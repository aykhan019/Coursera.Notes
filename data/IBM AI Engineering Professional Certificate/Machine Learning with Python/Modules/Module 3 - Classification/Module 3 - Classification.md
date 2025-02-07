

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMPGOZVF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDCrDfl6xcui6IxHmghWKttp2oewLAbOhNgN1zMAG90lAIhAMVzVw4uYGqET2HeUtpNiq5XG9NXopG4UzbQfRDuzI7qKv8DCGkQABoMNjM3NDIzMTgzODA1IgxDMVo2jdeWuuU921Aq3ANYEoQ8rDTFzhgUWv%2FwjINuEiPkHpCM%2F5usG7PT16qYtu9oXedlSXrLQqi7PIScedGFSCsO17oip1WZO1MVIAfj2ocGqL8A5faAGRONaATuHAtjlH%2FBLxW3B8ilfOthhuqrZT21VGFgKSBkeF6YuegFvgrDLyAcQKfhtVDXue9Q1MEEjLHgQGlqwALWgZXcMoNa0Xp5XTwwG88rGkTolcF5wgGIObm%2Fk4cNv4Jj7c0%2BYN4EyY36xFbg2gKDM6R3p1Dt7KRoQ3wH6XD0A%2B23c2PsYEY238%2FBBwmUbHrClF0su%2FexZhT%2FTC3%2F%2BkaeMCqHYiaoLr%2FfC9B6%2BHjpSo98jmNIN5MYEOs7T3ITcUJHuX7gIPfwKihiMcGIKIPQhT4lgJVENgqsswX4%2FtjZBnThkIVWolwFjvOk8yGZkQhxB6jDp4xCd%2B2NVEu2UDKiq%2BJR5NtIsAxwOmZy4A%2B6XuMvIKFw7M8MxXlLM3kpWESOz2Iwlml66DuGx%2FG2FwRH8aCByf92%2B3p4ohT7V5R8GUfoG63VEjEE0m1JmA3tKmcumUeJhSd0Yzz8P%2FgIlZezVYGpFznFxZGGdx%2FuGCx83jcVPz6c3Lyy%2FbCqNQA%2BOp5p%2FS857vMabRbHxrr5fIuYfjCampW9BjqkAZDddVsZEqRg44ogAKdNCg87kE5fsOfkSFFXjjQmXnv4LGRzsNkSK43Wpq4Cx5o2kVIByggYEhLqP05Y31VZqdE%2Fim0kMBTLhJgE5cyk8uWyBhLURywkj1M2b%2Fnp73qRINRxZYBDCQ%2BhO4JRz%2B4c9VP8Scy3Kx%2Ba5xfUmqddH%2BV0%2Bd%2FUO4a0qJzEH3RKrUKk700UztyQQV6V8Mbg9U2%2Fp2zcdhnh&X-Amz-Signature=1de52d9abba1e434fcee30ac2ab9229634a31d7b0a1d645bf7261bdcb4f661f4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMPGOZVF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDCrDfl6xcui6IxHmghWKttp2oewLAbOhNgN1zMAG90lAIhAMVzVw4uYGqET2HeUtpNiq5XG9NXopG4UzbQfRDuzI7qKv8DCGkQABoMNjM3NDIzMTgzODA1IgxDMVo2jdeWuuU921Aq3ANYEoQ8rDTFzhgUWv%2FwjINuEiPkHpCM%2F5usG7PT16qYtu9oXedlSXrLQqi7PIScedGFSCsO17oip1WZO1MVIAfj2ocGqL8A5faAGRONaATuHAtjlH%2FBLxW3B8ilfOthhuqrZT21VGFgKSBkeF6YuegFvgrDLyAcQKfhtVDXue9Q1MEEjLHgQGlqwALWgZXcMoNa0Xp5XTwwG88rGkTolcF5wgGIObm%2Fk4cNv4Jj7c0%2BYN4EyY36xFbg2gKDM6R3p1Dt7KRoQ3wH6XD0A%2B23c2PsYEY238%2FBBwmUbHrClF0su%2FexZhT%2FTC3%2F%2BkaeMCqHYiaoLr%2FfC9B6%2BHjpSo98jmNIN5MYEOs7T3ITcUJHuX7gIPfwKihiMcGIKIPQhT4lgJVENgqsswX4%2FtjZBnThkIVWolwFjvOk8yGZkQhxB6jDp4xCd%2B2NVEu2UDKiq%2BJR5NtIsAxwOmZy4A%2B6XuMvIKFw7M8MxXlLM3kpWESOz2Iwlml66DuGx%2FG2FwRH8aCByf92%2B3p4ohT7V5R8GUfoG63VEjEE0m1JmA3tKmcumUeJhSd0Yzz8P%2FgIlZezVYGpFznFxZGGdx%2FuGCx83jcVPz6c3Lyy%2FbCqNQA%2BOp5p%2FS857vMabRbHxrr5fIuYfjCampW9BjqkAZDddVsZEqRg44ogAKdNCg87kE5fsOfkSFFXjjQmXnv4LGRzsNkSK43Wpq4Cx5o2kVIByggYEhLqP05Y31VZqdE%2Fim0kMBTLhJgE5cyk8uWyBhLURywkj1M2b%2Fnp73qRINRxZYBDCQ%2BhO4JRz%2B4c9VP8Scy3Kx%2Ba5xfUmqddH%2BV0%2Bd%2FUO4a0qJzEH3RKrUKk700UztyQQV6V8Mbg9U2%2Fp2zcdhnh&X-Amz-Signature=d9b473d39d453366695f86b0ec85988585d280a29a497ea73b10d74c914d49cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMPGOZVF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDCrDfl6xcui6IxHmghWKttp2oewLAbOhNgN1zMAG90lAIhAMVzVw4uYGqET2HeUtpNiq5XG9NXopG4UzbQfRDuzI7qKv8DCGkQABoMNjM3NDIzMTgzODA1IgxDMVo2jdeWuuU921Aq3ANYEoQ8rDTFzhgUWv%2FwjINuEiPkHpCM%2F5usG7PT16qYtu9oXedlSXrLQqi7PIScedGFSCsO17oip1WZO1MVIAfj2ocGqL8A5faAGRONaATuHAtjlH%2FBLxW3B8ilfOthhuqrZT21VGFgKSBkeF6YuegFvgrDLyAcQKfhtVDXue9Q1MEEjLHgQGlqwALWgZXcMoNa0Xp5XTwwG88rGkTolcF5wgGIObm%2Fk4cNv4Jj7c0%2BYN4EyY36xFbg2gKDM6R3p1Dt7KRoQ3wH6XD0A%2B23c2PsYEY238%2FBBwmUbHrClF0su%2FexZhT%2FTC3%2F%2BkaeMCqHYiaoLr%2FfC9B6%2BHjpSo98jmNIN5MYEOs7T3ITcUJHuX7gIPfwKihiMcGIKIPQhT4lgJVENgqsswX4%2FtjZBnThkIVWolwFjvOk8yGZkQhxB6jDp4xCd%2B2NVEu2UDKiq%2BJR5NtIsAxwOmZy4A%2B6XuMvIKFw7M8MxXlLM3kpWESOz2Iwlml66DuGx%2FG2FwRH8aCByf92%2B3p4ohT7V5R8GUfoG63VEjEE0m1JmA3tKmcumUeJhSd0Yzz8P%2FgIlZezVYGpFznFxZGGdx%2FuGCx83jcVPz6c3Lyy%2FbCqNQA%2BOp5p%2FS857vMabRbHxrr5fIuYfjCampW9BjqkAZDddVsZEqRg44ogAKdNCg87kE5fsOfkSFFXjjQmXnv4LGRzsNkSK43Wpq4Cx5o2kVIByggYEhLqP05Y31VZqdE%2Fim0kMBTLhJgE5cyk8uWyBhLURywkj1M2b%2Fnp73qRINRxZYBDCQ%2BhO4JRz%2B4c9VP8Scy3Kx%2Ba5xfUmqddH%2BV0%2Bd%2FUO4a0qJzEH3RKrUKk700UztyQQV6V8Mbg9U2%2Fp2zcdhnh&X-Amz-Signature=e64e40908aaf0ba856172bb2ffefdeec738e0e5ac5a975b4b017f7a059a80c4b&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ7ZGOM5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHNqg6ZMjmf%2FZFOHWz%2Flf47cB3BV15l9K%2FdEO3nMZhTWAiEA8Zecy4%2BuqOYx83iSbx7wnSpm3KpccGTzJT5YAu8QAxIq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPESyHmNgyZXbOgudCrcA%2BD%2BfjB8CUT2IczJNebULzK1HQRWc74MDRC2VYGUP%2BI%2ByjYp1KEzTkxs%2F3gfRHUjnSz8HJ%2FI8PT69pme6Y8LxYPVgmDu4JEuRj3x1DV2mwaD9pCQlZERnsoDEeh4CjuAuxmL7YOGwO8etjE2TqVwztMboh0iIP8%2F8pN7CthtnXov0NvefPANno73CvoYr%2F4HgR7sj2YrizlLTGUQyzLRbxtyoY6CwaZlzY7ie%2FGh8%2BpNb9gwe%2FdbsSkiSB68Guc3tfZxkKVuHuSEW7vwnD19Oa41LkcHN9p%2BaWFjdGlpNUNWdzqnE2naVwUDUmT6abCdG4wsEAaRbif%2F73b3KBmxD9Ev4hPfWB07JVhHDKhEfzJ887gsv3sOrQHPYM%2FdaGu8KNo4cgLI2%2B8j9grX6c7aeVXf%2FY4QQF1I2x9TGJLR6woVBKVtYlxX5lDLcoZVd5262ylzh%2Fwm2kKr6OH3ro1Iy6Ye1cj8LkXBGRhb24cTYujXe%2FTChRCw7JPJiiYs%2BmQhJQhCfGmtpDD8jAVKQNRTW06bhLyxew7BkF4m%2BXQGgKm9HHo3DlxCEmpsiZMNY8BTkdI50PQwOnKJt6wZNrc6E81x2SwVl%2FL62mpV4Pz%2F%2Brp5hfbC%2FRaQW4fVhm6wML6alb0GOqUBIIsUbI5AF0%2BV6x1yPD%2B34wm0XVpHHiq%2BlvamB6SEuC%2Fxst3TCToS5WZwOPAMElbQ3VRlY2O3pTbo6TWwVlQ6Er%2FMeFWxXc0mdIWVLrZjD6kY8bcJjBLC%2BnYPvMmj7LByQ07gzg%2BiOdDWIwjIxmzqFQedb%2BXmL0QrHroRdSFYc%2BJw7TiUjFyI4c%2BCPw%2B1sInEjGTDfhxDX5iehFU378C7lw%2BjuMDX&X-Amz-Signature=a31a0eae27eb5883c1639179650be3b0029e5e59fc5fc587c3a1a23b73c292b8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ7ZGOM5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIHNqg6ZMjmf%2FZFOHWz%2Flf47cB3BV15l9K%2FdEO3nMZhTWAiEA8Zecy4%2BuqOYx83iSbx7wnSpm3KpccGTzJT5YAu8QAxIq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDPESyHmNgyZXbOgudCrcA%2BD%2BfjB8CUT2IczJNebULzK1HQRWc74MDRC2VYGUP%2BI%2ByjYp1KEzTkxs%2F3gfRHUjnSz8HJ%2FI8PT69pme6Y8LxYPVgmDu4JEuRj3x1DV2mwaD9pCQlZERnsoDEeh4CjuAuxmL7YOGwO8etjE2TqVwztMboh0iIP8%2F8pN7CthtnXov0NvefPANno73CvoYr%2F4HgR7sj2YrizlLTGUQyzLRbxtyoY6CwaZlzY7ie%2FGh8%2BpNb9gwe%2FdbsSkiSB68Guc3tfZxkKVuHuSEW7vwnD19Oa41LkcHN9p%2BaWFjdGlpNUNWdzqnE2naVwUDUmT6abCdG4wsEAaRbif%2F73b3KBmxD9Ev4hPfWB07JVhHDKhEfzJ887gsv3sOrQHPYM%2FdaGu8KNo4cgLI2%2B8j9grX6c7aeVXf%2FY4QQF1I2x9TGJLR6woVBKVtYlxX5lDLcoZVd5262ylzh%2Fwm2kKr6OH3ro1Iy6Ye1cj8LkXBGRhb24cTYujXe%2FTChRCw7JPJiiYs%2BmQhJQhCfGmtpDD8jAVKQNRTW06bhLyxew7BkF4m%2BXQGgKm9HHo3DlxCEmpsiZMNY8BTkdI50PQwOnKJt6wZNrc6E81x2SwVl%2FL62mpV4Pz%2F%2Brp5hfbC%2FRaQW4fVhm6wML6alb0GOqUBIIsUbI5AF0%2BV6x1yPD%2B34wm0XVpHHiq%2BlvamB6SEuC%2Fxst3TCToS5WZwOPAMElbQ3VRlY2O3pTbo6TWwVlQ6Er%2FMeFWxXc0mdIWVLrZjD6kY8bcJjBLC%2BnYPvMmj7LByQ07gzg%2BiOdDWIwjIxmzqFQedb%2BXmL0QrHroRdSFYc%2BJw7TiUjFyI4c%2BCPw%2B1sInEjGTDfhxDX5iehFU378C7lw%2BjuMDX&X-Amz-Signature=26c2a807231ce4a1873e9932b8633ff3350230e006e81ab9420ea668f4b3bbaa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMPGOZVF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T010940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDCrDfl6xcui6IxHmghWKttp2oewLAbOhNgN1zMAG90lAIhAMVzVw4uYGqET2HeUtpNiq5XG9NXopG4UzbQfRDuzI7qKv8DCGkQABoMNjM3NDIzMTgzODA1IgxDMVo2jdeWuuU921Aq3ANYEoQ8rDTFzhgUWv%2FwjINuEiPkHpCM%2F5usG7PT16qYtu9oXedlSXrLQqi7PIScedGFSCsO17oip1WZO1MVIAfj2ocGqL8A5faAGRONaATuHAtjlH%2FBLxW3B8ilfOthhuqrZT21VGFgKSBkeF6YuegFvgrDLyAcQKfhtVDXue9Q1MEEjLHgQGlqwALWgZXcMoNa0Xp5XTwwG88rGkTolcF5wgGIObm%2Fk4cNv4Jj7c0%2BYN4EyY36xFbg2gKDM6R3p1Dt7KRoQ3wH6XD0A%2B23c2PsYEY238%2FBBwmUbHrClF0su%2FexZhT%2FTC3%2F%2BkaeMCqHYiaoLr%2FfC9B6%2BHjpSo98jmNIN5MYEOs7T3ITcUJHuX7gIPfwKihiMcGIKIPQhT4lgJVENgqsswX4%2FtjZBnThkIVWolwFjvOk8yGZkQhxB6jDp4xCd%2B2NVEu2UDKiq%2BJR5NtIsAxwOmZy4A%2B6XuMvIKFw7M8MxXlLM3kpWESOz2Iwlml66DuGx%2FG2FwRH8aCByf92%2B3p4ohT7V5R8GUfoG63VEjEE0m1JmA3tKmcumUeJhSd0Yzz8P%2FgIlZezVYGpFznFxZGGdx%2FuGCx83jcVPz6c3Lyy%2FbCqNQA%2BOp5p%2FS857vMabRbHxrr5fIuYfjCampW9BjqkAZDddVsZEqRg44ogAKdNCg87kE5fsOfkSFFXjjQmXnv4LGRzsNkSK43Wpq4Cx5o2kVIByggYEhLqP05Y31VZqdE%2Fim0kMBTLhJgE5cyk8uWyBhLURywkj1M2b%2Fnp73qRINRxZYBDCQ%2BhO4JRz%2B4c9VP8Scy3Kx%2Ba5xfUmqddH%2BV0%2Bd%2FUO4a0qJzEH3RKrUKk700UztyQQV6V8Mbg9U2%2Fp2zcdhnh&X-Amz-Signature=56f4100f138c9e5daf85d332b57c9b867125ae1ca06fe17e0c6aa60593b77265&X-Amz-SignedHeaders=host&x-id=GetObject)
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