

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672PN7NL6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDF%2FdS6dYeJ9Nh92PWd4ZcaBEP4YwogsWiGb8o6KmCkpAIgfi%2FA9yfyHj12TP%2FYvmKvqEbIaROXFtWtssykmVmNtqQqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWbYTLcV%2BmJ%2BF%2B9MyrcA4VWZsvZ5o0X6mc2UcpvkUERvEzq72ZyYIRMl4ecaiyWubfHYZHtG7W3AoO6mLs23nB8ZlSKV%2BnurAahSl25hWXjlxCWkozXKTZARYUPFRLG65tPpaBoq87WABkkLAfalHgtX4FKiFq6ekN8esBNH9zTJvosb8c86BFVpSAosPD91yoUNHjEjKGtMSPnuuhGC8VQJAQHkoIhLqDhHuLzyK6XzGGc7IRQ2C6qis%2FS3lIWh3fBtVh9RAP4LIaTzH0fuLYpNVlo0X97sYi6p3OCJFN8ecBe00sTEzRIAFApPbdj2AEifCmKodg6XySMvM4rPfuxA5%2BXrsTUpQcED2kbPzmLfQkphOL0%2F2TSB1HUcuipqPhKq7c0KXy7GELeDII8LRerCmwEuQAmxXTEtvqbcKcmfHPxMLaDt3aMTWQrPBD8fcQmYusUrl9Q%2BQCPo0Sep3330rGJjxXxQNY7QwNDnWQPkdiV6X4e0UcNbykHhYXk8Rua%2B92f8opB7IBDNgsHXBp%2BR88aF%2FIZplGslTcnzGdyD4hD2xP86m1KokBPbZ%2B2iHN4pVfduzuGxG7vPJT%2FoWaXFWxEd1Pv7mLgjB1h8q8rLYlU5Kv5Z8fhBwKISoX50nr47S2BwkwNHkrwMKHB9rwGOqUBP7ZdejdrA7asFNx25%2B5CP%2FZhOUUEOczIJ9D4MCM6%2FVz%2FPD%2FQ1oUVslnhivRpzK1YuxdFlO3nn51gJf0UalhXgU6Y6U86Otltk4F5E4jFv0ybf5%2BqrvaYWGX32b6t9B3d13wb6zht6K7klKb6AXKK%2BgPOJ3OeTvnZoXuTfmsgHfO8BLxqtCsGFwFgCNDsJaV0xE9hGFM0H38NDbhmYYn0Y35IZnzk&X-Amz-Signature=1efec4ca5501d7cde1b47bf9860776a36e4c4fecac295dc4d8a99d64ca011d70&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672PN7NL6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDF%2FdS6dYeJ9Nh92PWd4ZcaBEP4YwogsWiGb8o6KmCkpAIgfi%2FA9yfyHj12TP%2FYvmKvqEbIaROXFtWtssykmVmNtqQqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWbYTLcV%2BmJ%2BF%2B9MyrcA4VWZsvZ5o0X6mc2UcpvkUERvEzq72ZyYIRMl4ecaiyWubfHYZHtG7W3AoO6mLs23nB8ZlSKV%2BnurAahSl25hWXjlxCWkozXKTZARYUPFRLG65tPpaBoq87WABkkLAfalHgtX4FKiFq6ekN8esBNH9zTJvosb8c86BFVpSAosPD91yoUNHjEjKGtMSPnuuhGC8VQJAQHkoIhLqDhHuLzyK6XzGGc7IRQ2C6qis%2FS3lIWh3fBtVh9RAP4LIaTzH0fuLYpNVlo0X97sYi6p3OCJFN8ecBe00sTEzRIAFApPbdj2AEifCmKodg6XySMvM4rPfuxA5%2BXrsTUpQcED2kbPzmLfQkphOL0%2F2TSB1HUcuipqPhKq7c0KXy7GELeDII8LRerCmwEuQAmxXTEtvqbcKcmfHPxMLaDt3aMTWQrPBD8fcQmYusUrl9Q%2BQCPo0Sep3330rGJjxXxQNY7QwNDnWQPkdiV6X4e0UcNbykHhYXk8Rua%2B92f8opB7IBDNgsHXBp%2BR88aF%2FIZplGslTcnzGdyD4hD2xP86m1KokBPbZ%2B2iHN4pVfduzuGxG7vPJT%2FoWaXFWxEd1Pv7mLgjB1h8q8rLYlU5Kv5Z8fhBwKISoX50nr47S2BwkwNHkrwMKHB9rwGOqUBP7ZdejdrA7asFNx25%2B5CP%2FZhOUUEOczIJ9D4MCM6%2FVz%2FPD%2FQ1oUVslnhivRpzK1YuxdFlO3nn51gJf0UalhXgU6Y6U86Otltk4F5E4jFv0ybf5%2BqrvaYWGX32b6t9B3d13wb6zht6K7klKb6AXKK%2BgPOJ3OeTvnZoXuTfmsgHfO8BLxqtCsGFwFgCNDsJaV0xE9hGFM0H38NDbhmYYn0Y35IZnzk&X-Amz-Signature=b3db3b800042ec5d8e07e7659b4f8dcc5d058c8dc845ae522cca6dd5585ba461&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672PN7NL6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDF%2FdS6dYeJ9Nh92PWd4ZcaBEP4YwogsWiGb8o6KmCkpAIgfi%2FA9yfyHj12TP%2FYvmKvqEbIaROXFtWtssykmVmNtqQqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWbYTLcV%2BmJ%2BF%2B9MyrcA4VWZsvZ5o0X6mc2UcpvkUERvEzq72ZyYIRMl4ecaiyWubfHYZHtG7W3AoO6mLs23nB8ZlSKV%2BnurAahSl25hWXjlxCWkozXKTZARYUPFRLG65tPpaBoq87WABkkLAfalHgtX4FKiFq6ekN8esBNH9zTJvosb8c86BFVpSAosPD91yoUNHjEjKGtMSPnuuhGC8VQJAQHkoIhLqDhHuLzyK6XzGGc7IRQ2C6qis%2FS3lIWh3fBtVh9RAP4LIaTzH0fuLYpNVlo0X97sYi6p3OCJFN8ecBe00sTEzRIAFApPbdj2AEifCmKodg6XySMvM4rPfuxA5%2BXrsTUpQcED2kbPzmLfQkphOL0%2F2TSB1HUcuipqPhKq7c0KXy7GELeDII8LRerCmwEuQAmxXTEtvqbcKcmfHPxMLaDt3aMTWQrPBD8fcQmYusUrl9Q%2BQCPo0Sep3330rGJjxXxQNY7QwNDnWQPkdiV6X4e0UcNbykHhYXk8Rua%2B92f8opB7IBDNgsHXBp%2BR88aF%2FIZplGslTcnzGdyD4hD2xP86m1KokBPbZ%2B2iHN4pVfduzuGxG7vPJT%2FoWaXFWxEd1Pv7mLgjB1h8q8rLYlU5Kv5Z8fhBwKISoX50nr47S2BwkwNHkrwMKHB9rwGOqUBP7ZdejdrA7asFNx25%2B5CP%2FZhOUUEOczIJ9D4MCM6%2FVz%2FPD%2FQ1oUVslnhivRpzK1YuxdFlO3nn51gJf0UalhXgU6Y6U86Otltk4F5E4jFv0ybf5%2BqrvaYWGX32b6t9B3d13wb6zht6K7klKb6AXKK%2BgPOJ3OeTvnZoXuTfmsgHfO8BLxqtCsGFwFgCNDsJaV0xE9hGFM0H38NDbhmYYn0Y35IZnzk&X-Amz-Signature=6d361438b8cf7aaaa723d20d43c14a981d99c386ca78170db564189123c49447&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBKALEVU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FMrkIe6c19bDfrrI2HnJJ8KYkpKNSnZRrWDjw0q08LwIgTxd0YIjhf%2B0XE9BuJcsid71HL0eETYtwQaQ%2FaqqhmFkqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHMywjSF%2FD21BGJ7uSrcAwC1lHBzQ48it4DgY%2BGvYKa6E24rw3Rco3d77bxTcEXr4Mce1I%2BLu%2F%2BEHOhgF3GgO042gy43x7UXttMm6sMRXHHCROHL2Lf3env0T5B5f6GmlHJfiunXX7%2B1mPahLsxqoeJi3pgJAApVo%2BcVWrb%2BECd8ZBY4i8beBVwzP0JM5FG9Y9loYs%2BxgzNAudR27UOLQ%2FfaQqEdFyp8MBuC81odKisj%2F2aXTGzqCWXxtUkGI1uZ0De2fNlXU1z%2BWcdmj5zUrZGTj6BIkvHmBBz%2BKE0quHgtGoCdeEeOZuA5UghzlEUE1X8%2F0HMm0EjuUuUn266G92ATDDJa0hlnX5am7iCdfnFKM5aadMTA%2BUkVlPAXQTxJxPmD2lNJHjjBKwWPhjwwYJ%2Buu%2FeUCmfad87Vpt%2BdwTaGO6jbmc%2Bfi%2FlX4R5itSGLOY1ZjA8A%2F21bR9BoyI%2FrC3Ag3BG10aqcouJmJpHzFLiQsNTqRSD4YQEENFfzw1RhLmCO%2BqhTFPvdWIiS%2BkTDvCeVWmEO5m58VoDjeSxzS1Y1O77xdx1eZDMQxtBNsSBT%2BF1mveZtYTgySts1TmyCy96YlVVtZO%2BfHj%2Fbq0i5NYmP9ssgDOnCcE30I4Wic4c2hMiLRxAKpksPQAu1MKHB9rwGOqUBCA%2B1fQpYXGXNBSs9estCFzxk7DLV79e4CJjSZg7pMGx%2BHHIzHn5u1au1ukHn96%2FSigIdG4%2FPr%2B4km92fn%2F4o6ObIU7KWDtOIdEid4Lm%2Bu1p0SmRJ%2Ba6ekkQkuHypNrJRjczyDKSVtMWShMEX%2FX5G09Tj4hiSvqHhIC0gP8Hsw%2BsAS1Ikov%2FR9fnBNKazoHGR74l34cnfPgTs56wuihIbXhY4Vv%2Fa&X-Amz-Signature=229770307f8eb6ab41ab6a0bb655b446c857ba41fad164606f923bda17554c29&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBKALEVU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FMrkIe6c19bDfrrI2HnJJ8KYkpKNSnZRrWDjw0q08LwIgTxd0YIjhf%2B0XE9BuJcsid71HL0eETYtwQaQ%2FaqqhmFkqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHMywjSF%2FD21BGJ7uSrcAwC1lHBzQ48it4DgY%2BGvYKa6E24rw3Rco3d77bxTcEXr4Mce1I%2BLu%2F%2BEHOhgF3GgO042gy43x7UXttMm6sMRXHHCROHL2Lf3env0T5B5f6GmlHJfiunXX7%2B1mPahLsxqoeJi3pgJAApVo%2BcVWrb%2BECd8ZBY4i8beBVwzP0JM5FG9Y9loYs%2BxgzNAudR27UOLQ%2FfaQqEdFyp8MBuC81odKisj%2F2aXTGzqCWXxtUkGI1uZ0De2fNlXU1z%2BWcdmj5zUrZGTj6BIkvHmBBz%2BKE0quHgtGoCdeEeOZuA5UghzlEUE1X8%2F0HMm0EjuUuUn266G92ATDDJa0hlnX5am7iCdfnFKM5aadMTA%2BUkVlPAXQTxJxPmD2lNJHjjBKwWPhjwwYJ%2Buu%2FeUCmfad87Vpt%2BdwTaGO6jbmc%2Bfi%2FlX4R5itSGLOY1ZjA8A%2F21bR9BoyI%2FrC3Ag3BG10aqcouJmJpHzFLiQsNTqRSD4YQEENFfzw1RhLmCO%2BqhTFPvdWIiS%2BkTDvCeVWmEO5m58VoDjeSxzS1Y1O77xdx1eZDMQxtBNsSBT%2BF1mveZtYTgySts1TmyCy96YlVVtZO%2BfHj%2Fbq0i5NYmP9ssgDOnCcE30I4Wic4c2hMiLRxAKpksPQAu1MKHB9rwGOqUBCA%2B1fQpYXGXNBSs9estCFzxk7DLV79e4CJjSZg7pMGx%2BHHIzHn5u1au1ukHn96%2FSigIdG4%2FPr%2B4km92fn%2F4o6ObIU7KWDtOIdEid4Lm%2Bu1p0SmRJ%2Ba6ekkQkuHypNrJRjczyDKSVtMWShMEX%2FX5G09Tj4hiSvqHhIC0gP8Hsw%2BsAS1Ikov%2FR9fnBNKazoHGR74l34cnfPgTs56wuihIbXhY4Vv%2Fa&X-Amz-Signature=d46ed60c67f0c0fc55ed7f751eecd44729315c3c0a9a928c1a698676bb50ee71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672PN7NL6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDF%2FdS6dYeJ9Nh92PWd4ZcaBEP4YwogsWiGb8o6KmCkpAIgfi%2FA9yfyHj12TP%2FYvmKvqEbIaROXFtWtssykmVmNtqQqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWbYTLcV%2BmJ%2BF%2B9MyrcA4VWZsvZ5o0X6mc2UcpvkUERvEzq72ZyYIRMl4ecaiyWubfHYZHtG7W3AoO6mLs23nB8ZlSKV%2BnurAahSl25hWXjlxCWkozXKTZARYUPFRLG65tPpaBoq87WABkkLAfalHgtX4FKiFq6ekN8esBNH9zTJvosb8c86BFVpSAosPD91yoUNHjEjKGtMSPnuuhGC8VQJAQHkoIhLqDhHuLzyK6XzGGc7IRQ2C6qis%2FS3lIWh3fBtVh9RAP4LIaTzH0fuLYpNVlo0X97sYi6p3OCJFN8ecBe00sTEzRIAFApPbdj2AEifCmKodg6XySMvM4rPfuxA5%2BXrsTUpQcED2kbPzmLfQkphOL0%2F2TSB1HUcuipqPhKq7c0KXy7GELeDII8LRerCmwEuQAmxXTEtvqbcKcmfHPxMLaDt3aMTWQrPBD8fcQmYusUrl9Q%2BQCPo0Sep3330rGJjxXxQNY7QwNDnWQPkdiV6X4e0UcNbykHhYXk8Rua%2B92f8opB7IBDNgsHXBp%2BR88aF%2FIZplGslTcnzGdyD4hD2xP86m1KokBPbZ%2B2iHN4pVfduzuGxG7vPJT%2FoWaXFWxEd1Pv7mLgjB1h8q8rLYlU5Kv5Z8fhBwKISoX50nr47S2BwkwNHkrwMKHB9rwGOqUBP7ZdejdrA7asFNx25%2B5CP%2FZhOUUEOczIJ9D4MCM6%2FVz%2FPD%2FQ1oUVslnhivRpzK1YuxdFlO3nn51gJf0UalhXgU6Y6U86Otltk4F5E4jFv0ybf5%2BqrvaYWGX32b6t9B3d13wb6zht6K7klKb6AXKK%2BgPOJ3OeTvnZoXuTfmsgHfO8BLxqtCsGFwFgCNDsJaV0xE9hGFM0H38NDbhmYYn0Y35IZnzk&X-Amz-Signature=d79aa0a1fc45c9f9e547c8a4343f7854e3870d76706756ee7030f82d9ca19d0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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