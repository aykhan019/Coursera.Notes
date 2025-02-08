

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW5POXT2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQD66faJ1HDSmZ03ANd%2F2BsmppYgbibLWc1OSWUuod8G5wIgI3FTGV670a20wtxDSlToNHSMiSrlvX%2Fj3moqIXQwTrIqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGhO3bn12KM8%2FZ%2BD6CrcA7Qvl3A0lmu7yFlpq%2BjdzSmP%2FwjiBEXkBtdhynRWbS4SBGW48OBYRi6iOArNChOiEoAJZ83%2F%2FbLhIWq4x%2FUpyKO4wJCDZ5gyg8NTezUbjuuShsH6rRafh1blePI%2F9DL86sIPvxfdC1SuAZZkmpkQzGdPgM6CPh1gryOk4V%2BqIg%2BFam8503tyY%2FOmo9dOf8E5Qzl2mZIkeAw2eod5ij4b9cpaCvLFNXcQH48ntE%2BsNh5m6vzNjucDeMz49IrafjdLrjmrI2qy7pavPp836naJKCqLXk1YEn69mDtsFqsuQ1Gt6rMoDpEXObK8C5XtNZKnOn7zLeuJwh%2Bqbdnx2z%2F%2FYq5qcxF7GU1HzcspyEaNSjUu%2FtLH0ddNdK0VOyt9mJpmE8c195MARzi3plV0DCKBZV13dyEC0EJt3DLov2%2FoDcE2rsBMShNtZ%2B2R%2Bxj6w%2FWLNuZ8R3Vd68evUT8buj6TJ8mZru%2BzXGMTXJtIyWvjQyb%2BR%2F%2FtV1X18TGOCSs3RW2xdOb2Y%2FpnAla0qTBliMS0i4xupgwSwcdXYp7F0EOe%2BI6IGJqeiql0iumg78gOlHDLuJc1GbhnMapYA9jvLFKGkJtS1%2FXZAwbfEEC9m5uKgVbXULSXrmqCB1XI2dKiMK3Um70GOqUB5ASaewDMcqmYT4Wh4KbyLzxjyiJ2dfQSNtSxkVxjfuQb3n%2F4H8535C2d2UnbDrnkNYuUNw5OXH3TWpTQTb5SZr%2BdlEx%2FLbe%2FB9YrKHcx6yoA3EMqkncH6CgArp%2B8xbvp5NjJNklUPOM%2BrDugKxMHBBF2gtq0bIoZd%2Bh8YHnGs%2B2qnLXLV4M9a8abLlYCDUBPmqW3g3hT%2BGTAS1ciUyNG4EQikR2x&X-Amz-Signature=61efc92a4cc1a65525355e42a9080cbb486efd4fbb9d28c66651ef9904ffe556&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW5POXT2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQD66faJ1HDSmZ03ANd%2F2BsmppYgbibLWc1OSWUuod8G5wIgI3FTGV670a20wtxDSlToNHSMiSrlvX%2Fj3moqIXQwTrIqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGhO3bn12KM8%2FZ%2BD6CrcA7Qvl3A0lmu7yFlpq%2BjdzSmP%2FwjiBEXkBtdhynRWbS4SBGW48OBYRi6iOArNChOiEoAJZ83%2F%2FbLhIWq4x%2FUpyKO4wJCDZ5gyg8NTezUbjuuShsH6rRafh1blePI%2F9DL86sIPvxfdC1SuAZZkmpkQzGdPgM6CPh1gryOk4V%2BqIg%2BFam8503tyY%2FOmo9dOf8E5Qzl2mZIkeAw2eod5ij4b9cpaCvLFNXcQH48ntE%2BsNh5m6vzNjucDeMz49IrafjdLrjmrI2qy7pavPp836naJKCqLXk1YEn69mDtsFqsuQ1Gt6rMoDpEXObK8C5XtNZKnOn7zLeuJwh%2Bqbdnx2z%2F%2FYq5qcxF7GU1HzcspyEaNSjUu%2FtLH0ddNdK0VOyt9mJpmE8c195MARzi3plV0DCKBZV13dyEC0EJt3DLov2%2FoDcE2rsBMShNtZ%2B2R%2Bxj6w%2FWLNuZ8R3Vd68evUT8buj6TJ8mZru%2BzXGMTXJtIyWvjQyb%2BR%2F%2FtV1X18TGOCSs3RW2xdOb2Y%2FpnAla0qTBliMS0i4xupgwSwcdXYp7F0EOe%2BI6IGJqeiql0iumg78gOlHDLuJc1GbhnMapYA9jvLFKGkJtS1%2FXZAwbfEEC9m5uKgVbXULSXrmqCB1XI2dKiMK3Um70GOqUB5ASaewDMcqmYT4Wh4KbyLzxjyiJ2dfQSNtSxkVxjfuQb3n%2F4H8535C2d2UnbDrnkNYuUNw5OXH3TWpTQTb5SZr%2BdlEx%2FLbe%2FB9YrKHcx6yoA3EMqkncH6CgArp%2B8xbvp5NjJNklUPOM%2BrDugKxMHBBF2gtq0bIoZd%2Bh8YHnGs%2B2qnLXLV4M9a8abLlYCDUBPmqW3g3hT%2BGTAS1ciUyNG4EQikR2x&X-Amz-Signature=2f065b8a864a3880a5e94d3c3aa5fc92be4867a65503051015f4717aacff3126&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW5POXT2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQD66faJ1HDSmZ03ANd%2F2BsmppYgbibLWc1OSWUuod8G5wIgI3FTGV670a20wtxDSlToNHSMiSrlvX%2Fj3moqIXQwTrIqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGhO3bn12KM8%2FZ%2BD6CrcA7Qvl3A0lmu7yFlpq%2BjdzSmP%2FwjiBEXkBtdhynRWbS4SBGW48OBYRi6iOArNChOiEoAJZ83%2F%2FbLhIWq4x%2FUpyKO4wJCDZ5gyg8NTezUbjuuShsH6rRafh1blePI%2F9DL86sIPvxfdC1SuAZZkmpkQzGdPgM6CPh1gryOk4V%2BqIg%2BFam8503tyY%2FOmo9dOf8E5Qzl2mZIkeAw2eod5ij4b9cpaCvLFNXcQH48ntE%2BsNh5m6vzNjucDeMz49IrafjdLrjmrI2qy7pavPp836naJKCqLXk1YEn69mDtsFqsuQ1Gt6rMoDpEXObK8C5XtNZKnOn7zLeuJwh%2Bqbdnx2z%2F%2FYq5qcxF7GU1HzcspyEaNSjUu%2FtLH0ddNdK0VOyt9mJpmE8c195MARzi3plV0DCKBZV13dyEC0EJt3DLov2%2FoDcE2rsBMShNtZ%2B2R%2Bxj6w%2FWLNuZ8R3Vd68evUT8buj6TJ8mZru%2BzXGMTXJtIyWvjQyb%2BR%2F%2FtV1X18TGOCSs3RW2xdOb2Y%2FpnAla0qTBliMS0i4xupgwSwcdXYp7F0EOe%2BI6IGJqeiql0iumg78gOlHDLuJc1GbhnMapYA9jvLFKGkJtS1%2FXZAwbfEEC9m5uKgVbXULSXrmqCB1XI2dKiMK3Um70GOqUB5ASaewDMcqmYT4Wh4KbyLzxjyiJ2dfQSNtSxkVxjfuQb3n%2F4H8535C2d2UnbDrnkNYuUNw5OXH3TWpTQTb5SZr%2BdlEx%2FLbe%2FB9YrKHcx6yoA3EMqkncH6CgArp%2B8xbvp5NjJNklUPOM%2BrDugKxMHBBF2gtq0bIoZd%2Bh8YHnGs%2B2qnLXLV4M9a8abLlYCDUBPmqW3g3hT%2BGTAS1ciUyNG4EQikR2x&X-Amz-Signature=a5740b15d5f17234998dc07ad7d8d51855083c6fb950563e0396a3086548d604&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K3P6YHO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQC%2BoYI04CLtLwblrh2lHHw9N3HXL%2FL7VQyGzPwTAAhUOQIgbXaNSl36hLjHDYZbniCwXvNTYGx0daR1d7jwYyFmu7UqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGBvx1QS383YM2BW6SrcA5A3DzQQpqccUOtBa6ermknXoQcK5P14BJavE2BcFhJyesAr3lSVEv%2FlfzWELRnR4DNuwe67PlPiQJhPMgLBUv2Hj6x2XSFd%2BRJqe3nUsn3qkXA64gBvQyPtQgslnlFH2ztvEkZBYUTi7JFffhA9%2F%2BkHnz9XQD6phTYbCaxF3DciBtx%2FhLFOOI1G0qV4RD6%2BISu%2B8oKkPXRiRIv%2BIadq0uOIupsTGZV988yBXrDkKzHqWQSjEc4GK7F1x8fR37l1CcPaLyzOCorw4FDteRQjlSgsqxqsj%2FaUI%2FBDmZf9%2BTsjTxUxEJQwgXKhQuUGL0ITgpyfAG7Hp1RSbsLvwm6tNju%2FPb8ziB2p0dCCyT3AARe9YVC7O7TV4cJuIMOEtx76f%2BdS%2FuHY2lsFtsFx2hk6vqNcVhTzdl2ibY6TQ7uT%2FB34KaenXWIUYPIIBxOJuW3A1E%2BsFDGihoJs4ogoPBKA6UVDyqxp%2FdQ1tsoGbeNPVcTQXWrBkDGKtGXiD2yL7vBuOBtHWUoIXx9Mx7t3dwX3jpgyNOQtxj0nkC0EJptF7PXCpGvtCLcRacpTmdR9pu%2FdyGR7n5iFyqq8u6BEYOB826P1c9yv4RL0s6C1ofM4r%2FZpkPGid0vbmQ4R0gcoMMnUm70GOqUByaGPsvvCPXXfXPmKQ3BTwRmRor%2FN7coBeZVZos04eJUPpqQFBK1LBUWvEn7xQDbliQGLVy0DGehA4pJYwdOLHQ0uHk5QcUV3rkI8WF3l0caFfqDmILay9mauIqO02Go0RK4fvkoFeW43q%2FhZUfM1UCeXYyRE02bZqgpQMae%2FmPHyd0ScMhRiJDIX2e2Tnkaitg6zi1zOCUxlL7x4nfQwkqSvwFVg&X-Amz-Signature=c73edcd106adad03d26c342925cfa3c7028e62773413386dccdf003621223495&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K3P6YHO%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQC%2BoYI04CLtLwblrh2lHHw9N3HXL%2FL7VQyGzPwTAAhUOQIgbXaNSl36hLjHDYZbniCwXvNTYGx0daR1d7jwYyFmu7UqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGBvx1QS383YM2BW6SrcA5A3DzQQpqccUOtBa6ermknXoQcK5P14BJavE2BcFhJyesAr3lSVEv%2FlfzWELRnR4DNuwe67PlPiQJhPMgLBUv2Hj6x2XSFd%2BRJqe3nUsn3qkXA64gBvQyPtQgslnlFH2ztvEkZBYUTi7JFffhA9%2F%2BkHnz9XQD6phTYbCaxF3DciBtx%2FhLFOOI1G0qV4RD6%2BISu%2B8oKkPXRiRIv%2BIadq0uOIupsTGZV988yBXrDkKzHqWQSjEc4GK7F1x8fR37l1CcPaLyzOCorw4FDteRQjlSgsqxqsj%2FaUI%2FBDmZf9%2BTsjTxUxEJQwgXKhQuUGL0ITgpyfAG7Hp1RSbsLvwm6tNju%2FPb8ziB2p0dCCyT3AARe9YVC7O7TV4cJuIMOEtx76f%2BdS%2FuHY2lsFtsFx2hk6vqNcVhTzdl2ibY6TQ7uT%2FB34KaenXWIUYPIIBxOJuW3A1E%2BsFDGihoJs4ogoPBKA6UVDyqxp%2FdQ1tsoGbeNPVcTQXWrBkDGKtGXiD2yL7vBuOBtHWUoIXx9Mx7t3dwX3jpgyNOQtxj0nkC0EJptF7PXCpGvtCLcRacpTmdR9pu%2FdyGR7n5iFyqq8u6BEYOB826P1c9yv4RL0s6C1ofM4r%2FZpkPGid0vbmQ4R0gcoMMnUm70GOqUByaGPsvvCPXXfXPmKQ3BTwRmRor%2FN7coBeZVZos04eJUPpqQFBK1LBUWvEn7xQDbliQGLVy0DGehA4pJYwdOLHQ0uHk5QcUV3rkI8WF3l0caFfqDmILay9mauIqO02Go0RK4fvkoFeW43q%2FhZUfM1UCeXYyRE02bZqgpQMae%2FmPHyd0ScMhRiJDIX2e2Tnkaitg6zi1zOCUxlL7x4nfQwkqSvwFVg&X-Amz-Signature=c2ae27a9ecc35d0086b20879b57c547e7d5cd4b34e67feda448b2d9c5a23e4a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RW5POXT2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQD66faJ1HDSmZ03ANd%2F2BsmppYgbibLWc1OSWUuod8G5wIgI3FTGV670a20wtxDSlToNHSMiSrlvX%2Fj3moqIXQwTrIqiAQIhv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGhO3bn12KM8%2FZ%2BD6CrcA7Qvl3A0lmu7yFlpq%2BjdzSmP%2FwjiBEXkBtdhynRWbS4SBGW48OBYRi6iOArNChOiEoAJZ83%2F%2FbLhIWq4x%2FUpyKO4wJCDZ5gyg8NTezUbjuuShsH6rRafh1blePI%2F9DL86sIPvxfdC1SuAZZkmpkQzGdPgM6CPh1gryOk4V%2BqIg%2BFam8503tyY%2FOmo9dOf8E5Qzl2mZIkeAw2eod5ij4b9cpaCvLFNXcQH48ntE%2BsNh5m6vzNjucDeMz49IrafjdLrjmrI2qy7pavPp836naJKCqLXk1YEn69mDtsFqsuQ1Gt6rMoDpEXObK8C5XtNZKnOn7zLeuJwh%2Bqbdnx2z%2F%2FYq5qcxF7GU1HzcspyEaNSjUu%2FtLH0ddNdK0VOyt9mJpmE8c195MARzi3plV0DCKBZV13dyEC0EJt3DLov2%2FoDcE2rsBMShNtZ%2B2R%2Bxj6w%2FWLNuZ8R3Vd68evUT8buj6TJ8mZru%2BzXGMTXJtIyWvjQyb%2BR%2F%2FtV1X18TGOCSs3RW2xdOb2Y%2FpnAla0qTBliMS0i4xupgwSwcdXYp7F0EOe%2BI6IGJqeiql0iumg78gOlHDLuJc1GbhnMapYA9jvLFKGkJtS1%2FXZAwbfEEC9m5uKgVbXULSXrmqCB1XI2dKiMK3Um70GOqUB5ASaewDMcqmYT4Wh4KbyLzxjyiJ2dfQSNtSxkVxjfuQb3n%2F4H8535C2d2UnbDrnkNYuUNw5OXH3TWpTQTb5SZr%2BdlEx%2FLbe%2FB9YrKHcx6yoA3EMqkncH6CgArp%2B8xbvp5NjJNklUPOM%2BrDugKxMHBBF2gtq0bIoZd%2Bh8YHnGs%2B2qnLXLV4M9a8abLlYCDUBPmqW3g3hT%2BGTAS1ciUyNG4EQikR2x&X-Amz-Signature=7400e32de7e46b24f2e4dc2cf449a6d89146cb4bfa2333f6a90f2ff52d3006ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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