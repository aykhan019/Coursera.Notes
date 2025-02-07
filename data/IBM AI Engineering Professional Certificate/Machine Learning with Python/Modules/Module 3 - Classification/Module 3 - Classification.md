

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIHNVTR3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEqabHYCnqrRxihKuOMDzTjXX37S1lMZVdZC3%2FjXCZ4kAiBoN64zyPaCDJ8wpSDB22zPKsV23JkOjQWcAXXBVls76Sr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIM2OBEigTG5Wb8Ij1KKtwDnZQNeGT%2BZqIM33hKXIIMxL4WMZDEAKpF5JLKaFVCXKciRP%2FhUa9t4RRr9TwNXjVklLGXNJHRXiTTlgH%2BzfFFqU9BEqgQUn9lAnF7apyBMRti8MNbthamxGIbBiRSbl1UvvUDpylAeafuykrgRuotCjH7CnDJkzyy7RrPpHPtVDm1so%2FH0OAdVnLAOxN%2FNGCiRljFX57xRqVQ%2Fy4CnkF%2BorOqaZ%2F8VI9YCXdCvH233hUK1nYJ7vetUoUGeHerRJ%2B6MpYlqH1KohUYfa3CDnxSPVrRxvik5b5r%2FQKiW009KbAz%2F5QzmgTTK2fZXopiU%2B5PLmMItPOKVGYxSkqS7%2B4MWoT83gshOqt1MdxQc0kuiG%2B5rkJNWtyNhvT6SnkbYd6R4HkvU8bWstATHbslluRGABS08OlOhxd3CmQBP8aTAJ9%2BS7%2BO4rhfcmYyxxoLY9oS1TutgPcweR9D%2BhEhzeB04%2FEhKQBGmrmLDpuzFPVKPFjzAGhbCfv7B2LfLrC5IpvJnTFExs%2BMg%2FVzTxGKnN67PiFzjaP7ZruCM8phB43Taa6l510d8uLaB4Rcs93k06x9dNWES4YzxPbRJMsF%2Bn9ZdKYfSpJ0u0fBaXjT36bp0ppdBmvy5xPdLfMGUKcw9YqYvQY6pgF%2BJeaBbKWX9L8P7euLTzyPLQ%2FTbwZu1hCURd8JWaohoiiZYfqHOz45I7eWFbDmrK%2B8uPdmZRzWw244306QUdZigX8JLJOIb2cWuGhcR4BVclexUYgERGZG9OH2M0j2Kci3%2Bx8xni2lwpPwwoZZNpYg6ANhBLp9s9MEZwC0YDJ6%2FqT0b%2BTdaF9BQHG7pFP5PVVlzNnIxmQworuOY%2BrpWFVzN5wPwQbl&X-Amz-Signature=26812de85e3a1b0e50559a8323c332f8921784dd50f8dd7547a505cb389a49ed&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIHNVTR3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEqabHYCnqrRxihKuOMDzTjXX37S1lMZVdZC3%2FjXCZ4kAiBoN64zyPaCDJ8wpSDB22zPKsV23JkOjQWcAXXBVls76Sr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIM2OBEigTG5Wb8Ij1KKtwDnZQNeGT%2BZqIM33hKXIIMxL4WMZDEAKpF5JLKaFVCXKciRP%2FhUa9t4RRr9TwNXjVklLGXNJHRXiTTlgH%2BzfFFqU9BEqgQUn9lAnF7apyBMRti8MNbthamxGIbBiRSbl1UvvUDpylAeafuykrgRuotCjH7CnDJkzyy7RrPpHPtVDm1so%2FH0OAdVnLAOxN%2FNGCiRljFX57xRqVQ%2Fy4CnkF%2BorOqaZ%2F8VI9YCXdCvH233hUK1nYJ7vetUoUGeHerRJ%2B6MpYlqH1KohUYfa3CDnxSPVrRxvik5b5r%2FQKiW009KbAz%2F5QzmgTTK2fZXopiU%2B5PLmMItPOKVGYxSkqS7%2B4MWoT83gshOqt1MdxQc0kuiG%2B5rkJNWtyNhvT6SnkbYd6R4HkvU8bWstATHbslluRGABS08OlOhxd3CmQBP8aTAJ9%2BS7%2BO4rhfcmYyxxoLY9oS1TutgPcweR9D%2BhEhzeB04%2FEhKQBGmrmLDpuzFPVKPFjzAGhbCfv7B2LfLrC5IpvJnTFExs%2BMg%2FVzTxGKnN67PiFzjaP7ZruCM8phB43Taa6l510d8uLaB4Rcs93k06x9dNWES4YzxPbRJMsF%2Bn9ZdKYfSpJ0u0fBaXjT36bp0ppdBmvy5xPdLfMGUKcw9YqYvQY6pgF%2BJeaBbKWX9L8P7euLTzyPLQ%2FTbwZu1hCURd8JWaohoiiZYfqHOz45I7eWFbDmrK%2B8uPdmZRzWw244306QUdZigX8JLJOIb2cWuGhcR4BVclexUYgERGZG9OH2M0j2Kci3%2Bx8xni2lwpPwwoZZNpYg6ANhBLp9s9MEZwC0YDJ6%2FqT0b%2BTdaF9BQHG7pFP5PVVlzNnIxmQworuOY%2BrpWFVzN5wPwQbl&X-Amz-Signature=54c4af474916ebe3a33c99176e070f04f201a6ecfbe90ee9f30957f080e806a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIHNVTR3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEqabHYCnqrRxihKuOMDzTjXX37S1lMZVdZC3%2FjXCZ4kAiBoN64zyPaCDJ8wpSDB22zPKsV23JkOjQWcAXXBVls76Sr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIM2OBEigTG5Wb8Ij1KKtwDnZQNeGT%2BZqIM33hKXIIMxL4WMZDEAKpF5JLKaFVCXKciRP%2FhUa9t4RRr9TwNXjVklLGXNJHRXiTTlgH%2BzfFFqU9BEqgQUn9lAnF7apyBMRti8MNbthamxGIbBiRSbl1UvvUDpylAeafuykrgRuotCjH7CnDJkzyy7RrPpHPtVDm1so%2FH0OAdVnLAOxN%2FNGCiRljFX57xRqVQ%2Fy4CnkF%2BorOqaZ%2F8VI9YCXdCvH233hUK1nYJ7vetUoUGeHerRJ%2B6MpYlqH1KohUYfa3CDnxSPVrRxvik5b5r%2FQKiW009KbAz%2F5QzmgTTK2fZXopiU%2B5PLmMItPOKVGYxSkqS7%2B4MWoT83gshOqt1MdxQc0kuiG%2B5rkJNWtyNhvT6SnkbYd6R4HkvU8bWstATHbslluRGABS08OlOhxd3CmQBP8aTAJ9%2BS7%2BO4rhfcmYyxxoLY9oS1TutgPcweR9D%2BhEhzeB04%2FEhKQBGmrmLDpuzFPVKPFjzAGhbCfv7B2LfLrC5IpvJnTFExs%2BMg%2FVzTxGKnN67PiFzjaP7ZruCM8phB43Taa6l510d8uLaB4Rcs93k06x9dNWES4YzxPbRJMsF%2Bn9ZdKYfSpJ0u0fBaXjT36bp0ppdBmvy5xPdLfMGUKcw9YqYvQY6pgF%2BJeaBbKWX9L8P7euLTzyPLQ%2FTbwZu1hCURd8JWaohoiiZYfqHOz45I7eWFbDmrK%2B8uPdmZRzWw244306QUdZigX8JLJOIb2cWuGhcR4BVclexUYgERGZG9OH2M0j2Kci3%2Bx8xni2lwpPwwoZZNpYg6ANhBLp9s9MEZwC0YDJ6%2FqT0b%2BTdaF9BQHG7pFP5PVVlzNnIxmQworuOY%2BrpWFVzN5wPwQbl&X-Amz-Signature=c551be1423fc1845623414d0666e5ed2f152db6663c53c9157374e63fd77cfa5&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO4FZJ3T%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQD9pT4OoqFQoKvEZvPTVefMk8WqbGRgoflWMMkgSp09DwIhANr%2BnYwghjvY4Rafw0dSPd5TBfyBI4Wpfk45L978gEgJKv8DCHYQABoMNjM3NDIzMTgzODA1IgwhaEjn2UOI%2FzMX7Iwq3ANkSS0HqgbbL%2FAbyPvqlmFuw9VIj7m73kR07BK35ByLF3%2Fcv%2Fw9SPMF%2B8ORArQLrM5f3x1GK6Je3YzemM%2FGmoT0KJoYZ6R0oiE5WvJmvDsJxeJyoo1VaOALyghAt%2B9vxZi4WLvvIn4dTWMS8RwUzR9v%2Fj3wRGPUxWEY9zlasmBYaGoRD9TWa3m9aeLt6ZFlsSi6%2BGVnHx03gEpBBGCvx26c%2B2t1vsWKj9XhEDnBOYzp%2F5yUF8XjjB3Xz5avfKJZxE1YiequFW6%2FQ9xMi%2Fbsje%2BZkJKDrnGuVln1tnppBAgXQ6dsJEmyjmNgY4kx7UgoXildtcMMGH5Us0ATQVCe5b5jKNcN2V4%2FT8tRBEcoMaicIRwMCz1A6z5yaJlOlnkqlVW8z4ibcmIm%2FZPNkvX3lfebUuqx7JkMrCGAO3BNbuOKcsJTc0aIey4r7TJmsj7TaQ66jiRHUmelg9%2BgazmCmfDJFaatz%2BztolTCgNZtdr3maa2c38lQDs8%2FnpL0edjVBFbpKB6UmzKIZwOiDBDKtQh%2Fwt0bOqpZC4LtRBL13KnD8D71uLbUGEgKdTIlRZRe73kAlo3pKmji4VLlxbVU73QXkZRPMdvh5mpYPgtIzPVmYGHwjLpouoSFOc3IjTCpi5i9BjqkAUTZI%2FfZzn2G%2Be1jR4POp%2ByHKO8lz6rAZleQvWxEYdA4r8liKDDRH%2FukGQ7AtUhw9qGJQsgXXylvWVT%2Bw5UD%2BA%2FGUhdcCjK7ierBH6wr1u4nAK11wNtZ%2BQDVPrbPBDt%2FUkVgwCcU8Qv4%2FFjvzdTs5FHQGFa7jIT8VHQta6Lw%2FAY8IXp2KrhzEu6%2Fz9xFMN5tSqwKfxXWhcGiKeqNVtq0KfhFNCyW&X-Amz-Signature=770f2a4380dfeb3ee415e042425b88afb20db4a9bfb5d87e7bea79049ea5f58b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO4FZJ3T%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQD9pT4OoqFQoKvEZvPTVefMk8WqbGRgoflWMMkgSp09DwIhANr%2BnYwghjvY4Rafw0dSPd5TBfyBI4Wpfk45L978gEgJKv8DCHYQABoMNjM3NDIzMTgzODA1IgwhaEjn2UOI%2FzMX7Iwq3ANkSS0HqgbbL%2FAbyPvqlmFuw9VIj7m73kR07BK35ByLF3%2Fcv%2Fw9SPMF%2B8ORArQLrM5f3x1GK6Je3YzemM%2FGmoT0KJoYZ6R0oiE5WvJmvDsJxeJyoo1VaOALyghAt%2B9vxZi4WLvvIn4dTWMS8RwUzR9v%2Fj3wRGPUxWEY9zlasmBYaGoRD9TWa3m9aeLt6ZFlsSi6%2BGVnHx03gEpBBGCvx26c%2B2t1vsWKj9XhEDnBOYzp%2F5yUF8XjjB3Xz5avfKJZxE1YiequFW6%2FQ9xMi%2Fbsje%2BZkJKDrnGuVln1tnppBAgXQ6dsJEmyjmNgY4kx7UgoXildtcMMGH5Us0ATQVCe5b5jKNcN2V4%2FT8tRBEcoMaicIRwMCz1A6z5yaJlOlnkqlVW8z4ibcmIm%2FZPNkvX3lfebUuqx7JkMrCGAO3BNbuOKcsJTc0aIey4r7TJmsj7TaQ66jiRHUmelg9%2BgazmCmfDJFaatz%2BztolTCgNZtdr3maa2c38lQDs8%2FnpL0edjVBFbpKB6UmzKIZwOiDBDKtQh%2Fwt0bOqpZC4LtRBL13KnD8D71uLbUGEgKdTIlRZRe73kAlo3pKmji4VLlxbVU73QXkZRPMdvh5mpYPgtIzPVmYGHwjLpouoSFOc3IjTCpi5i9BjqkAUTZI%2FfZzn2G%2Be1jR4POp%2ByHKO8lz6rAZleQvWxEYdA4r8liKDDRH%2FukGQ7AtUhw9qGJQsgXXylvWVT%2Bw5UD%2BA%2FGUhdcCjK7ierBH6wr1u4nAK11wNtZ%2BQDVPrbPBDt%2FUkVgwCcU8Qv4%2FFjvzdTs5FHQGFa7jIT8VHQta6Lw%2FAY8IXp2KrhzEu6%2Fz9xFMN5tSqwKfxXWhcGiKeqNVtq0KfhFNCyW&X-Amz-Signature=8dd0f0b33e2833342f25f96ec1826a65784dd5d6fdf9cc2adbda3ac933caf9b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIHNVTR3%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEqabHYCnqrRxihKuOMDzTjXX37S1lMZVdZC3%2FjXCZ4kAiBoN64zyPaCDJ8wpSDB22zPKsV23JkOjQWcAXXBVls76Sr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIM2OBEigTG5Wb8Ij1KKtwDnZQNeGT%2BZqIM33hKXIIMxL4WMZDEAKpF5JLKaFVCXKciRP%2FhUa9t4RRr9TwNXjVklLGXNJHRXiTTlgH%2BzfFFqU9BEqgQUn9lAnF7apyBMRti8MNbthamxGIbBiRSbl1UvvUDpylAeafuykrgRuotCjH7CnDJkzyy7RrPpHPtVDm1so%2FH0OAdVnLAOxN%2FNGCiRljFX57xRqVQ%2Fy4CnkF%2BorOqaZ%2F8VI9YCXdCvH233hUK1nYJ7vetUoUGeHerRJ%2B6MpYlqH1KohUYfa3CDnxSPVrRxvik5b5r%2FQKiW009KbAz%2F5QzmgTTK2fZXopiU%2B5PLmMItPOKVGYxSkqS7%2B4MWoT83gshOqt1MdxQc0kuiG%2B5rkJNWtyNhvT6SnkbYd6R4HkvU8bWstATHbslluRGABS08OlOhxd3CmQBP8aTAJ9%2BS7%2BO4rhfcmYyxxoLY9oS1TutgPcweR9D%2BhEhzeB04%2FEhKQBGmrmLDpuzFPVKPFjzAGhbCfv7B2LfLrC5IpvJnTFExs%2BMg%2FVzTxGKnN67PiFzjaP7ZruCM8phB43Taa6l510d8uLaB4Rcs93k06x9dNWES4YzxPbRJMsF%2Bn9ZdKYfSpJ0u0fBaXjT36bp0ppdBmvy5xPdLfMGUKcw9YqYvQY6pgF%2BJeaBbKWX9L8P7euLTzyPLQ%2FTbwZu1hCURd8JWaohoiiZYfqHOz45I7eWFbDmrK%2B8uPdmZRzWw244306QUdZigX8JLJOIb2cWuGhcR4BVclexUYgERGZG9OH2M0j2Kci3%2Bx8xni2lwpPwwoZZNpYg6ANhBLp9s9MEZwC0YDJ6%2FqT0b%2BTdaF9BQHG7pFP5PVVlzNnIxmQworuOY%2BrpWFVzN5wPwQbl&X-Amz-Signature=b6bdc7af2460d09dd7e274f424df8a38caa4ca715d83c18a13609a30934012f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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