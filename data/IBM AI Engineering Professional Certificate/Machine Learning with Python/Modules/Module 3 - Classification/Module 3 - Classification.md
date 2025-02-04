

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVK7SD6B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQCJI7DAJvD9Nitk2HSo%2BLve30iO87ufWvRtwF6pG6qRigIhAMZWnwyS2z16qFDxZtuflAJ9O6dvMiEotVSwhAf1yDOzKv8DCCQQABoMNjM3NDIzMTgzODA1Igw4obN9FNRhJziOrj4q3AMiR7mRhZ19fd7RSeUrBkPbtiMtxygZPKGo1LC5EQUiFPkhWxEkM6uFnOf4FHV1mrQeO%2FSMcxUdAe6wpTUJLlLYsqxwG5UVb2DvbaNgkfKb8gKZZjtiQ%2BCP5B7G%2BbKpXOb6qvRG35C8lr00XwFjP5LGMRxXFrwbykgOq2jqJvaKwM1QbzOTW8FMJ0g90%2BEE1yaI3HGejmxvw7CZOR5jCGazTVn6vjc3us5uRiMLDC%2B5so8hrgUsOrMM%2FvzD2mnelq9RHI4YLE0WDu2baMypB4VNBhAQ0DTpyTWqNAX6JQPnqAo0Jphm1blQqoIP71fE8vk%2FkF3H4S3xWQAZkpplIItVqzXbpetrnkmLoqDeXL3caVY4ZSud4cF%2BccDpveELjMGRc8dks7SMNM2jdt%2F1LrLE66kAJs%2FZICdbA41%2Fr3bUfbeQAej6gXWEcSA9T3nF4hhqA%2BbY%2BzkTxaXUfnxW6u1I35vlKPWSRYS4%2Bj7E49IBfBx%2B6Re98oMOEbr03BgC%2BMTJF50w5G7vxyxCbpgKMaDpo2D8DKx%2BLf9Pw4gvlrB2Gjb%2F0b3nVrD1fXB7hDdzhnAufcUlo%2FQHZt6PI0RFTwZFO3EMyS0XzFskHqDvsoFBMlXDIoTys1AqRRbKVTCfhYa9BjqkAdXRejCuKLmFnGeWG2lW7g87awXh2SGaDI5mseeshtNKMFG12n6ggKp5VUWKB2wRmlXNd8UWOG1gMbKPjcaSKey52%2BZzdVA27Py5j7DJZSCPPYrkIFpLuFkVdy4mZjpnccYWsLn6VRv0o3pcEJGna90H%2FoRZrvZBdCR77omsDC477yOrPV2ratGQaRv13XGF1RZMeTehnfxeeq0phJ83TN7T5%2F4r&X-Amz-Signature=0a14e0e349bc6b40e7397366cf3ce781ea0eb2784812ea2c6e14b27dc28bc7b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVK7SD6B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQCJI7DAJvD9Nitk2HSo%2BLve30iO87ufWvRtwF6pG6qRigIhAMZWnwyS2z16qFDxZtuflAJ9O6dvMiEotVSwhAf1yDOzKv8DCCQQABoMNjM3NDIzMTgzODA1Igw4obN9FNRhJziOrj4q3AMiR7mRhZ19fd7RSeUrBkPbtiMtxygZPKGo1LC5EQUiFPkhWxEkM6uFnOf4FHV1mrQeO%2FSMcxUdAe6wpTUJLlLYsqxwG5UVb2DvbaNgkfKb8gKZZjtiQ%2BCP5B7G%2BbKpXOb6qvRG35C8lr00XwFjP5LGMRxXFrwbykgOq2jqJvaKwM1QbzOTW8FMJ0g90%2BEE1yaI3HGejmxvw7CZOR5jCGazTVn6vjc3us5uRiMLDC%2B5so8hrgUsOrMM%2FvzD2mnelq9RHI4YLE0WDu2baMypB4VNBhAQ0DTpyTWqNAX6JQPnqAo0Jphm1blQqoIP71fE8vk%2FkF3H4S3xWQAZkpplIItVqzXbpetrnkmLoqDeXL3caVY4ZSud4cF%2BccDpveELjMGRc8dks7SMNM2jdt%2F1LrLE66kAJs%2FZICdbA41%2Fr3bUfbeQAej6gXWEcSA9T3nF4hhqA%2BbY%2BzkTxaXUfnxW6u1I35vlKPWSRYS4%2Bj7E49IBfBx%2B6Re98oMOEbr03BgC%2BMTJF50w5G7vxyxCbpgKMaDpo2D8DKx%2BLf9Pw4gvlrB2Gjb%2F0b3nVrD1fXB7hDdzhnAufcUlo%2FQHZt6PI0RFTwZFO3EMyS0XzFskHqDvsoFBMlXDIoTys1AqRRbKVTCfhYa9BjqkAdXRejCuKLmFnGeWG2lW7g87awXh2SGaDI5mseeshtNKMFG12n6ggKp5VUWKB2wRmlXNd8UWOG1gMbKPjcaSKey52%2BZzdVA27Py5j7DJZSCPPYrkIFpLuFkVdy4mZjpnccYWsLn6VRv0o3pcEJGna90H%2FoRZrvZBdCR77omsDC477yOrPV2ratGQaRv13XGF1RZMeTehnfxeeq0phJ83TN7T5%2F4r&X-Amz-Signature=e25d6f89a3ee44592baf7380eed52b1d3f3bf13680f18fcee2b2e090e22db23e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVK7SD6B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQCJI7DAJvD9Nitk2HSo%2BLve30iO87ufWvRtwF6pG6qRigIhAMZWnwyS2z16qFDxZtuflAJ9O6dvMiEotVSwhAf1yDOzKv8DCCQQABoMNjM3NDIzMTgzODA1Igw4obN9FNRhJziOrj4q3AMiR7mRhZ19fd7RSeUrBkPbtiMtxygZPKGo1LC5EQUiFPkhWxEkM6uFnOf4FHV1mrQeO%2FSMcxUdAe6wpTUJLlLYsqxwG5UVb2DvbaNgkfKb8gKZZjtiQ%2BCP5B7G%2BbKpXOb6qvRG35C8lr00XwFjP5LGMRxXFrwbykgOq2jqJvaKwM1QbzOTW8FMJ0g90%2BEE1yaI3HGejmxvw7CZOR5jCGazTVn6vjc3us5uRiMLDC%2B5so8hrgUsOrMM%2FvzD2mnelq9RHI4YLE0WDu2baMypB4VNBhAQ0DTpyTWqNAX6JQPnqAo0Jphm1blQqoIP71fE8vk%2FkF3H4S3xWQAZkpplIItVqzXbpetrnkmLoqDeXL3caVY4ZSud4cF%2BccDpveELjMGRc8dks7SMNM2jdt%2F1LrLE66kAJs%2FZICdbA41%2Fr3bUfbeQAej6gXWEcSA9T3nF4hhqA%2BbY%2BzkTxaXUfnxW6u1I35vlKPWSRYS4%2Bj7E49IBfBx%2B6Re98oMOEbr03BgC%2BMTJF50w5G7vxyxCbpgKMaDpo2D8DKx%2BLf9Pw4gvlrB2Gjb%2F0b3nVrD1fXB7hDdzhnAufcUlo%2FQHZt6PI0RFTwZFO3EMyS0XzFskHqDvsoFBMlXDIoTys1AqRRbKVTCfhYa9BjqkAdXRejCuKLmFnGeWG2lW7g87awXh2SGaDI5mseeshtNKMFG12n6ggKp5VUWKB2wRmlXNd8UWOG1gMbKPjcaSKey52%2BZzdVA27Py5j7DJZSCPPYrkIFpLuFkVdy4mZjpnccYWsLn6VRv0o3pcEJGna90H%2FoRZrvZBdCR77omsDC477yOrPV2ratGQaRv13XGF1RZMeTehnfxeeq0phJ83TN7T5%2F4r&X-Amz-Signature=5203918913036e1e92322b1af3f6a57bcd28470bd523cfddfb4b7ebb12acbdf9&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRNKRDXL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIBvKxQjCqGRff31y3hNlsD8hysqecfn7L24j2PQxSjfSAiA6Ew2SB7QzgqOkjBzIzas1adMKMgeNJu1xoFMuaxOYcir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMVucVtakWtdA6UZhWKtwDweXJP0NFJLlQHM%2BhH9JuDsRDUimB3s%2FFAt7r2ah46VEDsanO5cutM%2B1U6k2Hvv8Cr%2BE0xM4iPx66Kjkw3qwgpkVZBCdaokde3eew%2FZbFW5DA1WDCDRcDIbxkD7CmPgtuWyGxCy8K2IrgYuf5oWiy4yvEyzDU5gqI3VyjpvUZ3FzY8GCqztCTi%2FHY1qzmc%2B6dXlCXJ6dvvqbc9EuOhPQcnVx03Kr4euo%2FIxPLLOeghPUI6BNE87P%2BbB4EI2fu76zpA5t3NZOJpqhIuFIBR%2BQmknxJDj1JBnuo%2FPFVEiqg3eDVWsneoAZIoKWXKtmBXbIy0ghavaWhfZLqnMMhDCh7KMG7e9DIYSjDGS5XR75zh5itPufiTusXrvvkkR%2FXd6%2BPuG5Hrokq%2B2uZp3V3sLjopN8D9jciyeoJWTrPojeVCSeaNEyuvH5qJKLr9ob6aTMmbLGJCxHVAClvyUUqouEQe%2BmPoszJ9r87yFgnZttN4lUuBtTBwxOx56hLt%2BAboaQCvWxewqe4nPpx6vjr%2FqutE9DVwOTyzm%2BoNOnmkVNaHdkRhRzPjJjWqjksMARgVtHXkjtOEJKEpmS%2F8QNuEucHXT4c6XTGUJuKkNWMrdowYF1Xjbw15OB%2Bx7ltwqsw5ISGvQY6pgGiHEhuALgqGqnBe2SQ0a4kr2r0Biy3CYuQqvdGZkKPk%2BPDT%2BEkCuRfAVw6I%2FaAo0dk30pJDcsDPXW49dZ5bUL6FvDHnK7Q9%2FbZJdBZZwgNhkJOP6OduvfZzp%2FaEk28abebIKiIzoC46dqRqz51dQfPt2bwcKz3633U8j87%2FtrN17digwMUiVXHhEaXSfCAaQVd710xawfjugue7Oepv0srLWkDFiVV&X-Amz-Signature=a93867ca656c804e531a54d7cf21ecb8095b4a462ed1cb3c987c745cd176c63e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRNKRDXL%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJGMEQCIBvKxQjCqGRff31y3hNlsD8hysqecfn7L24j2PQxSjfSAiA6Ew2SB7QzgqOkjBzIzas1adMKMgeNJu1xoFMuaxOYcir%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMVucVtakWtdA6UZhWKtwDweXJP0NFJLlQHM%2BhH9JuDsRDUimB3s%2FFAt7r2ah46VEDsanO5cutM%2B1U6k2Hvv8Cr%2BE0xM4iPx66Kjkw3qwgpkVZBCdaokde3eew%2FZbFW5DA1WDCDRcDIbxkD7CmPgtuWyGxCy8K2IrgYuf5oWiy4yvEyzDU5gqI3VyjpvUZ3FzY8GCqztCTi%2FHY1qzmc%2B6dXlCXJ6dvvqbc9EuOhPQcnVx03Kr4euo%2FIxPLLOeghPUI6BNE87P%2BbB4EI2fu76zpA5t3NZOJpqhIuFIBR%2BQmknxJDj1JBnuo%2FPFVEiqg3eDVWsneoAZIoKWXKtmBXbIy0ghavaWhfZLqnMMhDCh7KMG7e9DIYSjDGS5XR75zh5itPufiTusXrvvkkR%2FXd6%2BPuG5Hrokq%2B2uZp3V3sLjopN8D9jciyeoJWTrPojeVCSeaNEyuvH5qJKLr9ob6aTMmbLGJCxHVAClvyUUqouEQe%2BmPoszJ9r87yFgnZttN4lUuBtTBwxOx56hLt%2BAboaQCvWxewqe4nPpx6vjr%2FqutE9DVwOTyzm%2BoNOnmkVNaHdkRhRzPjJjWqjksMARgVtHXkjtOEJKEpmS%2F8QNuEucHXT4c6XTGUJuKkNWMrdowYF1Xjbw15OB%2Bx7ltwqsw5ISGvQY6pgGiHEhuALgqGqnBe2SQ0a4kr2r0Biy3CYuQqvdGZkKPk%2BPDT%2BEkCuRfAVw6I%2FaAo0dk30pJDcsDPXW49dZ5bUL6FvDHnK7Q9%2FbZJdBZZwgNhkJOP6OduvfZzp%2FaEk28abebIKiIzoC46dqRqz51dQfPt2bwcKz3633U8j87%2FtrN17digwMUiVXHhEaXSfCAaQVd710xawfjugue7Oepv0srLWkDFiVV&X-Amz-Signature=5af45b50ed46924c3c5835bc8dbbe4c6a81e658d1ce0a17242557f678c13aff7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVK7SD6B%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJIMEYCIQCJI7DAJvD9Nitk2HSo%2BLve30iO87ufWvRtwF6pG6qRigIhAMZWnwyS2z16qFDxZtuflAJ9O6dvMiEotVSwhAf1yDOzKv8DCCQQABoMNjM3NDIzMTgzODA1Igw4obN9FNRhJziOrj4q3AMiR7mRhZ19fd7RSeUrBkPbtiMtxygZPKGo1LC5EQUiFPkhWxEkM6uFnOf4FHV1mrQeO%2FSMcxUdAe6wpTUJLlLYsqxwG5UVb2DvbaNgkfKb8gKZZjtiQ%2BCP5B7G%2BbKpXOb6qvRG35C8lr00XwFjP5LGMRxXFrwbykgOq2jqJvaKwM1QbzOTW8FMJ0g90%2BEE1yaI3HGejmxvw7CZOR5jCGazTVn6vjc3us5uRiMLDC%2B5so8hrgUsOrMM%2FvzD2mnelq9RHI4YLE0WDu2baMypB4VNBhAQ0DTpyTWqNAX6JQPnqAo0Jphm1blQqoIP71fE8vk%2FkF3H4S3xWQAZkpplIItVqzXbpetrnkmLoqDeXL3caVY4ZSud4cF%2BccDpveELjMGRc8dks7SMNM2jdt%2F1LrLE66kAJs%2FZICdbA41%2Fr3bUfbeQAej6gXWEcSA9T3nF4hhqA%2BbY%2BzkTxaXUfnxW6u1I35vlKPWSRYS4%2Bj7E49IBfBx%2B6Re98oMOEbr03BgC%2BMTJF50w5G7vxyxCbpgKMaDpo2D8DKx%2BLf9Pw4gvlrB2Gjb%2F0b3nVrD1fXB7hDdzhnAufcUlo%2FQHZt6PI0RFTwZFO3EMyS0XzFskHqDvsoFBMlXDIoTys1AqRRbKVTCfhYa9BjqkAdXRejCuKLmFnGeWG2lW7g87awXh2SGaDI5mseeshtNKMFG12n6ggKp5VUWKB2wRmlXNd8UWOG1gMbKPjcaSKey52%2BZzdVA27Py5j7DJZSCPPYrkIFpLuFkVdy4mZjpnccYWsLn6VRv0o3pcEJGna90H%2FoRZrvZBdCR77omsDC477yOrPV2ratGQaRv13XGF1RZMeTehnfxeeq0phJ83TN7T5%2F4r&X-Amz-Signature=ce964bd0b6733a8c201f8df929bea08cdbc23104c83a2adc66f4cc7c6d07dc5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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