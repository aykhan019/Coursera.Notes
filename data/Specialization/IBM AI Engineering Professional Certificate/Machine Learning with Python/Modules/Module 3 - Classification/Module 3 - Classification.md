

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNI7QWW3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCb0Esbsnb1Ekvsa7qkZwEOspD12zRIqFSaadrsOnsstgIhAMWf9y1EZtwginNLROusrMIIU32g2Gc7GPMv6mKavNlDKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZdDaK34YMrI0dN4Mq3APRtk2tUVtKzTMNa8nCxZ4vFVfTcwY0CJKcEAXtbt40L6bKov8NWGTN%2FGvzS3d2Q0fZP%2FS8oWPR%2FDdy81ImOkdsijbq0YxBKkvJssM9eo8PWyUG3caO10IT96BvtTGlohMDIaB4irhcOVwpI6g%2FoFvde9t77G93IkHScDcHKLz2ZN4f0GJKf5C8NH%2FYYUMdWBAgpba3fz6Mvyi4cNSO98vIIHp5qZlwE%2F%2FTsn1FIh4UQzDvNvNTOpu7EaRKBszrpwFyg4cOkdsNuKhwOWigyEqhy%2FWtpZ6yJ02BRkFkpacoW1%2ByCYqfau0DpQrwdy5qi0sMWvrJdUrdUS7juEM1R27JpIulpS0Hl6zv1uRkVtSrUQe09PWHI6CAmarYcTUQTwhMiFhQCkobqGtPMeA5H8jbDE2Le%2F1crTEbold2o2qCkMNGsWAt52fJ3zu72M1h6q98tTMMq2d3wC6ucmI8BmBBvuamR1%2FlmAJQPvlxnOiGBsWhQvt5wNe%2BAgN5KfuMSFOZaM4%2Bh1MCaalLZGCDgK77WpPyVWPemaowIK8plrU1ja8Cm5sbCaSPJu7ci7YaLhcCYxKSF8E6tVE%2BoeJeT8qANRYRuCMnoakZc1DuajEO71eQkpX7mJ4gDQ%2BmnjCg6%2By8BjqkAdMF9Y%2BZz5OMvRBvC0Qkl1WW5qQZVtaQBy566xPmMAIU6uWUgHw1BCVlKJM9YGyzwmgh2VPxCSj9Dik2wxemuV6NKfRLtzZFmN%2FC%2BwReIyrPFCchfY7CoaeelqFifIptH0KD1E6c3ANGLDkmc62Kbe7DL17wjVYM3Gh%2Bl5s1LAy8487FFFaS6u9st%2BwIvdHAZPx%2F20j3e8uqpjtF%2BK418IQJ7LAd&X-Amz-Signature=ac9c90b78b1bc6a0a0f1c7abc17fc4171cf8b8ca062f617037db15108db2f60b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNI7QWW3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCb0Esbsnb1Ekvsa7qkZwEOspD12zRIqFSaadrsOnsstgIhAMWf9y1EZtwginNLROusrMIIU32g2Gc7GPMv6mKavNlDKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZdDaK34YMrI0dN4Mq3APRtk2tUVtKzTMNa8nCxZ4vFVfTcwY0CJKcEAXtbt40L6bKov8NWGTN%2FGvzS3d2Q0fZP%2FS8oWPR%2FDdy81ImOkdsijbq0YxBKkvJssM9eo8PWyUG3caO10IT96BvtTGlohMDIaB4irhcOVwpI6g%2FoFvde9t77G93IkHScDcHKLz2ZN4f0GJKf5C8NH%2FYYUMdWBAgpba3fz6Mvyi4cNSO98vIIHp5qZlwE%2F%2FTsn1FIh4UQzDvNvNTOpu7EaRKBszrpwFyg4cOkdsNuKhwOWigyEqhy%2FWtpZ6yJ02BRkFkpacoW1%2ByCYqfau0DpQrwdy5qi0sMWvrJdUrdUS7juEM1R27JpIulpS0Hl6zv1uRkVtSrUQe09PWHI6CAmarYcTUQTwhMiFhQCkobqGtPMeA5H8jbDE2Le%2F1crTEbold2o2qCkMNGsWAt52fJ3zu72M1h6q98tTMMq2d3wC6ucmI8BmBBvuamR1%2FlmAJQPvlxnOiGBsWhQvt5wNe%2BAgN5KfuMSFOZaM4%2Bh1MCaalLZGCDgK77WpPyVWPemaowIK8plrU1ja8Cm5sbCaSPJu7ci7YaLhcCYxKSF8E6tVE%2BoeJeT8qANRYRuCMnoakZc1DuajEO71eQkpX7mJ4gDQ%2BmnjCg6%2By8BjqkAdMF9Y%2BZz5OMvRBvC0Qkl1WW5qQZVtaQBy566xPmMAIU6uWUgHw1BCVlKJM9YGyzwmgh2VPxCSj9Dik2wxemuV6NKfRLtzZFmN%2FC%2BwReIyrPFCchfY7CoaeelqFifIptH0KD1E6c3ANGLDkmc62Kbe7DL17wjVYM3Gh%2Bl5s1LAy8487FFFaS6u9st%2BwIvdHAZPx%2F20j3e8uqpjtF%2BK418IQJ7LAd&X-Amz-Signature=cdca4a78ab1f2c69b6b8d4e317e27978b2cae14f3b2291bf91a4e947ec2af79a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNI7QWW3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCb0Esbsnb1Ekvsa7qkZwEOspD12zRIqFSaadrsOnsstgIhAMWf9y1EZtwginNLROusrMIIU32g2Gc7GPMv6mKavNlDKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZdDaK34YMrI0dN4Mq3APRtk2tUVtKzTMNa8nCxZ4vFVfTcwY0CJKcEAXtbt40L6bKov8NWGTN%2FGvzS3d2Q0fZP%2FS8oWPR%2FDdy81ImOkdsijbq0YxBKkvJssM9eo8PWyUG3caO10IT96BvtTGlohMDIaB4irhcOVwpI6g%2FoFvde9t77G93IkHScDcHKLz2ZN4f0GJKf5C8NH%2FYYUMdWBAgpba3fz6Mvyi4cNSO98vIIHp5qZlwE%2F%2FTsn1FIh4UQzDvNvNTOpu7EaRKBszrpwFyg4cOkdsNuKhwOWigyEqhy%2FWtpZ6yJ02BRkFkpacoW1%2ByCYqfau0DpQrwdy5qi0sMWvrJdUrdUS7juEM1R27JpIulpS0Hl6zv1uRkVtSrUQe09PWHI6CAmarYcTUQTwhMiFhQCkobqGtPMeA5H8jbDE2Le%2F1crTEbold2o2qCkMNGsWAt52fJ3zu72M1h6q98tTMMq2d3wC6ucmI8BmBBvuamR1%2FlmAJQPvlxnOiGBsWhQvt5wNe%2BAgN5KfuMSFOZaM4%2Bh1MCaalLZGCDgK77WpPyVWPemaowIK8plrU1ja8Cm5sbCaSPJu7ci7YaLhcCYxKSF8E6tVE%2BoeJeT8qANRYRuCMnoakZc1DuajEO71eQkpX7mJ4gDQ%2BmnjCg6%2By8BjqkAdMF9Y%2BZz5OMvRBvC0Qkl1WW5qQZVtaQBy566xPmMAIU6uWUgHw1BCVlKJM9YGyzwmgh2VPxCSj9Dik2wxemuV6NKfRLtzZFmN%2FC%2BwReIyrPFCchfY7CoaeelqFifIptH0KD1E6c3ANGLDkmc62Kbe7DL17wjVYM3Gh%2Bl5s1LAy8487FFFaS6u9st%2BwIvdHAZPx%2F20j3e8uqpjtF%2BK418IQJ7LAd&X-Amz-Signature=82b22b0025a75fc3171f8afc6c192092ca8ad3356ca4b25766e76c86fba3ba30&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYK72FNS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081826Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEJyzQSYM%2FMVYYxvowmn5pRjuLmbaHaC%2FvZ6OVHDx7aAIhALuvjbT7hmw6RLCcC9vFJ2vQgAB4Fj1D4H2LpYwabnF0KogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTjp%2FQM8Yfo5QmQ%2FAq3APp4q5ueKnXqjbix1W%2FBB0Izkbo7L%2B%2Brc52bH8F2OpUz4MQEGSWEuzjsBiLimgedkQyiNNuKP37BIsmxCnDJ6DYqlcu2rA8AxQm7umu3v4Z9ASxgCjYcj01xX26TEnjv3WTYaM8ROwatmrVObzrHv6WG9Ub2ZdIxprMvX9yq9KnQdu8w4y1stUS9FcC0zvIXgEg336NNzpC%2FfMPqEBl6RxlfLvEq%2B3izP13kHmd7sORDmYbRAPAEMxCot3EO9DwWQypDK7rqEx2YG7bFF%2FI1058ZtrmYbN8vA%2Fi9eclPevxbK0q8dmG26xhKpeSb0FufjfMDM0JiCRD1REqdfOkkh4uwH2usxtuM469WPQFUh1aUvUfDhQfSL4doaN3XtuzweA%2F5l%2BgRzC4f8KtmT8KylA1zwhNiRoVYTyu6NNfw0NHbnlrdWZ3haph39FlCQ02E2tqoG4c4CCxxJJ50%2FCkdAS7QJvzlldzbqmy0aaMvU%2BYO9fyp8IodXae1SyB%2FBg2uonNwU9xMdQdF9X8X6O%2Bu8yUY%2BOo%2FvPF1VqX10Hdsejqg74doSXcgu%2Bv%2Bz71hU5ja5N0ThrYrQAM8svjvbxsQwLOfQvIfjU%2BvYmsXwbCkIgpMKq3LrpgnnqEYCUacTDHouy8BjqkAbK5txHSZW5veuYqJMjgBMA9fYSDT1El69rNW172Np9tdBjT4wnwWu1Npa4e40bqsbAnxu91d8%2FPB5JOEKVGjBQJSQs9AimHHX%2BudZF2XEAA7Hmh9CbMYMJZv%2FpmN%2B3gYfgWoqAmJIHDnO17r1Oz%2BLr4O%2Fx7kbpmdr1JBu4FOCJDGQCKKHKWgPtCQLQL3OrFvi1dw0W9tMhpAL5fzNFdAA2IHwX%2F&X-Amz-Signature=746036120ce19b7266ecf7ec77de54fd85398a68ebee8ac1fb1e3b37a6b2504f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYK72FNS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081826Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEJyzQSYM%2FMVYYxvowmn5pRjuLmbaHaC%2FvZ6OVHDx7aAIhALuvjbT7hmw6RLCcC9vFJ2vQgAB4Fj1D4H2LpYwabnF0KogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzTjp%2FQM8Yfo5QmQ%2FAq3APp4q5ueKnXqjbix1W%2FBB0Izkbo7L%2B%2Brc52bH8F2OpUz4MQEGSWEuzjsBiLimgedkQyiNNuKP37BIsmxCnDJ6DYqlcu2rA8AxQm7umu3v4Z9ASxgCjYcj01xX26TEnjv3WTYaM8ROwatmrVObzrHv6WG9Ub2ZdIxprMvX9yq9KnQdu8w4y1stUS9FcC0zvIXgEg336NNzpC%2FfMPqEBl6RxlfLvEq%2B3izP13kHmd7sORDmYbRAPAEMxCot3EO9DwWQypDK7rqEx2YG7bFF%2FI1058ZtrmYbN8vA%2Fi9eclPevxbK0q8dmG26xhKpeSb0FufjfMDM0JiCRD1REqdfOkkh4uwH2usxtuM469WPQFUh1aUvUfDhQfSL4doaN3XtuzweA%2F5l%2BgRzC4f8KtmT8KylA1zwhNiRoVYTyu6NNfw0NHbnlrdWZ3haph39FlCQ02E2tqoG4c4CCxxJJ50%2FCkdAS7QJvzlldzbqmy0aaMvU%2BYO9fyp8IodXae1SyB%2FBg2uonNwU9xMdQdF9X8X6O%2Bu8yUY%2BOo%2FvPF1VqX10Hdsejqg74doSXcgu%2Bv%2Bz71hU5ja5N0ThrYrQAM8svjvbxsQwLOfQvIfjU%2BvYmsXwbCkIgpMKq3LrpgnnqEYCUacTDHouy8BjqkAbK5txHSZW5veuYqJMjgBMA9fYSDT1El69rNW172Np9tdBjT4wnwWu1Npa4e40bqsbAnxu91d8%2FPB5JOEKVGjBQJSQs9AimHHX%2BudZF2XEAA7Hmh9CbMYMJZv%2FpmN%2B3gYfgWoqAmJIHDnO17r1Oz%2BLr4O%2Fx7kbpmdr1JBu4FOCJDGQCKKHKWgPtCQLQL3OrFvi1dw0W9tMhpAL5fzNFdAA2IHwX%2F&X-Amz-Signature=5e7912593ca04dc022210adf2be6ef5060102a285cdc4d3b8db56275bc556b86&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNI7QWW3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCb0Esbsnb1Ekvsa7qkZwEOspD12zRIqFSaadrsOnsstgIhAMWf9y1EZtwginNLROusrMIIU32g2Gc7GPMv6mKavNlDKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZdDaK34YMrI0dN4Mq3APRtk2tUVtKzTMNa8nCxZ4vFVfTcwY0CJKcEAXtbt40L6bKov8NWGTN%2FGvzS3d2Q0fZP%2FS8oWPR%2FDdy81ImOkdsijbq0YxBKkvJssM9eo8PWyUG3caO10IT96BvtTGlohMDIaB4irhcOVwpI6g%2FoFvde9t77G93IkHScDcHKLz2ZN4f0GJKf5C8NH%2FYYUMdWBAgpba3fz6Mvyi4cNSO98vIIHp5qZlwE%2F%2FTsn1FIh4UQzDvNvNTOpu7EaRKBszrpwFyg4cOkdsNuKhwOWigyEqhy%2FWtpZ6yJ02BRkFkpacoW1%2ByCYqfau0DpQrwdy5qi0sMWvrJdUrdUS7juEM1R27JpIulpS0Hl6zv1uRkVtSrUQe09PWHI6CAmarYcTUQTwhMiFhQCkobqGtPMeA5H8jbDE2Le%2F1crTEbold2o2qCkMNGsWAt52fJ3zu72M1h6q98tTMMq2d3wC6ucmI8BmBBvuamR1%2FlmAJQPvlxnOiGBsWhQvt5wNe%2BAgN5KfuMSFOZaM4%2Bh1MCaalLZGCDgK77WpPyVWPemaowIK8plrU1ja8Cm5sbCaSPJu7ci7YaLhcCYxKSF8E6tVE%2BoeJeT8qANRYRuCMnoakZc1DuajEO71eQkpX7mJ4gDQ%2BmnjCg6%2By8BjqkAdMF9Y%2BZz5OMvRBvC0Qkl1WW5qQZVtaQBy566xPmMAIU6uWUgHw1BCVlKJM9YGyzwmgh2VPxCSj9Dik2wxemuV6NKfRLtzZFmN%2FC%2BwReIyrPFCchfY7CoaeelqFifIptH0KD1E6c3ANGLDkmc62Kbe7DL17wjVYM3Gh%2Bl5s1LAy8487FFFaS6u9st%2BwIvdHAZPx%2F20j3e8uqpjtF%2BK418IQJ7LAd&X-Amz-Signature=ee4e4b52322d4d9779556474f153d57846a0ec8631033fe0a06d0ca8f372bf9b&X-Amz-SignedHeaders=host&x-id=GetObject)
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