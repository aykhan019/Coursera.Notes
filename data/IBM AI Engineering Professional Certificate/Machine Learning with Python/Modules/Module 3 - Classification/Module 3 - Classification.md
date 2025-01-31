

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VQ5DBJP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2Bzz1a8CbIzYxUZ%2FdlzparHeYkjEisgfl2EOL2voHnjAiACf1aCX6Dg9wNciAl%2B%2Ft6J4PQFxWGvGk17FoWmR%2BLA0SqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjz80muf4KlpPPR55KtwDFHKYInoqGWQXUjQdk35g%2B70eQ6CAFiyKsGA%2Bmt5mJblyVvh7SmGBTs%2Fd%2BF93BzWW3n8ycfPOUG5vhKeeqCkPIAzYkcqP%2BbESkg5FsJzro6JyEvVwTKHwivLuyHfZelB0Ecz%2F36ehbzoRUJsCnR%2FG1jpKJF%2BHDaLw8wV1hQsxY4nA7PdTYhcu1FhJ7rXmIsOsjOh7IJNjaEky9eLdqPjGuX4IFYvbwGFzNSI2JrTImkmcvxuf5C3l27F4nQItIA%2BY9nnXaH3zlhLGHbQbCveA5BxzOYGftNNfTbD%2FZr5I0O8kvw1d0inuNn7YXYEzc07zfR5bZGPcim33OyaMSijUUUS94zf9QtZNR2CjQKW1hz42sS%2F%2FAFSNw03vSA7MS4SEJ3tM1czTdIM58Fj0X3B2%2B8MBtRbryOGDOgbYYbFM5W%2FgYSuqr%2FDVMFj1nWw35ChYfyrNIQDCjkxyZDh1BPhDGCP%2BoQ%2BGr2W17fb7YvQrILd0b3xctQd4tmcGZdB7wtYkqMTb8ZjfVqGN3ekl8ARYxZubZVvUHCEhgTpbFf%2F%2FJ8YEkDYbZ1KrKsczpLFQr8P%2F1YRafrSXH8ZD2%2BEIC2trns%2Fu3es%2BKSxMIG5hvjKyYvnVBatw3iJ6AumbLmYw6I%2FzvAY6pgG0aODzOqLTC%2BPpIm92%2Fn6ysw8TWA3NE7SG3nW5CvM0BBBZ%2FhPv%2B1%2F4h5LEriUAQ7x%2BTKj5rIL7U45HmYbii3DcwfnuNpHH6UQjvX2AuCMGv%2Fdlq75X0%2BQTd7DNvOjivi5OS9UxVgnKLDJLX59ur3GxK9gkFEjzIizFSvp0Egcu95DwzeZgFQB8MBuCTBwf8mN2YsFWO0rjpJm64yQErKhZt4XyAax7&X-Amz-Signature=64726246b5cd184a18edb6c44fb95d7843c2b249f9ee07188a2ee27b966ee5ee&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VQ5DBJP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2Bzz1a8CbIzYxUZ%2FdlzparHeYkjEisgfl2EOL2voHnjAiACf1aCX6Dg9wNciAl%2B%2Ft6J4PQFxWGvGk17FoWmR%2BLA0SqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjz80muf4KlpPPR55KtwDFHKYInoqGWQXUjQdk35g%2B70eQ6CAFiyKsGA%2Bmt5mJblyVvh7SmGBTs%2Fd%2BF93BzWW3n8ycfPOUG5vhKeeqCkPIAzYkcqP%2BbESkg5FsJzro6JyEvVwTKHwivLuyHfZelB0Ecz%2F36ehbzoRUJsCnR%2FG1jpKJF%2BHDaLw8wV1hQsxY4nA7PdTYhcu1FhJ7rXmIsOsjOh7IJNjaEky9eLdqPjGuX4IFYvbwGFzNSI2JrTImkmcvxuf5C3l27F4nQItIA%2BY9nnXaH3zlhLGHbQbCveA5BxzOYGftNNfTbD%2FZr5I0O8kvw1d0inuNn7YXYEzc07zfR5bZGPcim33OyaMSijUUUS94zf9QtZNR2CjQKW1hz42sS%2F%2FAFSNw03vSA7MS4SEJ3tM1czTdIM58Fj0X3B2%2B8MBtRbryOGDOgbYYbFM5W%2FgYSuqr%2FDVMFj1nWw35ChYfyrNIQDCjkxyZDh1BPhDGCP%2BoQ%2BGr2W17fb7YvQrILd0b3xctQd4tmcGZdB7wtYkqMTb8ZjfVqGN3ekl8ARYxZubZVvUHCEhgTpbFf%2F%2FJ8YEkDYbZ1KrKsczpLFQr8P%2F1YRafrSXH8ZD2%2BEIC2trns%2Fu3es%2BKSxMIG5hvjKyYvnVBatw3iJ6AumbLmYw6I%2FzvAY6pgG0aODzOqLTC%2BPpIm92%2Fn6ysw8TWA3NE7SG3nW5CvM0BBBZ%2FhPv%2B1%2F4h5LEriUAQ7x%2BTKj5rIL7U45HmYbii3DcwfnuNpHH6UQjvX2AuCMGv%2Fdlq75X0%2BQTd7DNvOjivi5OS9UxVgnKLDJLX59ur3GxK9gkFEjzIizFSvp0Egcu95DwzeZgFQB8MBuCTBwf8mN2YsFWO0rjpJm64yQErKhZt4XyAax7&X-Amz-Signature=e45eb6340dffafe5c2eac4d7268d1ca10de944bdafeac5cf8dadcd17abbe7e8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VQ5DBJP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2Bzz1a8CbIzYxUZ%2FdlzparHeYkjEisgfl2EOL2voHnjAiACf1aCX6Dg9wNciAl%2B%2Ft6J4PQFxWGvGk17FoWmR%2BLA0SqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjz80muf4KlpPPR55KtwDFHKYInoqGWQXUjQdk35g%2B70eQ6CAFiyKsGA%2Bmt5mJblyVvh7SmGBTs%2Fd%2BF93BzWW3n8ycfPOUG5vhKeeqCkPIAzYkcqP%2BbESkg5FsJzro6JyEvVwTKHwivLuyHfZelB0Ecz%2F36ehbzoRUJsCnR%2FG1jpKJF%2BHDaLw8wV1hQsxY4nA7PdTYhcu1FhJ7rXmIsOsjOh7IJNjaEky9eLdqPjGuX4IFYvbwGFzNSI2JrTImkmcvxuf5C3l27F4nQItIA%2BY9nnXaH3zlhLGHbQbCveA5BxzOYGftNNfTbD%2FZr5I0O8kvw1d0inuNn7YXYEzc07zfR5bZGPcim33OyaMSijUUUS94zf9QtZNR2CjQKW1hz42sS%2F%2FAFSNw03vSA7MS4SEJ3tM1czTdIM58Fj0X3B2%2B8MBtRbryOGDOgbYYbFM5W%2FgYSuqr%2FDVMFj1nWw35ChYfyrNIQDCjkxyZDh1BPhDGCP%2BoQ%2BGr2W17fb7YvQrILd0b3xctQd4tmcGZdB7wtYkqMTb8ZjfVqGN3ekl8ARYxZubZVvUHCEhgTpbFf%2F%2FJ8YEkDYbZ1KrKsczpLFQr8P%2F1YRafrSXH8ZD2%2BEIC2trns%2Fu3es%2BKSxMIG5hvjKyYvnVBatw3iJ6AumbLmYw6I%2FzvAY6pgG0aODzOqLTC%2BPpIm92%2Fn6ysw8TWA3NE7SG3nW5CvM0BBBZ%2FhPv%2B1%2F4h5LEriUAQ7x%2BTKj5rIL7U45HmYbii3DcwfnuNpHH6UQjvX2AuCMGv%2Fdlq75X0%2BQTd7DNvOjivi5OS9UxVgnKLDJLX59ur3GxK9gkFEjzIizFSvp0Egcu95DwzeZgFQB8MBuCTBwf8mN2YsFWO0rjpJm64yQErKhZt4XyAax7&X-Amz-Signature=eae1d2fed16e4afdcd249913a1e017048cf505ee559628a4068062d8458edf93&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EE7OGRP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdZPz9a5N%2BtCHyByt4HulZwBg%2FTbqcuevdWVCQEG9KjAIgSnuYbnPW12KSRQhYM0z3j9OS01E1Eela59Tsbh683G0qiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLOlbcFUVEoOPmSg%2FSrcA4DCFB%2FTl6NmyV9oWJ0fYyvfDZxmj0I%2FA6OETJs%2FM3S33eRyVSfY%2F4PZUk23GDKAex33914lx%2FLmE1%2BNRvc1Lqhqzlz92dKu1EVXLx%2B8guRkkGmlS25gsazXhccNmPZXvZnPXWBjFkwmsqPS6Oap1o%2Fn0eJKpWVUMUqPv%2BJmsmUcCqJFU7Sz8vuD%2FrA6jR9YCrv2cuFwryhZwf%2BE42%2B8W51EciPbyUx%2B8PbVmOOS1226a%2FllO%2FPwR%2FPWRex2FwameLdKLzDj5oIqb%2FusdVaPKaM3zCLGbqj8apbuxAMN9gy2kXaMECasPpvno4yYOWzm%2FtQSkjm4%2B0xTNz4FQcRiGB9vcQEagTyHSgPlkB01n%2BjlbXbAdXR33lmDmLdxucmF4dEGIr3naqZNjXr8uRjy1KyA27w%2F%2BCruxwcQcGiqlySpJkT5Oz5MBv4twKuHQi33Ql3sYz5LM5rMBUrN5xAW%2BH7vdAM98QMRHEzVoU01uYHBT2GHeOErf%2BZZV%2BWJbm8Nb6OOIQThuPx%2BMtKo0RaV9EN2hhRl%2FqhcNmOFcs5lmwFzQXwRVLnLmASj0%2FzSEIxclHD42ifjMxu%2BrYKq9IYEdCLl1C3TNiIZA3XxPioMyu%2FO4LGN9q%2FbICQ95so6MOGP87wGOqUBoCsQZn%2F3W2hjhayB8C1%2B8R2xQ4ntx7uyiAjziDdUmF1Cml16j2rmUxfbhIwF0eWpcf%2Bt3%2FOUWXfijJ6IINvHxMfaxIwhpHlKnZUpVvhNpI%2BPdOamwhZEx1Wha8SfLvgGa4JDOehbBp4cmKLxDc8Jwd9jAtmjGSfJe2%2F30nCwCgk8upPqBKYa8UsQQOLllF8Ioe%2BUlfps%2BfuOLSqsEcx7pXQVdtWh&X-Amz-Signature=f6c505d620f396089e2315058195fbf02a5f99a25cf81884a99e7a776ca5a66a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EE7OGRP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdZPz9a5N%2BtCHyByt4HulZwBg%2FTbqcuevdWVCQEG9KjAIgSnuYbnPW12KSRQhYM0z3j9OS01E1Eela59Tsbh683G0qiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLOlbcFUVEoOPmSg%2FSrcA4DCFB%2FTl6NmyV9oWJ0fYyvfDZxmj0I%2FA6OETJs%2FM3S33eRyVSfY%2F4PZUk23GDKAex33914lx%2FLmE1%2BNRvc1Lqhqzlz92dKu1EVXLx%2B8guRkkGmlS25gsazXhccNmPZXvZnPXWBjFkwmsqPS6Oap1o%2Fn0eJKpWVUMUqPv%2BJmsmUcCqJFU7Sz8vuD%2FrA6jR9YCrv2cuFwryhZwf%2BE42%2B8W51EciPbyUx%2B8PbVmOOS1226a%2FllO%2FPwR%2FPWRex2FwameLdKLzDj5oIqb%2FusdVaPKaM3zCLGbqj8apbuxAMN9gy2kXaMECasPpvno4yYOWzm%2FtQSkjm4%2B0xTNz4FQcRiGB9vcQEagTyHSgPlkB01n%2BjlbXbAdXR33lmDmLdxucmF4dEGIr3naqZNjXr8uRjy1KyA27w%2F%2BCruxwcQcGiqlySpJkT5Oz5MBv4twKuHQi33Ql3sYz5LM5rMBUrN5xAW%2BH7vdAM98QMRHEzVoU01uYHBT2GHeOErf%2BZZV%2BWJbm8Nb6OOIQThuPx%2BMtKo0RaV9EN2hhRl%2FqhcNmOFcs5lmwFzQXwRVLnLmASj0%2FzSEIxclHD42ifjMxu%2BrYKq9IYEdCLl1C3TNiIZA3XxPioMyu%2FO4LGN9q%2FbICQ95so6MOGP87wGOqUBoCsQZn%2F3W2hjhayB8C1%2B8R2xQ4ntx7uyiAjziDdUmF1Cml16j2rmUxfbhIwF0eWpcf%2Bt3%2FOUWXfijJ6IINvHxMfaxIwhpHlKnZUpVvhNpI%2BPdOamwhZEx1Wha8SfLvgGa4JDOehbBp4cmKLxDc8Jwd9jAtmjGSfJe2%2F30nCwCgk8upPqBKYa8UsQQOLllF8Ioe%2BUlfps%2BfuOLSqsEcx7pXQVdtWh&X-Amz-Signature=612a4337b10cacd972909804d5720cba38a35dfe198987032dbcc7f4c12d5e17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VQ5DBJP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2Bzz1a8CbIzYxUZ%2FdlzparHeYkjEisgfl2EOL2voHnjAiACf1aCX6Dg9wNciAl%2B%2Ft6J4PQFxWGvGk17FoWmR%2BLA0SqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjz80muf4KlpPPR55KtwDFHKYInoqGWQXUjQdk35g%2B70eQ6CAFiyKsGA%2Bmt5mJblyVvh7SmGBTs%2Fd%2BF93BzWW3n8ycfPOUG5vhKeeqCkPIAzYkcqP%2BbESkg5FsJzro6JyEvVwTKHwivLuyHfZelB0Ecz%2F36ehbzoRUJsCnR%2FG1jpKJF%2BHDaLw8wV1hQsxY4nA7PdTYhcu1FhJ7rXmIsOsjOh7IJNjaEky9eLdqPjGuX4IFYvbwGFzNSI2JrTImkmcvxuf5C3l27F4nQItIA%2BY9nnXaH3zlhLGHbQbCveA5BxzOYGftNNfTbD%2FZr5I0O8kvw1d0inuNn7YXYEzc07zfR5bZGPcim33OyaMSijUUUS94zf9QtZNR2CjQKW1hz42sS%2F%2FAFSNw03vSA7MS4SEJ3tM1czTdIM58Fj0X3B2%2B8MBtRbryOGDOgbYYbFM5W%2FgYSuqr%2FDVMFj1nWw35ChYfyrNIQDCjkxyZDh1BPhDGCP%2BoQ%2BGr2W17fb7YvQrILd0b3xctQd4tmcGZdB7wtYkqMTb8ZjfVqGN3ekl8ARYxZubZVvUHCEhgTpbFf%2F%2FJ8YEkDYbZ1KrKsczpLFQr8P%2F1YRafrSXH8ZD2%2BEIC2trns%2Fu3es%2BKSxMIG5hvjKyYvnVBatw3iJ6AumbLmYw6I%2FzvAY6pgG0aODzOqLTC%2BPpIm92%2Fn6ysw8TWA3NE7SG3nW5CvM0BBBZ%2FhPv%2B1%2F4h5LEriUAQ7x%2BTKj5rIL7U45HmYbii3DcwfnuNpHH6UQjvX2AuCMGv%2Fdlq75X0%2BQTd7DNvOjivi5OS9UxVgnKLDJLX59ur3GxK9gkFEjzIizFSvp0Egcu95DwzeZgFQB8MBuCTBwf8mN2YsFWO0rjpJm64yQErKhZt4XyAax7&X-Amz-Signature=8a64263c7d0324a7fb5ad27a7562a9d51e623dd0f84de7b5abc1770b98799289&X-Amz-SignedHeaders=host&x-id=GetObject)
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