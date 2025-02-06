

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHMO2J5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIAczpOmiBHEb9%2BX%2FsQvskQohYYoTcEXuvEBfxwvVJ6GaAiEAh3KCxu1sx8XjjXHBwJ24l6%2B7ed0r1tBQnW2tfQZf%2FYwq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBsT%2FOpFilmMcTb%2BhircA6Jfi8%2B4rWeEqtZJkz09Fkt9vczc2%2BD0%2BHTh6rtCS0rdsW1LmXe5HkhDCObI738t4MTQrHNygN7dhwsrcgGjtNigv2yxbkIwRCSw%2Ffh5gi1kXgp4oMBqPnF%2BQR8fr0cDs7s5YZ88TRSOYHK8jM6SKojE6amWZ9oJJ3BO7xoNJneBlQ85gpU1SVkIMAIB6EacU7OIgpOX4ExLOaSXFBTGfnazaouSh1Az1HSQeEiSJyh8W6ANdRW4fUlw%2Bw28C00rb6jcdnXREPIfXR%2B6coDbbWYRUIFJQiWd5Fwm6j3Wg99Pq9WbcfMB7Ziu7zUQyEpP7nB4ES2ixq1rokuRxZO1uojUMnJhJfqzlblg%2BWOoyA1POewJEDuwqUDZeFJHq9LV%2BsWqz9UXqpR9%2BKPnKAd65VqQhqqcHqRtiUksKfqcFpLSr1ArXcNM9QEA8hUDsUELfiNRDU5CYkUps2tRzWBIx1hfPbhzXaVNkPFcef8KDr6nNEyMPKBa1ckHo9qchRvJGXkYi%2BbTYGsYCL5ezBTpi8NdKJmV5FZLiOgm2OXINrkzpU1u7vIUv4dVnPscetes%2FEMeF9jmzf%2FZP2N6TN2uhusMactOncbO76XreR4sF994YgMAhMb33uJt6%2BfEMPn7k70GOqUBAUEYdoqFSp2puSV2dxt5vGcUgOFTiT7Zjzc1gBgFrwm5glYkKu9QOTk5n2KJtHDIWpekhfHR0ON8J0H8amOGNATOCig8xu%2B9IhUaOw%2BqvYMdBhBqwuj6IXEsadPm70ubcgGomfT9BfE3FOIOyxDcSdnWnfr29YH7%2FFLxLgkrlKuh4irfUdQv9laWcgq7lzMzcLnloNCfyn8DbgbFG%2BDZZxVpsMXn&X-Amz-Signature=89c6e2db4d65318e302b9e135b3592965cf715c81f212084be240be3bbb1add1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHMO2J5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIAczpOmiBHEb9%2BX%2FsQvskQohYYoTcEXuvEBfxwvVJ6GaAiEAh3KCxu1sx8XjjXHBwJ24l6%2B7ed0r1tBQnW2tfQZf%2FYwq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBsT%2FOpFilmMcTb%2BhircA6Jfi8%2B4rWeEqtZJkz09Fkt9vczc2%2BD0%2BHTh6rtCS0rdsW1LmXe5HkhDCObI738t4MTQrHNygN7dhwsrcgGjtNigv2yxbkIwRCSw%2Ffh5gi1kXgp4oMBqPnF%2BQR8fr0cDs7s5YZ88TRSOYHK8jM6SKojE6amWZ9oJJ3BO7xoNJneBlQ85gpU1SVkIMAIB6EacU7OIgpOX4ExLOaSXFBTGfnazaouSh1Az1HSQeEiSJyh8W6ANdRW4fUlw%2Bw28C00rb6jcdnXREPIfXR%2B6coDbbWYRUIFJQiWd5Fwm6j3Wg99Pq9WbcfMB7Ziu7zUQyEpP7nB4ES2ixq1rokuRxZO1uojUMnJhJfqzlblg%2BWOoyA1POewJEDuwqUDZeFJHq9LV%2BsWqz9UXqpR9%2BKPnKAd65VqQhqqcHqRtiUksKfqcFpLSr1ArXcNM9QEA8hUDsUELfiNRDU5CYkUps2tRzWBIx1hfPbhzXaVNkPFcef8KDr6nNEyMPKBa1ckHo9qchRvJGXkYi%2BbTYGsYCL5ezBTpi8NdKJmV5FZLiOgm2OXINrkzpU1u7vIUv4dVnPscetes%2FEMeF9jmzf%2FZP2N6TN2uhusMactOncbO76XreR4sF994YgMAhMb33uJt6%2BfEMPn7k70GOqUBAUEYdoqFSp2puSV2dxt5vGcUgOFTiT7Zjzc1gBgFrwm5glYkKu9QOTk5n2KJtHDIWpekhfHR0ON8J0H8amOGNATOCig8xu%2B9IhUaOw%2BqvYMdBhBqwuj6IXEsadPm70ubcgGomfT9BfE3FOIOyxDcSdnWnfr29YH7%2FFLxLgkrlKuh4irfUdQv9laWcgq7lzMzcLnloNCfyn8DbgbFG%2BDZZxVpsMXn&X-Amz-Signature=71a5667ff9df1a379c9221d378ed44238c31a78eb83d0285b0dea4f41ad70b40&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHMO2J5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIAczpOmiBHEb9%2BX%2FsQvskQohYYoTcEXuvEBfxwvVJ6GaAiEAh3KCxu1sx8XjjXHBwJ24l6%2B7ed0r1tBQnW2tfQZf%2FYwq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBsT%2FOpFilmMcTb%2BhircA6Jfi8%2B4rWeEqtZJkz09Fkt9vczc2%2BD0%2BHTh6rtCS0rdsW1LmXe5HkhDCObI738t4MTQrHNygN7dhwsrcgGjtNigv2yxbkIwRCSw%2Ffh5gi1kXgp4oMBqPnF%2BQR8fr0cDs7s5YZ88TRSOYHK8jM6SKojE6amWZ9oJJ3BO7xoNJneBlQ85gpU1SVkIMAIB6EacU7OIgpOX4ExLOaSXFBTGfnazaouSh1Az1HSQeEiSJyh8W6ANdRW4fUlw%2Bw28C00rb6jcdnXREPIfXR%2B6coDbbWYRUIFJQiWd5Fwm6j3Wg99Pq9WbcfMB7Ziu7zUQyEpP7nB4ES2ixq1rokuRxZO1uojUMnJhJfqzlblg%2BWOoyA1POewJEDuwqUDZeFJHq9LV%2BsWqz9UXqpR9%2BKPnKAd65VqQhqqcHqRtiUksKfqcFpLSr1ArXcNM9QEA8hUDsUELfiNRDU5CYkUps2tRzWBIx1hfPbhzXaVNkPFcef8KDr6nNEyMPKBa1ckHo9qchRvJGXkYi%2BbTYGsYCL5ezBTpi8NdKJmV5FZLiOgm2OXINrkzpU1u7vIUv4dVnPscetes%2FEMeF9jmzf%2FZP2N6TN2uhusMactOncbO76XreR4sF994YgMAhMb33uJt6%2BfEMPn7k70GOqUBAUEYdoqFSp2puSV2dxt5vGcUgOFTiT7Zjzc1gBgFrwm5glYkKu9QOTk5n2KJtHDIWpekhfHR0ON8J0H8amOGNATOCig8xu%2B9IhUaOw%2BqvYMdBhBqwuj6IXEsadPm70ubcgGomfT9BfE3FOIOyxDcSdnWnfr29YH7%2FFLxLgkrlKuh4irfUdQv9laWcgq7lzMzcLnloNCfyn8DbgbFG%2BDZZxVpsMXn&X-Amz-Signature=55a9a6587d81a0d8095891d9847b3a85c3dc64c2693af1681b6d7c695c30e1ec&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP5FLQI7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQC09Nw%2FDgbQILh5DnlHFdQ9RfHgvHXnYQwSnzyY4aLzWgIgaW70a7EL%2FtDDZqhTSfJwphnf%2FbSzaSJ08B8G7d%2B%2BJ9Aq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDO1K57lscZU2z2LfgSrcA4kD1n%2Bgt3m%2BaTujvOnyvXWVWsemKeBfIEQEy%2Faym%2BVNEJf7GadLTcmruih8YyAtgNKkLAD9daAOLHAeP9Bkx1oSNyjr2yyVJ1Lu%2Bu7cHvPkUAtu12ziu%2FdeGjgXLfiaK2kOJCR8WSJ9y%2FTqapWPqjMhV6ZRvvNGmdn0Gt%2F9wyM6Fb7y8vtRMHLMGvYGL0wfqqI7euCNKtguIhlidehlKY%2FXaBctAe8C4fArSdwT%2FyyJsF6ZfYtqmA9D3%2Fk2qJ9J4LYspA8C0Ws%2BMEOce8GIvS1ckQMSe9xRF5K9FU%2BFOIhXnHoFg07OinDAECyUXwnPEZ%2BJUffDzkKJeNxOLtPULH201uHx0mo0I4ZMmaUKIDGhRJRLdo1T4W%2FKZ8wKCDykE6HZ6SE3sgwL9WyngOuwqRC9k2cZZm2LqXUA93qupGT6wKK%2BMDG7sNmjy%2BxqQDyjOmorVlsBrr67xxbYfQRVTVlRF6Vg768Wv4K25n1vY5sjk%2FM6oTbEDO7pz81tIYcpCGDK6TVm%2BM9i5ItIqu%2BZDlLsonKzTDFBW1%2BuQzPt48XTPKTOzWThViCAkiHPbyK4XWbu1LuuIBdbeJb5BfgDmRY9DPbSkjudo3NAsffHMYFP2s3P9t9Kyu8%2FT%2BcEMP77k70GOqUBfOneTPdT7QjMdAyUMXpCYL%2F85%2FTHcuxjY3%2BH2EJljja3IpLxZqkg%2FwcwHjPC%2FanAMypFXUkkZ9%2F6RSxa5xDvw3yceQwGxgQG9qqtPXbivKgTqICJlJZws9rMqdOMChbTqoOrezQ9%2F%2BlyYh4BTW5U%2BqqnEBY1kjTxNoIyAoqkmQ%2FPjslyGC4DeJCMRWPHIPrin8cOE%2BXnAtH8ZNUAyvcpAiAGSmeO&X-Amz-Signature=f61b2caaf2be26fae8b85e7e14687371a5666b8d9b4d6ce451813f99c75d8bab&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZP5FLQI7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQC09Nw%2FDgbQILh5DnlHFdQ9RfHgvHXnYQwSnzyY4aLzWgIgaW70a7EL%2FtDDZqhTSfJwphnf%2FbSzaSJ08B8G7d%2B%2BJ9Aq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDO1K57lscZU2z2LfgSrcA4kD1n%2Bgt3m%2BaTujvOnyvXWVWsemKeBfIEQEy%2Faym%2BVNEJf7GadLTcmruih8YyAtgNKkLAD9daAOLHAeP9Bkx1oSNyjr2yyVJ1Lu%2Bu7cHvPkUAtu12ziu%2FdeGjgXLfiaK2kOJCR8WSJ9y%2FTqapWPqjMhV6ZRvvNGmdn0Gt%2F9wyM6Fb7y8vtRMHLMGvYGL0wfqqI7euCNKtguIhlidehlKY%2FXaBctAe8C4fArSdwT%2FyyJsF6ZfYtqmA9D3%2Fk2qJ9J4LYspA8C0Ws%2BMEOce8GIvS1ckQMSe9xRF5K9FU%2BFOIhXnHoFg07OinDAECyUXwnPEZ%2BJUffDzkKJeNxOLtPULH201uHx0mo0I4ZMmaUKIDGhRJRLdo1T4W%2FKZ8wKCDykE6HZ6SE3sgwL9WyngOuwqRC9k2cZZm2LqXUA93qupGT6wKK%2BMDG7sNmjy%2BxqQDyjOmorVlsBrr67xxbYfQRVTVlRF6Vg768Wv4K25n1vY5sjk%2FM6oTbEDO7pz81tIYcpCGDK6TVm%2BM9i5ItIqu%2BZDlLsonKzTDFBW1%2BuQzPt48XTPKTOzWThViCAkiHPbyK4XWbu1LuuIBdbeJb5BfgDmRY9DPbSkjudo3NAsffHMYFP2s3P9t9Kyu8%2FT%2BcEMP77k70GOqUBfOneTPdT7QjMdAyUMXpCYL%2F85%2FTHcuxjY3%2BH2EJljja3IpLxZqkg%2FwcwHjPC%2FanAMypFXUkkZ9%2F6RSxa5xDvw3yceQwGxgQG9qqtPXbivKgTqICJlJZws9rMqdOMChbTqoOrezQ9%2F%2BlyYh4BTW5U%2BqqnEBY1kjTxNoIyAoqkmQ%2FPjslyGC4DeJCMRWPHIPrin8cOE%2BXnAtH8ZNUAyvcpAiAGSmeO&X-Amz-Signature=8ecaa2d2366c7465ac256779cbfb2b73c453375d8b0fe83b9cc6042c63f223b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHMO2J5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIAczpOmiBHEb9%2BX%2FsQvskQohYYoTcEXuvEBfxwvVJ6GaAiEAh3KCxu1sx8XjjXHBwJ24l6%2B7ed0r1tBQnW2tfQZf%2FYwq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDBsT%2FOpFilmMcTb%2BhircA6Jfi8%2B4rWeEqtZJkz09Fkt9vczc2%2BD0%2BHTh6rtCS0rdsW1LmXe5HkhDCObI738t4MTQrHNygN7dhwsrcgGjtNigv2yxbkIwRCSw%2Ffh5gi1kXgp4oMBqPnF%2BQR8fr0cDs7s5YZ88TRSOYHK8jM6SKojE6amWZ9oJJ3BO7xoNJneBlQ85gpU1SVkIMAIB6EacU7OIgpOX4ExLOaSXFBTGfnazaouSh1Az1HSQeEiSJyh8W6ANdRW4fUlw%2Bw28C00rb6jcdnXREPIfXR%2B6coDbbWYRUIFJQiWd5Fwm6j3Wg99Pq9WbcfMB7Ziu7zUQyEpP7nB4ES2ixq1rokuRxZO1uojUMnJhJfqzlblg%2BWOoyA1POewJEDuwqUDZeFJHq9LV%2BsWqz9UXqpR9%2BKPnKAd65VqQhqqcHqRtiUksKfqcFpLSr1ArXcNM9QEA8hUDsUELfiNRDU5CYkUps2tRzWBIx1hfPbhzXaVNkPFcef8KDr6nNEyMPKBa1ckHo9qchRvJGXkYi%2BbTYGsYCL5ezBTpi8NdKJmV5FZLiOgm2OXINrkzpU1u7vIUv4dVnPscetes%2FEMeF9jmzf%2FZP2N6TN2uhusMactOncbO76XreR4sF994YgMAhMb33uJt6%2BfEMPn7k70GOqUBAUEYdoqFSp2puSV2dxt5vGcUgOFTiT7Zjzc1gBgFrwm5glYkKu9QOTk5n2KJtHDIWpekhfHR0ON8J0H8amOGNATOCig8xu%2B9IhUaOw%2BqvYMdBhBqwuj6IXEsadPm70ubcgGomfT9BfE3FOIOyxDcSdnWnfr29YH7%2FFLxLgkrlKuh4irfUdQv9laWcgq7lzMzcLnloNCfyn8DbgbFG%2BDZZxVpsMXn&X-Amz-Signature=9dac653f4d7b4126c49eef5cfa4e0d01475c1ffcc28e0d4a1a42835ccab5f653&X-Amz-SignedHeaders=host&x-id=GetObject)
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