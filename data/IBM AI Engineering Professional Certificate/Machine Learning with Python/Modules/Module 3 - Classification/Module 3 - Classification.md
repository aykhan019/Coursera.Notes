

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZLOX7OF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIE6P2VKZpYsarxObJv4E68Pg0uANUZhFWBkqOPOn%2FzHpAiEA3R3rDb8cRq7xwe10HnESYEMN0cv5wPFV2dtwmg22M88qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBbnrx9T%2BqO0Sp3ijCrcA%2BPh6x8lJSdL8FK70TSz8JouRBrx3PI1mPu86D2f7ElPVqjaCYMDUrgB85gT6NE4urB79kaIt2MkRH79l6eFGGuiQjAfLGVLYafrdW74QeQI0%2B223LpUBvtGRWmAtNTFIi0t9gKeQDrPcTHzqeL0nVM2wlKzlmXdf3hB2sPCQbCkN3733hef2Z5c60Di%2F7ac1BSySvRLfq0fD%2BbTstbdBtFU7Z1XDhfwtoy%2ByHr1bYaWIZjqUOb6XPCM3So474V216M8IubTM%2F2Ry%2FBGzyv8uUJxVBQFuU7TgAh%2F0HswzSrHl89L8%2BK757ovfCwTuaF%2BAf1k0rmTUSZas2V9rHQATemIlYYDZxaOVajSAks%2FljZ%2FeG5g27v00sllnt4Acf76LJ0O6fNXYZmCr5VWBjoDpPDROXLbdxYhNOczBPkoAVDkZPJkK87X%2BnowVxsfqxKu8npyIwXLWOR6VARFglO1GRIPr2Q1juXidi2JvS0tV%2FK6L9XTy26%2F1DTITXj8mCwQJV2iUBPdPC4VfzdwjRXI4IGBWAQdzeUE%2FQLBOLKm0R7Zo5BAsZmAD4%2FjPPB2meIQW7LtqK6h06d2599JJLpeW07eO08Dnxh2W5YONG7V%2Bv2E0A9T7F%2F%2FKIPH8HFbMODvm70GOqUBFc3maWiP05ylZwh5zutmZPQYdwmqyRRBFCjIqo3VrQ%2BYwQI3mTcK%2F9H6c14l01G1t1ZAXg%2FUHhKAHPom7r0wjJlyeG0pJv%2FDYc1pxzvQIVv1yCm7t51E9EQG7%2FXK6WViEofrPLVaSX4fIubedYcphSmPdkVoi0jAo3YtYypAQpM5SwbXq2t2%2BRP6x%2Bkn%2BvSwZr%2B4o4zdy0By4Tn8QzIkDKY%2FlOEN&X-Amz-Signature=c7003bbf5daa504657f65bdfab6da53826e7ce637adad1784b50374fba22641f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZLOX7OF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIE6P2VKZpYsarxObJv4E68Pg0uANUZhFWBkqOPOn%2FzHpAiEA3R3rDb8cRq7xwe10HnESYEMN0cv5wPFV2dtwmg22M88qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBbnrx9T%2BqO0Sp3ijCrcA%2BPh6x8lJSdL8FK70TSz8JouRBrx3PI1mPu86D2f7ElPVqjaCYMDUrgB85gT6NE4urB79kaIt2MkRH79l6eFGGuiQjAfLGVLYafrdW74QeQI0%2B223LpUBvtGRWmAtNTFIi0t9gKeQDrPcTHzqeL0nVM2wlKzlmXdf3hB2sPCQbCkN3733hef2Z5c60Di%2F7ac1BSySvRLfq0fD%2BbTstbdBtFU7Z1XDhfwtoy%2ByHr1bYaWIZjqUOb6XPCM3So474V216M8IubTM%2F2Ry%2FBGzyv8uUJxVBQFuU7TgAh%2F0HswzSrHl89L8%2BK757ovfCwTuaF%2BAf1k0rmTUSZas2V9rHQATemIlYYDZxaOVajSAks%2FljZ%2FeG5g27v00sllnt4Acf76LJ0O6fNXYZmCr5VWBjoDpPDROXLbdxYhNOczBPkoAVDkZPJkK87X%2BnowVxsfqxKu8npyIwXLWOR6VARFglO1GRIPr2Q1juXidi2JvS0tV%2FK6L9XTy26%2F1DTITXj8mCwQJV2iUBPdPC4VfzdwjRXI4IGBWAQdzeUE%2FQLBOLKm0R7Zo5BAsZmAD4%2FjPPB2meIQW7LtqK6h06d2599JJLpeW07eO08Dnxh2W5YONG7V%2Bv2E0A9T7F%2F%2FKIPH8HFbMODvm70GOqUBFc3maWiP05ylZwh5zutmZPQYdwmqyRRBFCjIqo3VrQ%2BYwQI3mTcK%2F9H6c14l01G1t1ZAXg%2FUHhKAHPom7r0wjJlyeG0pJv%2FDYc1pxzvQIVv1yCm7t51E9EQG7%2FXK6WViEofrPLVaSX4fIubedYcphSmPdkVoi0jAo3YtYypAQpM5SwbXq2t2%2BRP6x%2Bkn%2BvSwZr%2B4o4zdy0By4Tn8QzIkDKY%2FlOEN&X-Amz-Signature=aca4221c023a7948b840ed5b91c54315e4e42c14f77724bf3719f4e4aed07d22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZLOX7OF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIE6P2VKZpYsarxObJv4E68Pg0uANUZhFWBkqOPOn%2FzHpAiEA3R3rDb8cRq7xwe10HnESYEMN0cv5wPFV2dtwmg22M88qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBbnrx9T%2BqO0Sp3ijCrcA%2BPh6x8lJSdL8FK70TSz8JouRBrx3PI1mPu86D2f7ElPVqjaCYMDUrgB85gT6NE4urB79kaIt2MkRH79l6eFGGuiQjAfLGVLYafrdW74QeQI0%2B223LpUBvtGRWmAtNTFIi0t9gKeQDrPcTHzqeL0nVM2wlKzlmXdf3hB2sPCQbCkN3733hef2Z5c60Di%2F7ac1BSySvRLfq0fD%2BbTstbdBtFU7Z1XDhfwtoy%2ByHr1bYaWIZjqUOb6XPCM3So474V216M8IubTM%2F2Ry%2FBGzyv8uUJxVBQFuU7TgAh%2F0HswzSrHl89L8%2BK757ovfCwTuaF%2BAf1k0rmTUSZas2V9rHQATemIlYYDZxaOVajSAks%2FljZ%2FeG5g27v00sllnt4Acf76LJ0O6fNXYZmCr5VWBjoDpPDROXLbdxYhNOczBPkoAVDkZPJkK87X%2BnowVxsfqxKu8npyIwXLWOR6VARFglO1GRIPr2Q1juXidi2JvS0tV%2FK6L9XTy26%2F1DTITXj8mCwQJV2iUBPdPC4VfzdwjRXI4IGBWAQdzeUE%2FQLBOLKm0R7Zo5BAsZmAD4%2FjPPB2meIQW7LtqK6h06d2599JJLpeW07eO08Dnxh2W5YONG7V%2Bv2E0A9T7F%2F%2FKIPH8HFbMODvm70GOqUBFc3maWiP05ylZwh5zutmZPQYdwmqyRRBFCjIqo3VrQ%2BYwQI3mTcK%2F9H6c14l01G1t1ZAXg%2FUHhKAHPom7r0wjJlyeG0pJv%2FDYc1pxzvQIVv1yCm7t51E9EQG7%2FXK6WViEofrPLVaSX4fIubedYcphSmPdkVoi0jAo3YtYypAQpM5SwbXq2t2%2BRP6x%2Bkn%2BvSwZr%2B4o4zdy0By4Tn8QzIkDKY%2FlOEN&X-Amz-Signature=c756b90c011ca2da8c251a22dc612840ac3536fe76078fcaaf07acf95b411d32&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HLUPICM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE659ncm19eTcbEJa3dPBWJOcSmP4ZF0rsQSBd2g5FBmAiB9sG5%2FN627Z3zfvThQkwlAl1e5JTp8X9TrVwg9fqFx7SqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM89vnJvvGoYciXjHsKtwDXAS%2FuJuNWdy5LevgjxdwjrwTKJpL3dhGubFE3f%2B%2F%2BA82ajAko28nI34PA76HYefDGaGY5P95oDHUlBtb%2BUmX1WuJ4BN271n8gLelpOOXMXTl8eNYy40B95mKHQob3oyngTS7wJumxqw3A8dH%2FSdZw3ujikbPcTcPHuZKUlboYkrPYdzwX1gGi%2FHgcMdGJbxhUlVjXigOINJ0uYyszlSHVm948Oy3DioYamjtRdTntEkWZ31ifW2aLdCbptxTf8wgzEZayfWAQd3YFOG0LPigMSVyRhtEVD2L%2BfHUfKuyHKu%2Bs9iiiR2nlReoKnYJRcRbadPV4mdQ%2BZ810vN%2FeT33hAJzKtP70tCgmN%2F5UK%2BMaPKhUbqXNY8J3n425n8fCP5vnGhXNuulYzWsYtAu2OyU6ltcZCWIIreW73DN5erVEIXyOD2FenKpc%2FQEkuOwpwX5Q7I3TDe9vOr8FcfGDlcmzktjMxuKz5rzTYiC3ujYeWk3N2Ds79A%2BjLneuIsFj0ngtGJc0%2FzCoqdlL1zgmWOaqFNwLMFIyvufbRjQNDqwZgSC%2FI%2BSbHpfaZ3NPTBgUurGvdEUi3CTN6lNQtM8q%2BmVmyt%2FToO52fqPQEqub1eRaGirPyeUTacwlBgK7zcw1u%2BbvQY6pgEfflNNNIjX1%2BF5Gr%2F9MI3DZt2p9mMvenl0FWU4RNUaAd2zRPKxTuzjT6EYOvS1BzfyW6FZy3SoRWy%2Bb56ofkVm%2B%2FBUrrjj%2BzQ1ENVHpHdieg9e0dS5pyb15iTiNLm%2FRoJ%2FtXOSmU1NqaROhP1wAKVBM3SbAkI16%2BeBXaO8Qi0MQ170gQeacfCT2YmjKdcF6k20QmSJY2mqA26CmTNAaL8wXSDLl0XF&X-Amz-Signature=a9aaae1b978bb5e587736afa70b3e062930af15a450e16f2a14c7f91ea9c7911&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HLUPICM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJGMEQCIE659ncm19eTcbEJa3dPBWJOcSmP4ZF0rsQSBd2g5FBmAiB9sG5%2FN627Z3zfvThQkwlAl1e5JTp8X9TrVwg9fqFx7SqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM89vnJvvGoYciXjHsKtwDXAS%2FuJuNWdy5LevgjxdwjrwTKJpL3dhGubFE3f%2B%2F%2BA82ajAko28nI34PA76HYefDGaGY5P95oDHUlBtb%2BUmX1WuJ4BN271n8gLelpOOXMXTl8eNYy40B95mKHQob3oyngTS7wJumxqw3A8dH%2FSdZw3ujikbPcTcPHuZKUlboYkrPYdzwX1gGi%2FHgcMdGJbxhUlVjXigOINJ0uYyszlSHVm948Oy3DioYamjtRdTntEkWZ31ifW2aLdCbptxTf8wgzEZayfWAQd3YFOG0LPigMSVyRhtEVD2L%2BfHUfKuyHKu%2Bs9iiiR2nlReoKnYJRcRbadPV4mdQ%2BZ810vN%2FeT33hAJzKtP70tCgmN%2F5UK%2BMaPKhUbqXNY8J3n425n8fCP5vnGhXNuulYzWsYtAu2OyU6ltcZCWIIreW73DN5erVEIXyOD2FenKpc%2FQEkuOwpwX5Q7I3TDe9vOr8FcfGDlcmzktjMxuKz5rzTYiC3ujYeWk3N2Ds79A%2BjLneuIsFj0ngtGJc0%2FzCoqdlL1zgmWOaqFNwLMFIyvufbRjQNDqwZgSC%2FI%2BSbHpfaZ3NPTBgUurGvdEUi3CTN6lNQtM8q%2BmVmyt%2FToO52fqPQEqub1eRaGirPyeUTacwlBgK7zcw1u%2BbvQY6pgEfflNNNIjX1%2BF5Gr%2F9MI3DZt2p9mMvenl0FWU4RNUaAd2zRPKxTuzjT6EYOvS1BzfyW6FZy3SoRWy%2Bb56ofkVm%2B%2FBUrrjj%2BzQ1ENVHpHdieg9e0dS5pyb15iTiNLm%2FRoJ%2FtXOSmU1NqaROhP1wAKVBM3SbAkI16%2BeBXaO8Qi0MQ170gQeacfCT2YmjKdcF6k20QmSJY2mqA26CmTNAaL8wXSDLl0XF&X-Amz-Signature=899661f20ad431a0fd223d9f2ac0e18222a53a9a280e39b16b669b5984f1e87d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZLOX7OF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIE6P2VKZpYsarxObJv4E68Pg0uANUZhFWBkqOPOn%2FzHpAiEA3R3rDb8cRq7xwe10HnESYEMN0cv5wPFV2dtwmg22M88qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBbnrx9T%2BqO0Sp3ijCrcA%2BPh6x8lJSdL8FK70TSz8JouRBrx3PI1mPu86D2f7ElPVqjaCYMDUrgB85gT6NE4urB79kaIt2MkRH79l6eFGGuiQjAfLGVLYafrdW74QeQI0%2B223LpUBvtGRWmAtNTFIi0t9gKeQDrPcTHzqeL0nVM2wlKzlmXdf3hB2sPCQbCkN3733hef2Z5c60Di%2F7ac1BSySvRLfq0fD%2BbTstbdBtFU7Z1XDhfwtoy%2ByHr1bYaWIZjqUOb6XPCM3So474V216M8IubTM%2F2Ry%2FBGzyv8uUJxVBQFuU7TgAh%2F0HswzSrHl89L8%2BK757ovfCwTuaF%2BAf1k0rmTUSZas2V9rHQATemIlYYDZxaOVajSAks%2FljZ%2FeG5g27v00sllnt4Acf76LJ0O6fNXYZmCr5VWBjoDpPDROXLbdxYhNOczBPkoAVDkZPJkK87X%2BnowVxsfqxKu8npyIwXLWOR6VARFglO1GRIPr2Q1juXidi2JvS0tV%2FK6L9XTy26%2F1DTITXj8mCwQJV2iUBPdPC4VfzdwjRXI4IGBWAQdzeUE%2FQLBOLKm0R7Zo5BAsZmAD4%2FjPPB2meIQW7LtqK6h06d2599JJLpeW07eO08Dnxh2W5YONG7V%2Bv2E0A9T7F%2F%2FKIPH8HFbMODvm70GOqUBFc3maWiP05ylZwh5zutmZPQYdwmqyRRBFCjIqo3VrQ%2BYwQI3mTcK%2F9H6c14l01G1t1ZAXg%2FUHhKAHPom7r0wjJlyeG0pJv%2FDYc1pxzvQIVv1yCm7t51E9EQG7%2FXK6WViEofrPLVaSX4fIubedYcphSmPdkVoi0jAo3YtYypAQpM5SwbXq2t2%2BRP6x%2Bkn%2BvSwZr%2B4o4zdy0By4Tn8QzIkDKY%2FlOEN&X-Amz-Signature=bacf02804f891857b866aab5177255097ee99c677b59318de35cdbcdd11f0a90&X-Amz-SignedHeaders=host&x-id=GetObject)
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