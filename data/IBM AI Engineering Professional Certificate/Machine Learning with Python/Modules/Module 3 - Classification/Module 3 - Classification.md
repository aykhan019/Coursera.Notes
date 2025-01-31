

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPDOSI3R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjgRrBkSNX1erMNlCWBWprkg2VZ0gGfyNvj6FKjtwpgAiEAldk4S1wG7y3hE8WKRdt1k5zLlQW3RTOtDMAs%2BOs3R9cqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBHAisCMNYwOuYVDaSrcA%2Bp389mmpOsn1eQN6uMhhY43AYUZt6p8MGupgusTIb2F0Quc%2Bwvzh5%2BrVvH14uCbjXn%2B3TP4qvK7KW4GmcsJUK237D%2FfA%2FEmSZBCeGhCoblpvEoaSRi0KLOgnYNapyPkrrv85UWHbXbsXHKsKgBCJnSyMGzTSjvXqvf%2BX%2BC8dA%2Blb2Q2uuVb%2Bzjthge8IUGYVnY4e40Llco8ikvjK0Rdme4KviQCZDuVCd%2BV%2B%2FYRyJuVWCk6Te5x66RUW2GruB64u%2FtO6SC4FpTFlUYE6iufZKo2E8LeIjZh9hE%2F4UpXKjvqrS7c%2FRlawUUax7gMPPBnM1NaFgAZE7bqHJSl23McxbZz67AKESAmqx3eayv5Dn7vabe4fWqqWb6fFrPRItobtuJFOLCsoliPQvd%2FL%2F0laIEXyxG0grSaclKvjsWsav5M7WEIkII9eKT5ddYybg6BqmX1hpDR8ool6pqxSDrqYNCra2p%2FVHII%2Bkm%2BiNJxGNkUy%2B9OofeS%2FznXc26I7BcnQIMH9shdjpWGZCqqTg%2FCujXKLfoOIxs22Yjxkx2lSTk2qtC4jDL0PMUFjRzhHeDxGcXqhMUQatvKQoueOoaBcXUOyNXriBh%2BJukejMUhLHTvVbFNZD8XXtMVVLYxMNiU9bwGOqUByO67wqHc2TUhCd4OXBjHmM%2FWd89IuUnMmHZvxNKAzfVpCCbZdLpxa%2FBr2vp4czdSivawp3egJp9k10DsH6jXQPqMr3TTJUAvTYlGcCFWchVI6O6XwKHZ1s7v57Kmuld4i5m0tNN5owKfpU%2BTrzs%2BDpPmPNwmqrgyRxbrO8fziwxxbiYbPsdd%2BMZ4YJfb7ingcVKbY4bOpkU2Pyue2834zxaLBeZn&X-Amz-Signature=7930f67440502eb05338f2a2824952ba7547a5ddd1dca086d97d54dfe4d2d5d0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPDOSI3R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjgRrBkSNX1erMNlCWBWprkg2VZ0gGfyNvj6FKjtwpgAiEAldk4S1wG7y3hE8WKRdt1k5zLlQW3RTOtDMAs%2BOs3R9cqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBHAisCMNYwOuYVDaSrcA%2Bp389mmpOsn1eQN6uMhhY43AYUZt6p8MGupgusTIb2F0Quc%2Bwvzh5%2BrVvH14uCbjXn%2B3TP4qvK7KW4GmcsJUK237D%2FfA%2FEmSZBCeGhCoblpvEoaSRi0KLOgnYNapyPkrrv85UWHbXbsXHKsKgBCJnSyMGzTSjvXqvf%2BX%2BC8dA%2Blb2Q2uuVb%2Bzjthge8IUGYVnY4e40Llco8ikvjK0Rdme4KviQCZDuVCd%2BV%2B%2FYRyJuVWCk6Te5x66RUW2GruB64u%2FtO6SC4FpTFlUYE6iufZKo2E8LeIjZh9hE%2F4UpXKjvqrS7c%2FRlawUUax7gMPPBnM1NaFgAZE7bqHJSl23McxbZz67AKESAmqx3eayv5Dn7vabe4fWqqWb6fFrPRItobtuJFOLCsoliPQvd%2FL%2F0laIEXyxG0grSaclKvjsWsav5M7WEIkII9eKT5ddYybg6BqmX1hpDR8ool6pqxSDrqYNCra2p%2FVHII%2Bkm%2BiNJxGNkUy%2B9OofeS%2FznXc26I7BcnQIMH9shdjpWGZCqqTg%2FCujXKLfoOIxs22Yjxkx2lSTk2qtC4jDL0PMUFjRzhHeDxGcXqhMUQatvKQoueOoaBcXUOyNXriBh%2BJukejMUhLHTvVbFNZD8XXtMVVLYxMNiU9bwGOqUByO67wqHc2TUhCd4OXBjHmM%2FWd89IuUnMmHZvxNKAzfVpCCbZdLpxa%2FBr2vp4czdSivawp3egJp9k10DsH6jXQPqMr3TTJUAvTYlGcCFWchVI6O6XwKHZ1s7v57Kmuld4i5m0tNN5owKfpU%2BTrzs%2BDpPmPNwmqrgyRxbrO8fziwxxbiYbPsdd%2BMZ4YJfb7ingcVKbY4bOpkU2Pyue2834zxaLBeZn&X-Amz-Signature=42b506f3feac0959e31112f87dafffe641bda2df084aed82598a1465184c4182&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPDOSI3R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjgRrBkSNX1erMNlCWBWprkg2VZ0gGfyNvj6FKjtwpgAiEAldk4S1wG7y3hE8WKRdt1k5zLlQW3RTOtDMAs%2BOs3R9cqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBHAisCMNYwOuYVDaSrcA%2Bp389mmpOsn1eQN6uMhhY43AYUZt6p8MGupgusTIb2F0Quc%2Bwvzh5%2BrVvH14uCbjXn%2B3TP4qvK7KW4GmcsJUK237D%2FfA%2FEmSZBCeGhCoblpvEoaSRi0KLOgnYNapyPkrrv85UWHbXbsXHKsKgBCJnSyMGzTSjvXqvf%2BX%2BC8dA%2Blb2Q2uuVb%2Bzjthge8IUGYVnY4e40Llco8ikvjK0Rdme4KviQCZDuVCd%2BV%2B%2FYRyJuVWCk6Te5x66RUW2GruB64u%2FtO6SC4FpTFlUYE6iufZKo2E8LeIjZh9hE%2F4UpXKjvqrS7c%2FRlawUUax7gMPPBnM1NaFgAZE7bqHJSl23McxbZz67AKESAmqx3eayv5Dn7vabe4fWqqWb6fFrPRItobtuJFOLCsoliPQvd%2FL%2F0laIEXyxG0grSaclKvjsWsav5M7WEIkII9eKT5ddYybg6BqmX1hpDR8ool6pqxSDrqYNCra2p%2FVHII%2Bkm%2BiNJxGNkUy%2B9OofeS%2FznXc26I7BcnQIMH9shdjpWGZCqqTg%2FCujXKLfoOIxs22Yjxkx2lSTk2qtC4jDL0PMUFjRzhHeDxGcXqhMUQatvKQoueOoaBcXUOyNXriBh%2BJukejMUhLHTvVbFNZD8XXtMVVLYxMNiU9bwGOqUByO67wqHc2TUhCd4OXBjHmM%2FWd89IuUnMmHZvxNKAzfVpCCbZdLpxa%2FBr2vp4czdSivawp3egJp9k10DsH6jXQPqMr3TTJUAvTYlGcCFWchVI6O6XwKHZ1s7v57Kmuld4i5m0tNN5owKfpU%2BTrzs%2BDpPmPNwmqrgyRxbrO8fziwxxbiYbPsdd%2BMZ4YJfb7ingcVKbY4bOpkU2Pyue2834zxaLBeZn&X-Amz-Signature=78958694ccf594b3aacd2d450b56ddb5fc89a07f752bcc3ff00c8fb9e9d0e668&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB6M27PD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOFazE5w9i6fsWEh9iFLFeo2i%2F7YD5vk2TJ23UIFCNoQIgVrOlXN2PpRzSn2Cepijfc5vDboLK33IU97kf5HSPCooqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDETfdZzfxck%2B0LJ4qSrcA4UdZVhs4rC5iMpzdCsrUvzJAlfHfKw9n6sMDqV68mrvDzYXtJnVIzWcmH2EvSwKtIMAw%2B6bO7KuOWXubcrQ46hz1pUzgBm5aVHIyIlSWKC3Vu5xXX0CMLiHdjbPqBhNK8TlW3%2FTQ45e%2F0n0HRSs%2BRJq0LX8O5to9T74n2MCwU7r6KLoqTdK1QN9eb12DoyVYoSPZe1snv%2B26cXqr6ysNH%2BvVGO0347tt3bArRrF%2Fv3aOx1j5LNoRwXc91nFTH4ONrJymrWhXVODj87CkBB6%2FEXDt2vMkTycqsERqvF8gvWRdUJ6%2Bs8yCCd7uHCTjdUyh1JL4rBgllCYLgqUGEOhIQVDA10uUhyGmTB9mm1xnPmjPSajP7vFvdMgNj6lI0pJLJ8bK03y6nz4GFNAVQrOB72zppmV4lKtMZGS5eBt7BIlgWW5%2BE4g5TNT8etQb7eZmf%2BpDsvGKrIWKOgZxz5xrSJOHa%2BPX1CdHj47%2BcClQH4fWJE0b51ZjtXsO6Nw8uHNS0AX53A6Dq8oqI9C2B3WYv8IhRLbJ52%2Fj3xtGupLoKDNUuTacN0pFJ74%2FKtFZiqLtOS2mh2RdQHgfUvWmFVTWfn4o9PItVxMhfoOuwUT3UdSsBTh7DoD8j4Rk1jAMN2T9bwGOqUBEtHSGsfmiUrJlRnnZ6M5y3JsodZY1VUD87HVgWeiowZG6zKCt64aK6Mr50aNkfw9FQlLTZB7JVLilLPSKj09a7NRqAJgP55vBEfWxJYKlnAbmbdJydBK%2B2ccIXh5Ivr43LmmUhlcuWvh%2BGvFUeD2nNPMJpgRFQ4LYojvtpo3K5ohUOMlFI0SdeA2kl5O2%2B5gbmBGjWfr%2BLvydWG4lFHi5rq6Rhy5&X-Amz-Signature=06684af8d1fdc19f6c4e92ee508c40931a0b30d3913a5e715cd51d312a6e4f73&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB6M27PD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOFazE5w9i6fsWEh9iFLFeo2i%2F7YD5vk2TJ23UIFCNoQIgVrOlXN2PpRzSn2Cepijfc5vDboLK33IU97kf5HSPCooqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDETfdZzfxck%2B0LJ4qSrcA4UdZVhs4rC5iMpzdCsrUvzJAlfHfKw9n6sMDqV68mrvDzYXtJnVIzWcmH2EvSwKtIMAw%2B6bO7KuOWXubcrQ46hz1pUzgBm5aVHIyIlSWKC3Vu5xXX0CMLiHdjbPqBhNK8TlW3%2FTQ45e%2F0n0HRSs%2BRJq0LX8O5to9T74n2MCwU7r6KLoqTdK1QN9eb12DoyVYoSPZe1snv%2B26cXqr6ysNH%2BvVGO0347tt3bArRrF%2Fv3aOx1j5LNoRwXc91nFTH4ONrJymrWhXVODj87CkBB6%2FEXDt2vMkTycqsERqvF8gvWRdUJ6%2Bs8yCCd7uHCTjdUyh1JL4rBgllCYLgqUGEOhIQVDA10uUhyGmTB9mm1xnPmjPSajP7vFvdMgNj6lI0pJLJ8bK03y6nz4GFNAVQrOB72zppmV4lKtMZGS5eBt7BIlgWW5%2BE4g5TNT8etQb7eZmf%2BpDsvGKrIWKOgZxz5xrSJOHa%2BPX1CdHj47%2BcClQH4fWJE0b51ZjtXsO6Nw8uHNS0AX53A6Dq8oqI9C2B3WYv8IhRLbJ52%2Fj3xtGupLoKDNUuTacN0pFJ74%2FKtFZiqLtOS2mh2RdQHgfUvWmFVTWfn4o9PItVxMhfoOuwUT3UdSsBTh7DoD8j4Rk1jAMN2T9bwGOqUBEtHSGsfmiUrJlRnnZ6M5y3JsodZY1VUD87HVgWeiowZG6zKCt64aK6Mr50aNkfw9FQlLTZB7JVLilLPSKj09a7NRqAJgP55vBEfWxJYKlnAbmbdJydBK%2B2ccIXh5Ivr43LmmUhlcuWvh%2BGvFUeD2nNPMJpgRFQ4LYojvtpo3K5ohUOMlFI0SdeA2kl5O2%2B5gbmBGjWfr%2BLvydWG4lFHi5rq6Rhy5&X-Amz-Signature=61c4a924b08946e26d5f9d93a972c379faccee3ba5fa3d943ac78186a1e0d173&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPDOSI3R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjgRrBkSNX1erMNlCWBWprkg2VZ0gGfyNvj6FKjtwpgAiEAldk4S1wG7y3hE8WKRdt1k5zLlQW3RTOtDMAs%2BOs3R9cqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBHAisCMNYwOuYVDaSrcA%2Bp389mmpOsn1eQN6uMhhY43AYUZt6p8MGupgusTIb2F0Quc%2Bwvzh5%2BrVvH14uCbjXn%2B3TP4qvK7KW4GmcsJUK237D%2FfA%2FEmSZBCeGhCoblpvEoaSRi0KLOgnYNapyPkrrv85UWHbXbsXHKsKgBCJnSyMGzTSjvXqvf%2BX%2BC8dA%2Blb2Q2uuVb%2Bzjthge8IUGYVnY4e40Llco8ikvjK0Rdme4KviQCZDuVCd%2BV%2B%2FYRyJuVWCk6Te5x66RUW2GruB64u%2FtO6SC4FpTFlUYE6iufZKo2E8LeIjZh9hE%2F4UpXKjvqrS7c%2FRlawUUax7gMPPBnM1NaFgAZE7bqHJSl23McxbZz67AKESAmqx3eayv5Dn7vabe4fWqqWb6fFrPRItobtuJFOLCsoliPQvd%2FL%2F0laIEXyxG0grSaclKvjsWsav5M7WEIkII9eKT5ddYybg6BqmX1hpDR8ool6pqxSDrqYNCra2p%2FVHII%2Bkm%2BiNJxGNkUy%2B9OofeS%2FznXc26I7BcnQIMH9shdjpWGZCqqTg%2FCujXKLfoOIxs22Yjxkx2lSTk2qtC4jDL0PMUFjRzhHeDxGcXqhMUQatvKQoueOoaBcXUOyNXriBh%2BJukejMUhLHTvVbFNZD8XXtMVVLYxMNiU9bwGOqUByO67wqHc2TUhCd4OXBjHmM%2FWd89IuUnMmHZvxNKAzfVpCCbZdLpxa%2FBr2vp4czdSivawp3egJp9k10DsH6jXQPqMr3TTJUAvTYlGcCFWchVI6O6XwKHZ1s7v57Kmuld4i5m0tNN5owKfpU%2BTrzs%2BDpPmPNwmqrgyRxbrO8fziwxxbiYbPsdd%2BMZ4YJfb7ingcVKbY4bOpkU2Pyue2834zxaLBeZn&X-Amz-Signature=43aefc3770be6051b9ab60c252220921bf8946febdd9784ab80fd00a6c8ae11e&X-Amz-SignedHeaders=host&x-id=GetObject)
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