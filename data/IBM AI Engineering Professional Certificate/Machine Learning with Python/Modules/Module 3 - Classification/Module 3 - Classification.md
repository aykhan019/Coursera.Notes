

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFBBF6KQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE7boHOK%2FUnQKBcW75R9hohyAc0F3Jyx8gXnTsy139%2FKAiEA5lEMwQwIUutI7kW0FYg5bPQiP%2BAg4ibfe9wt86GOimoqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIw1y2v0G1GKAG89%2FyrcA%2Buj5ErM69Z%2B9%2BStmsvBQvYT7Q8DtKt5VmAg93Ys%2F7UWphlfP0H%2FMMur2rf4NKgy10OzqTvCcJrJY6i%2BCnte5UlIkCUhpY3NdZ4dhhaLvywcCeRbBJDpEwfWZs4%2F%2B%2FD1s2lGV1%2BT6ISLP4jusPr2TdszZ3ll4OiC0HEkndn78SdWCXSHEVZRrc2PJY3vB%2Fztd%2BZQa50tFvVj0%2FYdKLQUmRySMYH0QU2yNR7hEAbdbIYBXy6IA3pq6xTYU2WMImtIbP7y1bXw%2BX5yniSEzFlBXqN2AaC9e7a5OcpPaOaNdCNrOSf%2B%2B9SuZzV43Imr2lQZTsBLguPQD%2BclIc5a%2F%2BNbkRrLB6lA8FEn79G5kBFs7B7HKRbvEige%2B9mZ862Kro8quUENfohnEbwuYKqaVxoWqrhn%2FNoxfZaFJYFKhqllpvhSGS1tEYK6QgDwd6Yy4xzzB9M%2FTy0ZhQD30EMOzU%2FJjZvXzcjOHYmtmKG8UDzmgoKJx9iWSzBiIbgrbLqUMzjMmDHKyR%2Fc8uXW5Z%2FdTJrSul87L3u%2Fnmt9AwE6svpnJ9Af8rcRiKsvrd8KjO%2Bg4DdM8I%2F8kpdIWBRxfV32C5dx9zRbUNnciuIBi7OeAIHlrP53qopfX1zYayTQiJb%2FMNaOnL0GOqUBr4zWR3sjqN2tfVavnFpZZsCj4pGRspnlI93fYynABa%2B%2BYzCzhbr6wWj29DLYmUVskIsvwtsdpeFXpLRItJBa1tNWonQnebOT09u%2BD7gvkXlTsgnYKmhMjZj8AoPmZTAZJU0SY2%2F%2BGErLRhf1JXBMYnSPVAMkeht47VXBzGVbN8S1WV7RskCa8XVn5fFzPDlzVhENWmRcqTJkSYucaw9ddDzvzuFc&X-Amz-Signature=4db1471d73bcb06c9eec49b6978519b944a0c95f19ebd6ea652aef3f55db7953&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFBBF6KQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE7boHOK%2FUnQKBcW75R9hohyAc0F3Jyx8gXnTsy139%2FKAiEA5lEMwQwIUutI7kW0FYg5bPQiP%2BAg4ibfe9wt86GOimoqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIw1y2v0G1GKAG89%2FyrcA%2Buj5ErM69Z%2B9%2BStmsvBQvYT7Q8DtKt5VmAg93Ys%2F7UWphlfP0H%2FMMur2rf4NKgy10OzqTvCcJrJY6i%2BCnte5UlIkCUhpY3NdZ4dhhaLvywcCeRbBJDpEwfWZs4%2F%2B%2FD1s2lGV1%2BT6ISLP4jusPr2TdszZ3ll4OiC0HEkndn78SdWCXSHEVZRrc2PJY3vB%2Fztd%2BZQa50tFvVj0%2FYdKLQUmRySMYH0QU2yNR7hEAbdbIYBXy6IA3pq6xTYU2WMImtIbP7y1bXw%2BX5yniSEzFlBXqN2AaC9e7a5OcpPaOaNdCNrOSf%2B%2B9SuZzV43Imr2lQZTsBLguPQD%2BclIc5a%2F%2BNbkRrLB6lA8FEn79G5kBFs7B7HKRbvEige%2B9mZ862Kro8quUENfohnEbwuYKqaVxoWqrhn%2FNoxfZaFJYFKhqllpvhSGS1tEYK6QgDwd6Yy4xzzB9M%2FTy0ZhQD30EMOzU%2FJjZvXzcjOHYmtmKG8UDzmgoKJx9iWSzBiIbgrbLqUMzjMmDHKyR%2Fc8uXW5Z%2FdTJrSul87L3u%2Fnmt9AwE6svpnJ9Af8rcRiKsvrd8KjO%2Bg4DdM8I%2F8kpdIWBRxfV32C5dx9zRbUNnciuIBi7OeAIHlrP53qopfX1zYayTQiJb%2FMNaOnL0GOqUBr4zWR3sjqN2tfVavnFpZZsCj4pGRspnlI93fYynABa%2B%2BYzCzhbr6wWj29DLYmUVskIsvwtsdpeFXpLRItJBa1tNWonQnebOT09u%2BD7gvkXlTsgnYKmhMjZj8AoPmZTAZJU0SY2%2F%2BGErLRhf1JXBMYnSPVAMkeht47VXBzGVbN8S1WV7RskCa8XVn5fFzPDlzVhENWmRcqTJkSYucaw9ddDzvzuFc&X-Amz-Signature=d416fdfa96a590a13cd61e1c10465708a33a5090b0bacd99643974fce0089bea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFBBF6KQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE7boHOK%2FUnQKBcW75R9hohyAc0F3Jyx8gXnTsy139%2FKAiEA5lEMwQwIUutI7kW0FYg5bPQiP%2BAg4ibfe9wt86GOimoqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIw1y2v0G1GKAG89%2FyrcA%2Buj5ErM69Z%2B9%2BStmsvBQvYT7Q8DtKt5VmAg93Ys%2F7UWphlfP0H%2FMMur2rf4NKgy10OzqTvCcJrJY6i%2BCnte5UlIkCUhpY3NdZ4dhhaLvywcCeRbBJDpEwfWZs4%2F%2B%2FD1s2lGV1%2BT6ISLP4jusPr2TdszZ3ll4OiC0HEkndn78SdWCXSHEVZRrc2PJY3vB%2Fztd%2BZQa50tFvVj0%2FYdKLQUmRySMYH0QU2yNR7hEAbdbIYBXy6IA3pq6xTYU2WMImtIbP7y1bXw%2BX5yniSEzFlBXqN2AaC9e7a5OcpPaOaNdCNrOSf%2B%2B9SuZzV43Imr2lQZTsBLguPQD%2BclIc5a%2F%2BNbkRrLB6lA8FEn79G5kBFs7B7HKRbvEige%2B9mZ862Kro8quUENfohnEbwuYKqaVxoWqrhn%2FNoxfZaFJYFKhqllpvhSGS1tEYK6QgDwd6Yy4xzzB9M%2FTy0ZhQD30EMOzU%2FJjZvXzcjOHYmtmKG8UDzmgoKJx9iWSzBiIbgrbLqUMzjMmDHKyR%2Fc8uXW5Z%2FdTJrSul87L3u%2Fnmt9AwE6svpnJ9Af8rcRiKsvrd8KjO%2Bg4DdM8I%2F8kpdIWBRxfV32C5dx9zRbUNnciuIBi7OeAIHlrP53qopfX1zYayTQiJb%2FMNaOnL0GOqUBr4zWR3sjqN2tfVavnFpZZsCj4pGRspnlI93fYynABa%2B%2BYzCzhbr6wWj29DLYmUVskIsvwtsdpeFXpLRItJBa1tNWonQnebOT09u%2BD7gvkXlTsgnYKmhMjZj8AoPmZTAZJU0SY2%2F%2BGErLRhf1JXBMYnSPVAMkeht47VXBzGVbN8S1WV7RskCa8XVn5fFzPDlzVhENWmRcqTJkSYucaw9ddDzvzuFc&X-Amz-Signature=9b00c0b160184315c29904fd5d9b7249acbd775c481afa2b3e38c0f358ab5255&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Z54DZXO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDEQl03az5bJDPy%2Fg5b1ZH1ZMFzjgSRpeF2XRee4YG3ywIgY3KLZYEL0lqkMbgRlpntQfOxpvRlkP90XzdwEl3nKp4qiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAfNt6hy%2FRt47WSNzircA0mZAKXJYIiHUTUw9Urxi%2FmCLVCrc0Pdh9uRxrKqnOhTsWGNJE8bVJOjCAREgNqqFr22JR54NWZiDeZxIIWj%2ByfL%2FX3SGDTcrIhdk5s1NOgHACqgToB1gziOcN7eMLnbThDR8PpNBcyXQNhs6s5wHzMzeplnrVpIbqKMhT56AUrJ1PHG9GV0KE%2BqcVusJuj10K%2BUt6RsehCVnnKClGMJYr9UT52x8u6rCsvoqLjsw%2FAoXeNXcy1%2F1jcVlQkfrnZhITMZbANFkAN0Zg3htcjNLW1R2fYAKRCS110nxs4npx8cO6S%2B%2FeFUQJZkKUrJN7E5pOg8Qu1EvtzDm5cUNv4pYWhnXWEnqsCs44ki%2BsYQJ6z2Fc2bm%2Ba4PNOD8owpU3L8M4smPcXUkbLKf%2FtsbZ4zWc5RxYslWToEiIOjbiNazXdRB801FZJ8PPvN95Eq%2F%2Fk7R2JObW820XQcN0WCRRZTYd05Dj1DTLnNnOQd59BGAwjTlYGQY722Bagi2xuRccTDqExexlImoBRCYGfrBMQCLoPMTMpvJ8x8qc2p%2F9i4D%2BOh2PZHCDCZ1rB9bsHerh6GBEPe92DZGVCwgE501bPeVEmoYNCYxnUSP8MPe26wyx8WIZ%2B4HAuepHyc1PaNMNCOnL0GOqUB6oemqmtL33F6ZbA62jTBS9wtPQ%2FFTk3dtkK5Po%2Bq5%2FWhopmxHWvEKsOqaByJTz8SJyuOorm4WdH6QK0EiQPBUK0Tx2RxJqHym%2BR4rGur%2BeWPEaRvNQouU%2FA2kZG7Ond2osjghmsPYBlkOBphD%2BSkG5L5nRr9PEv%2FPKYJmjPp751iEGVMibeXb27Yai0IzCGqkvI2pjLKSEMQHG%2FG6uQxmJPgUIKu&X-Amz-Signature=d3f9392bc4ef002830c565dd02e75c6898b5025dd0b1c01ca21e2644daac5a9d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Z54DZXO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDEQl03az5bJDPy%2Fg5b1ZH1ZMFzjgSRpeF2XRee4YG3ywIgY3KLZYEL0lqkMbgRlpntQfOxpvRlkP90XzdwEl3nKp4qiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAfNt6hy%2FRt47WSNzircA0mZAKXJYIiHUTUw9Urxi%2FmCLVCrc0Pdh9uRxrKqnOhTsWGNJE8bVJOjCAREgNqqFr22JR54NWZiDeZxIIWj%2ByfL%2FX3SGDTcrIhdk5s1NOgHACqgToB1gziOcN7eMLnbThDR8PpNBcyXQNhs6s5wHzMzeplnrVpIbqKMhT56AUrJ1PHG9GV0KE%2BqcVusJuj10K%2BUt6RsehCVnnKClGMJYr9UT52x8u6rCsvoqLjsw%2FAoXeNXcy1%2F1jcVlQkfrnZhITMZbANFkAN0Zg3htcjNLW1R2fYAKRCS110nxs4npx8cO6S%2B%2FeFUQJZkKUrJN7E5pOg8Qu1EvtzDm5cUNv4pYWhnXWEnqsCs44ki%2BsYQJ6z2Fc2bm%2Ba4PNOD8owpU3L8M4smPcXUkbLKf%2FtsbZ4zWc5RxYslWToEiIOjbiNazXdRB801FZJ8PPvN95Eq%2F%2Fk7R2JObW820XQcN0WCRRZTYd05Dj1DTLnNnOQd59BGAwjTlYGQY722Bagi2xuRccTDqExexlImoBRCYGfrBMQCLoPMTMpvJ8x8qc2p%2F9i4D%2BOh2PZHCDCZ1rB9bsHerh6GBEPe92DZGVCwgE501bPeVEmoYNCYxnUSP8MPe26wyx8WIZ%2B4HAuepHyc1PaNMNCOnL0GOqUB6oemqmtL33F6ZbA62jTBS9wtPQ%2FFTk3dtkK5Po%2Bq5%2FWhopmxHWvEKsOqaByJTz8SJyuOorm4WdH6QK0EiQPBUK0Tx2RxJqHym%2BR4rGur%2BeWPEaRvNQouU%2FA2kZG7Ond2osjghmsPYBlkOBphD%2BSkG5L5nRr9PEv%2FPKYJmjPp751iEGVMibeXb27Yai0IzCGqkvI2pjLKSEMQHG%2FG6uQxmJPgUIKu&X-Amz-Signature=f10e741e9d1cdebe3051bebbda2df177b7826cbbeb086cd8bd8a9b98084f0414&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFBBF6KQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIE7boHOK%2FUnQKBcW75R9hohyAc0F3Jyx8gXnTsy139%2FKAiEA5lEMwQwIUutI7kW0FYg5bPQiP%2BAg4ibfe9wt86GOimoqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIw1y2v0G1GKAG89%2FyrcA%2Buj5ErM69Z%2B9%2BStmsvBQvYT7Q8DtKt5VmAg93Ys%2F7UWphlfP0H%2FMMur2rf4NKgy10OzqTvCcJrJY6i%2BCnte5UlIkCUhpY3NdZ4dhhaLvywcCeRbBJDpEwfWZs4%2F%2B%2FD1s2lGV1%2BT6ISLP4jusPr2TdszZ3ll4OiC0HEkndn78SdWCXSHEVZRrc2PJY3vB%2Fztd%2BZQa50tFvVj0%2FYdKLQUmRySMYH0QU2yNR7hEAbdbIYBXy6IA3pq6xTYU2WMImtIbP7y1bXw%2BX5yniSEzFlBXqN2AaC9e7a5OcpPaOaNdCNrOSf%2B%2B9SuZzV43Imr2lQZTsBLguPQD%2BclIc5a%2F%2BNbkRrLB6lA8FEn79G5kBFs7B7HKRbvEige%2B9mZ862Kro8quUENfohnEbwuYKqaVxoWqrhn%2FNoxfZaFJYFKhqllpvhSGS1tEYK6QgDwd6Yy4xzzB9M%2FTy0ZhQD30EMOzU%2FJjZvXzcjOHYmtmKG8UDzmgoKJx9iWSzBiIbgrbLqUMzjMmDHKyR%2Fc8uXW5Z%2FdTJrSul87L3u%2Fnmt9AwE6svpnJ9Af8rcRiKsvrd8KjO%2Bg4DdM8I%2F8kpdIWBRxfV32C5dx9zRbUNnciuIBi7OeAIHlrP53qopfX1zYayTQiJb%2FMNaOnL0GOqUBr4zWR3sjqN2tfVavnFpZZsCj4pGRspnlI93fYynABa%2B%2BYzCzhbr6wWj29DLYmUVskIsvwtsdpeFXpLRItJBa1tNWonQnebOT09u%2BD7gvkXlTsgnYKmhMjZj8AoPmZTAZJU0SY2%2F%2BGErLRhf1JXBMYnSPVAMkeht47VXBzGVbN8S1WV7RskCa8XVn5fFzPDlzVhENWmRcqTJkSYucaw9ddDzvzuFc&X-Amz-Signature=fa9ff072b29e517e762a73c8762b03d2a5de27d15f9d2f4da268ecb019a0bde9&X-Amz-SignedHeaders=host&x-id=GetObject)
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