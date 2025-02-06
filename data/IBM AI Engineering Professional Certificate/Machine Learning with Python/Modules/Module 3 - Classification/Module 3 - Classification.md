

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRMIM2AJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIHLRn32Dwfxbk27YMnUF%2BiR2VqxGCBqOk5n5yCxaKkYAAiEAjkovMCUioA8rOQHHHy%2B%2Ff6%2BdpzBnZLX9LJgShixkxggq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDK3Oisqi%2Bab5vbmu8CrcA55rd%2FR2DJiZWWIPKExinX%2Bcwe1tJYCVb1QedqGcTsu9RE%2BL2s4lhEHgyHZhUoAtgOY0waGY6e0IkWmqtgWD9DUXcPeeDp2ZE9kLqr92oNwFRuLMsIvi4oH5tQvl7z0hCRowf3pLB%2BppXHpl7W1hxVoaw%2BTxPOmmwJHnfw%2BEP%2F1%2F%2F%2FkWJXY58WbS9Sa1iiGcsY1JbSx8flCzSUfPaRkFKmzIecghJH8JgC1VsvMZ5v1jdaeEFBJ8aM39rgSKJjER8S1An1U4GpQ0cnKjRbghurT%2F7%2BwV7Rl53OAs80sjE4J4hqh%2BHPQbstC2GqdiMb4ylZRmsmWJlxlio9t9SIPD1sxsw17Eoct%2BLfpNFiFU6sqNEBZ%2Fa27kAAF7FQkAHOZum%2B3HNzI44vEtN3m2KnWvI%2FV1Oah9nc14xwg7yq4z9S7JN11OSLpGQHy7Fk8iyE6YoMpA83G9wEgN7%2B6dunu41Dcfy6ahTVlPm%2FIiBl%2BSO6ToJ%2BNY9lOwPjRqP96n%2Bh%2Bvn%2FN2hXD1YB6ncIT4GuEFE5YyWdRd2U9OjhKfTYFdDOLAWcuvKhNoy9AADNPwBImaJrZ7ZMzIf21T7a%2FV3ZIQw0p%2BaOr%2BB9y317fy1%2FUgdz1mYj9rqbonTgZNNAaUMPjDkr0GOqUBUN0m7kq6mwBTBhCEz8VnqsFgSZ%2FXEQLK88PVLTDI1Jwb1Lug6vS0n9EehymV%2FeG%2BB7K6FDEyw4jcZkS0KHPDOTInv%2B4F5iYzYCofBMdU2GrAKK4v4SLKsjQr9ZgWVIF2wFIFE2hs1JwGfeRoIVwKbMqHJbJe3nsk46m%2BTVQdI61D2XUAgkCUMXqpMI6FdJQ1u91qeZf7Ykhla1dz65vTZBwKAMK7&X-Amz-Signature=2b5cabe603ae89bc3cec45ad4057f3b819f96b796a50e6093c795c127f107808&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRMIM2AJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIHLRn32Dwfxbk27YMnUF%2BiR2VqxGCBqOk5n5yCxaKkYAAiEAjkovMCUioA8rOQHHHy%2B%2Ff6%2BdpzBnZLX9LJgShixkxggq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDK3Oisqi%2Bab5vbmu8CrcA55rd%2FR2DJiZWWIPKExinX%2Bcwe1tJYCVb1QedqGcTsu9RE%2BL2s4lhEHgyHZhUoAtgOY0waGY6e0IkWmqtgWD9DUXcPeeDp2ZE9kLqr92oNwFRuLMsIvi4oH5tQvl7z0hCRowf3pLB%2BppXHpl7W1hxVoaw%2BTxPOmmwJHnfw%2BEP%2F1%2F%2F%2FkWJXY58WbS9Sa1iiGcsY1JbSx8flCzSUfPaRkFKmzIecghJH8JgC1VsvMZ5v1jdaeEFBJ8aM39rgSKJjER8S1An1U4GpQ0cnKjRbghurT%2F7%2BwV7Rl53OAs80sjE4J4hqh%2BHPQbstC2GqdiMb4ylZRmsmWJlxlio9t9SIPD1sxsw17Eoct%2BLfpNFiFU6sqNEBZ%2Fa27kAAF7FQkAHOZum%2B3HNzI44vEtN3m2KnWvI%2FV1Oah9nc14xwg7yq4z9S7JN11OSLpGQHy7Fk8iyE6YoMpA83G9wEgN7%2B6dunu41Dcfy6ahTVlPm%2FIiBl%2BSO6ToJ%2BNY9lOwPjRqP96n%2Bh%2Bvn%2FN2hXD1YB6ncIT4GuEFE5YyWdRd2U9OjhKfTYFdDOLAWcuvKhNoy9AADNPwBImaJrZ7ZMzIf21T7a%2FV3ZIQw0p%2BaOr%2BB9y317fy1%2FUgdz1mYj9rqbonTgZNNAaUMPjDkr0GOqUBUN0m7kq6mwBTBhCEz8VnqsFgSZ%2FXEQLK88PVLTDI1Jwb1Lug6vS0n9EehymV%2FeG%2BB7K6FDEyw4jcZkS0KHPDOTInv%2B4F5iYzYCofBMdU2GrAKK4v4SLKsjQr9ZgWVIF2wFIFE2hs1JwGfeRoIVwKbMqHJbJe3nsk46m%2BTVQdI61D2XUAgkCUMXqpMI6FdJQ1u91qeZf7Ykhla1dz65vTZBwKAMK7&X-Amz-Signature=166269ff3789dba3daf2f37b295b2894fe8729a6f6ed02be1fedcb3df3d4c10d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRMIM2AJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIHLRn32Dwfxbk27YMnUF%2BiR2VqxGCBqOk5n5yCxaKkYAAiEAjkovMCUioA8rOQHHHy%2B%2Ff6%2BdpzBnZLX9LJgShixkxggq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDK3Oisqi%2Bab5vbmu8CrcA55rd%2FR2DJiZWWIPKExinX%2Bcwe1tJYCVb1QedqGcTsu9RE%2BL2s4lhEHgyHZhUoAtgOY0waGY6e0IkWmqtgWD9DUXcPeeDp2ZE9kLqr92oNwFRuLMsIvi4oH5tQvl7z0hCRowf3pLB%2BppXHpl7W1hxVoaw%2BTxPOmmwJHnfw%2BEP%2F1%2F%2F%2FkWJXY58WbS9Sa1iiGcsY1JbSx8flCzSUfPaRkFKmzIecghJH8JgC1VsvMZ5v1jdaeEFBJ8aM39rgSKJjER8S1An1U4GpQ0cnKjRbghurT%2F7%2BwV7Rl53OAs80sjE4J4hqh%2BHPQbstC2GqdiMb4ylZRmsmWJlxlio9t9SIPD1sxsw17Eoct%2BLfpNFiFU6sqNEBZ%2Fa27kAAF7FQkAHOZum%2B3HNzI44vEtN3m2KnWvI%2FV1Oah9nc14xwg7yq4z9S7JN11OSLpGQHy7Fk8iyE6YoMpA83G9wEgN7%2B6dunu41Dcfy6ahTVlPm%2FIiBl%2BSO6ToJ%2BNY9lOwPjRqP96n%2Bh%2Bvn%2FN2hXD1YB6ncIT4GuEFE5YyWdRd2U9OjhKfTYFdDOLAWcuvKhNoy9AADNPwBImaJrZ7ZMzIf21T7a%2FV3ZIQw0p%2BaOr%2BB9y317fy1%2FUgdz1mYj9rqbonTgZNNAaUMPjDkr0GOqUBUN0m7kq6mwBTBhCEz8VnqsFgSZ%2FXEQLK88PVLTDI1Jwb1Lug6vS0n9EehymV%2FeG%2BB7K6FDEyw4jcZkS0KHPDOTInv%2B4F5iYzYCofBMdU2GrAKK4v4SLKsjQr9ZgWVIF2wFIFE2hs1JwGfeRoIVwKbMqHJbJe3nsk46m%2BTVQdI61D2XUAgkCUMXqpMI6FdJQ1u91qeZf7Ykhla1dz65vTZBwKAMK7&X-Amz-Signature=89a8ac8c66a8c47d5d5bbedb0df882dfb240d018274b2d2103c80b9d117140ab&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQZ7KD5T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDhwDMQUjv88rzr7TVIloDWQurvpmR8LTraXAJ4oYliagIgd368EhggyzZlWTWUQtBysI4nW3hQSQR6vtaMq62U2Skq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDEdQ9j9B1v7%2FoFMEZyrcA54ounfTCE9wcB5QiIOozVzOpE4a5nJtP00L71HSAuyuo%2BcFPveCsmAm7UPvuPMYahfI4nlBm7CRFPIEXlSiPOcnbFk1OCEZJbr0Di7cjtiuf3TeL4xvVjVWglEN3SqyX0cnb%2BViPSqhcMXHpVth17vD1jcm3%2BjgfjlwoEuKb3Wu1wgSTftq9DwtHZnPLlXuq6EcGeVhQ%2Bra%2BLyAwUL97HszuAocevWmaFeSfcvfI7Jph%2FXVlGRT8kLewCx%2BIHgdiREhnVBXVDBQgPnmN6M02X51dAQb2%2Fb84A0rHuiVBxKiKp0AtGnDcJtni2ifD7Y1PxhNiaNHPGTlZIR04y2Euh5k3HcNNyMIvagFH%2BcuNkTYmc1a4MjZ4QlW4IoET9wcyeAkAT5vVirvyT5qoYbLnvvRpyn75R%2Bf7hs0UiezlzKR%2F3ttF5kZZvWbbHX%2BO5T4SwGQ%2F6mkOGrV%2FMnPYcqWkGGetu4zmiXpZIz69Lwg%2FhDmLa%2FyqBVrSw3H7X%2F9I1Q8Zss98C3PTUu7jwUusntfV9tLcZe6GpBoct3AYIExTO9uFc3Z%2F1alxHMGcCSmM5BGktt28B1TnJvMvO7sJDNBHxtTdt5AOYxCpIMfD1kEvRY%2BWbck%2BrGbu0ghIxjEMKjEkr0GOqUB%2Bfq4LQx67bRHAE%2FhYfiwGmJNNTpSAgDS0pCPXdKO7SgiRUtdVLbwdLaehoYwJ%2FLyDj4Bqkmvp2axt6EuiCF37SMg54lFx9bidLpvlhc02mTcAug%2BTDsXqNriKNtX%2FC8RM659I2dADVkJ4io%2FrOEhFD1Bvpl93UvEKLd9wz%2BUNd5BgfWnMU1FRQSETkXuH0iXYYSZWT0s2tZe6t1mAo%2BWqKNGv8Ma&X-Amz-Signature=62d0e86c6d0abef851d1e0f11412da28caa938b93b13dde8af86c9c34d6050e5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQZ7KD5T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDhwDMQUjv88rzr7TVIloDWQurvpmR8LTraXAJ4oYliagIgd368EhggyzZlWTWUQtBysI4nW3hQSQR6vtaMq62U2Skq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDEdQ9j9B1v7%2FoFMEZyrcA54ounfTCE9wcB5QiIOozVzOpE4a5nJtP00L71HSAuyuo%2BcFPveCsmAm7UPvuPMYahfI4nlBm7CRFPIEXlSiPOcnbFk1OCEZJbr0Di7cjtiuf3TeL4xvVjVWglEN3SqyX0cnb%2BViPSqhcMXHpVth17vD1jcm3%2BjgfjlwoEuKb3Wu1wgSTftq9DwtHZnPLlXuq6EcGeVhQ%2Bra%2BLyAwUL97HszuAocevWmaFeSfcvfI7Jph%2FXVlGRT8kLewCx%2BIHgdiREhnVBXVDBQgPnmN6M02X51dAQb2%2Fb84A0rHuiVBxKiKp0AtGnDcJtni2ifD7Y1PxhNiaNHPGTlZIR04y2Euh5k3HcNNyMIvagFH%2BcuNkTYmc1a4MjZ4QlW4IoET9wcyeAkAT5vVirvyT5qoYbLnvvRpyn75R%2Bf7hs0UiezlzKR%2F3ttF5kZZvWbbHX%2BO5T4SwGQ%2F6mkOGrV%2FMnPYcqWkGGetu4zmiXpZIz69Lwg%2FhDmLa%2FyqBVrSw3H7X%2F9I1Q8Zss98C3PTUu7jwUusntfV9tLcZe6GpBoct3AYIExTO9uFc3Z%2F1alxHMGcCSmM5BGktt28B1TnJvMvO7sJDNBHxtTdt5AOYxCpIMfD1kEvRY%2BWbck%2BrGbu0ghIxjEMKjEkr0GOqUB%2Bfq4LQx67bRHAE%2FhYfiwGmJNNTpSAgDS0pCPXdKO7SgiRUtdVLbwdLaehoYwJ%2FLyDj4Bqkmvp2axt6EuiCF37SMg54lFx9bidLpvlhc02mTcAug%2BTDsXqNriKNtX%2FC8RM659I2dADVkJ4io%2FrOEhFD1Bvpl93UvEKLd9wz%2BUNd5BgfWnMU1FRQSETkXuH0iXYYSZWT0s2tZe6t1mAo%2BWqKNGv8Ma&X-Amz-Signature=a9d129c75aff1482fea0b5a493029a5958da94725b218fc1a63d32487f1ddc11&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRMIM2AJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIHLRn32Dwfxbk27YMnUF%2BiR2VqxGCBqOk5n5yCxaKkYAAiEAjkovMCUioA8rOQHHHy%2B%2Ff6%2BdpzBnZLX9LJgShixkxggq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDK3Oisqi%2Bab5vbmu8CrcA55rd%2FR2DJiZWWIPKExinX%2Bcwe1tJYCVb1QedqGcTsu9RE%2BL2s4lhEHgyHZhUoAtgOY0waGY6e0IkWmqtgWD9DUXcPeeDp2ZE9kLqr92oNwFRuLMsIvi4oH5tQvl7z0hCRowf3pLB%2BppXHpl7W1hxVoaw%2BTxPOmmwJHnfw%2BEP%2F1%2F%2F%2FkWJXY58WbS9Sa1iiGcsY1JbSx8flCzSUfPaRkFKmzIecghJH8JgC1VsvMZ5v1jdaeEFBJ8aM39rgSKJjER8S1An1U4GpQ0cnKjRbghurT%2F7%2BwV7Rl53OAs80sjE4J4hqh%2BHPQbstC2GqdiMb4ylZRmsmWJlxlio9t9SIPD1sxsw17Eoct%2BLfpNFiFU6sqNEBZ%2Fa27kAAF7FQkAHOZum%2B3HNzI44vEtN3m2KnWvI%2FV1Oah9nc14xwg7yq4z9S7JN11OSLpGQHy7Fk8iyE6YoMpA83G9wEgN7%2B6dunu41Dcfy6ahTVlPm%2FIiBl%2BSO6ToJ%2BNY9lOwPjRqP96n%2Bh%2Bvn%2FN2hXD1YB6ncIT4GuEFE5YyWdRd2U9OjhKfTYFdDOLAWcuvKhNoy9AADNPwBImaJrZ7ZMzIf21T7a%2FV3ZIQw0p%2BaOr%2BB9y317fy1%2FUgdz1mYj9rqbonTgZNNAaUMPjDkr0GOqUBUN0m7kq6mwBTBhCEz8VnqsFgSZ%2FXEQLK88PVLTDI1Jwb1Lug6vS0n9EehymV%2FeG%2BB7K6FDEyw4jcZkS0KHPDOTInv%2B4F5iYzYCofBMdU2GrAKK4v4SLKsjQr9ZgWVIF2wFIFE2hs1JwGfeRoIVwKbMqHJbJe3nsk46m%2BTVQdI61D2XUAgkCUMXqpMI6FdJQ1u91qeZf7Ykhla1dz65vTZBwKAMK7&X-Amz-Signature=f6fc52d776a3545c3db674430f28ac40689eb51e72651a3c8ca3cf9ce653c918&X-Amz-SignedHeaders=host&x-id=GetObject)
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