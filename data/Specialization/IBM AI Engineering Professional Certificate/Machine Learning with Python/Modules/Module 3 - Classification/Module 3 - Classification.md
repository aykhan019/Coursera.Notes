

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634M5ENXP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBrJ7tUBIOxXXpF0i83t38hAxaDrdynqwgHv32tHFrXyAiEAuy1Wmcz3ur7AYYcGoWDl%2B%2BM79M03dtL9%2FaHmxKnDAlkqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLFtWGkH3TF2I9BzgyrcAz%2F2QazLo3EmbxeNYwM2%2BIaJ0ecJo1awi0w5kzgmhze3%2FC694wgjYXMCwO3tBVu0wLxRSCmYFvZsepiJLa3rFhHUp%2Bf5hb1DafewKmwReb3OVNNct7OSTXxtdMgM8C2B3n2r%2FediOVXLTU15lknBf6fLrQH%2FuxKamcFvZUVcxa63pIAGzpxA8EGueBgm7eZ04SUHAmq4C9aRykbwkiYa8%2FX0H3mF3I1QosD4%2BSGpAXV07X4IY1VsUve2KhJGDPganEP2dY6%2BzXV%2BB5Cod8LvNya%2FT6ELrgFlAamViJHQNijxl38Yy648SoN%2FQckdod12P0lK08U3Vw9ESRR6nXfTdQoLjrUv5DncIp1yv252Yp9bjxZcWDMZOBCtEXxMWfJSZjllGE%2FklL%2BhBioWtwP3qedbRRc4hWoj1UK1fAaV2DGG7SQ%2BhYfKnwGmjLI7F9rW1L8KUxEHn1n9nDra6VWIV%2F6TUppSVQAHHoLDPkwZkiMdOlRpwY5EUg7Z6sToYZV30QioyMIEgG%2Bo1k%2BPqdToiGz1Mo%2FpuzxHa0dWkk947H9OSleoSfVFcYOUr3zoxZuIW3OLTP3XMIGiD4tQ%2BqGcMlnBWN1F0FrHicsajEgOVozeRAzis1x%2FozrwH3TdMJyj7LwGOqUB2rMALNWuEk4rVadCCwzAfkqqBLoQnrAt8sNGkoq6Psw819g36kbt3SZLVoC5uYDYg2LwnnqeM%2Biauu0UqVdAQP7S9D048OFzG8J8UQhmA221q3%2B0pLir9P7R3aUpbJEdf1Rs2D6S74McUPoCs7RAOKTW0I7bXh84otN9RmDg6Tk%2BOuT%2FtngxOeAeVTkSAwMrApyyUXFLRkSu0odGOTYWetlgJWEC&X-Amz-Signature=749b2dc453591cb805b9add4e8b22d28846a8249efeb946e1a36a00a296ee4ad&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634M5ENXP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBrJ7tUBIOxXXpF0i83t38hAxaDrdynqwgHv32tHFrXyAiEAuy1Wmcz3ur7AYYcGoWDl%2B%2BM79M03dtL9%2FaHmxKnDAlkqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLFtWGkH3TF2I9BzgyrcAz%2F2QazLo3EmbxeNYwM2%2BIaJ0ecJo1awi0w5kzgmhze3%2FC694wgjYXMCwO3tBVu0wLxRSCmYFvZsepiJLa3rFhHUp%2Bf5hb1DafewKmwReb3OVNNct7OSTXxtdMgM8C2B3n2r%2FediOVXLTU15lknBf6fLrQH%2FuxKamcFvZUVcxa63pIAGzpxA8EGueBgm7eZ04SUHAmq4C9aRykbwkiYa8%2FX0H3mF3I1QosD4%2BSGpAXV07X4IY1VsUve2KhJGDPganEP2dY6%2BzXV%2BB5Cod8LvNya%2FT6ELrgFlAamViJHQNijxl38Yy648SoN%2FQckdod12P0lK08U3Vw9ESRR6nXfTdQoLjrUv5DncIp1yv252Yp9bjxZcWDMZOBCtEXxMWfJSZjllGE%2FklL%2BhBioWtwP3qedbRRc4hWoj1UK1fAaV2DGG7SQ%2BhYfKnwGmjLI7F9rW1L8KUxEHn1n9nDra6VWIV%2F6TUppSVQAHHoLDPkwZkiMdOlRpwY5EUg7Z6sToYZV30QioyMIEgG%2Bo1k%2BPqdToiGz1Mo%2FpuzxHa0dWkk947H9OSleoSfVFcYOUr3zoxZuIW3OLTP3XMIGiD4tQ%2BqGcMlnBWN1F0FrHicsajEgOVozeRAzis1x%2FozrwH3TdMJyj7LwGOqUB2rMALNWuEk4rVadCCwzAfkqqBLoQnrAt8sNGkoq6Psw819g36kbt3SZLVoC5uYDYg2LwnnqeM%2Biauu0UqVdAQP7S9D048OFzG8J8UQhmA221q3%2B0pLir9P7R3aUpbJEdf1Rs2D6S74McUPoCs7RAOKTW0I7bXh84otN9RmDg6Tk%2BOuT%2FtngxOeAeVTkSAwMrApyyUXFLRkSu0odGOTYWetlgJWEC&X-Amz-Signature=9d90b03e4266e3bb45a7bb86077832e1851b725ddad0a9779795749f912d078b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634M5ENXP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBrJ7tUBIOxXXpF0i83t38hAxaDrdynqwgHv32tHFrXyAiEAuy1Wmcz3ur7AYYcGoWDl%2B%2BM79M03dtL9%2FaHmxKnDAlkqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLFtWGkH3TF2I9BzgyrcAz%2F2QazLo3EmbxeNYwM2%2BIaJ0ecJo1awi0w5kzgmhze3%2FC694wgjYXMCwO3tBVu0wLxRSCmYFvZsepiJLa3rFhHUp%2Bf5hb1DafewKmwReb3OVNNct7OSTXxtdMgM8C2B3n2r%2FediOVXLTU15lknBf6fLrQH%2FuxKamcFvZUVcxa63pIAGzpxA8EGueBgm7eZ04SUHAmq4C9aRykbwkiYa8%2FX0H3mF3I1QosD4%2BSGpAXV07X4IY1VsUve2KhJGDPganEP2dY6%2BzXV%2BB5Cod8LvNya%2FT6ELrgFlAamViJHQNijxl38Yy648SoN%2FQckdod12P0lK08U3Vw9ESRR6nXfTdQoLjrUv5DncIp1yv252Yp9bjxZcWDMZOBCtEXxMWfJSZjllGE%2FklL%2BhBioWtwP3qedbRRc4hWoj1UK1fAaV2DGG7SQ%2BhYfKnwGmjLI7F9rW1L8KUxEHn1n9nDra6VWIV%2F6TUppSVQAHHoLDPkwZkiMdOlRpwY5EUg7Z6sToYZV30QioyMIEgG%2Bo1k%2BPqdToiGz1Mo%2FpuzxHa0dWkk947H9OSleoSfVFcYOUr3zoxZuIW3OLTP3XMIGiD4tQ%2BqGcMlnBWN1F0FrHicsajEgOVozeRAzis1x%2FozrwH3TdMJyj7LwGOqUB2rMALNWuEk4rVadCCwzAfkqqBLoQnrAt8sNGkoq6Psw819g36kbt3SZLVoC5uYDYg2LwnnqeM%2Biauu0UqVdAQP7S9D048OFzG8J8UQhmA221q3%2B0pLir9P7R3aUpbJEdf1Rs2D6S74McUPoCs7RAOKTW0I7bXh84otN9RmDg6Tk%2BOuT%2FtngxOeAeVTkSAwMrApyyUXFLRkSu0odGOTYWetlgJWEC&X-Amz-Signature=1d114303729346c8c87d78f109695d6f0a68bdf2e43306a7abdb6bc45d402f97&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2SU4ZZZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBQfob5oGrVCw4dWe1Moq%2BZntKi%2FiM4ADQwmibz9F8kaAiEAxsvUq5oT6GZlcnqvbTRkncTJUNC2oAoJU7JBHXbMBIgqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBLj%2Fsio5xAhNUKPxSrcA4bUKbuEB8A65wBpZ%2FHXA7gZBmR25U6mx1VcXsdUICBQkj2eItK4NykVOUGERrBsS4QHTp9TGtHwVDxAibJ944ZKGG3dyLqM8dMkH2WZl2HNnMFt9bEkoOC%2F1rHJVT%2Bknz0Ock56x9mNRjw2WbyahtV4DUQAcsp6XXKU9IKZ7FZQ%2BrIxKtHSZhgNQyfFlQxL2kRUTdwrFBvl%2B79%2FrrAntAY1R2Aqq6N97Zv04kX82S4pLqlaoH519%2BkhIQ%2FYnITIdGH%2Bzq5%2BV0Gei8GWexg%2B8e04wux1oCGSn%2B06%2FAqziLPlAz9H5ur56D3%2BptQVPLV1Nx0PWDhoAl1w%2BlrfXhJYNX3cItvxZecKc34vVr7DsXQxWRMMsB7x4Q1AJUVg%2Bju10S%2FwGE1QjepMOPMNyFhMR2SWgq2XSunXTP0r%2BWniehzUvQy33YsKOYaloHxp8C8Hv4FEVmp0ntpPpigLjVRYuVgnG7%2BH%2F80MElqj%2FvnAvYbIc5Tupp%2F0QuTeVaLbeG6%2B5vuyaagyn3aQRlxSpZXGuuHFnQ%2Bk2A4o8SOKCsTkJQX47dCHANW%2F9VR5%2BPlEgEDysVx8CI3u%2BW%2BtiMoTMy8wKKDBTzEBWt7qTdPHpNyq4PuYiSxRr4zZnk59uFTvMKaj7LwGOqUBcxymuSNql7SuEZrckZulGJ8gc%2FWKCoAs0OO4R22dABKEy%2FXjFH2qGOL3nDy%2FATD%2BPBz7u1aw9CKMFSX%2FtxdMmeozR%2FUx0c8N1A%2FwpI0sxA1ickzuv8VN8VhZoG20lMSpoglzWMxS65ZlOSLnUitk3ShNEZKLlpqyeuNse7z%2FfJFthKp5WaptTz7DuWID7KpP3isgvx47o43EnUwBKHCBV3kRp%2BHJ&X-Amz-Signature=33cd851cdf414c5031b021297074ef773af54f1a17745664960d8221e3b32c19&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2SU4ZZZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBQfob5oGrVCw4dWe1Moq%2BZntKi%2FiM4ADQwmibz9F8kaAiEAxsvUq5oT6GZlcnqvbTRkncTJUNC2oAoJU7JBHXbMBIgqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBLj%2Fsio5xAhNUKPxSrcA4bUKbuEB8A65wBpZ%2FHXA7gZBmR25U6mx1VcXsdUICBQkj2eItK4NykVOUGERrBsS4QHTp9TGtHwVDxAibJ944ZKGG3dyLqM8dMkH2WZl2HNnMFt9bEkoOC%2F1rHJVT%2Bknz0Ock56x9mNRjw2WbyahtV4DUQAcsp6XXKU9IKZ7FZQ%2BrIxKtHSZhgNQyfFlQxL2kRUTdwrFBvl%2B79%2FrrAntAY1R2Aqq6N97Zv04kX82S4pLqlaoH519%2BkhIQ%2FYnITIdGH%2Bzq5%2BV0Gei8GWexg%2B8e04wux1oCGSn%2B06%2FAqziLPlAz9H5ur56D3%2BptQVPLV1Nx0PWDhoAl1w%2BlrfXhJYNX3cItvxZecKc34vVr7DsXQxWRMMsB7x4Q1AJUVg%2Bju10S%2FwGE1QjepMOPMNyFhMR2SWgq2XSunXTP0r%2BWniehzUvQy33YsKOYaloHxp8C8Hv4FEVmp0ntpPpigLjVRYuVgnG7%2BH%2F80MElqj%2FvnAvYbIc5Tupp%2F0QuTeVaLbeG6%2B5vuyaagyn3aQRlxSpZXGuuHFnQ%2Bk2A4o8SOKCsTkJQX47dCHANW%2F9VR5%2BPlEgEDysVx8CI3u%2BW%2BtiMoTMy8wKKDBTzEBWt7qTdPHpNyq4PuYiSxRr4zZnk59uFTvMKaj7LwGOqUBcxymuSNql7SuEZrckZulGJ8gc%2FWKCoAs0OO4R22dABKEy%2FXjFH2qGOL3nDy%2FATD%2BPBz7u1aw9CKMFSX%2FtxdMmeozR%2FUx0c8N1A%2FwpI0sxA1ickzuv8VN8VhZoG20lMSpoglzWMxS65ZlOSLnUitk3ShNEZKLlpqyeuNse7z%2FfJFthKp5WaptTz7DuWID7KpP3isgvx47o43EnUwBKHCBV3kRp%2BHJ&X-Amz-Signature=7ab0b9e6b64600929cba7eaee49fb58aaccff56b6b820ca4689f33991cea3d63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634M5ENXP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBrJ7tUBIOxXXpF0i83t38hAxaDrdynqwgHv32tHFrXyAiEAuy1Wmcz3ur7AYYcGoWDl%2B%2BM79M03dtL9%2FaHmxKnDAlkqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLFtWGkH3TF2I9BzgyrcAz%2F2QazLo3EmbxeNYwM2%2BIaJ0ecJo1awi0w5kzgmhze3%2FC694wgjYXMCwO3tBVu0wLxRSCmYFvZsepiJLa3rFhHUp%2Bf5hb1DafewKmwReb3OVNNct7OSTXxtdMgM8C2B3n2r%2FediOVXLTU15lknBf6fLrQH%2FuxKamcFvZUVcxa63pIAGzpxA8EGueBgm7eZ04SUHAmq4C9aRykbwkiYa8%2FX0H3mF3I1QosD4%2BSGpAXV07X4IY1VsUve2KhJGDPganEP2dY6%2BzXV%2BB5Cod8LvNya%2FT6ELrgFlAamViJHQNijxl38Yy648SoN%2FQckdod12P0lK08U3Vw9ESRR6nXfTdQoLjrUv5DncIp1yv252Yp9bjxZcWDMZOBCtEXxMWfJSZjllGE%2FklL%2BhBioWtwP3qedbRRc4hWoj1UK1fAaV2DGG7SQ%2BhYfKnwGmjLI7F9rW1L8KUxEHn1n9nDra6VWIV%2F6TUppSVQAHHoLDPkwZkiMdOlRpwY5EUg7Z6sToYZV30QioyMIEgG%2Bo1k%2BPqdToiGz1Mo%2FpuzxHa0dWkk947H9OSleoSfVFcYOUr3zoxZuIW3OLTP3XMIGiD4tQ%2BqGcMlnBWN1F0FrHicsajEgOVozeRAzis1x%2FozrwH3TdMJyj7LwGOqUB2rMALNWuEk4rVadCCwzAfkqqBLoQnrAt8sNGkoq6Psw819g36kbt3SZLVoC5uYDYg2LwnnqeM%2Biauu0UqVdAQP7S9D048OFzG8J8UQhmA221q3%2B0pLir9P7R3aUpbJEdf1Rs2D6S74McUPoCs7RAOKTW0I7bXh84otN9RmDg6Tk%2BOuT%2FtngxOeAeVTkSAwMrApyyUXFLRkSu0odGOTYWetlgJWEC&X-Amz-Signature=f8fafc775fbc041e003cf60e88a263eeb66a06230b82569265bfa0121f65c77d&X-Amz-SignedHeaders=host&x-id=GetObject)
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