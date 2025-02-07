

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NA3RHTR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIDgmKo4iz1mWqObtfOqYHUorRlINesvnOTABp6%2BtPf1zAiEA15UoFQ%2FWM%2FLcI24qzsdAVyfOA8R%2FK725atoDQFwPiLIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIyHUiXvcYxQU5vXgSrcA410vRv9kiWUrnD61moQgA16hghtEyDsfnJKKWsysn56h2g3m8q97ytZ%2FO5exWonEmOkqhtdxB%2FldqalOZG%2BDMVZQdbmSB3XHpDy742tPgiH04Fb%2BzWOgA1aCUXoaqVUFuBQ4Uqa6qYDb0oxrDisMKodGDPQ6YdfzHydpC0Afy2Lgo%2FYlAc29IQrPAXSRPntv4JPpAKDRmnF1tkACAgbX4Ru5%2BMeMnMSVY03Vb6YBFJyLtEVoT%2FR02JJ9i1KXMd%2BNpei5oTpYCgsa5ZQO2tTpKEYxI91j42a0rYPkirYy0a50k1XPl1fU8Sg%2Fe6Ktc4rRY0BtRdU36FlnJCbcGVBxwMfvGQ86Rkw8KnXi1uJupkI7UTF%2BFzEJxA%2FBeDJd40kGJaUMouH5ZO3I62mwwcE7AWSWpDmvaGoP2TLMT9t5aNHdF%2Fd%2FBwLJStn0K5di4MTfOupTLAtgHcigt39UOI7jk2OrEaUgoBv6p73YYeYk2zkWUQ837Cc2jb%2F4ucW%2FXtFWUrNCRzM333JQNggPzY9vsZ43xPUuhnWbwpyteftWzRnz3zHE4Uz8mSJr9GLujSNGolG7bCdjIRPAJ1g0IrURZUdMaH9B%2FducTlfnMRlNcLoLtvCyll7d9fSf6EyMNL%2Bmb0GOqUBXWTn0MJddYcV5YWzs8ljoFwGckJSILyOibGOLflsfPu3xt6MSnwOJGwiU5vJ3%2BSsg61iLceK7H3y9OX%2BDLcz3Y06nRI8mp%2F8ZEDcppF1giOYWbiiWw%2BBYWnQ27%2Fe9%2Fcr40saaSrVWDYBeSyaAgqrp14R%2F%2BgVD%2FASTt%2FliNQ5V4szntCDoLA000xwBTb6lPkrnDDQ7OjrKPJxHVxXRL9hwGnLBo8D&X-Amz-Signature=c5c59d330f8d770e9ed05745735bc6fc3c983cb274480f1a3e48f9946c2c749e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NA3RHTR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIDgmKo4iz1mWqObtfOqYHUorRlINesvnOTABp6%2BtPf1zAiEA15UoFQ%2FWM%2FLcI24qzsdAVyfOA8R%2FK725atoDQFwPiLIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIyHUiXvcYxQU5vXgSrcA410vRv9kiWUrnD61moQgA16hghtEyDsfnJKKWsysn56h2g3m8q97ytZ%2FO5exWonEmOkqhtdxB%2FldqalOZG%2BDMVZQdbmSB3XHpDy742tPgiH04Fb%2BzWOgA1aCUXoaqVUFuBQ4Uqa6qYDb0oxrDisMKodGDPQ6YdfzHydpC0Afy2Lgo%2FYlAc29IQrPAXSRPntv4JPpAKDRmnF1tkACAgbX4Ru5%2BMeMnMSVY03Vb6YBFJyLtEVoT%2FR02JJ9i1KXMd%2BNpei5oTpYCgsa5ZQO2tTpKEYxI91j42a0rYPkirYy0a50k1XPl1fU8Sg%2Fe6Ktc4rRY0BtRdU36FlnJCbcGVBxwMfvGQ86Rkw8KnXi1uJupkI7UTF%2BFzEJxA%2FBeDJd40kGJaUMouH5ZO3I62mwwcE7AWSWpDmvaGoP2TLMT9t5aNHdF%2Fd%2FBwLJStn0K5di4MTfOupTLAtgHcigt39UOI7jk2OrEaUgoBv6p73YYeYk2zkWUQ837Cc2jb%2F4ucW%2FXtFWUrNCRzM333JQNggPzY9vsZ43xPUuhnWbwpyteftWzRnz3zHE4Uz8mSJr9GLujSNGolG7bCdjIRPAJ1g0IrURZUdMaH9B%2FducTlfnMRlNcLoLtvCyll7d9fSf6EyMNL%2Bmb0GOqUBXWTn0MJddYcV5YWzs8ljoFwGckJSILyOibGOLflsfPu3xt6MSnwOJGwiU5vJ3%2BSsg61iLceK7H3y9OX%2BDLcz3Y06nRI8mp%2F8ZEDcppF1giOYWbiiWw%2BBYWnQ27%2Fe9%2Fcr40saaSrVWDYBeSyaAgqrp14R%2F%2BgVD%2FASTt%2FliNQ5V4szntCDoLA000xwBTb6lPkrnDDQ7OjrKPJxHVxXRL9hwGnLBo8D&X-Amz-Signature=f44fc4456a4b57c33dd3f33d2cb4772d517e395964c2e5bec9999e8abdce86f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NA3RHTR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIDgmKo4iz1mWqObtfOqYHUorRlINesvnOTABp6%2BtPf1zAiEA15UoFQ%2FWM%2FLcI24qzsdAVyfOA8R%2FK725atoDQFwPiLIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIyHUiXvcYxQU5vXgSrcA410vRv9kiWUrnD61moQgA16hghtEyDsfnJKKWsysn56h2g3m8q97ytZ%2FO5exWonEmOkqhtdxB%2FldqalOZG%2BDMVZQdbmSB3XHpDy742tPgiH04Fb%2BzWOgA1aCUXoaqVUFuBQ4Uqa6qYDb0oxrDisMKodGDPQ6YdfzHydpC0Afy2Lgo%2FYlAc29IQrPAXSRPntv4JPpAKDRmnF1tkACAgbX4Ru5%2BMeMnMSVY03Vb6YBFJyLtEVoT%2FR02JJ9i1KXMd%2BNpei5oTpYCgsa5ZQO2tTpKEYxI91j42a0rYPkirYy0a50k1XPl1fU8Sg%2Fe6Ktc4rRY0BtRdU36FlnJCbcGVBxwMfvGQ86Rkw8KnXi1uJupkI7UTF%2BFzEJxA%2FBeDJd40kGJaUMouH5ZO3I62mwwcE7AWSWpDmvaGoP2TLMT9t5aNHdF%2Fd%2FBwLJStn0K5di4MTfOupTLAtgHcigt39UOI7jk2OrEaUgoBv6p73YYeYk2zkWUQ837Cc2jb%2F4ucW%2FXtFWUrNCRzM333JQNggPzY9vsZ43xPUuhnWbwpyteftWzRnz3zHE4Uz8mSJr9GLujSNGolG7bCdjIRPAJ1g0IrURZUdMaH9B%2FducTlfnMRlNcLoLtvCyll7d9fSf6EyMNL%2Bmb0GOqUBXWTn0MJddYcV5YWzs8ljoFwGckJSILyOibGOLflsfPu3xt6MSnwOJGwiU5vJ3%2BSsg61iLceK7H3y9OX%2BDLcz3Y06nRI8mp%2F8ZEDcppF1giOYWbiiWw%2BBYWnQ27%2Fe9%2Fcr40saaSrVWDYBeSyaAgqrp14R%2F%2BgVD%2FASTt%2FliNQ5V4szntCDoLA000xwBTb6lPkrnDDQ7OjrKPJxHVxXRL9hwGnLBo8D&X-Amz-Signature=8f5fb2ee397887e6da78d84f1e7754af2ef836e4f86f1a216488a835f0ccd571&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLEUVW6K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDL6CWHSUpvHYrEmKml%2BNmiirUZRDa0Z0I08P02%2BKApBQIgCfb8LxtKBJlB3NeJhwDjTBkIYkq1dX%2F6Ei6jxh6Ph7Iq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHomNInFfaIOABP1FyrcA5lPKZLCevkbhcWgFrw01LnXIic0Uf%2Bd%2BqwvYabBAG0ZYFZjmL4hjvMlX%2FHiFUlAMI7Ljj4wjHY59bCzYM%2BRv3TABhKn%2FlaPknb6Ga9gm%2FDHymDbCY4uaSxT9oyFT%2BASPonW2ULStNGnrKetdMBG7UYEjg1hw6jXtOfUd11%2FpVP4icVqoJPCCnrOCycFcGXBdYrdndjR8DOaJM2hV8GlGdhXcXdgWfsjERapiQDCdH6wMGpUZDnjjABnm0LyLCjE0xXXLE2MdflpX4vw%2F79ixKNUntOtqJiEDxXMTZXRP3UJAe9Xmemxql2cuEuQgocFvNoyTCjEm9O%2FNeMrtch%2FbgmrHYBkBuXTzu1l2wPuaVstgTp0M9OdzmoXWT3naShKDAzH5CKCZuoHVxdYWrT8l06oQnHwypvGs2IhCOP1DV1qaDDvxDMfLHEp1OxRYmgM7kT6bGboXYug4In0ZibL2%2FxQDvirW4XMwX%2BJc8CuYu%2BaH1wtDIrKGZuWLtX3xEd0SP4ZJR%2B4woBTlwUrqVCimnznCWQPTaLT6h%2B6BVz7teRTqjjRU4HBFNVkS%2Fulg8IHLqcsC0LExiAlPCkpFVcWJzR5hxBMZtzSLOFXLIgsKB2%2Fz9Q9cDAgYC%2B4AXwbMJf%2Bmb0GOqUBgzdbposI8J%2Fsjzx6BzGUSkvC69HjQt57WEORkT%2By9XeIXxMBtaNni92hBA3yO32Gtz2QOFh6XQX7cHP157cCCKd9tGuX7H%2F6QJ7InVcmCoZXc3mM%2Bu1sjJ6V0BxN2JkK7nZHtNpTKj2yeZrTBvlN3hl4FBh1nMEP5XAL%2FUFiUYmhtJq%2BDn1S81ZSa%2BN%2BFax%2FR7kI6mtpCdhcjPqYuyN%2BK1Yyb20y&X-Amz-Signature=780c0c42361db0686cfa1b49e618aa2a8d455da5b84c1d08378f9f4526e6ff8d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLEUVW6K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDL6CWHSUpvHYrEmKml%2BNmiirUZRDa0Z0I08P02%2BKApBQIgCfb8LxtKBJlB3NeJhwDjTBkIYkq1dX%2F6Ei6jxh6Ph7Iq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHomNInFfaIOABP1FyrcA5lPKZLCevkbhcWgFrw01LnXIic0Uf%2Bd%2BqwvYabBAG0ZYFZjmL4hjvMlX%2FHiFUlAMI7Ljj4wjHY59bCzYM%2BRv3TABhKn%2FlaPknb6Ga9gm%2FDHymDbCY4uaSxT9oyFT%2BASPonW2ULStNGnrKetdMBG7UYEjg1hw6jXtOfUd11%2FpVP4icVqoJPCCnrOCycFcGXBdYrdndjR8DOaJM2hV8GlGdhXcXdgWfsjERapiQDCdH6wMGpUZDnjjABnm0LyLCjE0xXXLE2MdflpX4vw%2F79ixKNUntOtqJiEDxXMTZXRP3UJAe9Xmemxql2cuEuQgocFvNoyTCjEm9O%2FNeMrtch%2FbgmrHYBkBuXTzu1l2wPuaVstgTp0M9OdzmoXWT3naShKDAzH5CKCZuoHVxdYWrT8l06oQnHwypvGs2IhCOP1DV1qaDDvxDMfLHEp1OxRYmgM7kT6bGboXYug4In0ZibL2%2FxQDvirW4XMwX%2BJc8CuYu%2BaH1wtDIrKGZuWLtX3xEd0SP4ZJR%2B4woBTlwUrqVCimnznCWQPTaLT6h%2B6BVz7teRTqjjRU4HBFNVkS%2Fulg8IHLqcsC0LExiAlPCkpFVcWJzR5hxBMZtzSLOFXLIgsKB2%2Fz9Q9cDAgYC%2B4AXwbMJf%2Bmb0GOqUBgzdbposI8J%2Fsjzx6BzGUSkvC69HjQt57WEORkT%2By9XeIXxMBtaNni92hBA3yO32Gtz2QOFh6XQX7cHP157cCCKd9tGuX7H%2F6QJ7InVcmCoZXc3mM%2Bu1sjJ6V0BxN2JkK7nZHtNpTKj2yeZrTBvlN3hl4FBh1nMEP5XAL%2FUFiUYmhtJq%2BDn1S81ZSa%2BN%2BFax%2FR7kI6mtpCdhcjPqYuyN%2BK1Yyb20y&X-Amz-Signature=ef022b161c70ab2ad4c0534d2ac60ca0c83794e3f0f4f3207d49d5813e581b94&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NA3RHTR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIDgmKo4iz1mWqObtfOqYHUorRlINesvnOTABp6%2BtPf1zAiEA15UoFQ%2FWM%2FLcI24qzsdAVyfOA8R%2FK725atoDQFwPiLIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIyHUiXvcYxQU5vXgSrcA410vRv9kiWUrnD61moQgA16hghtEyDsfnJKKWsysn56h2g3m8q97ytZ%2FO5exWonEmOkqhtdxB%2FldqalOZG%2BDMVZQdbmSB3XHpDy742tPgiH04Fb%2BzWOgA1aCUXoaqVUFuBQ4Uqa6qYDb0oxrDisMKodGDPQ6YdfzHydpC0Afy2Lgo%2FYlAc29IQrPAXSRPntv4JPpAKDRmnF1tkACAgbX4Ru5%2BMeMnMSVY03Vb6YBFJyLtEVoT%2FR02JJ9i1KXMd%2BNpei5oTpYCgsa5ZQO2tTpKEYxI91j42a0rYPkirYy0a50k1XPl1fU8Sg%2Fe6Ktc4rRY0BtRdU36FlnJCbcGVBxwMfvGQ86Rkw8KnXi1uJupkI7UTF%2BFzEJxA%2FBeDJd40kGJaUMouH5ZO3I62mwwcE7AWSWpDmvaGoP2TLMT9t5aNHdF%2Fd%2FBwLJStn0K5di4MTfOupTLAtgHcigt39UOI7jk2OrEaUgoBv6p73YYeYk2zkWUQ837Cc2jb%2F4ucW%2FXtFWUrNCRzM333JQNggPzY9vsZ43xPUuhnWbwpyteftWzRnz3zHE4Uz8mSJr9GLujSNGolG7bCdjIRPAJ1g0IrURZUdMaH9B%2FducTlfnMRlNcLoLtvCyll7d9fSf6EyMNL%2Bmb0GOqUBXWTn0MJddYcV5YWzs8ljoFwGckJSILyOibGOLflsfPu3xt6MSnwOJGwiU5vJ3%2BSsg61iLceK7H3y9OX%2BDLcz3Y06nRI8mp%2F8ZEDcppF1giOYWbiiWw%2BBYWnQ27%2Fe9%2Fcr40saaSrVWDYBeSyaAgqrp14R%2F%2BgVD%2FASTt%2FliNQ5V4szntCDoLA000xwBTb6lPkrnDDQ7OjrKPJxHVxXRL9hwGnLBo8D&X-Amz-Signature=430132a965e8b5bfa9dcde53cab996855c326ce4a923b2b6f2a09c6193d64a78&X-Amz-SignedHeaders=host&x-id=GetObject)
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