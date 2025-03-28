

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3UJPNTX%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCIH3gmhauledkMHgthZhCUAw5pch0%2Fwjl%2FHfzGmdsrNb9AiAYAp34XUoxSpNfOZBvg5d7tdk2LEG8m%2BByk2kM9X%2B0sCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPg7Czik9y%2Bahw0HdKtwD%2FNzsuxYeGztSE%2B1NAOa7vHnlOWeHUtIkyXlhyHcdNS3uoI%2FqFXHofMnK6jqxSYeSobBdNEd9F0rAfEt41M25sDoGkDTb7VNQrSmk1aZwahCfJUwAsdk95IXBNEfMkEqrpY8KnGgAymppi%2Bc5oeQDdpkCX%2FTAhTMJKVZoTwzZRLqJ%2BZc5Pm3ziHTRWlbJ8LnzmPAQzIxGXasZGWDEtqYRFiT3L%2FGMmaF8tIkSYnU4718CN%2FfUL6FA6RGXJi15L0v%2BMq%2F4Rt5Bw6TWfU99pSjyU1ZPQjp3Gxa6ajd7dd3wiHBLwnJttFsh7M4M8%2FknGkSEmgF1iDraUoxvX6EFaeBW9aXy16u4ZJI%2BfJ5i2QEvvEQTje0tOuGRjo5JyBVqmTomyUCJIjETgDgBv7cstXR8xe5yjuntQfZ2Wl84UvO8LXSxFK2%2Bw8ahUvV3ExV55hL1WdJPgTMVs5SkaYuvURfbTVqSRQSvKfn23vfHj86UiXGheD3OO62AgeTyUoLdngEfVfO3mXYK%2BUtWBqGhgGnx5opNrt%2Bn4onulFZ0txuoDp5Eu1SYU7sl9qN84EBRnwSAJ0iRQTYWGX5nfqrSkd6bT5Eux3WlrCxLchszQleaXFj0%2Fb1eVLDMEzZfmTkwnbb8vgY6pgGagCkqOzYUurE0h2y51Es%2FFAhvHN%2F0bpVqv2rjNUW9l3CiA59EDVdSCh163OrZynySWQgTeH6BWC0xSjwSRw34g%2FOiNqyl%2BjuQhGAE8iJu%2BzhtvMMFw%2Frzhgf%2BpxPxygQf4G%2FAr0Prepetwhfa6xHvhNDVSVydXJX%2BekUsRoae2vAQhkspECD4tCaI7odY5sdjHrO6CwUllhesaClE0Y%2FAUCXPsgRM&X-Amz-Signature=1c20fcaab18528d539c4f2899b0794ff5edf827e23b3bce267d662110a9410b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3UJPNTX%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCIH3gmhauledkMHgthZhCUAw5pch0%2Fwjl%2FHfzGmdsrNb9AiAYAp34XUoxSpNfOZBvg5d7tdk2LEG8m%2BByk2kM9X%2B0sCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPg7Czik9y%2Bahw0HdKtwD%2FNzsuxYeGztSE%2B1NAOa7vHnlOWeHUtIkyXlhyHcdNS3uoI%2FqFXHofMnK6jqxSYeSobBdNEd9F0rAfEt41M25sDoGkDTb7VNQrSmk1aZwahCfJUwAsdk95IXBNEfMkEqrpY8KnGgAymppi%2Bc5oeQDdpkCX%2FTAhTMJKVZoTwzZRLqJ%2BZc5Pm3ziHTRWlbJ8LnzmPAQzIxGXasZGWDEtqYRFiT3L%2FGMmaF8tIkSYnU4718CN%2FfUL6FA6RGXJi15L0v%2BMq%2F4Rt5Bw6TWfU99pSjyU1ZPQjp3Gxa6ajd7dd3wiHBLwnJttFsh7M4M8%2FknGkSEmgF1iDraUoxvX6EFaeBW9aXy16u4ZJI%2BfJ5i2QEvvEQTje0tOuGRjo5JyBVqmTomyUCJIjETgDgBv7cstXR8xe5yjuntQfZ2Wl84UvO8LXSxFK2%2Bw8ahUvV3ExV55hL1WdJPgTMVs5SkaYuvURfbTVqSRQSvKfn23vfHj86UiXGheD3OO62AgeTyUoLdngEfVfO3mXYK%2BUtWBqGhgGnx5opNrt%2Bn4onulFZ0txuoDp5Eu1SYU7sl9qN84EBRnwSAJ0iRQTYWGX5nfqrSkd6bT5Eux3WlrCxLchszQleaXFj0%2Fb1eVLDMEzZfmTkwnbb8vgY6pgGagCkqOzYUurE0h2y51Es%2FFAhvHN%2F0bpVqv2rjNUW9l3CiA59EDVdSCh163OrZynySWQgTeH6BWC0xSjwSRw34g%2FOiNqyl%2BjuQhGAE8iJu%2BzhtvMMFw%2Frzhgf%2BpxPxygQf4G%2FAr0Prepetwhfa6xHvhNDVSVydXJX%2BekUsRoae2vAQhkspECD4tCaI7odY5sdjHrO6CwUllhesaClE0Y%2FAUCXPsgRM&X-Amz-Signature=8d91b71dae6ae1c47c19d2f6c239aef49e0c01b7639ae205796da32b34bf0866&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3UJPNTX%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCIH3gmhauledkMHgthZhCUAw5pch0%2Fwjl%2FHfzGmdsrNb9AiAYAp34XUoxSpNfOZBvg5d7tdk2LEG8m%2BByk2kM9X%2B0sCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPg7Czik9y%2Bahw0HdKtwD%2FNzsuxYeGztSE%2B1NAOa7vHnlOWeHUtIkyXlhyHcdNS3uoI%2FqFXHofMnK6jqxSYeSobBdNEd9F0rAfEt41M25sDoGkDTb7VNQrSmk1aZwahCfJUwAsdk95IXBNEfMkEqrpY8KnGgAymppi%2Bc5oeQDdpkCX%2FTAhTMJKVZoTwzZRLqJ%2BZc5Pm3ziHTRWlbJ8LnzmPAQzIxGXasZGWDEtqYRFiT3L%2FGMmaF8tIkSYnU4718CN%2FfUL6FA6RGXJi15L0v%2BMq%2F4Rt5Bw6TWfU99pSjyU1ZPQjp3Gxa6ajd7dd3wiHBLwnJttFsh7M4M8%2FknGkSEmgF1iDraUoxvX6EFaeBW9aXy16u4ZJI%2BfJ5i2QEvvEQTje0tOuGRjo5JyBVqmTomyUCJIjETgDgBv7cstXR8xe5yjuntQfZ2Wl84UvO8LXSxFK2%2Bw8ahUvV3ExV55hL1WdJPgTMVs5SkaYuvURfbTVqSRQSvKfn23vfHj86UiXGheD3OO62AgeTyUoLdngEfVfO3mXYK%2BUtWBqGhgGnx5opNrt%2Bn4onulFZ0txuoDp5Eu1SYU7sl9qN84EBRnwSAJ0iRQTYWGX5nfqrSkd6bT5Eux3WlrCxLchszQleaXFj0%2Fb1eVLDMEzZfmTkwnbb8vgY6pgGagCkqOzYUurE0h2y51Es%2FFAhvHN%2F0bpVqv2rjNUW9l3CiA59EDVdSCh163OrZynySWQgTeH6BWC0xSjwSRw34g%2FOiNqyl%2BjuQhGAE8iJu%2BzhtvMMFw%2Frzhgf%2BpxPxygQf4G%2FAr0Prepetwhfa6xHvhNDVSVydXJX%2BekUsRoae2vAQhkspECD4tCaI7odY5sdjHrO6CwUllhesaClE0Y%2FAUCXPsgRM&X-Amz-Signature=99915756033d59fdb327b53268db9bceb670bcf72bca8a80f6cf933ee4e01460&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHJJIMO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIF2qpvrMv43%2BFB605ForBQP7Si%2Fj%2B2yfDgQoknyF7FB2AiBPDpmAO9meYa1LEbkriKmnK2%2B84OgZKza8lyOzAYaliiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjKXIfcMxHHvYmYtiKtwDg6BEPqzUxsbnear5KL2UtGRMKGnn1cI%2BkMfdSG9huRnQquI6oulwQ1v5FT0iLpitao7Nk9Yo66UiNBsOw6taPJLrH%2Fv8xcu6Rpz%2F%2BqplsB3wji0ynvGXESTrXtPh3v0djr5cz6%2BXyo6bA4UQ5VpevvaclgK4K5VskJlxivTf8OlSWRLzD7XT0W8ojXAA1CIu1zCJanwG3guf%2BbWyGG5zdrsmtAobr6odZMMbTbiDbQOz03OEYIrA1V5biXKQ%2FJETjUXvXVW6v4Fj8bsBdNKBt85zeBioxzaBl30l66PzyNboSsHsulxtLrl9LiczIh48XOrhRkJKM%2BltGTE6SXsHDWa0s8ZYEPANn6PM7OoeTuU2J8i8T4GaO3%2B%2F6t0ZAEPnV%2FF%2BsAf2PaxdGz7q5UlB%2F2qZNPV8NkXIILjDg3qE%2FIRhvWy1nWD9cVVzm9UdHeSmrH%2BSIEDnsJ7BBntflBMCRG4AcjvAHOa8cdlro3cqmJqmBuOZlqNHOr%2B2mwOcSgjrzmHsY%2Fw0LqxWmQtl6h5%2FrHge8kwV19PzSu5WB03bi4W4xdMo6Dwm7UafnaTVEsnXewVv5t5gP63NHeQOnzkZZDPpCGm%2B3y%2F050nNRC3sH7jo8ojLf%2FcRxU15KBAwjrX8vgY6pgGVu7%2B9rDhq4owp8Xmu3FC5NajzdN%2BDPAfLyO%2F3jS2JX6UKOvg7IhVomwgf1vU%2B1e1gJY7fDDBMi3tEaPSz9UB7OXFR5EER8%2BXTLnPE3otqtxvHdkk4BQJdBElxCGjHjD9mhyc2I4Be2d89qiDV0kDqg%2FVRgkFwwXmNMosudS5%2BniLaeQix9QZDpjgSSiMh9JcKJLZjNFpFEdsrifqznTslHuVhSwag&X-Amz-Signature=ea154a91bc4050c0b328d575fa36db2094c52c7cb87649e20b9fca23ed0c2d8a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BHJJIMO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIF2qpvrMv43%2BFB605ForBQP7Si%2Fj%2B2yfDgQoknyF7FB2AiBPDpmAO9meYa1LEbkriKmnK2%2B84OgZKza8lyOzAYaliiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjKXIfcMxHHvYmYtiKtwDg6BEPqzUxsbnear5KL2UtGRMKGnn1cI%2BkMfdSG9huRnQquI6oulwQ1v5FT0iLpitao7Nk9Yo66UiNBsOw6taPJLrH%2Fv8xcu6Rpz%2F%2BqplsB3wji0ynvGXESTrXtPh3v0djr5cz6%2BXyo6bA4UQ5VpevvaclgK4K5VskJlxivTf8OlSWRLzD7XT0W8ojXAA1CIu1zCJanwG3guf%2BbWyGG5zdrsmtAobr6odZMMbTbiDbQOz03OEYIrA1V5biXKQ%2FJETjUXvXVW6v4Fj8bsBdNKBt85zeBioxzaBl30l66PzyNboSsHsulxtLrl9LiczIh48XOrhRkJKM%2BltGTE6SXsHDWa0s8ZYEPANn6PM7OoeTuU2J8i8T4GaO3%2B%2F6t0ZAEPnV%2FF%2BsAf2PaxdGz7q5UlB%2F2qZNPV8NkXIILjDg3qE%2FIRhvWy1nWD9cVVzm9UdHeSmrH%2BSIEDnsJ7BBntflBMCRG4AcjvAHOa8cdlro3cqmJqmBuOZlqNHOr%2B2mwOcSgjrzmHsY%2Fw0LqxWmQtl6h5%2FrHge8kwV19PzSu5WB03bi4W4xdMo6Dwm7UafnaTVEsnXewVv5t5gP63NHeQOnzkZZDPpCGm%2B3y%2F050nNRC3sH7jo8ojLf%2FcRxU15KBAwjrX8vgY6pgGVu7%2B9rDhq4owp8Xmu3FC5NajzdN%2BDPAfLyO%2F3jS2JX6UKOvg7IhVomwgf1vU%2B1e1gJY7fDDBMi3tEaPSz9UB7OXFR5EER8%2BXTLnPE3otqtxvHdkk4BQJdBElxCGjHjD9mhyc2I4Be2d89qiDV0kDqg%2FVRgkFwwXmNMosudS5%2BniLaeQix9QZDpjgSSiMh9JcKJLZjNFpFEdsrifqznTslHuVhSwag&X-Amz-Signature=38c879dd7382341f3ad1196454e32f72140f9a3cf459f383f3f34818d2b8dd4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3UJPNTX%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJGMEQCIH3gmhauledkMHgthZhCUAw5pch0%2Fwjl%2FHfzGmdsrNb9AiAYAp34XUoxSpNfOZBvg5d7tdk2LEG8m%2BByk2kM9X%2B0sCqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPg7Czik9y%2Bahw0HdKtwD%2FNzsuxYeGztSE%2B1NAOa7vHnlOWeHUtIkyXlhyHcdNS3uoI%2FqFXHofMnK6jqxSYeSobBdNEd9F0rAfEt41M25sDoGkDTb7VNQrSmk1aZwahCfJUwAsdk95IXBNEfMkEqrpY8KnGgAymppi%2Bc5oeQDdpkCX%2FTAhTMJKVZoTwzZRLqJ%2BZc5Pm3ziHTRWlbJ8LnzmPAQzIxGXasZGWDEtqYRFiT3L%2FGMmaF8tIkSYnU4718CN%2FfUL6FA6RGXJi15L0v%2BMq%2F4Rt5Bw6TWfU99pSjyU1ZPQjp3Gxa6ajd7dd3wiHBLwnJttFsh7M4M8%2FknGkSEmgF1iDraUoxvX6EFaeBW9aXy16u4ZJI%2BfJ5i2QEvvEQTje0tOuGRjo5JyBVqmTomyUCJIjETgDgBv7cstXR8xe5yjuntQfZ2Wl84UvO8LXSxFK2%2Bw8ahUvV3ExV55hL1WdJPgTMVs5SkaYuvURfbTVqSRQSvKfn23vfHj86UiXGheD3OO62AgeTyUoLdngEfVfO3mXYK%2BUtWBqGhgGnx5opNrt%2Bn4onulFZ0txuoDp5Eu1SYU7sl9qN84EBRnwSAJ0iRQTYWGX5nfqrSkd6bT5Eux3WlrCxLchszQleaXFj0%2Fb1eVLDMEzZfmTkwnbb8vgY6pgGagCkqOzYUurE0h2y51Es%2FFAhvHN%2F0bpVqv2rjNUW9l3CiA59EDVdSCh163OrZynySWQgTeH6BWC0xSjwSRw34g%2FOiNqyl%2BjuQhGAE8iJu%2BzhtvMMFw%2Frzhgf%2BpxPxygQf4G%2FAr0Prepetwhfa6xHvhNDVSVydXJX%2BekUsRoae2vAQhkspECD4tCaI7odY5sdjHrO6CwUllhesaClE0Y%2FAUCXPsgRM&X-Amz-Signature=50f570df24847779c82e286e17eedb4ab179750e2dfd624042e76194bf0ec4d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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