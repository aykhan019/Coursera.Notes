

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZOTKCF2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn7xCzpMj%2FeLWiiT7xFWaM6wnpsCpexilqTAm4%2B%2BvlYQIgZ5Dk%2FMG2xwf4QIrnDzamUITp9dR3PgRt%2BXnp9aOe0CAqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBB4g3z%2FyLEVLTuAMyrcA%2BBY68tbacQ2DpzD4M%2BK4VDAawqlh31%2FCdXddW%2FkS1mOP1dr8BANpVDZoERJyeVs%2FwHXE84t944Bh9oi1H%2FTuWr3JO%2FDAvaK3mHV8lZlVmQt%2FBqO9pNgyWVU5xMXa0MzenV9chRS%2FEIW3MUGMgNY4D60JMhrKIjvRhJ8irqNukCHYB2IvZGelc9niqvNUyUVkDT%2BDFDmeW37Yod2HA%2FIRy4PQ4Lskw96NP2Ey1QK0rMwWzlrkEDc4u4x5QwzsNapvGgZXjJ%2FfKVmlPdnEWzAaXmDXMg6q%2FaUqlv0z0NveO7V4XdDEmvcVpLGrDoMyIY5SeV0%2F76HuVSQ6Y8NUN9%2BVFupXHbJqFXM4Dq0FDZv4U3ewK348v9gMFBdA%2FFcONtaklB7h1MIZ8DHwh1%2FO%2BXtS3x1Xw7av1FWJuh7T2Huaf8ucimayXvRGa%2BpVdssD7R1gkkxJRY2eBkQTqEFPgBQucHazWcWkOxLRndu3c%2BrlO0OTU28eMPqrfWgY0fCOR3QRbM5F861NaXep%2F8AfcxU38VPzgBZ69MqddfEvaR97lqBCBXkIx7IQYNQHeBL897fNNXv1pNEFI67GCJU%2BiDrqa3WkEi%2BT7uUBIsAUpED95L5MIO10Sc6%2F6H3JOsWMJLT%2FrwGOqUBodgNFEHil5YsXT5HVTyj6iCzhOaORUpfbYpG4%2FGe%2FqDzWn4aMCvQPgGZBg8bkxW422wwOZJipqWBZRN%2FW1Z8AThPpTxV%2FPJSQOGBNH2hvsUTp3HTRwo2k2qvbKpwJQn%2BgQK1dNYSkRUWKu410FORV8cZraE56MfM6r9ml79R%2BKCOgKE0%2F%2BTQbB4kgV7Pfgy4hzPuHGqU%2B9kxpuWqwyA7%2BPImvSIq&X-Amz-Signature=b755dd4333b821c401f7c412eb6c64a5ac91cc4c948ff3c3b9ac0427e084e0ac&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZOTKCF2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn7xCzpMj%2FeLWiiT7xFWaM6wnpsCpexilqTAm4%2B%2BvlYQIgZ5Dk%2FMG2xwf4QIrnDzamUITp9dR3PgRt%2BXnp9aOe0CAqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBB4g3z%2FyLEVLTuAMyrcA%2BBY68tbacQ2DpzD4M%2BK4VDAawqlh31%2FCdXddW%2FkS1mOP1dr8BANpVDZoERJyeVs%2FwHXE84t944Bh9oi1H%2FTuWr3JO%2FDAvaK3mHV8lZlVmQt%2FBqO9pNgyWVU5xMXa0MzenV9chRS%2FEIW3MUGMgNY4D60JMhrKIjvRhJ8irqNukCHYB2IvZGelc9niqvNUyUVkDT%2BDFDmeW37Yod2HA%2FIRy4PQ4Lskw96NP2Ey1QK0rMwWzlrkEDc4u4x5QwzsNapvGgZXjJ%2FfKVmlPdnEWzAaXmDXMg6q%2FaUqlv0z0NveO7V4XdDEmvcVpLGrDoMyIY5SeV0%2F76HuVSQ6Y8NUN9%2BVFupXHbJqFXM4Dq0FDZv4U3ewK348v9gMFBdA%2FFcONtaklB7h1MIZ8DHwh1%2FO%2BXtS3x1Xw7av1FWJuh7T2Huaf8ucimayXvRGa%2BpVdssD7R1gkkxJRY2eBkQTqEFPgBQucHazWcWkOxLRndu3c%2BrlO0OTU28eMPqrfWgY0fCOR3QRbM5F861NaXep%2F8AfcxU38VPzgBZ69MqddfEvaR97lqBCBXkIx7IQYNQHeBL897fNNXv1pNEFI67GCJU%2BiDrqa3WkEi%2BT7uUBIsAUpED95L5MIO10Sc6%2F6H3JOsWMJLT%2FrwGOqUBodgNFEHil5YsXT5HVTyj6iCzhOaORUpfbYpG4%2FGe%2FqDzWn4aMCvQPgGZBg8bkxW422wwOZJipqWBZRN%2FW1Z8AThPpTxV%2FPJSQOGBNH2hvsUTp3HTRwo2k2qvbKpwJQn%2BgQK1dNYSkRUWKu410FORV8cZraE56MfM6r9ml79R%2BKCOgKE0%2F%2BTQbB4kgV7Pfgy4hzPuHGqU%2B9kxpuWqwyA7%2BPImvSIq&X-Amz-Signature=971e5d43f6a2b97dd4c2fd7c3fabc77e5cff44648cdd9a18146a6de5e0832aff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZOTKCF2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn7xCzpMj%2FeLWiiT7xFWaM6wnpsCpexilqTAm4%2B%2BvlYQIgZ5Dk%2FMG2xwf4QIrnDzamUITp9dR3PgRt%2BXnp9aOe0CAqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBB4g3z%2FyLEVLTuAMyrcA%2BBY68tbacQ2DpzD4M%2BK4VDAawqlh31%2FCdXddW%2FkS1mOP1dr8BANpVDZoERJyeVs%2FwHXE84t944Bh9oi1H%2FTuWr3JO%2FDAvaK3mHV8lZlVmQt%2FBqO9pNgyWVU5xMXa0MzenV9chRS%2FEIW3MUGMgNY4D60JMhrKIjvRhJ8irqNukCHYB2IvZGelc9niqvNUyUVkDT%2BDFDmeW37Yod2HA%2FIRy4PQ4Lskw96NP2Ey1QK0rMwWzlrkEDc4u4x5QwzsNapvGgZXjJ%2FfKVmlPdnEWzAaXmDXMg6q%2FaUqlv0z0NveO7V4XdDEmvcVpLGrDoMyIY5SeV0%2F76HuVSQ6Y8NUN9%2BVFupXHbJqFXM4Dq0FDZv4U3ewK348v9gMFBdA%2FFcONtaklB7h1MIZ8DHwh1%2FO%2BXtS3x1Xw7av1FWJuh7T2Huaf8ucimayXvRGa%2BpVdssD7R1gkkxJRY2eBkQTqEFPgBQucHazWcWkOxLRndu3c%2BrlO0OTU28eMPqrfWgY0fCOR3QRbM5F861NaXep%2F8AfcxU38VPzgBZ69MqddfEvaR97lqBCBXkIx7IQYNQHeBL897fNNXv1pNEFI67GCJU%2BiDrqa3WkEi%2BT7uUBIsAUpED95L5MIO10Sc6%2F6H3JOsWMJLT%2FrwGOqUBodgNFEHil5YsXT5HVTyj6iCzhOaORUpfbYpG4%2FGe%2FqDzWn4aMCvQPgGZBg8bkxW422wwOZJipqWBZRN%2FW1Z8AThPpTxV%2FPJSQOGBNH2hvsUTp3HTRwo2k2qvbKpwJQn%2BgQK1dNYSkRUWKu410FORV8cZraE56MfM6r9ml79R%2BKCOgKE0%2F%2BTQbB4kgV7Pfgy4hzPuHGqU%2B9kxpuWqwyA7%2BPImvSIq&X-Amz-Signature=8ec2b6a2f48c096af31173a9bf1f7b54b78826d56f267df864f7bf561664895b&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFT5XLMB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCS%2FU4J4HgGRz090KzYOZEYxpCugXtQhjlpuZICvxZmHwIgf3%2B4lqpeRX%2FRbunFfLofeAVfxYXsdu7Wv6HzhKMdXl8qiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKhjTtZy71SHjfM8OircA1nu%2BT5sYAIJ%2F3t5Y7WHmFQVmxJwqaU5%2BgCna6%2FD2nYHu7Nng3XvcVHgqG9CxL68dQ0iI9x%2BWkmD2A9Q2USdpJjj6uJ1hCOGKvPRX58Yz7tSy4xqx6Vb39di5BYVBC4W3Kgs2NaSuoSMipZNNQxk7ZrMVOVnoqqkihgPTP%2Bbv%2Bd2WMhuR1DggLrfwnnaJ9F0qXPgJR3xyRx6LcdOFmzMUOl14W%2FjkyAmhB4hTYSdPQ%2FL3ZumO86ZtyM1LarUmCLOdnsHhYQYMHEZSEe3SySP6My3ek1mfNH%2Bt6e3rZX3wDaCipoQ66ht0XoEP2eH87mNtNnYBPjv5TDjYbACVMXRbidQvncE03Kv35spS7ilVOT0G%2FTWKHYkSByn%2BLdfphzvFAM9%2BsQ1OOJBvNV6aVwR6eqEBFJW4%2FcYghc%2BeyiEnzaSk59i4pU20P0AoBcEfvArwVNA%2BIlx%2BMqCA8qZf2QyHI2NshkDjUf2Vq%2Fi8MPOzlvYA5aGrj99EbwFCK2nziEbTEG8to7vz4AM6b9lHSdNecP3k0Ymi1Rcs7McNO3Fw2aYgcyR3K8BsLkN3hPdLA0C5c1h62Euq9CZnldv%2BzlnYdG7Ki7Cbz2N9p%2Fk1BZKIrXqDNrqUYKzD%2BEut2XDMJLT%2FrwGOqUBjHBqNgfNp70r1UG2EVSKCfxz4a5UTPfJCeWjgXXD6YUBLtlzUGQbDMumvtcy28zQBiuSXR68QRJgYTtxDUJu4R9cAvU07%2F1HH%2BkIKxAV78ppSIH%2FjRhDG%2FIUpVwPpf6z%2BGhF1pjrUm1QlXpv0abD5B%2FucZEf%2FjfDQG%2F0si68wfDUbILgUalbsNcKamoL4NGGlEl4ayGC3oyY3drCxVKAmPy9ehl8&X-Amz-Signature=9d1534175278cb3777c91ecc210b8de1a8a6648bc00c8b827f773a767269f822&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFT5XLMB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCS%2FU4J4HgGRz090KzYOZEYxpCugXtQhjlpuZICvxZmHwIgf3%2B4lqpeRX%2FRbunFfLofeAVfxYXsdu7Wv6HzhKMdXl8qiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKhjTtZy71SHjfM8OircA1nu%2BT5sYAIJ%2F3t5Y7WHmFQVmxJwqaU5%2BgCna6%2FD2nYHu7Nng3XvcVHgqG9CxL68dQ0iI9x%2BWkmD2A9Q2USdpJjj6uJ1hCOGKvPRX58Yz7tSy4xqx6Vb39di5BYVBC4W3Kgs2NaSuoSMipZNNQxk7ZrMVOVnoqqkihgPTP%2Bbv%2Bd2WMhuR1DggLrfwnnaJ9F0qXPgJR3xyRx6LcdOFmzMUOl14W%2FjkyAmhB4hTYSdPQ%2FL3ZumO86ZtyM1LarUmCLOdnsHhYQYMHEZSEe3SySP6My3ek1mfNH%2Bt6e3rZX3wDaCipoQ66ht0XoEP2eH87mNtNnYBPjv5TDjYbACVMXRbidQvncE03Kv35spS7ilVOT0G%2FTWKHYkSByn%2BLdfphzvFAM9%2BsQ1OOJBvNV6aVwR6eqEBFJW4%2FcYghc%2BeyiEnzaSk59i4pU20P0AoBcEfvArwVNA%2BIlx%2BMqCA8qZf2QyHI2NshkDjUf2Vq%2Fi8MPOzlvYA5aGrj99EbwFCK2nziEbTEG8to7vz4AM6b9lHSdNecP3k0Ymi1Rcs7McNO3Fw2aYgcyR3K8BsLkN3hPdLA0C5c1h62Euq9CZnldv%2BzlnYdG7Ki7Cbz2N9p%2Fk1BZKIrXqDNrqUYKzD%2BEut2XDMJLT%2FrwGOqUBjHBqNgfNp70r1UG2EVSKCfxz4a5UTPfJCeWjgXXD6YUBLtlzUGQbDMumvtcy28zQBiuSXR68QRJgYTtxDUJu4R9cAvU07%2F1HH%2BkIKxAV78ppSIH%2FjRhDG%2FIUpVwPpf6z%2BGhF1pjrUm1QlXpv0abD5B%2FucZEf%2FjfDQG%2F0si68wfDUbILgUalbsNcKamoL4NGGlEl4ayGC3oyY3drCxVKAmPy9ehl8&X-Amz-Signature=840342203e2d64e5f9e2a42b858f8419cfc84b1c1dfa42eaa1a3df9393e5ad99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZOTKCF2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn7xCzpMj%2FeLWiiT7xFWaM6wnpsCpexilqTAm4%2B%2BvlYQIgZ5Dk%2FMG2xwf4QIrnDzamUITp9dR3PgRt%2BXnp9aOe0CAqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBB4g3z%2FyLEVLTuAMyrcA%2BBY68tbacQ2DpzD4M%2BK4VDAawqlh31%2FCdXddW%2FkS1mOP1dr8BANpVDZoERJyeVs%2FwHXE84t944Bh9oi1H%2FTuWr3JO%2FDAvaK3mHV8lZlVmQt%2FBqO9pNgyWVU5xMXa0MzenV9chRS%2FEIW3MUGMgNY4D60JMhrKIjvRhJ8irqNukCHYB2IvZGelc9niqvNUyUVkDT%2BDFDmeW37Yod2HA%2FIRy4PQ4Lskw96NP2Ey1QK0rMwWzlrkEDc4u4x5QwzsNapvGgZXjJ%2FfKVmlPdnEWzAaXmDXMg6q%2FaUqlv0z0NveO7V4XdDEmvcVpLGrDoMyIY5SeV0%2F76HuVSQ6Y8NUN9%2BVFupXHbJqFXM4Dq0FDZv4U3ewK348v9gMFBdA%2FFcONtaklB7h1MIZ8DHwh1%2FO%2BXtS3x1Xw7av1FWJuh7T2Huaf8ucimayXvRGa%2BpVdssD7R1gkkxJRY2eBkQTqEFPgBQucHazWcWkOxLRndu3c%2BrlO0OTU28eMPqrfWgY0fCOR3QRbM5F861NaXep%2F8AfcxU38VPzgBZ69MqddfEvaR97lqBCBXkIx7IQYNQHeBL897fNNXv1pNEFI67GCJU%2BiDrqa3WkEi%2BT7uUBIsAUpED95L5MIO10Sc6%2F6H3JOsWMJLT%2FrwGOqUBodgNFEHil5YsXT5HVTyj6iCzhOaORUpfbYpG4%2FGe%2FqDzWn4aMCvQPgGZBg8bkxW422wwOZJipqWBZRN%2FW1Z8AThPpTxV%2FPJSQOGBNH2hvsUTp3HTRwo2k2qvbKpwJQn%2BgQK1dNYSkRUWKu410FORV8cZraE56MfM6r9ml79R%2BKCOgKE0%2F%2BTQbB4kgV7Pfgy4hzPuHGqU%2B9kxpuWqwyA7%2BPImvSIq&X-Amz-Signature=6d89c61afc849642d6f0cf7cbe86801c67467f6b688f8296f16747af09988dbe&X-Amz-SignedHeaders=host&x-id=GetObject)
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