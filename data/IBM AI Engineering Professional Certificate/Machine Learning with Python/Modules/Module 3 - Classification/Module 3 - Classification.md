

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMN5KHC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeEMfto8AvOFmEaoxnqHSySyUOwevY57SHLuRBSCRGOAiEAh7XpYohhErCSY8CeQycWPv1U%2BSJISvXY4vV72BmPcjwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhxEnxIYFRmp7RC5CrcA27coYm74EQP7cGnJ3Z%2FVz3sOr4%2F%2F31Gv6lafM1Zqike%2B0Z3vsWjwT00Gq90ciX7LFj%2Fbgn5HMDRBPMvEWASfyOBP4QAX6xY3LtkS3D1eXedMJ8TFkBu2BKx%2FiF7wvs4KUc4DCE1FZGps38TkXjLmDvCY04F%2FHkEzL0u41ehLD6hJt1P97GhXBKdWCAj2W8%2FfGaHSCe4LgcqVJaFT0A%2Ftpe3ELKwbVMRxiFfHXmIChQfsuMXMuSd8wUqRMU9Bk2gwb6RBwmn4fOXm902Q23jVI03OGU7vDVnZczr44%2BWEYcj7j0a8kH2W77zlYwDbVyNFva8CNs32FKP7hMqXXBDEYpZcmhsoyxmFvSge%2F4DmOcI%2BAvfO8fdu0cjXU4O5tOq3M0FbvPaEXTFpIk7vRtK%2BmXi39eXu6BHcZYiaWnCMm93ihd58rXJ0DgRNZfyoWqEV%2BsFteC9Jz04YZc7dy%2B0IwjoOxQ3k6wmqb73nAwcxwPiP7M9JQDk27YfICp9w2F1nxfCdloRLFUpsc1fMQ8%2FCPwEmx3QM3Tich%2FZMHz803XuT%2FPraUGsR%2FnImoUTOx8zPGchggdiKqzgV0Q%2FvrcFUI32%2BX4%2FZ2hwQFzi6iz7oCv82KhoSK5AsWFA1IGVMN2T9bwGOqUBRCEGUXF7nbNZ%2BSWywNSSIn6hZ6Jp1xTmMBg2yiu4tBx0flIN%2FHkU%2FUZdMvA7497ZpMUHr2MhcgNhlhpNVqcrquHd%2BLCXhjoNKPW8mLfhfD3vRmhnQKoG%2BxRRZmq9w6bUA%2Bjzq2kjyHvie0J6trn3o7uqzmVVSKS4PV4cugg0n0OMF1TWvZFICo5%2FLeWCPk%2FwUxtXfeFJ4Q9RCeESzWHiW5GCasZP&X-Amz-Signature=fac788aae2f2ade6a1ab52d7229e41b05d082e53188b2e78c0902980d209e7ec&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMN5KHC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeEMfto8AvOFmEaoxnqHSySyUOwevY57SHLuRBSCRGOAiEAh7XpYohhErCSY8CeQycWPv1U%2BSJISvXY4vV72BmPcjwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhxEnxIYFRmp7RC5CrcA27coYm74EQP7cGnJ3Z%2FVz3sOr4%2F%2F31Gv6lafM1Zqike%2B0Z3vsWjwT00Gq90ciX7LFj%2Fbgn5HMDRBPMvEWASfyOBP4QAX6xY3LtkS3D1eXedMJ8TFkBu2BKx%2FiF7wvs4KUc4DCE1FZGps38TkXjLmDvCY04F%2FHkEzL0u41ehLD6hJt1P97GhXBKdWCAj2W8%2FfGaHSCe4LgcqVJaFT0A%2Ftpe3ELKwbVMRxiFfHXmIChQfsuMXMuSd8wUqRMU9Bk2gwb6RBwmn4fOXm902Q23jVI03OGU7vDVnZczr44%2BWEYcj7j0a8kH2W77zlYwDbVyNFva8CNs32FKP7hMqXXBDEYpZcmhsoyxmFvSge%2F4DmOcI%2BAvfO8fdu0cjXU4O5tOq3M0FbvPaEXTFpIk7vRtK%2BmXi39eXu6BHcZYiaWnCMm93ihd58rXJ0DgRNZfyoWqEV%2BsFteC9Jz04YZc7dy%2B0IwjoOxQ3k6wmqb73nAwcxwPiP7M9JQDk27YfICp9w2F1nxfCdloRLFUpsc1fMQ8%2FCPwEmx3QM3Tich%2FZMHz803XuT%2FPraUGsR%2FnImoUTOx8zPGchggdiKqzgV0Q%2FvrcFUI32%2BX4%2FZ2hwQFzi6iz7oCv82KhoSK5AsWFA1IGVMN2T9bwGOqUBRCEGUXF7nbNZ%2BSWywNSSIn6hZ6Jp1xTmMBg2yiu4tBx0flIN%2FHkU%2FUZdMvA7497ZpMUHr2MhcgNhlhpNVqcrquHd%2BLCXhjoNKPW8mLfhfD3vRmhnQKoG%2BxRRZmq9w6bUA%2Bjzq2kjyHvie0J6trn3o7uqzmVVSKS4PV4cugg0n0OMF1TWvZFICo5%2FLeWCPk%2FwUxtXfeFJ4Q9RCeESzWHiW5GCasZP&X-Amz-Signature=e682cbe9078a98e6cdcd46696527518ee278399fc30dd28d499c31d8921a27ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMN5KHC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeEMfto8AvOFmEaoxnqHSySyUOwevY57SHLuRBSCRGOAiEAh7XpYohhErCSY8CeQycWPv1U%2BSJISvXY4vV72BmPcjwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhxEnxIYFRmp7RC5CrcA27coYm74EQP7cGnJ3Z%2FVz3sOr4%2F%2F31Gv6lafM1Zqike%2B0Z3vsWjwT00Gq90ciX7LFj%2Fbgn5HMDRBPMvEWASfyOBP4QAX6xY3LtkS3D1eXedMJ8TFkBu2BKx%2FiF7wvs4KUc4DCE1FZGps38TkXjLmDvCY04F%2FHkEzL0u41ehLD6hJt1P97GhXBKdWCAj2W8%2FfGaHSCe4LgcqVJaFT0A%2Ftpe3ELKwbVMRxiFfHXmIChQfsuMXMuSd8wUqRMU9Bk2gwb6RBwmn4fOXm902Q23jVI03OGU7vDVnZczr44%2BWEYcj7j0a8kH2W77zlYwDbVyNFva8CNs32FKP7hMqXXBDEYpZcmhsoyxmFvSge%2F4DmOcI%2BAvfO8fdu0cjXU4O5tOq3M0FbvPaEXTFpIk7vRtK%2BmXi39eXu6BHcZYiaWnCMm93ihd58rXJ0DgRNZfyoWqEV%2BsFteC9Jz04YZc7dy%2B0IwjoOxQ3k6wmqb73nAwcxwPiP7M9JQDk27YfICp9w2F1nxfCdloRLFUpsc1fMQ8%2FCPwEmx3QM3Tich%2FZMHz803XuT%2FPraUGsR%2FnImoUTOx8zPGchggdiKqzgV0Q%2FvrcFUI32%2BX4%2FZ2hwQFzi6iz7oCv82KhoSK5AsWFA1IGVMN2T9bwGOqUBRCEGUXF7nbNZ%2BSWywNSSIn6hZ6Jp1xTmMBg2yiu4tBx0flIN%2FHkU%2FUZdMvA7497ZpMUHr2MhcgNhlhpNVqcrquHd%2BLCXhjoNKPW8mLfhfD3vRmhnQKoG%2BxRRZmq9w6bUA%2Bjzq2kjyHvie0J6trn3o7uqzmVVSKS4PV4cugg0n0OMF1TWvZFICo5%2FLeWCPk%2FwUxtXfeFJ4Q9RCeESzWHiW5GCasZP&X-Amz-Signature=0c8a11f0dfc2300a39e94e8f978a658c23d69b38758e2728686825f6dcbe7adb&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVYIGWKL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpLnbQ%2BhpQFFQEtLWiIfm7URJIAgqDmDtzg%2FcHcsaz1gIhAO3K%2FCw57vEPgFpWMSN1bcYDsBPqFf5ViEZj0IzxQ6YnKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSCFqBzGHhqa3di4Aq3AN6AEUhqV1m3v%2BgKnyznB4k5jbmcryM1yy5PraHPlqkyz2rrSLRRw1Wznyrj%2BL2YYzKbUSPG4nQduqnallwBl%2BykRkKaYoVRBnCYbZ42E5MiUwZ%2F7gcAVfswq60XzenfS4RtIWdsS854UVHjapwMo4LmTuhYpUqAJgtrXCNuRnjlKOJQsRJ0lzh45eCGI9tkFAoX5XZrvRwKvqFLpYl9a7nHZJHNj0Ac%2FtMcDpbuxsUSDe16TNmzA32GWBawEzvAAueryYXOV3ZujFAJXf5pM3a4UKKsx8QqHtCrbzcL5Uw34FiRibsAzibsAIABFoy79go1V68yAtfU7IQ9eovM4a8HlJ0fXYhnPWpD4WZ1B%2FZqMsd0%2Bnhd%2FzYyQWtfKt3XDlLTt16OPN1o%2BjFgvc%2FqdQz7yVJ2nOSLDUY2wuiVJIcPoIN9qdOv6Z8ELAtsnPiOQg1gLRzHD23lI%2BlReDHqMqIO8avsFrP5VnnEQYRreHZ4u34qBdHX1Q9h3OypVtNfrUAUfegrTupFgSVeuJVfdxlcMaJV1Xd0i8GaP6DPCDXYz7XhOvqhAA1rhKVRgUAztuIt7DyM1I07B5PWIpZEPMiu9MzK0wfhvyuIU2hMzQR%2FH0lwuRj9WWMbQagpTCVlPW8BjqkAYF4NfPTrboLLBqcwdOqeIETPydwq1LBa9CFg%2BpkvZQbYGw7QFh0Vw%2Fkj8FbzGuqN1RQ%2F0YUG12qzRanOWwpIg32tkg1OtHRIM3Py%2FCu2YsMYVsbKN3bv5eutsfg5kP2xeVU9FEOUg8s85xAb3AypU1%2Fh18JeXwk6qzAg3KkdnnSuGNmyDMrUeFGPebZStpg5eEtOiskeabov1xTsrwGaHXqGnEp&X-Amz-Signature=ee58ca6684ee53a16bf48cdccf978b7e81da34ba7f6b829335f528ccb3e5e392&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVYIGWKL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpLnbQ%2BhpQFFQEtLWiIfm7URJIAgqDmDtzg%2FcHcsaz1gIhAO3K%2FCw57vEPgFpWMSN1bcYDsBPqFf5ViEZj0IzxQ6YnKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzSCFqBzGHhqa3di4Aq3AN6AEUhqV1m3v%2BgKnyznB4k5jbmcryM1yy5PraHPlqkyz2rrSLRRw1Wznyrj%2BL2YYzKbUSPG4nQduqnallwBl%2BykRkKaYoVRBnCYbZ42E5MiUwZ%2F7gcAVfswq60XzenfS4RtIWdsS854UVHjapwMo4LmTuhYpUqAJgtrXCNuRnjlKOJQsRJ0lzh45eCGI9tkFAoX5XZrvRwKvqFLpYl9a7nHZJHNj0Ac%2FtMcDpbuxsUSDe16TNmzA32GWBawEzvAAueryYXOV3ZujFAJXf5pM3a4UKKsx8QqHtCrbzcL5Uw34FiRibsAzibsAIABFoy79go1V68yAtfU7IQ9eovM4a8HlJ0fXYhnPWpD4WZ1B%2FZqMsd0%2Bnhd%2FzYyQWtfKt3XDlLTt16OPN1o%2BjFgvc%2FqdQz7yVJ2nOSLDUY2wuiVJIcPoIN9qdOv6Z8ELAtsnPiOQg1gLRzHD23lI%2BlReDHqMqIO8avsFrP5VnnEQYRreHZ4u34qBdHX1Q9h3OypVtNfrUAUfegrTupFgSVeuJVfdxlcMaJV1Xd0i8GaP6DPCDXYz7XhOvqhAA1rhKVRgUAztuIt7DyM1I07B5PWIpZEPMiu9MzK0wfhvyuIU2hMzQR%2FH0lwuRj9WWMbQagpTCVlPW8BjqkAYF4NfPTrboLLBqcwdOqeIETPydwq1LBa9CFg%2BpkvZQbYGw7QFh0Vw%2Fkj8FbzGuqN1RQ%2F0YUG12qzRanOWwpIg32tkg1OtHRIM3Py%2FCu2YsMYVsbKN3bv5eutsfg5kP2xeVU9FEOUg8s85xAb3AypU1%2Fh18JeXwk6qzAg3KkdnnSuGNmyDMrUeFGPebZStpg5eEtOiskeabov1xTsrwGaHXqGnEp&X-Amz-Signature=800d48492d96b26f65cb3c8c740c6e7c74c4111f20f9bc713127cd7520e40c90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMN5KHC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeEMfto8AvOFmEaoxnqHSySyUOwevY57SHLuRBSCRGOAiEAh7XpYohhErCSY8CeQycWPv1U%2BSJISvXY4vV72BmPcjwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEhxEnxIYFRmp7RC5CrcA27coYm74EQP7cGnJ3Z%2FVz3sOr4%2F%2F31Gv6lafM1Zqike%2B0Z3vsWjwT00Gq90ciX7LFj%2Fbgn5HMDRBPMvEWASfyOBP4QAX6xY3LtkS3D1eXedMJ8TFkBu2BKx%2FiF7wvs4KUc4DCE1FZGps38TkXjLmDvCY04F%2FHkEzL0u41ehLD6hJt1P97GhXBKdWCAj2W8%2FfGaHSCe4LgcqVJaFT0A%2Ftpe3ELKwbVMRxiFfHXmIChQfsuMXMuSd8wUqRMU9Bk2gwb6RBwmn4fOXm902Q23jVI03OGU7vDVnZczr44%2BWEYcj7j0a8kH2W77zlYwDbVyNFva8CNs32FKP7hMqXXBDEYpZcmhsoyxmFvSge%2F4DmOcI%2BAvfO8fdu0cjXU4O5tOq3M0FbvPaEXTFpIk7vRtK%2BmXi39eXu6BHcZYiaWnCMm93ihd58rXJ0DgRNZfyoWqEV%2BsFteC9Jz04YZc7dy%2B0IwjoOxQ3k6wmqb73nAwcxwPiP7M9JQDk27YfICp9w2F1nxfCdloRLFUpsc1fMQ8%2FCPwEmx3QM3Tich%2FZMHz803XuT%2FPraUGsR%2FnImoUTOx8zPGchggdiKqzgV0Q%2FvrcFUI32%2BX4%2FZ2hwQFzi6iz7oCv82KhoSK5AsWFA1IGVMN2T9bwGOqUBRCEGUXF7nbNZ%2BSWywNSSIn6hZ6Jp1xTmMBg2yiu4tBx0flIN%2FHkU%2FUZdMvA7497ZpMUHr2MhcgNhlhpNVqcrquHd%2BLCXhjoNKPW8mLfhfD3vRmhnQKoG%2BxRRZmq9w6bUA%2Bjzq2kjyHvie0J6trn3o7uqzmVVSKS4PV4cugg0n0OMF1TWvZFICo5%2FLeWCPk%2FwUxtXfeFJ4Q9RCeESzWHiW5GCasZP&X-Amz-Signature=4f2951594df94b2364d1f2153c85e07a88262bfd01f2f9fda6862451c8e49ba4&X-Amz-SignedHeaders=host&x-id=GetObject)
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