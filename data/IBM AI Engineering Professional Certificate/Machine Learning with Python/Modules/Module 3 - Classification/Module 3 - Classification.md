

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HIEZASF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfUR%2BNWm9cvbdnP%2Frfo10RIc8LhujrGWuwqG16vBw4NAiBpu2O0TUALIt6mMU%2Fl620XB%2F40JI0jXnEV3lLLUIvZsiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsT2RRuW3hXkKkVzpKtwDhyhHuBgrCL1%2Fwi%2FthM5OTF46UEUO7ZaxjJfOMzQ1Hzk3kUmkmPOKliHqMToC7AC5BpThBSpTgmTHntDayqiPDFZnJj7FZZb3KZv%2BPcCNijmfeqKT3tQqpTVkbvz7BP%2BvsCKGpu8aB6HNqH0QHQGTX1xzQbG7CKHJuFFFM9rfwln0vgTORiGBy%2FsKE%2BwrxgTB4tGvs3tatrfy3pQALhn%2Bk7Ms139YDKya3Y96jx47Exwz63x07WWZyq5Hz%2BzJjttiZwLoSmOIuF7MP0GzyMRml6vkBrN68MsUhCEeDGHob7ZHLaa8xowUIuF832CbecTtSyTmP1%2Bnutgsb4amVq0ERcBalc%2BWeB%2BmQ9M5qzcFSN9Qonkqu%2BNG%2BOi4hCuQ8AiRbmXxTGmtSQh8AhgzC95re%2F89lG5Fpa70Amyrkva%2ByAQRTxcnJJt23W6rATBA%2BwyiwnurRi2fSabOhSkDwbHMPyRyfdiEtAxdoauLfwRTRCpD7barXYXYkhikvUshhpTZOxc4Zq9663Je2rSI7nxq4eujgeDnKxfvzZVhnIBAyI2dP86ieYwuEuL2SIvwzcJeWmwi0SFg70kIN5zjh6wuG0rw2vfeWHJGOdwj79BXRWrZWTMmNbIPXlH%2BhoMwuOT%2FvAY6pgHpBxE%2BcYFNlftehVgnVqEer2IenXIoHdtyfqFnrz0L5pZbyD66%2Ba0E99f7P6FSUEMiGyA2wYI3F%2Fsk3vRsoRz3X41OboXVXsOLH7BSo2MDaM2DRSWh3B6%2B7AH41xzsq1twGSajw9rqdiD70jJSNg7BmD4cImJmdEnYQLRf8d3zpXwEwXFJt5rwQmMEV%2F58XDRs3QMCulonwzw02f2nzKPPX2sHJppI&X-Amz-Signature=1c711a4ed88d64def2e67da93f7e1e846c0c56b47db1be00103bddd83ad2e590&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HIEZASF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfUR%2BNWm9cvbdnP%2Frfo10RIc8LhujrGWuwqG16vBw4NAiBpu2O0TUALIt6mMU%2Fl620XB%2F40JI0jXnEV3lLLUIvZsiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsT2RRuW3hXkKkVzpKtwDhyhHuBgrCL1%2Fwi%2FthM5OTF46UEUO7ZaxjJfOMzQ1Hzk3kUmkmPOKliHqMToC7AC5BpThBSpTgmTHntDayqiPDFZnJj7FZZb3KZv%2BPcCNijmfeqKT3tQqpTVkbvz7BP%2BvsCKGpu8aB6HNqH0QHQGTX1xzQbG7CKHJuFFFM9rfwln0vgTORiGBy%2FsKE%2BwrxgTB4tGvs3tatrfy3pQALhn%2Bk7Ms139YDKya3Y96jx47Exwz63x07WWZyq5Hz%2BzJjttiZwLoSmOIuF7MP0GzyMRml6vkBrN68MsUhCEeDGHob7ZHLaa8xowUIuF832CbecTtSyTmP1%2Bnutgsb4amVq0ERcBalc%2BWeB%2BmQ9M5qzcFSN9Qonkqu%2BNG%2BOi4hCuQ8AiRbmXxTGmtSQh8AhgzC95re%2F89lG5Fpa70Amyrkva%2ByAQRTxcnJJt23W6rATBA%2BwyiwnurRi2fSabOhSkDwbHMPyRyfdiEtAxdoauLfwRTRCpD7barXYXYkhikvUshhpTZOxc4Zq9663Je2rSI7nxq4eujgeDnKxfvzZVhnIBAyI2dP86ieYwuEuL2SIvwzcJeWmwi0SFg70kIN5zjh6wuG0rw2vfeWHJGOdwj79BXRWrZWTMmNbIPXlH%2BhoMwuOT%2FvAY6pgHpBxE%2BcYFNlftehVgnVqEer2IenXIoHdtyfqFnrz0L5pZbyD66%2Ba0E99f7P6FSUEMiGyA2wYI3F%2Fsk3vRsoRz3X41OboXVXsOLH7BSo2MDaM2DRSWh3B6%2B7AH41xzsq1twGSajw9rqdiD70jJSNg7BmD4cImJmdEnYQLRf8d3zpXwEwXFJt5rwQmMEV%2F58XDRs3QMCulonwzw02f2nzKPPX2sHJppI&X-Amz-Signature=12c9658307f123b4168c9cad8281574408a1606a2636b50d6b9c922f348f9464&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HIEZASF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfUR%2BNWm9cvbdnP%2Frfo10RIc8LhujrGWuwqG16vBw4NAiBpu2O0TUALIt6mMU%2Fl620XB%2F40JI0jXnEV3lLLUIvZsiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsT2RRuW3hXkKkVzpKtwDhyhHuBgrCL1%2Fwi%2FthM5OTF46UEUO7ZaxjJfOMzQ1Hzk3kUmkmPOKliHqMToC7AC5BpThBSpTgmTHntDayqiPDFZnJj7FZZb3KZv%2BPcCNijmfeqKT3tQqpTVkbvz7BP%2BvsCKGpu8aB6HNqH0QHQGTX1xzQbG7CKHJuFFFM9rfwln0vgTORiGBy%2FsKE%2BwrxgTB4tGvs3tatrfy3pQALhn%2Bk7Ms139YDKya3Y96jx47Exwz63x07WWZyq5Hz%2BzJjttiZwLoSmOIuF7MP0GzyMRml6vkBrN68MsUhCEeDGHob7ZHLaa8xowUIuF832CbecTtSyTmP1%2Bnutgsb4amVq0ERcBalc%2BWeB%2BmQ9M5qzcFSN9Qonkqu%2BNG%2BOi4hCuQ8AiRbmXxTGmtSQh8AhgzC95re%2F89lG5Fpa70Amyrkva%2ByAQRTxcnJJt23W6rATBA%2BwyiwnurRi2fSabOhSkDwbHMPyRyfdiEtAxdoauLfwRTRCpD7barXYXYkhikvUshhpTZOxc4Zq9663Je2rSI7nxq4eujgeDnKxfvzZVhnIBAyI2dP86ieYwuEuL2SIvwzcJeWmwi0SFg70kIN5zjh6wuG0rw2vfeWHJGOdwj79BXRWrZWTMmNbIPXlH%2BhoMwuOT%2FvAY6pgHpBxE%2BcYFNlftehVgnVqEer2IenXIoHdtyfqFnrz0L5pZbyD66%2Ba0E99f7P6FSUEMiGyA2wYI3F%2Fsk3vRsoRz3X41OboXVXsOLH7BSo2MDaM2DRSWh3B6%2B7AH41xzsq1twGSajw9rqdiD70jJSNg7BmD4cImJmdEnYQLRf8d3zpXwEwXFJt5rwQmMEV%2F58XDRs3QMCulonwzw02f2nzKPPX2sHJppI&X-Amz-Signature=98d9e66929a8cca375a32413a8d9c4f90ea2a094eb9d27ccb763e0a9489e94a6&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGXC5AOR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0PadGOo52C77DQbIJdoJ%2B3o1vvTN9dTL9e276i1mSqwIhAM1mdU7V51XIE5eDJEaQawFp5Mp9Q3sVNRY7ALvOpXN%2FKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2F7QHnElC%2FuzEGPQQq3APU9Y33cts%2BjNg1yVE1KkzyvshbQUN%2BgJoEi2Oh76hys07XLRM2kaASUiBdpoIl53KIliOxYgBNwjdUWPbk2hK7IfmgaeoS0FabrfFEIqBxX%2FAExb3CbZsVWGXYkovznn1rOe%2FDGdrR6Ap8Dxxat3%2F%2BOWbBJWO%2Bp6j9U43zaGhxxbESeU8w6r5gbzwUnUvgBs9hTHtl%2BkQjLMjWYyVnQMj7wwVfmEJ8zI9rY7fq9h%2BbP2pRQw6GFInqmojCfS%2B1isLvpqQi2vmpmKnQG6uRYjI7YjMneqavFEXhTHGEBvQlOt%2Ff4CBCp8ZvHRLrRkX5JseA4lkZOw1CVTaPZJ9T2WuhOCMy4dSEQZyg%2FOIzND7zuoJ1Tz%2BjHWD%2FHU50NA%2Fj6WlJALskIuQjBDgu6iWmtjWe1RUJvKRBpafMUbyvsXvNqgmq27p0C%2Bz1%2Fv184wtfop4nP%2F1IBPz26aFPEW2eDL5yH4UOWcmVWPlSxYJUnsKnHGZneGM5xyYwQMBLXvVv20z%2BORMXDUfvzMSiv%2F9PI1EB3P7dY3DepCZXUhpqv%2BMdgGVgeZe0HS%2F3RT8FzHiVrg5rO0t8fA23Ftq0ex0SKrDgAwD2bluuDctQeC4WglnqYhuQfY%2FVlKkjOo3QFjDX5f%2B8BjqkAZ12dQ5ExQkdkIV2Ea9wlYrRnUfGgNLA5n6skDMXo7JR4pIgKK5IWT4ZYo6tJ0E4G25h16%2BMbglsr8hkbLI%2F7%2FUUO4U9nv9BsxdNx0HNuiBUucQX0AnWAjMoJH85yp9hCW%2Bb2Y9jbTmuS%2BsddXQwCb4wpQ7DJkwQ1adRpFcVlnCuEvs0SctS%2BDEiuYrfyHRHmS4xyYAxbYwt%2Bvik8guZIoS2XfgG&X-Amz-Signature=f05c7995cb16efa4405712eaf4267722464ffd1c6c7092408435e67a406b89cb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGXC5AOR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0PadGOo52C77DQbIJdoJ%2B3o1vvTN9dTL9e276i1mSqwIhAM1mdU7V51XIE5eDJEaQawFp5Mp9Q3sVNRY7ALvOpXN%2FKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2F7QHnElC%2FuzEGPQQq3APU9Y33cts%2BjNg1yVE1KkzyvshbQUN%2BgJoEi2Oh76hys07XLRM2kaASUiBdpoIl53KIliOxYgBNwjdUWPbk2hK7IfmgaeoS0FabrfFEIqBxX%2FAExb3CbZsVWGXYkovznn1rOe%2FDGdrR6Ap8Dxxat3%2F%2BOWbBJWO%2Bp6j9U43zaGhxxbESeU8w6r5gbzwUnUvgBs9hTHtl%2BkQjLMjWYyVnQMj7wwVfmEJ8zI9rY7fq9h%2BbP2pRQw6GFInqmojCfS%2B1isLvpqQi2vmpmKnQG6uRYjI7YjMneqavFEXhTHGEBvQlOt%2Ff4CBCp8ZvHRLrRkX5JseA4lkZOw1CVTaPZJ9T2WuhOCMy4dSEQZyg%2FOIzND7zuoJ1Tz%2BjHWD%2FHU50NA%2Fj6WlJALskIuQjBDgu6iWmtjWe1RUJvKRBpafMUbyvsXvNqgmq27p0C%2Bz1%2Fv184wtfop4nP%2F1IBPz26aFPEW2eDL5yH4UOWcmVWPlSxYJUnsKnHGZneGM5xyYwQMBLXvVv20z%2BORMXDUfvzMSiv%2F9PI1EB3P7dY3DepCZXUhpqv%2BMdgGVgeZe0HS%2F3RT8FzHiVrg5rO0t8fA23Ftq0ex0SKrDgAwD2bluuDctQeC4WglnqYhuQfY%2FVlKkjOo3QFjDX5f%2B8BjqkAZ12dQ5ExQkdkIV2Ea9wlYrRnUfGgNLA5n6skDMXo7JR4pIgKK5IWT4ZYo6tJ0E4G25h16%2BMbglsr8hkbLI%2F7%2FUUO4U9nv9BsxdNx0HNuiBUucQX0AnWAjMoJH85yp9hCW%2Bb2Y9jbTmuS%2BsddXQwCb4wpQ7DJkwQ1adRpFcVlnCuEvs0SctS%2BDEiuYrfyHRHmS4xyYAxbYwt%2Bvik8guZIoS2XfgG&X-Amz-Signature=fca907fff75e09418a80d024dc1f290c706e594ace8239be8f92f04a0780c539&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HIEZASF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfUR%2BNWm9cvbdnP%2Frfo10RIc8LhujrGWuwqG16vBw4NAiBpu2O0TUALIt6mMU%2Fl620XB%2F40JI0jXnEV3lLLUIvZsiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsT2RRuW3hXkKkVzpKtwDhyhHuBgrCL1%2Fwi%2FthM5OTF46UEUO7ZaxjJfOMzQ1Hzk3kUmkmPOKliHqMToC7AC5BpThBSpTgmTHntDayqiPDFZnJj7FZZb3KZv%2BPcCNijmfeqKT3tQqpTVkbvz7BP%2BvsCKGpu8aB6HNqH0QHQGTX1xzQbG7CKHJuFFFM9rfwln0vgTORiGBy%2FsKE%2BwrxgTB4tGvs3tatrfy3pQALhn%2Bk7Ms139YDKya3Y96jx47Exwz63x07WWZyq5Hz%2BzJjttiZwLoSmOIuF7MP0GzyMRml6vkBrN68MsUhCEeDGHob7ZHLaa8xowUIuF832CbecTtSyTmP1%2Bnutgsb4amVq0ERcBalc%2BWeB%2BmQ9M5qzcFSN9Qonkqu%2BNG%2BOi4hCuQ8AiRbmXxTGmtSQh8AhgzC95re%2F89lG5Fpa70Amyrkva%2ByAQRTxcnJJt23W6rATBA%2BwyiwnurRi2fSabOhSkDwbHMPyRyfdiEtAxdoauLfwRTRCpD7barXYXYkhikvUshhpTZOxc4Zq9663Je2rSI7nxq4eujgeDnKxfvzZVhnIBAyI2dP86ieYwuEuL2SIvwzcJeWmwi0SFg70kIN5zjh6wuG0rw2vfeWHJGOdwj79BXRWrZWTMmNbIPXlH%2BhoMwuOT%2FvAY6pgHpBxE%2BcYFNlftehVgnVqEer2IenXIoHdtyfqFnrz0L5pZbyD66%2Ba0E99f7P6FSUEMiGyA2wYI3F%2Fsk3vRsoRz3X41OboXVXsOLH7BSo2MDaM2DRSWh3B6%2B7AH41xzsq1twGSajw9rqdiD70jJSNg7BmD4cImJmdEnYQLRf8d3zpXwEwXFJt5rwQmMEV%2F58XDRs3QMCulonwzw02f2nzKPPX2sHJppI&X-Amz-Signature=80345faed1605576a8afe75987008db06cf16dea7b2bbae98ec99efe9ca35c0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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