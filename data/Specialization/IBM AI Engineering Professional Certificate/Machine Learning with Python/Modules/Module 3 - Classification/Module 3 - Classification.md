

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3YNPVNL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHveA7E1aCWUeVODnneP9skQFRKlw82tqeKCmXNW0ExGAiBKPClnzj1egjsZjCW3LqqrlpFR2WEjDR%2BYI0U%2BAfukXCqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8gh3b9tpR5BXkaIhKtwDvWwLLkhjNWafVOGgWhXNx2RuhZwdg1qC5Y%2FJOyvTJ85z7w5lUci8uC29lGpFODjO2mas3hG9erM7eDQiEDtZR8qR3OrX%2ByXUZnGOQhkdO%2B1kBSxIytceNtRwFT9ov5Aa7tQtMLRAE%2BbaZpRjqDmjotxiNeuiRWlMAcaDxaO048X0PcQyzAJi9WU917q7fvTSNpKXD3%2FuDW2%2FvT7a%2BnXHNEnjTkM9osKigUakGFEj%2BS55%2BlxaVUtdbs%2ByGsce3yY6SO%2BoRkHsQ42AqM56t0g9IcGlG6YHvvIzeplF5ENdM%2BH7Tj3f7z6OgNmJkS%2Bjm90veHq5rfoBxDEMI4ee7c2%2FkaCGp09Q1Kyyg9JF33jcFFwikhLdePAgHDE8eQ%2FTvRnW%2FdGUwKXhvq4lCDkLPgw5B8WieUZP9y0BcnK%2BPziZn6n2KwTOiCX%2Fh%2FVAeGti7Wv%2FQt14tgRcqhxryTeoSbBQ0dEO%2BLNVvKSpuhvyR5tggTWbyw1QIuRZmdIxguzPWFcaSFwqrts0DL2Ky8JiYTsECuvgrhrcewSHb1n6PCWNhvkwUTCDLCGXy5Jqj%2FSbN%2FCi%2BAMaMZMmtlDPqWHhYEmvHh9d%2Bb%2Fkd8MMtxjDoSIV8Xv3T5JbbdZEvh6%2FRj8w7cXqvAY6pgGzCbmyo7mUf2BOXa7HZDn6BT%2Fa3lOvjc0TDkfZZQpnseddRwvzudheZR6cspgbOOehbi8ihIMJZjiSQ2l6kCZM88RfvKDpZS1LKjz5rZ53Rt9DjV4YXOHfcS7JQpFW4ObWcQtO61O8hcS4lvdRbhsHRK2lTS6kcTfQTPV01SHS8whM2nn%2Fq6z0xrmsy9R%2BbqSYxHbaEYxf9NdQRc4H51qPha0ymt1z&X-Amz-Signature=f7b232c6ae78b37fe336e5c2117b931d269d779ef6a34d54df1f9334fd38deec&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3YNPVNL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHveA7E1aCWUeVODnneP9skQFRKlw82tqeKCmXNW0ExGAiBKPClnzj1egjsZjCW3LqqrlpFR2WEjDR%2BYI0U%2BAfukXCqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8gh3b9tpR5BXkaIhKtwDvWwLLkhjNWafVOGgWhXNx2RuhZwdg1qC5Y%2FJOyvTJ85z7w5lUci8uC29lGpFODjO2mas3hG9erM7eDQiEDtZR8qR3OrX%2ByXUZnGOQhkdO%2B1kBSxIytceNtRwFT9ov5Aa7tQtMLRAE%2BbaZpRjqDmjotxiNeuiRWlMAcaDxaO048X0PcQyzAJi9WU917q7fvTSNpKXD3%2FuDW2%2FvT7a%2BnXHNEnjTkM9osKigUakGFEj%2BS55%2BlxaVUtdbs%2ByGsce3yY6SO%2BoRkHsQ42AqM56t0g9IcGlG6YHvvIzeplF5ENdM%2BH7Tj3f7z6OgNmJkS%2Bjm90veHq5rfoBxDEMI4ee7c2%2FkaCGp09Q1Kyyg9JF33jcFFwikhLdePAgHDE8eQ%2FTvRnW%2FdGUwKXhvq4lCDkLPgw5B8WieUZP9y0BcnK%2BPziZn6n2KwTOiCX%2Fh%2FVAeGti7Wv%2FQt14tgRcqhxryTeoSbBQ0dEO%2BLNVvKSpuhvyR5tggTWbyw1QIuRZmdIxguzPWFcaSFwqrts0DL2Ky8JiYTsECuvgrhrcewSHb1n6PCWNhvkwUTCDLCGXy5Jqj%2FSbN%2FCi%2BAMaMZMmtlDPqWHhYEmvHh9d%2Bb%2Fkd8MMtxjDoSIV8Xv3T5JbbdZEvh6%2FRj8w7cXqvAY6pgGzCbmyo7mUf2BOXa7HZDn6BT%2Fa3lOvjc0TDkfZZQpnseddRwvzudheZR6cspgbOOehbi8ihIMJZjiSQ2l6kCZM88RfvKDpZS1LKjz5rZ53Rt9DjV4YXOHfcS7JQpFW4ObWcQtO61O8hcS4lvdRbhsHRK2lTS6kcTfQTPV01SHS8whM2nn%2Fq6z0xrmsy9R%2BbqSYxHbaEYxf9NdQRc4H51qPha0ymt1z&X-Amz-Signature=7795c8211fe816d29d9bf8f65a8fdc4b1e91da279c8c5a29d0b09e63fbdd7876&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3YNPVNL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHveA7E1aCWUeVODnneP9skQFRKlw82tqeKCmXNW0ExGAiBKPClnzj1egjsZjCW3LqqrlpFR2WEjDR%2BYI0U%2BAfukXCqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8gh3b9tpR5BXkaIhKtwDvWwLLkhjNWafVOGgWhXNx2RuhZwdg1qC5Y%2FJOyvTJ85z7w5lUci8uC29lGpFODjO2mas3hG9erM7eDQiEDtZR8qR3OrX%2ByXUZnGOQhkdO%2B1kBSxIytceNtRwFT9ov5Aa7tQtMLRAE%2BbaZpRjqDmjotxiNeuiRWlMAcaDxaO048X0PcQyzAJi9WU917q7fvTSNpKXD3%2FuDW2%2FvT7a%2BnXHNEnjTkM9osKigUakGFEj%2BS55%2BlxaVUtdbs%2ByGsce3yY6SO%2BoRkHsQ42AqM56t0g9IcGlG6YHvvIzeplF5ENdM%2BH7Tj3f7z6OgNmJkS%2Bjm90veHq5rfoBxDEMI4ee7c2%2FkaCGp09Q1Kyyg9JF33jcFFwikhLdePAgHDE8eQ%2FTvRnW%2FdGUwKXhvq4lCDkLPgw5B8WieUZP9y0BcnK%2BPziZn6n2KwTOiCX%2Fh%2FVAeGti7Wv%2FQt14tgRcqhxryTeoSbBQ0dEO%2BLNVvKSpuhvyR5tggTWbyw1QIuRZmdIxguzPWFcaSFwqrts0DL2Ky8JiYTsECuvgrhrcewSHb1n6PCWNhvkwUTCDLCGXy5Jqj%2FSbN%2FCi%2BAMaMZMmtlDPqWHhYEmvHh9d%2Bb%2Fkd8MMtxjDoSIV8Xv3T5JbbdZEvh6%2FRj8w7cXqvAY6pgGzCbmyo7mUf2BOXa7HZDn6BT%2Fa3lOvjc0TDkfZZQpnseddRwvzudheZR6cspgbOOehbi8ihIMJZjiSQ2l6kCZM88RfvKDpZS1LKjz5rZ53Rt9DjV4YXOHfcS7JQpFW4ObWcQtO61O8hcS4lvdRbhsHRK2lTS6kcTfQTPV01SHS8whM2nn%2Fq6z0xrmsy9R%2BbqSYxHbaEYxf9NdQRc4H51qPha0ymt1z&X-Amz-Signature=52410289c37af5991e69bdeb3579a6a6ab4dc2ebcc946c0c0adb284b1518ce16&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HW3QYB6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGpSzNUdlWvD0WpdBXYJKa50nfr4lT2ouWOkkK6Lb5KzAiEAjuiDw%2BXFIS%2BDWpq07h58otf3YzDFcysP6JNPDhsaSs0qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZQChyD04q0w%2B1CpSrcA7RhNQuc%2F5y9nXBA0f%2F4uJomXnI5Hh0yUn6MUNhLHi0iKlCqS4jVepBG19IxGKFIrNUERkGnrp3rYiibmEuhF1STFYknlwLcqPLGBxIPfdbmke%2BtGdddvkgeFvcJ3aDDcqe3Kc7bbuyMkcxrQEhE7Ihj3ZNYKw0wamCi2NrIGE0B%2BeYNcUMV4byAhDeh5kMf0I7NCC9IqKUTCr7i5tdZS1GM%2B9ycMLVMbo%2FwL313MULfw5srQ4NRBmXoloaPmw6UaAmJzWiPR7EoUlllVq7HMasAC2w%2B%2F2Zh0JzxEqsmgrMmYTzBW4Fm6D%2FLUAcDYjznFNcVROK8xih3aeQLj12YprKSFeu6XREjxwkhIiW28lPx0%2FivuwOq4CSYaMoQVOlG1lskptsMIVddw%2BFhm7fKYxV5w4uyrt9jSXbivZskivMj8IzFdzQQMLQBW9eyvxDNQ%2B02H71XekQLACfhrDCplESkOuwgZ%2FxNLoUsyZZkSbOeURluA9x%2BDOX%2FAmNzqLuJpI7z1%2FYbwHza728VPXz6H3SSmeDgDXWkw%2BpaRq%2B4SnvTAN9llHKpW2nBoTSY9E9f3sbJSRsqHSbMataK%2FaagD8ZDNx%2F9sr1Lg8Xcx%2BzPNqsdDe4BKWlQYRljj8RpMOHF6rwGOqUBKLkVqigBfSY8yn2pmYb5OVLKoLNH4e3CoBLFWUOpmd9nIwAmLNaX1aZy7KAOiKZbHpg9qnZO8KCxL2xlxMIDGq1lrb5qux3%2F3ONUxJ1wsAAmcYUtMBhRcQuSMBKL4RdYbz5YOj8VYaX%2B2nJ5bB2LR4oYlcIWtxgZrM2jd1pAhtlLQTR6WaHg6WxnbPSLA6jk7Q%2Bga0WnDzvO3DTgbM0AJD0VLHgb&X-Amz-Signature=dbf03c4f5519be8c51cc10a2f4109079c3a209e21e55fbcb289a7a3bb22b3adf&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HW3QYB6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGpSzNUdlWvD0WpdBXYJKa50nfr4lT2ouWOkkK6Lb5KzAiEAjuiDw%2BXFIS%2BDWpq07h58otf3YzDFcysP6JNPDhsaSs0qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAZQChyD04q0w%2B1CpSrcA7RhNQuc%2F5y9nXBA0f%2F4uJomXnI5Hh0yUn6MUNhLHi0iKlCqS4jVepBG19IxGKFIrNUERkGnrp3rYiibmEuhF1STFYknlwLcqPLGBxIPfdbmke%2BtGdddvkgeFvcJ3aDDcqe3Kc7bbuyMkcxrQEhE7Ihj3ZNYKw0wamCi2NrIGE0B%2BeYNcUMV4byAhDeh5kMf0I7NCC9IqKUTCr7i5tdZS1GM%2B9ycMLVMbo%2FwL313MULfw5srQ4NRBmXoloaPmw6UaAmJzWiPR7EoUlllVq7HMasAC2w%2B%2F2Zh0JzxEqsmgrMmYTzBW4Fm6D%2FLUAcDYjznFNcVROK8xih3aeQLj12YprKSFeu6XREjxwkhIiW28lPx0%2FivuwOq4CSYaMoQVOlG1lskptsMIVddw%2BFhm7fKYxV5w4uyrt9jSXbivZskivMj8IzFdzQQMLQBW9eyvxDNQ%2B02H71XekQLACfhrDCplESkOuwgZ%2FxNLoUsyZZkSbOeURluA9x%2BDOX%2FAmNzqLuJpI7z1%2FYbwHza728VPXz6H3SSmeDgDXWkw%2BpaRq%2B4SnvTAN9llHKpW2nBoTSY9E9f3sbJSRsqHSbMataK%2FaagD8ZDNx%2F9sr1Lg8Xcx%2BzPNqsdDe4BKWlQYRljj8RpMOHF6rwGOqUBKLkVqigBfSY8yn2pmYb5OVLKoLNH4e3CoBLFWUOpmd9nIwAmLNaX1aZy7KAOiKZbHpg9qnZO8KCxL2xlxMIDGq1lrb5qux3%2F3ONUxJ1wsAAmcYUtMBhRcQuSMBKL4RdYbz5YOj8VYaX%2B2nJ5bB2LR4oYlcIWtxgZrM2jd1pAhtlLQTR6WaHg6WxnbPSLA6jk7Q%2Bga0WnDzvO3DTgbM0AJD0VLHgb&X-Amz-Signature=181ec254d01dbd82347fbb248e248a75db1d09f44769cc49ae7822c11d6442fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3YNPVNL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHveA7E1aCWUeVODnneP9skQFRKlw82tqeKCmXNW0ExGAiBKPClnzj1egjsZjCW3LqqrlpFR2WEjDR%2BYI0U%2BAfukXCqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8gh3b9tpR5BXkaIhKtwDvWwLLkhjNWafVOGgWhXNx2RuhZwdg1qC5Y%2FJOyvTJ85z7w5lUci8uC29lGpFODjO2mas3hG9erM7eDQiEDtZR8qR3OrX%2ByXUZnGOQhkdO%2B1kBSxIytceNtRwFT9ov5Aa7tQtMLRAE%2BbaZpRjqDmjotxiNeuiRWlMAcaDxaO048X0PcQyzAJi9WU917q7fvTSNpKXD3%2FuDW2%2FvT7a%2BnXHNEnjTkM9osKigUakGFEj%2BS55%2BlxaVUtdbs%2ByGsce3yY6SO%2BoRkHsQ42AqM56t0g9IcGlG6YHvvIzeplF5ENdM%2BH7Tj3f7z6OgNmJkS%2Bjm90veHq5rfoBxDEMI4ee7c2%2FkaCGp09Q1Kyyg9JF33jcFFwikhLdePAgHDE8eQ%2FTvRnW%2FdGUwKXhvq4lCDkLPgw5B8WieUZP9y0BcnK%2BPziZn6n2KwTOiCX%2Fh%2FVAeGti7Wv%2FQt14tgRcqhxryTeoSbBQ0dEO%2BLNVvKSpuhvyR5tggTWbyw1QIuRZmdIxguzPWFcaSFwqrts0DL2Ky8JiYTsECuvgrhrcewSHb1n6PCWNhvkwUTCDLCGXy5Jqj%2FSbN%2FCi%2BAMaMZMmtlDPqWHhYEmvHh9d%2Bb%2Fkd8MMtxjDoSIV8Xv3T5JbbdZEvh6%2FRj8w7cXqvAY6pgGzCbmyo7mUf2BOXa7HZDn6BT%2Fa3lOvjc0TDkfZZQpnseddRwvzudheZR6cspgbOOehbi8ihIMJZjiSQ2l6kCZM88RfvKDpZS1LKjz5rZ53Rt9DjV4YXOHfcS7JQpFW4ObWcQtO61O8hcS4lvdRbhsHRK2lTS6kcTfQTPV01SHS8whM2nn%2Fq6z0xrmsy9R%2BbqSYxHbaEYxf9NdQRc4H51qPha0ymt1z&X-Amz-Signature=ea7dd3dc2e07feff45312b23b7b874b4f7098b35ebc9679dd6bbcf6077b3953b&X-Amz-SignedHeaders=host&x-id=GetObject)
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