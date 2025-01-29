

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IH2NXJQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCHyfS0ugl%2FqU74IY2vxOvBZW9DTaDejfHgnyUJTC3D9kCIQCJpT75o2YDmxt%2BSOvWlPTHG50qEuKCgRSMT4i%2B%2BxdXBiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM885SS5Soum5n%2FcnLKtwDSTgjpmJznxEXIK4MQaBjOJ0%2BXEN80Slbpc5lHrb1lw00VdvzICLmVm%2BRoVC1qWX2dgTImwIcd8nDD4ak%2Bb9yA0tb%2BwSTNyJTB8bnb%2F2bjIIp9PHv%2F4epkICMv9ObpsVvghOuTb2yQXZlbBN6lSVJPyZ%2Fueo3ylg4fKfXaRVJKn2%2BhIyJ%2F3uqC8z0VcSOd4ZsQuwtW8jdxWbLRse16C%2FBIt7UOZdP3d9x4bYhVWBFCzvE2H0YmIT42mxG1GUCLtIzpRt84heMow3Xuje9HQD6Rv6V4nTCDVymmYTcnFIViW5Ix%2B3%2BzCvZagKIux1rjqC7zLkQn0dwsmigqL0ogaQCm%2FxV34544a6B0Ej4rQMBC9R%2BPiZfo9sz7eNoJUJf35A9bOfeMJUTdwdUXo32JentRvNGgZx78lbBLYc43xONUGHX%2BtnQrnosrghPIgs1chfkUsK8BkCOzebSDKomCssmXyMyQCVlO%2BX7mm9SsOBbaKHiAA%2FzjSr%2FEL1eFBUxy5nNy0nclqDP%2B9BNLXKO9UeMPcNfy5j8%2Bo79dlCss7lDb9YNAqFtz7smSDa3Q0Nejx05gtlluqBQZNixpz%2B%2F2eoNktzuw7P61sCWkw07%2BabvGToGW30xq7MaruNacfowy%2FTpvAY6pgFre5Ld11A2FH627WsbZrCI%2BNJpeQNncICKDAmbq%2Faw1M97lklVAum9SR8S0pIBwSbYk4M4V3394QtMji7KGSwIXmsFCMaMdHmYw8uycJho8MDhC5LN%2BKlB8Ko2LkRY7ZqyTCRlKKvFqOmcdb6L0bk48oXvba1cFcqoZecuS0%2FweIRwn%2FpWfsQmT39HVP6StOyjXhvSxnncMKD2Ix4ur0SsPVTF57fj&X-Amz-Signature=67145e5261f72c792e8b0348c9c9b517e49eb0ff7566e8d1380b140e06490386&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IH2NXJQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCHyfS0ugl%2FqU74IY2vxOvBZW9DTaDejfHgnyUJTC3D9kCIQCJpT75o2YDmxt%2BSOvWlPTHG50qEuKCgRSMT4i%2B%2BxdXBiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM885SS5Soum5n%2FcnLKtwDSTgjpmJznxEXIK4MQaBjOJ0%2BXEN80Slbpc5lHrb1lw00VdvzICLmVm%2BRoVC1qWX2dgTImwIcd8nDD4ak%2Bb9yA0tb%2BwSTNyJTB8bnb%2F2bjIIp9PHv%2F4epkICMv9ObpsVvghOuTb2yQXZlbBN6lSVJPyZ%2Fueo3ylg4fKfXaRVJKn2%2BhIyJ%2F3uqC8z0VcSOd4ZsQuwtW8jdxWbLRse16C%2FBIt7UOZdP3d9x4bYhVWBFCzvE2H0YmIT42mxG1GUCLtIzpRt84heMow3Xuje9HQD6Rv6V4nTCDVymmYTcnFIViW5Ix%2B3%2BzCvZagKIux1rjqC7zLkQn0dwsmigqL0ogaQCm%2FxV34544a6B0Ej4rQMBC9R%2BPiZfo9sz7eNoJUJf35A9bOfeMJUTdwdUXo32JentRvNGgZx78lbBLYc43xONUGHX%2BtnQrnosrghPIgs1chfkUsK8BkCOzebSDKomCssmXyMyQCVlO%2BX7mm9SsOBbaKHiAA%2FzjSr%2FEL1eFBUxy5nNy0nclqDP%2B9BNLXKO9UeMPcNfy5j8%2Bo79dlCss7lDb9YNAqFtz7smSDa3Q0Nejx05gtlluqBQZNixpz%2B%2F2eoNktzuw7P61sCWkw07%2BabvGToGW30xq7MaruNacfowy%2FTpvAY6pgFre5Ld11A2FH627WsbZrCI%2BNJpeQNncICKDAmbq%2Faw1M97lklVAum9SR8S0pIBwSbYk4M4V3394QtMji7KGSwIXmsFCMaMdHmYw8uycJho8MDhC5LN%2BKlB8Ko2LkRY7ZqyTCRlKKvFqOmcdb6L0bk48oXvba1cFcqoZecuS0%2FweIRwn%2FpWfsQmT39HVP6StOyjXhvSxnncMKD2Ix4ur0SsPVTF57fj&X-Amz-Signature=9cecc3d2f1fcc3951856e228bcac26e06cf48951afe1e5388171349b4142e8f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IH2NXJQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCHyfS0ugl%2FqU74IY2vxOvBZW9DTaDejfHgnyUJTC3D9kCIQCJpT75o2YDmxt%2BSOvWlPTHG50qEuKCgRSMT4i%2B%2BxdXBiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM885SS5Soum5n%2FcnLKtwDSTgjpmJznxEXIK4MQaBjOJ0%2BXEN80Slbpc5lHrb1lw00VdvzICLmVm%2BRoVC1qWX2dgTImwIcd8nDD4ak%2Bb9yA0tb%2BwSTNyJTB8bnb%2F2bjIIp9PHv%2F4epkICMv9ObpsVvghOuTb2yQXZlbBN6lSVJPyZ%2Fueo3ylg4fKfXaRVJKn2%2BhIyJ%2F3uqC8z0VcSOd4ZsQuwtW8jdxWbLRse16C%2FBIt7UOZdP3d9x4bYhVWBFCzvE2H0YmIT42mxG1GUCLtIzpRt84heMow3Xuje9HQD6Rv6V4nTCDVymmYTcnFIViW5Ix%2B3%2BzCvZagKIux1rjqC7zLkQn0dwsmigqL0ogaQCm%2FxV34544a6B0Ej4rQMBC9R%2BPiZfo9sz7eNoJUJf35A9bOfeMJUTdwdUXo32JentRvNGgZx78lbBLYc43xONUGHX%2BtnQrnosrghPIgs1chfkUsK8BkCOzebSDKomCssmXyMyQCVlO%2BX7mm9SsOBbaKHiAA%2FzjSr%2FEL1eFBUxy5nNy0nclqDP%2B9BNLXKO9UeMPcNfy5j8%2Bo79dlCss7lDb9YNAqFtz7smSDa3Q0Nejx05gtlluqBQZNixpz%2B%2F2eoNktzuw7P61sCWkw07%2BabvGToGW30xq7MaruNacfowy%2FTpvAY6pgFre5Ld11A2FH627WsbZrCI%2BNJpeQNncICKDAmbq%2Faw1M97lklVAum9SR8S0pIBwSbYk4M4V3394QtMji7KGSwIXmsFCMaMdHmYw8uycJho8MDhC5LN%2BKlB8Ko2LkRY7ZqyTCRlKKvFqOmcdb6L0bk48oXvba1cFcqoZecuS0%2FweIRwn%2FpWfsQmT39HVP6StOyjXhvSxnncMKD2Ix4ur0SsPVTF57fj&X-Amz-Signature=ee1befb327ef805bc88470fbb75bbd3548e287b4a020a47293842f8aee8db434&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664U34CXHX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHATyOsb7Yd2OCOjXPVBESPUq8rEeccEq2OWvF5tYLoCAiBFDzsS7fuz3GZ7G%2FwS390fojZhhKLc9QItezaG48%2FYdyqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmgcZkU0Vr3o%2FkCXaKtwDA6XsVlKorpYbXlGqlh5Awmmp1bG5eoTP1sdiGF9nfoXDXi5w%2FK7yBG9wdm%2F04fSkT8WTVin%2Fo6KcXyiva0B00snPw1yilM0GoPJpLsHTizdD91yxqmk8fwHSTEwhw%2FDRBgT1c75QH34yTS4O78ieO46NqlWlJKFBmnsXMB8pel5CzhhQa7oTs2yQwAGUL9Vj9932TSlJ2B490vi%2BOaRu2QDMPLSTww9R0hV4mbjGsZ9wmpcgzSgRi64xs6w01tBubuxuIxf10A%2BaKfVpXPwc8hyDD0MPXbcXNHvS8UJrRQWpKLIhWrFADKpFb%2BT847cyBlj9emGJaq%2BQkgvrE7Y6DPhiHQeutA8GOfNfeXlVZIpFcNWQIOS6MOc6pFXi%2Fl4T0FPcYlsNiaAK256qO5SGiGXdc2I2eQ5kz022lMTRlTuQjJ%2BfZlvi%2FPDqB0od2UBJPTimVI5Lt3dbztfKkiAcCnE%2F%2BlPpLA0m5iQLXKmhBSgAyTQEXqu1Z7CZBOv00Q31qEuPXXeGBGkxKvp2QyYGXNrQwTb1opF0Me7AX0GVNfmLeBIU98OVKxodGMIcTM4e2XSkOxVkcWX9eCoK65CIxix3jsIaBOsdMpcW%2BiYcBY4VntLduXR%2Fe2o4WWUw9PTpvAY6pgG%2F9hoD03fWI06BqEfiYdEMswmBCqNZRts9poG7scpSnJEUeSMqg08klTePk8wh9iQOpl%2ByjqC0TZp18YiOA5c0uE4nV3N7Bde2yMN4oJL%2BOGUq1A1n45%2BOixP%2BayBzXmq8Dek0sJjmy%2BG4hc4fWgSgR00q2Z7s00%2FUIdc6yfELtue9%2FAMpmE3sg%2B3GPACioFR40AQJoX59VYEhJQ7RPfMI5W%2FRvnBf&X-Amz-Signature=43b74a00e23f61ce0521fefcca5f1e77ea92d6210ac98d678bbf5154b1f58dc7&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664U34CXHX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHATyOsb7Yd2OCOjXPVBESPUq8rEeccEq2OWvF5tYLoCAiBFDzsS7fuz3GZ7G%2FwS390fojZhhKLc9QItezaG48%2FYdyqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmgcZkU0Vr3o%2FkCXaKtwDA6XsVlKorpYbXlGqlh5Awmmp1bG5eoTP1sdiGF9nfoXDXi5w%2FK7yBG9wdm%2F04fSkT8WTVin%2Fo6KcXyiva0B00snPw1yilM0GoPJpLsHTizdD91yxqmk8fwHSTEwhw%2FDRBgT1c75QH34yTS4O78ieO46NqlWlJKFBmnsXMB8pel5CzhhQa7oTs2yQwAGUL9Vj9932TSlJ2B490vi%2BOaRu2QDMPLSTww9R0hV4mbjGsZ9wmpcgzSgRi64xs6w01tBubuxuIxf10A%2BaKfVpXPwc8hyDD0MPXbcXNHvS8UJrRQWpKLIhWrFADKpFb%2BT847cyBlj9emGJaq%2BQkgvrE7Y6DPhiHQeutA8GOfNfeXlVZIpFcNWQIOS6MOc6pFXi%2Fl4T0FPcYlsNiaAK256qO5SGiGXdc2I2eQ5kz022lMTRlTuQjJ%2BfZlvi%2FPDqB0od2UBJPTimVI5Lt3dbztfKkiAcCnE%2F%2BlPpLA0m5iQLXKmhBSgAyTQEXqu1Z7CZBOv00Q31qEuPXXeGBGkxKvp2QyYGXNrQwTb1opF0Me7AX0GVNfmLeBIU98OVKxodGMIcTM4e2XSkOxVkcWX9eCoK65CIxix3jsIaBOsdMpcW%2BiYcBY4VntLduXR%2Fe2o4WWUw9PTpvAY6pgG%2F9hoD03fWI06BqEfiYdEMswmBCqNZRts9poG7scpSnJEUeSMqg08klTePk8wh9iQOpl%2ByjqC0TZp18YiOA5c0uE4nV3N7Bde2yMN4oJL%2BOGUq1A1n45%2BOixP%2BayBzXmq8Dek0sJjmy%2BG4hc4fWgSgR00q2Z7s00%2FUIdc6yfELtue9%2FAMpmE3sg%2B3GPACioFR40AQJoX59VYEhJQ7RPfMI5W%2FRvnBf&X-Amz-Signature=b58f6b13a6916f8c28ee5603759ecd4fb4ecd844388906911f4152ae30ba2bf6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IH2NXJQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCHyfS0ugl%2FqU74IY2vxOvBZW9DTaDejfHgnyUJTC3D9kCIQCJpT75o2YDmxt%2BSOvWlPTHG50qEuKCgRSMT4i%2B%2BxdXBiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM885SS5Soum5n%2FcnLKtwDSTgjpmJznxEXIK4MQaBjOJ0%2BXEN80Slbpc5lHrb1lw00VdvzICLmVm%2BRoVC1qWX2dgTImwIcd8nDD4ak%2Bb9yA0tb%2BwSTNyJTB8bnb%2F2bjIIp9PHv%2F4epkICMv9ObpsVvghOuTb2yQXZlbBN6lSVJPyZ%2Fueo3ylg4fKfXaRVJKn2%2BhIyJ%2F3uqC8z0VcSOd4ZsQuwtW8jdxWbLRse16C%2FBIt7UOZdP3d9x4bYhVWBFCzvE2H0YmIT42mxG1GUCLtIzpRt84heMow3Xuje9HQD6Rv6V4nTCDVymmYTcnFIViW5Ix%2B3%2BzCvZagKIux1rjqC7zLkQn0dwsmigqL0ogaQCm%2FxV34544a6B0Ej4rQMBC9R%2BPiZfo9sz7eNoJUJf35A9bOfeMJUTdwdUXo32JentRvNGgZx78lbBLYc43xONUGHX%2BtnQrnosrghPIgs1chfkUsK8BkCOzebSDKomCssmXyMyQCVlO%2BX7mm9SsOBbaKHiAA%2FzjSr%2FEL1eFBUxy5nNy0nclqDP%2B9BNLXKO9UeMPcNfy5j8%2Bo79dlCss7lDb9YNAqFtz7smSDa3Q0Nejx05gtlluqBQZNixpz%2B%2F2eoNktzuw7P61sCWkw07%2BabvGToGW30xq7MaruNacfowy%2FTpvAY6pgFre5Ld11A2FH627WsbZrCI%2BNJpeQNncICKDAmbq%2Faw1M97lklVAum9SR8S0pIBwSbYk4M4V3394QtMji7KGSwIXmsFCMaMdHmYw8uycJho8MDhC5LN%2BKlB8Ko2LkRY7ZqyTCRlKKvFqOmcdb6L0bk48oXvba1cFcqoZecuS0%2FweIRwn%2FpWfsQmT39HVP6StOyjXhvSxnncMKD2Ix4ur0SsPVTF57fj&X-Amz-Signature=09bde075b03efde98310cef1369f8beab2efbf8e753a45c9771eecb1c50cb857&X-Amz-SignedHeaders=host&x-id=GetObject)
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