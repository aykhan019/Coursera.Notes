

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HQKZS6B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7Q3H6L9nBM5H%2FZfjoan%2FPikV1FChd%2FjI4ZujQ2eR3HAIgX86oedjnPUCK%2BcBRuNlqteNY5%2FWHpYUnysdRW3R1DgEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOZkvA4k8cHARz57yrcA%2B5kz1jkMI70mYSSI9cC0LLMUeY5XWA9cgtFeSxA2%2BtDFagYPsezuy2shG4go2xh%2FFLKk%2Ft0ryEJRAiL7pqsyG%2Fh8IF%2FDMN9tjxS%2BU18Ve4z2H7MmpCg4gyycRCqG4Y%2BkdSiTgkw0lRAQncrp9HE51klAt%2FBZkkbsa07Bdbzd9t26v3VEYmqnGReniqAc7H8EPn3NIyLrIVrLES5w3lVQVBX8tUz0lK2mqCDIYsyuTl9x8KNzEMbJNU2BsTFP2cGBwC2OcXC8Z6G%2Fo2OBNH0GvuaqU6tybp7Tm5P%2BQu17vkFjuNkrbpj%2Fxd6NvH4xy7hkoA%2BGXpywqMSLJiqRSbAb1%2BBCnFK4Bozy0XSAZOXy%2BmK%2F1EGWzMI8rQPnj2eO6o%2F%2FhAMTM%2FOJEp4BaAjA6dgZBOJHebhXti%2BTAAG%2FyW%2BBPsQhuUd4I9JTAYdGEZtDp4hPVdJ%2BmLZt%2FsR2n%2Fe8KKv0XDnX72Uuio6CdSYz0u0qrKY2iRUxguhdglnrx7AHPRq4i4Q2h15dwgZYimKsgc4N3wIrthpzHceuWEtscElBC3716jxOYageAYptbPkcmk35%2Fyb79CFPl8T%2BksZrppUjkhuXJ%2BdxDSUBNH%2BUQmE1EKJkakYIJkNTPyN%2FakOMOPx%2BrwGOqUBXee5BsJEfrGbuo8ciUBhhAYx1YEvg2Mg86P61tDztBjD2fxXKfX%2F1P2nIlZ0iZJAzNMv2LlskuEYKOAw4fx1RKZ1kSuflqjru6nqeNHoNi3k5Yj7hPP8MNxBlyVtDKfbv2NjXEpq9FAHDXr%2FNRfkgIjihfqZO9a2qwQUAGOtczxyBKVaUEDTN9wiAtUUC3G9S1uMsRwoVHusqrBXE3ZXqPlhfF0j&X-Amz-Signature=bef5a196d7168f60da247f4cb11ecb373e39900f982924d56f916b8c8a1b0227&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HQKZS6B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7Q3H6L9nBM5H%2FZfjoan%2FPikV1FChd%2FjI4ZujQ2eR3HAIgX86oedjnPUCK%2BcBRuNlqteNY5%2FWHpYUnysdRW3R1DgEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOZkvA4k8cHARz57yrcA%2B5kz1jkMI70mYSSI9cC0LLMUeY5XWA9cgtFeSxA2%2BtDFagYPsezuy2shG4go2xh%2FFLKk%2Ft0ryEJRAiL7pqsyG%2Fh8IF%2FDMN9tjxS%2BU18Ve4z2H7MmpCg4gyycRCqG4Y%2BkdSiTgkw0lRAQncrp9HE51klAt%2FBZkkbsa07Bdbzd9t26v3VEYmqnGReniqAc7H8EPn3NIyLrIVrLES5w3lVQVBX8tUz0lK2mqCDIYsyuTl9x8KNzEMbJNU2BsTFP2cGBwC2OcXC8Z6G%2Fo2OBNH0GvuaqU6tybp7Tm5P%2BQu17vkFjuNkrbpj%2Fxd6NvH4xy7hkoA%2BGXpywqMSLJiqRSbAb1%2BBCnFK4Bozy0XSAZOXy%2BmK%2F1EGWzMI8rQPnj2eO6o%2F%2FhAMTM%2FOJEp4BaAjA6dgZBOJHebhXti%2BTAAG%2FyW%2BBPsQhuUd4I9JTAYdGEZtDp4hPVdJ%2BmLZt%2FsR2n%2Fe8KKv0XDnX72Uuio6CdSYz0u0qrKY2iRUxguhdglnrx7AHPRq4i4Q2h15dwgZYimKsgc4N3wIrthpzHceuWEtscElBC3716jxOYageAYptbPkcmk35%2Fyb79CFPl8T%2BksZrppUjkhuXJ%2BdxDSUBNH%2BUQmE1EKJkakYIJkNTPyN%2FakOMOPx%2BrwGOqUBXee5BsJEfrGbuo8ciUBhhAYx1YEvg2Mg86P61tDztBjD2fxXKfX%2F1P2nIlZ0iZJAzNMv2LlskuEYKOAw4fx1RKZ1kSuflqjru6nqeNHoNi3k5Yj7hPP8MNxBlyVtDKfbv2NjXEpq9FAHDXr%2FNRfkgIjihfqZO9a2qwQUAGOtczxyBKVaUEDTN9wiAtUUC3G9S1uMsRwoVHusqrBXE3ZXqPlhfF0j&X-Amz-Signature=3d360967f0e13a0f7d77eede596ab4cbf3fae4731906c4de13f60efce91ef73b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HQKZS6B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7Q3H6L9nBM5H%2FZfjoan%2FPikV1FChd%2FjI4ZujQ2eR3HAIgX86oedjnPUCK%2BcBRuNlqteNY5%2FWHpYUnysdRW3R1DgEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOZkvA4k8cHARz57yrcA%2B5kz1jkMI70mYSSI9cC0LLMUeY5XWA9cgtFeSxA2%2BtDFagYPsezuy2shG4go2xh%2FFLKk%2Ft0ryEJRAiL7pqsyG%2Fh8IF%2FDMN9tjxS%2BU18Ve4z2H7MmpCg4gyycRCqG4Y%2BkdSiTgkw0lRAQncrp9HE51klAt%2FBZkkbsa07Bdbzd9t26v3VEYmqnGReniqAc7H8EPn3NIyLrIVrLES5w3lVQVBX8tUz0lK2mqCDIYsyuTl9x8KNzEMbJNU2BsTFP2cGBwC2OcXC8Z6G%2Fo2OBNH0GvuaqU6tybp7Tm5P%2BQu17vkFjuNkrbpj%2Fxd6NvH4xy7hkoA%2BGXpywqMSLJiqRSbAb1%2BBCnFK4Bozy0XSAZOXy%2BmK%2F1EGWzMI8rQPnj2eO6o%2F%2FhAMTM%2FOJEp4BaAjA6dgZBOJHebhXti%2BTAAG%2FyW%2BBPsQhuUd4I9JTAYdGEZtDp4hPVdJ%2BmLZt%2FsR2n%2Fe8KKv0XDnX72Uuio6CdSYz0u0qrKY2iRUxguhdglnrx7AHPRq4i4Q2h15dwgZYimKsgc4N3wIrthpzHceuWEtscElBC3716jxOYageAYptbPkcmk35%2Fyb79CFPl8T%2BksZrppUjkhuXJ%2BdxDSUBNH%2BUQmE1EKJkakYIJkNTPyN%2FakOMOPx%2BrwGOqUBXee5BsJEfrGbuo8ciUBhhAYx1YEvg2Mg86P61tDztBjD2fxXKfX%2F1P2nIlZ0iZJAzNMv2LlskuEYKOAw4fx1RKZ1kSuflqjru6nqeNHoNi3k5Yj7hPP8MNxBlyVtDKfbv2NjXEpq9FAHDXr%2FNRfkgIjihfqZO9a2qwQUAGOtczxyBKVaUEDTN9wiAtUUC3G9S1uMsRwoVHusqrBXE3ZXqPlhfF0j&X-Amz-Signature=d7de72d3ac0f7b1b415d6515733b40c209b88a2021b4ef182f4c79b0ab1e2ac5&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2T5RNA5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZhFxmthAk%2BGY5qHl1EKn3Gj3X4OZJzkW4CKirFqMI6QIhAJZhVJhcgwKLk300Lj2rsXkOQwbr9j8dCi2sLlxXUwpSKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYHm26XLGrPvMU8VYq3ANhV0PZln%2F3nslfILOjDBY6nezBWOkOcmRW1sfaqn0irjXC5rPt0ab6XRFE4bN9tQx7LzsUQ%2FWbjBdqONCpDOXgr6lgyxrYoawU4iVWdvj%2BHAjLYpAQh%2BWbJ%2BewxFYm3Vf4fMMlsALOW2BWy1QBc1Tl68T%2FOesj5S2NoiHbrqXKsiRvd30irebPiaIywVcMtwwgNIxU8Q%2Fmk6Sn5zMOfaf0ZMnDPHrG8zdV3eeyOaQkjXjlUUNJPAl1CrN%2Bd%2FGhd9KQ95fiB5sZnr2oyvZOXjjAOgePxrSVwLAIA0GdNTP4zo1xey4OLSYc2cvxxZ7DyODWsQve3EcQLBsfOSP%2BE2vIFeSUwxUq54hGka8qNEsi088TjxysJA04q1XCjhV%2BfbTdhmRngQ3wsUi%2F2qs2W9USf3OJod2XCvrkhOutBYWhgDHJePwhrkwAASO0zFhSDMbVK1aTAodio%2BIsfBBS7iJ1DawQ8EOde0LYPF8Xy6fYb3oA%2F7qWmsLxPxK3iPwYV7Ls0e14zQ2a4sUyyP5KDbdpbLxIDDYsoavOuRWsQJoCLX8e5Xb4%2FSq3wX5xauRzSBS37gWTmPfexFSGZ7HMg%2FSKgAUErnAOXuSPNKNjTdNrNoupHk0fHumjAyzLDDDF8fq8BjqkAVXPgUGO9K6m4LnsTmhKlDdbfqk9LrnRhfV40%2BbmvuhAbicxtQTwLLDrZh3ZwQOHRZbqIlfSBbbIhR0oLVPhomWvzVqz63b1lVlXnb8Cf%2BsKtjvLePYH7RsqbW7NmMclrToTkjeEaTap8HePLgnyAlpejcq%2BZKLdqwSCvYeqJXVXOxrQvdW%2B51D2X%2F4XEWqlVwKbm9K5PLHDbvlwInot8SjPOXig&X-Amz-Signature=75d9c0f0b5e297c9af483f3bee1d3f14d4de57e1a7939ca2a7be8feb6675ea28&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2T5RNA5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZhFxmthAk%2BGY5qHl1EKn3Gj3X4OZJzkW4CKirFqMI6QIhAJZhVJhcgwKLk300Lj2rsXkOQwbr9j8dCi2sLlxXUwpSKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYHm26XLGrPvMU8VYq3ANhV0PZln%2F3nslfILOjDBY6nezBWOkOcmRW1sfaqn0irjXC5rPt0ab6XRFE4bN9tQx7LzsUQ%2FWbjBdqONCpDOXgr6lgyxrYoawU4iVWdvj%2BHAjLYpAQh%2BWbJ%2BewxFYm3Vf4fMMlsALOW2BWy1QBc1Tl68T%2FOesj5S2NoiHbrqXKsiRvd30irebPiaIywVcMtwwgNIxU8Q%2Fmk6Sn5zMOfaf0ZMnDPHrG8zdV3eeyOaQkjXjlUUNJPAl1CrN%2Bd%2FGhd9KQ95fiB5sZnr2oyvZOXjjAOgePxrSVwLAIA0GdNTP4zo1xey4OLSYc2cvxxZ7DyODWsQve3EcQLBsfOSP%2BE2vIFeSUwxUq54hGka8qNEsi088TjxysJA04q1XCjhV%2BfbTdhmRngQ3wsUi%2F2qs2W9USf3OJod2XCvrkhOutBYWhgDHJePwhrkwAASO0zFhSDMbVK1aTAodio%2BIsfBBS7iJ1DawQ8EOde0LYPF8Xy6fYb3oA%2F7qWmsLxPxK3iPwYV7Ls0e14zQ2a4sUyyP5KDbdpbLxIDDYsoavOuRWsQJoCLX8e5Xb4%2FSq3wX5xauRzSBS37gWTmPfexFSGZ7HMg%2FSKgAUErnAOXuSPNKNjTdNrNoupHk0fHumjAyzLDDDF8fq8BjqkAVXPgUGO9K6m4LnsTmhKlDdbfqk9LrnRhfV40%2BbmvuhAbicxtQTwLLDrZh3ZwQOHRZbqIlfSBbbIhR0oLVPhomWvzVqz63b1lVlXnb8Cf%2BsKtjvLePYH7RsqbW7NmMclrToTkjeEaTap8HePLgnyAlpejcq%2BZKLdqwSCvYeqJXVXOxrQvdW%2B51D2X%2F4XEWqlVwKbm9K5PLHDbvlwInot8SjPOXig&X-Amz-Signature=a7f7b62f8226c67285532d5010fe8593b0ed5d51e6fc21faa8bee959264ac880&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HQKZS6B%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7Q3H6L9nBM5H%2FZfjoan%2FPikV1FChd%2FjI4ZujQ2eR3HAIgX86oedjnPUCK%2BcBRuNlqteNY5%2FWHpYUnysdRW3R1DgEqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOZkvA4k8cHARz57yrcA%2B5kz1jkMI70mYSSI9cC0LLMUeY5XWA9cgtFeSxA2%2BtDFagYPsezuy2shG4go2xh%2FFLKk%2Ft0ryEJRAiL7pqsyG%2Fh8IF%2FDMN9tjxS%2BU18Ve4z2H7MmpCg4gyycRCqG4Y%2BkdSiTgkw0lRAQncrp9HE51klAt%2FBZkkbsa07Bdbzd9t26v3VEYmqnGReniqAc7H8EPn3NIyLrIVrLES5w3lVQVBX8tUz0lK2mqCDIYsyuTl9x8KNzEMbJNU2BsTFP2cGBwC2OcXC8Z6G%2Fo2OBNH0GvuaqU6tybp7Tm5P%2BQu17vkFjuNkrbpj%2Fxd6NvH4xy7hkoA%2BGXpywqMSLJiqRSbAb1%2BBCnFK4Bozy0XSAZOXy%2BmK%2F1EGWzMI8rQPnj2eO6o%2F%2FhAMTM%2FOJEp4BaAjA6dgZBOJHebhXti%2BTAAG%2FyW%2BBPsQhuUd4I9JTAYdGEZtDp4hPVdJ%2BmLZt%2FsR2n%2Fe8KKv0XDnX72Uuio6CdSYz0u0qrKY2iRUxguhdglnrx7AHPRq4i4Q2h15dwgZYimKsgc4N3wIrthpzHceuWEtscElBC3716jxOYageAYptbPkcmk35%2Fyb79CFPl8T%2BksZrppUjkhuXJ%2BdxDSUBNH%2BUQmE1EKJkakYIJkNTPyN%2FakOMOPx%2BrwGOqUBXee5BsJEfrGbuo8ciUBhhAYx1YEvg2Mg86P61tDztBjD2fxXKfX%2F1P2nIlZ0iZJAzNMv2LlskuEYKOAw4fx1RKZ1kSuflqjru6nqeNHoNi3k5Yj7hPP8MNxBlyVtDKfbv2NjXEpq9FAHDXr%2FNRfkgIjihfqZO9a2qwQUAGOtczxyBKVaUEDTN9wiAtUUC3G9S1uMsRwoVHusqrBXE3ZXqPlhfF0j&X-Amz-Signature=d28a8619dc7d7b2385b0c4c2f5e46c3805a1cdbba7a2d8058fd35cb646c5f3f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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