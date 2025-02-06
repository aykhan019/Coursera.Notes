

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SWBTFJW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIG0oo9kdWFq16%2FHdmkl7DKt3jukQgwy6piyE0YK32SJ3AiAaZnGUFUTUD9mET5d1Q0BiMuYIwy8EFiqt%2BQ8GWlt1Bir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMDfOP4U%2BMAhJKKowdKtwDldATMO6t%2BQe8WHJ%2BzbSpB%2FDq7V%2Fi9BHKkvSVzuf26aGRPfLsKCmtvSzh%2BhmutLdOOw941SOMTNl6N3XCwW%2Fpjrf1dhb%2F8OPfPTJvljNNc0G%2FfjH14nqttCv7jiIwTegzXar8h8FwLHTLtlIH07pskhd%2FNht5vYNn60F0jzrAeYp3QsfTNlAabClkuDrr%2FRdI3Yhl0cC%2F%2F10sPmkrqX5AwnhWotN9C1zcXt3zp1InKSeNXURxZ7HS4YWkViIfKOdlJfycm%2BdFz3ocdH1%2F58b6frrDCJmyUtDGm6qDa54eSwYZGYPiMMM1asLOCxvsaZkSXE0%2Bp6cFTvjtYxNcK0%2BP9DoUHV4RgF5O3mkQLoIGZwLakvCKQQSy8bfgmO2fmm99Hos7mdvxdZyw9kCEUIT9rmJ30Bx6jKYi39n5DyzQE%2Fi4Jp%2BTkEdWyYGWrZWNB6mg1gecXZnk6PzjhE1sjhGDtGkf3wT74ypg%2FKPp4bA3muHhHOi%2BpJi%2FUiTGPwS9aQUjQR3YFOa2LOVkvbHa2O%2BdLelmotPY%2BGhAjS%2Bl8BVxtsmXOffIFJuFON2lISSl2BjbbvGvMLdcehKdC6tm2s9m4rYk0FmkYOQk%2FmM5f%2FXqzJ%2FUlRC4veDScPI7jBww3uuRvQY6pgGqGem%2F96ABFst9CMMBNfzQDwtaOLE1rgQwuilKVJna86eoPeh9vI0vmo%2FPOxNQJQjHc2FGXHkQ1kOmrlY2TQMMnHjzh5OIKwQ%2BKPClbkCBSqFb0QCw29YjZQi%2BWFVJ3rFLvnRRFwgmSo1%2B5P%2BLm%2FAm5DymfeWs0xU77Jku6PEmJSeKIvQUUoP%2B6ppscR6XDIb5n%2BzGQF4thnMaBiJCflzIqH%2BFxwcb&X-Amz-Signature=50d7d36140d84bd44290e7a7117c521ef4f6fb326cb21b5c3b1199ef3c0e0edf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SWBTFJW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIG0oo9kdWFq16%2FHdmkl7DKt3jukQgwy6piyE0YK32SJ3AiAaZnGUFUTUD9mET5d1Q0BiMuYIwy8EFiqt%2BQ8GWlt1Bir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMDfOP4U%2BMAhJKKowdKtwDldATMO6t%2BQe8WHJ%2BzbSpB%2FDq7V%2Fi9BHKkvSVzuf26aGRPfLsKCmtvSzh%2BhmutLdOOw941SOMTNl6N3XCwW%2Fpjrf1dhb%2F8OPfPTJvljNNc0G%2FfjH14nqttCv7jiIwTegzXar8h8FwLHTLtlIH07pskhd%2FNht5vYNn60F0jzrAeYp3QsfTNlAabClkuDrr%2FRdI3Yhl0cC%2F%2F10sPmkrqX5AwnhWotN9C1zcXt3zp1InKSeNXURxZ7HS4YWkViIfKOdlJfycm%2BdFz3ocdH1%2F58b6frrDCJmyUtDGm6qDa54eSwYZGYPiMMM1asLOCxvsaZkSXE0%2Bp6cFTvjtYxNcK0%2BP9DoUHV4RgF5O3mkQLoIGZwLakvCKQQSy8bfgmO2fmm99Hos7mdvxdZyw9kCEUIT9rmJ30Bx6jKYi39n5DyzQE%2Fi4Jp%2BTkEdWyYGWrZWNB6mg1gecXZnk6PzjhE1sjhGDtGkf3wT74ypg%2FKPp4bA3muHhHOi%2BpJi%2FUiTGPwS9aQUjQR3YFOa2LOVkvbHa2O%2BdLelmotPY%2BGhAjS%2Bl8BVxtsmXOffIFJuFON2lISSl2BjbbvGvMLdcehKdC6tm2s9m4rYk0FmkYOQk%2FmM5f%2FXqzJ%2FUlRC4veDScPI7jBww3uuRvQY6pgGqGem%2F96ABFst9CMMBNfzQDwtaOLE1rgQwuilKVJna86eoPeh9vI0vmo%2FPOxNQJQjHc2FGXHkQ1kOmrlY2TQMMnHjzh5OIKwQ%2BKPClbkCBSqFb0QCw29YjZQi%2BWFVJ3rFLvnRRFwgmSo1%2B5P%2BLm%2FAm5DymfeWs0xU77Jku6PEmJSeKIvQUUoP%2B6ppscR6XDIb5n%2BzGQF4thnMaBiJCflzIqH%2BFxwcb&X-Amz-Signature=d0b54a3b9c3924662bd919d711007bf0a40802d7ee87edd95b49fe212ce9f323&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SWBTFJW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIG0oo9kdWFq16%2FHdmkl7DKt3jukQgwy6piyE0YK32SJ3AiAaZnGUFUTUD9mET5d1Q0BiMuYIwy8EFiqt%2BQ8GWlt1Bir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMDfOP4U%2BMAhJKKowdKtwDldATMO6t%2BQe8WHJ%2BzbSpB%2FDq7V%2Fi9BHKkvSVzuf26aGRPfLsKCmtvSzh%2BhmutLdOOw941SOMTNl6N3XCwW%2Fpjrf1dhb%2F8OPfPTJvljNNc0G%2FfjH14nqttCv7jiIwTegzXar8h8FwLHTLtlIH07pskhd%2FNht5vYNn60F0jzrAeYp3QsfTNlAabClkuDrr%2FRdI3Yhl0cC%2F%2F10sPmkrqX5AwnhWotN9C1zcXt3zp1InKSeNXURxZ7HS4YWkViIfKOdlJfycm%2BdFz3ocdH1%2F58b6frrDCJmyUtDGm6qDa54eSwYZGYPiMMM1asLOCxvsaZkSXE0%2Bp6cFTvjtYxNcK0%2BP9DoUHV4RgF5O3mkQLoIGZwLakvCKQQSy8bfgmO2fmm99Hos7mdvxdZyw9kCEUIT9rmJ30Bx6jKYi39n5DyzQE%2Fi4Jp%2BTkEdWyYGWrZWNB6mg1gecXZnk6PzjhE1sjhGDtGkf3wT74ypg%2FKPp4bA3muHhHOi%2BpJi%2FUiTGPwS9aQUjQR3YFOa2LOVkvbHa2O%2BdLelmotPY%2BGhAjS%2Bl8BVxtsmXOffIFJuFON2lISSl2BjbbvGvMLdcehKdC6tm2s9m4rYk0FmkYOQk%2FmM5f%2FXqzJ%2FUlRC4veDScPI7jBww3uuRvQY6pgGqGem%2F96ABFst9CMMBNfzQDwtaOLE1rgQwuilKVJna86eoPeh9vI0vmo%2FPOxNQJQjHc2FGXHkQ1kOmrlY2TQMMnHjzh5OIKwQ%2BKPClbkCBSqFb0QCw29YjZQi%2BWFVJ3rFLvnRRFwgmSo1%2B5P%2BLm%2FAm5DymfeWs0xU77Jku6PEmJSeKIvQUUoP%2B6ppscR6XDIb5n%2BzGQF4thnMaBiJCflzIqH%2BFxwcb&X-Amz-Signature=969fd46e08856f00044c6ed4b14bf5f8e7ffa10ceaa64f99a04ece90c1b8ce49&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGVM7JGA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQD%2BHQ5WT9kcHIapa6zOpqBH0J80lO68jZBDaBF6PF99UQIhAL5ZLLPOe9aglwuEP00PwfiHr5DGaBEkbFP70JFMqSBRKv8DCFwQABoMNjM3NDIzMTgzODA1Igwnpj4IJctioO49YSYq3AOQDv5kfAnnGUoQUhM6pvrDg1nrOgTx9MiuFfzyaqG1oo3Fac%2FnpfBKjXyWHdB3O4XP8V0fh33aR0gyEGUHaJw4EoCqpPfEQzM84CqZ3lcZoJs6LvaegaC8DRni56qWq2IccGICWnvG5hpwDNDcX0fs5pyDuoxf7ni2E74Y4vBHwHuX3yXLeD7lZP7JtQOH88QLY4Ch6npFX2H9d5lXuXjMUut2qCYJB86ALJSrbZHCocJnuIXlC98aunZ7dzAKfZGxkqWRrhsXPWMRnwlhXHoU%2Bq6W73Jkn%2FcT1kUPpumHmbN9qXsVhNybm2RSl2s2r6WAg4HTt%2BTpuxGVnYZVFSX5K8AnH8nSYkGrQiV5SQj3nuL6fD99HdXa2%2BsDxhsitAZsDj8AZDkp7%2BeZVwjJQ%2F4QKgwnVxQN6g4qpE20u4FaeLffl1%2F7RMnKCsS5u54Rwpgyc254K5iZYm4990fEvuqDLlEWR7NwfQJGYP56MkTn1oVFZJdRiCuldWsLwMYdKnqSVx%2BIhxEGaXuN47EYgWDTKNJN0CqPra6ISOjwrq0UZ22q3BT3Ue%2BsvXtbVdWW1n0ao871y5VteMqbctS8X2earhxukV%2BIheKRUvZ9xv9X494Z%2BsDdWj9jV6GOATCtppK9BjqkAdu%2BGfrm6z63%2BMyTGSaEHJhExU77LMoWk%2FSrBHc3BYg4TnjWz6RxFAt2Qwbxo9lJiLjSkjz%2FBHqRCWrTcVGgZTFS4IbUkKytGGpNwGg9VDMVigZ3AKnMkrEwyv8F24My4Ebf%2BtWGgnbtMS0cPHJqvKT1AcupQSQ%2FV7CXVcvAer6MobqmYirc5fQ6iHMiothSLSi387EmpRluxVdMKunuHR4MgRlI&X-Amz-Signature=8c824d9661f7de0a90c5a199ccf64818a3bb984f4dd63bb67fab8d9d032d2fa2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGVM7JGA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQD%2BHQ5WT9kcHIapa6zOpqBH0J80lO68jZBDaBF6PF99UQIhAL5ZLLPOe9aglwuEP00PwfiHr5DGaBEkbFP70JFMqSBRKv8DCFwQABoMNjM3NDIzMTgzODA1Igwnpj4IJctioO49YSYq3AOQDv5kfAnnGUoQUhM6pvrDg1nrOgTx9MiuFfzyaqG1oo3Fac%2FnpfBKjXyWHdB3O4XP8V0fh33aR0gyEGUHaJw4EoCqpPfEQzM84CqZ3lcZoJs6LvaegaC8DRni56qWq2IccGICWnvG5hpwDNDcX0fs5pyDuoxf7ni2E74Y4vBHwHuX3yXLeD7lZP7JtQOH88QLY4Ch6npFX2H9d5lXuXjMUut2qCYJB86ALJSrbZHCocJnuIXlC98aunZ7dzAKfZGxkqWRrhsXPWMRnwlhXHoU%2Bq6W73Jkn%2FcT1kUPpumHmbN9qXsVhNybm2RSl2s2r6WAg4HTt%2BTpuxGVnYZVFSX5K8AnH8nSYkGrQiV5SQj3nuL6fD99HdXa2%2BsDxhsitAZsDj8AZDkp7%2BeZVwjJQ%2F4QKgwnVxQN6g4qpE20u4FaeLffl1%2F7RMnKCsS5u54Rwpgyc254K5iZYm4990fEvuqDLlEWR7NwfQJGYP56MkTn1oVFZJdRiCuldWsLwMYdKnqSVx%2BIhxEGaXuN47EYgWDTKNJN0CqPra6ISOjwrq0UZ22q3BT3Ue%2BsvXtbVdWW1n0ao871y5VteMqbctS8X2earhxukV%2BIheKRUvZ9xv9X494Z%2BsDdWj9jV6GOATCtppK9BjqkAdu%2BGfrm6z63%2BMyTGSaEHJhExU77LMoWk%2FSrBHc3BYg4TnjWz6RxFAt2Qwbxo9lJiLjSkjz%2FBHqRCWrTcVGgZTFS4IbUkKytGGpNwGg9VDMVigZ3AKnMkrEwyv8F24My4Ebf%2BtWGgnbtMS0cPHJqvKT1AcupQSQ%2FV7CXVcvAer6MobqmYirc5fQ6iHMiothSLSi387EmpRluxVdMKunuHR4MgRlI&X-Amz-Signature=da2039f5c41d53ecb07518abe8de06c7d9b94a955d0cfcca02f1be18975b4205&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SWBTFJW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIG0oo9kdWFq16%2FHdmkl7DKt3jukQgwy6piyE0YK32SJ3AiAaZnGUFUTUD9mET5d1Q0BiMuYIwy8EFiqt%2BQ8GWlt1Bir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMDfOP4U%2BMAhJKKowdKtwDldATMO6t%2BQe8WHJ%2BzbSpB%2FDq7V%2Fi9BHKkvSVzuf26aGRPfLsKCmtvSzh%2BhmutLdOOw941SOMTNl6N3XCwW%2Fpjrf1dhb%2F8OPfPTJvljNNc0G%2FfjH14nqttCv7jiIwTegzXar8h8FwLHTLtlIH07pskhd%2FNht5vYNn60F0jzrAeYp3QsfTNlAabClkuDrr%2FRdI3Yhl0cC%2F%2F10sPmkrqX5AwnhWotN9C1zcXt3zp1InKSeNXURxZ7HS4YWkViIfKOdlJfycm%2BdFz3ocdH1%2F58b6frrDCJmyUtDGm6qDa54eSwYZGYPiMMM1asLOCxvsaZkSXE0%2Bp6cFTvjtYxNcK0%2BP9DoUHV4RgF5O3mkQLoIGZwLakvCKQQSy8bfgmO2fmm99Hos7mdvxdZyw9kCEUIT9rmJ30Bx6jKYi39n5DyzQE%2Fi4Jp%2BTkEdWyYGWrZWNB6mg1gecXZnk6PzjhE1sjhGDtGkf3wT74ypg%2FKPp4bA3muHhHOi%2BpJi%2FUiTGPwS9aQUjQR3YFOa2LOVkvbHa2O%2BdLelmotPY%2BGhAjS%2Bl8BVxtsmXOffIFJuFON2lISSl2BjbbvGvMLdcehKdC6tm2s9m4rYk0FmkYOQk%2FmM5f%2FXqzJ%2FUlRC4veDScPI7jBww3uuRvQY6pgGqGem%2F96ABFst9CMMBNfzQDwtaOLE1rgQwuilKVJna86eoPeh9vI0vmo%2FPOxNQJQjHc2FGXHkQ1kOmrlY2TQMMnHjzh5OIKwQ%2BKPClbkCBSqFb0QCw29YjZQi%2BWFVJ3rFLvnRRFwgmSo1%2B5P%2BLm%2FAm5DymfeWs0xU77Jku6PEmJSeKIvQUUoP%2B6ppscR6XDIb5n%2BzGQF4thnMaBiJCflzIqH%2BFxwcb&X-Amz-Signature=4b94920fa46e3d3b2b1c30f1744991b18189aaa6d4a1423008c6dd750a138c08&X-Amz-SignedHeaders=host&x-id=GetObject)
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