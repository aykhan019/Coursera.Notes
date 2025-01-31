

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CF2DIR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBV1e8Qv9%2FeJ8XFLiAJY8s%2Fhu%2B%2Ba8SL19A7%2BOEG6LE2AiB73dVrKuDO2X3CT1qi9AIPOfxDBg0HtaDlT3ddZMqiWyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtngm3OsDQIAgj6UVKtwDSXBTaHjexw3Y8eolSykM%2FVd1SDQdn5KoMkuQhSBmQeW23mPUQrF1fPSau%2BI5p2ADeVbFC%2BguiU6gqA06%2Bobkxi5KwePduMYVD7ZlN0pLk1CfP%2FOKRUACzUwXim7FRRmDkwdiQG6zBIT5N8Sf7BBGcQYFxXUfiqaO4g4Q40uUdDdoiYz4iRlgA6ERYog588jCVwOBWC5t0PeHA1Z%2Fm9DQRdkFbIv2S6fNCUjeGBnmS9T1Br0A1bmnqNl1Nqd1udPqixv0%2FQK0twV1erSSuCMObkVxBJ47Sy7%2BBO0VakXwPW8HT0l7pq3Bwp3B1sfrN4tF5J3cN0VSq5zP%2FEg1haEm8XM4GmArab%2BeoO40%2Ft8auwoj7RBqBOM%2FJKy5%2FNhCtx8fxmNLVYp6jVbZG3llmM3DP%2FeJH%2BS8XpisVI%2FvinetcbA%2FEeOQmD%2BzMOc6PEDMGcfd0MgU8Om1SbuRy2rtuXoxXTqBq2hUBTfLi%2ByqOvF1H7f3bddOJZR8gcDscpu7rB4IyRhA%2FkgD%2FIUnPN%2BWYWA6GznEL5c31QuZck1CUI5X5%2FOby76kvmPXyNvXEsUPo1jx9Bg9RUHAyPpN7TErxnI1fISEXguUqzE4pUSRUwXKEuqgHZwGBY%2Bntcq0iE0woP7xvAY6pgFN%2F1ezjntAdRf5ZKYu%2Fq4PPjlhIagSWpb%2FVyMtLfrE6nTsh%2Fl792cwoy1NIZrqdU3yRSbzXzXwV%2FjceN%2FEapYKDY51dKVdPhMLkKgiVFVZS%2FATTv2FFBRlGptqkKuhp4xJ22xmoW0SqFjP037%2BdhsmMc08OHkho3ZosPjtHq8ywk%2FTLx6Trothz%2BcxvJlncEnQiXu2T18hYDF%2FqDN1Kp1cZbYTcYsg&X-Amz-Signature=c013852928d137b6de9bcb7b696354dfa4139a112933a3a7732f8f62dd1810c4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CF2DIR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBV1e8Qv9%2FeJ8XFLiAJY8s%2Fhu%2B%2Ba8SL19A7%2BOEG6LE2AiB73dVrKuDO2X3CT1qi9AIPOfxDBg0HtaDlT3ddZMqiWyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtngm3OsDQIAgj6UVKtwDSXBTaHjexw3Y8eolSykM%2FVd1SDQdn5KoMkuQhSBmQeW23mPUQrF1fPSau%2BI5p2ADeVbFC%2BguiU6gqA06%2Bobkxi5KwePduMYVD7ZlN0pLk1CfP%2FOKRUACzUwXim7FRRmDkwdiQG6zBIT5N8Sf7BBGcQYFxXUfiqaO4g4Q40uUdDdoiYz4iRlgA6ERYog588jCVwOBWC5t0PeHA1Z%2Fm9DQRdkFbIv2S6fNCUjeGBnmS9T1Br0A1bmnqNl1Nqd1udPqixv0%2FQK0twV1erSSuCMObkVxBJ47Sy7%2BBO0VakXwPW8HT0l7pq3Bwp3B1sfrN4tF5J3cN0VSq5zP%2FEg1haEm8XM4GmArab%2BeoO40%2Ft8auwoj7RBqBOM%2FJKy5%2FNhCtx8fxmNLVYp6jVbZG3llmM3DP%2FeJH%2BS8XpisVI%2FvinetcbA%2FEeOQmD%2BzMOc6PEDMGcfd0MgU8Om1SbuRy2rtuXoxXTqBq2hUBTfLi%2ByqOvF1H7f3bddOJZR8gcDscpu7rB4IyRhA%2FkgD%2FIUnPN%2BWYWA6GznEL5c31QuZck1CUI5X5%2FOby76kvmPXyNvXEsUPo1jx9Bg9RUHAyPpN7TErxnI1fISEXguUqzE4pUSRUwXKEuqgHZwGBY%2Bntcq0iE0woP7xvAY6pgFN%2F1ezjntAdRf5ZKYu%2Fq4PPjlhIagSWpb%2FVyMtLfrE6nTsh%2Fl792cwoy1NIZrqdU3yRSbzXzXwV%2FjceN%2FEapYKDY51dKVdPhMLkKgiVFVZS%2FATTv2FFBRlGptqkKuhp4xJ22xmoW0SqFjP037%2BdhsmMc08OHkho3ZosPjtHq8ywk%2FTLx6Trothz%2BcxvJlncEnQiXu2T18hYDF%2FqDN1Kp1cZbYTcYsg&X-Amz-Signature=f0dc5ee913812943413a1ce9dc59b282ab65d3721d7db2fa4f872ce5e00146e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CF2DIR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBV1e8Qv9%2FeJ8XFLiAJY8s%2Fhu%2B%2Ba8SL19A7%2BOEG6LE2AiB73dVrKuDO2X3CT1qi9AIPOfxDBg0HtaDlT3ddZMqiWyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtngm3OsDQIAgj6UVKtwDSXBTaHjexw3Y8eolSykM%2FVd1SDQdn5KoMkuQhSBmQeW23mPUQrF1fPSau%2BI5p2ADeVbFC%2BguiU6gqA06%2Bobkxi5KwePduMYVD7ZlN0pLk1CfP%2FOKRUACzUwXim7FRRmDkwdiQG6zBIT5N8Sf7BBGcQYFxXUfiqaO4g4Q40uUdDdoiYz4iRlgA6ERYog588jCVwOBWC5t0PeHA1Z%2Fm9DQRdkFbIv2S6fNCUjeGBnmS9T1Br0A1bmnqNl1Nqd1udPqixv0%2FQK0twV1erSSuCMObkVxBJ47Sy7%2BBO0VakXwPW8HT0l7pq3Bwp3B1sfrN4tF5J3cN0VSq5zP%2FEg1haEm8XM4GmArab%2BeoO40%2Ft8auwoj7RBqBOM%2FJKy5%2FNhCtx8fxmNLVYp6jVbZG3llmM3DP%2FeJH%2BS8XpisVI%2FvinetcbA%2FEeOQmD%2BzMOc6PEDMGcfd0MgU8Om1SbuRy2rtuXoxXTqBq2hUBTfLi%2ByqOvF1H7f3bddOJZR8gcDscpu7rB4IyRhA%2FkgD%2FIUnPN%2BWYWA6GznEL5c31QuZck1CUI5X5%2FOby76kvmPXyNvXEsUPo1jx9Bg9RUHAyPpN7TErxnI1fISEXguUqzE4pUSRUwXKEuqgHZwGBY%2Bntcq0iE0woP7xvAY6pgFN%2F1ezjntAdRf5ZKYu%2Fq4PPjlhIagSWpb%2FVyMtLfrE6nTsh%2Fl792cwoy1NIZrqdU3yRSbzXzXwV%2FjceN%2FEapYKDY51dKVdPhMLkKgiVFVZS%2FATTv2FFBRlGptqkKuhp4xJ22xmoW0SqFjP037%2BdhsmMc08OHkho3ZosPjtHq8ywk%2FTLx6Trothz%2BcxvJlncEnQiXu2T18hYDF%2FqDN1Kp1cZbYTcYsg&X-Amz-Signature=4c93545057e2c82c14886ef2faecec9de391e1c8e86c883b942b91729298cbd2&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654O3DANX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfus53lbSvmDrl%2FwLz5wqNPjrWdglQzxJaD2ji0XvAtAiBS7Q4mVGzIh7MYe1dSyeGfF43CQhZppBbu9s0yaLItZiqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9gi2JOtJdd5IIstCKtwDWO7lUAcx%2FvFqS%2FeySOTFxkGroEIEfiO3OOGLeYG%2Fhq4UnLRK4hH0jFnlwhPthnDFOrya2B2NChOQXqAA%2BRcH1fOVTjFh3CeeFdLhh%2BGLj4gLLQoYIt6yx4qmDP0y44TKmSpGcqKomeMj%2BfP6pxzOCKTEGc1Hm%2FJ9qoR0VjpLlQGqCEtGei3a8cO19r22IacujSWSOF6iZkzpxVoCTYcb1grCXPx8KJWrIFJ7X4RpdcYkFycXN5jx9qcIvYWY66UxFllCTrYaP%2FVVs6XOr%2FgIbwt5Eh5ZHWs6RkmtFTw1baGTYCrPpdXw1PH457I%2Fuf%2BQS6XLqG2Rs%2Bxcwuz3jtGx6LkfRpub%2FUcSX82FWbjw4oDbA5Hiu59ELTkBWJm7tYtCrbOia1fyp8ZxhzO5x3KUnlpP78YxAWt5%2BKsITrVBBMpRZe%2Fa6vI4k7Rm5tCJawWxHeDUAG5HkOpd3r51Lp0Yyq8eoYXtvMQx0fdxf%2Fe1QUM2WQxyTyRL65LHVqnhs1LAudwNULy%2Bg4fc2MPBRvWpsE3sFxxvkzBReku1U7buH7GVEoKnho8exKRCbHSxUVt3btx%2FL2vmilO2Pu0EfLi4acRHUg4XSiFQ8eE860GBzZ5ZUSHtLa3NnzYPmdUw4%2F3xvAY6pgHeF6tJ0fWczlsR619UdZZGfRIoCtnsxckf0eDBHR4PXtMfbV9cdqpYyRU3bIwTU%2BPUW24nCB8kO7mtQmdtVAJgKirlORKc7%2BvN7WQBaslOKM6siHUv8IH06nxYMsbrNxHWh3U7%2FU%2BjtjYoN%2BtEXWLlLYd6jnv771wgy%2Fjibk63GkyLm2WK5oX%2B%2FyBSpXk%2BEAOzIJsObImqM69Wl5kyR8XZ2yb34qX0&X-Amz-Signature=6c241556a86ba1cfd77fb6b0e3d627979a8957f5ec4560ce3a8e6ca0f0c0b431&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654O3DANX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGfus53lbSvmDrl%2FwLz5wqNPjrWdglQzxJaD2ji0XvAtAiBS7Q4mVGzIh7MYe1dSyeGfF43CQhZppBbu9s0yaLItZiqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9gi2JOtJdd5IIstCKtwDWO7lUAcx%2FvFqS%2FeySOTFxkGroEIEfiO3OOGLeYG%2Fhq4UnLRK4hH0jFnlwhPthnDFOrya2B2NChOQXqAA%2BRcH1fOVTjFh3CeeFdLhh%2BGLj4gLLQoYIt6yx4qmDP0y44TKmSpGcqKomeMj%2BfP6pxzOCKTEGc1Hm%2FJ9qoR0VjpLlQGqCEtGei3a8cO19r22IacujSWSOF6iZkzpxVoCTYcb1grCXPx8KJWrIFJ7X4RpdcYkFycXN5jx9qcIvYWY66UxFllCTrYaP%2FVVs6XOr%2FgIbwt5Eh5ZHWs6RkmtFTw1baGTYCrPpdXw1PH457I%2Fuf%2BQS6XLqG2Rs%2Bxcwuz3jtGx6LkfRpub%2FUcSX82FWbjw4oDbA5Hiu59ELTkBWJm7tYtCrbOia1fyp8ZxhzO5x3KUnlpP78YxAWt5%2BKsITrVBBMpRZe%2Fa6vI4k7Rm5tCJawWxHeDUAG5HkOpd3r51Lp0Yyq8eoYXtvMQx0fdxf%2Fe1QUM2WQxyTyRL65LHVqnhs1LAudwNULy%2Bg4fc2MPBRvWpsE3sFxxvkzBReku1U7buH7GVEoKnho8exKRCbHSxUVt3btx%2FL2vmilO2Pu0EfLi4acRHUg4XSiFQ8eE860GBzZ5ZUSHtLa3NnzYPmdUw4%2F3xvAY6pgHeF6tJ0fWczlsR619UdZZGfRIoCtnsxckf0eDBHR4PXtMfbV9cdqpYyRU3bIwTU%2BPUW24nCB8kO7mtQmdtVAJgKirlORKc7%2BvN7WQBaslOKM6siHUv8IH06nxYMsbrNxHWh3U7%2FU%2BjtjYoN%2BtEXWLlLYd6jnv771wgy%2Fjibk63GkyLm2WK5oX%2B%2FyBSpXk%2BEAOzIJsObImqM69Wl5kyR8XZ2yb34qX0&X-Amz-Signature=269b0c8b73c968888f15c347b9409eabe91d179b5d7cda961c63e87d73064ce7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CF2DIR6%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHBV1e8Qv9%2FeJ8XFLiAJY8s%2Fhu%2B%2Ba8SL19A7%2BOEG6LE2AiB73dVrKuDO2X3CT1qi9AIPOfxDBg0HtaDlT3ddZMqiWyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtngm3OsDQIAgj6UVKtwDSXBTaHjexw3Y8eolSykM%2FVd1SDQdn5KoMkuQhSBmQeW23mPUQrF1fPSau%2BI5p2ADeVbFC%2BguiU6gqA06%2Bobkxi5KwePduMYVD7ZlN0pLk1CfP%2FOKRUACzUwXim7FRRmDkwdiQG6zBIT5N8Sf7BBGcQYFxXUfiqaO4g4Q40uUdDdoiYz4iRlgA6ERYog588jCVwOBWC5t0PeHA1Z%2Fm9DQRdkFbIv2S6fNCUjeGBnmS9T1Br0A1bmnqNl1Nqd1udPqixv0%2FQK0twV1erSSuCMObkVxBJ47Sy7%2BBO0VakXwPW8HT0l7pq3Bwp3B1sfrN4tF5J3cN0VSq5zP%2FEg1haEm8XM4GmArab%2BeoO40%2Ft8auwoj7RBqBOM%2FJKy5%2FNhCtx8fxmNLVYp6jVbZG3llmM3DP%2FeJH%2BS8XpisVI%2FvinetcbA%2FEeOQmD%2BzMOc6PEDMGcfd0MgU8Om1SbuRy2rtuXoxXTqBq2hUBTfLi%2ByqOvF1H7f3bddOJZR8gcDscpu7rB4IyRhA%2FkgD%2FIUnPN%2BWYWA6GznEL5c31QuZck1CUI5X5%2FOby76kvmPXyNvXEsUPo1jx9Bg9RUHAyPpN7TErxnI1fISEXguUqzE4pUSRUwXKEuqgHZwGBY%2Bntcq0iE0woP7xvAY6pgFN%2F1ezjntAdRf5ZKYu%2Fq4PPjlhIagSWpb%2FVyMtLfrE6nTsh%2Fl792cwoy1NIZrqdU3yRSbzXzXwV%2FjceN%2FEapYKDY51dKVdPhMLkKgiVFVZS%2FATTv2FFBRlGptqkKuhp4xJ22xmoW0SqFjP037%2BdhsmMc08OHkho3ZosPjtHq8ywk%2FTLx6Trothz%2BcxvJlncEnQiXu2T18hYDF%2FqDN1Kp1cZbYTcYsg&X-Amz-Signature=58f807ec0f77257856d399befc00f5f6097728810fec33214110be4be5f15bd6&X-Amz-SignedHeaders=host&x-id=GetObject)
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