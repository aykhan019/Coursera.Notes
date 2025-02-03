

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM5RC37B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDJJXJ%2B0ULwzSO6ULd637zluX5ZmJGLIAGskM2alMdDsAiAHqhb2gfGJ9CraQxWO97%2FDUABdjcA9OCxpPeGUCRAewyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3nj48JUQLbWeyp03KtwD8o11eX9PD4yqiIFaEQFzgEjlTjpmnfPpQrL%2Bah9VhwZ1A4Q%2FbffTGzVPl9f3yqphHCVVdsHZYIe3svP0YkjiMQFkE%2FuVMHF7PqAm9dIwlr%2Fh%2BihBuXt07lDKGn2wWJExB5nYSj4QevVeAtUIJXcQdhHYGW%2Fltg4pUhulwGGH6wp3%2FP9Uo4Qdv2At3biGi9vQr4ZEbozJRJNHWPyFdXmmYGG8eRF%2FCGxt0khIu9%2B6mPqVYOOXu13RIB7SFQ3EmXeKet8TmWKRF8Oqb0xlzn9VF4OgFsTXfWcGlB2vX9qRyuBVZcq7%2BD%2BIZgZDK3hL69%2BeHl3tKN75I6DaS5ZtWeh9mSe7XThe3Q1GD%2FzXBtoOWHqxK1sUINIioYwRRbtKXa6b3o3tfAnavR2ptljKQzvDztkDG1SZB8OizbtUnIvn0D9w7yb73tYPLV621JOdoqS4M0tIH3pGU5KB63rqDo95KGHqTh5VYTYPPZNlmRH3SP47dzGix1Bi1MPWO57Y5SM%2FTRLhKqLPBwbGlkaf0mQ4RLgtn3S2A1m9P2KexhoCfSn%2BiVqWSoXh4GEdTCvBXCdBYsw7TkVzPEsxpevEFM7j%2FNGtWlmyX3TRA2gMZXaPWuAc0AD632BGrWQTmLUwvcCAvQY6pgEJR3kmL5F%2BvNUcsg5mmqtPWY9yYTO%2FpcGsV65qxjlv8XJ5RQLVa0%2FTfURIFqmUNvVfACVUa8oK0IRSkFJZL6%2FFw7CnIZIlOYcwm7t0iFIcG%2FWX%2FY%2BV7LcwbAWuJJuAByUY3lkaQhETkp9lrrOH72Payaf1mkoMECevcDB%2Fu%2Fo46wYp2wHb49Q9T780Uv4qIRL2PZnDNwYNgpXbTCGMnP7RYVxNMgrE&X-Amz-Signature=eb38f34e7f41b9c07f504bd116295ee6cca397e61d05bf783da0044f5fd77342&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM5RC37B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDJJXJ%2B0ULwzSO6ULd637zluX5ZmJGLIAGskM2alMdDsAiAHqhb2gfGJ9CraQxWO97%2FDUABdjcA9OCxpPeGUCRAewyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3nj48JUQLbWeyp03KtwD8o11eX9PD4yqiIFaEQFzgEjlTjpmnfPpQrL%2Bah9VhwZ1A4Q%2FbffTGzVPl9f3yqphHCVVdsHZYIe3svP0YkjiMQFkE%2FuVMHF7PqAm9dIwlr%2Fh%2BihBuXt07lDKGn2wWJExB5nYSj4QevVeAtUIJXcQdhHYGW%2Fltg4pUhulwGGH6wp3%2FP9Uo4Qdv2At3biGi9vQr4ZEbozJRJNHWPyFdXmmYGG8eRF%2FCGxt0khIu9%2B6mPqVYOOXu13RIB7SFQ3EmXeKet8TmWKRF8Oqb0xlzn9VF4OgFsTXfWcGlB2vX9qRyuBVZcq7%2BD%2BIZgZDK3hL69%2BeHl3tKN75I6DaS5ZtWeh9mSe7XThe3Q1GD%2FzXBtoOWHqxK1sUINIioYwRRbtKXa6b3o3tfAnavR2ptljKQzvDztkDG1SZB8OizbtUnIvn0D9w7yb73tYPLV621JOdoqS4M0tIH3pGU5KB63rqDo95KGHqTh5VYTYPPZNlmRH3SP47dzGix1Bi1MPWO57Y5SM%2FTRLhKqLPBwbGlkaf0mQ4RLgtn3S2A1m9P2KexhoCfSn%2BiVqWSoXh4GEdTCvBXCdBYsw7TkVzPEsxpevEFM7j%2FNGtWlmyX3TRA2gMZXaPWuAc0AD632BGrWQTmLUwvcCAvQY6pgEJR3kmL5F%2BvNUcsg5mmqtPWY9yYTO%2FpcGsV65qxjlv8XJ5RQLVa0%2FTfURIFqmUNvVfACVUa8oK0IRSkFJZL6%2FFw7CnIZIlOYcwm7t0iFIcG%2FWX%2FY%2BV7LcwbAWuJJuAByUY3lkaQhETkp9lrrOH72Payaf1mkoMECevcDB%2Fu%2Fo46wYp2wHb49Q9T780Uv4qIRL2PZnDNwYNgpXbTCGMnP7RYVxNMgrE&X-Amz-Signature=adc8ed1f598cba259e98b20557da5ee458552317bf252fef3baa833532ee2013&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM5RC37B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDJJXJ%2B0ULwzSO6ULd637zluX5ZmJGLIAGskM2alMdDsAiAHqhb2gfGJ9CraQxWO97%2FDUABdjcA9OCxpPeGUCRAewyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3nj48JUQLbWeyp03KtwD8o11eX9PD4yqiIFaEQFzgEjlTjpmnfPpQrL%2Bah9VhwZ1A4Q%2FbffTGzVPl9f3yqphHCVVdsHZYIe3svP0YkjiMQFkE%2FuVMHF7PqAm9dIwlr%2Fh%2BihBuXt07lDKGn2wWJExB5nYSj4QevVeAtUIJXcQdhHYGW%2Fltg4pUhulwGGH6wp3%2FP9Uo4Qdv2At3biGi9vQr4ZEbozJRJNHWPyFdXmmYGG8eRF%2FCGxt0khIu9%2B6mPqVYOOXu13RIB7SFQ3EmXeKet8TmWKRF8Oqb0xlzn9VF4OgFsTXfWcGlB2vX9qRyuBVZcq7%2BD%2BIZgZDK3hL69%2BeHl3tKN75I6DaS5ZtWeh9mSe7XThe3Q1GD%2FzXBtoOWHqxK1sUINIioYwRRbtKXa6b3o3tfAnavR2ptljKQzvDztkDG1SZB8OizbtUnIvn0D9w7yb73tYPLV621JOdoqS4M0tIH3pGU5KB63rqDo95KGHqTh5VYTYPPZNlmRH3SP47dzGix1Bi1MPWO57Y5SM%2FTRLhKqLPBwbGlkaf0mQ4RLgtn3S2A1m9P2KexhoCfSn%2BiVqWSoXh4GEdTCvBXCdBYsw7TkVzPEsxpevEFM7j%2FNGtWlmyX3TRA2gMZXaPWuAc0AD632BGrWQTmLUwvcCAvQY6pgEJR3kmL5F%2BvNUcsg5mmqtPWY9yYTO%2FpcGsV65qxjlv8XJ5RQLVa0%2FTfURIFqmUNvVfACVUa8oK0IRSkFJZL6%2FFw7CnIZIlOYcwm7t0iFIcG%2FWX%2FY%2BV7LcwbAWuJJuAByUY3lkaQhETkp9lrrOH72Payaf1mkoMECevcDB%2Fu%2Fo46wYp2wHb49Q9T780Uv4qIRL2PZnDNwYNgpXbTCGMnP7RYVxNMgrE&X-Amz-Signature=4225e2252b7062489a0a17d902852cf763897824e486fd02b4df3f88e8fea3fa&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLSRRENN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVmLMombSRY67erTrH%2BzGvbjQq6oYwrKDCOC9cG%2BTG1QIgAPvraZAlZz07ahXtlbxJoABLK0517Rg%2F2aIiP4vCxGMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO4wUwvmzt6GpKkO1SrcA4cJv6Vjb2Rz56dgqUraxKgJVxVzsNsI2wkbFtFIj7kobnHhcy7DQMj3F7A2DuzBLgg%2Fn0eID4IB39FbFZgeysBERrhJhmX6nIG%2BOe7wKqA%2BGywHAtsjcT4qqyFU66mtnu0XUaqY7w%2BiTQdxQLEZIN3rIC9xC4qq%2Bjw6k42c9voTWtJ5qhX9k0I6UYD0416xsgMU8kD0GuBEM7vrTTUjd0KKlQ6nWfIOUP5hzV0jlIZz8HvC%2BO0s4rAb%2FY0cd5%2F%2FpHCOyoAc9MvDfAfFKRbA6n7snzhSovBM6Y%2BLzM0fD6TGlRfrQ2J5XNSA9AN%2FF2sZ4Mh7Kbyz5Ygw%2FL9nOWKnlN6YwPoueoAGuCTpZzmMmCmtbSTQwSBJqP5Fh072RijgZSwdsnO7mY1FmtUW%2BVTiIUmEt8eYuoeYdDF6HB%2BcN7OE6OS%2B6MefVnrxZmFx5n5y368jzfPu%2FvZA0tCgb4UodopLIArFhf9pC%2FRZ2M317WRPWPDWkRz4sz%2BGy10s7HljtLoeYiplfls%2FaSfcDUjr2nvqnQSGJbosnMjitE0MSydwDqcKrZ1yxKJSx4FqMAwc5zViVqYcuPXUdLh5nJ9qF9JSt0ILJAe6lSCbN2BJf6yMYYrtUWyArWA0IH1oMPG%2FgL0GOqUB33kbmuEOXma28P7gxGsIHIOZtUXTfK0gqyWacZoxeysi%2FHswKpgnuqntNPjQFLi4UnKY5%2FLKWNTUQCVWb96o7hCgLyZnqR12lfH3npKWvDqtlRHp%2FeyKRxw1QzK3maxMQgPEIkgD1Z793bPsdiMjC7IFHn3wZZ%2BkG8rSl7Sv7Fp0CQuDcWDJf2Xpw7cT5H6PyakSIVlqo5l4UhSDjdcYajAxOmK9&X-Amz-Signature=c05239a81f45b37f625da58947d42d21692ef7320e9811275b2ec05d79629826&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLSRRENN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVmLMombSRY67erTrH%2BzGvbjQq6oYwrKDCOC9cG%2BTG1QIgAPvraZAlZz07ahXtlbxJoABLK0517Rg%2F2aIiP4vCxGMqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO4wUwvmzt6GpKkO1SrcA4cJv6Vjb2Rz56dgqUraxKgJVxVzsNsI2wkbFtFIj7kobnHhcy7DQMj3F7A2DuzBLgg%2Fn0eID4IB39FbFZgeysBERrhJhmX6nIG%2BOe7wKqA%2BGywHAtsjcT4qqyFU66mtnu0XUaqY7w%2BiTQdxQLEZIN3rIC9xC4qq%2Bjw6k42c9voTWtJ5qhX9k0I6UYD0416xsgMU8kD0GuBEM7vrTTUjd0KKlQ6nWfIOUP5hzV0jlIZz8HvC%2BO0s4rAb%2FY0cd5%2F%2FpHCOyoAc9MvDfAfFKRbA6n7snzhSovBM6Y%2BLzM0fD6TGlRfrQ2J5XNSA9AN%2FF2sZ4Mh7Kbyz5Ygw%2FL9nOWKnlN6YwPoueoAGuCTpZzmMmCmtbSTQwSBJqP5Fh072RijgZSwdsnO7mY1FmtUW%2BVTiIUmEt8eYuoeYdDF6HB%2BcN7OE6OS%2B6MefVnrxZmFx5n5y368jzfPu%2FvZA0tCgb4UodopLIArFhf9pC%2FRZ2M317WRPWPDWkRz4sz%2BGy10s7HljtLoeYiplfls%2FaSfcDUjr2nvqnQSGJbosnMjitE0MSydwDqcKrZ1yxKJSx4FqMAwc5zViVqYcuPXUdLh5nJ9qF9JSt0ILJAe6lSCbN2BJf6yMYYrtUWyArWA0IH1oMPG%2FgL0GOqUB33kbmuEOXma28P7gxGsIHIOZtUXTfK0gqyWacZoxeysi%2FHswKpgnuqntNPjQFLi4UnKY5%2FLKWNTUQCVWb96o7hCgLyZnqR12lfH3npKWvDqtlRHp%2FeyKRxw1QzK3maxMQgPEIkgD1Z793bPsdiMjC7IFHn3wZZ%2BkG8rSl7Sv7Fp0CQuDcWDJf2Xpw7cT5H6PyakSIVlqo5l4UhSDjdcYajAxOmK9&X-Amz-Signature=a72432b9e5333f216465905f6d70f22435b2ff35fbf25dc088b3d18c192d5aef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM5RC37B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDJJXJ%2B0ULwzSO6ULd637zluX5ZmJGLIAGskM2alMdDsAiAHqhb2gfGJ9CraQxWO97%2FDUABdjcA9OCxpPeGUCRAewyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3nj48JUQLbWeyp03KtwD8o11eX9PD4yqiIFaEQFzgEjlTjpmnfPpQrL%2Bah9VhwZ1A4Q%2FbffTGzVPl9f3yqphHCVVdsHZYIe3svP0YkjiMQFkE%2FuVMHF7PqAm9dIwlr%2Fh%2BihBuXt07lDKGn2wWJExB5nYSj4QevVeAtUIJXcQdhHYGW%2Fltg4pUhulwGGH6wp3%2FP9Uo4Qdv2At3biGi9vQr4ZEbozJRJNHWPyFdXmmYGG8eRF%2FCGxt0khIu9%2B6mPqVYOOXu13RIB7SFQ3EmXeKet8TmWKRF8Oqb0xlzn9VF4OgFsTXfWcGlB2vX9qRyuBVZcq7%2BD%2BIZgZDK3hL69%2BeHl3tKN75I6DaS5ZtWeh9mSe7XThe3Q1GD%2FzXBtoOWHqxK1sUINIioYwRRbtKXa6b3o3tfAnavR2ptljKQzvDztkDG1SZB8OizbtUnIvn0D9w7yb73tYPLV621JOdoqS4M0tIH3pGU5KB63rqDo95KGHqTh5VYTYPPZNlmRH3SP47dzGix1Bi1MPWO57Y5SM%2FTRLhKqLPBwbGlkaf0mQ4RLgtn3S2A1m9P2KexhoCfSn%2BiVqWSoXh4GEdTCvBXCdBYsw7TkVzPEsxpevEFM7j%2FNGtWlmyX3TRA2gMZXaPWuAc0AD632BGrWQTmLUwvcCAvQY6pgEJR3kmL5F%2BvNUcsg5mmqtPWY9yYTO%2FpcGsV65qxjlv8XJ5RQLVa0%2FTfURIFqmUNvVfACVUa8oK0IRSkFJZL6%2FFw7CnIZIlOYcwm7t0iFIcG%2FWX%2FY%2BV7LcwbAWuJJuAByUY3lkaQhETkp9lrrOH72Payaf1mkoMECevcDB%2Fu%2Fo46wYp2wHb49Q9T780Uv4qIRL2PZnDNwYNgpXbTCGMnP7RYVxNMgrE&X-Amz-Signature=4652ebe8a0b8ccb66fbf70e20ba9f338288c0fded090c0226affc4d957237b85&X-Amz-SignedHeaders=host&x-id=GetObject)
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