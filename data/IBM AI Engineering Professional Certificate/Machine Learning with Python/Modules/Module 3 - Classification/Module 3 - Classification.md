

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYIVWQI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEvmqe3WAJyUy1cy7IhRfLtCli7yXoqX%2FumplurvQrwZAiAevdzDjZipLHF%2BgHbPeV%2B9x4o54WbXKmKC%2FgCKsxjOwyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgV6Eb0KRGiq6wTO3KtwD88swBs5uVyDhNjvYK0ZDlP41EWYqAjPyoTZEtd6JuBhYo1KOotLlDxUCp2zerwr03aarep27557qns1JHZXdZqYcAIR7LWttQVnDXrxUYx2Cj7St0jKqK3BCziz%2FJlRGniWjtn3Z4SOQbVV4mdKK2lyaeg67vtpYgtnw3k41jSdbj410Q3jmTthZzR4DMzOCJTmHXzkzuJKcR3mnSLAhWJ1SrnBD8PvPbwKQj5CzhdD%2B5o%2BLMRvkttJ1oTwaanfIzu%2FVGcIYF%2FB11Hgs70%2Bhb6ylWtnQcDKyO3RhoS57YDkz5vvb2zK%2BLMLPjX1BLg8uDj%2FGCf0POdkOwikFlMbevE1Zw8GCIWhczdGsCZjJ3E2Bnwo%2Bm%2FAq88igQBxICIwo54s8yJvBVweKOZLCo5tO1%2FMaYdJSiO8%2B3gmxsPzODLY5J12K6wC5%2Fd2nwM4T%2BKRWl17BpRHIAqbC5BAC5pPjDSOL0QUrlifxEARV7ntgyZk8vFLukoBVRdVz6wl6DMPGtzF6XvOdQlvi6iP%2FC7nSEylYi30%2BWIjReDc2xU0gWBdBTpfy9z4sXy3wsT3Y3JwMHd%2F0aYKWqgoCiT5gG56WeEyXhl9fDaAOFWyMjJtIGyNROk7Gqp%2ByHjPma2Aw0779vAY6pgGNCoOaGB7l8E4zav3yAA3DzHHuv4pzGLR1r24GeKnP8TcR2bmju9V7WLl4oWzR3nV3NwyZ7%2F2%2F7TgOEME7%2Bi0YeJLuLp0gDwgbyqKck2OgA%2BEgwg7cQ9IcAQEi68z9hYE9QCEo3eBla81QYLZJ%2FnLBsYZnOApJA8X8t5XRxfVM3iNeCpMWIuBtGhvGzVckN%2FcLDFLKslOh5QcxrSS6%2BID4ykCc8q0W&X-Amz-Signature=1a513cc8f3d38f6b9536e5e42c7afcc8d0ccdd6050882b89ce97d429204d98c5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYIVWQI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEvmqe3WAJyUy1cy7IhRfLtCli7yXoqX%2FumplurvQrwZAiAevdzDjZipLHF%2BgHbPeV%2B9x4o54WbXKmKC%2FgCKsxjOwyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgV6Eb0KRGiq6wTO3KtwD88swBs5uVyDhNjvYK0ZDlP41EWYqAjPyoTZEtd6JuBhYo1KOotLlDxUCp2zerwr03aarep27557qns1JHZXdZqYcAIR7LWttQVnDXrxUYx2Cj7St0jKqK3BCziz%2FJlRGniWjtn3Z4SOQbVV4mdKK2lyaeg67vtpYgtnw3k41jSdbj410Q3jmTthZzR4DMzOCJTmHXzkzuJKcR3mnSLAhWJ1SrnBD8PvPbwKQj5CzhdD%2B5o%2BLMRvkttJ1oTwaanfIzu%2FVGcIYF%2FB11Hgs70%2Bhb6ylWtnQcDKyO3RhoS57YDkz5vvb2zK%2BLMLPjX1BLg8uDj%2FGCf0POdkOwikFlMbevE1Zw8GCIWhczdGsCZjJ3E2Bnwo%2Bm%2FAq88igQBxICIwo54s8yJvBVweKOZLCo5tO1%2FMaYdJSiO8%2B3gmxsPzODLY5J12K6wC5%2Fd2nwM4T%2BKRWl17BpRHIAqbC5BAC5pPjDSOL0QUrlifxEARV7ntgyZk8vFLukoBVRdVz6wl6DMPGtzF6XvOdQlvi6iP%2FC7nSEylYi30%2BWIjReDc2xU0gWBdBTpfy9z4sXy3wsT3Y3JwMHd%2F0aYKWqgoCiT5gG56WeEyXhl9fDaAOFWyMjJtIGyNROk7Gqp%2ByHjPma2Aw0779vAY6pgGNCoOaGB7l8E4zav3yAA3DzHHuv4pzGLR1r24GeKnP8TcR2bmju9V7WLl4oWzR3nV3NwyZ7%2F2%2F7TgOEME7%2Bi0YeJLuLp0gDwgbyqKck2OgA%2BEgwg7cQ9IcAQEi68z9hYE9QCEo3eBla81QYLZJ%2FnLBsYZnOApJA8X8t5XRxfVM3iNeCpMWIuBtGhvGzVckN%2FcLDFLKslOh5QcxrSS6%2BID4ykCc8q0W&X-Amz-Signature=d1902c57799ef9fb2130225804ad8eabb89e444eb711657204b4b5a1ab10a032&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYIVWQI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEvmqe3WAJyUy1cy7IhRfLtCli7yXoqX%2FumplurvQrwZAiAevdzDjZipLHF%2BgHbPeV%2B9x4o54WbXKmKC%2FgCKsxjOwyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgV6Eb0KRGiq6wTO3KtwD88swBs5uVyDhNjvYK0ZDlP41EWYqAjPyoTZEtd6JuBhYo1KOotLlDxUCp2zerwr03aarep27557qns1JHZXdZqYcAIR7LWttQVnDXrxUYx2Cj7St0jKqK3BCziz%2FJlRGniWjtn3Z4SOQbVV4mdKK2lyaeg67vtpYgtnw3k41jSdbj410Q3jmTthZzR4DMzOCJTmHXzkzuJKcR3mnSLAhWJ1SrnBD8PvPbwKQj5CzhdD%2B5o%2BLMRvkttJ1oTwaanfIzu%2FVGcIYF%2FB11Hgs70%2Bhb6ylWtnQcDKyO3RhoS57YDkz5vvb2zK%2BLMLPjX1BLg8uDj%2FGCf0POdkOwikFlMbevE1Zw8GCIWhczdGsCZjJ3E2Bnwo%2Bm%2FAq88igQBxICIwo54s8yJvBVweKOZLCo5tO1%2FMaYdJSiO8%2B3gmxsPzODLY5J12K6wC5%2Fd2nwM4T%2BKRWl17BpRHIAqbC5BAC5pPjDSOL0QUrlifxEARV7ntgyZk8vFLukoBVRdVz6wl6DMPGtzF6XvOdQlvi6iP%2FC7nSEylYi30%2BWIjReDc2xU0gWBdBTpfy9z4sXy3wsT3Y3JwMHd%2F0aYKWqgoCiT5gG56WeEyXhl9fDaAOFWyMjJtIGyNROk7Gqp%2ByHjPma2Aw0779vAY6pgGNCoOaGB7l8E4zav3yAA3DzHHuv4pzGLR1r24GeKnP8TcR2bmju9V7WLl4oWzR3nV3NwyZ7%2F2%2F7TgOEME7%2Bi0YeJLuLp0gDwgbyqKck2OgA%2BEgwg7cQ9IcAQEi68z9hYE9QCEo3eBla81QYLZJ%2FnLBsYZnOApJA8X8t5XRxfVM3iNeCpMWIuBtGhvGzVckN%2FcLDFLKslOh5QcxrSS6%2BID4ykCc8q0W&X-Amz-Signature=5af796ccd28e75f8146ebc7049bc1d6fc676f97507e398014b831c99baea6f65&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RYG2S63%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDq%2FdlmdRkH6d2B%2FuZXUNSkExwyJjJwlcB3%2FdGcHJKa7AIgYxeHm1TU09zl5EYrJPQKuCYko00R%2FowOzunM4zTUAp4qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErGf1aYK9LQ2meTMyrcA8Jq5I%2F7xq0bsKdvVO6uoil2lQDt3QUo5Hj9Cn5QMU8QqbzaKSrVXGF3TjkCR3RDl2qPeW4%2F9pt4I7AgUrN%2BLMqPkMI5kE9giHB5zzDnFfavpyFz8rmvGZZ1Hmknbe8uKitWJyssMsuKvbjwHSsRiSIP7aaGOCXCd7jlXRvqTlz0SHTKhn8VwM3X%2BZsrusLS3FfnxwdAdlJ%2F7LdRaJ%2BHvRw6P47tOexmoT48QeB4%2FpRctVML8gSVBTiN83o0LKnGBg1J72oK8oMJ8hsWy8sd6Rd5Ra%2FlDiZyRrlQc0E5JsxA%2FJwMVOHv28CENnPttQtPKuC8KxNV6yJ%2FBQUQ7pPeQdfYt%2FOpWlQ44D0XAz9dgbZNVZ3CAEZsuP33XSiRinbO31iumSQNHsPdbLtXknJbMsp112Jku35Lnoz2uUknEZmGsBDoUPfCxqCWxzLpdd%2B3HNttCJOyq6wsiyW5I4T4hq7RR9aB2azHk1NikoCHOUGrLlsHspClxn5aTn4J25DxsRiJRgRrtdwBHH5aUNSldYX44KA0QozqxRgQw7kF6RGi088nWUBidqgxXFHthcD2Yio%2B9%2BAq9%2FBMfu8kthrLLCDebFxubUzIOYj%2B%2Bd1pdrg2I%2B8eZm%2FZiRSEbNpVMJq5%2FbwGOqUBJ8FRhHrlWD%2FNAuzSNFR1AMDZCB3hzToskEhAqtvbT9XpmzMDYNTpYhLiDYCKQgV%2F0Gtk8DTqrITNFomjNBILqShMj7TTYHF%2Bnexaj%2FOZHWubz7KgcFsog3BYEuyI%2F7PVOG3iC7%2BBQ7a%2BpCsQkEn1zacYj0AJ2O5VXEASeIABtkEOtpo8zbgEqLe44VqSKVYZ7siqhWOlbBfN%2FbQEtAbaJ6btw4xy&X-Amz-Signature=923e793ca272e13c7489814e34799364cb8a87c6de9589b2160eedec46b17e2d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RYG2S63%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDq%2FdlmdRkH6d2B%2FuZXUNSkExwyJjJwlcB3%2FdGcHJKa7AIgYxeHm1TU09zl5EYrJPQKuCYko00R%2FowOzunM4zTUAp4qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErGf1aYK9LQ2meTMyrcA8Jq5I%2F7xq0bsKdvVO6uoil2lQDt3QUo5Hj9Cn5QMU8QqbzaKSrVXGF3TjkCR3RDl2qPeW4%2F9pt4I7AgUrN%2BLMqPkMI5kE9giHB5zzDnFfavpyFz8rmvGZZ1Hmknbe8uKitWJyssMsuKvbjwHSsRiSIP7aaGOCXCd7jlXRvqTlz0SHTKhn8VwM3X%2BZsrusLS3FfnxwdAdlJ%2F7LdRaJ%2BHvRw6P47tOexmoT48QeB4%2FpRctVML8gSVBTiN83o0LKnGBg1J72oK8oMJ8hsWy8sd6Rd5Ra%2FlDiZyRrlQc0E5JsxA%2FJwMVOHv28CENnPttQtPKuC8KxNV6yJ%2FBQUQ7pPeQdfYt%2FOpWlQ44D0XAz9dgbZNVZ3CAEZsuP33XSiRinbO31iumSQNHsPdbLtXknJbMsp112Jku35Lnoz2uUknEZmGsBDoUPfCxqCWxzLpdd%2B3HNttCJOyq6wsiyW5I4T4hq7RR9aB2azHk1NikoCHOUGrLlsHspClxn5aTn4J25DxsRiJRgRrtdwBHH5aUNSldYX44KA0QozqxRgQw7kF6RGi088nWUBidqgxXFHthcD2Yio%2B9%2BAq9%2FBMfu8kthrLLCDebFxubUzIOYj%2B%2Bd1pdrg2I%2B8eZm%2FZiRSEbNpVMJq5%2FbwGOqUBJ8FRhHrlWD%2FNAuzSNFR1AMDZCB3hzToskEhAqtvbT9XpmzMDYNTpYhLiDYCKQgV%2F0Gtk8DTqrITNFomjNBILqShMj7TTYHF%2Bnexaj%2FOZHWubz7KgcFsog3BYEuyI%2F7PVOG3iC7%2BBQ7a%2BpCsQkEn1zacYj0AJ2O5VXEASeIABtkEOtpo8zbgEqLe44VqSKVYZ7siqhWOlbBfN%2FbQEtAbaJ6btw4xy&X-Amz-Signature=9a106ba40f27b92d71f3b3151f623d971562afd6b74aeb64966ddbe871564ed4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYIVWQI6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEvmqe3WAJyUy1cy7IhRfLtCli7yXoqX%2FumplurvQrwZAiAevdzDjZipLHF%2BgHbPeV%2B9x4o54WbXKmKC%2FgCKsxjOwyqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgV6Eb0KRGiq6wTO3KtwD88swBs5uVyDhNjvYK0ZDlP41EWYqAjPyoTZEtd6JuBhYo1KOotLlDxUCp2zerwr03aarep27557qns1JHZXdZqYcAIR7LWttQVnDXrxUYx2Cj7St0jKqK3BCziz%2FJlRGniWjtn3Z4SOQbVV4mdKK2lyaeg67vtpYgtnw3k41jSdbj410Q3jmTthZzR4DMzOCJTmHXzkzuJKcR3mnSLAhWJ1SrnBD8PvPbwKQj5CzhdD%2B5o%2BLMRvkttJ1oTwaanfIzu%2FVGcIYF%2FB11Hgs70%2Bhb6ylWtnQcDKyO3RhoS57YDkz5vvb2zK%2BLMLPjX1BLg8uDj%2FGCf0POdkOwikFlMbevE1Zw8GCIWhczdGsCZjJ3E2Bnwo%2Bm%2FAq88igQBxICIwo54s8yJvBVweKOZLCo5tO1%2FMaYdJSiO8%2B3gmxsPzODLY5J12K6wC5%2Fd2nwM4T%2BKRWl17BpRHIAqbC5BAC5pPjDSOL0QUrlifxEARV7ntgyZk8vFLukoBVRdVz6wl6DMPGtzF6XvOdQlvi6iP%2FC7nSEylYi30%2BWIjReDc2xU0gWBdBTpfy9z4sXy3wsT3Y3JwMHd%2F0aYKWqgoCiT5gG56WeEyXhl9fDaAOFWyMjJtIGyNROk7Gqp%2ByHjPma2Aw0779vAY6pgGNCoOaGB7l8E4zav3yAA3DzHHuv4pzGLR1r24GeKnP8TcR2bmju9V7WLl4oWzR3nV3NwyZ7%2F2%2F7TgOEME7%2Bi0YeJLuLp0gDwgbyqKck2OgA%2BEgwg7cQ9IcAQEi68z9hYE9QCEo3eBla81QYLZJ%2FnLBsYZnOApJA8X8t5XRxfVM3iNeCpMWIuBtGhvGzVckN%2FcLDFLKslOh5QcxrSS6%2BID4ykCc8q0W&X-Amz-Signature=1ab2c785fed4e6044ebadc4328147e43a86c57ace7f424157945078eb331f7c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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