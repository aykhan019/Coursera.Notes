

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPTWUSAS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFGKR7ZPxACws8fNySoxvrRv%2B7GE9h9lwH4sfO0klOxQIgX5jlMOT9dzPearrxkibtydOkg%2FwPWvnTXUcd9QFsnWIqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2pckbQFguypaXiaircAyhBktZH2HUZT5hd3PzVbGpA3U5tIA78K8cH9jVRKZI8vpzYURGCOjNN4n9ytEzziIKVSYi3nXhsCCx5acJ1mXYB0cJayCEtzJW0mCh6zYcn4UdiZvLK6J0LWAk%2BRCE97RcQLNDo2reZyghqsLX2sf8v%2B3oTbCTTgL1tLi0qILZh59nJlRXQ%2F9kjdsFD8ZVXOkyktiV0bgeDX6GwjBhqbayWeDkx0zqtP%2BEGvl0PGlyO1ucS%2Fx3coJJ3aIL5lqj5cWMjydEBfVj9I%2FSet4NylswhPQE03H5yuX1TwnFv5Aan2ho2gZs1dAFNg5wJHh8%2BQ%2FxGdbmJEObdPJbm%2F9vWNBC8bcFYrXKJ1Af7fWarquaS%2B04c0CVVgiBx9whdFhu4qd9KYKdnWEC9I8TOjvNCBG2o05bPw%2F%2BK1KeT3hcP68vTSKeqogoQSj1D1rDchSuDOzCxkWJ3Y3Cpf3OlOdxgV9m5A9ntElmX9mZ1BY%2FUS03gmqfJUu1EAEwQ4VDvhhaDu%2F54wNLfxMogw6OQeTJvpgyIx2f6hA9wQcaFw06BlhNDDdbN8dhoCDx4P%2F2MMZNcXqeG0Sy6ESFLvqSxu1zqcxALbRmf8gUPRz6mgcBvDZYB%2BJtiVmLITG5LMmIiML759rwGOqUBuyMnalo39pF7x0WWdPL7KY0MmTfI5UGHLwJ5fQhfu6cmUerU%2FyGa5if2ZXSw8VTKZxsbFdPBXnwBJfXDeoozcQxoCSY9wQVIvBjKoiN2kMEt7%2Fdiz7iDy5xVyaUBt870itWBpm9NK0h5vkB7N%2BSL2BkdhJpCX5HbS7M7fB0XiAsYqMkHeOodr1qnLuf9obszB7S21yUUGjwnGIvEckvYuKRUzv%2BU&X-Amz-Signature=ada961d752b097203edcdfbd12cdc02db768b9c414a3c743b7a5557eaf58397b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPTWUSAS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFGKR7ZPxACws8fNySoxvrRv%2B7GE9h9lwH4sfO0klOxQIgX5jlMOT9dzPearrxkibtydOkg%2FwPWvnTXUcd9QFsnWIqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2pckbQFguypaXiaircAyhBktZH2HUZT5hd3PzVbGpA3U5tIA78K8cH9jVRKZI8vpzYURGCOjNN4n9ytEzziIKVSYi3nXhsCCx5acJ1mXYB0cJayCEtzJW0mCh6zYcn4UdiZvLK6J0LWAk%2BRCE97RcQLNDo2reZyghqsLX2sf8v%2B3oTbCTTgL1tLi0qILZh59nJlRXQ%2F9kjdsFD8ZVXOkyktiV0bgeDX6GwjBhqbayWeDkx0zqtP%2BEGvl0PGlyO1ucS%2Fx3coJJ3aIL5lqj5cWMjydEBfVj9I%2FSet4NylswhPQE03H5yuX1TwnFv5Aan2ho2gZs1dAFNg5wJHh8%2BQ%2FxGdbmJEObdPJbm%2F9vWNBC8bcFYrXKJ1Af7fWarquaS%2B04c0CVVgiBx9whdFhu4qd9KYKdnWEC9I8TOjvNCBG2o05bPw%2F%2BK1KeT3hcP68vTSKeqogoQSj1D1rDchSuDOzCxkWJ3Y3Cpf3OlOdxgV9m5A9ntElmX9mZ1BY%2FUS03gmqfJUu1EAEwQ4VDvhhaDu%2F54wNLfxMogw6OQeTJvpgyIx2f6hA9wQcaFw06BlhNDDdbN8dhoCDx4P%2F2MMZNcXqeG0Sy6ESFLvqSxu1zqcxALbRmf8gUPRz6mgcBvDZYB%2BJtiVmLITG5LMmIiML759rwGOqUBuyMnalo39pF7x0WWdPL7KY0MmTfI5UGHLwJ5fQhfu6cmUerU%2FyGa5if2ZXSw8VTKZxsbFdPBXnwBJfXDeoozcQxoCSY9wQVIvBjKoiN2kMEt7%2Fdiz7iDy5xVyaUBt870itWBpm9NK0h5vkB7N%2BSL2BkdhJpCX5HbS7M7fB0XiAsYqMkHeOodr1qnLuf9obszB7S21yUUGjwnGIvEckvYuKRUzv%2BU&X-Amz-Signature=6b6f5b36f39839a5442f797b86009d53a705b7f9aeafa74154e1cd4408acf886&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPTWUSAS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFGKR7ZPxACws8fNySoxvrRv%2B7GE9h9lwH4sfO0klOxQIgX5jlMOT9dzPearrxkibtydOkg%2FwPWvnTXUcd9QFsnWIqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2pckbQFguypaXiaircAyhBktZH2HUZT5hd3PzVbGpA3U5tIA78K8cH9jVRKZI8vpzYURGCOjNN4n9ytEzziIKVSYi3nXhsCCx5acJ1mXYB0cJayCEtzJW0mCh6zYcn4UdiZvLK6J0LWAk%2BRCE97RcQLNDo2reZyghqsLX2sf8v%2B3oTbCTTgL1tLi0qILZh59nJlRXQ%2F9kjdsFD8ZVXOkyktiV0bgeDX6GwjBhqbayWeDkx0zqtP%2BEGvl0PGlyO1ucS%2Fx3coJJ3aIL5lqj5cWMjydEBfVj9I%2FSet4NylswhPQE03H5yuX1TwnFv5Aan2ho2gZs1dAFNg5wJHh8%2BQ%2FxGdbmJEObdPJbm%2F9vWNBC8bcFYrXKJ1Af7fWarquaS%2B04c0CVVgiBx9whdFhu4qd9KYKdnWEC9I8TOjvNCBG2o05bPw%2F%2BK1KeT3hcP68vTSKeqogoQSj1D1rDchSuDOzCxkWJ3Y3Cpf3OlOdxgV9m5A9ntElmX9mZ1BY%2FUS03gmqfJUu1EAEwQ4VDvhhaDu%2F54wNLfxMogw6OQeTJvpgyIx2f6hA9wQcaFw06BlhNDDdbN8dhoCDx4P%2F2MMZNcXqeG0Sy6ESFLvqSxu1zqcxALbRmf8gUPRz6mgcBvDZYB%2BJtiVmLITG5LMmIiML759rwGOqUBuyMnalo39pF7x0WWdPL7KY0MmTfI5UGHLwJ5fQhfu6cmUerU%2FyGa5if2ZXSw8VTKZxsbFdPBXnwBJfXDeoozcQxoCSY9wQVIvBjKoiN2kMEt7%2Fdiz7iDy5xVyaUBt870itWBpm9NK0h5vkB7N%2BSL2BkdhJpCX5HbS7M7fB0XiAsYqMkHeOodr1qnLuf9obszB7S21yUUGjwnGIvEckvYuKRUzv%2BU&X-Amz-Signature=74a3d4d964fede2b72f3a1c68f4deb9642102ea0a74f34997372c487309a0ba2&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Q52FINN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXLZvz%2Bn0uVsFsQdyA%2F%2B1AqC1Q%2FHcUgRzDzDAvqjLfywIgO8dCIB6NYA8mZlUqDJKmv1iBNJ6vg0B5Eb%2FnoGsYGlkqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIvcrF%2FuHBhgR4h21SrcA4pp1WRCD3vwk6y3ThKBO%2FqrORCUTh%2BxWWHDTz%2Bf6rLeEXirTdbXoX66ioq%2FVkP2gLIl%2FHXDJuanIU%2B6WrG2fbvsIGNL3Bz7fgcjxu%2BR5ea3wzXkxGOFzBOsTrAdqbIxKmznExHaQYgrfSq4OYOFROFXAF%2FDquFL010KWRqfG%2Bmm3Rzwp6vFWuhUxZ2%2FlTqz7SBSRHNcLqQnAvl%2Bxl8nahCbV9nQ5HjVhV7RAzkq%2BNNGz2MpB0YOWgSL3VMjMKaMUZ%2BtSf2Xgew9OqIW6D%2BWSibfzlzRmEDbKZMEIhCNd%2Ff3PsH1u5T375AbaE6XQbuBu2xQvBOFn2GeQnmuZU5KpB9AzXz2upAvAKLINNOfgO06JqLHc5JoXVkNWjPWISVv0tsaGEC2XQl95PkGWpcaeJCNQeesRzKrUrkO5GFJdgj6PFXkV50oEd6qomn7ikoZLqi21UR65IVCEfgPfB7hwO7U8cEtPYI3M9cGDKOFHl9QfBl8iyZzZJ6IGknULRjdAMdpJ2qO3o43P%2FRYZifjgrUYAQ5NayLgxZrPMLdzrODRdpoo8%2F8V28e6AxHYB3iZh%2B9z0Tw3errk6dn65ustHCnauqwQBJMvxvme%2Fl9N2TrMDCQ7R1OYCnOL7VuCMMn59rwGOqUBCAsW%2BnF2TdGY7FdLg9c%2F4FdDtDtqDjNlOknAW0a7aKQm3KvZCXwFS087SxtVdDFRSDJuz31w0l45zb%2BgxX%2Fur91bvdy7RDrBm%2BXkqojiYIdQGOUirwFM4GhsxUiEe8%2F3lheGUWQaa5AT9%2BHKOnO%2FlRvRA03xtvSeiDQe%2BGUPdPoswFBSQMQMwV2m8%2FSd7YVQF12GfOszzJ%2FNOxSwdiPhMS%2BVslXV&X-Amz-Signature=4a09a5a3cedbcf1841211b8dfed61ccaee7345a7587f946550c5bea586f6ab06&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Q52FINN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXLZvz%2Bn0uVsFsQdyA%2F%2B1AqC1Q%2FHcUgRzDzDAvqjLfywIgO8dCIB6NYA8mZlUqDJKmv1iBNJ6vg0B5Eb%2FnoGsYGlkqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIvcrF%2FuHBhgR4h21SrcA4pp1WRCD3vwk6y3ThKBO%2FqrORCUTh%2BxWWHDTz%2Bf6rLeEXirTdbXoX66ioq%2FVkP2gLIl%2FHXDJuanIU%2B6WrG2fbvsIGNL3Bz7fgcjxu%2BR5ea3wzXkxGOFzBOsTrAdqbIxKmznExHaQYgrfSq4OYOFROFXAF%2FDquFL010KWRqfG%2Bmm3Rzwp6vFWuhUxZ2%2FlTqz7SBSRHNcLqQnAvl%2Bxl8nahCbV9nQ5HjVhV7RAzkq%2BNNGz2MpB0YOWgSL3VMjMKaMUZ%2BtSf2Xgew9OqIW6D%2BWSibfzlzRmEDbKZMEIhCNd%2Ff3PsH1u5T375AbaE6XQbuBu2xQvBOFn2GeQnmuZU5KpB9AzXz2upAvAKLINNOfgO06JqLHc5JoXVkNWjPWISVv0tsaGEC2XQl95PkGWpcaeJCNQeesRzKrUrkO5GFJdgj6PFXkV50oEd6qomn7ikoZLqi21UR65IVCEfgPfB7hwO7U8cEtPYI3M9cGDKOFHl9QfBl8iyZzZJ6IGknULRjdAMdpJ2qO3o43P%2FRYZifjgrUYAQ5NayLgxZrPMLdzrODRdpoo8%2F8V28e6AxHYB3iZh%2B9z0Tw3errk6dn65ustHCnauqwQBJMvxvme%2Fl9N2TrMDCQ7R1OYCnOL7VuCMMn59rwGOqUBCAsW%2BnF2TdGY7FdLg9c%2F4FdDtDtqDjNlOknAW0a7aKQm3KvZCXwFS087SxtVdDFRSDJuz31w0l45zb%2BgxX%2Fur91bvdy7RDrBm%2BXkqojiYIdQGOUirwFM4GhsxUiEe8%2F3lheGUWQaa5AT9%2BHKOnO%2FlRvRA03xtvSeiDQe%2BGUPdPoswFBSQMQMwV2m8%2FSd7YVQF12GfOszzJ%2FNOxSwdiPhMS%2BVslXV&X-Amz-Signature=c165fa0dfb745a3e3131530974652e99d6ad70ece7e5d4163ebdb579ae611c53&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPTWUSAS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFGKR7ZPxACws8fNySoxvrRv%2B7GE9h9lwH4sfO0klOxQIgX5jlMOT9dzPearrxkibtydOkg%2FwPWvnTXUcd9QFsnWIqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2pckbQFguypaXiaircAyhBktZH2HUZT5hd3PzVbGpA3U5tIA78K8cH9jVRKZI8vpzYURGCOjNN4n9ytEzziIKVSYi3nXhsCCx5acJ1mXYB0cJayCEtzJW0mCh6zYcn4UdiZvLK6J0LWAk%2BRCE97RcQLNDo2reZyghqsLX2sf8v%2B3oTbCTTgL1tLi0qILZh59nJlRXQ%2F9kjdsFD8ZVXOkyktiV0bgeDX6GwjBhqbayWeDkx0zqtP%2BEGvl0PGlyO1ucS%2Fx3coJJ3aIL5lqj5cWMjydEBfVj9I%2FSet4NylswhPQE03H5yuX1TwnFv5Aan2ho2gZs1dAFNg5wJHh8%2BQ%2FxGdbmJEObdPJbm%2F9vWNBC8bcFYrXKJ1Af7fWarquaS%2B04c0CVVgiBx9whdFhu4qd9KYKdnWEC9I8TOjvNCBG2o05bPw%2F%2BK1KeT3hcP68vTSKeqogoQSj1D1rDchSuDOzCxkWJ3Y3Cpf3OlOdxgV9m5A9ntElmX9mZ1BY%2FUS03gmqfJUu1EAEwQ4VDvhhaDu%2F54wNLfxMogw6OQeTJvpgyIx2f6hA9wQcaFw06BlhNDDdbN8dhoCDx4P%2F2MMZNcXqeG0Sy6ESFLvqSxu1zqcxALbRmf8gUPRz6mgcBvDZYB%2BJtiVmLITG5LMmIiML759rwGOqUBuyMnalo39pF7x0WWdPL7KY0MmTfI5UGHLwJ5fQhfu6cmUerU%2FyGa5if2ZXSw8VTKZxsbFdPBXnwBJfXDeoozcQxoCSY9wQVIvBjKoiN2kMEt7%2Fdiz7iDy5xVyaUBt870itWBpm9NK0h5vkB7N%2BSL2BkdhJpCX5HbS7M7fB0XiAsYqMkHeOodr1qnLuf9obszB7S21yUUGjwnGIvEckvYuKRUzv%2BU&X-Amz-Signature=ceec2afaa9e107093c9162e92f4982fa358843919a57eba78862126d43a5b604&X-Amz-SignedHeaders=host&x-id=GetObject)
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