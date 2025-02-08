

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UGIGXZP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIBVkIQWxg4z78DDWKZa1TN5HP6iIKOTXcvSUjc%2FnlGTjAiEA5bMbQC%2FIOtHh30ihHSOKNL1mYvTmuSVwt0dVZAmX7zMqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2FMRdBlP%2B0uuVt2dCrcAwK0A9Np6AbeuhZcpTmIoKM5Mxm8gA%2BET4Nsbnpz0GrocLtcHB93O86CO15dsV4eUJ3wXtMcDDHZbo6G%2FnXwD8ti%2BwSthT%2BbXmO8beR4tRag0uA%2FhiWL9UuS5XoXlwzl%2BaNBOoIG1sQ%2FJLEKMmO%2Fc18Ax258K%2BspNxw1dUygYSRS7BWZB3cD62CPqOQhqoGFgOhQ8Xiotb1oYrtRauZ1018Pxpb1s7Q9Wu5iL9YCR%2B1Sk8WGR7FYk4Xw2o2gwCR0WD2gttyoyR%2BCWnOhQ32XyXc5d%2BW9wKkOuvwLdYf9ANLKcFLgby1QOrQ0RQIrHX41xe3B%2FCy4raXSonhyQQBEnseOqF5rHugtg7%2Fzt2UHkpqii6ju3fR1ukO74%2FsBPqDhN9D11pAnvEDhFbkWyhvxMpgtg4QoeKGYSg5qoILMkjjDulWKdbNPIfgY2G8FsPeE5JM%2Brr6510mUxIUZgvKFImcw1iBfoppbKFtVkMYaZm0VGqUj0fziDXbNp%2F6cAovdJsQZaATFaLZCGh6fZLyqWXb8YawY9n0a%2FtU%2BI96p5zzTpaW3lwrcXrbEaY%2BdMwhrXJOltCU%2FsNQPUmZsLQfOhYkb4yrZciMaXGn5izbCC1WHp%2BiITFXeaTMFbf5yMJ2%2Bmr0GOqUBJrpWtLNW05vX%2BXEKcbHtm1puCDheoh8VaCtf8eiQxzivWp%2B96DFSBjnCnJnmkUlTjOYchrKS2EV363fJLilp1DE3LECMJLPz1XOADNnJrxTopgTH%2FvgXt1wr2FJxkZ%2FEQ6PRG29CdVDEB4gTqulmsT%2BQwXqsIO%2BBF1zi4yeMHshlo%2Fz1jpf9Ov1S5iwOHEyUvaGr%2Fp0ZfDi4ExA5AhVwZOrXWy3q&X-Amz-Signature=dabf935da7cf7d3a682cc493f476984b92ed8552d5ad9b01c9c29920b539f4bd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UGIGXZP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIBVkIQWxg4z78DDWKZa1TN5HP6iIKOTXcvSUjc%2FnlGTjAiEA5bMbQC%2FIOtHh30ihHSOKNL1mYvTmuSVwt0dVZAmX7zMqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2FMRdBlP%2B0uuVt2dCrcAwK0A9Np6AbeuhZcpTmIoKM5Mxm8gA%2BET4Nsbnpz0GrocLtcHB93O86CO15dsV4eUJ3wXtMcDDHZbo6G%2FnXwD8ti%2BwSthT%2BbXmO8beR4tRag0uA%2FhiWL9UuS5XoXlwzl%2BaNBOoIG1sQ%2FJLEKMmO%2Fc18Ax258K%2BspNxw1dUygYSRS7BWZB3cD62CPqOQhqoGFgOhQ8Xiotb1oYrtRauZ1018Pxpb1s7Q9Wu5iL9YCR%2B1Sk8WGR7FYk4Xw2o2gwCR0WD2gttyoyR%2BCWnOhQ32XyXc5d%2BW9wKkOuvwLdYf9ANLKcFLgby1QOrQ0RQIrHX41xe3B%2FCy4raXSonhyQQBEnseOqF5rHugtg7%2Fzt2UHkpqii6ju3fR1ukO74%2FsBPqDhN9D11pAnvEDhFbkWyhvxMpgtg4QoeKGYSg5qoILMkjjDulWKdbNPIfgY2G8FsPeE5JM%2Brr6510mUxIUZgvKFImcw1iBfoppbKFtVkMYaZm0VGqUj0fziDXbNp%2F6cAovdJsQZaATFaLZCGh6fZLyqWXb8YawY9n0a%2FtU%2BI96p5zzTpaW3lwrcXrbEaY%2BdMwhrXJOltCU%2FsNQPUmZsLQfOhYkb4yrZciMaXGn5izbCC1WHp%2BiITFXeaTMFbf5yMJ2%2Bmr0GOqUBJrpWtLNW05vX%2BXEKcbHtm1puCDheoh8VaCtf8eiQxzivWp%2B96DFSBjnCnJnmkUlTjOYchrKS2EV363fJLilp1DE3LECMJLPz1XOADNnJrxTopgTH%2FvgXt1wr2FJxkZ%2FEQ6PRG29CdVDEB4gTqulmsT%2BQwXqsIO%2BBF1zi4yeMHshlo%2Fz1jpf9Ov1S5iwOHEyUvaGr%2Fp0ZfDi4ExA5AhVwZOrXWy3q&X-Amz-Signature=46c5261d0573f991242cca2b9c7c84d3b8cac12a9b50808151832d77ddf23360&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UGIGXZP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIBVkIQWxg4z78DDWKZa1TN5HP6iIKOTXcvSUjc%2FnlGTjAiEA5bMbQC%2FIOtHh30ihHSOKNL1mYvTmuSVwt0dVZAmX7zMqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2FMRdBlP%2B0uuVt2dCrcAwK0A9Np6AbeuhZcpTmIoKM5Mxm8gA%2BET4Nsbnpz0GrocLtcHB93O86CO15dsV4eUJ3wXtMcDDHZbo6G%2FnXwD8ti%2BwSthT%2BbXmO8beR4tRag0uA%2FhiWL9UuS5XoXlwzl%2BaNBOoIG1sQ%2FJLEKMmO%2Fc18Ax258K%2BspNxw1dUygYSRS7BWZB3cD62CPqOQhqoGFgOhQ8Xiotb1oYrtRauZ1018Pxpb1s7Q9Wu5iL9YCR%2B1Sk8WGR7FYk4Xw2o2gwCR0WD2gttyoyR%2BCWnOhQ32XyXc5d%2BW9wKkOuvwLdYf9ANLKcFLgby1QOrQ0RQIrHX41xe3B%2FCy4raXSonhyQQBEnseOqF5rHugtg7%2Fzt2UHkpqii6ju3fR1ukO74%2FsBPqDhN9D11pAnvEDhFbkWyhvxMpgtg4QoeKGYSg5qoILMkjjDulWKdbNPIfgY2G8FsPeE5JM%2Brr6510mUxIUZgvKFImcw1iBfoppbKFtVkMYaZm0VGqUj0fziDXbNp%2F6cAovdJsQZaATFaLZCGh6fZLyqWXb8YawY9n0a%2FtU%2BI96p5zzTpaW3lwrcXrbEaY%2BdMwhrXJOltCU%2FsNQPUmZsLQfOhYkb4yrZciMaXGn5izbCC1WHp%2BiITFXeaTMFbf5yMJ2%2Bmr0GOqUBJrpWtLNW05vX%2BXEKcbHtm1puCDheoh8VaCtf8eiQxzivWp%2B96DFSBjnCnJnmkUlTjOYchrKS2EV363fJLilp1DE3LECMJLPz1XOADNnJrxTopgTH%2FvgXt1wr2FJxkZ%2FEQ6PRG29CdVDEB4gTqulmsT%2BQwXqsIO%2BBF1zi4yeMHshlo%2Fz1jpf9Ov1S5iwOHEyUvaGr%2Fp0ZfDi4ExA5AhVwZOrXWy3q&X-Amz-Signature=312bca774601b85c9d6b392d61ac65ccb94088e52cad0fda7677843b02825569&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466756KSNHQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJIMEYCIQDPV%2BmdpIqBkukuFVHOV0WlnpTLsmk%2BtLYJgcbKjU3S5QIhAIl7LyUMl%2FJwdt%2Fau%2BICAGl5NQcVOUXuf%2FeFEgCBORsjKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHeDVrsknj9%2B%2BSTdMq3AMmaHDYaREFellZmTwFg%2FIIW04aYcQQhN0hQPpMN2O%2FFmxGTH%2FvRTBn4pDDTqgfCjFsxRN6HRFD7w%2FyemQ5p1iXhp8EVxoE%2B7ZQuKbHBfYOlpwwrUzPxiMj10UwyroPtbn%2FVROZj1Rn%2BG%2FFDChuivLivnj9AXxkLubS850YuO22y9QvimW01nQCd%2BNlrXfS9LZJZB1%2BEHdQqbnqyiME2maHLMQ6kUkQkRaGn%2FFeHMhO8PUIPU1ZBu7uTQKuy5zuBiJO8CR%2Bbijo5tOJc9zHpFbLmYxPUO9LLnpRs9zfqrX7iLw%2BJQRocDTQa3hI1Iy5jvUU31pzVZQgA3EZ8q4WbuZnrgR5GqBBS9FlS8plfCvSWr%2FmXT4Bo1BtCk%2BnwugU71pFyUGJ9THzgXF%2BdkbPf%2B5yyTKFj3EoaJGUt1kzRVZleXHsrqnOhuij%2FYLbgfTAdKNRXPeoqcquswFgUJi55YBj7E0I03EVQJk%2FcR%2FCTDYa95yUzPCpZbr3EXg5RTr6KvDPiWdoA1RlhCl8jW1%2B7TprMTFyAguQB5KCDr7Pj%2BQr0LToVxNL1u6nTuR823PrOCxQqrh3CAjNX%2BCNdYUY5nN0DOvR5wAO0dzL%2FGrMXske4T%2BD5ayW9MD569vH9DCevpq9BjqkARixCBS5%2B%2BsTjjG%2FNa0TId9yiuSV8oU1OTjjRTga%2Bjx1UMI%2FRDxhWFjgJnDWb6p0kq%2FtsMZOQ1%2B6HRZy1KY84WgUUCx2yghGPgNZeuLRbj8vNur%2FJvpaBxxtNeoCU0mCXKVd4%2B1rCOz%2FZkq9jyvASjVjlzr7qRXieRjSvPATiI2jLOKUgJWsDutOR1BsH3EaR40ad6%2BLuCo4hxVdcH2nEO%2BT3wd0&X-Amz-Signature=509b937743a65569f3d9136f2f4bb843c506b7721934df1f9267d56a5dd1ac95&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466756KSNHQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJIMEYCIQDPV%2BmdpIqBkukuFVHOV0WlnpTLsmk%2BtLYJgcbKjU3S5QIhAIl7LyUMl%2FJwdt%2Fau%2BICAGl5NQcVOUXuf%2FeFEgCBORsjKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHeDVrsknj9%2B%2BSTdMq3AMmaHDYaREFellZmTwFg%2FIIW04aYcQQhN0hQPpMN2O%2FFmxGTH%2FvRTBn4pDDTqgfCjFsxRN6HRFD7w%2FyemQ5p1iXhp8EVxoE%2B7ZQuKbHBfYOlpwwrUzPxiMj10UwyroPtbn%2FVROZj1Rn%2BG%2FFDChuivLivnj9AXxkLubS850YuO22y9QvimW01nQCd%2BNlrXfS9LZJZB1%2BEHdQqbnqyiME2maHLMQ6kUkQkRaGn%2FFeHMhO8PUIPU1ZBu7uTQKuy5zuBiJO8CR%2Bbijo5tOJc9zHpFbLmYxPUO9LLnpRs9zfqrX7iLw%2BJQRocDTQa3hI1Iy5jvUU31pzVZQgA3EZ8q4WbuZnrgR5GqBBS9FlS8plfCvSWr%2FmXT4Bo1BtCk%2BnwugU71pFyUGJ9THzgXF%2BdkbPf%2B5yyTKFj3EoaJGUt1kzRVZleXHsrqnOhuij%2FYLbgfTAdKNRXPeoqcquswFgUJi55YBj7E0I03EVQJk%2FcR%2FCTDYa95yUzPCpZbr3EXg5RTr6KvDPiWdoA1RlhCl8jW1%2B7TprMTFyAguQB5KCDr7Pj%2BQr0LToVxNL1u6nTuR823PrOCxQqrh3CAjNX%2BCNdYUY5nN0DOvR5wAO0dzL%2FGrMXske4T%2BD5ayW9MD569vH9DCevpq9BjqkARixCBS5%2B%2BsTjjG%2FNa0TId9yiuSV8oU1OTjjRTga%2Bjx1UMI%2FRDxhWFjgJnDWb6p0kq%2FtsMZOQ1%2B6HRZy1KY84WgUUCx2yghGPgNZeuLRbj8vNur%2FJvpaBxxtNeoCU0mCXKVd4%2B1rCOz%2FZkq9jyvASjVjlzr7qRXieRjSvPATiI2jLOKUgJWsDutOR1BsH3EaR40ad6%2BLuCo4hxVdcH2nEO%2BT3wd0&X-Amz-Signature=63b4f17650955551063f1ed4ea3262637490a34f4e368aa8ccf4da907e7620f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UGIGXZP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T010730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJHMEUCIBVkIQWxg4z78DDWKZa1TN5HP6iIKOTXcvSUjc%2FnlGTjAiEA5bMbQC%2FIOtHh30ihHSOKNL1mYvTmuSVwt0dVZAmX7zMqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2FMRdBlP%2B0uuVt2dCrcAwK0A9Np6AbeuhZcpTmIoKM5Mxm8gA%2BET4Nsbnpz0GrocLtcHB93O86CO15dsV4eUJ3wXtMcDDHZbo6G%2FnXwD8ti%2BwSthT%2BbXmO8beR4tRag0uA%2FhiWL9UuS5XoXlwzl%2BaNBOoIG1sQ%2FJLEKMmO%2Fc18Ax258K%2BspNxw1dUygYSRS7BWZB3cD62CPqOQhqoGFgOhQ8Xiotb1oYrtRauZ1018Pxpb1s7Q9Wu5iL9YCR%2B1Sk8WGR7FYk4Xw2o2gwCR0WD2gttyoyR%2BCWnOhQ32XyXc5d%2BW9wKkOuvwLdYf9ANLKcFLgby1QOrQ0RQIrHX41xe3B%2FCy4raXSonhyQQBEnseOqF5rHugtg7%2Fzt2UHkpqii6ju3fR1ukO74%2FsBPqDhN9D11pAnvEDhFbkWyhvxMpgtg4QoeKGYSg5qoILMkjjDulWKdbNPIfgY2G8FsPeE5JM%2Brr6510mUxIUZgvKFImcw1iBfoppbKFtVkMYaZm0VGqUj0fziDXbNp%2F6cAovdJsQZaATFaLZCGh6fZLyqWXb8YawY9n0a%2FtU%2BI96p5zzTpaW3lwrcXrbEaY%2BdMwhrXJOltCU%2FsNQPUmZsLQfOhYkb4yrZciMaXGn5izbCC1WHp%2BiITFXeaTMFbf5yMJ2%2Bmr0GOqUBJrpWtLNW05vX%2BXEKcbHtm1puCDheoh8VaCtf8eiQxzivWp%2B96DFSBjnCnJnmkUlTjOYchrKS2EV363fJLilp1DE3LECMJLPz1XOADNnJrxTopgTH%2FvgXt1wr2FJxkZ%2FEQ6PRG29CdVDEB4gTqulmsT%2BQwXqsIO%2BBF1zi4yeMHshlo%2Fz1jpf9Ov1S5iwOHEyUvaGr%2Fp0ZfDi4ExA5AhVwZOrXWy3q&X-Amz-Signature=6eb489242c16bd650063213dd1d910db8afc8aadd1c0ee820c2a7f0f124b8670&X-Amz-SignedHeaders=host&x-id=GetObject)
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