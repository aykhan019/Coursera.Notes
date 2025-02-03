

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5ZFBWZD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIOiqKmirwhaWU7Xn%2F4onEeXCCYADH7QioauY50XcKIAIhAO36wX5Xl3N7BRuo%2Bsc3Jpv2FUCroSi1ksL0Bz1KVljMKv8DCBYQABoMNjM3NDIzMTgzODA1IgzcglmxkcAbv9p72f4q3AOEKBf9Wbk4BCaty7dgVAWKUel0wTUFt%2FVd0%2Blo67MDiq6rnMYMowL4YocGAbuszwrWJ81mBnm3KxGgPqQKhRlzoKBxPXKLIXeDg%2Fqv9ACFgDnKblEMwViqZXzPLuEnLHZhsOHENzm9t9KCYPVhr7y8emVttiPzZAu%2BE6gw9mEkrGjOs5L8rP6J04D3cbkVQL5KbKFfOV%2FJ6q2gOXkfLshxvrl%2FU76ucdL8Ypid1RpJvpITVmrvQ0trl3OSMKxUwerj1cwADMdgS7uJ4kEmK3yHs6Ud7x4W3jZ%2FVx4dl7ROCvitkKKVNClqE8v2i08wboql0qDmHJTqzE3IKPtW%2Fxcnk5bHcLsnkhhm%2BMoZY6h8%2BsUYKK5xJOasyLQ3QIkAcMNXkMnL0rkjjduRJeDOK4axWRwLEJlQrOYd68vfn9EJd6UexOmYR%2BfM%2FA4pencKeIpUd4QAZPdx%2FvzKBEkiJWzHCL%2FA%2Bj0v8NL7T%2BKs3wTF9z8Uh1QTiqRpjrPgfwUze97QpDvyHwX%2BHnV%2Fsw7%2FUjoZKzNnBxdeRwPa1lFGync1FKH4n7zxRj7MaXr97feU6KMTNovQDPSOWpvr%2FIyz5E5g8gV%2FAJDqEzOOHs075RxPGVRZkYQUUaTZDxdVXjCb8YK9BjqkASRhz486QICKYZDy1Tf6nSsPtjmAUn5HvBVakhsAvZVPumChseGT5e7Ohk7rqz7hrDNvzqS4VJKK4UyOLZHAAfu9LZHKdas64Le%2BkwBEWa%2FRoHEYhOwe%2FqjtNctmhHkQ9vOYmTsNFxDgotuf%2BumoPbRHAWJ8XsYlaR7G0PRRZiKIuQm%2B0snOwQnSXiA2ZyaLry8jhc00WMzhNmRvHt%2FEjgJ%2Fp6e6&X-Amz-Signature=e097f41d0a156fd7c8b3b043f4e38a900ef31ff4a4352775ee06d54c8179c86c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5ZFBWZD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIOiqKmirwhaWU7Xn%2F4onEeXCCYADH7QioauY50XcKIAIhAO36wX5Xl3N7BRuo%2Bsc3Jpv2FUCroSi1ksL0Bz1KVljMKv8DCBYQABoMNjM3NDIzMTgzODA1IgzcglmxkcAbv9p72f4q3AOEKBf9Wbk4BCaty7dgVAWKUel0wTUFt%2FVd0%2Blo67MDiq6rnMYMowL4YocGAbuszwrWJ81mBnm3KxGgPqQKhRlzoKBxPXKLIXeDg%2Fqv9ACFgDnKblEMwViqZXzPLuEnLHZhsOHENzm9t9KCYPVhr7y8emVttiPzZAu%2BE6gw9mEkrGjOs5L8rP6J04D3cbkVQL5KbKFfOV%2FJ6q2gOXkfLshxvrl%2FU76ucdL8Ypid1RpJvpITVmrvQ0trl3OSMKxUwerj1cwADMdgS7uJ4kEmK3yHs6Ud7x4W3jZ%2FVx4dl7ROCvitkKKVNClqE8v2i08wboql0qDmHJTqzE3IKPtW%2Fxcnk5bHcLsnkhhm%2BMoZY6h8%2BsUYKK5xJOasyLQ3QIkAcMNXkMnL0rkjjduRJeDOK4axWRwLEJlQrOYd68vfn9EJd6UexOmYR%2BfM%2FA4pencKeIpUd4QAZPdx%2FvzKBEkiJWzHCL%2FA%2Bj0v8NL7T%2BKs3wTF9z8Uh1QTiqRpjrPgfwUze97QpDvyHwX%2BHnV%2Fsw7%2FUjoZKzNnBxdeRwPa1lFGync1FKH4n7zxRj7MaXr97feU6KMTNovQDPSOWpvr%2FIyz5E5g8gV%2FAJDqEzOOHs075RxPGVRZkYQUUaTZDxdVXjCb8YK9BjqkASRhz486QICKYZDy1Tf6nSsPtjmAUn5HvBVakhsAvZVPumChseGT5e7Ohk7rqz7hrDNvzqS4VJKK4UyOLZHAAfu9LZHKdas64Le%2BkwBEWa%2FRoHEYhOwe%2FqjtNctmhHkQ9vOYmTsNFxDgotuf%2BumoPbRHAWJ8XsYlaR7G0PRRZiKIuQm%2B0snOwQnSXiA2ZyaLry8jhc00WMzhNmRvHt%2FEjgJ%2Fp6e6&X-Amz-Signature=6568ff4265c535f9a9d9485a5c6c72ddc5c89aaeb2ba291534de1f30c393631b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5ZFBWZD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIOiqKmirwhaWU7Xn%2F4onEeXCCYADH7QioauY50XcKIAIhAO36wX5Xl3N7BRuo%2Bsc3Jpv2FUCroSi1ksL0Bz1KVljMKv8DCBYQABoMNjM3NDIzMTgzODA1IgzcglmxkcAbv9p72f4q3AOEKBf9Wbk4BCaty7dgVAWKUel0wTUFt%2FVd0%2Blo67MDiq6rnMYMowL4YocGAbuszwrWJ81mBnm3KxGgPqQKhRlzoKBxPXKLIXeDg%2Fqv9ACFgDnKblEMwViqZXzPLuEnLHZhsOHENzm9t9KCYPVhr7y8emVttiPzZAu%2BE6gw9mEkrGjOs5L8rP6J04D3cbkVQL5KbKFfOV%2FJ6q2gOXkfLshxvrl%2FU76ucdL8Ypid1RpJvpITVmrvQ0trl3OSMKxUwerj1cwADMdgS7uJ4kEmK3yHs6Ud7x4W3jZ%2FVx4dl7ROCvitkKKVNClqE8v2i08wboql0qDmHJTqzE3IKPtW%2Fxcnk5bHcLsnkhhm%2BMoZY6h8%2BsUYKK5xJOasyLQ3QIkAcMNXkMnL0rkjjduRJeDOK4axWRwLEJlQrOYd68vfn9EJd6UexOmYR%2BfM%2FA4pencKeIpUd4QAZPdx%2FvzKBEkiJWzHCL%2FA%2Bj0v8NL7T%2BKs3wTF9z8Uh1QTiqRpjrPgfwUze97QpDvyHwX%2BHnV%2Fsw7%2FUjoZKzNnBxdeRwPa1lFGync1FKH4n7zxRj7MaXr97feU6KMTNovQDPSOWpvr%2FIyz5E5g8gV%2FAJDqEzOOHs075RxPGVRZkYQUUaTZDxdVXjCb8YK9BjqkASRhz486QICKYZDy1Tf6nSsPtjmAUn5HvBVakhsAvZVPumChseGT5e7Ohk7rqz7hrDNvzqS4VJKK4UyOLZHAAfu9LZHKdas64Le%2BkwBEWa%2FRoHEYhOwe%2FqjtNctmhHkQ9vOYmTsNFxDgotuf%2BumoPbRHAWJ8XsYlaR7G0PRRZiKIuQm%2B0snOwQnSXiA2ZyaLry8jhc00WMzhNmRvHt%2FEjgJ%2Fp6e6&X-Amz-Signature=78a23e012d3e5cae0803f167ae28140d8d790025a96f5b426f189b09b52f182f&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622Y274VB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDl5%2BtaNDKk%2FGA3UKc0jQpud9cEKA6agt5qpklkdMytWAiAQrp52%2BgOfjhllIf07L09vEpX6%2B3wOlcbecw44%2B0XTXSr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMbuLBapEqstvigg%2BiKtwDg30Pslpeo2oulJsb%2FKbl4CaobzU00VdIESvtZoBSXcdFXqRimPzv8rOTmOnOs%2BGyHf7D14WAMoqGU1ypBxmGetxHUzl4FrPX%2B9llt121J26xO7e%2BeQbfXj%2BdM9tY2J39LGasQ2Xji%2Fg%2BzxuTp%2FBknSr0EfRbq%2FUX4xKAgSGq7xAAX17FmCkrmH6mGZGetc5SRKGazbJy54y377n2oAe%2BymQ4ze3Y2cy8qa4HFxc0Kh0EAtEzpgktLlKUfP2SmfDRh3nBaAD7UJJWuZWTeAWpXv9mKvbZzblR0bsxaU6t1vh8nejpYQv3KuJJPKSc9iOYgrEK2DbCPoYQUXWxT2rfTx2I1H12ulA227m4NY73wQRdnkxZjmxoVCTtI8lr0aGKfZmGLUelWjAqIB5INvYwFr35TPeFskgqzMddXsPGIlyly2mV1RP%2BaVNenKEXuex5o4FuM0KwEtqKmH9wguwjHsKxFg5FWmkL4adyaoHprAHF%2Bdwx9i2p1eIxvRP7%2BeLwMxcnNmJZti9uhcW8BzzegajFNIqyBSPJfVWuBGNCc%2Fw7KwfmGjfVcCLsJBpP%2FZREiQ7Sjhk3JRCtGZyNWQjR9fkrtaDSVoQKRbfrtLaJSzAmaB6YEX9aHA5eSwMwofGCvQY6pgG4lbnpy%2Fjqyr5%2F7aqrp1A2Wupvkp3kEMWYsjNPVWmybtGddDQCRO4bBUJgGamZ5tr5vMf4BH%2BUFZaawjdHaYgWIdEi1M2I%2BOPmIRCfkhGJqufEpHX7gv6QeJLzoBr4mkQbrYfOuJIQ9J2JangGwNA0wi82U%2BkQ0NQJf8dSfwTHMComZKtEGGBhQUwbEFkWCreR07hxGzv5qmSchC680KLd6GVC%2Ffew&X-Amz-Signature=99e221c50bf570240d4a08fe8fb5b03307490cee678b12833774e7bc26e19553&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622Y274VB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDl5%2BtaNDKk%2FGA3UKc0jQpud9cEKA6agt5qpklkdMytWAiAQrp52%2BgOfjhllIf07L09vEpX6%2B3wOlcbecw44%2B0XTXSr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMbuLBapEqstvigg%2BiKtwDg30Pslpeo2oulJsb%2FKbl4CaobzU00VdIESvtZoBSXcdFXqRimPzv8rOTmOnOs%2BGyHf7D14WAMoqGU1ypBxmGetxHUzl4FrPX%2B9llt121J26xO7e%2BeQbfXj%2BdM9tY2J39LGasQ2Xji%2Fg%2BzxuTp%2FBknSr0EfRbq%2FUX4xKAgSGq7xAAX17FmCkrmH6mGZGetc5SRKGazbJy54y377n2oAe%2BymQ4ze3Y2cy8qa4HFxc0Kh0EAtEzpgktLlKUfP2SmfDRh3nBaAD7UJJWuZWTeAWpXv9mKvbZzblR0bsxaU6t1vh8nejpYQv3KuJJPKSc9iOYgrEK2DbCPoYQUXWxT2rfTx2I1H12ulA227m4NY73wQRdnkxZjmxoVCTtI8lr0aGKfZmGLUelWjAqIB5INvYwFr35TPeFskgqzMddXsPGIlyly2mV1RP%2BaVNenKEXuex5o4FuM0KwEtqKmH9wguwjHsKxFg5FWmkL4adyaoHprAHF%2Bdwx9i2p1eIxvRP7%2BeLwMxcnNmJZti9uhcW8BzzegajFNIqyBSPJfVWuBGNCc%2Fw7KwfmGjfVcCLsJBpP%2FZREiQ7Sjhk3JRCtGZyNWQjR9fkrtaDSVoQKRbfrtLaJSzAmaB6YEX9aHA5eSwMwofGCvQY6pgG4lbnpy%2Fjqyr5%2F7aqrp1A2Wupvkp3kEMWYsjNPVWmybtGddDQCRO4bBUJgGamZ5tr5vMf4BH%2BUFZaawjdHaYgWIdEi1M2I%2BOPmIRCfkhGJqufEpHX7gv6QeJLzoBr4mkQbrYfOuJIQ9J2JangGwNA0wi82U%2BkQ0NQJf8dSfwTHMComZKtEGGBhQUwbEFkWCreR07hxGzv5qmSchC680KLd6GVC%2Ffew&X-Amz-Signature=336dbe0ca07592dc3f60ba04850c671decc1168ee03cb84041ef8abfc376c56b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5ZFBWZD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIOiqKmirwhaWU7Xn%2F4onEeXCCYADH7QioauY50XcKIAIhAO36wX5Xl3N7BRuo%2Bsc3Jpv2FUCroSi1ksL0Bz1KVljMKv8DCBYQABoMNjM3NDIzMTgzODA1IgzcglmxkcAbv9p72f4q3AOEKBf9Wbk4BCaty7dgVAWKUel0wTUFt%2FVd0%2Blo67MDiq6rnMYMowL4YocGAbuszwrWJ81mBnm3KxGgPqQKhRlzoKBxPXKLIXeDg%2Fqv9ACFgDnKblEMwViqZXzPLuEnLHZhsOHENzm9t9KCYPVhr7y8emVttiPzZAu%2BE6gw9mEkrGjOs5L8rP6J04D3cbkVQL5KbKFfOV%2FJ6q2gOXkfLshxvrl%2FU76ucdL8Ypid1RpJvpITVmrvQ0trl3OSMKxUwerj1cwADMdgS7uJ4kEmK3yHs6Ud7x4W3jZ%2FVx4dl7ROCvitkKKVNClqE8v2i08wboql0qDmHJTqzE3IKPtW%2Fxcnk5bHcLsnkhhm%2BMoZY6h8%2BsUYKK5xJOasyLQ3QIkAcMNXkMnL0rkjjduRJeDOK4axWRwLEJlQrOYd68vfn9EJd6UexOmYR%2BfM%2FA4pencKeIpUd4QAZPdx%2FvzKBEkiJWzHCL%2FA%2Bj0v8NL7T%2BKs3wTF9z8Uh1QTiqRpjrPgfwUze97QpDvyHwX%2BHnV%2Fsw7%2FUjoZKzNnBxdeRwPa1lFGync1FKH4n7zxRj7MaXr97feU6KMTNovQDPSOWpvr%2FIyz5E5g8gV%2FAJDqEzOOHs075RxPGVRZkYQUUaTZDxdVXjCb8YK9BjqkASRhz486QICKYZDy1Tf6nSsPtjmAUn5HvBVakhsAvZVPumChseGT5e7Ohk7rqz7hrDNvzqS4VJKK4UyOLZHAAfu9LZHKdas64Le%2BkwBEWa%2FRoHEYhOwe%2FqjtNctmhHkQ9vOYmTsNFxDgotuf%2BumoPbRHAWJ8XsYlaR7G0PRRZiKIuQm%2B0snOwQnSXiA2ZyaLry8jhc00WMzhNmRvHt%2FEjgJ%2Fp6e6&X-Amz-Signature=3ea3148c9cbb0512a63da7f95961ebb15f702dd85c5af0bc56f4c4be7d66fc36&X-Amz-SignedHeaders=host&x-id=GetObject)
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