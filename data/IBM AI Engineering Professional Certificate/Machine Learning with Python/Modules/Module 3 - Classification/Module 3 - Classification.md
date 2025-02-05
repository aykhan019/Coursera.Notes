

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJKZNVTR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIE38HSxUY5%2B%2BkGjXNUoCQaZSv%2BToaxQ4enzUF4bcmnjcAiEA1KhSvY51koTYf0B%2BXpum%2FCFVSVpzyPVL8zymQCPbmzQq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCP%2BEt13lftlJzaVNCrcA73ZS%2FfZsA8qGajO3vRId7CuOQw%2F1qncPQHhAKhVHC5zfDsFXGwRE0vulWDNLhMzJQ7IycrhfZbE8nl2IBLIQIK0ML2L5NSLPV9a28Cpvr2Mtz91GzsVV97LDgKYU3ZcK4KLyql3twrpmZyokk5JE%2BZ%2FD6TYad9WslXJ%2F1tnabIP8GyR8M9UMKL1UpRM1EJ7hNslGVbb%2FMI82lcB2S23szLajXGUojve0z%2F%2FicQZIr0vZGCNr7O8WlTtDhfAw7yymWBanYyfUyma34MhnxpHLEaumKPK%2B%2B%2FZfpVtwUuHy6HqZb1ypPSFWiBnvwwSzh4fYA29fsCPvpzK6RFgXhwSJYvm83BHoNlvx04vHqdJ%2Bd3el2dTtOdYXAW6BcWYyZ8REMMRKepyL61xFA9IpBGNyjF2wtOf0JMwlV%2FtOJlRep51FOl6dB%2Fx%2BjghnFrtypQtBknEuXKC4vyhTDJ76oxURT5Nxk9tR5bEUZN%2BHAx3TFWzcGYNuoYnqdxTWffA8WbAO89uqHDR8VR4QMdJQyqAPG1QTnedEtuFDX9VECxoSZrBmWnwpahStKRTTFeLQGjSgK5AheIelFR4Q6vbTi4DBFwyVTFvGKKzMn8n9il6Kbq8f5PnyV512po72kFWMKTNir0GOqUBtYU3ubOvRpTN7bz%2F18jngIIAxlOSwApjT8IGgdt5VYmWb%2BBJ76nOlNAODN0Ejr%2BWSzGPbd0y8bt7PNTEp7PeBXSr8ajZaL%2B5vnaLUlBorlZb6WcrOfLIvkoMO2omF8mX2GJCglZUzJWBbipaXX8VSBE7u1MrSfyU8zjKEtxZAEgKOcvdpjh2Zv1qzjs6VkdbY0hNyn%2F1FXRpnRrxYooTdapMcxyZ&X-Amz-Signature=9af305ccc18a6ea5947b8a101270c6370b85d51a3f959b9f8c4d74b28fc31fc3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJKZNVTR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIE38HSxUY5%2B%2BkGjXNUoCQaZSv%2BToaxQ4enzUF4bcmnjcAiEA1KhSvY51koTYf0B%2BXpum%2FCFVSVpzyPVL8zymQCPbmzQq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCP%2BEt13lftlJzaVNCrcA73ZS%2FfZsA8qGajO3vRId7CuOQw%2F1qncPQHhAKhVHC5zfDsFXGwRE0vulWDNLhMzJQ7IycrhfZbE8nl2IBLIQIK0ML2L5NSLPV9a28Cpvr2Mtz91GzsVV97LDgKYU3ZcK4KLyql3twrpmZyokk5JE%2BZ%2FD6TYad9WslXJ%2F1tnabIP8GyR8M9UMKL1UpRM1EJ7hNslGVbb%2FMI82lcB2S23szLajXGUojve0z%2F%2FicQZIr0vZGCNr7O8WlTtDhfAw7yymWBanYyfUyma34MhnxpHLEaumKPK%2B%2B%2FZfpVtwUuHy6HqZb1ypPSFWiBnvwwSzh4fYA29fsCPvpzK6RFgXhwSJYvm83BHoNlvx04vHqdJ%2Bd3el2dTtOdYXAW6BcWYyZ8REMMRKepyL61xFA9IpBGNyjF2wtOf0JMwlV%2FtOJlRep51FOl6dB%2Fx%2BjghnFrtypQtBknEuXKC4vyhTDJ76oxURT5Nxk9tR5bEUZN%2BHAx3TFWzcGYNuoYnqdxTWffA8WbAO89uqHDR8VR4QMdJQyqAPG1QTnedEtuFDX9VECxoSZrBmWnwpahStKRTTFeLQGjSgK5AheIelFR4Q6vbTi4DBFwyVTFvGKKzMn8n9il6Kbq8f5PnyV512po72kFWMKTNir0GOqUBtYU3ubOvRpTN7bz%2F18jngIIAxlOSwApjT8IGgdt5VYmWb%2BBJ76nOlNAODN0Ejr%2BWSzGPbd0y8bt7PNTEp7PeBXSr8ajZaL%2B5vnaLUlBorlZb6WcrOfLIvkoMO2omF8mX2GJCglZUzJWBbipaXX8VSBE7u1MrSfyU8zjKEtxZAEgKOcvdpjh2Zv1qzjs6VkdbY0hNyn%2F1FXRpnRrxYooTdapMcxyZ&X-Amz-Signature=3ed79a51135baf39a491d39f91749394e3281410cb08bb7f1555adcc780fc8b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJKZNVTR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIE38HSxUY5%2B%2BkGjXNUoCQaZSv%2BToaxQ4enzUF4bcmnjcAiEA1KhSvY51koTYf0B%2BXpum%2FCFVSVpzyPVL8zymQCPbmzQq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCP%2BEt13lftlJzaVNCrcA73ZS%2FfZsA8qGajO3vRId7CuOQw%2F1qncPQHhAKhVHC5zfDsFXGwRE0vulWDNLhMzJQ7IycrhfZbE8nl2IBLIQIK0ML2L5NSLPV9a28Cpvr2Mtz91GzsVV97LDgKYU3ZcK4KLyql3twrpmZyokk5JE%2BZ%2FD6TYad9WslXJ%2F1tnabIP8GyR8M9UMKL1UpRM1EJ7hNslGVbb%2FMI82lcB2S23szLajXGUojve0z%2F%2FicQZIr0vZGCNr7O8WlTtDhfAw7yymWBanYyfUyma34MhnxpHLEaumKPK%2B%2B%2FZfpVtwUuHy6HqZb1ypPSFWiBnvwwSzh4fYA29fsCPvpzK6RFgXhwSJYvm83BHoNlvx04vHqdJ%2Bd3el2dTtOdYXAW6BcWYyZ8REMMRKepyL61xFA9IpBGNyjF2wtOf0JMwlV%2FtOJlRep51FOl6dB%2Fx%2BjghnFrtypQtBknEuXKC4vyhTDJ76oxURT5Nxk9tR5bEUZN%2BHAx3TFWzcGYNuoYnqdxTWffA8WbAO89uqHDR8VR4QMdJQyqAPG1QTnedEtuFDX9VECxoSZrBmWnwpahStKRTTFeLQGjSgK5AheIelFR4Q6vbTi4DBFwyVTFvGKKzMn8n9il6Kbq8f5PnyV512po72kFWMKTNir0GOqUBtYU3ubOvRpTN7bz%2F18jngIIAxlOSwApjT8IGgdt5VYmWb%2BBJ76nOlNAODN0Ejr%2BWSzGPbd0y8bt7PNTEp7PeBXSr8ajZaL%2B5vnaLUlBorlZb6WcrOfLIvkoMO2omF8mX2GJCglZUzJWBbipaXX8VSBE7u1MrSfyU8zjKEtxZAEgKOcvdpjh2Zv1qzjs6VkdbY0hNyn%2F1FXRpnRrxYooTdapMcxyZ&X-Amz-Signature=80a09b0451464e6dce2f087211fbabb4abefdc70c305c9c29590da2e845a882a&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YCI4IXG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDWXCZ2uGGtDT7ZlBwgAEoEKBsLOufwOLGPytFeOWF%2B8gIhAKG1Tm5%2F3%2FUH5hGBddWQhy7sbvFhDls9SPT7K7uBfqjbKv8DCDkQABoMNjM3NDIzMTgzODA1Igx94yEkMYOxO5wWUbYq3ANFq%2BAZmkHELzN0RY%2Fa1sIqgYiP1mTN4Eh%2BBZZbrnCV3A8IKN6Fs69xEqS9mNIB67U2kinn0TCy45JJRmefD8N1OHdMPVve%2BrIvYFut%2BA8wrG%2FLU7IQUmTdS8RNP9Md6g%2FAhN9e%2FSlOxtiX06Lf3cILBOgG3CW2HTmV2xKBwacOoGGR2k52UtMxuN%2FJQCgWJhMLDErMztNlbju5aZJJI0TeDV2pBTFgl2CuQGXS6DmIs4nC6lsTO3Hne6Dxms2Lxu%2Byacwl3Drb6hB5vambNRA7rN1D%2BnUDFkFkVtNRFSAC4ZwEuD6bigTWS4zdkaiyTNKDG%2B3OzRDBdEf2LJSDjFmUbraXEHFmlFgKoQrN1Y3deO3VgCNEfhz0AlneGz3hZeNE2rAh9bXlVVDgltYJaiBqLtlRy0ukvtI123%2FL0DijAkj9iEoup6r%2FVlDGGp1CkUH%2FRJYIisjL08U6QB%2BzZVI3Wduqimw7raSj%2F%2B3Ii3ilrCIEHlZgVmseJV0MObP7eryArvVRJLMWcK9F48iixIHsQl4S0zSWsO628rK6yUXZ%2BKK%2F2vcpsVjWwXQJCXummLpcCD38e8SsPcKL9OoOy7pSFawsTSJY%2Fi1i9MZKrhfjkgP8ea30Q7i2I50sWTDTzYq9BjqkAfPha4j0YbAjNWIqWE3MQ7eNV05dgrDQMbdSqXfQHs7dKboKN%2BUQTeFNdt9hs8e42iS2VRfE%2BCRsChMEP9Np%2BPrKwjK7Vmp4woUzN113nQgpXS8R64rMtOelnhWHCrEXiDrrHS%2BZ%2B4ADTZWsyIkVAfRbgBiUh7JYmGQjIAoYjgzuv9zlaOkj1COI6dCJTKNLzRBq13w11IFcIPYKStmzpIbDt8Gd&X-Amz-Signature=16db80e6461e821d66f556208820bc2105c36bc73a3df425abdb80d81bbc14ea&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YCI4IXG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDWXCZ2uGGtDT7ZlBwgAEoEKBsLOufwOLGPytFeOWF%2B8gIhAKG1Tm5%2F3%2FUH5hGBddWQhy7sbvFhDls9SPT7K7uBfqjbKv8DCDkQABoMNjM3NDIzMTgzODA1Igx94yEkMYOxO5wWUbYq3ANFq%2BAZmkHELzN0RY%2Fa1sIqgYiP1mTN4Eh%2BBZZbrnCV3A8IKN6Fs69xEqS9mNIB67U2kinn0TCy45JJRmefD8N1OHdMPVve%2BrIvYFut%2BA8wrG%2FLU7IQUmTdS8RNP9Md6g%2FAhN9e%2FSlOxtiX06Lf3cILBOgG3CW2HTmV2xKBwacOoGGR2k52UtMxuN%2FJQCgWJhMLDErMztNlbju5aZJJI0TeDV2pBTFgl2CuQGXS6DmIs4nC6lsTO3Hne6Dxms2Lxu%2Byacwl3Drb6hB5vambNRA7rN1D%2BnUDFkFkVtNRFSAC4ZwEuD6bigTWS4zdkaiyTNKDG%2B3OzRDBdEf2LJSDjFmUbraXEHFmlFgKoQrN1Y3deO3VgCNEfhz0AlneGz3hZeNE2rAh9bXlVVDgltYJaiBqLtlRy0ukvtI123%2FL0DijAkj9iEoup6r%2FVlDGGp1CkUH%2FRJYIisjL08U6QB%2BzZVI3Wduqimw7raSj%2F%2B3Ii3ilrCIEHlZgVmseJV0MObP7eryArvVRJLMWcK9F48iixIHsQl4S0zSWsO628rK6yUXZ%2BKK%2F2vcpsVjWwXQJCXummLpcCD38e8SsPcKL9OoOy7pSFawsTSJY%2Fi1i9MZKrhfjkgP8ea30Q7i2I50sWTDTzYq9BjqkAfPha4j0YbAjNWIqWE3MQ7eNV05dgrDQMbdSqXfQHs7dKboKN%2BUQTeFNdt9hs8e42iS2VRfE%2BCRsChMEP9Np%2BPrKwjK7Vmp4woUzN113nQgpXS8R64rMtOelnhWHCrEXiDrrHS%2BZ%2B4ADTZWsyIkVAfRbgBiUh7JYmGQjIAoYjgzuv9zlaOkj1COI6dCJTKNLzRBq13w11IFcIPYKStmzpIbDt8Gd&X-Amz-Signature=abd39c22686a9e5932f0a7d274f75cbd5d771303113cfb48ad44fbe2e2664241&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJKZNVTR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIE38HSxUY5%2B%2BkGjXNUoCQaZSv%2BToaxQ4enzUF4bcmnjcAiEA1KhSvY51koTYf0B%2BXpum%2FCFVSVpzyPVL8zymQCPbmzQq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCP%2BEt13lftlJzaVNCrcA73ZS%2FfZsA8qGajO3vRId7CuOQw%2F1qncPQHhAKhVHC5zfDsFXGwRE0vulWDNLhMzJQ7IycrhfZbE8nl2IBLIQIK0ML2L5NSLPV9a28Cpvr2Mtz91GzsVV97LDgKYU3ZcK4KLyql3twrpmZyokk5JE%2BZ%2FD6TYad9WslXJ%2F1tnabIP8GyR8M9UMKL1UpRM1EJ7hNslGVbb%2FMI82lcB2S23szLajXGUojve0z%2F%2FicQZIr0vZGCNr7O8WlTtDhfAw7yymWBanYyfUyma34MhnxpHLEaumKPK%2B%2B%2FZfpVtwUuHy6HqZb1ypPSFWiBnvwwSzh4fYA29fsCPvpzK6RFgXhwSJYvm83BHoNlvx04vHqdJ%2Bd3el2dTtOdYXAW6BcWYyZ8REMMRKepyL61xFA9IpBGNyjF2wtOf0JMwlV%2FtOJlRep51FOl6dB%2Fx%2BjghnFrtypQtBknEuXKC4vyhTDJ76oxURT5Nxk9tR5bEUZN%2BHAx3TFWzcGYNuoYnqdxTWffA8WbAO89uqHDR8VR4QMdJQyqAPG1QTnedEtuFDX9VECxoSZrBmWnwpahStKRTTFeLQGjSgK5AheIelFR4Q6vbTi4DBFwyVTFvGKKzMn8n9il6Kbq8f5PnyV512po72kFWMKTNir0GOqUBtYU3ubOvRpTN7bz%2F18jngIIAxlOSwApjT8IGgdt5VYmWb%2BBJ76nOlNAODN0Ejr%2BWSzGPbd0y8bt7PNTEp7PeBXSr8ajZaL%2B5vnaLUlBorlZb6WcrOfLIvkoMO2omF8mX2GJCglZUzJWBbipaXX8VSBE7u1MrSfyU8zjKEtxZAEgKOcvdpjh2Zv1qzjs6VkdbY0hNyn%2F1FXRpnRrxYooTdapMcxyZ&X-Amz-Signature=f065467e17757a08ae330042e9021433723fa32dfb9b17216477f00fe49db6f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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