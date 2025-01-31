

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYAJUPV4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsrQd%2BnXNqE0ew7YeTxVlS8UuL75ucF6TWr8lhsfIQ6AIgVMfY092cZ2jxDrKyWQK2nyZiFwk13tnGFSwnNjfdWGIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9%2FNu9f6Tg6knJfmircA2eI8F8b3VvlF%2BCo9zbxh3pyjQvJ8Tv68DdRW93kaYqZbs%2BFNlo0z%2Bl1k8j2m1eY20SAKgxuNzPodFhVABlH9MzQ%2FSsjCXAdnZ8drFtDuSaQdg4r4wT9bmb570tC06V28nsDeMg%2BafPV0ekez8IUqIaHQqCz4t9%2Fby5QWA2L4ebS7JG4YO4bHlywF8YAYRqcFIFP%2BrJtFtxID6lM5o%2BZ%2BP9mYk%2F3vNDr0SbVKfdsMjy9ep%2BTek%2BHny2Ch7KEedSXu2VEyi9zg9lyo%2FteELXiArPAz4IhkwbrKNihzJOPtSslDMRBBbXME11%2Bmlpbsvo0B7s%2Bw49%2Bg5mZF2Wgl6BBAF8Saar%2BqgKEl5lhVgmQ1bg1fEUdZ5mexF2H4RhhPZ2FctHCutg6gbI0nZkvT3qvRSZgOFE2WrPhjrDr5M%2BU8wbDpk%2FBgA37Ry%2BjUQCMqmOcVfdDzu%2Bhag9r3ndN29Q6llL%2Bi3pEQvE2huLeoqvVyyvStcUtcVWqRO01SeMkQsGuUIR56rghy285KF6Zk70%2Bhbej%2BztiViK8q36pE9tTim%2Fr6g5n%2BcyVFbbk22ItxJ9tfZFfGb8rJz0xi%2BPeQ7UPic9uGIVKPLCDdaX%2BrghyoAcREWut0uFeo3KlZxyYMJ3r87wGOqUBCc%2FYMRgiYfsR6AWoDIOfIU%2FE4eLEVzgrw%2BqBfQZUCGKyYLBO8ESgeWQQji1XN8exbrZDPgXzk6%2Bvf2PbsRpHVTxV8Pq7hbOWQawPSOWsZRd3xo8ibBEOqDY3FhiRD%2FljVh8mCow3qUxy%2BbHFb8iAwA6TBcBY3fZ5kyxol%2BYnG4ZQgkLAXsYDMAPYZAMkc3YGh53GEtWGgP909CUtuEBAQPDNE%2F5b&X-Amz-Signature=fd974daad83ba2136c9c87002bfed8402c879e788f379d7505d8bd5f3e2a0820&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYAJUPV4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsrQd%2BnXNqE0ew7YeTxVlS8UuL75ucF6TWr8lhsfIQ6AIgVMfY092cZ2jxDrKyWQK2nyZiFwk13tnGFSwnNjfdWGIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9%2FNu9f6Tg6knJfmircA2eI8F8b3VvlF%2BCo9zbxh3pyjQvJ8Tv68DdRW93kaYqZbs%2BFNlo0z%2Bl1k8j2m1eY20SAKgxuNzPodFhVABlH9MzQ%2FSsjCXAdnZ8drFtDuSaQdg4r4wT9bmb570tC06V28nsDeMg%2BafPV0ekez8IUqIaHQqCz4t9%2Fby5QWA2L4ebS7JG4YO4bHlywF8YAYRqcFIFP%2BrJtFtxID6lM5o%2BZ%2BP9mYk%2F3vNDr0SbVKfdsMjy9ep%2BTek%2BHny2Ch7KEedSXu2VEyi9zg9lyo%2FteELXiArPAz4IhkwbrKNihzJOPtSslDMRBBbXME11%2Bmlpbsvo0B7s%2Bw49%2Bg5mZF2Wgl6BBAF8Saar%2BqgKEl5lhVgmQ1bg1fEUdZ5mexF2H4RhhPZ2FctHCutg6gbI0nZkvT3qvRSZgOFE2WrPhjrDr5M%2BU8wbDpk%2FBgA37Ry%2BjUQCMqmOcVfdDzu%2Bhag9r3ndN29Q6llL%2Bi3pEQvE2huLeoqvVyyvStcUtcVWqRO01SeMkQsGuUIR56rghy285KF6Zk70%2Bhbej%2BztiViK8q36pE9tTim%2Fr6g5n%2BcyVFbbk22ItxJ9tfZFfGb8rJz0xi%2BPeQ7UPic9uGIVKPLCDdaX%2BrghyoAcREWut0uFeo3KlZxyYMJ3r87wGOqUBCc%2FYMRgiYfsR6AWoDIOfIU%2FE4eLEVzgrw%2BqBfQZUCGKyYLBO8ESgeWQQji1XN8exbrZDPgXzk6%2Bvf2PbsRpHVTxV8Pq7hbOWQawPSOWsZRd3xo8ibBEOqDY3FhiRD%2FljVh8mCow3qUxy%2BbHFb8iAwA6TBcBY3fZ5kyxol%2BYnG4ZQgkLAXsYDMAPYZAMkc3YGh53GEtWGgP909CUtuEBAQPDNE%2F5b&X-Amz-Signature=e94a2d7e10233f38a5768d2b17cec7371516b1f41d0fc5f3c525bcca9b3592ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYAJUPV4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsrQd%2BnXNqE0ew7YeTxVlS8UuL75ucF6TWr8lhsfIQ6AIgVMfY092cZ2jxDrKyWQK2nyZiFwk13tnGFSwnNjfdWGIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9%2FNu9f6Tg6knJfmircA2eI8F8b3VvlF%2BCo9zbxh3pyjQvJ8Tv68DdRW93kaYqZbs%2BFNlo0z%2Bl1k8j2m1eY20SAKgxuNzPodFhVABlH9MzQ%2FSsjCXAdnZ8drFtDuSaQdg4r4wT9bmb570tC06V28nsDeMg%2BafPV0ekez8IUqIaHQqCz4t9%2Fby5QWA2L4ebS7JG4YO4bHlywF8YAYRqcFIFP%2BrJtFtxID6lM5o%2BZ%2BP9mYk%2F3vNDr0SbVKfdsMjy9ep%2BTek%2BHny2Ch7KEedSXu2VEyi9zg9lyo%2FteELXiArPAz4IhkwbrKNihzJOPtSslDMRBBbXME11%2Bmlpbsvo0B7s%2Bw49%2Bg5mZF2Wgl6BBAF8Saar%2BqgKEl5lhVgmQ1bg1fEUdZ5mexF2H4RhhPZ2FctHCutg6gbI0nZkvT3qvRSZgOFE2WrPhjrDr5M%2BU8wbDpk%2FBgA37Ry%2BjUQCMqmOcVfdDzu%2Bhag9r3ndN29Q6llL%2Bi3pEQvE2huLeoqvVyyvStcUtcVWqRO01SeMkQsGuUIR56rghy285KF6Zk70%2Bhbej%2BztiViK8q36pE9tTim%2Fr6g5n%2BcyVFbbk22ItxJ9tfZFfGb8rJz0xi%2BPeQ7UPic9uGIVKPLCDdaX%2BrghyoAcREWut0uFeo3KlZxyYMJ3r87wGOqUBCc%2FYMRgiYfsR6AWoDIOfIU%2FE4eLEVzgrw%2BqBfQZUCGKyYLBO8ESgeWQQji1XN8exbrZDPgXzk6%2Bvf2PbsRpHVTxV8Pq7hbOWQawPSOWsZRd3xo8ibBEOqDY3FhiRD%2FljVh8mCow3qUxy%2BbHFb8iAwA6TBcBY3fZ5kyxol%2BYnG4ZQgkLAXsYDMAPYZAMkc3YGh53GEtWGgP909CUtuEBAQPDNE%2F5b&X-Amz-Signature=95ef994714933e1786e204a388475f9c39156f160dc5a80d4f02083b7446a53f&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAD2UYCR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCthKJ1Kl%2FKdSnzqcYMKKA7Y4GiVlhcullA1niXqkZhxQIgRBGbRKKiCQUmUXw%2FlBlR7d9J9Q1zBb04CUjoGe51LHkqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDABkyQUgcxw5IY8r%2FircA9xP1ZllnG3siZlrz7NTlI6sMHjjb6Qc0c%2BQwvzu94toF%2BH0Q9Ecuiu0Eajl9OBERrtvF7l8RATgcM3lIGQ%2Fs71N5cp7xRhSSLl2CtXpIyeLJaodXGiIR84eHjcFqh7a4UkI%2FxN1c8pm2WaNx031DkqP4U6oVOhm9zaawGLC5WNlhC90HYehRFNvDar0CSieGX52D%2FJu2M8QBkhenIIaoqCojBxzQuL8y%2BdWFCA2NU0%2FzUcCMJaMK%2FnH6q0GK2e5W7wtFe9XkrORXDFEu%2BxWb8hPQvue9y0VYhmuyRW4ZX1ypJQCkkRB2TLrq2uk670RzQM7xqhlWoOCm688qOUaqKLPylrhOMXBEVZ%2Fz9kVr%2FTNJCWTz5MWKEK6s35cgXNnfmZmFwh%2F7Yl850WuHsOmPpXBgOqyYcefLJRzxmCimhJoXyPIxOuygbV6SYvUX6RHbxfG4DvDtO2ouB9wc4lFNekBbNyUm7Gcor3iwKvtOHjsImurhHTRGuMpwC0Eue0AL6ZOHnW57NrSZK6mknTsOy8Mq0a4jTQu%2FrXuKgE948QVIvTF1qiKtaFiA9FIi9tDeE1btH91nw25OETUuSI8%2F2kqvhENiT5W352HDXWAMhW%2FOPn%2B2TFpg4ja7%2By%2BMPnq87wGOqUBtQVHb6rPe%2B4iSOiCF%2BN7KI78xFEHSAKPaxAgKey0KxzJLWejBza%2BW7RX2RDe5RrQ83m%2BVAUXTHRW3DUK5D%2FpBv2V6o3ASfwSMjkvolwQXY34LtOzS9ZzPR8c6b3iFLeJvyRAAD%2By2o8VSLwgjDLKsPM3vb5cHxVSruZc%2F6RhcpP9a27mT4txTpz%2F4ng9vXz1bitU5Vs%2BMos2fIum0Dj%2BbSoD%2BR88&X-Amz-Signature=edc98d435d67195b24a3c5f7d7f3f317272b75fe08894208efa4f2df44dafa29&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAD2UYCR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCthKJ1Kl%2FKdSnzqcYMKKA7Y4GiVlhcullA1niXqkZhxQIgRBGbRKKiCQUmUXw%2FlBlR7d9J9Q1zBb04CUjoGe51LHkqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDABkyQUgcxw5IY8r%2FircA9xP1ZllnG3siZlrz7NTlI6sMHjjb6Qc0c%2BQwvzu94toF%2BH0Q9Ecuiu0Eajl9OBERrtvF7l8RATgcM3lIGQ%2Fs71N5cp7xRhSSLl2CtXpIyeLJaodXGiIR84eHjcFqh7a4UkI%2FxN1c8pm2WaNx031DkqP4U6oVOhm9zaawGLC5WNlhC90HYehRFNvDar0CSieGX52D%2FJu2M8QBkhenIIaoqCojBxzQuL8y%2BdWFCA2NU0%2FzUcCMJaMK%2FnH6q0GK2e5W7wtFe9XkrORXDFEu%2BxWb8hPQvue9y0VYhmuyRW4ZX1ypJQCkkRB2TLrq2uk670RzQM7xqhlWoOCm688qOUaqKLPylrhOMXBEVZ%2Fz9kVr%2FTNJCWTz5MWKEK6s35cgXNnfmZmFwh%2F7Yl850WuHsOmPpXBgOqyYcefLJRzxmCimhJoXyPIxOuygbV6SYvUX6RHbxfG4DvDtO2ouB9wc4lFNekBbNyUm7Gcor3iwKvtOHjsImurhHTRGuMpwC0Eue0AL6ZOHnW57NrSZK6mknTsOy8Mq0a4jTQu%2FrXuKgE948QVIvTF1qiKtaFiA9FIi9tDeE1btH91nw25OETUuSI8%2F2kqvhENiT5W352HDXWAMhW%2FOPn%2B2TFpg4ja7%2By%2BMPnq87wGOqUBtQVHb6rPe%2B4iSOiCF%2BN7KI78xFEHSAKPaxAgKey0KxzJLWejBza%2BW7RX2RDe5RrQ83m%2BVAUXTHRW3DUK5D%2FpBv2V6o3ASfwSMjkvolwQXY34LtOzS9ZzPR8c6b3iFLeJvyRAAD%2By2o8VSLwgjDLKsPM3vb5cHxVSruZc%2F6RhcpP9a27mT4txTpz%2F4ng9vXz1bitU5Vs%2BMos2fIum0Dj%2BbSoD%2BR88&X-Amz-Signature=4be8276ee4dc101278f445bf1d088e1af3f267cfd9192632c4bedff37be75523&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYAJUPV4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsrQd%2BnXNqE0ew7YeTxVlS8UuL75ucF6TWr8lhsfIQ6AIgVMfY092cZ2jxDrKyWQK2nyZiFwk13tnGFSwnNjfdWGIqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9%2FNu9f6Tg6knJfmircA2eI8F8b3VvlF%2BCo9zbxh3pyjQvJ8Tv68DdRW93kaYqZbs%2BFNlo0z%2Bl1k8j2m1eY20SAKgxuNzPodFhVABlH9MzQ%2FSsjCXAdnZ8drFtDuSaQdg4r4wT9bmb570tC06V28nsDeMg%2BafPV0ekez8IUqIaHQqCz4t9%2Fby5QWA2L4ebS7JG4YO4bHlywF8YAYRqcFIFP%2BrJtFtxID6lM5o%2BZ%2BP9mYk%2F3vNDr0SbVKfdsMjy9ep%2BTek%2BHny2Ch7KEedSXu2VEyi9zg9lyo%2FteELXiArPAz4IhkwbrKNihzJOPtSslDMRBBbXME11%2Bmlpbsvo0B7s%2Bw49%2Bg5mZF2Wgl6BBAF8Saar%2BqgKEl5lhVgmQ1bg1fEUdZ5mexF2H4RhhPZ2FctHCutg6gbI0nZkvT3qvRSZgOFE2WrPhjrDr5M%2BU8wbDpk%2FBgA37Ry%2BjUQCMqmOcVfdDzu%2Bhag9r3ndN29Q6llL%2Bi3pEQvE2huLeoqvVyyvStcUtcVWqRO01SeMkQsGuUIR56rghy285KF6Zk70%2Bhbej%2BztiViK8q36pE9tTim%2Fr6g5n%2BcyVFbbk22ItxJ9tfZFfGb8rJz0xi%2BPeQ7UPic9uGIVKPLCDdaX%2BrghyoAcREWut0uFeo3KlZxyYMJ3r87wGOqUBCc%2FYMRgiYfsR6AWoDIOfIU%2FE4eLEVzgrw%2BqBfQZUCGKyYLBO8ESgeWQQji1XN8exbrZDPgXzk6%2Bvf2PbsRpHVTxV8Pq7hbOWQawPSOWsZRd3xo8ibBEOqDY3FhiRD%2FljVh8mCow3qUxy%2BbHFb8iAwA6TBcBY3fZ5kyxol%2BYnG4ZQgkLAXsYDMAPYZAMkc3YGh53GEtWGgP909CUtuEBAQPDNE%2F5b&X-Amz-Signature=780d8f8deaff166825d51fe9b5694dd50e0cf701486b933fa10d2c4c573bc84b&X-Amz-SignedHeaders=host&x-id=GetObject)
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