

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZN6AJFH4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlQqdyR4z0h9mrGGYCdEO3zwfPKdziS0OzsHjKgssXEwIgdit%2FvwBWbZnZunH0%2F4OoPu5M3%2Fbo1bj44Wtjrs6rUbsqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIAMOfagNInoqaOAeCrcAy6Xtv1zMoDSpwDnC49I4R3Z1xFF6YHep1T3KjTVSjkHq1cioM%2FfoOTNvnRQ0jQkj1u2yBsKSyuPW52fawzxGWB3K1Vb67sKDWDWxyHGMkstaAGnYHhvSFllCrj%2FaO%2BIhvQGMkomK9J9Q7BZwlpmauX7Cg6G%2BbddvUpl27w2UjxcRPzafJlRv1%2BKOY6RrIHbMAnX%2FgSzQj6TRxgVOpXRZwFLbUi6%2BjA63Bmm1Ytah84%2FGCHEddIQYuuJmTfZ6j5o8OxjrswZYoRk9V3fVUqIesWOQRC4IsYGJl9kZSW8Jr51x%2BrJ%2FdeGjtS4dN%2B11e1W1PHbC3gAOKXZzneGBuXuZMRD0XhIOWSH23ASEth42LrdA2jyzkkKEj9ExZWg7Qas0m6nizWPl2VqCxUFa5o5XcvMxTawxghjTojxJaYD6ADP%2FgveOvpYn3yzSECoVQ5mbnEhM1Ijp84iDgHRSKErH0LbRcrndG9%2FLV3%2Fo%2FN%2Bc3B1YNfofSbYeSBwgXPdU1gXjmWGV5tGImMdmOik9qF%2FtRc8q%2BVgGox5XoD%2F9c2pSfJtT3ZkoypZZzgq9uRCOBr7olFl4HuXd%2BNRhJWdUcoGceicDlAr65ZkTCT0bjitMWhidJjIdVK%2F2EcC0e5jMMbh77wGOqUBfxXzf3Tz8S%2FwGE%2F3sVUQ5tmnSzVElTVWNpzS4Hi5%2BgiClh13mn1UrlZS5cQMBssZLr9fL69BJgD5T%2BLZynRgREhmDVwAw3PdUGoeHsX9W4lZ2VmSaGz6pzbQFnr9fymC9JuNP1pg6szDY6vN5PEzdvWg4zbCekWl9ipx%2Bz8SRKwFsy0lXJm1%2FTPUbHuRbVIl2cATjuraY5JwVfk1i%2BtO8ZGqKHN7&X-Amz-Signature=e123c1c0a406a7ec43a1d1b39c449062a9e7d5844c4954d3f0fe3c669045a6e1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZN6AJFH4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlQqdyR4z0h9mrGGYCdEO3zwfPKdziS0OzsHjKgssXEwIgdit%2FvwBWbZnZunH0%2F4OoPu5M3%2Fbo1bj44Wtjrs6rUbsqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIAMOfagNInoqaOAeCrcAy6Xtv1zMoDSpwDnC49I4R3Z1xFF6YHep1T3KjTVSjkHq1cioM%2FfoOTNvnRQ0jQkj1u2yBsKSyuPW52fawzxGWB3K1Vb67sKDWDWxyHGMkstaAGnYHhvSFllCrj%2FaO%2BIhvQGMkomK9J9Q7BZwlpmauX7Cg6G%2BbddvUpl27w2UjxcRPzafJlRv1%2BKOY6RrIHbMAnX%2FgSzQj6TRxgVOpXRZwFLbUi6%2BjA63Bmm1Ytah84%2FGCHEddIQYuuJmTfZ6j5o8OxjrswZYoRk9V3fVUqIesWOQRC4IsYGJl9kZSW8Jr51x%2BrJ%2FdeGjtS4dN%2B11e1W1PHbC3gAOKXZzneGBuXuZMRD0XhIOWSH23ASEth42LrdA2jyzkkKEj9ExZWg7Qas0m6nizWPl2VqCxUFa5o5XcvMxTawxghjTojxJaYD6ADP%2FgveOvpYn3yzSECoVQ5mbnEhM1Ijp84iDgHRSKErH0LbRcrndG9%2FLV3%2Fo%2FN%2Bc3B1YNfofSbYeSBwgXPdU1gXjmWGV5tGImMdmOik9qF%2FtRc8q%2BVgGox5XoD%2F9c2pSfJtT3ZkoypZZzgq9uRCOBr7olFl4HuXd%2BNRhJWdUcoGceicDlAr65ZkTCT0bjitMWhidJjIdVK%2F2EcC0e5jMMbh77wGOqUBfxXzf3Tz8S%2FwGE%2F3sVUQ5tmnSzVElTVWNpzS4Hi5%2BgiClh13mn1UrlZS5cQMBssZLr9fL69BJgD5T%2BLZynRgREhmDVwAw3PdUGoeHsX9W4lZ2VmSaGz6pzbQFnr9fymC9JuNP1pg6szDY6vN5PEzdvWg4zbCekWl9ipx%2Bz8SRKwFsy0lXJm1%2FTPUbHuRbVIl2cATjuraY5JwVfk1i%2BtO8ZGqKHN7&X-Amz-Signature=48512e8ab6df4af0421567bf4eb157b165e4f50404af5c10d20ba4113950a29e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZN6AJFH4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlQqdyR4z0h9mrGGYCdEO3zwfPKdziS0OzsHjKgssXEwIgdit%2FvwBWbZnZunH0%2F4OoPu5M3%2Fbo1bj44Wtjrs6rUbsqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIAMOfagNInoqaOAeCrcAy6Xtv1zMoDSpwDnC49I4R3Z1xFF6YHep1T3KjTVSjkHq1cioM%2FfoOTNvnRQ0jQkj1u2yBsKSyuPW52fawzxGWB3K1Vb67sKDWDWxyHGMkstaAGnYHhvSFllCrj%2FaO%2BIhvQGMkomK9J9Q7BZwlpmauX7Cg6G%2BbddvUpl27w2UjxcRPzafJlRv1%2BKOY6RrIHbMAnX%2FgSzQj6TRxgVOpXRZwFLbUi6%2BjA63Bmm1Ytah84%2FGCHEddIQYuuJmTfZ6j5o8OxjrswZYoRk9V3fVUqIesWOQRC4IsYGJl9kZSW8Jr51x%2BrJ%2FdeGjtS4dN%2B11e1W1PHbC3gAOKXZzneGBuXuZMRD0XhIOWSH23ASEth42LrdA2jyzkkKEj9ExZWg7Qas0m6nizWPl2VqCxUFa5o5XcvMxTawxghjTojxJaYD6ADP%2FgveOvpYn3yzSECoVQ5mbnEhM1Ijp84iDgHRSKErH0LbRcrndG9%2FLV3%2Fo%2FN%2Bc3B1YNfofSbYeSBwgXPdU1gXjmWGV5tGImMdmOik9qF%2FtRc8q%2BVgGox5XoD%2F9c2pSfJtT3ZkoypZZzgq9uRCOBr7olFl4HuXd%2BNRhJWdUcoGceicDlAr65ZkTCT0bjitMWhidJjIdVK%2F2EcC0e5jMMbh77wGOqUBfxXzf3Tz8S%2FwGE%2F3sVUQ5tmnSzVElTVWNpzS4Hi5%2BgiClh13mn1UrlZS5cQMBssZLr9fL69BJgD5T%2BLZynRgREhmDVwAw3PdUGoeHsX9W4lZ2VmSaGz6pzbQFnr9fymC9JuNP1pg6szDY6vN5PEzdvWg4zbCekWl9ipx%2Bz8SRKwFsy0lXJm1%2FTPUbHuRbVIl2cATjuraY5JwVfk1i%2BtO8ZGqKHN7&X-Amz-Signature=0551d5adf971d230856b0dd6d35b1442021ddffbd46a047756c25fb97b6deee5&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIQMTIBQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCptvXvi4zKFthpYn7XQtc2zLQsx6kUJAruBmIEGYrfywIgP5KiqE2FfGDZDdGzEj8JTHpF0kBo4VhVX1%2BKk3HCbUwqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK9pWXWvR%2Bs2Ko0c7SrcA9Pqvw04JoFw2JSJs%2FRbJDYJcQMp4oQkBQLL22zbQ61Fa5EWnYnkE%2BspzlZo6oWtQ2qn6cV0C2XK7XmeXsugINUN1pM6RCDer1vJwo2CkxVW7LH5R91vjdsIEAWmGnDkN5w3wIPWH2r6BZCaC71E6LImF4MCZCBVadc6AXF5EtX260yvEbzEfyaSgjs18b9U4y8Qf7RwRMEDPizM8QI4L2Z006d%2Fhfiid1wX8%2B8BBVt%2B2cXOhhP6EDaGhDdTgaorP6KIsoysMWCv3hqrpC8%2FrFA%2BjN7omwpDUta81PVoLUTIs%2Fb8dt3%2FyvV7sYMvuBAgneyTJZrkJ4vP0Q%2BzcZid3hsDBy5ysTUlzTcu5ewoNeZX4x6O1a%2FOeTakN9%2FRCC1M3LDgCOqU%2BOm3YF4l20YgUg598deVtbyIJSzwfa53BftsWrzG1Wx8V98sAJUM887bnYd%2FXtf%2BEwBiqs8UGXrS8XMtyeHBfrZX6M3tG%2FJqfaEASbSAfIJUI29Bj36b4FK0LQzJWy5oTXNGL2ccMg2NBCEmtPoDwTIOoaZJFQ%2BtFzDFEm3a%2BQtDD4ZM1LRjAcnPQQwIfpI8tAW5Tj0Vz%2BvZzE%2F404NR%2FqV7NfI%2BPVZitaJitmSbzS6R4IupkrXNMNDh77wGOqUBvnxgAhoVKoXXlFQ02y%2FD%2BPLrCuS3ge84FX%2B5JhoNBfFBWL%2BkTghr4uQrzx2C6mHYd1vs1sBpcimlI7I26DDxewZ7h4YDonLoDipI%2BgP%2FsOzOxNqs6MqtAiLxVvbuM7rAr%2F1rb8tAeY7A2UOWnpDX0kh6cZ%2BqBrWiZaQ3SX0zUKlSkdzfxLINR4wpzV02ffKeDxbu7Y%2FUvoKzywBNfZa29MBrOI1Y&X-Amz-Signature=0a3f9484b1df87fa0a37f61c7671fbf143062207967c9b5971fb5edccfb3449b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIQMTIBQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCptvXvi4zKFthpYn7XQtc2zLQsx6kUJAruBmIEGYrfywIgP5KiqE2FfGDZDdGzEj8JTHpF0kBo4VhVX1%2BKk3HCbUwqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK9pWXWvR%2Bs2Ko0c7SrcA9Pqvw04JoFw2JSJs%2FRbJDYJcQMp4oQkBQLL22zbQ61Fa5EWnYnkE%2BspzlZo6oWtQ2qn6cV0C2XK7XmeXsugINUN1pM6RCDer1vJwo2CkxVW7LH5R91vjdsIEAWmGnDkN5w3wIPWH2r6BZCaC71E6LImF4MCZCBVadc6AXF5EtX260yvEbzEfyaSgjs18b9U4y8Qf7RwRMEDPizM8QI4L2Z006d%2Fhfiid1wX8%2B8BBVt%2B2cXOhhP6EDaGhDdTgaorP6KIsoysMWCv3hqrpC8%2FrFA%2BjN7omwpDUta81PVoLUTIs%2Fb8dt3%2FyvV7sYMvuBAgneyTJZrkJ4vP0Q%2BzcZid3hsDBy5ysTUlzTcu5ewoNeZX4x6O1a%2FOeTakN9%2FRCC1M3LDgCOqU%2BOm3YF4l20YgUg598deVtbyIJSzwfa53BftsWrzG1Wx8V98sAJUM887bnYd%2FXtf%2BEwBiqs8UGXrS8XMtyeHBfrZX6M3tG%2FJqfaEASbSAfIJUI29Bj36b4FK0LQzJWy5oTXNGL2ccMg2NBCEmtPoDwTIOoaZJFQ%2BtFzDFEm3a%2BQtDD4ZM1LRjAcnPQQwIfpI8tAW5Tj0Vz%2BvZzE%2F404NR%2FqV7NfI%2BPVZitaJitmSbzS6R4IupkrXNMNDh77wGOqUBvnxgAhoVKoXXlFQ02y%2FD%2BPLrCuS3ge84FX%2B5JhoNBfFBWL%2BkTghr4uQrzx2C6mHYd1vs1sBpcimlI7I26DDxewZ7h4YDonLoDipI%2BgP%2FsOzOxNqs6MqtAiLxVvbuM7rAr%2F1rb8tAeY7A2UOWnpDX0kh6cZ%2BqBrWiZaQ3SX0zUKlSkdzfxLINR4wpzV02ffKeDxbu7Y%2FUvoKzywBNfZa29MBrOI1Y&X-Amz-Signature=756de7353cda26640e7737f1ba762676639ce2f875648cce0e4a9541ee13bfc5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZN6AJFH4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlQqdyR4z0h9mrGGYCdEO3zwfPKdziS0OzsHjKgssXEwIgdit%2FvwBWbZnZunH0%2F4OoPu5M3%2Fbo1bj44Wtjrs6rUbsqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIAMOfagNInoqaOAeCrcAy6Xtv1zMoDSpwDnC49I4R3Z1xFF6YHep1T3KjTVSjkHq1cioM%2FfoOTNvnRQ0jQkj1u2yBsKSyuPW52fawzxGWB3K1Vb67sKDWDWxyHGMkstaAGnYHhvSFllCrj%2FaO%2BIhvQGMkomK9J9Q7BZwlpmauX7Cg6G%2BbddvUpl27w2UjxcRPzafJlRv1%2BKOY6RrIHbMAnX%2FgSzQj6TRxgVOpXRZwFLbUi6%2BjA63Bmm1Ytah84%2FGCHEddIQYuuJmTfZ6j5o8OxjrswZYoRk9V3fVUqIesWOQRC4IsYGJl9kZSW8Jr51x%2BrJ%2FdeGjtS4dN%2B11e1W1PHbC3gAOKXZzneGBuXuZMRD0XhIOWSH23ASEth42LrdA2jyzkkKEj9ExZWg7Qas0m6nizWPl2VqCxUFa5o5XcvMxTawxghjTojxJaYD6ADP%2FgveOvpYn3yzSECoVQ5mbnEhM1Ijp84iDgHRSKErH0LbRcrndG9%2FLV3%2Fo%2FN%2Bc3B1YNfofSbYeSBwgXPdU1gXjmWGV5tGImMdmOik9qF%2FtRc8q%2BVgGox5XoD%2F9c2pSfJtT3ZkoypZZzgq9uRCOBr7olFl4HuXd%2BNRhJWdUcoGceicDlAr65ZkTCT0bjitMWhidJjIdVK%2F2EcC0e5jMMbh77wGOqUBfxXzf3Tz8S%2FwGE%2F3sVUQ5tmnSzVElTVWNpzS4Hi5%2BgiClh13mn1UrlZS5cQMBssZLr9fL69BJgD5T%2BLZynRgREhmDVwAw3PdUGoeHsX9W4lZ2VmSaGz6pzbQFnr9fymC9JuNP1pg6szDY6vN5PEzdvWg4zbCekWl9ipx%2Bz8SRKwFsy0lXJm1%2FTPUbHuRbVIl2cATjuraY5JwVfk1i%2BtO8ZGqKHN7&X-Amz-Signature=d0954d6d31ea2b108865f046ab6c684a787d82bac3479711001dff48d7a1de56&X-Amz-SignedHeaders=host&x-id=GetObject)
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