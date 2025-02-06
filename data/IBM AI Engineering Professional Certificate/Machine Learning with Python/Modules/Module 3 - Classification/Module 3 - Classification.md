

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7YRKXUA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIC2yoZBWIJRVGFCk5ZyVEycOVSisPhZkuLTAulM3Q%2FKVAiEA%2FqK8fJvkIXgfMoBX0bCKrp7nyp94p2p2Vm8Y98uTy6oq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDCoPSb5NXsyo1th7lSrcA2Vz1W0dQ7ujNJfyIhoLYCE74YJwekuMn%2FRWiKZZ5WDu50m6VjMQ8Rb%2BGTr1h%2FKwbyleMDwmJRBnf0N7C3slFSpLXxfU5O2LgWWJ%2FLRf9fclC4wQC9OckdzjTO3cZw%2FyvYLH%2FFp8js94uMPPyLVZsVb3QfU2s0QdMvU8ldT%2BsfM0HGLud6zdRMHrETXgrAd37Ox1DjF7FyrL0RJW0dc54XEiUjkyJ2mQOkHMs4t2EUcKP4jwBZhBsz0GZLebveFRwFj8SIW7DQ03Z5XGCvOLNXYWJvbvdqEi%2BJTg0HAuDVIDTDBigG8UMP7UNSUcN7MplxwQwTaQhF%2FqVzXdpLrjRMHEtrB6DBTcZR3dwi9vJkPsmu6S1ETfZM9xm%2FdB%2BuERdJwwBL23vD1HtFeMwRxrX93AzWUBy%2BiHk86xdP7L2x%2FfhSJ3pAL0zzzLsIg0i45V2rtck8GatnsX1BlWbKSdpErjUeKokNAfFQtnjEaZ5Y%2F4iToEwem3k8l4ja8lC%2F4v4wpF1i%2FJy7ysMn1GDf6WNK3WXnlLFLPD8Yr%2BzrgKFd3hOhgxcKB%2BTtQzEG6rBBjevNjJt%2FrO8dikEYyDZ9MqvMdvwT2dwa8hBNhImIkfgfkhb%2BranYGuU3nNCWqrMM75kr0GOqUBCHVkw5dlcBsxdzTvPbbUgR6VYPsW8JfuCwQ7oYRU3ubPi9e0Q3EwpHLw35dH2OV3pKKMr2D%2BBLg0nid08r1wAQWtkeMjQZyCbqfXn%2BfKYGGdIC6ThxrooSypykUAegkWWvyLzEl0ke37YV8%2Bld30L8HU3ZGOfzvqID6bkmSSzSzxCXZ0rpzlHrqngDMxineUXZ5%2FGq6VGGIniLMoTV4XwpLu8%2FoB&X-Amz-Signature=4c610e28b21d11af536453e87eb64e7a757293411e3e485ba262ac5743649ea5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7YRKXUA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIC2yoZBWIJRVGFCk5ZyVEycOVSisPhZkuLTAulM3Q%2FKVAiEA%2FqK8fJvkIXgfMoBX0bCKrp7nyp94p2p2Vm8Y98uTy6oq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDCoPSb5NXsyo1th7lSrcA2Vz1W0dQ7ujNJfyIhoLYCE74YJwekuMn%2FRWiKZZ5WDu50m6VjMQ8Rb%2BGTr1h%2FKwbyleMDwmJRBnf0N7C3slFSpLXxfU5O2LgWWJ%2FLRf9fclC4wQC9OckdzjTO3cZw%2FyvYLH%2FFp8js94uMPPyLVZsVb3QfU2s0QdMvU8ldT%2BsfM0HGLud6zdRMHrETXgrAd37Ox1DjF7FyrL0RJW0dc54XEiUjkyJ2mQOkHMs4t2EUcKP4jwBZhBsz0GZLebveFRwFj8SIW7DQ03Z5XGCvOLNXYWJvbvdqEi%2BJTg0HAuDVIDTDBigG8UMP7UNSUcN7MplxwQwTaQhF%2FqVzXdpLrjRMHEtrB6DBTcZR3dwi9vJkPsmu6S1ETfZM9xm%2FdB%2BuERdJwwBL23vD1HtFeMwRxrX93AzWUBy%2BiHk86xdP7L2x%2FfhSJ3pAL0zzzLsIg0i45V2rtck8GatnsX1BlWbKSdpErjUeKokNAfFQtnjEaZ5Y%2F4iToEwem3k8l4ja8lC%2F4v4wpF1i%2FJy7ysMn1GDf6WNK3WXnlLFLPD8Yr%2BzrgKFd3hOhgxcKB%2BTtQzEG6rBBjevNjJt%2FrO8dikEYyDZ9MqvMdvwT2dwa8hBNhImIkfgfkhb%2BranYGuU3nNCWqrMM75kr0GOqUBCHVkw5dlcBsxdzTvPbbUgR6VYPsW8JfuCwQ7oYRU3ubPi9e0Q3EwpHLw35dH2OV3pKKMr2D%2BBLg0nid08r1wAQWtkeMjQZyCbqfXn%2BfKYGGdIC6ThxrooSypykUAegkWWvyLzEl0ke37YV8%2Bld30L8HU3ZGOfzvqID6bkmSSzSzxCXZ0rpzlHrqngDMxineUXZ5%2FGq6VGGIniLMoTV4XwpLu8%2FoB&X-Amz-Signature=876c1a272b5a368aabdd718ac4479c8114918124b5e50cddf751d67dc24b18a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7YRKXUA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIC2yoZBWIJRVGFCk5ZyVEycOVSisPhZkuLTAulM3Q%2FKVAiEA%2FqK8fJvkIXgfMoBX0bCKrp7nyp94p2p2Vm8Y98uTy6oq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDCoPSb5NXsyo1th7lSrcA2Vz1W0dQ7ujNJfyIhoLYCE74YJwekuMn%2FRWiKZZ5WDu50m6VjMQ8Rb%2BGTr1h%2FKwbyleMDwmJRBnf0N7C3slFSpLXxfU5O2LgWWJ%2FLRf9fclC4wQC9OckdzjTO3cZw%2FyvYLH%2FFp8js94uMPPyLVZsVb3QfU2s0QdMvU8ldT%2BsfM0HGLud6zdRMHrETXgrAd37Ox1DjF7FyrL0RJW0dc54XEiUjkyJ2mQOkHMs4t2EUcKP4jwBZhBsz0GZLebveFRwFj8SIW7DQ03Z5XGCvOLNXYWJvbvdqEi%2BJTg0HAuDVIDTDBigG8UMP7UNSUcN7MplxwQwTaQhF%2FqVzXdpLrjRMHEtrB6DBTcZR3dwi9vJkPsmu6S1ETfZM9xm%2FdB%2BuERdJwwBL23vD1HtFeMwRxrX93AzWUBy%2BiHk86xdP7L2x%2FfhSJ3pAL0zzzLsIg0i45V2rtck8GatnsX1BlWbKSdpErjUeKokNAfFQtnjEaZ5Y%2F4iToEwem3k8l4ja8lC%2F4v4wpF1i%2FJy7ysMn1GDf6WNK3WXnlLFLPD8Yr%2BzrgKFd3hOhgxcKB%2BTtQzEG6rBBjevNjJt%2FrO8dikEYyDZ9MqvMdvwT2dwa8hBNhImIkfgfkhb%2BranYGuU3nNCWqrMM75kr0GOqUBCHVkw5dlcBsxdzTvPbbUgR6VYPsW8JfuCwQ7oYRU3ubPi9e0Q3EwpHLw35dH2OV3pKKMr2D%2BBLg0nid08r1wAQWtkeMjQZyCbqfXn%2BfKYGGdIC6ThxrooSypykUAegkWWvyLzEl0ke37YV8%2Bld30L8HU3ZGOfzvqID6bkmSSzSzxCXZ0rpzlHrqngDMxineUXZ5%2FGq6VGGIniLMoTV4XwpLu8%2FoB&X-Amz-Signature=8e5abb631c78d47785323292c3ebbb6824a49449d64affbbef36dce756fcdfa2&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWLN5P6K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCID%2BYkwPkE1Q5vgV77VRItndsuE2x%2BlrqgWcvKf5zkH7TAiABCafQ%2FjFcdfYavsv07F47cMxPed9EI4k%2ByZc6P%2F4NzCr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMg50yWM6hnyu13pZJKtwDmhTbcT7rJbKTG6KM2Q35E7CFMH0Vi60oLhN7vmTniPvblZ1B%2FJLdrYSbmpNDH7laSoTHt%2B0XTvujFpVfOThvMEceXaC%2BGf4t4uwUUT2zcw51%2FPkBLYriFRKIIt2SK0RD1wfP7JUCkKXfgfKPgjoVvoafNd6VCIp%2F9AavHhRnXYrQAvx85GoBrommgeHJt2%2Fw1BGkEGx0XILfx9YKX7ZWs2ajTQLt6A6lcfIS5lRMfCRX7i8SM8Ud0b%2BPudzqmfr%2FrUf6NmoeeFdgUJOlgLcLtivqepMWOb8VG4afSpdRukbxMci2n7%2FTcCKiG3waKslnt0WyuHcDDXpYETsEJjKENuFo5nN%2FucYeamTvWBwtNKzYIXGLavHFeSKAR%2BaP9njVzEtBB2AypH3CX6qLBm0JR5JMrhCCy4HvCfixdpj2oIq2Gpt83ZonV6DQ65E0ggn%2F%2BfleBIsjtvPC2NTW%2BBc%2FDrjvZTXRIvXV6UXGQk6WE2bPJidOesI6BIYPyIJIQGOncekHLXsmQIbQkAJReQedOzZgQaGQ8ejgkvd%2BTpfUr5SDGjqdZFgifT6pYdrYjP4WwQWQJeIedePL05MDOxssOLGHztTzWUeUA%2F7ovHv5CTdaczqD52kBqWvSzIUwpfqSvQY6pgHd8ntuMWVjBx%2Fuy6%2BzUh6sqr0PN23%2BSmWNcFT0rykq9B4eSIjOLcYWM%2FIuWG%2BSPI1XdqoZOlaLdrsMWHFRS4FQY5TDwSLsBwnY6r2mwL7VDMYrENf549%2FMjmOedZr3eEuFLJzVmsZJLzud0uFZkvWgNrzd%2FSN6ytFS0IXjTm79E%2BLLDHcVxVr9o%2BzpT5VQi04aNphVi%2BTMRSdFTANu9tL5DPCF%2BHE2&X-Amz-Signature=740e9000e44344d81b70bad126c5bf3d95b9d886a44c5a35bf87d9268ee5c93c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWLN5P6K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCID%2BYkwPkE1Q5vgV77VRItndsuE2x%2BlrqgWcvKf5zkH7TAiABCafQ%2FjFcdfYavsv07F47cMxPed9EI4k%2ByZc6P%2F4NzCr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIMg50yWM6hnyu13pZJKtwDmhTbcT7rJbKTG6KM2Q35E7CFMH0Vi60oLhN7vmTniPvblZ1B%2FJLdrYSbmpNDH7laSoTHt%2B0XTvujFpVfOThvMEceXaC%2BGf4t4uwUUT2zcw51%2FPkBLYriFRKIIt2SK0RD1wfP7JUCkKXfgfKPgjoVvoafNd6VCIp%2F9AavHhRnXYrQAvx85GoBrommgeHJt2%2Fw1BGkEGx0XILfx9YKX7ZWs2ajTQLt6A6lcfIS5lRMfCRX7i8SM8Ud0b%2BPudzqmfr%2FrUf6NmoeeFdgUJOlgLcLtivqepMWOb8VG4afSpdRukbxMci2n7%2FTcCKiG3waKslnt0WyuHcDDXpYETsEJjKENuFo5nN%2FucYeamTvWBwtNKzYIXGLavHFeSKAR%2BaP9njVzEtBB2AypH3CX6qLBm0JR5JMrhCCy4HvCfixdpj2oIq2Gpt83ZonV6DQ65E0ggn%2F%2BfleBIsjtvPC2NTW%2BBc%2FDrjvZTXRIvXV6UXGQk6WE2bPJidOesI6BIYPyIJIQGOncekHLXsmQIbQkAJReQedOzZgQaGQ8ejgkvd%2BTpfUr5SDGjqdZFgifT6pYdrYjP4WwQWQJeIedePL05MDOxssOLGHztTzWUeUA%2F7ovHv5CTdaczqD52kBqWvSzIUwpfqSvQY6pgHd8ntuMWVjBx%2Fuy6%2BzUh6sqr0PN23%2BSmWNcFT0rykq9B4eSIjOLcYWM%2FIuWG%2BSPI1XdqoZOlaLdrsMWHFRS4FQY5TDwSLsBwnY6r2mwL7VDMYrENf549%2FMjmOedZr3eEuFLJzVmsZJLzud0uFZkvWgNrzd%2FSN6ytFS0IXjTm79E%2BLLDHcVxVr9o%2BzpT5VQi04aNphVi%2BTMRSdFTANu9tL5DPCF%2BHE2&X-Amz-Signature=06054159f4ab7a69d7e84634417b7ee395eecc4c55db529c6e9871493243e3e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7YRKXUA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIC2yoZBWIJRVGFCk5ZyVEycOVSisPhZkuLTAulM3Q%2FKVAiEA%2FqK8fJvkIXgfMoBX0bCKrp7nyp94p2p2Vm8Y98uTy6oq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDCoPSb5NXsyo1th7lSrcA2Vz1W0dQ7ujNJfyIhoLYCE74YJwekuMn%2FRWiKZZ5WDu50m6VjMQ8Rb%2BGTr1h%2FKwbyleMDwmJRBnf0N7C3slFSpLXxfU5O2LgWWJ%2FLRf9fclC4wQC9OckdzjTO3cZw%2FyvYLH%2FFp8js94uMPPyLVZsVb3QfU2s0QdMvU8ldT%2BsfM0HGLud6zdRMHrETXgrAd37Ox1DjF7FyrL0RJW0dc54XEiUjkyJ2mQOkHMs4t2EUcKP4jwBZhBsz0GZLebveFRwFj8SIW7DQ03Z5XGCvOLNXYWJvbvdqEi%2BJTg0HAuDVIDTDBigG8UMP7UNSUcN7MplxwQwTaQhF%2FqVzXdpLrjRMHEtrB6DBTcZR3dwi9vJkPsmu6S1ETfZM9xm%2FdB%2BuERdJwwBL23vD1HtFeMwRxrX93AzWUBy%2BiHk86xdP7L2x%2FfhSJ3pAL0zzzLsIg0i45V2rtck8GatnsX1BlWbKSdpErjUeKokNAfFQtnjEaZ5Y%2F4iToEwem3k8l4ja8lC%2F4v4wpF1i%2FJy7ysMn1GDf6WNK3WXnlLFLPD8Yr%2BzrgKFd3hOhgxcKB%2BTtQzEG6rBBjevNjJt%2FrO8dikEYyDZ9MqvMdvwT2dwa8hBNhImIkfgfkhb%2BranYGuU3nNCWqrMM75kr0GOqUBCHVkw5dlcBsxdzTvPbbUgR6VYPsW8JfuCwQ7oYRU3ubPi9e0Q3EwpHLw35dH2OV3pKKMr2D%2BBLg0nid08r1wAQWtkeMjQZyCbqfXn%2BfKYGGdIC6ThxrooSypykUAegkWWvyLzEl0ke37YV8%2Bld30L8HU3ZGOfzvqID6bkmSSzSzxCXZ0rpzlHrqngDMxineUXZ5%2FGq6VGGIniLMoTV4XwpLu8%2FoB&X-Amz-Signature=bbc19502cb8dc3d03a889f1e1a94c09c2fe4cfec36bed33f1ad14be68b30289f&X-Amz-SignedHeaders=host&x-id=GetObject)
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