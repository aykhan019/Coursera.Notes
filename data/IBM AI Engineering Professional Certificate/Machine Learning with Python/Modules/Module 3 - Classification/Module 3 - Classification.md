

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FYRVSNS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQCuKJHLN4kAkOXAyIcm1vKQlCZyRYqCbMcLwo3j3XMOUwIgI%2Ffc06dBTtkxBsBZLzgD8INSjlErzHLnVPu93fs2r9kq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIyQd4nA5KNrGmFIsSrcAzzzMzSfCp2nQdPH2laLz2Tj0piBA6FUoxvZULGdTMV6x7s7NCgZa09ENzvdN2%2F6I6G20t95%2Bh9UNXU%2FlCwsMvaTT7Wqd7RkFQ3g6sT%2F9GcEDfAR2WB4LlAOp72SJ5JdfnGrTIqB89x84%2B8cqodhD5o63k08ZUfeQxoncNdWqIiqkKKhR%2FlYih7V9Z0X%2BPDyGkBgbVW9Rnc%2FGQfTXqFs4%2Fpzccv5%2F7P%2BPJDrMGd7ZdjzsKIehOCzyUErdV0XWGvOyzU0BcGUbVqVzdIYRYP5Ly8HY%2BT6FOYKYvxkNhHky8uj%2BR7n7a26F8VhII6feSVd3RYQqQATTQsufDfQLmqjaCFGCeI7Y1hA0tArc%2Fa5CaXzUrwBdj7RYMBDjoe1PFlLy4x8H9X2f%2F%2Fij5FrqZjNTJQA6vK9ZC35Ok1n1ZNr7T7PWblnzdTAKfVRe7j4s1jk2pKHyE%2FOxDIXxhM2tmxUrvq47m6qwM6NKFKbvs7onJpCZwuMBr6mN8WvMVob2GcalFahVZi21mCmJzyQJihFCXFpwLLeWYCjV3MsbjWJFaUawWWEkoK1irDkEsJjfHn48ZuGczl6%2Bn4JUp%2F%2BTVeS06Mub0wRmPMpR%2B%2FnxgBixVjG%2FytGufKvouEJxv36MLnrj70GOqUBqJ5u8dL9sMZOXZbGv41XDtnEDr2IArkKWlko8sjjX%2BTrVM0VBiP9VfBcjanN16El9ndJyxwH033H0rDz0iTRDOQ2J5n1XbU4O6MSBsw4GnDti8DOEbp00RGlAz7F06X77UCwdtI4gssU2JqoZ1LBosmmnkNGw3SKlNYHkCH3eOwdMCz03iKJlzP7AoglA4JY4dZ5HOy2KqpKsIEUxoLFvU1gjMC%2B&X-Amz-Signature=31b85faaeee8a9c85df6f1078ac1a696032c5b9ee19a396dac68f79c09fbbdc6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FYRVSNS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQCuKJHLN4kAkOXAyIcm1vKQlCZyRYqCbMcLwo3j3XMOUwIgI%2Ffc06dBTtkxBsBZLzgD8INSjlErzHLnVPu93fs2r9kq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIyQd4nA5KNrGmFIsSrcAzzzMzSfCp2nQdPH2laLz2Tj0piBA6FUoxvZULGdTMV6x7s7NCgZa09ENzvdN2%2F6I6G20t95%2Bh9UNXU%2FlCwsMvaTT7Wqd7RkFQ3g6sT%2F9GcEDfAR2WB4LlAOp72SJ5JdfnGrTIqB89x84%2B8cqodhD5o63k08ZUfeQxoncNdWqIiqkKKhR%2FlYih7V9Z0X%2BPDyGkBgbVW9Rnc%2FGQfTXqFs4%2Fpzccv5%2F7P%2BPJDrMGd7ZdjzsKIehOCzyUErdV0XWGvOyzU0BcGUbVqVzdIYRYP5Ly8HY%2BT6FOYKYvxkNhHky8uj%2BR7n7a26F8VhII6feSVd3RYQqQATTQsufDfQLmqjaCFGCeI7Y1hA0tArc%2Fa5CaXzUrwBdj7RYMBDjoe1PFlLy4x8H9X2f%2F%2Fij5FrqZjNTJQA6vK9ZC35Ok1n1ZNr7T7PWblnzdTAKfVRe7j4s1jk2pKHyE%2FOxDIXxhM2tmxUrvq47m6qwM6NKFKbvs7onJpCZwuMBr6mN8WvMVob2GcalFahVZi21mCmJzyQJihFCXFpwLLeWYCjV3MsbjWJFaUawWWEkoK1irDkEsJjfHn48ZuGczl6%2Bn4JUp%2F%2BTVeS06Mub0wRmPMpR%2B%2FnxgBixVjG%2FytGufKvouEJxv36MLnrj70GOqUBqJ5u8dL9sMZOXZbGv41XDtnEDr2IArkKWlko8sjjX%2BTrVM0VBiP9VfBcjanN16El9ndJyxwH033H0rDz0iTRDOQ2J5n1XbU4O6MSBsw4GnDti8DOEbp00RGlAz7F06X77UCwdtI4gssU2JqoZ1LBosmmnkNGw3SKlNYHkCH3eOwdMCz03iKJlzP7AoglA4JY4dZ5HOy2KqpKsIEUxoLFvU1gjMC%2B&X-Amz-Signature=ffff62cb5f32c3efdde200c48df5c18074b98b31a155617f9a51c4bdf3dbddd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FYRVSNS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQCuKJHLN4kAkOXAyIcm1vKQlCZyRYqCbMcLwo3j3XMOUwIgI%2Ffc06dBTtkxBsBZLzgD8INSjlErzHLnVPu93fs2r9kq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIyQd4nA5KNrGmFIsSrcAzzzMzSfCp2nQdPH2laLz2Tj0piBA6FUoxvZULGdTMV6x7s7NCgZa09ENzvdN2%2F6I6G20t95%2Bh9UNXU%2FlCwsMvaTT7Wqd7RkFQ3g6sT%2F9GcEDfAR2WB4LlAOp72SJ5JdfnGrTIqB89x84%2B8cqodhD5o63k08ZUfeQxoncNdWqIiqkKKhR%2FlYih7V9Z0X%2BPDyGkBgbVW9Rnc%2FGQfTXqFs4%2Fpzccv5%2F7P%2BPJDrMGd7ZdjzsKIehOCzyUErdV0XWGvOyzU0BcGUbVqVzdIYRYP5Ly8HY%2BT6FOYKYvxkNhHky8uj%2BR7n7a26F8VhII6feSVd3RYQqQATTQsufDfQLmqjaCFGCeI7Y1hA0tArc%2Fa5CaXzUrwBdj7RYMBDjoe1PFlLy4x8H9X2f%2F%2Fij5FrqZjNTJQA6vK9ZC35Ok1n1ZNr7T7PWblnzdTAKfVRe7j4s1jk2pKHyE%2FOxDIXxhM2tmxUrvq47m6qwM6NKFKbvs7onJpCZwuMBr6mN8WvMVob2GcalFahVZi21mCmJzyQJihFCXFpwLLeWYCjV3MsbjWJFaUawWWEkoK1irDkEsJjfHn48ZuGczl6%2Bn4JUp%2F%2BTVeS06Mub0wRmPMpR%2B%2FnxgBixVjG%2FytGufKvouEJxv36MLnrj70GOqUBqJ5u8dL9sMZOXZbGv41XDtnEDr2IArkKWlko8sjjX%2BTrVM0VBiP9VfBcjanN16El9ndJyxwH033H0rDz0iTRDOQ2J5n1XbU4O6MSBsw4GnDti8DOEbp00RGlAz7F06X77UCwdtI4gssU2JqoZ1LBosmmnkNGw3SKlNYHkCH3eOwdMCz03iKJlzP7AoglA4JY4dZ5HOy2KqpKsIEUxoLFvU1gjMC%2B&X-Amz-Signature=c1d76e009b5d8982d149d50445c2af7ab4fc760a5ba62e085b0589d94ac14428&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXYJ6TT2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCMLzfCcg%2BfBojM33qn0KuLQ8DVXkyA1xJQVnqOUH1BlgIhAOP%2FosOOB30%2BjqVEKqhIsQqqYo3OqS5dc9y1O5MHfr0MKv8DCFEQABoMNjM3NDIzMTgzODA1Igwa4Q2V%2Bqo8lVQvgGoq3AM8ovOSJ%2BahXb%2BdfKc3S0pHMd4Bck56WLp6FysHJ8dKvMTZx7vzPW9907weTj9welLnErpGFczZApgYsQCd0e5Uk4gXIUxxaMdruH7kUaqGHJmyk%2BrSJjNIViW%2FWAtMCUKRi6cAmvebzTL3N0d5XiQpHphoydRzud%2FbmKWMatI5hNRuPBOZYZcH9OHsfYJQ3osQRHEwKRp83Pl%2FxXkUu8WbbBDJpS%2BLqLOX9AGutPqHByEM80SabWF6UmfOGokJ5sQPJJpx9dneyF4pXIGlVYFy%2BY68w3KRXRW5wDfosyCt52zVtuM5S7cy3u6GSIid82%2BmMbqjIo0o%2F6kgLreAzLzyut32Iyncz9DAKI7%2BT0n3Oq6FaTU0tcerCXh9oZQ8sw%2FXa%2FxXjC%2BX7MP3AkKG%2BU9e5%2B%2BB6D0c78yBEeHSPN3VUlkDIn4Ozihl3LrWgnPETUhPJD6extNiQCyo7oO9zzR5BY3K8O5wtIq8ZjMqyzJVaA0tlYA75HwKRwLDGlEr2oG7oagG11Gkms%2FCjEX7pnLPtSL%2B18M1R4p3tuxMvZlrt6JOFbksms01VqvBbKGXZ4znBLUDrP5qvFO9eSl75BQt0ealDovKgpJCRZ%2BBWn1xSaeojWoC6okzMm%2FuDjC96o%2B9BjqkASOW5AWBRAFcK4UsC3E9dfGahJmniu9sJaw13Dp3mFYEDIoWqdM3tlBhMUi%2F0531aeR88XKsj8gS8gLkou%2BfIAdWnKl7DEUWhxD7ijqN5r8QKuODXG5yA6xZs%2BZCO9PoMgYf0YtK2QXVjLvsZsdvE72LpmnI0vAc9Jxx33L%2FTM6MEvtSSqCs9oDNBdg%2FjAap22gK4kCkoM40hVKXo0zD98EPr%2FU%2F&X-Amz-Signature=4f533266dfdf55706bab66d1315d941b8b8f50455a886a146fbccd2a9e1739c6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXYJ6TT2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCMLzfCcg%2BfBojM33qn0KuLQ8DVXkyA1xJQVnqOUH1BlgIhAOP%2FosOOB30%2BjqVEKqhIsQqqYo3OqS5dc9y1O5MHfr0MKv8DCFEQABoMNjM3NDIzMTgzODA1Igwa4Q2V%2Bqo8lVQvgGoq3AM8ovOSJ%2BahXb%2BdfKc3S0pHMd4Bck56WLp6FysHJ8dKvMTZx7vzPW9907weTj9welLnErpGFczZApgYsQCd0e5Uk4gXIUxxaMdruH7kUaqGHJmyk%2BrSJjNIViW%2FWAtMCUKRi6cAmvebzTL3N0d5XiQpHphoydRzud%2FbmKWMatI5hNRuPBOZYZcH9OHsfYJQ3osQRHEwKRp83Pl%2FxXkUu8WbbBDJpS%2BLqLOX9AGutPqHByEM80SabWF6UmfOGokJ5sQPJJpx9dneyF4pXIGlVYFy%2BY68w3KRXRW5wDfosyCt52zVtuM5S7cy3u6GSIid82%2BmMbqjIo0o%2F6kgLreAzLzyut32Iyncz9DAKI7%2BT0n3Oq6FaTU0tcerCXh9oZQ8sw%2FXa%2FxXjC%2BX7MP3AkKG%2BU9e5%2B%2BB6D0c78yBEeHSPN3VUlkDIn4Ozihl3LrWgnPETUhPJD6extNiQCyo7oO9zzR5BY3K8O5wtIq8ZjMqyzJVaA0tlYA75HwKRwLDGlEr2oG7oagG11Gkms%2FCjEX7pnLPtSL%2B18M1R4p3tuxMvZlrt6JOFbksms01VqvBbKGXZ4znBLUDrP5qvFO9eSl75BQt0ealDovKgpJCRZ%2BBWn1xSaeojWoC6okzMm%2FuDjC96o%2B9BjqkASOW5AWBRAFcK4UsC3E9dfGahJmniu9sJaw13Dp3mFYEDIoWqdM3tlBhMUi%2F0531aeR88XKsj8gS8gLkou%2BfIAdWnKl7DEUWhxD7ijqN5r8QKuODXG5yA6xZs%2BZCO9PoMgYf0YtK2QXVjLvsZsdvE72LpmnI0vAc9Jxx33L%2FTM6MEvtSSqCs9oDNBdg%2FjAap22gK4kCkoM40hVKXo0zD98EPr%2FU%2F&X-Amz-Signature=bc0ac70053cbd74adcbc6f720a831ed6efd3f24eaa9ef8ff31ba9b155c8d59ba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FYRVSNS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQCuKJHLN4kAkOXAyIcm1vKQlCZyRYqCbMcLwo3j3XMOUwIgI%2Ffc06dBTtkxBsBZLzgD8INSjlErzHLnVPu93fs2r9kq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDIyQd4nA5KNrGmFIsSrcAzzzMzSfCp2nQdPH2laLz2Tj0piBA6FUoxvZULGdTMV6x7s7NCgZa09ENzvdN2%2F6I6G20t95%2Bh9UNXU%2FlCwsMvaTT7Wqd7RkFQ3g6sT%2F9GcEDfAR2WB4LlAOp72SJ5JdfnGrTIqB89x84%2B8cqodhD5o63k08ZUfeQxoncNdWqIiqkKKhR%2FlYih7V9Z0X%2BPDyGkBgbVW9Rnc%2FGQfTXqFs4%2Fpzccv5%2F7P%2BPJDrMGd7ZdjzsKIehOCzyUErdV0XWGvOyzU0BcGUbVqVzdIYRYP5Ly8HY%2BT6FOYKYvxkNhHky8uj%2BR7n7a26F8VhII6feSVd3RYQqQATTQsufDfQLmqjaCFGCeI7Y1hA0tArc%2Fa5CaXzUrwBdj7RYMBDjoe1PFlLy4x8H9X2f%2F%2Fij5FrqZjNTJQA6vK9ZC35Ok1n1ZNr7T7PWblnzdTAKfVRe7j4s1jk2pKHyE%2FOxDIXxhM2tmxUrvq47m6qwM6NKFKbvs7onJpCZwuMBr6mN8WvMVob2GcalFahVZi21mCmJzyQJihFCXFpwLLeWYCjV3MsbjWJFaUawWWEkoK1irDkEsJjfHn48ZuGczl6%2Bn4JUp%2F%2BTVeS06Mub0wRmPMpR%2B%2FnxgBixVjG%2FytGufKvouEJxv36MLnrj70GOqUBqJ5u8dL9sMZOXZbGv41XDtnEDr2IArkKWlko8sjjX%2BTrVM0VBiP9VfBcjanN16El9ndJyxwH033H0rDz0iTRDOQ2J5n1XbU4O6MSBsw4GnDti8DOEbp00RGlAz7F06X77UCwdtI4gssU2JqoZ1LBosmmnkNGw3SKlNYHkCH3eOwdMCz03iKJlzP7AoglA4JY4dZ5HOy2KqpKsIEUxoLFvU1gjMC%2B&X-Amz-Signature=bd8eb7e2ad476fcc583d25d4f0bf3abf47be78ed0c371976c19d8aba27d56a67&X-Amz-SignedHeaders=host&x-id=GetObject)
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