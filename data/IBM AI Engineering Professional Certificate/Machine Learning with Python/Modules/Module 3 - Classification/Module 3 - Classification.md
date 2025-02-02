

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHOXSZWQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJRAHtH2uTNONnuWK1a2wvCVlbTqbkiX%2B3XJ%2FVdW1RGwIhAKilcF72unWMjTSKGIT9lnv18TNhhoAoY2InwJ7dOQpDKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzGS3Ceav3p6zjKfCsq3ANFOZZ1GgqnIBNrPkCJRVRG56aaZb021KLqjvjy6RMQ1mvE6mKv6gRJuXPT4%2BQwuPp%2FEUsYefUyH6q9ddTHTX8VgBt6fBrqwAO%2Bj5e%2Fu9zApArIgjMKC%2FyDKMXhJrU39zCMGrO6HEYPDcPN1vQEOzQ164Sjtuxv1OjH9Wj3XmR7%2BTRWAmra%2FxpFjzhKj1WzVl%2FrTvOfT0L42nAcLlJdzfyG3U04BprR0DQzvSLqeJMFd1hK0gQOafo4CLt6dYvNVQnyfWRF56nMFZ9EySV5X4wgDmvnEC9FL52dELMZOcfiLimV0R9G8gwBbKDOt3cbeh57UdUxPIJhu7hu8TV5NUQGdjbSkAqqpnhhLMUH%2FLca0H2e0CsBa74My07zVLQgCM4Z3rxQ3kNIP9W%2FdF2zDiBiitoHxwkB7FGYJ761KAwwNC72XJlwqZpwG0kzdqOOY5sucWmMjeaEyPJDwQSIqECRB2LJVwnSU%2FrXBgrmPGitxu5r2SnRbt2fBiEC7eOYd9bqPte0Y6QVkDcVqzs0W3gKrCAryUDSB4iPHH96gQ4AyiXdvi0hvwvuG%2B%2B0aEqQ%2Bk9ej1cjX%2Bl28oTxNHq3D5MyiZfzAAH7sC0syR68GB91QRekCbRmJHhgxUBCbDC64fu8BjqkAW1%2BpXXh5xM%2FLbg1TDV5NKTvCFIssc74nkJVcgV8uYrlXGMMCyb4CcjDd5N%2FjSjNjVu2g4InujLNYz4qX51ebCCAHxOMeYN850wVD9sRA9vh%2BQcyikHi6pMN9L3YXtlNCsbcl%2F9in%2FTN5lioRjLPhvpB9XT%2BlG%2B5YA9NlgrcT4e0E9hG4HoNkt0hCMRhqVw8cnY4yCtX7AHoA5Ztfl6JFtlKaHfW&X-Amz-Signature=a2525a203997dd190f0d6d928ae5d5fd3929c68c9a67c61f30b4ab7dd7d5c3ab&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHOXSZWQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJRAHtH2uTNONnuWK1a2wvCVlbTqbkiX%2B3XJ%2FVdW1RGwIhAKilcF72unWMjTSKGIT9lnv18TNhhoAoY2InwJ7dOQpDKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzGS3Ceav3p6zjKfCsq3ANFOZZ1GgqnIBNrPkCJRVRG56aaZb021KLqjvjy6RMQ1mvE6mKv6gRJuXPT4%2BQwuPp%2FEUsYefUyH6q9ddTHTX8VgBt6fBrqwAO%2Bj5e%2Fu9zApArIgjMKC%2FyDKMXhJrU39zCMGrO6HEYPDcPN1vQEOzQ164Sjtuxv1OjH9Wj3XmR7%2BTRWAmra%2FxpFjzhKj1WzVl%2FrTvOfT0L42nAcLlJdzfyG3U04BprR0DQzvSLqeJMFd1hK0gQOafo4CLt6dYvNVQnyfWRF56nMFZ9EySV5X4wgDmvnEC9FL52dELMZOcfiLimV0R9G8gwBbKDOt3cbeh57UdUxPIJhu7hu8TV5NUQGdjbSkAqqpnhhLMUH%2FLca0H2e0CsBa74My07zVLQgCM4Z3rxQ3kNIP9W%2FdF2zDiBiitoHxwkB7FGYJ761KAwwNC72XJlwqZpwG0kzdqOOY5sucWmMjeaEyPJDwQSIqECRB2LJVwnSU%2FrXBgrmPGitxu5r2SnRbt2fBiEC7eOYd9bqPte0Y6QVkDcVqzs0W3gKrCAryUDSB4iPHH96gQ4AyiXdvi0hvwvuG%2B%2B0aEqQ%2Bk9ej1cjX%2Bl28oTxNHq3D5MyiZfzAAH7sC0syR68GB91QRekCbRmJHhgxUBCbDC64fu8BjqkAW1%2BpXXh5xM%2FLbg1TDV5NKTvCFIssc74nkJVcgV8uYrlXGMMCyb4CcjDd5N%2FjSjNjVu2g4InujLNYz4qX51ebCCAHxOMeYN850wVD9sRA9vh%2BQcyikHi6pMN9L3YXtlNCsbcl%2F9in%2FTN5lioRjLPhvpB9XT%2BlG%2B5YA9NlgrcT4e0E9hG4HoNkt0hCMRhqVw8cnY4yCtX7AHoA5Ztfl6JFtlKaHfW&X-Amz-Signature=cd99523bea1c00b673c6f96b69e2a5d097a59a8730e69dddf31e6af6a442da0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHOXSZWQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJRAHtH2uTNONnuWK1a2wvCVlbTqbkiX%2B3XJ%2FVdW1RGwIhAKilcF72unWMjTSKGIT9lnv18TNhhoAoY2InwJ7dOQpDKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzGS3Ceav3p6zjKfCsq3ANFOZZ1GgqnIBNrPkCJRVRG56aaZb021KLqjvjy6RMQ1mvE6mKv6gRJuXPT4%2BQwuPp%2FEUsYefUyH6q9ddTHTX8VgBt6fBrqwAO%2Bj5e%2Fu9zApArIgjMKC%2FyDKMXhJrU39zCMGrO6HEYPDcPN1vQEOzQ164Sjtuxv1OjH9Wj3XmR7%2BTRWAmra%2FxpFjzhKj1WzVl%2FrTvOfT0L42nAcLlJdzfyG3U04BprR0DQzvSLqeJMFd1hK0gQOafo4CLt6dYvNVQnyfWRF56nMFZ9EySV5X4wgDmvnEC9FL52dELMZOcfiLimV0R9G8gwBbKDOt3cbeh57UdUxPIJhu7hu8TV5NUQGdjbSkAqqpnhhLMUH%2FLca0H2e0CsBa74My07zVLQgCM4Z3rxQ3kNIP9W%2FdF2zDiBiitoHxwkB7FGYJ761KAwwNC72XJlwqZpwG0kzdqOOY5sucWmMjeaEyPJDwQSIqECRB2LJVwnSU%2FrXBgrmPGitxu5r2SnRbt2fBiEC7eOYd9bqPte0Y6QVkDcVqzs0W3gKrCAryUDSB4iPHH96gQ4AyiXdvi0hvwvuG%2B%2B0aEqQ%2Bk9ej1cjX%2Bl28oTxNHq3D5MyiZfzAAH7sC0syR68GB91QRekCbRmJHhgxUBCbDC64fu8BjqkAW1%2BpXXh5xM%2FLbg1TDV5NKTvCFIssc74nkJVcgV8uYrlXGMMCyb4CcjDd5N%2FjSjNjVu2g4InujLNYz4qX51ebCCAHxOMeYN850wVD9sRA9vh%2BQcyikHi6pMN9L3YXtlNCsbcl%2F9in%2FTN5lioRjLPhvpB9XT%2BlG%2B5YA9NlgrcT4e0E9hG4HoNkt0hCMRhqVw8cnY4yCtX7AHoA5Ztfl6JFtlKaHfW&X-Amz-Signature=0ebf2435a71e07dd884b57175d610b9880fc30374e9a441aa359774f3eea785f&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZAECE5R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICI%2Ffqq2uaAc58v7JXvhSqLLX1th12xfFtiMurDcz22WAiEA1HLXVruJnNwtrJoiRP8jJAtmOvHjUAOhCmdGXJJ%2FZUcqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG2ZhsaWUVai7giOLCrcA6IKcSvfHZ45quBIaGq2UdQ%2FpJU86OX7oZTee9dK%2BhitB%2BZYhH0pFLjEoiDF9pZn%2BhQH526S3HUl8dD3Vt30TNwIYly17mI0s9NaeTbai6CaqY79%2FjkX%2FDh%2FtpWM6pfR2w4HeUl4fX4xnhXLdoTdBmQb4yMC4ZXbD6t1fT4ep%2F38uc7AHIeMVD6roP%2BL%2B%2F0gKSe9vv0P0K2VI7urHg1ZgWt3I1f7q6PvtSqgk%2B%2BDYDacZYOURbBZe1J0Mgy1ddiabk%2FiY3pZMwiGh8ERJHhnoI%2FAQOH31%2FeSCH75g4zEztzcm%2F7foVnFhbgCZ5RlE3C31e9RuPhZQOY7hiXI6agv6aAVpbIgW0EKr%2FMq1zHq4kNQzbEeZ2kGvRaJ5rdLZyv8a%2FWLyuFqnjhGTnNM0sIrfl3WzTAUkK6M%2B5K1ujXqLRHZlYgPCMr1E%2FHV288%2Bq%2FyR2lcIN9VrJsWk8owcshONJsOZ%2FPfjNKw1noWJ5nTiAfOeaHqeOxC2TmvOZUizYUsA3dc9lzikhaHKf8LomUtuiazqkKgOOz5X7zOCI5149jcnhLE%2BdQDTy5bgFLwsk5LVayQVsllYIbdJoMWGkuJp1T%2Bpy58MZr5lhyICRV9EjWrq2s%2Fg%2B4Rh44e5RHPHMNjh%2B7wGOqUBWp3DEgY3vL9hmeNpVEF%2BfHMUFvLbv9cIZDA4TvTCEf%2F4RyDfP%2BXK5QpBSNHY2e1C5dDRItlmt0GkLagwWQub38YyZVrOERxDwYbrMKK%2BIpjTuT0BHnqFumWN%2BUtsj6kFXmL2zg0zLUqnSVyUzUTP0AtpYGYpoSbO%2Fxjm0YmXviuoASrE0A1ztvkjilLIc%2ByHw8fot8Ho%2FRNax0dChYtDHIvIzt0C&X-Amz-Signature=1b9541f386403241b97cfd1ebadd26672e60b801e2be8ef152ba3682f4761727&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZAECE5R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICI%2Ffqq2uaAc58v7JXvhSqLLX1th12xfFtiMurDcz22WAiEA1HLXVruJnNwtrJoiRP8jJAtmOvHjUAOhCmdGXJJ%2FZUcqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG2ZhsaWUVai7giOLCrcA6IKcSvfHZ45quBIaGq2UdQ%2FpJU86OX7oZTee9dK%2BhitB%2BZYhH0pFLjEoiDF9pZn%2BhQH526S3HUl8dD3Vt30TNwIYly17mI0s9NaeTbai6CaqY79%2FjkX%2FDh%2FtpWM6pfR2w4HeUl4fX4xnhXLdoTdBmQb4yMC4ZXbD6t1fT4ep%2F38uc7AHIeMVD6roP%2BL%2B%2F0gKSe9vv0P0K2VI7urHg1ZgWt3I1f7q6PvtSqgk%2B%2BDYDacZYOURbBZe1J0Mgy1ddiabk%2FiY3pZMwiGh8ERJHhnoI%2FAQOH31%2FeSCH75g4zEztzcm%2F7foVnFhbgCZ5RlE3C31e9RuPhZQOY7hiXI6agv6aAVpbIgW0EKr%2FMq1zHq4kNQzbEeZ2kGvRaJ5rdLZyv8a%2FWLyuFqnjhGTnNM0sIrfl3WzTAUkK6M%2B5K1ujXqLRHZlYgPCMr1E%2FHV288%2Bq%2FyR2lcIN9VrJsWk8owcshONJsOZ%2FPfjNKw1noWJ5nTiAfOeaHqeOxC2TmvOZUizYUsA3dc9lzikhaHKf8LomUtuiazqkKgOOz5X7zOCI5149jcnhLE%2BdQDTy5bgFLwsk5LVayQVsllYIbdJoMWGkuJp1T%2Bpy58MZr5lhyICRV9EjWrq2s%2Fg%2B4Rh44e5RHPHMNjh%2B7wGOqUBWp3DEgY3vL9hmeNpVEF%2BfHMUFvLbv9cIZDA4TvTCEf%2F4RyDfP%2BXK5QpBSNHY2e1C5dDRItlmt0GkLagwWQub38YyZVrOERxDwYbrMKK%2BIpjTuT0BHnqFumWN%2BUtsj6kFXmL2zg0zLUqnSVyUzUTP0AtpYGYpoSbO%2Fxjm0YmXviuoASrE0A1ztvkjilLIc%2ByHw8fot8Ho%2FRNax0dChYtDHIvIzt0C&X-Amz-Signature=fb0ae53ede0035efdf49d02ff2e2a306e55e4f1693f2722fd22e7d9bddc81ead&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHOXSZWQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJRAHtH2uTNONnuWK1a2wvCVlbTqbkiX%2B3XJ%2FVdW1RGwIhAKilcF72unWMjTSKGIT9lnv18TNhhoAoY2InwJ7dOQpDKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzGS3Ceav3p6zjKfCsq3ANFOZZ1GgqnIBNrPkCJRVRG56aaZb021KLqjvjy6RMQ1mvE6mKv6gRJuXPT4%2BQwuPp%2FEUsYefUyH6q9ddTHTX8VgBt6fBrqwAO%2Bj5e%2Fu9zApArIgjMKC%2FyDKMXhJrU39zCMGrO6HEYPDcPN1vQEOzQ164Sjtuxv1OjH9Wj3XmR7%2BTRWAmra%2FxpFjzhKj1WzVl%2FrTvOfT0L42nAcLlJdzfyG3U04BprR0DQzvSLqeJMFd1hK0gQOafo4CLt6dYvNVQnyfWRF56nMFZ9EySV5X4wgDmvnEC9FL52dELMZOcfiLimV0R9G8gwBbKDOt3cbeh57UdUxPIJhu7hu8TV5NUQGdjbSkAqqpnhhLMUH%2FLca0H2e0CsBa74My07zVLQgCM4Z3rxQ3kNIP9W%2FdF2zDiBiitoHxwkB7FGYJ761KAwwNC72XJlwqZpwG0kzdqOOY5sucWmMjeaEyPJDwQSIqECRB2LJVwnSU%2FrXBgrmPGitxu5r2SnRbt2fBiEC7eOYd9bqPte0Y6QVkDcVqzs0W3gKrCAryUDSB4iPHH96gQ4AyiXdvi0hvwvuG%2B%2B0aEqQ%2Bk9ej1cjX%2Bl28oTxNHq3D5MyiZfzAAH7sC0syR68GB91QRekCbRmJHhgxUBCbDC64fu8BjqkAW1%2BpXXh5xM%2FLbg1TDV5NKTvCFIssc74nkJVcgV8uYrlXGMMCyb4CcjDd5N%2FjSjNjVu2g4InujLNYz4qX51ebCCAHxOMeYN850wVD9sRA9vh%2BQcyikHi6pMN9L3YXtlNCsbcl%2F9in%2FTN5lioRjLPhvpB9XT%2BlG%2B5YA9NlgrcT4e0E9hG4HoNkt0hCMRhqVw8cnY4yCtX7AHoA5Ztfl6JFtlKaHfW&X-Amz-Signature=79c93baf124beea679b128f1c6aae95083fe175ef023f274f6534220cc0a7945&X-Amz-SignedHeaders=host&x-id=GetObject)
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