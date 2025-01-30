

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XAEDRFG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ9SdxAN%2FJCwaRjq5kEtor5nQ2No8FzDaywSUFktBw%2BAIgH4jPSf8qzmGz4W8nGELfFt%2FsIpzpSntVimy2v9cxJWcqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGoBDdu8IxqSnqcrHyrcA0oqvFbNiIkCqBW9KvESP4yea1iivPz8Deut1N32IGLmbtxRVSe3HwNWl179wK%2BPcxhbtkvVUZO80hEwUArFo5nA2mJoXHAfjk%2BwehKeXNQ3Q2W%2BNDZds2%2BehZ6ZeC6y9PDsDZ3PeupF1dxnCj3A0BIJzf52Qp82Jo55wJPrz7SDFt4%2BzsXUQzBYUpPiuE1hleFh4naYWLmUSUKoyFAGeZiwKs%2BmXYPrGhnNUmzEFe4ny6PxjHf%2FCCFTpaOOznbwjj%2Fv5bYgH2oVEDAbppvS6gf4Zst80rCA6Qqrq2UPWH4w%2BfN%2FVaUW%2FLH6%2BfR4QXgYW3H7b2M%2Ftv4S8lOB1Mp14%2Fpgl8dKhskEgEN1VP7AnCPDMaVlKbrJydynRgH8QOcl3LnVICpu201x1ZLoUFzGH6mCk3821%2BACoLcFzrjFlotdhrb71jWtfXuE9Oyx7LcLx7tD2J9JqyMWY%2BmNCGOQiVhamOKrrylof7Rijj9KBscjZ1187jACDs0AaIOJ1xIf8kxsFjIPw2CPuwCwV8yokCK%2B2OzSWTnbpXgo8zI1Y7pTIR8UpVLxtnnJMR10MLZ%2BoNoxt26q9ueUqEzdPGzlgLMq%2BltUsHsOw9pQ2FWhV4GM8j%2FkQRQE6Wbj4TcHMNOi7LwGOqUBYVjQODXOlZBVgaUGeSjN%2FyDHy%2FgvAQ6P8jeNWMKEaPEvqtsbr0izZ91bMcZv347V9Rpfdxn6xWhPWYX7kfx4%2F%2BRlKZe2%2FszVR3bc8MgAJPjGz9168e8hZbBjlTcsH305NnTPnVXOWe3s6mVFxts9CkB7GXTI%2BbZOAfaN%2FYCzJlfxeDXvZkTGNM%2BKawXPmxJFIxCAOPWAw70wjgjaDDEspx58xSya&X-Amz-Signature=bee2c5bf10201e400d4b380b947bfd8744ce9a16defff59c3490a781ad3eee40&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XAEDRFG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ9SdxAN%2FJCwaRjq5kEtor5nQ2No8FzDaywSUFktBw%2BAIgH4jPSf8qzmGz4W8nGELfFt%2FsIpzpSntVimy2v9cxJWcqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGoBDdu8IxqSnqcrHyrcA0oqvFbNiIkCqBW9KvESP4yea1iivPz8Deut1N32IGLmbtxRVSe3HwNWl179wK%2BPcxhbtkvVUZO80hEwUArFo5nA2mJoXHAfjk%2BwehKeXNQ3Q2W%2BNDZds2%2BehZ6ZeC6y9PDsDZ3PeupF1dxnCj3A0BIJzf52Qp82Jo55wJPrz7SDFt4%2BzsXUQzBYUpPiuE1hleFh4naYWLmUSUKoyFAGeZiwKs%2BmXYPrGhnNUmzEFe4ny6PxjHf%2FCCFTpaOOznbwjj%2Fv5bYgH2oVEDAbppvS6gf4Zst80rCA6Qqrq2UPWH4w%2BfN%2FVaUW%2FLH6%2BfR4QXgYW3H7b2M%2Ftv4S8lOB1Mp14%2Fpgl8dKhskEgEN1VP7AnCPDMaVlKbrJydynRgH8QOcl3LnVICpu201x1ZLoUFzGH6mCk3821%2BACoLcFzrjFlotdhrb71jWtfXuE9Oyx7LcLx7tD2J9JqyMWY%2BmNCGOQiVhamOKrrylof7Rijj9KBscjZ1187jACDs0AaIOJ1xIf8kxsFjIPw2CPuwCwV8yokCK%2B2OzSWTnbpXgo8zI1Y7pTIR8UpVLxtnnJMR10MLZ%2BoNoxt26q9ueUqEzdPGzlgLMq%2BltUsHsOw9pQ2FWhV4GM8j%2FkQRQE6Wbj4TcHMNOi7LwGOqUBYVjQODXOlZBVgaUGeSjN%2FyDHy%2FgvAQ6P8jeNWMKEaPEvqtsbr0izZ91bMcZv347V9Rpfdxn6xWhPWYX7kfx4%2F%2BRlKZe2%2FszVR3bc8MgAJPjGz9168e8hZbBjlTcsH305NnTPnVXOWe3s6mVFxts9CkB7GXTI%2BbZOAfaN%2FYCzJlfxeDXvZkTGNM%2BKawXPmxJFIxCAOPWAw70wjgjaDDEspx58xSya&X-Amz-Signature=a6edabe6790e849ce6b0843b7944a5efd50d9f2a66820274ff6651cf85a550c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XAEDRFG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ9SdxAN%2FJCwaRjq5kEtor5nQ2No8FzDaywSUFktBw%2BAIgH4jPSf8qzmGz4W8nGELfFt%2FsIpzpSntVimy2v9cxJWcqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGoBDdu8IxqSnqcrHyrcA0oqvFbNiIkCqBW9KvESP4yea1iivPz8Deut1N32IGLmbtxRVSe3HwNWl179wK%2BPcxhbtkvVUZO80hEwUArFo5nA2mJoXHAfjk%2BwehKeXNQ3Q2W%2BNDZds2%2BehZ6ZeC6y9PDsDZ3PeupF1dxnCj3A0BIJzf52Qp82Jo55wJPrz7SDFt4%2BzsXUQzBYUpPiuE1hleFh4naYWLmUSUKoyFAGeZiwKs%2BmXYPrGhnNUmzEFe4ny6PxjHf%2FCCFTpaOOznbwjj%2Fv5bYgH2oVEDAbppvS6gf4Zst80rCA6Qqrq2UPWH4w%2BfN%2FVaUW%2FLH6%2BfR4QXgYW3H7b2M%2Ftv4S8lOB1Mp14%2Fpgl8dKhskEgEN1VP7AnCPDMaVlKbrJydynRgH8QOcl3LnVICpu201x1ZLoUFzGH6mCk3821%2BACoLcFzrjFlotdhrb71jWtfXuE9Oyx7LcLx7tD2J9JqyMWY%2BmNCGOQiVhamOKrrylof7Rijj9KBscjZ1187jACDs0AaIOJ1xIf8kxsFjIPw2CPuwCwV8yokCK%2B2OzSWTnbpXgo8zI1Y7pTIR8UpVLxtnnJMR10MLZ%2BoNoxt26q9ueUqEzdPGzlgLMq%2BltUsHsOw9pQ2FWhV4GM8j%2FkQRQE6Wbj4TcHMNOi7LwGOqUBYVjQODXOlZBVgaUGeSjN%2FyDHy%2FgvAQ6P8jeNWMKEaPEvqtsbr0izZ91bMcZv347V9Rpfdxn6xWhPWYX7kfx4%2F%2BRlKZe2%2FszVR3bc8MgAJPjGz9168e8hZbBjlTcsH305NnTPnVXOWe3s6mVFxts9CkB7GXTI%2BbZOAfaN%2FYCzJlfxeDXvZkTGNM%2BKawXPmxJFIxCAOPWAw70wjgjaDDEspx58xSya&X-Amz-Signature=a0eb8932f63a71d6b9794a26d70a21d6014e8710f69c52275a580971ea0bb25f&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPZ4XM65%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAP6CCRW5dsyNYq3EOHDsaZycp20bVQWxdyy0HPMEZ98AiEA6XRINu1r%2F0351DmdC90OgNgPs%2Bfilx%2BQVnaws9jzWcwqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClkh8pfbJ83scBJEircA%2F0viMEIdrs9e4UVrGwFgKLEMaNtMoGPFnQarUE5NaQadDq1C7Opf9sZoqJs26mBS8oIcn%2B8m8cANqQfIb4fAWAN5FFy1cqXr5p86SPfKjWwAsTyQBzCLu6%2BoICjoLjpm9IpPr%2FNj2DT3fkWqnC9gacDzSGRCSsacJpc6srkRCMgkTdE4hD0zsNIL22lSkTFc0vXwcsuU6%2FCyaN6ox%2BtzhYwz9Z%2FSRl8uvNBS%2BKDJsSBlcBeNZHgI%2FW4qUnPEUTc8A5rw%2FA2bv3utcS8%2BHESSgtPMyHnYs4QGBuixlPtNGJbnx32droCbSPgEBz9TyE%2FEoT3EsEildk%2B0dlirS5nzW4V71iTpJL9q%2FPq5a5Clt8pwl6Zli0vN%2BsTyXTLqu5JFUzk2RIKg2hMUuWVwyfQ9eVrGX9fzgDRvctUrRTK5INhYhz01TA7OODf%2FjAkjjAi2SdY71nCsSZ8IvGf0Twtj%2FtQ4lXJdUy%2FhCgpaW%2F4RhCe7o4MWhX2rewTJgf7Bhmfjtp63pW9tXgk9whQmnQieELBT3qs4XU3obpdfpks%2F25sO2FT9f52AI3cUhoDNdkG8OFGUKEhEXkeftKFQ4OCeDS7pcz2ogtrNC7ava1JkJ%2B4ae4Deu83j5b2NtEQMKyj7LwGOqUBE1Eyw5z6jKKW7r0yp%2BZabdHdg%2BJ%2FCTEEHtCZhP8n7SPJ6%2BnVThqCKpjvzBRzUG7c3ddPTX7s8FHhFfdQezGUOXRZguakEKXypxFf9B1%2BOGkmpWU%2BD7d%2BhW8FgrOc6EdeYUsn%2FbBHMcNgSB7b86s6hod%2B6uRCf73ZYW7xBvLf3nmEPZbWSn88fKAPEfoChfTHOSsQDczxn58exwWTVApYhBOdnWlG&X-Amz-Signature=b917f38259df1de036859ab0130e6d4da9223e8676260ad8edb9f1ceb5f3b0c8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPZ4XM65%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAP6CCRW5dsyNYq3EOHDsaZycp20bVQWxdyy0HPMEZ98AiEA6XRINu1r%2F0351DmdC90OgNgPs%2Bfilx%2BQVnaws9jzWcwqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClkh8pfbJ83scBJEircA%2F0viMEIdrs9e4UVrGwFgKLEMaNtMoGPFnQarUE5NaQadDq1C7Opf9sZoqJs26mBS8oIcn%2B8m8cANqQfIb4fAWAN5FFy1cqXr5p86SPfKjWwAsTyQBzCLu6%2BoICjoLjpm9IpPr%2FNj2DT3fkWqnC9gacDzSGRCSsacJpc6srkRCMgkTdE4hD0zsNIL22lSkTFc0vXwcsuU6%2FCyaN6ox%2BtzhYwz9Z%2FSRl8uvNBS%2BKDJsSBlcBeNZHgI%2FW4qUnPEUTc8A5rw%2FA2bv3utcS8%2BHESSgtPMyHnYs4QGBuixlPtNGJbnx32droCbSPgEBz9TyE%2FEoT3EsEildk%2B0dlirS5nzW4V71iTpJL9q%2FPq5a5Clt8pwl6Zli0vN%2BsTyXTLqu5JFUzk2RIKg2hMUuWVwyfQ9eVrGX9fzgDRvctUrRTK5INhYhz01TA7OODf%2FjAkjjAi2SdY71nCsSZ8IvGf0Twtj%2FtQ4lXJdUy%2FhCgpaW%2F4RhCe7o4MWhX2rewTJgf7Bhmfjtp63pW9tXgk9whQmnQieELBT3qs4XU3obpdfpks%2F25sO2FT9f52AI3cUhoDNdkG8OFGUKEhEXkeftKFQ4OCeDS7pcz2ogtrNC7ava1JkJ%2B4ae4Deu83j5b2NtEQMKyj7LwGOqUBE1Eyw5z6jKKW7r0yp%2BZabdHdg%2BJ%2FCTEEHtCZhP8n7SPJ6%2BnVThqCKpjvzBRzUG7c3ddPTX7s8FHhFfdQezGUOXRZguakEKXypxFf9B1%2BOGkmpWU%2BD7d%2BhW8FgrOc6EdeYUsn%2FbBHMcNgSB7b86s6hod%2B6uRCf73ZYW7xBvLf3nmEPZbWSn88fKAPEfoChfTHOSsQDczxn58exwWTVApYhBOdnWlG&X-Amz-Signature=6ac88bd859005d508f202ae9308caed1f3a98c2c6bbd60bc8cdc6c329f10c948&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XAEDRFG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQ9SdxAN%2FJCwaRjq5kEtor5nQ2No8FzDaywSUFktBw%2BAIgH4jPSf8qzmGz4W8nGELfFt%2FsIpzpSntVimy2v9cxJWcqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGoBDdu8IxqSnqcrHyrcA0oqvFbNiIkCqBW9KvESP4yea1iivPz8Deut1N32IGLmbtxRVSe3HwNWl179wK%2BPcxhbtkvVUZO80hEwUArFo5nA2mJoXHAfjk%2BwehKeXNQ3Q2W%2BNDZds2%2BehZ6ZeC6y9PDsDZ3PeupF1dxnCj3A0BIJzf52Qp82Jo55wJPrz7SDFt4%2BzsXUQzBYUpPiuE1hleFh4naYWLmUSUKoyFAGeZiwKs%2BmXYPrGhnNUmzEFe4ny6PxjHf%2FCCFTpaOOznbwjj%2Fv5bYgH2oVEDAbppvS6gf4Zst80rCA6Qqrq2UPWH4w%2BfN%2FVaUW%2FLH6%2BfR4QXgYW3H7b2M%2Ftv4S8lOB1Mp14%2Fpgl8dKhskEgEN1VP7AnCPDMaVlKbrJydynRgH8QOcl3LnVICpu201x1ZLoUFzGH6mCk3821%2BACoLcFzrjFlotdhrb71jWtfXuE9Oyx7LcLx7tD2J9JqyMWY%2BmNCGOQiVhamOKrrylof7Rijj9KBscjZ1187jACDs0AaIOJ1xIf8kxsFjIPw2CPuwCwV8yokCK%2B2OzSWTnbpXgo8zI1Y7pTIR8UpVLxtnnJMR10MLZ%2BoNoxt26q9ueUqEzdPGzlgLMq%2BltUsHsOw9pQ2FWhV4GM8j%2FkQRQE6Wbj4TcHMNOi7LwGOqUBYVjQODXOlZBVgaUGeSjN%2FyDHy%2FgvAQ6P8jeNWMKEaPEvqtsbr0izZ91bMcZv347V9Rpfdxn6xWhPWYX7kfx4%2F%2BRlKZe2%2FszVR3bc8MgAJPjGz9168e8hZbBjlTcsH305NnTPnVXOWe3s6mVFxts9CkB7GXTI%2BbZOAfaN%2FYCzJlfxeDXvZkTGNM%2BKawXPmxJFIxCAOPWAw70wjgjaDDEspx58xSya&X-Amz-Signature=f8f576436f835edd0b349a303f624df1e07126586c43b583a6ae490795392850&X-Amz-SignedHeaders=host&x-id=GetObject)
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