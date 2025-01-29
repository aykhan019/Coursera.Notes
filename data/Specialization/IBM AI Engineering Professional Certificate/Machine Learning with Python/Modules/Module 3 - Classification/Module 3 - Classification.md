

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFHLD2P7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDjaZg6GjfY%2F0OAOh4aL1DJ1S%2Fje2qR5tVI9bv%2BAKkYKAIhAJL1OeUG1RHXv2%2B4lyHbL5JWTXKThTgZ0NOsORzgDOkiKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJr6ytA67Fjyj7ZXAq3ANaypBWmDer6PzIpx9I1HfC7lPBJkUN6YZrbS5dyhiaU7T0q6om%2BWklN6vCEMHVc04MTtVLeD5Q848mHT%2FwrCCMCswCcUFjbVBPKdw5mYskYwjZZjFLlDPIdQ4wrbBL2CFbn4qDE0pluKPFb9wc5utrEN0Nh2h8NCabZVj6ArRhr%2FhJRkUAwQYsP3NefPm8t3%2FZCgqJ5hzho49pZsZUaIQ0ijq%2FIiPBYGKiQWBzkGhv1TGGFv0oxmphcpgR3kWF0Vkbp9Q2iy06xO%2Fra64teIy0269edfHVYPtpiKCPPiNPdw7e0sIeq3LaJ6fCnQy3W1iijxwC5ON8vjEGjrNuFh6W9VgmRjYIhbh5I0tdgJxEx5d2dSpwcLbtLTHJjXq0Yf1M%2BclcOCFZ0rSrCJmQs3l6E3DFNkWiW11wVDfggjvlr7BoGc2hIx45rN0E7Ksi5DBWEUBjSO8XATLSMGK8nEdoLPy11i92QAeF8oZQ87bihtb8Bm5haf4bn7OTS0nIgw8GkbtYiedhQtkAepi8OizIQLsc4fS9k%2FzjF2DFO0Krv96%2F1xn9KNsW1pPGv%2B5v%2FTfnNA%2FQ1PBCykYCXURll34yWsCVGr0nm7ihj2XG4RNeVHBe1rC2dnZVSltReDCFu%2Ba8BjqkAQPk2G1hHjFMAQHWPghBwJaUeLZcGJsoJFaNHgshRk6rcbImuYu3tyWHalzMQipwNGouUs8v6M%2BgSuYaqXLSMV9Nt%2BiOIlpUYKWB9nfKbQ8ep%2BntbH95kYTfj0l98KkVzYY21ToTewEJI8lKGEi%2FuArNJkFpGIxJZMFv2KavPltvc32QR20UijY1wReo%2FKYF479ahmuFHFULLxA%2BsHXwED9OZPyA&X-Amz-Signature=eb5dee6ca490283adcdc627319dcb451c9e8da9ed5ab01048a0f15655ab645c4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFHLD2P7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDjaZg6GjfY%2F0OAOh4aL1DJ1S%2Fje2qR5tVI9bv%2BAKkYKAIhAJL1OeUG1RHXv2%2B4lyHbL5JWTXKThTgZ0NOsORzgDOkiKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJr6ytA67Fjyj7ZXAq3ANaypBWmDer6PzIpx9I1HfC7lPBJkUN6YZrbS5dyhiaU7T0q6om%2BWklN6vCEMHVc04MTtVLeD5Q848mHT%2FwrCCMCswCcUFjbVBPKdw5mYskYwjZZjFLlDPIdQ4wrbBL2CFbn4qDE0pluKPFb9wc5utrEN0Nh2h8NCabZVj6ArRhr%2FhJRkUAwQYsP3NefPm8t3%2FZCgqJ5hzho49pZsZUaIQ0ijq%2FIiPBYGKiQWBzkGhv1TGGFv0oxmphcpgR3kWF0Vkbp9Q2iy06xO%2Fra64teIy0269edfHVYPtpiKCPPiNPdw7e0sIeq3LaJ6fCnQy3W1iijxwC5ON8vjEGjrNuFh6W9VgmRjYIhbh5I0tdgJxEx5d2dSpwcLbtLTHJjXq0Yf1M%2BclcOCFZ0rSrCJmQs3l6E3DFNkWiW11wVDfggjvlr7BoGc2hIx45rN0E7Ksi5DBWEUBjSO8XATLSMGK8nEdoLPy11i92QAeF8oZQ87bihtb8Bm5haf4bn7OTS0nIgw8GkbtYiedhQtkAepi8OizIQLsc4fS9k%2FzjF2DFO0Krv96%2F1xn9KNsW1pPGv%2B5v%2FTfnNA%2FQ1PBCykYCXURll34yWsCVGr0nm7ihj2XG4RNeVHBe1rC2dnZVSltReDCFu%2Ba8BjqkAQPk2G1hHjFMAQHWPghBwJaUeLZcGJsoJFaNHgshRk6rcbImuYu3tyWHalzMQipwNGouUs8v6M%2BgSuYaqXLSMV9Nt%2BiOIlpUYKWB9nfKbQ8ep%2BntbH95kYTfj0l98KkVzYY21ToTewEJI8lKGEi%2FuArNJkFpGIxJZMFv2KavPltvc32QR20UijY1wReo%2FKYF479ahmuFHFULLxA%2BsHXwED9OZPyA&X-Amz-Signature=158fce0e19be2f0783944c66fb0e1d009ddad1b5d31ecff459bc4765390e0929&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFHLD2P7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDjaZg6GjfY%2F0OAOh4aL1DJ1S%2Fje2qR5tVI9bv%2BAKkYKAIhAJL1OeUG1RHXv2%2B4lyHbL5JWTXKThTgZ0NOsORzgDOkiKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJr6ytA67Fjyj7ZXAq3ANaypBWmDer6PzIpx9I1HfC7lPBJkUN6YZrbS5dyhiaU7T0q6om%2BWklN6vCEMHVc04MTtVLeD5Q848mHT%2FwrCCMCswCcUFjbVBPKdw5mYskYwjZZjFLlDPIdQ4wrbBL2CFbn4qDE0pluKPFb9wc5utrEN0Nh2h8NCabZVj6ArRhr%2FhJRkUAwQYsP3NefPm8t3%2FZCgqJ5hzho49pZsZUaIQ0ijq%2FIiPBYGKiQWBzkGhv1TGGFv0oxmphcpgR3kWF0Vkbp9Q2iy06xO%2Fra64teIy0269edfHVYPtpiKCPPiNPdw7e0sIeq3LaJ6fCnQy3W1iijxwC5ON8vjEGjrNuFh6W9VgmRjYIhbh5I0tdgJxEx5d2dSpwcLbtLTHJjXq0Yf1M%2BclcOCFZ0rSrCJmQs3l6E3DFNkWiW11wVDfggjvlr7BoGc2hIx45rN0E7Ksi5DBWEUBjSO8XATLSMGK8nEdoLPy11i92QAeF8oZQ87bihtb8Bm5haf4bn7OTS0nIgw8GkbtYiedhQtkAepi8OizIQLsc4fS9k%2FzjF2DFO0Krv96%2F1xn9KNsW1pPGv%2B5v%2FTfnNA%2FQ1PBCykYCXURll34yWsCVGr0nm7ihj2XG4RNeVHBe1rC2dnZVSltReDCFu%2Ba8BjqkAQPk2G1hHjFMAQHWPghBwJaUeLZcGJsoJFaNHgshRk6rcbImuYu3tyWHalzMQipwNGouUs8v6M%2BgSuYaqXLSMV9Nt%2BiOIlpUYKWB9nfKbQ8ep%2BntbH95kYTfj0l98KkVzYY21ToTewEJI8lKGEi%2FuArNJkFpGIxJZMFv2KavPltvc32QR20UijY1wReo%2FKYF479ahmuFHFULLxA%2BsHXwED9OZPyA&X-Amz-Signature=d6f4e58c682128e874e324494927babf5068a0c4d1a5ba9e9044cb5ee1124286&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JCG6R5T%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDRb6iMNIz3mmnhCh7VMK9mwgHNaMCU7CYUuXcSKK7xmQIhAOp4mWDhqQG%2FQlxUVxHSOmo3rLNLEr%2BlYPaIXrCmEf%2BVKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOXENQqQITt4%2FTswIq3AMMACChm%2FJg6S14O6j%2Fgw7F%2FGAPL2Q5eTsNdWp58oUyjXjnmC8kYLP67XnGg2UmejzJlFeQjtMaKWgOgqmHn0GYWsxvUyY3gb1GW2Wn2icvJXbubvyTUvUAaMzbl9v36a2Qr%2BFfpr00MxmdXm7JxoALTM83mKW8Cxqo219%2FVZu%2BpTlDadzSX2tibWkDclOh6sj%2FaGGnscePiyY3snJBY1OHCMGPVggbGm2zjeagFOpLwSFiKDMIzuBxIKZ8rQPew6aYXmNM8hGhzfwFCg1zLyEHTuhIsw6MYsV4mqNzkMDQ5MXeGduuqwIe5nEQeTCA774wSYQbsH%2BiS8TLwHVPi1pK6ARhFIc%2B7CZgMxig6hWYIJY1jjqXQqAmS0ujeT0xHIw6YKprfIfDwGNwq91%2FxAvqsPzDm%2FPrB6ThlOn3HIDlcm6OsO0UU0ZlYI3sdCYaCQDDguY635vO8s5i9%2B5QZqNPbzQr6Ns%2B53DDsUwdS74mC%2B0TBNwP7b7J2krvwbDfNDf5dCVwL1SCuI4woTf5jeYnTOhexOwx404y1fR8hC0ebrmc9zEcVTDa8NjTx%2BcMJ6VPeACK0uaFH0%2FQgYd8sTJux83PN7fNww2PazutTndl4%2BoBkp0f0O1751%2F0%2FjD7uua8BjqkAauqr96xhPGlvll4ZUfjP7m0mjO8t%2FvnJaop4a8JXTPq7ItmSVdGqY3fMQNX9F7tQ2GT5koN0cROlifuKCePs1eXENXbkI74HNblRtC4nGtilqUues%2FHrIMBDbzF%2FGHVnqOIwqrKNZKMRlSfx47ONSZaI9Bj5taMPnjiYVcxl7N8QTogipEP8epQwsEd1PF9Rf8Uwb5MKyZLkhYWU0w5%2BmVYbdTm&X-Amz-Signature=02a0497b83fc26c0ed7f1e8a1d10267317c780a50e1d9765f53154f50f11af37&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JCG6R5T%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDRb6iMNIz3mmnhCh7VMK9mwgHNaMCU7CYUuXcSKK7xmQIhAOp4mWDhqQG%2FQlxUVxHSOmo3rLNLEr%2BlYPaIXrCmEf%2BVKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOXENQqQITt4%2FTswIq3AMMACChm%2FJg6S14O6j%2Fgw7F%2FGAPL2Q5eTsNdWp58oUyjXjnmC8kYLP67XnGg2UmejzJlFeQjtMaKWgOgqmHn0GYWsxvUyY3gb1GW2Wn2icvJXbubvyTUvUAaMzbl9v36a2Qr%2BFfpr00MxmdXm7JxoALTM83mKW8Cxqo219%2FVZu%2BpTlDadzSX2tibWkDclOh6sj%2FaGGnscePiyY3snJBY1OHCMGPVggbGm2zjeagFOpLwSFiKDMIzuBxIKZ8rQPew6aYXmNM8hGhzfwFCg1zLyEHTuhIsw6MYsV4mqNzkMDQ5MXeGduuqwIe5nEQeTCA774wSYQbsH%2BiS8TLwHVPi1pK6ARhFIc%2B7CZgMxig6hWYIJY1jjqXQqAmS0ujeT0xHIw6YKprfIfDwGNwq91%2FxAvqsPzDm%2FPrB6ThlOn3HIDlcm6OsO0UU0ZlYI3sdCYaCQDDguY635vO8s5i9%2B5QZqNPbzQr6Ns%2B53DDsUwdS74mC%2B0TBNwP7b7J2krvwbDfNDf5dCVwL1SCuI4woTf5jeYnTOhexOwx404y1fR8hC0ebrmc9zEcVTDa8NjTx%2BcMJ6VPeACK0uaFH0%2FQgYd8sTJux83PN7fNww2PazutTndl4%2BoBkp0f0O1751%2F0%2FjD7uua8BjqkAauqr96xhPGlvll4ZUfjP7m0mjO8t%2FvnJaop4a8JXTPq7ItmSVdGqY3fMQNX9F7tQ2GT5koN0cROlifuKCePs1eXENXbkI74HNblRtC4nGtilqUues%2FHrIMBDbzF%2FGHVnqOIwqrKNZKMRlSfx47ONSZaI9Bj5taMPnjiYVcxl7N8QTogipEP8epQwsEd1PF9Rf8Uwb5MKyZLkhYWU0w5%2BmVYbdTm&X-Amz-Signature=50622557292db85d14ce27619eefbc5ee323e5a2a6659b2c39fd192b6c498fee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFHLD2P7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDjaZg6GjfY%2F0OAOh4aL1DJ1S%2Fje2qR5tVI9bv%2BAKkYKAIhAJL1OeUG1RHXv2%2B4lyHbL5JWTXKThTgZ0NOsORzgDOkiKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJr6ytA67Fjyj7ZXAq3ANaypBWmDer6PzIpx9I1HfC7lPBJkUN6YZrbS5dyhiaU7T0q6om%2BWklN6vCEMHVc04MTtVLeD5Q848mHT%2FwrCCMCswCcUFjbVBPKdw5mYskYwjZZjFLlDPIdQ4wrbBL2CFbn4qDE0pluKPFb9wc5utrEN0Nh2h8NCabZVj6ArRhr%2FhJRkUAwQYsP3NefPm8t3%2FZCgqJ5hzho49pZsZUaIQ0ijq%2FIiPBYGKiQWBzkGhv1TGGFv0oxmphcpgR3kWF0Vkbp9Q2iy06xO%2Fra64teIy0269edfHVYPtpiKCPPiNPdw7e0sIeq3LaJ6fCnQy3W1iijxwC5ON8vjEGjrNuFh6W9VgmRjYIhbh5I0tdgJxEx5d2dSpwcLbtLTHJjXq0Yf1M%2BclcOCFZ0rSrCJmQs3l6E3DFNkWiW11wVDfggjvlr7BoGc2hIx45rN0E7Ksi5DBWEUBjSO8XATLSMGK8nEdoLPy11i92QAeF8oZQ87bihtb8Bm5haf4bn7OTS0nIgw8GkbtYiedhQtkAepi8OizIQLsc4fS9k%2FzjF2DFO0Krv96%2F1xn9KNsW1pPGv%2B5v%2FTfnNA%2FQ1PBCykYCXURll34yWsCVGr0nm7ihj2XG4RNeVHBe1rC2dnZVSltReDCFu%2Ba8BjqkAQPk2G1hHjFMAQHWPghBwJaUeLZcGJsoJFaNHgshRk6rcbImuYu3tyWHalzMQipwNGouUs8v6M%2BgSuYaqXLSMV9Nt%2BiOIlpUYKWB9nfKbQ8ep%2BntbH95kYTfj0l98KkVzYY21ToTewEJI8lKGEi%2FuArNJkFpGIxJZMFv2KavPltvc32QR20UijY1wReo%2FKYF479ahmuFHFULLxA%2BsHXwED9OZPyA&X-Amz-Signature=aefad648cc07a8566e4e2b0ea9f4a73b68c682996c9dbc35219a57e9f04316f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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