

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEW267WY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHkFeO2TsMLxEOTuXB7UI%2FiQ7JujE3dbWNuhzT%2FbbYtDAiAhAVYH7rvdqocLBz9npODHf4osTNeeFQ7WfJjeTjY9GiqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlyYAoUy0CCZez%2FTHKtwDKJNrVBOgnDZM%2BHGTKUWl4plZTW4TsNO5h1sRvKZuxgaZSc2%2BXvcOnlKYn3gIA1FIIM%2Bm6b6%2BL%2BMA2jPeTC4hk7G%2FnJdxNMBawTodjkDD%2B533J5UEYDiu%2BxNc34HkifbdGDBMT4I%2F37hnajf5jNGc69Fofz60jH93uEFYGcQx2AZiC2i6%2Fjsr9MejPO8wN7eQ5%2B%2Bh4igTJR1Qgz3%2Faownoh%2F3G4O3YJ0L7V%2Fsn1PI6NJWfT3a1jyQOubGARt5eCYlLvKHQ%2FoTQKfEgizacVZqRsBRII5pDLuXNeCEtwegEV8jpUnI9Xn6Xq8JEL96sjdSZ1BK1quIHfsdcChlHsZYuNm8GPwHstrvY6%2Fp76a%2F3wtrVPPBoIOM0y8EdCXXvVto09DXgBueEuxGhPqrKvJS5vb3i1DSrADzuf0il35AycNoiG8gRQasYPK8YnPfVWbS%2BgN7xezot%2BLf9e6rnIh1SG427w3al3IerAyEeC0YzlFe0wocygYVcoz6toEuNoZqT9ZbBYqKPPjRg7moTZVAapSwnffGKGUxYf87tFdBcr0RthCOM2Tz88WrSJ%2B9BCRBMSmVxQmtYj1KQ8PkqIX8kDyHVzjgaprFFnfyraNiQWGaRck2FAdlNwRcJI8w7cz1vAY6pgHE6PgmwmzDKcEJQZiY4P7xGFXk5nAq3XFTpXBj2vYV2axIjYy08iINM4R8blHZ5c0K8YCl4rs7Ejhu0Xb3L7nRKGAzy9EbBWOYoQUrXK8PzVkD2QEKo%2FULvY0qHmK%2FE1D7CWsy%2FX%2FxAS7vVzMTwovZpjT4QJ8gI9LwxGpP3ZTsr3PPAq%2FKVSSYdXhvLFv9THZblWVlKNTeMxY0qXyQpeN76Hvz8dRP&X-Amz-Signature=5d6742243913955123c78f9432f623616cbb874d6fd3c126e6eacb38f2650175&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEW267WY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHkFeO2TsMLxEOTuXB7UI%2FiQ7JujE3dbWNuhzT%2FbbYtDAiAhAVYH7rvdqocLBz9npODHf4osTNeeFQ7WfJjeTjY9GiqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlyYAoUy0CCZez%2FTHKtwDKJNrVBOgnDZM%2BHGTKUWl4plZTW4TsNO5h1sRvKZuxgaZSc2%2BXvcOnlKYn3gIA1FIIM%2Bm6b6%2BL%2BMA2jPeTC4hk7G%2FnJdxNMBawTodjkDD%2B533J5UEYDiu%2BxNc34HkifbdGDBMT4I%2F37hnajf5jNGc69Fofz60jH93uEFYGcQx2AZiC2i6%2Fjsr9MejPO8wN7eQ5%2B%2Bh4igTJR1Qgz3%2Faownoh%2F3G4O3YJ0L7V%2Fsn1PI6NJWfT3a1jyQOubGARt5eCYlLvKHQ%2FoTQKfEgizacVZqRsBRII5pDLuXNeCEtwegEV8jpUnI9Xn6Xq8JEL96sjdSZ1BK1quIHfsdcChlHsZYuNm8GPwHstrvY6%2Fp76a%2F3wtrVPPBoIOM0y8EdCXXvVto09DXgBueEuxGhPqrKvJS5vb3i1DSrADzuf0il35AycNoiG8gRQasYPK8YnPfVWbS%2BgN7xezot%2BLf9e6rnIh1SG427w3al3IerAyEeC0YzlFe0wocygYVcoz6toEuNoZqT9ZbBYqKPPjRg7moTZVAapSwnffGKGUxYf87tFdBcr0RthCOM2Tz88WrSJ%2B9BCRBMSmVxQmtYj1KQ8PkqIX8kDyHVzjgaprFFnfyraNiQWGaRck2FAdlNwRcJI8w7cz1vAY6pgHE6PgmwmzDKcEJQZiY4P7xGFXk5nAq3XFTpXBj2vYV2axIjYy08iINM4R8blHZ5c0K8YCl4rs7Ejhu0Xb3L7nRKGAzy9EbBWOYoQUrXK8PzVkD2QEKo%2FULvY0qHmK%2FE1D7CWsy%2FX%2FxAS7vVzMTwovZpjT4QJ8gI9LwxGpP3ZTsr3PPAq%2FKVSSYdXhvLFv9THZblWVlKNTeMxY0qXyQpeN76Hvz8dRP&X-Amz-Signature=e83e3c49e3823ee2138836c9e5a2327854afbcda1f81b35cc8fcab482f635053&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEW267WY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHkFeO2TsMLxEOTuXB7UI%2FiQ7JujE3dbWNuhzT%2FbbYtDAiAhAVYH7rvdqocLBz9npODHf4osTNeeFQ7WfJjeTjY9GiqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlyYAoUy0CCZez%2FTHKtwDKJNrVBOgnDZM%2BHGTKUWl4plZTW4TsNO5h1sRvKZuxgaZSc2%2BXvcOnlKYn3gIA1FIIM%2Bm6b6%2BL%2BMA2jPeTC4hk7G%2FnJdxNMBawTodjkDD%2B533J5UEYDiu%2BxNc34HkifbdGDBMT4I%2F37hnajf5jNGc69Fofz60jH93uEFYGcQx2AZiC2i6%2Fjsr9MejPO8wN7eQ5%2B%2Bh4igTJR1Qgz3%2Faownoh%2F3G4O3YJ0L7V%2Fsn1PI6NJWfT3a1jyQOubGARt5eCYlLvKHQ%2FoTQKfEgizacVZqRsBRII5pDLuXNeCEtwegEV8jpUnI9Xn6Xq8JEL96sjdSZ1BK1quIHfsdcChlHsZYuNm8GPwHstrvY6%2Fp76a%2F3wtrVPPBoIOM0y8EdCXXvVto09DXgBueEuxGhPqrKvJS5vb3i1DSrADzuf0il35AycNoiG8gRQasYPK8YnPfVWbS%2BgN7xezot%2BLf9e6rnIh1SG427w3al3IerAyEeC0YzlFe0wocygYVcoz6toEuNoZqT9ZbBYqKPPjRg7moTZVAapSwnffGKGUxYf87tFdBcr0RthCOM2Tz88WrSJ%2B9BCRBMSmVxQmtYj1KQ8PkqIX8kDyHVzjgaprFFnfyraNiQWGaRck2FAdlNwRcJI8w7cz1vAY6pgHE6PgmwmzDKcEJQZiY4P7xGFXk5nAq3XFTpXBj2vYV2axIjYy08iINM4R8blHZ5c0K8YCl4rs7Ejhu0Xb3L7nRKGAzy9EbBWOYoQUrXK8PzVkD2QEKo%2FULvY0qHmK%2FE1D7CWsy%2FX%2FxAS7vVzMTwovZpjT4QJ8gI9LwxGpP3ZTsr3PPAq%2FKVSSYdXhvLFv9THZblWVlKNTeMxY0qXyQpeN76Hvz8dRP&X-Amz-Signature=589ebba2f16b00c00dbebeb49f460230c9cb3b4512a270c339b50e2bb6b06ff1&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKXCEH62%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsuzDz3ZeapziJwnv9Y4iy6Ese13I9Z8YZ5gi22VoblAIhAO8gReAKF8mHTXsEJyL%2F0ACjYn9ADtweHFXnkXBrivZMKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKhzrus%2FIFtxOTHrwq3AMwYtlWM1R3Jwd6h5%2FHJp4Wt%2F8rInZX1oQ1YVfB9n1OlYItYNhHnCXKt4SZKa4Wakw50Tr5V0FlHitytTPxvobySnayP28tulNHz60rb1ReGCUz2577uijyiwqiA9I5EvhzWnfwgKsI4N8bqPw%2BJEcw7wT7tmosDSmTw0eBFK62i9d2zJXSXrdcaf4aIhD%2Befdsu3TJvrrIvb11m6zIe24ARyQWU3D9lHRCYJNS3ww63gYWzHrVuzP8jmzQ%2FdYfPs5kkzOn5dYqRBsg40VxUY9ES26iRyb3MUD6xWJaYfiY%2BkKniR442a4%2F%2F3p8igHCBhdutOKZaICacSLGgxNsP1rJqUK%2FJw0lOD1LPBVmNQMm4LE40kIbJSdr1g063230b6pwPHXBCi0ySb4kFRYQngX9cyBSPqCtK%2BZLxRhP4A8TfH3RdXmGjRqK%2F2mN%2FUZ2dM0oqsyiGZ5BsBxycn1S9VWbmei5WGiODl4PjszuQsyNkwXASBwdrlvI6d0VCS3VW8PpK9Saf2so5ZURSIi1LGouHQJcn9GE7c5w3ZKWXCODHsacv4AfKLrvbDQxigzL52x0blI3zC2bvDM3mS8Qg41DjnC0djg2JEjeTXZ62aJvQNbNELo6haPM0HyhaTDrzPW8BjqkAUvGHpp0ML8lU34qcoMBfGMf3veric%2BVoq47mHf7jNeMWQBltrsdV7wAZEB%2FnZbs9PgsSHsCuydwK5r9Ge%2BlD4nV3Zoyv5OTeJ3VBO%2BQLf29QOUt78T%2Fdr4XS70qeVtPmDBwCiobA2CJvfkPHYMSitxyntfvmGe4ZUxxeKjl8KSVKmG809K1ATjMZc6D8eDkIKqIcy7YhUu%2BTTrQAFykZLFMJc4m&X-Amz-Signature=202ea4de37950cb4621225703307262b5c5bd9235fb452e5f712ddc1264d2b2e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKXCEH62%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsuzDz3ZeapziJwnv9Y4iy6Ese13I9Z8YZ5gi22VoblAIhAO8gReAKF8mHTXsEJyL%2F0ACjYn9ADtweHFXnkXBrivZMKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKhzrus%2FIFtxOTHrwq3AMwYtlWM1R3Jwd6h5%2FHJp4Wt%2F8rInZX1oQ1YVfB9n1OlYItYNhHnCXKt4SZKa4Wakw50Tr5V0FlHitytTPxvobySnayP28tulNHz60rb1ReGCUz2577uijyiwqiA9I5EvhzWnfwgKsI4N8bqPw%2BJEcw7wT7tmosDSmTw0eBFK62i9d2zJXSXrdcaf4aIhD%2Befdsu3TJvrrIvb11m6zIe24ARyQWU3D9lHRCYJNS3ww63gYWzHrVuzP8jmzQ%2FdYfPs5kkzOn5dYqRBsg40VxUY9ES26iRyb3MUD6xWJaYfiY%2BkKniR442a4%2F%2F3p8igHCBhdutOKZaICacSLGgxNsP1rJqUK%2FJw0lOD1LPBVmNQMm4LE40kIbJSdr1g063230b6pwPHXBCi0ySb4kFRYQngX9cyBSPqCtK%2BZLxRhP4A8TfH3RdXmGjRqK%2F2mN%2FUZ2dM0oqsyiGZ5BsBxycn1S9VWbmei5WGiODl4PjszuQsyNkwXASBwdrlvI6d0VCS3VW8PpK9Saf2so5ZURSIi1LGouHQJcn9GE7c5w3ZKWXCODHsacv4AfKLrvbDQxigzL52x0blI3zC2bvDM3mS8Qg41DjnC0djg2JEjeTXZ62aJvQNbNELo6haPM0HyhaTDrzPW8BjqkAUvGHpp0ML8lU34qcoMBfGMf3veric%2BVoq47mHf7jNeMWQBltrsdV7wAZEB%2FnZbs9PgsSHsCuydwK5r9Ge%2BlD4nV3Zoyv5OTeJ3VBO%2BQLf29QOUt78T%2Fdr4XS70qeVtPmDBwCiobA2CJvfkPHYMSitxyntfvmGe4ZUxxeKjl8KSVKmG809K1ATjMZc6D8eDkIKqIcy7YhUu%2BTTrQAFykZLFMJc4m&X-Amz-Signature=3f498b6593ca887b3452b0dc5705c42e5e91ee15ccac169dd13f1cdd3a2273e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEW267WY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHkFeO2TsMLxEOTuXB7UI%2FiQ7JujE3dbWNuhzT%2FbbYtDAiAhAVYH7rvdqocLBz9npODHf4osTNeeFQ7WfJjeTjY9GiqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlyYAoUy0CCZez%2FTHKtwDKJNrVBOgnDZM%2BHGTKUWl4plZTW4TsNO5h1sRvKZuxgaZSc2%2BXvcOnlKYn3gIA1FIIM%2Bm6b6%2BL%2BMA2jPeTC4hk7G%2FnJdxNMBawTodjkDD%2B533J5UEYDiu%2BxNc34HkifbdGDBMT4I%2F37hnajf5jNGc69Fofz60jH93uEFYGcQx2AZiC2i6%2Fjsr9MejPO8wN7eQ5%2B%2Bh4igTJR1Qgz3%2Faownoh%2F3G4O3YJ0L7V%2Fsn1PI6NJWfT3a1jyQOubGARt5eCYlLvKHQ%2FoTQKfEgizacVZqRsBRII5pDLuXNeCEtwegEV8jpUnI9Xn6Xq8JEL96sjdSZ1BK1quIHfsdcChlHsZYuNm8GPwHstrvY6%2Fp76a%2F3wtrVPPBoIOM0y8EdCXXvVto09DXgBueEuxGhPqrKvJS5vb3i1DSrADzuf0il35AycNoiG8gRQasYPK8YnPfVWbS%2BgN7xezot%2BLf9e6rnIh1SG427w3al3IerAyEeC0YzlFe0wocygYVcoz6toEuNoZqT9ZbBYqKPPjRg7moTZVAapSwnffGKGUxYf87tFdBcr0RthCOM2Tz88WrSJ%2B9BCRBMSmVxQmtYj1KQ8PkqIX8kDyHVzjgaprFFnfyraNiQWGaRck2FAdlNwRcJI8w7cz1vAY6pgHE6PgmwmzDKcEJQZiY4P7xGFXk5nAq3XFTpXBj2vYV2axIjYy08iINM4R8blHZ5c0K8YCl4rs7Ejhu0Xb3L7nRKGAzy9EbBWOYoQUrXK8PzVkD2QEKo%2FULvY0qHmK%2FE1D7CWsy%2FX%2FxAS7vVzMTwovZpjT4QJ8gI9LwxGpP3ZTsr3PPAq%2FKVSSYdXhvLFv9THZblWVlKNTeMxY0qXyQpeN76Hvz8dRP&X-Amz-Signature=a74230b0db79d8d234fe52067215e5530891f9a7d2b4fc4cf87d5b048554e05a&X-Amz-SignedHeaders=host&x-id=GetObject)
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