

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWBU7W4H%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGD3A%2F%2B9Mz8vN67IvNXK6cAYWzbu8gWUiWz3Smx0HMojAiBczXj8JjjMCmKVgXOBzvkwJJxBpJw0rYZrT9grACFFPSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzToE6rvL4VkDEcjPKtwDRFHkMg9k1rkGCHdP7Rrw58KwrK39XTQlolsrpmaYmwlOdpE9bB65GGZFRMh5GOf71p45ek26sMSUNXikQ5FixeeBdphBIFkZMgn%2FFMh8BQ3ysV0qa4VAZNAmBDlm2AlqPtSKu4RoA21L70q1d%2F57gOvgXOLAqL2NX92az3LQEdEeWV3jqWYBCXIIaZ44BSq3%2BbricUj1qsVhowGZUI%2B7XKDpuzrkE2xyPSOl16W0dh2iwJpDyx017zsXDVRx3B5LDRG7XnJdc27%2FIpyB0pcg0SZpG3o45%2F2sSbVm0GOo%2B%2BIMZt%2FRXEFUsWKgrBSPCD1MVnTIBtVAWo2T9DfGO2PiMvZc5GUPDnPtE%2BhMazNUdJ67rvM8hvEbpiOioEHer3czIdOzn7a%2FFpGd0T%2FLgTEhlwyDS5OmUybH1V%2BygXUvr3dLorZKZf%2BqVY7hyKx%2BxqEZe20pLbidHC3FEWIqmQ5v9kA%2BvX6ILkNmuxLpqTg3pn9z6twaxYBxhuO2Iod1XG1CyswEJXIpkdSqUjHvsZuCqOterboKrQu0z8q6k7Vf432Ne2J0l6ogaTHCaVJ%2FLo0ScH85k5igSnY2FnxoZgsG%2F7457idKTOt0CwhqaAx9GSVSYyu4AA5cMuEv6fIw35WbvQY6pgHlYdsATkVMXJxda7GU4puGJ3%2BTy2%2BP7jm0piuHfrzQ7i2Zqr41QNWBXx%2BDYWfvRctPFsZ4ZsNBNtc%2Bq2%2BFFja9oDW7wh0VZmkAd1Oa84wIoC7xsRSkzPd0iegsk46C6S21Jo87HBR1fspTWh%2BpMM7arYQmymuMjEp6eVqSUA08hLtE7C0PEIcCoP2ZrC4H2g2ifKwXrQ2VDcav1hPEaUxDk1XGsjBa&X-Amz-Signature=3408cb74736617c7f965b15bb117738abb6ea4580c1ec25aca71e5e668c6cc5a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWBU7W4H%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGD3A%2F%2B9Mz8vN67IvNXK6cAYWzbu8gWUiWz3Smx0HMojAiBczXj8JjjMCmKVgXOBzvkwJJxBpJw0rYZrT9grACFFPSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzToE6rvL4VkDEcjPKtwDRFHkMg9k1rkGCHdP7Rrw58KwrK39XTQlolsrpmaYmwlOdpE9bB65GGZFRMh5GOf71p45ek26sMSUNXikQ5FixeeBdphBIFkZMgn%2FFMh8BQ3ysV0qa4VAZNAmBDlm2AlqPtSKu4RoA21L70q1d%2F57gOvgXOLAqL2NX92az3LQEdEeWV3jqWYBCXIIaZ44BSq3%2BbricUj1qsVhowGZUI%2B7XKDpuzrkE2xyPSOl16W0dh2iwJpDyx017zsXDVRx3B5LDRG7XnJdc27%2FIpyB0pcg0SZpG3o45%2F2sSbVm0GOo%2B%2BIMZt%2FRXEFUsWKgrBSPCD1MVnTIBtVAWo2T9DfGO2PiMvZc5GUPDnPtE%2BhMazNUdJ67rvM8hvEbpiOioEHer3czIdOzn7a%2FFpGd0T%2FLgTEhlwyDS5OmUybH1V%2BygXUvr3dLorZKZf%2BqVY7hyKx%2BxqEZe20pLbidHC3FEWIqmQ5v9kA%2BvX6ILkNmuxLpqTg3pn9z6twaxYBxhuO2Iod1XG1CyswEJXIpkdSqUjHvsZuCqOterboKrQu0z8q6k7Vf432Ne2J0l6ogaTHCaVJ%2FLo0ScH85k5igSnY2FnxoZgsG%2F7457idKTOt0CwhqaAx9GSVSYyu4AA5cMuEv6fIw35WbvQY6pgHlYdsATkVMXJxda7GU4puGJ3%2BTy2%2BP7jm0piuHfrzQ7i2Zqr41QNWBXx%2BDYWfvRctPFsZ4ZsNBNtc%2Bq2%2BFFja9oDW7wh0VZmkAd1Oa84wIoC7xsRSkzPd0iegsk46C6S21Jo87HBR1fspTWh%2BpMM7arYQmymuMjEp6eVqSUA08hLtE7C0PEIcCoP2ZrC4H2g2ifKwXrQ2VDcav1hPEaUxDk1XGsjBa&X-Amz-Signature=6697effe41c2b29fc28ba01fd9eba72c4b7092918a2f8a5fe943a15b408c6886&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWBU7W4H%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGD3A%2F%2B9Mz8vN67IvNXK6cAYWzbu8gWUiWz3Smx0HMojAiBczXj8JjjMCmKVgXOBzvkwJJxBpJw0rYZrT9grACFFPSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzToE6rvL4VkDEcjPKtwDRFHkMg9k1rkGCHdP7Rrw58KwrK39XTQlolsrpmaYmwlOdpE9bB65GGZFRMh5GOf71p45ek26sMSUNXikQ5FixeeBdphBIFkZMgn%2FFMh8BQ3ysV0qa4VAZNAmBDlm2AlqPtSKu4RoA21L70q1d%2F57gOvgXOLAqL2NX92az3LQEdEeWV3jqWYBCXIIaZ44BSq3%2BbricUj1qsVhowGZUI%2B7XKDpuzrkE2xyPSOl16W0dh2iwJpDyx017zsXDVRx3B5LDRG7XnJdc27%2FIpyB0pcg0SZpG3o45%2F2sSbVm0GOo%2B%2BIMZt%2FRXEFUsWKgrBSPCD1MVnTIBtVAWo2T9DfGO2PiMvZc5GUPDnPtE%2BhMazNUdJ67rvM8hvEbpiOioEHer3czIdOzn7a%2FFpGd0T%2FLgTEhlwyDS5OmUybH1V%2BygXUvr3dLorZKZf%2BqVY7hyKx%2BxqEZe20pLbidHC3FEWIqmQ5v9kA%2BvX6ILkNmuxLpqTg3pn9z6twaxYBxhuO2Iod1XG1CyswEJXIpkdSqUjHvsZuCqOterboKrQu0z8q6k7Vf432Ne2J0l6ogaTHCaVJ%2FLo0ScH85k5igSnY2FnxoZgsG%2F7457idKTOt0CwhqaAx9GSVSYyu4AA5cMuEv6fIw35WbvQY6pgHlYdsATkVMXJxda7GU4puGJ3%2BTy2%2BP7jm0piuHfrzQ7i2Zqr41QNWBXx%2BDYWfvRctPFsZ4ZsNBNtc%2Bq2%2BFFja9oDW7wh0VZmkAd1Oa84wIoC7xsRSkzPd0iegsk46C6S21Jo87HBR1fspTWh%2BpMM7arYQmymuMjEp6eVqSUA08hLtE7C0PEIcCoP2ZrC4H2g2ifKwXrQ2VDcav1hPEaUxDk1XGsjBa&X-Amz-Signature=5bcc69e306dc2b8aa0b168cfd87f0ab684054a3ee88e59329bd569ce4a3c0a2a&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWHFIWXH%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCs5m9GQgJE3z7oq9sPHduNLtXD88eyS1zuLr4Thss91AIgPgRC26WqIiy4vS0xDMZj9HHBgm0AsysBphyMGraPyy4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC8uRYf75Lr3PM7poyrcA23REFBrFsLymgGI44xMVrfMWSSExwN6qQAaW6Bjk3twDi3wiZJ5leblTP1cNPohn1%2BsDkrdNE4u1Nha7qTE5hl6RKl8aiYUSNUMtRC8CCwylsUu7e31vGkc%2F3MasSyB4n25TV514Kt3DV7Lldy9caly9itGN44NERlD3G0b0EQIEueLXdPPOeoqRhyLA6YPY%2Bvj72d5sKAC%2FQGHrhsJOT80mzXcleipuL60T1cq0DRyXzGM7NwXuUD8csk%2Bfky%2FR7CxTQO3WHbfv1zb%2FOeAjGFGdFmUJ%2BeHcDM1LRZ0H3GGChCEJ4BC8lKjBt4WEfJeydcwgJ0pBBbZZKIARYI7b0bthMiw9j4h0em3%2BrzY0pzdt2STfcdwHhvwMijp%2BkZUlmdvSnyeCw8cgtAseBSuIatYRtfvi7D8O9L4h%2FIfOmgGgFMjyYjIB6oOGHe7vsms%2F4BUpbL3rcJoIAAlcM6vIqDZ%2BgzTZVIBg6B%2Fj6zNoxTBn29LrIs439XpzcTAHUM5cgrHjvqEm9n%2BAioC5wZvV0x4BacIugm7GqUCw%2FrsoweS%2B6PD%2B3ubavt5OUjOHVvPoMMBaB%2F9GMLEijV15ry3EYEG4BEux9XKb%2FxVhjDKqB5o7bTFS74wB7eeIsDyMOSVm70GOqUBaRl1xKSU%2FFbXvufHHd19Ho5t2cyav26SN7ee8sPMqtC7Kid62jJY6pyhJaMhhY2hGnpIqShss6vyvgInA%2FJrDTxx9nutMQYi1FnqVLH9Kwokn%2FzMGp%2F6vRaphik64DOfr5fHV%2BP99nj1IpMjhY6Me52u%2Bf%2BzGDKJvPVbqy%2F3KUAjHxJTjnDt9C2Zrws8AWLIoEV5q9ysXBCb3oOM9JtYQ9FnXJTZ&X-Amz-Signature=dc3bd8198a9252e36bcf960e5dd8b97b05feb90cbc020e843386fe7db1823ccb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWHFIWXH%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCs5m9GQgJE3z7oq9sPHduNLtXD88eyS1zuLr4Thss91AIgPgRC26WqIiy4vS0xDMZj9HHBgm0AsysBphyMGraPyy4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC8uRYf75Lr3PM7poyrcA23REFBrFsLymgGI44xMVrfMWSSExwN6qQAaW6Bjk3twDi3wiZJ5leblTP1cNPohn1%2BsDkrdNE4u1Nha7qTE5hl6RKl8aiYUSNUMtRC8CCwylsUu7e31vGkc%2F3MasSyB4n25TV514Kt3DV7Lldy9caly9itGN44NERlD3G0b0EQIEueLXdPPOeoqRhyLA6YPY%2Bvj72d5sKAC%2FQGHrhsJOT80mzXcleipuL60T1cq0DRyXzGM7NwXuUD8csk%2Bfky%2FR7CxTQO3WHbfv1zb%2FOeAjGFGdFmUJ%2BeHcDM1LRZ0H3GGChCEJ4BC8lKjBt4WEfJeydcwgJ0pBBbZZKIARYI7b0bthMiw9j4h0em3%2BrzY0pzdt2STfcdwHhvwMijp%2BkZUlmdvSnyeCw8cgtAseBSuIatYRtfvi7D8O9L4h%2FIfOmgGgFMjyYjIB6oOGHe7vsms%2F4BUpbL3rcJoIAAlcM6vIqDZ%2BgzTZVIBg6B%2Fj6zNoxTBn29LrIs439XpzcTAHUM5cgrHjvqEm9n%2BAioC5wZvV0x4BacIugm7GqUCw%2FrsoweS%2B6PD%2B3ubavt5OUjOHVvPoMMBaB%2F9GMLEijV15ry3EYEG4BEux9XKb%2FxVhjDKqB5o7bTFS74wB7eeIsDyMOSVm70GOqUBaRl1xKSU%2FFbXvufHHd19Ho5t2cyav26SN7ee8sPMqtC7Kid62jJY6pyhJaMhhY2hGnpIqShss6vyvgInA%2FJrDTxx9nutMQYi1FnqVLH9Kwokn%2FzMGp%2F6vRaphik64DOfr5fHV%2BP99nj1IpMjhY6Me52u%2Bf%2BzGDKJvPVbqy%2F3KUAjHxJTjnDt9C2Zrws8AWLIoEV5q9ysXBCb3oOM9JtYQ9FnXJTZ&X-Amz-Signature=f5255c4cda22f224eed467a35c756a89bc123501c99be9fc3186b37b8d687c94&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWBU7W4H%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGD3A%2F%2B9Mz8vN67IvNXK6cAYWzbu8gWUiWz3Smx0HMojAiBczXj8JjjMCmKVgXOBzvkwJJxBpJw0rYZrT9grACFFPSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzToE6rvL4VkDEcjPKtwDRFHkMg9k1rkGCHdP7Rrw58KwrK39XTQlolsrpmaYmwlOdpE9bB65GGZFRMh5GOf71p45ek26sMSUNXikQ5FixeeBdphBIFkZMgn%2FFMh8BQ3ysV0qa4VAZNAmBDlm2AlqPtSKu4RoA21L70q1d%2F57gOvgXOLAqL2NX92az3LQEdEeWV3jqWYBCXIIaZ44BSq3%2BbricUj1qsVhowGZUI%2B7XKDpuzrkE2xyPSOl16W0dh2iwJpDyx017zsXDVRx3B5LDRG7XnJdc27%2FIpyB0pcg0SZpG3o45%2F2sSbVm0GOo%2B%2BIMZt%2FRXEFUsWKgrBSPCD1MVnTIBtVAWo2T9DfGO2PiMvZc5GUPDnPtE%2BhMazNUdJ67rvM8hvEbpiOioEHer3czIdOzn7a%2FFpGd0T%2FLgTEhlwyDS5OmUybH1V%2BygXUvr3dLorZKZf%2BqVY7hyKx%2BxqEZe20pLbidHC3FEWIqmQ5v9kA%2BvX6ILkNmuxLpqTg3pn9z6twaxYBxhuO2Iod1XG1CyswEJXIpkdSqUjHvsZuCqOterboKrQu0z8q6k7Vf432Ne2J0l6ogaTHCaVJ%2FLo0ScH85k5igSnY2FnxoZgsG%2F7457idKTOt0CwhqaAx9GSVSYyu4AA5cMuEv6fIw35WbvQY6pgHlYdsATkVMXJxda7GU4puGJ3%2BTy2%2BP7jm0piuHfrzQ7i2Zqr41QNWBXx%2BDYWfvRctPFsZ4ZsNBNtc%2Bq2%2BFFja9oDW7wh0VZmkAd1Oa84wIoC7xsRSkzPd0iegsk46C6S21Jo87HBR1fspTWh%2BpMM7arYQmymuMjEp6eVqSUA08hLtE7C0PEIcCoP2ZrC4H2g2ifKwXrQ2VDcav1hPEaUxDk1XGsjBa&X-Amz-Signature=755e2d7fee247e56e7ecb89c16838e468ea6754f16f3cc8b2697d4516c0392f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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