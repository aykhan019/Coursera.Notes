

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZIU6SQY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIDvDvfVnfZQcThDy6VlzucoIMmKz%2BbhvGD4r5FKnnDICAiBfwvjQ%2B1NX9fzTAOOIeFKi0U5JtiX410I%2Fu9BIE95S%2Bir%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMuRnAICflztYPQ3sYKtwDXIWgiu0kJFHAVR3aYKdiTNtakdqe4OOfsFtN9fdlfhFxfxpLEeK%2FW4qmbe8KLEi0hJ7%2FWMpYE%2BjrWHN26Id8x%2BbQu0CwnPURMtLYTB9vGugGwMMpAqCnFzqOr0%2F%2FnXxaQB%2BrZ0ZQi0iwd7Y8vZbBvmDJwk6767IgC8KDgxyomQmD298h2HA9UkNAYk8vsWUoJQk3M4%2B41i0Oh5bvO%2BAYXO3N0pBftHCdl6%2F3e9vEXxkOwr7oAgZAxRmfniGr5VI%2BAeaF4U5vHFU0ZhQbQp1aFP2tqPUiQpKDaXVsf0c9EpXSCqhTfsoItCb%2B07M5RtJpnEMq4e29Nnoex%2BbOmb49cbqOe0wazWpJ68%2FUh87zOMt4iBVN71h6Ll83KG%2BjYeDhR1%2BJh9Dy5CnhIILIp0xIvkA3MEMFbCSV03TA%2FYZeEfNC%2FA16apst%2BHnK3pzYcEAImeVA%2Fg%2FxuhMuP%2FUBJjWh0QGHYstObU4W822THN7uJ0xCFQy8hWRMQsFf5c22mepXHq%2FsY5GgRPIZzg1Gemp6ol%2FAGo5bCD6x2vDM43AmeSRNAdmSrxD9sWgp0co%2F1Vbvb%2BpKS841sKJWgv3zAIUcdFk35abShRLypUBybp7E1yms5aiEvA5w1ciA8sUw0OCYvQY6pgFjHkeurj1CZ3ZLwSN%2BfD5y%2Fdbfg90DeqHB0YktXpfQWld2dTtZHQm2X9GVG3bqwBzPvxb2Z6jU%2BG5yvXlskZlusN0aeJ4TU%2Br6j%2BB6I3t1ezsttpz%2FxZWkp2znVAm7GcCQYKbldDcPh%2FAG%2BozLEHdzYJooYUkw4GPnbdX%2FvDBPMmRFncj6KR7YJkWejUz6o2YBu%2BQoLtKxbm5yWMFUQ4r1a1e3TI4h&X-Amz-Signature=8e1f6dd4529c18adfec129bf67eee68c719420dc3e135db7263631983f978cca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZIU6SQY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIDvDvfVnfZQcThDy6VlzucoIMmKz%2BbhvGD4r5FKnnDICAiBfwvjQ%2B1NX9fzTAOOIeFKi0U5JtiX410I%2Fu9BIE95S%2Bir%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMuRnAICflztYPQ3sYKtwDXIWgiu0kJFHAVR3aYKdiTNtakdqe4OOfsFtN9fdlfhFxfxpLEeK%2FW4qmbe8KLEi0hJ7%2FWMpYE%2BjrWHN26Id8x%2BbQu0CwnPURMtLYTB9vGugGwMMpAqCnFzqOr0%2F%2FnXxaQB%2BrZ0ZQi0iwd7Y8vZbBvmDJwk6767IgC8KDgxyomQmD298h2HA9UkNAYk8vsWUoJQk3M4%2B41i0Oh5bvO%2BAYXO3N0pBftHCdl6%2F3e9vEXxkOwr7oAgZAxRmfniGr5VI%2BAeaF4U5vHFU0ZhQbQp1aFP2tqPUiQpKDaXVsf0c9EpXSCqhTfsoItCb%2B07M5RtJpnEMq4e29Nnoex%2BbOmb49cbqOe0wazWpJ68%2FUh87zOMt4iBVN71h6Ll83KG%2BjYeDhR1%2BJh9Dy5CnhIILIp0xIvkA3MEMFbCSV03TA%2FYZeEfNC%2FA16apst%2BHnK3pzYcEAImeVA%2Fg%2FxuhMuP%2FUBJjWh0QGHYstObU4W822THN7uJ0xCFQy8hWRMQsFf5c22mepXHq%2FsY5GgRPIZzg1Gemp6ol%2FAGo5bCD6x2vDM43AmeSRNAdmSrxD9sWgp0co%2F1Vbvb%2BpKS841sKJWgv3zAIUcdFk35abShRLypUBybp7E1yms5aiEvA5w1ciA8sUw0OCYvQY6pgFjHkeurj1CZ3ZLwSN%2BfD5y%2Fdbfg90DeqHB0YktXpfQWld2dTtZHQm2X9GVG3bqwBzPvxb2Z6jU%2BG5yvXlskZlusN0aeJ4TU%2Br6j%2BB6I3t1ezsttpz%2FxZWkp2znVAm7GcCQYKbldDcPh%2FAG%2BozLEHdzYJooYUkw4GPnbdX%2FvDBPMmRFncj6KR7YJkWejUz6o2YBu%2BQoLtKxbm5yWMFUQ4r1a1e3TI4h&X-Amz-Signature=276ef2cc9ec97b0ee86c987d426d8665171eb48efb57bf4c761a77710445caa3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZIU6SQY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIDvDvfVnfZQcThDy6VlzucoIMmKz%2BbhvGD4r5FKnnDICAiBfwvjQ%2B1NX9fzTAOOIeFKi0U5JtiX410I%2Fu9BIE95S%2Bir%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMuRnAICflztYPQ3sYKtwDXIWgiu0kJFHAVR3aYKdiTNtakdqe4OOfsFtN9fdlfhFxfxpLEeK%2FW4qmbe8KLEi0hJ7%2FWMpYE%2BjrWHN26Id8x%2BbQu0CwnPURMtLYTB9vGugGwMMpAqCnFzqOr0%2F%2FnXxaQB%2BrZ0ZQi0iwd7Y8vZbBvmDJwk6767IgC8KDgxyomQmD298h2HA9UkNAYk8vsWUoJQk3M4%2B41i0Oh5bvO%2BAYXO3N0pBftHCdl6%2F3e9vEXxkOwr7oAgZAxRmfniGr5VI%2BAeaF4U5vHFU0ZhQbQp1aFP2tqPUiQpKDaXVsf0c9EpXSCqhTfsoItCb%2B07M5RtJpnEMq4e29Nnoex%2BbOmb49cbqOe0wazWpJ68%2FUh87zOMt4iBVN71h6Ll83KG%2BjYeDhR1%2BJh9Dy5CnhIILIp0xIvkA3MEMFbCSV03TA%2FYZeEfNC%2FA16apst%2BHnK3pzYcEAImeVA%2Fg%2FxuhMuP%2FUBJjWh0QGHYstObU4W822THN7uJ0xCFQy8hWRMQsFf5c22mepXHq%2FsY5GgRPIZzg1Gemp6ol%2FAGo5bCD6x2vDM43AmeSRNAdmSrxD9sWgp0co%2F1Vbvb%2BpKS841sKJWgv3zAIUcdFk35abShRLypUBybp7E1yms5aiEvA5w1ciA8sUw0OCYvQY6pgFjHkeurj1CZ3ZLwSN%2BfD5y%2Fdbfg90DeqHB0YktXpfQWld2dTtZHQm2X9GVG3bqwBzPvxb2Z6jU%2BG5yvXlskZlusN0aeJ4TU%2Br6j%2BB6I3t1ezsttpz%2FxZWkp2znVAm7GcCQYKbldDcPh%2FAG%2BozLEHdzYJooYUkw4GPnbdX%2FvDBPMmRFncj6KR7YJkWejUz6o2YBu%2BQoLtKxbm5yWMFUQ4r1a1e3TI4h&X-Amz-Signature=838862eeaee171474e5066569e11fa04f4ad610516b13a746cb031f7eb67a3f5&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VO2VDSW3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCa5BguQ1Kbin%2F95lN8Pahe1RGz7qfmR9a541Jl06wJvQIgLi9pXh4j%2BcFkgI3LNUlab6DR2OMgNqvVa1gbXQUM4hAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDBUhrbdvQg9k9Iy1WCrcA%2BhgrpU%2Fc9PVAYS1EtWSJBAy4GOMuZ0BArmqU4yzxjduRL4uAzbLNjZHE7rraTEjluSbW3ZfbigEcshlkF6HZcfb8RF%2B%2BoO7RB9wMuKvucL5miygdyF9sN6QZDEJA0dc0E3V1w5V9nWmrel6h9Q%2BGHOW7fXS7dGN4ja3dH1bI5tyG4f5JNRJ00cTQtmH8okOMIFF4bcNJfRosTl2GJ4uBiqHsEgnnG0AXAnRAGmatrQayIGdaGi5H1%2BO54gHrlypQH1yJeQF7nqoCww3pgoT0jejJYLHwkfsd%2BkoCUtDywsyhUgthsFGD1EqB2z3kz2%2FWGsylqKth7UY8Wg3di0oXCvNJaAVRLVs74z5vQtUxeK4bZE%2F1yItoqiCgd%2F1RypcM38kVQCRhmUmmLQlYSb3PhPX4q7G7BE3tlP2SzNKGEmx5Z%2BqCmJANz23tuKm1pVqc0k1%2FFW1u%2BOIcuhKl1Rsv9T1xX0cLq3JasCiKsAzDCXfgFTrdpgNMrsHM741%2BF2BUuRBfAaanlZv0kAKylhmK0jXez%2Fd%2FWNU0d4aC99u5tm6%2FvVhNeqtdDc9PYhz8B70839tzhisslVE2KDTtQL9TCMlXtuhaKjw0OmoVi6mJLDMGaKRsrRwVlrOHlYHMPPfmL0GOqUBiuRAiqsdeLx6m64MGQ09N68qFgDR3ziM%2BUkoX930d3IookCvQ2Rqvp7ZQG4D%2FsgidbFr9hf16t38wiov5w7HgxW3NyinKsSPZmEqeW%2FmV5W5fpQseRcDojcdAM7E70FbQc9KZFzO8YVfbFG5OGdsEQdAimg0Mp%2BdgVxuKyGFq2pMQVNmxdX89N87%2Fo9CHcuOOqKKzog7YO5rNMD9RdydDyU3HLAm&X-Amz-Signature=2e65c4d067093f1432adfa3d1957cd4c827afa53de39ab020bcbb2a5b26b3aed&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VO2VDSW3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQCa5BguQ1Kbin%2F95lN8Pahe1RGz7qfmR9a541Jl06wJvQIgLi9pXh4j%2BcFkgI3LNUlab6DR2OMgNqvVa1gbXQUM4hAq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDBUhrbdvQg9k9Iy1WCrcA%2BhgrpU%2Fc9PVAYS1EtWSJBAy4GOMuZ0BArmqU4yzxjduRL4uAzbLNjZHE7rraTEjluSbW3ZfbigEcshlkF6HZcfb8RF%2B%2BoO7RB9wMuKvucL5miygdyF9sN6QZDEJA0dc0E3V1w5V9nWmrel6h9Q%2BGHOW7fXS7dGN4ja3dH1bI5tyG4f5JNRJ00cTQtmH8okOMIFF4bcNJfRosTl2GJ4uBiqHsEgnnG0AXAnRAGmatrQayIGdaGi5H1%2BO54gHrlypQH1yJeQF7nqoCww3pgoT0jejJYLHwkfsd%2BkoCUtDywsyhUgthsFGD1EqB2z3kz2%2FWGsylqKth7UY8Wg3di0oXCvNJaAVRLVs74z5vQtUxeK4bZE%2F1yItoqiCgd%2F1RypcM38kVQCRhmUmmLQlYSb3PhPX4q7G7BE3tlP2SzNKGEmx5Z%2BqCmJANz23tuKm1pVqc0k1%2FFW1u%2BOIcuhKl1Rsv9T1xX0cLq3JasCiKsAzDCXfgFTrdpgNMrsHM741%2BF2BUuRBfAaanlZv0kAKylhmK0jXez%2Fd%2FWNU0d4aC99u5tm6%2FvVhNeqtdDc9PYhz8B70839tzhisslVE2KDTtQL9TCMlXtuhaKjw0OmoVi6mJLDMGaKRsrRwVlrOHlYHMPPfmL0GOqUBiuRAiqsdeLx6m64MGQ09N68qFgDR3ziM%2BUkoX930d3IookCvQ2Rqvp7ZQG4D%2FsgidbFr9hf16t38wiov5w7HgxW3NyinKsSPZmEqeW%2FmV5W5fpQseRcDojcdAM7E70FbQc9KZFzO8YVfbFG5OGdsEQdAimg0Mp%2BdgVxuKyGFq2pMQVNmxdX89N87%2Fo9CHcuOOqKKzog7YO5rNMD9RdydDyU3HLAm&X-Amz-Signature=f701507d549d4cc6239e8bfd8046fb48a3adf0946bd4658ff288d60e923963bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZIU6SQY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIDvDvfVnfZQcThDy6VlzucoIMmKz%2BbhvGD4r5FKnnDICAiBfwvjQ%2B1NX9fzTAOOIeFKi0U5JtiX410I%2Fu9BIE95S%2Bir%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMuRnAICflztYPQ3sYKtwDXIWgiu0kJFHAVR3aYKdiTNtakdqe4OOfsFtN9fdlfhFxfxpLEeK%2FW4qmbe8KLEi0hJ7%2FWMpYE%2BjrWHN26Id8x%2BbQu0CwnPURMtLYTB9vGugGwMMpAqCnFzqOr0%2F%2FnXxaQB%2BrZ0ZQi0iwd7Y8vZbBvmDJwk6767IgC8KDgxyomQmD298h2HA9UkNAYk8vsWUoJQk3M4%2B41i0Oh5bvO%2BAYXO3N0pBftHCdl6%2F3e9vEXxkOwr7oAgZAxRmfniGr5VI%2BAeaF4U5vHFU0ZhQbQp1aFP2tqPUiQpKDaXVsf0c9EpXSCqhTfsoItCb%2B07M5RtJpnEMq4e29Nnoex%2BbOmb49cbqOe0wazWpJ68%2FUh87zOMt4iBVN71h6Ll83KG%2BjYeDhR1%2BJh9Dy5CnhIILIp0xIvkA3MEMFbCSV03TA%2FYZeEfNC%2FA16apst%2BHnK3pzYcEAImeVA%2Fg%2FxuhMuP%2FUBJjWh0QGHYstObU4W822THN7uJ0xCFQy8hWRMQsFf5c22mepXHq%2FsY5GgRPIZzg1Gemp6ol%2FAGo5bCD6x2vDM43AmeSRNAdmSrxD9sWgp0co%2F1Vbvb%2BpKS841sKJWgv3zAIUcdFk35abShRLypUBybp7E1yms5aiEvA5w1ciA8sUw0OCYvQY6pgFjHkeurj1CZ3ZLwSN%2BfD5y%2Fdbfg90DeqHB0YktXpfQWld2dTtZHQm2X9GVG3bqwBzPvxb2Z6jU%2BG5yvXlskZlusN0aeJ4TU%2Br6j%2BB6I3t1ezsttpz%2FxZWkp2znVAm7GcCQYKbldDcPh%2FAG%2BozLEHdzYJooYUkw4GPnbdX%2FvDBPMmRFncj6KR7YJkWejUz6o2YBu%2BQoLtKxbm5yWMFUQ4r1a1e3TI4h&X-Amz-Signature=af8ff8569db9cce955923bcab696aebdb5b24e60d587381c0d8f033211ba5389&X-Amz-SignedHeaders=host&x-id=GetObject)
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