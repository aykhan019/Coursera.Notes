

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXNFKQKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTnwey3VIqEw8UTgfod7987Ygi2SAi8xM8zUO6SGz38QIgbZh%2F4Io0zO%2B0cHUbybPAiWwhU4jegNiMTwOa0VR0s%2BgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDX3sHM5%2FP88KWzcMCrcA8SPGtr65Yzw66kboMlhs6OPDNlQ7N8nyqBD2VpRzIXsPO4YcqEuUVFM3WFHaJbchmgahrluNNdaTCKjDyffTKrJvKaRIjptjC7rODhoWTICd%2F2CKx%2F%2B8%2BwPeiFSUrnFKkzFY5APt1lUYkMhpJJ105dwuRLjO%2BYe5KLXBRezXVbzUXrNStwIjPnB9Fd%2FuImwjSL2Ay%2ByjoWRL06e4UZgtmxX6EE213M%2Fmcaof3%2Bb7kLZ%2BpHQnPyYcllGhIPL4715qJrKsntfjuctYKBbqDTodo4pJlVIDTQb4ABHUZxKoEjud33WjuCCoFxmG56CvSZe7rDH1QRPOGD0w7TQvJfqLXXnnduxq7VWFizb4U%2Bqj3KHPejoTV5v1fn2pKgBXQ%2FHAgxbEucuxFBlqT4d3%2B%2Fdd1wrFPXT3eTdQ3fxub%2BmC3XsHg0KoipYli%2B%2FdZ70LZlqDwIoM%2FCy8cM0oT8TkaTATLS9gWil3MWhQGO0sYngtyIcmfzP%2FIz2Td9gzJ9faNZVbWb1%2BvcI4QO3%2BIczAmyAKQr5SXQUiv4gmpk6qHSnVJrEFZcuvOCsGVGrFk0BU9IbvYCO0WJTstc0JS39KZmDmk4Jx1U3PurH%2B7Bum%2BW3EvtI5Dx1y88yWf6WTADeMPeNnL0GOqUB%2F5D0NCoP8XlJm%2B5WtX8xgO8UF7UM0x6NIY6R4RCM6HwDIHDOjgZ4Witk7k85JbMNCA34AykA9a%2BlDPthdGTJpnSFESUkfXvR5FHRt1mAw0m9dJctlsZ%2B%2Bdtw9vAJyUhVtMqoyh5YHILYDhCBP2L%2BIz5AZ8xWP%2F6fVVQafQjAj6JkyyT5FcJ1tI%2F%2FOhFZfakKf3CBsR7l9eKT3RCh6xXD%2F7gQQHS8&X-Amz-Signature=d695f18d31c2938c28b802d5df86ee2cdb42ee84db053ef51c8c087e5ad668af&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXNFKQKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTnwey3VIqEw8UTgfod7987Ygi2SAi8xM8zUO6SGz38QIgbZh%2F4Io0zO%2B0cHUbybPAiWwhU4jegNiMTwOa0VR0s%2BgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDX3sHM5%2FP88KWzcMCrcA8SPGtr65Yzw66kboMlhs6OPDNlQ7N8nyqBD2VpRzIXsPO4YcqEuUVFM3WFHaJbchmgahrluNNdaTCKjDyffTKrJvKaRIjptjC7rODhoWTICd%2F2CKx%2F%2B8%2BwPeiFSUrnFKkzFY5APt1lUYkMhpJJ105dwuRLjO%2BYe5KLXBRezXVbzUXrNStwIjPnB9Fd%2FuImwjSL2Ay%2ByjoWRL06e4UZgtmxX6EE213M%2Fmcaof3%2Bb7kLZ%2BpHQnPyYcllGhIPL4715qJrKsntfjuctYKBbqDTodo4pJlVIDTQb4ABHUZxKoEjud33WjuCCoFxmG56CvSZe7rDH1QRPOGD0w7TQvJfqLXXnnduxq7VWFizb4U%2Bqj3KHPejoTV5v1fn2pKgBXQ%2FHAgxbEucuxFBlqT4d3%2B%2Fdd1wrFPXT3eTdQ3fxub%2BmC3XsHg0KoipYli%2B%2FdZ70LZlqDwIoM%2FCy8cM0oT8TkaTATLS9gWil3MWhQGO0sYngtyIcmfzP%2FIz2Td9gzJ9faNZVbWb1%2BvcI4QO3%2BIczAmyAKQr5SXQUiv4gmpk6qHSnVJrEFZcuvOCsGVGrFk0BU9IbvYCO0WJTstc0JS39KZmDmk4Jx1U3PurH%2B7Bum%2BW3EvtI5Dx1y88yWf6WTADeMPeNnL0GOqUB%2F5D0NCoP8XlJm%2B5WtX8xgO8UF7UM0x6NIY6R4RCM6HwDIHDOjgZ4Witk7k85JbMNCA34AykA9a%2BlDPthdGTJpnSFESUkfXvR5FHRt1mAw0m9dJctlsZ%2B%2Bdtw9vAJyUhVtMqoyh5YHILYDhCBP2L%2BIz5AZ8xWP%2F6fVVQafQjAj6JkyyT5FcJ1tI%2F%2FOhFZfakKf3CBsR7l9eKT3RCh6xXD%2F7gQQHS8&X-Amz-Signature=0b534342ed20ff88168a863074767580b6e782053ebe67da0b3c5ecf5d20b307&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXNFKQKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTnwey3VIqEw8UTgfod7987Ygi2SAi8xM8zUO6SGz38QIgbZh%2F4Io0zO%2B0cHUbybPAiWwhU4jegNiMTwOa0VR0s%2BgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDX3sHM5%2FP88KWzcMCrcA8SPGtr65Yzw66kboMlhs6OPDNlQ7N8nyqBD2VpRzIXsPO4YcqEuUVFM3WFHaJbchmgahrluNNdaTCKjDyffTKrJvKaRIjptjC7rODhoWTICd%2F2CKx%2F%2B8%2BwPeiFSUrnFKkzFY5APt1lUYkMhpJJ105dwuRLjO%2BYe5KLXBRezXVbzUXrNStwIjPnB9Fd%2FuImwjSL2Ay%2ByjoWRL06e4UZgtmxX6EE213M%2Fmcaof3%2Bb7kLZ%2BpHQnPyYcllGhIPL4715qJrKsntfjuctYKBbqDTodo4pJlVIDTQb4ABHUZxKoEjud33WjuCCoFxmG56CvSZe7rDH1QRPOGD0w7TQvJfqLXXnnduxq7VWFizb4U%2Bqj3KHPejoTV5v1fn2pKgBXQ%2FHAgxbEucuxFBlqT4d3%2B%2Fdd1wrFPXT3eTdQ3fxub%2BmC3XsHg0KoipYli%2B%2FdZ70LZlqDwIoM%2FCy8cM0oT8TkaTATLS9gWil3MWhQGO0sYngtyIcmfzP%2FIz2Td9gzJ9faNZVbWb1%2BvcI4QO3%2BIczAmyAKQr5SXQUiv4gmpk6qHSnVJrEFZcuvOCsGVGrFk0BU9IbvYCO0WJTstc0JS39KZmDmk4Jx1U3PurH%2B7Bum%2BW3EvtI5Dx1y88yWf6WTADeMPeNnL0GOqUB%2F5D0NCoP8XlJm%2B5WtX8xgO8UF7UM0x6NIY6R4RCM6HwDIHDOjgZ4Witk7k85JbMNCA34AykA9a%2BlDPthdGTJpnSFESUkfXvR5FHRt1mAw0m9dJctlsZ%2B%2Bdtw9vAJyUhVtMqoyh5YHILYDhCBP2L%2BIz5AZ8xWP%2F6fVVQafQjAj6JkyyT5FcJ1tI%2F%2FOhFZfakKf3CBsR7l9eKT3RCh6xXD%2F7gQQHS8&X-Amz-Signature=8f9ad51d37b857afefcc87c044672b32942185bb49e1fd65d6f4fd5e71ae4518&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFEIJP5C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDSKaA5R2Q18Rp277z9pkpvUXL6uDh1jU7icqj7W4LLYAiEArL0w09WmkvHLVEwGpkognpfX6Vq8%2BOXgP34mluTvgbsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6CFAC0IQ0nO34aQSrcA9OPYwyJ5qxvCOFD9gsyqCep1kzPwP38z5rBxOp7x9FWAXUeLDPXabGdlHO1j4sqcHPj6pZIMWdo71ExMSTAUyakQKBwOlqcIHjZgaX624%2FnQG%2BvJp2owY8o699MhIK5GgY6ze6n1V%2FPevoPhXo3RhraP81x5d72Frt5qeYHpQpAz83LWpSWAVUqTFZ%2BOWv6s0W5MK0Fj%2BpJ41UCfYDqUBClwIKYS2DBqfpP3uGzCQWqX0qAjfOnTjLMvNFQh7%2B%2BxkXG%2Bhnc8ycEaCmk9D7X2ttcVtlPvIKIjfumpj7MGbQ2%2FTNTI3WrM1%2FPVFfRyfbu61LsopKBS025%2BLhVl3NuQ20xv3Kv4OwOG29m1svD0OPAp9sEFiINtBNsZRZnilLMKVYq%2F%2B5bn%2FyrSpg38dR7dmx6irLEb9we20GPswotZhKeVDCp%2FwU2fqeH8%2F3OWZ%2BgqAk8HRceEiepAJOlwzwD9arAQsB4YQbMC75CH4DojI1EtlKAFkbB9tvWTbqlnFAcHmhEs0oT%2FR8JGZFJh5qtGjHWYP69nKoll0i%2B7%2B6TLThQKMCgBKbE7QbN09ZHvbLPCXZR6AZcmgUgvfkvizrK6YJbUXtAZhwJq8rWTEoH9%2BfeHpllcpPDKFqM1a2CMLmOnL0GOqUBekrM82oTq7griT6foyoWw%2BdM%2F5CRuwPKhJAJ%2FdgY83WCQKPGZ5eKu2sSBfJkg5qcDWImHNqSOl0zHiOWvog6QgNYNSlDFJCAlGAboQZAzvXdZtTPGh9x6t0HzbDvTiwABZWcjM4%2BtzPRMI%2FP%2FGAx4pYCa4kRuIy8nKH%2BV68yR2pvkEvo2r2KBNh3vQdJ9sVMaeo%2F70UdWV2zV%2BGeafexvghgs%2FAl&X-Amz-Signature=bb252dbc18bb9cb967b12b798f8af08d927d2f418185e7b0f9d9d88d7103c58c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFEIJP5C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDSKaA5R2Q18Rp277z9pkpvUXL6uDh1jU7icqj7W4LLYAiEArL0w09WmkvHLVEwGpkognpfX6Vq8%2BOXgP34mluTvgbsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO6CFAC0IQ0nO34aQSrcA9OPYwyJ5qxvCOFD9gsyqCep1kzPwP38z5rBxOp7x9FWAXUeLDPXabGdlHO1j4sqcHPj6pZIMWdo71ExMSTAUyakQKBwOlqcIHjZgaX624%2FnQG%2BvJp2owY8o699MhIK5GgY6ze6n1V%2FPevoPhXo3RhraP81x5d72Frt5qeYHpQpAz83LWpSWAVUqTFZ%2BOWv6s0W5MK0Fj%2BpJ41UCfYDqUBClwIKYS2DBqfpP3uGzCQWqX0qAjfOnTjLMvNFQh7%2B%2BxkXG%2Bhnc8ycEaCmk9D7X2ttcVtlPvIKIjfumpj7MGbQ2%2FTNTI3WrM1%2FPVFfRyfbu61LsopKBS025%2BLhVl3NuQ20xv3Kv4OwOG29m1svD0OPAp9sEFiINtBNsZRZnilLMKVYq%2F%2B5bn%2FyrSpg38dR7dmx6irLEb9we20GPswotZhKeVDCp%2FwU2fqeH8%2F3OWZ%2BgqAk8HRceEiepAJOlwzwD9arAQsB4YQbMC75CH4DojI1EtlKAFkbB9tvWTbqlnFAcHmhEs0oT%2FR8JGZFJh5qtGjHWYP69nKoll0i%2B7%2B6TLThQKMCgBKbE7QbN09ZHvbLPCXZR6AZcmgUgvfkvizrK6YJbUXtAZhwJq8rWTEoH9%2BfeHpllcpPDKFqM1a2CMLmOnL0GOqUBekrM82oTq7griT6foyoWw%2BdM%2F5CRuwPKhJAJ%2FdgY83WCQKPGZ5eKu2sSBfJkg5qcDWImHNqSOl0zHiOWvog6QgNYNSlDFJCAlGAboQZAzvXdZtTPGh9x6t0HzbDvTiwABZWcjM4%2BtzPRMI%2FP%2FGAx4pYCa4kRuIy8nKH%2BV68yR2pvkEvo2r2KBNh3vQdJ9sVMaeo%2F70UdWV2zV%2BGeafexvghgs%2FAl&X-Amz-Signature=1a71275fd0f67b06ae7f2f291e9404afef0cb0df1feeb9b294d58981f25a1f22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXNFKQKS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDTnwey3VIqEw8UTgfod7987Ygi2SAi8xM8zUO6SGz38QIgbZh%2F4Io0zO%2B0cHUbybPAiWwhU4jegNiMTwOa0VR0s%2BgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDX3sHM5%2FP88KWzcMCrcA8SPGtr65Yzw66kboMlhs6OPDNlQ7N8nyqBD2VpRzIXsPO4YcqEuUVFM3WFHaJbchmgahrluNNdaTCKjDyffTKrJvKaRIjptjC7rODhoWTICd%2F2CKx%2F%2B8%2BwPeiFSUrnFKkzFY5APt1lUYkMhpJJ105dwuRLjO%2BYe5KLXBRezXVbzUXrNStwIjPnB9Fd%2FuImwjSL2Ay%2ByjoWRL06e4UZgtmxX6EE213M%2Fmcaof3%2Bb7kLZ%2BpHQnPyYcllGhIPL4715qJrKsntfjuctYKBbqDTodo4pJlVIDTQb4ABHUZxKoEjud33WjuCCoFxmG56CvSZe7rDH1QRPOGD0w7TQvJfqLXXnnduxq7VWFizb4U%2Bqj3KHPejoTV5v1fn2pKgBXQ%2FHAgxbEucuxFBlqT4d3%2B%2Fdd1wrFPXT3eTdQ3fxub%2BmC3XsHg0KoipYli%2B%2FdZ70LZlqDwIoM%2FCy8cM0oT8TkaTATLS9gWil3MWhQGO0sYngtyIcmfzP%2FIz2Td9gzJ9faNZVbWb1%2BvcI4QO3%2BIczAmyAKQr5SXQUiv4gmpk6qHSnVJrEFZcuvOCsGVGrFk0BU9IbvYCO0WJTstc0JS39KZmDmk4Jx1U3PurH%2B7Bum%2BW3EvtI5Dx1y88yWf6WTADeMPeNnL0GOqUB%2F5D0NCoP8XlJm%2B5WtX8xgO8UF7UM0x6NIY6R4RCM6HwDIHDOjgZ4Witk7k85JbMNCA34AykA9a%2BlDPthdGTJpnSFESUkfXvR5FHRt1mAw0m9dJctlsZ%2B%2Bdtw9vAJyUhVtMqoyh5YHILYDhCBP2L%2BIz5AZ8xWP%2F6fVVQafQjAj6JkyyT5FcJ1tI%2F%2FOhFZfakKf3CBsR7l9eKT3RCh6xXD%2F7gQQHS8&X-Amz-Signature=b73df852cb6b377ec7a742f836f5c045527e35f7cd8dcb7d8a9a239b60aca26c&X-Amz-SignedHeaders=host&x-id=GetObject)
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