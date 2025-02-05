

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TZKYRYG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCVfhSF%2BqX7wp2xgcZSvZoSCrnrzSF0wcCIBX4vOQF8gwIhAMhxIs4dQLHecjfFXQZpQ%2BQKnqw0G4StI1V1cMo%2FSImHKv8DCEQQABoMNjM3NDIzMTgzODA1IgznbhqqBWVKYemHkMEq3ANBmZHie1ejTrQRnccQD9WP3UMV2aaRcRQ%2Fo8TR7W9Q5EfkdcWJ4rQFHBojMAQHuJmlj4JgNKmyWW5%2Bxgyo8zjejVEpbR1eej7%2Bi8Uq6vzVvcdlEwnjbwPPwAHLW1bzJhhI0%2BjSjZ6gpbr1U%2BZ1xCJAaEYurWD7eJUgcwHqiHMkXCEut8EezIgyxabOlm2nK7x5XJgn4oMdPjdIUGgJtk8clBN%2FOmaaA2Y%2FO546KNW8TafWUZcpjhyNX92O8IFtRuGKzK6FOfieJuJHeOgPmAWbJ8vReovpzfcXEOa500bs%2Fwl2P8FV%2FCJDr%2FBK%2FV%2Fm3LVbhAJ90r0FlnbUPhcDMR2VZZCkv4etHnUmLOt2hEnrtDNb91VIU5G916D7xbdYMvXi5cbYFd0ZWG9Ff8P0ly5WwtLS7oyKY2AMPKQeJevopViih1AaJqx2A08TaRFxjj4d0MoyuUDR29xYYgV%2F05DzmHvvlVo5gEV%2BeN2NkCpQOSnnt9KyrKskCzb%2FlDEgfJGHqNsVUJjc07T5v32yjjGFEzA93%2Fyy5ablngKW6mjm72Z005Mpgd2SULAboqrk8eRmEuQ%2FlSASrp9ptc%2FCybAfGrxrjB%2F1RSjwWUx%2BVDUGB1tbRytknv0VjPhvrTCui429BjqkAWmED3xDlgtHJUcmPDDvpwq%2BU1lwu5PRo7aJ9G2nsJ5s4SchV2TejVsoxAUcUzjzhNYdo1zpC4Z9GnEesldFp%2BDIe03yZJs3AXxRBn3jgbfHuAC%2FNg%2FHYXwbWlPQ5m31L%2BnNqj5XkWijKQh%2BH71XM07cRji5qFtzkFsgvcFja5CcQCAf79xKEm7vA001o5VvDNBxBPaObq3pModzkzIl31sBudYS&X-Amz-Signature=9660fbcac4a66df151ff465106b63e7a922b9bb0e5f3dfaaa7951e4399a1a104&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TZKYRYG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCVfhSF%2BqX7wp2xgcZSvZoSCrnrzSF0wcCIBX4vOQF8gwIhAMhxIs4dQLHecjfFXQZpQ%2BQKnqw0G4StI1V1cMo%2FSImHKv8DCEQQABoMNjM3NDIzMTgzODA1IgznbhqqBWVKYemHkMEq3ANBmZHie1ejTrQRnccQD9WP3UMV2aaRcRQ%2Fo8TR7W9Q5EfkdcWJ4rQFHBojMAQHuJmlj4JgNKmyWW5%2Bxgyo8zjejVEpbR1eej7%2Bi8Uq6vzVvcdlEwnjbwPPwAHLW1bzJhhI0%2BjSjZ6gpbr1U%2BZ1xCJAaEYurWD7eJUgcwHqiHMkXCEut8EezIgyxabOlm2nK7x5XJgn4oMdPjdIUGgJtk8clBN%2FOmaaA2Y%2FO546KNW8TafWUZcpjhyNX92O8IFtRuGKzK6FOfieJuJHeOgPmAWbJ8vReovpzfcXEOa500bs%2Fwl2P8FV%2FCJDr%2FBK%2FV%2Fm3LVbhAJ90r0FlnbUPhcDMR2VZZCkv4etHnUmLOt2hEnrtDNb91VIU5G916D7xbdYMvXi5cbYFd0ZWG9Ff8P0ly5WwtLS7oyKY2AMPKQeJevopViih1AaJqx2A08TaRFxjj4d0MoyuUDR29xYYgV%2F05DzmHvvlVo5gEV%2BeN2NkCpQOSnnt9KyrKskCzb%2FlDEgfJGHqNsVUJjc07T5v32yjjGFEzA93%2Fyy5ablngKW6mjm72Z005Mpgd2SULAboqrk8eRmEuQ%2FlSASrp9ptc%2FCybAfGrxrjB%2F1RSjwWUx%2BVDUGB1tbRytknv0VjPhvrTCui429BjqkAWmED3xDlgtHJUcmPDDvpwq%2BU1lwu5PRo7aJ9G2nsJ5s4SchV2TejVsoxAUcUzjzhNYdo1zpC4Z9GnEesldFp%2BDIe03yZJs3AXxRBn3jgbfHuAC%2FNg%2FHYXwbWlPQ5m31L%2BnNqj5XkWijKQh%2BH71XM07cRji5qFtzkFsgvcFja5CcQCAf79xKEm7vA001o5VvDNBxBPaObq3pModzkzIl31sBudYS&X-Amz-Signature=faeeb0680173ced01bda28e3db3bbcfb277b7ac868f76ec274d91720cc1c434b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TZKYRYG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCVfhSF%2BqX7wp2xgcZSvZoSCrnrzSF0wcCIBX4vOQF8gwIhAMhxIs4dQLHecjfFXQZpQ%2BQKnqw0G4StI1V1cMo%2FSImHKv8DCEQQABoMNjM3NDIzMTgzODA1IgznbhqqBWVKYemHkMEq3ANBmZHie1ejTrQRnccQD9WP3UMV2aaRcRQ%2Fo8TR7W9Q5EfkdcWJ4rQFHBojMAQHuJmlj4JgNKmyWW5%2Bxgyo8zjejVEpbR1eej7%2Bi8Uq6vzVvcdlEwnjbwPPwAHLW1bzJhhI0%2BjSjZ6gpbr1U%2BZ1xCJAaEYurWD7eJUgcwHqiHMkXCEut8EezIgyxabOlm2nK7x5XJgn4oMdPjdIUGgJtk8clBN%2FOmaaA2Y%2FO546KNW8TafWUZcpjhyNX92O8IFtRuGKzK6FOfieJuJHeOgPmAWbJ8vReovpzfcXEOa500bs%2Fwl2P8FV%2FCJDr%2FBK%2FV%2Fm3LVbhAJ90r0FlnbUPhcDMR2VZZCkv4etHnUmLOt2hEnrtDNb91VIU5G916D7xbdYMvXi5cbYFd0ZWG9Ff8P0ly5WwtLS7oyKY2AMPKQeJevopViih1AaJqx2A08TaRFxjj4d0MoyuUDR29xYYgV%2F05DzmHvvlVo5gEV%2BeN2NkCpQOSnnt9KyrKskCzb%2FlDEgfJGHqNsVUJjc07T5v32yjjGFEzA93%2Fyy5ablngKW6mjm72Z005Mpgd2SULAboqrk8eRmEuQ%2FlSASrp9ptc%2FCybAfGrxrjB%2F1RSjwWUx%2BVDUGB1tbRytknv0VjPhvrTCui429BjqkAWmED3xDlgtHJUcmPDDvpwq%2BU1lwu5PRo7aJ9G2nsJ5s4SchV2TejVsoxAUcUzjzhNYdo1zpC4Z9GnEesldFp%2BDIe03yZJs3AXxRBn3jgbfHuAC%2FNg%2FHYXwbWlPQ5m31L%2BnNqj5XkWijKQh%2BH71XM07cRji5qFtzkFsgvcFja5CcQCAf79xKEm7vA001o5VvDNBxBPaObq3pModzkzIl31sBudYS&X-Amz-Signature=2b17bd30d52d82c5c052b634dce77d7882fff416d2f3adce793dbe1e32332f8c&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2J73T64%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQD4BM3%2F9c47uVQ7IfHYtvBuRc0TEeDQB8QtLP1Qs9G%2BJAIgK5%2FRPjqe7o%2BYwAQfSbfOxje90%2Bw2n0kjCz%2FIjf4ZcAcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDD6GrWQlHB0EGBGkwSrcA4t7YGcGeT6TBpRVn4HTxcsBtR3YQ3C7HXYsEVOI4aU9rkbTmvA%2Bm4lcBMxBdPJXHXT%2BX9IMuTxYMCmhM1Oy31xxuLQGKWw9m22Mr%2F3eBkIKIP4ss3gMHHEXUFhwaYt6royQuOuHvTTA0DeU4bseM7IQudW5zQX3dt%2B0xsv%2F2Ag1LGSU9Bx22NXKfFHvkAme7K9qv3ZZhpJcjPLjN3yF%2BGoeTxP8nwaGpHUmEmYIHmparevFchM7wc79NxoiR5BcyoQfjLYO6KUY9jVb%2FHp0YWAdah4MjTf9CiPKMoTsFyAl0%2F6Fj3zW2OwFYU2leatuZHYGcPiPKC2aKCw%2F2sm8yLY6bPMg7PigeXQQ2%2Bti2JUj0YStw2DDuk3%2Bof1MJWOJDxQqMY3EQCTgWp7scNV6y8E%2F8kwycgEk8GvZYktw1QeTqcKYdD3asfBUzdRAE9N44A%2FTpmlXX4TrYZFVLlXLhNhqrWFCNkGQftZvV96DxdxYKGoawpcsVrFTKZ8KWFr4ZrQtsW%2BScm5kXw765Bz%2Fi%2BElx%2Bfx5cMUQdwIA1pUhJqz28lvN6dJDtfNh5o0x0AZ4%2BuPd8DmocBj6tyzHJi8jtCWLY9FANMLhovlfYjBqLLP0GF%2F3HkRbJsHkbD9MJmLjb0GOqUB3y6msOv77z6jUUqW4tj9DbxnGgrmuB4ECJXaKOJazmee3JYfOy5KIHHrhv9v4AM51iY9%2Falw973T2vDDHgwi0OIm3KDboak3rtkflz34DhfVPQq3GGd2PQLU9gJa%2FGulxtv24FqWQ32lmvwQ1E8aXK4At6q06qJvq34FL7k95MNri1lVMHHrrANAGep8D96ooXg9aUZkcfe4NAn5BDQN2%2BnVMgpj&X-Amz-Signature=cfcbfad726c69941834f457f766105abc3c5b8e41074945d0e02b312205264d0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2J73T64%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQD4BM3%2F9c47uVQ7IfHYtvBuRc0TEeDQB8QtLP1Qs9G%2BJAIgK5%2FRPjqe7o%2BYwAQfSbfOxje90%2Bw2n0kjCz%2FIjf4ZcAcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDD6GrWQlHB0EGBGkwSrcA4t7YGcGeT6TBpRVn4HTxcsBtR3YQ3C7HXYsEVOI4aU9rkbTmvA%2Bm4lcBMxBdPJXHXT%2BX9IMuTxYMCmhM1Oy31xxuLQGKWw9m22Mr%2F3eBkIKIP4ss3gMHHEXUFhwaYt6royQuOuHvTTA0DeU4bseM7IQudW5zQX3dt%2B0xsv%2F2Ag1LGSU9Bx22NXKfFHvkAme7K9qv3ZZhpJcjPLjN3yF%2BGoeTxP8nwaGpHUmEmYIHmparevFchM7wc79NxoiR5BcyoQfjLYO6KUY9jVb%2FHp0YWAdah4MjTf9CiPKMoTsFyAl0%2F6Fj3zW2OwFYU2leatuZHYGcPiPKC2aKCw%2F2sm8yLY6bPMg7PigeXQQ2%2Bti2JUj0YStw2DDuk3%2Bof1MJWOJDxQqMY3EQCTgWp7scNV6y8E%2F8kwycgEk8GvZYktw1QeTqcKYdD3asfBUzdRAE9N44A%2FTpmlXX4TrYZFVLlXLhNhqrWFCNkGQftZvV96DxdxYKGoawpcsVrFTKZ8KWFr4ZrQtsW%2BScm5kXw765Bz%2Fi%2BElx%2Bfx5cMUQdwIA1pUhJqz28lvN6dJDtfNh5o0x0AZ4%2BuPd8DmocBj6tyzHJi8jtCWLY9FANMLhovlfYjBqLLP0GF%2F3HkRbJsHkbD9MJmLjb0GOqUB3y6msOv77z6jUUqW4tj9DbxnGgrmuB4ECJXaKOJazmee3JYfOy5KIHHrhv9v4AM51iY9%2Falw973T2vDDHgwi0OIm3KDboak3rtkflz34DhfVPQq3GGd2PQLU9gJa%2FGulxtv24FqWQ32lmvwQ1E8aXK4At6q06qJvq34FL7k95MNri1lVMHHrrANAGep8D96ooXg9aUZkcfe4NAn5BDQN2%2BnVMgpj&X-Amz-Signature=f06c1a9668ec86ef393933cad6b1b7e9d01d061b1b36f05785d4e8849551db48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TZKYRYG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCVfhSF%2BqX7wp2xgcZSvZoSCrnrzSF0wcCIBX4vOQF8gwIhAMhxIs4dQLHecjfFXQZpQ%2BQKnqw0G4StI1V1cMo%2FSImHKv8DCEQQABoMNjM3NDIzMTgzODA1IgznbhqqBWVKYemHkMEq3ANBmZHie1ejTrQRnccQD9WP3UMV2aaRcRQ%2Fo8TR7W9Q5EfkdcWJ4rQFHBojMAQHuJmlj4JgNKmyWW5%2Bxgyo8zjejVEpbR1eej7%2Bi8Uq6vzVvcdlEwnjbwPPwAHLW1bzJhhI0%2BjSjZ6gpbr1U%2BZ1xCJAaEYurWD7eJUgcwHqiHMkXCEut8EezIgyxabOlm2nK7x5XJgn4oMdPjdIUGgJtk8clBN%2FOmaaA2Y%2FO546KNW8TafWUZcpjhyNX92O8IFtRuGKzK6FOfieJuJHeOgPmAWbJ8vReovpzfcXEOa500bs%2Fwl2P8FV%2FCJDr%2FBK%2FV%2Fm3LVbhAJ90r0FlnbUPhcDMR2VZZCkv4etHnUmLOt2hEnrtDNb91VIU5G916D7xbdYMvXi5cbYFd0ZWG9Ff8P0ly5WwtLS7oyKY2AMPKQeJevopViih1AaJqx2A08TaRFxjj4d0MoyuUDR29xYYgV%2F05DzmHvvlVo5gEV%2BeN2NkCpQOSnnt9KyrKskCzb%2FlDEgfJGHqNsVUJjc07T5v32yjjGFEzA93%2Fyy5ablngKW6mjm72Z005Mpgd2SULAboqrk8eRmEuQ%2FlSASrp9ptc%2FCybAfGrxrjB%2F1RSjwWUx%2BVDUGB1tbRytknv0VjPhvrTCui429BjqkAWmED3xDlgtHJUcmPDDvpwq%2BU1lwu5PRo7aJ9G2nsJ5s4SchV2TejVsoxAUcUzjzhNYdo1zpC4Z9GnEesldFp%2BDIe03yZJs3AXxRBn3jgbfHuAC%2FNg%2FHYXwbWlPQ5m31L%2BnNqj5XkWijKQh%2BH71XM07cRji5qFtzkFsgvcFja5CcQCAf79xKEm7vA001o5VvDNBxBPaObq3pModzkzIl31sBudYS&X-Amz-Signature=b432d40435d1f9b609760c74b398dc65847243bd6815b2e93a26ed99a897b2e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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