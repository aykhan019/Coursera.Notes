

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PNV2GZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPNdsZVU%2Fnf8ool2EdtqSic50WsQQ838wIkiQseu%2FHUgIgIm1kRWQRzVhYAWHE72fYiN1o1h%2BUnwM4Pi2GDeEnOm8qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFI9EWF53ZLDGXyRFyrcA7R42cp5JuDDgZyr6nfn8g29JNUh4oZIqvuzVgzey6PlNOtcM5MyLdUzXnwYq3M2CDhfFuq%2FLn0%2FQU0QVIqLZx%2BUwU98dAC4569q8BRa%2Fi24c0n09dVabcSIOg4P81zA6gej%2B68Y0QUN%2F35ACgXGvgyw0hcPu66co4h99eVRqUSAW7IYYPD%2FV5vi1QjeUVbap8i5x9Q3z2bTBwVmufCEcU1YEz0yR%2BjwjZR7uXs%2FDuEeuP0BQHcbc7cLRAj8OTniLi1y30GXoKYJheDCLmpucJd%2FF%2B2J84W2B9brqtRLnoB1%2Fp3LByulNdSOaMcQeTkzLR1i6%2BVStvs%2BmQhynC%2FWIoXpKyYb9s2u7F6rg%2BcekEGxQvYGeQuoui8Mukil9YK9isJf6Q5l2DShNDfMMNWEzjqs93FleV5w7Bo24v2RiAYVjej4gx3A6%2BZey6AgUMbwHv0CJMqcRzosFB3cnbhMAwNuZS6EDPtcQysebFe9PKkNHidG7mcn%2FpusWBJcAuvNEtTP9ggg7vBgizZK0k67tViNXfZZOVL87hZxJEXPLUWwIl%2FGN5bUIwSzwEgOnZxDc8UyNgoa6m2gOqIUp5Z%2BaNWJn8l1UnuYvpfQ3Y7ZLEuZ2AMn5r2VYt6MFe0GMIrr7LwGOqUBs1BXVviZbR7cO3XxSWUem1vM1ORdKCnpopPJgWRLL7ZzhEQYBZ7hXLk8ouZWs5ZAYzhmL%2BDKzzab9XnE%2Fuww0J%2BoPHunWDK2OGEPsiWH6Pl5WuPBWwCr9h1MLm4Z%2BwJqLrxuQ59Fo96%2FtlyftOfAZ9Zhv5LayA%2BLD%2BsG8X4CGqie9DXmJTNhDuTUOsHpGhUN%2BzQg9aEGI6F8UQdjMXjGtwRWJdYm&X-Amz-Signature=54e8e5f250079529892e9ce1c35ffe0439516b9e538ec9f52efa8fbfab9504a1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PNV2GZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPNdsZVU%2Fnf8ool2EdtqSic50WsQQ838wIkiQseu%2FHUgIgIm1kRWQRzVhYAWHE72fYiN1o1h%2BUnwM4Pi2GDeEnOm8qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFI9EWF53ZLDGXyRFyrcA7R42cp5JuDDgZyr6nfn8g29JNUh4oZIqvuzVgzey6PlNOtcM5MyLdUzXnwYq3M2CDhfFuq%2FLn0%2FQU0QVIqLZx%2BUwU98dAC4569q8BRa%2Fi24c0n09dVabcSIOg4P81zA6gej%2B68Y0QUN%2F35ACgXGvgyw0hcPu66co4h99eVRqUSAW7IYYPD%2FV5vi1QjeUVbap8i5x9Q3z2bTBwVmufCEcU1YEz0yR%2BjwjZR7uXs%2FDuEeuP0BQHcbc7cLRAj8OTniLi1y30GXoKYJheDCLmpucJd%2FF%2B2J84W2B9brqtRLnoB1%2Fp3LByulNdSOaMcQeTkzLR1i6%2BVStvs%2BmQhynC%2FWIoXpKyYb9s2u7F6rg%2BcekEGxQvYGeQuoui8Mukil9YK9isJf6Q5l2DShNDfMMNWEzjqs93FleV5w7Bo24v2RiAYVjej4gx3A6%2BZey6AgUMbwHv0CJMqcRzosFB3cnbhMAwNuZS6EDPtcQysebFe9PKkNHidG7mcn%2FpusWBJcAuvNEtTP9ggg7vBgizZK0k67tViNXfZZOVL87hZxJEXPLUWwIl%2FGN5bUIwSzwEgOnZxDc8UyNgoa6m2gOqIUp5Z%2BaNWJn8l1UnuYvpfQ3Y7ZLEuZ2AMn5r2VYt6MFe0GMIrr7LwGOqUBs1BXVviZbR7cO3XxSWUem1vM1ORdKCnpopPJgWRLL7ZzhEQYBZ7hXLk8ouZWs5ZAYzhmL%2BDKzzab9XnE%2Fuww0J%2BoPHunWDK2OGEPsiWH6Pl5WuPBWwCr9h1MLm4Z%2BwJqLrxuQ59Fo96%2FtlyftOfAZ9Zhv5LayA%2BLD%2BsG8X4CGqie9DXmJTNhDuTUOsHpGhUN%2BzQg9aEGI6F8UQdjMXjGtwRWJdYm&X-Amz-Signature=7011f33f59f94c0a1178fdd1b9f83b578b4bdbcd988affea33e7a939e58d0477&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PNV2GZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPNdsZVU%2Fnf8ool2EdtqSic50WsQQ838wIkiQseu%2FHUgIgIm1kRWQRzVhYAWHE72fYiN1o1h%2BUnwM4Pi2GDeEnOm8qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFI9EWF53ZLDGXyRFyrcA7R42cp5JuDDgZyr6nfn8g29JNUh4oZIqvuzVgzey6PlNOtcM5MyLdUzXnwYq3M2CDhfFuq%2FLn0%2FQU0QVIqLZx%2BUwU98dAC4569q8BRa%2Fi24c0n09dVabcSIOg4P81zA6gej%2B68Y0QUN%2F35ACgXGvgyw0hcPu66co4h99eVRqUSAW7IYYPD%2FV5vi1QjeUVbap8i5x9Q3z2bTBwVmufCEcU1YEz0yR%2BjwjZR7uXs%2FDuEeuP0BQHcbc7cLRAj8OTniLi1y30GXoKYJheDCLmpucJd%2FF%2B2J84W2B9brqtRLnoB1%2Fp3LByulNdSOaMcQeTkzLR1i6%2BVStvs%2BmQhynC%2FWIoXpKyYb9s2u7F6rg%2BcekEGxQvYGeQuoui8Mukil9YK9isJf6Q5l2DShNDfMMNWEzjqs93FleV5w7Bo24v2RiAYVjej4gx3A6%2BZey6AgUMbwHv0CJMqcRzosFB3cnbhMAwNuZS6EDPtcQysebFe9PKkNHidG7mcn%2FpusWBJcAuvNEtTP9ggg7vBgizZK0k67tViNXfZZOVL87hZxJEXPLUWwIl%2FGN5bUIwSzwEgOnZxDc8UyNgoa6m2gOqIUp5Z%2BaNWJn8l1UnuYvpfQ3Y7ZLEuZ2AMn5r2VYt6MFe0GMIrr7LwGOqUBs1BXVviZbR7cO3XxSWUem1vM1ORdKCnpopPJgWRLL7ZzhEQYBZ7hXLk8ouZWs5ZAYzhmL%2BDKzzab9XnE%2Fuww0J%2BoPHunWDK2OGEPsiWH6Pl5WuPBWwCr9h1MLm4Z%2BwJqLrxuQ59Fo96%2FtlyftOfAZ9Zhv5LayA%2BLD%2BsG8X4CGqie9DXmJTNhDuTUOsHpGhUN%2BzQg9aEGI6F8UQdjMXjGtwRWJdYm&X-Amz-Signature=1df12e9165178926365c074c1c9ca65740ffd0e91d488e14d0407bbb3103cf30&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQDKFZGQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCkPUXbvtXocOHBRuevot%2Bl0x60mQmg4pPCCT0JxgN%2FnQIgLsjG5ZFaGPLdiR11raRUWeUlDWiD6%2B5QaHFF2qHmAYAqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQBoaHYveHDRssVrSrcA72y5yf2TiCJD4sBgZvOfBXgeVSYfLVos2Zc8jNU4R70uOXW4cZcoR%2Fik9Jn4RZecAvhLp%2FxCYCzmuW6PH39%2B9s%2FbYlepIebtn7pCBUFQiYu2978ozMmqg6voj6X40GIl8zw6GkkaeTt8p%2F48kGyk4bdoV5p%2BfugTPaLLlRSsA5MGZQ6bSCZIrshoHA1Umvo69aDTkQ%2BqiBZchiy8Mw9pRNDfH21eWsHxjwJxo1k3ul0l50L2tE%2B5DwhNpPyn%2B1O5vY3ClhM2hpssRpyuaucgPLMlmaKoRwmC3138aWq48u%2BqZgiZJnVXxo4%2FW%2Ftq49WM6iSW5DcJbqsS0yZlH9PSSmPdh%2FWfglLpi7ctCR9gH0PItpEOdTYXvaywJKe27kYmLYIecB1R1JW9xbC6HX5jAFZGxO1orHMXRi44sLEEIIT5pVFPv7DSBSrQVIgGKEJNcu%2B3VzttbZuMVIdOwe4p9ZEczS21HCFovIP6hMSwbiiuzmiYUo7Wn3FLh7PCa4uwHo6p3yDxEZKxBJjTf%2FD9vVLZjBaSNP6zd5BvQRWmCVV8xLKMOoU8OB2tcmL4GKv764EbQuHng%2FpxYkK9jMC9cozWhgF1pwlX0GzEaKxiy7QZkOwadyIchyW%2BYLFMIrr7LwGOqUBQPHftiNXrpKciCwUeoeKhxs5IuF288OBiXA1EX5P7S%2BJUeSKuK1I8A6vCf7knreBbkEyhx8OqR5C%2B5DdIakN3x0bmapJDpWl2mLTvgL1iFnXsw5sAOUHL5lIIvFmHTMS45cxGMz6NlVqUP4HRQWfuZf40rd6izQX2fj89AZ33yzFDLnM18%2BN2cCc%2BGllDIY%2B%2FJMdz%2B8HinD%2FIqvJgMWg7n%2Fev29k&X-Amz-Signature=836c030ee0da08cdad44e7f7a05eece6f3385b19bef4b4d3db4b2b6b6d11670a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQDKFZGQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCkPUXbvtXocOHBRuevot%2Bl0x60mQmg4pPCCT0JxgN%2FnQIgLsjG5ZFaGPLdiR11raRUWeUlDWiD6%2B5QaHFF2qHmAYAqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMQBoaHYveHDRssVrSrcA72y5yf2TiCJD4sBgZvOfBXgeVSYfLVos2Zc8jNU4R70uOXW4cZcoR%2Fik9Jn4RZecAvhLp%2FxCYCzmuW6PH39%2B9s%2FbYlepIebtn7pCBUFQiYu2978ozMmqg6voj6X40GIl8zw6GkkaeTt8p%2F48kGyk4bdoV5p%2BfugTPaLLlRSsA5MGZQ6bSCZIrshoHA1Umvo69aDTkQ%2BqiBZchiy8Mw9pRNDfH21eWsHxjwJxo1k3ul0l50L2tE%2B5DwhNpPyn%2B1O5vY3ClhM2hpssRpyuaucgPLMlmaKoRwmC3138aWq48u%2BqZgiZJnVXxo4%2FW%2Ftq49WM6iSW5DcJbqsS0yZlH9PSSmPdh%2FWfglLpi7ctCR9gH0PItpEOdTYXvaywJKe27kYmLYIecB1R1JW9xbC6HX5jAFZGxO1orHMXRi44sLEEIIT5pVFPv7DSBSrQVIgGKEJNcu%2B3VzttbZuMVIdOwe4p9ZEczS21HCFovIP6hMSwbiiuzmiYUo7Wn3FLh7PCa4uwHo6p3yDxEZKxBJjTf%2FD9vVLZjBaSNP6zd5BvQRWmCVV8xLKMOoU8OB2tcmL4GKv764EbQuHng%2FpxYkK9jMC9cozWhgF1pwlX0GzEaKxiy7QZkOwadyIchyW%2BYLFMIrr7LwGOqUBQPHftiNXrpKciCwUeoeKhxs5IuF288OBiXA1EX5P7S%2BJUeSKuK1I8A6vCf7knreBbkEyhx8OqR5C%2B5DdIakN3x0bmapJDpWl2mLTvgL1iFnXsw5sAOUHL5lIIvFmHTMS45cxGMz6NlVqUP4HRQWfuZf40rd6izQX2fj89AZ33yzFDLnM18%2BN2cCc%2BGllDIY%2B%2FJMdz%2B8HinD%2FIqvJgMWg7n%2Fev29k&X-Amz-Signature=695301ffbea9656d401c829da34a9e54870c16a38b5cd501af22baa5262e6f80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665PNV2GZX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPNdsZVU%2Fnf8ool2EdtqSic50WsQQ838wIkiQseu%2FHUgIgIm1kRWQRzVhYAWHE72fYiN1o1h%2BUnwM4Pi2GDeEnOm8qiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFI9EWF53ZLDGXyRFyrcA7R42cp5JuDDgZyr6nfn8g29JNUh4oZIqvuzVgzey6PlNOtcM5MyLdUzXnwYq3M2CDhfFuq%2FLn0%2FQU0QVIqLZx%2BUwU98dAC4569q8BRa%2Fi24c0n09dVabcSIOg4P81zA6gej%2B68Y0QUN%2F35ACgXGvgyw0hcPu66co4h99eVRqUSAW7IYYPD%2FV5vi1QjeUVbap8i5x9Q3z2bTBwVmufCEcU1YEz0yR%2BjwjZR7uXs%2FDuEeuP0BQHcbc7cLRAj8OTniLi1y30GXoKYJheDCLmpucJd%2FF%2B2J84W2B9brqtRLnoB1%2Fp3LByulNdSOaMcQeTkzLR1i6%2BVStvs%2BmQhynC%2FWIoXpKyYb9s2u7F6rg%2BcekEGxQvYGeQuoui8Mukil9YK9isJf6Q5l2DShNDfMMNWEzjqs93FleV5w7Bo24v2RiAYVjej4gx3A6%2BZey6AgUMbwHv0CJMqcRzosFB3cnbhMAwNuZS6EDPtcQysebFe9PKkNHidG7mcn%2FpusWBJcAuvNEtTP9ggg7vBgizZK0k67tViNXfZZOVL87hZxJEXPLUWwIl%2FGN5bUIwSzwEgOnZxDc8UyNgoa6m2gOqIUp5Z%2BaNWJn8l1UnuYvpfQ3Y7ZLEuZ2AMn5r2VYt6MFe0GMIrr7LwGOqUBs1BXVviZbR7cO3XxSWUem1vM1ORdKCnpopPJgWRLL7ZzhEQYBZ7hXLk8ouZWs5ZAYzhmL%2BDKzzab9XnE%2Fuww0J%2BoPHunWDK2OGEPsiWH6Pl5WuPBWwCr9h1MLm4Z%2BwJqLrxuQ59Fo96%2FtlyftOfAZ9Zhv5LayA%2BLD%2BsG8X4CGqie9DXmJTNhDuTUOsHpGhUN%2BzQg9aEGI6F8UQdjMXjGtwRWJdYm&X-Amz-Signature=f050380b7e538b126a8523d2637a96b0078f9ef2bd7a5422b1476cde47b14391&X-Amz-SignedHeaders=host&x-id=GetObject)
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