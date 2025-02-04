

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPWNKDKN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIB3HdADn%2BFjYkViwXpLFssCNetrI5r%2BnIxe2jgJN3S%2ByAiAwP6MxkqvKOA%2BS7i3FiKXxKxhkaC7nO57wiF3%2FoeTJiCr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMMEL7uoFO1IB%2FHrx3KtwDceqFHf5kS9kyNzDN3vHaTMUqHpSVBzPJvD8IUa%2BE2N%2Br5WucYWTae9UAFj%2FhqfN4m4Euj4r816dh23act%2B7CCUpI7tYs7NBp3IptpWQDS%2BZqd1g6pUs7aAV61PJtjbHdQbLz9WI%2BXLt9soTBTm%2FWRBgnLiAb7yRZ1mv6kcg70p4s2fnJhVNjCjlGMDnVX2QhgSNrdjp0hk3k0RndmUkApOURpBjq2WC0CE3ID1DAuYFX6Tan5gTgZ54odhnzHdhowhf0fqlC82TNenhJEwK6ePPtUVenwm8Y%2Flycl4lYAJTunOjBaayRyOx9xHeJSUJ243NqY0N%2BtPXj6w9rSIdQ4eIJDSbuSCDbWkJJVyvBDR6lXnj1IqlN5iGhHVgcSPL%2BB%2FjRvWfZfukqx3VujjW7H5dEnvRrEtpwbsYmAjUskXxT2uob3iw4yXB1iUA3im7Jy5DvYAegsu36AbhNVtwfcOzocXTf57yg%2Fu%2B9%2BE8QxYyVuNSPJeu8OBpRxJYzZ%2BcvNKe4S6W4sXHWIUefZn4WPO4rURrxzERA%2BA20jqm0tqEHmw3jFhiZKd45YYQ8aboyp6S4hM69XUt3Ep4%2BMtQHXB18s2tWopnqsaP%2BNc24kgGJOJgSQrygcKuIru0w3L6GvQY6pgFqoo4FUsRQS0eyr3d%2Bn9gex5YgHsuK1JL04lZXeyxWZ98%2BHq5OcxsI7e1YnQMXmogFdBBwzLqnFmSetTt63XU48hvhv9oRI4JUiy8cfaPSlU8wXcfcvHlgLdpFyRjHkxoISub4V2iycFAl7kG90eWSTGdylHjxn6xWtuUWJcMUx7OjgTKQ5wbM6xGDvkvZzYj5qj5TF7sPs5h6bK%2BmGLnmRjEj2QID&X-Amz-Signature=a9b7305799151fcb3a4c3621682c3669f866fe354c9613c21b6e3dc6ee001076&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPWNKDKN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIB3HdADn%2BFjYkViwXpLFssCNetrI5r%2BnIxe2jgJN3S%2ByAiAwP6MxkqvKOA%2BS7i3FiKXxKxhkaC7nO57wiF3%2FoeTJiCr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMMEL7uoFO1IB%2FHrx3KtwDceqFHf5kS9kyNzDN3vHaTMUqHpSVBzPJvD8IUa%2BE2N%2Br5WucYWTae9UAFj%2FhqfN4m4Euj4r816dh23act%2B7CCUpI7tYs7NBp3IptpWQDS%2BZqd1g6pUs7aAV61PJtjbHdQbLz9WI%2BXLt9soTBTm%2FWRBgnLiAb7yRZ1mv6kcg70p4s2fnJhVNjCjlGMDnVX2QhgSNrdjp0hk3k0RndmUkApOURpBjq2WC0CE3ID1DAuYFX6Tan5gTgZ54odhnzHdhowhf0fqlC82TNenhJEwK6ePPtUVenwm8Y%2Flycl4lYAJTunOjBaayRyOx9xHeJSUJ243NqY0N%2BtPXj6w9rSIdQ4eIJDSbuSCDbWkJJVyvBDR6lXnj1IqlN5iGhHVgcSPL%2BB%2FjRvWfZfukqx3VujjW7H5dEnvRrEtpwbsYmAjUskXxT2uob3iw4yXB1iUA3im7Jy5DvYAegsu36AbhNVtwfcOzocXTf57yg%2Fu%2B9%2BE8QxYyVuNSPJeu8OBpRxJYzZ%2BcvNKe4S6W4sXHWIUefZn4WPO4rURrxzERA%2BA20jqm0tqEHmw3jFhiZKd45YYQ8aboyp6S4hM69XUt3Ep4%2BMtQHXB18s2tWopnqsaP%2BNc24kgGJOJgSQrygcKuIru0w3L6GvQY6pgFqoo4FUsRQS0eyr3d%2Bn9gex5YgHsuK1JL04lZXeyxWZ98%2BHq5OcxsI7e1YnQMXmogFdBBwzLqnFmSetTt63XU48hvhv9oRI4JUiy8cfaPSlU8wXcfcvHlgLdpFyRjHkxoISub4V2iycFAl7kG90eWSTGdylHjxn6xWtuUWJcMUx7OjgTKQ5wbM6xGDvkvZzYj5qj5TF7sPs5h6bK%2BmGLnmRjEj2QID&X-Amz-Signature=12a9066dbb8027f12e89b63b7e30e016aa420914ea5f177f42f4f2ce466eb9fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPWNKDKN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIB3HdADn%2BFjYkViwXpLFssCNetrI5r%2BnIxe2jgJN3S%2ByAiAwP6MxkqvKOA%2BS7i3FiKXxKxhkaC7nO57wiF3%2FoeTJiCr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMMEL7uoFO1IB%2FHrx3KtwDceqFHf5kS9kyNzDN3vHaTMUqHpSVBzPJvD8IUa%2BE2N%2Br5WucYWTae9UAFj%2FhqfN4m4Euj4r816dh23act%2B7CCUpI7tYs7NBp3IptpWQDS%2BZqd1g6pUs7aAV61PJtjbHdQbLz9WI%2BXLt9soTBTm%2FWRBgnLiAb7yRZ1mv6kcg70p4s2fnJhVNjCjlGMDnVX2QhgSNrdjp0hk3k0RndmUkApOURpBjq2WC0CE3ID1DAuYFX6Tan5gTgZ54odhnzHdhowhf0fqlC82TNenhJEwK6ePPtUVenwm8Y%2Flycl4lYAJTunOjBaayRyOx9xHeJSUJ243NqY0N%2BtPXj6w9rSIdQ4eIJDSbuSCDbWkJJVyvBDR6lXnj1IqlN5iGhHVgcSPL%2BB%2FjRvWfZfukqx3VujjW7H5dEnvRrEtpwbsYmAjUskXxT2uob3iw4yXB1iUA3im7Jy5DvYAegsu36AbhNVtwfcOzocXTf57yg%2Fu%2B9%2BE8QxYyVuNSPJeu8OBpRxJYzZ%2BcvNKe4S6W4sXHWIUefZn4WPO4rURrxzERA%2BA20jqm0tqEHmw3jFhiZKd45YYQ8aboyp6S4hM69XUt3Ep4%2BMtQHXB18s2tWopnqsaP%2BNc24kgGJOJgSQrygcKuIru0w3L6GvQY6pgFqoo4FUsRQS0eyr3d%2Bn9gex5YgHsuK1JL04lZXeyxWZ98%2BHq5OcxsI7e1YnQMXmogFdBBwzLqnFmSetTt63XU48hvhv9oRI4JUiy8cfaPSlU8wXcfcvHlgLdpFyRjHkxoISub4V2iycFAl7kG90eWSTGdylHjxn6xWtuUWJcMUx7OjgTKQ5wbM6xGDvkvZzYj5qj5TF7sPs5h6bK%2BmGLnmRjEj2QID&X-Amz-Signature=f02fd7d37e87a84dce3ab4f900b44a78ddb8326f57509175dea1885d308ce7ab&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZ6LUQHJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIC7TcAv8MhuNEb%2FNKcvR%2FJVK8AqQRogdeLdD0PxzF6a6AiArRwjvcREMdNjHSczgbj7pahJqgR25U28fEuMnqi2Mlir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMB%2Fwx5NRLJI%2FB8Et7KtwDVKI3yGQ%2BzDf0PJUMT%2BP%2BKR9D9%2FgjsmSRlBHM%2BiR0aQiCGuFobLcXFzQZmjQlgbZvjWx5Rps%2Fq2qwFYI0eh346nzAMWlS%2BGjYQWLvTeC6NJxV1sSbBBqkkgu84Efr%2FtsnfCqwmITMUL4k35R4OjnZfZBR5JnUdPZWqz9NsXFuQIK%2B7MEQmwxA51TPWwYHSQ%2FhWahE%2F8y%2FCz%2FdMikjgpdntlHfBrEfTn%2BvAxYjZ9GXtmhtmBPQvG9uslg2pu1hyqkReunQPZ3PXfxdmLSMeE4CdZDZggOF%2BG0FzPX3RuYtyfuH%2ByejFs4q8%2BvxhBsDzu44FPEFmkMYRr5FEYvQd3B9SQEkDO%2B7Seg62%2FDhzxqxcIwaw65JHNh9W0NMBZtdPoYxwQjpHID7ItpmAAmHPR0dvKn1jhmzIUm86gDB5yxlZfyEkOzX0F53fS8q424jphhVzpYbDe1F8ohH3R3sQ7rXjeCsEjfAKPFBYCI%2BdCYslk%2Bo5ra6mkrei%2FU5oUBjB28wLWK2wO7Ez0kHSlJ5j6eYd7CP6XfyKDkY5XmGXw1WgWAwpavfIptHtfAJ3Rhc6EfIKf3KlQsMV0tGgxPcsa8JQCyoBmRBH%2B21lD0OnbjmGQRcu8iF14Qi1yDYIzcw1r6GvQY6pgHj3YLIdwLLCODSitPXQ1Z4BS816%2BNzth%2BxgSo%2BZzeXfgehcGNF2hBllsqdB4HS5bw4wlXsPKOJarVcwBwxZt9aHvp%2BmNk64qr0pjd%2BTOMnp96lmb8qFykYAAMJoVfFE2dtqbL37rljEEZFPkO%2FLqhSFfYs4aDs%2BCo8Ry%2B6Lhdqj5PZ%2BspTnTGI88fkXmIjFDmde6uqSh%2BGHMLks0azUOEBc%2FfXTpx9&X-Amz-Signature=c9cc13dd8439c63dff49c25010c9f059f6ef3fa93efdacade058b97a0ba6a2a2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZ6LUQHJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIC7TcAv8MhuNEb%2FNKcvR%2FJVK8AqQRogdeLdD0PxzF6a6AiArRwjvcREMdNjHSczgbj7pahJqgR25U28fEuMnqi2Mlir%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMB%2Fwx5NRLJI%2FB8Et7KtwDVKI3yGQ%2BzDf0PJUMT%2BP%2BKR9D9%2FgjsmSRlBHM%2BiR0aQiCGuFobLcXFzQZmjQlgbZvjWx5Rps%2Fq2qwFYI0eh346nzAMWlS%2BGjYQWLvTeC6NJxV1sSbBBqkkgu84Efr%2FtsnfCqwmITMUL4k35R4OjnZfZBR5JnUdPZWqz9NsXFuQIK%2B7MEQmwxA51TPWwYHSQ%2FhWahE%2F8y%2FCz%2FdMikjgpdntlHfBrEfTn%2BvAxYjZ9GXtmhtmBPQvG9uslg2pu1hyqkReunQPZ3PXfxdmLSMeE4CdZDZggOF%2BG0FzPX3RuYtyfuH%2ByejFs4q8%2BvxhBsDzu44FPEFmkMYRr5FEYvQd3B9SQEkDO%2B7Seg62%2FDhzxqxcIwaw65JHNh9W0NMBZtdPoYxwQjpHID7ItpmAAmHPR0dvKn1jhmzIUm86gDB5yxlZfyEkOzX0F53fS8q424jphhVzpYbDe1F8ohH3R3sQ7rXjeCsEjfAKPFBYCI%2BdCYslk%2Bo5ra6mkrei%2FU5oUBjB28wLWK2wO7Ez0kHSlJ5j6eYd7CP6XfyKDkY5XmGXw1WgWAwpavfIptHtfAJ3Rhc6EfIKf3KlQsMV0tGgxPcsa8JQCyoBmRBH%2B21lD0OnbjmGQRcu8iF14Qi1yDYIzcw1r6GvQY6pgHj3YLIdwLLCODSitPXQ1Z4BS816%2BNzth%2BxgSo%2BZzeXfgehcGNF2hBllsqdB4HS5bw4wlXsPKOJarVcwBwxZt9aHvp%2BmNk64qr0pjd%2BTOMnp96lmb8qFykYAAMJoVfFE2dtqbL37rljEEZFPkO%2FLqhSFfYs4aDs%2BCo8Ry%2B6Lhdqj5PZ%2BspTnTGI88fkXmIjFDmde6uqSh%2BGHMLks0azUOEBc%2FfXTpx9&X-Amz-Signature=ecdf94fe1e3ace697922abf020b94aafb51c3bbe3609b813a60178ed16706dc0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPWNKDKN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIB3HdADn%2BFjYkViwXpLFssCNetrI5r%2BnIxe2jgJN3S%2ByAiAwP6MxkqvKOA%2BS7i3FiKXxKxhkaC7nO57wiF3%2FoeTJiCr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMMEL7uoFO1IB%2FHrx3KtwDceqFHf5kS9kyNzDN3vHaTMUqHpSVBzPJvD8IUa%2BE2N%2Br5WucYWTae9UAFj%2FhqfN4m4Euj4r816dh23act%2B7CCUpI7tYs7NBp3IptpWQDS%2BZqd1g6pUs7aAV61PJtjbHdQbLz9WI%2BXLt9soTBTm%2FWRBgnLiAb7yRZ1mv6kcg70p4s2fnJhVNjCjlGMDnVX2QhgSNrdjp0hk3k0RndmUkApOURpBjq2WC0CE3ID1DAuYFX6Tan5gTgZ54odhnzHdhowhf0fqlC82TNenhJEwK6ePPtUVenwm8Y%2Flycl4lYAJTunOjBaayRyOx9xHeJSUJ243NqY0N%2BtPXj6w9rSIdQ4eIJDSbuSCDbWkJJVyvBDR6lXnj1IqlN5iGhHVgcSPL%2BB%2FjRvWfZfukqx3VujjW7H5dEnvRrEtpwbsYmAjUskXxT2uob3iw4yXB1iUA3im7Jy5DvYAegsu36AbhNVtwfcOzocXTf57yg%2Fu%2B9%2BE8QxYyVuNSPJeu8OBpRxJYzZ%2BcvNKe4S6W4sXHWIUefZn4WPO4rURrxzERA%2BA20jqm0tqEHmw3jFhiZKd45YYQ8aboyp6S4hM69XUt3Ep4%2BMtQHXB18s2tWopnqsaP%2BNc24kgGJOJgSQrygcKuIru0w3L6GvQY6pgFqoo4FUsRQS0eyr3d%2Bn9gex5YgHsuK1JL04lZXeyxWZ98%2BHq5OcxsI7e1YnQMXmogFdBBwzLqnFmSetTt63XU48hvhv9oRI4JUiy8cfaPSlU8wXcfcvHlgLdpFyRjHkxoISub4V2iycFAl7kG90eWSTGdylHjxn6xWtuUWJcMUx7OjgTKQ5wbM6xGDvkvZzYj5qj5TF7sPs5h6bK%2BmGLnmRjEj2QID&X-Amz-Signature=1cb61f758a9a914dc7c2abbbbd981e124551782f42351b3fe56535887164817d&X-Amz-SignedHeaders=host&x-id=GetObject)
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