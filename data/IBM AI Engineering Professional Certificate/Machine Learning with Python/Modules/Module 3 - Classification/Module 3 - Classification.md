

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUT7OCM6%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGPDcuQhsCFypPe6zjAe5ODKyCzfdbUW8khbF4u4zuhNAiEAku23VSGs3FVKGp11l10f3m0VVJkMH4YCCL5lA7jxTZIq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDN4W5wAyuWwf51wQ0yrcA20gjzIMe7U%2FjyOp7meWIjXlrPDTNGv1X4yNr6VDGQirH2kFx59oDIXGGln4juEz7YTsYsaS8L0FG7yKDHoiZ%2FaP%2BJZhN36lyAXg3qOadHYUXxzbEp3N6P2ejG1%2B49wyz1bHF1XYahB5rz%2FrtNr7aKEoPB3alXEE6wX4RBts83OrqBYa6WyPgTePvs0eA9qqMyljWi%2Bd2n%2BAm8MKVYLB35tD9xAHzNJJc3%2Bn8s9VfvsbjkXmjxWyp%2Bygf8W7cqyySi6ep8GVuj7LvmVEwzLqL1AlN6tkdb7WLGNl5mLgweyh9NnRPh0xCtECvL%2BSnaBLJyGAZB5e1GRh%2FaLbTew%2Fo4JeDS%2BThKB3%2F3xIgkLCCF3OoRB7UwXJpHJVDnECirgzUj7h7%2BIEKpN77gjQiq%2BslUuAeykNfR3lLXgm6Un4m9hUx5421s%2FqnxI1srMcXUu80OyglE7QXJ3jV1M%2Fd7fXztCMw3DZEQnuBBgLde%2FT5Wh80gZ5St7fbd3CtzB79LLQz6LKfmvGx5RoVorOlc6FR5xPXk9oSa9UzsqLdbsjhIDv%2FxoSI5x7n%2Ftt%2Bz2RTeCQ0xORUd%2FxQMwHtwbRHXztLjfgsq63Oo64O5BswK1F%2FaHHGI5I3AUIUYR6De%2B4MPeps74GOqUBXOTURkYylwBRZ83ifrVg%2BrrHJQ7bL%2BZkYG0IiKa4lbWhQu2qUUJwOoMhqR6%2B9Gm10JqlLPYdoCTdoMtDkWDnAdMejM8t9QbI%2BJQpbCNbIeuVA8Tg5ms28bfwxVvVz%2Fnl1MkYVg9Ayno3yhuNT4koSyd1WQFXIYbD0hu2OXESgpl4%2FPAviZdQ48f8n5BTrpX46ZLpMTMoTHgt8aTkdreZdpZcHfp8&X-Amz-Signature=e5051945d84ef0113bb2a899c6aa8a4303ebda079a7de2625242fb204e031f32&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUT7OCM6%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGPDcuQhsCFypPe6zjAe5ODKyCzfdbUW8khbF4u4zuhNAiEAku23VSGs3FVKGp11l10f3m0VVJkMH4YCCL5lA7jxTZIq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDN4W5wAyuWwf51wQ0yrcA20gjzIMe7U%2FjyOp7meWIjXlrPDTNGv1X4yNr6VDGQirH2kFx59oDIXGGln4juEz7YTsYsaS8L0FG7yKDHoiZ%2FaP%2BJZhN36lyAXg3qOadHYUXxzbEp3N6P2ejG1%2B49wyz1bHF1XYahB5rz%2FrtNr7aKEoPB3alXEE6wX4RBts83OrqBYa6WyPgTePvs0eA9qqMyljWi%2Bd2n%2BAm8MKVYLB35tD9xAHzNJJc3%2Bn8s9VfvsbjkXmjxWyp%2Bygf8W7cqyySi6ep8GVuj7LvmVEwzLqL1AlN6tkdb7WLGNl5mLgweyh9NnRPh0xCtECvL%2BSnaBLJyGAZB5e1GRh%2FaLbTew%2Fo4JeDS%2BThKB3%2F3xIgkLCCF3OoRB7UwXJpHJVDnECirgzUj7h7%2BIEKpN77gjQiq%2BslUuAeykNfR3lLXgm6Un4m9hUx5421s%2FqnxI1srMcXUu80OyglE7QXJ3jV1M%2Fd7fXztCMw3DZEQnuBBgLde%2FT5Wh80gZ5St7fbd3CtzB79LLQz6LKfmvGx5RoVorOlc6FR5xPXk9oSa9UzsqLdbsjhIDv%2FxoSI5x7n%2Ftt%2Bz2RTeCQ0xORUd%2FxQMwHtwbRHXztLjfgsq63Oo64O5BswK1F%2FaHHGI5I3AUIUYR6De%2B4MPeps74GOqUBXOTURkYylwBRZ83ifrVg%2BrrHJQ7bL%2BZkYG0IiKa4lbWhQu2qUUJwOoMhqR6%2B9Gm10JqlLPYdoCTdoMtDkWDnAdMejM8t9QbI%2BJQpbCNbIeuVA8Tg5ms28bfwxVvVz%2Fnl1MkYVg9Ayno3yhuNT4koSyd1WQFXIYbD0hu2OXESgpl4%2FPAviZdQ48f8n5BTrpX46ZLpMTMoTHgt8aTkdreZdpZcHfp8&X-Amz-Signature=79778443f035a46c48e431af6a9c8be58be3795aeead9f2be4e2f77dd60418ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUT7OCM6%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGPDcuQhsCFypPe6zjAe5ODKyCzfdbUW8khbF4u4zuhNAiEAku23VSGs3FVKGp11l10f3m0VVJkMH4YCCL5lA7jxTZIq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDN4W5wAyuWwf51wQ0yrcA20gjzIMe7U%2FjyOp7meWIjXlrPDTNGv1X4yNr6VDGQirH2kFx59oDIXGGln4juEz7YTsYsaS8L0FG7yKDHoiZ%2FaP%2BJZhN36lyAXg3qOadHYUXxzbEp3N6P2ejG1%2B49wyz1bHF1XYahB5rz%2FrtNr7aKEoPB3alXEE6wX4RBts83OrqBYa6WyPgTePvs0eA9qqMyljWi%2Bd2n%2BAm8MKVYLB35tD9xAHzNJJc3%2Bn8s9VfvsbjkXmjxWyp%2Bygf8W7cqyySi6ep8GVuj7LvmVEwzLqL1AlN6tkdb7WLGNl5mLgweyh9NnRPh0xCtECvL%2BSnaBLJyGAZB5e1GRh%2FaLbTew%2Fo4JeDS%2BThKB3%2F3xIgkLCCF3OoRB7UwXJpHJVDnECirgzUj7h7%2BIEKpN77gjQiq%2BslUuAeykNfR3lLXgm6Un4m9hUx5421s%2FqnxI1srMcXUu80OyglE7QXJ3jV1M%2Fd7fXztCMw3DZEQnuBBgLde%2FT5Wh80gZ5St7fbd3CtzB79LLQz6LKfmvGx5RoVorOlc6FR5xPXk9oSa9UzsqLdbsjhIDv%2FxoSI5x7n%2Ftt%2Bz2RTeCQ0xORUd%2FxQMwHtwbRHXztLjfgsq63Oo64O5BswK1F%2FaHHGI5I3AUIUYR6De%2B4MPeps74GOqUBXOTURkYylwBRZ83ifrVg%2BrrHJQ7bL%2BZkYG0IiKa4lbWhQu2qUUJwOoMhqR6%2B9Gm10JqlLPYdoCTdoMtDkWDnAdMejM8t9QbI%2BJQpbCNbIeuVA8Tg5ms28bfwxVvVz%2Fnl1MkYVg9Ayno3yhuNT4koSyd1WQFXIYbD0hu2OXESgpl4%2FPAviZdQ48f8n5BTrpX46ZLpMTMoTHgt8aTkdreZdpZcHfp8&X-Amz-Signature=176276bba0e5081ba9b5316117fb573fc16f0147d2f8ab4ac4207209b796ed8f&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFOJTRKR%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICFDduPRnn4LyL66XFuIKMmXlz0qwoakqcR9nUgpqbbDAiEA40fnbGyJfJVhk9FMlP3bfJuehCINCNsSCksWCHVJfXMq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDAMhfZ4t9o1XzpTRbyrcA1ku4dHM7pzLt8tzCWQbOe70MLMlfmTYDk6IQ3WTS7IpHp91rmd2DcpdJ5xwvP5aXHXMP60MII6M%2ByjvtmEudYoAosvk%2Bdy96XGuFABCep39RY6lJXslAMqmBjMgAevQPfpshHj7MO2UrKhn2I9H%2BX9%2BdNBz9IXvODdDZ%2Femgv%2FegiVJ8CF74bl7aGTgHx%2BQVAkMT8q04bp5%2FJXyIrvcuSjxC8cBlK8d1hxk%2BNRSIr%2BI2Q%2BXrzTQE6HMPbsARuMwYmnhT9f0oRXvyof5HkIxdMPvG9tJJaWpD45O4c88oI3NwwIiYN2hJX89vE%2FWT3oJmi6ACJ6%2BRMk8VmwJ1Sh3CDydxcAHTz760U%2FmvwIeDk%2BEIA1MZYR0%2BvMWXswdyB28x9Beyc6LSnMwryq6HUYASydlpxxhO%2BIsmLc6d4LiPSe9meidwBpUo96n%2B%2F9cIUOOeCD75ljmdl8PVQCxFk8WwNocWZzZCn%2BTUzGqdyOIykaEWaw6vDFk5Ep4YFmi1o4Mmzk5h7a5KsFjHfIayKmPz5qfD%2BvgmnUdjZLQX%2FhIlv9bJcHLwj%2FGQdEjI27%2Fa5uB%2FZaQfqr8X%2BnULqXBuFnH51vT1H8sRsTUznUPpUHmePVYOQBs4cH7F7mXmHbgMJ2qs74GOqUB8gfxwgexq3KQMAJ%2Fc%2BomzFK07Bq1d3MZVN8wXrpahChtMUnznjIjXGkVRMDPCQ6ZbEDjpAzXKvcg35GWFIQWUA6mazapCxp3aN%2BNr4Vbu9wKyz7jyYbS6MvijX%2FQ5hpZQIf3n1uieDKyDZ33lccz0Hxo5w5wtcX4ga%2BVKd7YY9%2Bm8rHMJaOsIEZY0lOT3yEU43krh09ypnbVjgWGEebg1veSpnDT&X-Amz-Signature=bafb7e7c8dddbe121b343dfca670b8916fad4e86d1bd16e0dd7d05c6066f62e6&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFOJTRKR%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICFDduPRnn4LyL66XFuIKMmXlz0qwoakqcR9nUgpqbbDAiEA40fnbGyJfJVhk9FMlP3bfJuehCINCNsSCksWCHVJfXMq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDAMhfZ4t9o1XzpTRbyrcA1ku4dHM7pzLt8tzCWQbOe70MLMlfmTYDk6IQ3WTS7IpHp91rmd2DcpdJ5xwvP5aXHXMP60MII6M%2ByjvtmEudYoAosvk%2Bdy96XGuFABCep39RY6lJXslAMqmBjMgAevQPfpshHj7MO2UrKhn2I9H%2BX9%2BdNBz9IXvODdDZ%2Femgv%2FegiVJ8CF74bl7aGTgHx%2BQVAkMT8q04bp5%2FJXyIrvcuSjxC8cBlK8d1hxk%2BNRSIr%2BI2Q%2BXrzTQE6HMPbsARuMwYmnhT9f0oRXvyof5HkIxdMPvG9tJJaWpD45O4c88oI3NwwIiYN2hJX89vE%2FWT3oJmi6ACJ6%2BRMk8VmwJ1Sh3CDydxcAHTz760U%2FmvwIeDk%2BEIA1MZYR0%2BvMWXswdyB28x9Beyc6LSnMwryq6HUYASydlpxxhO%2BIsmLc6d4LiPSe9meidwBpUo96n%2B%2F9cIUOOeCD75ljmdl8PVQCxFk8WwNocWZzZCn%2BTUzGqdyOIykaEWaw6vDFk5Ep4YFmi1o4Mmzk5h7a5KsFjHfIayKmPz5qfD%2BvgmnUdjZLQX%2FhIlv9bJcHLwj%2FGQdEjI27%2Fa5uB%2FZaQfqr8X%2BnULqXBuFnH51vT1H8sRsTUznUPpUHmePVYOQBs4cH7F7mXmHbgMJ2qs74GOqUB8gfxwgexq3KQMAJ%2Fc%2BomzFK07Bq1d3MZVN8wXrpahChtMUnznjIjXGkVRMDPCQ6ZbEDjpAzXKvcg35GWFIQWUA6mazapCxp3aN%2BNr4Vbu9wKyz7jyYbS6MvijX%2FQ5hpZQIf3n1uieDKyDZ33lccz0Hxo5w5wtcX4ga%2BVKd7YY9%2Bm8rHMJaOsIEZY0lOT3yEU43krh09ypnbVjgWGEebg1veSpnDT&X-Amz-Signature=87d60f536701a206197e5d3252fcbefe5d12696a14e76ba0cc938666749241b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUT7OCM6%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGPDcuQhsCFypPe6zjAe5ODKyCzfdbUW8khbF4u4zuhNAiEAku23VSGs3FVKGp11l10f3m0VVJkMH4YCCL5lA7jxTZIq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDN4W5wAyuWwf51wQ0yrcA20gjzIMe7U%2FjyOp7meWIjXlrPDTNGv1X4yNr6VDGQirH2kFx59oDIXGGln4juEz7YTsYsaS8L0FG7yKDHoiZ%2FaP%2BJZhN36lyAXg3qOadHYUXxzbEp3N6P2ejG1%2B49wyz1bHF1XYahB5rz%2FrtNr7aKEoPB3alXEE6wX4RBts83OrqBYa6WyPgTePvs0eA9qqMyljWi%2Bd2n%2BAm8MKVYLB35tD9xAHzNJJc3%2Bn8s9VfvsbjkXmjxWyp%2Bygf8W7cqyySi6ep8GVuj7LvmVEwzLqL1AlN6tkdb7WLGNl5mLgweyh9NnRPh0xCtECvL%2BSnaBLJyGAZB5e1GRh%2FaLbTew%2Fo4JeDS%2BThKB3%2F3xIgkLCCF3OoRB7UwXJpHJVDnECirgzUj7h7%2BIEKpN77gjQiq%2BslUuAeykNfR3lLXgm6Un4m9hUx5421s%2FqnxI1srMcXUu80OyglE7QXJ3jV1M%2Fd7fXztCMw3DZEQnuBBgLde%2FT5Wh80gZ5St7fbd3CtzB79LLQz6LKfmvGx5RoVorOlc6FR5xPXk9oSa9UzsqLdbsjhIDv%2FxoSI5x7n%2Ftt%2Bz2RTeCQ0xORUd%2FxQMwHtwbRHXztLjfgsq63Oo64O5BswK1F%2FaHHGI5I3AUIUYR6De%2B4MPeps74GOqUBXOTURkYylwBRZ83ifrVg%2BrrHJQ7bL%2BZkYG0IiKa4lbWhQu2qUUJwOoMhqR6%2B9Gm10JqlLPYdoCTdoMtDkWDnAdMejM8t9QbI%2BJQpbCNbIeuVA8Tg5ms28bfwxVvVz%2Fnl1MkYVg9Ayno3yhuNT4koSyd1WQFXIYbD0hu2OXESgpl4%2FPAviZdQ48f8n5BTrpX46ZLpMTMoTHgt8aTkdreZdpZcHfp8&X-Amz-Signature=29575088dc9a256d023ecfd7c69f82855504b7aa95189996490ab20d4d4b3714&X-Amz-SignedHeaders=host&x-id=GetObject)
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