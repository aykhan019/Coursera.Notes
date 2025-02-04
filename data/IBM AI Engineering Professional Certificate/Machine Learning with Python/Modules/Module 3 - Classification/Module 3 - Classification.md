

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSQHGTV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCpqLta5TLvSh9ZXOXNHv%2BdAfhoXpn89HcVsh%2FjnggR2wIhAOXEUskKA%2BSrbe8JTYCo9un0p5KMelHJ148nfOJfZx6sKv8DCDYQABoMNjM3NDIzMTgzODA1IgzzftOO3VUxWlD%2FGmMq3AOeZ3ftZPG%2B%2Fb16f4njavr3V40peynkje1hOIjivkg%2FNOgogHg9PtgU6xlZyny1zhFoSVZyOxucWdVA9hwKF7OTJ9f3V60nynC7ZpO1puaVEhihYHzt89Pwb%2BTGboXIY2df0QkCr88sy%2BZUzG1ZtGEGZa%2B%2Bo0rflhk7%2FJQdRyKqoC6wIijsRtFH7Wul4sWWFEc5Z3KBPrlmpmofzuof3MGmHM6uHrN5l5SYp9A22RkoTl08Gk8YETC5xBFapvmkHMRw1GgTo5bX5%2B7QoaTf6%2B%2BqJlbNk7U1pZ7heuhgKjuNbN1swvGO5rCjhOgB2HB5uqxGr4lhabAkqW7pZ6nzg0qKX7KODRtWgoN1udEj7v9ULImsCQJ5mg%2FOweikiJVhvK5AFUg9QBosvM3a1ekkW%2BgFPOdTslEkCE3kLU%2FrEXgGrrH97qibQ1b8HSILWkeysNvTk5Rf5nt8W1YE8ZrEEiZriSpkl3SCjvVNRVdof1cMOngw6%2BvW1Ww5UAo4ZmCO4eOdp8LSjQSkeBzqca1W9bVfea4RSK0wnMuj0VzRJlmXETpptPeZg2hhBodOCMcRfEzewtee8FRnv9ZHyxiZyOQnxLhaV61iAcnSwXcqcCfovoDbRt12r0Wf77SyNDCv%2FYm9BjqkAZcos1040lkF26qZFHGrUXVk8PQZuiUZ9P6zy%2FMCo%2BySau%2FGnWFqO9loiIvZdhD7lZV%2BSj1d6SmM9ixqmfb78cdL46hZ41SOOGsct8CiuSqB7EFJ0zHlqScvRYRgOdUoreNMjJ8dguDTblnfpX9qdstFqd4fXAZ2mC4VRa7h5gwsexC6fyhIsxVNJRNRD5Hhm2BYgPd%2BEiXJSmDpCTKR7jCmY1mk&X-Amz-Signature=2b38e8a9c04a96881dd949ab2e11d556b32bae9d25b935820c055dbe770524fa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSQHGTV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCpqLta5TLvSh9ZXOXNHv%2BdAfhoXpn89HcVsh%2FjnggR2wIhAOXEUskKA%2BSrbe8JTYCo9un0p5KMelHJ148nfOJfZx6sKv8DCDYQABoMNjM3NDIzMTgzODA1IgzzftOO3VUxWlD%2FGmMq3AOeZ3ftZPG%2B%2Fb16f4njavr3V40peynkje1hOIjivkg%2FNOgogHg9PtgU6xlZyny1zhFoSVZyOxucWdVA9hwKF7OTJ9f3V60nynC7ZpO1puaVEhihYHzt89Pwb%2BTGboXIY2df0QkCr88sy%2BZUzG1ZtGEGZa%2B%2Bo0rflhk7%2FJQdRyKqoC6wIijsRtFH7Wul4sWWFEc5Z3KBPrlmpmofzuof3MGmHM6uHrN5l5SYp9A22RkoTl08Gk8YETC5xBFapvmkHMRw1GgTo5bX5%2B7QoaTf6%2B%2BqJlbNk7U1pZ7heuhgKjuNbN1swvGO5rCjhOgB2HB5uqxGr4lhabAkqW7pZ6nzg0qKX7KODRtWgoN1udEj7v9ULImsCQJ5mg%2FOweikiJVhvK5AFUg9QBosvM3a1ekkW%2BgFPOdTslEkCE3kLU%2FrEXgGrrH97qibQ1b8HSILWkeysNvTk5Rf5nt8W1YE8ZrEEiZriSpkl3SCjvVNRVdof1cMOngw6%2BvW1Ww5UAo4ZmCO4eOdp8LSjQSkeBzqca1W9bVfea4RSK0wnMuj0VzRJlmXETpptPeZg2hhBodOCMcRfEzewtee8FRnv9ZHyxiZyOQnxLhaV61iAcnSwXcqcCfovoDbRt12r0Wf77SyNDCv%2FYm9BjqkAZcos1040lkF26qZFHGrUXVk8PQZuiUZ9P6zy%2FMCo%2BySau%2FGnWFqO9loiIvZdhD7lZV%2BSj1d6SmM9ixqmfb78cdL46hZ41SOOGsct8CiuSqB7EFJ0zHlqScvRYRgOdUoreNMjJ8dguDTblnfpX9qdstFqd4fXAZ2mC4VRa7h5gwsexC6fyhIsxVNJRNRD5Hhm2BYgPd%2BEiXJSmDpCTKR7jCmY1mk&X-Amz-Signature=33fb47a3c3d83b2bc0be87a48e322c30e97a66cc804abaf5ea94b8d33072c0b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSQHGTV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCpqLta5TLvSh9ZXOXNHv%2BdAfhoXpn89HcVsh%2FjnggR2wIhAOXEUskKA%2BSrbe8JTYCo9un0p5KMelHJ148nfOJfZx6sKv8DCDYQABoMNjM3NDIzMTgzODA1IgzzftOO3VUxWlD%2FGmMq3AOeZ3ftZPG%2B%2Fb16f4njavr3V40peynkje1hOIjivkg%2FNOgogHg9PtgU6xlZyny1zhFoSVZyOxucWdVA9hwKF7OTJ9f3V60nynC7ZpO1puaVEhihYHzt89Pwb%2BTGboXIY2df0QkCr88sy%2BZUzG1ZtGEGZa%2B%2Bo0rflhk7%2FJQdRyKqoC6wIijsRtFH7Wul4sWWFEc5Z3KBPrlmpmofzuof3MGmHM6uHrN5l5SYp9A22RkoTl08Gk8YETC5xBFapvmkHMRw1GgTo5bX5%2B7QoaTf6%2B%2BqJlbNk7U1pZ7heuhgKjuNbN1swvGO5rCjhOgB2HB5uqxGr4lhabAkqW7pZ6nzg0qKX7KODRtWgoN1udEj7v9ULImsCQJ5mg%2FOweikiJVhvK5AFUg9QBosvM3a1ekkW%2BgFPOdTslEkCE3kLU%2FrEXgGrrH97qibQ1b8HSILWkeysNvTk5Rf5nt8W1YE8ZrEEiZriSpkl3SCjvVNRVdof1cMOngw6%2BvW1Ww5UAo4ZmCO4eOdp8LSjQSkeBzqca1W9bVfea4RSK0wnMuj0VzRJlmXETpptPeZg2hhBodOCMcRfEzewtee8FRnv9ZHyxiZyOQnxLhaV61iAcnSwXcqcCfovoDbRt12r0Wf77SyNDCv%2FYm9BjqkAZcos1040lkF26qZFHGrUXVk8PQZuiUZ9P6zy%2FMCo%2BySau%2FGnWFqO9loiIvZdhD7lZV%2BSj1d6SmM9ixqmfb78cdL46hZ41SOOGsct8CiuSqB7EFJ0zHlqScvRYRgOdUoreNMjJ8dguDTblnfpX9qdstFqd4fXAZ2mC4VRa7h5gwsexC6fyhIsxVNJRNRD5Hhm2BYgPd%2BEiXJSmDpCTKR7jCmY1mk&X-Amz-Signature=16bc2478f5ee8ac6e61d31f67f7d1e66611b86f38e50e5d8bb2be8ebece41652&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEIXN7DE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIARJq55VSEBm%2FNK%2F8oIgfuIGra96c6xjIIU8j%2BwcoOgCAiAhJ5YfPKfUAoY1K9wCDXKZRdz0Pu4Syr%2F%2FDcZTTPeOmCr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMuWocyNnVK2bZ%2Bf2IKtwDQspiECeO59xhj%2BppYT7s5J3ch8sACf2eQTGjsFDZo1JsE9Sh8AYrpAWeFHdGnIoxtOBXfu75s37N1jnwo4ExpVhwDKxeGsJ0MkwKUPTV1leYplKDS5cDFQE%2FJQMNYE%2BfYcn54zUvuPXQfqrbbihr37ihhhOjmbQ7lK9ZIZ3u1YvDAIdEupBQeeJSvf1RIeGvW6k%2BK6NEqHldoW3Kyf1aq7EiGPuCnBQyK%2B12bSmvm7ufhjWLlxdouf1CLfxEm2G1CZFMPgbEYbhrWMD2CGjD4k%2BAUXSpiqf%2FNHxjg7wu8O1h4KBlUv%2FdcMPYM1paqcE6xoFPp9JLv7uusnUoGFeFl46U262bGhiZZrJT9anS9eukZnTQEheXSJxa%2BQW5rV%2BiAxvLXFjk50qH9JANDINPZypyMUTocGdZ62L8qpN4phIP3I4xAdwjiTdOWyaYNKgyxTFB%2BKsO33jFJxN4bdl6IRcVqUnS5uuUqVNyCG%2BNKZ%2Bi%2FctVkjmS8Szs%2BGyuhKonoja%2B3ZIURtRzQ7FgWsEG6OzmYletdWuZzSqBHruorGRSEIM7ykow%2B7gMbzZqor6jG40LwNU7E6LVP%2Fx%2BSqtsCGlV7l0kHy54wWwefRIHkG2hAUXcucseEC%2BywVkwmP2JvQY6pgF%2B5mvoIBqMHdNlM3bPaYrnHAJb%2B7rWS74eWCxmnltimk1KFTX10sHi4N5trC9%2Bd1NAILLbGV2X0tqhtUq7XJat2Fvh6lGX3Y2XIuoeryYa8Ci8R5K7%2Bipt21B0ipObC%2BR%2FUwVfXfHJFJbqrWkzfnWS9XlUJRLp%2BNza5tk1TOcsMtlzZWdXu6YQldB5JYizhLyBlLdATFzC35vWxViwBUi6VUztoS28&X-Amz-Signature=f444c9f2c7957b915988345f2989bf3284f81000191ebe725c7f276ae83f7341&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEIXN7DE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIARJq55VSEBm%2FNK%2F8oIgfuIGra96c6xjIIU8j%2BwcoOgCAiAhJ5YfPKfUAoY1K9wCDXKZRdz0Pu4Syr%2F%2FDcZTTPeOmCr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMuWocyNnVK2bZ%2Bf2IKtwDQspiECeO59xhj%2BppYT7s5J3ch8sACf2eQTGjsFDZo1JsE9Sh8AYrpAWeFHdGnIoxtOBXfu75s37N1jnwo4ExpVhwDKxeGsJ0MkwKUPTV1leYplKDS5cDFQE%2FJQMNYE%2BfYcn54zUvuPXQfqrbbihr37ihhhOjmbQ7lK9ZIZ3u1YvDAIdEupBQeeJSvf1RIeGvW6k%2BK6NEqHldoW3Kyf1aq7EiGPuCnBQyK%2B12bSmvm7ufhjWLlxdouf1CLfxEm2G1CZFMPgbEYbhrWMD2CGjD4k%2BAUXSpiqf%2FNHxjg7wu8O1h4KBlUv%2FdcMPYM1paqcE6xoFPp9JLv7uusnUoGFeFl46U262bGhiZZrJT9anS9eukZnTQEheXSJxa%2BQW5rV%2BiAxvLXFjk50qH9JANDINPZypyMUTocGdZ62L8qpN4phIP3I4xAdwjiTdOWyaYNKgyxTFB%2BKsO33jFJxN4bdl6IRcVqUnS5uuUqVNyCG%2BNKZ%2Bi%2FctVkjmS8Szs%2BGyuhKonoja%2B3ZIURtRzQ7FgWsEG6OzmYletdWuZzSqBHruorGRSEIM7ykow%2B7gMbzZqor6jG40LwNU7E6LVP%2Fx%2BSqtsCGlV7l0kHy54wWwefRIHkG2hAUXcucseEC%2BywVkwmP2JvQY6pgF%2B5mvoIBqMHdNlM3bPaYrnHAJb%2B7rWS74eWCxmnltimk1KFTX10sHi4N5trC9%2Bd1NAILLbGV2X0tqhtUq7XJat2Fvh6lGX3Y2XIuoeryYa8Ci8R5K7%2Bipt21B0ipObC%2BR%2FUwVfXfHJFJbqrWkzfnWS9XlUJRLp%2BNza5tk1TOcsMtlzZWdXu6YQldB5JYizhLyBlLdATFzC35vWxViwBUi6VUztoS28&X-Amz-Signature=420ed7f2bb12e7fb2ffb282118c406cce469ee59a96b5305ff26994f64c639ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSQHGTV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCpqLta5TLvSh9ZXOXNHv%2BdAfhoXpn89HcVsh%2FjnggR2wIhAOXEUskKA%2BSrbe8JTYCo9un0p5KMelHJ148nfOJfZx6sKv8DCDYQABoMNjM3NDIzMTgzODA1IgzzftOO3VUxWlD%2FGmMq3AOeZ3ftZPG%2B%2Fb16f4njavr3V40peynkje1hOIjivkg%2FNOgogHg9PtgU6xlZyny1zhFoSVZyOxucWdVA9hwKF7OTJ9f3V60nynC7ZpO1puaVEhihYHzt89Pwb%2BTGboXIY2df0QkCr88sy%2BZUzG1ZtGEGZa%2B%2Bo0rflhk7%2FJQdRyKqoC6wIijsRtFH7Wul4sWWFEc5Z3KBPrlmpmofzuof3MGmHM6uHrN5l5SYp9A22RkoTl08Gk8YETC5xBFapvmkHMRw1GgTo5bX5%2B7QoaTf6%2B%2BqJlbNk7U1pZ7heuhgKjuNbN1swvGO5rCjhOgB2HB5uqxGr4lhabAkqW7pZ6nzg0qKX7KODRtWgoN1udEj7v9ULImsCQJ5mg%2FOweikiJVhvK5AFUg9QBosvM3a1ekkW%2BgFPOdTslEkCE3kLU%2FrEXgGrrH97qibQ1b8HSILWkeysNvTk5Rf5nt8W1YE8ZrEEiZriSpkl3SCjvVNRVdof1cMOngw6%2BvW1Ww5UAo4ZmCO4eOdp8LSjQSkeBzqca1W9bVfea4RSK0wnMuj0VzRJlmXETpptPeZg2hhBodOCMcRfEzewtee8FRnv9ZHyxiZyOQnxLhaV61iAcnSwXcqcCfovoDbRt12r0Wf77SyNDCv%2FYm9BjqkAZcos1040lkF26qZFHGrUXVk8PQZuiUZ9P6zy%2FMCo%2BySau%2FGnWFqO9loiIvZdhD7lZV%2BSj1d6SmM9ixqmfb78cdL46hZ41SOOGsct8CiuSqB7EFJ0zHlqScvRYRgOdUoreNMjJ8dguDTblnfpX9qdstFqd4fXAZ2mC4VRa7h5gwsexC6fyhIsxVNJRNRD5Hhm2BYgPd%2BEiXJSmDpCTKR7jCmY1mk&X-Amz-Signature=7e85fcb7cf2dee84dd1bdebdebbeae33bfe5b55eacd9d6e4ca3e5b5c4ef41092&X-Amz-SignedHeaders=host&x-id=GetObject)
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