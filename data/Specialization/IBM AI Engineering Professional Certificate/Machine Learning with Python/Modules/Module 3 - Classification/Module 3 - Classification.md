

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQI2HIJC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq4cPMfmwlWHBGtQqAjamj8c2X%2FH8z%2B%2FvYHRBVIltczgIgB8qflaUbIzWfpEjwM0o9%2FXoN1Gl6vfvKxQ6wNgydug4qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKuZ9P4DqqYcn6bexCrcA2aXNkw71icc%2F9y1SOyiUckzpnGhAL%2B8UbddEfzJ7MP0XwKerlcRKoBmufX4YmS3hbPc30CwtQUkqoTBOtccYQBK%2Fi40tOxEmeUNCd8qUJnbPhgM8VqBSg4%2Fsfybs3YgV11Vywu6e8FdXJEBe9k75jktFly%2Fhcwtew2C2zY67aDMpSYkVFlHdUDNX%2FUYuElDvsh1JbYn784UPLk2L7bN1%2BsP4Nze%2ByGjFtBX4sC4SRi8agtqJTEppAoIFhkntS8agN%2BoH6yXFfjiY11WhgHj4%2B4lul0iT98Z%2BcBovYLeuWkeIDSm7Kimqk0eNyL1Zn6yEtOFTd1IHLHNUfT2luAmiRPKnR1SWpEjNL72tkL8NKBwZFGGHQk712mm4vT%2FYk0DSjUIwF7Ffq5bRtwr1HCd%2FbD8NXGMO6rcI%2FUwb2vw4ag8EahJLkqVTk5D0K1qh1HsqUYvGT%2BeoR1MJTqxKgRMrcuFyeFZkNmE3Pa%2FmLlpdbZZ%2BO6Jb8Fdjih43X2ASWTlQrVSkqrcGRFGKSg2F%2FVlD1gFubdvB%2Fw4cim25x1rRtkrTMIOyMuRYJOXALUrtU5wOyU7hgA6X%2Bn9q2JoGo3hS37cdwn9uiPQls%2BfD2upPcn%2F4SmC1nB2TRUH7ZwoMPOD6bwGOqUBeTM2yo4%2Fo%2B%2FOPIeDpC8256mlSCWN4%2FnzHmMLcSyy620JF0Fa2E5bK1xe90SX4BOTb9%2F6laxTwMUTuoYT6p%2BLozF2tlv4iiRsV0UBSLp9GtKmUOP5pKflXCwuPHapCPn4oDn72iFhnrzD1Nf0x1cy%2B7T0C0cOvlG9VZoo5JHWWyaADCEG2ZYPmfrQAq0IT01k%2FjmnH29u6nKSwUP08hEjUa95Wn9m&X-Amz-Signature=d6f57d5080a1cdc548898317d49ede5d12b953e50ac4d1eaa58c932339145029&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQI2HIJC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq4cPMfmwlWHBGtQqAjamj8c2X%2FH8z%2B%2FvYHRBVIltczgIgB8qflaUbIzWfpEjwM0o9%2FXoN1Gl6vfvKxQ6wNgydug4qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKuZ9P4DqqYcn6bexCrcA2aXNkw71icc%2F9y1SOyiUckzpnGhAL%2B8UbddEfzJ7MP0XwKerlcRKoBmufX4YmS3hbPc30CwtQUkqoTBOtccYQBK%2Fi40tOxEmeUNCd8qUJnbPhgM8VqBSg4%2Fsfybs3YgV11Vywu6e8FdXJEBe9k75jktFly%2Fhcwtew2C2zY67aDMpSYkVFlHdUDNX%2FUYuElDvsh1JbYn784UPLk2L7bN1%2BsP4Nze%2ByGjFtBX4sC4SRi8agtqJTEppAoIFhkntS8agN%2BoH6yXFfjiY11WhgHj4%2B4lul0iT98Z%2BcBovYLeuWkeIDSm7Kimqk0eNyL1Zn6yEtOFTd1IHLHNUfT2luAmiRPKnR1SWpEjNL72tkL8NKBwZFGGHQk712mm4vT%2FYk0DSjUIwF7Ffq5bRtwr1HCd%2FbD8NXGMO6rcI%2FUwb2vw4ag8EahJLkqVTk5D0K1qh1HsqUYvGT%2BeoR1MJTqxKgRMrcuFyeFZkNmE3Pa%2FmLlpdbZZ%2BO6Jb8Fdjih43X2ASWTlQrVSkqrcGRFGKSg2F%2FVlD1gFubdvB%2Fw4cim25x1rRtkrTMIOyMuRYJOXALUrtU5wOyU7hgA6X%2Bn9q2JoGo3hS37cdwn9uiPQls%2BfD2upPcn%2F4SmC1nB2TRUH7ZwoMPOD6bwGOqUBeTM2yo4%2Fo%2B%2FOPIeDpC8256mlSCWN4%2FnzHmMLcSyy620JF0Fa2E5bK1xe90SX4BOTb9%2F6laxTwMUTuoYT6p%2BLozF2tlv4iiRsV0UBSLp9GtKmUOP5pKflXCwuPHapCPn4oDn72iFhnrzD1Nf0x1cy%2B7T0C0cOvlG9VZoo5JHWWyaADCEG2ZYPmfrQAq0IT01k%2FjmnH29u6nKSwUP08hEjUa95Wn9m&X-Amz-Signature=4b16a03b0ee390ae031c1a55608bc0b2c008550351309e262ec5c028f1b86eaa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQI2HIJC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq4cPMfmwlWHBGtQqAjamj8c2X%2FH8z%2B%2FvYHRBVIltczgIgB8qflaUbIzWfpEjwM0o9%2FXoN1Gl6vfvKxQ6wNgydug4qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKuZ9P4DqqYcn6bexCrcA2aXNkw71icc%2F9y1SOyiUckzpnGhAL%2B8UbddEfzJ7MP0XwKerlcRKoBmufX4YmS3hbPc30CwtQUkqoTBOtccYQBK%2Fi40tOxEmeUNCd8qUJnbPhgM8VqBSg4%2Fsfybs3YgV11Vywu6e8FdXJEBe9k75jktFly%2Fhcwtew2C2zY67aDMpSYkVFlHdUDNX%2FUYuElDvsh1JbYn784UPLk2L7bN1%2BsP4Nze%2ByGjFtBX4sC4SRi8agtqJTEppAoIFhkntS8agN%2BoH6yXFfjiY11WhgHj4%2B4lul0iT98Z%2BcBovYLeuWkeIDSm7Kimqk0eNyL1Zn6yEtOFTd1IHLHNUfT2luAmiRPKnR1SWpEjNL72tkL8NKBwZFGGHQk712mm4vT%2FYk0DSjUIwF7Ffq5bRtwr1HCd%2FbD8NXGMO6rcI%2FUwb2vw4ag8EahJLkqVTk5D0K1qh1HsqUYvGT%2BeoR1MJTqxKgRMrcuFyeFZkNmE3Pa%2FmLlpdbZZ%2BO6Jb8Fdjih43X2ASWTlQrVSkqrcGRFGKSg2F%2FVlD1gFubdvB%2Fw4cim25x1rRtkrTMIOyMuRYJOXALUrtU5wOyU7hgA6X%2Bn9q2JoGo3hS37cdwn9uiPQls%2BfD2upPcn%2F4SmC1nB2TRUH7ZwoMPOD6bwGOqUBeTM2yo4%2Fo%2B%2FOPIeDpC8256mlSCWN4%2FnzHmMLcSyy620JF0Fa2E5bK1xe90SX4BOTb9%2F6laxTwMUTuoYT6p%2BLozF2tlv4iiRsV0UBSLp9GtKmUOP5pKflXCwuPHapCPn4oDn72iFhnrzD1Nf0x1cy%2B7T0C0cOvlG9VZoo5JHWWyaADCEG2ZYPmfrQAq0IT01k%2FjmnH29u6nKSwUP08hEjUa95Wn9m&X-Amz-Signature=a1ea8c1b0379cbf0165569f04007a04aee4c6c5b0d7cef49a7892b04015598c7&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ2IZOG6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs4BasLN4fkFxg0NaMQxT88nbaLWkHeNvt4L%2B0D1THKwIgPPk6xUNxYLcDpClu9Db03yJiIkC7IJomRLQ8goUXaNgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7VWNj%2BnQOZuQUWeCrcA%2Fibp0p6FhuW3AfaloRYfrm4cteLB83jxvYD%2FozpWOeV8gaZN%2BXp%2FY%2FJOPcUzuxyhDiuaAzQc3W9Q%2BeCKwsvRDOfp75%2BXjLrKSjasmObrBE7CleB48MZVFOHLOzms4MNvTwrdrubllzecTeVLKuFs17J5n3udSxtYNkNurdm48dw8HxP5kYNgOvh1E4j2k68u%2Bmcfsp%2Bn92bNiJqf1aeeR5vKm5OEDLPcvqi%2B3EVffiP7MIJDa%2FvuuYpVd6uvmp3S0AShcPM8j%2B3EC9JGQqcZ0%2BJTzPEb%2BNhDzI3kiNm%2BXCXQi0OGtWPOOFvugXkWtiHuK6qBwlPu4erASlykT6kF%2FHo8l3yEtMsrhSXysP1OfYYyGR1PLwPUDcFbCLeyxuyaEAI8Qbp%2BzemNYFkNC%2BjmdskEQTGggrQnGrXDaNJqwcx4DZKXr1fBgVAQ3IY2daZsgQ0DybMMRtnPTm5abFZ13UEKf%2BGO1E80EdHxPFeqd80ey3PwTqVJ2w5senNJBmF189GmticTVyRiOif6Dqlzp7A5hv40d22K7QGGVCOOSFzZX6hYBXlf4mNeKgAgQtyoFU5aMUhOvDJYrTk9%2FR4KiqWxkSb3H0Dw6OWD6U8tlSFQdZn6QjWluqkcvRWMOyD6bwGOqUBqkhgBH7b8G6XQhFVl747aFvmalm7ldtr0msvPBb5yF9Ex8yW7hNc79t3mIEzJS2Ta2m5pk6BVCYAwx5AHdar%2B0diORd0dgmh5aymsNNOPUo3wKoqUz6igbec5%2BH3yIM%2BEx5Nc6JOGJLsfkMYOyGqPu9UUUOeM71Jaocl1Ydt23cQk6uXCumgE3KY%2BJ6HwkepjuoRV0IdTk3ayWrv9ELuLMMZ615K&X-Amz-Signature=f9b0ac943a2ed4b026f8723025b892c7cee7b6675dd7afe60ab1ce69fb667c76&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ2IZOG6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs4BasLN4fkFxg0NaMQxT88nbaLWkHeNvt4L%2B0D1THKwIgPPk6xUNxYLcDpClu9Db03yJiIkC7IJomRLQ8goUXaNgqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7VWNj%2BnQOZuQUWeCrcA%2Fibp0p6FhuW3AfaloRYfrm4cteLB83jxvYD%2FozpWOeV8gaZN%2BXp%2FY%2FJOPcUzuxyhDiuaAzQc3W9Q%2BeCKwsvRDOfp75%2BXjLrKSjasmObrBE7CleB48MZVFOHLOzms4MNvTwrdrubllzecTeVLKuFs17J5n3udSxtYNkNurdm48dw8HxP5kYNgOvh1E4j2k68u%2Bmcfsp%2Bn92bNiJqf1aeeR5vKm5OEDLPcvqi%2B3EVffiP7MIJDa%2FvuuYpVd6uvmp3S0AShcPM8j%2B3EC9JGQqcZ0%2BJTzPEb%2BNhDzI3kiNm%2BXCXQi0OGtWPOOFvugXkWtiHuK6qBwlPu4erASlykT6kF%2FHo8l3yEtMsrhSXysP1OfYYyGR1PLwPUDcFbCLeyxuyaEAI8Qbp%2BzemNYFkNC%2BjmdskEQTGggrQnGrXDaNJqwcx4DZKXr1fBgVAQ3IY2daZsgQ0DybMMRtnPTm5abFZ13UEKf%2BGO1E80EdHxPFeqd80ey3PwTqVJ2w5senNJBmF189GmticTVyRiOif6Dqlzp7A5hv40d22K7QGGVCOOSFzZX6hYBXlf4mNeKgAgQtyoFU5aMUhOvDJYrTk9%2FR4KiqWxkSb3H0Dw6OWD6U8tlSFQdZn6QjWluqkcvRWMOyD6bwGOqUBqkhgBH7b8G6XQhFVl747aFvmalm7ldtr0msvPBb5yF9Ex8yW7hNc79t3mIEzJS2Ta2m5pk6BVCYAwx5AHdar%2B0diORd0dgmh5aymsNNOPUo3wKoqUz6igbec5%2BH3yIM%2BEx5Nc6JOGJLsfkMYOyGqPu9UUUOeM71Jaocl1Ydt23cQk6uXCumgE3KY%2BJ6HwkepjuoRV0IdTk3ayWrv9ELuLMMZ615K&X-Amz-Signature=496b8bd4c3e505e3476cb3bfd74cdb2fa0ca233afde76fa246c138a2f999aeb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQI2HIJC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCq4cPMfmwlWHBGtQqAjamj8c2X%2FH8z%2B%2FvYHRBVIltczgIgB8qflaUbIzWfpEjwM0o9%2FXoN1Gl6vfvKxQ6wNgydug4qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKuZ9P4DqqYcn6bexCrcA2aXNkw71icc%2F9y1SOyiUckzpnGhAL%2B8UbddEfzJ7MP0XwKerlcRKoBmufX4YmS3hbPc30CwtQUkqoTBOtccYQBK%2Fi40tOxEmeUNCd8qUJnbPhgM8VqBSg4%2Fsfybs3YgV11Vywu6e8FdXJEBe9k75jktFly%2Fhcwtew2C2zY67aDMpSYkVFlHdUDNX%2FUYuElDvsh1JbYn784UPLk2L7bN1%2BsP4Nze%2ByGjFtBX4sC4SRi8agtqJTEppAoIFhkntS8agN%2BoH6yXFfjiY11WhgHj4%2B4lul0iT98Z%2BcBovYLeuWkeIDSm7Kimqk0eNyL1Zn6yEtOFTd1IHLHNUfT2luAmiRPKnR1SWpEjNL72tkL8NKBwZFGGHQk712mm4vT%2FYk0DSjUIwF7Ffq5bRtwr1HCd%2FbD8NXGMO6rcI%2FUwb2vw4ag8EahJLkqVTk5D0K1qh1HsqUYvGT%2BeoR1MJTqxKgRMrcuFyeFZkNmE3Pa%2FmLlpdbZZ%2BO6Jb8Fdjih43X2ASWTlQrVSkqrcGRFGKSg2F%2FVlD1gFubdvB%2Fw4cim25x1rRtkrTMIOyMuRYJOXALUrtU5wOyU7hgA6X%2Bn9q2JoGo3hS37cdwn9uiPQls%2BfD2upPcn%2F4SmC1nB2TRUH7ZwoMPOD6bwGOqUBeTM2yo4%2Fo%2B%2FOPIeDpC8256mlSCWN4%2FnzHmMLcSyy620JF0Fa2E5bK1xe90SX4BOTb9%2F6laxTwMUTuoYT6p%2BLozF2tlv4iiRsV0UBSLp9GtKmUOP5pKflXCwuPHapCPn4oDn72iFhnrzD1Nf0x1cy%2B7T0C0cOvlG9VZoo5JHWWyaADCEG2ZYPmfrQAq0IT01k%2FjmnH29u6nKSwUP08hEjUa95Wn9m&X-Amz-Signature=b7159e51b52c4284b9dcf27f9f0e336674d6733265aead3fe3e4549592114980&X-Amz-SignedHeaders=host&x-id=GetObject)
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