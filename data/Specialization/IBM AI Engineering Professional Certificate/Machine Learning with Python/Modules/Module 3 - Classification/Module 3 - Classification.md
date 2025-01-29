

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LPMOXQF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3d8B0W%2FkyxWG4Itgls8G2J1BPYQ1i1nNV4QyX7dbtOAIhAIFD3o6ZUlP4hKix7Ljwbr4YCENG0Bo5iBF%2FKqOBIVVSKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy0F1CVNRNicIurc18q3AP7C6bxuPWmMF8HgSuoam9936ynZ4XkeoEQ3seKdbrB9uq3QXHlL1iPjw5Dfa4E0Ow0mHdZ9N4hZ5V%2BFM6zRSot5pBYEg45UIWmiRseyjt15xTmxs43V%2FiQYr%2FNhBKN1NRm5fw3BzlfcHjag014g1Mq8TbWdGKYC%2F%2FFKJ3IQhSyAKcFzIHymIchqAmlVPBLQBxhar7Q8PNw2222Ah%2Byniku%2Bytl3Spvm08Uvoc2M6bRdWAJNs0f%2B3lM887HBCwQtud3jXEFH92ixtDw7ognjvzYDA4cTD7kCaeoT1zrliKQEzDrNgaiy7Hn4xSNdaRLs5pBpDkuu4Xfi4%2BLbSEQFuZ%2BwOjtzh58W6K1EUWULaIxXLXNPWcSre65Bjsn2708Wz1LnABn7%2FulWGVwHvWz8lvqC47R2Cmu%2FRJvbOvyES83PYjpKJI7TGcQr2YpVjFxnJC2BxFArj3CquX773OcplWkTRi9264pw5xA0L9t3PeEdwx3kVUIb2eh4wG29i8vrmcJIUWsgz8qfg2Fmc3VauNBru8cGjfkfnLMzd5EH5PykPxaRGNakMOwpjrMymiMbtK7SI5mCKKBot5cQXNk48TEe8GQ5TLBRqxoEQixEPW%2BHm5K8hM%2FUqd7PZ%2FBrjDh5ui8BjqkAVVo%2BrBm4DH%2FZ4ooN4HOp833CBgZQzHMLMJctYFvxaUlHJIHeb1JUS%2Fs0NNAiuaKQEQd7cMCxhUvZovHhp4FWj%2BgTopeHAJqQn5wR3G9adyfDHH4IhEu2zCTPvcAbvNcP0G%2B%2FD6HfZku2RiXQVWj4sW59el%2BS6EMcIEWXQ6DFS2ntAKRk4bmpuyphGFqJwP0HWc5lHItzh9ZfFQWDYaFw6tp2LWH&X-Amz-Signature=d2bd6c7a26b98f67fd14e14cd217ed1fce3a3be5cb1ca86b5987ee763da468b4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LPMOXQF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3d8B0W%2FkyxWG4Itgls8G2J1BPYQ1i1nNV4QyX7dbtOAIhAIFD3o6ZUlP4hKix7Ljwbr4YCENG0Bo5iBF%2FKqOBIVVSKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy0F1CVNRNicIurc18q3AP7C6bxuPWmMF8HgSuoam9936ynZ4XkeoEQ3seKdbrB9uq3QXHlL1iPjw5Dfa4E0Ow0mHdZ9N4hZ5V%2BFM6zRSot5pBYEg45UIWmiRseyjt15xTmxs43V%2FiQYr%2FNhBKN1NRm5fw3BzlfcHjag014g1Mq8TbWdGKYC%2F%2FFKJ3IQhSyAKcFzIHymIchqAmlVPBLQBxhar7Q8PNw2222Ah%2Byniku%2Bytl3Spvm08Uvoc2M6bRdWAJNs0f%2B3lM887HBCwQtud3jXEFH92ixtDw7ognjvzYDA4cTD7kCaeoT1zrliKQEzDrNgaiy7Hn4xSNdaRLs5pBpDkuu4Xfi4%2BLbSEQFuZ%2BwOjtzh58W6K1EUWULaIxXLXNPWcSre65Bjsn2708Wz1LnABn7%2FulWGVwHvWz8lvqC47R2Cmu%2FRJvbOvyES83PYjpKJI7TGcQr2YpVjFxnJC2BxFArj3CquX773OcplWkTRi9264pw5xA0L9t3PeEdwx3kVUIb2eh4wG29i8vrmcJIUWsgz8qfg2Fmc3VauNBru8cGjfkfnLMzd5EH5PykPxaRGNakMOwpjrMymiMbtK7SI5mCKKBot5cQXNk48TEe8GQ5TLBRqxoEQixEPW%2BHm5K8hM%2FUqd7PZ%2FBrjDh5ui8BjqkAVVo%2BrBm4DH%2FZ4ooN4HOp833CBgZQzHMLMJctYFvxaUlHJIHeb1JUS%2Fs0NNAiuaKQEQd7cMCxhUvZovHhp4FWj%2BgTopeHAJqQn5wR3G9adyfDHH4IhEu2zCTPvcAbvNcP0G%2B%2FD6HfZku2RiXQVWj4sW59el%2BS6EMcIEWXQ6DFS2ntAKRk4bmpuyphGFqJwP0HWc5lHItzh9ZfFQWDYaFw6tp2LWH&X-Amz-Signature=bae56c5ed4182775548eeb40c24ef1ce3b1f4b2bd018b52d967b1bcb752d286a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LPMOXQF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3d8B0W%2FkyxWG4Itgls8G2J1BPYQ1i1nNV4QyX7dbtOAIhAIFD3o6ZUlP4hKix7Ljwbr4YCENG0Bo5iBF%2FKqOBIVVSKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy0F1CVNRNicIurc18q3AP7C6bxuPWmMF8HgSuoam9936ynZ4XkeoEQ3seKdbrB9uq3QXHlL1iPjw5Dfa4E0Ow0mHdZ9N4hZ5V%2BFM6zRSot5pBYEg45UIWmiRseyjt15xTmxs43V%2FiQYr%2FNhBKN1NRm5fw3BzlfcHjag014g1Mq8TbWdGKYC%2F%2FFKJ3IQhSyAKcFzIHymIchqAmlVPBLQBxhar7Q8PNw2222Ah%2Byniku%2Bytl3Spvm08Uvoc2M6bRdWAJNs0f%2B3lM887HBCwQtud3jXEFH92ixtDw7ognjvzYDA4cTD7kCaeoT1zrliKQEzDrNgaiy7Hn4xSNdaRLs5pBpDkuu4Xfi4%2BLbSEQFuZ%2BwOjtzh58W6K1EUWULaIxXLXNPWcSre65Bjsn2708Wz1LnABn7%2FulWGVwHvWz8lvqC47R2Cmu%2FRJvbOvyES83PYjpKJI7TGcQr2YpVjFxnJC2BxFArj3CquX773OcplWkTRi9264pw5xA0L9t3PeEdwx3kVUIb2eh4wG29i8vrmcJIUWsgz8qfg2Fmc3VauNBru8cGjfkfnLMzd5EH5PykPxaRGNakMOwpjrMymiMbtK7SI5mCKKBot5cQXNk48TEe8GQ5TLBRqxoEQixEPW%2BHm5K8hM%2FUqd7PZ%2FBrjDh5ui8BjqkAVVo%2BrBm4DH%2FZ4ooN4HOp833CBgZQzHMLMJctYFvxaUlHJIHeb1JUS%2Fs0NNAiuaKQEQd7cMCxhUvZovHhp4FWj%2BgTopeHAJqQn5wR3G9adyfDHH4IhEu2zCTPvcAbvNcP0G%2B%2FD6HfZku2RiXQVWj4sW59el%2BS6EMcIEWXQ6DFS2ntAKRk4bmpuyphGFqJwP0HWc5lHItzh9ZfFQWDYaFw6tp2LWH&X-Amz-Signature=b425aacdffc9e5417c72f7be8763261247fc22a6e2a5d2ad71a64514fea6f58a&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632B5LPFP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPFbyoYV%2BsG2uLB95qGptpc4Lkp028cDQ%2FPFd4ppPNzQIgQhz6DEgPFONQhIjDDSBFbdATYioESrh%2B7D5QHbsV%2Fv8qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVoKbIwP2xBL2hmbCrcA7PHEKz%2F6JDfOqU3NKX4ZnEuiaF5uLsgGVLtlUSOwnJV5HS2mrki7nveA05sciq78Z2CqMeuvHKjY9ICiPopHEG7WcKMqqfxrBnZkyDaVFFxbG%2BfG2wWi9JOF60sPlssRfydKy%2FRXT7Ap84dnEFgNGhRSp6uK78Y2j04QSfSlULsQTdf%2F86jZ6jU9Rx%2BJ9QwPrkJu6LcZA6YJbuEe2%2B1mVHUpUK7Y%2BpLxdEzfmEntBj%2BfZDT2THDICl3xNeJBgZQwEg6oy0d6UFJvCtXGpcrJSSGrDdSieyxNiDCGwMjmznHJjOMM7a2j4SQnLKTVVk0IZuexwZQoW8%2B9eRubGUqm9JWVf5o40qi3WzBMvDWkoVxz%2FUUCOBtl%2Frvd%2FXm9IFHPHm4cF5HfW604IIWQ29u27iWiA8%2Fz3EZ15fEjHWIIMKq7S5O%2FjIySsNfYFURS6UBEI0vIL%2Fc6PhgmCfBUAUsXk5%2FwsheZY13smwCVfdY22S9rrZlhxHkjmx5%2BDle4K2uDJKNUZTNK8bYAvreHiOBs7ap8NCtEVrj00WkTANP7SdLGLtnhD2i0T9wO8tHRxT%2FCiECxLi5tc8ue1DcQUY0vnD%2FPQfXrQ0GV1IiZ0a2YY%2BSQa%2FNu0Geni5uKbfIMPXm6LwGOqUBYQZM35xu9LQ28BLR3p0GtjltBhm4R%2BLY5W4wNFwVc3MsL%2Bes6Y6nYJ%2BSPJAwbskvwP9w0QFuq6RUiDf9MuWgMoNRKDuCXQWlGmkMuJVf2EYi5hKJnZGvryRZ4hGm8wtomZP7fCztXjlaqNlT2MzsmQMnVZyYoYm0jSdIfM4JeGbUZ9a7R7opDRR51Oa3ozm2QG6NAhA8%2Ftr5%2FGsZVBkAJ2emykjW&X-Amz-Signature=fd9e4e176e2118b5c24067937214cc57f9609aab05e62b2f04acb195d9859f1b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632B5LPFP%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPFbyoYV%2BsG2uLB95qGptpc4Lkp028cDQ%2FPFd4ppPNzQIgQhz6DEgPFONQhIjDDSBFbdATYioESrh%2B7D5QHbsV%2Fv8qiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVoKbIwP2xBL2hmbCrcA7PHEKz%2F6JDfOqU3NKX4ZnEuiaF5uLsgGVLtlUSOwnJV5HS2mrki7nveA05sciq78Z2CqMeuvHKjY9ICiPopHEG7WcKMqqfxrBnZkyDaVFFxbG%2BfG2wWi9JOF60sPlssRfydKy%2FRXT7Ap84dnEFgNGhRSp6uK78Y2j04QSfSlULsQTdf%2F86jZ6jU9Rx%2BJ9QwPrkJu6LcZA6YJbuEe2%2B1mVHUpUK7Y%2BpLxdEzfmEntBj%2BfZDT2THDICl3xNeJBgZQwEg6oy0d6UFJvCtXGpcrJSSGrDdSieyxNiDCGwMjmznHJjOMM7a2j4SQnLKTVVk0IZuexwZQoW8%2B9eRubGUqm9JWVf5o40qi3WzBMvDWkoVxz%2FUUCOBtl%2Frvd%2FXm9IFHPHm4cF5HfW604IIWQ29u27iWiA8%2Fz3EZ15fEjHWIIMKq7S5O%2FjIySsNfYFURS6UBEI0vIL%2Fc6PhgmCfBUAUsXk5%2FwsheZY13smwCVfdY22S9rrZlhxHkjmx5%2BDle4K2uDJKNUZTNK8bYAvreHiOBs7ap8NCtEVrj00WkTANP7SdLGLtnhD2i0T9wO8tHRxT%2FCiECxLi5tc8ue1DcQUY0vnD%2FPQfXrQ0GV1IiZ0a2YY%2BSQa%2FNu0Geni5uKbfIMPXm6LwGOqUBYQZM35xu9LQ28BLR3p0GtjltBhm4R%2BLY5W4wNFwVc3MsL%2Bes6Y6nYJ%2BSPJAwbskvwP9w0QFuq6RUiDf9MuWgMoNRKDuCXQWlGmkMuJVf2EYi5hKJnZGvryRZ4hGm8wtomZP7fCztXjlaqNlT2MzsmQMnVZyYoYm0jSdIfM4JeGbUZ9a7R7opDRR51Oa3ozm2QG6NAhA8%2Ftr5%2FGsZVBkAJ2emykjW&X-Amz-Signature=f25b08e57f368660e4ac79151ab1647f8c5de8320aa97c044a55f28446aab632&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LPMOXQF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3d8B0W%2FkyxWG4Itgls8G2J1BPYQ1i1nNV4QyX7dbtOAIhAIFD3o6ZUlP4hKix7Ljwbr4YCENG0Bo5iBF%2FKqOBIVVSKogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy0F1CVNRNicIurc18q3AP7C6bxuPWmMF8HgSuoam9936ynZ4XkeoEQ3seKdbrB9uq3QXHlL1iPjw5Dfa4E0Ow0mHdZ9N4hZ5V%2BFM6zRSot5pBYEg45UIWmiRseyjt15xTmxs43V%2FiQYr%2FNhBKN1NRm5fw3BzlfcHjag014g1Mq8TbWdGKYC%2F%2FFKJ3IQhSyAKcFzIHymIchqAmlVPBLQBxhar7Q8PNw2222Ah%2Byniku%2Bytl3Spvm08Uvoc2M6bRdWAJNs0f%2B3lM887HBCwQtud3jXEFH92ixtDw7ognjvzYDA4cTD7kCaeoT1zrliKQEzDrNgaiy7Hn4xSNdaRLs5pBpDkuu4Xfi4%2BLbSEQFuZ%2BwOjtzh58W6K1EUWULaIxXLXNPWcSre65Bjsn2708Wz1LnABn7%2FulWGVwHvWz8lvqC47R2Cmu%2FRJvbOvyES83PYjpKJI7TGcQr2YpVjFxnJC2BxFArj3CquX773OcplWkTRi9264pw5xA0L9t3PeEdwx3kVUIb2eh4wG29i8vrmcJIUWsgz8qfg2Fmc3VauNBru8cGjfkfnLMzd5EH5PykPxaRGNakMOwpjrMymiMbtK7SI5mCKKBot5cQXNk48TEe8GQ5TLBRqxoEQixEPW%2BHm5K8hM%2FUqd7PZ%2FBrjDh5ui8BjqkAVVo%2BrBm4DH%2FZ4ooN4HOp833CBgZQzHMLMJctYFvxaUlHJIHeb1JUS%2Fs0NNAiuaKQEQd7cMCxhUvZovHhp4FWj%2BgTopeHAJqQn5wR3G9adyfDHH4IhEu2zCTPvcAbvNcP0G%2B%2FD6HfZku2RiXQVWj4sW59el%2BS6EMcIEWXQ6DFS2ntAKRk4bmpuyphGFqJwP0HWc5lHItzh9ZfFQWDYaFw6tp2LWH&X-Amz-Signature=d8d6d5d8cc21e4e7ec233a4e133599213c06d2fdea67164f47be8ff862b79793&X-Amz-SignedHeaders=host&x-id=GetObject)
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