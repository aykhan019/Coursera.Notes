

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGBG2SRD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4YWURTsYur7tzfBXKCoPma3Wc15q2sgam64JcTsS18QIhAP6ZyGN%2Fdhk6q6gNef71i2tEPch8UH8PmTc19Gi1EVapKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRR7cWRwEytZFxqiwq3AMG6plfCJRNfxhrZ%2BiNTapfaz6jeE6GSVdM7g2HluU6yEHk%2Bgb%2BjUitkMEvbBBn3gw0OQ77Csg%2FBB1rEGRLmuJMgy2VlHcyuCeN4tl3sKm62aBYKtKH7Fq4jLyokPhchnQdJc72Q4HXrb74yZ4fUGK0qGytBfOTyrBIzF9nwIzNYgXKPSBOd3JsZtLIQJq%2FSlRlB4RYrmh1gGCebFFAndhulVw1vuEE3zvcQEF%2FTpxahDcTss1Vx3mUVA%2Bgt9qcdeMs81oRBmLVJCYS%2FyOoKkstJLR5%2FaoAU2o5tMS1RKxdzKOv8u45xU%2BcDxpB4FQ8b6gECg6azdg7TCweDeC25%2FkJ14aByQHukPSilAfTCOijJ6oiHMmMztG8w322%2FqebPLf80F37jFTbu8%2F%2BGnSSC6pe%2BEkcU1WuG3QiMzbDfxpnuIzY%2FqOuqLmrJlE%2B624%2B3W9CjK5H%2BkCsMHPvOJdCb6fMZnpMxnhbPAVEuwmf5GLwM0pmzFa0%2BeCmoKH5S96YSIPEuJZWKB4zfnjExoApcHDlWHj2Sph64sfPC3ovZt0wseQznMjUp9IpJ0RO80MRTFe93dEE7TIL5MhLVOdD3bkIHmvQ4aQnWEdSim7PHSo%2BisVIC7zc4AQY4IvM3zDK9vm8BjqkAS1q0TfxRmpGt5BOGArd97ol133fRCTf24F6BNKjYND8xrzawxvMl02IrGFjQn%2FkwNvV9lsQzQ5PA8pc9wJTSINFMZGnre3oOKF57OiN3MBsdmsFwGv5oGkbTd3ioeknnrBzB5tafslsCVuyMCXBFkazkazw9MR44rr8FD5LcXtBg7KE6hSfDhAszAR7Q5Ts%2Bb%2FI6VlEPNYZWrGvX0Klf%2BgWbjs8&X-Amz-Signature=47c651f8a16d9f86933ab3196c6970ebae9bea86138bc91b226544bf45a0b498&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGBG2SRD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4YWURTsYur7tzfBXKCoPma3Wc15q2sgam64JcTsS18QIhAP6ZyGN%2Fdhk6q6gNef71i2tEPch8UH8PmTc19Gi1EVapKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRR7cWRwEytZFxqiwq3AMG6plfCJRNfxhrZ%2BiNTapfaz6jeE6GSVdM7g2HluU6yEHk%2Bgb%2BjUitkMEvbBBn3gw0OQ77Csg%2FBB1rEGRLmuJMgy2VlHcyuCeN4tl3sKm62aBYKtKH7Fq4jLyokPhchnQdJc72Q4HXrb74yZ4fUGK0qGytBfOTyrBIzF9nwIzNYgXKPSBOd3JsZtLIQJq%2FSlRlB4RYrmh1gGCebFFAndhulVw1vuEE3zvcQEF%2FTpxahDcTss1Vx3mUVA%2Bgt9qcdeMs81oRBmLVJCYS%2FyOoKkstJLR5%2FaoAU2o5tMS1RKxdzKOv8u45xU%2BcDxpB4FQ8b6gECg6azdg7TCweDeC25%2FkJ14aByQHukPSilAfTCOijJ6oiHMmMztG8w322%2FqebPLf80F37jFTbu8%2F%2BGnSSC6pe%2BEkcU1WuG3QiMzbDfxpnuIzY%2FqOuqLmrJlE%2B624%2B3W9CjK5H%2BkCsMHPvOJdCb6fMZnpMxnhbPAVEuwmf5GLwM0pmzFa0%2BeCmoKH5S96YSIPEuJZWKB4zfnjExoApcHDlWHj2Sph64sfPC3ovZt0wseQznMjUp9IpJ0RO80MRTFe93dEE7TIL5MhLVOdD3bkIHmvQ4aQnWEdSim7PHSo%2BisVIC7zc4AQY4IvM3zDK9vm8BjqkAS1q0TfxRmpGt5BOGArd97ol133fRCTf24F6BNKjYND8xrzawxvMl02IrGFjQn%2FkwNvV9lsQzQ5PA8pc9wJTSINFMZGnre3oOKF57OiN3MBsdmsFwGv5oGkbTd3ioeknnrBzB5tafslsCVuyMCXBFkazkazw9MR44rr8FD5LcXtBg7KE6hSfDhAszAR7Q5Ts%2Bb%2FI6VlEPNYZWrGvX0Klf%2BgWbjs8&X-Amz-Signature=2e9674f2e93b688df9549b0994d087cd131b8e16419ca528a26a73d8b9d7df0f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Applications
#### Business Use Cases
- Churn detection
- Customer segmentation
- Response prediction
#### Industries
- Email filtering
- Speech and handwriting recognition
- Biometric identification
### Common Classification Algorithms
- K-Nearest Neighbors (KNN)
- Decision Trees
- Logistic Regression
- Support Vector Machines (SVM)
- Neural Networks
- Naive Bayes
- SoftMax Regression
- One-vs-All (One-vs-Rest)
- One-vs-One
___
## K-Nearest Neighbors (KNN) Algorithm
### Overview
The **K-Nearest Neighbors (KNN)** algorithm is a supervised learning classification technique used to classify a data point based on how its neighbors are classified. It is based on the concept that data points that are close to each other are more likely to belong to the same class. KNN can also be used for regression tasks.
### Example Scenario
Consider a telecommunications provider that has segmented its customer base into four groups based on service usage patterns. The goal is to predict which group a new customer belongs to using demographic data such as age and income. This is a classification problem, where the goal is to assign a class label to a new, unknown case based on the known labels of other cases.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGBG2SRD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4YWURTsYur7tzfBXKCoPma3Wc15q2sgam64JcTsS18QIhAP6ZyGN%2Fdhk6q6gNef71i2tEPch8UH8PmTc19Gi1EVapKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRR7cWRwEytZFxqiwq3AMG6plfCJRNfxhrZ%2BiNTapfaz6jeE6GSVdM7g2HluU6yEHk%2Bgb%2BjUitkMEvbBBn3gw0OQ77Csg%2FBB1rEGRLmuJMgy2VlHcyuCeN4tl3sKm62aBYKtKH7Fq4jLyokPhchnQdJc72Q4HXrb74yZ4fUGK0qGytBfOTyrBIzF9nwIzNYgXKPSBOd3JsZtLIQJq%2FSlRlB4RYrmh1gGCebFFAndhulVw1vuEE3zvcQEF%2FTpxahDcTss1Vx3mUVA%2Bgt9qcdeMs81oRBmLVJCYS%2FyOoKkstJLR5%2FaoAU2o5tMS1RKxdzKOv8u45xU%2BcDxpB4FQ8b6gECg6azdg7TCweDeC25%2FkJ14aByQHukPSilAfTCOijJ6oiHMmMztG8w322%2FqebPLf80F37jFTbu8%2F%2BGnSSC6pe%2BEkcU1WuG3QiMzbDfxpnuIzY%2FqOuqLmrJlE%2B624%2B3W9CjK5H%2BkCsMHPvOJdCb6fMZnpMxnhbPAVEuwmf5GLwM0pmzFa0%2BeCmoKH5S96YSIPEuJZWKB4zfnjExoApcHDlWHj2Sph64sfPC3ovZt0wseQznMjUp9IpJ0RO80MRTFe93dEE7TIL5MhLVOdD3bkIHmvQ4aQnWEdSim7PHSo%2BisVIC7zc4AQY4IvM3zDK9vm8BjqkAS1q0TfxRmpGt5BOGArd97ol133fRCTf24F6BNKjYND8xrzawxvMl02IrGFjQn%2FkwNvV9lsQzQ5PA8pc9wJTSINFMZGnre3oOKF57OiN3MBsdmsFwGv5oGkbTd3ioeknnrBzB5tafslsCVuyMCXBFkazkazw9MR44rr8FD5LcXtBg7KE6hSfDhAszAR7Q5Ts%2Bb%2FI6VlEPNYZWrGvX0Klf%2BgWbjs8&X-Amz-Signature=d9f3c05b9c79e78b676255abb4f837200249f63308acec9cb01236720265c93e&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPVPUT24%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAHHL0hcFxmOAA7UohRcTkXZVbPZ6SJNdnr4kju0Lg6JAiEAiBn8l051P8j4AR%2FNQG2UmdBaCCrPIikSu5FVs1BgMcQqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOBDbisVlZ3KXYLctircA3F8rEKYsQiktcDY3qKg3Yl7qrZzQnpHif7iBOHtKQziIbyGnOtXcv56XC%2FvUWga2cGEe6B11o2XicwZUkN9buhDO7z0TLQjDeHbX5usdn%2B64L3s7a2OY808CX6QZeNJ2Pjmbpdj4UGL%2FpuJvbRmZWKmp5qcft7bDoVkNuheUMHm4loICrqD7XdjfqUlN7pGi%2BwA2fjgsbqTiyKF1nuT5FVIHT7IobBvXGyamAWR6wEmrMcF5cwnaeZE21B5EpS9nUltxQ6rOXt0Q0ob4V4QacYFuzBvzOFQ8jS2jFa1sVNZFcdIt7QvGiPnjyFy6Uk7TU6EZBpFngFh5YfP9uJr285bL3cAMS4EYTRtDahlZLSJTYGejaR9uGyZRKVTUvnhH%2BPj4%2BDJOj0%2FJ1KxTt7rr%2FxP%2FXARws2LI2nLjkG%2F%2FjydtFqgZIyzKqRg%2ByPUamY0Lrk2ZCmj1rjlVMXUCdYZ7NCf%2FqbuWHiU%2BaEanun0yUuMWsGrRLPW7BwzhsKsmytjACINs2RxUlFvAs%2FO2o%2FhJ4aiXC0%2BhnOoY6wbpxbdmyVRp6uYPWzakeLyr7rpTypN9tAWTvKyrEs4amDoU6EoxQHjqBkRRW94HbISP2iXOaD37C%2Fn7r%2BUnhMnV%2B%2FOMNX2%2BbwGOqUBvPOLr9jfXQLcdsAZS6uYp6xhQQq0Rl0vqFmwUgBH3ne1OwqJePXh7lRaznyS%2BeyEIHfF9xWcF%2FhtcIfeloimC9ulqDTFoNqFgE2QLMxhww6U9vNySdrtbLY6c%2Bozi6GRrgsRyPjrVArDlK%2BJWnaKHJTTKZCqf5lOQ6pm3oHM9X1yfYJLK9lBmmYiov56E%2FeGZyqsUJS2AblUuc8EWiYay14ipwY2&X-Amz-Signature=b11dc58e1794b7c13fe4700dfdc9247c0ba52d786709f0860748d122c0e9ecc5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPVPUT24%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAHHL0hcFxmOAA7UohRcTkXZVbPZ6SJNdnr4kju0Lg6JAiEAiBn8l051P8j4AR%2FNQG2UmdBaCCrPIikSu5FVs1BgMcQqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOBDbisVlZ3KXYLctircA3F8rEKYsQiktcDY3qKg3Yl7qrZzQnpHif7iBOHtKQziIbyGnOtXcv56XC%2FvUWga2cGEe6B11o2XicwZUkN9buhDO7z0TLQjDeHbX5usdn%2B64L3s7a2OY808CX6QZeNJ2Pjmbpdj4UGL%2FpuJvbRmZWKmp5qcft7bDoVkNuheUMHm4loICrqD7XdjfqUlN7pGi%2BwA2fjgsbqTiyKF1nuT5FVIHT7IobBvXGyamAWR6wEmrMcF5cwnaeZE21B5EpS9nUltxQ6rOXt0Q0ob4V4QacYFuzBvzOFQ8jS2jFa1sVNZFcdIt7QvGiPnjyFy6Uk7TU6EZBpFngFh5YfP9uJr285bL3cAMS4EYTRtDahlZLSJTYGejaR9uGyZRKVTUvnhH%2BPj4%2BDJOj0%2FJ1KxTt7rr%2FxP%2FXARws2LI2nLjkG%2F%2FjydtFqgZIyzKqRg%2ByPUamY0Lrk2ZCmj1rjlVMXUCdYZ7NCf%2FqbuWHiU%2BaEanun0yUuMWsGrRLPW7BwzhsKsmytjACINs2RxUlFvAs%2FO2o%2FhJ4aiXC0%2BhnOoY6wbpxbdmyVRp6uYPWzakeLyr7rpTypN9tAWTvKyrEs4amDoU6EoxQHjqBkRRW94HbISP2iXOaD37C%2Fn7r%2BUnhMnV%2B%2FOMNX2%2BbwGOqUBvPOLr9jfXQLcdsAZS6uYp6xhQQq0Rl0vqFmwUgBH3ne1OwqJePXh7lRaznyS%2BeyEIHfF9xWcF%2FhtcIfeloimC9ulqDTFoNqFgE2QLMxhww6U9vNySdrtbLY6c%2Bozi6GRrgsRyPjrVArDlK%2BJWnaKHJTTKZCqf5lOQ6pm3oHM9X1yfYJLK9lBmmYiov56E%2FeGZyqsUJS2AblUuc8EWiYay14ipwY2&X-Amz-Signature=5012c2c476ef34d78b839c439c4adbe70ba4b0bca7e292ebfc1a784851a114e7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Example Code for KNN:
```python
from sklearn.neighbors import KNeighborsClassifier

# Training data
X_train = df[['Age', 'Income']]
y_train = df['Customer Group']

# New customer data
new_customer = [[30, 55000]]

# Initialize KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Fit the model
knn.fit(X_train, y_train)

# Predict the class of the new customer
predicted_class = knn.predict(new_customer)
print(f'Predicted Customer Group: {predicted_class[0]}')
```
### Choosing the Value of K
- **Small K**: A small value of K (e.g., K=1) might lead to a model that is too specific, potentially capturing noise and outliers. This can result in overfitting, where the model performs well on the training data but poorly on unseen data.
- **Large K**: A large value of K (e.g., K=20) might make the model too generalized, leading to underfitting, where the model is too simple and fails to capture important patterns in the data.
### Finding the Optimal K
To find the optimal value of K:
5. Reserve a portion of your data for testing.
6. Train the model using the training data and evaluate its accuracy on the test data for different values of K.
7. Choose the value of K that results in the highest accuracy.
### Example of Choosing K:
```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2)

# Evaluate different values of K
accuracies = []
for k in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracies.append(accuracy_score(y_test, y_pred))

best_k = accuracies.index(max(accuracies)) + 1
print(f'Best K: {best_k}')
```
### Regression with KNN
KNN can also be used for regression tasks. In this case, instead of assigning a class label, the algorithm predicts a continuous value (e.g., the price of a house). The predicted value is typically the average or median of the K nearest neighbors' values.
#### Example of KNN Regression
- **Scenario**: Predicting the price of a house based on features such as the number of rooms, square footage, and the year it was built.
- **Process**: The algorithm finds the K nearest houses (based on the features) and predicts the price of the new house as the average or median of the prices of these K neighbors.
### Summary
The KNN algorithm is a simple yet powerful tool for both classification and regression tasks. Its effectiveness depends on the choice of K and the distance metric used. The main challenge lies in finding the right balance between underfitting and overfitting by selecting an appropriate value of K.
___
## Evaluation Metrics for Classifiers
Model evaluation metrics are essential in determining the performance of a classifier. These metrics provide insights into areas where the model might require improvement. In this note, we will explore three evaluation metrics for classification: Jaccard index, F1 score, and Log Loss.
### 1. Jaccard Index
#### Definition
The **Jaccard index** (also known as the Jaccard similarity coefficient) measures the similarity between the actual labels and the predicted labels by the model. It is calculated as the size of the intersection divided by the size of the union of the two label sets.
#### Formula
Given that `y` represents the true labels and `ŷ` represents the predicted labels:
$$ \text{Jaccard Index} = \frac{|y \cap \hat{y}|}{|y \cup \hat{y}|} $$
#### Example
For a test set of size 10 with 8 correct predictions (8 intersections):
$$ \text{Jaccard Index} = \frac{8}{10 + (10 - 8)} = 0.6 $$
#### Interpretation
- A Jaccard index of 1.0 indicates a perfect match between predicted and true labels.
- A value closer to 0 indicates a poor match.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGBG2SRD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4YWURTsYur7tzfBXKCoPma3Wc15q2sgam64JcTsS18QIhAP6ZyGN%2Fdhk6q6gNef71i2tEPch8UH8PmTc19Gi1EVapKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRR7cWRwEytZFxqiwq3AMG6plfCJRNfxhrZ%2BiNTapfaz6jeE6GSVdM7g2HluU6yEHk%2Bgb%2BjUitkMEvbBBn3gw0OQ77Csg%2FBB1rEGRLmuJMgy2VlHcyuCeN4tl3sKm62aBYKtKH7Fq4jLyokPhchnQdJc72Q4HXrb74yZ4fUGK0qGytBfOTyrBIzF9nwIzNYgXKPSBOd3JsZtLIQJq%2FSlRlB4RYrmh1gGCebFFAndhulVw1vuEE3zvcQEF%2FTpxahDcTss1Vx3mUVA%2Bgt9qcdeMs81oRBmLVJCYS%2FyOoKkstJLR5%2FaoAU2o5tMS1RKxdzKOv8u45xU%2BcDxpB4FQ8b6gECg6azdg7TCweDeC25%2FkJ14aByQHukPSilAfTCOijJ6oiHMmMztG8w322%2FqebPLf80F37jFTbu8%2F%2BGnSSC6pe%2BEkcU1WuG3QiMzbDfxpnuIzY%2FqOuqLmrJlE%2B624%2B3W9CjK5H%2BkCsMHPvOJdCb6fMZnpMxnhbPAVEuwmf5GLwM0pmzFa0%2BeCmoKH5S96YSIPEuJZWKB4zfnjExoApcHDlWHj2Sph64sfPC3ovZt0wseQznMjUp9IpJ0RO80MRTFe93dEE7TIL5MhLVOdD3bkIHmvQ4aQnWEdSim7PHSo%2BisVIC7zc4AQY4IvM3zDK9vm8BjqkAS1q0TfxRmpGt5BOGArd97ol133fRCTf24F6BNKjYND8xrzawxvMl02IrGFjQn%2FkwNvV9lsQzQ5PA8pc9wJTSINFMZGnre3oOKF57OiN3MBsdmsFwGv5oGkbTd3ioeknnrBzB5tafslsCVuyMCXBFkazkazw9MR44rr8FD5LcXtBg7KE6hSfDhAszAR7Q5Ts%2Bb%2FI6VlEPNYZWrGvX0Klf%2BgWbjs8&X-Amz-Signature=3a07cc0ff6f7ce478a77843dd2fcb0bcec70bb95ed57affa77358e944431de9c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Code Example
```python
from sklearn.metrics import jaccard_score

# True labels
y_true = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1]

# Predicted labels
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

# Compute Jaccard Index
jaccard = jaccard_score(y_true, y_pred)
print("Jaccard Index:", jaccard)
```
### 2. Confusion Matrix
#### Definition
A **confusion matrix** is a table that is often used to describe the performance of a classification model on a set of test data for which the true values are known. Each row of the matrix represents the actual instances in a predicted class, while each column represents the instances in an actual class.
#### Example
Consider a confusion matrix for a binary classification with 40 rows:

||Predicted: No (0)|Predicted: Yes (1)|
|