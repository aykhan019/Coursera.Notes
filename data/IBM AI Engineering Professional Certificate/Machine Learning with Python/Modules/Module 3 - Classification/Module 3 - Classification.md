

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWLNWFRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIELEHOH4fk7EyYO06VzPilK6AswsW8DYAGceZUV8zo%2FVAiEAwUsFWhq2ItZDIYoAtd0TVt8n6rAD62xXxHlatnb%2BjmMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFl2Phjr%2FvMfBOs99SrcA5aHTateABS0D2ncRm2G2dkD6D9stTor96pwunErFD%2BRDOtB%2BwzrZXX4oxXUGiA5rLn%2BUIFUxoMAVuWQx4sFutkqVSuelaCYS7G%2Bh8GCx6tqxT3GK1wd%2B5TCyohv4v%2BYkpR8jNFO%2ByVJLIZQGdd%2BtegL6Ce1xn5JMaHohAFqzBdB18Z7OFdRcmIWFlcCXBYkV7pe7hc5M9Vm5bJmfNG1Y%2Bx3f4b1fWK7DxTL%2B8dj0HD9SmS3%2FLIThb%2F7tM0Ehc8t%2BVsGWWqFYTBkGnbbAU507b%2By0fD4b2Xp%2FgP38rvDD1KyID5f7huNDdqIQf2OJYXJzCQybf8H9a7iKvOuo9b9HSDQqQbrqEx5zUgKbIiGW%2F8ChijSIoMIEvBJeSgy8c4gNVNXpV3LZjrgyNGpbkV4uB2em%2FPz7K8fkoTGGwP32okmZhb2gMAGHPSqBQ57C%2BKlikY91ufY0dXlYMjONkNg3wViYeqt3bU8c9jKcx5z50RV0G2Tpb1XhMMfBh2IPnKPHgJiMsMzkLWpM20Ks1qLSmThAchwTD6Z76oe59i3J34wd6ZC0BUFqvFm6YuX3psi1INrHEIogFh398WcufrZuk%2FkG8UHHANOzD8K2JliPTgRlA87jtjCUviZ8IpRML6Fnb0GOqUBoUJBiAtlgdRft1WcJwTGE%2FJ1svQKZ186kxArN4AB3sAiZ1hTF8akZLxZPk0LYn43qKx7op%2BujLJJH5IHceEV83B0T5Huffm507p1wZFxFZ3cjyxozpzO2ZiXMRK76Vh0gDTWxMmCQ5SS3WgpoG4Z4NKnU977NmdHO5SjvcgqnU5uTk73hE7vXD0%2F2B8P7Z9qXWb4Gr41rFcZtoqH4hdADBSwYO5A&X-Amz-Signature=c6f7265293d9d9d45c46ca81e208c1a65a430a68810d3a7b377f540a5be329a4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWLNWFRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIELEHOH4fk7EyYO06VzPilK6AswsW8DYAGceZUV8zo%2FVAiEAwUsFWhq2ItZDIYoAtd0TVt8n6rAD62xXxHlatnb%2BjmMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFl2Phjr%2FvMfBOs99SrcA5aHTateABS0D2ncRm2G2dkD6D9stTor96pwunErFD%2BRDOtB%2BwzrZXX4oxXUGiA5rLn%2BUIFUxoMAVuWQx4sFutkqVSuelaCYS7G%2Bh8GCx6tqxT3GK1wd%2B5TCyohv4v%2BYkpR8jNFO%2ByVJLIZQGdd%2BtegL6Ce1xn5JMaHohAFqzBdB18Z7OFdRcmIWFlcCXBYkV7pe7hc5M9Vm5bJmfNG1Y%2Bx3f4b1fWK7DxTL%2B8dj0HD9SmS3%2FLIThb%2F7tM0Ehc8t%2BVsGWWqFYTBkGnbbAU507b%2By0fD4b2Xp%2FgP38rvDD1KyID5f7huNDdqIQf2OJYXJzCQybf8H9a7iKvOuo9b9HSDQqQbrqEx5zUgKbIiGW%2F8ChijSIoMIEvBJeSgy8c4gNVNXpV3LZjrgyNGpbkV4uB2em%2FPz7K8fkoTGGwP32okmZhb2gMAGHPSqBQ57C%2BKlikY91ufY0dXlYMjONkNg3wViYeqt3bU8c9jKcx5z50RV0G2Tpb1XhMMfBh2IPnKPHgJiMsMzkLWpM20Ks1qLSmThAchwTD6Z76oe59i3J34wd6ZC0BUFqvFm6YuX3psi1INrHEIogFh398WcufrZuk%2FkG8UHHANOzD8K2JliPTgRlA87jtjCUviZ8IpRML6Fnb0GOqUBoUJBiAtlgdRft1WcJwTGE%2FJ1svQKZ186kxArN4AB3sAiZ1hTF8akZLxZPk0LYn43qKx7op%2BujLJJH5IHceEV83B0T5Huffm507p1wZFxFZ3cjyxozpzO2ZiXMRK76Vh0gDTWxMmCQ5SS3WgpoG4Z4NKnU977NmdHO5SjvcgqnU5uTk73hE7vXD0%2F2B8P7Z9qXWb4Gr41rFcZtoqH4hdADBSwYO5A&X-Amz-Signature=8805349f9abd190eaa2025080199b772d9a7828c7b179839842fe6c501eff7d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWLNWFRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIELEHOH4fk7EyYO06VzPilK6AswsW8DYAGceZUV8zo%2FVAiEAwUsFWhq2ItZDIYoAtd0TVt8n6rAD62xXxHlatnb%2BjmMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFl2Phjr%2FvMfBOs99SrcA5aHTateABS0D2ncRm2G2dkD6D9stTor96pwunErFD%2BRDOtB%2BwzrZXX4oxXUGiA5rLn%2BUIFUxoMAVuWQx4sFutkqVSuelaCYS7G%2Bh8GCx6tqxT3GK1wd%2B5TCyohv4v%2BYkpR8jNFO%2ByVJLIZQGdd%2BtegL6Ce1xn5JMaHohAFqzBdB18Z7OFdRcmIWFlcCXBYkV7pe7hc5M9Vm5bJmfNG1Y%2Bx3f4b1fWK7DxTL%2B8dj0HD9SmS3%2FLIThb%2F7tM0Ehc8t%2BVsGWWqFYTBkGnbbAU507b%2By0fD4b2Xp%2FgP38rvDD1KyID5f7huNDdqIQf2OJYXJzCQybf8H9a7iKvOuo9b9HSDQqQbrqEx5zUgKbIiGW%2F8ChijSIoMIEvBJeSgy8c4gNVNXpV3LZjrgyNGpbkV4uB2em%2FPz7K8fkoTGGwP32okmZhb2gMAGHPSqBQ57C%2BKlikY91ufY0dXlYMjONkNg3wViYeqt3bU8c9jKcx5z50RV0G2Tpb1XhMMfBh2IPnKPHgJiMsMzkLWpM20Ks1qLSmThAchwTD6Z76oe59i3J34wd6ZC0BUFqvFm6YuX3psi1INrHEIogFh398WcufrZuk%2FkG8UHHANOzD8K2JliPTgRlA87jtjCUviZ8IpRML6Fnb0GOqUBoUJBiAtlgdRft1WcJwTGE%2FJ1svQKZ186kxArN4AB3sAiZ1hTF8akZLxZPk0LYn43qKx7op%2BujLJJH5IHceEV83B0T5Huffm507p1wZFxFZ3cjyxozpzO2ZiXMRK76Vh0gDTWxMmCQ5SS3WgpoG4Z4NKnU977NmdHO5SjvcgqnU5uTk73hE7vXD0%2F2B8P7Z9qXWb4Gr41rFcZtoqH4hdADBSwYO5A&X-Amz-Signature=39780f2850d250539f595e9c0cdbbbd301cdd375a80fc71bda5c08c083d55071&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJQBWBTV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIH9nUZOHtPO%2F2VDTFO3qcxKpfQP4JrkJDKF9jkxzGBjNAiEA%2Bo%2B0%2BmR%2FkDistf53mqMGsNQUXMRiXmq%2FYRwjwLRfcTkqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMO4yNiVhPgwjmS16yrcA7Ds5zgQp7OsSZE0%2FLOeLFbgB%2BQBJvFtP8ILw0aFj25wR6j7S%2BqSOCAIU9y1GLYmShMJ84n4nbreyp8TzUdg0YtBg2O8ppWOCQhUkUNER%2Bi8J2NVpwEisroQFQN9c0hDgB0%2FG7akfaObqh2qY2OznX%2BhKJwb1kbwVqd4URpsCrDNDKCNXF28dDwNSyb53dPzAqrpRi7Qx0WoBc%2F93hB3Iygea4Ol5R6XwaVZukuQANF6lFvUyqs6xbGdKVB3DtncPOrCA8mfxrYjKmdO%2FHm%2By1mQplk73xSe1WZzKhAnguTwOu4K0IiNWX2R2cw9RVR%2B0swar%2F94XVzlwNhY9yR9lURZMYabo%2BWKSbCal%2F3FosMcQPO7Y6%2BW2sS38IEQGnuleGh7aPz93scKAIwFJdYX0vhMlP8HHG8LV3IL%2BzkzEPK0skR7LOnF5%2BexcSsQQMw1TUapcpa2MnoQ4L378ubjCCdJ5v4SCQxzc8eqJP5YW7yZWst6ziJv8U1ARvI%2Bz%2BZR4j0j7UiW%2BjYK1QpxCyoizQM%2FTW8K9dvfu1n83xIUj3c%2FKeQy%2BbpT7xuSnCOYPY3Yu2%2FwSIt7u9UchK%2B4nOkFQLdKWLkqBZ%2BtsaU5ynwSJx3PtI%2FhLelheiAT7UJ%2FMIGFnb0GOqUBEpq4ryFofWLfR%2Fn%2BxYzp%2BdDuCJKGG515OmidHyz4Phjqe06x9zkmQMjpleJ%2F6kcDuf3QcjRz3M5mmFva36gDuq06j9f%2F5yvS%2B%2FsrAhhkwIhc35Y5%2FJA1JHyM8yY9BQkNAbXL75mRYsAPKcZRzBfECECZADZKC8t9xUXYQE39RtMS7tT7RkeNjFdRbENJ3Ft4fXPSWtLo8I%2Fzqlhfsv9PgSrZkzsY&X-Amz-Signature=db7c17e2c8b9dbdd4866cd2725cc009fb0d655284570898c056e2d7ee19f0785&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJQBWBTV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIH9nUZOHtPO%2F2VDTFO3qcxKpfQP4JrkJDKF9jkxzGBjNAiEA%2Bo%2B0%2BmR%2FkDistf53mqMGsNQUXMRiXmq%2FYRwjwLRfcTkqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMO4yNiVhPgwjmS16yrcA7Ds5zgQp7OsSZE0%2FLOeLFbgB%2BQBJvFtP8ILw0aFj25wR6j7S%2BqSOCAIU9y1GLYmShMJ84n4nbreyp8TzUdg0YtBg2O8ppWOCQhUkUNER%2Bi8J2NVpwEisroQFQN9c0hDgB0%2FG7akfaObqh2qY2OznX%2BhKJwb1kbwVqd4URpsCrDNDKCNXF28dDwNSyb53dPzAqrpRi7Qx0WoBc%2F93hB3Iygea4Ol5R6XwaVZukuQANF6lFvUyqs6xbGdKVB3DtncPOrCA8mfxrYjKmdO%2FHm%2By1mQplk73xSe1WZzKhAnguTwOu4K0IiNWX2R2cw9RVR%2B0swar%2F94XVzlwNhY9yR9lURZMYabo%2BWKSbCal%2F3FosMcQPO7Y6%2BW2sS38IEQGnuleGh7aPz93scKAIwFJdYX0vhMlP8HHG8LV3IL%2BzkzEPK0skR7LOnF5%2BexcSsQQMw1TUapcpa2MnoQ4L378ubjCCdJ5v4SCQxzc8eqJP5YW7yZWst6ziJv8U1ARvI%2Bz%2BZR4j0j7UiW%2BjYK1QpxCyoizQM%2FTW8K9dvfu1n83xIUj3c%2FKeQy%2BbpT7xuSnCOYPY3Yu2%2FwSIt7u9UchK%2B4nOkFQLdKWLkqBZ%2BtsaU5ynwSJx3PtI%2FhLelheiAT7UJ%2FMIGFnb0GOqUBEpq4ryFofWLfR%2Fn%2BxYzp%2BdDuCJKGG515OmidHyz4Phjqe06x9zkmQMjpleJ%2F6kcDuf3QcjRz3M5mmFva36gDuq06j9f%2F5yvS%2B%2FsrAhhkwIhc35Y5%2FJA1JHyM8yY9BQkNAbXL75mRYsAPKcZRzBfECECZADZKC8t9xUXYQE39RtMS7tT7RkeNjFdRbENJ3Ft4fXPSWtLo8I%2Fzqlhfsv9PgSrZkzsY&X-Amz-Signature=03a9f53a5840409cce1ce97c57bc37308eebf26e41cdd16b10ce3b99f9da5a98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWLNWFRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIELEHOH4fk7EyYO06VzPilK6AswsW8DYAGceZUV8zo%2FVAiEAwUsFWhq2ItZDIYoAtd0TVt8n6rAD62xXxHlatnb%2BjmMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFl2Phjr%2FvMfBOs99SrcA5aHTateABS0D2ncRm2G2dkD6D9stTor96pwunErFD%2BRDOtB%2BwzrZXX4oxXUGiA5rLn%2BUIFUxoMAVuWQx4sFutkqVSuelaCYS7G%2Bh8GCx6tqxT3GK1wd%2B5TCyohv4v%2BYkpR8jNFO%2ByVJLIZQGdd%2BtegL6Ce1xn5JMaHohAFqzBdB18Z7OFdRcmIWFlcCXBYkV7pe7hc5M9Vm5bJmfNG1Y%2Bx3f4b1fWK7DxTL%2B8dj0HD9SmS3%2FLIThb%2F7tM0Ehc8t%2BVsGWWqFYTBkGnbbAU507b%2By0fD4b2Xp%2FgP38rvDD1KyID5f7huNDdqIQf2OJYXJzCQybf8H9a7iKvOuo9b9HSDQqQbrqEx5zUgKbIiGW%2F8ChijSIoMIEvBJeSgy8c4gNVNXpV3LZjrgyNGpbkV4uB2em%2FPz7K8fkoTGGwP32okmZhb2gMAGHPSqBQ57C%2BKlikY91ufY0dXlYMjONkNg3wViYeqt3bU8c9jKcx5z50RV0G2Tpb1XhMMfBh2IPnKPHgJiMsMzkLWpM20Ks1qLSmThAchwTD6Z76oe59i3J34wd6ZC0BUFqvFm6YuX3psi1INrHEIogFh398WcufrZuk%2FkG8UHHANOzD8K2JliPTgRlA87jtjCUviZ8IpRML6Fnb0GOqUBoUJBiAtlgdRft1WcJwTGE%2FJ1svQKZ186kxArN4AB3sAiZ1hTF8akZLxZPk0LYn43qKx7op%2BujLJJH5IHceEV83B0T5Huffm507p1wZFxFZ3cjyxozpzO2ZiXMRK76Vh0gDTWxMmCQ5SS3WgpoG4Z4NKnU977NmdHO5SjvcgqnU5uTk73hE7vXD0%2F2B8P7Z9qXWb4Gr41rFcZtoqH4hdADBSwYO5A&X-Amz-Signature=671c06bfaf94a3ebd2195458691a723e7baa1ad2bd7f2ca10f9eda25bee3a692&X-Amz-SignedHeaders=host&x-id=GetObject)
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