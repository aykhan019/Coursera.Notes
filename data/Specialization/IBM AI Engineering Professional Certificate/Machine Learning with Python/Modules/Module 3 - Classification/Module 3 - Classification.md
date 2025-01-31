

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QETSPWBK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDmfgNsRTR4ea4KcdtxgpE%2FWnoXZT5Xkfmv%2FUfuZ7l8XAiEA0wTcy%2Ftp3iudI8URiZ7DqklxoGwo1%2Bx2DadSymMW0T4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLewZXV4nxS2GN9PmSrcA7bpgRxd3HBCXgoGV3mTJelAHhW4p7jUUEcopSIQZw3%2FFzY8ar%2FT2hGBwPZkVNvSX2%2FTvgl4pwOhVyU0HoJBtw9wy4kcaGnA3aKnQtsUSBkI%2FpGKFZfYdZHGDzV%2FzlpktPKstwvbnt4EDm5aa%2F9PeoR3ciBmcNJhJWTtRnl%2BZHmaXfTbYwi7OwMdE3A2KDfeGRy2dkDw%2FQXTs4PLBtjXzoVz1MRweTfU5JVLbxt%2BOzFXYanAGh0uAFZVlRrjR4d8%2BFUsQ%2Bxby0RdSxMQNOfh3Up5qskscu7VL1IXYTqYxskFoG%2BSgZ4TGMWtkgqgsZjzOcn24zkkPwKyKZJDiqLSFoVAnYRQ46kx9kfDRoDOYOfCMD%2BEt68D2lvrnvs1RgUmM2R1i4rj7aC9KQLK%2Fjukm282lHb7%2BQDsyOpnvgMS2wST4ESRZZSRQXpuOKLyLCuFxZqDH17wSTm5sDM3ADwM8Um7odUDQzMDUOpJj5doAe7dFEUGYBWb1SUDlEwzR30bUjtj%2FKP%2FOwMedu3MacdfmUzyEJHIa%2FdNBnc9OcizHJCTd8LfR%2FtwVA%2Fr1WQ7WIR7dUYIB8T8WIGyBGC7uVKFuz3R4jTMA4SgoxZnO%2F7J6iYp2bo7gUP9sDyWEyAcMNu28rwGOqUBRjyLRyw0p0BTTM27o7CRmgBn9lk0R1Yf38L0NoPY1hsaiAzfhHEgur7vnnb2aJU7KFvroobkOUWLiHVT4d3eQFk9Vv5RfcgzEE6D%2Br8KgVPvCq2182Nm%2FB5Lhcimg%2BthWMQRClQxq8nbuA8ZmqDIlvYXfirlH8i%2FjnoW%2BXM4kVD2YD87NbqZBR%2FlYFx7uIAZNJcTlqQJDVOzv0mR3TIAKtk7GNSa&X-Amz-Signature=5d115b5fbcb32aef399f5779386f9015814d97bc87494aecce1620def59449f0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QETSPWBK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDmfgNsRTR4ea4KcdtxgpE%2FWnoXZT5Xkfmv%2FUfuZ7l8XAiEA0wTcy%2Ftp3iudI8URiZ7DqklxoGwo1%2Bx2DadSymMW0T4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLewZXV4nxS2GN9PmSrcA7bpgRxd3HBCXgoGV3mTJelAHhW4p7jUUEcopSIQZw3%2FFzY8ar%2FT2hGBwPZkVNvSX2%2FTvgl4pwOhVyU0HoJBtw9wy4kcaGnA3aKnQtsUSBkI%2FpGKFZfYdZHGDzV%2FzlpktPKstwvbnt4EDm5aa%2F9PeoR3ciBmcNJhJWTtRnl%2BZHmaXfTbYwi7OwMdE3A2KDfeGRy2dkDw%2FQXTs4PLBtjXzoVz1MRweTfU5JVLbxt%2BOzFXYanAGh0uAFZVlRrjR4d8%2BFUsQ%2Bxby0RdSxMQNOfh3Up5qskscu7VL1IXYTqYxskFoG%2BSgZ4TGMWtkgqgsZjzOcn24zkkPwKyKZJDiqLSFoVAnYRQ46kx9kfDRoDOYOfCMD%2BEt68D2lvrnvs1RgUmM2R1i4rj7aC9KQLK%2Fjukm282lHb7%2BQDsyOpnvgMS2wST4ESRZZSRQXpuOKLyLCuFxZqDH17wSTm5sDM3ADwM8Um7odUDQzMDUOpJj5doAe7dFEUGYBWb1SUDlEwzR30bUjtj%2FKP%2FOwMedu3MacdfmUzyEJHIa%2FdNBnc9OcizHJCTd8LfR%2FtwVA%2Fr1WQ7WIR7dUYIB8T8WIGyBGC7uVKFuz3R4jTMA4SgoxZnO%2F7J6iYp2bo7gUP9sDyWEyAcMNu28rwGOqUBRjyLRyw0p0BTTM27o7CRmgBn9lk0R1Yf38L0NoPY1hsaiAzfhHEgur7vnnb2aJU7KFvroobkOUWLiHVT4d3eQFk9Vv5RfcgzEE6D%2Br8KgVPvCq2182Nm%2FB5Lhcimg%2BthWMQRClQxq8nbuA8ZmqDIlvYXfirlH8i%2FjnoW%2BXM4kVD2YD87NbqZBR%2FlYFx7uIAZNJcTlqQJDVOzv0mR3TIAKtk7GNSa&X-Amz-Signature=db6cdb642826f746bfbf35c6a9ce408c599d09635409f61970b07b73898791c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QETSPWBK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDmfgNsRTR4ea4KcdtxgpE%2FWnoXZT5Xkfmv%2FUfuZ7l8XAiEA0wTcy%2Ftp3iudI8URiZ7DqklxoGwo1%2Bx2DadSymMW0T4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLewZXV4nxS2GN9PmSrcA7bpgRxd3HBCXgoGV3mTJelAHhW4p7jUUEcopSIQZw3%2FFzY8ar%2FT2hGBwPZkVNvSX2%2FTvgl4pwOhVyU0HoJBtw9wy4kcaGnA3aKnQtsUSBkI%2FpGKFZfYdZHGDzV%2FzlpktPKstwvbnt4EDm5aa%2F9PeoR3ciBmcNJhJWTtRnl%2BZHmaXfTbYwi7OwMdE3A2KDfeGRy2dkDw%2FQXTs4PLBtjXzoVz1MRweTfU5JVLbxt%2BOzFXYanAGh0uAFZVlRrjR4d8%2BFUsQ%2Bxby0RdSxMQNOfh3Up5qskscu7VL1IXYTqYxskFoG%2BSgZ4TGMWtkgqgsZjzOcn24zkkPwKyKZJDiqLSFoVAnYRQ46kx9kfDRoDOYOfCMD%2BEt68D2lvrnvs1RgUmM2R1i4rj7aC9KQLK%2Fjukm282lHb7%2BQDsyOpnvgMS2wST4ESRZZSRQXpuOKLyLCuFxZqDH17wSTm5sDM3ADwM8Um7odUDQzMDUOpJj5doAe7dFEUGYBWb1SUDlEwzR30bUjtj%2FKP%2FOwMedu3MacdfmUzyEJHIa%2FdNBnc9OcizHJCTd8LfR%2FtwVA%2Fr1WQ7WIR7dUYIB8T8WIGyBGC7uVKFuz3R4jTMA4SgoxZnO%2F7J6iYp2bo7gUP9sDyWEyAcMNu28rwGOqUBRjyLRyw0p0BTTM27o7CRmgBn9lk0R1Yf38L0NoPY1hsaiAzfhHEgur7vnnb2aJU7KFvroobkOUWLiHVT4d3eQFk9Vv5RfcgzEE6D%2Br8KgVPvCq2182Nm%2FB5Lhcimg%2BthWMQRClQxq8nbuA8ZmqDIlvYXfirlH8i%2FjnoW%2BXM4kVD2YD87NbqZBR%2FlYFx7uIAZNJcTlqQJDVOzv0mR3TIAKtk7GNSa&X-Amz-Signature=13b222caa897cbccd62e2c684508e67a2a37460be774afdf2a9b9df423443f23&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYL4MCNC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpIij17B5Fa%2FhvZmX%2Bv9UJG3OJK5vynJPZgXb8D3NIOAiACJIhMN%2BV6u4KGGe1cGx6sG88oYtmEUu1EBoWFav3u0CqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9TuoPeKCy4NqvIipKtwDNUYfVUN0w0V9SOHh%2FKxWPfhzQPr947pCNvpZIN7ppar38nDJmZQ6wPtpfWVk1wUFf1cLEeW0DejYXi2afgHulwWlOVyyfCJ9eNqnRCf1OHAnib9kyMo7ZybCfNCnnCWr11f%2Bon8mIQqxE9zefj3As0mf3ZBOGeuHJHuqVZIoxk7R1vAgw22Bs2aaratar1iovjpeYMlhtbvN4g1SjNQDQxyNOv0vBMv9FeCtWtSso4xQUAirHNjqEAh5RIfExhgt2ajfY0ynFeKV0I6q2G4JgMD0EppdZU59RMqH6waM68l%2Bs%2F213fUvUF2S1vSMKLizgNxeJ9%2BBIassPMvA%2BmOYAty%2B%2FfLOrKRH1IAezcBIqGQ67qctpMQ2Ejc%2B9rfNZea6%2FvDgga321PM%2FQD7u5xdmA6xnr40f6RScwZuQiLm3dnPCCP3JdeCWb368g%2BBOl1Kom0x0Bc0GL53rxo3nxE3LRiIJq5at1VAbtLEPLOKxm%2BFWxpYMEaatSGrwb1h5S3vqiRCj%2BPMP%2BBw%2B8uq%2BlzcPdnIkD%2FQwWA%2B%2BxZAYRWfvD9QkftsEj%2BtRy7w9g%2FExltKaKbHNnNAWoGo6N07SC6dVCFFQOskCSdokM9JaNJVzNjgWmKsNOVLnFT%2FgYJEwxrfyvAY6pgEMGqzmJ4m3%2FDH3uApgT40MPSEKavz%2BYF%2BFDdeiet%2BY4xETQvQNm4kuY%2FzRDLHOcZbAXU0wxeUyY2WSDAE4c7j3d4Y8pzW%2FNBPzqCblVviUns9qVGgbBrY3Y13QCyOJ3R9PGVbfWc4YwJtnTYNcrw5s4GI8kTeEHHtL2vLGs0xIm8qjO6NU9406nTsIw9duWp%2FJYVbtP7OQDqHYzc8gAcIl0dxB%2FANE&X-Amz-Signature=5c91442477f54716f4ca86d734a1d82b160e186e36d41ee710d3ca647c34bf05&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYL4MCNC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpIij17B5Fa%2FhvZmX%2Bv9UJG3OJK5vynJPZgXb8D3NIOAiACJIhMN%2BV6u4KGGe1cGx6sG88oYtmEUu1EBoWFav3u0CqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM9TuoPeKCy4NqvIipKtwDNUYfVUN0w0V9SOHh%2FKxWPfhzQPr947pCNvpZIN7ppar38nDJmZQ6wPtpfWVk1wUFf1cLEeW0DejYXi2afgHulwWlOVyyfCJ9eNqnRCf1OHAnib9kyMo7ZybCfNCnnCWr11f%2Bon8mIQqxE9zefj3As0mf3ZBOGeuHJHuqVZIoxk7R1vAgw22Bs2aaratar1iovjpeYMlhtbvN4g1SjNQDQxyNOv0vBMv9FeCtWtSso4xQUAirHNjqEAh5RIfExhgt2ajfY0ynFeKV0I6q2G4JgMD0EppdZU59RMqH6waM68l%2Bs%2F213fUvUF2S1vSMKLizgNxeJ9%2BBIassPMvA%2BmOYAty%2B%2FfLOrKRH1IAezcBIqGQ67qctpMQ2Ejc%2B9rfNZea6%2FvDgga321PM%2FQD7u5xdmA6xnr40f6RScwZuQiLm3dnPCCP3JdeCWb368g%2BBOl1Kom0x0Bc0GL53rxo3nxE3LRiIJq5at1VAbtLEPLOKxm%2BFWxpYMEaatSGrwb1h5S3vqiRCj%2BPMP%2BBw%2B8uq%2BlzcPdnIkD%2FQwWA%2B%2BxZAYRWfvD9QkftsEj%2BtRy7w9g%2FExltKaKbHNnNAWoGo6N07SC6dVCFFQOskCSdokM9JaNJVzNjgWmKsNOVLnFT%2FgYJEwxrfyvAY6pgEMGqzmJ4m3%2FDH3uApgT40MPSEKavz%2BYF%2BFDdeiet%2BY4xETQvQNm4kuY%2FzRDLHOcZbAXU0wxeUyY2WSDAE4c7j3d4Y8pzW%2FNBPzqCblVviUns9qVGgbBrY3Y13QCyOJ3R9PGVbfWc4YwJtnTYNcrw5s4GI8kTeEHHtL2vLGs0xIm8qjO6NU9406nTsIw9duWp%2FJYVbtP7OQDqHYzc8gAcIl0dxB%2FANE&X-Amz-Signature=66985a943f4c8900e735374d0128ad1ff4a8956a053728fc0744a7410bd721ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QETSPWBK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDmfgNsRTR4ea4KcdtxgpE%2FWnoXZT5Xkfmv%2FUfuZ7l8XAiEA0wTcy%2Ftp3iudI8URiZ7DqklxoGwo1%2Bx2DadSymMW0T4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLewZXV4nxS2GN9PmSrcA7bpgRxd3HBCXgoGV3mTJelAHhW4p7jUUEcopSIQZw3%2FFzY8ar%2FT2hGBwPZkVNvSX2%2FTvgl4pwOhVyU0HoJBtw9wy4kcaGnA3aKnQtsUSBkI%2FpGKFZfYdZHGDzV%2FzlpktPKstwvbnt4EDm5aa%2F9PeoR3ciBmcNJhJWTtRnl%2BZHmaXfTbYwi7OwMdE3A2KDfeGRy2dkDw%2FQXTs4PLBtjXzoVz1MRweTfU5JVLbxt%2BOzFXYanAGh0uAFZVlRrjR4d8%2BFUsQ%2Bxby0RdSxMQNOfh3Up5qskscu7VL1IXYTqYxskFoG%2BSgZ4TGMWtkgqgsZjzOcn24zkkPwKyKZJDiqLSFoVAnYRQ46kx9kfDRoDOYOfCMD%2BEt68D2lvrnvs1RgUmM2R1i4rj7aC9KQLK%2Fjukm282lHb7%2BQDsyOpnvgMS2wST4ESRZZSRQXpuOKLyLCuFxZqDH17wSTm5sDM3ADwM8Um7odUDQzMDUOpJj5doAe7dFEUGYBWb1SUDlEwzR30bUjtj%2FKP%2FOwMedu3MacdfmUzyEJHIa%2FdNBnc9OcizHJCTd8LfR%2FtwVA%2Fr1WQ7WIR7dUYIB8T8WIGyBGC7uVKFuz3R4jTMA4SgoxZnO%2F7J6iYp2bo7gUP9sDyWEyAcMNu28rwGOqUBRjyLRyw0p0BTTM27o7CRmgBn9lk0R1Yf38L0NoPY1hsaiAzfhHEgur7vnnb2aJU7KFvroobkOUWLiHVT4d3eQFk9Vv5RfcgzEE6D%2Br8KgVPvCq2182Nm%2FB5Lhcimg%2BthWMQRClQxq8nbuA8ZmqDIlvYXfirlH8i%2FjnoW%2BXM4kVD2YD87NbqZBR%2FlYFx7uIAZNJcTlqQJDVOzv0mR3TIAKtk7GNSa&X-Amz-Signature=5e1d6e7ae365081cbb4de6b3c203ba6afc00d84e176e09fbbb7388cf248f2274&X-Amz-SignedHeaders=host&x-id=GetObject)
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