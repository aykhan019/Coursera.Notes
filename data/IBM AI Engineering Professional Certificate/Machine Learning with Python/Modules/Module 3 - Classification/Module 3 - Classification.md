

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642UTBWZF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDzORYQEU3txMcUwZ3crEzY%2BueoByBhsFTs2BArdDLQzgIhALu43LrI3vlraFrH5zYqEZx9dFL7OYNb76TKQBps7NFMKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhzZBxOZIMkKRIhuoq3AP5VD8ico3weSVYauditZznb0jWW%2FPfT7hrA6B4%2B7J1OJ1iYdYy79ug9E7%2Bk2mid1cQurC%2FX0daJMOqlFleHaAz3CIFnn%2BZ9CsvkEuMrg6TgGklaZ1Vcm%2BguiN%2B9IXjvFSRV3Koc1x5wsLNHlfJyC4IuUYttc7N9BlhZT8zHRA0YkpdmeMTj75ox1vCVaO6T3mbQD0OwM5Z3ODZcCwbwQbzeZE5NN%2B2mmHRb9HJp0HN1m6Z0n21AxCXw3saCfA3gqR%2BurHxmPsLc8BrD8OINL1dsqjY%2FCQ1EY0zDkF8FN8pC5AhXZFN%2Bb1eYTOKd8P80ArKFVD%2FadzI9JYLIsWS%2FGT0XVV2kRsAjYDVp1zhah%2BSeVk%2FBLZLP4Ra8X3BwV113nNC9mrQmdxrMAA8%2FMt%2FQ3z7LHxYHE7CIfsrsExbQHi15lCZeFlxDOcEYqPwYELf07bKLyo9uAzs4tcpa5AZFS2Ru%2F3rBkpR5fMVbTAd3Sugj5iPAPFVoodtyrd5alwrx6w6f2Z4QpuXgqP8vQNKXb6%2BLdH66768JFO%2FAnCXFG8ChRBPTQfSOYrvkrVVWR%2Bye3JJsitxCsiuzZ87oTKE%2FyLiErho3ihO0aai5r2h9rP4Fc%2FWt%2BebgLdSpdlU4zDyspu9BjqkAcJl1FMl9UIYTTEMuP1lGy3W8JD%2BQMIlNEEThq6Qmnb5vd7y49GAOW8WuI%2Fiiz9r3eoObO3%2B9FjmVuA451IU58zeETKvvxelq2QcpXdt9BD5ha1v0VRaiUNua4Xq%2FR1gfqcg%2BSJ0a3Tka%2FFlTMU02Hp7YnDYOwOzbdguaafKPSQoh9T%2BvnNlm%2BAMTqCZ9pZSUlCXd3xOum3o7Mlf6l7LF2EsK2R4&X-Amz-Signature=6523788ed31295c78497108b23a01dbf4ee72f1101d3e7050b7a0c1beebcadc2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642UTBWZF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDzORYQEU3txMcUwZ3crEzY%2BueoByBhsFTs2BArdDLQzgIhALu43LrI3vlraFrH5zYqEZx9dFL7OYNb76TKQBps7NFMKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhzZBxOZIMkKRIhuoq3AP5VD8ico3weSVYauditZznb0jWW%2FPfT7hrA6B4%2B7J1OJ1iYdYy79ug9E7%2Bk2mid1cQurC%2FX0daJMOqlFleHaAz3CIFnn%2BZ9CsvkEuMrg6TgGklaZ1Vcm%2BguiN%2B9IXjvFSRV3Koc1x5wsLNHlfJyC4IuUYttc7N9BlhZT8zHRA0YkpdmeMTj75ox1vCVaO6T3mbQD0OwM5Z3ODZcCwbwQbzeZE5NN%2B2mmHRb9HJp0HN1m6Z0n21AxCXw3saCfA3gqR%2BurHxmPsLc8BrD8OINL1dsqjY%2FCQ1EY0zDkF8FN8pC5AhXZFN%2Bb1eYTOKd8P80ArKFVD%2FadzI9JYLIsWS%2FGT0XVV2kRsAjYDVp1zhah%2BSeVk%2FBLZLP4Ra8X3BwV113nNC9mrQmdxrMAA8%2FMt%2FQ3z7LHxYHE7CIfsrsExbQHi15lCZeFlxDOcEYqPwYELf07bKLyo9uAzs4tcpa5AZFS2Ru%2F3rBkpR5fMVbTAd3Sugj5iPAPFVoodtyrd5alwrx6w6f2Z4QpuXgqP8vQNKXb6%2BLdH66768JFO%2FAnCXFG8ChRBPTQfSOYrvkrVVWR%2Bye3JJsitxCsiuzZ87oTKE%2FyLiErho3ihO0aai5r2h9rP4Fc%2FWt%2BebgLdSpdlU4zDyspu9BjqkAcJl1FMl9UIYTTEMuP1lGy3W8JD%2BQMIlNEEThq6Qmnb5vd7y49GAOW8WuI%2Fiiz9r3eoObO3%2B9FjmVuA451IU58zeETKvvxelq2QcpXdt9BD5ha1v0VRaiUNua4Xq%2FR1gfqcg%2BSJ0a3Tka%2FFlTMU02Hp7YnDYOwOzbdguaafKPSQoh9T%2BvnNlm%2BAMTqCZ9pZSUlCXd3xOum3o7Mlf6l7LF2EsK2R4&X-Amz-Signature=70352ba21e37c28fe0f9e055f7f7277600dd8eb354f818aaf1d0ba4af2853852&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642UTBWZF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDzORYQEU3txMcUwZ3crEzY%2BueoByBhsFTs2BArdDLQzgIhALu43LrI3vlraFrH5zYqEZx9dFL7OYNb76TKQBps7NFMKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhzZBxOZIMkKRIhuoq3AP5VD8ico3weSVYauditZznb0jWW%2FPfT7hrA6B4%2B7J1OJ1iYdYy79ug9E7%2Bk2mid1cQurC%2FX0daJMOqlFleHaAz3CIFnn%2BZ9CsvkEuMrg6TgGklaZ1Vcm%2BguiN%2B9IXjvFSRV3Koc1x5wsLNHlfJyC4IuUYttc7N9BlhZT8zHRA0YkpdmeMTj75ox1vCVaO6T3mbQD0OwM5Z3ODZcCwbwQbzeZE5NN%2B2mmHRb9HJp0HN1m6Z0n21AxCXw3saCfA3gqR%2BurHxmPsLc8BrD8OINL1dsqjY%2FCQ1EY0zDkF8FN8pC5AhXZFN%2Bb1eYTOKd8P80ArKFVD%2FadzI9JYLIsWS%2FGT0XVV2kRsAjYDVp1zhah%2BSeVk%2FBLZLP4Ra8X3BwV113nNC9mrQmdxrMAA8%2FMt%2FQ3z7LHxYHE7CIfsrsExbQHi15lCZeFlxDOcEYqPwYELf07bKLyo9uAzs4tcpa5AZFS2Ru%2F3rBkpR5fMVbTAd3Sugj5iPAPFVoodtyrd5alwrx6w6f2Z4QpuXgqP8vQNKXb6%2BLdH66768JFO%2FAnCXFG8ChRBPTQfSOYrvkrVVWR%2Bye3JJsitxCsiuzZ87oTKE%2FyLiErho3ihO0aai5r2h9rP4Fc%2FWt%2BebgLdSpdlU4zDyspu9BjqkAcJl1FMl9UIYTTEMuP1lGy3W8JD%2BQMIlNEEThq6Qmnb5vd7y49GAOW8WuI%2Fiiz9r3eoObO3%2B9FjmVuA451IU58zeETKvvxelq2QcpXdt9BD5ha1v0VRaiUNua4Xq%2FR1gfqcg%2BSJ0a3Tka%2FFlTMU02Hp7YnDYOwOzbdguaafKPSQoh9T%2BvnNlm%2BAMTqCZ9pZSUlCXd3xOum3o7Mlf6l7LF2EsK2R4&X-Amz-Signature=66d995218ba3dac24b6b0670a1522536de3af586da60f70a1fae134627f994de&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SND6BIP5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDhke7Cf6aR6TTRmE%2B48HuJu1VpN1euKRo0pbbkmX5SXQIhAKKahop1jqYcgMDO81OuzWzFzahyhS%2Bl%2F8hEYEhNiiPpKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqRnto71fpErnep1Eq3APrFbEAs2EIzA8OPBgnJytoLiQS215OY0E91uQWk0yQRKvVLmDAzPTJqBTjWXgIVMMDacOt1uRJuRCx%2F2Uguk7S6j3l%2FKlQF5USmXEwjWj8d9DkaNfVmAf9yJ9Gb2QPM0JXgAaVuWqkzDDKaXEdUZrCTgNibJOvn12%2FCCn04ZEQeGhh0X7z7Lbkl1eqooQvSaxuHLF9ukr9G3qpWqcis%2FGiHeizbOvGzXQhdgYSVJoPZOaoC%2BQ1UpWqldzj%2F1juePqcsSOMRlUC2lEjTmiogKVlX1lBmc2iNq7ssmM7Viy4hvA5pyjyte1cRrXjmBC3TOclZ1y6r%2BSiG9MbQjdaoIs4x745aVV32Hfh4j8vQ85xJfcls5cPobh05RWw5UTVMAlMRPOuEBBshbDDzGd%2Fk8HsfHDk927JvcDxpyUNzqL1ML4FqTqwZwFeObzLrG5VnXEDdPAzk6RjK1Pq69ZsFtGAT1OGq5oYpzL6nNjRezQw89agopsqoVVUrNH8j5rgGd2UCTvEb%2FS14WpdfxL4H4bCpcUtwhyhr0ssKfvYHve3UVsTUSzj9nFnTgPPg9rzcBcVvBmQwghoNoMNkOqSWiT5hYtCWK3xO60jDQlRO0Uk7y3JJrfzPt%2BW%2BjNW9jDUspu9BjqkATrBZaeY3oV23PwF07RArr7V4GKGXNrF%2B23IZjygX9d%2BK8ShEt%2Be1meEa31CFEDd6LrAxUtckRt8WPOqUOBgTRZixrT8qF0MDbQgE9c2uuaaTNzbnubgKD4KxxQwmcoKHs5htLn61hhQbRPD1hY00UcSptjRzbgpo0QMuuLOIoEW9yY1VPRxpP9A3iOs3tOD87E648%2F0PlD2tQZG40zLnpOdiO0U&X-Amz-Signature=79bc1495466ca550b62d3f50f3a6aa316ab0e37e73782853271506634872dc67&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SND6BIP5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDhke7Cf6aR6TTRmE%2B48HuJu1VpN1euKRo0pbbkmX5SXQIhAKKahop1jqYcgMDO81OuzWzFzahyhS%2Bl%2F8hEYEhNiiPpKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqRnto71fpErnep1Eq3APrFbEAs2EIzA8OPBgnJytoLiQS215OY0E91uQWk0yQRKvVLmDAzPTJqBTjWXgIVMMDacOt1uRJuRCx%2F2Uguk7S6j3l%2FKlQF5USmXEwjWj8d9DkaNfVmAf9yJ9Gb2QPM0JXgAaVuWqkzDDKaXEdUZrCTgNibJOvn12%2FCCn04ZEQeGhh0X7z7Lbkl1eqooQvSaxuHLF9ukr9G3qpWqcis%2FGiHeizbOvGzXQhdgYSVJoPZOaoC%2BQ1UpWqldzj%2F1juePqcsSOMRlUC2lEjTmiogKVlX1lBmc2iNq7ssmM7Viy4hvA5pyjyte1cRrXjmBC3TOclZ1y6r%2BSiG9MbQjdaoIs4x745aVV32Hfh4j8vQ85xJfcls5cPobh05RWw5UTVMAlMRPOuEBBshbDDzGd%2Fk8HsfHDk927JvcDxpyUNzqL1ML4FqTqwZwFeObzLrG5VnXEDdPAzk6RjK1Pq69ZsFtGAT1OGq5oYpzL6nNjRezQw89agopsqoVVUrNH8j5rgGd2UCTvEb%2FS14WpdfxL4H4bCpcUtwhyhr0ssKfvYHve3UVsTUSzj9nFnTgPPg9rzcBcVvBmQwghoNoMNkOqSWiT5hYtCWK3xO60jDQlRO0Uk7y3JJrfzPt%2BW%2BjNW9jDUspu9BjqkATrBZaeY3oV23PwF07RArr7V4GKGXNrF%2B23IZjygX9d%2BK8ShEt%2Be1meEa31CFEDd6LrAxUtckRt8WPOqUOBgTRZixrT8qF0MDbQgE9c2uuaaTNzbnubgKD4KxxQwmcoKHs5htLn61hhQbRPD1hY00UcSptjRzbgpo0QMuuLOIoEW9yY1VPRxpP9A3iOs3tOD87E648%2F0PlD2tQZG40zLnpOdiO0U&X-Amz-Signature=f96e1765703b2db5b340a2d04023a4df3af70877f099fc88e604851835a39c58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642UTBWZF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJIMEYCIQDzORYQEU3txMcUwZ3crEzY%2BueoByBhsFTs2BArdDLQzgIhALu43LrI3vlraFrH5zYqEZx9dFL7OYNb76TKQBps7NFMKogECIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxhzZBxOZIMkKRIhuoq3AP5VD8ico3weSVYauditZznb0jWW%2FPfT7hrA6B4%2B7J1OJ1iYdYy79ug9E7%2Bk2mid1cQurC%2FX0daJMOqlFleHaAz3CIFnn%2BZ9CsvkEuMrg6TgGklaZ1Vcm%2BguiN%2B9IXjvFSRV3Koc1x5wsLNHlfJyC4IuUYttc7N9BlhZT8zHRA0YkpdmeMTj75ox1vCVaO6T3mbQD0OwM5Z3ODZcCwbwQbzeZE5NN%2B2mmHRb9HJp0HN1m6Z0n21AxCXw3saCfA3gqR%2BurHxmPsLc8BrD8OINL1dsqjY%2FCQ1EY0zDkF8FN8pC5AhXZFN%2Bb1eYTOKd8P80ArKFVD%2FadzI9JYLIsWS%2FGT0XVV2kRsAjYDVp1zhah%2BSeVk%2FBLZLP4Ra8X3BwV113nNC9mrQmdxrMAA8%2FMt%2FQ3z7LHxYHE7CIfsrsExbQHi15lCZeFlxDOcEYqPwYELf07bKLyo9uAzs4tcpa5AZFS2Ru%2F3rBkpR5fMVbTAd3Sugj5iPAPFVoodtyrd5alwrx6w6f2Z4QpuXgqP8vQNKXb6%2BLdH66768JFO%2FAnCXFG8ChRBPTQfSOYrvkrVVWR%2Bye3JJsitxCsiuzZ87oTKE%2FyLiErho3ihO0aai5r2h9rP4Fc%2FWt%2BebgLdSpdlU4zDyspu9BjqkAcJl1FMl9UIYTTEMuP1lGy3W8JD%2BQMIlNEEThq6Qmnb5vd7y49GAOW8WuI%2Fiiz9r3eoObO3%2B9FjmVuA451IU58zeETKvvxelq2QcpXdt9BD5ha1v0VRaiUNua4Xq%2FR1gfqcg%2BSJ0a3Tka%2FFlTMU02Hp7YnDYOwOzbdguaafKPSQoh9T%2BvnNlm%2BAMTqCZ9pZSUlCXd3xOum3o7Mlf6l7LF2EsK2R4&X-Amz-Signature=9a44c74d000b71143333d6da84cd5df45b7aa3dd3aa694939e1c9e2fed0575d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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