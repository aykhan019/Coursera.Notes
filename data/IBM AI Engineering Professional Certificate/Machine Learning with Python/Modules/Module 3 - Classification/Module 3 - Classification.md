

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TLO7FRT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIGD%2Bw91aM6xG3d6GSyOkAHXnUUhStPdqY6au1C7v0jPWAiBAIw0lTJ6xjdPB7rf27xjGFlvohjPzvuEAaEhEQ%2FjjQir%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMf4552C6qJ42%2Fpox5KtwDgTRea0uZIVtbfdDNsK95qsqBQ83NKCE2ufh%2BwVfCUZ1pjId%2BJ9VXch4bUAgFZEjttZGvFtHqrMhguz7nm7j%2Fiil4sUDk4kIdtlJ%2F%2F12yHQHztpx%2BU7HvuEOQENsPL4SUkC21okrLbq27QesP9NCttCFgByHnJmsvfCcjzLLLS5D%2BfSIEjPQvoY9skfqeSEBPgcWe0DXSCT%2B%2Bm2XiuwmJGcQARDo9Gj8JBtvi24TOtEanS0XBpCOZ4qVC25VsocnbANyJ923z3exEb42ktpcJwb2l1lxJvzd8X%2B4FXcBEbl%2FZJ6xsgjDpmz5tiHUYy0erfevNPvlRcAe%2FPjWepNC00ConF%2F1EtwfIzIiZqwj2J3E%2FswVMZNVtHXCzm9ssu55TF2BHENlZaiw59w07vi68bhJD1lNZKKVztqXp9WUm6I0Inbhg3uol%2FU5%2BauHwqv8LwL4jdvvlxGY8GrP2MS%2FUylr2C3gqPYYmfiaT2a1nRPhCw80Os8OtnYkf%2FQLBr%2BtvYxEGBRKjhAtshk0%2FFMEARB0NRb8OzpdYcx%2FWJ8D%2FuRhep%2BTiKyeca0QlzDs%2B4dRIvYb1pG3ZxQoYcMAx58poGXIGnEkty3v2mQkNtn6NoZI%2B7t95zCprgfnl2UUwt66HvQY6pgEH8%2BzjS%2FVMsaNpXIrgVQY%2FoyrLNFN8KwPgdh34H0yKrjEdnvpT9oslwkwVPJDOMT61vXSmsr6EpcI4oFGunrwuUE5z31DsQA43VIxQ8b%2BoCgVZ%2FFjgcPXatnSaaMd1tUqyQit7hxk6qWaplWnVEWTjT8cX2g8zME0Gh2nnDv3ra2BjBcs%2B0gwirpC6DXIg5M1RE0IOehYn0UgieA4U%2FiziNe%2FWNanD&X-Amz-Signature=5c6e6539d14d656bd251b10a2e23d9424e4c122510fa812c21b846d4796039eb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TLO7FRT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIGD%2Bw91aM6xG3d6GSyOkAHXnUUhStPdqY6au1C7v0jPWAiBAIw0lTJ6xjdPB7rf27xjGFlvohjPzvuEAaEhEQ%2FjjQir%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMf4552C6qJ42%2Fpox5KtwDgTRea0uZIVtbfdDNsK95qsqBQ83NKCE2ufh%2BwVfCUZ1pjId%2BJ9VXch4bUAgFZEjttZGvFtHqrMhguz7nm7j%2Fiil4sUDk4kIdtlJ%2F%2F12yHQHztpx%2BU7HvuEOQENsPL4SUkC21okrLbq27QesP9NCttCFgByHnJmsvfCcjzLLLS5D%2BfSIEjPQvoY9skfqeSEBPgcWe0DXSCT%2B%2Bm2XiuwmJGcQARDo9Gj8JBtvi24TOtEanS0XBpCOZ4qVC25VsocnbANyJ923z3exEb42ktpcJwb2l1lxJvzd8X%2B4FXcBEbl%2FZJ6xsgjDpmz5tiHUYy0erfevNPvlRcAe%2FPjWepNC00ConF%2F1EtwfIzIiZqwj2J3E%2FswVMZNVtHXCzm9ssu55TF2BHENlZaiw59w07vi68bhJD1lNZKKVztqXp9WUm6I0Inbhg3uol%2FU5%2BauHwqv8LwL4jdvvlxGY8GrP2MS%2FUylr2C3gqPYYmfiaT2a1nRPhCw80Os8OtnYkf%2FQLBr%2BtvYxEGBRKjhAtshk0%2FFMEARB0NRb8OzpdYcx%2FWJ8D%2FuRhep%2BTiKyeca0QlzDs%2B4dRIvYb1pG3ZxQoYcMAx58poGXIGnEkty3v2mQkNtn6NoZI%2B7t95zCprgfnl2UUwt66HvQY6pgEH8%2BzjS%2FVMsaNpXIrgVQY%2FoyrLNFN8KwPgdh34H0yKrjEdnvpT9oslwkwVPJDOMT61vXSmsr6EpcI4oFGunrwuUE5z31DsQA43VIxQ8b%2BoCgVZ%2FFjgcPXatnSaaMd1tUqyQit7hxk6qWaplWnVEWTjT8cX2g8zME0Gh2nnDv3ra2BjBcs%2B0gwirpC6DXIg5M1RE0IOehYn0UgieA4U%2FiziNe%2FWNanD&X-Amz-Signature=14283d80c4992787be50bf7961b9995896adb30cf657b5310fa6fbb221966e0e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TLO7FRT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIGD%2Bw91aM6xG3d6GSyOkAHXnUUhStPdqY6au1C7v0jPWAiBAIw0lTJ6xjdPB7rf27xjGFlvohjPzvuEAaEhEQ%2FjjQir%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMf4552C6qJ42%2Fpox5KtwDgTRea0uZIVtbfdDNsK95qsqBQ83NKCE2ufh%2BwVfCUZ1pjId%2BJ9VXch4bUAgFZEjttZGvFtHqrMhguz7nm7j%2Fiil4sUDk4kIdtlJ%2F%2F12yHQHztpx%2BU7HvuEOQENsPL4SUkC21okrLbq27QesP9NCttCFgByHnJmsvfCcjzLLLS5D%2BfSIEjPQvoY9skfqeSEBPgcWe0DXSCT%2B%2Bm2XiuwmJGcQARDo9Gj8JBtvi24TOtEanS0XBpCOZ4qVC25VsocnbANyJ923z3exEb42ktpcJwb2l1lxJvzd8X%2B4FXcBEbl%2FZJ6xsgjDpmz5tiHUYy0erfevNPvlRcAe%2FPjWepNC00ConF%2F1EtwfIzIiZqwj2J3E%2FswVMZNVtHXCzm9ssu55TF2BHENlZaiw59w07vi68bhJD1lNZKKVztqXp9WUm6I0Inbhg3uol%2FU5%2BauHwqv8LwL4jdvvlxGY8GrP2MS%2FUylr2C3gqPYYmfiaT2a1nRPhCw80Os8OtnYkf%2FQLBr%2BtvYxEGBRKjhAtshk0%2FFMEARB0NRb8OzpdYcx%2FWJ8D%2FuRhep%2BTiKyeca0QlzDs%2B4dRIvYb1pG3ZxQoYcMAx58poGXIGnEkty3v2mQkNtn6NoZI%2B7t95zCprgfnl2UUwt66HvQY6pgEH8%2BzjS%2FVMsaNpXIrgVQY%2FoyrLNFN8KwPgdh34H0yKrjEdnvpT9oslwkwVPJDOMT61vXSmsr6EpcI4oFGunrwuUE5z31DsQA43VIxQ8b%2BoCgVZ%2FFjgcPXatnSaaMd1tUqyQit7hxk6qWaplWnVEWTjT8cX2g8zME0Gh2nnDv3ra2BjBcs%2B0gwirpC6DXIg5M1RE0IOehYn0UgieA4U%2FiziNe%2FWNanD&X-Amz-Signature=79affa28c62c1e951dcb9322ad92eac3d6caa57fab127d34eee018c4d67c5ca8&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624HOW7KF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCICg7%2BHzL83ZYmIpL9iKpJUMzAE5LLZF5dvUNSZskzI0LAiEA90sAUGy9SxRlB1ylMc9zO7DfuC8P%2ByK3jZW%2BwbVQ3p4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDGCCxADV9TId51HfRircA%2FAXBz1tX%2FJ97cPLD62MnE0KeuZ15ay17Nw2WCRi43qnFIGS%2Fxnsk7Wb5%2BwnbcyxMz9eZTgJ%2BXdGFIlvwOlRq9sxaDzH8tii%2F%2FkqXM3voTr7jFkopF3mOUXcE6Wy9bqr0NYLQEBomiBb1H2nbb1l1yC63pYkzNGcIpqH948dTFtFX7K7L4U92DrCP43vi0Kjf7MbZlXuwmDS1HXjJ9N6WAdkuQuVI%2BdhU9qec7Gwv2D9eew9x%2FbQ2PZB8GFSsOn2Pq4msSG2qnVP4ICIu3yw8T8vdOiKqfj3f4syE%2Fr5ZzAk9SeCO65cgTaWq1Y%2FzOrGjD1aqDwg5iCOIxxCUyik9Q3xI5A7ij1N1UzsxOJR9naMPdVWEbf4B1h9TobaT5uKerdcUlhcu83cc2dYed2LKcAlwdoZCaYWS8PbAhnOCZ3KBZek7GbuZnUKy6JCHP%2BaHoWJkzT%2FwaK87SqYh6Ghque954qEA1ZKXbNS8ik0OdEJA3i0q%2FvhpjWVm8EgqazvuA3eoa%2BmlqMvw34g2kfII10OYpgC%2FgANvq8%2BnV63gtpJs4EZzmYKf6iaV6vuO%2FbRFtgetpVE%2BE8q5mVk7ig3w2mGeTNp4Cab0u0T2CQJs%2FYUdXSq0JEWrzmhnK%2BAMNauh70GOqUBwyZB2rP48JHBTkJwFoG0HRP9qqr%2BwzKrH4p%2FJoNjc3vg%2FP0FCNsJ9S2XT1Dbvxrk%2B0fFQAARcjVIu61WVL0v8AxmFmjjwHkZ%2BxuLGm6WobfOQLI%2BFXVqvWsm9JFrjBzZ1q23Xt8IoF284zcz0ko4qCkXST2kDNpN4zQAgoUF3N1F75%2Ba0pu4g2Zxj1BLQkbz3j45AONqypdooFaqmmbxnHF%2F0mZV&X-Amz-Signature=618cd7cdb6a68a95b52a8d43ef3cb8a646498c8f4d3fe4c711a8790e47ac9ecb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624HOW7KF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCICg7%2BHzL83ZYmIpL9iKpJUMzAE5LLZF5dvUNSZskzI0LAiEA90sAUGy9SxRlB1ylMc9zO7DfuC8P%2ByK3jZW%2BwbVQ3p4q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDGCCxADV9TId51HfRircA%2FAXBz1tX%2FJ97cPLD62MnE0KeuZ15ay17Nw2WCRi43qnFIGS%2Fxnsk7Wb5%2BwnbcyxMz9eZTgJ%2BXdGFIlvwOlRq9sxaDzH8tii%2F%2FkqXM3voTr7jFkopF3mOUXcE6Wy9bqr0NYLQEBomiBb1H2nbb1l1yC63pYkzNGcIpqH948dTFtFX7K7L4U92DrCP43vi0Kjf7MbZlXuwmDS1HXjJ9N6WAdkuQuVI%2BdhU9qec7Gwv2D9eew9x%2FbQ2PZB8GFSsOn2Pq4msSG2qnVP4ICIu3yw8T8vdOiKqfj3f4syE%2Fr5ZzAk9SeCO65cgTaWq1Y%2FzOrGjD1aqDwg5iCOIxxCUyik9Q3xI5A7ij1N1UzsxOJR9naMPdVWEbf4B1h9TobaT5uKerdcUlhcu83cc2dYed2LKcAlwdoZCaYWS8PbAhnOCZ3KBZek7GbuZnUKy6JCHP%2BaHoWJkzT%2FwaK87SqYh6Ghque954qEA1ZKXbNS8ik0OdEJA3i0q%2FvhpjWVm8EgqazvuA3eoa%2BmlqMvw34g2kfII10OYpgC%2FgANvq8%2BnV63gtpJs4EZzmYKf6iaV6vuO%2FbRFtgetpVE%2BE8q5mVk7ig3w2mGeTNp4Cab0u0T2CQJs%2FYUdXSq0JEWrzmhnK%2BAMNauh70GOqUBwyZB2rP48JHBTkJwFoG0HRP9qqr%2BwzKrH4p%2FJoNjc3vg%2FP0FCNsJ9S2XT1Dbvxrk%2B0fFQAARcjVIu61WVL0v8AxmFmjjwHkZ%2BxuLGm6WobfOQLI%2BFXVqvWsm9JFrjBzZ1q23Xt8IoF284zcz0ko4qCkXST2kDNpN4zQAgoUF3N1F75%2Ba0pu4g2Zxj1BLQkbz3j45AONqypdooFaqmmbxnHF%2F0mZV&X-Amz-Signature=f4b7041cba8c34d88e96e639a3c2eab59db1d7ea4ed3628ebe0ff4cd9b076653&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TLO7FRT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIGD%2Bw91aM6xG3d6GSyOkAHXnUUhStPdqY6au1C7v0jPWAiBAIw0lTJ6xjdPB7rf27xjGFlvohjPzvuEAaEhEQ%2FjjQir%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMf4552C6qJ42%2Fpox5KtwDgTRea0uZIVtbfdDNsK95qsqBQ83NKCE2ufh%2BwVfCUZ1pjId%2BJ9VXch4bUAgFZEjttZGvFtHqrMhguz7nm7j%2Fiil4sUDk4kIdtlJ%2F%2F12yHQHztpx%2BU7HvuEOQENsPL4SUkC21okrLbq27QesP9NCttCFgByHnJmsvfCcjzLLLS5D%2BfSIEjPQvoY9skfqeSEBPgcWe0DXSCT%2B%2Bm2XiuwmJGcQARDo9Gj8JBtvi24TOtEanS0XBpCOZ4qVC25VsocnbANyJ923z3exEb42ktpcJwb2l1lxJvzd8X%2B4FXcBEbl%2FZJ6xsgjDpmz5tiHUYy0erfevNPvlRcAe%2FPjWepNC00ConF%2F1EtwfIzIiZqwj2J3E%2FswVMZNVtHXCzm9ssu55TF2BHENlZaiw59w07vi68bhJD1lNZKKVztqXp9WUm6I0Inbhg3uol%2FU5%2BauHwqv8LwL4jdvvlxGY8GrP2MS%2FUylr2C3gqPYYmfiaT2a1nRPhCw80Os8OtnYkf%2FQLBr%2BtvYxEGBRKjhAtshk0%2FFMEARB0NRb8OzpdYcx%2FWJ8D%2FuRhep%2BTiKyeca0QlzDs%2B4dRIvYb1pG3ZxQoYcMAx58poGXIGnEkty3v2mQkNtn6NoZI%2B7t95zCprgfnl2UUwt66HvQY6pgEH8%2BzjS%2FVMsaNpXIrgVQY%2FoyrLNFN8KwPgdh34H0yKrjEdnvpT9oslwkwVPJDOMT61vXSmsr6EpcI4oFGunrwuUE5z31DsQA43VIxQ8b%2BoCgVZ%2FFjgcPXatnSaaMd1tUqyQit7hxk6qWaplWnVEWTjT8cX2g8zME0Gh2nnDv3ra2BjBcs%2B0gwirpC6DXIg5M1RE0IOehYn0UgieA4U%2FiziNe%2FWNanD&X-Amz-Signature=ab1152ef044504547bdc36c8bc4405051849cc5a9b183c7ab1b0a15cc7a3db0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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