

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URKSF56C%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF0J7r2g8TIFULK74aVn%2BK3QIbAtLaLruSTXoE%2BrGPXNAiB25PKuGgvRtZzrKMKTjcm5s%2B%2B4VEelqo3iFiGG7%2FGGDir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMwe0nMC5FVzEqIkncKtwD%2BN5Ik5TNz1f%2F6s6vTtE3kOebp3G8p7FHC%2F%2Frjr2Zx3r6VsKY4UC%2BZpoC2YPGD7O443eAuxsPy4ECGJm20zdLs2Wroa%2BBuz%2BnDY04L9qUdPZVnk1jwqrDmGnDT5Hant%2FM4cg%2FgeqY8GKoPzaYPAnAXw1%2FT8Y7YclO21cQi0lDvg30PvwWn7yrWw%2FJ5W4%2BKJx9ipKoTY8kRoSQDut9pcixP6zX%2FCm%2B%2F7ghoV9znq3hfAcp9%2FTWyC%2FdumJP6ekbD3ucGjLj0FDv9b6Wf0SplHnOS%2BnvEkXRWFeSZkK6RpsiV5qAqcjNpdTfkmT7Nxyjg8IYNcAIEAi098Fn5XgIl8G8ONNDjOKTYnlyeKfF7%2BSSdJ0yAj9a0NpTtFZEQAWL3ZDVqV1r3ToI1pibAefyXZ4BqOIPx%2Fnm8n9k14Q67SLHy3K6QG7DBTJQXtyrJSbT6OyBtWByRNWy01oviN%2BJTMJWIh2iE4doTAWoy0LYT9i6kOfny6Vu9Nb7sbrNcW88k7tojUPIOa%2FibK%2FMRLNNBuOHlA6zVOfQRZpqfNfKKe9EfysjWsHxAt%2B%2BfdJUnaL5%2BU1fQJ5uO0vAz6IX%2BlP7XE1nW%2BYNW4awrp8gknp%2BcLXFPzA5Dr28FbiXjuWQIQgw2%2BqPvQY6pgGCIvdV5Z4w47m4%2FzK7PDj3ktDiLvIzwYmedW83AxINhCaak%2Bc9%2FwvlNpJAufV995fcuBxH46g2yjJmeJAAW%2FUmE6pWsJs46zD0TZJ0OkXoGEYKRei5Dq9uCwD5gKZeOSi7%2FTysn6NrW8Ek1%2Bb6IjUt56LKx3yD9wGF4LZuJK5xtvepUuPNgULGXyIgSA02B5Za21akRLHzL%2BCAezXrcZA%2Fhzo5orwq&X-Amz-Signature=b6094a49e9a000204dca9aca81a4a0d63b74efa3f99242c245d9ebc403f80fc6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URKSF56C%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF0J7r2g8TIFULK74aVn%2BK3QIbAtLaLruSTXoE%2BrGPXNAiB25PKuGgvRtZzrKMKTjcm5s%2B%2B4VEelqo3iFiGG7%2FGGDir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMwe0nMC5FVzEqIkncKtwD%2BN5Ik5TNz1f%2F6s6vTtE3kOebp3G8p7FHC%2F%2Frjr2Zx3r6VsKY4UC%2BZpoC2YPGD7O443eAuxsPy4ECGJm20zdLs2Wroa%2BBuz%2BnDY04L9qUdPZVnk1jwqrDmGnDT5Hant%2FM4cg%2FgeqY8GKoPzaYPAnAXw1%2FT8Y7YclO21cQi0lDvg30PvwWn7yrWw%2FJ5W4%2BKJx9ipKoTY8kRoSQDut9pcixP6zX%2FCm%2B%2F7ghoV9znq3hfAcp9%2FTWyC%2FdumJP6ekbD3ucGjLj0FDv9b6Wf0SplHnOS%2BnvEkXRWFeSZkK6RpsiV5qAqcjNpdTfkmT7Nxyjg8IYNcAIEAi098Fn5XgIl8G8ONNDjOKTYnlyeKfF7%2BSSdJ0yAj9a0NpTtFZEQAWL3ZDVqV1r3ToI1pibAefyXZ4BqOIPx%2Fnm8n9k14Q67SLHy3K6QG7DBTJQXtyrJSbT6OyBtWByRNWy01oviN%2BJTMJWIh2iE4doTAWoy0LYT9i6kOfny6Vu9Nb7sbrNcW88k7tojUPIOa%2FibK%2FMRLNNBuOHlA6zVOfQRZpqfNfKKe9EfysjWsHxAt%2B%2BfdJUnaL5%2BU1fQJ5uO0vAz6IX%2BlP7XE1nW%2BYNW4awrp8gknp%2BcLXFPzA5Dr28FbiXjuWQIQgw2%2BqPvQY6pgGCIvdV5Z4w47m4%2FzK7PDj3ktDiLvIzwYmedW83AxINhCaak%2Bc9%2FwvlNpJAufV995fcuBxH46g2yjJmeJAAW%2FUmE6pWsJs46zD0TZJ0OkXoGEYKRei5Dq9uCwD5gKZeOSi7%2FTysn6NrW8Ek1%2Bb6IjUt56LKx3yD9wGF4LZuJK5xtvepUuPNgULGXyIgSA02B5Za21akRLHzL%2BCAezXrcZA%2Fhzo5orwq&X-Amz-Signature=8b2def5bd459ef36e786ed9d6f96c4670fa45c017b5c395c328d9a00afd84ce3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URKSF56C%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF0J7r2g8TIFULK74aVn%2BK3QIbAtLaLruSTXoE%2BrGPXNAiB25PKuGgvRtZzrKMKTjcm5s%2B%2B4VEelqo3iFiGG7%2FGGDir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMwe0nMC5FVzEqIkncKtwD%2BN5Ik5TNz1f%2F6s6vTtE3kOebp3G8p7FHC%2F%2Frjr2Zx3r6VsKY4UC%2BZpoC2YPGD7O443eAuxsPy4ECGJm20zdLs2Wroa%2BBuz%2BnDY04L9qUdPZVnk1jwqrDmGnDT5Hant%2FM4cg%2FgeqY8GKoPzaYPAnAXw1%2FT8Y7YclO21cQi0lDvg30PvwWn7yrWw%2FJ5W4%2BKJx9ipKoTY8kRoSQDut9pcixP6zX%2FCm%2B%2F7ghoV9znq3hfAcp9%2FTWyC%2FdumJP6ekbD3ucGjLj0FDv9b6Wf0SplHnOS%2BnvEkXRWFeSZkK6RpsiV5qAqcjNpdTfkmT7Nxyjg8IYNcAIEAi098Fn5XgIl8G8ONNDjOKTYnlyeKfF7%2BSSdJ0yAj9a0NpTtFZEQAWL3ZDVqV1r3ToI1pibAefyXZ4BqOIPx%2Fnm8n9k14Q67SLHy3K6QG7DBTJQXtyrJSbT6OyBtWByRNWy01oviN%2BJTMJWIh2iE4doTAWoy0LYT9i6kOfny6Vu9Nb7sbrNcW88k7tojUPIOa%2FibK%2FMRLNNBuOHlA6zVOfQRZpqfNfKKe9EfysjWsHxAt%2B%2BfdJUnaL5%2BU1fQJ5uO0vAz6IX%2BlP7XE1nW%2BYNW4awrp8gknp%2BcLXFPzA5Dr28FbiXjuWQIQgw2%2BqPvQY6pgGCIvdV5Z4w47m4%2FzK7PDj3ktDiLvIzwYmedW83AxINhCaak%2Bc9%2FwvlNpJAufV995fcuBxH46g2yjJmeJAAW%2FUmE6pWsJs46zD0TZJ0OkXoGEYKRei5Dq9uCwD5gKZeOSi7%2FTysn6NrW8Ek1%2Bb6IjUt56LKx3yD9wGF4LZuJK5xtvepUuPNgULGXyIgSA02B5Za21akRLHzL%2BCAezXrcZA%2Fhzo5orwq&X-Amz-Signature=3289de7945c16c0d8926a2af246657d9abaed785496682d669125da5109759a9&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPEU4WB7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBEEa32L%2FQ%2BFKetmN6b8qpMQEbgFOXwJRFGi9Voa9rToAiEA10USoX2aFO41Kxby1cDBNIbaaNOqDS5lp3hNBkhwPY8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMPCzEb3KZDHEBRuySrcA2PG3isUGXgoQHzCEHody%2FD10N3CbH3bJg2kZ%2F%2FJ%2FC7rjvDZ47P1hh%2Bw6Rj1jqe6%2FpZ5JEThbAt4tH4PbFcrq9j%2FjD6qUS75F1AvgsmtJDC2i5xtQsQcJ7Wwkfocp5zyEOsA3rPakSwlvWtYviRDz957eMgBUwaH8NBhLkIXGQ2%2FXo4EzStwLFX8vd%2BA7tc3gRKxfRLNK1U3scZBbUN1kYA4jySNQg9bx1TDXjNS9kAkEgS%2BdHHxQF76WJjgnQ3fhtl1kjdvNoMhMZj52%2FCa04jJMYpvLXQueqvokageW0qefYfgXW6WDeko%2F19Kuys0mZ2dsdO5UeK6Cv4Idn%2ByrEjmmAfaAf%2B5j1BgwkoVZ5LLnvfl3KQXwzjty%2BOxgTSZM2QXuArLa7XsRr9l9RUJ5zP6ik1gtF7BuMIlD2mRMOUwB2Pq89ChcYLnUR1CDpkjo5PYN4C6xUkLOjpK3VjSffv7k%2BrFSjAFCcjYPN%2FUFRD4mP7PmqQ1u3RRGhgWG%2Fv8dlndvoH7ywcnatWur5d0ymwzo1pxJyyRyxoNgOkdrRSlFtuOYKylwkdaOZ%2Fw7ycgpIEPkRDK%2BQMqfh6uGqUlx6Kkg6zFGE9pEhuTT6uigA%2FXteqPHTOqhsn37%2FciMO7qj70GOqUBqf%2Ft4jDiHvvVix3UuNgadEBnhaLOntSCTep3WrB9w1qxC5SB9YXr6Vo2m4vBMGce%2BQD59UNuMa%2BYBZkis8oYAeW2QVGAVFSnYTIyPQ9yP%2FVqTPMOP%2BS4YR4PcOhH%2F2y%2FqEeI4II0GAgZOzL0tKOWwZPe5q1Zu98c%2BasPL2WhXg9ma1FzkfCkGTklAIrynedRuyyaGb2m21cuovfyl0VjI4KAG%2BCD&X-Amz-Signature=4eba18fd1ea0806ca0af2ad7b568881e1d0d0a67db80dd38318f74089da706fa&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPEU4WB7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIBEEa32L%2FQ%2BFKetmN6b8qpMQEbgFOXwJRFGi9Voa9rToAiEA10USoX2aFO41Kxby1cDBNIbaaNOqDS5lp3hNBkhwPY8q%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDMPCzEb3KZDHEBRuySrcA2PG3isUGXgoQHzCEHody%2FD10N3CbH3bJg2kZ%2F%2FJ%2FC7rjvDZ47P1hh%2Bw6Rj1jqe6%2FpZ5JEThbAt4tH4PbFcrq9j%2FjD6qUS75F1AvgsmtJDC2i5xtQsQcJ7Wwkfocp5zyEOsA3rPakSwlvWtYviRDz957eMgBUwaH8NBhLkIXGQ2%2FXo4EzStwLFX8vd%2BA7tc3gRKxfRLNK1U3scZBbUN1kYA4jySNQg9bx1TDXjNS9kAkEgS%2BdHHxQF76WJjgnQ3fhtl1kjdvNoMhMZj52%2FCa04jJMYpvLXQueqvokageW0qefYfgXW6WDeko%2F19Kuys0mZ2dsdO5UeK6Cv4Idn%2ByrEjmmAfaAf%2B5j1BgwkoVZ5LLnvfl3KQXwzjty%2BOxgTSZM2QXuArLa7XsRr9l9RUJ5zP6ik1gtF7BuMIlD2mRMOUwB2Pq89ChcYLnUR1CDpkjo5PYN4C6xUkLOjpK3VjSffv7k%2BrFSjAFCcjYPN%2FUFRD4mP7PmqQ1u3RRGhgWG%2Fv8dlndvoH7ywcnatWur5d0ymwzo1pxJyyRyxoNgOkdrRSlFtuOYKylwkdaOZ%2Fw7ycgpIEPkRDK%2BQMqfh6uGqUlx6Kkg6zFGE9pEhuTT6uigA%2FXteqPHTOqhsn37%2FciMO7qj70GOqUBqf%2Ft4jDiHvvVix3UuNgadEBnhaLOntSCTep3WrB9w1qxC5SB9YXr6Vo2m4vBMGce%2BQD59UNuMa%2BYBZkis8oYAeW2QVGAVFSnYTIyPQ9yP%2FVqTPMOP%2BS4YR4PcOhH%2F2y%2FqEeI4II0GAgZOzL0tKOWwZPe5q1Zu98c%2BasPL2WhXg9ma1FzkfCkGTklAIrynedRuyyaGb2m21cuovfyl0VjI4KAG%2BCD&X-Amz-Signature=a05a89bddcd477a4461401edea7c8563e1ef98c06b8b757ae19f30702374a036&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URKSF56C%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIF0J7r2g8TIFULK74aVn%2BK3QIbAtLaLruSTXoE%2BrGPXNAiB25PKuGgvRtZzrKMKTjcm5s%2B%2B4VEelqo3iFiGG7%2FGGDir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMwe0nMC5FVzEqIkncKtwD%2BN5Ik5TNz1f%2F6s6vTtE3kOebp3G8p7FHC%2F%2Frjr2Zx3r6VsKY4UC%2BZpoC2YPGD7O443eAuxsPy4ECGJm20zdLs2Wroa%2BBuz%2BnDY04L9qUdPZVnk1jwqrDmGnDT5Hant%2FM4cg%2FgeqY8GKoPzaYPAnAXw1%2FT8Y7YclO21cQi0lDvg30PvwWn7yrWw%2FJ5W4%2BKJx9ipKoTY8kRoSQDut9pcixP6zX%2FCm%2B%2F7ghoV9znq3hfAcp9%2FTWyC%2FdumJP6ekbD3ucGjLj0FDv9b6Wf0SplHnOS%2BnvEkXRWFeSZkK6RpsiV5qAqcjNpdTfkmT7Nxyjg8IYNcAIEAi098Fn5XgIl8G8ONNDjOKTYnlyeKfF7%2BSSdJ0yAj9a0NpTtFZEQAWL3ZDVqV1r3ToI1pibAefyXZ4BqOIPx%2Fnm8n9k14Q67SLHy3K6QG7DBTJQXtyrJSbT6OyBtWByRNWy01oviN%2BJTMJWIh2iE4doTAWoy0LYT9i6kOfny6Vu9Nb7sbrNcW88k7tojUPIOa%2FibK%2FMRLNNBuOHlA6zVOfQRZpqfNfKKe9EfysjWsHxAt%2B%2BfdJUnaL5%2BU1fQJ5uO0vAz6IX%2BlP7XE1nW%2BYNW4awrp8gknp%2BcLXFPzA5Dr28FbiXjuWQIQgw2%2BqPvQY6pgGCIvdV5Z4w47m4%2FzK7PDj3ktDiLvIzwYmedW83AxINhCaak%2Bc9%2FwvlNpJAufV995fcuBxH46g2yjJmeJAAW%2FUmE6pWsJs46zD0TZJ0OkXoGEYKRei5Dq9uCwD5gKZeOSi7%2FTysn6NrW8Ek1%2Bb6IjUt56LKx3yD9wGF4LZuJK5xtvepUuPNgULGXyIgSA02B5Za21akRLHzL%2BCAezXrcZA%2Fhzo5orwq&X-Amz-Signature=ac1ce1215398a8975f0dd1a009ffb8340b253e65b4925624a8f72e9e003b9559&X-Amz-SignedHeaders=host&x-id=GetObject)
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