

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVB7OEYP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCD3OA9ftK%2FvX3v79sgcJ6JhhS70Z9e5U9MvkGYpajixgIgIbKPCkvheR5xvn4SXgXqMY%2BHQGi4DGpirsSxWgmThFIqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFasGxJINCV%2BojI7oCrcA0CBcBrFQZ6UX8DUppRcaWALurue4SrENC5NIODGS%2Bnrxe%2Bw5C3lOX81Y1r%2FjqDD83ezu2zmItgxVFgwm3WuBpTN%2FXLqMSfPHrdnJ0DT7ZXCzppp08mDZzSMVh2ud1o5N5yIt5KsyO5fpFaCXpjGefWZEDQ1gt9y9sHXsnZZ6NR5tZp0XlWd5jeEl0wfjXR0Rz1C4eP8xYymrM2NwfQONyKTx0HInozsHw0A2B71PEEuJWTscKG3%2B7RZpTmq6o81fQ3xk1vmnEhI2O3qGjnrjQ2uGpN9mds3xdn63q2xFw%2FCtPdUSEkE5230dPon8c4GJDzZYwdcR9FVc%2B7HNFhKjVsSnLGvGzdqAtjT0nuS9YOx1M3jybxUWS7pEjF9g9aPe02ncuH9QjUQ6XC3pXu5p6%2ByDWTIEm5e7QR%2FXeHoSZwBrQlOQlzkTG65mFcLlMbX5kEDVR0dK%2F4368d%2B2sXFPiPknXEkp%2BsEK9ylIA4xHkLRITkPDT%2BaEjnY75SA623FEBDZcSNpDVr58PP5fNqV6mJMwC5bF5c5BQMdQp2VmzLZcxEEXk%2FeBWSEvd90q2mAMxmQ2OHh2FEqovt0Kv9A7oW9FN2xW%2BZJihVirDXwD2QJZ0mQ%2Bp%2BwotfOd6FOMIbz7rwGOqUBzKZ%2FySG50uGjPUsnynwoAyyZcdDOrtvjpyo79KU6msn69CuqO5ZCsQevZoymYmt0ZtLTjXi3O49qt%2Bt0TfT7ckZjy5Cm7K2C7Z7wPDCNRoxi3gmfDVGP%2FzAzpe43btT%2BnbrUtY4Q2DBewxURqkqZf7XDPT2uO2sObT%2FG29%2BoB9T4d3YFn5j%2BXSgeS85zD3khVV59RKOmefxlGGNp1oJtDMfU%2FmUK&X-Amz-Signature=ecdfe46b0b15b5c9e87ef8e8420d4e73d6580b824eda24fde311ce5b0d64e670&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVB7OEYP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCD3OA9ftK%2FvX3v79sgcJ6JhhS70Z9e5U9MvkGYpajixgIgIbKPCkvheR5xvn4SXgXqMY%2BHQGi4DGpirsSxWgmThFIqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFasGxJINCV%2BojI7oCrcA0CBcBrFQZ6UX8DUppRcaWALurue4SrENC5NIODGS%2Bnrxe%2Bw5C3lOX81Y1r%2FjqDD83ezu2zmItgxVFgwm3WuBpTN%2FXLqMSfPHrdnJ0DT7ZXCzppp08mDZzSMVh2ud1o5N5yIt5KsyO5fpFaCXpjGefWZEDQ1gt9y9sHXsnZZ6NR5tZp0XlWd5jeEl0wfjXR0Rz1C4eP8xYymrM2NwfQONyKTx0HInozsHw0A2B71PEEuJWTscKG3%2B7RZpTmq6o81fQ3xk1vmnEhI2O3qGjnrjQ2uGpN9mds3xdn63q2xFw%2FCtPdUSEkE5230dPon8c4GJDzZYwdcR9FVc%2B7HNFhKjVsSnLGvGzdqAtjT0nuS9YOx1M3jybxUWS7pEjF9g9aPe02ncuH9QjUQ6XC3pXu5p6%2ByDWTIEm5e7QR%2FXeHoSZwBrQlOQlzkTG65mFcLlMbX5kEDVR0dK%2F4368d%2B2sXFPiPknXEkp%2BsEK9ylIA4xHkLRITkPDT%2BaEjnY75SA623FEBDZcSNpDVr58PP5fNqV6mJMwC5bF5c5BQMdQp2VmzLZcxEEXk%2FeBWSEvd90q2mAMxmQ2OHh2FEqovt0Kv9A7oW9FN2xW%2BZJihVirDXwD2QJZ0mQ%2Bp%2BwotfOd6FOMIbz7rwGOqUBzKZ%2FySG50uGjPUsnynwoAyyZcdDOrtvjpyo79KU6msn69CuqO5ZCsQevZoymYmt0ZtLTjXi3O49qt%2Bt0TfT7ckZjy5Cm7K2C7Z7wPDCNRoxi3gmfDVGP%2FzAzpe43btT%2BnbrUtY4Q2DBewxURqkqZf7XDPT2uO2sObT%2FG29%2BoB9T4d3YFn5j%2BXSgeS85zD3khVV59RKOmefxlGGNp1oJtDMfU%2FmUK&X-Amz-Signature=b672b63f8904b92e716b670f4e67b05cb8e340bdd76b8f93a5fad1ed1b75ceee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVB7OEYP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCD3OA9ftK%2FvX3v79sgcJ6JhhS70Z9e5U9MvkGYpajixgIgIbKPCkvheR5xvn4SXgXqMY%2BHQGi4DGpirsSxWgmThFIqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFasGxJINCV%2BojI7oCrcA0CBcBrFQZ6UX8DUppRcaWALurue4SrENC5NIODGS%2Bnrxe%2Bw5C3lOX81Y1r%2FjqDD83ezu2zmItgxVFgwm3WuBpTN%2FXLqMSfPHrdnJ0DT7ZXCzppp08mDZzSMVh2ud1o5N5yIt5KsyO5fpFaCXpjGefWZEDQ1gt9y9sHXsnZZ6NR5tZp0XlWd5jeEl0wfjXR0Rz1C4eP8xYymrM2NwfQONyKTx0HInozsHw0A2B71PEEuJWTscKG3%2B7RZpTmq6o81fQ3xk1vmnEhI2O3qGjnrjQ2uGpN9mds3xdn63q2xFw%2FCtPdUSEkE5230dPon8c4GJDzZYwdcR9FVc%2B7HNFhKjVsSnLGvGzdqAtjT0nuS9YOx1M3jybxUWS7pEjF9g9aPe02ncuH9QjUQ6XC3pXu5p6%2ByDWTIEm5e7QR%2FXeHoSZwBrQlOQlzkTG65mFcLlMbX5kEDVR0dK%2F4368d%2B2sXFPiPknXEkp%2BsEK9ylIA4xHkLRITkPDT%2BaEjnY75SA623FEBDZcSNpDVr58PP5fNqV6mJMwC5bF5c5BQMdQp2VmzLZcxEEXk%2FeBWSEvd90q2mAMxmQ2OHh2FEqovt0Kv9A7oW9FN2xW%2BZJihVirDXwD2QJZ0mQ%2Bp%2BwotfOd6FOMIbz7rwGOqUBzKZ%2FySG50uGjPUsnynwoAyyZcdDOrtvjpyo79KU6msn69CuqO5ZCsQevZoymYmt0ZtLTjXi3O49qt%2Bt0TfT7ckZjy5Cm7K2C7Z7wPDCNRoxi3gmfDVGP%2FzAzpe43btT%2BnbrUtY4Q2DBewxURqkqZf7XDPT2uO2sObT%2FG29%2BoB9T4d3YFn5j%2BXSgeS85zD3khVV59RKOmefxlGGNp1oJtDMfU%2FmUK&X-Amz-Signature=527a418ddeb908619862a62d5d630550f8f8074bf7acbc385bd2eaff19b6b863&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466752XURBC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIWWslS9WGGkUw3a03F9Hus6r5kE215BK9QIEqdrY76wIgU%2Bkcw4vPkuIrwDqdcmPXynw4sOXHknJpdaDeZA0cBgkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOfPAp4Lz4kYVR7d1SrcA7AbPde7n4Oq%2Fi2lAEkh3BM20W1PDj94Fm0tN8n3SEmtxhIS8NnO%2FUwH1ssfjjBFKsCqfmiQER%2Fij9QTsz3%2BhRrBWE%2BS77QPsK1OgsuHan9tVyLYiz7eniAJFSi0YNjvTwMkFn9AZrQrTwN7KNYyjgD46pnAi%2BYcCj3ZKU6M74AGhtvoylKv5AXV24o0GyvcmNUTrMnenrejfZTeehUN5hS758NmkuaQ451GmyAgjakpIY0YqMRTYE5WUiZmd1ekWIT3Baqa8hbX16JXK6QrLyW52JXAqPrCHYEN%2B8XrFqPdXBkTnNw0zTZCP7ElEClnAh%2BEpUzcReTFfjNfyMycxcePpcwR7l9FfgJlhfpPFzFjr8bXl9KaVgiFJOhroeajsFKPfZyISjWNPVZ3aFEspHlWPdFTKHQIYVU0y5kJo8dt1uH1TzaJBXgho5307068XkjTkXoQ1MYbW1P24f2SteyHOKLAdKIOycMAR2IBWE9ZsMpqG53rWHUUP5HvcL3mdHvjFTsFAGaqjcjoLQEMUkv9XGyr4oPjWRp%2FXUwry6PdvLcERbag5jX4pvC8flObsU7f7Rux%2FLNK05iHRlPQNw%2B9MxTRwztfwvQylIhl8BnBWooBdJGf%2B%2ByxW%2FlBMJTz7rwGOqUBrPJ%2BJzN6Mex6K5TOJkGBoGZy3Aysl6O%2F15H0%2Fmh%2FPiRKgtOobcdRWZNQuSiFgz%2FVzhBvwet2x0eosUmzULVFdK2ZLRuM9QIaABI4oiiAP7Up1MhUVu9QtU6skxbvnf1YWNyU%2BEtxaNZkNwtqfpKJSWyK5vxyGx6hF0K6AFW3oK6lA3HUo9gh%2Bde308DYYZA2QPFm6TpggSBptu5xNzUUKyeVNrqU&X-Amz-Signature=b2a09f8858e6b2ce98f8b733691594b48b37d01c838c70a1f8907f6c157b3c2a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466752XURBC%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIWWslS9WGGkUw3a03F9Hus6r5kE215BK9QIEqdrY76wIgU%2Bkcw4vPkuIrwDqdcmPXynw4sOXHknJpdaDeZA0cBgkqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOfPAp4Lz4kYVR7d1SrcA7AbPde7n4Oq%2Fi2lAEkh3BM20W1PDj94Fm0tN8n3SEmtxhIS8NnO%2FUwH1ssfjjBFKsCqfmiQER%2Fij9QTsz3%2BhRrBWE%2BS77QPsK1OgsuHan9tVyLYiz7eniAJFSi0YNjvTwMkFn9AZrQrTwN7KNYyjgD46pnAi%2BYcCj3ZKU6M74AGhtvoylKv5AXV24o0GyvcmNUTrMnenrejfZTeehUN5hS758NmkuaQ451GmyAgjakpIY0YqMRTYE5WUiZmd1ekWIT3Baqa8hbX16JXK6QrLyW52JXAqPrCHYEN%2B8XrFqPdXBkTnNw0zTZCP7ElEClnAh%2BEpUzcReTFfjNfyMycxcePpcwR7l9FfgJlhfpPFzFjr8bXl9KaVgiFJOhroeajsFKPfZyISjWNPVZ3aFEspHlWPdFTKHQIYVU0y5kJo8dt1uH1TzaJBXgho5307068XkjTkXoQ1MYbW1P24f2SteyHOKLAdKIOycMAR2IBWE9ZsMpqG53rWHUUP5HvcL3mdHvjFTsFAGaqjcjoLQEMUkv9XGyr4oPjWRp%2FXUwry6PdvLcERbag5jX4pvC8flObsU7f7Rux%2FLNK05iHRlPQNw%2B9MxTRwztfwvQylIhl8BnBWooBdJGf%2B%2ByxW%2FlBMJTz7rwGOqUBrPJ%2BJzN6Mex6K5TOJkGBoGZy3Aysl6O%2F15H0%2Fmh%2FPiRKgtOobcdRWZNQuSiFgz%2FVzhBvwet2x0eosUmzULVFdK2ZLRuM9QIaABI4oiiAP7Up1MhUVu9QtU6skxbvnf1YWNyU%2BEtxaNZkNwtqfpKJSWyK5vxyGx6hF0K6AFW3oK6lA3HUo9gh%2Bde308DYYZA2QPFm6TpggSBptu5xNzUUKyeVNrqU&X-Amz-Signature=e6bb16b0498248811670be5f469ccda4c4f0ec18c17373c2ce999467b2031bdb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVB7OEYP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCD3OA9ftK%2FvX3v79sgcJ6JhhS70Z9e5U9MvkGYpajixgIgIbKPCkvheR5xvn4SXgXqMY%2BHQGi4DGpirsSxWgmThFIqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFasGxJINCV%2BojI7oCrcA0CBcBrFQZ6UX8DUppRcaWALurue4SrENC5NIODGS%2Bnrxe%2Bw5C3lOX81Y1r%2FjqDD83ezu2zmItgxVFgwm3WuBpTN%2FXLqMSfPHrdnJ0DT7ZXCzppp08mDZzSMVh2ud1o5N5yIt5KsyO5fpFaCXpjGefWZEDQ1gt9y9sHXsnZZ6NR5tZp0XlWd5jeEl0wfjXR0Rz1C4eP8xYymrM2NwfQONyKTx0HInozsHw0A2B71PEEuJWTscKG3%2B7RZpTmq6o81fQ3xk1vmnEhI2O3qGjnrjQ2uGpN9mds3xdn63q2xFw%2FCtPdUSEkE5230dPon8c4GJDzZYwdcR9FVc%2B7HNFhKjVsSnLGvGzdqAtjT0nuS9YOx1M3jybxUWS7pEjF9g9aPe02ncuH9QjUQ6XC3pXu5p6%2ByDWTIEm5e7QR%2FXeHoSZwBrQlOQlzkTG65mFcLlMbX5kEDVR0dK%2F4368d%2B2sXFPiPknXEkp%2BsEK9ylIA4xHkLRITkPDT%2BaEjnY75SA623FEBDZcSNpDVr58PP5fNqV6mJMwC5bF5c5BQMdQp2VmzLZcxEEXk%2FeBWSEvd90q2mAMxmQ2OHh2FEqovt0Kv9A7oW9FN2xW%2BZJihVirDXwD2QJZ0mQ%2Bp%2BwotfOd6FOMIbz7rwGOqUBzKZ%2FySG50uGjPUsnynwoAyyZcdDOrtvjpyo79KU6msn69CuqO5ZCsQevZoymYmt0ZtLTjXi3O49qt%2Bt0TfT7ckZjy5Cm7K2C7Z7wPDCNRoxi3gmfDVGP%2FzAzpe43btT%2BnbrUtY4Q2DBewxURqkqZf7XDPT2uO2sObT%2FG29%2BoB9T4d3YFn5j%2BXSgeS85zD3khVV59RKOmefxlGGNp1oJtDMfU%2FmUK&X-Amz-Signature=e0d040eac56f58d02cff982f375b86f9fe709b85d7c65e55c9a6a6213487c409&X-Amz-SignedHeaders=host&x-id=GetObject)
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