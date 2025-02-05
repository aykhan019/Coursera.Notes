

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S52Q2HCR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCWbAsjtB%2F%2BB%2Bi0Eq%2F3ia9R2JlgLLi8DIdwciWPr%2Faw9wIhAPYfJS8BOB7CqOqq8Rox25m%2F2hZCsvV5LYoxd6gXU9CjKv8DCEQQABoMNjM3NDIzMTgzODA1IgzO1bKYTkzmJ2bq8xEq3ANc7B7dUzAZxa%2BS%2FGnQtTt7OIEZ5Uuy0Df%2BbZ%2F3i9LwpLeT2nnqeQjDY2Yp77%2B9hcKv3RGgBieba%2BnlXZAbSjRwIVGbqtwq6CYMo5EpHUyEItgoe8OqLiYQZlpERHPw4mMOhG6XrYxaTGsMtQQOIjhzsSW7OaE3oN1DtAV1Sm1zmI%2FYEFkkv5k7fz25LrKkWw8PHwsxtGzuMVmeULueKGavhDUkZPMxt5eTTSY4OExPhfOcJ8RDzaMBK66goCiBLrwL9KFI9d0ahdLkIP35CUbjG2mw2P6lBtwnCMcIcHk8R5npScVqGJnRRqAy7WKt55GXBaBjl18Tm4r8sAKLxa8OpYaoMp%2Fmurd%2BiYICtvwB4EGXsI4tLDZL%2Bc83ecnBch3efLQZ0kbMMBdj7hTe56HrnnhYT8AtGzboHdpldyoRxzU2UjbwA0RZDZyvUI225rPPC2cD8gHpri7N3pgYWiH8udZP6tkOXLt3S5dDfgGy58LvXQkP8mePNBeH2vEYEnmnBnBu9NXuaW9FtnzEm1e749alC4dZOGWjn%2FY1LVTs0cqGvHmne3H6DsI4V01pvxWE%2F2T1WJcUgxOWXA8lM4vsBi2Nf5QX0ztiRt0VAOgwc%2FM6l09RDpjthbOW%2BTDcio29BjqkAbREUwfZBkZm%2BVAF6zf%2Be9H4rPwzYqmzZCBtUmGuLqCb%2FQ%2F8CwyVHgsF1pds4OM86LulGrSkvc3K%2BEuhsYZRl6R2nESFv%2F4Y0lwnScbO2XMXrJ2EXHyhwKbXVC2xkQa24MozM41EodTqlkSnf%2BvppXzTIpZySDebX2kkQjBi%2Brqru5qvBYGIDtx51rQqJQIez6c%2BKTTdSvw11FTFeKAfT2FQNIGC&X-Amz-Signature=e8d47544148c2893c54149fbbd389d44c1cf75581c069d974d93e8884869fef1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S52Q2HCR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCWbAsjtB%2F%2BB%2Bi0Eq%2F3ia9R2JlgLLi8DIdwciWPr%2Faw9wIhAPYfJS8BOB7CqOqq8Rox25m%2F2hZCsvV5LYoxd6gXU9CjKv8DCEQQABoMNjM3NDIzMTgzODA1IgzO1bKYTkzmJ2bq8xEq3ANc7B7dUzAZxa%2BS%2FGnQtTt7OIEZ5Uuy0Df%2BbZ%2F3i9LwpLeT2nnqeQjDY2Yp77%2B9hcKv3RGgBieba%2BnlXZAbSjRwIVGbqtwq6CYMo5EpHUyEItgoe8OqLiYQZlpERHPw4mMOhG6XrYxaTGsMtQQOIjhzsSW7OaE3oN1DtAV1Sm1zmI%2FYEFkkv5k7fz25LrKkWw8PHwsxtGzuMVmeULueKGavhDUkZPMxt5eTTSY4OExPhfOcJ8RDzaMBK66goCiBLrwL9KFI9d0ahdLkIP35CUbjG2mw2P6lBtwnCMcIcHk8R5npScVqGJnRRqAy7WKt55GXBaBjl18Tm4r8sAKLxa8OpYaoMp%2Fmurd%2BiYICtvwB4EGXsI4tLDZL%2Bc83ecnBch3efLQZ0kbMMBdj7hTe56HrnnhYT8AtGzboHdpldyoRxzU2UjbwA0RZDZyvUI225rPPC2cD8gHpri7N3pgYWiH8udZP6tkOXLt3S5dDfgGy58LvXQkP8mePNBeH2vEYEnmnBnBu9NXuaW9FtnzEm1e749alC4dZOGWjn%2FY1LVTs0cqGvHmne3H6DsI4V01pvxWE%2F2T1WJcUgxOWXA8lM4vsBi2Nf5QX0ztiRt0VAOgwc%2FM6l09RDpjthbOW%2BTDcio29BjqkAbREUwfZBkZm%2BVAF6zf%2Be9H4rPwzYqmzZCBtUmGuLqCb%2FQ%2F8CwyVHgsF1pds4OM86LulGrSkvc3K%2BEuhsYZRl6R2nESFv%2F4Y0lwnScbO2XMXrJ2EXHyhwKbXVC2xkQa24MozM41EodTqlkSnf%2BvppXzTIpZySDebX2kkQjBi%2Brqru5qvBYGIDtx51rQqJQIez6c%2BKTTdSvw11FTFeKAfT2FQNIGC&X-Amz-Signature=5cbd12809a2276e817f684d070114692aee3354659873efced320dcd8a2c4795&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S52Q2HCR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCWbAsjtB%2F%2BB%2Bi0Eq%2F3ia9R2JlgLLi8DIdwciWPr%2Faw9wIhAPYfJS8BOB7CqOqq8Rox25m%2F2hZCsvV5LYoxd6gXU9CjKv8DCEQQABoMNjM3NDIzMTgzODA1IgzO1bKYTkzmJ2bq8xEq3ANc7B7dUzAZxa%2BS%2FGnQtTt7OIEZ5Uuy0Df%2BbZ%2F3i9LwpLeT2nnqeQjDY2Yp77%2B9hcKv3RGgBieba%2BnlXZAbSjRwIVGbqtwq6CYMo5EpHUyEItgoe8OqLiYQZlpERHPw4mMOhG6XrYxaTGsMtQQOIjhzsSW7OaE3oN1DtAV1Sm1zmI%2FYEFkkv5k7fz25LrKkWw8PHwsxtGzuMVmeULueKGavhDUkZPMxt5eTTSY4OExPhfOcJ8RDzaMBK66goCiBLrwL9KFI9d0ahdLkIP35CUbjG2mw2P6lBtwnCMcIcHk8R5npScVqGJnRRqAy7WKt55GXBaBjl18Tm4r8sAKLxa8OpYaoMp%2Fmurd%2BiYICtvwB4EGXsI4tLDZL%2Bc83ecnBch3efLQZ0kbMMBdj7hTe56HrnnhYT8AtGzboHdpldyoRxzU2UjbwA0RZDZyvUI225rPPC2cD8gHpri7N3pgYWiH8udZP6tkOXLt3S5dDfgGy58LvXQkP8mePNBeH2vEYEnmnBnBu9NXuaW9FtnzEm1e749alC4dZOGWjn%2FY1LVTs0cqGvHmne3H6DsI4V01pvxWE%2F2T1WJcUgxOWXA8lM4vsBi2Nf5QX0ztiRt0VAOgwc%2FM6l09RDpjthbOW%2BTDcio29BjqkAbREUwfZBkZm%2BVAF6zf%2Be9H4rPwzYqmzZCBtUmGuLqCb%2FQ%2F8CwyVHgsF1pds4OM86LulGrSkvc3K%2BEuhsYZRl6R2nESFv%2F4Y0lwnScbO2XMXrJ2EXHyhwKbXVC2xkQa24MozM41EodTqlkSnf%2BvppXzTIpZySDebX2kkQjBi%2Brqru5qvBYGIDtx51rQqJQIez6c%2BKTTdSvw11FTFeKAfT2FQNIGC&X-Amz-Signature=10be4d51980dc491b84c60642e9ca4964d2bf09fdfc0de8539c6720907876368&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZV5H5LCT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIF9iYMuRyN8ny%2BsC92%2FKJOt2FfCd0ynxlhlLVRtYP6flAiEAxOaZtRtLM2d1iyhZjsghGfP8nX2dPgsqLkGYHu8%2Bag4q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDMR4Psz29xDNLed0lSrcA8YhhJDCYwMPpOEHJdkAuxkTuZLZG%2F1KlBk3Nop4UXJt7eqpJdHwMwko3%2Fr4YRxJDL1b43VgdZrk72D88p8ROLa2ZT2oe4TAAcIhNbj4Lun4eftEvDnRr5MtRhOdaKDhp7JhpMAnmMnXDJGOkdSgL1AITcCqLGizt0N7tfwOQKWh3r%2FJYjzNZPHSj3kmrwjD1vvj0hZRXVrmire8QMkImHYuTbu5wMOdkPhfaebfg02piOocpUZ6jnYOs%2FM2D32PbPimBWLu1uF4a%2FnRJu1zKKSknzc%2BuHbx9pJErQ6DUhBiMYk71XCEdCL7%2FylRs5cGNl8DvDgs7DKDhBRMcq19kByqqj%2BCdnK8qOUELpWBlBT0rCEHUn%2FufyODJgwFlxcBy2K%2BLDoiZBUck6wixf59kSYvarDglpBogcQ7nIzS6TX1TVQi7ZlgKZ%2F9%2B7Ac%2BfYi580TH7ZgR5F1qQyQqxMfwLNuW2A6Mg45%2Fg6UF1vZwSkMDAdtk5XCPJCXb04iGhJNDq4u9lKoS9VMcPGOILZ4zyuAD%2FNVRlET1Z3sGNOZ0qLs6pqiayuORDimVowucG4rF%2FJNCK2s6DPagrxdFRcxN%2BatILt9ebMhFLVy6DyzYHYioc4cqmHLCFsfwWKKMNaKjb0GOqUB7rGFcj%2FBsESW%2Bpw0pph6OSE8wpXzxEUToI%2FfvxND7uLE2dnroLL%2Bs6mikVPFIzCbgev52YnMqK3O2rz%2FeW%2Ftb4DlYFCjvSTdUStkIWnPWAp2BmRuUNmlu0C1SESLuRxc8QuTq3NM%2FuXsvyXOOIOYygJoAmLAyAhi%2FOWi7IcJOwBSfeWwkfAtBEq%2B%2Bp0RXQf9u0imOr0BcOkCMvmkCqTDpt8%2Fhpz%2B&X-Amz-Signature=5ccc0f7b4b209e5c1e48f7afb435939e756cf7cab022214402d78452f664776d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZV5H5LCT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIF9iYMuRyN8ny%2BsC92%2FKJOt2FfCd0ynxlhlLVRtYP6flAiEAxOaZtRtLM2d1iyhZjsghGfP8nX2dPgsqLkGYHu8%2Bag4q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDMR4Psz29xDNLed0lSrcA8YhhJDCYwMPpOEHJdkAuxkTuZLZG%2F1KlBk3Nop4UXJt7eqpJdHwMwko3%2Fr4YRxJDL1b43VgdZrk72D88p8ROLa2ZT2oe4TAAcIhNbj4Lun4eftEvDnRr5MtRhOdaKDhp7JhpMAnmMnXDJGOkdSgL1AITcCqLGizt0N7tfwOQKWh3r%2FJYjzNZPHSj3kmrwjD1vvj0hZRXVrmire8QMkImHYuTbu5wMOdkPhfaebfg02piOocpUZ6jnYOs%2FM2D32PbPimBWLu1uF4a%2FnRJu1zKKSknzc%2BuHbx9pJErQ6DUhBiMYk71XCEdCL7%2FylRs5cGNl8DvDgs7DKDhBRMcq19kByqqj%2BCdnK8qOUELpWBlBT0rCEHUn%2FufyODJgwFlxcBy2K%2BLDoiZBUck6wixf59kSYvarDglpBogcQ7nIzS6TX1TVQi7ZlgKZ%2F9%2B7Ac%2BfYi580TH7ZgR5F1qQyQqxMfwLNuW2A6Mg45%2Fg6UF1vZwSkMDAdtk5XCPJCXb04iGhJNDq4u9lKoS9VMcPGOILZ4zyuAD%2FNVRlET1Z3sGNOZ0qLs6pqiayuORDimVowucG4rF%2FJNCK2s6DPagrxdFRcxN%2BatILt9ebMhFLVy6DyzYHYioc4cqmHLCFsfwWKKMNaKjb0GOqUB7rGFcj%2FBsESW%2Bpw0pph6OSE8wpXzxEUToI%2FfvxND7uLE2dnroLL%2Bs6mikVPFIzCbgev52YnMqK3O2rz%2FeW%2Ftb4DlYFCjvSTdUStkIWnPWAp2BmRuUNmlu0C1SESLuRxc8QuTq3NM%2FuXsvyXOOIOYygJoAmLAyAhi%2FOWi7IcJOwBSfeWwkfAtBEq%2B%2Bp0RXQf9u0imOr0BcOkCMvmkCqTDpt8%2Fhpz%2B&X-Amz-Signature=5ad0e7a10f83797f8afa5ae0451af882937b76d81066b42ae8401ff157a5cd7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S52Q2HCR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCWbAsjtB%2F%2BB%2Bi0Eq%2F3ia9R2JlgLLi8DIdwciWPr%2Faw9wIhAPYfJS8BOB7CqOqq8Rox25m%2F2hZCsvV5LYoxd6gXU9CjKv8DCEQQABoMNjM3NDIzMTgzODA1IgzO1bKYTkzmJ2bq8xEq3ANc7B7dUzAZxa%2BS%2FGnQtTt7OIEZ5Uuy0Df%2BbZ%2F3i9LwpLeT2nnqeQjDY2Yp77%2B9hcKv3RGgBieba%2BnlXZAbSjRwIVGbqtwq6CYMo5EpHUyEItgoe8OqLiYQZlpERHPw4mMOhG6XrYxaTGsMtQQOIjhzsSW7OaE3oN1DtAV1Sm1zmI%2FYEFkkv5k7fz25LrKkWw8PHwsxtGzuMVmeULueKGavhDUkZPMxt5eTTSY4OExPhfOcJ8RDzaMBK66goCiBLrwL9KFI9d0ahdLkIP35CUbjG2mw2P6lBtwnCMcIcHk8R5npScVqGJnRRqAy7WKt55GXBaBjl18Tm4r8sAKLxa8OpYaoMp%2Fmurd%2BiYICtvwB4EGXsI4tLDZL%2Bc83ecnBch3efLQZ0kbMMBdj7hTe56HrnnhYT8AtGzboHdpldyoRxzU2UjbwA0RZDZyvUI225rPPC2cD8gHpri7N3pgYWiH8udZP6tkOXLt3S5dDfgGy58LvXQkP8mePNBeH2vEYEnmnBnBu9NXuaW9FtnzEm1e749alC4dZOGWjn%2FY1LVTs0cqGvHmne3H6DsI4V01pvxWE%2F2T1WJcUgxOWXA8lM4vsBi2Nf5QX0ztiRt0VAOgwc%2FM6l09RDpjthbOW%2BTDcio29BjqkAbREUwfZBkZm%2BVAF6zf%2Be9H4rPwzYqmzZCBtUmGuLqCb%2FQ%2F8CwyVHgsF1pds4OM86LulGrSkvc3K%2BEuhsYZRl6R2nESFv%2F4Y0lwnScbO2XMXrJ2EXHyhwKbXVC2xkQa24MozM41EodTqlkSnf%2BvppXzTIpZySDebX2kkQjBi%2Brqru5qvBYGIDtx51rQqJQIez6c%2BKTTdSvw11FTFeKAfT2FQNIGC&X-Amz-Signature=fbcd2d244f66cf36fbb87ed66106035a46e90da8f25ddd3fed59ec196d22b389&X-Amz-SignedHeaders=host&x-id=GetObject)
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