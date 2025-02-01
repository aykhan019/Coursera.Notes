

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZBVQBE3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtpV6HhHpk2IMGRWpzY7bA03ZcwidzDjFxURfDwTyYIAiARD%2B89xCs4CWHNvu8bmu0wbJUMosOW3ImnJ%2FdQq5y4AyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvAJyDGxnQL0vlvh5KtwD8NGQROoFWcMeOQaxMdDfMIxV6LkW1wolnE0PJNq1MsNQyxoWyozIwz87YE6%2FDZa0yQBS%2FRybF9%2Ba65Jw95dpH5T8c0ih66YMW8y%2FG84gtlevl0%2FxUcI1AG6VysK8dKJdfLkyL%2B%2BOgvfiFCBOnJbg4jF4nbAk5rzDV%2FIvT9tCWy52BvD3w9ey9QiVo%2FOq%2BQ514BCo6RT3bcmRtQ7lCpWS2PL9oB%2BRsAo8f7iJUEzpm98KaWEfrai92IJXKN0CKOwlpYj116EoEWmK21FS0OYYOHHcFqxZQAQj%2BX6PCW%2BIT%2FPFfDSSVCBcIedShp97jBL8RfxsHsmDRY37vFnALj4E42ppziMwYpi5JxzpKvbNBfb2yg6WKat6BW4wN6DFpx5%2FeBPQmcFysKg1VVYiRlFcSnNYnEUistbXq6Ftx7dc0%2FFaBPyO8RnwlfV1JrMQnEAMzPrcDuDTiQLmK9TtQKxLzA%2BT9lVSe9gyuiUDpMLp2w0%2B01eoWmwsx1%2Fhal%2BOLRDd%2FZeeNREC87w%2FE%2BXSt0LW%2BW57isLounflwfxe0jymRtKeP5gV3EsdvNqO6SLlhK2b4M3RAWRPmJoCiVr9qjrmiOl2BiXoreEP3beGRZo4fTZR7K21jUKL4wl2bN8wvab2vAY6pgFMBKckZED3qeBalx%2Fra%2BkDkrw2eZpXQDxus2Xk19mqkTiWr2a7JP8wQbw0neDyeXtOjMHkTJIZ55vaLo8fj2766%2BnPj0NhXOkJUA%2BC0e%2FwC05%2BvkRmSECPcWuRi%2BK7Y3Wa%2F3hFSyR5ghwildCyWbUZqtq1dmLgDwUHWZx81jmbnNFYhkgXcSII5N7jccZpaO4yNxLYH2BqYMvmLImBWviGMdcC8OgJ&X-Amz-Signature=c589847cfbc6d39187d60abfa1677c8d2ccdc019c76536e38a3844184fdb38a9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZBVQBE3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtpV6HhHpk2IMGRWpzY7bA03ZcwidzDjFxURfDwTyYIAiARD%2B89xCs4CWHNvu8bmu0wbJUMosOW3ImnJ%2FdQq5y4AyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvAJyDGxnQL0vlvh5KtwD8NGQROoFWcMeOQaxMdDfMIxV6LkW1wolnE0PJNq1MsNQyxoWyozIwz87YE6%2FDZa0yQBS%2FRybF9%2Ba65Jw95dpH5T8c0ih66YMW8y%2FG84gtlevl0%2FxUcI1AG6VysK8dKJdfLkyL%2B%2BOgvfiFCBOnJbg4jF4nbAk5rzDV%2FIvT9tCWy52BvD3w9ey9QiVo%2FOq%2BQ514BCo6RT3bcmRtQ7lCpWS2PL9oB%2BRsAo8f7iJUEzpm98KaWEfrai92IJXKN0CKOwlpYj116EoEWmK21FS0OYYOHHcFqxZQAQj%2BX6PCW%2BIT%2FPFfDSSVCBcIedShp97jBL8RfxsHsmDRY37vFnALj4E42ppziMwYpi5JxzpKvbNBfb2yg6WKat6BW4wN6DFpx5%2FeBPQmcFysKg1VVYiRlFcSnNYnEUistbXq6Ftx7dc0%2FFaBPyO8RnwlfV1JrMQnEAMzPrcDuDTiQLmK9TtQKxLzA%2BT9lVSe9gyuiUDpMLp2w0%2B01eoWmwsx1%2Fhal%2BOLRDd%2FZeeNREC87w%2FE%2BXSt0LW%2BW57isLounflwfxe0jymRtKeP5gV3EsdvNqO6SLlhK2b4M3RAWRPmJoCiVr9qjrmiOl2BiXoreEP3beGRZo4fTZR7K21jUKL4wl2bN8wvab2vAY6pgFMBKckZED3qeBalx%2Fra%2BkDkrw2eZpXQDxus2Xk19mqkTiWr2a7JP8wQbw0neDyeXtOjMHkTJIZ55vaLo8fj2766%2BnPj0NhXOkJUA%2BC0e%2FwC05%2BvkRmSECPcWuRi%2BK7Y3Wa%2F3hFSyR5ghwildCyWbUZqtq1dmLgDwUHWZx81jmbnNFYhkgXcSII5N7jccZpaO4yNxLYH2BqYMvmLImBWviGMdcC8OgJ&X-Amz-Signature=82b3ec7f8be9d66305c9767fadb72350db51d36a79c6880fc744f90e00c1734c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZBVQBE3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtpV6HhHpk2IMGRWpzY7bA03ZcwidzDjFxURfDwTyYIAiARD%2B89xCs4CWHNvu8bmu0wbJUMosOW3ImnJ%2FdQq5y4AyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvAJyDGxnQL0vlvh5KtwD8NGQROoFWcMeOQaxMdDfMIxV6LkW1wolnE0PJNq1MsNQyxoWyozIwz87YE6%2FDZa0yQBS%2FRybF9%2Ba65Jw95dpH5T8c0ih66YMW8y%2FG84gtlevl0%2FxUcI1AG6VysK8dKJdfLkyL%2B%2BOgvfiFCBOnJbg4jF4nbAk5rzDV%2FIvT9tCWy52BvD3w9ey9QiVo%2FOq%2BQ514BCo6RT3bcmRtQ7lCpWS2PL9oB%2BRsAo8f7iJUEzpm98KaWEfrai92IJXKN0CKOwlpYj116EoEWmK21FS0OYYOHHcFqxZQAQj%2BX6PCW%2BIT%2FPFfDSSVCBcIedShp97jBL8RfxsHsmDRY37vFnALj4E42ppziMwYpi5JxzpKvbNBfb2yg6WKat6BW4wN6DFpx5%2FeBPQmcFysKg1VVYiRlFcSnNYnEUistbXq6Ftx7dc0%2FFaBPyO8RnwlfV1JrMQnEAMzPrcDuDTiQLmK9TtQKxLzA%2BT9lVSe9gyuiUDpMLp2w0%2B01eoWmwsx1%2Fhal%2BOLRDd%2FZeeNREC87w%2FE%2BXSt0LW%2BW57isLounflwfxe0jymRtKeP5gV3EsdvNqO6SLlhK2b4M3RAWRPmJoCiVr9qjrmiOl2BiXoreEP3beGRZo4fTZR7K21jUKL4wl2bN8wvab2vAY6pgFMBKckZED3qeBalx%2Fra%2BkDkrw2eZpXQDxus2Xk19mqkTiWr2a7JP8wQbw0neDyeXtOjMHkTJIZ55vaLo8fj2766%2BnPj0NhXOkJUA%2BC0e%2FwC05%2BvkRmSECPcWuRi%2BK7Y3Wa%2F3hFSyR5ghwildCyWbUZqtq1dmLgDwUHWZx81jmbnNFYhkgXcSII5N7jccZpaO4yNxLYH2BqYMvmLImBWviGMdcC8OgJ&X-Amz-Signature=39f502a9de40c2a6f4e3852dcf156db2e225ebb72bafdfaf40accb817c233a42&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6TQVVXJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGe4kDq7Yvup7%2BKI2ed%2F7XeHbh1VsBrdEJQYGbbvYM1QIhAPP%2BLD12Z8fN6HQE%2BUn96w3yPmccTjE9iWCND%2FS5D%2FeDKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdPAyQToriyb848eYq3AP1UXOLZBW7R%2FdJWqNDi69rsEEaYRx8o5LzIS6FvnV74VvEhJJCC40KKe3oTfCzt6dpR%2FzrlnQC2aZHuonqcBdtfSIqMDgeQj2X%2FtASKPPcojaafppo59O9fVxdKUSjI2zWsQqE1%2BIlELV%2BUDpZ0QiaQPfeQR%2BCEicRPnBezX0PUcG%2FM18ORfCo1BFFzZgAkmyDUuM0oS68lQ4P3gr6G%2BL41JDh0mRTlhv1k%2FvQCHM7%2BAFzNYJ6Ub8sJxMD1niH9zrK0V9eVSGg3ecqMx%2FxoDNmk3JaWhDR%2Bm5e3%2B1vg1%2B06ef%2F4peaRy2eqT9kB4ER6Lu%2FtFTc4NpmU03AhdOsC8UKP6Bwtp8LpcWdzX%2BWKOP523EeZtk8i1ucljzw3FZ%2B5fpKpmE0nLZJDgLE4iHBnU7GpZmVaciRMcC3jUR%2BNP1CGgzYZFYDTg9%2BrLDGyTExOAn3Hrr0w6%2BYshQcGFe9oRxzT4u3TWPZo2zg9%2B2eBWIHAnpYOxJ2aMaguZccK8vSszxFRz%2FN83uXnv%2FtJ437zHN8coV%2BR%2F29H6sG%2BAG6RCmWQuz72dso%2BATZXdAgkB%2FLcNABUBGASjtbaCLsK%2FD1BWOM5TXZ1Z%2Fqpe1%2BvKfkWfget2EhNPVG3RaIABnW2DD9pfa8BjqkAT529XqvahSC0G64r0Hh3u2Ukt7YL6NF3u9o61%2BhNB0u2CQRaGy3aQfdlEPZqhMDLXAioGKHTVLUUOm3ECut0ltXc7nMlNKxeZ%2B%2BoRd%2FfAOz1BrouNvjUGTmwwZqay64J78%2Bhvu6qSCk3LfutDINqIxIjspEKrFdSjuPYouAUbdzjeMgR%2FyUaE6KwQITwmakiq9Ai4ErADJpeqWKAo8n0EuKVMNz&X-Amz-Signature=dfcda6b333ffa773dbd768a2ea735230a88669b5da6ae8cea3f71ee7e17ebd4b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6TQVVXJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGe4kDq7Yvup7%2BKI2ed%2F7XeHbh1VsBrdEJQYGbbvYM1QIhAPP%2BLD12Z8fN6HQE%2BUn96w3yPmccTjE9iWCND%2FS5D%2FeDKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdPAyQToriyb848eYq3AP1UXOLZBW7R%2FdJWqNDi69rsEEaYRx8o5LzIS6FvnV74VvEhJJCC40KKe3oTfCzt6dpR%2FzrlnQC2aZHuonqcBdtfSIqMDgeQj2X%2FtASKPPcojaafppo59O9fVxdKUSjI2zWsQqE1%2BIlELV%2BUDpZ0QiaQPfeQR%2BCEicRPnBezX0PUcG%2FM18ORfCo1BFFzZgAkmyDUuM0oS68lQ4P3gr6G%2BL41JDh0mRTlhv1k%2FvQCHM7%2BAFzNYJ6Ub8sJxMD1niH9zrK0V9eVSGg3ecqMx%2FxoDNmk3JaWhDR%2Bm5e3%2B1vg1%2B06ef%2F4peaRy2eqT9kB4ER6Lu%2FtFTc4NpmU03AhdOsC8UKP6Bwtp8LpcWdzX%2BWKOP523EeZtk8i1ucljzw3FZ%2B5fpKpmE0nLZJDgLE4iHBnU7GpZmVaciRMcC3jUR%2BNP1CGgzYZFYDTg9%2BrLDGyTExOAn3Hrr0w6%2BYshQcGFe9oRxzT4u3TWPZo2zg9%2B2eBWIHAnpYOxJ2aMaguZccK8vSszxFRz%2FN83uXnv%2FtJ437zHN8coV%2BR%2F29H6sG%2BAG6RCmWQuz72dso%2BATZXdAgkB%2FLcNABUBGASjtbaCLsK%2FD1BWOM5TXZ1Z%2Fqpe1%2BvKfkWfget2EhNPVG3RaIABnW2DD9pfa8BjqkAT529XqvahSC0G64r0Hh3u2Ukt7YL6NF3u9o61%2BhNB0u2CQRaGy3aQfdlEPZqhMDLXAioGKHTVLUUOm3ECut0ltXc7nMlNKxeZ%2B%2BoRd%2FfAOz1BrouNvjUGTmwwZqay64J78%2Bhvu6qSCk3LfutDINqIxIjspEKrFdSjuPYouAUbdzjeMgR%2FyUaE6KwQITwmakiq9Ai4ErADJpeqWKAo8n0EuKVMNz&X-Amz-Signature=e0c855bf755cdf17c32788f8faebc6286ff317469fb9ed0073074e9968f6db62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZBVQBE3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHtpV6HhHpk2IMGRWpzY7bA03ZcwidzDjFxURfDwTyYIAiARD%2B89xCs4CWHNvu8bmu0wbJUMosOW3ImnJ%2FdQq5y4AyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvAJyDGxnQL0vlvh5KtwD8NGQROoFWcMeOQaxMdDfMIxV6LkW1wolnE0PJNq1MsNQyxoWyozIwz87YE6%2FDZa0yQBS%2FRybF9%2Ba65Jw95dpH5T8c0ih66YMW8y%2FG84gtlevl0%2FxUcI1AG6VysK8dKJdfLkyL%2B%2BOgvfiFCBOnJbg4jF4nbAk5rzDV%2FIvT9tCWy52BvD3w9ey9QiVo%2FOq%2BQ514BCo6RT3bcmRtQ7lCpWS2PL9oB%2BRsAo8f7iJUEzpm98KaWEfrai92IJXKN0CKOwlpYj116EoEWmK21FS0OYYOHHcFqxZQAQj%2BX6PCW%2BIT%2FPFfDSSVCBcIedShp97jBL8RfxsHsmDRY37vFnALj4E42ppziMwYpi5JxzpKvbNBfb2yg6WKat6BW4wN6DFpx5%2FeBPQmcFysKg1VVYiRlFcSnNYnEUistbXq6Ftx7dc0%2FFaBPyO8RnwlfV1JrMQnEAMzPrcDuDTiQLmK9TtQKxLzA%2BT9lVSe9gyuiUDpMLp2w0%2B01eoWmwsx1%2Fhal%2BOLRDd%2FZeeNREC87w%2FE%2BXSt0LW%2BW57isLounflwfxe0jymRtKeP5gV3EsdvNqO6SLlhK2b4M3RAWRPmJoCiVr9qjrmiOl2BiXoreEP3beGRZo4fTZR7K21jUKL4wl2bN8wvab2vAY6pgFMBKckZED3qeBalx%2Fra%2BkDkrw2eZpXQDxus2Xk19mqkTiWr2a7JP8wQbw0neDyeXtOjMHkTJIZ55vaLo8fj2766%2BnPj0NhXOkJUA%2BC0e%2FwC05%2BvkRmSECPcWuRi%2BK7Y3Wa%2F3hFSyR5ghwildCyWbUZqtq1dmLgDwUHWZx81jmbnNFYhkgXcSII5N7jccZpaO4yNxLYH2BqYMvmLImBWviGMdcC8OgJ&X-Amz-Signature=1ad2818ba57bf639ef16562187532536bba2bcff53f6dedc893577ce19df6a99&X-Amz-SignedHeaders=host&x-id=GetObject)
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