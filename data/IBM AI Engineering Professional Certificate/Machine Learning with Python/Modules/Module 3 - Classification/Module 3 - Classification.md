

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLUTJLJC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCP8qxIfH4lP8cPJp30MxsT%2F24R8jZ%2BHsFsTi3y2F8dDwIhAMlJwEK9HVLW7wI7SIHkUcB4T28JLREFXkyqFUModoLDKv8DCGIQABoMNjM3NDIzMTgzODA1IgxxjDeaF5EbsLOWz5Mq3APglFQ32PUIL9HCAszLKXdga%2F3HWff2ZkAy6sKPaJ%2BWLyidbs9Sm0Q9jVPSpWORCeNNm92GPh8iv%2FZgvd%2F%2BhUI%2F4ENzlurSfpEoEspvwi6863Um76O8dyIRuT2fNEaAR4G8HOZ80YjNy%2BB%2FnoRwFvC08sCU3GzRDimU5eL9dioNSy2wwSHQg%2Fms%2BHLbTofMl%2F18i1l78%2FBcJ3iJq%2FuVv86U6QECnXQqqLSAUkRG1ukD62jZUM6TpnLsHBErjCnjmh2tU%2BotI6l7CK3ewwU%2FB8AezN4uekBj2KBKY46KZi28N%2BWL2Xsi2INFr5N%2B93DJjarzSiqAImotfjrBAE%2FpR9U3PNeSRJfEH2Ic1%2FjVBG8aQKordPDCti7OnF5KVyZV%2B8J1jPkYtZBIHyLIU0zZ0gZVdyYH0Lnh2uoNAZi7VAy6LDsic93oYchq2t6zt3q5N9%2FBEyvHOTqgstSPTjwDpS%2Bw3jiyObb7N%2BqPn49bYFT9ZI9rtK09gQBvBA7d0LN6iMr2BHtQxK1PYMrVNdIHuMsp5rFWX0RE%2BuP07hioKU5UMeFEfayLezsz63gsqxH3im63yiE3c1i6PZxy%2FcIBZnUnKfzvLle%2BwUAZzePXWBD0KCG%2FGaM4ni1doQrp3TDe0ZO9BjqkAdZbzpAvrlIkIC3YtRoMsLN7JIuSbqrG0vli4xZ7jvgDSaY2AXCc4XJlYKaING1moTppEKj8WpNB9r9I8p2yZOLvMlDybbzfdhaZPo3AtXseYuW5fcXdc6balcNjfZ6zwnsn5tE9c%2BMWEn9QJRVke%2F3plYmjZ9XtxCnYnwBo9YpRJ55%2Bc9l5DX3zYNcXZjT9Pq%2FVqg7ydLUQrI%2FICvVEWG%2BooTQu&X-Amz-Signature=8d79252c2c1641724c97b8c0d7390f71ec1ed3c0d27e8e4c8f7bd554478264b0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLUTJLJC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCP8qxIfH4lP8cPJp30MxsT%2F24R8jZ%2BHsFsTi3y2F8dDwIhAMlJwEK9HVLW7wI7SIHkUcB4T28JLREFXkyqFUModoLDKv8DCGIQABoMNjM3NDIzMTgzODA1IgxxjDeaF5EbsLOWz5Mq3APglFQ32PUIL9HCAszLKXdga%2F3HWff2ZkAy6sKPaJ%2BWLyidbs9Sm0Q9jVPSpWORCeNNm92GPh8iv%2FZgvd%2F%2BhUI%2F4ENzlurSfpEoEspvwi6863Um76O8dyIRuT2fNEaAR4G8HOZ80YjNy%2BB%2FnoRwFvC08sCU3GzRDimU5eL9dioNSy2wwSHQg%2Fms%2BHLbTofMl%2F18i1l78%2FBcJ3iJq%2FuVv86U6QECnXQqqLSAUkRG1ukD62jZUM6TpnLsHBErjCnjmh2tU%2BotI6l7CK3ewwU%2FB8AezN4uekBj2KBKY46KZi28N%2BWL2Xsi2INFr5N%2B93DJjarzSiqAImotfjrBAE%2FpR9U3PNeSRJfEH2Ic1%2FjVBG8aQKordPDCti7OnF5KVyZV%2B8J1jPkYtZBIHyLIU0zZ0gZVdyYH0Lnh2uoNAZi7VAy6LDsic93oYchq2t6zt3q5N9%2FBEyvHOTqgstSPTjwDpS%2Bw3jiyObb7N%2BqPn49bYFT9ZI9rtK09gQBvBA7d0LN6iMr2BHtQxK1PYMrVNdIHuMsp5rFWX0RE%2BuP07hioKU5UMeFEfayLezsz63gsqxH3im63yiE3c1i6PZxy%2FcIBZnUnKfzvLle%2BwUAZzePXWBD0KCG%2FGaM4ni1doQrp3TDe0ZO9BjqkAdZbzpAvrlIkIC3YtRoMsLN7JIuSbqrG0vli4xZ7jvgDSaY2AXCc4XJlYKaING1moTppEKj8WpNB9r9I8p2yZOLvMlDybbzfdhaZPo3AtXseYuW5fcXdc6balcNjfZ6zwnsn5tE9c%2BMWEn9QJRVke%2F3plYmjZ9XtxCnYnwBo9YpRJ55%2Bc9l5DX3zYNcXZjT9Pq%2FVqg7ydLUQrI%2FICvVEWG%2BooTQu&X-Amz-Signature=6c010c928f92824842bf43e5c151ae0b90116dfbdf12ead2ffa61e44c411651f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLUTJLJC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCP8qxIfH4lP8cPJp30MxsT%2F24R8jZ%2BHsFsTi3y2F8dDwIhAMlJwEK9HVLW7wI7SIHkUcB4T28JLREFXkyqFUModoLDKv8DCGIQABoMNjM3NDIzMTgzODA1IgxxjDeaF5EbsLOWz5Mq3APglFQ32PUIL9HCAszLKXdga%2F3HWff2ZkAy6sKPaJ%2BWLyidbs9Sm0Q9jVPSpWORCeNNm92GPh8iv%2FZgvd%2F%2BhUI%2F4ENzlurSfpEoEspvwi6863Um76O8dyIRuT2fNEaAR4G8HOZ80YjNy%2BB%2FnoRwFvC08sCU3GzRDimU5eL9dioNSy2wwSHQg%2Fms%2BHLbTofMl%2F18i1l78%2FBcJ3iJq%2FuVv86U6QECnXQqqLSAUkRG1ukD62jZUM6TpnLsHBErjCnjmh2tU%2BotI6l7CK3ewwU%2FB8AezN4uekBj2KBKY46KZi28N%2BWL2Xsi2INFr5N%2B93DJjarzSiqAImotfjrBAE%2FpR9U3PNeSRJfEH2Ic1%2FjVBG8aQKordPDCti7OnF5KVyZV%2B8J1jPkYtZBIHyLIU0zZ0gZVdyYH0Lnh2uoNAZi7VAy6LDsic93oYchq2t6zt3q5N9%2FBEyvHOTqgstSPTjwDpS%2Bw3jiyObb7N%2BqPn49bYFT9ZI9rtK09gQBvBA7d0LN6iMr2BHtQxK1PYMrVNdIHuMsp5rFWX0RE%2BuP07hioKU5UMeFEfayLezsz63gsqxH3im63yiE3c1i6PZxy%2FcIBZnUnKfzvLle%2BwUAZzePXWBD0KCG%2FGaM4ni1doQrp3TDe0ZO9BjqkAdZbzpAvrlIkIC3YtRoMsLN7JIuSbqrG0vli4xZ7jvgDSaY2AXCc4XJlYKaING1moTppEKj8WpNB9r9I8p2yZOLvMlDybbzfdhaZPo3AtXseYuW5fcXdc6balcNjfZ6zwnsn5tE9c%2BMWEn9QJRVke%2F3plYmjZ9XtxCnYnwBo9YpRJ55%2Bc9l5DX3zYNcXZjT9Pq%2FVqg7ydLUQrI%2FICvVEWG%2BooTQu&X-Amz-Signature=7f1b4a81c7863af9749e7ee35138c544693fc498787378b9439146e16099bf09&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYNZYPPH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIDUyx5fb9ErlgT3X%2FVZl0BWyeleb9vYoqaaaejXONds8AiEAsPH%2BEok%2FqX0cxXASCQ5z8g5ObO87uieJJLsm1y1eyjAq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDBAHmS3v6JaWfyiDyyrcA%2FJDFZNcmcrK7EkH6wm6RySG0wP3mNxNHrsFaA8CXXUNG310btHMbC86D6i0N7z8pbJfIgvcubZG5dNttZ4vvP0ro9dp4umL4%2BBQkHD15MhMNWvJDh7pIB05l7spDDS8xAvZpRBZ%2FIAaSLoIaB5iGvcNDX5kTsmrnT97FkaEz48FZK1nkfBFn0YkyVN2o%2FF%2BAgd06N2awHSVkL9bQ%2Bmm4Bt6NPz4Vry48e4jfFepPgZSxSxbGAH828YrxIiTg9FD2Jvf144NIb0qwNm9jKyA%2BImfaMWYO6NnDZyq2qwxf%2FyYNy%2FHZveLFbGX%2BJT8Akt2%2BBRopva2E%2FXnO5P4%2BfYjPaY775C1Xr2ZuMx4TCUUFLsOKfCOWTbMM4zVvzoEEb3r5NzZyB85xRQUFRgJdY3jpPds1%2Fvy%2F930v8zYs2EoGkbHF%2F8h2SULVR5NDgxF1FEKOk8AorM0HzPLTm84dn60FyxEmzuUGHCUmTR0G4rFrKX%2FcLSBgCn01i6MEUA2Eq0pZM2dsi5GF85oV8I9kd%2FqlN2tZjVmyY1unOUM%2B82oTbFMmctddsxsabNsU7Ru6DKyjft3qiElCuOMDbw6Z8oEb5GM5lZEN1gN2rgU2TcbSQG2Al4iqdElWhz0JlP3MJ3Rk70GOqUBNkif6af%2FHs7qb%2BjdxbWfrAiokk0DTs5XsyydVeX5jlyJoxpyED4a%2FdaPVJMNPyU4BajCOVq8jwUMoq3%2FsljReVqPx25PPVpp01%2BoVK5TimTSgNKa%2BRfmmY%2BMmWVbJWbMe4tx2WXN1zj1%2BLOww%2F1w5xexD%2BJKyQC2hMNMkUy6Rg3B0ZSukhr7q0JPde9yOy9i5IeIdDrMmYzgfdFpMyo6Q5UOz03b&X-Amz-Signature=bba86c259d6fd398b0b33966d7854261f48829dc3f95abc59e9ecc65c98c7ca6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYNZYPPH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIDUyx5fb9ErlgT3X%2FVZl0BWyeleb9vYoqaaaejXONds8AiEAsPH%2BEok%2FqX0cxXASCQ5z8g5ObO87uieJJLsm1y1eyjAq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDBAHmS3v6JaWfyiDyyrcA%2FJDFZNcmcrK7EkH6wm6RySG0wP3mNxNHrsFaA8CXXUNG310btHMbC86D6i0N7z8pbJfIgvcubZG5dNttZ4vvP0ro9dp4umL4%2BBQkHD15MhMNWvJDh7pIB05l7spDDS8xAvZpRBZ%2FIAaSLoIaB5iGvcNDX5kTsmrnT97FkaEz48FZK1nkfBFn0YkyVN2o%2FF%2BAgd06N2awHSVkL9bQ%2Bmm4Bt6NPz4Vry48e4jfFepPgZSxSxbGAH828YrxIiTg9FD2Jvf144NIb0qwNm9jKyA%2BImfaMWYO6NnDZyq2qwxf%2FyYNy%2FHZveLFbGX%2BJT8Akt2%2BBRopva2E%2FXnO5P4%2BfYjPaY775C1Xr2ZuMx4TCUUFLsOKfCOWTbMM4zVvzoEEb3r5NzZyB85xRQUFRgJdY3jpPds1%2Fvy%2F930v8zYs2EoGkbHF%2F8h2SULVR5NDgxF1FEKOk8AorM0HzPLTm84dn60FyxEmzuUGHCUmTR0G4rFrKX%2FcLSBgCn01i6MEUA2Eq0pZM2dsi5GF85oV8I9kd%2FqlN2tZjVmyY1unOUM%2B82oTbFMmctddsxsabNsU7Ru6DKyjft3qiElCuOMDbw6Z8oEb5GM5lZEN1gN2rgU2TcbSQG2Al4iqdElWhz0JlP3MJ3Rk70GOqUBNkif6af%2FHs7qb%2BjdxbWfrAiokk0DTs5XsyydVeX5jlyJoxpyED4a%2FdaPVJMNPyU4BajCOVq8jwUMoq3%2FsljReVqPx25PPVpp01%2BoVK5TimTSgNKa%2BRfmmY%2BMmWVbJWbMe4tx2WXN1zj1%2BLOww%2F1w5xexD%2BJKyQC2hMNMkUy6Rg3B0ZSukhr7q0JPde9yOy9i5IeIdDrMmYzgfdFpMyo6Q5UOz03b&X-Amz-Signature=7ad6b47dfcafc96ed643c8915a77f9c984aa921599b31a0ef846a9e80a59e340&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLUTJLJC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQCP8qxIfH4lP8cPJp30MxsT%2F24R8jZ%2BHsFsTi3y2F8dDwIhAMlJwEK9HVLW7wI7SIHkUcB4T28JLREFXkyqFUModoLDKv8DCGIQABoMNjM3NDIzMTgzODA1IgxxjDeaF5EbsLOWz5Mq3APglFQ32PUIL9HCAszLKXdga%2F3HWff2ZkAy6sKPaJ%2BWLyidbs9Sm0Q9jVPSpWORCeNNm92GPh8iv%2FZgvd%2F%2BhUI%2F4ENzlurSfpEoEspvwi6863Um76O8dyIRuT2fNEaAR4G8HOZ80YjNy%2BB%2FnoRwFvC08sCU3GzRDimU5eL9dioNSy2wwSHQg%2Fms%2BHLbTofMl%2F18i1l78%2FBcJ3iJq%2FuVv86U6QECnXQqqLSAUkRG1ukD62jZUM6TpnLsHBErjCnjmh2tU%2BotI6l7CK3ewwU%2FB8AezN4uekBj2KBKY46KZi28N%2BWL2Xsi2INFr5N%2B93DJjarzSiqAImotfjrBAE%2FpR9U3PNeSRJfEH2Ic1%2FjVBG8aQKordPDCti7OnF5KVyZV%2B8J1jPkYtZBIHyLIU0zZ0gZVdyYH0Lnh2uoNAZi7VAy6LDsic93oYchq2t6zt3q5N9%2FBEyvHOTqgstSPTjwDpS%2Bw3jiyObb7N%2BqPn49bYFT9ZI9rtK09gQBvBA7d0LN6iMr2BHtQxK1PYMrVNdIHuMsp5rFWX0RE%2BuP07hioKU5UMeFEfayLezsz63gsqxH3im63yiE3c1i6PZxy%2FcIBZnUnKfzvLle%2BwUAZzePXWBD0KCG%2FGaM4ni1doQrp3TDe0ZO9BjqkAdZbzpAvrlIkIC3YtRoMsLN7JIuSbqrG0vli4xZ7jvgDSaY2AXCc4XJlYKaING1moTppEKj8WpNB9r9I8p2yZOLvMlDybbzfdhaZPo3AtXseYuW5fcXdc6balcNjfZ6zwnsn5tE9c%2BMWEn9QJRVke%2F3plYmjZ9XtxCnYnwBo9YpRJ55%2Bc9l5DX3zYNcXZjT9Pq%2FVqg7ydLUQrI%2FICvVEWG%2BooTQu&X-Amz-Signature=0d5c28bd745cdc1154d4467009c7abce1b2488600fec80f5437e8ab1271a3baa&X-Amz-SignedHeaders=host&x-id=GetObject)
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