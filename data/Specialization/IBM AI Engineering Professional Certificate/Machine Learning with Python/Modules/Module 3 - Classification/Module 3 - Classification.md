

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U6Q5T7X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYeaa6i1zycAgr7XwT5RqOLYkWVyh4xrjJMBzdiijCpwIhAINkySUeCo3kCd4Iazi8Lpg7wQ%2FZ6wkcbrQ8jkd67eP4KogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igya7HP%2FrqqwfVWnKQ4q3AMdgNzq%2B%2FZUmqQP0JHmpU1TOytb0giEpSqjnKgTiJMJ4K3sqA1admjeaqK%2FxZPgGTW9CK95v5g2x8z9asat1Z5y6uNNTEC3Mlal0Y%2F1AjEeGDnCYDiHAOXxJKWEs%2Fe2Vx0GJiZZDoT0FVMP%2FIDd7C9miU9HMc80YW9c3BdoYQxzfYPSlALe%2BsA49tufZ8veXfzMGbLGLh9FdBLM8Gi%2F7Fa8c4Xh9I6b2MU0udgMaOgopg56oJJhoiqUVIvmUZdb%2Bg8eHNl9XJCd72kro7eof9jypPuzd%2FJbdTFFo19dKoMKy3BKHrjylgbwHMoZNxVuiCIPNt5ydVbbadxkV4wrIppxMpuNV6goOVKqWCLAxpXQUbm6edtyYTtNVic1t5rFMT6H%2FR02Bg7KCgR8mSjuB43%2Fda1oEneleFpxYMdHZOtdLzofPLqnb%2F0bE%2FdVF6MB8kJFINfS9rQz%2Bmgkq556k18ym2j0T3XC9Vu3c1sOAt7XZdcOp4llTZ8wHTI2GqMUScMu9Flg2avpy17eE5QMVqzB3tXV3nf%2FvsEyGRyG7JSsIV56eiq7ziwY%2B3hf47DW1aTq4IP1%2BMJudGiQ6oHjjgDhKKHGfM1DQYvG9MPrD1%2FKBmGTsrtQqTbXychWVzC83u28BjqkAdom5V3jf4GBD2uqVOWzuDP0xYKqNp5DfxCFrusGOqMgcv9gM%2BdN4oBmHr7YErO%2BY%2B9JHW60fL4bEYGlBlFXC1qCwU4bKlqlY8YpFog%2FVVR3u5aELnu6V2aBeifPs8SBP%2FtthEHy7hpNa5rvSQnrqTi47wDhwAE%2BjNa2wP4OVFUwTX4T%2Fmrr%2Fc%2BstzLC%2FRad%2Bv0wX8fBaNA2RA%2BDfw%2FbrW%2BvJeo7&X-Amz-Signature=6c03793c36be2a8695572d164bd2fc8c71d38c7f58f77865117bc8bd4dfb4538&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U6Q5T7X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYeaa6i1zycAgr7XwT5RqOLYkWVyh4xrjJMBzdiijCpwIhAINkySUeCo3kCd4Iazi8Lpg7wQ%2FZ6wkcbrQ8jkd67eP4KogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igya7HP%2FrqqwfVWnKQ4q3AMdgNzq%2B%2FZUmqQP0JHmpU1TOytb0giEpSqjnKgTiJMJ4K3sqA1admjeaqK%2FxZPgGTW9CK95v5g2x8z9asat1Z5y6uNNTEC3Mlal0Y%2F1AjEeGDnCYDiHAOXxJKWEs%2Fe2Vx0GJiZZDoT0FVMP%2FIDd7C9miU9HMc80YW9c3BdoYQxzfYPSlALe%2BsA49tufZ8veXfzMGbLGLh9FdBLM8Gi%2F7Fa8c4Xh9I6b2MU0udgMaOgopg56oJJhoiqUVIvmUZdb%2Bg8eHNl9XJCd72kro7eof9jypPuzd%2FJbdTFFo19dKoMKy3BKHrjylgbwHMoZNxVuiCIPNt5ydVbbadxkV4wrIppxMpuNV6goOVKqWCLAxpXQUbm6edtyYTtNVic1t5rFMT6H%2FR02Bg7KCgR8mSjuB43%2Fda1oEneleFpxYMdHZOtdLzofPLqnb%2F0bE%2FdVF6MB8kJFINfS9rQz%2Bmgkq556k18ym2j0T3XC9Vu3c1sOAt7XZdcOp4llTZ8wHTI2GqMUScMu9Flg2avpy17eE5QMVqzB3tXV3nf%2FvsEyGRyG7JSsIV56eiq7ziwY%2B3hf47DW1aTq4IP1%2BMJudGiQ6oHjjgDhKKHGfM1DQYvG9MPrD1%2FKBmGTsrtQqTbXychWVzC83u28BjqkAdom5V3jf4GBD2uqVOWzuDP0xYKqNp5DfxCFrusGOqMgcv9gM%2BdN4oBmHr7YErO%2BY%2B9JHW60fL4bEYGlBlFXC1qCwU4bKlqlY8YpFog%2FVVR3u5aELnu6V2aBeifPs8SBP%2FtthEHy7hpNa5rvSQnrqTi47wDhwAE%2BjNa2wP4OVFUwTX4T%2Fmrr%2Fc%2BstzLC%2FRad%2Bv0wX8fBaNA2RA%2BDfw%2FbrW%2BvJeo7&X-Amz-Signature=8ec6485ded7f20716d411a36b5ed54bb09e77d52332ea0c71a1e93e8a513fd9a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U6Q5T7X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYeaa6i1zycAgr7XwT5RqOLYkWVyh4xrjJMBzdiijCpwIhAINkySUeCo3kCd4Iazi8Lpg7wQ%2FZ6wkcbrQ8jkd67eP4KogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igya7HP%2FrqqwfVWnKQ4q3AMdgNzq%2B%2FZUmqQP0JHmpU1TOytb0giEpSqjnKgTiJMJ4K3sqA1admjeaqK%2FxZPgGTW9CK95v5g2x8z9asat1Z5y6uNNTEC3Mlal0Y%2F1AjEeGDnCYDiHAOXxJKWEs%2Fe2Vx0GJiZZDoT0FVMP%2FIDd7C9miU9HMc80YW9c3BdoYQxzfYPSlALe%2BsA49tufZ8veXfzMGbLGLh9FdBLM8Gi%2F7Fa8c4Xh9I6b2MU0udgMaOgopg56oJJhoiqUVIvmUZdb%2Bg8eHNl9XJCd72kro7eof9jypPuzd%2FJbdTFFo19dKoMKy3BKHrjylgbwHMoZNxVuiCIPNt5ydVbbadxkV4wrIppxMpuNV6goOVKqWCLAxpXQUbm6edtyYTtNVic1t5rFMT6H%2FR02Bg7KCgR8mSjuB43%2Fda1oEneleFpxYMdHZOtdLzofPLqnb%2F0bE%2FdVF6MB8kJFINfS9rQz%2Bmgkq556k18ym2j0T3XC9Vu3c1sOAt7XZdcOp4llTZ8wHTI2GqMUScMu9Flg2avpy17eE5QMVqzB3tXV3nf%2FvsEyGRyG7JSsIV56eiq7ziwY%2B3hf47DW1aTq4IP1%2BMJudGiQ6oHjjgDhKKHGfM1DQYvG9MPrD1%2FKBmGTsrtQqTbXychWVzC83u28BjqkAdom5V3jf4GBD2uqVOWzuDP0xYKqNp5DfxCFrusGOqMgcv9gM%2BdN4oBmHr7YErO%2BY%2B9JHW60fL4bEYGlBlFXC1qCwU4bKlqlY8YpFog%2FVVR3u5aELnu6V2aBeifPs8SBP%2FtthEHy7hpNa5rvSQnrqTi47wDhwAE%2BjNa2wP4OVFUwTX4T%2Fmrr%2Fc%2BstzLC%2FRad%2Bv0wX8fBaNA2RA%2BDfw%2FbrW%2BvJeo7&X-Amz-Signature=707cf557865110992ab25173ebbc58c2b19ea86396f7f3e91ae8a18671ec42fe&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US6PBU7N%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCttlfjdfw8MSdbdjVCT5XHQ4P7Dx7%2BzniHnFW7zSldEAIgSdIm6eeTzq0tH7rmoSsoSPBlBreVXiFkmlbcYxSv5yQqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKxY9VESMRBAHHk4XircA%2F%2FVYU0bqzbKCWSZCHW5Ln2%2Fn5ZFLbY8KRkjcTMMrafPlRtYaZPn7tvkxma7RF8UVhFY2A1B3FOthYGLUxClGrR8zWTF6rH1hFVh%2BB6AqL6X%2FhDRllGljfk5iyqaGxhMn8nYzi1yuRCRaKnBfG3NegYYQqaISr0FDKA%2FLmU24peb8yuvb1INddqrRnxfKZcZbKx%2B6nbaTK97V7QqdxTJFYZYJJoP8oRd1qt3uYD2A7MlzCnXZ1CxMRPoLcriSntvsdh7n479dm5LJDAFr3gsWIOD8d28g9u5RO1%2BrcRpGprhXel9yhc92N2R3xNQG8F%2Fgyc0BfNnU0AGL3CZqMXsvoX9hC%2BKoPA6S2OWtvkKSFqtO8w%2F%2BnF12TiJTZK1dE0Ha%2F9UGSccsR75NVIlBinTYRaiCW7ZWy90ltiaCeLupWmZC%2BU6QVp3%2F0Rqzv35Tpyf%2BSWkJZTkMcYDyW1NSfqS2MCiSDVj7Y2Ptw%2FELHOPrHl2HB2cRtxQMiNjEBeEPNL%2BqYuJoCovebHGn5k4Y5Grv042DWPoZTGZgE12i2E0Zg12nda8tDItJuXPYA%2B2pDl85CP4PU8%2BaQXvFqoqECBXMcA8PbchFq%2FoCFpJrho%2BpYVtR9jLtMJA2bM958LpMLze7bwGOqUB4P4W62JbeSzN3I3wsYtZJ2WjzJiF%2Bilhl1mxxZ3cCsxuCWb7%2FWh9LMdS5siM7GGRJmXwoWvi%2Bo6DfKVRYo3vyHHjm9Ql%2Fz0ar2OqkTQ%2FAjN5znSDMo9JtiqEuUAEbNHOqZUjqxwkD1agkcz34xdao8PvNTjpRy6DZyApey00A6TeYMicwqmQPszm50%2FaP8Yj1mLAzFIv74nUNU3uuaz06FQD5ye2&X-Amz-Signature=0e6415c841e2edf1d42c95a515cae5ce41dec7cc9bd97853fdd26d3e13ac67fe&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US6PBU7N%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCttlfjdfw8MSdbdjVCT5XHQ4P7Dx7%2BzniHnFW7zSldEAIgSdIm6eeTzq0tH7rmoSsoSPBlBreVXiFkmlbcYxSv5yQqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKxY9VESMRBAHHk4XircA%2F%2FVYU0bqzbKCWSZCHW5Ln2%2Fn5ZFLbY8KRkjcTMMrafPlRtYaZPn7tvkxma7RF8UVhFY2A1B3FOthYGLUxClGrR8zWTF6rH1hFVh%2BB6AqL6X%2FhDRllGljfk5iyqaGxhMn8nYzi1yuRCRaKnBfG3NegYYQqaISr0FDKA%2FLmU24peb8yuvb1INddqrRnxfKZcZbKx%2B6nbaTK97V7QqdxTJFYZYJJoP8oRd1qt3uYD2A7MlzCnXZ1CxMRPoLcriSntvsdh7n479dm5LJDAFr3gsWIOD8d28g9u5RO1%2BrcRpGprhXel9yhc92N2R3xNQG8F%2Fgyc0BfNnU0AGL3CZqMXsvoX9hC%2BKoPA6S2OWtvkKSFqtO8w%2F%2BnF12TiJTZK1dE0Ha%2F9UGSccsR75NVIlBinTYRaiCW7ZWy90ltiaCeLupWmZC%2BU6QVp3%2F0Rqzv35Tpyf%2BSWkJZTkMcYDyW1NSfqS2MCiSDVj7Y2Ptw%2FELHOPrHl2HB2cRtxQMiNjEBeEPNL%2BqYuJoCovebHGn5k4Y5Grv042DWPoZTGZgE12i2E0Zg12nda8tDItJuXPYA%2B2pDl85CP4PU8%2BaQXvFqoqECBXMcA8PbchFq%2FoCFpJrho%2BpYVtR9jLtMJA2bM958LpMLze7bwGOqUB4P4W62JbeSzN3I3wsYtZJ2WjzJiF%2Bilhl1mxxZ3cCsxuCWb7%2FWh9LMdS5siM7GGRJmXwoWvi%2Bo6DfKVRYo3vyHHjm9Ql%2Fz0ar2OqkTQ%2FAjN5znSDMo9JtiqEuUAEbNHOqZUjqxwkD1agkcz34xdao8PvNTjpRy6DZyApey00A6TeYMicwqmQPszm50%2FaP8Yj1mLAzFIv74nUNU3uuaz06FQD5ye2&X-Amz-Signature=6ab62013935f0e8a4f907971dde3fb0240754d6878e6ea3b9ad9bc663bada590&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U6Q5T7X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYeaa6i1zycAgr7XwT5RqOLYkWVyh4xrjJMBzdiijCpwIhAINkySUeCo3kCd4Iazi8Lpg7wQ%2FZ6wkcbrQ8jkd67eP4KogECKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igya7HP%2FrqqwfVWnKQ4q3AMdgNzq%2B%2FZUmqQP0JHmpU1TOytb0giEpSqjnKgTiJMJ4K3sqA1admjeaqK%2FxZPgGTW9CK95v5g2x8z9asat1Z5y6uNNTEC3Mlal0Y%2F1AjEeGDnCYDiHAOXxJKWEs%2Fe2Vx0GJiZZDoT0FVMP%2FIDd7C9miU9HMc80YW9c3BdoYQxzfYPSlALe%2BsA49tufZ8veXfzMGbLGLh9FdBLM8Gi%2F7Fa8c4Xh9I6b2MU0udgMaOgopg56oJJhoiqUVIvmUZdb%2Bg8eHNl9XJCd72kro7eof9jypPuzd%2FJbdTFFo19dKoMKy3BKHrjylgbwHMoZNxVuiCIPNt5ydVbbadxkV4wrIppxMpuNV6goOVKqWCLAxpXQUbm6edtyYTtNVic1t5rFMT6H%2FR02Bg7KCgR8mSjuB43%2Fda1oEneleFpxYMdHZOtdLzofPLqnb%2F0bE%2FdVF6MB8kJFINfS9rQz%2Bmgkq556k18ym2j0T3XC9Vu3c1sOAt7XZdcOp4llTZ8wHTI2GqMUScMu9Flg2avpy17eE5QMVqzB3tXV3nf%2FvsEyGRyG7JSsIV56eiq7ziwY%2B3hf47DW1aTq4IP1%2BMJudGiQ6oHjjgDhKKHGfM1DQYvG9MPrD1%2FKBmGTsrtQqTbXychWVzC83u28BjqkAdom5V3jf4GBD2uqVOWzuDP0xYKqNp5DfxCFrusGOqMgcv9gM%2BdN4oBmHr7YErO%2BY%2B9JHW60fL4bEYGlBlFXC1qCwU4bKlqlY8YpFog%2FVVR3u5aELnu6V2aBeifPs8SBP%2FtthEHy7hpNa5rvSQnrqTi47wDhwAE%2BjNa2wP4OVFUwTX4T%2Fmrr%2Fc%2BstzLC%2FRad%2Bv0wX8fBaNA2RA%2BDfw%2FbrW%2BvJeo7&X-Amz-Signature=b0da2846d4158373e4bfc3103198d374648fa2ecda89a23670d8032cc01072c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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