

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QV3KPHZF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDlrqp%2Bioja8HIfKKMBrDwrcIhcF7mT%2FjglAE37jnT63gIgLXDtysdKl0s9pOeKASuvB7uuaKPur9AAHYmbWPAx3AYq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDLKvrElz9a7lifbvUyrcA%2FkfC1raHPpR25Bby8e%2BqDEutcb2qfqVamTgsSL5e59XjrW9UjwQybhw%2F21cMiZa0939ahWJq1fThBZIYcBQ2slNrP%2FfXE1vqLKkRqLVcCoLqjOn6i%2FT0Ynfw2MyQ29rAHpv9D2KhCPiWvY71xdEJeROJw8nJ0MjCajIMkIAzECu6tVH1u4o5KdRPOZsruXod%2FSoB3RM9Hve4XSAJdB6peqvexee1A7yKXi20gk5flArmXp7lCXTGqyTnlhTebFrne2BFs3K%2FxoNqSyPhZA40yl61KSDGWYMBdoYoBR%2Bxp8Qg7jAqfNBJApEx5NsandnzW1kdCqvtav6lOOYvStAeEOYJEi11vlYhNm5dJMJ9VlDbj%2Bhqp5aP1Vp4nn9I4IuZK%2FsEAf%2BlHOC17ZuulpvOXXFV0yR9TsSu4%2BKiPsin7u2ERAD9PPw%2FlTuRETtJhhAiTYVqgzcE8coWNhhEcjgZztG9z3WuNZUUJQUGQtPNwxMztUlZWWB4BzBY8ffaZEHwqXjHUZuL82Fk40UNVquaEdw2QTzT0P5z5s277TyPi1%2FUeMHhT0W7BGz2QfS%2FsuVdlMQNqkhQPbLpVNeqNJ%2FLQEuEEvjLEL0Yjx6au3Qvk9vpAKgfE3rT4tjI0G2MIP7lr0GOqUBeLRbB5yL8pVIoa%2Fl2Kp9%2BZ4fxKt3yCXkXFqpej9FsxleZ9G2iRK3GyvjTFP3xlII5CS616I6TAg2pbn%2BjXYiljDEeHJXgW952IPo1%2BByLvOlZRoADSHtw69wVHVMaiDyH9pkD2zGve4hbX5zlu6WG%2Faod1CU59pZWvX%2B5HRhwVyFRkULpaOwGPGxJxemRE1zJj09NGDURY%2BZowiCuhT6yvm0OqGV&X-Amz-Signature=1e4fa613fa24d02c8a104ccf2c83a26828b0a6893a6a01429d184f5a4aa279c7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QV3KPHZF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDlrqp%2Bioja8HIfKKMBrDwrcIhcF7mT%2FjglAE37jnT63gIgLXDtysdKl0s9pOeKASuvB7uuaKPur9AAHYmbWPAx3AYq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDLKvrElz9a7lifbvUyrcA%2FkfC1raHPpR25Bby8e%2BqDEutcb2qfqVamTgsSL5e59XjrW9UjwQybhw%2F21cMiZa0939ahWJq1fThBZIYcBQ2slNrP%2FfXE1vqLKkRqLVcCoLqjOn6i%2FT0Ynfw2MyQ29rAHpv9D2KhCPiWvY71xdEJeROJw8nJ0MjCajIMkIAzECu6tVH1u4o5KdRPOZsruXod%2FSoB3RM9Hve4XSAJdB6peqvexee1A7yKXi20gk5flArmXp7lCXTGqyTnlhTebFrne2BFs3K%2FxoNqSyPhZA40yl61KSDGWYMBdoYoBR%2Bxp8Qg7jAqfNBJApEx5NsandnzW1kdCqvtav6lOOYvStAeEOYJEi11vlYhNm5dJMJ9VlDbj%2Bhqp5aP1Vp4nn9I4IuZK%2FsEAf%2BlHOC17ZuulpvOXXFV0yR9TsSu4%2BKiPsin7u2ERAD9PPw%2FlTuRETtJhhAiTYVqgzcE8coWNhhEcjgZztG9z3WuNZUUJQUGQtPNwxMztUlZWWB4BzBY8ffaZEHwqXjHUZuL82Fk40UNVquaEdw2QTzT0P5z5s277TyPi1%2FUeMHhT0W7BGz2QfS%2FsuVdlMQNqkhQPbLpVNeqNJ%2FLQEuEEvjLEL0Yjx6au3Qvk9vpAKgfE3rT4tjI0G2MIP7lr0GOqUBeLRbB5yL8pVIoa%2Fl2Kp9%2BZ4fxKt3yCXkXFqpej9FsxleZ9G2iRK3GyvjTFP3xlII5CS616I6TAg2pbn%2BjXYiljDEeHJXgW952IPo1%2BByLvOlZRoADSHtw69wVHVMaiDyH9pkD2zGve4hbX5zlu6WG%2Faod1CU59pZWvX%2B5HRhwVyFRkULpaOwGPGxJxemRE1zJj09NGDURY%2BZowiCuhT6yvm0OqGV&X-Amz-Signature=23c68cc25caef10bf57a2befb9df6ece634c571baf14d5e7560bf550617bbe2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QV3KPHZF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDlrqp%2Bioja8HIfKKMBrDwrcIhcF7mT%2FjglAE37jnT63gIgLXDtysdKl0s9pOeKASuvB7uuaKPur9AAHYmbWPAx3AYq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDLKvrElz9a7lifbvUyrcA%2FkfC1raHPpR25Bby8e%2BqDEutcb2qfqVamTgsSL5e59XjrW9UjwQybhw%2F21cMiZa0939ahWJq1fThBZIYcBQ2slNrP%2FfXE1vqLKkRqLVcCoLqjOn6i%2FT0Ynfw2MyQ29rAHpv9D2KhCPiWvY71xdEJeROJw8nJ0MjCajIMkIAzECu6tVH1u4o5KdRPOZsruXod%2FSoB3RM9Hve4XSAJdB6peqvexee1A7yKXi20gk5flArmXp7lCXTGqyTnlhTebFrne2BFs3K%2FxoNqSyPhZA40yl61KSDGWYMBdoYoBR%2Bxp8Qg7jAqfNBJApEx5NsandnzW1kdCqvtav6lOOYvStAeEOYJEi11vlYhNm5dJMJ9VlDbj%2Bhqp5aP1Vp4nn9I4IuZK%2FsEAf%2BlHOC17ZuulpvOXXFV0yR9TsSu4%2BKiPsin7u2ERAD9PPw%2FlTuRETtJhhAiTYVqgzcE8coWNhhEcjgZztG9z3WuNZUUJQUGQtPNwxMztUlZWWB4BzBY8ffaZEHwqXjHUZuL82Fk40UNVquaEdw2QTzT0P5z5s277TyPi1%2FUeMHhT0W7BGz2QfS%2FsuVdlMQNqkhQPbLpVNeqNJ%2FLQEuEEvjLEL0Yjx6au3Qvk9vpAKgfE3rT4tjI0G2MIP7lr0GOqUBeLRbB5yL8pVIoa%2Fl2Kp9%2BZ4fxKt3yCXkXFqpej9FsxleZ9G2iRK3GyvjTFP3xlII5CS616I6TAg2pbn%2BjXYiljDEeHJXgW952IPo1%2BByLvOlZRoADSHtw69wVHVMaiDyH9pkD2zGve4hbX5zlu6WG%2Faod1CU59pZWvX%2B5HRhwVyFRkULpaOwGPGxJxemRE1zJj09NGDURY%2BZowiCuhT6yvm0OqGV&X-Amz-Signature=e233eff95392aee422b0cdb417f14edf5a1c023a81530bd1613054ea881b2afc&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCHBQVSB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIEou%2Bd3rMU4Op21eJGttCek94kgGwQgIpr%2BJsy4tjH5QAiAEQm4WW85SHN6IATHxu%2Fc%2BItKbIX%2B69BAGqrnUmlYKnir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMV5qacgU3X9UuB1VNKtwD8e3U1b8xalz6gV80h%2F2y0ZFqlfFnwWHxuzk2QMpKIQe4hugcmvJWct0G2iEXgvKe4gIodLkuaUQE7%2F4E7zuRfAMOBtz8lGhRgwbvVHFz2X%2FOtjh3K2yZ%2FaT1sPKpxc0PD7zXbmIP237pcxyuuQwBf5F5QcsW5WbpOisNjlZ7CuC1ycS1YJ9nqC0HUpNgxuBmLb%2BFnfi04GD2YfYR6IxiZq5YB7G4quVu1oLLN4bMwqGKAM8xhvyTK6SFjEo5qsVW3aKMkUhnLR0U7qAYuUy45Crt2QupMyT%2F8ya%2FybqOSWiW2VIwMuaBCzj%2BhHKd7sZ%2FwbcEhz5EQbD8n1rkoYsgXXZ0S7YPXgAEugnXF5%2F3aT%2BVf2kfXvQjqf1QcxRoBu483km18sdcYmBXkU6Ay%2FI9tl12iduTHQyF0LwrftG%2Bxi1Dw4mMkfCrdiBWKOFszo8%2FTNzeBdIj7%2BvwE81qht5P2dBTJvqTP2oEO2gv%2BMuzj8D1z1vYlLBsS0xoKFSRO9ZQjtsJ3OTcU6V4EFG5pjyscNVvGF9%2F7U1kZU2Af0IoD1eaMjzsMBXf%2Fdlvpxt9TQC4aeu3K7DR5xEX76VXaqBx7La3c8HTO9f7lOQGIBbdzOuLstRCcPUFxM9gTbQwy%2FmWvQY6pgHX0dec25ZKSt7Zw8I0Z20dh5dxek08ptwRu3YB02Whp0bhqFjGoztjnljtA0LbIZJ8SejnbWrdcC9AfIauISxosfRUPqJKLJD189pAXV3eOtKGUTN%2FaKB96gJ8hK0tp7AsBNvxhHitG%2B5ibW2aOIHYVCEy5HL1q5ZbNgRxjLiO0d5qdPKXAIgJBlZjMqork3ulb7LZcnZxJ9Ou0RbS22bdeq%2BLqk%2BL&X-Amz-Signature=bfbd5e45a054f3d5921d3e11b92d8f5068eb6121eee210fb33b4ec7ca8b2a64d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCHBQVSB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIEou%2Bd3rMU4Op21eJGttCek94kgGwQgIpr%2BJsy4tjH5QAiAEQm4WW85SHN6IATHxu%2Fc%2BItKbIX%2B69BAGqrnUmlYKnir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMV5qacgU3X9UuB1VNKtwD8e3U1b8xalz6gV80h%2F2y0ZFqlfFnwWHxuzk2QMpKIQe4hugcmvJWct0G2iEXgvKe4gIodLkuaUQE7%2F4E7zuRfAMOBtz8lGhRgwbvVHFz2X%2FOtjh3K2yZ%2FaT1sPKpxc0PD7zXbmIP237pcxyuuQwBf5F5QcsW5WbpOisNjlZ7CuC1ycS1YJ9nqC0HUpNgxuBmLb%2BFnfi04GD2YfYR6IxiZq5YB7G4quVu1oLLN4bMwqGKAM8xhvyTK6SFjEo5qsVW3aKMkUhnLR0U7qAYuUy45Crt2QupMyT%2F8ya%2FybqOSWiW2VIwMuaBCzj%2BhHKd7sZ%2FwbcEhz5EQbD8n1rkoYsgXXZ0S7YPXgAEugnXF5%2F3aT%2BVf2kfXvQjqf1QcxRoBu483km18sdcYmBXkU6Ay%2FI9tl12iduTHQyF0LwrftG%2Bxi1Dw4mMkfCrdiBWKOFszo8%2FTNzeBdIj7%2BvwE81qht5P2dBTJvqTP2oEO2gv%2BMuzj8D1z1vYlLBsS0xoKFSRO9ZQjtsJ3OTcU6V4EFG5pjyscNVvGF9%2F7U1kZU2Af0IoD1eaMjzsMBXf%2Fdlvpxt9TQC4aeu3K7DR5xEX76VXaqBx7La3c8HTO9f7lOQGIBbdzOuLstRCcPUFxM9gTbQwy%2FmWvQY6pgHX0dec25ZKSt7Zw8I0Z20dh5dxek08ptwRu3YB02Whp0bhqFjGoztjnljtA0LbIZJ8SejnbWrdcC9AfIauISxosfRUPqJKLJD189pAXV3eOtKGUTN%2FaKB96gJ8hK0tp7AsBNvxhHitG%2B5ibW2aOIHYVCEy5HL1q5ZbNgRxjLiO0d5qdPKXAIgJBlZjMqork3ulb7LZcnZxJ9Ou0RbS22bdeq%2BLqk%2BL&X-Amz-Signature=44232256e67512100a6f07ee8303fe2c7864d69e78367ca2bdb257210f0146b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QV3KPHZF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDlrqp%2Bioja8HIfKKMBrDwrcIhcF7mT%2FjglAE37jnT63gIgLXDtysdKl0s9pOeKASuvB7uuaKPur9AAHYmbWPAx3AYq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDLKvrElz9a7lifbvUyrcA%2FkfC1raHPpR25Bby8e%2BqDEutcb2qfqVamTgsSL5e59XjrW9UjwQybhw%2F21cMiZa0939ahWJq1fThBZIYcBQ2slNrP%2FfXE1vqLKkRqLVcCoLqjOn6i%2FT0Ynfw2MyQ29rAHpv9D2KhCPiWvY71xdEJeROJw8nJ0MjCajIMkIAzECu6tVH1u4o5KdRPOZsruXod%2FSoB3RM9Hve4XSAJdB6peqvexee1A7yKXi20gk5flArmXp7lCXTGqyTnlhTebFrne2BFs3K%2FxoNqSyPhZA40yl61KSDGWYMBdoYoBR%2Bxp8Qg7jAqfNBJApEx5NsandnzW1kdCqvtav6lOOYvStAeEOYJEi11vlYhNm5dJMJ9VlDbj%2Bhqp5aP1Vp4nn9I4IuZK%2FsEAf%2BlHOC17ZuulpvOXXFV0yR9TsSu4%2BKiPsin7u2ERAD9PPw%2FlTuRETtJhhAiTYVqgzcE8coWNhhEcjgZztG9z3WuNZUUJQUGQtPNwxMztUlZWWB4BzBY8ffaZEHwqXjHUZuL82Fk40UNVquaEdw2QTzT0P5z5s277TyPi1%2FUeMHhT0W7BGz2QfS%2FsuVdlMQNqkhQPbLpVNeqNJ%2FLQEuEEvjLEL0Yjx6au3Qvk9vpAKgfE3rT4tjI0G2MIP7lr0GOqUBeLRbB5yL8pVIoa%2Fl2Kp9%2BZ4fxKt3yCXkXFqpej9FsxleZ9G2iRK3GyvjTFP3xlII5CS616I6TAg2pbn%2BjXYiljDEeHJXgW952IPo1%2BByLvOlZRoADSHtw69wVHVMaiDyH9pkD2zGve4hbX5zlu6WG%2Faod1CU59pZWvX%2B5HRhwVyFRkULpaOwGPGxJxemRE1zJj09NGDURY%2BZowiCuhT6yvm0OqGV&X-Amz-Signature=299cc369b40c119586c33ff98596d378d3898946ea39f5939ffa6900320b635c&X-Amz-SignedHeaders=host&x-id=GetObject)
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