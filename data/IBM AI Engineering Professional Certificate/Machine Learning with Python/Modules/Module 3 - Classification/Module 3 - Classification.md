

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XRAFEGD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2BhWTaHVdCd4gzHIHpeQdJ6uwYddCAbGUCtflz%2FrI8MAiANXUnDk0IqDLNmlilE9uZJnJhSFe2%2BzsCOCQLv3aKdECqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEXpNUf%2FPAD5CzKn4KtwDTrSDn8mBg5s3qN5JOTsNb3aeeth8b6gRjLd%2FeiFCpdnxxFECfo58hkrmdVwmsBYCr9wWcMs2LpUbqFIGTuskDdXWNOhNZAGmdA%2BLCTSn9J6x33oDJugo%2F87GngrGK3Ng8bmliNyNkQdnOrHH3krymhEjOzY%2FoIEpx5Xmyyt0YMdzI3oPPzMO61q%2FT%2F%2FTFoaekk%2FfVRfwF0ZAMJJHFhkGHg7JnmljjUghtQrYpQT2kC1Xja9%2FGocSCy8XMFeORLm%2BvZhPZhtCQ6W7sYqA1a%2BKO5GI1DGl5oEbS%2BPjifeU3NwTArR9JdsMCd7F54qXLR3m2syFrLE7xP87R8QC1qKa7CWx%2FyeBeb%2FZ5Tp8iYO9TzdryNWT3UHmKbrKbtfQtUG7Lv6N9pe%2BQjtGYCAgyFih57t%2FxTpzrD7kbk10zvPCiMx8eipvqL%2BULadu8n2yRA4Fd4%2B62bgnCRF76%2F0UgzZFYLBovFtFQbhrkx8yGuf1%2BeKPU8UIbvsACy4ue8IFy8W4r42n8ikqRSTtsHYByqgambAtcMMZS0P9EY78DZqq4ebnNnf2GpQk5E%2BeR91w8BLEG14F%2BMBfqZa7VkbIwml6YVGZsKwxFfKfyg7wR4945rsgYQcYclpqC6TY2wQwjsz3vAY6pgEbxXaYcVjmKVHzmxK6oUkzIq%2BlP2%2FtZV0pVtAGG3iHM2Dk19Zlqf%2BxqkeqIatL9p5mHVeC%2FCdn5taId15lb%2FJYOFoMXUvM74gTYIiamMZrfzSaWUnCtuOJkRYz1ntt4%2FNxyIa9p2phZ5ukAH%2BKfiHabVXKuR3USqoivhOpcMQB%2BzVckgvsHH%2FJUEGh0wC7bm%2F%2BW7w3J93pZfriehHISXYEZbCI1T47&X-Amz-Signature=d6b17a7b14f132f263674dcbc9f86965415eb618bbd5799c96ecc243278e52dd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XRAFEGD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2BhWTaHVdCd4gzHIHpeQdJ6uwYddCAbGUCtflz%2FrI8MAiANXUnDk0IqDLNmlilE9uZJnJhSFe2%2BzsCOCQLv3aKdECqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEXpNUf%2FPAD5CzKn4KtwDTrSDn8mBg5s3qN5JOTsNb3aeeth8b6gRjLd%2FeiFCpdnxxFECfo58hkrmdVwmsBYCr9wWcMs2LpUbqFIGTuskDdXWNOhNZAGmdA%2BLCTSn9J6x33oDJugo%2F87GngrGK3Ng8bmliNyNkQdnOrHH3krymhEjOzY%2FoIEpx5Xmyyt0YMdzI3oPPzMO61q%2FT%2F%2FTFoaekk%2FfVRfwF0ZAMJJHFhkGHg7JnmljjUghtQrYpQT2kC1Xja9%2FGocSCy8XMFeORLm%2BvZhPZhtCQ6W7sYqA1a%2BKO5GI1DGl5oEbS%2BPjifeU3NwTArR9JdsMCd7F54qXLR3m2syFrLE7xP87R8QC1qKa7CWx%2FyeBeb%2FZ5Tp8iYO9TzdryNWT3UHmKbrKbtfQtUG7Lv6N9pe%2BQjtGYCAgyFih57t%2FxTpzrD7kbk10zvPCiMx8eipvqL%2BULadu8n2yRA4Fd4%2B62bgnCRF76%2F0UgzZFYLBovFtFQbhrkx8yGuf1%2BeKPU8UIbvsACy4ue8IFy8W4r42n8ikqRSTtsHYByqgambAtcMMZS0P9EY78DZqq4ebnNnf2GpQk5E%2BeR91w8BLEG14F%2BMBfqZa7VkbIwml6YVGZsKwxFfKfyg7wR4945rsgYQcYclpqC6TY2wQwjsz3vAY6pgEbxXaYcVjmKVHzmxK6oUkzIq%2BlP2%2FtZV0pVtAGG3iHM2Dk19Zlqf%2BxqkeqIatL9p5mHVeC%2FCdn5taId15lb%2FJYOFoMXUvM74gTYIiamMZrfzSaWUnCtuOJkRYz1ntt4%2FNxyIa9p2phZ5ukAH%2BKfiHabVXKuR3USqoivhOpcMQB%2BzVckgvsHH%2FJUEGh0wC7bm%2F%2BW7w3J93pZfriehHISXYEZbCI1T47&X-Amz-Signature=774bd3e3b4d5903c64b06e9a1d74d784b0786376e2d787727ca5b1f1ec04be20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XRAFEGD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2BhWTaHVdCd4gzHIHpeQdJ6uwYddCAbGUCtflz%2FrI8MAiANXUnDk0IqDLNmlilE9uZJnJhSFe2%2BzsCOCQLv3aKdECqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEXpNUf%2FPAD5CzKn4KtwDTrSDn8mBg5s3qN5JOTsNb3aeeth8b6gRjLd%2FeiFCpdnxxFECfo58hkrmdVwmsBYCr9wWcMs2LpUbqFIGTuskDdXWNOhNZAGmdA%2BLCTSn9J6x33oDJugo%2F87GngrGK3Ng8bmliNyNkQdnOrHH3krymhEjOzY%2FoIEpx5Xmyyt0YMdzI3oPPzMO61q%2FT%2F%2FTFoaekk%2FfVRfwF0ZAMJJHFhkGHg7JnmljjUghtQrYpQT2kC1Xja9%2FGocSCy8XMFeORLm%2BvZhPZhtCQ6W7sYqA1a%2BKO5GI1DGl5oEbS%2BPjifeU3NwTArR9JdsMCd7F54qXLR3m2syFrLE7xP87R8QC1qKa7CWx%2FyeBeb%2FZ5Tp8iYO9TzdryNWT3UHmKbrKbtfQtUG7Lv6N9pe%2BQjtGYCAgyFih57t%2FxTpzrD7kbk10zvPCiMx8eipvqL%2BULadu8n2yRA4Fd4%2B62bgnCRF76%2F0UgzZFYLBovFtFQbhrkx8yGuf1%2BeKPU8UIbvsACy4ue8IFy8W4r42n8ikqRSTtsHYByqgambAtcMMZS0P9EY78DZqq4ebnNnf2GpQk5E%2BeR91w8BLEG14F%2BMBfqZa7VkbIwml6YVGZsKwxFfKfyg7wR4945rsgYQcYclpqC6TY2wQwjsz3vAY6pgEbxXaYcVjmKVHzmxK6oUkzIq%2BlP2%2FtZV0pVtAGG3iHM2Dk19Zlqf%2BxqkeqIatL9p5mHVeC%2FCdn5taId15lb%2FJYOFoMXUvM74gTYIiamMZrfzSaWUnCtuOJkRYz1ntt4%2FNxyIa9p2phZ5ukAH%2BKfiHabVXKuR3USqoivhOpcMQB%2BzVckgvsHH%2FJUEGh0wC7bm%2F%2BW7w3J93pZfriehHISXYEZbCI1T47&X-Amz-Signature=c03de962d1b5de5707a991e2e154dda845e9a24c3c06394f9949d6036e5dda47&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUX3JRSH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8LF19lH%2F2b15v6xk1IsoCaRSdM%2BIJ1wlPChy4nV7bzQIgaZEsPF0HtRxqgbT2Sxx9lkJEB5iZSlkFyzExHtbA%2BjoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKJaX5YR5BRW2o2q6ircA9R%2B22qZ6Y91oOF3%2FN646OfeHs3nCmG5d%2FnVtZmDAIxdblz0IVZjZazvNKHxOKz782cGshSArQHNBkJTzeE4a6evgEuoRzPksU1jOQTbz1sgllvHge6KXpT7qFwEQZ5nd46RmVswK8SbjwSm%2F%2Fu%2FPnouMqzYw2ycbpc36PeJdA%2BuMX6FPQBEFtxzhVzmTPxYZEI4TjwiW%2BLjXF5uM1DAndH5YRkSpP2uj7hikARd6Gmm2chSayToHotdB9Xoxl1eM5u%2FwD0i9qVGrsZfinl12MKNh3YS2UMAbrZu01DuU%2BRPNvdc%2F50oF%2BOt9OyfYupfXGjpUl5gbV3XACNgOQxsdGoDMJ8Ia%2FlIYQCrPrpkKGwIpCPhqyLE3TqYGDfyufKyWCe3yzpbOD2%2FCksXhLUdl3pd%2BJU3IPMI%2BK6cOvU2%2BkvtOp6xwIVDKNzcLiJOYZUJPYEcZOh0JQo1FqdB0GaSBnBDAf%2FMC%2FW%2Fb3iAprIC9flVfyxbYVCFIc0DTECC6BnHQHXAYRxx3W2UXWTqv202FhmrvxvdRBs%2FIY5dSBML4oxAk0n3C8gL%2FAjMB9sVFv1ICvVx2rQM2hHAxIvOESXzMKLqYPQx9gcE%2F%2BNK2qusIHDbmDx3blh1ANsXdwQHMIjI%2BLwGOqUBvAShR2IiOrMY2TgPZg%2F3U8wn9CDTOet1Behs37B9ZGV3Vfx06uFIYxX8qGNCjbeHvJ95VtFI1zKhxCbX1%2BjCWfidqNqxeExH8f9d98SWO%2F346OGM%2F7fgBD2XRwGCchCW9nQtx6LpD7C3ZwDjgojCAPP5kBmk6XqTelSWLtEXu%2BybF67CmSA86LaGhRqAx68uMmFZlXh76rbGyJDhf4pDI108jY2Y&X-Amz-Signature=602ea54de9d81d4fcc105c9f3f947b1ffd76e544a03a14a70c7e9fc17d8ad0e4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUX3JRSH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8LF19lH%2F2b15v6xk1IsoCaRSdM%2BIJ1wlPChy4nV7bzQIgaZEsPF0HtRxqgbT2Sxx9lkJEB5iZSlkFyzExHtbA%2BjoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKJaX5YR5BRW2o2q6ircA9R%2B22qZ6Y91oOF3%2FN646OfeHs3nCmG5d%2FnVtZmDAIxdblz0IVZjZazvNKHxOKz782cGshSArQHNBkJTzeE4a6evgEuoRzPksU1jOQTbz1sgllvHge6KXpT7qFwEQZ5nd46RmVswK8SbjwSm%2F%2Fu%2FPnouMqzYw2ycbpc36PeJdA%2BuMX6FPQBEFtxzhVzmTPxYZEI4TjwiW%2BLjXF5uM1DAndH5YRkSpP2uj7hikARd6Gmm2chSayToHotdB9Xoxl1eM5u%2FwD0i9qVGrsZfinl12MKNh3YS2UMAbrZu01DuU%2BRPNvdc%2F50oF%2BOt9OyfYupfXGjpUl5gbV3XACNgOQxsdGoDMJ8Ia%2FlIYQCrPrpkKGwIpCPhqyLE3TqYGDfyufKyWCe3yzpbOD2%2FCksXhLUdl3pd%2BJU3IPMI%2BK6cOvU2%2BkvtOp6xwIVDKNzcLiJOYZUJPYEcZOh0JQo1FqdB0GaSBnBDAf%2FMC%2FW%2Fb3iAprIC9flVfyxbYVCFIc0DTECC6BnHQHXAYRxx3W2UXWTqv202FhmrvxvdRBs%2FIY5dSBML4oxAk0n3C8gL%2FAjMB9sVFv1ICvVx2rQM2hHAxIvOESXzMKLqYPQx9gcE%2F%2BNK2qusIHDbmDx3blh1ANsXdwQHMIjI%2BLwGOqUBvAShR2IiOrMY2TgPZg%2F3U8wn9CDTOet1Behs37B9ZGV3Vfx06uFIYxX8qGNCjbeHvJ95VtFI1zKhxCbX1%2BjCWfidqNqxeExH8f9d98SWO%2F346OGM%2F7fgBD2XRwGCchCW9nQtx6LpD7C3ZwDjgojCAPP5kBmk6XqTelSWLtEXu%2BybF67CmSA86LaGhRqAx68uMmFZlXh76rbGyJDhf4pDI108jY2Y&X-Amz-Signature=81322dfa76eea3d511f4871211df343cc77a62070282c5d0696b1ac1140c56da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XRAFEGD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T141150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2BhWTaHVdCd4gzHIHpeQdJ6uwYddCAbGUCtflz%2FrI8MAiANXUnDk0IqDLNmlilE9uZJnJhSFe2%2BzsCOCQLv3aKdECqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEXpNUf%2FPAD5CzKn4KtwDTrSDn8mBg5s3qN5JOTsNb3aeeth8b6gRjLd%2FeiFCpdnxxFECfo58hkrmdVwmsBYCr9wWcMs2LpUbqFIGTuskDdXWNOhNZAGmdA%2BLCTSn9J6x33oDJugo%2F87GngrGK3Ng8bmliNyNkQdnOrHH3krymhEjOzY%2FoIEpx5Xmyyt0YMdzI3oPPzMO61q%2FT%2F%2FTFoaekk%2FfVRfwF0ZAMJJHFhkGHg7JnmljjUghtQrYpQT2kC1Xja9%2FGocSCy8XMFeORLm%2BvZhPZhtCQ6W7sYqA1a%2BKO5GI1DGl5oEbS%2BPjifeU3NwTArR9JdsMCd7F54qXLR3m2syFrLE7xP87R8QC1qKa7CWx%2FyeBeb%2FZ5Tp8iYO9TzdryNWT3UHmKbrKbtfQtUG7Lv6N9pe%2BQjtGYCAgyFih57t%2FxTpzrD7kbk10zvPCiMx8eipvqL%2BULadu8n2yRA4Fd4%2B62bgnCRF76%2F0UgzZFYLBovFtFQbhrkx8yGuf1%2BeKPU8UIbvsACy4ue8IFy8W4r42n8ikqRSTtsHYByqgambAtcMMZS0P9EY78DZqq4ebnNnf2GpQk5E%2BeR91w8BLEG14F%2BMBfqZa7VkbIwml6YVGZsKwxFfKfyg7wR4945rsgYQcYclpqC6TY2wQwjsz3vAY6pgEbxXaYcVjmKVHzmxK6oUkzIq%2BlP2%2FtZV0pVtAGG3iHM2Dk19Zlqf%2BxqkeqIatL9p5mHVeC%2FCdn5taId15lb%2FJYOFoMXUvM74gTYIiamMZrfzSaWUnCtuOJkRYz1ntt4%2FNxyIa9p2phZ5ukAH%2BKfiHabVXKuR3USqoivhOpcMQB%2BzVckgvsHH%2FJUEGh0wC7bm%2F%2BW7w3J93pZfriehHISXYEZbCI1T47&X-Amz-Signature=3aaef9d5cc74f0e897dbf727d603b45c331fb1de272d9c440c25b6d130781136&X-Amz-SignedHeaders=host&x-id=GetObject)
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