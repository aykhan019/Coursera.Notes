

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRR4H6JX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsFXslrhrGqEtsfLJc1utGCjTJ8KRGXmbZvP3yYXAjdAiBqg5BxlmZPu8AtmtUVLyWGG5RS1RXB9O2cNYW11sqK8iqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzVFMBNRcAnClm1fOKtwD8Z2EMudlubfiS7i0WqHCEGufW6i%2BAQuxOxUirVGGp9qJxV6N41YCveNTUs5DRmZFvjd2HSYz5rzQqgyrYrnb7tHv8CVTkfn0nyrahfYeiE%2FJzf8qgTgVtlwf7ASYamBcpGfGoKwPUge5a7froFX%2FHeFNf06hELNeRvz%2Fw04yOvKl1BeD8OiiWEIsWWqiLVhGEj9vZc2jPSQpNieGMe3RhxF%2Fge4dJv66RKEx5ikLC7dzASw8mb%2B2DcCVDZ969%2FycRE9X5DPUiNvs4kTVjBwjraZw%2BSqrsUKlu2CRvOk0Buc32b%2BxkPUVUxFOUKoXIhVGmKSLsm%2BbmjFOhnHx%2FetJxR4%2BUML%2BnJB8K8lc%2FTSYc%2BjqzvgkZQ7hY%2Bh%2BZ6ZXK40faVrA3sWDJplwKftAZrn%2BfnH0vQGWRRsUNA1UTnRv3MKrWREUbB6n%2Bx1eiyfX7ubp5jnKnyFTU3jaZTAff1N9a6RddMFcvbGs1kE0j%2FMcup1wrJtFXCZuyN3s2gbts6QXTOCCXuIPUP%2FZL3MfkOdERHLegfY8%2BG3quae%2BZyYpjL7vjKQgND3vHdLq2AhRFe2vR4bLEjEoS0BIeG39fDSBmIYwAStDzNYcjTFOMdVXyHGqwi4dvIWcOk2zCLQwoNfyvAY6pgEF1hmuJfd1%2FxMZcQCDYr3CgZRfnzgAGclx8LAT8G6HPLGdyrxWFiqRWzLW6sL8jcpB%2B5Il1G%2BMvxgC%2FyyN1D9ijzNDfR1K4EyZbKu1FtN%2BzxkEeIBla%2B90GLddQdFkETJQgHnBdYWHBFXi9dBdWinMafIzjpCzdIcOkhOlqM5bCMvk3O16R6jVOm5IZaknYtK5cGr1CjUvZJ%2BBtGtIkAINU28x1O4R&X-Amz-Signature=a6817217c23cd2fe8ee68927b65c5bddecf33d37ae26f86c2100ddb3c6e95d04&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRR4H6JX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsFXslrhrGqEtsfLJc1utGCjTJ8KRGXmbZvP3yYXAjdAiBqg5BxlmZPu8AtmtUVLyWGG5RS1RXB9O2cNYW11sqK8iqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzVFMBNRcAnClm1fOKtwD8Z2EMudlubfiS7i0WqHCEGufW6i%2BAQuxOxUirVGGp9qJxV6N41YCveNTUs5DRmZFvjd2HSYz5rzQqgyrYrnb7tHv8CVTkfn0nyrahfYeiE%2FJzf8qgTgVtlwf7ASYamBcpGfGoKwPUge5a7froFX%2FHeFNf06hELNeRvz%2Fw04yOvKl1BeD8OiiWEIsWWqiLVhGEj9vZc2jPSQpNieGMe3RhxF%2Fge4dJv66RKEx5ikLC7dzASw8mb%2B2DcCVDZ969%2FycRE9X5DPUiNvs4kTVjBwjraZw%2BSqrsUKlu2CRvOk0Buc32b%2BxkPUVUxFOUKoXIhVGmKSLsm%2BbmjFOhnHx%2FetJxR4%2BUML%2BnJB8K8lc%2FTSYc%2BjqzvgkZQ7hY%2Bh%2BZ6ZXK40faVrA3sWDJplwKftAZrn%2BfnH0vQGWRRsUNA1UTnRv3MKrWREUbB6n%2Bx1eiyfX7ubp5jnKnyFTU3jaZTAff1N9a6RddMFcvbGs1kE0j%2FMcup1wrJtFXCZuyN3s2gbts6QXTOCCXuIPUP%2FZL3MfkOdERHLegfY8%2BG3quae%2BZyYpjL7vjKQgND3vHdLq2AhRFe2vR4bLEjEoS0BIeG39fDSBmIYwAStDzNYcjTFOMdVXyHGqwi4dvIWcOk2zCLQwoNfyvAY6pgEF1hmuJfd1%2FxMZcQCDYr3CgZRfnzgAGclx8LAT8G6HPLGdyrxWFiqRWzLW6sL8jcpB%2B5Il1G%2BMvxgC%2FyyN1D9ijzNDfR1K4EyZbKu1FtN%2BzxkEeIBla%2B90GLddQdFkETJQgHnBdYWHBFXi9dBdWinMafIzjpCzdIcOkhOlqM5bCMvk3O16R6jVOm5IZaknYtK5cGr1CjUvZJ%2BBtGtIkAINU28x1O4R&X-Amz-Signature=09877a960ab7819104b84cc708930344ad8f37eeb418e00be6dcd07ddeb41b06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRR4H6JX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsFXslrhrGqEtsfLJc1utGCjTJ8KRGXmbZvP3yYXAjdAiBqg5BxlmZPu8AtmtUVLyWGG5RS1RXB9O2cNYW11sqK8iqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzVFMBNRcAnClm1fOKtwD8Z2EMudlubfiS7i0WqHCEGufW6i%2BAQuxOxUirVGGp9qJxV6N41YCveNTUs5DRmZFvjd2HSYz5rzQqgyrYrnb7tHv8CVTkfn0nyrahfYeiE%2FJzf8qgTgVtlwf7ASYamBcpGfGoKwPUge5a7froFX%2FHeFNf06hELNeRvz%2Fw04yOvKl1BeD8OiiWEIsWWqiLVhGEj9vZc2jPSQpNieGMe3RhxF%2Fge4dJv66RKEx5ikLC7dzASw8mb%2B2DcCVDZ969%2FycRE9X5DPUiNvs4kTVjBwjraZw%2BSqrsUKlu2CRvOk0Buc32b%2BxkPUVUxFOUKoXIhVGmKSLsm%2BbmjFOhnHx%2FetJxR4%2BUML%2BnJB8K8lc%2FTSYc%2BjqzvgkZQ7hY%2Bh%2BZ6ZXK40faVrA3sWDJplwKftAZrn%2BfnH0vQGWRRsUNA1UTnRv3MKrWREUbB6n%2Bx1eiyfX7ubp5jnKnyFTU3jaZTAff1N9a6RddMFcvbGs1kE0j%2FMcup1wrJtFXCZuyN3s2gbts6QXTOCCXuIPUP%2FZL3MfkOdERHLegfY8%2BG3quae%2BZyYpjL7vjKQgND3vHdLq2AhRFe2vR4bLEjEoS0BIeG39fDSBmIYwAStDzNYcjTFOMdVXyHGqwi4dvIWcOk2zCLQwoNfyvAY6pgEF1hmuJfd1%2FxMZcQCDYr3CgZRfnzgAGclx8LAT8G6HPLGdyrxWFiqRWzLW6sL8jcpB%2B5Il1G%2BMvxgC%2FyyN1D9ijzNDfR1K4EyZbKu1FtN%2BzxkEeIBla%2B90GLddQdFkETJQgHnBdYWHBFXi9dBdWinMafIzjpCzdIcOkhOlqM5bCMvk3O16R6jVOm5IZaknYtK5cGr1CjUvZJ%2BBtGtIkAINU28x1O4R&X-Amz-Signature=39093826c33e5d373da7787e5e7dc149d9a1a572a542c275713d74990694c31f&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRJLZND%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEDZbAN43tevoUcUW2y%2FkF1jVmuntODA4%2F1pkb2%2Bb4JjAiAVXRE2XnYRA%2BHO7dPlxT7ovjosFgbiIIgXSlekhHjEJyqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvMF89LyNbiZ4CMgNKtwDF4j3wzgTfKQX6XPTkGl0TWzb9dXo1uytDwPUwtuOD1r0D7uqBNMi9kfYUvejhU6jeGhfu7CIStnaop1Cg9j%2Fv8l%2BbJMgDhuH8qgu5HQbbxHY%2FkbJbJ4sBOqXS%2FEeHJI9aEuUtTzZHo8XhW%2F9kbVVbdGW3nhkjCJtHV6mdrBsOBM%2BB%2BsoG00fSNt8nW6pf%2F4pnhGKGVHbU1%2FcVHd%2Fgn2AEYeHa7HTjISt02zOJHCpXz2BBOioo757YGtNo1%2FqPH7XFP2VoeKuVdtjRUtIXFAS9eGaKeSrlDo6El2fOVWOazSxL440ouXcYorw78Q26Y4lyTPF5OypM2nehAMSIHBxzz9NjD2ewD7NzE6Q%2BwdxmreE8gbPMJWmLydg%2BsvQo15iiN1PAEbZU7kMDfFwRLwkV4tXFWUAdIJXYypV5zWtHx25bC%2BaA0eUDsZ0oFQvuRvEsFYm2%2FJdEGDjgXxQ7BkC9Ndhn7qQsaCur8PNdC1q7%2BkUSivi1XnwnJi%2Br38IdVnDq60QUQzgzWZDZu6S3w2lulU4Ikfjgcivjlxjcw6EdUwt2pihLr4yXyWkME7bKm7R%2BXGMK5nE1eheC%2F18B0Qfa4vJOgV5QKbuBT4O01NX8VntJp8UrA1OBEhHSaEw3dbyvAY6pgEqiGk9ugC1EwYuHJ%2BZYFZAkfI%2FZKr0jOfyLZM5L%2B7I%2B3vz41hVwwpLMcG8p3bpRt5IyKX1iXrspfB5KLBIF5sT8xmbdnKz09a%2F6pex7yINEzpGfB%2Ffnx8vLd9Aag6jLDtDYBYWzyDWU08E5YDTUvUPB8udOKSTrUn4EmLz3jwLYLaAAZJLP%2FEp9BzNA%2BZZnsoP2toXk6mAtRzQOUyZAJMeVDDodlcQ&X-Amz-Signature=9b2a73956f030efd20035e241555ca7d6d3e7ef95f10104f45edc2f4e8c9c77a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHRJLZND%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEDZbAN43tevoUcUW2y%2FkF1jVmuntODA4%2F1pkb2%2Bb4JjAiAVXRE2XnYRA%2BHO7dPlxT7ovjosFgbiIIgXSlekhHjEJyqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvMF89LyNbiZ4CMgNKtwDF4j3wzgTfKQX6XPTkGl0TWzb9dXo1uytDwPUwtuOD1r0D7uqBNMi9kfYUvejhU6jeGhfu7CIStnaop1Cg9j%2Fv8l%2BbJMgDhuH8qgu5HQbbxHY%2FkbJbJ4sBOqXS%2FEeHJI9aEuUtTzZHo8XhW%2F9kbVVbdGW3nhkjCJtHV6mdrBsOBM%2BB%2BsoG00fSNt8nW6pf%2F4pnhGKGVHbU1%2FcVHd%2Fgn2AEYeHa7HTjISt02zOJHCpXz2BBOioo757YGtNo1%2FqPH7XFP2VoeKuVdtjRUtIXFAS9eGaKeSrlDo6El2fOVWOazSxL440ouXcYorw78Q26Y4lyTPF5OypM2nehAMSIHBxzz9NjD2ewD7NzE6Q%2BwdxmreE8gbPMJWmLydg%2BsvQo15iiN1PAEbZU7kMDfFwRLwkV4tXFWUAdIJXYypV5zWtHx25bC%2BaA0eUDsZ0oFQvuRvEsFYm2%2FJdEGDjgXxQ7BkC9Ndhn7qQsaCur8PNdC1q7%2BkUSivi1XnwnJi%2Br38IdVnDq60QUQzgzWZDZu6S3w2lulU4Ikfjgcivjlxjcw6EdUwt2pihLr4yXyWkME7bKm7R%2BXGMK5nE1eheC%2F18B0Qfa4vJOgV5QKbuBT4O01NX8VntJp8UrA1OBEhHSaEw3dbyvAY6pgEqiGk9ugC1EwYuHJ%2BZYFZAkfI%2FZKr0jOfyLZM5L%2B7I%2B3vz41hVwwpLMcG8p3bpRt5IyKX1iXrspfB5KLBIF5sT8xmbdnKz09a%2F6pex7yINEzpGfB%2Ffnx8vLd9Aag6jLDtDYBYWzyDWU08E5YDTUvUPB8udOKSTrUn4EmLz3jwLYLaAAZJLP%2FEp9BzNA%2BZZnsoP2toXk6mAtRzQOUyZAJMeVDDodlcQ&X-Amz-Signature=d243083f0549b988d75542c73baf9a7fc5be961f6cac3baa8e4c0de4b274cbec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRR4H6JX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFsFXslrhrGqEtsfLJc1utGCjTJ8KRGXmbZvP3yYXAjdAiBqg5BxlmZPu8AtmtUVLyWGG5RS1RXB9O2cNYW11sqK8iqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzVFMBNRcAnClm1fOKtwD8Z2EMudlubfiS7i0WqHCEGufW6i%2BAQuxOxUirVGGp9qJxV6N41YCveNTUs5DRmZFvjd2HSYz5rzQqgyrYrnb7tHv8CVTkfn0nyrahfYeiE%2FJzf8qgTgVtlwf7ASYamBcpGfGoKwPUge5a7froFX%2FHeFNf06hELNeRvz%2Fw04yOvKl1BeD8OiiWEIsWWqiLVhGEj9vZc2jPSQpNieGMe3RhxF%2Fge4dJv66RKEx5ikLC7dzASw8mb%2B2DcCVDZ969%2FycRE9X5DPUiNvs4kTVjBwjraZw%2BSqrsUKlu2CRvOk0Buc32b%2BxkPUVUxFOUKoXIhVGmKSLsm%2BbmjFOhnHx%2FetJxR4%2BUML%2BnJB8K8lc%2FTSYc%2BjqzvgkZQ7hY%2Bh%2BZ6ZXK40faVrA3sWDJplwKftAZrn%2BfnH0vQGWRRsUNA1UTnRv3MKrWREUbB6n%2Bx1eiyfX7ubp5jnKnyFTU3jaZTAff1N9a6RddMFcvbGs1kE0j%2FMcup1wrJtFXCZuyN3s2gbts6QXTOCCXuIPUP%2FZL3MfkOdERHLegfY8%2BG3quae%2BZyYpjL7vjKQgND3vHdLq2AhRFe2vR4bLEjEoS0BIeG39fDSBmIYwAStDzNYcjTFOMdVXyHGqwi4dvIWcOk2zCLQwoNfyvAY6pgEF1hmuJfd1%2FxMZcQCDYr3CgZRfnzgAGclx8LAT8G6HPLGdyrxWFiqRWzLW6sL8jcpB%2B5Il1G%2BMvxgC%2FyyN1D9ijzNDfR1K4EyZbKu1FtN%2BzxkEeIBla%2B90GLddQdFkETJQgHnBdYWHBFXi9dBdWinMafIzjpCzdIcOkhOlqM5bCMvk3O16R6jVOm5IZaknYtK5cGr1CjUvZJ%2BBtGtIkAINU28x1O4R&X-Amz-Signature=b9d6b67fd357750ba57b4baa9a933c0edd4d843253134188a5c30cfcc31d7488&X-Amz-SignedHeaders=host&x-id=GetObject)
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