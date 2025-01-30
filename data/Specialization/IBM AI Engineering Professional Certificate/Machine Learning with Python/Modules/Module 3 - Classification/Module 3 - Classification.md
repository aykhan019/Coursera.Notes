

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHTIE45J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGHPfWqfpL34OKeL4tCUCrfIeSupqH%2F%2BcngGUxNCY2pqAiEAxsy0K4ovyiq1U%2BxqvNQ%2BEeVgzEdWPWMO1%2B%2BAiftOWx0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGwEHSFC9E76IZl83CrcA19vea0z735xxeffM6e8n%2FM5ca7CMmxHURHIh2zs8I4lZEfsiM5G7F9WjHilRoFSejXvQGqdBWI%2FmZZjTZIXqytswBcAuhS5IuQvthBvoR55iGcAetORZiNwaSyf0xyeSWLIiupvasnndgr0O%2FqA%2FgiCHKWzoifOJKEPM2kuvczROc3F0WXKBskhqjBpJuZxycCfKP1lqK4ojkdeP2%2BnXzNGeMPXz9QAs9Q8Eh4MnVXc%2B%2FdSoFvOpDKPh%2BRTAFJb5eqMzHGBO9%2Fl%2Fq0UNSU5UsVO6kRS7qlTjhON0DeWqjRGMRSliCSmdR2BzBTlcgVX8ZLMfL3In8VSSil5%2FJvP%2F33Wiwkz7U4PEVJ%2F8WOr7DP2iewhGbew6hdQ2Z0a38Lc0jB%2FFQBLD6Smu%2FNRejWL6IAB5plq8%2B3aL2Qvcutuq2Za%2FBNGDq2%2Fr0pSzlL9CQ0F9eWwsvK9%2FFShxwKYXvlKkio2D%2FYI2dlIHYxa7SqlWurzMVxauxLf%2FnqgtZz1ztnS6sCfgi84X%2B%2F3N5l5Yk6hJhQ4g6f1T%2BYzZcgEpijAu4kz8KkYBcqFGO88tFhtOss%2FcX0SZDi5HP5sKjF8MsEB%2FcgRJpYgbnP2vXF25bUH4VXopPUcUki7q1fKOsOdMIey67wGOqUBU8%2BATu1D%2BOCH6KMCbNXkwQ1bnP1jfu7hl%2F4d3n6P2b9Pl4lEPUhyGa%2BRVe0L2dzElY4eTwYNt3jUak8usAsPLAbejrAiaIiNsIxELLszo2qe6WnbvfHaWrkJtW4M%2BnnE%2BVAQoJ3HfLsq2nkPFSsBv%2B5cEqyxnRU8sQtbuPYG6c%2B2suJJQDLSrbV1aM7aMQvZAYVrPo0FNI31hLWhcsSAbP7Uoh67&X-Amz-Signature=bdbf68acae1d4a2c633bd60b844ce5c7af9f9d6301bbed351e86d6a65020fb22&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHTIE45J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGHPfWqfpL34OKeL4tCUCrfIeSupqH%2F%2BcngGUxNCY2pqAiEAxsy0K4ovyiq1U%2BxqvNQ%2BEeVgzEdWPWMO1%2B%2BAiftOWx0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGwEHSFC9E76IZl83CrcA19vea0z735xxeffM6e8n%2FM5ca7CMmxHURHIh2zs8I4lZEfsiM5G7F9WjHilRoFSejXvQGqdBWI%2FmZZjTZIXqytswBcAuhS5IuQvthBvoR55iGcAetORZiNwaSyf0xyeSWLIiupvasnndgr0O%2FqA%2FgiCHKWzoifOJKEPM2kuvczROc3F0WXKBskhqjBpJuZxycCfKP1lqK4ojkdeP2%2BnXzNGeMPXz9QAs9Q8Eh4MnVXc%2B%2FdSoFvOpDKPh%2BRTAFJb5eqMzHGBO9%2Fl%2Fq0UNSU5UsVO6kRS7qlTjhON0DeWqjRGMRSliCSmdR2BzBTlcgVX8ZLMfL3In8VSSil5%2FJvP%2F33Wiwkz7U4PEVJ%2F8WOr7DP2iewhGbew6hdQ2Z0a38Lc0jB%2FFQBLD6Smu%2FNRejWL6IAB5plq8%2B3aL2Qvcutuq2Za%2FBNGDq2%2Fr0pSzlL9CQ0F9eWwsvK9%2FFShxwKYXvlKkio2D%2FYI2dlIHYxa7SqlWurzMVxauxLf%2FnqgtZz1ztnS6sCfgi84X%2B%2F3N5l5Yk6hJhQ4g6f1T%2BYzZcgEpijAu4kz8KkYBcqFGO88tFhtOss%2FcX0SZDi5HP5sKjF8MsEB%2FcgRJpYgbnP2vXF25bUH4VXopPUcUki7q1fKOsOdMIey67wGOqUBU8%2BATu1D%2BOCH6KMCbNXkwQ1bnP1jfu7hl%2F4d3n6P2b9Pl4lEPUhyGa%2BRVe0L2dzElY4eTwYNt3jUak8usAsPLAbejrAiaIiNsIxELLszo2qe6WnbvfHaWrkJtW4M%2BnnE%2BVAQoJ3HfLsq2nkPFSsBv%2B5cEqyxnRU8sQtbuPYG6c%2B2suJJQDLSrbV1aM7aMQvZAYVrPo0FNI31hLWhcsSAbP7Uoh67&X-Amz-Signature=f5d3e8ddb43cd6e38124f28607bb7d32280d1e9deb5793b14bea4cd7cc0a847f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHTIE45J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGHPfWqfpL34OKeL4tCUCrfIeSupqH%2F%2BcngGUxNCY2pqAiEAxsy0K4ovyiq1U%2BxqvNQ%2BEeVgzEdWPWMO1%2B%2BAiftOWx0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGwEHSFC9E76IZl83CrcA19vea0z735xxeffM6e8n%2FM5ca7CMmxHURHIh2zs8I4lZEfsiM5G7F9WjHilRoFSejXvQGqdBWI%2FmZZjTZIXqytswBcAuhS5IuQvthBvoR55iGcAetORZiNwaSyf0xyeSWLIiupvasnndgr0O%2FqA%2FgiCHKWzoifOJKEPM2kuvczROc3F0WXKBskhqjBpJuZxycCfKP1lqK4ojkdeP2%2BnXzNGeMPXz9QAs9Q8Eh4MnVXc%2B%2FdSoFvOpDKPh%2BRTAFJb5eqMzHGBO9%2Fl%2Fq0UNSU5UsVO6kRS7qlTjhON0DeWqjRGMRSliCSmdR2BzBTlcgVX8ZLMfL3In8VSSil5%2FJvP%2F33Wiwkz7U4PEVJ%2F8WOr7DP2iewhGbew6hdQ2Z0a38Lc0jB%2FFQBLD6Smu%2FNRejWL6IAB5plq8%2B3aL2Qvcutuq2Za%2FBNGDq2%2Fr0pSzlL9CQ0F9eWwsvK9%2FFShxwKYXvlKkio2D%2FYI2dlIHYxa7SqlWurzMVxauxLf%2FnqgtZz1ztnS6sCfgi84X%2B%2F3N5l5Yk6hJhQ4g6f1T%2BYzZcgEpijAu4kz8KkYBcqFGO88tFhtOss%2FcX0SZDi5HP5sKjF8MsEB%2FcgRJpYgbnP2vXF25bUH4VXopPUcUki7q1fKOsOdMIey67wGOqUBU8%2BATu1D%2BOCH6KMCbNXkwQ1bnP1jfu7hl%2F4d3n6P2b9Pl4lEPUhyGa%2BRVe0L2dzElY4eTwYNt3jUak8usAsPLAbejrAiaIiNsIxELLszo2qe6WnbvfHaWrkJtW4M%2BnnE%2BVAQoJ3HfLsq2nkPFSsBv%2B5cEqyxnRU8sQtbuPYG6c%2B2suJJQDLSrbV1aM7aMQvZAYVrPo0FNI31hLWhcsSAbP7Uoh67&X-Amz-Signature=0176902c7fc5f6c459be83bdac4b726193dc2738e5eb6b5a9db647e8260eaef1&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOWJWWYO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFcUiJPsOH9ZfcPG11DHLXnEVPqywm9ncmnaYBz8b0uAIgfzcHxg0deZgPwFX0FE9A94se4QcRFXvUPOkhOnvSuvoqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSWRnrmYdlKMLFmSircA2f27Kd3ClRe2FBHyibR0QzANNL5iyDs1QIoNJv%2BXkcLovDEyx%2BaNbEkkRsA7CLl014OykluO0kFQjDyBV8Ax9pwngz%2FQctLOe6EA07Sqs%2FwmUJihgrQWV7NHPyLWIwsK%2F7O3W0QhaMLDp2bb1u1%2FUhtP6zuyFS6sQrU6TVfVbNHqsYnTw0KXM5xo5V0zX%2BJZxMJwS26bORVot%2Fd3aKfjYMHzHnZw97ezRrSiz2DccTkmdS4IpRN3d4vDDIKklP%2FvK0Nj4p9wLCMGfTqmOEajumxSfV%2FKJjXSIVndo2%2FSgjZcBedOcLj3H1k1%2BlAxj6oX1sJMSAvlVmIcQja%2FpbvantFVdmIMY77fy5s9Fri9J3urxxFwPlIZ3z9Ucr5WmXSwEksU8KlmKtWVl6moV2%2BJQDjNmMgxKzN6Q%2FXfiNVxO6VhdM%2BOluFp54k%2BOiMXxpir0tLZw%2FFYnDA%2Fa996W9xf%2FldlLmk1K9JTt%2BxLzkYlbQ39TjP7zaqAq89NnJtAyi1WLuVTYjG0msGvj3Crf9fzi4JlbcG1FG9zZvM7wAovDYzgUI4eaC5aySelVrUgks6ZySW%2BCh%2Br1JoM0wMgk2Acz5g40kLpFAPm%2FeY6jlj0xTcoVGZQXqsuFKAsN2jMOSx67wGOqUBqbR1jsJ%2BMnEipIwbSMud%2BeVMSgTtEvmS2tBjEOwMwqnzslq3yHpleiUhD7LbR%2F87j9WOSxm54P8qFsRAiT5k2bE2tSfw1vrNj33xlJRm6rY5Zw%2FOf5wOl1FtkYhvA%2FuGSWffWvQM1JWXJYRjkALEej7c5zIVtnkzzvDzLi9VLrrSu6nxkZhOPrkvVLe9dw0U0vWvMIoMFWV%2Fvw9kAQu3VBwZt47g&X-Amz-Signature=082dbd8a35fc3d745f9fb5cb7978719a12460e096dd56621bfa7a83336dbb1fb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOWJWWYO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCFcUiJPsOH9ZfcPG11DHLXnEVPqywm9ncmnaYBz8b0uAIgfzcHxg0deZgPwFX0FE9A94se4QcRFXvUPOkhOnvSuvoqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSWRnrmYdlKMLFmSircA2f27Kd3ClRe2FBHyibR0QzANNL5iyDs1QIoNJv%2BXkcLovDEyx%2BaNbEkkRsA7CLl014OykluO0kFQjDyBV8Ax9pwngz%2FQctLOe6EA07Sqs%2FwmUJihgrQWV7NHPyLWIwsK%2F7O3W0QhaMLDp2bb1u1%2FUhtP6zuyFS6sQrU6TVfVbNHqsYnTw0KXM5xo5V0zX%2BJZxMJwS26bORVot%2Fd3aKfjYMHzHnZw97ezRrSiz2DccTkmdS4IpRN3d4vDDIKklP%2FvK0Nj4p9wLCMGfTqmOEajumxSfV%2FKJjXSIVndo2%2FSgjZcBedOcLj3H1k1%2BlAxj6oX1sJMSAvlVmIcQja%2FpbvantFVdmIMY77fy5s9Fri9J3urxxFwPlIZ3z9Ucr5WmXSwEksU8KlmKtWVl6moV2%2BJQDjNmMgxKzN6Q%2FXfiNVxO6VhdM%2BOluFp54k%2BOiMXxpir0tLZw%2FFYnDA%2Fa996W9xf%2FldlLmk1K9JTt%2BxLzkYlbQ39TjP7zaqAq89NnJtAyi1WLuVTYjG0msGvj3Crf9fzi4JlbcG1FG9zZvM7wAovDYzgUI4eaC5aySelVrUgks6ZySW%2BCh%2Br1JoM0wMgk2Acz5g40kLpFAPm%2FeY6jlj0xTcoVGZQXqsuFKAsN2jMOSx67wGOqUBqbR1jsJ%2BMnEipIwbSMud%2BeVMSgTtEvmS2tBjEOwMwqnzslq3yHpleiUhD7LbR%2F87j9WOSxm54P8qFsRAiT5k2bE2tSfw1vrNj33xlJRm6rY5Zw%2FOf5wOl1FtkYhvA%2FuGSWffWvQM1JWXJYRjkALEej7c5zIVtnkzzvDzLi9VLrrSu6nxkZhOPrkvVLe9dw0U0vWvMIoMFWV%2Fvw9kAQu3VBwZt47g&X-Amz-Signature=6bc813a5b5f4463aab95cc27ab73e814e1e56cf8abff0b14dfc83f6f0daaa5d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHTIE45J%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGHPfWqfpL34OKeL4tCUCrfIeSupqH%2F%2BcngGUxNCY2pqAiEAxsy0K4ovyiq1U%2BxqvNQ%2BEeVgzEdWPWMO1%2B%2BAiftOWx0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGwEHSFC9E76IZl83CrcA19vea0z735xxeffM6e8n%2FM5ca7CMmxHURHIh2zs8I4lZEfsiM5G7F9WjHilRoFSejXvQGqdBWI%2FmZZjTZIXqytswBcAuhS5IuQvthBvoR55iGcAetORZiNwaSyf0xyeSWLIiupvasnndgr0O%2FqA%2FgiCHKWzoifOJKEPM2kuvczROc3F0WXKBskhqjBpJuZxycCfKP1lqK4ojkdeP2%2BnXzNGeMPXz9QAs9Q8Eh4MnVXc%2B%2FdSoFvOpDKPh%2BRTAFJb5eqMzHGBO9%2Fl%2Fq0UNSU5UsVO6kRS7qlTjhON0DeWqjRGMRSliCSmdR2BzBTlcgVX8ZLMfL3In8VSSil5%2FJvP%2F33Wiwkz7U4PEVJ%2F8WOr7DP2iewhGbew6hdQ2Z0a38Lc0jB%2FFQBLD6Smu%2FNRejWL6IAB5plq8%2B3aL2Qvcutuq2Za%2FBNGDq2%2Fr0pSzlL9CQ0F9eWwsvK9%2FFShxwKYXvlKkio2D%2FYI2dlIHYxa7SqlWurzMVxauxLf%2FnqgtZz1ztnS6sCfgi84X%2B%2F3N5l5Yk6hJhQ4g6f1T%2BYzZcgEpijAu4kz8KkYBcqFGO88tFhtOss%2FcX0SZDi5HP5sKjF8MsEB%2FcgRJpYgbnP2vXF25bUH4VXopPUcUki7q1fKOsOdMIey67wGOqUBU8%2BATu1D%2BOCH6KMCbNXkwQ1bnP1jfu7hl%2F4d3n6P2b9Pl4lEPUhyGa%2BRVe0L2dzElY4eTwYNt3jUak8usAsPLAbejrAiaIiNsIxELLszo2qe6WnbvfHaWrkJtW4M%2BnnE%2BVAQoJ3HfLsq2nkPFSsBv%2B5cEqyxnRU8sQtbuPYG6c%2B2suJJQDLSrbV1aM7aMQvZAYVrPo0FNI31hLWhcsSAbP7Uoh67&X-Amz-Signature=5fdcc0771b6b1a4c35a668a3a917762e22d6807eeffc2491ff0f96d617e3a522&X-Amz-SignedHeaders=host&x-id=GetObject)
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