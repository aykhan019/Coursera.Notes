

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLY3KNED%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQCPGq241jfZ0b%2FmelWyy%2FaH%2FdAaZhaE7yrKvWFNQ82J3wIhAM0dsH%2B8XRhB%2BQcT%2FpSGZBotnysUmh09BVXLlfozZf%2BKKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzhlUlqgbYTDHqGWvcq3AMsEewM6wgLZB4GO7%2FMcOCtbsz3r7ckZ9ZleyRrM5gsmKTwNIBZqMTmw1gGj7EMaEVlEIouc%2Fd%2FWT8VQzBfPaJAESE%2FXoTp%2BsSYfnx%2BbsqatqhO3am%2B0I3lco1GfPjACB5UvmDR4cPRW1EKx5Gz1mJ8S2pggFv5uHVQZtRRVXcS6i9RmKEBnW%2FEkQyleYOU0BSFbl446s7SWmznR6WznG5KA0rQ2QuDK3XjoJ2mLqRq3WtKYJ9h1bFwdnH8WFKoAowxXhr3ZNwjs2Y2hWJUhaAcF6d5p5gumSvX6xGH1m1eRxDFi6GI83tY%2BZg64XqLn8yywSJp8cRtW4BB4ZiSZLD7poqi7N2hfmggizcOPLNqQgV6jZ30MRjs225VTV8ypkUM2KQcZWBkQZZa0EtvPxU1KUestndnLivotQPiaCudO7QNXpZgv66NXDy3JLFgS6IeDJzFD7vN4pfsHGxYKwJ8UiByyVG4zYzm4HZxAM1ZajivTgQcLsgoV81Ra0vMj78DXcQSYufs%2BvXDNxK3lgE6VEMj0J2Xldqx9UF8EI82IVAFHBYlJs5OgTOkMyYYUzm4UtZIsrxmEMOstYJzaoUrsy%2FWfrh7jLXDJOqtln1l56abmWKWMA5mYtD8czDAt46%2BBjqkASTIByYKHcb0pEr2KXTr4VN0psWzKsnJ2i%2BQLqjwk1sBOV8gkcj2U0ecPam%2FXtqjnzqbIxeFEWJR%2BLvQRfqPeNteucg0NM1IdW6m123wWsUMK0cly48U%2FvRdtHMaHn%2FGpJyPJWOuuH612tE3A1%2FzIul2TD%2BvOSPQvNPcH3DornpGMrq%2BItIg53knMmjV%2FaWXnTOqmpnr8LF%2FkPpWpN0m%2FJ97Zpdz&X-Amz-Signature=acccfd2f9ce2015eb1c818adf64cea0ad34f32a0008f3050153d0015e3e5f315&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLY3KNED%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQCPGq241jfZ0b%2FmelWyy%2FaH%2FdAaZhaE7yrKvWFNQ82J3wIhAM0dsH%2B8XRhB%2BQcT%2FpSGZBotnysUmh09BVXLlfozZf%2BKKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzhlUlqgbYTDHqGWvcq3AMsEewM6wgLZB4GO7%2FMcOCtbsz3r7ckZ9ZleyRrM5gsmKTwNIBZqMTmw1gGj7EMaEVlEIouc%2Fd%2FWT8VQzBfPaJAESE%2FXoTp%2BsSYfnx%2BbsqatqhO3am%2B0I3lco1GfPjACB5UvmDR4cPRW1EKx5Gz1mJ8S2pggFv5uHVQZtRRVXcS6i9RmKEBnW%2FEkQyleYOU0BSFbl446s7SWmznR6WznG5KA0rQ2QuDK3XjoJ2mLqRq3WtKYJ9h1bFwdnH8WFKoAowxXhr3ZNwjs2Y2hWJUhaAcF6d5p5gumSvX6xGH1m1eRxDFi6GI83tY%2BZg64XqLn8yywSJp8cRtW4BB4ZiSZLD7poqi7N2hfmggizcOPLNqQgV6jZ30MRjs225VTV8ypkUM2KQcZWBkQZZa0EtvPxU1KUestndnLivotQPiaCudO7QNXpZgv66NXDy3JLFgS6IeDJzFD7vN4pfsHGxYKwJ8UiByyVG4zYzm4HZxAM1ZajivTgQcLsgoV81Ra0vMj78DXcQSYufs%2BvXDNxK3lgE6VEMj0J2Xldqx9UF8EI82IVAFHBYlJs5OgTOkMyYYUzm4UtZIsrxmEMOstYJzaoUrsy%2FWfrh7jLXDJOqtln1l56abmWKWMA5mYtD8czDAt46%2BBjqkASTIByYKHcb0pEr2KXTr4VN0psWzKsnJ2i%2BQLqjwk1sBOV8gkcj2U0ecPam%2FXtqjnzqbIxeFEWJR%2BLvQRfqPeNteucg0NM1IdW6m123wWsUMK0cly48U%2FvRdtHMaHn%2FGpJyPJWOuuH612tE3A1%2FzIul2TD%2BvOSPQvNPcH3DornpGMrq%2BItIg53knMmjV%2FaWXnTOqmpnr8LF%2FkPpWpN0m%2FJ97Zpdz&X-Amz-Signature=c8bd5d217c8851a857a532cd30c32d7c05d74f5cf9a056c9dd2b12002f7a7a70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLY3KNED%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQCPGq241jfZ0b%2FmelWyy%2FaH%2FdAaZhaE7yrKvWFNQ82J3wIhAM0dsH%2B8XRhB%2BQcT%2FpSGZBotnysUmh09BVXLlfozZf%2BKKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzhlUlqgbYTDHqGWvcq3AMsEewM6wgLZB4GO7%2FMcOCtbsz3r7ckZ9ZleyRrM5gsmKTwNIBZqMTmw1gGj7EMaEVlEIouc%2Fd%2FWT8VQzBfPaJAESE%2FXoTp%2BsSYfnx%2BbsqatqhO3am%2B0I3lco1GfPjACB5UvmDR4cPRW1EKx5Gz1mJ8S2pggFv5uHVQZtRRVXcS6i9RmKEBnW%2FEkQyleYOU0BSFbl446s7SWmznR6WznG5KA0rQ2QuDK3XjoJ2mLqRq3WtKYJ9h1bFwdnH8WFKoAowxXhr3ZNwjs2Y2hWJUhaAcF6d5p5gumSvX6xGH1m1eRxDFi6GI83tY%2BZg64XqLn8yywSJp8cRtW4BB4ZiSZLD7poqi7N2hfmggizcOPLNqQgV6jZ30MRjs225VTV8ypkUM2KQcZWBkQZZa0EtvPxU1KUestndnLivotQPiaCudO7QNXpZgv66NXDy3JLFgS6IeDJzFD7vN4pfsHGxYKwJ8UiByyVG4zYzm4HZxAM1ZajivTgQcLsgoV81Ra0vMj78DXcQSYufs%2BvXDNxK3lgE6VEMj0J2Xldqx9UF8EI82IVAFHBYlJs5OgTOkMyYYUzm4UtZIsrxmEMOstYJzaoUrsy%2FWfrh7jLXDJOqtln1l56abmWKWMA5mYtD8czDAt46%2BBjqkASTIByYKHcb0pEr2KXTr4VN0psWzKsnJ2i%2BQLqjwk1sBOV8gkcj2U0ecPam%2FXtqjnzqbIxeFEWJR%2BLvQRfqPeNteucg0NM1IdW6m123wWsUMK0cly48U%2FvRdtHMaHn%2FGpJyPJWOuuH612tE3A1%2FzIul2TD%2BvOSPQvNPcH3DornpGMrq%2BItIg53knMmjV%2FaWXnTOqmpnr8LF%2FkPpWpN0m%2FJ97Zpdz&X-Amz-Signature=ea57a75871bc077d01e5aeb01938503dea634632382df3ef68a9ada7789ad29c&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LM7I7RP%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQDpQJ9ttIFOCJo4pxBzJIX%2BoPLQDc392vSrc05fpnuZMgIhAOSuhNMN4nJPdYuQTXci8sXVgy2fw9SXHB5uJWPfK2dZKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyl9RVUnN9stCddKnsq3ANEdjTipNv4IJ7R4IOnWhDy4HwqApKFdN8w3bkUP6Cyz9S79KFt8dK5T4pZPbWi%2BOK2gtpC33Fb6p1LuGsGcJtQL6vRcKikxcO5ikeHOGm3Fvej0iJBVv2ydim7SCAI9mSoeXpluWoril2ZJtgYj3x6DoxZj9EGM7OcyBDnhHjqW%2FDycxC2iO9iA4crcqY9IJaXtraws%2FZiSZ7uTqTXofxzLexGewCuUCheIJH4gvilpIuf1Zes6uBgYFVwbzhYS5AcAkFcCFiExH1cgFDP%2BHiKOaxhhpjtWP0%2FccodtWHsdGlSio7YTvOJfVlA2NUyduwtJueqWTrVznFS2efrNkbbyxm86MsklllR2fwwRDWjryrY%2FucDT1Uu6ClzGDW9GFg325iK73dokfztIpItbObxxA8MwDuynR9%2FJaLGAINYBM9OZsgSFWwY0o5Tiq9qE8bMMPC7ikclhBwsxeJiUuwr3WfN7z2ieU3ufRyXgZkzCN2ZI%2BHOLA1fzIdQqUuGX8C%2Foxk%2Ba%2Fir5McoTpq68JJQkLkidlq6cN9Z0%2BkXfRU0wRhYLKMo3q5wP7zkklIox5MRtsUjQTidnM52JKQg6z1bGZHApho922XCF3COUf6rcATmeCdapIgCcfQv4jC5t46%2BBjqkAfFcNnAqIyp5Gj3shAbZU%2BaYC98EaXI6F2VeWQhhw702CtuLJOWFZZPEKEp2wmqhkTeWdzI5ZGPyW55qZcyr88tAjd14Vt2Ftdi0BGXOaweD2Mm%2BEIXHjxzp5LE5cP6cDjS7tgFfQv2JuZvgxnGhm18qQD9qqbspg0uIat%2BhAsBke7UVnZIZ1ejf4BNH4Roy5iXE2g%2BO1AbqN0XzF%2Bk6ZStue7la&X-Amz-Signature=e726b4bbd9f342f30f6844c9807abde69b9c120abe913eac611a0973c8ac6c51&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LM7I7RP%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQDpQJ9ttIFOCJo4pxBzJIX%2BoPLQDc392vSrc05fpnuZMgIhAOSuhNMN4nJPdYuQTXci8sXVgy2fw9SXHB5uJWPfK2dZKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyl9RVUnN9stCddKnsq3ANEdjTipNv4IJ7R4IOnWhDy4HwqApKFdN8w3bkUP6Cyz9S79KFt8dK5T4pZPbWi%2BOK2gtpC33Fb6p1LuGsGcJtQL6vRcKikxcO5ikeHOGm3Fvej0iJBVv2ydim7SCAI9mSoeXpluWoril2ZJtgYj3x6DoxZj9EGM7OcyBDnhHjqW%2FDycxC2iO9iA4crcqY9IJaXtraws%2FZiSZ7uTqTXofxzLexGewCuUCheIJH4gvilpIuf1Zes6uBgYFVwbzhYS5AcAkFcCFiExH1cgFDP%2BHiKOaxhhpjtWP0%2FccodtWHsdGlSio7YTvOJfVlA2NUyduwtJueqWTrVznFS2efrNkbbyxm86MsklllR2fwwRDWjryrY%2FucDT1Uu6ClzGDW9GFg325iK73dokfztIpItbObxxA8MwDuynR9%2FJaLGAINYBM9OZsgSFWwY0o5Tiq9qE8bMMPC7ikclhBwsxeJiUuwr3WfN7z2ieU3ufRyXgZkzCN2ZI%2BHOLA1fzIdQqUuGX8C%2Foxk%2Ba%2Fir5McoTpq68JJQkLkidlq6cN9Z0%2BkXfRU0wRhYLKMo3q5wP7zkklIox5MRtsUjQTidnM52JKQg6z1bGZHApho922XCF3COUf6rcATmeCdapIgCcfQv4jC5t46%2BBjqkAfFcNnAqIyp5Gj3shAbZU%2BaYC98EaXI6F2VeWQhhw702CtuLJOWFZZPEKEp2wmqhkTeWdzI5ZGPyW55qZcyr88tAjd14Vt2Ftdi0BGXOaweD2Mm%2BEIXHjxzp5LE5cP6cDjS7tgFfQv2JuZvgxnGhm18qQD9qqbspg0uIat%2BhAsBke7UVnZIZ1ejf4BNH4Roy5iXE2g%2BO1AbqN0XzF%2Bk6ZStue7la&X-Amz-Signature=b203f93b115d5902214328bb04fc04b086730fd001cdedd31d9947fbbe461403&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLY3KNED%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQCPGq241jfZ0b%2FmelWyy%2FaH%2FdAaZhaE7yrKvWFNQ82J3wIhAM0dsH%2B8XRhB%2BQcT%2FpSGZBotnysUmh09BVXLlfozZf%2BKKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzhlUlqgbYTDHqGWvcq3AMsEewM6wgLZB4GO7%2FMcOCtbsz3r7ckZ9ZleyRrM5gsmKTwNIBZqMTmw1gGj7EMaEVlEIouc%2Fd%2FWT8VQzBfPaJAESE%2FXoTp%2BsSYfnx%2BbsqatqhO3am%2B0I3lco1GfPjACB5UvmDR4cPRW1EKx5Gz1mJ8S2pggFv5uHVQZtRRVXcS6i9RmKEBnW%2FEkQyleYOU0BSFbl446s7SWmznR6WznG5KA0rQ2QuDK3XjoJ2mLqRq3WtKYJ9h1bFwdnH8WFKoAowxXhr3ZNwjs2Y2hWJUhaAcF6d5p5gumSvX6xGH1m1eRxDFi6GI83tY%2BZg64XqLn8yywSJp8cRtW4BB4ZiSZLD7poqi7N2hfmggizcOPLNqQgV6jZ30MRjs225VTV8ypkUM2KQcZWBkQZZa0EtvPxU1KUestndnLivotQPiaCudO7QNXpZgv66NXDy3JLFgS6IeDJzFD7vN4pfsHGxYKwJ8UiByyVG4zYzm4HZxAM1ZajivTgQcLsgoV81Ra0vMj78DXcQSYufs%2BvXDNxK3lgE6VEMj0J2Xldqx9UF8EI82IVAFHBYlJs5OgTOkMyYYUzm4UtZIsrxmEMOstYJzaoUrsy%2FWfrh7jLXDJOqtln1l56abmWKWMA5mYtD8czDAt46%2BBjqkASTIByYKHcb0pEr2KXTr4VN0psWzKsnJ2i%2BQLqjwk1sBOV8gkcj2U0ecPam%2FXtqjnzqbIxeFEWJR%2BLvQRfqPeNteucg0NM1IdW6m123wWsUMK0cly48U%2FvRdtHMaHn%2FGpJyPJWOuuH612tE3A1%2FzIul2TD%2BvOSPQvNPcH3DornpGMrq%2BItIg53knMmjV%2FaWXnTOqmpnr8LF%2FkPpWpN0m%2FJ97Zpdz&X-Amz-Signature=dc6c4ec129602ca5bfcaf3f1410adca86763f5b2ea90df527c1449ed19511bb5&X-Amz-SignedHeaders=host&x-id=GetObject)
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