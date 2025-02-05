

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2D3GND%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDJnsXcmy%2BiJ8adY1cx0GhXQnJouqNK7F9yOpA2OCbaoAiAfEASDG%2B%2FPvZJAwN8inhMO7ZH3k9Zb0XC4Cq8QlaQHlir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMCHjG8wN6M0ECN7dOKtwDT4OGqy3xPKDfAkwlxwr9QNKdiyOtIwrsHj1xsCmcVQmT8UivR0vPq4pJausNbF%2FVcv%2BMHgWGK0AMMPQ%2B%2BftsvYAF4e83QbhIl4M0xNeGsuqiVY5SzV5wPaY8By5tAO0vSyRjvo%2FywQGVW7AQAG7AZbdQmJgmKql9wH5SQR8d%2FEZilYo9r3eevf1Vn0oh%2FPPK5M%2BDRH03%2F9B%2FOhTJh0Envrw2f6e52Ws4io2Vs75u%2BhXp%2BhFrifqpDctIsbxToU0DkA%2BWmsWQFRYUJXknR%2BoxEL%2BCAgz5ckZnqv0jRPwhBviHFqqB4tlFRKAyITc0vFN4VulZH%2BSQyT8Llp%2Fc4CX4%2Bm76ElZaEb5KF9K1IMCqGjWozj1hTErsP4%2BHquoa%2FfO4S3AcS5IICpVg%2FcjJ%2FsBCtX5ovfKFNDcPhLbNQ%2BlsKhRBAJvJdU7JMAyRqNiLfmJFp%2BuJAFENM7Z%2B47FbLBCJgaOXXw%2FNMLn75pmF0a3YOugJiZbaQ1bBkk%2BKXGDV%2BJL8V2zc7ntB3dMn420Pr2y5nag5qqezEv871dDnreBFF6ZD1YdMGsvUrGyY3KcA1sdryZ3qA%2F%2FlcC5veUcrPehxhk7HasaLXThFyWXVYXyOxv1mPWyfk9D5EZ5iqLEwh7uOvQY6pgFBvHsZ4n63W%2BLqTyUaP7V5oVRIbbAdjyTGShDnEIKar4O%2FACD0sUEdUyZroONsrHhZwKz0pD0YdCuPhVhXkdfcdJIzjAuUgXnybqb6iQKTLl%2B5U9p%2B623iVvvgQoOX3GRZNFy8O%2FufMDbIorGvIrC2YawBJfKtz1XXgc9OdW7gQZ4YMU2jPbc59bjlD1aSgnkW3IDFLuRoZF4upwXaqvso6UsvPLqB&X-Amz-Signature=cc1e1ec7c1f4a7832611c119fdeb588055d5023cdad413a526eb2be74fb80438&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2D3GND%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDJnsXcmy%2BiJ8adY1cx0GhXQnJouqNK7F9yOpA2OCbaoAiAfEASDG%2B%2FPvZJAwN8inhMO7ZH3k9Zb0XC4Cq8QlaQHlir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMCHjG8wN6M0ECN7dOKtwDT4OGqy3xPKDfAkwlxwr9QNKdiyOtIwrsHj1xsCmcVQmT8UivR0vPq4pJausNbF%2FVcv%2BMHgWGK0AMMPQ%2B%2BftsvYAF4e83QbhIl4M0xNeGsuqiVY5SzV5wPaY8By5tAO0vSyRjvo%2FywQGVW7AQAG7AZbdQmJgmKql9wH5SQR8d%2FEZilYo9r3eevf1Vn0oh%2FPPK5M%2BDRH03%2F9B%2FOhTJh0Envrw2f6e52Ws4io2Vs75u%2BhXp%2BhFrifqpDctIsbxToU0DkA%2BWmsWQFRYUJXknR%2BoxEL%2BCAgz5ckZnqv0jRPwhBviHFqqB4tlFRKAyITc0vFN4VulZH%2BSQyT8Llp%2Fc4CX4%2Bm76ElZaEb5KF9K1IMCqGjWozj1hTErsP4%2BHquoa%2FfO4S3AcS5IICpVg%2FcjJ%2FsBCtX5ovfKFNDcPhLbNQ%2BlsKhRBAJvJdU7JMAyRqNiLfmJFp%2BuJAFENM7Z%2B47FbLBCJgaOXXw%2FNMLn75pmF0a3YOugJiZbaQ1bBkk%2BKXGDV%2BJL8V2zc7ntB3dMn420Pr2y5nag5qqezEv871dDnreBFF6ZD1YdMGsvUrGyY3KcA1sdryZ3qA%2F%2FlcC5veUcrPehxhk7HasaLXThFyWXVYXyOxv1mPWyfk9D5EZ5iqLEwh7uOvQY6pgFBvHsZ4n63W%2BLqTyUaP7V5oVRIbbAdjyTGShDnEIKar4O%2FACD0sUEdUyZroONsrHhZwKz0pD0YdCuPhVhXkdfcdJIzjAuUgXnybqb6iQKTLl%2B5U9p%2B623iVvvgQoOX3GRZNFy8O%2FufMDbIorGvIrC2YawBJfKtz1XXgc9OdW7gQZ4YMU2jPbc59bjlD1aSgnkW3IDFLuRoZF4upwXaqvso6UsvPLqB&X-Amz-Signature=5db11b1cc75866b0af24d6f927862eeb3d99454ad2a19b2fa8b5a2cacf69bf1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2D3GND%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDJnsXcmy%2BiJ8adY1cx0GhXQnJouqNK7F9yOpA2OCbaoAiAfEASDG%2B%2FPvZJAwN8inhMO7ZH3k9Zb0XC4Cq8QlaQHlir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMCHjG8wN6M0ECN7dOKtwDT4OGqy3xPKDfAkwlxwr9QNKdiyOtIwrsHj1xsCmcVQmT8UivR0vPq4pJausNbF%2FVcv%2BMHgWGK0AMMPQ%2B%2BftsvYAF4e83QbhIl4M0xNeGsuqiVY5SzV5wPaY8By5tAO0vSyRjvo%2FywQGVW7AQAG7AZbdQmJgmKql9wH5SQR8d%2FEZilYo9r3eevf1Vn0oh%2FPPK5M%2BDRH03%2F9B%2FOhTJh0Envrw2f6e52Ws4io2Vs75u%2BhXp%2BhFrifqpDctIsbxToU0DkA%2BWmsWQFRYUJXknR%2BoxEL%2BCAgz5ckZnqv0jRPwhBviHFqqB4tlFRKAyITc0vFN4VulZH%2BSQyT8Llp%2Fc4CX4%2Bm76ElZaEb5KF9K1IMCqGjWozj1hTErsP4%2BHquoa%2FfO4S3AcS5IICpVg%2FcjJ%2FsBCtX5ovfKFNDcPhLbNQ%2BlsKhRBAJvJdU7JMAyRqNiLfmJFp%2BuJAFENM7Z%2B47FbLBCJgaOXXw%2FNMLn75pmF0a3YOugJiZbaQ1bBkk%2BKXGDV%2BJL8V2zc7ntB3dMn420Pr2y5nag5qqezEv871dDnreBFF6ZD1YdMGsvUrGyY3KcA1sdryZ3qA%2F%2FlcC5veUcrPehxhk7HasaLXThFyWXVYXyOxv1mPWyfk9D5EZ5iqLEwh7uOvQY6pgFBvHsZ4n63W%2BLqTyUaP7V5oVRIbbAdjyTGShDnEIKar4O%2FACD0sUEdUyZroONsrHhZwKz0pD0YdCuPhVhXkdfcdJIzjAuUgXnybqb6iQKTLl%2B5U9p%2B623iVvvgQoOX3GRZNFy8O%2FufMDbIorGvIrC2YawBJfKtz1XXgc9OdW7gQZ4YMU2jPbc59bjlD1aSgnkW3IDFLuRoZF4upwXaqvso6UsvPLqB&X-Amz-Signature=42a7628f033ec6c7788d2ed3be4a29c600444b2e2d6b6d7af999cb4d070bfab8&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RH5PGGW3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCQ4H%2BeMhZ9%2B9GMzfezIZJV%2FFoy8fCSka5wyUmAldkXewIgMZP4czN9ID0b7M3wkbyMu4gByNWuqyyYsXf1vLJn6SIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDCMeA3zrUJ9afYAHECrcA%2BRH3CuFPoU052BEyEi%2FLrKf0yLxGn3Jw6R%2BNwNewnA1Hzj6ZkKNohUsjOcVFvGgHZzWMOZvcVa3m%2Fs75BI%2F0s9kAwHAmdAL5bxjMXuQmDpNMhTbR62eN8h6VOZE1T5NLXZTzFhJQao3aJlzR26fy8GVHcxV5gV2Vx9DA16B%2BQ3kqqy0AVodcjfcTQOKbAxDJdIV7zRbqYp9IwOIQHbzFs4u1cnBU2x%2FXAn3ZjyWF%2FnOwZLkBjtm9dyD1tePjGwbjaBZeE5z897ZQwEtAGhQg7D7uVzTv9wxZd4hG1z4u41hp7oXdP%2BJno7cjwTlC7J3691lM%2BVi%2BZ875YcI758q3AzKC7IpyFh%2FRMxctPWbe%2Buao1z0NOYYKFPcTWvZU%2FO4n3mH86YxlRvINrXOZDbpT%2BLZ7J3jCrh8c4qsJ16BqbXidKBJvhlsDf8IwQlQHd2aBZdc741ZsByp%2BUZNvuvZUCKlRDMf6AaITi94I1yYu97vvkyVvJFMC%2Bdw%2FXaE2ZHFT3IMiRN3Hdx7tgEMZObn%2FbeOEbWNZrvicTdsViMn8uxnd4pamgPvnKTxbznu8gcfO2dxbNUSsS0KHdTW25pctJU98wU9rfijM53DyB4xbIG0kSTAYwg7Vz4DUADDMO66jr0GOqUBKNkAazs9lB0jTzfyal8plK7mZm0tWrjRV9x9e0zRFwEJ1pz4V8QDSLurp9RZYZ3XKJ%2BW8JRNQwtX0lBcWVwdXnp8IFeOWTt8v43vcNMTU3ZthyBix9C1L7XFwJK%2FrPu%2BPC8IKvxw8hn68UtISJKcPj%2BFz9OK%2F2N%2Fp5wqR%2BywlXjmLC8yxFNYmLunzU1JGVKN6AH0T4KtUDrnrRMCOseCoYMr0csy&X-Amz-Signature=188c52797bd7edea2942540f8c7abd2c480be161d7f51640b8d7d99dde558a30&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RH5PGGW3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCQ4H%2BeMhZ9%2B9GMzfezIZJV%2FFoy8fCSka5wyUmAldkXewIgMZP4czN9ID0b7M3wkbyMu4gByNWuqyyYsXf1vLJn6SIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDCMeA3zrUJ9afYAHECrcA%2BRH3CuFPoU052BEyEi%2FLrKf0yLxGn3Jw6R%2BNwNewnA1Hzj6ZkKNohUsjOcVFvGgHZzWMOZvcVa3m%2Fs75BI%2F0s9kAwHAmdAL5bxjMXuQmDpNMhTbR62eN8h6VOZE1T5NLXZTzFhJQao3aJlzR26fy8GVHcxV5gV2Vx9DA16B%2BQ3kqqy0AVodcjfcTQOKbAxDJdIV7zRbqYp9IwOIQHbzFs4u1cnBU2x%2FXAn3ZjyWF%2FnOwZLkBjtm9dyD1tePjGwbjaBZeE5z897ZQwEtAGhQg7D7uVzTv9wxZd4hG1z4u41hp7oXdP%2BJno7cjwTlC7J3691lM%2BVi%2BZ875YcI758q3AzKC7IpyFh%2FRMxctPWbe%2Buao1z0NOYYKFPcTWvZU%2FO4n3mH86YxlRvINrXOZDbpT%2BLZ7J3jCrh8c4qsJ16BqbXidKBJvhlsDf8IwQlQHd2aBZdc741ZsByp%2BUZNvuvZUCKlRDMf6AaITi94I1yYu97vvkyVvJFMC%2Bdw%2FXaE2ZHFT3IMiRN3Hdx7tgEMZObn%2FbeOEbWNZrvicTdsViMn8uxnd4pamgPvnKTxbznu8gcfO2dxbNUSsS0KHdTW25pctJU98wU9rfijM53DyB4xbIG0kSTAYwg7Vz4DUADDMO66jr0GOqUBKNkAazs9lB0jTzfyal8plK7mZm0tWrjRV9x9e0zRFwEJ1pz4V8QDSLurp9RZYZ3XKJ%2BW8JRNQwtX0lBcWVwdXnp8IFeOWTt8v43vcNMTU3ZthyBix9C1L7XFwJK%2FrPu%2BPC8IKvxw8hn68UtISJKcPj%2BFz9OK%2F2N%2Fp5wqR%2BywlXjmLC8yxFNYmLunzU1JGVKN6AH0T4KtUDrnrRMCOseCoYMr0csy&X-Amz-Signature=e97bfc95ffab4c256b3373a1f52d6413a50e97f33a45656a64631a2c570b7728&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2D3GND%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIDJnsXcmy%2BiJ8adY1cx0GhXQnJouqNK7F9yOpA2OCbaoAiAfEASDG%2B%2FPvZJAwN8inhMO7ZH3k9Zb0XC4Cq8QlaQHlir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMCHjG8wN6M0ECN7dOKtwDT4OGqy3xPKDfAkwlxwr9QNKdiyOtIwrsHj1xsCmcVQmT8UivR0vPq4pJausNbF%2FVcv%2BMHgWGK0AMMPQ%2B%2BftsvYAF4e83QbhIl4M0xNeGsuqiVY5SzV5wPaY8By5tAO0vSyRjvo%2FywQGVW7AQAG7AZbdQmJgmKql9wH5SQR8d%2FEZilYo9r3eevf1Vn0oh%2FPPK5M%2BDRH03%2F9B%2FOhTJh0Envrw2f6e52Ws4io2Vs75u%2BhXp%2BhFrifqpDctIsbxToU0DkA%2BWmsWQFRYUJXknR%2BoxEL%2BCAgz5ckZnqv0jRPwhBviHFqqB4tlFRKAyITc0vFN4VulZH%2BSQyT8Llp%2Fc4CX4%2Bm76ElZaEb5KF9K1IMCqGjWozj1hTErsP4%2BHquoa%2FfO4S3AcS5IICpVg%2FcjJ%2FsBCtX5ovfKFNDcPhLbNQ%2BlsKhRBAJvJdU7JMAyRqNiLfmJFp%2BuJAFENM7Z%2B47FbLBCJgaOXXw%2FNMLn75pmF0a3YOugJiZbaQ1bBkk%2BKXGDV%2BJL8V2zc7ntB3dMn420Pr2y5nag5qqezEv871dDnreBFF6ZD1YdMGsvUrGyY3KcA1sdryZ3qA%2F%2FlcC5veUcrPehxhk7HasaLXThFyWXVYXyOxv1mPWyfk9D5EZ5iqLEwh7uOvQY6pgFBvHsZ4n63W%2BLqTyUaP7V5oVRIbbAdjyTGShDnEIKar4O%2FACD0sUEdUyZroONsrHhZwKz0pD0YdCuPhVhXkdfcdJIzjAuUgXnybqb6iQKTLl%2B5U9p%2B623iVvvgQoOX3GRZNFy8O%2FufMDbIorGvIrC2YawBJfKtz1XXgc9OdW7gQZ4YMU2jPbc59bjlD1aSgnkW3IDFLuRoZF4upwXaqvso6UsvPLqB&X-Amz-Signature=d409f8ef13ac172e37676a5456c442a4fa1eec5a4f9c81c8b8139e6ec97f7575&X-Amz-SignedHeaders=host&x-id=GetObject)
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