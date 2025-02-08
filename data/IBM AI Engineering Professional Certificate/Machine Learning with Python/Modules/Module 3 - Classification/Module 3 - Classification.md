

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RL5B6PRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIHqXWJThgNOjx3eykc1FmFkIMB4vbb4EJzRez8ZCxX%2BcAiEAlUDjuSy6EAryW0kDVOrmrDVTwdkFnl%2FNoKBpooKdX9MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIXHNye0QSjj%2FYNSfSrcA0QsqhUVsV2B84LDmLDlFp07aBFGBhOw108x%2Bp8a5t%2FGHO3Ub0sM4CrtvlMmWffVTHyXoju2Hf0izhKboFQNWqdl7iwfhljb9wOydvHM4L%2Bn5CIru%2BonJ8oIjQ2cQToRa5A10PIlHS8aT7LtfrBdQck0bOBqxbo4LNtW0o5KS2lySiCrHFRkNI8iSUPEa6lpf0yrrttaEhEABF%2BoHsF1uKdqCVZmJzu0lPAI7hbTIasoxRCOWcqJ%2BrZSmR77IcVFB1TfhaE0ObAiE4%2BKlyLaHan0vrnNETOO5a19A739%2BCc8XurEjX1t4XBcwCFqO6JjUsDQ%2BUWrTYDS29JkTFDzo6ttIpOqq5T9powTm6fS002MGLPRTKoxS7UlQOEbtfCxCXGVSo9aR3BoWFreif%2BAoQaftAXiYtromwLWpPgBvag7N6bL94pxeSqakWkDKEE4CmvqXS9wMWOOzsO80ameWGf3%2BO0V0ID7RuELcZGL1OZM%2Fz29vaNPIanRow0DX94Wm%2Bv84M79lCY1w5QZfTZOQem8Li8zl9kRlPbSAPN51uEHNWAauyGrn0EJF88YLEYAaKpWgg%2BZlMZVOHvkQv4WW2p3j6M7xKSUBxbfuqQvE3xdi7QaDZozhNGlfZpnMNCym70GOqUB%2Fn7HQ5fkHeALYmpKp7nI0aJBdhz2gREvXptrZEYEgDsDv%2FTr5DZVnzY2MMc9Lrxo3EPzF7kUZJmFuh3%2F6rMFbsVplQEv7vY7HVM8i%2BHCtkuy9L1jrkKY0XC1oOHgNlgESkfNjqWkX2wVtOzNwFCXIlLqyIM9jKHt7eKXUomIeT8nDVyVDAZ4OYAdflTkRKDbwmiRPaJAOUn1IrIiHJb9hH318ed8&X-Amz-Signature=c298da907f241acd587011a9321cd5b0bd640d5104a26c7ff6281f7b0fcbf3a0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RL5B6PRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIHqXWJThgNOjx3eykc1FmFkIMB4vbb4EJzRez8ZCxX%2BcAiEAlUDjuSy6EAryW0kDVOrmrDVTwdkFnl%2FNoKBpooKdX9MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIXHNye0QSjj%2FYNSfSrcA0QsqhUVsV2B84LDmLDlFp07aBFGBhOw108x%2Bp8a5t%2FGHO3Ub0sM4CrtvlMmWffVTHyXoju2Hf0izhKboFQNWqdl7iwfhljb9wOydvHM4L%2Bn5CIru%2BonJ8oIjQ2cQToRa5A10PIlHS8aT7LtfrBdQck0bOBqxbo4LNtW0o5KS2lySiCrHFRkNI8iSUPEa6lpf0yrrttaEhEABF%2BoHsF1uKdqCVZmJzu0lPAI7hbTIasoxRCOWcqJ%2BrZSmR77IcVFB1TfhaE0ObAiE4%2BKlyLaHan0vrnNETOO5a19A739%2BCc8XurEjX1t4XBcwCFqO6JjUsDQ%2BUWrTYDS29JkTFDzo6ttIpOqq5T9powTm6fS002MGLPRTKoxS7UlQOEbtfCxCXGVSo9aR3BoWFreif%2BAoQaftAXiYtromwLWpPgBvag7N6bL94pxeSqakWkDKEE4CmvqXS9wMWOOzsO80ameWGf3%2BO0V0ID7RuELcZGL1OZM%2Fz29vaNPIanRow0DX94Wm%2Bv84M79lCY1w5QZfTZOQem8Li8zl9kRlPbSAPN51uEHNWAauyGrn0EJF88YLEYAaKpWgg%2BZlMZVOHvkQv4WW2p3j6M7xKSUBxbfuqQvE3xdi7QaDZozhNGlfZpnMNCym70GOqUB%2Fn7HQ5fkHeALYmpKp7nI0aJBdhz2gREvXptrZEYEgDsDv%2FTr5DZVnzY2MMc9Lrxo3EPzF7kUZJmFuh3%2F6rMFbsVplQEv7vY7HVM8i%2BHCtkuy9L1jrkKY0XC1oOHgNlgESkfNjqWkX2wVtOzNwFCXIlLqyIM9jKHt7eKXUomIeT8nDVyVDAZ4OYAdflTkRKDbwmiRPaJAOUn1IrIiHJb9hH318ed8&X-Amz-Signature=ecdedf046141d1682c78345baa427c48b6828d4b489e64efc97a97c5f4d134f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RL5B6PRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIHqXWJThgNOjx3eykc1FmFkIMB4vbb4EJzRez8ZCxX%2BcAiEAlUDjuSy6EAryW0kDVOrmrDVTwdkFnl%2FNoKBpooKdX9MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIXHNye0QSjj%2FYNSfSrcA0QsqhUVsV2B84LDmLDlFp07aBFGBhOw108x%2Bp8a5t%2FGHO3Ub0sM4CrtvlMmWffVTHyXoju2Hf0izhKboFQNWqdl7iwfhljb9wOydvHM4L%2Bn5CIru%2BonJ8oIjQ2cQToRa5A10PIlHS8aT7LtfrBdQck0bOBqxbo4LNtW0o5KS2lySiCrHFRkNI8iSUPEa6lpf0yrrttaEhEABF%2BoHsF1uKdqCVZmJzu0lPAI7hbTIasoxRCOWcqJ%2BrZSmR77IcVFB1TfhaE0ObAiE4%2BKlyLaHan0vrnNETOO5a19A739%2BCc8XurEjX1t4XBcwCFqO6JjUsDQ%2BUWrTYDS29JkTFDzo6ttIpOqq5T9powTm6fS002MGLPRTKoxS7UlQOEbtfCxCXGVSo9aR3BoWFreif%2BAoQaftAXiYtromwLWpPgBvag7N6bL94pxeSqakWkDKEE4CmvqXS9wMWOOzsO80ameWGf3%2BO0V0ID7RuELcZGL1OZM%2Fz29vaNPIanRow0DX94Wm%2Bv84M79lCY1w5QZfTZOQem8Li8zl9kRlPbSAPN51uEHNWAauyGrn0EJF88YLEYAaKpWgg%2BZlMZVOHvkQv4WW2p3j6M7xKSUBxbfuqQvE3xdi7QaDZozhNGlfZpnMNCym70GOqUB%2Fn7HQ5fkHeALYmpKp7nI0aJBdhz2gREvXptrZEYEgDsDv%2FTr5DZVnzY2MMc9Lrxo3EPzF7kUZJmFuh3%2F6rMFbsVplQEv7vY7HVM8i%2BHCtkuy9L1jrkKY0XC1oOHgNlgESkfNjqWkX2wVtOzNwFCXIlLqyIM9jKHt7eKXUomIeT8nDVyVDAZ4OYAdflTkRKDbwmiRPaJAOUn1IrIiHJb9hH318ed8&X-Amz-Signature=c0eb4c23036380221b7a9790368173879b999911bca857dbffe19a105463da0e&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ETUXB5A%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCID%2FJVGZBdyCwMTllI9vT8CMMYj4grlTqzreXgDzid4qpAiBeTmPVy0RL8nqMrSlB4kpBO0paoswtPrFfBxDBMA%2F4OCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMONoy2%2BgYn71RPp%2FYKtwDa6A73SIhThG41lMg6757kkhnBHep3G2P1bA6NV304Eh1w8nBzRD4fF0TTWnvOvd6Zv5aypJfCH%2BBt1PsK8%2FXrC5X3G%2FzJ2nSIr0TipcmwvbajiLTMEiqgrh3fDcI8PmnXBCACGnT8fez0H0LXhx9MTnFJdumw2KCv7Cz1Vn9W1DmCEvU6qwnhDXlKOHSjiKB3zH4EtFZSH5g6jW7mHlrdevwWBNUNZE7dJXDFImDAednparnNBU%2BlSuy2D%2Bb7NssXuermqhVm7d3%2FXYL2d8JZtnIXNdcygTy%2Bhf4zGaGCz8J%2BIkdh2Z8R8wUYkWi6OEa5zzGwd5bpSgi0gccbCiIVTaBovxFNJ2M55dyfT1vJt7v9wN0sLyWJIJrW60bUqyvjNjgftJJ1Kv9Jx1n%2FLxvudX3DH9CD3ltXTgZSpNdUgnBcKAAZpvx0pFS0wMDD5X2HSgodJO71iesPLzxdnkBu4elnjzO27W7ZyE7hUwzVmrKe6hZ8fiw8bDY1wgujcTQpYNo6rcQN5MtAblDfC%2FYElQwEgYTuBakOPNkeTJlfgidOSCFy9Oe%2FS7BXXONj6vTGZuGFnoZkSrp6U0drFbZex%2B6CKlBWL8exwvKIU%2BOlkZQ8Ki2nv1xRAoBHRYwi7ObvQY6pgFg7HqVB%2BUiDW66%2BwsPSVw3CMIolEbdcxgT2APwKInVSn3jr0VP6kYFc6uFqGMB%2BDVPq5FFN10pdEC8NfQMxW0jf9whDETdFdZaYVxVz47n3pzpQm%2Bfg16xyxmt3PxBkwWdxGVl535cx%2FaR2knPkGn4XBeYvru5eMU825aJTRoSo7I%2BkUCT8HW9LhRzGFG8iWVSPnXRpQ6XkDRReyYgkfbcav74Mryv&X-Amz-Signature=dfc9e0b1c40a501daa882d08ab078cad59456ab548967a62c6ea3ba9d4ece773&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ETUXB5A%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCID%2FJVGZBdyCwMTllI9vT8CMMYj4grlTqzreXgDzid4qpAiBeTmPVy0RL8nqMrSlB4kpBO0paoswtPrFfBxDBMA%2F4OCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMONoy2%2BgYn71RPp%2FYKtwDa6A73SIhThG41lMg6757kkhnBHep3G2P1bA6NV304Eh1w8nBzRD4fF0TTWnvOvd6Zv5aypJfCH%2BBt1PsK8%2FXrC5X3G%2FzJ2nSIr0TipcmwvbajiLTMEiqgrh3fDcI8PmnXBCACGnT8fez0H0LXhx9MTnFJdumw2KCv7Cz1Vn9W1DmCEvU6qwnhDXlKOHSjiKB3zH4EtFZSH5g6jW7mHlrdevwWBNUNZE7dJXDFImDAednparnNBU%2BlSuy2D%2Bb7NssXuermqhVm7d3%2FXYL2d8JZtnIXNdcygTy%2Bhf4zGaGCz8J%2BIkdh2Z8R8wUYkWi6OEa5zzGwd5bpSgi0gccbCiIVTaBovxFNJ2M55dyfT1vJt7v9wN0sLyWJIJrW60bUqyvjNjgftJJ1Kv9Jx1n%2FLxvudX3DH9CD3ltXTgZSpNdUgnBcKAAZpvx0pFS0wMDD5X2HSgodJO71iesPLzxdnkBu4elnjzO27W7ZyE7hUwzVmrKe6hZ8fiw8bDY1wgujcTQpYNo6rcQN5MtAblDfC%2FYElQwEgYTuBakOPNkeTJlfgidOSCFy9Oe%2FS7BXXONj6vTGZuGFnoZkSrp6U0drFbZex%2B6CKlBWL8exwvKIU%2BOlkZQ8Ki2nv1xRAoBHRYwi7ObvQY6pgFg7HqVB%2BUiDW66%2BwsPSVw3CMIolEbdcxgT2APwKInVSn3jr0VP6kYFc6uFqGMB%2BDVPq5FFN10pdEC8NfQMxW0jf9whDETdFdZaYVxVz47n3pzpQm%2Bfg16xyxmt3PxBkwWdxGVl535cx%2FaR2knPkGn4XBeYvru5eMU825aJTRoSo7I%2BkUCT8HW9LhRzGFG8iWVSPnXRpQ6XkDRReyYgkfbcav74Mryv&X-Amz-Signature=1b35a81c4f1d8faf9031d9b3c8379b944d4813942beef4a7f408789e16c6b2c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RL5B6PRG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIHqXWJThgNOjx3eykc1FmFkIMB4vbb4EJzRez8ZCxX%2BcAiEAlUDjuSy6EAryW0kDVOrmrDVTwdkFnl%2FNoKBpooKdX9MqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIXHNye0QSjj%2FYNSfSrcA0QsqhUVsV2B84LDmLDlFp07aBFGBhOw108x%2Bp8a5t%2FGHO3Ub0sM4CrtvlMmWffVTHyXoju2Hf0izhKboFQNWqdl7iwfhljb9wOydvHM4L%2Bn5CIru%2BonJ8oIjQ2cQToRa5A10PIlHS8aT7LtfrBdQck0bOBqxbo4LNtW0o5KS2lySiCrHFRkNI8iSUPEa6lpf0yrrttaEhEABF%2BoHsF1uKdqCVZmJzu0lPAI7hbTIasoxRCOWcqJ%2BrZSmR77IcVFB1TfhaE0ObAiE4%2BKlyLaHan0vrnNETOO5a19A739%2BCc8XurEjX1t4XBcwCFqO6JjUsDQ%2BUWrTYDS29JkTFDzo6ttIpOqq5T9powTm6fS002MGLPRTKoxS7UlQOEbtfCxCXGVSo9aR3BoWFreif%2BAoQaftAXiYtromwLWpPgBvag7N6bL94pxeSqakWkDKEE4CmvqXS9wMWOOzsO80ameWGf3%2BO0V0ID7RuELcZGL1OZM%2Fz29vaNPIanRow0DX94Wm%2Bv84M79lCY1w5QZfTZOQem8Li8zl9kRlPbSAPN51uEHNWAauyGrn0EJF88YLEYAaKpWgg%2BZlMZVOHvkQv4WW2p3j6M7xKSUBxbfuqQvE3xdi7QaDZozhNGlfZpnMNCym70GOqUB%2Fn7HQ5fkHeALYmpKp7nI0aJBdhz2gREvXptrZEYEgDsDv%2FTr5DZVnzY2MMc9Lrxo3EPzF7kUZJmFuh3%2F6rMFbsVplQEv7vY7HVM8i%2BHCtkuy9L1jrkKY0XC1oOHgNlgESkfNjqWkX2wVtOzNwFCXIlLqyIM9jKHt7eKXUomIeT8nDVyVDAZ4OYAdflTkRKDbwmiRPaJAOUn1IrIiHJb9hH318ed8&X-Amz-Signature=d95d8f9c6a063322324175b527f4496d86a84d46fdeb57e0558bd0a85dcee9c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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