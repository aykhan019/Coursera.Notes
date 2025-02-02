

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU7HL2JN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACyl2tmylS8d8tmGjbi4788CLDuSp0FB%2B390DMq3%2BMwAiA%2Bia0U7iWyPGFwdoEWICTCLitK1SqIXe2xT354Rc3ziyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWJtSFKf8wTSCAi%2BKtwD8cBG4fSJcxJFtAq1NfF6qQZ8%2FiUtq3%2FIHRi81sds%2B5rXW88YtJofhA2cKoZb%2F7hGexVFIlaS%2FOx97fPT%2BFn8nMXktj%2Ba%2BrHxnPvOmRLDXv9yQsSOZjyhka7l43%2FEK5nD%2FQrf%2BtEN5Sc6oCdHWhEaPNUMYEEwDXsnOWNiif%2BDRetLZSE4Xql0pL2ko0W%2BbHr1A%2BZ9BG293c4zWgmDBvgnIehKbQ4i8D7masA9IGU0ihsvrYaXt%2BjveYSCXsVCsz8wjWrnRAAJLUZjyGB4dVo58t7U6mYrxZb6NlHJHhBqjFUlQ0F2tXj%2BVFY0NLrXmckmF71no5DUlh1SPgKa%2BVrMohKC4gCwaTBs8jzl2Z8jl2v13dq%2Bzd%2FijrriUUY5MwMJeO8JpBgHuGz1k8FzFHmiVAciTeMFEOXsiqFHwpN4GcE52h%2BqZ2Ej0h5KkL%2Ff%2BE9%2BKbnFCq3gd4I8zVbQunUuTHyEbK0WDE3KaKxTzL7Ihehw%2F%2BQIjCurDgE3gyUD%2F%2BBuVPi4%2F2llPSnM2OncbBTzerLtyhjxCl4eMgvbOHsLCAct%2BZ529JTs5cF%2B68Oebeo5d%2B%2B45%2BNXE3nOjYqpHm7LtL0QwjU0b2PppjULxZox%2BlpPNpz%2FXTwUxBRP2WEwn%2BT%2BvAY6pgHZUT%2F6AnDEL0Oo3b%2FGpw5AiJTCarN69pPxBkctFIBsKcNUpUZ5VmNqXvUjfzuyEXZnR1GzRrp4qmo%2BLwOAt7GR5A0ZrJtn65kl0uiubhg4g51UXwMK9xKS08Q6v0dFBXSrsuyAh0wXxuXZ8ifb1W7Hx5f4STb07a3gCOMJ4kTfeLGWbq%2F0XVSMxxs7b3ZE2g0EMKrBZe337vtbqarpFKwkDoBzqQVO&X-Amz-Signature=1c05f7bba82dba9cc7b21d00a1c8f2d1337225896d9f0c3693b29c20d53431ca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU7HL2JN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACyl2tmylS8d8tmGjbi4788CLDuSp0FB%2B390DMq3%2BMwAiA%2Bia0U7iWyPGFwdoEWICTCLitK1SqIXe2xT354Rc3ziyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWJtSFKf8wTSCAi%2BKtwD8cBG4fSJcxJFtAq1NfF6qQZ8%2FiUtq3%2FIHRi81sds%2B5rXW88YtJofhA2cKoZb%2F7hGexVFIlaS%2FOx97fPT%2BFn8nMXktj%2Ba%2BrHxnPvOmRLDXv9yQsSOZjyhka7l43%2FEK5nD%2FQrf%2BtEN5Sc6oCdHWhEaPNUMYEEwDXsnOWNiif%2BDRetLZSE4Xql0pL2ko0W%2BbHr1A%2BZ9BG293c4zWgmDBvgnIehKbQ4i8D7masA9IGU0ihsvrYaXt%2BjveYSCXsVCsz8wjWrnRAAJLUZjyGB4dVo58t7U6mYrxZb6NlHJHhBqjFUlQ0F2tXj%2BVFY0NLrXmckmF71no5DUlh1SPgKa%2BVrMohKC4gCwaTBs8jzl2Z8jl2v13dq%2Bzd%2FijrriUUY5MwMJeO8JpBgHuGz1k8FzFHmiVAciTeMFEOXsiqFHwpN4GcE52h%2BqZ2Ej0h5KkL%2Ff%2BE9%2BKbnFCq3gd4I8zVbQunUuTHyEbK0WDE3KaKxTzL7Ihehw%2F%2BQIjCurDgE3gyUD%2F%2BBuVPi4%2F2llPSnM2OncbBTzerLtyhjxCl4eMgvbOHsLCAct%2BZ529JTs5cF%2B68Oebeo5d%2B%2B45%2BNXE3nOjYqpHm7LtL0QwjU0b2PppjULxZox%2BlpPNpz%2FXTwUxBRP2WEwn%2BT%2BvAY6pgHZUT%2F6AnDEL0Oo3b%2FGpw5AiJTCarN69pPxBkctFIBsKcNUpUZ5VmNqXvUjfzuyEXZnR1GzRrp4qmo%2BLwOAt7GR5A0ZrJtn65kl0uiubhg4g51UXwMK9xKS08Q6v0dFBXSrsuyAh0wXxuXZ8ifb1W7Hx5f4STb07a3gCOMJ4kTfeLGWbq%2F0XVSMxxs7b3ZE2g0EMKrBZe337vtbqarpFKwkDoBzqQVO&X-Amz-Signature=6b6e30c99c95a0375b68fb41f1807b3f10683ef7112ac5cde8eedfccbd39d75b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU7HL2JN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACyl2tmylS8d8tmGjbi4788CLDuSp0FB%2B390DMq3%2BMwAiA%2Bia0U7iWyPGFwdoEWICTCLitK1SqIXe2xT354Rc3ziyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWJtSFKf8wTSCAi%2BKtwD8cBG4fSJcxJFtAq1NfF6qQZ8%2FiUtq3%2FIHRi81sds%2B5rXW88YtJofhA2cKoZb%2F7hGexVFIlaS%2FOx97fPT%2BFn8nMXktj%2Ba%2BrHxnPvOmRLDXv9yQsSOZjyhka7l43%2FEK5nD%2FQrf%2BtEN5Sc6oCdHWhEaPNUMYEEwDXsnOWNiif%2BDRetLZSE4Xql0pL2ko0W%2BbHr1A%2BZ9BG293c4zWgmDBvgnIehKbQ4i8D7masA9IGU0ihsvrYaXt%2BjveYSCXsVCsz8wjWrnRAAJLUZjyGB4dVo58t7U6mYrxZb6NlHJHhBqjFUlQ0F2tXj%2BVFY0NLrXmckmF71no5DUlh1SPgKa%2BVrMohKC4gCwaTBs8jzl2Z8jl2v13dq%2Bzd%2FijrriUUY5MwMJeO8JpBgHuGz1k8FzFHmiVAciTeMFEOXsiqFHwpN4GcE52h%2BqZ2Ej0h5KkL%2Ff%2BE9%2BKbnFCq3gd4I8zVbQunUuTHyEbK0WDE3KaKxTzL7Ihehw%2F%2BQIjCurDgE3gyUD%2F%2BBuVPi4%2F2llPSnM2OncbBTzerLtyhjxCl4eMgvbOHsLCAct%2BZ529JTs5cF%2B68Oebeo5d%2B%2B45%2BNXE3nOjYqpHm7LtL0QwjU0b2PppjULxZox%2BlpPNpz%2FXTwUxBRP2WEwn%2BT%2BvAY6pgHZUT%2F6AnDEL0Oo3b%2FGpw5AiJTCarN69pPxBkctFIBsKcNUpUZ5VmNqXvUjfzuyEXZnR1GzRrp4qmo%2BLwOAt7GR5A0ZrJtn65kl0uiubhg4g51UXwMK9xKS08Q6v0dFBXSrsuyAh0wXxuXZ8ifb1W7Hx5f4STb07a3gCOMJ4kTfeLGWbq%2F0XVSMxxs7b3ZE2g0EMKrBZe337vtbqarpFKwkDoBzqQVO&X-Amz-Signature=44ec57fe47615555f98673207e1bf0a9cccf7ca10eb5478cb343d10a2e1ac05b&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QJRBOF7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTfKyKQ7wo8d3EQmaonvNW0ykUZkiqfKM2897Cnx%2FgXAIhAPnrDaWB2JOpu3JFnhsTzyTb1yAra%2FDFeJ2uhrt2S8zzKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBiWAH5OVqTuGsCzwq3AMqP%2FEi9YBCRmTffj%2BmRizrRUpPlAN0suqx5O3wJvmcG4Su%2FslxdI0sXnrQhXxn14Fwji2mtSCU1NQFGdOK6Kn%2F1kuNUVQ7CMpOAy4Wao%2BtVTOp3qBeWg3pDCQbcaECv%2BVijET3mUXFd1xHJBj5xs8JgrAuOGp962wvKEMGZb%2FGvEIhlrZLa01u3evGyH6D9G9jh6QBLOWCgZw5CdfmowP1Fw12ancjWbVMJXhmMUMHRnmLqUj67RMbfPFSoIxSUKHU4%2BFVkZIA16pRTpfTLanxe1Rr8a%2BoAsFzA%2BVYFi6N6Mv8aw5V08ig9TRYIq6UtOrPTSyyX1m9wylYO%2FtjlzXoPqvDX3x89DiXVuyxJuEonBh%2BdqTMizyaa8Zpf%2Be5IVJIrnCG%2B9Knzh2Va6CHUIHq%2FaTxjLgVdjBSMXvVbhXerRFyxyyaSc1jmtto0ET2IpRNkAzsUmXAxYaQX%2BTpIDJmA%2Fo37JKFybmdWyOnAdFPiqXRoL3g4NKibQ8qmY1OahuU6%2BSmBXL3TG9Vg3whugmSGxWV%2B0lakKgTz7yUSnUywyngS2Ung5dzSf5RINh2ZnncDiwZS8r%2B%2F1oh9jOfEwBYvglOl0FNAmpOkfjcdXjMXVnUfaiUfen8ow3TbjCG4f68BjqkAYjY%2FHcS%2FE19e5RV8JXditsvsELoatU6Hz44ML9dkvdaAm1QY4FG4cfl4Qe1F3jBem1aGu8NRlfclDadZ7VndFb5IXJuXh7KOyoN%2FPfBBqtanqE75A2gfNxp400p6k7VHbj84Vw2fyvHVVvDyYF9plivW8QS2oV20DmDX%2BWmM3R375sGUTMt0F0b6vFDmwQgGndljkh9l6j%2FWWnBcGxOL0SxOvPz&X-Amz-Signature=cc7261d9bab631becfc8fae2ba531222ff355d048007dd0104ab3496d944bbe1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QJRBOF7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTfKyKQ7wo8d3EQmaonvNW0ykUZkiqfKM2897Cnx%2FgXAIhAPnrDaWB2JOpu3JFnhsTzyTb1yAra%2FDFeJ2uhrt2S8zzKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBiWAH5OVqTuGsCzwq3AMqP%2FEi9YBCRmTffj%2BmRizrRUpPlAN0suqx5O3wJvmcG4Su%2FslxdI0sXnrQhXxn14Fwji2mtSCU1NQFGdOK6Kn%2F1kuNUVQ7CMpOAy4Wao%2BtVTOp3qBeWg3pDCQbcaECv%2BVijET3mUXFd1xHJBj5xs8JgrAuOGp962wvKEMGZb%2FGvEIhlrZLa01u3evGyH6D9G9jh6QBLOWCgZw5CdfmowP1Fw12ancjWbVMJXhmMUMHRnmLqUj67RMbfPFSoIxSUKHU4%2BFVkZIA16pRTpfTLanxe1Rr8a%2BoAsFzA%2BVYFi6N6Mv8aw5V08ig9TRYIq6UtOrPTSyyX1m9wylYO%2FtjlzXoPqvDX3x89DiXVuyxJuEonBh%2BdqTMizyaa8Zpf%2Be5IVJIrnCG%2B9Knzh2Va6CHUIHq%2FaTxjLgVdjBSMXvVbhXerRFyxyyaSc1jmtto0ET2IpRNkAzsUmXAxYaQX%2BTpIDJmA%2Fo37JKFybmdWyOnAdFPiqXRoL3g4NKibQ8qmY1OahuU6%2BSmBXL3TG9Vg3whugmSGxWV%2B0lakKgTz7yUSnUywyngS2Ung5dzSf5RINh2ZnncDiwZS8r%2B%2F1oh9jOfEwBYvglOl0FNAmpOkfjcdXjMXVnUfaiUfen8ow3TbjCG4f68BjqkAYjY%2FHcS%2FE19e5RV8JXditsvsELoatU6Hz44ML9dkvdaAm1QY4FG4cfl4Qe1F3jBem1aGu8NRlfclDadZ7VndFb5IXJuXh7KOyoN%2FPfBBqtanqE75A2gfNxp400p6k7VHbj84Vw2fyvHVVvDyYF9plivW8QS2oV20DmDX%2BWmM3R375sGUTMt0F0b6vFDmwQgGndljkh9l6j%2FWWnBcGxOL0SxOvPz&X-Amz-Signature=eab58ab1d372d2e47998fbf0f4e8a69419f824f5e3f885b042fab454e46ccce5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU7HL2JN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACyl2tmylS8d8tmGjbi4788CLDuSp0FB%2B390DMq3%2BMwAiA%2Bia0U7iWyPGFwdoEWICTCLitK1SqIXe2xT354Rc3ziyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdWJtSFKf8wTSCAi%2BKtwD8cBG4fSJcxJFtAq1NfF6qQZ8%2FiUtq3%2FIHRi81sds%2B5rXW88YtJofhA2cKoZb%2F7hGexVFIlaS%2FOx97fPT%2BFn8nMXktj%2Ba%2BrHxnPvOmRLDXv9yQsSOZjyhka7l43%2FEK5nD%2FQrf%2BtEN5Sc6oCdHWhEaPNUMYEEwDXsnOWNiif%2BDRetLZSE4Xql0pL2ko0W%2BbHr1A%2BZ9BG293c4zWgmDBvgnIehKbQ4i8D7masA9IGU0ihsvrYaXt%2BjveYSCXsVCsz8wjWrnRAAJLUZjyGB4dVo58t7U6mYrxZb6NlHJHhBqjFUlQ0F2tXj%2BVFY0NLrXmckmF71no5DUlh1SPgKa%2BVrMohKC4gCwaTBs8jzl2Z8jl2v13dq%2Bzd%2FijrriUUY5MwMJeO8JpBgHuGz1k8FzFHmiVAciTeMFEOXsiqFHwpN4GcE52h%2BqZ2Ej0h5KkL%2Ff%2BE9%2BKbnFCq3gd4I8zVbQunUuTHyEbK0WDE3KaKxTzL7Ihehw%2F%2BQIjCurDgE3gyUD%2F%2BBuVPi4%2F2llPSnM2OncbBTzerLtyhjxCl4eMgvbOHsLCAct%2BZ529JTs5cF%2B68Oebeo5d%2B%2B45%2BNXE3nOjYqpHm7LtL0QwjU0b2PppjULxZox%2BlpPNpz%2FXTwUxBRP2WEwn%2BT%2BvAY6pgHZUT%2F6AnDEL0Oo3b%2FGpw5AiJTCarN69pPxBkctFIBsKcNUpUZ5VmNqXvUjfzuyEXZnR1GzRrp4qmo%2BLwOAt7GR5A0ZrJtn65kl0uiubhg4g51UXwMK9xKS08Q6v0dFBXSrsuyAh0wXxuXZ8ifb1W7Hx5f4STb07a3gCOMJ4kTfeLGWbq%2F0XVSMxxs7b3ZE2g0EMKrBZe337vtbqarpFKwkDoBzqQVO&X-Amz-Signature=eeca9ed3184bf46a9df96da4d41783816ff9ca7740b291777dd134e4958b32d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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