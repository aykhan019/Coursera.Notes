

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3MGO5EY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDuOZoGeBYHHgQp8pJFITyx5yT6XxPN7tCqJqSxT%2BMxogIhAMUvEJIwR2Q3LvHIQEfsXQBaQtSrWXRUyK3bAahSTJilKv8DCGYQABoMNjM3NDIzMTgzODA1IgxRP3eCbzEQ1lLc%2FYQq3AMDCj%2BciUjsc9DHBOb90QprZwHAEzXJXmqiM0pyi1rcpc62Q3M%2BSHuSNYsjz%2BOYHEYl4T5aLx%2BrgpoEK0niMaDL3UqiHD15cb0feCEi2eCjJ%2FC%2FjkzINc1zHxPS3iJRPFOfq%2FycqOV9FPgu%2FE%2BU%2BYQfMtcNytc95OXJYQhFNDBCMKwlOUPk5Kdjw08hsX5frG9xqF1VElgZ3MRCZ4zlTPnPju0zIz25dta4jKGeE2Iemv%2Bkv7RxBkyvyElegMODUGbGyhJ51lgp3GT9lpXnYzBHo%2F8y2ac2miqbb%2BUecQCpyPj1Bl9DraDAx5WyIkvVlK7dAit17%2BmiJ70bBNqZDZ8KnABGJU3EaGe9ur4ZQmluNB0ip2xvcIYrNYVt%2FOchm6YXRh98AAPcVvHcIaYOnIpcTyp4b9ymeWUzozD4PmsZYHi6Wg5o1AyXwM5gJuYK5JllCQxg6DgFOaWO5CO5wfU6LAH617wHloa%2FdyjlP62VHoD9WpX4rNSBwpuLneZuLYjG2ZOc8U2KrYU2QAyI5s15sMoLYYMtr1GNZziumS3%2BozRTOd2ZMB1S44ifn6m%2BB%2FsEiNxM2tksF8oYGv5k8Dt%2BY3M294dYWPHkGmz330qrLwyJ2keWeKaYMRqKUTDKuJS9BjqkAdRxVvRA8Izuo1vC9Td6r8mBVbu7%2F%2BhZLgXKLBjXMUh142Z90D3FqmN5cmBxELlgpJTE3H2%2BY6qdKCx7gXT%2BSBy0xSLEVfy%2FL54LR%2BA9hYpSgxXQq2HHRvPf75O25hI9qp0WB8VByM70Ibf1toDtu5FeBovHbT%2FNBy7sMJtePi8eIGhXJGAsocPAPvB9J9h5MAR8De4XFBfRrVnwQdB9Nwltmyb9&X-Amz-Signature=699065eabf407bb9ee2e5aa8dfb58be26d3cffba5bf0be9ef803a21ca100ed7e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3MGO5EY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDuOZoGeBYHHgQp8pJFITyx5yT6XxPN7tCqJqSxT%2BMxogIhAMUvEJIwR2Q3LvHIQEfsXQBaQtSrWXRUyK3bAahSTJilKv8DCGYQABoMNjM3NDIzMTgzODA1IgxRP3eCbzEQ1lLc%2FYQq3AMDCj%2BciUjsc9DHBOb90QprZwHAEzXJXmqiM0pyi1rcpc62Q3M%2BSHuSNYsjz%2BOYHEYl4T5aLx%2BrgpoEK0niMaDL3UqiHD15cb0feCEi2eCjJ%2FC%2FjkzINc1zHxPS3iJRPFOfq%2FycqOV9FPgu%2FE%2BU%2BYQfMtcNytc95OXJYQhFNDBCMKwlOUPk5Kdjw08hsX5frG9xqF1VElgZ3MRCZ4zlTPnPju0zIz25dta4jKGeE2Iemv%2Bkv7RxBkyvyElegMODUGbGyhJ51lgp3GT9lpXnYzBHo%2F8y2ac2miqbb%2BUecQCpyPj1Bl9DraDAx5WyIkvVlK7dAit17%2BmiJ70bBNqZDZ8KnABGJU3EaGe9ur4ZQmluNB0ip2xvcIYrNYVt%2FOchm6YXRh98AAPcVvHcIaYOnIpcTyp4b9ymeWUzozD4PmsZYHi6Wg5o1AyXwM5gJuYK5JllCQxg6DgFOaWO5CO5wfU6LAH617wHloa%2FdyjlP62VHoD9WpX4rNSBwpuLneZuLYjG2ZOc8U2KrYU2QAyI5s15sMoLYYMtr1GNZziumS3%2BozRTOd2ZMB1S44ifn6m%2BB%2FsEiNxM2tksF8oYGv5k8Dt%2BY3M294dYWPHkGmz330qrLwyJ2keWeKaYMRqKUTDKuJS9BjqkAdRxVvRA8Izuo1vC9Td6r8mBVbu7%2F%2BhZLgXKLBjXMUh142Z90D3FqmN5cmBxELlgpJTE3H2%2BY6qdKCx7gXT%2BSBy0xSLEVfy%2FL54LR%2BA9hYpSgxXQq2HHRvPf75O25hI9qp0WB8VByM70Ibf1toDtu5FeBovHbT%2FNBy7sMJtePi8eIGhXJGAsocPAPvB9J9h5MAR8De4XFBfRrVnwQdB9Nwltmyb9&X-Amz-Signature=9b28bf191a665662aec89dcbee3aa147bc03faa4daf60a467f6d252a2e5a45a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3MGO5EY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDuOZoGeBYHHgQp8pJFITyx5yT6XxPN7tCqJqSxT%2BMxogIhAMUvEJIwR2Q3LvHIQEfsXQBaQtSrWXRUyK3bAahSTJilKv8DCGYQABoMNjM3NDIzMTgzODA1IgxRP3eCbzEQ1lLc%2FYQq3AMDCj%2BciUjsc9DHBOb90QprZwHAEzXJXmqiM0pyi1rcpc62Q3M%2BSHuSNYsjz%2BOYHEYl4T5aLx%2BrgpoEK0niMaDL3UqiHD15cb0feCEi2eCjJ%2FC%2FjkzINc1zHxPS3iJRPFOfq%2FycqOV9FPgu%2FE%2BU%2BYQfMtcNytc95OXJYQhFNDBCMKwlOUPk5Kdjw08hsX5frG9xqF1VElgZ3MRCZ4zlTPnPju0zIz25dta4jKGeE2Iemv%2Bkv7RxBkyvyElegMODUGbGyhJ51lgp3GT9lpXnYzBHo%2F8y2ac2miqbb%2BUecQCpyPj1Bl9DraDAx5WyIkvVlK7dAit17%2BmiJ70bBNqZDZ8KnABGJU3EaGe9ur4ZQmluNB0ip2xvcIYrNYVt%2FOchm6YXRh98AAPcVvHcIaYOnIpcTyp4b9ymeWUzozD4PmsZYHi6Wg5o1AyXwM5gJuYK5JllCQxg6DgFOaWO5CO5wfU6LAH617wHloa%2FdyjlP62VHoD9WpX4rNSBwpuLneZuLYjG2ZOc8U2KrYU2QAyI5s15sMoLYYMtr1GNZziumS3%2BozRTOd2ZMB1S44ifn6m%2BB%2FsEiNxM2tksF8oYGv5k8Dt%2BY3M294dYWPHkGmz330qrLwyJ2keWeKaYMRqKUTDKuJS9BjqkAdRxVvRA8Izuo1vC9Td6r8mBVbu7%2F%2BhZLgXKLBjXMUh142Z90D3FqmN5cmBxELlgpJTE3H2%2BY6qdKCx7gXT%2BSBy0xSLEVfy%2FL54LR%2BA9hYpSgxXQq2HHRvPf75O25hI9qp0WB8VByM70Ibf1toDtu5FeBovHbT%2FNBy7sMJtePi8eIGhXJGAsocPAPvB9J9h5MAR8De4XFBfRrVnwQdB9Nwltmyb9&X-Amz-Signature=d9fa24a20939a64c3489df5403d8029a8a382147ff4626d90ef38858d0df7b06&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZORTFH26%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIDD735xVdilDGvsXXHY8C7aE41g6gEszzQVdNgg8VBikAiB9JCnnSjtbdEQidE3CPlTPxN9aYA6pXttvSX16RVrejCr%2FAwhlEAAaDDYzNzQyMzE4MzgwNSIMWkyfc221D3OCpVEkKtwDQXNgmrf34W8M%2Bn%2FSrEVM6s44kwPYQE3tRbOhjcUWbwUvna2ZqJKnvAI%2BtrlOW4aMElcwvWDor25NoJr2XAGYWIZayYAM8ikLCHN4q5tkHK1DJlzYOaaUGL%2BBnZIqGNiKSac%2Bjc%2F4rkbwBXLMphEzBbPWKRbF4c9JXLZsaisPB7PF9RVUtKkGlxYnYyUbTropVrmo8bDy9%2Bgi5a3dQ6kDbKta6xu5rUEGTrBeUc69UBn5txttuEgX6yx3BMrUmP%2FoHHFNCVsLHhR00O6ZzUYbifpYZ0Umw7sEQOysgRp3VQR0rjyjgSu7hiuvQM5Le79JYv8FIay7cX86C%2B%2Fb1tvEEqpRvo6RUBYlMoVjHGKVtaC3ZNIyJWVBsIBqEynxNgiSdPbxrrFsfkaeoBqOEtKXOXc1OC8SGJ7yWZkJKHBNaeogbUd6NgGgRnMgRUFPx%2FLSJe0i%2FfFJeD4Ici2wJZJhl4IEleNVnwwAKAT9HjoDBlRHDAYV5gtcLfPp00LDu98hAgVDHYSW%2BAxqBOsnXxTh0RS2pEjTE2ONVmZN5cqMEdp9xkJrjtjtUVq%2F%2BQrBNbu1UadS3mTTuUy1ZKVyUsWB0mS2rb18oPnsciVfB7bRgyJDAKxivA101tSCz%2Bow67eUvQY6pgGAxJm2sDpD9TlMkkQ1INN0PpPXp71s3KWudqfujuqjcoILFU7EfFFSsTr5K5Jlz3a82YlMMSj9GNHcwkmdiZUP9rtWytt%2FHw3SVLCKxbzr0i3oBHZNOoqQ7OCFkW9UV5P9IYo1JqeDQu9dJmAzErH0GcIzkElinnL9pUfR6YhUSKUoST272C6Tu%2Fh2rL55wiXUBWyT18GVkKLSW2sfHS3ptonXYBaQ&X-Amz-Signature=6a7e0973195fc705c06942009d70bcef9f71b2290b6621f21a61b30b167b1e19&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZORTFH26%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIDD735xVdilDGvsXXHY8C7aE41g6gEszzQVdNgg8VBikAiB9JCnnSjtbdEQidE3CPlTPxN9aYA6pXttvSX16RVrejCr%2FAwhlEAAaDDYzNzQyMzE4MzgwNSIMWkyfc221D3OCpVEkKtwDQXNgmrf34W8M%2Bn%2FSrEVM6s44kwPYQE3tRbOhjcUWbwUvna2ZqJKnvAI%2BtrlOW4aMElcwvWDor25NoJr2XAGYWIZayYAM8ikLCHN4q5tkHK1DJlzYOaaUGL%2BBnZIqGNiKSac%2Bjc%2F4rkbwBXLMphEzBbPWKRbF4c9JXLZsaisPB7PF9RVUtKkGlxYnYyUbTropVrmo8bDy9%2Bgi5a3dQ6kDbKta6xu5rUEGTrBeUc69UBn5txttuEgX6yx3BMrUmP%2FoHHFNCVsLHhR00O6ZzUYbifpYZ0Umw7sEQOysgRp3VQR0rjyjgSu7hiuvQM5Le79JYv8FIay7cX86C%2B%2Fb1tvEEqpRvo6RUBYlMoVjHGKVtaC3ZNIyJWVBsIBqEynxNgiSdPbxrrFsfkaeoBqOEtKXOXc1OC8SGJ7yWZkJKHBNaeogbUd6NgGgRnMgRUFPx%2FLSJe0i%2FfFJeD4Ici2wJZJhl4IEleNVnwwAKAT9HjoDBlRHDAYV5gtcLfPp00LDu98hAgVDHYSW%2BAxqBOsnXxTh0RS2pEjTE2ONVmZN5cqMEdp9xkJrjtjtUVq%2F%2BQrBNbu1UadS3mTTuUy1ZKVyUsWB0mS2rb18oPnsciVfB7bRgyJDAKxivA101tSCz%2Bow67eUvQY6pgGAxJm2sDpD9TlMkkQ1INN0PpPXp71s3KWudqfujuqjcoILFU7EfFFSsTr5K5Jlz3a82YlMMSj9GNHcwkmdiZUP9rtWytt%2FHw3SVLCKxbzr0i3oBHZNOoqQ7OCFkW9UV5P9IYo1JqeDQu9dJmAzErH0GcIzkElinnL9pUfR6YhUSKUoST272C6Tu%2Fh2rL55wiXUBWyT18GVkKLSW2sfHS3ptonXYBaQ&X-Amz-Signature=56bc01d4f3d1f71dfea5d19ab8531d9e577633aa9fe8bb0aa7a81a0e6c662a7d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3MGO5EY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDuOZoGeBYHHgQp8pJFITyx5yT6XxPN7tCqJqSxT%2BMxogIhAMUvEJIwR2Q3LvHIQEfsXQBaQtSrWXRUyK3bAahSTJilKv8DCGYQABoMNjM3NDIzMTgzODA1IgxRP3eCbzEQ1lLc%2FYQq3AMDCj%2BciUjsc9DHBOb90QprZwHAEzXJXmqiM0pyi1rcpc62Q3M%2BSHuSNYsjz%2BOYHEYl4T5aLx%2BrgpoEK0niMaDL3UqiHD15cb0feCEi2eCjJ%2FC%2FjkzINc1zHxPS3iJRPFOfq%2FycqOV9FPgu%2FE%2BU%2BYQfMtcNytc95OXJYQhFNDBCMKwlOUPk5Kdjw08hsX5frG9xqF1VElgZ3MRCZ4zlTPnPju0zIz25dta4jKGeE2Iemv%2Bkv7RxBkyvyElegMODUGbGyhJ51lgp3GT9lpXnYzBHo%2F8y2ac2miqbb%2BUecQCpyPj1Bl9DraDAx5WyIkvVlK7dAit17%2BmiJ70bBNqZDZ8KnABGJU3EaGe9ur4ZQmluNB0ip2xvcIYrNYVt%2FOchm6YXRh98AAPcVvHcIaYOnIpcTyp4b9ymeWUzozD4PmsZYHi6Wg5o1AyXwM5gJuYK5JllCQxg6DgFOaWO5CO5wfU6LAH617wHloa%2FdyjlP62VHoD9WpX4rNSBwpuLneZuLYjG2ZOc8U2KrYU2QAyI5s15sMoLYYMtr1GNZziumS3%2BozRTOd2ZMB1S44ifn6m%2BB%2FsEiNxM2tksF8oYGv5k8Dt%2BY3M294dYWPHkGmz330qrLwyJ2keWeKaYMRqKUTDKuJS9BjqkAdRxVvRA8Izuo1vC9Td6r8mBVbu7%2F%2BhZLgXKLBjXMUh142Z90D3FqmN5cmBxELlgpJTE3H2%2BY6qdKCx7gXT%2BSBy0xSLEVfy%2FL54LR%2BA9hYpSgxXQq2HHRvPf75O25hI9qp0WB8VByM70Ibf1toDtu5FeBovHbT%2FNBy7sMJtePi8eIGhXJGAsocPAPvB9J9h5MAR8De4XFBfRrVnwQdB9Nwltmyb9&X-Amz-Signature=225c211473753fc857177a78ac0ff48755f7ee05dd494aeb147aaa05583a6051&X-Amz-SignedHeaders=host&x-id=GetObject)
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