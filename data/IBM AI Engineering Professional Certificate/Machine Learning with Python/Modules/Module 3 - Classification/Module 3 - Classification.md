

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DJ7K277%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPWSpIwk6GB2ieNk3v8KhfdDJiZWRPP7zUjwAKGy4KqgIgFmsH8cZQ%2B6FK8vowdjB%2BtI8Cp5sYOqnIm4L8ThxrZO4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDIkRIVPJwJ9ly4eyrSrcA0JreMruyanh1SRb9H97hMP7vr27fNKLTfDNYQzOf7l2STAAJpgGNNE8ueX3by4iRObPJaPsq9bSgRXALvIVCbIojfiq0sUtvoH83gkhrRgTWbg7iPFrhHP5lB7VhYFR2rsLHrUQxLvSMXx3sSl2YCSo7cx7c3bQ%2FaHlAwZT8cBaeaS8N7qrji1BhWsP8d6Aiwl3BLK%2BChm0b2nHa21%2B0xXRC7rxUUQ4QtXX7s9UIQDWZ6RL6ZlxPVBOYTOVKxJiDZhlEW8UGA5JcSpI3bA9pGal4L%2B%2FVxEWdgbQ7gpN%2FU2wE%2Fe2sJmkCfUY3E9mL%2F229zjrd0JCfAQ2pOIc9isJ9MXiwNZZGjs5X6ySXJ5YFDuLzxLueZK7Qo94iweleiZRNwIEMSppr6%2FnmWIp3NG67stAQvu01agmeo%2BwRhqC8aCtP%2F5EMUBhLz1MEH9bZ9mrayFBJCX61kPDSg6Q8ZoC2dG9yqymNUFf%2FqAPzsW8o1bdNvRVZdi98nzcgHfLWJxZd6jRIwvqH7FRSxe9cukz8a1IX7pIDX8nm4me0Fy0mLxENJ80J137iZg4ZSVV%2BZMEE10sqaD%2FMUlTVvvNXn9CxsfzlcaTr9JPVffpBEu9E1G%2B0nw%2Bup%2BzQZgaiWTZMOWNg70GOqUBRFSa%2FFzxgF8u69fmAx8maeVITU7rULRaDCPXZEpA%2BvZtOLngcD2QiW70LbaNjWYnNfoMQXISvMHOfbeRTphOndsb4K6WQIGXLZw6gMojXscWLId1npL91gYciKd9DC0HSjL7oGKzEeam5P%2B%2BEsTnDtHeRoHYCfTzmCeygToaYnUv7j563cGyLgXLXlDYlT%2BoC3PF9Cs8biTa6TGTcKAPwqv7xnlx&X-Amz-Signature=72760fcfe16db6bfdfdbf7968ebd27c3adf50ddeef9163cbdc3f3415c2f675a4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DJ7K277%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPWSpIwk6GB2ieNk3v8KhfdDJiZWRPP7zUjwAKGy4KqgIgFmsH8cZQ%2B6FK8vowdjB%2BtI8Cp5sYOqnIm4L8ThxrZO4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDIkRIVPJwJ9ly4eyrSrcA0JreMruyanh1SRb9H97hMP7vr27fNKLTfDNYQzOf7l2STAAJpgGNNE8ueX3by4iRObPJaPsq9bSgRXALvIVCbIojfiq0sUtvoH83gkhrRgTWbg7iPFrhHP5lB7VhYFR2rsLHrUQxLvSMXx3sSl2YCSo7cx7c3bQ%2FaHlAwZT8cBaeaS8N7qrji1BhWsP8d6Aiwl3BLK%2BChm0b2nHa21%2B0xXRC7rxUUQ4QtXX7s9UIQDWZ6RL6ZlxPVBOYTOVKxJiDZhlEW8UGA5JcSpI3bA9pGal4L%2B%2FVxEWdgbQ7gpN%2FU2wE%2Fe2sJmkCfUY3E9mL%2F229zjrd0JCfAQ2pOIc9isJ9MXiwNZZGjs5X6ySXJ5YFDuLzxLueZK7Qo94iweleiZRNwIEMSppr6%2FnmWIp3NG67stAQvu01agmeo%2BwRhqC8aCtP%2F5EMUBhLz1MEH9bZ9mrayFBJCX61kPDSg6Q8ZoC2dG9yqymNUFf%2FqAPzsW8o1bdNvRVZdi98nzcgHfLWJxZd6jRIwvqH7FRSxe9cukz8a1IX7pIDX8nm4me0Fy0mLxENJ80J137iZg4ZSVV%2BZMEE10sqaD%2FMUlTVvvNXn9CxsfzlcaTr9JPVffpBEu9E1G%2B0nw%2Bup%2BzQZgaiWTZMOWNg70GOqUBRFSa%2FFzxgF8u69fmAx8maeVITU7rULRaDCPXZEpA%2BvZtOLngcD2QiW70LbaNjWYnNfoMQXISvMHOfbeRTphOndsb4K6WQIGXLZw6gMojXscWLId1npL91gYciKd9DC0HSjL7oGKzEeam5P%2B%2BEsTnDtHeRoHYCfTzmCeygToaYnUv7j563cGyLgXLXlDYlT%2BoC3PF9Cs8biTa6TGTcKAPwqv7xnlx&X-Amz-Signature=f6fff45e32612256fd05d35720b3c61f19b06f5250a9e4529cdb70c8816ba206&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DJ7K277%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPWSpIwk6GB2ieNk3v8KhfdDJiZWRPP7zUjwAKGy4KqgIgFmsH8cZQ%2B6FK8vowdjB%2BtI8Cp5sYOqnIm4L8ThxrZO4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDIkRIVPJwJ9ly4eyrSrcA0JreMruyanh1SRb9H97hMP7vr27fNKLTfDNYQzOf7l2STAAJpgGNNE8ueX3by4iRObPJaPsq9bSgRXALvIVCbIojfiq0sUtvoH83gkhrRgTWbg7iPFrhHP5lB7VhYFR2rsLHrUQxLvSMXx3sSl2YCSo7cx7c3bQ%2FaHlAwZT8cBaeaS8N7qrji1BhWsP8d6Aiwl3BLK%2BChm0b2nHa21%2B0xXRC7rxUUQ4QtXX7s9UIQDWZ6RL6ZlxPVBOYTOVKxJiDZhlEW8UGA5JcSpI3bA9pGal4L%2B%2FVxEWdgbQ7gpN%2FU2wE%2Fe2sJmkCfUY3E9mL%2F229zjrd0JCfAQ2pOIc9isJ9MXiwNZZGjs5X6ySXJ5YFDuLzxLueZK7Qo94iweleiZRNwIEMSppr6%2FnmWIp3NG67stAQvu01agmeo%2BwRhqC8aCtP%2F5EMUBhLz1MEH9bZ9mrayFBJCX61kPDSg6Q8ZoC2dG9yqymNUFf%2FqAPzsW8o1bdNvRVZdi98nzcgHfLWJxZd6jRIwvqH7FRSxe9cukz8a1IX7pIDX8nm4me0Fy0mLxENJ80J137iZg4ZSVV%2BZMEE10sqaD%2FMUlTVvvNXn9CxsfzlcaTr9JPVffpBEu9E1G%2B0nw%2Bup%2BzQZgaiWTZMOWNg70GOqUBRFSa%2FFzxgF8u69fmAx8maeVITU7rULRaDCPXZEpA%2BvZtOLngcD2QiW70LbaNjWYnNfoMQXISvMHOfbeRTphOndsb4K6WQIGXLZw6gMojXscWLId1npL91gYciKd9DC0HSjL7oGKzEeam5P%2B%2BEsTnDtHeRoHYCfTzmCeygToaYnUv7j563cGyLgXLXlDYlT%2BoC3PF9Cs8biTa6TGTcKAPwqv7xnlx&X-Amz-Signature=123863043f0cb46abbdaef3438069cd66e268ab9b44cf7f91311ec44c92e9889&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYGK7BME%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIESdp%2Ba9ygAe%2BOXeyv7Qa%2B%2BdsR9sXozu3WIDij8ZHSbCAiEAwG6yP9vKpsZvK7VRcnnAQ36CfVVPLPrasaWjel5qKPcq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDNj9OyeR7GqtoIEwIyrcA26MSOpQ71fiOZ1joz4HDQOTsXzMMcqhshYanjYTB7%2B4bz%2F%2FETYoqbX3WHCrm2QGMd1aLJKtETfLWZm0w3OlmAv8yMA%2Fs96uB8yfLrEEdY77TwltvY4YyzobWq0EzLo9vOOO9tnIry2VSoS9S2k3Z%2Fva0M8D1dU08d0DOc%2F6kR8FFzfCuhUv45p%2B%2FN%2FOAgpBLZ%2FsmiHCZs%2FWEw%2Fg1Q7DGkJeIu0hD%2FxW0oYsAJHOBwbPiVB9tojju0DDGZqEuiFv5Dikbz%2B1UuVxf91A7XXRKQIzQNNidIVoeoiEWLiNQuUHs4BIL5kZWDraudlUOSuoNOAEiYK%2FBBsDPgHcEeTBb8uOpw2qCz89J%2B7jqKPTxvs%2FayNWWKEVi2Qr1bupngSMy7lPrFZ8fHiq%2FzIkhqgu3SCY5snUJAkzjcwjHNVQUbDUVl%2BHJ1Pv1HdRLU0FPAUAg1LBP5h9KMRtSt9b2dWc%2BMuRAaA6vvhc0IdkzkvjjPmPbV7n4D52DUr%2FirTGzW21B%2FT3F%2BGds86nLsSwBJHKl3W7rgxTVXAkmBYw2iZK4LD7VAh8wI5bkZ28T4jtad1g9qXNNIRKA7xPj6IaoRpbKAaTzkSrciVSKEXek9aCUoQWHnIQbGJJ011UL6zuMMCNg70GOqUBbfGPk%2FaEfxzkz3YNy5GWVyVGS%2BEfUTo8sbiWTcYv%2FQkEMNcWxWle4iVXNITmXcahz99fWGRQ8TEIhjWf3et1Qo9Ouom55uXaPRoaWVSv8W3EMNEiqNeuFIYobeBUz%2FBfu8vWJ6H1Euk%2FH59vVRdqxn7wcEAl9JPgqD3xtMcSbk0hI4%2F%2FAU3jmBqLUbd0qDdkwBBEXuaMEuLf2un895azNmNyVKid&X-Amz-Signature=089764cca39b14e681f1df14c3bd1370c39f81f658b0c6d0356210bee8b1a471&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYGK7BME%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIESdp%2Ba9ygAe%2BOXeyv7Qa%2B%2BdsR9sXozu3WIDij8ZHSbCAiEAwG6yP9vKpsZvK7VRcnnAQ36CfVVPLPrasaWjel5qKPcq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDNj9OyeR7GqtoIEwIyrcA26MSOpQ71fiOZ1joz4HDQOTsXzMMcqhshYanjYTB7%2B4bz%2F%2FETYoqbX3WHCrm2QGMd1aLJKtETfLWZm0w3OlmAv8yMA%2Fs96uB8yfLrEEdY77TwltvY4YyzobWq0EzLo9vOOO9tnIry2VSoS9S2k3Z%2Fva0M8D1dU08d0DOc%2F6kR8FFzfCuhUv45p%2B%2FN%2FOAgpBLZ%2FsmiHCZs%2FWEw%2Fg1Q7DGkJeIu0hD%2FxW0oYsAJHOBwbPiVB9tojju0DDGZqEuiFv5Dikbz%2B1UuVxf91A7XXRKQIzQNNidIVoeoiEWLiNQuUHs4BIL5kZWDraudlUOSuoNOAEiYK%2FBBsDPgHcEeTBb8uOpw2qCz89J%2B7jqKPTxvs%2FayNWWKEVi2Qr1bupngSMy7lPrFZ8fHiq%2FzIkhqgu3SCY5snUJAkzjcwjHNVQUbDUVl%2BHJ1Pv1HdRLU0FPAUAg1LBP5h9KMRtSt9b2dWc%2BMuRAaA6vvhc0IdkzkvjjPmPbV7n4D52DUr%2FirTGzW21B%2FT3F%2BGds86nLsSwBJHKl3W7rgxTVXAkmBYw2iZK4LD7VAh8wI5bkZ28T4jtad1g9qXNNIRKA7xPj6IaoRpbKAaTzkSrciVSKEXek9aCUoQWHnIQbGJJ011UL6zuMMCNg70GOqUBbfGPk%2FaEfxzkz3YNy5GWVyVGS%2BEfUTo8sbiWTcYv%2FQkEMNcWxWle4iVXNITmXcahz99fWGRQ8TEIhjWf3et1Qo9Ouom55uXaPRoaWVSv8W3EMNEiqNeuFIYobeBUz%2FBfu8vWJ6H1Euk%2FH59vVRdqxn7wcEAl9JPgqD3xtMcSbk0hI4%2F%2FAU3jmBqLUbd0qDdkwBBEXuaMEuLf2un895azNmNyVKid&X-Amz-Signature=b2a26cbf9ca52dd43503f64330562dab12f6c7e691311eef9d65ddbe809a9d86&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DJ7K277%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPWSpIwk6GB2ieNk3v8KhfdDJiZWRPP7zUjwAKGy4KqgIgFmsH8cZQ%2B6FK8vowdjB%2BtI8Cp5sYOqnIm4L8ThxrZO4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDIkRIVPJwJ9ly4eyrSrcA0JreMruyanh1SRb9H97hMP7vr27fNKLTfDNYQzOf7l2STAAJpgGNNE8ueX3by4iRObPJaPsq9bSgRXALvIVCbIojfiq0sUtvoH83gkhrRgTWbg7iPFrhHP5lB7VhYFR2rsLHrUQxLvSMXx3sSl2YCSo7cx7c3bQ%2FaHlAwZT8cBaeaS8N7qrji1BhWsP8d6Aiwl3BLK%2BChm0b2nHa21%2B0xXRC7rxUUQ4QtXX7s9UIQDWZ6RL6ZlxPVBOYTOVKxJiDZhlEW8UGA5JcSpI3bA9pGal4L%2B%2FVxEWdgbQ7gpN%2FU2wE%2Fe2sJmkCfUY3E9mL%2F229zjrd0JCfAQ2pOIc9isJ9MXiwNZZGjs5X6ySXJ5YFDuLzxLueZK7Qo94iweleiZRNwIEMSppr6%2FnmWIp3NG67stAQvu01agmeo%2BwRhqC8aCtP%2F5EMUBhLz1MEH9bZ9mrayFBJCX61kPDSg6Q8ZoC2dG9yqymNUFf%2FqAPzsW8o1bdNvRVZdi98nzcgHfLWJxZd6jRIwvqH7FRSxe9cukz8a1IX7pIDX8nm4me0Fy0mLxENJ80J137iZg4ZSVV%2BZMEE10sqaD%2FMUlTVvvNXn9CxsfzlcaTr9JPVffpBEu9E1G%2B0nw%2Bup%2BzQZgaiWTZMOWNg70GOqUBRFSa%2FFzxgF8u69fmAx8maeVITU7rULRaDCPXZEpA%2BvZtOLngcD2QiW70LbaNjWYnNfoMQXISvMHOfbeRTphOndsb4K6WQIGXLZw6gMojXscWLId1npL91gYciKd9DC0HSjL7oGKzEeam5P%2B%2BEsTnDtHeRoHYCfTzmCeygToaYnUv7j563cGyLgXLXlDYlT%2BoC3PF9Cs8biTa6TGTcKAPwqv7xnlx&X-Amz-Signature=2515a94d7ea5b99695c8d4d3524a2d4bf054b779d15001a78ed2106d5cb52123&X-Amz-SignedHeaders=host&x-id=GetObject)
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