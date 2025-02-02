

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GVGPMCW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkSxc2kE60ctibC28rZDcRcqYDw6X514Qk8KGHJA3t1wIgciwwPp5m8aAb9%2B4ADIHMNJweZtdwfOhUO6c2tu00WlkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEQFG5%2BdAqYvy30W2CrcAwqzXHjI4bxxXwkiJ39lVBdIvmMCIic%2BCsBwNZp3%2F4uxMK49No7cZaBh7EeKje6Ku%2BQUJd4tLKd1OuFINtcGcqqG7KV4xWSAIVrgOWZ17OzYtThIt%2FO7tkeNcR%2Fh20w883aVFZ4OrKsTsNb%2F6CsM9rC1HGt6SKwt0UjCEplPLQ9MQNF0xc3sbae78sDUxL5HwA1uSEoNMW%2BGQK69mfi53v%2FTLy1LAo8y9V9WaPGt1TSbYxvFVSTAHcuZzmbbPO05pYO0pRzk7aW%2BUAmJMcSC0BOAsY6vM%2FF0lREwuImE2%2FGWefXjVE7oU3B1p3VB579sHajDodU5fiJJ%2FUPhta%2BZtSB7XpavLUxwN5jbx%2Bw%2B%2BhuSqU8UXpBNfSSJDyjJ%2Fp2NQmUoNhjsNtvBBOg%2BbhxuSK556LcWQmfbp6ZDhsa8sQvGEd4cAZQ1QQQdwtGc0xXtTdph%2Bv9lQU9yf5q%2FlFlqoZDO0hskT0V3pr3AZnjJaxDtd%2BtwXfmWDsUbMSCU%2BK%2BeFkfRvI0jL9CLwtd4O0g0oaCWSbjZBR%2BRCMwnDLgWO74i1c6I3Isrw%2B0BeuXU1vlODdMwQPMvHYUwhT6gXHcZkDiXoN%2BVppzQF1baEam3E3sqIC3KmqqQooMMeBAEMOTB%2FbwGOqUBUZLl8byXYSFUl0CBRkdGPtXNec9LF5Zh6TRqa%2FuFobfAt9bagBYLqDDOKVSAEDxz8MWhzlOSEukne95x7moNO4yFUfk5PQzmvZgdacjxRaqXaSR%2Blm4xc642pqor0AlaMu7ZGFZz1gt923dPF%2FNwIB4%2FpMViYg98t9gqg7T%2BqVP1m89zIS5WhefdZuSVjZ99QkWWr97ljmnUYHMOx8N6ck4Z%2B3Fr&X-Amz-Signature=ad4153d1f3b03ffedaf549bb45b06d54106af9eb89eb037395ab674587afec2a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GVGPMCW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkSxc2kE60ctibC28rZDcRcqYDw6X514Qk8KGHJA3t1wIgciwwPp5m8aAb9%2B4ADIHMNJweZtdwfOhUO6c2tu00WlkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEQFG5%2BdAqYvy30W2CrcAwqzXHjI4bxxXwkiJ39lVBdIvmMCIic%2BCsBwNZp3%2F4uxMK49No7cZaBh7EeKje6Ku%2BQUJd4tLKd1OuFINtcGcqqG7KV4xWSAIVrgOWZ17OzYtThIt%2FO7tkeNcR%2Fh20w883aVFZ4OrKsTsNb%2F6CsM9rC1HGt6SKwt0UjCEplPLQ9MQNF0xc3sbae78sDUxL5HwA1uSEoNMW%2BGQK69mfi53v%2FTLy1LAo8y9V9WaPGt1TSbYxvFVSTAHcuZzmbbPO05pYO0pRzk7aW%2BUAmJMcSC0BOAsY6vM%2FF0lREwuImE2%2FGWefXjVE7oU3B1p3VB579sHajDodU5fiJJ%2FUPhta%2BZtSB7XpavLUxwN5jbx%2Bw%2B%2BhuSqU8UXpBNfSSJDyjJ%2Fp2NQmUoNhjsNtvBBOg%2BbhxuSK556LcWQmfbp6ZDhsa8sQvGEd4cAZQ1QQQdwtGc0xXtTdph%2Bv9lQU9yf5q%2FlFlqoZDO0hskT0V3pr3AZnjJaxDtd%2BtwXfmWDsUbMSCU%2BK%2BeFkfRvI0jL9CLwtd4O0g0oaCWSbjZBR%2BRCMwnDLgWO74i1c6I3Isrw%2B0BeuXU1vlODdMwQPMvHYUwhT6gXHcZkDiXoN%2BVppzQF1baEam3E3sqIC3KmqqQooMMeBAEMOTB%2FbwGOqUBUZLl8byXYSFUl0CBRkdGPtXNec9LF5Zh6TRqa%2FuFobfAt9bagBYLqDDOKVSAEDxz8MWhzlOSEukne95x7moNO4yFUfk5PQzmvZgdacjxRaqXaSR%2Blm4xc642pqor0AlaMu7ZGFZz1gt923dPF%2FNwIB4%2FpMViYg98t9gqg7T%2BqVP1m89zIS5WhefdZuSVjZ99QkWWr97ljmnUYHMOx8N6ck4Z%2B3Fr&X-Amz-Signature=aa2a38cbda0e7b542129fa5556adc91d1c000bbb300d9d775c54c49b90923668&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GVGPMCW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkSxc2kE60ctibC28rZDcRcqYDw6X514Qk8KGHJA3t1wIgciwwPp5m8aAb9%2B4ADIHMNJweZtdwfOhUO6c2tu00WlkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEQFG5%2BdAqYvy30W2CrcAwqzXHjI4bxxXwkiJ39lVBdIvmMCIic%2BCsBwNZp3%2F4uxMK49No7cZaBh7EeKje6Ku%2BQUJd4tLKd1OuFINtcGcqqG7KV4xWSAIVrgOWZ17OzYtThIt%2FO7tkeNcR%2Fh20w883aVFZ4OrKsTsNb%2F6CsM9rC1HGt6SKwt0UjCEplPLQ9MQNF0xc3sbae78sDUxL5HwA1uSEoNMW%2BGQK69mfi53v%2FTLy1LAo8y9V9WaPGt1TSbYxvFVSTAHcuZzmbbPO05pYO0pRzk7aW%2BUAmJMcSC0BOAsY6vM%2FF0lREwuImE2%2FGWefXjVE7oU3B1p3VB579sHajDodU5fiJJ%2FUPhta%2BZtSB7XpavLUxwN5jbx%2Bw%2B%2BhuSqU8UXpBNfSSJDyjJ%2Fp2NQmUoNhjsNtvBBOg%2BbhxuSK556LcWQmfbp6ZDhsa8sQvGEd4cAZQ1QQQdwtGc0xXtTdph%2Bv9lQU9yf5q%2FlFlqoZDO0hskT0V3pr3AZnjJaxDtd%2BtwXfmWDsUbMSCU%2BK%2BeFkfRvI0jL9CLwtd4O0g0oaCWSbjZBR%2BRCMwnDLgWO74i1c6I3Isrw%2B0BeuXU1vlODdMwQPMvHYUwhT6gXHcZkDiXoN%2BVppzQF1baEam3E3sqIC3KmqqQooMMeBAEMOTB%2FbwGOqUBUZLl8byXYSFUl0CBRkdGPtXNec9LF5Zh6TRqa%2FuFobfAt9bagBYLqDDOKVSAEDxz8MWhzlOSEukne95x7moNO4yFUfk5PQzmvZgdacjxRaqXaSR%2Blm4xc642pqor0AlaMu7ZGFZz1gt923dPF%2FNwIB4%2FpMViYg98t9gqg7T%2BqVP1m89zIS5WhefdZuSVjZ99QkWWr97ljmnUYHMOx8N6ck4Z%2B3Fr&X-Amz-Signature=91f4d6092b8976b35762bdedc7842632ffe6a37508aa27a80ec930caada06a4c&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3AZYHTG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBbeyNf04zgOc3M%2B6Av4qzstZ39tdchD42OFJkZhvEWaAiEAihFBMlFF%2BRp54l3wghdqebkSRqYOWg95XqaEWk0ynwgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBttZ%2BTFms6hA3tjUSrcAwzeb%2B7y1%2BczPu8%2ByNgclnZhLZL0SjUDrF6HaKJXrwAw91pylsBluYikoEd3LivgcVvj%2F6z6d%2FkjpWHpSTvjmJRMdPJziZl1eVsAyc4Or5UWBqoIwMS61EQ0X21vLjiaTWK3Z2QSQ99zzSu8hxvF7l5xyfMMgtZ%2FgIhVtdWVP%2FIuDGTcjl1XQakUOtEhOUac13lCQBZYu5bz7fc8wS4hXq0kkkI08rTzU9ipDPbXvEZFFmyEWUgsvWpcSU1j1kqZLGoStCdGsoL8FzYqHYeaBpK04%2BTKIk%2FrLr51b8Ibs9wvVTe5JGWlwyOkaQAJnFcJuNXqdj0O05sSdkKD4y48ZoZ23dr6zmjW%2BOMwxYlPX5dKqBGCyXRnpxhTKGUj%2FBfPxu%2FjTDZQiVwrDSk1iGa5AwIsOh4UkiUg%2FcIvDdW3i5qME3p0A75ib0Sq4xXI6%2BrbA18qH6a6%2BrkE5wfauS16CNMJG34cP5y1o8gPe64pCs3L3%2BxqNb4xvuKuJTp1r7I2ArHkLXfSl2MaI9ycDJERlbAdOFrpIbtJ7bVMK%2BwFd7mvNYwfkswyOfBlzJ%2FVZKVVczJ0r8isHG2149l27xArt3WMDZ2uvDj1tNOE4s%2B4qOyfC6nQIf70GWOeMi93ML%2FB%2FbwGOqUB8U3aQPNu7Y0cx7mZ7Jt2yg%2Bs%2F5wW%2BgNox9oaH7Qp8i%2FuKrX6UkWgyCrzqxgQcfvjdefejdq5Dls3tHMXhO4qJZbA%2FRHWhOZV6Zxzt1jrIFaYmBpSPvFoN9QuJ%2BwUt4HokaZ5eiTermmQDfFX%2B2pa%2Bb5QKDJrCMBq0w0ee6igl8ZVwZISSy%2F8rsYS9r9%2Bdl52%2FdrssgvQz4nN4effr23gcS5CyuLr&X-Amz-Signature=75fa2ad2278d47d44bd7b66d59dfede598a770d892a9cc73f54877d3c228a26e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3AZYHTG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBbeyNf04zgOc3M%2B6Av4qzstZ39tdchD42OFJkZhvEWaAiEAihFBMlFF%2BRp54l3wghdqebkSRqYOWg95XqaEWk0ynwgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBttZ%2BTFms6hA3tjUSrcAwzeb%2B7y1%2BczPu8%2ByNgclnZhLZL0SjUDrF6HaKJXrwAw91pylsBluYikoEd3LivgcVvj%2F6z6d%2FkjpWHpSTvjmJRMdPJziZl1eVsAyc4Or5UWBqoIwMS61EQ0X21vLjiaTWK3Z2QSQ99zzSu8hxvF7l5xyfMMgtZ%2FgIhVtdWVP%2FIuDGTcjl1XQakUOtEhOUac13lCQBZYu5bz7fc8wS4hXq0kkkI08rTzU9ipDPbXvEZFFmyEWUgsvWpcSU1j1kqZLGoStCdGsoL8FzYqHYeaBpK04%2BTKIk%2FrLr51b8Ibs9wvVTe5JGWlwyOkaQAJnFcJuNXqdj0O05sSdkKD4y48ZoZ23dr6zmjW%2BOMwxYlPX5dKqBGCyXRnpxhTKGUj%2FBfPxu%2FjTDZQiVwrDSk1iGa5AwIsOh4UkiUg%2FcIvDdW3i5qME3p0A75ib0Sq4xXI6%2BrbA18qH6a6%2BrkE5wfauS16CNMJG34cP5y1o8gPe64pCs3L3%2BxqNb4xvuKuJTp1r7I2ArHkLXfSl2MaI9ycDJERlbAdOFrpIbtJ7bVMK%2BwFd7mvNYwfkswyOfBlzJ%2FVZKVVczJ0r8isHG2149l27xArt3WMDZ2uvDj1tNOE4s%2B4qOyfC6nQIf70GWOeMi93ML%2FB%2FbwGOqUB8U3aQPNu7Y0cx7mZ7Jt2yg%2Bs%2F5wW%2BgNox9oaH7Qp8i%2FuKrX6UkWgyCrzqxgQcfvjdefejdq5Dls3tHMXhO4qJZbA%2FRHWhOZV6Zxzt1jrIFaYmBpSPvFoN9QuJ%2BwUt4HokaZ5eiTermmQDfFX%2B2pa%2Bb5QKDJrCMBq0w0ee6igl8ZVwZISSy%2F8rsYS9r9%2Bdl52%2FdrssgvQz4nN4effr23gcS5CyuLr&X-Amz-Signature=922aa7c40a7f17eb1825823b45251788e6258fe5c39129700f3114a43bc213a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GVGPMCW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkSxc2kE60ctibC28rZDcRcqYDw6X514Qk8KGHJA3t1wIgciwwPp5m8aAb9%2B4ADIHMNJweZtdwfOhUO6c2tu00WlkqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEQFG5%2BdAqYvy30W2CrcAwqzXHjI4bxxXwkiJ39lVBdIvmMCIic%2BCsBwNZp3%2F4uxMK49No7cZaBh7EeKje6Ku%2BQUJd4tLKd1OuFINtcGcqqG7KV4xWSAIVrgOWZ17OzYtThIt%2FO7tkeNcR%2Fh20w883aVFZ4OrKsTsNb%2F6CsM9rC1HGt6SKwt0UjCEplPLQ9MQNF0xc3sbae78sDUxL5HwA1uSEoNMW%2BGQK69mfi53v%2FTLy1LAo8y9V9WaPGt1TSbYxvFVSTAHcuZzmbbPO05pYO0pRzk7aW%2BUAmJMcSC0BOAsY6vM%2FF0lREwuImE2%2FGWefXjVE7oU3B1p3VB579sHajDodU5fiJJ%2FUPhta%2BZtSB7XpavLUxwN5jbx%2Bw%2B%2BhuSqU8UXpBNfSSJDyjJ%2Fp2NQmUoNhjsNtvBBOg%2BbhxuSK556LcWQmfbp6ZDhsa8sQvGEd4cAZQ1QQQdwtGc0xXtTdph%2Bv9lQU9yf5q%2FlFlqoZDO0hskT0V3pr3AZnjJaxDtd%2BtwXfmWDsUbMSCU%2BK%2BeFkfRvI0jL9CLwtd4O0g0oaCWSbjZBR%2BRCMwnDLgWO74i1c6I3Isrw%2B0BeuXU1vlODdMwQPMvHYUwhT6gXHcZkDiXoN%2BVppzQF1baEam3E3sqIC3KmqqQooMMeBAEMOTB%2FbwGOqUBUZLl8byXYSFUl0CBRkdGPtXNec9LF5Zh6TRqa%2FuFobfAt9bagBYLqDDOKVSAEDxz8MWhzlOSEukne95x7moNO4yFUfk5PQzmvZgdacjxRaqXaSR%2Blm4xc642pqor0AlaMu7ZGFZz1gt923dPF%2FNwIB4%2FpMViYg98t9gqg7T%2BqVP1m89zIS5WhefdZuSVjZ99QkWWr97ljmnUYHMOx8N6ck4Z%2B3Fr&X-Amz-Signature=fff746971ff5c99c6662d932a59aa0643e6d2360806630cb70b2a03aa9a3dafa&X-Amz-SignedHeaders=host&x-id=GetObject)
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