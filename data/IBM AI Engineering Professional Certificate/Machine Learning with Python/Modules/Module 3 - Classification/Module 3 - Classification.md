

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657NVYSEW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIAgux56Pw%2FLgfp9bGpvI32x2C8cJw8UiQuyTUsLl%2FOeSAiAVhNmJwcOWooEbWIPIzdp4d77l6eGNVwIgXRKyPrEUair%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMSksF2ELQfsZKn75LKtwDdPuQyc1rxVxYhiBr74yGKN0j%2FQuBwRS1mfCiasnyFcpvwePw4u2v4s6JA7CBWtEjsV4EoQ22Vpd%2B7LF%2BeyYPcUrWDFy2Mpu24yU67JnPUZObul06ZF3%2BEwbf36XhHioIfruuDAQ6JLpXwu%2FNQ99Y%2BCo4JZyh9T9RATaf3CIFWyJYRdD87KtIXIDc40FIWemo8u3GfSRd26R834c8HA89vbaFgUJtmcfUPGfRHta%2F84EymKeAcDvi%2BcEGDS0hyjJ6yMCdITFseA9FIn286VjUHC7X0kZBVC34gZHfbuoiwl704UBqSBTaVbInzIKXcSrI2R%2FtG%2FrLr5%2BRIHueP%2BKeFYHyKd2dQBk17Zn82oeUzTSXuC%2Bdd6rXUA32jGAPmi1kDsFLftpH3qV2yiOjKqhe2hzeaK%2FAGVRwaPXVc7CpyxXtQiu9Judd%2B7%2BvxLjEADKA8Ug4yoUEshTxpCDTeHURQE%2BoeSasxVSgrVGBbmOD7Yh9ciWrnlXDs7t7RTDUROZUqlNdutywfEo2%2B%2B7mLTNy1m%2F31A5crraQQMQkEcjgi8tv0YtpS73ZqN1xhlSwQSKqEvCdaC2kVjye7tX7OozhwgGYDauzz9SYCbx3n6hUus1912rhLRTMsZ1cSgcw2sOYvQY6pgGTCtps5Xaiq2zHFUOIDtIFihASGvtDE6umXRtHv5r3TkzcS1Kn8XfV0Dbnq6XHMsRG0tu6NqEBr%2B1iCz%2BH%2B6p9%2BmpgWq7STqAt66KqK2UU0XWmx32qeuRfWiM%2B3SBZyyndm0l4m3HCLJHtwM5fOTARQvazEO1c3x3R49WjIxzmiZspamdUMFdZBBTkuL6ONVZj3Q%2FbmGqDwVpXfdBGN7%2Bu8XUs2dap&X-Amz-Signature=002fd76de99a4c73b29a6eb2edc20bfd8d6815e8402a09a336f24ffc860cc662&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657NVYSEW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIAgux56Pw%2FLgfp9bGpvI32x2C8cJw8UiQuyTUsLl%2FOeSAiAVhNmJwcOWooEbWIPIzdp4d77l6eGNVwIgXRKyPrEUair%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMSksF2ELQfsZKn75LKtwDdPuQyc1rxVxYhiBr74yGKN0j%2FQuBwRS1mfCiasnyFcpvwePw4u2v4s6JA7CBWtEjsV4EoQ22Vpd%2B7LF%2BeyYPcUrWDFy2Mpu24yU67JnPUZObul06ZF3%2BEwbf36XhHioIfruuDAQ6JLpXwu%2FNQ99Y%2BCo4JZyh9T9RATaf3CIFWyJYRdD87KtIXIDc40FIWemo8u3GfSRd26R834c8HA89vbaFgUJtmcfUPGfRHta%2F84EymKeAcDvi%2BcEGDS0hyjJ6yMCdITFseA9FIn286VjUHC7X0kZBVC34gZHfbuoiwl704UBqSBTaVbInzIKXcSrI2R%2FtG%2FrLr5%2BRIHueP%2BKeFYHyKd2dQBk17Zn82oeUzTSXuC%2Bdd6rXUA32jGAPmi1kDsFLftpH3qV2yiOjKqhe2hzeaK%2FAGVRwaPXVc7CpyxXtQiu9Judd%2B7%2BvxLjEADKA8Ug4yoUEshTxpCDTeHURQE%2BoeSasxVSgrVGBbmOD7Yh9ciWrnlXDs7t7RTDUROZUqlNdutywfEo2%2B%2B7mLTNy1m%2F31A5crraQQMQkEcjgi8tv0YtpS73ZqN1xhlSwQSKqEvCdaC2kVjye7tX7OozhwgGYDauzz9SYCbx3n6hUus1912rhLRTMsZ1cSgcw2sOYvQY6pgGTCtps5Xaiq2zHFUOIDtIFihASGvtDE6umXRtHv5r3TkzcS1Kn8XfV0Dbnq6XHMsRG0tu6NqEBr%2B1iCz%2BH%2B6p9%2BmpgWq7STqAt66KqK2UU0XWmx32qeuRfWiM%2B3SBZyyndm0l4m3HCLJHtwM5fOTARQvazEO1c3x3R49WjIxzmiZspamdUMFdZBBTkuL6ONVZj3Q%2FbmGqDwVpXfdBGN7%2Bu8XUs2dap&X-Amz-Signature=b112b45a888a31c3dee99a7b52c50e05dd7aa71e317268a487f2d0b06ce41d09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657NVYSEW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIAgux56Pw%2FLgfp9bGpvI32x2C8cJw8UiQuyTUsLl%2FOeSAiAVhNmJwcOWooEbWIPIzdp4d77l6eGNVwIgXRKyPrEUair%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMSksF2ELQfsZKn75LKtwDdPuQyc1rxVxYhiBr74yGKN0j%2FQuBwRS1mfCiasnyFcpvwePw4u2v4s6JA7CBWtEjsV4EoQ22Vpd%2B7LF%2BeyYPcUrWDFy2Mpu24yU67JnPUZObul06ZF3%2BEwbf36XhHioIfruuDAQ6JLpXwu%2FNQ99Y%2BCo4JZyh9T9RATaf3CIFWyJYRdD87KtIXIDc40FIWemo8u3GfSRd26R834c8HA89vbaFgUJtmcfUPGfRHta%2F84EymKeAcDvi%2BcEGDS0hyjJ6yMCdITFseA9FIn286VjUHC7X0kZBVC34gZHfbuoiwl704UBqSBTaVbInzIKXcSrI2R%2FtG%2FrLr5%2BRIHueP%2BKeFYHyKd2dQBk17Zn82oeUzTSXuC%2Bdd6rXUA32jGAPmi1kDsFLftpH3qV2yiOjKqhe2hzeaK%2FAGVRwaPXVc7CpyxXtQiu9Judd%2B7%2BvxLjEADKA8Ug4yoUEshTxpCDTeHURQE%2BoeSasxVSgrVGBbmOD7Yh9ciWrnlXDs7t7RTDUROZUqlNdutywfEo2%2B%2B7mLTNy1m%2F31A5crraQQMQkEcjgi8tv0YtpS73ZqN1xhlSwQSKqEvCdaC2kVjye7tX7OozhwgGYDauzz9SYCbx3n6hUus1912rhLRTMsZ1cSgcw2sOYvQY6pgGTCtps5Xaiq2zHFUOIDtIFihASGvtDE6umXRtHv5r3TkzcS1Kn8XfV0Dbnq6XHMsRG0tu6NqEBr%2B1iCz%2BH%2B6p9%2BmpgWq7STqAt66KqK2UU0XWmx32qeuRfWiM%2B3SBZyyndm0l4m3HCLJHtwM5fOTARQvazEO1c3x3R49WjIxzmiZspamdUMFdZBBTkuL6ONVZj3Q%2FbmGqDwVpXfdBGN7%2Bu8XUs2dap&X-Amz-Signature=7ecfbbe936a1d9423422570a251c3cd360c8cdc1baaf951557e568cae2021168&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBAKXVDJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGlO%2BEI5VdUrJPAvx%2Byw3i4pvjgvhyKnEkR%2FL42siXx8AiEAm%2FFzgxvEtqReHlAnbgj6f6dPa18za%2FNybjupnimZU44q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDHLRsXiy3YeL9lQ0RyrcAxVPhVkYrk6BZfePVDCMVosqK0%2Bn7O0aKwd9d8l%2BS404uaLKwGqDDD1QvjZvKEvghha0oHDvzn7Cwn5nndLxw0%2FIqZsy7%2FklCGHk3FLQWRgqBjy75m6wPyesb6qh5mo5eRWAlupfhfcbI2KSjLNei4ZMT%2B87GJmwWFpXpHaTxw4AKx7AeO73vRN0i1ORIRy5zNPQIH0co9TyRg7RKEKv5ms8ujc%2FlSYxhAy7T%2FiTy4ukvdtjK2XHnMhOeSkt1XBm3kk2mcUM0yj5Q5D6VhenlxV4Mgg8v9gUUTJM41CDST%2Fve7P4ZhaBr7S1zwyh51rlUwGRTjJbjjC%2FwVnhybzskoxaMJXAcGIXuExv1XB8okTutDnEBY%2FZGlv6VTDlycG8nDyZ3JYmHBsmqUxAzxgqS0G9luCitxdd7o%2BJKKBch9pjSkGO%2Fzqjn1n%2BwpeY3cnKB6EaEgv%2BFlOTWkRKgsgiRtTDcr0BhhfJyEkukVtFK8OoYp4x1yaCyEbK6fFGo0ClV9BKXx4DaS7ivE2WHDAyDXhQ03P4qDbjmcS6hZ1LZ9EaoKP8MHHXL3fNRByn9pL9Xbd%2FXDxYEN%2BvOUILwKf9lmQM3qvlzjC9SlScw%2Fq2gnZt0%2BYitr%2Fr9KJcmL2MMMXEmL0GOqUB%2FM74ZQKoAuBjkj4ivkZKLYgDx5ivl1enO%2FN%2BvYqpdxuu8cG%2BPVIcK3%2FnJIIxx%2B4HLMUauD5AW74Yl%2B8yMbuw0k0h%2BASRkWkX4uAwrmWHLcsYGjrUcr2%2B6lgs7GCQpgbujI620gbtFGNlnPd%2FASPB%2BvgeYh3N2JliaPb0njFEKQ6hfgdLG81cfAFeyIVcsc6nXNSqYVsoE0m%2FCCjweu%2Bf%2FVsC31Zq&X-Amz-Signature=4864ced47f1c684de8844d6e6eafd7b711ce6d80c9235ceac43e046dc2060b65&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBAKXVDJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIGlO%2BEI5VdUrJPAvx%2Byw3i4pvjgvhyKnEkR%2FL42siXx8AiEAm%2FFzgxvEtqReHlAnbgj6f6dPa18za%2FNybjupnimZU44q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDHLRsXiy3YeL9lQ0RyrcAxVPhVkYrk6BZfePVDCMVosqK0%2Bn7O0aKwd9d8l%2BS404uaLKwGqDDD1QvjZvKEvghha0oHDvzn7Cwn5nndLxw0%2FIqZsy7%2FklCGHk3FLQWRgqBjy75m6wPyesb6qh5mo5eRWAlupfhfcbI2KSjLNei4ZMT%2B87GJmwWFpXpHaTxw4AKx7AeO73vRN0i1ORIRy5zNPQIH0co9TyRg7RKEKv5ms8ujc%2FlSYxhAy7T%2FiTy4ukvdtjK2XHnMhOeSkt1XBm3kk2mcUM0yj5Q5D6VhenlxV4Mgg8v9gUUTJM41CDST%2Fve7P4ZhaBr7S1zwyh51rlUwGRTjJbjjC%2FwVnhybzskoxaMJXAcGIXuExv1XB8okTutDnEBY%2FZGlv6VTDlycG8nDyZ3JYmHBsmqUxAzxgqS0G9luCitxdd7o%2BJKKBch9pjSkGO%2Fzqjn1n%2BwpeY3cnKB6EaEgv%2BFlOTWkRKgsgiRtTDcr0BhhfJyEkukVtFK8OoYp4x1yaCyEbK6fFGo0ClV9BKXx4DaS7ivE2WHDAyDXhQ03P4qDbjmcS6hZ1LZ9EaoKP8MHHXL3fNRByn9pL9Xbd%2FXDxYEN%2BvOUILwKf9lmQM3qvlzjC9SlScw%2Fq2gnZt0%2BYitr%2Fr9KJcmL2MMMXEmL0GOqUB%2FM74ZQKoAuBjkj4ivkZKLYgDx5ivl1enO%2FN%2BvYqpdxuu8cG%2BPVIcK3%2FnJIIxx%2B4HLMUauD5AW74Yl%2B8yMbuw0k0h%2BASRkWkX4uAwrmWHLcsYGjrUcr2%2B6lgs7GCQpgbujI620gbtFGNlnPd%2FASPB%2BvgeYh3N2JliaPb0njFEKQ6hfgdLG81cfAFeyIVcsc6nXNSqYVsoE0m%2FCCjweu%2Bf%2FVsC31Zq&X-Amz-Signature=8e0960b80441aaaa98fdd9b17f8b1a677cd457c4d35a07d6408768960acbbe0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657NVYSEW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T151522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJGMEQCIAgux56Pw%2FLgfp9bGpvI32x2C8cJw8UiQuyTUsLl%2FOeSAiAVhNmJwcOWooEbWIPIzdp4d77l6eGNVwIgXRKyPrEUair%2FAwh4EAAaDDYzNzQyMzE4MzgwNSIMSksF2ELQfsZKn75LKtwDdPuQyc1rxVxYhiBr74yGKN0j%2FQuBwRS1mfCiasnyFcpvwePw4u2v4s6JA7CBWtEjsV4EoQ22Vpd%2B7LF%2BeyYPcUrWDFy2Mpu24yU67JnPUZObul06ZF3%2BEwbf36XhHioIfruuDAQ6JLpXwu%2FNQ99Y%2BCo4JZyh9T9RATaf3CIFWyJYRdD87KtIXIDc40FIWemo8u3GfSRd26R834c8HA89vbaFgUJtmcfUPGfRHta%2F84EymKeAcDvi%2BcEGDS0hyjJ6yMCdITFseA9FIn286VjUHC7X0kZBVC34gZHfbuoiwl704UBqSBTaVbInzIKXcSrI2R%2FtG%2FrLr5%2BRIHueP%2BKeFYHyKd2dQBk17Zn82oeUzTSXuC%2Bdd6rXUA32jGAPmi1kDsFLftpH3qV2yiOjKqhe2hzeaK%2FAGVRwaPXVc7CpyxXtQiu9Judd%2B7%2BvxLjEADKA8Ug4yoUEshTxpCDTeHURQE%2BoeSasxVSgrVGBbmOD7Yh9ciWrnlXDs7t7RTDUROZUqlNdutywfEo2%2B%2B7mLTNy1m%2F31A5crraQQMQkEcjgi8tv0YtpS73ZqN1xhlSwQSKqEvCdaC2kVjye7tX7OozhwgGYDauzz9SYCbx3n6hUus1912rhLRTMsZ1cSgcw2sOYvQY6pgGTCtps5Xaiq2zHFUOIDtIFihASGvtDE6umXRtHv5r3TkzcS1Kn8XfV0Dbnq6XHMsRG0tu6NqEBr%2B1iCz%2BH%2B6p9%2BmpgWq7STqAt66KqK2UU0XWmx32qeuRfWiM%2B3SBZyyndm0l4m3HCLJHtwM5fOTARQvazEO1c3x3R49WjIxzmiZspamdUMFdZBBTkuL6ONVZj3Q%2FbmGqDwVpXfdBGN7%2Bu8XUs2dap&X-Amz-Signature=626c2adc5ef2e200c7915a33bfc7741ba6d937d12139362def0f75cab1942f04&X-Amz-SignedHeaders=host&x-id=GetObject)
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