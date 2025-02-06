

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EEAQACO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIBCK5UwDJBlT%2FwFIsGWVrI%2Bml3qXxlFbX0%2BWEiPxIdiKAiEAwpdO3z8Qr842COzQTwAKQRbKa3La5CMTo5BWT71kmZQq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDKHg55iCWKPIKkwTFircA8eKY8e1HT8gm%2Fv3d3og7eHVvAy%2B4VCTgkwAV3lW2JqkGv64%2Bsd3wvSDWYUxp2MZA%2BMY%2BCChwE583%2BF%2B8y7XcjXyJNZVvUJtXU%2FUhQgPc019xnhJzOO9JqPD8LvPTpL1EWDvgsCMl%2BrXtNQY%2BUquuRQIAMusEFc5Jt2R7UAqZebvC22Q%2BaUjQ%2FMNwWuueGhN0DQL79aL7rzMun2hf9hn%2FOW6q8%2BgntYlpW75SAYJn9ENxEPwQMlZ93R6moFJNRj4FcusfAsqJXA75RbgoMnBbYPnPeHuRwUaZ7EVg9ODQVlz4kS%2B%2FS0CELgTnRF6pF%2BDUfBTtfRrbjREJi9ooXtfSxNMlhUPnAZqq3p23PuiZIkYsOwHZ5FJ9exVIPQTKKCniL27WOaL0xu%2BXAlc1EVZnvRZsIyfU0k%2BY7NzfaZzpaGbVrhkp663ZYEoQGPLc%2Bnn3S16ksyb6hYjf%2FgHIx43e%2BoDnq%2FjLHlc7V3cer48CkGk2JfA4ffhovFZy6E3Dqr1sxyFi9yg6w6KzkSinFoiEt5WkqnMIemfyXWYxwJUeqHXwlinGelNKltZCo1pZkXaZE2nXqZS3ESi%2FeQ%2BusvLxNAAKibzrxYZ0P3Ud9%2B9xhpBwgbsJSkaa%2FFfYoycMOT7kL0GOqUBHF8cgcJct6ySaxQoBhhML5vmPgkqTJAAKmtn%2BPrBw1sUZwjjbzL%2Brit1PxuS%2BJ81aT6hqB6rReJfF0mIwlhaVMKiDVIpAjqn3ozxELfLZY1LJCEkVBgOkR%2BzewOsr0uPD8k0psgIvZZFimnNr17ZOJ429kH7VxhCs8TMt1Tsc3fhR1j3hG%2F2sqjWroOCEgpYaHmrkaCqROPrpHofYuT%2FwR0P2%2FI8&X-Amz-Signature=e5f1da2f998ef5db3071c900e8ca915990d1c956ca6351ec9d8ed52a96e20293&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EEAQACO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIBCK5UwDJBlT%2FwFIsGWVrI%2Bml3qXxlFbX0%2BWEiPxIdiKAiEAwpdO3z8Qr842COzQTwAKQRbKa3La5CMTo5BWT71kmZQq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDKHg55iCWKPIKkwTFircA8eKY8e1HT8gm%2Fv3d3og7eHVvAy%2B4VCTgkwAV3lW2JqkGv64%2Bsd3wvSDWYUxp2MZA%2BMY%2BCChwE583%2BF%2B8y7XcjXyJNZVvUJtXU%2FUhQgPc019xnhJzOO9JqPD8LvPTpL1EWDvgsCMl%2BrXtNQY%2BUquuRQIAMusEFc5Jt2R7UAqZebvC22Q%2BaUjQ%2FMNwWuueGhN0DQL79aL7rzMun2hf9hn%2FOW6q8%2BgntYlpW75SAYJn9ENxEPwQMlZ93R6moFJNRj4FcusfAsqJXA75RbgoMnBbYPnPeHuRwUaZ7EVg9ODQVlz4kS%2B%2FS0CELgTnRF6pF%2BDUfBTtfRrbjREJi9ooXtfSxNMlhUPnAZqq3p23PuiZIkYsOwHZ5FJ9exVIPQTKKCniL27WOaL0xu%2BXAlc1EVZnvRZsIyfU0k%2BY7NzfaZzpaGbVrhkp663ZYEoQGPLc%2Bnn3S16ksyb6hYjf%2FgHIx43e%2BoDnq%2FjLHlc7V3cer48CkGk2JfA4ffhovFZy6E3Dqr1sxyFi9yg6w6KzkSinFoiEt5WkqnMIemfyXWYxwJUeqHXwlinGelNKltZCo1pZkXaZE2nXqZS3ESi%2FeQ%2BusvLxNAAKibzrxYZ0P3Ud9%2B9xhpBwgbsJSkaa%2FFfYoycMOT7kL0GOqUBHF8cgcJct6ySaxQoBhhML5vmPgkqTJAAKmtn%2BPrBw1sUZwjjbzL%2Brit1PxuS%2BJ81aT6hqB6rReJfF0mIwlhaVMKiDVIpAjqn3ozxELfLZY1LJCEkVBgOkR%2BzewOsr0uPD8k0psgIvZZFimnNr17ZOJ429kH7VxhCs8TMt1Tsc3fhR1j3hG%2F2sqjWroOCEgpYaHmrkaCqROPrpHofYuT%2FwR0P2%2FI8&X-Amz-Signature=30bb71f8ecbe588e058c8818d0778573aa5b143bf9bc3f9b16d3ce750dd252d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EEAQACO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIBCK5UwDJBlT%2FwFIsGWVrI%2Bml3qXxlFbX0%2BWEiPxIdiKAiEAwpdO3z8Qr842COzQTwAKQRbKa3La5CMTo5BWT71kmZQq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDKHg55iCWKPIKkwTFircA8eKY8e1HT8gm%2Fv3d3og7eHVvAy%2B4VCTgkwAV3lW2JqkGv64%2Bsd3wvSDWYUxp2MZA%2BMY%2BCChwE583%2BF%2B8y7XcjXyJNZVvUJtXU%2FUhQgPc019xnhJzOO9JqPD8LvPTpL1EWDvgsCMl%2BrXtNQY%2BUquuRQIAMusEFc5Jt2R7UAqZebvC22Q%2BaUjQ%2FMNwWuueGhN0DQL79aL7rzMun2hf9hn%2FOW6q8%2BgntYlpW75SAYJn9ENxEPwQMlZ93R6moFJNRj4FcusfAsqJXA75RbgoMnBbYPnPeHuRwUaZ7EVg9ODQVlz4kS%2B%2FS0CELgTnRF6pF%2BDUfBTtfRrbjREJi9ooXtfSxNMlhUPnAZqq3p23PuiZIkYsOwHZ5FJ9exVIPQTKKCniL27WOaL0xu%2BXAlc1EVZnvRZsIyfU0k%2BY7NzfaZzpaGbVrhkp663ZYEoQGPLc%2Bnn3S16ksyb6hYjf%2FgHIx43e%2BoDnq%2FjLHlc7V3cer48CkGk2JfA4ffhovFZy6E3Dqr1sxyFi9yg6w6KzkSinFoiEt5WkqnMIemfyXWYxwJUeqHXwlinGelNKltZCo1pZkXaZE2nXqZS3ESi%2FeQ%2BusvLxNAAKibzrxYZ0P3Ud9%2B9xhpBwgbsJSkaa%2FFfYoycMOT7kL0GOqUBHF8cgcJct6ySaxQoBhhML5vmPgkqTJAAKmtn%2BPrBw1sUZwjjbzL%2Brit1PxuS%2BJ81aT6hqB6rReJfF0mIwlhaVMKiDVIpAjqn3ozxELfLZY1LJCEkVBgOkR%2BzewOsr0uPD8k0psgIvZZFimnNr17ZOJ429kH7VxhCs8TMt1Tsc3fhR1j3hG%2F2sqjWroOCEgpYaHmrkaCqROPrpHofYuT%2FwR0P2%2FI8&X-Amz-Signature=f19016b258a4358652c4d84c8064e1484e5968d3ca50d5d20a39b91918083878&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BIXXMH3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIBX9R7SbwZkM%2B%2BTwbMhNw9kSkKk6VP9l4fqCrQMecXEWAiEA1rMoWYU4z2Q4j8cdNUr72d3rLmeWWWi%2F0GF8Pnv6KQ8q%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDFKM9s7i0hcmhcmR9ircAz8%2F9FM%2FbVzjsBaBOfbOaOz5QvK4ycAyZt8gjwI59Uqh6eZ%2BsX8WZpNwZIc8JL9EisU9Z7CVog02yfjseom6MRK%2BOIjdfpzV6Pap6nBF3RH0zfiPXe%2FowXRLfVULqbE3hQy%2F2SrIqMqbxAQylJy%2Fzpyw%2BoLtyO163xoGVvAV53nTglaMrqx9EQA1bot%2F1j8I3Wr4ohE%2Fo%2BOGIICkjV4oZjsiGCojzxG%2FQT6%2FtCk4aVw5OHQCyPfIhogBukC91yC8t6gN0tfIi%2FwFjtJYHEDqQcNVpQlzbbX68dMRQ4%2Bs%2Bwa5J0AZTrlZLv81lWQ7c7NDnL5zSc1krSiNzTLZ9cOj8Dl6%2BVrf0rknKO0rRK5jiFq03fl%2BNCgxbnh8TiLaSFB3G5%2BRc4N0y58MS1PHx1P7HYWTLrXsNiyV55XjWL4roZJHtB%2B7Q0GRsg%2BTolx6m0qZgW6CC5CPQuBue6jynKvSpcQcAbkebLC8vjUPX%2BSEFFPXpBo6y2AeaF7oCWhqwtUb3sA7gQ%2Fg4yZIO2hMkfaxMCRO%2FwoKoJU4xMvvgngFQPypPMRB08HzwDpZ%2FKm3wGkZQJM4AKJzSq69bu5ccBTzQvBEW%2FF0qfLkoHPhfqxapwXDdrBFZAlX2A1rnX1hMP37kL0GOqUB1X4jr5qhKfXvrzbSViTcZkFvKahSxaHupmH3kuc6gZTdrA02DkXEWjDAoOwQLS5Pch70NJcbj4s3KctFrFT6lgmn64wV3UIDSMeEFuBkX485zGtFAHErClt7vAXAnZfDFT8JFBSllZFW74u7%2BxH%2BlNI93RrUHR9cHa7gG2JM6uyBLcXUyuKRnkNfLkZlxFZOHsb%2FFbKH9R4jux6tUec89qCRHMVB&X-Amz-Signature=6b6a7d990f7c4698dbe8a98f0898686866d4fdfe6d36dbc778a3052fd7fb9840&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BIXXMH3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIBX9R7SbwZkM%2B%2BTwbMhNw9kSkKk6VP9l4fqCrQMecXEWAiEA1rMoWYU4z2Q4j8cdNUr72d3rLmeWWWi%2F0GF8Pnv6KQ8q%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDFKM9s7i0hcmhcmR9ircAz8%2F9FM%2FbVzjsBaBOfbOaOz5QvK4ycAyZt8gjwI59Uqh6eZ%2BsX8WZpNwZIc8JL9EisU9Z7CVog02yfjseom6MRK%2BOIjdfpzV6Pap6nBF3RH0zfiPXe%2FowXRLfVULqbE3hQy%2F2SrIqMqbxAQylJy%2Fzpyw%2BoLtyO163xoGVvAV53nTglaMrqx9EQA1bot%2F1j8I3Wr4ohE%2Fo%2BOGIICkjV4oZjsiGCojzxG%2FQT6%2FtCk4aVw5OHQCyPfIhogBukC91yC8t6gN0tfIi%2FwFjtJYHEDqQcNVpQlzbbX68dMRQ4%2Bs%2Bwa5J0AZTrlZLv81lWQ7c7NDnL5zSc1krSiNzTLZ9cOj8Dl6%2BVrf0rknKO0rRK5jiFq03fl%2BNCgxbnh8TiLaSFB3G5%2BRc4N0y58MS1PHx1P7HYWTLrXsNiyV55XjWL4roZJHtB%2B7Q0GRsg%2BTolx6m0qZgW6CC5CPQuBue6jynKvSpcQcAbkebLC8vjUPX%2BSEFFPXpBo6y2AeaF7oCWhqwtUb3sA7gQ%2Fg4yZIO2hMkfaxMCRO%2FwoKoJU4xMvvgngFQPypPMRB08HzwDpZ%2FKm3wGkZQJM4AKJzSq69bu5ccBTzQvBEW%2FF0qfLkoHPhfqxapwXDdrBFZAlX2A1rnX1hMP37kL0GOqUB1X4jr5qhKfXvrzbSViTcZkFvKahSxaHupmH3kuc6gZTdrA02DkXEWjDAoOwQLS5Pch70NJcbj4s3KctFrFT6lgmn64wV3UIDSMeEFuBkX485zGtFAHErClt7vAXAnZfDFT8JFBSllZFW74u7%2BxH%2BlNI93RrUHR9cHa7gG2JM6uyBLcXUyuKRnkNfLkZlxFZOHsb%2FFbKH9R4jux6tUec89qCRHMVB&X-Amz-Signature=c4ba03331471ca0a922d852532d914eeec82787b24b972e16166cd60b6a4ba14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EEAQACO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIBCK5UwDJBlT%2FwFIsGWVrI%2Bml3qXxlFbX0%2BWEiPxIdiKAiEAwpdO3z8Qr842COzQTwAKQRbKa3La5CMTo5BWT71kmZQq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDKHg55iCWKPIKkwTFircA8eKY8e1HT8gm%2Fv3d3og7eHVvAy%2B4VCTgkwAV3lW2JqkGv64%2Bsd3wvSDWYUxp2MZA%2BMY%2BCChwE583%2BF%2B8y7XcjXyJNZVvUJtXU%2FUhQgPc019xnhJzOO9JqPD8LvPTpL1EWDvgsCMl%2BrXtNQY%2BUquuRQIAMusEFc5Jt2R7UAqZebvC22Q%2BaUjQ%2FMNwWuueGhN0DQL79aL7rzMun2hf9hn%2FOW6q8%2BgntYlpW75SAYJn9ENxEPwQMlZ93R6moFJNRj4FcusfAsqJXA75RbgoMnBbYPnPeHuRwUaZ7EVg9ODQVlz4kS%2B%2FS0CELgTnRF6pF%2BDUfBTtfRrbjREJi9ooXtfSxNMlhUPnAZqq3p23PuiZIkYsOwHZ5FJ9exVIPQTKKCniL27WOaL0xu%2BXAlc1EVZnvRZsIyfU0k%2BY7NzfaZzpaGbVrhkp663ZYEoQGPLc%2Bnn3S16ksyb6hYjf%2FgHIx43e%2BoDnq%2FjLHlc7V3cer48CkGk2JfA4ffhovFZy6E3Dqr1sxyFi9yg6w6KzkSinFoiEt5WkqnMIemfyXWYxwJUeqHXwlinGelNKltZCo1pZkXaZE2nXqZS3ESi%2FeQ%2BusvLxNAAKibzrxYZ0P3Ud9%2B9xhpBwgbsJSkaa%2FFfYoycMOT7kL0GOqUBHF8cgcJct6ySaxQoBhhML5vmPgkqTJAAKmtn%2BPrBw1sUZwjjbzL%2Brit1PxuS%2BJ81aT6hqB6rReJfF0mIwlhaVMKiDVIpAjqn3ozxELfLZY1LJCEkVBgOkR%2BzewOsr0uPD8k0psgIvZZFimnNr17ZOJ429kH7VxhCs8TMt1Tsc3fhR1j3hG%2F2sqjWroOCEgpYaHmrkaCqROPrpHofYuT%2FwR0P2%2FI8&X-Amz-Signature=48fbda6a2dfa5d8e0e2993471af373fa059ccf77173abfac20c8d18e6f690971&X-Amz-SignedHeaders=host&x-id=GetObject)
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