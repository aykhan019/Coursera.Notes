

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNXPB2PJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrVLRmwTQhmg8yRxhNuiPJCpwpaRahUpoTwRL184VTTAiBsxrpUiQ268pyzokbpNaUFPZDzwzVyjdHwzHuGXdJh%2BSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMS%2F%2Bmjcgag1vgMiouKtwDrbUPnZZrqcpIYreb34FNjDmZTexi45QT%2B94HvOPLhswu0blZYSaGensoVqkVHUD%2FYyiegg%2FacRl2scaOokFAL5q1eO1b1XKast6rNh0p3BkgdlmbB4cpryq5GMUVGAQ%2BmPxSZNqd8YCOsrzA%2BwSrBocNm6WgDbqcIctyX5M3Fd87qwb%2BJiHMop2KqiFsdxRdzggIWysVHNTLtwimaQKP43YON0TblM%2BJGzRFMvJg1yCmzwfRMkDLBT4ZePUOqCVSZMSY2zSHXiH%2FviODvj7gWfkLzsQGPjeG%2Fr0aZJxXxCZTUS5GbwLlHwr0ZhQB82r2ZdQFbbbydKuUf2UIJlb5tKbqGiLlPwR0UU%2Bjh3xeivftvFqK9HhJqUYDNOmnd69TWy%2FB9RJQP%2F%2FSl6DxM3IBowbJG0rZFuqrVPF5AmHXhaKxUpPYfeP1aXh%2Btr9kekzG%2F9%2Bf%2BEVvgVvKHMLYuEA9UxmHZn7P%2FbErTSNjDu09Tek9EXO89MJy%2Bn7K2wzX%2BqPwoPBBMiYmamFiXnPPI8xeM%2BzqtfmBTgHzsjt6tHoz8qZc7vRrXv0jf%2F6yF2qx6rZ84BARKAjpsUQA4oBsDARYL6%2FkE9gKXSy6trzXWJ1X45tUTj2W1gpw84MRpuAw65v8vAY6pgHT5Myen%2Bg04G96SPIOLwfWI4pbshbsXT5EWNXOO9cyNUWVCNsFvT4dnLbXV%2FPZWG6WH%2FJaN7C1JysZ43PcYGT9lMyDwuuVr4GJrX9PLFiU%2FOycCYLSnMG8iyJwGf9VHEuy3ZwDC3hf8zSGOvREFiHa4MsXJU3R9yCfYhn4Vb7GFYiGgJO%2B7I%2Fb5kTsn7W0tyQbSKZ7d5vMHspu4m5VEypA87dZG%2Fhc&X-Amz-Signature=5b360d0970bdc98119200c9dcf99e5cfc8a1d7a3350a2dc01124d487380e826d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNXPB2PJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrVLRmwTQhmg8yRxhNuiPJCpwpaRahUpoTwRL184VTTAiBsxrpUiQ268pyzokbpNaUFPZDzwzVyjdHwzHuGXdJh%2BSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMS%2F%2Bmjcgag1vgMiouKtwDrbUPnZZrqcpIYreb34FNjDmZTexi45QT%2B94HvOPLhswu0blZYSaGensoVqkVHUD%2FYyiegg%2FacRl2scaOokFAL5q1eO1b1XKast6rNh0p3BkgdlmbB4cpryq5GMUVGAQ%2BmPxSZNqd8YCOsrzA%2BwSrBocNm6WgDbqcIctyX5M3Fd87qwb%2BJiHMop2KqiFsdxRdzggIWysVHNTLtwimaQKP43YON0TblM%2BJGzRFMvJg1yCmzwfRMkDLBT4ZePUOqCVSZMSY2zSHXiH%2FviODvj7gWfkLzsQGPjeG%2Fr0aZJxXxCZTUS5GbwLlHwr0ZhQB82r2ZdQFbbbydKuUf2UIJlb5tKbqGiLlPwR0UU%2Bjh3xeivftvFqK9HhJqUYDNOmnd69TWy%2FB9RJQP%2F%2FSl6DxM3IBowbJG0rZFuqrVPF5AmHXhaKxUpPYfeP1aXh%2Btr9kekzG%2F9%2Bf%2BEVvgVvKHMLYuEA9UxmHZn7P%2FbErTSNjDu09Tek9EXO89MJy%2Bn7K2wzX%2BqPwoPBBMiYmamFiXnPPI8xeM%2BzqtfmBTgHzsjt6tHoz8qZc7vRrXv0jf%2F6yF2qx6rZ84BARKAjpsUQA4oBsDARYL6%2FkE9gKXSy6trzXWJ1X45tUTj2W1gpw84MRpuAw65v8vAY6pgHT5Myen%2Bg04G96SPIOLwfWI4pbshbsXT5EWNXOO9cyNUWVCNsFvT4dnLbXV%2FPZWG6WH%2FJaN7C1JysZ43PcYGT9lMyDwuuVr4GJrX9PLFiU%2FOycCYLSnMG8iyJwGf9VHEuy3ZwDC3hf8zSGOvREFiHa4MsXJU3R9yCfYhn4Vb7GFYiGgJO%2B7I%2Fb5kTsn7W0tyQbSKZ7d5vMHspu4m5VEypA87dZG%2Fhc&X-Amz-Signature=7d4cff3221630aa8e6cf46e2c41bea465a1e1b8f2b1d397a7f15893d58ae408a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNXPB2PJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrVLRmwTQhmg8yRxhNuiPJCpwpaRahUpoTwRL184VTTAiBsxrpUiQ268pyzokbpNaUFPZDzwzVyjdHwzHuGXdJh%2BSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMS%2F%2Bmjcgag1vgMiouKtwDrbUPnZZrqcpIYreb34FNjDmZTexi45QT%2B94HvOPLhswu0blZYSaGensoVqkVHUD%2FYyiegg%2FacRl2scaOokFAL5q1eO1b1XKast6rNh0p3BkgdlmbB4cpryq5GMUVGAQ%2BmPxSZNqd8YCOsrzA%2BwSrBocNm6WgDbqcIctyX5M3Fd87qwb%2BJiHMop2KqiFsdxRdzggIWysVHNTLtwimaQKP43YON0TblM%2BJGzRFMvJg1yCmzwfRMkDLBT4ZePUOqCVSZMSY2zSHXiH%2FviODvj7gWfkLzsQGPjeG%2Fr0aZJxXxCZTUS5GbwLlHwr0ZhQB82r2ZdQFbbbydKuUf2UIJlb5tKbqGiLlPwR0UU%2Bjh3xeivftvFqK9HhJqUYDNOmnd69TWy%2FB9RJQP%2F%2FSl6DxM3IBowbJG0rZFuqrVPF5AmHXhaKxUpPYfeP1aXh%2Btr9kekzG%2F9%2Bf%2BEVvgVvKHMLYuEA9UxmHZn7P%2FbErTSNjDu09Tek9EXO89MJy%2Bn7K2wzX%2BqPwoPBBMiYmamFiXnPPI8xeM%2BzqtfmBTgHzsjt6tHoz8qZc7vRrXv0jf%2F6yF2qx6rZ84BARKAjpsUQA4oBsDARYL6%2FkE9gKXSy6trzXWJ1X45tUTj2W1gpw84MRpuAw65v8vAY6pgHT5Myen%2Bg04G96SPIOLwfWI4pbshbsXT5EWNXOO9cyNUWVCNsFvT4dnLbXV%2FPZWG6WH%2FJaN7C1JysZ43PcYGT9lMyDwuuVr4GJrX9PLFiU%2FOycCYLSnMG8iyJwGf9VHEuy3ZwDC3hf8zSGOvREFiHa4MsXJU3R9yCfYhn4Vb7GFYiGgJO%2B7I%2Fb5kTsn7W0tyQbSKZ7d5vMHspu4m5VEypA87dZG%2Fhc&X-Amz-Signature=658abcb565f750f493fb361e84cf7543e4d175717246e90e20fbdd9bca0ccfac&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2TW3C7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCGcK7mg%2BQAzaqfUo3tqZ93TOuCDb4e%2BFyf66n8optS2QIgW2kLLnKB2TQbmxKjzdFaIWgZiSYwZdQjVs5ce4YJK2UqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKd4SQ2dnG6CNUxs%2FyrcA5ykwlRKOt%2F%2FmPQKl7esxSKpasH5ckG3GVepQCr2epjNjz1hVDvlDkUJARmVFQrVbtC1OnNXapWIpA%2FhXxLReF%2F%2Bn0FqemZ0KS%2BL6Fe%2FGcxmHtyy1Hot1FV%2ByptCQePq91SaNdMwNebLHNC6Ry4dknkQj307ALop1SuShXQE40eUhuDUAdgE7e2wIp9GDwxCX3zugL49aSWrWau2pLvNHP%2BY%2Bh7%2B3C%2FgB6ZXJLqc2Rnwobaxqij0YLPQ%2Fw7%2B1M2fwGhOR8hbD0Yq%2F8aFkIBIFfRJrkxkrLi5pOO6V1Ic0zJuSeQ4vkvClbSBRGhQbkLNT2G1IWobnqkhRRvhDu94nCFVgktMzitXqykkZkXeFo2phpZAJ8ec0dHXl%2FgYZEhibB3DACp%2FXFBOxqYyiaTAfh5j%2Fe5JNeh0uW3NSPqLgA%2FCBgztpXYGQuyCfTjiuzGxBpB%2BwPWxy33o59koMP8FPv48U%2BJDw9l94acdz5LzTOJAQztG9gYb5PcrRFJCyThGumXWiWN0W5QIaUpNjj5bHVZJJ6lNZtWRfBMircpJq9z4VAusoccyBXYBGwct3sift34XkJl6AQHMHkW982sX3bQjshYvH%2BQpDWgJ6AgApB30m9nds%2F1sZYFA6%2FtYMM%2Bb%2FLwGOqUB2bdkjEa9Bx52DaaimubS9DMGlw8yu%2FOYqO6NCrFS1Z2ffPei8ZWVn2x2nZJY58DswtF0F8DTpZVUHLAt7BKfOafxBlQrWicaYVWB1Bty3Mmr0nhaiavFLjP5eWHWRoMvCwIXXbtwAwmqx0L8eaXXXW8KR%2BXXj4m5JgXCpjW4buq8dX6o7GDwrTvAButEMIeYWb26rROjBO%2BL0nITa4hKYEycOttg&X-Amz-Signature=95e7b0ad37dd4d06f1a1c53f4f914d077a632396decff0720de973d826fbcd11&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ2TW3C7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCGcK7mg%2BQAzaqfUo3tqZ93TOuCDb4e%2BFyf66n8optS2QIgW2kLLnKB2TQbmxKjzdFaIWgZiSYwZdQjVs5ce4YJK2UqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKd4SQ2dnG6CNUxs%2FyrcA5ykwlRKOt%2F%2FmPQKl7esxSKpasH5ckG3GVepQCr2epjNjz1hVDvlDkUJARmVFQrVbtC1OnNXapWIpA%2FhXxLReF%2F%2Bn0FqemZ0KS%2BL6Fe%2FGcxmHtyy1Hot1FV%2ByptCQePq91SaNdMwNebLHNC6Ry4dknkQj307ALop1SuShXQE40eUhuDUAdgE7e2wIp9GDwxCX3zugL49aSWrWau2pLvNHP%2BY%2Bh7%2B3C%2FgB6ZXJLqc2Rnwobaxqij0YLPQ%2Fw7%2B1M2fwGhOR8hbD0Yq%2F8aFkIBIFfRJrkxkrLi5pOO6V1Ic0zJuSeQ4vkvClbSBRGhQbkLNT2G1IWobnqkhRRvhDu94nCFVgktMzitXqykkZkXeFo2phpZAJ8ec0dHXl%2FgYZEhibB3DACp%2FXFBOxqYyiaTAfh5j%2Fe5JNeh0uW3NSPqLgA%2FCBgztpXYGQuyCfTjiuzGxBpB%2BwPWxy33o59koMP8FPv48U%2BJDw9l94acdz5LzTOJAQztG9gYb5PcrRFJCyThGumXWiWN0W5QIaUpNjj5bHVZJJ6lNZtWRfBMircpJq9z4VAusoccyBXYBGwct3sift34XkJl6AQHMHkW982sX3bQjshYvH%2BQpDWgJ6AgApB30m9nds%2F1sZYFA6%2FtYMM%2Bb%2FLwGOqUB2bdkjEa9Bx52DaaimubS9DMGlw8yu%2FOYqO6NCrFS1Z2ffPei8ZWVn2x2nZJY58DswtF0F8DTpZVUHLAt7BKfOafxBlQrWicaYVWB1Bty3Mmr0nhaiavFLjP5eWHWRoMvCwIXXbtwAwmqx0L8eaXXXW8KR%2BXXj4m5JgXCpjW4buq8dX6o7GDwrTvAButEMIeYWb26rROjBO%2BL0nITa4hKYEycOttg&X-Amz-Signature=14eb2e6b9871d031bdac500f50b163f0c50f5297f1dd33dbd673b3fffcc987d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNXPB2PJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrVLRmwTQhmg8yRxhNuiPJCpwpaRahUpoTwRL184VTTAiBsxrpUiQ268pyzokbpNaUFPZDzwzVyjdHwzHuGXdJh%2BSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMS%2F%2Bmjcgag1vgMiouKtwDrbUPnZZrqcpIYreb34FNjDmZTexi45QT%2B94HvOPLhswu0blZYSaGensoVqkVHUD%2FYyiegg%2FacRl2scaOokFAL5q1eO1b1XKast6rNh0p3BkgdlmbB4cpryq5GMUVGAQ%2BmPxSZNqd8YCOsrzA%2BwSrBocNm6WgDbqcIctyX5M3Fd87qwb%2BJiHMop2KqiFsdxRdzggIWysVHNTLtwimaQKP43YON0TblM%2BJGzRFMvJg1yCmzwfRMkDLBT4ZePUOqCVSZMSY2zSHXiH%2FviODvj7gWfkLzsQGPjeG%2Fr0aZJxXxCZTUS5GbwLlHwr0ZhQB82r2ZdQFbbbydKuUf2UIJlb5tKbqGiLlPwR0UU%2Bjh3xeivftvFqK9HhJqUYDNOmnd69TWy%2FB9RJQP%2F%2FSl6DxM3IBowbJG0rZFuqrVPF5AmHXhaKxUpPYfeP1aXh%2Btr9kekzG%2F9%2Bf%2BEVvgVvKHMLYuEA9UxmHZn7P%2FbErTSNjDu09Tek9EXO89MJy%2Bn7K2wzX%2BqPwoPBBMiYmamFiXnPPI8xeM%2BzqtfmBTgHzsjt6tHoz8qZc7vRrXv0jf%2F6yF2qx6rZ84BARKAjpsUQA4oBsDARYL6%2FkE9gKXSy6trzXWJ1X45tUTj2W1gpw84MRpuAw65v8vAY6pgHT5Myen%2Bg04G96SPIOLwfWI4pbshbsXT5EWNXOO9cyNUWVCNsFvT4dnLbXV%2FPZWG6WH%2FJaN7C1JysZ43PcYGT9lMyDwuuVr4GJrX9PLFiU%2FOycCYLSnMG8iyJwGf9VHEuy3ZwDC3hf8zSGOvREFiHa4MsXJU3R9yCfYhn4Vb7GFYiGgJO%2B7I%2Fb5kTsn7W0tyQbSKZ7d5vMHspu4m5VEypA87dZG%2Fhc&X-Amz-Signature=258321ee75210bb0c5a9456bc8c024c081187372f3703e0c26d134a77cb6074f&X-Amz-SignedHeaders=host&x-id=GetObject)
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