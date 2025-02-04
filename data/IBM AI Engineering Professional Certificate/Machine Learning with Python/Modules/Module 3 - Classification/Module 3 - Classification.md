

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WE4OPMNZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIHGq6nPE%2FaqZD1m0SJbp5fZeDiF4PzEwGVd6ulMk1o5rAiBwLaOZUC2zYzpOtzUxG5W%2FuwC6Os9sX56uhFE3ezuGJir%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMlCd2adfm%2FnMLrjghKtwDTQwf96TjlDT5e%2FufR7LeJJ4krF09HBNTaTK5XP9Ax4d9OKmS6hOqUslpSricLABDQLdJ1Vzc3LaBEknWhTVeZzJd8eU%2FdJNDPbPshZKxtw2Sn%2FSHIvnTyqjORi4KfQFvxoUOcTDcZfn7wgMuFx5kmU8SEoywiBHg5OjLwGsIHA%2F0ZLhBa2N5zVOJinu6AOUOdiVNPKCawd8le5s9gU3We%2B8KgiLUsozrEInx4htIcRUF107N0EamFdFd%2FQinLZWA%2BDfirwyzSi1m421ThdvTDwj2tisLyTGHonQ2JuSnIzL5EaWIKgpRebXZP2sTXW4AGGZb00ay1TGSi6ZJv%2FW%2BmWGf8TcTJYmd8gOmRc5Q3ArJXM1M6GdggYu%2BVrDGspsRtWpO%2ByK2wkfVwtz%2B46jsJTDsciBCwT4D3A7LBCcoHOAIt6Jx9pU6G96731qaLHvoPIrtl3v%2Fl6JHpbK2M7RfhAYGq05qrROOrdjKQlet42XEpH%2BJOTNyS%2BGXzCneBWtv2c4RSSMOKJV20Y83lWeNudUyw%2Be0na6c%2FYXJNSghUgaH7ALq5YX4k216op5ewj15BQE0aidaQoXRq%2FzvgLVqqZbBigkFW4cvUs%2F7nJHjWtFEG%2B%2B5%2FJU8W%2FzNI%2BQwieaHvQY6pgF%2BlRa2usryKgGLkxCh%2FfCIaH4V6ACLXTrfBaAwro%2BqEOn1NK5iF0YNL4sj6HPE6NFinvj7Q%2FEYZT4CKh2LKbrfWHC88YcrnUMeqz154lu3Y38PrDhDdnNaNRwfvJHrpJ51JLjiDK7dBZhJcDP7lnOuK59MDh5bv9nCXaYzc6t%2FY%2FBRXkpKM6uX2JlSYjldV%2B6oD9ScvLLWqDWrMGLxLSk%2BsYznf1zm&X-Amz-Signature=13ab474b9b124cc46c8215dcb0a2dda73c1d348e09997aad531f83f502879edf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WE4OPMNZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIHGq6nPE%2FaqZD1m0SJbp5fZeDiF4PzEwGVd6ulMk1o5rAiBwLaOZUC2zYzpOtzUxG5W%2FuwC6Os9sX56uhFE3ezuGJir%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMlCd2adfm%2FnMLrjghKtwDTQwf96TjlDT5e%2FufR7LeJJ4krF09HBNTaTK5XP9Ax4d9OKmS6hOqUslpSricLABDQLdJ1Vzc3LaBEknWhTVeZzJd8eU%2FdJNDPbPshZKxtw2Sn%2FSHIvnTyqjORi4KfQFvxoUOcTDcZfn7wgMuFx5kmU8SEoywiBHg5OjLwGsIHA%2F0ZLhBa2N5zVOJinu6AOUOdiVNPKCawd8le5s9gU3We%2B8KgiLUsozrEInx4htIcRUF107N0EamFdFd%2FQinLZWA%2BDfirwyzSi1m421ThdvTDwj2tisLyTGHonQ2JuSnIzL5EaWIKgpRebXZP2sTXW4AGGZb00ay1TGSi6ZJv%2FW%2BmWGf8TcTJYmd8gOmRc5Q3ArJXM1M6GdggYu%2BVrDGspsRtWpO%2ByK2wkfVwtz%2B46jsJTDsciBCwT4D3A7LBCcoHOAIt6Jx9pU6G96731qaLHvoPIrtl3v%2Fl6JHpbK2M7RfhAYGq05qrROOrdjKQlet42XEpH%2BJOTNyS%2BGXzCneBWtv2c4RSSMOKJV20Y83lWeNudUyw%2Be0na6c%2FYXJNSghUgaH7ALq5YX4k216op5ewj15BQE0aidaQoXRq%2FzvgLVqqZbBigkFW4cvUs%2F7nJHjWtFEG%2B%2B5%2FJU8W%2FzNI%2BQwieaHvQY6pgF%2BlRa2usryKgGLkxCh%2FfCIaH4V6ACLXTrfBaAwro%2BqEOn1NK5iF0YNL4sj6HPE6NFinvj7Q%2FEYZT4CKh2LKbrfWHC88YcrnUMeqz154lu3Y38PrDhDdnNaNRwfvJHrpJ51JLjiDK7dBZhJcDP7lnOuK59MDh5bv9nCXaYzc6t%2FY%2FBRXkpKM6uX2JlSYjldV%2B6oD9ScvLLWqDWrMGLxLSk%2BsYznf1zm&X-Amz-Signature=acde5a6460c445edee0c1b5cc218e47ab48d05b39b11f5ac82f35c4487dce85b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WE4OPMNZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIHGq6nPE%2FaqZD1m0SJbp5fZeDiF4PzEwGVd6ulMk1o5rAiBwLaOZUC2zYzpOtzUxG5W%2FuwC6Os9sX56uhFE3ezuGJir%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMlCd2adfm%2FnMLrjghKtwDTQwf96TjlDT5e%2FufR7LeJJ4krF09HBNTaTK5XP9Ax4d9OKmS6hOqUslpSricLABDQLdJ1Vzc3LaBEknWhTVeZzJd8eU%2FdJNDPbPshZKxtw2Sn%2FSHIvnTyqjORi4KfQFvxoUOcTDcZfn7wgMuFx5kmU8SEoywiBHg5OjLwGsIHA%2F0ZLhBa2N5zVOJinu6AOUOdiVNPKCawd8le5s9gU3We%2B8KgiLUsozrEInx4htIcRUF107N0EamFdFd%2FQinLZWA%2BDfirwyzSi1m421ThdvTDwj2tisLyTGHonQ2JuSnIzL5EaWIKgpRebXZP2sTXW4AGGZb00ay1TGSi6ZJv%2FW%2BmWGf8TcTJYmd8gOmRc5Q3ArJXM1M6GdggYu%2BVrDGspsRtWpO%2ByK2wkfVwtz%2B46jsJTDsciBCwT4D3A7LBCcoHOAIt6Jx9pU6G96731qaLHvoPIrtl3v%2Fl6JHpbK2M7RfhAYGq05qrROOrdjKQlet42XEpH%2BJOTNyS%2BGXzCneBWtv2c4RSSMOKJV20Y83lWeNudUyw%2Be0na6c%2FYXJNSghUgaH7ALq5YX4k216op5ewj15BQE0aidaQoXRq%2FzvgLVqqZbBigkFW4cvUs%2F7nJHjWtFEG%2B%2B5%2FJU8W%2FzNI%2BQwieaHvQY6pgF%2BlRa2usryKgGLkxCh%2FfCIaH4V6ACLXTrfBaAwro%2BqEOn1NK5iF0YNL4sj6HPE6NFinvj7Q%2FEYZT4CKh2LKbrfWHC88YcrnUMeqz154lu3Y38PrDhDdnNaNRwfvJHrpJ51JLjiDK7dBZhJcDP7lnOuK59MDh5bv9nCXaYzc6t%2FY%2FBRXkpKM6uX2JlSYjldV%2B6oD9ScvLLWqDWrMGLxLSk%2BsYznf1zm&X-Amz-Signature=29ba337067d1973f743c134a17c2ceb6eadbc39eb9337972c68e83c8cb2fdc02&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RMPLCTR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIA3fXShg2DOZSwOmOk9k%2Fsc3Fz2%2ByPJEAs0uz5ip2ZpUAiAuHioPEwlskiYltpSiv9%2Fz%2Bei02xYDT5mR%2FajhXSU4byr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMs2fzvnuAtRT1KW3%2FKtwDEKIzRympvqiGmKmyOB%2BLqoIk%2BiXkd9yctEx4BJ%2BTluYSXFOmMI0KTFmp0Gz2Dfv6%2FIzK3buGFy2MpKFntbUui1icGAM2uNgIrjRVyjwtI9IJIoB94rNrLZvzuVjXOxa3Snk7jlEjsNG0QF6634X4v1JNIuIoNRmYGvW3W2tEAC%2BLwPNpRMDs1c%2B%2BXSdmjylYbBoaeJgKSDRsghtDCEqoqHhWE6mXhg%2FtY5iG3apRi9oDRKS1pcG59svNtd4gSl7h%2FORF0bHkxxYDoEMeDKzIjm7z5gVNBFEwMATka2hPUTMCDVKlA24TN8am1JY3b%2Bm0upRUp6OzLMLcD6PcWpnbLmmEC%2F63BEL9lMpStWUd0A5wt770Y%2BE1rIm78MrUou3t%2FKfopcsUUpEBA31oG6b1tDBhpfEK1l1cO1uhiserPrwpw7HgINXsSZ9QVoMyE1C9bGYgxhS06u11U1%2BljG8%2B%2Bwpo%2B2%2BB6AdkCfF%2BSEQ%2FUczXd6gEsE%2BMmU6IA6OKppzXMr2ohGaC7qlQZKHk6i7by3ub870nmojwJ0CUQ2afOk0m%2FznjOqnT%2F2oavHXaAFpTTXSTlY1syn7Lx%2Fl3lMMf3UfYQU%2FHwEHRgJtnb0atQjrdS0bbfxasLdoJsy8wn%2BaHvQY6pgFe3bwJn%2BQQbTv%2FuU%2BCSDew9wnnkS7mQJH1Ihp%2Bmdd%2BIDD7rwfHo28RsLEHhFOpk5FD%2F8glXzsukdhftNESJr1p03Iv7mcZ0%2BbInlqS8BzWGOwXNS2rLVMiO0EbWp7vvg1owSA9exm6hvMxspRZFiw0t1sE8InLED1oT7iaXGQVPD%2F7p28asC0qSVnyAtHIJ62Ex99vpzGhOaujhGodiUCQhyzE6qrW&X-Amz-Signature=d124253d3c357802d6cbd5212904bda970b1c5ec2ad603b6196de11533859b34&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RMPLCTR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIA3fXShg2DOZSwOmOk9k%2Fsc3Fz2%2ByPJEAs0uz5ip2ZpUAiAuHioPEwlskiYltpSiv9%2Fz%2Bei02xYDT5mR%2FajhXSU4byr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMs2fzvnuAtRT1KW3%2FKtwDEKIzRympvqiGmKmyOB%2BLqoIk%2BiXkd9yctEx4BJ%2BTluYSXFOmMI0KTFmp0Gz2Dfv6%2FIzK3buGFy2MpKFntbUui1icGAM2uNgIrjRVyjwtI9IJIoB94rNrLZvzuVjXOxa3Snk7jlEjsNG0QF6634X4v1JNIuIoNRmYGvW3W2tEAC%2BLwPNpRMDs1c%2B%2BXSdmjylYbBoaeJgKSDRsghtDCEqoqHhWE6mXhg%2FtY5iG3apRi9oDRKS1pcG59svNtd4gSl7h%2FORF0bHkxxYDoEMeDKzIjm7z5gVNBFEwMATka2hPUTMCDVKlA24TN8am1JY3b%2Bm0upRUp6OzLMLcD6PcWpnbLmmEC%2F63BEL9lMpStWUd0A5wt770Y%2BE1rIm78MrUou3t%2FKfopcsUUpEBA31oG6b1tDBhpfEK1l1cO1uhiserPrwpw7HgINXsSZ9QVoMyE1C9bGYgxhS06u11U1%2BljG8%2B%2Bwpo%2B2%2BB6AdkCfF%2BSEQ%2FUczXd6gEsE%2BMmU6IA6OKppzXMr2ohGaC7qlQZKHk6i7by3ub870nmojwJ0CUQ2afOk0m%2FznjOqnT%2F2oavHXaAFpTTXSTlY1syn7Lx%2Fl3lMMf3UfYQU%2FHwEHRgJtnb0atQjrdS0bbfxasLdoJsy8wn%2BaHvQY6pgFe3bwJn%2BQQbTv%2FuU%2BCSDew9wnnkS7mQJH1Ihp%2Bmdd%2BIDD7rwfHo28RsLEHhFOpk5FD%2F8glXzsukdhftNESJr1p03Iv7mcZ0%2BbInlqS8BzWGOwXNS2rLVMiO0EbWp7vvg1owSA9exm6hvMxspRZFiw0t1sE8InLED1oT7iaXGQVPD%2F7p28asC0qSVnyAtHIJ62Ex99vpzGhOaujhGodiUCQhyzE6qrW&X-Amz-Signature=237721709c507d3953db5fd0936b42ba427240c0f6be6a2b91e7bb2ef257fe2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WE4OPMNZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJGMEQCIHGq6nPE%2FaqZD1m0SJbp5fZeDiF4PzEwGVd6ulMk1o5rAiBwLaOZUC2zYzpOtzUxG5W%2FuwC6Os9sX56uhFE3ezuGJir%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMlCd2adfm%2FnMLrjghKtwDTQwf96TjlDT5e%2FufR7LeJJ4krF09HBNTaTK5XP9Ax4d9OKmS6hOqUslpSricLABDQLdJ1Vzc3LaBEknWhTVeZzJd8eU%2FdJNDPbPshZKxtw2Sn%2FSHIvnTyqjORi4KfQFvxoUOcTDcZfn7wgMuFx5kmU8SEoywiBHg5OjLwGsIHA%2F0ZLhBa2N5zVOJinu6AOUOdiVNPKCawd8le5s9gU3We%2B8KgiLUsozrEInx4htIcRUF107N0EamFdFd%2FQinLZWA%2BDfirwyzSi1m421ThdvTDwj2tisLyTGHonQ2JuSnIzL5EaWIKgpRebXZP2sTXW4AGGZb00ay1TGSi6ZJv%2FW%2BmWGf8TcTJYmd8gOmRc5Q3ArJXM1M6GdggYu%2BVrDGspsRtWpO%2ByK2wkfVwtz%2B46jsJTDsciBCwT4D3A7LBCcoHOAIt6Jx9pU6G96731qaLHvoPIrtl3v%2Fl6JHpbK2M7RfhAYGq05qrROOrdjKQlet42XEpH%2BJOTNyS%2BGXzCneBWtv2c4RSSMOKJV20Y83lWeNudUyw%2Be0na6c%2FYXJNSghUgaH7ALq5YX4k216op5ewj15BQE0aidaQoXRq%2FzvgLVqqZbBigkFW4cvUs%2F7nJHjWtFEG%2B%2B5%2FJU8W%2FzNI%2BQwieaHvQY6pgF%2BlRa2usryKgGLkxCh%2FfCIaH4V6ACLXTrfBaAwro%2BqEOn1NK5iF0YNL4sj6HPE6NFinvj7Q%2FEYZT4CKh2LKbrfWHC88YcrnUMeqz154lu3Y38PrDhDdnNaNRwfvJHrpJ51JLjiDK7dBZhJcDP7lnOuK59MDh5bv9nCXaYzc6t%2FY%2FBRXkpKM6uX2JlSYjldV%2B6oD9ScvLLWqDWrMGLxLSk%2BsYznf1zm&X-Amz-Signature=2b92faabed94a73028e97b6354b3386ac0fd0149bb5128137bbecd5ceaf5c0d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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