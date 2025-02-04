

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVEWJLPU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIFjjeqdSb1wRnfrTq3CEXo8NPq1k%2FDHeuQYe0vTTvxxYAiEAh4gwr2QWZC9jqG3nwS9ohb2K24U44JWd4Ve2BNxV0kAq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDNnfKMfbg12V0%2FGv6yrcA5r3ZuU59uYKAmp75rG1O6FlsGr70ZgzrNsiM8txc6EV5koKy8NgasrO8qeJt7C3WMoHXLl1sFUOe6yxDtLBxRBFyT7bkgLAKk9KsZpxdH2eGT9YaeUq0rwuIcdf7CXIq8%2B%2BXDqXg5YGv7cfV9zzQkyX0v6AZq%2F3wL1pWNVAUslTTZnnifKDRnxhkVe646Mp91VSxpRfUQq41PG0WgEn9gNxJSIS%2BTX1PretjKTAAtNFygzM2cU5g8NiQFT2RD7GLC3%2BdDOwN4yDscG5ub9OVaM5aLhbfA7YR%2FLsdUlyp5GyJrJI7byv8DQpYhVzFmPWR0DUz41J0vFUHXLWErK8%2B%2F0vSqRN5kB6v1OYDxB2aUeXzak9nJrCqbhpD92gxykfEq2FtxP14EXNZsMFOaFl9RFO03lfkBx8vYbk8ACry5q96G0BbA5%2Fo9nqr3ovLtJQQNSV3mXU66bwr9F21I1OIMoqv3ZhqlIOE4uR9vbKlT2XKMsEq1f%2BRByuZej1CcdNgCn%2FBXSGqM%2F339jJtPMRCvlGvW45OE5bNlH2YjLd%2FX5a0djXkJfZP5MSfi4gy6G6AjFzSUMBkBPWDI4SR77w8M7mbe%2FIp67rqXcXqbmgtiqKYHf2j3OU7fCqtUfMMLaTh70GOqUBzQmqYdQRpXV0SE745T71H%2F5YrqHn%2FiRhI6GDVPt4khkPZ9Om%2FNOsNf5O2hxPZ30Zy0Gw2k5AKUzUxCJJUE5R8c6fkzL3UhZeWHW7MLqP%2BSe4m2OnXnxK3%2FhzmxL011eor8nonyl8IzGak%2FEm9dHPtsZm0EunbsxMyPX7UKXpk3Sc5NaXGy0iIYwfpJRYcORr%2Bh%2BpeCWB3QQdKuK5gMprjkGpyUek&X-Amz-Signature=c470bacdf1f8bfa03aa8db017fe5da86912cffec029478fa56d39e3fc8c56615&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVEWJLPU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIFjjeqdSb1wRnfrTq3CEXo8NPq1k%2FDHeuQYe0vTTvxxYAiEAh4gwr2QWZC9jqG3nwS9ohb2K24U44JWd4Ve2BNxV0kAq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDNnfKMfbg12V0%2FGv6yrcA5r3ZuU59uYKAmp75rG1O6FlsGr70ZgzrNsiM8txc6EV5koKy8NgasrO8qeJt7C3WMoHXLl1sFUOe6yxDtLBxRBFyT7bkgLAKk9KsZpxdH2eGT9YaeUq0rwuIcdf7CXIq8%2B%2BXDqXg5YGv7cfV9zzQkyX0v6AZq%2F3wL1pWNVAUslTTZnnifKDRnxhkVe646Mp91VSxpRfUQq41PG0WgEn9gNxJSIS%2BTX1PretjKTAAtNFygzM2cU5g8NiQFT2RD7GLC3%2BdDOwN4yDscG5ub9OVaM5aLhbfA7YR%2FLsdUlyp5GyJrJI7byv8DQpYhVzFmPWR0DUz41J0vFUHXLWErK8%2B%2F0vSqRN5kB6v1OYDxB2aUeXzak9nJrCqbhpD92gxykfEq2FtxP14EXNZsMFOaFl9RFO03lfkBx8vYbk8ACry5q96G0BbA5%2Fo9nqr3ovLtJQQNSV3mXU66bwr9F21I1OIMoqv3ZhqlIOE4uR9vbKlT2XKMsEq1f%2BRByuZej1CcdNgCn%2FBXSGqM%2F339jJtPMRCvlGvW45OE5bNlH2YjLd%2FX5a0djXkJfZP5MSfi4gy6G6AjFzSUMBkBPWDI4SR77w8M7mbe%2FIp67rqXcXqbmgtiqKYHf2j3OU7fCqtUfMMLaTh70GOqUBzQmqYdQRpXV0SE745T71H%2F5YrqHn%2FiRhI6GDVPt4khkPZ9Om%2FNOsNf5O2hxPZ30Zy0Gw2k5AKUzUxCJJUE5R8c6fkzL3UhZeWHW7MLqP%2BSe4m2OnXnxK3%2FhzmxL011eor8nonyl8IzGak%2FEm9dHPtsZm0EunbsxMyPX7UKXpk3Sc5NaXGy0iIYwfpJRYcORr%2Bh%2BpeCWB3QQdKuK5gMprjkGpyUek&X-Amz-Signature=77a1fabccc57fd571b98c1555f0a30a72b9230eff5e016db7b2a2c7775397f2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVEWJLPU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIFjjeqdSb1wRnfrTq3CEXo8NPq1k%2FDHeuQYe0vTTvxxYAiEAh4gwr2QWZC9jqG3nwS9ohb2K24U44JWd4Ve2BNxV0kAq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDNnfKMfbg12V0%2FGv6yrcA5r3ZuU59uYKAmp75rG1O6FlsGr70ZgzrNsiM8txc6EV5koKy8NgasrO8qeJt7C3WMoHXLl1sFUOe6yxDtLBxRBFyT7bkgLAKk9KsZpxdH2eGT9YaeUq0rwuIcdf7CXIq8%2B%2BXDqXg5YGv7cfV9zzQkyX0v6AZq%2F3wL1pWNVAUslTTZnnifKDRnxhkVe646Mp91VSxpRfUQq41PG0WgEn9gNxJSIS%2BTX1PretjKTAAtNFygzM2cU5g8NiQFT2RD7GLC3%2BdDOwN4yDscG5ub9OVaM5aLhbfA7YR%2FLsdUlyp5GyJrJI7byv8DQpYhVzFmPWR0DUz41J0vFUHXLWErK8%2B%2F0vSqRN5kB6v1OYDxB2aUeXzak9nJrCqbhpD92gxykfEq2FtxP14EXNZsMFOaFl9RFO03lfkBx8vYbk8ACry5q96G0BbA5%2Fo9nqr3ovLtJQQNSV3mXU66bwr9F21I1OIMoqv3ZhqlIOE4uR9vbKlT2XKMsEq1f%2BRByuZej1CcdNgCn%2FBXSGqM%2F339jJtPMRCvlGvW45OE5bNlH2YjLd%2FX5a0djXkJfZP5MSfi4gy6G6AjFzSUMBkBPWDI4SR77w8M7mbe%2FIp67rqXcXqbmgtiqKYHf2j3OU7fCqtUfMMLaTh70GOqUBzQmqYdQRpXV0SE745T71H%2F5YrqHn%2FiRhI6GDVPt4khkPZ9Om%2FNOsNf5O2hxPZ30Zy0Gw2k5AKUzUxCJJUE5R8c6fkzL3UhZeWHW7MLqP%2BSe4m2OnXnxK3%2FhzmxL011eor8nonyl8IzGak%2FEm9dHPtsZm0EunbsxMyPX7UKXpk3Sc5NaXGy0iIYwfpJRYcORr%2Bh%2BpeCWB3QQdKuK5gMprjkGpyUek&X-Amz-Signature=c159c3dc46d772a8517d4815c10472c825cefbcc20a993115e744b68af7a1093&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDQBBHAN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIQCX8P%2BDtR0vFE1V%2FEhj8y6%2FmxaosLEFaL6fhtdoEtpg3AIgL2%2BKoyUX9w9282T0Ve2jiVXBiqObRVP0ODbgPqNKGkcq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDEiR532RPD47GLT2hircA7bjJrgnGtTXiE3OB0RmMhSiwjhAjDv6w9Cvmd%2BozZMlIrUvHS7HvMGKPu2jnccHz%2FJVmMYOibgIdNjx1kWYGrmyic6c6tzuciw0j%2FzDwA8Op07m1ynDPDqlql%2FLL8Q7eiY%2B89qvCX7UBAle0MPDWQ14CgvcHXpUCJFqVHH7QFk4x5NfxaZR41t%2FeyXaYVfMQEIu2Wk3pyjmpT30FRfOLKXqS08Of%2FTmyrmgpBqHz7oB3arUgBuzuzv%2FKco2etg9NEnTMMchSBxMj2B0gDY0h6so1WaqIRtwDoOPDzxyf14vbdqNGkruhEbX4FNMlNylWlPArfAkuG%2B%2Bshpq48zCm7%2F6sFevoFMadTIwbC%2FINBzlm2hgiLT3bDzWSrqi9IPmCkURX5HiEJqAEHzhEFsjmV4RFvTb9exEIK1X7pxWZHWqH2hEXn3HcifeXjvW%2FltMo%2Fa6r9Az4EMAfV1eEV5tvkCasdd%2F89ihhLDj3tU1fvkOHAfhVuo13SVjB2wUdtOV9XqF0SniQSl5HDxiSDqmdqOiyCJpXZ%2FBNtBcSnGnadepdihx8g2yYrjH9qvzNuJ9%2BRaFwf7iWeoNzKqPa7%2BFLgP0VKeVU9gNVpPM%2Bm6EZFVinVy5k4NtlAfZqrUKMMyRh70GOqUBxrJyAp797U1Q%2FesfIHZcbeXGU5tqGTP7MIhvh%2FZw9k0Dnz1HfgbSU5M5WYfpOxDcj2K7gxui2IADW%2BMq8tmJxsx6oBC%2BBcvlBGr54lazAJQ0N1%2FpupdRl0py7IxGaS86kZy2EKVfQ1W2PZ9EjNRpjmS0XY7RZZ2%2Bp60GIqdOWP%2BMcnmX4lVPpA8VHlcH%2FCx86RHDkA4TClIZYG4jR%2BqRLJoBXo6v&X-Amz-Signature=53497aa4c12e7e40435d2102dfe7d84ea1763ad62ca153b867a2e8ff9cf84b11&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDQBBHAN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIQCX8P%2BDtR0vFE1V%2FEhj8y6%2FmxaosLEFaL6fhtdoEtpg3AIgL2%2BKoyUX9w9282T0Ve2jiVXBiqObRVP0ODbgPqNKGkcq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDEiR532RPD47GLT2hircA7bjJrgnGtTXiE3OB0RmMhSiwjhAjDv6w9Cvmd%2BozZMlIrUvHS7HvMGKPu2jnccHz%2FJVmMYOibgIdNjx1kWYGrmyic6c6tzuciw0j%2FzDwA8Op07m1ynDPDqlql%2FLL8Q7eiY%2B89qvCX7UBAle0MPDWQ14CgvcHXpUCJFqVHH7QFk4x5NfxaZR41t%2FeyXaYVfMQEIu2Wk3pyjmpT30FRfOLKXqS08Of%2FTmyrmgpBqHz7oB3arUgBuzuzv%2FKco2etg9NEnTMMchSBxMj2B0gDY0h6so1WaqIRtwDoOPDzxyf14vbdqNGkruhEbX4FNMlNylWlPArfAkuG%2B%2Bshpq48zCm7%2F6sFevoFMadTIwbC%2FINBzlm2hgiLT3bDzWSrqi9IPmCkURX5HiEJqAEHzhEFsjmV4RFvTb9exEIK1X7pxWZHWqH2hEXn3HcifeXjvW%2FltMo%2Fa6r9Az4EMAfV1eEV5tvkCasdd%2F89ihhLDj3tU1fvkOHAfhVuo13SVjB2wUdtOV9XqF0SniQSl5HDxiSDqmdqOiyCJpXZ%2FBNtBcSnGnadepdihx8g2yYrjH9qvzNuJ9%2BRaFwf7iWeoNzKqPa7%2BFLgP0VKeVU9gNVpPM%2Bm6EZFVinVy5k4NtlAfZqrUKMMyRh70GOqUBxrJyAp797U1Q%2FesfIHZcbeXGU5tqGTP7MIhvh%2FZw9k0Dnz1HfgbSU5M5WYfpOxDcj2K7gxui2IADW%2BMq8tmJxsx6oBC%2BBcvlBGr54lazAJQ0N1%2FpupdRl0py7IxGaS86kZy2EKVfQ1W2PZ9EjNRpjmS0XY7RZZ2%2Bp60GIqdOWP%2BMcnmX4lVPpA8VHlcH%2FCx86RHDkA4TClIZYG4jR%2BqRLJoBXo6v&X-Amz-Signature=94f4a1777ea779a67dbca9be72530a203d0e6aca45de9f41c634737c2c3d5218&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVEWJLPU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIFjjeqdSb1wRnfrTq3CEXo8NPq1k%2FDHeuQYe0vTTvxxYAiEAh4gwr2QWZC9jqG3nwS9ohb2K24U44JWd4Ve2BNxV0kAq%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDNnfKMfbg12V0%2FGv6yrcA5r3ZuU59uYKAmp75rG1O6FlsGr70ZgzrNsiM8txc6EV5koKy8NgasrO8qeJt7C3WMoHXLl1sFUOe6yxDtLBxRBFyT7bkgLAKk9KsZpxdH2eGT9YaeUq0rwuIcdf7CXIq8%2B%2BXDqXg5YGv7cfV9zzQkyX0v6AZq%2F3wL1pWNVAUslTTZnnifKDRnxhkVe646Mp91VSxpRfUQq41PG0WgEn9gNxJSIS%2BTX1PretjKTAAtNFygzM2cU5g8NiQFT2RD7GLC3%2BdDOwN4yDscG5ub9OVaM5aLhbfA7YR%2FLsdUlyp5GyJrJI7byv8DQpYhVzFmPWR0DUz41J0vFUHXLWErK8%2B%2F0vSqRN5kB6v1OYDxB2aUeXzak9nJrCqbhpD92gxykfEq2FtxP14EXNZsMFOaFl9RFO03lfkBx8vYbk8ACry5q96G0BbA5%2Fo9nqr3ovLtJQQNSV3mXU66bwr9F21I1OIMoqv3ZhqlIOE4uR9vbKlT2XKMsEq1f%2BRByuZej1CcdNgCn%2FBXSGqM%2F339jJtPMRCvlGvW45OE5bNlH2YjLd%2FX5a0djXkJfZP5MSfi4gy6G6AjFzSUMBkBPWDI4SR77w8M7mbe%2FIp67rqXcXqbmgtiqKYHf2j3OU7fCqtUfMMLaTh70GOqUBzQmqYdQRpXV0SE745T71H%2F5YrqHn%2FiRhI6GDVPt4khkPZ9Om%2FNOsNf5O2hxPZ30Zy0Gw2k5AKUzUxCJJUE5R8c6fkzL3UhZeWHW7MLqP%2BSe4m2OnXnxK3%2FhzmxL011eor8nonyl8IzGak%2FEm9dHPtsZm0EunbsxMyPX7UKXpk3Sc5NaXGy0iIYwfpJRYcORr%2Bh%2BpeCWB3QQdKuK5gMprjkGpyUek&X-Amz-Signature=a4f07f67c2863bf127a90e622c042da576d66fc90df5efbde8ac9e884f986598&X-Amz-SignedHeaders=host&x-id=GetObject)
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