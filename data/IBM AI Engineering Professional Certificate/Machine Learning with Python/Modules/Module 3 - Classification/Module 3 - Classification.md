

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWTAPI5E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNIcLffDic2jG4w%2BnCdIxVVhnAR%2BewE1rVnDUTaw0AKgIhAI6a8UCHTIRw1LjUuom%2Fi3dT9NGtd8YLpoKpd6J1dtXNKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc2g%2FrApLaD1i%2FPpgq3ANJBcPu9FoNfcxBXlStl5jqS6fuymp7jpMLCkKeXSAqwcOAyzV5uizafwBZqJIxZn8fMYRA79P%2BM%2FDNZl3aHmbBrqMwSvDaYoyTiwPGT%2BXvB2NioGU3fBVAhI0zmLf5NOeUv%2B%2BZiaRY109Upm4MH2paSdnZUyOMysXN8XEf%2BqYe2S0e02M0vc3RgfKwTNcnAx6kv43taAw%2BkFPx9OBrul9ekvkd%2BGRDLrwGXMpQxWLWN7abO69ET7oXqpCsFZiX63ERycjfzj2IC61%2B%2F1rc2zE%2BPfttLcXflLRF00jr2H%2FXbTrvpg6SfhIm7z%2ByZJlhj1%2FptLEqYoZPK99SW%2Fhs8vQngI6%2B5AswFyllQ3TQWItX8sGmBjNom1Rx8DLVwB9eDRo3j7OBFXixCP%2BBwhrf9reKrGp8fhlSichmfAKwxmlgChMSbEwZGGHEZPukkB1s9LHz0XOnlK3APpqU9Uo3TMgLU1ikqp7nFvN%2Fian5lubCrTcMIRDWCVr9%2BhNdtlKs3YwJFRccLflDNOgC2nM3SVyRwWSPZeSqbsUeZ3NnEvZho5jgqIjR1LPmeIInlj%2FeDpMt766g5qEVLzY493me2QZuA29L4fPsRIV9vNp%2Fyv2m5%2BJZxClYCJ3o3kszyzDP4fu8BjqkAWbKPvkle8FSqPXvrW%2B9XNhjI0geOSoatH50eevyOS11FTcJZcEkK2juVtwgcWxtg1ZvDQgM36tamVwYiSa27LndQPJJL7uThssaI5asiL0fpMFmqpixw52jmgW9rou%2BD%2FOMN2W4P7TIZqy8FXkpoGBYiWWlnYtk0uqPjJEKXQbmfIunLfqzw1whudpY50LEyJf2u%2Fp5NJtgkRDEuA%2B%2FXIT7B%2BxF&X-Amz-Signature=f74d1d63e017b6f4472e24ae71ead7e3569bd5abfbdefaf446dacbdaa2bc1e3a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWTAPI5E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNIcLffDic2jG4w%2BnCdIxVVhnAR%2BewE1rVnDUTaw0AKgIhAI6a8UCHTIRw1LjUuom%2Fi3dT9NGtd8YLpoKpd6J1dtXNKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc2g%2FrApLaD1i%2FPpgq3ANJBcPu9FoNfcxBXlStl5jqS6fuymp7jpMLCkKeXSAqwcOAyzV5uizafwBZqJIxZn8fMYRA79P%2BM%2FDNZl3aHmbBrqMwSvDaYoyTiwPGT%2BXvB2NioGU3fBVAhI0zmLf5NOeUv%2B%2BZiaRY109Upm4MH2paSdnZUyOMysXN8XEf%2BqYe2S0e02M0vc3RgfKwTNcnAx6kv43taAw%2BkFPx9OBrul9ekvkd%2BGRDLrwGXMpQxWLWN7abO69ET7oXqpCsFZiX63ERycjfzj2IC61%2B%2F1rc2zE%2BPfttLcXflLRF00jr2H%2FXbTrvpg6SfhIm7z%2ByZJlhj1%2FptLEqYoZPK99SW%2Fhs8vQngI6%2B5AswFyllQ3TQWItX8sGmBjNom1Rx8DLVwB9eDRo3j7OBFXixCP%2BBwhrf9reKrGp8fhlSichmfAKwxmlgChMSbEwZGGHEZPukkB1s9LHz0XOnlK3APpqU9Uo3TMgLU1ikqp7nFvN%2Fian5lubCrTcMIRDWCVr9%2BhNdtlKs3YwJFRccLflDNOgC2nM3SVyRwWSPZeSqbsUeZ3NnEvZho5jgqIjR1LPmeIInlj%2FeDpMt766g5qEVLzY493me2QZuA29L4fPsRIV9vNp%2Fyv2m5%2BJZxClYCJ3o3kszyzDP4fu8BjqkAWbKPvkle8FSqPXvrW%2B9XNhjI0geOSoatH50eevyOS11FTcJZcEkK2juVtwgcWxtg1ZvDQgM36tamVwYiSa27LndQPJJL7uThssaI5asiL0fpMFmqpixw52jmgW9rou%2BD%2FOMN2W4P7TIZqy8FXkpoGBYiWWlnYtk0uqPjJEKXQbmfIunLfqzw1whudpY50LEyJf2u%2Fp5NJtgkRDEuA%2B%2FXIT7B%2BxF&X-Amz-Signature=9241ee18b8bd24f039c68fbd64d9ab2a72bf1c5348ee4168a8a5e220b1bfc15a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWTAPI5E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNIcLffDic2jG4w%2BnCdIxVVhnAR%2BewE1rVnDUTaw0AKgIhAI6a8UCHTIRw1LjUuom%2Fi3dT9NGtd8YLpoKpd6J1dtXNKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc2g%2FrApLaD1i%2FPpgq3ANJBcPu9FoNfcxBXlStl5jqS6fuymp7jpMLCkKeXSAqwcOAyzV5uizafwBZqJIxZn8fMYRA79P%2BM%2FDNZl3aHmbBrqMwSvDaYoyTiwPGT%2BXvB2NioGU3fBVAhI0zmLf5NOeUv%2B%2BZiaRY109Upm4MH2paSdnZUyOMysXN8XEf%2BqYe2S0e02M0vc3RgfKwTNcnAx6kv43taAw%2BkFPx9OBrul9ekvkd%2BGRDLrwGXMpQxWLWN7abO69ET7oXqpCsFZiX63ERycjfzj2IC61%2B%2F1rc2zE%2BPfttLcXflLRF00jr2H%2FXbTrvpg6SfhIm7z%2ByZJlhj1%2FptLEqYoZPK99SW%2Fhs8vQngI6%2B5AswFyllQ3TQWItX8sGmBjNom1Rx8DLVwB9eDRo3j7OBFXixCP%2BBwhrf9reKrGp8fhlSichmfAKwxmlgChMSbEwZGGHEZPukkB1s9LHz0XOnlK3APpqU9Uo3TMgLU1ikqp7nFvN%2Fian5lubCrTcMIRDWCVr9%2BhNdtlKs3YwJFRccLflDNOgC2nM3SVyRwWSPZeSqbsUeZ3NnEvZho5jgqIjR1LPmeIInlj%2FeDpMt766g5qEVLzY493me2QZuA29L4fPsRIV9vNp%2Fyv2m5%2BJZxClYCJ3o3kszyzDP4fu8BjqkAWbKPvkle8FSqPXvrW%2B9XNhjI0geOSoatH50eevyOS11FTcJZcEkK2juVtwgcWxtg1ZvDQgM36tamVwYiSa27LndQPJJL7uThssaI5asiL0fpMFmqpixw52jmgW9rou%2BD%2FOMN2W4P7TIZqy8FXkpoGBYiWWlnYtk0uqPjJEKXQbmfIunLfqzw1whudpY50LEyJf2u%2Fp5NJtgkRDEuA%2B%2FXIT7B%2BxF&X-Amz-Signature=21ffcb3c2f85ade344da76de4041295f4a1dcd3bbb244eaeec225eed0922c437&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662TUKSK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIELsQpAYp9VK3jAb8e7hbrqmPRJ62OZb%2BguG9wtStD1cAiAj4tv6OFNJWW7CAFCt3E0Pd0L5t1HMM2VwcZNW8poJKiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiF3%2F2fCFb5nWg0KNKtwD5ZFErfsAAHRVm2cVmYpjUfYllzlrm6jZjLwrf86v3FLiGOBMJBsbkeE28an6077HSqLbVtGNXymApqn97D3n64dh7qxpEoAq17SeQ0iCjAUb1BU%2FGRU9gZPe8TSSlhgVI%2BmR%2FTKEd5gG4O8UaWmoo8FTnLYrMZXi5CzcCKddhAk9%2FQA3wHAHK%2B7E0BMy%2FOCayIoakiZPOQXcVW2%2BJb4DIV1Sf%2BQazWwEZ4MFDXgrfvSqQe5Gx%2FwKi%2BOq66yD3XDfGOPfG4o3rZfxMrX9rrG9bg10WT7jNF6AUf2kYuj%2FSPQ21F%2Fsr8Vyu750K52HE8YgjcC26B11gK%2FgG5I7YUrs2LAr4tp1WxmwitQo%2BHxdKP%2Fiq6yWLaHfMgpvFLDlWpSKD7372QIHjeLaGEYDxFh72pxWolMO%2BtYeA2p%2BjyNgWL7uh8I8pQ7s5iH3LEQoM0IHkIcUQ3bKJxIkUvDOHUzYOsLYcCer7nYFwPvEqeFE7geQEhHEyz%2BzokzNDj7t6tSkUSKsNsm8lRGf5tZOXrn8Vnpodfp5mERR%2BkDnal66UazxdiBrEQXA7YJY8H7qsEM3uIYQ9jXEKQp2hFFltLmR0jnINGB8G1EGsyjl5HWnOq9OHUcjN71f7mS2dyYwleH7vAY6pgEMyPpc3es4nYtTp3S4xJ%2FyxwOOfPCmyIfTohbj1y7CguJ05Hs3MUYbpT2FrHwhqd4DG87JeALiGPxwMcGRtznLY%2FejRL5wILJcWFIcnfvI4MXV5TpLlzYNOqqOqWjnyNZXMS3QGO5XzokQU4mbb9Olt%2BWHGsruDyA0dOtpDdlbccK4Z5fnPWiMiixzK%2B9CsEtlH0MN9G7AvzAriOgwbN%2FOiBGnCeDf&X-Amz-Signature=cb74095bd7634b31109107285b3e916d343aa4d7de62d2a0c808104dd981ad6c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662TUKSK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIELsQpAYp9VK3jAb8e7hbrqmPRJ62OZb%2BguG9wtStD1cAiAj4tv6OFNJWW7CAFCt3E0Pd0L5t1HMM2VwcZNW8poJKiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiF3%2F2fCFb5nWg0KNKtwD5ZFErfsAAHRVm2cVmYpjUfYllzlrm6jZjLwrf86v3FLiGOBMJBsbkeE28an6077HSqLbVtGNXymApqn97D3n64dh7qxpEoAq17SeQ0iCjAUb1BU%2FGRU9gZPe8TSSlhgVI%2BmR%2FTKEd5gG4O8UaWmoo8FTnLYrMZXi5CzcCKddhAk9%2FQA3wHAHK%2B7E0BMy%2FOCayIoakiZPOQXcVW2%2BJb4DIV1Sf%2BQazWwEZ4MFDXgrfvSqQe5Gx%2FwKi%2BOq66yD3XDfGOPfG4o3rZfxMrX9rrG9bg10WT7jNF6AUf2kYuj%2FSPQ21F%2Fsr8Vyu750K52HE8YgjcC26B11gK%2FgG5I7YUrs2LAr4tp1WxmwitQo%2BHxdKP%2Fiq6yWLaHfMgpvFLDlWpSKD7372QIHjeLaGEYDxFh72pxWolMO%2BtYeA2p%2BjyNgWL7uh8I8pQ7s5iH3LEQoM0IHkIcUQ3bKJxIkUvDOHUzYOsLYcCer7nYFwPvEqeFE7geQEhHEyz%2BzokzNDj7t6tSkUSKsNsm8lRGf5tZOXrn8Vnpodfp5mERR%2BkDnal66UazxdiBrEQXA7YJY8H7qsEM3uIYQ9jXEKQp2hFFltLmR0jnINGB8G1EGsyjl5HWnOq9OHUcjN71f7mS2dyYwleH7vAY6pgEMyPpc3es4nYtTp3S4xJ%2FyxwOOfPCmyIfTohbj1y7CguJ05Hs3MUYbpT2FrHwhqd4DG87JeALiGPxwMcGRtznLY%2FejRL5wILJcWFIcnfvI4MXV5TpLlzYNOqqOqWjnyNZXMS3QGO5XzokQU4mbb9Olt%2BWHGsruDyA0dOtpDdlbccK4Z5fnPWiMiixzK%2B9CsEtlH0MN9G7AvzAriOgwbN%2FOiBGnCeDf&X-Amz-Signature=301ec9d43cf10f0b90785e14e9c0c7bac309c948ac297024f2f8f0621ec3247e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWTAPI5E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNIcLffDic2jG4w%2BnCdIxVVhnAR%2BewE1rVnDUTaw0AKgIhAI6a8UCHTIRw1LjUuom%2Fi3dT9NGtd8YLpoKpd6J1dtXNKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzc2g%2FrApLaD1i%2FPpgq3ANJBcPu9FoNfcxBXlStl5jqS6fuymp7jpMLCkKeXSAqwcOAyzV5uizafwBZqJIxZn8fMYRA79P%2BM%2FDNZl3aHmbBrqMwSvDaYoyTiwPGT%2BXvB2NioGU3fBVAhI0zmLf5NOeUv%2B%2BZiaRY109Upm4MH2paSdnZUyOMysXN8XEf%2BqYe2S0e02M0vc3RgfKwTNcnAx6kv43taAw%2BkFPx9OBrul9ekvkd%2BGRDLrwGXMpQxWLWN7abO69ET7oXqpCsFZiX63ERycjfzj2IC61%2B%2F1rc2zE%2BPfttLcXflLRF00jr2H%2FXbTrvpg6SfhIm7z%2ByZJlhj1%2FptLEqYoZPK99SW%2Fhs8vQngI6%2B5AswFyllQ3TQWItX8sGmBjNom1Rx8DLVwB9eDRo3j7OBFXixCP%2BBwhrf9reKrGp8fhlSichmfAKwxmlgChMSbEwZGGHEZPukkB1s9LHz0XOnlK3APpqU9Uo3TMgLU1ikqp7nFvN%2Fian5lubCrTcMIRDWCVr9%2BhNdtlKs3YwJFRccLflDNOgC2nM3SVyRwWSPZeSqbsUeZ3NnEvZho5jgqIjR1LPmeIInlj%2FeDpMt766g5qEVLzY493me2QZuA29L4fPsRIV9vNp%2Fyv2m5%2BJZxClYCJ3o3kszyzDP4fu8BjqkAWbKPvkle8FSqPXvrW%2B9XNhjI0geOSoatH50eevyOS11FTcJZcEkK2juVtwgcWxtg1ZvDQgM36tamVwYiSa27LndQPJJL7uThssaI5asiL0fpMFmqpixw52jmgW9rou%2BD%2FOMN2W4P7TIZqy8FXkpoGBYiWWlnYtk0uqPjJEKXQbmfIunLfqzw1whudpY50LEyJf2u%2Fp5NJtgkRDEuA%2B%2FXIT7B%2BxF&X-Amz-Signature=4eabece6f36238cd3923bf6709fcb74dc5fa78c3728e93917563a44b4b6e5bea&X-Amz-SignedHeaders=host&x-id=GetObject)
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