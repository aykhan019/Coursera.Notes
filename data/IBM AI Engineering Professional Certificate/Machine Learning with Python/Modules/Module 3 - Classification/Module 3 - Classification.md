

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNHYBQBS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC%2FV0UVzZYPyZDahmV6Q%2FT2fFaccCzozLRO%2FQGKxFZAPQIhAPFSIbO%2FqxRKSjAAVCqh5G%2BwI6aiodChBEg18EcpWsQzKv8DCFUQABoMNjM3NDIzMTgzODA1IgzqcnHVL6hX%2FAXFxfgq3APL1d5ChVWW%2Fp6x%2BDewWg42Am4Ks4DHXasqVKFM4PibD9x9zRv%2FwpYuggQGGmbJpQdml8Y7jWCXYyl8OwhMr9ev2tuC9OGWtVukJYhuC2I7KHxWs4MK0%2B%2F%2BZFfuimrRCaN1sbmUTI2rD%2FvOoRvzTq3kqMLqkGmfxKtRe%2Bwr8KjeD0qkUZwgLUSDJB2SOGmTSbuDF4tk6de5JYYRwptH8619L9GQ9CpBwKR1YPR8cXIBvAJlSGnX7XaKOhw2CuHYcrw%2BnOWCNrQwUYoCw09z6gO%2FSVjo7ZbPQhTTsguu89KhckgGktRAFqXtSiOhJqHuZ9Lz0LkRPsSWbC9ngHKW0oRe4A4DguIW2c07vaNlwDf5DI4qXFW%2BuTAS8Vu78b65WSAZTK4HYSkamu%2BNE7eJE%2FqqkJQajZy5m7lh3zxbDpVS%2BN9n6X4ka7Ecl1SFgPqjrvNmrV9gkat6gPs3D8NtKmFdNNi46fen4mI3PLIIeuLcM0nFykv4hsFyH0Y3UFPnTN9Bu04v6YslziDfBiiH8NH7fTfDPcGVt0mJN%2FUrkm4jWHRGC5GtXwE6JeDslJKBcrIUAuZkeCIgp4nvVa%2Ba7mVn0Dhkw3M3KSZwgPaeE5gtgF9qs81JSMlyMtpu4TCA4JC9BjqkAcv1HNiZpHOxPhxG67t62vE9xB37mWx6Hw%2FDKov58q3RcRnB5jP%2BvZzbdEJwnkHlHBlj71doRGk1sISmscsCj5Ud0AdaQcK88J9iT%2BZlszb5XdyC60moxXh%2B6ZgGtfcFmeBVLYXs3671aIyvrxVvWgay%2FpgUHUl8HKA6th7Ty%2BxYP%2Bp8jhBThE338C8jjZMxsaHbDCdSvArZ0RlsFItKf7dWTFZK&X-Amz-Signature=9570713ff576b0033e6f07d5e9ea58fffc05e214f109cd3c809eb2c3a67f86a8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNHYBQBS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC%2FV0UVzZYPyZDahmV6Q%2FT2fFaccCzozLRO%2FQGKxFZAPQIhAPFSIbO%2FqxRKSjAAVCqh5G%2BwI6aiodChBEg18EcpWsQzKv8DCFUQABoMNjM3NDIzMTgzODA1IgzqcnHVL6hX%2FAXFxfgq3APL1d5ChVWW%2Fp6x%2BDewWg42Am4Ks4DHXasqVKFM4PibD9x9zRv%2FwpYuggQGGmbJpQdml8Y7jWCXYyl8OwhMr9ev2tuC9OGWtVukJYhuC2I7KHxWs4MK0%2B%2F%2BZFfuimrRCaN1sbmUTI2rD%2FvOoRvzTq3kqMLqkGmfxKtRe%2Bwr8KjeD0qkUZwgLUSDJB2SOGmTSbuDF4tk6de5JYYRwptH8619L9GQ9CpBwKR1YPR8cXIBvAJlSGnX7XaKOhw2CuHYcrw%2BnOWCNrQwUYoCw09z6gO%2FSVjo7ZbPQhTTsguu89KhckgGktRAFqXtSiOhJqHuZ9Lz0LkRPsSWbC9ngHKW0oRe4A4DguIW2c07vaNlwDf5DI4qXFW%2BuTAS8Vu78b65WSAZTK4HYSkamu%2BNE7eJE%2FqqkJQajZy5m7lh3zxbDpVS%2BN9n6X4ka7Ecl1SFgPqjrvNmrV9gkat6gPs3D8NtKmFdNNi46fen4mI3PLIIeuLcM0nFykv4hsFyH0Y3UFPnTN9Bu04v6YslziDfBiiH8NH7fTfDPcGVt0mJN%2FUrkm4jWHRGC5GtXwE6JeDslJKBcrIUAuZkeCIgp4nvVa%2Ba7mVn0Dhkw3M3KSZwgPaeE5gtgF9qs81JSMlyMtpu4TCA4JC9BjqkAcv1HNiZpHOxPhxG67t62vE9xB37mWx6Hw%2FDKov58q3RcRnB5jP%2BvZzbdEJwnkHlHBlj71doRGk1sISmscsCj5Ud0AdaQcK88J9iT%2BZlszb5XdyC60moxXh%2B6ZgGtfcFmeBVLYXs3671aIyvrxVvWgay%2FpgUHUl8HKA6th7Ty%2BxYP%2Bp8jhBThE338C8jjZMxsaHbDCdSvArZ0RlsFItKf7dWTFZK&X-Amz-Signature=1d28d28d748efadd73aa574609511cbc12ef6be84e5e7351c40c5b580206c22d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNHYBQBS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC%2FV0UVzZYPyZDahmV6Q%2FT2fFaccCzozLRO%2FQGKxFZAPQIhAPFSIbO%2FqxRKSjAAVCqh5G%2BwI6aiodChBEg18EcpWsQzKv8DCFUQABoMNjM3NDIzMTgzODA1IgzqcnHVL6hX%2FAXFxfgq3APL1d5ChVWW%2Fp6x%2BDewWg42Am4Ks4DHXasqVKFM4PibD9x9zRv%2FwpYuggQGGmbJpQdml8Y7jWCXYyl8OwhMr9ev2tuC9OGWtVukJYhuC2I7KHxWs4MK0%2B%2F%2BZFfuimrRCaN1sbmUTI2rD%2FvOoRvzTq3kqMLqkGmfxKtRe%2Bwr8KjeD0qkUZwgLUSDJB2SOGmTSbuDF4tk6de5JYYRwptH8619L9GQ9CpBwKR1YPR8cXIBvAJlSGnX7XaKOhw2CuHYcrw%2BnOWCNrQwUYoCw09z6gO%2FSVjo7ZbPQhTTsguu89KhckgGktRAFqXtSiOhJqHuZ9Lz0LkRPsSWbC9ngHKW0oRe4A4DguIW2c07vaNlwDf5DI4qXFW%2BuTAS8Vu78b65WSAZTK4HYSkamu%2BNE7eJE%2FqqkJQajZy5m7lh3zxbDpVS%2BN9n6X4ka7Ecl1SFgPqjrvNmrV9gkat6gPs3D8NtKmFdNNi46fen4mI3PLIIeuLcM0nFykv4hsFyH0Y3UFPnTN9Bu04v6YslziDfBiiH8NH7fTfDPcGVt0mJN%2FUrkm4jWHRGC5GtXwE6JeDslJKBcrIUAuZkeCIgp4nvVa%2Ba7mVn0Dhkw3M3KSZwgPaeE5gtgF9qs81JSMlyMtpu4TCA4JC9BjqkAcv1HNiZpHOxPhxG67t62vE9xB37mWx6Hw%2FDKov58q3RcRnB5jP%2BvZzbdEJwnkHlHBlj71doRGk1sISmscsCj5Ud0AdaQcK88J9iT%2BZlszb5XdyC60moxXh%2B6ZgGtfcFmeBVLYXs3671aIyvrxVvWgay%2FpgUHUl8HKA6th7Ty%2BxYP%2Bp8jhBThE338C8jjZMxsaHbDCdSvArZ0RlsFItKf7dWTFZK&X-Amz-Signature=e0260b9106188ac5bd830ee824d48713a631fe0baaeff8310cab1d808e1c1e29&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDSRSPXU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCICSw0vFrw9HlhHA2Hqk8MdTwJqJDH0LD2HhI46q%2BWrOfAiA5INNc%2F9%2B03bK7xeGycp58VurWuwVemGCVeo7sN%2FczQir%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIM1CO1zkJQMOx1aMd7KtwDgCWJgOKuGGgRUheHYxfklkdtyAZsLZkl3LM83w7%2Fqj0kmPkCKAu8orbSwJOTJ%2Bm18m%2Fdr8P6Xa%2B7H7xiRFzNTHMZi62JZUmlsT%2FYxh%2Bbq1l6xMdeDUInmjXk945SmKU9jb8cKu4RxGRZd963S6Z%2BxVxNBRyKfDhWUd%2FtbAwiDCOmzj6sXF2euaAMjK612g%2FGQpFe1MSZbcf9o7a%2Fw6sncVgK9IqSB3re01cXadJlNnkSRj%2F%2FJKqiutF%2F4WPXhaGZ%2FNKcL1QbwgzcgxOF4p3JTev3t1RrrtPVqSUTguFWwjTnFKfJktn3pcQUcdorrPqaPp35XqiWMR24QO3UlAPo%2BIPVY617GW3QnuNXIPhxRAxGJJd4tR%2F9pfUYHFjyKthMALrx1WfbW5eqK2k%2FUoeg7zLs4kLk80jFneJrIfNNEIXmfWEIdvfGdcLKUdy7%2BgX3zwFq8TdV4cZX4XXWoBBydg025Y7I93WHTXqVU59CLMv8k9MR%2FXYSWz7Sv9eOFuOLk3q1H%2B1DshBOiP2hz3zbtVlgHsKCzttE2jBl5RB%2FwmWw0lMMpI1SRsLq7jTw6YKso%2FGkR28Wo2%2BxuszzdmhCfNK9%2Fy03RJd%2FvtN%2F0jdPDrxL%2BjxBcy9xu2HPcA8wy9%2BQvQY6pgHNhtMQ4IK%2BAvu6iPkCMxuc7Ut7hSK38xqK%2FYZHdYKq8UzZSxaiU1XkoplHC29thyLcm0cgVO6yKXRQV9IqsmkZcTYHP6xizIIzrnu1ZJhVuVUOOromoEwWf1alMjPQuc7zZUATSkQ7Xaft77DZffyo3Y3Y4b%2F5jHim3Ak0wgr13xtfPgMaC5UzL9czPDjDhS3wTC7L8N2cJoEpiyo8xxMxSWGls17L&X-Amz-Signature=6fff5e1307b6727ff7edf85a0ba2f5362c4b040c0b38efe3216f210c41f2ba01&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDSRSPXU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCICSw0vFrw9HlhHA2Hqk8MdTwJqJDH0LD2HhI46q%2BWrOfAiA5INNc%2F9%2B03bK7xeGycp58VurWuwVemGCVeo7sN%2FczQir%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIM1CO1zkJQMOx1aMd7KtwDgCWJgOKuGGgRUheHYxfklkdtyAZsLZkl3LM83w7%2Fqj0kmPkCKAu8orbSwJOTJ%2Bm18m%2Fdr8P6Xa%2B7H7xiRFzNTHMZi62JZUmlsT%2FYxh%2Bbq1l6xMdeDUInmjXk945SmKU9jb8cKu4RxGRZd963S6Z%2BxVxNBRyKfDhWUd%2FtbAwiDCOmzj6sXF2euaAMjK612g%2FGQpFe1MSZbcf9o7a%2Fw6sncVgK9IqSB3re01cXadJlNnkSRj%2F%2FJKqiutF%2F4WPXhaGZ%2FNKcL1QbwgzcgxOF4p3JTev3t1RrrtPVqSUTguFWwjTnFKfJktn3pcQUcdorrPqaPp35XqiWMR24QO3UlAPo%2BIPVY617GW3QnuNXIPhxRAxGJJd4tR%2F9pfUYHFjyKthMALrx1WfbW5eqK2k%2FUoeg7zLs4kLk80jFneJrIfNNEIXmfWEIdvfGdcLKUdy7%2BgX3zwFq8TdV4cZX4XXWoBBydg025Y7I93WHTXqVU59CLMv8k9MR%2FXYSWz7Sv9eOFuOLk3q1H%2B1DshBOiP2hz3zbtVlgHsKCzttE2jBl5RB%2FwmWw0lMMpI1SRsLq7jTw6YKso%2FGkR28Wo2%2BxuszzdmhCfNK9%2Fy03RJd%2FvtN%2F0jdPDrxL%2BjxBcy9xu2HPcA8wy9%2BQvQY6pgHNhtMQ4IK%2BAvu6iPkCMxuc7Ut7hSK38xqK%2FYZHdYKq8UzZSxaiU1XkoplHC29thyLcm0cgVO6yKXRQV9IqsmkZcTYHP6xizIIzrnu1ZJhVuVUOOromoEwWf1alMjPQuc7zZUATSkQ7Xaft77DZffyo3Y3Y4b%2F5jHim3Ak0wgr13xtfPgMaC5UzL9czPDjDhS3wTC7L8N2cJoEpiyo8xxMxSWGls17L&X-Amz-Signature=1f6e33541ef60072acf788f9e67c648db117d69ce99688ae98b0d950d8061966&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNHYBQBS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQC%2FV0UVzZYPyZDahmV6Q%2FT2fFaccCzozLRO%2FQGKxFZAPQIhAPFSIbO%2FqxRKSjAAVCqh5G%2BwI6aiodChBEg18EcpWsQzKv8DCFUQABoMNjM3NDIzMTgzODA1IgzqcnHVL6hX%2FAXFxfgq3APL1d5ChVWW%2Fp6x%2BDewWg42Am4Ks4DHXasqVKFM4PibD9x9zRv%2FwpYuggQGGmbJpQdml8Y7jWCXYyl8OwhMr9ev2tuC9OGWtVukJYhuC2I7KHxWs4MK0%2B%2F%2BZFfuimrRCaN1sbmUTI2rD%2FvOoRvzTq3kqMLqkGmfxKtRe%2Bwr8KjeD0qkUZwgLUSDJB2SOGmTSbuDF4tk6de5JYYRwptH8619L9GQ9CpBwKR1YPR8cXIBvAJlSGnX7XaKOhw2CuHYcrw%2BnOWCNrQwUYoCw09z6gO%2FSVjo7ZbPQhTTsguu89KhckgGktRAFqXtSiOhJqHuZ9Lz0LkRPsSWbC9ngHKW0oRe4A4DguIW2c07vaNlwDf5DI4qXFW%2BuTAS8Vu78b65WSAZTK4HYSkamu%2BNE7eJE%2FqqkJQajZy5m7lh3zxbDpVS%2BN9n6X4ka7Ecl1SFgPqjrvNmrV9gkat6gPs3D8NtKmFdNNi46fen4mI3PLIIeuLcM0nFykv4hsFyH0Y3UFPnTN9Bu04v6YslziDfBiiH8NH7fTfDPcGVt0mJN%2FUrkm4jWHRGC5GtXwE6JeDslJKBcrIUAuZkeCIgp4nvVa%2Ba7mVn0Dhkw3M3KSZwgPaeE5gtgF9qs81JSMlyMtpu4TCA4JC9BjqkAcv1HNiZpHOxPhxG67t62vE9xB37mWx6Hw%2FDKov58q3RcRnB5jP%2BvZzbdEJwnkHlHBlj71doRGk1sISmscsCj5Ud0AdaQcK88J9iT%2BZlszb5XdyC60moxXh%2B6ZgGtfcFmeBVLYXs3671aIyvrxVvWgay%2FpgUHUl8HKA6th7Ty%2BxYP%2Bp8jhBThE338C8jjZMxsaHbDCdSvArZ0RlsFItKf7dWTFZK&X-Amz-Signature=19e378894ac6b34b2723573c9b856d29a15c5b8c4f8b9ad293208ede5304332f&X-Amz-SignedHeaders=host&x-id=GetObject)
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