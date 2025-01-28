

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6UN3Q32%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQCtdc3ztr2wJo1EjVOIiXrFwR7Q01dQMwMvj0LjW4Q5GAIgbPoDb7DPcospzVEJfiIVLYHlvyh3ngBMOkgXXQ3ERnAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIGIt0OTaAP7hGSGnCrcA0%2BUBvwZg0ynXhUtUdTxYCeL49zmQM4RJI9x9LPhSxLwNXnmnb9HE8aTx5LXva2C07pikUxkRASzz1KdTTVJgFYiLGZ5ANUjM0LiEwK5y2DDb38EDi1wnV5ywwlWSrB%2F6Yi00DcweenR%2FpQou9rHijt6uyZSWT5j7YMBcSq7oddUxCSQEnFrD%2FsuzGmiT8ZJUL3rWMCOGQlvuLmO2PLTYaPk6uCaIZOnSXNhYz3PTW5kC4gVgfWzsKK7tsD%2F7A%2Fsr0ampJH8GbpVZKjO3wuXV0avpzbBxgE4YN1NdCznnhABPEzSS6dAh109%2FVoJ8yfV7RnvDwn%2FHrW2ZCQBrZs6khqV5sW8Qn1RiBR2RsBtyJiQ6yfN4E4AcdLcJwQ6ejvt0VMUUVgUZ4%2F%2BMjscWx%2FC9Y%2B0aQaURoqMnT3k6B6unLRJdvJaxoINFrGWV8EvB%2BW5ZT9qYsHo5YkfabENr8zVmeusCgY1pYbh%2FYMO7QtouqTg11E%2FVCS5KITydfVzvNx9DWHkO0jySAWkLadT2rJnzN%2F2Ny4NVXhZVFG0Ht5%2B%2F%2BWuwu9kqiMYHRmiB3Y85fqhE4qZfrgv3k63SEn0xPp8K6Vg%2FLsePTc5KaPDDJ8hFvLs1rW0FUsLSuBuahbCMNuw5bwGOqUBPfrYdbsakdbS0scp62vtOre9qptKcd8%2BfWDmWkB5jm2r5I%2F8UrSNnAjdCh9jJdxLVRXdj3KPnbvbpRrsk27HrJc5tUdNLk%2BVDaaRvJPRP9TSZU7nOtDKz5jKzjhF93dZcr9HHZq2oSgcymMF%2FQtOKWMKmVs0Z3nXWR2cVbSsnNuHB2DOz0PmYYQDLczBBgPzNjWPT%2Bt%2FOy06M%2Fg%2BgwyQkTVziZtN&X-Amz-Signature=affd6cc2238ae5c58257a438c00f68b9bd6d03e17418bea0faaae0da7cb7a976&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6UN3Q32%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQCtdc3ztr2wJo1EjVOIiXrFwR7Q01dQMwMvj0LjW4Q5GAIgbPoDb7DPcospzVEJfiIVLYHlvyh3ngBMOkgXXQ3ERnAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIGIt0OTaAP7hGSGnCrcA0%2BUBvwZg0ynXhUtUdTxYCeL49zmQM4RJI9x9LPhSxLwNXnmnb9HE8aTx5LXva2C07pikUxkRASzz1KdTTVJgFYiLGZ5ANUjM0LiEwK5y2DDb38EDi1wnV5ywwlWSrB%2F6Yi00DcweenR%2FpQou9rHijt6uyZSWT5j7YMBcSq7oddUxCSQEnFrD%2FsuzGmiT8ZJUL3rWMCOGQlvuLmO2PLTYaPk6uCaIZOnSXNhYz3PTW5kC4gVgfWzsKK7tsD%2F7A%2Fsr0ampJH8GbpVZKjO3wuXV0avpzbBxgE4YN1NdCznnhABPEzSS6dAh109%2FVoJ8yfV7RnvDwn%2FHrW2ZCQBrZs6khqV5sW8Qn1RiBR2RsBtyJiQ6yfN4E4AcdLcJwQ6ejvt0VMUUVgUZ4%2F%2BMjscWx%2FC9Y%2B0aQaURoqMnT3k6B6unLRJdvJaxoINFrGWV8EvB%2BW5ZT9qYsHo5YkfabENr8zVmeusCgY1pYbh%2FYMO7QtouqTg11E%2FVCS5KITydfVzvNx9DWHkO0jySAWkLadT2rJnzN%2F2Ny4NVXhZVFG0Ht5%2B%2F%2BWuwu9kqiMYHRmiB3Y85fqhE4qZfrgv3k63SEn0xPp8K6Vg%2FLsePTc5KaPDDJ8hFvLs1rW0FUsLSuBuahbCMNuw5bwGOqUBPfrYdbsakdbS0scp62vtOre9qptKcd8%2BfWDmWkB5jm2r5I%2F8UrSNnAjdCh9jJdxLVRXdj3KPnbvbpRrsk27HrJc5tUdNLk%2BVDaaRvJPRP9TSZU7nOtDKz5jKzjhF93dZcr9HHZq2oSgcymMF%2FQtOKWMKmVs0Z3nXWR2cVbSsnNuHB2DOz0PmYYQDLczBBgPzNjWPT%2Bt%2FOy06M%2Fg%2BgwyQkTVziZtN&X-Amz-Signature=af4a259a839b216b5fc469b4af8f021cdf27b81ff4166f41b51e45cb681af557&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6UN3Q32%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQCtdc3ztr2wJo1EjVOIiXrFwR7Q01dQMwMvj0LjW4Q5GAIgbPoDb7DPcospzVEJfiIVLYHlvyh3ngBMOkgXXQ3ERnAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIGIt0OTaAP7hGSGnCrcA0%2BUBvwZg0ynXhUtUdTxYCeL49zmQM4RJI9x9LPhSxLwNXnmnb9HE8aTx5LXva2C07pikUxkRASzz1KdTTVJgFYiLGZ5ANUjM0LiEwK5y2DDb38EDi1wnV5ywwlWSrB%2F6Yi00DcweenR%2FpQou9rHijt6uyZSWT5j7YMBcSq7oddUxCSQEnFrD%2FsuzGmiT8ZJUL3rWMCOGQlvuLmO2PLTYaPk6uCaIZOnSXNhYz3PTW5kC4gVgfWzsKK7tsD%2F7A%2Fsr0ampJH8GbpVZKjO3wuXV0avpzbBxgE4YN1NdCznnhABPEzSS6dAh109%2FVoJ8yfV7RnvDwn%2FHrW2ZCQBrZs6khqV5sW8Qn1RiBR2RsBtyJiQ6yfN4E4AcdLcJwQ6ejvt0VMUUVgUZ4%2F%2BMjscWx%2FC9Y%2B0aQaURoqMnT3k6B6unLRJdvJaxoINFrGWV8EvB%2BW5ZT9qYsHo5YkfabENr8zVmeusCgY1pYbh%2FYMO7QtouqTg11E%2FVCS5KITydfVzvNx9DWHkO0jySAWkLadT2rJnzN%2F2Ny4NVXhZVFG0Ht5%2B%2F%2BWuwu9kqiMYHRmiB3Y85fqhE4qZfrgv3k63SEn0xPp8K6Vg%2FLsePTc5KaPDDJ8hFvLs1rW0FUsLSuBuahbCMNuw5bwGOqUBPfrYdbsakdbS0scp62vtOre9qptKcd8%2BfWDmWkB5jm2r5I%2F8UrSNnAjdCh9jJdxLVRXdj3KPnbvbpRrsk27HrJc5tUdNLk%2BVDaaRvJPRP9TSZU7nOtDKz5jKzjhF93dZcr9HHZq2oSgcymMF%2FQtOKWMKmVs0Z3nXWR2cVbSsnNuHB2DOz0PmYYQDLczBBgPzNjWPT%2Bt%2FOy06M%2Fg%2BgwyQkTVziZtN&X-Amz-Signature=c57334a4d792c3d3814c22dc64070ec1d03194a65386667c597d6f028c664509&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VXYVIJG%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQCH6wI3x9IKpdkMcRP028hsE1kMy%2FOZPBwLYC9pTGUSSQIgbSDp6h2GsNba7bYbkRzWpsiI19MDrWM2jFFtdyrHyuoq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOipC0UoMb7bCdVpjCrcA5uMTu1qPMQwc8Ti%2B41MXRoTCez0Izi2AhsMYRzBJeZ8x0ZsIU3Kr3exMCtlwfaV8S3Up92MpP0HkEioBcoRcKumkPle0coXe%2B7Y6Xrf%2BbB5LnxVi6mtTWg3Mfb%2F3PMw0ZrGErdyzXN0%2B%2BEauIIqBWAKuXtY5Uic6sYM5fTyXiHwaPIyofotJ9t4VIyL7KZdGKBNXfm7pFfpEJ4QE5KfSHN1qn%2FnBb1Q1kFQfoC8lPRPvug9IpC4nxm0bNuwfOOtMrNxrlFxrv68OkTTrm0JR4LoLu9u6GryV9MTgXOWnGeOcGrH1fPzM8eaCOBt2v%2B6l%2BK7qO4Im0LXEwe5vJdRi4bv%2FvKpNyCQ3oCfQEWA9hXDMczDTLeMWth5hNCc1JoB9APwN8yDsRlV6cdcae9gZHFcHktKuhgBlVbx98q3zFOz2dOQkRC0w7%2Bk4fcY4qsBvfMOAoIaI59ZFDYUFvjJ2zW8QG%2F9jV0r%2FZjD7r1E0BMZR8r5O5lGU1zSjBK2RNdvw7O4AcIeV8G1iZs6JuT3%2BzB4wNmn%2B8WXFMA710JbyePbWz0MNej%2FEramXXk7e9ApaV5aMSWfwIHRJ4DgYwDWFxtUkFlWGopTT7qisGkMs58kEqsK8DBGCMuitvMCMNuw5bwGOqUBUwOWfL0P7qiBnNYgErgEA8aszfK%2B2vXs6OxpCoHCkBrd9eJNbi2%2BpylWIWwCpLXWbuz%2F65LctGF8%2B%2Fq%2F22OMKx%2FpatDbUN6zTuiEjkrPYMTuTq4Zp6hnMQAoRbm78BBKv8JGTGRMRTbQ1dll4AuVMr8j9Ruepj8n9FA7wvJSNISfwLV79ojveQEa7z3P3AlRLieY8nZyWOkqofZ%2BsKkINxLB38ez&X-Amz-Signature=d3b7ed7a5d753f168b9d383ef4d9cc06a709643d64417dcf02c19f3a1ad11df5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VXYVIJG%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQCH6wI3x9IKpdkMcRP028hsE1kMy%2FOZPBwLYC9pTGUSSQIgbSDp6h2GsNba7bYbkRzWpsiI19MDrWM2jFFtdyrHyuoq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOipC0UoMb7bCdVpjCrcA5uMTu1qPMQwc8Ti%2B41MXRoTCez0Izi2AhsMYRzBJeZ8x0ZsIU3Kr3exMCtlwfaV8S3Up92MpP0HkEioBcoRcKumkPle0coXe%2B7Y6Xrf%2BbB5LnxVi6mtTWg3Mfb%2F3PMw0ZrGErdyzXN0%2B%2BEauIIqBWAKuXtY5Uic6sYM5fTyXiHwaPIyofotJ9t4VIyL7KZdGKBNXfm7pFfpEJ4QE5KfSHN1qn%2FnBb1Q1kFQfoC8lPRPvug9IpC4nxm0bNuwfOOtMrNxrlFxrv68OkTTrm0JR4LoLu9u6GryV9MTgXOWnGeOcGrH1fPzM8eaCOBt2v%2B6l%2BK7qO4Im0LXEwe5vJdRi4bv%2FvKpNyCQ3oCfQEWA9hXDMczDTLeMWth5hNCc1JoB9APwN8yDsRlV6cdcae9gZHFcHktKuhgBlVbx98q3zFOz2dOQkRC0w7%2Bk4fcY4qsBvfMOAoIaI59ZFDYUFvjJ2zW8QG%2F9jV0r%2FZjD7r1E0BMZR8r5O5lGU1zSjBK2RNdvw7O4AcIeV8G1iZs6JuT3%2BzB4wNmn%2B8WXFMA710JbyePbWz0MNej%2FEramXXk7e9ApaV5aMSWfwIHRJ4DgYwDWFxtUkFlWGopTT7qisGkMs58kEqsK8DBGCMuitvMCMNuw5bwGOqUBUwOWfL0P7qiBnNYgErgEA8aszfK%2B2vXs6OxpCoHCkBrd9eJNbi2%2BpylWIWwCpLXWbuz%2F65LctGF8%2B%2Fq%2F22OMKx%2FpatDbUN6zTuiEjkrPYMTuTq4Zp6hnMQAoRbm78BBKv8JGTGRMRTbQ1dll4AuVMr8j9Ruepj8n9FA7wvJSNISfwLV79ojveQEa7z3P3AlRLieY8nZyWOkqofZ%2BsKkINxLB38ez&X-Amz-Signature=13fe1adb13471c17f4f1fa19c9d5b217643fd558dfd267fd38651155c3c6766a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6UN3Q32%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIQCtdc3ztr2wJo1EjVOIiXrFwR7Q01dQMwMvj0LjW4Q5GAIgbPoDb7DPcospzVEJfiIVLYHlvyh3ngBMOkgXXQ3ERnAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDIGIt0OTaAP7hGSGnCrcA0%2BUBvwZg0ynXhUtUdTxYCeL49zmQM4RJI9x9LPhSxLwNXnmnb9HE8aTx5LXva2C07pikUxkRASzz1KdTTVJgFYiLGZ5ANUjM0LiEwK5y2DDb38EDi1wnV5ywwlWSrB%2F6Yi00DcweenR%2FpQou9rHijt6uyZSWT5j7YMBcSq7oddUxCSQEnFrD%2FsuzGmiT8ZJUL3rWMCOGQlvuLmO2PLTYaPk6uCaIZOnSXNhYz3PTW5kC4gVgfWzsKK7tsD%2F7A%2Fsr0ampJH8GbpVZKjO3wuXV0avpzbBxgE4YN1NdCznnhABPEzSS6dAh109%2FVoJ8yfV7RnvDwn%2FHrW2ZCQBrZs6khqV5sW8Qn1RiBR2RsBtyJiQ6yfN4E4AcdLcJwQ6ejvt0VMUUVgUZ4%2F%2BMjscWx%2FC9Y%2B0aQaURoqMnT3k6B6unLRJdvJaxoINFrGWV8EvB%2BW5ZT9qYsHo5YkfabENr8zVmeusCgY1pYbh%2FYMO7QtouqTg11E%2FVCS5KITydfVzvNx9DWHkO0jySAWkLadT2rJnzN%2F2Ny4NVXhZVFG0Ht5%2B%2F%2BWuwu9kqiMYHRmiB3Y85fqhE4qZfrgv3k63SEn0xPp8K6Vg%2FLsePTc5KaPDDJ8hFvLs1rW0FUsLSuBuahbCMNuw5bwGOqUBPfrYdbsakdbS0scp62vtOre9qptKcd8%2BfWDmWkB5jm2r5I%2F8UrSNnAjdCh9jJdxLVRXdj3KPnbvbpRrsk27HrJc5tUdNLk%2BVDaaRvJPRP9TSZU7nOtDKz5jKzjhF93dZcr9HHZq2oSgcymMF%2FQtOKWMKmVs0Z3nXWR2cVbSsnNuHB2DOz0PmYYQDLczBBgPzNjWPT%2Bt%2FOy06M%2Fg%2BgwyQkTVziZtN&X-Amz-Signature=22b310e5f1a386805a3f3193f9e5c07fad1a85ac1859d19576981e48c543ef99&X-Amz-SignedHeaders=host&x-id=GetObject)
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