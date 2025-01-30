

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZEFUTQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFJbSvWN3p7bW9TzS%2FGBu4rna%2B1nmzzMXEcShyDkUThwIhAIp7MFo5lkMqMQBgunYp00NuXEMcv5o%2BrSZLpoDQRvX2KogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7o5D1wv2CPStCSVAq3APyqRZr15YMWLUZ1vl08syva5%2Fa3tZjc4bf5SHqDmBwGG4T84zhlqzbAwf6bdZP2xRnhPC2ZIvQ4YwK8cUTQd9fvJK7WKwInHC7%2FaZTFzPFI5XrbO%2FxqXc4gLkSPuurIN9MHCJsXy46du79AJCld5jpE%2BaCeLISGQvLDmGoX%2Fx2TiKX%2B2jTowKTz7kFUp9FLw5FlPZqLR7ZM%2BhSYqNUqVe0gwAwqwVyA5zqe%2BhTqtSucI906Ih017UwtDIhixzO8MBZKhc0joRpTQqGnSHeXBTFY6LhapSlP0qSUijQquasI5dD9BkQqlWKCFsr0uiocRp8fNDc1WvlWU%2BqVCruft1%2BuP9T2dQfiFnxTZ0tI8xItIOukrOp8UZHt5RP3Fax3Dd3vdg5Ku1A1v9WhcbLKpXzHbWz4CxNn8qSKS19JkDzToizNAvaBE1Vz8Yfx7JmOw1pu1mu4zmqHxMgEpnFvzMKXUshYqJFmex2bgqXwd9gfSGqXrlsSi1mvTRPhr82L4Xud0v9hzejkMGr6Hovglwi%2FOjYp30AYUjZmS%2F1kXt92DQBCzW7XnsjdxiPHWDtXq1Bfs7QJrCqsiztF3%2FHKtnHGf9cmELYWFvOtehRxeIPvHvxuhFd7Yg0kj5dWDCR1%2B68BjqkAff2pVZukPAxr%2FsyAJSwSsof5zpl3fxGYPIf09EhbXpyJDC476mZ%2BJ01tgP9hXUz42hKZelEnAfciEjVsn20i19TztgUdafU%2BGW%2BSlgAP8P2zlzfMSGLI5wNnDjJFslyk9Z%2BuCaLT2Q7IOhLQrLq8sDyYziQMq9G%2BS6lHSD2d9dJKC1BnPbP0xHG%2BuWYxxfa%2FqrQhOsnTyCtnk1yyGx5H8b69pDE&X-Amz-Signature=593969e1413abbabe011a0f1488c6aa1665222855e2e69f380d8e2f911fe89dd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZEFUTQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFJbSvWN3p7bW9TzS%2FGBu4rna%2B1nmzzMXEcShyDkUThwIhAIp7MFo5lkMqMQBgunYp00NuXEMcv5o%2BrSZLpoDQRvX2KogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7o5D1wv2CPStCSVAq3APyqRZr15YMWLUZ1vl08syva5%2Fa3tZjc4bf5SHqDmBwGG4T84zhlqzbAwf6bdZP2xRnhPC2ZIvQ4YwK8cUTQd9fvJK7WKwInHC7%2FaZTFzPFI5XrbO%2FxqXc4gLkSPuurIN9MHCJsXy46du79AJCld5jpE%2BaCeLISGQvLDmGoX%2Fx2TiKX%2B2jTowKTz7kFUp9FLw5FlPZqLR7ZM%2BhSYqNUqVe0gwAwqwVyA5zqe%2BhTqtSucI906Ih017UwtDIhixzO8MBZKhc0joRpTQqGnSHeXBTFY6LhapSlP0qSUijQquasI5dD9BkQqlWKCFsr0uiocRp8fNDc1WvlWU%2BqVCruft1%2BuP9T2dQfiFnxTZ0tI8xItIOukrOp8UZHt5RP3Fax3Dd3vdg5Ku1A1v9WhcbLKpXzHbWz4CxNn8qSKS19JkDzToizNAvaBE1Vz8Yfx7JmOw1pu1mu4zmqHxMgEpnFvzMKXUshYqJFmex2bgqXwd9gfSGqXrlsSi1mvTRPhr82L4Xud0v9hzejkMGr6Hovglwi%2FOjYp30AYUjZmS%2F1kXt92DQBCzW7XnsjdxiPHWDtXq1Bfs7QJrCqsiztF3%2FHKtnHGf9cmELYWFvOtehRxeIPvHvxuhFd7Yg0kj5dWDCR1%2B68BjqkAff2pVZukPAxr%2FsyAJSwSsof5zpl3fxGYPIf09EhbXpyJDC476mZ%2BJ01tgP9hXUz42hKZelEnAfciEjVsn20i19TztgUdafU%2BGW%2BSlgAP8P2zlzfMSGLI5wNnDjJFslyk9Z%2BuCaLT2Q7IOhLQrLq8sDyYziQMq9G%2BS6lHSD2d9dJKC1BnPbP0xHG%2BuWYxxfa%2FqrQhOsnTyCtnk1yyGx5H8b69pDE&X-Amz-Signature=2d7a3eeac9c546b02454258e5f461310ad74e875c28a1596cc25229ebb0794e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZEFUTQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFJbSvWN3p7bW9TzS%2FGBu4rna%2B1nmzzMXEcShyDkUThwIhAIp7MFo5lkMqMQBgunYp00NuXEMcv5o%2BrSZLpoDQRvX2KogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7o5D1wv2CPStCSVAq3APyqRZr15YMWLUZ1vl08syva5%2Fa3tZjc4bf5SHqDmBwGG4T84zhlqzbAwf6bdZP2xRnhPC2ZIvQ4YwK8cUTQd9fvJK7WKwInHC7%2FaZTFzPFI5XrbO%2FxqXc4gLkSPuurIN9MHCJsXy46du79AJCld5jpE%2BaCeLISGQvLDmGoX%2Fx2TiKX%2B2jTowKTz7kFUp9FLw5FlPZqLR7ZM%2BhSYqNUqVe0gwAwqwVyA5zqe%2BhTqtSucI906Ih017UwtDIhixzO8MBZKhc0joRpTQqGnSHeXBTFY6LhapSlP0qSUijQquasI5dD9BkQqlWKCFsr0uiocRp8fNDc1WvlWU%2BqVCruft1%2BuP9T2dQfiFnxTZ0tI8xItIOukrOp8UZHt5RP3Fax3Dd3vdg5Ku1A1v9WhcbLKpXzHbWz4CxNn8qSKS19JkDzToizNAvaBE1Vz8Yfx7JmOw1pu1mu4zmqHxMgEpnFvzMKXUshYqJFmex2bgqXwd9gfSGqXrlsSi1mvTRPhr82L4Xud0v9hzejkMGr6Hovglwi%2FOjYp30AYUjZmS%2F1kXt92DQBCzW7XnsjdxiPHWDtXq1Bfs7QJrCqsiztF3%2FHKtnHGf9cmELYWFvOtehRxeIPvHvxuhFd7Yg0kj5dWDCR1%2B68BjqkAff2pVZukPAxr%2FsyAJSwSsof5zpl3fxGYPIf09EhbXpyJDC476mZ%2BJ01tgP9hXUz42hKZelEnAfciEjVsn20i19TztgUdafU%2BGW%2BSlgAP8P2zlzfMSGLI5wNnDjJFslyk9Z%2BuCaLT2Q7IOhLQrLq8sDyYziQMq9G%2BS6lHSD2d9dJKC1BnPbP0xHG%2BuWYxxfa%2FqrQhOsnTyCtnk1yyGx5H8b69pDE&X-Amz-Signature=2776b393f49def8df364d6d35dc58497a8c5ccaaa2ecd89c322ab5ef213811a3&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6TJ3HQ3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDGONiITOJ9o3f1D9ohJdFgA3C9Mf0bsSk93mN1V0BFZAiEA4hr03p2GS%2FpslqX16oLl0sg6bPP0dYl9XOVIzIvA%2BSgqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOvCoMYYQu5gYtdSQSrcA1jwhOkhLM4ZLW4uCwSZOvf5R8%2F8bmY8I8edYTuEqB3lU%2F321Up6tal7CKRgJDEt%2B%2F99V%2FGzKBPbXtAR2oAjPKU%2FB78b856xhsoXX0GjXRcHLlS3RxhDIMK61vVz3mkpYXwZWHsFEV33%2FShOBdzXvou6ejssLjO94cmZ5RZV3jmKN5%2BkNcXPf%2FHVdIUe5f46ESZR1K8Hf85wAjE9UBeh14T3oNyLkwsdN%2FSZyMCtes6rt5RXU8Q6%2F8Js3DMRbrOHSiOd%2FoO13UNZHLdQaDOF5OIa0FgnWJMO%2F%2Fa4yrj12em4MgP6NL2iKeS4w68YkTOd%2F8wVf5JLa2ZRnosScaTH7pk1N5nEmfxNs9Xa%2FKycyMPpvY2kUono0p%2BOfdIxJn%2FOTDlam%2BDGAnU4bKzi75DhojsFx370OqdQ6fWWOOdm%2BpCK2f5uOWL57owCXjX9kSo8RU%2BfqSogl%2FXvjEV%2BFCRVjG1%2FUkLULx8gG2blQlJ1m%2B0u88meXzeQy%2FDyM0gOcWFFr7PdqLMxFV2frLIHZkdpqNcHJS6AQ33L5%2FZhzr2CNaoWKWo%2FWv15Y6tZSeyoGaDHKTkB9oyGNQBuuq2ZpVFRvcx14l5Ti%2FeHk%2Fk1LcBVYJ0qbMwTC2SZ0i2keVZSMP7W7rwGOqUBKsSQi4F7kn%2FXoxmhSzq6u8MolVCkNjk7ACeyAwtAJI4aQLdZNWk665EBiZtDbaCO%2F7%2FH3Q6z7r8ipFFxiEBdf0Hmllc8ZmiZXsvx7SbgBySi2d9QxI6FLDc%2B7CRFJ%2FSMIk34l%2FXqi4TSQybP4Gy3BxOH4Utv2b7m5Di9hH6C%2BOEAdn9rgmVi08gcStIyLfEX9yqerPQISNKOtgZUb6LiwLHRy3Fn&X-Amz-Signature=19b7f4d11ee4e86441666f531c1cb2215e8274c661a21e1029a0a583093d24a6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6TJ3HQ3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDGONiITOJ9o3f1D9ohJdFgA3C9Mf0bsSk93mN1V0BFZAiEA4hr03p2GS%2FpslqX16oLl0sg6bPP0dYl9XOVIzIvA%2BSgqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOvCoMYYQu5gYtdSQSrcA1jwhOkhLM4ZLW4uCwSZOvf5R8%2F8bmY8I8edYTuEqB3lU%2F321Up6tal7CKRgJDEt%2B%2F99V%2FGzKBPbXtAR2oAjPKU%2FB78b856xhsoXX0GjXRcHLlS3RxhDIMK61vVz3mkpYXwZWHsFEV33%2FShOBdzXvou6ejssLjO94cmZ5RZV3jmKN5%2BkNcXPf%2FHVdIUe5f46ESZR1K8Hf85wAjE9UBeh14T3oNyLkwsdN%2FSZyMCtes6rt5RXU8Q6%2F8Js3DMRbrOHSiOd%2FoO13UNZHLdQaDOF5OIa0FgnWJMO%2F%2Fa4yrj12em4MgP6NL2iKeS4w68YkTOd%2F8wVf5JLa2ZRnosScaTH7pk1N5nEmfxNs9Xa%2FKycyMPpvY2kUono0p%2BOfdIxJn%2FOTDlam%2BDGAnU4bKzi75DhojsFx370OqdQ6fWWOOdm%2BpCK2f5uOWL57owCXjX9kSo8RU%2BfqSogl%2FXvjEV%2BFCRVjG1%2FUkLULx8gG2blQlJ1m%2B0u88meXzeQy%2FDyM0gOcWFFr7PdqLMxFV2frLIHZkdpqNcHJS6AQ33L5%2FZhzr2CNaoWKWo%2FWv15Y6tZSeyoGaDHKTkB9oyGNQBuuq2ZpVFRvcx14l5Ti%2FeHk%2Fk1LcBVYJ0qbMwTC2SZ0i2keVZSMP7W7rwGOqUBKsSQi4F7kn%2FXoxmhSzq6u8MolVCkNjk7ACeyAwtAJI4aQLdZNWk665EBiZtDbaCO%2F7%2FH3Q6z7r8ipFFxiEBdf0Hmllc8ZmiZXsvx7SbgBySi2d9QxI6FLDc%2B7CRFJ%2FSMIk34l%2FXqi4TSQybP4Gy3BxOH4Utv2b7m5Di9hH6C%2BOEAdn9rgmVi08gcStIyLfEX9yqerPQISNKOtgZUb6LiwLHRy3Fn&X-Amz-Signature=ffc3fc3652a382c99c5de856f836ab6525b8f0778afc22438df170fcbcc56e97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVZEFUTQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFJbSvWN3p7bW9TzS%2FGBu4rna%2B1nmzzMXEcShyDkUThwIhAIp7MFo5lkMqMQBgunYp00NuXEMcv5o%2BrSZLpoDQRvX2KogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7o5D1wv2CPStCSVAq3APyqRZr15YMWLUZ1vl08syva5%2Fa3tZjc4bf5SHqDmBwGG4T84zhlqzbAwf6bdZP2xRnhPC2ZIvQ4YwK8cUTQd9fvJK7WKwInHC7%2FaZTFzPFI5XrbO%2FxqXc4gLkSPuurIN9MHCJsXy46du79AJCld5jpE%2BaCeLISGQvLDmGoX%2Fx2TiKX%2B2jTowKTz7kFUp9FLw5FlPZqLR7ZM%2BhSYqNUqVe0gwAwqwVyA5zqe%2BhTqtSucI906Ih017UwtDIhixzO8MBZKhc0joRpTQqGnSHeXBTFY6LhapSlP0qSUijQquasI5dD9BkQqlWKCFsr0uiocRp8fNDc1WvlWU%2BqVCruft1%2BuP9T2dQfiFnxTZ0tI8xItIOukrOp8UZHt5RP3Fax3Dd3vdg5Ku1A1v9WhcbLKpXzHbWz4CxNn8qSKS19JkDzToizNAvaBE1Vz8Yfx7JmOw1pu1mu4zmqHxMgEpnFvzMKXUshYqJFmex2bgqXwd9gfSGqXrlsSi1mvTRPhr82L4Xud0v9hzejkMGr6Hovglwi%2FOjYp30AYUjZmS%2F1kXt92DQBCzW7XnsjdxiPHWDtXq1Bfs7QJrCqsiztF3%2FHKtnHGf9cmELYWFvOtehRxeIPvHvxuhFd7Yg0kj5dWDCR1%2B68BjqkAff2pVZukPAxr%2FsyAJSwSsof5zpl3fxGYPIf09EhbXpyJDC476mZ%2BJ01tgP9hXUz42hKZelEnAfciEjVsn20i19TztgUdafU%2BGW%2BSlgAP8P2zlzfMSGLI5wNnDjJFslyk9Z%2BuCaLT2Q7IOhLQrLq8sDyYziQMq9G%2BS6lHSD2d9dJKC1BnPbP0xHG%2BuWYxxfa%2FqrQhOsnTyCtnk1yyGx5H8b69pDE&X-Amz-Signature=8cbfc81ec44d03879301dc13cf6efa5199f181f2606c2adf3a273f13f7ab6483&X-Amz-SignedHeaders=host&x-id=GetObject)
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