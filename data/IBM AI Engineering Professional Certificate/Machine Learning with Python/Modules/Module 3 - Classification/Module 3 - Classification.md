

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZQW6HOW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIA%2B2qYic4YH%2FHrSjZhI0OeOZ08W%2FJ6JcQz4oqsQUApc5AiAe1uJC4PLG7MVH614w0OwpMNbumFnqAdmRdGi37IyUNir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMLjBk9cVl%2Bc0pFQPxKtwDGhcsbcQw6CctxVvXCqrx5t9fwZcRcCpnHyHbFTZNWzKwBK1YYqu5v69DZ0GWGzwUzwaKyKXmp5NDDNVeju67o%2BU9iU6MYjiJhud2EtfAsbGbe0OZgULZDFahV5HMQn1gOdqxijY%2BO0KXgAQyjT7vQiqLkMl13Zrm7xu%2F1X2n09XJGeZpa0pApLUqGlKKmzlPpdW30ws58skVCz5n6A6xLW8t22usdNn7bhyDbO7Gon11VcHUzn1dm%2BichGJ0pN3VWwVUHBkM4AUf9XW2U%2BQLCy8W6MIOlkNhFDU9WNk%2BxywVj5PGJA0qgqnRk%2BlRbPm3JTaXy%2FMi6j8%2FJERPgwiZqCZi%2B9lMTQnODzIAs2UT4tp58B8kt2YQmu8Zmrokg5tsH0kZAdWzkZldmq%2Ftox5mHt8X6E5jYEMmAFFmPUfaT%2FiYx0a68InFB3xUrNR3c3fmhP8XwJYtBUv%2FhwYfNp86QfoiDNyYchnTY%2FXuoY8qBIi5ma0%2FkGlPcxp9SMpSvIVRh3H7u8QTJOYhZwn02CIkSGucbILJD75mi0Qbr5eIvYljZFX4qniSITJ3nH9gXsVTrDvmS3wEBm87PbbclvtZdab3bXJd4cU1EiodHBbOFsAZICS%2Fa5FugUbT%2BOEw%2FJmZvQY6pgGuipa0Ti3z4lSoc2Ebb2xZDGxatQd5U2CJd5d0juTLGaSiwK1WlZfV6X%2Fv1XoE42IqA2dL8GWOIVgQxGmaSKw0t8cqRR9M9Jmue0GHq02zbqkhHWnLDXTqLbZDHfRmKnAzmlfv0xOOjF%2BTCfJcXwrUi%2FNrsYSGD8M8dPrp12siEGiDa9JfP74GrhzZ9omt6vmz6sLH8y8VDGFBWaKImOvHbWIIYciW&X-Amz-Signature=70670f969a0f4dbc021fd3ab96f1e8adaa887e7a26c06dba17ce737458c09fad&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZQW6HOW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIA%2B2qYic4YH%2FHrSjZhI0OeOZ08W%2FJ6JcQz4oqsQUApc5AiAe1uJC4PLG7MVH614w0OwpMNbumFnqAdmRdGi37IyUNir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMLjBk9cVl%2Bc0pFQPxKtwDGhcsbcQw6CctxVvXCqrx5t9fwZcRcCpnHyHbFTZNWzKwBK1YYqu5v69DZ0GWGzwUzwaKyKXmp5NDDNVeju67o%2BU9iU6MYjiJhud2EtfAsbGbe0OZgULZDFahV5HMQn1gOdqxijY%2BO0KXgAQyjT7vQiqLkMl13Zrm7xu%2F1X2n09XJGeZpa0pApLUqGlKKmzlPpdW30ws58skVCz5n6A6xLW8t22usdNn7bhyDbO7Gon11VcHUzn1dm%2BichGJ0pN3VWwVUHBkM4AUf9XW2U%2BQLCy8W6MIOlkNhFDU9WNk%2BxywVj5PGJA0qgqnRk%2BlRbPm3JTaXy%2FMi6j8%2FJERPgwiZqCZi%2B9lMTQnODzIAs2UT4tp58B8kt2YQmu8Zmrokg5tsH0kZAdWzkZldmq%2Ftox5mHt8X6E5jYEMmAFFmPUfaT%2FiYx0a68InFB3xUrNR3c3fmhP8XwJYtBUv%2FhwYfNp86QfoiDNyYchnTY%2FXuoY8qBIi5ma0%2FkGlPcxp9SMpSvIVRh3H7u8QTJOYhZwn02CIkSGucbILJD75mi0Qbr5eIvYljZFX4qniSITJ3nH9gXsVTrDvmS3wEBm87PbbclvtZdab3bXJd4cU1EiodHBbOFsAZICS%2Fa5FugUbT%2BOEw%2FJmZvQY6pgGuipa0Ti3z4lSoc2Ebb2xZDGxatQd5U2CJd5d0juTLGaSiwK1WlZfV6X%2Fv1XoE42IqA2dL8GWOIVgQxGmaSKw0t8cqRR9M9Jmue0GHq02zbqkhHWnLDXTqLbZDHfRmKnAzmlfv0xOOjF%2BTCfJcXwrUi%2FNrsYSGD8M8dPrp12siEGiDa9JfP74GrhzZ9omt6vmz6sLH8y8VDGFBWaKImOvHbWIIYciW&X-Amz-Signature=e3f107d5240b4840e4b5043f4aace5f58dd689a69ff214b2ddec7ef395b9145c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZQW6HOW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIA%2B2qYic4YH%2FHrSjZhI0OeOZ08W%2FJ6JcQz4oqsQUApc5AiAe1uJC4PLG7MVH614w0OwpMNbumFnqAdmRdGi37IyUNir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMLjBk9cVl%2Bc0pFQPxKtwDGhcsbcQw6CctxVvXCqrx5t9fwZcRcCpnHyHbFTZNWzKwBK1YYqu5v69DZ0GWGzwUzwaKyKXmp5NDDNVeju67o%2BU9iU6MYjiJhud2EtfAsbGbe0OZgULZDFahV5HMQn1gOdqxijY%2BO0KXgAQyjT7vQiqLkMl13Zrm7xu%2F1X2n09XJGeZpa0pApLUqGlKKmzlPpdW30ws58skVCz5n6A6xLW8t22usdNn7bhyDbO7Gon11VcHUzn1dm%2BichGJ0pN3VWwVUHBkM4AUf9XW2U%2BQLCy8W6MIOlkNhFDU9WNk%2BxywVj5PGJA0qgqnRk%2BlRbPm3JTaXy%2FMi6j8%2FJERPgwiZqCZi%2B9lMTQnODzIAs2UT4tp58B8kt2YQmu8Zmrokg5tsH0kZAdWzkZldmq%2Ftox5mHt8X6E5jYEMmAFFmPUfaT%2FiYx0a68InFB3xUrNR3c3fmhP8XwJYtBUv%2FhwYfNp86QfoiDNyYchnTY%2FXuoY8qBIi5ma0%2FkGlPcxp9SMpSvIVRh3H7u8QTJOYhZwn02CIkSGucbILJD75mi0Qbr5eIvYljZFX4qniSITJ3nH9gXsVTrDvmS3wEBm87PbbclvtZdab3bXJd4cU1EiodHBbOFsAZICS%2Fa5FugUbT%2BOEw%2FJmZvQY6pgGuipa0Ti3z4lSoc2Ebb2xZDGxatQd5U2CJd5d0juTLGaSiwK1WlZfV6X%2Fv1XoE42IqA2dL8GWOIVgQxGmaSKw0t8cqRR9M9Jmue0GHq02zbqkhHWnLDXTqLbZDHfRmKnAzmlfv0xOOjF%2BTCfJcXwrUi%2FNrsYSGD8M8dPrp12siEGiDa9JfP74GrhzZ9omt6vmz6sLH8y8VDGFBWaKImOvHbWIIYciW&X-Amz-Signature=4f4257a65ad4d59c89ecaa99fb5078d62e3432c9720a99ab7deb9844ec6a5718&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCFUBMCJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIF3rdQXfefMcPMHxQdJIeqpHr8DnsV9OM0h0GcG9IHmYAiAswJKhDELzMKzRNg1glAvdKNFkC7yRRE6coFsO%2FM7O4yr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMnoLeVHTKFVRmdnVjKtwDhL9mFILdk2S388eBpJ6xZVrIZUR3TgHLgKoWF9iS8ZURSJWkOcKxFcU3DyPVAmKgRIHyg9%2FciRboGCcDfiwC8avbCOMSzUZdnYA48qd9UcmINinue2%2Bg8%2B6o4IzSTSX54bWJAE2zMhCHYo652yHb3sIV27nz5eFc%2BPnbZlW8pzTWSt5cppf4O%2Bhtcunk8clPWNFjZX2nkBKgip9vWVOIv47mFly%2FEu6PfmvCp5V3wAiA6pciQGPSQvUSIoZWI5A0vTls1fdxmvYVSu7PJrWeFkE24vtIVGFZxfJY3xjALfa25k7XidVuocREDZN%2F6%2BTgQ5WfULXTlon40LcdUVG9GsXogZqyWpJqFaqc68RpUGOrxyQpmutZDitU7I7w1GffTRmRs8hBJp5AUnR%2B0GozfWnSs3W8vkiz30Mup02ltJ%2BRpYQaLE08U0xCcu1pIaHnlpD0kABSMDc1XDxMeTvXiIH6sF6BA0dp4jG6qFiH2%2F0yFPBiDI0M1SZldOPwYPtinaBpiuYcZ%2FWRQKeiG%2Bmf9EnUSUi1N1VnkvTLJ929xQSVdJi53yEhXQsbN%2FtxqP3gj8o8mR9IQTOvKAUBOUpKQhLMmJ%2FNbwgnFS6ngG7eeF1JH%2BROCWqXFSdRPNEwhZqZvQY6pgH%2F0Oe6qE%2B8QAklwsEwaI3nEsp6XNk0J%2B%2FT9r3WTBcef15N7S0bB5p6R%2Bv0fHeYX3we5zr9RpeTC6pqA%2BOXmVkxjZXd1c4tzOH94kHVZSxVB8ePsEPazG2A0k2EZdVxjd%2FDW20hhtaOpMqZX3oruvuBbyXYJK7aOSg4M87Iptg3UXB7B%2BFWeG9aWYev8f7Pz9u3ed3E7fWPi11wPaYyGaZS%2BzRACfsn&X-Amz-Signature=bf310de50721f189ea0aad02a003a1f1852c94d087b585b25d39a12587068b44&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SCFUBMCJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIF3rdQXfefMcPMHxQdJIeqpHr8DnsV9OM0h0GcG9IHmYAiAswJKhDELzMKzRNg1glAvdKNFkC7yRRE6coFsO%2FM7O4yr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMnoLeVHTKFVRmdnVjKtwDhL9mFILdk2S388eBpJ6xZVrIZUR3TgHLgKoWF9iS8ZURSJWkOcKxFcU3DyPVAmKgRIHyg9%2FciRboGCcDfiwC8avbCOMSzUZdnYA48qd9UcmINinue2%2Bg8%2B6o4IzSTSX54bWJAE2zMhCHYo652yHb3sIV27nz5eFc%2BPnbZlW8pzTWSt5cppf4O%2Bhtcunk8clPWNFjZX2nkBKgip9vWVOIv47mFly%2FEu6PfmvCp5V3wAiA6pciQGPSQvUSIoZWI5A0vTls1fdxmvYVSu7PJrWeFkE24vtIVGFZxfJY3xjALfa25k7XidVuocREDZN%2F6%2BTgQ5WfULXTlon40LcdUVG9GsXogZqyWpJqFaqc68RpUGOrxyQpmutZDitU7I7w1GffTRmRs8hBJp5AUnR%2B0GozfWnSs3W8vkiz30Mup02ltJ%2BRpYQaLE08U0xCcu1pIaHnlpD0kABSMDc1XDxMeTvXiIH6sF6BA0dp4jG6qFiH2%2F0yFPBiDI0M1SZldOPwYPtinaBpiuYcZ%2FWRQKeiG%2Bmf9EnUSUi1N1VnkvTLJ929xQSVdJi53yEhXQsbN%2FtxqP3gj8o8mR9IQTOvKAUBOUpKQhLMmJ%2FNbwgnFS6ngG7eeF1JH%2BROCWqXFSdRPNEwhZqZvQY6pgH%2F0Oe6qE%2B8QAklwsEwaI3nEsp6XNk0J%2B%2FT9r3WTBcef15N7S0bB5p6R%2Bv0fHeYX3we5zr9RpeTC6pqA%2BOXmVkxjZXd1c4tzOH94kHVZSxVB8ePsEPazG2A0k2EZdVxjd%2FDW20hhtaOpMqZX3oruvuBbyXYJK7aOSg4M87Iptg3UXB7B%2BFWeG9aWYev8f7Pz9u3ed3E7fWPi11wPaYyGaZS%2BzRACfsn&X-Amz-Signature=42568585f6a28ca18e5d7b265cc7d40ae5174d488c76fa93aad44bf614c4e845&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ZQW6HOW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIA%2B2qYic4YH%2FHrSjZhI0OeOZ08W%2FJ6JcQz4oqsQUApc5AiAe1uJC4PLG7MVH614w0OwpMNbumFnqAdmRdGi37IyUNir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMLjBk9cVl%2Bc0pFQPxKtwDGhcsbcQw6CctxVvXCqrx5t9fwZcRcCpnHyHbFTZNWzKwBK1YYqu5v69DZ0GWGzwUzwaKyKXmp5NDDNVeju67o%2BU9iU6MYjiJhud2EtfAsbGbe0OZgULZDFahV5HMQn1gOdqxijY%2BO0KXgAQyjT7vQiqLkMl13Zrm7xu%2F1X2n09XJGeZpa0pApLUqGlKKmzlPpdW30ws58skVCz5n6A6xLW8t22usdNn7bhyDbO7Gon11VcHUzn1dm%2BichGJ0pN3VWwVUHBkM4AUf9XW2U%2BQLCy8W6MIOlkNhFDU9WNk%2BxywVj5PGJA0qgqnRk%2BlRbPm3JTaXy%2FMi6j8%2FJERPgwiZqCZi%2B9lMTQnODzIAs2UT4tp58B8kt2YQmu8Zmrokg5tsH0kZAdWzkZldmq%2Ftox5mHt8X6E5jYEMmAFFmPUfaT%2FiYx0a68InFB3xUrNR3c3fmhP8XwJYtBUv%2FhwYfNp86QfoiDNyYchnTY%2FXuoY8qBIi5ma0%2FkGlPcxp9SMpSvIVRh3H7u8QTJOYhZwn02CIkSGucbILJD75mi0Qbr5eIvYljZFX4qniSITJ3nH9gXsVTrDvmS3wEBm87PbbclvtZdab3bXJd4cU1EiodHBbOFsAZICS%2Fa5FugUbT%2BOEw%2FJmZvQY6pgGuipa0Ti3z4lSoc2Ebb2xZDGxatQd5U2CJd5d0juTLGaSiwK1WlZfV6X%2Fv1XoE42IqA2dL8GWOIVgQxGmaSKw0t8cqRR9M9Jmue0GHq02zbqkhHWnLDXTqLbZDHfRmKnAzmlfv0xOOjF%2BTCfJcXwrUi%2FNrsYSGD8M8dPrp12siEGiDa9JfP74GrhzZ9omt6vmz6sLH8y8VDGFBWaKImOvHbWIIYciW&X-Amz-Signature=dfe9923c6b624cd337d24bab415bad7e8b6062df8730a89887e5fa31cd73e71a&X-Amz-SignedHeaders=host&x-id=GetObject)
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