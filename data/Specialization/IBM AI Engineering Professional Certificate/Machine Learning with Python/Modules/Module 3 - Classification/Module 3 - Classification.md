

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662H4OBHT3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWZyQzdn6b3wi2cO5H1aalkMCV9X%2Bq2D1Vm3ahNqf16AiEA%2BxZZmd4nIgxKIx6bYSz6Qk42h1cbvx%2B%2B5lgR12RFH%2F4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEphbzooPJs5IcZSlSrcA%2BxkN90h7bispxWrTdOSxzPVnqEow6S6mZDPkNSLmZgsRRqnBD8VQk29ha2GChW2Dm36Y4hdQN%2Bo3qpXzh12c69QtdpmMbQQMLnhRmA47nig0XvYrZLb8aX1gqAOeyV4bWzs3GSMFLAeHxeSPTYLNkFqncrXt6WHjiJk%2B6eI2KAEwPdsE4JpSLkm9Go6SiHlRsqtdTUxk4437l5R%2Bd0KXJq8gprnvFhWw7AUAjEGuZtolPq2LMEtpjK%2B3ZsBSomW2Xa4KOZ7k8%2BCdYwq5krgye5Rg0AdNq4jvrOck%2FARoWbaMgw5Mupbk3me70FoEBDXm8VNwjEkSQr2tbaGHkje7o9dAr1liaEeA8OE9UB4%2FhNUrX2CZbRV7acZl1%2Fv96I1qlgfiYpT%2FTFvyYFl9Rvsj%2FvpXDU5u%2FxEXyy95TDtVNQShRpnj1Kp%2BX8lsHD8rs7zehvJRCGbk%2F91SnCZg6fmVZ9tgC8L2rqiqzoieOsKny6B445r6jFGvSXJ1sT4U3Oyw1kAobwcWlxaY1xAyQna6CcWPpWQcqpYOHATuF99ZeuurWap%2FeW%2FAWdryAWXi1xJBXT8St6UYQLi1FPoFbquMR4gueevSedtvr9jVsTSvnpmMGdgza55yX5ywSsPMNWN77wGOqUBT%2FzIYCLDRpMYOoJkSFcz%2BMJRTm13XxKJq9RKDrI7LpzvvzlmP8VQJjtdcnumFkp2nU1El2ToHrJnh7ehaAQT4758e%2FJTyzia7TrtFfgGe7vRpDq%2BDdlVc6aD79eLd0wq4%2FB2a8pu5zhDkg88zftLg%2Bu4PRxFvyOL5QLRz%2BvFKIA8OfRwxKiIGwudKMEwjVd8T38XnVmRDVKzgZngfhBQuIKRZ511&X-Amz-Signature=74e9a50a2e89744e1d5e76be202082aa958dd984af4891508eaac72a6e9380cb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662H4OBHT3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWZyQzdn6b3wi2cO5H1aalkMCV9X%2Bq2D1Vm3ahNqf16AiEA%2BxZZmd4nIgxKIx6bYSz6Qk42h1cbvx%2B%2B5lgR12RFH%2F4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEphbzooPJs5IcZSlSrcA%2BxkN90h7bispxWrTdOSxzPVnqEow6S6mZDPkNSLmZgsRRqnBD8VQk29ha2GChW2Dm36Y4hdQN%2Bo3qpXzh12c69QtdpmMbQQMLnhRmA47nig0XvYrZLb8aX1gqAOeyV4bWzs3GSMFLAeHxeSPTYLNkFqncrXt6WHjiJk%2B6eI2KAEwPdsE4JpSLkm9Go6SiHlRsqtdTUxk4437l5R%2Bd0KXJq8gprnvFhWw7AUAjEGuZtolPq2LMEtpjK%2B3ZsBSomW2Xa4KOZ7k8%2BCdYwq5krgye5Rg0AdNq4jvrOck%2FARoWbaMgw5Mupbk3me70FoEBDXm8VNwjEkSQr2tbaGHkje7o9dAr1liaEeA8OE9UB4%2FhNUrX2CZbRV7acZl1%2Fv96I1qlgfiYpT%2FTFvyYFl9Rvsj%2FvpXDU5u%2FxEXyy95TDtVNQShRpnj1Kp%2BX8lsHD8rs7zehvJRCGbk%2F91SnCZg6fmVZ9tgC8L2rqiqzoieOsKny6B445r6jFGvSXJ1sT4U3Oyw1kAobwcWlxaY1xAyQna6CcWPpWQcqpYOHATuF99ZeuurWap%2FeW%2FAWdryAWXi1xJBXT8St6UYQLi1FPoFbquMR4gueevSedtvr9jVsTSvnpmMGdgza55yX5ywSsPMNWN77wGOqUBT%2FzIYCLDRpMYOoJkSFcz%2BMJRTm13XxKJq9RKDrI7LpzvvzlmP8VQJjtdcnumFkp2nU1El2ToHrJnh7ehaAQT4758e%2FJTyzia7TrtFfgGe7vRpDq%2BDdlVc6aD79eLd0wq4%2FB2a8pu5zhDkg88zftLg%2Bu4PRxFvyOL5QLRz%2BvFKIA8OfRwxKiIGwudKMEwjVd8T38XnVmRDVKzgZngfhBQuIKRZ511&X-Amz-Signature=90b81337222b01c73ad47adfcf982abd63394323bd136f801dcc3f072f825bdc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662H4OBHT3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWZyQzdn6b3wi2cO5H1aalkMCV9X%2Bq2D1Vm3ahNqf16AiEA%2BxZZmd4nIgxKIx6bYSz6Qk42h1cbvx%2B%2B5lgR12RFH%2F4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEphbzooPJs5IcZSlSrcA%2BxkN90h7bispxWrTdOSxzPVnqEow6S6mZDPkNSLmZgsRRqnBD8VQk29ha2GChW2Dm36Y4hdQN%2Bo3qpXzh12c69QtdpmMbQQMLnhRmA47nig0XvYrZLb8aX1gqAOeyV4bWzs3GSMFLAeHxeSPTYLNkFqncrXt6WHjiJk%2B6eI2KAEwPdsE4JpSLkm9Go6SiHlRsqtdTUxk4437l5R%2Bd0KXJq8gprnvFhWw7AUAjEGuZtolPq2LMEtpjK%2B3ZsBSomW2Xa4KOZ7k8%2BCdYwq5krgye5Rg0AdNq4jvrOck%2FARoWbaMgw5Mupbk3me70FoEBDXm8VNwjEkSQr2tbaGHkje7o9dAr1liaEeA8OE9UB4%2FhNUrX2CZbRV7acZl1%2Fv96I1qlgfiYpT%2FTFvyYFl9Rvsj%2FvpXDU5u%2FxEXyy95TDtVNQShRpnj1Kp%2BX8lsHD8rs7zehvJRCGbk%2F91SnCZg6fmVZ9tgC8L2rqiqzoieOsKny6B445r6jFGvSXJ1sT4U3Oyw1kAobwcWlxaY1xAyQna6CcWPpWQcqpYOHATuF99ZeuurWap%2FeW%2FAWdryAWXi1xJBXT8St6UYQLi1FPoFbquMR4gueevSedtvr9jVsTSvnpmMGdgza55yX5ywSsPMNWN77wGOqUBT%2FzIYCLDRpMYOoJkSFcz%2BMJRTm13XxKJq9RKDrI7LpzvvzlmP8VQJjtdcnumFkp2nU1El2ToHrJnh7ehaAQT4758e%2FJTyzia7TrtFfgGe7vRpDq%2BDdlVc6aD79eLd0wq4%2FB2a8pu5zhDkg88zftLg%2Bu4PRxFvyOL5QLRz%2BvFKIA8OfRwxKiIGwudKMEwjVd8T38XnVmRDVKzgZngfhBQuIKRZ511&X-Amz-Signature=f8431587fa8fab9ca16595867537a4d926aa7eb0fc32e752bc8ef23071d1d304&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6J7MM4E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPpDDFVQtuiUENZBZSjv%2FlxzDh5yE7uyuRBWv40Jc%2B1wIhANNWUMh5d86aDUKvLZieHVOyIINMjermIXcj4J5DhNYuKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb8bfMM5sNJPYRB24q3AO69iKqroINWFrCfhXN15ZEfh0DP%2F8WIjI7uYLuRDjXW0VYT4weprV7%2FR4nHzLYyea80mDEp0qTzur708QAcw1kHqicwgJiI3z%2FgFFMNgl25LX%2FmsO8RajrJqnzAY9htqaxV2KyDSxYP5%2BSBH6J7MIbU3YLIJa6gDgi%2FbjUi4JjBU2gNc4gMQy0qjVtBeL9KvOSQBJfNXTIcT%2FIQAQ5Irm7a8ge0ihS%2BsRawQGLtmRVIIS8MP070u7BXTuX9CB4IWZA9knxpDG7XVifxHBnUyDedZrhNRRx2TyczAU1Cq2QFgcZ8mIRXvs3dM4L1ekKsad9T4FgmMQ17Q8lAP9pxzVNKBV7DNFbBgKLfAMeLR0YTcLAQXuEzH2NKuzaDVBbQP%2FcLR7ahzIX9LZu%2F8slydaKJ7kKebUxUL3FJXKQYFbZCuwHNZyzaspkmPjgsSsBj3LxFXmcLUX0jHWs9A7QPyiBjdjifiLIeTMOSUH8ReZmNE38MonUMG1pMKDQVfa3TTwA11DTVrBWJJU7uvxte6NIEWozvriPcyN0lV3JBAd6qVct9wyWudo0%2BQkA76M1Fk5zkAjZyiP6nCGb1kppAy%2FpCr8E8YhWcfC5r7UjSF5cBwcJwvwOkCQWIH1CCTCdju%2B8BjqkARNVJMYXo8sUoFepah%2FbDiTPpEQvCbHHMDSGIj1QFb8zuXSheowvxBhPJqGYDmOoizc%2BdoM8ye%2Bs%2B1tSW52JnSiuNoxUAm%2Ftstg6%2BM63AOG9eAygOZwoznLWciNBasNLvC5lzgE1I7tXpwZt3Hgb5RR21UhkrXQEPhg1PtfP1VA6jADlKYQMcNvIdzZNC%2BOrGWUzgue4ee9OZvfVG7mpVF1ktRY8&X-Amz-Signature=1cfb661cbe5d47ae30f733b7a66655d0cc7a05f15bbb85dc4124373edeabc099&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6J7MM4E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPpDDFVQtuiUENZBZSjv%2FlxzDh5yE7uyuRBWv40Jc%2B1wIhANNWUMh5d86aDUKvLZieHVOyIINMjermIXcj4J5DhNYuKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxb8bfMM5sNJPYRB24q3AO69iKqroINWFrCfhXN15ZEfh0DP%2F8WIjI7uYLuRDjXW0VYT4weprV7%2FR4nHzLYyea80mDEp0qTzur708QAcw1kHqicwgJiI3z%2FgFFMNgl25LX%2FmsO8RajrJqnzAY9htqaxV2KyDSxYP5%2BSBH6J7MIbU3YLIJa6gDgi%2FbjUi4JjBU2gNc4gMQy0qjVtBeL9KvOSQBJfNXTIcT%2FIQAQ5Irm7a8ge0ihS%2BsRawQGLtmRVIIS8MP070u7BXTuX9CB4IWZA9knxpDG7XVifxHBnUyDedZrhNRRx2TyczAU1Cq2QFgcZ8mIRXvs3dM4L1ekKsad9T4FgmMQ17Q8lAP9pxzVNKBV7DNFbBgKLfAMeLR0YTcLAQXuEzH2NKuzaDVBbQP%2FcLR7ahzIX9LZu%2F8slydaKJ7kKebUxUL3FJXKQYFbZCuwHNZyzaspkmPjgsSsBj3LxFXmcLUX0jHWs9A7QPyiBjdjifiLIeTMOSUH8ReZmNE38MonUMG1pMKDQVfa3TTwA11DTVrBWJJU7uvxte6NIEWozvriPcyN0lV3JBAd6qVct9wyWudo0%2BQkA76M1Fk5zkAjZyiP6nCGb1kppAy%2FpCr8E8YhWcfC5r7UjSF5cBwcJwvwOkCQWIH1CCTCdju%2B8BjqkARNVJMYXo8sUoFepah%2FbDiTPpEQvCbHHMDSGIj1QFb8zuXSheowvxBhPJqGYDmOoizc%2BdoM8ye%2Bs%2B1tSW52JnSiuNoxUAm%2Ftstg6%2BM63AOG9eAygOZwoznLWciNBasNLvC5lzgE1I7tXpwZt3Hgb5RR21UhkrXQEPhg1PtfP1VA6jADlKYQMcNvIdzZNC%2BOrGWUzgue4ee9OZvfVG7mpVF1ktRY8&X-Amz-Signature=860e408623ef94ae8d9295eeda4c4d2a891daa3b4bef71ec969d848b1396f1b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662H4OBHT3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWZyQzdn6b3wi2cO5H1aalkMCV9X%2Bq2D1Vm3ahNqf16AiEA%2BxZZmd4nIgxKIx6bYSz6Qk42h1cbvx%2B%2B5lgR12RFH%2F4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEphbzooPJs5IcZSlSrcA%2BxkN90h7bispxWrTdOSxzPVnqEow6S6mZDPkNSLmZgsRRqnBD8VQk29ha2GChW2Dm36Y4hdQN%2Bo3qpXzh12c69QtdpmMbQQMLnhRmA47nig0XvYrZLb8aX1gqAOeyV4bWzs3GSMFLAeHxeSPTYLNkFqncrXt6WHjiJk%2B6eI2KAEwPdsE4JpSLkm9Go6SiHlRsqtdTUxk4437l5R%2Bd0KXJq8gprnvFhWw7AUAjEGuZtolPq2LMEtpjK%2B3ZsBSomW2Xa4KOZ7k8%2BCdYwq5krgye5Rg0AdNq4jvrOck%2FARoWbaMgw5Mupbk3me70FoEBDXm8VNwjEkSQr2tbaGHkje7o9dAr1liaEeA8OE9UB4%2FhNUrX2CZbRV7acZl1%2Fv96I1qlgfiYpT%2FTFvyYFl9Rvsj%2FvpXDU5u%2FxEXyy95TDtVNQShRpnj1Kp%2BX8lsHD8rs7zehvJRCGbk%2F91SnCZg6fmVZ9tgC8L2rqiqzoieOsKny6B445r6jFGvSXJ1sT4U3Oyw1kAobwcWlxaY1xAyQna6CcWPpWQcqpYOHATuF99ZeuurWap%2FeW%2FAWdryAWXi1xJBXT8St6UYQLi1FPoFbquMR4gueevSedtvr9jVsTSvnpmMGdgza55yX5ywSsPMNWN77wGOqUBT%2FzIYCLDRpMYOoJkSFcz%2BMJRTm13XxKJq9RKDrI7LpzvvzlmP8VQJjtdcnumFkp2nU1El2ToHrJnh7ehaAQT4758e%2FJTyzia7TrtFfgGe7vRpDq%2BDdlVc6aD79eLd0wq4%2FB2a8pu5zhDkg88zftLg%2Bu4PRxFvyOL5QLRz%2BvFKIA8OfRwxKiIGwudKMEwjVd8T38XnVmRDVKzgZngfhBQuIKRZ511&X-Amz-Signature=0381a6e36949a191d83bb98cda9f72cd4ab887df19b7246d418bb5c8b574f19a&X-Amz-SignedHeaders=host&x-id=GetObject)
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