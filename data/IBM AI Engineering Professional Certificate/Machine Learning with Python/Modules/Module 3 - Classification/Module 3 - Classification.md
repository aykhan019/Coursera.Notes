

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KQ7US4W%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIDd1S96MDHxka56KehuvMWQajKbjtQq5yJuiQbScVsy2AiEA1RCdxUQAZm5XQpzSDZKo9Bf2BdSuZCOMkqJTQGq7CLQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDJjNUY7qr8m2ncP%2FECrcAypsuK6uFYdcaCV7SSl4K7tGnM2MOKEpzYA1RGB3kOHot%2FO9IjpB1IdS3Q6flI%2FQ8qm4S1DyeKyrzLQAtrkit%2Fvo6IORaB4KOPd2IJzDrP1vNK9NaUVr2gw5xLhUmCqUQ%2B7bbdEqxkhF4kxG0d4GFwdaJoEQwFL79%2BB177M%2FRc1Nj%2BUV3k%2Fen1txSZEFEUop193TZ7WYGsq8ShHW6Sccd0PQapMBD6MmCB2mVbcMCHdPQWG20Ynv3laxOfjdE9kHZdCKBzXN4wEmq8HKGjnd4imnD5C6F0KcH3Oav9lmbMlOlp3JP9vQ6PdNwlzwq4Tt8wtM44PIRfjSQHb124zazGaSqwyoADCd2SNqj8j14u8Zar1i43uVVAmY%2FjHm4OllLRcVK3pIS2fwfAsYLO20coysOWCqBTGz1ldmrufv7PuKFyWim%2BHxqQtkDxomVZI60bSYCX2QUtyYZ785heel1bfrJc6GjE%2B5uagSOpx0YcbEYdwbUyxiA31XlIR1WTYeqFfvy0MnOe3vjpSRQ0WnVOlomKCGMSKhkPwi5q%2Bwxw8VXOlU9quw%2BJuYJyT9dO73JvHoAhwD2%2Bm6b2R6tr0QBTozvon5sHaWUUmTU%2FYXxhZmLPWTYUTGsBzPiNoWMPC6jr0GOqUB7%2FDRHuQCGCg4gap5P4CYRlPv2pC0PSTLM0FVUBJ8%2BV77W7BSjUFT5YwsP%2FIEGtCDaZQvPRvZ859l3doQSq%2FoD4%2BMnFXCqty%2FRKYJry6tz9bt0l0%2Bzsxk%2BPPzsHAbpFnoQDnE9lxyxp6OG4dn2mQzbTK2ji3RTBVLqivrdyBJE0DG1EKhlgIFpCVXrZtDScLkcElTUy7gjepkoTVq9ytzi6Tj7xyA&X-Amz-Signature=db3129b2e4914b298e02ac28ee1793eaa5cc7b62bb850d9bd72b6cf282c29cf0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KQ7US4W%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIDd1S96MDHxka56KehuvMWQajKbjtQq5yJuiQbScVsy2AiEA1RCdxUQAZm5XQpzSDZKo9Bf2BdSuZCOMkqJTQGq7CLQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDJjNUY7qr8m2ncP%2FECrcAypsuK6uFYdcaCV7SSl4K7tGnM2MOKEpzYA1RGB3kOHot%2FO9IjpB1IdS3Q6flI%2FQ8qm4S1DyeKyrzLQAtrkit%2Fvo6IORaB4KOPd2IJzDrP1vNK9NaUVr2gw5xLhUmCqUQ%2B7bbdEqxkhF4kxG0d4GFwdaJoEQwFL79%2BB177M%2FRc1Nj%2BUV3k%2Fen1txSZEFEUop193TZ7WYGsq8ShHW6Sccd0PQapMBD6MmCB2mVbcMCHdPQWG20Ynv3laxOfjdE9kHZdCKBzXN4wEmq8HKGjnd4imnD5C6F0KcH3Oav9lmbMlOlp3JP9vQ6PdNwlzwq4Tt8wtM44PIRfjSQHb124zazGaSqwyoADCd2SNqj8j14u8Zar1i43uVVAmY%2FjHm4OllLRcVK3pIS2fwfAsYLO20coysOWCqBTGz1ldmrufv7PuKFyWim%2BHxqQtkDxomVZI60bSYCX2QUtyYZ785heel1bfrJc6GjE%2B5uagSOpx0YcbEYdwbUyxiA31XlIR1WTYeqFfvy0MnOe3vjpSRQ0WnVOlomKCGMSKhkPwi5q%2Bwxw8VXOlU9quw%2BJuYJyT9dO73JvHoAhwD2%2Bm6b2R6tr0QBTozvon5sHaWUUmTU%2FYXxhZmLPWTYUTGsBzPiNoWMPC6jr0GOqUB7%2FDRHuQCGCg4gap5P4CYRlPv2pC0PSTLM0FVUBJ8%2BV77W7BSjUFT5YwsP%2FIEGtCDaZQvPRvZ859l3doQSq%2FoD4%2BMnFXCqty%2FRKYJry6tz9bt0l0%2Bzsxk%2BPPzsHAbpFnoQDnE9lxyxp6OG4dn2mQzbTK2ji3RTBVLqivrdyBJE0DG1EKhlgIFpCVXrZtDScLkcElTUy7gjepkoTVq9ytzi6Tj7xyA&X-Amz-Signature=21483361bba0e86d069c0ce5adb8e382793245aea87e87270dda23c9079308f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KQ7US4W%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIDd1S96MDHxka56KehuvMWQajKbjtQq5yJuiQbScVsy2AiEA1RCdxUQAZm5XQpzSDZKo9Bf2BdSuZCOMkqJTQGq7CLQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDJjNUY7qr8m2ncP%2FECrcAypsuK6uFYdcaCV7SSl4K7tGnM2MOKEpzYA1RGB3kOHot%2FO9IjpB1IdS3Q6flI%2FQ8qm4S1DyeKyrzLQAtrkit%2Fvo6IORaB4KOPd2IJzDrP1vNK9NaUVr2gw5xLhUmCqUQ%2B7bbdEqxkhF4kxG0d4GFwdaJoEQwFL79%2BB177M%2FRc1Nj%2BUV3k%2Fen1txSZEFEUop193TZ7WYGsq8ShHW6Sccd0PQapMBD6MmCB2mVbcMCHdPQWG20Ynv3laxOfjdE9kHZdCKBzXN4wEmq8HKGjnd4imnD5C6F0KcH3Oav9lmbMlOlp3JP9vQ6PdNwlzwq4Tt8wtM44PIRfjSQHb124zazGaSqwyoADCd2SNqj8j14u8Zar1i43uVVAmY%2FjHm4OllLRcVK3pIS2fwfAsYLO20coysOWCqBTGz1ldmrufv7PuKFyWim%2BHxqQtkDxomVZI60bSYCX2QUtyYZ785heel1bfrJc6GjE%2B5uagSOpx0YcbEYdwbUyxiA31XlIR1WTYeqFfvy0MnOe3vjpSRQ0WnVOlomKCGMSKhkPwi5q%2Bwxw8VXOlU9quw%2BJuYJyT9dO73JvHoAhwD2%2Bm6b2R6tr0QBTozvon5sHaWUUmTU%2FYXxhZmLPWTYUTGsBzPiNoWMPC6jr0GOqUB7%2FDRHuQCGCg4gap5P4CYRlPv2pC0PSTLM0FVUBJ8%2BV77W7BSjUFT5YwsP%2FIEGtCDaZQvPRvZ859l3doQSq%2FoD4%2BMnFXCqty%2FRKYJry6tz9bt0l0%2Bzsxk%2BPPzsHAbpFnoQDnE9lxyxp6OG4dn2mQzbTK2ji3RTBVLqivrdyBJE0DG1EKhlgIFpCVXrZtDScLkcElTUy7gjepkoTVq9ytzi6Tj7xyA&X-Amz-Signature=946069ba6b7c5f7f88719cb34265f403f1afeca3f692b62616c88b92abcc79c5&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DXJKRHI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIFaGUF0xb0rTXqzxtiiL9edJMuO9zmTBSBDnU32qmT0aAiEAttUYF%2FEdVenVauOM0R8m1HczgxLMt9%2FeEmUYFYN%2FZQwq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDCHRvlRHLNg%2Fj5WxMSrcA6ZSK35QWhQtRCyWNjs3dAmD5mG96ugSL4doiETc2Hvh%2FKKs0IItv3nBH0U6b5x7nLcd09NR161b%2FaP0gw%2BNwc8KmDapr06J1k%2BA2kYdmGOInAFVsPRuK7yrbf9JIXepWcmxbpNU2k549FbDhj%2Fldb%2BhjSglrhnK2SazqvOqb6sSXBSipz9O3RG9e2CQuXH6YjgPib9Kjtoah9O0BzNXgBy5teAKEefMX9NXxtDlVenB8PfTkQ2gCY1WBhS7%2BDYXmbeGRlVYvKhSsyF4IwJKkS3Ml7vV2IRGb1q3o1rgSq3wQK0hSNA6h1H9tHU3nql0dJjQD30BqRrJ54%2BLzEFHVp9mMPW9cJvLeaxHEd4DDRIrQH29MZyyN%2BoHNDY%2BDHpJ3nheI3XEJKDFlazKqJzw6CmLvmYQ17%2B6pDvu8HdX82TodrZPhDhtZolpZ%2FuKWlVpg2aOzyl%2Br8I8bA3xadVOzKbzkJmp%2BwW6dOolxOqHJUyKP%2BxDSvDrObAs0a9WaAOJRRKTMWT%2FLiy1aJQQoc5vKIkYLiDHdjypDFPRx9ypns3Nyf0jyCs2A9dgn47v4OrkbcLjb9CPnGex4sbHhLZNYCoNZ9MDNiFGkZqwQ3LEAnVZjwBduW9yLFgjJniPMJe6jr0GOqUBzll92rwXD9UQDP4TU4pD%2B3tYKHtfBlE6x%2BG%2F4jnlJh%2F5xhEiN3vK1Ze5OvFuJFI4UnlwkPBJ6IKSD1bXdVtV8ASseTkSHhhJrJOmYQmGBBiARub5MgKij6LWjPTYSo2Z8iw0qfA6Y1eUI7umrj0vlwTTu9Z5nfwR%2B3dU1ZCbNOLhbABezj%2FoMRtthCCwzWppuq3XERqdi6P3LgAR0yVapU3fUiuv&X-Amz-Signature=2d673c8996f007b200be6f52bdd2412e928954172be583ff68c3f012ea5564f3&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DXJKRHI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIFaGUF0xb0rTXqzxtiiL9edJMuO9zmTBSBDnU32qmT0aAiEAttUYF%2FEdVenVauOM0R8m1HczgxLMt9%2FeEmUYFYN%2FZQwq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDCHRvlRHLNg%2Fj5WxMSrcA6ZSK35QWhQtRCyWNjs3dAmD5mG96ugSL4doiETc2Hvh%2FKKs0IItv3nBH0U6b5x7nLcd09NR161b%2FaP0gw%2BNwc8KmDapr06J1k%2BA2kYdmGOInAFVsPRuK7yrbf9JIXepWcmxbpNU2k549FbDhj%2Fldb%2BhjSglrhnK2SazqvOqb6sSXBSipz9O3RG9e2CQuXH6YjgPib9Kjtoah9O0BzNXgBy5teAKEefMX9NXxtDlVenB8PfTkQ2gCY1WBhS7%2BDYXmbeGRlVYvKhSsyF4IwJKkS3Ml7vV2IRGb1q3o1rgSq3wQK0hSNA6h1H9tHU3nql0dJjQD30BqRrJ54%2BLzEFHVp9mMPW9cJvLeaxHEd4DDRIrQH29MZyyN%2BoHNDY%2BDHpJ3nheI3XEJKDFlazKqJzw6CmLvmYQ17%2B6pDvu8HdX82TodrZPhDhtZolpZ%2FuKWlVpg2aOzyl%2Br8I8bA3xadVOzKbzkJmp%2BwW6dOolxOqHJUyKP%2BxDSvDrObAs0a9WaAOJRRKTMWT%2FLiy1aJQQoc5vKIkYLiDHdjypDFPRx9ypns3Nyf0jyCs2A9dgn47v4OrkbcLjb9CPnGex4sbHhLZNYCoNZ9MDNiFGkZqwQ3LEAnVZjwBduW9yLFgjJniPMJe6jr0GOqUBzll92rwXD9UQDP4TU4pD%2B3tYKHtfBlE6x%2BG%2F4jnlJh%2F5xhEiN3vK1Ze5OvFuJFI4UnlwkPBJ6IKSD1bXdVtV8ASseTkSHhhJrJOmYQmGBBiARub5MgKij6LWjPTYSo2Z8iw0qfA6Y1eUI7umrj0vlwTTu9Z5nfwR%2B3dU1ZCbNOLhbABezj%2FoMRtthCCwzWppuq3XERqdi6P3LgAR0yVapU3fUiuv&X-Amz-Signature=6f422b5cc9ba57b58ec78840b809737b39806b2933d6602f61f5be19d4c7196b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KQ7US4W%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIDd1S96MDHxka56KehuvMWQajKbjtQq5yJuiQbScVsy2AiEA1RCdxUQAZm5XQpzSDZKo9Bf2BdSuZCOMkqJTQGq7CLQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDJjNUY7qr8m2ncP%2FECrcAypsuK6uFYdcaCV7SSl4K7tGnM2MOKEpzYA1RGB3kOHot%2FO9IjpB1IdS3Q6flI%2FQ8qm4S1DyeKyrzLQAtrkit%2Fvo6IORaB4KOPd2IJzDrP1vNK9NaUVr2gw5xLhUmCqUQ%2B7bbdEqxkhF4kxG0d4GFwdaJoEQwFL79%2BB177M%2FRc1Nj%2BUV3k%2Fen1txSZEFEUop193TZ7WYGsq8ShHW6Sccd0PQapMBD6MmCB2mVbcMCHdPQWG20Ynv3laxOfjdE9kHZdCKBzXN4wEmq8HKGjnd4imnD5C6F0KcH3Oav9lmbMlOlp3JP9vQ6PdNwlzwq4Tt8wtM44PIRfjSQHb124zazGaSqwyoADCd2SNqj8j14u8Zar1i43uVVAmY%2FjHm4OllLRcVK3pIS2fwfAsYLO20coysOWCqBTGz1ldmrufv7PuKFyWim%2BHxqQtkDxomVZI60bSYCX2QUtyYZ785heel1bfrJc6GjE%2B5uagSOpx0YcbEYdwbUyxiA31XlIR1WTYeqFfvy0MnOe3vjpSRQ0WnVOlomKCGMSKhkPwi5q%2Bwxw8VXOlU9quw%2BJuYJyT9dO73JvHoAhwD2%2Bm6b2R6tr0QBTozvon5sHaWUUmTU%2FYXxhZmLPWTYUTGsBzPiNoWMPC6jr0GOqUB7%2FDRHuQCGCg4gap5P4CYRlPv2pC0PSTLM0FVUBJ8%2BV77W7BSjUFT5YwsP%2FIEGtCDaZQvPRvZ859l3doQSq%2FoD4%2BMnFXCqty%2FRKYJry6tz9bt0l0%2Bzsxk%2BPPzsHAbpFnoQDnE9lxyxp6OG4dn2mQzbTK2ji3RTBVLqivrdyBJE0DG1EKhlgIFpCVXrZtDScLkcElTUy7gjepkoTVq9ytzi6Tj7xyA&X-Amz-Signature=fa80bd411ddb649ce47d6bdf9aa945dc425e8c9ae818b3f93e48859faf643db8&X-Amz-SignedHeaders=host&x-id=GetObject)
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