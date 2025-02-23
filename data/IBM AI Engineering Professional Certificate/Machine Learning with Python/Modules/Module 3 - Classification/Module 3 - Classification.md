

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQRSXI2G%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcfuhUpRLMCPb558c6fsVNabwgVzhsEA85sGzFh%2BMx3AiBKLm%2BrWanRnM2ukNkJXAqNdQ3DrvBo1jguh%2BZle9C9AiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Fy%2Bn9nFLqekGusWzKtwDba26RvMkJIagYoPYTwgaTjVGoXsBW5zeTg%2F6IhT3l9j5Xq%2B1qPn78g0DbFm0MbtOYK45jh6WYviVpawm2Y5IomuEeemuthcbIjWRFKU9v0VXoUg7YatsmjMX%2BdW7MjS7aR65AfVTjPRcMeTEVPD7PPUIuwed%2FHd2CMy%2Bilvucw5rKR1YrCYHQPgCSE1aTDAy8g08qeU2eFkJT4zpIDMS2iWUzVFnOmWQjKnT3d7NneiNAK2BUhJ9d3HX2QGJrRjyhNebTzeGCxDDAkEmX%2BkKihLxDLBTNg%2BVE9gud4fnqa0Hr3nyCeIJRz3dpLTImauLauvfE8pWKRoRjNPVibnOZlmzetbm1r5kT%2FuA%2BllP5cU2hrcFFqByVGEViAjWuNTZI%2FRDf0fiRoDq%2BXZwqfubtPN168dD3AkEbb%2B10LzYVFq2awahehHSyAboOUnWqb3SEx5HpN51qeypdzNX7dQnCHlu3F8dNCDyf5exTseAaGusJX25jpgH3KjKXSLQC618uONn9T3xbbYisGb4dzdhhgRov9RxzzzfXh1qP7O7LKoB0J8F5oQCX2P%2Bw94Tl6V7KkGZUEKOiJyeF07w7R01URE%2B%2Fb2PhkpMHChZWjTiuq5xFZi0V6pYaVzFR%2FowuKTpvQY6pgEUKFhuIF043WdosEhhtDSsaILogiMh6ANqtLteHapoANh1Ee%2F9uAtfv1f1GQ8YkuFPaVv%2FzukOfWYKwbZMbvtAmAAZiUnYaY4Ee%2BRWxBLih0Y5AReSP40jP2Udtdglf%2BXnOF5oac4fsMbulWAPbMMLoN2%2BexRJNktwGVHmVPRyxiwL3%2BoS%2BL0C4d%2BT8FBuan4Xc3tKUPAw9AcFtFfiegfQuL8RvptA&X-Amz-Signature=2084720a36bf778ebfc500605099c31b84dc0539fe33d9058b1d2a123e343095&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQRSXI2G%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcfuhUpRLMCPb558c6fsVNabwgVzhsEA85sGzFh%2BMx3AiBKLm%2BrWanRnM2ukNkJXAqNdQ3DrvBo1jguh%2BZle9C9AiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Fy%2Bn9nFLqekGusWzKtwDba26RvMkJIagYoPYTwgaTjVGoXsBW5zeTg%2F6IhT3l9j5Xq%2B1qPn78g0DbFm0MbtOYK45jh6WYviVpawm2Y5IomuEeemuthcbIjWRFKU9v0VXoUg7YatsmjMX%2BdW7MjS7aR65AfVTjPRcMeTEVPD7PPUIuwed%2FHd2CMy%2Bilvucw5rKR1YrCYHQPgCSE1aTDAy8g08qeU2eFkJT4zpIDMS2iWUzVFnOmWQjKnT3d7NneiNAK2BUhJ9d3HX2QGJrRjyhNebTzeGCxDDAkEmX%2BkKihLxDLBTNg%2BVE9gud4fnqa0Hr3nyCeIJRz3dpLTImauLauvfE8pWKRoRjNPVibnOZlmzetbm1r5kT%2FuA%2BllP5cU2hrcFFqByVGEViAjWuNTZI%2FRDf0fiRoDq%2BXZwqfubtPN168dD3AkEbb%2B10LzYVFq2awahehHSyAboOUnWqb3SEx5HpN51qeypdzNX7dQnCHlu3F8dNCDyf5exTseAaGusJX25jpgH3KjKXSLQC618uONn9T3xbbYisGb4dzdhhgRov9RxzzzfXh1qP7O7LKoB0J8F5oQCX2P%2Bw94Tl6V7KkGZUEKOiJyeF07w7R01URE%2B%2Fb2PhkpMHChZWjTiuq5xFZi0V6pYaVzFR%2FowuKTpvQY6pgEUKFhuIF043WdosEhhtDSsaILogiMh6ANqtLteHapoANh1Ee%2F9uAtfv1f1GQ8YkuFPaVv%2FzukOfWYKwbZMbvtAmAAZiUnYaY4Ee%2BRWxBLih0Y5AReSP40jP2Udtdglf%2BXnOF5oac4fsMbulWAPbMMLoN2%2BexRJNktwGVHmVPRyxiwL3%2BoS%2BL0C4d%2BT8FBuan4Xc3tKUPAw9AcFtFfiegfQuL8RvptA&X-Amz-Signature=15e18bdd3d6c43167f87150c3c6981e21d15426fbcb689ae6cd8a200fb557b7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQRSXI2G%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcfuhUpRLMCPb558c6fsVNabwgVzhsEA85sGzFh%2BMx3AiBKLm%2BrWanRnM2ukNkJXAqNdQ3DrvBo1jguh%2BZle9C9AiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Fy%2Bn9nFLqekGusWzKtwDba26RvMkJIagYoPYTwgaTjVGoXsBW5zeTg%2F6IhT3l9j5Xq%2B1qPn78g0DbFm0MbtOYK45jh6WYviVpawm2Y5IomuEeemuthcbIjWRFKU9v0VXoUg7YatsmjMX%2BdW7MjS7aR65AfVTjPRcMeTEVPD7PPUIuwed%2FHd2CMy%2Bilvucw5rKR1YrCYHQPgCSE1aTDAy8g08qeU2eFkJT4zpIDMS2iWUzVFnOmWQjKnT3d7NneiNAK2BUhJ9d3HX2QGJrRjyhNebTzeGCxDDAkEmX%2BkKihLxDLBTNg%2BVE9gud4fnqa0Hr3nyCeIJRz3dpLTImauLauvfE8pWKRoRjNPVibnOZlmzetbm1r5kT%2FuA%2BllP5cU2hrcFFqByVGEViAjWuNTZI%2FRDf0fiRoDq%2BXZwqfubtPN168dD3AkEbb%2B10LzYVFq2awahehHSyAboOUnWqb3SEx5HpN51qeypdzNX7dQnCHlu3F8dNCDyf5exTseAaGusJX25jpgH3KjKXSLQC618uONn9T3xbbYisGb4dzdhhgRov9RxzzzfXh1qP7O7LKoB0J8F5oQCX2P%2Bw94Tl6V7KkGZUEKOiJyeF07w7R01URE%2B%2Fb2PhkpMHChZWjTiuq5xFZi0V6pYaVzFR%2FowuKTpvQY6pgEUKFhuIF043WdosEhhtDSsaILogiMh6ANqtLteHapoANh1Ee%2F9uAtfv1f1GQ8YkuFPaVv%2FzukOfWYKwbZMbvtAmAAZiUnYaY4Ee%2BRWxBLih0Y5AReSP40jP2Udtdglf%2BXnOF5oac4fsMbulWAPbMMLoN2%2BexRJNktwGVHmVPRyxiwL3%2BoS%2BL0C4d%2BT8FBuan4Xc3tKUPAw9AcFtFfiegfQuL8RvptA&X-Amz-Signature=0c9094c7721d37cb34f4056b2988106760340406240401ba7322987be5a354fb&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXGODSTR%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZn%2FQzowk6M2spQVrYdspmYL4fr%2FOfAOAlzZshdV29NQIgbKO0wX17o05nN4v11BIcmZ8QRyoXOVu89wiQ%2BToSXIAqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdQH%2FpQ12cy89%2BaqyrcA8niozyXNoXiJMjuq7rvcCJ0aXd%2Bro5E91dCguc3EjY29brw5Rg7HKHyMVa7fkrrfPbMqSmGkioy%2BGrmlAW4nyfa95dlcPdqjuuY4Q6TBQeRQ3WqeofVAmPmlFqWI%2BGoBHM0oOg%2BzC9%2B6b1DY%2BtMwMDwFqTKUhzn7djh2vTAbckojI7UKa6qs7ku2bK%2BjTf8GK7RooVKIiwrA6ozLYDP9vkOIjfIFzbel2a9X9U6mheNYxwpnPRVnNBIpvsKO%2FfdTdyV8o6U%2FWgQafdlSVt70qTNNokISRpLVv52s%2FT8MBGMRKTzUZSuD0T9YBvnf6UJ4JYtMGOK5hEKi5xPXalkfK7%2B7WFxj%2Fj%2F3bCNiFuWA7iFz%2BX%2Fqo1IIgKTKsUhKM5s0XR%2Bwst%2BheJUV97K783OX2ktTCQ26in5ZVJNw3pFeW8JrhSvsoLUiJiMj3mFQU%2FSyHBGtEr9drvA6jq9cD4z70TglB95xYveRK1Pv7uTYTOCf1Q7yygf6Isglg4iKONlQq3MNKdRYxXnbkxTu%2BWUKPZC3%2BGkQnXPtSlM%2Fzt4NkqQ9VlF8zPLANHeEkhVR3pN%2BxdGMs0LCLsQz8z7it1%2FftJKG0cVEgEf4NBu%2FL9zOZAPsc1M%2FFbs%2FjtiGarYMLyn6b0GOqUBJC2ElUhLcMLEZlE%2BoZ5N72lAKf13NyUxKAHVwcdMKgAUmr9Pb3vo6V6fhh2jHhoin0JPpB0tTiNKetmZpCqJap%2B2ZIhNgpeVkEsIlFQ5tJE8ItXEN7Q2Qm6bBD5Gjc4eOf7xfKeqVBcFvt3LPqt6XA%2FVpQv74HScSPaCQ9juhMQC3%2B1LbUL8vA8gvUMTDTc%2BPyZW135ryk2eiPvq6LQ6kFumbFsn&X-Amz-Signature=9e86c26d548bd2ebbde844eec7aec84aa950fae6fd2a85126a79b2d0d3f2d3f7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXGODSTR%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZn%2FQzowk6M2spQVrYdspmYL4fr%2FOfAOAlzZshdV29NQIgbKO0wX17o05nN4v11BIcmZ8QRyoXOVu89wiQ%2BToSXIAqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDdQH%2FpQ12cy89%2BaqyrcA8niozyXNoXiJMjuq7rvcCJ0aXd%2Bro5E91dCguc3EjY29brw5Rg7HKHyMVa7fkrrfPbMqSmGkioy%2BGrmlAW4nyfa95dlcPdqjuuY4Q6TBQeRQ3WqeofVAmPmlFqWI%2BGoBHM0oOg%2BzC9%2B6b1DY%2BtMwMDwFqTKUhzn7djh2vTAbckojI7UKa6qs7ku2bK%2BjTf8GK7RooVKIiwrA6ozLYDP9vkOIjfIFzbel2a9X9U6mheNYxwpnPRVnNBIpvsKO%2FfdTdyV8o6U%2FWgQafdlSVt70qTNNokISRpLVv52s%2FT8MBGMRKTzUZSuD0T9YBvnf6UJ4JYtMGOK5hEKi5xPXalkfK7%2B7WFxj%2Fj%2F3bCNiFuWA7iFz%2BX%2Fqo1IIgKTKsUhKM5s0XR%2Bwst%2BheJUV97K783OX2ktTCQ26in5ZVJNw3pFeW8JrhSvsoLUiJiMj3mFQU%2FSyHBGtEr9drvA6jq9cD4z70TglB95xYveRK1Pv7uTYTOCf1Q7yygf6Isglg4iKONlQq3MNKdRYxXnbkxTu%2BWUKPZC3%2BGkQnXPtSlM%2Fzt4NkqQ9VlF8zPLANHeEkhVR3pN%2BxdGMs0LCLsQz8z7it1%2FftJKG0cVEgEf4NBu%2FL9zOZAPsc1M%2FFbs%2FjtiGarYMLyn6b0GOqUBJC2ElUhLcMLEZlE%2BoZ5N72lAKf13NyUxKAHVwcdMKgAUmr9Pb3vo6V6fhh2jHhoin0JPpB0tTiNKetmZpCqJap%2B2ZIhNgpeVkEsIlFQ5tJE8ItXEN7Q2Qm6bBD5Gjc4eOf7xfKeqVBcFvt3LPqt6XA%2FVpQv74HScSPaCQ9juhMQC3%2B1LbUL8vA8gvUMTDTc%2BPyZW135ryk2eiPvq6LQ6kFumbFsn&X-Amz-Signature=3737c34f5a4ac1f042bd3abe2d10acff25d006149ba48832127e3f5f7a45dfa6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQRSXI2G%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFcfuhUpRLMCPb558c6fsVNabwgVzhsEA85sGzFh%2BMx3AiBKLm%2BrWanRnM2ukNkJXAqNdQ3DrvBo1jguh%2BZle9C9AiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Fy%2Bn9nFLqekGusWzKtwDba26RvMkJIagYoPYTwgaTjVGoXsBW5zeTg%2F6IhT3l9j5Xq%2B1qPn78g0DbFm0MbtOYK45jh6WYviVpawm2Y5IomuEeemuthcbIjWRFKU9v0VXoUg7YatsmjMX%2BdW7MjS7aR65AfVTjPRcMeTEVPD7PPUIuwed%2FHd2CMy%2Bilvucw5rKR1YrCYHQPgCSE1aTDAy8g08qeU2eFkJT4zpIDMS2iWUzVFnOmWQjKnT3d7NneiNAK2BUhJ9d3HX2QGJrRjyhNebTzeGCxDDAkEmX%2BkKihLxDLBTNg%2BVE9gud4fnqa0Hr3nyCeIJRz3dpLTImauLauvfE8pWKRoRjNPVibnOZlmzetbm1r5kT%2FuA%2BllP5cU2hrcFFqByVGEViAjWuNTZI%2FRDf0fiRoDq%2BXZwqfubtPN168dD3AkEbb%2B10LzYVFq2awahehHSyAboOUnWqb3SEx5HpN51qeypdzNX7dQnCHlu3F8dNCDyf5exTseAaGusJX25jpgH3KjKXSLQC618uONn9T3xbbYisGb4dzdhhgRov9RxzzzfXh1qP7O7LKoB0J8F5oQCX2P%2Bw94Tl6V7KkGZUEKOiJyeF07w7R01URE%2B%2Fb2PhkpMHChZWjTiuq5xFZi0V6pYaVzFR%2FowuKTpvQY6pgEUKFhuIF043WdosEhhtDSsaILogiMh6ANqtLteHapoANh1Ee%2F9uAtfv1f1GQ8YkuFPaVv%2FzukOfWYKwbZMbvtAmAAZiUnYaY4Ee%2BRWxBLih0Y5AReSP40jP2Udtdglf%2BXnOF5oac4fsMbulWAPbMMLoN2%2BexRJNktwGVHmVPRyxiwL3%2BoS%2BL0C4d%2BT8FBuan4Xc3tKUPAw9AcFtFfiegfQuL8RvptA&X-Amz-Signature=63dfefcff3c833561ebaab233ebd3db46fe8bd6ffc01750673db9f4b3a92a554&X-Amz-SignedHeaders=host&x-id=GetObject)
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