

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643TTHOFD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIH2IzWvP6BAEtHVIYN7CPfDex9LzU6mOVd%2Fu542KZBlpAiBWg9kw8zbiUBSgfSyML037%2BhPJfPfdV0RZTTrS6m7AdyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKpyelEOorxoc31IFKtwDVXHn%2BTBJVguGcVwdGf2pUJ1YH1WjWoblJ14JDd9hIax2LGHYM2xMTy9jZA3qtKUvCtuB8Pgumk4l6Nr1qamayY8vo0pBqlEaUGcUNdytb0dQcucR32SJpbAg%2FiB8R36%2BGqTdusP8meN%2BaSVQMOqXw7jETx9hTdJrUxRcAg5icES%2FCICDPxoWe69iTca7crQJNvbNjkVgZfEpDrH1DaS79UdDChyqNEa21h4tHFhIIBU7puSSew8%2F5oSXLW5CF%2B1N8DWUBDwVbaN%2FC6YC%2BgZ2ElZkexo1q%2FylYvIyjPZjkO%2BZYBGxbv7uSuNiAtTR6%2FFbe0USRK0NlyAgP3i9EEn8Qe39y6MJoTxesYgIpiFb7OGlt2w9Hta%2BVxxYQU7MTvuFPTTKRCLRT5BSwiuvau5tjv3MONoBrZ2tr0RyAm3AXmBT2Ana1OXrVCd3YFgBcnQrGyVTsCpJYDecbomxzOLLNZXJbfCw%2BNXf0xGB02dnTBwhp7cpahffLhbvVQHB72l3znOrYRADhCcCre9faTaUhzY0B97Kxk0xYel%2F0sPBrqzwDjOEWP9TDl4uORJtYDJFSt2pOrpeEA%2BDSoSR3ZgZBAFEI%2FRCa9JCqFz5TDiIF7u0VXOjOlu9zsA37REwrZDnvAY6pgHAEl8G81n5mECbT5byvmDSNqg%2FO86T%2BTAn4Ea3tLTaGGMSbHz%2BYZdt62Qv1ZSef%2BzyJV37Fqk1KXmVVcnE3sY2EIaFh9D%2BpdUpR2LD3PPxe696YJuA0vKhzodAe20itO9c0Un0Wqa1abdLzHLWfw7%2F5Gr1VPYQ%2BosCX6EDGvXqEbw8ui%2BcOWPSF%2FBrFGjm503cGdX1nVrtBkwO%2FSl6Pv45pj4DrGAM&X-Amz-Signature=067c3a8ec079631ea73cd3e3fb6648b05f26744f5a1e4ee5d48fbb6554b1785e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643TTHOFD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIH2IzWvP6BAEtHVIYN7CPfDex9LzU6mOVd%2Fu542KZBlpAiBWg9kw8zbiUBSgfSyML037%2BhPJfPfdV0RZTTrS6m7AdyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKpyelEOorxoc31IFKtwDVXHn%2BTBJVguGcVwdGf2pUJ1YH1WjWoblJ14JDd9hIax2LGHYM2xMTy9jZA3qtKUvCtuB8Pgumk4l6Nr1qamayY8vo0pBqlEaUGcUNdytb0dQcucR32SJpbAg%2FiB8R36%2BGqTdusP8meN%2BaSVQMOqXw7jETx9hTdJrUxRcAg5icES%2FCICDPxoWe69iTca7crQJNvbNjkVgZfEpDrH1DaS79UdDChyqNEa21h4tHFhIIBU7puSSew8%2F5oSXLW5CF%2B1N8DWUBDwVbaN%2FC6YC%2BgZ2ElZkexo1q%2FylYvIyjPZjkO%2BZYBGxbv7uSuNiAtTR6%2FFbe0USRK0NlyAgP3i9EEn8Qe39y6MJoTxesYgIpiFb7OGlt2w9Hta%2BVxxYQU7MTvuFPTTKRCLRT5BSwiuvau5tjv3MONoBrZ2tr0RyAm3AXmBT2Ana1OXrVCd3YFgBcnQrGyVTsCpJYDecbomxzOLLNZXJbfCw%2BNXf0xGB02dnTBwhp7cpahffLhbvVQHB72l3znOrYRADhCcCre9faTaUhzY0B97Kxk0xYel%2F0sPBrqzwDjOEWP9TDl4uORJtYDJFSt2pOrpeEA%2BDSoSR3ZgZBAFEI%2FRCa9JCqFz5TDiIF7u0VXOjOlu9zsA37REwrZDnvAY6pgHAEl8G81n5mECbT5byvmDSNqg%2FO86T%2BTAn4Ea3tLTaGGMSbHz%2BYZdt62Qv1ZSef%2BzyJV37Fqk1KXmVVcnE3sY2EIaFh9D%2BpdUpR2LD3PPxe696YJuA0vKhzodAe20itO9c0Un0Wqa1abdLzHLWfw7%2F5Gr1VPYQ%2BosCX6EDGvXqEbw8ui%2BcOWPSF%2FBrFGjm503cGdX1nVrtBkwO%2FSl6Pv45pj4DrGAM&X-Amz-Signature=3ee71d4df1a89eadc47eee4327f471c43ff9727cb3aaa6fd31e1f669cc46cc29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643TTHOFD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIH2IzWvP6BAEtHVIYN7CPfDex9LzU6mOVd%2Fu542KZBlpAiBWg9kw8zbiUBSgfSyML037%2BhPJfPfdV0RZTTrS6m7AdyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKpyelEOorxoc31IFKtwDVXHn%2BTBJVguGcVwdGf2pUJ1YH1WjWoblJ14JDd9hIax2LGHYM2xMTy9jZA3qtKUvCtuB8Pgumk4l6Nr1qamayY8vo0pBqlEaUGcUNdytb0dQcucR32SJpbAg%2FiB8R36%2BGqTdusP8meN%2BaSVQMOqXw7jETx9hTdJrUxRcAg5icES%2FCICDPxoWe69iTca7crQJNvbNjkVgZfEpDrH1DaS79UdDChyqNEa21h4tHFhIIBU7puSSew8%2F5oSXLW5CF%2B1N8DWUBDwVbaN%2FC6YC%2BgZ2ElZkexo1q%2FylYvIyjPZjkO%2BZYBGxbv7uSuNiAtTR6%2FFbe0USRK0NlyAgP3i9EEn8Qe39y6MJoTxesYgIpiFb7OGlt2w9Hta%2BVxxYQU7MTvuFPTTKRCLRT5BSwiuvau5tjv3MONoBrZ2tr0RyAm3AXmBT2Ana1OXrVCd3YFgBcnQrGyVTsCpJYDecbomxzOLLNZXJbfCw%2BNXf0xGB02dnTBwhp7cpahffLhbvVQHB72l3znOrYRADhCcCre9faTaUhzY0B97Kxk0xYel%2F0sPBrqzwDjOEWP9TDl4uORJtYDJFSt2pOrpeEA%2BDSoSR3ZgZBAFEI%2FRCa9JCqFz5TDiIF7u0VXOjOlu9zsA37REwrZDnvAY6pgHAEl8G81n5mECbT5byvmDSNqg%2FO86T%2BTAn4Ea3tLTaGGMSbHz%2BYZdt62Qv1ZSef%2BzyJV37Fqk1KXmVVcnE3sY2EIaFh9D%2BpdUpR2LD3PPxe696YJuA0vKhzodAe20itO9c0Un0Wqa1abdLzHLWfw7%2F5Gr1VPYQ%2BosCX6EDGvXqEbw8ui%2BcOWPSF%2FBrFGjm503cGdX1nVrtBkwO%2FSl6Pv45pj4DrGAM&X-Amz-Signature=d9bfd08d2eddc291fe142b688fafb232e0f1115e8d5bbf0927a0989e78e42bc7&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624LRQGVM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCICBGuz0TZVPEi6S8yt7dmZe6Az437Sfb99V%2BGQscRfczAiBUDYnlEkBLudsKT0Em%2BN%2FH4l4miLjkzAQBcKdIYcwsBiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnbjpvAx%2BYYgJazRqKtwDVeirmJu4DmR41JwOyuQ3hCgyszxGEtj1hTFhypqwtG%2FCzKzeJBWQF3WrA4rGjlwYEaEZZr3UA1x%2F9OkJAj%2B8Vz%2Fh34hcDLBOAhekdX%2BDuDRykD8gm0cQ6FP83Grt5Mm0AwSylwnx%2BpVv6Iee6I4qUCBDU8lXIq5cv%2BY7sW2fcpSfp3Qw71iAXb4NoEqZcO1Rf5fAfdYWxHz%2BsgsZDzGwIMyC7j%2FVkUMP8CwDkGaWs%2FS3cWX5V3Qq3bNrevQ74LpOHjRgqmrSyXpDLoCNMCeiwNfNgGaZQWnD6%2B4TL2SJmcQ81xODr8rWqKnpENfopr49itRwJ%2FD0qvsy6na6iHlilQKMTteXdzLB5wsK88Z2R5IlPRU0Smj1YGKA6W5SzCoDAoiqI%2BodTPVId%2FpbM3X1BTolDmNjm0a4tMM3QSY1kbo6OCaIbX5Q6rVHV1%2FVnANed13eJ%2FjczLDj01sqDDYCQGuCmLiA7m7duZm3cMQPRjK9wR8bXHhWUWaYVMkkgopiOekZ5UZc82VOMy50SMvCI6gYla49WmBdLJurrlxVgdTsiF0fBidNCoRp60sKtBaf3lUZHGYqiTME2PyS4I1zC6EioEOTecz%2FZdMYTKk8spU5qOJRL%2Fh%2FdvQ6fxUwuJDnvAY6pgE5gE7g3QR9Gs4MWMUffKa0EvJuFC%2FsLXu1GPR3LAkGDkjTz3M%2B%2FuHegA05cjBpZLz1RvQ0Sbfls%2BHAMnx3uurTUYpKvEAzAwRmo%2B8X7nNkhazIeEkCNnnq9za8iWjllW94emBCDrHmr9ZWES7nPnfHLF2PlDR68O7UKMLr1YwVp9PvQxnDyIxzw8movx%2FquMe5A9jk9ExWp6bnT01Esp1JfV7pkx8b&X-Amz-Signature=c3039a13924f4c73545c80b6e6185d67f91eae3c8525851ae743b3ea1f3445a8&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624LRQGVM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCICBGuz0TZVPEi6S8yt7dmZe6Az437Sfb99V%2BGQscRfczAiBUDYnlEkBLudsKT0Em%2BN%2FH4l4miLjkzAQBcKdIYcwsBiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnbjpvAx%2BYYgJazRqKtwDVeirmJu4DmR41JwOyuQ3hCgyszxGEtj1hTFhypqwtG%2FCzKzeJBWQF3WrA4rGjlwYEaEZZr3UA1x%2F9OkJAj%2B8Vz%2Fh34hcDLBOAhekdX%2BDuDRykD8gm0cQ6FP83Grt5Mm0AwSylwnx%2BpVv6Iee6I4qUCBDU8lXIq5cv%2BY7sW2fcpSfp3Qw71iAXb4NoEqZcO1Rf5fAfdYWxHz%2BsgsZDzGwIMyC7j%2FVkUMP8CwDkGaWs%2FS3cWX5V3Qq3bNrevQ74LpOHjRgqmrSyXpDLoCNMCeiwNfNgGaZQWnD6%2B4TL2SJmcQ81xODr8rWqKnpENfopr49itRwJ%2FD0qvsy6na6iHlilQKMTteXdzLB5wsK88Z2R5IlPRU0Smj1YGKA6W5SzCoDAoiqI%2BodTPVId%2FpbM3X1BTolDmNjm0a4tMM3QSY1kbo6OCaIbX5Q6rVHV1%2FVnANed13eJ%2FjczLDj01sqDDYCQGuCmLiA7m7duZm3cMQPRjK9wR8bXHhWUWaYVMkkgopiOekZ5UZc82VOMy50SMvCI6gYla49WmBdLJurrlxVgdTsiF0fBidNCoRp60sKtBaf3lUZHGYqiTME2PyS4I1zC6EioEOTecz%2FZdMYTKk8spU5qOJRL%2Fh%2FdvQ6fxUwuJDnvAY6pgE5gE7g3QR9Gs4MWMUffKa0EvJuFC%2FsLXu1GPR3LAkGDkjTz3M%2B%2FuHegA05cjBpZLz1RvQ0Sbfls%2BHAMnx3uurTUYpKvEAzAwRmo%2B8X7nNkhazIeEkCNnnq9za8iWjllW94emBCDrHmr9ZWES7nPnfHLF2PlDR68O7UKMLr1YwVp9PvQxnDyIxzw8movx%2FquMe5A9jk9ExWp6bnT01Esp1JfV7pkx8b&X-Amz-Signature=2c53ca77ed5843cddc8d956bbf3b812062d708438926d89d2ab2a9e0e30c2220&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643TTHOFD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJGMEQCIH2IzWvP6BAEtHVIYN7CPfDex9LzU6mOVd%2Fu542KZBlpAiBWg9kw8zbiUBSgfSyML037%2BhPJfPfdV0RZTTrS6m7AdyqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKpyelEOorxoc31IFKtwDVXHn%2BTBJVguGcVwdGf2pUJ1YH1WjWoblJ14JDd9hIax2LGHYM2xMTy9jZA3qtKUvCtuB8Pgumk4l6Nr1qamayY8vo0pBqlEaUGcUNdytb0dQcucR32SJpbAg%2FiB8R36%2BGqTdusP8meN%2BaSVQMOqXw7jETx9hTdJrUxRcAg5icES%2FCICDPxoWe69iTca7crQJNvbNjkVgZfEpDrH1DaS79UdDChyqNEa21h4tHFhIIBU7puSSew8%2F5oSXLW5CF%2B1N8DWUBDwVbaN%2FC6YC%2BgZ2ElZkexo1q%2FylYvIyjPZjkO%2BZYBGxbv7uSuNiAtTR6%2FFbe0USRK0NlyAgP3i9EEn8Qe39y6MJoTxesYgIpiFb7OGlt2w9Hta%2BVxxYQU7MTvuFPTTKRCLRT5BSwiuvau5tjv3MONoBrZ2tr0RyAm3AXmBT2Ana1OXrVCd3YFgBcnQrGyVTsCpJYDecbomxzOLLNZXJbfCw%2BNXf0xGB02dnTBwhp7cpahffLhbvVQHB72l3znOrYRADhCcCre9faTaUhzY0B97Kxk0xYel%2F0sPBrqzwDjOEWP9TDl4uORJtYDJFSt2pOrpeEA%2BDSoSR3ZgZBAFEI%2FRCa9JCqFz5TDiIF7u0VXOjOlu9zsA37REwrZDnvAY6pgHAEl8G81n5mECbT5byvmDSNqg%2FO86T%2BTAn4Ea3tLTaGGMSbHz%2BYZdt62Qv1ZSef%2BzyJV37Fqk1KXmVVcnE3sY2EIaFh9D%2BpdUpR2LD3PPxe696YJuA0vKhzodAe20itO9c0Un0Wqa1abdLzHLWfw7%2F5Gr1VPYQ%2BosCX6EDGvXqEbw8ui%2BcOWPSF%2FBrFGjm503cGdX1nVrtBkwO%2FSl6Pv45pj4DrGAM&X-Amz-Signature=cdeb5bf3d9b860ab675bc6510ac5d40aa71e8bb73f175f729c4926b52573889d&X-Amz-SignedHeaders=host&x-id=GetObject)
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