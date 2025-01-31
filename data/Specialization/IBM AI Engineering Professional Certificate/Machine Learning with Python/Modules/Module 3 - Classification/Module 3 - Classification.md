

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NJVRAXG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTC2R0eGLF%2Fyq5WUmAkOqGxHOzMAlIJv%2BtS9JiQTCg%2FAIgevgCvy2mxY88eT2L%2FqRKLPYKKBLW%2FdBzeYF%2BK0zpYcgqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGa86LITefZ3gHPX4SrcA%2FUKZnu3da%2FYMgh5t9K3jatngDTPpj4YE6j7o943FyPMc3q1ZaeJIbqkQNFJEGy1vRYdQuPVFpG%2BE4pUFun50cOS08O2Lma456schHsM0IfgdmZfghR7NMpWh12OnTrJxvGCliki9nQmFnXsqrZVC%2BksMo87MQJGa3IK20ELyD9aV8dTR4GfMLmk%2FbUJyW87inNjQsFHTyZhGHaQZBjh%2FB1rv6VVEHeu%2BbNalNE4%2Foz1PshfmHjyHGmXHG0hhydguOXJI6trV7qO3PGR%2BZLp5f6C1HnIAxpaDz3g5Gs4ha0uRkmr%2BjHj6JVC3lX4cET8e1FeQP016zbcr7XnnIuXlzkqy8Ig03iLInYF6jqrYY7%2FLEJRT4%2BcI4dxzfusuSpxGhGCg5SSOtQmvBeQITn87e6FYf38kzJR3kR9rXGgRpyG0LfaG1eJ0gRZlzstONEtzoMYop0%2B5D%2BK3VRtdhAshalc0jzdHeorBryiXWTbOXcwmBplkmDo%2BfXVHoV5bv%2FGCPM%2FjCbs6A8%2FIZKS4SBR8EToSCfWDLx%2BtJymFtuibCT41kFWFD8mZI31nBQ1JWAtwTT%2B9q9bEVa7lxgslOYwnkS4wa01fedtQ9sniIIdQSyNhbpBszLFymqp%2BiTsMO7Q8LwGOqUBnhrZulutUC7OcenEo3OuhWChg8oozznxUEhIhnTQM3Alkar%2Fnd%2FUW2TbRUzugHNeO1UxZWrrx%2BgMlbDoeNxaL31YoFxSe28HgAYQS9XYVqqCwJYXqAyvmcZ8f0DSrAOo21UaEWpqq048CQPS9gERA7cGAaagweEiDEMIbpTHm99m6w2I4fI1PvInwphJxHVrx3kwcYn3MQDdREXnGiwtXtLS6aW8&X-Amz-Signature=e6cb5cb04d1325323c1dbac1187abf6dd28f377e4369b3604b2aff891e774842&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NJVRAXG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTC2R0eGLF%2Fyq5WUmAkOqGxHOzMAlIJv%2BtS9JiQTCg%2FAIgevgCvy2mxY88eT2L%2FqRKLPYKKBLW%2FdBzeYF%2BK0zpYcgqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGa86LITefZ3gHPX4SrcA%2FUKZnu3da%2FYMgh5t9K3jatngDTPpj4YE6j7o943FyPMc3q1ZaeJIbqkQNFJEGy1vRYdQuPVFpG%2BE4pUFun50cOS08O2Lma456schHsM0IfgdmZfghR7NMpWh12OnTrJxvGCliki9nQmFnXsqrZVC%2BksMo87MQJGa3IK20ELyD9aV8dTR4GfMLmk%2FbUJyW87inNjQsFHTyZhGHaQZBjh%2FB1rv6VVEHeu%2BbNalNE4%2Foz1PshfmHjyHGmXHG0hhydguOXJI6trV7qO3PGR%2BZLp5f6C1HnIAxpaDz3g5Gs4ha0uRkmr%2BjHj6JVC3lX4cET8e1FeQP016zbcr7XnnIuXlzkqy8Ig03iLInYF6jqrYY7%2FLEJRT4%2BcI4dxzfusuSpxGhGCg5SSOtQmvBeQITn87e6FYf38kzJR3kR9rXGgRpyG0LfaG1eJ0gRZlzstONEtzoMYop0%2B5D%2BK3VRtdhAshalc0jzdHeorBryiXWTbOXcwmBplkmDo%2BfXVHoV5bv%2FGCPM%2FjCbs6A8%2FIZKS4SBR8EToSCfWDLx%2BtJymFtuibCT41kFWFD8mZI31nBQ1JWAtwTT%2B9q9bEVa7lxgslOYwnkS4wa01fedtQ9sniIIdQSyNhbpBszLFymqp%2BiTsMO7Q8LwGOqUBnhrZulutUC7OcenEo3OuhWChg8oozznxUEhIhnTQM3Alkar%2Fnd%2FUW2TbRUzugHNeO1UxZWrrx%2BgMlbDoeNxaL31YoFxSe28HgAYQS9XYVqqCwJYXqAyvmcZ8f0DSrAOo21UaEWpqq048CQPS9gERA7cGAaagweEiDEMIbpTHm99m6w2I4fI1PvInwphJxHVrx3kwcYn3MQDdREXnGiwtXtLS6aW8&X-Amz-Signature=bb97f954de9d339489a1a31647e12ee84e6af36effc730ae5c0da437787b8bf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NJVRAXG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTC2R0eGLF%2Fyq5WUmAkOqGxHOzMAlIJv%2BtS9JiQTCg%2FAIgevgCvy2mxY88eT2L%2FqRKLPYKKBLW%2FdBzeYF%2BK0zpYcgqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGa86LITefZ3gHPX4SrcA%2FUKZnu3da%2FYMgh5t9K3jatngDTPpj4YE6j7o943FyPMc3q1ZaeJIbqkQNFJEGy1vRYdQuPVFpG%2BE4pUFun50cOS08O2Lma456schHsM0IfgdmZfghR7NMpWh12OnTrJxvGCliki9nQmFnXsqrZVC%2BksMo87MQJGa3IK20ELyD9aV8dTR4GfMLmk%2FbUJyW87inNjQsFHTyZhGHaQZBjh%2FB1rv6VVEHeu%2BbNalNE4%2Foz1PshfmHjyHGmXHG0hhydguOXJI6trV7qO3PGR%2BZLp5f6C1HnIAxpaDz3g5Gs4ha0uRkmr%2BjHj6JVC3lX4cET8e1FeQP016zbcr7XnnIuXlzkqy8Ig03iLInYF6jqrYY7%2FLEJRT4%2BcI4dxzfusuSpxGhGCg5SSOtQmvBeQITn87e6FYf38kzJR3kR9rXGgRpyG0LfaG1eJ0gRZlzstONEtzoMYop0%2B5D%2BK3VRtdhAshalc0jzdHeorBryiXWTbOXcwmBplkmDo%2BfXVHoV5bv%2FGCPM%2FjCbs6A8%2FIZKS4SBR8EToSCfWDLx%2BtJymFtuibCT41kFWFD8mZI31nBQ1JWAtwTT%2B9q9bEVa7lxgslOYwnkS4wa01fedtQ9sniIIdQSyNhbpBszLFymqp%2BiTsMO7Q8LwGOqUBnhrZulutUC7OcenEo3OuhWChg8oozznxUEhIhnTQM3Alkar%2Fnd%2FUW2TbRUzugHNeO1UxZWrrx%2BgMlbDoeNxaL31YoFxSe28HgAYQS9XYVqqCwJYXqAyvmcZ8f0DSrAOo21UaEWpqq048CQPS9gERA7cGAaagweEiDEMIbpTHm99m6w2I4fI1PvInwphJxHVrx3kwcYn3MQDdREXnGiwtXtLS6aW8&X-Amz-Signature=3a69bba49ee4e41692f6043d85e9b5b987d0ba650dec0d38d9c96505b0d4b7f4&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVCWTOYJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGECplSVxOiHurA1GPkoLLrkUAy%2F9vakdwHKshvBbisDAiAK6DIT05RabEZ0M%2BwBvr4ofH%2BK6BSmvzgOJAtshHAeECqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTg451wwn5exWBW8XKtwDayFgb0qXNWrZs%2FYq3U3bIKzt4iI%2BLc6mFtJngoOEF2peSma1XqIXVbD15ctpQBFObfnA5IikMmOvOA0ciVdF5vBCmczohbQSuLL5wWDJrIYFY59xPyUvs%2B24XUpYqHbXF1RHGlAgkviEeKRPs1sqy79jgnOM2nRF%2FGW5%2FcejxlQUbnyZASTjl5SeFe%2BivOysHLWBP6umGE118U0uU8TSPDuuy6Rx4NoshihqCnMt0Tcy5Fy8W%2F6eRFjGKYEMa%2B%2BFVmOVKFLNtM4a7Ct7UK2iZBOLeI%2Bxf8N6V0Fz575yZhqY7uev3Cer43RTkxFLFl5TYDsCZKOWI0HG4qwaYHr6zHkPrMCCA36cbGnVpjt3Cmd%2FkEi1YTH6ysAEtCVPNNENsCVLh8YbVL3S9hiPQJ7JvPOxMD0rhl5zuPLsXHZFdJAjGTW6RVw4TwoIj%2Fd1lJhWmcYYXtVxdwlmb4yh4LxbD2m60q5KmTykkSsouSsvRjRPIcksLFw16Pg%2B6Sm1j4Vurpb5Gu23RwHzBLck7pIFdli8r52%2BY7SMIFKoTd9vSMVi7Zy4151rHeQk%2B5Hbpt6JMTT36QVUDO83ASKUsPhpM6Own233SrJVhnwEs75mOTvbrCEM5Llr40fgNggw7tDwvAY6pgFlJNJRq%2FrTQ%2FPUh0QqX8iC7l152vCJaDo%2BRFouKqL%2BVrfU6chxhSzVgKIpr%2BeXwHn0dKDlf2q%2BvVrk9s14LQPo3of3pT%2FPSXaJy5ery6b6J8xUECMcgg8pIFirwEkTLj%2Fjv2BjLs95xOyDhwigyoEywLeqdqaKg5VmlWjuPEWFwcQskwGlk481mPyJBDtNgSwlCRnG7luxq9weKrxVon7uOEtD9Cg2&X-Amz-Signature=83f320aabd56c01edbd569303592a568d6d8b69fe531e7b4e7f22e9c0972e737&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVCWTOYJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGECplSVxOiHurA1GPkoLLrkUAy%2F9vakdwHKshvBbisDAiAK6DIT05RabEZ0M%2BwBvr4ofH%2BK6BSmvzgOJAtshHAeECqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTg451wwn5exWBW8XKtwDayFgb0qXNWrZs%2FYq3U3bIKzt4iI%2BLc6mFtJngoOEF2peSma1XqIXVbD15ctpQBFObfnA5IikMmOvOA0ciVdF5vBCmczohbQSuLL5wWDJrIYFY59xPyUvs%2B24XUpYqHbXF1RHGlAgkviEeKRPs1sqy79jgnOM2nRF%2FGW5%2FcejxlQUbnyZASTjl5SeFe%2BivOysHLWBP6umGE118U0uU8TSPDuuy6Rx4NoshihqCnMt0Tcy5Fy8W%2F6eRFjGKYEMa%2B%2BFVmOVKFLNtM4a7Ct7UK2iZBOLeI%2Bxf8N6V0Fz575yZhqY7uev3Cer43RTkxFLFl5TYDsCZKOWI0HG4qwaYHr6zHkPrMCCA36cbGnVpjt3Cmd%2FkEi1YTH6ysAEtCVPNNENsCVLh8YbVL3S9hiPQJ7JvPOxMD0rhl5zuPLsXHZFdJAjGTW6RVw4TwoIj%2Fd1lJhWmcYYXtVxdwlmb4yh4LxbD2m60q5KmTykkSsouSsvRjRPIcksLFw16Pg%2B6Sm1j4Vurpb5Gu23RwHzBLck7pIFdli8r52%2BY7SMIFKoTd9vSMVi7Zy4151rHeQk%2B5Hbpt6JMTT36QVUDO83ASKUsPhpM6Own233SrJVhnwEs75mOTvbrCEM5Llr40fgNggw7tDwvAY6pgFlJNJRq%2FrTQ%2FPUh0QqX8iC7l152vCJaDo%2BRFouKqL%2BVrfU6chxhSzVgKIpr%2BeXwHn0dKDlf2q%2BvVrk9s14LQPo3of3pT%2FPSXaJy5ery6b6J8xUECMcgg8pIFirwEkTLj%2Fjv2BjLs95xOyDhwigyoEywLeqdqaKg5VmlWjuPEWFwcQskwGlk481mPyJBDtNgSwlCRnG7luxq9weKrxVon7uOEtD9Cg2&X-Amz-Signature=7e8cb788e47b544afd6a102adc2e784996f3e77410fc3dca64543a2b518ef1cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NJVRAXG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTC2R0eGLF%2Fyq5WUmAkOqGxHOzMAlIJv%2BtS9JiQTCg%2FAIgevgCvy2mxY88eT2L%2FqRKLPYKKBLW%2FdBzeYF%2BK0zpYcgqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGa86LITefZ3gHPX4SrcA%2FUKZnu3da%2FYMgh5t9K3jatngDTPpj4YE6j7o943FyPMc3q1ZaeJIbqkQNFJEGy1vRYdQuPVFpG%2BE4pUFun50cOS08O2Lma456schHsM0IfgdmZfghR7NMpWh12OnTrJxvGCliki9nQmFnXsqrZVC%2BksMo87MQJGa3IK20ELyD9aV8dTR4GfMLmk%2FbUJyW87inNjQsFHTyZhGHaQZBjh%2FB1rv6VVEHeu%2BbNalNE4%2Foz1PshfmHjyHGmXHG0hhydguOXJI6trV7qO3PGR%2BZLp5f6C1HnIAxpaDz3g5Gs4ha0uRkmr%2BjHj6JVC3lX4cET8e1FeQP016zbcr7XnnIuXlzkqy8Ig03iLInYF6jqrYY7%2FLEJRT4%2BcI4dxzfusuSpxGhGCg5SSOtQmvBeQITn87e6FYf38kzJR3kR9rXGgRpyG0LfaG1eJ0gRZlzstONEtzoMYop0%2B5D%2BK3VRtdhAshalc0jzdHeorBryiXWTbOXcwmBplkmDo%2BfXVHoV5bv%2FGCPM%2FjCbs6A8%2FIZKS4SBR8EToSCfWDLx%2BtJymFtuibCT41kFWFD8mZI31nBQ1JWAtwTT%2B9q9bEVa7lxgslOYwnkS4wa01fedtQ9sniIIdQSyNhbpBszLFymqp%2BiTsMO7Q8LwGOqUBnhrZulutUC7OcenEo3OuhWChg8oozznxUEhIhnTQM3Alkar%2Fnd%2FUW2TbRUzugHNeO1UxZWrrx%2BgMlbDoeNxaL31YoFxSe28HgAYQS9XYVqqCwJYXqAyvmcZ8f0DSrAOo21UaEWpqq048CQPS9gERA7cGAaagweEiDEMIbpTHm99m6w2I4fI1PvInwphJxHVrx3kwcYn3MQDdREXnGiwtXtLS6aW8&X-Amz-Signature=0c729fc3e1e62163ddbb19e000ea0e8655f08ecb306ae630c6f6694e18f70efe&X-Amz-SignedHeaders=host&x-id=GetObject)
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