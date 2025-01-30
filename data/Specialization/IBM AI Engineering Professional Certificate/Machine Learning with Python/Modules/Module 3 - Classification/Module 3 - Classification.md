

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDFQOUSS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvPmQc5bNoA%2FKRk2jw%2BXPxxcAgLE8tgDaYYC8DLiDu9gIhANDco8eYzQzBVO%2BueZ9hReVML5u%2FTFq6X8CsWxNeQSxYKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmfn35FDgmwkFua6Qq3AMAS3P8k70YZRPIV2OIT1vutPp0m1UE6Dx03%2BbLDDMlI9hrmKBg%2Fl4zeIJhNRSoNKxWJl8z5B5igjx%2FANUU2dWs61N5V7ZPKUPmSMADM%2FKxz2pu0fGlqLA%2BXLkB126%2BwHk4Cp82JK5%2FfUKX7kNaqUXjNR40oMT%2B3mzChnSqvpGwV%2FH%2FlMfeZ1UOTq4kqfNenpVsAvWKbj86tFWc5h9BY%2F1Re%2FtbQP0WjJuB7ImOE%2F0gY03EI2fX%2BzIXDZ2Q8%2BVnt4vJMR5mZlNfJkh47m%2FKZL7wAAeNxgLz49JNkeoULChGR%2FLUvz%2FEPoGKIqPe7fMtNN8nL8Oct4%2FGYvx%2BEpPkwged25jI5enRN%2BB1ezE%2Fk%2BQVuEk%2Bk2FXDhiTW9%2FUTS8FYQXF0DJQfAmP2vYNxUrp%2FL7plZcI4e7WWXGqlbbsDGeWQcmIF%2BawXXSMzVt5eQh4n0QNaNcSh7d%2FG%2Bp8CBSNP%2F79YxVr64RFMMhQDcB8%2B8gPD1cqpqYHgPKtMg9sMZuxE2XwXMf%2B7Dcpa2vhdTv26W%2BZuUp1hs3wiywFFzeGiRRuCJi6FrdwgXwrPfNPzf8vpEOAhDC3GDIwJOqmsD%2BYwq6%2BTRyS8SZ7IKhsQD1mIwSdeh44CP1upkUCp9%2FpUzCyxe%2B8BjqkAfmsvcJiui6Hbwc4rsPrFGeC9nBsq3zz2rENXN8ZYcrxqaIrS6VDWp7mV0gCqFXf5kf7gyfzWnjPlIAuXUxkJQRAaOi%2FBzhufvRb5PDFFAQLzDuOQ0okt%2FxHGtgU2Mghq8GToqpEB0MfiRSuHLYPCHr78y7Izxv8rb5S49Dul983RtEpkqmjDup%2FRq%2Bk6a%2F%2B%2FJHNAkYyPdoRavVrYn%2FLDtaqa6qE&X-Amz-Signature=94312cd482d38767f1dd8395c60a4cf56466707c1cd45add482bc3efb3c9a7d1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDFQOUSS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvPmQc5bNoA%2FKRk2jw%2BXPxxcAgLE8tgDaYYC8DLiDu9gIhANDco8eYzQzBVO%2BueZ9hReVML5u%2FTFq6X8CsWxNeQSxYKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmfn35FDgmwkFua6Qq3AMAS3P8k70YZRPIV2OIT1vutPp0m1UE6Dx03%2BbLDDMlI9hrmKBg%2Fl4zeIJhNRSoNKxWJl8z5B5igjx%2FANUU2dWs61N5V7ZPKUPmSMADM%2FKxz2pu0fGlqLA%2BXLkB126%2BwHk4Cp82JK5%2FfUKX7kNaqUXjNR40oMT%2B3mzChnSqvpGwV%2FH%2FlMfeZ1UOTq4kqfNenpVsAvWKbj86tFWc5h9BY%2F1Re%2FtbQP0WjJuB7ImOE%2F0gY03EI2fX%2BzIXDZ2Q8%2BVnt4vJMR5mZlNfJkh47m%2FKZL7wAAeNxgLz49JNkeoULChGR%2FLUvz%2FEPoGKIqPe7fMtNN8nL8Oct4%2FGYvx%2BEpPkwged25jI5enRN%2BB1ezE%2Fk%2BQVuEk%2Bk2FXDhiTW9%2FUTS8FYQXF0DJQfAmP2vYNxUrp%2FL7plZcI4e7WWXGqlbbsDGeWQcmIF%2BawXXSMzVt5eQh4n0QNaNcSh7d%2FG%2Bp8CBSNP%2F79YxVr64RFMMhQDcB8%2B8gPD1cqpqYHgPKtMg9sMZuxE2XwXMf%2B7Dcpa2vhdTv26W%2BZuUp1hs3wiywFFzeGiRRuCJi6FrdwgXwrPfNPzf8vpEOAhDC3GDIwJOqmsD%2BYwq6%2BTRyS8SZ7IKhsQD1mIwSdeh44CP1upkUCp9%2FpUzCyxe%2B8BjqkAfmsvcJiui6Hbwc4rsPrFGeC9nBsq3zz2rENXN8ZYcrxqaIrS6VDWp7mV0gCqFXf5kf7gyfzWnjPlIAuXUxkJQRAaOi%2FBzhufvRb5PDFFAQLzDuOQ0okt%2FxHGtgU2Mghq8GToqpEB0MfiRSuHLYPCHr78y7Izxv8rb5S49Dul983RtEpkqmjDup%2FRq%2Bk6a%2F%2B%2FJHNAkYyPdoRavVrYn%2FLDtaqa6qE&X-Amz-Signature=c7d825b73f762dfee220d62615012d085e4c909a0adf0c72634a209333256d84&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDFQOUSS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvPmQc5bNoA%2FKRk2jw%2BXPxxcAgLE8tgDaYYC8DLiDu9gIhANDco8eYzQzBVO%2BueZ9hReVML5u%2FTFq6X8CsWxNeQSxYKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmfn35FDgmwkFua6Qq3AMAS3P8k70YZRPIV2OIT1vutPp0m1UE6Dx03%2BbLDDMlI9hrmKBg%2Fl4zeIJhNRSoNKxWJl8z5B5igjx%2FANUU2dWs61N5V7ZPKUPmSMADM%2FKxz2pu0fGlqLA%2BXLkB126%2BwHk4Cp82JK5%2FfUKX7kNaqUXjNR40oMT%2B3mzChnSqvpGwV%2FH%2FlMfeZ1UOTq4kqfNenpVsAvWKbj86tFWc5h9BY%2F1Re%2FtbQP0WjJuB7ImOE%2F0gY03EI2fX%2BzIXDZ2Q8%2BVnt4vJMR5mZlNfJkh47m%2FKZL7wAAeNxgLz49JNkeoULChGR%2FLUvz%2FEPoGKIqPe7fMtNN8nL8Oct4%2FGYvx%2BEpPkwged25jI5enRN%2BB1ezE%2Fk%2BQVuEk%2Bk2FXDhiTW9%2FUTS8FYQXF0DJQfAmP2vYNxUrp%2FL7plZcI4e7WWXGqlbbsDGeWQcmIF%2BawXXSMzVt5eQh4n0QNaNcSh7d%2FG%2Bp8CBSNP%2F79YxVr64RFMMhQDcB8%2B8gPD1cqpqYHgPKtMg9sMZuxE2XwXMf%2B7Dcpa2vhdTv26W%2BZuUp1hs3wiywFFzeGiRRuCJi6FrdwgXwrPfNPzf8vpEOAhDC3GDIwJOqmsD%2BYwq6%2BTRyS8SZ7IKhsQD1mIwSdeh44CP1upkUCp9%2FpUzCyxe%2B8BjqkAfmsvcJiui6Hbwc4rsPrFGeC9nBsq3zz2rENXN8ZYcrxqaIrS6VDWp7mV0gCqFXf5kf7gyfzWnjPlIAuXUxkJQRAaOi%2FBzhufvRb5PDFFAQLzDuOQ0okt%2FxHGtgU2Mghq8GToqpEB0MfiRSuHLYPCHr78y7Izxv8rb5S49Dul983RtEpkqmjDup%2FRq%2Bk6a%2F%2B%2FJHNAkYyPdoRavVrYn%2FLDtaqa6qE&X-Amz-Signature=a85300d3affa537e83c95df58739cfa3d6b89e5fe88f293e60930a956e78d106&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVADBB4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC80u3CWLRzOccgyYnnowjWu6TL8RqgHKToFs%2Fynm18aAiEA2Nsefha8vcNfcIFgq4b%2BoyFdkSTCkcnO5dg1cSlfWNUqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLFI%2FsSOm6TO2iRrKCrcA7MwjG4OZBCAneMUSJ3urG5SxHJqMnK5RXnREUS3g7umEP0AN0SWLn2uRsWLKsjfAXzmjN8ZsLrUJC1oICscAUUOYfkMDfpts1ATbBL4zvr908lsuQhh%2FWRdrDR6RYDc4X883EqIRpyD0qk0ezhw3gCjtz6x%2B9J1PO9McNRrqf%2BzB4nJ6c9E3hQ8clDdCLsj2mkP1tfVSw%2Bccy6viUe0JLEJtVFqmI0ZfhxhHiUiuQtx4X2EDfR%2BMsQBhmarj0HKbI0qbOxh8aQwafxKSuEXiLdXVv6KdqXTzdySMrp8JyxRBac4JgkOn0LAVgZpSNXnOSaFFv4iWWjFWV4keecd5SDJScOlnQ0AEk%2BP%2B9xvf4H3r53u7PIaHs6ZUFCgQR7BZDKNZjna4H07o2sFof7Xv6p%2FPIP8knAz4eK28VdkhyAMxTuErKtLqNB94S3xFL5xNRE8RHUMbrGVTNqNIsSZAsaktVpIVtW7rl0NWY7zJVLVTYOeBw6KtAxfzxpck3%2BQmykRWt08r3HobPJdMum6nNujB1Be42TIp4IMlHh7sEu%2Bf43qDArKphqMsW%2BGkCJU9zytMzE40NePW7vMAMUdyEicfhqUG5Q9tXwf2LwyYMy21qv044BKPgkGc4w4MNLF77wGOqUBhYgRKl38hJKiNKBM%2BEnukfD%2FkzOWsY4v88qQg%2F%2BsFjBWJlE4XEc2U%2FJjTxRGkbyA5E91bUChYR0FqNGXZcvn%2BY%2BcGFH1M3LqZ4TEwKiDyrSFVAaCL76wKDzlVMOcVrvgJc9Y9vBL2lLUG5saT%2B7NPe%2Bxg3KSnp3DXcC6S4nA9QsfxoE6hO%2FhEaogL9S1h321s1HRLxqr%2Fu6cYDpQSO7TQV3CZUJd&X-Amz-Signature=33000f205aced49f14fe8dad4cd36f72fab08c0625ce14098ab50b478e33ba58&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXVADBB4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC80u3CWLRzOccgyYnnowjWu6TL8RqgHKToFs%2Fynm18aAiEA2Nsefha8vcNfcIFgq4b%2BoyFdkSTCkcnO5dg1cSlfWNUqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLFI%2FsSOm6TO2iRrKCrcA7MwjG4OZBCAneMUSJ3urG5SxHJqMnK5RXnREUS3g7umEP0AN0SWLn2uRsWLKsjfAXzmjN8ZsLrUJC1oICscAUUOYfkMDfpts1ATbBL4zvr908lsuQhh%2FWRdrDR6RYDc4X883EqIRpyD0qk0ezhw3gCjtz6x%2B9J1PO9McNRrqf%2BzB4nJ6c9E3hQ8clDdCLsj2mkP1tfVSw%2Bccy6viUe0JLEJtVFqmI0ZfhxhHiUiuQtx4X2EDfR%2BMsQBhmarj0HKbI0qbOxh8aQwafxKSuEXiLdXVv6KdqXTzdySMrp8JyxRBac4JgkOn0LAVgZpSNXnOSaFFv4iWWjFWV4keecd5SDJScOlnQ0AEk%2BP%2B9xvf4H3r53u7PIaHs6ZUFCgQR7BZDKNZjna4H07o2sFof7Xv6p%2FPIP8knAz4eK28VdkhyAMxTuErKtLqNB94S3xFL5xNRE8RHUMbrGVTNqNIsSZAsaktVpIVtW7rl0NWY7zJVLVTYOeBw6KtAxfzxpck3%2BQmykRWt08r3HobPJdMum6nNujB1Be42TIp4IMlHh7sEu%2Bf43qDArKphqMsW%2BGkCJU9zytMzE40NePW7vMAMUdyEicfhqUG5Q9tXwf2LwyYMy21qv044BKPgkGc4w4MNLF77wGOqUBhYgRKl38hJKiNKBM%2BEnukfD%2FkzOWsY4v88qQg%2F%2BsFjBWJlE4XEc2U%2FJjTxRGkbyA5E91bUChYR0FqNGXZcvn%2BY%2BcGFH1M3LqZ4TEwKiDyrSFVAaCL76wKDzlVMOcVrvgJc9Y9vBL2lLUG5saT%2B7NPe%2Bxg3KSnp3DXcC6S4nA9QsfxoE6hO%2FhEaogL9S1h321s1HRLxqr%2Fu6cYDpQSO7TQV3CZUJd&X-Amz-Signature=cdd3572d2f1222da3462fb3e489008b576799292bcc33ad53701c6a04a0f3d7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDFQOUSS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvPmQc5bNoA%2FKRk2jw%2BXPxxcAgLE8tgDaYYC8DLiDu9gIhANDco8eYzQzBVO%2BueZ9hReVML5u%2FTFq6X8CsWxNeQSxYKogECK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxmfn35FDgmwkFua6Qq3AMAS3P8k70YZRPIV2OIT1vutPp0m1UE6Dx03%2BbLDDMlI9hrmKBg%2Fl4zeIJhNRSoNKxWJl8z5B5igjx%2FANUU2dWs61N5V7ZPKUPmSMADM%2FKxz2pu0fGlqLA%2BXLkB126%2BwHk4Cp82JK5%2FfUKX7kNaqUXjNR40oMT%2B3mzChnSqvpGwV%2FH%2FlMfeZ1UOTq4kqfNenpVsAvWKbj86tFWc5h9BY%2F1Re%2FtbQP0WjJuB7ImOE%2F0gY03EI2fX%2BzIXDZ2Q8%2BVnt4vJMR5mZlNfJkh47m%2FKZL7wAAeNxgLz49JNkeoULChGR%2FLUvz%2FEPoGKIqPe7fMtNN8nL8Oct4%2FGYvx%2BEpPkwged25jI5enRN%2BB1ezE%2Fk%2BQVuEk%2Bk2FXDhiTW9%2FUTS8FYQXF0DJQfAmP2vYNxUrp%2FL7plZcI4e7WWXGqlbbsDGeWQcmIF%2BawXXSMzVt5eQh4n0QNaNcSh7d%2FG%2Bp8CBSNP%2F79YxVr64RFMMhQDcB8%2B8gPD1cqpqYHgPKtMg9sMZuxE2XwXMf%2B7Dcpa2vhdTv26W%2BZuUp1hs3wiywFFzeGiRRuCJi6FrdwgXwrPfNPzf8vpEOAhDC3GDIwJOqmsD%2BYwq6%2BTRyS8SZ7IKhsQD1mIwSdeh44CP1upkUCp9%2FpUzCyxe%2B8BjqkAfmsvcJiui6Hbwc4rsPrFGeC9nBsq3zz2rENXN8ZYcrxqaIrS6VDWp7mV0gCqFXf5kf7gyfzWnjPlIAuXUxkJQRAaOi%2FBzhufvRb5PDFFAQLzDuOQ0okt%2FxHGtgU2Mghq8GToqpEB0MfiRSuHLYPCHr78y7Izxv8rb5S49Dul983RtEpkqmjDup%2FRq%2Bk6a%2F%2B%2FJHNAkYyPdoRavVrYn%2FLDtaqa6qE&X-Amz-Signature=1645f40a0b3b68f2688c40de1449faaaec62bcd821df0561855fe24b98a01625&X-Amz-SignedHeaders=host&x-id=GetObject)
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