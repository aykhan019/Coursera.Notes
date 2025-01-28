

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKI6B2MK%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCjm4TyLJgPCsW8g%2B3RkzrTIYU2OKD9ZNvOhVTD1TSrGwIgO1OISWpmOAWnGzPXfoPRBP1bGlDELQQDxUwXf8A73qMq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDLbQPx7aY1woLVcHEyrcA4lhMtzoQK3SKpN7SEBHibbdxAnuRyLoQBbXZD2OBUi6YpjCGv0Db3oNEM1u7B0dwF1MlAIC439Ax%2Bmv3h%2FZIfEq45MZQ1zbNwDG7x%2FHaZE%2BVrwC2A5Vc8FUgEoLnNEqhQUERRjEdOpfS7PtSGH0rEpvuCPNLOMJ%2FT1RqVmyrarw86OUbfVqOe44SDPksUOE%2Fz7LKYKoxzJ2aq7JSiAslRCWzL6li07FNsVGE77kzWYbule4bjFNs%2BVH33KyAVLezHu5Y4qy%2F6z39GCw7uz6UU%2B%2BTNWaBqNU2P6EsIMK%2B8fAnKIyyYsasFWBTrga0jSnxdIsa%2FPm3I62xJZ%2B%2BiqLS4z6MGACHSitNrYSO3mGiFDvM4z%2BJonC8%2Bha0qyZyEa2MVuISp6yK%2FzHJ%2Fq048eG9kKf8n9pm6tdnE2X4KMvRChomTGdww9KWXsJD0OHyYKmirQHIGfJB%2Fpr4vWZo3Ff1LTouf8CgP8vveo%2F9z4fQs7SgVMW3zrTyxvRj9wF7vF7%2BzKvdJVBS7LMaB%2FBghAqYmjXQXPpSaonSR3Uo%2Fpvy0rART%2By%2FzouUVOd3TBa6vpp9rSfmta1peNHjgRXOq2HsCc8N2%2F%2BNx3zoFxQz17Wh%2Fwnyln56xtGSJeTMBhUMKCU5bwGOqUBTl0nKPbzzQLS%2BQnVWIyppDyngqf3v5SYTzyLvNAPgjn7oDQgiCmPLNx8862aqZYOqJ5Rq%2BSNUuZQa5cTgZ7bg2V%2BHvXBx9A7RDgp6VuaRidRI%2BAkOv4C%2Bg23j5DTEsQPF9%2FJqfy0ZCZ5mCHj2ClK9jS8sdjyR1ITvod8EuJeowTfCKIqvkes7M4bsrzgLkix%2Bqz%2BKybunAv99H0q8g1eYq17DIPZ&X-Amz-Signature=93a5ee2868ac358e77c63309317232704e739018d28f62736b83492dbbbf1086&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKI6B2MK%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCjm4TyLJgPCsW8g%2B3RkzrTIYU2OKD9ZNvOhVTD1TSrGwIgO1OISWpmOAWnGzPXfoPRBP1bGlDELQQDxUwXf8A73qMq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDLbQPx7aY1woLVcHEyrcA4lhMtzoQK3SKpN7SEBHibbdxAnuRyLoQBbXZD2OBUi6YpjCGv0Db3oNEM1u7B0dwF1MlAIC439Ax%2Bmv3h%2FZIfEq45MZQ1zbNwDG7x%2FHaZE%2BVrwC2A5Vc8FUgEoLnNEqhQUERRjEdOpfS7PtSGH0rEpvuCPNLOMJ%2FT1RqVmyrarw86OUbfVqOe44SDPksUOE%2Fz7LKYKoxzJ2aq7JSiAslRCWzL6li07FNsVGE77kzWYbule4bjFNs%2BVH33KyAVLezHu5Y4qy%2F6z39GCw7uz6UU%2B%2BTNWaBqNU2P6EsIMK%2B8fAnKIyyYsasFWBTrga0jSnxdIsa%2FPm3I62xJZ%2B%2BiqLS4z6MGACHSitNrYSO3mGiFDvM4z%2BJonC8%2Bha0qyZyEa2MVuISp6yK%2FzHJ%2Fq048eG9kKf8n9pm6tdnE2X4KMvRChomTGdww9KWXsJD0OHyYKmirQHIGfJB%2Fpr4vWZo3Ff1LTouf8CgP8vveo%2F9z4fQs7SgVMW3zrTyxvRj9wF7vF7%2BzKvdJVBS7LMaB%2FBghAqYmjXQXPpSaonSR3Uo%2Fpvy0rART%2By%2FzouUVOd3TBa6vpp9rSfmta1peNHjgRXOq2HsCc8N2%2F%2BNx3zoFxQz17Wh%2Fwnyln56xtGSJeTMBhUMKCU5bwGOqUBTl0nKPbzzQLS%2BQnVWIyppDyngqf3v5SYTzyLvNAPgjn7oDQgiCmPLNx8862aqZYOqJ5Rq%2BSNUuZQa5cTgZ7bg2V%2BHvXBx9A7RDgp6VuaRidRI%2BAkOv4C%2Bg23j5DTEsQPF9%2FJqfy0ZCZ5mCHj2ClK9jS8sdjyR1ITvod8EuJeowTfCKIqvkes7M4bsrzgLkix%2Bqz%2BKybunAv99H0q8g1eYq17DIPZ&X-Amz-Signature=9c53bd7f00856bcc0fd1320c4f79f65623335f2640c5828b9e70300446552e4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKI6B2MK%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCjm4TyLJgPCsW8g%2B3RkzrTIYU2OKD9ZNvOhVTD1TSrGwIgO1OISWpmOAWnGzPXfoPRBP1bGlDELQQDxUwXf8A73qMq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDLbQPx7aY1woLVcHEyrcA4lhMtzoQK3SKpN7SEBHibbdxAnuRyLoQBbXZD2OBUi6YpjCGv0Db3oNEM1u7B0dwF1MlAIC439Ax%2Bmv3h%2FZIfEq45MZQ1zbNwDG7x%2FHaZE%2BVrwC2A5Vc8FUgEoLnNEqhQUERRjEdOpfS7PtSGH0rEpvuCPNLOMJ%2FT1RqVmyrarw86OUbfVqOe44SDPksUOE%2Fz7LKYKoxzJ2aq7JSiAslRCWzL6li07FNsVGE77kzWYbule4bjFNs%2BVH33KyAVLezHu5Y4qy%2F6z39GCw7uz6UU%2B%2BTNWaBqNU2P6EsIMK%2B8fAnKIyyYsasFWBTrga0jSnxdIsa%2FPm3I62xJZ%2B%2BiqLS4z6MGACHSitNrYSO3mGiFDvM4z%2BJonC8%2Bha0qyZyEa2MVuISp6yK%2FzHJ%2Fq048eG9kKf8n9pm6tdnE2X4KMvRChomTGdww9KWXsJD0OHyYKmirQHIGfJB%2Fpr4vWZo3Ff1LTouf8CgP8vveo%2F9z4fQs7SgVMW3zrTyxvRj9wF7vF7%2BzKvdJVBS7LMaB%2FBghAqYmjXQXPpSaonSR3Uo%2Fpvy0rART%2By%2FzouUVOd3TBa6vpp9rSfmta1peNHjgRXOq2HsCc8N2%2F%2BNx3zoFxQz17Wh%2Fwnyln56xtGSJeTMBhUMKCU5bwGOqUBTl0nKPbzzQLS%2BQnVWIyppDyngqf3v5SYTzyLvNAPgjn7oDQgiCmPLNx8862aqZYOqJ5Rq%2BSNUuZQa5cTgZ7bg2V%2BHvXBx9A7RDgp6VuaRidRI%2BAkOv4C%2Bg23j5DTEsQPF9%2FJqfy0ZCZ5mCHj2ClK9jS8sdjyR1ITvod8EuJeowTfCKIqvkes7M4bsrzgLkix%2Bqz%2BKybunAv99H0q8g1eYq17DIPZ&X-Amz-Signature=7b267115f6f190db6069e45b678a2523a00ff701fbea4922a4bfb2544f247c99&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA6YB4PK%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIDlgVOPxKDGBzzdEeRUyKlRfuENo2nZmHQ28%2B9%2FspQsDAiEAyjQOQNhEiJssHFHW4wO9WRT662LNuVI1ZXQLFH5zST4q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDOhSU74avfEXW2960SrcA4flgjYZl9hvgSbHm0bZCLFC9E%2BkAmFy%2FQQpKMRqvFDmUSLkmAHwwLcjRQfsP1NZ548%2BvyREUyRdacWD5nDwHnmAkAX%2FSUWER2FCoXA3JnHf80Xl83j8D8hnP9i9Sh1h4C7UPWUJRuY2D0qxA5lHzVa%2FHDMuKFxjacE4tz6nBotgNzZhd9%2Fh3%2FpcdcpCOn5CVRBcPExwzVb0RZTsWDLWow86b2cSoygSxZwnJfGoTtQgV0gm%2FSmk8Oq2aA0xF44muCi79P4WbTOw36iQpXbQS%2FPpij9ztk2kM3GABxjvRgGnib7BMX6PzjlTqElIzvstkmxUtc2XybqGu1rv8DgccS14Dzl8w1ZX%2B3p401EL%2Fx9SD7KtsSujIhypPpIt33RY58FestSYpPoRd%2F9l9J5UvfTeqye89Fnq1rPK%2B%2BUid9Rw2Bdr%2BnLf6g9HR00m7H09ToGuJC%2BFgVSQCvSJGcLj1tgyChQk6ZKsRohDmpLntM4xHeZVaFjjAdy5KTewO0jI9Z5cRHrAQy9XHIyJ7MiJWuW4yZsA1Mr6RK8DgOUEQbQejeKxpRpV6SfPARVLA0Xoeq3BXBTaM%2Fa0FNquOxUjn6GdPemSEVuLQVN3f8iEbOJfLFdJnATE7d27NMOVMO2U5bwGOqUBNyukaG%2FAuWAAZdBLzZOD8SWOja9eB57KtOkLMOiTkEuj12kZVQ2jEt8dfSPmpwIm9pL1AJZ575UlCKwCEBMlqfw2pWeJu1ttNbDXRchVXZlNrK2XZxsbOMaYu2xGwm0aHDM2eztitOejWr4jhWgu254QLcK5d2Gx2ENVtJV2xeIX0bHDjXzTtP1xEav5eBr4lTR%2BSNU17E8p81I5Sfa7guZ37yRT&X-Amz-Signature=03c502eddcba7d55e2fc56870cca1e0ed81d4e873eb7176202714ffc6e32d337&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA6YB4PK%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIDlgVOPxKDGBzzdEeRUyKlRfuENo2nZmHQ28%2B9%2FspQsDAiEAyjQOQNhEiJssHFHW4wO9WRT662LNuVI1ZXQLFH5zST4q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDOhSU74avfEXW2960SrcA4flgjYZl9hvgSbHm0bZCLFC9E%2BkAmFy%2FQQpKMRqvFDmUSLkmAHwwLcjRQfsP1NZ548%2BvyREUyRdacWD5nDwHnmAkAX%2FSUWER2FCoXA3JnHf80Xl83j8D8hnP9i9Sh1h4C7UPWUJRuY2D0qxA5lHzVa%2FHDMuKFxjacE4tz6nBotgNzZhd9%2Fh3%2FpcdcpCOn5CVRBcPExwzVb0RZTsWDLWow86b2cSoygSxZwnJfGoTtQgV0gm%2FSmk8Oq2aA0xF44muCi79P4WbTOw36iQpXbQS%2FPpij9ztk2kM3GABxjvRgGnib7BMX6PzjlTqElIzvstkmxUtc2XybqGu1rv8DgccS14Dzl8w1ZX%2B3p401EL%2Fx9SD7KtsSujIhypPpIt33RY58FestSYpPoRd%2F9l9J5UvfTeqye89Fnq1rPK%2B%2BUid9Rw2Bdr%2BnLf6g9HR00m7H09ToGuJC%2BFgVSQCvSJGcLj1tgyChQk6ZKsRohDmpLntM4xHeZVaFjjAdy5KTewO0jI9Z5cRHrAQy9XHIyJ7MiJWuW4yZsA1Mr6RK8DgOUEQbQejeKxpRpV6SfPARVLA0Xoeq3BXBTaM%2Fa0FNquOxUjn6GdPemSEVuLQVN3f8iEbOJfLFdJnATE7d27NMOVMO2U5bwGOqUBNyukaG%2FAuWAAZdBLzZOD8SWOja9eB57KtOkLMOiTkEuj12kZVQ2jEt8dfSPmpwIm9pL1AJZ575UlCKwCEBMlqfw2pWeJu1ttNbDXRchVXZlNrK2XZxsbOMaYu2xGwm0aHDM2eztitOejWr4jhWgu254QLcK5d2Gx2ENVtJV2xeIX0bHDjXzTtP1xEav5eBr4lTR%2BSNU17E8p81I5Sfa7guZ37yRT&X-Amz-Signature=2813aae3bb13923034f3d4a527a2242bd3635d7326a2eab7a670ba4f4aca0ef5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKI6B2MK%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCjm4TyLJgPCsW8g%2B3RkzrTIYU2OKD9ZNvOhVTD1TSrGwIgO1OISWpmOAWnGzPXfoPRBP1bGlDELQQDxUwXf8A73qMq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDLbQPx7aY1woLVcHEyrcA4lhMtzoQK3SKpN7SEBHibbdxAnuRyLoQBbXZD2OBUi6YpjCGv0Db3oNEM1u7B0dwF1MlAIC439Ax%2Bmv3h%2FZIfEq45MZQ1zbNwDG7x%2FHaZE%2BVrwC2A5Vc8FUgEoLnNEqhQUERRjEdOpfS7PtSGH0rEpvuCPNLOMJ%2FT1RqVmyrarw86OUbfVqOe44SDPksUOE%2Fz7LKYKoxzJ2aq7JSiAslRCWzL6li07FNsVGE77kzWYbule4bjFNs%2BVH33KyAVLezHu5Y4qy%2F6z39GCw7uz6UU%2B%2BTNWaBqNU2P6EsIMK%2B8fAnKIyyYsasFWBTrga0jSnxdIsa%2FPm3I62xJZ%2B%2BiqLS4z6MGACHSitNrYSO3mGiFDvM4z%2BJonC8%2Bha0qyZyEa2MVuISp6yK%2FzHJ%2Fq048eG9kKf8n9pm6tdnE2X4KMvRChomTGdww9KWXsJD0OHyYKmirQHIGfJB%2Fpr4vWZo3Ff1LTouf8CgP8vveo%2F9z4fQs7SgVMW3zrTyxvRj9wF7vF7%2BzKvdJVBS7LMaB%2FBghAqYmjXQXPpSaonSR3Uo%2Fpvy0rART%2By%2FzouUVOd3TBa6vpp9rSfmta1peNHjgRXOq2HsCc8N2%2F%2BNx3zoFxQz17Wh%2Fwnyln56xtGSJeTMBhUMKCU5bwGOqUBTl0nKPbzzQLS%2BQnVWIyppDyngqf3v5SYTzyLvNAPgjn7oDQgiCmPLNx8862aqZYOqJ5Rq%2BSNUuZQa5cTgZ7bg2V%2BHvXBx9A7RDgp6VuaRidRI%2BAkOv4C%2Bg23j5DTEsQPF9%2FJqfy0ZCZ5mCHj2ClK9jS8sdjyR1ITvod8EuJeowTfCKIqvkes7M4bsrzgLkix%2Bqz%2BKybunAv99H0q8g1eYq17DIPZ&X-Amz-Signature=d13fb6e177195e6ed6e1b573d924e624a9567996eb22c1199096b7cc12e4396f&X-Amz-SignedHeaders=host&x-id=GetObject)
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