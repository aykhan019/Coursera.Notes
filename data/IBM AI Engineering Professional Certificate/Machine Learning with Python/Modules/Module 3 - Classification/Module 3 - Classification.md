

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4XITN6I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIFoHe85UeFEfBgu4aSFhNX429P8%2Bk1147oW0ghHhduRpAiAGoA1Az%2F8Otjq4eRrAfbPyb78nDr2goa%2FKTiq0aWAQZyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMOQ9kTL8Jz0rHbs5eKtwDnUazAPM4P3KL5oq0I3xOl%2FXMfgQR1DhfMpFkoxb5DmMnb2I8WSGw%2F%2F94%2BRJV4ndsr7VDrZ2kot4P4RF2rJIybSk6jsPFMAMUsZ8j2HGzw6qseMArLUnDR7YPO3CIGfZ%2B26fwBhCKiCN4vZc886nvn0TqClyoBksuqF5Wk1upq2jJEtTyLlzsURG1jCP%2Fx5PqfY6Xcz4V5LZtGACxiGTcVxg6e0wtTiQ9FkLpVd5zIqGVWwCMHbHtUx6k3RzFTUcyl6BoH%2B3zcHxrVZ6OgZP0hbi65hbr8Gl%2BAbySxfu02nCeVSPJ7TyZF%2BgGAfICP0c%2FWRjfH%2FNTL%2BH8L%2BUwXJoiaRx4H5HUSeOSdjuNK44Lg6bK61bASBmRT7KrChNgyR1%2FpKP1ViW0FHIbah5RyJwVoM%2B4dQ0cAswla4drsPRCldqXeZX6ijbpB4sjdgoQPXIdujmWKnnpugqv%2FDD3kt3YGUkER3zUKky0lKad3RP4FZmTxQsxr8g1WR9StZQ0H9%2BVnmXkcrksKTl%2BAlkKJDlDSP2YCgSIPI%2Fijq6tavjYSPTNIgnsjh6e%2FtWYm%2FmrxTYLafvCWrM12JXwVH44Y2ej6Rel2t9%2FYmJca7xBvdQsrxLX4wwpzfrpCupPv9wwuO%2BMvQY6pgERJN5fLaVQp8Gax2uqOAGHalFxM91%2FgwHa5Txl%2Fq%2FFqASAj7Dk2IuCbfP%2B4jbWEduSmVJO5RxCj571Geyt2IzK9bCuRhXsWwmMt%2BilVfMYfCKRfZ%2FV%2FHEalGr6yWDCwpL30ic3ZVDpN6jXAQAywamS7nbhChNvrd0f4W283FhOghZ0OwDCE7SxL0rLoGZk7ynR6mWQP7gN7vvaS2Lg%2Fqp5NJQx5pml&X-Amz-Signature=572cb8668e576b962c36bba39d215948b6da886740e39c1ff1b1294fd43f4390&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4XITN6I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIFoHe85UeFEfBgu4aSFhNX429P8%2Bk1147oW0ghHhduRpAiAGoA1Az%2F8Otjq4eRrAfbPyb78nDr2goa%2FKTiq0aWAQZyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMOQ9kTL8Jz0rHbs5eKtwDnUazAPM4P3KL5oq0I3xOl%2FXMfgQR1DhfMpFkoxb5DmMnb2I8WSGw%2F%2F94%2BRJV4ndsr7VDrZ2kot4P4RF2rJIybSk6jsPFMAMUsZ8j2HGzw6qseMArLUnDR7YPO3CIGfZ%2B26fwBhCKiCN4vZc886nvn0TqClyoBksuqF5Wk1upq2jJEtTyLlzsURG1jCP%2Fx5PqfY6Xcz4V5LZtGACxiGTcVxg6e0wtTiQ9FkLpVd5zIqGVWwCMHbHtUx6k3RzFTUcyl6BoH%2B3zcHxrVZ6OgZP0hbi65hbr8Gl%2BAbySxfu02nCeVSPJ7TyZF%2BgGAfICP0c%2FWRjfH%2FNTL%2BH8L%2BUwXJoiaRx4H5HUSeOSdjuNK44Lg6bK61bASBmRT7KrChNgyR1%2FpKP1ViW0FHIbah5RyJwVoM%2B4dQ0cAswla4drsPRCldqXeZX6ijbpB4sjdgoQPXIdujmWKnnpugqv%2FDD3kt3YGUkER3zUKky0lKad3RP4FZmTxQsxr8g1WR9StZQ0H9%2BVnmXkcrksKTl%2BAlkKJDlDSP2YCgSIPI%2Fijq6tavjYSPTNIgnsjh6e%2FtWYm%2FmrxTYLafvCWrM12JXwVH44Y2ej6Rel2t9%2FYmJca7xBvdQsrxLX4wwpzfrpCupPv9wwuO%2BMvQY6pgERJN5fLaVQp8Gax2uqOAGHalFxM91%2FgwHa5Txl%2Fq%2FFqASAj7Dk2IuCbfP%2B4jbWEduSmVJO5RxCj571Geyt2IzK9bCuRhXsWwmMt%2BilVfMYfCKRfZ%2FV%2FHEalGr6yWDCwpL30ic3ZVDpN6jXAQAywamS7nbhChNvrd0f4W283FhOghZ0OwDCE7SxL0rLoGZk7ynR6mWQP7gN7vvaS2Lg%2Fqp5NJQx5pml&X-Amz-Signature=1ca5409ddf6cf764415e5b9c70e7f83907b6c717501639b9b384fb1821e88fbe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4XITN6I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIFoHe85UeFEfBgu4aSFhNX429P8%2Bk1147oW0ghHhduRpAiAGoA1Az%2F8Otjq4eRrAfbPyb78nDr2goa%2FKTiq0aWAQZyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMOQ9kTL8Jz0rHbs5eKtwDnUazAPM4P3KL5oq0I3xOl%2FXMfgQR1DhfMpFkoxb5DmMnb2I8WSGw%2F%2F94%2BRJV4ndsr7VDrZ2kot4P4RF2rJIybSk6jsPFMAMUsZ8j2HGzw6qseMArLUnDR7YPO3CIGfZ%2B26fwBhCKiCN4vZc886nvn0TqClyoBksuqF5Wk1upq2jJEtTyLlzsURG1jCP%2Fx5PqfY6Xcz4V5LZtGACxiGTcVxg6e0wtTiQ9FkLpVd5zIqGVWwCMHbHtUx6k3RzFTUcyl6BoH%2B3zcHxrVZ6OgZP0hbi65hbr8Gl%2BAbySxfu02nCeVSPJ7TyZF%2BgGAfICP0c%2FWRjfH%2FNTL%2BH8L%2BUwXJoiaRx4H5HUSeOSdjuNK44Lg6bK61bASBmRT7KrChNgyR1%2FpKP1ViW0FHIbah5RyJwVoM%2B4dQ0cAswla4drsPRCldqXeZX6ijbpB4sjdgoQPXIdujmWKnnpugqv%2FDD3kt3YGUkER3zUKky0lKad3RP4FZmTxQsxr8g1WR9StZQ0H9%2BVnmXkcrksKTl%2BAlkKJDlDSP2YCgSIPI%2Fijq6tavjYSPTNIgnsjh6e%2FtWYm%2FmrxTYLafvCWrM12JXwVH44Y2ej6Rel2t9%2FYmJca7xBvdQsrxLX4wwpzfrpCupPv9wwuO%2BMvQY6pgERJN5fLaVQp8Gax2uqOAGHalFxM91%2FgwHa5Txl%2Fq%2FFqASAj7Dk2IuCbfP%2B4jbWEduSmVJO5RxCj571Geyt2IzK9bCuRhXsWwmMt%2BilVfMYfCKRfZ%2FV%2FHEalGr6yWDCwpL30ic3ZVDpN6jXAQAywamS7nbhChNvrd0f4W283FhOghZ0OwDCE7SxL0rLoGZk7ynR6mWQP7gN7vvaS2Lg%2Fqp5NJQx5pml&X-Amz-Signature=37dbc222639d05f196d8642b2372241cb1c0470fffcda9614f1ce133780e8d12&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVVXSJ3K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCiFPm1%2B4c8JLv3khHHd1qzx%2FLfH5pSdi8FR641E3HdQwIhAOVAw%2FL15%2FaeOSwThLHN%2FHKXO9LzU%2FkDrdtp1p1qmNaZKv8DCEMQABoMNjM3NDIzMTgzODA1Igz3Lyhtc%2BDKRAEALSAq3AO91jHkihOGVQEa6IvH%2FUB1yZdHspvvLBu9OGzEUsUYr5ItofTCkCtk%2FxV2lSYuV1YAwqE9f0yeT4T4iK5urvLYqLL2XTWScIA9y4Ky6zEDYOTBl7jAnkZ7rYSdRy0%2FvZYZo%2BqlZRi%2F9Lf7qLA1ibgKMqvFNReGsj%2BMoBDcuVpdMwaobqMrN3kBIo6AIOGp%2FBts7rWuX6UKgD%2FlC%2FKNVFbe%2F9roOL6F4WCHcX4yokAQJ%2F31WwuMO%2Bji8pVIAyM4Sz0a76HCFBGmw2ERxI0bQQdc8Y%2FAK2lEGlG9WNrR3hsLmRowGe8XKjmxlZaKtRB5Zfq%2FoflCXTrhPPWK1ZrmOY6jBGrR3%2BIoqWiFLIfi1gH7CNAXnFX4txIP%2Bd3qn7ULcjSBHUOE4B1T7JHkfad0JscwY89M314MVmEwcyq4ayJ1oTKuWES7SOqX02%2B%2FRWy8q%2B1sFlzUJc8HfiLv1lJ6RVocJKaVpPyyTyDsNreuGIv5BC2mvkQBX%2B4faX8m0QQZiwRQeF6SCghnue03I4emO3zp29bN6KI0COke30IpKVVOeidJYJbj%2BuH1G54gAxWv9B38jHwOnbxDoipCg3JED5nD%2FT4A2Hfz0FHiwE%2F5u1e%2FSOSiZ5GSfXW5%2Bj8lADCt74y9BjqkAauC%2FA0%2ByTdeY83rqE2c73B%2FzAmfc6%2Ba4bJQDkr3KFSgJGphvb8%2BlrZEDzh0TlXxumllvBbfXefXqDrbcU6mXvJiFW245Zp8Lia256N%2B8%2FgGO1jfiEFqYnR86YyoJ%2FPpezvRJwj9IEpaFueYJZpf27gdGiTZ15ExD58l32oNhWp9lTr%2FGaDbvjTp1ZhrofS4otRrpMRmqc1Qjigub76JhQWNa4ac&X-Amz-Signature=51b4731fda3a031c68e25c74a7a096c5914598371e84273ecdc16fa80b0c86e7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVVXSJ3K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCiFPm1%2B4c8JLv3khHHd1qzx%2FLfH5pSdi8FR641E3HdQwIhAOVAw%2FL15%2FaeOSwThLHN%2FHKXO9LzU%2FkDrdtp1p1qmNaZKv8DCEMQABoMNjM3NDIzMTgzODA1Igz3Lyhtc%2BDKRAEALSAq3AO91jHkihOGVQEa6IvH%2FUB1yZdHspvvLBu9OGzEUsUYr5ItofTCkCtk%2FxV2lSYuV1YAwqE9f0yeT4T4iK5urvLYqLL2XTWScIA9y4Ky6zEDYOTBl7jAnkZ7rYSdRy0%2FvZYZo%2BqlZRi%2F9Lf7qLA1ibgKMqvFNReGsj%2BMoBDcuVpdMwaobqMrN3kBIo6AIOGp%2FBts7rWuX6UKgD%2FlC%2FKNVFbe%2F9roOL6F4WCHcX4yokAQJ%2F31WwuMO%2Bji8pVIAyM4Sz0a76HCFBGmw2ERxI0bQQdc8Y%2FAK2lEGlG9WNrR3hsLmRowGe8XKjmxlZaKtRB5Zfq%2FoflCXTrhPPWK1ZrmOY6jBGrR3%2BIoqWiFLIfi1gH7CNAXnFX4txIP%2Bd3qn7ULcjSBHUOE4B1T7JHkfad0JscwY89M314MVmEwcyq4ayJ1oTKuWES7SOqX02%2B%2FRWy8q%2B1sFlzUJc8HfiLv1lJ6RVocJKaVpPyyTyDsNreuGIv5BC2mvkQBX%2B4faX8m0QQZiwRQeF6SCghnue03I4emO3zp29bN6KI0COke30IpKVVOeidJYJbj%2BuH1G54gAxWv9B38jHwOnbxDoipCg3JED5nD%2FT4A2Hfz0FHiwE%2F5u1e%2FSOSiZ5GSfXW5%2Bj8lADCt74y9BjqkAauC%2FA0%2ByTdeY83rqE2c73B%2FzAmfc6%2Ba4bJQDkr3KFSgJGphvb8%2BlrZEDzh0TlXxumllvBbfXefXqDrbcU6mXvJiFW245Zp8Lia256N%2B8%2FgGO1jfiEFqYnR86YyoJ%2FPpezvRJwj9IEpaFueYJZpf27gdGiTZ15ExD58l32oNhWp9lTr%2FGaDbvjTp1ZhrofS4otRrpMRmqc1Qjigub76JhQWNa4ac&X-Amz-Signature=ab47e8fe962bb5d11c7592bcff205b4ff02d41b39c2d03755917b52adaee52fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4XITN6I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIFoHe85UeFEfBgu4aSFhNX429P8%2Bk1147oW0ghHhduRpAiAGoA1Az%2F8Otjq4eRrAfbPyb78nDr2goa%2FKTiq0aWAQZyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMOQ9kTL8Jz0rHbs5eKtwDnUazAPM4P3KL5oq0I3xOl%2FXMfgQR1DhfMpFkoxb5DmMnb2I8WSGw%2F%2F94%2BRJV4ndsr7VDrZ2kot4P4RF2rJIybSk6jsPFMAMUsZ8j2HGzw6qseMArLUnDR7YPO3CIGfZ%2B26fwBhCKiCN4vZc886nvn0TqClyoBksuqF5Wk1upq2jJEtTyLlzsURG1jCP%2Fx5PqfY6Xcz4V5LZtGACxiGTcVxg6e0wtTiQ9FkLpVd5zIqGVWwCMHbHtUx6k3RzFTUcyl6BoH%2B3zcHxrVZ6OgZP0hbi65hbr8Gl%2BAbySxfu02nCeVSPJ7TyZF%2BgGAfICP0c%2FWRjfH%2FNTL%2BH8L%2BUwXJoiaRx4H5HUSeOSdjuNK44Lg6bK61bASBmRT7KrChNgyR1%2FpKP1ViW0FHIbah5RyJwVoM%2B4dQ0cAswla4drsPRCldqXeZX6ijbpB4sjdgoQPXIdujmWKnnpugqv%2FDD3kt3YGUkER3zUKky0lKad3RP4FZmTxQsxr8g1WR9StZQ0H9%2BVnmXkcrksKTl%2BAlkKJDlDSP2YCgSIPI%2Fijq6tavjYSPTNIgnsjh6e%2FtWYm%2FmrxTYLafvCWrM12JXwVH44Y2ej6Rel2t9%2FYmJca7xBvdQsrxLX4wwpzfrpCupPv9wwuO%2BMvQY6pgERJN5fLaVQp8Gax2uqOAGHalFxM91%2FgwHa5Txl%2Fq%2FFqASAj7Dk2IuCbfP%2B4jbWEduSmVJO5RxCj571Geyt2IzK9bCuRhXsWwmMt%2BilVfMYfCKRfZ%2FV%2FHEalGr6yWDCwpL30ic3ZVDpN6jXAQAywamS7nbhChNvrd0f4W283FhOghZ0OwDCE7SxL0rLoGZk7ynR6mWQP7gN7vvaS2Lg%2Fqp5NJQx5pml&X-Amz-Signature=a1d567bb68deb5c0f061112f45494e3d598161103d6e17fa7204cea539484737&X-Amz-SignedHeaders=host&x-id=GetObject)
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