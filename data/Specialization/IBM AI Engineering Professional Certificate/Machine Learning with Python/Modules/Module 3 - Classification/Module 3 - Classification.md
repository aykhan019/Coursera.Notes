

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YRHMCOL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIGODMpmTtHw2WdAD6xwJfybJWKjKqadz%2FIEhInghdx3zAiA4W2cqzKKWBEChGD6JtXX7UUm27Y%2FucAO2YB3JZyDDciqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyA%2FvDM2aiHcfum6eKtwDOhXULYkWu%2FiRiCdv1ZKjeD9sMz0CmIFjvvLv6ATx6zi7mvqTu0CvH64Wan4B3M3KBZlmZeWj5iOV6824zvKJqh8wa5j7etJGP5xjAMRvOwlcBTFX6K0Mez4uA58uDJP%2FrHMJ7IlFRkzOH6E%2FjCoPCSR%2B2l8zwvFkyYt4Kq18ojY%2Fv%2FSU4Idd0U0z4YFwODKrtHDt4HnM0WipW3CYNyXQRtx51XBjHu09r0isIP5RFxOvbhSL1zaWQYltFUYs6%2FGCFOqDZ5nL2wgbPws92bgYzwPxxOBVvxpUiR%2BMJg2bmtJ3CsrbT9mW%2F5liqjjDDaz33R3VVByhnyGCpEgtk7rSBlcrbex8CXPvfCQBhRoWJSxJMLKqbfAIZADQ3yZfTpzdy7wBwdQZweOQuFXlCEO8l4uNXRwrM7yWVRzIXqzPTXBhXLt%2BpNvENSfe3CO8Q6KUaFfW%2B52oMae0EAk3SA5cyqHFXxUPF34bAP%2F2A8Lg22aaYSt%2BH8MK2cFz%2BmxpU9ysywCh8YToGj%2BMHF1AmtkIJNVvsvC6XLVXa7tnhVQJWLcu1AqtFMEeraQbgm93V4FuiqVAgHFCfVFugLNruCaZ8GaEcvxRQ3OTgBwY%2FitNf1qDk0EBH5Kncknmjb4w0p%2FmvAY6pgFZjSiD5L%2FmFzH9S2YtPuIeMz5d%2Bg9dOwsUEuJUJDjdVARqNgGPHg3zSb8%2F6PCEwzGb1T%2B0f6aIXGeSJFU0mOxiFQhVuHwKACMrD%2Bjevyx32FQqEisJGZIWesfPlvwhQlLl5mHBrFYDVCFf1I827rC7yKJPxOY%2BfF%2FXc%2FS2othYjU%2B2wOdla5uvjjs7gZBsMRqExjmvpcbXFf9bqEonTBO9NWogRWgp&X-Amz-Signature=f5391c9a355aa0d7fa2bb62c3ff82029e3fad8b61f965e1e027bcad643fea5db&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YRHMCOL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIGODMpmTtHw2WdAD6xwJfybJWKjKqadz%2FIEhInghdx3zAiA4W2cqzKKWBEChGD6JtXX7UUm27Y%2FucAO2YB3JZyDDciqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyA%2FvDM2aiHcfum6eKtwDOhXULYkWu%2FiRiCdv1ZKjeD9sMz0CmIFjvvLv6ATx6zi7mvqTu0CvH64Wan4B3M3KBZlmZeWj5iOV6824zvKJqh8wa5j7etJGP5xjAMRvOwlcBTFX6K0Mez4uA58uDJP%2FrHMJ7IlFRkzOH6E%2FjCoPCSR%2B2l8zwvFkyYt4Kq18ojY%2Fv%2FSU4Idd0U0z4YFwODKrtHDt4HnM0WipW3CYNyXQRtx51XBjHu09r0isIP5RFxOvbhSL1zaWQYltFUYs6%2FGCFOqDZ5nL2wgbPws92bgYzwPxxOBVvxpUiR%2BMJg2bmtJ3CsrbT9mW%2F5liqjjDDaz33R3VVByhnyGCpEgtk7rSBlcrbex8CXPvfCQBhRoWJSxJMLKqbfAIZADQ3yZfTpzdy7wBwdQZweOQuFXlCEO8l4uNXRwrM7yWVRzIXqzPTXBhXLt%2BpNvENSfe3CO8Q6KUaFfW%2B52oMae0EAk3SA5cyqHFXxUPF34bAP%2F2A8Lg22aaYSt%2BH8MK2cFz%2BmxpU9ysywCh8YToGj%2BMHF1AmtkIJNVvsvC6XLVXa7tnhVQJWLcu1AqtFMEeraQbgm93V4FuiqVAgHFCfVFugLNruCaZ8GaEcvxRQ3OTgBwY%2FitNf1qDk0EBH5Kncknmjb4w0p%2FmvAY6pgFZjSiD5L%2FmFzH9S2YtPuIeMz5d%2Bg9dOwsUEuJUJDjdVARqNgGPHg3zSb8%2F6PCEwzGb1T%2B0f6aIXGeSJFU0mOxiFQhVuHwKACMrD%2Bjevyx32FQqEisJGZIWesfPlvwhQlLl5mHBrFYDVCFf1I827rC7yKJPxOY%2BfF%2FXc%2FS2othYjU%2B2wOdla5uvjjs7gZBsMRqExjmvpcbXFf9bqEonTBO9NWogRWgp&X-Amz-Signature=81bd156dc80d4aecbe1eca34e7536c2e7215484f2367c2febe4415bcc6af54fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YRHMCOL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIGODMpmTtHw2WdAD6xwJfybJWKjKqadz%2FIEhInghdx3zAiA4W2cqzKKWBEChGD6JtXX7UUm27Y%2FucAO2YB3JZyDDciqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyA%2FvDM2aiHcfum6eKtwDOhXULYkWu%2FiRiCdv1ZKjeD9sMz0CmIFjvvLv6ATx6zi7mvqTu0CvH64Wan4B3M3KBZlmZeWj5iOV6824zvKJqh8wa5j7etJGP5xjAMRvOwlcBTFX6K0Mez4uA58uDJP%2FrHMJ7IlFRkzOH6E%2FjCoPCSR%2B2l8zwvFkyYt4Kq18ojY%2Fv%2FSU4Idd0U0z4YFwODKrtHDt4HnM0WipW3CYNyXQRtx51XBjHu09r0isIP5RFxOvbhSL1zaWQYltFUYs6%2FGCFOqDZ5nL2wgbPws92bgYzwPxxOBVvxpUiR%2BMJg2bmtJ3CsrbT9mW%2F5liqjjDDaz33R3VVByhnyGCpEgtk7rSBlcrbex8CXPvfCQBhRoWJSxJMLKqbfAIZADQ3yZfTpzdy7wBwdQZweOQuFXlCEO8l4uNXRwrM7yWVRzIXqzPTXBhXLt%2BpNvENSfe3CO8Q6KUaFfW%2B52oMae0EAk3SA5cyqHFXxUPF34bAP%2F2A8Lg22aaYSt%2BH8MK2cFz%2BmxpU9ysywCh8YToGj%2BMHF1AmtkIJNVvsvC6XLVXa7tnhVQJWLcu1AqtFMEeraQbgm93V4FuiqVAgHFCfVFugLNruCaZ8GaEcvxRQ3OTgBwY%2FitNf1qDk0EBH5Kncknmjb4w0p%2FmvAY6pgFZjSiD5L%2FmFzH9S2YtPuIeMz5d%2Bg9dOwsUEuJUJDjdVARqNgGPHg3zSb8%2F6PCEwzGb1T%2B0f6aIXGeSJFU0mOxiFQhVuHwKACMrD%2Bjevyx32FQqEisJGZIWesfPlvwhQlLl5mHBrFYDVCFf1I827rC7yKJPxOY%2BfF%2FXc%2FS2othYjU%2B2wOdla5uvjjs7gZBsMRqExjmvpcbXFf9bqEonTBO9NWogRWgp&X-Amz-Signature=81303edd215c30a8b97283e140d709019e30e38f5fd8494401190f5a6e063914&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJU674EI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCSc7UxC1WBtBTpcly26VO5UiP3OPWGrnc%2FOoCdYEaLEAIgSubGmb5UGc3qwVcVF1IRXEfiVZZMv8hEVp26VDbrJcAqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIrQ1De%2BKolwiFk7lircA1FHRr%2Bk16SytkkAn5LrAGKkjzjSVH0%2B%2Frww84PO94qqdnxPTD2Y%2B5j9E8yduJ8%2F5f%2FQd3%2BBYemWKAke9PQDQq3NZRj75RiPjLc3Kbh4EBphsZAsBZxfHPg70Gbwea1odrWb1B31sieDOJ%2BLRbnbe4exddc%2BtWe4mjQs6BQlR%2F7j7uUti05NodfzSPZN2mbdx4%2Fm7tAP5moCZL1DcchiJmpYCMIAiFKL1GCmyxrnnrMOzQBIY6GcM6z%2BJ49s7hzkaCRqUE1kNLdst2PcG3J9xcTR7YPIrFoc0avTwCnb2T8jaorKH5fQ8DT6GiLeMeMkl3NrPVcEFF3XWUQf7qUF%2BLQ5%2FhmhukqJ4j3WsfOklOcWbSomQyeDc6CzU0fP5n1OJrBU9qBBcsjYpxnWHKuED4ix7vx1ovGIDNOrmaZHviLQyJNxDYxFAjELJ53F9f2TeXwSZVbHAcTYSUcC1Cwb7svhau864gtFHiIuV41cdBf5u7ryBqiUFcQFov0iAZpT0hVAbS4uiJZ%2FVdB1%2BonFUOOMrGPU4nwvLj6eh6XItLX%2BuRoq6K1HxrHtkls3NHuEjAOA66xVt%2Fj0B0jAxvHHUL48CUEyyg1CLAGb%2Fly6H9lOaqgD6%2BZ7M1awmleqMIKg5rwGOqUB9AWxgltCZqzUnUnYZ2%2BaWO3XMEBxkxCWIFnG7bXk%2BWRSMAqkKhsYQC09L1xvCXpT57TTBLmz7rfOWeYZsnJJfat%2BHXmBMACDUYOoOVDJRA%2B3u%2FX4aUTQpY4Qe%2BoG3yPfEDCblBgln%2FX73q5A65L%2Ba5VPdROhPrlmOubuTTx4rV6MnExZmtV1I8Kyru4RVjCmaJmPFZe7HCQpY2v%2F6Rizbq6m9dbD&X-Amz-Signature=54cb1791b10ef4f28b7b2ba197e62eafc812baefcc4672bcba525bc23ab54f13&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJU674EI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCSc7UxC1WBtBTpcly26VO5UiP3OPWGrnc%2FOoCdYEaLEAIgSubGmb5UGc3qwVcVF1IRXEfiVZZMv8hEVp26VDbrJcAqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIrQ1De%2BKolwiFk7lircA1FHRr%2Bk16SytkkAn5LrAGKkjzjSVH0%2B%2Frww84PO94qqdnxPTD2Y%2B5j9E8yduJ8%2F5f%2FQd3%2BBYemWKAke9PQDQq3NZRj75RiPjLc3Kbh4EBphsZAsBZxfHPg70Gbwea1odrWb1B31sieDOJ%2BLRbnbe4exddc%2BtWe4mjQs6BQlR%2F7j7uUti05NodfzSPZN2mbdx4%2Fm7tAP5moCZL1DcchiJmpYCMIAiFKL1GCmyxrnnrMOzQBIY6GcM6z%2BJ49s7hzkaCRqUE1kNLdst2PcG3J9xcTR7YPIrFoc0avTwCnb2T8jaorKH5fQ8DT6GiLeMeMkl3NrPVcEFF3XWUQf7qUF%2BLQ5%2FhmhukqJ4j3WsfOklOcWbSomQyeDc6CzU0fP5n1OJrBU9qBBcsjYpxnWHKuED4ix7vx1ovGIDNOrmaZHviLQyJNxDYxFAjELJ53F9f2TeXwSZVbHAcTYSUcC1Cwb7svhau864gtFHiIuV41cdBf5u7ryBqiUFcQFov0iAZpT0hVAbS4uiJZ%2FVdB1%2BonFUOOMrGPU4nwvLj6eh6XItLX%2BuRoq6K1HxrHtkls3NHuEjAOA66xVt%2Fj0B0jAxvHHUL48CUEyyg1CLAGb%2Fly6H9lOaqgD6%2BZ7M1awmleqMIKg5rwGOqUB9AWxgltCZqzUnUnYZ2%2BaWO3XMEBxkxCWIFnG7bXk%2BWRSMAqkKhsYQC09L1xvCXpT57TTBLmz7rfOWeYZsnJJfat%2BHXmBMACDUYOoOVDJRA%2B3u%2FX4aUTQpY4Qe%2BoG3yPfEDCblBgln%2FX73q5A65L%2Ba5VPdROhPrlmOubuTTx4rV6MnExZmtV1I8Kyru4RVjCmaJmPFZe7HCQpY2v%2F6Rizbq6m9dbD&X-Amz-Signature=e92d7e28df6af4e03e7508d6dd917341ff95189bec02081366c080a4715a8783&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YRHMCOL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIGODMpmTtHw2WdAD6xwJfybJWKjKqadz%2FIEhInghdx3zAiA4W2cqzKKWBEChGD6JtXX7UUm27Y%2FucAO2YB3JZyDDciqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyA%2FvDM2aiHcfum6eKtwDOhXULYkWu%2FiRiCdv1ZKjeD9sMz0CmIFjvvLv6ATx6zi7mvqTu0CvH64Wan4B3M3KBZlmZeWj5iOV6824zvKJqh8wa5j7etJGP5xjAMRvOwlcBTFX6K0Mez4uA58uDJP%2FrHMJ7IlFRkzOH6E%2FjCoPCSR%2B2l8zwvFkyYt4Kq18ojY%2Fv%2FSU4Idd0U0z4YFwODKrtHDt4HnM0WipW3CYNyXQRtx51XBjHu09r0isIP5RFxOvbhSL1zaWQYltFUYs6%2FGCFOqDZ5nL2wgbPws92bgYzwPxxOBVvxpUiR%2BMJg2bmtJ3CsrbT9mW%2F5liqjjDDaz33R3VVByhnyGCpEgtk7rSBlcrbex8CXPvfCQBhRoWJSxJMLKqbfAIZADQ3yZfTpzdy7wBwdQZweOQuFXlCEO8l4uNXRwrM7yWVRzIXqzPTXBhXLt%2BpNvENSfe3CO8Q6KUaFfW%2B52oMae0EAk3SA5cyqHFXxUPF34bAP%2F2A8Lg22aaYSt%2BH8MK2cFz%2BmxpU9ysywCh8YToGj%2BMHF1AmtkIJNVvsvC6XLVXa7tnhVQJWLcu1AqtFMEeraQbgm93V4FuiqVAgHFCfVFugLNruCaZ8GaEcvxRQ3OTgBwY%2FitNf1qDk0EBH5Kncknmjb4w0p%2FmvAY6pgFZjSiD5L%2FmFzH9S2YtPuIeMz5d%2Bg9dOwsUEuJUJDjdVARqNgGPHg3zSb8%2F6PCEwzGb1T%2B0f6aIXGeSJFU0mOxiFQhVuHwKACMrD%2Bjevyx32FQqEisJGZIWesfPlvwhQlLl5mHBrFYDVCFf1I827rC7yKJPxOY%2BfF%2FXc%2FS2othYjU%2B2wOdla5uvjjs7gZBsMRqExjmvpcbXFf9bqEonTBO9NWogRWgp&X-Amz-Signature=af924ef5c636a8e2ae6340a842916aa2c0737348975848cbadc4d80e73bd7a0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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