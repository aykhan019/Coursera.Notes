

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBXRJPGT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDmV5dMzbI6AEKppjnFzpy4Bhi2f8SrSUIXKBWuSBeI%2BwIhAL7J7ToXA2FBDq3IL%2FOebUSJWFcHi2lu1gg0N8SZBqB8Kv8DCCsQABoMNjM3NDIzMTgzODA1Igxq98qpkbjaSzBmOvYq3APLcub3x9y9NQxJWe5rl2yzf5zTaqjuF6ZRJebVmIVtxc7PwxZnP7EfBt32SdsBOGOax0Qem%2F44BZwxYq2F123FlmfxI8eUZz2oJ47bmPYoHRCfXxT%2BMeNsHBnaNpQkJD48W4halcuhZO8CBXxwjoGqhCoz17LAWd8fGRz4a5Rxf1z91JEzV6NQNnYIIQqijgvmYMIjxuZLI4T1pyhAwc9%2Ban1yLSmxavCG0wffGFq8nj7Bke95IUILC5YyCZwujdP%2FydYK6nk8xcRM3Gct50wHhJEKYTU6QHtl50gVqgpo9ygy89CfrcwkYWSaFPixRuWi9II1jStHXsTiAZ5tGvaMyTJbcr6X2x3M8DRSUtO3LfGUYAkswxUHXljLN52eeDopRGf37YpDrUyvcPN32kk7pYMz6kWvAAaYBMnJUmTRS%2BZ%2B7cQv5dQobGt1Wq0igXk4dSEgfhn82d6qQZPDdKtxzBJ3JG0vH7K2%2B9spjUW0ijivC4N8mNJo3FAlPKuMYtJh3%2FAmUCtz6XZlfj5%2FMuHPOv9uZ1lXATJV9OnKMP95bwi%2B5zp0lGE6PeY1GIAhBj6r2BaDe2HgH%2Bd7OGYnUs8iS147Iq7st3J62ra%2FArQYH%2BUBrA25YmfY8KyVpjCvyoe9BjqkATSNRn8zLQDPbOweRDrDgnEhFv%2Bu2sv6T3uVvOKLoVyeALzcF27w5It5hmqoL1f1e7arfax0SbxmhgzMb2aKUKDr5Ka38emvwTrJ2pST0%2Fz%2BLGNXfHG8ioqt6e5AEMkP3JauwqcJnJ0m7keEpDEUqHAQf23OTN6GJV0yZjgr9U9VyYqq1H5UV0FMJzdD51QHsVr%2BVzMlf%2B2IrZ4fF4d8Rm898eWG&X-Amz-Signature=7807e45c3854ddaf64ab940e3e0e810f17ba1669f11c5a44fe85eb05910fdd59&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBXRJPGT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDmV5dMzbI6AEKppjnFzpy4Bhi2f8SrSUIXKBWuSBeI%2BwIhAL7J7ToXA2FBDq3IL%2FOebUSJWFcHi2lu1gg0N8SZBqB8Kv8DCCsQABoMNjM3NDIzMTgzODA1Igxq98qpkbjaSzBmOvYq3APLcub3x9y9NQxJWe5rl2yzf5zTaqjuF6ZRJebVmIVtxc7PwxZnP7EfBt32SdsBOGOax0Qem%2F44BZwxYq2F123FlmfxI8eUZz2oJ47bmPYoHRCfXxT%2BMeNsHBnaNpQkJD48W4halcuhZO8CBXxwjoGqhCoz17LAWd8fGRz4a5Rxf1z91JEzV6NQNnYIIQqijgvmYMIjxuZLI4T1pyhAwc9%2Ban1yLSmxavCG0wffGFq8nj7Bke95IUILC5YyCZwujdP%2FydYK6nk8xcRM3Gct50wHhJEKYTU6QHtl50gVqgpo9ygy89CfrcwkYWSaFPixRuWi9II1jStHXsTiAZ5tGvaMyTJbcr6X2x3M8DRSUtO3LfGUYAkswxUHXljLN52eeDopRGf37YpDrUyvcPN32kk7pYMz6kWvAAaYBMnJUmTRS%2BZ%2B7cQv5dQobGt1Wq0igXk4dSEgfhn82d6qQZPDdKtxzBJ3JG0vH7K2%2B9spjUW0ijivC4N8mNJo3FAlPKuMYtJh3%2FAmUCtz6XZlfj5%2FMuHPOv9uZ1lXATJV9OnKMP95bwi%2B5zp0lGE6PeY1GIAhBj6r2BaDe2HgH%2Bd7OGYnUs8iS147Iq7st3J62ra%2FArQYH%2BUBrA25YmfY8KyVpjCvyoe9BjqkATSNRn8zLQDPbOweRDrDgnEhFv%2Bu2sv6T3uVvOKLoVyeALzcF27w5It5hmqoL1f1e7arfax0SbxmhgzMb2aKUKDr5Ka38emvwTrJ2pST0%2Fz%2BLGNXfHG8ioqt6e5AEMkP3JauwqcJnJ0m7keEpDEUqHAQf23OTN6GJV0yZjgr9U9VyYqq1H5UV0FMJzdD51QHsVr%2BVzMlf%2B2IrZ4fF4d8Rm898eWG&X-Amz-Signature=6da9526f5e91b1e1a8a195c2a75f3fbec76e85cc009a4a01a7ade193e2afae24&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBXRJPGT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDmV5dMzbI6AEKppjnFzpy4Bhi2f8SrSUIXKBWuSBeI%2BwIhAL7J7ToXA2FBDq3IL%2FOebUSJWFcHi2lu1gg0N8SZBqB8Kv8DCCsQABoMNjM3NDIzMTgzODA1Igxq98qpkbjaSzBmOvYq3APLcub3x9y9NQxJWe5rl2yzf5zTaqjuF6ZRJebVmIVtxc7PwxZnP7EfBt32SdsBOGOax0Qem%2F44BZwxYq2F123FlmfxI8eUZz2oJ47bmPYoHRCfXxT%2BMeNsHBnaNpQkJD48W4halcuhZO8CBXxwjoGqhCoz17LAWd8fGRz4a5Rxf1z91JEzV6NQNnYIIQqijgvmYMIjxuZLI4T1pyhAwc9%2Ban1yLSmxavCG0wffGFq8nj7Bke95IUILC5YyCZwujdP%2FydYK6nk8xcRM3Gct50wHhJEKYTU6QHtl50gVqgpo9ygy89CfrcwkYWSaFPixRuWi9II1jStHXsTiAZ5tGvaMyTJbcr6X2x3M8DRSUtO3LfGUYAkswxUHXljLN52eeDopRGf37YpDrUyvcPN32kk7pYMz6kWvAAaYBMnJUmTRS%2BZ%2B7cQv5dQobGt1Wq0igXk4dSEgfhn82d6qQZPDdKtxzBJ3JG0vH7K2%2B9spjUW0ijivC4N8mNJo3FAlPKuMYtJh3%2FAmUCtz6XZlfj5%2FMuHPOv9uZ1lXATJV9OnKMP95bwi%2B5zp0lGE6PeY1GIAhBj6r2BaDe2HgH%2Bd7OGYnUs8iS147Iq7st3J62ra%2FArQYH%2BUBrA25YmfY8KyVpjCvyoe9BjqkATSNRn8zLQDPbOweRDrDgnEhFv%2Bu2sv6T3uVvOKLoVyeALzcF27w5It5hmqoL1f1e7arfax0SbxmhgzMb2aKUKDr5Ka38emvwTrJ2pST0%2Fz%2BLGNXfHG8ioqt6e5AEMkP3JauwqcJnJ0m7keEpDEUqHAQf23OTN6GJV0yZjgr9U9VyYqq1H5UV0FMJzdD51QHsVr%2BVzMlf%2B2IrZ4fF4d8Rm898eWG&X-Amz-Signature=161b0391e6ecab4a072432288939716831655c108b1fe58f236383eec6d3dae5&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4NDIKMW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCrupBayWFjiTz7fYU9nD%2Bp9ovnYLIpjrBhwnGfSGnMvgIhAIENvnTn%2FxIXwoGOP8rTI9GPhp5VW7YRkziTb8PLld7MKv8DCCsQABoMNjM3NDIzMTgzODA1IgwXDz%2Fy9XESkPBh%2Btcq3AOG%2BJHD07sCvlwEsuGxalSX%2Bhpl5ElQGrkoGz%2F6C%2B4dYfhLBGERvL58tsHgToaPdrk5VxzOdXB6BjrX7YSAyXDse25uCG2N%2FMsknJP0ARObU5usgtSILuLsr6pEi5WtvHnOSDi4rwkqRdckEGUWhaySq6FRxAsNMrbuB%2BLYffamaQaccEw5AN%2BdhrGYzYNX3rEmnEiS8b7uHDs1r99Siqv4nQaMnLBeU8FpO5lPQkQKVRF5wZ8tjacrk9nmdfmK34ildI938uz%2B5N4hIbOyODsZV3CyAhwIS0qRoes2aNyas1Gcpvf16cyTn7SPwxs2aFeZsMptHU6kkPY31cQiqor8aBQ9M9PfNzwRq7Zjz1TDqx9A1wZJpGOfn2nLKefRh2ixdbTQgoab5%2BPE74hM0K%2Fw3zQslRZWXVdMY6K%2FSWzZku9TQ%2FlnaxH7CbI5ICrxIRGwY1mflV6%2Fb2bdsJuxfmIHhA9kJahoftdTrDgwrMlNgMdltJ2RJIW5aKxXsYQIsRa8OQhdqdT%2Bh10LbZRi71%2Foi%2FiOqKyE6tzE6o3mdCivVSfvtzXZQ8ls1dA0ZCKyW0DdAlW93QiYh5lk4EtrABSAoGk7%2BwY0%2BmDQrZBstc%2FDyHW%2B0rRyAf6kCkW0njDCyoe9BjqkAbMoqlQ4h7SWllgbQrS90IXCZqTHcRDL4QjE11OH9ArfL69eesl6qDPwuxKYE9qnfzNCfZyslm%2FrwfhuN4Ej8RuFn3ayfwjYveCg1rCF3kCLxzMrcq8Wyz5A%2Bzx8E%2Bwga3uwp8XOvPTGkuE0YSdmZ0QUfO2ZrTag5Gq%2BW7pPiYa1IUa7gim7FjQ%2FtC03xoo0c6MwpxixFS1gYP9PEjXOi3t0dXwR&X-Amz-Signature=58aec17994a9e2462053b00da0d1f32f97f6d2adb9bf21358872770d4e48a804&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4NDIKMW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQCrupBayWFjiTz7fYU9nD%2Bp9ovnYLIpjrBhwnGfSGnMvgIhAIENvnTn%2FxIXwoGOP8rTI9GPhp5VW7YRkziTb8PLld7MKv8DCCsQABoMNjM3NDIzMTgzODA1IgwXDz%2Fy9XESkPBh%2Btcq3AOG%2BJHD07sCvlwEsuGxalSX%2Bhpl5ElQGrkoGz%2F6C%2B4dYfhLBGERvL58tsHgToaPdrk5VxzOdXB6BjrX7YSAyXDse25uCG2N%2FMsknJP0ARObU5usgtSILuLsr6pEi5WtvHnOSDi4rwkqRdckEGUWhaySq6FRxAsNMrbuB%2BLYffamaQaccEw5AN%2BdhrGYzYNX3rEmnEiS8b7uHDs1r99Siqv4nQaMnLBeU8FpO5lPQkQKVRF5wZ8tjacrk9nmdfmK34ildI938uz%2B5N4hIbOyODsZV3CyAhwIS0qRoes2aNyas1Gcpvf16cyTn7SPwxs2aFeZsMptHU6kkPY31cQiqor8aBQ9M9PfNzwRq7Zjz1TDqx9A1wZJpGOfn2nLKefRh2ixdbTQgoab5%2BPE74hM0K%2Fw3zQslRZWXVdMY6K%2FSWzZku9TQ%2FlnaxH7CbI5ICrxIRGwY1mflV6%2Fb2bdsJuxfmIHhA9kJahoftdTrDgwrMlNgMdltJ2RJIW5aKxXsYQIsRa8OQhdqdT%2Bh10LbZRi71%2Foi%2FiOqKyE6tzE6o3mdCivVSfvtzXZQ8ls1dA0ZCKyW0DdAlW93QiYh5lk4EtrABSAoGk7%2BwY0%2BmDQrZBstc%2FDyHW%2B0rRyAf6kCkW0njDCyoe9BjqkAbMoqlQ4h7SWllgbQrS90IXCZqTHcRDL4QjE11OH9ArfL69eesl6qDPwuxKYE9qnfzNCfZyslm%2FrwfhuN4Ej8RuFn3ayfwjYveCg1rCF3kCLxzMrcq8Wyz5A%2Bzx8E%2Bwga3uwp8XOvPTGkuE0YSdmZ0QUfO2ZrTag5Gq%2BW7pPiYa1IUa7gim7FjQ%2FtC03xoo0c6MwpxixFS1gYP9PEjXOi3t0dXwR&X-Amz-Signature=7bcdf99afffcc0a7576551d92a3952cb60c02933662d0c0cc0bbf6ef51708e72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBXRJPGT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDmV5dMzbI6AEKppjnFzpy4Bhi2f8SrSUIXKBWuSBeI%2BwIhAL7J7ToXA2FBDq3IL%2FOebUSJWFcHi2lu1gg0N8SZBqB8Kv8DCCsQABoMNjM3NDIzMTgzODA1Igxq98qpkbjaSzBmOvYq3APLcub3x9y9NQxJWe5rl2yzf5zTaqjuF6ZRJebVmIVtxc7PwxZnP7EfBt32SdsBOGOax0Qem%2F44BZwxYq2F123FlmfxI8eUZz2oJ47bmPYoHRCfXxT%2BMeNsHBnaNpQkJD48W4halcuhZO8CBXxwjoGqhCoz17LAWd8fGRz4a5Rxf1z91JEzV6NQNnYIIQqijgvmYMIjxuZLI4T1pyhAwc9%2Ban1yLSmxavCG0wffGFq8nj7Bke95IUILC5YyCZwujdP%2FydYK6nk8xcRM3Gct50wHhJEKYTU6QHtl50gVqgpo9ygy89CfrcwkYWSaFPixRuWi9II1jStHXsTiAZ5tGvaMyTJbcr6X2x3M8DRSUtO3LfGUYAkswxUHXljLN52eeDopRGf37YpDrUyvcPN32kk7pYMz6kWvAAaYBMnJUmTRS%2BZ%2B7cQv5dQobGt1Wq0igXk4dSEgfhn82d6qQZPDdKtxzBJ3JG0vH7K2%2B9spjUW0ijivC4N8mNJo3FAlPKuMYtJh3%2FAmUCtz6XZlfj5%2FMuHPOv9uZ1lXATJV9OnKMP95bwi%2B5zp0lGE6PeY1GIAhBj6r2BaDe2HgH%2Bd7OGYnUs8iS147Iq7st3J62ra%2FArQYH%2BUBrA25YmfY8KyVpjCvyoe9BjqkATSNRn8zLQDPbOweRDrDgnEhFv%2Bu2sv6T3uVvOKLoVyeALzcF27w5It5hmqoL1f1e7arfax0SbxmhgzMb2aKUKDr5Ka38emvwTrJ2pST0%2Fz%2BLGNXfHG8ioqt6e5AEMkP3JauwqcJnJ0m7keEpDEUqHAQf23OTN6GJV0yZjgr9U9VyYqq1H5UV0FMJzdD51QHsVr%2BVzMlf%2B2IrZ4fF4d8Rm898eWG&X-Amz-Signature=a2b3546f83fa8e1686dabfa7ef5699a3639324cd9aa26fcfc484d40bd70eb490&X-Amz-SignedHeaders=host&x-id=GetObject)
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