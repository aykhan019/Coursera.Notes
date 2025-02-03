

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP2B5WFQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNEIS7E00PrncZGYcEBrVMpfDad6zI9JyYm3GbReE%2FsAIhALZ0xjT68PaySBPkTCQ9bv1FrvebagQrLVANElrhfmv9KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRePOpMULEOUoo%2FcEq3ANjz77%2Bv5BP02%2BdRL%2BJ9gmmRdVkyHz6%2F42E7M0iAFpz0adAQA%2B0H6SxJkq6x6rX7JTi26GfE5hTW%2B4LBSUdcYK0%2FjEriq96SWCPnjkAaivBrErmzfc67y3cUb4X1mIg4QUVIP7Y7h1E%2Bn0%2BElVyx%2Fbj%2FD%2F17u5t1hkJ%2BcKyZFrcuxX3hTHOkbPyWF87RcMGTYTqezMUtZV%2FX9l3XOTt8ddPOAJQ6%2BKaGfyVlq%2BKC%2B1zmGgATeCQXzVJb8x1Q2tNda5wirGwQXF5IJSXviLqL5lhozAGPNzcziRKXmKLNSOguMsQXO54M9D12XJIdrFlzmCS%2F42DGnpxIBSne4WIUICCyZ%2BGXyjleGLfz5ZsgdskpXYsqAaQBOAu%2F9Sv5QFObTkbtuwLp4RaP1G2efGM0KtCLkjJCUzwVYQiKUmt3ZDOjnV2N%2BHMAdrS0L1sHOJCo%2BY7sZM8AXmofseVjJeTDWgwdfmon4U3VEmlJxkO7u5bX7SMNl7Hu0rbHZiIIlym1pbroVgrwg0OGzazlWPji%2BnZlNaLWnmSkjFL3o%2Fq3fiytE2HpSCVCg6dfJmdSba8CI0eK0p9mKdADQWjp8Iv%2B%2BGPRNIcrzZ1q0a19riC4hoRx2Cb2%2FHo7hiAP8uCKjDBv4C9BjqkAbdadMNrLx4T%2Bhb%2ByTQ7LF9NlaUYSrUBmkOXI6iIAU%2BCUf76WrEIcJCtmpZ1GpTRaKpIWYbqwIRFQdGXZC1Nc2KAUUzvS7hnqmgdiKNu3RIN49iAwenNemQkC1Uvjd%2FnblI23%2FfCG2Q4%2BYnnvDjlHOjXyUABgiajXApFml0fWvw8NwDCZyi3BlU0DjpAxWgxoa1djMIIaoCr4qMfPx9KgZCt4%2B7d&X-Amz-Signature=2bbab1562f20f6bcdba290bf6e8d2f6202f291c75c6f71421b776502533a63fd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP2B5WFQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNEIS7E00PrncZGYcEBrVMpfDad6zI9JyYm3GbReE%2FsAIhALZ0xjT68PaySBPkTCQ9bv1FrvebagQrLVANElrhfmv9KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRePOpMULEOUoo%2FcEq3ANjz77%2Bv5BP02%2BdRL%2BJ9gmmRdVkyHz6%2F42E7M0iAFpz0adAQA%2B0H6SxJkq6x6rX7JTi26GfE5hTW%2B4LBSUdcYK0%2FjEriq96SWCPnjkAaivBrErmzfc67y3cUb4X1mIg4QUVIP7Y7h1E%2Bn0%2BElVyx%2Fbj%2FD%2F17u5t1hkJ%2BcKyZFrcuxX3hTHOkbPyWF87RcMGTYTqezMUtZV%2FX9l3XOTt8ddPOAJQ6%2BKaGfyVlq%2BKC%2B1zmGgATeCQXzVJb8x1Q2tNda5wirGwQXF5IJSXviLqL5lhozAGPNzcziRKXmKLNSOguMsQXO54M9D12XJIdrFlzmCS%2F42DGnpxIBSne4WIUICCyZ%2BGXyjleGLfz5ZsgdskpXYsqAaQBOAu%2F9Sv5QFObTkbtuwLp4RaP1G2efGM0KtCLkjJCUzwVYQiKUmt3ZDOjnV2N%2BHMAdrS0L1sHOJCo%2BY7sZM8AXmofseVjJeTDWgwdfmon4U3VEmlJxkO7u5bX7SMNl7Hu0rbHZiIIlym1pbroVgrwg0OGzazlWPji%2BnZlNaLWnmSkjFL3o%2Fq3fiytE2HpSCVCg6dfJmdSba8CI0eK0p9mKdADQWjp8Iv%2B%2BGPRNIcrzZ1q0a19riC4hoRx2Cb2%2FHo7hiAP8uCKjDBv4C9BjqkAbdadMNrLx4T%2Bhb%2ByTQ7LF9NlaUYSrUBmkOXI6iIAU%2BCUf76WrEIcJCtmpZ1GpTRaKpIWYbqwIRFQdGXZC1Nc2KAUUzvS7hnqmgdiKNu3RIN49iAwenNemQkC1Uvjd%2FnblI23%2FfCG2Q4%2BYnnvDjlHOjXyUABgiajXApFml0fWvw8NwDCZyi3BlU0DjpAxWgxoa1djMIIaoCr4qMfPx9KgZCt4%2B7d&X-Amz-Signature=98081b50be2f92e123d17dc092357077b4db70871d5e978213bc7419700fa4e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP2B5WFQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNEIS7E00PrncZGYcEBrVMpfDad6zI9JyYm3GbReE%2FsAIhALZ0xjT68PaySBPkTCQ9bv1FrvebagQrLVANElrhfmv9KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRePOpMULEOUoo%2FcEq3ANjz77%2Bv5BP02%2BdRL%2BJ9gmmRdVkyHz6%2F42E7M0iAFpz0adAQA%2B0H6SxJkq6x6rX7JTi26GfE5hTW%2B4LBSUdcYK0%2FjEriq96SWCPnjkAaivBrErmzfc67y3cUb4X1mIg4QUVIP7Y7h1E%2Bn0%2BElVyx%2Fbj%2FD%2F17u5t1hkJ%2BcKyZFrcuxX3hTHOkbPyWF87RcMGTYTqezMUtZV%2FX9l3XOTt8ddPOAJQ6%2BKaGfyVlq%2BKC%2B1zmGgATeCQXzVJb8x1Q2tNda5wirGwQXF5IJSXviLqL5lhozAGPNzcziRKXmKLNSOguMsQXO54M9D12XJIdrFlzmCS%2F42DGnpxIBSne4WIUICCyZ%2BGXyjleGLfz5ZsgdskpXYsqAaQBOAu%2F9Sv5QFObTkbtuwLp4RaP1G2efGM0KtCLkjJCUzwVYQiKUmt3ZDOjnV2N%2BHMAdrS0L1sHOJCo%2BY7sZM8AXmofseVjJeTDWgwdfmon4U3VEmlJxkO7u5bX7SMNl7Hu0rbHZiIIlym1pbroVgrwg0OGzazlWPji%2BnZlNaLWnmSkjFL3o%2Fq3fiytE2HpSCVCg6dfJmdSba8CI0eK0p9mKdADQWjp8Iv%2B%2BGPRNIcrzZ1q0a19riC4hoRx2Cb2%2FHo7hiAP8uCKjDBv4C9BjqkAbdadMNrLx4T%2Bhb%2ByTQ7LF9NlaUYSrUBmkOXI6iIAU%2BCUf76WrEIcJCtmpZ1GpTRaKpIWYbqwIRFQdGXZC1Nc2KAUUzvS7hnqmgdiKNu3RIN49iAwenNemQkC1Uvjd%2FnblI23%2FfCG2Q4%2BYnnvDjlHOjXyUABgiajXApFml0fWvw8NwDCZyi3BlU0DjpAxWgxoa1djMIIaoCr4qMfPx9KgZCt4%2B7d&X-Amz-Signature=d066747e9c5ea1300bbf860835b074e08b6bcfd25a54c3d6b74b0cd66296ee15&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U3LMF62%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdwy%2FqU%2B%2Bkjnc8qF6L3YK2tkvWnVtEWcZ7nrWR63VcIwIhAKuihHSazTKzQ8Rx1v%2BVmWAY%2Bk%2FNw0NM1nxZg3hlkNhwKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxEt0YsntSIft5%2F8xEq3ANzvggqwLNGRQM%2BOvP5bBeAjmh4lTDkL8MyRQxi%2BcZVNOkMYmh1qb27wivkOQ6osG3q5fSnPO8oOe060TKfC04VrrnyVQG4lV%2F0Xhay9NK%2FWUX0aAiv4OEoMyZfdBZsoSLV5xvla4JLVez20KyFSxGqn2WVmXzFKKzOonmkTFROGpnGNSbTHV0laQLyLxzxIpWnKqpxYUO6qDGk%2BVpA8ryIadwTdRwaoZTRhx2Lp7fv3mVuSNpNM1Y81WJZRecRT6B5tyZ5r0M8jFk8A9m71fSCFBEx1vPm7%2B5SZLximqdOWooLTRYIDw%2BpUyqp1HyyTpziwSBeOTYweg5q5VNoKnUI%2FOeUIHqy8KALWLHc5V9pDBfS190PsueokRMO5xaAfp8pl4X%2FLQhc%2Fn9%2B%2BsChBSkaVy5vQPrMQScvV97w5WJiEaRpncaN2Zs9ua4Zg5om8bbtdMD2l9w7PxW4vVFzKsErQe1cUkS%2FZ2jqe6WDZuG5qMHmbB0%2Bsc89U5f7Yo75CuZHhinx397cMsebpuUjJ5RUTLIEAaffHoPjmYU%2Bfiv26uY29742G0gnrWzVWpbXydazICAVnkBii50IP0lJVp%2Bk5ihBFSKjYbsexYgeC%2BcgPB8hhKKJ5Hu38mdCNDDPv4C9BjqkAaur4V9u8PFDGBTNFrvLsLaC%2BiS%2FA9XUJrUv4ipj9B0a%2B4mKTo5i%2B%2BKobmXnbGA4esEKG11giM8F6ncW54Wud4Z6PtRUrxMsiOSulhfD6PcorzK02yyRiqyyj1eeTc4Zh63bfu1lOVgilMpXjmgiI1HasCniQjQQxoBig6n3WSGQcPvOj84fZlpsRkOdywckbGmVW5CaFrwyG2KczOktVsQe8wDp&X-Amz-Signature=5dc9fa3654a8965a5bbd82399d472c14f8f9dc05fbee69ee22b808b7d4e954b5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U3LMF62%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdwy%2FqU%2B%2Bkjnc8qF6L3YK2tkvWnVtEWcZ7nrWR63VcIwIhAKuihHSazTKzQ8Rx1v%2BVmWAY%2Bk%2FNw0NM1nxZg3hlkNhwKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxEt0YsntSIft5%2F8xEq3ANzvggqwLNGRQM%2BOvP5bBeAjmh4lTDkL8MyRQxi%2BcZVNOkMYmh1qb27wivkOQ6osG3q5fSnPO8oOe060TKfC04VrrnyVQG4lV%2F0Xhay9NK%2FWUX0aAiv4OEoMyZfdBZsoSLV5xvla4JLVez20KyFSxGqn2WVmXzFKKzOonmkTFROGpnGNSbTHV0laQLyLxzxIpWnKqpxYUO6qDGk%2BVpA8ryIadwTdRwaoZTRhx2Lp7fv3mVuSNpNM1Y81WJZRecRT6B5tyZ5r0M8jFk8A9m71fSCFBEx1vPm7%2B5SZLximqdOWooLTRYIDw%2BpUyqp1HyyTpziwSBeOTYweg5q5VNoKnUI%2FOeUIHqy8KALWLHc5V9pDBfS190PsueokRMO5xaAfp8pl4X%2FLQhc%2Fn9%2B%2BsChBSkaVy5vQPrMQScvV97w5WJiEaRpncaN2Zs9ua4Zg5om8bbtdMD2l9w7PxW4vVFzKsErQe1cUkS%2FZ2jqe6WDZuG5qMHmbB0%2Bsc89U5f7Yo75CuZHhinx397cMsebpuUjJ5RUTLIEAaffHoPjmYU%2Bfiv26uY29742G0gnrWzVWpbXydazICAVnkBii50IP0lJVp%2Bk5ihBFSKjYbsexYgeC%2BcgPB8hhKKJ5Hu38mdCNDDPv4C9BjqkAaur4V9u8PFDGBTNFrvLsLaC%2BiS%2FA9XUJrUv4ipj9B0a%2B4mKTo5i%2B%2BKobmXnbGA4esEKG11giM8F6ncW54Wud4Z6PtRUrxMsiOSulhfD6PcorzK02yyRiqyyj1eeTc4Zh63bfu1lOVgilMpXjmgiI1HasCniQjQQxoBig6n3WSGQcPvOj84fZlpsRkOdywckbGmVW5CaFrwyG2KczOktVsQe8wDp&X-Amz-Signature=ccdb6a4165c1adc62e787ba154cd04ed8e19e9456bfba922458106bd7519842d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP2B5WFQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNEIS7E00PrncZGYcEBrVMpfDad6zI9JyYm3GbReE%2FsAIhALZ0xjT68PaySBPkTCQ9bv1FrvebagQrLVANElrhfmv9KogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRePOpMULEOUoo%2FcEq3ANjz77%2Bv5BP02%2BdRL%2BJ9gmmRdVkyHz6%2F42E7M0iAFpz0adAQA%2B0H6SxJkq6x6rX7JTi26GfE5hTW%2B4LBSUdcYK0%2FjEriq96SWCPnjkAaivBrErmzfc67y3cUb4X1mIg4QUVIP7Y7h1E%2Bn0%2BElVyx%2Fbj%2FD%2F17u5t1hkJ%2BcKyZFrcuxX3hTHOkbPyWF87RcMGTYTqezMUtZV%2FX9l3XOTt8ddPOAJQ6%2BKaGfyVlq%2BKC%2B1zmGgATeCQXzVJb8x1Q2tNda5wirGwQXF5IJSXviLqL5lhozAGPNzcziRKXmKLNSOguMsQXO54M9D12XJIdrFlzmCS%2F42DGnpxIBSne4WIUICCyZ%2BGXyjleGLfz5ZsgdskpXYsqAaQBOAu%2F9Sv5QFObTkbtuwLp4RaP1G2efGM0KtCLkjJCUzwVYQiKUmt3ZDOjnV2N%2BHMAdrS0L1sHOJCo%2BY7sZM8AXmofseVjJeTDWgwdfmon4U3VEmlJxkO7u5bX7SMNl7Hu0rbHZiIIlym1pbroVgrwg0OGzazlWPji%2BnZlNaLWnmSkjFL3o%2Fq3fiytE2HpSCVCg6dfJmdSba8CI0eK0p9mKdADQWjp8Iv%2B%2BGPRNIcrzZ1q0a19riC4hoRx2Cb2%2FHo7hiAP8uCKjDBv4C9BjqkAbdadMNrLx4T%2Bhb%2ByTQ7LF9NlaUYSrUBmkOXI6iIAU%2BCUf76WrEIcJCtmpZ1GpTRaKpIWYbqwIRFQdGXZC1Nc2KAUUzvS7hnqmgdiKNu3RIN49iAwenNemQkC1Uvjd%2FnblI23%2FfCG2Q4%2BYnnvDjlHOjXyUABgiajXApFml0fWvw8NwDCZyi3BlU0DjpAxWgxoa1djMIIaoCr4qMfPx9KgZCt4%2B7d&X-Amz-Signature=3657f899af220ba0032505773b704958449421c9996c7d24d200b0635757d658&X-Amz-SignedHeaders=host&x-id=GetObject)
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