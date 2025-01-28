

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466445TAKXX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDIPYvtGlGN%2BbbPkZXjt%2F6Lnf2p7l4SNHmlde59xuK57wIgbwFlWOyT6t0fhRf%2B%2FkeyC9v66FE4%2FuxnDteRjlVHx88q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDG8BHBrTNCtfhPR7yrcA9oXEVd0hbl3d4SyYJe%2Bm6vk%2FyqVtdsW2%2B9Ewwlc%2BEVHWO%2F%2FTu1fsH9wDdGo4JKXDvhIuneOFKMdhl%2BkhZbMkneT9P%2FO1kjyRcj8Ji0Xgu6SiZsnb4Pe%2FJfFmZTL096olpnD86MtPDLQ2B3DKJ6o%2BMESIp%2FveiG1o1NIoGLxX%2BojNqof1%2FO%2FNe71kV7T0Evp%2B%2FuQm0%2B8DLABgjDY%2Fg1tBXf%2B6SOLat7ImL4D8k%2BWweWbNj7qvWYOTgy9J1fsWC5hPoKnTClrGdFGBzZ2XDJedzM%2BLDW41SzVs3Kf%2BP9CnX52EPHWxEDNgI4Vg2QtV2Be%2F8b8zJ8QVbMAs3L0Gd5Jwt9WBHrYa4HPiEvTIMmqEpsaArJTZHHoKpfR3H0cutI373nss5BSTHufNUou8yNDTe%2FbgzPsIj3Us1pBiW%2FRfGqgM9T5sH7wfb9tst0QJIxRyug7vcfCaHamyUzt3S5ZPizSd7cpgImbx4PcjPBdLHhYGng8wxVePByGIVg26epv%2FP02Bry%2FDkTb5oc3TRVwLn5vkfW8BU087hf%2BoTSlUfnMDtPHIjgkexiRFdBZAXcOanQaT%2FxaGZ51dwH3cVUkLzD3FR%2BpbB20kZwveaA50TMEnuVMVgHWnHRDk4%2FyMLfm5LwGOqUB2sh%2Bh4GEpoH2Tyjo%2Fau8LhT44A1hcRAik6DgKFC3SJDrLTm88Qvs6XZ%2FaDfC%2BzqNnLV39t8d%2BDaCo90JxGit2nJXkBTJFh4G2HFY5Aiq5L%2FpCoYptAByDV%2BHf27sQ5v97cluwONpwU9ouEPVzn4bNyEu3gGh0qd%2FEx8k%2Fj4sWokIABip%2ByfiYZw2CW8bvSIunfjVOmgGiGbKRDFbmK0KEv1p4Yp4&X-Amz-Signature=2b92bfb3ea810aa8a2935a6ceb1ef4bb58c55daa7ab10042ffaa589f3268a839&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466445TAKXX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDIPYvtGlGN%2BbbPkZXjt%2F6Lnf2p7l4SNHmlde59xuK57wIgbwFlWOyT6t0fhRf%2B%2FkeyC9v66FE4%2FuxnDteRjlVHx88q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDG8BHBrTNCtfhPR7yrcA9oXEVd0hbl3d4SyYJe%2Bm6vk%2FyqVtdsW2%2B9Ewwlc%2BEVHWO%2F%2FTu1fsH9wDdGo4JKXDvhIuneOFKMdhl%2BkhZbMkneT9P%2FO1kjyRcj8Ji0Xgu6SiZsnb4Pe%2FJfFmZTL096olpnD86MtPDLQ2B3DKJ6o%2BMESIp%2FveiG1o1NIoGLxX%2BojNqof1%2FO%2FNe71kV7T0Evp%2B%2FuQm0%2B8DLABgjDY%2Fg1tBXf%2B6SOLat7ImL4D8k%2BWweWbNj7qvWYOTgy9J1fsWC5hPoKnTClrGdFGBzZ2XDJedzM%2BLDW41SzVs3Kf%2BP9CnX52EPHWxEDNgI4Vg2QtV2Be%2F8b8zJ8QVbMAs3L0Gd5Jwt9WBHrYa4HPiEvTIMmqEpsaArJTZHHoKpfR3H0cutI373nss5BSTHufNUou8yNDTe%2FbgzPsIj3Us1pBiW%2FRfGqgM9T5sH7wfb9tst0QJIxRyug7vcfCaHamyUzt3S5ZPizSd7cpgImbx4PcjPBdLHhYGng8wxVePByGIVg26epv%2FP02Bry%2FDkTb5oc3TRVwLn5vkfW8BU087hf%2BoTSlUfnMDtPHIjgkexiRFdBZAXcOanQaT%2FxaGZ51dwH3cVUkLzD3FR%2BpbB20kZwveaA50TMEnuVMVgHWnHRDk4%2FyMLfm5LwGOqUB2sh%2Bh4GEpoH2Tyjo%2Fau8LhT44A1hcRAik6DgKFC3SJDrLTm88Qvs6XZ%2FaDfC%2BzqNnLV39t8d%2BDaCo90JxGit2nJXkBTJFh4G2HFY5Aiq5L%2FpCoYptAByDV%2BHf27sQ5v97cluwONpwU9ouEPVzn4bNyEu3gGh0qd%2FEx8k%2Fj4sWokIABip%2ByfiYZw2CW8bvSIunfjVOmgGiGbKRDFbmK0KEv1p4Yp4&X-Amz-Signature=2d11924c38f5e2550bab8c32b6590903a22bd52b02947616f449073770363274&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466445TAKXX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDIPYvtGlGN%2BbbPkZXjt%2F6Lnf2p7l4SNHmlde59xuK57wIgbwFlWOyT6t0fhRf%2B%2FkeyC9v66FE4%2FuxnDteRjlVHx88q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDG8BHBrTNCtfhPR7yrcA9oXEVd0hbl3d4SyYJe%2Bm6vk%2FyqVtdsW2%2B9Ewwlc%2BEVHWO%2F%2FTu1fsH9wDdGo4JKXDvhIuneOFKMdhl%2BkhZbMkneT9P%2FO1kjyRcj8Ji0Xgu6SiZsnb4Pe%2FJfFmZTL096olpnD86MtPDLQ2B3DKJ6o%2BMESIp%2FveiG1o1NIoGLxX%2BojNqof1%2FO%2FNe71kV7T0Evp%2B%2FuQm0%2B8DLABgjDY%2Fg1tBXf%2B6SOLat7ImL4D8k%2BWweWbNj7qvWYOTgy9J1fsWC5hPoKnTClrGdFGBzZ2XDJedzM%2BLDW41SzVs3Kf%2BP9CnX52EPHWxEDNgI4Vg2QtV2Be%2F8b8zJ8QVbMAs3L0Gd5Jwt9WBHrYa4HPiEvTIMmqEpsaArJTZHHoKpfR3H0cutI373nss5BSTHufNUou8yNDTe%2FbgzPsIj3Us1pBiW%2FRfGqgM9T5sH7wfb9tst0QJIxRyug7vcfCaHamyUzt3S5ZPizSd7cpgImbx4PcjPBdLHhYGng8wxVePByGIVg26epv%2FP02Bry%2FDkTb5oc3TRVwLn5vkfW8BU087hf%2BoTSlUfnMDtPHIjgkexiRFdBZAXcOanQaT%2FxaGZ51dwH3cVUkLzD3FR%2BpbB20kZwveaA50TMEnuVMVgHWnHRDk4%2FyMLfm5LwGOqUB2sh%2Bh4GEpoH2Tyjo%2Fau8LhT44A1hcRAik6DgKFC3SJDrLTm88Qvs6XZ%2FaDfC%2BzqNnLV39t8d%2BDaCo90JxGit2nJXkBTJFh4G2HFY5Aiq5L%2FpCoYptAByDV%2BHf27sQ5v97cluwONpwU9ouEPVzn4bNyEu3gGh0qd%2FEx8k%2Fj4sWokIABip%2ByfiYZw2CW8bvSIunfjVOmgGiGbKRDFbmK0KEv1p4Yp4&X-Amz-Signature=89dbcb01744fae721558c49b4d1eafce361fe9ba86668c4892c3c08df77f4ecd&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFLO5EJV%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGC0wXRx865umjvoj7mOJ2v1%2BhGsjPkJYRGh5jdYZfLDAiEA0sxfGeFoHewIj5j9CSVAdZP%2ByaH7YUNUFozrNgezhy0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEUUCYsZ4w%2FbK%2FGzOircAyzMF8o2lmPNCpvw%2FVk5B6RSz8RQW2LpQeiylCuHqRxMYac9b%2B7aaY6vrhZfcqF8oMVhG1BUcgZ%2BVRVbL2UvY9RkGkgU2BQeXNoC5CStvgfb8JsJ5HzC3aBAW9Mb%2BbsB%2B4578WJ1%2B8zsrvH7BArilXNrS6vm9lnoz7B9SEJ3xT5Qpzxd1xvVezj3sHxC01OCYuSOtoiPYPWFSInNmuFPXyGCC5fzWxxjXPDoasRPOqOf%2FU6asYmBqfIRqvRcLbWZa26Q1fXdkbjCTkF1djMKObzYfxUAC95bEthoDnxz7eAV3Uxj98muqQ9YzWyfEjki9k%2BDGZOOlYmTPfeI%2FqOxvrdd0B8%2BqpQLUOtHebWQevHrlf02wHifKH3vd4YOazZlGIfXCQbTO3tKcKqyNxaEhEMkAYydU2Jw778DYNoTLISx8CqOYW8hwXvNaewRTHbKPJhG2%2BBAoE%2BCd5EK3emw8KAQE2Am2BG6MVp6SpGA9qMkjbh%2FxL%2Bb3E36ip43qJO06gzQwn2fPPkNeBEqmR48HbbMGzRamOAVHyvv4Y99koX%2BbyQLH7z%2B%2F%2Bj7FM4cN6M46mbT36%2FIk5VShcc5ViP6mLqW9sNB%2FJmG0PM0HORBxP7g9zrzhOgIaFS6OGX4MJvl5LwGOqUBY0SkQRoabgKq31TMmgTjXfdb2iofaT6qZ9%2B78ysTpW6seQrVGYP3IkeE6AktEG%2BYZ2NQBbvDB957OikjTHDR4PwxcMsTNPhT3loGwaAYV8vCaMN7uZ65KLP2OQA9c%2BPqh4AJw%2FARkfJxi%2BM6n4WOcxIjiYE6Oq%2Fv7uuch146qMbcnILE7XHUI8Js%2BhxlKnGafZBnVhriWp4fXBm3guIDjjN%2Bl%2FwV&X-Amz-Signature=311e45b737cdcabd2038f108047e83c144838f7412ad7c7c8e780092c1a5ced5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFLO5EJV%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGC0wXRx865umjvoj7mOJ2v1%2BhGsjPkJYRGh5jdYZfLDAiEA0sxfGeFoHewIj5j9CSVAdZP%2ByaH7YUNUFozrNgezhy0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEUUCYsZ4w%2FbK%2FGzOircAyzMF8o2lmPNCpvw%2FVk5B6RSz8RQW2LpQeiylCuHqRxMYac9b%2B7aaY6vrhZfcqF8oMVhG1BUcgZ%2BVRVbL2UvY9RkGkgU2BQeXNoC5CStvgfb8JsJ5HzC3aBAW9Mb%2BbsB%2B4578WJ1%2B8zsrvH7BArilXNrS6vm9lnoz7B9SEJ3xT5Qpzxd1xvVezj3sHxC01OCYuSOtoiPYPWFSInNmuFPXyGCC5fzWxxjXPDoasRPOqOf%2FU6asYmBqfIRqvRcLbWZa26Q1fXdkbjCTkF1djMKObzYfxUAC95bEthoDnxz7eAV3Uxj98muqQ9YzWyfEjki9k%2BDGZOOlYmTPfeI%2FqOxvrdd0B8%2BqpQLUOtHebWQevHrlf02wHifKH3vd4YOazZlGIfXCQbTO3tKcKqyNxaEhEMkAYydU2Jw778DYNoTLISx8CqOYW8hwXvNaewRTHbKPJhG2%2BBAoE%2BCd5EK3emw8KAQE2Am2BG6MVp6SpGA9qMkjbh%2FxL%2Bb3E36ip43qJO06gzQwn2fPPkNeBEqmR48HbbMGzRamOAVHyvv4Y99koX%2BbyQLH7z%2B%2F%2Bj7FM4cN6M46mbT36%2FIk5VShcc5ViP6mLqW9sNB%2FJmG0PM0HORBxP7g9zrzhOgIaFS6OGX4MJvl5LwGOqUBY0SkQRoabgKq31TMmgTjXfdb2iofaT6qZ9%2B78ysTpW6seQrVGYP3IkeE6AktEG%2BYZ2NQBbvDB957OikjTHDR4PwxcMsTNPhT3loGwaAYV8vCaMN7uZ65KLP2OQA9c%2BPqh4AJw%2FARkfJxi%2BM6n4WOcxIjiYE6Oq%2Fv7uuch146qMbcnILE7XHUI8Js%2BhxlKnGafZBnVhriWp4fXBm3guIDjjN%2Bl%2FwV&X-Amz-Signature=45d061ae25a25bda949f7957ae6f4ae65e1ff3614fbd992c17ca9e1663f0a210&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466445TAKXX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDIPYvtGlGN%2BbbPkZXjt%2F6Lnf2p7l4SNHmlde59xuK57wIgbwFlWOyT6t0fhRf%2B%2FkeyC9v66FE4%2FuxnDteRjlVHx88q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDG8BHBrTNCtfhPR7yrcA9oXEVd0hbl3d4SyYJe%2Bm6vk%2FyqVtdsW2%2B9Ewwlc%2BEVHWO%2F%2FTu1fsH9wDdGo4JKXDvhIuneOFKMdhl%2BkhZbMkneT9P%2FO1kjyRcj8Ji0Xgu6SiZsnb4Pe%2FJfFmZTL096olpnD86MtPDLQ2B3DKJ6o%2BMESIp%2FveiG1o1NIoGLxX%2BojNqof1%2FO%2FNe71kV7T0Evp%2B%2FuQm0%2B8DLABgjDY%2Fg1tBXf%2B6SOLat7ImL4D8k%2BWweWbNj7qvWYOTgy9J1fsWC5hPoKnTClrGdFGBzZ2XDJedzM%2BLDW41SzVs3Kf%2BP9CnX52EPHWxEDNgI4Vg2QtV2Be%2F8b8zJ8QVbMAs3L0Gd5Jwt9WBHrYa4HPiEvTIMmqEpsaArJTZHHoKpfR3H0cutI373nss5BSTHufNUou8yNDTe%2FbgzPsIj3Us1pBiW%2FRfGqgM9T5sH7wfb9tst0QJIxRyug7vcfCaHamyUzt3S5ZPizSd7cpgImbx4PcjPBdLHhYGng8wxVePByGIVg26epv%2FP02Bry%2FDkTb5oc3TRVwLn5vkfW8BU087hf%2BoTSlUfnMDtPHIjgkexiRFdBZAXcOanQaT%2FxaGZ51dwH3cVUkLzD3FR%2BpbB20kZwveaA50TMEnuVMVgHWnHRDk4%2FyMLfm5LwGOqUB2sh%2Bh4GEpoH2Tyjo%2Fau8LhT44A1hcRAik6DgKFC3SJDrLTm88Qvs6XZ%2FaDfC%2BzqNnLV39t8d%2BDaCo90JxGit2nJXkBTJFh4G2HFY5Aiq5L%2FpCoYptAByDV%2BHf27sQ5v97cluwONpwU9ouEPVzn4bNyEu3gGh0qd%2FEx8k%2Fj4sWokIABip%2ByfiYZw2CW8bvSIunfjVOmgGiGbKRDFbmK0KEv1p4Yp4&X-Amz-Signature=9ee342980c0bb3bd04eacfdbd0b234e73b79562c860565ea5919958dbb0d6175&X-Amz-SignedHeaders=host&x-id=GetObject)
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