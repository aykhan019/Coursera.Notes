

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDDVNEMM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCrqtltYLnYrwNdaGj0%2FoUlcKaQBbOUhWL4h2lL7KikAQIgF1uQAdIUigTYPncP8bekmmTg%2FMBemOhtWnVwdygTRlAq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNg9zLcb0aL2TApDZSrcAwcyknS6Kf1iU%2F71ul3OAYybZNvZ5ju1Qxss2GCya1X7Y5oQ2sG80Q%2FZ%2BF6GsKNek52sUTk8UbQMWEH39HatfT%2FfsXskV7o8ooMcMLKYojUvQZzNLGWkqx0Uk7iPkYGhM%2F9AM%2BIHauRW1XQLgXzCHPWbKTD3HwclIHcxY7n%2B5Jeto6p%2BjtwVLoOKvxarCH6qQ8cTrfZBNScIcCZLU5PueCxQMap9ETCUrJG7H0MBLyvxfsb1zZJ%2FsDJ83p9yNoaBAmS9vhC1vcFdSRMG2dHIoZZxwAwonPGL4lU3JYvv7wWKdmHLtynJMiucmKZKTqK3kQLMN3XORkfsNT3OFZj65cSPf7iSgEebGrrAefM9wL4%2Fh0m3IdaWCnIPvAG75ZdoBHKjyXJ47wIu9iGgUScCuuUh4p8Ydd3Sg8u3vuKmooQdKuwroi%2FXINaYgIHQeidN275xBucThMrCj06AVGJ5gRy1ySjDydZAQOpAuMipq%2F2phcgKiSfteue6lowPn6A7afN4as34e42DU2PFPgVeCyUFusMrShTFLX4okOnF9xRFY6u8%2FPLEPIXMyC%2FLQBsQ79GrjyRTtSj2nS%2FmqcQgVLq%2BnQRGfe3K8lIQ9%2FcceC%2F%2Fpy%2BRmZslN6cM1sT%2BMPTDkr0GOqUBmKx3ize6FUv5JEfHaiXxoftQQ15AiUkOLgR2vPTwSef8XJKTowSxPIMAh0i7X5idRAlhc9plS4vzFuxF18WZJNUt8KNK%2FoOIC4rvzn2VmwacnhAI%2FWs0LsOtp5fWK4pPA0P9yZOrpOmNq37mRcRNAo9xLWYect%2FeaqaAiAWzW%2BYaTS4Q8AIeM18qUPeRbJYb5PHBY0hn2Xpa85nwocmH%2BHiFX7mx&X-Amz-Signature=81e83ac8a6b716856244226f813a8c863ef3c5ae08224af0e9571650bf3d205e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDDVNEMM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCrqtltYLnYrwNdaGj0%2FoUlcKaQBbOUhWL4h2lL7KikAQIgF1uQAdIUigTYPncP8bekmmTg%2FMBemOhtWnVwdygTRlAq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNg9zLcb0aL2TApDZSrcAwcyknS6Kf1iU%2F71ul3OAYybZNvZ5ju1Qxss2GCya1X7Y5oQ2sG80Q%2FZ%2BF6GsKNek52sUTk8UbQMWEH39HatfT%2FfsXskV7o8ooMcMLKYojUvQZzNLGWkqx0Uk7iPkYGhM%2F9AM%2BIHauRW1XQLgXzCHPWbKTD3HwclIHcxY7n%2B5Jeto6p%2BjtwVLoOKvxarCH6qQ8cTrfZBNScIcCZLU5PueCxQMap9ETCUrJG7H0MBLyvxfsb1zZJ%2FsDJ83p9yNoaBAmS9vhC1vcFdSRMG2dHIoZZxwAwonPGL4lU3JYvv7wWKdmHLtynJMiucmKZKTqK3kQLMN3XORkfsNT3OFZj65cSPf7iSgEebGrrAefM9wL4%2Fh0m3IdaWCnIPvAG75ZdoBHKjyXJ47wIu9iGgUScCuuUh4p8Ydd3Sg8u3vuKmooQdKuwroi%2FXINaYgIHQeidN275xBucThMrCj06AVGJ5gRy1ySjDydZAQOpAuMipq%2F2phcgKiSfteue6lowPn6A7afN4as34e42DU2PFPgVeCyUFusMrShTFLX4okOnF9xRFY6u8%2FPLEPIXMyC%2FLQBsQ79GrjyRTtSj2nS%2FmqcQgVLq%2BnQRGfe3K8lIQ9%2FcceC%2F%2Fpy%2BRmZslN6cM1sT%2BMPTDkr0GOqUBmKx3ize6FUv5JEfHaiXxoftQQ15AiUkOLgR2vPTwSef8XJKTowSxPIMAh0i7X5idRAlhc9plS4vzFuxF18WZJNUt8KNK%2FoOIC4rvzn2VmwacnhAI%2FWs0LsOtp5fWK4pPA0P9yZOrpOmNq37mRcRNAo9xLWYect%2FeaqaAiAWzW%2BYaTS4Q8AIeM18qUPeRbJYb5PHBY0hn2Xpa85nwocmH%2BHiFX7mx&X-Amz-Signature=5ca179d64ffb1f697c62222016cff309b6a60aa36cded84792e57c8e154ea760&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDDVNEMM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCrqtltYLnYrwNdaGj0%2FoUlcKaQBbOUhWL4h2lL7KikAQIgF1uQAdIUigTYPncP8bekmmTg%2FMBemOhtWnVwdygTRlAq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNg9zLcb0aL2TApDZSrcAwcyknS6Kf1iU%2F71ul3OAYybZNvZ5ju1Qxss2GCya1X7Y5oQ2sG80Q%2FZ%2BF6GsKNek52sUTk8UbQMWEH39HatfT%2FfsXskV7o8ooMcMLKYojUvQZzNLGWkqx0Uk7iPkYGhM%2F9AM%2BIHauRW1XQLgXzCHPWbKTD3HwclIHcxY7n%2B5Jeto6p%2BjtwVLoOKvxarCH6qQ8cTrfZBNScIcCZLU5PueCxQMap9ETCUrJG7H0MBLyvxfsb1zZJ%2FsDJ83p9yNoaBAmS9vhC1vcFdSRMG2dHIoZZxwAwonPGL4lU3JYvv7wWKdmHLtynJMiucmKZKTqK3kQLMN3XORkfsNT3OFZj65cSPf7iSgEebGrrAefM9wL4%2Fh0m3IdaWCnIPvAG75ZdoBHKjyXJ47wIu9iGgUScCuuUh4p8Ydd3Sg8u3vuKmooQdKuwroi%2FXINaYgIHQeidN275xBucThMrCj06AVGJ5gRy1ySjDydZAQOpAuMipq%2F2phcgKiSfteue6lowPn6A7afN4as34e42DU2PFPgVeCyUFusMrShTFLX4okOnF9xRFY6u8%2FPLEPIXMyC%2FLQBsQ79GrjyRTtSj2nS%2FmqcQgVLq%2BnQRGfe3K8lIQ9%2FcceC%2F%2Fpy%2BRmZslN6cM1sT%2BMPTDkr0GOqUBmKx3ize6FUv5JEfHaiXxoftQQ15AiUkOLgR2vPTwSef8XJKTowSxPIMAh0i7X5idRAlhc9plS4vzFuxF18WZJNUt8KNK%2FoOIC4rvzn2VmwacnhAI%2FWs0LsOtp5fWK4pPA0P9yZOrpOmNq37mRcRNAo9xLWYect%2FeaqaAiAWzW%2BYaTS4Q8AIeM18qUPeRbJYb5PHBY0hn2Xpa85nwocmH%2BHiFX7mx&X-Amz-Signature=2c1f8ea3c408a43792d07d757f0a244aee4ace7147d3bd02b02ee1a8e187c944&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OJJ5CSE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQDOMAkgK19kwsO7Q8lV81cP1bQsd7pOxEmGpK6uYI1u7AIhAOWMxbvwcnCx9Fx78n6%2FFCsSQ%2FiRAC7eXGKsq2RYolq2Kv8DCF0QABoMNjM3NDIzMTgzODA1IgzsfKVj6Oknzed3S2sq3AMIZPjQ1KtshNnQAr8A5Vbc0x%2FkXZWHqLmngBLSKWGOtJbAo7M3%2F0%2BXkXcfKwDSGQh2VuJJSkiZYeNNek%2Blv4xo7llNwhcqZdWJzyhet6UsyreWR8ZtD%2Bhz49cbppydvv1zdAHguNsVubmD98gE5fNppvcqTakOIYNITv0FzXqKNRe1GJUC4Il8CmrOOjtSNqt4sOBMnc6pXUWBlEQNQOAN2Y00ZSldi2%2FYu0R6W4tT0De3EnpfFkYEMOAbBTF41sVX4wII%2BlZr0Ez%2BTrQzPIJ7csjMpQCcyGRAttYLKgWz6nj8C7IzPJTyCez%2BuOHCFFlS5kC1wOkO1m6NjHKY21J%2Bzh%2FI8KPG9sfOuLp4CCk1UwQh%2FcKqaB4EaFFGcnXZPw841NxJfRtN8PilbniY%2B5fysLSmcXDt%2Bwqy8paDb16tLuK1M2D481h3DqiiKod0e9XzgTxfON2VL2R%2FLDZA0sEL8b26k04qE3db1ktla%2FJjQUMBCN34srYc%2FMs7mQiqLYxRt0sYSob%2BMxnYOfJNmHkjmYCYFURkWBwfXR5ATLk%2BOVcCfWjs1M31%2FE31EqM3DZYhlhDwUPa8w1a9Q1BuS%2BSWC3%2F%2FIPr%2BQwx3bXXtrcpE7a%2FJpPophfnn6BKAfzDOw5K9BjqkAerN8zAXiFsEjRfQLOU7uQ7lpH5oyhS%2Fd%2FZztFtCZ9FHNQBzNJ1nMQdPfkzp%2BjjwenHb73V8eFjcoJ0uCtMw0GRt7JMIkD3%2BOoBZz4yhUfh9r%2BIuCsD6o8WF0KdNMnDEn0%2BR9d2PUTLe767qoF26aQDtPwgq7z2OaaJ4wAXPujT1Lgqd444XB9GDtjspnZB1Q2rHaJrzizOKr4ryUfGFOZZKt6Uo&X-Amz-Signature=d7513ce697aa12ef280592d6f071ed6a7092e8ea6d414c5b562361cb101de934&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OJJ5CSE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQDOMAkgK19kwsO7Q8lV81cP1bQsd7pOxEmGpK6uYI1u7AIhAOWMxbvwcnCx9Fx78n6%2FFCsSQ%2FiRAC7eXGKsq2RYolq2Kv8DCF0QABoMNjM3NDIzMTgzODA1IgzsfKVj6Oknzed3S2sq3AMIZPjQ1KtshNnQAr8A5Vbc0x%2FkXZWHqLmngBLSKWGOtJbAo7M3%2F0%2BXkXcfKwDSGQh2VuJJSkiZYeNNek%2Blv4xo7llNwhcqZdWJzyhet6UsyreWR8ZtD%2Bhz49cbppydvv1zdAHguNsVubmD98gE5fNppvcqTakOIYNITv0FzXqKNRe1GJUC4Il8CmrOOjtSNqt4sOBMnc6pXUWBlEQNQOAN2Y00ZSldi2%2FYu0R6W4tT0De3EnpfFkYEMOAbBTF41sVX4wII%2BlZr0Ez%2BTrQzPIJ7csjMpQCcyGRAttYLKgWz6nj8C7IzPJTyCez%2BuOHCFFlS5kC1wOkO1m6NjHKY21J%2Bzh%2FI8KPG9sfOuLp4CCk1UwQh%2FcKqaB4EaFFGcnXZPw841NxJfRtN8PilbniY%2B5fysLSmcXDt%2Bwqy8paDb16tLuK1M2D481h3DqiiKod0e9XzgTxfON2VL2R%2FLDZA0sEL8b26k04qE3db1ktla%2FJjQUMBCN34srYc%2FMs7mQiqLYxRt0sYSob%2BMxnYOfJNmHkjmYCYFURkWBwfXR5ATLk%2BOVcCfWjs1M31%2FE31EqM3DZYhlhDwUPa8w1a9Q1BuS%2BSWC3%2F%2FIPr%2BQwx3bXXtrcpE7a%2FJpPophfnn6BKAfzDOw5K9BjqkAerN8zAXiFsEjRfQLOU7uQ7lpH5oyhS%2Fd%2FZztFtCZ9FHNQBzNJ1nMQdPfkzp%2BjjwenHb73V8eFjcoJ0uCtMw0GRt7JMIkD3%2BOoBZz4yhUfh9r%2BIuCsD6o8WF0KdNMnDEn0%2BR9d2PUTLe767qoF26aQDtPwgq7z2OaaJ4wAXPujT1Lgqd444XB9GDtjspnZB1Q2rHaJrzizOKr4ryUfGFOZZKt6Uo&X-Amz-Signature=e6f94048d567751164e522f8cf4b5dad1be4b950b6a292b0c9bb8fdc2c6632b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDDVNEMM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCrqtltYLnYrwNdaGj0%2FoUlcKaQBbOUhWL4h2lL7KikAQIgF1uQAdIUigTYPncP8bekmmTg%2FMBemOhtWnVwdygTRlAq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNg9zLcb0aL2TApDZSrcAwcyknS6Kf1iU%2F71ul3OAYybZNvZ5ju1Qxss2GCya1X7Y5oQ2sG80Q%2FZ%2BF6GsKNek52sUTk8UbQMWEH39HatfT%2FfsXskV7o8ooMcMLKYojUvQZzNLGWkqx0Uk7iPkYGhM%2F9AM%2BIHauRW1XQLgXzCHPWbKTD3HwclIHcxY7n%2B5Jeto6p%2BjtwVLoOKvxarCH6qQ8cTrfZBNScIcCZLU5PueCxQMap9ETCUrJG7H0MBLyvxfsb1zZJ%2FsDJ83p9yNoaBAmS9vhC1vcFdSRMG2dHIoZZxwAwonPGL4lU3JYvv7wWKdmHLtynJMiucmKZKTqK3kQLMN3XORkfsNT3OFZj65cSPf7iSgEebGrrAefM9wL4%2Fh0m3IdaWCnIPvAG75ZdoBHKjyXJ47wIu9iGgUScCuuUh4p8Ydd3Sg8u3vuKmooQdKuwroi%2FXINaYgIHQeidN275xBucThMrCj06AVGJ5gRy1ySjDydZAQOpAuMipq%2F2phcgKiSfteue6lowPn6A7afN4as34e42DU2PFPgVeCyUFusMrShTFLX4okOnF9xRFY6u8%2FPLEPIXMyC%2FLQBsQ79GrjyRTtSj2nS%2FmqcQgVLq%2BnQRGfe3K8lIQ9%2FcceC%2F%2Fpy%2BRmZslN6cM1sT%2BMPTDkr0GOqUBmKx3ize6FUv5JEfHaiXxoftQQ15AiUkOLgR2vPTwSef8XJKTowSxPIMAh0i7X5idRAlhc9plS4vzFuxF18WZJNUt8KNK%2FoOIC4rvzn2VmwacnhAI%2FWs0LsOtp5fWK4pPA0P9yZOrpOmNq37mRcRNAo9xLWYect%2FeaqaAiAWzW%2BYaTS4Q8AIeM18qUPeRbJYb5PHBY0hn2Xpa85nwocmH%2BHiFX7mx&X-Amz-Signature=604e78c76478f5d78c904eb9f3c35b735c6ec28af23ab16d60f7c7a8d5b85d44&X-Amz-SignedHeaders=host&x-id=GetObject)
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