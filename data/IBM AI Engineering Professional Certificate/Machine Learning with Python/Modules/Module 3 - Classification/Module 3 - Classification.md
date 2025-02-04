

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GCRZ4KT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHfi2JbtXQmoNAXVgqM0OF3VX8LR1VcdFSzA%2Fn9XOUDkAiEAw60YCzrWaH0MMuI7qxI%2BxVudEdaPcB%2FSABb%2Fhzbe1hIq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDKouB5WRXJhYATKm5SrcA2cGXIHe6DDMuHRQeJ2SEn%2BvHjePTLu22TL0lQGVUQUE252vfNUnaqZ%2BzxhYXa%2BpY5PMX%2B6i3Q2DQ0YXpHg78j7PT0pIQRhyscc3u4HJ4%2FfA%2FUAGNHuTAIypoxjeS6t4EnMFuPzJp9li8tzf7u1NHaej1P5e%2FX7Snyollw7CxmU%2BefyaMplqQqnx3LRpcrXlzki5ojIF5g8%2FRTlW7Hsl3QOoKGpnPH5WmQqfO1kXeKJf7yQkQivq04ok1m5bmEo5zvkq0jIKYgY%2BYApc%2Ffc7YUs7Vtkg6e1Ui1BO3EZufH7D93kRnbi4CV93nPkseOKtF9W8MuHPPI1x51FmLn5kC1kDFuNlqyCXsCLlmYxJKwS5HyMrUGuU8Mkihm5IrJC8kcRfkII68J5TjvbNf1c27kScDuX%2BqA3NobmB8To7qtgiowr%2B4C2REe2We2en7qdt4e0MpU9kRknu6lqBQquT09CLuHPJ0TnoLVSAsxLaJVB%2FxS2KtErixWeeN0GKq5uZNpG9C75O8GdnaKiPsfo%2FN0Ixt4bBZIUBDy8YIEzKziX1EPq%2BSYNNSDUybBMxNwFvAlY4VMy79RbGI8qlqFdMAaFlvUJ%2FVARfEGBNxCXu4SHu1xVhSdmhtW%2BxCEZmMLy9ib0GOqUBbKUdvYFtoRwK4iBpNW1Ar%2BPh3tDSoBeWUxK794pVAj7a06ZLNeZ%2Fz%2F8kT61FHevlchBLLb%2FAC2rqwPLdUzle%2FfMlVeNyjxprF0lUXjh96rFWjoEwYeym5%2BbHise7Q68A%2BRCOBHKMtFkyOXtxwO7r1%2BcQ7tjyCtOOsGXJekt2S8uFs04euFUPcEPqoF54ub4ZbeGwBmIWbCL3J2TaE3AnI0oKaMMK&X-Amz-Signature=171982bd10114b1f31181edfcad2460c98113affff0b1ba0e4d9a810b78303d6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GCRZ4KT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHfi2JbtXQmoNAXVgqM0OF3VX8LR1VcdFSzA%2Fn9XOUDkAiEAw60YCzrWaH0MMuI7qxI%2BxVudEdaPcB%2FSABb%2Fhzbe1hIq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDKouB5WRXJhYATKm5SrcA2cGXIHe6DDMuHRQeJ2SEn%2BvHjePTLu22TL0lQGVUQUE252vfNUnaqZ%2BzxhYXa%2BpY5PMX%2B6i3Q2DQ0YXpHg78j7PT0pIQRhyscc3u4HJ4%2FfA%2FUAGNHuTAIypoxjeS6t4EnMFuPzJp9li8tzf7u1NHaej1P5e%2FX7Snyollw7CxmU%2BefyaMplqQqnx3LRpcrXlzki5ojIF5g8%2FRTlW7Hsl3QOoKGpnPH5WmQqfO1kXeKJf7yQkQivq04ok1m5bmEo5zvkq0jIKYgY%2BYApc%2Ffc7YUs7Vtkg6e1Ui1BO3EZufH7D93kRnbi4CV93nPkseOKtF9W8MuHPPI1x51FmLn5kC1kDFuNlqyCXsCLlmYxJKwS5HyMrUGuU8Mkihm5IrJC8kcRfkII68J5TjvbNf1c27kScDuX%2BqA3NobmB8To7qtgiowr%2B4C2REe2We2en7qdt4e0MpU9kRknu6lqBQquT09CLuHPJ0TnoLVSAsxLaJVB%2FxS2KtErixWeeN0GKq5uZNpG9C75O8GdnaKiPsfo%2FN0Ixt4bBZIUBDy8YIEzKziX1EPq%2BSYNNSDUybBMxNwFvAlY4VMy79RbGI8qlqFdMAaFlvUJ%2FVARfEGBNxCXu4SHu1xVhSdmhtW%2BxCEZmMLy9ib0GOqUBbKUdvYFtoRwK4iBpNW1Ar%2BPh3tDSoBeWUxK794pVAj7a06ZLNeZ%2Fz%2F8kT61FHevlchBLLb%2FAC2rqwPLdUzle%2FfMlVeNyjxprF0lUXjh96rFWjoEwYeym5%2BbHise7Q68A%2BRCOBHKMtFkyOXtxwO7r1%2BcQ7tjyCtOOsGXJekt2S8uFs04euFUPcEPqoF54ub4ZbeGwBmIWbCL3J2TaE3AnI0oKaMMK&X-Amz-Signature=f9f800cdc18c99b1012fe54a7c2e0e3d4385c8351d47e513c906631fab6fa132&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GCRZ4KT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHfi2JbtXQmoNAXVgqM0OF3VX8LR1VcdFSzA%2Fn9XOUDkAiEAw60YCzrWaH0MMuI7qxI%2BxVudEdaPcB%2FSABb%2Fhzbe1hIq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDKouB5WRXJhYATKm5SrcA2cGXIHe6DDMuHRQeJ2SEn%2BvHjePTLu22TL0lQGVUQUE252vfNUnaqZ%2BzxhYXa%2BpY5PMX%2B6i3Q2DQ0YXpHg78j7PT0pIQRhyscc3u4HJ4%2FfA%2FUAGNHuTAIypoxjeS6t4EnMFuPzJp9li8tzf7u1NHaej1P5e%2FX7Snyollw7CxmU%2BefyaMplqQqnx3LRpcrXlzki5ojIF5g8%2FRTlW7Hsl3QOoKGpnPH5WmQqfO1kXeKJf7yQkQivq04ok1m5bmEo5zvkq0jIKYgY%2BYApc%2Ffc7YUs7Vtkg6e1Ui1BO3EZufH7D93kRnbi4CV93nPkseOKtF9W8MuHPPI1x51FmLn5kC1kDFuNlqyCXsCLlmYxJKwS5HyMrUGuU8Mkihm5IrJC8kcRfkII68J5TjvbNf1c27kScDuX%2BqA3NobmB8To7qtgiowr%2B4C2REe2We2en7qdt4e0MpU9kRknu6lqBQquT09CLuHPJ0TnoLVSAsxLaJVB%2FxS2KtErixWeeN0GKq5uZNpG9C75O8GdnaKiPsfo%2FN0Ixt4bBZIUBDy8YIEzKziX1EPq%2BSYNNSDUybBMxNwFvAlY4VMy79RbGI8qlqFdMAaFlvUJ%2FVARfEGBNxCXu4SHu1xVhSdmhtW%2BxCEZmMLy9ib0GOqUBbKUdvYFtoRwK4iBpNW1Ar%2BPh3tDSoBeWUxK794pVAj7a06ZLNeZ%2Fz%2F8kT61FHevlchBLLb%2FAC2rqwPLdUzle%2FfMlVeNyjxprF0lUXjh96rFWjoEwYeym5%2BbHise7Q68A%2BRCOBHKMtFkyOXtxwO7r1%2BcQ7tjyCtOOsGXJekt2S8uFs04euFUPcEPqoF54ub4ZbeGwBmIWbCL3J2TaE3AnI0oKaMMK&X-Amz-Signature=e38203bfd19b6e115ea0875771cf22a7dfd26f5684641d0777d8773e002f3d39&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7ZBZJXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIBEuPCW%2FK%2B94oXFiKR5DcjB%2BVhrbfcwFjNdKqKJbfrr%2FAiBfqLIrZ%2FvCLsLZspRUpG3C%2F9%2F6bhHqc79CUHlGWx2FgSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMNj0R5jnTDKl%2B3MmRKtwDSCdAgA8db6kpwV0oGN6THNWLENpG2FJVJHmY12IYeVCWNoYBUFQgMoFvkEBEXwaM9Xg4evsOItFVnXNEr1Ww7WyAjhlOD7R4peVVaWSCO0KPMMmMXKycfBXg5BNghdVHJyfaQgr1ick8uUa0TTLfxh%2FYL1G3KBQkJRbhVXZ02ZGr0kBxONGFXEnJ1mkSZG0Pdyh3oW4ClqBIe7u6PwgXHKsv5FVj2ftay4GRdVRDB6p4YSTzR%2BGpFGoqkJQ0%2BgmtyRa437l%2Bmicx2RceC73hlSjKtr2sKnuAGBmpPQyTTrvjngHQiAX0%2FZ6tAzySoElIfgoZ6hvY6xaiiQzdNBZdVwazpeDBLPDPi1b9npDZ0awV0Q3oXW7zwClqQcbt5UYJiV8510Tw6ddYorsYyoF%2B7hIGRwzqhwodPXFnRcpqTNns7%2BBQ9lEKUoF2fhpsbH9UtMigLS5q6KkJIBZ0rVpJAMC6dX0ugqDEezawh7ijj1wax3xIwU7axto4V%2FFHFNa32RTz3qlasSuSwVaaeDrBxcva9%2BEVrTdmOOcLqDSafRiZXu1O7VQHtbTEXoJDtphA8BF%2BgU%2FzWqWEFtVb2S6QCsj6sTsblPgAPYnO9bCJxP4H9DS3PaYY3T93d5UwkL2JvQY6pgHxTRgqenLdPbFDEpQuywlTXw3I0yJ%2BEOwKqycxT433EuIkoJykc9Hl%2FLptQ4bsHh5PL4%2BVhpW4kQmuJqubhuSHoElxGkCSAGDdxlcTvoorbV2ePoHSdL0mV5pBq1NS67likqHCg3yvRcMl2NPUfmbADyEXvMRp4DOH9Re9FC7TmmXfnOGMpwiuO5ek%2FrjAf5gyD%2Fff%2FsL6OaDV8YkN7CTnJfvaT30W&X-Amz-Signature=b30a19e0fbd32add0b29b0908b0a8871fa1c49273bbbe06bfd89cf9f9f3bd167&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7ZBZJXJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIBEuPCW%2FK%2B94oXFiKR5DcjB%2BVhrbfcwFjNdKqKJbfrr%2FAiBfqLIrZ%2FvCLsLZspRUpG3C%2F9%2F6bhHqc79CUHlGWx2FgSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMNj0R5jnTDKl%2B3MmRKtwDSCdAgA8db6kpwV0oGN6THNWLENpG2FJVJHmY12IYeVCWNoYBUFQgMoFvkEBEXwaM9Xg4evsOItFVnXNEr1Ww7WyAjhlOD7R4peVVaWSCO0KPMMmMXKycfBXg5BNghdVHJyfaQgr1ick8uUa0TTLfxh%2FYL1G3KBQkJRbhVXZ02ZGr0kBxONGFXEnJ1mkSZG0Pdyh3oW4ClqBIe7u6PwgXHKsv5FVj2ftay4GRdVRDB6p4YSTzR%2BGpFGoqkJQ0%2BgmtyRa437l%2Bmicx2RceC73hlSjKtr2sKnuAGBmpPQyTTrvjngHQiAX0%2FZ6tAzySoElIfgoZ6hvY6xaiiQzdNBZdVwazpeDBLPDPi1b9npDZ0awV0Q3oXW7zwClqQcbt5UYJiV8510Tw6ddYorsYyoF%2B7hIGRwzqhwodPXFnRcpqTNns7%2BBQ9lEKUoF2fhpsbH9UtMigLS5q6KkJIBZ0rVpJAMC6dX0ugqDEezawh7ijj1wax3xIwU7axto4V%2FFHFNa32RTz3qlasSuSwVaaeDrBxcva9%2BEVrTdmOOcLqDSafRiZXu1O7VQHtbTEXoJDtphA8BF%2BgU%2FzWqWEFtVb2S6QCsj6sTsblPgAPYnO9bCJxP4H9DS3PaYY3T93d5UwkL2JvQY6pgHxTRgqenLdPbFDEpQuywlTXw3I0yJ%2BEOwKqycxT433EuIkoJykc9Hl%2FLptQ4bsHh5PL4%2BVhpW4kQmuJqubhuSHoElxGkCSAGDdxlcTvoorbV2ePoHSdL0mV5pBq1NS67likqHCg3yvRcMl2NPUfmbADyEXvMRp4DOH9Re9FC7TmmXfnOGMpwiuO5ek%2FrjAf5gyD%2Fff%2FsL6OaDV8YkN7CTnJfvaT30W&X-Amz-Signature=ac6871baa2eb7a970c83a9a557b936ba4f99c59f039da9d93b1bec1a42618e5e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GCRZ4KT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHfi2JbtXQmoNAXVgqM0OF3VX8LR1VcdFSzA%2Fn9XOUDkAiEAw60YCzrWaH0MMuI7qxI%2BxVudEdaPcB%2FSABb%2Fhzbe1hIq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDKouB5WRXJhYATKm5SrcA2cGXIHe6DDMuHRQeJ2SEn%2BvHjePTLu22TL0lQGVUQUE252vfNUnaqZ%2BzxhYXa%2BpY5PMX%2B6i3Q2DQ0YXpHg78j7PT0pIQRhyscc3u4HJ4%2FfA%2FUAGNHuTAIypoxjeS6t4EnMFuPzJp9li8tzf7u1NHaej1P5e%2FX7Snyollw7CxmU%2BefyaMplqQqnx3LRpcrXlzki5ojIF5g8%2FRTlW7Hsl3QOoKGpnPH5WmQqfO1kXeKJf7yQkQivq04ok1m5bmEo5zvkq0jIKYgY%2BYApc%2Ffc7YUs7Vtkg6e1Ui1BO3EZufH7D93kRnbi4CV93nPkseOKtF9W8MuHPPI1x51FmLn5kC1kDFuNlqyCXsCLlmYxJKwS5HyMrUGuU8Mkihm5IrJC8kcRfkII68J5TjvbNf1c27kScDuX%2BqA3NobmB8To7qtgiowr%2B4C2REe2We2en7qdt4e0MpU9kRknu6lqBQquT09CLuHPJ0TnoLVSAsxLaJVB%2FxS2KtErixWeeN0GKq5uZNpG9C75O8GdnaKiPsfo%2FN0Ixt4bBZIUBDy8YIEzKziX1EPq%2BSYNNSDUybBMxNwFvAlY4VMy79RbGI8qlqFdMAaFlvUJ%2FVARfEGBNxCXu4SHu1xVhSdmhtW%2BxCEZmMLy9ib0GOqUBbKUdvYFtoRwK4iBpNW1Ar%2BPh3tDSoBeWUxK794pVAj7a06ZLNeZ%2Fz%2F8kT61FHevlchBLLb%2FAC2rqwPLdUzle%2FfMlVeNyjxprF0lUXjh96rFWjoEwYeym5%2BbHise7Q68A%2BRCOBHKMtFkyOXtxwO7r1%2BcQ7tjyCtOOsGXJekt2S8uFs04euFUPcEPqoF54ub4ZbeGwBmIWbCL3J2TaE3AnI0oKaMMK&X-Amz-Signature=e2b0b1ce29cb3ae26ae9d4e0c35c59baf624357951c3e53212426d6c1457f455&X-Amz-SignedHeaders=host&x-id=GetObject)
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