

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLTILKJY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHPMZHSEHy69PoBJUBq9njFIoU3qzHVOqjope8%2FgXsryAiEArcgVVO5q3AD4bow%2F3tGjaxcNlhCo%2BU3TNCk8JFs5efcqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGXugB5aeeSCVtCvuircA2Yl1ZdZ9bD0fEwS6kvCvGLPVne%2BZB7KggZwaKnQZOqtrqOKvujHz5ljenzENm7InAriRgEIjhFi0okN2Ln7rlHbd6hRqfr6LoYhGe4W2v%2BXmOzKPaThFnzcT8P5CeaRf%2BgdPvz6roCih8LAqLIR0JYjA9Ab1MDz4Q8AGlULdkzZjRYztsQmtf7%2B4bYmYqEyIEYDeHz6Lsjo%2F%2FJ6x3BUXXrpVnnOs7A6PADVRd9NXXXb0aqHWsXWfYZ7IauZcJWtvE1gHdC7gi6Yy8BpytzDERQQ5iNe4A77rcYgBUZnztpOd1qdURx7UZrzhj3I%2FTLuUFsYjl08l4O%2FVSS9Kl8B2SeRHm7EUkFz7J7eE6%2F3Fn%2BaeBzImLWSmte7I4n2QuM9ei3DjoYKlM7NL2LCSSQKw6mVOwj%2Bq2Mt%2FTaMDKmKiZ27%2FxHQg1pHXU%2FAmhgH%2F5AWS%2F0N9w6%2BNC%2FpS4rykA32WW9k7mdb39aO%2FafptpSHpXCXR%2FjSLAD7S8Kw3dBF%2F7YwbPD1t%2FWvKMuiwzAv%2FnfwnO3U4Br3b%2FR9nekANbsMf0b6vPJXmEk2f4QOdHXnKvAnFIbXWeZ5lDrDQp6niDZIhlx7MbpTiJ4%2F%2F4U12ALSBi7cfUpKV4YVimw8lfrDMJyu57wGOqUBzGE2DA8VDRtCv49o8NwKGRO6JfNDhio419ccRoiQ9qLs0LEvFVqRUmxDadHb%2FX8NS1t%2BU2mF7ZpCfjjeqkV%2FLyNIx%2BZd9fL04hPLuYaJ%2Bt2D0%2BZyGPVARQ%2FW2Puaps207RddJNktpebfu33tQfu%2FHg0YOkkEEDYwNSwGFnwpQXnd48Sq7QZlNZ%2FXEAXq1IVMN0vOjJx48WsWHJuhJXNEdu0SXpIa&X-Amz-Signature=fb545a6042d7f217c6442d448fc944f8c996b6454d91d7ac79fca42883dbc079&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLTILKJY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHPMZHSEHy69PoBJUBq9njFIoU3qzHVOqjope8%2FgXsryAiEArcgVVO5q3AD4bow%2F3tGjaxcNlhCo%2BU3TNCk8JFs5efcqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGXugB5aeeSCVtCvuircA2Yl1ZdZ9bD0fEwS6kvCvGLPVne%2BZB7KggZwaKnQZOqtrqOKvujHz5ljenzENm7InAriRgEIjhFi0okN2Ln7rlHbd6hRqfr6LoYhGe4W2v%2BXmOzKPaThFnzcT8P5CeaRf%2BgdPvz6roCih8LAqLIR0JYjA9Ab1MDz4Q8AGlULdkzZjRYztsQmtf7%2B4bYmYqEyIEYDeHz6Lsjo%2F%2FJ6x3BUXXrpVnnOs7A6PADVRd9NXXXb0aqHWsXWfYZ7IauZcJWtvE1gHdC7gi6Yy8BpytzDERQQ5iNe4A77rcYgBUZnztpOd1qdURx7UZrzhj3I%2FTLuUFsYjl08l4O%2FVSS9Kl8B2SeRHm7EUkFz7J7eE6%2F3Fn%2BaeBzImLWSmte7I4n2QuM9ei3DjoYKlM7NL2LCSSQKw6mVOwj%2Bq2Mt%2FTaMDKmKiZ27%2FxHQg1pHXU%2FAmhgH%2F5AWS%2F0N9w6%2BNC%2FpS4rykA32WW9k7mdb39aO%2FafptpSHpXCXR%2FjSLAD7S8Kw3dBF%2F7YwbPD1t%2FWvKMuiwzAv%2FnfwnO3U4Br3b%2FR9nekANbsMf0b6vPJXmEk2f4QOdHXnKvAnFIbXWeZ5lDrDQp6niDZIhlx7MbpTiJ4%2F%2F4U12ALSBi7cfUpKV4YVimw8lfrDMJyu57wGOqUBzGE2DA8VDRtCv49o8NwKGRO6JfNDhio419ccRoiQ9qLs0LEvFVqRUmxDadHb%2FX8NS1t%2BU2mF7ZpCfjjeqkV%2FLyNIx%2BZd9fL04hPLuYaJ%2Bt2D0%2BZyGPVARQ%2FW2Puaps207RddJNktpebfu33tQfu%2FHg0YOkkEEDYwNSwGFnwpQXnd48Sq7QZlNZ%2FXEAXq1IVMN0vOjJx48WsWHJuhJXNEdu0SXpIa&X-Amz-Signature=962f4d12002ee827b4f88d066b23b99197112d0532c2be0cd2eb5a9b3c786e67&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLTILKJY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHPMZHSEHy69PoBJUBq9njFIoU3qzHVOqjope8%2FgXsryAiEArcgVVO5q3AD4bow%2F3tGjaxcNlhCo%2BU3TNCk8JFs5efcqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGXugB5aeeSCVtCvuircA2Yl1ZdZ9bD0fEwS6kvCvGLPVne%2BZB7KggZwaKnQZOqtrqOKvujHz5ljenzENm7InAriRgEIjhFi0okN2Ln7rlHbd6hRqfr6LoYhGe4W2v%2BXmOzKPaThFnzcT8P5CeaRf%2BgdPvz6roCih8LAqLIR0JYjA9Ab1MDz4Q8AGlULdkzZjRYztsQmtf7%2B4bYmYqEyIEYDeHz6Lsjo%2F%2FJ6x3BUXXrpVnnOs7A6PADVRd9NXXXb0aqHWsXWfYZ7IauZcJWtvE1gHdC7gi6Yy8BpytzDERQQ5iNe4A77rcYgBUZnztpOd1qdURx7UZrzhj3I%2FTLuUFsYjl08l4O%2FVSS9Kl8B2SeRHm7EUkFz7J7eE6%2F3Fn%2BaeBzImLWSmte7I4n2QuM9ei3DjoYKlM7NL2LCSSQKw6mVOwj%2Bq2Mt%2FTaMDKmKiZ27%2FxHQg1pHXU%2FAmhgH%2F5AWS%2F0N9w6%2BNC%2FpS4rykA32WW9k7mdb39aO%2FafptpSHpXCXR%2FjSLAD7S8Kw3dBF%2F7YwbPD1t%2FWvKMuiwzAv%2FnfwnO3U4Br3b%2FR9nekANbsMf0b6vPJXmEk2f4QOdHXnKvAnFIbXWeZ5lDrDQp6niDZIhlx7MbpTiJ4%2F%2F4U12ALSBi7cfUpKV4YVimw8lfrDMJyu57wGOqUBzGE2DA8VDRtCv49o8NwKGRO6JfNDhio419ccRoiQ9qLs0LEvFVqRUmxDadHb%2FX8NS1t%2BU2mF7ZpCfjjeqkV%2FLyNIx%2BZd9fL04hPLuYaJ%2Bt2D0%2BZyGPVARQ%2FW2Puaps207RddJNktpebfu33tQfu%2FHg0YOkkEEDYwNSwGFnwpQXnd48Sq7QZlNZ%2FXEAXq1IVMN0vOjJx48WsWHJuhJXNEdu0SXpIa&X-Amz-Signature=8db1cfbf7965b4e42460d2e09f8f5c64a65adc9dde968be9030759c10a339e66&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEAHEYY3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHe%2B8yTHaweTOBW%2Bauz1Fbony7FHw3OCnkQ63DF5zzriAiBg8dYAoVbBms9Sj6H%2BMPCGpdiLs3i5dEJ8tH1uH7CNMyqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhbd%2Fs8PQo%2BxX6Ow9KtwD7YMKILZrTH76U2beAvoeWsA4LT5gxGR0%2Big41BNk6n7WTf2imMgraGq3pLpxEx8OwUA%2Bzpu1X1KJvGep8LJt9tj5Ert7WF8tZk1nbN30aBboprTVcP3nFubvqV3ZdW%2BVcoB8BPkJAbhZcPSFwSgK0%2Fb9YIoGxUb%2Fjw1fNdQv5%2BrUcOG2NwT8gor7aPtgj0s8HzpJXF7R0VquHEAQo7JLOvJ19jMZTP%2F%2BvLERVTp9Y9HEon8KBFQANhXrHD2JGYevbNYsRTcpsz37nhEIo2rwwCnk7ofRdQk%2BBs1lz%2FdfCKsxxeQnBFAnNIXMQCuC%2BlgKXWb6syAD2Pwa75W3UC5%2FVWk%2BxN1EqAa7IBClaGMTrY0m0PnOdFMPH3LFOGcC8x6w1YrOdudHnjhpzyUz0h4N0rdzZnKBNZqmJ38KVOyQaVz0VjuX77Z3VMym6vzLDj1aI6SDrC1a%2Fo28ERPPdQ4ZfHGrE3mVamGr%2Fm9AaAp%2Fh9B4oOEkrOcRuY3z5gTqyr5JMn4XF5S%2BzbtGfN7GnMo7BZ1M9hTguAGigRQj0iDIc7SHSn%2FmG0g%2B0ldFNqbBi7iuOvMiixkLuc2xiLbfl1hZATDmx1s97FiTUnSNstsfVdc%2BxaaYW7qKM3p1NjEw0qznvAY6pgGSGxuCYAfuDabayLqCSjUeQu9BMc%2FrqraXwu1gO8p5sowyIYBQzSv6EIdxGO%2BbvV%2F2c008KcMOY2qgIKhvQKFq6KUhIhlxDtCOAxMHuO%2BUUCYu%2B4YPq5weZ2FQXds1iTPD0KEJQTTgbaPQPi8m%2Bu%2B%2BxGbzgqbmxBk37hWp1FywPfsqCZWeHorxF0vDqHha6u7D2sg%2FyNf%2Fskfq%2BpwZC0T05Ylihrw%2F&X-Amz-Signature=398bb32ead25b4df714e723aae1251444fbfe5ab939c935dd74a6fcd832fa8f7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEAHEYY3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHe%2B8yTHaweTOBW%2Bauz1Fbony7FHw3OCnkQ63DF5zzriAiBg8dYAoVbBms9Sj6H%2BMPCGpdiLs3i5dEJ8tH1uH7CNMyqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhbd%2Fs8PQo%2BxX6Ow9KtwD7YMKILZrTH76U2beAvoeWsA4LT5gxGR0%2Big41BNk6n7WTf2imMgraGq3pLpxEx8OwUA%2Bzpu1X1KJvGep8LJt9tj5Ert7WF8tZk1nbN30aBboprTVcP3nFubvqV3ZdW%2BVcoB8BPkJAbhZcPSFwSgK0%2Fb9YIoGxUb%2Fjw1fNdQv5%2BrUcOG2NwT8gor7aPtgj0s8HzpJXF7R0VquHEAQo7JLOvJ19jMZTP%2F%2BvLERVTp9Y9HEon8KBFQANhXrHD2JGYevbNYsRTcpsz37nhEIo2rwwCnk7ofRdQk%2BBs1lz%2FdfCKsxxeQnBFAnNIXMQCuC%2BlgKXWb6syAD2Pwa75W3UC5%2FVWk%2BxN1EqAa7IBClaGMTrY0m0PnOdFMPH3LFOGcC8x6w1YrOdudHnjhpzyUz0h4N0rdzZnKBNZqmJ38KVOyQaVz0VjuX77Z3VMym6vzLDj1aI6SDrC1a%2Fo28ERPPdQ4ZfHGrE3mVamGr%2Fm9AaAp%2Fh9B4oOEkrOcRuY3z5gTqyr5JMn4XF5S%2BzbtGfN7GnMo7BZ1M9hTguAGigRQj0iDIc7SHSn%2FmG0g%2B0ldFNqbBi7iuOvMiixkLuc2xiLbfl1hZATDmx1s97FiTUnSNstsfVdc%2BxaaYW7qKM3p1NjEw0qznvAY6pgGSGxuCYAfuDabayLqCSjUeQu9BMc%2FrqraXwu1gO8p5sowyIYBQzSv6EIdxGO%2BbvV%2F2c008KcMOY2qgIKhvQKFq6KUhIhlxDtCOAxMHuO%2BUUCYu%2B4YPq5weZ2FQXds1iTPD0KEJQTTgbaPQPi8m%2Bu%2B%2BxGbzgqbmxBk37hWp1FywPfsqCZWeHorxF0vDqHha6u7D2sg%2FyNf%2Fskfq%2BpwZC0T05Ylihrw%2F&X-Amz-Signature=fa95ad8ad8b46edb0dd4e33920975baa8ba027e892504c3f00ae096aee9f4499&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLTILKJY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHPMZHSEHy69PoBJUBq9njFIoU3qzHVOqjope8%2FgXsryAiEArcgVVO5q3AD4bow%2F3tGjaxcNlhCo%2BU3TNCk8JFs5efcqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGXugB5aeeSCVtCvuircA2Yl1ZdZ9bD0fEwS6kvCvGLPVne%2BZB7KggZwaKnQZOqtrqOKvujHz5ljenzENm7InAriRgEIjhFi0okN2Ln7rlHbd6hRqfr6LoYhGe4W2v%2BXmOzKPaThFnzcT8P5CeaRf%2BgdPvz6roCih8LAqLIR0JYjA9Ab1MDz4Q8AGlULdkzZjRYztsQmtf7%2B4bYmYqEyIEYDeHz6Lsjo%2F%2FJ6x3BUXXrpVnnOs7A6PADVRd9NXXXb0aqHWsXWfYZ7IauZcJWtvE1gHdC7gi6Yy8BpytzDERQQ5iNe4A77rcYgBUZnztpOd1qdURx7UZrzhj3I%2FTLuUFsYjl08l4O%2FVSS9Kl8B2SeRHm7EUkFz7J7eE6%2F3Fn%2BaeBzImLWSmte7I4n2QuM9ei3DjoYKlM7NL2LCSSQKw6mVOwj%2Bq2Mt%2FTaMDKmKiZ27%2FxHQg1pHXU%2FAmhgH%2F5AWS%2F0N9w6%2BNC%2FpS4rykA32WW9k7mdb39aO%2FafptpSHpXCXR%2FjSLAD7S8Kw3dBF%2F7YwbPD1t%2FWvKMuiwzAv%2FnfwnO3U4Br3b%2FR9nekANbsMf0b6vPJXmEk2f4QOdHXnKvAnFIbXWeZ5lDrDQp6niDZIhlx7MbpTiJ4%2F%2F4U12ALSBi7cfUpKV4YVimw8lfrDMJyu57wGOqUBzGE2DA8VDRtCv49o8NwKGRO6JfNDhio419ccRoiQ9qLs0LEvFVqRUmxDadHb%2FX8NS1t%2BU2mF7ZpCfjjeqkV%2FLyNIx%2BZd9fL04hPLuYaJ%2Bt2D0%2BZyGPVARQ%2FW2Puaps207RddJNktpebfu33tQfu%2FHg0YOkkEEDYwNSwGFnwpQXnd48Sq7QZlNZ%2FXEAXq1IVMN0vOjJx48WsWHJuhJXNEdu0SXpIa&X-Amz-Signature=98b6770798d049edeeb3823f894a8e6a266d2de87d26f8e4419c097918ce7c56&X-Amz-SignedHeaders=host&x-id=GetObject)
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