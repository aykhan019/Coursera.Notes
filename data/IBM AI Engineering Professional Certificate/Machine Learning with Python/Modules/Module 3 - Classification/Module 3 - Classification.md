

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635FAH4RV%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0mSlGqyAeBnP2oJKGpA0QUqPlWsxPLUNTz1c3FIFLQIhAO6ZHGx0savhDXz7KSELpzQ5JrEHXph56sEX4mJLVKZlKv8DCCAQABoMNjM3NDIzMTgzODA1IgyS3yJyKFhftpULNQQq3AMYKHbBlQpGJndwvSqCpaksLO8p9Evzqu2lf%2B4oDIOy5Sb%2BOKCj8WK6i4kq2%2FGhWtFD7KqXp%2BTkTM0SF0pyjMQXo4LlMQDrMqFpynuXbjp2wAlLqwTAMHM7Bw8oycn%2BycxCPz7D1CdxuHsQZgyVQYj2ODae%2FMPh6JmALwvQhJgptKmHDNVrAWQSv%2FV6r35PIbD13rsVyJI%2Bfg2XiKt%2FOyOYE0pFyKovckdW3TkpgU02uAfE%2BhNWe4klxkJ50OJbriyiMsEY1pvGLEmKkyjzOm0Wj%2BF3835W0%2B9%2F%2FuhpKLP2ZGKQHg9ccgSG%2F%2Fl5MHlV5xQy4NqptbLMyPrmUO7ipLa%2FbjeJRr8WoQUkK8BWzr2rtaTZSOlsNvGZBlyZVu1KwxLd09LxQ0KCIM4SzSk9QGMsuneMn%2FkPltqC3TxtNHRetU5vBsQqCCra5RqYVWLzyfJL9WtgCzhs%2FGEaBsaMelVVTdmFHAqnUZEfYBewcPkg6o%2FHgPsS4t2g8iWBDACtaHxSbS%2FJzd3PzIrcVwvMaGc6k4nnSzU4C4izga81zkmIjX16tlfVzgv81JAa6YE8gHh9hX7cIEoSNzR1rWLE6SJ8dyjk76QqbiBE0EhBulGVmm5Kqvu1SL3GFY0teDDT%2F9e%2BBjqkAeQWgaB8ubKujs0KSjsuusfJn1gClRmwNfS5GHzrcoOXpUtEZtjUccmf%2BvdNbfcb7KT0CLHmCtq8JqnOUCUU7Mxyj1roq5tUW0gN8Jx77xHOEwK%2Bcpj%2FFI7v4HMGO8%2BAJ8fBoDR1uGWJHAncmQviiyrpMa9y6Lx03K1UN3gnXQjXXWlnTK%2Bbt7EUfgQdBvSH9aohGsoN%2BXz7HD9%2FXFvXCBmhPyc7&X-Amz-Signature=8519360b401342c7c0495a60d001d5c0ffd3a90875bafbaf9c0ed7379bd19b4a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635FAH4RV%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0mSlGqyAeBnP2oJKGpA0QUqPlWsxPLUNTz1c3FIFLQIhAO6ZHGx0savhDXz7KSELpzQ5JrEHXph56sEX4mJLVKZlKv8DCCAQABoMNjM3NDIzMTgzODA1IgyS3yJyKFhftpULNQQq3AMYKHbBlQpGJndwvSqCpaksLO8p9Evzqu2lf%2B4oDIOy5Sb%2BOKCj8WK6i4kq2%2FGhWtFD7KqXp%2BTkTM0SF0pyjMQXo4LlMQDrMqFpynuXbjp2wAlLqwTAMHM7Bw8oycn%2BycxCPz7D1CdxuHsQZgyVQYj2ODae%2FMPh6JmALwvQhJgptKmHDNVrAWQSv%2FV6r35PIbD13rsVyJI%2Bfg2XiKt%2FOyOYE0pFyKovckdW3TkpgU02uAfE%2BhNWe4klxkJ50OJbriyiMsEY1pvGLEmKkyjzOm0Wj%2BF3835W0%2B9%2F%2FuhpKLP2ZGKQHg9ccgSG%2F%2Fl5MHlV5xQy4NqptbLMyPrmUO7ipLa%2FbjeJRr8WoQUkK8BWzr2rtaTZSOlsNvGZBlyZVu1KwxLd09LxQ0KCIM4SzSk9QGMsuneMn%2FkPltqC3TxtNHRetU5vBsQqCCra5RqYVWLzyfJL9WtgCzhs%2FGEaBsaMelVVTdmFHAqnUZEfYBewcPkg6o%2FHgPsS4t2g8iWBDACtaHxSbS%2FJzd3PzIrcVwvMaGc6k4nnSzU4C4izga81zkmIjX16tlfVzgv81JAa6YE8gHh9hX7cIEoSNzR1rWLE6SJ8dyjk76QqbiBE0EhBulGVmm5Kqvu1SL3GFY0teDDT%2F9e%2BBjqkAeQWgaB8ubKujs0KSjsuusfJn1gClRmwNfS5GHzrcoOXpUtEZtjUccmf%2BvdNbfcb7KT0CLHmCtq8JqnOUCUU7Mxyj1roq5tUW0gN8Jx77xHOEwK%2Bcpj%2FFI7v4HMGO8%2BAJ8fBoDR1uGWJHAncmQviiyrpMa9y6Lx03K1UN3gnXQjXXWlnTK%2Bbt7EUfgQdBvSH9aohGsoN%2BXz7HD9%2FXFvXCBmhPyc7&X-Amz-Signature=ea08f73d661a4532563fc820405ac8164db66ef0f7968baa055f450f9abc3a57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635FAH4RV%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0mSlGqyAeBnP2oJKGpA0QUqPlWsxPLUNTz1c3FIFLQIhAO6ZHGx0savhDXz7KSELpzQ5JrEHXph56sEX4mJLVKZlKv8DCCAQABoMNjM3NDIzMTgzODA1IgyS3yJyKFhftpULNQQq3AMYKHbBlQpGJndwvSqCpaksLO8p9Evzqu2lf%2B4oDIOy5Sb%2BOKCj8WK6i4kq2%2FGhWtFD7KqXp%2BTkTM0SF0pyjMQXo4LlMQDrMqFpynuXbjp2wAlLqwTAMHM7Bw8oycn%2BycxCPz7D1CdxuHsQZgyVQYj2ODae%2FMPh6JmALwvQhJgptKmHDNVrAWQSv%2FV6r35PIbD13rsVyJI%2Bfg2XiKt%2FOyOYE0pFyKovckdW3TkpgU02uAfE%2BhNWe4klxkJ50OJbriyiMsEY1pvGLEmKkyjzOm0Wj%2BF3835W0%2B9%2F%2FuhpKLP2ZGKQHg9ccgSG%2F%2Fl5MHlV5xQy4NqptbLMyPrmUO7ipLa%2FbjeJRr8WoQUkK8BWzr2rtaTZSOlsNvGZBlyZVu1KwxLd09LxQ0KCIM4SzSk9QGMsuneMn%2FkPltqC3TxtNHRetU5vBsQqCCra5RqYVWLzyfJL9WtgCzhs%2FGEaBsaMelVVTdmFHAqnUZEfYBewcPkg6o%2FHgPsS4t2g8iWBDACtaHxSbS%2FJzd3PzIrcVwvMaGc6k4nnSzU4C4izga81zkmIjX16tlfVzgv81JAa6YE8gHh9hX7cIEoSNzR1rWLE6SJ8dyjk76QqbiBE0EhBulGVmm5Kqvu1SL3GFY0teDDT%2F9e%2BBjqkAeQWgaB8ubKujs0KSjsuusfJn1gClRmwNfS5GHzrcoOXpUtEZtjUccmf%2BvdNbfcb7KT0CLHmCtq8JqnOUCUU7Mxyj1roq5tUW0gN8Jx77xHOEwK%2Bcpj%2FFI7v4HMGO8%2BAJ8fBoDR1uGWJHAncmQviiyrpMa9y6Lx03K1UN3gnXQjXXWlnTK%2Bbt7EUfgQdBvSH9aohGsoN%2BXz7HD9%2FXFvXCBmhPyc7&X-Amz-Signature=04ad7e5f0f76dff2b46750e24a62157e95d5d6744b560b0b0f0caa23ede5ee7b&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YVAAIDA%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDOFvTMyguT%2BdX4ukUY7DPddtLYUkc9vAMZ4Ycghy5LDAiAULiDwmlm9hO1y0VOAaY4w3da27yhboKXyiIZbCu%2BYMSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMVGKnt0OfxIFpVw%2BYKtwD3XdFCUClzLfxmxvABCDB9G5JWfMlm0a5137y9iYGq2AGSZRsUq0qNmV5JfRq7pjtbzFYSceD73CpY%2F93lrlDTVXdmP6JaoyuXaT1gSzFbkaVhaffmtZuM592v%2B317oZRD%2FcVRCAHOyjnQB1jLaOy8r9FNVm9VQJipMpO%2F5IWTEqVopG3bOlDx75HTFk0u36jvLp5jG4U0MpsX2FqWNPe%2B0J%2B5s70k8XgbcscadS5td9ifpZtaUe0NFOJa58FEQHvd5Bucmxeu2FNbKQmKiK1%2FS5BMlfDiG1zk%2BczzuizpakJhF2ixPvHkvK4jbDJbKu3sEdrc5t7Q1QybemKxtTzRM6s8sfSP0zd4w2eKU0OT%2BXl1ZMXcJwLwZj0rlKUyl6nBfWaJtxpIz%2FnUEYhlOJ%2F73BOy4X7LiwV9Prf0yL04O4%2FXlLlq9Lx7WyRpPZVh4zGjHN%2F27daZxu3Xdj5oJVOyD02%2B6pDQEJYIm0FLBT6cCig7bNELJy4c2khWdFzrIqTO%2F5sgl%2F%2BAYzQnwzyAPB0CPFOy56Ti94BodK1pS5kq17NstGCJ7RiCO0wE4M1z4%2Fj2TbocXScFoxbLqkYRGmIwi3SRWnQSlSnEeg3y5NLO5zw%2FZCUq%2FHK%2FTTox2ww2%2F%2FXvgY6pgGqwDuYeNoN7fBzY1EgPtP3HDdlQV9dkTXCTE1ybiVkvbK3o%2FeSa%2B3yl3nghThSqkwqoS9pP6g1vstQz1O0sAThYoW3%2BW%2FG%2BfqXYVIMW4gweTYGA%2Bs68FZ5MY%2F6o9zBAXUd1uO0sbT7a%2FlnvQ5jYIzRJ%2Fcv2%2FZK4s0MTyc2pXm%2BFfd4LtlnKM2gLepXp7GjTNVKNDBrakCmIfCYpZKy4K7YKY1N9%2BUr&X-Amz-Signature=5a43f5f8b574d0e34b60154ae6d8a5530d2dad6b4a3ceb8a3b669ad4f02ad319&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YVAAIDA%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDOFvTMyguT%2BdX4ukUY7DPddtLYUkc9vAMZ4Ycghy5LDAiAULiDwmlm9hO1y0VOAaY4w3da27yhboKXyiIZbCu%2BYMSr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMVGKnt0OfxIFpVw%2BYKtwD3XdFCUClzLfxmxvABCDB9G5JWfMlm0a5137y9iYGq2AGSZRsUq0qNmV5JfRq7pjtbzFYSceD73CpY%2F93lrlDTVXdmP6JaoyuXaT1gSzFbkaVhaffmtZuM592v%2B317oZRD%2FcVRCAHOyjnQB1jLaOy8r9FNVm9VQJipMpO%2F5IWTEqVopG3bOlDx75HTFk0u36jvLp5jG4U0MpsX2FqWNPe%2B0J%2B5s70k8XgbcscadS5td9ifpZtaUe0NFOJa58FEQHvd5Bucmxeu2FNbKQmKiK1%2FS5BMlfDiG1zk%2BczzuizpakJhF2ixPvHkvK4jbDJbKu3sEdrc5t7Q1QybemKxtTzRM6s8sfSP0zd4w2eKU0OT%2BXl1ZMXcJwLwZj0rlKUyl6nBfWaJtxpIz%2FnUEYhlOJ%2F73BOy4X7LiwV9Prf0yL04O4%2FXlLlq9Lx7WyRpPZVh4zGjHN%2F27daZxu3Xdj5oJVOyD02%2B6pDQEJYIm0FLBT6cCig7bNELJy4c2khWdFzrIqTO%2F5sgl%2F%2BAYzQnwzyAPB0CPFOy56Ti94BodK1pS5kq17NstGCJ7RiCO0wE4M1z4%2Fj2TbocXScFoxbLqkYRGmIwi3SRWnQSlSnEeg3y5NLO5zw%2FZCUq%2FHK%2FTTox2ww2%2F%2FXvgY6pgGqwDuYeNoN7fBzY1EgPtP3HDdlQV9dkTXCTE1ybiVkvbK3o%2FeSa%2B3yl3nghThSqkwqoS9pP6g1vstQz1O0sAThYoW3%2BW%2FG%2BfqXYVIMW4gweTYGA%2Bs68FZ5MY%2F6o9zBAXUd1uO0sbT7a%2FlnvQ5jYIzRJ%2Fcv2%2FZK4s0MTyc2pXm%2BFfd4LtlnKM2gLepXp7GjTNVKNDBrakCmIfCYpZKy4K7YKY1N9%2BUr&X-Amz-Signature=eb1fbb212483472c50e3c3c70e71c7619db1e255b9e8f2730fa23c8ce5837729&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635FAH4RV%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx0mSlGqyAeBnP2oJKGpA0QUqPlWsxPLUNTz1c3FIFLQIhAO6ZHGx0savhDXz7KSELpzQ5JrEHXph56sEX4mJLVKZlKv8DCCAQABoMNjM3NDIzMTgzODA1IgyS3yJyKFhftpULNQQq3AMYKHbBlQpGJndwvSqCpaksLO8p9Evzqu2lf%2B4oDIOy5Sb%2BOKCj8WK6i4kq2%2FGhWtFD7KqXp%2BTkTM0SF0pyjMQXo4LlMQDrMqFpynuXbjp2wAlLqwTAMHM7Bw8oycn%2BycxCPz7D1CdxuHsQZgyVQYj2ODae%2FMPh6JmALwvQhJgptKmHDNVrAWQSv%2FV6r35PIbD13rsVyJI%2Bfg2XiKt%2FOyOYE0pFyKovckdW3TkpgU02uAfE%2BhNWe4klxkJ50OJbriyiMsEY1pvGLEmKkyjzOm0Wj%2BF3835W0%2B9%2F%2FuhpKLP2ZGKQHg9ccgSG%2F%2Fl5MHlV5xQy4NqptbLMyPrmUO7ipLa%2FbjeJRr8WoQUkK8BWzr2rtaTZSOlsNvGZBlyZVu1KwxLd09LxQ0KCIM4SzSk9QGMsuneMn%2FkPltqC3TxtNHRetU5vBsQqCCra5RqYVWLzyfJL9WtgCzhs%2FGEaBsaMelVVTdmFHAqnUZEfYBewcPkg6o%2FHgPsS4t2g8iWBDACtaHxSbS%2FJzd3PzIrcVwvMaGc6k4nnSzU4C4izga81zkmIjX16tlfVzgv81JAa6YE8gHh9hX7cIEoSNzR1rWLE6SJ8dyjk76QqbiBE0EhBulGVmm5Kqvu1SL3GFY0teDDT%2F9e%2BBjqkAeQWgaB8ubKujs0KSjsuusfJn1gClRmwNfS5GHzrcoOXpUtEZtjUccmf%2BvdNbfcb7KT0CLHmCtq8JqnOUCUU7Mxyj1roq5tUW0gN8Jx77xHOEwK%2Bcpj%2FFI7v4HMGO8%2BAJ8fBoDR1uGWJHAncmQviiyrpMa9y6Lx03K1UN3gnXQjXXWlnTK%2Bbt7EUfgQdBvSH9aohGsoN%2BXz7HD9%2FXFvXCBmhPyc7&X-Amz-Signature=43e3165de579ea57d7436725c6124056b563cd6b7f8d247f00530c55fa990042&X-Amz-SignedHeaders=host&x-id=GetObject)
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