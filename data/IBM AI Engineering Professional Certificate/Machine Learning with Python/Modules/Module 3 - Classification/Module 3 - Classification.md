

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRATHSVF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDMsb6o%2F3SN1g0jnXeng74g25WPY2OP%2BPV%2FGlv%2B0RDhEgIhANZhAiWAgo7TmboyhV1YFHCJVODrPTuIukXdxXXWTywVKv8DCC8QABoMNjM3NDIzMTgzODA1IgxFB4JA2RjCPxNL%2FLYq3AN4k68ijthTjP6d43koOmyzlJKes9vV5XzH60g1ggSR7O%2FiXkotmUKiY2iHYCHtkmpjjWltRPFOJelvq5zoNu6cLAlswlsdAp1sDzO8rTT%2FtQ9FxbWdfMSVOeJVYdoSWa4N%2BM8DtZAarfo2lZhVtvatFfJqruw0H3uXuNuA8AaZHNu%2FcLQvCsl9eqRqdLXA7Dwfxbqs1POrAm%2BC4KKfxdtXQnSwWb1wNOnSoAqSg2iSKtyZNwBVG%2Funiiz%2BiLKzc%2F7HLJmFpKJGkD8ufTHX2lRo%2FGOmnoMsYaJi4EcfnX%2BEyt%2Fw0pH0uIsTv3pIbSaxP4RAohcWa8xcULfQTakcAZnE2c7NaozTI2%2FR3JgzytQxsAxe19DBLSRquin6tk2a0FYTcYlTz0oM7twN4JNXBp93CuPYy%2BWfz1s%2FRYz9wjEV9liy9PhneXo3ab0elXlh4i9LolhAudZNDqWga2Gtx9aWblyexEd8yEHA7jq0dZnnr5YGWLZLjv3iuWpJspPVLN1g6ZVHyiVbuKeZDYnWcIipkqseJNFlwfrixs4eyTp8PemW2ZH01VhEYRexXwSvM2ctcCgp4bAr0YGRUy02fSuGJKm772%2BM21LVpS%2BhcyHRiyu1CvfUb6rsUeMDqjDRvIi9BjqkAahS70fIPXkglHaf4ABbUXAoRbc4FWqW1o4V5pVboQYfKZGQB9KxdfmoHk%2FxMG1cNJgmPFKk7qOVHzG3R14K3Tr6rftGpEawNhMEbRY0YVKROaAxca57rSMeN0R7OpmFT%2FOjSkdzta6CfJ5uWJvNLfNzsCv%2B1%2FryFMNinDXLP8QLvBDUShkYPD%2BXxu8SQcBu%2BdLDwMJaK6HR%2FPB%2BeREioAqNoWkw&X-Amz-Signature=a11cedccf56865ec01a2844e97e8a32cb6b1ff36b5c6eb035af05e8624050b4f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRATHSVF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDMsb6o%2F3SN1g0jnXeng74g25WPY2OP%2BPV%2FGlv%2B0RDhEgIhANZhAiWAgo7TmboyhV1YFHCJVODrPTuIukXdxXXWTywVKv8DCC8QABoMNjM3NDIzMTgzODA1IgxFB4JA2RjCPxNL%2FLYq3AN4k68ijthTjP6d43koOmyzlJKes9vV5XzH60g1ggSR7O%2FiXkotmUKiY2iHYCHtkmpjjWltRPFOJelvq5zoNu6cLAlswlsdAp1sDzO8rTT%2FtQ9FxbWdfMSVOeJVYdoSWa4N%2BM8DtZAarfo2lZhVtvatFfJqruw0H3uXuNuA8AaZHNu%2FcLQvCsl9eqRqdLXA7Dwfxbqs1POrAm%2BC4KKfxdtXQnSwWb1wNOnSoAqSg2iSKtyZNwBVG%2Funiiz%2BiLKzc%2F7HLJmFpKJGkD8ufTHX2lRo%2FGOmnoMsYaJi4EcfnX%2BEyt%2Fw0pH0uIsTv3pIbSaxP4RAohcWa8xcULfQTakcAZnE2c7NaozTI2%2FR3JgzytQxsAxe19DBLSRquin6tk2a0FYTcYlTz0oM7twN4JNXBp93CuPYy%2BWfz1s%2FRYz9wjEV9liy9PhneXo3ab0elXlh4i9LolhAudZNDqWga2Gtx9aWblyexEd8yEHA7jq0dZnnr5YGWLZLjv3iuWpJspPVLN1g6ZVHyiVbuKeZDYnWcIipkqseJNFlwfrixs4eyTp8PemW2ZH01VhEYRexXwSvM2ctcCgp4bAr0YGRUy02fSuGJKm772%2BM21LVpS%2BhcyHRiyu1CvfUb6rsUeMDqjDRvIi9BjqkAahS70fIPXkglHaf4ABbUXAoRbc4FWqW1o4V5pVboQYfKZGQB9KxdfmoHk%2FxMG1cNJgmPFKk7qOVHzG3R14K3Tr6rftGpEawNhMEbRY0YVKROaAxca57rSMeN0R7OpmFT%2FOjSkdzta6CfJ5uWJvNLfNzsCv%2B1%2FryFMNinDXLP8QLvBDUShkYPD%2BXxu8SQcBu%2BdLDwMJaK6HR%2FPB%2BeREioAqNoWkw&X-Amz-Signature=0a59a534625a8f1b3745cbd438ede45da56aeb652aa94af28cc2ba0b376d3a74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRATHSVF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDMsb6o%2F3SN1g0jnXeng74g25WPY2OP%2BPV%2FGlv%2B0RDhEgIhANZhAiWAgo7TmboyhV1YFHCJVODrPTuIukXdxXXWTywVKv8DCC8QABoMNjM3NDIzMTgzODA1IgxFB4JA2RjCPxNL%2FLYq3AN4k68ijthTjP6d43koOmyzlJKes9vV5XzH60g1ggSR7O%2FiXkotmUKiY2iHYCHtkmpjjWltRPFOJelvq5zoNu6cLAlswlsdAp1sDzO8rTT%2FtQ9FxbWdfMSVOeJVYdoSWa4N%2BM8DtZAarfo2lZhVtvatFfJqruw0H3uXuNuA8AaZHNu%2FcLQvCsl9eqRqdLXA7Dwfxbqs1POrAm%2BC4KKfxdtXQnSwWb1wNOnSoAqSg2iSKtyZNwBVG%2Funiiz%2BiLKzc%2F7HLJmFpKJGkD8ufTHX2lRo%2FGOmnoMsYaJi4EcfnX%2BEyt%2Fw0pH0uIsTv3pIbSaxP4RAohcWa8xcULfQTakcAZnE2c7NaozTI2%2FR3JgzytQxsAxe19DBLSRquin6tk2a0FYTcYlTz0oM7twN4JNXBp93CuPYy%2BWfz1s%2FRYz9wjEV9liy9PhneXo3ab0elXlh4i9LolhAudZNDqWga2Gtx9aWblyexEd8yEHA7jq0dZnnr5YGWLZLjv3iuWpJspPVLN1g6ZVHyiVbuKeZDYnWcIipkqseJNFlwfrixs4eyTp8PemW2ZH01VhEYRexXwSvM2ctcCgp4bAr0YGRUy02fSuGJKm772%2BM21LVpS%2BhcyHRiyu1CvfUb6rsUeMDqjDRvIi9BjqkAahS70fIPXkglHaf4ABbUXAoRbc4FWqW1o4V5pVboQYfKZGQB9KxdfmoHk%2FxMG1cNJgmPFKk7qOVHzG3R14K3Tr6rftGpEawNhMEbRY0YVKROaAxca57rSMeN0R7OpmFT%2FOjSkdzta6CfJ5uWJvNLfNzsCv%2B1%2FryFMNinDXLP8QLvBDUShkYPD%2BXxu8SQcBu%2BdLDwMJaK6HR%2FPB%2BeREioAqNoWkw&X-Amz-Signature=041af2f28162cb0d83e59b629d5e7bf252a0d4a167b4e34c4b04053ce19b38b4&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGTA3FIM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIB6q%2FYeHnt374IBiahG%2BTWVN6ysrEX2XzNk4UeypbUKdAiBwZ0vqswM%2BTkn5UY90snx0hiKSKqeYt3GUTuddqEHLyir%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMhr6LhNO6U0XfZxDhKtwD1x0rS2x%2FzCb0O3smnECsa3WAEE7Ztoi9LdFnneLVPT5pg6Ie%2B7rHt%2FiQJIyGQavpeyQqEjJoYgSdbEkQJw0e19jc393w7k%2FGA1dpeSoxqpMAmoD61VLF6qdV%2B5hUpn8tfA3Ds8jHvxM23UlrcAm9b1v2NaHWThHLMKimon9nHplngfx%2BMzQyGIkEGvuQmIeL9aG7PKFEbrm9hY5qZnPd1Gm88jRoQSsVcG4jhAN5utr1ZCxmFdIOtuxDf711JzWeISaVbEQ71oP6DXt6u%2FENe%2Bx9pBURwW3c5cRbC6lACAoo1Lt77QqmyrWdnCz5rm1eBgGGJVVGh1CBs%2Bibwd4FE7EqZsTC5NVdGn1Pan50cfOGttzWtc%2FTMRHGeKs1rUWHKZb159UI%2BhhWKpuBFbu6GBizLc5R%2BQCnXbP%2FxbiH6kZO4NqJnBNayz5WLymARnaXJEp4wUN%2BNjkAl96RSEhIceYaCWGj4T03Pp8miIw59IU4lEYbiaLlbU1U2o4bGBupMmaWLXF0aRQ6wIk2saPjX6Pd0QoG3XHluneDHvZkQMyTg%2BD%2BvDYD%2FaP1c8jvgKy%2BjqLjtdUlZIjqVqFHG%2B4tlG9cg9h3Ki78sJl%2BT05crCran%2BFEozODqTFmrrcwyryIvQY6pgGDBXJ5ZDEJHOP8ItiVIEPTPv5L2i2DZwW6Ht4NA9sl1MmxSaMl6nnv1%2FVo09Q%2BsfCrVhyUi%2B8D2uIjuU%2F4fKs7Gn2yfIEQO5jB4MwTNKO8GgpGZ%2BqPVpP%2BZSwSMzY7cq1eqzPlQGXFT2hlhkUhNiYaFKtUDx%2FsSIIJ89rfIMXbbwRa%2F1gdOS9Umci05l6wog%2FsFiYniohIuVp1GI1VWC8Tet8ylKW0&X-Amz-Signature=de2e76a142c805b7e7b443e331a43b647c7a97bc9d391f9b2d14ab04cb4b4b7f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGTA3FIM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIB6q%2FYeHnt374IBiahG%2BTWVN6ysrEX2XzNk4UeypbUKdAiBwZ0vqswM%2BTkn5UY90snx0hiKSKqeYt3GUTuddqEHLyir%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMhr6LhNO6U0XfZxDhKtwD1x0rS2x%2FzCb0O3smnECsa3WAEE7Ztoi9LdFnneLVPT5pg6Ie%2B7rHt%2FiQJIyGQavpeyQqEjJoYgSdbEkQJw0e19jc393w7k%2FGA1dpeSoxqpMAmoD61VLF6qdV%2B5hUpn8tfA3Ds8jHvxM23UlrcAm9b1v2NaHWThHLMKimon9nHplngfx%2BMzQyGIkEGvuQmIeL9aG7PKFEbrm9hY5qZnPd1Gm88jRoQSsVcG4jhAN5utr1ZCxmFdIOtuxDf711JzWeISaVbEQ71oP6DXt6u%2FENe%2Bx9pBURwW3c5cRbC6lACAoo1Lt77QqmyrWdnCz5rm1eBgGGJVVGh1CBs%2Bibwd4FE7EqZsTC5NVdGn1Pan50cfOGttzWtc%2FTMRHGeKs1rUWHKZb159UI%2BhhWKpuBFbu6GBizLc5R%2BQCnXbP%2FxbiH6kZO4NqJnBNayz5WLymARnaXJEp4wUN%2BNjkAl96RSEhIceYaCWGj4T03Pp8miIw59IU4lEYbiaLlbU1U2o4bGBupMmaWLXF0aRQ6wIk2saPjX6Pd0QoG3XHluneDHvZkQMyTg%2BD%2BvDYD%2FaP1c8jvgKy%2BjqLjtdUlZIjqVqFHG%2B4tlG9cg9h3Ki78sJl%2BT05crCran%2BFEozODqTFmrrcwyryIvQY6pgGDBXJ5ZDEJHOP8ItiVIEPTPv5L2i2DZwW6Ht4NA9sl1MmxSaMl6nnv1%2FVo09Q%2BsfCrVhyUi%2B8D2uIjuU%2F4fKs7Gn2yfIEQO5jB4MwTNKO8GgpGZ%2BqPVpP%2BZSwSMzY7cq1eqzPlQGXFT2hlhkUhNiYaFKtUDx%2FsSIIJ89rfIMXbbwRa%2F1gdOS9Umci05l6wog%2FsFiYniohIuVp1GI1VWC8Tet8ylKW0&X-Amz-Signature=7567d0b5a20ae7a635bb5a3ca65346ee51578bc9b4e6289392d6921532dbad41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRATHSVF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDMsb6o%2F3SN1g0jnXeng74g25WPY2OP%2BPV%2FGlv%2B0RDhEgIhANZhAiWAgo7TmboyhV1YFHCJVODrPTuIukXdxXXWTywVKv8DCC8QABoMNjM3NDIzMTgzODA1IgxFB4JA2RjCPxNL%2FLYq3AN4k68ijthTjP6d43koOmyzlJKes9vV5XzH60g1ggSR7O%2FiXkotmUKiY2iHYCHtkmpjjWltRPFOJelvq5zoNu6cLAlswlsdAp1sDzO8rTT%2FtQ9FxbWdfMSVOeJVYdoSWa4N%2BM8DtZAarfo2lZhVtvatFfJqruw0H3uXuNuA8AaZHNu%2FcLQvCsl9eqRqdLXA7Dwfxbqs1POrAm%2BC4KKfxdtXQnSwWb1wNOnSoAqSg2iSKtyZNwBVG%2Funiiz%2BiLKzc%2F7HLJmFpKJGkD8ufTHX2lRo%2FGOmnoMsYaJi4EcfnX%2BEyt%2Fw0pH0uIsTv3pIbSaxP4RAohcWa8xcULfQTakcAZnE2c7NaozTI2%2FR3JgzytQxsAxe19DBLSRquin6tk2a0FYTcYlTz0oM7twN4JNXBp93CuPYy%2BWfz1s%2FRYz9wjEV9liy9PhneXo3ab0elXlh4i9LolhAudZNDqWga2Gtx9aWblyexEd8yEHA7jq0dZnnr5YGWLZLjv3iuWpJspPVLN1g6ZVHyiVbuKeZDYnWcIipkqseJNFlwfrixs4eyTp8PemW2ZH01VhEYRexXwSvM2ctcCgp4bAr0YGRUy02fSuGJKm772%2BM21LVpS%2BhcyHRiyu1CvfUb6rsUeMDqjDRvIi9BjqkAahS70fIPXkglHaf4ABbUXAoRbc4FWqW1o4V5pVboQYfKZGQB9KxdfmoHk%2FxMG1cNJgmPFKk7qOVHzG3R14K3Tr6rftGpEawNhMEbRY0YVKROaAxca57rSMeN0R7OpmFT%2FOjSkdzta6CfJ5uWJvNLfNzsCv%2B1%2FryFMNinDXLP8QLvBDUShkYPD%2BXxu8SQcBu%2BdLDwMJaK6HR%2FPB%2BeREioAqNoWkw&X-Amz-Signature=fa230c4cef1c102d866d15aff855abd3b444688d8b9fd9c854575b8f363292c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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