

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673KVPE5W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA4FyNBtc8%2F7lq%2FdzeY6P1hlG2jmMgTq8xqutcJrEDUoAiBwEcqxeWsAnNmJCjUodDEgrw2QlbZx9fXlt7b1fdkCLSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBqVT0KZrlHVZFLdUKtwD2nkw1M%2FabKN6uRoi%2FsFIj4Gy19uIesnPxyJfuQoIXvP3f00KhshC0J6Z%2BD7AW2PsUM%2BqngPfgXh6U3yrOdnKrAjUHUiLjc1D7PUrl8Pz6uicGPhmiBki2tRnwR5Z6dWKbW2quGYW%2F3lXGmU8KQgho3IJwH1goMbcQPinWwf15vegeykaRKCLFTCMFsxGq3oOa%2BkOi4iGs%2FD7NJUODt%2FMwkJVYP5Qw9jjHgTOih6FUViSqhw%2BkDetDgb6FKqJ3%2BXi6mGCRVsu8l84matesNB%2FXdLQFv3zDYlbNq%2FzLhBOq5MacjimXkTCQ9%2BHIIYEta3SIqCectcdxohtSxufsmZtJHljkk6W2JIGKmI6BxrzNHZVYClL%2FvP%2B2nN7bhrjrOdZuCnaDZE9Od5KZFg31vP%2BEQ59rROklNKOiRlQnFwVZhoy6rxwBp%2F8JAjOUDRzXnlvhTeieRDKN3WbvHWiDWRW%2FpPNDQeqnP0D0IdAbTd2Zwdaq3lgsWsEhXIbDRjVhFnfHko3FJydwmRZIFA%2B2NHE5FHG%2F2qrQ%2BiwYyXq927qMW9XQdNDsXOOFPu9iiNS5kwvel6lbcJ%2Ffd6nn%2BIkJSzq3ngkBWSt3xFseRjuBkR3sawcSnfb01Hu2HrDhc0wvdDwvAY6pgEhgEiwJWW1VdrYE0WzmjygjWW0ED4%2FKuPaVwFkOdwMR2CxPJq2%2BnYb4851Zltp8ZSHZgGT2xzZ84nciTfx7HUZVt3tiSvFKKngPiZXdv8JO6IlP5nFJg76i1lBEePZHr%2FHP0%2B9frq8Um23uTNzf31k2PcZD%2B585n7FIf6NOd9BdQXtjj2AyOruNZtJzHU%2FfzT5QVLOb%2BV%2FJPJ9NdTEb5U7GgEBX%2FmF&X-Amz-Signature=663f761d693ebe0dae7ca351cfbce17c7d9cd632464ed8c71e2f6ac43beba3a3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673KVPE5W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA4FyNBtc8%2F7lq%2FdzeY6P1hlG2jmMgTq8xqutcJrEDUoAiBwEcqxeWsAnNmJCjUodDEgrw2QlbZx9fXlt7b1fdkCLSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBqVT0KZrlHVZFLdUKtwD2nkw1M%2FabKN6uRoi%2FsFIj4Gy19uIesnPxyJfuQoIXvP3f00KhshC0J6Z%2BD7AW2PsUM%2BqngPfgXh6U3yrOdnKrAjUHUiLjc1D7PUrl8Pz6uicGPhmiBki2tRnwR5Z6dWKbW2quGYW%2F3lXGmU8KQgho3IJwH1goMbcQPinWwf15vegeykaRKCLFTCMFsxGq3oOa%2BkOi4iGs%2FD7NJUODt%2FMwkJVYP5Qw9jjHgTOih6FUViSqhw%2BkDetDgb6FKqJ3%2BXi6mGCRVsu8l84matesNB%2FXdLQFv3zDYlbNq%2FzLhBOq5MacjimXkTCQ9%2BHIIYEta3SIqCectcdxohtSxufsmZtJHljkk6W2JIGKmI6BxrzNHZVYClL%2FvP%2B2nN7bhrjrOdZuCnaDZE9Od5KZFg31vP%2BEQ59rROklNKOiRlQnFwVZhoy6rxwBp%2F8JAjOUDRzXnlvhTeieRDKN3WbvHWiDWRW%2FpPNDQeqnP0D0IdAbTd2Zwdaq3lgsWsEhXIbDRjVhFnfHko3FJydwmRZIFA%2B2NHE5FHG%2F2qrQ%2BiwYyXq927qMW9XQdNDsXOOFPu9iiNS5kwvel6lbcJ%2Ffd6nn%2BIkJSzq3ngkBWSt3xFseRjuBkR3sawcSnfb01Hu2HrDhc0wvdDwvAY6pgEhgEiwJWW1VdrYE0WzmjygjWW0ED4%2FKuPaVwFkOdwMR2CxPJq2%2BnYb4851Zltp8ZSHZgGT2xzZ84nciTfx7HUZVt3tiSvFKKngPiZXdv8JO6IlP5nFJg76i1lBEePZHr%2FHP0%2B9frq8Um23uTNzf31k2PcZD%2B585n7FIf6NOd9BdQXtjj2AyOruNZtJzHU%2FfzT5QVLOb%2BV%2FJPJ9NdTEb5U7GgEBX%2FmF&X-Amz-Signature=fae0adcd4aeede26796cef2ef57cf13c0bb2c425470fd8a09ff451b499787a9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673KVPE5W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA4FyNBtc8%2F7lq%2FdzeY6P1hlG2jmMgTq8xqutcJrEDUoAiBwEcqxeWsAnNmJCjUodDEgrw2QlbZx9fXlt7b1fdkCLSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBqVT0KZrlHVZFLdUKtwD2nkw1M%2FabKN6uRoi%2FsFIj4Gy19uIesnPxyJfuQoIXvP3f00KhshC0J6Z%2BD7AW2PsUM%2BqngPfgXh6U3yrOdnKrAjUHUiLjc1D7PUrl8Pz6uicGPhmiBki2tRnwR5Z6dWKbW2quGYW%2F3lXGmU8KQgho3IJwH1goMbcQPinWwf15vegeykaRKCLFTCMFsxGq3oOa%2BkOi4iGs%2FD7NJUODt%2FMwkJVYP5Qw9jjHgTOih6FUViSqhw%2BkDetDgb6FKqJ3%2BXi6mGCRVsu8l84matesNB%2FXdLQFv3zDYlbNq%2FzLhBOq5MacjimXkTCQ9%2BHIIYEta3SIqCectcdxohtSxufsmZtJHljkk6W2JIGKmI6BxrzNHZVYClL%2FvP%2B2nN7bhrjrOdZuCnaDZE9Od5KZFg31vP%2BEQ59rROklNKOiRlQnFwVZhoy6rxwBp%2F8JAjOUDRzXnlvhTeieRDKN3WbvHWiDWRW%2FpPNDQeqnP0D0IdAbTd2Zwdaq3lgsWsEhXIbDRjVhFnfHko3FJydwmRZIFA%2B2NHE5FHG%2F2qrQ%2BiwYyXq927qMW9XQdNDsXOOFPu9iiNS5kwvel6lbcJ%2Ffd6nn%2BIkJSzq3ngkBWSt3xFseRjuBkR3sawcSnfb01Hu2HrDhc0wvdDwvAY6pgEhgEiwJWW1VdrYE0WzmjygjWW0ED4%2FKuPaVwFkOdwMR2CxPJq2%2BnYb4851Zltp8ZSHZgGT2xzZ84nciTfx7HUZVt3tiSvFKKngPiZXdv8JO6IlP5nFJg76i1lBEePZHr%2FHP0%2B9frq8Um23uTNzf31k2PcZD%2B585n7FIf6NOd9BdQXtjj2AyOruNZtJzHU%2FfzT5QVLOb%2BV%2FJPJ9NdTEb5U7GgEBX%2FmF&X-Amz-Signature=4b932d954617a17d6a2fb4dbe9b4c1c7d41a730bfb15606ebe2c113f8084559d&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPTGK4JP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV2MW6F03jigm02I4PDRcf%2Fjg2xgrfoT%2FUg3GVF4eKYAiEAkGFGRxuACyBWEZKS41IzNJ1gtRiQ4O2aHo14yQO5JxYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKdki9gY%2BtTymGlqECrcA3J3vuE7SVH7clFk%2FLs5C6DbNXa4szb5VOkYn2MNxn35yCEzId5ZPGqUzXwV6rTyq6B9gtckEtqlfx1b%2BDe3ytupJ1FmA%2FkZN3NxQdalVTtRQ2cKEe0bCktiyDAnzv5AItE6npRUY4ZUeiGPQEsvq995fPm8zuojzd4xx1%2Bk35cBGL5%2BgY14rociCotMQTKa3iSKLePWtI75oKQ3bDANcsbEssDhyBN38ts%2F1sQgZvqT%2Bun0IFaQvfAQ5VLr7X1AuQmke8itTxa%2FbxzY2M%2Fjiv7XLCodTGp4af67wWCNHq5FAjLWdQLYpYDTBTgOUhau1%2Fnnq9fVHW0sYfDvTTS93xl3lawwzbPJUqtKhRGKbhQK4U1s%2BSiFeVXTsNshUqfLEqIPioH0ndqkWVgqq%2B2nVhn1q4zqRd7Dh8%2Bbk9pDHA8OMjh644J%2Fk4qaaqrYmDZgF3mImNRSQQDo9i%2Fo1IGDLZO7LqYCqYhp1QmWupnOZuJndJROHDQgy0AxTUBUmdjIMBeBF74JttNsN7%2FByT9jJ6UXvp3Z%2FWOUEYDFpa5um%2BD3yCwLsBjsAjTD648TyYfCTPj0PrTfJ1r9tr0C7GLSHCbKL31d7OsgMbaOGzNc%2FHX%2BziduGP6yFgyL4nwSMLLQ8LwGOqUBIhT0gYxAcKLeBCOPncWG6e08HVrF1GcZFrAJ3FK4XbAMELdhz1MTtJCfQHwrITPJk3U3jHqDIUovIM4d5avsmMOyiIqpdO80YZXHS3SdBczu1WES%2Fz%2Bpm67SkHUG6xW8ET6PiWUeUdyXoOhc7yJlgiJuQd%2BdwZN9jfpBsoNJSpqc3dGhamJyzq%2FqGvtpxeYpN9PFCngbftgtpaWhbAo3TMZ30%2BQB&X-Amz-Signature=01f2d83f8114901b2bf52ed0e401265d17cea2dba8f28618e09f7c8ec3c8430f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPTGK4JP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV2MW6F03jigm02I4PDRcf%2Fjg2xgrfoT%2FUg3GVF4eKYAiEAkGFGRxuACyBWEZKS41IzNJ1gtRiQ4O2aHo14yQO5JxYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKdki9gY%2BtTymGlqECrcA3J3vuE7SVH7clFk%2FLs5C6DbNXa4szb5VOkYn2MNxn35yCEzId5ZPGqUzXwV6rTyq6B9gtckEtqlfx1b%2BDe3ytupJ1FmA%2FkZN3NxQdalVTtRQ2cKEe0bCktiyDAnzv5AItE6npRUY4ZUeiGPQEsvq995fPm8zuojzd4xx1%2Bk35cBGL5%2BgY14rociCotMQTKa3iSKLePWtI75oKQ3bDANcsbEssDhyBN38ts%2F1sQgZvqT%2Bun0IFaQvfAQ5VLr7X1AuQmke8itTxa%2FbxzY2M%2Fjiv7XLCodTGp4af67wWCNHq5FAjLWdQLYpYDTBTgOUhau1%2Fnnq9fVHW0sYfDvTTS93xl3lawwzbPJUqtKhRGKbhQK4U1s%2BSiFeVXTsNshUqfLEqIPioH0ndqkWVgqq%2B2nVhn1q4zqRd7Dh8%2Bbk9pDHA8OMjh644J%2Fk4qaaqrYmDZgF3mImNRSQQDo9i%2Fo1IGDLZO7LqYCqYhp1QmWupnOZuJndJROHDQgy0AxTUBUmdjIMBeBF74JttNsN7%2FByT9jJ6UXvp3Z%2FWOUEYDFpa5um%2BD3yCwLsBjsAjTD648TyYfCTPj0PrTfJ1r9tr0C7GLSHCbKL31d7OsgMbaOGzNc%2FHX%2BziduGP6yFgyL4nwSMLLQ8LwGOqUBIhT0gYxAcKLeBCOPncWG6e08HVrF1GcZFrAJ3FK4XbAMELdhz1MTtJCfQHwrITPJk3U3jHqDIUovIM4d5avsmMOyiIqpdO80YZXHS3SdBczu1WES%2Fz%2Bpm67SkHUG6xW8ET6PiWUeUdyXoOhc7yJlgiJuQd%2BdwZN9jfpBsoNJSpqc3dGhamJyzq%2FqGvtpxeYpN9PFCngbftgtpaWhbAo3TMZ30%2BQB&X-Amz-Signature=96ac40689d57676954c6f5e565711d5118e0e879aec9a501a70f628a6e53976c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673KVPE5W%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA4FyNBtc8%2F7lq%2FdzeY6P1hlG2jmMgTq8xqutcJrEDUoAiBwEcqxeWsAnNmJCjUodDEgrw2QlbZx9fXlt7b1fdkCLSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBqVT0KZrlHVZFLdUKtwD2nkw1M%2FabKN6uRoi%2FsFIj4Gy19uIesnPxyJfuQoIXvP3f00KhshC0J6Z%2BD7AW2PsUM%2BqngPfgXh6U3yrOdnKrAjUHUiLjc1D7PUrl8Pz6uicGPhmiBki2tRnwR5Z6dWKbW2quGYW%2F3lXGmU8KQgho3IJwH1goMbcQPinWwf15vegeykaRKCLFTCMFsxGq3oOa%2BkOi4iGs%2FD7NJUODt%2FMwkJVYP5Qw9jjHgTOih6FUViSqhw%2BkDetDgb6FKqJ3%2BXi6mGCRVsu8l84matesNB%2FXdLQFv3zDYlbNq%2FzLhBOq5MacjimXkTCQ9%2BHIIYEta3SIqCectcdxohtSxufsmZtJHljkk6W2JIGKmI6BxrzNHZVYClL%2FvP%2B2nN7bhrjrOdZuCnaDZE9Od5KZFg31vP%2BEQ59rROklNKOiRlQnFwVZhoy6rxwBp%2F8JAjOUDRzXnlvhTeieRDKN3WbvHWiDWRW%2FpPNDQeqnP0D0IdAbTd2Zwdaq3lgsWsEhXIbDRjVhFnfHko3FJydwmRZIFA%2B2NHE5FHG%2F2qrQ%2BiwYyXq927qMW9XQdNDsXOOFPu9iiNS5kwvel6lbcJ%2Ffd6nn%2BIkJSzq3ngkBWSt3xFseRjuBkR3sawcSnfb01Hu2HrDhc0wvdDwvAY6pgEhgEiwJWW1VdrYE0WzmjygjWW0ED4%2FKuPaVwFkOdwMR2CxPJq2%2BnYb4851Zltp8ZSHZgGT2xzZ84nciTfx7HUZVt3tiSvFKKngPiZXdv8JO6IlP5nFJg76i1lBEePZHr%2FHP0%2B9frq8Um23uTNzf31k2PcZD%2B585n7FIf6NOd9BdQXtjj2AyOruNZtJzHU%2FfzT5QVLOb%2BV%2FJPJ9NdTEb5U7GgEBX%2FmF&X-Amz-Signature=bc568a3cfcd2aa1da86e98743581b5657dfb0799047b1bc3c2d09b9b067304e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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