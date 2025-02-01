

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MGHB4IX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCssrvb8YwlZCu0VfZt9cku5mbXRg0%2FzdgJrllt5XWVxAIgdIrq5lqaB4oHAlQxunfZOjl0%2BOFWAWgtCNe1oQK7luAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQA3%2FBuCI5GAA7X5SrcA14Ik3qIA6WDjGLXUXLLAZ%2BEyxccp9ZleGIFvsBIfmYEWScvUN8%2Fliqt1dvIp0ES0OnVu%2BVKXHbclo7xfpOAfbUptY492qpibHNVpZzo2IXhOwTBwy7wxOOUEDOYuh7DTAtfLW0p44vJs%2F4%2BvNqGlmh67Uf%2BPLiisH8RG32u6gXTpJs9RwaHLMZXip0Fr%2FP1THKDJzY0WOmlWTmNTNbIueVSmAWN16S%2Bj%2F0ShoGtZ34XsEGfwVPIN%2FefMd3eNX9zSR9oVO%2FYqX4l7OWeU9UjSP4DJpezs8yK8lQCJ7uJEN7DGZSVpqK%2BsWUt62qzIdjPBDuWAfWTNr2Y0RiMahMPqxq8JcAUWqHwgYIht%2BaNuWbLaVm7DJqt%2BPg3%2B2OGxg5iapWMK0%2FlJmprfngsg%2Bqah19SH6jLfP5NRSjg%2B1Nnp3nN06RpIDWF3%2BIi8wq6Cn808p20%2B0Bz1VluFjBhY7cA8S5DAUWbDsvdXjdaoRFkGWpfWVsPPKHkOtzwD%2BqkMn%2BqiPgpx4ip6ysOKtY%2BomIQ2HzIsTLFYQVZqr0SLaO9p6FqUcc9L2UxuKqujRg0ElCY9CXqU47bIGSgERNGsWgY07xdSFice5ErJai%2Bj7NMPZVZ8sOmEnB2mXE3M0RfMJ%2Bl97wGOqUBfGRA4MKpqJpjFMSaf0fDl8JaD%2FekbPwxA%2FqwPfQumRAChLxndNOhcVMBDMUSVrZgK200BpgqI01uzlndt8xthKcKcTGKg5PpGdePZfgE7Fk8qnk9igkOKl8iw1ee5fQ%2FYm%2FyErSDhCyOAi3v%2Fjyv9Zc1OalI46XdLdr%2FNU5E0jLRpNTFaigNSx6CEEFwP8LgaG%2F73tOjwUtsnRyMEliTLRgdrcBu&X-Amz-Signature=0d081c0e619a487d2d038e160a9b407c8b1d580b635fe31a5accee7a19d2edbb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MGHB4IX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCssrvb8YwlZCu0VfZt9cku5mbXRg0%2FzdgJrllt5XWVxAIgdIrq5lqaB4oHAlQxunfZOjl0%2BOFWAWgtCNe1oQK7luAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQA3%2FBuCI5GAA7X5SrcA14Ik3qIA6WDjGLXUXLLAZ%2BEyxccp9ZleGIFvsBIfmYEWScvUN8%2Fliqt1dvIp0ES0OnVu%2BVKXHbclo7xfpOAfbUptY492qpibHNVpZzo2IXhOwTBwy7wxOOUEDOYuh7DTAtfLW0p44vJs%2F4%2BvNqGlmh67Uf%2BPLiisH8RG32u6gXTpJs9RwaHLMZXip0Fr%2FP1THKDJzY0WOmlWTmNTNbIueVSmAWN16S%2Bj%2F0ShoGtZ34XsEGfwVPIN%2FefMd3eNX9zSR9oVO%2FYqX4l7OWeU9UjSP4DJpezs8yK8lQCJ7uJEN7DGZSVpqK%2BsWUt62qzIdjPBDuWAfWTNr2Y0RiMahMPqxq8JcAUWqHwgYIht%2BaNuWbLaVm7DJqt%2BPg3%2B2OGxg5iapWMK0%2FlJmprfngsg%2Bqah19SH6jLfP5NRSjg%2B1Nnp3nN06RpIDWF3%2BIi8wq6Cn808p20%2B0Bz1VluFjBhY7cA8S5DAUWbDsvdXjdaoRFkGWpfWVsPPKHkOtzwD%2BqkMn%2BqiPgpx4ip6ysOKtY%2BomIQ2HzIsTLFYQVZqr0SLaO9p6FqUcc9L2UxuKqujRg0ElCY9CXqU47bIGSgERNGsWgY07xdSFice5ErJai%2Bj7NMPZVZ8sOmEnB2mXE3M0RfMJ%2Bl97wGOqUBfGRA4MKpqJpjFMSaf0fDl8JaD%2FekbPwxA%2FqwPfQumRAChLxndNOhcVMBDMUSVrZgK200BpgqI01uzlndt8xthKcKcTGKg5PpGdePZfgE7Fk8qnk9igkOKl8iw1ee5fQ%2FYm%2FyErSDhCyOAi3v%2Fjyv9Zc1OalI46XdLdr%2FNU5E0jLRpNTFaigNSx6CEEFwP8LgaG%2F73tOjwUtsnRyMEliTLRgdrcBu&X-Amz-Signature=d08c3d804f9b84e762abc8365b000865ae4cbc614c63eb5049c218228b3dd6ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MGHB4IX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCssrvb8YwlZCu0VfZt9cku5mbXRg0%2FzdgJrllt5XWVxAIgdIrq5lqaB4oHAlQxunfZOjl0%2BOFWAWgtCNe1oQK7luAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQA3%2FBuCI5GAA7X5SrcA14Ik3qIA6WDjGLXUXLLAZ%2BEyxccp9ZleGIFvsBIfmYEWScvUN8%2Fliqt1dvIp0ES0OnVu%2BVKXHbclo7xfpOAfbUptY492qpibHNVpZzo2IXhOwTBwy7wxOOUEDOYuh7DTAtfLW0p44vJs%2F4%2BvNqGlmh67Uf%2BPLiisH8RG32u6gXTpJs9RwaHLMZXip0Fr%2FP1THKDJzY0WOmlWTmNTNbIueVSmAWN16S%2Bj%2F0ShoGtZ34XsEGfwVPIN%2FefMd3eNX9zSR9oVO%2FYqX4l7OWeU9UjSP4DJpezs8yK8lQCJ7uJEN7DGZSVpqK%2BsWUt62qzIdjPBDuWAfWTNr2Y0RiMahMPqxq8JcAUWqHwgYIht%2BaNuWbLaVm7DJqt%2BPg3%2B2OGxg5iapWMK0%2FlJmprfngsg%2Bqah19SH6jLfP5NRSjg%2B1Nnp3nN06RpIDWF3%2BIi8wq6Cn808p20%2B0Bz1VluFjBhY7cA8S5DAUWbDsvdXjdaoRFkGWpfWVsPPKHkOtzwD%2BqkMn%2BqiPgpx4ip6ysOKtY%2BomIQ2HzIsTLFYQVZqr0SLaO9p6FqUcc9L2UxuKqujRg0ElCY9CXqU47bIGSgERNGsWgY07xdSFice5ErJai%2Bj7NMPZVZ8sOmEnB2mXE3M0RfMJ%2Bl97wGOqUBfGRA4MKpqJpjFMSaf0fDl8JaD%2FekbPwxA%2FqwPfQumRAChLxndNOhcVMBDMUSVrZgK200BpgqI01uzlndt8xthKcKcTGKg5PpGdePZfgE7Fk8qnk9igkOKl8iw1ee5fQ%2FYm%2FyErSDhCyOAi3v%2Fjyv9Zc1OalI46XdLdr%2FNU5E0jLRpNTFaigNSx6CEEFwP8LgaG%2F73tOjwUtsnRyMEliTLRgdrcBu&X-Amz-Signature=b2ee914a95b7325327fd145e47973ef3dd03c9f64ccafd9cdc4451d79023d06f&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NJ3XBJX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXhIjdzdU04cXctNYeeD0AJMFQVm3wOBf0NzK%2F%2Fq5AHwIhAO52TIAuPMjn4EvY0Tk61ulw9%2F5j%2B0YpsnLeLiZ9i2LtKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzPM%2BjYigltNXEDl3sq3AMpyV5toFovxBdNfzrFslqkIbLuWSaZxY8UoDHi99d%2BlFCO%2F6eWm%2F0c3xMk%2Bi2F6nl3d1uUG1ifMeKYriGMoGZaOd9mi6iyJRu4XumreknJj5jCob0sJFbd3E6xZ3TadUUR2I4QNkA0pyr%2FIs5d23ZvEevhTpEX5OCcx%2Bi4Vb5hxMFCVOm1bY67c7hoHTBgC3KggBEYY4fmrEdU5ERYp7K1LwNBqIf7%2BLfqF238VEHmIa%2FOzTeA79UdvN9xv36%2FaOL%2FwI4mev8TAgCJcFD5L%2Bqhl7yqtpI3AbfoZdDEBBpkcjCBRJtJoglJjXnqmkyYisBd1uqvRJYwd6%2F6Jk%2BD7dkMHq%2BrWkh%2Bg2Mn4LXVmsXn586newovHaRPMqV9LMUmwUzgENvELUyc%2BtBWPG6PKbZOT82Wx%2FFnjasCH1Z3BocN8n%2Bqva%2FkB9egogDrdRWDfK4USvadGdrSgyFpUEu2knqL8kw2k5cj5tK4WNi9aCWKnct81LkZyXTdc0MNTOaYT6wvmFx5DNZHEqiuT7UKQUXj2GrgZOUHyCw4Q0pjkTh6zvoPALLzd2H0oE16c1LEvGpyg2mrcEDQ1oji7fd18yblSKPdzXX1oE06usgjkiOY92GowiR3Q4Zhxl109zCApfe8BjqkAeqNWaJhn%2B93B4kqAI8Ha%2FCB3uqAHSUZtFkzCrUc6sbutzy%2FBY5q9UW%2F0ZwJxZoo3jQpbanqx7iIaRBQS7ovRH9os1rFhIYNszL%2B%2B%2FMV3Yz3lEfdo60tIiNF%2BAr4A%2FZhbk6ZgMOS1F0P6oUpsqAc72lBZFOH1pistKxzW%2FFqWWpOnPjITivd5lQmNmoRXqTb9fw2JplK1Lf%2F1BpP8yj6%2BtW7s%2BLs&X-Amz-Signature=d41a506f9e6bc6db27113e3da6f35ca5b3161231f6d16dcb9e870217a22e2b75&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NJ3XBJX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXhIjdzdU04cXctNYeeD0AJMFQVm3wOBf0NzK%2F%2Fq5AHwIhAO52TIAuPMjn4EvY0Tk61ulw9%2F5j%2B0YpsnLeLiZ9i2LtKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzPM%2BjYigltNXEDl3sq3AMpyV5toFovxBdNfzrFslqkIbLuWSaZxY8UoDHi99d%2BlFCO%2F6eWm%2F0c3xMk%2Bi2F6nl3d1uUG1ifMeKYriGMoGZaOd9mi6iyJRu4XumreknJj5jCob0sJFbd3E6xZ3TadUUR2I4QNkA0pyr%2FIs5d23ZvEevhTpEX5OCcx%2Bi4Vb5hxMFCVOm1bY67c7hoHTBgC3KggBEYY4fmrEdU5ERYp7K1LwNBqIf7%2BLfqF238VEHmIa%2FOzTeA79UdvN9xv36%2FaOL%2FwI4mev8TAgCJcFD5L%2Bqhl7yqtpI3AbfoZdDEBBpkcjCBRJtJoglJjXnqmkyYisBd1uqvRJYwd6%2F6Jk%2BD7dkMHq%2BrWkh%2Bg2Mn4LXVmsXn586newovHaRPMqV9LMUmwUzgENvELUyc%2BtBWPG6PKbZOT82Wx%2FFnjasCH1Z3BocN8n%2Bqva%2FkB9egogDrdRWDfK4USvadGdrSgyFpUEu2knqL8kw2k5cj5tK4WNi9aCWKnct81LkZyXTdc0MNTOaYT6wvmFx5DNZHEqiuT7UKQUXj2GrgZOUHyCw4Q0pjkTh6zvoPALLzd2H0oE16c1LEvGpyg2mrcEDQ1oji7fd18yblSKPdzXX1oE06usgjkiOY92GowiR3Q4Zhxl109zCApfe8BjqkAeqNWaJhn%2B93B4kqAI8Ha%2FCB3uqAHSUZtFkzCrUc6sbutzy%2FBY5q9UW%2F0ZwJxZoo3jQpbanqx7iIaRBQS7ovRH9os1rFhIYNszL%2B%2B%2FMV3Yz3lEfdo60tIiNF%2BAr4A%2FZhbk6ZgMOS1F0P6oUpsqAc72lBZFOH1pistKxzW%2FFqWWpOnPjITivd5lQmNmoRXqTb9fw2JplK1Lf%2F1BpP8yj6%2BtW7s%2BLs&X-Amz-Signature=64365ef894a3c1c71b4333c6885b2a5e385c53077ea645db5dc8f6c39c2eae88&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MGHB4IX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCssrvb8YwlZCu0VfZt9cku5mbXRg0%2FzdgJrllt5XWVxAIgdIrq5lqaB4oHAlQxunfZOjl0%2BOFWAWgtCNe1oQK7luAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQA3%2FBuCI5GAA7X5SrcA14Ik3qIA6WDjGLXUXLLAZ%2BEyxccp9ZleGIFvsBIfmYEWScvUN8%2Fliqt1dvIp0ES0OnVu%2BVKXHbclo7xfpOAfbUptY492qpibHNVpZzo2IXhOwTBwy7wxOOUEDOYuh7DTAtfLW0p44vJs%2F4%2BvNqGlmh67Uf%2BPLiisH8RG32u6gXTpJs9RwaHLMZXip0Fr%2FP1THKDJzY0WOmlWTmNTNbIueVSmAWN16S%2Bj%2F0ShoGtZ34XsEGfwVPIN%2FefMd3eNX9zSR9oVO%2FYqX4l7OWeU9UjSP4DJpezs8yK8lQCJ7uJEN7DGZSVpqK%2BsWUt62qzIdjPBDuWAfWTNr2Y0RiMahMPqxq8JcAUWqHwgYIht%2BaNuWbLaVm7DJqt%2BPg3%2B2OGxg5iapWMK0%2FlJmprfngsg%2Bqah19SH6jLfP5NRSjg%2B1Nnp3nN06RpIDWF3%2BIi8wq6Cn808p20%2B0Bz1VluFjBhY7cA8S5DAUWbDsvdXjdaoRFkGWpfWVsPPKHkOtzwD%2BqkMn%2BqiPgpx4ip6ysOKtY%2BomIQ2HzIsTLFYQVZqr0SLaO9p6FqUcc9L2UxuKqujRg0ElCY9CXqU47bIGSgERNGsWgY07xdSFice5ErJai%2Bj7NMPZVZ8sOmEnB2mXE3M0RfMJ%2Bl97wGOqUBfGRA4MKpqJpjFMSaf0fDl8JaD%2FekbPwxA%2FqwPfQumRAChLxndNOhcVMBDMUSVrZgK200BpgqI01uzlndt8xthKcKcTGKg5PpGdePZfgE7Fk8qnk9igkOKl8iw1ee5fQ%2FYm%2FyErSDhCyOAi3v%2Fjyv9Zc1OalI46XdLdr%2FNU5E0jLRpNTFaigNSx6CEEFwP8LgaG%2F73tOjwUtsnRyMEliTLRgdrcBu&X-Amz-Signature=3a7a3d7030d4a396cd15508ff3a7e1939ac2839cd5f3127cc22723d1dada1be8&X-Amz-SignedHeaders=host&x-id=GetObject)
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