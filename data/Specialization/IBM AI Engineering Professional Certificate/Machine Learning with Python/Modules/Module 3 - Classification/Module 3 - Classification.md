

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSJOSN4W%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCL2Ma9TOXr4jyoiKdomQPlnm7wK7Jm0mLkDQi4FkRDTAIhALd2nWuL9H9NCCGX35aG8pvO%2FGG5GxYzTWT2t7Hh%2B1GrKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuFJsolx5vimApxjYq3ANIPSIjYOTUE2WCjVRMtNiE2r2SFHK4vtJ5l5y%2BZs%2BOLDS7sV%2FDIsdAn0sDIZ5AM1tQsb%2F2zxb4QUovPq5YXxNmHH7TIGiyak%2B7td73e1T%2BgcNbsxYGdHWa8gjKu5M4sxAp7Z8TDes9vZtTCl2PbyrWXku2X%2FHpWd2mGVhpIzHhQOf8BFVkEzGlAs3PZYzuUG3WfxW%2BApg7KO6Q5k43%2BOjhxJn%2FjygAkbCLebcGrQtPhFkTWy0wweHOtCnutloZujTy14%2Fi5sOVlXopF47s%2B0It%2FZ8SDvc1hf%2FXk%2Bb84ad98ZkRS2juHzgx7l%2FOQFHnK%2F52AMxqBXsODBihQkgewhMXegYBujp0UWRYXVOe8DQaCZK4ERJfem69SEWY6pjj5r3JnUxZz8cjXNmdtuAwNQ%2FHetUQOjl0zTm5xjfVfruwuh4%2FPn3A2OYYUYfTUQtM1BzSGj3w2x5ZDRNDWcMFtU%2Fr6hiOkFX6JsLpXPLgSNbWsBiToslg3tXlM1t9AOfAqRRC8NPiFJGFFgBfA1vw8DQPRvxcrCmuHyf7Zzb4pQkiOyz27PtDQQmSqu4HO3J19zZ4HaCVa2TqrJViIr1XAZYpGpDjFh3Qn6Bw9Lnd5UD29HejeBKH2LVMieGINTDCoOa8BjqkAfrcKnNot2raBQrLSwBvGCIDXgd1qRWDMryR1dSG3pct%2Fa117%2FfgU6lPNdUpPnjxG65yRxCs1hcni5dZkMv1vB4nUba0qltgejuXf8M%2BQvojjo4knyC88lMEpQrdnIV1vkpFAT2%2Fpve34wqOHsSvE%2BGZisUTZnQW7XUw5EBYTnXHHjiHKov5MuCPK%2FAV2eSopTXO7kQd1rvCl0xWAWRAPKlrpGik&X-Amz-Signature=b85af45378fc9618c68b0d030cd47590792e6401fc5953034f263e9dc67703d8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSJOSN4W%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCL2Ma9TOXr4jyoiKdomQPlnm7wK7Jm0mLkDQi4FkRDTAIhALd2nWuL9H9NCCGX35aG8pvO%2FGG5GxYzTWT2t7Hh%2B1GrKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuFJsolx5vimApxjYq3ANIPSIjYOTUE2WCjVRMtNiE2r2SFHK4vtJ5l5y%2BZs%2BOLDS7sV%2FDIsdAn0sDIZ5AM1tQsb%2F2zxb4QUovPq5YXxNmHH7TIGiyak%2B7td73e1T%2BgcNbsxYGdHWa8gjKu5M4sxAp7Z8TDes9vZtTCl2PbyrWXku2X%2FHpWd2mGVhpIzHhQOf8BFVkEzGlAs3PZYzuUG3WfxW%2BApg7KO6Q5k43%2BOjhxJn%2FjygAkbCLebcGrQtPhFkTWy0wweHOtCnutloZujTy14%2Fi5sOVlXopF47s%2B0It%2FZ8SDvc1hf%2FXk%2Bb84ad98ZkRS2juHzgx7l%2FOQFHnK%2F52AMxqBXsODBihQkgewhMXegYBujp0UWRYXVOe8DQaCZK4ERJfem69SEWY6pjj5r3JnUxZz8cjXNmdtuAwNQ%2FHetUQOjl0zTm5xjfVfruwuh4%2FPn3A2OYYUYfTUQtM1BzSGj3w2x5ZDRNDWcMFtU%2Fr6hiOkFX6JsLpXPLgSNbWsBiToslg3tXlM1t9AOfAqRRC8NPiFJGFFgBfA1vw8DQPRvxcrCmuHyf7Zzb4pQkiOyz27PtDQQmSqu4HO3J19zZ4HaCVa2TqrJViIr1XAZYpGpDjFh3Qn6Bw9Lnd5UD29HejeBKH2LVMieGINTDCoOa8BjqkAfrcKnNot2raBQrLSwBvGCIDXgd1qRWDMryR1dSG3pct%2Fa117%2FfgU6lPNdUpPnjxG65yRxCs1hcni5dZkMv1vB4nUba0qltgejuXf8M%2BQvojjo4knyC88lMEpQrdnIV1vkpFAT2%2Fpve34wqOHsSvE%2BGZisUTZnQW7XUw5EBYTnXHHjiHKov5MuCPK%2FAV2eSopTXO7kQd1rvCl0xWAWRAPKlrpGik&X-Amz-Signature=06ac1619bd0b18889cc39ccca4e83dac1f72dde65c6b23c4ad1a7dff3de82a83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSJOSN4W%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCL2Ma9TOXr4jyoiKdomQPlnm7wK7Jm0mLkDQi4FkRDTAIhALd2nWuL9H9NCCGX35aG8pvO%2FGG5GxYzTWT2t7Hh%2B1GrKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuFJsolx5vimApxjYq3ANIPSIjYOTUE2WCjVRMtNiE2r2SFHK4vtJ5l5y%2BZs%2BOLDS7sV%2FDIsdAn0sDIZ5AM1tQsb%2F2zxb4QUovPq5YXxNmHH7TIGiyak%2B7td73e1T%2BgcNbsxYGdHWa8gjKu5M4sxAp7Z8TDes9vZtTCl2PbyrWXku2X%2FHpWd2mGVhpIzHhQOf8BFVkEzGlAs3PZYzuUG3WfxW%2BApg7KO6Q5k43%2BOjhxJn%2FjygAkbCLebcGrQtPhFkTWy0wweHOtCnutloZujTy14%2Fi5sOVlXopF47s%2B0It%2FZ8SDvc1hf%2FXk%2Bb84ad98ZkRS2juHzgx7l%2FOQFHnK%2F52AMxqBXsODBihQkgewhMXegYBujp0UWRYXVOe8DQaCZK4ERJfem69SEWY6pjj5r3JnUxZz8cjXNmdtuAwNQ%2FHetUQOjl0zTm5xjfVfruwuh4%2FPn3A2OYYUYfTUQtM1BzSGj3w2x5ZDRNDWcMFtU%2Fr6hiOkFX6JsLpXPLgSNbWsBiToslg3tXlM1t9AOfAqRRC8NPiFJGFFgBfA1vw8DQPRvxcrCmuHyf7Zzb4pQkiOyz27PtDQQmSqu4HO3J19zZ4HaCVa2TqrJViIr1XAZYpGpDjFh3Qn6Bw9Lnd5UD29HejeBKH2LVMieGINTDCoOa8BjqkAfrcKnNot2raBQrLSwBvGCIDXgd1qRWDMryR1dSG3pct%2Fa117%2FfgU6lPNdUpPnjxG65yRxCs1hcni5dZkMv1vB4nUba0qltgejuXf8M%2BQvojjo4knyC88lMEpQrdnIV1vkpFAT2%2Fpve34wqOHsSvE%2BGZisUTZnQW7XUw5EBYTnXHHjiHKov5MuCPK%2FAV2eSopTXO7kQd1rvCl0xWAWRAPKlrpGik&X-Amz-Signature=96fad9a66bf1e3540d4815f27c30f45a298d26311c66f11819c2c08f13836854&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5BLCWXK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIC2gFZYTXVBcCEoKIZ4gb4y9ArYPamRPNKZ1rObS69IbAiAnNKkH0BFo5y5nXtmHV32GE2tk0d5JkcI7ERtmTdZ6JiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcR%2BN69iyuN4f%2B6bOKtwDMjeq95YgIe6vclePoyh%2FswqlvSW0Z6aQEPv%2FO3GpxAOlquazOflbRN3tWRqwL73w%2FXa6pMRQWV0iSPKhNiRoCXOLHQeOAM28gLxUGqidr7Pak5Jz0HhqFmDaJG%2FgVPJfFoO5054D5rJF6BGxrs2tp9r2f7gBOeayxos1mXzx2pefoQPKuLkp6M4GffnY3mxhwZMEHX194BcrkdVh4%2BBdluYrHQjdyv9T%2F%2BVV9umdhOqlM%2Fc9Ezk4YkMNBJBTrtqsjfSgFvCKtoMa0UzcKYx2WVy2l9xoDfVjpYvHIf%2F%2BGURJSFgF6WtKrcBS0Fz9ZaIFRMo%2FdcmjF8Y15vWV29ZOFHNv46mV8in6cp0xu%2BFCdL3qxMPXy6C%2Bmvpgo%2Bp%2FTUIkEORqrEymL5jP6EGPjHkRz71q6g4z0ntYKHgLzEFq9aSm0Fasbz2s%2B4a3TNnlA8yaQfsxwQpTMqHtgI3dZFpdb1I7fvwUK8p%2B388OCWlcSe9xpQ2t1wP4yAtGymhSgKmyDnJmq3kckYx4owhSuwzG5ep071tTAlA%2Bte52Aamlxl%2BT0Ni4xRLpKB8LMo9OLPQwiUJt492NhHvHyex%2Bis%2BPwCidDOHi4ObhvNV%2B8DAP2m3AdB%2FT9eIhX4IpVBow3brmvAY6pgFlUd6MTXkJSs6%2B9JI3GZzpr%2B8NhXDEP%2F5QEHc1bX8EfnwnDQm8kEddK6HMNlvg4fgFVCjUI2c%2BsRv%2BNs2jd%2FCsXM%2BLffvJpqnWHKT6065twAaIXeqkLM6kcfzfVk3KnWmlpgOnESfttuQZkxiCiphimWYHjm2WsDuzrOQlIHxh2d0wzqU4UgNUJ7v7J9K5ptX%2BKnvLXK3tR49I7iPslRo%2B2K74uk3q&X-Amz-Signature=a80cd5ea9abe70729a12ed2df8e854c2734a0ea124d26e1e654658e45dc7e093&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5BLCWXK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIC2gFZYTXVBcCEoKIZ4gb4y9ArYPamRPNKZ1rObS69IbAiAnNKkH0BFo5y5nXtmHV32GE2tk0d5JkcI7ERtmTdZ6JiqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcR%2BN69iyuN4f%2B6bOKtwDMjeq95YgIe6vclePoyh%2FswqlvSW0Z6aQEPv%2FO3GpxAOlquazOflbRN3tWRqwL73w%2FXa6pMRQWV0iSPKhNiRoCXOLHQeOAM28gLxUGqidr7Pak5Jz0HhqFmDaJG%2FgVPJfFoO5054D5rJF6BGxrs2tp9r2f7gBOeayxos1mXzx2pefoQPKuLkp6M4GffnY3mxhwZMEHX194BcrkdVh4%2BBdluYrHQjdyv9T%2F%2BVV9umdhOqlM%2Fc9Ezk4YkMNBJBTrtqsjfSgFvCKtoMa0UzcKYx2WVy2l9xoDfVjpYvHIf%2F%2BGURJSFgF6WtKrcBS0Fz9ZaIFRMo%2FdcmjF8Y15vWV29ZOFHNv46mV8in6cp0xu%2BFCdL3qxMPXy6C%2Bmvpgo%2Bp%2FTUIkEORqrEymL5jP6EGPjHkRz71q6g4z0ntYKHgLzEFq9aSm0Fasbz2s%2B4a3TNnlA8yaQfsxwQpTMqHtgI3dZFpdb1I7fvwUK8p%2B388OCWlcSe9xpQ2t1wP4yAtGymhSgKmyDnJmq3kckYx4owhSuwzG5ep071tTAlA%2Bte52Aamlxl%2BT0Ni4xRLpKB8LMo9OLPQwiUJt492NhHvHyex%2Bis%2BPwCidDOHi4ObhvNV%2B8DAP2m3AdB%2FT9eIhX4IpVBow3brmvAY6pgFlUd6MTXkJSs6%2B9JI3GZzpr%2B8NhXDEP%2F5QEHc1bX8EfnwnDQm8kEddK6HMNlvg4fgFVCjUI2c%2BsRv%2BNs2jd%2FCsXM%2BLffvJpqnWHKT6065twAaIXeqkLM6kcfzfVk3KnWmlpgOnESfttuQZkxiCiphimWYHjm2WsDuzrOQlIHxh2d0wzqU4UgNUJ7v7J9K5ptX%2BKnvLXK3tR49I7iPslRo%2B2K74uk3q&X-Amz-Signature=ee6bb8c5c801d2c5885989060af1471deb4deeafa21a89623117f645ace3d544&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSJOSN4W%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCL2Ma9TOXr4jyoiKdomQPlnm7wK7Jm0mLkDQi4FkRDTAIhALd2nWuL9H9NCCGX35aG8pvO%2FGG5GxYzTWT2t7Hh%2B1GrKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuFJsolx5vimApxjYq3ANIPSIjYOTUE2WCjVRMtNiE2r2SFHK4vtJ5l5y%2BZs%2BOLDS7sV%2FDIsdAn0sDIZ5AM1tQsb%2F2zxb4QUovPq5YXxNmHH7TIGiyak%2B7td73e1T%2BgcNbsxYGdHWa8gjKu5M4sxAp7Z8TDes9vZtTCl2PbyrWXku2X%2FHpWd2mGVhpIzHhQOf8BFVkEzGlAs3PZYzuUG3WfxW%2BApg7KO6Q5k43%2BOjhxJn%2FjygAkbCLebcGrQtPhFkTWy0wweHOtCnutloZujTy14%2Fi5sOVlXopF47s%2B0It%2FZ8SDvc1hf%2FXk%2Bb84ad98ZkRS2juHzgx7l%2FOQFHnK%2F52AMxqBXsODBihQkgewhMXegYBujp0UWRYXVOe8DQaCZK4ERJfem69SEWY6pjj5r3JnUxZz8cjXNmdtuAwNQ%2FHetUQOjl0zTm5xjfVfruwuh4%2FPn3A2OYYUYfTUQtM1BzSGj3w2x5ZDRNDWcMFtU%2Fr6hiOkFX6JsLpXPLgSNbWsBiToslg3tXlM1t9AOfAqRRC8NPiFJGFFgBfA1vw8DQPRvxcrCmuHyf7Zzb4pQkiOyz27PtDQQmSqu4HO3J19zZ4HaCVa2TqrJViIr1XAZYpGpDjFh3Qn6Bw9Lnd5UD29HejeBKH2LVMieGINTDCoOa8BjqkAfrcKnNot2raBQrLSwBvGCIDXgd1qRWDMryR1dSG3pct%2Fa117%2FfgU6lPNdUpPnjxG65yRxCs1hcni5dZkMv1vB4nUba0qltgejuXf8M%2BQvojjo4knyC88lMEpQrdnIV1vkpFAT2%2Fpve34wqOHsSvE%2BGZisUTZnQW7XUw5EBYTnXHHjiHKov5MuCPK%2FAV2eSopTXO7kQd1rvCl0xWAWRAPKlrpGik&X-Amz-Signature=dd7683dea0f0c47cea4d0951f900035787232620766fb974685c513d4c2bfb00&X-Amz-SignedHeaders=host&x-id=GetObject)
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