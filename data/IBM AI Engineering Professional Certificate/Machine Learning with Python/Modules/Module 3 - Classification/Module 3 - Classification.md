

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKFPFOXU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIGd4nkeEbjB31cTtggseGd7OxxH3QDJTUppeMOmuo41vAiEA8J3hyCvmLheQk4VKtBxufHVHqdnJ51XHTvQFEBbtqQcq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDHD1%2FCk8jAMwqNyoGircA3sN4%2FEIwRubxfnICJU0tifaBJs26zWrRyj1BwTh46pmn6w6qUrABmkeCWBfsJPurZJntkcaaxXHuekHGUuxqEWogFDp5euVeeedWb0VGNssVoTAFISobzN8Va24hB8i5fmK7hs5dYOeCVX8gfEBznrvg%2B423GFDvIGr2OCBCVhUl3r1Z1Ub3zzVO%2BbtwyPOq6ZanH6a7B1Ln2u94EWcM0sKcahy8oYKRhDhs0P7tw6U4%2FOtWoggVvuE7OQv5T0IvVBhzXe%2BYjH%2FrPjOTPtqn7T85J2o9bjJFb8GKHqAl%2BOMzHS6pbXVHJP%2B%2Byu9vVi8SrQYkerkpLpDqXzo3WHh2B8dZTzr4JEBXcG73dGkoZvgiX6hNYEUu72fc%2FyIRGwVgJpF0MFYrzEXzkfnya3flNxvQVPA2A4f%2BpmVe0ZS1G0%2FJsc5iz6jyV6KBQJe0NtWX4ZPgb7GK4Z8bOmFj0fuDl0LIql%2F%2FD2qLu6EQ09jBGQFCh00vqEU9fgnmJ5NGbVqDrjCvTuDmBUWhYRciFmpx7YxH7MXxTwbf4mfgd7f0zISww3e7tsjKsUGHMJH7FQ45j8fyj2zEKFA00wVwbnMchh0h29LT9gUR79oFRZxsYi6KFvYl2VuVMVwgJZaMITwl70GOqUBa4N7MmW9AeNC85h%2FHWzruN4Fxtx28PgI9RQJS5Gwbn1eIuh9VTVleo8umK43IS9NjO76IXAVeIaA9DO87jrIxMGgnUwtXWvBFSM4NI04NnIaCbfq9K2bI2oNIBjoL%2FeH%2F6FfKjbT1Na3k6WEBtx1A%2FAwMK7gsm86LYxpGCqz6tWLaVG0H73qF0Ls6klmjLH8BGoBrPyBUnL%2F%2BWTuPeDiUxTWEzSt&X-Amz-Signature=3eaee8d4e61e33d51e1947048c36cbc910c8b4c01b71298454477a80f40bbe3e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKFPFOXU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIGd4nkeEbjB31cTtggseGd7OxxH3QDJTUppeMOmuo41vAiEA8J3hyCvmLheQk4VKtBxufHVHqdnJ51XHTvQFEBbtqQcq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDHD1%2FCk8jAMwqNyoGircA3sN4%2FEIwRubxfnICJU0tifaBJs26zWrRyj1BwTh46pmn6w6qUrABmkeCWBfsJPurZJntkcaaxXHuekHGUuxqEWogFDp5euVeeedWb0VGNssVoTAFISobzN8Va24hB8i5fmK7hs5dYOeCVX8gfEBznrvg%2B423GFDvIGr2OCBCVhUl3r1Z1Ub3zzVO%2BbtwyPOq6ZanH6a7B1Ln2u94EWcM0sKcahy8oYKRhDhs0P7tw6U4%2FOtWoggVvuE7OQv5T0IvVBhzXe%2BYjH%2FrPjOTPtqn7T85J2o9bjJFb8GKHqAl%2BOMzHS6pbXVHJP%2B%2Byu9vVi8SrQYkerkpLpDqXzo3WHh2B8dZTzr4JEBXcG73dGkoZvgiX6hNYEUu72fc%2FyIRGwVgJpF0MFYrzEXzkfnya3flNxvQVPA2A4f%2BpmVe0ZS1G0%2FJsc5iz6jyV6KBQJe0NtWX4ZPgb7GK4Z8bOmFj0fuDl0LIql%2F%2FD2qLu6EQ09jBGQFCh00vqEU9fgnmJ5NGbVqDrjCvTuDmBUWhYRciFmpx7YxH7MXxTwbf4mfgd7f0zISww3e7tsjKsUGHMJH7FQ45j8fyj2zEKFA00wVwbnMchh0h29LT9gUR79oFRZxsYi6KFvYl2VuVMVwgJZaMITwl70GOqUBa4N7MmW9AeNC85h%2FHWzruN4Fxtx28PgI9RQJS5Gwbn1eIuh9VTVleo8umK43IS9NjO76IXAVeIaA9DO87jrIxMGgnUwtXWvBFSM4NI04NnIaCbfq9K2bI2oNIBjoL%2FeH%2F6FfKjbT1Na3k6WEBtx1A%2FAwMK7gsm86LYxpGCqz6tWLaVG0H73qF0Ls6klmjLH8BGoBrPyBUnL%2F%2BWTuPeDiUxTWEzSt&X-Amz-Signature=c238b7c6d0437c4d26ec5a160ece82cb65e69aae93de2b0dcab86fed2c55f6f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKFPFOXU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIGd4nkeEbjB31cTtggseGd7OxxH3QDJTUppeMOmuo41vAiEA8J3hyCvmLheQk4VKtBxufHVHqdnJ51XHTvQFEBbtqQcq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDHD1%2FCk8jAMwqNyoGircA3sN4%2FEIwRubxfnICJU0tifaBJs26zWrRyj1BwTh46pmn6w6qUrABmkeCWBfsJPurZJntkcaaxXHuekHGUuxqEWogFDp5euVeeedWb0VGNssVoTAFISobzN8Va24hB8i5fmK7hs5dYOeCVX8gfEBznrvg%2B423GFDvIGr2OCBCVhUl3r1Z1Ub3zzVO%2BbtwyPOq6ZanH6a7B1Ln2u94EWcM0sKcahy8oYKRhDhs0P7tw6U4%2FOtWoggVvuE7OQv5T0IvVBhzXe%2BYjH%2FrPjOTPtqn7T85J2o9bjJFb8GKHqAl%2BOMzHS6pbXVHJP%2B%2Byu9vVi8SrQYkerkpLpDqXzo3WHh2B8dZTzr4JEBXcG73dGkoZvgiX6hNYEUu72fc%2FyIRGwVgJpF0MFYrzEXzkfnya3flNxvQVPA2A4f%2BpmVe0ZS1G0%2FJsc5iz6jyV6KBQJe0NtWX4ZPgb7GK4Z8bOmFj0fuDl0LIql%2F%2FD2qLu6EQ09jBGQFCh00vqEU9fgnmJ5NGbVqDrjCvTuDmBUWhYRciFmpx7YxH7MXxTwbf4mfgd7f0zISww3e7tsjKsUGHMJH7FQ45j8fyj2zEKFA00wVwbnMchh0h29LT9gUR79oFRZxsYi6KFvYl2VuVMVwgJZaMITwl70GOqUBa4N7MmW9AeNC85h%2FHWzruN4Fxtx28PgI9RQJS5Gwbn1eIuh9VTVleo8umK43IS9NjO76IXAVeIaA9DO87jrIxMGgnUwtXWvBFSM4NI04NnIaCbfq9K2bI2oNIBjoL%2FeH%2F6FfKjbT1Na3k6WEBtx1A%2FAwMK7gsm86LYxpGCqz6tWLaVG0H73qF0Ls6klmjLH8BGoBrPyBUnL%2F%2BWTuPeDiUxTWEzSt&X-Amz-Signature=8c02501fd6e88684ec2ad1f0f834e9bbb8f67281677f1e5f4333f48c237cb1b7&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCXKBGD3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQCptYdx1CukUqywdTY8%2FDWxL1MVb1mIIApqEw2a2y2kPQIgH3tOGTJOkEtQcQSiFPd8AQF6OO0fElrW0%2FWaWa7T9qYq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDJ84Ij%2BscDFXdekbISrcA6uSduXmCWoiB0um4iVedv7JOSzpKhyfS86bLRU1y9Jo60Rnd25QI1cdJg8jRVCQf30cL0pglbPaZPhpMEU3AaGMP%2FXzhDal%2BpRnTxl6EdRynkuPcHMabacsrhIqsQ3V22gLrzYvYA5SAlwG6OAE1Jqfc8l48BOhmvLFC2VkmtdBzRfIy8fq%2BSKY3lp7fjvGqcEs9gF3iGdxrxnGvF9WW67sWZ0GKZRi8DfbHHjhT4l0rJNbZ9Lh%2FPs3kbvCrBpgrBvCcaXYsRyHjE4krbNSw78eLiZjC7C8cm%2FVJ5TC8QB8e%2Bow55vKoKG0Sgkio75T0gyTRhrIW5zA41Yv7rEH1mMxBLxIDAwbR7Zy7mjfl%2FSefp6NaqMB6a2bK4OBld7wBOO%2FzG65fo93WUlHJPqpnNOMT%2Bfiei71VOIpRiKmZNx1l5eRNXeQulDbP4knFyXDoELryH1oFyaYiXna0aB7sfT6V%2FtEMnlrUQeuZdvirDzjQb7RvRB7rM5clcQabPl6%2FNRH9Nd1%2Bp2z63AzLJ8rJq0J%2BkUHklKBPPlgQiJHr4Jnx4MJnUk2dovI4ZTDTqmnmqyLdkpR6buO6%2Bvg712ukuPh43soqsFmjgU7atNQeSZOGgD%2F0cprQShB4UUCMIPwl70GOqUBybUUap%2BcxKFtmHmmPWktpq%2FH3aE7GCHOVpa2FCs1w07BkuALHkCvCLMgtBqNTeKMplNbgHQwR7yX07YXxZ6jqJrEhYafzdmNHekcX7iV0dmG8b4e5gu6UESCh0tlKtqT3Y%2BN6TiEyGxs01iFmdTGpsnN8IQ3%2FjeHMpE2oit0mevn8pgxnYuTCqQwhi8s7viDK2qkauwZ6MxuPV67Uplx%2FCfrcrs%2F&X-Amz-Signature=5acc839fb5b981e11732dded35f30d8909f2e0238eda18980ba9b31ed339b62e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCXKBGD3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQCptYdx1CukUqywdTY8%2FDWxL1MVb1mIIApqEw2a2y2kPQIgH3tOGTJOkEtQcQSiFPd8AQF6OO0fElrW0%2FWaWa7T9qYq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDJ84Ij%2BscDFXdekbISrcA6uSduXmCWoiB0um4iVedv7JOSzpKhyfS86bLRU1y9Jo60Rnd25QI1cdJg8jRVCQf30cL0pglbPaZPhpMEU3AaGMP%2FXzhDal%2BpRnTxl6EdRynkuPcHMabacsrhIqsQ3V22gLrzYvYA5SAlwG6OAE1Jqfc8l48BOhmvLFC2VkmtdBzRfIy8fq%2BSKY3lp7fjvGqcEs9gF3iGdxrxnGvF9WW67sWZ0GKZRi8DfbHHjhT4l0rJNbZ9Lh%2FPs3kbvCrBpgrBvCcaXYsRyHjE4krbNSw78eLiZjC7C8cm%2FVJ5TC8QB8e%2Bow55vKoKG0Sgkio75T0gyTRhrIW5zA41Yv7rEH1mMxBLxIDAwbR7Zy7mjfl%2FSefp6NaqMB6a2bK4OBld7wBOO%2FzG65fo93WUlHJPqpnNOMT%2Bfiei71VOIpRiKmZNx1l5eRNXeQulDbP4knFyXDoELryH1oFyaYiXna0aB7sfT6V%2FtEMnlrUQeuZdvirDzjQb7RvRB7rM5clcQabPl6%2FNRH9Nd1%2Bp2z63AzLJ8rJq0J%2BkUHklKBPPlgQiJHr4Jnx4MJnUk2dovI4ZTDTqmnmqyLdkpR6buO6%2Bvg712ukuPh43soqsFmjgU7atNQeSZOGgD%2F0cprQShB4UUCMIPwl70GOqUBybUUap%2BcxKFtmHmmPWktpq%2FH3aE7GCHOVpa2FCs1w07BkuALHkCvCLMgtBqNTeKMplNbgHQwR7yX07YXxZ6jqJrEhYafzdmNHekcX7iV0dmG8b4e5gu6UESCh0tlKtqT3Y%2BN6TiEyGxs01iFmdTGpsnN8IQ3%2FjeHMpE2oit0mevn8pgxnYuTCqQwhi8s7viDK2qkauwZ6MxuPV67Uplx%2FCfrcrs%2F&X-Amz-Signature=9133a611678358afb676ba9e2abbae065fff2b6a138c210888d2704bf82ab3fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKFPFOXU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIGd4nkeEbjB31cTtggseGd7OxxH3QDJTUppeMOmuo41vAiEA8J3hyCvmLheQk4VKtBxufHVHqdnJ51XHTvQFEBbtqQcq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDHD1%2FCk8jAMwqNyoGircA3sN4%2FEIwRubxfnICJU0tifaBJs26zWrRyj1BwTh46pmn6w6qUrABmkeCWBfsJPurZJntkcaaxXHuekHGUuxqEWogFDp5euVeeedWb0VGNssVoTAFISobzN8Va24hB8i5fmK7hs5dYOeCVX8gfEBznrvg%2B423GFDvIGr2OCBCVhUl3r1Z1Ub3zzVO%2BbtwyPOq6ZanH6a7B1Ln2u94EWcM0sKcahy8oYKRhDhs0P7tw6U4%2FOtWoggVvuE7OQv5T0IvVBhzXe%2BYjH%2FrPjOTPtqn7T85J2o9bjJFb8GKHqAl%2BOMzHS6pbXVHJP%2B%2Byu9vVi8SrQYkerkpLpDqXzo3WHh2B8dZTzr4JEBXcG73dGkoZvgiX6hNYEUu72fc%2FyIRGwVgJpF0MFYrzEXzkfnya3flNxvQVPA2A4f%2BpmVe0ZS1G0%2FJsc5iz6jyV6KBQJe0NtWX4ZPgb7GK4Z8bOmFj0fuDl0LIql%2F%2FD2qLu6EQ09jBGQFCh00vqEU9fgnmJ5NGbVqDrjCvTuDmBUWhYRciFmpx7YxH7MXxTwbf4mfgd7f0zISww3e7tsjKsUGHMJH7FQ45j8fyj2zEKFA00wVwbnMchh0h29LT9gUR79oFRZxsYi6KFvYl2VuVMVwgJZaMITwl70GOqUBa4N7MmW9AeNC85h%2FHWzruN4Fxtx28PgI9RQJS5Gwbn1eIuh9VTVleo8umK43IS9NjO76IXAVeIaA9DO87jrIxMGgnUwtXWvBFSM4NI04NnIaCbfq9K2bI2oNIBjoL%2FeH%2F6FfKjbT1Na3k6WEBtx1A%2FAwMK7gsm86LYxpGCqz6tWLaVG0H73qF0Ls6klmjLH8BGoBrPyBUnL%2F%2BWTuPeDiUxTWEzSt&X-Amz-Signature=c04d2f1ce09ec9c0cb5950701c697e0a36f3ca784ca7e073424a0c9577f5433d&X-Amz-SignedHeaders=host&x-id=GetObject)
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