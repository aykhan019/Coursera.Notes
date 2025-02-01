

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMNBHB7O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGyI0MDC34mjeq96hs4BtuXuQwwQQ3f17azDQh0eELZVAiEA97BNDr6FIzZGX3SShHOE1FZMMno067jyvBnv56DvDCAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPIVAK6DPzNwiwqo3ircA4ksErQLuPhI0Bh3ksStVZOBgS8Vl1aLgpqCQFoDefGMrj7cLwJcvJ6BKDuaYbSJnNOeg1NaOlh9OMiv2%2FZGV1WIIy9rNNj8CznrlkCye%2BvuhxuQtkE9XWJOcCOlbclCdVA0tq29JUoCW%2BZKiKkhkVWQaS9qUM6hU5RgiGpltgDdU%2F6zasjv6Nrj0%2BJbbsPFGKZyyV1TZMBYEOZtJBpNbc05aJm7czHwCOr%2BPxEZseBAY2e7oSZrNqZl7uOB3lUHTVoXorFjIBcwLN5AQ1ZX0j3LRoA6eN51WCkWqohskNdp%2BVZ1TxuQFM2VncUkX%2BypwYctpPamtZRr9cPsEOCgBOrGlgTdeCX0VoDT07cL2scw3WZ82zSNW5CcjBxz6%2FCi3qVf4VnV0vskTZ3CrgIX6j4zPyFHNRGv0bYMe2Uep8egGbYYoi1Eu85f%2BMK6FAJLsDUC2DZwS2rPbES3Yf8eRckJt%2BBX8ds%2B4GIqIMERlspzrrkimXoxlC8lcslV2hOoevdPko4ZePT4rRY33mLJQ%2B2QqqJT9V%2FSX0v%2FWMnBhXaXYIbIXTqSJh7bwlZcgt2lbL%2BxNRv%2BulV7VvuJy9CH8Bwny2KQ4Wee84ni6xIpKJTFK4kPzFgEwkdH2G5OMMnG%2BLwGOqUBn1ZrNqWIQbcxW38VIOE0aXru0JTvbPipcEbUqBcTReoh4wwntCPlOZklnAekApylm3yzN3nSDOAWguIoavF30rhNNZ%2B4BV1acuxXupxku%2FDdi6r5%2FqBPed35EdafgSZkGv%2FExMXMtu6Gkn%2FReK3pXRjcQuZygDYwVav0dXHPMthdh9Zc3dMLSowoG%2BmPZLAluf5gtrC%2BbhyFsalWbaB%2FbIEmb8Fm&X-Amz-Signature=ac18465b4a79088d5ace1d5243e9ab79dfd184a4ac703a15999c011678f6a97d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMNBHB7O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGyI0MDC34mjeq96hs4BtuXuQwwQQ3f17azDQh0eELZVAiEA97BNDr6FIzZGX3SShHOE1FZMMno067jyvBnv56DvDCAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPIVAK6DPzNwiwqo3ircA4ksErQLuPhI0Bh3ksStVZOBgS8Vl1aLgpqCQFoDefGMrj7cLwJcvJ6BKDuaYbSJnNOeg1NaOlh9OMiv2%2FZGV1WIIy9rNNj8CznrlkCye%2BvuhxuQtkE9XWJOcCOlbclCdVA0tq29JUoCW%2BZKiKkhkVWQaS9qUM6hU5RgiGpltgDdU%2F6zasjv6Nrj0%2BJbbsPFGKZyyV1TZMBYEOZtJBpNbc05aJm7czHwCOr%2BPxEZseBAY2e7oSZrNqZl7uOB3lUHTVoXorFjIBcwLN5AQ1ZX0j3LRoA6eN51WCkWqohskNdp%2BVZ1TxuQFM2VncUkX%2BypwYctpPamtZRr9cPsEOCgBOrGlgTdeCX0VoDT07cL2scw3WZ82zSNW5CcjBxz6%2FCi3qVf4VnV0vskTZ3CrgIX6j4zPyFHNRGv0bYMe2Uep8egGbYYoi1Eu85f%2BMK6FAJLsDUC2DZwS2rPbES3Yf8eRckJt%2BBX8ds%2B4GIqIMERlspzrrkimXoxlC8lcslV2hOoevdPko4ZePT4rRY33mLJQ%2B2QqqJT9V%2FSX0v%2FWMnBhXaXYIbIXTqSJh7bwlZcgt2lbL%2BxNRv%2BulV7VvuJy9CH8Bwny2KQ4Wee84ni6xIpKJTFK4kPzFgEwkdH2G5OMMnG%2BLwGOqUBn1ZrNqWIQbcxW38VIOE0aXru0JTvbPipcEbUqBcTReoh4wwntCPlOZklnAekApylm3yzN3nSDOAWguIoavF30rhNNZ%2B4BV1acuxXupxku%2FDdi6r5%2FqBPed35EdafgSZkGv%2FExMXMtu6Gkn%2FReK3pXRjcQuZygDYwVav0dXHPMthdh9Zc3dMLSowoG%2BmPZLAluf5gtrC%2BbhyFsalWbaB%2FbIEmb8Fm&X-Amz-Signature=723b96e3132df2c203b6152bd30e191138be6760fad4a694c5368bccdf21bd22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMNBHB7O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGyI0MDC34mjeq96hs4BtuXuQwwQQ3f17azDQh0eELZVAiEA97BNDr6FIzZGX3SShHOE1FZMMno067jyvBnv56DvDCAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPIVAK6DPzNwiwqo3ircA4ksErQLuPhI0Bh3ksStVZOBgS8Vl1aLgpqCQFoDefGMrj7cLwJcvJ6BKDuaYbSJnNOeg1NaOlh9OMiv2%2FZGV1WIIy9rNNj8CznrlkCye%2BvuhxuQtkE9XWJOcCOlbclCdVA0tq29JUoCW%2BZKiKkhkVWQaS9qUM6hU5RgiGpltgDdU%2F6zasjv6Nrj0%2BJbbsPFGKZyyV1TZMBYEOZtJBpNbc05aJm7czHwCOr%2BPxEZseBAY2e7oSZrNqZl7uOB3lUHTVoXorFjIBcwLN5AQ1ZX0j3LRoA6eN51WCkWqohskNdp%2BVZ1TxuQFM2VncUkX%2BypwYctpPamtZRr9cPsEOCgBOrGlgTdeCX0VoDT07cL2scw3WZ82zSNW5CcjBxz6%2FCi3qVf4VnV0vskTZ3CrgIX6j4zPyFHNRGv0bYMe2Uep8egGbYYoi1Eu85f%2BMK6FAJLsDUC2DZwS2rPbES3Yf8eRckJt%2BBX8ds%2B4GIqIMERlspzrrkimXoxlC8lcslV2hOoevdPko4ZePT4rRY33mLJQ%2B2QqqJT9V%2FSX0v%2FWMnBhXaXYIbIXTqSJh7bwlZcgt2lbL%2BxNRv%2BulV7VvuJy9CH8Bwny2KQ4Wee84ni6xIpKJTFK4kPzFgEwkdH2G5OMMnG%2BLwGOqUBn1ZrNqWIQbcxW38VIOE0aXru0JTvbPipcEbUqBcTReoh4wwntCPlOZklnAekApylm3yzN3nSDOAWguIoavF30rhNNZ%2B4BV1acuxXupxku%2FDdi6r5%2FqBPed35EdafgSZkGv%2FExMXMtu6Gkn%2FReK3pXRjcQuZygDYwVav0dXHPMthdh9Zc3dMLSowoG%2BmPZLAluf5gtrC%2BbhyFsalWbaB%2FbIEmb8Fm&X-Amz-Signature=c04b504d1e8478fdb616617cb822dc97d1ca6b988dd4c0e0730581f033b1eab2&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653J7BJKB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHokWh80x6fQfoOImeXx7pfgil6Pd%2FreFObBZ8wRAlyAIhAKdrTtH3sZ8lsIVMUeXqpkKJ9lmgSRmWknivHWOuvmJcKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzoLU1U6o%2FM3wXnemcq3APzm54g39ahVBxWftcxK89j%2BRZOiA4jv1tLEuoGWFkqKVH3w00JV8%2FISjylfGz8TWPBeP5e9jI%2Fpqk%2FKlRVdgCqf6pFxfMQo%2Bl3qV%2Fb5dMwf0RBkjCYatxTgqjNt01V4r5Z%2FBD5vHEbSr8SZsWreXNvmoPINolE7WHOuQ1Kk%2BUtpPFnMgz%2FaLQV6cYhp9VUdTFUJZ%2BhoTYm%2Bm%2FFDgpdvFZXtEzTDZALKVFXN%2BL%2BY%2BN3JrKIOI%2F%2F%2BKuqcCLvuAuJRQQuP3vlaHOVZJaaWCwxg25FjGO6JeGmC4DeJA%2F9b%2BxiYEGPKF%2F8xAku6W9KV0%2BEKuH7wMX1ftSyQOu6u4exqXK7jBVPQwkGIgmVaaOaWLVaxjoOTuF2fYL2OoM6VElgGw%2FGnGTJRFMtj%2BQIG0DFRhGdLsTWxzBh9tYWwG%2FoFB7mnLXavOC5egv1FPD8rWUR66R3dAclXd8R0BWIGQ81mLuXyP02RnmJDsN%2FMKCc8se4UND9gCs4OeESXQ5A7gWeBrPvtrfZHzOuqt4%2Fi%2FPgIMaWu7K0RUwSNR4J5UsAGAD29ahNtLVhaj5FGRPDh0097ujUg7j5fXTU7hEaz50E8Ei7Z%2BeDrO9BlfuSGke6N1xN8G0NTHVLzq43Kg2AXzC7x%2Fi8BjqkAYuUjPoMVDPk%2FTqO%2B92VoI17%2B5gtfofYXj%2FCF86zavU093DNWL3HZQIwQzih%2FPNddp8HV1%2FZ94s98d2auZPGmT%2BX402oRoeA%2BtqGBQfhsBbCLn4UWjG4zAD8JM6W5tWAGkMG%2B88a2AN%2FHffhub1c95Es45vFubIIpbjAeTC81%2BtvJBO8mgxbcynU%2FY5kKywb27MwYPyS68Fx8pD94nynIhurPc85&X-Amz-Signature=01540186d7ff7f7ab1cbfd1b79332ba371e04dfd7ea18e9e753db3a0a17b9a51&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653J7BJKB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHokWh80x6fQfoOImeXx7pfgil6Pd%2FreFObBZ8wRAlyAIhAKdrTtH3sZ8lsIVMUeXqpkKJ9lmgSRmWknivHWOuvmJcKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzoLU1U6o%2FM3wXnemcq3APzm54g39ahVBxWftcxK89j%2BRZOiA4jv1tLEuoGWFkqKVH3w00JV8%2FISjylfGz8TWPBeP5e9jI%2Fpqk%2FKlRVdgCqf6pFxfMQo%2Bl3qV%2Fb5dMwf0RBkjCYatxTgqjNt01V4r5Z%2FBD5vHEbSr8SZsWreXNvmoPINolE7WHOuQ1Kk%2BUtpPFnMgz%2FaLQV6cYhp9VUdTFUJZ%2BhoTYm%2Bm%2FFDgpdvFZXtEzTDZALKVFXN%2BL%2BY%2BN3JrKIOI%2F%2F%2BKuqcCLvuAuJRQQuP3vlaHOVZJaaWCwxg25FjGO6JeGmC4DeJA%2F9b%2BxiYEGPKF%2F8xAku6W9KV0%2BEKuH7wMX1ftSyQOu6u4exqXK7jBVPQwkGIgmVaaOaWLVaxjoOTuF2fYL2OoM6VElgGw%2FGnGTJRFMtj%2BQIG0DFRhGdLsTWxzBh9tYWwG%2FoFB7mnLXavOC5egv1FPD8rWUR66R3dAclXd8R0BWIGQ81mLuXyP02RnmJDsN%2FMKCc8se4UND9gCs4OeESXQ5A7gWeBrPvtrfZHzOuqt4%2Fi%2FPgIMaWu7K0RUwSNR4J5UsAGAD29ahNtLVhaj5FGRPDh0097ujUg7j5fXTU7hEaz50E8Ei7Z%2BeDrO9BlfuSGke6N1xN8G0NTHVLzq43Kg2AXzC7x%2Fi8BjqkAYuUjPoMVDPk%2FTqO%2B92VoI17%2B5gtfofYXj%2FCF86zavU093DNWL3HZQIwQzih%2FPNddp8HV1%2FZ94s98d2auZPGmT%2BX402oRoeA%2BtqGBQfhsBbCLn4UWjG4zAD8JM6W5tWAGkMG%2B88a2AN%2FHffhub1c95Es45vFubIIpbjAeTC81%2BtvJBO8mgxbcynU%2FY5kKywb27MwYPyS68Fx8pD94nynIhurPc85&X-Amz-Signature=bc2c761823b369e5febfe496be45a536f2ba917840cf39c8b956e92b222ee8dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMNBHB7O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGyI0MDC34mjeq96hs4BtuXuQwwQQ3f17azDQh0eELZVAiEA97BNDr6FIzZGX3SShHOE1FZMMno067jyvBnv56DvDCAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPIVAK6DPzNwiwqo3ircA4ksErQLuPhI0Bh3ksStVZOBgS8Vl1aLgpqCQFoDefGMrj7cLwJcvJ6BKDuaYbSJnNOeg1NaOlh9OMiv2%2FZGV1WIIy9rNNj8CznrlkCye%2BvuhxuQtkE9XWJOcCOlbclCdVA0tq29JUoCW%2BZKiKkhkVWQaS9qUM6hU5RgiGpltgDdU%2F6zasjv6Nrj0%2BJbbsPFGKZyyV1TZMBYEOZtJBpNbc05aJm7czHwCOr%2BPxEZseBAY2e7oSZrNqZl7uOB3lUHTVoXorFjIBcwLN5AQ1ZX0j3LRoA6eN51WCkWqohskNdp%2BVZ1TxuQFM2VncUkX%2BypwYctpPamtZRr9cPsEOCgBOrGlgTdeCX0VoDT07cL2scw3WZ82zSNW5CcjBxz6%2FCi3qVf4VnV0vskTZ3CrgIX6j4zPyFHNRGv0bYMe2Uep8egGbYYoi1Eu85f%2BMK6FAJLsDUC2DZwS2rPbES3Yf8eRckJt%2BBX8ds%2B4GIqIMERlspzrrkimXoxlC8lcslV2hOoevdPko4ZePT4rRY33mLJQ%2B2QqqJT9V%2FSX0v%2FWMnBhXaXYIbIXTqSJh7bwlZcgt2lbL%2BxNRv%2BulV7VvuJy9CH8Bwny2KQ4Wee84ni6xIpKJTFK4kPzFgEwkdH2G5OMMnG%2BLwGOqUBn1ZrNqWIQbcxW38VIOE0aXru0JTvbPipcEbUqBcTReoh4wwntCPlOZklnAekApylm3yzN3nSDOAWguIoavF30rhNNZ%2B4BV1acuxXupxku%2FDdi6r5%2FqBPed35EdafgSZkGv%2FExMXMtu6Gkn%2FReK3pXRjcQuZygDYwVav0dXHPMthdh9Zc3dMLSowoG%2BmPZLAluf5gtrC%2BbhyFsalWbaB%2FbIEmb8Fm&X-Amz-Signature=a53c2d0f4c96d25d484d41b7045bcf13f96847999db9ed98c25a517c5e291832&X-Amz-SignedHeaders=host&x-id=GetObject)
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