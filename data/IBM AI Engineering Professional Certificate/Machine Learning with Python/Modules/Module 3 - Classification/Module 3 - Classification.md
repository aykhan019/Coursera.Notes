

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNWTK3U7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDrHnU%2FG6vaFz11cyE5QpONO3bCdZw%2B8CPmSXnB6GpG9AiBeUHiiXASzXrYyRbAbqx%2BwdtH1yoTzlQIa%2BD3KMWyhIyr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMyoF1YZV8AcuegnpBKtwDgMP8BBbat86LZ9AWCDsKxnF6ZRRu68pq%2Ff2R3vUWKBN%2BkiRNr%2FVMlQH%2F%2Fl2BbqbUXwBOitmHGRxWoJqd3NDMGE3HDGQSblLh1tz9ckIIjnf9VCyDdq6p32RIYpeRyvukA%2FmNaSmh1dQ0cA%2FetJZPKvqlX5ZAOvOc6tQyHCuVoYFXhXK3mHWX5ybzDzjXb5lQMMpDcKt6n3OLHY99ISKZ9SyZrLtQdYrqTJnSCSLoD9wTq25YibaQGRHbzVy%2BdgXt5%2Fn40LQ61zHjlgD%2BQT1oRjMKajm3W8qQwWgJ6pYBqZVDKXkz0TjArgYQgHUtK%2BKZkIm1%2F9ObJOuy5pH2cDrbHuism1ZJJ%2BwTV9pBAhmpNBxzWf0deyFn0Zd%2F8GDOIwHxhko3JCDp70I1iixhEHoojeiS%2BFI%2BGY4B76dKtivx%2B4GGBPwUbVaRol%2FObwbrcSH8DpJhxBeMDtbJh8KgN16zZBVc8zHfZSdFYa%2Bn%2B66GuJPZTLFDiY9C6X1OGttommzFMwR%2Bq9GACPDiwiM%2BDyYr88tIqBR3DVBEPpMEEdYKdbD0zMF6xFf03QoUyWAPilpUIIReA7IeVqHwZOwzr%2BWsfWgV%2BgS2CTfCFeQC0Y48nlboYYWPCorU%2B7SsiN8w9o2DvQY6pgFxe4THDhwEzVvOPZlMg87shur1lAJK%2FSDw0RpQPmDOCnsLk7US9bV8QnLRzB00NdU1vFJjVPLYDvdDkVHnCpslA6kS19GJ0n9j8w4%2FqY4rQhuyk5Tg36yK1pzH5mIvqWQ9W0j0dabItmYyLstlFCUdv40c4U%2Bo8XMeqa78SI8TUqNbpcud0%2B0y6GJJIrU4OfFzK8DX0kwk5VnCR7j5xGEV%2B%2FEI7BBt&X-Amz-Signature=6bf63147921d371b3a59c3d0b187e69edefa26d0beb5a5101bf9c7e102195391&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNWTK3U7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDrHnU%2FG6vaFz11cyE5QpONO3bCdZw%2B8CPmSXnB6GpG9AiBeUHiiXASzXrYyRbAbqx%2BwdtH1yoTzlQIa%2BD3KMWyhIyr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMyoF1YZV8AcuegnpBKtwDgMP8BBbat86LZ9AWCDsKxnF6ZRRu68pq%2Ff2R3vUWKBN%2BkiRNr%2FVMlQH%2F%2Fl2BbqbUXwBOitmHGRxWoJqd3NDMGE3HDGQSblLh1tz9ckIIjnf9VCyDdq6p32RIYpeRyvukA%2FmNaSmh1dQ0cA%2FetJZPKvqlX5ZAOvOc6tQyHCuVoYFXhXK3mHWX5ybzDzjXb5lQMMpDcKt6n3OLHY99ISKZ9SyZrLtQdYrqTJnSCSLoD9wTq25YibaQGRHbzVy%2BdgXt5%2Fn40LQ61zHjlgD%2BQT1oRjMKajm3W8qQwWgJ6pYBqZVDKXkz0TjArgYQgHUtK%2BKZkIm1%2F9ObJOuy5pH2cDrbHuism1ZJJ%2BwTV9pBAhmpNBxzWf0deyFn0Zd%2F8GDOIwHxhko3JCDp70I1iixhEHoojeiS%2BFI%2BGY4B76dKtivx%2B4GGBPwUbVaRol%2FObwbrcSH8DpJhxBeMDtbJh8KgN16zZBVc8zHfZSdFYa%2Bn%2B66GuJPZTLFDiY9C6X1OGttommzFMwR%2Bq9GACPDiwiM%2BDyYr88tIqBR3DVBEPpMEEdYKdbD0zMF6xFf03QoUyWAPilpUIIReA7IeVqHwZOwzr%2BWsfWgV%2BgS2CTfCFeQC0Y48nlboYYWPCorU%2B7SsiN8w9o2DvQY6pgFxe4THDhwEzVvOPZlMg87shur1lAJK%2FSDw0RpQPmDOCnsLk7US9bV8QnLRzB00NdU1vFJjVPLYDvdDkVHnCpslA6kS19GJ0n9j8w4%2FqY4rQhuyk5Tg36yK1pzH5mIvqWQ9W0j0dabItmYyLstlFCUdv40c4U%2Bo8XMeqa78SI8TUqNbpcud0%2B0y6GJJIrU4OfFzK8DX0kwk5VnCR7j5xGEV%2B%2FEI7BBt&X-Amz-Signature=45a79367b0eb63d2db415187a2514cd8973833f425e2fa745457b02e732eb679&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNWTK3U7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDrHnU%2FG6vaFz11cyE5QpONO3bCdZw%2B8CPmSXnB6GpG9AiBeUHiiXASzXrYyRbAbqx%2BwdtH1yoTzlQIa%2BD3KMWyhIyr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMyoF1YZV8AcuegnpBKtwDgMP8BBbat86LZ9AWCDsKxnF6ZRRu68pq%2Ff2R3vUWKBN%2BkiRNr%2FVMlQH%2F%2Fl2BbqbUXwBOitmHGRxWoJqd3NDMGE3HDGQSblLh1tz9ckIIjnf9VCyDdq6p32RIYpeRyvukA%2FmNaSmh1dQ0cA%2FetJZPKvqlX5ZAOvOc6tQyHCuVoYFXhXK3mHWX5ybzDzjXb5lQMMpDcKt6n3OLHY99ISKZ9SyZrLtQdYrqTJnSCSLoD9wTq25YibaQGRHbzVy%2BdgXt5%2Fn40LQ61zHjlgD%2BQT1oRjMKajm3W8qQwWgJ6pYBqZVDKXkz0TjArgYQgHUtK%2BKZkIm1%2F9ObJOuy5pH2cDrbHuism1ZJJ%2BwTV9pBAhmpNBxzWf0deyFn0Zd%2F8GDOIwHxhko3JCDp70I1iixhEHoojeiS%2BFI%2BGY4B76dKtivx%2B4GGBPwUbVaRol%2FObwbrcSH8DpJhxBeMDtbJh8KgN16zZBVc8zHfZSdFYa%2Bn%2B66GuJPZTLFDiY9C6X1OGttommzFMwR%2Bq9GACPDiwiM%2BDyYr88tIqBR3DVBEPpMEEdYKdbD0zMF6xFf03QoUyWAPilpUIIReA7IeVqHwZOwzr%2BWsfWgV%2BgS2CTfCFeQC0Y48nlboYYWPCorU%2B7SsiN8w9o2DvQY6pgFxe4THDhwEzVvOPZlMg87shur1lAJK%2FSDw0RpQPmDOCnsLk7US9bV8QnLRzB00NdU1vFJjVPLYDvdDkVHnCpslA6kS19GJ0n9j8w4%2FqY4rQhuyk5Tg36yK1pzH5mIvqWQ9W0j0dabItmYyLstlFCUdv40c4U%2Bo8XMeqa78SI8TUqNbpcud0%2B0y6GJJIrU4OfFzK8DX0kwk5VnCR7j5xGEV%2B%2FEI7BBt&X-Amz-Signature=3561a8b97d167041de3d5fb39d1f9d594fc362815731ec370188dfc222c74eb7&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672GXHSDL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTcSsYXSH8CYNBoPIMGbrFN2aEAszViINDI1DOEYosMgIgMoMvjidmGADGQJJ8bMd%2F7QzChOqDp90Yz%2FjwneLHydEq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDLYrbvK5XMXyHmRpircA7IJkide12lNcfxrRldgcB0zQORgCuaAOY3OYDguXvgoU1WSkof19FU5yMl2koS30KUeDZCMfCEkJsvOnOinBpcdQPHcOh%2F%2FPzxlrm5hUua4sVqNGmnLdB6fQ%2Bm54j6LU19180wP9psSnXbn%2BeB5wylDhKZ%2FzJFwrn2wmfnJfw3FOGRJt6QI1cA%2BcaxBouvti1gUlPn5Oh3AgqtmJeCUG4XtB0oldDknkupC2HuGv%2BN7a4oHRdfUh5qoPqhmWQwJsncDESFD2hT3KnB9sJOQXZqI3PcsCoHS1w3bcFY0caiXYHsxi6tDDmcfVIm%2Bk0GRPx3XL10BdPMttQJN6X1%2B07APq%2FokRqG9Yq8lejj16PQyDyUC%2BDmCiAna5dnDpKy2kO7FzcFq5Wn7klXg1LPPKJrs349tuVgrufMjW%2BXBjTDtnbncl6zTNE%2FZ3adJdlicnbp1R8kwMcK5AJ%2FCCBez1J4FI9dhTRigPZz87CrFMegaGuGiPvge1FnSWC5wYZ29POJpqQh9zHF3Z%2Fw9vhxH07jycxWQ%2F93HgtCq5iTokp6xlxmFl4e7XqMI5r42dpfAwfTxuz%2FiSzGcDyt1PdoRTXagOq%2Bp2xT2IXhpAEJxC76BhEeEpBVgdueliIFWMKGNg70GOqUB04JMDCWFSorSzkDiXcPufhg7DAm7nimdvBEURMCGOcHnwrfv5AioD%2FuasuMRdTxFJP8lpcxtnMhxuDwdzNVB7IqUkffMs99oRhGlN0j6XMPd%2FRE%2FLeZedwLB8yn4K7VqLcq6LC0iQWwFp71rScUj42lDlyhuCvQ1ePxXYSx3f04vNuaCz48wHEM%2FENZyUop90vby4U4bkiEeCAymIatfzvZohUmO&X-Amz-Signature=e99f4b223bf8bdfc6091be3db46273b81993d6f8e542194bd133add4094dcad6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672GXHSDL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTcSsYXSH8CYNBoPIMGbrFN2aEAszViINDI1DOEYosMgIgMoMvjidmGADGQJJ8bMd%2F7QzChOqDp90Yz%2FjwneLHydEq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDDLYrbvK5XMXyHmRpircA7IJkide12lNcfxrRldgcB0zQORgCuaAOY3OYDguXvgoU1WSkof19FU5yMl2koS30KUeDZCMfCEkJsvOnOinBpcdQPHcOh%2F%2FPzxlrm5hUua4sVqNGmnLdB6fQ%2Bm54j6LU19180wP9psSnXbn%2BeB5wylDhKZ%2FzJFwrn2wmfnJfw3FOGRJt6QI1cA%2BcaxBouvti1gUlPn5Oh3AgqtmJeCUG4XtB0oldDknkupC2HuGv%2BN7a4oHRdfUh5qoPqhmWQwJsncDESFD2hT3KnB9sJOQXZqI3PcsCoHS1w3bcFY0caiXYHsxi6tDDmcfVIm%2Bk0GRPx3XL10BdPMttQJN6X1%2B07APq%2FokRqG9Yq8lejj16PQyDyUC%2BDmCiAna5dnDpKy2kO7FzcFq5Wn7klXg1LPPKJrs349tuVgrufMjW%2BXBjTDtnbncl6zTNE%2FZ3adJdlicnbp1R8kwMcK5AJ%2FCCBez1J4FI9dhTRigPZz87CrFMegaGuGiPvge1FnSWC5wYZ29POJpqQh9zHF3Z%2Fw9vhxH07jycxWQ%2F93HgtCq5iTokp6xlxmFl4e7XqMI5r42dpfAwfTxuz%2FiSzGcDyt1PdoRTXagOq%2Bp2xT2IXhpAEJxC76BhEeEpBVgdueliIFWMKGNg70GOqUB04JMDCWFSorSzkDiXcPufhg7DAm7nimdvBEURMCGOcHnwrfv5AioD%2FuasuMRdTxFJP8lpcxtnMhxuDwdzNVB7IqUkffMs99oRhGlN0j6XMPd%2FRE%2FLeZedwLB8yn4K7VqLcq6LC0iQWwFp71rScUj42lDlyhuCvQ1ePxXYSx3f04vNuaCz48wHEM%2FENZyUop90vby4U4bkiEeCAymIatfzvZohUmO&X-Amz-Signature=a6e40bd8c6efb988b336bcd2e72b00df3640a936b8aec6e69481ba2b09d7a70c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNWTK3U7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDrHnU%2FG6vaFz11cyE5QpONO3bCdZw%2B8CPmSXnB6GpG9AiBeUHiiXASzXrYyRbAbqx%2BwdtH1yoTzlQIa%2BD3KMWyhIyr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMyoF1YZV8AcuegnpBKtwDgMP8BBbat86LZ9AWCDsKxnF6ZRRu68pq%2Ff2R3vUWKBN%2BkiRNr%2FVMlQH%2F%2Fl2BbqbUXwBOitmHGRxWoJqd3NDMGE3HDGQSblLh1tz9ckIIjnf9VCyDdq6p32RIYpeRyvukA%2FmNaSmh1dQ0cA%2FetJZPKvqlX5ZAOvOc6tQyHCuVoYFXhXK3mHWX5ybzDzjXb5lQMMpDcKt6n3OLHY99ISKZ9SyZrLtQdYrqTJnSCSLoD9wTq25YibaQGRHbzVy%2BdgXt5%2Fn40LQ61zHjlgD%2BQT1oRjMKajm3W8qQwWgJ6pYBqZVDKXkz0TjArgYQgHUtK%2BKZkIm1%2F9ObJOuy5pH2cDrbHuism1ZJJ%2BwTV9pBAhmpNBxzWf0deyFn0Zd%2F8GDOIwHxhko3JCDp70I1iixhEHoojeiS%2BFI%2BGY4B76dKtivx%2B4GGBPwUbVaRol%2FObwbrcSH8DpJhxBeMDtbJh8KgN16zZBVc8zHfZSdFYa%2Bn%2B66GuJPZTLFDiY9C6X1OGttommzFMwR%2Bq9GACPDiwiM%2BDyYr88tIqBR3DVBEPpMEEdYKdbD0zMF6xFf03QoUyWAPilpUIIReA7IeVqHwZOwzr%2BWsfWgV%2BgS2CTfCFeQC0Y48nlboYYWPCorU%2B7SsiN8w9o2DvQY6pgFxe4THDhwEzVvOPZlMg87shur1lAJK%2FSDw0RpQPmDOCnsLk7US9bV8QnLRzB00NdU1vFJjVPLYDvdDkVHnCpslA6kS19GJ0n9j8w4%2FqY4rQhuyk5Tg36yK1pzH5mIvqWQ9W0j0dabItmYyLstlFCUdv40c4U%2Bo8XMeqa78SI8TUqNbpcud0%2B0y6GJJIrU4OfFzK8DX0kwk5VnCR7j5xGEV%2B%2FEI7BBt&X-Amz-Signature=7ab8bf6ad284f249ff8ac54f84984d89547d861016f7ca6790226c1462808208&X-Amz-SignedHeaders=host&x-id=GetObject)
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