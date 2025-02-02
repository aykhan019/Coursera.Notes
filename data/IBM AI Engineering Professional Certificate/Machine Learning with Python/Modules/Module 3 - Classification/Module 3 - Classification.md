

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEN5O7QL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMVi1U2R%2BzavxO8z3zo0TXQacNIvxiIYVf4g2HowwmEAiBeYNzGaecHBh71ifneIwCtOvQn3O5o%2BIhaPNa%2BmQic0yqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcNHL2%2FVMjrjFczYWKtwDHpWwDNMfpTm%2FdMAlZps%2FPHba8lNj2CfqTA5ydQcpPcD8hdsmhWpWZnhp0v2C%2BSrjHcsIX1F5gxN4Ks8EhJjMCOcjI3ChNdkXnwz8GhrQkMJrqZuycvXYjTSauuJ5xbkhv0zNzIWqKSv1t5zzbYoQ6ssZXeIODSppENC6hn5GOZoZIV9EloejJBbejYxACceIdSnPS0MxvjGNLgNIqmo%2FKoKEKA3dDuUK4u2V9m8gxHSB2XEWO7qgqZLnseBBH9PEOCqB1rIeAntYEl4FvqM%2B%2FM%2BuheVxgLHbJXBYHYG2%2FY%2BiI%2FrWBl4ghi97v4ezRYj3k12mi%2FwRDh6ebMOUEKo02dqrRR4hYT%2Bf7Y69Oa6N%2FJUJq62fSC6XUMjHqeyop%2BeMYAuvX7Wwsw9%2F2hZLvyeGr%2BUEzGYpm4Ysl9xbzH9eqvKuDg6GmjcZJfiUSLwAOOEdwdPbgMUnQJuRnogJHLmm9SmSdFQZWChsFAo6qYr7oPr3P0X4T34vhaNPM5RtP8AzI%2BIOuOC5%2Bu3iUCyySgMzbwTmu9470EAiOVZRZKpJZUqbBCocQQt8IL1J1rmxTM9glrln%2FImL1MjHKQd4PIB%2BalksBpb8njQw6lxKvbWgve4keITiMc8LK%2Fx6PPMwluP%2BvAY6pgH4vvPavQRyp9ASWB7%2BVau1Sh7XkKvgPPSCTPPiCb%2F%2Byx%2FgnHxsjda4ntALSjfdo90AfItChlssj05CJ62NxNBnTkNDEHNooQZaEsycsRA3cuY66jN7WAvCmAuAx6wc8WOPAOfAMzR64F3lovHe6qn7YyUI8Ionxf2ti%2B9bwJoSrhIEqd5wcjhaQy6i6TvOv4uwPO6NP4YXJv8DiTnfiA8qREYfKeUV&X-Amz-Signature=076a3c4afc14e2d5f5b2033ca7488cbccc5d851b11091174ead7806981ec39d1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEN5O7QL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMVi1U2R%2BzavxO8z3zo0TXQacNIvxiIYVf4g2HowwmEAiBeYNzGaecHBh71ifneIwCtOvQn3O5o%2BIhaPNa%2BmQic0yqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcNHL2%2FVMjrjFczYWKtwDHpWwDNMfpTm%2FdMAlZps%2FPHba8lNj2CfqTA5ydQcpPcD8hdsmhWpWZnhp0v2C%2BSrjHcsIX1F5gxN4Ks8EhJjMCOcjI3ChNdkXnwz8GhrQkMJrqZuycvXYjTSauuJ5xbkhv0zNzIWqKSv1t5zzbYoQ6ssZXeIODSppENC6hn5GOZoZIV9EloejJBbejYxACceIdSnPS0MxvjGNLgNIqmo%2FKoKEKA3dDuUK4u2V9m8gxHSB2XEWO7qgqZLnseBBH9PEOCqB1rIeAntYEl4FvqM%2B%2FM%2BuheVxgLHbJXBYHYG2%2FY%2BiI%2FrWBl4ghi97v4ezRYj3k12mi%2FwRDh6ebMOUEKo02dqrRR4hYT%2Bf7Y69Oa6N%2FJUJq62fSC6XUMjHqeyop%2BeMYAuvX7Wwsw9%2F2hZLvyeGr%2BUEzGYpm4Ysl9xbzH9eqvKuDg6GmjcZJfiUSLwAOOEdwdPbgMUnQJuRnogJHLmm9SmSdFQZWChsFAo6qYr7oPr3P0X4T34vhaNPM5RtP8AzI%2BIOuOC5%2Bu3iUCyySgMzbwTmu9470EAiOVZRZKpJZUqbBCocQQt8IL1J1rmxTM9glrln%2FImL1MjHKQd4PIB%2BalksBpb8njQw6lxKvbWgve4keITiMc8LK%2Fx6PPMwluP%2BvAY6pgH4vvPavQRyp9ASWB7%2BVau1Sh7XkKvgPPSCTPPiCb%2F%2Byx%2FgnHxsjda4ntALSjfdo90AfItChlssj05CJ62NxNBnTkNDEHNooQZaEsycsRA3cuY66jN7WAvCmAuAx6wc8WOPAOfAMzR64F3lovHe6qn7YyUI8Ionxf2ti%2B9bwJoSrhIEqd5wcjhaQy6i6TvOv4uwPO6NP4YXJv8DiTnfiA8qREYfKeUV&X-Amz-Signature=f17e48159132c9e9371a319d2c6a3144f8f43f2cf393f153aa6a2545eb15d09c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEN5O7QL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMVi1U2R%2BzavxO8z3zo0TXQacNIvxiIYVf4g2HowwmEAiBeYNzGaecHBh71ifneIwCtOvQn3O5o%2BIhaPNa%2BmQic0yqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcNHL2%2FVMjrjFczYWKtwDHpWwDNMfpTm%2FdMAlZps%2FPHba8lNj2CfqTA5ydQcpPcD8hdsmhWpWZnhp0v2C%2BSrjHcsIX1F5gxN4Ks8EhJjMCOcjI3ChNdkXnwz8GhrQkMJrqZuycvXYjTSauuJ5xbkhv0zNzIWqKSv1t5zzbYoQ6ssZXeIODSppENC6hn5GOZoZIV9EloejJBbejYxACceIdSnPS0MxvjGNLgNIqmo%2FKoKEKA3dDuUK4u2V9m8gxHSB2XEWO7qgqZLnseBBH9PEOCqB1rIeAntYEl4FvqM%2B%2FM%2BuheVxgLHbJXBYHYG2%2FY%2BiI%2FrWBl4ghi97v4ezRYj3k12mi%2FwRDh6ebMOUEKo02dqrRR4hYT%2Bf7Y69Oa6N%2FJUJq62fSC6XUMjHqeyop%2BeMYAuvX7Wwsw9%2F2hZLvyeGr%2BUEzGYpm4Ysl9xbzH9eqvKuDg6GmjcZJfiUSLwAOOEdwdPbgMUnQJuRnogJHLmm9SmSdFQZWChsFAo6qYr7oPr3P0X4T34vhaNPM5RtP8AzI%2BIOuOC5%2Bu3iUCyySgMzbwTmu9470EAiOVZRZKpJZUqbBCocQQt8IL1J1rmxTM9glrln%2FImL1MjHKQd4PIB%2BalksBpb8njQw6lxKvbWgve4keITiMc8LK%2Fx6PPMwluP%2BvAY6pgH4vvPavQRyp9ASWB7%2BVau1Sh7XkKvgPPSCTPPiCb%2F%2Byx%2FgnHxsjda4ntALSjfdo90AfItChlssj05CJ62NxNBnTkNDEHNooQZaEsycsRA3cuY66jN7WAvCmAuAx6wc8WOPAOfAMzR64F3lovHe6qn7YyUI8Ionxf2ti%2B9bwJoSrhIEqd5wcjhaQy6i6TvOv4uwPO6NP4YXJv8DiTnfiA8qREYfKeUV&X-Amz-Signature=d8bbf33d9e33b7efceb022865263520ef788752006caf4cc4ae7c91e25d73707&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y557K3Y3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDcKFgcifeou7v5Q1NcHMfa947DhEoDQa31%2BH2WFnQdwAiB%2FI3kcgHIsFQpfX8PmL4sFhow1ultVWa6OIpZ%2Bo%2B5TACqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEC0vtN3Zd%2BkeGuU5KtwDQavq3g1V9slRVvMJ3xY2mIhzl%2FTXqzrlmHHg0WnmykagLhC0MgTu5ypsvFkGVTH2A1WQz7QOi59SMv0lUW2XIIQB1pU8chhCmSPWnUePbwE%2FOppjcRoD170GiEq3uEg5hmOI2Yvskjd23VvF1vIKsRfZ%2B6GJasZ8qUr0eKJU9ehzb7Xdh56ntadIWO9GYcFMGZ%2BBTqYShmpgIFX0oJN8%2FqATinurUSVd5ylM3v53VT6Ta0RfdEN26abzn6rAwhzVyM9Gi9zU6rpgVg%2FuJRyrwpeBfUQbS5T8WyWNwNxcZDnSubZTRVpohvLmj9pyuYc7N8vBpHx5wY3tr0H97BH1NHiQiWBj3JeL3SLKjFgVDExhfiH2vtOB82lA3ZOTdi%2BUSpltP%2BQ3qDQnIOxwnweT9RhvuWKX1J%2FxlR0lDfDh0p3lZQ%2F9BwM1zfBRLUVfqxFrVrWJPRt%2FSnufmY7CH27G8E%2BJjVHxWFzCM%2F9%2FLxckgG8aty2pHYBHc%2FJZvWJiDgluQIevSYVGH3zWZe%2F7DSV1RR2eci5dV8plzLeY%2BUi5g6RfJ9vJQ9pwMtTU6bOCQHca4OYIVenEf%2FoUCeL1KIhePXfd%2B95EAtXJfGZzyHSNzE6GTl4AdJ11Ggzpd9Ywh9v%2BvAY6pgEWwRAbGlmJtC4XJHTaPVUO3SdRmvL99pddgjRHncSPVQb4V6XpDAlk7t0feynvXyIOjeMODGdWv5I2AaPPIDZoKzTq9fIcbfT4N9z%2Fu8sBxSUij2pUa%2Bou6kyJZGfcozHrffQrgzkKxrdCgopC1eUkzAwxy3m8cnO%2BNYMpjQxRf2C61Owipq0IdZ5HaCbfPmLh2EWrlfwHAbtgxUP4wj9DV1OYc4wA&X-Amz-Signature=dc7a18b7fbcc680f390f342e4a7476c9386ab64d18879ee52c9afd0da93f1f7c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y557K3Y3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDcKFgcifeou7v5Q1NcHMfa947DhEoDQa31%2BH2WFnQdwAiB%2FI3kcgHIsFQpfX8PmL4sFhow1ultVWa6OIpZ%2Bo%2B5TACqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEC0vtN3Zd%2BkeGuU5KtwDQavq3g1V9slRVvMJ3xY2mIhzl%2FTXqzrlmHHg0WnmykagLhC0MgTu5ypsvFkGVTH2A1WQz7QOi59SMv0lUW2XIIQB1pU8chhCmSPWnUePbwE%2FOppjcRoD170GiEq3uEg5hmOI2Yvskjd23VvF1vIKsRfZ%2B6GJasZ8qUr0eKJU9ehzb7Xdh56ntadIWO9GYcFMGZ%2BBTqYShmpgIFX0oJN8%2FqATinurUSVd5ylM3v53VT6Ta0RfdEN26abzn6rAwhzVyM9Gi9zU6rpgVg%2FuJRyrwpeBfUQbS5T8WyWNwNxcZDnSubZTRVpohvLmj9pyuYc7N8vBpHx5wY3tr0H97BH1NHiQiWBj3JeL3SLKjFgVDExhfiH2vtOB82lA3ZOTdi%2BUSpltP%2BQ3qDQnIOxwnweT9RhvuWKX1J%2FxlR0lDfDh0p3lZQ%2F9BwM1zfBRLUVfqxFrVrWJPRt%2FSnufmY7CH27G8E%2BJjVHxWFzCM%2F9%2FLxckgG8aty2pHYBHc%2FJZvWJiDgluQIevSYVGH3zWZe%2F7DSV1RR2eci5dV8plzLeY%2BUi5g6RfJ9vJQ9pwMtTU6bOCQHca4OYIVenEf%2FoUCeL1KIhePXfd%2B95EAtXJfGZzyHSNzE6GTl4AdJ11Ggzpd9Ywh9v%2BvAY6pgEWwRAbGlmJtC4XJHTaPVUO3SdRmvL99pddgjRHncSPVQb4V6XpDAlk7t0feynvXyIOjeMODGdWv5I2AaPPIDZoKzTq9fIcbfT4N9z%2Fu8sBxSUij2pUa%2Bou6kyJZGfcozHrffQrgzkKxrdCgopC1eUkzAwxy3m8cnO%2BNYMpjQxRf2C61Owipq0IdZ5HaCbfPmLh2EWrlfwHAbtgxUP4wj9DV1OYc4wA&X-Amz-Signature=61ca56b40d9b053763be7a928488e39bddace6aa9ef6416c05b1c797eea7d52f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEN5O7QL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBMVi1U2R%2BzavxO8z3zo0TXQacNIvxiIYVf4g2HowwmEAiBeYNzGaecHBh71ifneIwCtOvQn3O5o%2BIhaPNa%2BmQic0yqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcNHL2%2FVMjrjFczYWKtwDHpWwDNMfpTm%2FdMAlZps%2FPHba8lNj2CfqTA5ydQcpPcD8hdsmhWpWZnhp0v2C%2BSrjHcsIX1F5gxN4Ks8EhJjMCOcjI3ChNdkXnwz8GhrQkMJrqZuycvXYjTSauuJ5xbkhv0zNzIWqKSv1t5zzbYoQ6ssZXeIODSppENC6hn5GOZoZIV9EloejJBbejYxACceIdSnPS0MxvjGNLgNIqmo%2FKoKEKA3dDuUK4u2V9m8gxHSB2XEWO7qgqZLnseBBH9PEOCqB1rIeAntYEl4FvqM%2B%2FM%2BuheVxgLHbJXBYHYG2%2FY%2BiI%2FrWBl4ghi97v4ezRYj3k12mi%2FwRDh6ebMOUEKo02dqrRR4hYT%2Bf7Y69Oa6N%2FJUJq62fSC6XUMjHqeyop%2BeMYAuvX7Wwsw9%2F2hZLvyeGr%2BUEzGYpm4Ysl9xbzH9eqvKuDg6GmjcZJfiUSLwAOOEdwdPbgMUnQJuRnogJHLmm9SmSdFQZWChsFAo6qYr7oPr3P0X4T34vhaNPM5RtP8AzI%2BIOuOC5%2Bu3iUCyySgMzbwTmu9470EAiOVZRZKpJZUqbBCocQQt8IL1J1rmxTM9glrln%2FImL1MjHKQd4PIB%2BalksBpb8njQw6lxKvbWgve4keITiMc8LK%2Fx6PPMwluP%2BvAY6pgH4vvPavQRyp9ASWB7%2BVau1Sh7XkKvgPPSCTPPiCb%2F%2Byx%2FgnHxsjda4ntALSjfdo90AfItChlssj05CJ62NxNBnTkNDEHNooQZaEsycsRA3cuY66jN7WAvCmAuAx6wc8WOPAOfAMzR64F3lovHe6qn7YyUI8Ionxf2ti%2B9bwJoSrhIEqd5wcjhaQy6i6TvOv4uwPO6NP4YXJv8DiTnfiA8qREYfKeUV&X-Amz-Signature=eaa1f62c5788bb0beae73f507f6568de1cd0bf685ae54c7d9945bcfa8742dd79&X-Amz-SignedHeaders=host&x-id=GetObject)
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