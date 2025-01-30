

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M66UUFH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2FjqA8TtMwPAKUDIZsAqDP8rfzX%2B35ybdTdzM0Bz3nFAiEAyJCY7YPrO%2FO%2BHbnbwlFrz0mh%2F8urFdk203nu8%2FvEJ3cqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDpmgKVKL4PEovJ2uircA%2FZfeUivHzXmsGcp0S5kLDrZXebTZHOOD084Q9zE8XRjdj4RMa65oE7PyKOWfun8s%2Bgunxi5r9agggfkmo94lBepzAi7NrWFFYvnBTp%2FDejIRXOxAwo9h8chmnqMsSXwzhWW%2BQexguLA2uYPcy2h8V%2BXIfD%2FZtjf0jmStiSP9QDQCZcm4YE%2BWpSyRsrJcRWbW84x0Ltdi1h6yVgovuQJsTYxCBACHJ%2B9mdXmz1cFuUYU9uWWRzJHu%2FWtp0jwXr3a38zq1uMVkbMsz42njDklylXnZieD2L%2Fh1vd3UDhedBzUS%2F0Li1sz1R6cLHgcMA53OYiE7zcHRzRzpdmaHm%2FqAsriqTq8cljUwD8x8t%2FGjP%2FC9KENFmGt0gw17h9BhsuK82eKGE1U3wlL%2F72DQPAR5kH2PS4aZCmYjEKptGt3cf0tMZIJWenucscz%2FBVWCMGybxX%2Fls9QeOWLPlaXWrv8yT%2BWqkfoONZNjrLWshjBdDC5WSDKM6MPmpmdtYJ%2BcY6LHvB1HR2jk9vpSeijZn9cGSESYz%2F2%2Bg5nZckDYxgiDQp%2Bxynb%2FJ%2BIn0dWJnouuJv5KtzKHn5SUbWYtXRLut3bsRccBT2HN6AYGX4sA65pQquinhhKtxb90SHbdN5IMNWX7rwGOqUBWI1IA0YtmoCm8GhhUyxJ%2FWhX2LyxnbXEDm9j5S6wmnrlgBZzFzJPzYE%2F4dG2VRB6%2B3Vwj%2FSb2KOENpRbqAPQLjqv8ICFQLZTWit0gMMy27%2F%2Bmzo0rEak4hL%2BoVPnVCsqf9VNXZRLt3fLbsohHGdTifDRg1UwvLTksXGz6%2Ba0qjNdRrICy4737CtV7J74t3CGTb5g7KxnGJQDsAtwiQbm0BOCqZGH&X-Amz-Signature=c5f9bd46a50bf109752744c15ae711acd6d1fa153358c73d3c1c4cde98f9a342&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M66UUFH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2FjqA8TtMwPAKUDIZsAqDP8rfzX%2B35ybdTdzM0Bz3nFAiEAyJCY7YPrO%2FO%2BHbnbwlFrz0mh%2F8urFdk203nu8%2FvEJ3cqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDpmgKVKL4PEovJ2uircA%2FZfeUivHzXmsGcp0S5kLDrZXebTZHOOD084Q9zE8XRjdj4RMa65oE7PyKOWfun8s%2Bgunxi5r9agggfkmo94lBepzAi7NrWFFYvnBTp%2FDejIRXOxAwo9h8chmnqMsSXwzhWW%2BQexguLA2uYPcy2h8V%2BXIfD%2FZtjf0jmStiSP9QDQCZcm4YE%2BWpSyRsrJcRWbW84x0Ltdi1h6yVgovuQJsTYxCBACHJ%2B9mdXmz1cFuUYU9uWWRzJHu%2FWtp0jwXr3a38zq1uMVkbMsz42njDklylXnZieD2L%2Fh1vd3UDhedBzUS%2F0Li1sz1R6cLHgcMA53OYiE7zcHRzRzpdmaHm%2FqAsriqTq8cljUwD8x8t%2FGjP%2FC9KENFmGt0gw17h9BhsuK82eKGE1U3wlL%2F72DQPAR5kH2PS4aZCmYjEKptGt3cf0tMZIJWenucscz%2FBVWCMGybxX%2Fls9QeOWLPlaXWrv8yT%2BWqkfoONZNjrLWshjBdDC5WSDKM6MPmpmdtYJ%2BcY6LHvB1HR2jk9vpSeijZn9cGSESYz%2F2%2Bg5nZckDYxgiDQp%2Bxynb%2FJ%2BIn0dWJnouuJv5KtzKHn5SUbWYtXRLut3bsRccBT2HN6AYGX4sA65pQquinhhKtxb90SHbdN5IMNWX7rwGOqUBWI1IA0YtmoCm8GhhUyxJ%2FWhX2LyxnbXEDm9j5S6wmnrlgBZzFzJPzYE%2F4dG2VRB6%2B3Vwj%2FSb2KOENpRbqAPQLjqv8ICFQLZTWit0gMMy27%2F%2Bmzo0rEak4hL%2BoVPnVCsqf9VNXZRLt3fLbsohHGdTifDRg1UwvLTksXGz6%2Ba0qjNdRrICy4737CtV7J74t3CGTb5g7KxnGJQDsAtwiQbm0BOCqZGH&X-Amz-Signature=99aee8bd656f9cb10f8169e678c277c973ac25c9958b5d2142ddd36ac0384052&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M66UUFH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2FjqA8TtMwPAKUDIZsAqDP8rfzX%2B35ybdTdzM0Bz3nFAiEAyJCY7YPrO%2FO%2BHbnbwlFrz0mh%2F8urFdk203nu8%2FvEJ3cqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDpmgKVKL4PEovJ2uircA%2FZfeUivHzXmsGcp0S5kLDrZXebTZHOOD084Q9zE8XRjdj4RMa65oE7PyKOWfun8s%2Bgunxi5r9agggfkmo94lBepzAi7NrWFFYvnBTp%2FDejIRXOxAwo9h8chmnqMsSXwzhWW%2BQexguLA2uYPcy2h8V%2BXIfD%2FZtjf0jmStiSP9QDQCZcm4YE%2BWpSyRsrJcRWbW84x0Ltdi1h6yVgovuQJsTYxCBACHJ%2B9mdXmz1cFuUYU9uWWRzJHu%2FWtp0jwXr3a38zq1uMVkbMsz42njDklylXnZieD2L%2Fh1vd3UDhedBzUS%2F0Li1sz1R6cLHgcMA53OYiE7zcHRzRzpdmaHm%2FqAsriqTq8cljUwD8x8t%2FGjP%2FC9KENFmGt0gw17h9BhsuK82eKGE1U3wlL%2F72DQPAR5kH2PS4aZCmYjEKptGt3cf0tMZIJWenucscz%2FBVWCMGybxX%2Fls9QeOWLPlaXWrv8yT%2BWqkfoONZNjrLWshjBdDC5WSDKM6MPmpmdtYJ%2BcY6LHvB1HR2jk9vpSeijZn9cGSESYz%2F2%2Bg5nZckDYxgiDQp%2Bxynb%2FJ%2BIn0dWJnouuJv5KtzKHn5SUbWYtXRLut3bsRccBT2HN6AYGX4sA65pQquinhhKtxb90SHbdN5IMNWX7rwGOqUBWI1IA0YtmoCm8GhhUyxJ%2FWhX2LyxnbXEDm9j5S6wmnrlgBZzFzJPzYE%2F4dG2VRB6%2B3Vwj%2FSb2KOENpRbqAPQLjqv8ICFQLZTWit0gMMy27%2F%2Bmzo0rEak4hL%2BoVPnVCsqf9VNXZRLt3fLbsohHGdTifDRg1UwvLTksXGz6%2Ba0qjNdRrICy4737CtV7J74t3CGTb5g7KxnGJQDsAtwiQbm0BOCqZGH&X-Amz-Signature=1b635a50e43896708f9e223f9597e58a01777b3cea5ff1f45625eaddfbe8966f&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632Y2TXVU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDPs9tUMg%2Fj%2FmmgWBEqX6TrKgnnrXiMzN9sZGFPOXxqNAiEAifwoSigtZ9MuuULHBrDYBr8hDvkLtWb93Ix9XP88kiYqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIwLgLR8yqrLtIMYzSrcA%2Bq5qtO0x5mp68IIPsIc8%2FaNqV7I8KRG5fri%2BbMTJosqAQQ3%2Buz0%2FC3sF0K9OIrSTLs%2Fz28TaJQRwvW6RHpidemKNKtA%2F5qc2%2BbtIHmyvb3SrDfvQPsFq%2FmXgyXgrzoCNz56DSG2njvIPceL0gnjyq%2Fx8yR%2Bk0xmpyGFQKDc2BmQToPpCLjn2DyQ5QWz2I%2BOSrp%2FUuF5BSqErNkT6727pAkeTaicdXgIIbfZMucNCo%2FRERVWzl9xRlQYH86sE8ilJMa%2B3qA3Wc1IYiG9Mpnv7Oj8UWm6BV2In5VfQUNm4lJUdIwV3Xm7R8BVLv3efvzZX52AUtAAsCILHR0mQvcNniykCofLd%2BMCHZ5uV1aprk%2FjgOjnsN5DUgFt5eeTx5QDH4rs0FRSYBUT6h9DQQgzBPkidtQNBNYp04DN3lwoS5v37Hc4mDEkz5ar7k44NvI2eJShz8j3T1f9EJePzYBiTxEju7JA0nwM7so9ZZXLBNml7hdtcT2Sfa5lGBzTDbDP3AObF3%2Bfs%2F6NFcOJgGfVdCiuDn%2F2JGXHPA2VlZjHQkjMHYwyrFS7QOew64v3iLmK65zcpSDARWkZ6mb6PNWBEZ%2Ba1rWHiLMzY57g%2FMo59cXJt2qvSK8QFcoN5HR%2BMOmX7rwGOqUB1m3FKffGq9pdZa81r1LK0F2aZ61vD%2FSTRIj%2Fh%2BXPUGKPyEcUd3nzztvfMfNlClaFmJ9jXnLoLe7UG1%2FAgho%2BtkhjV%2Bv5cSlAlh%2FeDVV73KMEknecRN6ylBBveWeRXjzd75dhCts3kwyFBXjijgHgirbHrDYjJOlmg93odJiUW0q3aNqn%2FSwWnLSJiVz%2BBIBNxwG3bs7W0iJ0RIXFpJoMRpWTJM97&X-Amz-Signature=2dba2b63fa2711509aa0be2b66ba5511f81a02049d49c670b92ed45d82e4a2c5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632Y2TXVU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDPs9tUMg%2Fj%2FmmgWBEqX6TrKgnnrXiMzN9sZGFPOXxqNAiEAifwoSigtZ9MuuULHBrDYBr8hDvkLtWb93Ix9XP88kiYqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIwLgLR8yqrLtIMYzSrcA%2Bq5qtO0x5mp68IIPsIc8%2FaNqV7I8KRG5fri%2BbMTJosqAQQ3%2Buz0%2FC3sF0K9OIrSTLs%2Fz28TaJQRwvW6RHpidemKNKtA%2F5qc2%2BbtIHmyvb3SrDfvQPsFq%2FmXgyXgrzoCNz56DSG2njvIPceL0gnjyq%2Fx8yR%2Bk0xmpyGFQKDc2BmQToPpCLjn2DyQ5QWz2I%2BOSrp%2FUuF5BSqErNkT6727pAkeTaicdXgIIbfZMucNCo%2FRERVWzl9xRlQYH86sE8ilJMa%2B3qA3Wc1IYiG9Mpnv7Oj8UWm6BV2In5VfQUNm4lJUdIwV3Xm7R8BVLv3efvzZX52AUtAAsCILHR0mQvcNniykCofLd%2BMCHZ5uV1aprk%2FjgOjnsN5DUgFt5eeTx5QDH4rs0FRSYBUT6h9DQQgzBPkidtQNBNYp04DN3lwoS5v37Hc4mDEkz5ar7k44NvI2eJShz8j3T1f9EJePzYBiTxEju7JA0nwM7so9ZZXLBNml7hdtcT2Sfa5lGBzTDbDP3AObF3%2Bfs%2F6NFcOJgGfVdCiuDn%2F2JGXHPA2VlZjHQkjMHYwyrFS7QOew64v3iLmK65zcpSDARWkZ6mb6PNWBEZ%2Ba1rWHiLMzY57g%2FMo59cXJt2qvSK8QFcoN5HR%2BMOmX7rwGOqUB1m3FKffGq9pdZa81r1LK0F2aZ61vD%2FSTRIj%2Fh%2BXPUGKPyEcUd3nzztvfMfNlClaFmJ9jXnLoLe7UG1%2FAgho%2BtkhjV%2Bv5cSlAlh%2FeDVV73KMEknecRN6ylBBveWeRXjzd75dhCts3kwyFBXjijgHgirbHrDYjJOlmg93odJiUW0q3aNqn%2FSwWnLSJiVz%2BBIBNxwG3bs7W0iJ0RIXFpJoMRpWTJM97&X-Amz-Signature=5d63112fcd94ed2c06ebeebd8d1dfc53ee1dc4cad6d6d4ae76f297e951ef2180&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M66UUFH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T161813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2FjqA8TtMwPAKUDIZsAqDP8rfzX%2B35ybdTdzM0Bz3nFAiEAyJCY7YPrO%2FO%2BHbnbwlFrz0mh%2F8urFdk203nu8%2FvEJ3cqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDpmgKVKL4PEovJ2uircA%2FZfeUivHzXmsGcp0S5kLDrZXebTZHOOD084Q9zE8XRjdj4RMa65oE7PyKOWfun8s%2Bgunxi5r9agggfkmo94lBepzAi7NrWFFYvnBTp%2FDejIRXOxAwo9h8chmnqMsSXwzhWW%2BQexguLA2uYPcy2h8V%2BXIfD%2FZtjf0jmStiSP9QDQCZcm4YE%2BWpSyRsrJcRWbW84x0Ltdi1h6yVgovuQJsTYxCBACHJ%2B9mdXmz1cFuUYU9uWWRzJHu%2FWtp0jwXr3a38zq1uMVkbMsz42njDklylXnZieD2L%2Fh1vd3UDhedBzUS%2F0Li1sz1R6cLHgcMA53OYiE7zcHRzRzpdmaHm%2FqAsriqTq8cljUwD8x8t%2FGjP%2FC9KENFmGt0gw17h9BhsuK82eKGE1U3wlL%2F72DQPAR5kH2PS4aZCmYjEKptGt3cf0tMZIJWenucscz%2FBVWCMGybxX%2Fls9QeOWLPlaXWrv8yT%2BWqkfoONZNjrLWshjBdDC5WSDKM6MPmpmdtYJ%2BcY6LHvB1HR2jk9vpSeijZn9cGSESYz%2F2%2Bg5nZckDYxgiDQp%2Bxynb%2FJ%2BIn0dWJnouuJv5KtzKHn5SUbWYtXRLut3bsRccBT2HN6AYGX4sA65pQquinhhKtxb90SHbdN5IMNWX7rwGOqUBWI1IA0YtmoCm8GhhUyxJ%2FWhX2LyxnbXEDm9j5S6wmnrlgBZzFzJPzYE%2F4dG2VRB6%2B3Vwj%2FSb2KOENpRbqAPQLjqv8ICFQLZTWit0gMMy27%2F%2Bmzo0rEak4hL%2BoVPnVCsqf9VNXZRLt3fLbsohHGdTifDRg1UwvLTksXGz6%2Ba0qjNdRrICy4737CtV7J74t3CGTb5g7KxnGJQDsAtwiQbm0BOCqZGH&X-Amz-Signature=638c3a866ad9928a048b88cb2db4767bd7b47dcf75641b9ddd326c7756cc9181&X-Amz-SignedHeaders=host&x-id=GetObject)
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