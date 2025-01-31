

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ3ETDEF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJX2UAvO0ZCzI1obKDVHERq%2FMGxjmAVmW2qhhVfi7xsAiEAmUE96aQWWkD4cC5Xf1sgufW2vd8lo7d5O4EPSxoJ6PUqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFve0Q0pkYHzKR%2FUIircA9wEnaKI1dRCEGsjA99Mx%2BJsqhuCzKUKvntRC4mMFjd6VdyNWbRLF8hchhTzQyHIlrv3aSfz41Rgf09qTwGeYVtufY5QPfgbaRShHaRpTmKdVVOrT5kmskz%2BimGduVU%2B8OzYnnDi2cY8VGLJlzLcETHCJeDjjGPgqB9%2BEGQRp1XhzHJQuMoK8%2B%2Fn2ZNgnO6DqGL9oxbaM8u3G0zWb0ANnsdcrCx4Nw3hC4AZDpMt20r48l0tnbcW5IdulNYcQ9V76XnRev0Xq4dAC4lyA%2B2ENzRRE2jO43P80B4thMfOvewzkVwhxbCae4kPNxaMIQYY4dyrQ%2FpoCnclMrdOr9JKXvuy8XhgCep5qofD9aqaOVIjglkcIyA%2B4GU9Vc40HfxiLhncmiVt3%2BZU%2FQ5bt7MK4KTwqqX%2Fa6M2XUMxuIjZF%2BdKTSJh8ClTHQc2BJ5TammR3336gDUnRSZHuGzh4QjaPhbmdC9XrIifZfh3xLTe0xeFSl%2BLRsJTcc4yva2OispXLcJiUIZzus8bcxS%2BfFLB7WjdDzBrZY0HAxgUOa21rIHgdYd5GRBmfiN7UZlndn5eUyHafEtrWdkyGdiE7CmWgxvzRDRsnEpCjceKXSOhSuNiDvA4vjkovBHbjQVnMIjA9LwGOqUBIc%2B6L3oHJVWuh%2FxC%2BzyGb0TK9%2FEqKg78hAmuu0IABYOIlfz%2FP42jOi4%2BkwN3daCrtv8GM5KEudB03WJ%2Bfh0nlJOPf6hszM3PtQi8HEujULqoYzKo2GzHvxCX3E8wyESOCs7d2sj6QPxxq%2BoIF4W6Bty6MQejIqq%2FH9l4G17Xy32KWZUEsFx7kil%2FrejtKzpYF2y1IjuVLodfvkWqzfBAoM6DpJd0&X-Amz-Signature=1d557f3812ccb668ab535a20d35cfb0b80a2d9d7e60ee83ad0ac2b4ebcaa1316&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ3ETDEF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJX2UAvO0ZCzI1obKDVHERq%2FMGxjmAVmW2qhhVfi7xsAiEAmUE96aQWWkD4cC5Xf1sgufW2vd8lo7d5O4EPSxoJ6PUqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFve0Q0pkYHzKR%2FUIircA9wEnaKI1dRCEGsjA99Mx%2BJsqhuCzKUKvntRC4mMFjd6VdyNWbRLF8hchhTzQyHIlrv3aSfz41Rgf09qTwGeYVtufY5QPfgbaRShHaRpTmKdVVOrT5kmskz%2BimGduVU%2B8OzYnnDi2cY8VGLJlzLcETHCJeDjjGPgqB9%2BEGQRp1XhzHJQuMoK8%2B%2Fn2ZNgnO6DqGL9oxbaM8u3G0zWb0ANnsdcrCx4Nw3hC4AZDpMt20r48l0tnbcW5IdulNYcQ9V76XnRev0Xq4dAC4lyA%2B2ENzRRE2jO43P80B4thMfOvewzkVwhxbCae4kPNxaMIQYY4dyrQ%2FpoCnclMrdOr9JKXvuy8XhgCep5qofD9aqaOVIjglkcIyA%2B4GU9Vc40HfxiLhncmiVt3%2BZU%2FQ5bt7MK4KTwqqX%2Fa6M2XUMxuIjZF%2BdKTSJh8ClTHQc2BJ5TammR3336gDUnRSZHuGzh4QjaPhbmdC9XrIifZfh3xLTe0xeFSl%2BLRsJTcc4yva2OispXLcJiUIZzus8bcxS%2BfFLB7WjdDzBrZY0HAxgUOa21rIHgdYd5GRBmfiN7UZlndn5eUyHafEtrWdkyGdiE7CmWgxvzRDRsnEpCjceKXSOhSuNiDvA4vjkovBHbjQVnMIjA9LwGOqUBIc%2B6L3oHJVWuh%2FxC%2BzyGb0TK9%2FEqKg78hAmuu0IABYOIlfz%2FP42jOi4%2BkwN3daCrtv8GM5KEudB03WJ%2Bfh0nlJOPf6hszM3PtQi8HEujULqoYzKo2GzHvxCX3E8wyESOCs7d2sj6QPxxq%2BoIF4W6Bty6MQejIqq%2FH9l4G17Xy32KWZUEsFx7kil%2FrejtKzpYF2y1IjuVLodfvkWqzfBAoM6DpJd0&X-Amz-Signature=f5f02c3247792c55528feb934f4ffc783cf6a5d95508c64a5bff6ec43050f6d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ3ETDEF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJX2UAvO0ZCzI1obKDVHERq%2FMGxjmAVmW2qhhVfi7xsAiEAmUE96aQWWkD4cC5Xf1sgufW2vd8lo7d5O4EPSxoJ6PUqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFve0Q0pkYHzKR%2FUIircA9wEnaKI1dRCEGsjA99Mx%2BJsqhuCzKUKvntRC4mMFjd6VdyNWbRLF8hchhTzQyHIlrv3aSfz41Rgf09qTwGeYVtufY5QPfgbaRShHaRpTmKdVVOrT5kmskz%2BimGduVU%2B8OzYnnDi2cY8VGLJlzLcETHCJeDjjGPgqB9%2BEGQRp1XhzHJQuMoK8%2B%2Fn2ZNgnO6DqGL9oxbaM8u3G0zWb0ANnsdcrCx4Nw3hC4AZDpMt20r48l0tnbcW5IdulNYcQ9V76XnRev0Xq4dAC4lyA%2B2ENzRRE2jO43P80B4thMfOvewzkVwhxbCae4kPNxaMIQYY4dyrQ%2FpoCnclMrdOr9JKXvuy8XhgCep5qofD9aqaOVIjglkcIyA%2B4GU9Vc40HfxiLhncmiVt3%2BZU%2FQ5bt7MK4KTwqqX%2Fa6M2XUMxuIjZF%2BdKTSJh8ClTHQc2BJ5TammR3336gDUnRSZHuGzh4QjaPhbmdC9XrIifZfh3xLTe0xeFSl%2BLRsJTcc4yva2OispXLcJiUIZzus8bcxS%2BfFLB7WjdDzBrZY0HAxgUOa21rIHgdYd5GRBmfiN7UZlndn5eUyHafEtrWdkyGdiE7CmWgxvzRDRsnEpCjceKXSOhSuNiDvA4vjkovBHbjQVnMIjA9LwGOqUBIc%2B6L3oHJVWuh%2FxC%2BzyGb0TK9%2FEqKg78hAmuu0IABYOIlfz%2FP42jOi4%2BkwN3daCrtv8GM5KEudB03WJ%2Bfh0nlJOPf6hszM3PtQi8HEujULqoYzKo2GzHvxCX3E8wyESOCs7d2sj6QPxxq%2BoIF4W6Bty6MQejIqq%2FH9l4G17Xy32KWZUEsFx7kil%2FrejtKzpYF2y1IjuVLodfvkWqzfBAoM6DpJd0&X-Amz-Signature=cc1c287049550c079e3689748e2f52d8164177f2bda57e927fdd7a4cd48b42e8&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKVQ6TVL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICd8N2EKpOYpWhlkTCySGnWoPkCR8%2FNTfkZAxO%2F3OIhBAiEA0fweLfiyJV08BSNNlK8hIcW%2B8oyWEJoooha2HV2ogecqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOkxtCYPqcmkwj0dSCrcA8xXyIULNvFFejbm2Ssq7HJOwmxwsvM2ayAsm%2Fwgidx0wICK4fI33t8NWr%2BeAKxbGVfAU4fwN%2BzMAN6Iw5jIvcY26Vk1qTGHpkKvihjP11dJExtTotLJ0S74uUnvMubE2JvWrjhp2wB6t1v8DhrX2KLCIxuf7AGPNtB3%2BrkKFymKqUQRE2d2zrVrGu6FY7XU2qUawY8c%2FZnpoaO41wA9hCBnq5MMzliYIhGK0zl60sZa%2F%2BeYQnx%2FtAT4qBWNzg6lGo6F2U6e7P2H0MVjFmWUeKRt09%2BQXdIYPRly9YNot7zdGW9roB1CSiY1%2FfFfQRw5HVRniDG%2BsvaQaQrl2He3g6GBq8sQCjSVev5sF%2FCs2i%2FsRBjt68iXfizjDok0PtRun%2BfLTdqO0idPnMFHnMRgr8we5EEabQAE77Ch0K%2F1R4b%2Fd8%2BhbBICWkI9ptcbNPhj%2FAnG%2BE1OeYFQpaXMtKlTzeJeKbQTcc2eCfJdPeAZVeQPDDnZP6crNIkHAqg25NtVsCfvevRbk9RDAMoPYywgFzkNiDnxvi%2FU7TH7UQL1rrm9FYSvyRBMa%2BhzOefHQSADkoIkc6U5sjYI0TSfcQ8ocbTPOU2COGXueHMhgz5Xg8ioiKFV%2FvB7I6%2B9OHUiMPW%2F9LwGOqUB7dwWepzntx0YRFTBI%2BPbZmngTXs24YC8HQdEP1qnAiz8iVEHiHWQmLvqCl5e2xuqFMUWIBGDUYRmOSy07qhsMEp4FxRB2atRgRMNhxVqubsP7dm8n6WCfBjBtZ4vNnUVlKn2qYokkZ4KKesRyfhxIo8gPiNLbYXvRDY0twT3iQNvfh2Vv42dPndcgPEBcNgcTCwXSaybOMC%2FajiTAwIOCd6I5FiL&X-Amz-Signature=9fe71abe9c8635b66c230bd1c7fa6309243356ed529d0ecbc85384977eee4aa6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKVQ6TVL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICd8N2EKpOYpWhlkTCySGnWoPkCR8%2FNTfkZAxO%2F3OIhBAiEA0fweLfiyJV08BSNNlK8hIcW%2B8oyWEJoooha2HV2ogecqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOkxtCYPqcmkwj0dSCrcA8xXyIULNvFFejbm2Ssq7HJOwmxwsvM2ayAsm%2Fwgidx0wICK4fI33t8NWr%2BeAKxbGVfAU4fwN%2BzMAN6Iw5jIvcY26Vk1qTGHpkKvihjP11dJExtTotLJ0S74uUnvMubE2JvWrjhp2wB6t1v8DhrX2KLCIxuf7AGPNtB3%2BrkKFymKqUQRE2d2zrVrGu6FY7XU2qUawY8c%2FZnpoaO41wA9hCBnq5MMzliYIhGK0zl60sZa%2F%2BeYQnx%2FtAT4qBWNzg6lGo6F2U6e7P2H0MVjFmWUeKRt09%2BQXdIYPRly9YNot7zdGW9roB1CSiY1%2FfFfQRw5HVRniDG%2BsvaQaQrl2He3g6GBq8sQCjSVev5sF%2FCs2i%2FsRBjt68iXfizjDok0PtRun%2BfLTdqO0idPnMFHnMRgr8we5EEabQAE77Ch0K%2F1R4b%2Fd8%2BhbBICWkI9ptcbNPhj%2FAnG%2BE1OeYFQpaXMtKlTzeJeKbQTcc2eCfJdPeAZVeQPDDnZP6crNIkHAqg25NtVsCfvevRbk9RDAMoPYywgFzkNiDnxvi%2FU7TH7UQL1rrm9FYSvyRBMa%2BhzOefHQSADkoIkc6U5sjYI0TSfcQ8ocbTPOU2COGXueHMhgz5Xg8ioiKFV%2FvB7I6%2B9OHUiMPW%2F9LwGOqUB7dwWepzntx0YRFTBI%2BPbZmngTXs24YC8HQdEP1qnAiz8iVEHiHWQmLvqCl5e2xuqFMUWIBGDUYRmOSy07qhsMEp4FxRB2atRgRMNhxVqubsP7dm8n6WCfBjBtZ4vNnUVlKn2qYokkZ4KKesRyfhxIo8gPiNLbYXvRDY0twT3iQNvfh2Vv42dPndcgPEBcNgcTCwXSaybOMC%2FajiTAwIOCd6I5FiL&X-Amz-Signature=9e09cac83fc670039d3b9f595184d0e555cc6cea5732da323198575a98331085&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ3ETDEF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAJX2UAvO0ZCzI1obKDVHERq%2FMGxjmAVmW2qhhVfi7xsAiEAmUE96aQWWkD4cC5Xf1sgufW2vd8lo7d5O4EPSxoJ6PUqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFve0Q0pkYHzKR%2FUIircA9wEnaKI1dRCEGsjA99Mx%2BJsqhuCzKUKvntRC4mMFjd6VdyNWbRLF8hchhTzQyHIlrv3aSfz41Rgf09qTwGeYVtufY5QPfgbaRShHaRpTmKdVVOrT5kmskz%2BimGduVU%2B8OzYnnDi2cY8VGLJlzLcETHCJeDjjGPgqB9%2BEGQRp1XhzHJQuMoK8%2B%2Fn2ZNgnO6DqGL9oxbaM8u3G0zWb0ANnsdcrCx4Nw3hC4AZDpMt20r48l0tnbcW5IdulNYcQ9V76XnRev0Xq4dAC4lyA%2B2ENzRRE2jO43P80B4thMfOvewzkVwhxbCae4kPNxaMIQYY4dyrQ%2FpoCnclMrdOr9JKXvuy8XhgCep5qofD9aqaOVIjglkcIyA%2B4GU9Vc40HfxiLhncmiVt3%2BZU%2FQ5bt7MK4KTwqqX%2Fa6M2XUMxuIjZF%2BdKTSJh8ClTHQc2BJ5TammR3336gDUnRSZHuGzh4QjaPhbmdC9XrIifZfh3xLTe0xeFSl%2BLRsJTcc4yva2OispXLcJiUIZzus8bcxS%2BfFLB7WjdDzBrZY0HAxgUOa21rIHgdYd5GRBmfiN7UZlndn5eUyHafEtrWdkyGdiE7CmWgxvzRDRsnEpCjceKXSOhSuNiDvA4vjkovBHbjQVnMIjA9LwGOqUBIc%2B6L3oHJVWuh%2FxC%2BzyGb0TK9%2FEqKg78hAmuu0IABYOIlfz%2FP42jOi4%2BkwN3daCrtv8GM5KEudB03WJ%2Bfh0nlJOPf6hszM3PtQi8HEujULqoYzKo2GzHvxCX3E8wyESOCs7d2sj6QPxxq%2BoIF4W6Bty6MQejIqq%2FH9l4G17Xy32KWZUEsFx7kil%2FrejtKzpYF2y1IjuVLodfvkWqzfBAoM6DpJd0&X-Amz-Signature=e23ddaeccf8948a8241a0c52b486277f2aa3309eb3e6844e1c20dbe35a98099e&X-Amz-SignedHeaders=host&x-id=GetObject)
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