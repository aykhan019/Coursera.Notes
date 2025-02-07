

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633FICHEC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCICmB2HAfJ65iIOVdVGNIGSsHSmocX2VBkX73hea%2B1KbXAiBmDZOPk7VKfREDra4Fq8MoFL1Ba6iuO7WZlOqwgna9syr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMJ%2B54o9KRJB8EmRM0KtwDZY5TQIlObobWbx6tuw8Hvybf%2BQ8BD7dOlpmGZ1N3WyDq9QEi7oZJzQD1i%2BciRGGfj%2BemT3UQ%2FqfR2LqcrbA0hMVTFsUkLED5W8W3fer6kIyOB5T9cBu5HEzZaVUvF6t5UPhg4oYTQxRZMz9YdZOnHm4uFhCMYP83g9jNzCBnk97DgzuKnTbmBFWvGW5JdTXzSJ731Z0PpWP6AB6kh%2BzB%2BRc%2F9O9Tl%2BxYFL3MpyxtG3fBlmOFSZsNZs5qkSzNlxV%2FAjOUwm7DomqRSgArrwbBQ7Xd3u5kCYzVliZTS4VuD0MCiyP9di4rccGWmkK0RtiuMtF93TS2CVf%2FLE6ShHLQJI6V0bRwUDFacvERy7%2Br1va2l3Fz3TQ5M37gWxq%2FxOSZsTB82UIovuIcEWpB5GUj1%2BPOvFf0rXxkzz6xbEjL9s9L2X%2Fc5ABPxjGsSXF%2Bxx8F%2Fnpl6Hin9SrAXWlFaUoaZoPndmlizM4RJmlES82A7yTP4%2BMK0IoHbKT2%2FJPUOeFl7LbHP8w7guJb%2FHntENb7lonpU%2B1UwwFyaQnxS9TejFOwuj4qK%2FFEFtiuws16eteriFsFuRfrhQWz02V54Yk%2BVJli8BQC6HJhKuXCWWdclpVlk9pDFymVSp8PQTIwn96WvQY6pgHv0pLecOt%2Fg0V%2ByJA8S6bYkNrx20MYxC2m1IyY%2FhtLUSTl6eRVdb6cFtiUgn9hm47D7VKRlwN6hk7f1AL9LN1XOBUlD5oRLoj1w8b3rtayvZhADcokByZSX2NZuWX6k4gfoFZ5m2SrgwFcLUUc2Ze%2Bp4jA308GqXuM%2Bwen2Js3s685hmY11zQNkslquTa8ntCjYxhtoc%2FhVe9fAXEzUtHy1Qe3Lnqp&X-Amz-Signature=684ec324e3a3ca648c5dcf18b56716ad8854df78262cb6b16eaaef2d75a97e3a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633FICHEC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCICmB2HAfJ65iIOVdVGNIGSsHSmocX2VBkX73hea%2B1KbXAiBmDZOPk7VKfREDra4Fq8MoFL1Ba6iuO7WZlOqwgna9syr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMJ%2B54o9KRJB8EmRM0KtwDZY5TQIlObobWbx6tuw8Hvybf%2BQ8BD7dOlpmGZ1N3WyDq9QEi7oZJzQD1i%2BciRGGfj%2BemT3UQ%2FqfR2LqcrbA0hMVTFsUkLED5W8W3fer6kIyOB5T9cBu5HEzZaVUvF6t5UPhg4oYTQxRZMz9YdZOnHm4uFhCMYP83g9jNzCBnk97DgzuKnTbmBFWvGW5JdTXzSJ731Z0PpWP6AB6kh%2BzB%2BRc%2F9O9Tl%2BxYFL3MpyxtG3fBlmOFSZsNZs5qkSzNlxV%2FAjOUwm7DomqRSgArrwbBQ7Xd3u5kCYzVliZTS4VuD0MCiyP9di4rccGWmkK0RtiuMtF93TS2CVf%2FLE6ShHLQJI6V0bRwUDFacvERy7%2Br1va2l3Fz3TQ5M37gWxq%2FxOSZsTB82UIovuIcEWpB5GUj1%2BPOvFf0rXxkzz6xbEjL9s9L2X%2Fc5ABPxjGsSXF%2Bxx8F%2Fnpl6Hin9SrAXWlFaUoaZoPndmlizM4RJmlES82A7yTP4%2BMK0IoHbKT2%2FJPUOeFl7LbHP8w7guJb%2FHntENb7lonpU%2B1UwwFyaQnxS9TejFOwuj4qK%2FFEFtiuws16eteriFsFuRfrhQWz02V54Yk%2BVJli8BQC6HJhKuXCWWdclpVlk9pDFymVSp8PQTIwn96WvQY6pgHv0pLecOt%2Fg0V%2ByJA8S6bYkNrx20MYxC2m1IyY%2FhtLUSTl6eRVdb6cFtiUgn9hm47D7VKRlwN6hk7f1AL9LN1XOBUlD5oRLoj1w8b3rtayvZhADcokByZSX2NZuWX6k4gfoFZ5m2SrgwFcLUUc2Ze%2Bp4jA308GqXuM%2Bwen2Js3s685hmY11zQNkslquTa8ntCjYxhtoc%2FhVe9fAXEzUtHy1Qe3Lnqp&X-Amz-Signature=e4cbc0b6faffd531190c9866e107616ca34f1691582293dc34bfef9543e07e68&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633FICHEC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCICmB2HAfJ65iIOVdVGNIGSsHSmocX2VBkX73hea%2B1KbXAiBmDZOPk7VKfREDra4Fq8MoFL1Ba6iuO7WZlOqwgna9syr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMJ%2B54o9KRJB8EmRM0KtwDZY5TQIlObobWbx6tuw8Hvybf%2BQ8BD7dOlpmGZ1N3WyDq9QEi7oZJzQD1i%2BciRGGfj%2BemT3UQ%2FqfR2LqcrbA0hMVTFsUkLED5W8W3fer6kIyOB5T9cBu5HEzZaVUvF6t5UPhg4oYTQxRZMz9YdZOnHm4uFhCMYP83g9jNzCBnk97DgzuKnTbmBFWvGW5JdTXzSJ731Z0PpWP6AB6kh%2BzB%2BRc%2F9O9Tl%2BxYFL3MpyxtG3fBlmOFSZsNZs5qkSzNlxV%2FAjOUwm7DomqRSgArrwbBQ7Xd3u5kCYzVliZTS4VuD0MCiyP9di4rccGWmkK0RtiuMtF93TS2CVf%2FLE6ShHLQJI6V0bRwUDFacvERy7%2Br1va2l3Fz3TQ5M37gWxq%2FxOSZsTB82UIovuIcEWpB5GUj1%2BPOvFf0rXxkzz6xbEjL9s9L2X%2Fc5ABPxjGsSXF%2Bxx8F%2Fnpl6Hin9SrAXWlFaUoaZoPndmlizM4RJmlES82A7yTP4%2BMK0IoHbKT2%2FJPUOeFl7LbHP8w7guJb%2FHntENb7lonpU%2B1UwwFyaQnxS9TejFOwuj4qK%2FFEFtiuws16eteriFsFuRfrhQWz02V54Yk%2BVJli8BQC6HJhKuXCWWdclpVlk9pDFymVSp8PQTIwn96WvQY6pgHv0pLecOt%2Fg0V%2ByJA8S6bYkNrx20MYxC2m1IyY%2FhtLUSTl6eRVdb6cFtiUgn9hm47D7VKRlwN6hk7f1AL9LN1XOBUlD5oRLoj1w8b3rtayvZhADcokByZSX2NZuWX6k4gfoFZ5m2SrgwFcLUUc2Ze%2Bp4jA308GqXuM%2Bwen2Js3s685hmY11zQNkslquTa8ntCjYxhtoc%2FhVe9fAXEzUtHy1Qe3Lnqp&X-Amz-Signature=2c0b0af2dbd1f8981492e6b7e5eb7ff808e2da41ba168676361dd90b417b9304&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUIDWYT4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIBL4rZd9JpH%2BJ48XBYOjczEfIgIHBWaUtee0R5%2Fa7LWOAiAn59enN334OIHcsNLl%2FpXx8uZ1BoTVwYp8n%2B8Q2mWggSr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMu1SUIj6iGkuxiFzJKtwDxE03n0R1qMLivl3qtbwBtwwMMIkFjZKrcTP94StGGPcwi5K7%2BAvFW3Jqa3hHSYDFNlGdUDgCCw3nwHb1DD2zRBHU%2BTpY%2BNOs%2FFzaTF2PZA07WKuoalJcGwQOhWtqZFgPdbjjL6JK5a1vBzX1a3b5btwZEOPoKaCAYBLHkpYNwPJPxQ9rdsDlbJ%2BDxkvpDdoO%2BsvrtNe%2B0LIh%2B%2BuTblZJ%2F5kOYMPMDhQW1JHa9wlAT%2Fpk%2B%2BfXWIYoAfMHtPKi9yxtfPuouWj0EHYM77DBj8Mr3tDoRuFw86vAIXKfRHEAmbMAxZTnOKMJ29o2NSAyNFEikNbo9NvpgF%2B8RWXtYd2M%2B5qXZUJFwQ2nSHnjjKZ2sYp56MsPLPlEvFMaE0D8WTMfhV1JKfgHooEBFUge6uwiOOMaHWVhJzMj6Nmr6O1oCIzihifKwvhaFsE2tTAvGzFhR6wrhHirfgal8la7W7MxdGLrtTOHuPLhGmTIGuuKBVvPP4of793Bp87pW6VhO1fFvVLN%2BIl77gB81zEuHoaktZltd4ovUIKZinruPfr7dHCbUM7YnWaLa0wj0E7Hncs24da8y4jjRplTLx0KPXo2MC%2BE2cVE70nvxGUMPqvOFFrGWFojPCjLv0c6Hukw%2FtyWvQY6pgF7Z4uEO39yVWkev6JRIDxO808I6dToOjzMSzromS8UUur4%2FycifkfiG%2BXBoZaatI5Xempd%2FBYZDK03uA5Vy%2FHhKYCgFGad2EGGSl%2BvHadNq5o7fk81qjkRnPNuUgE1KoNW%2FQNwBqJ3uj1YDu7BYygOKN2l53ZatYwzQvh%2FH4Gic3UWpvbyDu21YTLb%2FvKgdY%2FC7uf4KwYFurqVP40MEd5AV1jr20Lh&X-Amz-Signature=b8f288708df0173330249ad653a9301b3bdbfa968d0097218a12c9f01d69bbae&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUIDWYT4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIBL4rZd9JpH%2BJ48XBYOjczEfIgIHBWaUtee0R5%2Fa7LWOAiAn59enN334OIHcsNLl%2FpXx8uZ1BoTVwYp8n%2B8Q2mWggSr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMu1SUIj6iGkuxiFzJKtwDxE03n0R1qMLivl3qtbwBtwwMMIkFjZKrcTP94StGGPcwi5K7%2BAvFW3Jqa3hHSYDFNlGdUDgCCw3nwHb1DD2zRBHU%2BTpY%2BNOs%2FFzaTF2PZA07WKuoalJcGwQOhWtqZFgPdbjjL6JK5a1vBzX1a3b5btwZEOPoKaCAYBLHkpYNwPJPxQ9rdsDlbJ%2BDxkvpDdoO%2BsvrtNe%2B0LIh%2B%2BuTblZJ%2F5kOYMPMDhQW1JHa9wlAT%2Fpk%2B%2BfXWIYoAfMHtPKi9yxtfPuouWj0EHYM77DBj8Mr3tDoRuFw86vAIXKfRHEAmbMAxZTnOKMJ29o2NSAyNFEikNbo9NvpgF%2B8RWXtYd2M%2B5qXZUJFwQ2nSHnjjKZ2sYp56MsPLPlEvFMaE0D8WTMfhV1JKfgHooEBFUge6uwiOOMaHWVhJzMj6Nmr6O1oCIzihifKwvhaFsE2tTAvGzFhR6wrhHirfgal8la7W7MxdGLrtTOHuPLhGmTIGuuKBVvPP4of793Bp87pW6VhO1fFvVLN%2BIl77gB81zEuHoaktZltd4ovUIKZinruPfr7dHCbUM7YnWaLa0wj0E7Hncs24da8y4jjRplTLx0KPXo2MC%2BE2cVE70nvxGUMPqvOFFrGWFojPCjLv0c6Hukw%2FtyWvQY6pgF7Z4uEO39yVWkev6JRIDxO808I6dToOjzMSzromS8UUur4%2FycifkfiG%2BXBoZaatI5Xempd%2FBYZDK03uA5Vy%2FHhKYCgFGad2EGGSl%2BvHadNq5o7fk81qjkRnPNuUgE1KoNW%2FQNwBqJ3uj1YDu7BYygOKN2l53ZatYwzQvh%2FH4Gic3UWpvbyDu21YTLb%2FvKgdY%2FC7uf4KwYFurqVP40MEd5AV1jr20Lh&X-Amz-Signature=4f9cdcb21b0085f7994f1901e2c1c1a60aba166fd00137f9a3d4e45a1bc7dd00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633FICHEC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCICmB2HAfJ65iIOVdVGNIGSsHSmocX2VBkX73hea%2B1KbXAiBmDZOPk7VKfREDra4Fq8MoFL1Ba6iuO7WZlOqwgna9syr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMJ%2B54o9KRJB8EmRM0KtwDZY5TQIlObobWbx6tuw8Hvybf%2BQ8BD7dOlpmGZ1N3WyDq9QEi7oZJzQD1i%2BciRGGfj%2BemT3UQ%2FqfR2LqcrbA0hMVTFsUkLED5W8W3fer6kIyOB5T9cBu5HEzZaVUvF6t5UPhg4oYTQxRZMz9YdZOnHm4uFhCMYP83g9jNzCBnk97DgzuKnTbmBFWvGW5JdTXzSJ731Z0PpWP6AB6kh%2BzB%2BRc%2F9O9Tl%2BxYFL3MpyxtG3fBlmOFSZsNZs5qkSzNlxV%2FAjOUwm7DomqRSgArrwbBQ7Xd3u5kCYzVliZTS4VuD0MCiyP9di4rccGWmkK0RtiuMtF93TS2CVf%2FLE6ShHLQJI6V0bRwUDFacvERy7%2Br1va2l3Fz3TQ5M37gWxq%2FxOSZsTB82UIovuIcEWpB5GUj1%2BPOvFf0rXxkzz6xbEjL9s9L2X%2Fc5ABPxjGsSXF%2Bxx8F%2Fnpl6Hin9SrAXWlFaUoaZoPndmlizM4RJmlES82A7yTP4%2BMK0IoHbKT2%2FJPUOeFl7LbHP8w7guJb%2FHntENb7lonpU%2B1UwwFyaQnxS9TejFOwuj4qK%2FFEFtiuws16eteriFsFuRfrhQWz02V54Yk%2BVJli8BQC6HJhKuXCWWdclpVlk9pDFymVSp8PQTIwn96WvQY6pgHv0pLecOt%2Fg0V%2ByJA8S6bYkNrx20MYxC2m1IyY%2FhtLUSTl6eRVdb6cFtiUgn9hm47D7VKRlwN6hk7f1AL9LN1XOBUlD5oRLoj1w8b3rtayvZhADcokByZSX2NZuWX6k4gfoFZ5m2SrgwFcLUUc2Ze%2Bp4jA308GqXuM%2Bwen2Js3s685hmY11zQNkslquTa8ntCjYxhtoc%2FhVe9fAXEzUtHy1Qe3Lnqp&X-Amz-Signature=10cda06b2cb4ae09d8c04765ac5dfe1ce484ac9c7e42e84196487acffa69f9f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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