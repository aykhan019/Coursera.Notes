

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIPHWM72%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDN%2FSD0QI8EHMOI9ALmla6c1s0lScyYOn9wqy0vbjZm6AiAvJZFYuFhKUbHwFMS2aek0h5e2%2BSiFNTi7yA00JhiU%2Bir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMGHseSzqICs3KR4WjKtwDFMliLEegpCJBoIQSBlpkykrvS3JsjwmI2nKKCbFcHIYtr4wfBxmPmKjWGfk%2FM%2BNo2ThWEv25vz%2B5AJtx9k3TmwyvEwCNAuAes%2BeWKyspF8%2B59VSVH9L6Sc0F53wvl1nG%2BoRQo3ms9xs6iSw0CRKusalwET45c5zrzeyC8ApyIKS31JGlOf48%2FpPyJaoYNI8kfup0sZxPv%2FgQRQX%2B0zTXd%2FF82NBfwzXWw21iS1vI977Z14SWbGAWOarscNiZui4W5j4PF1WrOoddeAXcN9ir5vpjCNTu8QOr56LKFgYdwSTYBxFC%2F7zoKttbieA5hg2EIpATts6sTU6cjXj6W6pNTACSlh0lmJhxRgb0%2B6UsfzoA%2B80E1L2g48akkEl1EOMqfwpd86fdVkQsMk5TY%2FLF%2Fkjdc4ZPtUB8I%2FjXQU44XjNLCaY8frOCNxrVWR%2BzM02SmSUWHzm5juc%2Fp6AKBekj4jB2z95uxCxsVXoAAy5Of%2FuY7E6kOh86ZEMh4bMV2iXLDx%2BkjclZ7oKcscSdsVvZ36dlUYy0R%2BLET0pp04UB3jCB6AviuiHoOUkJ7TsTJUE0aiwtsAvQHSYYWAcMsSW0kS8ZnkDxoIInqS9tZdkZ%2B8LouFj7YjC6GBkdVbkwvYSJvQY6pgHYL7x6M%2BWx8r%2FmI%2FgitzZoFmyYuclDuBF5cpfkTlAtktUav1vs6mfE5pWjv6HvIxiNcDaQkND09ZwCZn%2BRkyg9%2B2aXowj95RnKowupzvdmxCRC64lstOBuIx0IYbaavS%2F45p1kvPSAtUnDUJRGH73%2FjUURg4tVOeWn9kCgoUo1KVgFaR3SY2HIr9g0FMFtSeRWpN78c7MvFhdatlV0NAg%2BBqSYjcJm&X-Amz-Signature=73616efbc6aa54a96fb5e1aa6c1b4338c6c898e2a435622a9ffdcfb0176bfc49&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIPHWM72%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDN%2FSD0QI8EHMOI9ALmla6c1s0lScyYOn9wqy0vbjZm6AiAvJZFYuFhKUbHwFMS2aek0h5e2%2BSiFNTi7yA00JhiU%2Bir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMGHseSzqICs3KR4WjKtwDFMliLEegpCJBoIQSBlpkykrvS3JsjwmI2nKKCbFcHIYtr4wfBxmPmKjWGfk%2FM%2BNo2ThWEv25vz%2B5AJtx9k3TmwyvEwCNAuAes%2BeWKyspF8%2B59VSVH9L6Sc0F53wvl1nG%2BoRQo3ms9xs6iSw0CRKusalwET45c5zrzeyC8ApyIKS31JGlOf48%2FpPyJaoYNI8kfup0sZxPv%2FgQRQX%2B0zTXd%2FF82NBfwzXWw21iS1vI977Z14SWbGAWOarscNiZui4W5j4PF1WrOoddeAXcN9ir5vpjCNTu8QOr56LKFgYdwSTYBxFC%2F7zoKttbieA5hg2EIpATts6sTU6cjXj6W6pNTACSlh0lmJhxRgb0%2B6UsfzoA%2B80E1L2g48akkEl1EOMqfwpd86fdVkQsMk5TY%2FLF%2Fkjdc4ZPtUB8I%2FjXQU44XjNLCaY8frOCNxrVWR%2BzM02SmSUWHzm5juc%2Fp6AKBekj4jB2z95uxCxsVXoAAy5Of%2FuY7E6kOh86ZEMh4bMV2iXLDx%2BkjclZ7oKcscSdsVvZ36dlUYy0R%2BLET0pp04UB3jCB6AviuiHoOUkJ7TsTJUE0aiwtsAvQHSYYWAcMsSW0kS8ZnkDxoIInqS9tZdkZ%2B8LouFj7YjC6GBkdVbkwvYSJvQY6pgHYL7x6M%2BWx8r%2FmI%2FgitzZoFmyYuclDuBF5cpfkTlAtktUav1vs6mfE5pWjv6HvIxiNcDaQkND09ZwCZn%2BRkyg9%2B2aXowj95RnKowupzvdmxCRC64lstOBuIx0IYbaavS%2F45p1kvPSAtUnDUJRGH73%2FjUURg4tVOeWn9kCgoUo1KVgFaR3SY2HIr9g0FMFtSeRWpN78c7MvFhdatlV0NAg%2BBqSYjcJm&X-Amz-Signature=aff92dba7ff6c6208719b9032d5d556146da69f401c9dc9dee5a66c2db21c5a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIPHWM72%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDN%2FSD0QI8EHMOI9ALmla6c1s0lScyYOn9wqy0vbjZm6AiAvJZFYuFhKUbHwFMS2aek0h5e2%2BSiFNTi7yA00JhiU%2Bir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMGHseSzqICs3KR4WjKtwDFMliLEegpCJBoIQSBlpkykrvS3JsjwmI2nKKCbFcHIYtr4wfBxmPmKjWGfk%2FM%2BNo2ThWEv25vz%2B5AJtx9k3TmwyvEwCNAuAes%2BeWKyspF8%2B59VSVH9L6Sc0F53wvl1nG%2BoRQo3ms9xs6iSw0CRKusalwET45c5zrzeyC8ApyIKS31JGlOf48%2FpPyJaoYNI8kfup0sZxPv%2FgQRQX%2B0zTXd%2FF82NBfwzXWw21iS1vI977Z14SWbGAWOarscNiZui4W5j4PF1WrOoddeAXcN9ir5vpjCNTu8QOr56LKFgYdwSTYBxFC%2F7zoKttbieA5hg2EIpATts6sTU6cjXj6W6pNTACSlh0lmJhxRgb0%2B6UsfzoA%2B80E1L2g48akkEl1EOMqfwpd86fdVkQsMk5TY%2FLF%2Fkjdc4ZPtUB8I%2FjXQU44XjNLCaY8frOCNxrVWR%2BzM02SmSUWHzm5juc%2Fp6AKBekj4jB2z95uxCxsVXoAAy5Of%2FuY7E6kOh86ZEMh4bMV2iXLDx%2BkjclZ7oKcscSdsVvZ36dlUYy0R%2BLET0pp04UB3jCB6AviuiHoOUkJ7TsTJUE0aiwtsAvQHSYYWAcMsSW0kS8ZnkDxoIInqS9tZdkZ%2B8LouFj7YjC6GBkdVbkwvYSJvQY6pgHYL7x6M%2BWx8r%2FmI%2FgitzZoFmyYuclDuBF5cpfkTlAtktUav1vs6mfE5pWjv6HvIxiNcDaQkND09ZwCZn%2BRkyg9%2B2aXowj95RnKowupzvdmxCRC64lstOBuIx0IYbaavS%2F45p1kvPSAtUnDUJRGH73%2FjUURg4tVOeWn9kCgoUo1KVgFaR3SY2HIr9g0FMFtSeRWpN78c7MvFhdatlV0NAg%2BBqSYjcJm&X-Amz-Signature=dd9fee11809370cc5f6191370f1461cc9fd88725131c5ece95f27fd0caa9750d&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ27T22C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIEevjRaq2zZ2LSzg21LnlosZQO%2BkCWT7HNHW8jcyKCpNAiAx8sMA4of17%2FNeYBZWWZ8klMJQex0ssI%2B%2BDfRnz%2FKkQCr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMPss%2BTWsBaWDzvHtcKtwDlY6kPUAZILngge8g0nyODyfX101zALBj0CFZzjOyT%2FLxm3nWqew9N3emRt%2Bl5cQRBDb0N0hiNft5aVNgGhm65%2Bmc03ki%2FRj2jr5JJUIlMLyxiAP73rj89OT25OZpO%2FPNkM72NP11nOePb0ruRCDB4HV8iR1L3fCmiJYKbjhLcnVg4%2FR2zwq3YkgdUnZDj61vDHs4ooIiZ%2B5BltwtzFnpH3fs6YGNPXayAyAPuZYjjwKgDaZJXbEZnG9MolHEy%2BheF74L37BI4XcAGXWHulTzW1JUS5VdRaG3RHK1SjQGtVcJy875Om%2FES%2Bo8yeiwNkELJW89QuC31LZuE3PcdSzO59cQVTKliZ7pTqzXhz%2FOH2HbRoC5dKfzqDlDpzLj5NWQi84QCtjor1S%2B8zl9ZYzXbSpN%2FSQtcpc1RNrQXluTZQbYNZhjSvtcgHzTJLe2BuPi%2BiHk8Smyf5zcpvxXowmFoi3iFI6uiCw4odBeXFd5eT06nmbubTC3YDkNBEwx5FCy%2BX3J07mzX4d%2B1QBhXHqK568lPw7z0TUcoz6ydO9D4SFOFXXnWUpVf8qc7GPWYixSiASZpy1CkYnUPI%2BE26cT3B6wLsqnaM5Y73ksoO7idpaLAvmYmdu2G5SBwDAwkoSJvQY6pgEeHjCV75SvXoGQfFcAOZocIUmpn3LfqnxSR04LiAihDJsNhA1r0ZzWFXbhZvzmr6pSKyZFVP2hOeQi%2BYzlRBF56P3pFa%2FBzdSbuJG2EvGsC6OFZMksoedAVj0t1oGXU5MX61n3G8%2BenPg3fpHezBUtoQ8MAuVslxhbf1dQOazXm4zC0P2IY9euIKVUBywda5LoZh9VCRRrp0xvSkQkLeNX%2FdMXzYOE&X-Amz-Signature=93e62e8da93e75576b64eb7426cfd807121def731f5789219c821623d1c440fa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ27T22C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIEevjRaq2zZ2LSzg21LnlosZQO%2BkCWT7HNHW8jcyKCpNAiAx8sMA4of17%2FNeYBZWWZ8klMJQex0ssI%2B%2BDfRnz%2FKkQCr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMPss%2BTWsBaWDzvHtcKtwDlY6kPUAZILngge8g0nyODyfX101zALBj0CFZzjOyT%2FLxm3nWqew9N3emRt%2Bl5cQRBDb0N0hiNft5aVNgGhm65%2Bmc03ki%2FRj2jr5JJUIlMLyxiAP73rj89OT25OZpO%2FPNkM72NP11nOePb0ruRCDB4HV8iR1L3fCmiJYKbjhLcnVg4%2FR2zwq3YkgdUnZDj61vDHs4ooIiZ%2B5BltwtzFnpH3fs6YGNPXayAyAPuZYjjwKgDaZJXbEZnG9MolHEy%2BheF74L37BI4XcAGXWHulTzW1JUS5VdRaG3RHK1SjQGtVcJy875Om%2FES%2Bo8yeiwNkELJW89QuC31LZuE3PcdSzO59cQVTKliZ7pTqzXhz%2FOH2HbRoC5dKfzqDlDpzLj5NWQi84QCtjor1S%2B8zl9ZYzXbSpN%2FSQtcpc1RNrQXluTZQbYNZhjSvtcgHzTJLe2BuPi%2BiHk8Smyf5zcpvxXowmFoi3iFI6uiCw4odBeXFd5eT06nmbubTC3YDkNBEwx5FCy%2BX3J07mzX4d%2B1QBhXHqK568lPw7z0TUcoz6ydO9D4SFOFXXnWUpVf8qc7GPWYixSiASZpy1CkYnUPI%2BE26cT3B6wLsqnaM5Y73ksoO7idpaLAvmYmdu2G5SBwDAwkoSJvQY6pgEeHjCV75SvXoGQfFcAOZocIUmpn3LfqnxSR04LiAihDJsNhA1r0ZzWFXbhZvzmr6pSKyZFVP2hOeQi%2BYzlRBF56P3pFa%2FBzdSbuJG2EvGsC6OFZMksoedAVj0t1oGXU5MX61n3G8%2BenPg3fpHezBUtoQ8MAuVslxhbf1dQOazXm4zC0P2IY9euIKVUBywda5LoZh9VCRRrp0xvSkQkLeNX%2FdMXzYOE&X-Amz-Signature=a3729cc6bd914ec160b76ab481eef6d2805b8c5a0a537f76a647d6d625711ff1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIPHWM72%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIDN%2FSD0QI8EHMOI9ALmla6c1s0lScyYOn9wqy0vbjZm6AiAvJZFYuFhKUbHwFMS2aek0h5e2%2BSiFNTi7yA00JhiU%2Bir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMGHseSzqICs3KR4WjKtwDFMliLEegpCJBoIQSBlpkykrvS3JsjwmI2nKKCbFcHIYtr4wfBxmPmKjWGfk%2FM%2BNo2ThWEv25vz%2B5AJtx9k3TmwyvEwCNAuAes%2BeWKyspF8%2B59VSVH9L6Sc0F53wvl1nG%2BoRQo3ms9xs6iSw0CRKusalwET45c5zrzeyC8ApyIKS31JGlOf48%2FpPyJaoYNI8kfup0sZxPv%2FgQRQX%2B0zTXd%2FF82NBfwzXWw21iS1vI977Z14SWbGAWOarscNiZui4W5j4PF1WrOoddeAXcN9ir5vpjCNTu8QOr56LKFgYdwSTYBxFC%2F7zoKttbieA5hg2EIpATts6sTU6cjXj6W6pNTACSlh0lmJhxRgb0%2B6UsfzoA%2B80E1L2g48akkEl1EOMqfwpd86fdVkQsMk5TY%2FLF%2Fkjdc4ZPtUB8I%2FjXQU44XjNLCaY8frOCNxrVWR%2BzM02SmSUWHzm5juc%2Fp6AKBekj4jB2z95uxCxsVXoAAy5Of%2FuY7E6kOh86ZEMh4bMV2iXLDx%2BkjclZ7oKcscSdsVvZ36dlUYy0R%2BLET0pp04UB3jCB6AviuiHoOUkJ7TsTJUE0aiwtsAvQHSYYWAcMsSW0kS8ZnkDxoIInqS9tZdkZ%2B8LouFj7YjC6GBkdVbkwvYSJvQY6pgHYL7x6M%2BWx8r%2FmI%2FgitzZoFmyYuclDuBF5cpfkTlAtktUav1vs6mfE5pWjv6HvIxiNcDaQkND09ZwCZn%2BRkyg9%2B2aXowj95RnKowupzvdmxCRC64lstOBuIx0IYbaavS%2F45p1kvPSAtUnDUJRGH73%2FjUURg4tVOeWn9kCgoUo1KVgFaR3SY2HIr9g0FMFtSeRWpN78c7MvFhdatlV0NAg%2BBqSYjcJm&X-Amz-Signature=258a341b10e6f5fc99ecb8dec7dcce1017bb6cdfd4e3cd30ca51e8363456fa9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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