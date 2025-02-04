

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAYVGT2H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIGKJwmSMgHnjPUKdQeyYv7k87iXVt%2BF4Hv3lUScgKQBBAiBs%2FPgn35TEB7SpNoMFUjjZbL9zTPuVHYiFpr9neoCgmyr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMlga92UKDlNnLxuU6KtwDoMswhHpOAUaDK%2Ff9JpXZEQi0K%2FAxSyIegw%2F7XsJrItqh0%2FsJUJdJ3ttV7NXWSIQUrpGf4d0L2gEn1IzuhckPmwCT266GWGhg6VLD7urDRZ5k54SjRfTF1I7OJ9wEgFCW%2FwsVMMVyDCH3ps1h10COsd%2F7%2BGTcZHr88Xi7r1CzcmRXzFWi1ye7cJru0yLzknTZUg2R%2BVTtmr7aJLJlaeyB7BEywSCh89KgE11BZWmQszs5kPFHPYzUvstAuSEWCm1BBmjaFItlOBxg0qU6hUYUbsCLWS42c96TyZziyUPxOrNn3bGWu68CviLG%2FzcVGGJzcsst9MVFfxorEOYsFZgCgQ5jb2by0vGXipWujPi3tnTyyuv4cuRnYTASaRi96h34sr0w0DOOoDuptUAprpnYRn5wxHhbyazp3n5xIIAj6TTCMQ%2BP5PZymIt%2Bu3%2FO%2ByP2JspbITmQmTOWGG7ofxIB41KTmhKuwgj6%2BkdP3Qq5DLtS%2BvESvPfJ2ZGnYQQ%2Beno4NQ2fbRQcB7%2BHlYqswTTlLiMgjhk1mgGauB7TNHl%2BN%2BByw%2BA5KIBltJy6XCgVcrE4SWTwhiEE272jPX1eZ06TSjygxUNfoDPWzeMM%2B1ZLui5DrrINQD9bFHZqdqkwroKIvQY6pgGSwnIRjx53zFat8u%2Bj5Uo5uODiuytJI7dNoOJhLQtUiWelogxG%2FUCcKZfB36%2BWpfr%2F8Hz517%2FZHIV2yay%2FiqEfxw1o2KJqT2pYudDllMXLbrlLO%2FoWKzTmpVJMKV%2Ba0zv0IkB5%2BAyqMhqz3wyCivyx0Fts%2BnLBncV1wBxoF6Ts8u5X4E9M2MS14X4TCXqCW8W6OidhAktCHSpCweUa94de1KjEs6%2Bu&X-Amz-Signature=81b3fcfe0da44b8a4eeba348938d300afe0bb5c627960a3c7b0ade61d2d8eef9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAYVGT2H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIGKJwmSMgHnjPUKdQeyYv7k87iXVt%2BF4Hv3lUScgKQBBAiBs%2FPgn35TEB7SpNoMFUjjZbL9zTPuVHYiFpr9neoCgmyr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMlga92UKDlNnLxuU6KtwDoMswhHpOAUaDK%2Ff9JpXZEQi0K%2FAxSyIegw%2F7XsJrItqh0%2FsJUJdJ3ttV7NXWSIQUrpGf4d0L2gEn1IzuhckPmwCT266GWGhg6VLD7urDRZ5k54SjRfTF1I7OJ9wEgFCW%2FwsVMMVyDCH3ps1h10COsd%2F7%2BGTcZHr88Xi7r1CzcmRXzFWi1ye7cJru0yLzknTZUg2R%2BVTtmr7aJLJlaeyB7BEywSCh89KgE11BZWmQszs5kPFHPYzUvstAuSEWCm1BBmjaFItlOBxg0qU6hUYUbsCLWS42c96TyZziyUPxOrNn3bGWu68CviLG%2FzcVGGJzcsst9MVFfxorEOYsFZgCgQ5jb2by0vGXipWujPi3tnTyyuv4cuRnYTASaRi96h34sr0w0DOOoDuptUAprpnYRn5wxHhbyazp3n5xIIAj6TTCMQ%2BP5PZymIt%2Bu3%2FO%2ByP2JspbITmQmTOWGG7ofxIB41KTmhKuwgj6%2BkdP3Qq5DLtS%2BvESvPfJ2ZGnYQQ%2Beno4NQ2fbRQcB7%2BHlYqswTTlLiMgjhk1mgGauB7TNHl%2BN%2BByw%2BA5KIBltJy6XCgVcrE4SWTwhiEE272jPX1eZ06TSjygxUNfoDPWzeMM%2B1ZLui5DrrINQD9bFHZqdqkwroKIvQY6pgGSwnIRjx53zFat8u%2Bj5Uo5uODiuytJI7dNoOJhLQtUiWelogxG%2FUCcKZfB36%2BWpfr%2F8Hz517%2FZHIV2yay%2FiqEfxw1o2KJqT2pYudDllMXLbrlLO%2FoWKzTmpVJMKV%2Ba0zv0IkB5%2BAyqMhqz3wyCivyx0Fts%2BnLBncV1wBxoF6Ts8u5X4E9M2MS14X4TCXqCW8W6OidhAktCHSpCweUa94de1KjEs6%2Bu&X-Amz-Signature=7e5980cdb7329fa3ce932277f341ed9910d737e967954a5ab16379b78ba11573&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAYVGT2H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIGKJwmSMgHnjPUKdQeyYv7k87iXVt%2BF4Hv3lUScgKQBBAiBs%2FPgn35TEB7SpNoMFUjjZbL9zTPuVHYiFpr9neoCgmyr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMlga92UKDlNnLxuU6KtwDoMswhHpOAUaDK%2Ff9JpXZEQi0K%2FAxSyIegw%2F7XsJrItqh0%2FsJUJdJ3ttV7NXWSIQUrpGf4d0L2gEn1IzuhckPmwCT266GWGhg6VLD7urDRZ5k54SjRfTF1I7OJ9wEgFCW%2FwsVMMVyDCH3ps1h10COsd%2F7%2BGTcZHr88Xi7r1CzcmRXzFWi1ye7cJru0yLzknTZUg2R%2BVTtmr7aJLJlaeyB7BEywSCh89KgE11BZWmQszs5kPFHPYzUvstAuSEWCm1BBmjaFItlOBxg0qU6hUYUbsCLWS42c96TyZziyUPxOrNn3bGWu68CviLG%2FzcVGGJzcsst9MVFfxorEOYsFZgCgQ5jb2by0vGXipWujPi3tnTyyuv4cuRnYTASaRi96h34sr0w0DOOoDuptUAprpnYRn5wxHhbyazp3n5xIIAj6TTCMQ%2BP5PZymIt%2Bu3%2FO%2ByP2JspbITmQmTOWGG7ofxIB41KTmhKuwgj6%2BkdP3Qq5DLtS%2BvESvPfJ2ZGnYQQ%2Beno4NQ2fbRQcB7%2BHlYqswTTlLiMgjhk1mgGauB7TNHl%2BN%2BByw%2BA5KIBltJy6XCgVcrE4SWTwhiEE272jPX1eZ06TSjygxUNfoDPWzeMM%2B1ZLui5DrrINQD9bFHZqdqkwroKIvQY6pgGSwnIRjx53zFat8u%2Bj5Uo5uODiuytJI7dNoOJhLQtUiWelogxG%2FUCcKZfB36%2BWpfr%2F8Hz517%2FZHIV2yay%2FiqEfxw1o2KJqT2pYudDllMXLbrlLO%2FoWKzTmpVJMKV%2Ba0zv0IkB5%2BAyqMhqz3wyCivyx0Fts%2BnLBncV1wBxoF6Ts8u5X4E9M2MS14X4TCXqCW8W6OidhAktCHSpCweUa94de1KjEs6%2Bu&X-Amz-Signature=25f9c03de33897f02e2e97579ec15c54bf14b9f3cf286379d6d033ed5a3f6e68&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZNFT2MW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDCk0xU%2FlexsrpMwt%2BJegAYf9pWdqIu422p5XaH0IF2QwIhAIoxzA%2Fcf1MntxmQJxT5CsC9XVSYGzdo7QeIRBfDM39cKv8DCC0QABoMNjM3NDIzMTgzODA1IgwtrauyuIr0%2Fqu3hTgq3AMxEH2Pdl9eCDvuBPqVYHReNkpxOu7zc4S1Dxfm59RoT%2FSryieWw5m4morMxfFILmYLCxTeFbjjvfKtB%2Bo0ga9HLm4Lr%2Bsz8fuxnAANOkjLxRq6%2BIUZHdTZ%2FrCg4WdStd0fDO1dJPDCTfOzy4il0I7oNCfqmnLtzyjUm%2BDcrxbl3x9COBJVYP5%2FFKc5aw84Slgp2Am8RkM1sgtPFNBlj8yiXNyhcarMaYuf1j%2Fu%2BRzKKBgsI4z%2FS3YCE8SdG1uWpGbcTA0PWb%2BQg5SbyNXmAQgngF7UD9OCprxHer8tZlUQTUfcMnKR6B2WIkKOuBJShgs00P6qj7GIds%2BqjjwCk6hYwMjMY3e%2FC6EgCL%2FlKhKxv9REXLxfcmw4bu6YaFPkO3%2BNCLmWNa0MyzDEvymbBkGgBX2JXe3TPl%2FGfRnoIM4sJut1tjXZ%2BfbXVotmSeGrSxqEWp%2FXCRAJt2tkmRXP0SBEF%2B0XDLFi8LjLNGvRcBP13PvfxP1adQd%2FQZRSH9vzMfGwg8IFK7ILoLhEe96gaNHEvBv1zJK7ez2%2BRhfSvrrBeIRnHp%2BBbbG9%2BJId%2FrUzDL3q6rnu5wYDhE9uXU7ETeOpsF1bNxN2ifpHUvoyB0xhP2HaGlqWc7RRFWNsdzC1goi9BjqkARzZ2ijrDsITpORyGjhncqIB%2BAomLnT9uc3Blvc%2FXS1Bqum9tmbCcNFAwOx%2BTPX1KJhhEI%2Bt%2BeIhTkpNoaHY2DBDGsC0KSyhLXnDIf9OdkB%2BvjOX7%2BUEospQbaM%2Fi4PdAZ9wl%2FVWL%2B2%2Focl82A8EkRfu3yTqZkOuzze7ajm91c%2FsbuZbB5bEkD9z7YbL5VglP%2Bc9OP%2FrYRtsrT5M1k%2F%2BlfuSFUHf&X-Amz-Signature=b0607bbbeb274288864e16c14ce9a639d6df2e93e762c4f1a097cb96604bc33e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZNFT2MW%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDCk0xU%2FlexsrpMwt%2BJegAYf9pWdqIu422p5XaH0IF2QwIhAIoxzA%2Fcf1MntxmQJxT5CsC9XVSYGzdo7QeIRBfDM39cKv8DCC0QABoMNjM3NDIzMTgzODA1IgwtrauyuIr0%2Fqu3hTgq3AMxEH2Pdl9eCDvuBPqVYHReNkpxOu7zc4S1Dxfm59RoT%2FSryieWw5m4morMxfFILmYLCxTeFbjjvfKtB%2Bo0ga9HLm4Lr%2Bsz8fuxnAANOkjLxRq6%2BIUZHdTZ%2FrCg4WdStd0fDO1dJPDCTfOzy4il0I7oNCfqmnLtzyjUm%2BDcrxbl3x9COBJVYP5%2FFKc5aw84Slgp2Am8RkM1sgtPFNBlj8yiXNyhcarMaYuf1j%2Fu%2BRzKKBgsI4z%2FS3YCE8SdG1uWpGbcTA0PWb%2BQg5SbyNXmAQgngF7UD9OCprxHer8tZlUQTUfcMnKR6B2WIkKOuBJShgs00P6qj7GIds%2BqjjwCk6hYwMjMY3e%2FC6EgCL%2FlKhKxv9REXLxfcmw4bu6YaFPkO3%2BNCLmWNa0MyzDEvymbBkGgBX2JXe3TPl%2FGfRnoIM4sJut1tjXZ%2BfbXVotmSeGrSxqEWp%2FXCRAJt2tkmRXP0SBEF%2B0XDLFi8LjLNGvRcBP13PvfxP1adQd%2FQZRSH9vzMfGwg8IFK7ILoLhEe96gaNHEvBv1zJK7ez2%2BRhfSvrrBeIRnHp%2BBbbG9%2BJId%2FrUzDL3q6rnu5wYDhE9uXU7ETeOpsF1bNxN2ifpHUvoyB0xhP2HaGlqWc7RRFWNsdzC1goi9BjqkARzZ2ijrDsITpORyGjhncqIB%2BAomLnT9uc3Blvc%2FXS1Bqum9tmbCcNFAwOx%2BTPX1KJhhEI%2Bt%2BeIhTkpNoaHY2DBDGsC0KSyhLXnDIf9OdkB%2BvjOX7%2BUEospQbaM%2Fi4PdAZ9wl%2FVWL%2B2%2Focl82A8EkRfu3yTqZkOuzze7ajm91c%2FsbuZbB5bEkD9z7YbL5VglP%2Bc9OP%2FrYRtsrT5M1k%2F%2BlfuSFUHf&X-Amz-Signature=a845da80fb6c3d90ccba94e1dab9616b0ec9eca5724643a83c9475ab6005db46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAYVGT2H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIGKJwmSMgHnjPUKdQeyYv7k87iXVt%2BF4Hv3lUScgKQBBAiBs%2FPgn35TEB7SpNoMFUjjZbL9zTPuVHYiFpr9neoCgmyr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMlga92UKDlNnLxuU6KtwDoMswhHpOAUaDK%2Ff9JpXZEQi0K%2FAxSyIegw%2F7XsJrItqh0%2FsJUJdJ3ttV7NXWSIQUrpGf4d0L2gEn1IzuhckPmwCT266GWGhg6VLD7urDRZ5k54SjRfTF1I7OJ9wEgFCW%2FwsVMMVyDCH3ps1h10COsd%2F7%2BGTcZHr88Xi7r1CzcmRXzFWi1ye7cJru0yLzknTZUg2R%2BVTtmr7aJLJlaeyB7BEywSCh89KgE11BZWmQszs5kPFHPYzUvstAuSEWCm1BBmjaFItlOBxg0qU6hUYUbsCLWS42c96TyZziyUPxOrNn3bGWu68CviLG%2FzcVGGJzcsst9MVFfxorEOYsFZgCgQ5jb2by0vGXipWujPi3tnTyyuv4cuRnYTASaRi96h34sr0w0DOOoDuptUAprpnYRn5wxHhbyazp3n5xIIAj6TTCMQ%2BP5PZymIt%2Bu3%2FO%2ByP2JspbITmQmTOWGG7ofxIB41KTmhKuwgj6%2BkdP3Qq5DLtS%2BvESvPfJ2ZGnYQQ%2Beno4NQ2fbRQcB7%2BHlYqswTTlLiMgjhk1mgGauB7TNHl%2BN%2BByw%2BA5KIBltJy6XCgVcrE4SWTwhiEE272jPX1eZ06TSjygxUNfoDPWzeMM%2B1ZLui5DrrINQD9bFHZqdqkwroKIvQY6pgGSwnIRjx53zFat8u%2Bj5Uo5uODiuytJI7dNoOJhLQtUiWelogxG%2FUCcKZfB36%2BWpfr%2F8Hz517%2FZHIV2yay%2FiqEfxw1o2KJqT2pYudDllMXLbrlLO%2FoWKzTmpVJMKV%2Ba0zv0IkB5%2BAyqMhqz3wyCivyx0Fts%2BnLBncV1wBxoF6Ts8u5X4E9M2MS14X4TCXqCW8W6OidhAktCHSpCweUa94de1KjEs6%2Bu&X-Amz-Signature=73827df33d1155a6d9bc66242dcb3e0b22a4de570c3b29706ca1e71ed8bd6e21&X-Amz-SignedHeaders=host&x-id=GetObject)
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