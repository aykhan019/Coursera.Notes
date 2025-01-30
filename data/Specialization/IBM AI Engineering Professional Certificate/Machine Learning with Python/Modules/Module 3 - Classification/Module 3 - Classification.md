

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466626OWTFT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXSQdY7f1mroKBw6qWTKjcPrV7cQZyvPa0Gz7wzN7IeAiAgMUgc4l0V9206r4J1k%2B9Hv0e0kLBxmnEWydcr9PHkZSqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM70pfIJVBImxTSvJTKtwDigCh%2FFDPgrucg3bzsgYntuyuG%2BKF%2FKgwK3AaEHSu5%2BCZGN9OozQsDEfAt2%2BHYn0WpUPeTLYWvejXtgwoSg09eyv%2ByKNl%2FH0iJK56msS9pRq%2FgUjRfQ%2BmQLLTyGYunTzlmYxRmWOv4%2BVaYMUowRNdm69PKOmjp6hywQ273DTU8LhB8eX7utnjvfQrHGTdN9hXB6Gy67JxYWJn1%2FpJUTF5qYTpmr5KIs%2F0rZJs70djjAoHmqjT%2FGHTEfaWzGaQaPrB0Cpaqc3kjKh0ey8mlzK%2FiAavnVCqQj%2F%2B6Z%2Bj%2BQA%2B7CV6FBaW%2FOlRwNT3QrGnHObAgXSsDTISVQRBDA3zQnL8u3UN3nWVvbRjcUGFXoIuYxunYbTfKXq018IJqKnRKblT4iQLRSi9I%2BLvoqlv2f1S9u1w0ZDazC2vnfGA3Wxm%2F57Ji0OBnBRKqQdZt4u9QlVjGmXS1VKPlllifG5f5JlmqpBYDZhJKC%2BwJQi0%2FTI1Mxv7qiftNArn8EuKf13ZKNkmhaHrPZ1yX%2FrDZ0EyrqhpSuNaZBxXn%2BUYtc7nRmmMNW5wbg9Avh5Tyiw01fQoUMUcS3sS8vBJvzLITguONoFa0gWeVcz%2BAcsN57W4rorwsVHG1qDG%2FiZM9NGBQu8wgd%2FtvAY6pgGZQjVzwSJIGiDgeYLoNTosf7iI4b9R7QHpjR4hbju87UFF4rA55xTi6evICvNhypMFtqkDpM6t%2FjFfcuDliEgQuXz4GaTEKIwBrpeNkdNlD%2FmF8MacpbNyyE%2Fwzpqpj8RyhV5CGH%2BeLm0FT96%2FO7I45uJtzM1igmgNgnVWa%2Fgc36BFAazAAO5lTYzYouNlbPncNEk5T1pYk6d1D5jsTqGjfRvZYr4c&X-Amz-Signature=52b2e4e1a40413a375d8794a8d19879d37104faa443258e81408a54d96efa804&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466626OWTFT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXSQdY7f1mroKBw6qWTKjcPrV7cQZyvPa0Gz7wzN7IeAiAgMUgc4l0V9206r4J1k%2B9Hv0e0kLBxmnEWydcr9PHkZSqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM70pfIJVBImxTSvJTKtwDigCh%2FFDPgrucg3bzsgYntuyuG%2BKF%2FKgwK3AaEHSu5%2BCZGN9OozQsDEfAt2%2BHYn0WpUPeTLYWvejXtgwoSg09eyv%2ByKNl%2FH0iJK56msS9pRq%2FgUjRfQ%2BmQLLTyGYunTzlmYxRmWOv4%2BVaYMUowRNdm69PKOmjp6hywQ273DTU8LhB8eX7utnjvfQrHGTdN9hXB6Gy67JxYWJn1%2FpJUTF5qYTpmr5KIs%2F0rZJs70djjAoHmqjT%2FGHTEfaWzGaQaPrB0Cpaqc3kjKh0ey8mlzK%2FiAavnVCqQj%2F%2B6Z%2Bj%2BQA%2B7CV6FBaW%2FOlRwNT3QrGnHObAgXSsDTISVQRBDA3zQnL8u3UN3nWVvbRjcUGFXoIuYxunYbTfKXq018IJqKnRKblT4iQLRSi9I%2BLvoqlv2f1S9u1w0ZDazC2vnfGA3Wxm%2F57Ji0OBnBRKqQdZt4u9QlVjGmXS1VKPlllifG5f5JlmqpBYDZhJKC%2BwJQi0%2FTI1Mxv7qiftNArn8EuKf13ZKNkmhaHrPZ1yX%2FrDZ0EyrqhpSuNaZBxXn%2BUYtc7nRmmMNW5wbg9Avh5Tyiw01fQoUMUcS3sS8vBJvzLITguONoFa0gWeVcz%2BAcsN57W4rorwsVHG1qDG%2FiZM9NGBQu8wgd%2FtvAY6pgGZQjVzwSJIGiDgeYLoNTosf7iI4b9R7QHpjR4hbju87UFF4rA55xTi6evICvNhypMFtqkDpM6t%2FjFfcuDliEgQuXz4GaTEKIwBrpeNkdNlD%2FmF8MacpbNyyE%2Fwzpqpj8RyhV5CGH%2BeLm0FT96%2FO7I45uJtzM1igmgNgnVWa%2Fgc36BFAazAAO5lTYzYouNlbPncNEk5T1pYk6d1D5jsTqGjfRvZYr4c&X-Amz-Signature=18f94650fcd24716d514cf06449859eb09e69041ddaaec37c5d8ab1049f5c392&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466626OWTFT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXSQdY7f1mroKBw6qWTKjcPrV7cQZyvPa0Gz7wzN7IeAiAgMUgc4l0V9206r4J1k%2B9Hv0e0kLBxmnEWydcr9PHkZSqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM70pfIJVBImxTSvJTKtwDigCh%2FFDPgrucg3bzsgYntuyuG%2BKF%2FKgwK3AaEHSu5%2BCZGN9OozQsDEfAt2%2BHYn0WpUPeTLYWvejXtgwoSg09eyv%2ByKNl%2FH0iJK56msS9pRq%2FgUjRfQ%2BmQLLTyGYunTzlmYxRmWOv4%2BVaYMUowRNdm69PKOmjp6hywQ273DTU8LhB8eX7utnjvfQrHGTdN9hXB6Gy67JxYWJn1%2FpJUTF5qYTpmr5KIs%2F0rZJs70djjAoHmqjT%2FGHTEfaWzGaQaPrB0Cpaqc3kjKh0ey8mlzK%2FiAavnVCqQj%2F%2B6Z%2Bj%2BQA%2B7CV6FBaW%2FOlRwNT3QrGnHObAgXSsDTISVQRBDA3zQnL8u3UN3nWVvbRjcUGFXoIuYxunYbTfKXq018IJqKnRKblT4iQLRSi9I%2BLvoqlv2f1S9u1w0ZDazC2vnfGA3Wxm%2F57Ji0OBnBRKqQdZt4u9QlVjGmXS1VKPlllifG5f5JlmqpBYDZhJKC%2BwJQi0%2FTI1Mxv7qiftNArn8EuKf13ZKNkmhaHrPZ1yX%2FrDZ0EyrqhpSuNaZBxXn%2BUYtc7nRmmMNW5wbg9Avh5Tyiw01fQoUMUcS3sS8vBJvzLITguONoFa0gWeVcz%2BAcsN57W4rorwsVHG1qDG%2FiZM9NGBQu8wgd%2FtvAY6pgGZQjVzwSJIGiDgeYLoNTosf7iI4b9R7QHpjR4hbju87UFF4rA55xTi6evICvNhypMFtqkDpM6t%2FjFfcuDliEgQuXz4GaTEKIwBrpeNkdNlD%2FmF8MacpbNyyE%2Fwzpqpj8RyhV5CGH%2BeLm0FT96%2FO7I45uJtzM1igmgNgnVWa%2Fgc36BFAazAAO5lTYzYouNlbPncNEk5T1pYk6d1D5jsTqGjfRvZYr4c&X-Amz-Signature=faed3df368792c5b95e5dfef8bac09df354528572e1b4f2d4cbc7b6fd347a2a4&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TU3NFMX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDDKJMsdcecw%2BDDWFHC%2B%2FlXN1Lva6sGlU0OsW8iGEqbAIgEgdLs5HgbTeLym3ziwg%2BKtnM6IbLniDi8pXV%2B6ug0eQqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCLYkwAn1DV1rkmbgCrcAwDK7yRnOM8QkqK%2BlDGgcFY%2Fc6TZj9p%2Bht4gQ8yqsbvI%2BU93IiGWbDM4jPE0bx8uZ%2FkXWW9G%2BiRIngJWh4B9BZ2tYKkA8SrwYT%2BkexWab7Ct6umeSI1CrJ%2BFbni%2BBXzhshTOexAJ1E2QMlsHtXqdCgZ%2BXUOj03uHTXlq1fYKEkSY46V5VlQtClQZT9vIyHEUCj5bD5fk5N6HIv%2BHkeftjDIgOMk%2BGdUyBxCchTFs2Tczwg0Sy9Nwr24jgM3hIeb4fkSjAbF82VDK1wnQcTWT1msOJiSPOCtF4yjMQ%2BDuiEkYY4poQxDienm2VcGFriA21s7EzWqp9DqAwp0y4UiPlAdwupZHM2hdjma%2BVysV9ebC4n3ykMdfl59yqQMlrbujCwfTzx0F1E9LX9X%2Feb0aWzcuxC%2F2nlfyFXzN8My1%2FPLNMZHlsmuTswNSnqSY3X%2FboXFm%2Fnj9OF6S59TVx5kLNdz%2BQucINzfXMq5cRpjtePh%2BkdX2VeOEvYtPEZFU8L2z%2B3Z9V6uSLZV93uqBNLdNA36dQ6k0dGMhFPWSLvdXmOjhg2tEgnCQCvrkoH9FVbqpDwNijyLcWxjHq%2F2nwXgYqkC7doExaPLWoUCcKmsIztetX%2FXAbA0xwcNjUHrmMMfe7bwGOqUB7Z6DlJvzm0%2Fc1h4ARHYvns6IoeD%2BUA3AX1njeIqjDd9hSbQanGGC58ZR9gkeRERhlQeNzhIByOKrkN%2BN1NBiCkH9BKPdcSZNt%2BU3CBvSt4IdqG0IPYEcDGnQ%2Fa5f%2F%2BIa3lit%2FMWfe4qTBnXRFzkxS8OueWtdzPrKgAU7F6Q3pHjcjAkXyeW4mzHWV2sLwmJjOY5dHFy%2FC1B9i5as307pVYq9sIWA&X-Amz-Signature=573d238cf36815b744774f006a01eda06aae000cfd3cc354cbd0cd138e63f223&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TU3NFMX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDDKJMsdcecw%2BDDWFHC%2B%2FlXN1Lva6sGlU0OsW8iGEqbAIgEgdLs5HgbTeLym3ziwg%2BKtnM6IbLniDi8pXV%2B6ug0eQqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCLYkwAn1DV1rkmbgCrcAwDK7yRnOM8QkqK%2BlDGgcFY%2Fc6TZj9p%2Bht4gQ8yqsbvI%2BU93IiGWbDM4jPE0bx8uZ%2FkXWW9G%2BiRIngJWh4B9BZ2tYKkA8SrwYT%2BkexWab7Ct6umeSI1CrJ%2BFbni%2BBXzhshTOexAJ1E2QMlsHtXqdCgZ%2BXUOj03uHTXlq1fYKEkSY46V5VlQtClQZT9vIyHEUCj5bD5fk5N6HIv%2BHkeftjDIgOMk%2BGdUyBxCchTFs2Tczwg0Sy9Nwr24jgM3hIeb4fkSjAbF82VDK1wnQcTWT1msOJiSPOCtF4yjMQ%2BDuiEkYY4poQxDienm2VcGFriA21s7EzWqp9DqAwp0y4UiPlAdwupZHM2hdjma%2BVysV9ebC4n3ykMdfl59yqQMlrbujCwfTzx0F1E9LX9X%2Feb0aWzcuxC%2F2nlfyFXzN8My1%2FPLNMZHlsmuTswNSnqSY3X%2FboXFm%2Fnj9OF6S59TVx5kLNdz%2BQucINzfXMq5cRpjtePh%2BkdX2VeOEvYtPEZFU8L2z%2B3Z9V6uSLZV93uqBNLdNA36dQ6k0dGMhFPWSLvdXmOjhg2tEgnCQCvrkoH9FVbqpDwNijyLcWxjHq%2F2nwXgYqkC7doExaPLWoUCcKmsIztetX%2FXAbA0xwcNjUHrmMMfe7bwGOqUB7Z6DlJvzm0%2Fc1h4ARHYvns6IoeD%2BUA3AX1njeIqjDd9hSbQanGGC58ZR9gkeRERhlQeNzhIByOKrkN%2BN1NBiCkH9BKPdcSZNt%2BU3CBvSt4IdqG0IPYEcDGnQ%2Fa5f%2F%2BIa3lit%2FMWfe4qTBnXRFzkxS8OueWtdzPrKgAU7F6Q3pHjcjAkXyeW4mzHWV2sLwmJjOY5dHFy%2FC1B9i5as307pVYq9sIWA&X-Amz-Signature=ee47d6391bcc280490abea36dc154cf4a6c8e66528f358544607d025b1aafde6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466626OWTFT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHXSQdY7f1mroKBw6qWTKjcPrV7cQZyvPa0Gz7wzN7IeAiAgMUgc4l0V9206r4J1k%2B9Hv0e0kLBxmnEWydcr9PHkZSqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM70pfIJVBImxTSvJTKtwDigCh%2FFDPgrucg3bzsgYntuyuG%2BKF%2FKgwK3AaEHSu5%2BCZGN9OozQsDEfAt2%2BHYn0WpUPeTLYWvejXtgwoSg09eyv%2ByKNl%2FH0iJK56msS9pRq%2FgUjRfQ%2BmQLLTyGYunTzlmYxRmWOv4%2BVaYMUowRNdm69PKOmjp6hywQ273DTU8LhB8eX7utnjvfQrHGTdN9hXB6Gy67JxYWJn1%2FpJUTF5qYTpmr5KIs%2F0rZJs70djjAoHmqjT%2FGHTEfaWzGaQaPrB0Cpaqc3kjKh0ey8mlzK%2FiAavnVCqQj%2F%2B6Z%2Bj%2BQA%2B7CV6FBaW%2FOlRwNT3QrGnHObAgXSsDTISVQRBDA3zQnL8u3UN3nWVvbRjcUGFXoIuYxunYbTfKXq018IJqKnRKblT4iQLRSi9I%2BLvoqlv2f1S9u1w0ZDazC2vnfGA3Wxm%2F57Ji0OBnBRKqQdZt4u9QlVjGmXS1VKPlllifG5f5JlmqpBYDZhJKC%2BwJQi0%2FTI1Mxv7qiftNArn8EuKf13ZKNkmhaHrPZ1yX%2FrDZ0EyrqhpSuNaZBxXn%2BUYtc7nRmmMNW5wbg9Avh5Tyiw01fQoUMUcS3sS8vBJvzLITguONoFa0gWeVcz%2BAcsN57W4rorwsVHG1qDG%2FiZM9NGBQu8wgd%2FtvAY6pgGZQjVzwSJIGiDgeYLoNTosf7iI4b9R7QHpjR4hbju87UFF4rA55xTi6evICvNhypMFtqkDpM6t%2FjFfcuDliEgQuXz4GaTEKIwBrpeNkdNlD%2FmF8MacpbNyyE%2Fwzpqpj8RyhV5CGH%2BeLm0FT96%2FO7I45uJtzM1igmgNgnVWa%2Fgc36BFAazAAO5lTYzYouNlbPncNEk5T1pYk6d1D5jsTqGjfRvZYr4c&X-Amz-Signature=c160fe495646789141da12b8064c9cc7b87ee862f1cf7f449204ca13f6f9a303&X-Amz-SignedHeaders=host&x-id=GetObject)
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