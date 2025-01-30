

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXFGO7P4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICDw5BQMCFd41K1byVy356VFr6IA1Ly3LGtq%2B5hplkrQAiA2v55aRPcX1Ina6yj12X%2Bf5NNqvgO2chVJW%2BiRCOOEtSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOyJ%2FHYKoNtClsCSBKtwDbzuKSV33aAp5zzT9nOznn%2F8xdQN93v4s0ghEuTsvEQs7WT7FDHPvC%2FUERFB0ZEHK2U8qxo7i72dSBCw1awcededzXzBpgyKcn6QjoPnAleagkvub5zE2nMzBAGZJgnwDpb9D8fnfu46mXTMrrr1vTAlCmDVKLYHL4MMkEpl9%2BYTnuqWRTVvWKdta709qk7Urc8WwB3PfrK5jhGyAOzArkGFJoNjzoRPYJbKvfC8H1YYwUZ%2BxeqfxmRW2i2doO2Ctaift9qTXkelPEBBwFykJb1EnLsQtxq0sRcIR7vRGI3MCfoJVT3KKYzCC4rtibnD%2FkDZL2mVL8ZEyKJJq04rtVR1wnl5ecsDHm3acldy0a8PxtZGXyH9S1ff%2F01nSDwXiKNcx5A84VfEoJkSrHiRefEaaxJP6XdgZEufnpoht%2Bs9hmBjmeES%2Be8EvriQsWu6tQk5P6g0x8CEEJ8F3vuTkQ01D05vQ5OX2lE7HCLihaDpwCNlLtvjy1PT30M065TJmd6hh%2Fl16PvTTpibWC7fpzsiRXs202RmGb9lSP8D6sEaCamFQ060mojy%2FY5gxDIFglbBPqK%2FhPu%2FVNmWhSqG7tCQLOeiWQEOGWLagZC%2Bs7952GbASRk6KInvPYpEw%2BfrtvAY6pgEQnDe8pCt%2B58KeDeJLoEFdXRFVJtnBiDXCSb9gtWOgxa%2B%2Fq%2BXvkbzWVZLXRmO1pGXLW%2FWZ7%2B%2B5QGHedZAkv2mhpddsG6oGznlp6RU8VGCVPVVpt9CY3hK6sRgrmraKIxMP1fZTxaTkcc%2BNkg1SLZ0IdRHK6Gbzavj%2Bhfxq2%2F2XX%2FMch2ykG5VAqwJqcxv%2BWXRjs68fo8sF9duUOZoAksR5LbhtPIfY&X-Amz-Signature=87b12ecbac5770ff017c328f462c27ceb707a1ba216b5e603929ffa2c31b9e19&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXFGO7P4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICDw5BQMCFd41K1byVy356VFr6IA1Ly3LGtq%2B5hplkrQAiA2v55aRPcX1Ina6yj12X%2Bf5NNqvgO2chVJW%2BiRCOOEtSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOyJ%2FHYKoNtClsCSBKtwDbzuKSV33aAp5zzT9nOznn%2F8xdQN93v4s0ghEuTsvEQs7WT7FDHPvC%2FUERFB0ZEHK2U8qxo7i72dSBCw1awcededzXzBpgyKcn6QjoPnAleagkvub5zE2nMzBAGZJgnwDpb9D8fnfu46mXTMrrr1vTAlCmDVKLYHL4MMkEpl9%2BYTnuqWRTVvWKdta709qk7Urc8WwB3PfrK5jhGyAOzArkGFJoNjzoRPYJbKvfC8H1YYwUZ%2BxeqfxmRW2i2doO2Ctaift9qTXkelPEBBwFykJb1EnLsQtxq0sRcIR7vRGI3MCfoJVT3KKYzCC4rtibnD%2FkDZL2mVL8ZEyKJJq04rtVR1wnl5ecsDHm3acldy0a8PxtZGXyH9S1ff%2F01nSDwXiKNcx5A84VfEoJkSrHiRefEaaxJP6XdgZEufnpoht%2Bs9hmBjmeES%2Be8EvriQsWu6tQk5P6g0x8CEEJ8F3vuTkQ01D05vQ5OX2lE7HCLihaDpwCNlLtvjy1PT30M065TJmd6hh%2Fl16PvTTpibWC7fpzsiRXs202RmGb9lSP8D6sEaCamFQ060mojy%2FY5gxDIFglbBPqK%2FhPu%2FVNmWhSqG7tCQLOeiWQEOGWLagZC%2Bs7952GbASRk6KInvPYpEw%2BfrtvAY6pgEQnDe8pCt%2B58KeDeJLoEFdXRFVJtnBiDXCSb9gtWOgxa%2B%2Fq%2BXvkbzWVZLXRmO1pGXLW%2FWZ7%2B%2B5QGHedZAkv2mhpddsG6oGznlp6RU8VGCVPVVpt9CY3hK6sRgrmraKIxMP1fZTxaTkcc%2BNkg1SLZ0IdRHK6Gbzavj%2Bhfxq2%2F2XX%2FMch2ykG5VAqwJqcxv%2BWXRjs68fo8sF9duUOZoAksR5LbhtPIfY&X-Amz-Signature=0b05bfe1967e1c307ee37a0633d6f0652c26752c60de195792336e6441ccd495&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXFGO7P4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICDw5BQMCFd41K1byVy356VFr6IA1Ly3LGtq%2B5hplkrQAiA2v55aRPcX1Ina6yj12X%2Bf5NNqvgO2chVJW%2BiRCOOEtSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOyJ%2FHYKoNtClsCSBKtwDbzuKSV33aAp5zzT9nOznn%2F8xdQN93v4s0ghEuTsvEQs7WT7FDHPvC%2FUERFB0ZEHK2U8qxo7i72dSBCw1awcededzXzBpgyKcn6QjoPnAleagkvub5zE2nMzBAGZJgnwDpb9D8fnfu46mXTMrrr1vTAlCmDVKLYHL4MMkEpl9%2BYTnuqWRTVvWKdta709qk7Urc8WwB3PfrK5jhGyAOzArkGFJoNjzoRPYJbKvfC8H1YYwUZ%2BxeqfxmRW2i2doO2Ctaift9qTXkelPEBBwFykJb1EnLsQtxq0sRcIR7vRGI3MCfoJVT3KKYzCC4rtibnD%2FkDZL2mVL8ZEyKJJq04rtVR1wnl5ecsDHm3acldy0a8PxtZGXyH9S1ff%2F01nSDwXiKNcx5A84VfEoJkSrHiRefEaaxJP6XdgZEufnpoht%2Bs9hmBjmeES%2Be8EvriQsWu6tQk5P6g0x8CEEJ8F3vuTkQ01D05vQ5OX2lE7HCLihaDpwCNlLtvjy1PT30M065TJmd6hh%2Fl16PvTTpibWC7fpzsiRXs202RmGb9lSP8D6sEaCamFQ060mojy%2FY5gxDIFglbBPqK%2FhPu%2FVNmWhSqG7tCQLOeiWQEOGWLagZC%2Bs7952GbASRk6KInvPYpEw%2BfrtvAY6pgEQnDe8pCt%2B58KeDeJLoEFdXRFVJtnBiDXCSb9gtWOgxa%2B%2Fq%2BXvkbzWVZLXRmO1pGXLW%2FWZ7%2B%2B5QGHedZAkv2mhpddsG6oGznlp6RU8VGCVPVVpt9CY3hK6sRgrmraKIxMP1fZTxaTkcc%2BNkg1SLZ0IdRHK6Gbzavj%2Bhfxq2%2F2XX%2FMch2ykG5VAqwJqcxv%2BWXRjs68fo8sF9duUOZoAksR5LbhtPIfY&X-Amz-Signature=ab9f372134816db9791ef5fb3a39844aeaebc46e787f1a1761182cba67ce83f9&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROAWEN6C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICxWieYAslop7n7kUcpPu%2Fhl2OahorrQbll3PSa8oEWgAiEAuygTk47ogyi8tBdNP1QGnMFTzCw2TWW8owWPbAftKWUqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZ7s5l350ifyX%2FVzSrcA8iZ0S%2FFZ06SCsfJyHTWLQv6K1YbP7twMGsFimKwRsbPUZjyjkfyfSWml3fqhFHuXSONFlQJnPvw5BXisxF8RZJCXkaQgl4TeuOcz2AUpoTyi%2BhhG76GREoWN52Qp5ZtDWlPr9ntsjsLQNguZVcmKyPy620BRpXl7LDZc0cSdXhIsIk%2BjqnpyV41O8s9Pv%2BpKwYwGvugwmxQWxHsWPIkoeeG5FF%2Bf4BcZlfIiCnaSHVttUu%2FutNTVK551Wt2JtydWr2gwkyGXDjrlJuTg5Pn74AhM3HcqZbK6tbBrRwEsc98YNfGDa%2BJLVfbJKoklo5jyD1wBtduBkTXThgV%2F%2BetBh8rC1ha%2Bx%2Fe2TqdGODBld3O1gtB0pz7wkzAJhtU8BquEB5iKSjtyP%2FjL1SePpgpKnqsxbZyvtMxlKnKiEfl4Plr2d5M%2BZMBlk9l3c5XhNcLf6ahSo%2FkXMA%2FUGJJwsr57M1Gu0RvlK5DaUMbtzERXrE8fK93x4FxatiwgSSCrq9xyy1Pe0afpo8byLX4iogzJaoKfjdi9vKvnojR3KEeglMaYDCER%2FhI655hlYZOBxNaLYLr%2FZE8h57Oj8hkckwr%2Fz1oejmN4vowovl103vAuW7tJ5r7M%2BmmA0TlXWgrMMX67bwGOqUBHcUVXlMqdJpksHRIjO7CrIcG6GtCwE7rk5fK%2FzV3D0HhHdPqm%2BY6%2B3vCJKVyp6iJ1juX7sC%2BD7N5MibIHNJjWAHPqEe5Knz%2FhGFfpgUK0jBiybpqotk0twfRNST6moE51QKsbV4f%2Bgyc82hzgKK%2B8v2106HvEYptUs74f%2BiiPDTkea%2Bf3lVFWnLmhuRcuEMEE5pt87KjoQZAxCPj3b9FHR%2Fm4dE4&X-Amz-Signature=6f7d21404f0ed48f151a9592fd89a5160a39c562ba41916be5cb1a7b5081c325&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROAWEN6C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICxWieYAslop7n7kUcpPu%2Fhl2OahorrQbll3PSa8oEWgAiEAuygTk47ogyi8tBdNP1QGnMFTzCw2TWW8owWPbAftKWUqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZ7s5l350ifyX%2FVzSrcA8iZ0S%2FFZ06SCsfJyHTWLQv6K1YbP7twMGsFimKwRsbPUZjyjkfyfSWml3fqhFHuXSONFlQJnPvw5BXisxF8RZJCXkaQgl4TeuOcz2AUpoTyi%2BhhG76GREoWN52Qp5ZtDWlPr9ntsjsLQNguZVcmKyPy620BRpXl7LDZc0cSdXhIsIk%2BjqnpyV41O8s9Pv%2BpKwYwGvugwmxQWxHsWPIkoeeG5FF%2Bf4BcZlfIiCnaSHVttUu%2FutNTVK551Wt2JtydWr2gwkyGXDjrlJuTg5Pn74AhM3HcqZbK6tbBrRwEsc98YNfGDa%2BJLVfbJKoklo5jyD1wBtduBkTXThgV%2F%2BetBh8rC1ha%2Bx%2Fe2TqdGODBld3O1gtB0pz7wkzAJhtU8BquEB5iKSjtyP%2FjL1SePpgpKnqsxbZyvtMxlKnKiEfl4Plr2d5M%2BZMBlk9l3c5XhNcLf6ahSo%2FkXMA%2FUGJJwsr57M1Gu0RvlK5DaUMbtzERXrE8fK93x4FxatiwgSSCrq9xyy1Pe0afpo8byLX4iogzJaoKfjdi9vKvnojR3KEeglMaYDCER%2FhI655hlYZOBxNaLYLr%2FZE8h57Oj8hkckwr%2Fz1oejmN4vowovl103vAuW7tJ5r7M%2BmmA0TlXWgrMMX67bwGOqUBHcUVXlMqdJpksHRIjO7CrIcG6GtCwE7rk5fK%2FzV3D0HhHdPqm%2BY6%2B3vCJKVyp6iJ1juX7sC%2BD7N5MibIHNJjWAHPqEe5Knz%2FhGFfpgUK0jBiybpqotk0twfRNST6moE51QKsbV4f%2Bgyc82hzgKK%2B8v2106HvEYptUs74f%2BiiPDTkea%2Bf3lVFWnLmhuRcuEMEE5pt87KjoQZAxCPj3b9FHR%2Fm4dE4&X-Amz-Signature=11e152eaaa0d42dbad684c6a11d3e758caa266f8dcf69834f5ce1943d966b300&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXFGO7P4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICDw5BQMCFd41K1byVy356VFr6IA1Ly3LGtq%2B5hplkrQAiA2v55aRPcX1Ina6yj12X%2Bf5NNqvgO2chVJW%2BiRCOOEtSqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOyJ%2FHYKoNtClsCSBKtwDbzuKSV33aAp5zzT9nOznn%2F8xdQN93v4s0ghEuTsvEQs7WT7FDHPvC%2FUERFB0ZEHK2U8qxo7i72dSBCw1awcededzXzBpgyKcn6QjoPnAleagkvub5zE2nMzBAGZJgnwDpb9D8fnfu46mXTMrrr1vTAlCmDVKLYHL4MMkEpl9%2BYTnuqWRTVvWKdta709qk7Urc8WwB3PfrK5jhGyAOzArkGFJoNjzoRPYJbKvfC8H1YYwUZ%2BxeqfxmRW2i2doO2Ctaift9qTXkelPEBBwFykJb1EnLsQtxq0sRcIR7vRGI3MCfoJVT3KKYzCC4rtibnD%2FkDZL2mVL8ZEyKJJq04rtVR1wnl5ecsDHm3acldy0a8PxtZGXyH9S1ff%2F01nSDwXiKNcx5A84VfEoJkSrHiRefEaaxJP6XdgZEufnpoht%2Bs9hmBjmeES%2Be8EvriQsWu6tQk5P6g0x8CEEJ8F3vuTkQ01D05vQ5OX2lE7HCLihaDpwCNlLtvjy1PT30M065TJmd6hh%2Fl16PvTTpibWC7fpzsiRXs202RmGb9lSP8D6sEaCamFQ060mojy%2FY5gxDIFglbBPqK%2FhPu%2FVNmWhSqG7tCQLOeiWQEOGWLagZC%2Bs7952GbASRk6KInvPYpEw%2BfrtvAY6pgEQnDe8pCt%2B58KeDeJLoEFdXRFVJtnBiDXCSb9gtWOgxa%2B%2Fq%2BXvkbzWVZLXRmO1pGXLW%2FWZ7%2B%2B5QGHedZAkv2mhpddsG6oGznlp6RU8VGCVPVVpt9CY3hK6sRgrmraKIxMP1fZTxaTkcc%2BNkg1SLZ0IdRHK6Gbzavj%2Bhfxq2%2F2XX%2FMch2ykG5VAqwJqcxv%2BWXRjs68fo8sF9duUOZoAksR5LbhtPIfY&X-Amz-Signature=28e8b61dfa3483bc0bf8d9bc928240981ae729967a7dc3ddc4a2922ef9628033&X-Amz-SignedHeaders=host&x-id=GetObject)
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