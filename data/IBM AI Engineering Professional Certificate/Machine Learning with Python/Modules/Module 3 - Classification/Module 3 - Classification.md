

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFSXGVIB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIDeV4g3B2BEEaahUDh%2B1aM8aG6uzHhlDiw4qUyCMpa3iAiEA0An53Tj72n89gB3JjAxJzskThN68rP5Liufw732O6qoq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPaLcogmkw7XPkV5MircA%2B1Un91OhgA3dNwip%2BRlqNjd6gnDQGIB3gXnwI0fX0Z%2FJz7%2B3irOyPZIyGRn6YW00cf6QXdp6PwteDaKeqoTS3mbRqKNPUV0KPDfdCQUBJ9tqj9FNk6dzY35nJTPQ6KicMVEdEthCPhY9Ce5ttBesvC%2FVrqEjeeb21fQodylpsj0Kn%2Fjhmnkcx2nROYPaFGI4xyc9UfXDagHU3UtfbGmXTRDGRh0xOr5at6CHpTbJ8sdRofgvMttJqLsAcShOqkxRzlmJk9Qr6geKWisu3I%2F4SEEqt0Gc4hjzCpEDvl0H4ezYpMWEovuQrOaEWFnwBWvT7GLkN7dx5emrpZUeOhYTQGZmciJMsOQpH6Gl44saOuIRXjUmih7W4cEWN3NTFY0S6ce6bzT1Giil0EKuGun7wYxmF7AG8oNPgqN6ubkj4vZ5hazv60LRAEPmcTu9euwgyDvJbOBsqWHcm4JABnGvv3Dhj8BSikhARgkh9IhGYR7YKcwJpDGpSEJnBd%2BR5iRyeldaylGfXXhhQ6pHarEdHOtRgUlKABEtS5UOBqTGi0JN%2FzoKga8YxiEkVZCHjJ1%2BV8BsEDOluIvS0kEvUUQB%2BxIyJV6Hy%2Fd%2BEOkQsbEIe5BOwP5%2FqRi5VpQ7QWsMO%2BUir0GOqUBKrC7iHql%2FF11wshhO9KXrXKKGFB0K8c5v1zDsLl8WkCA%2F%2FdWGFQPVZdc6xy2Tnme0LttjvQzyU0%2FfnA6Nb2kWG%2FEBb1v%2FLxiJqm5cGj1O8tgCNuh%2BoOZJEGnZ%2BhGUWYObAT3ab1oZXzMlhX7DEShozW9zXBkgKfAqnacG32mvfDB1DTtP4XYN4DuZ3oSfsJ2ii5FqnohPx8Gv4caxIGux8dEwmt7&X-Amz-Signature=0390cf6cf450a8e464270795a47276ca3ed3d33f264966d9e44d694fdd5bb9f6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFSXGVIB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIDeV4g3B2BEEaahUDh%2B1aM8aG6uzHhlDiw4qUyCMpa3iAiEA0An53Tj72n89gB3JjAxJzskThN68rP5Liufw732O6qoq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPaLcogmkw7XPkV5MircA%2B1Un91OhgA3dNwip%2BRlqNjd6gnDQGIB3gXnwI0fX0Z%2FJz7%2B3irOyPZIyGRn6YW00cf6QXdp6PwteDaKeqoTS3mbRqKNPUV0KPDfdCQUBJ9tqj9FNk6dzY35nJTPQ6KicMVEdEthCPhY9Ce5ttBesvC%2FVrqEjeeb21fQodylpsj0Kn%2Fjhmnkcx2nROYPaFGI4xyc9UfXDagHU3UtfbGmXTRDGRh0xOr5at6CHpTbJ8sdRofgvMttJqLsAcShOqkxRzlmJk9Qr6geKWisu3I%2F4SEEqt0Gc4hjzCpEDvl0H4ezYpMWEovuQrOaEWFnwBWvT7GLkN7dx5emrpZUeOhYTQGZmciJMsOQpH6Gl44saOuIRXjUmih7W4cEWN3NTFY0S6ce6bzT1Giil0EKuGun7wYxmF7AG8oNPgqN6ubkj4vZ5hazv60LRAEPmcTu9euwgyDvJbOBsqWHcm4JABnGvv3Dhj8BSikhARgkh9IhGYR7YKcwJpDGpSEJnBd%2BR5iRyeldaylGfXXhhQ6pHarEdHOtRgUlKABEtS5UOBqTGi0JN%2FzoKga8YxiEkVZCHjJ1%2BV8BsEDOluIvS0kEvUUQB%2BxIyJV6Hy%2Fd%2BEOkQsbEIe5BOwP5%2FqRi5VpQ7QWsMO%2BUir0GOqUBKrC7iHql%2FF11wshhO9KXrXKKGFB0K8c5v1zDsLl8WkCA%2F%2FdWGFQPVZdc6xy2Tnme0LttjvQzyU0%2FfnA6Nb2kWG%2FEBb1v%2FLxiJqm5cGj1O8tgCNuh%2BoOZJEGnZ%2BhGUWYObAT3ab1oZXzMlhX7DEShozW9zXBkgKfAqnacG32mvfDB1DTtP4XYN4DuZ3oSfsJ2ii5FqnohPx8Gv4caxIGux8dEwmt7&X-Amz-Signature=566fc7b01bcca0a6116533ebbdbbcb370e1c76fac04c6544c472f291350ffac8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFSXGVIB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIDeV4g3B2BEEaahUDh%2B1aM8aG6uzHhlDiw4qUyCMpa3iAiEA0An53Tj72n89gB3JjAxJzskThN68rP5Liufw732O6qoq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPaLcogmkw7XPkV5MircA%2B1Un91OhgA3dNwip%2BRlqNjd6gnDQGIB3gXnwI0fX0Z%2FJz7%2B3irOyPZIyGRn6YW00cf6QXdp6PwteDaKeqoTS3mbRqKNPUV0KPDfdCQUBJ9tqj9FNk6dzY35nJTPQ6KicMVEdEthCPhY9Ce5ttBesvC%2FVrqEjeeb21fQodylpsj0Kn%2Fjhmnkcx2nROYPaFGI4xyc9UfXDagHU3UtfbGmXTRDGRh0xOr5at6CHpTbJ8sdRofgvMttJqLsAcShOqkxRzlmJk9Qr6geKWisu3I%2F4SEEqt0Gc4hjzCpEDvl0H4ezYpMWEovuQrOaEWFnwBWvT7GLkN7dx5emrpZUeOhYTQGZmciJMsOQpH6Gl44saOuIRXjUmih7W4cEWN3NTFY0S6ce6bzT1Giil0EKuGun7wYxmF7AG8oNPgqN6ubkj4vZ5hazv60LRAEPmcTu9euwgyDvJbOBsqWHcm4JABnGvv3Dhj8BSikhARgkh9IhGYR7YKcwJpDGpSEJnBd%2BR5iRyeldaylGfXXhhQ6pHarEdHOtRgUlKABEtS5UOBqTGi0JN%2FzoKga8YxiEkVZCHjJ1%2BV8BsEDOluIvS0kEvUUQB%2BxIyJV6Hy%2Fd%2BEOkQsbEIe5BOwP5%2FqRi5VpQ7QWsMO%2BUir0GOqUBKrC7iHql%2FF11wshhO9KXrXKKGFB0K8c5v1zDsLl8WkCA%2F%2FdWGFQPVZdc6xy2Tnme0LttjvQzyU0%2FfnA6Nb2kWG%2FEBb1v%2FLxiJqm5cGj1O8tgCNuh%2BoOZJEGnZ%2BhGUWYObAT3ab1oZXzMlhX7DEShozW9zXBkgKfAqnacG32mvfDB1DTtP4XYN4DuZ3oSfsJ2ii5FqnohPx8Gv4caxIGux8dEwmt7&X-Amz-Signature=776bb10a368b3d006b0097a5ec60134ed0731a089d2ba20023a18cc7f49b5346&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DILMJVY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIFmP3W%2BT4pSJ5HZT6Nd25f5XE%2B3UfxbSL9bh8dF%2FYxEsAiAH0Acx74IParigbZaNkRmmL8EbWpgC0solBvSzwUMthyr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMt9RYY%2BVSIYLEIeD8KtwDTaOrYnBiWuv0S0v2xSqvjWA%2FJg%2BJrvddEP67FL1wj6fkGvHLE1Myr493ZZjQWpkRm34qsOCzZJ%2FlregdDqs7%2Fa3V4oA5E94nuovTAyaHaeYymS%2FgX3J%2BmwBobgT%2BxwEuExCPJugLxQkmcQapTZHO4qtDozBQWkmpW8uNFnnfHEfSMU645BBcopvMcEzT%2Fc27r9lKDiQNgJ7n6fV%2FbhSeawQpXaC3hv3KcGd2e6FdhsKrBdURnJovP3tjEkc%2F%2FzoWeWIQiBjYPqs1w%2FaJSoUXbS9%2FNQ8MMmxPkXvYLoTjgZMOzZ9Z7he%2FSM%2FiSkzFN%2F3VojT9JPm0j2kU63R25jAOA35YCag0xRajv4s0Mphn04uhWZ3qpwOvjxfvaf03nm2HLolhaDvSvDlwb2MIuHe0ckINt3dfbCZdg3Ss8DLGoBM5z%2BTzLj1kY5EbQnNEVIH4rooP2H%2FkW43MLNTPQKnAwE0fmc8D%2Fw88Ojw5LhM8WOu5GJ%2BxOZsopAIjtGLrldHhOYLt9JZxULyGZ14TCyRQFLhr2pHJmxNZtk7wx%2BjYdDuZku7l8u4gL91seuWLBdpiAz4HLWh1e5emRSLngHuecCYMWiCYQeG1YIiaIIEXqkMDlvLkURwv%2BxC%2BYugwnZSKvQY6pgH8n1SA5%2FzdmdjLCQxnCFZgHzhv0WKz5O8trdiAGm3YUz1fFKau10Rw5xg18%2FMJFrh7w%2Fkp7HQgZD5XS3p6Mt2V74KhdADjd0abiE6vOFC3v6yTzY%2FL2JU3pX2Y28kXtCPcvAEUS7O%2BnOYcUp7jWPDBhzDmO4sKJpf7IBn3iwuhARAKrzjTpnK%2F4jBYUTyPuQ%2Bh0sUBqjHd7j02cggCVy3pvIMLLKsC&X-Amz-Signature=3e0777b9cc53e70f01014d43ae1a0e1bcd8ba5545ccf59ece34c15f7b490078e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DILMJVY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIFmP3W%2BT4pSJ5HZT6Nd25f5XE%2B3UfxbSL9bh8dF%2FYxEsAiAH0Acx74IParigbZaNkRmmL8EbWpgC0solBvSzwUMthyr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMt9RYY%2BVSIYLEIeD8KtwDTaOrYnBiWuv0S0v2xSqvjWA%2FJg%2BJrvddEP67FL1wj6fkGvHLE1Myr493ZZjQWpkRm34qsOCzZJ%2FlregdDqs7%2Fa3V4oA5E94nuovTAyaHaeYymS%2FgX3J%2BmwBobgT%2BxwEuExCPJugLxQkmcQapTZHO4qtDozBQWkmpW8uNFnnfHEfSMU645BBcopvMcEzT%2Fc27r9lKDiQNgJ7n6fV%2FbhSeawQpXaC3hv3KcGd2e6FdhsKrBdURnJovP3tjEkc%2F%2FzoWeWIQiBjYPqs1w%2FaJSoUXbS9%2FNQ8MMmxPkXvYLoTjgZMOzZ9Z7he%2FSM%2FiSkzFN%2F3VojT9JPm0j2kU63R25jAOA35YCag0xRajv4s0Mphn04uhWZ3qpwOvjxfvaf03nm2HLolhaDvSvDlwb2MIuHe0ckINt3dfbCZdg3Ss8DLGoBM5z%2BTzLj1kY5EbQnNEVIH4rooP2H%2FkW43MLNTPQKnAwE0fmc8D%2Fw88Ojw5LhM8WOu5GJ%2BxOZsopAIjtGLrldHhOYLt9JZxULyGZ14TCyRQFLhr2pHJmxNZtk7wx%2BjYdDuZku7l8u4gL91seuWLBdpiAz4HLWh1e5emRSLngHuecCYMWiCYQeG1YIiaIIEXqkMDlvLkURwv%2BxC%2BYugwnZSKvQY6pgH8n1SA5%2FzdmdjLCQxnCFZgHzhv0WKz5O8trdiAGm3YUz1fFKau10Rw5xg18%2FMJFrh7w%2Fkp7HQgZD5XS3p6Mt2V74KhdADjd0abiE6vOFC3v6yTzY%2FL2JU3pX2Y28kXtCPcvAEUS7O%2BnOYcUp7jWPDBhzDmO4sKJpf7IBn3iwuhARAKrzjTpnK%2F4jBYUTyPuQ%2Bh0sUBqjHd7j02cggCVy3pvIMLLKsC&X-Amz-Signature=1df5e68d91b567ef9fbcc96fa6a6c8221483759457837215749f05023f436853&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFSXGVIB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIDeV4g3B2BEEaahUDh%2B1aM8aG6uzHhlDiw4qUyCMpa3iAiEA0An53Tj72n89gB3JjAxJzskThN68rP5Liufw732O6qoq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDPaLcogmkw7XPkV5MircA%2B1Un91OhgA3dNwip%2BRlqNjd6gnDQGIB3gXnwI0fX0Z%2FJz7%2B3irOyPZIyGRn6YW00cf6QXdp6PwteDaKeqoTS3mbRqKNPUV0KPDfdCQUBJ9tqj9FNk6dzY35nJTPQ6KicMVEdEthCPhY9Ce5ttBesvC%2FVrqEjeeb21fQodylpsj0Kn%2Fjhmnkcx2nROYPaFGI4xyc9UfXDagHU3UtfbGmXTRDGRh0xOr5at6CHpTbJ8sdRofgvMttJqLsAcShOqkxRzlmJk9Qr6geKWisu3I%2F4SEEqt0Gc4hjzCpEDvl0H4ezYpMWEovuQrOaEWFnwBWvT7GLkN7dx5emrpZUeOhYTQGZmciJMsOQpH6Gl44saOuIRXjUmih7W4cEWN3NTFY0S6ce6bzT1Giil0EKuGun7wYxmF7AG8oNPgqN6ubkj4vZ5hazv60LRAEPmcTu9euwgyDvJbOBsqWHcm4JABnGvv3Dhj8BSikhARgkh9IhGYR7YKcwJpDGpSEJnBd%2BR5iRyeldaylGfXXhhQ6pHarEdHOtRgUlKABEtS5UOBqTGi0JN%2FzoKga8YxiEkVZCHjJ1%2BV8BsEDOluIvS0kEvUUQB%2BxIyJV6Hy%2Fd%2BEOkQsbEIe5BOwP5%2FqRi5VpQ7QWsMO%2BUir0GOqUBKrC7iHql%2FF11wshhO9KXrXKKGFB0K8c5v1zDsLl8WkCA%2F%2FdWGFQPVZdc6xy2Tnme0LttjvQzyU0%2FfnA6Nb2kWG%2FEBb1v%2FLxiJqm5cGj1O8tgCNuh%2BoOZJEGnZ%2BhGUWYObAT3ab1oZXzMlhX7DEShozW9zXBkgKfAqnacG32mvfDB1DTtP4XYN4DuZ3oSfsJ2ii5FqnohPx8Gv4caxIGux8dEwmt7&X-Amz-Signature=b9d983c4a9c668373991550ec5c8ec72560be864875176228716878fd7e2b002&X-Amz-SignedHeaders=host&x-id=GetObject)
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