

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ4WNCDT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIHCoB1fUbySCWuQMBa4PAJOPb7GrLfOsMksKK%2B0j8A%2BKAiEAmfIdR0DieueiJOU7%2BBU54gg7XgPiydRyaa7%2FQZsrj%2Fkq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDIfnZNomm5mHHy9tlyrcA6qJv8z3hGXaGCljXZmnlV2KqBkJWGsX12nMWVG%2FSi53qJl7jeEul8BBtbg48F5QLAUVZQCbWWD2wCms46baBj972WkfSJnE5Ogn1gCm9Xkhbr0wYceQV2bMngY9H%2Be93HQso7eSYnpCWMeit1HnlChlq7qE%2BF0g82iTeSslX2ocZXyX2AXnb9tHjSbWbK1YRlFcuKPVaubR%2B8yv%2BGeO6BeHUwFsjwmNnrZX2AFRgZs88zjcelaZ%2BWVPhqFZ5k8ppHcAUR7y6PedAvIcaoFrIftt5dr069zFOd39Eg19jZ%2ByJvDm9ku5GlATvVJaTFHrrFyXsh2G06JYfc%2F04JM00zBas1Dvw1kgbT3eKbouXGrOEdG9dEOwp3MuKpASMY6uta%2FVzaVMGNswPrQd241ieWE0MlMZD%2BtbIOcPiEJLJXqCRuJsldZkPAH%2BIgVsKTf7UydaXqhfapIkfteV5QHrTnPxXm6VQzyiJUqpYXcVBxYj6RDWDPS1z8xKfO%2BBC00F2aw4CfNxUAzXtIRKET2%2F2CPpPwvEOXtc48IN%2FmrwGR6DD8tGfx4xmabs4wSF%2F9qlUt2XjsQbKqE0rMuNOzJDUvq84bYCi3MmLZt6eq2O6lH3269QHtjKaWxFcwRlMO3di70GOqUBOUta5o7mJnec9AmL4le%2FdWl6Xsw4kXA6GwuhUXGoBYU%2BEVxXVQbpzIB4sPI%2Byq6qhSunw7lf71cuxwbAgW7Znui27oMiKzQ%2FOlPIpjOq2OWWp3tZi%2FeOEWocy0CoIXJOYwK7jDyXVbdnEZokPH68V9pnB%2BdaHjwrh1Tc6y2qURHr9r%2B9KIqrhE%2BmLO22%2Bg96BZ7l72MrVgzG4QM99GAJdE2XAc7T&X-Amz-Signature=4386bce93d00e7883e308ecc6fdf333f1766605f9500b3cef05f50c1ab80c847&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ4WNCDT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIHCoB1fUbySCWuQMBa4PAJOPb7GrLfOsMksKK%2B0j8A%2BKAiEAmfIdR0DieueiJOU7%2BBU54gg7XgPiydRyaa7%2FQZsrj%2Fkq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDIfnZNomm5mHHy9tlyrcA6qJv8z3hGXaGCljXZmnlV2KqBkJWGsX12nMWVG%2FSi53qJl7jeEul8BBtbg48F5QLAUVZQCbWWD2wCms46baBj972WkfSJnE5Ogn1gCm9Xkhbr0wYceQV2bMngY9H%2Be93HQso7eSYnpCWMeit1HnlChlq7qE%2BF0g82iTeSslX2ocZXyX2AXnb9tHjSbWbK1YRlFcuKPVaubR%2B8yv%2BGeO6BeHUwFsjwmNnrZX2AFRgZs88zjcelaZ%2BWVPhqFZ5k8ppHcAUR7y6PedAvIcaoFrIftt5dr069zFOd39Eg19jZ%2ByJvDm9ku5GlATvVJaTFHrrFyXsh2G06JYfc%2F04JM00zBas1Dvw1kgbT3eKbouXGrOEdG9dEOwp3MuKpASMY6uta%2FVzaVMGNswPrQd241ieWE0MlMZD%2BtbIOcPiEJLJXqCRuJsldZkPAH%2BIgVsKTf7UydaXqhfapIkfteV5QHrTnPxXm6VQzyiJUqpYXcVBxYj6RDWDPS1z8xKfO%2BBC00F2aw4CfNxUAzXtIRKET2%2F2CPpPwvEOXtc48IN%2FmrwGR6DD8tGfx4xmabs4wSF%2F9qlUt2XjsQbKqE0rMuNOzJDUvq84bYCi3MmLZt6eq2O6lH3269QHtjKaWxFcwRlMO3di70GOqUBOUta5o7mJnec9AmL4le%2FdWl6Xsw4kXA6GwuhUXGoBYU%2BEVxXVQbpzIB4sPI%2Byq6qhSunw7lf71cuxwbAgW7Znui27oMiKzQ%2FOlPIpjOq2OWWp3tZi%2FeOEWocy0CoIXJOYwK7jDyXVbdnEZokPH68V9pnB%2BdaHjwrh1Tc6y2qURHr9r%2B9KIqrhE%2BmLO22%2Bg96BZ7l72MrVgzG4QM99GAJdE2XAc7T&X-Amz-Signature=548293bf788d96b7d7ccf7d5602404a27921f19f930fc9089bf756079e7626d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ4WNCDT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIHCoB1fUbySCWuQMBa4PAJOPb7GrLfOsMksKK%2B0j8A%2BKAiEAmfIdR0DieueiJOU7%2BBU54gg7XgPiydRyaa7%2FQZsrj%2Fkq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDIfnZNomm5mHHy9tlyrcA6qJv8z3hGXaGCljXZmnlV2KqBkJWGsX12nMWVG%2FSi53qJl7jeEul8BBtbg48F5QLAUVZQCbWWD2wCms46baBj972WkfSJnE5Ogn1gCm9Xkhbr0wYceQV2bMngY9H%2Be93HQso7eSYnpCWMeit1HnlChlq7qE%2BF0g82iTeSslX2ocZXyX2AXnb9tHjSbWbK1YRlFcuKPVaubR%2B8yv%2BGeO6BeHUwFsjwmNnrZX2AFRgZs88zjcelaZ%2BWVPhqFZ5k8ppHcAUR7y6PedAvIcaoFrIftt5dr069zFOd39Eg19jZ%2ByJvDm9ku5GlATvVJaTFHrrFyXsh2G06JYfc%2F04JM00zBas1Dvw1kgbT3eKbouXGrOEdG9dEOwp3MuKpASMY6uta%2FVzaVMGNswPrQd241ieWE0MlMZD%2BtbIOcPiEJLJXqCRuJsldZkPAH%2BIgVsKTf7UydaXqhfapIkfteV5QHrTnPxXm6VQzyiJUqpYXcVBxYj6RDWDPS1z8xKfO%2BBC00F2aw4CfNxUAzXtIRKET2%2F2CPpPwvEOXtc48IN%2FmrwGR6DD8tGfx4xmabs4wSF%2F9qlUt2XjsQbKqE0rMuNOzJDUvq84bYCi3MmLZt6eq2O6lH3269QHtjKaWxFcwRlMO3di70GOqUBOUta5o7mJnec9AmL4le%2FdWl6Xsw4kXA6GwuhUXGoBYU%2BEVxXVQbpzIB4sPI%2Byq6qhSunw7lf71cuxwbAgW7Znui27oMiKzQ%2FOlPIpjOq2OWWp3tZi%2FeOEWocy0CoIXJOYwK7jDyXVbdnEZokPH68V9pnB%2BdaHjwrh1Tc6y2qURHr9r%2B9KIqrhE%2BmLO22%2Bg96BZ7l72MrVgzG4QM99GAJdE2XAc7T&X-Amz-Signature=0472bde3a8116f5ee1480bd49826dcf6e84629dd74b49bff8a2e676514e2dedb&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656ROR5KP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIDBXO4nhuWVWQxCGPMvd8L%2BNYa%2FJFdf7pBgKWcphCyh1AiBbwMddYrEvIlm14dvthgSxByffwFYThTUIDh%2Fe3v29cCr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMaCAlL0j7FRxtQQfaKtwD4xMApcxDZNjC0W6kqIxwvNS1omYZSY%2B4n6EhJVDC0fhQTmoFruZ1Yq7mBZRlsADvJN8NQiCtEL6RhN4gy05QkXvqPWBbXSJq9aX2JqSpOXlqdw6X2r2O1VvwOt4eE%2FzdIhUjRKWNrAfXqKrFsNEBA7ida2aFLhYYl62LI5Z8N9e7883eygMkeWMC7H0F9sZ4TTjnqDT5Ao9OkEhqPSfrBNUgEV0hEcbpMmq4peZP11Yjvzl6h9kIO%2BbhLYhLK0g7eAnzK%2Fu4UxjIGCMp6tEWf8%2BD8MjKTKrHp%2FAGf%2BUqp%2F%2F4fjHszNDxlu0aO%2B3qKd%2BYrYKK4%2FZiUXCEV3ZZqvcXDLHPrVERjYj%2BtaXHgalyjoFvhAa56tj1GyLOn8LUg5ss05qYE6QqqPW4ptOyU4mSpOXZzb8XnoxsT%2BI27EcthIt%2FDTCfC813MQgwsEIIGc95yYBC%2Fxr1RNUf5IVAPZUwjFvnnQLhm1k0NWk%2B91IomRMzwqPNlhrB2zalEDcu98g3C9jNZ2zbecbx3cCh2fvHcBlODI963GPhj0zMjRkN75aEDEoOaC0kGqWfOsVhXSrB%2Fd6DOMb8u4XKCQwPYxBsEYWCw9hVo7LMd9B6FMTVLD%2BSNjXW44H%2B%2BkJ%2BDUwwt92LvQY6pgFWzZ7rGnIxrYVHS0zp256HbzIbRyAjlq%2F144I%2FWPxBUu%2BJjwc5ZdngeF64YSP7Q9a%2FyPktMkx1F4nm8I0%2B6DMKZ131%2FeTA276TKm0eNDXAA7dUu87O9fdLG2TNqV9bOgeu0RZY2dr8hStb5N8xjrb%2BGh%2BnA7XVK0tr7tEdHzDoCOweiC8OaePNvRQAqLlDQiURXAoO4mchZiSGTv953w5keiVWjwsW&X-Amz-Signature=35d735cf955f1f9e6068bba6a2a93aa5451bf0e8b79e459ae41d4addbd59c7ea&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656ROR5KP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIDBXO4nhuWVWQxCGPMvd8L%2BNYa%2FJFdf7pBgKWcphCyh1AiBbwMddYrEvIlm14dvthgSxByffwFYThTUIDh%2Fe3v29cCr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMaCAlL0j7FRxtQQfaKtwD4xMApcxDZNjC0W6kqIxwvNS1omYZSY%2B4n6EhJVDC0fhQTmoFruZ1Yq7mBZRlsADvJN8NQiCtEL6RhN4gy05QkXvqPWBbXSJq9aX2JqSpOXlqdw6X2r2O1VvwOt4eE%2FzdIhUjRKWNrAfXqKrFsNEBA7ida2aFLhYYl62LI5Z8N9e7883eygMkeWMC7H0F9sZ4TTjnqDT5Ao9OkEhqPSfrBNUgEV0hEcbpMmq4peZP11Yjvzl6h9kIO%2BbhLYhLK0g7eAnzK%2Fu4UxjIGCMp6tEWf8%2BD8MjKTKrHp%2FAGf%2BUqp%2F%2F4fjHszNDxlu0aO%2B3qKd%2BYrYKK4%2FZiUXCEV3ZZqvcXDLHPrVERjYj%2BtaXHgalyjoFvhAa56tj1GyLOn8LUg5ss05qYE6QqqPW4ptOyU4mSpOXZzb8XnoxsT%2BI27EcthIt%2FDTCfC813MQgwsEIIGc95yYBC%2Fxr1RNUf5IVAPZUwjFvnnQLhm1k0NWk%2B91IomRMzwqPNlhrB2zalEDcu98g3C9jNZ2zbecbx3cCh2fvHcBlODI963GPhj0zMjRkN75aEDEoOaC0kGqWfOsVhXSrB%2Fd6DOMb8u4XKCQwPYxBsEYWCw9hVo7LMd9B6FMTVLD%2BSNjXW44H%2B%2BkJ%2BDUwwt92LvQY6pgFWzZ7rGnIxrYVHS0zp256HbzIbRyAjlq%2F144I%2FWPxBUu%2BJjwc5ZdngeF64YSP7Q9a%2FyPktMkx1F4nm8I0%2B6DMKZ131%2FeTA276TKm0eNDXAA7dUu87O9fdLG2TNqV9bOgeu0RZY2dr8hStb5N8xjrb%2BGh%2BnA7XVK0tr7tEdHzDoCOweiC8OaePNvRQAqLlDQiURXAoO4mchZiSGTv953w5keiVWjwsW&X-Amz-Signature=8eec879cc38e90dcf7fd0ff9c228b9c6682ef761d601dec99de294a0e1ed5874&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ4WNCDT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIHCoB1fUbySCWuQMBa4PAJOPb7GrLfOsMksKK%2B0j8A%2BKAiEAmfIdR0DieueiJOU7%2BBU54gg7XgPiydRyaa7%2FQZsrj%2Fkq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDIfnZNomm5mHHy9tlyrcA6qJv8z3hGXaGCljXZmnlV2KqBkJWGsX12nMWVG%2FSi53qJl7jeEul8BBtbg48F5QLAUVZQCbWWD2wCms46baBj972WkfSJnE5Ogn1gCm9Xkhbr0wYceQV2bMngY9H%2Be93HQso7eSYnpCWMeit1HnlChlq7qE%2BF0g82iTeSslX2ocZXyX2AXnb9tHjSbWbK1YRlFcuKPVaubR%2B8yv%2BGeO6BeHUwFsjwmNnrZX2AFRgZs88zjcelaZ%2BWVPhqFZ5k8ppHcAUR7y6PedAvIcaoFrIftt5dr069zFOd39Eg19jZ%2ByJvDm9ku5GlATvVJaTFHrrFyXsh2G06JYfc%2F04JM00zBas1Dvw1kgbT3eKbouXGrOEdG9dEOwp3MuKpASMY6uta%2FVzaVMGNswPrQd241ieWE0MlMZD%2BtbIOcPiEJLJXqCRuJsldZkPAH%2BIgVsKTf7UydaXqhfapIkfteV5QHrTnPxXm6VQzyiJUqpYXcVBxYj6RDWDPS1z8xKfO%2BBC00F2aw4CfNxUAzXtIRKET2%2F2CPpPwvEOXtc48IN%2FmrwGR6DD8tGfx4xmabs4wSF%2F9qlUt2XjsQbKqE0rMuNOzJDUvq84bYCi3MmLZt6eq2O6lH3269QHtjKaWxFcwRlMO3di70GOqUBOUta5o7mJnec9AmL4le%2FdWl6Xsw4kXA6GwuhUXGoBYU%2BEVxXVQbpzIB4sPI%2Byq6qhSunw7lf71cuxwbAgW7Znui27oMiKzQ%2FOlPIpjOq2OWWp3tZi%2FeOEWocy0CoIXJOYwK7jDyXVbdnEZokPH68V9pnB%2BdaHjwrh1Tc6y2qURHr9r%2B9KIqrhE%2BmLO22%2Bg96BZ7l72MrVgzG4QM99GAJdE2XAc7T&X-Amz-Signature=52f28b13494846589e8c250a2a259dffbb57fc38d57f68320c67ffb2ee5b738d&X-Amz-SignedHeaders=host&x-id=GetObject)
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