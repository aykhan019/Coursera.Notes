

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3YL6V5Z%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQD%2B1PgDcGNB%2B8tsFu83Cxhk0JJsjloKOmDrkheemtpUxQIgFFEqzO6ebXBTvsBe2WXye37RZDSXOUz9b7Sn%2FAaXHIoqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDbE6dLI0Md4iwjcbircA1HOxfAehnd4LrWWDnnhtQU2yy5m7x76COV1S0us8k0N1L122v%2FqxvEOEWkkjgKZC0GKQmEtxjTByTIDrUnMF%2FxybaFMQPV36kEl7CztRjqjlymRXeob7eBBRCinnN8v5SmUehPkSQA65swI1HNPeayRcCXydlJcgGqi5NFfR02ClqrAq2vOpO5Brja%2Fkx4Ab7KAkqMZip01Hp4w6hZXGLj2BGOiKCZ4M9WRr0WidqTjgYNbLZkOfBFYk6ixBh0F%2BWUruYo4umf2EdtvjkXgzgHr9etjBG9%2FViHREJfxE%2BowtS60f6U%2BSxFvzJD%2FjANBLDRWvuN%2FcsoHBuy2Tw1HTmf39%2FbXZ0IkmzoIiOnJVWQgrGd1KxMNMio4LS%2BJn7WWwvZyKqVSv%2Bu9opXiCRe0qPyLXPGTCZsBckLstFKwvBVimAVmZEp1JYvsMciBM6aJ3rH8wyrgnnxT3YWbrsfCHlncwwkWrN9p4HwarXhwBfQOxxpcYUp8a3ZjbBJ8dC1XeEgJl60e%2BL8gDKAes7TDV%2BVKYeGc%2F50aSbDPMKKGH1Sm0Edn%2Bx0zeZ%2BIXtP4KFeWAiOeh3q%2FbksuUovlAbL7loqGinaRTQuaQyRjhYCVzcbdsyTxEXvrrg52mj0XMJ78ob8GOqUBYlWBw%2F5d2wfuzQtLsYCUS3FXq5Cm8qMkkrZ1SzpHU0K6IxEeECGLdALQfgli1uUBLP1JFlJDGSS7tzXGEFYf6PO8VgLwAGaZ5hXTLOLTOgZfDkVxsvh55r4AO0x6K1eZXiZlHqhE9tKo2aDRCYzFq%2B4b1Ja0fA5qEn5CiuqHff9F%2FSffpZqizy8wa84YDN%2Bnc6sfLYmnKfTKFgg07oV0Ja4AhF%2Bt&X-Amz-Signature=536fec086d45f98fe63d3f48ac1877e93cf4cb92198132305fc344ee884d63c3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3YL6V5Z%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQD%2B1PgDcGNB%2B8tsFu83Cxhk0JJsjloKOmDrkheemtpUxQIgFFEqzO6ebXBTvsBe2WXye37RZDSXOUz9b7Sn%2FAaXHIoqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDbE6dLI0Md4iwjcbircA1HOxfAehnd4LrWWDnnhtQU2yy5m7x76COV1S0us8k0N1L122v%2FqxvEOEWkkjgKZC0GKQmEtxjTByTIDrUnMF%2FxybaFMQPV36kEl7CztRjqjlymRXeob7eBBRCinnN8v5SmUehPkSQA65swI1HNPeayRcCXydlJcgGqi5NFfR02ClqrAq2vOpO5Brja%2Fkx4Ab7KAkqMZip01Hp4w6hZXGLj2BGOiKCZ4M9WRr0WidqTjgYNbLZkOfBFYk6ixBh0F%2BWUruYo4umf2EdtvjkXgzgHr9etjBG9%2FViHREJfxE%2BowtS60f6U%2BSxFvzJD%2FjANBLDRWvuN%2FcsoHBuy2Tw1HTmf39%2FbXZ0IkmzoIiOnJVWQgrGd1KxMNMio4LS%2BJn7WWwvZyKqVSv%2Bu9opXiCRe0qPyLXPGTCZsBckLstFKwvBVimAVmZEp1JYvsMciBM6aJ3rH8wyrgnnxT3YWbrsfCHlncwwkWrN9p4HwarXhwBfQOxxpcYUp8a3ZjbBJ8dC1XeEgJl60e%2BL8gDKAes7TDV%2BVKYeGc%2F50aSbDPMKKGH1Sm0Edn%2Bx0zeZ%2BIXtP4KFeWAiOeh3q%2FbksuUovlAbL7loqGinaRTQuaQyRjhYCVzcbdsyTxEXvrrg52mj0XMJ78ob8GOqUBYlWBw%2F5d2wfuzQtLsYCUS3FXq5Cm8qMkkrZ1SzpHU0K6IxEeECGLdALQfgli1uUBLP1JFlJDGSS7tzXGEFYf6PO8VgLwAGaZ5hXTLOLTOgZfDkVxsvh55r4AO0x6K1eZXiZlHqhE9tKo2aDRCYzFq%2B4b1Ja0fA5qEn5CiuqHff9F%2FSffpZqizy8wa84YDN%2Bnc6sfLYmnKfTKFgg07oV0Ja4AhF%2Bt&X-Amz-Signature=8509129df60b599c3708a06cc40baf53278723b30362eafd5335d62ae9e735b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3YL6V5Z%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQD%2B1PgDcGNB%2B8tsFu83Cxhk0JJsjloKOmDrkheemtpUxQIgFFEqzO6ebXBTvsBe2WXye37RZDSXOUz9b7Sn%2FAaXHIoqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDbE6dLI0Md4iwjcbircA1HOxfAehnd4LrWWDnnhtQU2yy5m7x76COV1S0us8k0N1L122v%2FqxvEOEWkkjgKZC0GKQmEtxjTByTIDrUnMF%2FxybaFMQPV36kEl7CztRjqjlymRXeob7eBBRCinnN8v5SmUehPkSQA65swI1HNPeayRcCXydlJcgGqi5NFfR02ClqrAq2vOpO5Brja%2Fkx4Ab7KAkqMZip01Hp4w6hZXGLj2BGOiKCZ4M9WRr0WidqTjgYNbLZkOfBFYk6ixBh0F%2BWUruYo4umf2EdtvjkXgzgHr9etjBG9%2FViHREJfxE%2BowtS60f6U%2BSxFvzJD%2FjANBLDRWvuN%2FcsoHBuy2Tw1HTmf39%2FbXZ0IkmzoIiOnJVWQgrGd1KxMNMio4LS%2BJn7WWwvZyKqVSv%2Bu9opXiCRe0qPyLXPGTCZsBckLstFKwvBVimAVmZEp1JYvsMciBM6aJ3rH8wyrgnnxT3YWbrsfCHlncwwkWrN9p4HwarXhwBfQOxxpcYUp8a3ZjbBJ8dC1XeEgJl60e%2BL8gDKAes7TDV%2BVKYeGc%2F50aSbDPMKKGH1Sm0Edn%2Bx0zeZ%2BIXtP4KFeWAiOeh3q%2FbksuUovlAbL7loqGinaRTQuaQyRjhYCVzcbdsyTxEXvrrg52mj0XMJ78ob8GOqUBYlWBw%2F5d2wfuzQtLsYCUS3FXq5Cm8qMkkrZ1SzpHU0K6IxEeECGLdALQfgli1uUBLP1JFlJDGSS7tzXGEFYf6PO8VgLwAGaZ5hXTLOLTOgZfDkVxsvh55r4AO0x6K1eZXiZlHqhE9tKo2aDRCYzFq%2B4b1Ja0fA5qEn5CiuqHff9F%2FSffpZqizy8wa84YDN%2Bnc6sfLYmnKfTKFgg07oV0Ja4AhF%2Bt&X-Amz-Signature=dc580fa91b34d388092331be31245e3088a7d3df1196ec4354e66b6a8a77d4d4&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUSGLQ5U%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCDK8TGYt%2BcUfnl5zd7MbBKXU7UVY4rARL1LqYi1UirsgIgdOz3gcb%2FhSUO7%2F%2B0dlYIfTClSbzHDZ5%2F3RJENdM%2FQUUqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcQ0xRNcDF6MOh%2FYCrcA6bMR1Mwr1QVNDWtSrmuBMRzcGqAZH8k%2FiBgxuLY7U5nRLOhb3FfGgVRIwf%2BVnyMCaxMpif3V1KU6DV2MsS1XCDAmzeW8Y6S9jczsVOG9MGHIO7uu%2F3kP7IOkB02EeBr4CdhVleWjp9qUztPcG%2FcoWW4QbYk%2F3HcgxtgJJ2fAGLcuZ68MvDQZ%2FRkUtGkbWBqQR3KAOFdzC2kLMJcyUAccV5b6QJ1zrBiZg42mLnbpa2eXMdq0bNMgZ3hs0GROMWd9ExEgVm9tJpC5QKCsgYJPEYlO8tR1UQCCwOlNfno0UAbBo3RHfOMRj0V7CnYi9v4B8IviG4i4CaWr6AeL%2FCsURlNZvv60%2FzZkP%2BxyvkYO0VWCrNA9yUaUuq1mHzWTf4L2shy3K%2FYeMkDNBgPIq%2Bxklrk1GajtOb6x4TWBqTI%2FA52SfKdod%2Bwi%2BilNde6NcHYnqwo83QIOkCFraGnDP2KVF445To1UYmLwTxUg1iXRPcYF9Luqx%2Bo%2FbZT%2Fee9GC6DmW0OCdCrfmY7RzW%2FYaw4R4eyU0%2FaJKlC1wBW3bZ0Zp4LwXbHe3FEZrNE85tzX0qoizsYXaCG3dx5SH9aJyItDaOlNX1ZHFFxYvYWJzz9LpADjlgh86eVk3MJjQTtML38ob8GOqUBXPTQR12sQ6P73dBkJbLqpecfvOD4P4AJ7FtZWkKPpOdDLorCydLMvWyyrsxePpC03%2BHvA%2FUPtEhf1riNjuROx1JgwesUWWoRmvjOS5gn%2F7fLfQR81o2qGYcACBs7zZxENQmYjjiowmr3B916L5N979UcOFHWMQQYVU9syB%2FjdCn%2FmiOgz9hNHGRi7QAXCS63yRCAuMvMHnCnSJSBPAFkfs50IxX3&X-Amz-Signature=57b28e423471811dbd4af3f8dff07b1f48d72a3cfe19c2fc2a80216822108001&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUSGLQ5U%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCDK8TGYt%2BcUfnl5zd7MbBKXU7UVY4rARL1LqYi1UirsgIgdOz3gcb%2FhSUO7%2F%2B0dlYIfTClSbzHDZ5%2F3RJENdM%2FQUUqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcQ0xRNcDF6MOh%2FYCrcA6bMR1Mwr1QVNDWtSrmuBMRzcGqAZH8k%2FiBgxuLY7U5nRLOhb3FfGgVRIwf%2BVnyMCaxMpif3V1KU6DV2MsS1XCDAmzeW8Y6S9jczsVOG9MGHIO7uu%2F3kP7IOkB02EeBr4CdhVleWjp9qUztPcG%2FcoWW4QbYk%2F3HcgxtgJJ2fAGLcuZ68MvDQZ%2FRkUtGkbWBqQR3KAOFdzC2kLMJcyUAccV5b6QJ1zrBiZg42mLnbpa2eXMdq0bNMgZ3hs0GROMWd9ExEgVm9tJpC5QKCsgYJPEYlO8tR1UQCCwOlNfno0UAbBo3RHfOMRj0V7CnYi9v4B8IviG4i4CaWr6AeL%2FCsURlNZvv60%2FzZkP%2BxyvkYO0VWCrNA9yUaUuq1mHzWTf4L2shy3K%2FYeMkDNBgPIq%2Bxklrk1GajtOb6x4TWBqTI%2FA52SfKdod%2Bwi%2BilNde6NcHYnqwo83QIOkCFraGnDP2KVF445To1UYmLwTxUg1iXRPcYF9Luqx%2Bo%2FbZT%2Fee9GC6DmW0OCdCrfmY7RzW%2FYaw4R4eyU0%2FaJKlC1wBW3bZ0Zp4LwXbHe3FEZrNE85tzX0qoizsYXaCG3dx5SH9aJyItDaOlNX1ZHFFxYvYWJzz9LpADjlgh86eVk3MJjQTtML38ob8GOqUBXPTQR12sQ6P73dBkJbLqpecfvOD4P4AJ7FtZWkKPpOdDLorCydLMvWyyrsxePpC03%2BHvA%2FUPtEhf1riNjuROx1JgwesUWWoRmvjOS5gn%2F7fLfQR81o2qGYcACBs7zZxENQmYjjiowmr3B916L5N979UcOFHWMQQYVU9syB%2FjdCn%2FmiOgz9hNHGRi7QAXCS63yRCAuMvMHnCnSJSBPAFkfs50IxX3&X-Amz-Signature=8ce6a02c61d20ae2cf4be023488985e94aeca63ec66d73a04a8fc2a6ffbddf00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3YL6V5Z%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQD%2B1PgDcGNB%2B8tsFu83Cxhk0JJsjloKOmDrkheemtpUxQIgFFEqzO6ebXBTvsBe2WXye37RZDSXOUz9b7Sn%2FAaXHIoqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDbE6dLI0Md4iwjcbircA1HOxfAehnd4LrWWDnnhtQU2yy5m7x76COV1S0us8k0N1L122v%2FqxvEOEWkkjgKZC0GKQmEtxjTByTIDrUnMF%2FxybaFMQPV36kEl7CztRjqjlymRXeob7eBBRCinnN8v5SmUehPkSQA65swI1HNPeayRcCXydlJcgGqi5NFfR02ClqrAq2vOpO5Brja%2Fkx4Ab7KAkqMZip01Hp4w6hZXGLj2BGOiKCZ4M9WRr0WidqTjgYNbLZkOfBFYk6ixBh0F%2BWUruYo4umf2EdtvjkXgzgHr9etjBG9%2FViHREJfxE%2BowtS60f6U%2BSxFvzJD%2FjANBLDRWvuN%2FcsoHBuy2Tw1HTmf39%2FbXZ0IkmzoIiOnJVWQgrGd1KxMNMio4LS%2BJn7WWwvZyKqVSv%2Bu9opXiCRe0qPyLXPGTCZsBckLstFKwvBVimAVmZEp1JYvsMciBM6aJ3rH8wyrgnnxT3YWbrsfCHlncwwkWrN9p4HwarXhwBfQOxxpcYUp8a3ZjbBJ8dC1XeEgJl60e%2BL8gDKAes7TDV%2BVKYeGc%2F50aSbDPMKKGH1Sm0Edn%2Bx0zeZ%2BIXtP4KFeWAiOeh3q%2FbksuUovlAbL7loqGinaRTQuaQyRjhYCVzcbdsyTxEXvrrg52mj0XMJ78ob8GOqUBYlWBw%2F5d2wfuzQtLsYCUS3FXq5Cm8qMkkrZ1SzpHU0K6IxEeECGLdALQfgli1uUBLP1JFlJDGSS7tzXGEFYf6PO8VgLwAGaZ5hXTLOLTOgZfDkVxsvh55r4AO0x6K1eZXiZlHqhE9tKo2aDRCYzFq%2B4b1Ja0fA5qEn5CiuqHff9F%2FSffpZqizy8wa84YDN%2Bnc6sfLYmnKfTKFgg07oV0Ja4AhF%2Bt&X-Amz-Signature=d6b2e208fd687abb0412d8959931d88d5c813f4d44d6a3abca16254a3d68117f&X-Amz-SignedHeaders=host&x-id=GetObject)
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