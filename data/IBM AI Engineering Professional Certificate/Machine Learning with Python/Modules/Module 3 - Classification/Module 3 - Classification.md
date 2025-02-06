

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHCZN3KM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDHaDmZqeLOQMe9RYsQchGL9zof2etss1hDrch3hUIZOgIhAOYMYCP12TChczRigSAenl1iN3w8BaD21b5KKCDEwmRRKv8DCFoQABoMNjM3NDIzMTgzODA1IgyNlCgYMT5XtfvIJDEq3AOGyVwCKTg19AlkwkTh7W%2BAEfZZBBFb5sR1BR%2Fvl2XUPNf%2BGY879PuIYYtFaW6hcdBK%2FiEPzWr1nkN28wQo3tYbLKVzV2rdnOPLW2u5aZkY9ZdbsEOKRx31gDXQVtB%2BmADP3CKzkhl08sWn9Y0cVQFTgJMebkOgsUionVHc%2BrUP7xfdFbyqeIrAJNBcFUf%2B2IL3sKqhEX8sIJephQWi68nt77yqcZh4zp8Tti86PWqLFkeiQhXj926%2BzPrvR32r2gU%2BXmMdjK9Ck7jUky4xhB4krt2MI%2Fl4ruQKd6HWNSYLrHbQFMXXXe3%2BuPFXAPtAdomaoZ9l5jvRrrm5QqWSZAnFTCRp3dk9jUaVts6xLK3rP%2FDy9aveqVyWBHcmTV%2BrldX2USG72phw3RFDEPmGOKrMle27IJ%2F2ylxsendQ5A1Gp4flc%2Fv9nhC7H7YJ78Owe38atO8RHkkFvJHLxztdiZm1XggaMkFB4wiq46hiGdJoLEWjq0PqgR5XGcr%2FBNEfNLvOoikc12NpghNXsomz8UHs7z%2BjxoifdoyAQn3LBjBlXWIwBOMRxqZ2hrF4N5yBOsYccRDsNAqgM3z6zUVpTua3HaLkoYYPIjB6aWO59PIn6hoRNiUeusCIgw5PczCq7JG9BjqkAQps3wMDsStRViTY4HpCTjma9v0Ldnse28x8vW8XI%2FMrcoRGc04J494dEk3M3yh4h7bVAdnNcGx2ZHOx%2B6jQYioiyqvjpZ9ZFGniE5ud06DvC%2Fdio3q6qTFwTtIId9Q9MrgqFFxCyjWDj5HiaJy165qFlt2f9lezdv3esATvgYIT7DhqGHZqOk7ob29pC5InoS2H1KrZJL7iL5qZ%2B3bTw8uH3231&X-Amz-Signature=d23f9e983e7117aff4403a085a9e69f0b9dccba06396fcbafd91f2cc58c807a2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHCZN3KM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDHaDmZqeLOQMe9RYsQchGL9zof2etss1hDrch3hUIZOgIhAOYMYCP12TChczRigSAenl1iN3w8BaD21b5KKCDEwmRRKv8DCFoQABoMNjM3NDIzMTgzODA1IgyNlCgYMT5XtfvIJDEq3AOGyVwCKTg19AlkwkTh7W%2BAEfZZBBFb5sR1BR%2Fvl2XUPNf%2BGY879PuIYYtFaW6hcdBK%2FiEPzWr1nkN28wQo3tYbLKVzV2rdnOPLW2u5aZkY9ZdbsEOKRx31gDXQVtB%2BmADP3CKzkhl08sWn9Y0cVQFTgJMebkOgsUionVHc%2BrUP7xfdFbyqeIrAJNBcFUf%2B2IL3sKqhEX8sIJephQWi68nt77yqcZh4zp8Tti86PWqLFkeiQhXj926%2BzPrvR32r2gU%2BXmMdjK9Ck7jUky4xhB4krt2MI%2Fl4ruQKd6HWNSYLrHbQFMXXXe3%2BuPFXAPtAdomaoZ9l5jvRrrm5QqWSZAnFTCRp3dk9jUaVts6xLK3rP%2FDy9aveqVyWBHcmTV%2BrldX2USG72phw3RFDEPmGOKrMle27IJ%2F2ylxsendQ5A1Gp4flc%2Fv9nhC7H7YJ78Owe38atO8RHkkFvJHLxztdiZm1XggaMkFB4wiq46hiGdJoLEWjq0PqgR5XGcr%2FBNEfNLvOoikc12NpghNXsomz8UHs7z%2BjxoifdoyAQn3LBjBlXWIwBOMRxqZ2hrF4N5yBOsYccRDsNAqgM3z6zUVpTua3HaLkoYYPIjB6aWO59PIn6hoRNiUeusCIgw5PczCq7JG9BjqkAQps3wMDsStRViTY4HpCTjma9v0Ldnse28x8vW8XI%2FMrcoRGc04J494dEk3M3yh4h7bVAdnNcGx2ZHOx%2B6jQYioiyqvjpZ9ZFGniE5ud06DvC%2Fdio3q6qTFwTtIId9Q9MrgqFFxCyjWDj5HiaJy165qFlt2f9lezdv3esATvgYIT7DhqGHZqOk7ob29pC5InoS2H1KrZJL7iL5qZ%2B3bTw8uH3231&X-Amz-Signature=092a3eeb65afba9be9aeb0c685401258f8132b71e617a9fb91fd780738b479ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHCZN3KM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDHaDmZqeLOQMe9RYsQchGL9zof2etss1hDrch3hUIZOgIhAOYMYCP12TChczRigSAenl1iN3w8BaD21b5KKCDEwmRRKv8DCFoQABoMNjM3NDIzMTgzODA1IgyNlCgYMT5XtfvIJDEq3AOGyVwCKTg19AlkwkTh7W%2BAEfZZBBFb5sR1BR%2Fvl2XUPNf%2BGY879PuIYYtFaW6hcdBK%2FiEPzWr1nkN28wQo3tYbLKVzV2rdnOPLW2u5aZkY9ZdbsEOKRx31gDXQVtB%2BmADP3CKzkhl08sWn9Y0cVQFTgJMebkOgsUionVHc%2BrUP7xfdFbyqeIrAJNBcFUf%2B2IL3sKqhEX8sIJephQWi68nt77yqcZh4zp8Tti86PWqLFkeiQhXj926%2BzPrvR32r2gU%2BXmMdjK9Ck7jUky4xhB4krt2MI%2Fl4ruQKd6HWNSYLrHbQFMXXXe3%2BuPFXAPtAdomaoZ9l5jvRrrm5QqWSZAnFTCRp3dk9jUaVts6xLK3rP%2FDy9aveqVyWBHcmTV%2BrldX2USG72phw3RFDEPmGOKrMle27IJ%2F2ylxsendQ5A1Gp4flc%2Fv9nhC7H7YJ78Owe38atO8RHkkFvJHLxztdiZm1XggaMkFB4wiq46hiGdJoLEWjq0PqgR5XGcr%2FBNEfNLvOoikc12NpghNXsomz8UHs7z%2BjxoifdoyAQn3LBjBlXWIwBOMRxqZ2hrF4N5yBOsYccRDsNAqgM3z6zUVpTua3HaLkoYYPIjB6aWO59PIn6hoRNiUeusCIgw5PczCq7JG9BjqkAQps3wMDsStRViTY4HpCTjma9v0Ldnse28x8vW8XI%2FMrcoRGc04J494dEk3M3yh4h7bVAdnNcGx2ZHOx%2B6jQYioiyqvjpZ9ZFGniE5ud06DvC%2Fdio3q6qTFwTtIId9Q9MrgqFFxCyjWDj5HiaJy165qFlt2f9lezdv3esATvgYIT7DhqGHZqOk7ob29pC5InoS2H1KrZJL7iL5qZ%2B3bTw8uH3231&X-Amz-Signature=7432671ba764dd95321bc36a0afb313c60a97f92fd6ae1ac8ec95242a1973f7a&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RJFMMCP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDd88iz8zpImn2eXKMhzdecZOXgX%2BXfIuAnW9PhlADeogIhAMyx6FmRHXnIdGpu3MDwiROjzVU%2BWyw8HvaURtu1bV%2B6Kv8DCFoQABoMNjM3NDIzMTgzODA1IgxsvAmk%2BLYr6Vujzdcq3AMyXxc%2FeZ0ebnRTlx%2B6qALmnOYzm6W9LarOKrfF54Pp06As%2BXGxK5OVFOyDS7LWZj3z1w0WdnySDW272us95jaDCgukszyAVPyhBkojJ%2FCX4fQt3%2FflnUgPPumhxLhL0qRdywF3IY1kWXc%2Bcx2d3BaOQfXbOLA5eHNCvFGKP95E%2BJJshFO2smXxR%2FiBpiiDnp5eOyPfHiEGM4D7%2BZOgtod5PmFCSFgeR3ZYKJx%2Fzpg0TpCkc%2FOW85hvQ5uqMGZfWaK1iUBnCOClbHG5ZmSR0nQ2lDy%2B46xcMchtaoDBJB364up6%2Bme4U4VqZ4eN1QS4GsGiOWwK0usKyTMgpsB6wSfHQR1wP8iceA05nwcmUpRHIg1mrEEIMCt7Ar1PomoMH3J17TOdkArmTJHtppw37C%2FiiDfcXY8QmV%2BzX5K6alJRD7Ct1uzuf%2FR72R20EwmHkwzr%2FOxenO5XcYYo6D0ueFIzNWkXPApcClwqrqrSUhV94lt7aKvsTPFJrVi4NJika2268rmZhIc2q4ydWH53jSKGJRcTyv8%2BLbOcXO%2Bpx9DXlW8DOdGd69DXjiWTjkZXEKObvwevvaZEcC0TcceYHAOUe6rIFP%2Bf%2FewQfWjv89apQKmsuFPMyUsq9WfP6TCJ7JG9BjqkAVujtvh5eGCs0LVfJJDzqdvzf1jQQakOrm13zRrKHmUShd3gwdh6PYuddgXN74awDNycltkGjCtnW91%2Br%2FNkE88KgsOKVWuZlBeaIdC5R%2By9Agheo264fh6ajpqu60s2kAvxn4xHz1Ah%2FJhaROkMGnx3M9TDF5ozryPsU9eVPhQzxjEZIZQYui0t5vD7Zrqb40U6gt8SOb5KWXwEBD3%2BAeCFeATh&X-Amz-Signature=662aebd7967070d77ff44f510ae9325c541d6f0a301a84b6ad7025d509aaf7a4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RJFMMCP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDd88iz8zpImn2eXKMhzdecZOXgX%2BXfIuAnW9PhlADeogIhAMyx6FmRHXnIdGpu3MDwiROjzVU%2BWyw8HvaURtu1bV%2B6Kv8DCFoQABoMNjM3NDIzMTgzODA1IgxsvAmk%2BLYr6Vujzdcq3AMyXxc%2FeZ0ebnRTlx%2B6qALmnOYzm6W9LarOKrfF54Pp06As%2BXGxK5OVFOyDS7LWZj3z1w0WdnySDW272us95jaDCgukszyAVPyhBkojJ%2FCX4fQt3%2FflnUgPPumhxLhL0qRdywF3IY1kWXc%2Bcx2d3BaOQfXbOLA5eHNCvFGKP95E%2BJJshFO2smXxR%2FiBpiiDnp5eOyPfHiEGM4D7%2BZOgtod5PmFCSFgeR3ZYKJx%2Fzpg0TpCkc%2FOW85hvQ5uqMGZfWaK1iUBnCOClbHG5ZmSR0nQ2lDy%2B46xcMchtaoDBJB364up6%2Bme4U4VqZ4eN1QS4GsGiOWwK0usKyTMgpsB6wSfHQR1wP8iceA05nwcmUpRHIg1mrEEIMCt7Ar1PomoMH3J17TOdkArmTJHtppw37C%2FiiDfcXY8QmV%2BzX5K6alJRD7Ct1uzuf%2FR72R20EwmHkwzr%2FOxenO5XcYYo6D0ueFIzNWkXPApcClwqrqrSUhV94lt7aKvsTPFJrVi4NJika2268rmZhIc2q4ydWH53jSKGJRcTyv8%2BLbOcXO%2Bpx9DXlW8DOdGd69DXjiWTjkZXEKObvwevvaZEcC0TcceYHAOUe6rIFP%2Bf%2FewQfWjv89apQKmsuFPMyUsq9WfP6TCJ7JG9BjqkAVujtvh5eGCs0LVfJJDzqdvzf1jQQakOrm13zRrKHmUShd3gwdh6PYuddgXN74awDNycltkGjCtnW91%2Br%2FNkE88KgsOKVWuZlBeaIdC5R%2By9Agheo264fh6ajpqu60s2kAvxn4xHz1Ah%2FJhaROkMGnx3M9TDF5ozryPsU9eVPhQzxjEZIZQYui0t5vD7Zrqb40U6gt8SOb5KWXwEBD3%2BAeCFeATh&X-Amz-Signature=43d064afaed11c7d2cd71dbf190db27f9d607effaeca563b49740e39141ceb53&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHCZN3KM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDHaDmZqeLOQMe9RYsQchGL9zof2etss1hDrch3hUIZOgIhAOYMYCP12TChczRigSAenl1iN3w8BaD21b5KKCDEwmRRKv8DCFoQABoMNjM3NDIzMTgzODA1IgyNlCgYMT5XtfvIJDEq3AOGyVwCKTg19AlkwkTh7W%2BAEfZZBBFb5sR1BR%2Fvl2XUPNf%2BGY879PuIYYtFaW6hcdBK%2FiEPzWr1nkN28wQo3tYbLKVzV2rdnOPLW2u5aZkY9ZdbsEOKRx31gDXQVtB%2BmADP3CKzkhl08sWn9Y0cVQFTgJMebkOgsUionVHc%2BrUP7xfdFbyqeIrAJNBcFUf%2B2IL3sKqhEX8sIJephQWi68nt77yqcZh4zp8Tti86PWqLFkeiQhXj926%2BzPrvR32r2gU%2BXmMdjK9Ck7jUky4xhB4krt2MI%2Fl4ruQKd6HWNSYLrHbQFMXXXe3%2BuPFXAPtAdomaoZ9l5jvRrrm5QqWSZAnFTCRp3dk9jUaVts6xLK3rP%2FDy9aveqVyWBHcmTV%2BrldX2USG72phw3RFDEPmGOKrMle27IJ%2F2ylxsendQ5A1Gp4flc%2Fv9nhC7H7YJ78Owe38atO8RHkkFvJHLxztdiZm1XggaMkFB4wiq46hiGdJoLEWjq0PqgR5XGcr%2FBNEfNLvOoikc12NpghNXsomz8UHs7z%2BjxoifdoyAQn3LBjBlXWIwBOMRxqZ2hrF4N5yBOsYccRDsNAqgM3z6zUVpTua3HaLkoYYPIjB6aWO59PIn6hoRNiUeusCIgw5PczCq7JG9BjqkAQps3wMDsStRViTY4HpCTjma9v0Ldnse28x8vW8XI%2FMrcoRGc04J494dEk3M3yh4h7bVAdnNcGx2ZHOx%2B6jQYioiyqvjpZ9ZFGniE5ud06DvC%2Fdio3q6qTFwTtIId9Q9MrgqFFxCyjWDj5HiaJy165qFlt2f9lezdv3esATvgYIT7DhqGHZqOk7ob29pC5InoS2H1KrZJL7iL5qZ%2B3bTw8uH3231&X-Amz-Signature=dc4017d52783f5158a40c8bc879ecb296d254c7a8e630b115e3091b2806e1c05&X-Amz-SignedHeaders=host&x-id=GetObject)
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