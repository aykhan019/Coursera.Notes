

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR3VUO3B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDrLv3tazIFwq6FKnu9Q45NYtd9ssceXgicFRKv7um3yAIhAP3ZcWEGtl1deQOmqS2ZSWcllq2iFmq79fM%2BOBggiio9Kv8DCDcQABoMNjM3NDIzMTgzODA1IgwEqVus1Cou%2Bk4AQbUq3AOc5GR%2Fh6TAG1iJyC3ha0qsvby2w8oibGCsnJnGiy1JdLMOGi8SLWPOFnInRwFyda9xFtf3loKHFTtY%2Byc1wGO8RzEL2WZC3JKr8sP%2BwOi%2BSk8viNzmLZZX97deTEwp8dQs%2BFftahG44OsxGF1HkeKoFE9PolHEblpvKVSk9N9yNTF3bF2WC%2FsPsg2Gk3ngKPi8RirvyT42BcAhkFFN%2BBaolwzJ0A6k2tBUIpLGThJRVB5gLbr99gYy7LNbY72allKR8uUJBtwdid380oh0xIjfahF3p2qMkH0CS%2FvBIKzU9HIIud32qiX0jQsRhfFbRDrbCrfHSn0jEEHkWKgzaWcrJmtwi%2BX03hWhUDJBj7d98Hce3C%2BPIUMwnqbTjfeZ8%2F%2FhdHkaGDkH14GlzBtk6wYrErAEzwA2SY5Y0VPFDu5HrMsNQNqOHbCV2lLvBJy8d6d2MbZDG%2F%2BUnqHSr6%2BSZx6NHbhz5lAUzQbXNIY6q%2F8ZBUqxFW18fZCX6wfStiEvFA7nqETCo4UWhPA2e3tXcJXseNXM%2BahDBn%2Be7SgGvLXIfnobqkT7KNOxTmKhczzN%2Bk7xOqiqRn2z%2Fp%2FkbV%2FztMJUPPgOP7be38dI1eKzrghFjygFtB9jQSfNqwfTzTCtlIq9BjqkAay2p5LmwmSsgOOmITXocYer%2B9gn8Ecciu76ZJGPDyo4wNxCZTuoCs6mDbc1Vlwtvt%2B5u6PoUOeZBgaYcQTDZPC1W3VT%2Fz0ibxoh88OiGUcqAFb71NLD3I42P1Oon%2FoXDZGflC%2BMURxcYkDnJ2itWoNgMHugzcb3lOFYm%2FJQhvx7vlZJ%2Fq0NoNC4kSR2nHZ%2FnwsPU1oNnKf3IjU%2FW5CVrUlmjTrt&X-Amz-Signature=a29b8100e5048879b4f8b9aade3a8d98307da58384287c5c564b4672a6bd5104&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR3VUO3B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDrLv3tazIFwq6FKnu9Q45NYtd9ssceXgicFRKv7um3yAIhAP3ZcWEGtl1deQOmqS2ZSWcllq2iFmq79fM%2BOBggiio9Kv8DCDcQABoMNjM3NDIzMTgzODA1IgwEqVus1Cou%2Bk4AQbUq3AOc5GR%2Fh6TAG1iJyC3ha0qsvby2w8oibGCsnJnGiy1JdLMOGi8SLWPOFnInRwFyda9xFtf3loKHFTtY%2Byc1wGO8RzEL2WZC3JKr8sP%2BwOi%2BSk8viNzmLZZX97deTEwp8dQs%2BFftahG44OsxGF1HkeKoFE9PolHEblpvKVSk9N9yNTF3bF2WC%2FsPsg2Gk3ngKPi8RirvyT42BcAhkFFN%2BBaolwzJ0A6k2tBUIpLGThJRVB5gLbr99gYy7LNbY72allKR8uUJBtwdid380oh0xIjfahF3p2qMkH0CS%2FvBIKzU9HIIud32qiX0jQsRhfFbRDrbCrfHSn0jEEHkWKgzaWcrJmtwi%2BX03hWhUDJBj7d98Hce3C%2BPIUMwnqbTjfeZ8%2F%2FhdHkaGDkH14GlzBtk6wYrErAEzwA2SY5Y0VPFDu5HrMsNQNqOHbCV2lLvBJy8d6d2MbZDG%2F%2BUnqHSr6%2BSZx6NHbhz5lAUzQbXNIY6q%2F8ZBUqxFW18fZCX6wfStiEvFA7nqETCo4UWhPA2e3tXcJXseNXM%2BahDBn%2Be7SgGvLXIfnobqkT7KNOxTmKhczzN%2Bk7xOqiqRn2z%2Fp%2FkbV%2FztMJUPPgOP7be38dI1eKzrghFjygFtB9jQSfNqwfTzTCtlIq9BjqkAay2p5LmwmSsgOOmITXocYer%2B9gn8Ecciu76ZJGPDyo4wNxCZTuoCs6mDbc1Vlwtvt%2B5u6PoUOeZBgaYcQTDZPC1W3VT%2Fz0ibxoh88OiGUcqAFb71NLD3I42P1Oon%2FoXDZGflC%2BMURxcYkDnJ2itWoNgMHugzcb3lOFYm%2FJQhvx7vlZJ%2Fq0NoNC4kSR2nHZ%2FnwsPU1oNnKf3IjU%2FW5CVrUlmjTrt&X-Amz-Signature=f45bc275a265dcaaf57eb98920c170a06554c9d0b93f0740e76a8405bc361621&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR3VUO3B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDrLv3tazIFwq6FKnu9Q45NYtd9ssceXgicFRKv7um3yAIhAP3ZcWEGtl1deQOmqS2ZSWcllq2iFmq79fM%2BOBggiio9Kv8DCDcQABoMNjM3NDIzMTgzODA1IgwEqVus1Cou%2Bk4AQbUq3AOc5GR%2Fh6TAG1iJyC3ha0qsvby2w8oibGCsnJnGiy1JdLMOGi8SLWPOFnInRwFyda9xFtf3loKHFTtY%2Byc1wGO8RzEL2WZC3JKr8sP%2BwOi%2BSk8viNzmLZZX97deTEwp8dQs%2BFftahG44OsxGF1HkeKoFE9PolHEblpvKVSk9N9yNTF3bF2WC%2FsPsg2Gk3ngKPi8RirvyT42BcAhkFFN%2BBaolwzJ0A6k2tBUIpLGThJRVB5gLbr99gYy7LNbY72allKR8uUJBtwdid380oh0xIjfahF3p2qMkH0CS%2FvBIKzU9HIIud32qiX0jQsRhfFbRDrbCrfHSn0jEEHkWKgzaWcrJmtwi%2BX03hWhUDJBj7d98Hce3C%2BPIUMwnqbTjfeZ8%2F%2FhdHkaGDkH14GlzBtk6wYrErAEzwA2SY5Y0VPFDu5HrMsNQNqOHbCV2lLvBJy8d6d2MbZDG%2F%2BUnqHSr6%2BSZx6NHbhz5lAUzQbXNIY6q%2F8ZBUqxFW18fZCX6wfStiEvFA7nqETCo4UWhPA2e3tXcJXseNXM%2BahDBn%2Be7SgGvLXIfnobqkT7KNOxTmKhczzN%2Bk7xOqiqRn2z%2Fp%2FkbV%2FztMJUPPgOP7be38dI1eKzrghFjygFtB9jQSfNqwfTzTCtlIq9BjqkAay2p5LmwmSsgOOmITXocYer%2B9gn8Ecciu76ZJGPDyo4wNxCZTuoCs6mDbc1Vlwtvt%2B5u6PoUOeZBgaYcQTDZPC1W3VT%2Fz0ibxoh88OiGUcqAFb71NLD3I42P1Oon%2FoXDZGflC%2BMURxcYkDnJ2itWoNgMHugzcb3lOFYm%2FJQhvx7vlZJ%2Fq0NoNC4kSR2nHZ%2FnwsPU1oNnKf3IjU%2FW5CVrUlmjTrt&X-Amz-Signature=d845f634deb03ee7bb555bdf60455f39ac3175155cc8da393a6a767805ac75f3&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626ZV252D%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCjyEYyjIZ3JRUoqxXr3lRcGXQKc19Z556jqUU%2F59cn%2FQIhAMALXwOoRSJcpUEIYfcxct%2FStJi5%2FT83xde5pAbdoo2lKv8DCDcQABoMNjM3NDIzMTgzODA1Igx6jsOsJGJmlUXrnf8q3ANsiRJbDcZ6CvJv0MxglPdIfM9JWFVVXlzilSo57hwNce09bMqyE1o6CArBc%2BZZiRLZE8QNECyAY%2FK2XvUdQpgZTL2HJiWB89aNVuwxjXfgANUE043uJUxJZ003YRZobqdlDstSjTPAhoiWePn80Ouv6HcdiSt7BnfCl%2BRiaM9rWIfPbZ3seRmhKxNOkpTTXNz8Lg1AKwvnMvmnm0y6PZjbL1VfOOYU9%2FsNdsJmYN0HWD7UIhGJqHqyLcJCo2kmqOnhvlSQ6eeWFr01fDOUZ%2FEntUMMqrujY2PVjeNLKXBYzc%2F49KsjOkiClvgU5Tc0fi7mSryGq90HE5BzZFYDUfGYzFAGXQrSb4V7lmNmfrNYGyPm1YyWdM42CBpyqW66NrIYvaiZBD6xtrBdFDE8%2BMowsSvujTp3x4pTRxcBROa0iXsBj%2B0tl6ClF5Af%2Fa%2FdhtGGUMNTonoQ9%2FT33TsbpZj1z%2FjQW5j5t6qsw6DLwKQH9fOCLjhmhs5xDQaNik46lHKrJojjMQ288QhUkMFnvXKGCJsfLeUNY%2BMoxKpfTHr6%2B2oeJeoYiQjtarIfmPosdTax%2BFEVa9lNRx%2FsKzQ26Y3wJpfmWgRlktozsk4LbHvwG8WjCNUAXDlLQwigITCglIq9BjqkAR6jA4BeZWWN9Mv3eQKHMes3F3mngmafYfL3DKL7omxTCTkq9ni%2B0PdzFl4X5r1Y4ph2C6s0fNguSBWOIIjRoEVpuAhzoyCHI0%2BoY8pog2vzoZNIfQVZ%2FsxkUi6cISCLuX%2FFGDnsQOQLhqFkWpRyp8Peu1dKZpeiWi7x85lUhBzMmQZwHuboggRyh2GoFtK2wrpFYrwIrWtJIHGPWWEyv5F51Wfa&X-Amz-Signature=664857602e22ac03e971d8914d2d05f31680da4eb75b9fd885cde98d7f42c62f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626ZV252D%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCjyEYyjIZ3JRUoqxXr3lRcGXQKc19Z556jqUU%2F59cn%2FQIhAMALXwOoRSJcpUEIYfcxct%2FStJi5%2FT83xde5pAbdoo2lKv8DCDcQABoMNjM3NDIzMTgzODA1Igx6jsOsJGJmlUXrnf8q3ANsiRJbDcZ6CvJv0MxglPdIfM9JWFVVXlzilSo57hwNce09bMqyE1o6CArBc%2BZZiRLZE8QNECyAY%2FK2XvUdQpgZTL2HJiWB89aNVuwxjXfgANUE043uJUxJZ003YRZobqdlDstSjTPAhoiWePn80Ouv6HcdiSt7BnfCl%2BRiaM9rWIfPbZ3seRmhKxNOkpTTXNz8Lg1AKwvnMvmnm0y6PZjbL1VfOOYU9%2FsNdsJmYN0HWD7UIhGJqHqyLcJCo2kmqOnhvlSQ6eeWFr01fDOUZ%2FEntUMMqrujY2PVjeNLKXBYzc%2F49KsjOkiClvgU5Tc0fi7mSryGq90HE5BzZFYDUfGYzFAGXQrSb4V7lmNmfrNYGyPm1YyWdM42CBpyqW66NrIYvaiZBD6xtrBdFDE8%2BMowsSvujTp3x4pTRxcBROa0iXsBj%2B0tl6ClF5Af%2Fa%2FdhtGGUMNTonoQ9%2FT33TsbpZj1z%2FjQW5j5t6qsw6DLwKQH9fOCLjhmhs5xDQaNik46lHKrJojjMQ288QhUkMFnvXKGCJsfLeUNY%2BMoxKpfTHr6%2B2oeJeoYiQjtarIfmPosdTax%2BFEVa9lNRx%2FsKzQ26Y3wJpfmWgRlktozsk4LbHvwG8WjCNUAXDlLQwigITCglIq9BjqkAR6jA4BeZWWN9Mv3eQKHMes3F3mngmafYfL3DKL7omxTCTkq9ni%2B0PdzFl4X5r1Y4ph2C6s0fNguSBWOIIjRoEVpuAhzoyCHI0%2BoY8pog2vzoZNIfQVZ%2FsxkUi6cISCLuX%2FFGDnsQOQLhqFkWpRyp8Peu1dKZpeiWi7x85lUhBzMmQZwHuboggRyh2GoFtK2wrpFYrwIrWtJIHGPWWEyv5F51Wfa&X-Amz-Signature=6ea1ffeac5a2cfa7cc9ca3daa853bb2b4bcf1825ed4d8a1953839b608fd1ed3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR3VUO3B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDrLv3tazIFwq6FKnu9Q45NYtd9ssceXgicFRKv7um3yAIhAP3ZcWEGtl1deQOmqS2ZSWcllq2iFmq79fM%2BOBggiio9Kv8DCDcQABoMNjM3NDIzMTgzODA1IgwEqVus1Cou%2Bk4AQbUq3AOc5GR%2Fh6TAG1iJyC3ha0qsvby2w8oibGCsnJnGiy1JdLMOGi8SLWPOFnInRwFyda9xFtf3loKHFTtY%2Byc1wGO8RzEL2WZC3JKr8sP%2BwOi%2BSk8viNzmLZZX97deTEwp8dQs%2BFftahG44OsxGF1HkeKoFE9PolHEblpvKVSk9N9yNTF3bF2WC%2FsPsg2Gk3ngKPi8RirvyT42BcAhkFFN%2BBaolwzJ0A6k2tBUIpLGThJRVB5gLbr99gYy7LNbY72allKR8uUJBtwdid380oh0xIjfahF3p2qMkH0CS%2FvBIKzU9HIIud32qiX0jQsRhfFbRDrbCrfHSn0jEEHkWKgzaWcrJmtwi%2BX03hWhUDJBj7d98Hce3C%2BPIUMwnqbTjfeZ8%2F%2FhdHkaGDkH14GlzBtk6wYrErAEzwA2SY5Y0VPFDu5HrMsNQNqOHbCV2lLvBJy8d6d2MbZDG%2F%2BUnqHSr6%2BSZx6NHbhz5lAUzQbXNIY6q%2F8ZBUqxFW18fZCX6wfStiEvFA7nqETCo4UWhPA2e3tXcJXseNXM%2BahDBn%2Be7SgGvLXIfnobqkT7KNOxTmKhczzN%2Bk7xOqiqRn2z%2Fp%2FkbV%2FztMJUPPgOP7be38dI1eKzrghFjygFtB9jQSfNqwfTzTCtlIq9BjqkAay2p5LmwmSsgOOmITXocYer%2B9gn8Ecciu76ZJGPDyo4wNxCZTuoCs6mDbc1Vlwtvt%2B5u6PoUOeZBgaYcQTDZPC1W3VT%2Fz0ibxoh88OiGUcqAFb71NLD3I42P1Oon%2FoXDZGflC%2BMURxcYkDnJ2itWoNgMHugzcb3lOFYm%2FJQhvx7vlZJ%2Fq0NoNC4kSR2nHZ%2FnwsPU1oNnKf3IjU%2FW5CVrUlmjTrt&X-Amz-Signature=f3af0813a1b90d73880d403670d3a16277991713a0a105d04306f09a69036ea7&X-Amz-SignedHeaders=host&x-id=GetObject)
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