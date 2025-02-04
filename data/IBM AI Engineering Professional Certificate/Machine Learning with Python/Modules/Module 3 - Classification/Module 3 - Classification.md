

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKGMQNMR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDYn290SbaR3dTrFaVhZzlMA4WQeG5HPLzk3Upzsj3EhQIhAP7Jlo3PanbfZrbFKas2lzV1ol3XPPLykHvwBG7SnfDWKv8DCC8QABoMNjM3NDIzMTgzODA1Igw%2FQDtKRG92hsnNROUq3AO3Mzx9eOGXbeQs20kmGNr9oqOYZm%2BAurKfFr0NrMYLFBSAgDxjUrnR%2Fxlst2%2B5rxjMm1oJ9R1VDlgalDWA9htfRakkQP62ExN2j5zUG5Kt0uMC0sO2vrXHYAtG72FWL0Kk5b7BXOfHT7AVrmGnbJS20bLEbsfWOLFyIt3Z%2B5CkpzSU97DieIE1tdxvL%2BbP3O3ygFkxMNdv63naSJHYjs4npD5ziKCC9VIiovMLR2Yw9lapYKbFkjpFcgFxly1Mx9IEMjgTnB%2BZfPpUEnL2CPY%2Fw4LHVloAM8Cju5IHOG4dATYchK7sS8MJtZyLdEteTSbOFpsnJN9evJCmSCfVzM6bNupGHlBmkD3otqfC%2FkEgxMKojem06w2myziCSYcq7pjhvJyi6SP7YYaD%2BxogiU9%2FltEoWjMN%2B40yPOMMlt3RDdyegpVQfhXTt1Io3XOhQqAa8Ib90oSUgSeWLSPny1JDVltg%2BLcq066otU%2B3ZI7bCzaoyL3U81ugt3qE5tHhAcC4joa5WopRw7a2uTWveyrN0ocQuW%2FAzitV%2BNAsG%2FxQMudjnUsy0K6knwokbJdIUo06mwBPzUaI7Gh%2BWsxd%2Bd8Kai30Zofdzk47QrhFhK3QaOY0TxhSZvEsRTsZVjCBvYi9BjqkAaQ7TTKDRD9qj4%2BirwwfdZLUFbszUhD0OIMvekH5bXe%2BueZetgMsXH6cqnm3tVhwr1y%2Fu9Vo0nUk3CHJ0QS3WgDfknYtT%2BSzL%2BgZASCDjMu5gEw1ycAkSgk7TVcmBqvCIZNsN6DwN%2FxHSe9dQPAsqcwyCl4BE1rV59yqIXYSdAxkuGdBb3jlCTO48r0EyZ8trIEz5uqxcX5i58HECLj3uBDMYmQx&X-Amz-Signature=f0eb3477cde146ef8a19e599312b5d2749a721de9d4978bfc76ce0a546fc4de1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKGMQNMR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDYn290SbaR3dTrFaVhZzlMA4WQeG5HPLzk3Upzsj3EhQIhAP7Jlo3PanbfZrbFKas2lzV1ol3XPPLykHvwBG7SnfDWKv8DCC8QABoMNjM3NDIzMTgzODA1Igw%2FQDtKRG92hsnNROUq3AO3Mzx9eOGXbeQs20kmGNr9oqOYZm%2BAurKfFr0NrMYLFBSAgDxjUrnR%2Fxlst2%2B5rxjMm1oJ9R1VDlgalDWA9htfRakkQP62ExN2j5zUG5Kt0uMC0sO2vrXHYAtG72FWL0Kk5b7BXOfHT7AVrmGnbJS20bLEbsfWOLFyIt3Z%2B5CkpzSU97DieIE1tdxvL%2BbP3O3ygFkxMNdv63naSJHYjs4npD5ziKCC9VIiovMLR2Yw9lapYKbFkjpFcgFxly1Mx9IEMjgTnB%2BZfPpUEnL2CPY%2Fw4LHVloAM8Cju5IHOG4dATYchK7sS8MJtZyLdEteTSbOFpsnJN9evJCmSCfVzM6bNupGHlBmkD3otqfC%2FkEgxMKojem06w2myziCSYcq7pjhvJyi6SP7YYaD%2BxogiU9%2FltEoWjMN%2B40yPOMMlt3RDdyegpVQfhXTt1Io3XOhQqAa8Ib90oSUgSeWLSPny1JDVltg%2BLcq066otU%2B3ZI7bCzaoyL3U81ugt3qE5tHhAcC4joa5WopRw7a2uTWveyrN0ocQuW%2FAzitV%2BNAsG%2FxQMudjnUsy0K6knwokbJdIUo06mwBPzUaI7Gh%2BWsxd%2Bd8Kai30Zofdzk47QrhFhK3QaOY0TxhSZvEsRTsZVjCBvYi9BjqkAaQ7TTKDRD9qj4%2BirwwfdZLUFbszUhD0OIMvekH5bXe%2BueZetgMsXH6cqnm3tVhwr1y%2Fu9Vo0nUk3CHJ0QS3WgDfknYtT%2BSzL%2BgZASCDjMu5gEw1ycAkSgk7TVcmBqvCIZNsN6DwN%2FxHSe9dQPAsqcwyCl4BE1rV59yqIXYSdAxkuGdBb3jlCTO48r0EyZ8trIEz5uqxcX5i58HECLj3uBDMYmQx&X-Amz-Signature=5c625ff554d7ad439d3d899d037acb943fe8eb61aa5367954e1fe1c2c3ec4c1a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKGMQNMR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDYn290SbaR3dTrFaVhZzlMA4WQeG5HPLzk3Upzsj3EhQIhAP7Jlo3PanbfZrbFKas2lzV1ol3XPPLykHvwBG7SnfDWKv8DCC8QABoMNjM3NDIzMTgzODA1Igw%2FQDtKRG92hsnNROUq3AO3Mzx9eOGXbeQs20kmGNr9oqOYZm%2BAurKfFr0NrMYLFBSAgDxjUrnR%2Fxlst2%2B5rxjMm1oJ9R1VDlgalDWA9htfRakkQP62ExN2j5zUG5Kt0uMC0sO2vrXHYAtG72FWL0Kk5b7BXOfHT7AVrmGnbJS20bLEbsfWOLFyIt3Z%2B5CkpzSU97DieIE1tdxvL%2BbP3O3ygFkxMNdv63naSJHYjs4npD5ziKCC9VIiovMLR2Yw9lapYKbFkjpFcgFxly1Mx9IEMjgTnB%2BZfPpUEnL2CPY%2Fw4LHVloAM8Cju5IHOG4dATYchK7sS8MJtZyLdEteTSbOFpsnJN9evJCmSCfVzM6bNupGHlBmkD3otqfC%2FkEgxMKojem06w2myziCSYcq7pjhvJyi6SP7YYaD%2BxogiU9%2FltEoWjMN%2B40yPOMMlt3RDdyegpVQfhXTt1Io3XOhQqAa8Ib90oSUgSeWLSPny1JDVltg%2BLcq066otU%2B3ZI7bCzaoyL3U81ugt3qE5tHhAcC4joa5WopRw7a2uTWveyrN0ocQuW%2FAzitV%2BNAsG%2FxQMudjnUsy0K6knwokbJdIUo06mwBPzUaI7Gh%2BWsxd%2Bd8Kai30Zofdzk47QrhFhK3QaOY0TxhSZvEsRTsZVjCBvYi9BjqkAaQ7TTKDRD9qj4%2BirwwfdZLUFbszUhD0OIMvekH5bXe%2BueZetgMsXH6cqnm3tVhwr1y%2Fu9Vo0nUk3CHJ0QS3WgDfknYtT%2BSzL%2BgZASCDjMu5gEw1ycAkSgk7TVcmBqvCIZNsN6DwN%2FxHSe9dQPAsqcwyCl4BE1rV59yqIXYSdAxkuGdBb3jlCTO48r0EyZ8trIEz5uqxcX5i58HECLj3uBDMYmQx&X-Amz-Signature=d634feff5e71bec5ad043fdf14e244614f2ef4650c854c820e9a902452bf6795&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZM62TRZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCN54D8sw0QoYArXNxbvPAZKfx5D6njOr79WguSYihowQIhAJ2dXHKrYNy%2BNjoSPYCWrdqZSlSOu%2BmmeVUG8DwxJTHuKv8DCC8QABoMNjM3NDIzMTgzODA1IgzgSW7nUVQJJCl5EGkq3AP9vddFaRiZVL6Xzp1UcwvdU2ZP3172v6BD6edEYfSy%2B5TlAlk%2BMQBHlQgnDrft0Moy7zJ03bCpH0nFKgSidkjXW7TXneJIU3anfGMGu%2FLKQGGRSZ8OKRf8OOMtuuQKQrFHj%2BoQb%2BeEr3gcYg7szeyj1xi9zbHYj0Z8RFt%2BJc8KIOECFaT3oCNyxIDl%2FAadS4Qaf1uIdeSW8tUM9tK5bQh%2Bqzvfm5pY79Ohi4Du922R2HopF%2BuHE%2FN3dVGCt9TW6Q1QQ66xutI4JdvZcn6I1nvntqXTY6WuJvQ45C3R9Nl1rPgWdTuaEiRiHNtUvWcPAvr7QTd%2BpLrNMRVz3ZBBxWfKjVhicNDbHvsDFu8xAopcGTpOaxn6FynqoBwh1bJdjRtgY6J3q%2B7dAAxxo1DMK7li9RmKm4596ehAZydQOqqg1GEgeJGz%2F%2BJlySkV33YJtHguqxngsnB5immvNRKYlx6P0RKyEkTAuWgty8C5RXd5N0zwz7GsKVF%2FzVsA%2Bch4ndNwPfVTL1WZQhIVtP2aB%2F9Wh2UmDb%2BiVLK69%2BDUfU7cHyBtMybNvv%2BtaC02lU9eg7SfUIxU0k9cskAU9oDyH%2Fcf5h8eQ5sv0KfR7awmnQ3qSMRa66bchJwMqs6ThjDfvIi9BjqkARevmOpWAtJJVLkrZCg5kJVjkxaT5Dh9%2BZ3h31kBXrRD1Ds5rB%2FJSk8wyoLeV9%2BcbiNmvBMKGk8p%2B12M%2BcjTe44FrrjJdiU6CXxhF%2BLlKrEdeoeWUGO%2FW2VygDHihdRjcqYDjAwjCEx%2FK0Stqz9oq5hpAD8MvZCGHwx9pHqVspBmB5hQXToZAnIlH5f3L72rXJ8ZklA5fNodLgHKqHe0m99Law%2BJ&X-Amz-Signature=fee2b34f8b61a8f6b1f16fd96a753def4507c2a746c7efba20d9e020254a87bf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZM62TRZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCN54D8sw0QoYArXNxbvPAZKfx5D6njOr79WguSYihowQIhAJ2dXHKrYNy%2BNjoSPYCWrdqZSlSOu%2BmmeVUG8DwxJTHuKv8DCC8QABoMNjM3NDIzMTgzODA1IgzgSW7nUVQJJCl5EGkq3AP9vddFaRiZVL6Xzp1UcwvdU2ZP3172v6BD6edEYfSy%2B5TlAlk%2BMQBHlQgnDrft0Moy7zJ03bCpH0nFKgSidkjXW7TXneJIU3anfGMGu%2FLKQGGRSZ8OKRf8OOMtuuQKQrFHj%2BoQb%2BeEr3gcYg7szeyj1xi9zbHYj0Z8RFt%2BJc8KIOECFaT3oCNyxIDl%2FAadS4Qaf1uIdeSW8tUM9tK5bQh%2Bqzvfm5pY79Ohi4Du922R2HopF%2BuHE%2FN3dVGCt9TW6Q1QQ66xutI4JdvZcn6I1nvntqXTY6WuJvQ45C3R9Nl1rPgWdTuaEiRiHNtUvWcPAvr7QTd%2BpLrNMRVz3ZBBxWfKjVhicNDbHvsDFu8xAopcGTpOaxn6FynqoBwh1bJdjRtgY6J3q%2B7dAAxxo1DMK7li9RmKm4596ehAZydQOqqg1GEgeJGz%2F%2BJlySkV33YJtHguqxngsnB5immvNRKYlx6P0RKyEkTAuWgty8C5RXd5N0zwz7GsKVF%2FzVsA%2Bch4ndNwPfVTL1WZQhIVtP2aB%2F9Wh2UmDb%2BiVLK69%2BDUfU7cHyBtMybNvv%2BtaC02lU9eg7SfUIxU0k9cskAU9oDyH%2Fcf5h8eQ5sv0KfR7awmnQ3qSMRa66bchJwMqs6ThjDfvIi9BjqkARevmOpWAtJJVLkrZCg5kJVjkxaT5Dh9%2BZ3h31kBXrRD1Ds5rB%2FJSk8wyoLeV9%2BcbiNmvBMKGk8p%2B12M%2BcjTe44FrrjJdiU6CXxhF%2BLlKrEdeoeWUGO%2FW2VygDHihdRjcqYDjAwjCEx%2FK0Stqz9oq5hpAD8MvZCGHwx9pHqVspBmB5hQXToZAnIlH5f3L72rXJ8ZklA5fNodLgHKqHe0m99Law%2BJ&X-Amz-Signature=3de30ec38643dd168d504264173e153d039a4a59604aaa21dc2a8e2a66cc8e42&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKGMQNMR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDYn290SbaR3dTrFaVhZzlMA4WQeG5HPLzk3Upzsj3EhQIhAP7Jlo3PanbfZrbFKas2lzV1ol3XPPLykHvwBG7SnfDWKv8DCC8QABoMNjM3NDIzMTgzODA1Igw%2FQDtKRG92hsnNROUq3AO3Mzx9eOGXbeQs20kmGNr9oqOYZm%2BAurKfFr0NrMYLFBSAgDxjUrnR%2Fxlst2%2B5rxjMm1oJ9R1VDlgalDWA9htfRakkQP62ExN2j5zUG5Kt0uMC0sO2vrXHYAtG72FWL0Kk5b7BXOfHT7AVrmGnbJS20bLEbsfWOLFyIt3Z%2B5CkpzSU97DieIE1tdxvL%2BbP3O3ygFkxMNdv63naSJHYjs4npD5ziKCC9VIiovMLR2Yw9lapYKbFkjpFcgFxly1Mx9IEMjgTnB%2BZfPpUEnL2CPY%2Fw4LHVloAM8Cju5IHOG4dATYchK7sS8MJtZyLdEteTSbOFpsnJN9evJCmSCfVzM6bNupGHlBmkD3otqfC%2FkEgxMKojem06w2myziCSYcq7pjhvJyi6SP7YYaD%2BxogiU9%2FltEoWjMN%2B40yPOMMlt3RDdyegpVQfhXTt1Io3XOhQqAa8Ib90oSUgSeWLSPny1JDVltg%2BLcq066otU%2B3ZI7bCzaoyL3U81ugt3qE5tHhAcC4joa5WopRw7a2uTWveyrN0ocQuW%2FAzitV%2BNAsG%2FxQMudjnUsy0K6knwokbJdIUo06mwBPzUaI7Gh%2BWsxd%2Bd8Kai30Zofdzk47QrhFhK3QaOY0TxhSZvEsRTsZVjCBvYi9BjqkAaQ7TTKDRD9qj4%2BirwwfdZLUFbszUhD0OIMvekH5bXe%2BueZetgMsXH6cqnm3tVhwr1y%2Fu9Vo0nUk3CHJ0QS3WgDfknYtT%2BSzL%2BgZASCDjMu5gEw1ycAkSgk7TVcmBqvCIZNsN6DwN%2FxHSe9dQPAsqcwyCl4BE1rV59yqIXYSdAxkuGdBb3jlCTO48r0EyZ8trIEz5uqxcX5i58HECLj3uBDMYmQx&X-Amz-Signature=6dd35779406046ce3eade3f80af9acd1de15cc80ed79c9314bc49669b5d20767&X-Amz-SignedHeaders=host&x-id=GetObject)
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