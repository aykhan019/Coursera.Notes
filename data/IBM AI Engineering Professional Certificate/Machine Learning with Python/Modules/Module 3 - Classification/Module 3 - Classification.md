

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JDRMLPR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIAmT7Pn7WlinZmEGvUozQ66%2BFHNKSQIyXazlkFcYFnp3AiEA3bKKEBBeITeIv79HDD4EFJTKswbM96xWBgLEbpLG46kq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDK2NsOM%2F6bWqVHUbtyrcA6cK7A9hR%2BLum%2Fvkr2Ddgv8lB23vO8bPYLUDm4ZGNS1Ab7SJ9tdS0SG%2Bvv3f07LGZA1eg%2Bo6%2FOOXo%2FO7qfDpDJ3h9ySkDcRtAaEQLd6NUXVShpG2WiYl07UBYVUM635L%2FSb%2BnimBI5LZV%2BEh2RVRXLi4HmiP43voNWY0fgk1I4Ip8Atkc1UzotadyJd5SQKhyIgUa%2Fdn8wghU73JEG61PxtpmSdbr8FSpW%2BT4rCCFMJg8n9FpWPJd580hkwTh%2FxsEv24%2Bw6IO%2FtXhdHnRrwRrs80PZsYZyEVds3cF7upbLDR4sjq8216X6YTOrDmu1QBwFTOuU%2FxF0LbhMkX9Nu%2BWNsynUFPzC5FJzHo3dvZbEannXn%2BkJLOTFVN9IseNyc5lVgNStX1yIiwpqBJa4aKzttNlYpM6JBxIF2diNc%2FsTyE5Vc66v1ceEDe7JiqouptBwI5AF7MehE6GszF2CsqEIHKD6uw8TfskUuGTV%2B2aupgzt6C23pcERIxOOBnkVoYeMVaNkskCOCqrG3VJKlyMo5zOOxlzQ40wBKpZb%2BPJMdFVtm9Hn2n7%2FUsbrhD9Tw7Fy0qdO9o%2BtWh4YXq6Ysdo0fppfJFFg9p%2F%2BldUFLk%2FuaXYGKp92BJUbN13ea6MKTqhb0GOqUBS3GwlXQieOlLpZGZfMChHIbPQlLBPAOjNHHdgSI5F92Zma42a%2F5wA%2BLr3JK3m2grQxmXbKS4siYGnISNPOCs6GLv0EQsNFuPHl6ZBl0BDpMwKuubK%2BJpyM940%2BA2LDv62Y3hbkX0ufZydyNocTO27YgFAJ9MbbUG4z5xMlg2L9m56NBAelJQ1aQE0mf0d6Sk7Js%2BhVbeAHgBSwjXK8%2F4Dnn8Lbcz&X-Amz-Signature=691fbf07c1f730a137d04e1c379106074fd0b212cf57c7cc9d07dd03642edf95&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JDRMLPR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIAmT7Pn7WlinZmEGvUozQ66%2BFHNKSQIyXazlkFcYFnp3AiEA3bKKEBBeITeIv79HDD4EFJTKswbM96xWBgLEbpLG46kq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDK2NsOM%2F6bWqVHUbtyrcA6cK7A9hR%2BLum%2Fvkr2Ddgv8lB23vO8bPYLUDm4ZGNS1Ab7SJ9tdS0SG%2Bvv3f07LGZA1eg%2Bo6%2FOOXo%2FO7qfDpDJ3h9ySkDcRtAaEQLd6NUXVShpG2WiYl07UBYVUM635L%2FSb%2BnimBI5LZV%2BEh2RVRXLi4HmiP43voNWY0fgk1I4Ip8Atkc1UzotadyJd5SQKhyIgUa%2Fdn8wghU73JEG61PxtpmSdbr8FSpW%2BT4rCCFMJg8n9FpWPJd580hkwTh%2FxsEv24%2Bw6IO%2FtXhdHnRrwRrs80PZsYZyEVds3cF7upbLDR4sjq8216X6YTOrDmu1QBwFTOuU%2FxF0LbhMkX9Nu%2BWNsynUFPzC5FJzHo3dvZbEannXn%2BkJLOTFVN9IseNyc5lVgNStX1yIiwpqBJa4aKzttNlYpM6JBxIF2diNc%2FsTyE5Vc66v1ceEDe7JiqouptBwI5AF7MehE6GszF2CsqEIHKD6uw8TfskUuGTV%2B2aupgzt6C23pcERIxOOBnkVoYeMVaNkskCOCqrG3VJKlyMo5zOOxlzQ40wBKpZb%2BPJMdFVtm9Hn2n7%2FUsbrhD9Tw7Fy0qdO9o%2BtWh4YXq6Ysdo0fppfJFFg9p%2F%2BldUFLk%2FuaXYGKp92BJUbN13ea6MKTqhb0GOqUBS3GwlXQieOlLpZGZfMChHIbPQlLBPAOjNHHdgSI5F92Zma42a%2F5wA%2BLr3JK3m2grQxmXbKS4siYGnISNPOCs6GLv0EQsNFuPHl6ZBl0BDpMwKuubK%2BJpyM940%2BA2LDv62Y3hbkX0ufZydyNocTO27YgFAJ9MbbUG4z5xMlg2L9m56NBAelJQ1aQE0mf0d6Sk7Js%2BhVbeAHgBSwjXK8%2F4Dnn8Lbcz&X-Amz-Signature=fb596217b3a37394e9ba1f28a399339bdac0ca4aa4e10e19134d079024b82379&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JDRMLPR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIAmT7Pn7WlinZmEGvUozQ66%2BFHNKSQIyXazlkFcYFnp3AiEA3bKKEBBeITeIv79HDD4EFJTKswbM96xWBgLEbpLG46kq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDK2NsOM%2F6bWqVHUbtyrcA6cK7A9hR%2BLum%2Fvkr2Ddgv8lB23vO8bPYLUDm4ZGNS1Ab7SJ9tdS0SG%2Bvv3f07LGZA1eg%2Bo6%2FOOXo%2FO7qfDpDJ3h9ySkDcRtAaEQLd6NUXVShpG2WiYl07UBYVUM635L%2FSb%2BnimBI5LZV%2BEh2RVRXLi4HmiP43voNWY0fgk1I4Ip8Atkc1UzotadyJd5SQKhyIgUa%2Fdn8wghU73JEG61PxtpmSdbr8FSpW%2BT4rCCFMJg8n9FpWPJd580hkwTh%2FxsEv24%2Bw6IO%2FtXhdHnRrwRrs80PZsYZyEVds3cF7upbLDR4sjq8216X6YTOrDmu1QBwFTOuU%2FxF0LbhMkX9Nu%2BWNsynUFPzC5FJzHo3dvZbEannXn%2BkJLOTFVN9IseNyc5lVgNStX1yIiwpqBJa4aKzttNlYpM6JBxIF2diNc%2FsTyE5Vc66v1ceEDe7JiqouptBwI5AF7MehE6GszF2CsqEIHKD6uw8TfskUuGTV%2B2aupgzt6C23pcERIxOOBnkVoYeMVaNkskCOCqrG3VJKlyMo5zOOxlzQ40wBKpZb%2BPJMdFVtm9Hn2n7%2FUsbrhD9Tw7Fy0qdO9o%2BtWh4YXq6Ysdo0fppfJFFg9p%2F%2BldUFLk%2FuaXYGKp92BJUbN13ea6MKTqhb0GOqUBS3GwlXQieOlLpZGZfMChHIbPQlLBPAOjNHHdgSI5F92Zma42a%2F5wA%2BLr3JK3m2grQxmXbKS4siYGnISNPOCs6GLv0EQsNFuPHl6ZBl0BDpMwKuubK%2BJpyM940%2BA2LDv62Y3hbkX0ufZydyNocTO27YgFAJ9MbbUG4z5xMlg2L9m56NBAelJQ1aQE0mf0d6Sk7Js%2BhVbeAHgBSwjXK8%2F4Dnn8Lbcz&X-Amz-Signature=db46fda9f6f50212f1dedf99f5c7898802f96150d169e41624d67e4b27d21926&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KX73NOX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDRgSwtybntLxGe9rjDuF8BJa8voteTKyixN8%2Bhpxk1wAIgQwsIM2wBTFXz%2BqTJZuhwN5RFWT%2FtZ%2Bc%2FiFSkdaD0RSQq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDGmEfLPs819iNVlj3yrcA5dvbvTxV5MPQJwmX7z02%2FAi%2Bxhk97QR1nRUEJr4cCMxdrVLosTdnufA%2FULYIxHK6JSXEGEfZVtWydSYtZpdrF1B%2FDOLGhk7FAXCmiUdxv%2B2Cwp41Lrk0nL2QEq6N%2BH764Le5rcLDTePnSWQhVg0yFyr3t7lLK%2B85n9KZ%2BDZoqZPOzwMvfM4Oz9oiRwqT82eZ9FMSbcCW%2BcrR6rmP%2B9RYfraqYYH3ykohnAE8FOVz2SyShpSS7iF6xqjezFin1VOqpsp810RltDV5asP6i%2FuYxMXq%2F6bazN4SZctO2H8TRFLCNGD465R3RobOdQxjoamyfc5pi1d%2BS8zkaR9aNvHzALsLJUqJajYTWHN4gK2hF9JXxyDan1XdwlQ52TcslraXCh2F9z0eIFRMuDoCTOx71c9mtjLhZz7LYaKkaeoVHJJAlGmesgUOUrFrPRAmpAt5XGSIck%2FRQzs1EBl1lH%2BF%2FUpDkVl3CKeFL5fXUWagTAuBuquuodpmMSLBPuZfutsPZpD1dlkMyBkUpBV%2Bdo63P%2BxV9oLrI2EcZIhb8fGHrfoylLcIct8FKcCGeNBt5zon0xDlfgmyVXojxt9KKuLigBAcMS%2BkAfl1v%2F46GQ0kBiAVlBEfo5t%2BSwf4nY%2BMP7ohb0GOqUBFJJ4r%2FcN2jsdnroVX8qi63Xh%2BnrQ7EhAp55%2FPQSe%2BlPM1SosloYPbT%2BH9HrgFosghRUx1LJdicvi%2BZ%2FvdFlh%2Bvd66oWV82s5g18SGpcYYdsDm1PuL42S8%2B%2BDiE61%2F3FdLwxypbdzXJ1Lp0YT4OTPf5TOlua%2Ft3ak3ncD1fEtoVRqyWX4fuNBhTkN1vVXKduGdaodLsEeLk6KGPKT4bebFGWxHWcO&X-Amz-Signature=001f1b18e39522f6f3fe9007565d66b4bc504f7e855c4c472b6d5cb6d4692ee1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KX73NOX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDRgSwtybntLxGe9rjDuF8BJa8voteTKyixN8%2Bhpxk1wAIgQwsIM2wBTFXz%2BqTJZuhwN5RFWT%2FtZ%2Bc%2FiFSkdaD0RSQq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDGmEfLPs819iNVlj3yrcA5dvbvTxV5MPQJwmX7z02%2FAi%2Bxhk97QR1nRUEJr4cCMxdrVLosTdnufA%2FULYIxHK6JSXEGEfZVtWydSYtZpdrF1B%2FDOLGhk7FAXCmiUdxv%2B2Cwp41Lrk0nL2QEq6N%2BH764Le5rcLDTePnSWQhVg0yFyr3t7lLK%2B85n9KZ%2BDZoqZPOzwMvfM4Oz9oiRwqT82eZ9FMSbcCW%2BcrR6rmP%2B9RYfraqYYH3ykohnAE8FOVz2SyShpSS7iF6xqjezFin1VOqpsp810RltDV5asP6i%2FuYxMXq%2F6bazN4SZctO2H8TRFLCNGD465R3RobOdQxjoamyfc5pi1d%2BS8zkaR9aNvHzALsLJUqJajYTWHN4gK2hF9JXxyDan1XdwlQ52TcslraXCh2F9z0eIFRMuDoCTOx71c9mtjLhZz7LYaKkaeoVHJJAlGmesgUOUrFrPRAmpAt5XGSIck%2FRQzs1EBl1lH%2BF%2FUpDkVl3CKeFL5fXUWagTAuBuquuodpmMSLBPuZfutsPZpD1dlkMyBkUpBV%2Bdo63P%2BxV9oLrI2EcZIhb8fGHrfoylLcIct8FKcCGeNBt5zon0xDlfgmyVXojxt9KKuLigBAcMS%2BkAfl1v%2F46GQ0kBiAVlBEfo5t%2BSwf4nY%2BMP7ohb0GOqUBFJJ4r%2FcN2jsdnroVX8qi63Xh%2BnrQ7EhAp55%2FPQSe%2BlPM1SosloYPbT%2BH9HrgFosghRUx1LJdicvi%2BZ%2FvdFlh%2Bvd66oWV82s5g18SGpcYYdsDm1PuL42S8%2B%2BDiE61%2F3FdLwxypbdzXJ1Lp0YT4OTPf5TOlua%2Ft3ak3ncD1fEtoVRqyWX4fuNBhTkN1vVXKduGdaodLsEeLk6KGPKT4bebFGWxHWcO&X-Amz-Signature=d16f09d96e540c4cee09dac5c751578e992b1415710e1638cc0dc054df78b788&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JDRMLPR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIAmT7Pn7WlinZmEGvUozQ66%2BFHNKSQIyXazlkFcYFnp3AiEA3bKKEBBeITeIv79HDD4EFJTKswbM96xWBgLEbpLG46kq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDK2NsOM%2F6bWqVHUbtyrcA6cK7A9hR%2BLum%2Fvkr2Ddgv8lB23vO8bPYLUDm4ZGNS1Ab7SJ9tdS0SG%2Bvv3f07LGZA1eg%2Bo6%2FOOXo%2FO7qfDpDJ3h9ySkDcRtAaEQLd6NUXVShpG2WiYl07UBYVUM635L%2FSb%2BnimBI5LZV%2BEh2RVRXLi4HmiP43voNWY0fgk1I4Ip8Atkc1UzotadyJd5SQKhyIgUa%2Fdn8wghU73JEG61PxtpmSdbr8FSpW%2BT4rCCFMJg8n9FpWPJd580hkwTh%2FxsEv24%2Bw6IO%2FtXhdHnRrwRrs80PZsYZyEVds3cF7upbLDR4sjq8216X6YTOrDmu1QBwFTOuU%2FxF0LbhMkX9Nu%2BWNsynUFPzC5FJzHo3dvZbEannXn%2BkJLOTFVN9IseNyc5lVgNStX1yIiwpqBJa4aKzttNlYpM6JBxIF2diNc%2FsTyE5Vc66v1ceEDe7JiqouptBwI5AF7MehE6GszF2CsqEIHKD6uw8TfskUuGTV%2B2aupgzt6C23pcERIxOOBnkVoYeMVaNkskCOCqrG3VJKlyMo5zOOxlzQ40wBKpZb%2BPJMdFVtm9Hn2n7%2FUsbrhD9Tw7Fy0qdO9o%2BtWh4YXq6Ysdo0fppfJFFg9p%2F%2BldUFLk%2FuaXYGKp92BJUbN13ea6MKTqhb0GOqUBS3GwlXQieOlLpZGZfMChHIbPQlLBPAOjNHHdgSI5F92Zma42a%2F5wA%2BLr3JK3m2grQxmXbKS4siYGnISNPOCs6GLv0EQsNFuPHl6ZBl0BDpMwKuubK%2BJpyM940%2BA2LDv62Y3hbkX0ufZydyNocTO27YgFAJ9MbbUG4z5xMlg2L9m56NBAelJQ1aQE0mf0d6Sk7Js%2BhVbeAHgBSwjXK8%2F4Dnn8Lbcz&X-Amz-Signature=a5b93124bac59066ea754682087fe069463fe7abe74fd32889ab052d3a928920&X-Amz-SignedHeaders=host&x-id=GetObject)
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