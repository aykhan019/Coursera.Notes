

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRDQKJOD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIHAij%2FdnqMJNEJJpHwDFBhIwyfM3YGBpvehujNf5FmK%2FAiEAuViNnYVauEsTzYfcwYInyY%2BNRPt4zgJfYWLijU6HDcoq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDH3MnbyuGAvm55tLXyrcA%2F6yrFBtjA6GHuSjlpywt8G1hRubQ%2B4zKbhLmgZ3RTTbuWjxR6%2BQ%2FkKS9JbRFo9aDkgqbJBcwRnGNSXjxuDm%2FzgnrCG9k3Gka%2BAQ4eRjngu7M2j3OYp66IvOPNMpHuEhM3WXFLLGw2PpS0j38PbnSDJgIhzKj87QIrU2yMTx8VTpF3nEe%2BVf8dqjLf%2BWfvjp1juEsAv2rWmGjdwilsJd8Vb2gMMxv39vj58fkp8nLyLASqAudc2hAe3f3NXNrEoctJefS6pbE4dGPDdG6maRmvcljrBh%2FBUqsWrrAj%2F2fpWYJnwcRB38Quv2gzjIwqNfQMd8vC%2FvdtOCsYjYXjMsaifbzSouNhlvipHRg%2BhcbscW6jzFI%2B8mA%2BR2XHKgHvKYlgxW5ZNUzZ9ECNVP%2B5qcBo60uaxNV73zj%2FYm7aQQw11kggGC%2FBVxum1AAnOStcT%2FrCj4W5YKKTfR9Mck4Jl3ZLyFJY9tkklroOsnqKAtCtUaDD047%2FR8LEwD%2BS%2FQdJtcyMDqd%2F9isuRXKBuGNGxxsuDtp2U2BFGuh6s6XPRQVGMfSlA5CVzXk9LnRPxhfh5mhYKywZxw%2BGpKsDSM6cqCILbxYnjc5hKb3EYnb7e23AsDN5WCbodTO0Xct7HkMJ27jr0GOqUBDRMrykea0vDiFI6lCj%2F6S9b%2FsWX0YG%2Ft9swjW%2FtimwChLLyqiXy7XhSi4WGkZJO%2FFRR9hAjvYCzhYBwtsU5mk5bX%2BEGJs9FuaPRldTrt3p0AK12lLvlTfmUjwRM%2BBex6%2FWzwm1lrYH73nBeG2xHwo9sDKjgn3APRSRlkFeb%2FNFCiyn2txJea0zAuJmG%2FHzpgJh743xS9r9QVSbgrTN840SqPr3Mi&X-Amz-Signature=9dd5d0b0c4d4e9b002cc023d051018c1736f1e0f28c616ba263ef1c38d9b1d42&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRDQKJOD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIHAij%2FdnqMJNEJJpHwDFBhIwyfM3YGBpvehujNf5FmK%2FAiEAuViNnYVauEsTzYfcwYInyY%2BNRPt4zgJfYWLijU6HDcoq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDH3MnbyuGAvm55tLXyrcA%2F6yrFBtjA6GHuSjlpywt8G1hRubQ%2B4zKbhLmgZ3RTTbuWjxR6%2BQ%2FkKS9JbRFo9aDkgqbJBcwRnGNSXjxuDm%2FzgnrCG9k3Gka%2BAQ4eRjngu7M2j3OYp66IvOPNMpHuEhM3WXFLLGw2PpS0j38PbnSDJgIhzKj87QIrU2yMTx8VTpF3nEe%2BVf8dqjLf%2BWfvjp1juEsAv2rWmGjdwilsJd8Vb2gMMxv39vj58fkp8nLyLASqAudc2hAe3f3NXNrEoctJefS6pbE4dGPDdG6maRmvcljrBh%2FBUqsWrrAj%2F2fpWYJnwcRB38Quv2gzjIwqNfQMd8vC%2FvdtOCsYjYXjMsaifbzSouNhlvipHRg%2BhcbscW6jzFI%2B8mA%2BR2XHKgHvKYlgxW5ZNUzZ9ECNVP%2B5qcBo60uaxNV73zj%2FYm7aQQw11kggGC%2FBVxum1AAnOStcT%2FrCj4W5YKKTfR9Mck4Jl3ZLyFJY9tkklroOsnqKAtCtUaDD047%2FR8LEwD%2BS%2FQdJtcyMDqd%2F9isuRXKBuGNGxxsuDtp2U2BFGuh6s6XPRQVGMfSlA5CVzXk9LnRPxhfh5mhYKywZxw%2BGpKsDSM6cqCILbxYnjc5hKb3EYnb7e23AsDN5WCbodTO0Xct7HkMJ27jr0GOqUBDRMrykea0vDiFI6lCj%2F6S9b%2FsWX0YG%2Ft9swjW%2FtimwChLLyqiXy7XhSi4WGkZJO%2FFRR9hAjvYCzhYBwtsU5mk5bX%2BEGJs9FuaPRldTrt3p0AK12lLvlTfmUjwRM%2BBex6%2FWzwm1lrYH73nBeG2xHwo9sDKjgn3APRSRlkFeb%2FNFCiyn2txJea0zAuJmG%2FHzpgJh743xS9r9QVSbgrTN840SqPr3Mi&X-Amz-Signature=e98f699b301280dc2af183ec14db6527523cf2f6a259130af6d4dbf645d968c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRDQKJOD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIHAij%2FdnqMJNEJJpHwDFBhIwyfM3YGBpvehujNf5FmK%2FAiEAuViNnYVauEsTzYfcwYInyY%2BNRPt4zgJfYWLijU6HDcoq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDH3MnbyuGAvm55tLXyrcA%2F6yrFBtjA6GHuSjlpywt8G1hRubQ%2B4zKbhLmgZ3RTTbuWjxR6%2BQ%2FkKS9JbRFo9aDkgqbJBcwRnGNSXjxuDm%2FzgnrCG9k3Gka%2BAQ4eRjngu7M2j3OYp66IvOPNMpHuEhM3WXFLLGw2PpS0j38PbnSDJgIhzKj87QIrU2yMTx8VTpF3nEe%2BVf8dqjLf%2BWfvjp1juEsAv2rWmGjdwilsJd8Vb2gMMxv39vj58fkp8nLyLASqAudc2hAe3f3NXNrEoctJefS6pbE4dGPDdG6maRmvcljrBh%2FBUqsWrrAj%2F2fpWYJnwcRB38Quv2gzjIwqNfQMd8vC%2FvdtOCsYjYXjMsaifbzSouNhlvipHRg%2BhcbscW6jzFI%2B8mA%2BR2XHKgHvKYlgxW5ZNUzZ9ECNVP%2B5qcBo60uaxNV73zj%2FYm7aQQw11kggGC%2FBVxum1AAnOStcT%2FrCj4W5YKKTfR9Mck4Jl3ZLyFJY9tkklroOsnqKAtCtUaDD047%2FR8LEwD%2BS%2FQdJtcyMDqd%2F9isuRXKBuGNGxxsuDtp2U2BFGuh6s6XPRQVGMfSlA5CVzXk9LnRPxhfh5mhYKywZxw%2BGpKsDSM6cqCILbxYnjc5hKb3EYnb7e23AsDN5WCbodTO0Xct7HkMJ27jr0GOqUBDRMrykea0vDiFI6lCj%2F6S9b%2FsWX0YG%2Ft9swjW%2FtimwChLLyqiXy7XhSi4WGkZJO%2FFRR9hAjvYCzhYBwtsU5mk5bX%2BEGJs9FuaPRldTrt3p0AK12lLvlTfmUjwRM%2BBex6%2FWzwm1lrYH73nBeG2xHwo9sDKjgn3APRSRlkFeb%2FNFCiyn2txJea0zAuJmG%2FHzpgJh743xS9r9QVSbgrTN840SqPr3Mi&X-Amz-Signature=eac963c3672f2f687aa5cca8bcb23d10e899a49561469091f5f49f16506a86cf&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOIYHW73%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD%2F0LrKhG7Zz6oImMe4GSS583%2BwJHNCCujg6HupDRjDtgIhAPq5O30TbPHjuCgrkBpEliCBtmYxa5xcO70Rjh1D6QeNKv8DCEoQABoMNjM3NDIzMTgzODA1Igyj1RB5xmtI%2FM2XrJMq3APLB3KttsqQGUVN5P%2FCCCpvurYZx307Fhq30NWlFXNfekt7VBgxPDAmuOJiwywfn8TKdXu88o1L4y5b4b%2Fba1DRV2A897fA9O8qRtxOY2Gk9QfnatUNeEU%2BETpp6jeLCznnZlFx1wvIiC3VPi7B4ZYvt8OdYupaODHmrDgCMAtRpD59W%2FBoCzXIAwFzbsNLQ6RIK1LEwoy1sgIdAf5xbQ6aozHCxIpZxGpsRgJ1W6f6HR8yE4XBa2Iz1NmJadOdk4eZ9KzYspu91hWkA6cQRrglFS9ZEUMncF%2Bw7i6KH31PmkfK9LkMDzyS7fbe1bdNB4e5sDW1Alo2DqVyD9Gm6n6H%2BNa%2BQEU6D6WJ%2BXbJr3ShJzw525O8Sz911lqXs2wOFvAEIhtxd2fU44KWtt3OlpkD8d%2FHQAGSMRC9gI813jZFDfiTSTo1MOxkste0jOxo1WlgSp8ROHybbRYLc%2FTN4pOm5iFapL3o28kjvOvnC7bZRO%2BvrttpNkfsxxIcMTBfZUjo9lxIKQErb4a4vFekOkDyisiQD93L2SgjmkV6R%2FjgtKe57fQhvmLuMgCuW81jm3J9T4faV7dE1MGHdLoj0HRYrdEG2lwUWsJv9uKQIm0ue534sly7mRDxJOxwNjDbuo69BjqkARl2LP4Ewvo5xAbUR1yUDuTt2o%2B6qP%2B3V%2BkwfHnrkeP8Dls22Xf0TUQuaVAsD1cL7gk4c9ZypUNY7XJOHJvtHMVnoObLKnHjgDex6%2BRbOHjMzqxiXGqgBXeJp54zidpeODOjIPCDGWpQPYW94M5Np0SKEOpv5l0MddhT0FhYe6HxyN%2F6AjgaQpsG80F%2F9nGVXHqG%2FuEvQV%2BjSOSZKUdJAzs2h6Pz&X-Amz-Signature=0f7b505e3daa647fa8b4402181470944eebfcc0d12783b305e482d8af7daa140&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOIYHW73%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD%2F0LrKhG7Zz6oImMe4GSS583%2BwJHNCCujg6HupDRjDtgIhAPq5O30TbPHjuCgrkBpEliCBtmYxa5xcO70Rjh1D6QeNKv8DCEoQABoMNjM3NDIzMTgzODA1Igyj1RB5xmtI%2FM2XrJMq3APLB3KttsqQGUVN5P%2FCCCpvurYZx307Fhq30NWlFXNfekt7VBgxPDAmuOJiwywfn8TKdXu88o1L4y5b4b%2Fba1DRV2A897fA9O8qRtxOY2Gk9QfnatUNeEU%2BETpp6jeLCznnZlFx1wvIiC3VPi7B4ZYvt8OdYupaODHmrDgCMAtRpD59W%2FBoCzXIAwFzbsNLQ6RIK1LEwoy1sgIdAf5xbQ6aozHCxIpZxGpsRgJ1W6f6HR8yE4XBa2Iz1NmJadOdk4eZ9KzYspu91hWkA6cQRrglFS9ZEUMncF%2Bw7i6KH31PmkfK9LkMDzyS7fbe1bdNB4e5sDW1Alo2DqVyD9Gm6n6H%2BNa%2BQEU6D6WJ%2BXbJr3ShJzw525O8Sz911lqXs2wOFvAEIhtxd2fU44KWtt3OlpkD8d%2FHQAGSMRC9gI813jZFDfiTSTo1MOxkste0jOxo1WlgSp8ROHybbRYLc%2FTN4pOm5iFapL3o28kjvOvnC7bZRO%2BvrttpNkfsxxIcMTBfZUjo9lxIKQErb4a4vFekOkDyisiQD93L2SgjmkV6R%2FjgtKe57fQhvmLuMgCuW81jm3J9T4faV7dE1MGHdLoj0HRYrdEG2lwUWsJv9uKQIm0ue534sly7mRDxJOxwNjDbuo69BjqkARl2LP4Ewvo5xAbUR1yUDuTt2o%2B6qP%2B3V%2BkwfHnrkeP8Dls22Xf0TUQuaVAsD1cL7gk4c9ZypUNY7XJOHJvtHMVnoObLKnHjgDex6%2BRbOHjMzqxiXGqgBXeJp54zidpeODOjIPCDGWpQPYW94M5Np0SKEOpv5l0MddhT0FhYe6HxyN%2F6AjgaQpsG80F%2F9nGVXHqG%2FuEvQV%2BjSOSZKUdJAzs2h6Pz&X-Amz-Signature=bb5b39bf3af79aa51562b21bbad819a41187591a22d6fee07b935ed306282e1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRDQKJOD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIHAij%2FdnqMJNEJJpHwDFBhIwyfM3YGBpvehujNf5FmK%2FAiEAuViNnYVauEsTzYfcwYInyY%2BNRPt4zgJfYWLijU6HDcoq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDH3MnbyuGAvm55tLXyrcA%2F6yrFBtjA6GHuSjlpywt8G1hRubQ%2B4zKbhLmgZ3RTTbuWjxR6%2BQ%2FkKS9JbRFo9aDkgqbJBcwRnGNSXjxuDm%2FzgnrCG9k3Gka%2BAQ4eRjngu7M2j3OYp66IvOPNMpHuEhM3WXFLLGw2PpS0j38PbnSDJgIhzKj87QIrU2yMTx8VTpF3nEe%2BVf8dqjLf%2BWfvjp1juEsAv2rWmGjdwilsJd8Vb2gMMxv39vj58fkp8nLyLASqAudc2hAe3f3NXNrEoctJefS6pbE4dGPDdG6maRmvcljrBh%2FBUqsWrrAj%2F2fpWYJnwcRB38Quv2gzjIwqNfQMd8vC%2FvdtOCsYjYXjMsaifbzSouNhlvipHRg%2BhcbscW6jzFI%2B8mA%2BR2XHKgHvKYlgxW5ZNUzZ9ECNVP%2B5qcBo60uaxNV73zj%2FYm7aQQw11kggGC%2FBVxum1AAnOStcT%2FrCj4W5YKKTfR9Mck4Jl3ZLyFJY9tkklroOsnqKAtCtUaDD047%2FR8LEwD%2BS%2FQdJtcyMDqd%2F9isuRXKBuGNGxxsuDtp2U2BFGuh6s6XPRQVGMfSlA5CVzXk9LnRPxhfh5mhYKywZxw%2BGpKsDSM6cqCILbxYnjc5hKb3EYnb7e23AsDN5WCbodTO0Xct7HkMJ27jr0GOqUBDRMrykea0vDiFI6lCj%2F6S9b%2FsWX0YG%2Ft9swjW%2FtimwChLLyqiXy7XhSi4WGkZJO%2FFRR9hAjvYCzhYBwtsU5mk5bX%2BEGJs9FuaPRldTrt3p0AK12lLvlTfmUjwRM%2BBex6%2FWzwm1lrYH73nBeG2xHwo9sDKjgn3APRSRlkFeb%2FNFCiyn2txJea0zAuJmG%2FHzpgJh743xS9r9QVSbgrTN840SqPr3Mi&X-Amz-Signature=f395737502188b81d3f9d910e363ca34cf21cfac697156f0cc9115374d6287c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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