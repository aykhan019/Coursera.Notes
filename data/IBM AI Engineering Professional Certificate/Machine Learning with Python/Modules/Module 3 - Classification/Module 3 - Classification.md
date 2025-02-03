

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DFWQOOW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQDH5nqeDe1qbXoWANKarbHW7jnWuo9RyaiXZij6Hq8ulgIgUk9dziuRpcTEPYSBYrZx1iHOYludeB7xF%2BZ4Y%2Fzkxqwq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDLfaNeExSUPR5fi4ZCrcA5Tc1l%2BhU%2FbY49sKWESlEJ5d0LVOZaCgQ4Lu6AeMvTJzuwF4iCQ2eDoxLiKAWMH%2BUp9vDNJBNGAH%2FlGobB7c8veRq6uaVU%2Bcw3mXX9HofI2SwHVJd5DKsggEFQsnEvsSapBhiLterXZ6iOvhKahIe1UAnuBeV74qH0DN9%2F6KdX%2FgdT4zOxcxyYlwnjWrJq9yImIJ1Dhburbbf3mZdx1wI1TwMfBkXRgEtRV7jEQYJb3jfr54TU785mGoYUFMIPR7PkLAAQtpGrYHkPlbuY3wJNmk%2FyZLjZCsS%2BRfs%2BoGoLbkFiMrstcLzGGkkfqe2Emw3A%2BMtw5BEM%2BkAI69%2FNYe0FcKWdiHagOlH%2BG8%2Fs2%2B6GAH8qvQX3lr2H8RNhtHCDRNQUaNu%2Ff9urVEviNmU3UcTlQFuJ5FCgvAQ4va%2FjzAbwcmBdjwfqwm%2Fl75uMkF0OdpW%2BVmv4Z%2BFfWQFIjQCpYcxP9GqSJXc9GXMeHcPLJYpbiujQ2LAS5DMRgN1VCwYVo3CWSfk83ZgVT7haz4DBVdpcScs5r%2FIQbFj%2B8LDJTlaDsnH%2BKKqMFtBsCL%2BZWcNrN1V%2FanHZ1mmVrCgxcWvvgaghZ8vgUyP2E4Rco849zLNJ5dlSFhyIkd9gaLLKI8MP7lg70GOqUB75xQccRDpCglHL7JcTNfQqHklP6UDdGB92u%2BkAbVprY4xeThqMUf0A4jQF173jhvgywIBu8IlGEribv59J9C12NSIZacvaSQ1he5srGRVojvLAFhefCWNjewEk8kb56%2BGHJqroXsqPu%2BzAcYo4yMVWFfGmi3EBufmLodMFlGN26i88Qr2tTvfftstM51zx4YQQWNm7jXSpsBR22UmlobIsV7eXOh&X-Amz-Signature=9cab37498217320614ab0e9c021404cce0379d1e6c723f9a418b9ebf53499084&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DFWQOOW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQDH5nqeDe1qbXoWANKarbHW7jnWuo9RyaiXZij6Hq8ulgIgUk9dziuRpcTEPYSBYrZx1iHOYludeB7xF%2BZ4Y%2Fzkxqwq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDLfaNeExSUPR5fi4ZCrcA5Tc1l%2BhU%2FbY49sKWESlEJ5d0LVOZaCgQ4Lu6AeMvTJzuwF4iCQ2eDoxLiKAWMH%2BUp9vDNJBNGAH%2FlGobB7c8veRq6uaVU%2Bcw3mXX9HofI2SwHVJd5DKsggEFQsnEvsSapBhiLterXZ6iOvhKahIe1UAnuBeV74qH0DN9%2F6KdX%2FgdT4zOxcxyYlwnjWrJq9yImIJ1Dhburbbf3mZdx1wI1TwMfBkXRgEtRV7jEQYJb3jfr54TU785mGoYUFMIPR7PkLAAQtpGrYHkPlbuY3wJNmk%2FyZLjZCsS%2BRfs%2BoGoLbkFiMrstcLzGGkkfqe2Emw3A%2BMtw5BEM%2BkAI69%2FNYe0FcKWdiHagOlH%2BG8%2Fs2%2B6GAH8qvQX3lr2H8RNhtHCDRNQUaNu%2Ff9urVEviNmU3UcTlQFuJ5FCgvAQ4va%2FjzAbwcmBdjwfqwm%2Fl75uMkF0OdpW%2BVmv4Z%2BFfWQFIjQCpYcxP9GqSJXc9GXMeHcPLJYpbiujQ2LAS5DMRgN1VCwYVo3CWSfk83ZgVT7haz4DBVdpcScs5r%2FIQbFj%2B8LDJTlaDsnH%2BKKqMFtBsCL%2BZWcNrN1V%2FanHZ1mmVrCgxcWvvgaghZ8vgUyP2E4Rco849zLNJ5dlSFhyIkd9gaLLKI8MP7lg70GOqUB75xQccRDpCglHL7JcTNfQqHklP6UDdGB92u%2BkAbVprY4xeThqMUf0A4jQF173jhvgywIBu8IlGEribv59J9C12NSIZacvaSQ1he5srGRVojvLAFhefCWNjewEk8kb56%2BGHJqroXsqPu%2BzAcYo4yMVWFfGmi3EBufmLodMFlGN26i88Qr2tTvfftstM51zx4YQQWNm7jXSpsBR22UmlobIsV7eXOh&X-Amz-Signature=8c44a332a2fa9b760fb317aa55818ed500437bd1776a52a307da784bf98d1eb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DFWQOOW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQDH5nqeDe1qbXoWANKarbHW7jnWuo9RyaiXZij6Hq8ulgIgUk9dziuRpcTEPYSBYrZx1iHOYludeB7xF%2BZ4Y%2Fzkxqwq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDLfaNeExSUPR5fi4ZCrcA5Tc1l%2BhU%2FbY49sKWESlEJ5d0LVOZaCgQ4Lu6AeMvTJzuwF4iCQ2eDoxLiKAWMH%2BUp9vDNJBNGAH%2FlGobB7c8veRq6uaVU%2Bcw3mXX9HofI2SwHVJd5DKsggEFQsnEvsSapBhiLterXZ6iOvhKahIe1UAnuBeV74qH0DN9%2F6KdX%2FgdT4zOxcxyYlwnjWrJq9yImIJ1Dhburbbf3mZdx1wI1TwMfBkXRgEtRV7jEQYJb3jfr54TU785mGoYUFMIPR7PkLAAQtpGrYHkPlbuY3wJNmk%2FyZLjZCsS%2BRfs%2BoGoLbkFiMrstcLzGGkkfqe2Emw3A%2BMtw5BEM%2BkAI69%2FNYe0FcKWdiHagOlH%2BG8%2Fs2%2B6GAH8qvQX3lr2H8RNhtHCDRNQUaNu%2Ff9urVEviNmU3UcTlQFuJ5FCgvAQ4va%2FjzAbwcmBdjwfqwm%2Fl75uMkF0OdpW%2BVmv4Z%2BFfWQFIjQCpYcxP9GqSJXc9GXMeHcPLJYpbiujQ2LAS5DMRgN1VCwYVo3CWSfk83ZgVT7haz4DBVdpcScs5r%2FIQbFj%2B8LDJTlaDsnH%2BKKqMFtBsCL%2BZWcNrN1V%2FanHZ1mmVrCgxcWvvgaghZ8vgUyP2E4Rco849zLNJ5dlSFhyIkd9gaLLKI8MP7lg70GOqUB75xQccRDpCglHL7JcTNfQqHklP6UDdGB92u%2BkAbVprY4xeThqMUf0A4jQF173jhvgywIBu8IlGEribv59J9C12NSIZacvaSQ1he5srGRVojvLAFhefCWNjewEk8kb56%2BGHJqroXsqPu%2BzAcYo4yMVWFfGmi3EBufmLodMFlGN26i88Qr2tTvfftstM51zx4YQQWNm7jXSpsBR22UmlobIsV7eXOh&X-Amz-Signature=4398f6a2ff8e9ba77c9f5d1585cfb2a3fab42aa74324f1558791404c54bba68f&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMBQDWZX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQDNr9mgckHG7UKfbzPeJ%2BrGKinRKWQY0aowxA8qA04VAQIgY3etSR5vd%2BW5YGpyPAvNEcnfTKygV6iqMooWml7F%2FgEq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDGxGSU9RK5I%2B5kEaWircA5bVT6fvCg8bjJjnIPIcxIa7ExcMfunCN8S1WhE%2FxI4AfVcqUM9005IqH0n%2B1Yl1WLnr1og%2B2Ab%2Fiv15R8z5vo0AQgm5VQW5bzp8W7QlAXUSMssxrVd7eL58pK4TvG6aVDB3lBJx38EjGyr9QSIQeanHVaBoyCGHnLGL1z%2FiuamJr1DKsQbdmMN6XCTPJHQ3pobTeErHaebWSgOWzctN4xdhkNTJPxycTkQHV139GUknVgjbezsnyFjefnCE2efQid9Y8VXy%2BkUENUQABSiU1lE8YKuQQbCJhMC5pOktjcQ45xjdWx8GnD1BEJkvTIRCt9GHiDiGlOwge4nkED9jXO%2BL5Z2RkTiKjwJsKpp8YmNuLH7KAxE3kRSIfQrf%2B%2FeudJrw5YFpy1C3Mvp%2FdaChNzr7KOPbODb8CtsENfyQcbJB8EkKJqv48LAu2hwS2wX4YPB4DCToeR0xDY3kiWO4IR9JVZIUesJ9vJd%2FNRPwHsCUbmZJfNJbJ%2F1YvtgNIAczh15osHTEHjx9X15OVDrnWFG%2BpO35gUA8wZUmPtBIFTnFvXDDprqYK13NwKm50%2FMi9VsaELRUQjY8qmpsGi241hXhK3UYNTvK%2BU1T1CXqhggKoQt60TE3kNmo2cRwMIPmg70GOqUB9XTLu2YYSrTjtPngwYS5NlJSnB7uXs4%2BSnUxVB7cSWZhZvdvy1tSc7i52brz%2B%2B6xMzOdEDPEwLkdg61VY2ujmapgWran1Y1iCnp1IRBGfx1Tr9cmxZzx0S%2Fp%2BMEPGXWG%2B3OxRV6jeTtVLZENYeibJR012nnjMdKJJyKHnR%2FHgG5VumhuiJOjA2%2BmphiG4v3n%2B%2FJFzUIOtAMx%2BloyvNrTGw1rqMFs&X-Amz-Signature=751cb9376c3c78b4ed2d05f54bb53c501eed542f8a52089e7f7155f6dc1db68b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMBQDWZX%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQDNr9mgckHG7UKfbzPeJ%2BrGKinRKWQY0aowxA8qA04VAQIgY3etSR5vd%2BW5YGpyPAvNEcnfTKygV6iqMooWml7F%2FgEq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDGxGSU9RK5I%2B5kEaWircA5bVT6fvCg8bjJjnIPIcxIa7ExcMfunCN8S1WhE%2FxI4AfVcqUM9005IqH0n%2B1Yl1WLnr1og%2B2Ab%2Fiv15R8z5vo0AQgm5VQW5bzp8W7QlAXUSMssxrVd7eL58pK4TvG6aVDB3lBJx38EjGyr9QSIQeanHVaBoyCGHnLGL1z%2FiuamJr1DKsQbdmMN6XCTPJHQ3pobTeErHaebWSgOWzctN4xdhkNTJPxycTkQHV139GUknVgjbezsnyFjefnCE2efQid9Y8VXy%2BkUENUQABSiU1lE8YKuQQbCJhMC5pOktjcQ45xjdWx8GnD1BEJkvTIRCt9GHiDiGlOwge4nkED9jXO%2BL5Z2RkTiKjwJsKpp8YmNuLH7KAxE3kRSIfQrf%2B%2FeudJrw5YFpy1C3Mvp%2FdaChNzr7KOPbODb8CtsENfyQcbJB8EkKJqv48LAu2hwS2wX4YPB4DCToeR0xDY3kiWO4IR9JVZIUesJ9vJd%2FNRPwHsCUbmZJfNJbJ%2F1YvtgNIAczh15osHTEHjx9X15OVDrnWFG%2BpO35gUA8wZUmPtBIFTnFvXDDprqYK13NwKm50%2FMi9VsaELRUQjY8qmpsGi241hXhK3UYNTvK%2BU1T1CXqhggKoQt60TE3kNmo2cRwMIPmg70GOqUB9XTLu2YYSrTjtPngwYS5NlJSnB7uXs4%2BSnUxVB7cSWZhZvdvy1tSc7i52brz%2B%2B6xMzOdEDPEwLkdg61VY2ujmapgWran1Y1iCnp1IRBGfx1Tr9cmxZzx0S%2Fp%2BMEPGXWG%2B3OxRV6jeTtVLZENYeibJR012nnjMdKJJyKHnR%2FHgG5VumhuiJOjA2%2BmphiG4v3n%2B%2FJFzUIOtAMx%2BloyvNrTGw1rqMFs&X-Amz-Signature=52c45414bdbb0bb29463dbd8f9b29e09aaaaf0772fab16f11d3b417b517779d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DFWQOOW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQDH5nqeDe1qbXoWANKarbHW7jnWuo9RyaiXZij6Hq8ulgIgUk9dziuRpcTEPYSBYrZx1iHOYludeB7xF%2BZ4Y%2Fzkxqwq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDLfaNeExSUPR5fi4ZCrcA5Tc1l%2BhU%2FbY49sKWESlEJ5d0LVOZaCgQ4Lu6AeMvTJzuwF4iCQ2eDoxLiKAWMH%2BUp9vDNJBNGAH%2FlGobB7c8veRq6uaVU%2Bcw3mXX9HofI2SwHVJd5DKsggEFQsnEvsSapBhiLterXZ6iOvhKahIe1UAnuBeV74qH0DN9%2F6KdX%2FgdT4zOxcxyYlwnjWrJq9yImIJ1Dhburbbf3mZdx1wI1TwMfBkXRgEtRV7jEQYJb3jfr54TU785mGoYUFMIPR7PkLAAQtpGrYHkPlbuY3wJNmk%2FyZLjZCsS%2BRfs%2BoGoLbkFiMrstcLzGGkkfqe2Emw3A%2BMtw5BEM%2BkAI69%2FNYe0FcKWdiHagOlH%2BG8%2Fs2%2B6GAH8qvQX3lr2H8RNhtHCDRNQUaNu%2Ff9urVEviNmU3UcTlQFuJ5FCgvAQ4va%2FjzAbwcmBdjwfqwm%2Fl75uMkF0OdpW%2BVmv4Z%2BFfWQFIjQCpYcxP9GqSJXc9GXMeHcPLJYpbiujQ2LAS5DMRgN1VCwYVo3CWSfk83ZgVT7haz4DBVdpcScs5r%2FIQbFj%2B8LDJTlaDsnH%2BKKqMFtBsCL%2BZWcNrN1V%2FanHZ1mmVrCgxcWvvgaghZ8vgUyP2E4Rco849zLNJ5dlSFhyIkd9gaLLKI8MP7lg70GOqUB75xQccRDpCglHL7JcTNfQqHklP6UDdGB92u%2BkAbVprY4xeThqMUf0A4jQF173jhvgywIBu8IlGEribv59J9C12NSIZacvaSQ1he5srGRVojvLAFhefCWNjewEk8kb56%2BGHJqroXsqPu%2BzAcYo4yMVWFfGmi3EBufmLodMFlGN26i88Qr2tTvfftstM51zx4YQQWNm7jXSpsBR22UmlobIsV7eXOh&X-Amz-Signature=5d4203da783e4f677fc73ccab93a7a33b02449950b527ba194461b50a45ba441&X-Amz-SignedHeaders=host&x-id=GetObject)
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