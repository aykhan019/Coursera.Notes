

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQSIJGET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIBDLG%2B2WVL8gUxmcuI0w6fdFXhI2lVkTjiU5vNZcNJK7AiEA%2BwcvJtDyILOLksTNBGY5vhY1Q%2FudCX9sAC6IiZNK8i4q%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDFpfFNWgORa50dZxiSrcA0%2Bg9UeaBYFSy4LmOJ4luIrGlSggPRBVVLAr0rdre2C%2BydAWluNPW3WgX5Hfi2aH%2Ft4ttDC4wEMRa5c5OH%2FUPiiPdIeThL0JlMkiNOzM76jtTXG2rYvSVXo0Ur%2F1daclAszILS29eXz2S2Ovf5ZpkCBAve4FpvwpQZ04TAHavEcEiWtqiGBUzlu3ossu1e7%2FmiJjJLmn7a4lqhf9ucET0ZLe%2FYJR96TfL1oLE2NWfaO2KNm9fZExOiq6DtclbOH4M67mRmgZ8YneMoA4Jn3Sx4NUl2ylvD%2BcJk18iY6ZpIWJVFIUlw9cxJSYtmNzpp6ICZgmJb9p2vlksPGo4GXHfiE2gAHh0xDpyuTVxouI4n64MdKfzmE8d6WBLnlMb0cUMF5qVNdJg89%2FfL2Cs6HE4AIHETZ5r%2FRU9IwzwmyILx6UiH4vi1W29A6liuSKsaLndSpNZ8FanqSym2iXbRtR2SoxOdZOzPKH2mYa6qb5gHBoc6%2FCFXel24bvahCEz4Jgp1Gbr2RC9LPygp2gEF%2BnKeN8Y1Gv1hqpTAoHHA2tY3Rl72VpjffYTpqaox1qTfnkt0duqNIdOtg27SegFxeK7zJPfOx2NGP%2Fp%2FVrCBSWE%2F0qX%2FknRXmKJxDJ%2Bz7TMI2ihr0GOqUBSBXoIQGCXR5%2FyoIFqcYRcmp5Uzezomumx%2FMo%2Fk0tSkRGPXe4ROfY7QQPCE6cXTrM6tIhaHujBHKm4mbaA%2FIwKU%2BCbCbIgd%2F2aeizAOs67oRo71VES5NJZnHb4pE8gR6rNemCyT2ntJSHRgq%2B1lUqUvabRkmoXzkFs12hHYd0uV96pqgzsU61zaO4XSiEduCA%2Fksf7N2vzEJy%2B3Fls27l4mZUUAp7&X-Amz-Signature=f5e48a76dceb2a7ac070e12962817b47245b0cdfd0fe4b506edd949c555520ca&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQSIJGET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIBDLG%2B2WVL8gUxmcuI0w6fdFXhI2lVkTjiU5vNZcNJK7AiEA%2BwcvJtDyILOLksTNBGY5vhY1Q%2FudCX9sAC6IiZNK8i4q%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDFpfFNWgORa50dZxiSrcA0%2Bg9UeaBYFSy4LmOJ4luIrGlSggPRBVVLAr0rdre2C%2BydAWluNPW3WgX5Hfi2aH%2Ft4ttDC4wEMRa5c5OH%2FUPiiPdIeThL0JlMkiNOzM76jtTXG2rYvSVXo0Ur%2F1daclAszILS29eXz2S2Ovf5ZpkCBAve4FpvwpQZ04TAHavEcEiWtqiGBUzlu3ossu1e7%2FmiJjJLmn7a4lqhf9ucET0ZLe%2FYJR96TfL1oLE2NWfaO2KNm9fZExOiq6DtclbOH4M67mRmgZ8YneMoA4Jn3Sx4NUl2ylvD%2BcJk18iY6ZpIWJVFIUlw9cxJSYtmNzpp6ICZgmJb9p2vlksPGo4GXHfiE2gAHh0xDpyuTVxouI4n64MdKfzmE8d6WBLnlMb0cUMF5qVNdJg89%2FfL2Cs6HE4AIHETZ5r%2FRU9IwzwmyILx6UiH4vi1W29A6liuSKsaLndSpNZ8FanqSym2iXbRtR2SoxOdZOzPKH2mYa6qb5gHBoc6%2FCFXel24bvahCEz4Jgp1Gbr2RC9LPygp2gEF%2BnKeN8Y1Gv1hqpTAoHHA2tY3Rl72VpjffYTpqaox1qTfnkt0duqNIdOtg27SegFxeK7zJPfOx2NGP%2Fp%2FVrCBSWE%2F0qX%2FknRXmKJxDJ%2Bz7TMI2ihr0GOqUBSBXoIQGCXR5%2FyoIFqcYRcmp5Uzezomumx%2FMo%2Fk0tSkRGPXe4ROfY7QQPCE6cXTrM6tIhaHujBHKm4mbaA%2FIwKU%2BCbCbIgd%2F2aeizAOs67oRo71VES5NJZnHb4pE8gR6rNemCyT2ntJSHRgq%2B1lUqUvabRkmoXzkFs12hHYd0uV96pqgzsU61zaO4XSiEduCA%2Fksf7N2vzEJy%2B3Fls27l4mZUUAp7&X-Amz-Signature=d76c90b152b667de3320ab75c53524899beb3dc92b5e06cc7603070990bba053&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQSIJGET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIBDLG%2B2WVL8gUxmcuI0w6fdFXhI2lVkTjiU5vNZcNJK7AiEA%2BwcvJtDyILOLksTNBGY5vhY1Q%2FudCX9sAC6IiZNK8i4q%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDFpfFNWgORa50dZxiSrcA0%2Bg9UeaBYFSy4LmOJ4luIrGlSggPRBVVLAr0rdre2C%2BydAWluNPW3WgX5Hfi2aH%2Ft4ttDC4wEMRa5c5OH%2FUPiiPdIeThL0JlMkiNOzM76jtTXG2rYvSVXo0Ur%2F1daclAszILS29eXz2S2Ovf5ZpkCBAve4FpvwpQZ04TAHavEcEiWtqiGBUzlu3ossu1e7%2FmiJjJLmn7a4lqhf9ucET0ZLe%2FYJR96TfL1oLE2NWfaO2KNm9fZExOiq6DtclbOH4M67mRmgZ8YneMoA4Jn3Sx4NUl2ylvD%2BcJk18iY6ZpIWJVFIUlw9cxJSYtmNzpp6ICZgmJb9p2vlksPGo4GXHfiE2gAHh0xDpyuTVxouI4n64MdKfzmE8d6WBLnlMb0cUMF5qVNdJg89%2FfL2Cs6HE4AIHETZ5r%2FRU9IwzwmyILx6UiH4vi1W29A6liuSKsaLndSpNZ8FanqSym2iXbRtR2SoxOdZOzPKH2mYa6qb5gHBoc6%2FCFXel24bvahCEz4Jgp1Gbr2RC9LPygp2gEF%2BnKeN8Y1Gv1hqpTAoHHA2tY3Rl72VpjffYTpqaox1qTfnkt0duqNIdOtg27SegFxeK7zJPfOx2NGP%2Fp%2FVrCBSWE%2F0qX%2FknRXmKJxDJ%2Bz7TMI2ihr0GOqUBSBXoIQGCXR5%2FyoIFqcYRcmp5Uzezomumx%2FMo%2Fk0tSkRGPXe4ROfY7QQPCE6cXTrM6tIhaHujBHKm4mbaA%2FIwKU%2BCbCbIgd%2F2aeizAOs67oRo71VES5NJZnHb4pE8gR6rNemCyT2ntJSHRgq%2B1lUqUvabRkmoXzkFs12hHYd0uV96pqgzsU61zaO4XSiEduCA%2Fksf7N2vzEJy%2B3Fls27l4mZUUAp7&X-Amz-Signature=6478df3052a1510110f45a9f3ba9921faf9c4af411830fad8d6fc431f5492a89&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643K3SWSK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIHQyVnMz8Gy7wsXddg%2F4lSpxpxSHWz%2BW3ZaDaZeWvIgkAiEAjnSL78cY%2BB%2Bx6qC4lOsrZwynt3NZvSjhUFyCIUGfzTgq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJziCE2a5QOK2IPQiyrcA%2Bcu70S%2B6nRtHnymAr2vYF5Zo%2FfA7ew%2FZXMyH%2F9%2FrL4UBZ5HtDq9hmbfMguiY5bsn0Ie1d3Fj4Xa5aTYLnL%2BfVXJPXHrm5FCJU073SZLQRfPSw9QfgkmPdo4jvfqC87L%2BhO4mLuGTC7yLJH4WWP6QiK8vo47WIUhAhzhfeHK%2F0vfhUsMcBNL6S%2BBTZ7q%2BDjyaoMa7oHM4zGdfGKQbEnHX3X0BZfhRmAImqsCVFk3VEx%2BqAGS%2FK6ehErp%2BEGWfk2P6FtkvrpljChuFfpuuCAGfUmC9PQp1oO2pCYSI0YKVed0LomQt3FlMbS6HlKRV%2BWiMZPZe6kK%2FO9%2BJnlcxDqR6hzjKuWJQMjIVgi7VTI8ZcZnHcfTPDtpVJkntZTx78qQGj3ioUeWPCE5%2Fx0fOAZ%2Fz1esi7rqPcGiWrTfrlHcZf4zt0%2Fn%2FqV5KuiJrN6IVhQ2EaVjhj8QOcw8TnzPWnxx%2FaBAXztTL9oRzMBQ8DFu5iAKSJnSwZALyrA24pZgW2LIc56Z1yMQ9yvMl4ilR7KoWsUGM%2FXvZlzfpsrd8NwCwZy6XuccaLX8UcflOfmPhV3qUAhS78czMhl2tIyy7ldnL1fwIaWafEVI79ROAfMliWEF3EeU2ZEvXddAZMWgMO2hhr0GOqUBm7Bm7U%2FE8y5jPu2cyIed1mviyhh6gO16uzsNqYpaDsh5V4pnww1HaGP0rk1MBrNLZI01zhAfjPR9INgEZt8td67UYhapd6T6RyFtOwjvvjSok7kQrxUdcBsHMw6cUo7lO4DtQ9hb1xEDawt8dmkQUCu2BccgcG4X4pZpVZznquwY3EfrnbQAsFz5UKgY%2FB0zqFyXvIih4xGJZoGxsz%2B8tR9UNjJo&X-Amz-Signature=3d14c0ba1ea84e2e842cb41b72a8b0df6113756b30c6b8dd2cd488e834a3f844&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643K3SWSK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIHQyVnMz8Gy7wsXddg%2F4lSpxpxSHWz%2BW3ZaDaZeWvIgkAiEAjnSL78cY%2BB%2Bx6qC4lOsrZwynt3NZvSjhUFyCIUGfzTgq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDJziCE2a5QOK2IPQiyrcA%2Bcu70S%2B6nRtHnymAr2vYF5Zo%2FfA7ew%2FZXMyH%2F9%2FrL4UBZ5HtDq9hmbfMguiY5bsn0Ie1d3Fj4Xa5aTYLnL%2BfVXJPXHrm5FCJU073SZLQRfPSw9QfgkmPdo4jvfqC87L%2BhO4mLuGTC7yLJH4WWP6QiK8vo47WIUhAhzhfeHK%2F0vfhUsMcBNL6S%2BBTZ7q%2BDjyaoMa7oHM4zGdfGKQbEnHX3X0BZfhRmAImqsCVFk3VEx%2BqAGS%2FK6ehErp%2BEGWfk2P6FtkvrpljChuFfpuuCAGfUmC9PQp1oO2pCYSI0YKVed0LomQt3FlMbS6HlKRV%2BWiMZPZe6kK%2FO9%2BJnlcxDqR6hzjKuWJQMjIVgi7VTI8ZcZnHcfTPDtpVJkntZTx78qQGj3ioUeWPCE5%2Fx0fOAZ%2Fz1esi7rqPcGiWrTfrlHcZf4zt0%2Fn%2FqV5KuiJrN6IVhQ2EaVjhj8QOcw8TnzPWnxx%2FaBAXztTL9oRzMBQ8DFu5iAKSJnSwZALyrA24pZgW2LIc56Z1yMQ9yvMl4ilR7KoWsUGM%2FXvZlzfpsrd8NwCwZy6XuccaLX8UcflOfmPhV3qUAhS78czMhl2tIyy7ldnL1fwIaWafEVI79ROAfMliWEF3EeU2ZEvXddAZMWgMO2hhr0GOqUBm7Bm7U%2FE8y5jPu2cyIed1mviyhh6gO16uzsNqYpaDsh5V4pnww1HaGP0rk1MBrNLZI01zhAfjPR9INgEZt8td67UYhapd6T6RyFtOwjvvjSok7kQrxUdcBsHMw6cUo7lO4DtQ9hb1xEDawt8dmkQUCu2BccgcG4X4pZpVZznquwY3EfrnbQAsFz5UKgY%2FB0zqFyXvIih4xGJZoGxsz%2B8tR9UNjJo&X-Amz-Signature=3efeb0c6fd5dc488355c4623f201d53a9e4c24297252e76239548d4a7a3aa7aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQSIJGET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIBDLG%2B2WVL8gUxmcuI0w6fdFXhI2lVkTjiU5vNZcNJK7AiEA%2BwcvJtDyILOLksTNBGY5vhY1Q%2FudCX9sAC6IiZNK8i4q%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDFpfFNWgORa50dZxiSrcA0%2Bg9UeaBYFSy4LmOJ4luIrGlSggPRBVVLAr0rdre2C%2BydAWluNPW3WgX5Hfi2aH%2Ft4ttDC4wEMRa5c5OH%2FUPiiPdIeThL0JlMkiNOzM76jtTXG2rYvSVXo0Ur%2F1daclAszILS29eXz2S2Ovf5ZpkCBAve4FpvwpQZ04TAHavEcEiWtqiGBUzlu3ossu1e7%2FmiJjJLmn7a4lqhf9ucET0ZLe%2FYJR96TfL1oLE2NWfaO2KNm9fZExOiq6DtclbOH4M67mRmgZ8YneMoA4Jn3Sx4NUl2ylvD%2BcJk18iY6ZpIWJVFIUlw9cxJSYtmNzpp6ICZgmJb9p2vlksPGo4GXHfiE2gAHh0xDpyuTVxouI4n64MdKfzmE8d6WBLnlMb0cUMF5qVNdJg89%2FfL2Cs6HE4AIHETZ5r%2FRU9IwzwmyILx6UiH4vi1W29A6liuSKsaLndSpNZ8FanqSym2iXbRtR2SoxOdZOzPKH2mYa6qb5gHBoc6%2FCFXel24bvahCEz4Jgp1Gbr2RC9LPygp2gEF%2BnKeN8Y1Gv1hqpTAoHHA2tY3Rl72VpjffYTpqaox1qTfnkt0duqNIdOtg27SegFxeK7zJPfOx2NGP%2Fp%2FVrCBSWE%2F0qX%2FknRXmKJxDJ%2Bz7TMI2ihr0GOqUBSBXoIQGCXR5%2FyoIFqcYRcmp5Uzezomumx%2FMo%2Fk0tSkRGPXe4ROfY7QQPCE6cXTrM6tIhaHujBHKm4mbaA%2FIwKU%2BCbCbIgd%2F2aeizAOs67oRo71VES5NJZnHb4pE8gR6rNemCyT2ntJSHRgq%2B1lUqUvabRkmoXzkFs12hHYd0uV96pqgzsU61zaO4XSiEduCA%2Fksf7N2vzEJy%2B3Fls27l4mZUUAp7&X-Amz-Signature=f00bf7b44844c40ef25b0db5d3ad9407d8ceb59d2ceda27abed0ee5788c2adde&X-Amz-SignedHeaders=host&x-id=GetObject)
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