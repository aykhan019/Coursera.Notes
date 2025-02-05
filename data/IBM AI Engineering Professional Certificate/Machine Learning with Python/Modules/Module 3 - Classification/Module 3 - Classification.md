

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676KYF2DA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC%2F72O3Kj7Aw0I7AiPCoczEPzx%2B%2FDsd2Rjlp7vmpiJM1QIhAMsIXqkdBFP%2FRhtTekV3wLnvIPsYYZM4%2FMOqSVFa0Ei0Kv8DCDkQABoMNjM3NDIzMTgzODA1Igyi9D9RXiGqECi9n4Eq3APIOqzaNN9vcehx%2BmZy31UuFlVQ8wv6u340o2KN%2BnrtI1zDUmwk%2Ft3SdA9mh4gVOI3AotZ1X2Ghge69Ec4Z4OjZ6CgACYxdPopOoGznmIzKEqnmx6OkWq%2FgK7bKowdk%2B2bME0%2F7Dds9E43qzdxjFN5442wpyTevN3qp1xt1R6e3IktuMUtKastBCmWpI2b0LDDmIdO1o16bwKJT9Aww%2FNff1tuNZzWTalV%2BJDhmYErqG%2Brj2zMOGMmhTrHZNtl%2FkDuz6Yx9sL82LFD0F9c9JqYLMqSGTqGkLHs8YDrb21bjMS5mMNIHV7izSiimN8SQ6FqeKJKTiIvlzCJ%2BSvNqogNxnecSsbQjTou1xumzpr2Cd6mmsSRjVxbtAKMYMOdV70Fk7%2Fn%2BzjWc5JcWc0VNLu2L5H9MgwXxOZJEXQFZalsqbH7JG%2FhNSpgf1kJ4PBTOZBE1a7o1tQLSHcghumPORnevQquD%2Bg9ZXXsb0LKPksfQulq%2FrVo9oYd01ADBBQvN9UIrb6uIEbjTR9whk1F1zF7ECJSeOKLpnsLoDGefV9J8DskLW1XABKrb5TTxGpwpbX5iXtZsGex9yUxMWgWE625yogIjdYExRoOq8h7jM4BG4vjfyynlX1UQj9%2BX0zCQzYq9BjqkASbr3uhIyKx3%2FbgVfFdFbN0ekYVWQ6e3zt6tRSYC%2B5rwHGjoCuL2lmVDq7eMO3z6A5f4%2FAcEbsRLZWRwEt%2F4W%2BZhZ9Rel%2FxfU0MlyvMyjhmwEzFSEqIClc32PNuczT8ULm9OD53taVsm%2FJOO4yksWaYHtEw0BiQTukZgTrRkqFRflke7LTcw0z1f0kTfqRvGtHDTBgQdZnEfGUWSp%2FoMIT7SRoR7&X-Amz-Signature=10c78c03402913d891d5b9265b46056cc11ecbe34a94a8fbbd42bc5db5a0003c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676KYF2DA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC%2F72O3Kj7Aw0I7AiPCoczEPzx%2B%2FDsd2Rjlp7vmpiJM1QIhAMsIXqkdBFP%2FRhtTekV3wLnvIPsYYZM4%2FMOqSVFa0Ei0Kv8DCDkQABoMNjM3NDIzMTgzODA1Igyi9D9RXiGqECi9n4Eq3APIOqzaNN9vcehx%2BmZy31UuFlVQ8wv6u340o2KN%2BnrtI1zDUmwk%2Ft3SdA9mh4gVOI3AotZ1X2Ghge69Ec4Z4OjZ6CgACYxdPopOoGznmIzKEqnmx6OkWq%2FgK7bKowdk%2B2bME0%2F7Dds9E43qzdxjFN5442wpyTevN3qp1xt1R6e3IktuMUtKastBCmWpI2b0LDDmIdO1o16bwKJT9Aww%2FNff1tuNZzWTalV%2BJDhmYErqG%2Brj2zMOGMmhTrHZNtl%2FkDuz6Yx9sL82LFD0F9c9JqYLMqSGTqGkLHs8YDrb21bjMS5mMNIHV7izSiimN8SQ6FqeKJKTiIvlzCJ%2BSvNqogNxnecSsbQjTou1xumzpr2Cd6mmsSRjVxbtAKMYMOdV70Fk7%2Fn%2BzjWc5JcWc0VNLu2L5H9MgwXxOZJEXQFZalsqbH7JG%2FhNSpgf1kJ4PBTOZBE1a7o1tQLSHcghumPORnevQquD%2Bg9ZXXsb0LKPksfQulq%2FrVo9oYd01ADBBQvN9UIrb6uIEbjTR9whk1F1zF7ECJSeOKLpnsLoDGefV9J8DskLW1XABKrb5TTxGpwpbX5iXtZsGex9yUxMWgWE625yogIjdYExRoOq8h7jM4BG4vjfyynlX1UQj9%2BX0zCQzYq9BjqkASbr3uhIyKx3%2FbgVfFdFbN0ekYVWQ6e3zt6tRSYC%2B5rwHGjoCuL2lmVDq7eMO3z6A5f4%2FAcEbsRLZWRwEt%2F4W%2BZhZ9Rel%2FxfU0MlyvMyjhmwEzFSEqIClc32PNuczT8ULm9OD53taVsm%2FJOO4yksWaYHtEw0BiQTukZgTrRkqFRflke7LTcw0z1f0kTfqRvGtHDTBgQdZnEfGUWSp%2FoMIT7SRoR7&X-Amz-Signature=f15e2c689806c9a55959724b9ffa0769f1fd875ec94781d59d4dd43ecc6970d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676KYF2DA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC%2F72O3Kj7Aw0I7AiPCoczEPzx%2B%2FDsd2Rjlp7vmpiJM1QIhAMsIXqkdBFP%2FRhtTekV3wLnvIPsYYZM4%2FMOqSVFa0Ei0Kv8DCDkQABoMNjM3NDIzMTgzODA1Igyi9D9RXiGqECi9n4Eq3APIOqzaNN9vcehx%2BmZy31UuFlVQ8wv6u340o2KN%2BnrtI1zDUmwk%2Ft3SdA9mh4gVOI3AotZ1X2Ghge69Ec4Z4OjZ6CgACYxdPopOoGznmIzKEqnmx6OkWq%2FgK7bKowdk%2B2bME0%2F7Dds9E43qzdxjFN5442wpyTevN3qp1xt1R6e3IktuMUtKastBCmWpI2b0LDDmIdO1o16bwKJT9Aww%2FNff1tuNZzWTalV%2BJDhmYErqG%2Brj2zMOGMmhTrHZNtl%2FkDuz6Yx9sL82LFD0F9c9JqYLMqSGTqGkLHs8YDrb21bjMS5mMNIHV7izSiimN8SQ6FqeKJKTiIvlzCJ%2BSvNqogNxnecSsbQjTou1xumzpr2Cd6mmsSRjVxbtAKMYMOdV70Fk7%2Fn%2BzjWc5JcWc0VNLu2L5H9MgwXxOZJEXQFZalsqbH7JG%2FhNSpgf1kJ4PBTOZBE1a7o1tQLSHcghumPORnevQquD%2Bg9ZXXsb0LKPksfQulq%2FrVo9oYd01ADBBQvN9UIrb6uIEbjTR9whk1F1zF7ECJSeOKLpnsLoDGefV9J8DskLW1XABKrb5TTxGpwpbX5iXtZsGex9yUxMWgWE625yogIjdYExRoOq8h7jM4BG4vjfyynlX1UQj9%2BX0zCQzYq9BjqkASbr3uhIyKx3%2FbgVfFdFbN0ekYVWQ6e3zt6tRSYC%2B5rwHGjoCuL2lmVDq7eMO3z6A5f4%2FAcEbsRLZWRwEt%2F4W%2BZhZ9Rel%2FxfU0MlyvMyjhmwEzFSEqIClc32PNuczT8ULm9OD53taVsm%2FJOO4yksWaYHtEw0BiQTukZgTrRkqFRflke7LTcw0z1f0kTfqRvGtHDTBgQdZnEfGUWSp%2FoMIT7SRoR7&X-Amz-Signature=156fb563983348797376028f3e1dad26e0e0b0f561fee8762abcb754d24816ef&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HMPAIUK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDgSiedfNXz2Ds8LzGi9n43WgCJJDtyyl1OMoGm6Qb%2BdgIhAPv8uW3LayJ%2BxJ5I%2Fs3n3J33iWcTiyNXoy59w0m0%2FJ%2FVKv8DCDkQABoMNjM3NDIzMTgzODA1IgxW5%2F%2FdjraR%2FxaiXocq3AMM9g2q2L%2FXwk4bTUv7Pd%2BY9rObiDgBAYIke0T6%2FFp6VFqQORVP9cHtvq70FLPrwRtq8%2BZoVgV9SmVTnA%2FriD%2FLhBDFyrG4ii9nR0tMtH4I0ndKcQx%2FtyVNem9QqA9k%2F%2BC54cBizOSKyhRSBiAOy8IKjO8EeQ6yp4J4KwJgzVjikY06obMDgKuZBT%2FGIPcEWASCeku8mjFXXBVq0UHbpJK8Md8NzrmBvdbvBgE%2BI%2Bid45TNZhWsayy0JpNEqEnnCSVeU3oNuHuZjo1pk9u%2Bzy3OCh4a6ALLRVHGW2SSv1tk28Mv4xhoAH%2FDMFqf3AoVQ2OLTXo4n6y%2By9TV9owUkPeZjBriBzsf6QV%2B9FJKHi7eIfqwOIvlelJc4M0rRjmr2FuQq5TVchGenaAvMAGGTR2x0WxfKykCwUK9eprXgnnyC%2BTdQOcc1bbd4Nf4opxctaymzhT0cdgJzXy9Y5VCU0sl2m74AhpDTzOh2QyJ6z4cYCLD9jMvR3LmcIft96mcz1sqXHTukCWCLSRmtxY4i2P4R%2FGUcIxJd3W2XXUawsyLlR8aaBRSNEyMIPPO7EyFbY4ysxUNCG3ZEMBwoU%2F7kPr5%2BfFRpE696%2B1LQD%2FkthYUUiTxfKFoe33vQWHeFTDwzIq9BjqkAQZmp1gjVwhKe0NaBNwyeQ1p5IXc%2BjnquWvQgfhY%2FAov6v5AWxxh4y9q1BXf6dUE0arPpcE8BsybUxQJ2PGaSt2b0Pdlr2Ad8Q1qKlGqu2anXqW2rFYzfzWI6Mtz5AEqxxjos32Firre0Cg0UjG0Tb7oCphHK5fIZkri8dVdAZtk9%2FD4iPmPHnHAaQGASus4of4Fjp4xjDev2YyWDq%2B7M7S9ykJX&X-Amz-Signature=8965236eb4daaab574abd1664e54e30afcc6e676c8feb9d49a05edaa738a34ca&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HMPAIUK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDgSiedfNXz2Ds8LzGi9n43WgCJJDtyyl1OMoGm6Qb%2BdgIhAPv8uW3LayJ%2BxJ5I%2Fs3n3J33iWcTiyNXoy59w0m0%2FJ%2FVKv8DCDkQABoMNjM3NDIzMTgzODA1IgxW5%2F%2FdjraR%2FxaiXocq3AMM9g2q2L%2FXwk4bTUv7Pd%2BY9rObiDgBAYIke0T6%2FFp6VFqQORVP9cHtvq70FLPrwRtq8%2BZoVgV9SmVTnA%2FriD%2FLhBDFyrG4ii9nR0tMtH4I0ndKcQx%2FtyVNem9QqA9k%2F%2BC54cBizOSKyhRSBiAOy8IKjO8EeQ6yp4J4KwJgzVjikY06obMDgKuZBT%2FGIPcEWASCeku8mjFXXBVq0UHbpJK8Md8NzrmBvdbvBgE%2BI%2Bid45TNZhWsayy0JpNEqEnnCSVeU3oNuHuZjo1pk9u%2Bzy3OCh4a6ALLRVHGW2SSv1tk28Mv4xhoAH%2FDMFqf3AoVQ2OLTXo4n6y%2By9TV9owUkPeZjBriBzsf6QV%2B9FJKHi7eIfqwOIvlelJc4M0rRjmr2FuQq5TVchGenaAvMAGGTR2x0WxfKykCwUK9eprXgnnyC%2BTdQOcc1bbd4Nf4opxctaymzhT0cdgJzXy9Y5VCU0sl2m74AhpDTzOh2QyJ6z4cYCLD9jMvR3LmcIft96mcz1sqXHTukCWCLSRmtxY4i2P4R%2FGUcIxJd3W2XXUawsyLlR8aaBRSNEyMIPPO7EyFbY4ysxUNCG3ZEMBwoU%2F7kPr5%2BfFRpE696%2B1LQD%2FkthYUUiTxfKFoe33vQWHeFTDwzIq9BjqkAQZmp1gjVwhKe0NaBNwyeQ1p5IXc%2BjnquWvQgfhY%2FAov6v5AWxxh4y9q1BXf6dUE0arPpcE8BsybUxQJ2PGaSt2b0Pdlr2Ad8Q1qKlGqu2anXqW2rFYzfzWI6Mtz5AEqxxjos32Firre0Cg0UjG0Tb7oCphHK5fIZkri8dVdAZtk9%2FD4iPmPHnHAaQGASus4of4Fjp4xjDev2YyWDq%2B7M7S9ykJX&X-Amz-Signature=4074151bd3ae48a83e414ba74588142536a1558c528111f58b7c10ddfed11ee8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676KYF2DA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQC%2F72O3Kj7Aw0I7AiPCoczEPzx%2B%2FDsd2Rjlp7vmpiJM1QIhAMsIXqkdBFP%2FRhtTekV3wLnvIPsYYZM4%2FMOqSVFa0Ei0Kv8DCDkQABoMNjM3NDIzMTgzODA1Igyi9D9RXiGqECi9n4Eq3APIOqzaNN9vcehx%2BmZy31UuFlVQ8wv6u340o2KN%2BnrtI1zDUmwk%2Ft3SdA9mh4gVOI3AotZ1X2Ghge69Ec4Z4OjZ6CgACYxdPopOoGznmIzKEqnmx6OkWq%2FgK7bKowdk%2B2bME0%2F7Dds9E43qzdxjFN5442wpyTevN3qp1xt1R6e3IktuMUtKastBCmWpI2b0LDDmIdO1o16bwKJT9Aww%2FNff1tuNZzWTalV%2BJDhmYErqG%2Brj2zMOGMmhTrHZNtl%2FkDuz6Yx9sL82LFD0F9c9JqYLMqSGTqGkLHs8YDrb21bjMS5mMNIHV7izSiimN8SQ6FqeKJKTiIvlzCJ%2BSvNqogNxnecSsbQjTou1xumzpr2Cd6mmsSRjVxbtAKMYMOdV70Fk7%2Fn%2BzjWc5JcWc0VNLu2L5H9MgwXxOZJEXQFZalsqbH7JG%2FhNSpgf1kJ4PBTOZBE1a7o1tQLSHcghumPORnevQquD%2Bg9ZXXsb0LKPksfQulq%2FrVo9oYd01ADBBQvN9UIrb6uIEbjTR9whk1F1zF7ECJSeOKLpnsLoDGefV9J8DskLW1XABKrb5TTxGpwpbX5iXtZsGex9yUxMWgWE625yogIjdYExRoOq8h7jM4BG4vjfyynlX1UQj9%2BX0zCQzYq9BjqkASbr3uhIyKx3%2FbgVfFdFbN0ekYVWQ6e3zt6tRSYC%2B5rwHGjoCuL2lmVDq7eMO3z6A5f4%2FAcEbsRLZWRwEt%2F4W%2BZhZ9Rel%2FxfU0MlyvMyjhmwEzFSEqIClc32PNuczT8ULm9OD53taVsm%2FJOO4yksWaYHtEw0BiQTukZgTrRkqFRflke7LTcw0z1f0kTfqRvGtHDTBgQdZnEfGUWSp%2FoMIT7SRoR7&X-Amz-Signature=3166326ba5961d0ef3edda9ef8bc5939e0f2a942b20bef68fff4b65657d03f9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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