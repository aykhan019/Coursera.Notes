

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DDRGRMV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq328%2BwbSq3CBhoxJ%2Fm%2F5OE97DzU2wA%2FFfDB6DJIXK1wIgcHPLjgMo8hFIRKc5VPKay7j5BL01kg4xoDo5Xpc6RNkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDI6BuXeHj6tuWPd%2BOCrcAy0wTiSCU%2Bh2CKFEm0alpG4mqr3%2BcvyyFpIWZzLb22iRB3RpqkXcGDG9csb%2BSMHa7FP20ciT6N7YPROikS0vj0Fn85V2cRnIDz8s%2BbMHmE7zZZ4X0mxx1YvNKDV8rhzImVvq58V50cGVkQXRBoCgobuPa18ni6YbDuMlg%2FqVSrUybqjyXHhAnJgz7itoBVPN86xFMHCi5p3RZDUb9dmITdiVmNpNVCmKxOeD8Br1uYZR8p87o8Nuxu2Jj2%2FoYGmqQUI817X2EE%2BaLJTazmIeuiKDZgu1cQH73HZ9gnPWUmBhO8G5CzXsnThBDP%2FSeQ2Na3M%2Byz9A5KrS9grbPIHLDOrE%2FC39ZqNI0NIsjahEn3QOpNJiSn9EinCNW5BqbPwhmxuyabC%2FubvINOEA3%2FXmgLQJydkgdMbI2eP6Ahrl8p%2BzNP%2BUYmd4T59%2BphwQPv7D981RPijmxyfurBqe4CpX1JkqTv00TNJRh7Dmjh88XABZ0HQXHFSUZGA3CFxwAwOXbneOa9doBqksQswvZ%2F3YoxffRXGRTy%2B9R7PlECJeBVIdxwsERZJDq7oczdWhpWoMgBoaBf%2B%2B7poYoFwhoVROtfWDVk4mswO563DQthzd3WLIhLYWbYaFSWKwTOubMIX0gb0GOqUB2W3H9UgsI0QwvQ7RFEN8JYbM97K0ZrAATyZmPfzmo7uLZVCL0pmBRdznDsHxZzWBweQzzdq9OX349IrBCwN7mcIL5bJrSbbooRf3na1w9oEIr3OLEeyMEXXQLNMHcM4SgzO48wWeUiyml7alUS3cz68V7orWoylXSKtN29KQXd2dz0aag%2FPlVp15BNh1iy87kOF3pk6AdcWRggCXQt5PEKVbtb5R&X-Amz-Signature=974354d2f334c095cc83944480606d2864df12ec67dcc58d4d8d99553ceddf3c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DDRGRMV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq328%2BwbSq3CBhoxJ%2Fm%2F5OE97DzU2wA%2FFfDB6DJIXK1wIgcHPLjgMo8hFIRKc5VPKay7j5BL01kg4xoDo5Xpc6RNkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDI6BuXeHj6tuWPd%2BOCrcAy0wTiSCU%2Bh2CKFEm0alpG4mqr3%2BcvyyFpIWZzLb22iRB3RpqkXcGDG9csb%2BSMHa7FP20ciT6N7YPROikS0vj0Fn85V2cRnIDz8s%2BbMHmE7zZZ4X0mxx1YvNKDV8rhzImVvq58V50cGVkQXRBoCgobuPa18ni6YbDuMlg%2FqVSrUybqjyXHhAnJgz7itoBVPN86xFMHCi5p3RZDUb9dmITdiVmNpNVCmKxOeD8Br1uYZR8p87o8Nuxu2Jj2%2FoYGmqQUI817X2EE%2BaLJTazmIeuiKDZgu1cQH73HZ9gnPWUmBhO8G5CzXsnThBDP%2FSeQ2Na3M%2Byz9A5KrS9grbPIHLDOrE%2FC39ZqNI0NIsjahEn3QOpNJiSn9EinCNW5BqbPwhmxuyabC%2FubvINOEA3%2FXmgLQJydkgdMbI2eP6Ahrl8p%2BzNP%2BUYmd4T59%2BphwQPv7D981RPijmxyfurBqe4CpX1JkqTv00TNJRh7Dmjh88XABZ0HQXHFSUZGA3CFxwAwOXbneOa9doBqksQswvZ%2F3YoxffRXGRTy%2B9R7PlECJeBVIdxwsERZJDq7oczdWhpWoMgBoaBf%2B%2B7poYoFwhoVROtfWDVk4mswO563DQthzd3WLIhLYWbYaFSWKwTOubMIX0gb0GOqUB2W3H9UgsI0QwvQ7RFEN8JYbM97K0ZrAATyZmPfzmo7uLZVCL0pmBRdznDsHxZzWBweQzzdq9OX349IrBCwN7mcIL5bJrSbbooRf3na1w9oEIr3OLEeyMEXXQLNMHcM4SgzO48wWeUiyml7alUS3cz68V7orWoylXSKtN29KQXd2dz0aag%2FPlVp15BNh1iy87kOF3pk6AdcWRggCXQt5PEKVbtb5R&X-Amz-Signature=b9f345a46225cc4d02990befe484a0c0ad67a8bb8179c790e43739e77acbf8d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DDRGRMV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq328%2BwbSq3CBhoxJ%2Fm%2F5OE97DzU2wA%2FFfDB6DJIXK1wIgcHPLjgMo8hFIRKc5VPKay7j5BL01kg4xoDo5Xpc6RNkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDI6BuXeHj6tuWPd%2BOCrcAy0wTiSCU%2Bh2CKFEm0alpG4mqr3%2BcvyyFpIWZzLb22iRB3RpqkXcGDG9csb%2BSMHa7FP20ciT6N7YPROikS0vj0Fn85V2cRnIDz8s%2BbMHmE7zZZ4X0mxx1YvNKDV8rhzImVvq58V50cGVkQXRBoCgobuPa18ni6YbDuMlg%2FqVSrUybqjyXHhAnJgz7itoBVPN86xFMHCi5p3RZDUb9dmITdiVmNpNVCmKxOeD8Br1uYZR8p87o8Nuxu2Jj2%2FoYGmqQUI817X2EE%2BaLJTazmIeuiKDZgu1cQH73HZ9gnPWUmBhO8G5CzXsnThBDP%2FSeQ2Na3M%2Byz9A5KrS9grbPIHLDOrE%2FC39ZqNI0NIsjahEn3QOpNJiSn9EinCNW5BqbPwhmxuyabC%2FubvINOEA3%2FXmgLQJydkgdMbI2eP6Ahrl8p%2BzNP%2BUYmd4T59%2BphwQPv7D981RPijmxyfurBqe4CpX1JkqTv00TNJRh7Dmjh88XABZ0HQXHFSUZGA3CFxwAwOXbneOa9doBqksQswvZ%2F3YoxffRXGRTy%2B9R7PlECJeBVIdxwsERZJDq7oczdWhpWoMgBoaBf%2B%2B7poYoFwhoVROtfWDVk4mswO563DQthzd3WLIhLYWbYaFSWKwTOubMIX0gb0GOqUB2W3H9UgsI0QwvQ7RFEN8JYbM97K0ZrAATyZmPfzmo7uLZVCL0pmBRdznDsHxZzWBweQzzdq9OX349IrBCwN7mcIL5bJrSbbooRf3na1w9oEIr3OLEeyMEXXQLNMHcM4SgzO48wWeUiyml7alUS3cz68V7orWoylXSKtN29KQXd2dz0aag%2FPlVp15BNh1iy87kOF3pk6AdcWRggCXQt5PEKVbtb5R&X-Amz-Signature=5491b0e3676cdd1b05d9c5fba5a0025679e8cb9ba905006eb624d5669c987851&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVLW4FEV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIApVTy2FdhqDd5LJh51DayqVaTgrjWW5q3YynG9dGfV4AiBBbOFIRl6IDSLZthFufaSu1o49s1NNrpK8j39X4MwJWir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMOdTAo7Bhq1Wdkf9tKtwDH8SptJ9aePh4%2FEx4azxaQ6v%2BFZ2l73V%2FqN2rD6FL1jIfxYRLLkzuiqfuzmHKgdqy%2BaNB%2BeKN%2BVdWs7JdJKOWxxdAhOaCQWeeRFUiZ6rqyey15fJUf376ORs3a3oiY6P2bn6Ma%2FPi0lwhbZ8QafI3LXCMzA%2BrtPL2jgI6wxuBpH2Es9YFYN7zp3BR%2FrwzYU25f4W4w7wivuVCPugNxizoCptn6Y6ebM1ODpH1a4a3v1e78Ou6sQailserZd8Tj1VXGjrfXTEAl%2FgAkoWKZVTL9LBmW5lhN39nR3DFyFkqqseypNXgRuXR4lGHSeCR9uheMc8Zaur9zR%2FyZHAlFhonHBh6%2FJdbgS0nRAuAHPjZXOAwBXnhX5eVxoTQFfmrLUQl%2BGh7tW7z%2FjdEZ2gk5bZXvFzIqjQbvyLhmUZzg6TKSvRu9E6xwuOLB9K3ifdJjWgmsR6ciM9G03JVs1FIf%2BmOX5p9zEKOKE7mJYRqPMY8KUsPi0RYbUMOGvzDkEhxD8uFJw01%2BZ8a%2FMRp5F3%2F%2FxnYhFpxXRpabAVrdhLZUQMx7Fsywr032YSLZZzRZ2NG2lwnaxs%2F80ulVtaI6NEAqJ8gVwoPx68SwS4n1F8%2FRnB14pmiEbOVviruWc3r0GowmvSBvQY6pgFE%2FAQZxiuy6B6eRUWNYGNfEwNVXv%2FRJ2qRSYYRXLtVtBbJOoeZMr3X9ZkOQVMWJWiKWZCCZOUrlcDG%2F3Uy5qXy6%2F8R8juR3Ei412dC1Ym7UFAR9Zn4vEgWIMDCX9IlOKOcBn%2Fht7V5B3W96XjHEUuSLFmy%2FfqpiSfNHk%2Fx4ZEaV0wEj0ag2PTYsWElBZnerRycbmK4njMuuGu73gzDlk5Za0ptlbLS&X-Amz-Signature=398e1a5a2c8a215262336599d8e578d278de84d60dc17bb6238d570ffa28eb24&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVLW4FEV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIApVTy2FdhqDd5LJh51DayqVaTgrjWW5q3YynG9dGfV4AiBBbOFIRl6IDSLZthFufaSu1o49s1NNrpK8j39X4MwJWir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMOdTAo7Bhq1Wdkf9tKtwDH8SptJ9aePh4%2FEx4azxaQ6v%2BFZ2l73V%2FqN2rD6FL1jIfxYRLLkzuiqfuzmHKgdqy%2BaNB%2BeKN%2BVdWs7JdJKOWxxdAhOaCQWeeRFUiZ6rqyey15fJUf376ORs3a3oiY6P2bn6Ma%2FPi0lwhbZ8QafI3LXCMzA%2BrtPL2jgI6wxuBpH2Es9YFYN7zp3BR%2FrwzYU25f4W4w7wivuVCPugNxizoCptn6Y6ebM1ODpH1a4a3v1e78Ou6sQailserZd8Tj1VXGjrfXTEAl%2FgAkoWKZVTL9LBmW5lhN39nR3DFyFkqqseypNXgRuXR4lGHSeCR9uheMc8Zaur9zR%2FyZHAlFhonHBh6%2FJdbgS0nRAuAHPjZXOAwBXnhX5eVxoTQFfmrLUQl%2BGh7tW7z%2FjdEZ2gk5bZXvFzIqjQbvyLhmUZzg6TKSvRu9E6xwuOLB9K3ifdJjWgmsR6ciM9G03JVs1FIf%2BmOX5p9zEKOKE7mJYRqPMY8KUsPi0RYbUMOGvzDkEhxD8uFJw01%2BZ8a%2FMRp5F3%2F%2FxnYhFpxXRpabAVrdhLZUQMx7Fsywr032YSLZZzRZ2NG2lwnaxs%2F80ulVtaI6NEAqJ8gVwoPx68SwS4n1F8%2FRnB14pmiEbOVviruWc3r0GowmvSBvQY6pgFE%2FAQZxiuy6B6eRUWNYGNfEwNVXv%2FRJ2qRSYYRXLtVtBbJOoeZMr3X9ZkOQVMWJWiKWZCCZOUrlcDG%2F3Uy5qXy6%2F8R8juR3Ei412dC1Ym7UFAR9Zn4vEgWIMDCX9IlOKOcBn%2Fht7V5B3W96XjHEUuSLFmy%2FfqpiSfNHk%2Fx4ZEaV0wEj0ag2PTYsWElBZnerRycbmK4njMuuGu73gzDlk5Za0ptlbLS&X-Amz-Signature=f5888dfc445b733b504fea7f9a4acff9c94e285d0d13b95c0799bbb40914a79b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DDRGRMV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq328%2BwbSq3CBhoxJ%2Fm%2F5OE97DzU2wA%2FFfDB6DJIXK1wIgcHPLjgMo8hFIRKc5VPKay7j5BL01kg4xoDo5Xpc6RNkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDI6BuXeHj6tuWPd%2BOCrcAy0wTiSCU%2Bh2CKFEm0alpG4mqr3%2BcvyyFpIWZzLb22iRB3RpqkXcGDG9csb%2BSMHa7FP20ciT6N7YPROikS0vj0Fn85V2cRnIDz8s%2BbMHmE7zZZ4X0mxx1YvNKDV8rhzImVvq58V50cGVkQXRBoCgobuPa18ni6YbDuMlg%2FqVSrUybqjyXHhAnJgz7itoBVPN86xFMHCi5p3RZDUb9dmITdiVmNpNVCmKxOeD8Br1uYZR8p87o8Nuxu2Jj2%2FoYGmqQUI817X2EE%2BaLJTazmIeuiKDZgu1cQH73HZ9gnPWUmBhO8G5CzXsnThBDP%2FSeQ2Na3M%2Byz9A5KrS9grbPIHLDOrE%2FC39ZqNI0NIsjahEn3QOpNJiSn9EinCNW5BqbPwhmxuyabC%2FubvINOEA3%2FXmgLQJydkgdMbI2eP6Ahrl8p%2BzNP%2BUYmd4T59%2BphwQPv7D981RPijmxyfurBqe4CpX1JkqTv00TNJRh7Dmjh88XABZ0HQXHFSUZGA3CFxwAwOXbneOa9doBqksQswvZ%2F3YoxffRXGRTy%2B9R7PlECJeBVIdxwsERZJDq7oczdWhpWoMgBoaBf%2B%2B7poYoFwhoVROtfWDVk4mswO563DQthzd3WLIhLYWbYaFSWKwTOubMIX0gb0GOqUB2W3H9UgsI0QwvQ7RFEN8JYbM97K0ZrAATyZmPfzmo7uLZVCL0pmBRdznDsHxZzWBweQzzdq9OX349IrBCwN7mcIL5bJrSbbooRf3na1w9oEIr3OLEeyMEXXQLNMHcM4SgzO48wWeUiyml7alUS3cz68V7orWoylXSKtN29KQXd2dz0aag%2FPlVp15BNh1iy87kOF3pk6AdcWRggCXQt5PEKVbtb5R&X-Amz-Signature=0bb5e9d46e0787fa6d39bc41bc6117f4b8b6d5e26aff2db1c03de5a4300740c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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