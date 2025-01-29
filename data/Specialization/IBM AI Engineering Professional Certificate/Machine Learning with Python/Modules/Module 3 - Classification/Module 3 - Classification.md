

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FH7T4GC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJGMEQCIG43ed%2B5KPXK3ZUksCeTw6qthVBbh7sYRPxCxpU5ojsYAiATpzaxs9LZx%2BcbJ7Gcfcu3820da6IdGKTRQ40hS9GxNiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4DRXcHwWasesULvrKtwDvvNiece89J7Oyb7jrWtQ2N14mUrHKWOxtYDnbre7U0AoVLkYl1lqAb6NJn0mmzdR51tFpQohyzqGCAfElIvdqXBJiq01xqcuFUNAbXz443zpUU5nzDnkU1aTE36GlG%2BvclGTZM%2Bo6Hu3V2akB8w6evrSzUMZeYj67nb8%2BXwcO%2BRfFUIaeyZl1863rK%2FVhGkArTg%2BKilBPhZebfkRtt3OJMoxb54WANz4ErW4FduRC5ZbzI1JJIyCgay47QjSMAwa%2Fq8yIMiqWOi5lbCkUcPlrpYVjhH0ROEA%2FrnVMncoYZWXIEUvnS8t%2Fm4Z0ZwMeIh0VrNVF9Y8IqbyWYF5PBaRPOCBhqP6QEoMagFsFkbuiA%2FU%2BbYlClUfgIxLLO4tHdXwaQsce%2FsOJvIi8ePDNVsBrHFCUj7kNUN3UJWRD7e85c%2BSWcbukxBWi6zKiqbOG5NTuJFFNgd4jaHKIHG0TUErTJogyBQEMx4yablE0DToFQJiJnDWbnezyDuQo%2BVkMvnzbmJTgMg%2BYa1QfcCbDNLh5VoK7iP41b7CFSVtIP14zlAL2UKS9SnuHrj4ekXy356awIphp2Eq0ljSyLz%2F2Djox25wfZSZK9L8M5y%2FU4j51MhAQggjETd7IIkHK2ow%2Bo%2FnvAY6pgFuJbmGA%2Fv7Xnfu%2F15Qd2NWPjwYfhT7SfGhd2aVq7a7Ix9FPNVBOBTVbVsPiL%2BJwDJlH0xsCKGBw24vuLLTTj4b%2F9k2moGhft%2BoCP9V5CB1MkS2wRtYvjW4awQl5nS%2FmVRB7jSdsm48noWkME4w6g4mMDmWBsMB%2BeX%2F5kS7zocEQ6YpbEHomayRt8YChcIAULtmRieUdQ5lsaE2lHcTLV9ilDr5a2Zf&X-Amz-Signature=9fd21d6567987d567a80554f235099f7fc04c160b2db1ed01d3c8aa68149ddfe&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FH7T4GC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJGMEQCIG43ed%2B5KPXK3ZUksCeTw6qthVBbh7sYRPxCxpU5ojsYAiATpzaxs9LZx%2BcbJ7Gcfcu3820da6IdGKTRQ40hS9GxNiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4DRXcHwWasesULvrKtwDvvNiece89J7Oyb7jrWtQ2N14mUrHKWOxtYDnbre7U0AoVLkYl1lqAb6NJn0mmzdR51tFpQohyzqGCAfElIvdqXBJiq01xqcuFUNAbXz443zpUU5nzDnkU1aTE36GlG%2BvclGTZM%2Bo6Hu3V2akB8w6evrSzUMZeYj67nb8%2BXwcO%2BRfFUIaeyZl1863rK%2FVhGkArTg%2BKilBPhZebfkRtt3OJMoxb54WANz4ErW4FduRC5ZbzI1JJIyCgay47QjSMAwa%2Fq8yIMiqWOi5lbCkUcPlrpYVjhH0ROEA%2FrnVMncoYZWXIEUvnS8t%2Fm4Z0ZwMeIh0VrNVF9Y8IqbyWYF5PBaRPOCBhqP6QEoMagFsFkbuiA%2FU%2BbYlClUfgIxLLO4tHdXwaQsce%2FsOJvIi8ePDNVsBrHFCUj7kNUN3UJWRD7e85c%2BSWcbukxBWi6zKiqbOG5NTuJFFNgd4jaHKIHG0TUErTJogyBQEMx4yablE0DToFQJiJnDWbnezyDuQo%2BVkMvnzbmJTgMg%2BYa1QfcCbDNLh5VoK7iP41b7CFSVtIP14zlAL2UKS9SnuHrj4ekXy356awIphp2Eq0ljSyLz%2F2Djox25wfZSZK9L8M5y%2FU4j51MhAQggjETd7IIkHK2ow%2Bo%2FnvAY6pgFuJbmGA%2Fv7Xnfu%2F15Qd2NWPjwYfhT7SfGhd2aVq7a7Ix9FPNVBOBTVbVsPiL%2BJwDJlH0xsCKGBw24vuLLTTj4b%2F9k2moGhft%2BoCP9V5CB1MkS2wRtYvjW4awQl5nS%2FmVRB7jSdsm48noWkME4w6g4mMDmWBsMB%2BeX%2F5kS7zocEQ6YpbEHomayRt8YChcIAULtmRieUdQ5lsaE2lHcTLV9ilDr5a2Zf&X-Amz-Signature=ae69d62dd7edc5f0dbb989194e4cf68d814cd2a9892f4f8c8a1f0051f8c300c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FH7T4GC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJGMEQCIG43ed%2B5KPXK3ZUksCeTw6qthVBbh7sYRPxCxpU5ojsYAiATpzaxs9LZx%2BcbJ7Gcfcu3820da6IdGKTRQ40hS9GxNiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4DRXcHwWasesULvrKtwDvvNiece89J7Oyb7jrWtQ2N14mUrHKWOxtYDnbre7U0AoVLkYl1lqAb6NJn0mmzdR51tFpQohyzqGCAfElIvdqXBJiq01xqcuFUNAbXz443zpUU5nzDnkU1aTE36GlG%2BvclGTZM%2Bo6Hu3V2akB8w6evrSzUMZeYj67nb8%2BXwcO%2BRfFUIaeyZl1863rK%2FVhGkArTg%2BKilBPhZebfkRtt3OJMoxb54WANz4ErW4FduRC5ZbzI1JJIyCgay47QjSMAwa%2Fq8yIMiqWOi5lbCkUcPlrpYVjhH0ROEA%2FrnVMncoYZWXIEUvnS8t%2Fm4Z0ZwMeIh0VrNVF9Y8IqbyWYF5PBaRPOCBhqP6QEoMagFsFkbuiA%2FU%2BbYlClUfgIxLLO4tHdXwaQsce%2FsOJvIi8ePDNVsBrHFCUj7kNUN3UJWRD7e85c%2BSWcbukxBWi6zKiqbOG5NTuJFFNgd4jaHKIHG0TUErTJogyBQEMx4yablE0DToFQJiJnDWbnezyDuQo%2BVkMvnzbmJTgMg%2BYa1QfcCbDNLh5VoK7iP41b7CFSVtIP14zlAL2UKS9SnuHrj4ekXy356awIphp2Eq0ljSyLz%2F2Djox25wfZSZK9L8M5y%2FU4j51MhAQggjETd7IIkHK2ow%2Bo%2FnvAY6pgFuJbmGA%2Fv7Xnfu%2F15Qd2NWPjwYfhT7SfGhd2aVq7a7Ix9FPNVBOBTVbVsPiL%2BJwDJlH0xsCKGBw24vuLLTTj4b%2F9k2moGhft%2BoCP9V5CB1MkS2wRtYvjW4awQl5nS%2FmVRB7jSdsm48noWkME4w6g4mMDmWBsMB%2BeX%2F5kS7zocEQ6YpbEHomayRt8YChcIAULtmRieUdQ5lsaE2lHcTLV9ilDr5a2Zf&X-Amz-Signature=24ac47dcd279f286d72abeef598cd2df39e2d040117837f7b80b300d0d5852ef&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOHB2CVS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICxeN05blF1TBAKFW2tDMVjkhE0uuiNvwM6fXdek70YDAiBr1vZ285dqEU2vnpn3D3Ny5zjI5jSZBBJRuB6wJOeTxyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMalBf%2FkGIETRxYuwGKtwDXGaxhpP0XpjNmiLUR9QM6uEisOXm2QB2Tr1u0x%2FWvW5eqmu%2FgPYHPSjd%2B6YbqCpEiLtFPapraq8eBZDT7MpXwsBPzowQBsMt%2BaIxMa4LHavRU2hp%2B9EjwPSToO6Ktfs8HMmtua1sttM3OsSOHD73JTRVg%2B1qhfSvqGO5wePK4a9xWmjw1lQYgx4jVbyG59q7vWhyL633CQkC6PQzNBGxPGPQA0WBxplCWpgvcUpVCPW4QHYxOON26cGsKgflmj4Rk0JQ2LMI%2FUJKAJr%2FcrRQT3SOl681VYiQTuRCw0WhBVthQQAT59OYqYns%2FqtD0Yp21FHBflX6%2BfJq%2FbIxGGBydpAfHdoUZvZEeiFyXyCEDcwTpaydKAf%2FB0cmqC63rgb0NPM2SDhYF%2B%2FbczUgeettUKWZcJZ7l8r%2FZh1hYUcgRx19RHclDiv1f1E%2FQWGbaPZ638bufHMhFCZE%2B1rvHdhE0F2dvG%2FODtGN9HUZdY7KW%2F9dPJhWQ0M1Vc7xpSR09MLOOSHGgtu2LsQYUfpEaT4KAVr7%2B4E0kxMf%2BNiHuaJ%2FRkXrX5MH5eqd6UW%2FWcNoUuR1DRd7F2NaSLN0Z3Vib%2Bd57Q%2BWc3h3wAzaQtKzwEQXhx1K%2F2qC71Z2%2FMPgB3YwjrvmvAY6pgHfc8I%2FW10bvBGEtHaOmvMNXr9%2FgamfxRWhhz2wMFid5ibLcFD%2FGte7DCHf0FYEHURhOmDHiMRHskMkoCrapP7bqsLrPmjQ81E2h5FduTf0elmNHBA9rIZ%2FRG5itkJ6INOyndeQXPGiJCb0YE1IJTQnT%2Fz7OXWrrBuPu%2B4VnPVB43tlLXdMVkVVqTlyTDBp%2FI9FAeJWksrCqZU4GDD9BN0QkVTx7RyO&X-Amz-Signature=8a4ad640ec2b96beb807875d0d30fe7ced7503db2d49bbbaa56706f0621b624c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOHB2CVS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCICxeN05blF1TBAKFW2tDMVjkhE0uuiNvwM6fXdek70YDAiBr1vZ285dqEU2vnpn3D3Ny5zjI5jSZBBJRuB6wJOeTxyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMalBf%2FkGIETRxYuwGKtwDXGaxhpP0XpjNmiLUR9QM6uEisOXm2QB2Tr1u0x%2FWvW5eqmu%2FgPYHPSjd%2B6YbqCpEiLtFPapraq8eBZDT7MpXwsBPzowQBsMt%2BaIxMa4LHavRU2hp%2B9EjwPSToO6Ktfs8HMmtua1sttM3OsSOHD73JTRVg%2B1qhfSvqGO5wePK4a9xWmjw1lQYgx4jVbyG59q7vWhyL633CQkC6PQzNBGxPGPQA0WBxplCWpgvcUpVCPW4QHYxOON26cGsKgflmj4Rk0JQ2LMI%2FUJKAJr%2FcrRQT3SOl681VYiQTuRCw0WhBVthQQAT59OYqYns%2FqtD0Yp21FHBflX6%2BfJq%2FbIxGGBydpAfHdoUZvZEeiFyXyCEDcwTpaydKAf%2FB0cmqC63rgb0NPM2SDhYF%2B%2FbczUgeettUKWZcJZ7l8r%2FZh1hYUcgRx19RHclDiv1f1E%2FQWGbaPZ638bufHMhFCZE%2B1rvHdhE0F2dvG%2FODtGN9HUZdY7KW%2F9dPJhWQ0M1Vc7xpSR09MLOOSHGgtu2LsQYUfpEaT4KAVr7%2B4E0kxMf%2BNiHuaJ%2FRkXrX5MH5eqd6UW%2FWcNoUuR1DRd7F2NaSLN0Z3Vib%2Bd57Q%2BWc3h3wAzaQtKzwEQXhx1K%2F2qC71Z2%2FMPgB3YwjrvmvAY6pgHfc8I%2FW10bvBGEtHaOmvMNXr9%2FgamfxRWhhz2wMFid5ibLcFD%2FGte7DCHf0FYEHURhOmDHiMRHskMkoCrapP7bqsLrPmjQ81E2h5FduTf0elmNHBA9rIZ%2FRG5itkJ6INOyndeQXPGiJCb0YE1IJTQnT%2Fz7OXWrrBuPu%2B4VnPVB43tlLXdMVkVVqTlyTDBp%2FI9FAeJWksrCqZU4GDD9BN0QkVTx7RyO&X-Amz-Signature=c1e14ab90940ebb1c0bae003c199f03bd1ee8a3d9d8dc0296c0ed33695b5724f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FH7T4GC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJGMEQCIG43ed%2B5KPXK3ZUksCeTw6qthVBbh7sYRPxCxpU5ojsYAiATpzaxs9LZx%2BcbJ7Gcfcu3820da6IdGKTRQ40hS9GxNiqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4DRXcHwWasesULvrKtwDvvNiece89J7Oyb7jrWtQ2N14mUrHKWOxtYDnbre7U0AoVLkYl1lqAb6NJn0mmzdR51tFpQohyzqGCAfElIvdqXBJiq01xqcuFUNAbXz443zpUU5nzDnkU1aTE36GlG%2BvclGTZM%2Bo6Hu3V2akB8w6evrSzUMZeYj67nb8%2BXwcO%2BRfFUIaeyZl1863rK%2FVhGkArTg%2BKilBPhZebfkRtt3OJMoxb54WANz4ErW4FduRC5ZbzI1JJIyCgay47QjSMAwa%2Fq8yIMiqWOi5lbCkUcPlrpYVjhH0ROEA%2FrnVMncoYZWXIEUvnS8t%2Fm4Z0ZwMeIh0VrNVF9Y8IqbyWYF5PBaRPOCBhqP6QEoMagFsFkbuiA%2FU%2BbYlClUfgIxLLO4tHdXwaQsce%2FsOJvIi8ePDNVsBrHFCUj7kNUN3UJWRD7e85c%2BSWcbukxBWi6zKiqbOG5NTuJFFNgd4jaHKIHG0TUErTJogyBQEMx4yablE0DToFQJiJnDWbnezyDuQo%2BVkMvnzbmJTgMg%2BYa1QfcCbDNLh5VoK7iP41b7CFSVtIP14zlAL2UKS9SnuHrj4ekXy356awIphp2Eq0ljSyLz%2F2Djox25wfZSZK9L8M5y%2FU4j51MhAQggjETd7IIkHK2ow%2Bo%2FnvAY6pgFuJbmGA%2Fv7Xnfu%2F15Qd2NWPjwYfhT7SfGhd2aVq7a7Ix9FPNVBOBTVbVsPiL%2BJwDJlH0xsCKGBw24vuLLTTj4b%2F9k2moGhft%2BoCP9V5CB1MkS2wRtYvjW4awQl5nS%2FmVRB7jSdsm48noWkME4w6g4mMDmWBsMB%2BeX%2F5kS7zocEQ6YpbEHomayRt8YChcIAULtmRieUdQ5lsaE2lHcTLV9ilDr5a2Zf&X-Amz-Signature=7c6f2999e6ae375827cbde18fe66a6b1938b4cdfc7571df7b7dcea38697587bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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