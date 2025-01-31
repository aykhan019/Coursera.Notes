

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT7UOYVB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKVLu44fRkO%2F3sR%2FMnUGN6h31pl%2FLl%2FPdyyGBqyMpTTQIhAKx3TUBpuUNaJjh1aqUd2%2BdQIM4sGROFNt5c4rG%2ByKvFKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy65klgZvXbI01g0SIq3AP26j%2FF3PYhYgEwvwMZPPJ%2BJfjyiCbtqM2ojx3NJkaRlDsUgP4b0wgLmt4kDFSuli%2BPw%2FRC%2F%2FX01vkopbvF3qlyNLJdPPzMXyxh%2FEepWmD3SzeysPIimCcK%2FORBtitLO6tAvEPf2vxKBqyIXgubyLdTyCoI7CHjs0s4wnmpicGNL%2BzIKupMEk9WzHgbP5CmuUovZvoo8BwnMsaSIR4TkDh7OzBzG3dZIjBtF%2Fhy2X2Ys8NpqBY8ROk39QmlgZ0owtTH9glowOSQOYPPWh3sIgEpBfFAfAVmX1CqzObZsH%2BZhf7lWoc8ckA6FrilBUMkJ%2Bf31IwuWJq6Ivfxm0Zts0Fm%2FmFw%2B5kI9U0Oy%2FUIrlLgUTlsaT7eOBL8YhLjq7X3fxyl7nPsXDexeTocu3ess%2BhK9eMfeogYSLQI0bxrBNUwt9RA8GFjFwi5vQtOmBiXEvGAn1Ldjky4v78dSahg7rcpAIhULhcxRfBWKfZyeuyqEBQ6LrOR4MXaXadpjt4V4KyWWQPGWBwpv3Ol9cx5GfF84RJT2Mw5C%2FeJ3KZfq0HGXfI3BLxw3xHFnggwEyQOWxfd%2BLvyUdsTPXxIULocjwmaVjE9fjyYcE4tt3mJA%2FsN2gw6%2FTsur%2BZXMllSQTDQ8%2FK8BjqkAatDCv8DRtEG%2B5%2FAijaH0zvZ7G05wROwKENjZhKvR9f5oIbMGx1Fi0dx8DLt8LQ2O475BJ62%2Bj2fr5IEZILUIsGImPk%2BK9IycvEn1EMGeQP8xPTXlM%2Fu1Ig6akwO8cMrKszKpdGu5yTLGCIxNuiYhnuArra0vAMd7QGkcJQTzO8tS2RTmGsxr%2FEBmUEIkt9kEqTTOMrwq9SZB3fRUinFbuiGBx5t&X-Amz-Signature=1d49ec2ebcf5bb2fb56d79755cf78414d23478b6fec147c07aa9bfc15814f40b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT7UOYVB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKVLu44fRkO%2F3sR%2FMnUGN6h31pl%2FLl%2FPdyyGBqyMpTTQIhAKx3TUBpuUNaJjh1aqUd2%2BdQIM4sGROFNt5c4rG%2ByKvFKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy65klgZvXbI01g0SIq3AP26j%2FF3PYhYgEwvwMZPPJ%2BJfjyiCbtqM2ojx3NJkaRlDsUgP4b0wgLmt4kDFSuli%2BPw%2FRC%2F%2FX01vkopbvF3qlyNLJdPPzMXyxh%2FEepWmD3SzeysPIimCcK%2FORBtitLO6tAvEPf2vxKBqyIXgubyLdTyCoI7CHjs0s4wnmpicGNL%2BzIKupMEk9WzHgbP5CmuUovZvoo8BwnMsaSIR4TkDh7OzBzG3dZIjBtF%2Fhy2X2Ys8NpqBY8ROk39QmlgZ0owtTH9glowOSQOYPPWh3sIgEpBfFAfAVmX1CqzObZsH%2BZhf7lWoc8ckA6FrilBUMkJ%2Bf31IwuWJq6Ivfxm0Zts0Fm%2FmFw%2B5kI9U0Oy%2FUIrlLgUTlsaT7eOBL8YhLjq7X3fxyl7nPsXDexeTocu3ess%2BhK9eMfeogYSLQI0bxrBNUwt9RA8GFjFwi5vQtOmBiXEvGAn1Ldjky4v78dSahg7rcpAIhULhcxRfBWKfZyeuyqEBQ6LrOR4MXaXadpjt4V4KyWWQPGWBwpv3Ol9cx5GfF84RJT2Mw5C%2FeJ3KZfq0HGXfI3BLxw3xHFnggwEyQOWxfd%2BLvyUdsTPXxIULocjwmaVjE9fjyYcE4tt3mJA%2FsN2gw6%2FTsur%2BZXMllSQTDQ8%2FK8BjqkAatDCv8DRtEG%2B5%2FAijaH0zvZ7G05wROwKENjZhKvR9f5oIbMGx1Fi0dx8DLt8LQ2O475BJ62%2Bj2fr5IEZILUIsGImPk%2BK9IycvEn1EMGeQP8xPTXlM%2Fu1Ig6akwO8cMrKszKpdGu5yTLGCIxNuiYhnuArra0vAMd7QGkcJQTzO8tS2RTmGsxr%2FEBmUEIkt9kEqTTOMrwq9SZB3fRUinFbuiGBx5t&X-Amz-Signature=f9e3c69f1e059c886a0e44eeafac8bbe6b18e957628438f8b736273b3846f835&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT7UOYVB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKVLu44fRkO%2F3sR%2FMnUGN6h31pl%2FLl%2FPdyyGBqyMpTTQIhAKx3TUBpuUNaJjh1aqUd2%2BdQIM4sGROFNt5c4rG%2ByKvFKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy65klgZvXbI01g0SIq3AP26j%2FF3PYhYgEwvwMZPPJ%2BJfjyiCbtqM2ojx3NJkaRlDsUgP4b0wgLmt4kDFSuli%2BPw%2FRC%2F%2FX01vkopbvF3qlyNLJdPPzMXyxh%2FEepWmD3SzeysPIimCcK%2FORBtitLO6tAvEPf2vxKBqyIXgubyLdTyCoI7CHjs0s4wnmpicGNL%2BzIKupMEk9WzHgbP5CmuUovZvoo8BwnMsaSIR4TkDh7OzBzG3dZIjBtF%2Fhy2X2Ys8NpqBY8ROk39QmlgZ0owtTH9glowOSQOYPPWh3sIgEpBfFAfAVmX1CqzObZsH%2BZhf7lWoc8ckA6FrilBUMkJ%2Bf31IwuWJq6Ivfxm0Zts0Fm%2FmFw%2B5kI9U0Oy%2FUIrlLgUTlsaT7eOBL8YhLjq7X3fxyl7nPsXDexeTocu3ess%2BhK9eMfeogYSLQI0bxrBNUwt9RA8GFjFwi5vQtOmBiXEvGAn1Ldjky4v78dSahg7rcpAIhULhcxRfBWKfZyeuyqEBQ6LrOR4MXaXadpjt4V4KyWWQPGWBwpv3Ol9cx5GfF84RJT2Mw5C%2FeJ3KZfq0HGXfI3BLxw3xHFnggwEyQOWxfd%2BLvyUdsTPXxIULocjwmaVjE9fjyYcE4tt3mJA%2FsN2gw6%2FTsur%2BZXMllSQTDQ8%2FK8BjqkAatDCv8DRtEG%2B5%2FAijaH0zvZ7G05wROwKENjZhKvR9f5oIbMGx1Fi0dx8DLt8LQ2O475BJ62%2Bj2fr5IEZILUIsGImPk%2BK9IycvEn1EMGeQP8xPTXlM%2Fu1Ig6akwO8cMrKszKpdGu5yTLGCIxNuiYhnuArra0vAMd7QGkcJQTzO8tS2RTmGsxr%2FEBmUEIkt9kEqTTOMrwq9SZB3fRUinFbuiGBx5t&X-Amz-Signature=8cc693ab992eb7904bd62fc816e9d105b2fc33c8e56fe69a76532c2e51e42185&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKIUDQDV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALlPuSsjf6RzNFF%2F2Y7xxKfvwr%2FTBew9%2BGGcRBbhd7hAiEAiwHBHDOCXnaEnAwcvZZcJ0l3G1NnAel1yLfn%2BGQl8ZMqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADuJVsRwZNelVgtSCrcA4b9XIPYK8IrLQXwUcf2Ytyz4dsdrMFQ%2BT5aHLk0j8vPL2enuNBto5ilaPzVeyBVaZVFpL7MOdhNVPNOV4myhSPD7sSoaTtCVoxRsZqBBXBNgARxkNuwvqjyj82iKYLfGbfyGP4kuHwopf1YmeDlX3txwES7wcFNN2qmhjXkO%2B%2FXqbUmYy%2B0CcV1KTcJfaWSrQRFKPMbAKCKm%2BMduoHf5rSZXANrVPqY%2BGKT3Kj2mwMXFwYpibo4s4u%2BvfFG%2BTtKp49JmV8RPY7wUNp5tftj5Z%2Fg9syegtkn6p8yiOagulXgzbzJV%2BmqnBL0VMNYppVuNAdGYtwlTolNPytThtmKcJuFXDwdcx%2FXC5nb5lczoN4gfCVS7xdpuVQRNHpM2hozPNPpV8mP%2FtxkqPnPR15Nh1lqhlOBK0SZ5mOwJMkbPfBXSVNxXeSqfefCFaayn1ts9PS8VHRkDZFUKfU9j%2Fxt5fQw4%2FjiKphqR7D6LAHUV4lymNxiUB1ynqhHsqE696Ea8S8JySyZ3ctx%2FlTmD2%2FK5SQVKLyP2bKqIv4OR10se7y7gAAPJkm7411Ady%2BwjFlpBbcmeNd0WWFBCs0aZt%2BPDf2smdSyjR3KwPWGGkiMZhP2R2Nkbk7dBqzCP1OnMMnz8rwGOqUBB76xNHyNb8SA9sw%2FMpoZR26LAchLpGVGo%2FoVkoP52KEfh7MKdBecBPMkwxjVh0rB%2BK4skvFbMkhYximT2qp%2FOAnGLsUFa6QtqSkDlC5ZE6zklULjt96OptDguO05I7DAo57Mw9iJU9ztOhZbwrO%2FRNMwNY21Q1NG%2F0jg3IQBNcH4SqYoQs2BugOurFfbOkgulF3xM21YlRBg4MTg8oKg%2BM%2B8eBr%2B&X-Amz-Signature=e7f0b84c58024bff1724a51aca39da550215d68e3a8c77c1d3afa96f0ff6e301&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKIUDQDV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALlPuSsjf6RzNFF%2F2Y7xxKfvwr%2FTBew9%2BGGcRBbhd7hAiEAiwHBHDOCXnaEnAwcvZZcJ0l3G1NnAel1yLfn%2BGQl8ZMqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADuJVsRwZNelVgtSCrcA4b9XIPYK8IrLQXwUcf2Ytyz4dsdrMFQ%2BT5aHLk0j8vPL2enuNBto5ilaPzVeyBVaZVFpL7MOdhNVPNOV4myhSPD7sSoaTtCVoxRsZqBBXBNgARxkNuwvqjyj82iKYLfGbfyGP4kuHwopf1YmeDlX3txwES7wcFNN2qmhjXkO%2B%2FXqbUmYy%2B0CcV1KTcJfaWSrQRFKPMbAKCKm%2BMduoHf5rSZXANrVPqY%2BGKT3Kj2mwMXFwYpibo4s4u%2BvfFG%2BTtKp49JmV8RPY7wUNp5tftj5Z%2Fg9syegtkn6p8yiOagulXgzbzJV%2BmqnBL0VMNYppVuNAdGYtwlTolNPytThtmKcJuFXDwdcx%2FXC5nb5lczoN4gfCVS7xdpuVQRNHpM2hozPNPpV8mP%2FtxkqPnPR15Nh1lqhlOBK0SZ5mOwJMkbPfBXSVNxXeSqfefCFaayn1ts9PS8VHRkDZFUKfU9j%2Fxt5fQw4%2FjiKphqR7D6LAHUV4lymNxiUB1ynqhHsqE696Ea8S8JySyZ3ctx%2FlTmD2%2FK5SQVKLyP2bKqIv4OR10se7y7gAAPJkm7411Ady%2BwjFlpBbcmeNd0WWFBCs0aZt%2BPDf2smdSyjR3KwPWGGkiMZhP2R2Nkbk7dBqzCP1OnMMnz8rwGOqUBB76xNHyNb8SA9sw%2FMpoZR26LAchLpGVGo%2FoVkoP52KEfh7MKdBecBPMkwxjVh0rB%2BK4skvFbMkhYximT2qp%2FOAnGLsUFa6QtqSkDlC5ZE6zklULjt96OptDguO05I7DAo57Mw9iJU9ztOhZbwrO%2FRNMwNY21Q1NG%2F0jg3IQBNcH4SqYoQs2BugOurFfbOkgulF3xM21YlRBg4MTg8oKg%2BM%2B8eBr%2B&X-Amz-Signature=f7d9caec741a696efaf840086b47f71ea7d81e6dd67b8e588de480729b46859d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT7UOYVB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKVLu44fRkO%2F3sR%2FMnUGN6h31pl%2FLl%2FPdyyGBqyMpTTQIhAKx3TUBpuUNaJjh1aqUd2%2BdQIM4sGROFNt5c4rG%2ByKvFKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy65klgZvXbI01g0SIq3AP26j%2FF3PYhYgEwvwMZPPJ%2BJfjyiCbtqM2ojx3NJkaRlDsUgP4b0wgLmt4kDFSuli%2BPw%2FRC%2F%2FX01vkopbvF3qlyNLJdPPzMXyxh%2FEepWmD3SzeysPIimCcK%2FORBtitLO6tAvEPf2vxKBqyIXgubyLdTyCoI7CHjs0s4wnmpicGNL%2BzIKupMEk9WzHgbP5CmuUovZvoo8BwnMsaSIR4TkDh7OzBzG3dZIjBtF%2Fhy2X2Ys8NpqBY8ROk39QmlgZ0owtTH9glowOSQOYPPWh3sIgEpBfFAfAVmX1CqzObZsH%2BZhf7lWoc8ckA6FrilBUMkJ%2Bf31IwuWJq6Ivfxm0Zts0Fm%2FmFw%2B5kI9U0Oy%2FUIrlLgUTlsaT7eOBL8YhLjq7X3fxyl7nPsXDexeTocu3ess%2BhK9eMfeogYSLQI0bxrBNUwt9RA8GFjFwi5vQtOmBiXEvGAn1Ldjky4v78dSahg7rcpAIhULhcxRfBWKfZyeuyqEBQ6LrOR4MXaXadpjt4V4KyWWQPGWBwpv3Ol9cx5GfF84RJT2Mw5C%2FeJ3KZfq0HGXfI3BLxw3xHFnggwEyQOWxfd%2BLvyUdsTPXxIULocjwmaVjE9fjyYcE4tt3mJA%2FsN2gw6%2FTsur%2BZXMllSQTDQ8%2FK8BjqkAatDCv8DRtEG%2B5%2FAijaH0zvZ7G05wROwKENjZhKvR9f5oIbMGx1Fi0dx8DLt8LQ2O475BJ62%2Bj2fr5IEZILUIsGImPk%2BK9IycvEn1EMGeQP8xPTXlM%2Fu1Ig6akwO8cMrKszKpdGu5yTLGCIxNuiYhnuArra0vAMd7QGkcJQTzO8tS2RTmGsxr%2FEBmUEIkt9kEqTTOMrwq9SZB3fRUinFbuiGBx5t&X-Amz-Signature=50a9bb4231445b5c59fd56aa67903ed9f6cb1df0baa447556dfc7de2ac5e5a1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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