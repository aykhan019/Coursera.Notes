

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TP5WOMRL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTzKcKXkry7LRA%2FqahRwK4ooK6dWzpRySxweln0v99mgIgECiZjR5ff0FLl5qGKg6AaD69HmgVicp8DRET%2FvuR9vIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA4qxekKUIv3UftbRCrcA7L6L4CYiYK2yWIMtFmihsT2sHd5pHW5N9rEybt1%2FyHytLaD7R6rKW%2BZgtzt7RKvcegswmVt6k2JyVCIbNtfD7q1TuhExbc6bAjqPdvu2YQXIICTORsYx77iZ75IPEwdiilzFvTh%2BtXHKexkEVFnrqjjHjDvMhIQPOuUxObuAGiI7t0ga8WbyDMuPexNRpxShfs4xfVO2m06HT4Y7Dj%2FktFREL%2Bn7MQrdjjhqquK0YlpnMnqTExQ%2FxMXwajpwbl6m9lmCkbVv2pLPlH94wr2o3daBHauTUVoUjMni7exlpLqg8Dz3s4YVElcedYoLv2jWywGcH6QYZaApaNo%2BK8gQh48%2B858gWldVo8%2FSYtUiqG5oEhGNfEAANACdWtZ1rGbUl3vnSYj3cm9bbFPYPPr4PEwZwuxI4q0mnezbipqO%2Bhjf0vS%2FmKzaUHIYb3QwPevJQ2UZjuusEsyLAoUKlEnZ9ZGrDr%2By2LTjfEmIlZA%2F1j6sYYbmehzmAFf5hWEFogEkf4J%2FFmQRJ%2BEX0Hh4e4fSlHKvSVgc06TqP5B0asCtrjS6sQmbL1kqgDN7K28c%2F9JwU0yVAKT7HNmaxTCoWhl%2FQ2QjFlcSWhBiD5IT9Mq%2Bi0CWYlgAbTG57ftUpjRMJu%2B%2FbwGOqUBlBIh4nOP%2F1CLxaDzgs%2FL4FDIBXqgWSjYN%2Fw4RqI9quJQYJcX8JYPTAx1fMG4aVqC%2BWdgjkJM1oMqnl3%2BTdSvR1Xs78M3PA5tTZnoLQox4vOD71DDdyhBqxIY6qpYKROLMbJo02O8sk9YOyY9Qgjjg1LXoYDoztHufuKZSsAfhKxCqFlwki9S0Bhl1TOGr7gBGGzHlZPBUR9NNaVp%2BMYA%2BBwUL3T1&X-Amz-Signature=9555d7dc8e221edcc4c53533103f551efa12dda32825aa2655225b2e52377ab4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TP5WOMRL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTzKcKXkry7LRA%2FqahRwK4ooK6dWzpRySxweln0v99mgIgECiZjR5ff0FLl5qGKg6AaD69HmgVicp8DRET%2FvuR9vIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA4qxekKUIv3UftbRCrcA7L6L4CYiYK2yWIMtFmihsT2sHd5pHW5N9rEybt1%2FyHytLaD7R6rKW%2BZgtzt7RKvcegswmVt6k2JyVCIbNtfD7q1TuhExbc6bAjqPdvu2YQXIICTORsYx77iZ75IPEwdiilzFvTh%2BtXHKexkEVFnrqjjHjDvMhIQPOuUxObuAGiI7t0ga8WbyDMuPexNRpxShfs4xfVO2m06HT4Y7Dj%2FktFREL%2Bn7MQrdjjhqquK0YlpnMnqTExQ%2FxMXwajpwbl6m9lmCkbVv2pLPlH94wr2o3daBHauTUVoUjMni7exlpLqg8Dz3s4YVElcedYoLv2jWywGcH6QYZaApaNo%2BK8gQh48%2B858gWldVo8%2FSYtUiqG5oEhGNfEAANACdWtZ1rGbUl3vnSYj3cm9bbFPYPPr4PEwZwuxI4q0mnezbipqO%2Bhjf0vS%2FmKzaUHIYb3QwPevJQ2UZjuusEsyLAoUKlEnZ9ZGrDr%2By2LTjfEmIlZA%2F1j6sYYbmehzmAFf5hWEFogEkf4J%2FFmQRJ%2BEX0Hh4e4fSlHKvSVgc06TqP5B0asCtrjS6sQmbL1kqgDN7K28c%2F9JwU0yVAKT7HNmaxTCoWhl%2FQ2QjFlcSWhBiD5IT9Mq%2Bi0CWYlgAbTG57ftUpjRMJu%2B%2FbwGOqUBlBIh4nOP%2F1CLxaDzgs%2FL4FDIBXqgWSjYN%2Fw4RqI9quJQYJcX8JYPTAx1fMG4aVqC%2BWdgjkJM1oMqnl3%2BTdSvR1Xs78M3PA5tTZnoLQox4vOD71DDdyhBqxIY6qpYKROLMbJo02O8sk9YOyY9Qgjjg1LXoYDoztHufuKZSsAfhKxCqFlwki9S0Bhl1TOGr7gBGGzHlZPBUR9NNaVp%2BMYA%2BBwUL3T1&X-Amz-Signature=285858674348ac15d65633a63622b2fabe6dfa1ecdfe7cdf2b9e6dd97005f80c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TP5WOMRL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTzKcKXkry7LRA%2FqahRwK4ooK6dWzpRySxweln0v99mgIgECiZjR5ff0FLl5qGKg6AaD69HmgVicp8DRET%2FvuR9vIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA4qxekKUIv3UftbRCrcA7L6L4CYiYK2yWIMtFmihsT2sHd5pHW5N9rEybt1%2FyHytLaD7R6rKW%2BZgtzt7RKvcegswmVt6k2JyVCIbNtfD7q1TuhExbc6bAjqPdvu2YQXIICTORsYx77iZ75IPEwdiilzFvTh%2BtXHKexkEVFnrqjjHjDvMhIQPOuUxObuAGiI7t0ga8WbyDMuPexNRpxShfs4xfVO2m06HT4Y7Dj%2FktFREL%2Bn7MQrdjjhqquK0YlpnMnqTExQ%2FxMXwajpwbl6m9lmCkbVv2pLPlH94wr2o3daBHauTUVoUjMni7exlpLqg8Dz3s4YVElcedYoLv2jWywGcH6QYZaApaNo%2BK8gQh48%2B858gWldVo8%2FSYtUiqG5oEhGNfEAANACdWtZ1rGbUl3vnSYj3cm9bbFPYPPr4PEwZwuxI4q0mnezbipqO%2Bhjf0vS%2FmKzaUHIYb3QwPevJQ2UZjuusEsyLAoUKlEnZ9ZGrDr%2By2LTjfEmIlZA%2F1j6sYYbmehzmAFf5hWEFogEkf4J%2FFmQRJ%2BEX0Hh4e4fSlHKvSVgc06TqP5B0asCtrjS6sQmbL1kqgDN7K28c%2F9JwU0yVAKT7HNmaxTCoWhl%2FQ2QjFlcSWhBiD5IT9Mq%2Bi0CWYlgAbTG57ftUpjRMJu%2B%2FbwGOqUBlBIh4nOP%2F1CLxaDzgs%2FL4FDIBXqgWSjYN%2Fw4RqI9quJQYJcX8JYPTAx1fMG4aVqC%2BWdgjkJM1oMqnl3%2BTdSvR1Xs78M3PA5tTZnoLQox4vOD71DDdyhBqxIY6qpYKROLMbJo02O8sk9YOyY9Qgjjg1LXoYDoztHufuKZSsAfhKxCqFlwki9S0Bhl1TOGr7gBGGzHlZPBUR9NNaVp%2BMYA%2BBwUL3T1&X-Amz-Signature=2281a1b8173e04ca4ff06edd3de1e3e95c895858d29a4ba158b1c88a6cdd6e02&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YLQ2UJ6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1qj5Mwd1TZaKQPNyDNAdgCCH7mopNfOFrqO%2B%2FwfzgsQIgRsncekHDQhwD%2BKhu2bOYu8bZsufk8I5sv5KNI58XzeoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FjhlyI5o%2B4Kcy18SrcA1B0N6hthb%2BNnp2tyejjWzTvwzeURVmRmaJY1gsSnDF7%2FWSuoLispeRhf3OW4wvp5N0j6R5F0zzmFgsjvMq02U5CUpuob7Wwl4ycI30He8sJ3f83RIqjjvPnzzk64zXOHO1NYVI0v1FDcC8nxyQcfu6ZcDaDFlP9PRY9z5bV2JsBK9P3oax%2FZ3n2I8XL8yXdzQ1kT8YKPewdkJj%2Bi%2Fkm928%2FFN216pONadAfLMDMfXcCSN4cCI0jaW7UcmPZoQj4YWixSF%2BOFSc5nyFbZKLm2VnNTHpSHM4xqWwE4YeJ8YTHjQjhuMo4cFQV7REARYBApLJA229I5pFcHa1RKs12XLdXzKOr%2FF1etpzfqIXHfqkShOal20aUVhDqw7SfQ218dRJm9ZHQpEWvR01bfTvy3idMRtCBPl4DxGYDcpvo0bXVcPjv04UZGedXGXaW3X4Ox6J8rnL5LoamUasKpsUz8yMGjpTcNxTNr88LlV5e0gwIaUzLu%2Fmpdj%2BUuEOU1%2BRpUCT5Zw7OwoBEY67G9cTJOKDGSiDmhIHe4%2F%2BRtQ3bh6VvNgjMdQB1%2BXeWGBQfDWHmZGMQLW7KvNJKMhYuDkRv%2BIPLWjjgOrNDygHDmfdlMJMc4iLcRl2BGGo37IqNMM69%2FbwGOqUBQAzoN91%2B0lmegqTM%2BU%2BzAopON%2FKBG1xjgjqA6bqQe%2FsWC%2Bxwp6GqJQiKdn%2BXrtkZNumhGw8IVpnzhCmTQgVArvtlW3vABGt68Z%2B%2F3nIP3zqFutPMAw8%2BUu4LshUhvbbAyql9L0KZs95Ko5zUEJUw9al9yCDV0rLt80HOexv1ORUW0wFmANsYUw4EmE5bjFlch2wrCjXYKg19PMuz7QUZ%2FwBk3%2FxS&X-Amz-Signature=6d2cb60c887cd29494ee3d268c6b543e70735ec89807ac96c1321fb44970edc5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YLQ2UJ6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1qj5Mwd1TZaKQPNyDNAdgCCH7mopNfOFrqO%2B%2FwfzgsQIgRsncekHDQhwD%2BKhu2bOYu8bZsufk8I5sv5KNI58XzeoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2FjhlyI5o%2B4Kcy18SrcA1B0N6hthb%2BNnp2tyejjWzTvwzeURVmRmaJY1gsSnDF7%2FWSuoLispeRhf3OW4wvp5N0j6R5F0zzmFgsjvMq02U5CUpuob7Wwl4ycI30He8sJ3f83RIqjjvPnzzk64zXOHO1NYVI0v1FDcC8nxyQcfu6ZcDaDFlP9PRY9z5bV2JsBK9P3oax%2FZ3n2I8XL8yXdzQ1kT8YKPewdkJj%2Bi%2Fkm928%2FFN216pONadAfLMDMfXcCSN4cCI0jaW7UcmPZoQj4YWixSF%2BOFSc5nyFbZKLm2VnNTHpSHM4xqWwE4YeJ8YTHjQjhuMo4cFQV7REARYBApLJA229I5pFcHa1RKs12XLdXzKOr%2FF1etpzfqIXHfqkShOal20aUVhDqw7SfQ218dRJm9ZHQpEWvR01bfTvy3idMRtCBPl4DxGYDcpvo0bXVcPjv04UZGedXGXaW3X4Ox6J8rnL5LoamUasKpsUz8yMGjpTcNxTNr88LlV5e0gwIaUzLu%2Fmpdj%2BUuEOU1%2BRpUCT5Zw7OwoBEY67G9cTJOKDGSiDmhIHe4%2F%2BRtQ3bh6VvNgjMdQB1%2BXeWGBQfDWHmZGMQLW7KvNJKMhYuDkRv%2BIPLWjjgOrNDygHDmfdlMJMc4iLcRl2BGGo37IqNMM69%2FbwGOqUBQAzoN91%2B0lmegqTM%2BU%2BzAopON%2FKBG1xjgjqA6bqQe%2FsWC%2Bxwp6GqJQiKdn%2BXrtkZNumhGw8IVpnzhCmTQgVArvtlW3vABGt68Z%2B%2F3nIP3zqFutPMAw8%2BUu4LshUhvbbAyql9L0KZs95Ko5zUEJUw9al9yCDV0rLt80HOexv1ORUW0wFmANsYUw4EmE5bjFlch2wrCjXYKg19PMuz7QUZ%2FwBk3%2FxS&X-Amz-Signature=e1dfb624b404ea47fce9d7d3903278067daf8de3a54b75a802c86710ff57f275&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TP5WOMRL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTzKcKXkry7LRA%2FqahRwK4ooK6dWzpRySxweln0v99mgIgECiZjR5ff0FLl5qGKg6AaD69HmgVicp8DRET%2FvuR9vIqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA4qxekKUIv3UftbRCrcA7L6L4CYiYK2yWIMtFmihsT2sHd5pHW5N9rEybt1%2FyHytLaD7R6rKW%2BZgtzt7RKvcegswmVt6k2JyVCIbNtfD7q1TuhExbc6bAjqPdvu2YQXIICTORsYx77iZ75IPEwdiilzFvTh%2BtXHKexkEVFnrqjjHjDvMhIQPOuUxObuAGiI7t0ga8WbyDMuPexNRpxShfs4xfVO2m06HT4Y7Dj%2FktFREL%2Bn7MQrdjjhqquK0YlpnMnqTExQ%2FxMXwajpwbl6m9lmCkbVv2pLPlH94wr2o3daBHauTUVoUjMni7exlpLqg8Dz3s4YVElcedYoLv2jWywGcH6QYZaApaNo%2BK8gQh48%2B858gWldVo8%2FSYtUiqG5oEhGNfEAANACdWtZ1rGbUl3vnSYj3cm9bbFPYPPr4PEwZwuxI4q0mnezbipqO%2Bhjf0vS%2FmKzaUHIYb3QwPevJQ2UZjuusEsyLAoUKlEnZ9ZGrDr%2By2LTjfEmIlZA%2F1j6sYYbmehzmAFf5hWEFogEkf4J%2FFmQRJ%2BEX0Hh4e4fSlHKvSVgc06TqP5B0asCtrjS6sQmbL1kqgDN7K28c%2F9JwU0yVAKT7HNmaxTCoWhl%2FQ2QjFlcSWhBiD5IT9Mq%2Bi0CWYlgAbTG57ftUpjRMJu%2B%2FbwGOqUBlBIh4nOP%2F1CLxaDzgs%2FL4FDIBXqgWSjYN%2Fw4RqI9quJQYJcX8JYPTAx1fMG4aVqC%2BWdgjkJM1oMqnl3%2BTdSvR1Xs78M3PA5tTZnoLQox4vOD71DDdyhBqxIY6qpYKROLMbJo02O8sk9YOyY9Qgjjg1LXoYDoztHufuKZSsAfhKxCqFlwki9S0Bhl1TOGr7gBGGzHlZPBUR9NNaVp%2BMYA%2BBwUL3T1&X-Amz-Signature=d185de0b702c7ab61910d56e6bf860bdcd385c539b76550dff3bff1790889eba&X-Amz-SignedHeaders=host&x-id=GetObject)
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