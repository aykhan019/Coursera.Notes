

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQD3IW5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQD%2Fx3aB6W04OvFL7FcKy%2FDdzx6qMoCAArhHo3d4W%2FrIAAIhAMFUf9U9TYM0PcdHZ%2FLrDSr8PpzgA6gPEhwAilU4WKAuKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEhFPdQ6r4pfgCcj0q3ANW3v6eA47E3p%2BTPwUiNce3gHqh4PfdPW8VbVIAsiHt99ISa2TJkVLoBAoStBNFfSnxKxO%2BaZ%2FY1wkdpN9Oo3%2BfocCoP%2BA98K%2BX0vFa%2Ft1EvT%2FCdvftlgYGsUH1be8L4m3Gv%2BIUfGms%2BIP8vUf9dKMliaUh4rYhM68EqH9NhjaPR7ok2nNXX%2FS333%2BrGU1aJe2v9nDguppmXNepqol4TkjXB1lBrgX%2FZjqpQ80hWOYMetOMx2JwwI5807LkA09BrchZiUWuKrkWWX6m3yLQe%2BzvjyBnJ4Q%2F1pa0FsakzJ%2BREWpTDuQJpY%2F%2FHpF4aEq7ZfTcpGfxEp%2FHn%2Fml2BtKqos4X7rPaq1aNPsE%2FaVJRHG%2FGUt6YH3v0VkDwguE0t27wXyv5lnhWUGm4KIYFFOJw6XKYP7EM7gsOVaXQ9LG7zC%2Bmc2QFy%2F36kzAE6tmgaZqg7%2B3ZQAzew%2BQZ7%2FU3pGLZvh4FXx2RrAIx1EPAyaS7CK0eSHYEeIptQDr927ONX2%2BD4HK5mlYhyRjj4c5zR%2BXSJIwXxabxV85N57oCmlR1x5nOzPf3%2BpR7RoeViogto0pUCrrZFphi7UwoorlD1MDukdl03YR4wRTu8lzFlNTMd13i090UQ1y8fQ4tWqTATDxzIq9BjqkAbhtpfRMAivShwfqWnsCqu%2BQoR%2BaZzu49YOXG20Q9LlFyVUEArVeIfWGEo86COROJvuPXASktN5UzxyXaCvsFWc6Qk6SSj1Hbded47pwlvQZbpCDVJRSbfM66Eb0MiT4P2WHQtlrLsBIbDy7H3jiPtu1zioWz1%2B9tXFbk6hPR6Zlly24Yp2qbVcKbWMD8s1Qh9usRfokEzAm%2BaY955O%2FhW4T%2BQjd&X-Amz-Signature=e1fd7a7b1b451ea1c27501e2958c37bc4a64ca62656fe2c518c926d43e66fbe4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQD3IW5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQD%2Fx3aB6W04OvFL7FcKy%2FDdzx6qMoCAArhHo3d4W%2FrIAAIhAMFUf9U9TYM0PcdHZ%2FLrDSr8PpzgA6gPEhwAilU4WKAuKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEhFPdQ6r4pfgCcj0q3ANW3v6eA47E3p%2BTPwUiNce3gHqh4PfdPW8VbVIAsiHt99ISa2TJkVLoBAoStBNFfSnxKxO%2BaZ%2FY1wkdpN9Oo3%2BfocCoP%2BA98K%2BX0vFa%2Ft1EvT%2FCdvftlgYGsUH1be8L4m3Gv%2BIUfGms%2BIP8vUf9dKMliaUh4rYhM68EqH9NhjaPR7ok2nNXX%2FS333%2BrGU1aJe2v9nDguppmXNepqol4TkjXB1lBrgX%2FZjqpQ80hWOYMetOMx2JwwI5807LkA09BrchZiUWuKrkWWX6m3yLQe%2BzvjyBnJ4Q%2F1pa0FsakzJ%2BREWpTDuQJpY%2F%2FHpF4aEq7ZfTcpGfxEp%2FHn%2Fml2BtKqos4X7rPaq1aNPsE%2FaVJRHG%2FGUt6YH3v0VkDwguE0t27wXyv5lnhWUGm4KIYFFOJw6XKYP7EM7gsOVaXQ9LG7zC%2Bmc2QFy%2F36kzAE6tmgaZqg7%2B3ZQAzew%2BQZ7%2FU3pGLZvh4FXx2RrAIx1EPAyaS7CK0eSHYEeIptQDr927ONX2%2BD4HK5mlYhyRjj4c5zR%2BXSJIwXxabxV85N57oCmlR1x5nOzPf3%2BpR7RoeViogto0pUCrrZFphi7UwoorlD1MDukdl03YR4wRTu8lzFlNTMd13i090UQ1y8fQ4tWqTATDxzIq9BjqkAbhtpfRMAivShwfqWnsCqu%2BQoR%2BaZzu49YOXG20Q9LlFyVUEArVeIfWGEo86COROJvuPXASktN5UzxyXaCvsFWc6Qk6SSj1Hbded47pwlvQZbpCDVJRSbfM66Eb0MiT4P2WHQtlrLsBIbDy7H3jiPtu1zioWz1%2B9tXFbk6hPR6Zlly24Yp2qbVcKbWMD8s1Qh9usRfokEzAm%2BaY955O%2FhW4T%2BQjd&X-Amz-Signature=0625a3ffd13b6f4d9e86c19f2e55235a5052ee11a671cae3b3d83a5c7908dbad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQD3IW5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQD%2Fx3aB6W04OvFL7FcKy%2FDdzx6qMoCAArhHo3d4W%2FrIAAIhAMFUf9U9TYM0PcdHZ%2FLrDSr8PpzgA6gPEhwAilU4WKAuKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEhFPdQ6r4pfgCcj0q3ANW3v6eA47E3p%2BTPwUiNce3gHqh4PfdPW8VbVIAsiHt99ISa2TJkVLoBAoStBNFfSnxKxO%2BaZ%2FY1wkdpN9Oo3%2BfocCoP%2BA98K%2BX0vFa%2Ft1EvT%2FCdvftlgYGsUH1be8L4m3Gv%2BIUfGms%2BIP8vUf9dKMliaUh4rYhM68EqH9NhjaPR7ok2nNXX%2FS333%2BrGU1aJe2v9nDguppmXNepqol4TkjXB1lBrgX%2FZjqpQ80hWOYMetOMx2JwwI5807LkA09BrchZiUWuKrkWWX6m3yLQe%2BzvjyBnJ4Q%2F1pa0FsakzJ%2BREWpTDuQJpY%2F%2FHpF4aEq7ZfTcpGfxEp%2FHn%2Fml2BtKqos4X7rPaq1aNPsE%2FaVJRHG%2FGUt6YH3v0VkDwguE0t27wXyv5lnhWUGm4KIYFFOJw6XKYP7EM7gsOVaXQ9LG7zC%2Bmc2QFy%2F36kzAE6tmgaZqg7%2B3ZQAzew%2BQZ7%2FU3pGLZvh4FXx2RrAIx1EPAyaS7CK0eSHYEeIptQDr927ONX2%2BD4HK5mlYhyRjj4c5zR%2BXSJIwXxabxV85N57oCmlR1x5nOzPf3%2BpR7RoeViogto0pUCrrZFphi7UwoorlD1MDukdl03YR4wRTu8lzFlNTMd13i090UQ1y8fQ4tWqTATDxzIq9BjqkAbhtpfRMAivShwfqWnsCqu%2BQoR%2BaZzu49YOXG20Q9LlFyVUEArVeIfWGEo86COROJvuPXASktN5UzxyXaCvsFWc6Qk6SSj1Hbded47pwlvQZbpCDVJRSbfM66Eb0MiT4P2WHQtlrLsBIbDy7H3jiPtu1zioWz1%2B9tXFbk6hPR6Zlly24Yp2qbVcKbWMD8s1Qh9usRfokEzAm%2BaY955O%2FhW4T%2BQjd&X-Amz-Signature=80e4e0738c63a3e99957f1926249560aff5e6b3d2cd35d379c952831c704a034&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEV4I7JU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDO6WutnIo9teMHr%2BHJxp2jSFmdv2kGHCCeae4LPMOH5gIhAPz7tI0sx2UwVZ8FyYXm8rw6eDJZi6Zd1OCM9DXx8P7JKv8DCDkQABoMNjM3NDIzMTgzODA1IgwwFnZpXjgk6CdlDz0q3AP0PsZnbDfuj%2BOdWI7naWuBwy6VcrWH8oiQl13kb4O3tp1BcBx9kSjWVWAv10SeKWfcxbzsG7yaSQzRBkW74x9Btvc%2BoX2mtSV2P2zumsJ30wpHBg%2FKa1%2Fi3wImB7Xa6oQJpKedy7j%2BiKITDZiICsl7PHpRkB%2FMevuww75K9rgV55WqXNC8Nu9hxu%2FMzUOsArATWVNiTYIhQ7KHGapzrtmCaYCspPIHM%2BWeZGAOcoo0FvDiVIKx9JXbXuaMFsdQK4P1bUutFqM%2F%2BOgNPJrJvA5ZwHVDyQNxYRqyM1IbhNYQOZflBdV9UpoSKarrDLW1VkHOOLx5unKyKFaCaqhEczhm8K1rAlXLZuSOzyeDJj4VdB3kE%2FwjVvx%2FfeKAzkmuIz8GYKZOZbrPnCYHnTt3vocDcGMkh8lFoRqwxwPWkB1BN27qBCVDZQ4HJGmaujvwNXunUYXtSltbdgXP3dwUW5xf9w6u6zsF87m0UIjgEg2ODuFO1HzDJOGdbISyTiSqPTeZ%2BVsVtGy7PZBFHe6Jt9wLOne0ouTzdr1iNxsIU5MJ0cvsvfXghzNWDfSEUMvCwIOcessQoBx98qQmljc%2FOs4sGqfDHSTa22cPPT7TlVLYsb71%2BNbVgpw6%2B%2FQK4DDnzIq9BjqkAcaBf3yTj2QdW8B8PhV4ygkTRbWAFgomdt3QPLUYqQ5RBZTgiPvHRIZQ74s7ekjBR9x1bVJBqm55pM3y%2B5rOz2XMleqO4AOOKCVZCog6WBUoQt4aj33iOpvfa8Ug%2FQ%2BIUa3YTAV54oMKBetXyja5%2FndSXO%2Foj2FQA8NZarlKUXznxylAaeVSTIeWeLlKWNLDwr%2FK4HSa3N0RYDYaSc2koHX5hnDk&X-Amz-Signature=f837f5c77968b412ab68ced311afee3fd6a18c65104f3ca539354427673163b4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEV4I7JU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDO6WutnIo9teMHr%2BHJxp2jSFmdv2kGHCCeae4LPMOH5gIhAPz7tI0sx2UwVZ8FyYXm8rw6eDJZi6Zd1OCM9DXx8P7JKv8DCDkQABoMNjM3NDIzMTgzODA1IgwwFnZpXjgk6CdlDz0q3AP0PsZnbDfuj%2BOdWI7naWuBwy6VcrWH8oiQl13kb4O3tp1BcBx9kSjWVWAv10SeKWfcxbzsG7yaSQzRBkW74x9Btvc%2BoX2mtSV2P2zumsJ30wpHBg%2FKa1%2Fi3wImB7Xa6oQJpKedy7j%2BiKITDZiICsl7PHpRkB%2FMevuww75K9rgV55WqXNC8Nu9hxu%2FMzUOsArATWVNiTYIhQ7KHGapzrtmCaYCspPIHM%2BWeZGAOcoo0FvDiVIKx9JXbXuaMFsdQK4P1bUutFqM%2F%2BOgNPJrJvA5ZwHVDyQNxYRqyM1IbhNYQOZflBdV9UpoSKarrDLW1VkHOOLx5unKyKFaCaqhEczhm8K1rAlXLZuSOzyeDJj4VdB3kE%2FwjVvx%2FfeKAzkmuIz8GYKZOZbrPnCYHnTt3vocDcGMkh8lFoRqwxwPWkB1BN27qBCVDZQ4HJGmaujvwNXunUYXtSltbdgXP3dwUW5xf9w6u6zsF87m0UIjgEg2ODuFO1HzDJOGdbISyTiSqPTeZ%2BVsVtGy7PZBFHe6Jt9wLOne0ouTzdr1iNxsIU5MJ0cvsvfXghzNWDfSEUMvCwIOcessQoBx98qQmljc%2FOs4sGqfDHSTa22cPPT7TlVLYsb71%2BNbVgpw6%2B%2FQK4DDnzIq9BjqkAcaBf3yTj2QdW8B8PhV4ygkTRbWAFgomdt3QPLUYqQ5RBZTgiPvHRIZQ74s7ekjBR9x1bVJBqm55pM3y%2B5rOz2XMleqO4AOOKCVZCog6WBUoQt4aj33iOpvfa8Ug%2FQ%2BIUa3YTAV54oMKBetXyja5%2FndSXO%2Foj2FQA8NZarlKUXznxylAaeVSTIeWeLlKWNLDwr%2FK4HSa3N0RYDYaSc2koHX5hnDk&X-Amz-Signature=4fbf9786222d1fcbc6a3b93308528b7965cf6d5f0db9b6f213e5c1ab04436ab4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQD3IW5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQD%2Fx3aB6W04OvFL7FcKy%2FDdzx6qMoCAArhHo3d4W%2FrIAAIhAMFUf9U9TYM0PcdHZ%2FLrDSr8PpzgA6gPEhwAilU4WKAuKv8DCDkQABoMNjM3NDIzMTgzODA1IgyEhFPdQ6r4pfgCcj0q3ANW3v6eA47E3p%2BTPwUiNce3gHqh4PfdPW8VbVIAsiHt99ISa2TJkVLoBAoStBNFfSnxKxO%2BaZ%2FY1wkdpN9Oo3%2BfocCoP%2BA98K%2BX0vFa%2Ft1EvT%2FCdvftlgYGsUH1be8L4m3Gv%2BIUfGms%2BIP8vUf9dKMliaUh4rYhM68EqH9NhjaPR7ok2nNXX%2FS333%2BrGU1aJe2v9nDguppmXNepqol4TkjXB1lBrgX%2FZjqpQ80hWOYMetOMx2JwwI5807LkA09BrchZiUWuKrkWWX6m3yLQe%2BzvjyBnJ4Q%2F1pa0FsakzJ%2BREWpTDuQJpY%2F%2FHpF4aEq7ZfTcpGfxEp%2FHn%2Fml2BtKqos4X7rPaq1aNPsE%2FaVJRHG%2FGUt6YH3v0VkDwguE0t27wXyv5lnhWUGm4KIYFFOJw6XKYP7EM7gsOVaXQ9LG7zC%2Bmc2QFy%2F36kzAE6tmgaZqg7%2B3ZQAzew%2BQZ7%2FU3pGLZvh4FXx2RrAIx1EPAyaS7CK0eSHYEeIptQDr927ONX2%2BD4HK5mlYhyRjj4c5zR%2BXSJIwXxabxV85N57oCmlR1x5nOzPf3%2BpR7RoeViogto0pUCrrZFphi7UwoorlD1MDukdl03YR4wRTu8lzFlNTMd13i090UQ1y8fQ4tWqTATDxzIq9BjqkAbhtpfRMAivShwfqWnsCqu%2BQoR%2BaZzu49YOXG20Q9LlFyVUEArVeIfWGEo86COROJvuPXASktN5UzxyXaCvsFWc6Qk6SSj1Hbded47pwlvQZbpCDVJRSbfM66Eb0MiT4P2WHQtlrLsBIbDy7H3jiPtu1zioWz1%2B9tXFbk6hPR6Zlly24Yp2qbVcKbWMD8s1Qh9usRfokEzAm%2BaY955O%2FhW4T%2BQjd&X-Amz-Signature=338b4b78190337c94dee61297dfa262c36da05441ff02848592e1da3caf6c519&X-Amz-SignedHeaders=host&x-id=GetObject)
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