

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4TDET3O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2F2Zx0IuCVUpP9mFl4O7n%2B5WkiM8WOVaBwQOG2RQ2eJAiB0R0ISX7%2FqLovdTardcnDIp68Cc3sZAlnkArbCb7X82ir%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMItO9MGCMPtvveS4AKtwDkMiQDvPcTEy0rUhdaD%2Fiemt7D0Uj7fkN4O7UxQyrX8T1%2F5197RwKG2x%2B8Z8r4xHA71i2fXooanEX9%2FALeReqa2irW68Kalw%2FjP9AsSqoQjNOfu8UYHGQsoHw4zoX98j3xKnUKtz%2BZo%2BkpeQ%2B7Ma8YTvYeBBnYtBVcEoIionILeTXLm5akVKTJtWVBb0tiG2pZNRW6Af%2B0NSNybDqZK5YAjGlzHvGkGMixiDTNuq9GpN9wiARNw4p9Hi8%2FyDHDkhhEMHaJWO2VbYPEabmoaf%2B9Xu6gffWDFKmO9SteuFaB0YNZy3IZ2jp3FbNmgUeI7dfBmpnGWozDHq%2Fjhx%2Fy%2FHehtCbzA9EBmxug%2BMf897E%2FsymnijQ7EPMtp0SG8NCBDylAqI1TM7iEwuAJBrwcQD%2B%2Fe5DOwJ48p2FkfaduYUeVYDASADxWiZ9l4pNCEMqIwAd%2FMsScqeJ1KOnhYMQD6UeRSyZWQfFVORKM9M92Lv2U8JQfOcRqnHhbxGyql3loAYu1Jd6Zj1Bdl6t%2BtnyCLdc51bXiHhgGqR8MSv%2B27Mh09GAr34c4CjspQ53de3999tshNvs%2BamYs5DINy58n8bmHw%2BJjCThIJVBIrENxBCjdCurosUqL4kIw9WPJVgw7NKCvQY6pgGG%2FlNu96qCF%2FOjdABGUdqaoEdvUeJbr6waHmzog52ywH8C4QOD%2FJgZat8YBvLtXarxEWLC2XCpDo076ttoTaI9TCT9voUa2Vqr0bUOthOcVT9GCJpBY1sN%2BFcJiknG2GtmxR9%2FsDUyZ0eUq7%2FZ2LALwXL0qfqQQmpYF7SFEf0VhvwmoBmD0KeBqKfpQtXA3MON5Jb2oGjZNVXtYEZOPs%2F9L%2FUM3PVt&X-Amz-Signature=3dc66f8f4b6bea371cc89396da06c694f790dcb9c30b8f93b22eb44231a28dc7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4TDET3O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2F2Zx0IuCVUpP9mFl4O7n%2B5WkiM8WOVaBwQOG2RQ2eJAiB0R0ISX7%2FqLovdTardcnDIp68Cc3sZAlnkArbCb7X82ir%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMItO9MGCMPtvveS4AKtwDkMiQDvPcTEy0rUhdaD%2Fiemt7D0Uj7fkN4O7UxQyrX8T1%2F5197RwKG2x%2B8Z8r4xHA71i2fXooanEX9%2FALeReqa2irW68Kalw%2FjP9AsSqoQjNOfu8UYHGQsoHw4zoX98j3xKnUKtz%2BZo%2BkpeQ%2B7Ma8YTvYeBBnYtBVcEoIionILeTXLm5akVKTJtWVBb0tiG2pZNRW6Af%2B0NSNybDqZK5YAjGlzHvGkGMixiDTNuq9GpN9wiARNw4p9Hi8%2FyDHDkhhEMHaJWO2VbYPEabmoaf%2B9Xu6gffWDFKmO9SteuFaB0YNZy3IZ2jp3FbNmgUeI7dfBmpnGWozDHq%2Fjhx%2Fy%2FHehtCbzA9EBmxug%2BMf897E%2FsymnijQ7EPMtp0SG8NCBDylAqI1TM7iEwuAJBrwcQD%2B%2Fe5DOwJ48p2FkfaduYUeVYDASADxWiZ9l4pNCEMqIwAd%2FMsScqeJ1KOnhYMQD6UeRSyZWQfFVORKM9M92Lv2U8JQfOcRqnHhbxGyql3loAYu1Jd6Zj1Bdl6t%2BtnyCLdc51bXiHhgGqR8MSv%2B27Mh09GAr34c4CjspQ53de3999tshNvs%2BamYs5DINy58n8bmHw%2BJjCThIJVBIrENxBCjdCurosUqL4kIw9WPJVgw7NKCvQY6pgGG%2FlNu96qCF%2FOjdABGUdqaoEdvUeJbr6waHmzog52ywH8C4QOD%2FJgZat8YBvLtXarxEWLC2XCpDo076ttoTaI9TCT9voUa2Vqr0bUOthOcVT9GCJpBY1sN%2BFcJiknG2GtmxR9%2FsDUyZ0eUq7%2FZ2LALwXL0qfqQQmpYF7SFEf0VhvwmoBmD0KeBqKfpQtXA3MON5Jb2oGjZNVXtYEZOPs%2F9L%2FUM3PVt&X-Amz-Signature=06f3df21b400a7f2b5beda054550ea37e7ef28572d9ddb34db6518c6f436bd31&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4TDET3O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2F2Zx0IuCVUpP9mFl4O7n%2B5WkiM8WOVaBwQOG2RQ2eJAiB0R0ISX7%2FqLovdTardcnDIp68Cc3sZAlnkArbCb7X82ir%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMItO9MGCMPtvveS4AKtwDkMiQDvPcTEy0rUhdaD%2Fiemt7D0Uj7fkN4O7UxQyrX8T1%2F5197RwKG2x%2B8Z8r4xHA71i2fXooanEX9%2FALeReqa2irW68Kalw%2FjP9AsSqoQjNOfu8UYHGQsoHw4zoX98j3xKnUKtz%2BZo%2BkpeQ%2B7Ma8YTvYeBBnYtBVcEoIionILeTXLm5akVKTJtWVBb0tiG2pZNRW6Af%2B0NSNybDqZK5YAjGlzHvGkGMixiDTNuq9GpN9wiARNw4p9Hi8%2FyDHDkhhEMHaJWO2VbYPEabmoaf%2B9Xu6gffWDFKmO9SteuFaB0YNZy3IZ2jp3FbNmgUeI7dfBmpnGWozDHq%2Fjhx%2Fy%2FHehtCbzA9EBmxug%2BMf897E%2FsymnijQ7EPMtp0SG8NCBDylAqI1TM7iEwuAJBrwcQD%2B%2Fe5DOwJ48p2FkfaduYUeVYDASADxWiZ9l4pNCEMqIwAd%2FMsScqeJ1KOnhYMQD6UeRSyZWQfFVORKM9M92Lv2U8JQfOcRqnHhbxGyql3loAYu1Jd6Zj1Bdl6t%2BtnyCLdc51bXiHhgGqR8MSv%2B27Mh09GAr34c4CjspQ53de3999tshNvs%2BamYs5DINy58n8bmHw%2BJjCThIJVBIrENxBCjdCurosUqL4kIw9WPJVgw7NKCvQY6pgGG%2FlNu96qCF%2FOjdABGUdqaoEdvUeJbr6waHmzog52ywH8C4QOD%2FJgZat8YBvLtXarxEWLC2XCpDo076ttoTaI9TCT9voUa2Vqr0bUOthOcVT9GCJpBY1sN%2BFcJiknG2GtmxR9%2FsDUyZ0eUq7%2FZ2LALwXL0qfqQQmpYF7SFEf0VhvwmoBmD0KeBqKfpQtXA3MON5Jb2oGjZNVXtYEZOPs%2F9L%2FUM3PVt&X-Amz-Signature=81cb6784070ce1cddf6de1f8eaa6a4e69b35521a4d61730122b3aae94aafac9a&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674B72RCX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAsRW77OPIZOVTb7oJNRXfjOBj7JmGOcBkF710c7vmHjAiEA4h4bxTSoh4MLOKCuWHcKYGkV%2B%2FqmLUFHPLA1dJgrc4Iq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDCWvHvkW4NfTAMk1sCrcA1tLLV2nQEaMq73CJX1no4wZox8KU3%2F51UWYB9mXqY7dwoaaQP81goEQYcyJNJINa89bQvFUzRqI11aYl%2FgZqxzL%2B5JckNI9SWema6yUWJLFMCHMqyWZJFS9dS2njskIZMXAgkWAw3INPCJ%2BHxJILm3B%2FkSEUI2KEU3X1fczUsbgvv1KZ2hNXmJFhdvJQ%2BzWfsBCmiT5wwUrV5R5nxKx112iphn%2B%2FDH2srfwat4El5VMx%2FoAVLqoxAoQsE09fFE0x5OIWfnyISgmoTmYxcUYME%2BaNJsY5Yo%2Bu0yNjksZQkq6A9qobExprkmbp4hBtnIdJsKawzvBPWeNhWk6TdOtMAhi6K98dycIKIYfgaGWu3OxhWhNWQ4M680WoP9%2F8LxtNOeWWIW2yON2OXsqbOX7uvP9jXvYQvV7vlBjUa9Hwiqy1r2HHFALlnoeR5In5kbUtkTkGRBiHWVHk3abAAhYvyZ%2Fb9DPhh53kfnrUE9jrMb6tdrooCt%2Fw022dBbyvvWu4gdn0CsO7llBgDG7dJY%2FnaYjTrf1SwRpoF9olBT8rWl%2B7uTEVUh33Za82VXF6ar8xHZs%2F1svFUAPamfHoNAKvO8PDs8xJFLmCv%2FsIyB34vnh7e4bYUNzrLM%2F8vmfMKHTgr0GOqUB0uKyJDNSeDeSZvzOf06nhQbTid18RVD7qQUp0nq0FVWBt1Os3xHwJouNA4nedaMnR2k9wbVQX9CNDHX8CJ8XvCyRHBqavTPg0U%2FNGc8TvP0bDR6DnL6w%2FPTn4WQm7To5vsnHR%2B0dV0%2FZaOjlF%2Fvppw%2B9yynLyMCLJWwf2p6yhilHN4FCE03cJV%2BtCTPM0zBGW5kJ1JZSG%2BxsUn%2FpkpKR04%2F0HD9z&X-Amz-Signature=ca4bea698a8b48402fafb19306fc29af2091b0998f79338c0d474f3bb19ff65e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674B72RCX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAsRW77OPIZOVTb7oJNRXfjOBj7JmGOcBkF710c7vmHjAiEA4h4bxTSoh4MLOKCuWHcKYGkV%2B%2FqmLUFHPLA1dJgrc4Iq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDCWvHvkW4NfTAMk1sCrcA1tLLV2nQEaMq73CJX1no4wZox8KU3%2F51UWYB9mXqY7dwoaaQP81goEQYcyJNJINa89bQvFUzRqI11aYl%2FgZqxzL%2B5JckNI9SWema6yUWJLFMCHMqyWZJFS9dS2njskIZMXAgkWAw3INPCJ%2BHxJILm3B%2FkSEUI2KEU3X1fczUsbgvv1KZ2hNXmJFhdvJQ%2BzWfsBCmiT5wwUrV5R5nxKx112iphn%2B%2FDH2srfwat4El5VMx%2FoAVLqoxAoQsE09fFE0x5OIWfnyISgmoTmYxcUYME%2BaNJsY5Yo%2Bu0yNjksZQkq6A9qobExprkmbp4hBtnIdJsKawzvBPWeNhWk6TdOtMAhi6K98dycIKIYfgaGWu3OxhWhNWQ4M680WoP9%2F8LxtNOeWWIW2yON2OXsqbOX7uvP9jXvYQvV7vlBjUa9Hwiqy1r2HHFALlnoeR5In5kbUtkTkGRBiHWVHk3abAAhYvyZ%2Fb9DPhh53kfnrUE9jrMb6tdrooCt%2Fw022dBbyvvWu4gdn0CsO7llBgDG7dJY%2FnaYjTrf1SwRpoF9olBT8rWl%2B7uTEVUh33Za82VXF6ar8xHZs%2F1svFUAPamfHoNAKvO8PDs8xJFLmCv%2FsIyB34vnh7e4bYUNzrLM%2F8vmfMKHTgr0GOqUB0uKyJDNSeDeSZvzOf06nhQbTid18RVD7qQUp0nq0FVWBt1Os3xHwJouNA4nedaMnR2k9wbVQX9CNDHX8CJ8XvCyRHBqavTPg0U%2FNGc8TvP0bDR6DnL6w%2FPTn4WQm7To5vsnHR%2B0dV0%2FZaOjlF%2Fvppw%2B9yynLyMCLJWwf2p6yhilHN4FCE03cJV%2BtCTPM0zBGW5kJ1JZSG%2BxsUn%2FpkpKR04%2F0HD9z&X-Amz-Signature=2ff1e37dacba6f4615f2de51dd3edc8834fa7aaa68dafc4303eae525008cc5be&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4TDET3O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2F2Zx0IuCVUpP9mFl4O7n%2B5WkiM8WOVaBwQOG2RQ2eJAiB0R0ISX7%2FqLovdTardcnDIp68Cc3sZAlnkArbCb7X82ir%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMItO9MGCMPtvveS4AKtwDkMiQDvPcTEy0rUhdaD%2Fiemt7D0Uj7fkN4O7UxQyrX8T1%2F5197RwKG2x%2B8Z8r4xHA71i2fXooanEX9%2FALeReqa2irW68Kalw%2FjP9AsSqoQjNOfu8UYHGQsoHw4zoX98j3xKnUKtz%2BZo%2BkpeQ%2B7Ma8YTvYeBBnYtBVcEoIionILeTXLm5akVKTJtWVBb0tiG2pZNRW6Af%2B0NSNybDqZK5YAjGlzHvGkGMixiDTNuq9GpN9wiARNw4p9Hi8%2FyDHDkhhEMHaJWO2VbYPEabmoaf%2B9Xu6gffWDFKmO9SteuFaB0YNZy3IZ2jp3FbNmgUeI7dfBmpnGWozDHq%2Fjhx%2Fy%2FHehtCbzA9EBmxug%2BMf897E%2FsymnijQ7EPMtp0SG8NCBDylAqI1TM7iEwuAJBrwcQD%2B%2Fe5DOwJ48p2FkfaduYUeVYDASADxWiZ9l4pNCEMqIwAd%2FMsScqeJ1KOnhYMQD6UeRSyZWQfFVORKM9M92Lv2U8JQfOcRqnHhbxGyql3loAYu1Jd6Zj1Bdl6t%2BtnyCLdc51bXiHhgGqR8MSv%2B27Mh09GAr34c4CjspQ53de3999tshNvs%2BamYs5DINy58n8bmHw%2BJjCThIJVBIrENxBCjdCurosUqL4kIw9WPJVgw7NKCvQY6pgGG%2FlNu96qCF%2FOjdABGUdqaoEdvUeJbr6waHmzog52ywH8C4QOD%2FJgZat8YBvLtXarxEWLC2XCpDo076ttoTaI9TCT9voUa2Vqr0bUOthOcVT9GCJpBY1sN%2BFcJiknG2GtmxR9%2FsDUyZ0eUq7%2FZ2LALwXL0qfqQQmpYF7SFEf0VhvwmoBmD0KeBqKfpQtXA3MON5Jb2oGjZNVXtYEZOPs%2F9L%2FUM3PVt&X-Amz-Signature=1dbb2e28767613590d4946591520786742bb0adc20219304437115d2d7fba07d&X-Amz-SignedHeaders=host&x-id=GetObject)
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