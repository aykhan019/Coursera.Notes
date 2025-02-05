

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPPJBCZI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQDd0Y%2FxGnZfhMZ6ZQl7crBAB9oHKs3kB7VFls3d3ByUJQIhAOLtIjV7h%2BZN3v1Pb368lFhOWe3VVJaYBMZje8TpXg7dKv8DCD8QABoMNjM3NDIzMTgzODA1Igx0w%2BBHL0L%2BHSjj%2FTEq3APbrww0mg5Kc3fWdA0r3eIrkzTXAxElVbzXri9%2Bb%2FVwlqsd7C7IDqPzxU3ySvkZXKfqOzdFAY2mOpF9zQIebdhk1%2FMROHYIpgQxcHXGFFWuP2Pjf5wMBAFeCYnYEoJEC9VxYfgJHUqrS2GcmnVHi2FkSryQcwl%2Fh99WwSBVJUAtiNfejLMoAQbCvlqOahcKzQrOpoj3F1BLWmeBzvmpyEfCtH1SWDTk9DbwudGzPw14xfqR1F3HGvNQ3LHV1130%2FYove2%2B2p8UmCkKFbINZMhMWtLRPrXbsHqCGHhxIZ2WhPKis8fr5oSJG%2FEATWdccLHcvSYp4RW7eIcjMCdFZa9I1JB88m7o9OIaAKJUSipWomEULPx6WNlqJvUENqst8K44hU3p9UVuah55%2B9VadiDJY%2FBIQRviK4L8QB2HH2ystSlzSNJwcHEwvGml1PsoIwpw7w3rv1qLV%2BJXe2dB%2FeY7t6fdHXbSaGiTKJ5b%2Bfp04TPC%2Bp1ve%2FiZ8mDSjxdlErzP8Z%2FTFj0bcXwtjsoCeJYIX8In0A7TkEc9VNjlGhakgViTBcJPiDVP5llVRiQfkCblGRzNrcHZMxHokomcJxT1SruAUTKPmhgEFAJ6lD25PDHMk%2FihhImHqeGXiYjCJ%2Bou9BjqkAZeeezunpknvE1bPiD82%2Fje8Z5%2BcYJ7rPR%2BB0aWF5yYWdVsynHDgVnNMUZ4xQG9QjNZew8NZIQtNymLmqFUexel%2FapTJGM8EDPqYw7ZAsBMVoW%2BLeQTypNB2wI0EapG1vKRVN30gn8PQqLcPyXCQH5DejHvl%2BLPqmotZb1mGx3h3QHCRjul6rXzy9yvQK%2FFlAPJCtR6rdiYS8rrvKTa%2FCVZsbWig&X-Amz-Signature=e67d8bd5201bb1e82c7e738739a2dd3b088f77f5fca499e7c384e460e01bc9fe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPPJBCZI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQDd0Y%2FxGnZfhMZ6ZQl7crBAB9oHKs3kB7VFls3d3ByUJQIhAOLtIjV7h%2BZN3v1Pb368lFhOWe3VVJaYBMZje8TpXg7dKv8DCD8QABoMNjM3NDIzMTgzODA1Igx0w%2BBHL0L%2BHSjj%2FTEq3APbrww0mg5Kc3fWdA0r3eIrkzTXAxElVbzXri9%2Bb%2FVwlqsd7C7IDqPzxU3ySvkZXKfqOzdFAY2mOpF9zQIebdhk1%2FMROHYIpgQxcHXGFFWuP2Pjf5wMBAFeCYnYEoJEC9VxYfgJHUqrS2GcmnVHi2FkSryQcwl%2Fh99WwSBVJUAtiNfejLMoAQbCvlqOahcKzQrOpoj3F1BLWmeBzvmpyEfCtH1SWDTk9DbwudGzPw14xfqR1F3HGvNQ3LHV1130%2FYove2%2B2p8UmCkKFbINZMhMWtLRPrXbsHqCGHhxIZ2WhPKis8fr5oSJG%2FEATWdccLHcvSYp4RW7eIcjMCdFZa9I1JB88m7o9OIaAKJUSipWomEULPx6WNlqJvUENqst8K44hU3p9UVuah55%2B9VadiDJY%2FBIQRviK4L8QB2HH2ystSlzSNJwcHEwvGml1PsoIwpw7w3rv1qLV%2BJXe2dB%2FeY7t6fdHXbSaGiTKJ5b%2Bfp04TPC%2Bp1ve%2FiZ8mDSjxdlErzP8Z%2FTFj0bcXwtjsoCeJYIX8In0A7TkEc9VNjlGhakgViTBcJPiDVP5llVRiQfkCblGRzNrcHZMxHokomcJxT1SruAUTKPmhgEFAJ6lD25PDHMk%2FihhImHqeGXiYjCJ%2Bou9BjqkAZeeezunpknvE1bPiD82%2Fje8Z5%2BcYJ7rPR%2BB0aWF5yYWdVsynHDgVnNMUZ4xQG9QjNZew8NZIQtNymLmqFUexel%2FapTJGM8EDPqYw7ZAsBMVoW%2BLeQTypNB2wI0EapG1vKRVN30gn8PQqLcPyXCQH5DejHvl%2BLPqmotZb1mGx3h3QHCRjul6rXzy9yvQK%2FFlAPJCtR6rdiYS8rrvKTa%2FCVZsbWig&X-Amz-Signature=309de8c2ed91a85083583a61cc08b824b49f883c1269528fa093821e15c4264d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPPJBCZI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQDd0Y%2FxGnZfhMZ6ZQl7crBAB9oHKs3kB7VFls3d3ByUJQIhAOLtIjV7h%2BZN3v1Pb368lFhOWe3VVJaYBMZje8TpXg7dKv8DCD8QABoMNjM3NDIzMTgzODA1Igx0w%2BBHL0L%2BHSjj%2FTEq3APbrww0mg5Kc3fWdA0r3eIrkzTXAxElVbzXri9%2Bb%2FVwlqsd7C7IDqPzxU3ySvkZXKfqOzdFAY2mOpF9zQIebdhk1%2FMROHYIpgQxcHXGFFWuP2Pjf5wMBAFeCYnYEoJEC9VxYfgJHUqrS2GcmnVHi2FkSryQcwl%2Fh99WwSBVJUAtiNfejLMoAQbCvlqOahcKzQrOpoj3F1BLWmeBzvmpyEfCtH1SWDTk9DbwudGzPw14xfqR1F3HGvNQ3LHV1130%2FYove2%2B2p8UmCkKFbINZMhMWtLRPrXbsHqCGHhxIZ2WhPKis8fr5oSJG%2FEATWdccLHcvSYp4RW7eIcjMCdFZa9I1JB88m7o9OIaAKJUSipWomEULPx6WNlqJvUENqst8K44hU3p9UVuah55%2B9VadiDJY%2FBIQRviK4L8QB2HH2ystSlzSNJwcHEwvGml1PsoIwpw7w3rv1qLV%2BJXe2dB%2FeY7t6fdHXbSaGiTKJ5b%2Bfp04TPC%2Bp1ve%2FiZ8mDSjxdlErzP8Z%2FTFj0bcXwtjsoCeJYIX8In0A7TkEc9VNjlGhakgViTBcJPiDVP5llVRiQfkCblGRzNrcHZMxHokomcJxT1SruAUTKPmhgEFAJ6lD25PDHMk%2FihhImHqeGXiYjCJ%2Bou9BjqkAZeeezunpknvE1bPiD82%2Fje8Z5%2BcYJ7rPR%2BB0aWF5yYWdVsynHDgVnNMUZ4xQG9QjNZew8NZIQtNymLmqFUexel%2FapTJGM8EDPqYw7ZAsBMVoW%2BLeQTypNB2wI0EapG1vKRVN30gn8PQqLcPyXCQH5DejHvl%2BLPqmotZb1mGx3h3QHCRjul6rXzy9yvQK%2FFlAPJCtR6rdiYS8rrvKTa%2FCVZsbWig&X-Amz-Signature=759a395e0417508566af2d09132a646b53ee02ec54eb25c9a7de0343cc4e599f&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WYLQ3YV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBj2%2Fvu4nstejBucf2CCblZxKFevcDfpabbWALepkGkYAiEAiKGlBhSaqbMBe41dGXH0WmSyOcQEMynOZ%2Fl05PjW%2Bloq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDNUhX9LXShq0w79qTCrcA5BB9HMjXAvH15eX2%2BYVPEFgasnV8AMOaxHkoYSSBmOI5etz60IMWCNQUjT%2B%2Bx2LeBMyLVBiovXl%2FrefJtG6ryeJcUJX6yVzDDdwe6dOBSeARJ%2BzQVw1yLOBMcKY9wEQWwzrNrii4aQLf71g2Blvv4gRJHyjeF%2BiKqaez0Cbh7AkYdf1YxF9ND3EKPLxFP1NmABPwmKRJL0rB33Ksq7UMgfqC1L6oBq37nVvuFlD%2BGSxUfhTwpNH78rinZqLqkWikYgfPnbUhfwn6Vwk7zmRGS0TBd5Q9mOuFLbCm5JosDEi4oml7vb3CqisJM9emVJC2y6cU7Ck%2Ble5pxqgcPmrKeuzShzNTXFbfzBr5CJ0v76br%2BvqxCHkA9beFIVmhEs%2BUDd88AUNYPA8DwQ056%2F%2FZUETigAnhIuVnZ%2Bzh064qRICDbYpNSmETjhxrcA%2F5rucy%2FgTVLG7mUGcJAFRg%2BsCqTw8boOCkdWwuxDcL7zK3PxCtTbGUqby8ZzP3ePlzVSdixFxlovIQfR4DSGb49Xr%2FVnuK3CDK3e9%2BPMA6N0vMq7k1kTRxEqszx0dEkSB2ShY9gz%2FzQRVU1YzDKTO69f09ZuLxcs4aVeCa0UPzFu%2BySQG6u%2B70EkU%2BOS2ZQF8MID6i70GOqUBWQxU%2BEwtgOjKoLfKy1EsLX8BrHo4mffEe%2FK69ftA8bkd72tCmO9nHPg%2FtJ%2BVyoIDhPpRRE3LmEqbhTJO6FOh0vaEDtpJCGq%2BJ%2FGVfVqD6Dar%2Blm%2F9sHA3U1STflkhSBhm4tzSaOdJErYOf7OllZDlRQMMCc%2F7ViAQ8mnYMTa7RYYBsVxj1xduSWeuWy3Pm26R68NpurE9BpCX%2BptCdDhOv8fjEIZ&X-Amz-Signature=b5f5ade8c04cd9c7f0cacccfd807bed5851c781c87bdc8656940eadc5a421ce8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WYLQ3YV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBj2%2Fvu4nstejBucf2CCblZxKFevcDfpabbWALepkGkYAiEAiKGlBhSaqbMBe41dGXH0WmSyOcQEMynOZ%2Fl05PjW%2Bloq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDNUhX9LXShq0w79qTCrcA5BB9HMjXAvH15eX2%2BYVPEFgasnV8AMOaxHkoYSSBmOI5etz60IMWCNQUjT%2B%2Bx2LeBMyLVBiovXl%2FrefJtG6ryeJcUJX6yVzDDdwe6dOBSeARJ%2BzQVw1yLOBMcKY9wEQWwzrNrii4aQLf71g2Blvv4gRJHyjeF%2BiKqaez0Cbh7AkYdf1YxF9ND3EKPLxFP1NmABPwmKRJL0rB33Ksq7UMgfqC1L6oBq37nVvuFlD%2BGSxUfhTwpNH78rinZqLqkWikYgfPnbUhfwn6Vwk7zmRGS0TBd5Q9mOuFLbCm5JosDEi4oml7vb3CqisJM9emVJC2y6cU7Ck%2Ble5pxqgcPmrKeuzShzNTXFbfzBr5CJ0v76br%2BvqxCHkA9beFIVmhEs%2BUDd88AUNYPA8DwQ056%2F%2FZUETigAnhIuVnZ%2Bzh064qRICDbYpNSmETjhxrcA%2F5rucy%2FgTVLG7mUGcJAFRg%2BsCqTw8boOCkdWwuxDcL7zK3PxCtTbGUqby8ZzP3ePlzVSdixFxlovIQfR4DSGb49Xr%2FVnuK3CDK3e9%2BPMA6N0vMq7k1kTRxEqszx0dEkSB2ShY9gz%2FzQRVU1YzDKTO69f09ZuLxcs4aVeCa0UPzFu%2BySQG6u%2B70EkU%2BOS2ZQF8MID6i70GOqUBWQxU%2BEwtgOjKoLfKy1EsLX8BrHo4mffEe%2FK69ftA8bkd72tCmO9nHPg%2FtJ%2BVyoIDhPpRRE3LmEqbhTJO6FOh0vaEDtpJCGq%2BJ%2FGVfVqD6Dar%2Blm%2F9sHA3U1STflkhSBhm4tzSaOdJErYOf7OllZDlRQMMCc%2F7ViAQ8mnYMTa7RYYBsVxj1xduSWeuWy3Pm26R68NpurE9BpCX%2BptCdDhOv8fjEIZ&X-Amz-Signature=54b4f561547a72d4c674b7bde648a003cbd37fffcbf36e51f3ba8c4c4c26d5a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPPJBCZI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQDd0Y%2FxGnZfhMZ6ZQl7crBAB9oHKs3kB7VFls3d3ByUJQIhAOLtIjV7h%2BZN3v1Pb368lFhOWe3VVJaYBMZje8TpXg7dKv8DCD8QABoMNjM3NDIzMTgzODA1Igx0w%2BBHL0L%2BHSjj%2FTEq3APbrww0mg5Kc3fWdA0r3eIrkzTXAxElVbzXri9%2Bb%2FVwlqsd7C7IDqPzxU3ySvkZXKfqOzdFAY2mOpF9zQIebdhk1%2FMROHYIpgQxcHXGFFWuP2Pjf5wMBAFeCYnYEoJEC9VxYfgJHUqrS2GcmnVHi2FkSryQcwl%2Fh99WwSBVJUAtiNfejLMoAQbCvlqOahcKzQrOpoj3F1BLWmeBzvmpyEfCtH1SWDTk9DbwudGzPw14xfqR1F3HGvNQ3LHV1130%2FYove2%2B2p8UmCkKFbINZMhMWtLRPrXbsHqCGHhxIZ2WhPKis8fr5oSJG%2FEATWdccLHcvSYp4RW7eIcjMCdFZa9I1JB88m7o9OIaAKJUSipWomEULPx6WNlqJvUENqst8K44hU3p9UVuah55%2B9VadiDJY%2FBIQRviK4L8QB2HH2ystSlzSNJwcHEwvGml1PsoIwpw7w3rv1qLV%2BJXe2dB%2FeY7t6fdHXbSaGiTKJ5b%2Bfp04TPC%2Bp1ve%2FiZ8mDSjxdlErzP8Z%2FTFj0bcXwtjsoCeJYIX8In0A7TkEc9VNjlGhakgViTBcJPiDVP5llVRiQfkCblGRzNrcHZMxHokomcJxT1SruAUTKPmhgEFAJ6lD25PDHMk%2FihhImHqeGXiYjCJ%2Bou9BjqkAZeeezunpknvE1bPiD82%2Fje8Z5%2BcYJ7rPR%2BB0aWF5yYWdVsynHDgVnNMUZ4xQG9QjNZew8NZIQtNymLmqFUexel%2FapTJGM8EDPqYw7ZAsBMVoW%2BLeQTypNB2wI0EapG1vKRVN30gn8PQqLcPyXCQH5DejHvl%2BLPqmotZb1mGx3h3QHCRjul6rXzy9yvQK%2FFlAPJCtR6rdiYS8rrvKTa%2FCVZsbWig&X-Amz-Signature=f93a60f8482f115a9a0f6ae0c985a4808779c202f01fef16f9f171e4d6a99efd&X-Amz-SignedHeaders=host&x-id=GetObject)
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