

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIYR42MK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGL7Xig8lQowhPVeWjxi5qywWqKw7V%2F8sGjNh0PB2H5AiEAsopHW0pSM57n1BfxqwOD6WEhLN1F7u3ve7%2FjkmxKYQYqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsPw1DWS35sGa%2F1GyrcA%2F8b3yvKXIdzDP2ilTRO2EfmRUeHEM3Kf0iyJZ5MkOPfTbaeRTM7zwe0L%2FObnhyha3mzqq9uVSwPJBQLPTxm%2BZEO8avwvfPPmjz0QDK%2FhH0yUEbRC%2B9eDSO%2FgI7hocjKK2CS9CFMZBUbOq5mIPxmEzWL1%2FKGlinpFdSNLGho%2B3ysSLeLwMAsDQM%2FU2kyweD2NYWIIV9qD1meqnk2Nbk09932WuERPWkYz0SuRFQSuOJ6csms%2B1bBsqqv31Ep6AR%2FtxnTdc%2FkFk1UQjjM8eCvxbbkQq3CRgxJUd3hlANyQmOfTZt2IlzA3V52ziOFAAMwJcYmSvjV8JppIHo8XEn%2FwaO6BEN4twrJIKLu%2F5LKbfkRToQZMQE8AR%2FxcNSklgStMSjFArfabSWMRLhpiGA2MeSRPTA6E55Jdc%2FhSYzivXCUrozbgRzeC7c2mgYMeFgi6L08tidKtWrYSoxF%2BxrNFN2fSnrMkEbjGRzqW4OwovDyKoTgyLMf0zx38Q%2BRFt%2FZMjPcC%2FUh0HgDJiTthQI2A1eM%2BaNMlUEfutkt4Og8rV43gtDo%2FxlFpPPfSnYomKfLdVkiinDuI2LJsSI7hVMzQpnokvkj2LbWjGmpErwXlusLdJPuuu%2FSzOd1g%2FolMPmn7bwGOqUBjGzVybCMjbHCz8%2FXn1jgqJPM120N8ERlrADrSX5nlP%2F8RMOITyaZ96Up8W0vhE%2BXcoH0nW3uTk3Pd4zDtdHBHvFrfn%2F%2FCeehyda2wqjmcHLOm0D5sWykE4tDzm18nwaLxlZVoyp%2Bc2hDYyoI4OsmUQgYk%2BqgYUfUiOCy9PC5ZTDJR6NRMnzHMOkRT65t8FzWOTrXRDF%2FnuXTvbjp0clKgvvzajU5&X-Amz-Signature=4ca007e65cabc28c08453c96578474b681bb56f3d7281195623b245abc4e8462&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIYR42MK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGL7Xig8lQowhPVeWjxi5qywWqKw7V%2F8sGjNh0PB2H5AiEAsopHW0pSM57n1BfxqwOD6WEhLN1F7u3ve7%2FjkmxKYQYqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsPw1DWS35sGa%2F1GyrcA%2F8b3yvKXIdzDP2ilTRO2EfmRUeHEM3Kf0iyJZ5MkOPfTbaeRTM7zwe0L%2FObnhyha3mzqq9uVSwPJBQLPTxm%2BZEO8avwvfPPmjz0QDK%2FhH0yUEbRC%2B9eDSO%2FgI7hocjKK2CS9CFMZBUbOq5mIPxmEzWL1%2FKGlinpFdSNLGho%2B3ysSLeLwMAsDQM%2FU2kyweD2NYWIIV9qD1meqnk2Nbk09932WuERPWkYz0SuRFQSuOJ6csms%2B1bBsqqv31Ep6AR%2FtxnTdc%2FkFk1UQjjM8eCvxbbkQq3CRgxJUd3hlANyQmOfTZt2IlzA3V52ziOFAAMwJcYmSvjV8JppIHo8XEn%2FwaO6BEN4twrJIKLu%2F5LKbfkRToQZMQE8AR%2FxcNSklgStMSjFArfabSWMRLhpiGA2MeSRPTA6E55Jdc%2FhSYzivXCUrozbgRzeC7c2mgYMeFgi6L08tidKtWrYSoxF%2BxrNFN2fSnrMkEbjGRzqW4OwovDyKoTgyLMf0zx38Q%2BRFt%2FZMjPcC%2FUh0HgDJiTthQI2A1eM%2BaNMlUEfutkt4Og8rV43gtDo%2FxlFpPPfSnYomKfLdVkiinDuI2LJsSI7hVMzQpnokvkj2LbWjGmpErwXlusLdJPuuu%2FSzOd1g%2FolMPmn7bwGOqUBjGzVybCMjbHCz8%2FXn1jgqJPM120N8ERlrADrSX5nlP%2F8RMOITyaZ96Up8W0vhE%2BXcoH0nW3uTk3Pd4zDtdHBHvFrfn%2F%2FCeehyda2wqjmcHLOm0D5sWykE4tDzm18nwaLxlZVoyp%2Bc2hDYyoI4OsmUQgYk%2BqgYUfUiOCy9PC5ZTDJR6NRMnzHMOkRT65t8FzWOTrXRDF%2FnuXTvbjp0clKgvvzajU5&X-Amz-Signature=0df40290f68e5ca167f5102ab7d273f4692b378895b6526b16b542850dd6c2b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIYR42MK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGL7Xig8lQowhPVeWjxi5qywWqKw7V%2F8sGjNh0PB2H5AiEAsopHW0pSM57n1BfxqwOD6WEhLN1F7u3ve7%2FjkmxKYQYqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsPw1DWS35sGa%2F1GyrcA%2F8b3yvKXIdzDP2ilTRO2EfmRUeHEM3Kf0iyJZ5MkOPfTbaeRTM7zwe0L%2FObnhyha3mzqq9uVSwPJBQLPTxm%2BZEO8avwvfPPmjz0QDK%2FhH0yUEbRC%2B9eDSO%2FgI7hocjKK2CS9CFMZBUbOq5mIPxmEzWL1%2FKGlinpFdSNLGho%2B3ysSLeLwMAsDQM%2FU2kyweD2NYWIIV9qD1meqnk2Nbk09932WuERPWkYz0SuRFQSuOJ6csms%2B1bBsqqv31Ep6AR%2FtxnTdc%2FkFk1UQjjM8eCvxbbkQq3CRgxJUd3hlANyQmOfTZt2IlzA3V52ziOFAAMwJcYmSvjV8JppIHo8XEn%2FwaO6BEN4twrJIKLu%2F5LKbfkRToQZMQE8AR%2FxcNSklgStMSjFArfabSWMRLhpiGA2MeSRPTA6E55Jdc%2FhSYzivXCUrozbgRzeC7c2mgYMeFgi6L08tidKtWrYSoxF%2BxrNFN2fSnrMkEbjGRzqW4OwovDyKoTgyLMf0zx38Q%2BRFt%2FZMjPcC%2FUh0HgDJiTthQI2A1eM%2BaNMlUEfutkt4Og8rV43gtDo%2FxlFpPPfSnYomKfLdVkiinDuI2LJsSI7hVMzQpnokvkj2LbWjGmpErwXlusLdJPuuu%2FSzOd1g%2FolMPmn7bwGOqUBjGzVybCMjbHCz8%2FXn1jgqJPM120N8ERlrADrSX5nlP%2F8RMOITyaZ96Up8W0vhE%2BXcoH0nW3uTk3Pd4zDtdHBHvFrfn%2F%2FCeehyda2wqjmcHLOm0D5sWykE4tDzm18nwaLxlZVoyp%2Bc2hDYyoI4OsmUQgYk%2BqgYUfUiOCy9PC5ZTDJR6NRMnzHMOkRT65t8FzWOTrXRDF%2FnuXTvbjp0clKgvvzajU5&X-Amz-Signature=e4d4255b6eea3d20b1f28e4225d7d5eaa223038e133115405b87dd4c92eb7bc7&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHGGNDJB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHb5ghO4yq83mWLN%2BGGh3lboDHl07IPzGJ2QMepXzbNvAiEA5JPsg97A40LA6i%2BPZQC3SvJOYc0mXsqsNXXkyCi2eC0qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPyYxF%2FhT9qmwGAfRCrcAzZngTqXAe4EVr69VxmMhP8pc%2B7cz8t%2B7IR53aA5WXUude%2B79s%2F8MTu6ClUUq1sEath4PblaJVND1HXzy2qM0JAIIeJQwafsgaI%2F9r1blUyuvrwZoPjmOVQ74VPcafD8CVYJ7qbH2ruFpQXdB%2Ful6SK7kdseJrhdXG2zVTW0xauH6FbFz%2BVC3uaaB1PF9H7nztQaFKItlK%2Fk9GMre0PNkwzn9CX4U1EA3Ljsng8SXGouTn1U6t%2FUA6KtdU0UvQtui02PAJsOFMvCEIa9DZXBaHpbxxoHQXPkg5TgFlv5nfgXJ8Jea70L5IbQRzj%2FNoT6moDxuUx6%2Fh0Ggt8Ya4%2FBYoInE0%2FjWgAfB%2FgTWJQ6VlX%2B74l18sP1eSDAqKZHvDh4%2Bturlus56OtP0NFiZex7nb41g%2FYsUBUn5Qy2wGYN6mD5feEZDCxByZD9E7k%2FfhxCR%2FJGHirgkQNUXUpy3NuNnzB5vo3ZvyIQI75czwkh63b2oH3WCrtfQQDOC6F%2B25mo0EQ1gz0wBGdynFeb1l25e9UWdUkgJkpxkUtNGnmwFSmjnT68p%2FQLrByVhfqSybxBxyZpWB3TRmA6%2BcsVNfY6E1Am5mPTqsasCuNq8Tdt82oZHp9TIHYghLLJMZO4MKqo7bwGOqUBE00%2F9ub2rs7EZQr2PwPsPx%2FmUTPOnwl7ks7okcZvDlbNVebHUdYIt3o8A1ebNeygNXfA8Uoqzwe0higU95RH7PJuAOKCtN5z9i5xkHu4IPCWDSbVQymXdrn97nT1qjKyMlJbX3Eh1zJ5mpQw3SRvJALl17cEpdbfOTkiCnSI5%2FVX6PCyYTmBC51nzXSL0RMJXrcBMQTO29a6rEU4s%2FJSHBGiiVAb&X-Amz-Signature=69f627d2850f1751437cf32f3c19a476fb65bdd571d09aa5507ed8ed523b2859&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHGGNDJB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHb5ghO4yq83mWLN%2BGGh3lboDHl07IPzGJ2QMepXzbNvAiEA5JPsg97A40LA6i%2BPZQC3SvJOYc0mXsqsNXXkyCi2eC0qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPyYxF%2FhT9qmwGAfRCrcAzZngTqXAe4EVr69VxmMhP8pc%2B7cz8t%2B7IR53aA5WXUude%2B79s%2F8MTu6ClUUq1sEath4PblaJVND1HXzy2qM0JAIIeJQwafsgaI%2F9r1blUyuvrwZoPjmOVQ74VPcafD8CVYJ7qbH2ruFpQXdB%2Ful6SK7kdseJrhdXG2zVTW0xauH6FbFz%2BVC3uaaB1PF9H7nztQaFKItlK%2Fk9GMre0PNkwzn9CX4U1EA3Ljsng8SXGouTn1U6t%2FUA6KtdU0UvQtui02PAJsOFMvCEIa9DZXBaHpbxxoHQXPkg5TgFlv5nfgXJ8Jea70L5IbQRzj%2FNoT6moDxuUx6%2Fh0Ggt8Ya4%2FBYoInE0%2FjWgAfB%2FgTWJQ6VlX%2B74l18sP1eSDAqKZHvDh4%2Bturlus56OtP0NFiZex7nb41g%2FYsUBUn5Qy2wGYN6mD5feEZDCxByZD9E7k%2FfhxCR%2FJGHirgkQNUXUpy3NuNnzB5vo3ZvyIQI75czwkh63b2oH3WCrtfQQDOC6F%2B25mo0EQ1gz0wBGdynFeb1l25e9UWdUkgJkpxkUtNGnmwFSmjnT68p%2FQLrByVhfqSybxBxyZpWB3TRmA6%2BcsVNfY6E1Am5mPTqsasCuNq8Tdt82oZHp9TIHYghLLJMZO4MKqo7bwGOqUBE00%2F9ub2rs7EZQr2PwPsPx%2FmUTPOnwl7ks7okcZvDlbNVebHUdYIt3o8A1ebNeygNXfA8Uoqzwe0higU95RH7PJuAOKCtN5z9i5xkHu4IPCWDSbVQymXdrn97nT1qjKyMlJbX3Eh1zJ5mpQw3SRvJALl17cEpdbfOTkiCnSI5%2FVX6PCyYTmBC51nzXSL0RMJXrcBMQTO29a6rEU4s%2FJSHBGiiVAb&X-Amz-Signature=841cc720151d2e63d84e76f44cc17171f73fa5e738cd62a01d56ad270cf0d04f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIYR42MK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGL7Xig8lQowhPVeWjxi5qywWqKw7V%2F8sGjNh0PB2H5AiEAsopHW0pSM57n1BfxqwOD6WEhLN1F7u3ve7%2FjkmxKYQYqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsPw1DWS35sGa%2F1GyrcA%2F8b3yvKXIdzDP2ilTRO2EfmRUeHEM3Kf0iyJZ5MkOPfTbaeRTM7zwe0L%2FObnhyha3mzqq9uVSwPJBQLPTxm%2BZEO8avwvfPPmjz0QDK%2FhH0yUEbRC%2B9eDSO%2FgI7hocjKK2CS9CFMZBUbOq5mIPxmEzWL1%2FKGlinpFdSNLGho%2B3ysSLeLwMAsDQM%2FU2kyweD2NYWIIV9qD1meqnk2Nbk09932WuERPWkYz0SuRFQSuOJ6csms%2B1bBsqqv31Ep6AR%2FtxnTdc%2FkFk1UQjjM8eCvxbbkQq3CRgxJUd3hlANyQmOfTZt2IlzA3V52ziOFAAMwJcYmSvjV8JppIHo8XEn%2FwaO6BEN4twrJIKLu%2F5LKbfkRToQZMQE8AR%2FxcNSklgStMSjFArfabSWMRLhpiGA2MeSRPTA6E55Jdc%2FhSYzivXCUrozbgRzeC7c2mgYMeFgi6L08tidKtWrYSoxF%2BxrNFN2fSnrMkEbjGRzqW4OwovDyKoTgyLMf0zx38Q%2BRFt%2FZMjPcC%2FUh0HgDJiTthQI2A1eM%2BaNMlUEfutkt4Og8rV43gtDo%2FxlFpPPfSnYomKfLdVkiinDuI2LJsSI7hVMzQpnokvkj2LbWjGmpErwXlusLdJPuuu%2FSzOd1g%2FolMPmn7bwGOqUBjGzVybCMjbHCz8%2FXn1jgqJPM120N8ERlrADrSX5nlP%2F8RMOITyaZ96Up8W0vhE%2BXcoH0nW3uTk3Pd4zDtdHBHvFrfn%2F%2FCeehyda2wqjmcHLOm0D5sWykE4tDzm18nwaLxlZVoyp%2Bc2hDYyoI4OsmUQgYk%2BqgYUfUiOCy9PC5ZTDJR6NRMnzHMOkRT65t8FzWOTrXRDF%2FnuXTvbjp0clKgvvzajU5&X-Amz-Signature=51da7c362b1c3bf30f562f3b8a232f847689f60cd2590b63a888508d67b0878f&X-Amz-SignedHeaders=host&x-id=GetObject)
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