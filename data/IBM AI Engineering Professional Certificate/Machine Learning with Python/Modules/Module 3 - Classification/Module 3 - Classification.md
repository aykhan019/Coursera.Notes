

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652IKKQPQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIA66tySQ0IYwO7%2FIi%2B9s65EIpa7mrXTGnSumNqVB1Y%2BFAiBFAGVt%2B%2FJdLleMTqurbqHOg8iMzQDAbicCklgOPHaEDiqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6vmP8ZvFhTv0xn3qKtwDz27YBxxN9Ck8LLniZ4mQGyR9qG0%2BmzvFl3vRVa%2B4POGDJtyOwdc0b1dl1j5Ht7RtIEeLGWImIbFnsY%2FVELpPLZMppLC%2FdUr%2F%2B7HwPDxMdqoQrvIjbrtC0h7rE4X1auOKdtyEqsTCcB%2FTRe6Ultp7CBJXNGR54N1cGMdeo7maKs5bavY1sq2eM4oF2kS14RmqB1ioGykxGnxwNKgAREKFOG3KNx52s%2FaViVY2hdJ6sao3gXpWAJ6VOcVgil0Z24hmO6jimuksxlthvaMB0tOoJR1c30VBWMITKeL6qp3DfJ6MouLIz8Jh3ciX1Rt7gXPQYnwI0nRTxxeennCh8sp1ZlG4gotKFwnzUgCG%2Fn41n0FYnicK2I%2BUxtLocMlKN1VYh%2B%2FVihYL%2FOFFy2unEgmEqSNIDncIk1cz%2BxZrkkuO9tAqLeksOGbqF1GUiRUvHmWMWDA9t8fri2nb5%2FQlrjHbP6ig6xM%2BiO1gAc4P%2B0CuPaoR0c%2FC6kxBRE%2B7Det%2BqTIPRGtdVDdmSdERTk8aRj09EBBjl15uUL3uXU%2FwyKrDgSRVRDJO3nUZ6PceeWkAxjn2rrULkI1tEd8wVzzU%2B9zUfBNT1t%2FOfKLaMcc4p61QLsMrvwt8NIwIHvH4%2BDowyIWdvQY6pgHumZMEHTYmHYfXL5aUNUZQr5GEaQpKVT8m8Ai55tz75vv2FYZPhTqCSGFpDMzTLsezUQIvrwzoB8Ulz8cQgC4h%2B4Enkl%2Brz0GITo2FTvUVvmhy%2BO520Owvx%2BFzPVAYUTQaerJ6uqDdVQOxf5qikyOtdOoaaig07KzAxxmGN90hRjspdxKLWn4cx5H6fEGnWbovPeE1TaZRj4cjrEmTumseO4k2YnDv&X-Amz-Signature=3e5731418979e788340c090a4c70e9844e53033e0a35f25cf829f972fb03410c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652IKKQPQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIA66tySQ0IYwO7%2FIi%2B9s65EIpa7mrXTGnSumNqVB1Y%2BFAiBFAGVt%2B%2FJdLleMTqurbqHOg8iMzQDAbicCklgOPHaEDiqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6vmP8ZvFhTv0xn3qKtwDz27YBxxN9Ck8LLniZ4mQGyR9qG0%2BmzvFl3vRVa%2B4POGDJtyOwdc0b1dl1j5Ht7RtIEeLGWImIbFnsY%2FVELpPLZMppLC%2FdUr%2F%2B7HwPDxMdqoQrvIjbrtC0h7rE4X1auOKdtyEqsTCcB%2FTRe6Ultp7CBJXNGR54N1cGMdeo7maKs5bavY1sq2eM4oF2kS14RmqB1ioGykxGnxwNKgAREKFOG3KNx52s%2FaViVY2hdJ6sao3gXpWAJ6VOcVgil0Z24hmO6jimuksxlthvaMB0tOoJR1c30VBWMITKeL6qp3DfJ6MouLIz8Jh3ciX1Rt7gXPQYnwI0nRTxxeennCh8sp1ZlG4gotKFwnzUgCG%2Fn41n0FYnicK2I%2BUxtLocMlKN1VYh%2B%2FVihYL%2FOFFy2unEgmEqSNIDncIk1cz%2BxZrkkuO9tAqLeksOGbqF1GUiRUvHmWMWDA9t8fri2nb5%2FQlrjHbP6ig6xM%2BiO1gAc4P%2B0CuPaoR0c%2FC6kxBRE%2B7Det%2BqTIPRGtdVDdmSdERTk8aRj09EBBjl15uUL3uXU%2FwyKrDgSRVRDJO3nUZ6PceeWkAxjn2rrULkI1tEd8wVzzU%2B9zUfBNT1t%2FOfKLaMcc4p61QLsMrvwt8NIwIHvH4%2BDowyIWdvQY6pgHumZMEHTYmHYfXL5aUNUZQr5GEaQpKVT8m8Ai55tz75vv2FYZPhTqCSGFpDMzTLsezUQIvrwzoB8Ulz8cQgC4h%2B4Enkl%2Brz0GITo2FTvUVvmhy%2BO520Owvx%2BFzPVAYUTQaerJ6uqDdVQOxf5qikyOtdOoaaig07KzAxxmGN90hRjspdxKLWn4cx5H6fEGnWbovPeE1TaZRj4cjrEmTumseO4k2YnDv&X-Amz-Signature=1a5aa393332f1ddf501a817761709840b0d4daea3a9be07c2d0d2f6c6f2f7e98&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652IKKQPQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIA66tySQ0IYwO7%2FIi%2B9s65EIpa7mrXTGnSumNqVB1Y%2BFAiBFAGVt%2B%2FJdLleMTqurbqHOg8iMzQDAbicCklgOPHaEDiqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6vmP8ZvFhTv0xn3qKtwDz27YBxxN9Ck8LLniZ4mQGyR9qG0%2BmzvFl3vRVa%2B4POGDJtyOwdc0b1dl1j5Ht7RtIEeLGWImIbFnsY%2FVELpPLZMppLC%2FdUr%2F%2B7HwPDxMdqoQrvIjbrtC0h7rE4X1auOKdtyEqsTCcB%2FTRe6Ultp7CBJXNGR54N1cGMdeo7maKs5bavY1sq2eM4oF2kS14RmqB1ioGykxGnxwNKgAREKFOG3KNx52s%2FaViVY2hdJ6sao3gXpWAJ6VOcVgil0Z24hmO6jimuksxlthvaMB0tOoJR1c30VBWMITKeL6qp3DfJ6MouLIz8Jh3ciX1Rt7gXPQYnwI0nRTxxeennCh8sp1ZlG4gotKFwnzUgCG%2Fn41n0FYnicK2I%2BUxtLocMlKN1VYh%2B%2FVihYL%2FOFFy2unEgmEqSNIDncIk1cz%2BxZrkkuO9tAqLeksOGbqF1GUiRUvHmWMWDA9t8fri2nb5%2FQlrjHbP6ig6xM%2BiO1gAc4P%2B0CuPaoR0c%2FC6kxBRE%2B7Det%2BqTIPRGtdVDdmSdERTk8aRj09EBBjl15uUL3uXU%2FwyKrDgSRVRDJO3nUZ6PceeWkAxjn2rrULkI1tEd8wVzzU%2B9zUfBNT1t%2FOfKLaMcc4p61QLsMrvwt8NIwIHvH4%2BDowyIWdvQY6pgHumZMEHTYmHYfXL5aUNUZQr5GEaQpKVT8m8Ai55tz75vv2FYZPhTqCSGFpDMzTLsezUQIvrwzoB8Ulz8cQgC4h%2B4Enkl%2Brz0GITo2FTvUVvmhy%2BO520Owvx%2BFzPVAYUTQaerJ6uqDdVQOxf5qikyOtdOoaaig07KzAxxmGN90hRjspdxKLWn4cx5H6fEGnWbovPeE1TaZRj4cjrEmTumseO4k2YnDv&X-Amz-Signature=548ffef00ba63b03857dcb8a61d20d89798f38a13dd11b097c82caf8c397f68b&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIVKZ45F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDZ3sdQHby0t1ik7jT%2F0fnqUggg6FV31cZyu35sJXYztAiEAjOK25iC8qg2q3ULIuZJHb%2B%2FjPWLc960FV51ZDcu5jjMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAA3lYWcktVbyRuW7ircA7F1hV%2Fw%2BniJO1JC5b22BmW%2Fdl83a%2FNUUPTGF3fMzsR1DcWAScMHAl1%2BWUuQk0AVpD1oD2poa9shCBQBEvhQYj3JVfN8gE%2FFG5bqPlpdFYX2szvKsRYJ0oNf7HYYqv7iSr3GPYt8uYC7636MYLDNSh8GuYUroY5e1XwQfsFVcbopawlieObJ2GKvFn5%2B4csPnNl5hiKDbzFmi16Z8mbyBwdlbCu7lzLcq29I3Z5f4YII%2B32ZS86pPpF9AfdfN8HkY3tRmifxWnKYeGGGGxXO%2Fvgc%2FsFElvFR5uhn7KegwTpYgqJUBLX9QoO1eAZpd2SBiCS6XYAKkPLT2v4U5QDE9MSSeclOIneu4RSH5sLVoTsot%2FS%2FYn3lpY0nl4eSe4yu8pZRQ3C6uCTnb85OOp8rVfva9Y2f9T1M8R4H7oK%2BYRC8HM%2BnhPkD6PO0yCOpXYoQFrLGfYibY8v9yCMiAKDQ81dIC655uVv8gNd7uTKQ2FjzlFO5zR8Ryad5E9U6IWXUVR9xeYzDO3RFRLGOwFJmd9ALcyBdF3NjxkmPipfYfjT9Qv%2BqKK6PMqRCHFvEpM%2FqmoSbK%2FX9OMakmk8DPENLnWovgTAET%2Bl7ZdSid49d%2FcLHh%2F0uvwHWwZm0%2BdmXMMuFnb0GOqUBPcsPTrhJZitHubCaer4XkgSWAb8hPb2NwdgzWMqf0luEF1JIvodEH0YV1nbR3wHMM5s7rTZFYH9Rcr3P%2FjJOHStFJgbbYynkWnQ%2BjQx35dra%2BIK9t3ChN5ZwuPUjT12nLyiyhlkI0WE7qqk%2BRxOFowC9Fp0C1f%2BABKWxp0vbV8AIP1WyDIjGe2MYzVPSvSE2hcpx4sT0bt7vxMuR9VJ6fG1amqMO&X-Amz-Signature=473991283f9d208edd3d147a3c1011a4c7a33b9d0c8b6c28c5fe1ab05b9478dc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIVKZ45F%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDZ3sdQHby0t1ik7jT%2F0fnqUggg6FV31cZyu35sJXYztAiEAjOK25iC8qg2q3ULIuZJHb%2B%2FjPWLc960FV51ZDcu5jjMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAA3lYWcktVbyRuW7ircA7F1hV%2Fw%2BniJO1JC5b22BmW%2Fdl83a%2FNUUPTGF3fMzsR1DcWAScMHAl1%2BWUuQk0AVpD1oD2poa9shCBQBEvhQYj3JVfN8gE%2FFG5bqPlpdFYX2szvKsRYJ0oNf7HYYqv7iSr3GPYt8uYC7636MYLDNSh8GuYUroY5e1XwQfsFVcbopawlieObJ2GKvFn5%2B4csPnNl5hiKDbzFmi16Z8mbyBwdlbCu7lzLcq29I3Z5f4YII%2B32ZS86pPpF9AfdfN8HkY3tRmifxWnKYeGGGGxXO%2Fvgc%2FsFElvFR5uhn7KegwTpYgqJUBLX9QoO1eAZpd2SBiCS6XYAKkPLT2v4U5QDE9MSSeclOIneu4RSH5sLVoTsot%2FS%2FYn3lpY0nl4eSe4yu8pZRQ3C6uCTnb85OOp8rVfva9Y2f9T1M8R4H7oK%2BYRC8HM%2BnhPkD6PO0yCOpXYoQFrLGfYibY8v9yCMiAKDQ81dIC655uVv8gNd7uTKQ2FjzlFO5zR8Ryad5E9U6IWXUVR9xeYzDO3RFRLGOwFJmd9ALcyBdF3NjxkmPipfYfjT9Qv%2BqKK6PMqRCHFvEpM%2FqmoSbK%2FX9OMakmk8DPENLnWovgTAET%2Bl7ZdSid49d%2FcLHh%2F0uvwHWwZm0%2BdmXMMuFnb0GOqUBPcsPTrhJZitHubCaer4XkgSWAb8hPb2NwdgzWMqf0luEF1JIvodEH0YV1nbR3wHMM5s7rTZFYH9Rcr3P%2FjJOHStFJgbbYynkWnQ%2BjQx35dra%2BIK9t3ChN5ZwuPUjT12nLyiyhlkI0WE7qqk%2BRxOFowC9Fp0C1f%2BABKWxp0vbV8AIP1WyDIjGe2MYzVPSvSE2hcpx4sT0bt7vxMuR9VJ6fG1amqMO&X-Amz-Signature=443984acc3f751b8616fcdb689dc59861481a1f9ac7eabad356878e6ed8b32cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652IKKQPQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIA66tySQ0IYwO7%2FIi%2B9s65EIpa7mrXTGnSumNqVB1Y%2BFAiBFAGVt%2B%2FJdLleMTqurbqHOg8iMzQDAbicCklgOPHaEDiqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6vmP8ZvFhTv0xn3qKtwDz27YBxxN9Ck8LLniZ4mQGyR9qG0%2BmzvFl3vRVa%2B4POGDJtyOwdc0b1dl1j5Ht7RtIEeLGWImIbFnsY%2FVELpPLZMppLC%2FdUr%2F%2B7HwPDxMdqoQrvIjbrtC0h7rE4X1auOKdtyEqsTCcB%2FTRe6Ultp7CBJXNGR54N1cGMdeo7maKs5bavY1sq2eM4oF2kS14RmqB1ioGykxGnxwNKgAREKFOG3KNx52s%2FaViVY2hdJ6sao3gXpWAJ6VOcVgil0Z24hmO6jimuksxlthvaMB0tOoJR1c30VBWMITKeL6qp3DfJ6MouLIz8Jh3ciX1Rt7gXPQYnwI0nRTxxeennCh8sp1ZlG4gotKFwnzUgCG%2Fn41n0FYnicK2I%2BUxtLocMlKN1VYh%2B%2FVihYL%2FOFFy2unEgmEqSNIDncIk1cz%2BxZrkkuO9tAqLeksOGbqF1GUiRUvHmWMWDA9t8fri2nb5%2FQlrjHbP6ig6xM%2BiO1gAc4P%2B0CuPaoR0c%2FC6kxBRE%2B7Det%2BqTIPRGtdVDdmSdERTk8aRj09EBBjl15uUL3uXU%2FwyKrDgSRVRDJO3nUZ6PceeWkAxjn2rrULkI1tEd8wVzzU%2B9zUfBNT1t%2FOfKLaMcc4p61QLsMrvwt8NIwIHvH4%2BDowyIWdvQY6pgHumZMEHTYmHYfXL5aUNUZQr5GEaQpKVT8m8Ai55tz75vv2FYZPhTqCSGFpDMzTLsezUQIvrwzoB8Ulz8cQgC4h%2B4Enkl%2Brz0GITo2FTvUVvmhy%2BO520Owvx%2BFzPVAYUTQaerJ6uqDdVQOxf5qikyOtdOoaaig07KzAxxmGN90hRjspdxKLWn4cx5H6fEGnWbovPeE1TaZRj4cjrEmTumseO4k2YnDv&X-Amz-Signature=a14a9ba4942e4491c7f84ec3dfd95b9ef51c79e36140b68902dafa4d997218cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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