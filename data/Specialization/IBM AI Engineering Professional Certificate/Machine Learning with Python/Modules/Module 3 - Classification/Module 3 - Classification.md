

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTJ4YUNM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJsLopkbxGNvHH00WoPSYBzqCqy%2ByjeoXpFA9YI7lpNgIhAPXgjaa%2FOKaRLszj2cnVO7pquMCfPy2%2FHywhnvvYANGZKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwwGEIUS%2BdMlFE6RjIq3ANLu0KK5Eh3di64zBz1Eukq6ld1Kw1VcfAXVk%2FpWL%2FaRCJnZQW1Ctrw1bArFf8R5wgH6eMlHJHdD7TV3SKFTdqlhOL76Hhz5kP2O9h524ODgZjk0HmbQzv4fcqVPOUgwSz0FKX96crWecYqniGhoqRa%2FpFNXxdRYaeJeflz5TBgaFPDfeKVxASTIqsNazMCi1sGdNtzpm9WV8RycvzioiniFPU2rRIKTPtib2qDTm7icdEiZy%2BsRdyuO26piWOuESJC7EBGjjArd6%2BEYF3vb%2B38N%2BNWlAu9yK4GDcDCIvyQiJYt1KQhlA1IoTlsbrwiYQ2HZk11r3FaEk32KSWdwxdzTFad7eUmw7LuHFWTsNliW%2B6BaaoFBGXvnhkvgojk2IVxKKDnGIYnNb2x%2Fwg0APYh57%2BEUGNW8HxUHNg1vYmysDNVX4FynqGSVJMgutFr7aS0oYz5ZHaEjwj2nFThP8DfeRGBYFUVdWOnA952lh5ltQeRaoyBzzPw5a5iPkzNJgoAWmta%2BhKTS%2BjPERnQGeMgmm%2Fh7OfXxsRk%2BrqU6lMIOsMKsiiyjNvn7x%2FKQp44%2BUs6P9lbGwg33sadCGsOyGiHM%2BcW7jwnBeisoVBNZz6jiixN%2BdCd2N%2FH%2B6nHMzCMvOm8BjqkAR%2BS44o0fd3CxVGZeug6PxhQC1cFV2SXy7mpdJVfe4QUve4GugMKMl2qtwK8pkxzwy18hQH9M2kDIg4ssYFMz%2FLkDEqhaUjH6L8tHrZyhgFly9np97xfLD7y6OeAYDKOYtLyf4MNknWQteoucSOYikT%2B76qF9Xn0BJpD6p4PCIa6DFQ%2B64jwY%2FEc3CKCbX7YbtbVllLGvVhHBdQ0Mg5urkJZlNb2&X-Amz-Signature=e2cc1d2600c065c0a0f8a2901736ba4226133c44df4c4ef87226a08f8727b4a2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTJ4YUNM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJsLopkbxGNvHH00WoPSYBzqCqy%2ByjeoXpFA9YI7lpNgIhAPXgjaa%2FOKaRLszj2cnVO7pquMCfPy2%2FHywhnvvYANGZKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwwGEIUS%2BdMlFE6RjIq3ANLu0KK5Eh3di64zBz1Eukq6ld1Kw1VcfAXVk%2FpWL%2FaRCJnZQW1Ctrw1bArFf8R5wgH6eMlHJHdD7TV3SKFTdqlhOL76Hhz5kP2O9h524ODgZjk0HmbQzv4fcqVPOUgwSz0FKX96crWecYqniGhoqRa%2FpFNXxdRYaeJeflz5TBgaFPDfeKVxASTIqsNazMCi1sGdNtzpm9WV8RycvzioiniFPU2rRIKTPtib2qDTm7icdEiZy%2BsRdyuO26piWOuESJC7EBGjjArd6%2BEYF3vb%2B38N%2BNWlAu9yK4GDcDCIvyQiJYt1KQhlA1IoTlsbrwiYQ2HZk11r3FaEk32KSWdwxdzTFad7eUmw7LuHFWTsNliW%2B6BaaoFBGXvnhkvgojk2IVxKKDnGIYnNb2x%2Fwg0APYh57%2BEUGNW8HxUHNg1vYmysDNVX4FynqGSVJMgutFr7aS0oYz5ZHaEjwj2nFThP8DfeRGBYFUVdWOnA952lh5ltQeRaoyBzzPw5a5iPkzNJgoAWmta%2BhKTS%2BjPERnQGeMgmm%2Fh7OfXxsRk%2BrqU6lMIOsMKsiiyjNvn7x%2FKQp44%2BUs6P9lbGwg33sadCGsOyGiHM%2BcW7jwnBeisoVBNZz6jiixN%2BdCd2N%2FH%2B6nHMzCMvOm8BjqkAR%2BS44o0fd3CxVGZeug6PxhQC1cFV2SXy7mpdJVfe4QUve4GugMKMl2qtwK8pkxzwy18hQH9M2kDIg4ssYFMz%2FLkDEqhaUjH6L8tHrZyhgFly9np97xfLD7y6OeAYDKOYtLyf4MNknWQteoucSOYikT%2B76qF9Xn0BJpD6p4PCIa6DFQ%2B64jwY%2FEc3CKCbX7YbtbVllLGvVhHBdQ0Mg5urkJZlNb2&X-Amz-Signature=9bf36b1edbc0c0b27070715d6fa923677840174cec9a7048afe52750ab3e9398&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTJ4YUNM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJsLopkbxGNvHH00WoPSYBzqCqy%2ByjeoXpFA9YI7lpNgIhAPXgjaa%2FOKaRLszj2cnVO7pquMCfPy2%2FHywhnvvYANGZKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwwGEIUS%2BdMlFE6RjIq3ANLu0KK5Eh3di64zBz1Eukq6ld1Kw1VcfAXVk%2FpWL%2FaRCJnZQW1Ctrw1bArFf8R5wgH6eMlHJHdD7TV3SKFTdqlhOL76Hhz5kP2O9h524ODgZjk0HmbQzv4fcqVPOUgwSz0FKX96crWecYqniGhoqRa%2FpFNXxdRYaeJeflz5TBgaFPDfeKVxASTIqsNazMCi1sGdNtzpm9WV8RycvzioiniFPU2rRIKTPtib2qDTm7icdEiZy%2BsRdyuO26piWOuESJC7EBGjjArd6%2BEYF3vb%2B38N%2BNWlAu9yK4GDcDCIvyQiJYt1KQhlA1IoTlsbrwiYQ2HZk11r3FaEk32KSWdwxdzTFad7eUmw7LuHFWTsNliW%2B6BaaoFBGXvnhkvgojk2IVxKKDnGIYnNb2x%2Fwg0APYh57%2BEUGNW8HxUHNg1vYmysDNVX4FynqGSVJMgutFr7aS0oYz5ZHaEjwj2nFThP8DfeRGBYFUVdWOnA952lh5ltQeRaoyBzzPw5a5iPkzNJgoAWmta%2BhKTS%2BjPERnQGeMgmm%2Fh7OfXxsRk%2BrqU6lMIOsMKsiiyjNvn7x%2FKQp44%2BUs6P9lbGwg33sadCGsOyGiHM%2BcW7jwnBeisoVBNZz6jiixN%2BdCd2N%2FH%2B6nHMzCMvOm8BjqkAR%2BS44o0fd3CxVGZeug6PxhQC1cFV2SXy7mpdJVfe4QUve4GugMKMl2qtwK8pkxzwy18hQH9M2kDIg4ssYFMz%2FLkDEqhaUjH6L8tHrZyhgFly9np97xfLD7y6OeAYDKOYtLyf4MNknWQteoucSOYikT%2B76qF9Xn0BJpD6p4PCIa6DFQ%2B64jwY%2FEc3CKCbX7YbtbVllLGvVhHBdQ0Mg5urkJZlNb2&X-Amz-Signature=c1f8e52ed7850c23937487295a82662205f3c3eef552775b4f7352fafcacaad9&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBIOQ2JD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFbFaxDz95Zu2WsKKmriWglWtgdBtRMWgq7x0R1DIwJJAiAgAo2UxrdU8n%2FpzAJHSi%2FCJdF08P2s%2FL98LbdI2mo6DyqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiLQ74WcuGWRvBY5oKtwDgw76fnX7tuTTar6W7VnQpt%2FNjn7jiWLxWGjqpdcNLDGjDzSyxZrRjj6BKgJuFOSKX6fAvp%2BJB%2FiU%2FgKCNP5ytoAhOnj8ODrPZQ%2B7xD95QVmWMPxgMgMgOwj%2FY%2BPDEH%2FGDG6sQ4MLI7GtPEKl3%2FSl2vYVT3NdRtZs6mU7StNNqK0YRAaB7Bcuewn7y6eYUc72PMFy3ULy4vf5Hh1ebwit3YivG1WfmYY8NP9tOdpN35U6ksbjE%2FaFXYmqtTqeDG55nkGuCNvW1htb8RJA%2BCTVEP33N4N%2BRSAgsA102mmjLpaYx9gQVGsWOldUHS7RJNYRKVTaYe3hXPKGeqV9fMKoy7LhcbI2rX5%2Bseg7VmhucgHJjZlL8Xnka9NitIzFq9ASvKIUtYJwsUwmPYyTKPZKpVHmKvpuJbKMVzLLwtYxw31W%2B5%2BwIKpo9ztrctXDfGo%2FsBpWcPS2jyJOAjCo49O6ztQpLL1V6R1luAqWTirajP6tIa2GHN625OnUCM0MR9CI0zQdlTL6Tf7mfDk9PJ1UgHNraCW6EiYRbB5hKtDcwTYCzFpfHViBSBs9hJMxAx7OLQHTKlARdd%2BuOZDRPcXtnB%2FBrYju2PSLAsQk30f36wtPO0Jqrf4C%2B06L144wzbvpvAY6pgG76JQYC5L4Lji%2Bftlp2bEUeiPKtJGKtVmpq2qwTshNuy%2FV2PiH%2Bi71HJ%2FH%2BWBgLOVceE00eiEyJLlaOwOGoYLK730Jr8W2vxeeS8JP09pg%2FxZ2MD9yCTghNjt3wgeYYwsDhBCUN0Tbe5t9195h9B7X%2Fd7BqATpEw%2Bk0IQcgMTrboN2ZwledBF2%2FyfokN%2FYUPvUtrPT%2FIv1rDdYCr%2FFfadcmWUQdMcJ&X-Amz-Signature=f133b8b78942bcd11905fb3d93d0982ba25e64301584fbe20753ee1595d4439f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBIOQ2JD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFbFaxDz95Zu2WsKKmriWglWtgdBtRMWgq7x0R1DIwJJAiAgAo2UxrdU8n%2FpzAJHSi%2FCJdF08P2s%2FL98LbdI2mo6DyqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiLQ74WcuGWRvBY5oKtwDgw76fnX7tuTTar6W7VnQpt%2FNjn7jiWLxWGjqpdcNLDGjDzSyxZrRjj6BKgJuFOSKX6fAvp%2BJB%2FiU%2FgKCNP5ytoAhOnj8ODrPZQ%2B7xD95QVmWMPxgMgMgOwj%2FY%2BPDEH%2FGDG6sQ4MLI7GtPEKl3%2FSl2vYVT3NdRtZs6mU7StNNqK0YRAaB7Bcuewn7y6eYUc72PMFy3ULy4vf5Hh1ebwit3YivG1WfmYY8NP9tOdpN35U6ksbjE%2FaFXYmqtTqeDG55nkGuCNvW1htb8RJA%2BCTVEP33N4N%2BRSAgsA102mmjLpaYx9gQVGsWOldUHS7RJNYRKVTaYe3hXPKGeqV9fMKoy7LhcbI2rX5%2Bseg7VmhucgHJjZlL8Xnka9NitIzFq9ASvKIUtYJwsUwmPYyTKPZKpVHmKvpuJbKMVzLLwtYxw31W%2B5%2BwIKpo9ztrctXDfGo%2FsBpWcPS2jyJOAjCo49O6ztQpLL1V6R1luAqWTirajP6tIa2GHN625OnUCM0MR9CI0zQdlTL6Tf7mfDk9PJ1UgHNraCW6EiYRbB5hKtDcwTYCzFpfHViBSBs9hJMxAx7OLQHTKlARdd%2BuOZDRPcXtnB%2FBrYju2PSLAsQk30f36wtPO0Jqrf4C%2B06L144wzbvpvAY6pgG76JQYC5L4Lji%2Bftlp2bEUeiPKtJGKtVmpq2qwTshNuy%2FV2PiH%2Bi71HJ%2FH%2BWBgLOVceE00eiEyJLlaOwOGoYLK730Jr8W2vxeeS8JP09pg%2FxZ2MD9yCTghNjt3wgeYYwsDhBCUN0Tbe5t9195h9B7X%2Fd7BqATpEw%2Bk0IQcgMTrboN2ZwledBF2%2FyfokN%2FYUPvUtrPT%2FIv1rDdYCr%2FFfadcmWUQdMcJ&X-Amz-Signature=4d36a897844c6e2f0c6094efe50dab3d05457de05250b1367a49469e1604e267&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTJ4YUNM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJsLopkbxGNvHH00WoPSYBzqCqy%2ByjeoXpFA9YI7lpNgIhAPXgjaa%2FOKaRLszj2cnVO7pquMCfPy2%2FHywhnvvYANGZKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwwGEIUS%2BdMlFE6RjIq3ANLu0KK5Eh3di64zBz1Eukq6ld1Kw1VcfAXVk%2FpWL%2FaRCJnZQW1Ctrw1bArFf8R5wgH6eMlHJHdD7TV3SKFTdqlhOL76Hhz5kP2O9h524ODgZjk0HmbQzv4fcqVPOUgwSz0FKX96crWecYqniGhoqRa%2FpFNXxdRYaeJeflz5TBgaFPDfeKVxASTIqsNazMCi1sGdNtzpm9WV8RycvzioiniFPU2rRIKTPtib2qDTm7icdEiZy%2BsRdyuO26piWOuESJC7EBGjjArd6%2BEYF3vb%2B38N%2BNWlAu9yK4GDcDCIvyQiJYt1KQhlA1IoTlsbrwiYQ2HZk11r3FaEk32KSWdwxdzTFad7eUmw7LuHFWTsNliW%2B6BaaoFBGXvnhkvgojk2IVxKKDnGIYnNb2x%2Fwg0APYh57%2BEUGNW8HxUHNg1vYmysDNVX4FynqGSVJMgutFr7aS0oYz5ZHaEjwj2nFThP8DfeRGBYFUVdWOnA952lh5ltQeRaoyBzzPw5a5iPkzNJgoAWmta%2BhKTS%2BjPERnQGeMgmm%2Fh7OfXxsRk%2BrqU6lMIOsMKsiiyjNvn7x%2FKQp44%2BUs6P9lbGwg33sadCGsOyGiHM%2BcW7jwnBeisoVBNZz6jiixN%2BdCd2N%2FH%2B6nHMzCMvOm8BjqkAR%2BS44o0fd3CxVGZeug6PxhQC1cFV2SXy7mpdJVfe4QUve4GugMKMl2qtwK8pkxzwy18hQH9M2kDIg4ssYFMz%2FLkDEqhaUjH6L8tHrZyhgFly9np97xfLD7y6OeAYDKOYtLyf4MNknWQteoucSOYikT%2B76qF9Xn0BJpD6p4PCIa6DFQ%2B64jwY%2FEc3CKCbX7YbtbVllLGvVhHBdQ0Mg5urkJZlNb2&X-Amz-Signature=ca19ce26f7ed5450a37e2f655e7391507b9d69b5bed3dd2f1ceee84f4c4445e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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