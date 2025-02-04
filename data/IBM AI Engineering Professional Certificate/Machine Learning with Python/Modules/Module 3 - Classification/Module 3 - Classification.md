

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655CS3LOU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCID%2F%2Bo1nHlD%2BTYAkpbt%2FJvmVY3kgCRCHoCSkK2B7wyjFUAiAzCiAqTJB2lYilxDLn69aWBM1cvd%2BTmnOPjlWIVmESDir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMwb%2FPJkC%2Fj1igOHPaKtwDvbFh%2BJPVsNQC7fOVYY6gOVgyL%2BkQ9nYTQhiGMqjIt6vtm3CbPDvo9hDKA1WkwqqbJgjD8eYf1dZxEt6sOq%2FS17qrsSNbDWMxQGULMmgw1Lqt7W33JfuAcJo9NeJkZLter6PMyqBf%2BOM31tcZByhpF1cE5y%2F83%2BG%2FsY6cCSN7Phvvyo%2F5cwCteBIJHFnuXOwhnvKdbn1UFJpcBurMlqFX%2Bg8S09Jttf2yDmM7E0fR0mTFJnNCnphhx1uH6J4s3ushvYsPQEiNn40ymQP1ttNOyOawEwlt8ju3R%2Fot73GBs5fTviXDMzik4GOHA%2FjiwTiX5a0UyaY8JsguqtVEOPZsmfZ04KVBT6dVQ6kXaJZSxKhxqtOjDadqKmMZIoZhwjwJopiVuPUteYJJrNM9EiePdK6s%2BYMurwvTQCd1VUPNUFIZdMxEc9zgQWdQQyr7SzGo30YMd3qcD73Y006G%2FdlEBu7a1IbbOIuHWdFOtRbBuVI1QY9NhYsRA%2F15DJLQy1aIOk3sa8e%2B2EVc4StQn%2FQE40tPyQixmW%2B%2B9yd%2FiQm28GjDb2%2BFs83i7dZTLLvu5NM0jPAz7yS9SZTBP5r3%2FeP%2Bwj98CNIC6U3C7pcZhPjJP43SUId66Ko24mktlE8wkd2JvQY6pgHLqtZW5%2BaZJhux%2FHmfAeOZvUBHoQ0DHeK%2B5hJx3%2FeRgVGEAadm6tICIQ84tLOEoEdWqePZC6ubWnAPOA4Q7C8uSCNdqRkwPihiY0XFpenq4qxXKHEVUk8UcFxHQbi%2BBqmwcynLjYehj4zOGnBYAXgzLMaEpke0kZq%2BssJrIlzMJ0jB0J1thv6sfnVwHz3yO4yqvpHQpi5XF8MnY5x0kr9HyD3MsqJg&X-Amz-Signature=e3bb273060e2f1b0b7a210359576176a8efb63cdceaf1553121b5287d78fe601&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655CS3LOU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCID%2F%2Bo1nHlD%2BTYAkpbt%2FJvmVY3kgCRCHoCSkK2B7wyjFUAiAzCiAqTJB2lYilxDLn69aWBM1cvd%2BTmnOPjlWIVmESDir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMwb%2FPJkC%2Fj1igOHPaKtwDvbFh%2BJPVsNQC7fOVYY6gOVgyL%2BkQ9nYTQhiGMqjIt6vtm3CbPDvo9hDKA1WkwqqbJgjD8eYf1dZxEt6sOq%2FS17qrsSNbDWMxQGULMmgw1Lqt7W33JfuAcJo9NeJkZLter6PMyqBf%2BOM31tcZByhpF1cE5y%2F83%2BG%2FsY6cCSN7Phvvyo%2F5cwCteBIJHFnuXOwhnvKdbn1UFJpcBurMlqFX%2Bg8S09Jttf2yDmM7E0fR0mTFJnNCnphhx1uH6J4s3ushvYsPQEiNn40ymQP1ttNOyOawEwlt8ju3R%2Fot73GBs5fTviXDMzik4GOHA%2FjiwTiX5a0UyaY8JsguqtVEOPZsmfZ04KVBT6dVQ6kXaJZSxKhxqtOjDadqKmMZIoZhwjwJopiVuPUteYJJrNM9EiePdK6s%2BYMurwvTQCd1VUPNUFIZdMxEc9zgQWdQQyr7SzGo30YMd3qcD73Y006G%2FdlEBu7a1IbbOIuHWdFOtRbBuVI1QY9NhYsRA%2F15DJLQy1aIOk3sa8e%2B2EVc4StQn%2FQE40tPyQixmW%2B%2B9yd%2FiQm28GjDb2%2BFs83i7dZTLLvu5NM0jPAz7yS9SZTBP5r3%2FeP%2Bwj98CNIC6U3C7pcZhPjJP43SUId66Ko24mktlE8wkd2JvQY6pgHLqtZW5%2BaZJhux%2FHmfAeOZvUBHoQ0DHeK%2B5hJx3%2FeRgVGEAadm6tICIQ84tLOEoEdWqePZC6ubWnAPOA4Q7C8uSCNdqRkwPihiY0XFpenq4qxXKHEVUk8UcFxHQbi%2BBqmwcynLjYehj4zOGnBYAXgzLMaEpke0kZq%2BssJrIlzMJ0jB0J1thv6sfnVwHz3yO4yqvpHQpi5XF8MnY5x0kr9HyD3MsqJg&X-Amz-Signature=f1967888d3180006d6c30f13952e05fc214ad11c648a5fa010093a29228b24a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655CS3LOU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCID%2F%2Bo1nHlD%2BTYAkpbt%2FJvmVY3kgCRCHoCSkK2B7wyjFUAiAzCiAqTJB2lYilxDLn69aWBM1cvd%2BTmnOPjlWIVmESDir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMwb%2FPJkC%2Fj1igOHPaKtwDvbFh%2BJPVsNQC7fOVYY6gOVgyL%2BkQ9nYTQhiGMqjIt6vtm3CbPDvo9hDKA1WkwqqbJgjD8eYf1dZxEt6sOq%2FS17qrsSNbDWMxQGULMmgw1Lqt7W33JfuAcJo9NeJkZLter6PMyqBf%2BOM31tcZByhpF1cE5y%2F83%2BG%2FsY6cCSN7Phvvyo%2F5cwCteBIJHFnuXOwhnvKdbn1UFJpcBurMlqFX%2Bg8S09Jttf2yDmM7E0fR0mTFJnNCnphhx1uH6J4s3ushvYsPQEiNn40ymQP1ttNOyOawEwlt8ju3R%2Fot73GBs5fTviXDMzik4GOHA%2FjiwTiX5a0UyaY8JsguqtVEOPZsmfZ04KVBT6dVQ6kXaJZSxKhxqtOjDadqKmMZIoZhwjwJopiVuPUteYJJrNM9EiePdK6s%2BYMurwvTQCd1VUPNUFIZdMxEc9zgQWdQQyr7SzGo30YMd3qcD73Y006G%2FdlEBu7a1IbbOIuHWdFOtRbBuVI1QY9NhYsRA%2F15DJLQy1aIOk3sa8e%2B2EVc4StQn%2FQE40tPyQixmW%2B%2B9yd%2FiQm28GjDb2%2BFs83i7dZTLLvu5NM0jPAz7yS9SZTBP5r3%2FeP%2Bwj98CNIC6U3C7pcZhPjJP43SUId66Ko24mktlE8wkd2JvQY6pgHLqtZW5%2BaZJhux%2FHmfAeOZvUBHoQ0DHeK%2B5hJx3%2FeRgVGEAadm6tICIQ84tLOEoEdWqePZC6ubWnAPOA4Q7C8uSCNdqRkwPihiY0XFpenq4qxXKHEVUk8UcFxHQbi%2BBqmwcynLjYehj4zOGnBYAXgzLMaEpke0kZq%2BssJrIlzMJ0jB0J1thv6sfnVwHz3yO4yqvpHQpi5XF8MnY5x0kr9HyD3MsqJg&X-Amz-Signature=5dabf5dfd520702f21100a04999954c89555a331f9a805af67b06e273b2c58dc&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUETHPT4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIDQpa8j54oINdJ7zIHks1cwaTplkziOwOzWuWJTJSqV3AiAgPyT6r1cXAWI4M18pm2cVlMnL%2FBQxM%2B%2FgJbOyQkZWgSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIM1tbTEuLJPYJ8Kr6YKtwDYR1zMJVRF0HCYRhc1uqI9AIRbwBmhb1inRMvE05yhScyMTN5vqObVeaMf6RXsmOPW98qYaGzGbR9BijMeYoabXEFMhRysfzenbSWQSOfuCBxJ7QOqDjPRWcvFlHL%2F87nMl08tE2WnTkKUkLtJzy3B1AEs91%2FA3ZUc%2B1NL%2FhFIot7pV6Y07%2BiYk9iz3Scdt7LdDa2wEOmXmOJtiO6YGEfBoOjSaArZFbDS3Yp0a%2BhUO0gZlJXjqbwWagwbQ9Ki%2BNkTvTjF5Z7HYSSbM5qIgH8e72gycN1nL16eIOyE3sOQbsWEmEFASUxXhhh%2BzLkheeHf0Nu%2FIxTC5WE0pUDzKpbvSE1ndUekQlnMf41vLvWeoGSXm2S0Wrr0cJcC4h05pikR4YrKC98WIfKJ0XggATe11xiKnWsW7Q3vc6srR3EzFuB4x7yljiN1As55%2B4KxE6N5sRT12i9AOsaQJNXNtI96N9zRYNh93%2FyAe%2BSJ6axdJo6TWlAd8Iix%2BGmGIlmPRlc2jZhThnAErg6bZFu%2FuqqvFeRLsn6%2BRPAIdX99UF6Gpvnv5kVP28Vhf586ii0wKlTLmj2lx%2Fhzie0KR%2BkoD1okB57yKuFZK8TEO%2BkW19gBmHDa6sp5i6uuFotWG4w392JvQY6pgH3YcSxdj5eWyvbnLWm1KoG2okUBARECzLpS8b9QaA3uxKW9vtUJxoCFMwHqZGkRtcV2hGU5NyrmIzBEPJRWY32b%2F36%2FDCnF1cnOgrItyB17l8lAnzZin1FXDosleHsVEGKJCaKJ9b07CTLemPWaipALIyZTkTAjEtAtxRdUijSr1h4y7DRfVdFs7Jo4EvYAIGPcN%2F4vzQWWZFaa7CczCLEG%2F3oh30d&X-Amz-Signature=6f1391be65d812e54ae88b91d8c2a25b71bdfa5471d758ce129caff7df2939a5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUETHPT4%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIDQpa8j54oINdJ7zIHks1cwaTplkziOwOzWuWJTJSqV3AiAgPyT6r1cXAWI4M18pm2cVlMnL%2FBQxM%2B%2FgJbOyQkZWgSr%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIM1tbTEuLJPYJ8Kr6YKtwDYR1zMJVRF0HCYRhc1uqI9AIRbwBmhb1inRMvE05yhScyMTN5vqObVeaMf6RXsmOPW98qYaGzGbR9BijMeYoabXEFMhRysfzenbSWQSOfuCBxJ7QOqDjPRWcvFlHL%2F87nMl08tE2WnTkKUkLtJzy3B1AEs91%2FA3ZUc%2B1NL%2FhFIot7pV6Y07%2BiYk9iz3Scdt7LdDa2wEOmXmOJtiO6YGEfBoOjSaArZFbDS3Yp0a%2BhUO0gZlJXjqbwWagwbQ9Ki%2BNkTvTjF5Z7HYSSbM5qIgH8e72gycN1nL16eIOyE3sOQbsWEmEFASUxXhhh%2BzLkheeHf0Nu%2FIxTC5WE0pUDzKpbvSE1ndUekQlnMf41vLvWeoGSXm2S0Wrr0cJcC4h05pikR4YrKC98WIfKJ0XggATe11xiKnWsW7Q3vc6srR3EzFuB4x7yljiN1As55%2B4KxE6N5sRT12i9AOsaQJNXNtI96N9zRYNh93%2FyAe%2BSJ6axdJo6TWlAd8Iix%2BGmGIlmPRlc2jZhThnAErg6bZFu%2FuqqvFeRLsn6%2BRPAIdX99UF6Gpvnv5kVP28Vhf586ii0wKlTLmj2lx%2Fhzie0KR%2BkoD1okB57yKuFZK8TEO%2BkW19gBmHDa6sp5i6uuFotWG4w392JvQY6pgH3YcSxdj5eWyvbnLWm1KoG2okUBARECzLpS8b9QaA3uxKW9vtUJxoCFMwHqZGkRtcV2hGU5NyrmIzBEPJRWY32b%2F36%2FDCnF1cnOgrItyB17l8lAnzZin1FXDosleHsVEGKJCaKJ9b07CTLemPWaipALIyZTkTAjEtAtxRdUijSr1h4y7DRfVdFs7Jo4EvYAIGPcN%2F4vzQWWZFaa7CczCLEG%2F3oh30d&X-Amz-Signature=f858771e7f0b281cefdfa13a62d06f9c692e4414a7c593b4af49b255c6c8b862&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655CS3LOU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCID%2F%2Bo1nHlD%2BTYAkpbt%2FJvmVY3kgCRCHoCSkK2B7wyjFUAiAzCiAqTJB2lYilxDLn69aWBM1cvd%2BTmnOPjlWIVmESDir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIMwb%2FPJkC%2Fj1igOHPaKtwDvbFh%2BJPVsNQC7fOVYY6gOVgyL%2BkQ9nYTQhiGMqjIt6vtm3CbPDvo9hDKA1WkwqqbJgjD8eYf1dZxEt6sOq%2FS17qrsSNbDWMxQGULMmgw1Lqt7W33JfuAcJo9NeJkZLter6PMyqBf%2BOM31tcZByhpF1cE5y%2F83%2BG%2FsY6cCSN7Phvvyo%2F5cwCteBIJHFnuXOwhnvKdbn1UFJpcBurMlqFX%2Bg8S09Jttf2yDmM7E0fR0mTFJnNCnphhx1uH6J4s3ushvYsPQEiNn40ymQP1ttNOyOawEwlt8ju3R%2Fot73GBs5fTviXDMzik4GOHA%2FjiwTiX5a0UyaY8JsguqtVEOPZsmfZ04KVBT6dVQ6kXaJZSxKhxqtOjDadqKmMZIoZhwjwJopiVuPUteYJJrNM9EiePdK6s%2BYMurwvTQCd1VUPNUFIZdMxEc9zgQWdQQyr7SzGo30YMd3qcD73Y006G%2FdlEBu7a1IbbOIuHWdFOtRbBuVI1QY9NhYsRA%2F15DJLQy1aIOk3sa8e%2B2EVc4StQn%2FQE40tPyQixmW%2B%2B9yd%2FiQm28GjDb2%2BFs83i7dZTLLvu5NM0jPAz7yS9SZTBP5r3%2FeP%2Bwj98CNIC6U3C7pcZhPjJP43SUId66Ko24mktlE8wkd2JvQY6pgHLqtZW5%2BaZJhux%2FHmfAeOZvUBHoQ0DHeK%2B5hJx3%2FeRgVGEAadm6tICIQ84tLOEoEdWqePZC6ubWnAPOA4Q7C8uSCNdqRkwPihiY0XFpenq4qxXKHEVUk8UcFxHQbi%2BBqmwcynLjYehj4zOGnBYAXgzLMaEpke0kZq%2BssJrIlzMJ0jB0J1thv6sfnVwHz3yO4yqvpHQpi5XF8MnY5x0kr9HyD3MsqJg&X-Amz-Signature=e3cfd623879ad259b5144e5ddc1b884b3d14f6f1e930e9e3e052cfe054f70e56&X-Amz-SignedHeaders=host&x-id=GetObject)
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