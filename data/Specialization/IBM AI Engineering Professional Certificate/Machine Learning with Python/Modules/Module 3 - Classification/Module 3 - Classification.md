

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFOOOMHC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWWE9KsP%2FS%2FYIkNBn5EViW4HzWUVA4E1HRmosgwulHSgIhAL2n9GXU8Xzzpni9r0IVMe9GiSpdodnuGx09%2Bj5SVyxzKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwy5Vv1FfzYEruF%2B70q3AOPDD3nkP0qxhZAbsi0r8uDBLoeEV9JJeOeDusXe%2B1kyxnDhhv7hT%2B%2FXhFFnBCCN4XBPxSpxkFUoDdOQ5%2BdRGjVxwZOl5ti%2B2z1agP6gvifmpmhEkrwLbZBeotSuzuFVbRDgaS61koA183TgEvu8PKymWZVXWoO4O0VfDXKLezXdTSz1vPeunsn%2FSe%2F4%2Baan9zSxcGrgjafmDDHcfmi1nhE8i%2B34jJVevAh3RP8Iyyrq4XQ6lTGWZxJxaN%2FKXE2UXxjHmlpI1TVrDIHAzPjKW235gf%2Fb4S9mFvv1pVJjGcVuZFVae%2B1MDdnK3ZMxzEwpMCtLE32WheRweKKowC6Rlb6IsRLyy3dY7AoFza3EbRrjoeZFzUALwrhMnv5FTY556qcLLM8J34W0kzsPmhBPT5Wy69vX7JPFrJ6GvqpZNhzysF%2F9vPV8yhlMNn6SpzCdzMdlsOkLNrTkY7J3hcw3%2F%2FkfTTwPZFUBpBTTu8%2FesAFN6iIs1C5Q9qp%2ByBD70UoRmL1amJ65x6HgVtOI0gHOaNhYv%2BUsLKymhfvgZb1%2FkmfH0iMsBK6Js%2F6Qo1Ie75CJqltRPCOSFraBxyTcnAhceoVFdlkm244TNlAVePNwtUND0G%2FJJCWRUi7rQIrGjDoqOq8BjqkAVp8nsJ8mO9k9qqk20j%2FfC6%2F%2B6E3PkMTmPkZqB9bYTBZTVu5ZvVA2FfCPrM99MgDqPczvPUh3PH%2BgxOmTjcnpnSoM2mZ3SN5sJ9dGtRabxqSRB%2Fq46gctr2l1oJshM6wnkOnMMxIABwA3C9MEGUavdDddSAWA9GJo3gwWK7eeSUbF%2BafQ8kjF8Lb%2FXE6k6gDzs%2BPO7xWLwk0aecn2shuSfvgT6Ce&X-Amz-Signature=49dc633c4e9526af01a705f575da05cb0dda154aa5579d98c35ea4167c0a5de0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFOOOMHC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWWE9KsP%2FS%2FYIkNBn5EViW4HzWUVA4E1HRmosgwulHSgIhAL2n9GXU8Xzzpni9r0IVMe9GiSpdodnuGx09%2Bj5SVyxzKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwy5Vv1FfzYEruF%2B70q3AOPDD3nkP0qxhZAbsi0r8uDBLoeEV9JJeOeDusXe%2B1kyxnDhhv7hT%2B%2FXhFFnBCCN4XBPxSpxkFUoDdOQ5%2BdRGjVxwZOl5ti%2B2z1agP6gvifmpmhEkrwLbZBeotSuzuFVbRDgaS61koA183TgEvu8PKymWZVXWoO4O0VfDXKLezXdTSz1vPeunsn%2FSe%2F4%2Baan9zSxcGrgjafmDDHcfmi1nhE8i%2B34jJVevAh3RP8Iyyrq4XQ6lTGWZxJxaN%2FKXE2UXxjHmlpI1TVrDIHAzPjKW235gf%2Fb4S9mFvv1pVJjGcVuZFVae%2B1MDdnK3ZMxzEwpMCtLE32WheRweKKowC6Rlb6IsRLyy3dY7AoFza3EbRrjoeZFzUALwrhMnv5FTY556qcLLM8J34W0kzsPmhBPT5Wy69vX7JPFrJ6GvqpZNhzysF%2F9vPV8yhlMNn6SpzCdzMdlsOkLNrTkY7J3hcw3%2F%2FkfTTwPZFUBpBTTu8%2FesAFN6iIs1C5Q9qp%2ByBD70UoRmL1amJ65x6HgVtOI0gHOaNhYv%2BUsLKymhfvgZb1%2FkmfH0iMsBK6Js%2F6Qo1Ie75CJqltRPCOSFraBxyTcnAhceoVFdlkm244TNlAVePNwtUND0G%2FJJCWRUi7rQIrGjDoqOq8BjqkAVp8nsJ8mO9k9qqk20j%2FfC6%2F%2B6E3PkMTmPkZqB9bYTBZTVu5ZvVA2FfCPrM99MgDqPczvPUh3PH%2BgxOmTjcnpnSoM2mZ3SN5sJ9dGtRabxqSRB%2Fq46gctr2l1oJshM6wnkOnMMxIABwA3C9MEGUavdDddSAWA9GJo3gwWK7eeSUbF%2BafQ8kjF8Lb%2FXE6k6gDzs%2BPO7xWLwk0aecn2shuSfvgT6Ce&X-Amz-Signature=3a65ba04b254b473e865488b5e12c9aca513df1bc24cbfa0b1818869c8464cad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFOOOMHC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWWE9KsP%2FS%2FYIkNBn5EViW4HzWUVA4E1HRmosgwulHSgIhAL2n9GXU8Xzzpni9r0IVMe9GiSpdodnuGx09%2Bj5SVyxzKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwy5Vv1FfzYEruF%2B70q3AOPDD3nkP0qxhZAbsi0r8uDBLoeEV9JJeOeDusXe%2B1kyxnDhhv7hT%2B%2FXhFFnBCCN4XBPxSpxkFUoDdOQ5%2BdRGjVxwZOl5ti%2B2z1agP6gvifmpmhEkrwLbZBeotSuzuFVbRDgaS61koA183TgEvu8PKymWZVXWoO4O0VfDXKLezXdTSz1vPeunsn%2FSe%2F4%2Baan9zSxcGrgjafmDDHcfmi1nhE8i%2B34jJVevAh3RP8Iyyrq4XQ6lTGWZxJxaN%2FKXE2UXxjHmlpI1TVrDIHAzPjKW235gf%2Fb4S9mFvv1pVJjGcVuZFVae%2B1MDdnK3ZMxzEwpMCtLE32WheRweKKowC6Rlb6IsRLyy3dY7AoFza3EbRrjoeZFzUALwrhMnv5FTY556qcLLM8J34W0kzsPmhBPT5Wy69vX7JPFrJ6GvqpZNhzysF%2F9vPV8yhlMNn6SpzCdzMdlsOkLNrTkY7J3hcw3%2F%2FkfTTwPZFUBpBTTu8%2FesAFN6iIs1C5Q9qp%2ByBD70UoRmL1amJ65x6HgVtOI0gHOaNhYv%2BUsLKymhfvgZb1%2FkmfH0iMsBK6Js%2F6Qo1Ie75CJqltRPCOSFraBxyTcnAhceoVFdlkm244TNlAVePNwtUND0G%2FJJCWRUi7rQIrGjDoqOq8BjqkAVp8nsJ8mO9k9qqk20j%2FfC6%2F%2B6E3PkMTmPkZqB9bYTBZTVu5ZvVA2FfCPrM99MgDqPczvPUh3PH%2BgxOmTjcnpnSoM2mZ3SN5sJ9dGtRabxqSRB%2Fq46gctr2l1oJshM6wnkOnMMxIABwA3C9MEGUavdDddSAWA9GJo3gwWK7eeSUbF%2BafQ8kjF8Lb%2FXE6k6gDzs%2BPO7xWLwk0aecn2shuSfvgT6Ce&X-Amz-Signature=b349a627246fc2d886b17dab692a73a08f013fe8dc8bc6b56c52c5c0fe10b7c4&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYNMQBMA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA1g4ALY48WMvQ%2BIkSmv32grY5K0wo41M2IXRNoR6gJ%2BAiEAtr2ILVxnP%2FiOuTSJj3APjIkBvVS%2B1HJYGEr%2FG5A3kUgqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLB%2BhSDtoF5Tlllu4SrcA1%2FogQ1gsstQvPGMMk3kZXqS5Pimj2t5Ks9hIV79axKYteHvl%2B338YGNB1YBecJBJNZ2s%2FiXKLSVkxVuKJhfZFteYFsIO9wz6ItpyfU23NpQGb3dm5%2FgITvABT2yOMRordxPEHWaxsSlelP0XEqq4lN76JXE5r676cZsbmQIkN8M7TBKHmjcPSxh2C37QOUtXLN%2BEMIchuaEIZvHEFAocTX0AMePJuqsNYqTybH8n0N%2Fx3IKgA3saImdPPsgu4POMJAlaXhNg1j2ztLnmrsPVoWX6tInVaT3R2p92nsryV4VzK4l0rSpQDau1G3M0HZAKquY69Z5wTkJQOUzDajLFrxA7r7P8EEHrdSybSRtfTdxgkfT%2B2onhlXshrcARVbNJfxMWPA%2FJA%2FDsX%2FYIQj2zGPgX%2Fzh9Fh5sZkD0HcaOfb9VwkJaOSXR7wMku8WXFQ8yEnE7EhCZLqMFBUjy4Ouv6A2hm7z6Xb7VmS5kbyVyBoyKJMbN9eCwXQoqu9xMvbWfSAnjKGtl3ZYoYsAGxUS563ZDDkRCPRYmOBLg2kCk09ZI6fJ75LtyW5BtKd0OtQIJ07pG6cGy4DfhahY8qxbQlem9p7lcZT7IZhUi5HJkanWmgGXIQG4eDaq9MmAMP6o6rwGOqUBOL5uknaaZsy54ggjoZuR1TpHU1Y%2FNCVzvm%2B0ZAM%2FwLbRPIMmnLpsIEWdEl8ZjQaE5R804q%2BcIOf%2F%2FuUbTQPPuWHnVE0f8zaHx68hMJslHkQuuDR2C%2BCE7HQEw1xyeHhVRG2F4%2FFH4fmz9Q0YE8BOi5VhANQyIw0taV%2BcIE93qJI8NNm7UFBuv3VewZ6mfZoVsmhcGDsGXg6Akr4CyXNeu%2BZnuAyy&X-Amz-Signature=49bc234f7c150bb8a14147a911263ee299c6c27feecb20ed4721ddbc3741ca8e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYNMQBMA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA1g4ALY48WMvQ%2BIkSmv32grY5K0wo41M2IXRNoR6gJ%2BAiEAtr2ILVxnP%2FiOuTSJj3APjIkBvVS%2B1HJYGEr%2FG5A3kUgqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLB%2BhSDtoF5Tlllu4SrcA1%2FogQ1gsstQvPGMMk3kZXqS5Pimj2t5Ks9hIV79axKYteHvl%2B338YGNB1YBecJBJNZ2s%2FiXKLSVkxVuKJhfZFteYFsIO9wz6ItpyfU23NpQGb3dm5%2FgITvABT2yOMRordxPEHWaxsSlelP0XEqq4lN76JXE5r676cZsbmQIkN8M7TBKHmjcPSxh2C37QOUtXLN%2BEMIchuaEIZvHEFAocTX0AMePJuqsNYqTybH8n0N%2Fx3IKgA3saImdPPsgu4POMJAlaXhNg1j2ztLnmrsPVoWX6tInVaT3R2p92nsryV4VzK4l0rSpQDau1G3M0HZAKquY69Z5wTkJQOUzDajLFrxA7r7P8EEHrdSybSRtfTdxgkfT%2B2onhlXshrcARVbNJfxMWPA%2FJA%2FDsX%2FYIQj2zGPgX%2Fzh9Fh5sZkD0HcaOfb9VwkJaOSXR7wMku8WXFQ8yEnE7EhCZLqMFBUjy4Ouv6A2hm7z6Xb7VmS5kbyVyBoyKJMbN9eCwXQoqu9xMvbWfSAnjKGtl3ZYoYsAGxUS563ZDDkRCPRYmOBLg2kCk09ZI6fJ75LtyW5BtKd0OtQIJ07pG6cGy4DfhahY8qxbQlem9p7lcZT7IZhUi5HJkanWmgGXIQG4eDaq9MmAMP6o6rwGOqUBOL5uknaaZsy54ggjoZuR1TpHU1Y%2FNCVzvm%2B0ZAM%2FwLbRPIMmnLpsIEWdEl8ZjQaE5R804q%2BcIOf%2F%2FuUbTQPPuWHnVE0f8zaHx68hMJslHkQuuDR2C%2BCE7HQEw1xyeHhVRG2F4%2FFH4fmz9Q0YE8BOi5VhANQyIw0taV%2BcIE93qJI8NNm7UFBuv3VewZ6mfZoVsmhcGDsGXg6Akr4CyXNeu%2BZnuAyy&X-Amz-Signature=e85878b76e523fe72bf44148039d78bfbc8d20f7d982041730d651bb81eacdd9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFOOOMHC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWWE9KsP%2FS%2FYIkNBn5EViW4HzWUVA4E1HRmosgwulHSgIhAL2n9GXU8Xzzpni9r0IVMe9GiSpdodnuGx09%2Bj5SVyxzKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwy5Vv1FfzYEruF%2B70q3AOPDD3nkP0qxhZAbsi0r8uDBLoeEV9JJeOeDusXe%2B1kyxnDhhv7hT%2B%2FXhFFnBCCN4XBPxSpxkFUoDdOQ5%2BdRGjVxwZOl5ti%2B2z1agP6gvifmpmhEkrwLbZBeotSuzuFVbRDgaS61koA183TgEvu8PKymWZVXWoO4O0VfDXKLezXdTSz1vPeunsn%2FSe%2F4%2Baan9zSxcGrgjafmDDHcfmi1nhE8i%2B34jJVevAh3RP8Iyyrq4XQ6lTGWZxJxaN%2FKXE2UXxjHmlpI1TVrDIHAzPjKW235gf%2Fb4S9mFvv1pVJjGcVuZFVae%2B1MDdnK3ZMxzEwpMCtLE32WheRweKKowC6Rlb6IsRLyy3dY7AoFza3EbRrjoeZFzUALwrhMnv5FTY556qcLLM8J34W0kzsPmhBPT5Wy69vX7JPFrJ6GvqpZNhzysF%2F9vPV8yhlMNn6SpzCdzMdlsOkLNrTkY7J3hcw3%2F%2FkfTTwPZFUBpBTTu8%2FesAFN6iIs1C5Q9qp%2ByBD70UoRmL1amJ65x6HgVtOI0gHOaNhYv%2BUsLKymhfvgZb1%2FkmfH0iMsBK6Js%2F6Qo1Ie75CJqltRPCOSFraBxyTcnAhceoVFdlkm244TNlAVePNwtUND0G%2FJJCWRUi7rQIrGjDoqOq8BjqkAVp8nsJ8mO9k9qqk20j%2FfC6%2F%2B6E3PkMTmPkZqB9bYTBZTVu5ZvVA2FfCPrM99MgDqPczvPUh3PH%2BgxOmTjcnpnSoM2mZ3SN5sJ9dGtRabxqSRB%2Fq46gctr2l1oJshM6wnkOnMMxIABwA3C9MEGUavdDddSAWA9GJo3gwWK7eeSUbF%2BafQ8kjF8Lb%2FXE6k6gDzs%2BPO7xWLwk0aecn2shuSfvgT6Ce&X-Amz-Signature=59820ec31875b952a42e7d104190319bdc917554372f85143fe50d7adf521938&X-Amz-SignedHeaders=host&x-id=GetObject)
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