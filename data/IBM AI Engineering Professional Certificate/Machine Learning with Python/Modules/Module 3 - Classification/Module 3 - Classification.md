

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTG6VBRQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXHaHBbRrjZ4eZljz11KtKFEhve45erezKd3DHbsqFRwIhAKrAwB3rFoFopAebF3DJvos3mpk6RYGEeOFz2%2FbBUrkOKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igykg1Qjo87jbDKiijAq3AP4Q6OHFbKeA%2F2S75NO4yGVM7IjVLua0ZNMR9YRsRyOYZviQEmsO%2FqMIxPPo5st0caXbChYxnxyPFumJFgJQ1sWsAAdchvm7QNqYxWfWa%2BNeyGFRcsWo9BOiXcLZsnVIlf27jGpe8bQJQ%2BdTC1XqTrfPpV10IPTAyTCmawdINuR9Z0sr8zXMqSzrxzy%2BXC%2FI9UMGNHVZchOMz3YKarSQ5BMz811USfXC%2FygAwp3DJgewo7a8lzNaDV8leMYuN8V7mXpNShLkX5HVVNO1puvhO%2F1KoXOmzl2KZUpbS8k%2BUQoSN3%2F8bCD0Jiud3mpetLBh%2FWCY%2Bi%2B05wXyTaRvs0lcH5l%2FqRLtW8EQdfKcoBkoy7v67nv0akmr5Vo6bwYoTZc7cvL6rdmCPqXR%2Bv6uh0SgFEpPpL9VfQ7kLwltOEmFZlDxYEtc3KHPlJ3xSF0kuf5r3iOPhnwZJ6NStey5LDFPsLmduJJk%2Fnw1pCy8muasTorbBtRuemh%2FMbtPrRalA0oJO4whYhFwYQXTiu3fS6JLs8IaM%2Fx1aliMdlDJdFywy2%2FzvHsXZds1KjY79xgYhpyEZ0uxXcyfHNQrsUl%2FINzz7ZrYnAd2F7LOQYITz4Zg8RnRfs3dobyGK8CA82jtjDX3fa8BjqkAeGzfYvxAd3W9YOKs%2FfUS9EP82cXQ%2B2LSsvWxDa%2B%2FWVbkU%2BVi0qedod1N8cuGZ1o7Tk%2BjjcRLpgFq67rwb3VqiO52EAsiLeO5FSq1z0vWb9Rd7pDt2MMLnEu81tZJg76ERaJ%2BKMVr6EThnaOOpSMQRLAeQTJB9vFwByRwQoJxmBRHvIvJgbRw5H4KDWN2nvToDWHm7UCTrcl3iK9qbPjCwRBziJi&X-Amz-Signature=e35a50045cc193b7971d63a1bd5ce360da1c149e93ede9951b7e982bdcdc4ba0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTG6VBRQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXHaHBbRrjZ4eZljz11KtKFEhve45erezKd3DHbsqFRwIhAKrAwB3rFoFopAebF3DJvos3mpk6RYGEeOFz2%2FbBUrkOKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igykg1Qjo87jbDKiijAq3AP4Q6OHFbKeA%2F2S75NO4yGVM7IjVLua0ZNMR9YRsRyOYZviQEmsO%2FqMIxPPo5st0caXbChYxnxyPFumJFgJQ1sWsAAdchvm7QNqYxWfWa%2BNeyGFRcsWo9BOiXcLZsnVIlf27jGpe8bQJQ%2BdTC1XqTrfPpV10IPTAyTCmawdINuR9Z0sr8zXMqSzrxzy%2BXC%2FI9UMGNHVZchOMz3YKarSQ5BMz811USfXC%2FygAwp3DJgewo7a8lzNaDV8leMYuN8V7mXpNShLkX5HVVNO1puvhO%2F1KoXOmzl2KZUpbS8k%2BUQoSN3%2F8bCD0Jiud3mpetLBh%2FWCY%2Bi%2B05wXyTaRvs0lcH5l%2FqRLtW8EQdfKcoBkoy7v67nv0akmr5Vo6bwYoTZc7cvL6rdmCPqXR%2Bv6uh0SgFEpPpL9VfQ7kLwltOEmFZlDxYEtc3KHPlJ3xSF0kuf5r3iOPhnwZJ6NStey5LDFPsLmduJJk%2Fnw1pCy8muasTorbBtRuemh%2FMbtPrRalA0oJO4whYhFwYQXTiu3fS6JLs8IaM%2Fx1aliMdlDJdFywy2%2FzvHsXZds1KjY79xgYhpyEZ0uxXcyfHNQrsUl%2FINzz7ZrYnAd2F7LOQYITz4Zg8RnRfs3dobyGK8CA82jtjDX3fa8BjqkAeGzfYvxAd3W9YOKs%2FfUS9EP82cXQ%2B2LSsvWxDa%2B%2FWVbkU%2BVi0qedod1N8cuGZ1o7Tk%2BjjcRLpgFq67rwb3VqiO52EAsiLeO5FSq1z0vWb9Rd7pDt2MMLnEu81tZJg76ERaJ%2BKMVr6EThnaOOpSMQRLAeQTJB9vFwByRwQoJxmBRHvIvJgbRw5H4KDWN2nvToDWHm7UCTrcl3iK9qbPjCwRBziJi&X-Amz-Signature=d62871c6549b1ed1cd71cddd46f4eb6c9193c0520dda0daf60bbeb57380280d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTG6VBRQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXHaHBbRrjZ4eZljz11KtKFEhve45erezKd3DHbsqFRwIhAKrAwB3rFoFopAebF3DJvos3mpk6RYGEeOFz2%2FbBUrkOKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igykg1Qjo87jbDKiijAq3AP4Q6OHFbKeA%2F2S75NO4yGVM7IjVLua0ZNMR9YRsRyOYZviQEmsO%2FqMIxPPo5st0caXbChYxnxyPFumJFgJQ1sWsAAdchvm7QNqYxWfWa%2BNeyGFRcsWo9BOiXcLZsnVIlf27jGpe8bQJQ%2BdTC1XqTrfPpV10IPTAyTCmawdINuR9Z0sr8zXMqSzrxzy%2BXC%2FI9UMGNHVZchOMz3YKarSQ5BMz811USfXC%2FygAwp3DJgewo7a8lzNaDV8leMYuN8V7mXpNShLkX5HVVNO1puvhO%2F1KoXOmzl2KZUpbS8k%2BUQoSN3%2F8bCD0Jiud3mpetLBh%2FWCY%2Bi%2B05wXyTaRvs0lcH5l%2FqRLtW8EQdfKcoBkoy7v67nv0akmr5Vo6bwYoTZc7cvL6rdmCPqXR%2Bv6uh0SgFEpPpL9VfQ7kLwltOEmFZlDxYEtc3KHPlJ3xSF0kuf5r3iOPhnwZJ6NStey5LDFPsLmduJJk%2Fnw1pCy8muasTorbBtRuemh%2FMbtPrRalA0oJO4whYhFwYQXTiu3fS6JLs8IaM%2Fx1aliMdlDJdFywy2%2FzvHsXZds1KjY79xgYhpyEZ0uxXcyfHNQrsUl%2FINzz7ZrYnAd2F7LOQYITz4Zg8RnRfs3dobyGK8CA82jtjDX3fa8BjqkAeGzfYvxAd3W9YOKs%2FfUS9EP82cXQ%2B2LSsvWxDa%2B%2FWVbkU%2BVi0qedod1N8cuGZ1o7Tk%2BjjcRLpgFq67rwb3VqiO52EAsiLeO5FSq1z0vWb9Rd7pDt2MMLnEu81tZJg76ERaJ%2BKMVr6EThnaOOpSMQRLAeQTJB9vFwByRwQoJxmBRHvIvJgbRw5H4KDWN2nvToDWHm7UCTrcl3iK9qbPjCwRBziJi&X-Amz-Signature=3010cfa4eeff47e6bd637eee06e157430b2b8fc2d0c0c0738150a131aa656f38&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPZCSOR4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlRVVHbyJTg0eS%2FaaogL9JEB7EmQfqy24SRvbyhiqoFAiEAxud87FPEjFpelxLd%2BKAH1ojS9%2BJk6mIR5lPDwLjNlJQqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLc1y8CzKus2Ej0ARircA4royDyvWgvFqgSO%2FNJg24ipkMsaan0Rt0ZJZCjlgyIRKvNIE3dNrRZRyld3g%2FK6WKqTUPFlBEwKk5tEJyO5XUvNZzKS2byN%2FMzJdfYFfmzwtlMl6keTefDnWDT8l%2FyEZarXv3CxC4LBd7sNx9fZxtr5Kpd6RYVMfwGNv6BWbhys0rBHBu2Kf0ygSl8sF7AtErWJRM2IWdn0WOKw6O44bE0SrmAThMeCSbStZTWAPCJ9cu%2FdquvLXqepyY7lymN6WV1PlV6qilT3mYe8yd5KXgWUNRETrf6Rq%2BRzgSFzSDQmtfyAPb5GXzXLIGbd6rZ%2B0SlTxB3saYG38zyJ7kvlwuMfEmGTkDt5pX%2FuRHHgL5QsBeNmb3QWlDcinbq%2FS%2FEjU24xPFhjLZopLZdxeOWHwj59wGPK8jzCQE7N7GQJzOzWoOqEjdDJ%2BG9nv2H50F67ytDeUdY9fzBHh1iZd9AJzHtQFH7dGDBxk5VD%2BL2ONRn%2FW19aHC6P66cgnVTA%2FG%2BkxMQCA4VnAHb%2FKboyMmnUHMGeRJjJsoLV9zXXI4I7ZlUfocDs%2FuXSH52i2mN966uPomhUJ%2FJu54rNfje1eIKG3npHk3jiE%2BqdSvmLb7Msisg5dgt4p9fR%2BOCxSENCMMjd9rwGOqUBzoihLdY%2BHwiIki090%2FwruitkjI%2BmjqiXPAgjJAdQhbB0FGuN7WWM%2BKGbKUFrkikqrAH8XPfN3PVuiWw0%2Fodt179yCBUfbD4jrRLGkBBMC61YHVfr0H19%2Fw%2FxLvpqCAK4TD4rlhoOSOOxQ2Mkcd54F30%2BEdDFNfHgp2gN50jITdCswWger6WkjAPoKVKGwdXBSRbhwDFgb6%2FL%2B075A71gMNsroJEv&X-Amz-Signature=1ab59ef3ed558ef3225a0185cf699cac35a9987cbc4683a3075afff8480a17c7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPZCSOR4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlRVVHbyJTg0eS%2FaaogL9JEB7EmQfqy24SRvbyhiqoFAiEAxud87FPEjFpelxLd%2BKAH1ojS9%2BJk6mIR5lPDwLjNlJQqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLc1y8CzKus2Ej0ARircA4royDyvWgvFqgSO%2FNJg24ipkMsaan0Rt0ZJZCjlgyIRKvNIE3dNrRZRyld3g%2FK6WKqTUPFlBEwKk5tEJyO5XUvNZzKS2byN%2FMzJdfYFfmzwtlMl6keTefDnWDT8l%2FyEZarXv3CxC4LBd7sNx9fZxtr5Kpd6RYVMfwGNv6BWbhys0rBHBu2Kf0ygSl8sF7AtErWJRM2IWdn0WOKw6O44bE0SrmAThMeCSbStZTWAPCJ9cu%2FdquvLXqepyY7lymN6WV1PlV6qilT3mYe8yd5KXgWUNRETrf6Rq%2BRzgSFzSDQmtfyAPb5GXzXLIGbd6rZ%2B0SlTxB3saYG38zyJ7kvlwuMfEmGTkDt5pX%2FuRHHgL5QsBeNmb3QWlDcinbq%2FS%2FEjU24xPFhjLZopLZdxeOWHwj59wGPK8jzCQE7N7GQJzOzWoOqEjdDJ%2BG9nv2H50F67ytDeUdY9fzBHh1iZd9AJzHtQFH7dGDBxk5VD%2BL2ONRn%2FW19aHC6P66cgnVTA%2FG%2BkxMQCA4VnAHb%2FKboyMmnUHMGeRJjJsoLV9zXXI4I7ZlUfocDs%2FuXSH52i2mN966uPomhUJ%2FJu54rNfje1eIKG3npHk3jiE%2BqdSvmLb7Msisg5dgt4p9fR%2BOCxSENCMMjd9rwGOqUBzoihLdY%2BHwiIki090%2FwruitkjI%2BmjqiXPAgjJAdQhbB0FGuN7WWM%2BKGbKUFrkikqrAH8XPfN3PVuiWw0%2Fodt179yCBUfbD4jrRLGkBBMC61YHVfr0H19%2Fw%2FxLvpqCAK4TD4rlhoOSOOxQ2Mkcd54F30%2BEdDFNfHgp2gN50jITdCswWger6WkjAPoKVKGwdXBSRbhwDFgb6%2FL%2B075A71gMNsroJEv&X-Amz-Signature=959c7a55ce09b8a150ec2824ec6fc55a5bdec4ebd1108023ad379a15bbc4f68d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTG6VBRQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXHaHBbRrjZ4eZljz11KtKFEhve45erezKd3DHbsqFRwIhAKrAwB3rFoFopAebF3DJvos3mpk6RYGEeOFz2%2FbBUrkOKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igykg1Qjo87jbDKiijAq3AP4Q6OHFbKeA%2F2S75NO4yGVM7IjVLua0ZNMR9YRsRyOYZviQEmsO%2FqMIxPPo5st0caXbChYxnxyPFumJFgJQ1sWsAAdchvm7QNqYxWfWa%2BNeyGFRcsWo9BOiXcLZsnVIlf27jGpe8bQJQ%2BdTC1XqTrfPpV10IPTAyTCmawdINuR9Z0sr8zXMqSzrxzy%2BXC%2FI9UMGNHVZchOMz3YKarSQ5BMz811USfXC%2FygAwp3DJgewo7a8lzNaDV8leMYuN8V7mXpNShLkX5HVVNO1puvhO%2F1KoXOmzl2KZUpbS8k%2BUQoSN3%2F8bCD0Jiud3mpetLBh%2FWCY%2Bi%2B05wXyTaRvs0lcH5l%2FqRLtW8EQdfKcoBkoy7v67nv0akmr5Vo6bwYoTZc7cvL6rdmCPqXR%2Bv6uh0SgFEpPpL9VfQ7kLwltOEmFZlDxYEtc3KHPlJ3xSF0kuf5r3iOPhnwZJ6NStey5LDFPsLmduJJk%2Fnw1pCy8muasTorbBtRuemh%2FMbtPrRalA0oJO4whYhFwYQXTiu3fS6JLs8IaM%2Fx1aliMdlDJdFywy2%2FzvHsXZds1KjY79xgYhpyEZ0uxXcyfHNQrsUl%2FINzz7ZrYnAd2F7LOQYITz4Zg8RnRfs3dobyGK8CA82jtjDX3fa8BjqkAeGzfYvxAd3W9YOKs%2FfUS9EP82cXQ%2B2LSsvWxDa%2B%2FWVbkU%2BVi0qedod1N8cuGZ1o7Tk%2BjjcRLpgFq67rwb3VqiO52EAsiLeO5FSq1z0vWb9Rd7pDt2MMLnEu81tZJg76ERaJ%2BKMVr6EThnaOOpSMQRLAeQTJB9vFwByRwQoJxmBRHvIvJgbRw5H4KDWN2nvToDWHm7UCTrcl3iK9qbPjCwRBziJi&X-Amz-Signature=42b6b84b4124ae13ea1cb8dfd9d680f66aa42968283e8317e0c7d36d63cd3d13&X-Amz-SignedHeaders=host&x-id=GetObject)
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