

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI7DU7EN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvZVoQ9rDuWO0LFyGhDg69O5z3NTJmGHswKaVTmtyBGAIgUvt2JIUz%2B%2F4Jp7vn%2FSKMsFbzX7RT65n1Idd4eT9slOQqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBfWEsDqWjDCX9X1HCrcA1RdXGO8AtFQXpM8hq5o8bSVGMpIjlrS6LB2brAKvS%2BZEEMsGlKZm4ZN3Izwedp7WY4szbB0OMynr5PYxvYUX8F7jJO6o8nqijJ%2Fm1ME%2FOUaLMPh%2FpdfRDJZSVpu%2BU%2Fp%2FbQhPy7R8BRKzXwSBrr60SW35bhawJKa1GPmp0YJSBpwCHvOxQ9GukgKbWnOLd2r8o4U0YdxdNDxCPRp4HQGND4ucbarRMvAvLUmEyhB5nIw1m%2FX%2B%2FrYld2FeSm6Voyo5n8kelTkQaiSm8HjSfHru4i9DEsh4fCBVxT5O2AHf%2FoGWuOQGef0HQ4YzVwS7wT5mRdpmsHi405M9vu5j4CemksIh00eWPXclG6UTxFakAQNc%2Bj3bDD582121WW0UzSYCch80clEsmZPet6iuRpGXC7C6q63vOUCyg4IBcBLBzbmx5jSgHyR9zdmGCKVSNRUBxVsgsJ3o5MRgquvGmrA22PMqqmLwXiyIgOOqoeHMed0ZlMuw22%2F8iTn3Hoj3nGO55Vd6qExSnd28pE7ohSEacMupQUZAbdOBMtJ7b55f9vwgefRVFzuhRGFOwwbhfu%2F6Pqpd6Uvvsk%2B%2B62TuHxeKvmjIAS6mcEfTtvdYvZxET3QgyvsGbn7fqJbcp6QMMOD6bwGOqUBh%2BeHjIyJ1SgPKXNes5ddUi5WxDrrnvv1KyCj7%2BiisBljn9Gc6xdLhIbgfTAGhLg7IaFtD%2Byhi8r7Dm1taTI8rMm0Wg26NR7O4rtKXD2NbNfvH5%2BZhenIxlGKFzhme%2BItq4VV7iw7ph8QLEuLEpyS997oJeo2wkxanMgF%2F7oMtCt3cPN9EmijTZFDefAisYwIN04Yu9TSgKtjzAIURX2w67XNAZYz&X-Amz-Signature=823f3f7c78548eb35435f7413984f6a4572239ebb1af40012965874ad42ca757&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI7DU7EN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvZVoQ9rDuWO0LFyGhDg69O5z3NTJmGHswKaVTmtyBGAIgUvt2JIUz%2B%2F4Jp7vn%2FSKMsFbzX7RT65n1Idd4eT9slOQqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBfWEsDqWjDCX9X1HCrcA1RdXGO8AtFQXpM8hq5o8bSVGMpIjlrS6LB2brAKvS%2BZEEMsGlKZm4ZN3Izwedp7WY4szbB0OMynr5PYxvYUX8F7jJO6o8nqijJ%2Fm1ME%2FOUaLMPh%2FpdfRDJZSVpu%2BU%2Fp%2FbQhPy7R8BRKzXwSBrr60SW35bhawJKa1GPmp0YJSBpwCHvOxQ9GukgKbWnOLd2r8o4U0YdxdNDxCPRp4HQGND4ucbarRMvAvLUmEyhB5nIw1m%2FX%2B%2FrYld2FeSm6Voyo5n8kelTkQaiSm8HjSfHru4i9DEsh4fCBVxT5O2AHf%2FoGWuOQGef0HQ4YzVwS7wT5mRdpmsHi405M9vu5j4CemksIh00eWPXclG6UTxFakAQNc%2Bj3bDD582121WW0UzSYCch80clEsmZPet6iuRpGXC7C6q63vOUCyg4IBcBLBzbmx5jSgHyR9zdmGCKVSNRUBxVsgsJ3o5MRgquvGmrA22PMqqmLwXiyIgOOqoeHMed0ZlMuw22%2F8iTn3Hoj3nGO55Vd6qExSnd28pE7ohSEacMupQUZAbdOBMtJ7b55f9vwgefRVFzuhRGFOwwbhfu%2F6Pqpd6Uvvsk%2B%2B62TuHxeKvmjIAS6mcEfTtvdYvZxET3QgyvsGbn7fqJbcp6QMMOD6bwGOqUBh%2BeHjIyJ1SgPKXNes5ddUi5WxDrrnvv1KyCj7%2BiisBljn9Gc6xdLhIbgfTAGhLg7IaFtD%2Byhi8r7Dm1taTI8rMm0Wg26NR7O4rtKXD2NbNfvH5%2BZhenIxlGKFzhme%2BItq4VV7iw7ph8QLEuLEpyS997oJeo2wkxanMgF%2F7oMtCt3cPN9EmijTZFDefAisYwIN04Yu9TSgKtjzAIURX2w67XNAZYz&X-Amz-Signature=811e32e92de5fcdd781e188da9b03d04021b71173ec9b7c44213e6bd40921d59&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI7DU7EN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvZVoQ9rDuWO0LFyGhDg69O5z3NTJmGHswKaVTmtyBGAIgUvt2JIUz%2B%2F4Jp7vn%2FSKMsFbzX7RT65n1Idd4eT9slOQqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBfWEsDqWjDCX9X1HCrcA1RdXGO8AtFQXpM8hq5o8bSVGMpIjlrS6LB2brAKvS%2BZEEMsGlKZm4ZN3Izwedp7WY4szbB0OMynr5PYxvYUX8F7jJO6o8nqijJ%2Fm1ME%2FOUaLMPh%2FpdfRDJZSVpu%2BU%2Fp%2FbQhPy7R8BRKzXwSBrr60SW35bhawJKa1GPmp0YJSBpwCHvOxQ9GukgKbWnOLd2r8o4U0YdxdNDxCPRp4HQGND4ucbarRMvAvLUmEyhB5nIw1m%2FX%2B%2FrYld2FeSm6Voyo5n8kelTkQaiSm8HjSfHru4i9DEsh4fCBVxT5O2AHf%2FoGWuOQGef0HQ4YzVwS7wT5mRdpmsHi405M9vu5j4CemksIh00eWPXclG6UTxFakAQNc%2Bj3bDD582121WW0UzSYCch80clEsmZPet6iuRpGXC7C6q63vOUCyg4IBcBLBzbmx5jSgHyR9zdmGCKVSNRUBxVsgsJ3o5MRgquvGmrA22PMqqmLwXiyIgOOqoeHMed0ZlMuw22%2F8iTn3Hoj3nGO55Vd6qExSnd28pE7ohSEacMupQUZAbdOBMtJ7b55f9vwgefRVFzuhRGFOwwbhfu%2F6Pqpd6Uvvsk%2B%2B62TuHxeKvmjIAS6mcEfTtvdYvZxET3QgyvsGbn7fqJbcp6QMMOD6bwGOqUBh%2BeHjIyJ1SgPKXNes5ddUi5WxDrrnvv1KyCj7%2BiisBljn9Gc6xdLhIbgfTAGhLg7IaFtD%2Byhi8r7Dm1taTI8rMm0Wg26NR7O4rtKXD2NbNfvH5%2BZhenIxlGKFzhme%2BItq4VV7iw7ph8QLEuLEpyS997oJeo2wkxanMgF%2F7oMtCt3cPN9EmijTZFDefAisYwIN04Yu9TSgKtjzAIURX2w67XNAZYz&X-Amz-Signature=9132e31c1be895fbd8e2560f5db5916fc028d9a7436ee2be466e04bea94c11e3&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IGIAXPL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxBTARppUHpEe5P29XvqphlY1HpjSp1q3miRh1JbRoJAIgRspXVLWdRY%2BjvZE7bw8K35RaE%2Bf5x6JvDMYd%2BtWMRpkqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOowetR78rYsgCkqySrcA1ukCfL9Mjh2cTRXg76dDRzYv7EBPmclOLadK3stuXnKaCT8WNJZxXtPdf7Hkd2rpRvimYEoXdzAhMPsenYLABjC24Gf45MD71H%2FqZh9%2Fm%2BaXnyGeBhBfjpQKMjxBfx6k%2F3KIeTFNhYaqg5HyXAtWkncYXfSJkYVXmpdB%2FfnGfnx8i%2Fj3SVZb7ZPQ0pYCdr7LZZYTXV%2FB2be51cbMW2yILyU%2FVi1lxwVhdJhPlefwpvQ587C1qzrppR1mRwgT5rN8qSTNzXEE07dNbD%2FbEvCKMufjRqIJfu2mU6emAfXkW77R2F0kztdU19pR6zZ%2FSpFP5ZJSfMYmyYkh%2BWfLfIh7%2FGIeT5%2FB5pFdAfFl7QTLeiXt%2Bc9%2B7NyT3Y9EQrR1nGnk6ECDNNkjUVl8hBLEdPmSoWhNIIuRVIRrvzHYXB0ltDtxk6SNWswNcW8JxAhN%2FQirvPD79j3olD4JlsjE3nW9KFaIbdqMDGTAoEHqymrdAtNBS9Ve7gh5YuLlqHYTCLO2WTc3fnm1dAq3%2FgXkK09CQ5h7aBEfyga7QCqFrQ48w4XDBjz1YPx%2BhebQ9LlhzoGUM9hNeRm1JuGUHjtKsK1y%2FKh5V7wTTWkdd%2FpZoFdp8K7%2FZtFyG6VTnqzd%2FRuMO2D6bwGOqUBQi%2Bw1zaPUY7ljRPh2960IrgHkPIAc4qCaESkj7Yw%2BsDYmZSH6IgIDIHIQ5Vk9pxEhKIPbBLmfhzwLks8Nr29XSbs5J5JmwgQB6BO9YrQB20oRQPamCtP283dFksaUQ4ruujhfjY%2FqWdkGKGg4K%2BI8gjAkCLIjIhHJzku0eBPOKAlWGHGfFFQMGjjgq8f%2FeYoNkZy8vb7qgL6z5ed7c8mn0ZeeZkQ&X-Amz-Signature=b7ddb8892c8f720883d4084251212c9ca6a3204db5a902456d6aa50a1d5a777f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IGIAXPL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxBTARppUHpEe5P29XvqphlY1HpjSp1q3miRh1JbRoJAIgRspXVLWdRY%2BjvZE7bw8K35RaE%2Bf5x6JvDMYd%2BtWMRpkqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOowetR78rYsgCkqySrcA1ukCfL9Mjh2cTRXg76dDRzYv7EBPmclOLadK3stuXnKaCT8WNJZxXtPdf7Hkd2rpRvimYEoXdzAhMPsenYLABjC24Gf45MD71H%2FqZh9%2Fm%2BaXnyGeBhBfjpQKMjxBfx6k%2F3KIeTFNhYaqg5HyXAtWkncYXfSJkYVXmpdB%2FfnGfnx8i%2Fj3SVZb7ZPQ0pYCdr7LZZYTXV%2FB2be51cbMW2yILyU%2FVi1lxwVhdJhPlefwpvQ587C1qzrppR1mRwgT5rN8qSTNzXEE07dNbD%2FbEvCKMufjRqIJfu2mU6emAfXkW77R2F0kztdU19pR6zZ%2FSpFP5ZJSfMYmyYkh%2BWfLfIh7%2FGIeT5%2FB5pFdAfFl7QTLeiXt%2Bc9%2B7NyT3Y9EQrR1nGnk6ECDNNkjUVl8hBLEdPmSoWhNIIuRVIRrvzHYXB0ltDtxk6SNWswNcW8JxAhN%2FQirvPD79j3olD4JlsjE3nW9KFaIbdqMDGTAoEHqymrdAtNBS9Ve7gh5YuLlqHYTCLO2WTc3fnm1dAq3%2FgXkK09CQ5h7aBEfyga7QCqFrQ48w4XDBjz1YPx%2BhebQ9LlhzoGUM9hNeRm1JuGUHjtKsK1y%2FKh5V7wTTWkdd%2FpZoFdp8K7%2FZtFyG6VTnqzd%2FRuMO2D6bwGOqUBQi%2Bw1zaPUY7ljRPh2960IrgHkPIAc4qCaESkj7Yw%2BsDYmZSH6IgIDIHIQ5Vk9pxEhKIPbBLmfhzwLks8Nr29XSbs5J5JmwgQB6BO9YrQB20oRQPamCtP283dFksaUQ4ruujhfjY%2FqWdkGKGg4K%2BI8gjAkCLIjIhHJzku0eBPOKAlWGHGfFFQMGjjgq8f%2FeYoNkZy8vb7qgL6z5ed7c8mn0ZeeZkQ&X-Amz-Signature=07eb23ae75d83c10df0c6e2c3ca6a5be9ec43f01f619775e7d719db0ec018e80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI7DU7EN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvZVoQ9rDuWO0LFyGhDg69O5z3NTJmGHswKaVTmtyBGAIgUvt2JIUz%2B%2F4Jp7vn%2FSKMsFbzX7RT65n1Idd4eT9slOQqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBfWEsDqWjDCX9X1HCrcA1RdXGO8AtFQXpM8hq5o8bSVGMpIjlrS6LB2brAKvS%2BZEEMsGlKZm4ZN3Izwedp7WY4szbB0OMynr5PYxvYUX8F7jJO6o8nqijJ%2Fm1ME%2FOUaLMPh%2FpdfRDJZSVpu%2BU%2Fp%2FbQhPy7R8BRKzXwSBrr60SW35bhawJKa1GPmp0YJSBpwCHvOxQ9GukgKbWnOLd2r8o4U0YdxdNDxCPRp4HQGND4ucbarRMvAvLUmEyhB5nIw1m%2FX%2B%2FrYld2FeSm6Voyo5n8kelTkQaiSm8HjSfHru4i9DEsh4fCBVxT5O2AHf%2FoGWuOQGef0HQ4YzVwS7wT5mRdpmsHi405M9vu5j4CemksIh00eWPXclG6UTxFakAQNc%2Bj3bDD582121WW0UzSYCch80clEsmZPet6iuRpGXC7C6q63vOUCyg4IBcBLBzbmx5jSgHyR9zdmGCKVSNRUBxVsgsJ3o5MRgquvGmrA22PMqqmLwXiyIgOOqoeHMed0ZlMuw22%2F8iTn3Hoj3nGO55Vd6qExSnd28pE7ohSEacMupQUZAbdOBMtJ7b55f9vwgefRVFzuhRGFOwwbhfu%2F6Pqpd6Uvvsk%2B%2B62TuHxeKvmjIAS6mcEfTtvdYvZxET3QgyvsGbn7fqJbcp6QMMOD6bwGOqUBh%2BeHjIyJ1SgPKXNes5ddUi5WxDrrnvv1KyCj7%2BiisBljn9Gc6xdLhIbgfTAGhLg7IaFtD%2Byhi8r7Dm1taTI8rMm0Wg26NR7O4rtKXD2NbNfvH5%2BZhenIxlGKFzhme%2BItq4VV7iw7ph8QLEuLEpyS997oJeo2wkxanMgF%2F7oMtCt3cPN9EmijTZFDefAisYwIN04Yu9TSgKtjzAIURX2w67XNAZYz&X-Amz-Signature=ed820bada0c53de10abd62daa374b555e231720db44e334f78018b04684432ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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