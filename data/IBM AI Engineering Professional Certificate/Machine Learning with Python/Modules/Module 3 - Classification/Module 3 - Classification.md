

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROWZ5NHS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEZzbgRbdkhrEMufmqhsQV4zSUseBlnrWeYE6un5kdgUAiEAv2%2BOsRnT5S9Vlw1qDNesh6A308nSmAb0MdsNWj65YSsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAyBXYcRQ3FTnStQiSrcA%2FCU1pyPZJeQ8T6srdrDHYCdYF6hQitDkV8dmDf1cuKFB6LL%2F8rqH5Gy4t9lR4sG0fjAGrJZOAyh4ztX%2BLJ3D4E89RJXMPwXUpIxEj0LIDMxjJ%2B9j2SYawkE%2BWBn2oNEGJNj38tCSne46Hu1oOFMQMbfQpTNzwamjctqomV2Qq8xLFn58VrklIAW2HyHbV2pbz24u2QJJebYfyvWDSULkkmGSyO3FvYfm%2BqXXVtiK885jFRyRnL3o7gf0cA374aJoW8kBE1rwOY3UcRzC7N%2FdFJSnQrM32T%2F57IStI90J8jjT3tXZtY8Vn9FfhkfPMyg0Xzo2Luj9jSRPSmPUXStQIlNK6pVSRLkN%2BfMYyon0I3Cp5aRrx%2FmBxYRjgd5h2s7Nnwc6iUFVn0r5IVLXA3nbOL939jpQY8kdqdI5764ECmSW9WvHA%2B1yhp6vQsN20O85xTddpHvCDr0fAtexF0zo84xiewRfo4eBOXf4HYW6S1b%2Bi7TrIRBg7KebIDg8XVTrObAg%2Fo5xznR67DZ%2FuvSzSR3KGzRHARbcSpPKtTGARBwqbqqYTTuXPf73KLyhfUOdYfJU0lsvw61eB4lL%2FW38SBMigiQkNElMes6TuRE7qyJK1UFrOx7UwZ3JoJHMKm6gb0GOqUB1aiMi%2FFa3A1kqnHB2O%2FY6ZIoh5zGvMoWDnqQ87GZoHOv4mqa8I9Ibu%2B1k%2BpmPhiUupJmAiGsZt5sHshpMK%2Fv8vVHeUs1j8WA9iZtUZeqXXXjECF6%2BXAvip7P6GEw3V%2B9NYDZ2QlkC1PcsHahwdL3qqmeZp7DgCQWciySyZzNDnNkXtGgpf1ig%2F7YwgTQ0jcwMYI7xOzYrdfSxucB1P77Uba%2FAyGv&X-Amz-Signature=eac1c402b9dce9ff62248ecf5b0bc403140b151ed8a1f2607773f612765b174e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROWZ5NHS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEZzbgRbdkhrEMufmqhsQV4zSUseBlnrWeYE6un5kdgUAiEAv2%2BOsRnT5S9Vlw1qDNesh6A308nSmAb0MdsNWj65YSsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAyBXYcRQ3FTnStQiSrcA%2FCU1pyPZJeQ8T6srdrDHYCdYF6hQitDkV8dmDf1cuKFB6LL%2F8rqH5Gy4t9lR4sG0fjAGrJZOAyh4ztX%2BLJ3D4E89RJXMPwXUpIxEj0LIDMxjJ%2B9j2SYawkE%2BWBn2oNEGJNj38tCSne46Hu1oOFMQMbfQpTNzwamjctqomV2Qq8xLFn58VrklIAW2HyHbV2pbz24u2QJJebYfyvWDSULkkmGSyO3FvYfm%2BqXXVtiK885jFRyRnL3o7gf0cA374aJoW8kBE1rwOY3UcRzC7N%2FdFJSnQrM32T%2F57IStI90J8jjT3tXZtY8Vn9FfhkfPMyg0Xzo2Luj9jSRPSmPUXStQIlNK6pVSRLkN%2BfMYyon0I3Cp5aRrx%2FmBxYRjgd5h2s7Nnwc6iUFVn0r5IVLXA3nbOL939jpQY8kdqdI5764ECmSW9WvHA%2B1yhp6vQsN20O85xTddpHvCDr0fAtexF0zo84xiewRfo4eBOXf4HYW6S1b%2Bi7TrIRBg7KebIDg8XVTrObAg%2Fo5xznR67DZ%2FuvSzSR3KGzRHARbcSpPKtTGARBwqbqqYTTuXPf73KLyhfUOdYfJU0lsvw61eB4lL%2FW38SBMigiQkNElMes6TuRE7qyJK1UFrOx7UwZ3JoJHMKm6gb0GOqUB1aiMi%2FFa3A1kqnHB2O%2FY6ZIoh5zGvMoWDnqQ87GZoHOv4mqa8I9Ibu%2B1k%2BpmPhiUupJmAiGsZt5sHshpMK%2Fv8vVHeUs1j8WA9iZtUZeqXXXjECF6%2BXAvip7P6GEw3V%2B9NYDZ2QlkC1PcsHahwdL3qqmeZp7DgCQWciySyZzNDnNkXtGgpf1ig%2F7YwgTQ0jcwMYI7xOzYrdfSxucB1P77Uba%2FAyGv&X-Amz-Signature=4e1cb14ac88af36d19761e97fe289844cea11d728a253132e73c338bc89783f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROWZ5NHS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEZzbgRbdkhrEMufmqhsQV4zSUseBlnrWeYE6un5kdgUAiEAv2%2BOsRnT5S9Vlw1qDNesh6A308nSmAb0MdsNWj65YSsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAyBXYcRQ3FTnStQiSrcA%2FCU1pyPZJeQ8T6srdrDHYCdYF6hQitDkV8dmDf1cuKFB6LL%2F8rqH5Gy4t9lR4sG0fjAGrJZOAyh4ztX%2BLJ3D4E89RJXMPwXUpIxEj0LIDMxjJ%2B9j2SYawkE%2BWBn2oNEGJNj38tCSne46Hu1oOFMQMbfQpTNzwamjctqomV2Qq8xLFn58VrklIAW2HyHbV2pbz24u2QJJebYfyvWDSULkkmGSyO3FvYfm%2BqXXVtiK885jFRyRnL3o7gf0cA374aJoW8kBE1rwOY3UcRzC7N%2FdFJSnQrM32T%2F57IStI90J8jjT3tXZtY8Vn9FfhkfPMyg0Xzo2Luj9jSRPSmPUXStQIlNK6pVSRLkN%2BfMYyon0I3Cp5aRrx%2FmBxYRjgd5h2s7Nnwc6iUFVn0r5IVLXA3nbOL939jpQY8kdqdI5764ECmSW9WvHA%2B1yhp6vQsN20O85xTddpHvCDr0fAtexF0zo84xiewRfo4eBOXf4HYW6S1b%2Bi7TrIRBg7KebIDg8XVTrObAg%2Fo5xznR67DZ%2FuvSzSR3KGzRHARbcSpPKtTGARBwqbqqYTTuXPf73KLyhfUOdYfJU0lsvw61eB4lL%2FW38SBMigiQkNElMes6TuRE7qyJK1UFrOx7UwZ3JoJHMKm6gb0GOqUB1aiMi%2FFa3A1kqnHB2O%2FY6ZIoh5zGvMoWDnqQ87GZoHOv4mqa8I9Ibu%2B1k%2BpmPhiUupJmAiGsZt5sHshpMK%2Fv8vVHeUs1j8WA9iZtUZeqXXXjECF6%2BXAvip7P6GEw3V%2B9NYDZ2QlkC1PcsHahwdL3qqmeZp7DgCQWciySyZzNDnNkXtGgpf1ig%2F7YwgTQ0jcwMYI7xOzYrdfSxucB1P77Uba%2FAyGv&X-Amz-Signature=c23c3eeec84bd7d6a3a425b27e89b82ea0b35d51e972aa1bf68942ed358c7b17&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMJMZTDK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcYXW%2F%2FEbIiFdbi2O1V9soPxPmr2h0%2BR9s5X6S1z7MOAIhAPrEACKGlWjLlROEKOA1chAE3FKfQL2kS3B2cazXqgHyKogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxzzM0e50RCDRt6a%2Fwq3AOpSXVJejFhPdclJZV46M54faTkHVzz3k9WhSnikrZzQBPC2qVfEErgpwVlcK66r92%2FKgHOmJD34uBQTjEIUIBa3B9wIVzj%2FLcT%2BKV5UGIXwvvayhsvXri4uOfuZdDjMed60opNi67vumiTECP8yr4cGF8MvKYuPtxo%2BIgJua1EW11uQNliqFHop2%2Buzd0E0HdvydGmZmNouI%2FFJ5HbkHyE1RAdu0QAYic7BC2Vyhk%2F8SzbN22FOZhUiq6XiHx%2F6UiyWlZxf%2BneZPV%2BqWxMNKdYlyOr8C5O8tsE%2FKi6abBbACvKxvLfYp3gP77wl%2BthJVcANcvm5u9VdP93jk2qYyK%2FXgg9cA34QbfAwjRIYy%2FUfueQtrUIvYbXTnYnBWV73QF2O%2B9f9BM3zaActegZY4%2BRDeh8mxcsYU2ZKrymDGK%2BuF5H%2FaZvITUkC%2Bjlvv%2FYP6I%2FhuAECqviOAYrSIIbFYol2KQpI3rljoUx%2F9kKaIIDnLWiuXGwPxAetXDW5ig8cGz4pug3HQUMzDqTM9DzL1Vcb0viM9RU5paMQxb0E3dKSCNK%2BHRp5f%2B61YFbnnROIp2mcKU7FN3kU%2BMW0vTksnRyB6zegJ%2Fmc9yQDHcrzSoz%2FxvoZND9rFjprGJTSTDRuoG9BjqkAWREe2Z%2FWigZHyueBIERKuX0k8D%2FBy%2Fwi2mlrm%2BKUnvrLuZRX1MeIaceuvDOmiD1WM49ab%2B7Id6QrCHXphNPYOem666l%2BcGnwAQjt5%2BFXAG08HzgEnI6KOgbbjGUL9sW3ATYcNjlfFEfxOurjxh%2FoIIqW%2FWHlwaHv%2FPUtGqKsHwa3eMc7%2F1SZp5EdpOWlSQR8Yg3%2FQMNWXUbXqOZ2Va0vDBBLMbo&X-Amz-Signature=4053c4d6c4caa011843dff7b33b9fddba44485fd6cf31aee45c1ea3df0e1291e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMJMZTDK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcYXW%2F%2FEbIiFdbi2O1V9soPxPmr2h0%2BR9s5X6S1z7MOAIhAPrEACKGlWjLlROEKOA1chAE3FKfQL2kS3B2cazXqgHyKogECP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxzzM0e50RCDRt6a%2Fwq3AOpSXVJejFhPdclJZV46M54faTkHVzz3k9WhSnikrZzQBPC2qVfEErgpwVlcK66r92%2FKgHOmJD34uBQTjEIUIBa3B9wIVzj%2FLcT%2BKV5UGIXwvvayhsvXri4uOfuZdDjMed60opNi67vumiTECP8yr4cGF8MvKYuPtxo%2BIgJua1EW11uQNliqFHop2%2Buzd0E0HdvydGmZmNouI%2FFJ5HbkHyE1RAdu0QAYic7BC2Vyhk%2F8SzbN22FOZhUiq6XiHx%2F6UiyWlZxf%2BneZPV%2BqWxMNKdYlyOr8C5O8tsE%2FKi6abBbACvKxvLfYp3gP77wl%2BthJVcANcvm5u9VdP93jk2qYyK%2FXgg9cA34QbfAwjRIYy%2FUfueQtrUIvYbXTnYnBWV73QF2O%2B9f9BM3zaActegZY4%2BRDeh8mxcsYU2ZKrymDGK%2BuF5H%2FaZvITUkC%2Bjlvv%2FYP6I%2FhuAECqviOAYrSIIbFYol2KQpI3rljoUx%2F9kKaIIDnLWiuXGwPxAetXDW5ig8cGz4pug3HQUMzDqTM9DzL1Vcb0viM9RU5paMQxb0E3dKSCNK%2BHRp5f%2B61YFbnnROIp2mcKU7FN3kU%2BMW0vTksnRyB6zegJ%2Fmc9yQDHcrzSoz%2FxvoZND9rFjprGJTSTDRuoG9BjqkAWREe2Z%2FWigZHyueBIERKuX0k8D%2FBy%2Fwi2mlrm%2BKUnvrLuZRX1MeIaceuvDOmiD1WM49ab%2B7Id6QrCHXphNPYOem666l%2BcGnwAQjt5%2BFXAG08HzgEnI6KOgbbjGUL9sW3ATYcNjlfFEfxOurjxh%2FoIIqW%2FWHlwaHv%2FPUtGqKsHwa3eMc7%2F1SZp5EdpOWlSQR8Yg3%2FQMNWXUbXqOZ2Va0vDBBLMbo&X-Amz-Signature=c93c95b52eed17b91236b1f573dcbfbb404c5d05004368826c814b786ce75437&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROWZ5NHS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEZzbgRbdkhrEMufmqhsQV4zSUseBlnrWeYE6un5kdgUAiEAv2%2BOsRnT5S9Vlw1qDNesh6A308nSmAb0MdsNWj65YSsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAyBXYcRQ3FTnStQiSrcA%2FCU1pyPZJeQ8T6srdrDHYCdYF6hQitDkV8dmDf1cuKFB6LL%2F8rqH5Gy4t9lR4sG0fjAGrJZOAyh4ztX%2BLJ3D4E89RJXMPwXUpIxEj0LIDMxjJ%2B9j2SYawkE%2BWBn2oNEGJNj38tCSne46Hu1oOFMQMbfQpTNzwamjctqomV2Qq8xLFn58VrklIAW2HyHbV2pbz24u2QJJebYfyvWDSULkkmGSyO3FvYfm%2BqXXVtiK885jFRyRnL3o7gf0cA374aJoW8kBE1rwOY3UcRzC7N%2FdFJSnQrM32T%2F57IStI90J8jjT3tXZtY8Vn9FfhkfPMyg0Xzo2Luj9jSRPSmPUXStQIlNK6pVSRLkN%2BfMYyon0I3Cp5aRrx%2FmBxYRjgd5h2s7Nnwc6iUFVn0r5IVLXA3nbOL939jpQY8kdqdI5764ECmSW9WvHA%2B1yhp6vQsN20O85xTddpHvCDr0fAtexF0zo84xiewRfo4eBOXf4HYW6S1b%2Bi7TrIRBg7KebIDg8XVTrObAg%2Fo5xznR67DZ%2FuvSzSR3KGzRHARbcSpPKtTGARBwqbqqYTTuXPf73KLyhfUOdYfJU0lsvw61eB4lL%2FW38SBMigiQkNElMes6TuRE7qyJK1UFrOx7UwZ3JoJHMKm6gb0GOqUB1aiMi%2FFa3A1kqnHB2O%2FY6ZIoh5zGvMoWDnqQ87GZoHOv4mqa8I9Ibu%2B1k%2BpmPhiUupJmAiGsZt5sHshpMK%2Fv8vVHeUs1j8WA9iZtUZeqXXXjECF6%2BXAvip7P6GEw3V%2B9NYDZ2QlkC1PcsHahwdL3qqmeZp7DgCQWciySyZzNDnNkXtGgpf1ig%2F7YwgTQ0jcwMYI7xOzYrdfSxucB1P77Uba%2FAyGv&X-Amz-Signature=ea190188aa142ef6b85648646fbd8e3c9b1e5e937aae07e03fbd64613d2dfc48&X-Amz-SignedHeaders=host&x-id=GetObject)
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