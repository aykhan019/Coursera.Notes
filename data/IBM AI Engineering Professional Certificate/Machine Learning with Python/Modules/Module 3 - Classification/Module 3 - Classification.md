

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZOEGEQD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQz0lAhKW2xvUiqozt8wDUifq%2Bx5lXCMno4Ojk%2BSyGLAiEAoDK1RmvAWGFlWjht5SNy0UaKYzsC%2BsVi2FlT0Ay8Wdgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDJ%2FzLaBQBtDJtvrriSrcA%2FXOuFtRCh1OCb2D0vW8ioSOYwBjiwKzUtKlMrpH73vsrG5xiM%2FGvVMEbYb3Ww7QfE0yoU6rqYiHTnOtiFtFnZp7K0iBicLUEZ%2BRTSWMNsHVd3U1d6stgIbkycNAQmiYwXEzU4DXvkRY10oQLa6xEbdX2YuNDb03oVfV%2FJVvUKntFSpOpy4lOg3kaKO5%2F5BTVW7dkJmoANqwBglYfFtfISPNQQaepM%2BrUEiP1EkXWKQHMwF3qoulrinBLPQh2pNhfFKRTt839TO9fTmHsBr396%2BeVWHJXAhS9%2Bzny6GUc3h%2BS6hzQSgaJu3CP5MKjRuABDkbw99LoRkKqXAwR%2BHMmDk26jL99GJCSjjjf%2Ba6dSiXbr%2FyTHdPluYhKhWHnOVhrYxEgL4NFYYaDoPVblnqh7l7RlgzJrZ8mG%2FdYp0Uazq5Cq%2BKfE%2FrRH4BspRjgbMCkuftTsMzPcchbdY0VoEqZ9Qd2%2BvC%2FGB61DpyJ0oFsadiOJ62lS%2BtvpzKYxHgEPgdSjnqxHagEL%2BGW6LDFwj6JgibX0wxyozRlktygKbqU%2Be5%2Fg6W30a4wvDdwjevoU8yzk2LtNMV3dS71YlgRfqDJ9%2F7SkFxsjxykdtdspHzXpbs8gsb8SIV1pLZZLu1MLjzgb0GOqUBmzeKw%2BJ8R2Z7mT9Zl74qD4w%2Bnr%2Bc5xmRKBGsQm%2FV8Rs%2BexWfVTL6Jpt7NOzoTiucoyHA8UKPO8tO79%2FJb4B8jkebHDaIpofmte947iN8ivbOC0l16SuEtw%2BN%2Bgez0i2n5Iz6T0dG4PERc823K2jni1vtfcXSZTdV9WN0DOZ6e61AaBkHFOXqUxIuIRw7O34OQoefsw7v8rzKY3dRyqwPjskM0ePM&X-Amz-Signature=3361d85ae039f6c372c2e07489a37c8115e362fce92951a5e02d4ebd9fd963f6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZOEGEQD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQz0lAhKW2xvUiqozt8wDUifq%2Bx5lXCMno4Ojk%2BSyGLAiEAoDK1RmvAWGFlWjht5SNy0UaKYzsC%2BsVi2FlT0Ay8Wdgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDJ%2FzLaBQBtDJtvrriSrcA%2FXOuFtRCh1OCb2D0vW8ioSOYwBjiwKzUtKlMrpH73vsrG5xiM%2FGvVMEbYb3Ww7QfE0yoU6rqYiHTnOtiFtFnZp7K0iBicLUEZ%2BRTSWMNsHVd3U1d6stgIbkycNAQmiYwXEzU4DXvkRY10oQLa6xEbdX2YuNDb03oVfV%2FJVvUKntFSpOpy4lOg3kaKO5%2F5BTVW7dkJmoANqwBglYfFtfISPNQQaepM%2BrUEiP1EkXWKQHMwF3qoulrinBLPQh2pNhfFKRTt839TO9fTmHsBr396%2BeVWHJXAhS9%2Bzny6GUc3h%2BS6hzQSgaJu3CP5MKjRuABDkbw99LoRkKqXAwR%2BHMmDk26jL99GJCSjjjf%2Ba6dSiXbr%2FyTHdPluYhKhWHnOVhrYxEgL4NFYYaDoPVblnqh7l7RlgzJrZ8mG%2FdYp0Uazq5Cq%2BKfE%2FrRH4BspRjgbMCkuftTsMzPcchbdY0VoEqZ9Qd2%2BvC%2FGB61DpyJ0oFsadiOJ62lS%2BtvpzKYxHgEPgdSjnqxHagEL%2BGW6LDFwj6JgibX0wxyozRlktygKbqU%2Be5%2Fg6W30a4wvDdwjevoU8yzk2LtNMV3dS71YlgRfqDJ9%2F7SkFxsjxykdtdspHzXpbs8gsb8SIV1pLZZLu1MLjzgb0GOqUBmzeKw%2BJ8R2Z7mT9Zl74qD4w%2Bnr%2Bc5xmRKBGsQm%2FV8Rs%2BexWfVTL6Jpt7NOzoTiucoyHA8UKPO8tO79%2FJb4B8jkebHDaIpofmte947iN8ivbOC0l16SuEtw%2BN%2Bgez0i2n5Iz6T0dG4PERc823K2jni1vtfcXSZTdV9WN0DOZ6e61AaBkHFOXqUxIuIRw7O34OQoefsw7v8rzKY3dRyqwPjskM0ePM&X-Amz-Signature=cb8a556b1732dc670f68b5e360c46ce6995e4db684b82f25cfcf3fcbdaca14ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZOEGEQD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQz0lAhKW2xvUiqozt8wDUifq%2Bx5lXCMno4Ojk%2BSyGLAiEAoDK1RmvAWGFlWjht5SNy0UaKYzsC%2BsVi2FlT0Ay8Wdgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDJ%2FzLaBQBtDJtvrriSrcA%2FXOuFtRCh1OCb2D0vW8ioSOYwBjiwKzUtKlMrpH73vsrG5xiM%2FGvVMEbYb3Ww7QfE0yoU6rqYiHTnOtiFtFnZp7K0iBicLUEZ%2BRTSWMNsHVd3U1d6stgIbkycNAQmiYwXEzU4DXvkRY10oQLa6xEbdX2YuNDb03oVfV%2FJVvUKntFSpOpy4lOg3kaKO5%2F5BTVW7dkJmoANqwBglYfFtfISPNQQaepM%2BrUEiP1EkXWKQHMwF3qoulrinBLPQh2pNhfFKRTt839TO9fTmHsBr396%2BeVWHJXAhS9%2Bzny6GUc3h%2BS6hzQSgaJu3CP5MKjRuABDkbw99LoRkKqXAwR%2BHMmDk26jL99GJCSjjjf%2Ba6dSiXbr%2FyTHdPluYhKhWHnOVhrYxEgL4NFYYaDoPVblnqh7l7RlgzJrZ8mG%2FdYp0Uazq5Cq%2BKfE%2FrRH4BspRjgbMCkuftTsMzPcchbdY0VoEqZ9Qd2%2BvC%2FGB61DpyJ0oFsadiOJ62lS%2BtvpzKYxHgEPgdSjnqxHagEL%2BGW6LDFwj6JgibX0wxyozRlktygKbqU%2Be5%2Fg6W30a4wvDdwjevoU8yzk2LtNMV3dS71YlgRfqDJ9%2F7SkFxsjxykdtdspHzXpbs8gsb8SIV1pLZZLu1MLjzgb0GOqUBmzeKw%2BJ8R2Z7mT9Zl74qD4w%2Bnr%2Bc5xmRKBGsQm%2FV8Rs%2BexWfVTL6Jpt7NOzoTiucoyHA8UKPO8tO79%2FJb4B8jkebHDaIpofmte947iN8ivbOC0l16SuEtw%2BN%2Bgez0i2n5Iz6T0dG4PERc823K2jni1vtfcXSZTdV9WN0DOZ6e61AaBkHFOXqUxIuIRw7O34OQoefsw7v8rzKY3dRyqwPjskM0ePM&X-Amz-Signature=6b3cfa67193258c30c3b7233cbe9e50fb3c9c006435281a2d8d6818a0554fd41&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZMHCW55%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJrpr400GghUgbTDUqqXSHwxL2wJss5zmXdQJYVmvpjQIgPYLV1mDMR55ZRV4ScDxTJQzt%2Bnt5ANJ1lFZAUrDiN5gq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLTwucZhc1ISVNZBPyrcAxrk8wOLcRslbwRptp2CrvOXPHD3w0E6%2BqD2cwDFjgR9WNG6Jy364GbwAhOG%2Bh%2Be6E4DpcOrp6Vrk%2BouI772k%2FvQtqUcyiffa%2B%2FeFfWoFL0qCm5hT7IG%2BPuodyM7ZQgXuq1C6xu7%2B68Fdv3246jy6BaPmeLb%2FTtHohbDygxnOchdAEK8FsUw9vowi8kzOi%2Bf4oeiuG7B4ya0c%2F70lvDVBpAdbc0nchTfFYJI7vCa497zsirf5YQ0gbIpJuK0Xa0ZzEfhkhe5p7wxFRSgBQ3D9gwBnDc7cBjlElRx9rqjLspLsTLd6pf0sBg0CE22hV1G5S2xxTMR7rRJy%2BdT5sBgwoMvBK%2B5IxFnWDZrsP7Jg6gv%2FHi7dCavDUycmjlE7ak8GaSSkYB6sUTk5cqIVMW%2FTaTSmTSvJsWjYe3sAEjRjTYeUD4Ywl9BgZYnOWvQ6cRfw9xjMFmQzL28Sw17cGRHyU%2BgyLP1v%2BEcTxJMxbmS6SOqOaiUKycphRGHKrkok7K9XI7vFhFbQZfkpYkOqTdmpU9awSru7AYTQ6Qj%2BZq4Ikg0Owo0oQCmiBNUVzrBJQlB6ccPGdhFTC%2BuZ10gbVKXgU%2BF%2FEQoMnoF%2BGfy9uUIPih9dFBdOSSAUC94h6gaMLvzgb0GOqUB%2FvfguFNXRcGsYJsftaKReHqIsz%2FKfSWUFsmJPVuwAXgFdTSg1Hpk%2FFW%2FGC7FmkKBXmtLTEEd1IOrNHC%2BAfP1SbappG9rKFpRQOn4YoAxf3Xn7H7wMq%2FM9FqkFEnYaneR0Xh3VAZNBnUE5W1FeGgI3Wol03zLoCIn3KkzB230agHsV41cSRdQ6CmpX5eeqQsqJoIGyB5mG86gylnCIRx4HzmDSbn0&X-Amz-Signature=7a437968216e3ea9fff2170d0ef1d9c8f6952f440d4ad4e77628248b2093706a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZMHCW55%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJrpr400GghUgbTDUqqXSHwxL2wJss5zmXdQJYVmvpjQIgPYLV1mDMR55ZRV4ScDxTJQzt%2Bnt5ANJ1lFZAUrDiN5gq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLTwucZhc1ISVNZBPyrcAxrk8wOLcRslbwRptp2CrvOXPHD3w0E6%2BqD2cwDFjgR9WNG6Jy364GbwAhOG%2Bh%2Be6E4DpcOrp6Vrk%2BouI772k%2FvQtqUcyiffa%2B%2FeFfWoFL0qCm5hT7IG%2BPuodyM7ZQgXuq1C6xu7%2B68Fdv3246jy6BaPmeLb%2FTtHohbDygxnOchdAEK8FsUw9vowi8kzOi%2Bf4oeiuG7B4ya0c%2F70lvDVBpAdbc0nchTfFYJI7vCa497zsirf5YQ0gbIpJuK0Xa0ZzEfhkhe5p7wxFRSgBQ3D9gwBnDc7cBjlElRx9rqjLspLsTLd6pf0sBg0CE22hV1G5S2xxTMR7rRJy%2BdT5sBgwoMvBK%2B5IxFnWDZrsP7Jg6gv%2FHi7dCavDUycmjlE7ak8GaSSkYB6sUTk5cqIVMW%2FTaTSmTSvJsWjYe3sAEjRjTYeUD4Ywl9BgZYnOWvQ6cRfw9xjMFmQzL28Sw17cGRHyU%2BgyLP1v%2BEcTxJMxbmS6SOqOaiUKycphRGHKrkok7K9XI7vFhFbQZfkpYkOqTdmpU9awSru7AYTQ6Qj%2BZq4Ikg0Owo0oQCmiBNUVzrBJQlB6ccPGdhFTC%2BuZ10gbVKXgU%2BF%2FEQoMnoF%2BGfy9uUIPih9dFBdOSSAUC94h6gaMLvzgb0GOqUB%2FvfguFNXRcGsYJsftaKReHqIsz%2FKfSWUFsmJPVuwAXgFdTSg1Hpk%2FFW%2FGC7FmkKBXmtLTEEd1IOrNHC%2BAfP1SbappG9rKFpRQOn4YoAxf3Xn7H7wMq%2FM9FqkFEnYaneR0Xh3VAZNBnUE5W1FeGgI3Wol03zLoCIn3KkzB230agHsV41cSRdQ6CmpX5eeqQsqJoIGyB5mG86gylnCIRx4HzmDSbn0&X-Amz-Signature=c3e2674e85cdce9f44815c5b94f410f8a7dd5da86f4013869fdb37bdd7974ea7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZOEGEQD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICQz0lAhKW2xvUiqozt8wDUifq%2Bx5lXCMno4Ojk%2BSyGLAiEAoDK1RmvAWGFlWjht5SNy0UaKYzsC%2BsVi2FlT0Ay8Wdgq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDJ%2FzLaBQBtDJtvrriSrcA%2FXOuFtRCh1OCb2D0vW8ioSOYwBjiwKzUtKlMrpH73vsrG5xiM%2FGvVMEbYb3Ww7QfE0yoU6rqYiHTnOtiFtFnZp7K0iBicLUEZ%2BRTSWMNsHVd3U1d6stgIbkycNAQmiYwXEzU4DXvkRY10oQLa6xEbdX2YuNDb03oVfV%2FJVvUKntFSpOpy4lOg3kaKO5%2F5BTVW7dkJmoANqwBglYfFtfISPNQQaepM%2BrUEiP1EkXWKQHMwF3qoulrinBLPQh2pNhfFKRTt839TO9fTmHsBr396%2BeVWHJXAhS9%2Bzny6GUc3h%2BS6hzQSgaJu3CP5MKjRuABDkbw99LoRkKqXAwR%2BHMmDk26jL99GJCSjjjf%2Ba6dSiXbr%2FyTHdPluYhKhWHnOVhrYxEgL4NFYYaDoPVblnqh7l7RlgzJrZ8mG%2FdYp0Uazq5Cq%2BKfE%2FrRH4BspRjgbMCkuftTsMzPcchbdY0VoEqZ9Qd2%2BvC%2FGB61DpyJ0oFsadiOJ62lS%2BtvpzKYxHgEPgdSjnqxHagEL%2BGW6LDFwj6JgibX0wxyozRlktygKbqU%2Be5%2Fg6W30a4wvDdwjevoU8yzk2LtNMV3dS71YlgRfqDJ9%2F7SkFxsjxykdtdspHzXpbs8gsb8SIV1pLZZLu1MLjzgb0GOqUBmzeKw%2BJ8R2Z7mT9Zl74qD4w%2Bnr%2Bc5xmRKBGsQm%2FV8Rs%2BexWfVTL6Jpt7NOzoTiucoyHA8UKPO8tO79%2FJb4B8jkebHDaIpofmte947iN8ivbOC0l16SuEtw%2BN%2Bgez0i2n5Iz6T0dG4PERc823K2jni1vtfcXSZTdV9WN0DOZ6e61AaBkHFOXqUxIuIRw7O34OQoefsw7v8rzKY3dRyqwPjskM0ePM&X-Amz-Signature=3012884d0d3373b369e78a4e8dee9ac68b7bddaf559f2fd18655f830306e4fe0&X-Amz-SignedHeaders=host&x-id=GetObject)
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