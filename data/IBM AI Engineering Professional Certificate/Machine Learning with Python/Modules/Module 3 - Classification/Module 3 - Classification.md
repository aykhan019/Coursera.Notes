

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLKIVZX5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDZGz0WMN%2F77jnjVUlFUWwrha4kr90jX%2Bm4nWiBc%2BvX7QIhAKJvRfzybykDZtH0sFyk%2FnpPL%2Bbcx8eiKvdlp2Dzzsp6Kv8DCB8QABoMNjM3NDIzMTgzODA1Igx9pcOO7wu6wHH4twMq3AMwMPxWIPY9B51uEL1Ndmwl3D%2BPHDKe2X8OWvDwk0wQ9lU5U1GyL4DwJAlpUitS0fXXTzF06fCbOvVkFZSa9ZW0hC3sNyhEq%2F%2FrlbNiCLfGhMLpkdv7rHOfVG7LTKRKdWfvxfyMOSP%2FkhrAQEnLIDL8faZGZkvj8o8snl6G394AcFLHXBI0kMCgA9LG%2Bhc983PKEsrNt1NlklqqHv%2Fjyvde39WSU5nPZdsr6C2ddaUu2P4NOe1XYbc%2Fx80hVgKclOSC442cw5nAWWQcNqC4MoNHP5%2BRZKcZsN8tZwc8muWkEA9ingRm8hGkZkB2kw5k3EJ5JyISmioRKxEUTla3UFD0HISHoR2EY9KjIJnyY5pU4LKwAY5ZE2ILclmtZ9EWzdUTr66Ajiio2VoX%2Bpa08qUN4sr%2FQ%2F0hPznTJtffQEmhgzwA7aLKEJ9fPWlleXYE4pqYqmg%2BA0swMl8YBp7M6ocS%2B9Xb6BFdQSicIwnd4ttdvJMVctVLL9%2BZK8cgpi4Oohvhgoss8gM3NRXSKoroE7s0qFyaj2FgcESYq1Y5GYQGlrlB0AwCFrKBAbgN3CMTQlJd1HkR2wWLWG5fI8h3x7aAX8waqgJvbfor4mqnnmEAuNYz1Z9bjGJMOB9bfzCq94S9BjqkAY0g6xWo9ngP0lzoaFaS4czir4zm0Pn6ucAFzen65VqSZW1SI%2BHrqepPYaIOCfi2bzBb00Ek%2Baz0BN5plCJgh4IBL%2FYHj6PeLnh%2FxexW2JspyTbUqFSBGHG9%2BOxPLplbsuqKxg8rCo3Qeyh3kELUqdS1VCh7i3vUEaYyU7%2FRYJEkSyv9ELd6HiwTMDuKivQKbbIojin%2BXcKEdQ0EBS7A5a7E8Kyn&X-Amz-Signature=18e95bc20a76151c8d9db4d398c2cc68c588f59019a0e75a245005c10b933ad6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLKIVZX5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDZGz0WMN%2F77jnjVUlFUWwrha4kr90jX%2Bm4nWiBc%2BvX7QIhAKJvRfzybykDZtH0sFyk%2FnpPL%2Bbcx8eiKvdlp2Dzzsp6Kv8DCB8QABoMNjM3NDIzMTgzODA1Igx9pcOO7wu6wHH4twMq3AMwMPxWIPY9B51uEL1Ndmwl3D%2BPHDKe2X8OWvDwk0wQ9lU5U1GyL4DwJAlpUitS0fXXTzF06fCbOvVkFZSa9ZW0hC3sNyhEq%2F%2FrlbNiCLfGhMLpkdv7rHOfVG7LTKRKdWfvxfyMOSP%2FkhrAQEnLIDL8faZGZkvj8o8snl6G394AcFLHXBI0kMCgA9LG%2Bhc983PKEsrNt1NlklqqHv%2Fjyvde39WSU5nPZdsr6C2ddaUu2P4NOe1XYbc%2Fx80hVgKclOSC442cw5nAWWQcNqC4MoNHP5%2BRZKcZsN8tZwc8muWkEA9ingRm8hGkZkB2kw5k3EJ5JyISmioRKxEUTla3UFD0HISHoR2EY9KjIJnyY5pU4LKwAY5ZE2ILclmtZ9EWzdUTr66Ajiio2VoX%2Bpa08qUN4sr%2FQ%2F0hPznTJtffQEmhgzwA7aLKEJ9fPWlleXYE4pqYqmg%2BA0swMl8YBp7M6ocS%2B9Xb6BFdQSicIwnd4ttdvJMVctVLL9%2BZK8cgpi4Oohvhgoss8gM3NRXSKoroE7s0qFyaj2FgcESYq1Y5GYQGlrlB0AwCFrKBAbgN3CMTQlJd1HkR2wWLWG5fI8h3x7aAX8waqgJvbfor4mqnnmEAuNYz1Z9bjGJMOB9bfzCq94S9BjqkAY0g6xWo9ngP0lzoaFaS4czir4zm0Pn6ucAFzen65VqSZW1SI%2BHrqepPYaIOCfi2bzBb00Ek%2Baz0BN5plCJgh4IBL%2FYHj6PeLnh%2FxexW2JspyTbUqFSBGHG9%2BOxPLplbsuqKxg8rCo3Qeyh3kELUqdS1VCh7i3vUEaYyU7%2FRYJEkSyv9ELd6HiwTMDuKivQKbbIojin%2BXcKEdQ0EBS7A5a7E8Kyn&X-Amz-Signature=c29805b372dc9ec97eeceb9fe6d88e60f2964f3007e46be773d1dedd293eaaa6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLKIVZX5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDZGz0WMN%2F77jnjVUlFUWwrha4kr90jX%2Bm4nWiBc%2BvX7QIhAKJvRfzybykDZtH0sFyk%2FnpPL%2Bbcx8eiKvdlp2Dzzsp6Kv8DCB8QABoMNjM3NDIzMTgzODA1Igx9pcOO7wu6wHH4twMq3AMwMPxWIPY9B51uEL1Ndmwl3D%2BPHDKe2X8OWvDwk0wQ9lU5U1GyL4DwJAlpUitS0fXXTzF06fCbOvVkFZSa9ZW0hC3sNyhEq%2F%2FrlbNiCLfGhMLpkdv7rHOfVG7LTKRKdWfvxfyMOSP%2FkhrAQEnLIDL8faZGZkvj8o8snl6G394AcFLHXBI0kMCgA9LG%2Bhc983PKEsrNt1NlklqqHv%2Fjyvde39WSU5nPZdsr6C2ddaUu2P4NOe1XYbc%2Fx80hVgKclOSC442cw5nAWWQcNqC4MoNHP5%2BRZKcZsN8tZwc8muWkEA9ingRm8hGkZkB2kw5k3EJ5JyISmioRKxEUTla3UFD0HISHoR2EY9KjIJnyY5pU4LKwAY5ZE2ILclmtZ9EWzdUTr66Ajiio2VoX%2Bpa08qUN4sr%2FQ%2F0hPznTJtffQEmhgzwA7aLKEJ9fPWlleXYE4pqYqmg%2BA0swMl8YBp7M6ocS%2B9Xb6BFdQSicIwnd4ttdvJMVctVLL9%2BZK8cgpi4Oohvhgoss8gM3NRXSKoroE7s0qFyaj2FgcESYq1Y5GYQGlrlB0AwCFrKBAbgN3CMTQlJd1HkR2wWLWG5fI8h3x7aAX8waqgJvbfor4mqnnmEAuNYz1Z9bjGJMOB9bfzCq94S9BjqkAY0g6xWo9ngP0lzoaFaS4czir4zm0Pn6ucAFzen65VqSZW1SI%2BHrqepPYaIOCfi2bzBb00Ek%2Baz0BN5plCJgh4IBL%2FYHj6PeLnh%2FxexW2JspyTbUqFSBGHG9%2BOxPLplbsuqKxg8rCo3Qeyh3kELUqdS1VCh7i3vUEaYyU7%2FRYJEkSyv9ELd6HiwTMDuKivQKbbIojin%2BXcKEdQ0EBS7A5a7E8Kyn&X-Amz-Signature=4fd12bee5cf2941936330db5656fa521bcee862a692c2008c19f9d1020643da4&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQRV7HMM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDQKqlwCaeXkh4%2FWKJy%2B5E0K9rqimmGAIWLeEw4etTRTAIgWcfEATmN1L4dsbKSjmLZOnw6prwm3VCbNHTC1kRHiXsq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDOiPc%2Fxojl3LhARjeircA4FpBJKK%2BR9rASkysHJr%2FEcujjjqhZosNbBUo5z%2FWx2JTOD0Zc1HS5TGSNlnth%2FHlOLX3HlA%2BPzl9owykDvRrTHnVn%2FSmjH4Wr8pbaWqbyMS2VgH6gKRaICj02kOdjPTvzjAzqejjYXD6mpG0whPST72C8WdNCMfOCmLRF5rFUB1UYjDAJWJkcUc4y5jctJ%2B2w6H0abOjTcC3TR17dajCkFM0JtM2KzOoTdGl0%2FpRrm5509kfwtftmWABTD3hOZDSFP%2FI3LrlSu1cYp5j2N7dNLXSXXlvxYJ4RhZ1Lkfh%2Fy8RrLvgE9aPwiAepX8zcMMnRdW1tIYg1l8OzqIfoeN41fK%2BOOAjK8ftbeWHtkl%2FO26S3BJT6TW%2BNxOEfLnN17bubIzSiZqbmtSxnunZlffN8YgOToYQnGziqDSoAcqqNp6PZNrjciuO7qI1W7GNO7j9QkbSQHx5my23VE69BNZ8fVmBfRMNXo%2Bqjp1c%2B0itezMmLqO6M%2FeApIjYqtAuDIcMx0VmrfTTs8oO9xkAf1wq%2FAvoqDwqAdpSpHAY8RCQuun%2B9V44Bl16I0uzWgrrekJeimP4w5lZfqVIVWdYli6L2TFyEpsaI6RnxJyyDxq4w%2BZwvUiIqQCo2gaELccMIj3hL0GOqUB7lvlBlMKuXbwaKYQ1HkrRzWJqoTQI1pKx9b1xysFezXQBL5nl3N9GG7LUQQWKXnaze9j4uOq5y48uI65xPtSfXZ2llryU3y8gYk2HovSUezPwSiofu0UdINqyJgUBQ189Vodb7zCSA%2BYrF8SUYJuVVe77fiENNfCiiCYa%2FRYGl7LX79o0u8NLtat%2FAX4cNHSuHSIlmYD1ldmHkh2pB%2FXjOWtzhm0&X-Amz-Signature=e5df1e7d3b68f978de7167315c4084206512f605b169cdd0eb11490bf734bda6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQRV7HMM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDQKqlwCaeXkh4%2FWKJy%2B5E0K9rqimmGAIWLeEw4etTRTAIgWcfEATmN1L4dsbKSjmLZOnw6prwm3VCbNHTC1kRHiXsq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDOiPc%2Fxojl3LhARjeircA4FpBJKK%2BR9rASkysHJr%2FEcujjjqhZosNbBUo5z%2FWx2JTOD0Zc1HS5TGSNlnth%2FHlOLX3HlA%2BPzl9owykDvRrTHnVn%2FSmjH4Wr8pbaWqbyMS2VgH6gKRaICj02kOdjPTvzjAzqejjYXD6mpG0whPST72C8WdNCMfOCmLRF5rFUB1UYjDAJWJkcUc4y5jctJ%2B2w6H0abOjTcC3TR17dajCkFM0JtM2KzOoTdGl0%2FpRrm5509kfwtftmWABTD3hOZDSFP%2FI3LrlSu1cYp5j2N7dNLXSXXlvxYJ4RhZ1Lkfh%2Fy8RrLvgE9aPwiAepX8zcMMnRdW1tIYg1l8OzqIfoeN41fK%2BOOAjK8ftbeWHtkl%2FO26S3BJT6TW%2BNxOEfLnN17bubIzSiZqbmtSxnunZlffN8YgOToYQnGziqDSoAcqqNp6PZNrjciuO7qI1W7GNO7j9QkbSQHx5my23VE69BNZ8fVmBfRMNXo%2Bqjp1c%2B0itezMmLqO6M%2FeApIjYqtAuDIcMx0VmrfTTs8oO9xkAf1wq%2FAvoqDwqAdpSpHAY8RCQuun%2B9V44Bl16I0uzWgrrekJeimP4w5lZfqVIVWdYli6L2TFyEpsaI6RnxJyyDxq4w%2BZwvUiIqQCo2gaELccMIj3hL0GOqUB7lvlBlMKuXbwaKYQ1HkrRzWJqoTQI1pKx9b1xysFezXQBL5nl3N9GG7LUQQWKXnaze9j4uOq5y48uI65xPtSfXZ2llryU3y8gYk2HovSUezPwSiofu0UdINqyJgUBQ189Vodb7zCSA%2BYrF8SUYJuVVe77fiENNfCiiCYa%2FRYGl7LX79o0u8NLtat%2FAX4cNHSuHSIlmYD1ldmHkh2pB%2FXjOWtzhm0&X-Amz-Signature=6ef4fb21a1ee10419081a36e5f7f890304d310fd54743ac32c6dfe96191a7d08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLKIVZX5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDZGz0WMN%2F77jnjVUlFUWwrha4kr90jX%2Bm4nWiBc%2BvX7QIhAKJvRfzybykDZtH0sFyk%2FnpPL%2Bbcx8eiKvdlp2Dzzsp6Kv8DCB8QABoMNjM3NDIzMTgzODA1Igx9pcOO7wu6wHH4twMq3AMwMPxWIPY9B51uEL1Ndmwl3D%2BPHDKe2X8OWvDwk0wQ9lU5U1GyL4DwJAlpUitS0fXXTzF06fCbOvVkFZSa9ZW0hC3sNyhEq%2F%2FrlbNiCLfGhMLpkdv7rHOfVG7LTKRKdWfvxfyMOSP%2FkhrAQEnLIDL8faZGZkvj8o8snl6G394AcFLHXBI0kMCgA9LG%2Bhc983PKEsrNt1NlklqqHv%2Fjyvde39WSU5nPZdsr6C2ddaUu2P4NOe1XYbc%2Fx80hVgKclOSC442cw5nAWWQcNqC4MoNHP5%2BRZKcZsN8tZwc8muWkEA9ingRm8hGkZkB2kw5k3EJ5JyISmioRKxEUTla3UFD0HISHoR2EY9KjIJnyY5pU4LKwAY5ZE2ILclmtZ9EWzdUTr66Ajiio2VoX%2Bpa08qUN4sr%2FQ%2F0hPznTJtffQEmhgzwA7aLKEJ9fPWlleXYE4pqYqmg%2BA0swMl8YBp7M6ocS%2B9Xb6BFdQSicIwnd4ttdvJMVctVLL9%2BZK8cgpi4Oohvhgoss8gM3NRXSKoroE7s0qFyaj2FgcESYq1Y5GYQGlrlB0AwCFrKBAbgN3CMTQlJd1HkR2wWLWG5fI8h3x7aAX8waqgJvbfor4mqnnmEAuNYz1Z9bjGJMOB9bfzCq94S9BjqkAY0g6xWo9ngP0lzoaFaS4czir4zm0Pn6ucAFzen65VqSZW1SI%2BHrqepPYaIOCfi2bzBb00Ek%2Baz0BN5plCJgh4IBL%2FYHj6PeLnh%2FxexW2JspyTbUqFSBGHG9%2BOxPLplbsuqKxg8rCo3Qeyh3kELUqdS1VCh7i3vUEaYyU7%2FRYJEkSyv9ELd6HiwTMDuKivQKbbIojin%2BXcKEdQ0EBS7A5a7E8Kyn&X-Amz-Signature=d377122329f7430e3c98944da1c369fa178bba5f0e3efb190e0a0c1e10a90339&X-Amz-SignedHeaders=host&x-id=GetObject)
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