

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URWUWCJ5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDXfI7bZ1PWnzxopoepbCkVay1aadKXjlHhEuUhPjZmYgIgKzVIkhBDl379uiXmdb4Eodz3MjQyISjBrZWep8mBC0wq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDFJNBZKpHaAGgxHPdyrcA%2FxGjZBNLBVga4LV5ajjcTKJwwwGaNkNAbqot29enruMJczzxvTg5nuaxWaVgzvf8tGaHKMeOOFz255yyYaXyVSnXzFuaNor1b152CAj9ufQiK7B6YB0JGGImPcUMx9Kk1D2ZTDMQA3B%2FPLKmIgZgfXWRh8X%2BZXWvDCg2lspYpwS%2FFPDvZlj9o%2B4xgxkP7e9kHcvVEdFlCI12N077xjjtqUshU3evrgGWgs5hxM91Ukdu27BR5N5lgdgBbMbqJtudTgwgUlXbSaSt4kCZdOI%2F09K2OM0orwWhB%2F6Wbzxp84%2B7cKHHxyj3o7s%2Fn0IzZ%2BfiZKcdWagZOfDZqdG9NGvIvli7oJrLKVzSIsdrVe2dhJ7rDGvoRBq4uwCnqu21kcHjiU7OR6FQuJsWcrGNapfrRqJPg4LlNYxwCQ7X37aGdeRn8V0u%2FJdEiTldj8QBAfBGNbnZyW8R%2FOi7IwWiMu7WRXTjBRqvOYcYgC7NGzpkV1Yd%2FSpQWcns1O8sDC%2BldQTKTYXI%2BS0MGqXD5tkUKP%2F2exwHHCYhulwlA%2FrV73VtIC2IT8c5voMTu2SERR949jOTSzMq5FUbKp8C4FBmTqpo3I3AYHrMa9v0ndpNaXy4ILAp0egD%2FhW8p%2F0ZJcgMIvPjL0GOqUBbQv8rFHsq%2F6KnP2P1I5Ol7qKcCH6hgjFrNUE%2BLDbxTW11iyd5ggg38qo%2FbgWdmi8C%2BxKfNdEM9ABsndmqhMzeHkYcvcxDF4yGmQn6EUi%2Ft%2BEDSY7at8id3ovnNRvhqDDVLR8HjT0EPPRLMr8uSx26uES4FzEd44eGzVjaJWtzf6wHglT3tbrMNMFhIWUHfrbhf47gSrnTxa3l41Va6c23kT1KYOT&X-Amz-Signature=534f1fe4160fbb609ecbe2b1d70a1b5126dda6a3bf2b257c34ae02ca04a69dab&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URWUWCJ5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDXfI7bZ1PWnzxopoepbCkVay1aadKXjlHhEuUhPjZmYgIgKzVIkhBDl379uiXmdb4Eodz3MjQyISjBrZWep8mBC0wq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDFJNBZKpHaAGgxHPdyrcA%2FxGjZBNLBVga4LV5ajjcTKJwwwGaNkNAbqot29enruMJczzxvTg5nuaxWaVgzvf8tGaHKMeOOFz255yyYaXyVSnXzFuaNor1b152CAj9ufQiK7B6YB0JGGImPcUMx9Kk1D2ZTDMQA3B%2FPLKmIgZgfXWRh8X%2BZXWvDCg2lspYpwS%2FFPDvZlj9o%2B4xgxkP7e9kHcvVEdFlCI12N077xjjtqUshU3evrgGWgs5hxM91Ukdu27BR5N5lgdgBbMbqJtudTgwgUlXbSaSt4kCZdOI%2F09K2OM0orwWhB%2F6Wbzxp84%2B7cKHHxyj3o7s%2Fn0IzZ%2BfiZKcdWagZOfDZqdG9NGvIvli7oJrLKVzSIsdrVe2dhJ7rDGvoRBq4uwCnqu21kcHjiU7OR6FQuJsWcrGNapfrRqJPg4LlNYxwCQ7X37aGdeRn8V0u%2FJdEiTldj8QBAfBGNbnZyW8R%2FOi7IwWiMu7WRXTjBRqvOYcYgC7NGzpkV1Yd%2FSpQWcns1O8sDC%2BldQTKTYXI%2BS0MGqXD5tkUKP%2F2exwHHCYhulwlA%2FrV73VtIC2IT8c5voMTu2SERR949jOTSzMq5FUbKp8C4FBmTqpo3I3AYHrMa9v0ndpNaXy4ILAp0egD%2FhW8p%2F0ZJcgMIvPjL0GOqUBbQv8rFHsq%2F6KnP2P1I5Ol7qKcCH6hgjFrNUE%2BLDbxTW11iyd5ggg38qo%2FbgWdmi8C%2BxKfNdEM9ABsndmqhMzeHkYcvcxDF4yGmQn6EUi%2Ft%2BEDSY7at8id3ovnNRvhqDDVLR8HjT0EPPRLMr8uSx26uES4FzEd44eGzVjaJWtzf6wHglT3tbrMNMFhIWUHfrbhf47gSrnTxa3l41Va6c23kT1KYOT&X-Amz-Signature=1e05591a8c828aa57fbd79bf8d336332fdbd701fd052ddc1c6b813654043964c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URWUWCJ5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDXfI7bZ1PWnzxopoepbCkVay1aadKXjlHhEuUhPjZmYgIgKzVIkhBDl379uiXmdb4Eodz3MjQyISjBrZWep8mBC0wq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDFJNBZKpHaAGgxHPdyrcA%2FxGjZBNLBVga4LV5ajjcTKJwwwGaNkNAbqot29enruMJczzxvTg5nuaxWaVgzvf8tGaHKMeOOFz255yyYaXyVSnXzFuaNor1b152CAj9ufQiK7B6YB0JGGImPcUMx9Kk1D2ZTDMQA3B%2FPLKmIgZgfXWRh8X%2BZXWvDCg2lspYpwS%2FFPDvZlj9o%2B4xgxkP7e9kHcvVEdFlCI12N077xjjtqUshU3evrgGWgs5hxM91Ukdu27BR5N5lgdgBbMbqJtudTgwgUlXbSaSt4kCZdOI%2F09K2OM0orwWhB%2F6Wbzxp84%2B7cKHHxyj3o7s%2Fn0IzZ%2BfiZKcdWagZOfDZqdG9NGvIvli7oJrLKVzSIsdrVe2dhJ7rDGvoRBq4uwCnqu21kcHjiU7OR6FQuJsWcrGNapfrRqJPg4LlNYxwCQ7X37aGdeRn8V0u%2FJdEiTldj8QBAfBGNbnZyW8R%2FOi7IwWiMu7WRXTjBRqvOYcYgC7NGzpkV1Yd%2FSpQWcns1O8sDC%2BldQTKTYXI%2BS0MGqXD5tkUKP%2F2exwHHCYhulwlA%2FrV73VtIC2IT8c5voMTu2SERR949jOTSzMq5FUbKp8C4FBmTqpo3I3AYHrMa9v0ndpNaXy4ILAp0egD%2FhW8p%2F0ZJcgMIvPjL0GOqUBbQv8rFHsq%2F6KnP2P1I5Ol7qKcCH6hgjFrNUE%2BLDbxTW11iyd5ggg38qo%2FbgWdmi8C%2BxKfNdEM9ABsndmqhMzeHkYcvcxDF4yGmQn6EUi%2Ft%2BEDSY7at8id3ovnNRvhqDDVLR8HjT0EPPRLMr8uSx26uES4FzEd44eGzVjaJWtzf6wHglT3tbrMNMFhIWUHfrbhf47gSrnTxa3l41Va6c23kT1KYOT&X-Amz-Signature=6b87382cb69ced527597d4595b051182f67825b849254c61b3ef831d74e26dc1&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5TUX2WN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIBOaMmIIFGn8JHLtYVPjzqXWc5gIcSrobItJHKK5zfGtAiEA%2BAAKyMGKULR4r8LZdzSeM%2FOG2%2FFTEBQ6%2FsouZ4QxMncq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDFPRUbLHWAR9Sg7inCrcA9nUeSm8VmetGdzK%2B39LPfEDG%2B%2FaWYs%2BUcINQdceopeZeHWDaJ8wdhFYur%2B5NEHZZDThV00niDbdr8eHHIXqScE5TabjiBp9mROjPB3Vgqnom0bW0RbSfYiewO2Msaq2o%2Fk0pw3mdIr16z7SekESa1JMAT2lE4N%2BBNp%2BBT7wb3ifF7ns%2BJdUbWVg%2FFpoSxomd0LsYtYhYQRanQ9wT3fzQGjjIdJ4DVLev2Dq9ax41FfPWh1Ly%2BAVTleJCK8YMmsmP1gfc3uq%2F9L3WYxAGaTZ5%2FfyH2Fl21%2F3RDbwfn%2FdczkSZyVnvwajQsjjt%2Fe0m4rZai9p3o%2BJivGZuFBpRCmX27dc3G3lzC4zpsYPxjsoUk70yMwXduqkRR6iWjDb3%2BddvSLIK6tm5XnasWcM%2F4uiAgFNZrHdDFdah6Avp8SengW%2F3ZNtUmwlTBatlTCCukmLY15uAVwQvunCSAlU7bA8dCthG031f%2FcrV0l4nI853owqmCjunMqASWRp5YXnz1peFMa1AlvVStr7X%2FVaYkR9u9QyS4V%2FIkHKMCbnvh86rHtWrastaWlUX4eg%2BdRk%2FT2nYivV6U3uadYw2UR28q%2FjkdAGU0Of6Tf422%2FEUPrX%2Bdo62xER2vDKlzg%2Fwh1JMJLPjL0GOqUBqYRWY%2B1J6NVddP%2FZRqmavUH3AHh4HDiblxm4CYSQRc%2FetnsK7jmlR9XwZg9%2FXz4pjp6j4GIzaBclgnxdhxGlE3alUj1AcmWUzc92COLiSmAHti3Ys1SMRkCXObnMDfe27wrJJIepFnip55HJ05tFtwBim11zuJRPjR9H6Y%2Fvc%2B6g80xXcjGq8KFxAiXyDOOVhou%2BqlnFua0egtLhg6G1FPa0RARb&X-Amz-Signature=6f65a86f47a44c6950785aafd9ff947de3a2f5a8c7e273055e89852390fd797c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5TUX2WN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIBOaMmIIFGn8JHLtYVPjzqXWc5gIcSrobItJHKK5zfGtAiEA%2BAAKyMGKULR4r8LZdzSeM%2FOG2%2FFTEBQ6%2FsouZ4QxMncq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDFPRUbLHWAR9Sg7inCrcA9nUeSm8VmetGdzK%2B39LPfEDG%2B%2FaWYs%2BUcINQdceopeZeHWDaJ8wdhFYur%2B5NEHZZDThV00niDbdr8eHHIXqScE5TabjiBp9mROjPB3Vgqnom0bW0RbSfYiewO2Msaq2o%2Fk0pw3mdIr16z7SekESa1JMAT2lE4N%2BBNp%2BBT7wb3ifF7ns%2BJdUbWVg%2FFpoSxomd0LsYtYhYQRanQ9wT3fzQGjjIdJ4DVLev2Dq9ax41FfPWh1Ly%2BAVTleJCK8YMmsmP1gfc3uq%2F9L3WYxAGaTZ5%2FfyH2Fl21%2F3RDbwfn%2FdczkSZyVnvwajQsjjt%2Fe0m4rZai9p3o%2BJivGZuFBpRCmX27dc3G3lzC4zpsYPxjsoUk70yMwXduqkRR6iWjDb3%2BddvSLIK6tm5XnasWcM%2F4uiAgFNZrHdDFdah6Avp8SengW%2F3ZNtUmwlTBatlTCCukmLY15uAVwQvunCSAlU7bA8dCthG031f%2FcrV0l4nI853owqmCjunMqASWRp5YXnz1peFMa1AlvVStr7X%2FVaYkR9u9QyS4V%2FIkHKMCbnvh86rHtWrastaWlUX4eg%2BdRk%2FT2nYivV6U3uadYw2UR28q%2FjkdAGU0Of6Tf422%2FEUPrX%2Bdo62xER2vDKlzg%2Fwh1JMJLPjL0GOqUBqYRWY%2B1J6NVddP%2FZRqmavUH3AHh4HDiblxm4CYSQRc%2FetnsK7jmlR9XwZg9%2FXz4pjp6j4GIzaBclgnxdhxGlE3alUj1AcmWUzc92COLiSmAHti3Ys1SMRkCXObnMDfe27wrJJIepFnip55HJ05tFtwBim11zuJRPjR9H6Y%2Fvc%2B6g80xXcjGq8KFxAiXyDOOVhou%2BqlnFua0egtLhg6G1FPa0RARb&X-Amz-Signature=561ab979046121aad338ab1b9ce3cb5030af2fe9257c8cb2789fb4f56f57c5bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URWUWCJ5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDXfI7bZ1PWnzxopoepbCkVay1aadKXjlHhEuUhPjZmYgIgKzVIkhBDl379uiXmdb4Eodz3MjQyISjBrZWep8mBC0wq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDFJNBZKpHaAGgxHPdyrcA%2FxGjZBNLBVga4LV5ajjcTKJwwwGaNkNAbqot29enruMJczzxvTg5nuaxWaVgzvf8tGaHKMeOOFz255yyYaXyVSnXzFuaNor1b152CAj9ufQiK7B6YB0JGGImPcUMx9Kk1D2ZTDMQA3B%2FPLKmIgZgfXWRh8X%2BZXWvDCg2lspYpwS%2FFPDvZlj9o%2B4xgxkP7e9kHcvVEdFlCI12N077xjjtqUshU3evrgGWgs5hxM91Ukdu27BR5N5lgdgBbMbqJtudTgwgUlXbSaSt4kCZdOI%2F09K2OM0orwWhB%2F6Wbzxp84%2B7cKHHxyj3o7s%2Fn0IzZ%2BfiZKcdWagZOfDZqdG9NGvIvli7oJrLKVzSIsdrVe2dhJ7rDGvoRBq4uwCnqu21kcHjiU7OR6FQuJsWcrGNapfrRqJPg4LlNYxwCQ7X37aGdeRn8V0u%2FJdEiTldj8QBAfBGNbnZyW8R%2FOi7IwWiMu7WRXTjBRqvOYcYgC7NGzpkV1Yd%2FSpQWcns1O8sDC%2BldQTKTYXI%2BS0MGqXD5tkUKP%2F2exwHHCYhulwlA%2FrV73VtIC2IT8c5voMTu2SERR949jOTSzMq5FUbKp8C4FBmTqpo3I3AYHrMa9v0ndpNaXy4ILAp0egD%2FhW8p%2F0ZJcgMIvPjL0GOqUBbQv8rFHsq%2F6KnP2P1I5Ol7qKcCH6hgjFrNUE%2BLDbxTW11iyd5ggg38qo%2FbgWdmi8C%2BxKfNdEM9ABsndmqhMzeHkYcvcxDF4yGmQn6EUi%2Ft%2BEDSY7at8id3ovnNRvhqDDVLR8HjT0EPPRLMr8uSx26uES4FzEd44eGzVjaJWtzf6wHglT3tbrMNMFhIWUHfrbhf47gSrnTxa3l41Va6c23kT1KYOT&X-Amz-Signature=aa8b8c1b4b82762e8d95fcec583b02e9460fba5196e496855478817d67569b0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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