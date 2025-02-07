

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3PB37CE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDdCB8iq88zlPSGONdLOOoR8YqDYQUrYFhvFA2HJCNuzAIgZLtnlPL0TdSVl7PAIrvVAIsKPltNixNWFgrx8IFu7Gcq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDEDTcWwM%2B3GHXC3%2FvSrcA6BtID6J2aRjIsb5yslh7pR3QpGuDjvl9t1rhNQLX8Lzl7VgRcDaoQC4ijwHXETRmam07lN8Sd76M9R9EuwjKDJtdX2eeW1Dgrce8h1T1CvABE6n8IIT8x%2FsGuNdfvFy7mMVmApQoZK51njM8T07hCBzhO9MXDyEN%2FYgOsU4o%2FMeAkDW6Hqfc%2BP4YigpVuH%2Fjom0vqbv8Y3Rbe8dJ5%2BSXWsLuBiu9jwr1lMbxaJes8FMBqin%2B%2F1nr42eWV1QLxd%2FKh6uApB%2BhnTpfgrEk5BCfbnVP4zE1oYYjAQCYiRkcvDdfBD7R04ZTlvgTlamQ1gWlJ7a80x5iF6Viag2D7mvG9yD18T3e9SK7WTJ4kKoGWY3eFT%2BStzdOfAB6wQS9yJiRmj7XJ2vJYL3bYahoOcw%2FKQNIGc8qE%2BKmHljWSRL2O%2Bik%2BJGDn6ylZDjjREbUzz3h5zk3JGgc3RKUbVKfYoAhyvXo8hDbphArRZkqdq1S8g9nyvUM0wIvDJ36Gor%2BXyvwzDX9nJJ8WiSDPNRf4Yp9evAr2EzCQXST2dzFrgmXreLy71FDx4zkxsSfArs%2FrQbRu5H0tM5dmPscjwo1zu7Dyl5D33%2FyGhCsYagFbnCYQVM8B4PKDsOi7Tr3RxCMMeLmL0GOqUB92sS0ewjfuwzyKAzGdCRVC7KuaiTaVmYq1RxWdyDu4uBNhxS0bPL%2BGJLq7dJ6DFsO4ni%2FtrqSwP1398meCKCMuD9l3Q05zUzvmRU3hw8NhtsNgfvw2n0sgPNIOw58VR1rkSzha0ISlf07bZYwfPrBpJvedUibgpenYwp5mCDF%2Fd0BD6f2Gx24TQdkBmPzDb7L4mS5lBaNqdbFvD5d%2BOSsuJHyF0B&X-Amz-Signature=7be201dc1d3d71b2b2588c0574d8aed39d3c7651747d206b73a0199101ead115&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3PB37CE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDdCB8iq88zlPSGONdLOOoR8YqDYQUrYFhvFA2HJCNuzAIgZLtnlPL0TdSVl7PAIrvVAIsKPltNixNWFgrx8IFu7Gcq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDEDTcWwM%2B3GHXC3%2FvSrcA6BtID6J2aRjIsb5yslh7pR3QpGuDjvl9t1rhNQLX8Lzl7VgRcDaoQC4ijwHXETRmam07lN8Sd76M9R9EuwjKDJtdX2eeW1Dgrce8h1T1CvABE6n8IIT8x%2FsGuNdfvFy7mMVmApQoZK51njM8T07hCBzhO9MXDyEN%2FYgOsU4o%2FMeAkDW6Hqfc%2BP4YigpVuH%2Fjom0vqbv8Y3Rbe8dJ5%2BSXWsLuBiu9jwr1lMbxaJes8FMBqin%2B%2F1nr42eWV1QLxd%2FKh6uApB%2BhnTpfgrEk5BCfbnVP4zE1oYYjAQCYiRkcvDdfBD7R04ZTlvgTlamQ1gWlJ7a80x5iF6Viag2D7mvG9yD18T3e9SK7WTJ4kKoGWY3eFT%2BStzdOfAB6wQS9yJiRmj7XJ2vJYL3bYahoOcw%2FKQNIGc8qE%2BKmHljWSRL2O%2Bik%2BJGDn6ylZDjjREbUzz3h5zk3JGgc3RKUbVKfYoAhyvXo8hDbphArRZkqdq1S8g9nyvUM0wIvDJ36Gor%2BXyvwzDX9nJJ8WiSDPNRf4Yp9evAr2EzCQXST2dzFrgmXreLy71FDx4zkxsSfArs%2FrQbRu5H0tM5dmPscjwo1zu7Dyl5D33%2FyGhCsYagFbnCYQVM8B4PKDsOi7Tr3RxCMMeLmL0GOqUB92sS0ewjfuwzyKAzGdCRVC7KuaiTaVmYq1RxWdyDu4uBNhxS0bPL%2BGJLq7dJ6DFsO4ni%2FtrqSwP1398meCKCMuD9l3Q05zUzvmRU3hw8NhtsNgfvw2n0sgPNIOw58VR1rkSzha0ISlf07bZYwfPrBpJvedUibgpenYwp5mCDF%2Fd0BD6f2Gx24TQdkBmPzDb7L4mS5lBaNqdbFvD5d%2BOSsuJHyF0B&X-Amz-Signature=300b144aceec670699146f8448d6d05d4ee41e867a004099e745d02f4ffec553&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3PB37CE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDdCB8iq88zlPSGONdLOOoR8YqDYQUrYFhvFA2HJCNuzAIgZLtnlPL0TdSVl7PAIrvVAIsKPltNixNWFgrx8IFu7Gcq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDEDTcWwM%2B3GHXC3%2FvSrcA6BtID6J2aRjIsb5yslh7pR3QpGuDjvl9t1rhNQLX8Lzl7VgRcDaoQC4ijwHXETRmam07lN8Sd76M9R9EuwjKDJtdX2eeW1Dgrce8h1T1CvABE6n8IIT8x%2FsGuNdfvFy7mMVmApQoZK51njM8T07hCBzhO9MXDyEN%2FYgOsU4o%2FMeAkDW6Hqfc%2BP4YigpVuH%2Fjom0vqbv8Y3Rbe8dJ5%2BSXWsLuBiu9jwr1lMbxaJes8FMBqin%2B%2F1nr42eWV1QLxd%2FKh6uApB%2BhnTpfgrEk5BCfbnVP4zE1oYYjAQCYiRkcvDdfBD7R04ZTlvgTlamQ1gWlJ7a80x5iF6Viag2D7mvG9yD18T3e9SK7WTJ4kKoGWY3eFT%2BStzdOfAB6wQS9yJiRmj7XJ2vJYL3bYahoOcw%2FKQNIGc8qE%2BKmHljWSRL2O%2Bik%2BJGDn6ylZDjjREbUzz3h5zk3JGgc3RKUbVKfYoAhyvXo8hDbphArRZkqdq1S8g9nyvUM0wIvDJ36Gor%2BXyvwzDX9nJJ8WiSDPNRf4Yp9evAr2EzCQXST2dzFrgmXreLy71FDx4zkxsSfArs%2FrQbRu5H0tM5dmPscjwo1zu7Dyl5D33%2FyGhCsYagFbnCYQVM8B4PKDsOi7Tr3RxCMMeLmL0GOqUB92sS0ewjfuwzyKAzGdCRVC7KuaiTaVmYq1RxWdyDu4uBNhxS0bPL%2BGJLq7dJ6DFsO4ni%2FtrqSwP1398meCKCMuD9l3Q05zUzvmRU3hw8NhtsNgfvw2n0sgPNIOw58VR1rkSzha0ISlf07bZYwfPrBpJvedUibgpenYwp5mCDF%2Fd0BD6f2Gx24TQdkBmPzDb7L4mS5lBaNqdbFvD5d%2BOSsuJHyF0B&X-Amz-Signature=ff80b97ab2d4523862d8d2b791bb1f2df5c1a58a0a47db947063d1688c0e3ada&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBADQIK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQC%2B9rxxsxIbRlUCSAmMBYVt2z0e1g3Rp5%2Fv9s1R6XpwywIhAOz8840AvAy0JYMPt1cRsNjZWtpgjTRjo%2FtInxJ6Db7aKv8DCHYQABoMNjM3NDIzMTgzODA1Igza081RhmiNPf31MKIq3AOQK4nJPaY4wIk86UNaCoTxLE6VCbTqmy7XGLlndY1TdiuvKHbZrVHkpDrSSnnc2DPGS2JdlVLKjYSV501BB%2Fu%2BDy%2FhE9N4%2BDWvjxP6ofMgCZYAj0kHYJUYps05%2FBpUinKeZ%2BBIVggdCTFfgaMx5f1UmTcjumafEsiqQ8iKco8ceet2ykD8JAB6%2B%2BUuxg7xoz0vEKtn6p2FPTl5MclkjtbOyrK0cbc%2FfL8eptP%2FRB%2BYQAPndFsvkCySKctLLPSnR4Kfb%2BP9at20X%2Bw5LeVzdeUC2eYQ0SCE1eADKwrvu%2F8lb2VifWJAVCQo2y2gx5gBTYpYmkGQdKEReXRRLD1XCh7dBcwtXT4sbCVT8LOhy4VKZRjZSpDRRffu36Bku%2BXSnosUOh219JS7%2BS1440%2BDi4p28DEqSS4bJM%2BrTYSEhS4aKuaqqbcwsgVtkT97yOhDDKSmzLYfVMI4SoDeJfsjVCkWs7VpQP8a3YI8R9DYEIp72f67SFLv5KlS%2FitDc8qKTsJTvMcQC%2Bsi%2FRStKGPK908rdN3pHt5ZZnaYN%2FNlh9v%2F%2BxwlGgGRwwOZf9IDL0h8aU8xw2CI8%2BSQiaItN6OxumXeRG0y%2FQuw3Ax2y%2Bw73%2FZ26WOwrwb3gWAZ0Qf10TC7i5i9BjqkAfsIGIcbAnQYnjz%2B%2B%2B%2FPGfjWaIk%2BeNDa8rU%2FGb%2FoQcbKqY%2FgOcslpxM8l8oJqSTiAfI3fLx8bDRl8S0ZdEBQ0C8IiZQ3aUK9mQaIY8RAY4TnOrScVRyWNrHrPb5rzYiVWe5sdPMAHnQ%2FD9XtQslhMw%2BKNxgf043bHFdmyLFm%2F1OpyO%2BTPMT5yJ2nkZyi66qSJpU1E2e9ycMeWFUtmSx341iPYHAh&X-Amz-Signature=43c0ae309feb1aacadfc7b4a55f05312f97d0e531af94ba7b08e5ffefbdabc69&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBADQIK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQC%2B9rxxsxIbRlUCSAmMBYVt2z0e1g3Rp5%2Fv9s1R6XpwywIhAOz8840AvAy0JYMPt1cRsNjZWtpgjTRjo%2FtInxJ6Db7aKv8DCHYQABoMNjM3NDIzMTgzODA1Igza081RhmiNPf31MKIq3AOQK4nJPaY4wIk86UNaCoTxLE6VCbTqmy7XGLlndY1TdiuvKHbZrVHkpDrSSnnc2DPGS2JdlVLKjYSV501BB%2Fu%2BDy%2FhE9N4%2BDWvjxP6ofMgCZYAj0kHYJUYps05%2FBpUinKeZ%2BBIVggdCTFfgaMx5f1UmTcjumafEsiqQ8iKco8ceet2ykD8JAB6%2B%2BUuxg7xoz0vEKtn6p2FPTl5MclkjtbOyrK0cbc%2FfL8eptP%2FRB%2BYQAPndFsvkCySKctLLPSnR4Kfb%2BP9at20X%2Bw5LeVzdeUC2eYQ0SCE1eADKwrvu%2F8lb2VifWJAVCQo2y2gx5gBTYpYmkGQdKEReXRRLD1XCh7dBcwtXT4sbCVT8LOhy4VKZRjZSpDRRffu36Bku%2BXSnosUOh219JS7%2BS1440%2BDi4p28DEqSS4bJM%2BrTYSEhS4aKuaqqbcwsgVtkT97yOhDDKSmzLYfVMI4SoDeJfsjVCkWs7VpQP8a3YI8R9DYEIp72f67SFLv5KlS%2FitDc8qKTsJTvMcQC%2Bsi%2FRStKGPK908rdN3pHt5ZZnaYN%2FNlh9v%2F%2BxwlGgGRwwOZf9IDL0h8aU8xw2CI8%2BSQiaItN6OxumXeRG0y%2FQuw3Ax2y%2Bw73%2FZ26WOwrwb3gWAZ0Qf10TC7i5i9BjqkAfsIGIcbAnQYnjz%2B%2B%2B%2FPGfjWaIk%2BeNDa8rU%2FGb%2FoQcbKqY%2FgOcslpxM8l8oJqSTiAfI3fLx8bDRl8S0ZdEBQ0C8IiZQ3aUK9mQaIY8RAY4TnOrScVRyWNrHrPb5rzYiVWe5sdPMAHnQ%2FD9XtQslhMw%2BKNxgf043bHFdmyLFm%2F1OpyO%2BTPMT5yJ2nkZyi66qSJpU1E2e9ycMeWFUtmSx341iPYHAh&X-Amz-Signature=3d4028317f531e9c5853149288adccc02b8daae5478a0eb10cc5654029798161&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3PB37CE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDdCB8iq88zlPSGONdLOOoR8YqDYQUrYFhvFA2HJCNuzAIgZLtnlPL0TdSVl7PAIrvVAIsKPltNixNWFgrx8IFu7Gcq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDEDTcWwM%2B3GHXC3%2FvSrcA6BtID6J2aRjIsb5yslh7pR3QpGuDjvl9t1rhNQLX8Lzl7VgRcDaoQC4ijwHXETRmam07lN8Sd76M9R9EuwjKDJtdX2eeW1Dgrce8h1T1CvABE6n8IIT8x%2FsGuNdfvFy7mMVmApQoZK51njM8T07hCBzhO9MXDyEN%2FYgOsU4o%2FMeAkDW6Hqfc%2BP4YigpVuH%2Fjom0vqbv8Y3Rbe8dJ5%2BSXWsLuBiu9jwr1lMbxaJes8FMBqin%2B%2F1nr42eWV1QLxd%2FKh6uApB%2BhnTpfgrEk5BCfbnVP4zE1oYYjAQCYiRkcvDdfBD7R04ZTlvgTlamQ1gWlJ7a80x5iF6Viag2D7mvG9yD18T3e9SK7WTJ4kKoGWY3eFT%2BStzdOfAB6wQS9yJiRmj7XJ2vJYL3bYahoOcw%2FKQNIGc8qE%2BKmHljWSRL2O%2Bik%2BJGDn6ylZDjjREbUzz3h5zk3JGgc3RKUbVKfYoAhyvXo8hDbphArRZkqdq1S8g9nyvUM0wIvDJ36Gor%2BXyvwzDX9nJJ8WiSDPNRf4Yp9evAr2EzCQXST2dzFrgmXreLy71FDx4zkxsSfArs%2FrQbRu5H0tM5dmPscjwo1zu7Dyl5D33%2FyGhCsYagFbnCYQVM8B4PKDsOi7Tr3RxCMMeLmL0GOqUB92sS0ewjfuwzyKAzGdCRVC7KuaiTaVmYq1RxWdyDu4uBNhxS0bPL%2BGJLq7dJ6DFsO4ni%2FtrqSwP1398meCKCMuD9l3Q05zUzvmRU3hw8NhtsNgfvw2n0sgPNIOw58VR1rkSzha0ISlf07bZYwfPrBpJvedUibgpenYwp5mCDF%2Fd0BD6f2Gx24TQdkBmPzDb7L4mS5lBaNqdbFvD5d%2BOSsuJHyF0B&X-Amz-Signature=500cba3480d39af9d97658401fbfd61dfb8949f090396872cd357d6b750cd792&X-Amz-SignedHeaders=host&x-id=GetObject)
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