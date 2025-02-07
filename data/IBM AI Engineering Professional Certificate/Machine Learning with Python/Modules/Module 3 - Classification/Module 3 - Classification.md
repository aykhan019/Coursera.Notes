

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAC3NSPX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIFC6IhlgKhlGWStDhXwsoBVHsD9DhGR%2BeN%2Fpx17%2Bq4IRAiEA9seL4Cq7h7BWqRBFW%2FbP24nRO5MeWSCLFusCwcYQBQMq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDF4oN2pZogcyTfhbJyrcA0D409TBiDcbl3z4W%2FH6xGCiQG5NlZb1TL0lkPpTMlQj2qmGRJsQ9M1P562YPLjXuOh7iRD85PaH8RzMuJ23H9lELqk7%2FyIc0bxBJ9AdjxranTb1fC%2Fxhr0O6A6%2F9bE2s1CCnfis3hNiESSpT%2B29ITcouWGXPUMJUUn3DO1MORVTDifBAQpE%2BpR0BKl9L5nDNGmjHFFw1yIkVjwjeCgzyFIQNc%2FlOSmEeddHvwn8rjrQ46uqfxZo0AqfDSjcw3fjMoUcEv5WbHDZe59PADpBy%2B1jIEXHFfuN4kYFq3b0VEmK0%2BUBhevNBQVAVAqfBn6vjJRKLwhkkvirAnnI2BGGZHuGxTS9LhrVGrWuxEZHC8clOpIyi0XdUH8IAcLLwkJzulc%2B0Mlno4hCC1rIv3J1vzotyNJPAp7rCYHszRwR3WcvL%2FYsW0Ed%2BoucT4%2F3nxk4fUFyW4fyOGfD6IQUwGtCXUmdovHYqpOOPi6nslskqCNjMkmnafGAsfPUtXBN%2BUhfcGoswSjIl5pfSKbHbKyKGeG48Li%2FrmOsAgurHKomqYNk055EZhpPjOm5EmGJa3q5jX5bW0F1gQnCQCkov0kl0Ynvet7Gk%2Bl2n3lCZMeBpRXrX9ILJGzHnhXVWgJXMLb5lr0GOqUB41F1dqsYHX%2Fm0cuk3Dhnpe6fHV%2F5N0uEVxxvkHLdhqUhaTBdySJr1CR8gljwKwguUy3dNV0aBBNL6w3T35nOj52Bg1Fz0d%2B6JpORMWy2zpUo4W%2BXO%2FlFVo41HOQ1h9C8PJDCYa0vQuGdCcmwDxLBdCcxeytCf608WRIguuxHGaSqWi3L4RGGqaiByeQX3lP3zBPw1sX76OsT1xtrYZ9u1mFmhEGC&X-Amz-Signature=d50d9714720bd41795735482675c335231ab2af069c1a0d60762b7885676de0e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAC3NSPX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIFC6IhlgKhlGWStDhXwsoBVHsD9DhGR%2BeN%2Fpx17%2Bq4IRAiEA9seL4Cq7h7BWqRBFW%2FbP24nRO5MeWSCLFusCwcYQBQMq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDF4oN2pZogcyTfhbJyrcA0D409TBiDcbl3z4W%2FH6xGCiQG5NlZb1TL0lkPpTMlQj2qmGRJsQ9M1P562YPLjXuOh7iRD85PaH8RzMuJ23H9lELqk7%2FyIc0bxBJ9AdjxranTb1fC%2Fxhr0O6A6%2F9bE2s1CCnfis3hNiESSpT%2B29ITcouWGXPUMJUUn3DO1MORVTDifBAQpE%2BpR0BKl9L5nDNGmjHFFw1yIkVjwjeCgzyFIQNc%2FlOSmEeddHvwn8rjrQ46uqfxZo0AqfDSjcw3fjMoUcEv5WbHDZe59PADpBy%2B1jIEXHFfuN4kYFq3b0VEmK0%2BUBhevNBQVAVAqfBn6vjJRKLwhkkvirAnnI2BGGZHuGxTS9LhrVGrWuxEZHC8clOpIyi0XdUH8IAcLLwkJzulc%2B0Mlno4hCC1rIv3J1vzotyNJPAp7rCYHszRwR3WcvL%2FYsW0Ed%2BoucT4%2F3nxk4fUFyW4fyOGfD6IQUwGtCXUmdovHYqpOOPi6nslskqCNjMkmnafGAsfPUtXBN%2BUhfcGoswSjIl5pfSKbHbKyKGeG48Li%2FrmOsAgurHKomqYNk055EZhpPjOm5EmGJa3q5jX5bW0F1gQnCQCkov0kl0Ynvet7Gk%2Bl2n3lCZMeBpRXrX9ILJGzHnhXVWgJXMLb5lr0GOqUB41F1dqsYHX%2Fm0cuk3Dhnpe6fHV%2F5N0uEVxxvkHLdhqUhaTBdySJr1CR8gljwKwguUy3dNV0aBBNL6w3T35nOj52Bg1Fz0d%2B6JpORMWy2zpUo4W%2BXO%2FlFVo41HOQ1h9C8PJDCYa0vQuGdCcmwDxLBdCcxeytCf608WRIguuxHGaSqWi3L4RGGqaiByeQX3lP3zBPw1sX76OsT1xtrYZ9u1mFmhEGC&X-Amz-Signature=72b53425480db2d1db8702b9acc609f4859b652ce10bdc3bed7bb26e11265135&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAC3NSPX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIFC6IhlgKhlGWStDhXwsoBVHsD9DhGR%2BeN%2Fpx17%2Bq4IRAiEA9seL4Cq7h7BWqRBFW%2FbP24nRO5MeWSCLFusCwcYQBQMq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDF4oN2pZogcyTfhbJyrcA0D409TBiDcbl3z4W%2FH6xGCiQG5NlZb1TL0lkPpTMlQj2qmGRJsQ9M1P562YPLjXuOh7iRD85PaH8RzMuJ23H9lELqk7%2FyIc0bxBJ9AdjxranTb1fC%2Fxhr0O6A6%2F9bE2s1CCnfis3hNiESSpT%2B29ITcouWGXPUMJUUn3DO1MORVTDifBAQpE%2BpR0BKl9L5nDNGmjHFFw1yIkVjwjeCgzyFIQNc%2FlOSmEeddHvwn8rjrQ46uqfxZo0AqfDSjcw3fjMoUcEv5WbHDZe59PADpBy%2B1jIEXHFfuN4kYFq3b0VEmK0%2BUBhevNBQVAVAqfBn6vjJRKLwhkkvirAnnI2BGGZHuGxTS9LhrVGrWuxEZHC8clOpIyi0XdUH8IAcLLwkJzulc%2B0Mlno4hCC1rIv3J1vzotyNJPAp7rCYHszRwR3WcvL%2FYsW0Ed%2BoucT4%2F3nxk4fUFyW4fyOGfD6IQUwGtCXUmdovHYqpOOPi6nslskqCNjMkmnafGAsfPUtXBN%2BUhfcGoswSjIl5pfSKbHbKyKGeG48Li%2FrmOsAgurHKomqYNk055EZhpPjOm5EmGJa3q5jX5bW0F1gQnCQCkov0kl0Ynvet7Gk%2Bl2n3lCZMeBpRXrX9ILJGzHnhXVWgJXMLb5lr0GOqUB41F1dqsYHX%2Fm0cuk3Dhnpe6fHV%2F5N0uEVxxvkHLdhqUhaTBdySJr1CR8gljwKwguUy3dNV0aBBNL6w3T35nOj52Bg1Fz0d%2B6JpORMWy2zpUo4W%2BXO%2FlFVo41HOQ1h9C8PJDCYa0vQuGdCcmwDxLBdCcxeytCf608WRIguuxHGaSqWi3L4RGGqaiByeQX3lP3zBPw1sX76OsT1xtrYZ9u1mFmhEGC&X-Amz-Signature=a625975db96a43341a1e6e4a24da41caadc1219c273bba9fe1a5f78216282ea9&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDI5LJ5D%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCJKUevaGVKMFtW91FKWI6oc87YnGlthrDFw3JQ54g1mwIgeXJQ%2FXODRZ5UD3BHqUYnzeOZrkyhgi84MuCmEq%2FP8Xwq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNfZN9sn91Sse92n%2BircAzsZsivvJ4lKBFtUm0NM38%2FYuFc2EdCsUxW4UvcnPpJ2waZzj66vEjw04VK8riv%2BIRJylhXplOAvzGFLfSEh5TdSUlmx48I2Tkz5uI9%2Fiyp2o636XcUsYbeLGTziSS%2FVkhuZfLbKL6HaWhot8luYfjC4KLlLsEHGlVJAv03HE151stxflFGgRqch09rmLXGASFgElN2vej5HQCpcUvTMmwwhDvWHUe%2FL0jWPQXmHYyoT9KFqUgI7ZRZ4JSiy6gzdHi8mwHxoBJqwP5v30%2Brwm9A2Lcqp5s%2BomcwKUkJ25ZJ0d5ASqjVX9PSKnl21hSPOows7yh5gV%2BboMdPUyFqs03hbOTzYkxuDfOS0uXY1WLRa9NHhDaDBkF5GIOxBaPFwx0%2Beo%2FHE7tEBeKgoRzao%2BpEW9WJwgTfjPbv1QzcQXMyTYZwjTEKse5XVomChse97DygvV2h%2BoOjI9e%2BRY18QI1GfgkuBfyVpfbx3M8%2Fnsr58JmiqHGFd%2FfYaYs%2BKdTEB%2B9ADDCZZKk%2FdaRk6GVpi81YslFvANaIVHrQRef3KLnHwyDXrRcmOnI60PfZw1QRpzLyyYN8lah1I%2F6gl9WFbks7S5nADID%2BQy5NbObYmhEkJaSEqDJjb98TNDP2OMNb5lr0GOqUBY8x06LuL1VyMEAtI550qFSzFr%2BnwSMJ6oAwBIRkpHHzDeP%2FXR8HICn3%2B%2F70VllhN%2BEjb8z4aMJbtMOMcBJtU8O14n%2F2A5DDEEeiTsnMhSjVdroN5UqUzwhs3LVp9y8A1bGeyGnv3DfUJocbGIBqU0NRkDVKemw9GXzh1IoP0Ou1Du4eCd0HbSyDhOxUaOIwOrGfwIexjNyvBR3hKkTjdSNZY0bNn&X-Amz-Signature=324294e68af7ff0363a71bc4db851797ff110c0e3fcc4f72c0f80ff8863eab5b&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDI5LJ5D%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQCJKUevaGVKMFtW91FKWI6oc87YnGlthrDFw3JQ54g1mwIgeXJQ%2FXODRZ5UD3BHqUYnzeOZrkyhgi84MuCmEq%2FP8Xwq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDNfZN9sn91Sse92n%2BircAzsZsivvJ4lKBFtUm0NM38%2FYuFc2EdCsUxW4UvcnPpJ2waZzj66vEjw04VK8riv%2BIRJylhXplOAvzGFLfSEh5TdSUlmx48I2Tkz5uI9%2Fiyp2o636XcUsYbeLGTziSS%2FVkhuZfLbKL6HaWhot8luYfjC4KLlLsEHGlVJAv03HE151stxflFGgRqch09rmLXGASFgElN2vej5HQCpcUvTMmwwhDvWHUe%2FL0jWPQXmHYyoT9KFqUgI7ZRZ4JSiy6gzdHi8mwHxoBJqwP5v30%2Brwm9A2Lcqp5s%2BomcwKUkJ25ZJ0d5ASqjVX9PSKnl21hSPOows7yh5gV%2BboMdPUyFqs03hbOTzYkxuDfOS0uXY1WLRa9NHhDaDBkF5GIOxBaPFwx0%2Beo%2FHE7tEBeKgoRzao%2BpEW9WJwgTfjPbv1QzcQXMyTYZwjTEKse5XVomChse97DygvV2h%2BoOjI9e%2BRY18QI1GfgkuBfyVpfbx3M8%2Fnsr58JmiqHGFd%2FfYaYs%2BKdTEB%2B9ADDCZZKk%2FdaRk6GVpi81YslFvANaIVHrQRef3KLnHwyDXrRcmOnI60PfZw1QRpzLyyYN8lah1I%2F6gl9WFbks7S5nADID%2BQy5NbObYmhEkJaSEqDJjb98TNDP2OMNb5lr0GOqUBY8x06LuL1VyMEAtI550qFSzFr%2BnwSMJ6oAwBIRkpHHzDeP%2FXR8HICn3%2B%2F70VllhN%2BEjb8z4aMJbtMOMcBJtU8O14n%2F2A5DDEEeiTsnMhSjVdroN5UqUzwhs3LVp9y8A1bGeyGnv3DfUJocbGIBqU0NRkDVKemw9GXzh1IoP0Ou1Du4eCd0HbSyDhOxUaOIwOrGfwIexjNyvBR3hKkTjdSNZY0bNn&X-Amz-Signature=b53dc5f42edbe696d8fe160bd42a5624b8e9edcd4b5a887759260613d13f59ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAC3NSPX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIFC6IhlgKhlGWStDhXwsoBVHsD9DhGR%2BeN%2Fpx17%2Bq4IRAiEA9seL4Cq7h7BWqRBFW%2FbP24nRO5MeWSCLFusCwcYQBQMq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDF4oN2pZogcyTfhbJyrcA0D409TBiDcbl3z4W%2FH6xGCiQG5NlZb1TL0lkPpTMlQj2qmGRJsQ9M1P562YPLjXuOh7iRD85PaH8RzMuJ23H9lELqk7%2FyIc0bxBJ9AdjxranTb1fC%2Fxhr0O6A6%2F9bE2s1CCnfis3hNiESSpT%2B29ITcouWGXPUMJUUn3DO1MORVTDifBAQpE%2BpR0BKl9L5nDNGmjHFFw1yIkVjwjeCgzyFIQNc%2FlOSmEeddHvwn8rjrQ46uqfxZo0AqfDSjcw3fjMoUcEv5WbHDZe59PADpBy%2B1jIEXHFfuN4kYFq3b0VEmK0%2BUBhevNBQVAVAqfBn6vjJRKLwhkkvirAnnI2BGGZHuGxTS9LhrVGrWuxEZHC8clOpIyi0XdUH8IAcLLwkJzulc%2B0Mlno4hCC1rIv3J1vzotyNJPAp7rCYHszRwR3WcvL%2FYsW0Ed%2BoucT4%2F3nxk4fUFyW4fyOGfD6IQUwGtCXUmdovHYqpOOPi6nslskqCNjMkmnafGAsfPUtXBN%2BUhfcGoswSjIl5pfSKbHbKyKGeG48Li%2FrmOsAgurHKomqYNk055EZhpPjOm5EmGJa3q5jX5bW0F1gQnCQCkov0kl0Ynvet7Gk%2Bl2n3lCZMeBpRXrX9ILJGzHnhXVWgJXMLb5lr0GOqUB41F1dqsYHX%2Fm0cuk3Dhnpe6fHV%2F5N0uEVxxvkHLdhqUhaTBdySJr1CR8gljwKwguUy3dNV0aBBNL6w3T35nOj52Bg1Fz0d%2B6JpORMWy2zpUo4W%2BXO%2FlFVo41HOQ1h9C8PJDCYa0vQuGdCcmwDxLBdCcxeytCf608WRIguuxHGaSqWi3L4RGGqaiByeQX3lP3zBPw1sX76OsT1xtrYZ9u1mFmhEGC&X-Amz-Signature=ba1c0814d0c052d1aebb410bf5f9d8558e73c53f4e2732f27d0edc4945f11990&X-Amz-SignedHeaders=host&x-id=GetObject)
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