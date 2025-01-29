

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUOZID3U%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDH6FXQ8yYw47AP9RkjdYUekg2tM4%2F8hgQipFX94V3%2FyQIgHBnxmN6JjFtdgsGi98KH9l2rfvSBaTqNAlBN1bx1qKoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCmTKQhmp0Ak%2BOJosSrcA8jdFvz6VSuwN1Vsw3pQMqUbS63e19LGBCWWeaL%2FkN42N2%2BV791psUzv%2FjTKE3J%2BQIxNilrvptBxtaT01DApb03EVsWlKlAC11x9OhFpjEQB4v043AXWDin%2FgeMUufqN%2FBvDcnjR6EcpYuHItqrhbtIf1nIbedTh1mmBuiIfRHdZfkegJRlQT10qFOS%2FGvsYv8AB8UGCd5e19O5GnBFTfldKTDCcW9904AYZmH97S7AQ7t99J4oWglOVABLvI3Ap%2FX5o8WhwQIVM93PspglmERVbIxstD9vnbEt2iR8WFiuJ0kUMxUHo3qNHfYQiDPLZYBiE9%2FK3kNaDHk9MIMhx1J0SLdz4MkahDIjXfEX0wRWAEb49iN1dZuXbbxXV3F%2FvpKwI0e2D6z4BwstJo86xDXbbJJWETbaKhzj2HaaMPXFsa%2FaQsNdvlF7%2FfC7t8Es5JtzM4BR18ZxtKbUlzEMYrz46AogrBO55HozePv6k0YUjkc5UyHiZfYiMfnlzbNdePUgFoavu%2Bwt8y1SOmzYjtfjBCtM2XtcSWqI0JB46kLi6in1vIx0V9gNmBE5x70zrDRRVlOuHfiGyZJpUcUxMKlWeuSAj3aZP8gR2wqKGgKj40ibasiVNw1TkfaxFMMT%2F57wGOqUB%2BFs4afqMvRbVoUeawUs%2B6utm1k27vNgY2OiyEIQ%2FBXa4ByBBrxX2a%2Bv%2F2%2F1BFcyB4HPMg9IfrzSShE64NnF9WSdyvQOxMLNc%2BeGX%2Frxzg5Zm3dCt9%2FK%2B6IPJ9fIZpGbEIKqEAgoJs9nyR0BIwbYCDmlmZUxFcx4OvSthxm2hqNm41ed2fS8p7nfNFtbDNxdzt7vpGOiW%2F6Cu5CRqXxqDelPfxIRC&X-Amz-Signature=528f511a8ea5c4d4e792acefe142546df0d7fbfc9102b0ee3324b3902137a7f2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUOZID3U%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDH6FXQ8yYw47AP9RkjdYUekg2tM4%2F8hgQipFX94V3%2FyQIgHBnxmN6JjFtdgsGi98KH9l2rfvSBaTqNAlBN1bx1qKoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCmTKQhmp0Ak%2BOJosSrcA8jdFvz6VSuwN1Vsw3pQMqUbS63e19LGBCWWeaL%2FkN42N2%2BV791psUzv%2FjTKE3J%2BQIxNilrvptBxtaT01DApb03EVsWlKlAC11x9OhFpjEQB4v043AXWDin%2FgeMUufqN%2FBvDcnjR6EcpYuHItqrhbtIf1nIbedTh1mmBuiIfRHdZfkegJRlQT10qFOS%2FGvsYv8AB8UGCd5e19O5GnBFTfldKTDCcW9904AYZmH97S7AQ7t99J4oWglOVABLvI3Ap%2FX5o8WhwQIVM93PspglmERVbIxstD9vnbEt2iR8WFiuJ0kUMxUHo3qNHfYQiDPLZYBiE9%2FK3kNaDHk9MIMhx1J0SLdz4MkahDIjXfEX0wRWAEb49iN1dZuXbbxXV3F%2FvpKwI0e2D6z4BwstJo86xDXbbJJWETbaKhzj2HaaMPXFsa%2FaQsNdvlF7%2FfC7t8Es5JtzM4BR18ZxtKbUlzEMYrz46AogrBO55HozePv6k0YUjkc5UyHiZfYiMfnlzbNdePUgFoavu%2Bwt8y1SOmzYjtfjBCtM2XtcSWqI0JB46kLi6in1vIx0V9gNmBE5x70zrDRRVlOuHfiGyZJpUcUxMKlWeuSAj3aZP8gR2wqKGgKj40ibasiVNw1TkfaxFMMT%2F57wGOqUB%2BFs4afqMvRbVoUeawUs%2B6utm1k27vNgY2OiyEIQ%2FBXa4ByBBrxX2a%2Bv%2F2%2F1BFcyB4HPMg9IfrzSShE64NnF9WSdyvQOxMLNc%2BeGX%2Frxzg5Zm3dCt9%2FK%2B6IPJ9fIZpGbEIKqEAgoJs9nyR0BIwbYCDmlmZUxFcx4OvSthxm2hqNm41ed2fS8p7nfNFtbDNxdzt7vpGOiW%2F6Cu5CRqXxqDelPfxIRC&X-Amz-Signature=721c334071500d1bbc6ae44dda45171d07c429a31429a77ead99efcde8a9fc88&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUOZID3U%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDH6FXQ8yYw47AP9RkjdYUekg2tM4%2F8hgQipFX94V3%2FyQIgHBnxmN6JjFtdgsGi98KH9l2rfvSBaTqNAlBN1bx1qKoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCmTKQhmp0Ak%2BOJosSrcA8jdFvz6VSuwN1Vsw3pQMqUbS63e19LGBCWWeaL%2FkN42N2%2BV791psUzv%2FjTKE3J%2BQIxNilrvptBxtaT01DApb03EVsWlKlAC11x9OhFpjEQB4v043AXWDin%2FgeMUufqN%2FBvDcnjR6EcpYuHItqrhbtIf1nIbedTh1mmBuiIfRHdZfkegJRlQT10qFOS%2FGvsYv8AB8UGCd5e19O5GnBFTfldKTDCcW9904AYZmH97S7AQ7t99J4oWglOVABLvI3Ap%2FX5o8WhwQIVM93PspglmERVbIxstD9vnbEt2iR8WFiuJ0kUMxUHo3qNHfYQiDPLZYBiE9%2FK3kNaDHk9MIMhx1J0SLdz4MkahDIjXfEX0wRWAEb49iN1dZuXbbxXV3F%2FvpKwI0e2D6z4BwstJo86xDXbbJJWETbaKhzj2HaaMPXFsa%2FaQsNdvlF7%2FfC7t8Es5JtzM4BR18ZxtKbUlzEMYrz46AogrBO55HozePv6k0YUjkc5UyHiZfYiMfnlzbNdePUgFoavu%2Bwt8y1SOmzYjtfjBCtM2XtcSWqI0JB46kLi6in1vIx0V9gNmBE5x70zrDRRVlOuHfiGyZJpUcUxMKlWeuSAj3aZP8gR2wqKGgKj40ibasiVNw1TkfaxFMMT%2F57wGOqUB%2BFs4afqMvRbVoUeawUs%2B6utm1k27vNgY2OiyEIQ%2FBXa4ByBBrxX2a%2Bv%2F2%2F1BFcyB4HPMg9IfrzSShE64NnF9WSdyvQOxMLNc%2BeGX%2Frxzg5Zm3dCt9%2FK%2B6IPJ9fIZpGbEIKqEAgoJs9nyR0BIwbYCDmlmZUxFcx4OvSthxm2hqNm41ed2fS8p7nfNFtbDNxdzt7vpGOiW%2F6Cu5CRqXxqDelPfxIRC&X-Amz-Signature=ec9304e7b1dd3ad4817e7a4098ae62ae61481a9c3a02b6c8422e8d7eba28ce05&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EZCVSGY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFX0iWPoWfj2xxGQyYakwCwltvcwNzrWWfJiaGtgMLBiAiEAmhegQ4HwNbt1OV9Z6Lyyu4siCR7%2FIEG9KFDAd0BhjZ8qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEdXAUrWHQGO0QmTnSrcAy6zu2XIgr%2FYVUR6zFTl0aVgNwM2SFAuEExcjLmOPfIPND2RHt2XG5vfBb6uxbwpQHRnJvjzlFN7gh%2FHcOC032goc%2FX6Cx03JleV1DD%2FZD1N6ofIJnS9Z7yCRdJW1fwNIT4R3LMkj4WnaLbwzGPdQmDi8NMZS2oPm4CMFzUkGrqw%2FTwcUOy%2FOucVEZCemezYA73bFcYHZHXb04A%2F2FAREwG642JngyUh0WF8q2qQIN7r4GTcYnczRHX5QZv31eylJoX8%2FIc7MpDJDUC9kbBSa7VTDiekXgQwhdEpbIo6j3s0NXwDdOIVUf%2FKS%2BhTIBYBEMNEc85AAD5xf4IyraGc7jXd%2FyTT%2B9DO3OeharpWo5YA5oXybdi2%2Bht9BsbveoN3s%2F6wTTsSJboX3pkgily78IfKcLgM1pBoxkF%2F9d%2FqudwrBTIcQA8FBCUMuIQ5RFFCcSrSF%2ByeHPV8t%2B85nAKxIU6SoGgAHv%2FxXYi15MzU9RwS%2BiFZXUw1Jb%2FqdB2RlAewdP%2B%2BLvtRLrv6H3kUq3yZxMptMaeeLLY1ZCpkhpFqyBTu2WAx6%2BZKLFEha06IJKpIPQR%2BNce7yUEIjsCl5MINWhpl4Ymu7Bz9cNPlWVQ3BT8verHZsIBzJfMCIBroMMj%2B57wGOqUBD%2BCBRCdfxbI9AnziOav5WejajJGYyLU%2BgdzHjWoYInZ1l9BRKXHI4GdueyCp%2BNvOSsyXsmaOr14w2hh1RYolnSd%2FQF1O2Wv43n7bU40kK0XxfYvpjCEHkRTsLe1DHfGG5OdJRid4IdnCgfkKpnrIUcFF%2BKlHzYTq00Ebb08RUSVg9NZiKvTmR6uU7OExgtw6dHtJDpBtENmfeNq2jHDlrxDbRefB&X-Amz-Signature=47ab0e79574db9a0c9f7d27658701f83c7233e68993c6282a5dc5405e8e2896d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EZCVSGY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFX0iWPoWfj2xxGQyYakwCwltvcwNzrWWfJiaGtgMLBiAiEAmhegQ4HwNbt1OV9Z6Lyyu4siCR7%2FIEG9KFDAd0BhjZ8qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEdXAUrWHQGO0QmTnSrcAy6zu2XIgr%2FYVUR6zFTl0aVgNwM2SFAuEExcjLmOPfIPND2RHt2XG5vfBb6uxbwpQHRnJvjzlFN7gh%2FHcOC032goc%2FX6Cx03JleV1DD%2FZD1N6ofIJnS9Z7yCRdJW1fwNIT4R3LMkj4WnaLbwzGPdQmDi8NMZS2oPm4CMFzUkGrqw%2FTwcUOy%2FOucVEZCemezYA73bFcYHZHXb04A%2F2FAREwG642JngyUh0WF8q2qQIN7r4GTcYnczRHX5QZv31eylJoX8%2FIc7MpDJDUC9kbBSa7VTDiekXgQwhdEpbIo6j3s0NXwDdOIVUf%2FKS%2BhTIBYBEMNEc85AAD5xf4IyraGc7jXd%2FyTT%2B9DO3OeharpWo5YA5oXybdi2%2Bht9BsbveoN3s%2F6wTTsSJboX3pkgily78IfKcLgM1pBoxkF%2F9d%2FqudwrBTIcQA8FBCUMuIQ5RFFCcSrSF%2ByeHPV8t%2B85nAKxIU6SoGgAHv%2FxXYi15MzU9RwS%2BiFZXUw1Jb%2FqdB2RlAewdP%2B%2BLvtRLrv6H3kUq3yZxMptMaeeLLY1ZCpkhpFqyBTu2WAx6%2BZKLFEha06IJKpIPQR%2BNce7yUEIjsCl5MINWhpl4Ymu7Bz9cNPlWVQ3BT8verHZsIBzJfMCIBroMMj%2B57wGOqUBD%2BCBRCdfxbI9AnziOav5WejajJGYyLU%2BgdzHjWoYInZ1l9BRKXHI4GdueyCp%2BNvOSsyXsmaOr14w2hh1RYolnSd%2FQF1O2Wv43n7bU40kK0XxfYvpjCEHkRTsLe1DHfGG5OdJRid4IdnCgfkKpnrIUcFF%2BKlHzYTq00Ebb08RUSVg9NZiKvTmR6uU7OExgtw6dHtJDpBtENmfeNq2jHDlrxDbRefB&X-Amz-Signature=2800454937fe758def9cd9d6859968545633b1bdd6857bacb5d77a60f23556b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUOZID3U%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDH6FXQ8yYw47AP9RkjdYUekg2tM4%2F8hgQipFX94V3%2FyQIgHBnxmN6JjFtdgsGi98KH9l2rfvSBaTqNAlBN1bx1qKoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCmTKQhmp0Ak%2BOJosSrcA8jdFvz6VSuwN1Vsw3pQMqUbS63e19LGBCWWeaL%2FkN42N2%2BV791psUzv%2FjTKE3J%2BQIxNilrvptBxtaT01DApb03EVsWlKlAC11x9OhFpjEQB4v043AXWDin%2FgeMUufqN%2FBvDcnjR6EcpYuHItqrhbtIf1nIbedTh1mmBuiIfRHdZfkegJRlQT10qFOS%2FGvsYv8AB8UGCd5e19O5GnBFTfldKTDCcW9904AYZmH97S7AQ7t99J4oWglOVABLvI3Ap%2FX5o8WhwQIVM93PspglmERVbIxstD9vnbEt2iR8WFiuJ0kUMxUHo3qNHfYQiDPLZYBiE9%2FK3kNaDHk9MIMhx1J0SLdz4MkahDIjXfEX0wRWAEb49iN1dZuXbbxXV3F%2FvpKwI0e2D6z4BwstJo86xDXbbJJWETbaKhzj2HaaMPXFsa%2FaQsNdvlF7%2FfC7t8Es5JtzM4BR18ZxtKbUlzEMYrz46AogrBO55HozePv6k0YUjkc5UyHiZfYiMfnlzbNdePUgFoavu%2Bwt8y1SOmzYjtfjBCtM2XtcSWqI0JB46kLi6in1vIx0V9gNmBE5x70zrDRRVlOuHfiGyZJpUcUxMKlWeuSAj3aZP8gR2wqKGgKj40ibasiVNw1TkfaxFMMT%2F57wGOqUB%2BFs4afqMvRbVoUeawUs%2B6utm1k27vNgY2OiyEIQ%2FBXa4ByBBrxX2a%2Bv%2F2%2F1BFcyB4HPMg9IfrzSShE64NnF9WSdyvQOxMLNc%2BeGX%2Frxzg5Zm3dCt9%2FK%2B6IPJ9fIZpGbEIKqEAgoJs9nyR0BIwbYCDmlmZUxFcx4OvSthxm2hqNm41ed2fS8p7nfNFtbDNxdzt7vpGOiW%2F6Cu5CRqXxqDelPfxIRC&X-Amz-Signature=37b4607b0518b35d36a66e68f50b8cdd6da34f4d6d95302107d3f1c73f871501&X-Amz-SignedHeaders=host&x-id=GetObject)
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