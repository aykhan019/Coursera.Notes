

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTAVU7WI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDhTeW8CfshdUtRCmMFECVhC8Mf3x1ZVWkMuQK6UrKEFgIgTMr9yEanbq6xWnyfrKkCUuQNPmw8VYchd0iIVl0n1ygq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHSNXlq29fLQ452uSircAy1%2BX4XrD5T%2FXa5%2Br%2F8OlwzQrjgP2j7l692qB34UZtXEhXysDTe7NWYxBFsq2dFOzSLaNv5eozYChyQyzumFLf8JIIhv0eJ78OyyNTYx1iOnplTFcKX6695alUlT1hJVVUvbmaeUNB9A%2Bvpdw1djud499QcS0ZmfQ3hzB2CvQEpgJHEr6Vqomg4qCseEotM7pjHFGBIIaEsAGxbA9cor%2F%2BfSU9IBA9wmgfREq45gXyhVoDJWjW2pjJWFo42rWLeDCt2ymKIhWaGe4KA7IzdckGXIBmg2UOvlWIP3Pqm7Kf2GMMcQfWAqzYPx8S4ZOE%2BG48pW%2B2jUZhk3Spbjr8oPhCKKbO6lsmW%2B4xEu%2FQyTNSVZUtVRKz7bKdRjJgSsT8GnF90njdzfnwoLiROfNcugR4Hdg1oHWMUUZtRA%2Bsl0i9ZiuECdO0%2BhCs432swJGBkg%2Bt75WzRElFfmeB1W6KeTaUvhhy0TUylTo%2BtknSYsQ3lH4vCphJznTCONPlsB1I1XiqidGSV8yKX2U0YjAy4yTsb6N4l1acnKpw6V5bxne7zTZE38Ib%2FXq291118egaomUspnmmGR1DRZDP2IMk413ZQCuYMwcUWHJ1HKNHY%2F6UV8OrY8eKSMtrPcfybGMO6%2Bhr0GOqUBgKeu4zgVL%2FlJqQVHMP1r1MjnCgbEv6vxmgZEr0D%2FfTMpyy8qiR1Qi5RWGa9S2AWAGSAHxfcEn5VIBKK3E5iCimkWj%2BmQXGjTP2B2RUK6ZynHGwVNdH3c%2FLtTFxPpCEHFtadvQGP44icLt9HbkXeYV3PVtgK2oqTmr8G2UNCd0r6DwTRfdYavnwDt%2BW0Mgghqkp2ygNyGTM9RfxdOaRyljb%2FBAQE%2B&X-Amz-Signature=fd437bfa6d74507b098e354a883bdac611663b280462e11b46296345807d4197&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTAVU7WI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDhTeW8CfshdUtRCmMFECVhC8Mf3x1ZVWkMuQK6UrKEFgIgTMr9yEanbq6xWnyfrKkCUuQNPmw8VYchd0iIVl0n1ygq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHSNXlq29fLQ452uSircAy1%2BX4XrD5T%2FXa5%2Br%2F8OlwzQrjgP2j7l692qB34UZtXEhXysDTe7NWYxBFsq2dFOzSLaNv5eozYChyQyzumFLf8JIIhv0eJ78OyyNTYx1iOnplTFcKX6695alUlT1hJVVUvbmaeUNB9A%2Bvpdw1djud499QcS0ZmfQ3hzB2CvQEpgJHEr6Vqomg4qCseEotM7pjHFGBIIaEsAGxbA9cor%2F%2BfSU9IBA9wmgfREq45gXyhVoDJWjW2pjJWFo42rWLeDCt2ymKIhWaGe4KA7IzdckGXIBmg2UOvlWIP3Pqm7Kf2GMMcQfWAqzYPx8S4ZOE%2BG48pW%2B2jUZhk3Spbjr8oPhCKKbO6lsmW%2B4xEu%2FQyTNSVZUtVRKz7bKdRjJgSsT8GnF90njdzfnwoLiROfNcugR4Hdg1oHWMUUZtRA%2Bsl0i9ZiuECdO0%2BhCs432swJGBkg%2Bt75WzRElFfmeB1W6KeTaUvhhy0TUylTo%2BtknSYsQ3lH4vCphJznTCONPlsB1I1XiqidGSV8yKX2U0YjAy4yTsb6N4l1acnKpw6V5bxne7zTZE38Ib%2FXq291118egaomUspnmmGR1DRZDP2IMk413ZQCuYMwcUWHJ1HKNHY%2F6UV8OrY8eKSMtrPcfybGMO6%2Bhr0GOqUBgKeu4zgVL%2FlJqQVHMP1r1MjnCgbEv6vxmgZEr0D%2FfTMpyy8qiR1Qi5RWGa9S2AWAGSAHxfcEn5VIBKK3E5iCimkWj%2BmQXGjTP2B2RUK6ZynHGwVNdH3c%2FLtTFxPpCEHFtadvQGP44icLt9HbkXeYV3PVtgK2oqTmr8G2UNCd0r6DwTRfdYavnwDt%2BW0Mgghqkp2ygNyGTM9RfxdOaRyljb%2FBAQE%2B&X-Amz-Signature=db2d484ab5b501f3f6e5e0da7fc8bda77b3d2392ffdceed0cbfdfd2894d5c3fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTAVU7WI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDhTeW8CfshdUtRCmMFECVhC8Mf3x1ZVWkMuQK6UrKEFgIgTMr9yEanbq6xWnyfrKkCUuQNPmw8VYchd0iIVl0n1ygq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHSNXlq29fLQ452uSircAy1%2BX4XrD5T%2FXa5%2Br%2F8OlwzQrjgP2j7l692qB34UZtXEhXysDTe7NWYxBFsq2dFOzSLaNv5eozYChyQyzumFLf8JIIhv0eJ78OyyNTYx1iOnplTFcKX6695alUlT1hJVVUvbmaeUNB9A%2Bvpdw1djud499QcS0ZmfQ3hzB2CvQEpgJHEr6Vqomg4qCseEotM7pjHFGBIIaEsAGxbA9cor%2F%2BfSU9IBA9wmgfREq45gXyhVoDJWjW2pjJWFo42rWLeDCt2ymKIhWaGe4KA7IzdckGXIBmg2UOvlWIP3Pqm7Kf2GMMcQfWAqzYPx8S4ZOE%2BG48pW%2B2jUZhk3Spbjr8oPhCKKbO6lsmW%2B4xEu%2FQyTNSVZUtVRKz7bKdRjJgSsT8GnF90njdzfnwoLiROfNcugR4Hdg1oHWMUUZtRA%2Bsl0i9ZiuECdO0%2BhCs432swJGBkg%2Bt75WzRElFfmeB1W6KeTaUvhhy0TUylTo%2BtknSYsQ3lH4vCphJznTCONPlsB1I1XiqidGSV8yKX2U0YjAy4yTsb6N4l1acnKpw6V5bxne7zTZE38Ib%2FXq291118egaomUspnmmGR1DRZDP2IMk413ZQCuYMwcUWHJ1HKNHY%2F6UV8OrY8eKSMtrPcfybGMO6%2Bhr0GOqUBgKeu4zgVL%2FlJqQVHMP1r1MjnCgbEv6vxmgZEr0D%2FfTMpyy8qiR1Qi5RWGa9S2AWAGSAHxfcEn5VIBKK3E5iCimkWj%2BmQXGjTP2B2RUK6ZynHGwVNdH3c%2FLtTFxPpCEHFtadvQGP44icLt9HbkXeYV3PVtgK2oqTmr8G2UNCd0r6DwTRfdYavnwDt%2BW0Mgghqkp2ygNyGTM9RfxdOaRyljb%2FBAQE%2B&X-Amz-Signature=506c8163bed9b72e10d73212f53b66c220dbcf3f5f9ac3f64f6ffb5a69ea7df8&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666OWY745%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCaB7Z0%2BHLfbTNTyOGxKWOxaveIMyiVyGXI26HSnK0qXwIhAM5z20FQGghFWNGd1izRcdPe6t2RLhWRbUV9NAhKzYTQKv8DCCYQABoMNjM3NDIzMTgzODA1IgxhRa800sE66rklnlUq3AONHTrJyfDR4DTG2bnFEQpTJTmFweaTNIIgRLvL1zLhvHpX7HgVwa7QVkwenQYcaJ%2Bzc9jF%2BO0JhTq697MCkocu14np1EVK%2FYI19RG03w3J9mlgiT65ThXgLfMTtxixUuaHomFqJULNjkCEpeu7aL2QQ0BQWmdO1VbQEkm0rL9DXGgYcfP1gSAMRiDcaIYflt2zBXggK0EmwQQ%2FUJ%2BHWtHGgPUG2pisusADbMEe7EBSXM1yF5iaQbHFYUH9pxU8X8fLUURknBPUMIB2S8kRtY2nnMKTLdB3suBEG3zddYE5sKNIi3b5s849%2Bd4KMakEvIaHamcvBS0qWPY7ui2nesNnxuyDsGENgwnQYvQ9SxMYZZcWo%2FlY5dD7MI0xxwsMMoEu232olOICEomhwfV2rZLcM%2FM%2BcoMuKfEClnneGEJyc%2F6XSemEAtxU88vaXsdt0LfxW3%2B%2BedN0%2FvpnOfPw2IA%2Fo4SY9e333hDBNkucf8XMyyWwQinrCUlZYsF8xQo6XJUYlzPJ0ZsDOO8CZdJqoIF%2BUg5lVX81tJycTZodS%2BkZqJbYiJkEzALyNWmAF340lg9eWIRmyVUULnza6F7I37bY92eN0oXC9S82H589wDTvFpArtHdpvT77N66hijDJvoa9BjqkAbUbFvspSR4xYH0qJv383hg7R%2FLz8A0cLHfI%2BswDRnsCaEykFkMc0eY5APwI4I9jP%2FZyL0b3pm63nmVGSauiFeGO3kMXF6Uh3BjoCrQOWLl%2B6lT3fwQq1cH%2Fs5fNM%2BOA%2BPy4duMR8YKUJOmP%2BHjiK6tuRTDUu0ZNLDUaWXb7pELSfLoRt3TJx0WOT1oSCX7Pn%2F9tsV7%2F0%2Bt9ssFPExZzL8WSd3qV&X-Amz-Signature=40538ac35a16253d6dd5cedb69635079081966a6181421466668cd13737070d1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666OWY745%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCaB7Z0%2BHLfbTNTyOGxKWOxaveIMyiVyGXI26HSnK0qXwIhAM5z20FQGghFWNGd1izRcdPe6t2RLhWRbUV9NAhKzYTQKv8DCCYQABoMNjM3NDIzMTgzODA1IgxhRa800sE66rklnlUq3AONHTrJyfDR4DTG2bnFEQpTJTmFweaTNIIgRLvL1zLhvHpX7HgVwa7QVkwenQYcaJ%2Bzc9jF%2BO0JhTq697MCkocu14np1EVK%2FYI19RG03w3J9mlgiT65ThXgLfMTtxixUuaHomFqJULNjkCEpeu7aL2QQ0BQWmdO1VbQEkm0rL9DXGgYcfP1gSAMRiDcaIYflt2zBXggK0EmwQQ%2FUJ%2BHWtHGgPUG2pisusADbMEe7EBSXM1yF5iaQbHFYUH9pxU8X8fLUURknBPUMIB2S8kRtY2nnMKTLdB3suBEG3zddYE5sKNIi3b5s849%2Bd4KMakEvIaHamcvBS0qWPY7ui2nesNnxuyDsGENgwnQYvQ9SxMYZZcWo%2FlY5dD7MI0xxwsMMoEu232olOICEomhwfV2rZLcM%2FM%2BcoMuKfEClnneGEJyc%2F6XSemEAtxU88vaXsdt0LfxW3%2B%2BedN0%2FvpnOfPw2IA%2Fo4SY9e333hDBNkucf8XMyyWwQinrCUlZYsF8xQo6XJUYlzPJ0ZsDOO8CZdJqoIF%2BUg5lVX81tJycTZodS%2BkZqJbYiJkEzALyNWmAF340lg9eWIRmyVUULnza6F7I37bY92eN0oXC9S82H589wDTvFpArtHdpvT77N66hijDJvoa9BjqkAbUbFvspSR4xYH0qJv383hg7R%2FLz8A0cLHfI%2BswDRnsCaEykFkMc0eY5APwI4I9jP%2FZyL0b3pm63nmVGSauiFeGO3kMXF6Uh3BjoCrQOWLl%2B6lT3fwQq1cH%2Fs5fNM%2BOA%2BPy4duMR8YKUJOmP%2BHjiK6tuRTDUu0ZNLDUaWXb7pELSfLoRt3TJx0WOT1oSCX7Pn%2F9tsV7%2F0%2Bt9ssFPExZzL8WSd3qV&X-Amz-Signature=24d69cc352db3881f3fbb4beca0178ee130462a42db8b0745554dc73103bd151&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTAVU7WI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDhTeW8CfshdUtRCmMFECVhC8Mf3x1ZVWkMuQK6UrKEFgIgTMr9yEanbq6xWnyfrKkCUuQNPmw8VYchd0iIVl0n1ygq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDHSNXlq29fLQ452uSircAy1%2BX4XrD5T%2FXa5%2Br%2F8OlwzQrjgP2j7l692qB34UZtXEhXysDTe7NWYxBFsq2dFOzSLaNv5eozYChyQyzumFLf8JIIhv0eJ78OyyNTYx1iOnplTFcKX6695alUlT1hJVVUvbmaeUNB9A%2Bvpdw1djud499QcS0ZmfQ3hzB2CvQEpgJHEr6Vqomg4qCseEotM7pjHFGBIIaEsAGxbA9cor%2F%2BfSU9IBA9wmgfREq45gXyhVoDJWjW2pjJWFo42rWLeDCt2ymKIhWaGe4KA7IzdckGXIBmg2UOvlWIP3Pqm7Kf2GMMcQfWAqzYPx8S4ZOE%2BG48pW%2B2jUZhk3Spbjr8oPhCKKbO6lsmW%2B4xEu%2FQyTNSVZUtVRKz7bKdRjJgSsT8GnF90njdzfnwoLiROfNcugR4Hdg1oHWMUUZtRA%2Bsl0i9ZiuECdO0%2BhCs432swJGBkg%2Bt75WzRElFfmeB1W6KeTaUvhhy0TUylTo%2BtknSYsQ3lH4vCphJznTCONPlsB1I1XiqidGSV8yKX2U0YjAy4yTsb6N4l1acnKpw6V5bxne7zTZE38Ib%2FXq291118egaomUspnmmGR1DRZDP2IMk413ZQCuYMwcUWHJ1HKNHY%2F6UV8OrY8eKSMtrPcfybGMO6%2Bhr0GOqUBgKeu4zgVL%2FlJqQVHMP1r1MjnCgbEv6vxmgZEr0D%2FfTMpyy8qiR1Qi5RWGa9S2AWAGSAHxfcEn5VIBKK3E5iCimkWj%2BmQXGjTP2B2RUK6ZynHGwVNdH3c%2FLtTFxPpCEHFtadvQGP44icLt9HbkXeYV3PVtgK2oqTmr8G2UNCd0r6DwTRfdYavnwDt%2BW0Mgghqkp2ygNyGTM9RfxdOaRyljb%2FBAQE%2B&X-Amz-Signature=e7b2199c138c89aea72647b1acedab61c6fb9bd6dfa215daa23c9dae383a37c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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