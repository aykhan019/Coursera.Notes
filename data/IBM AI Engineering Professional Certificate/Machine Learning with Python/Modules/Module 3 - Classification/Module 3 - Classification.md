

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO26MLGY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQDH%2BZmd5CcwB%2FOetMOCeAMkBKk7WFvyblRgx%2BAKMuNSJQIgPqPBTYKSLhpdw72BUg9J%2BATP9TvhW0B9H%2BbUTkeQviYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN14WXxVWRuLFkbhxircA5bZo50DnERMfnqVmNKj49CuwyY3I52ZeS3MM%2FTX9gap%2BpwXdmjyyameafEmkmt0nqh84nXriso2JbicaKJYU1l6hq6J0m%2F0llJlXXGhRQhTxt0t7JJcPK8N69JlvSslSoWOBc93cEWiImAo9ZR%2FYEvsKjmSu2UgG%2F4Moq0iWR5oV0ouYBnwfWNbNnMQ6LG1E7WQE11fBJiXNQeW4zDNnAuUZbWAae%2F4PdqSiBUIyogqDczRD0j15%2BPOUTbgtkHa5aIYkrMZHmhHzg3ifMI3M7gQ59W17YDMvpNWVZeTOT1sMWLK4YxJbZ35CJ6CJdCERu5aN3cci2iK5PlpVFHVJPSCKPIphEk%2F%2BB4faO8a7%2FT0Kv3qWYId55fPx7att6VQaVlTNEqkgN6YGpTgmlm3%2B7v9P52OoGkmkpRbCJZb%2FX2oo3F8T%2FIcPpnIUmpriV9GLo5o5Q3SJ6XN3Gd0Y6rB0Coq11JglIbtW6i7dfP%2BgpYVw5JtUO7scHd%2BFze0LjQZ3ed2GOHFcZiXzRIzOPgv2D%2BKVPoqdDxDNNEgiJHa0njwFT20QiXv%2Ff4TaUnxaoBScjKD2U1RCtf5wOO0xbTG2oVGJwgWIhLs%2BmhcSDcdRmPTXQ4wgwQfhuOReHL4MKbRk70GOqUBmYbUHCGGu7%2BlRc9Sq5lzDZ%2BTTCfrYbSETMtND1V11hu2RvJ0s3lPZsYJ2FkqLG2k1e4pvbIfkQVGBHyI%2B89pDNHNrvEarD%2Bx5Y2b%2BolDOhD9XtMPpSG3Wntf4GhJ4u1C8z3yLjL77k7Wj4djKkl6c5xzavZBskX%2BjJuv9njG4yEeahDl%2BzlO%2BFrUiZZysy7z%2B3%2BsGjJgrNzTFEpLlKqEnzdMJP7S&X-Amz-Signature=4e79651c4dc5bc97cfd6eb5dac47e169c9984b10c3060d689da3cd60ea801e46&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO26MLGY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQDH%2BZmd5CcwB%2FOetMOCeAMkBKk7WFvyblRgx%2BAKMuNSJQIgPqPBTYKSLhpdw72BUg9J%2BATP9TvhW0B9H%2BbUTkeQviYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN14WXxVWRuLFkbhxircA5bZo50DnERMfnqVmNKj49CuwyY3I52ZeS3MM%2FTX9gap%2BpwXdmjyyameafEmkmt0nqh84nXriso2JbicaKJYU1l6hq6J0m%2F0llJlXXGhRQhTxt0t7JJcPK8N69JlvSslSoWOBc93cEWiImAo9ZR%2FYEvsKjmSu2UgG%2F4Moq0iWR5oV0ouYBnwfWNbNnMQ6LG1E7WQE11fBJiXNQeW4zDNnAuUZbWAae%2F4PdqSiBUIyogqDczRD0j15%2BPOUTbgtkHa5aIYkrMZHmhHzg3ifMI3M7gQ59W17YDMvpNWVZeTOT1sMWLK4YxJbZ35CJ6CJdCERu5aN3cci2iK5PlpVFHVJPSCKPIphEk%2F%2BB4faO8a7%2FT0Kv3qWYId55fPx7att6VQaVlTNEqkgN6YGpTgmlm3%2B7v9P52OoGkmkpRbCJZb%2FX2oo3F8T%2FIcPpnIUmpriV9GLo5o5Q3SJ6XN3Gd0Y6rB0Coq11JglIbtW6i7dfP%2BgpYVw5JtUO7scHd%2BFze0LjQZ3ed2GOHFcZiXzRIzOPgv2D%2BKVPoqdDxDNNEgiJHa0njwFT20QiXv%2Ff4TaUnxaoBScjKD2U1RCtf5wOO0xbTG2oVGJwgWIhLs%2BmhcSDcdRmPTXQ4wgwQfhuOReHL4MKbRk70GOqUBmYbUHCGGu7%2BlRc9Sq5lzDZ%2BTTCfrYbSETMtND1V11hu2RvJ0s3lPZsYJ2FkqLG2k1e4pvbIfkQVGBHyI%2B89pDNHNrvEarD%2Bx5Y2b%2BolDOhD9XtMPpSG3Wntf4GhJ4u1C8z3yLjL77k7Wj4djKkl6c5xzavZBskX%2BjJuv9njG4yEeahDl%2BzlO%2BFrUiZZysy7z%2B3%2BsGjJgrNzTFEpLlKqEnzdMJP7S&X-Amz-Signature=a522a1d4bdddfbe790eaa7a31df040555e783657e121b396344d9827c1b50335&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO26MLGY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQDH%2BZmd5CcwB%2FOetMOCeAMkBKk7WFvyblRgx%2BAKMuNSJQIgPqPBTYKSLhpdw72BUg9J%2BATP9TvhW0B9H%2BbUTkeQviYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN14WXxVWRuLFkbhxircA5bZo50DnERMfnqVmNKj49CuwyY3I52ZeS3MM%2FTX9gap%2BpwXdmjyyameafEmkmt0nqh84nXriso2JbicaKJYU1l6hq6J0m%2F0llJlXXGhRQhTxt0t7JJcPK8N69JlvSslSoWOBc93cEWiImAo9ZR%2FYEvsKjmSu2UgG%2F4Moq0iWR5oV0ouYBnwfWNbNnMQ6LG1E7WQE11fBJiXNQeW4zDNnAuUZbWAae%2F4PdqSiBUIyogqDczRD0j15%2BPOUTbgtkHa5aIYkrMZHmhHzg3ifMI3M7gQ59W17YDMvpNWVZeTOT1sMWLK4YxJbZ35CJ6CJdCERu5aN3cci2iK5PlpVFHVJPSCKPIphEk%2F%2BB4faO8a7%2FT0Kv3qWYId55fPx7att6VQaVlTNEqkgN6YGpTgmlm3%2B7v9P52OoGkmkpRbCJZb%2FX2oo3F8T%2FIcPpnIUmpriV9GLo5o5Q3SJ6XN3Gd0Y6rB0Coq11JglIbtW6i7dfP%2BgpYVw5JtUO7scHd%2BFze0LjQZ3ed2GOHFcZiXzRIzOPgv2D%2BKVPoqdDxDNNEgiJHa0njwFT20QiXv%2Ff4TaUnxaoBScjKD2U1RCtf5wOO0xbTG2oVGJwgWIhLs%2BmhcSDcdRmPTXQ4wgwQfhuOReHL4MKbRk70GOqUBmYbUHCGGu7%2BlRc9Sq5lzDZ%2BTTCfrYbSETMtND1V11hu2RvJ0s3lPZsYJ2FkqLG2k1e4pvbIfkQVGBHyI%2B89pDNHNrvEarD%2Bx5Y2b%2BolDOhD9XtMPpSG3Wntf4GhJ4u1C8z3yLjL77k7Wj4djKkl6c5xzavZBskX%2BjJuv9njG4yEeahDl%2BzlO%2BFrUiZZysy7z%2B3%2BsGjJgrNzTFEpLlKqEnzdMJP7S&X-Amz-Signature=88f4c72cfd83bb368a94fddf8e0fdb6220d058acc2695b1746230b7848113ffc&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQN3GIDA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQC8XdzjZryW10TUSz2ACp8If24l6%2BZG4d8RfB7HFNKF%2BAIhAP7%2BKb3idZ6STolFjsgWy1Kb69A%2Fztau5HDOvKEo3fS7Kv8DCGIQABoMNjM3NDIzMTgzODA1Igyzhi12p5dXLZ0cj3gq3AP9GG3LxV2TR%2B6zFLBps5lPwrAh17IJB54FzrRsL5nhS0S6pYIgQookeSCorNjbdmazqWAbEUzUjgCLsN5tOIyd1%2FasBLgsIaQoLBldMLIq1uF4xfoV2sITJRYDFfwFhPI9RuTKOvNkx9hBC%2B7tluOyZ%2BVuHxu%2Bq4hO53FN1gHuzUa0NW4QzU%2Bv5x%2F9en12RKgg6dyWF1qC0uKRJJdnAK1%2B6eyI2iIxNRo%2Fgt9npX%2Bv4%2F9P2ZekHtpDZzc8yjMOAmwDjtHsqSexTTub7XKBcByqMpVuVVThJUfj4fOjH0d%2FLam66CH%2Fn7V2mgGVJNAI1aBDLeacwxxV8qcjrZAM1EmA8GEVZCXRYDfWm8zhQz3fRyPaXEgU7sTp910NKbqYLpTAEyMhBGW7I7JjIzV1%2BVsRmi7GdHVTuL4zNn25o6puQBauZuQFA5uxSOy8y5sjQNU4P8vx7XyulpgXc9UmwwD9zlCx5pLIEscBMoTYRSrm5LCg%2FYAV0j7%2FtsHxJujGmwhiMRBNErfX%2FE7%2B4PXyC8bCuYeQfxdgKroxqE4eD2l6R6WqX7L7Pq3DU%2Bog7PGeTeRAF7DPlv1D6ZF3emumDnRfzSpuBFaacnxaF9s%2FtvdSWPXs%2FBl%2BxVXhY10GRzDJ0ZO9BjqkAYfifObVqFJfYKDxb3XvSZ1JcMlG%2F6WrPgV2h%2FZeuFer4T6tDlIIA7kxVi0FHAiwTRuH3RrMC%2FJuqqJPFC5U%2BeGR7CYLfgaovucjYO6zwKztGOYhKeYwGYDjVmNFqfKs8%2FoSRlf6rhbDkfmiB5c1dL0YSu44KD1ufOVid2nIHZx%2FQN1ABVjsCxxeI%2FLHcC6kDsXCRw8WhO2TKcgz3FnnLF%2BMK0DI&X-Amz-Signature=977d99464776e2c33225f687a7865cfa862d8e543b42bb3dcf2fac1ccc8abd7c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQN3GIDA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQC8XdzjZryW10TUSz2ACp8If24l6%2BZG4d8RfB7HFNKF%2BAIhAP7%2BKb3idZ6STolFjsgWy1Kb69A%2Fztau5HDOvKEo3fS7Kv8DCGIQABoMNjM3NDIzMTgzODA1Igyzhi12p5dXLZ0cj3gq3AP9GG3LxV2TR%2B6zFLBps5lPwrAh17IJB54FzrRsL5nhS0S6pYIgQookeSCorNjbdmazqWAbEUzUjgCLsN5tOIyd1%2FasBLgsIaQoLBldMLIq1uF4xfoV2sITJRYDFfwFhPI9RuTKOvNkx9hBC%2B7tluOyZ%2BVuHxu%2Bq4hO53FN1gHuzUa0NW4QzU%2Bv5x%2F9en12RKgg6dyWF1qC0uKRJJdnAK1%2B6eyI2iIxNRo%2Fgt9npX%2Bv4%2F9P2ZekHtpDZzc8yjMOAmwDjtHsqSexTTub7XKBcByqMpVuVVThJUfj4fOjH0d%2FLam66CH%2Fn7V2mgGVJNAI1aBDLeacwxxV8qcjrZAM1EmA8GEVZCXRYDfWm8zhQz3fRyPaXEgU7sTp910NKbqYLpTAEyMhBGW7I7JjIzV1%2BVsRmi7GdHVTuL4zNn25o6puQBauZuQFA5uxSOy8y5sjQNU4P8vx7XyulpgXc9UmwwD9zlCx5pLIEscBMoTYRSrm5LCg%2FYAV0j7%2FtsHxJujGmwhiMRBNErfX%2FE7%2B4PXyC8bCuYeQfxdgKroxqE4eD2l6R6WqX7L7Pq3DU%2Bog7PGeTeRAF7DPlv1D6ZF3emumDnRfzSpuBFaacnxaF9s%2FtvdSWPXs%2FBl%2BxVXhY10GRzDJ0ZO9BjqkAYfifObVqFJfYKDxb3XvSZ1JcMlG%2F6WrPgV2h%2FZeuFer4T6tDlIIA7kxVi0FHAiwTRuH3RrMC%2FJuqqJPFC5U%2BeGR7CYLfgaovucjYO6zwKztGOYhKeYwGYDjVmNFqfKs8%2FoSRlf6rhbDkfmiB5c1dL0YSu44KD1ufOVid2nIHZx%2FQN1ABVjsCxxeI%2FLHcC6kDsXCRw8WhO2TKcgz3FnnLF%2BMK0DI&X-Amz-Signature=b5b94f50697c91b3ef6ecadd0416f72cb1ca9c336e0531c7d27aa1741eb90acd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO26MLGY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQDH%2BZmd5CcwB%2FOetMOCeAMkBKk7WFvyblRgx%2BAKMuNSJQIgPqPBTYKSLhpdw72BUg9J%2BATP9TvhW0B9H%2BbUTkeQviYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDN14WXxVWRuLFkbhxircA5bZo50DnERMfnqVmNKj49CuwyY3I52ZeS3MM%2FTX9gap%2BpwXdmjyyameafEmkmt0nqh84nXriso2JbicaKJYU1l6hq6J0m%2F0llJlXXGhRQhTxt0t7JJcPK8N69JlvSslSoWOBc93cEWiImAo9ZR%2FYEvsKjmSu2UgG%2F4Moq0iWR5oV0ouYBnwfWNbNnMQ6LG1E7WQE11fBJiXNQeW4zDNnAuUZbWAae%2F4PdqSiBUIyogqDczRD0j15%2BPOUTbgtkHa5aIYkrMZHmhHzg3ifMI3M7gQ59W17YDMvpNWVZeTOT1sMWLK4YxJbZ35CJ6CJdCERu5aN3cci2iK5PlpVFHVJPSCKPIphEk%2F%2BB4faO8a7%2FT0Kv3qWYId55fPx7att6VQaVlTNEqkgN6YGpTgmlm3%2B7v9P52OoGkmkpRbCJZb%2FX2oo3F8T%2FIcPpnIUmpriV9GLo5o5Q3SJ6XN3Gd0Y6rB0Coq11JglIbtW6i7dfP%2BgpYVw5JtUO7scHd%2BFze0LjQZ3ed2GOHFcZiXzRIzOPgv2D%2BKVPoqdDxDNNEgiJHa0njwFT20QiXv%2Ff4TaUnxaoBScjKD2U1RCtf5wOO0xbTG2oVGJwgWIhLs%2BmhcSDcdRmPTXQ4wgwQfhuOReHL4MKbRk70GOqUBmYbUHCGGu7%2BlRc9Sq5lzDZ%2BTTCfrYbSETMtND1V11hu2RvJ0s3lPZsYJ2FkqLG2k1e4pvbIfkQVGBHyI%2B89pDNHNrvEarD%2Bx5Y2b%2BolDOhD9XtMPpSG3Wntf4GhJ4u1C8z3yLjL77k7Wj4djKkl6c5xzavZBskX%2BjJuv9njG4yEeahDl%2BzlO%2BFrUiZZysy7z%2B3%2BsGjJgrNzTFEpLlKqEnzdMJP7S&X-Amz-Signature=8498f6980cea96c354f64381720cc96a5ac513ec0e707127e039963bd03c5e7b&X-Amz-SignedHeaders=host&x-id=GetObject)
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