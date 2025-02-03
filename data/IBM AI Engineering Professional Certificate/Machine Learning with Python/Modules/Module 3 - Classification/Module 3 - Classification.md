

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZF6AXOXN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIAVAuKqt84ln1D4EU1eVrxJ6Q4u3hrZlcyCpfsyn%2BQjcAiEA0lV4zBKRO37HhZ6q1tTTvwlqcJtWlFcpwgfxvu4vXwAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDMKM8fBKBWfD1YL8UCrcA%2FN4YG24clW6vqOfGn4ea0VqUUwhcgB0xFkLzjkYgQ25rkytYL5ZwArvmotDlhv3jm0gG6%2FiYJXtfzB%2B785fadSuFyPh3rzCQ1nM7ZNu6hG12mgY5yRQgUuaqbQ1CC1LGgZq0fg8j8SwtHltGWmOZ8FOI0n6Se1XYZiX0rMSUQayLI9egiUIfTc917CF6vT45W6%2FMbr1F5gUrzch34vA9hhM4cRzRD18OlmEi8Zr68ofGNxDObR3ZWPzRetw506MAjMss7MB12R%2Bvx6GM8C5mmjFV7SFsun7RBZr8PPq27m%2BgG7KH%2FDNjZ7dimcYupVn1ExWJ03g%2BeYr8EK4OVdnjk4Hlkje2MRIsGhtiy3Q9Seuh8GS7R7viptTmVQzYDk4NBY9SWPNTc22a1TK7Ct6dHw24LCbJh%2BUKzGVRXEbhl8fi%2BaWU3%2FhdAJVuDKcxAI1d3642LO%2Bk5sd7a6tcSpm1E%2B3O1izXqbQqTG%2BLjuieji%2B5tBIrK7Wjzn%2B4Thijg1nKg%2BsfhA9ahHO2FmSS9PE%2BgYty6yG8BZ%2BYHp5EIaChK5VtCbe3aSIOay%2B9ic5uzQayXDS7%2FUJCv6hUPR1Jb83N6mIokyA78D%2BlieFCBSgMkiFm7JjC3OjaagmcaEbMPeThb0GOqUBodRFJ6Qa34081yx42rmY3aOWn3gLS7nn%2FtXWTDaPj7Uc2FqtSByeRdWKZ1W5Pd9FaDVbzXqjrdni3n%2FGBpqGiwWkL1KQNkZczr1LiIjRqhxELV26dx9gIZdOcyyuuYYjE27ZQV0sltxtYjI%2F1j1TVidi%2Beq63XJ8X%2BIqmW3LYshls%2BZNMinlIXFTFH8LNFrgx7pVmS0UJnSreMsAZ%2BqXe2joK56U&X-Amz-Signature=822f6faa75aa30e6500d8212266404cc322941ddf045000f4eef5f9a9cfbf868&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZF6AXOXN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIAVAuKqt84ln1D4EU1eVrxJ6Q4u3hrZlcyCpfsyn%2BQjcAiEA0lV4zBKRO37HhZ6q1tTTvwlqcJtWlFcpwgfxvu4vXwAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDMKM8fBKBWfD1YL8UCrcA%2FN4YG24clW6vqOfGn4ea0VqUUwhcgB0xFkLzjkYgQ25rkytYL5ZwArvmotDlhv3jm0gG6%2FiYJXtfzB%2B785fadSuFyPh3rzCQ1nM7ZNu6hG12mgY5yRQgUuaqbQ1CC1LGgZq0fg8j8SwtHltGWmOZ8FOI0n6Se1XYZiX0rMSUQayLI9egiUIfTc917CF6vT45W6%2FMbr1F5gUrzch34vA9hhM4cRzRD18OlmEi8Zr68ofGNxDObR3ZWPzRetw506MAjMss7MB12R%2Bvx6GM8C5mmjFV7SFsun7RBZr8PPq27m%2BgG7KH%2FDNjZ7dimcYupVn1ExWJ03g%2BeYr8EK4OVdnjk4Hlkje2MRIsGhtiy3Q9Seuh8GS7R7viptTmVQzYDk4NBY9SWPNTc22a1TK7Ct6dHw24LCbJh%2BUKzGVRXEbhl8fi%2BaWU3%2FhdAJVuDKcxAI1d3642LO%2Bk5sd7a6tcSpm1E%2B3O1izXqbQqTG%2BLjuieji%2B5tBIrK7Wjzn%2B4Thijg1nKg%2BsfhA9ahHO2FmSS9PE%2BgYty6yG8BZ%2BYHp5EIaChK5VtCbe3aSIOay%2B9ic5uzQayXDS7%2FUJCv6hUPR1Jb83N6mIokyA78D%2BlieFCBSgMkiFm7JjC3OjaagmcaEbMPeThb0GOqUBodRFJ6Qa34081yx42rmY3aOWn3gLS7nn%2FtXWTDaPj7Uc2FqtSByeRdWKZ1W5Pd9FaDVbzXqjrdni3n%2FGBpqGiwWkL1KQNkZczr1LiIjRqhxELV26dx9gIZdOcyyuuYYjE27ZQV0sltxtYjI%2F1j1TVidi%2Beq63XJ8X%2BIqmW3LYshls%2BZNMinlIXFTFH8LNFrgx7pVmS0UJnSreMsAZ%2BqXe2joK56U&X-Amz-Signature=14652840184ef4c0781418b21bfd17f7e364f3ee55373544c2290d4f0e4b99b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZF6AXOXN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIAVAuKqt84ln1D4EU1eVrxJ6Q4u3hrZlcyCpfsyn%2BQjcAiEA0lV4zBKRO37HhZ6q1tTTvwlqcJtWlFcpwgfxvu4vXwAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDMKM8fBKBWfD1YL8UCrcA%2FN4YG24clW6vqOfGn4ea0VqUUwhcgB0xFkLzjkYgQ25rkytYL5ZwArvmotDlhv3jm0gG6%2FiYJXtfzB%2B785fadSuFyPh3rzCQ1nM7ZNu6hG12mgY5yRQgUuaqbQ1CC1LGgZq0fg8j8SwtHltGWmOZ8FOI0n6Se1XYZiX0rMSUQayLI9egiUIfTc917CF6vT45W6%2FMbr1F5gUrzch34vA9hhM4cRzRD18OlmEi8Zr68ofGNxDObR3ZWPzRetw506MAjMss7MB12R%2Bvx6GM8C5mmjFV7SFsun7RBZr8PPq27m%2BgG7KH%2FDNjZ7dimcYupVn1ExWJ03g%2BeYr8EK4OVdnjk4Hlkje2MRIsGhtiy3Q9Seuh8GS7R7viptTmVQzYDk4NBY9SWPNTc22a1TK7Ct6dHw24LCbJh%2BUKzGVRXEbhl8fi%2BaWU3%2FhdAJVuDKcxAI1d3642LO%2Bk5sd7a6tcSpm1E%2B3O1izXqbQqTG%2BLjuieji%2B5tBIrK7Wjzn%2B4Thijg1nKg%2BsfhA9ahHO2FmSS9PE%2BgYty6yG8BZ%2BYHp5EIaChK5VtCbe3aSIOay%2B9ic5uzQayXDS7%2FUJCv6hUPR1Jb83N6mIokyA78D%2BlieFCBSgMkiFm7JjC3OjaagmcaEbMPeThb0GOqUBodRFJ6Qa34081yx42rmY3aOWn3gLS7nn%2FtXWTDaPj7Uc2FqtSByeRdWKZ1W5Pd9FaDVbzXqjrdni3n%2FGBpqGiwWkL1KQNkZczr1LiIjRqhxELV26dx9gIZdOcyyuuYYjE27ZQV0sltxtYjI%2F1j1TVidi%2Beq63XJ8X%2BIqmW3LYshls%2BZNMinlIXFTFH8LNFrgx7pVmS0UJnSreMsAZ%2BqXe2joK56U&X-Amz-Signature=d89bb9262f4269cb4f7ff3e930f78d5798d8342193a48201739b0888a0e255f5&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WK6AKKZN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQC%2FbQaDeGp14LsNM1W6ySDazfwcWAfS8sMUeeau2Q0vuQIhAOFxnxUeV%2FG0G%2BcbSL5cRQneJolWZ7K6GthAdHpgM4rDKv8DCCAQABoMNjM3NDIzMTgzODA1IgzeMfmcpCOJNdU3gpcq3AO8MMDvBMSLj5s%2BkcgZMjpnAFaEbShSpMNcmAfzxtQ2PzhdAmYdquZu2UpSGuR0Obqp2vLiWIt7lYGLmxmK6i2kMtRwTxbeyAHYiap42pl8dEd81mMdnY16ALWaWOO3%2BI2chCBhRacQpBwuF2ubOB9yVhukrTTGaKvIwSyC1WYDTvLsDwaJ6ToLJmJMyiE8F0hgKZkKxI%2BcdSL0GyGBsYWqsVscpqX5xEZPhyDZn0HJsXMkl5NInlnb66tAvu4MjQ7llcUwTWMRmquj8ZtSnB5B%2FDnIaGuDsJqRkSpFEBrXxLEMPGhtrws9qvdmusS0kQ5k0xm3mI2GyEYYTS89MceqVG2vkwPGxGm7LR55u8wLnmR8pZFGxTWx9SsZ2GL4hybG1LYu9l%2Ffzq5lmUVA%2BQBMCswwzQL2wA4tKAevJsKLOjJh922Cy5tr7%2Bl5S4bFEN6mfpeFp2Js0vgtaxjLO7QMpCyTZScogtkD80SQy5yuqTVN6MZYdsjV3BC7bzHoScrhVKjTloZzNKXCHxTGSEYA60G0pH8fZkh51xcykaW3IAK6If1x4uOOOqdxZaUmA8B930ggitY1%2Br4%2BlrzAuVv7EYnLdEUdgDqOj4B0YPrJ0XUrT9e7A4LjW9CRGDDNk4W9BjqkAaZkUpw4LA%2FLLz74RzvreD2gRtisUDGtMshxKO8SWNZqhV7sLUXeDiMTt9IX8nTuu9BmiszEszgTEIjyO%2Bi1GPvHrajtwwhYszkhUrlsC5iMeBI5m6t%2BRK3eq%2Beq85xBkthv%2FxP0gjfWfr%2F6FDmmRXJwwnNOX9HOqyjydRdAksXIxNDNCsHS9ylrNCU2kEZvpsxvalkVF6eR4OpCFXaL9G4Je2wc&X-Amz-Signature=12c3f43446e3e2a4e5189a9c3b11f29fd4da45802895165b75dec3164f5a82a8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WK6AKKZN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQC%2FbQaDeGp14LsNM1W6ySDazfwcWAfS8sMUeeau2Q0vuQIhAOFxnxUeV%2FG0G%2BcbSL5cRQneJolWZ7K6GthAdHpgM4rDKv8DCCAQABoMNjM3NDIzMTgzODA1IgzeMfmcpCOJNdU3gpcq3AO8MMDvBMSLj5s%2BkcgZMjpnAFaEbShSpMNcmAfzxtQ2PzhdAmYdquZu2UpSGuR0Obqp2vLiWIt7lYGLmxmK6i2kMtRwTxbeyAHYiap42pl8dEd81mMdnY16ALWaWOO3%2BI2chCBhRacQpBwuF2ubOB9yVhukrTTGaKvIwSyC1WYDTvLsDwaJ6ToLJmJMyiE8F0hgKZkKxI%2BcdSL0GyGBsYWqsVscpqX5xEZPhyDZn0HJsXMkl5NInlnb66tAvu4MjQ7llcUwTWMRmquj8ZtSnB5B%2FDnIaGuDsJqRkSpFEBrXxLEMPGhtrws9qvdmusS0kQ5k0xm3mI2GyEYYTS89MceqVG2vkwPGxGm7LR55u8wLnmR8pZFGxTWx9SsZ2GL4hybG1LYu9l%2Ffzq5lmUVA%2BQBMCswwzQL2wA4tKAevJsKLOjJh922Cy5tr7%2Bl5S4bFEN6mfpeFp2Js0vgtaxjLO7QMpCyTZScogtkD80SQy5yuqTVN6MZYdsjV3BC7bzHoScrhVKjTloZzNKXCHxTGSEYA60G0pH8fZkh51xcykaW3IAK6If1x4uOOOqdxZaUmA8B930ggitY1%2Br4%2BlrzAuVv7EYnLdEUdgDqOj4B0YPrJ0XUrT9e7A4LjW9CRGDDNk4W9BjqkAaZkUpw4LA%2FLLz74RzvreD2gRtisUDGtMshxKO8SWNZqhV7sLUXeDiMTt9IX8nTuu9BmiszEszgTEIjyO%2Bi1GPvHrajtwwhYszkhUrlsC5iMeBI5m6t%2BRK3eq%2Beq85xBkthv%2FxP0gjfWfr%2F6FDmmRXJwwnNOX9HOqyjydRdAksXIxNDNCsHS9ylrNCU2kEZvpsxvalkVF6eR4OpCFXaL9G4Je2wc&X-Amz-Signature=4ee70a03ee364acad4234da557e75d1ad5f87a2d6bc44fcb4a7d09a8b84b7bc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZF6AXOXN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIAVAuKqt84ln1D4EU1eVrxJ6Q4u3hrZlcyCpfsyn%2BQjcAiEA0lV4zBKRO37HhZ6q1tTTvwlqcJtWlFcpwgfxvu4vXwAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDMKM8fBKBWfD1YL8UCrcA%2FN4YG24clW6vqOfGn4ea0VqUUwhcgB0xFkLzjkYgQ25rkytYL5ZwArvmotDlhv3jm0gG6%2FiYJXtfzB%2B785fadSuFyPh3rzCQ1nM7ZNu6hG12mgY5yRQgUuaqbQ1CC1LGgZq0fg8j8SwtHltGWmOZ8FOI0n6Se1XYZiX0rMSUQayLI9egiUIfTc917CF6vT45W6%2FMbr1F5gUrzch34vA9hhM4cRzRD18OlmEi8Zr68ofGNxDObR3ZWPzRetw506MAjMss7MB12R%2Bvx6GM8C5mmjFV7SFsun7RBZr8PPq27m%2BgG7KH%2FDNjZ7dimcYupVn1ExWJ03g%2BeYr8EK4OVdnjk4Hlkje2MRIsGhtiy3Q9Seuh8GS7R7viptTmVQzYDk4NBY9SWPNTc22a1TK7Ct6dHw24LCbJh%2BUKzGVRXEbhl8fi%2BaWU3%2FhdAJVuDKcxAI1d3642LO%2Bk5sd7a6tcSpm1E%2B3O1izXqbQqTG%2BLjuieji%2B5tBIrK7Wjzn%2B4Thijg1nKg%2BsfhA9ahHO2FmSS9PE%2BgYty6yG8BZ%2BYHp5EIaChK5VtCbe3aSIOay%2B9ic5uzQayXDS7%2FUJCv6hUPR1Jb83N6mIokyA78D%2BlieFCBSgMkiFm7JjC3OjaagmcaEbMPeThb0GOqUBodRFJ6Qa34081yx42rmY3aOWn3gLS7nn%2FtXWTDaPj7Uc2FqtSByeRdWKZ1W5Pd9FaDVbzXqjrdni3n%2FGBpqGiwWkL1KQNkZczr1LiIjRqhxELV26dx9gIZdOcyyuuYYjE27ZQV0sltxtYjI%2F1j1TVidi%2Beq63XJ8X%2BIqmW3LYshls%2BZNMinlIXFTFH8LNFrgx7pVmS0UJnSreMsAZ%2BqXe2joK56U&X-Amz-Signature=78cef4d0a7f802a206ca843876c06328ad0e903ae874275239d9cc9248748c65&X-Amz-SignedHeaders=host&x-id=GetObject)
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