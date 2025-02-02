

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFTSSXIU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYAJsNoMSEnZEAOBUdwxcxvD7TFhpGetnj5P2TEvyVkAIgVUoy7MDUOw6cHPy7h1UlLYZ4DQwNxMWuIuU0GDXfoOsqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC5FOsQ4JRbpgvrwVyrcA6obajHyGgz9m8wqmp8BYP6i0sKoS9VpXhweqwJV7fDBo03HCv6%2BJ7uZHJgLrD5VtR0%2Foe2Z6yPjhqTzlSkJqIpi4SpABfsKkoLKPEcM81wmtuARf3VTHCnq5hvbd1L1W2axu3Lzv%2FVXI7EkJfzcw7DtheuKIVtf9IXrvFB0wzQG%2Fi2xKnxd1PiccjiPKmym1pdFYnqkJsKkej8CSkXsQkqVyh%2FvwFr2g91bG0QuwP0SbzrC8FGV6hY6AE6%2FArAXJUZ2HJUfZlb7PK2MYWFZEhVXEZ%2BeZrub0B%2F9pxmXZtmwPvvdQDruPimhFgo22uYtuUV%2BZc02P96lYvnDpNFmtdigUbuwVrWmgUG7kXQLPjtPDw4Sx0gkfSYI%2FVFYBz2%2BFN07E2VRt%2B4ZmcHlgl1RJOfeRnd06qlr9iWXIEXFcIFnQhzuVfm%2FnRFdBQNdGqArLc5X0%2Bc6uviYGbb557eihG77lSFjTNW%2BqnnpFZumHZwGiYTcflatvW5HXANUlKikbJCoQytqZnCtQwNBnm9VuLBE%2F2sVCY5KG4G9VgfPjaJJIf%2FGK1vSFmHnsIplUKX%2FRR8v2gBpZyrF7qu0D6tpumug5abREdzP6JN27ZUZLeJdBOFA316rRR%2FeCwgSMJbu%2FLwGOqUBj14bEO71DhesxQAk6ysacKUP91DE97ENpWFbhbRGZCk4salw9QizwsBfAjT79YKcp1hSbVuqGHgBjnVuvACoIz3UE9q%2By91CoNuZfJefkv%2Bs%2B05q4QM5nvsLguiKuCqGuo0PSwrZLgUCF4K73L1Rq%2F%2BOOr4k4%2F8M079n2J6QDScRwpVAnekOHC7%2FKYUXnIVHyQOEO3ChCyEvRKNBuc5Ysj%2BNaY4k&X-Amz-Signature=2d7643ad17703ab36a1c5ebbb361d0fc937a6daa96815e5e4beb247e18e41f24&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFTSSXIU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYAJsNoMSEnZEAOBUdwxcxvD7TFhpGetnj5P2TEvyVkAIgVUoy7MDUOw6cHPy7h1UlLYZ4DQwNxMWuIuU0GDXfoOsqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC5FOsQ4JRbpgvrwVyrcA6obajHyGgz9m8wqmp8BYP6i0sKoS9VpXhweqwJV7fDBo03HCv6%2BJ7uZHJgLrD5VtR0%2Foe2Z6yPjhqTzlSkJqIpi4SpABfsKkoLKPEcM81wmtuARf3VTHCnq5hvbd1L1W2axu3Lzv%2FVXI7EkJfzcw7DtheuKIVtf9IXrvFB0wzQG%2Fi2xKnxd1PiccjiPKmym1pdFYnqkJsKkej8CSkXsQkqVyh%2FvwFr2g91bG0QuwP0SbzrC8FGV6hY6AE6%2FArAXJUZ2HJUfZlb7PK2MYWFZEhVXEZ%2BeZrub0B%2F9pxmXZtmwPvvdQDruPimhFgo22uYtuUV%2BZc02P96lYvnDpNFmtdigUbuwVrWmgUG7kXQLPjtPDw4Sx0gkfSYI%2FVFYBz2%2BFN07E2VRt%2B4ZmcHlgl1RJOfeRnd06qlr9iWXIEXFcIFnQhzuVfm%2FnRFdBQNdGqArLc5X0%2Bc6uviYGbb557eihG77lSFjTNW%2BqnnpFZumHZwGiYTcflatvW5HXANUlKikbJCoQytqZnCtQwNBnm9VuLBE%2F2sVCY5KG4G9VgfPjaJJIf%2FGK1vSFmHnsIplUKX%2FRR8v2gBpZyrF7qu0D6tpumug5abREdzP6JN27ZUZLeJdBOFA316rRR%2FeCwgSMJbu%2FLwGOqUBj14bEO71DhesxQAk6ysacKUP91DE97ENpWFbhbRGZCk4salw9QizwsBfAjT79YKcp1hSbVuqGHgBjnVuvACoIz3UE9q%2By91CoNuZfJefkv%2Bs%2B05q4QM5nvsLguiKuCqGuo0PSwrZLgUCF4K73L1Rq%2F%2BOOr4k4%2F8M079n2J6QDScRwpVAnekOHC7%2FKYUXnIVHyQOEO3ChCyEvRKNBuc5Ysj%2BNaY4k&X-Amz-Signature=29b510bf02aeec5c35b3498bcc86a1af21630841c6214ce357a6931395735c56&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFTSSXIU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYAJsNoMSEnZEAOBUdwxcxvD7TFhpGetnj5P2TEvyVkAIgVUoy7MDUOw6cHPy7h1UlLYZ4DQwNxMWuIuU0GDXfoOsqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC5FOsQ4JRbpgvrwVyrcA6obajHyGgz9m8wqmp8BYP6i0sKoS9VpXhweqwJV7fDBo03HCv6%2BJ7uZHJgLrD5VtR0%2Foe2Z6yPjhqTzlSkJqIpi4SpABfsKkoLKPEcM81wmtuARf3VTHCnq5hvbd1L1W2axu3Lzv%2FVXI7EkJfzcw7DtheuKIVtf9IXrvFB0wzQG%2Fi2xKnxd1PiccjiPKmym1pdFYnqkJsKkej8CSkXsQkqVyh%2FvwFr2g91bG0QuwP0SbzrC8FGV6hY6AE6%2FArAXJUZ2HJUfZlb7PK2MYWFZEhVXEZ%2BeZrub0B%2F9pxmXZtmwPvvdQDruPimhFgo22uYtuUV%2BZc02P96lYvnDpNFmtdigUbuwVrWmgUG7kXQLPjtPDw4Sx0gkfSYI%2FVFYBz2%2BFN07E2VRt%2B4ZmcHlgl1RJOfeRnd06qlr9iWXIEXFcIFnQhzuVfm%2FnRFdBQNdGqArLc5X0%2Bc6uviYGbb557eihG77lSFjTNW%2BqnnpFZumHZwGiYTcflatvW5HXANUlKikbJCoQytqZnCtQwNBnm9VuLBE%2F2sVCY5KG4G9VgfPjaJJIf%2FGK1vSFmHnsIplUKX%2FRR8v2gBpZyrF7qu0D6tpumug5abREdzP6JN27ZUZLeJdBOFA316rRR%2FeCwgSMJbu%2FLwGOqUBj14bEO71DhesxQAk6ysacKUP91DE97ENpWFbhbRGZCk4salw9QizwsBfAjT79YKcp1hSbVuqGHgBjnVuvACoIz3UE9q%2By91CoNuZfJefkv%2Bs%2B05q4QM5nvsLguiKuCqGuo0PSwrZLgUCF4K73L1Rq%2F%2BOOr4k4%2F8M079n2J6QDScRwpVAnekOHC7%2FKYUXnIVHyQOEO3ChCyEvRKNBuc5Ysj%2BNaY4k&X-Amz-Signature=4575eae0b28ce9cf5e623b820c1b3deef45e03c40fc522c80ef684e60b70496b&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ5BVNSN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaQTzDBNtMLj15N2zuk4QulQYopqiTc9sOkK9yKea3dQIgTkmmesbcWF9cX1k0CJouW95LhQWHxViUvqbEK2BZOQMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHNZfzEP8JCNBM3zNCrcAyqBkD8acHZO6SHZiCY%2BtHrXfPUq3dp%2Bccjq50TJ1YZ%2F59%2F%2B%2BQZH%2F9pZ%2B0RrHjs6DeALFe7eFe%2FM1Lf1A1PvHDN%2FptvLmBLyYfar9zlhhMG0JMeWhmJbele1gbeQb0uJpqm49ZVIZEiMoyUUhKoxj6%2Fdbe%2FYk3XYOYfmBHWvy0s61hRaQBLW6IbqnajYbS5eSjLBfF6bo%2FI7U9nOcNhNUNdDQxFZTHHGb%2BWhpcic4L%2BWbojUOibSPzyLoqNYedhEXUWebxO0ASAJ%2FXNpvFy68RYvfxdmm6kDsqs3rEdYT254Ldr69ikRY1Wtqt%2BRozUb3oBf7J1hwEHHFr8c9zT0KJcbS5B6avgZuI9hrbyFaHwK58c0xQlu%2BJq6RHGRw6m0cuUMqm%2FUwm15pSsu%2FIZoWwTQ59uK5di5AT291FTRwU0hJN2Ty7PKjjX9SCY2tQKF6XI9%2Bs0CK2FGAAopWLrT9hvLjQf1bdf8DSq0Bfy%2BgzFhZqTUDUEDYA9BYR1ac7oPMoeUlUT%2Fb7foqi%2BO%2B1iF8MUPwPXuMRcitUgxmLwDg%2BxyNMH6%2B0Jxl0EAWcqt%2FkYDYM3FS3gscv3gEx8M3iEUZSeVEP4EGpgrVFw%2FWoDBdgAqgJmE5MfjZx%2Bgd9IfMI6c%2FLwGOqUBuxZmegHN2sN0MhNQRt6c%2BiO4XcKc0CZHZeapNJ%2BKvhEBlHNriphxcVVLY5KkzxlGXqrNx4Br3FCt643ePgYSN2diFYypch%2F6aImsJciouGnMWJs8bGm7qnEZX38jd6f39EvOJE4HzlBRoCYjswtjwk9XVWTk6MgavvRW0lkQYTDD%2BZltpKeYKNUloeHAquPJxxjdsMKQbm8Qs1TkLcEPy%2F9G2qH0&X-Amz-Signature=7f85c106ed2f1d6b35cf57e71fa634f493f605a7cc71db8496a5f97fd1e705da&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ5BVNSN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaQTzDBNtMLj15N2zuk4QulQYopqiTc9sOkK9yKea3dQIgTkmmesbcWF9cX1k0CJouW95LhQWHxViUvqbEK2BZOQMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHNZfzEP8JCNBM3zNCrcAyqBkD8acHZO6SHZiCY%2BtHrXfPUq3dp%2Bccjq50TJ1YZ%2F59%2F%2B%2BQZH%2F9pZ%2B0RrHjs6DeALFe7eFe%2FM1Lf1A1PvHDN%2FptvLmBLyYfar9zlhhMG0JMeWhmJbele1gbeQb0uJpqm49ZVIZEiMoyUUhKoxj6%2Fdbe%2FYk3XYOYfmBHWvy0s61hRaQBLW6IbqnajYbS5eSjLBfF6bo%2FI7U9nOcNhNUNdDQxFZTHHGb%2BWhpcic4L%2BWbojUOibSPzyLoqNYedhEXUWebxO0ASAJ%2FXNpvFy68RYvfxdmm6kDsqs3rEdYT254Ldr69ikRY1Wtqt%2BRozUb3oBf7J1hwEHHFr8c9zT0KJcbS5B6avgZuI9hrbyFaHwK58c0xQlu%2BJq6RHGRw6m0cuUMqm%2FUwm15pSsu%2FIZoWwTQ59uK5di5AT291FTRwU0hJN2Ty7PKjjX9SCY2tQKF6XI9%2Bs0CK2FGAAopWLrT9hvLjQf1bdf8DSq0Bfy%2BgzFhZqTUDUEDYA9BYR1ac7oPMoeUlUT%2Fb7foqi%2BO%2B1iF8MUPwPXuMRcitUgxmLwDg%2BxyNMH6%2B0Jxl0EAWcqt%2FkYDYM3FS3gscv3gEx8M3iEUZSeVEP4EGpgrVFw%2FWoDBdgAqgJmE5MfjZx%2Bgd9IfMI6c%2FLwGOqUBuxZmegHN2sN0MhNQRt6c%2BiO4XcKc0CZHZeapNJ%2BKvhEBlHNriphxcVVLY5KkzxlGXqrNx4Br3FCt643ePgYSN2diFYypch%2F6aImsJciouGnMWJs8bGm7qnEZX38jd6f39EvOJE4HzlBRoCYjswtjwk9XVWTk6MgavvRW0lkQYTDD%2BZltpKeYKNUloeHAquPJxxjdsMKQbm8Qs1TkLcEPy%2F9G2qH0&X-Amz-Signature=1e77573281c622a240e0a91175cc5781ae2dd490866540e96e9961912e1cf1f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFTSSXIU%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYAJsNoMSEnZEAOBUdwxcxvD7TFhpGetnj5P2TEvyVkAIgVUoy7MDUOw6cHPy7h1UlLYZ4DQwNxMWuIuU0GDXfoOsqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC5FOsQ4JRbpgvrwVyrcA6obajHyGgz9m8wqmp8BYP6i0sKoS9VpXhweqwJV7fDBo03HCv6%2BJ7uZHJgLrD5VtR0%2Foe2Z6yPjhqTzlSkJqIpi4SpABfsKkoLKPEcM81wmtuARf3VTHCnq5hvbd1L1W2axu3Lzv%2FVXI7EkJfzcw7DtheuKIVtf9IXrvFB0wzQG%2Fi2xKnxd1PiccjiPKmym1pdFYnqkJsKkej8CSkXsQkqVyh%2FvwFr2g91bG0QuwP0SbzrC8FGV6hY6AE6%2FArAXJUZ2HJUfZlb7PK2MYWFZEhVXEZ%2BeZrub0B%2F9pxmXZtmwPvvdQDruPimhFgo22uYtuUV%2BZc02P96lYvnDpNFmtdigUbuwVrWmgUG7kXQLPjtPDw4Sx0gkfSYI%2FVFYBz2%2BFN07E2VRt%2B4ZmcHlgl1RJOfeRnd06qlr9iWXIEXFcIFnQhzuVfm%2FnRFdBQNdGqArLc5X0%2Bc6uviYGbb557eihG77lSFjTNW%2BqnnpFZumHZwGiYTcflatvW5HXANUlKikbJCoQytqZnCtQwNBnm9VuLBE%2F2sVCY5KG4G9VgfPjaJJIf%2FGK1vSFmHnsIplUKX%2FRR8v2gBpZyrF7qu0D6tpumug5abREdzP6JN27ZUZLeJdBOFA316rRR%2FeCwgSMJbu%2FLwGOqUBj14bEO71DhesxQAk6ysacKUP91DE97ENpWFbhbRGZCk4salw9QizwsBfAjT79YKcp1hSbVuqGHgBjnVuvACoIz3UE9q%2By91CoNuZfJefkv%2Bs%2B05q4QM5nvsLguiKuCqGuo0PSwrZLgUCF4K73L1Rq%2F%2BOOr4k4%2F8M079n2J6QDScRwpVAnekOHC7%2FKYUXnIVHyQOEO3ChCyEvRKNBuc5Ysj%2BNaY4k&X-Amz-Signature=c7a10239224eb88d00a933c3038e88e2597d06af7293e9544ab13ce31d857a8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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