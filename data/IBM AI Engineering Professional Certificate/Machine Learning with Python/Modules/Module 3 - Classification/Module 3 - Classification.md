

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC54TV5T%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDv%2FS0EXw8djblRuN3XikQP6sjDXYQgXrXRY727Oh%2FlQAIhAIEy7efUDuepH8WP9H5moVFuxTVgh%2FW79%2BxPC7BFisLcKogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgygnmZxVCJ5zlsQssoq3ANoVsTUu5PDcKnh7eR7qsB80NphYUxlHJPgF3FMMrIbxVPZcA9aC2jBY%2BxOLJQebcmc%2FLqZD%2BbzCEJXfQkWNisMXODO3j21rfufVr4MPoz%2B0%2Fwjt%2FZ6ckWFivcRUZmgKnKGP618E32tkBqTmE7%2FWJmk6KxzKwwvfhjR0e%2BN0RL2zOwDSHug6xElEzH0UWQEY6SI1nL0GGXJdPSmoG5dW0iBCYwDgKqA1q99DX5vpmaKfzxeiQMzJLN2pvAiJbkky2s4IaXg552TyVwp9Bg%2BC5ELuBv7LlNwCLtCdfBoPe3XI52ogJ2zVhMB1PXBm7AbMwSAAif2lGRfBrJ%2Fg2F7ff20vk2AvUMJDcFe3mtNFtBAUoGNgp9E2q7xPq%2B5uKu6zjxebSZYicJmlHrApkzFEk2RnO8A1Bh4j6JWLdTyL4JDSEKWmeqkGSGBCrJ1URqpSkSpNUZEnVqHoqTes02C5dw6wn6a6zIikd8tLEz89Xkgvzg52LCaeqdlUy2UeOFe6pvSKhEw0U5E5CFd20cVA4P3i3rd2ghVCPlZ6FSmDTXWTDfAMnddRwbwzqa0b5ChTEhi2t%2B7yhF%2FA7kOoZygFuqlf%2BhA5%2FAxewnXo%2B6%2FXs5ebVIH1BhgS3THmK73sDC11p%2B9BjqkAZdMqvtPLQvFrsygTcyPou4iqKlQ8tDVKRHn30cWLGW%2BAmVX1k%2B2bvPKPVbOY3%2BbuQ76vgYB1NHJySUVrBfnMBIEUHE9tBrvzyiKbpVvBVhFQC2mhfgVCJ%2FlQ2yfQ4GzhWSSC%2FvMjmKoizWBNmbIsaNqDFmcVaI1t0RyrI46Akfb8BaTW3zGqvBWP6Ui5Z7jP6WDPxCpXaorWGvzM8n1g02GUn%2B0&X-Amz-Signature=9b5e297d0e0a8e1ab61ba4b1370a6c55e2f413de27e59be508d65eddbc91789e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC54TV5T%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDv%2FS0EXw8djblRuN3XikQP6sjDXYQgXrXRY727Oh%2FlQAIhAIEy7efUDuepH8WP9H5moVFuxTVgh%2FW79%2BxPC7BFisLcKogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgygnmZxVCJ5zlsQssoq3ANoVsTUu5PDcKnh7eR7qsB80NphYUxlHJPgF3FMMrIbxVPZcA9aC2jBY%2BxOLJQebcmc%2FLqZD%2BbzCEJXfQkWNisMXODO3j21rfufVr4MPoz%2B0%2Fwjt%2FZ6ckWFivcRUZmgKnKGP618E32tkBqTmE7%2FWJmk6KxzKwwvfhjR0e%2BN0RL2zOwDSHug6xElEzH0UWQEY6SI1nL0GGXJdPSmoG5dW0iBCYwDgKqA1q99DX5vpmaKfzxeiQMzJLN2pvAiJbkky2s4IaXg552TyVwp9Bg%2BC5ELuBv7LlNwCLtCdfBoPe3XI52ogJ2zVhMB1PXBm7AbMwSAAif2lGRfBrJ%2Fg2F7ff20vk2AvUMJDcFe3mtNFtBAUoGNgp9E2q7xPq%2B5uKu6zjxebSZYicJmlHrApkzFEk2RnO8A1Bh4j6JWLdTyL4JDSEKWmeqkGSGBCrJ1URqpSkSpNUZEnVqHoqTes02C5dw6wn6a6zIikd8tLEz89Xkgvzg52LCaeqdlUy2UeOFe6pvSKhEw0U5E5CFd20cVA4P3i3rd2ghVCPlZ6FSmDTXWTDfAMnddRwbwzqa0b5ChTEhi2t%2B7yhF%2FA7kOoZygFuqlf%2BhA5%2FAxewnXo%2B6%2FXs5ebVIH1BhgS3THmK73sDC11p%2B9BjqkAZdMqvtPLQvFrsygTcyPou4iqKlQ8tDVKRHn30cWLGW%2BAmVX1k%2B2bvPKPVbOY3%2BbuQ76vgYB1NHJySUVrBfnMBIEUHE9tBrvzyiKbpVvBVhFQC2mhfgVCJ%2FlQ2yfQ4GzhWSSC%2FvMjmKoizWBNmbIsaNqDFmcVaI1t0RyrI46Akfb8BaTW3zGqvBWP6Ui5Z7jP6WDPxCpXaorWGvzM8n1g02GUn%2B0&X-Amz-Signature=3f6162b2deab314f7bf1996bd2a3bdba5213c97de8421a357e64a68dc60336da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC54TV5T%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDv%2FS0EXw8djblRuN3XikQP6sjDXYQgXrXRY727Oh%2FlQAIhAIEy7efUDuepH8WP9H5moVFuxTVgh%2FW79%2BxPC7BFisLcKogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgygnmZxVCJ5zlsQssoq3ANoVsTUu5PDcKnh7eR7qsB80NphYUxlHJPgF3FMMrIbxVPZcA9aC2jBY%2BxOLJQebcmc%2FLqZD%2BbzCEJXfQkWNisMXODO3j21rfufVr4MPoz%2B0%2Fwjt%2FZ6ckWFivcRUZmgKnKGP618E32tkBqTmE7%2FWJmk6KxzKwwvfhjR0e%2BN0RL2zOwDSHug6xElEzH0UWQEY6SI1nL0GGXJdPSmoG5dW0iBCYwDgKqA1q99DX5vpmaKfzxeiQMzJLN2pvAiJbkky2s4IaXg552TyVwp9Bg%2BC5ELuBv7LlNwCLtCdfBoPe3XI52ogJ2zVhMB1PXBm7AbMwSAAif2lGRfBrJ%2Fg2F7ff20vk2AvUMJDcFe3mtNFtBAUoGNgp9E2q7xPq%2B5uKu6zjxebSZYicJmlHrApkzFEk2RnO8A1Bh4j6JWLdTyL4JDSEKWmeqkGSGBCrJ1URqpSkSpNUZEnVqHoqTes02C5dw6wn6a6zIikd8tLEz89Xkgvzg52LCaeqdlUy2UeOFe6pvSKhEw0U5E5CFd20cVA4P3i3rd2ghVCPlZ6FSmDTXWTDfAMnddRwbwzqa0b5ChTEhi2t%2B7yhF%2FA7kOoZygFuqlf%2BhA5%2FAxewnXo%2B6%2FXs5ebVIH1BhgS3THmK73sDC11p%2B9BjqkAZdMqvtPLQvFrsygTcyPou4iqKlQ8tDVKRHn30cWLGW%2BAmVX1k%2B2bvPKPVbOY3%2BbuQ76vgYB1NHJySUVrBfnMBIEUHE9tBrvzyiKbpVvBVhFQC2mhfgVCJ%2FlQ2yfQ4GzhWSSC%2FvMjmKoizWBNmbIsaNqDFmcVaI1t0RyrI46Akfb8BaTW3zGqvBWP6Ui5Z7jP6WDPxCpXaorWGvzM8n1g02GUn%2B0&X-Amz-Signature=02ef1c5bd9b9bbb896f934ca85a25577e95cbeadc883ba6c44a18d33b67e2dde&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYFK5GZB%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxDtpUaBB59GzAzxxzeBQ0G82YB7L1q50w33euFmBzRQIgWluw8nJ687B%2FbVfbzCE8rWMtOHzV86bfWRjIMutStioqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEwf%2BQbc34ih2ogw2ircA0IjEqcuiFng1XToSenM1sWXCqNg9sa63LfWOR9d5%2B3lTggoKyY%2BPGgBPBzioLozT3NRLRu0MOhnfdndiDc%2BBDzmZo%2B0LztKPIHy60YUvWNsMESGmDWtAlX4qHijEmcUq2g2cx9Yy%2Bmos%2FwAvNTqd76eiZayYiYP0b%2BcpobzqAsgdrMJW4SVyJxWQbRLFKMF2E8DN8FAxX81YPNk8PjAwq7Er79fGe9P5zGDVuLgWQEo5%2F1By9m6mVorRz5KWmilflgRWqnNbpQmaf4XJlovIktY15haSy7tYjgx1EF86iv3YbVznIuebExtB6F0NyqHyAfGEHyTtemTXDFlTASPhsUmjbedkKdgwnFUHjPZKXthQZ2DhPhm1NwIG%2FPkLZZyDRqsO%2FtAPMWu946xZhxK39Inn6bU%2F8Pk1HjdCiIov8ncwovP1qJF6A4oGH0CZNPbMCm3cT%2BD%2BT%2FYmlNO%2FWyq2EovGKPDV5NtnwdM1qddvMGdrT9Yg7xebbQzR3qPskowxP6kngDChpo%2BWnIjkqdd%2FFJVQ%2BuTi41bD%2BiwXXHf0Nc12zaiQj%2Fp6H%2FWVjKL2tHexiauQlXiovsDU74ESDVcD7SoI3hmnWdffLaLkNMoDy7r45edsAZRhlsfU1dNMPPWn70GOqUBniglp6q%2FjJfR361s0xTwtExrSIG4sNzeE0LC%2FSf30v7eOO1RaMpOGg14SDMDyv6lIbhyfPUqJAuPdsVZYwWz%2Fah6S7bLzMbUpeFJd%2B9qDnZomdbGu0iZ5WojYdsgPBOMm9TdGZl4sLcmgbB9TNsQ02w%2Fd50JkgSHUkmyFvJoxA5A3Qxcp9RWKu6%2Buv2Q5MKsNREuIBmBMRkTiQim45TlfXPcIZUS&X-Amz-Signature=aebb2948c3469536e096bd00b60b06130a5280c92f454b517d8df722cd968b5e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYFK5GZB%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxDtpUaBB59GzAzxxzeBQ0G82YB7L1q50w33euFmBzRQIgWluw8nJ687B%2FbVfbzCE8rWMtOHzV86bfWRjIMutStioqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEwf%2BQbc34ih2ogw2ircA0IjEqcuiFng1XToSenM1sWXCqNg9sa63LfWOR9d5%2B3lTggoKyY%2BPGgBPBzioLozT3NRLRu0MOhnfdndiDc%2BBDzmZo%2B0LztKPIHy60YUvWNsMESGmDWtAlX4qHijEmcUq2g2cx9Yy%2Bmos%2FwAvNTqd76eiZayYiYP0b%2BcpobzqAsgdrMJW4SVyJxWQbRLFKMF2E8DN8FAxX81YPNk8PjAwq7Er79fGe9P5zGDVuLgWQEo5%2F1By9m6mVorRz5KWmilflgRWqnNbpQmaf4XJlovIktY15haSy7tYjgx1EF86iv3YbVznIuebExtB6F0NyqHyAfGEHyTtemTXDFlTASPhsUmjbedkKdgwnFUHjPZKXthQZ2DhPhm1NwIG%2FPkLZZyDRqsO%2FtAPMWu946xZhxK39Inn6bU%2F8Pk1HjdCiIov8ncwovP1qJF6A4oGH0CZNPbMCm3cT%2BD%2BT%2FYmlNO%2FWyq2EovGKPDV5NtnwdM1qddvMGdrT9Yg7xebbQzR3qPskowxP6kngDChpo%2BWnIjkqdd%2FFJVQ%2BuTi41bD%2BiwXXHf0Nc12zaiQj%2Fp6H%2FWVjKL2tHexiauQlXiovsDU74ESDVcD7SoI3hmnWdffLaLkNMoDy7r45edsAZRhlsfU1dNMPPWn70GOqUBniglp6q%2FjJfR361s0xTwtExrSIG4sNzeE0LC%2FSf30v7eOO1RaMpOGg14SDMDyv6lIbhyfPUqJAuPdsVZYwWz%2Fah6S7bLzMbUpeFJd%2B9qDnZomdbGu0iZ5WojYdsgPBOMm9TdGZl4sLcmgbB9TNsQ02w%2Fd50JkgSHUkmyFvJoxA5A3Qxcp9RWKu6%2Buv2Q5MKsNREuIBmBMRkTiQim45TlfXPcIZUS&X-Amz-Signature=276e6d9693fe1808a931f6a4450cfe4bcde6744f4c0aea5e398c2ca565bfc529&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC54TV5T%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDv%2FS0EXw8djblRuN3XikQP6sjDXYQgXrXRY727Oh%2FlQAIhAIEy7efUDuepH8WP9H5moVFuxTVgh%2FW79%2BxPC7BFisLcKogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgygnmZxVCJ5zlsQssoq3ANoVsTUu5PDcKnh7eR7qsB80NphYUxlHJPgF3FMMrIbxVPZcA9aC2jBY%2BxOLJQebcmc%2FLqZD%2BbzCEJXfQkWNisMXODO3j21rfufVr4MPoz%2B0%2Fwjt%2FZ6ckWFivcRUZmgKnKGP618E32tkBqTmE7%2FWJmk6KxzKwwvfhjR0e%2BN0RL2zOwDSHug6xElEzH0UWQEY6SI1nL0GGXJdPSmoG5dW0iBCYwDgKqA1q99DX5vpmaKfzxeiQMzJLN2pvAiJbkky2s4IaXg552TyVwp9Bg%2BC5ELuBv7LlNwCLtCdfBoPe3XI52ogJ2zVhMB1PXBm7AbMwSAAif2lGRfBrJ%2Fg2F7ff20vk2AvUMJDcFe3mtNFtBAUoGNgp9E2q7xPq%2B5uKu6zjxebSZYicJmlHrApkzFEk2RnO8A1Bh4j6JWLdTyL4JDSEKWmeqkGSGBCrJ1URqpSkSpNUZEnVqHoqTes02C5dw6wn6a6zIikd8tLEz89Xkgvzg52LCaeqdlUy2UeOFe6pvSKhEw0U5E5CFd20cVA4P3i3rd2ghVCPlZ6FSmDTXWTDfAMnddRwbwzqa0b5ChTEhi2t%2B7yhF%2FA7kOoZygFuqlf%2BhA5%2FAxewnXo%2B6%2FXs5ebVIH1BhgS3THmK73sDC11p%2B9BjqkAZdMqvtPLQvFrsygTcyPou4iqKlQ8tDVKRHn30cWLGW%2BAmVX1k%2B2bvPKPVbOY3%2BbuQ76vgYB1NHJySUVrBfnMBIEUHE9tBrvzyiKbpVvBVhFQC2mhfgVCJ%2FlQ2yfQ4GzhWSSC%2FvMjmKoizWBNmbIsaNqDFmcVaI1t0RyrI46Akfb8BaTW3zGqvBWP6Ui5Z7jP6WDPxCpXaorWGvzM8n1g02GUn%2B0&X-Amz-Signature=0dc9efa89be64f724b619d6d63f1c70c3e7318a3256d9647413a3783cde93b84&X-Amz-SignedHeaders=host&x-id=GetObject)
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