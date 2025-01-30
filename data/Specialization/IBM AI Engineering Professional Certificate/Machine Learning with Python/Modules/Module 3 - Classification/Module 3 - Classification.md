

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645J76GGV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuTU0lFytb%2F13lJHG7AscpQQiQkJMCIykESx16lZ7JeAiEAjjfLbrU%2BcWX6prozZFP%2Bs%2BmUir4vKtfME1hHyXBq4CcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BW3MkS4OddBHXk2SrcA%2BXXiGuIL9aYZsezO7tdP6Y1kdbW30xjJvp29E3mw%2FATLgkPfFbikz5sYO5x3wjGq0Xy6tbDOK78UxHCuZ0wma6HUeZmnMF0IfQVks3IlEDW6ZV4igGlM3idKfi0IlfFjU5g2JfN05oum30W8BI7a%2FAEqrgc1HXfcEQqOa28QIw5DE7ZUxOhbHYh5RiaBLJiqwgdTAb94iK0lQy6Z2KKeOrOtG1BRXWHp9dU%2BLa9hbnJ6sw367Uqy1QucJVFWZF0ujcMGRHIsd2lIvFvy8nmI5rPPyzPVj4QfCUX1QYvOwo0aTiMFODqUA4sp6zwhnl14MDUqGceLyVPYO4aBeiz%2FsGjttQYE%2FHPltTDsvtcSN8v%2FHM%2BcsWYWglFuU9W%2BYGGhZ2WHRlvjmPMnPvnsVj4l9pDbh%2BwNcZ5HbfT7q8fT4RLXaPN7G99g%2Fo3bJZFf%2BkRWgbSTMLyvTb9rGtcr5Y6%2F%2FY1g%2Fj3cXK%2BLwzOE2%2Bv1Rtp07ufmHDNiEMexiJ7%2BWCH4YCenHiV8MEhMvOofDzN01QqJgMIp1ZPnNUaKunOszT4U5HbFSApq16FI%2FGVa78TnUIabQks3i3EOnVVik%2BxMPTooqHfinUpTnctSwZEtfUW2qeCVv2PNJ7v5XLlMJ%2FP67wGOqUB4oYnNgdn9YNkyEWsunryX%2BCCT0QI7Rkc3L0rPRQ%2BEDu7%2BQOER%2B8WOgb8mI5lk8k9H5e%2FAlbKUA7FM%2FaqQ5sLnncZhh%2FaSiexZL1tC%2Ftv5Y3TAfD7q4AvXKjMQL5WzPOq5uMsbltdKwPsEjK2YgYIpdfeUOO2trz3DhavzrKNj2PV3mocXXjig1c%2FmepvK7JPee3QvK39SU8khXLs%2BJ4vsI%2BUESZs&X-Amz-Signature=f498dc8f8eea67a7e45e12c6fa327a7faa58b2104085b400434925349757685a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645J76GGV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuTU0lFytb%2F13lJHG7AscpQQiQkJMCIykESx16lZ7JeAiEAjjfLbrU%2BcWX6prozZFP%2Bs%2BmUir4vKtfME1hHyXBq4CcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BW3MkS4OddBHXk2SrcA%2BXXiGuIL9aYZsezO7tdP6Y1kdbW30xjJvp29E3mw%2FATLgkPfFbikz5sYO5x3wjGq0Xy6tbDOK78UxHCuZ0wma6HUeZmnMF0IfQVks3IlEDW6ZV4igGlM3idKfi0IlfFjU5g2JfN05oum30W8BI7a%2FAEqrgc1HXfcEQqOa28QIw5DE7ZUxOhbHYh5RiaBLJiqwgdTAb94iK0lQy6Z2KKeOrOtG1BRXWHp9dU%2BLa9hbnJ6sw367Uqy1QucJVFWZF0ujcMGRHIsd2lIvFvy8nmI5rPPyzPVj4QfCUX1QYvOwo0aTiMFODqUA4sp6zwhnl14MDUqGceLyVPYO4aBeiz%2FsGjttQYE%2FHPltTDsvtcSN8v%2FHM%2BcsWYWglFuU9W%2BYGGhZ2WHRlvjmPMnPvnsVj4l9pDbh%2BwNcZ5HbfT7q8fT4RLXaPN7G99g%2Fo3bJZFf%2BkRWgbSTMLyvTb9rGtcr5Y6%2F%2FY1g%2Fj3cXK%2BLwzOE2%2Bv1Rtp07ufmHDNiEMexiJ7%2BWCH4YCenHiV8MEhMvOofDzN01QqJgMIp1ZPnNUaKunOszT4U5HbFSApq16FI%2FGVa78TnUIabQks3i3EOnVVik%2BxMPTooqHfinUpTnctSwZEtfUW2qeCVv2PNJ7v5XLlMJ%2FP67wGOqUB4oYnNgdn9YNkyEWsunryX%2BCCT0QI7Rkc3L0rPRQ%2BEDu7%2BQOER%2B8WOgb8mI5lk8k9H5e%2FAlbKUA7FM%2FaqQ5sLnncZhh%2FaSiexZL1tC%2Ftv5Y3TAfD7q4AvXKjMQL5WzPOq5uMsbltdKwPsEjK2YgYIpdfeUOO2trz3DhavzrKNj2PV3mocXXjig1c%2FmepvK7JPee3QvK39SU8khXLs%2BJ4vsI%2BUESZs&X-Amz-Signature=cd7cc8d111b530d91abad58ebffeee70bf6904a1faa18f0d8c0c9286eaea604e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645J76GGV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuTU0lFytb%2F13lJHG7AscpQQiQkJMCIykESx16lZ7JeAiEAjjfLbrU%2BcWX6prozZFP%2Bs%2BmUir4vKtfME1hHyXBq4CcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BW3MkS4OddBHXk2SrcA%2BXXiGuIL9aYZsezO7tdP6Y1kdbW30xjJvp29E3mw%2FATLgkPfFbikz5sYO5x3wjGq0Xy6tbDOK78UxHCuZ0wma6HUeZmnMF0IfQVks3IlEDW6ZV4igGlM3idKfi0IlfFjU5g2JfN05oum30W8BI7a%2FAEqrgc1HXfcEQqOa28QIw5DE7ZUxOhbHYh5RiaBLJiqwgdTAb94iK0lQy6Z2KKeOrOtG1BRXWHp9dU%2BLa9hbnJ6sw367Uqy1QucJVFWZF0ujcMGRHIsd2lIvFvy8nmI5rPPyzPVj4QfCUX1QYvOwo0aTiMFODqUA4sp6zwhnl14MDUqGceLyVPYO4aBeiz%2FsGjttQYE%2FHPltTDsvtcSN8v%2FHM%2BcsWYWglFuU9W%2BYGGhZ2WHRlvjmPMnPvnsVj4l9pDbh%2BwNcZ5HbfT7q8fT4RLXaPN7G99g%2Fo3bJZFf%2BkRWgbSTMLyvTb9rGtcr5Y6%2F%2FY1g%2Fj3cXK%2BLwzOE2%2Bv1Rtp07ufmHDNiEMexiJ7%2BWCH4YCenHiV8MEhMvOofDzN01QqJgMIp1ZPnNUaKunOszT4U5HbFSApq16FI%2FGVa78TnUIabQks3i3EOnVVik%2BxMPTooqHfinUpTnctSwZEtfUW2qeCVv2PNJ7v5XLlMJ%2FP67wGOqUB4oYnNgdn9YNkyEWsunryX%2BCCT0QI7Rkc3L0rPRQ%2BEDu7%2BQOER%2B8WOgb8mI5lk8k9H5e%2FAlbKUA7FM%2FaqQ5sLnncZhh%2FaSiexZL1tC%2Ftv5Y3TAfD7q4AvXKjMQL5WzPOq5uMsbltdKwPsEjK2YgYIpdfeUOO2trz3DhavzrKNj2PV3mocXXjig1c%2FmepvK7JPee3QvK39SU8khXLs%2BJ4vsI%2BUESZs&X-Amz-Signature=38ac08a4af7c8015c761be76cbe48d57fbc19681c9415e7c5c20986fdae3be9c&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TOWF73X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDFIG4t2DgipTnZFGGsL9%2FAIzGytnDPls2C1NHdCtvITAiEAq2jLzDj8Gc9mw3EILT1ZkZ%2BuSiQXMZqgob3zAdp126oqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNdOmG0FWeVGQ8UibircA7NeXUUTjfho8o6%2Bx9pfkLXrjTXUw%2BkWGsmaA5rZKn7yvZo4SGpsOIFv%2BD6KCf%2FJhUAXZQE5PwpIA0ypizZukg7orEbIl%2FNuYIL09pieqMhx%2B2sBdyfW22QcqqZ9BASwa1Cp27NUj84lTJnpy9YvvkPC7zTtMe5FTCkB5MgFj6QX9M5CUccxC47yQyiT7bhR3XJPQdCbZnDArexuJbD%2Frvmz3PVDWiJ58Kdmaqr6T6B4pFOlYk%2ByeDBASitIkzLCxCmKs88WTYByIp85Fm56j%2BRSuWhmWS1GwhL9f4%2FxjwxBGpY4P7moDJVl%2Bpb58Tbj5wsxTqmY95S%2FrBx7kg%2BeQoXDVL8SDWEOnruOKU0b49amUNoNpVu6fDdIqNCoVcqxXCXvJKS3hE0G0wH%2B%2BLTE2qnsdqcfevtCzPxHLgVPqdrZWN5J45Ow0Yu4bUNGzWPmijKFzMvkMc8CQmJ6%2BZ7Dy2LerRXyM5AvCwQzrCVlFbweaCViHxR0CbmE%2BAuxNG1KIMQWXVqTcT5RMGhXghf%2FbasHPHcFYubTLQfz0JTmjfds%2BY8POw2rbaQo3a%2BnnG5LFy4TOU2NviyrfmM2C5AG4eyRWQqKfZNQ8hpE9%2FUYPThMtSu9ZVOaD1pOS0A9MKTO67wGOqUBUl4uwLj8tlv9RCeKUDrDyqhsWd5er0%2Bq%2B6ICxj0FZzXe4qVgoSYWnmpdcqriBlpydjhLGn%2BwlLHdH2%2FuEKXzN6VDa8ktcksJEEZ8HHZwmlYmfOhxVWy4uI1pl%2BmD%2BgjVHgHgX2Rzgwe35Sugb%2Bzl8EeKq7L%2B1xX0bSlGiZ4PSj4XFa6gpwu%2BBwQHWQb1djnysXlJQiEtoMZGHIGALsoSUcyW4Wuj&X-Amz-Signature=bba6447fa42af84edb6cd3718974a18a1a941ce5e198919db166d1b7a53c7104&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TOWF73X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDFIG4t2DgipTnZFGGsL9%2FAIzGytnDPls2C1NHdCtvITAiEAq2jLzDj8Gc9mw3EILT1ZkZ%2BuSiQXMZqgob3zAdp126oqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNdOmG0FWeVGQ8UibircA7NeXUUTjfho8o6%2Bx9pfkLXrjTXUw%2BkWGsmaA5rZKn7yvZo4SGpsOIFv%2BD6KCf%2FJhUAXZQE5PwpIA0ypizZukg7orEbIl%2FNuYIL09pieqMhx%2B2sBdyfW22QcqqZ9BASwa1Cp27NUj84lTJnpy9YvvkPC7zTtMe5FTCkB5MgFj6QX9M5CUccxC47yQyiT7bhR3XJPQdCbZnDArexuJbD%2Frvmz3PVDWiJ58Kdmaqr6T6B4pFOlYk%2ByeDBASitIkzLCxCmKs88WTYByIp85Fm56j%2BRSuWhmWS1GwhL9f4%2FxjwxBGpY4P7moDJVl%2Bpb58Tbj5wsxTqmY95S%2FrBx7kg%2BeQoXDVL8SDWEOnruOKU0b49amUNoNpVu6fDdIqNCoVcqxXCXvJKS3hE0G0wH%2B%2BLTE2qnsdqcfevtCzPxHLgVPqdrZWN5J45Ow0Yu4bUNGzWPmijKFzMvkMc8CQmJ6%2BZ7Dy2LerRXyM5AvCwQzrCVlFbweaCViHxR0CbmE%2BAuxNG1KIMQWXVqTcT5RMGhXghf%2FbasHPHcFYubTLQfz0JTmjfds%2BY8POw2rbaQo3a%2BnnG5LFy4TOU2NviyrfmM2C5AG4eyRWQqKfZNQ8hpE9%2FUYPThMtSu9ZVOaD1pOS0A9MKTO67wGOqUBUl4uwLj8tlv9RCeKUDrDyqhsWd5er0%2Bq%2B6ICxj0FZzXe4qVgoSYWnmpdcqriBlpydjhLGn%2BwlLHdH2%2FuEKXzN6VDa8ktcksJEEZ8HHZwmlYmfOhxVWy4uI1pl%2BmD%2BgjVHgHgX2Rzgwe35Sugb%2Bzl8EeKq7L%2B1xX0bSlGiZ4PSj4XFa6gpwu%2BBwQHWQb1djnysXlJQiEtoMZGHIGALsoSUcyW4Wuj&X-Amz-Signature=3ea4242e61b50e2a7c2dad544b579f24a260b535bf2cf6899992ec3b7ef3bce6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645J76GGV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBuTU0lFytb%2F13lJHG7AscpQQiQkJMCIykESx16lZ7JeAiEAjjfLbrU%2BcWX6prozZFP%2Bs%2BmUir4vKtfME1hHyXBq4CcqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BW3MkS4OddBHXk2SrcA%2BXXiGuIL9aYZsezO7tdP6Y1kdbW30xjJvp29E3mw%2FATLgkPfFbikz5sYO5x3wjGq0Xy6tbDOK78UxHCuZ0wma6HUeZmnMF0IfQVks3IlEDW6ZV4igGlM3idKfi0IlfFjU5g2JfN05oum30W8BI7a%2FAEqrgc1HXfcEQqOa28QIw5DE7ZUxOhbHYh5RiaBLJiqwgdTAb94iK0lQy6Z2KKeOrOtG1BRXWHp9dU%2BLa9hbnJ6sw367Uqy1QucJVFWZF0ujcMGRHIsd2lIvFvy8nmI5rPPyzPVj4QfCUX1QYvOwo0aTiMFODqUA4sp6zwhnl14MDUqGceLyVPYO4aBeiz%2FsGjttQYE%2FHPltTDsvtcSN8v%2FHM%2BcsWYWglFuU9W%2BYGGhZ2WHRlvjmPMnPvnsVj4l9pDbh%2BwNcZ5HbfT7q8fT4RLXaPN7G99g%2Fo3bJZFf%2BkRWgbSTMLyvTb9rGtcr5Y6%2F%2FY1g%2Fj3cXK%2BLwzOE2%2Bv1Rtp07ufmHDNiEMexiJ7%2BWCH4YCenHiV8MEhMvOofDzN01QqJgMIp1ZPnNUaKunOszT4U5HbFSApq16FI%2FGVa78TnUIabQks3i3EOnVVik%2BxMPTooqHfinUpTnctSwZEtfUW2qeCVv2PNJ7v5XLlMJ%2FP67wGOqUB4oYnNgdn9YNkyEWsunryX%2BCCT0QI7Rkc3L0rPRQ%2BEDu7%2BQOER%2B8WOgb8mI5lk8k9H5e%2FAlbKUA7FM%2FaqQ5sLnncZhh%2FaSiexZL1tC%2Ftv5Y3TAfD7q4AvXKjMQL5WzPOq5uMsbltdKwPsEjK2YgYIpdfeUOO2trz3DhavzrKNj2PV3mocXXjig1c%2FmepvK7JPee3QvK39SU8khXLs%2BJ4vsI%2BUESZs&X-Amz-Signature=a25c438b37342d8496cdd2864fcb251181e301d45d207227b8d7880fa192a82d&X-Amz-SignedHeaders=host&x-id=GetObject)
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