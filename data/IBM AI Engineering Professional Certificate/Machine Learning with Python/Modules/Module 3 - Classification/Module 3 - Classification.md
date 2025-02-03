

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUPNOELQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIDn4WWIfTQYNkcCHleb3SxZYGGsXA7FzrGfrZyklBWOGAiBRavmXF0R7uugHNJ0AHJs8ED2z%2FbhpIsYucc6SXcuGvyr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMbpm0LaV2wS0SG66aKtwDaf6R%2FsiKJjfTDd2fh2unqW09EZAZ6Gn5nvEubSx59r5qdD5Vf8tH9NeTWiJopVsQXbrAMTQiyDofopNEuyq0sM49D4jUMSU3%2BtWHxe41QWJzVP3ZjXL7tMNH5htAFZ16wq0oiSaRjxYmWe0bM%2BVLn8KBTcDd%2BqJ0l%2BRZ2jRYN3ImDWPWTtK32w0CYvNFwZSGH8t9QBZS3W35IFyljM9eoB54SbudipV4MymZgHmEpSe4Brnyvq6wRKLrEGJ2WBk3Eyb1LZlVKFCrvzssgJ%2F4cJ1bXNulAo2DOOA4t%2FTNAJK5cc3d2w7zxJhO6qRwtbIZ95CUC7u9o7H26edg6%2FhOHoJi5ZuP0BdaBRxeNkGDCk4aUMvLiJGbIprqY428Ao2bvu8FJv%2Fy8p8cvrG5k%2B6YbxOyHXzDRmv%2FpLdWh%2F7DDMexGH47p7Ojq%2Fp0P8I3Nj8HhN32giuXFpqagVFfhRekxoN1EpocW5CizI8HYnWbs5rEUbMI3GJ5MoQnZNMjLRDOnJUMi1MSSWFYb6ZRfbwnCyC%2BciZ%2FkuaM6tmonFl9zLE2QF%2FjYbgYl%2Fc5Fcb9RJAU0Vq0Yos6Dp31kuS%2FC%2B%2B5UKIlVdzq7XhqpqnV8MbVGlqwMA3UIi%2FaTU29jDsw34OEvQY6pgHG0RN23TogBBpWBHmpeZwEQ5cQjAtAQ3n4cgeRTTRuheRCSCGLUceCljQYyTc9EOoWza2twAF7dND718S4t2XonP83IensIurImxqcS7ErtCzU5i1C%2BA2yNumccTY2G6rWkRnXlXt6tA%2Bfq0UHQpN5yWzg8TM9wtBShCfCIkX5bY3%2FnkFbth4iKZiDzNPH6G2dcE1n3IiyBHd98T3ZzYlYIcT%2BGVE%2B&X-Amz-Signature=ea5f499a16f431baf8438e24ef891bfd0226b00eeeff31e60c41d40deb580403&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUPNOELQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIDn4WWIfTQYNkcCHleb3SxZYGGsXA7FzrGfrZyklBWOGAiBRavmXF0R7uugHNJ0AHJs8ED2z%2FbhpIsYucc6SXcuGvyr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMbpm0LaV2wS0SG66aKtwDaf6R%2FsiKJjfTDd2fh2unqW09EZAZ6Gn5nvEubSx59r5qdD5Vf8tH9NeTWiJopVsQXbrAMTQiyDofopNEuyq0sM49D4jUMSU3%2BtWHxe41QWJzVP3ZjXL7tMNH5htAFZ16wq0oiSaRjxYmWe0bM%2BVLn8KBTcDd%2BqJ0l%2BRZ2jRYN3ImDWPWTtK32w0CYvNFwZSGH8t9QBZS3W35IFyljM9eoB54SbudipV4MymZgHmEpSe4Brnyvq6wRKLrEGJ2WBk3Eyb1LZlVKFCrvzssgJ%2F4cJ1bXNulAo2DOOA4t%2FTNAJK5cc3d2w7zxJhO6qRwtbIZ95CUC7u9o7H26edg6%2FhOHoJi5ZuP0BdaBRxeNkGDCk4aUMvLiJGbIprqY428Ao2bvu8FJv%2Fy8p8cvrG5k%2B6YbxOyHXzDRmv%2FpLdWh%2F7DDMexGH47p7Ojq%2Fp0P8I3Nj8HhN32giuXFpqagVFfhRekxoN1EpocW5CizI8HYnWbs5rEUbMI3GJ5MoQnZNMjLRDOnJUMi1MSSWFYb6ZRfbwnCyC%2BciZ%2FkuaM6tmonFl9zLE2QF%2FjYbgYl%2Fc5Fcb9RJAU0Vq0Yos6Dp31kuS%2FC%2B%2B5UKIlVdzq7XhqpqnV8MbVGlqwMA3UIi%2FaTU29jDsw34OEvQY6pgHG0RN23TogBBpWBHmpeZwEQ5cQjAtAQ3n4cgeRTTRuheRCSCGLUceCljQYyTc9EOoWza2twAF7dND718S4t2XonP83IensIurImxqcS7ErtCzU5i1C%2BA2yNumccTY2G6rWkRnXlXt6tA%2Bfq0UHQpN5yWzg8TM9wtBShCfCIkX5bY3%2FnkFbth4iKZiDzNPH6G2dcE1n3IiyBHd98T3ZzYlYIcT%2BGVE%2B&X-Amz-Signature=bcfaedcdd3c5b9ac1f6d3cffa5a40dd9de63cd3a33cc229e0b880a28c6a2e007&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUPNOELQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIDn4WWIfTQYNkcCHleb3SxZYGGsXA7FzrGfrZyklBWOGAiBRavmXF0R7uugHNJ0AHJs8ED2z%2FbhpIsYucc6SXcuGvyr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMbpm0LaV2wS0SG66aKtwDaf6R%2FsiKJjfTDd2fh2unqW09EZAZ6Gn5nvEubSx59r5qdD5Vf8tH9NeTWiJopVsQXbrAMTQiyDofopNEuyq0sM49D4jUMSU3%2BtWHxe41QWJzVP3ZjXL7tMNH5htAFZ16wq0oiSaRjxYmWe0bM%2BVLn8KBTcDd%2BqJ0l%2BRZ2jRYN3ImDWPWTtK32w0CYvNFwZSGH8t9QBZS3W35IFyljM9eoB54SbudipV4MymZgHmEpSe4Brnyvq6wRKLrEGJ2WBk3Eyb1LZlVKFCrvzssgJ%2F4cJ1bXNulAo2DOOA4t%2FTNAJK5cc3d2w7zxJhO6qRwtbIZ95CUC7u9o7H26edg6%2FhOHoJi5ZuP0BdaBRxeNkGDCk4aUMvLiJGbIprqY428Ao2bvu8FJv%2Fy8p8cvrG5k%2B6YbxOyHXzDRmv%2FpLdWh%2F7DDMexGH47p7Ojq%2Fp0P8I3Nj8HhN32giuXFpqagVFfhRekxoN1EpocW5CizI8HYnWbs5rEUbMI3GJ5MoQnZNMjLRDOnJUMi1MSSWFYb6ZRfbwnCyC%2BciZ%2FkuaM6tmonFl9zLE2QF%2FjYbgYl%2Fc5Fcb9RJAU0Vq0Yos6Dp31kuS%2FC%2B%2B5UKIlVdzq7XhqpqnV8MbVGlqwMA3UIi%2FaTU29jDsw34OEvQY6pgHG0RN23TogBBpWBHmpeZwEQ5cQjAtAQ3n4cgeRTTRuheRCSCGLUceCljQYyTc9EOoWza2twAF7dND718S4t2XonP83IensIurImxqcS7ErtCzU5i1C%2BA2yNumccTY2G6rWkRnXlXt6tA%2Bfq0UHQpN5yWzg8TM9wtBShCfCIkX5bY3%2FnkFbth4iKZiDzNPH6G2dcE1n3IiyBHd98T3ZzYlYIcT%2BGVE%2B&X-Amz-Signature=74b1f06e850bcba48598516c40459d4c1ac1c000ba8ebd987b1ac181fa2f9245&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQBQONEV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCmybqCEbxMSXLW8ZUe2nTP1vaqrleIgB2QHwb9qy3VKgIgfoPB4rdZPy%2F6gf0kwJ58Llrm9n%2FuvsF5iiXqNs%2F6UnUq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDMVGQay2oUnzyISvaCrcAz0O4AXfHnx6Oh2QhhhxaKSe6DLfZjLizIuJITJywGSnPeFcD4BBqR29FGuhxjww6A8GdgrqbbHUzte9yvOHqsZQA%2BfTJSizf1gg51ZNdpQCIPiNtoHPg%2BElC5xXssvJ4NNVFifcG4IryOZWZKuFHtodYE22bEzUZg2%2FORwGCI1J05iQbDu0ebmWBFv5AGeSoRPWzlw7djpo3Se8tB%2BJ2ctzfo6ZAQL5X4%2B0EArWsr2huR7LBP6iO8VXsJmRzOzJC8hak9J7zQSPPG%2FA8cNfDTfXpjx2uFY6RqOjzA5BMckpp4VYhwQBhFCgLdBIsQ%2FbLZdqlzuVux3LR%2BHxDzMuY%2BiWTmWv%2Beu8q6jC7eCTyDe%2BJ39SkgCl17pAnvz8%2F1E1oqhy8bgBOldTqiZsxQc5zJ1EoyruCS%2FzASycLSk8P8v0JT9r4CUzSJT%2FduMMIiskUOvw%2FBsNbxssfnxrw82vKakMJZn1wJN9kqnTJWeGFQQG%2F23jfJt2WRoRg7F9YuTnpdqVlw0a%2BD%2FIzMrkUfBKrN3mMD2jyMQpSDyEGDBSAOl3CED0M6gTXYHLDVHvXKtnqpx9ewlANWJoCkW75pz6why%2FBfh3EDA4q2veNm4UykZWSsS1L0znPKnjG4bdMMmDhL0GOqUBkyJVRY%2B1G3aBboeKk8%2BPsCrpbMCfKWVtjiyZ33c76mdH43QFfrxzpIqht4VYDCejjhFF8QlwsenfVYO%2Fdo5RqGRKvGOgLObftwtcvLpCpADti39BMikDO0f29b28isNlvOkGvIpbTlQTw6lJk4ErFCUdP2EkKaGhontYua%2FWdj5ofLNz3SAtdvckiuA77L16Cq4XTeda4aidF%2BgeU2%2B4m%2B%2FwYiR%2B&X-Amz-Signature=d1253a7f063f5e84c0a2f0d1132b818f6d7d91b2c60e175bdc2b263d37b7d4a1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQBQONEV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCmybqCEbxMSXLW8ZUe2nTP1vaqrleIgB2QHwb9qy3VKgIgfoPB4rdZPy%2F6gf0kwJ58Llrm9n%2FuvsF5iiXqNs%2F6UnUq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDMVGQay2oUnzyISvaCrcAz0O4AXfHnx6Oh2QhhhxaKSe6DLfZjLizIuJITJywGSnPeFcD4BBqR29FGuhxjww6A8GdgrqbbHUzte9yvOHqsZQA%2BfTJSizf1gg51ZNdpQCIPiNtoHPg%2BElC5xXssvJ4NNVFifcG4IryOZWZKuFHtodYE22bEzUZg2%2FORwGCI1J05iQbDu0ebmWBFv5AGeSoRPWzlw7djpo3Se8tB%2BJ2ctzfo6ZAQL5X4%2B0EArWsr2huR7LBP6iO8VXsJmRzOzJC8hak9J7zQSPPG%2FA8cNfDTfXpjx2uFY6RqOjzA5BMckpp4VYhwQBhFCgLdBIsQ%2FbLZdqlzuVux3LR%2BHxDzMuY%2BiWTmWv%2Beu8q6jC7eCTyDe%2BJ39SkgCl17pAnvz8%2F1E1oqhy8bgBOldTqiZsxQc5zJ1EoyruCS%2FzASycLSk8P8v0JT9r4CUzSJT%2FduMMIiskUOvw%2FBsNbxssfnxrw82vKakMJZn1wJN9kqnTJWeGFQQG%2F23jfJt2WRoRg7F9YuTnpdqVlw0a%2BD%2FIzMrkUfBKrN3mMD2jyMQpSDyEGDBSAOl3CED0M6gTXYHLDVHvXKtnqpx9ewlANWJoCkW75pz6why%2FBfh3EDA4q2veNm4UykZWSsS1L0znPKnjG4bdMMmDhL0GOqUBkyJVRY%2B1G3aBboeKk8%2BPsCrpbMCfKWVtjiyZ33c76mdH43QFfrxzpIqht4VYDCejjhFF8QlwsenfVYO%2Fdo5RqGRKvGOgLObftwtcvLpCpADti39BMikDO0f29b28isNlvOkGvIpbTlQTw6lJk4ErFCUdP2EkKaGhontYua%2FWdj5ofLNz3SAtdvckiuA77L16Cq4XTeda4aidF%2BgeU2%2B4m%2B%2FwYiR%2B&X-Amz-Signature=b0d3ec9ecde5f1be120b73b112d730838dcf0996cb8a065b872ec8730efbafe9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUPNOELQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIDn4WWIfTQYNkcCHleb3SxZYGGsXA7FzrGfrZyklBWOGAiBRavmXF0R7uugHNJ0AHJs8ED2z%2FbhpIsYucc6SXcuGvyr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMbpm0LaV2wS0SG66aKtwDaf6R%2FsiKJjfTDd2fh2unqW09EZAZ6Gn5nvEubSx59r5qdD5Vf8tH9NeTWiJopVsQXbrAMTQiyDofopNEuyq0sM49D4jUMSU3%2BtWHxe41QWJzVP3ZjXL7tMNH5htAFZ16wq0oiSaRjxYmWe0bM%2BVLn8KBTcDd%2BqJ0l%2BRZ2jRYN3ImDWPWTtK32w0CYvNFwZSGH8t9QBZS3W35IFyljM9eoB54SbudipV4MymZgHmEpSe4Brnyvq6wRKLrEGJ2WBk3Eyb1LZlVKFCrvzssgJ%2F4cJ1bXNulAo2DOOA4t%2FTNAJK5cc3d2w7zxJhO6qRwtbIZ95CUC7u9o7H26edg6%2FhOHoJi5ZuP0BdaBRxeNkGDCk4aUMvLiJGbIprqY428Ao2bvu8FJv%2Fy8p8cvrG5k%2B6YbxOyHXzDRmv%2FpLdWh%2F7DDMexGH47p7Ojq%2Fp0P8I3Nj8HhN32giuXFpqagVFfhRekxoN1EpocW5CizI8HYnWbs5rEUbMI3GJ5MoQnZNMjLRDOnJUMi1MSSWFYb6ZRfbwnCyC%2BciZ%2FkuaM6tmonFl9zLE2QF%2FjYbgYl%2Fc5Fcb9RJAU0Vq0Yos6Dp31kuS%2FC%2B%2B5UKIlVdzq7XhqpqnV8MbVGlqwMA3UIi%2FaTU29jDsw34OEvQY6pgHG0RN23TogBBpWBHmpeZwEQ5cQjAtAQ3n4cgeRTTRuheRCSCGLUceCljQYyTc9EOoWza2twAF7dND718S4t2XonP83IensIurImxqcS7ErtCzU5i1C%2BA2yNumccTY2G6rWkRnXlXt6tA%2Bfq0UHQpN5yWzg8TM9wtBShCfCIkX5bY3%2FnkFbth4iKZiDzNPH6G2dcE1n3IiyBHd98T3ZzYlYIcT%2BGVE%2B&X-Amz-Signature=85df96a24c0930cf16e484429ae334a03d95f67ee3547ade9884454be1f0544a&X-Amz-SignedHeaders=host&x-id=GetObject)
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