

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZADSVGG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDImZF1KFm928a1%2B8ZoBMuZf%2BP7EnVykfoqajcE6ekRjwIgUXQSK50Ur1sXeuehAQjahH%2FgXevymL6vfXgm1jqlSIgq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDLOLBYzMbyOt9O3f0yrcA%2F6xAnXOjeklNyIVddLWHzd4iFHFEYpS2TKO8pBvAZcMm2kSOumnDi7wcKlNBUblyF9YzwS3Eh46F4WfhUMeMJR5EbqwKwR6L3wnFn20lw9prgCSCSj69s7mFmc7USN3FtMLPMCRzl69WCxnptDByfFqBv9bcBKDlFvUl5rDZBC6h3v11afjbEjzz6I7e3TD%2BhdUnpn24X0UnKiTrO6aALLoyUnLmD6BKlROAUJM9AZifK4Ui3jZA%2FK7iOG%2B4ZP9F9wYvYRRl4S6cfGtamAs%2B7UeFmfvEZW2J6wfFdbpRto0Hg35FMAR0RBt4hifLrgTKfkhV7tgB9pDy6qajcHGQF2OEEory3iRBVjKFFSA4%2FlpsbPoUeChFl6zzpLLDaY2M9LWP8EGYr%2BP0of3tpbmI9eoPDgWtvS30A8eLmPQYPN7oa2x%2B65NTQcM6sxsJySbhASQ5iqLpgo9LXAv7N7k%2BP7Dnq545kRlReX5MBjz%2Fot3lGENiiaXPZkTCypasAY1kKBj46bWdH7WV%2FIMAvgdVEMuszxpFhJsbC1jQq8Rf1qK57e0RMuk6rzfdj9LLc58uWm3Ig0kKM4Cos8MrS2FJpCjAgK0SKUUcax59XJ3UPqm7KJZLrdlgUFGLpdWMJjniL0GOqUBC44VKdchRefv8FCPujGDQctuS3qcpl8zSS5q2IsQqVxRrPQOlzftSPJncGYSOeG4wEzD32gQJEw1HeJfH03Qq9HLh7IHMnoA4cWLrwwUq3YU0VSZ6Qpqd9PdJKuLeIbdBM9shqrHdJDoSPklUZjTFjDGC52gQF%2FjS%2BJkLivWDYjKWS53qdmSeCvdvgBYKuUF4JafnypMuPiCouNw6pXmvps6uW5j&X-Amz-Signature=8be99b59e4392a682d832eff5b666016e7617806300afacade83d59488eee51b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZADSVGG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDImZF1KFm928a1%2B8ZoBMuZf%2BP7EnVykfoqajcE6ekRjwIgUXQSK50Ur1sXeuehAQjahH%2FgXevymL6vfXgm1jqlSIgq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDLOLBYzMbyOt9O3f0yrcA%2F6xAnXOjeklNyIVddLWHzd4iFHFEYpS2TKO8pBvAZcMm2kSOumnDi7wcKlNBUblyF9YzwS3Eh46F4WfhUMeMJR5EbqwKwR6L3wnFn20lw9prgCSCSj69s7mFmc7USN3FtMLPMCRzl69WCxnptDByfFqBv9bcBKDlFvUl5rDZBC6h3v11afjbEjzz6I7e3TD%2BhdUnpn24X0UnKiTrO6aALLoyUnLmD6BKlROAUJM9AZifK4Ui3jZA%2FK7iOG%2B4ZP9F9wYvYRRl4S6cfGtamAs%2B7UeFmfvEZW2J6wfFdbpRto0Hg35FMAR0RBt4hifLrgTKfkhV7tgB9pDy6qajcHGQF2OEEory3iRBVjKFFSA4%2FlpsbPoUeChFl6zzpLLDaY2M9LWP8EGYr%2BP0of3tpbmI9eoPDgWtvS30A8eLmPQYPN7oa2x%2B65NTQcM6sxsJySbhASQ5iqLpgo9LXAv7N7k%2BP7Dnq545kRlReX5MBjz%2Fot3lGENiiaXPZkTCypasAY1kKBj46bWdH7WV%2FIMAvgdVEMuszxpFhJsbC1jQq8Rf1qK57e0RMuk6rzfdj9LLc58uWm3Ig0kKM4Cos8MrS2FJpCjAgK0SKUUcax59XJ3UPqm7KJZLrdlgUFGLpdWMJjniL0GOqUBC44VKdchRefv8FCPujGDQctuS3qcpl8zSS5q2IsQqVxRrPQOlzftSPJncGYSOeG4wEzD32gQJEw1HeJfH03Qq9HLh7IHMnoA4cWLrwwUq3YU0VSZ6Qpqd9PdJKuLeIbdBM9shqrHdJDoSPklUZjTFjDGC52gQF%2FjS%2BJkLivWDYjKWS53qdmSeCvdvgBYKuUF4JafnypMuPiCouNw6pXmvps6uW5j&X-Amz-Signature=f31204de3c17f655bcef13ba2adce7d8722fc4529cf38327970bee7b475909d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZADSVGG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDImZF1KFm928a1%2B8ZoBMuZf%2BP7EnVykfoqajcE6ekRjwIgUXQSK50Ur1sXeuehAQjahH%2FgXevymL6vfXgm1jqlSIgq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDLOLBYzMbyOt9O3f0yrcA%2F6xAnXOjeklNyIVddLWHzd4iFHFEYpS2TKO8pBvAZcMm2kSOumnDi7wcKlNBUblyF9YzwS3Eh46F4WfhUMeMJR5EbqwKwR6L3wnFn20lw9prgCSCSj69s7mFmc7USN3FtMLPMCRzl69WCxnptDByfFqBv9bcBKDlFvUl5rDZBC6h3v11afjbEjzz6I7e3TD%2BhdUnpn24X0UnKiTrO6aALLoyUnLmD6BKlROAUJM9AZifK4Ui3jZA%2FK7iOG%2B4ZP9F9wYvYRRl4S6cfGtamAs%2B7UeFmfvEZW2J6wfFdbpRto0Hg35FMAR0RBt4hifLrgTKfkhV7tgB9pDy6qajcHGQF2OEEory3iRBVjKFFSA4%2FlpsbPoUeChFl6zzpLLDaY2M9LWP8EGYr%2BP0of3tpbmI9eoPDgWtvS30A8eLmPQYPN7oa2x%2B65NTQcM6sxsJySbhASQ5iqLpgo9LXAv7N7k%2BP7Dnq545kRlReX5MBjz%2Fot3lGENiiaXPZkTCypasAY1kKBj46bWdH7WV%2FIMAvgdVEMuszxpFhJsbC1jQq8Rf1qK57e0RMuk6rzfdj9LLc58uWm3Ig0kKM4Cos8MrS2FJpCjAgK0SKUUcax59XJ3UPqm7KJZLrdlgUFGLpdWMJjniL0GOqUBC44VKdchRefv8FCPujGDQctuS3qcpl8zSS5q2IsQqVxRrPQOlzftSPJncGYSOeG4wEzD32gQJEw1HeJfH03Qq9HLh7IHMnoA4cWLrwwUq3YU0VSZ6Qpqd9PdJKuLeIbdBM9shqrHdJDoSPklUZjTFjDGC52gQF%2FjS%2BJkLivWDYjKWS53qdmSeCvdvgBYKuUF4JafnypMuPiCouNw6pXmvps6uW5j&X-Amz-Signature=a134c6d917af52a6ea5ccf5bac08a26d4a60e01a33c4198fe2e39f003435bce7&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KIOVZSM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQCRs5jLLfXPcC%2BiWj1nzt0eB9SCbn5NW5HkxCR8QhRNSQIgYNji28XY%2F3qdHclmzclqEVKhMZ7lM%2FOgcJ0XKuHVK9kq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDHkAgwokULGh5SLr9CrcA4KED6QDUoNmcWDho4uPvc99DT8OX41kLG0cf4QcVHd2LFM12fBIDa5sye8KP7DHUo8ARUwP8SfV7hs6NYh4GDnhRhsax1yY7FWYEhSIExSC0ehXo5dVgAz7PQJ2drFdVXrmFqT33UR4NDjqWwODNqx0T4bqGfLCUC%2FFPSYZkhn9mLBZAwlvZrEPpoMuUr%2F2%2FaW7ZmPBf%2FE2Ki8gRt53xCgNCXIPmDihbKU2b8O8YhUIlvbyBhZxOaG6agRe%2Frcp4FoT0iXjWJvW4OaV0E7cUjCuQEvdzCmeJ6RoFoTdpyVW7BdlUR8CXvtjFf8JywnyhsWFKLQCMB%2BH2%2BmmCMxXE7cI02rQToGt6PQCxhaaWSMHMbSX%2F0G4ceE%2BcgYVP9rDgbFS84tBJ5efA%2Bgn2WeoHqL8eAWlyCZdZHFRr143yWSc6Dp3UaxOGwzFjjG1I4%2FmC%2B6b%2FXRRGxb5t7%2BxCgIojVSe6BOTS6oD6R79KFjkRtYOUcI7%2BQt%2Fa0EuNv1Ryh%2Fmfj9Ht6W2OHPe%2F2d9pzvojjKkMMr8bNm5tDBwgyqwhty4g4Xf8d6Yco9Pbu2XcQ0%2FSWOF0SKXbMvEFoJKIrlOIAMgEJSMwCakyqoEJPNqObz5A5r7B2K9s%2BmOz1mMMJTniL0GOqUBeqkKuaM4kjklouXR9COKV0YifrYAsopy84ZIue5fem96tzYEve1JlHefx6kMHhI8a6XaQLIo6qOwr9E0Yug8N68ZWK1HC5j9ewflY86fb0nmNOfH4mT9tQex5kkX9dWYTD2erMS73NzgohfjX8vrZxnB%2BF82C612%2F4d2gc1fjseNVFbMccOIWSVOyqKgJBfzw3LBbi5FG7WxGbgP52SEAfUoRKRo&X-Amz-Signature=f0b7458215e1c169e4888c097f957b3e582b8230cbe5651d1993d06c512a9371&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KIOVZSM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQCRs5jLLfXPcC%2BiWj1nzt0eB9SCbn5NW5HkxCR8QhRNSQIgYNji28XY%2F3qdHclmzclqEVKhMZ7lM%2FOgcJ0XKuHVK9kq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDHkAgwokULGh5SLr9CrcA4KED6QDUoNmcWDho4uPvc99DT8OX41kLG0cf4QcVHd2LFM12fBIDa5sye8KP7DHUo8ARUwP8SfV7hs6NYh4GDnhRhsax1yY7FWYEhSIExSC0ehXo5dVgAz7PQJ2drFdVXrmFqT33UR4NDjqWwODNqx0T4bqGfLCUC%2FFPSYZkhn9mLBZAwlvZrEPpoMuUr%2F2%2FaW7ZmPBf%2FE2Ki8gRt53xCgNCXIPmDihbKU2b8O8YhUIlvbyBhZxOaG6agRe%2Frcp4FoT0iXjWJvW4OaV0E7cUjCuQEvdzCmeJ6RoFoTdpyVW7BdlUR8CXvtjFf8JywnyhsWFKLQCMB%2BH2%2BmmCMxXE7cI02rQToGt6PQCxhaaWSMHMbSX%2F0G4ceE%2BcgYVP9rDgbFS84tBJ5efA%2Bgn2WeoHqL8eAWlyCZdZHFRr143yWSc6Dp3UaxOGwzFjjG1I4%2FmC%2B6b%2FXRRGxb5t7%2BxCgIojVSe6BOTS6oD6R79KFjkRtYOUcI7%2BQt%2Fa0EuNv1Ryh%2Fmfj9Ht6W2OHPe%2F2d9pzvojjKkMMr8bNm5tDBwgyqwhty4g4Xf8d6Yco9Pbu2XcQ0%2FSWOF0SKXbMvEFoJKIrlOIAMgEJSMwCakyqoEJPNqObz5A5r7B2K9s%2BmOz1mMMJTniL0GOqUBeqkKuaM4kjklouXR9COKV0YifrYAsopy84ZIue5fem96tzYEve1JlHefx6kMHhI8a6XaQLIo6qOwr9E0Yug8N68ZWK1HC5j9ewflY86fb0nmNOfH4mT9tQex5kkX9dWYTD2erMS73NzgohfjX8vrZxnB%2BF82C612%2F4d2gc1fjseNVFbMccOIWSVOyqKgJBfzw3LBbi5FG7WxGbgP52SEAfUoRKRo&X-Amz-Signature=0612fae9beb7cad9f0df48bbfb3aa2f9be6fefd879840a1355dbc2e4e0173a96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZADSVGG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDImZF1KFm928a1%2B8ZoBMuZf%2BP7EnVykfoqajcE6ekRjwIgUXQSK50Ur1sXeuehAQjahH%2FgXevymL6vfXgm1jqlSIgq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDLOLBYzMbyOt9O3f0yrcA%2F6xAnXOjeklNyIVddLWHzd4iFHFEYpS2TKO8pBvAZcMm2kSOumnDi7wcKlNBUblyF9YzwS3Eh46F4WfhUMeMJR5EbqwKwR6L3wnFn20lw9prgCSCSj69s7mFmc7USN3FtMLPMCRzl69WCxnptDByfFqBv9bcBKDlFvUl5rDZBC6h3v11afjbEjzz6I7e3TD%2BhdUnpn24X0UnKiTrO6aALLoyUnLmD6BKlROAUJM9AZifK4Ui3jZA%2FK7iOG%2B4ZP9F9wYvYRRl4S6cfGtamAs%2B7UeFmfvEZW2J6wfFdbpRto0Hg35FMAR0RBt4hifLrgTKfkhV7tgB9pDy6qajcHGQF2OEEory3iRBVjKFFSA4%2FlpsbPoUeChFl6zzpLLDaY2M9LWP8EGYr%2BP0of3tpbmI9eoPDgWtvS30A8eLmPQYPN7oa2x%2B65NTQcM6sxsJySbhASQ5iqLpgo9LXAv7N7k%2BP7Dnq545kRlReX5MBjz%2Fot3lGENiiaXPZkTCypasAY1kKBj46bWdH7WV%2FIMAvgdVEMuszxpFhJsbC1jQq8Rf1qK57e0RMuk6rzfdj9LLc58uWm3Ig0kKM4Cos8MrS2FJpCjAgK0SKUUcax59XJ3UPqm7KJZLrdlgUFGLpdWMJjniL0GOqUBC44VKdchRefv8FCPujGDQctuS3qcpl8zSS5q2IsQqVxRrPQOlzftSPJncGYSOeG4wEzD32gQJEw1HeJfH03Qq9HLh7IHMnoA4cWLrwwUq3YU0VSZ6Qpqd9PdJKuLeIbdBM9shqrHdJDoSPklUZjTFjDGC52gQF%2FjS%2BJkLivWDYjKWS53qdmSeCvdvgBYKuUF4JafnypMuPiCouNw6pXmvps6uW5j&X-Amz-Signature=062c3f75de7a314fac837da68fc7e6f2e958ba68f4bfc332a095d986114aba42&X-Amz-SignedHeaders=host&x-id=GetObject)
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