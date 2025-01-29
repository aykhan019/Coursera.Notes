

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFENFY4M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIH%2FAADxJIJ5%2Fpd86F6EYRKASrvczXsQRDEBDLdmsEvHRAiBaK%2FrevBoTw9n9757Xu90v2qvFm%2Fi3QV%2FN6oBqVzx%2F2CqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUhXeuoDeQIqYONhzKtwDZ0AKSjaby3MMUEymwBI%2FTTOTlwbZmELKVnX4xfxDlcowscZxME1LzL%2FNCUxy0Jim0oeP5UPWLTwUdwx6FQOFVnet92oC%2BAnt3KlmxjpUkSJMfLtOwRVERP8ickG97%2FsZYHEyB166cgsEc%2F4iXAGqdm3OUR%2B%2BTehBf8LOHttHrWj15ZM6a4l%2B3hRbfa%2BOfsgSfAFjvKggOBjg2Nxz%2BdkMkp%2BYvdxDb1Hqc60RXi4on%2Bbi9bcql2P3zF%2FSrAUq6b6qeF%2BNwK2hmiIM92y2x%2BPColh2jp7xCHxaAxcJztXDbR3g9htBvbXf4Checa4dzJrcmLFnaNgm1WSRLVY59tRZREG0j0ZkkQzTStMp%2FJMN8%2F4wIoOrq%2FhnnAyrHnlLvCwg20O4W2itPERPmjn%2FqmHQDW9CV5zgYMeClvv25n8%2FNCNYTIVCrBw9wVxf58ysEPaams%2FLbr4lfxfF9LFFl6Ysvrm9q89Pq6I52iYHKZTl1kwnX6M8nW%2FKiTzQRsFGukUdeRElF3x7F%2B1IUZYVg5lq7LJDJf0Wx9Oj%2B%2B8IvPuwyv9cAoDDAmsfgm%2BfkWKEQJTljpYDkMgNj2C80X2thgbI6XYCZaZAACtB8HyumtX5i2TmKZq1wTXGTTzjU7wwxeflvAY6pgEs6bKDSrG%2BFro8k%2FX%2FH9UGlhbTLh75N%2FJUZhcmxXCxxAmQUX0wVCFGtpHSt1FyjLDRrMgJPjKpRs0WDKHD%2BXAxTqEH2jClVJVFh3LVUGZIyeuhzQNw0At4NOEzsNsH5a%2Bll9GLteY2bXdcFRy5atf1cH8hgmOv3xFNMOOHoaZ01sMIEBqNV88%2Bf7pIJENcKIP76iiR6Xv69ANjLrGd7D6Rsmit%2BcGM&X-Amz-Signature=c8f8e8779688e92227ac10e72d1faff80c8b62997342d48bcc84476cef749e7f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFENFY4M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIH%2FAADxJIJ5%2Fpd86F6EYRKASrvczXsQRDEBDLdmsEvHRAiBaK%2FrevBoTw9n9757Xu90v2qvFm%2Fi3QV%2FN6oBqVzx%2F2CqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUhXeuoDeQIqYONhzKtwDZ0AKSjaby3MMUEymwBI%2FTTOTlwbZmELKVnX4xfxDlcowscZxME1LzL%2FNCUxy0Jim0oeP5UPWLTwUdwx6FQOFVnet92oC%2BAnt3KlmxjpUkSJMfLtOwRVERP8ickG97%2FsZYHEyB166cgsEc%2F4iXAGqdm3OUR%2B%2BTehBf8LOHttHrWj15ZM6a4l%2B3hRbfa%2BOfsgSfAFjvKggOBjg2Nxz%2BdkMkp%2BYvdxDb1Hqc60RXi4on%2Bbi9bcql2P3zF%2FSrAUq6b6qeF%2BNwK2hmiIM92y2x%2BPColh2jp7xCHxaAxcJztXDbR3g9htBvbXf4Checa4dzJrcmLFnaNgm1WSRLVY59tRZREG0j0ZkkQzTStMp%2FJMN8%2F4wIoOrq%2FhnnAyrHnlLvCwg20O4W2itPERPmjn%2FqmHQDW9CV5zgYMeClvv25n8%2FNCNYTIVCrBw9wVxf58ysEPaams%2FLbr4lfxfF9LFFl6Ysvrm9q89Pq6I52iYHKZTl1kwnX6M8nW%2FKiTzQRsFGukUdeRElF3x7F%2B1IUZYVg5lq7LJDJf0Wx9Oj%2B%2B8IvPuwyv9cAoDDAmsfgm%2BfkWKEQJTljpYDkMgNj2C80X2thgbI6XYCZaZAACtB8HyumtX5i2TmKZq1wTXGTTzjU7wwxeflvAY6pgEs6bKDSrG%2BFro8k%2FX%2FH9UGlhbTLh75N%2FJUZhcmxXCxxAmQUX0wVCFGtpHSt1FyjLDRrMgJPjKpRs0WDKHD%2BXAxTqEH2jClVJVFh3LVUGZIyeuhzQNw0At4NOEzsNsH5a%2Bll9GLteY2bXdcFRy5atf1cH8hgmOv3xFNMOOHoaZ01sMIEBqNV88%2Bf7pIJENcKIP76iiR6Xv69ANjLrGd7D6Rsmit%2BcGM&X-Amz-Signature=54e951a960f4e976d6a9788cf23af408179b6cf6980d4a684e649976e0ac948d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFENFY4M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIH%2FAADxJIJ5%2Fpd86F6EYRKASrvczXsQRDEBDLdmsEvHRAiBaK%2FrevBoTw9n9757Xu90v2qvFm%2Fi3QV%2FN6oBqVzx%2F2CqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUhXeuoDeQIqYONhzKtwDZ0AKSjaby3MMUEymwBI%2FTTOTlwbZmELKVnX4xfxDlcowscZxME1LzL%2FNCUxy0Jim0oeP5UPWLTwUdwx6FQOFVnet92oC%2BAnt3KlmxjpUkSJMfLtOwRVERP8ickG97%2FsZYHEyB166cgsEc%2F4iXAGqdm3OUR%2B%2BTehBf8LOHttHrWj15ZM6a4l%2B3hRbfa%2BOfsgSfAFjvKggOBjg2Nxz%2BdkMkp%2BYvdxDb1Hqc60RXi4on%2Bbi9bcql2P3zF%2FSrAUq6b6qeF%2BNwK2hmiIM92y2x%2BPColh2jp7xCHxaAxcJztXDbR3g9htBvbXf4Checa4dzJrcmLFnaNgm1WSRLVY59tRZREG0j0ZkkQzTStMp%2FJMN8%2F4wIoOrq%2FhnnAyrHnlLvCwg20O4W2itPERPmjn%2FqmHQDW9CV5zgYMeClvv25n8%2FNCNYTIVCrBw9wVxf58ysEPaams%2FLbr4lfxfF9LFFl6Ysvrm9q89Pq6I52iYHKZTl1kwnX6M8nW%2FKiTzQRsFGukUdeRElF3x7F%2B1IUZYVg5lq7LJDJf0Wx9Oj%2B%2B8IvPuwyv9cAoDDAmsfgm%2BfkWKEQJTljpYDkMgNj2C80X2thgbI6XYCZaZAACtB8HyumtX5i2TmKZq1wTXGTTzjU7wwxeflvAY6pgEs6bKDSrG%2BFro8k%2FX%2FH9UGlhbTLh75N%2FJUZhcmxXCxxAmQUX0wVCFGtpHSt1FyjLDRrMgJPjKpRs0WDKHD%2BXAxTqEH2jClVJVFh3LVUGZIyeuhzQNw0At4NOEzsNsH5a%2Bll9GLteY2bXdcFRy5atf1cH8hgmOv3xFNMOOHoaZ01sMIEBqNV88%2Bf7pIJENcKIP76iiR6Xv69ANjLrGd7D6Rsmit%2BcGM&X-Amz-Signature=819ca261064fd335aa55684cd801efc41b1bfee5fde62afa1c423ec3075a5445&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V64R44IE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIG0iWbWlVUvC3C5goz8YnNMszNC7oz4xbRiSRdtnrt6CAiEA24S9WN5k4oF%2BjfI%2F9lNScrJtfDq7rzlfv7gOdV%2FiBmQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIVBTfTNgD8I9zZ%2BYircAypuTPeNz3qTCHAHEmaV5aMoUtQmzWZhDy3cffQJ8XoiWzHT21nhYYtvnTagDgn9lAL8qhLLQ1ITdpACJG2mDx4eVnK7g0P89X5sun8zf7w4r5IP7Fh9jzxASuAYay3g%2B0NQJ3Ypq9oyo%2BIAuqEoRMWTehQ%2Fn61KPm197jcXUc8W2FKwuyjLQMBJMw5h0xxNCGlEPn53erXbZ2Q%2BRcYBIk%2FNUzd%2Bzz1lxQM0EN8710ouZZ1BzM0oGcm0zHsI0RFEW407y3B5qtr1pnMeRRDmXSSF4FLsEdp7WJqOd2g9XpahakgcHshYoI3BNsrUUsJrYFNCu%2B3s%2BCvV%2BHOeOr7XmCQEsbtur9P1AcEExrvQXfkFsZJyw1VUO6iIypwptZJZH1J3fNMyy3LHzU9JqSdGp6smmi7%2BYTosUjV%2FhdQN1spzStrthwM6mPdhTGHSF7ohwTfkOdQgh4etM%2B8WpkeOAUvddMLkNB8t9PSRf43nLcQGTSNsY1hMnQCgj9up8BaOf306Rea5u3DJ1KMwBscUo957Ql8At1NIY%2BHDHtf9KgkKNT8SDC2pZnv0pLQBDJYYeKHNp%2BcDRl3YGoBjtqFSAGlO4HoQKR0eBQv%2B9aMrLq5VktoCWWQY0U0Ht1ivMKPo5bwGOqUBmpQZ9F5Z9DSaoIX52uyssRMJn8qkLnnvfE8I%2BShuFe1IollrChtaUtcda1dXgMPk4d619XTbrkuNQSF4G2YBqkn%2F2zrT8Mo0hh4l7eVRsvQVPuKlfzg7l5LS358gsYHZLTuTw1fGiipEB08hxPHrMOAlKQU89G0BDpQTj%2FnWZXPn%2BPiPfx2xqDpAbc%2F8Xx3IFyUzgeMsbij2KzGCAe73vdnL67Am&X-Amz-Signature=193033a8422449d0727363c8a9828ac6a2d8f29d6beaadc7eea22a6d3a9671b1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V64R44IE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIG0iWbWlVUvC3C5goz8YnNMszNC7oz4xbRiSRdtnrt6CAiEA24S9WN5k4oF%2BjfI%2F9lNScrJtfDq7rzlfv7gOdV%2FiBmQqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIVBTfTNgD8I9zZ%2BYircAypuTPeNz3qTCHAHEmaV5aMoUtQmzWZhDy3cffQJ8XoiWzHT21nhYYtvnTagDgn9lAL8qhLLQ1ITdpACJG2mDx4eVnK7g0P89X5sun8zf7w4r5IP7Fh9jzxASuAYay3g%2B0NQJ3Ypq9oyo%2BIAuqEoRMWTehQ%2Fn61KPm197jcXUc8W2FKwuyjLQMBJMw5h0xxNCGlEPn53erXbZ2Q%2BRcYBIk%2FNUzd%2Bzz1lxQM0EN8710ouZZ1BzM0oGcm0zHsI0RFEW407y3B5qtr1pnMeRRDmXSSF4FLsEdp7WJqOd2g9XpahakgcHshYoI3BNsrUUsJrYFNCu%2B3s%2BCvV%2BHOeOr7XmCQEsbtur9P1AcEExrvQXfkFsZJyw1VUO6iIypwptZJZH1J3fNMyy3LHzU9JqSdGp6smmi7%2BYTosUjV%2FhdQN1spzStrthwM6mPdhTGHSF7ohwTfkOdQgh4etM%2B8WpkeOAUvddMLkNB8t9PSRf43nLcQGTSNsY1hMnQCgj9up8BaOf306Rea5u3DJ1KMwBscUo957Ql8At1NIY%2BHDHtf9KgkKNT8SDC2pZnv0pLQBDJYYeKHNp%2BcDRl3YGoBjtqFSAGlO4HoQKR0eBQv%2B9aMrLq5VktoCWWQY0U0Ht1ivMKPo5bwGOqUBmpQZ9F5Z9DSaoIX52uyssRMJn8qkLnnvfE8I%2BShuFe1IollrChtaUtcda1dXgMPk4d619XTbrkuNQSF4G2YBqkn%2F2zrT8Mo0hh4l7eVRsvQVPuKlfzg7l5LS358gsYHZLTuTw1fGiipEB08hxPHrMOAlKQU89G0BDpQTj%2FnWZXPn%2BPiPfx2xqDpAbc%2F8Xx3IFyUzgeMsbij2KzGCAe73vdnL67Am&X-Amz-Signature=b4a00e2e49e382d255b2934d9bed6065b6e213c499f52350effafa3ee6eb96df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFENFY4M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIH%2FAADxJIJ5%2Fpd86F6EYRKASrvczXsQRDEBDLdmsEvHRAiBaK%2FrevBoTw9n9757Xu90v2qvFm%2Fi3QV%2FN6oBqVzx%2F2CqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUhXeuoDeQIqYONhzKtwDZ0AKSjaby3MMUEymwBI%2FTTOTlwbZmELKVnX4xfxDlcowscZxME1LzL%2FNCUxy0Jim0oeP5UPWLTwUdwx6FQOFVnet92oC%2BAnt3KlmxjpUkSJMfLtOwRVERP8ickG97%2FsZYHEyB166cgsEc%2F4iXAGqdm3OUR%2B%2BTehBf8LOHttHrWj15ZM6a4l%2B3hRbfa%2BOfsgSfAFjvKggOBjg2Nxz%2BdkMkp%2BYvdxDb1Hqc60RXi4on%2Bbi9bcql2P3zF%2FSrAUq6b6qeF%2BNwK2hmiIM92y2x%2BPColh2jp7xCHxaAxcJztXDbR3g9htBvbXf4Checa4dzJrcmLFnaNgm1WSRLVY59tRZREG0j0ZkkQzTStMp%2FJMN8%2F4wIoOrq%2FhnnAyrHnlLvCwg20O4W2itPERPmjn%2FqmHQDW9CV5zgYMeClvv25n8%2FNCNYTIVCrBw9wVxf58ysEPaams%2FLbr4lfxfF9LFFl6Ysvrm9q89Pq6I52iYHKZTl1kwnX6M8nW%2FKiTzQRsFGukUdeRElF3x7F%2B1IUZYVg5lq7LJDJf0Wx9Oj%2B%2B8IvPuwyv9cAoDDAmsfgm%2BfkWKEQJTljpYDkMgNj2C80X2thgbI6XYCZaZAACtB8HyumtX5i2TmKZq1wTXGTTzjU7wwxeflvAY6pgEs6bKDSrG%2BFro8k%2FX%2FH9UGlhbTLh75N%2FJUZhcmxXCxxAmQUX0wVCFGtpHSt1FyjLDRrMgJPjKpRs0WDKHD%2BXAxTqEH2jClVJVFh3LVUGZIyeuhzQNw0At4NOEzsNsH5a%2Bll9GLteY2bXdcFRy5atf1cH8hgmOv3xFNMOOHoaZ01sMIEBqNV88%2Bf7pIJENcKIP76iiR6Xv69ANjLrGd7D6Rsmit%2BcGM&X-Amz-Signature=d65a9f4345538f3adbe3d386e57ad03739f41f45aa7f2f21ea753cb897180a34&X-Amz-SignedHeaders=host&x-id=GetObject)
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