

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSCHO2II%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCF6tA%2Fj0mnjfWWF9UsFVuFKe5SRCWFlkF4PQepRXakMgIgWDquxiMbUuk%2FY6i5edYPrLC5PYAo3MP%2FSLez2Q9Vhgoq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDHHIXsjaZ0tkW16EJircA3gV7fcY%2Bya%2BlBWAcBO9eqntsM3AduHtrfvVvL4MynlAXzYAIUA%2FITix4iO2FME5vvRmi30Tk7J9HbMQfl9WfgsKedge63RrGoBlCiCaFmLciKrtYAjq8lPXeMVqxj7aWy37FeigJaNVsbm6dRWL3GYYL2%2FcoeT05HGQOOGbWTfiQoSetXXyWYam6ts6IJrRzW5k2gY7hDsp%2FYqlVJkbS3jbQayriRdV9AJFhUF%2Fd6ZHi8L6pqoGE3WPflpgV58fKu263g7CspwcXqlv4bmCVsadtR5Auvj0btteIXQX%2BlSk8zS%2FGEXTpSGplyKYuRfCt5NAYqt6AFMkgsH4MRyujR3lj9Cs0SB92y8toFM21P0gCvwJ82mYFg3ryBemtLZrjiiUCNtV3EPS3G0SQaBBG7jhfe5yUvn%2FxCjoGo6PBV7tyn8%2B0C8s9EtaGraa4bh23RowUVLYu3TvLCKS1fCZ1GMVSj9dSuQWCcHe%2Bi81ZOrGuBMVleA3JxUVruJx6NUYE%2Bw4fBGqCoq5PJWnsIoavHA%2FZsWJ7vAcl4R06V2sUej9%2BF%2BLWobIcKdK2mswTOoJpqJtjIUvnZAs6I3%2Bt5doKWIjhgvYuEmjJe3pQ5dvE9wFz3c4pJTbvD8LRs74MMH5lr0GOqUBxN4GCGDLEOjnivREe2RbMF4uEFpooN%2FXous7zvYxiIV2nEqwJuYM4uqIB8HmPSvSaL25Kr79RrxO%2Bs5A5%2BCtgDGvORV3FPRXJTJy2ACbCMEfX7ct%2BS6Z8ia2%2FYNWogEZ1g6y33j7j%2BoVFz8aGFWB3WumLE1tVLru%2BmSsGS9ossgS6pxEqlpqOOuv%2FTzJuLLZnIiDFW1zrlP2BN4vsJqoS2PF8G0J&X-Amz-Signature=c6e4829e9cb77f505f97efcfa6ddeb1fcf6c86cc52fe62349cc2d22d04948616&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSCHO2II%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCF6tA%2Fj0mnjfWWF9UsFVuFKe5SRCWFlkF4PQepRXakMgIgWDquxiMbUuk%2FY6i5edYPrLC5PYAo3MP%2FSLez2Q9Vhgoq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDHHIXsjaZ0tkW16EJircA3gV7fcY%2Bya%2BlBWAcBO9eqntsM3AduHtrfvVvL4MynlAXzYAIUA%2FITix4iO2FME5vvRmi30Tk7J9HbMQfl9WfgsKedge63RrGoBlCiCaFmLciKrtYAjq8lPXeMVqxj7aWy37FeigJaNVsbm6dRWL3GYYL2%2FcoeT05HGQOOGbWTfiQoSetXXyWYam6ts6IJrRzW5k2gY7hDsp%2FYqlVJkbS3jbQayriRdV9AJFhUF%2Fd6ZHi8L6pqoGE3WPflpgV58fKu263g7CspwcXqlv4bmCVsadtR5Auvj0btteIXQX%2BlSk8zS%2FGEXTpSGplyKYuRfCt5NAYqt6AFMkgsH4MRyujR3lj9Cs0SB92y8toFM21P0gCvwJ82mYFg3ryBemtLZrjiiUCNtV3EPS3G0SQaBBG7jhfe5yUvn%2FxCjoGo6PBV7tyn8%2B0C8s9EtaGraa4bh23RowUVLYu3TvLCKS1fCZ1GMVSj9dSuQWCcHe%2Bi81ZOrGuBMVleA3JxUVruJx6NUYE%2Bw4fBGqCoq5PJWnsIoavHA%2FZsWJ7vAcl4R06V2sUej9%2BF%2BLWobIcKdK2mswTOoJpqJtjIUvnZAs6I3%2Bt5doKWIjhgvYuEmjJe3pQ5dvE9wFz3c4pJTbvD8LRs74MMH5lr0GOqUBxN4GCGDLEOjnivREe2RbMF4uEFpooN%2FXous7zvYxiIV2nEqwJuYM4uqIB8HmPSvSaL25Kr79RrxO%2Bs5A5%2BCtgDGvORV3FPRXJTJy2ACbCMEfX7ct%2BS6Z8ia2%2FYNWogEZ1g6y33j7j%2BoVFz8aGFWB3WumLE1tVLru%2BmSsGS9ossgS6pxEqlpqOOuv%2FTzJuLLZnIiDFW1zrlP2BN4vsJqoS2PF8G0J&X-Amz-Signature=852c93bab900d18357e2831bedf64a32b235e9ef49ff529bec69657eb0f6fb25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSCHO2II%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCF6tA%2Fj0mnjfWWF9UsFVuFKe5SRCWFlkF4PQepRXakMgIgWDquxiMbUuk%2FY6i5edYPrLC5PYAo3MP%2FSLez2Q9Vhgoq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDHHIXsjaZ0tkW16EJircA3gV7fcY%2Bya%2BlBWAcBO9eqntsM3AduHtrfvVvL4MynlAXzYAIUA%2FITix4iO2FME5vvRmi30Tk7J9HbMQfl9WfgsKedge63RrGoBlCiCaFmLciKrtYAjq8lPXeMVqxj7aWy37FeigJaNVsbm6dRWL3GYYL2%2FcoeT05HGQOOGbWTfiQoSetXXyWYam6ts6IJrRzW5k2gY7hDsp%2FYqlVJkbS3jbQayriRdV9AJFhUF%2Fd6ZHi8L6pqoGE3WPflpgV58fKu263g7CspwcXqlv4bmCVsadtR5Auvj0btteIXQX%2BlSk8zS%2FGEXTpSGplyKYuRfCt5NAYqt6AFMkgsH4MRyujR3lj9Cs0SB92y8toFM21P0gCvwJ82mYFg3ryBemtLZrjiiUCNtV3EPS3G0SQaBBG7jhfe5yUvn%2FxCjoGo6PBV7tyn8%2B0C8s9EtaGraa4bh23RowUVLYu3TvLCKS1fCZ1GMVSj9dSuQWCcHe%2Bi81ZOrGuBMVleA3JxUVruJx6NUYE%2Bw4fBGqCoq5PJWnsIoavHA%2FZsWJ7vAcl4R06V2sUej9%2BF%2BLWobIcKdK2mswTOoJpqJtjIUvnZAs6I3%2Bt5doKWIjhgvYuEmjJe3pQ5dvE9wFz3c4pJTbvD8LRs74MMH5lr0GOqUBxN4GCGDLEOjnivREe2RbMF4uEFpooN%2FXous7zvYxiIV2nEqwJuYM4uqIB8HmPSvSaL25Kr79RrxO%2Bs5A5%2BCtgDGvORV3FPRXJTJy2ACbCMEfX7ct%2BS6Z8ia2%2FYNWogEZ1g6y33j7j%2BoVFz8aGFWB3WumLE1tVLru%2BmSsGS9ossgS6pxEqlpqOOuv%2FTzJuLLZnIiDFW1zrlP2BN4vsJqoS2PF8G0J&X-Amz-Signature=faffe898466fa1be7a0777918306cbac1a64a76de1981e0d3fef95fd501a47e3&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXPP5ISQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCICLif4QgLnu6eyPbbn%2FUOhlwLwsBHkHWfNxMlNd73vwvAiBoAIKFMpWznQMNxlMxvh%2FcYGPPW9Ll8O%2B6zfKLBSM62Cr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM%2FP85cEwEatit46SIKtwDQeln3YlZaObAUgHfjIE7INP5z6WYXGlMe7aSEIaHWliMCbI5zLhRswelYcgw7xEI7LMuH%2FWHa%2BEiuWvWRG3cnicWKl4TfjQwxpX0Jh2DfpWAiou4ICYNkhlPjrFVG9JjMo6DbqWPhcbK8g1v2Hhkc9gnfn1Wq2R6iEw7T8wnkUNsAEHxL1eb52uQ38I9Ag2wPo5qFWqEYuaOHo7AcPikIfhI5chN3baccNPnkMlneTzVPTrG2VtHC2xBd%2F1a%2FGJhJcrKVakhv3RKcH7ozxXFcYnwmYVYawJ8W88EkL9d85IKusYoAr5XjUOuM80HyLOXOoKBit8Xx5uRnBLpj7HhVHS3B%2FH%2BAMPyNLDyGCo4xRsWU291qBQWNAQ7IUNIqWExlgaEDUhpHWbZ5Z63QWIQ78osF5zg%2FUTSoosRlFaJv3As8O0usiWf%2B%2Bdk68%2B7cskQmF4XTSYDMH2Jn0PvcnM3OsmmrmwJBKoo9r3g7D66GL0%2Bh%2F0SnTvFniuXsaZNILKvfAuelK2hmXIGPloWGQiICfFtOmAxgUAO2h551if9GtzvFydcUnIH2C9jHujzLYcAWTAXeIUO5axR2ca4dyvDZnj6lUrCSRlXDhDmPaZ%2BqrLoPX5zRMtSj1TDhfMw%2FvmWvQY6pgG2Csfo29eTDlIMTjzthT4pXwNwYzboScT%2FgqB8KP%2Bxlku27nzEJ0TvxE2XaF76vdaagP08KlSjVzBpN5Pj5GxFreQ1H1ZlvVTzUHFkyuFFx3k90HGuBMm0J9gwq1fr2l5%2FQ2%2FeAaW5ZvFCKJzSobgtbWWEgVPhmr0jTq%2BVSX4MxC264kvTdPXso20pC0bFj3wn9rrgbT3CYyFPx4M2LlREe0tvOQes&X-Amz-Signature=0e4a557d845eaa105e312f409281c20869aaef25298154228d903b8e0b2b972a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXPP5ISQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCICLif4QgLnu6eyPbbn%2FUOhlwLwsBHkHWfNxMlNd73vwvAiBoAIKFMpWznQMNxlMxvh%2FcYGPPW9Ll8O%2B6zfKLBSM62Cr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM%2FP85cEwEatit46SIKtwDQeln3YlZaObAUgHfjIE7INP5z6WYXGlMe7aSEIaHWliMCbI5zLhRswelYcgw7xEI7LMuH%2FWHa%2BEiuWvWRG3cnicWKl4TfjQwxpX0Jh2DfpWAiou4ICYNkhlPjrFVG9JjMo6DbqWPhcbK8g1v2Hhkc9gnfn1Wq2R6iEw7T8wnkUNsAEHxL1eb52uQ38I9Ag2wPo5qFWqEYuaOHo7AcPikIfhI5chN3baccNPnkMlneTzVPTrG2VtHC2xBd%2F1a%2FGJhJcrKVakhv3RKcH7ozxXFcYnwmYVYawJ8W88EkL9d85IKusYoAr5XjUOuM80HyLOXOoKBit8Xx5uRnBLpj7HhVHS3B%2FH%2BAMPyNLDyGCo4xRsWU291qBQWNAQ7IUNIqWExlgaEDUhpHWbZ5Z63QWIQ78osF5zg%2FUTSoosRlFaJv3As8O0usiWf%2B%2Bdk68%2B7cskQmF4XTSYDMH2Jn0PvcnM3OsmmrmwJBKoo9r3g7D66GL0%2Bh%2F0SnTvFniuXsaZNILKvfAuelK2hmXIGPloWGQiICfFtOmAxgUAO2h551if9GtzvFydcUnIH2C9jHujzLYcAWTAXeIUO5axR2ca4dyvDZnj6lUrCSRlXDhDmPaZ%2BqrLoPX5zRMtSj1TDhfMw%2FvmWvQY6pgG2Csfo29eTDlIMTjzthT4pXwNwYzboScT%2FgqB8KP%2Bxlku27nzEJ0TvxE2XaF76vdaagP08KlSjVzBpN5Pj5GxFreQ1H1ZlvVTzUHFkyuFFx3k90HGuBMm0J9gwq1fr2l5%2FQ2%2FeAaW5ZvFCKJzSobgtbWWEgVPhmr0jTq%2BVSX4MxC264kvTdPXso20pC0bFj3wn9rrgbT3CYyFPx4M2LlREe0tvOQes&X-Amz-Signature=2c6cd5c2cf5e19370f6d3b127d5d8ca12d822b66ae46d6d17a53f0e4eae6d973&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSCHO2II%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCF6tA%2Fj0mnjfWWF9UsFVuFKe5SRCWFlkF4PQepRXakMgIgWDquxiMbUuk%2FY6i5edYPrLC5PYAo3MP%2FSLez2Q9Vhgoq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDHHIXsjaZ0tkW16EJircA3gV7fcY%2Bya%2BlBWAcBO9eqntsM3AduHtrfvVvL4MynlAXzYAIUA%2FITix4iO2FME5vvRmi30Tk7J9HbMQfl9WfgsKedge63RrGoBlCiCaFmLciKrtYAjq8lPXeMVqxj7aWy37FeigJaNVsbm6dRWL3GYYL2%2FcoeT05HGQOOGbWTfiQoSetXXyWYam6ts6IJrRzW5k2gY7hDsp%2FYqlVJkbS3jbQayriRdV9AJFhUF%2Fd6ZHi8L6pqoGE3WPflpgV58fKu263g7CspwcXqlv4bmCVsadtR5Auvj0btteIXQX%2BlSk8zS%2FGEXTpSGplyKYuRfCt5NAYqt6AFMkgsH4MRyujR3lj9Cs0SB92y8toFM21P0gCvwJ82mYFg3ryBemtLZrjiiUCNtV3EPS3G0SQaBBG7jhfe5yUvn%2FxCjoGo6PBV7tyn8%2B0C8s9EtaGraa4bh23RowUVLYu3TvLCKS1fCZ1GMVSj9dSuQWCcHe%2Bi81ZOrGuBMVleA3JxUVruJx6NUYE%2Bw4fBGqCoq5PJWnsIoavHA%2FZsWJ7vAcl4R06V2sUej9%2BF%2BLWobIcKdK2mswTOoJpqJtjIUvnZAs6I3%2Bt5doKWIjhgvYuEmjJe3pQ5dvE9wFz3c4pJTbvD8LRs74MMH5lr0GOqUBxN4GCGDLEOjnivREe2RbMF4uEFpooN%2FXous7zvYxiIV2nEqwJuYM4uqIB8HmPSvSaL25Kr79RrxO%2Bs5A5%2BCtgDGvORV3FPRXJTJy2ACbCMEfX7ct%2BS6Z8ia2%2FYNWogEZ1g6y33j7j%2BoVFz8aGFWB3WumLE1tVLru%2BmSsGS9ossgS6pxEqlpqOOuv%2FTzJuLLZnIiDFW1zrlP2BN4vsJqoS2PF8G0J&X-Amz-Signature=0fdea813460747e16e09d11901b0330f34cfc05e1e8790b13c11a8c37bd19e6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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