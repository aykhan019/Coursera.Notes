

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFZQZCLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5vmPSYMwCEs5Es8PbVZTJIbby3O9Kt03EHo108J7eZQIhAIEggZY2o9t%2BHueMlvoEkamn2mPuc4r3u%2F09su7P6Ax1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzk4cd3FAZXqpUOgTgq3AObvn2h6gdlll%2FbjOfIrcbOfaDGNcdUcQ9jLmzOS96%2FHVWVk72PmkE2%2FF8RItjs5AE8U0z7Djx8DS42AP77UPXdATsXnudIFDzFOHjlPJQ6uVXjwyxW6gEKnkM%2B6V5X9GzuhYb%2BesfDyamJaFBdZR0TJxUaDmA3DFTEF1sPaZH5Aebs11Ran7YKlKJlnn1T97s2OLB%2F84hrX3PqLPRrr9CkQVWuvyPN449vsZ8rqoGGZjx79Flwfer7qBJBzBhYRGWnWmWNrizxWZBJovfVmHnLeLGL26pid1dhj2l%2BZjqd41BpyQ1o0Zuevzi8Lu6gIhhHjAxNNEkBCPUxpq9S7B%2F%2BHR%2FS5Vj9IYh0cjt%2Fjk%2BaN%2F8Q4ni17smlO5jdWwXxQfAWOpgG1uy9aCJ5VyL0TkjbwqgbncRpwPsabX%2F7z8378r4o7ud1ZBHYcAE%2Bn8pvDmDgpuvN0roRPnhggT%2FaUFDVRGCVFjGP7edJHwv6ASVLE%2F3MHcNeaoQ8HGPsZW%2BMqh6dXKm2yQWnWkeYvyhFU%2FTIAQjaZKY51jR1K1rWs%2FQW7%2Fy5JoWPU%2BdfAHhipRkLf0DSlVRKF%2FIMCW%2FaohwtpCQ03ihItYVH50SWlbZq778fVPB6ZWdCndpFBHN3%2FjDm7PW8BjqkAUTNEjWtkYXEIWN%2Bd1W0SDk7cKOZ91wwOIwYwTEYCEwexPVJTCiMdcSbkgezs3hW%2BMAPUOzGTcIXPZe5C5poaArj2N4umK5RW6C6BiVED%2B22TDYEtu%2FIrPq6MvSjJKhFv4mCWnIWnDxwHSDNA6OCmHEcdA7aTfi3oE9QDGJU3weK819vMmke8y4%2FeFL0VXe%2FB5oGnB112ekZ8i1FFLGNINIO3q4Z&X-Amz-Signature=a97eeac329ac373bd129015e3704ad0d0a689ba172cd1c8dccaaabe08a8acc36&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFZQZCLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5vmPSYMwCEs5Es8PbVZTJIbby3O9Kt03EHo108J7eZQIhAIEggZY2o9t%2BHueMlvoEkamn2mPuc4r3u%2F09su7P6Ax1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzk4cd3FAZXqpUOgTgq3AObvn2h6gdlll%2FbjOfIrcbOfaDGNcdUcQ9jLmzOS96%2FHVWVk72PmkE2%2FF8RItjs5AE8U0z7Djx8DS42AP77UPXdATsXnudIFDzFOHjlPJQ6uVXjwyxW6gEKnkM%2B6V5X9GzuhYb%2BesfDyamJaFBdZR0TJxUaDmA3DFTEF1sPaZH5Aebs11Ran7YKlKJlnn1T97s2OLB%2F84hrX3PqLPRrr9CkQVWuvyPN449vsZ8rqoGGZjx79Flwfer7qBJBzBhYRGWnWmWNrizxWZBJovfVmHnLeLGL26pid1dhj2l%2BZjqd41BpyQ1o0Zuevzi8Lu6gIhhHjAxNNEkBCPUxpq9S7B%2F%2BHR%2FS5Vj9IYh0cjt%2Fjk%2BaN%2F8Q4ni17smlO5jdWwXxQfAWOpgG1uy9aCJ5VyL0TkjbwqgbncRpwPsabX%2F7z8378r4o7ud1ZBHYcAE%2Bn8pvDmDgpuvN0roRPnhggT%2FaUFDVRGCVFjGP7edJHwv6ASVLE%2F3MHcNeaoQ8HGPsZW%2BMqh6dXKm2yQWnWkeYvyhFU%2FTIAQjaZKY51jR1K1rWs%2FQW7%2Fy5JoWPU%2BdfAHhipRkLf0DSlVRKF%2FIMCW%2FaohwtpCQ03ihItYVH50SWlbZq778fVPB6ZWdCndpFBHN3%2FjDm7PW8BjqkAUTNEjWtkYXEIWN%2Bd1W0SDk7cKOZ91wwOIwYwTEYCEwexPVJTCiMdcSbkgezs3hW%2BMAPUOzGTcIXPZe5C5poaArj2N4umK5RW6C6BiVED%2B22TDYEtu%2FIrPq6MvSjJKhFv4mCWnIWnDxwHSDNA6OCmHEcdA7aTfi3oE9QDGJU3weK819vMmke8y4%2FeFL0VXe%2FB5oGnB112ekZ8i1FFLGNINIO3q4Z&X-Amz-Signature=f4e3b389c00fea55c81eea4d72628fdf903fdda62a3ae15fb48882c9426658f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFZQZCLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5vmPSYMwCEs5Es8PbVZTJIbby3O9Kt03EHo108J7eZQIhAIEggZY2o9t%2BHueMlvoEkamn2mPuc4r3u%2F09su7P6Ax1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzk4cd3FAZXqpUOgTgq3AObvn2h6gdlll%2FbjOfIrcbOfaDGNcdUcQ9jLmzOS96%2FHVWVk72PmkE2%2FF8RItjs5AE8U0z7Djx8DS42AP77UPXdATsXnudIFDzFOHjlPJQ6uVXjwyxW6gEKnkM%2B6V5X9GzuhYb%2BesfDyamJaFBdZR0TJxUaDmA3DFTEF1sPaZH5Aebs11Ran7YKlKJlnn1T97s2OLB%2F84hrX3PqLPRrr9CkQVWuvyPN449vsZ8rqoGGZjx79Flwfer7qBJBzBhYRGWnWmWNrizxWZBJovfVmHnLeLGL26pid1dhj2l%2BZjqd41BpyQ1o0Zuevzi8Lu6gIhhHjAxNNEkBCPUxpq9S7B%2F%2BHR%2FS5Vj9IYh0cjt%2Fjk%2BaN%2F8Q4ni17smlO5jdWwXxQfAWOpgG1uy9aCJ5VyL0TkjbwqgbncRpwPsabX%2F7z8378r4o7ud1ZBHYcAE%2Bn8pvDmDgpuvN0roRPnhggT%2FaUFDVRGCVFjGP7edJHwv6ASVLE%2F3MHcNeaoQ8HGPsZW%2BMqh6dXKm2yQWnWkeYvyhFU%2FTIAQjaZKY51jR1K1rWs%2FQW7%2Fy5JoWPU%2BdfAHhipRkLf0DSlVRKF%2FIMCW%2FaohwtpCQ03ihItYVH50SWlbZq778fVPB6ZWdCndpFBHN3%2FjDm7PW8BjqkAUTNEjWtkYXEIWN%2Bd1W0SDk7cKOZ91wwOIwYwTEYCEwexPVJTCiMdcSbkgezs3hW%2BMAPUOzGTcIXPZe5C5poaArj2N4umK5RW6C6BiVED%2B22TDYEtu%2FIrPq6MvSjJKhFv4mCWnIWnDxwHSDNA6OCmHEcdA7aTfi3oE9QDGJU3weK819vMmke8y4%2FeFL0VXe%2FB5oGnB112ekZ8i1FFLGNINIO3q4Z&X-Amz-Signature=e96c0c8430554a620ebaf551a6952c3fe79f50b97a44fb282ca2ffb7ebfc4bad&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYOKT3HJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvfoG%2B2EaTf8z8iJG%2BRlj8OZAi1i50ay7kZe7sLICF9wIgHBWmCfvDrGFtIUjI04vxCX5OwkZlhBg5vwDZzN%2B2bJkqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2BkiYLHixp8vZIArCrcA2%2B4GiTAyPG1eIq0seLGbjS66ZV3NSKDmiVsHhwfs2Vx6BM7Y80NeOIhMojEagRHaSOTJM1YJ5isWMbwsUliyv7PfXuzRCYJ0gEtmOc6KPoKF9ecUImHx5YbtRU9dmF4zxta2VbGl%2BCBHtPQBcv%2FuRD1pCOk0QCsycsnq2ahzOYPMuptcRl0tmGl%2B4ekiIaAJDmucLSOcPkzJImeRJr9ICSWcP1GfWogRWdjCvs57pbXAi4qtBaFem2%2FcxHURARW04%2FNNIhhwL00mYI1roWu9czX0VOzDOb6lqEcxEDIPuMONVnWv6rYuvmG7H9m9YlFqwMkRoFqaHrj5cgHWVcdNvL68OjSh%2BldMCfVutaTbb8sGIYKIovFHS5AzESYgvDsoRCR05uxD6RetExbJVhSatd3QaaJCHGS13ZgpOXZ7GTNOV%2Bi%2FXzYm%2Fi5velrSqWpRtUvs7kB8Ab8dBaQvy3s3%2BKW8kYQrAhBrREe3d%2BaI0v0%2BUVAdqPxPJ%2FZsjItjIwFBX7wYXOg2%2Fn2HOMj8DqFUzO57FnlPm3FDihRbJ%2FquV10uOr63ocqLXzHByF0Dnir8QIb88V5nQd3HFDfwF5i3QmeMyZk1K4MmI5eH6QHLJH%2FQ2QMXrOTDyKhykbdMNbs9bwGOqUB96rs%2Fo4dqWMrk9rNIai7v0QistPVXqIDl0d%2FyfKkAjpetzMKJRPx58lWCAlL%2Fpl%2BsEmKh7AofruI7a%2F1nEu5QO9lDmppgjhsbkc5HbjMcJEjx6myQh6w0yi7jfFd6z2VFR5d0sSjGCuJsmaVOXE804dUzMZUPOCpc5tk4zUegM5FgNdHfAyIpGQ39BYMH%2FNRZKNEwjHQlBEhqpRD1nHLE4dvMoeX&X-Amz-Signature=34ddbad3a6eb96a6a0ad0da29f48a1f046308154fccf023fc25d288f43d80a89&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYOKT3HJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvfoG%2B2EaTf8z8iJG%2BRlj8OZAi1i50ay7kZe7sLICF9wIgHBWmCfvDrGFtIUjI04vxCX5OwkZlhBg5vwDZzN%2B2bJkqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2BkiYLHixp8vZIArCrcA2%2B4GiTAyPG1eIq0seLGbjS66ZV3NSKDmiVsHhwfs2Vx6BM7Y80NeOIhMojEagRHaSOTJM1YJ5isWMbwsUliyv7PfXuzRCYJ0gEtmOc6KPoKF9ecUImHx5YbtRU9dmF4zxta2VbGl%2BCBHtPQBcv%2FuRD1pCOk0QCsycsnq2ahzOYPMuptcRl0tmGl%2B4ekiIaAJDmucLSOcPkzJImeRJr9ICSWcP1GfWogRWdjCvs57pbXAi4qtBaFem2%2FcxHURARW04%2FNNIhhwL00mYI1roWu9czX0VOzDOb6lqEcxEDIPuMONVnWv6rYuvmG7H9m9YlFqwMkRoFqaHrj5cgHWVcdNvL68OjSh%2BldMCfVutaTbb8sGIYKIovFHS5AzESYgvDsoRCR05uxD6RetExbJVhSatd3QaaJCHGS13ZgpOXZ7GTNOV%2Bi%2FXzYm%2Fi5velrSqWpRtUvs7kB8Ab8dBaQvy3s3%2BKW8kYQrAhBrREe3d%2BaI0v0%2BUVAdqPxPJ%2FZsjItjIwFBX7wYXOg2%2Fn2HOMj8DqFUzO57FnlPm3FDihRbJ%2FquV10uOr63ocqLXzHByF0Dnir8QIb88V5nQd3HFDfwF5i3QmeMyZk1K4MmI5eH6QHLJH%2FQ2QMXrOTDyKhykbdMNbs9bwGOqUB96rs%2Fo4dqWMrk9rNIai7v0QistPVXqIDl0d%2FyfKkAjpetzMKJRPx58lWCAlL%2Fpl%2BsEmKh7AofruI7a%2F1nEu5QO9lDmppgjhsbkc5HbjMcJEjx6myQh6w0yi7jfFd6z2VFR5d0sSjGCuJsmaVOXE804dUzMZUPOCpc5tk4zUegM5FgNdHfAyIpGQ39BYMH%2FNRZKNEwjHQlBEhqpRD1nHLE4dvMoeX&X-Amz-Signature=917a40abbe159d41fb08691b5c9acbaf4d9c9e442e47307982a203fec0e10f64&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFZQZCLD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5vmPSYMwCEs5Es8PbVZTJIbby3O9Kt03EHo108J7eZQIhAIEggZY2o9t%2BHueMlvoEkamn2mPuc4r3u%2F09su7P6Ax1KogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzk4cd3FAZXqpUOgTgq3AObvn2h6gdlll%2FbjOfIrcbOfaDGNcdUcQ9jLmzOS96%2FHVWVk72PmkE2%2FF8RItjs5AE8U0z7Djx8DS42AP77UPXdATsXnudIFDzFOHjlPJQ6uVXjwyxW6gEKnkM%2B6V5X9GzuhYb%2BesfDyamJaFBdZR0TJxUaDmA3DFTEF1sPaZH5Aebs11Ran7YKlKJlnn1T97s2OLB%2F84hrX3PqLPRrr9CkQVWuvyPN449vsZ8rqoGGZjx79Flwfer7qBJBzBhYRGWnWmWNrizxWZBJovfVmHnLeLGL26pid1dhj2l%2BZjqd41BpyQ1o0Zuevzi8Lu6gIhhHjAxNNEkBCPUxpq9S7B%2F%2BHR%2FS5Vj9IYh0cjt%2Fjk%2BaN%2F8Q4ni17smlO5jdWwXxQfAWOpgG1uy9aCJ5VyL0TkjbwqgbncRpwPsabX%2F7z8378r4o7ud1ZBHYcAE%2Bn8pvDmDgpuvN0roRPnhggT%2FaUFDVRGCVFjGP7edJHwv6ASVLE%2F3MHcNeaoQ8HGPsZW%2BMqh6dXKm2yQWnWkeYvyhFU%2FTIAQjaZKY51jR1K1rWs%2FQW7%2Fy5JoWPU%2BdfAHhipRkLf0DSlVRKF%2FIMCW%2FaohwtpCQ03ihItYVH50SWlbZq778fVPB6ZWdCndpFBHN3%2FjDm7PW8BjqkAUTNEjWtkYXEIWN%2Bd1W0SDk7cKOZ91wwOIwYwTEYCEwexPVJTCiMdcSbkgezs3hW%2BMAPUOzGTcIXPZe5C5poaArj2N4umK5RW6C6BiVED%2B22TDYEtu%2FIrPq6MvSjJKhFv4mCWnIWnDxwHSDNA6OCmHEcdA7aTfi3oE9QDGJU3weK819vMmke8y4%2FeFL0VXe%2FB5oGnB112ekZ8i1FFLGNINIO3q4Z&X-Amz-Signature=a838f94552e65042c934e84d09721abc0e173cfd608ff258a1190e5192a5612b&X-Amz-SignedHeaders=host&x-id=GetObject)
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