

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NBXYSHE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCRn6Gg4g%2BhwhODgTxfUzQlFxbGRMcGF0DDkKEbzY%2F73AIgCGuQ1cHZnQm6Gxw16ScReMm%2BCJUN1HYPhQyHWIsLelMqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA6vmQb%2BK65zzc4%2FdyrcA347hdVym%2BX4TQTcZlmO62V49S4AadyuxdFUDrbqWnYDS5xkJVZ6mnBOOVVUCDR2wdcWQPgsm61X%2FCIgfg89wEWu6l2T%2FvcBAkE4zIfStiVN%2BFOyfR5Q43fFj78rig4aL2fqPS%2Bjbji8kBMT06IdMscz8powdYAfrOS%2BURjydp4X%2BaCvbs6uyA0IEdwWlEza5KAGR1MyJUY%2BEwfqka4egymQWIkqVYRacN0nuBQXX3lGYsUgYchCZSWUuPzn8bTMgnhvU5L062zwe8GloPgks0DXwA2op1wdv97k6Tmi0H88WyCR2Bh08MYGvZg%2FQGF%2F1Y%2B4ZYxcECKZdHMRaaYUfoWeh575yp%2BTN6iHctZ6aGlsR96jeHC4stzWjl%2BEOFoUK0rjaCFFSVVOZXF4MUOlycY0kWrcq7BGpYGbGPNLRGecq9ehjFV8DVv0IcBaBABZwOSBGaPqFPG9U2ALn38Wxs3kpd8EevESnbDY1iACSOlFYztPyydxPjRE4YjmGL80LAUdDVxfWJp2eN9Szn79fBmCVduVJl7JvDAMVjzOiJ49Isy4YqxfBD0xNuSExp%2B7linllqup8CwUNgr47uQuUM3mUX51kPfgB4aDB0Ux%2B8XvkqZEmF%2BS4iNC7ZfmMJCOnL0GOqUBDfbyoCSEuDF4p9VO7AzUNqBYXdVinVYPc7P0jrYRG7oF29N9wr4EXp8TQwQgO%2FZz%2FO%2BDsATCGrPgbV8iclSymRo0akvFyIFiKOTRpuZAi%2BjFHlayBo6x1fTXeXgH9NNH2Re7d%2FrGsNxriRMzidn%2BgQSHaA7jGGvhQw3rhNYP94%2BYkMHAk7m4H8EbIiPH1b8FYroZuNO0yDrN%2B8XiFZcJwqb5q%2FDa&X-Amz-Signature=279a699454eb88d12834aabf9e47767596eb85b3cc9fb8b1881020ee253432eb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NBXYSHE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCRn6Gg4g%2BhwhODgTxfUzQlFxbGRMcGF0DDkKEbzY%2F73AIgCGuQ1cHZnQm6Gxw16ScReMm%2BCJUN1HYPhQyHWIsLelMqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA6vmQb%2BK65zzc4%2FdyrcA347hdVym%2BX4TQTcZlmO62V49S4AadyuxdFUDrbqWnYDS5xkJVZ6mnBOOVVUCDR2wdcWQPgsm61X%2FCIgfg89wEWu6l2T%2FvcBAkE4zIfStiVN%2BFOyfR5Q43fFj78rig4aL2fqPS%2Bjbji8kBMT06IdMscz8powdYAfrOS%2BURjydp4X%2BaCvbs6uyA0IEdwWlEza5KAGR1MyJUY%2BEwfqka4egymQWIkqVYRacN0nuBQXX3lGYsUgYchCZSWUuPzn8bTMgnhvU5L062zwe8GloPgks0DXwA2op1wdv97k6Tmi0H88WyCR2Bh08MYGvZg%2FQGF%2F1Y%2B4ZYxcECKZdHMRaaYUfoWeh575yp%2BTN6iHctZ6aGlsR96jeHC4stzWjl%2BEOFoUK0rjaCFFSVVOZXF4MUOlycY0kWrcq7BGpYGbGPNLRGecq9ehjFV8DVv0IcBaBABZwOSBGaPqFPG9U2ALn38Wxs3kpd8EevESnbDY1iACSOlFYztPyydxPjRE4YjmGL80LAUdDVxfWJp2eN9Szn79fBmCVduVJl7JvDAMVjzOiJ49Isy4YqxfBD0xNuSExp%2B7linllqup8CwUNgr47uQuUM3mUX51kPfgB4aDB0Ux%2B8XvkqZEmF%2BS4iNC7ZfmMJCOnL0GOqUBDfbyoCSEuDF4p9VO7AzUNqBYXdVinVYPc7P0jrYRG7oF29N9wr4EXp8TQwQgO%2FZz%2FO%2BDsATCGrPgbV8iclSymRo0akvFyIFiKOTRpuZAi%2BjFHlayBo6x1fTXeXgH9NNH2Re7d%2FrGsNxriRMzidn%2BgQSHaA7jGGvhQw3rhNYP94%2BYkMHAk7m4H8EbIiPH1b8FYroZuNO0yDrN%2B8XiFZcJwqb5q%2FDa&X-Amz-Signature=0854324c07edc47aa61e10c94bd3b16ccd94c57f801436db3d1b9a3697d2b3e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NBXYSHE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCRn6Gg4g%2BhwhODgTxfUzQlFxbGRMcGF0DDkKEbzY%2F73AIgCGuQ1cHZnQm6Gxw16ScReMm%2BCJUN1HYPhQyHWIsLelMqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA6vmQb%2BK65zzc4%2FdyrcA347hdVym%2BX4TQTcZlmO62V49S4AadyuxdFUDrbqWnYDS5xkJVZ6mnBOOVVUCDR2wdcWQPgsm61X%2FCIgfg89wEWu6l2T%2FvcBAkE4zIfStiVN%2BFOyfR5Q43fFj78rig4aL2fqPS%2Bjbji8kBMT06IdMscz8powdYAfrOS%2BURjydp4X%2BaCvbs6uyA0IEdwWlEza5KAGR1MyJUY%2BEwfqka4egymQWIkqVYRacN0nuBQXX3lGYsUgYchCZSWUuPzn8bTMgnhvU5L062zwe8GloPgks0DXwA2op1wdv97k6Tmi0H88WyCR2Bh08MYGvZg%2FQGF%2F1Y%2B4ZYxcECKZdHMRaaYUfoWeh575yp%2BTN6iHctZ6aGlsR96jeHC4stzWjl%2BEOFoUK0rjaCFFSVVOZXF4MUOlycY0kWrcq7BGpYGbGPNLRGecq9ehjFV8DVv0IcBaBABZwOSBGaPqFPG9U2ALn38Wxs3kpd8EevESnbDY1iACSOlFYztPyydxPjRE4YjmGL80LAUdDVxfWJp2eN9Szn79fBmCVduVJl7JvDAMVjzOiJ49Isy4YqxfBD0xNuSExp%2B7linllqup8CwUNgr47uQuUM3mUX51kPfgB4aDB0Ux%2B8XvkqZEmF%2BS4iNC7ZfmMJCOnL0GOqUBDfbyoCSEuDF4p9VO7AzUNqBYXdVinVYPc7P0jrYRG7oF29N9wr4EXp8TQwQgO%2FZz%2FO%2BDsATCGrPgbV8iclSymRo0akvFyIFiKOTRpuZAi%2BjFHlayBo6x1fTXeXgH9NNH2Re7d%2FrGsNxriRMzidn%2BgQSHaA7jGGvhQw3rhNYP94%2BYkMHAk7m4H8EbIiPH1b8FYroZuNO0yDrN%2B8XiFZcJwqb5q%2FDa&X-Amz-Signature=b86163419a81f9492452e5bd251dae4f5dae742c4c8dfa5fb04f39ca9229000f&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6L62FFI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDES0VQlU68t%2FSxvFfjAI48pOdITzo3jPrfZDVdQcvlEAiEA4RnO4rw1UqqHs8TitWZvkLo26pkJYzWF9dcUJfBcgCgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMnvZ3%2FVDd0xibCa1SrcA5dGc%2BsHfZWt9hqIHHTzJ7yB8MWlwFcswC8PAqHyLT4KzlvQqUXKqu5P6K2GmxnKbaJkjWH6fFVqFWVV%2BGELeIG0S8f4CmnyhfcHFNvz%2BHOLv9TUczJzMxBc0LiEXsX6cVh%2Ff44uM8mRuwOVuWLXo5fdbnTb2sLzbrlWuG%2FwCB6q9qAbmP0hOzWGikyJT6wgxKY62%2BlTs5T%2BL%2FTJh5PwbtIXe3EFmExHZXd5OJy%2F5Rldydq5bBJzKkq4MRPZZQd4hXyVdKnnvyPyDKaXzHAU9%2F1XojXIOKAybIULWAZURjTrKBWYQkSI46zMxBVpIDbhERqOuBVVLMFUiUVT6skiroFp829kfavSaSimuKWqsJXsWF231MJNHaDejwOg6Qyo9NOeGB88u%2BEAoB8MwUKhBd8hjU2goNoxx8ubf24oeQOs1TNzziVzQBg4l87Jgni7kFH8s5z8RaGh22vN8l7pUMdOdrAj4ajx0M3ekAjwYkvTIeg2en23n9Dxv%2B9aOPDJL5yShKaYMCFb6DZqsPpoOscMOTO7QC2zRe8yuL%2BeqU%2BjUJ5jsBPjLZAE5gEnb9SYjOC01BsJhpqaR0xK0quKU%2BU2ExBaHogVGBnwMuii%2Fl0TxLHOFtxvwH%2BBIDqqMNuOnL0GOqUBI875buHrOawg3DkfsUN9TJ%2B8TNgZUYfc5pATRFzAoSPMD3gIy2%2BKBz2orBnoTEt8RrZukWwD4G8HhLtcnuVmFVu9q2WgdDPIweqac8lFq2ii2mFAgqSxiEc%2FhnVH8vVuhZJ6xfGlJLEZDhBhidJ8isY8hKtO%2Bsdv%2FE4r0D8TVQKoSr6dVWWfqf8F08xGIolktlDHqhC1F3xpQyC2cz28ClFYk0xv&X-Amz-Signature=17b4a7e32a212d98c59b6f4556bc1dc737e34049bb66dcbe902b88866d4bd0b2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6L62FFI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIDES0VQlU68t%2FSxvFfjAI48pOdITzo3jPrfZDVdQcvlEAiEA4RnO4rw1UqqHs8TitWZvkLo26pkJYzWF9dcUJfBcgCgqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMnvZ3%2FVDd0xibCa1SrcA5dGc%2BsHfZWt9hqIHHTzJ7yB8MWlwFcswC8PAqHyLT4KzlvQqUXKqu5P6K2GmxnKbaJkjWH6fFVqFWVV%2BGELeIG0S8f4CmnyhfcHFNvz%2BHOLv9TUczJzMxBc0LiEXsX6cVh%2Ff44uM8mRuwOVuWLXo5fdbnTb2sLzbrlWuG%2FwCB6q9qAbmP0hOzWGikyJT6wgxKY62%2BlTs5T%2BL%2FTJh5PwbtIXe3EFmExHZXd5OJy%2F5Rldydq5bBJzKkq4MRPZZQd4hXyVdKnnvyPyDKaXzHAU9%2F1XojXIOKAybIULWAZURjTrKBWYQkSI46zMxBVpIDbhERqOuBVVLMFUiUVT6skiroFp829kfavSaSimuKWqsJXsWF231MJNHaDejwOg6Qyo9NOeGB88u%2BEAoB8MwUKhBd8hjU2goNoxx8ubf24oeQOs1TNzziVzQBg4l87Jgni7kFH8s5z8RaGh22vN8l7pUMdOdrAj4ajx0M3ekAjwYkvTIeg2en23n9Dxv%2B9aOPDJL5yShKaYMCFb6DZqsPpoOscMOTO7QC2zRe8yuL%2BeqU%2BjUJ5jsBPjLZAE5gEnb9SYjOC01BsJhpqaR0xK0quKU%2BU2ExBaHogVGBnwMuii%2Fl0TxLHOFtxvwH%2BBIDqqMNuOnL0GOqUBI875buHrOawg3DkfsUN9TJ%2B8TNgZUYfc5pATRFzAoSPMD3gIy2%2BKBz2orBnoTEt8RrZukWwD4G8HhLtcnuVmFVu9q2WgdDPIweqac8lFq2ii2mFAgqSxiEc%2FhnVH8vVuhZJ6xfGlJLEZDhBhidJ8isY8hKtO%2Bsdv%2FE4r0D8TVQKoSr6dVWWfqf8F08xGIolktlDHqhC1F3xpQyC2cz28ClFYk0xv&X-Amz-Signature=5586834efd2c855009063337445b305f82967a16fd9268301dc52de038c0fe43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NBXYSHE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T091352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCRn6Gg4g%2BhwhODgTxfUzQlFxbGRMcGF0DDkKEbzY%2F73AIgCGuQ1cHZnQm6Gxw16ScReMm%2BCJUN1HYPhQyHWIsLelMqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA6vmQb%2BK65zzc4%2FdyrcA347hdVym%2BX4TQTcZlmO62V49S4AadyuxdFUDrbqWnYDS5xkJVZ6mnBOOVVUCDR2wdcWQPgsm61X%2FCIgfg89wEWu6l2T%2FvcBAkE4zIfStiVN%2BFOyfR5Q43fFj78rig4aL2fqPS%2Bjbji8kBMT06IdMscz8powdYAfrOS%2BURjydp4X%2BaCvbs6uyA0IEdwWlEza5KAGR1MyJUY%2BEwfqka4egymQWIkqVYRacN0nuBQXX3lGYsUgYchCZSWUuPzn8bTMgnhvU5L062zwe8GloPgks0DXwA2op1wdv97k6Tmi0H88WyCR2Bh08MYGvZg%2FQGF%2F1Y%2B4ZYxcECKZdHMRaaYUfoWeh575yp%2BTN6iHctZ6aGlsR96jeHC4stzWjl%2BEOFoUK0rjaCFFSVVOZXF4MUOlycY0kWrcq7BGpYGbGPNLRGecq9ehjFV8DVv0IcBaBABZwOSBGaPqFPG9U2ALn38Wxs3kpd8EevESnbDY1iACSOlFYztPyydxPjRE4YjmGL80LAUdDVxfWJp2eN9Szn79fBmCVduVJl7JvDAMVjzOiJ49Isy4YqxfBD0xNuSExp%2B7linllqup8CwUNgr47uQuUM3mUX51kPfgB4aDB0Ux%2B8XvkqZEmF%2BS4iNC7ZfmMJCOnL0GOqUBDfbyoCSEuDF4p9VO7AzUNqBYXdVinVYPc7P0jrYRG7oF29N9wr4EXp8TQwQgO%2FZz%2FO%2BDsATCGrPgbV8iclSymRo0akvFyIFiKOTRpuZAi%2BjFHlayBo6x1fTXeXgH9NNH2Re7d%2FrGsNxriRMzidn%2BgQSHaA7jGGvhQw3rhNYP94%2BYkMHAk7m4H8EbIiPH1b8FYroZuNO0yDrN%2B8XiFZcJwqb5q%2FDa&X-Amz-Signature=fcbfb1a9a5f3b0e051a99b470b46fe1aa49ff96c86f7bfd9b6110d090e6501b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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