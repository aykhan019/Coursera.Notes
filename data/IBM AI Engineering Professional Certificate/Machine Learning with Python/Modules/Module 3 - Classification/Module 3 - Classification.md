

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SA5TPCHE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFiNz3vLEhnh4otwOpHomsNA137LUHLbi%2B%2B98w1SVTCAiEA%2Fw%2BoI%2B5vXii%2F%2B9DdH0RIECAmrPSAJhSZfShh%2Bv%2FAdB8qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOptm8WrTRGNzZyupyrcA8upoPeLzNE63rH0t4DZo9EKTnsBU7jkY4P3EeEfEGurHAANrz8Z8%2FmzVr%2Fk3pIfynzWyWHhh4wJb4Ck9hEZI3w5Uidu49gjZv6iEsxnrQo1vbNk%2BskIwCkEbRwhFSonmqRjFxLxx6LSK57WAs3JcjDk5NYJZ%2B2NHoDJVRjLMjkjw8Oau5sv7fj%2BYetYIID4ekHwCXTX9Ycef6yBN78vNhJATFOPf6kUP47jiJjJhss5%2FOWxKUoOHVz%2Fx9uo73uYCr4%2BXqi%2BcTaw5z5pfeqKX1kNl8MXmjkYLwpNVjhICrvh%2Fo8291CeBzrbP7bhUDv95zPOiLTDLFjOdcvvnw%2FVxPXXz08U0fKr8H5E3xGVvmhKi2ucyZkqzH78vZRwZCsAHpo%2BDcGb96OVxf6l0WqiqnBO87k61tWtQv%2FqXYdVYCgsfoLhcnvesDSIXYq3X%2BfUbwjqvD7QyLuCbnW0gYhuZkLnoA8161tZgJ5d6Xu2Cod89STPAvCkwY55JTCiYuaoNwNlGzmkKd8QFM08G8BXBXrLCSdnaAhSNB%2FbGRGoT2F%2B%2B80o3PzW%2F9uUguHUrR8VA%2BuUnJyttmFXPFBpIc%2FsbMmsB%2FmrEPR%2Bd6cwqi9s5KYeaufye7wu9k%2FS3Pt6MOCb%2FLwGOqUBAID1rgYZHxLUTqS3mbRpIK2ZCR5Nd76t%2BvBpdt6U%2B1mzG%2FBNeMXA9gCv33I5PSZ7IMGiB6mPrjP%2FOv%2BnB9MlCJSn2JoNR1lr1X4B9%2F5s7JascpAv2UBOvHrajEkxr6uJUseaY%2BW%2B9G%2BRSYaQp9t%2BKMl37%2BpuZefwieoIJyPAwpS9wmSrVmkrxhqUAkzyL%2FIlOqBphW7bvSqyHAzpcqKCQSrj4FOt&X-Amz-Signature=cb114ec9d40a07af56d6a8bc2c61c3411224f228d7d0ab1c9a70d863dcc1006e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SA5TPCHE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFiNz3vLEhnh4otwOpHomsNA137LUHLbi%2B%2B98w1SVTCAiEA%2Fw%2BoI%2B5vXii%2F%2B9DdH0RIECAmrPSAJhSZfShh%2Bv%2FAdB8qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOptm8WrTRGNzZyupyrcA8upoPeLzNE63rH0t4DZo9EKTnsBU7jkY4P3EeEfEGurHAANrz8Z8%2FmzVr%2Fk3pIfynzWyWHhh4wJb4Ck9hEZI3w5Uidu49gjZv6iEsxnrQo1vbNk%2BskIwCkEbRwhFSonmqRjFxLxx6LSK57WAs3JcjDk5NYJZ%2B2NHoDJVRjLMjkjw8Oau5sv7fj%2BYetYIID4ekHwCXTX9Ycef6yBN78vNhJATFOPf6kUP47jiJjJhss5%2FOWxKUoOHVz%2Fx9uo73uYCr4%2BXqi%2BcTaw5z5pfeqKX1kNl8MXmjkYLwpNVjhICrvh%2Fo8291CeBzrbP7bhUDv95zPOiLTDLFjOdcvvnw%2FVxPXXz08U0fKr8H5E3xGVvmhKi2ucyZkqzH78vZRwZCsAHpo%2BDcGb96OVxf6l0WqiqnBO87k61tWtQv%2FqXYdVYCgsfoLhcnvesDSIXYq3X%2BfUbwjqvD7QyLuCbnW0gYhuZkLnoA8161tZgJ5d6Xu2Cod89STPAvCkwY55JTCiYuaoNwNlGzmkKd8QFM08G8BXBXrLCSdnaAhSNB%2FbGRGoT2F%2B%2B80o3PzW%2F9uUguHUrR8VA%2BuUnJyttmFXPFBpIc%2FsbMmsB%2FmrEPR%2Bd6cwqi9s5KYeaufye7wu9k%2FS3Pt6MOCb%2FLwGOqUBAID1rgYZHxLUTqS3mbRpIK2ZCR5Nd76t%2BvBpdt6U%2B1mzG%2FBNeMXA9gCv33I5PSZ7IMGiB6mPrjP%2FOv%2BnB9MlCJSn2JoNR1lr1X4B9%2F5s7JascpAv2UBOvHrajEkxr6uJUseaY%2BW%2B9G%2BRSYaQp9t%2BKMl37%2BpuZefwieoIJyPAwpS9wmSrVmkrxhqUAkzyL%2FIlOqBphW7bvSqyHAzpcqKCQSrj4FOt&X-Amz-Signature=f7a092ed6b2562e16a420226d8c3782614a32cc591bf6b0cb0cbd4a45aba12fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SA5TPCHE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFiNz3vLEhnh4otwOpHomsNA137LUHLbi%2B%2B98w1SVTCAiEA%2Fw%2BoI%2B5vXii%2F%2B9DdH0RIECAmrPSAJhSZfShh%2Bv%2FAdB8qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOptm8WrTRGNzZyupyrcA8upoPeLzNE63rH0t4DZo9EKTnsBU7jkY4P3EeEfEGurHAANrz8Z8%2FmzVr%2Fk3pIfynzWyWHhh4wJb4Ck9hEZI3w5Uidu49gjZv6iEsxnrQo1vbNk%2BskIwCkEbRwhFSonmqRjFxLxx6LSK57WAs3JcjDk5NYJZ%2B2NHoDJVRjLMjkjw8Oau5sv7fj%2BYetYIID4ekHwCXTX9Ycef6yBN78vNhJATFOPf6kUP47jiJjJhss5%2FOWxKUoOHVz%2Fx9uo73uYCr4%2BXqi%2BcTaw5z5pfeqKX1kNl8MXmjkYLwpNVjhICrvh%2Fo8291CeBzrbP7bhUDv95zPOiLTDLFjOdcvvnw%2FVxPXXz08U0fKr8H5E3xGVvmhKi2ucyZkqzH78vZRwZCsAHpo%2BDcGb96OVxf6l0WqiqnBO87k61tWtQv%2FqXYdVYCgsfoLhcnvesDSIXYq3X%2BfUbwjqvD7QyLuCbnW0gYhuZkLnoA8161tZgJ5d6Xu2Cod89STPAvCkwY55JTCiYuaoNwNlGzmkKd8QFM08G8BXBXrLCSdnaAhSNB%2FbGRGoT2F%2B%2B80o3PzW%2F9uUguHUrR8VA%2BuUnJyttmFXPFBpIc%2FsbMmsB%2FmrEPR%2Bd6cwqi9s5KYeaufye7wu9k%2FS3Pt6MOCb%2FLwGOqUBAID1rgYZHxLUTqS3mbRpIK2ZCR5Nd76t%2BvBpdt6U%2B1mzG%2FBNeMXA9gCv33I5PSZ7IMGiB6mPrjP%2FOv%2BnB9MlCJSn2JoNR1lr1X4B9%2F5s7JascpAv2UBOvHrajEkxr6uJUseaY%2BW%2B9G%2BRSYaQp9t%2BKMl37%2BpuZefwieoIJyPAwpS9wmSrVmkrxhqUAkzyL%2FIlOqBphW7bvSqyHAzpcqKCQSrj4FOt&X-Amz-Signature=f68c1975d49a903ce96aaef0558ddaecb57e269cd0db7f04848be37bf1c5b147&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOVPTAOO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBeLV0c3gA8D%2BbhQT7a6VvnSPqItprkWvtH9q96sJ5XCAiEAy38T8jVIQJYWnCQdsPaWwkNB2hzjxxNyEETUbYVMTLUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDioElNWDtBW%2BcJuVircA9OC0t2PvvFXbGL%2B7cXutjvE93SKs30b99Pqr2z%2FrBa0daGSXka4NvlhIXyb%2FEa3zVd5fW4uRR3bAM0cURfb4X2XTNrdwu1w9jIQnZgUD%2BliktpCQBRWSVbXW2%2BD8d1cMIavjEjg9MvIuRxKi9cfylIrUP%2B3q8mV2yD6T3m8Sr0%2BQgvhQEAvqYAWuOIh101B7nnpM4QS7oyPgeC0ckwNvYzNXhkIj%2FRJ90eLnrzNFN2xQ659bapBrT9VafxRmDDylRQXq8LOs%2F0qMm8WSgoz506vuIosYzzgisiWEb5gWcl2ToffTDZ%2BPUucUfL2OOfTlSTlsgrm7eO6YZ%2B62jvFUdS%2BI0Mf3enTN58n3eyVFpbhIlzpUI9bm%2B7lDtUCZFGdvCjGkOhCaB%2BPc%2BbiUlEpNtHURaLeYWlYwXM5wW8zivQDjpi7Rmjo%2FoZ3pWHwlPgOFR5VIF2O568B%2BMfrHz1zWQVMp8AbhSNII2Wk7dmO8t%2F%2BMhEV0p4BEQbUN1JJhMJHnfUd7P0bRbelMmNmuhstajrKV5wiJWG8zW9O9e3LJjSgcy1gWWPLzK2jm15s0zAsMmXXCMg6W6mwgW180fO0IKjekJQrqLSxOJUPD9fTcu%2B4jxO7aBnviiBek%2FpWMJac%2FLwGOqUBBErzbV%2Fz10nMu23TqvRVLWGfLj3HSRfIKcAGkdEPLmtYJ7OiS1dzZfK4AtoXnpQC1x7LoH2AxSGDKB3XDtwkrX9PnABckPpIiVKtWmageabI%2BkCPbVtlklFYtRck8%2Fl2LXYPJOo%2BD%2B79ow4FQcKTPJoh3%2BangwrnwL5tMuu9gDs1idOqZuSoAFnv0s6fodFJbpbnVP1FesCoLqnKQ4h0gNH1WoAs&X-Amz-Signature=c63fede85da214b4e854b87dab4badadbcc64dcf65b9e060bb2ceda6b5ae4033&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOVPTAOO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBeLV0c3gA8D%2BbhQT7a6VvnSPqItprkWvtH9q96sJ5XCAiEAy38T8jVIQJYWnCQdsPaWwkNB2hzjxxNyEETUbYVMTLUqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDioElNWDtBW%2BcJuVircA9OC0t2PvvFXbGL%2B7cXutjvE93SKs30b99Pqr2z%2FrBa0daGSXka4NvlhIXyb%2FEa3zVd5fW4uRR3bAM0cURfb4X2XTNrdwu1w9jIQnZgUD%2BliktpCQBRWSVbXW2%2BD8d1cMIavjEjg9MvIuRxKi9cfylIrUP%2B3q8mV2yD6T3m8Sr0%2BQgvhQEAvqYAWuOIh101B7nnpM4QS7oyPgeC0ckwNvYzNXhkIj%2FRJ90eLnrzNFN2xQ659bapBrT9VafxRmDDylRQXq8LOs%2F0qMm8WSgoz506vuIosYzzgisiWEb5gWcl2ToffTDZ%2BPUucUfL2OOfTlSTlsgrm7eO6YZ%2B62jvFUdS%2BI0Mf3enTN58n3eyVFpbhIlzpUI9bm%2B7lDtUCZFGdvCjGkOhCaB%2BPc%2BbiUlEpNtHURaLeYWlYwXM5wW8zivQDjpi7Rmjo%2FoZ3pWHwlPgOFR5VIF2O568B%2BMfrHz1zWQVMp8AbhSNII2Wk7dmO8t%2F%2BMhEV0p4BEQbUN1JJhMJHnfUd7P0bRbelMmNmuhstajrKV5wiJWG8zW9O9e3LJjSgcy1gWWPLzK2jm15s0zAsMmXXCMg6W6mwgW180fO0IKjekJQrqLSxOJUPD9fTcu%2B4jxO7aBnviiBek%2FpWMJac%2FLwGOqUBBErzbV%2Fz10nMu23TqvRVLWGfLj3HSRfIKcAGkdEPLmtYJ7OiS1dzZfK4AtoXnpQC1x7LoH2AxSGDKB3XDtwkrX9PnABckPpIiVKtWmageabI%2BkCPbVtlklFYtRck8%2Fl2LXYPJOo%2BD%2B79ow4FQcKTPJoh3%2BangwrnwL5tMuu9gDs1idOqZuSoAFnv0s6fodFJbpbnVP1FesCoLqnKQ4h0gNH1WoAs&X-Amz-Signature=5192e507acc622cf611bc79d6be14d1305a3ebbd4906f476649643191784b70e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SA5TPCHE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T111143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFiNz3vLEhnh4otwOpHomsNA137LUHLbi%2B%2B98w1SVTCAiEA%2Fw%2BoI%2B5vXii%2F%2B9DdH0RIECAmrPSAJhSZfShh%2Bv%2FAdB8qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOptm8WrTRGNzZyupyrcA8upoPeLzNE63rH0t4DZo9EKTnsBU7jkY4P3EeEfEGurHAANrz8Z8%2FmzVr%2Fk3pIfynzWyWHhh4wJb4Ck9hEZI3w5Uidu49gjZv6iEsxnrQo1vbNk%2BskIwCkEbRwhFSonmqRjFxLxx6LSK57WAs3JcjDk5NYJZ%2B2NHoDJVRjLMjkjw8Oau5sv7fj%2BYetYIID4ekHwCXTX9Ycef6yBN78vNhJATFOPf6kUP47jiJjJhss5%2FOWxKUoOHVz%2Fx9uo73uYCr4%2BXqi%2BcTaw5z5pfeqKX1kNl8MXmjkYLwpNVjhICrvh%2Fo8291CeBzrbP7bhUDv95zPOiLTDLFjOdcvvnw%2FVxPXXz08U0fKr8H5E3xGVvmhKi2ucyZkqzH78vZRwZCsAHpo%2BDcGb96OVxf6l0WqiqnBO87k61tWtQv%2FqXYdVYCgsfoLhcnvesDSIXYq3X%2BfUbwjqvD7QyLuCbnW0gYhuZkLnoA8161tZgJ5d6Xu2Cod89STPAvCkwY55JTCiYuaoNwNlGzmkKd8QFM08G8BXBXrLCSdnaAhSNB%2FbGRGoT2F%2B%2B80o3PzW%2F9uUguHUrR8VA%2BuUnJyttmFXPFBpIc%2FsbMmsB%2FmrEPR%2Bd6cwqi9s5KYeaufye7wu9k%2FS3Pt6MOCb%2FLwGOqUBAID1rgYZHxLUTqS3mbRpIK2ZCR5Nd76t%2BvBpdt6U%2B1mzG%2FBNeMXA9gCv33I5PSZ7IMGiB6mPrjP%2FOv%2BnB9MlCJSn2JoNR1lr1X4B9%2F5s7JascpAv2UBOvHrajEkxr6uJUseaY%2BW%2B9G%2BRSYaQp9t%2BKMl37%2BpuZefwieoIJyPAwpS9wmSrVmkrxhqUAkzyL%2FIlOqBphW7bvSqyHAzpcqKCQSrj4FOt&X-Amz-Signature=fb2bff754de66e2a0044e23ae8f504bd23de5f9fbdc7dc9c19e8db9893e2b693&X-Amz-SignedHeaders=host&x-id=GetObject)
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