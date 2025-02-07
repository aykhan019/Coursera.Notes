

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA6A4SPB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCOocQc0fJqmxERaFUxq7REFEYwEw2mKPRAq13cGEahFgIhANpVT4uupxQ2Z%2FHHVlDYCx%2Flb1cO6glhZDWDHf4fuZU0Kv8DCG4QABoMNjM3NDIzMTgzODA1IgyVCAsYmIPmwdneCxcq3AMCBrGLnD4rz68kEgj997bYIv2Lkd%2FtIPALiqgJYR20Ec%2FlTyM6O%2BALCLxlW4WfG9fz68As%2B%2FRFRQbWsrnxvK54uC4t%2BMNiUaaQOfmmne1W%2BDhyuHRoof%2Fb86d%2FFTCx3fCb3MhLESWpSjrRXDrqWDudRl5Cwts6CyArqxKG5tEv5QKZe1%2FAgbDEllQNz%2FNF6NdTs7fmff3HOo4I8S5d4QTSXrV3QeoZwUzPbUfpp6DvoiU2G3oOKxSctndwOsgMv36OedHDD9lnn5alQ1vc%2FX5CtMAe70htt7%2F%2FAiWv1CChFGwQ2wcNzDyvfPbn55vF5S8aAMc0MIM26riIyu8JguH%2BmHASfbK1QEy9BAcqYIPaePfEiGM1ungO0cMMhUeIkQ%2BsgNyAxiKJnVJQvpqwy9mDcMVGOgLHIH24VI0QRh8%2BkljAZHh76EnjAJMUTGlG5u6x%2Fwm4YxsSPg8fcy8lE%2Bb1bTOtpamAxDI6kZ3CH8B4QCg2ZVGq1uGI0Q6aGbuOZtTxWTW8kXLjQJYxfjYWQylObuEVVBtfNgW4wQDc3JVOGe96q0Dd1r%2FiDEI%2Fw9ZdxO1TIuf0L%2Bq3fGutGJJcF0W2M%2BWaLL1iMACqn9WYF9Hzk%2FlM7ABGhsTnbWP0ujCXoZa9BjqkAVOdm0DdH1GZIpmjJ3ajdRcDbWV3qyTSag53l5wiQSSOyDpFRR1G0IPd%2Bt7GhmZkJuJeGjIeHS6QYyNGuy21J7AwekFWEXe6K75Hzu7ldiKxm1YGrs5ed%2BbRg3OMfxVokIcFcC7GVfvc6oOwhi%2By2OI5oouqAwqb5bAUpQ5m%2B67kqArJUi4iflA4cZWXNx2yzxqXnK2bfM5WEqSbwst8WArn3RvP&X-Amz-Signature=3b6ca8e3faccf33741d53c90441925d36b42a7e865aa6c9623919c9ae0e0a73f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA6A4SPB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCOocQc0fJqmxERaFUxq7REFEYwEw2mKPRAq13cGEahFgIhANpVT4uupxQ2Z%2FHHVlDYCx%2Flb1cO6glhZDWDHf4fuZU0Kv8DCG4QABoMNjM3NDIzMTgzODA1IgyVCAsYmIPmwdneCxcq3AMCBrGLnD4rz68kEgj997bYIv2Lkd%2FtIPALiqgJYR20Ec%2FlTyM6O%2BALCLxlW4WfG9fz68As%2B%2FRFRQbWsrnxvK54uC4t%2BMNiUaaQOfmmne1W%2BDhyuHRoof%2Fb86d%2FFTCx3fCb3MhLESWpSjrRXDrqWDudRl5Cwts6CyArqxKG5tEv5QKZe1%2FAgbDEllQNz%2FNF6NdTs7fmff3HOo4I8S5d4QTSXrV3QeoZwUzPbUfpp6DvoiU2G3oOKxSctndwOsgMv36OedHDD9lnn5alQ1vc%2FX5CtMAe70htt7%2F%2FAiWv1CChFGwQ2wcNzDyvfPbn55vF5S8aAMc0MIM26riIyu8JguH%2BmHASfbK1QEy9BAcqYIPaePfEiGM1ungO0cMMhUeIkQ%2BsgNyAxiKJnVJQvpqwy9mDcMVGOgLHIH24VI0QRh8%2BkljAZHh76EnjAJMUTGlG5u6x%2Fwm4YxsSPg8fcy8lE%2Bb1bTOtpamAxDI6kZ3CH8B4QCg2ZVGq1uGI0Q6aGbuOZtTxWTW8kXLjQJYxfjYWQylObuEVVBtfNgW4wQDc3JVOGe96q0Dd1r%2FiDEI%2Fw9ZdxO1TIuf0L%2Bq3fGutGJJcF0W2M%2BWaLL1iMACqn9WYF9Hzk%2FlM7ABGhsTnbWP0ujCXoZa9BjqkAVOdm0DdH1GZIpmjJ3ajdRcDbWV3qyTSag53l5wiQSSOyDpFRR1G0IPd%2Bt7GhmZkJuJeGjIeHS6QYyNGuy21J7AwekFWEXe6K75Hzu7ldiKxm1YGrs5ed%2BbRg3OMfxVokIcFcC7GVfvc6oOwhi%2By2OI5oouqAwqb5bAUpQ5m%2B67kqArJUi4iflA4cZWXNx2yzxqXnK2bfM5WEqSbwst8WArn3RvP&X-Amz-Signature=dc324e4f9bb9f024d65f524f8af9bf392e848a564f2fae112b086cfb212d552e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA6A4SPB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCOocQc0fJqmxERaFUxq7REFEYwEw2mKPRAq13cGEahFgIhANpVT4uupxQ2Z%2FHHVlDYCx%2Flb1cO6glhZDWDHf4fuZU0Kv8DCG4QABoMNjM3NDIzMTgzODA1IgyVCAsYmIPmwdneCxcq3AMCBrGLnD4rz68kEgj997bYIv2Lkd%2FtIPALiqgJYR20Ec%2FlTyM6O%2BALCLxlW4WfG9fz68As%2B%2FRFRQbWsrnxvK54uC4t%2BMNiUaaQOfmmne1W%2BDhyuHRoof%2Fb86d%2FFTCx3fCb3MhLESWpSjrRXDrqWDudRl5Cwts6CyArqxKG5tEv5QKZe1%2FAgbDEllQNz%2FNF6NdTs7fmff3HOo4I8S5d4QTSXrV3QeoZwUzPbUfpp6DvoiU2G3oOKxSctndwOsgMv36OedHDD9lnn5alQ1vc%2FX5CtMAe70htt7%2F%2FAiWv1CChFGwQ2wcNzDyvfPbn55vF5S8aAMc0MIM26riIyu8JguH%2BmHASfbK1QEy9BAcqYIPaePfEiGM1ungO0cMMhUeIkQ%2BsgNyAxiKJnVJQvpqwy9mDcMVGOgLHIH24VI0QRh8%2BkljAZHh76EnjAJMUTGlG5u6x%2Fwm4YxsSPg8fcy8lE%2Bb1bTOtpamAxDI6kZ3CH8B4QCg2ZVGq1uGI0Q6aGbuOZtTxWTW8kXLjQJYxfjYWQylObuEVVBtfNgW4wQDc3JVOGe96q0Dd1r%2FiDEI%2Fw9ZdxO1TIuf0L%2Bq3fGutGJJcF0W2M%2BWaLL1iMACqn9WYF9Hzk%2FlM7ABGhsTnbWP0ujCXoZa9BjqkAVOdm0DdH1GZIpmjJ3ajdRcDbWV3qyTSag53l5wiQSSOyDpFRR1G0IPd%2Bt7GhmZkJuJeGjIeHS6QYyNGuy21J7AwekFWEXe6K75Hzu7ldiKxm1YGrs5ed%2BbRg3OMfxVokIcFcC7GVfvc6oOwhi%2By2OI5oouqAwqb5bAUpQ5m%2B67kqArJUi4iflA4cZWXNx2yzxqXnK2bfM5WEqSbwst8WArn3RvP&X-Amz-Signature=37d8e4140f17e1c6a3c295dc3c3d180aed8b392c92e943696a90c1fc372f9939&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDXFUY6H%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIDyMRSls8OBkfxhOaZZapOX5K7BOfCBiI6SBU8t07aAKAiB7os72qPSRJVsB0G4XHz0N1NUbl4lraHLRulcYj3AO8Sr%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIMo5O5N0Ly2fMPmd0tKtwDCXVHc8gxJF31DAao51%2Bt7JzSE9OdSoHWFTwqKJBX4utMP0TFPc%2FIsQumqhUM2F0C0crPqI8EGtEgV6OA1CWSmtoyWY7zgGyqWz8vH%2Bpbco1QIWpWvJaYc%2BC8dQ1pLhMH%2FE27GseZkpH0f5vWg3spjNYD4hZTtC1P90YW9dE57tR4KfcKCdFtksCQRnB3%2BcgdTu8ujuaZ4pbvHnE4kW0CcuVQQIY9maU0VwUkk7SYTj4fkyM5r5I7bd%2BRr%2Bu7sCLh1kuzrpc3G0lrRpDRqEO82I9nNlvD8UqxwPr5FtCwaw96YJbvYMbH9S%2FFBQ%2F57vPM3NGOPAojaQeBJCqvUjh6PFnhfNzoneTpNr6t2wZTTgYQmu7GoQnmhDPlpLFzaH3DXnxvUSqxOpWicJB2wDxxQy7ci%2FitQEW0pQs%2BE4h5UrmvHhOW%2Fo7UdI3WtIz3KOkCNKV7%2FHASR5%2F9x3Vay%2Fw78TZAEUUiPEUYIjyyV3gaJUgopj1nx0Zv%2Fw2gLJehZeV8d8GIcq7zRDTbDg83Js%2FxFzRo%2FTb%2FxtybNH9agO%2F7wk247XeOeseUABSxoDA59ZoFTTV8i%2FeRx3utKooP0u3bHS4lcDFdQYQUCx5z9euHbgOg%2B8Cjnnpk9vQnXMkw6qGWvQY6pgEOSPH0782BxkfuZJUym%2BjDKGgu%2FtU%2BDigndWoZH9LJLzKasOjI5GzAtggcYTrXuKTF%2BiBNW1EITHwck27RYbxhb8K%2FqgrmtkyUiV15%2FE%2FGBNIQtUTxM5XIr1MqSkzSzcBe3KJKU408yhUZ5Jy7R2R4T62ktBrmkeVVHdII3K1OcHKOnKvT%2FeYifQgzu1S2FmdCsfZFqtrF8DxpSVKE%2FN%2FRwjynGoGP&X-Amz-Signature=709b69e29f50289fa6f980c0d10b4214814ae29e6a60421d29d2057992ae5136&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDXFUY6H%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJGMEQCIDyMRSls8OBkfxhOaZZapOX5K7BOfCBiI6SBU8t07aAKAiB7os72qPSRJVsB0G4XHz0N1NUbl4lraHLRulcYj3AO8Sr%2FAwhuEAAaDDYzNzQyMzE4MzgwNSIMo5O5N0Ly2fMPmd0tKtwDCXVHc8gxJF31DAao51%2Bt7JzSE9OdSoHWFTwqKJBX4utMP0TFPc%2FIsQumqhUM2F0C0crPqI8EGtEgV6OA1CWSmtoyWY7zgGyqWz8vH%2Bpbco1QIWpWvJaYc%2BC8dQ1pLhMH%2FE27GseZkpH0f5vWg3spjNYD4hZTtC1P90YW9dE57tR4KfcKCdFtksCQRnB3%2BcgdTu8ujuaZ4pbvHnE4kW0CcuVQQIY9maU0VwUkk7SYTj4fkyM5r5I7bd%2BRr%2Bu7sCLh1kuzrpc3G0lrRpDRqEO82I9nNlvD8UqxwPr5FtCwaw96YJbvYMbH9S%2FFBQ%2F57vPM3NGOPAojaQeBJCqvUjh6PFnhfNzoneTpNr6t2wZTTgYQmu7GoQnmhDPlpLFzaH3DXnxvUSqxOpWicJB2wDxxQy7ci%2FitQEW0pQs%2BE4h5UrmvHhOW%2Fo7UdI3WtIz3KOkCNKV7%2FHASR5%2F9x3Vay%2Fw78TZAEUUiPEUYIjyyV3gaJUgopj1nx0Zv%2Fw2gLJehZeV8d8GIcq7zRDTbDg83Js%2FxFzRo%2FTb%2FxtybNH9agO%2F7wk247XeOeseUABSxoDA59ZoFTTV8i%2FeRx3utKooP0u3bHS4lcDFdQYQUCx5z9euHbgOg%2B8Cjnnpk9vQnXMkw6qGWvQY6pgEOSPH0782BxkfuZJUym%2BjDKGgu%2FtU%2BDigndWoZH9LJLzKasOjI5GzAtggcYTrXuKTF%2BiBNW1EITHwck27RYbxhb8K%2FqgrmtkyUiV15%2FE%2FGBNIQtUTxM5XIr1MqSkzSzcBe3KJKU408yhUZ5Jy7R2R4T62ktBrmkeVVHdII3K1OcHKOnKvT%2FeYifQgzu1S2FmdCsfZFqtrF8DxpSVKE%2FN%2FRwjynGoGP&X-Amz-Signature=f80acf95196db9e0a84501437460987c25285f9b90417d06191f796c7a376695&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA6A4SPB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCOocQc0fJqmxERaFUxq7REFEYwEw2mKPRAq13cGEahFgIhANpVT4uupxQ2Z%2FHHVlDYCx%2Flb1cO6glhZDWDHf4fuZU0Kv8DCG4QABoMNjM3NDIzMTgzODA1IgyVCAsYmIPmwdneCxcq3AMCBrGLnD4rz68kEgj997bYIv2Lkd%2FtIPALiqgJYR20Ec%2FlTyM6O%2BALCLxlW4WfG9fz68As%2B%2FRFRQbWsrnxvK54uC4t%2BMNiUaaQOfmmne1W%2BDhyuHRoof%2Fb86d%2FFTCx3fCb3MhLESWpSjrRXDrqWDudRl5Cwts6CyArqxKG5tEv5QKZe1%2FAgbDEllQNz%2FNF6NdTs7fmff3HOo4I8S5d4QTSXrV3QeoZwUzPbUfpp6DvoiU2G3oOKxSctndwOsgMv36OedHDD9lnn5alQ1vc%2FX5CtMAe70htt7%2F%2FAiWv1CChFGwQ2wcNzDyvfPbn55vF5S8aAMc0MIM26riIyu8JguH%2BmHASfbK1QEy9BAcqYIPaePfEiGM1ungO0cMMhUeIkQ%2BsgNyAxiKJnVJQvpqwy9mDcMVGOgLHIH24VI0QRh8%2BkljAZHh76EnjAJMUTGlG5u6x%2Fwm4YxsSPg8fcy8lE%2Bb1bTOtpamAxDI6kZ3CH8B4QCg2ZVGq1uGI0Q6aGbuOZtTxWTW8kXLjQJYxfjYWQylObuEVVBtfNgW4wQDc3JVOGe96q0Dd1r%2FiDEI%2Fw9ZdxO1TIuf0L%2Bq3fGutGJJcF0W2M%2BWaLL1iMACqn9WYF9Hzk%2FlM7ABGhsTnbWP0ujCXoZa9BjqkAVOdm0DdH1GZIpmjJ3ajdRcDbWV3qyTSag53l5wiQSSOyDpFRR1G0IPd%2Bt7GhmZkJuJeGjIeHS6QYyNGuy21J7AwekFWEXe6K75Hzu7ldiKxm1YGrs5ed%2BbRg3OMfxVokIcFcC7GVfvc6oOwhi%2By2OI5oouqAwqb5bAUpQ5m%2B67kqArJUi4iflA4cZWXNx2yzxqXnK2bfM5WEqSbwst8WArn3RvP&X-Amz-Signature=96dcce54cbfc880a1afb2511f8c18ab8819a7940505b230a4c980305d4bd643c&X-Amz-SignedHeaders=host&x-id=GetObject)
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