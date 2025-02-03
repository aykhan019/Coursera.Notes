

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2KQZSYW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIBs7YuNJG8HsGlom7DDQKB8iUiI0LEU1s096eGAZMlVXAiEA23sYUwYU1nvxBdAm3KWKXtKMSwAx1mE2iK%2BMje9xCmQq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDJzFMHZUAwfOJs8i9ircA4co7L7K%2F6zGHFs936wuRREVwie2X2Jpq1kc7mQTQsVxcPJmnKEaiKx2UeFhiv%2FRJBZM6e3NeEZKQ9xQPPzygM4e8gDtB%2Fv5a3EU5qmbOVCyJOCshhArRkBDbrTGzik%2BVquWNuwKNerhIOqgPj8Dr91q43051Cn5eeq3LCX5z31a7A2LgXV9GVxP5pfLGHF2h1Gcq2O0oyI6NT9c58p90pfLHIUfErPaQoWfUeTz3F0zd3TQhZaYBKxu1AuebeMTMSOwvniiO1GAUkn3aUDb1FiYKhHG15dx6Imn2zqKR8f939YOS%2FRfI40%2Bu7mv5WZK70fk3twrY%2BdB8G5VmLDtQS0JC18CDOSLSYKsPXIOGchVk6xf4jpPuL6Gqc8UqGHNwF8roISBTl1xxWZFSUUvduWQNdg%2BS%2FxPmCcfK2ySjTjBhy9GpDIMIzkOTdk0GUoCt58yUTLWqIFVj7IiKwTNynfF%2F8VQHcVXV%2F1Sexf5QCCocV0H8jNU0CIuXSXsKwCSfWSHNuaAULM%2B%2Fj9gkKeoBGZvgZWzowVa54cLNvNEYM1oWV6aUbsod8Y5VPz3%2FosVmpqppFjTEUd8nr5TqMWWajp33xwfOktpJdgrWUXnEyrC0xjE0e5qo0UKq9m3MIKihL0GOqUBENpJrnIbxGVjuj8IVLOzdPiEvBwcaOaIGJ7jTDRpAfufGN%2F9n26zqgJ5yqB%2FZ65fPtJ7sDg0q2alhzkEoIospKMSDkM44cEu52U87rnPpldlXNss08SYaFderevf6683zAiq8xkSzJ9aflFb3oKXFgG%2BOBD51%2BKz%2FrgPQy3A6U1knX%2FN9ksGrfVPDYnkQuOksQnR8GlaJS2uY1QQll3RW17Vbpwg&X-Amz-Signature=7ea6fc456b75425ae92b80ad749cd23f983152329eea60afa7492966fe884d7d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2KQZSYW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIBs7YuNJG8HsGlom7DDQKB8iUiI0LEU1s096eGAZMlVXAiEA23sYUwYU1nvxBdAm3KWKXtKMSwAx1mE2iK%2BMje9xCmQq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDJzFMHZUAwfOJs8i9ircA4co7L7K%2F6zGHFs936wuRREVwie2X2Jpq1kc7mQTQsVxcPJmnKEaiKx2UeFhiv%2FRJBZM6e3NeEZKQ9xQPPzygM4e8gDtB%2Fv5a3EU5qmbOVCyJOCshhArRkBDbrTGzik%2BVquWNuwKNerhIOqgPj8Dr91q43051Cn5eeq3LCX5z31a7A2LgXV9GVxP5pfLGHF2h1Gcq2O0oyI6NT9c58p90pfLHIUfErPaQoWfUeTz3F0zd3TQhZaYBKxu1AuebeMTMSOwvniiO1GAUkn3aUDb1FiYKhHG15dx6Imn2zqKR8f939YOS%2FRfI40%2Bu7mv5WZK70fk3twrY%2BdB8G5VmLDtQS0JC18CDOSLSYKsPXIOGchVk6xf4jpPuL6Gqc8UqGHNwF8roISBTl1xxWZFSUUvduWQNdg%2BS%2FxPmCcfK2ySjTjBhy9GpDIMIzkOTdk0GUoCt58yUTLWqIFVj7IiKwTNynfF%2F8VQHcVXV%2F1Sexf5QCCocV0H8jNU0CIuXSXsKwCSfWSHNuaAULM%2B%2Fj9gkKeoBGZvgZWzowVa54cLNvNEYM1oWV6aUbsod8Y5VPz3%2FosVmpqppFjTEUd8nr5TqMWWajp33xwfOktpJdgrWUXnEyrC0xjE0e5qo0UKq9m3MIKihL0GOqUBENpJrnIbxGVjuj8IVLOzdPiEvBwcaOaIGJ7jTDRpAfufGN%2F9n26zqgJ5yqB%2FZ65fPtJ7sDg0q2alhzkEoIospKMSDkM44cEu52U87rnPpldlXNss08SYaFderevf6683zAiq8xkSzJ9aflFb3oKXFgG%2BOBD51%2BKz%2FrgPQy3A6U1knX%2FN9ksGrfVPDYnkQuOksQnR8GlaJS2uY1QQll3RW17Vbpwg&X-Amz-Signature=1faab0a5f72a8695816793cbbf8549c7f945945fc27c2ca1107b83a9cefd70b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2KQZSYW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIBs7YuNJG8HsGlom7DDQKB8iUiI0LEU1s096eGAZMlVXAiEA23sYUwYU1nvxBdAm3KWKXtKMSwAx1mE2iK%2BMje9xCmQq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDJzFMHZUAwfOJs8i9ircA4co7L7K%2F6zGHFs936wuRREVwie2X2Jpq1kc7mQTQsVxcPJmnKEaiKx2UeFhiv%2FRJBZM6e3NeEZKQ9xQPPzygM4e8gDtB%2Fv5a3EU5qmbOVCyJOCshhArRkBDbrTGzik%2BVquWNuwKNerhIOqgPj8Dr91q43051Cn5eeq3LCX5z31a7A2LgXV9GVxP5pfLGHF2h1Gcq2O0oyI6NT9c58p90pfLHIUfErPaQoWfUeTz3F0zd3TQhZaYBKxu1AuebeMTMSOwvniiO1GAUkn3aUDb1FiYKhHG15dx6Imn2zqKR8f939YOS%2FRfI40%2Bu7mv5WZK70fk3twrY%2BdB8G5VmLDtQS0JC18CDOSLSYKsPXIOGchVk6xf4jpPuL6Gqc8UqGHNwF8roISBTl1xxWZFSUUvduWQNdg%2BS%2FxPmCcfK2ySjTjBhy9GpDIMIzkOTdk0GUoCt58yUTLWqIFVj7IiKwTNynfF%2F8VQHcVXV%2F1Sexf5QCCocV0H8jNU0CIuXSXsKwCSfWSHNuaAULM%2B%2Fj9gkKeoBGZvgZWzowVa54cLNvNEYM1oWV6aUbsod8Y5VPz3%2FosVmpqppFjTEUd8nr5TqMWWajp33xwfOktpJdgrWUXnEyrC0xjE0e5qo0UKq9m3MIKihL0GOqUBENpJrnIbxGVjuj8IVLOzdPiEvBwcaOaIGJ7jTDRpAfufGN%2F9n26zqgJ5yqB%2FZ65fPtJ7sDg0q2alhzkEoIospKMSDkM44cEu52U87rnPpldlXNss08SYaFderevf6683zAiq8xkSzJ9aflFb3oKXFgG%2BOBD51%2BKz%2FrgPQy3A6U1knX%2FN9ksGrfVPDYnkQuOksQnR8GlaJS2uY1QQll3RW17Vbpwg&X-Amz-Signature=79764a740355bfe357196a6f48f712549cec241129640d01953006fc2365a4c6&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IEWNPAK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCICS%2Brz64EgRRCzlh1pHaduLE7FPnwoNACJSmDDhkzRUYAiAhkewmzRevc7tuaP6Jy7ZpyoAeq%2By2F1IhcnX7dSZrESr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIM%2BhFh0GVP5evh396%2FKtwDnNExNWJN3vm3wSwy%2BRX%2B9waEAU10ZZL5m9KSshWTEA0JT58Y4fqg2ampAYjQG86TPW2ziFRKvg11cEERWdEQQXaS6SY8tl3NPTrwVgEEep6phhePaMeCvWQe1LPsYqUp5D0im63rDBNxEdXGCu%2FPz9fZFtk3RpJr4RdlBi2w2D7PjUMn6W2hSqrH2LtcBYWFuLNRQrYfhXt7YUid6JHIlXqeR5ttedk1BhwA%2FjvVU%2FbAfKCoGJNkgB2%2FOTYa4tm4VsV2OtSmr1xQ5y9IeXdyWj%2B%2Fsu%2Bg0kT5xitTQQQBfzl6CZIhq%2FWjaOfmLJ%2BP%2Fe%2FIuADZDFrtZFc%2FpevBfEAd%2FIEyuhJxgPfOSZ5rFNKSWcMXwPoWCmzTC1wYZP6cPFzgZrWmFPw%2BUIB%2Bdg8miWz1OJMFnzhrlIQcG9ZofyAfOkdx%2FcTE%2BNvylemL2jFvzVc1WsG4iTVyJ%2FAaOSpDPG1dzzgHhpffJ0TbEZe%2FTiiJngNJZFsUoUfuYjXVjdl5cI0I%2BsLCyE1Wrx3gfvi1Kl0PQaUaglhZqIEoB5l3wtYsVoWwJcrdtMH5mYQIM8vVFuU4E0veWo%2FEfpKNtoc2j%2Bs6%2BRhsgTaJaVLZbrneY4OJTPPianDWg2x%2B48YpqtcwraKEvQY6pgFxG6TleXZN3XKQlIE8RdIeyXrvG08a2%2FciPPE18vMD3OBx0uy179%2BBSULdcQm1S5ZMMEmbObjfszLqhRXqk4uMfUN1xGMNW4vs%2FWgw2K5WrcPpLoUJDMEhK4%2F1RqyXvbOqXa1mIQPGt%2F4LrihriZKp0qj0sn0TySrsJoKQufFSi3UyCA3Z6IFUDAxz4aDzVSiWUZWd7FwFovn%2BiwVS5CmpyT8wUcxk&X-Amz-Signature=c767a459e98d7bd5f16f1960accdbff5c981b485ad55cca16bd3d87ac85becc1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IEWNPAK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCICS%2Brz64EgRRCzlh1pHaduLE7FPnwoNACJSmDDhkzRUYAiAhkewmzRevc7tuaP6Jy7ZpyoAeq%2By2F1IhcnX7dSZrESr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIM%2BhFh0GVP5evh396%2FKtwDnNExNWJN3vm3wSwy%2BRX%2B9waEAU10ZZL5m9KSshWTEA0JT58Y4fqg2ampAYjQG86TPW2ziFRKvg11cEERWdEQQXaS6SY8tl3NPTrwVgEEep6phhePaMeCvWQe1LPsYqUp5D0im63rDBNxEdXGCu%2FPz9fZFtk3RpJr4RdlBi2w2D7PjUMn6W2hSqrH2LtcBYWFuLNRQrYfhXt7YUid6JHIlXqeR5ttedk1BhwA%2FjvVU%2FbAfKCoGJNkgB2%2FOTYa4tm4VsV2OtSmr1xQ5y9IeXdyWj%2B%2Fsu%2Bg0kT5xitTQQQBfzl6CZIhq%2FWjaOfmLJ%2BP%2Fe%2FIuADZDFrtZFc%2FpevBfEAd%2FIEyuhJxgPfOSZ5rFNKSWcMXwPoWCmzTC1wYZP6cPFzgZrWmFPw%2BUIB%2Bdg8miWz1OJMFnzhrlIQcG9ZofyAfOkdx%2FcTE%2BNvylemL2jFvzVc1WsG4iTVyJ%2FAaOSpDPG1dzzgHhpffJ0TbEZe%2FTiiJngNJZFsUoUfuYjXVjdl5cI0I%2BsLCyE1Wrx3gfvi1Kl0PQaUaglhZqIEoB5l3wtYsVoWwJcrdtMH5mYQIM8vVFuU4E0veWo%2FEfpKNtoc2j%2Bs6%2BRhsgTaJaVLZbrneY4OJTPPianDWg2x%2B48YpqtcwraKEvQY6pgFxG6TleXZN3XKQlIE8RdIeyXrvG08a2%2FciPPE18vMD3OBx0uy179%2BBSULdcQm1S5ZMMEmbObjfszLqhRXqk4uMfUN1xGMNW4vs%2FWgw2K5WrcPpLoUJDMEhK4%2F1RqyXvbOqXa1mIQPGt%2F4LrihriZKp0qj0sn0TySrsJoKQufFSi3UyCA3Z6IFUDAxz4aDzVSiWUZWd7FwFovn%2BiwVS5CmpyT8wUcxk&X-Amz-Signature=8008df9bdf445eb8f0f6111868beb9635ac28d3afe4e2bcfa150eb86265a8133&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2KQZSYW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIBs7YuNJG8HsGlom7DDQKB8iUiI0LEU1s096eGAZMlVXAiEA23sYUwYU1nvxBdAm3KWKXtKMSwAx1mE2iK%2BMje9xCmQq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDJzFMHZUAwfOJs8i9ircA4co7L7K%2F6zGHFs936wuRREVwie2X2Jpq1kc7mQTQsVxcPJmnKEaiKx2UeFhiv%2FRJBZM6e3NeEZKQ9xQPPzygM4e8gDtB%2Fv5a3EU5qmbOVCyJOCshhArRkBDbrTGzik%2BVquWNuwKNerhIOqgPj8Dr91q43051Cn5eeq3LCX5z31a7A2LgXV9GVxP5pfLGHF2h1Gcq2O0oyI6NT9c58p90pfLHIUfErPaQoWfUeTz3F0zd3TQhZaYBKxu1AuebeMTMSOwvniiO1GAUkn3aUDb1FiYKhHG15dx6Imn2zqKR8f939YOS%2FRfI40%2Bu7mv5WZK70fk3twrY%2BdB8G5VmLDtQS0JC18CDOSLSYKsPXIOGchVk6xf4jpPuL6Gqc8UqGHNwF8roISBTl1xxWZFSUUvduWQNdg%2BS%2FxPmCcfK2ySjTjBhy9GpDIMIzkOTdk0GUoCt58yUTLWqIFVj7IiKwTNynfF%2F8VQHcVXV%2F1Sexf5QCCocV0H8jNU0CIuXSXsKwCSfWSHNuaAULM%2B%2Fj9gkKeoBGZvgZWzowVa54cLNvNEYM1oWV6aUbsod8Y5VPz3%2FosVmpqppFjTEUd8nr5TqMWWajp33xwfOktpJdgrWUXnEyrC0xjE0e5qo0UKq9m3MIKihL0GOqUBENpJrnIbxGVjuj8IVLOzdPiEvBwcaOaIGJ7jTDRpAfufGN%2F9n26zqgJ5yqB%2FZ65fPtJ7sDg0q2alhzkEoIospKMSDkM44cEu52U87rnPpldlXNss08SYaFderevf6683zAiq8xkSzJ9aflFb3oKXFgG%2BOBD51%2BKz%2FrgPQy3A6U1knX%2FN9ksGrfVPDYnkQuOksQnR8GlaJS2uY1QQll3RW17Vbpwg&X-Amz-Signature=cd49158f1c27149c04d94781e648a9af8105f6eaee064e4a653926da256865ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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