

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBBBXOIP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDj9VwjOwF%2F%2Bit3GYxzrukCcMN8KCny5OvbudV3O2qChQIgJ437RxEJGTfVMRpzyErfk8y2gQknYOTtKo7FgMEJs20q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDA0xvzAskbWLbBDBYSrcAzI1N%2B541BDwYcNwEO%2BKq%2FuUcez5iLs650Aex3tImp%2Fp0fgfLyP%2F%2BwXcyhcF%2FW4syIo7Y4dxHRGqi6C9J3v%2FOoW0i0X8bQDF6iIkzAmh%2BWOKojUSs5f7jB43IpMPGd1%2FN3mmm0se%2F%2B4HabEyWgnQJVAOXogWschCqYemaJOYXcNnrFuyGGucYtlpAkez7uKLOfp6vHWX1xYat3iBvPnM%2FelpWUrHYmRE%2FEMeopEuQuhJVDA3nlGk9SEAZROUuWc84aaXeXIsICwHadJMx%2BFzohr%2BMdwWgfX%2BCeprZCzCrNsW%2B4UpWBghQ1EXKTvqDMHSjUTtlemh9pAQB49%2Flpu4mkX8gdOwpl%2Bx3BaaTIuK0pqDK9U2MzZQQKZjLUYJwLAOtdw5PSVUkAA%2BhjKJSR8o15RA3ZmEcVSoo6QlqKBtHjcSBDoq1Ct99oKczlYTn3wKf79NqFHIK1NK25PqDDao25PcMCzAir%2BUUpJtACMir9GHuxDl9gnO%2FvgYu5xxbHpyORQrShpLPv32ou8R%2Buti1MLlZJRtoJp5BX%2FHNlr%2BPUIKbqypMnQNOkjHGYHyRNNmS0bTkktj2RS1KBjX4zYek%2BVsS5zh1o5MarTkm%2FAT%2ByY3U6LK0v9qHoTgH%2BMPMPudk70GOqUBEKF0lt2PHffG9s2%2FrFXJE5Ps5UOqfTL3W0f4JIJzSztTU8hQCnA4y36895KHjDm%2FPsb2uP505U9IWdk2Wop8XybiibFptH0PpJ3pptkmwvftyJuhw2%2FLiS1xnEUWDnCCaXfs9tCZZmXEUBMwyg7dswbWE0hHIg8kjxTWqgCjQ3cdy3X08F9rD52dmOBpUj9vDeVpRW1FTmzvDafHBISrziBmucit&X-Amz-Signature=b6d91805e573f03f0a0b1c41746c1d06bb61d001a295e12b2cff241662e3af33&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBBBXOIP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDj9VwjOwF%2F%2Bit3GYxzrukCcMN8KCny5OvbudV3O2qChQIgJ437RxEJGTfVMRpzyErfk8y2gQknYOTtKo7FgMEJs20q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDA0xvzAskbWLbBDBYSrcAzI1N%2B541BDwYcNwEO%2BKq%2FuUcez5iLs650Aex3tImp%2Fp0fgfLyP%2F%2BwXcyhcF%2FW4syIo7Y4dxHRGqi6C9J3v%2FOoW0i0X8bQDF6iIkzAmh%2BWOKojUSs5f7jB43IpMPGd1%2FN3mmm0se%2F%2B4HabEyWgnQJVAOXogWschCqYemaJOYXcNnrFuyGGucYtlpAkez7uKLOfp6vHWX1xYat3iBvPnM%2FelpWUrHYmRE%2FEMeopEuQuhJVDA3nlGk9SEAZROUuWc84aaXeXIsICwHadJMx%2BFzohr%2BMdwWgfX%2BCeprZCzCrNsW%2B4UpWBghQ1EXKTvqDMHSjUTtlemh9pAQB49%2Flpu4mkX8gdOwpl%2Bx3BaaTIuK0pqDK9U2MzZQQKZjLUYJwLAOtdw5PSVUkAA%2BhjKJSR8o15RA3ZmEcVSoo6QlqKBtHjcSBDoq1Ct99oKczlYTn3wKf79NqFHIK1NK25PqDDao25PcMCzAir%2BUUpJtACMir9GHuxDl9gnO%2FvgYu5xxbHpyORQrShpLPv32ou8R%2Buti1MLlZJRtoJp5BX%2FHNlr%2BPUIKbqypMnQNOkjHGYHyRNNmS0bTkktj2RS1KBjX4zYek%2BVsS5zh1o5MarTkm%2FAT%2ByY3U6LK0v9qHoTgH%2BMPMPudk70GOqUBEKF0lt2PHffG9s2%2FrFXJE5Ps5UOqfTL3W0f4JIJzSztTU8hQCnA4y36895KHjDm%2FPsb2uP505U9IWdk2Wop8XybiibFptH0PpJ3pptkmwvftyJuhw2%2FLiS1xnEUWDnCCaXfs9tCZZmXEUBMwyg7dswbWE0hHIg8kjxTWqgCjQ3cdy3X08F9rD52dmOBpUj9vDeVpRW1FTmzvDafHBISrziBmucit&X-Amz-Signature=b250517fa8046a0c6651f3a092435af7fe26477ebde2f98f032aa81cccae59f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBBBXOIP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDj9VwjOwF%2F%2Bit3GYxzrukCcMN8KCny5OvbudV3O2qChQIgJ437RxEJGTfVMRpzyErfk8y2gQknYOTtKo7FgMEJs20q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDA0xvzAskbWLbBDBYSrcAzI1N%2B541BDwYcNwEO%2BKq%2FuUcez5iLs650Aex3tImp%2Fp0fgfLyP%2F%2BwXcyhcF%2FW4syIo7Y4dxHRGqi6C9J3v%2FOoW0i0X8bQDF6iIkzAmh%2BWOKojUSs5f7jB43IpMPGd1%2FN3mmm0se%2F%2B4HabEyWgnQJVAOXogWschCqYemaJOYXcNnrFuyGGucYtlpAkez7uKLOfp6vHWX1xYat3iBvPnM%2FelpWUrHYmRE%2FEMeopEuQuhJVDA3nlGk9SEAZROUuWc84aaXeXIsICwHadJMx%2BFzohr%2BMdwWgfX%2BCeprZCzCrNsW%2B4UpWBghQ1EXKTvqDMHSjUTtlemh9pAQB49%2Flpu4mkX8gdOwpl%2Bx3BaaTIuK0pqDK9U2MzZQQKZjLUYJwLAOtdw5PSVUkAA%2BhjKJSR8o15RA3ZmEcVSoo6QlqKBtHjcSBDoq1Ct99oKczlYTn3wKf79NqFHIK1NK25PqDDao25PcMCzAir%2BUUpJtACMir9GHuxDl9gnO%2FvgYu5xxbHpyORQrShpLPv32ou8R%2Buti1MLlZJRtoJp5BX%2FHNlr%2BPUIKbqypMnQNOkjHGYHyRNNmS0bTkktj2RS1KBjX4zYek%2BVsS5zh1o5MarTkm%2FAT%2ByY3U6LK0v9qHoTgH%2BMPMPudk70GOqUBEKF0lt2PHffG9s2%2FrFXJE5Ps5UOqfTL3W0f4JIJzSztTU8hQCnA4y36895KHjDm%2FPsb2uP505U9IWdk2Wop8XybiibFptH0PpJ3pptkmwvftyJuhw2%2FLiS1xnEUWDnCCaXfs9tCZZmXEUBMwyg7dswbWE0hHIg8kjxTWqgCjQ3cdy3X08F9rD52dmOBpUj9vDeVpRW1FTmzvDafHBISrziBmucit&X-Amz-Signature=7e1235cf43d0cdcb98f984f26aea3a7f3bbf8739938fcf58876b3b8065c9f7e1&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTNFF5FE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHfkEJMk9mS1K9SrBiVIT1dW780DTWAo8Xf50D8pXyOhAiBFzdTmHdaEAJVSOC39teAd6Xd%2Ba1o7SJ3%2FiDgYh%2FEeNyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMykAo8b1YnJ8D1YPwKtwD759q3e8oIftJuCHZA1EfCVzd0ksTFv6BzoP%2Fpb6xlACsGC1ca%2FTZi0eQolhE3Hvlyd4LX2fOMqAs8KCGP3GVoKz1hqZmztSH7x5yGQrXF9SBEn8pnmjAIuNNjvgqcmy7Iot6CW05FjBo7HGdv6gcHo2ytT5m7Wj08xQx9qNNq9FfVCQCR%2FWOOiRKbFts%2BJw%2FQf5ZRwQ62EMMrNxkCR5i71lxmvj0At21k1Ffplsu1h5sTtQT2rVxnS20oDYaPNaiRQZmU51DQcJUZoGC7iQH9FxqAMFAVibHb8e5TUSZelPRqPzDZq5b3M01B0HS6VMrdL%2Bhg2J6s8qFjYuFp7D%2Foe0oWSO3finLo4Lc1a0BsmTL3EWE4ygBbkZ5eSZCRxCMm9mK9pNPFXg2rAcEd35G3Za6HjoHuXGbGETFb%2FwJgjXsWgx%2BYvnQ1V5iy2FBfiHoAfhxhgslvLn3F8YpzsR7cPpsB7HUi2DWNJ0Gd7Yzhjw3Z%2BCea6p216PqCHiZzuGzzjTTg0kd%2Bc4sB4DR4h5%2FSwtem6L6tQhwF%2Bxw%2BrrHa2L8biPyjmFjKh96aa9M5PNIcAK1z7OtRBhUUuIRAJgnzMfImwFs5Dh7loGwjfL8clgRBT6jETrqiXODXIMw7ZuTvQY6pgH28gXufQJt2XObRproOguLfrqeQW%2FviShUCthnqEW17nJoimMWpdUqh2fRtCj%2BPpUqlaZ%2BriiIHfjQzwumz%2B%2B9rUtqUjOWtaT8318sOGAP%2BX%2F0aGoYG92GVT6%2FmajKXTaTKp0z4Ip4i0ahLsv7ponsjFonSx3Dd%2FE%2Bqy9ThQwFoVq3nSuz1DSGyeYu6pnxGLg8bn6xcfACqqzkkwHaN6w6QDXe6Jp2&X-Amz-Signature=16360f45e0db64fec7433fea781d300eea8740091695545c48d5b930a752aa6c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTNFF5FE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIHfkEJMk9mS1K9SrBiVIT1dW780DTWAo8Xf50D8pXyOhAiBFzdTmHdaEAJVSOC39teAd6Xd%2Ba1o7SJ3%2FiDgYh%2FEeNyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMykAo8b1YnJ8D1YPwKtwD759q3e8oIftJuCHZA1EfCVzd0ksTFv6BzoP%2Fpb6xlACsGC1ca%2FTZi0eQolhE3Hvlyd4LX2fOMqAs8KCGP3GVoKz1hqZmztSH7x5yGQrXF9SBEn8pnmjAIuNNjvgqcmy7Iot6CW05FjBo7HGdv6gcHo2ytT5m7Wj08xQx9qNNq9FfVCQCR%2FWOOiRKbFts%2BJw%2FQf5ZRwQ62EMMrNxkCR5i71lxmvj0At21k1Ffplsu1h5sTtQT2rVxnS20oDYaPNaiRQZmU51DQcJUZoGC7iQH9FxqAMFAVibHb8e5TUSZelPRqPzDZq5b3M01B0HS6VMrdL%2Bhg2J6s8qFjYuFp7D%2Foe0oWSO3finLo4Lc1a0BsmTL3EWE4ygBbkZ5eSZCRxCMm9mK9pNPFXg2rAcEd35G3Za6HjoHuXGbGETFb%2FwJgjXsWgx%2BYvnQ1V5iy2FBfiHoAfhxhgslvLn3F8YpzsR7cPpsB7HUi2DWNJ0Gd7Yzhjw3Z%2BCea6p216PqCHiZzuGzzjTTg0kd%2Bc4sB4DR4h5%2FSwtem6L6tQhwF%2Bxw%2BrrHa2L8biPyjmFjKh96aa9M5PNIcAK1z7OtRBhUUuIRAJgnzMfImwFs5Dh7loGwjfL8clgRBT6jETrqiXODXIMw7ZuTvQY6pgH28gXufQJt2XObRproOguLfrqeQW%2FviShUCthnqEW17nJoimMWpdUqh2fRtCj%2BPpUqlaZ%2BriiIHfjQzwumz%2B%2B9rUtqUjOWtaT8318sOGAP%2BX%2F0aGoYG92GVT6%2FmajKXTaTKp0z4Ip4i0ahLsv7ponsjFonSx3Dd%2FE%2Bqy9ThQwFoVq3nSuz1DSGyeYu6pnxGLg8bn6xcfACqqzkkwHaN6w6QDXe6Jp2&X-Amz-Signature=edb73f7f039bac4ee7ca668c72281a1687775a9080d7b6d8d1f0f038089f4d47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBBBXOIP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDj9VwjOwF%2F%2Bit3GYxzrukCcMN8KCny5OvbudV3O2qChQIgJ437RxEJGTfVMRpzyErfk8y2gQknYOTtKo7FgMEJs20q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDA0xvzAskbWLbBDBYSrcAzI1N%2B541BDwYcNwEO%2BKq%2FuUcez5iLs650Aex3tImp%2Fp0fgfLyP%2F%2BwXcyhcF%2FW4syIo7Y4dxHRGqi6C9J3v%2FOoW0i0X8bQDF6iIkzAmh%2BWOKojUSs5f7jB43IpMPGd1%2FN3mmm0se%2F%2B4HabEyWgnQJVAOXogWschCqYemaJOYXcNnrFuyGGucYtlpAkez7uKLOfp6vHWX1xYat3iBvPnM%2FelpWUrHYmRE%2FEMeopEuQuhJVDA3nlGk9SEAZROUuWc84aaXeXIsICwHadJMx%2BFzohr%2BMdwWgfX%2BCeprZCzCrNsW%2B4UpWBghQ1EXKTvqDMHSjUTtlemh9pAQB49%2Flpu4mkX8gdOwpl%2Bx3BaaTIuK0pqDK9U2MzZQQKZjLUYJwLAOtdw5PSVUkAA%2BhjKJSR8o15RA3ZmEcVSoo6QlqKBtHjcSBDoq1Ct99oKczlYTn3wKf79NqFHIK1NK25PqDDao25PcMCzAir%2BUUpJtACMir9GHuxDl9gnO%2FvgYu5xxbHpyORQrShpLPv32ou8R%2Buti1MLlZJRtoJp5BX%2FHNlr%2BPUIKbqypMnQNOkjHGYHyRNNmS0bTkktj2RS1KBjX4zYek%2BVsS5zh1o5MarTkm%2FAT%2ByY3U6LK0v9qHoTgH%2BMPMPudk70GOqUBEKF0lt2PHffG9s2%2FrFXJE5Ps5UOqfTL3W0f4JIJzSztTU8hQCnA4y36895KHjDm%2FPsb2uP505U9IWdk2Wop8XybiibFptH0PpJ3pptkmwvftyJuhw2%2FLiS1xnEUWDnCCaXfs9tCZZmXEUBMwyg7dswbWE0hHIg8kjxTWqgCjQ3cdy3X08F9rD52dmOBpUj9vDeVpRW1FTmzvDafHBISrziBmucit&X-Amz-Signature=a69ff0404aec209b366c07dd5dc7469ec73dcc759f1bb0e6f7e999ec58ba0f40&X-Amz-SignedHeaders=host&x-id=GetObject)
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