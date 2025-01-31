

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637G6FRPQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDEiU3rXmKVSo%2BXEDUZFFwcUnbYicY5w8ZCRFX9zI1HWAiEAzBsehJDL7hUWto7CC2a%2BBF2qDnXY23lGnCOiT80NDzEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJoaU%2BP0TXNsqosOKircA3AsXM9QJGsw2odoJn2zc3I33dRk9v5hpjc%2FKjdNJCSgZ25392Wz8ZvP2imED%2BMYD%2B2YE5uQKxs6NRAxgG6pxltrgBTgB5V8jh1BpbIYV85wYaVepJab%2B2u5HqYDLGtHQ8xkq1ZMJ7rfECbIrwkkQtrqEvwMHvIo2NdK%2BlFgElmn4p%2FZeGK48lfaBPKiCSR2BFbSPUiEKW8kGbalXN7DAWIB%2FFDnU5WrM73x2U5YmaFsijSt3ZCeE8OZ6Y0pT8IINkWZUAmPyiC0nfZGFZwrwMGTNP4SsfKBc0D%2FDnNSbxGaDFhGzqmM1nYZd8wHP8mmZiakLMgWDUE7lCt72I7CVD4gBACIJdaKKtH7Z7qmCR2IFlT24CZ9o0WJwYwEB7OzLuJF%2BjULtT4mPlB51a9PNoNc67KgaYlFDmVFqpSjMU0U08W6tFpJu4F4%2FTDFaZtdCohbL5rA8DnlYZibPmfwntbfHsTq0oVYZM8aY%2BwUXaopRATvkBlP%2FH99xPAPEBdjDKmLg34MNcGdqsusp%2FVvxJL9iC9ivf0kjJSbokuPITIJCXXkEztsDTXkTIqtJcF%2FVbKbU10KH6lokYbUbzrm10aor4M4zTQ%2BvEqmMAzQ5pLC3vFTIUWVWFLkyEXAMK%2FQ8LwGOqUBxE264uBRUsUtqnPLys36o6ymmJZp4oMw%2FftVmBcInScVweBXaXLxnYB4LGC3T3LvkyXZ8pn6AcXfphUjI%2Fm1zV09W4RZbq1saPprqvN9HrFFfbiMmyO%2BU%2BktET4bCA36%2FEPw7AX3vL63yBRcygl1ujretjqhTPEymur%2BQKLa%2B%2BtBzMbaDDDVbcIaN0bGRBY%2Fg1tq%2Ff2C8SPt1ZsJAO4TLFCfj3T6&X-Amz-Signature=cd72d138ae0a5222c7ea74e90c59e37a74e2b2de0e2d28a799092b524e30c9b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637G6FRPQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDEiU3rXmKVSo%2BXEDUZFFwcUnbYicY5w8ZCRFX9zI1HWAiEAzBsehJDL7hUWto7CC2a%2BBF2qDnXY23lGnCOiT80NDzEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJoaU%2BP0TXNsqosOKircA3AsXM9QJGsw2odoJn2zc3I33dRk9v5hpjc%2FKjdNJCSgZ25392Wz8ZvP2imED%2BMYD%2B2YE5uQKxs6NRAxgG6pxltrgBTgB5V8jh1BpbIYV85wYaVepJab%2B2u5HqYDLGtHQ8xkq1ZMJ7rfECbIrwkkQtrqEvwMHvIo2NdK%2BlFgElmn4p%2FZeGK48lfaBPKiCSR2BFbSPUiEKW8kGbalXN7DAWIB%2FFDnU5WrM73x2U5YmaFsijSt3ZCeE8OZ6Y0pT8IINkWZUAmPyiC0nfZGFZwrwMGTNP4SsfKBc0D%2FDnNSbxGaDFhGzqmM1nYZd8wHP8mmZiakLMgWDUE7lCt72I7CVD4gBACIJdaKKtH7Z7qmCR2IFlT24CZ9o0WJwYwEB7OzLuJF%2BjULtT4mPlB51a9PNoNc67KgaYlFDmVFqpSjMU0U08W6tFpJu4F4%2FTDFaZtdCohbL5rA8DnlYZibPmfwntbfHsTq0oVYZM8aY%2BwUXaopRATvkBlP%2FH99xPAPEBdjDKmLg34MNcGdqsusp%2FVvxJL9iC9ivf0kjJSbokuPITIJCXXkEztsDTXkTIqtJcF%2FVbKbU10KH6lokYbUbzrm10aor4M4zTQ%2BvEqmMAzQ5pLC3vFTIUWVWFLkyEXAMK%2FQ8LwGOqUBxE264uBRUsUtqnPLys36o6ymmJZp4oMw%2FftVmBcInScVweBXaXLxnYB4LGC3T3LvkyXZ8pn6AcXfphUjI%2Fm1zV09W4RZbq1saPprqvN9HrFFfbiMmyO%2BU%2BktET4bCA36%2FEPw7AX3vL63yBRcygl1ujretjqhTPEymur%2BQKLa%2B%2BtBzMbaDDDVbcIaN0bGRBY%2Fg1tq%2Ff2C8SPt1ZsJAO4TLFCfj3T6&X-Amz-Signature=c951f0ae0443f86365ddee7152728dc551148703fd024afb6bd2ee552a2cc396&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637G6FRPQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDEiU3rXmKVSo%2BXEDUZFFwcUnbYicY5w8ZCRFX9zI1HWAiEAzBsehJDL7hUWto7CC2a%2BBF2qDnXY23lGnCOiT80NDzEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJoaU%2BP0TXNsqosOKircA3AsXM9QJGsw2odoJn2zc3I33dRk9v5hpjc%2FKjdNJCSgZ25392Wz8ZvP2imED%2BMYD%2B2YE5uQKxs6NRAxgG6pxltrgBTgB5V8jh1BpbIYV85wYaVepJab%2B2u5HqYDLGtHQ8xkq1ZMJ7rfECbIrwkkQtrqEvwMHvIo2NdK%2BlFgElmn4p%2FZeGK48lfaBPKiCSR2BFbSPUiEKW8kGbalXN7DAWIB%2FFDnU5WrM73x2U5YmaFsijSt3ZCeE8OZ6Y0pT8IINkWZUAmPyiC0nfZGFZwrwMGTNP4SsfKBc0D%2FDnNSbxGaDFhGzqmM1nYZd8wHP8mmZiakLMgWDUE7lCt72I7CVD4gBACIJdaKKtH7Z7qmCR2IFlT24CZ9o0WJwYwEB7OzLuJF%2BjULtT4mPlB51a9PNoNc67KgaYlFDmVFqpSjMU0U08W6tFpJu4F4%2FTDFaZtdCohbL5rA8DnlYZibPmfwntbfHsTq0oVYZM8aY%2BwUXaopRATvkBlP%2FH99xPAPEBdjDKmLg34MNcGdqsusp%2FVvxJL9iC9ivf0kjJSbokuPITIJCXXkEztsDTXkTIqtJcF%2FVbKbU10KH6lokYbUbzrm10aor4M4zTQ%2BvEqmMAzQ5pLC3vFTIUWVWFLkyEXAMK%2FQ8LwGOqUBxE264uBRUsUtqnPLys36o6ymmJZp4oMw%2FftVmBcInScVweBXaXLxnYB4LGC3T3LvkyXZ8pn6AcXfphUjI%2Fm1zV09W4RZbq1saPprqvN9HrFFfbiMmyO%2BU%2BktET4bCA36%2FEPw7AX3vL63yBRcygl1ujretjqhTPEymur%2BQKLa%2B%2BtBzMbaDDDVbcIaN0bGRBY%2Fg1tq%2Ff2C8SPt1ZsJAO4TLFCfj3T6&X-Amz-Signature=7faf55ed31da93ea037d85300fddd9a7d3327ef7ae6f58f68e504be5bb53d917&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCSF67SE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGq95AOOOOpeWyDCWUI1hJgt7sCgSfJQ9MpofqsHQJMXAiB1EEKcys2CO2LDO8iNQRzQvl45FzvfjzPhxhyKLy%2FchCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAs76ezJ3DpwbGTr7KtwDlHi7ZB9T5y6oWpZymc16Bhg7TTQhetOCbNfz4iYsWkJD%2FdjeBplgoqhQ0WaHqN4%2BvAY8%2B0IyVCMRfHMU9ZuhEG7YtSrOw7ACyyv7C8HkKguqcKJs2LU%2BR06ERvnXHOy8pEDAJ3Sub5pJicD4d%2FqT4TYn1NCm%2F%2FTdX7a4qF2ZCmcfupMfqihpK1%2F4tcdwCbt6YK4%2FQUmNaTSybgDDlBxcikNxsBDZt6qVzVoreqDvERycvf6zf00N%2FAOOfYd26vcuaHvyc7qY2tqo1sSrMcM%2F55So1glMNTKz7puvqGAdi0VaiIlfp2iejPZJM8xRuievljLC1BERWAmolDsRQhSEpXx6oq0nbImiQW2BiA0Pf7YN1saMwF9QoZKruM2ZfHW81YajJY50j6MQXf3%2FOWaNkLavEkZK5GQ4ay2CqiRKyeGN68SBOaUq9NERBnyVVX3O2m6IX9mmEPMRnzpOGjV2rJ4M8cheS7EI1hjloVely47temgqnc%2F8l4k3aMmpkUmTcgH9e0aiqTDIaDLE6sZi84Eo4fmxP73nLt0sLQmGF7gFUsAAu%2BmxCp%2FhNZTxMSsecPadLQD%2FWuNngW8YZ7kBGgTlugu24MHxN2xV8n40aAREQEatdI%2BUQlkYrXEw1dDwvAY6pgFqTHWCJSfY8z%2F9I%2BUPdD2PJvR2Wo6XjA%2B9iqgeHfkMUKL9QXFp1OgqfPmQSCtYqDwVmXS4L1HHnim5tAaLL5tmeAUpLFraLBjc4MnabPh6Vxzy4Vi%2Bp4Sa3FvyFubYxFtuIrM4ddVa61e4ew2F1GjxI4yGs2BONL3gp4P88hCn50p8aSmxVXlT1wkvwMnu07Z766tWomdOLeowWbpJHhQSZqM%2BEYN2&X-Amz-Signature=7ea663d9400b35743bab687bf32388ce2808dad11d3a6087a38c4929db6b059e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCSF67SE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGq95AOOOOpeWyDCWUI1hJgt7sCgSfJQ9MpofqsHQJMXAiB1EEKcys2CO2LDO8iNQRzQvl45FzvfjzPhxhyKLy%2FchCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAs76ezJ3DpwbGTr7KtwDlHi7ZB9T5y6oWpZymc16Bhg7TTQhetOCbNfz4iYsWkJD%2FdjeBplgoqhQ0WaHqN4%2BvAY8%2B0IyVCMRfHMU9ZuhEG7YtSrOw7ACyyv7C8HkKguqcKJs2LU%2BR06ERvnXHOy8pEDAJ3Sub5pJicD4d%2FqT4TYn1NCm%2F%2FTdX7a4qF2ZCmcfupMfqihpK1%2F4tcdwCbt6YK4%2FQUmNaTSybgDDlBxcikNxsBDZt6qVzVoreqDvERycvf6zf00N%2FAOOfYd26vcuaHvyc7qY2tqo1sSrMcM%2F55So1glMNTKz7puvqGAdi0VaiIlfp2iejPZJM8xRuievljLC1BERWAmolDsRQhSEpXx6oq0nbImiQW2BiA0Pf7YN1saMwF9QoZKruM2ZfHW81YajJY50j6MQXf3%2FOWaNkLavEkZK5GQ4ay2CqiRKyeGN68SBOaUq9NERBnyVVX3O2m6IX9mmEPMRnzpOGjV2rJ4M8cheS7EI1hjloVely47temgqnc%2F8l4k3aMmpkUmTcgH9e0aiqTDIaDLE6sZi84Eo4fmxP73nLt0sLQmGF7gFUsAAu%2BmxCp%2FhNZTxMSsecPadLQD%2FWuNngW8YZ7kBGgTlugu24MHxN2xV8n40aAREQEatdI%2BUQlkYrXEw1dDwvAY6pgFqTHWCJSfY8z%2F9I%2BUPdD2PJvR2Wo6XjA%2B9iqgeHfkMUKL9QXFp1OgqfPmQSCtYqDwVmXS4L1HHnim5tAaLL5tmeAUpLFraLBjc4MnabPh6Vxzy4Vi%2Bp4Sa3FvyFubYxFtuIrM4ddVa61e4ew2F1GjxI4yGs2BONL3gp4P88hCn50p8aSmxVXlT1wkvwMnu07Z766tWomdOLeowWbpJHhQSZqM%2BEYN2&X-Amz-Signature=2d6b222af00aac188660711d359150430dad11309845952206814c56deb8d0b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637G6FRPQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDEiU3rXmKVSo%2BXEDUZFFwcUnbYicY5w8ZCRFX9zI1HWAiEAzBsehJDL7hUWto7CC2a%2BBF2qDnXY23lGnCOiT80NDzEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJoaU%2BP0TXNsqosOKircA3AsXM9QJGsw2odoJn2zc3I33dRk9v5hpjc%2FKjdNJCSgZ25392Wz8ZvP2imED%2BMYD%2B2YE5uQKxs6NRAxgG6pxltrgBTgB5V8jh1BpbIYV85wYaVepJab%2B2u5HqYDLGtHQ8xkq1ZMJ7rfECbIrwkkQtrqEvwMHvIo2NdK%2BlFgElmn4p%2FZeGK48lfaBPKiCSR2BFbSPUiEKW8kGbalXN7DAWIB%2FFDnU5WrM73x2U5YmaFsijSt3ZCeE8OZ6Y0pT8IINkWZUAmPyiC0nfZGFZwrwMGTNP4SsfKBc0D%2FDnNSbxGaDFhGzqmM1nYZd8wHP8mmZiakLMgWDUE7lCt72I7CVD4gBACIJdaKKtH7Z7qmCR2IFlT24CZ9o0WJwYwEB7OzLuJF%2BjULtT4mPlB51a9PNoNc67KgaYlFDmVFqpSjMU0U08W6tFpJu4F4%2FTDFaZtdCohbL5rA8DnlYZibPmfwntbfHsTq0oVYZM8aY%2BwUXaopRATvkBlP%2FH99xPAPEBdjDKmLg34MNcGdqsusp%2FVvxJL9iC9ivf0kjJSbokuPITIJCXXkEztsDTXkTIqtJcF%2FVbKbU10KH6lokYbUbzrm10aor4M4zTQ%2BvEqmMAzQ5pLC3vFTIUWVWFLkyEXAMK%2FQ8LwGOqUBxE264uBRUsUtqnPLys36o6ymmJZp4oMw%2FftVmBcInScVweBXaXLxnYB4LGC3T3LvkyXZ8pn6AcXfphUjI%2Fm1zV09W4RZbq1saPprqvN9HrFFfbiMmyO%2BU%2BktET4bCA36%2FEPw7AX3vL63yBRcygl1ujretjqhTPEymur%2BQKLa%2B%2BtBzMbaDDDVbcIaN0bGRBY%2Fg1tq%2Ff2C8SPt1ZsJAO4TLFCfj3T6&X-Amz-Signature=b2764635cd747a6bf2f6ce27d836b83dd18e407de4f93d8ea9a0aaefa8235f02&X-Amz-SignedHeaders=host&x-id=GetObject)
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