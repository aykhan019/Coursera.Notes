

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5L43BIM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8IVx1fifoDmGi%2BWpShMbGCAV%2FZGaN1RP221zj9MUjUwIhAOC%2FBHVdvSU80mn9I4Wt75LrSI1Z%2BqELxkgBIvCaKigqKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz2gViCEE1je1NlaUQq3AOZvYUiBmrRH6l8QK6s%2B3aLUuy8Z317ze0fL8y7Y2bt2DBiQK2ptg47fPEgGSkK5%2BWmKUYJtr2I1eU82Yf3q4L04rrB72hWXkrPGWS98Q37z4dJG%2FSWJY2o%2FBQXlFTgG4seYeMmNaCRL5CJWPiQjhBNP0T1rv0bqvPCqCtXqJfNr8wvAHXBHWiAfkCQAf8iqlUoQzXldTc2FUanNiS8iZTo5E5JF1QBHxv9BmXMFg9omIsb3U6s%2BROXgnCJOu0TMUcXWvm1TofxOXDz9C6aVAir3M%2FxQjasA%2FTMc8loUMu6KpVlBjsrtvyUdtT1cbDtVOW%2BB%2FPKYAVgtlwnHUAYhk3UoNxn5ymeazMtVSYPNgs01z3iEioHfuUYtNqmthaWkzDe1HzjQ10mtZfN3fPbC9yAVv%2F0MbhLyQ5sXTY%2Fg6jQyYGnrNoR6hOxuIz93WNOAwR%2Bg8qcnJiEjsp1sSnEIM%2BYxOjpQ%2FGfnHGTa84U6VaEnSYpnY0T903Y3oP8UXKJrbZz13rBUu33h3Hgw1EctJvY0pmu7GrLCvPULsc88RzXMLPfQKrUmmtCLJL3xKYrv%2FJb26Chfakos2lt1XUpPeCT6ifkKTMwFfY3XuqcVBq5SQKal3HwvhxM%2FC4r5zCoyPi8BjqkAaBDawaI%2FjAZi%2Fty05SXSteE9C0h%2FTQm4jdkzPMY56OrHImF2luXD82XBQhQhp%2BEk9BAmnsUuPqX6ooFTjyn8My8UAaO2c24GnFsGgGmLtR4tCu3utYaZrpXDWr5yuBo%2FNoGPn3S7Igdh2PN2t6%2BuPc3KDaJepdIsqFoyTnt%2F5hIvL1TKELaatIMlCp6mv4sS%2FqTbwub%2Fn2XqzOMN2m9GrUqOiqq&X-Amz-Signature=0b84cf80a4079df957f4e44eb6212179d13a383867bdaa07f685c4e3b7f9e6b5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5L43BIM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8IVx1fifoDmGi%2BWpShMbGCAV%2FZGaN1RP221zj9MUjUwIhAOC%2FBHVdvSU80mn9I4Wt75LrSI1Z%2BqELxkgBIvCaKigqKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz2gViCEE1je1NlaUQq3AOZvYUiBmrRH6l8QK6s%2B3aLUuy8Z317ze0fL8y7Y2bt2DBiQK2ptg47fPEgGSkK5%2BWmKUYJtr2I1eU82Yf3q4L04rrB72hWXkrPGWS98Q37z4dJG%2FSWJY2o%2FBQXlFTgG4seYeMmNaCRL5CJWPiQjhBNP0T1rv0bqvPCqCtXqJfNr8wvAHXBHWiAfkCQAf8iqlUoQzXldTc2FUanNiS8iZTo5E5JF1QBHxv9BmXMFg9omIsb3U6s%2BROXgnCJOu0TMUcXWvm1TofxOXDz9C6aVAir3M%2FxQjasA%2FTMc8loUMu6KpVlBjsrtvyUdtT1cbDtVOW%2BB%2FPKYAVgtlwnHUAYhk3UoNxn5ymeazMtVSYPNgs01z3iEioHfuUYtNqmthaWkzDe1HzjQ10mtZfN3fPbC9yAVv%2F0MbhLyQ5sXTY%2Fg6jQyYGnrNoR6hOxuIz93WNOAwR%2Bg8qcnJiEjsp1sSnEIM%2BYxOjpQ%2FGfnHGTa84U6VaEnSYpnY0T903Y3oP8UXKJrbZz13rBUu33h3Hgw1EctJvY0pmu7GrLCvPULsc88RzXMLPfQKrUmmtCLJL3xKYrv%2FJb26Chfakos2lt1XUpPeCT6ifkKTMwFfY3XuqcVBq5SQKal3HwvhxM%2FC4r5zCoyPi8BjqkAaBDawaI%2FjAZi%2Fty05SXSteE9C0h%2FTQm4jdkzPMY56OrHImF2luXD82XBQhQhp%2BEk9BAmnsUuPqX6ooFTjyn8My8UAaO2c24GnFsGgGmLtR4tCu3utYaZrpXDWr5yuBo%2FNoGPn3S7Igdh2PN2t6%2BuPc3KDaJepdIsqFoyTnt%2F5hIvL1TKELaatIMlCp6mv4sS%2FqTbwub%2Fn2XqzOMN2m9GrUqOiqq&X-Amz-Signature=0894f54ecf0452ecbffeebb6cf28de0ccdf6732b200c25ec6fbfa9a66c166869&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5L43BIM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8IVx1fifoDmGi%2BWpShMbGCAV%2FZGaN1RP221zj9MUjUwIhAOC%2FBHVdvSU80mn9I4Wt75LrSI1Z%2BqELxkgBIvCaKigqKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz2gViCEE1je1NlaUQq3AOZvYUiBmrRH6l8QK6s%2B3aLUuy8Z317ze0fL8y7Y2bt2DBiQK2ptg47fPEgGSkK5%2BWmKUYJtr2I1eU82Yf3q4L04rrB72hWXkrPGWS98Q37z4dJG%2FSWJY2o%2FBQXlFTgG4seYeMmNaCRL5CJWPiQjhBNP0T1rv0bqvPCqCtXqJfNr8wvAHXBHWiAfkCQAf8iqlUoQzXldTc2FUanNiS8iZTo5E5JF1QBHxv9BmXMFg9omIsb3U6s%2BROXgnCJOu0TMUcXWvm1TofxOXDz9C6aVAir3M%2FxQjasA%2FTMc8loUMu6KpVlBjsrtvyUdtT1cbDtVOW%2BB%2FPKYAVgtlwnHUAYhk3UoNxn5ymeazMtVSYPNgs01z3iEioHfuUYtNqmthaWkzDe1HzjQ10mtZfN3fPbC9yAVv%2F0MbhLyQ5sXTY%2Fg6jQyYGnrNoR6hOxuIz93WNOAwR%2Bg8qcnJiEjsp1sSnEIM%2BYxOjpQ%2FGfnHGTa84U6VaEnSYpnY0T903Y3oP8UXKJrbZz13rBUu33h3Hgw1EctJvY0pmu7GrLCvPULsc88RzXMLPfQKrUmmtCLJL3xKYrv%2FJb26Chfakos2lt1XUpPeCT6ifkKTMwFfY3XuqcVBq5SQKal3HwvhxM%2FC4r5zCoyPi8BjqkAaBDawaI%2FjAZi%2Fty05SXSteE9C0h%2FTQm4jdkzPMY56OrHImF2luXD82XBQhQhp%2BEk9BAmnsUuPqX6ooFTjyn8My8UAaO2c24GnFsGgGmLtR4tCu3utYaZrpXDWr5yuBo%2FNoGPn3S7Igdh2PN2t6%2BuPc3KDaJepdIsqFoyTnt%2F5hIvL1TKELaatIMlCp6mv4sS%2FqTbwub%2Fn2XqzOMN2m9GrUqOiqq&X-Amz-Signature=065a80806d523eaedd17a4a0b41897e794a814edf4e437053f7928bda62382d1&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IFKHDRV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjopzeb7ACHsIIIJsAds4zd3KRKEcmFAwWXHzoGSyFYAiEA61chvPRJ6vl5TjcNDos09d6bc5N0DkBgDKncll%2BNI4QqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKb1h9PhUBtoQR4kPircA64Eesd23w65NxFV7nziWtdRhQY9ybpEJJ4zfgdVQrEJMi0Nfn1Kucr%2BNgOJoCG4N%2FY5Q3VPxEWjc6NgEcdT%2FwPOpRtc%2ByiR5GSE82EeHiEsy0XMyEuKpajLwP13PvcmgUSzff6y%2FyKNh8ekE5QvtvKKdWjCs5Kz2Swd6QP0qJjFR9ETZ3alkP%2Fiy1Kl2DghhoK%2Fhc9UbdZyyG1lncLV8d%2FkaVHZ5LzM0lbNQgtxiTYWbeAMjCdF1uFcuhlEAw7cHlf9mxDyqpaBZ2CsHQJ2zjCTIpN1yBBKKI3TPkJ7ox7GPxl%2BBZ6GkHuG21WdubfUsXzcdN6dAaL0jJPGwsXxaMbs4LxRQHVe%2BayZPhcoclw7i3B8nugTTdF883ijTEJb%2BNm%2BmkMuzXsqbk6ABmAwH3H7aKb4ohWzf6GaqdNYEsGwbqTq9tF6Bk1d84RD6uVycBHneGrK6NxBIyIRBsGJGKHticp2u0Tyf2%2BqzHayL2dFTuM7XUXBmEn8ibSaAe%2FZwRBzir8EBaHL3LaRM3VwpNnPegYwwroc0GG1NvFxU4W3HDlbflUYQJ%2BhSmKwQnV86%2FaIhWDWdElqmSRBG4qECPD8ZVe%2FqKYuYPJ%2B0z8YtJR0wxrhvg04aczLQnWsMPfF%2BLwGOqUBex49UTwn2jAwk5r3YxrSY%2Ftb5BP4JxlgM%2BojdfwYhHJpXHWB4d1ShbCeiaErWs9vImmSodqUbOnqGGi3Is6F0%2FbAjzLfnBQXp94fio3Wlf2Q2nYUdXVUCWoUv4syU1iSoawTJhLZ2FUrorKxFIui890JxBk4Jum9Sf5fCvB7vyZ3deMiPjOyxSQTVIbHr8llAfauvO2ozgvDpUe4jQyxnSHyxOo0&X-Amz-Signature=8602e8d2aebff725ca8b63f5673f376c5c9b6bdfa70d95953cd248a27eac9e06&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IFKHDRV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFjopzeb7ACHsIIIJsAds4zd3KRKEcmFAwWXHzoGSyFYAiEA61chvPRJ6vl5TjcNDos09d6bc5N0DkBgDKncll%2BNI4QqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKb1h9PhUBtoQR4kPircA64Eesd23w65NxFV7nziWtdRhQY9ybpEJJ4zfgdVQrEJMi0Nfn1Kucr%2BNgOJoCG4N%2FY5Q3VPxEWjc6NgEcdT%2FwPOpRtc%2ByiR5GSE82EeHiEsy0XMyEuKpajLwP13PvcmgUSzff6y%2FyKNh8ekE5QvtvKKdWjCs5Kz2Swd6QP0qJjFR9ETZ3alkP%2Fiy1Kl2DghhoK%2Fhc9UbdZyyG1lncLV8d%2FkaVHZ5LzM0lbNQgtxiTYWbeAMjCdF1uFcuhlEAw7cHlf9mxDyqpaBZ2CsHQJ2zjCTIpN1yBBKKI3TPkJ7ox7GPxl%2BBZ6GkHuG21WdubfUsXzcdN6dAaL0jJPGwsXxaMbs4LxRQHVe%2BayZPhcoclw7i3B8nugTTdF883ijTEJb%2BNm%2BmkMuzXsqbk6ABmAwH3H7aKb4ohWzf6GaqdNYEsGwbqTq9tF6Bk1d84RD6uVycBHneGrK6NxBIyIRBsGJGKHticp2u0Tyf2%2BqzHayL2dFTuM7XUXBmEn8ibSaAe%2FZwRBzir8EBaHL3LaRM3VwpNnPegYwwroc0GG1NvFxU4W3HDlbflUYQJ%2BhSmKwQnV86%2FaIhWDWdElqmSRBG4qECPD8ZVe%2FqKYuYPJ%2B0z8YtJR0wxrhvg04aczLQnWsMPfF%2BLwGOqUBex49UTwn2jAwk5r3YxrSY%2Ftb5BP4JxlgM%2BojdfwYhHJpXHWB4d1ShbCeiaErWs9vImmSodqUbOnqGGi3Is6F0%2FbAjzLfnBQXp94fio3Wlf2Q2nYUdXVUCWoUv4syU1iSoawTJhLZ2FUrorKxFIui890JxBk4Jum9Sf5fCvB7vyZ3deMiPjOyxSQTVIbHr8llAfauvO2ozgvDpUe4jQyxnSHyxOo0&X-Amz-Signature=2f8f05e024ddb4a6e11f11b12f536930fa1282a7f7e4eb67c6af6d6e5642ba5d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5L43BIM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T191035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8IVx1fifoDmGi%2BWpShMbGCAV%2FZGaN1RP221zj9MUjUwIhAOC%2FBHVdvSU80mn9I4Wt75LrSI1Z%2BqELxkgBIvCaKigqKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz2gViCEE1je1NlaUQq3AOZvYUiBmrRH6l8QK6s%2B3aLUuy8Z317ze0fL8y7Y2bt2DBiQK2ptg47fPEgGSkK5%2BWmKUYJtr2I1eU82Yf3q4L04rrB72hWXkrPGWS98Q37z4dJG%2FSWJY2o%2FBQXlFTgG4seYeMmNaCRL5CJWPiQjhBNP0T1rv0bqvPCqCtXqJfNr8wvAHXBHWiAfkCQAf8iqlUoQzXldTc2FUanNiS8iZTo5E5JF1QBHxv9BmXMFg9omIsb3U6s%2BROXgnCJOu0TMUcXWvm1TofxOXDz9C6aVAir3M%2FxQjasA%2FTMc8loUMu6KpVlBjsrtvyUdtT1cbDtVOW%2BB%2FPKYAVgtlwnHUAYhk3UoNxn5ymeazMtVSYPNgs01z3iEioHfuUYtNqmthaWkzDe1HzjQ10mtZfN3fPbC9yAVv%2F0MbhLyQ5sXTY%2Fg6jQyYGnrNoR6hOxuIz93WNOAwR%2Bg8qcnJiEjsp1sSnEIM%2BYxOjpQ%2FGfnHGTa84U6VaEnSYpnY0T903Y3oP8UXKJrbZz13rBUu33h3Hgw1EctJvY0pmu7GrLCvPULsc88RzXMLPfQKrUmmtCLJL3xKYrv%2FJb26Chfakos2lt1XUpPeCT6ifkKTMwFfY3XuqcVBq5SQKal3HwvhxM%2FC4r5zCoyPi8BjqkAaBDawaI%2FjAZi%2Fty05SXSteE9C0h%2FTQm4jdkzPMY56OrHImF2luXD82XBQhQhp%2BEk9BAmnsUuPqX6ooFTjyn8My8UAaO2c24GnFsGgGmLtR4tCu3utYaZrpXDWr5yuBo%2FNoGPn3S7Igdh2PN2t6%2BuPc3KDaJepdIsqFoyTnt%2F5hIvL1TKELaatIMlCp6mv4sS%2FqTbwub%2Fn2XqzOMN2m9GrUqOiqq&X-Amz-Signature=4103462b504d88ca0ab73dd330702aaf03a1c3aced5ead99b5cff0377e3eb2d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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