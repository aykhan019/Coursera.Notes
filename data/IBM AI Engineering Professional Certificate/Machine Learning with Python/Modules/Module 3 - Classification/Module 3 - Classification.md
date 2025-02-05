

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBT4X5IU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQC2lKmu%2BneOS7RdL3MDS09S30SwwI5YdlMT%2FXT0REFeHgIhAPkEjk9iUbGDhfzy0WGVdrddoN%2BDrJy%2Fxjr%2FLTrpf699Kv8DCEQQABoMNjM3NDIzMTgzODA1IgxQYCDirXUNGSPdNa8q3AMZCLv3FHXVfZ9P6S3P5dW5SUeShossXnwZZlPE4k%2Ftbd0%2BoDNYDufWsTAV%2BMgxrotsbYe%2B7KvW%2FCfkWfqJ4j1fosHiiA0jdUJKIz08%2BATFYed6ZAT26tOY9WtOLVH6%2B3ApA5QZ0%2FLOuyu%2F5HFwp77f4H0l2h7Ft1D%2FtwkHo15NsKAuFWhfFok3QMBcVxn1D%2BVk16%2F52LUusfght33v35Au9fC52FmmuUnSMHmPWcE8mFV6rL6lWRyKScRh07qxN1JWHRo2kgZz7GhKVbDAvk5uVPalhyG5fuqLK0g%2FJF0i%2FDylKiF3Zq%2Fjvg%2BBRzMexsZCPZjd%2BrilF5IDMtB88RdnmRbVPrViXKpUGhg%2FfPjaVFFEig4y%2FwdKFu3aIrWQyM6NxC4Qr0ZVlMTOCm1Xzq8UW2e4hTzz0wWfN5RFIeSEo%2FE7PDQJwl3yWleSKQL1rRy8j56iZVkur1hz4ljN7iGWxLIr9khBffLR36c8%2B5fB0rj4Af2Xe2mb2cUSMZn7184zUpZbEBKEImeKKMRAt40w3IKiNh2nXNEGEga0jsIZCw7mHpiCnXkt437JtFTcsAq78xdduiSFTjgGRNnyUJfD2yMoLNRLYPDKA509ZfxYsXFiaux1Cx39zi0u2DDmio29BjqkAZFTNdP1tgNxhn4V%2BG5SuK6%2BlHxY%2BYZOlodcouA4BdY6IUWhaFkNEc11OMyWJriVQ1Tq9d%2BRpEDoHpzYrK9QPPbwlawOQGumPlPyLZodVNoORcO9JdVjGrK4rs6VGwn77EzZH6KS9CfnjYa%2Bxl%2Fi4ofm4N5UPJJB93IV4NDDeJmqpWbLJKwZME5SjafofmMW3IyVEeaJtRDZ%2FyyEqPG%2FCGsA2W88&X-Amz-Signature=0d4b4be9f5795af6bcd591232e1609cfc83a647b92f1ad4794af76af24b474f8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBT4X5IU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQC2lKmu%2BneOS7RdL3MDS09S30SwwI5YdlMT%2FXT0REFeHgIhAPkEjk9iUbGDhfzy0WGVdrddoN%2BDrJy%2Fxjr%2FLTrpf699Kv8DCEQQABoMNjM3NDIzMTgzODA1IgxQYCDirXUNGSPdNa8q3AMZCLv3FHXVfZ9P6S3P5dW5SUeShossXnwZZlPE4k%2Ftbd0%2BoDNYDufWsTAV%2BMgxrotsbYe%2B7KvW%2FCfkWfqJ4j1fosHiiA0jdUJKIz08%2BATFYed6ZAT26tOY9WtOLVH6%2B3ApA5QZ0%2FLOuyu%2F5HFwp77f4H0l2h7Ft1D%2FtwkHo15NsKAuFWhfFok3QMBcVxn1D%2BVk16%2F52LUusfght33v35Au9fC52FmmuUnSMHmPWcE8mFV6rL6lWRyKScRh07qxN1JWHRo2kgZz7GhKVbDAvk5uVPalhyG5fuqLK0g%2FJF0i%2FDylKiF3Zq%2Fjvg%2BBRzMexsZCPZjd%2BrilF5IDMtB88RdnmRbVPrViXKpUGhg%2FfPjaVFFEig4y%2FwdKFu3aIrWQyM6NxC4Qr0ZVlMTOCm1Xzq8UW2e4hTzz0wWfN5RFIeSEo%2FE7PDQJwl3yWleSKQL1rRy8j56iZVkur1hz4ljN7iGWxLIr9khBffLR36c8%2B5fB0rj4Af2Xe2mb2cUSMZn7184zUpZbEBKEImeKKMRAt40w3IKiNh2nXNEGEga0jsIZCw7mHpiCnXkt437JtFTcsAq78xdduiSFTjgGRNnyUJfD2yMoLNRLYPDKA509ZfxYsXFiaux1Cx39zi0u2DDmio29BjqkAZFTNdP1tgNxhn4V%2BG5SuK6%2BlHxY%2BYZOlodcouA4BdY6IUWhaFkNEc11OMyWJriVQ1Tq9d%2BRpEDoHpzYrK9QPPbwlawOQGumPlPyLZodVNoORcO9JdVjGrK4rs6VGwn77EzZH6KS9CfnjYa%2Bxl%2Fi4ofm4N5UPJJB93IV4NDDeJmqpWbLJKwZME5SjafofmMW3IyVEeaJtRDZ%2FyyEqPG%2FCGsA2W88&X-Amz-Signature=ff2b6edd1e458abe79e0d566475dbd106a7e2ecff64b85da95c4c3ea7d737422&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBT4X5IU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQC2lKmu%2BneOS7RdL3MDS09S30SwwI5YdlMT%2FXT0REFeHgIhAPkEjk9iUbGDhfzy0WGVdrddoN%2BDrJy%2Fxjr%2FLTrpf699Kv8DCEQQABoMNjM3NDIzMTgzODA1IgxQYCDirXUNGSPdNa8q3AMZCLv3FHXVfZ9P6S3P5dW5SUeShossXnwZZlPE4k%2Ftbd0%2BoDNYDufWsTAV%2BMgxrotsbYe%2B7KvW%2FCfkWfqJ4j1fosHiiA0jdUJKIz08%2BATFYed6ZAT26tOY9WtOLVH6%2B3ApA5QZ0%2FLOuyu%2F5HFwp77f4H0l2h7Ft1D%2FtwkHo15NsKAuFWhfFok3QMBcVxn1D%2BVk16%2F52LUusfght33v35Au9fC52FmmuUnSMHmPWcE8mFV6rL6lWRyKScRh07qxN1JWHRo2kgZz7GhKVbDAvk5uVPalhyG5fuqLK0g%2FJF0i%2FDylKiF3Zq%2Fjvg%2BBRzMexsZCPZjd%2BrilF5IDMtB88RdnmRbVPrViXKpUGhg%2FfPjaVFFEig4y%2FwdKFu3aIrWQyM6NxC4Qr0ZVlMTOCm1Xzq8UW2e4hTzz0wWfN5RFIeSEo%2FE7PDQJwl3yWleSKQL1rRy8j56iZVkur1hz4ljN7iGWxLIr9khBffLR36c8%2B5fB0rj4Af2Xe2mb2cUSMZn7184zUpZbEBKEImeKKMRAt40w3IKiNh2nXNEGEga0jsIZCw7mHpiCnXkt437JtFTcsAq78xdduiSFTjgGRNnyUJfD2yMoLNRLYPDKA509ZfxYsXFiaux1Cx39zi0u2DDmio29BjqkAZFTNdP1tgNxhn4V%2BG5SuK6%2BlHxY%2BYZOlodcouA4BdY6IUWhaFkNEc11OMyWJriVQ1Tq9d%2BRpEDoHpzYrK9QPPbwlawOQGumPlPyLZodVNoORcO9JdVjGrK4rs6VGwn77EzZH6KS9CfnjYa%2Bxl%2Fi4ofm4N5UPJJB93IV4NDDeJmqpWbLJKwZME5SjafofmMW3IyVEeaJtRDZ%2FyyEqPG%2FCGsA2W88&X-Amz-Signature=263e5a3852a51a837f5dfd46a3481f3af89f3e4cd57aa1c6bd803be7d69a28e5&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KIWTVWF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQD0bo6J9PWEkysnGL8UX%2BJBmc2WFy6cjg2ssb6GDRD0XwIhAK8sd6%2BcCil63sRz3lttiSyoOEB5PJSJC7LTo2sxDZQ2Kv8DCEcQABoMNjM3NDIzMTgzODA1IgydoEIChlNPs9erXiIq3APc0tR7Naz89HdAVkDoSnUm0JL7cIXbwl0RSaBFZ6GpFkLj5sr2uK8ZpG%2BilVWtKJCI0%2Bfi85dMiLTmBAm6aJrguG9ALZpG4cqTW%2F3hGVWsocWCT5FetyXPtgIjksNWe03NC7HL5x6f9RZ%2FWtaMDqp7HROXb7r3AzCcucPh0tCvfS%2B5nIgC6cpqFk6QWc%2BiU3hUkR%2FNRk6QQ4%2FReVnzv%2FG0JRzGRZV3pJ1vSZ2a%2BbGT8fHtxl1ygzPrExlDJTMISWiPmC7s60AAkSEk00sWhmQyBRMvPQyYpgLGorC7tjiGzSZvGTKM%2FgXk07wda6qdBfXdahY8diSl104HLTnWI8kttwSpuDLQnfrw4hBGVqseb4QUUOSTcr%2FwVmrahHuHaGQp5cbx4c%2FBiQkWLcPS%2BOo47BEdPo2XvF3exgjTLWyjR6EupB8st%2FNrr9Pxi%2BLxXtSzqYN0gGiHbIJDSuHXrQJhj2myIF8%2BdSuER%2FGnP35Fsgz7LKmzdFv8BXgYhcUwYotKo1F0UCRNI%2FHLNgB18fuUBMGRPmyjpmTTsIG8jb30lMYOTVoENaTJTbMNZ4Jtnek9EhVFmUMz7c9dSUJaEKe0VSXVCcRjFlpdY61MsI%2BdgWcBRkGXLCze%2FdluRTC44429BjqkAfFBOQq69F4AguG7oMU37rC4YI9PfeH%2F4LzEsM6Uzxq8WTEyQ%2BsVLJRzYxPsU%2FePI0kzGTWBrdcrRbl009xkGm8gTc1DMugzlGZ27GGMRQGlAgZ0aUo6BNpTYWIfEDplrBZHqA%2BEiUsTV3pD0RVlWUFfzyf55ZQ9CPiL%2BMSviatQbL57rr5JIHJz9cXk2eluyFCWK1SCEhOxIdwGYcuOSmP7e3%2BI&X-Amz-Signature=5d1dace687091f184804872156f9fccf8c83e1c0d04c59b88c33626875125f0b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KIWTVWF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQD0bo6J9PWEkysnGL8UX%2BJBmc2WFy6cjg2ssb6GDRD0XwIhAK8sd6%2BcCil63sRz3lttiSyoOEB5PJSJC7LTo2sxDZQ2Kv8DCEcQABoMNjM3NDIzMTgzODA1IgydoEIChlNPs9erXiIq3APc0tR7Naz89HdAVkDoSnUm0JL7cIXbwl0RSaBFZ6GpFkLj5sr2uK8ZpG%2BilVWtKJCI0%2Bfi85dMiLTmBAm6aJrguG9ALZpG4cqTW%2F3hGVWsocWCT5FetyXPtgIjksNWe03NC7HL5x6f9RZ%2FWtaMDqp7HROXb7r3AzCcucPh0tCvfS%2B5nIgC6cpqFk6QWc%2BiU3hUkR%2FNRk6QQ4%2FReVnzv%2FG0JRzGRZV3pJ1vSZ2a%2BbGT8fHtxl1ygzPrExlDJTMISWiPmC7s60AAkSEk00sWhmQyBRMvPQyYpgLGorC7tjiGzSZvGTKM%2FgXk07wda6qdBfXdahY8diSl104HLTnWI8kttwSpuDLQnfrw4hBGVqseb4QUUOSTcr%2FwVmrahHuHaGQp5cbx4c%2FBiQkWLcPS%2BOo47BEdPo2XvF3exgjTLWyjR6EupB8st%2FNrr9Pxi%2BLxXtSzqYN0gGiHbIJDSuHXrQJhj2myIF8%2BdSuER%2FGnP35Fsgz7LKmzdFv8BXgYhcUwYotKo1F0UCRNI%2FHLNgB18fuUBMGRPmyjpmTTsIG8jb30lMYOTVoENaTJTbMNZ4Jtnek9EhVFmUMz7c9dSUJaEKe0VSXVCcRjFlpdY61MsI%2BdgWcBRkGXLCze%2FdluRTC44429BjqkAfFBOQq69F4AguG7oMU37rC4YI9PfeH%2F4LzEsM6Uzxq8WTEyQ%2BsVLJRzYxPsU%2FePI0kzGTWBrdcrRbl009xkGm8gTc1DMugzlGZ27GGMRQGlAgZ0aUo6BNpTYWIfEDplrBZHqA%2BEiUsTV3pD0RVlWUFfzyf55ZQ9CPiL%2BMSviatQbL57rr5JIHJz9cXk2eluyFCWK1SCEhOxIdwGYcuOSmP7e3%2BI&X-Amz-Signature=f80908acb0356f73915c24b9bc610a31df731039e372210d601d1498b2bcf856&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBT4X5IU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQC2lKmu%2BneOS7RdL3MDS09S30SwwI5YdlMT%2FXT0REFeHgIhAPkEjk9iUbGDhfzy0WGVdrddoN%2BDrJy%2Fxjr%2FLTrpf699Kv8DCEQQABoMNjM3NDIzMTgzODA1IgxQYCDirXUNGSPdNa8q3AMZCLv3FHXVfZ9P6S3P5dW5SUeShossXnwZZlPE4k%2Ftbd0%2BoDNYDufWsTAV%2BMgxrotsbYe%2B7KvW%2FCfkWfqJ4j1fosHiiA0jdUJKIz08%2BATFYed6ZAT26tOY9WtOLVH6%2B3ApA5QZ0%2FLOuyu%2F5HFwp77f4H0l2h7Ft1D%2FtwkHo15NsKAuFWhfFok3QMBcVxn1D%2BVk16%2F52LUusfght33v35Au9fC52FmmuUnSMHmPWcE8mFV6rL6lWRyKScRh07qxN1JWHRo2kgZz7GhKVbDAvk5uVPalhyG5fuqLK0g%2FJF0i%2FDylKiF3Zq%2Fjvg%2BBRzMexsZCPZjd%2BrilF5IDMtB88RdnmRbVPrViXKpUGhg%2FfPjaVFFEig4y%2FwdKFu3aIrWQyM6NxC4Qr0ZVlMTOCm1Xzq8UW2e4hTzz0wWfN5RFIeSEo%2FE7PDQJwl3yWleSKQL1rRy8j56iZVkur1hz4ljN7iGWxLIr9khBffLR36c8%2B5fB0rj4Af2Xe2mb2cUSMZn7184zUpZbEBKEImeKKMRAt40w3IKiNh2nXNEGEga0jsIZCw7mHpiCnXkt437JtFTcsAq78xdduiSFTjgGRNnyUJfD2yMoLNRLYPDKA509ZfxYsXFiaux1Cx39zi0u2DDmio29BjqkAZFTNdP1tgNxhn4V%2BG5SuK6%2BlHxY%2BYZOlodcouA4BdY6IUWhaFkNEc11OMyWJriVQ1Tq9d%2BRpEDoHpzYrK9QPPbwlawOQGumPlPyLZodVNoORcO9JdVjGrK4rs6VGwn77EzZH6KS9CfnjYa%2Bxl%2Fi4ofm4N5UPJJB93IV4NDDeJmqpWbLJKwZME5SjafofmMW3IyVEeaJtRDZ%2FyyEqPG%2FCGsA2W88&X-Amz-Signature=ebe1b8b425595547052968201116dc24023755781c48de988237cbe9c228deed&X-Amz-SignedHeaders=host&x-id=GetObject)
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