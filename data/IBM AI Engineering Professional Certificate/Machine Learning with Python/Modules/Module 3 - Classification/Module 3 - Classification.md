

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6BOO4VD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIBp3lp32EpL8ToX0WcowdxAfcr%2FKxPT76tA31FPAMc22AiEA%2BQrF0gdbnud%2BPs5nJ%2FJwIzihtBKARnZ3quBVR2EflwMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDJogHVjHPfrF7SOC1SrcA4uANf%2BnKGT7tSxXfZJD9atNe7%2Fs1oIoiIEiFe2MLYyZPA8rpjiU2IrSOmKA7UhQDQnOGJOl045dgVOOHhYC81B0eOK19tCyQgJDnuXdM8t%2B5rJ0yXd8gIEJRE8enmtMgyjIPspb4kGosLJ2X3U4k7IcEhRPX4WiYFW%2F4wUIK4H3mH59V%2Fk%2BnboKO9imKB52IMDazJCx0mYYN4JTbXqASFmORVVG7qpcBxetXHaB%2BQyKbIwF1cC5LJQHpRrMt7tHYJbeQYIbx4xs5rppaxnslhYtlt0CmzKPp2YD%2FPl6Plan03gAPm5hxMJ7c2TbF8%2FT2frbvLG5Yao0hT2vwIl0ozlSn%2FaOjlyTc4JxBUH9we4kY0ozPUOMdCPzLCmkAzpFiOIfxpwq2MbTggJQvUcROpRZrKDa88CUkz%2FtGd%2BtOivLJ8wcV2DMwUhxwNikSeoHdaWVTqcQGkeWVDr4wMlp%2BlGLJxAER%2F7FZldVZdYMmLdmHBBUct1O31Ap9MibyoOURmyAWt17A%2F1%2Be6e07UYJuxKkdbcEim9QZIjSPJRoT2vSQVRufCIVcTRq3h6VSHnzEStHzpz70yzu8trDdKXGyBymxFhIzUW%2FY%2BDPhveuELa%2FtAS7pS2YlYH14i%2BDMJWZmb0GOqUBF4LhGyXXep5bZxiRDTYdV%2BGz8RC7Zgdxc%2BhmueuoXCctjhCHO80veApLGays2TyR6dvesi6%2BmWMEcPgM4XWHWB%2FpJ%2Fa23t6Us4FM5Q9T%2FD%2BiOTFkrzCN22oPMR4UFOlqM4hcKtEhSn7FN0%2FkCqpWkC7dWo5m7R3fU4I%2FrqGHaONpIaq5qaAnF9wCGStmQMk8i2oBPSTsvtPcSvV%2Fq764aSxChlp7&X-Amz-Signature=e5cca5f976650d2a9595ee44b8484e71bb0a1473d6621168cc814e078b5ceacf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6BOO4VD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIBp3lp32EpL8ToX0WcowdxAfcr%2FKxPT76tA31FPAMc22AiEA%2BQrF0gdbnud%2BPs5nJ%2FJwIzihtBKARnZ3quBVR2EflwMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDJogHVjHPfrF7SOC1SrcA4uANf%2BnKGT7tSxXfZJD9atNe7%2Fs1oIoiIEiFe2MLYyZPA8rpjiU2IrSOmKA7UhQDQnOGJOl045dgVOOHhYC81B0eOK19tCyQgJDnuXdM8t%2B5rJ0yXd8gIEJRE8enmtMgyjIPspb4kGosLJ2X3U4k7IcEhRPX4WiYFW%2F4wUIK4H3mH59V%2Fk%2BnboKO9imKB52IMDazJCx0mYYN4JTbXqASFmORVVG7qpcBxetXHaB%2BQyKbIwF1cC5LJQHpRrMt7tHYJbeQYIbx4xs5rppaxnslhYtlt0CmzKPp2YD%2FPl6Plan03gAPm5hxMJ7c2TbF8%2FT2frbvLG5Yao0hT2vwIl0ozlSn%2FaOjlyTc4JxBUH9we4kY0ozPUOMdCPzLCmkAzpFiOIfxpwq2MbTggJQvUcROpRZrKDa88CUkz%2FtGd%2BtOivLJ8wcV2DMwUhxwNikSeoHdaWVTqcQGkeWVDr4wMlp%2BlGLJxAER%2F7FZldVZdYMmLdmHBBUct1O31Ap9MibyoOURmyAWt17A%2F1%2Be6e07UYJuxKkdbcEim9QZIjSPJRoT2vSQVRufCIVcTRq3h6VSHnzEStHzpz70yzu8trDdKXGyBymxFhIzUW%2FY%2BDPhveuELa%2FtAS7pS2YlYH14i%2BDMJWZmb0GOqUBF4LhGyXXep5bZxiRDTYdV%2BGz8RC7Zgdxc%2BhmueuoXCctjhCHO80veApLGays2TyR6dvesi6%2BmWMEcPgM4XWHWB%2FpJ%2Fa23t6Us4FM5Q9T%2FD%2BiOTFkrzCN22oPMR4UFOlqM4hcKtEhSn7FN0%2FkCqpWkC7dWo5m7R3fU4I%2FrqGHaONpIaq5qaAnF9wCGStmQMk8i2oBPSTsvtPcSvV%2Fq764aSxChlp7&X-Amz-Signature=0410839042c66362ae10ebfd9fdefdabec799a403a4640b025e2a1138e15858a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6BOO4VD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIBp3lp32EpL8ToX0WcowdxAfcr%2FKxPT76tA31FPAMc22AiEA%2BQrF0gdbnud%2BPs5nJ%2FJwIzihtBKARnZ3quBVR2EflwMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDJogHVjHPfrF7SOC1SrcA4uANf%2BnKGT7tSxXfZJD9atNe7%2Fs1oIoiIEiFe2MLYyZPA8rpjiU2IrSOmKA7UhQDQnOGJOl045dgVOOHhYC81B0eOK19tCyQgJDnuXdM8t%2B5rJ0yXd8gIEJRE8enmtMgyjIPspb4kGosLJ2X3U4k7IcEhRPX4WiYFW%2F4wUIK4H3mH59V%2Fk%2BnboKO9imKB52IMDazJCx0mYYN4JTbXqASFmORVVG7qpcBxetXHaB%2BQyKbIwF1cC5LJQHpRrMt7tHYJbeQYIbx4xs5rppaxnslhYtlt0CmzKPp2YD%2FPl6Plan03gAPm5hxMJ7c2TbF8%2FT2frbvLG5Yao0hT2vwIl0ozlSn%2FaOjlyTc4JxBUH9we4kY0ozPUOMdCPzLCmkAzpFiOIfxpwq2MbTggJQvUcROpRZrKDa88CUkz%2FtGd%2BtOivLJ8wcV2DMwUhxwNikSeoHdaWVTqcQGkeWVDr4wMlp%2BlGLJxAER%2F7FZldVZdYMmLdmHBBUct1O31Ap9MibyoOURmyAWt17A%2F1%2Be6e07UYJuxKkdbcEim9QZIjSPJRoT2vSQVRufCIVcTRq3h6VSHnzEStHzpz70yzu8trDdKXGyBymxFhIzUW%2FY%2BDPhveuELa%2FtAS7pS2YlYH14i%2BDMJWZmb0GOqUBF4LhGyXXep5bZxiRDTYdV%2BGz8RC7Zgdxc%2BhmueuoXCctjhCHO80veApLGays2TyR6dvesi6%2BmWMEcPgM4XWHWB%2FpJ%2Fa23t6Us4FM5Q9T%2FD%2BiOTFkrzCN22oPMR4UFOlqM4hcKtEhSn7FN0%2FkCqpWkC7dWo5m7R3fU4I%2FrqGHaONpIaq5qaAnF9wCGStmQMk8i2oBPSTsvtPcSvV%2Fq764aSxChlp7&X-Amz-Signature=fbd4d4ee908b4bc1020bd282aa89a00e0b81d83a45e6453427b2a171cdde6754&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SP3N4III%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCA%2ByXsf%2BKn7dtn994E%2FgLFKUYP%2FfN%2FcldG33QXuafqqwIhALRxFBGZvUXL2%2FbEDbLv%2BswehiuB8pZFgzOpxmUpmCeaKv8DCHsQABoMNjM3NDIzMTgzODA1IgxYh7RG6iU5vkCLSM0q3AMfpHUi5msrP4El0bneznqmQXXyAO3QxnBQ5G%2B5GTZomlNM8v1ecb3xE%2BBYGUsGnY1jH%2B16o4lMf6AzbaZVnMoTAxez8phyxJADfJSajcM5A8Ro969pf%2FHYFuaiXNnbqrmqD%2B8lnjQnbC66a6a3alcMXaXmqy6DbbWcfDwlXuw10wvSn2SJHFFv7TcBvurbdP53OJNPRrV6085C4KB4bDYVLJPmMS3xCdbMAYYwlQbojHOJgmro%2FP%2BbW6T3ahN7YHIwVWHB%2FvKU%2Fhjlb3fQM07sj7NYTFe9P369Sy8BFtvQvLzb%2FYroSdz3NJb%2FHrbNLqg0MlBtyGx2rwsIef1iwQvM9SufIN%2FZEIeo%2FkIT9bFhudR%2FSNLGvQQhyVCUxdWQ9YdrmxBjU95YI6Vk%2FZXGC1sgfrQOYPHRrd%2Ba4O18qyyomwKYJCLQ3m2EXXuRJRA05HIvd0I94rCsvXgNxbRKOoVn13Z3TDfYIcOY57fqli1A4dbqqClpvONLQuL84cZHz26t0d%2BmF56Dy%2FKdJoiEuUIUWbnI4bW9HXA5CLAZAwkt1AY3qxQmGcGlCYB473qJfO7gki2wkKiMTheCCaf8dUGaHQb8TO2FKtlJJlmG5gFY%2FPAWpSDxXjd%2BwMMyFTCrmZm9BjqkAXzevTirfRs62UduX1LPFKH5ezVDzv32PQBTHYPyLmvzQVLkQTMjEtKkdzzio2ILRA4%2BWl31OaKiBLwvThwzC8bpumd1zbePxJRSvKdpIe0rVds8NkTlUR30ClXZ5fO%2FnfkSkof%2BkgGeZDT3CFb%2FFWsKQJQlpcI0LtMaczDXXcDWr8vZH0nqkE1IbJSjgykvL2VJb8ysO3m1lTgsNg9711cRXKhd&X-Amz-Signature=2ca916909d6431b3a0b9feddb0645b259f20de6aa30b01121ae0b81395ab8a1e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SP3N4III%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCA%2ByXsf%2BKn7dtn994E%2FgLFKUYP%2FfN%2FcldG33QXuafqqwIhALRxFBGZvUXL2%2FbEDbLv%2BswehiuB8pZFgzOpxmUpmCeaKv8DCHsQABoMNjM3NDIzMTgzODA1IgxYh7RG6iU5vkCLSM0q3AMfpHUi5msrP4El0bneznqmQXXyAO3QxnBQ5G%2B5GTZomlNM8v1ecb3xE%2BBYGUsGnY1jH%2B16o4lMf6AzbaZVnMoTAxez8phyxJADfJSajcM5A8Ro969pf%2FHYFuaiXNnbqrmqD%2B8lnjQnbC66a6a3alcMXaXmqy6DbbWcfDwlXuw10wvSn2SJHFFv7TcBvurbdP53OJNPRrV6085C4KB4bDYVLJPmMS3xCdbMAYYwlQbojHOJgmro%2FP%2BbW6T3ahN7YHIwVWHB%2FvKU%2Fhjlb3fQM07sj7NYTFe9P369Sy8BFtvQvLzb%2FYroSdz3NJb%2FHrbNLqg0MlBtyGx2rwsIef1iwQvM9SufIN%2FZEIeo%2FkIT9bFhudR%2FSNLGvQQhyVCUxdWQ9YdrmxBjU95YI6Vk%2FZXGC1sgfrQOYPHRrd%2Ba4O18qyyomwKYJCLQ3m2EXXuRJRA05HIvd0I94rCsvXgNxbRKOoVn13Z3TDfYIcOY57fqli1A4dbqqClpvONLQuL84cZHz26t0d%2BmF56Dy%2FKdJoiEuUIUWbnI4bW9HXA5CLAZAwkt1AY3qxQmGcGlCYB473qJfO7gki2wkKiMTheCCaf8dUGaHQb8TO2FKtlJJlmG5gFY%2FPAWpSDxXjd%2BwMMyFTCrmZm9BjqkAXzevTirfRs62UduX1LPFKH5ezVDzv32PQBTHYPyLmvzQVLkQTMjEtKkdzzio2ILRA4%2BWl31OaKiBLwvThwzC8bpumd1zbePxJRSvKdpIe0rVds8NkTlUR30ClXZ5fO%2FnfkSkof%2BkgGeZDT3CFb%2FFWsKQJQlpcI0LtMaczDXXcDWr8vZH0nqkE1IbJSjgykvL2VJb8ysO3m1lTgsNg9711cRXKhd&X-Amz-Signature=ea8394bc088fedbd7b01d96ec4b78483e36d74a099f343c409d0a0182f4bccd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6BOO4VD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIBp3lp32EpL8ToX0WcowdxAfcr%2FKxPT76tA31FPAMc22AiEA%2BQrF0gdbnud%2BPs5nJ%2FJwIzihtBKARnZ3quBVR2EflwMq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDJogHVjHPfrF7SOC1SrcA4uANf%2BnKGT7tSxXfZJD9atNe7%2Fs1oIoiIEiFe2MLYyZPA8rpjiU2IrSOmKA7UhQDQnOGJOl045dgVOOHhYC81B0eOK19tCyQgJDnuXdM8t%2B5rJ0yXd8gIEJRE8enmtMgyjIPspb4kGosLJ2X3U4k7IcEhRPX4WiYFW%2F4wUIK4H3mH59V%2Fk%2BnboKO9imKB52IMDazJCx0mYYN4JTbXqASFmORVVG7qpcBxetXHaB%2BQyKbIwF1cC5LJQHpRrMt7tHYJbeQYIbx4xs5rppaxnslhYtlt0CmzKPp2YD%2FPl6Plan03gAPm5hxMJ7c2TbF8%2FT2frbvLG5Yao0hT2vwIl0ozlSn%2FaOjlyTc4JxBUH9we4kY0ozPUOMdCPzLCmkAzpFiOIfxpwq2MbTggJQvUcROpRZrKDa88CUkz%2FtGd%2BtOivLJ8wcV2DMwUhxwNikSeoHdaWVTqcQGkeWVDr4wMlp%2BlGLJxAER%2F7FZldVZdYMmLdmHBBUct1O31Ap9MibyoOURmyAWt17A%2F1%2Be6e07UYJuxKkdbcEim9QZIjSPJRoT2vSQVRufCIVcTRq3h6VSHnzEStHzpz70yzu8trDdKXGyBymxFhIzUW%2FY%2BDPhveuELa%2FtAS7pS2YlYH14i%2BDMJWZmb0GOqUBF4LhGyXXep5bZxiRDTYdV%2BGz8RC7Zgdxc%2BhmueuoXCctjhCHO80veApLGays2TyR6dvesi6%2BmWMEcPgM4XWHWB%2FpJ%2Fa23t6Us4FM5Q9T%2FD%2BiOTFkrzCN22oPMR4UFOlqM4hcKtEhSn7FN0%2FkCqpWkC7dWo5m7R3fU4I%2FrqGHaONpIaq5qaAnF9wCGStmQMk8i2oBPSTsvtPcSvV%2Fq764aSxChlp7&X-Amz-Signature=a25fefdd274d9cb749a27551705d980ccdf7db7c8c7df45bf8ea69c310ffc8cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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