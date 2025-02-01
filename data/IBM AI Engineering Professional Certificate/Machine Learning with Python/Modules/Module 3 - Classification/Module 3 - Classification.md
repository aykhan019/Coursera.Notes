

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXU466E3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBeM7Svd5zZCghjY%2BuzAbWAaDfx5VC96qcFMQ2%2Bpufy5AiEAgYZVetBrNaAJ7VXcnHxk3bb5t8TQcAq1uNMRhGYGUYwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGS8TbopPfu3V%2B%2BVzCrcA65dk%2B%2FYMeZ38tf%2FA92%2BPsdAP19Ww1fkqqaxTYKLSP9wNgfrH0Iqh1NsyRHg3DCI3yyT4cSFY9eOAwbazlezSYtw3NfjTBAY7pMDLj%2F6rMgMuJF5vmBBfd6Q5SI%2BdmB61twCt6bwgiPRm5yo%2FzcImtcBS3YxJIXx1N6a3bODOgmh%2BlT%2Foi57Q2WYqCdpNQpfDAkg2rU1KaSY5PAsZHz9V4JuygAlkUUk1pDFvjhtpqmxUWGIyux%2FPi%2B%2FksI3FcCACyxosCuzou1mo%2BFxzv81FRekPL52eBSgNMkWHnM6Z0VEXa6zrpr%2BZT43UXumsGI1rFT%2FPbbPihLoICeme7g7djMP9oZPxqE1HO6f2kXjBweI%2FEiknIr70oMdEbmC52RHtPQlKR5IEVEQY5d%2BAHNS4zRRdAbUiW32ZB1HZFueENaMdJly6rEwCaJMTKsHa4X8loIRAsGJiJN%2FfNiDatxtNsQzgfIFtLDbpR4YoXwkxb995k3MX%2BSbdgy57Xymvb0UeYfHqlgKigtJHQr4e4xInMx2B7dKipWI0exHguiKlDZ7LozvBit6jQjeVK%2Fdr4NM2ioYrWVtFsYymQxlFKe%2BncnOri%2FvB3Wf60ner%2F31bL12Tzx9BpkAjl0%2FVpG3MNKk97wGOqUBb3DVKOG5tXrKXWBT6BMaV%2BnqJ0uzLaNSjp335xxAuTvQxN0w%2FgMrDPQYKt3p47rA8qENvsiQeifvd7la25eUJRCVEznVsIO8cPfM6wpA%2B9EWtJzHZk9Pu%2BqrTR24izEd88HSpTwe1DZwEShTlUpPwcApdGudyhnMH%2Bs6zXUyltu5d2UxhuKpTr14vKYxzztxoKxXiaZYct%2BjR98YYzBtsJ32XOpQ&X-Amz-Signature=8a7281e7ebc4f2697ff8565dd7db503e776ce4eb651691da398b23ddcf187011&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXU466E3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBeM7Svd5zZCghjY%2BuzAbWAaDfx5VC96qcFMQ2%2Bpufy5AiEAgYZVetBrNaAJ7VXcnHxk3bb5t8TQcAq1uNMRhGYGUYwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGS8TbopPfu3V%2B%2BVzCrcA65dk%2B%2FYMeZ38tf%2FA92%2BPsdAP19Ww1fkqqaxTYKLSP9wNgfrH0Iqh1NsyRHg3DCI3yyT4cSFY9eOAwbazlezSYtw3NfjTBAY7pMDLj%2F6rMgMuJF5vmBBfd6Q5SI%2BdmB61twCt6bwgiPRm5yo%2FzcImtcBS3YxJIXx1N6a3bODOgmh%2BlT%2Foi57Q2WYqCdpNQpfDAkg2rU1KaSY5PAsZHz9V4JuygAlkUUk1pDFvjhtpqmxUWGIyux%2FPi%2B%2FksI3FcCACyxosCuzou1mo%2BFxzv81FRekPL52eBSgNMkWHnM6Z0VEXa6zrpr%2BZT43UXumsGI1rFT%2FPbbPihLoICeme7g7djMP9oZPxqE1HO6f2kXjBweI%2FEiknIr70oMdEbmC52RHtPQlKR5IEVEQY5d%2BAHNS4zRRdAbUiW32ZB1HZFueENaMdJly6rEwCaJMTKsHa4X8loIRAsGJiJN%2FfNiDatxtNsQzgfIFtLDbpR4YoXwkxb995k3MX%2BSbdgy57Xymvb0UeYfHqlgKigtJHQr4e4xInMx2B7dKipWI0exHguiKlDZ7LozvBit6jQjeVK%2Fdr4NM2ioYrWVtFsYymQxlFKe%2BncnOri%2FvB3Wf60ner%2F31bL12Tzx9BpkAjl0%2FVpG3MNKk97wGOqUBb3DVKOG5tXrKXWBT6BMaV%2BnqJ0uzLaNSjp335xxAuTvQxN0w%2FgMrDPQYKt3p47rA8qENvsiQeifvd7la25eUJRCVEznVsIO8cPfM6wpA%2B9EWtJzHZk9Pu%2BqrTR24izEd88HSpTwe1DZwEShTlUpPwcApdGudyhnMH%2Bs6zXUyltu5d2UxhuKpTr14vKYxzztxoKxXiaZYct%2BjR98YYzBtsJ32XOpQ&X-Amz-Signature=7204de6eb82620129f68120059ea686ee155fa501b2648b6393bc02cfd739320&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXU466E3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBeM7Svd5zZCghjY%2BuzAbWAaDfx5VC96qcFMQ2%2Bpufy5AiEAgYZVetBrNaAJ7VXcnHxk3bb5t8TQcAq1uNMRhGYGUYwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGS8TbopPfu3V%2B%2BVzCrcA65dk%2B%2FYMeZ38tf%2FA92%2BPsdAP19Ww1fkqqaxTYKLSP9wNgfrH0Iqh1NsyRHg3DCI3yyT4cSFY9eOAwbazlezSYtw3NfjTBAY7pMDLj%2F6rMgMuJF5vmBBfd6Q5SI%2BdmB61twCt6bwgiPRm5yo%2FzcImtcBS3YxJIXx1N6a3bODOgmh%2BlT%2Foi57Q2WYqCdpNQpfDAkg2rU1KaSY5PAsZHz9V4JuygAlkUUk1pDFvjhtpqmxUWGIyux%2FPi%2B%2FksI3FcCACyxosCuzou1mo%2BFxzv81FRekPL52eBSgNMkWHnM6Z0VEXa6zrpr%2BZT43UXumsGI1rFT%2FPbbPihLoICeme7g7djMP9oZPxqE1HO6f2kXjBweI%2FEiknIr70oMdEbmC52RHtPQlKR5IEVEQY5d%2BAHNS4zRRdAbUiW32ZB1HZFueENaMdJly6rEwCaJMTKsHa4X8loIRAsGJiJN%2FfNiDatxtNsQzgfIFtLDbpR4YoXwkxb995k3MX%2BSbdgy57Xymvb0UeYfHqlgKigtJHQr4e4xInMx2B7dKipWI0exHguiKlDZ7LozvBit6jQjeVK%2Fdr4NM2ioYrWVtFsYymQxlFKe%2BncnOri%2FvB3Wf60ner%2F31bL12Tzx9BpkAjl0%2FVpG3MNKk97wGOqUBb3DVKOG5tXrKXWBT6BMaV%2BnqJ0uzLaNSjp335xxAuTvQxN0w%2FgMrDPQYKt3p47rA8qENvsiQeifvd7la25eUJRCVEznVsIO8cPfM6wpA%2B9EWtJzHZk9Pu%2BqrTR24izEd88HSpTwe1DZwEShTlUpPwcApdGudyhnMH%2Bs6zXUyltu5d2UxhuKpTr14vKYxzztxoKxXiaZYct%2BjR98YYzBtsJ32XOpQ&X-Amz-Signature=e63d96f7bb4209134c3601c3b170221c187ff93210d5dd6fccd866b7dc1b4a1c&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665IMU4Q4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0kovSG6DpZgxJ%2B0THkHRhvoraaUkEILhPYqJKQEoHCAiBTcy2SsrFeSOUIW%2B0MTYfJoA9%2FKfnJ7xWB4MWszaWu%2FiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF48tFv9cfcBRvibxKtwDemgkCJwCL6QaU6GoRbhMG4KuEKdsaJGU5wyU7Ej3FWR3cH%2BOEKzp7xkXSYZVi8ITUIiXecbrSlHCOV08TWo0qI%2B%2FYz1yGTXW%2B1xFkfwd5bbr7Z5MZaskSefHukj%2F2nOshlnwpP%2F0x%2FrEB%2FoUmaj92U75rYzEpNUjVr0EI8jBaX%2B9iakiw4gV87I8HowTsGKXGFnKymcu7N7g7k968SLY7veBKbcAZrhxc%2FuqBat31icD4h%2BXPuMjkkixSrklB0UBw0yoPcu%2FcJbME0iNH%2FjaBxFWuWmBC8rHo8Qv55V4SGD6Z%2FZFAsIe0c67MNm9XO4vjmZYaogodX77pJO9teQde0X9byqT5pt7IeVz4kFZOpUlj8ttdRDkqNJ1JOEtb4qbTLUHaEvZqm%2FXSjj21dFS5Zy1ke0cZCtzMhiTcVroloD7J2waFZLgnofkVPB0Vi%2FXw11ZWMF2V2MtF0%2FkMc1YHe1JrtGSBjpSXsSQ6ssKAWSBHaMUyTO2YX9nAxEpc1crVFvnVKsUTjFv7xvhlLHQLSKpCjD%2BnN1JwRsHhB2eAhxbOhGEH6Lk3tQwdBgvk4Xsg3fx%2BCfiXYKhFnLA%2B8V4enkT0Axd0TJcboCV0AwmIWWZihJDiHMJH7nzTAcwx6T3vAY6pgFKGV6iFEUeJRINdBqUN8%2BwylVVXrmj8NRKnUPrD6y9Ww4U6%2B1EW1f6ZwULU64qauDDqHWyegB9ujfB2W2GGJKzkl3QASl3AdcjQjt%2BXVM%2BoHC627N9upkb3WDbT7NaBAJ5tAHktSAxTDfwQ2h5LZvxaRntaazgq2ZrLWfQ2IyQyE0HZqUY8znyxEFEWoM9u%2FLQq7ZQuO5NroZd2prasYvwMEQDhUA%2B&X-Amz-Signature=8c40b0a34ae08b13fb6453234f196f1d5f12c35b3ff42aa457557edbefdb45a6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665IMU4Q4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0kovSG6DpZgxJ%2B0THkHRhvoraaUkEILhPYqJKQEoHCAiBTcy2SsrFeSOUIW%2B0MTYfJoA9%2FKfnJ7xWB4MWszaWu%2FiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF48tFv9cfcBRvibxKtwDemgkCJwCL6QaU6GoRbhMG4KuEKdsaJGU5wyU7Ej3FWR3cH%2BOEKzp7xkXSYZVi8ITUIiXecbrSlHCOV08TWo0qI%2B%2FYz1yGTXW%2B1xFkfwd5bbr7Z5MZaskSefHukj%2F2nOshlnwpP%2F0x%2FrEB%2FoUmaj92U75rYzEpNUjVr0EI8jBaX%2B9iakiw4gV87I8HowTsGKXGFnKymcu7N7g7k968SLY7veBKbcAZrhxc%2FuqBat31icD4h%2BXPuMjkkixSrklB0UBw0yoPcu%2FcJbME0iNH%2FjaBxFWuWmBC8rHo8Qv55V4SGD6Z%2FZFAsIe0c67MNm9XO4vjmZYaogodX77pJO9teQde0X9byqT5pt7IeVz4kFZOpUlj8ttdRDkqNJ1JOEtb4qbTLUHaEvZqm%2FXSjj21dFS5Zy1ke0cZCtzMhiTcVroloD7J2waFZLgnofkVPB0Vi%2FXw11ZWMF2V2MtF0%2FkMc1YHe1JrtGSBjpSXsSQ6ssKAWSBHaMUyTO2YX9nAxEpc1crVFvnVKsUTjFv7xvhlLHQLSKpCjD%2BnN1JwRsHhB2eAhxbOhGEH6Lk3tQwdBgvk4Xsg3fx%2BCfiXYKhFnLA%2B8V4enkT0Axd0TJcboCV0AwmIWWZihJDiHMJH7nzTAcwx6T3vAY6pgFKGV6iFEUeJRINdBqUN8%2BwylVVXrmj8NRKnUPrD6y9Ww4U6%2B1EW1f6ZwULU64qauDDqHWyegB9ujfB2W2GGJKzkl3QASl3AdcjQjt%2BXVM%2BoHC627N9upkb3WDbT7NaBAJ5tAHktSAxTDfwQ2h5LZvxaRntaazgq2ZrLWfQ2IyQyE0HZqUY8znyxEFEWoM9u%2FLQq7ZQuO5NroZd2prasYvwMEQDhUA%2B&X-Amz-Signature=cdbb0d9fceb077be89557e21d86ced7b542f5110d90a011808d9bbfd8d01bd09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXU466E3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBeM7Svd5zZCghjY%2BuzAbWAaDfx5VC96qcFMQ2%2Bpufy5AiEAgYZVetBrNaAJ7VXcnHxk3bb5t8TQcAq1uNMRhGYGUYwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGS8TbopPfu3V%2B%2BVzCrcA65dk%2B%2FYMeZ38tf%2FA92%2BPsdAP19Ww1fkqqaxTYKLSP9wNgfrH0Iqh1NsyRHg3DCI3yyT4cSFY9eOAwbazlezSYtw3NfjTBAY7pMDLj%2F6rMgMuJF5vmBBfd6Q5SI%2BdmB61twCt6bwgiPRm5yo%2FzcImtcBS3YxJIXx1N6a3bODOgmh%2BlT%2Foi57Q2WYqCdpNQpfDAkg2rU1KaSY5PAsZHz9V4JuygAlkUUk1pDFvjhtpqmxUWGIyux%2FPi%2B%2FksI3FcCACyxosCuzou1mo%2BFxzv81FRekPL52eBSgNMkWHnM6Z0VEXa6zrpr%2BZT43UXumsGI1rFT%2FPbbPihLoICeme7g7djMP9oZPxqE1HO6f2kXjBweI%2FEiknIr70oMdEbmC52RHtPQlKR5IEVEQY5d%2BAHNS4zRRdAbUiW32ZB1HZFueENaMdJly6rEwCaJMTKsHa4X8loIRAsGJiJN%2FfNiDatxtNsQzgfIFtLDbpR4YoXwkxb995k3MX%2BSbdgy57Xymvb0UeYfHqlgKigtJHQr4e4xInMx2B7dKipWI0exHguiKlDZ7LozvBit6jQjeVK%2Fdr4NM2ioYrWVtFsYymQxlFKe%2BncnOri%2FvB3Wf60ner%2F31bL12Tzx9BpkAjl0%2FVpG3MNKk97wGOqUBb3DVKOG5tXrKXWBT6BMaV%2BnqJ0uzLaNSjp335xxAuTvQxN0w%2FgMrDPQYKt3p47rA8qENvsiQeifvd7la25eUJRCVEznVsIO8cPfM6wpA%2B9EWtJzHZk9Pu%2BqrTR24izEd88HSpTwe1DZwEShTlUpPwcApdGudyhnMH%2Bs6zXUyltu5d2UxhuKpTr14vKYxzztxoKxXiaZYct%2BjR98YYzBtsJ32XOpQ&X-Amz-Signature=e26989dbbc35eca4d87bf6dcc59cc82621fe6578c1f28a752f286f9501882ced&X-Amz-SignedHeaders=host&x-id=GetObject)
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