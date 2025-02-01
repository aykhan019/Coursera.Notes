

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=43072e09f499a0039926fa1b1c551c2424efc7944e52ad9a182ef7ccab90b752&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=d733c9a46c393e0fa69b2e0714467ab90444f5e64a634c07d67e99459cb26edf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=a3158b93bf48d6b6701de06e8ee390f10c054dcb2ee901aae506074444020128&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=51c6346152890ea5583e85ef38f0cc00878e0f654e6d889036675ad61e03c58b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=c444e50ac6d625aca0a7f3a3f182b4baa9c5bdc2c44db0a318ad0a6510ac84cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=3eabc6115f43220d68d8cbcc04d833ecd0539bafe0b1052416a350504659c54c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=320062f420039b983eb7644e20b24295534e53bdefed4b5c84500e8c8046dbf4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=fd90bb188542dcda96cd174ef2786bc899e3d0d931e8dbc6e033ee79ab945734&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=9c722d7d7f8efd42017a3c6bc840b39efc115d55e48575de23773a82e765bd45&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627PRAB7P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsNQxxEu6DaNo2VqhHc61y9GJ%2FiPBDY9WihJT9gE4f1wIgLPMv5S%2BlOrO3rCnHVPdFM8GhG3iNsTwVbG2CCB5A%2F5UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPnuF5DcvxkyMNKThyrcA8kGz1yHpFbfOmfpdFkYHMgTnf64IOErV9SDatxyuIqvxs4uBnr%2F%2B06nxufFbD2I3%2BO0l12t0lW0j0vbA%2FBzCRdnLAR4W3A9REyL8TbtnTp74CB2lLECqS3LnG3C0%2Bsql%2B0E2XEJNaXWT95tf%2B0ZcK2LsWykSYCYHw%2B8JlBFK7jIa%2FasZ5G2zUCvC5jvGPmWIXMQEgGKcu1udbsSr2WoVc1ZBpYZIs2R%2FklsdT6OdAmuK4mk942uNSJj3MjAQ9%2F0EgvyG2DA4ZJy43w2y2XEssBCxb%2FQEA53zmN3kB0k%2B%2B%2F%2FMf1E3ux55Nk8Ggz8cVJOYINy8NfTCsWmhgcL9%2BE%2BosbfrrdU3HUip1BaC7VVYkibMnX7DfLAxbxPmtNet9K%2B7hb%2B%2BjkuEB4xnHa9OHDaZB4ahS6D3hWjjKTII2dYZFtNTjJzqsJ2U2BokaM9avHk6c7wMAwtc6YRyLtIwPkjBEIR9NervGhC1xbjlNvtzg2nOQcF7Q6Qq2t4fVcPZ7vldSuiffXS7wdxU42x8wUVLoAzJOCcZhIUnk0LRno2ZcIL%2BT2rl1mhDKO5bDSWfeeftB926aknkvKMFx6xIUgN984avA8mUrQ5dr693zSR4Iz3UoA2c6W4FDj4OVYCMJml97wGOqUBnocBizRL1I8kDU8CIstu1DW0IhrZl7bq1vRmKUexQt8JPhRbXWfPAzUXovMeX0SYxghSFjUCOJ%2Fh8eHGAOP9zKfVh9jiTX5853X%2BdwlnkVzG%2BwsyOy4Oun0NJvbjW19fRK66e4OqPg4V7BPN6WJBvmvmYWxsxdmLrkLx8baNf9sRZbyV5FRGC%2BLgZkRv4xcnCrK670jlFp3PctNCuXGNvp9UGVzV&X-Amz-Signature=c68e5168433c182ed16c321a9916490b7c588e96781365cf006235095fc48564&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627PRAB7P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsNQxxEu6DaNo2VqhHc61y9GJ%2FiPBDY9WihJT9gE4f1wIgLPMv5S%2BlOrO3rCnHVPdFM8GhG3iNsTwVbG2CCB5A%2F5UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPnuF5DcvxkyMNKThyrcA8kGz1yHpFbfOmfpdFkYHMgTnf64IOErV9SDatxyuIqvxs4uBnr%2F%2B06nxufFbD2I3%2BO0l12t0lW0j0vbA%2FBzCRdnLAR4W3A9REyL8TbtnTp74CB2lLECqS3LnG3C0%2Bsql%2B0E2XEJNaXWT95tf%2B0ZcK2LsWykSYCYHw%2B8JlBFK7jIa%2FasZ5G2zUCvC5jvGPmWIXMQEgGKcu1udbsSr2WoVc1ZBpYZIs2R%2FklsdT6OdAmuK4mk942uNSJj3MjAQ9%2F0EgvyG2DA4ZJy43w2y2XEssBCxb%2FQEA53zmN3kB0k%2B%2B%2F%2FMf1E3ux55Nk8Ggz8cVJOYINy8NfTCsWmhgcL9%2BE%2BosbfrrdU3HUip1BaC7VVYkibMnX7DfLAxbxPmtNet9K%2B7hb%2B%2BjkuEB4xnHa9OHDaZB4ahS6D3hWjjKTII2dYZFtNTjJzqsJ2U2BokaM9avHk6c7wMAwtc6YRyLtIwPkjBEIR9NervGhC1xbjlNvtzg2nOQcF7Q6Qq2t4fVcPZ7vldSuiffXS7wdxU42x8wUVLoAzJOCcZhIUnk0LRno2ZcIL%2BT2rl1mhDKO5bDSWfeeftB926aknkvKMFx6xIUgN984avA8mUrQ5dr693zSR4Iz3UoA2c6W4FDj4OVYCMJml97wGOqUBnocBizRL1I8kDU8CIstu1DW0IhrZl7bq1vRmKUexQt8JPhRbXWfPAzUXovMeX0SYxghSFjUCOJ%2Fh8eHGAOP9zKfVh9jiTX5853X%2BdwlnkVzG%2BwsyOy4Oun0NJvbjW19fRK66e4OqPg4V7BPN6WJBvmvmYWxsxdmLrkLx8baNf9sRZbyV5FRGC%2BLgZkRv4xcnCrK670jlFp3PctNCuXGNvp9UGVzV&X-Amz-Signature=f49992cd03f705618c0899708918c4cb982b09ddeef3b62e59f15e37558a023b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627PRAB7P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsNQxxEu6DaNo2VqhHc61y9GJ%2FiPBDY9WihJT9gE4f1wIgLPMv5S%2BlOrO3rCnHVPdFM8GhG3iNsTwVbG2CCB5A%2F5UqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPnuF5DcvxkyMNKThyrcA8kGz1yHpFbfOmfpdFkYHMgTnf64IOErV9SDatxyuIqvxs4uBnr%2F%2B06nxufFbD2I3%2BO0l12t0lW0j0vbA%2FBzCRdnLAR4W3A9REyL8TbtnTp74CB2lLECqS3LnG3C0%2Bsql%2B0E2XEJNaXWT95tf%2B0ZcK2LsWykSYCYHw%2B8JlBFK7jIa%2FasZ5G2zUCvC5jvGPmWIXMQEgGKcu1udbsSr2WoVc1ZBpYZIs2R%2FklsdT6OdAmuK4mk942uNSJj3MjAQ9%2F0EgvyG2DA4ZJy43w2y2XEssBCxb%2FQEA53zmN3kB0k%2B%2B%2F%2FMf1E3ux55Nk8Ggz8cVJOYINy8NfTCsWmhgcL9%2BE%2BosbfrrdU3HUip1BaC7VVYkibMnX7DfLAxbxPmtNet9K%2B7hb%2B%2BjkuEB4xnHa9OHDaZB4ahS6D3hWjjKTII2dYZFtNTjJzqsJ2U2BokaM9avHk6c7wMAwtc6YRyLtIwPkjBEIR9NervGhC1xbjlNvtzg2nOQcF7Q6Qq2t4fVcPZ7vldSuiffXS7wdxU42x8wUVLoAzJOCcZhIUnk0LRno2ZcIL%2BT2rl1mhDKO5bDSWfeeftB926aknkvKMFx6xIUgN984avA8mUrQ5dr693zSR4Iz3UoA2c6W4FDj4OVYCMJml97wGOqUBnocBizRL1I8kDU8CIstu1DW0IhrZl7bq1vRmKUexQt8JPhRbXWfPAzUXovMeX0SYxghSFjUCOJ%2Fh8eHGAOP9zKfVh9jiTX5853X%2BdwlnkVzG%2BwsyOy4Oun0NJvbjW19fRK66e4OqPg4V7BPN6WJBvmvmYWxsxdmLrkLx8baNf9sRZbyV5FRGC%2BLgZkRv4xcnCrK670jlFp3PctNCuXGNvp9UGVzV&X-Amz-Signature=dd245fe92fa88e3b672e6a09edcfd7b029e9e0025062e675da00fa73c015e4a5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=d496fff43a5d0af82ef1ff698a147f680b10569ac223da5315b28a394977665b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=b5a56f8131824c7043d41582e17a95b27dcf7fd5f0072cf4ee045abe63c96d95&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=b0c5c625beaeba073c015703d7707ad1ccbcf6ce9aad9b28d6e2881c9088eef9&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=674a14a15954e2358ba7505f51964bc19f071d0a1d79d52cd31f9c7948615cbb&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=d8ca3f4b97bb988347216838222b021271473c1d00dafe1f62ddab7ae7f24c8e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5YNTZ6N%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCguDAlVEOk6mVgX0%2FGv3AqEIzY1Hh5A%2FDMdML4zqLpRAIhAKQ9hEozOZihIysuAxmkdD6qhqvAUtA5vmEUQxp5QrpVKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKLTbTQzH0mNrUY34q3AOV9ISZXeaw%2Ba%2BmMg7Y0dm6lbU8CGaw%2Fyr87q6xLLJ1l2dtdvdhtiMhG49BEPwYBxv77t9HxaEMSO7fw0FmGx6B4Hx52uKxK2LMYJzZddbbXlwN5RZkGMQQxzkNZDg8PgQJB%2BPb1fQOIfacCNnvimAKKxztw8H4NinMk0X0jB5%2Bh9FAC%2BH%2B3RANdba0rHX65BT1lGh7LDlwJO2o7u92Y4hVsw%2FC28Lj21BiwZMww5AUpvE60RbRdtHi%2FwiE9S3N00wC27sNdJt6lTWf8F5ptxnb%2FA07qGmi066TLHTLzZOt4A82QfQZ4ozL7EhWCAXb5mPvFwtL6l0W1m2kz4Plh7k0QcdL6gpAtjaanR6uA%2Bh8jEtijshDMs1KN9HuJHwTrF1cKa%2FRelp7msWEtB9ETmjl%2Fw54DE4nsbmb3zPcDr3lIgvXsyywQ7m%2FryPvjN7ytJixkiuJavrOUBKBxwiPEla1wIIi4TwbG%2FkLpvjZCwGK2Ihr6nnWDPYbF2602zdTsZqj6jqV9WL%2BjyVkAy7r6ADXKMtPiBSZEyfAPXZ4%2BwOwnb0C%2BmFrmo3krtaCPfCLbE2nvFnSVia5SYG9wShWgsIwv%2F2ckkxcQMmfvOZePQfngtv%2Bl8rv%2F6gLlK7IJjDJpPe8BjqkAbb1YqnSk4wwMdp%2FfOeqAyPA8POotUGoSKJ5faU8T9T%2B9VwWzUb3NRK7k4GXcH74XEdy7850KI1SMPMOJiVLmrZt8n%2Fu8dL8PDY9SIsoMV9%2Fdpm0zxXDsjhlWAiYtgWTXO7SlejaS3JedZ9%2FMsnDlvcwzj3j%2FqHcytCDiTuRzYS34r6CTeO8LtzhCIjh8qvrbR81IILAvNwOdbxyyJ24Bs8pOvSe&X-Amz-Signature=279f3cbdcf66d983a70bd690fc50221b60a850fe56b91145bb1395628309e127&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR44MFAX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDqbY73Gn5JoYBvuSn7wlUPCXneLfBonopt07wpvO98DAiEAi9SSjkpf4DnPhUowC09UsM0uhZhv7c%2Fk12plxHYJ%2FCAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGNZmXBf%2BZBxBJwFfircA1OYUpt%2FCvH1kHK4O0D8lF3M%2BdGEDW8EhTD4zhKLOvc53nzmhU61XnyVWN%2BxT4HHAcxqJnaq7ZzAzZRHNXcCS471PRmeNQW50fIK92THpBTnAK0n%2BHGn7h7fILHzIaDmiRYPdc0ao3XVqYAUn1peI82Y4N5%2FjAT6c5%2F6iAVR1hFb7X%2B2SqPLM3blS0joXApPAWfwsxL4PntIbLtVTXGP9uYt1mOdrJoxWnFHTm6ZbgZ28HPR%2FO6S3JrOkR0jQXQXh%2FhDqoGJWuZD4TkhXIDD5tKY%2BdnD2F52731fRZ9gxc0weaRS0yx886sIbxphYObuDyCBhJyIAo6QLZThRwbTiq0eLHZm76lfIwlCXqOHdQJ6BixK3YTrkUuaSWjeX4%2BniJh64UnP%2FMO9lLQodrXgnddSkx5NVthW5WRTMVCWW8h7jM%2Bek3E5X0KIkYtWHkxhLCcc4xrT%2B%2BSDYyjSCVaew%2FwZhuNR2IUD%2FNI%2BtPvx1WVBhGxOLb%2FZFyFZHsOU9WynWoFalp9cKUy5IB4SOxMYgJHYYIjLus2P7lw0CxYvav4LiNxQmcC2J50S%2F%2FwQ%2B5cdo8cY3GyL1Mm8Kjx%2FV3Zd0FPovUlEAqke%2FOF5k7VunOJK1IBBf9lEc59P%2F935MKqk97wGOqUBXTQrvudvwebfh%2FEYtUAyOZzTLYfIJS7WvkAn3F%2FOTahJD3S16eiiNzIRt%2F6%2FFDg7GkoW45AXhQQsEOLxy9jgSLMWpaQuG54KBVluIxUAcnQXhluy1cL0usW84sbXFxu%2BbcfHbVJGZkQbkxhZqpSyKYZCT8bbS%2Bt99uG2NhjNJESMwPdfEIwAraARNjoiax1XoqqWGrvNf8ntlpuOHvtUax%2FvQFmW&X-Amz-Signature=ba15723e4592f24d22caa09d1dc266ac39bff15ab3186818d301e761f79cb58e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR44MFAX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDqbY73Gn5JoYBvuSn7wlUPCXneLfBonopt07wpvO98DAiEAi9SSjkpf4DnPhUowC09UsM0uhZhv7c%2Fk12plxHYJ%2FCAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGNZmXBf%2BZBxBJwFfircA1OYUpt%2FCvH1kHK4O0D8lF3M%2BdGEDW8EhTD4zhKLOvc53nzmhU61XnyVWN%2BxT4HHAcxqJnaq7ZzAzZRHNXcCS471PRmeNQW50fIK92THpBTnAK0n%2BHGn7h7fILHzIaDmiRYPdc0ao3XVqYAUn1peI82Y4N5%2FjAT6c5%2F6iAVR1hFb7X%2B2SqPLM3blS0joXApPAWfwsxL4PntIbLtVTXGP9uYt1mOdrJoxWnFHTm6ZbgZ28HPR%2FO6S3JrOkR0jQXQXh%2FhDqoGJWuZD4TkhXIDD5tKY%2BdnD2F52731fRZ9gxc0weaRS0yx886sIbxphYObuDyCBhJyIAo6QLZThRwbTiq0eLHZm76lfIwlCXqOHdQJ6BixK3YTrkUuaSWjeX4%2BniJh64UnP%2FMO9lLQodrXgnddSkx5NVthW5WRTMVCWW8h7jM%2Bek3E5X0KIkYtWHkxhLCcc4xrT%2B%2BSDYyjSCVaew%2FwZhuNR2IUD%2FNI%2BtPvx1WVBhGxOLb%2FZFyFZHsOU9WynWoFalp9cKUy5IB4SOxMYgJHYYIjLus2P7lw0CxYvav4LiNxQmcC2J50S%2F%2FwQ%2B5cdo8cY3GyL1Mm8Kjx%2FV3Zd0FPovUlEAqke%2FOF5k7VunOJK1IBBf9lEc59P%2F935MKqk97wGOqUBXTQrvudvwebfh%2FEYtUAyOZzTLYfIJS7WvkAn3F%2FOTahJD3S16eiiNzIRt%2F6%2FFDg7GkoW45AXhQQsEOLxy9jgSLMWpaQuG54KBVluIxUAcnQXhluy1cL0usW84sbXFxu%2BbcfHbVJGZkQbkxhZqpSyKYZCT8bbS%2Bt99uG2NhjNJESMwPdfEIwAraARNjoiax1XoqqWGrvNf8ntlpuOHvtUax%2FvQFmW&X-Amz-Signature=7adead83a8826f98a10be3fa0808c8cc5158a871e164e01c2cf484c075e7faf9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTTSDWLV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDNI7abEpVsMltbStWL6UHXIwShFnWLYZawjLY5obM43wIgXBw%2FcBpknpLuugbj7gofylb3Re%2BXhtvhdqfMu07oxKkqiAQI0v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK4H8FG4qyYbkE5TiSrcA%2FX4TRrRwhvs6cxsL47rdtrVLuP2Q%2BSDjURLzeRCTiCyZwswtjQ6YPrrBwk61Yo64nFPiZshGTBte0sajyltyl3oNTIobcq0DkoeQTaBudAAVpswTzNXNPneVivTIpIF2kkrNBhUqZhsiqaZmqEJDN2xW34h9v9BP13B5v4FZm4nTeCF6IBk%2Ba1mpX8jWBfjl%2FronK%2B87HjSknq%2FY8%2FImhJ1TH2OSdxCGH7ZABJbKmry%2FEJqpFmwDWLM8%2BLfGO18BwPGzDWocPN7QCKQAfXwWXIAbWbKVeXGoCUCBA%2BAFw%2FHFKa6CqaE17esXduU396rBrJIBB8sR6mIeORkpD43%2BlrteZVdjrD7MM1kzWr%2FBjd1dYRsVLXaOKnyFxvsCS3P%2BO4tCChlHPZ6npbvS39NLffXZ9toJL0s2g2ZPZXccuuqTbGsnbVKMU9RFu2cHA6XzWH22latr4AUI4wNUtQClNpDKOqzLrrjYlfVL%2B%2BjgyaX95F1q1C5sBm5rlaApKcGd5BK5uAulPKowUMU%2BWk8QBArmyF%2F5kR%2FZKZmRuNsJEgRmHmeSG47HXpObACJbBDTE4UZz8I7TKndsDJND2R%2Fbt7%2BMqPFFjZwDCfavB%2BYGfUDIioIzVI73FwjYIPFMM7L97wGOqUBJEj8LtWH9QLNq1Fr8rGVZKklTjkW2vwykTQR7Z0Gs7J%2Bo%2BY%2F7rq%2FDLcxSpMPJdP1UKOSXOLdku0oL%2FiiQgNZdfWLSPPsRdVl%2Flm%2BaIb%2FlCBk8s7knooQJf17C63JEURkTqogyQJS7Ynkf46eOSAaNHferGqqkLEeB6%2FtZgeN1rIZK8xuJPQ7LANjVZ729wgih5Xvrpvc9vFCnTvbO0ueIExzeb8m&X-Amz-Signature=ed9d4cd81e765c117a62f3a44ae16e471c7346e47e1ae9a1bb3cd42e7821c1b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGAMV2G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4BJzOxjK6de3u1bv%2BcoT0CzwHs5%2B8gafc3JSfpqhA9AiEA3BJMGF7eTXHqBixxQ3EPTDkrZEU6BtAvRFoAE5%2FUZ9AqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6hih%2FNZorJoqdwwCrcAxOOLkHMoIrXSVCm2yzlCVEx3AhEr%2FTQtSE0UlfeKsm3ZF6AcfpTFk%2FdULczOwvXXKisEIkucXvC8TcUoKPtPVkdTagHCyUdkjOIfXnsozJEhEe5pm12K69FO2Qe0jt8xLWm0cKl6Miwf2pkNI8nWaKaM7p4chOuNWhaaEbfCQlS7I6NoD6Ef4aY5YIaib758K%2BHdISPcg1X96JC%2FY%2BcMFiHLzWz%2FMCD1LRdrGrCN9zZyBw3mjBGVKMP8yTYbVoj2iPORcHOeIatj43o6Wx11mVmWtjBUdFcCq1d6e2%2BmeSTt7NSWtl1sRhIWxmv2POHff87EwI5mQHF1Ag2Yc4IR0sI8mfBFFGX7SEkEdFLyvMFBN9MXMxex47uRNqx3j79hDFFZdiqRKxHVKdq5TmGWzN3M64ibPwed%2F9ppyusCV2vNeDAUNYlkW09droqZM8kc0xlw5SFDOd%2Bsz8oPmKeKNKoBwCoJddvqEF%2FFj%2B8gkYcKK9y0Y%2F%2Bj1uBVnwQ%2B%2BjZEhiR9GzJ1mBMcj08lNWVanE2iZXtzRps8hxP8f7ZeEenh7mv7KGNzml%2BZYbYpeNmA29sk24LqDJnpUxNPW1D%2BISWvPq3WhjicG8YRDD3OkHDBdx9hKkAILNSUl5EMOak97wGOqUB7rb7UqlyYt5axMfI5FQIKJVNKxR7qyh7Lvok3Jkadz2wOZ8avkttaQpUmTDbSAOiIG%2FvF8zSPr%2FNM9iWL%2BvUMpjsQd%2FK9CCWBI446mDh6M0ZlmxKoJzWbGUCEQQzIr%2BEuh9xjy9waFLFsR%2Fg9ZKhuJkBBKvBAG9EtfTv18oZivyC%2F%2BfwUasGV87I2Y18JeVGDVok%2BSX5Bnk0EPqMQzG9IsLxQQ09&X-Amz-Signature=48720a54eba3bb4f65e7afbebec679f6cea42b25f83363a74f754ad110325d47&X-Amz-SignedHeaders=host&x-id=GetObject)
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