

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIMPMDQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqloI7Q16xblhQeqACIHL%2FIy6boH6lZCIH5fDlbeLGRAiEA1wxyg%2Bn1juCTHQ6CUQy%2Ba%2BMHuy5n%2FBx9khDFpRMPdX0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXHVnGTq7LuHMFZ5ircA7GOPi6jv1lXSwz4HDXOA6gznHvr9FP4mj7VGTfFrvgo6yfoGsKtvoH90rR7zfWk37IrnAea5%2FEK36%2BQs4SInbxJMOID4L8xPhC34Euxrkg%2B%2FioMJkRqW27NaC%2FBWB9Vf7Lszs9imgQdYR7jkHZ9Nm539MrI3E7tKo%2BXnPrf%2FeKcbz%2FPKD06IEfLv6ZNGMsVzm008%2Bwos0ynw8wuwuoUX5RmsuXF4iYYoGUl19ocovQ9Ka0J%2FPkj9WKWK3p0TglPKr71F91ULMrggVtKtaD2Ju%2Flj8b8d%2BVK0jihw8XpJcEu2nvMHkM5bETZhLcWXUWucqj9cVpi4lnqutCN99v%2BKqCTu%2BBgHA4Vppn%2FUEws8rE7vvhTEl8qUCj3%2BnIrU6I95ZHyrlNbTg4mDK6s6Mi7BHQtroZD7bIpsvMhCsvQ%2BPyXTNWYfbopRM9%2Bmnm0u9fnAVUJyfI4zR2Oy5qRoYhhcbIBsfFio2kwsa2rnyhAVuICpaAZuLvYJW3F2KLu8WNU%2Bi83g34J3sLF%2FZmKuJD7veD5TN%2Fnb9o5sRHUjHYM3er3l1FordHE1mgmhjNiILeQLlh4FRSSlpechRiuPG4jMlmVrjyN%2BWPdspuzafge3LMDi3Ah5p6rk%2BjhK5oCMOOb%2FLwGOqUBgb9mhoyYtEQhYv1dw%2Fc6c7rRQhZLnUW%2B1Ved1dOnawdshdcdS4WwgamLfEosKQ6eFBrOrb2h2xmpYquNzQMQqfEu9a9gjeLBIEerUSvDcQ8IwyLrylADpDKl6qT87saZqXAWNwus%2FwlU6dgNaXTxWesqB%2BFEZ15Z43v1vfDH2j%2Bc0LqnIBD9jsfVcDyw3MxIzJzLN3KZruwSTcx41jL3j6HAIqLg&X-Amz-Signature=ee4545e887c6857337fdc141455a320b1adb66778dd7ff466ea7c0d0401a9c7b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIMPMDQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqloI7Q16xblhQeqACIHL%2FIy6boH6lZCIH5fDlbeLGRAiEA1wxyg%2Bn1juCTHQ6CUQy%2Ba%2BMHuy5n%2FBx9khDFpRMPdX0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXHVnGTq7LuHMFZ5ircA7GOPi6jv1lXSwz4HDXOA6gznHvr9FP4mj7VGTfFrvgo6yfoGsKtvoH90rR7zfWk37IrnAea5%2FEK36%2BQs4SInbxJMOID4L8xPhC34Euxrkg%2B%2FioMJkRqW27NaC%2FBWB9Vf7Lszs9imgQdYR7jkHZ9Nm539MrI3E7tKo%2BXnPrf%2FeKcbz%2FPKD06IEfLv6ZNGMsVzm008%2Bwos0ynw8wuwuoUX5RmsuXF4iYYoGUl19ocovQ9Ka0J%2FPkj9WKWK3p0TglPKr71F91ULMrggVtKtaD2Ju%2Flj8b8d%2BVK0jihw8XpJcEu2nvMHkM5bETZhLcWXUWucqj9cVpi4lnqutCN99v%2BKqCTu%2BBgHA4Vppn%2FUEws8rE7vvhTEl8qUCj3%2BnIrU6I95ZHyrlNbTg4mDK6s6Mi7BHQtroZD7bIpsvMhCsvQ%2BPyXTNWYfbopRM9%2Bmnm0u9fnAVUJyfI4zR2Oy5qRoYhhcbIBsfFio2kwsa2rnyhAVuICpaAZuLvYJW3F2KLu8WNU%2Bi83g34J3sLF%2FZmKuJD7veD5TN%2Fnb9o5sRHUjHYM3er3l1FordHE1mgmhjNiILeQLlh4FRSSlpechRiuPG4jMlmVrjyN%2BWPdspuzafge3LMDi3Ah5p6rk%2BjhK5oCMOOb%2FLwGOqUBgb9mhoyYtEQhYv1dw%2Fc6c7rRQhZLnUW%2B1Ved1dOnawdshdcdS4WwgamLfEosKQ6eFBrOrb2h2xmpYquNzQMQqfEu9a9gjeLBIEerUSvDcQ8IwyLrylADpDKl6qT87saZqXAWNwus%2FwlU6dgNaXTxWesqB%2BFEZ15Z43v1vfDH2j%2Bc0LqnIBD9jsfVcDyw3MxIzJzLN3KZruwSTcx41jL3j6HAIqLg&X-Amz-Signature=d05d99bf2b685cb32a03cad885690accb3cebf8364473534acc51ef81b2996ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIMPMDQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqloI7Q16xblhQeqACIHL%2FIy6boH6lZCIH5fDlbeLGRAiEA1wxyg%2Bn1juCTHQ6CUQy%2Ba%2BMHuy5n%2FBx9khDFpRMPdX0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXHVnGTq7LuHMFZ5ircA7GOPi6jv1lXSwz4HDXOA6gznHvr9FP4mj7VGTfFrvgo6yfoGsKtvoH90rR7zfWk37IrnAea5%2FEK36%2BQs4SInbxJMOID4L8xPhC34Euxrkg%2B%2FioMJkRqW27NaC%2FBWB9Vf7Lszs9imgQdYR7jkHZ9Nm539MrI3E7tKo%2BXnPrf%2FeKcbz%2FPKD06IEfLv6ZNGMsVzm008%2Bwos0ynw8wuwuoUX5RmsuXF4iYYoGUl19ocovQ9Ka0J%2FPkj9WKWK3p0TglPKr71F91ULMrggVtKtaD2Ju%2Flj8b8d%2BVK0jihw8XpJcEu2nvMHkM5bETZhLcWXUWucqj9cVpi4lnqutCN99v%2BKqCTu%2BBgHA4Vppn%2FUEws8rE7vvhTEl8qUCj3%2BnIrU6I95ZHyrlNbTg4mDK6s6Mi7BHQtroZD7bIpsvMhCsvQ%2BPyXTNWYfbopRM9%2Bmnm0u9fnAVUJyfI4zR2Oy5qRoYhhcbIBsfFio2kwsa2rnyhAVuICpaAZuLvYJW3F2KLu8WNU%2Bi83g34J3sLF%2FZmKuJD7veD5TN%2Fnb9o5sRHUjHYM3er3l1FordHE1mgmhjNiILeQLlh4FRSSlpechRiuPG4jMlmVrjyN%2BWPdspuzafge3LMDi3Ah5p6rk%2BjhK5oCMOOb%2FLwGOqUBgb9mhoyYtEQhYv1dw%2Fc6c7rRQhZLnUW%2B1Ved1dOnawdshdcdS4WwgamLfEosKQ6eFBrOrb2h2xmpYquNzQMQqfEu9a9gjeLBIEerUSvDcQ8IwyLrylADpDKl6qT87saZqXAWNwus%2FwlU6dgNaXTxWesqB%2BFEZ15Z43v1vfDH2j%2Bc0LqnIBD9jsfVcDyw3MxIzJzLN3KZruwSTcx41jL3j6HAIqLg&X-Amz-Signature=3f68deeab37f2d8313f0dbe9a5475c5f08d043bda40bc01263b52a7dab44fd61&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF46QXBQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDq%2B7L%2BOVzigsCDJVrwTQollqIZT%2BEgHx4NBDY%2Bv6prRAIgCqJ7NIV9Gd6UOMbya4QW6%2Fb2YN3s%2B31USo%2FKNxGFarUqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOH3lFYgrzJLCOSa9CrcA30YTWZxf5bOoj7SoaCY72RYX%2FM826pwKhdNpwYZ4VfqL7vF32sUpfqDzPsfi%2BG7WVsVPczcHds%2FT0x%2BuWbjxKJMhlYpOXL02WQVy%2Fso6bS4%2BLqWHnSrGyl8eblRENC%2FTbTGETyNPFjQE6IP8ko9dPIIMGWQn71YqsMR2ERsnhw7sahAkc9dSxgZjkaXS7Dnr9jsIf2lf918C%2B07VTFyZxhX6rIG8hy8Mmt9GbHkITOBYz15BgXV2Ix1VYFocec0KyYdSlEcsS8Gqob7nlYfpx2PNCxwUNjb%2BcPUVM%2FBTMWZztXXMrDKOPKo7Y%2BaBVzzfhTKHdelnmepTye6i9hoYqkYa3vzPNqN86jwJcE0vX2DXEOwa1udomRCX2MV4iWqKERbdbWxNtrP05JGDcRknL6BDSBJGaLCJK6gTdmBLb5Nm3wvxgv8R0chbaCJHSbgz96oaEC9ZAxkyJorlhnb%2FIOzlF%2FmdAx9DJl3aYYZKf%2BPKd%2B1J5SMZbSmbk%2FbYCPZIAPvBcGGgVW5zyAG8aD6e8nx1N45uoSelCsuEwaMHLrlFn0tcZ4Fb9CTM8Ef7aPx1I%2FK2MhNRs3B83kPgtYuIRuCu9xr5h%2BcYz86l4qjC26DG5dtXjv0Q8JXvHLGMJjh%2B7wGOqUBRunYbc%2B5pY2Gm%2B4MhXf%2Bt8HWYYuvs%2BlMI7yPq1wobREarmW5KWCE4VU14JBM6GDfmhHbKbmi5uX3tp8EDXm3b5VByvDISEyxfHaHMWa0YGqU0hytMrBe9dfmwx4DE5NeJQBkwic04PO%2FYZ5BhmQah7OwjgjarwjpfDLIBvcQQ%2B8wz%2BBXLsFyeUy5Q1YSkxoFZqtgMlkaziMZUqJkPzYDNXjsUzbr&X-Amz-Signature=bc9ed4e89524802786abaf7fae46b6e4f94e8985d20f81dffea5c1194dbb7a11&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF46QXBQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDq%2B7L%2BOVzigsCDJVrwTQollqIZT%2BEgHx4NBDY%2Bv6prRAIgCqJ7NIV9Gd6UOMbya4QW6%2Fb2YN3s%2B31USo%2FKNxGFarUqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOH3lFYgrzJLCOSa9CrcA30YTWZxf5bOoj7SoaCY72RYX%2FM826pwKhdNpwYZ4VfqL7vF32sUpfqDzPsfi%2BG7WVsVPczcHds%2FT0x%2BuWbjxKJMhlYpOXL02WQVy%2Fso6bS4%2BLqWHnSrGyl8eblRENC%2FTbTGETyNPFjQE6IP8ko9dPIIMGWQn71YqsMR2ERsnhw7sahAkc9dSxgZjkaXS7Dnr9jsIf2lf918C%2B07VTFyZxhX6rIG8hy8Mmt9GbHkITOBYz15BgXV2Ix1VYFocec0KyYdSlEcsS8Gqob7nlYfpx2PNCxwUNjb%2BcPUVM%2FBTMWZztXXMrDKOPKo7Y%2BaBVzzfhTKHdelnmepTye6i9hoYqkYa3vzPNqN86jwJcE0vX2DXEOwa1udomRCX2MV4iWqKERbdbWxNtrP05JGDcRknL6BDSBJGaLCJK6gTdmBLb5Nm3wvxgv8R0chbaCJHSbgz96oaEC9ZAxkyJorlhnb%2FIOzlF%2FmdAx9DJl3aYYZKf%2BPKd%2B1J5SMZbSmbk%2FbYCPZIAPvBcGGgVW5zyAG8aD6e8nx1N45uoSelCsuEwaMHLrlFn0tcZ4Fb9CTM8Ef7aPx1I%2FK2MhNRs3B83kPgtYuIRuCu9xr5h%2BcYz86l4qjC26DG5dtXjv0Q8JXvHLGMJjh%2B7wGOqUBRunYbc%2B5pY2Gm%2B4MhXf%2Bt8HWYYuvs%2BlMI7yPq1wobREarmW5KWCE4VU14JBM6GDfmhHbKbmi5uX3tp8EDXm3b5VByvDISEyxfHaHMWa0YGqU0hytMrBe9dfmwx4DE5NeJQBkwic04PO%2FYZ5BhmQah7OwjgjarwjpfDLIBvcQQ%2B8wz%2BBXLsFyeUy5Q1YSkxoFZqtgMlkaziMZUqJkPzYDNXjsUzbr&X-Amz-Signature=f91a780573c01ed50ff64fb4fefa2ddbb2de8a8d0b1b5d49aedf838c08cb1e16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIMPMDQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBqloI7Q16xblhQeqACIHL%2FIy6boH6lZCIH5fDlbeLGRAiEA1wxyg%2Bn1juCTHQ6CUQy%2Ba%2BMHuy5n%2FBx9khDFpRMPdX0qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXHVnGTq7LuHMFZ5ircA7GOPi6jv1lXSwz4HDXOA6gznHvr9FP4mj7VGTfFrvgo6yfoGsKtvoH90rR7zfWk37IrnAea5%2FEK36%2BQs4SInbxJMOID4L8xPhC34Euxrkg%2B%2FioMJkRqW27NaC%2FBWB9Vf7Lszs9imgQdYR7jkHZ9Nm539MrI3E7tKo%2BXnPrf%2FeKcbz%2FPKD06IEfLv6ZNGMsVzm008%2Bwos0ynw8wuwuoUX5RmsuXF4iYYoGUl19ocovQ9Ka0J%2FPkj9WKWK3p0TglPKr71F91ULMrggVtKtaD2Ju%2Flj8b8d%2BVK0jihw8XpJcEu2nvMHkM5bETZhLcWXUWucqj9cVpi4lnqutCN99v%2BKqCTu%2BBgHA4Vppn%2FUEws8rE7vvhTEl8qUCj3%2BnIrU6I95ZHyrlNbTg4mDK6s6Mi7BHQtroZD7bIpsvMhCsvQ%2BPyXTNWYfbopRM9%2Bmnm0u9fnAVUJyfI4zR2Oy5qRoYhhcbIBsfFio2kwsa2rnyhAVuICpaAZuLvYJW3F2KLu8WNU%2Bi83g34J3sLF%2FZmKuJD7veD5TN%2Fnb9o5sRHUjHYM3er3l1FordHE1mgmhjNiILeQLlh4FRSSlpechRiuPG4jMlmVrjyN%2BWPdspuzafge3LMDi3Ah5p6rk%2BjhK5oCMOOb%2FLwGOqUBgb9mhoyYtEQhYv1dw%2Fc6c7rRQhZLnUW%2B1Ved1dOnawdshdcdS4WwgamLfEosKQ6eFBrOrb2h2xmpYquNzQMQqfEu9a9gjeLBIEerUSvDcQ8IwyLrylADpDKl6qT87saZqXAWNwus%2FwlU6dgNaXTxWesqB%2BFEZ15Z43v1vfDH2j%2Bc0LqnIBD9jsfVcDyw3MxIzJzLN3KZruwSTcx41jL3j6HAIqLg&X-Amz-Signature=12903c31e312a81bc4fc206f2f0ff20f57f9fa068c6b896631ced32a5334fe4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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