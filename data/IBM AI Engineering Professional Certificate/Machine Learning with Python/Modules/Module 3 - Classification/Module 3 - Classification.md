

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS7UEDUO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIHhPIbATYB5qiuqP%2B8oMovUhpm4wZ5kRHDfC0530R4%2FlAiA6qEqPwbh13YV6bnppDF6ink4ZEc3i1y6950stpR%2FSNir%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMHn%2BoMnzBjGr9sT1VKtwD0hiWgcUMC56KtWmfPh3MEsoZlPj%2B6c3w9D7FRVIrwMVx%2BpquLPIbY2bveMpWNHzYQP7mSZWA0gSkQNHLBQTQVVy4%2BsBTJzDpPN4XoxZlKPK%2FAe%2F5dAPvaRfZl%2Fsxrwql6M%2BusXc4iMu%2F6DpIxnig8Bou7zbqAeo8t62Jjt9yTc5XK00CoYykaw222ZXuJNeUYleGmhr%2Bd26bycjx9zIJThrTnCZgTDvN5G7DVmFS5LiZaucwzyHgcX1ub61IHMdGXDVDZIpyjEU%2FzxlJDZoVeLq%2BIeuZJskGdSLMmJLV1XxFCcHEcA2KG7Vo%2FUNByUSL8h8iTr0b6Yn87y8c4R%2BiRIkZr4CoBicwDJ%2Frii9sBTLeQ%2F1JVIi9U3fQ0dtvFGIw9siA5u%2B1DDLRDzYsV7sH9xjAyUDzCyvSacpmOkCupVCCLb8YDF9I9aLzPIPC3m6qB9Dy4KiIwRdWQ9DmXCf%2BPOI5ERgtRc344%2FB9P8vEcFr7sA%2BD6dalqvN5OQnla6Bt80uJgwSx32xDCzYp6laNb0jMNAb6sRUdlqI98k8XCXVDsp40br9FNOYNy0DaH7lI%2BerPvqDJLvJrVzBcFMLSW9TFlrp55o52jSpnXhQ2T3caC8HPpowAMKHCKQowj5mRvQY6pgFKmo2S7Xz%2BvX5sYhLp0hFFX5ZsOVHaw31GB%2FopgkO7QWhJrmRO%2BFKcBzw1owinEVhhLlGha4B6XCcfCwVmV1LppybSt9HMtL18aDHzTE4nGhRv8fiJUVhuo4YRisNB0CLZ7VFQe3K99iIE1EYvcmLy32ctLea6F6UUYXHNfpCBVldJLijoNqqapBoBF01q6lAKvoFoYGV8%2FovtTBuu%2FY1TC5h1Fjdg&X-Amz-Signature=e1630d56732254a41e7ecd0c95da3f711f787d00e3cae0e74b84ba97a95b2c2a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS7UEDUO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIHhPIbATYB5qiuqP%2B8oMovUhpm4wZ5kRHDfC0530R4%2FlAiA6qEqPwbh13YV6bnppDF6ink4ZEc3i1y6950stpR%2FSNir%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMHn%2BoMnzBjGr9sT1VKtwD0hiWgcUMC56KtWmfPh3MEsoZlPj%2B6c3w9D7FRVIrwMVx%2BpquLPIbY2bveMpWNHzYQP7mSZWA0gSkQNHLBQTQVVy4%2BsBTJzDpPN4XoxZlKPK%2FAe%2F5dAPvaRfZl%2Fsxrwql6M%2BusXc4iMu%2F6DpIxnig8Bou7zbqAeo8t62Jjt9yTc5XK00CoYykaw222ZXuJNeUYleGmhr%2Bd26bycjx9zIJThrTnCZgTDvN5G7DVmFS5LiZaucwzyHgcX1ub61IHMdGXDVDZIpyjEU%2FzxlJDZoVeLq%2BIeuZJskGdSLMmJLV1XxFCcHEcA2KG7Vo%2FUNByUSL8h8iTr0b6Yn87y8c4R%2BiRIkZr4CoBicwDJ%2Frii9sBTLeQ%2F1JVIi9U3fQ0dtvFGIw9siA5u%2B1DDLRDzYsV7sH9xjAyUDzCyvSacpmOkCupVCCLb8YDF9I9aLzPIPC3m6qB9Dy4KiIwRdWQ9DmXCf%2BPOI5ERgtRc344%2FB9P8vEcFr7sA%2BD6dalqvN5OQnla6Bt80uJgwSx32xDCzYp6laNb0jMNAb6sRUdlqI98k8XCXVDsp40br9FNOYNy0DaH7lI%2BerPvqDJLvJrVzBcFMLSW9TFlrp55o52jSpnXhQ2T3caC8HPpowAMKHCKQowj5mRvQY6pgFKmo2S7Xz%2BvX5sYhLp0hFFX5ZsOVHaw31GB%2FopgkO7QWhJrmRO%2BFKcBzw1owinEVhhLlGha4B6XCcfCwVmV1LppybSt9HMtL18aDHzTE4nGhRv8fiJUVhuo4YRisNB0CLZ7VFQe3K99iIE1EYvcmLy32ctLea6F6UUYXHNfpCBVldJLijoNqqapBoBF01q6lAKvoFoYGV8%2FovtTBuu%2FY1TC5h1Fjdg&X-Amz-Signature=0cd679cf03d298c0ee4dc323aee8a87d6ab39d08744cf6fe55c6f59924aaefa2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS7UEDUO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIHhPIbATYB5qiuqP%2B8oMovUhpm4wZ5kRHDfC0530R4%2FlAiA6qEqPwbh13YV6bnppDF6ink4ZEc3i1y6950stpR%2FSNir%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMHn%2BoMnzBjGr9sT1VKtwD0hiWgcUMC56KtWmfPh3MEsoZlPj%2B6c3w9D7FRVIrwMVx%2BpquLPIbY2bveMpWNHzYQP7mSZWA0gSkQNHLBQTQVVy4%2BsBTJzDpPN4XoxZlKPK%2FAe%2F5dAPvaRfZl%2Fsxrwql6M%2BusXc4iMu%2F6DpIxnig8Bou7zbqAeo8t62Jjt9yTc5XK00CoYykaw222ZXuJNeUYleGmhr%2Bd26bycjx9zIJThrTnCZgTDvN5G7DVmFS5LiZaucwzyHgcX1ub61IHMdGXDVDZIpyjEU%2FzxlJDZoVeLq%2BIeuZJskGdSLMmJLV1XxFCcHEcA2KG7Vo%2FUNByUSL8h8iTr0b6Yn87y8c4R%2BiRIkZr4CoBicwDJ%2Frii9sBTLeQ%2F1JVIi9U3fQ0dtvFGIw9siA5u%2B1DDLRDzYsV7sH9xjAyUDzCyvSacpmOkCupVCCLb8YDF9I9aLzPIPC3m6qB9Dy4KiIwRdWQ9DmXCf%2BPOI5ERgtRc344%2FB9P8vEcFr7sA%2BD6dalqvN5OQnla6Bt80uJgwSx32xDCzYp6laNb0jMNAb6sRUdlqI98k8XCXVDsp40br9FNOYNy0DaH7lI%2BerPvqDJLvJrVzBcFMLSW9TFlrp55o52jSpnXhQ2T3caC8HPpowAMKHCKQowj5mRvQY6pgFKmo2S7Xz%2BvX5sYhLp0hFFX5ZsOVHaw31GB%2FopgkO7QWhJrmRO%2BFKcBzw1owinEVhhLlGha4B6XCcfCwVmV1LppybSt9HMtL18aDHzTE4nGhRv8fiJUVhuo4YRisNB0CLZ7VFQe3K99iIE1EYvcmLy32ctLea6F6UUYXHNfpCBVldJLijoNqqapBoBF01q6lAKvoFoYGV8%2FovtTBuu%2FY1TC5h1Fjdg&X-Amz-Signature=10eb358b54c7096c3c46bce55a0855b8f7a078f0be874eef054921b2a42af5a2&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FSCB2DC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDejwnRHWVtOn7oefxxWcBLCTaVAugCsYljMEFpqHK9rgIgSvU33mYyLauQIaOWwISuAVNUJE9oVLo4eOQb7WVfQNkq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFBtbUgC9l4ic6mw7CrcA%2B0B7Qhy4eu%2B6l50A0VWRkvZRlPqdCB%2B1RlMFjMV6sMuxCIyIlB%2FakRpoLo1jk%2BdJtx%2FrAdHn6VvWl9LRxamLRS4sTvG2IFGLijmeyoRFKK9qXMkBjlqx2dtTo5lR42SZ9EaQst0O%2F00Xb6bx9nbH%2BQLwNpXlhdUo4HHPi2NRBSwA7YaCISkdJndxqp6dbgjlp1avrKbjFcGkyY%2Ft0a42f0McHgWGhFeG2tjcE0yXphRsreDglbJHOSAGDcuO0LAYiekVUEMQP%2FKZwPsPABMmQX3wAJgeHESuoLxbIvZSuMm%2BMRSUTGCBDmleqaLoKG5djH5v%2FXUCsC475VcegKqqUkeRG8GNZAmjv6zoH25KPk%2FhxC7Krohnws9Fppv5R8GE2zXm8W4KMm%2Fi5PlGiQcCuTg0MCytU8zyz7OpCNsLUo%2B5nCPyfzuKnxuQNp2KlNo%2BcDkfNEtPxTOWzV0Yxp%2Btrw5EVNmogRfNI%2BkHwkQ1A%2Fkv7y9CoMtWxviwlu4In1xqlgd0xiS7bYbM9PLuUizkvZmsbGvO0SI4xVhF4nJ2yQlMEVvgU7LL8BXzoaVo6qxHCQiORyRVQ6hOS8PCVGA8GnJ%2BKyWM6%2BVzbmUXBu6HzGfyDQYVVnlWFYIwAQZMPSYkb0GOqUBZ%2B0Iu4pq92Wl85sou95bBCP6InDUm8bFfMznWFq2XMroo%2BWYPM2l2mMMflL8p7GyCMlwt1v%2FEFg%2BswI%2Bx%2Btfe%2FGmjH%2BiNeyHtJYB%2BDFdFdVQd%2Bo66qOOX%2BCxU0xI8wU12oIm1Tc%2BKDrm49Yq%2FCXT4ReKifCS80Mqxlnkm9mKpkrx9UQ8JGHsfKodMd0YTvkMBMPbZSpdDmS9HjYQcX4nGJP5nl7D&X-Amz-Signature=d70b9568e1259da845424214ff7296c4138d7bc947f295f18af72c72edb3490f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FSCB2DC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDejwnRHWVtOn7oefxxWcBLCTaVAugCsYljMEFpqHK9rgIgSvU33mYyLauQIaOWwISuAVNUJE9oVLo4eOQb7WVfQNkq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDFBtbUgC9l4ic6mw7CrcA%2B0B7Qhy4eu%2B6l50A0VWRkvZRlPqdCB%2B1RlMFjMV6sMuxCIyIlB%2FakRpoLo1jk%2BdJtx%2FrAdHn6VvWl9LRxamLRS4sTvG2IFGLijmeyoRFKK9qXMkBjlqx2dtTo5lR42SZ9EaQst0O%2F00Xb6bx9nbH%2BQLwNpXlhdUo4HHPi2NRBSwA7YaCISkdJndxqp6dbgjlp1avrKbjFcGkyY%2Ft0a42f0McHgWGhFeG2tjcE0yXphRsreDglbJHOSAGDcuO0LAYiekVUEMQP%2FKZwPsPABMmQX3wAJgeHESuoLxbIvZSuMm%2BMRSUTGCBDmleqaLoKG5djH5v%2FXUCsC475VcegKqqUkeRG8GNZAmjv6zoH25KPk%2FhxC7Krohnws9Fppv5R8GE2zXm8W4KMm%2Fi5PlGiQcCuTg0MCytU8zyz7OpCNsLUo%2B5nCPyfzuKnxuQNp2KlNo%2BcDkfNEtPxTOWzV0Yxp%2Btrw5EVNmogRfNI%2BkHwkQ1A%2Fkv7y9CoMtWxviwlu4In1xqlgd0xiS7bYbM9PLuUizkvZmsbGvO0SI4xVhF4nJ2yQlMEVvgU7LL8BXzoaVo6qxHCQiORyRVQ6hOS8PCVGA8GnJ%2BKyWM6%2BVzbmUXBu6HzGfyDQYVVnlWFYIwAQZMPSYkb0GOqUBZ%2B0Iu4pq92Wl85sou95bBCP6InDUm8bFfMznWFq2XMroo%2BWYPM2l2mMMflL8p7GyCMlwt1v%2FEFg%2BswI%2Bx%2Btfe%2FGmjH%2BiNeyHtJYB%2BDFdFdVQd%2Bo66qOOX%2BCxU0xI8wU12oIm1Tc%2BKDrm49Yq%2FCXT4ReKifCS80Mqxlnkm9mKpkrx9UQ8JGHsfKodMd0YTvkMBMPbZSpdDmS9HjYQcX4nGJP5nl7D&X-Amz-Signature=21064cf26fa877f6998a0ff9fb015f6d860f99b8bb46982e0be1089f7bfe8830&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS7UEDUO%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T062117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIHhPIbATYB5qiuqP%2B8oMovUhpm4wZ5kRHDfC0530R4%2FlAiA6qEqPwbh13YV6bnppDF6ink4ZEc3i1y6950stpR%2FSNir%2FAwhXEAAaDDYzNzQyMzE4MzgwNSIMHn%2BoMnzBjGr9sT1VKtwD0hiWgcUMC56KtWmfPh3MEsoZlPj%2B6c3w9D7FRVIrwMVx%2BpquLPIbY2bveMpWNHzYQP7mSZWA0gSkQNHLBQTQVVy4%2BsBTJzDpPN4XoxZlKPK%2FAe%2F5dAPvaRfZl%2Fsxrwql6M%2BusXc4iMu%2F6DpIxnig8Bou7zbqAeo8t62Jjt9yTc5XK00CoYykaw222ZXuJNeUYleGmhr%2Bd26bycjx9zIJThrTnCZgTDvN5G7DVmFS5LiZaucwzyHgcX1ub61IHMdGXDVDZIpyjEU%2FzxlJDZoVeLq%2BIeuZJskGdSLMmJLV1XxFCcHEcA2KG7Vo%2FUNByUSL8h8iTr0b6Yn87y8c4R%2BiRIkZr4CoBicwDJ%2Frii9sBTLeQ%2F1JVIi9U3fQ0dtvFGIw9siA5u%2B1DDLRDzYsV7sH9xjAyUDzCyvSacpmOkCupVCCLb8YDF9I9aLzPIPC3m6qB9Dy4KiIwRdWQ9DmXCf%2BPOI5ERgtRc344%2FB9P8vEcFr7sA%2BD6dalqvN5OQnla6Bt80uJgwSx32xDCzYp6laNb0jMNAb6sRUdlqI98k8XCXVDsp40br9FNOYNy0DaH7lI%2BerPvqDJLvJrVzBcFMLSW9TFlrp55o52jSpnXhQ2T3caC8HPpowAMKHCKQowj5mRvQY6pgFKmo2S7Xz%2BvX5sYhLp0hFFX5ZsOVHaw31GB%2FopgkO7QWhJrmRO%2BFKcBzw1owinEVhhLlGha4B6XCcfCwVmV1LppybSt9HMtL18aDHzTE4nGhRv8fiJUVhuo4YRisNB0CLZ7VFQe3K99iIE1EYvcmLy32ctLea6F6UUYXHNfpCBVldJLijoNqqapBoBF01q6lAKvoFoYGV8%2FovtTBuu%2FY1TC5h1Fjdg&X-Amz-Signature=ced2b2a109a1b66a509a53e8a00d00d01e87e2794b3ca34ed5a5259b75db630a&X-Amz-SignedHeaders=host&x-id=GetObject)
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