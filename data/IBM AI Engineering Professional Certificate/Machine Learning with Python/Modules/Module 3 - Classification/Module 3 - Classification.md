

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6YDNF2R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpf60s9IpSEoj%2BMvp4A4BZWtG1Pg%2BPWGkecNfEUmRDNAiEAmpm8km3KhF95g50HiuLTvT5r4tU%2BQrC7gQY0OzgMUxkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB9RHtkhyY0oZ0NSjSrcA00eiOBSbGolhNwUYtZYJF9Da0ISYIk9m4QereyUDje9qoOnDR7WayxQkeIt8Dowyxk%2BLujmZf9dJaHnhwVhgp3QF8NyBATf1cxcrMbiLsi1uDWf%2Fcr9HYo7WJwpqKdsPOXgUoqLIop1sVrWRVNSu65ovuJKs1aSzZbzSCzrVkNH7HcqDngJoaIXeKrdMyaG1RK1Wlvy56PjA6tMbhnSeUPT3Oeeqjpy%2B9%2FVxLwpecqR89Po9Li89YeycRTU3Iw%2Ft%2BgUlKiK31pgYxFQEMtAGzlZgO7WTKvxNiZvMl%2FSTaFXp%2FDJ3%2BvGPnxK6uMt95SLVUfP%2F1p%2FkYKMNvoFSvyOd%2FZ8QZqF7BBwVvUFahVVvS9AkRRooY1hpfveZCKiJfsRgrwuyMVZmI5B%2Bssm7vqPMcUo9Y5tBAIJF3X77nPJmleM2xIldUX9n9zZczYsC6zxUeOtqu5rrryhN%2F%2F%2BBgxS2Razw98i0yF5cSzNQroHpwGWD9PXISUQeV%2B2yeP0WkWS6SJK6mkf7dRG3jP54oDIG9bZ9wsGEsQm5i3IWMqfgLGMliB1BJ1jwlrAFwMCp6fOgdGwulvF448lEvewkkQ2OG%2Fps%2FTo6XjGOnwZvoQP8nGRhnIbsLLRWiWs8wPAMN2k97wGOqUBHDfZ9%2F4sMuuMyqQsY7UQPNA996gOkubW2V2ovrEXr1PCMpKtbtZVP5HA0IpUmHOl4eT9imtcQkRRk2qY9dPfdUjIBfs6upeXUMTK%2B29xJknGG1HJxTf11usAcvoniXjVKmSMWdryL%2Bw60yvBLZVrbX3fetTcf6a8IBcNoD7EJKH%2BuwinOliHcNtKzAMQD6NnDTqNUsWJz1%2FVqcRDk745sVUn6JVN&X-Amz-Signature=62d82f6876996e37343b2e8b07b597128b3f40fddd7cb5a3ca0eaf9df06fc6f2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6YDNF2R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpf60s9IpSEoj%2BMvp4A4BZWtG1Pg%2BPWGkecNfEUmRDNAiEAmpm8km3KhF95g50HiuLTvT5r4tU%2BQrC7gQY0OzgMUxkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB9RHtkhyY0oZ0NSjSrcA00eiOBSbGolhNwUYtZYJF9Da0ISYIk9m4QereyUDje9qoOnDR7WayxQkeIt8Dowyxk%2BLujmZf9dJaHnhwVhgp3QF8NyBATf1cxcrMbiLsi1uDWf%2Fcr9HYo7WJwpqKdsPOXgUoqLIop1sVrWRVNSu65ovuJKs1aSzZbzSCzrVkNH7HcqDngJoaIXeKrdMyaG1RK1Wlvy56PjA6tMbhnSeUPT3Oeeqjpy%2B9%2FVxLwpecqR89Po9Li89YeycRTU3Iw%2Ft%2BgUlKiK31pgYxFQEMtAGzlZgO7WTKvxNiZvMl%2FSTaFXp%2FDJ3%2BvGPnxK6uMt95SLVUfP%2F1p%2FkYKMNvoFSvyOd%2FZ8QZqF7BBwVvUFahVVvS9AkRRooY1hpfveZCKiJfsRgrwuyMVZmI5B%2Bssm7vqPMcUo9Y5tBAIJF3X77nPJmleM2xIldUX9n9zZczYsC6zxUeOtqu5rrryhN%2F%2F%2BBgxS2Razw98i0yF5cSzNQroHpwGWD9PXISUQeV%2B2yeP0WkWS6SJK6mkf7dRG3jP54oDIG9bZ9wsGEsQm5i3IWMqfgLGMliB1BJ1jwlrAFwMCp6fOgdGwulvF448lEvewkkQ2OG%2Fps%2FTo6XjGOnwZvoQP8nGRhnIbsLLRWiWs8wPAMN2k97wGOqUBHDfZ9%2F4sMuuMyqQsY7UQPNA996gOkubW2V2ovrEXr1PCMpKtbtZVP5HA0IpUmHOl4eT9imtcQkRRk2qY9dPfdUjIBfs6upeXUMTK%2B29xJknGG1HJxTf11usAcvoniXjVKmSMWdryL%2Bw60yvBLZVrbX3fetTcf6a8IBcNoD7EJKH%2BuwinOliHcNtKzAMQD6NnDTqNUsWJz1%2FVqcRDk745sVUn6JVN&X-Amz-Signature=cedc518b41e1b2c27f1ed26f0bb5dd951bf5bcd70fde0d8670bb146b46766838&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6YDNF2R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpf60s9IpSEoj%2BMvp4A4BZWtG1Pg%2BPWGkecNfEUmRDNAiEAmpm8km3KhF95g50HiuLTvT5r4tU%2BQrC7gQY0OzgMUxkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB9RHtkhyY0oZ0NSjSrcA00eiOBSbGolhNwUYtZYJF9Da0ISYIk9m4QereyUDje9qoOnDR7WayxQkeIt8Dowyxk%2BLujmZf9dJaHnhwVhgp3QF8NyBATf1cxcrMbiLsi1uDWf%2Fcr9HYo7WJwpqKdsPOXgUoqLIop1sVrWRVNSu65ovuJKs1aSzZbzSCzrVkNH7HcqDngJoaIXeKrdMyaG1RK1Wlvy56PjA6tMbhnSeUPT3Oeeqjpy%2B9%2FVxLwpecqR89Po9Li89YeycRTU3Iw%2Ft%2BgUlKiK31pgYxFQEMtAGzlZgO7WTKvxNiZvMl%2FSTaFXp%2FDJ3%2BvGPnxK6uMt95SLVUfP%2F1p%2FkYKMNvoFSvyOd%2FZ8QZqF7BBwVvUFahVVvS9AkRRooY1hpfveZCKiJfsRgrwuyMVZmI5B%2Bssm7vqPMcUo9Y5tBAIJF3X77nPJmleM2xIldUX9n9zZczYsC6zxUeOtqu5rrryhN%2F%2F%2BBgxS2Razw98i0yF5cSzNQroHpwGWD9PXISUQeV%2B2yeP0WkWS6SJK6mkf7dRG3jP54oDIG9bZ9wsGEsQm5i3IWMqfgLGMliB1BJ1jwlrAFwMCp6fOgdGwulvF448lEvewkkQ2OG%2Fps%2FTo6XjGOnwZvoQP8nGRhnIbsLLRWiWs8wPAMN2k97wGOqUBHDfZ9%2F4sMuuMyqQsY7UQPNA996gOkubW2V2ovrEXr1PCMpKtbtZVP5HA0IpUmHOl4eT9imtcQkRRk2qY9dPfdUjIBfs6upeXUMTK%2B29xJknGG1HJxTf11usAcvoniXjVKmSMWdryL%2Bw60yvBLZVrbX3fetTcf6a8IBcNoD7EJKH%2BuwinOliHcNtKzAMQD6NnDTqNUsWJz1%2FVqcRDk745sVUn6JVN&X-Amz-Signature=8a2926bfd8f7823e791c80b152217e63ffca2bdd33ad944ae2c3b06df02e5643&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ3O4TRW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICXgbjKhNHSm9sBYcOjdxZBTTP0om%2FiAfwuEcHBOmGrHAiBQ%2BEi%2BWX9eSTeD7JRZLDEG3PZK840yfV8W3AJGg85DlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVrYqknB2WK%2FturIEKtwDUY6d6P48eUUOWSlfsqoiQysUE6r3ryX2cQIpv3RWowW4NSLuZDPoJEqwneUuKjqPvocq%2Bmz4i1Pz7k%2Fz7cRJMMnjKEHyiIRKbtFynGwdGPSUNiLwmcC8UmyJQRRN7rsaVEW7c2SJepM6zm%2BRGu%2FtNA8adq1SR5MCMRglhV%2BRuXy2CEG6KnKw7WuHLy%2FHIotjTHAJEWE2pxFcFKUq%2Brr3IQsJPro%2Bhk2sdu119Qvg%2FLrC14qNuA%2Fj5t7rQUJTJ9qM3gd51PQijfXu5344MQgeE%2BKnt2Xm38udTNONLAcH62Lt7j3S4bmm%2B3TzFFSe3JHfIRdqeOrApynDkO4IG3eUaY96DjF86mObmQjmOOixKD0zQ51UzC0VLtoMyOo8BVkFJ%2B6nDFmmm0TfaFLJ0kyoYfkL0B%2Be0PwetZN9klqxNT%2FbkdZuz96fsgmQjUYjC2SLbCk8l%2FpxEbYOzLcrckYugCjpN5J8bQjrYIH0EbfZFwzI%2BcTIkmGgeLR%2Fpx%2FZkQtfGlIthAB59KaeYgR8z7P%2FILcYJihoXUU3Znx2jWzsT7mwxULKRa2ZjqwStX52sb6a43o1cHAx993HWdR%2BfWM9JidCggrZ4uR0fzeBUMud1hE%2FyKxCmLTiCIIhfhEw5qT3vAY6pgHAsVJ7A0w%2BEmT%2F5JGVwLgcfAIVp4vM%2B1hdV%2FZVAAYcBa1gBBzskGKkLsdWoqr%2F5DnSkRVoSH8mqbVr%2F8TUuf5l3FT7m8Y%2FU7zWuTesdUolG7b9gqphr1ZfmdqWUPo%2F4IQ%2Fgpb%2BLay4%2B6%2FMMWBqb2d6A0oCMnqcJBIN%2Ft7b22Qv4acyO%2BitHbunHfBlR6sA20xXjf30%2FTTPxwCFJRUlcTB94cpM%2BugB&X-Amz-Signature=c28848b1ad3f231ee18dc54411f6fcac09554f0ec1f1da8beed05de4dba950f6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQ3O4TRW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICXgbjKhNHSm9sBYcOjdxZBTTP0om%2FiAfwuEcHBOmGrHAiBQ%2BEi%2BWX9eSTeD7JRZLDEG3PZK840yfV8W3AJGg85DlCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVrYqknB2WK%2FturIEKtwDUY6d6P48eUUOWSlfsqoiQysUE6r3ryX2cQIpv3RWowW4NSLuZDPoJEqwneUuKjqPvocq%2Bmz4i1Pz7k%2Fz7cRJMMnjKEHyiIRKbtFynGwdGPSUNiLwmcC8UmyJQRRN7rsaVEW7c2SJepM6zm%2BRGu%2FtNA8adq1SR5MCMRglhV%2BRuXy2CEG6KnKw7WuHLy%2FHIotjTHAJEWE2pxFcFKUq%2Brr3IQsJPro%2Bhk2sdu119Qvg%2FLrC14qNuA%2Fj5t7rQUJTJ9qM3gd51PQijfXu5344MQgeE%2BKnt2Xm38udTNONLAcH62Lt7j3S4bmm%2B3TzFFSe3JHfIRdqeOrApynDkO4IG3eUaY96DjF86mObmQjmOOixKD0zQ51UzC0VLtoMyOo8BVkFJ%2B6nDFmmm0TfaFLJ0kyoYfkL0B%2Be0PwetZN9klqxNT%2FbkdZuz96fsgmQjUYjC2SLbCk8l%2FpxEbYOzLcrckYugCjpN5J8bQjrYIH0EbfZFwzI%2BcTIkmGgeLR%2Fpx%2FZkQtfGlIthAB59KaeYgR8z7P%2FILcYJihoXUU3Znx2jWzsT7mwxULKRa2ZjqwStX52sb6a43o1cHAx993HWdR%2BfWM9JidCggrZ4uR0fzeBUMud1hE%2FyKxCmLTiCIIhfhEw5qT3vAY6pgHAsVJ7A0w%2BEmT%2F5JGVwLgcfAIVp4vM%2B1hdV%2FZVAAYcBa1gBBzskGKkLsdWoqr%2F5DnSkRVoSH8mqbVr%2F8TUuf5l3FT7m8Y%2FU7zWuTesdUolG7b9gqphr1ZfmdqWUPo%2F4IQ%2Fgpb%2BLay4%2B6%2FMMWBqb2d6A0oCMnqcJBIN%2Ft7b22Qv4acyO%2BitHbunHfBlR6sA20xXjf30%2FTTPxwCFJRUlcTB94cpM%2BugB&X-Amz-Signature=13a18058869a8a3e042d20dcc4706a378074bdcc4e0c8eaf4e55e147aa63ded8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6YDNF2R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpf60s9IpSEoj%2BMvp4A4BZWtG1Pg%2BPWGkecNfEUmRDNAiEAmpm8km3KhF95g50HiuLTvT5r4tU%2BQrC7gQY0OzgMUxkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB9RHtkhyY0oZ0NSjSrcA00eiOBSbGolhNwUYtZYJF9Da0ISYIk9m4QereyUDje9qoOnDR7WayxQkeIt8Dowyxk%2BLujmZf9dJaHnhwVhgp3QF8NyBATf1cxcrMbiLsi1uDWf%2Fcr9HYo7WJwpqKdsPOXgUoqLIop1sVrWRVNSu65ovuJKs1aSzZbzSCzrVkNH7HcqDngJoaIXeKrdMyaG1RK1Wlvy56PjA6tMbhnSeUPT3Oeeqjpy%2B9%2FVxLwpecqR89Po9Li89YeycRTU3Iw%2Ft%2BgUlKiK31pgYxFQEMtAGzlZgO7WTKvxNiZvMl%2FSTaFXp%2FDJ3%2BvGPnxK6uMt95SLVUfP%2F1p%2FkYKMNvoFSvyOd%2FZ8QZqF7BBwVvUFahVVvS9AkRRooY1hpfveZCKiJfsRgrwuyMVZmI5B%2Bssm7vqPMcUo9Y5tBAIJF3X77nPJmleM2xIldUX9n9zZczYsC6zxUeOtqu5rrryhN%2F%2F%2BBgxS2Razw98i0yF5cSzNQroHpwGWD9PXISUQeV%2B2yeP0WkWS6SJK6mkf7dRG3jP54oDIG9bZ9wsGEsQm5i3IWMqfgLGMliB1BJ1jwlrAFwMCp6fOgdGwulvF448lEvewkkQ2OG%2Fps%2FTo6XjGOnwZvoQP8nGRhnIbsLLRWiWs8wPAMN2k97wGOqUBHDfZ9%2F4sMuuMyqQsY7UQPNA996gOkubW2V2ovrEXr1PCMpKtbtZVP5HA0IpUmHOl4eT9imtcQkRRk2qY9dPfdUjIBfs6upeXUMTK%2B29xJknGG1HJxTf11usAcvoniXjVKmSMWdryL%2Bw60yvBLZVrbX3fetTcf6a8IBcNoD7EJKH%2BuwinOliHcNtKzAMQD6NnDTqNUsWJz1%2FVqcRDk745sVUn6JVN&X-Amz-Signature=5e85202cf8c0ec9359e1355980122e7293a85c0743009de2e8a26128ded4913e&X-Amz-SignedHeaders=host&x-id=GetObject)
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