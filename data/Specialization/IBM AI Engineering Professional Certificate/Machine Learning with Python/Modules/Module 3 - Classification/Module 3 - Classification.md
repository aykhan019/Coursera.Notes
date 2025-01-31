

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GVG4NQ3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2alCppjLpQ8BTCbaa0Vim9JWz7NS%2FmVyQef4CA8ytCAiEAnu1sXY6B%2B6bE4iOdPEpwdh3bziP2spmJJTOX9gFSk08qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBRaY4xEDDLVqt7KQCrcA1eq6pRGeLv%2BpF%2FdJGQe%2BUYLdJt%2B45atnUStxEKL0adhyTVAykBG5Jyrd2VGC0tlGEsoZsmqewAc4a95qq1yMSdroYN5SF3iqXu10SYjptpgIFpcOzKC0i4BYsnyshx0kxZ5nNmhg3yupN9NnAWV7P72CmOABrCkZgV90ANvysBWR%2Bd%2FkOF6qdY74Zl9SgW28yIIHE%2Bmxd%2BRP%2BqNl0zLH7oNkFgKoeg1guAdBBuAhcRQKcaK2YtOZ6iW0rCbNiScodEaXAXtScsXzzSYHoSCrkIJAwuLZAe17GWBNdRd4u7eeqc496kii%2B%2BYZm9afoSwH1gEgd6GD8jclgLlQlzp9OeIDAhn9lwspmojZfdPqlFPyVeb2dNy6DTo87O8SQpNSYhY0OSovh7%2BPYnqVOg%2Fpg4RLiaHUPguFabyFL2BPHR7n6nAKqSjwzZDXAlI1DNEZkUW%2Ftplf4c63y%2FhssGRtC03FCZyP9Yvdwb8Q3MeUebGSanxuDYx%2BvUKhAWbNfQShu4mJMRHFfVzrp332BUNRB0%2BCD9%2F7sFz8SYZwTdmWJL6vA8sXNlVqOT9V5FwoPlTUAUs9fti2oK6%2BzYurXbz3t4GiX5QD9xW7LMMpfWiMU4FKSSDRYehAf5vKp4kMN%2FQ8LwGOqUBrnvQhRlNXClWxSt2%2F7CQw%2Btg2tnepKrVzUDF3KWLIJSHcvYzQ4K7VlAkHPVb7QtkppW8eEWSIfjm39Dz3I0iYqzwYUN7%2FXqPRDnXzmR%2FZekptX9ASzFIrw40PrMSqkLxapREyh0Td0jYHsemb0k4fuKIL5aMbSaEcy4plwpVQcVhGnxdttTeBpEo9EF%2BLxPpsUtJIw%2FS7DQuVTjRz6oUIJehgH0j&X-Amz-Signature=4c940413fccb14a90b84bb877cbd807c621b736c5ea6245af3d8c27268e7ab3f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GVG4NQ3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2alCppjLpQ8BTCbaa0Vim9JWz7NS%2FmVyQef4CA8ytCAiEAnu1sXY6B%2B6bE4iOdPEpwdh3bziP2spmJJTOX9gFSk08qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBRaY4xEDDLVqt7KQCrcA1eq6pRGeLv%2BpF%2FdJGQe%2BUYLdJt%2B45atnUStxEKL0adhyTVAykBG5Jyrd2VGC0tlGEsoZsmqewAc4a95qq1yMSdroYN5SF3iqXu10SYjptpgIFpcOzKC0i4BYsnyshx0kxZ5nNmhg3yupN9NnAWV7P72CmOABrCkZgV90ANvysBWR%2Bd%2FkOF6qdY74Zl9SgW28yIIHE%2Bmxd%2BRP%2BqNl0zLH7oNkFgKoeg1guAdBBuAhcRQKcaK2YtOZ6iW0rCbNiScodEaXAXtScsXzzSYHoSCrkIJAwuLZAe17GWBNdRd4u7eeqc496kii%2B%2BYZm9afoSwH1gEgd6GD8jclgLlQlzp9OeIDAhn9lwspmojZfdPqlFPyVeb2dNy6DTo87O8SQpNSYhY0OSovh7%2BPYnqVOg%2Fpg4RLiaHUPguFabyFL2BPHR7n6nAKqSjwzZDXAlI1DNEZkUW%2Ftplf4c63y%2FhssGRtC03FCZyP9Yvdwb8Q3MeUebGSanxuDYx%2BvUKhAWbNfQShu4mJMRHFfVzrp332BUNRB0%2BCD9%2F7sFz8SYZwTdmWJL6vA8sXNlVqOT9V5FwoPlTUAUs9fti2oK6%2BzYurXbz3t4GiX5QD9xW7LMMpfWiMU4FKSSDRYehAf5vKp4kMN%2FQ8LwGOqUBrnvQhRlNXClWxSt2%2F7CQw%2Btg2tnepKrVzUDF3KWLIJSHcvYzQ4K7VlAkHPVb7QtkppW8eEWSIfjm39Dz3I0iYqzwYUN7%2FXqPRDnXzmR%2FZekptX9ASzFIrw40PrMSqkLxapREyh0Td0jYHsemb0k4fuKIL5aMbSaEcy4plwpVQcVhGnxdttTeBpEo9EF%2BLxPpsUtJIw%2FS7DQuVTjRz6oUIJehgH0j&X-Amz-Signature=b183d1cb9b5db4ab6413a26643957a048f068b3d353b6a18881b709393f3c092&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GVG4NQ3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2alCppjLpQ8BTCbaa0Vim9JWz7NS%2FmVyQef4CA8ytCAiEAnu1sXY6B%2B6bE4iOdPEpwdh3bziP2spmJJTOX9gFSk08qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBRaY4xEDDLVqt7KQCrcA1eq6pRGeLv%2BpF%2FdJGQe%2BUYLdJt%2B45atnUStxEKL0adhyTVAykBG5Jyrd2VGC0tlGEsoZsmqewAc4a95qq1yMSdroYN5SF3iqXu10SYjptpgIFpcOzKC0i4BYsnyshx0kxZ5nNmhg3yupN9NnAWV7P72CmOABrCkZgV90ANvysBWR%2Bd%2FkOF6qdY74Zl9SgW28yIIHE%2Bmxd%2BRP%2BqNl0zLH7oNkFgKoeg1guAdBBuAhcRQKcaK2YtOZ6iW0rCbNiScodEaXAXtScsXzzSYHoSCrkIJAwuLZAe17GWBNdRd4u7eeqc496kii%2B%2BYZm9afoSwH1gEgd6GD8jclgLlQlzp9OeIDAhn9lwspmojZfdPqlFPyVeb2dNy6DTo87O8SQpNSYhY0OSovh7%2BPYnqVOg%2Fpg4RLiaHUPguFabyFL2BPHR7n6nAKqSjwzZDXAlI1DNEZkUW%2Ftplf4c63y%2FhssGRtC03FCZyP9Yvdwb8Q3MeUebGSanxuDYx%2BvUKhAWbNfQShu4mJMRHFfVzrp332BUNRB0%2BCD9%2F7sFz8SYZwTdmWJL6vA8sXNlVqOT9V5FwoPlTUAUs9fti2oK6%2BzYurXbz3t4GiX5QD9xW7LMMpfWiMU4FKSSDRYehAf5vKp4kMN%2FQ8LwGOqUBrnvQhRlNXClWxSt2%2F7CQw%2Btg2tnepKrVzUDF3KWLIJSHcvYzQ4K7VlAkHPVb7QtkppW8eEWSIfjm39Dz3I0iYqzwYUN7%2FXqPRDnXzmR%2FZekptX9ASzFIrw40PrMSqkLxapREyh0Td0jYHsemb0k4fuKIL5aMbSaEcy4plwpVQcVhGnxdttTeBpEo9EF%2BLxPpsUtJIw%2FS7DQuVTjRz6oUIJehgH0j&X-Amz-Signature=3487358b8d0ff83b94204c49a76aadfaeb461ee2ee429d45573ac4151a2b0f66&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZ5BE64K%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDs0Xrm3u4bkQ6Svp%2FvqPV1T1Lr8S26PZUp%2F1GZbraFBgIhAPLHVSsbFu9O1PE9a1j1UpJRDkQvQXuhTSr8Tv7gXzjPKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGZhM11%2BUeDL1pmGoq3AMWnRpyPGKmUM2uuIm8OuTh%2Bm%2FIKxosfHgDtCdjQNLbTg9sWS2pvQvnn7%2BGuplz95W%2B2PK1%2BCBm9VcT9yKwMoUDm5hloIyeoREZtj6aPz%2FqJQ82GVcejmADICgtXJvuIftyoa5Vf19dg9eCQ28wcsxJC25zK1y2sZoIPjHN06t%2Bzh96NeGd5AiENm7S9Y0%2FjX%2FIgeFQjhDd4qTA%2FKVuha%2BLSEWVXAExINTMA9BH38EPDmNYEVKWsP4x1HsPDSK%2FEO4mrnPzeavzCDvR5Kz1MlZ5wwYvldMngIR1bJzexlopnDE9tJQtJUeaoJNPXvFSFz%2FcRpk9NxAeuDzNcEYXfibnYD4Tnrz1qU4bF4YbJXIpoG9oGDcQCsziXkufz7R0HFE%2FiV7agUGOYf589kWBDGS8DPBNcmlcyb7AVm60ehdG9to0MZ0ZPtV9ttsWHdtl%2BjGtIOD%2Bqlm29zQ9e5wwDC7ixRei9LnfYcfHEVnuaOXzMzTvSr6HyKzi42EA7ceROLlhIcXcdCUInTtl5MEDzRzgumU7rIgJglCjJFOAfYu%2B%2FR9RklS27WBEBAbjauu2SPy9TvTPoGMghQAt5wvVSmHb%2FBNro8L06TTJvK6p4vfDRDZf4hK0yS64n23jRTCz0PC8BjqkAcs3ghYXkpxq13x%2BclMA4BKuZ3pthy0MEyTb7tbpqQrFPn%2B5LmkR4ln3C7fIUpq1F78AkTpqYyqxONawRqpYxzd%2BeXGxkYQSbni%2BMqW9MTBG8JDAGnsvJDDv9OCSrazeIfhe9uxdmTZOvQN7K%2B%2F2jrOiEktRzhLBeALbJo3OsC133dZVuvBfjxViM%2Bw86KCESSSXyUAHQFyaYTFnTWHOC1M9ykpB&X-Amz-Signature=4cd7c2801a5a608ebfbe8f9f2f34c94089bc973eb2b94eee72dbe27164c748c8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZ5BE64K%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDs0Xrm3u4bkQ6Svp%2FvqPV1T1Lr8S26PZUp%2F1GZbraFBgIhAPLHVSsbFu9O1PE9a1j1UpJRDkQvQXuhTSr8Tv7gXzjPKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGZhM11%2BUeDL1pmGoq3AMWnRpyPGKmUM2uuIm8OuTh%2Bm%2FIKxosfHgDtCdjQNLbTg9sWS2pvQvnn7%2BGuplz95W%2B2PK1%2BCBm9VcT9yKwMoUDm5hloIyeoREZtj6aPz%2FqJQ82GVcejmADICgtXJvuIftyoa5Vf19dg9eCQ28wcsxJC25zK1y2sZoIPjHN06t%2Bzh96NeGd5AiENm7S9Y0%2FjX%2FIgeFQjhDd4qTA%2FKVuha%2BLSEWVXAExINTMA9BH38EPDmNYEVKWsP4x1HsPDSK%2FEO4mrnPzeavzCDvR5Kz1MlZ5wwYvldMngIR1bJzexlopnDE9tJQtJUeaoJNPXvFSFz%2FcRpk9NxAeuDzNcEYXfibnYD4Tnrz1qU4bF4YbJXIpoG9oGDcQCsziXkufz7R0HFE%2FiV7agUGOYf589kWBDGS8DPBNcmlcyb7AVm60ehdG9to0MZ0ZPtV9ttsWHdtl%2BjGtIOD%2Bqlm29zQ9e5wwDC7ixRei9LnfYcfHEVnuaOXzMzTvSr6HyKzi42EA7ceROLlhIcXcdCUInTtl5MEDzRzgumU7rIgJglCjJFOAfYu%2B%2FR9RklS27WBEBAbjauu2SPy9TvTPoGMghQAt5wvVSmHb%2FBNro8L06TTJvK6p4vfDRDZf4hK0yS64n23jRTCz0PC8BjqkAcs3ghYXkpxq13x%2BclMA4BKuZ3pthy0MEyTb7tbpqQrFPn%2B5LmkR4ln3C7fIUpq1F78AkTpqYyqxONawRqpYxzd%2BeXGxkYQSbni%2BMqW9MTBG8JDAGnsvJDDv9OCSrazeIfhe9uxdmTZOvQN7K%2B%2F2jrOiEktRzhLBeALbJo3OsC133dZVuvBfjxViM%2Bw86KCESSSXyUAHQFyaYTFnTWHOC1M9ykpB&X-Amz-Signature=566bcb06397876110f8f749d832fa583a69213f96f77b36573a88e184393d13a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GVG4NQ3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH2alCppjLpQ8BTCbaa0Vim9JWz7NS%2FmVyQef4CA8ytCAiEAnu1sXY6B%2B6bE4iOdPEpwdh3bziP2spmJJTOX9gFSk08qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBRaY4xEDDLVqt7KQCrcA1eq6pRGeLv%2BpF%2FdJGQe%2BUYLdJt%2B45atnUStxEKL0adhyTVAykBG5Jyrd2VGC0tlGEsoZsmqewAc4a95qq1yMSdroYN5SF3iqXu10SYjptpgIFpcOzKC0i4BYsnyshx0kxZ5nNmhg3yupN9NnAWV7P72CmOABrCkZgV90ANvysBWR%2Bd%2FkOF6qdY74Zl9SgW28yIIHE%2Bmxd%2BRP%2BqNl0zLH7oNkFgKoeg1guAdBBuAhcRQKcaK2YtOZ6iW0rCbNiScodEaXAXtScsXzzSYHoSCrkIJAwuLZAe17GWBNdRd4u7eeqc496kii%2B%2BYZm9afoSwH1gEgd6GD8jclgLlQlzp9OeIDAhn9lwspmojZfdPqlFPyVeb2dNy6DTo87O8SQpNSYhY0OSovh7%2BPYnqVOg%2Fpg4RLiaHUPguFabyFL2BPHR7n6nAKqSjwzZDXAlI1DNEZkUW%2Ftplf4c63y%2FhssGRtC03FCZyP9Yvdwb8Q3MeUebGSanxuDYx%2BvUKhAWbNfQShu4mJMRHFfVzrp332BUNRB0%2BCD9%2F7sFz8SYZwTdmWJL6vA8sXNlVqOT9V5FwoPlTUAUs9fti2oK6%2BzYurXbz3t4GiX5QD9xW7LMMpfWiMU4FKSSDRYehAf5vKp4kMN%2FQ8LwGOqUBrnvQhRlNXClWxSt2%2F7CQw%2Btg2tnepKrVzUDF3KWLIJSHcvYzQ4K7VlAkHPVb7QtkppW8eEWSIfjm39Dz3I0iYqzwYUN7%2FXqPRDnXzmR%2FZekptX9ASzFIrw40PrMSqkLxapREyh0Td0jYHsemb0k4fuKIL5aMbSaEcy4plwpVQcVhGnxdttTeBpEo9EF%2BLxPpsUtJIw%2FS7DQuVTjRz6oUIJehgH0j&X-Amz-Signature=5754e939a136d24a7f140c662eb4ceed2c9ec3d3bdcb826a500f460a668e3e57&X-Amz-SignedHeaders=host&x-id=GetObject)
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