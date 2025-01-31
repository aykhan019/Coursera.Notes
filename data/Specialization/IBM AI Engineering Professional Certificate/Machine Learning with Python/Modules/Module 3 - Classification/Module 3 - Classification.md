

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2Z5ZKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXxuGvfXQ5pw%2Fz97SLGdtT3NlOM3xVKs%2BsssMUND6YwgIgQDSIRJxJV6qKmraM98hocr7%2BQe02ix18ufuTfADXkAEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM7s2gJ0cCfEsr%2FM3SrcA%2F6CEyJh5lNvVfQXVkOnuudh5jmG1HKvmq841aQbOTxGSLnlV5SkQ4Y2fNncrYhVaH%2Fl33aIBh1bQ5S6YmAdqDLMXZN19uBWXIgNHimQ50WJZXKWtE9M%2F7EfCDnSkpIHEfExKEwHrEcV%2FBsg7aoz2xNdQ2SeEQtQZRmBOucYr5VMe63scE1cXvlpon4%2FLTQ8wpCRdCURVoWAYTuapZB7K4tmAovOkIPnZCAAtImRlO7qRQsUVEizYIe4Qiqkl3gwN%2FIqnF4sSBH%2Bz%2BWob92BTup%2Fh43lSvB9hrbts7RYe83BUlw7eQtEC2vLxhITGOp9f9d2Kpv6QMAGIVoxJWy5wcMgHHdSSyasHTVGQAqZR7iv7IAJtWQb890Uein8QYsxM%2FQUaon22KuZLMbaVXaYeirude3RexVeEqHMLugFL9MNUqAvcVZOBaP2RQzH3pczWqRZ1uD%2B7F%2FSKacC8swFgoXvUqmdzfoVfT8i0CFR8koFpXsdnyMwvjK60CrwOjL8yQUSjCe2HAPtIfmqf7W9iZsOgjYznzruvi%2F1f0SrBLnBz%2BliMxeNny1y%2Bjf1I0Bgj%2BGwDlHUdSWa8MXZu1ccPgeNkgAn%2FTFLJN1g5zmxRbBGXq9hYEDa4Ucmv8OGMJjQ8LwGOqUBfXqLbcvNpvjuPBRXRCL1IgGegGsYAWWCeEqrT9NfmBOKaOiIFaKiaHnKV4YhWf4wvq0QZT11Wwq%2BaQKN1C75nV5uBc4Vsdqs%2Bs6rxtn5%2F%2BXdHlCiDLRMmPt6v5hkrVoDVqEu4ymrsSGu6W3ZeGxjJE2pADtmFhH2u8zTauiO%2F0S0G4Bxyo419lFBmGb7Gu9blDvZ2dLhufomtlXiHVYtFGk0jXAW&X-Amz-Signature=845d5dd9d59665866109fe986d2e81f27c96fbea28f6835981631af045f3db95&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2Z5ZKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXxuGvfXQ5pw%2Fz97SLGdtT3NlOM3xVKs%2BsssMUND6YwgIgQDSIRJxJV6qKmraM98hocr7%2BQe02ix18ufuTfADXkAEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM7s2gJ0cCfEsr%2FM3SrcA%2F6CEyJh5lNvVfQXVkOnuudh5jmG1HKvmq841aQbOTxGSLnlV5SkQ4Y2fNncrYhVaH%2Fl33aIBh1bQ5S6YmAdqDLMXZN19uBWXIgNHimQ50WJZXKWtE9M%2F7EfCDnSkpIHEfExKEwHrEcV%2FBsg7aoz2xNdQ2SeEQtQZRmBOucYr5VMe63scE1cXvlpon4%2FLTQ8wpCRdCURVoWAYTuapZB7K4tmAovOkIPnZCAAtImRlO7qRQsUVEizYIe4Qiqkl3gwN%2FIqnF4sSBH%2Bz%2BWob92BTup%2Fh43lSvB9hrbts7RYe83BUlw7eQtEC2vLxhITGOp9f9d2Kpv6QMAGIVoxJWy5wcMgHHdSSyasHTVGQAqZR7iv7IAJtWQb890Uein8QYsxM%2FQUaon22KuZLMbaVXaYeirude3RexVeEqHMLugFL9MNUqAvcVZOBaP2RQzH3pczWqRZ1uD%2B7F%2FSKacC8swFgoXvUqmdzfoVfT8i0CFR8koFpXsdnyMwvjK60CrwOjL8yQUSjCe2HAPtIfmqf7W9iZsOgjYznzruvi%2F1f0SrBLnBz%2BliMxeNny1y%2Bjf1I0Bgj%2BGwDlHUdSWa8MXZu1ccPgeNkgAn%2FTFLJN1g5zmxRbBGXq9hYEDa4Ucmv8OGMJjQ8LwGOqUBfXqLbcvNpvjuPBRXRCL1IgGegGsYAWWCeEqrT9NfmBOKaOiIFaKiaHnKV4YhWf4wvq0QZT11Wwq%2BaQKN1C75nV5uBc4Vsdqs%2Bs6rxtn5%2F%2BXdHlCiDLRMmPt6v5hkrVoDVqEu4ymrsSGu6W3ZeGxjJE2pADtmFhH2u8zTauiO%2F0S0G4Bxyo419lFBmGb7Gu9blDvZ2dLhufomtlXiHVYtFGk0jXAW&X-Amz-Signature=7d869bfbe715c629619132f6877e0e7198e8a8d9cc45ab4911caa013ebeb7b30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2Z5ZKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXxuGvfXQ5pw%2Fz97SLGdtT3NlOM3xVKs%2BsssMUND6YwgIgQDSIRJxJV6qKmraM98hocr7%2BQe02ix18ufuTfADXkAEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM7s2gJ0cCfEsr%2FM3SrcA%2F6CEyJh5lNvVfQXVkOnuudh5jmG1HKvmq841aQbOTxGSLnlV5SkQ4Y2fNncrYhVaH%2Fl33aIBh1bQ5S6YmAdqDLMXZN19uBWXIgNHimQ50WJZXKWtE9M%2F7EfCDnSkpIHEfExKEwHrEcV%2FBsg7aoz2xNdQ2SeEQtQZRmBOucYr5VMe63scE1cXvlpon4%2FLTQ8wpCRdCURVoWAYTuapZB7K4tmAovOkIPnZCAAtImRlO7qRQsUVEizYIe4Qiqkl3gwN%2FIqnF4sSBH%2Bz%2BWob92BTup%2Fh43lSvB9hrbts7RYe83BUlw7eQtEC2vLxhITGOp9f9d2Kpv6QMAGIVoxJWy5wcMgHHdSSyasHTVGQAqZR7iv7IAJtWQb890Uein8QYsxM%2FQUaon22KuZLMbaVXaYeirude3RexVeEqHMLugFL9MNUqAvcVZOBaP2RQzH3pczWqRZ1uD%2B7F%2FSKacC8swFgoXvUqmdzfoVfT8i0CFR8koFpXsdnyMwvjK60CrwOjL8yQUSjCe2HAPtIfmqf7W9iZsOgjYznzruvi%2F1f0SrBLnBz%2BliMxeNny1y%2Bjf1I0Bgj%2BGwDlHUdSWa8MXZu1ccPgeNkgAn%2FTFLJN1g5zmxRbBGXq9hYEDa4Ucmv8OGMJjQ8LwGOqUBfXqLbcvNpvjuPBRXRCL1IgGegGsYAWWCeEqrT9NfmBOKaOiIFaKiaHnKV4YhWf4wvq0QZT11Wwq%2BaQKN1C75nV5uBc4Vsdqs%2Bs6rxtn5%2F%2BXdHlCiDLRMmPt6v5hkrVoDVqEu4ymrsSGu6W3ZeGxjJE2pADtmFhH2u8zTauiO%2F0S0G4Bxyo419lFBmGb7Gu9blDvZ2dLhufomtlXiHVYtFGk0jXAW&X-Amz-Signature=13024c5f713c7072f4fad3c63cce420417e736a383efcd04698af1f072615703&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSZ653I5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQComvzfOnOa93CWBx2TxBbYQDLw1qyiaAdQx05anbz3JAIgdtRVAa753wzKqsKqS%2B9I0CLUXxqk5ucPK95leuF6M7cqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCFgGspH3nAdMogyTircA9yLmudUy%2FV2zHj5aazKdwG%2FsknpurRWceRprzHuaJJTpWH7E0tLK8%2FcbahZrPb0gsJqrko%2FiEO3T7uVfGId7hvxeW3qamOco3wRk2%2BT%2FdLQ8YzA6H%2FgpeGQVHNG3C6qtUhnmk2saMxR0nE4RI6cOd38MIzFqeTV4oNj5LRIdHbNP%2BlFZsJA0k9lO%2FtCtGThFogcQXoM0VhjWFboSNhhODL%2BADApNMFG0UNXnyaYW%2BZ%2BbQMYwj%2FP2FC4t2ODlaWMOW1kw8j4IIcCdHj3kMklMXlycpo5Ggu%2BFXt2XHMtxdUHVx1PdF1vCzaeahQZe5lzyvChu3Iv0rXxq0mnrMOldA%2FqIkYIS%2BO7JJ0%2BRNccUisEH7mkClpdtozIJoAVZO9yEWDQByg6S1LiTxjhRh%2Bf2iOWtRcAcJWUIVvZK6k8kP93ayKkxvGcqYRmhCcg3tZOv2FRZi1onJ%2BPPLJQPbgjz6W1ns2FXkn%2B6kEkjw5sAtY9BLqGh9UfcWKftbmvNSk4NdMOKWw33s2cuEYMj07I%2FuS47pTcqDjln5p%2FpzmcVHHLofM8qAgpVvGwPZkUBxj0fl3Ilefh5JrrzyheKnNBUrLOPDA%2BYnkprYtiWXGrLG4kr8f%2BR3orC6I3MNhbMOLQ8LwGOqUBfv0er%2Bgru83e6OF2D6iiRRVvqJuFe%2FfQtvWb88zW2uY2ZTCl6ehXedOQdehxSJs22QcZ7Kl5A9HRsAjn5ZVbz%2BP6QmMcsazdHJGtcwlk1DdJnRwEBnG5WJAacfbZGsbMItHZW7p2irACaK5sy47VGeCHY6PNwY99MtuPEMvhW%2FWuc9Suff0es3wGsjEonx3REUCPH7IpIQ7xHUTwIeyiSpARw3my&X-Amz-Signature=cdbd7d11018b73cf123389d4d4ed94d8666c61c8ddc275e1f2612d1bbae46588&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSZ653I5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQComvzfOnOa93CWBx2TxBbYQDLw1qyiaAdQx05anbz3JAIgdtRVAa753wzKqsKqS%2B9I0CLUXxqk5ucPK95leuF6M7cqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCFgGspH3nAdMogyTircA9yLmudUy%2FV2zHj5aazKdwG%2FsknpurRWceRprzHuaJJTpWH7E0tLK8%2FcbahZrPb0gsJqrko%2FiEO3T7uVfGId7hvxeW3qamOco3wRk2%2BT%2FdLQ8YzA6H%2FgpeGQVHNG3C6qtUhnmk2saMxR0nE4RI6cOd38MIzFqeTV4oNj5LRIdHbNP%2BlFZsJA0k9lO%2FtCtGThFogcQXoM0VhjWFboSNhhODL%2BADApNMFG0UNXnyaYW%2BZ%2BbQMYwj%2FP2FC4t2ODlaWMOW1kw8j4IIcCdHj3kMklMXlycpo5Ggu%2BFXt2XHMtxdUHVx1PdF1vCzaeahQZe5lzyvChu3Iv0rXxq0mnrMOldA%2FqIkYIS%2BO7JJ0%2BRNccUisEH7mkClpdtozIJoAVZO9yEWDQByg6S1LiTxjhRh%2Bf2iOWtRcAcJWUIVvZK6k8kP93ayKkxvGcqYRmhCcg3tZOv2FRZi1onJ%2BPPLJQPbgjz6W1ns2FXkn%2B6kEkjw5sAtY9BLqGh9UfcWKftbmvNSk4NdMOKWw33s2cuEYMj07I%2FuS47pTcqDjln5p%2FpzmcVHHLofM8qAgpVvGwPZkUBxj0fl3Ilefh5JrrzyheKnNBUrLOPDA%2BYnkprYtiWXGrLG4kr8f%2BR3orC6I3MNhbMOLQ8LwGOqUBfv0er%2Bgru83e6OF2D6iiRRVvqJuFe%2FfQtvWb88zW2uY2ZTCl6ehXedOQdehxSJs22QcZ7Kl5A9HRsAjn5ZVbz%2BP6QmMcsazdHJGtcwlk1DdJnRwEBnG5WJAacfbZGsbMItHZW7p2irACaK5sy47VGeCHY6PNwY99MtuPEMvhW%2FWuc9Suff0es3wGsjEonx3REUCPH7IpIQ7xHUTwIeyiSpARw3my&X-Amz-Signature=c28517091b057a25be2d697a9b4e17ac2b2d63a577156c0e7553a07f607fa53e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2Z5ZKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXxuGvfXQ5pw%2Fz97SLGdtT3NlOM3xVKs%2BsssMUND6YwgIgQDSIRJxJV6qKmraM98hocr7%2BQe02ix18ufuTfADXkAEqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM7s2gJ0cCfEsr%2FM3SrcA%2F6CEyJh5lNvVfQXVkOnuudh5jmG1HKvmq841aQbOTxGSLnlV5SkQ4Y2fNncrYhVaH%2Fl33aIBh1bQ5S6YmAdqDLMXZN19uBWXIgNHimQ50WJZXKWtE9M%2F7EfCDnSkpIHEfExKEwHrEcV%2FBsg7aoz2xNdQ2SeEQtQZRmBOucYr5VMe63scE1cXvlpon4%2FLTQ8wpCRdCURVoWAYTuapZB7K4tmAovOkIPnZCAAtImRlO7qRQsUVEizYIe4Qiqkl3gwN%2FIqnF4sSBH%2Bz%2BWob92BTup%2Fh43lSvB9hrbts7RYe83BUlw7eQtEC2vLxhITGOp9f9d2Kpv6QMAGIVoxJWy5wcMgHHdSSyasHTVGQAqZR7iv7IAJtWQb890Uein8QYsxM%2FQUaon22KuZLMbaVXaYeirude3RexVeEqHMLugFL9MNUqAvcVZOBaP2RQzH3pczWqRZ1uD%2B7F%2FSKacC8swFgoXvUqmdzfoVfT8i0CFR8koFpXsdnyMwvjK60CrwOjL8yQUSjCe2HAPtIfmqf7W9iZsOgjYznzruvi%2F1f0SrBLnBz%2BliMxeNny1y%2Bjf1I0Bgj%2BGwDlHUdSWa8MXZu1ccPgeNkgAn%2FTFLJN1g5zmxRbBGXq9hYEDa4Ucmv8OGMJjQ8LwGOqUBfXqLbcvNpvjuPBRXRCL1IgGegGsYAWWCeEqrT9NfmBOKaOiIFaKiaHnKV4YhWf4wvq0QZT11Wwq%2BaQKN1C75nV5uBc4Vsdqs%2Bs6rxtn5%2F%2BXdHlCiDLRMmPt6v5hkrVoDVqEu4ymrsSGu6W3ZeGxjJE2pADtmFhH2u8zTauiO%2F0S0G4Bxyo419lFBmGb7Gu9blDvZ2dLhufomtlXiHVYtFGk0jXAW&X-Amz-Signature=e943bdab02e17874f166e3c3789125dbb7ab1d5bfdc4ce1f040c54e16523e097&X-Amz-SignedHeaders=host&x-id=GetObject)
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