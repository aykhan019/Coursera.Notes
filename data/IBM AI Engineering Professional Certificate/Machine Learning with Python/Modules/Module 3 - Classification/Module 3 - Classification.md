

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644V5D7U7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRhpldi00uCmII4Oi7%2F6ggEYOas%2BHXqyIlAd%2FJivooTgIhAKe5Re2jhaoQYjO4yJd003Zcmli6czwMkrmB5idAe%2BuBKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDExpbsswEztgx5J8q3ANNTZsovy3R86dGL4MDP1mlrwr%2FrUQtAal3f4TOK2gNxvu3JNur3IM%2FmRvDgIb%2FSW%2FDhiDRbc5Bg4pqvD6H1bqKOpjF8IXmO7m79GT3Ley%2B97nRl7OoD8RvQnlurM2qbD%2B79nwsAa0xdY7BKX%2Fqg4Af1pYURI3WwKAzYqVfYKyere2J7A448u10xItBUnDKARiTanndmeJnlsr2MAIV%2B1uXhUt5bFpePfNcW00gqrjERVd8%2Frzuyroho597bnwBsZWlFCdH9h9kpFypMH5LsDrCgY6MpUmVMHVs3SwrTYorjLBlQbhJ%2FNBErhAz7gl8aPr1HQd1%2BQtjQ4y4DAVNABf7gTGvTP6JSweGMTd%2BNX3j5OPiMPCGuCR3xLrpC%2BtYbQWoc9z91JcPfvd3acbQmN5YUXl9YZVDa29L7iOQKkS5%2FMG%2FLPzNC9p5jcQPI0ylFnZuGmHnPMfN4LHV1HBu0GLo%2Fu%2BEy97CERmv5nwnpTiJ3wjT%2Fe0AymCacaC3XG1WG20upbxqtjGIE43m2duPz8lZoChiSeZ7vpCf2p8FXzyzf75wjGo1HtHuYF88Bf8bpII5lL1SfF5NyEstkb0Uyaz24sHVuf35UATe53t9YCSD2K%2FX1UwVe3pUg8bb6zDkrPO8BjqkAbyUKC5qEMVGOYzfHMsa1x4C1O2F9QNEcZsU4KcqA8WK5gfzSB888TuO1rxEtSzEx8bYPyeS1ykdc4UloMmqtXSKMjPcq7koNO02Lo2dzw44SIqKZTh6OBtSP83q1uzG8zkSoOi2FWr56Sey5cfzOcwOwMbuCC%2BiMl5VoqnvpvOQrcXuyAqVffPL85ls8mm3zZLwqpUP0jTs7tVakVmGz7uarcBp&X-Amz-Signature=ed5d8d143bb8712cafb85e766fbef344aebeef7ee7c47c7649b8dd8086c11746&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644V5D7U7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRhpldi00uCmII4Oi7%2F6ggEYOas%2BHXqyIlAd%2FJivooTgIhAKe5Re2jhaoQYjO4yJd003Zcmli6czwMkrmB5idAe%2BuBKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDExpbsswEztgx5J8q3ANNTZsovy3R86dGL4MDP1mlrwr%2FrUQtAal3f4TOK2gNxvu3JNur3IM%2FmRvDgIb%2FSW%2FDhiDRbc5Bg4pqvD6H1bqKOpjF8IXmO7m79GT3Ley%2B97nRl7OoD8RvQnlurM2qbD%2B79nwsAa0xdY7BKX%2Fqg4Af1pYURI3WwKAzYqVfYKyere2J7A448u10xItBUnDKARiTanndmeJnlsr2MAIV%2B1uXhUt5bFpePfNcW00gqrjERVd8%2Frzuyroho597bnwBsZWlFCdH9h9kpFypMH5LsDrCgY6MpUmVMHVs3SwrTYorjLBlQbhJ%2FNBErhAz7gl8aPr1HQd1%2BQtjQ4y4DAVNABf7gTGvTP6JSweGMTd%2BNX3j5OPiMPCGuCR3xLrpC%2BtYbQWoc9z91JcPfvd3acbQmN5YUXl9YZVDa29L7iOQKkS5%2FMG%2FLPzNC9p5jcQPI0ylFnZuGmHnPMfN4LHV1HBu0GLo%2Fu%2BEy97CERmv5nwnpTiJ3wjT%2Fe0AymCacaC3XG1WG20upbxqtjGIE43m2duPz8lZoChiSeZ7vpCf2p8FXzyzf75wjGo1HtHuYF88Bf8bpII5lL1SfF5NyEstkb0Uyaz24sHVuf35UATe53t9YCSD2K%2FX1UwVe3pUg8bb6zDkrPO8BjqkAbyUKC5qEMVGOYzfHMsa1x4C1O2F9QNEcZsU4KcqA8WK5gfzSB888TuO1rxEtSzEx8bYPyeS1ykdc4UloMmqtXSKMjPcq7koNO02Lo2dzw44SIqKZTh6OBtSP83q1uzG8zkSoOi2FWr56Sey5cfzOcwOwMbuCC%2BiMl5VoqnvpvOQrcXuyAqVffPL85ls8mm3zZLwqpUP0jTs7tVakVmGz7uarcBp&X-Amz-Signature=66ba7ee6cf14ebcf8970c4fded65db010a3169141205ba3654f8f84ad2e93a9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644V5D7U7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRhpldi00uCmII4Oi7%2F6ggEYOas%2BHXqyIlAd%2FJivooTgIhAKe5Re2jhaoQYjO4yJd003Zcmli6czwMkrmB5idAe%2BuBKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDExpbsswEztgx5J8q3ANNTZsovy3R86dGL4MDP1mlrwr%2FrUQtAal3f4TOK2gNxvu3JNur3IM%2FmRvDgIb%2FSW%2FDhiDRbc5Bg4pqvD6H1bqKOpjF8IXmO7m79GT3Ley%2B97nRl7OoD8RvQnlurM2qbD%2B79nwsAa0xdY7BKX%2Fqg4Af1pYURI3WwKAzYqVfYKyere2J7A448u10xItBUnDKARiTanndmeJnlsr2MAIV%2B1uXhUt5bFpePfNcW00gqrjERVd8%2Frzuyroho597bnwBsZWlFCdH9h9kpFypMH5LsDrCgY6MpUmVMHVs3SwrTYorjLBlQbhJ%2FNBErhAz7gl8aPr1HQd1%2BQtjQ4y4DAVNABf7gTGvTP6JSweGMTd%2BNX3j5OPiMPCGuCR3xLrpC%2BtYbQWoc9z91JcPfvd3acbQmN5YUXl9YZVDa29L7iOQKkS5%2FMG%2FLPzNC9p5jcQPI0ylFnZuGmHnPMfN4LHV1HBu0GLo%2Fu%2BEy97CERmv5nwnpTiJ3wjT%2Fe0AymCacaC3XG1WG20upbxqtjGIE43m2duPz8lZoChiSeZ7vpCf2p8FXzyzf75wjGo1HtHuYF88Bf8bpII5lL1SfF5NyEstkb0Uyaz24sHVuf35UATe53t9YCSD2K%2FX1UwVe3pUg8bb6zDkrPO8BjqkAbyUKC5qEMVGOYzfHMsa1x4C1O2F9QNEcZsU4KcqA8WK5gfzSB888TuO1rxEtSzEx8bYPyeS1ykdc4UloMmqtXSKMjPcq7koNO02Lo2dzw44SIqKZTh6OBtSP83q1uzG8zkSoOi2FWr56Sey5cfzOcwOwMbuCC%2BiMl5VoqnvpvOQrcXuyAqVffPL85ls8mm3zZLwqpUP0jTs7tVakVmGz7uarcBp&X-Amz-Signature=8b2158ca86ed149472991bfd633e9d3b9d088ded2f000d0fa9a9f81505c2e843&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6EBBLFJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCO%2BCuUTpV1pvSpML8eUzGh4FSbl2nIKng4eCfAtYP4TQIhAPXQJonj4Ka8ZDOsUzrER9V3aM7KsKDncP8XKZXl5Z3SKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtFDzAynqJvasBkUMq3AMSrUdxa0QU9XtbznLtt2Bv1C06ByhFbVRdmJtO%2F0qz5Hla8aMAQZrRATLwXEWhKAlIPa7vH5%2FlFhY%2Fpbr2TS9cDLKZ%2FD4jCSzAvg8EIiS%2FOryCUN1NvUZITSjJBDr2TkIRSOYOaBGKb9ZhFRZtQoA4cojEsjM7Rq2896gWesEZJYppGPGHzCL8RtxzzdRNvuQVpi5Eri8jN5QKWgZTKZTThcnc9gxOldtqokZH4Hp17ACiGUu%2BuEVE4%2BTu2ndHP5VB%2Bs5mFS%2Fol8WUotw%2F%2B96AV5pd%2B2DCQH200KG6hycEzMgm%2BNU331dB0l3cPYC05Gt4E6KObjR09o%2BS2h2q2vmmwTmoBcaS6Sw1IHekhLPDtiMtozw7pNx%2Bc1hLzftghPY9P3RscaiBQiWY3QKuHJcINmgfbB%2F7f%2F6KovQSbJYIMpsCTpgs521WsZhR9Gs06pLgk4MgyPjOIcm8BHOmq5Ergk1yT4hbdtLdlX1gv97W2iLX4y2DjttTtDYlMNj6vwOny%2B%2B7MXjTbA4fOQII2Ic95WEjns8eqk9pd5EUVkqcoDZIEHBJN6tBM4xVxZ%2BLfER16BgNkj9HN7QzXrzaFVaraXH47YbMkTvVR8vgJsRPmSyZZrFj3NBDejg7oTDlrfO8BjqkASmL09bzkBdAf7MLG9lHZprnNQYmV1dFXYlC%2B%2FkrTj7NlbZutNKx08QsAPDy2ecSX6RRh%2F4RL1XY%2BZKeT99aMAVQJ6WyRtiiVHIBoNZWdceACw6PK15JlqeHVfi1g7jQvKGd4CubCkX8Zn6Z4nN4HdcaSkTBZyjKeEl3lzsa2KTOiolD%2FC688xnWS7Wty2Oie3rm0PtpB%2FuPbEKlsejY3EZWFode&X-Amz-Signature=9eb49766da520cc3974dc056fa958fbd873a76c79f736e6f543847c237355989&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6EBBLFJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCO%2BCuUTpV1pvSpML8eUzGh4FSbl2nIKng4eCfAtYP4TQIhAPXQJonj4Ka8ZDOsUzrER9V3aM7KsKDncP8XKZXl5Z3SKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtFDzAynqJvasBkUMq3AMSrUdxa0QU9XtbznLtt2Bv1C06ByhFbVRdmJtO%2F0qz5Hla8aMAQZrRATLwXEWhKAlIPa7vH5%2FlFhY%2Fpbr2TS9cDLKZ%2FD4jCSzAvg8EIiS%2FOryCUN1NvUZITSjJBDr2TkIRSOYOaBGKb9ZhFRZtQoA4cojEsjM7Rq2896gWesEZJYppGPGHzCL8RtxzzdRNvuQVpi5Eri8jN5QKWgZTKZTThcnc9gxOldtqokZH4Hp17ACiGUu%2BuEVE4%2BTu2ndHP5VB%2Bs5mFS%2Fol8WUotw%2F%2B96AV5pd%2B2DCQH200KG6hycEzMgm%2BNU331dB0l3cPYC05Gt4E6KObjR09o%2BS2h2q2vmmwTmoBcaS6Sw1IHekhLPDtiMtozw7pNx%2Bc1hLzftghPY9P3RscaiBQiWY3QKuHJcINmgfbB%2F7f%2F6KovQSbJYIMpsCTpgs521WsZhR9Gs06pLgk4MgyPjOIcm8BHOmq5Ergk1yT4hbdtLdlX1gv97W2iLX4y2DjttTtDYlMNj6vwOny%2B%2B7MXjTbA4fOQII2Ic95WEjns8eqk9pd5EUVkqcoDZIEHBJN6tBM4xVxZ%2BLfER16BgNkj9HN7QzXrzaFVaraXH47YbMkTvVR8vgJsRPmSyZZrFj3NBDejg7oTDlrfO8BjqkASmL09bzkBdAf7MLG9lHZprnNQYmV1dFXYlC%2B%2FkrTj7NlbZutNKx08QsAPDy2ecSX6RRh%2F4RL1XY%2BZKeT99aMAVQJ6WyRtiiVHIBoNZWdceACw6PK15JlqeHVfi1g7jQvKGd4CubCkX8Zn6Z4nN4HdcaSkTBZyjKeEl3lzsa2KTOiolD%2FC688xnWS7Wty2Oie3rm0PtpB%2FuPbEKlsejY3EZWFode&X-Amz-Signature=b1ab041e96a6a8aa4e174c689a9c94ba8239a17c1202f248cdfbf68f7af1c7af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644V5D7U7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRhpldi00uCmII4Oi7%2F6ggEYOas%2BHXqyIlAd%2FJivooTgIhAKe5Re2jhaoQYjO4yJd003Zcmli6czwMkrmB5idAe%2BuBKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxDExpbsswEztgx5J8q3ANNTZsovy3R86dGL4MDP1mlrwr%2FrUQtAal3f4TOK2gNxvu3JNur3IM%2FmRvDgIb%2FSW%2FDhiDRbc5Bg4pqvD6H1bqKOpjF8IXmO7m79GT3Ley%2B97nRl7OoD8RvQnlurM2qbD%2B79nwsAa0xdY7BKX%2Fqg4Af1pYURI3WwKAzYqVfYKyere2J7A448u10xItBUnDKARiTanndmeJnlsr2MAIV%2B1uXhUt5bFpePfNcW00gqrjERVd8%2Frzuyroho597bnwBsZWlFCdH9h9kpFypMH5LsDrCgY6MpUmVMHVs3SwrTYorjLBlQbhJ%2FNBErhAz7gl8aPr1HQd1%2BQtjQ4y4DAVNABf7gTGvTP6JSweGMTd%2BNX3j5OPiMPCGuCR3xLrpC%2BtYbQWoc9z91JcPfvd3acbQmN5YUXl9YZVDa29L7iOQKkS5%2FMG%2FLPzNC9p5jcQPI0ylFnZuGmHnPMfN4LHV1HBu0GLo%2Fu%2BEy97CERmv5nwnpTiJ3wjT%2Fe0AymCacaC3XG1WG20upbxqtjGIE43m2duPz8lZoChiSeZ7vpCf2p8FXzyzf75wjGo1HtHuYF88Bf8bpII5lL1SfF5NyEstkb0Uyaz24sHVuf35UATe53t9YCSD2K%2FX1UwVe3pUg8bb6zDkrPO8BjqkAbyUKC5qEMVGOYzfHMsa1x4C1O2F9QNEcZsU4KcqA8WK5gfzSB888TuO1rxEtSzEx8bYPyeS1ykdc4UloMmqtXSKMjPcq7koNO02Lo2dzw44SIqKZTh6OBtSP83q1uzG8zkSoOi2FWr56Sey5cfzOcwOwMbuCC%2BiMl5VoqnvpvOQrcXuyAqVffPL85ls8mm3zZLwqpUP0jTs7tVakVmGz7uarcBp&X-Amz-Signature=5d95a5dc26ecba5bfe7b493b847408077a764e83a622b4d7c2a9e187fa25dbf8&X-Amz-SignedHeaders=host&x-id=GetObject)
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