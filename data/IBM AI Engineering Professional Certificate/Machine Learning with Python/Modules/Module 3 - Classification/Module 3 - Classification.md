

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBZQFNZB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIFN%2FoZ4hqybH6QzdpCqI7tXmMvPS0a6QronHerGQ9EKDAiEA6npnsBKpE4p%2FWxZa%2FjxACWW29cVLmaaOxnkMP0CBlQ4q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHBxfqtCPaNzBbBHkSrcA3wc2eLB1vRIMU8qRWHARk6BXD4h0r84I%2FYkD5J2gq1OrolQAfu1m3VzRZl8ZO6K3vC1lhsRmYrddEPSOpfoDw34%2BO82zbKN2PTYWmwBfdkwO%2FF4YD6bw08HFennlmvkQNaZ%2FLhPYMtQt7eqoLQH6%2BZhi6rZdlL9GK%2FzwPdY86hPvAnJHxepuYBmePu9O1GG9E1cHJoaGzYC8xIaxSbeK7jskj%2BRzJDiGyfH%2Fi75OkblBPKGmsFQASfG9mqydHgamuuRNIDmcVXwZC4s7%2BqGYaXn2uJoaz729hWGJKWT4sgPbpaHCSgVZW23rJHxNvljrAgaSfBRFTHrLtB3XU%2FYXjsuP%2Bm9q0ypKI6wHp96Qk%2Bb4tFWrZFyCBKhv09Y%2BAimF6nt62jaYMReu3Pr%2FrIwbmA6bU5RhIm8WkF4ITQ7OC5BgazsGNI33cWTMvkjhpzHszsFZRNtIVfFltMIfOiqmVwxjqpLDKclps8AUuYIVANauWDM%2BzgSwPBXc8E2c2%2BEzsTubN2xD0Bcva28dktjBc3wWmPwrkwElCL%2FqGIaW09rBynhMS%2B1QrHqnw%2BcEpFG0Y2ozhs2uOgdp2zLFAV5dRtub8cD9FW2AF%2BYaNc5%2BwEMG2%2FiESt8MY%2Fmz9XuMI6ck70GOqUBVSGGywsQgwAh3ha9a6mBWkq%2F4e0XIlCBsh49ZSSFjqyErykpNxC3YbWY%2F%2BVFANZ0Ozb7CIuehi72qrmJI5tAY070q7IKdQY8eeZ1l1Po3dq%2BkKdHFzDdUzjyOE47nY3tIrznYZiddZteHfdB6TT6Re6iG%2FcucBP8k3DriQtSoGkVlUwbvhEYt7JXKV0LW8azJTXIxKHEB2tmJbLo%2BDhexxjiFXIH&X-Amz-Signature=64d0cd71b01b4d879eed5588baa85a81b50961a7e9290e71cad96492d69ac3c6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBZQFNZB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIFN%2FoZ4hqybH6QzdpCqI7tXmMvPS0a6QronHerGQ9EKDAiEA6npnsBKpE4p%2FWxZa%2FjxACWW29cVLmaaOxnkMP0CBlQ4q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHBxfqtCPaNzBbBHkSrcA3wc2eLB1vRIMU8qRWHARk6BXD4h0r84I%2FYkD5J2gq1OrolQAfu1m3VzRZl8ZO6K3vC1lhsRmYrddEPSOpfoDw34%2BO82zbKN2PTYWmwBfdkwO%2FF4YD6bw08HFennlmvkQNaZ%2FLhPYMtQt7eqoLQH6%2BZhi6rZdlL9GK%2FzwPdY86hPvAnJHxepuYBmePu9O1GG9E1cHJoaGzYC8xIaxSbeK7jskj%2BRzJDiGyfH%2Fi75OkblBPKGmsFQASfG9mqydHgamuuRNIDmcVXwZC4s7%2BqGYaXn2uJoaz729hWGJKWT4sgPbpaHCSgVZW23rJHxNvljrAgaSfBRFTHrLtB3XU%2FYXjsuP%2Bm9q0ypKI6wHp96Qk%2Bb4tFWrZFyCBKhv09Y%2BAimF6nt62jaYMReu3Pr%2FrIwbmA6bU5RhIm8WkF4ITQ7OC5BgazsGNI33cWTMvkjhpzHszsFZRNtIVfFltMIfOiqmVwxjqpLDKclps8AUuYIVANauWDM%2BzgSwPBXc8E2c2%2BEzsTubN2xD0Bcva28dktjBc3wWmPwrkwElCL%2FqGIaW09rBynhMS%2B1QrHqnw%2BcEpFG0Y2ozhs2uOgdp2zLFAV5dRtub8cD9FW2AF%2BYaNc5%2BwEMG2%2FiESt8MY%2Fmz9XuMI6ck70GOqUBVSGGywsQgwAh3ha9a6mBWkq%2F4e0XIlCBsh49ZSSFjqyErykpNxC3YbWY%2F%2BVFANZ0Ozb7CIuehi72qrmJI5tAY070q7IKdQY8eeZ1l1Po3dq%2BkKdHFzDdUzjyOE47nY3tIrznYZiddZteHfdB6TT6Re6iG%2FcucBP8k3DriQtSoGkVlUwbvhEYt7JXKV0LW8azJTXIxKHEB2tmJbLo%2BDhexxjiFXIH&X-Amz-Signature=6ff0bfc94aa4137a21f10b65685a11fc2302a3e5c1151e4f3f12a6d41d4673b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBZQFNZB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIFN%2FoZ4hqybH6QzdpCqI7tXmMvPS0a6QronHerGQ9EKDAiEA6npnsBKpE4p%2FWxZa%2FjxACWW29cVLmaaOxnkMP0CBlQ4q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHBxfqtCPaNzBbBHkSrcA3wc2eLB1vRIMU8qRWHARk6BXD4h0r84I%2FYkD5J2gq1OrolQAfu1m3VzRZl8ZO6K3vC1lhsRmYrddEPSOpfoDw34%2BO82zbKN2PTYWmwBfdkwO%2FF4YD6bw08HFennlmvkQNaZ%2FLhPYMtQt7eqoLQH6%2BZhi6rZdlL9GK%2FzwPdY86hPvAnJHxepuYBmePu9O1GG9E1cHJoaGzYC8xIaxSbeK7jskj%2BRzJDiGyfH%2Fi75OkblBPKGmsFQASfG9mqydHgamuuRNIDmcVXwZC4s7%2BqGYaXn2uJoaz729hWGJKWT4sgPbpaHCSgVZW23rJHxNvljrAgaSfBRFTHrLtB3XU%2FYXjsuP%2Bm9q0ypKI6wHp96Qk%2Bb4tFWrZFyCBKhv09Y%2BAimF6nt62jaYMReu3Pr%2FrIwbmA6bU5RhIm8WkF4ITQ7OC5BgazsGNI33cWTMvkjhpzHszsFZRNtIVfFltMIfOiqmVwxjqpLDKclps8AUuYIVANauWDM%2BzgSwPBXc8E2c2%2BEzsTubN2xD0Bcva28dktjBc3wWmPwrkwElCL%2FqGIaW09rBynhMS%2B1QrHqnw%2BcEpFG0Y2ozhs2uOgdp2zLFAV5dRtub8cD9FW2AF%2BYaNc5%2BwEMG2%2FiESt8MY%2Fmz9XuMI6ck70GOqUBVSGGywsQgwAh3ha9a6mBWkq%2F4e0XIlCBsh49ZSSFjqyErykpNxC3YbWY%2F%2BVFANZ0Ozb7CIuehi72qrmJI5tAY070q7IKdQY8eeZ1l1Po3dq%2BkKdHFzDdUzjyOE47nY3tIrznYZiddZteHfdB6TT6Re6iG%2FcucBP8k3DriQtSoGkVlUwbvhEYt7JXKV0LW8azJTXIxKHEB2tmJbLo%2BDhexxjiFXIH&X-Amz-Signature=fee9df076b0d6233965658d677f0aae2adf5c3b4b2a3c395b894fe71a26570bc&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643KOGEXA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIG9tf5V3yp2OK%2BtU%2BB%2BkcP75z05v3Kc%2BUXHdadSrYQH5AiEAmgTFbPQ6IEkYTFb8uCa97z331inozhyXZcCSm9X3U6cq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDK8oNYBRcSt7xreMqyrcAwFCXo92OgdLzMVQIPt26O6UUxONhAtcgtAN1HL8xlkOUfTLhfh1PV2m8lPKhjL6N6bI4eWq46RkF%2B%2FDQ6oElMn7MhRDAYAux28O361L2qLnKVU5iqhNADkuq4xEypuVZErNoYn40hZxAfCJmDeeYGU3pmHhrPBSBVJoR%2FoV5LjkpCUNN4yIx5%2BXFTqTghzdLhZ6MuDfrLatv9405HTXvnGOd%2FzsqAY9q1AMm%2F4qDADAvj5ayyZi4A4jAvy%2B3dtr6qOY0LzcQX0ohIpkWCz21t9M4Fy24XD9QqIoj3EVmPVO7kHhxJ6hFHq4jcFsxzM62LrTs2%2FR96fRYe2%2B2uKaq9vEss3edfyaUzO%2FQkZplnOOpZ2QAze9jkqUY82pXJeRjNxf8sRGYgI0tdIrkwUE7sIcLe39L34bUZlFGQ70SR1CIHn%2FUsYdUEJS6CGzk687ygPkgPAtdhQXdF1iaqbd2Vt%2BLTuhj2BC0LDjMxLUBLcOc3en%2FljeIGb55qphOHcyij5YLzGJlhsX7FgjcYSvi4Lqg2GwfqqkoCTLvDX6o1xp0LTmzlGeYKn4eebnOZ3%2B7mZsbOOwzQU0sruxBosz1w2Ow%2BGtjpJDOakXdIR4CImB2Fj8jowegAQ5f4lRMIWck70GOqUB28PwDVmank2MlS7gIFxI9cI739qm%2Fo1K7a%2Bsf4k5%2FzOXOkmTAsYzSRhAFRASWueai5dIDftrxQ%2F%2F8FWBKwOwybx1H1f%2B3vblLdtSl4dl%2FORtTEYqQEmkwORQlfGCe4Q3j5Q2wKGVf%2Fz04RfhQL6Mjkw%2Fif4ik8Q6iQvp7cz7l%2BcBWWUqb6LmwnNh4He%2FHg7UMoguflJwacByqJQ68bTST88usn6a&X-Amz-Signature=1ad0615931e08d3eca97741daace7e6e5706d77c0c2e18d939e99bf88407c31a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643KOGEXA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIG9tf5V3yp2OK%2BtU%2BB%2BkcP75z05v3Kc%2BUXHdadSrYQH5AiEAmgTFbPQ6IEkYTFb8uCa97z331inozhyXZcCSm9X3U6cq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDK8oNYBRcSt7xreMqyrcAwFCXo92OgdLzMVQIPt26O6UUxONhAtcgtAN1HL8xlkOUfTLhfh1PV2m8lPKhjL6N6bI4eWq46RkF%2B%2FDQ6oElMn7MhRDAYAux28O361L2qLnKVU5iqhNADkuq4xEypuVZErNoYn40hZxAfCJmDeeYGU3pmHhrPBSBVJoR%2FoV5LjkpCUNN4yIx5%2BXFTqTghzdLhZ6MuDfrLatv9405HTXvnGOd%2FzsqAY9q1AMm%2F4qDADAvj5ayyZi4A4jAvy%2B3dtr6qOY0LzcQX0ohIpkWCz21t9M4Fy24XD9QqIoj3EVmPVO7kHhxJ6hFHq4jcFsxzM62LrTs2%2FR96fRYe2%2B2uKaq9vEss3edfyaUzO%2FQkZplnOOpZ2QAze9jkqUY82pXJeRjNxf8sRGYgI0tdIrkwUE7sIcLe39L34bUZlFGQ70SR1CIHn%2FUsYdUEJS6CGzk687ygPkgPAtdhQXdF1iaqbd2Vt%2BLTuhj2BC0LDjMxLUBLcOc3en%2FljeIGb55qphOHcyij5YLzGJlhsX7FgjcYSvi4Lqg2GwfqqkoCTLvDX6o1xp0LTmzlGeYKn4eebnOZ3%2B7mZsbOOwzQU0sruxBosz1w2Ow%2BGtjpJDOakXdIR4CImB2Fj8jowegAQ5f4lRMIWck70GOqUB28PwDVmank2MlS7gIFxI9cI739qm%2Fo1K7a%2Bsf4k5%2FzOXOkmTAsYzSRhAFRASWueai5dIDftrxQ%2F%2F8FWBKwOwybx1H1f%2B3vblLdtSl4dl%2FORtTEYqQEmkwORQlfGCe4Q3j5Q2wKGVf%2Fz04RfhQL6Mjkw%2Fif4ik8Q6iQvp7cz7l%2BcBWWUqb6LmwnNh4He%2FHg7UMoguflJwacByqJQ68bTST88usn6a&X-Amz-Signature=38a87483dd06f405867870b8ab67b83a2a9948e371b964177505ddcb3f76f538&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBZQFNZB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIFN%2FoZ4hqybH6QzdpCqI7tXmMvPS0a6QronHerGQ9EKDAiEA6npnsBKpE4p%2FWxZa%2FjxACWW29cVLmaaOxnkMP0CBlQ4q%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDHBxfqtCPaNzBbBHkSrcA3wc2eLB1vRIMU8qRWHARk6BXD4h0r84I%2FYkD5J2gq1OrolQAfu1m3VzRZl8ZO6K3vC1lhsRmYrddEPSOpfoDw34%2BO82zbKN2PTYWmwBfdkwO%2FF4YD6bw08HFennlmvkQNaZ%2FLhPYMtQt7eqoLQH6%2BZhi6rZdlL9GK%2FzwPdY86hPvAnJHxepuYBmePu9O1GG9E1cHJoaGzYC8xIaxSbeK7jskj%2BRzJDiGyfH%2Fi75OkblBPKGmsFQASfG9mqydHgamuuRNIDmcVXwZC4s7%2BqGYaXn2uJoaz729hWGJKWT4sgPbpaHCSgVZW23rJHxNvljrAgaSfBRFTHrLtB3XU%2FYXjsuP%2Bm9q0ypKI6wHp96Qk%2Bb4tFWrZFyCBKhv09Y%2BAimF6nt62jaYMReu3Pr%2FrIwbmA6bU5RhIm8WkF4ITQ7OC5BgazsGNI33cWTMvkjhpzHszsFZRNtIVfFltMIfOiqmVwxjqpLDKclps8AUuYIVANauWDM%2BzgSwPBXc8E2c2%2BEzsTubN2xD0Bcva28dktjBc3wWmPwrkwElCL%2FqGIaW09rBynhMS%2B1QrHqnw%2BcEpFG0Y2ozhs2uOgdp2zLFAV5dRtub8cD9FW2AF%2BYaNc5%2BwEMG2%2FiESt8MY%2Fmz9XuMI6ck70GOqUBVSGGywsQgwAh3ha9a6mBWkq%2F4e0XIlCBsh49ZSSFjqyErykpNxC3YbWY%2F%2BVFANZ0Ozb7CIuehi72qrmJI5tAY070q7IKdQY8eeZ1l1Po3dq%2BkKdHFzDdUzjyOE47nY3tIrznYZiddZteHfdB6TT6Re6iG%2FcucBP8k3DriQtSoGkVlUwbvhEYt7JXKV0LW8azJTXIxKHEB2tmJbLo%2BDhexxjiFXIH&X-Amz-Signature=ad49c85686400a3d7377ffd4a875cf94d92dd10a86fa085e28c7e7a20cbe7604&X-Amz-SignedHeaders=host&x-id=GetObject)
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