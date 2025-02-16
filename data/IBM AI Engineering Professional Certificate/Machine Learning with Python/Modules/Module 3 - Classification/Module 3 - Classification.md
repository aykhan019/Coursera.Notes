

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY7DRD2O%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCPTHjYFhuXIMyw7JmEHsQRLt584OxyHWtLaO%2FgcGX7uAIhAOk9lIXFxN12%2FeAjh5C084r7uusJGlVubx3NgROdUMr9Kv8DCFIQABoMNjM3NDIzMTgzODA1Igw1FXT8rixfMkvS5wQq3AMTkdB6CCCUpFFZN73o2FMjaKJro86aXNWh8WgHkJtRoZaVY4SyfJpMXtTfQ%2B9Y4ifh8l6mb%2BXTA%2B6sAWeliAqTADRVGYM7sH97MtrQsZc%2Bt95SIg%2Fecvwj5Uzta7bZMJoi375CkV991Z14SR7mDI2XJq2djnk%2F%2FspwoXhZXryiNzW53%2FEFluI9mfwRIZGsriDWqUkbJY2A2I%2B4vv0r5MOhas5z6vmPHhThH28IjiTai7fcLc49A8ZEYiy7vi7dH3LUn5MuDsBII%2FQ4KSa2QnxcA7WvyurU01COqdv2D8xO84x9j1txqgdCZOJn7%2FQatZBR1EFEAUktMcyE%2FDGyiZTxvlwOYm5qknVEGEWU%2Bbmyr1F8UJhUTr2dwhLFdBjs5YV37KW7iuJZ38dsVc42CefjwBC7NolAdnk9Xtlp97fHy713LqTXP1KaWaIIJaiZpkBAKa69J4cFQT6uv5Zw1Y0%2FqGGB%2FoFTsN0jlvZimAu%2FKonIiFRNc5FGuDSMh3kGnf2iWNUjZT2B5s7kwZRK7EvO74rFmzle7HJyLd%2F%2BexXCpRdrsi%2F%2Fcjz0WBU%2FgIxIdNlELbrZQ7MVGIv8u9TlKwX2m%2BKFBvjF2mHFYjzAg1xQNrbyhdU7OrmesvSyiTCk5cS9BjqkAbTvAQB98XCW5UOXaRcSASpKM2L0VN0YMGRLRq3YP%2BLjujKxCZgoVzUy387ONOOdDAVQek04R68bR4SKxAEXhGBIqh0jTt7rGjWdXULIHcYEsupJYFIZotuYTIS1974LbIYuuwRNHy1N7QeNLS0PMJ5kkMTVFP0Yu33cklxKAzdvQAxMdyw%2BOETeHN66mM5Ueu3sRQdw7XkSdZwJ%2B9ZsFBDjma%2BV&X-Amz-Signature=44a75df56fa77eed5253555e8370130d869484d53d68fe70bd888388c0c50c0f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY7DRD2O%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCPTHjYFhuXIMyw7JmEHsQRLt584OxyHWtLaO%2FgcGX7uAIhAOk9lIXFxN12%2FeAjh5C084r7uusJGlVubx3NgROdUMr9Kv8DCFIQABoMNjM3NDIzMTgzODA1Igw1FXT8rixfMkvS5wQq3AMTkdB6CCCUpFFZN73o2FMjaKJro86aXNWh8WgHkJtRoZaVY4SyfJpMXtTfQ%2B9Y4ifh8l6mb%2BXTA%2B6sAWeliAqTADRVGYM7sH97MtrQsZc%2Bt95SIg%2Fecvwj5Uzta7bZMJoi375CkV991Z14SR7mDI2XJq2djnk%2F%2FspwoXhZXryiNzW53%2FEFluI9mfwRIZGsriDWqUkbJY2A2I%2B4vv0r5MOhas5z6vmPHhThH28IjiTai7fcLc49A8ZEYiy7vi7dH3LUn5MuDsBII%2FQ4KSa2QnxcA7WvyurU01COqdv2D8xO84x9j1txqgdCZOJn7%2FQatZBR1EFEAUktMcyE%2FDGyiZTxvlwOYm5qknVEGEWU%2Bbmyr1F8UJhUTr2dwhLFdBjs5YV37KW7iuJZ38dsVc42CefjwBC7NolAdnk9Xtlp97fHy713LqTXP1KaWaIIJaiZpkBAKa69J4cFQT6uv5Zw1Y0%2FqGGB%2FoFTsN0jlvZimAu%2FKonIiFRNc5FGuDSMh3kGnf2iWNUjZT2B5s7kwZRK7EvO74rFmzle7HJyLd%2F%2BexXCpRdrsi%2F%2Fcjz0WBU%2FgIxIdNlELbrZQ7MVGIv8u9TlKwX2m%2BKFBvjF2mHFYjzAg1xQNrbyhdU7OrmesvSyiTCk5cS9BjqkAbTvAQB98XCW5UOXaRcSASpKM2L0VN0YMGRLRq3YP%2BLjujKxCZgoVzUy387ONOOdDAVQek04R68bR4SKxAEXhGBIqh0jTt7rGjWdXULIHcYEsupJYFIZotuYTIS1974LbIYuuwRNHy1N7QeNLS0PMJ5kkMTVFP0Yu33cklxKAzdvQAxMdyw%2BOETeHN66mM5Ueu3sRQdw7XkSdZwJ%2B9ZsFBDjma%2BV&X-Amz-Signature=ba6899847d0b81a64183040442fc071903130229a56d5116d40ab5f16a16a163&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY7DRD2O%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCPTHjYFhuXIMyw7JmEHsQRLt584OxyHWtLaO%2FgcGX7uAIhAOk9lIXFxN12%2FeAjh5C084r7uusJGlVubx3NgROdUMr9Kv8DCFIQABoMNjM3NDIzMTgzODA1Igw1FXT8rixfMkvS5wQq3AMTkdB6CCCUpFFZN73o2FMjaKJro86aXNWh8WgHkJtRoZaVY4SyfJpMXtTfQ%2B9Y4ifh8l6mb%2BXTA%2B6sAWeliAqTADRVGYM7sH97MtrQsZc%2Bt95SIg%2Fecvwj5Uzta7bZMJoi375CkV991Z14SR7mDI2XJq2djnk%2F%2FspwoXhZXryiNzW53%2FEFluI9mfwRIZGsriDWqUkbJY2A2I%2B4vv0r5MOhas5z6vmPHhThH28IjiTai7fcLc49A8ZEYiy7vi7dH3LUn5MuDsBII%2FQ4KSa2QnxcA7WvyurU01COqdv2D8xO84x9j1txqgdCZOJn7%2FQatZBR1EFEAUktMcyE%2FDGyiZTxvlwOYm5qknVEGEWU%2Bbmyr1F8UJhUTr2dwhLFdBjs5YV37KW7iuJZ38dsVc42CefjwBC7NolAdnk9Xtlp97fHy713LqTXP1KaWaIIJaiZpkBAKa69J4cFQT6uv5Zw1Y0%2FqGGB%2FoFTsN0jlvZimAu%2FKonIiFRNc5FGuDSMh3kGnf2iWNUjZT2B5s7kwZRK7EvO74rFmzle7HJyLd%2F%2BexXCpRdrsi%2F%2Fcjz0WBU%2FgIxIdNlELbrZQ7MVGIv8u9TlKwX2m%2BKFBvjF2mHFYjzAg1xQNrbyhdU7OrmesvSyiTCk5cS9BjqkAbTvAQB98XCW5UOXaRcSASpKM2L0VN0YMGRLRq3YP%2BLjujKxCZgoVzUy387ONOOdDAVQek04R68bR4SKxAEXhGBIqh0jTt7rGjWdXULIHcYEsupJYFIZotuYTIS1974LbIYuuwRNHy1N7QeNLS0PMJ5kkMTVFP0Yu33cklxKAzdvQAxMdyw%2BOETeHN66mM5Ueu3sRQdw7XkSdZwJ%2B9ZsFBDjma%2BV&X-Amz-Signature=d40741a9cd1bb6fd2efeb922e3b30a12f966e286ceef9d1f7134ea9ce63581cc&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFATKI5Z%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIHnyjekpU%2BhVYTwSGrvR6rmvsi63hTRRYkKrl%2Fgk8u4aAiAwpXRkAJHgCZuSEngkBM%2ByAiL4KS4UDZSVe3hG1ghwwCr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMFN%2FOmsP5K8NEThmaKtwDOqnQegpZSC%2FTeX%2B5PWUewFLQZ0pyR29h8atzeQ8evQsWFtJehuhPE9Q2pSGXseVmpdI6bIcyTy7%2F3M9BndAARlCKXKlXFKmDhJhEhe7mDGtwnXOpAa%2FzP4svNbv9nEDb1p10Vj8lSOGJFWdgDLwDCMysnun5%2BACld%2B0LJeJ2BQJLTkIJ7I5bsgdRDd%2FxqOHOm5Hyl1gl5SNFjh76mAbgPH6wxpKaVjUmM%2FPMn1R%2BIZ3LdFkSTTVR62JhWoV7uPj1KICDL%2Bmc7yuPtrEeM1S%2Btd66wnJI7Ln0J6oULsxMVszEubvvzua6q9g4gH639TWv4JxgGws9g2U8W2sVdG9AoAF4NTFe7H1Wsg4CQZuNkxQh6sacWMNhnCnDv4T2VZnmHhYWxqj3OEfaPfiQD21pX5YypTXp%2Bh%2FHMpv%2BE4rqFpFp1Su2OJRhrGdjTD46q6z6NIrdt5c16f2JTgj%2BxjfGS9Lmb7ENYsxWEsUAoWtHiYCG5JUXh%2B2TVqm5fVK9s3Wws328BuCd%2B8miFAfElGkrSxMVGaIxBbbCq47hARprxQ9wNaGpSXf9Di4oP8im65IM0ANtEmTpNsPcpkWD0f4FW6JcCbDX6A%2Bb6y53K%2Bp2kI%2FTOAy00pfCKJ5iuqcw6eTEvQY6pgF7sCeL5CNHHq3i58IUpsz2oP4Kd5KkMYb0VKfyC%2FksaeTPzynriXeDSaXzLjct1HWBeaKDPOfRKTtT%2BCVjIYQzElGPoQ5rHoAL1v%2FrCZMHlw1EvcPKcdNj9f35dA4vOR3BaXzO9%2FLtEx5lZgRYY7BHuBGrUDgZCcuOdAKOr6RhB1lEoCxbYLpBu0YcjC%2Fm2fjJcAhBzINFdnyGPmeJ%2FWovkjAtQFhY&X-Amz-Signature=de5c0fa01b4f33c5c476d647d5180f770aad5d9ff7c845ae4e4596e2dd9e8d8e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFATKI5Z%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIHnyjekpU%2BhVYTwSGrvR6rmvsi63hTRRYkKrl%2Fgk8u4aAiAwpXRkAJHgCZuSEngkBM%2ByAiL4KS4UDZSVe3hG1ghwwCr%2FAwhSEAAaDDYzNzQyMzE4MzgwNSIMFN%2FOmsP5K8NEThmaKtwDOqnQegpZSC%2FTeX%2B5PWUewFLQZ0pyR29h8atzeQ8evQsWFtJehuhPE9Q2pSGXseVmpdI6bIcyTy7%2F3M9BndAARlCKXKlXFKmDhJhEhe7mDGtwnXOpAa%2FzP4svNbv9nEDb1p10Vj8lSOGJFWdgDLwDCMysnun5%2BACld%2B0LJeJ2BQJLTkIJ7I5bsgdRDd%2FxqOHOm5Hyl1gl5SNFjh76mAbgPH6wxpKaVjUmM%2FPMn1R%2BIZ3LdFkSTTVR62JhWoV7uPj1KICDL%2Bmc7yuPtrEeM1S%2Btd66wnJI7Ln0J6oULsxMVszEubvvzua6q9g4gH639TWv4JxgGws9g2U8W2sVdG9AoAF4NTFe7H1Wsg4CQZuNkxQh6sacWMNhnCnDv4T2VZnmHhYWxqj3OEfaPfiQD21pX5YypTXp%2Bh%2FHMpv%2BE4rqFpFp1Su2OJRhrGdjTD46q6z6NIrdt5c16f2JTgj%2BxjfGS9Lmb7ENYsxWEsUAoWtHiYCG5JUXh%2B2TVqm5fVK9s3Wws328BuCd%2B8miFAfElGkrSxMVGaIxBbbCq47hARprxQ9wNaGpSXf9Di4oP8im65IM0ANtEmTpNsPcpkWD0f4FW6JcCbDX6A%2Bb6y53K%2Bp2kI%2FTOAy00pfCKJ5iuqcw6eTEvQY6pgF7sCeL5CNHHq3i58IUpsz2oP4Kd5KkMYb0VKfyC%2FksaeTPzynriXeDSaXzLjct1HWBeaKDPOfRKTtT%2BCVjIYQzElGPoQ5rHoAL1v%2FrCZMHlw1EvcPKcdNj9f35dA4vOR3BaXzO9%2FLtEx5lZgRYY7BHuBGrUDgZCcuOdAKOr6RhB1lEoCxbYLpBu0YcjC%2Fm2fjJcAhBzINFdnyGPmeJ%2FWovkjAtQFhY&X-Amz-Signature=3f007d9e6c80d977eed6c107255479fb8de972791b5aacf434153cf98ad691d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY7DRD2O%2F20250216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250216T004208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQCPTHjYFhuXIMyw7JmEHsQRLt584OxyHWtLaO%2FgcGX7uAIhAOk9lIXFxN12%2FeAjh5C084r7uusJGlVubx3NgROdUMr9Kv8DCFIQABoMNjM3NDIzMTgzODA1Igw1FXT8rixfMkvS5wQq3AMTkdB6CCCUpFFZN73o2FMjaKJro86aXNWh8WgHkJtRoZaVY4SyfJpMXtTfQ%2B9Y4ifh8l6mb%2BXTA%2B6sAWeliAqTADRVGYM7sH97MtrQsZc%2Bt95SIg%2Fecvwj5Uzta7bZMJoi375CkV991Z14SR7mDI2XJq2djnk%2F%2FspwoXhZXryiNzW53%2FEFluI9mfwRIZGsriDWqUkbJY2A2I%2B4vv0r5MOhas5z6vmPHhThH28IjiTai7fcLc49A8ZEYiy7vi7dH3LUn5MuDsBII%2FQ4KSa2QnxcA7WvyurU01COqdv2D8xO84x9j1txqgdCZOJn7%2FQatZBR1EFEAUktMcyE%2FDGyiZTxvlwOYm5qknVEGEWU%2Bbmyr1F8UJhUTr2dwhLFdBjs5YV37KW7iuJZ38dsVc42CefjwBC7NolAdnk9Xtlp97fHy713LqTXP1KaWaIIJaiZpkBAKa69J4cFQT6uv5Zw1Y0%2FqGGB%2FoFTsN0jlvZimAu%2FKonIiFRNc5FGuDSMh3kGnf2iWNUjZT2B5s7kwZRK7EvO74rFmzle7HJyLd%2F%2BexXCpRdrsi%2F%2Fcjz0WBU%2FgIxIdNlELbrZQ7MVGIv8u9TlKwX2m%2BKFBvjF2mHFYjzAg1xQNrbyhdU7OrmesvSyiTCk5cS9BjqkAbTvAQB98XCW5UOXaRcSASpKM2L0VN0YMGRLRq3YP%2BLjujKxCZgoVzUy387ONOOdDAVQek04R68bR4SKxAEXhGBIqh0jTt7rGjWdXULIHcYEsupJYFIZotuYTIS1974LbIYuuwRNHy1N7QeNLS0PMJ5kkMTVFP0Yu33cklxKAzdvQAxMdyw%2BOETeHN66mM5Ueu3sRQdw7XkSdZwJ%2B9ZsFBDjma%2BV&X-Amz-Signature=80d48f9ee988fafdd01d20bb1718fe5e093eff5866fe7a44bdc6779dbfa9f671&X-Amz-SignedHeaders=host&x-id=GetObject)
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