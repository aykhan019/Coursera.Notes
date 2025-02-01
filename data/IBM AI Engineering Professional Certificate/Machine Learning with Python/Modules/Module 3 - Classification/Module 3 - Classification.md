

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTMC7NN7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDftniRbCwcK1omFUTMa76rPPSSHpvfzQbxhvWWwprTRQIgLiO4Mca0ddWxqxxpa%2FRpxcfQ3B1GDNwNVCtYAjRvrMkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgKi6iEbrtoySK8ayrcA9%2Bx%2F1zJ9cscgi3qRwL8yLoQ2vowPJbOtCFGsl6yZk4mO0%2FRT4i%2BkxytAERlobiAz9KVMWN3SSfSalm%2FgOnvnvG%2FyeLg6aA7%2BrHa7JVkqMW%2FCd9dU5cngaHS0x9u8ZLOa1jKapn8n9Q%2Bah3AkZTuHMf4vzI7rYeCRzaZxK2YPSUJHmaVZbVwF6z2TMquGCmi%2BVXD4rGPLFhtQVXo9iUXfWNdM0C17cfL%2BvNDJekdM8rLymUkVsaBdi4rhvdNwLoS6rT0WYHRXDd3K467t3uMlXY%2FEgPImKlcG7AxyFFcvEeZW2RPW03jF11SAt0sFMqACn%2BrOiI7CCigvdnC5BX8IzEg5w9Iurg5kPTmHB39vgEsr8eqFyUrUab95ASYwWIYOu5cbzseO9MidO4clEMiykwuibi3%2F%2FQgnhbje4vN6aYPW8aV4%2BGDtHqLVh9wGkuhsf2ukVbeCU750EWctZxNEQO8h7%2Bhi0BtpuesFblcdiFs1QIqel%2FrhN1aZZxSHh4EAKkp%2BLCU6RN9Jj2g9MjfwUAl4dTDuMbs4eSFVwDncmQbLAXdoEANUDhHNhr2WYD4nl6Fc1Mn0V6wolssH5wbcbaCQfF1zyAq%2Fp87idC%2BiAWTqsezRItMDIBm61MTMPvJ%2BLwGOqUBr016u1NQOjkJ3RZh0M5NAeZNNnFX5k40ER0FbuK2S0RWjnez8vsiqCT%2F8L%2BeDIhPxWo8%2BzayKL84JLdfZ1xyLfYvYW7komJs%2BBIkuz1lnwbKvLZmNlTlgmsnjjOZ1d7Vcj0IxmqOVmX5vyPb0eDQ7ARJKRXjnq8DmcTfclC0WkD1O6K6XcbdVmuKtGn2LsL0zoAp0LaDCmEFIuoFvU4uv%2BNrGJF3&X-Amz-Signature=81457d76f1d732fdd8d3acbcf254bce3aa01fba9bbd9b63ad349aea0c009d308&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTMC7NN7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDftniRbCwcK1omFUTMa76rPPSSHpvfzQbxhvWWwprTRQIgLiO4Mca0ddWxqxxpa%2FRpxcfQ3B1GDNwNVCtYAjRvrMkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgKi6iEbrtoySK8ayrcA9%2Bx%2F1zJ9cscgi3qRwL8yLoQ2vowPJbOtCFGsl6yZk4mO0%2FRT4i%2BkxytAERlobiAz9KVMWN3SSfSalm%2FgOnvnvG%2FyeLg6aA7%2BrHa7JVkqMW%2FCd9dU5cngaHS0x9u8ZLOa1jKapn8n9Q%2Bah3AkZTuHMf4vzI7rYeCRzaZxK2YPSUJHmaVZbVwF6z2TMquGCmi%2BVXD4rGPLFhtQVXo9iUXfWNdM0C17cfL%2BvNDJekdM8rLymUkVsaBdi4rhvdNwLoS6rT0WYHRXDd3K467t3uMlXY%2FEgPImKlcG7AxyFFcvEeZW2RPW03jF11SAt0sFMqACn%2BrOiI7CCigvdnC5BX8IzEg5w9Iurg5kPTmHB39vgEsr8eqFyUrUab95ASYwWIYOu5cbzseO9MidO4clEMiykwuibi3%2F%2FQgnhbje4vN6aYPW8aV4%2BGDtHqLVh9wGkuhsf2ukVbeCU750EWctZxNEQO8h7%2Bhi0BtpuesFblcdiFs1QIqel%2FrhN1aZZxSHh4EAKkp%2BLCU6RN9Jj2g9MjfwUAl4dTDuMbs4eSFVwDncmQbLAXdoEANUDhHNhr2WYD4nl6Fc1Mn0V6wolssH5wbcbaCQfF1zyAq%2Fp87idC%2BiAWTqsezRItMDIBm61MTMPvJ%2BLwGOqUBr016u1NQOjkJ3RZh0M5NAeZNNnFX5k40ER0FbuK2S0RWjnez8vsiqCT%2F8L%2BeDIhPxWo8%2BzayKL84JLdfZ1xyLfYvYW7komJs%2BBIkuz1lnwbKvLZmNlTlgmsnjjOZ1d7Vcj0IxmqOVmX5vyPb0eDQ7ARJKRXjnq8DmcTfclC0WkD1O6K6XcbdVmuKtGn2LsL0zoAp0LaDCmEFIuoFvU4uv%2BNrGJF3&X-Amz-Signature=c04c24296ac0ea40b587bdedce91ef98885c132fc7779a0bf0a7c4ea43521c9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTMC7NN7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDftniRbCwcK1omFUTMa76rPPSSHpvfzQbxhvWWwprTRQIgLiO4Mca0ddWxqxxpa%2FRpxcfQ3B1GDNwNVCtYAjRvrMkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgKi6iEbrtoySK8ayrcA9%2Bx%2F1zJ9cscgi3qRwL8yLoQ2vowPJbOtCFGsl6yZk4mO0%2FRT4i%2BkxytAERlobiAz9KVMWN3SSfSalm%2FgOnvnvG%2FyeLg6aA7%2BrHa7JVkqMW%2FCd9dU5cngaHS0x9u8ZLOa1jKapn8n9Q%2Bah3AkZTuHMf4vzI7rYeCRzaZxK2YPSUJHmaVZbVwF6z2TMquGCmi%2BVXD4rGPLFhtQVXo9iUXfWNdM0C17cfL%2BvNDJekdM8rLymUkVsaBdi4rhvdNwLoS6rT0WYHRXDd3K467t3uMlXY%2FEgPImKlcG7AxyFFcvEeZW2RPW03jF11SAt0sFMqACn%2BrOiI7CCigvdnC5BX8IzEg5w9Iurg5kPTmHB39vgEsr8eqFyUrUab95ASYwWIYOu5cbzseO9MidO4clEMiykwuibi3%2F%2FQgnhbje4vN6aYPW8aV4%2BGDtHqLVh9wGkuhsf2ukVbeCU750EWctZxNEQO8h7%2Bhi0BtpuesFblcdiFs1QIqel%2FrhN1aZZxSHh4EAKkp%2BLCU6RN9Jj2g9MjfwUAl4dTDuMbs4eSFVwDncmQbLAXdoEANUDhHNhr2WYD4nl6Fc1Mn0V6wolssH5wbcbaCQfF1zyAq%2Fp87idC%2BiAWTqsezRItMDIBm61MTMPvJ%2BLwGOqUBr016u1NQOjkJ3RZh0M5NAeZNNnFX5k40ER0FbuK2S0RWjnez8vsiqCT%2F8L%2BeDIhPxWo8%2BzayKL84JLdfZ1xyLfYvYW7komJs%2BBIkuz1lnwbKvLZmNlTlgmsnjjOZ1d7Vcj0IxmqOVmX5vyPb0eDQ7ARJKRXjnq8DmcTfclC0WkD1O6K6XcbdVmuKtGn2LsL0zoAp0LaDCmEFIuoFvU4uv%2BNrGJF3&X-Amz-Signature=c12f23e68bf981596b59abe28e8652a8850f7d83efa2aee584928619566fe66c&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WXXYS3T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHqv3iCw%2BTGXt93a%2BvxJeNIM9G3IW3bfVBvgw%2FKf7VqMAiEAgKpeThnUzEUtYoIBni5HcY8LNQK4rxMotLRM9PvhUIwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMthTq8G2PaLDQZruircA8QluEVylnwNlyJQVgddte67P0MKpNVCj9ojDC7vl8buS2gtZso6C1dtYwCFBJC0TIiXG%2FwALn%2BsI%2FCQ7xiJgmwp%2BZf%2FFzqf%2FAa3cqrF7d8296wcmvz91C3F0QtXXldIz976wcGagmTKVPk%2B2bgyPaDBk8WNFBGYW4MvBa5OsO%2FDPVh0FC5j1p5zBQdQXIEWkpCepJ%2BdR5t2sjXKzLt4%2FzuweaJqj%2BgHBN4NcPjvUnrVbIScfN%2Bkjs6cJ0K90z80J0RHrn6T4oiclR9BcdTg5CKzyeQ2J2IJhoTgmLKRpIQgf1qxj%2FMHbdLMIPv84bzu9CmvkkrHEQxo8ERB8AIN51mFlKc2IKlRlaezSqcb1YwwaZnBscYKrfmGVQ0tdwlB82%2BstM38%2FUurvYVEjnG5SF4lt3KYxoFu8TBVQghLhTPGBGzNEWKdxOeV6G2zhi6POlBKAFkuB1Lv3HbRxiiud6SoZCQoABbjVzCrXUM52eO1%2BndqSHXxp7v%2FRFPEPp0yZRynDnPQRZwY5CEVaJ78FjxNcEexFM0Zd4F%2Funl7HvNy0%2Bn7Q9UfUZogKlXeK5oDParnxVUs9iS%2B7zalUhVeB3WLj2Zn2RaHKDBjb91EgY1PF%2F%2FI8uN5%2BvBA6pkDMMrB%2BLwGOqUBS%2FYHS6tyl5T6uFyDdNStDd5QAtH71KeDrlGvRjAglvRrpoUWAvuV2fl%2Fn8kWpY1MTEaOGqxQyLUBwY4VRuQPT8CmW%2BqbEbtlIz8AU860ewgobz0T62kAe411diSD1FByFtRUFizjQnobv7ozGAXVQUB5LtAOpo052cuwvlVOK7MB4V4EB9G65fV4dpuYCsr6NHkVylG%2FeUIAnrztu8vJIec8iU%2Br&X-Amz-Signature=0926f8856495d6a427cdd134e0e1624911d6ad97738e548b30f1700222ba0c6c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WXXYS3T%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHqv3iCw%2BTGXt93a%2BvxJeNIM9G3IW3bfVBvgw%2FKf7VqMAiEAgKpeThnUzEUtYoIBni5HcY8LNQK4rxMotLRM9PvhUIwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMthTq8G2PaLDQZruircA8QluEVylnwNlyJQVgddte67P0MKpNVCj9ojDC7vl8buS2gtZso6C1dtYwCFBJC0TIiXG%2FwALn%2BsI%2FCQ7xiJgmwp%2BZf%2FFzqf%2FAa3cqrF7d8296wcmvz91C3F0QtXXldIz976wcGagmTKVPk%2B2bgyPaDBk8WNFBGYW4MvBa5OsO%2FDPVh0FC5j1p5zBQdQXIEWkpCepJ%2BdR5t2sjXKzLt4%2FzuweaJqj%2BgHBN4NcPjvUnrVbIScfN%2Bkjs6cJ0K90z80J0RHrn6T4oiclR9BcdTg5CKzyeQ2J2IJhoTgmLKRpIQgf1qxj%2FMHbdLMIPv84bzu9CmvkkrHEQxo8ERB8AIN51mFlKc2IKlRlaezSqcb1YwwaZnBscYKrfmGVQ0tdwlB82%2BstM38%2FUurvYVEjnG5SF4lt3KYxoFu8TBVQghLhTPGBGzNEWKdxOeV6G2zhi6POlBKAFkuB1Lv3HbRxiiud6SoZCQoABbjVzCrXUM52eO1%2BndqSHXxp7v%2FRFPEPp0yZRynDnPQRZwY5CEVaJ78FjxNcEexFM0Zd4F%2Funl7HvNy0%2Bn7Q9UfUZogKlXeK5oDParnxVUs9iS%2B7zalUhVeB3WLj2Zn2RaHKDBjb91EgY1PF%2F%2FI8uN5%2BvBA6pkDMMrB%2BLwGOqUBS%2FYHS6tyl5T6uFyDdNStDd5QAtH71KeDrlGvRjAglvRrpoUWAvuV2fl%2Fn8kWpY1MTEaOGqxQyLUBwY4VRuQPT8CmW%2BqbEbtlIz8AU860ewgobz0T62kAe411diSD1FByFtRUFizjQnobv7ozGAXVQUB5LtAOpo052cuwvlVOK7MB4V4EB9G65fV4dpuYCsr6NHkVylG%2FeUIAnrztu8vJIec8iU%2Br&X-Amz-Signature=c6e349f703e0bc3655f20af71ce5e583113167b8ab0a25b212ae6a20196e44c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTMC7NN7%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T171235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDftniRbCwcK1omFUTMa76rPPSSHpvfzQbxhvWWwprTRQIgLiO4Mca0ddWxqxxpa%2FRpxcfQ3B1GDNwNVCtYAjRvrMkqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgKi6iEbrtoySK8ayrcA9%2Bx%2F1zJ9cscgi3qRwL8yLoQ2vowPJbOtCFGsl6yZk4mO0%2FRT4i%2BkxytAERlobiAz9KVMWN3SSfSalm%2FgOnvnvG%2FyeLg6aA7%2BrHa7JVkqMW%2FCd9dU5cngaHS0x9u8ZLOa1jKapn8n9Q%2Bah3AkZTuHMf4vzI7rYeCRzaZxK2YPSUJHmaVZbVwF6z2TMquGCmi%2BVXD4rGPLFhtQVXo9iUXfWNdM0C17cfL%2BvNDJekdM8rLymUkVsaBdi4rhvdNwLoS6rT0WYHRXDd3K467t3uMlXY%2FEgPImKlcG7AxyFFcvEeZW2RPW03jF11SAt0sFMqACn%2BrOiI7CCigvdnC5BX8IzEg5w9Iurg5kPTmHB39vgEsr8eqFyUrUab95ASYwWIYOu5cbzseO9MidO4clEMiykwuibi3%2F%2FQgnhbje4vN6aYPW8aV4%2BGDtHqLVh9wGkuhsf2ukVbeCU750EWctZxNEQO8h7%2Bhi0BtpuesFblcdiFs1QIqel%2FrhN1aZZxSHh4EAKkp%2BLCU6RN9Jj2g9MjfwUAl4dTDuMbs4eSFVwDncmQbLAXdoEANUDhHNhr2WYD4nl6Fc1Mn0V6wolssH5wbcbaCQfF1zyAq%2Fp87idC%2BiAWTqsezRItMDIBm61MTMPvJ%2BLwGOqUBr016u1NQOjkJ3RZh0M5NAeZNNnFX5k40ER0FbuK2S0RWjnez8vsiqCT%2F8L%2BeDIhPxWo8%2BzayKL84JLdfZ1xyLfYvYW7komJs%2BBIkuz1lnwbKvLZmNlTlgmsnjjOZ1d7Vcj0IxmqOVmX5vyPb0eDQ7ARJKRXjnq8DmcTfclC0WkD1O6K6XcbdVmuKtGn2LsL0zoAp0LaDCmEFIuoFvU4uv%2BNrGJF3&X-Amz-Signature=49f98f99a3c467db4556cab0b58f5e2516a85ef5deecff17f84d222769ccfc70&X-Amz-SignedHeaders=host&x-id=GetObject)
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