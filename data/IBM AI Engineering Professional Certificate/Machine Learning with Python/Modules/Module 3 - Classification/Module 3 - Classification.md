

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3UN44C4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIG8BSyyynkCe%2FFCVl%2BGK4afOwi0EPMBpE8RZw4Me%2B0tgAiEArLf2Ux3JlSyzzam4Mjmv0cV5uoZ%2F%2BsMvpPueSjAF%2FQYq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDFn0mOSB9S7hpPblWircA5qNM%2Bij7Rawd2mBU1WNM5E6RL4ujtHJeXF1v3%2FAShxWHo1MUJ3wX3eAoTsh3WdVbbtoggh3cPI0l32yyZmjIj7spgRK6%2BnsxFhUdaR1BmEuuXfLJwjuJekzBXiEMVg6NLzdoAVZbsDIXlEdF9eqxYQOa2Fp37YGuOMWppnlmLFVQlmpQdqDjh65Z9OzHGfNW4TAGeydYh4F1kPYV1zCXiuL%2FoZT%2FysMHPs1lTpODnLZOCL0HpwgsIMQ94UELSqdbWQyfr%2FJTydEtuXGz60QfnlFyJG2K%2Bi1OvaZ1Tp8hKBYOn%2B3RsyrAukGIU4i9w%2B4PmwQ5qz%2BME5cO%2BStIiEHhRi1w7NauRDlN8ysCd7FcPNJTV4wrb9wKOdtYILMyS53cO96rOThSBooP%2F%2FhNd6eDv50OuNS2ARgqPnVh57gprPe%2FB6jdiJ%2BgeHyJ8Vmj1%2FLirTSUrdqaGCCMWmJIrvHxSJs7zd%2FA6rWH%2F%2BKW04Uqz%2BjiZbgf1MXQ3KxXNAsdqxMYYByr9CU0P%2FBVOrBXj6EpiMtA3D17AVAd0Qt4YHRmufjQ2OC2p1kYLoIMIa4NSa7kF3FiJCUim4OmANjkLnE0EBJrwV9z5OfEb7fJSAfMFj0MZdQ4e39Y4FxYERcMJqeiL0GOqUBOPTgsTReHdtnNlc%2F5VxUUYDTaIwroJ5ekgOzGQTgeVsPPJHMzcKMUTbYlQVJD2uXbDaoypQdf6of9uqNWZJcyDzw5Xg4%2FX4RKCyr9lTmnZTJbYiSEPHFXRQ6ZSLpLuRhpFYt5k8V%2BoJNOQ8Z%2FXI0YRcGqWJgQZD%2Fzph%2FQdjW4sQEdkRe3SnSmsVrBuh3qby494oVv4e%2FH2AWQBh2EtAKIk5u1ojU&X-Amz-Signature=9e85cba01488fb0ef6ecf5d251e92c189f37473e19516b139b4255d5588ca2c6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3UN44C4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIG8BSyyynkCe%2FFCVl%2BGK4afOwi0EPMBpE8RZw4Me%2B0tgAiEArLf2Ux3JlSyzzam4Mjmv0cV5uoZ%2F%2BsMvpPueSjAF%2FQYq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDFn0mOSB9S7hpPblWircA5qNM%2Bij7Rawd2mBU1WNM5E6RL4ujtHJeXF1v3%2FAShxWHo1MUJ3wX3eAoTsh3WdVbbtoggh3cPI0l32yyZmjIj7spgRK6%2BnsxFhUdaR1BmEuuXfLJwjuJekzBXiEMVg6NLzdoAVZbsDIXlEdF9eqxYQOa2Fp37YGuOMWppnlmLFVQlmpQdqDjh65Z9OzHGfNW4TAGeydYh4F1kPYV1zCXiuL%2FoZT%2FysMHPs1lTpODnLZOCL0HpwgsIMQ94UELSqdbWQyfr%2FJTydEtuXGz60QfnlFyJG2K%2Bi1OvaZ1Tp8hKBYOn%2B3RsyrAukGIU4i9w%2B4PmwQ5qz%2BME5cO%2BStIiEHhRi1w7NauRDlN8ysCd7FcPNJTV4wrb9wKOdtYILMyS53cO96rOThSBooP%2F%2FhNd6eDv50OuNS2ARgqPnVh57gprPe%2FB6jdiJ%2BgeHyJ8Vmj1%2FLirTSUrdqaGCCMWmJIrvHxSJs7zd%2FA6rWH%2F%2BKW04Uqz%2BjiZbgf1MXQ3KxXNAsdqxMYYByr9CU0P%2FBVOrBXj6EpiMtA3D17AVAd0Qt4YHRmufjQ2OC2p1kYLoIMIa4NSa7kF3FiJCUim4OmANjkLnE0EBJrwV9z5OfEb7fJSAfMFj0MZdQ4e39Y4FxYERcMJqeiL0GOqUBOPTgsTReHdtnNlc%2F5VxUUYDTaIwroJ5ekgOzGQTgeVsPPJHMzcKMUTbYlQVJD2uXbDaoypQdf6of9uqNWZJcyDzw5Xg4%2FX4RKCyr9lTmnZTJbYiSEPHFXRQ6ZSLpLuRhpFYt5k8V%2BoJNOQ8Z%2FXI0YRcGqWJgQZD%2Fzph%2FQdjW4sQEdkRe3SnSmsVrBuh3qby494oVv4e%2FH2AWQBh2EtAKIk5u1ojU&X-Amz-Signature=85e0252056787fb2bacdcfd17778a83dd5b0fff88eaa4ad2696d952b34bc403d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3UN44C4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIG8BSyyynkCe%2FFCVl%2BGK4afOwi0EPMBpE8RZw4Me%2B0tgAiEArLf2Ux3JlSyzzam4Mjmv0cV5uoZ%2F%2BsMvpPueSjAF%2FQYq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDFn0mOSB9S7hpPblWircA5qNM%2Bij7Rawd2mBU1WNM5E6RL4ujtHJeXF1v3%2FAShxWHo1MUJ3wX3eAoTsh3WdVbbtoggh3cPI0l32yyZmjIj7spgRK6%2BnsxFhUdaR1BmEuuXfLJwjuJekzBXiEMVg6NLzdoAVZbsDIXlEdF9eqxYQOa2Fp37YGuOMWppnlmLFVQlmpQdqDjh65Z9OzHGfNW4TAGeydYh4F1kPYV1zCXiuL%2FoZT%2FysMHPs1lTpODnLZOCL0HpwgsIMQ94UELSqdbWQyfr%2FJTydEtuXGz60QfnlFyJG2K%2Bi1OvaZ1Tp8hKBYOn%2B3RsyrAukGIU4i9w%2B4PmwQ5qz%2BME5cO%2BStIiEHhRi1w7NauRDlN8ysCd7FcPNJTV4wrb9wKOdtYILMyS53cO96rOThSBooP%2F%2FhNd6eDv50OuNS2ARgqPnVh57gprPe%2FB6jdiJ%2BgeHyJ8Vmj1%2FLirTSUrdqaGCCMWmJIrvHxSJs7zd%2FA6rWH%2F%2BKW04Uqz%2BjiZbgf1MXQ3KxXNAsdqxMYYByr9CU0P%2FBVOrBXj6EpiMtA3D17AVAd0Qt4YHRmufjQ2OC2p1kYLoIMIa4NSa7kF3FiJCUim4OmANjkLnE0EBJrwV9z5OfEb7fJSAfMFj0MZdQ4e39Y4FxYERcMJqeiL0GOqUBOPTgsTReHdtnNlc%2F5VxUUYDTaIwroJ5ekgOzGQTgeVsPPJHMzcKMUTbYlQVJD2uXbDaoypQdf6of9uqNWZJcyDzw5Xg4%2FX4RKCyr9lTmnZTJbYiSEPHFXRQ6ZSLpLuRhpFYt5k8V%2BoJNOQ8Z%2FXI0YRcGqWJgQZD%2Fzph%2FQdjW4sQEdkRe3SnSmsVrBuh3qby494oVv4e%2FH2AWQBh2EtAKIk5u1ojU&X-Amz-Signature=2d7ab5b281cc8868221b3a336604b9a5ef79717b69d02d71357b2efbb9df8cf6&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WP4DPY3H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIAU5lCvkqCT65rcfYLAu3I%2FUQAah9OdsHgYNvYEv5G6xAiARkeyhOQ1DpdNRHkKNoIdcXFCiiMk6GV0rL6ZeKT0%2FzCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMkSLxG%2FnGSF80wCEEKtwDuwBlapIw5aVtQFN2eM%2F5GwDLtdMcQ3OOzEu5MdllaAg1ujQdrqgLQ%2By5tmsDC2buxNbgjPazqLyZ%2FHnQZDfSmO4k1O4JFIesif0eQZ%2FsH2IWDnplOw7r91Ggt7PGcjuBvejU8uvs53X5X3qjVEL%2FBUI54%2FwZNjSnI2m1NYQK4OsDQBbdMSa6nC8cil7Ysq1xvAdJmmuMBuvSMecRJMDq99%2BAgECnOf8zucvRXycyj%2BzhyERD7vkHBGlEtvAw7rB%2B%2FWO0Z7obEb5WEwfiKVEsDARM2G4TNoij74YvYdpOuEGzrO2eWmjsHvgL%2BEHcjEwRqVHrXKEd%2Bs0r314Imt%2F6juRUaFKwEsXm5UPSCfQf7o6xAUjg4S6P7l25GREUaESnd9r0HjnJHUQbylO8A6z5T0DFJRN%2F2YZ6wMqxlKi7aTr3T7dMI%2F4A8wXfw60z20QAATnsWJtOJ3ZElh1GpKH%2BvV3oT8rZaDsAeNp4FKAwqjNSxuCuHlHx%2F265I2zJHzH2UyKIEozjbFU3c1aO3TuNzxjM8BA15mz%2FW%2FpRLhY3SwgEXKOnI%2BO6JwtlzoB%2FXx2%2F17dxBDT%2FjSfLT4ALa2tMiI4nmt%2F7OACNRoDrAED8PjjqRdGBJmEWbizaZ%2Bgwop6IvQY6pgFP%2BCEyaIdLQIkeBpJ4kvh5XV8kAi47If%2B46uao8rHRZsEadl5cMetIe2i6abaB%2BU9PFj0w3bgEuj8%2FjeLoZzRv6SeNGr%2BEh8flDM7FxpK%2Bx6oRBg4KaeeTRGrcY0aNyT4c6eHue7JlCQQByU0QZnPxia0o6%2BD1WFMcirrrC7C%2F8yxX2F052yN6QDacGZYpJGG5ePke9mZ76TZPJ6QcuCAE70n1%2FFYU&X-Amz-Signature=71af1c6f2594afbd11333125a26743a26121237b1b915102d2c3f1e122db3fb9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WP4DPY3H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIAU5lCvkqCT65rcfYLAu3I%2FUQAah9OdsHgYNvYEv5G6xAiARkeyhOQ1DpdNRHkKNoIdcXFCiiMk6GV0rL6ZeKT0%2FzCr%2FAwguEAAaDDYzNzQyMzE4MzgwNSIMkSLxG%2FnGSF80wCEEKtwDuwBlapIw5aVtQFN2eM%2F5GwDLtdMcQ3OOzEu5MdllaAg1ujQdrqgLQ%2By5tmsDC2buxNbgjPazqLyZ%2FHnQZDfSmO4k1O4JFIesif0eQZ%2FsH2IWDnplOw7r91Ggt7PGcjuBvejU8uvs53X5X3qjVEL%2FBUI54%2FwZNjSnI2m1NYQK4OsDQBbdMSa6nC8cil7Ysq1xvAdJmmuMBuvSMecRJMDq99%2BAgECnOf8zucvRXycyj%2BzhyERD7vkHBGlEtvAw7rB%2B%2FWO0Z7obEb5WEwfiKVEsDARM2G4TNoij74YvYdpOuEGzrO2eWmjsHvgL%2BEHcjEwRqVHrXKEd%2Bs0r314Imt%2F6juRUaFKwEsXm5UPSCfQf7o6xAUjg4S6P7l25GREUaESnd9r0HjnJHUQbylO8A6z5T0DFJRN%2F2YZ6wMqxlKi7aTr3T7dMI%2F4A8wXfw60z20QAATnsWJtOJ3ZElh1GpKH%2BvV3oT8rZaDsAeNp4FKAwqjNSxuCuHlHx%2F265I2zJHzH2UyKIEozjbFU3c1aO3TuNzxjM8BA15mz%2FW%2FpRLhY3SwgEXKOnI%2BO6JwtlzoB%2FXx2%2F17dxBDT%2FjSfLT4ALa2tMiI4nmt%2F7OACNRoDrAED8PjjqRdGBJmEWbizaZ%2Bgwop6IvQY6pgFP%2BCEyaIdLQIkeBpJ4kvh5XV8kAi47If%2B46uao8rHRZsEadl5cMetIe2i6abaB%2BU9PFj0w3bgEuj8%2FjeLoZzRv6SeNGr%2BEh8flDM7FxpK%2Bx6oRBg4KaeeTRGrcY0aNyT4c6eHue7JlCQQByU0QZnPxia0o6%2BD1WFMcirrrC7C%2F8yxX2F052yN6QDacGZYpJGG5ePke9mZ76TZPJ6QcuCAE70n1%2FFYU&X-Amz-Signature=f484c2bd4fe917b8b37640a89bbc4727871f30dd83bfcbea2cda1a56e4fc66c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3UN44C4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIG8BSyyynkCe%2FFCVl%2BGK4afOwi0EPMBpE8RZw4Me%2B0tgAiEArLf2Ux3JlSyzzam4Mjmv0cV5uoZ%2F%2BsMvpPueSjAF%2FQYq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDFn0mOSB9S7hpPblWircA5qNM%2Bij7Rawd2mBU1WNM5E6RL4ujtHJeXF1v3%2FAShxWHo1MUJ3wX3eAoTsh3WdVbbtoggh3cPI0l32yyZmjIj7spgRK6%2BnsxFhUdaR1BmEuuXfLJwjuJekzBXiEMVg6NLzdoAVZbsDIXlEdF9eqxYQOa2Fp37YGuOMWppnlmLFVQlmpQdqDjh65Z9OzHGfNW4TAGeydYh4F1kPYV1zCXiuL%2FoZT%2FysMHPs1lTpODnLZOCL0HpwgsIMQ94UELSqdbWQyfr%2FJTydEtuXGz60QfnlFyJG2K%2Bi1OvaZ1Tp8hKBYOn%2B3RsyrAukGIU4i9w%2B4PmwQ5qz%2BME5cO%2BStIiEHhRi1w7NauRDlN8ysCd7FcPNJTV4wrb9wKOdtYILMyS53cO96rOThSBooP%2F%2FhNd6eDv50OuNS2ARgqPnVh57gprPe%2FB6jdiJ%2BgeHyJ8Vmj1%2FLirTSUrdqaGCCMWmJIrvHxSJs7zd%2FA6rWH%2F%2BKW04Uqz%2BjiZbgf1MXQ3KxXNAsdqxMYYByr9CU0P%2FBVOrBXj6EpiMtA3D17AVAd0Qt4YHRmufjQ2OC2p1kYLoIMIa4NSa7kF3FiJCUim4OmANjkLnE0EBJrwV9z5OfEb7fJSAfMFj0MZdQ4e39Y4FxYERcMJqeiL0GOqUBOPTgsTReHdtnNlc%2F5VxUUYDTaIwroJ5ekgOzGQTgeVsPPJHMzcKMUTbYlQVJD2uXbDaoypQdf6of9uqNWZJcyDzw5Xg4%2FX4RKCyr9lTmnZTJbYiSEPHFXRQ6ZSLpLuRhpFYt5k8V%2BoJNOQ8Z%2FXI0YRcGqWJgQZD%2Fzph%2FQdjW4sQEdkRe3SnSmsVrBuh3qby494oVv4e%2FH2AWQBh2EtAKIk5u1ojU&X-Amz-Signature=1d1fc8b311935dd150212f697bcb5b0fe6c9e0b1de5a10ae55c5b5b1b6b171fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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