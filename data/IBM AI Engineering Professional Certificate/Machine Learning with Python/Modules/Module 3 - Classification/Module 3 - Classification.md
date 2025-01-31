

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS4Q2CM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUbf%2FP%2B%2FJZCcyv%2FkQ0Ols92r51%2FmheNEZojf7S2j6YgAiAHV700ouY7NWCY8bhDt0DlS2T9k%2FoAtM5R%2FDXeo8AamSqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvCst7xlwo9PbYVTJKtwDycz7fqU2SWkMGEhkGL%2F6D6ojvpEalLRmSZdfgFUiDJke5hI2aQUbhdvolbhZGgQxVBx3rHjzISn%2BCggcahKB4oPREx0VLbEfqhumv5Hcwa4brL5QAIMCu5ueXvYAt4UBGqMzwwgh5IPzdVeT2IrLWCSfBLly84rMHV6q45ZmO3dIYca1t18ceUIYyzDBiF3XAv6jLUIa9qK%2B0Fr6ZvrMMAXMZaqwgh9k9TfCHzp1SBDstuL3UJolws2V2ETK2o8TYyG7pWtoR%2FHULfaonPr%2BhvimCgQAe4qtMqC2yGyN5w7BW5%2FCZZsAO%2Fibbfyw7hr%2B8wRupRepLQ0QG7QM2JsMXaNBcNFFz0hGclySwZsBVXRCbHN%2F0Wx8QhkN880Zyf512IFg7Qdlu6Yx0E8osgZGgYrzFhmfa%2Bw6rGbpgqOIfQkgpLuv7qiRUErd%2FbicVoOl3Zruonh%2F6LFXRh4%2BiOU32XO8ChXeYpCcrz9cHXrppPnl1qDxRVl9ZPIZTTj4uvXocpiFV732%2BzmN26pgfsdIX9aWYbAuLtnAFVumttxDlvtrdyCZI0xZwXnDlNxmjjVt4PtUiJMHCd3PUkDlDGpRWGutDVTpDdXfXiANrNjMiF6KhmuGLMgPmKU0U2Mwj9v0vAY6pgHJ%2BMhnaN3hX1LD1%2FHTb%2FjHr86dhwK6daYJ5NvNHZ1MT4wkTz4dTky8ljBTw2riwF5Ex1xgn2Qx6l47NHirzRFfRPETu04r4G7W0eA5uKLpaAyczbJKAAypB%2FI4gWvsFQ97SzdqtVAH3BwNux85LAunwVyasVLe7zC%2BkfTq5Mvr59%2F6tECEglweOJIvD6lrzz8cbE6mqnQ6%2BtCYQtPo5iaRFTy%2BfD7d&X-Amz-Signature=ce408f844d7ece40b655647fda89b75c9b1c1d6ea622fc17ff3eeb06f40f047b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS4Q2CM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUbf%2FP%2B%2FJZCcyv%2FkQ0Ols92r51%2FmheNEZojf7S2j6YgAiAHV700ouY7NWCY8bhDt0DlS2T9k%2FoAtM5R%2FDXeo8AamSqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvCst7xlwo9PbYVTJKtwDycz7fqU2SWkMGEhkGL%2F6D6ojvpEalLRmSZdfgFUiDJke5hI2aQUbhdvolbhZGgQxVBx3rHjzISn%2BCggcahKB4oPREx0VLbEfqhumv5Hcwa4brL5QAIMCu5ueXvYAt4UBGqMzwwgh5IPzdVeT2IrLWCSfBLly84rMHV6q45ZmO3dIYca1t18ceUIYyzDBiF3XAv6jLUIa9qK%2B0Fr6ZvrMMAXMZaqwgh9k9TfCHzp1SBDstuL3UJolws2V2ETK2o8TYyG7pWtoR%2FHULfaonPr%2BhvimCgQAe4qtMqC2yGyN5w7BW5%2FCZZsAO%2Fibbfyw7hr%2B8wRupRepLQ0QG7QM2JsMXaNBcNFFz0hGclySwZsBVXRCbHN%2F0Wx8QhkN880Zyf512IFg7Qdlu6Yx0E8osgZGgYrzFhmfa%2Bw6rGbpgqOIfQkgpLuv7qiRUErd%2FbicVoOl3Zruonh%2F6LFXRh4%2BiOU32XO8ChXeYpCcrz9cHXrppPnl1qDxRVl9ZPIZTTj4uvXocpiFV732%2BzmN26pgfsdIX9aWYbAuLtnAFVumttxDlvtrdyCZI0xZwXnDlNxmjjVt4PtUiJMHCd3PUkDlDGpRWGutDVTpDdXfXiANrNjMiF6KhmuGLMgPmKU0U2Mwj9v0vAY6pgHJ%2BMhnaN3hX1LD1%2FHTb%2FjHr86dhwK6daYJ5NvNHZ1MT4wkTz4dTky8ljBTw2riwF5Ex1xgn2Qx6l47NHirzRFfRPETu04r4G7W0eA5uKLpaAyczbJKAAypB%2FI4gWvsFQ97SzdqtVAH3BwNux85LAunwVyasVLe7zC%2BkfTq5Mvr59%2F6tECEglweOJIvD6lrzz8cbE6mqnQ6%2BtCYQtPo5iaRFTy%2BfD7d&X-Amz-Signature=949723752b7e8fd31734f0535d6afc2efe8df48ea1bdab1ffedba33a5a58092e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS4Q2CM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUbf%2FP%2B%2FJZCcyv%2FkQ0Ols92r51%2FmheNEZojf7S2j6YgAiAHV700ouY7NWCY8bhDt0DlS2T9k%2FoAtM5R%2FDXeo8AamSqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvCst7xlwo9PbYVTJKtwDycz7fqU2SWkMGEhkGL%2F6D6ojvpEalLRmSZdfgFUiDJke5hI2aQUbhdvolbhZGgQxVBx3rHjzISn%2BCggcahKB4oPREx0VLbEfqhumv5Hcwa4brL5QAIMCu5ueXvYAt4UBGqMzwwgh5IPzdVeT2IrLWCSfBLly84rMHV6q45ZmO3dIYca1t18ceUIYyzDBiF3XAv6jLUIa9qK%2B0Fr6ZvrMMAXMZaqwgh9k9TfCHzp1SBDstuL3UJolws2V2ETK2o8TYyG7pWtoR%2FHULfaonPr%2BhvimCgQAe4qtMqC2yGyN5w7BW5%2FCZZsAO%2Fibbfyw7hr%2B8wRupRepLQ0QG7QM2JsMXaNBcNFFz0hGclySwZsBVXRCbHN%2F0Wx8QhkN880Zyf512IFg7Qdlu6Yx0E8osgZGgYrzFhmfa%2Bw6rGbpgqOIfQkgpLuv7qiRUErd%2FbicVoOl3Zruonh%2F6LFXRh4%2BiOU32XO8ChXeYpCcrz9cHXrppPnl1qDxRVl9ZPIZTTj4uvXocpiFV732%2BzmN26pgfsdIX9aWYbAuLtnAFVumttxDlvtrdyCZI0xZwXnDlNxmjjVt4PtUiJMHCd3PUkDlDGpRWGutDVTpDdXfXiANrNjMiF6KhmuGLMgPmKU0U2Mwj9v0vAY6pgHJ%2BMhnaN3hX1LD1%2FHTb%2FjHr86dhwK6daYJ5NvNHZ1MT4wkTz4dTky8ljBTw2riwF5Ex1xgn2Qx6l47NHirzRFfRPETu04r4G7W0eA5uKLpaAyczbJKAAypB%2FI4gWvsFQ97SzdqtVAH3BwNux85LAunwVyasVLe7zC%2BkfTq5Mvr59%2F6tECEglweOJIvD6lrzz8cbE6mqnQ6%2BtCYQtPo5iaRFTy%2BfD7d&X-Amz-Signature=1020e6f8a91ffadf7be37223f3ceb2b70f0d31c179a82fdec0159c0831b093d6&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Y4XJK42%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC8XVunGCGmNxSjdAhz%2BN2wGLISnQLVKfkrjWN2%2BcznOAiEA89bUoYPfxfHIC0l907oLeHGC0SXL1Q2dQ%2FETRkZwX%2BoqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXHTD6HEOwoJFr%2FXyrcA59rUCTjWl7c%2FqRUiYaZZCG8UPxERwnLQeLau7AuIyWpnU%2B120PnH3DTg8krDRy%2BPp3%2BDAu5y2Hf78X739WbWYb1HiJj97alyXktryT16smGYOQKG2PFXVPR3tTdT3%2BsswC2t45uWZcfoSu1zhg6nMTv6eQLciVbO4sLuHYJ312Lf5efjv0%2B5zKtGEgqj%2BvxewhJIccjfsYwvqLpqaKnzaEj0DKSO3RdHjAi8KyarQ2Fg87n43s26qLpEYAfJeDAOhodpL10bMefmdkjLT%2FNHLuSAOC3GC4IiQTVboMWl9UYohVGLTow1J%2F77vLwnjtbx9Ude1O7Vw0O5yAg%2FK5nFCEWMavdhpjE4M8a8r6IUqiOJ3EzOCa9aVYzEtqjQ5adC6z5prnpwqdH%2BMHTttCRUD5%2FF5wtIh7u1S6yPZMcZ7xjlVqRuru%2B2CI03u3H4MdK4lhlKdUFZC%2Fzc%2B6WPZIcqpnShx8CeQ8%2BNt8ygGNfsLnXhpF3okWIWiuZvbmXT7E6sBgyBimL3uJKN%2FLCo1HYEWSzzOL2GcZVc2XqryW1wm1vaG91QkBRo%2FHzyog7h9iugfwQL2FdXmNwwsLGOFlDw2EpI0GmkVsN0ROdwpeTSwb1aCv%2B03%2BrB%2F0VMjmyMITc9LwGOqUB5qIIp2LPo3A6Bjqy2E0g%2Blyszw1xy9LFZEdBtPjCs91S%2FXsGAZFufxtJhsdnB6WNJTPh0ksfxwZRaDF0zCpHGFHF7ALTzgmzBfFkO6h6VxsxAGYJsNdTukOsmTOaB7BhSF9bfnbUBRNvrp1pP7BCBfRLmj6fB3FrPu1sHrXTaIeXD1qVNMXjagEC36ZKSJpAeYMgYtwUvyzNu4%2Bac34%2Bm0Pzgsna&X-Amz-Signature=a5b8f3608993b6004c1505249b9879df514b9bcaaa47c8226134db97232d3ecf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Y4XJK42%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC8XVunGCGmNxSjdAhz%2BN2wGLISnQLVKfkrjWN2%2BcznOAiEA89bUoYPfxfHIC0l907oLeHGC0SXL1Q2dQ%2FETRkZwX%2BoqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXHTD6HEOwoJFr%2FXyrcA59rUCTjWl7c%2FqRUiYaZZCG8UPxERwnLQeLau7AuIyWpnU%2B120PnH3DTg8krDRy%2BPp3%2BDAu5y2Hf78X739WbWYb1HiJj97alyXktryT16smGYOQKG2PFXVPR3tTdT3%2BsswC2t45uWZcfoSu1zhg6nMTv6eQLciVbO4sLuHYJ312Lf5efjv0%2B5zKtGEgqj%2BvxewhJIccjfsYwvqLpqaKnzaEj0DKSO3RdHjAi8KyarQ2Fg87n43s26qLpEYAfJeDAOhodpL10bMefmdkjLT%2FNHLuSAOC3GC4IiQTVboMWl9UYohVGLTow1J%2F77vLwnjtbx9Ude1O7Vw0O5yAg%2FK5nFCEWMavdhpjE4M8a8r6IUqiOJ3EzOCa9aVYzEtqjQ5adC6z5prnpwqdH%2BMHTttCRUD5%2FF5wtIh7u1S6yPZMcZ7xjlVqRuru%2B2CI03u3H4MdK4lhlKdUFZC%2Fzc%2B6WPZIcqpnShx8CeQ8%2BNt8ygGNfsLnXhpF3okWIWiuZvbmXT7E6sBgyBimL3uJKN%2FLCo1HYEWSzzOL2GcZVc2XqryW1wm1vaG91QkBRo%2FHzyog7h9iugfwQL2FdXmNwwsLGOFlDw2EpI0GmkVsN0ROdwpeTSwb1aCv%2B03%2BrB%2F0VMjmyMITc9LwGOqUB5qIIp2LPo3A6Bjqy2E0g%2Blyszw1xy9LFZEdBtPjCs91S%2FXsGAZFufxtJhsdnB6WNJTPh0ksfxwZRaDF0zCpHGFHF7ALTzgmzBfFkO6h6VxsxAGYJsNdTukOsmTOaB7BhSF9bfnbUBRNvrp1pP7BCBfRLmj6fB3FrPu1sHrXTaIeXD1qVNMXjagEC36ZKSJpAeYMgYtwUvyzNu4%2Bac34%2Bm0Pzgsna&X-Amz-Signature=93bf496345e0a4db5aeef841baf00df1fe0c98f1180a67d072a6e5b220a2651a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOS4Q2CM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUbf%2FP%2B%2FJZCcyv%2FkQ0Ols92r51%2FmheNEZojf7S2j6YgAiAHV700ouY7NWCY8bhDt0DlS2T9k%2FoAtM5R%2FDXeo8AamSqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvCst7xlwo9PbYVTJKtwDycz7fqU2SWkMGEhkGL%2F6D6ojvpEalLRmSZdfgFUiDJke5hI2aQUbhdvolbhZGgQxVBx3rHjzISn%2BCggcahKB4oPREx0VLbEfqhumv5Hcwa4brL5QAIMCu5ueXvYAt4UBGqMzwwgh5IPzdVeT2IrLWCSfBLly84rMHV6q45ZmO3dIYca1t18ceUIYyzDBiF3XAv6jLUIa9qK%2B0Fr6ZvrMMAXMZaqwgh9k9TfCHzp1SBDstuL3UJolws2V2ETK2o8TYyG7pWtoR%2FHULfaonPr%2BhvimCgQAe4qtMqC2yGyN5w7BW5%2FCZZsAO%2Fibbfyw7hr%2B8wRupRepLQ0QG7QM2JsMXaNBcNFFz0hGclySwZsBVXRCbHN%2F0Wx8QhkN880Zyf512IFg7Qdlu6Yx0E8osgZGgYrzFhmfa%2Bw6rGbpgqOIfQkgpLuv7qiRUErd%2FbicVoOl3Zruonh%2F6LFXRh4%2BiOU32XO8ChXeYpCcrz9cHXrppPnl1qDxRVl9ZPIZTTj4uvXocpiFV732%2BzmN26pgfsdIX9aWYbAuLtnAFVumttxDlvtrdyCZI0xZwXnDlNxmjjVt4PtUiJMHCd3PUkDlDGpRWGutDVTpDdXfXiANrNjMiF6KhmuGLMgPmKU0U2Mwj9v0vAY6pgHJ%2BMhnaN3hX1LD1%2FHTb%2FjHr86dhwK6daYJ5NvNHZ1MT4wkTz4dTky8ljBTw2riwF5Ex1xgn2Qx6l47NHirzRFfRPETu04r4G7W0eA5uKLpaAyczbJKAAypB%2FI4gWvsFQ97SzdqtVAH3BwNux85LAunwVyasVLe7zC%2BkfTq5Mvr59%2F6tECEglweOJIvD6lrzz8cbE6mqnQ6%2BtCYQtPo5iaRFTy%2BfD7d&X-Amz-Signature=ceb937602312c707669344312d472aff83235531c74fc0c964a577c37c5f1953&X-Amz-SignedHeaders=host&x-id=GetObject)
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