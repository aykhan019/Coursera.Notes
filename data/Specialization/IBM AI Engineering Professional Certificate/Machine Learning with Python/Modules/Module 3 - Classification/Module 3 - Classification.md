

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LCEXQ54%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIFRHhTKsc8NC8GmEprxtEOYuQrm%2Bb81L7FH%2BBVvZ5VDqAiEA9biQXZ3xlTuZijM4Xd2bFGkdaJWvXYdN%2F5H2SpwbFyQq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDL%2F9WX%2BMyaUm5CbH3SrcAzAhafrW2zfz4KeohuhSAvj0RJTJpwtW2Xt5f%2B7rNy7lacahP1JrgaRPmsZkpdVPxVWvZ%2FyRgqvvOCT7v8WNcwx1SekRTTyBZClTTHSWAN%2BADtldHdXioZx2XixKZvtcbhd%2FFf77tN%2FjNFgYtBbh8s2qk%2F0FRsOPJ%2Bb3QLjFHbcVHmYcnIMU6lqzLtMwWYY5JoHh%2BC9BHZF0UNgg966GacEqZ9vAy3fASQEcuGC%2FbynOJy62KwW%2FOFOOqw5Tg%2B%2FS236q9MsQvqLxqm2gdZjsbsf2r3reKrWTR6Jyc5I6Pmq2%2FXUOtF%2Fp%2FwBTEfDe%2BgrdMc1eMIhu50vmmxUk1ShUC6Dwnvz8QYxmlj%2B2NPZ%2Fz%2BzhnMqhlKoksGkiAwx8wOE21kEvA6D2jNggpmlq1DDFGbvKz%2FrmvpWrBy18azqKRn0rfbnl8EJ2tr%2B3TpKbkdCfbuP8CpNIes5wAPxyOJJAW5%2F82pjop8z%2BuBWCQ4G5Too%2FSSPNiU1Q%2FBcxIB41HGPa%2BXgMsrDHI%2BUYc7rAF0IhZXbXtsmu3ijHawEeZYLLDjkgmMwWiw%2BjjLLRioNm7YNdhQzi%2BNyLKGL%2BK5aRHQbnWgOMD163AzdKr5UwWh6JVBAs6tAVVhsR3drc8pn%2FMIj65LwGOqUBCIl%2F7gS362vmhW5927pYmlkr%2BqkYCU7tCkI%2F67mK8SSGXcnCHcFefgKtoNlmeEaoXgB7vanmDC87vr8ZEaoxBZwxsgqeUQSg36tdKm7tOjOjeBGDAGkpRQtZCNIDuM%2FAOS7vTdGFvYg1MNpx0FKnahcc0hKoqIInC3WUkNaXvb%2FtztMPonXhnRqpM6NGY8I3eSlUqFKgXHGtdSrN2VmlZqRbKbFD&X-Amz-Signature=2fe1d4a57153e89a565d19b137a7e0da12c588f9d3cc4d0f6a1bcc7f7d8721eb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LCEXQ54%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIFRHhTKsc8NC8GmEprxtEOYuQrm%2Bb81L7FH%2BBVvZ5VDqAiEA9biQXZ3xlTuZijM4Xd2bFGkdaJWvXYdN%2F5H2SpwbFyQq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDL%2F9WX%2BMyaUm5CbH3SrcAzAhafrW2zfz4KeohuhSAvj0RJTJpwtW2Xt5f%2B7rNy7lacahP1JrgaRPmsZkpdVPxVWvZ%2FyRgqvvOCT7v8WNcwx1SekRTTyBZClTTHSWAN%2BADtldHdXioZx2XixKZvtcbhd%2FFf77tN%2FjNFgYtBbh8s2qk%2F0FRsOPJ%2Bb3QLjFHbcVHmYcnIMU6lqzLtMwWYY5JoHh%2BC9BHZF0UNgg966GacEqZ9vAy3fASQEcuGC%2FbynOJy62KwW%2FOFOOqw5Tg%2B%2FS236q9MsQvqLxqm2gdZjsbsf2r3reKrWTR6Jyc5I6Pmq2%2FXUOtF%2Fp%2FwBTEfDe%2BgrdMc1eMIhu50vmmxUk1ShUC6Dwnvz8QYxmlj%2B2NPZ%2Fz%2BzhnMqhlKoksGkiAwx8wOE21kEvA6D2jNggpmlq1DDFGbvKz%2FrmvpWrBy18azqKRn0rfbnl8EJ2tr%2B3TpKbkdCfbuP8CpNIes5wAPxyOJJAW5%2F82pjop8z%2BuBWCQ4G5Too%2FSSPNiU1Q%2FBcxIB41HGPa%2BXgMsrDHI%2BUYc7rAF0IhZXbXtsmu3ijHawEeZYLLDjkgmMwWiw%2BjjLLRioNm7YNdhQzi%2BNyLKGL%2BK5aRHQbnWgOMD163AzdKr5UwWh6JVBAs6tAVVhsR3drc8pn%2FMIj65LwGOqUBCIl%2F7gS362vmhW5927pYmlkr%2BqkYCU7tCkI%2F67mK8SSGXcnCHcFefgKtoNlmeEaoXgB7vanmDC87vr8ZEaoxBZwxsgqeUQSg36tdKm7tOjOjeBGDAGkpRQtZCNIDuM%2FAOS7vTdGFvYg1MNpx0FKnahcc0hKoqIInC3WUkNaXvb%2FtztMPonXhnRqpM6NGY8I3eSlUqFKgXHGtdSrN2VmlZqRbKbFD&X-Amz-Signature=aa5a67f7d61ea1b8819b110178f4330c6905651cc45f90366f7ddfd261b99b2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LCEXQ54%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIFRHhTKsc8NC8GmEprxtEOYuQrm%2Bb81L7FH%2BBVvZ5VDqAiEA9biQXZ3xlTuZijM4Xd2bFGkdaJWvXYdN%2F5H2SpwbFyQq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDL%2F9WX%2BMyaUm5CbH3SrcAzAhafrW2zfz4KeohuhSAvj0RJTJpwtW2Xt5f%2B7rNy7lacahP1JrgaRPmsZkpdVPxVWvZ%2FyRgqvvOCT7v8WNcwx1SekRTTyBZClTTHSWAN%2BADtldHdXioZx2XixKZvtcbhd%2FFf77tN%2FjNFgYtBbh8s2qk%2F0FRsOPJ%2Bb3QLjFHbcVHmYcnIMU6lqzLtMwWYY5JoHh%2BC9BHZF0UNgg966GacEqZ9vAy3fASQEcuGC%2FbynOJy62KwW%2FOFOOqw5Tg%2B%2FS236q9MsQvqLxqm2gdZjsbsf2r3reKrWTR6Jyc5I6Pmq2%2FXUOtF%2Fp%2FwBTEfDe%2BgrdMc1eMIhu50vmmxUk1ShUC6Dwnvz8QYxmlj%2B2NPZ%2Fz%2BzhnMqhlKoksGkiAwx8wOE21kEvA6D2jNggpmlq1DDFGbvKz%2FrmvpWrBy18azqKRn0rfbnl8EJ2tr%2B3TpKbkdCfbuP8CpNIes5wAPxyOJJAW5%2F82pjop8z%2BuBWCQ4G5Too%2FSSPNiU1Q%2FBcxIB41HGPa%2BXgMsrDHI%2BUYc7rAF0IhZXbXtsmu3ijHawEeZYLLDjkgmMwWiw%2BjjLLRioNm7YNdhQzi%2BNyLKGL%2BK5aRHQbnWgOMD163AzdKr5UwWh6JVBAs6tAVVhsR3drc8pn%2FMIj65LwGOqUBCIl%2F7gS362vmhW5927pYmlkr%2BqkYCU7tCkI%2F67mK8SSGXcnCHcFefgKtoNlmeEaoXgB7vanmDC87vr8ZEaoxBZwxsgqeUQSg36tdKm7tOjOjeBGDAGkpRQtZCNIDuM%2FAOS7vTdGFvYg1MNpx0FKnahcc0hKoqIInC3WUkNaXvb%2FtztMPonXhnRqpM6NGY8I3eSlUqFKgXHGtdSrN2VmlZqRbKbFD&X-Amz-Signature=65cf12ce2add0ad5c5033d33f7004fb28d94c195bc821c4be9c5d6ee28a333d7&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRMN4F2J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIDaqTaYpKSENq7XabH2RJZq5lzYc%2B2lmeArm61rkXjQMAiEAkHFGbMMMioGGL6QnzBzTz%2BItrIvOvQL49YVuU%2FnUQkIq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDDLOjI8I53Lnmd5Z7SrcAzoHQetq81bVLZwc25W2%2FN3OrZRYYaG4Mo5jq6DlbgorFnyH3fQ1GJtkr2TRbuYYBZVbPmMibntKlAqqyaCdgEFFxkJClxeVzW%2B8u%2BOkp0is3tHpocMmTwaW6oB6A0R9t0RzjX0cdtx2L%2FkvtXwzFYvo3jDNWK7XemuK%2FqA8KdWwWWTDqO6MyxrZDAFPT26GO7%2BrmJ%2FDPCWE%2BoN8LSA4O1fJQ9THINr2fxV9W%2BquXuqW3%2BzH526CIdwCg0wCBtq09CSFKUoxmIsldf4IdEgBPi5wCBi9tqrzKxSsoXV1fzZprQxZ2QrUrikdFnCXzj%2Bd5RPVxZhA3yxryBN2DYs77VeEpSlTrBLtuzuNovsj4LwQJROenDtlnXwTzSIaWcE%2ByGs9qtrbTtKh6G6PzuJcQEla740l4RfU9n6kbv0cp7n3ghKwec%2FyZCykqR0QTm6RbpxqCQS2%2Fc0Aq0GILT4n3ETMJXmT42SdLOX8IvfZ6owyZFQA8tondHOryg2toXBKzhqzjD9ViGpvb0j4Aluj6yeahV6MJiThEbjgRGDA8IUH7c6D1jpogfhPCHGl882gWs%2FHfmLnoVmTXWPyz%2BQFs%2FmJnOEmDzbWBIUF91JAkEm89dMnoENmFcMuXc7gMIn65LwGOqUByStzwLQudLNPyIyDuAZ30Fs5PbMXNhNU%2Bh6qOw7fuNJ98wIU4kB%2BJArVD9hF0O7GmE7gaff6AYv4C5rc0h2ud%2BejTpdayPcTnsaOeQNchM%2F1MFtH9fjsOnYIeIu4PhlJJHuNmIedCKZJrjhQjZqrECWbRPnlTP7NkgauNWWiz71SM3rtdtfbVUjxuGRSlrhUifQAUnMbdjGpuIG%2BWj1CSW75izJ7&X-Amz-Signature=98bc1b4670952ccb3776589bc89a79c423575460bd2288a3b8ab1ef20034b524&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRMN4F2J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIDaqTaYpKSENq7XabH2RJZq5lzYc%2B2lmeArm61rkXjQMAiEAkHFGbMMMioGGL6QnzBzTz%2BItrIvOvQL49YVuU%2FnUQkIq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDDLOjI8I53Lnmd5Z7SrcAzoHQetq81bVLZwc25W2%2FN3OrZRYYaG4Mo5jq6DlbgorFnyH3fQ1GJtkr2TRbuYYBZVbPmMibntKlAqqyaCdgEFFxkJClxeVzW%2B8u%2BOkp0is3tHpocMmTwaW6oB6A0R9t0RzjX0cdtx2L%2FkvtXwzFYvo3jDNWK7XemuK%2FqA8KdWwWWTDqO6MyxrZDAFPT26GO7%2BrmJ%2FDPCWE%2BoN8LSA4O1fJQ9THINr2fxV9W%2BquXuqW3%2BzH526CIdwCg0wCBtq09CSFKUoxmIsldf4IdEgBPi5wCBi9tqrzKxSsoXV1fzZprQxZ2QrUrikdFnCXzj%2Bd5RPVxZhA3yxryBN2DYs77VeEpSlTrBLtuzuNovsj4LwQJROenDtlnXwTzSIaWcE%2ByGs9qtrbTtKh6G6PzuJcQEla740l4RfU9n6kbv0cp7n3ghKwec%2FyZCykqR0QTm6RbpxqCQS2%2Fc0Aq0GILT4n3ETMJXmT42SdLOX8IvfZ6owyZFQA8tondHOryg2toXBKzhqzjD9ViGpvb0j4Aluj6yeahV6MJiThEbjgRGDA8IUH7c6D1jpogfhPCHGl882gWs%2FHfmLnoVmTXWPyz%2BQFs%2FmJnOEmDzbWBIUF91JAkEm89dMnoENmFcMuXc7gMIn65LwGOqUByStzwLQudLNPyIyDuAZ30Fs5PbMXNhNU%2Bh6qOw7fuNJ98wIU4kB%2BJArVD9hF0O7GmE7gaff6AYv4C5rc0h2ud%2BejTpdayPcTnsaOeQNchM%2F1MFtH9fjsOnYIeIu4PhlJJHuNmIedCKZJrjhQjZqrECWbRPnlTP7NkgauNWWiz71SM3rtdtfbVUjxuGRSlrhUifQAUnMbdjGpuIG%2BWj1CSW75izJ7&X-Amz-Signature=71bb4623576c102693ded141215586157cd45999831736b7e403df84cdac9cb9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LCEXQ54%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIFRHhTKsc8NC8GmEprxtEOYuQrm%2Bb81L7FH%2BBVvZ5VDqAiEA9biQXZ3xlTuZijM4Xd2bFGkdaJWvXYdN%2F5H2SpwbFyQq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDL%2F9WX%2BMyaUm5CbH3SrcAzAhafrW2zfz4KeohuhSAvj0RJTJpwtW2Xt5f%2B7rNy7lacahP1JrgaRPmsZkpdVPxVWvZ%2FyRgqvvOCT7v8WNcwx1SekRTTyBZClTTHSWAN%2BADtldHdXioZx2XixKZvtcbhd%2FFf77tN%2FjNFgYtBbh8s2qk%2F0FRsOPJ%2Bb3QLjFHbcVHmYcnIMU6lqzLtMwWYY5JoHh%2BC9BHZF0UNgg966GacEqZ9vAy3fASQEcuGC%2FbynOJy62KwW%2FOFOOqw5Tg%2B%2FS236q9MsQvqLxqm2gdZjsbsf2r3reKrWTR6Jyc5I6Pmq2%2FXUOtF%2Fp%2FwBTEfDe%2BgrdMc1eMIhu50vmmxUk1ShUC6Dwnvz8QYxmlj%2B2NPZ%2Fz%2BzhnMqhlKoksGkiAwx8wOE21kEvA6D2jNggpmlq1DDFGbvKz%2FrmvpWrBy18azqKRn0rfbnl8EJ2tr%2B3TpKbkdCfbuP8CpNIes5wAPxyOJJAW5%2F82pjop8z%2BuBWCQ4G5Too%2FSSPNiU1Q%2FBcxIB41HGPa%2BXgMsrDHI%2BUYc7rAF0IhZXbXtsmu3ijHawEeZYLLDjkgmMwWiw%2BjjLLRioNm7YNdhQzi%2BNyLKGL%2BK5aRHQbnWgOMD163AzdKr5UwWh6JVBAs6tAVVhsR3drc8pn%2FMIj65LwGOqUBCIl%2F7gS362vmhW5927pYmlkr%2BqkYCU7tCkI%2F67mK8SSGXcnCHcFefgKtoNlmeEaoXgB7vanmDC87vr8ZEaoxBZwxsgqeUQSg36tdKm7tOjOjeBGDAGkpRQtZCNIDuM%2FAOS7vTdGFvYg1MNpx0FKnahcc0hKoqIInC3WUkNaXvb%2FtztMPonXhnRqpM6NGY8I3eSlUqFKgXHGtdSrN2VmlZqRbKbFD&X-Amz-Signature=86914261e7589c46dcab13cff4d27fbaca5033489ffcdf3974b12a7d66745d77&X-Amz-SignedHeaders=host&x-id=GetObject)
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