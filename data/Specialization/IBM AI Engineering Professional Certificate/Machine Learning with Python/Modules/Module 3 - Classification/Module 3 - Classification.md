

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5P23RTD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHLAq99C9S%2FDoyViYDT45TOY%2BOuHia5CIW%2FLjrHoP7ZgAiEA%2FjtwdR5yJ8HcMPmoUve8JzXJ0lyii1qiEhtBdSzy5BoqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEl%2F6lCfkJYGBIavYSrcAzrFZs1kosT9FbE8wG24c3wFyGXB4G6m1wVsPoUfUvd6eQRnnQ36%2FyhkOn39psRfIXjK%2FY7AFxFU%2FnU1MF41%2FM6bMSLW16n8AnI3E0w4OCH4O89zG9kv7jPsXdzJuhdhZ%2F8oywFwE2nusu9yFHyEPi30BxXFDnh7P%2FyEZYE127edfPNuq5mvP2biK%2BhmoF4NkVj3PlglITpm4tdsbf7DrRVXACL2n9NsBsGByHddq%2FX%2FBAqgg8AUUIKrUQB%2BSv0AznWH76qcIHsKYzC%2F3IDbULyUTJMqkfQPcKCflcXJjR%2F6RNF4sRjuMymcJiCGTa%2FdycoetvvTtCvoxmBbEKFamXTyPiF24EPMvQ8GtzGWUwtCBghLkFBxGuTvFvOuU5aQu7O12BqrJiw9hpnE2tT1UNHygx0oONorh2tu3B95AWdnTC51Z18q2HOz%2B0b6eaYEL%2BNgIHuVB7emzseM%2BxaZnkc2hZ2%2BHQ5JSdSUMaSwk6Rp38dmnaB2Zgh1N8hVFz%2FtmEPfOLSJuG0iqOdBeJ%2BDSFTfTCNLq08bNwdAmzlNjOui4EpQaqH%2FErKDWSfaS8o34ZuyxCWmPhCHnHTwIIJDvYRoVd7G73sLULfwF2lFY5lDGdRtjHqoOkXhLSJNMNXh8bwGOqUBw4Sv9oTlhTBHPW7qVeCpjjJLc2CD5wtoSXd0SyQo6U9J5dxLTKECXvy3osHglSVumbmQGOKjR0qtTxKir0HCS%2BJBorPemLXE0VE1tZpigCOuZp3%2BMpO7oydsdp%2B%2Bl7VC%2BwEv0%2BtfZxNnDuIFN1sG%2Ffn0k56WZyQW9fYjZXLCr9xlbC48bJxU%2BXGVJya%2BQuhlXd1vW2bdRMMkPZ5J2XXSfj7ss2bh&X-Amz-Signature=b9d5cc8161ab451d00474bf4d22688239a0cdb93acd01112158b2fef9adbaf8f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5P23RTD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHLAq99C9S%2FDoyViYDT45TOY%2BOuHia5CIW%2FLjrHoP7ZgAiEA%2FjtwdR5yJ8HcMPmoUve8JzXJ0lyii1qiEhtBdSzy5BoqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEl%2F6lCfkJYGBIavYSrcAzrFZs1kosT9FbE8wG24c3wFyGXB4G6m1wVsPoUfUvd6eQRnnQ36%2FyhkOn39psRfIXjK%2FY7AFxFU%2FnU1MF41%2FM6bMSLW16n8AnI3E0w4OCH4O89zG9kv7jPsXdzJuhdhZ%2F8oywFwE2nusu9yFHyEPi30BxXFDnh7P%2FyEZYE127edfPNuq5mvP2biK%2BhmoF4NkVj3PlglITpm4tdsbf7DrRVXACL2n9NsBsGByHddq%2FX%2FBAqgg8AUUIKrUQB%2BSv0AznWH76qcIHsKYzC%2F3IDbULyUTJMqkfQPcKCflcXJjR%2F6RNF4sRjuMymcJiCGTa%2FdycoetvvTtCvoxmBbEKFamXTyPiF24EPMvQ8GtzGWUwtCBghLkFBxGuTvFvOuU5aQu7O12BqrJiw9hpnE2tT1UNHygx0oONorh2tu3B95AWdnTC51Z18q2HOz%2B0b6eaYEL%2BNgIHuVB7emzseM%2BxaZnkc2hZ2%2BHQ5JSdSUMaSwk6Rp38dmnaB2Zgh1N8hVFz%2FtmEPfOLSJuG0iqOdBeJ%2BDSFTfTCNLq08bNwdAmzlNjOui4EpQaqH%2FErKDWSfaS8o34ZuyxCWmPhCHnHTwIIJDvYRoVd7G73sLULfwF2lFY5lDGdRtjHqoOkXhLSJNMNXh8bwGOqUBw4Sv9oTlhTBHPW7qVeCpjjJLc2CD5wtoSXd0SyQo6U9J5dxLTKECXvy3osHglSVumbmQGOKjR0qtTxKir0HCS%2BJBorPemLXE0VE1tZpigCOuZp3%2BMpO7oydsdp%2B%2Bl7VC%2BwEv0%2BtfZxNnDuIFN1sG%2Ffn0k56WZyQW9fYjZXLCr9xlbC48bJxU%2BXGVJya%2BQuhlXd1vW2bdRMMkPZ5J2XXSfj7ss2bh&X-Amz-Signature=8314883915a910ebd9777a5cf4d3b3604798b7b31e7e600bcd4d2a6549d8b9a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5P23RTD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHLAq99C9S%2FDoyViYDT45TOY%2BOuHia5CIW%2FLjrHoP7ZgAiEA%2FjtwdR5yJ8HcMPmoUve8JzXJ0lyii1qiEhtBdSzy5BoqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEl%2F6lCfkJYGBIavYSrcAzrFZs1kosT9FbE8wG24c3wFyGXB4G6m1wVsPoUfUvd6eQRnnQ36%2FyhkOn39psRfIXjK%2FY7AFxFU%2FnU1MF41%2FM6bMSLW16n8AnI3E0w4OCH4O89zG9kv7jPsXdzJuhdhZ%2F8oywFwE2nusu9yFHyEPi30BxXFDnh7P%2FyEZYE127edfPNuq5mvP2biK%2BhmoF4NkVj3PlglITpm4tdsbf7DrRVXACL2n9NsBsGByHddq%2FX%2FBAqgg8AUUIKrUQB%2BSv0AznWH76qcIHsKYzC%2F3IDbULyUTJMqkfQPcKCflcXJjR%2F6RNF4sRjuMymcJiCGTa%2FdycoetvvTtCvoxmBbEKFamXTyPiF24EPMvQ8GtzGWUwtCBghLkFBxGuTvFvOuU5aQu7O12BqrJiw9hpnE2tT1UNHygx0oONorh2tu3B95AWdnTC51Z18q2HOz%2B0b6eaYEL%2BNgIHuVB7emzseM%2BxaZnkc2hZ2%2BHQ5JSdSUMaSwk6Rp38dmnaB2Zgh1N8hVFz%2FtmEPfOLSJuG0iqOdBeJ%2BDSFTfTCNLq08bNwdAmzlNjOui4EpQaqH%2FErKDWSfaS8o34ZuyxCWmPhCHnHTwIIJDvYRoVd7G73sLULfwF2lFY5lDGdRtjHqoOkXhLSJNMNXh8bwGOqUBw4Sv9oTlhTBHPW7qVeCpjjJLc2CD5wtoSXd0SyQo6U9J5dxLTKECXvy3osHglSVumbmQGOKjR0qtTxKir0HCS%2BJBorPemLXE0VE1tZpigCOuZp3%2BMpO7oydsdp%2B%2Bl7VC%2BwEv0%2BtfZxNnDuIFN1sG%2Ffn0k56WZyQW9fYjZXLCr9xlbC48bJxU%2BXGVJya%2BQuhlXd1vW2bdRMMkPZ5J2XXSfj7ss2bh&X-Amz-Signature=a13202b8a767036bd7ce1beb1abf4a3674875b296b851193a3c354e8ff603d64&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KWKHOP7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGGGGInKocrbwWEGzUXG1LpxcW57hjzermwVCoSssBLBAiAMKjVpA7O362vyfZnZkJYLGFMRBfhwetf5q1JBA2nXdCqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHiN7eL%2FJqypGRA8TKtwDVER48VqINKD%2F%2F1TZCWHfX636yaeiawfsankUg9sRkx1FTVp8KSO1ku3K34ZKgddctb03QN5EeqYJkWlQNU53k425YYOIQ4ddw313Zsrczsu5%2FNF1KqssMbfEET69SID1%2BYX19Ti3cchwtSL0TBTLBV0GyoY%2Bt%2BtLbbzsGQZ1oH5OmQbAWZsOe4s6hMc9rPEuYF4oyv2ksBPYQulRHYNp9PHo%2Be%2BtmIV7O3Ume2ZHSiIkS7%2BpqvgjXEP7mtsEp4MmJYgarBWpvex3CGn4Rf8%2FufwPP4hAFpgXLl0PzyGzGB%2B8RWikK4pHPac2VLYNjW1EvtFiocWbwSk%2FA4%2BCpyd9i4pz7E%2BeY7aUNvriDbjoJzyB6CxZ55QeCvZgieLhqPWxFiVQse5JWprIhH31ezXLJ%2FcVGFVsODx%2F7nO8DlbhN66ULfaK2sL55vTXA6Vc090qoUN%2F75e%2FqlQigmo33GrDtjDOvner1FhyEfwxxqzFVZvGrT2vT4JBewS1ASBWV434%2BcLEcPwnZuzwqqYb7zVcX68hvW6fBRUnJg68fgemJNGIJsY%2Fypk1EuyhCKvzqs7PsxdR3BSF6ARytuyu5JKWtFlxPVzhEorFNAEDoyDhIOXZnfTMvzjfEKsWsmAww%2BHxvAY6pgGqyxJttrrooS%2BIoLFE5zYVtscFBLBsCXn3ltrxRA5QSQbMuKTr1F9bTw8YvHoblbfo1M16KE5mkW1RlPL7a00rnbKUdffy%2F%2F7098gmJGjXm1GrcelYSlXjPOkPg0NXBF1q2yGhCFp%2BInNUmZnVRjooBBChxF6KFYo4jEaTE3z0qb4euU8D3lvfMd2wuuVPQXYjn3SrKqsxUrd0Imj8AZwysvjW%2FovH&X-Amz-Signature=2f8d6a7abf99a6f0710f3d62efc974806968be714177bf675e862a6766423e7b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KWKHOP7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGGGGInKocrbwWEGzUXG1LpxcW57hjzermwVCoSssBLBAiAMKjVpA7O362vyfZnZkJYLGFMRBfhwetf5q1JBA2nXdCqIBAi4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHiN7eL%2FJqypGRA8TKtwDVER48VqINKD%2F%2F1TZCWHfX636yaeiawfsankUg9sRkx1FTVp8KSO1ku3K34ZKgddctb03QN5EeqYJkWlQNU53k425YYOIQ4ddw313Zsrczsu5%2FNF1KqssMbfEET69SID1%2BYX19Ti3cchwtSL0TBTLBV0GyoY%2Bt%2BtLbbzsGQZ1oH5OmQbAWZsOe4s6hMc9rPEuYF4oyv2ksBPYQulRHYNp9PHo%2Be%2BtmIV7O3Ume2ZHSiIkS7%2BpqvgjXEP7mtsEp4MmJYgarBWpvex3CGn4Rf8%2FufwPP4hAFpgXLl0PzyGzGB%2B8RWikK4pHPac2VLYNjW1EvtFiocWbwSk%2FA4%2BCpyd9i4pz7E%2BeY7aUNvriDbjoJzyB6CxZ55QeCvZgieLhqPWxFiVQse5JWprIhH31ezXLJ%2FcVGFVsODx%2F7nO8DlbhN66ULfaK2sL55vTXA6Vc090qoUN%2F75e%2FqlQigmo33GrDtjDOvner1FhyEfwxxqzFVZvGrT2vT4JBewS1ASBWV434%2BcLEcPwnZuzwqqYb7zVcX68hvW6fBRUnJg68fgemJNGIJsY%2Fypk1EuyhCKvzqs7PsxdR3BSF6ARytuyu5JKWtFlxPVzhEorFNAEDoyDhIOXZnfTMvzjfEKsWsmAww%2BHxvAY6pgGqyxJttrrooS%2BIoLFE5zYVtscFBLBsCXn3ltrxRA5QSQbMuKTr1F9bTw8YvHoblbfo1M16KE5mkW1RlPL7a00rnbKUdffy%2F%2F7098gmJGjXm1GrcelYSlXjPOkPg0NXBF1q2yGhCFp%2BInNUmZnVRjooBBChxF6KFYo4jEaTE3z0qb4euU8D3lvfMd2wuuVPQXYjn3SrKqsxUrd0Imj8AZwysvjW%2FovH&X-Amz-Signature=e961ea73d6052314cf7280794708b8af0dd815d174f9d01a621fcaa0d7ccd43f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5P23RTD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHLAq99C9S%2FDoyViYDT45TOY%2BOuHia5CIW%2FLjrHoP7ZgAiEA%2FjtwdR5yJ8HcMPmoUve8JzXJ0lyii1qiEhtBdSzy5BoqiAQIuP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEl%2F6lCfkJYGBIavYSrcAzrFZs1kosT9FbE8wG24c3wFyGXB4G6m1wVsPoUfUvd6eQRnnQ36%2FyhkOn39psRfIXjK%2FY7AFxFU%2FnU1MF41%2FM6bMSLW16n8AnI3E0w4OCH4O89zG9kv7jPsXdzJuhdhZ%2F8oywFwE2nusu9yFHyEPi30BxXFDnh7P%2FyEZYE127edfPNuq5mvP2biK%2BhmoF4NkVj3PlglITpm4tdsbf7DrRVXACL2n9NsBsGByHddq%2FX%2FBAqgg8AUUIKrUQB%2BSv0AznWH76qcIHsKYzC%2F3IDbULyUTJMqkfQPcKCflcXJjR%2F6RNF4sRjuMymcJiCGTa%2FdycoetvvTtCvoxmBbEKFamXTyPiF24EPMvQ8GtzGWUwtCBghLkFBxGuTvFvOuU5aQu7O12BqrJiw9hpnE2tT1UNHygx0oONorh2tu3B95AWdnTC51Z18q2HOz%2B0b6eaYEL%2BNgIHuVB7emzseM%2BxaZnkc2hZ2%2BHQ5JSdSUMaSwk6Rp38dmnaB2Zgh1N8hVFz%2FtmEPfOLSJuG0iqOdBeJ%2BDSFTfTCNLq08bNwdAmzlNjOui4EpQaqH%2FErKDWSfaS8o34ZuyxCWmPhCHnHTwIIJDvYRoVd7G73sLULfwF2lFY5lDGdRtjHqoOkXhLSJNMNXh8bwGOqUBw4Sv9oTlhTBHPW7qVeCpjjJLc2CD5wtoSXd0SyQo6U9J5dxLTKECXvy3osHglSVumbmQGOKjR0qtTxKir0HCS%2BJBorPemLXE0VE1tZpigCOuZp3%2BMpO7oydsdp%2B%2Bl7VC%2BwEv0%2BtfZxNnDuIFN1sG%2Ffn0k56WZyQW9fYjZXLCr9xlbC48bJxU%2BXGVJya%2BQuhlXd1vW2bdRMMkPZ5J2XXSfj7ss2bh&X-Amz-Signature=832c47bb97ac17fc97fd2cc2397c7de47c5a0bd4259c29b9baa85669ef1ce0e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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