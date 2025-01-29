

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XFYAFY2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIH4THewt%2BN7EZ823kUVJ52V1c2fg8WHMuKcyabeiATr%2BAiEA4yI8eHsR8QM7hZH8pUmcHf4r4V50PYD2eeLtf2atL2cqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdRe5npzS%2FMKzoZgircA8jKAuSQyvZSoxuY%2FjFe7bQhvS%2BEhh3Y4dQzkAqCd8chdQDICl%2BYxciwDzr6500g5C4fj2EiGIxMYkYmqu1x9%2BFyCsgFWnHgTCEKrqOgoT%2BFNFD4fbCIFwGQxLEP5aOaZOkYwrxVfZi0MMPrWng602862Bbcd%2BAqi11JdTGzckdwpHNMaKvzdm%2BKoecbDkDZYdcBn0N2apAQ7dJdSQLFqT1Rv%2BS%2F6cff%2F%2BMxkdU8w8Vv5fHTKM9aiqKGqcb9rdqLUJh5m0smwzD1WMqYHB%2BmLy0JOTALLG99MMvOlmI9e4xquaX9OiP3tUlnj4MBfFt9LZISelivBix20I7BjIjb%2FWyuDe4s%2F3YTxJHM%2BGo8KDYUv%2F5X274w1lcUKsDAgWZGcbhZOf5yLRit1uxse8%2FyMm9c%2FR6I1KOIrA2vjaonZNnPJEcUyFm3HjI4IVWuYGZb7TW0iA%2FXfBgcAVxnZOYIOqk7yW4r%2FCA%2Ft7tLihon1iCxhpgoZLcmeWYaMbGRkSP1FCugl5WQebRcjsPYB%2BQmOrzAJqzJKa4ArA0MKnFoUaxhYNA%2BX8LzN%2FhHfrB8XDgx4PbgFGzoPBhKJqPs21IspXetmFXlAfXsIfnhBePlhkFJUuNVxzaaoDqrBocmMIi75rwGOqUBFhHpp0qJNPE0zupN1IxyzxEU5y5jspGZg%2BAIsH00gERge2aB1PAQySr2Y4LtdQXxccSnfMAozvMKA6XJrcLygnwxnJ4cSacCo4asoz1s%2BrBKJBrwSybAy1qWsO92%2F4w2AXc28t9SLvwnbUfKD3xUFA8ZLt8G62jVUmmpIKj%2BiKvh04FZgYea07XlniwMFOOSev7KcU1LHeaKm0TbUKp8O8GQiPEx&X-Amz-Signature=90abb0c314ad1ffd7e84afabb51968702fecd9f3b8d72e5137be21c0246940f1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XFYAFY2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIH4THewt%2BN7EZ823kUVJ52V1c2fg8WHMuKcyabeiATr%2BAiEA4yI8eHsR8QM7hZH8pUmcHf4r4V50PYD2eeLtf2atL2cqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdRe5npzS%2FMKzoZgircA8jKAuSQyvZSoxuY%2FjFe7bQhvS%2BEhh3Y4dQzkAqCd8chdQDICl%2BYxciwDzr6500g5C4fj2EiGIxMYkYmqu1x9%2BFyCsgFWnHgTCEKrqOgoT%2BFNFD4fbCIFwGQxLEP5aOaZOkYwrxVfZi0MMPrWng602862Bbcd%2BAqi11JdTGzckdwpHNMaKvzdm%2BKoecbDkDZYdcBn0N2apAQ7dJdSQLFqT1Rv%2BS%2F6cff%2F%2BMxkdU8w8Vv5fHTKM9aiqKGqcb9rdqLUJh5m0smwzD1WMqYHB%2BmLy0JOTALLG99MMvOlmI9e4xquaX9OiP3tUlnj4MBfFt9LZISelivBix20I7BjIjb%2FWyuDe4s%2F3YTxJHM%2BGo8KDYUv%2F5X274w1lcUKsDAgWZGcbhZOf5yLRit1uxse8%2FyMm9c%2FR6I1KOIrA2vjaonZNnPJEcUyFm3HjI4IVWuYGZb7TW0iA%2FXfBgcAVxnZOYIOqk7yW4r%2FCA%2Ft7tLihon1iCxhpgoZLcmeWYaMbGRkSP1FCugl5WQebRcjsPYB%2BQmOrzAJqzJKa4ArA0MKnFoUaxhYNA%2BX8LzN%2FhHfrB8XDgx4PbgFGzoPBhKJqPs21IspXetmFXlAfXsIfnhBePlhkFJUuNVxzaaoDqrBocmMIi75rwGOqUBFhHpp0qJNPE0zupN1IxyzxEU5y5jspGZg%2BAIsH00gERge2aB1PAQySr2Y4LtdQXxccSnfMAozvMKA6XJrcLygnwxnJ4cSacCo4asoz1s%2BrBKJBrwSybAy1qWsO92%2F4w2AXc28t9SLvwnbUfKD3xUFA8ZLt8G62jVUmmpIKj%2BiKvh04FZgYea07XlniwMFOOSev7KcU1LHeaKm0TbUKp8O8GQiPEx&X-Amz-Signature=40e371e8c03b11fa9222ed902631a91c8343cc92f12f5864cc7e2e2e614c7aa8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XFYAFY2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIH4THewt%2BN7EZ823kUVJ52V1c2fg8WHMuKcyabeiATr%2BAiEA4yI8eHsR8QM7hZH8pUmcHf4r4V50PYD2eeLtf2atL2cqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdRe5npzS%2FMKzoZgircA8jKAuSQyvZSoxuY%2FjFe7bQhvS%2BEhh3Y4dQzkAqCd8chdQDICl%2BYxciwDzr6500g5C4fj2EiGIxMYkYmqu1x9%2BFyCsgFWnHgTCEKrqOgoT%2BFNFD4fbCIFwGQxLEP5aOaZOkYwrxVfZi0MMPrWng602862Bbcd%2BAqi11JdTGzckdwpHNMaKvzdm%2BKoecbDkDZYdcBn0N2apAQ7dJdSQLFqT1Rv%2BS%2F6cff%2F%2BMxkdU8w8Vv5fHTKM9aiqKGqcb9rdqLUJh5m0smwzD1WMqYHB%2BmLy0JOTALLG99MMvOlmI9e4xquaX9OiP3tUlnj4MBfFt9LZISelivBix20I7BjIjb%2FWyuDe4s%2F3YTxJHM%2BGo8KDYUv%2F5X274w1lcUKsDAgWZGcbhZOf5yLRit1uxse8%2FyMm9c%2FR6I1KOIrA2vjaonZNnPJEcUyFm3HjI4IVWuYGZb7TW0iA%2FXfBgcAVxnZOYIOqk7yW4r%2FCA%2Ft7tLihon1iCxhpgoZLcmeWYaMbGRkSP1FCugl5WQebRcjsPYB%2BQmOrzAJqzJKa4ArA0MKnFoUaxhYNA%2BX8LzN%2FhHfrB8XDgx4PbgFGzoPBhKJqPs21IspXetmFXlAfXsIfnhBePlhkFJUuNVxzaaoDqrBocmMIi75rwGOqUBFhHpp0qJNPE0zupN1IxyzxEU5y5jspGZg%2BAIsH00gERge2aB1PAQySr2Y4LtdQXxccSnfMAozvMKA6XJrcLygnwxnJ4cSacCo4asoz1s%2BrBKJBrwSybAy1qWsO92%2F4w2AXc28t9SLvwnbUfKD3xUFA8ZLt8G62jVUmmpIKj%2BiKvh04FZgYea07XlniwMFOOSev7KcU1LHeaKm0TbUKp8O8GQiPEx&X-Amz-Signature=bde60acd7163a021b9bb35f5720a7ac42545b8565593666350cc96db863c8018&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQ65I74E%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCID6ZFHdt%2FfLPsjtY9QJGYR5AZKOhmBmL4%2B%2FqlxBWyUS9AiAX10BgT%2F%2FQy5Ka%2FaSKAznFqp%2FSNE%2Fhe5iDd3Cqzb467SqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMihAa4Sw0IphRAfoFKtwDp6mT%2BbxlnHsUu%2BuaL53Np4hyTXJOgzPTC3ustarB3pGgHIyq1%2Fh34bdQVr1QCjVTS4HFovRK0XISAUYQmzk8W0zVDJYKHpj0p6RsvTVWuDblQ9z1GH04hOfPLvyKF9Y4MJOIL3YM9FTfWTMgJvzcLvfy6aYvJSwq4wDTlGPPuAVi3Ow2xt2Kxah%2FrYUv0t%2BVwAtuZzb3VZNyQkY8xQMG12GDnSdBojIufNL68OLXyedMBib9WH2GcQFhGTgYd3eVb1vdcSddgfrftlZ%2F64c8cGcWNYw0P19Vq756KMX70NESsrFUkrg0s%2FZNMLujaPA1179W%2F6ERrxQ8aSArtMvTRQHxWNnXAOQiOA3o15MSm3NhFo5rpaZYNwO67pbb03cli068Crpy9jA4mcMRlBDnJ4KNQO57T3gbhgqkdK3OCVf80q7Emp6vyjYZ4BLCSAHCTyML%2F8O33cTVMEImLgWwXWZE9Re9vBbN%2FsAFTFiNYZrSe5TCvdZtfEZnvUwPmfKKSfpDyGZD0BCS4sf1RrHvDHCJzujBLnmTMKacWy5UZqJl%2BK49NoT7SlQFXf%2BnzmMxuIb94HiPWtGhYMyrSkuKBKT4fMo9HtjLbercq4x73e%2BLqa28kwaONSlxoXgwrrvmvAY6pgHojqdmrCi1SAGNGibuK%2BCAw4Yj4KSX0R60PTk1byXNHQj6Ok%2Fc%2FR%2BBG4AoFnKosZGwHv6ZtHuhUGWFhwENkj9%2F7FIwam4bk5fqZpqdrrbUWcNAkONfj5DyOYLjmamz%2BfwUK4ClOc53SGmQYVbV7pxaR2HMhyLtC%2FAfamXzgZxQIOZT2XzrojPPMVrIF4IDdshlTv4H1eo1zJG6ZqAUYDgWR%2BJ7ZCLo&X-Amz-Signature=6cd543ac9af28b1d062ada7ad99ba70aa8d3a392a672b7dba096bdaac4802560&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQ65I74E%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCID6ZFHdt%2FfLPsjtY9QJGYR5AZKOhmBmL4%2B%2FqlxBWyUS9AiAX10BgT%2F%2FQy5Ka%2FaSKAznFqp%2FSNE%2Fhe5iDd3Cqzb467SqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMihAa4Sw0IphRAfoFKtwDp6mT%2BbxlnHsUu%2BuaL53Np4hyTXJOgzPTC3ustarB3pGgHIyq1%2Fh34bdQVr1QCjVTS4HFovRK0XISAUYQmzk8W0zVDJYKHpj0p6RsvTVWuDblQ9z1GH04hOfPLvyKF9Y4MJOIL3YM9FTfWTMgJvzcLvfy6aYvJSwq4wDTlGPPuAVi3Ow2xt2Kxah%2FrYUv0t%2BVwAtuZzb3VZNyQkY8xQMG12GDnSdBojIufNL68OLXyedMBib9WH2GcQFhGTgYd3eVb1vdcSddgfrftlZ%2F64c8cGcWNYw0P19Vq756KMX70NESsrFUkrg0s%2FZNMLujaPA1179W%2F6ERrxQ8aSArtMvTRQHxWNnXAOQiOA3o15MSm3NhFo5rpaZYNwO67pbb03cli068Crpy9jA4mcMRlBDnJ4KNQO57T3gbhgqkdK3OCVf80q7Emp6vyjYZ4BLCSAHCTyML%2F8O33cTVMEImLgWwXWZE9Re9vBbN%2FsAFTFiNYZrSe5TCvdZtfEZnvUwPmfKKSfpDyGZD0BCS4sf1RrHvDHCJzujBLnmTMKacWy5UZqJl%2BK49NoT7SlQFXf%2BnzmMxuIb94HiPWtGhYMyrSkuKBKT4fMo9HtjLbercq4x73e%2BLqa28kwaONSlxoXgwrrvmvAY6pgHojqdmrCi1SAGNGibuK%2BCAw4Yj4KSX0R60PTk1byXNHQj6Ok%2Fc%2FR%2BBG4AoFnKosZGwHv6ZtHuhUGWFhwENkj9%2F7FIwam4bk5fqZpqdrrbUWcNAkONfj5DyOYLjmamz%2BfwUK4ClOc53SGmQYVbV7pxaR2HMhyLtC%2FAfamXzgZxQIOZT2XzrojPPMVrIF4IDdshlTv4H1eo1zJG6ZqAUYDgWR%2BJ7ZCLo&X-Amz-Signature=975ab1929e9b4c9925d25ee500ea6d2c4b2948d2c1e14b9325978bead27deef3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XFYAFY2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIH4THewt%2BN7EZ823kUVJ52V1c2fg8WHMuKcyabeiATr%2BAiEA4yI8eHsR8QM7hZH8pUmcHf4r4V50PYD2eeLtf2atL2cqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdRe5npzS%2FMKzoZgircA8jKAuSQyvZSoxuY%2FjFe7bQhvS%2BEhh3Y4dQzkAqCd8chdQDICl%2BYxciwDzr6500g5C4fj2EiGIxMYkYmqu1x9%2BFyCsgFWnHgTCEKrqOgoT%2BFNFD4fbCIFwGQxLEP5aOaZOkYwrxVfZi0MMPrWng602862Bbcd%2BAqi11JdTGzckdwpHNMaKvzdm%2BKoecbDkDZYdcBn0N2apAQ7dJdSQLFqT1Rv%2BS%2F6cff%2F%2BMxkdU8w8Vv5fHTKM9aiqKGqcb9rdqLUJh5m0smwzD1WMqYHB%2BmLy0JOTALLG99MMvOlmI9e4xquaX9OiP3tUlnj4MBfFt9LZISelivBix20I7BjIjb%2FWyuDe4s%2F3YTxJHM%2BGo8KDYUv%2F5X274w1lcUKsDAgWZGcbhZOf5yLRit1uxse8%2FyMm9c%2FR6I1KOIrA2vjaonZNnPJEcUyFm3HjI4IVWuYGZb7TW0iA%2FXfBgcAVxnZOYIOqk7yW4r%2FCA%2Ft7tLihon1iCxhpgoZLcmeWYaMbGRkSP1FCugl5WQebRcjsPYB%2BQmOrzAJqzJKa4ArA0MKnFoUaxhYNA%2BX8LzN%2FhHfrB8XDgx4PbgFGzoPBhKJqPs21IspXetmFXlAfXsIfnhBePlhkFJUuNVxzaaoDqrBocmMIi75rwGOqUBFhHpp0qJNPE0zupN1IxyzxEU5y5jspGZg%2BAIsH00gERge2aB1PAQySr2Y4LtdQXxccSnfMAozvMKA6XJrcLygnwxnJ4cSacCo4asoz1s%2BrBKJBrwSybAy1qWsO92%2F4w2AXc28t9SLvwnbUfKD3xUFA8ZLt8G62jVUmmpIKj%2BiKvh04FZgYea07XlniwMFOOSev7KcU1LHeaKm0TbUKp8O8GQiPEx&X-Amz-Signature=3a0d673550fc23cf1fad180e8c8d11d724ff59013daa77a43ac516a024da45a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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