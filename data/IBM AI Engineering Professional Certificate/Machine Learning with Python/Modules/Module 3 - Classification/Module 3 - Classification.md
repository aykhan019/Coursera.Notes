

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753ACWGA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDIkoapMPQdPHezj2%2B8OWtji4kLgTLzdYpmnurWOcei3wIhAP54wl3SgAl1WOoDWdWE4h0rXEdE9ruTkf9e2x5yV%2B76Kv8DCHEQABoMNjM3NDIzMTgzODA1IgwVRVLjusBNX8IMOGgq3AMBQv8%2F4weMJqj9EN5pQKjMfVDyRP58eOkRkro2FZrqprK0mx7SnoaZWZLV3rVexM5dCSb%2F2lcCtDVG9yw87D7majyuA22hcrfONrIwa40m0jgfOs45C6lyVgnOjPQXCu4K906%2FPFFV1mZt8%2BQX9WOL5CNdP10ZbD7l7Fm7BjlY0pYlM4mbiUmHdwxqlVnxzuMAkdj3q407SstFDCpSUl3HJnwLDqB8YWDBxjbv2G4rJtHQWFMwJ5JeK2bV46Ksng0UcvFZMdFSCQBs3xTSiV2fhRoC4ugFwXt1io09%2BaWM5XMqf%2F8CaxbespMScGBOhpKaWhhG%2FCzpshv4rvC7lgBsKSzzyYh%2FSpWyIszsb8w01Ddj0Za7z2NfK8GqWxJY7UU5PeU%2Bbh%2Bu0UeXUDpfWrwxdbg2tnUPPjWeggEUIsW%2Fssfb%2BTBKybYhKhB7npOEZzLJKkXLBK9EP6fUj2kRJl3omoYtMy9GLtqBQol8E35E5mnw6D0VTzfW4piZZRn4h3GnTaLHaVSUGc6MhbYny3k8JXY2YHBzWfULJr7%2BGCPrVJ3UPYOXNCq5jfXef9QwCn99GV6PKQO1KWz%2BaXsazFfk4ynAYNqIb6%2FCvURBIEytVWare15xMbQFUJj9UTCF%2Bpa9BjqkAaSkoYzleYPUWLi7XB2JKq6NrKLIdb8AFaEHw1znDoyLSDsqhhZo%2BaQrHk1lXtCmT2SxZfqIZH4Y7YUUK7pZw4UcybAX9rX3vH48XFtyUKLeDM24uCmsf7Elrepen2BZoL5l%2BTkjRLfxYTRFbHnfAmN0aaOgkYMVRNz8qsy4tiz3sKbQBxsrJpCd6idKzN3UAdLv3ottLefsbK9iGQJ67l0jSB1Q&X-Amz-Signature=3c281af8219bc7be29613af98e6a22aed0b3f0ed8e48d361207cd0cb493b8674&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753ACWGA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDIkoapMPQdPHezj2%2B8OWtji4kLgTLzdYpmnurWOcei3wIhAP54wl3SgAl1WOoDWdWE4h0rXEdE9ruTkf9e2x5yV%2B76Kv8DCHEQABoMNjM3NDIzMTgzODA1IgwVRVLjusBNX8IMOGgq3AMBQv8%2F4weMJqj9EN5pQKjMfVDyRP58eOkRkro2FZrqprK0mx7SnoaZWZLV3rVexM5dCSb%2F2lcCtDVG9yw87D7majyuA22hcrfONrIwa40m0jgfOs45C6lyVgnOjPQXCu4K906%2FPFFV1mZt8%2BQX9WOL5CNdP10ZbD7l7Fm7BjlY0pYlM4mbiUmHdwxqlVnxzuMAkdj3q407SstFDCpSUl3HJnwLDqB8YWDBxjbv2G4rJtHQWFMwJ5JeK2bV46Ksng0UcvFZMdFSCQBs3xTSiV2fhRoC4ugFwXt1io09%2BaWM5XMqf%2F8CaxbespMScGBOhpKaWhhG%2FCzpshv4rvC7lgBsKSzzyYh%2FSpWyIszsb8w01Ddj0Za7z2NfK8GqWxJY7UU5PeU%2Bbh%2Bu0UeXUDpfWrwxdbg2tnUPPjWeggEUIsW%2Fssfb%2BTBKybYhKhB7npOEZzLJKkXLBK9EP6fUj2kRJl3omoYtMy9GLtqBQol8E35E5mnw6D0VTzfW4piZZRn4h3GnTaLHaVSUGc6MhbYny3k8JXY2YHBzWfULJr7%2BGCPrVJ3UPYOXNCq5jfXef9QwCn99GV6PKQO1KWz%2BaXsazFfk4ynAYNqIb6%2FCvURBIEytVWare15xMbQFUJj9UTCF%2Bpa9BjqkAaSkoYzleYPUWLi7XB2JKq6NrKLIdb8AFaEHw1znDoyLSDsqhhZo%2BaQrHk1lXtCmT2SxZfqIZH4Y7YUUK7pZw4UcybAX9rX3vH48XFtyUKLeDM24uCmsf7Elrepen2BZoL5l%2BTkjRLfxYTRFbHnfAmN0aaOgkYMVRNz8qsy4tiz3sKbQBxsrJpCd6idKzN3UAdLv3ottLefsbK9iGQJ67l0jSB1Q&X-Amz-Signature=701affe81936b7b23b2f34fc5a36f02945051a9c61321105e1ce386698204fe3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753ACWGA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDIkoapMPQdPHezj2%2B8OWtji4kLgTLzdYpmnurWOcei3wIhAP54wl3SgAl1WOoDWdWE4h0rXEdE9ruTkf9e2x5yV%2B76Kv8DCHEQABoMNjM3NDIzMTgzODA1IgwVRVLjusBNX8IMOGgq3AMBQv8%2F4weMJqj9EN5pQKjMfVDyRP58eOkRkro2FZrqprK0mx7SnoaZWZLV3rVexM5dCSb%2F2lcCtDVG9yw87D7majyuA22hcrfONrIwa40m0jgfOs45C6lyVgnOjPQXCu4K906%2FPFFV1mZt8%2BQX9WOL5CNdP10ZbD7l7Fm7BjlY0pYlM4mbiUmHdwxqlVnxzuMAkdj3q407SstFDCpSUl3HJnwLDqB8YWDBxjbv2G4rJtHQWFMwJ5JeK2bV46Ksng0UcvFZMdFSCQBs3xTSiV2fhRoC4ugFwXt1io09%2BaWM5XMqf%2F8CaxbespMScGBOhpKaWhhG%2FCzpshv4rvC7lgBsKSzzyYh%2FSpWyIszsb8w01Ddj0Za7z2NfK8GqWxJY7UU5PeU%2Bbh%2Bu0UeXUDpfWrwxdbg2tnUPPjWeggEUIsW%2Fssfb%2BTBKybYhKhB7npOEZzLJKkXLBK9EP6fUj2kRJl3omoYtMy9GLtqBQol8E35E5mnw6D0VTzfW4piZZRn4h3GnTaLHaVSUGc6MhbYny3k8JXY2YHBzWfULJr7%2BGCPrVJ3UPYOXNCq5jfXef9QwCn99GV6PKQO1KWz%2BaXsazFfk4ynAYNqIb6%2FCvURBIEytVWare15xMbQFUJj9UTCF%2Bpa9BjqkAaSkoYzleYPUWLi7XB2JKq6NrKLIdb8AFaEHw1znDoyLSDsqhhZo%2BaQrHk1lXtCmT2SxZfqIZH4Y7YUUK7pZw4UcybAX9rX3vH48XFtyUKLeDM24uCmsf7Elrepen2BZoL5l%2BTkjRLfxYTRFbHnfAmN0aaOgkYMVRNz8qsy4tiz3sKbQBxsrJpCd6idKzN3UAdLv3ottLefsbK9iGQJ67l0jSB1Q&X-Amz-Signature=2e93cbd160164d9a777a90f214d57915a60ff601f2d07f002fbb9d94e7816817&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663H7ZSADI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIGq8mZYEkY0TsHdfApKEGzf%2BIQSe1SSbPxK8RpyKm26JAiEAhHWv7%2FX4KIq5wcg3SpkEeiXGjjXBDeS5viV%2B%2BDqviCIq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDHeMxhj8l0%2B710ZIiCrcAwWzxSgp%2FE4qn7TK9nN4YjLGytMWQRlfxakQLpRnS5ij%2FnEjEF8dGtw53DrPdFZ8t8nT5Ei3Bb3dZAuoCCz08gZt%2F66ptDdbdsjf%2BwruHT0FrT3Z2S6HDD6b8EMquJU3UqV%2BTT3R5D0p1so5RjDcPQcEtAdeMqrNNlz1oL%2BmJ7bv%2FHCXM7WqTHeRNU1%2FCXZ8du%2FgVtmaKNTXAA%2FQqyXDw4qhoTZ2YwESy0dgsYbLxe64nxo9UYoo8TkhHWxiv9CTd1A3Yt2boX6b9R9tpRNriA%2BMPV3UjKdB7Ff85mmVOHG0pPske%2FHNweqV%2BgXkie76xoRAiSiejy0Zj4lNmQZL8mepVXH9frMmeyyQg5IXqZuC%2FGiLslL2PQTz0Y0G2gESmTN6OIgB1JpqVVrSxKGwNBJjjMM7uqJqkxL0%2BIelsWXZPa9En2YZuDkVjHLLSFxBegBGe3rBbtuCxrHPlZn6t81S0zW080NNYlxRmJGT22sB09M34vSmOPsBy741RXK8ceHXIA9cZcEki8LrXRsR9ZRBoqr0B0hXHHxuU3cg%2BS3p9VEZQ6MogPslhtbgySlAW46Wz178%2BuDazY4bX9RnJFLV7ANh1uPrrDZYRc9zAoMHLvGyyQv00YzZb9CgMPv5lr0GOqUBBHVpt0sCOGPm0R9abNJwbaExTRero%2BoUS5etrsDwz4t7JVhphMia3W%2BkOphIBA4tcPIanEu6zauCQZplA1Dc7lbbiuq%2Bgy0D1boqr5pQH1Ds3moUQ5pxy40ZXhSrKlpg1wi7VdN5if33ANyBcejmBBuPTTtoBycOgGVPXF8siENBk0hbhTabheyMzX4ZNlOAQ3dxO9QtlxcUgi%2B%2B0Qj4I%2F4UDvEA&X-Amz-Signature=3d3632c0c7bb1b18d176e709aedc8216afb892a91c078d05b780ddfc25779f1f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663H7ZSADI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIGq8mZYEkY0TsHdfApKEGzf%2BIQSe1SSbPxK8RpyKm26JAiEAhHWv7%2FX4KIq5wcg3SpkEeiXGjjXBDeS5viV%2B%2BDqviCIq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDHeMxhj8l0%2B710ZIiCrcAwWzxSgp%2FE4qn7TK9nN4YjLGytMWQRlfxakQLpRnS5ij%2FnEjEF8dGtw53DrPdFZ8t8nT5Ei3Bb3dZAuoCCz08gZt%2F66ptDdbdsjf%2BwruHT0FrT3Z2S6HDD6b8EMquJU3UqV%2BTT3R5D0p1so5RjDcPQcEtAdeMqrNNlz1oL%2BmJ7bv%2FHCXM7WqTHeRNU1%2FCXZ8du%2FgVtmaKNTXAA%2FQqyXDw4qhoTZ2YwESy0dgsYbLxe64nxo9UYoo8TkhHWxiv9CTd1A3Yt2boX6b9R9tpRNriA%2BMPV3UjKdB7Ff85mmVOHG0pPske%2FHNweqV%2BgXkie76xoRAiSiejy0Zj4lNmQZL8mepVXH9frMmeyyQg5IXqZuC%2FGiLslL2PQTz0Y0G2gESmTN6OIgB1JpqVVrSxKGwNBJjjMM7uqJqkxL0%2BIelsWXZPa9En2YZuDkVjHLLSFxBegBGe3rBbtuCxrHPlZn6t81S0zW080NNYlxRmJGT22sB09M34vSmOPsBy741RXK8ceHXIA9cZcEki8LrXRsR9ZRBoqr0B0hXHHxuU3cg%2BS3p9VEZQ6MogPslhtbgySlAW46Wz178%2BuDazY4bX9RnJFLV7ANh1uPrrDZYRc9zAoMHLvGyyQv00YzZb9CgMPv5lr0GOqUBBHVpt0sCOGPm0R9abNJwbaExTRero%2BoUS5etrsDwz4t7JVhphMia3W%2BkOphIBA4tcPIanEu6zauCQZplA1Dc7lbbiuq%2Bgy0D1boqr5pQH1Ds3moUQ5pxy40ZXhSrKlpg1wi7VdN5if33ANyBcejmBBuPTTtoBycOgGVPXF8siENBk0hbhTabheyMzX4ZNlOAQ3dxO9QtlxcUgi%2B%2B0Qj4I%2F4UDvEA&X-Amz-Signature=dbf6d26419c51d7b3eadf0c3e510ba0cb56cd0542af0962441b1af56db1eea9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466753ACWGA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDIkoapMPQdPHezj2%2B8OWtji4kLgTLzdYpmnurWOcei3wIhAP54wl3SgAl1WOoDWdWE4h0rXEdE9ruTkf9e2x5yV%2B76Kv8DCHEQABoMNjM3NDIzMTgzODA1IgwVRVLjusBNX8IMOGgq3AMBQv8%2F4weMJqj9EN5pQKjMfVDyRP58eOkRkro2FZrqprK0mx7SnoaZWZLV3rVexM5dCSb%2F2lcCtDVG9yw87D7majyuA22hcrfONrIwa40m0jgfOs45C6lyVgnOjPQXCu4K906%2FPFFV1mZt8%2BQX9WOL5CNdP10ZbD7l7Fm7BjlY0pYlM4mbiUmHdwxqlVnxzuMAkdj3q407SstFDCpSUl3HJnwLDqB8YWDBxjbv2G4rJtHQWFMwJ5JeK2bV46Ksng0UcvFZMdFSCQBs3xTSiV2fhRoC4ugFwXt1io09%2BaWM5XMqf%2F8CaxbespMScGBOhpKaWhhG%2FCzpshv4rvC7lgBsKSzzyYh%2FSpWyIszsb8w01Ddj0Za7z2NfK8GqWxJY7UU5PeU%2Bbh%2Bu0UeXUDpfWrwxdbg2tnUPPjWeggEUIsW%2Fssfb%2BTBKybYhKhB7npOEZzLJKkXLBK9EP6fUj2kRJl3omoYtMy9GLtqBQol8E35E5mnw6D0VTzfW4piZZRn4h3GnTaLHaVSUGc6MhbYny3k8JXY2YHBzWfULJr7%2BGCPrVJ3UPYOXNCq5jfXef9QwCn99GV6PKQO1KWz%2BaXsazFfk4ynAYNqIb6%2FCvURBIEytVWare15xMbQFUJj9UTCF%2Bpa9BjqkAaSkoYzleYPUWLi7XB2JKq6NrKLIdb8AFaEHw1znDoyLSDsqhhZo%2BaQrHk1lXtCmT2SxZfqIZH4Y7YUUK7pZw4UcybAX9rX3vH48XFtyUKLeDM24uCmsf7Elrepen2BZoL5l%2BTkjRLfxYTRFbHnfAmN0aaOgkYMVRNz8qsy4tiz3sKbQBxsrJpCd6idKzN3UAdLv3ottLefsbK9iGQJ67l0jSB1Q&X-Amz-Signature=b5d7ce97c6cc9d3d009fd2751327d92b9ccf1209f0608794f495967a535493bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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