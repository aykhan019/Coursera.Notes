

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TNVKDW6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC83vVUh0YaF6RzZrUN3%2FZpb6ndr4UVCOe5OBNP7Nf5ewIhALpLEbafpCVhHXTeJj8zmmjbeaZoLr8vh8SfZr7dQeyLKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2F4EaUwmitiigPLVYq3ANStJ7%2BH1SjdIpIx9%2F%2BglcOMHwn52Yn1n7mWUmwAfBZTNbU5Qs%2FaqTrPKlXNMsWl2z6LyH0n8yV%2BIKHqJrGbtiurCXPVfWR7XjawVzO4mngAPiUnnM74FZsFEE%2B8blB7ddeQfslUiRCGWQHAnfabewUBgW1hL6N0qWsiXZWBTqop4HFBk93cbiTPyHFbEKIUozki8Bf64t9DAHuvyKPUlIjwF9ba7eX1yeh00SH3MiAaP%2F2ECbArj2jhDItlyRmkra9%2FkGDqjmltVeK8YT5RuLogrMfSDg2y42Zjur7nZuazsbud8nztg9pbP0LHCuFjS8Hnvf7LeljrlAwCf%2BAvgZwZY1OZlq5jIBlJLBsEmIAcII9fj%2FezrGF7jzwUPxDRkd0ixlrBiR2UWA%2BiZpskjvwpMGiMeLNOhF4JlI56lmRf7pYxE43REPdAeDYifVGIMPldVHHAZqLzmtw19b1DMtmYTvpTJt3roO6RFCgHk0JTE2iCwFyyHf3GbNKMEk1VIfOcOUDO1CUKwxBZuuz7ahAwzbWWX%2B7%2FU%2BUcjTZc4X3qjFwoRyRKV4Auenq1HFnD5YQxIvfAa4z8ZaQbTE7mPlfzGMnt80DAeDfzlgEZ2kZPbkQgu8PSHoGqa%2FiNDDTpPe8BjqkAbdwIHvluJ0iOj0Q6C2H3SBH8gKGVk%2FPr7kjOu6b2RThmfvB2183xAw81yIyGP4sME%2FSrOaeI1Q5WrxdUB%2FkSNFjb9E2%2FyJOXgvi2ZN3fsVOvz1uq0g5QNExGPr3gR0HFOFhfqYtjEVC3X022jRL0%2FK0uKASLyCl1lN8w05L321ewHFOJs6f%2FckY7SQOO74puCd0lOHNVIkqLduOVoxlFnGnROKQ&X-Amz-Signature=07716b1ec307c29d5608f35675db66ac62cdddbefacf9cbd2fa0817d73a76bb2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TNVKDW6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC83vVUh0YaF6RzZrUN3%2FZpb6ndr4UVCOe5OBNP7Nf5ewIhALpLEbafpCVhHXTeJj8zmmjbeaZoLr8vh8SfZr7dQeyLKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2F4EaUwmitiigPLVYq3ANStJ7%2BH1SjdIpIx9%2F%2BglcOMHwn52Yn1n7mWUmwAfBZTNbU5Qs%2FaqTrPKlXNMsWl2z6LyH0n8yV%2BIKHqJrGbtiurCXPVfWR7XjawVzO4mngAPiUnnM74FZsFEE%2B8blB7ddeQfslUiRCGWQHAnfabewUBgW1hL6N0qWsiXZWBTqop4HFBk93cbiTPyHFbEKIUozki8Bf64t9DAHuvyKPUlIjwF9ba7eX1yeh00SH3MiAaP%2F2ECbArj2jhDItlyRmkra9%2FkGDqjmltVeK8YT5RuLogrMfSDg2y42Zjur7nZuazsbud8nztg9pbP0LHCuFjS8Hnvf7LeljrlAwCf%2BAvgZwZY1OZlq5jIBlJLBsEmIAcII9fj%2FezrGF7jzwUPxDRkd0ixlrBiR2UWA%2BiZpskjvwpMGiMeLNOhF4JlI56lmRf7pYxE43REPdAeDYifVGIMPldVHHAZqLzmtw19b1DMtmYTvpTJt3roO6RFCgHk0JTE2iCwFyyHf3GbNKMEk1VIfOcOUDO1CUKwxBZuuz7ahAwzbWWX%2B7%2FU%2BUcjTZc4X3qjFwoRyRKV4Auenq1HFnD5YQxIvfAa4z8ZaQbTE7mPlfzGMnt80DAeDfzlgEZ2kZPbkQgu8PSHoGqa%2FiNDDTpPe8BjqkAbdwIHvluJ0iOj0Q6C2H3SBH8gKGVk%2FPr7kjOu6b2RThmfvB2183xAw81yIyGP4sME%2FSrOaeI1Q5WrxdUB%2FkSNFjb9E2%2FyJOXgvi2ZN3fsVOvz1uq0g5QNExGPr3gR0HFOFhfqYtjEVC3X022jRL0%2FK0uKASLyCl1lN8w05L321ewHFOJs6f%2FckY7SQOO74puCd0lOHNVIkqLduOVoxlFnGnROKQ&X-Amz-Signature=08bc4e09f83f2589996a8b16b91bb95e08a4cf7c785b161fd4cff4ab4432714e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TNVKDW6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC83vVUh0YaF6RzZrUN3%2FZpb6ndr4UVCOe5OBNP7Nf5ewIhALpLEbafpCVhHXTeJj8zmmjbeaZoLr8vh8SfZr7dQeyLKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2F4EaUwmitiigPLVYq3ANStJ7%2BH1SjdIpIx9%2F%2BglcOMHwn52Yn1n7mWUmwAfBZTNbU5Qs%2FaqTrPKlXNMsWl2z6LyH0n8yV%2BIKHqJrGbtiurCXPVfWR7XjawVzO4mngAPiUnnM74FZsFEE%2B8blB7ddeQfslUiRCGWQHAnfabewUBgW1hL6N0qWsiXZWBTqop4HFBk93cbiTPyHFbEKIUozki8Bf64t9DAHuvyKPUlIjwF9ba7eX1yeh00SH3MiAaP%2F2ECbArj2jhDItlyRmkra9%2FkGDqjmltVeK8YT5RuLogrMfSDg2y42Zjur7nZuazsbud8nztg9pbP0LHCuFjS8Hnvf7LeljrlAwCf%2BAvgZwZY1OZlq5jIBlJLBsEmIAcII9fj%2FezrGF7jzwUPxDRkd0ixlrBiR2UWA%2BiZpskjvwpMGiMeLNOhF4JlI56lmRf7pYxE43REPdAeDYifVGIMPldVHHAZqLzmtw19b1DMtmYTvpTJt3roO6RFCgHk0JTE2iCwFyyHf3GbNKMEk1VIfOcOUDO1CUKwxBZuuz7ahAwzbWWX%2B7%2FU%2BUcjTZc4X3qjFwoRyRKV4Auenq1HFnD5YQxIvfAa4z8ZaQbTE7mPlfzGMnt80DAeDfzlgEZ2kZPbkQgu8PSHoGqa%2FiNDDTpPe8BjqkAbdwIHvluJ0iOj0Q6C2H3SBH8gKGVk%2FPr7kjOu6b2RThmfvB2183xAw81yIyGP4sME%2FSrOaeI1Q5WrxdUB%2FkSNFjb9E2%2FyJOXgvi2ZN3fsVOvz1uq0g5QNExGPr3gR0HFOFhfqYtjEVC3X022jRL0%2FK0uKASLyCl1lN8w05L321ewHFOJs6f%2FckY7SQOO74puCd0lOHNVIkqLduOVoxlFnGnROKQ&X-Amz-Signature=c1e03776f878950339b746ed5e785d65c9aae910676b1a720e9774854387050c&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SL4BNKW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD90EHoEYvitjo6WJ%2Bk3gtwptZAvsltRe0ZT%2FOq2vDRkgIgPbENg6L2oDzAepAqjFPApPvxB4YrV487nvTMBNRaHWgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB66XM8SvOEBVPYqsCrcA%2BC9v%2BNFXhKUKzyaBRooMqHWR0h9U%2FvduASiwB%2Fq1W4wLOEuKhzAD%2BPIFH4E4tXKiAsH%2FsVcblai%2BQ6t3belFWCU9czq4fzoiS4RgNEflSm1SzctAVyW%2ByOOK8UXWMDS6DvNvTwJ09ghRfuG17yw%2FcLJ8NCujf89AhzVNgDvgNIl2uG8zhVQBC1VTsSVp2UfCTDSEz9j3CusIWoE5goc8p2%2FB0ntrTgtpN9Z9CXyCk3WTXQCobRNjQk9Y9%2FTKkymcjXHF8McmxzXUxGEgYwc4%2B9TJW61MIUQawtXvntgDooayef%2BqsPSlXWvKayH3omdZda%2BTI%2BjS604SSBmR0%2BWnfeRvARwzY%2BNY%2BB2ZE5QDu9GaSNxrAVhKE663D3%2Fe%2BgO1velCYYEy8nVYed2qm%2BzXueAZSPhq2jU8EdfAQL8JnVQKiG17et7MAXfkx4z1zhazV7lI2Um6KXnEDHIZES2jKNLVwRBfdaHwOUOuiiQFOHlAQKSYOenlbuLiD7OU6zc744RqVy0jj5gFSn6DEtpj8r90%2BY8aWxf6I9udu%2Fw5XOKzjELFrEOLADxVCbad4%2BHPgNzr7NAt%2B%2BVwZR1sPt6uXTEG1S9PIyzrvbCBFRa2VS%2Fu4aMIfBvUudkoAl9MJmk97wGOqUBxkPb%2BB34DsLgPZvgDA44hbevA3Cas3kPhlWj%2BBvobG1XMq%2B6obsLPB92s80bvgMlwQMe5VlJMBepeWfJ%2F8dtych7ArwJSLqemruw65ZV0fzxTgN6XGi%2FgFmQE16CI95GSP1QqVJLe32VtLGkdramf43dM6pCxl9%2F4ZD03DdO%2FZo2yB4rxi1HbjkqM8GvsqB%2F00ZYUdfaDQMoRgcDohAjhqTGGNWp&X-Amz-Signature=1ef6ebf0ea47ab8bf4c4ccdaf2a51c02e0a5b65b914032101a4d8ed9db6dcd6a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SL4BNKW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD90EHoEYvitjo6WJ%2Bk3gtwptZAvsltRe0ZT%2FOq2vDRkgIgPbENg6L2oDzAepAqjFPApPvxB4YrV487nvTMBNRaHWgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB66XM8SvOEBVPYqsCrcA%2BC9v%2BNFXhKUKzyaBRooMqHWR0h9U%2FvduASiwB%2Fq1W4wLOEuKhzAD%2BPIFH4E4tXKiAsH%2FsVcblai%2BQ6t3belFWCU9czq4fzoiS4RgNEflSm1SzctAVyW%2ByOOK8UXWMDS6DvNvTwJ09ghRfuG17yw%2FcLJ8NCujf89AhzVNgDvgNIl2uG8zhVQBC1VTsSVp2UfCTDSEz9j3CusIWoE5goc8p2%2FB0ntrTgtpN9Z9CXyCk3WTXQCobRNjQk9Y9%2FTKkymcjXHF8McmxzXUxGEgYwc4%2B9TJW61MIUQawtXvntgDooayef%2BqsPSlXWvKayH3omdZda%2BTI%2BjS604SSBmR0%2BWnfeRvARwzY%2BNY%2BB2ZE5QDu9GaSNxrAVhKE663D3%2Fe%2BgO1velCYYEy8nVYed2qm%2BzXueAZSPhq2jU8EdfAQL8JnVQKiG17et7MAXfkx4z1zhazV7lI2Um6KXnEDHIZES2jKNLVwRBfdaHwOUOuiiQFOHlAQKSYOenlbuLiD7OU6zc744RqVy0jj5gFSn6DEtpj8r90%2BY8aWxf6I9udu%2Fw5XOKzjELFrEOLADxVCbad4%2BHPgNzr7NAt%2B%2BVwZR1sPt6uXTEG1S9PIyzrvbCBFRa2VS%2Fu4aMIfBvUudkoAl9MJmk97wGOqUBxkPb%2BB34DsLgPZvgDA44hbevA3Cas3kPhlWj%2BBvobG1XMq%2B6obsLPB92s80bvgMlwQMe5VlJMBepeWfJ%2F8dtych7ArwJSLqemruw65ZV0fzxTgN6XGi%2FgFmQE16CI95GSP1QqVJLe32VtLGkdramf43dM6pCxl9%2F4ZD03DdO%2FZo2yB4rxi1HbjkqM8GvsqB%2F00ZYUdfaDQMoRgcDohAjhqTGGNWp&X-Amz-Signature=c1f3871e2e3a7aac1f2f7c353a14a1f2d1cd1d8ce728073f286e5b9bfe8af919&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TNVKDW6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC83vVUh0YaF6RzZrUN3%2FZpb6ndr4UVCOe5OBNP7Nf5ewIhALpLEbafpCVhHXTeJj8zmmjbeaZoLr8vh8SfZr7dQeyLKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2F4EaUwmitiigPLVYq3ANStJ7%2BH1SjdIpIx9%2F%2BglcOMHwn52Yn1n7mWUmwAfBZTNbU5Qs%2FaqTrPKlXNMsWl2z6LyH0n8yV%2BIKHqJrGbtiurCXPVfWR7XjawVzO4mngAPiUnnM74FZsFEE%2B8blB7ddeQfslUiRCGWQHAnfabewUBgW1hL6N0qWsiXZWBTqop4HFBk93cbiTPyHFbEKIUozki8Bf64t9DAHuvyKPUlIjwF9ba7eX1yeh00SH3MiAaP%2F2ECbArj2jhDItlyRmkra9%2FkGDqjmltVeK8YT5RuLogrMfSDg2y42Zjur7nZuazsbud8nztg9pbP0LHCuFjS8Hnvf7LeljrlAwCf%2BAvgZwZY1OZlq5jIBlJLBsEmIAcII9fj%2FezrGF7jzwUPxDRkd0ixlrBiR2UWA%2BiZpskjvwpMGiMeLNOhF4JlI56lmRf7pYxE43REPdAeDYifVGIMPldVHHAZqLzmtw19b1DMtmYTvpTJt3roO6RFCgHk0JTE2iCwFyyHf3GbNKMEk1VIfOcOUDO1CUKwxBZuuz7ahAwzbWWX%2B7%2FU%2BUcjTZc4X3qjFwoRyRKV4Auenq1HFnD5YQxIvfAa4z8ZaQbTE7mPlfzGMnt80DAeDfzlgEZ2kZPbkQgu8PSHoGqa%2FiNDDTpPe8BjqkAbdwIHvluJ0iOj0Q6C2H3SBH8gKGVk%2FPr7kjOu6b2RThmfvB2183xAw81yIyGP4sME%2FSrOaeI1Q5WrxdUB%2FkSNFjb9E2%2FyJOXgvi2ZN3fsVOvz1uq0g5QNExGPr3gR0HFOFhfqYtjEVC3X022jRL0%2FK0uKASLyCl1lN8w05L321ewHFOJs6f%2FckY7SQOO74puCd0lOHNVIkqLduOVoxlFnGnROKQ&X-Amz-Signature=3b9674805d0ae5df41fd528e29eb5ce855e85fec6e2fc0cd2db28dd37e7d14cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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