

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y57THKDT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFzbHSHp5AB4otdEdvcRWMAUfztYjS6%2B6Ya5lnv542WBAiEApFyzBUA4%2FThBQ8sOGWj035LhQCN%2BTJnujr3ZsiYJq9IqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNYcikEADtY6%2Fg%2BvyrcAw6TVw2Ehn8u6yxxtHSXexA3renkCscAfiqh%2FcCzX855zv4M37ysJdS9F4ZO9to6nYOJbg8pDh%2B4UCg6QePrg0GcnZe5sUBZ0DnKaJbfX1cw74lXwyNhloA0PapIgYvkDBiRfrMxFUWCEb9gy4mHv5AEE9Ni9H4I6g5jWN96LmTwNAAYNCaMCjpdsEk0YByDy3pSD7owPDcWefBalgrWtUsF0nabwVcB8Q%2Fnaw%2BoaJHKPWkZKNNSKIxFffuFNrR6IPmNNB92dgWyU%2BZcayJhr%2F3de%2BuKwzeZiCZgg9bDrTxZufdkFr%2FtoKcJZwuAH8pdp7O3Hrkak0t2XKQMdJ0EQUB0XLEio3bQhOSC79NNEl3%2B8LnFvxANNdwWHESiUDbBP6vcC8DHURUCHZ88UyrRpJakKI4wmlsLKgvs5fg5z9hn7zxEVHAAVKhkbBnyGFA3TW1x0tKCrbEDEwwDaDwvpS2R5jhwLKSQgt6fuVfjQ0Q2rI2iBGq1T19IknoTN8mL8bfJ5vhf56y1eadDJxQhKbtfdxZ0FkWBWDB2ofl5ko0VQN1hKOLp1AqlAAR%2BxkWmAMSqfq5ea893UdmsDNqPU%2BWrITPK8jY%2FiViUd%2FVciTbaciKGwUDMGxTOyPmoMP2e%2B7wGOqUBCho2AkeMSqoaZOnAHLmltiW5zz6nlzO8xIQ7aQVOFwQN%2FeuuOFyAVygVZBTjkyisc%2BVffEn%2BpMfQePk815y7eJrHVrq0Eqr1vhxkR1jqAW2R5h51FVEb5GHed9C4vOVESJvHo0t70vQNVzKiuP%2FGgQkOSEss5A%2F1MatLVxHovq8E%2Bp%2FPvjpSCRUAiDJt9eELrjYSdmyHGcCJXuoPcxYoRdNgYFnc&X-Amz-Signature=d79ebdd7397e384bfdfe546fe224547a046564725ffbdbbb0a129ab568bbf4ed&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y57THKDT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFzbHSHp5AB4otdEdvcRWMAUfztYjS6%2B6Ya5lnv542WBAiEApFyzBUA4%2FThBQ8sOGWj035LhQCN%2BTJnujr3ZsiYJq9IqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNYcikEADtY6%2Fg%2BvyrcAw6TVw2Ehn8u6yxxtHSXexA3renkCscAfiqh%2FcCzX855zv4M37ysJdS9F4ZO9to6nYOJbg8pDh%2B4UCg6QePrg0GcnZe5sUBZ0DnKaJbfX1cw74lXwyNhloA0PapIgYvkDBiRfrMxFUWCEb9gy4mHv5AEE9Ni9H4I6g5jWN96LmTwNAAYNCaMCjpdsEk0YByDy3pSD7owPDcWefBalgrWtUsF0nabwVcB8Q%2Fnaw%2BoaJHKPWkZKNNSKIxFffuFNrR6IPmNNB92dgWyU%2BZcayJhr%2F3de%2BuKwzeZiCZgg9bDrTxZufdkFr%2FtoKcJZwuAH8pdp7O3Hrkak0t2XKQMdJ0EQUB0XLEio3bQhOSC79NNEl3%2B8LnFvxANNdwWHESiUDbBP6vcC8DHURUCHZ88UyrRpJakKI4wmlsLKgvs5fg5z9hn7zxEVHAAVKhkbBnyGFA3TW1x0tKCrbEDEwwDaDwvpS2R5jhwLKSQgt6fuVfjQ0Q2rI2iBGq1T19IknoTN8mL8bfJ5vhf56y1eadDJxQhKbtfdxZ0FkWBWDB2ofl5ko0VQN1hKOLp1AqlAAR%2BxkWmAMSqfq5ea893UdmsDNqPU%2BWrITPK8jY%2FiViUd%2FVciTbaciKGwUDMGxTOyPmoMP2e%2B7wGOqUBCho2AkeMSqoaZOnAHLmltiW5zz6nlzO8xIQ7aQVOFwQN%2FeuuOFyAVygVZBTjkyisc%2BVffEn%2BpMfQePk815y7eJrHVrq0Eqr1vhxkR1jqAW2R5h51FVEb5GHed9C4vOVESJvHo0t70vQNVzKiuP%2FGgQkOSEss5A%2F1MatLVxHovq8E%2Bp%2FPvjpSCRUAiDJt9eELrjYSdmyHGcCJXuoPcxYoRdNgYFnc&X-Amz-Signature=b130629ac30efd44f5fbd48d03e45363c4baef902d24bb9020274afeb5bfdf58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y57THKDT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFzbHSHp5AB4otdEdvcRWMAUfztYjS6%2B6Ya5lnv542WBAiEApFyzBUA4%2FThBQ8sOGWj035LhQCN%2BTJnujr3ZsiYJq9IqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNYcikEADtY6%2Fg%2BvyrcAw6TVw2Ehn8u6yxxtHSXexA3renkCscAfiqh%2FcCzX855zv4M37ysJdS9F4ZO9to6nYOJbg8pDh%2B4UCg6QePrg0GcnZe5sUBZ0DnKaJbfX1cw74lXwyNhloA0PapIgYvkDBiRfrMxFUWCEb9gy4mHv5AEE9Ni9H4I6g5jWN96LmTwNAAYNCaMCjpdsEk0YByDy3pSD7owPDcWefBalgrWtUsF0nabwVcB8Q%2Fnaw%2BoaJHKPWkZKNNSKIxFffuFNrR6IPmNNB92dgWyU%2BZcayJhr%2F3de%2BuKwzeZiCZgg9bDrTxZufdkFr%2FtoKcJZwuAH8pdp7O3Hrkak0t2XKQMdJ0EQUB0XLEio3bQhOSC79NNEl3%2B8LnFvxANNdwWHESiUDbBP6vcC8DHURUCHZ88UyrRpJakKI4wmlsLKgvs5fg5z9hn7zxEVHAAVKhkbBnyGFA3TW1x0tKCrbEDEwwDaDwvpS2R5jhwLKSQgt6fuVfjQ0Q2rI2iBGq1T19IknoTN8mL8bfJ5vhf56y1eadDJxQhKbtfdxZ0FkWBWDB2ofl5ko0VQN1hKOLp1AqlAAR%2BxkWmAMSqfq5ea893UdmsDNqPU%2BWrITPK8jY%2FiViUd%2FVciTbaciKGwUDMGxTOyPmoMP2e%2B7wGOqUBCho2AkeMSqoaZOnAHLmltiW5zz6nlzO8xIQ7aQVOFwQN%2FeuuOFyAVygVZBTjkyisc%2BVffEn%2BpMfQePk815y7eJrHVrq0Eqr1vhxkR1jqAW2R5h51FVEb5GHed9C4vOVESJvHo0t70vQNVzKiuP%2FGgQkOSEss5A%2F1MatLVxHovq8E%2Bp%2FPvjpSCRUAiDJt9eELrjYSdmyHGcCJXuoPcxYoRdNgYFnc&X-Amz-Signature=8ad976c8dc6f0593a35bcc3ec4be210f12f586456aa08c21a8c696b64dfd064d&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCV2ZB5P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAThoO95Wnq6mzC8IxG9DUYfJWcN8Jn3gOivkJRZ8biyAiA3NHB7hrW7e%2BzLnAaIZRGfA%2BF0MBV7ZxMev4wYMYGbJCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAFBm8QF045r8fRk2KtwDuJfzmxQwjCVDSEiVAWWUWSrbmWdeMXNtyrUxW7iwJb7fcFSYzlgvUotgl3Tx52t%2FUmGRtiR%2BTXuAKEzOMZ91xd0OgX1Yb1LHSbvnPt5cCjXVHKrk5ZT4qngJ29PhCTdtDLY6O4LTH3iyBllPre3WxWYg2oN7dvmYz5a%2BytCErxL2ocYxJPKw1ZIroSTljiZSJMcadiIVaEJrFenlifzG7bSuXowTIFzxYHnsDgOA64L%2BoKbAsJPggVaMNYZyz6vbDH5VSg0%2BD6hJ15DmZ3XDbiAac5XyQDKa0xk%2BgtTk50A5bbIzM1DuSzYOqc%2Fn%2BMIpDV4d6FDCftHIUg1xJZEvPQSzuFYngkqZVv%2BsfAr5%2F4w1EcoYHqO1BG%2FWqNT4aXjsCcZ1HTT8B%2FGKwiXMR1brTuXdhWJQFqjiCjX0iICkQWGMIpN60wb3ytg2XQOUr331v%2Bsxcr9mSrt8eG2FP4%2BRaqgFkuW6r9lfWv3Wzg0GWThsak%2FiYtTv8HHpTB%2FQloOdr677Hmdt5uNLtggrW7NBoaPfZQi3BZ6zos9NtGtzZVhIInXDgJE%2F5ENushOluw0kqzidwr5HpgsNDPhEWhT2saW90dEDN8PRzFnDbLrbcwLZyFxWKTs2YivZwwIwj5%2F7vAY6pgHHmALvnMQmI%2Bwi%2FXmnLomD3OMPILlGe2OmxVb7NqHP1wtEADTprW%2BRLNXVnuZKo%2FvUs9rKgP20wmG9ypEQmCmtCdr8vXYTq0wCzAbmWLf4%2FKw%2Bn7F%2B9QHFTNvLV6KqCy6wCZWw21EFWQFMPUpMpfasP2CBEoa3sRGxKH6q9b3TlpISBHwJ8%2F4bz0H9u%2FyL9pVPwb%2BBrCe1c%2Fmh4KCn6jInyN8zprd8&X-Amz-Signature=92d41030c5fbfb51169c3777c092f3c7bb6c370a9fee638c9bcf34c57f1f5eb1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCV2ZB5P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAThoO95Wnq6mzC8IxG9DUYfJWcN8Jn3gOivkJRZ8biyAiA3NHB7hrW7e%2BzLnAaIZRGfA%2BF0MBV7ZxMev4wYMYGbJCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAFBm8QF045r8fRk2KtwDuJfzmxQwjCVDSEiVAWWUWSrbmWdeMXNtyrUxW7iwJb7fcFSYzlgvUotgl3Tx52t%2FUmGRtiR%2BTXuAKEzOMZ91xd0OgX1Yb1LHSbvnPt5cCjXVHKrk5ZT4qngJ29PhCTdtDLY6O4LTH3iyBllPre3WxWYg2oN7dvmYz5a%2BytCErxL2ocYxJPKw1ZIroSTljiZSJMcadiIVaEJrFenlifzG7bSuXowTIFzxYHnsDgOA64L%2BoKbAsJPggVaMNYZyz6vbDH5VSg0%2BD6hJ15DmZ3XDbiAac5XyQDKa0xk%2BgtTk50A5bbIzM1DuSzYOqc%2Fn%2BMIpDV4d6FDCftHIUg1xJZEvPQSzuFYngkqZVv%2BsfAr5%2F4w1EcoYHqO1BG%2FWqNT4aXjsCcZ1HTT8B%2FGKwiXMR1brTuXdhWJQFqjiCjX0iICkQWGMIpN60wb3ytg2XQOUr331v%2Bsxcr9mSrt8eG2FP4%2BRaqgFkuW6r9lfWv3Wzg0GWThsak%2FiYtTv8HHpTB%2FQloOdr677Hmdt5uNLtggrW7NBoaPfZQi3BZ6zos9NtGtzZVhIInXDgJE%2F5ENushOluw0kqzidwr5HpgsNDPhEWhT2saW90dEDN8PRzFnDbLrbcwLZyFxWKTs2YivZwwIwj5%2F7vAY6pgHHmALvnMQmI%2Bwi%2FXmnLomD3OMPILlGe2OmxVb7NqHP1wtEADTprW%2BRLNXVnuZKo%2FvUs9rKgP20wmG9ypEQmCmtCdr8vXYTq0wCzAbmWLf4%2FKw%2Bn7F%2B9QHFTNvLV6KqCy6wCZWw21EFWQFMPUpMpfasP2CBEoa3sRGxKH6q9b3TlpISBHwJ8%2F4bz0H9u%2FyL9pVPwb%2BBrCe1c%2Fmh4KCn6jInyN8zprd8&X-Amz-Signature=40b8b4dad7b89d7db154bb1f4cfed88c27c3a35c6e4295957a761c7cd6c0aee4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y57THKDT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFzbHSHp5AB4otdEdvcRWMAUfztYjS6%2B6Ya5lnv542WBAiEApFyzBUA4%2FThBQ8sOGWj035LhQCN%2BTJnujr3ZsiYJq9IqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNYcikEADtY6%2Fg%2BvyrcAw6TVw2Ehn8u6yxxtHSXexA3renkCscAfiqh%2FcCzX855zv4M37ysJdS9F4ZO9to6nYOJbg8pDh%2B4UCg6QePrg0GcnZe5sUBZ0DnKaJbfX1cw74lXwyNhloA0PapIgYvkDBiRfrMxFUWCEb9gy4mHv5AEE9Ni9H4I6g5jWN96LmTwNAAYNCaMCjpdsEk0YByDy3pSD7owPDcWefBalgrWtUsF0nabwVcB8Q%2Fnaw%2BoaJHKPWkZKNNSKIxFffuFNrR6IPmNNB92dgWyU%2BZcayJhr%2F3de%2BuKwzeZiCZgg9bDrTxZufdkFr%2FtoKcJZwuAH8pdp7O3Hrkak0t2XKQMdJ0EQUB0XLEio3bQhOSC79NNEl3%2B8LnFvxANNdwWHESiUDbBP6vcC8DHURUCHZ88UyrRpJakKI4wmlsLKgvs5fg5z9hn7zxEVHAAVKhkbBnyGFA3TW1x0tKCrbEDEwwDaDwvpS2R5jhwLKSQgt6fuVfjQ0Q2rI2iBGq1T19IknoTN8mL8bfJ5vhf56y1eadDJxQhKbtfdxZ0FkWBWDB2ofl5ko0VQN1hKOLp1AqlAAR%2BxkWmAMSqfq5ea893UdmsDNqPU%2BWrITPK8jY%2FiViUd%2FVciTbaciKGwUDMGxTOyPmoMP2e%2B7wGOqUBCho2AkeMSqoaZOnAHLmltiW5zz6nlzO8xIQ7aQVOFwQN%2FeuuOFyAVygVZBTjkyisc%2BVffEn%2BpMfQePk815y7eJrHVrq0Eqr1vhxkR1jqAW2R5h51FVEb5GHed9C4vOVESJvHo0t70vQNVzKiuP%2FGgQkOSEss5A%2F1MatLVxHovq8E%2Bp%2FPvjpSCRUAiDJt9eELrjYSdmyHGcCJXuoPcxYoRdNgYFnc&X-Amz-Signature=79a12583e43f0a5e28534cbcddba9f988f917df7f933a77d4d0f22cfe8a264c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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