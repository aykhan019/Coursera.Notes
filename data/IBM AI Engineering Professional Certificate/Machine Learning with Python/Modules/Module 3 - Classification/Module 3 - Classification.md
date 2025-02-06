

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USXX3TDF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIG3D12Ua4%2BgFkTuoxJY1%2FIw0h7TdhEV1d3T1uF0TOR%2BbAiACxskdEbznDst4ywSx8axr1OtsGyE1y9xJwljm1Q371Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMKyPiwMr1rHcrmYEXKtwDOzhWFsViExTI6m60z6q5I%2BFXNATQI%2BEluAiX9bu9j725GwQkweJZijQrW6O8PHG6NXshjfUKkmo071VVm6q8RKdh7R0ZAfH2SmiFqxXfKSOmsGjxFqyw%2BQ9sw6A1%2Bqifl4FHjcMRtUibxq3QZM8wjzRTgTJYu5xBcKBhcU0q63YntgiaqhkMbuQe5mJCmhn%2FcqsQQP1hklzQjtw%2FuPLDZVeDHZTCPXAsgwKCVQsKfICPZVyiSEHjSCPznEhvimuyc4L4iiYjYyHdPokpHqcDsea7cMpUXt02G2e0FXNIAX4JB5DRkIL5M4YrZz0cuSAYYqY0we7SXlf%2B135xA7d82rKYaBWqpD3r%2BfspM2DMVI8BfQyW0XubD4Ixx%2BkDikDnNCJa2bvVT4rKyR2BsybdI5u53tKPe%2B%2BrxK1b4gfv78CVIYivmHf0w1fVRg1oSyG8zpW0EXgC2zhfE8SqBn%2BBlW7bsx1yxqlYkSZsVgEU41sh6fEV%2FQFJys8L44VtyzywolGgZ%2FJ%2BDkE3vkuKvfgO86MfAvxKNrp6mfyRJBFCWKrAnrPyX9gyleTlg1yIZSA9173DvSPwyyNi2OQk6cmdCZ291fTEC8VLV5y4VPwmukx1dnhoqhSkj4TNnOYw2PuTvQY6pgEK84T8TXdgZF2DLDs8tyd8birqgyvQ27fSSmlK1IysHEHJysGQ10uzuV%2FfvBN%2BC1Bmez1nugGKDzxwQAtTdxye91IAcE%2FUfRJ92zOFO269IxfpbGozQgAb9c9Pjw2adpziqH87ouz2pVb2C8REPyNzKG9SchDfZAa9WB2HdNU2RN4Kc85x0%2FapjQn16EL4BGFUFuLOmNHNqQIwD0s4WJlSDde%2FnZ%2F6&X-Amz-Signature=5c8cfe261a4464f95ee852e4354c743a2156d9c72bee24bdb06e8fcc26cc0f9a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USXX3TDF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIG3D12Ua4%2BgFkTuoxJY1%2FIw0h7TdhEV1d3T1uF0TOR%2BbAiACxskdEbznDst4ywSx8axr1OtsGyE1y9xJwljm1Q371Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMKyPiwMr1rHcrmYEXKtwDOzhWFsViExTI6m60z6q5I%2BFXNATQI%2BEluAiX9bu9j725GwQkweJZijQrW6O8PHG6NXshjfUKkmo071VVm6q8RKdh7R0ZAfH2SmiFqxXfKSOmsGjxFqyw%2BQ9sw6A1%2Bqifl4FHjcMRtUibxq3QZM8wjzRTgTJYu5xBcKBhcU0q63YntgiaqhkMbuQe5mJCmhn%2FcqsQQP1hklzQjtw%2FuPLDZVeDHZTCPXAsgwKCVQsKfICPZVyiSEHjSCPznEhvimuyc4L4iiYjYyHdPokpHqcDsea7cMpUXt02G2e0FXNIAX4JB5DRkIL5M4YrZz0cuSAYYqY0we7SXlf%2B135xA7d82rKYaBWqpD3r%2BfspM2DMVI8BfQyW0XubD4Ixx%2BkDikDnNCJa2bvVT4rKyR2BsybdI5u53tKPe%2B%2BrxK1b4gfv78CVIYivmHf0w1fVRg1oSyG8zpW0EXgC2zhfE8SqBn%2BBlW7bsx1yxqlYkSZsVgEU41sh6fEV%2FQFJys8L44VtyzywolGgZ%2FJ%2BDkE3vkuKvfgO86MfAvxKNrp6mfyRJBFCWKrAnrPyX9gyleTlg1yIZSA9173DvSPwyyNi2OQk6cmdCZ291fTEC8VLV5y4VPwmukx1dnhoqhSkj4TNnOYw2PuTvQY6pgEK84T8TXdgZF2DLDs8tyd8birqgyvQ27fSSmlK1IysHEHJysGQ10uzuV%2FfvBN%2BC1Bmez1nugGKDzxwQAtTdxye91IAcE%2FUfRJ92zOFO269IxfpbGozQgAb9c9Pjw2adpziqH87ouz2pVb2C8REPyNzKG9SchDfZAa9WB2HdNU2RN4Kc85x0%2FapjQn16EL4BGFUFuLOmNHNqQIwD0s4WJlSDde%2FnZ%2F6&X-Amz-Signature=1ca74ca73e4958e40a6d8021b4c1d161ac91eefdbf9390082665c8fec4d901d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USXX3TDF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIG3D12Ua4%2BgFkTuoxJY1%2FIw0h7TdhEV1d3T1uF0TOR%2BbAiACxskdEbznDst4ywSx8axr1OtsGyE1y9xJwljm1Q371Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMKyPiwMr1rHcrmYEXKtwDOzhWFsViExTI6m60z6q5I%2BFXNATQI%2BEluAiX9bu9j725GwQkweJZijQrW6O8PHG6NXshjfUKkmo071VVm6q8RKdh7R0ZAfH2SmiFqxXfKSOmsGjxFqyw%2BQ9sw6A1%2Bqifl4FHjcMRtUibxq3QZM8wjzRTgTJYu5xBcKBhcU0q63YntgiaqhkMbuQe5mJCmhn%2FcqsQQP1hklzQjtw%2FuPLDZVeDHZTCPXAsgwKCVQsKfICPZVyiSEHjSCPznEhvimuyc4L4iiYjYyHdPokpHqcDsea7cMpUXt02G2e0FXNIAX4JB5DRkIL5M4YrZz0cuSAYYqY0we7SXlf%2B135xA7d82rKYaBWqpD3r%2BfspM2DMVI8BfQyW0XubD4Ixx%2BkDikDnNCJa2bvVT4rKyR2BsybdI5u53tKPe%2B%2BrxK1b4gfv78CVIYivmHf0w1fVRg1oSyG8zpW0EXgC2zhfE8SqBn%2BBlW7bsx1yxqlYkSZsVgEU41sh6fEV%2FQFJys8L44VtyzywolGgZ%2FJ%2BDkE3vkuKvfgO86MfAvxKNrp6mfyRJBFCWKrAnrPyX9gyleTlg1yIZSA9173DvSPwyyNi2OQk6cmdCZ291fTEC8VLV5y4VPwmukx1dnhoqhSkj4TNnOYw2PuTvQY6pgEK84T8TXdgZF2DLDs8tyd8birqgyvQ27fSSmlK1IysHEHJysGQ10uzuV%2FfvBN%2BC1Bmez1nugGKDzxwQAtTdxye91IAcE%2FUfRJ92zOFO269IxfpbGozQgAb9c9Pjw2adpziqH87ouz2pVb2C8REPyNzKG9SchDfZAa9WB2HdNU2RN4Kc85x0%2FapjQn16EL4BGFUFuLOmNHNqQIwD0s4WJlSDde%2FnZ%2F6&X-Amz-Signature=0500163ca82c0e1f47ecb6e9fc9650399a630838495fcdc1835cbe919436cace&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KFQJSKD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIE5yPW1NUX77%2BSzNUr%2BHmYhXN1VStON2OZP0tN7itdhsAiBEWK54qo00ZYnyajTOUil1JCvYlQfzl1DVFAec79kmmSr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMJGUxM1XxmTNunhXeKtwDQpeUPuFOduGc1aTGe0ULGnQEbEmFllSD8pUrLvGTNdTgOgE0fI4yoZD%2FspdNAUiR%2By0dH7wIqZmHI4StP0YjKJY9RYiChFSL9zvtLiKosTlRvkyt%2FY7O0dUBTG4AIAWQVDFIPWbniTLKdZ7k4PkVvksIQFt2gSPqpteN45HDhuqdtaoW4ZYhibACn13Q1SZz%2F728IDe%2Fg2lg%2FzkLpR4Yjd19Y5AKVg4hbFwK8Z3d0sWkmsDqkqZyKD2EcFiKuvtOYRavg8GQl3IGwfuRGjhlTyDeRKGr83MX0U0uZs4KJAuemeH2ItHky7dOJTE97XqpK%2FkQ3xOK1kh6QC3vAWO4B2l6ZGpuGrdHSPo6a9J%2FeGN4wK%2FDHHnLqaj9jSvaoy8GvIK23P%2FaLlIVNnIFYbvgsOd37n0DlpAx%2Bag5OXdWaPk0OFwvDmWEf8QxLkYQ0BSNFVnzn3%2FAFLUKMZDkU7A%2By3CEnWx8P42yFnBlGX1EzuKsjTYFfJKxlKKmhrtSF4y4DSPMvtchdlGr65aVUpiGUDzNu47ClEbUSvdUUp0N%2Fn3yjl9UR8U8rK4v6id48C%2FtYGoP8LSwIvLKZceOz4ghN3WbidQ5MDj6Q5coTUH7Zj6ytup1%2FGwUFVAt1gww0PuTvQY6pgGq6T0L2N7KonRoaLgE2VNyhxUsMhzDkBg%2B410FXQpRytf4wplgmQAwCItY7g2TdcB3UAeTCnSoRyJ7hNTvSru7Cggc3p5pGY5azdVNrKfWpZEo%2Fg28yhlVttYaEpHEHjuIpFc4N5Imj3rdlPnD%2FUXu929DWr%2BkHb66MLPtPCWocWeCQRGmruRARDCxqskXfCc3Fme%2FyQJ9Vzx9wydNsFRCSXV6a986&X-Amz-Signature=ae47d8ef7ac7636184484c30099f9c7e6b220a99b5974992c1402292d6c99d0c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KFQJSKD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIE5yPW1NUX77%2BSzNUr%2BHmYhXN1VStON2OZP0tN7itdhsAiBEWK54qo00ZYnyajTOUil1JCvYlQfzl1DVFAec79kmmSr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMJGUxM1XxmTNunhXeKtwDQpeUPuFOduGc1aTGe0ULGnQEbEmFllSD8pUrLvGTNdTgOgE0fI4yoZD%2FspdNAUiR%2By0dH7wIqZmHI4StP0YjKJY9RYiChFSL9zvtLiKosTlRvkyt%2FY7O0dUBTG4AIAWQVDFIPWbniTLKdZ7k4PkVvksIQFt2gSPqpteN45HDhuqdtaoW4ZYhibACn13Q1SZz%2F728IDe%2Fg2lg%2FzkLpR4Yjd19Y5AKVg4hbFwK8Z3d0sWkmsDqkqZyKD2EcFiKuvtOYRavg8GQl3IGwfuRGjhlTyDeRKGr83MX0U0uZs4KJAuemeH2ItHky7dOJTE97XqpK%2FkQ3xOK1kh6QC3vAWO4B2l6ZGpuGrdHSPo6a9J%2FeGN4wK%2FDHHnLqaj9jSvaoy8GvIK23P%2FaLlIVNnIFYbvgsOd37n0DlpAx%2Bag5OXdWaPk0OFwvDmWEf8QxLkYQ0BSNFVnzn3%2FAFLUKMZDkU7A%2By3CEnWx8P42yFnBlGX1EzuKsjTYFfJKxlKKmhrtSF4y4DSPMvtchdlGr65aVUpiGUDzNu47ClEbUSvdUUp0N%2Fn3yjl9UR8U8rK4v6id48C%2FtYGoP8LSwIvLKZceOz4ghN3WbidQ5MDj6Q5coTUH7Zj6ytup1%2FGwUFVAt1gww0PuTvQY6pgGq6T0L2N7KonRoaLgE2VNyhxUsMhzDkBg%2B410FXQpRytf4wplgmQAwCItY7g2TdcB3UAeTCnSoRyJ7hNTvSru7Cggc3p5pGY5azdVNrKfWpZEo%2Fg28yhlVttYaEpHEHjuIpFc4N5Imj3rdlPnD%2FUXu929DWr%2BkHb66MLPtPCWocWeCQRGmruRARDCxqskXfCc3Fme%2FyQJ9Vzx9wydNsFRCSXV6a986&X-Amz-Signature=d7dfec6a75641667fc37bf9ec1920c7c5060aa273fa075d2a6653dc4527221b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USXX3TDF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIG3D12Ua4%2BgFkTuoxJY1%2FIw0h7TdhEV1d3T1uF0TOR%2BbAiACxskdEbznDst4ywSx8axr1OtsGyE1y9xJwljm1Q371Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMKyPiwMr1rHcrmYEXKtwDOzhWFsViExTI6m60z6q5I%2BFXNATQI%2BEluAiX9bu9j725GwQkweJZijQrW6O8PHG6NXshjfUKkmo071VVm6q8RKdh7R0ZAfH2SmiFqxXfKSOmsGjxFqyw%2BQ9sw6A1%2Bqifl4FHjcMRtUibxq3QZM8wjzRTgTJYu5xBcKBhcU0q63YntgiaqhkMbuQe5mJCmhn%2FcqsQQP1hklzQjtw%2FuPLDZVeDHZTCPXAsgwKCVQsKfICPZVyiSEHjSCPznEhvimuyc4L4iiYjYyHdPokpHqcDsea7cMpUXt02G2e0FXNIAX4JB5DRkIL5M4YrZz0cuSAYYqY0we7SXlf%2B135xA7d82rKYaBWqpD3r%2BfspM2DMVI8BfQyW0XubD4Ixx%2BkDikDnNCJa2bvVT4rKyR2BsybdI5u53tKPe%2B%2BrxK1b4gfv78CVIYivmHf0w1fVRg1oSyG8zpW0EXgC2zhfE8SqBn%2BBlW7bsx1yxqlYkSZsVgEU41sh6fEV%2FQFJys8L44VtyzywolGgZ%2FJ%2BDkE3vkuKvfgO86MfAvxKNrp6mfyRJBFCWKrAnrPyX9gyleTlg1yIZSA9173DvSPwyyNi2OQk6cmdCZ291fTEC8VLV5y4VPwmukx1dnhoqhSkj4TNnOYw2PuTvQY6pgEK84T8TXdgZF2DLDs8tyd8birqgyvQ27fSSmlK1IysHEHJysGQ10uzuV%2FfvBN%2BC1Bmez1nugGKDzxwQAtTdxye91IAcE%2FUfRJ92zOFO269IxfpbGozQgAb9c9Pjw2adpziqH87ouz2pVb2C8REPyNzKG9SchDfZAa9WB2HdNU2RN4Kc85x0%2FapjQn16EL4BGFUFuLOmNHNqQIwD0s4WJlSDde%2FnZ%2F6&X-Amz-Signature=f23e494b6489f386c97c3faa40667d01d562fcf3b3ff66db2d3b8e2951e2f4e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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