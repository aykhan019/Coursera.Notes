

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OT2MTZ6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrSA3ZtsxAp3sKA4ZoDopFm%2BM3YGL8PnLTL%2BWQW9KVZQIhAOTiJREtyBiSZ%2BVTZgNV%2FRLPE4RImG1bfJJaw5%2B5ol%2B9KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9S7zUmPMyyR0OzSAq3AMjFagd7bBNRNz%2FwZHr9LV3AX1NwP%2FIL%2BlSmazXu0IHPbDIcAkfFDIAs3AjThS1imCQqYZ2zvZrwv%2Bag2298wuD1u7dlczAqlvg7IBDVFM%2BHn0qsskcfOJpg%2FnQo3Y9oXN9PI%2FoIU%2Fz7fuwmF0yPYLBE5q04UU%2FZPWCYFzMKooJ0mXXACmO9PhGAGF4ayGXpnZ9vohm%2Beh45jrLzI7OP%2BsLqn8hqNAkrGVGHQj2RyY0xQAtb1RVwOymGIRx8kRTPFSgI4OlhCHYnU00zGD60JBUT5mVwb89V640rZ%2Bjpl%2Bg80ROU3XWrXWkUZhF4lsLwzNFkUax4mkLvrIWoexlTxm23S%2FaSaCloW24gDWLgoXohv%2Bo1SpgaGWCpLNJwJSeE203v90B0qyQejo%2FwTOnMLA3jq1GwnCcedfSldz8ZCqy04JOt%2Fsv0Hhg3BkeAiZTKwJ4tJQ62bCAtZvyDQ58JJFVpSNpJLC8XSmdV4%2FCPvNrjbHw4Lrgh9wl0zciuoyJBbHD4QiKvUZ51ELlByjyhs%2B5MMN3FKsMN0BVnH9BpFirlYhM1KKFSjqWTR64vTkWBAndJWVMoeUqO1bKRIY%2BJV1wi%2BibT166RKRnloSmQ%2FVO1j5rqk%2BT1LdP5H7rGzCp4%2Be8BjqkAQlCG5q0JnFDN9JGmzQUGAcWFsFPbGHVHsdMBYWdkCpn7PGJOwE6BUFAnaetcvPex6FOjzk%2FSLkRM3GezfOlFh%2FRz%2FxPejXkZqRslX%2FAbsbEiSaiC4uvNOlAFW%2FDIBmfLOvhUmTJPIFjEySQQuYqn5SQsHg%2BRmpnC0ObMxhfmqJg9jBkr1s2fVQXVWrz0Tg77tXUaioFxjONcToqdVwnpzvf%2FUyC&X-Amz-Signature=7bcc873a4be164a00babc80d009f144a713c4f5c62f4dcfe2dcc93502856099f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OT2MTZ6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrSA3ZtsxAp3sKA4ZoDopFm%2BM3YGL8PnLTL%2BWQW9KVZQIhAOTiJREtyBiSZ%2BVTZgNV%2FRLPE4RImG1bfJJaw5%2B5ol%2B9KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9S7zUmPMyyR0OzSAq3AMjFagd7bBNRNz%2FwZHr9LV3AX1NwP%2FIL%2BlSmazXu0IHPbDIcAkfFDIAs3AjThS1imCQqYZ2zvZrwv%2Bag2298wuD1u7dlczAqlvg7IBDVFM%2BHn0qsskcfOJpg%2FnQo3Y9oXN9PI%2FoIU%2Fz7fuwmF0yPYLBE5q04UU%2FZPWCYFzMKooJ0mXXACmO9PhGAGF4ayGXpnZ9vohm%2Beh45jrLzI7OP%2BsLqn8hqNAkrGVGHQj2RyY0xQAtb1RVwOymGIRx8kRTPFSgI4OlhCHYnU00zGD60JBUT5mVwb89V640rZ%2Bjpl%2Bg80ROU3XWrXWkUZhF4lsLwzNFkUax4mkLvrIWoexlTxm23S%2FaSaCloW24gDWLgoXohv%2Bo1SpgaGWCpLNJwJSeE203v90B0qyQejo%2FwTOnMLA3jq1GwnCcedfSldz8ZCqy04JOt%2Fsv0Hhg3BkeAiZTKwJ4tJQ62bCAtZvyDQ58JJFVpSNpJLC8XSmdV4%2FCPvNrjbHw4Lrgh9wl0zciuoyJBbHD4QiKvUZ51ELlByjyhs%2B5MMN3FKsMN0BVnH9BpFirlYhM1KKFSjqWTR64vTkWBAndJWVMoeUqO1bKRIY%2BJV1wi%2BibT166RKRnloSmQ%2FVO1j5rqk%2BT1LdP5H7rGzCp4%2Be8BjqkAQlCG5q0JnFDN9JGmzQUGAcWFsFPbGHVHsdMBYWdkCpn7PGJOwE6BUFAnaetcvPex6FOjzk%2FSLkRM3GezfOlFh%2FRz%2FxPejXkZqRslX%2FAbsbEiSaiC4uvNOlAFW%2FDIBmfLOvhUmTJPIFjEySQQuYqn5SQsHg%2BRmpnC0ObMxhfmqJg9jBkr1s2fVQXVWrz0Tg77tXUaioFxjONcToqdVwnpzvf%2FUyC&X-Amz-Signature=380e090b2afb44e9232f68ac8cfa24c2f0a695902da58967af1265ae355c4a65&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OT2MTZ6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrSA3ZtsxAp3sKA4ZoDopFm%2BM3YGL8PnLTL%2BWQW9KVZQIhAOTiJREtyBiSZ%2BVTZgNV%2FRLPE4RImG1bfJJaw5%2B5ol%2B9KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9S7zUmPMyyR0OzSAq3AMjFagd7bBNRNz%2FwZHr9LV3AX1NwP%2FIL%2BlSmazXu0IHPbDIcAkfFDIAs3AjThS1imCQqYZ2zvZrwv%2Bag2298wuD1u7dlczAqlvg7IBDVFM%2BHn0qsskcfOJpg%2FnQo3Y9oXN9PI%2FoIU%2Fz7fuwmF0yPYLBE5q04UU%2FZPWCYFzMKooJ0mXXACmO9PhGAGF4ayGXpnZ9vohm%2Beh45jrLzI7OP%2BsLqn8hqNAkrGVGHQj2RyY0xQAtb1RVwOymGIRx8kRTPFSgI4OlhCHYnU00zGD60JBUT5mVwb89V640rZ%2Bjpl%2Bg80ROU3XWrXWkUZhF4lsLwzNFkUax4mkLvrIWoexlTxm23S%2FaSaCloW24gDWLgoXohv%2Bo1SpgaGWCpLNJwJSeE203v90B0qyQejo%2FwTOnMLA3jq1GwnCcedfSldz8ZCqy04JOt%2Fsv0Hhg3BkeAiZTKwJ4tJQ62bCAtZvyDQ58JJFVpSNpJLC8XSmdV4%2FCPvNrjbHw4Lrgh9wl0zciuoyJBbHD4QiKvUZ51ELlByjyhs%2B5MMN3FKsMN0BVnH9BpFirlYhM1KKFSjqWTR64vTkWBAndJWVMoeUqO1bKRIY%2BJV1wi%2BibT166RKRnloSmQ%2FVO1j5rqk%2BT1LdP5H7rGzCp4%2Be8BjqkAQlCG5q0JnFDN9JGmzQUGAcWFsFPbGHVHsdMBYWdkCpn7PGJOwE6BUFAnaetcvPex6FOjzk%2FSLkRM3GezfOlFh%2FRz%2FxPejXkZqRslX%2FAbsbEiSaiC4uvNOlAFW%2FDIBmfLOvhUmTJPIFjEySQQuYqn5SQsHg%2BRmpnC0ObMxhfmqJg9jBkr1s2fVQXVWrz0Tg77tXUaioFxjONcToqdVwnpzvf%2FUyC&X-Amz-Signature=77e03f5a2c48ce672c4b08433849956f88c6f2d839439355d5118e83f4f8da92&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUADZOGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDPbaZHMaVhiDGinRRKU4HbU2CzuDMI7WCaDOIlh6mvyAiEAm7TKDQkhCKFwujFw9oKOxppSMekSfBP11ZbGzsLAh6gqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAA7Z2XTwr0Zk8JmwCrcAzTZPqlWGqp7B0Ja3RQgP83rcRmNcmgjHpzhc0EoUnYYeyN8yUeMLM5sZVgd5UXqCVZV40UCjJuL2hudX%2FXw9NdZmQSkIoCA3kpb22gUKzaAk3XyY6MXiqo13ouQNwOHKRn3%2FUTRgqR8PCGBZDAgTsvPJ3IVlJXgqi0LJazXSEkhum8EnFf9eik2726944oAl9LKVdjCPVa9wa4AaANUTmZP0KlkyyDZuic9WC%2B1RAYuAeuTNJj0fl5lT%2FFVjrgBFBa5mWai%2BWMmHvCnGTbaVGXGenlfyHf29wFZZHt7v5LeKQgoVI9wPklkRK2eCxKQ9i6%2FzLwv8XyYIaj8ASuqkWRf8SBk9UBd0HezbCjKNI37%2F1EiyyETITJAMhaW6l6oqqbQWBexx6RxJAyJiTBd3ICnNiWdRmHRYzG3lIcb2AAv%2FtUHLwFTGNPBOrjYy79MuBWuxb%2Fsd%2BmTew1riiRJ4gA7v92vOPF%2BhGqnMN2T1jz0AOcMzyuH64GZWKztGwYc8kg0wiYy1wMMvqjRm2Yp8snVew5uomQTwxBcgfTDzd4cMcPZDEqMx5miXXZtAUZqGlRDmcC7Je5duh7BGaBKjiQ8F6OHAcbI8P3Urru06FowU3gpf6OWtQfaB0UOMO%2F%2B57wGOqUBl%2FuPlD85FObVfbcSMaRoO0Mlk8mK1Pkn5Nle%2BvxzCbxNw9gQm9P0fdQQ8aR8Dju72nvVWwZGVW0m4jDIJsoRVuszsn119M1wrd5c6Lyu5fbQMyDxvZhM%2F6C28%2FR5ZMS202e61dg2rJTs0025nkoCoqhe%2FYLtfcMWCdg2VI9E%2BLC796Dxa5SpWDwF7c2Q1hPaBcsQOiZq1SzEkOWADqQ7IJPlumaz&X-Amz-Signature=491005acd6ea6410013c51fa50adaff0fca7e1e91f2a1f89ca3548170bc00a76&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUADZOGL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDPbaZHMaVhiDGinRRKU4HbU2CzuDMI7WCaDOIlh6mvyAiEAm7TKDQkhCKFwujFw9oKOxppSMekSfBP11ZbGzsLAh6gqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAA7Z2XTwr0Zk8JmwCrcAzTZPqlWGqp7B0Ja3RQgP83rcRmNcmgjHpzhc0EoUnYYeyN8yUeMLM5sZVgd5UXqCVZV40UCjJuL2hudX%2FXw9NdZmQSkIoCA3kpb22gUKzaAk3XyY6MXiqo13ouQNwOHKRn3%2FUTRgqR8PCGBZDAgTsvPJ3IVlJXgqi0LJazXSEkhum8EnFf9eik2726944oAl9LKVdjCPVa9wa4AaANUTmZP0KlkyyDZuic9WC%2B1RAYuAeuTNJj0fl5lT%2FFVjrgBFBa5mWai%2BWMmHvCnGTbaVGXGenlfyHf29wFZZHt7v5LeKQgoVI9wPklkRK2eCxKQ9i6%2FzLwv8XyYIaj8ASuqkWRf8SBk9UBd0HezbCjKNI37%2F1EiyyETITJAMhaW6l6oqqbQWBexx6RxJAyJiTBd3ICnNiWdRmHRYzG3lIcb2AAv%2FtUHLwFTGNPBOrjYy79MuBWuxb%2Fsd%2BmTew1riiRJ4gA7v92vOPF%2BhGqnMN2T1jz0AOcMzyuH64GZWKztGwYc8kg0wiYy1wMMvqjRm2Yp8snVew5uomQTwxBcgfTDzd4cMcPZDEqMx5miXXZtAUZqGlRDmcC7Je5duh7BGaBKjiQ8F6OHAcbI8P3Urru06FowU3gpf6OWtQfaB0UOMO%2F%2B57wGOqUBl%2FuPlD85FObVfbcSMaRoO0Mlk8mK1Pkn5Nle%2BvxzCbxNw9gQm9P0fdQQ8aR8Dju72nvVWwZGVW0m4jDIJsoRVuszsn119M1wrd5c6Lyu5fbQMyDxvZhM%2F6C28%2FR5ZMS202e61dg2rJTs0025nkoCoqhe%2FYLtfcMWCdg2VI9E%2BLC796Dxa5SpWDwF7c2Q1hPaBcsQOiZq1SzEkOWADqQ7IJPlumaz&X-Amz-Signature=19b435b188a9d8ebf823675a88865875b075ef94783b58db0ca21a925bc09aae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OT2MTZ6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T101535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrSA3ZtsxAp3sKA4ZoDopFm%2BM3YGL8PnLTL%2BWQW9KVZQIhAOTiJREtyBiSZ%2BVTZgNV%2FRLPE4RImG1bfJJaw5%2B5ol%2B9KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9S7zUmPMyyR0OzSAq3AMjFagd7bBNRNz%2FwZHr9LV3AX1NwP%2FIL%2BlSmazXu0IHPbDIcAkfFDIAs3AjThS1imCQqYZ2zvZrwv%2Bag2298wuD1u7dlczAqlvg7IBDVFM%2BHn0qsskcfOJpg%2FnQo3Y9oXN9PI%2FoIU%2Fz7fuwmF0yPYLBE5q04UU%2FZPWCYFzMKooJ0mXXACmO9PhGAGF4ayGXpnZ9vohm%2Beh45jrLzI7OP%2BsLqn8hqNAkrGVGHQj2RyY0xQAtb1RVwOymGIRx8kRTPFSgI4OlhCHYnU00zGD60JBUT5mVwb89V640rZ%2Bjpl%2Bg80ROU3XWrXWkUZhF4lsLwzNFkUax4mkLvrIWoexlTxm23S%2FaSaCloW24gDWLgoXohv%2Bo1SpgaGWCpLNJwJSeE203v90B0qyQejo%2FwTOnMLA3jq1GwnCcedfSldz8ZCqy04JOt%2Fsv0Hhg3BkeAiZTKwJ4tJQ62bCAtZvyDQ58JJFVpSNpJLC8XSmdV4%2FCPvNrjbHw4Lrgh9wl0zciuoyJBbHD4QiKvUZ51ELlByjyhs%2B5MMN3FKsMN0BVnH9BpFirlYhM1KKFSjqWTR64vTkWBAndJWVMoeUqO1bKRIY%2BJV1wi%2BibT166RKRnloSmQ%2FVO1j5rqk%2BT1LdP5H7rGzCp4%2Be8BjqkAQlCG5q0JnFDN9JGmzQUGAcWFsFPbGHVHsdMBYWdkCpn7PGJOwE6BUFAnaetcvPex6FOjzk%2FSLkRM3GezfOlFh%2FRz%2FxPejXkZqRslX%2FAbsbEiSaiC4uvNOlAFW%2FDIBmfLOvhUmTJPIFjEySQQuYqn5SQsHg%2BRmpnC0ObMxhfmqJg9jBkr1s2fVQXVWrz0Tg77tXUaioFxjONcToqdVwnpzvf%2FUyC&X-Amz-Signature=668c2d40bc0817b328b62b506307363da08cdd3403929bf920d079118b78cde0&X-Amz-SignedHeaders=host&x-id=GetObject)
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