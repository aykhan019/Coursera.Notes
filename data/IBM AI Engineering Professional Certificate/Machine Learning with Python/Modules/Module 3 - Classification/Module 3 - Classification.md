

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQKSJSJQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIHzDGYI73L8oSAU9ufYyI99IS48TsRitDBY%2BiZvkx3QCAiAeNnZHHt2jlaw54q%2FeKboWUhvbHFpzBwux%2FgXHCOdmHSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMxu%2FjR4n2YledyXhOKtwDoyvS%2B01EJKsY3Mo5IHCQgbzp2xhGpTsTxtQF1ofhdkbJMg7vFJ2PEZ4ub7qgSqm2%2FGgpQXpZ4wCUiSRLUKLiOdKhXn4Ckc6rwd4xkbzfjjM9ZJhMbmvo0FNQpS105u2WUCSwy%2B5tFTO3J4etc8fBNJBwPtin5w7GWnkbtwvs6rCS%2F51SFcpqf283Pv4OwScM4E6NTevkldqggzLE3fl43zFbZ1QF8MXBt6qcmLYEiEbBaLqUIwl4N%2F3leYyJ0g3lzwTNMl9XfS454u6t34NZxXLu0LbwtzZfEmEKlDlOK%2BJWI8PvV45Vbr9AXTQSKPzeYc1YPcuqxQH5PSkq74tjAzJcVNQxaGtTSdvIo3PKAjhY%2Bi6oGWypz46V%2FjhppUWuIDjxDH4xnNPVNcIYyu3Npk96EIsTP4E3Pf3S0mbvPvyBfNZHG2kD7BB0oWsAw4kWY%2FJRAmHeh4RbWAe6KtQROrGXEouCLNDI4oseBexh84yKaEAKbHMGVsp9gTSjsdzmu7IFLoOpzX0UTBWzNjYs2bPAuPHzxRe8P58nk%2B5y3OaveNoh7exsrWzDnrn9PgDg1AkzYGY5nBKjtvLT67WPKdUeKX2oCFLUawGz1535yzj1m270pGJXNOcp9U4wnpaMvQY6pgHRl8j4PLE1AJJRrR2PvA9JGMgVWFvqGHkSEW9DZONRoc6mjpRz4FFE4K%2BWLyLTY61GME9eGGoBIorpLXjw43%2BcANnya0P5KyjBu1IUS3NbLvzyjBbm2XssGeg64ecgNZXW0EjUmr7pP5Vp6wumP%2Fl6dN6gPzMQaIIEp2qqW0X4yDPr3Nm8TCmMYOje0lMDG6YcFt4YX3VUYvUsbMCDl%2BXe0XNdbuN%2B&X-Amz-Signature=05b62242c38ff77c0d92e08eb07df7cbb16cfdd3d6949ca8a88994adf56b6f65&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQKSJSJQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIHzDGYI73L8oSAU9ufYyI99IS48TsRitDBY%2BiZvkx3QCAiAeNnZHHt2jlaw54q%2FeKboWUhvbHFpzBwux%2FgXHCOdmHSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMxu%2FjR4n2YledyXhOKtwDoyvS%2B01EJKsY3Mo5IHCQgbzp2xhGpTsTxtQF1ofhdkbJMg7vFJ2PEZ4ub7qgSqm2%2FGgpQXpZ4wCUiSRLUKLiOdKhXn4Ckc6rwd4xkbzfjjM9ZJhMbmvo0FNQpS105u2WUCSwy%2B5tFTO3J4etc8fBNJBwPtin5w7GWnkbtwvs6rCS%2F51SFcpqf283Pv4OwScM4E6NTevkldqggzLE3fl43zFbZ1QF8MXBt6qcmLYEiEbBaLqUIwl4N%2F3leYyJ0g3lzwTNMl9XfS454u6t34NZxXLu0LbwtzZfEmEKlDlOK%2BJWI8PvV45Vbr9AXTQSKPzeYc1YPcuqxQH5PSkq74tjAzJcVNQxaGtTSdvIo3PKAjhY%2Bi6oGWypz46V%2FjhppUWuIDjxDH4xnNPVNcIYyu3Npk96EIsTP4E3Pf3S0mbvPvyBfNZHG2kD7BB0oWsAw4kWY%2FJRAmHeh4RbWAe6KtQROrGXEouCLNDI4oseBexh84yKaEAKbHMGVsp9gTSjsdzmu7IFLoOpzX0UTBWzNjYs2bPAuPHzxRe8P58nk%2B5y3OaveNoh7exsrWzDnrn9PgDg1AkzYGY5nBKjtvLT67WPKdUeKX2oCFLUawGz1535yzj1m270pGJXNOcp9U4wnpaMvQY6pgHRl8j4PLE1AJJRrR2PvA9JGMgVWFvqGHkSEW9DZONRoc6mjpRz4FFE4K%2BWLyLTY61GME9eGGoBIorpLXjw43%2BcANnya0P5KyjBu1IUS3NbLvzyjBbm2XssGeg64ecgNZXW0EjUmr7pP5Vp6wumP%2Fl6dN6gPzMQaIIEp2qqW0X4yDPr3Nm8TCmMYOje0lMDG6YcFt4YX3VUYvUsbMCDl%2BXe0XNdbuN%2B&X-Amz-Signature=c47724f3769a0944f4f1f30ea3c98c79cb2e1d7d92330cd57322f76ad4dd0b9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQKSJSJQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIHzDGYI73L8oSAU9ufYyI99IS48TsRitDBY%2BiZvkx3QCAiAeNnZHHt2jlaw54q%2FeKboWUhvbHFpzBwux%2FgXHCOdmHSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMxu%2FjR4n2YledyXhOKtwDoyvS%2B01EJKsY3Mo5IHCQgbzp2xhGpTsTxtQF1ofhdkbJMg7vFJ2PEZ4ub7qgSqm2%2FGgpQXpZ4wCUiSRLUKLiOdKhXn4Ckc6rwd4xkbzfjjM9ZJhMbmvo0FNQpS105u2WUCSwy%2B5tFTO3J4etc8fBNJBwPtin5w7GWnkbtwvs6rCS%2F51SFcpqf283Pv4OwScM4E6NTevkldqggzLE3fl43zFbZ1QF8MXBt6qcmLYEiEbBaLqUIwl4N%2F3leYyJ0g3lzwTNMl9XfS454u6t34NZxXLu0LbwtzZfEmEKlDlOK%2BJWI8PvV45Vbr9AXTQSKPzeYc1YPcuqxQH5PSkq74tjAzJcVNQxaGtTSdvIo3PKAjhY%2Bi6oGWypz46V%2FjhppUWuIDjxDH4xnNPVNcIYyu3Npk96EIsTP4E3Pf3S0mbvPvyBfNZHG2kD7BB0oWsAw4kWY%2FJRAmHeh4RbWAe6KtQROrGXEouCLNDI4oseBexh84yKaEAKbHMGVsp9gTSjsdzmu7IFLoOpzX0UTBWzNjYs2bPAuPHzxRe8P58nk%2B5y3OaveNoh7exsrWzDnrn9PgDg1AkzYGY5nBKjtvLT67WPKdUeKX2oCFLUawGz1535yzj1m270pGJXNOcp9U4wnpaMvQY6pgHRl8j4PLE1AJJRrR2PvA9JGMgVWFvqGHkSEW9DZONRoc6mjpRz4FFE4K%2BWLyLTY61GME9eGGoBIorpLXjw43%2BcANnya0P5KyjBu1IUS3NbLvzyjBbm2XssGeg64ecgNZXW0EjUmr7pP5Vp6wumP%2Fl6dN6gPzMQaIIEp2qqW0X4yDPr3Nm8TCmMYOje0lMDG6YcFt4YX3VUYvUsbMCDl%2BXe0XNdbuN%2B&X-Amz-Signature=2328e6254c497c5d73425a8d7d60322661f6552153afe56d7642cf5bd346855a&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWK3SWEC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCICQlEhy1yD07%2F0BiCpMwnJuGNRdrq1oB0kD7RYdTx5zxAiAH%2BZJC6Ha4%2FzTVzZxNbv7P49%2BxiYE1vGEjpm9tHCWjxCr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIM%2FE5imNm8xiUnaftlKtwDQaUqt0KgTjdSagfMwV0naEAKc15o8KA3q52lxpBmRrBIMZqgN8lVQomWjCqPXb3fzDog5%2BOExhyIeOjnCDJNOnbmWokIFFaLhIXxXDI2ZlnWqNswI2jFg%2FD3wfUwnsaVnnJA3gHprRZc%2B0Cq2TFXxOnAIKgEYVxCL8mdbtnewCeB6Ol98fq0EcjqBJgWOwoRqF37DJQsM81vw%2BhcMaJb1e6fbalFTvrJdWkdumgiLVeBrn4vgUwVm0gIA0H7Pmn5IA0U89wfH2fYjH5Y2pa5EMCiXWOOuhgZDEdLjp4eStEY8CetCNyzGg2g04nwk2jgZHhF4KTgzANXmIQcqvkjmQhkWKlTCsRsbb3jK1KpL4%2FP5255UI2rF9hzM1CwZb5zANkn5qGUU0qN5IvQx6B44VRcwwIsCFWlTi8vkd%2F2oj9JIEciApRdULFHfxitDa5iwopkZPxyODWquKE4cbKrjIa5STXrQS7fJVQpDhgISKVmqD0a5qPhEhpJUqWh0fMtO8il2Y3LM6Ez3p6MHgSLCGSVdVKbIIwX0pZEdq%2BsID%2FvOfWtpcjivSUo3bNrRDJG1YYIQLqehZ7BiOG9JXmxuA%2B3lTafwjereiADkje2tTQjVyaSRMjKGMA07YYwy5WMvQY6pgGCD1fjbs74tg7m4%2FGjv4CpgZUj1c4YBUC3s%2B6GWXua2soLYyMQvdnlp9d9mguUfoJhlHU8GJYenfJPGQlrioO36LlY3T3KoURgA95KowI2oyNquJz2oETDDI1ShZtdG4vKScOrMOW%2BN%2FCxoAHCwFMxpMAXUX8l34scNZehWPz3BC6D8PoKLb7rK605pFErEWaFNLK1e0p9oDf8E%2BExj10diCg9VSbj&X-Amz-Signature=9a2dd91bc7714a51cf1f153764959cf5e0c6a39702728a05b4976aa4e3353aea&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWK3SWEC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCICQlEhy1yD07%2F0BiCpMwnJuGNRdrq1oB0kD7RYdTx5zxAiAH%2BZJC6Ha4%2FzTVzZxNbv7P49%2BxiYE1vGEjpm9tHCWjxCr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIM%2FE5imNm8xiUnaftlKtwDQaUqt0KgTjdSagfMwV0naEAKc15o8KA3q52lxpBmRrBIMZqgN8lVQomWjCqPXb3fzDog5%2BOExhyIeOjnCDJNOnbmWokIFFaLhIXxXDI2ZlnWqNswI2jFg%2FD3wfUwnsaVnnJA3gHprRZc%2B0Cq2TFXxOnAIKgEYVxCL8mdbtnewCeB6Ol98fq0EcjqBJgWOwoRqF37DJQsM81vw%2BhcMaJb1e6fbalFTvrJdWkdumgiLVeBrn4vgUwVm0gIA0H7Pmn5IA0U89wfH2fYjH5Y2pa5EMCiXWOOuhgZDEdLjp4eStEY8CetCNyzGg2g04nwk2jgZHhF4KTgzANXmIQcqvkjmQhkWKlTCsRsbb3jK1KpL4%2FP5255UI2rF9hzM1CwZb5zANkn5qGUU0qN5IvQx6B44VRcwwIsCFWlTi8vkd%2F2oj9JIEciApRdULFHfxitDa5iwopkZPxyODWquKE4cbKrjIa5STXrQS7fJVQpDhgISKVmqD0a5qPhEhpJUqWh0fMtO8il2Y3LM6Ez3p6MHgSLCGSVdVKbIIwX0pZEdq%2BsID%2FvOfWtpcjivSUo3bNrRDJG1YYIQLqehZ7BiOG9JXmxuA%2B3lTafwjereiADkje2tTQjVyaSRMjKGMA07YYwy5WMvQY6pgGCD1fjbs74tg7m4%2FGjv4CpgZUj1c4YBUC3s%2B6GWXua2soLYyMQvdnlp9d9mguUfoJhlHU8GJYenfJPGQlrioO36LlY3T3KoURgA95KowI2oyNquJz2oETDDI1ShZtdG4vKScOrMOW%2BN%2FCxoAHCwFMxpMAXUX8l34scNZehWPz3BC6D8PoKLb7rK605pFErEWaFNLK1e0p9oDf8E%2BExj10diCg9VSbj&X-Amz-Signature=3920f330ec142fc5cbdd4c607acb2568655a8da82853e61f6b599af1c2f7bc3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQKSJSJQ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIHzDGYI73L8oSAU9ufYyI99IS48TsRitDBY%2BiZvkx3QCAiAeNnZHHt2jlaw54q%2FeKboWUhvbHFpzBwux%2FgXHCOdmHSr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMxu%2FjR4n2YledyXhOKtwDoyvS%2B01EJKsY3Mo5IHCQgbzp2xhGpTsTxtQF1ofhdkbJMg7vFJ2PEZ4ub7qgSqm2%2FGgpQXpZ4wCUiSRLUKLiOdKhXn4Ckc6rwd4xkbzfjjM9ZJhMbmvo0FNQpS105u2WUCSwy%2B5tFTO3J4etc8fBNJBwPtin5w7GWnkbtwvs6rCS%2F51SFcpqf283Pv4OwScM4E6NTevkldqggzLE3fl43zFbZ1QF8MXBt6qcmLYEiEbBaLqUIwl4N%2F3leYyJ0g3lzwTNMl9XfS454u6t34NZxXLu0LbwtzZfEmEKlDlOK%2BJWI8PvV45Vbr9AXTQSKPzeYc1YPcuqxQH5PSkq74tjAzJcVNQxaGtTSdvIo3PKAjhY%2Bi6oGWypz46V%2FjhppUWuIDjxDH4xnNPVNcIYyu3Npk96EIsTP4E3Pf3S0mbvPvyBfNZHG2kD7BB0oWsAw4kWY%2FJRAmHeh4RbWAe6KtQROrGXEouCLNDI4oseBexh84yKaEAKbHMGVsp9gTSjsdzmu7IFLoOpzX0UTBWzNjYs2bPAuPHzxRe8P58nk%2B5y3OaveNoh7exsrWzDnrn9PgDg1AkzYGY5nBKjtvLT67WPKdUeKX2oCFLUawGz1535yzj1m270pGJXNOcp9U4wnpaMvQY6pgHRl8j4PLE1AJJRrR2PvA9JGMgVWFvqGHkSEW9DZONRoc6mjpRz4FFE4K%2BWLyLTY61GME9eGGoBIorpLXjw43%2BcANnya0P5KyjBu1IUS3NbLvzyjBbm2XssGeg64ecgNZXW0EjUmr7pP5Vp6wumP%2Fl6dN6gPzMQaIIEp2qqW0X4yDPr3Nm8TCmMYOje0lMDG6YcFt4YX3VUYvUsbMCDl%2BXe0XNdbuN%2B&X-Amz-Signature=51988f170a78dbc360051d98311430c9ad73ee807b229ac11257716496a85b3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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