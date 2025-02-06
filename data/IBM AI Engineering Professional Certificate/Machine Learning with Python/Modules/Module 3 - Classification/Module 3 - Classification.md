

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XLHV64W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIAdxxOEns1gbk6SmAw%2BjB7QH%2FjoDgYgp4nrSgjiOcwhPAiB5X%2BnYYYlnq52lZhrGgxBJDbzhYuaDlVrtO%2FqVrBljRir%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIMx58DA%2FQoC61jtl02KtwD0n8m%2Bx%2FXfkvg9wZsbN9rgLochgRWJtgQxC12lEPQuUs6ZWvpuX9a7ahoDMO%2BwitMKjs9l56MzO%2BrqptTgVZhgUGSWW5KB5hZwr09bmBkGxRGtXMjCTB98QljYoc4zm7WxGmP%2BtqASDCFyMjKytflyoAfg5boSJvedxEYHhpQIC2XDwpASM1BdFjcPWg3ysVd2HqqTB9%2BeKEo31PXV%2B9Um1Yb7acyjs9wFNyM72YiZW3PutfRgdfi%2Bj2A9BIoL9ycPma7oYgcWB5O5AJHyoin2N8T6pwLFtzgcmdg%2FwvwyHMNaLDm7Tih%2FHs7MXaozBw1PB4Mwt%2B32SRMuoEpA29o8ML55Ib%2FOEjmv994%2F6HL2871ukXZzXkdSWIxccGazPiAcgnNDMCcXA5cLrvGI4WwFW%2Bxnd6BBqWmrm5w596oUUgmNijjgJbcn6arAe7Nbj%2BYlAMkE8kPK2DDSOPCmmrxOBFcLTTY11zHoQl4qE0aKUWvN0v%2F%2BrvjNQXiEI7qfYnkQMP47TCw3Nw6CYCOVkwFiyTGSTXChOkt%2BsSeGtM%2FnWLEcoJmBRPId9SLFYlqjAAU8X1y96KTDj3ejTD5Xg8ecpv5PQ%2B3NfAAoY9Vbr5Z4qAXvIXHs6L%2BT0GjlRkwytGRvQY6pgHRGBkLGvaxiL32FPrsmpeIZApKJTmd6uJheRkUTWrr9WNTF3MiSlXhHig0u4Rr9CBWMTcVfIWSXpalegZ%2FXtg2hAGzGmLWgHIe572nAbX85JZP2rO7a52iT%2Fpjzo3LbRJQsDf%2BaUU0ex7868xgihnFqlKKrt2hrnb%2FA%2BVj2o5lcOmHmz4duevjONtpj3w0Hrx22sRYi7qyc8iZmB%2BYcDpV22%2BDcCj2&X-Amz-Signature=51a0f0cbde2a13e761a070eb701d707c78a19de50975e19bcb471a2492973be2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XLHV64W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIAdxxOEns1gbk6SmAw%2BjB7QH%2FjoDgYgp4nrSgjiOcwhPAiB5X%2BnYYYlnq52lZhrGgxBJDbzhYuaDlVrtO%2FqVrBljRir%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIMx58DA%2FQoC61jtl02KtwD0n8m%2Bx%2FXfkvg9wZsbN9rgLochgRWJtgQxC12lEPQuUs6ZWvpuX9a7ahoDMO%2BwitMKjs9l56MzO%2BrqptTgVZhgUGSWW5KB5hZwr09bmBkGxRGtXMjCTB98QljYoc4zm7WxGmP%2BtqASDCFyMjKytflyoAfg5boSJvedxEYHhpQIC2XDwpASM1BdFjcPWg3ysVd2HqqTB9%2BeKEo31PXV%2B9Um1Yb7acyjs9wFNyM72YiZW3PutfRgdfi%2Bj2A9BIoL9ycPma7oYgcWB5O5AJHyoin2N8T6pwLFtzgcmdg%2FwvwyHMNaLDm7Tih%2FHs7MXaozBw1PB4Mwt%2B32SRMuoEpA29o8ML55Ib%2FOEjmv994%2F6HL2871ukXZzXkdSWIxccGazPiAcgnNDMCcXA5cLrvGI4WwFW%2Bxnd6BBqWmrm5w596oUUgmNijjgJbcn6arAe7Nbj%2BYlAMkE8kPK2DDSOPCmmrxOBFcLTTY11zHoQl4qE0aKUWvN0v%2F%2BrvjNQXiEI7qfYnkQMP47TCw3Nw6CYCOVkwFiyTGSTXChOkt%2BsSeGtM%2FnWLEcoJmBRPId9SLFYlqjAAU8X1y96KTDj3ejTD5Xg8ecpv5PQ%2B3NfAAoY9Vbr5Z4qAXvIXHs6L%2BT0GjlRkwytGRvQY6pgHRGBkLGvaxiL32FPrsmpeIZApKJTmd6uJheRkUTWrr9WNTF3MiSlXhHig0u4Rr9CBWMTcVfIWSXpalegZ%2FXtg2hAGzGmLWgHIe572nAbX85JZP2rO7a52iT%2Fpjzo3LbRJQsDf%2BaUU0ex7868xgihnFqlKKrt2hrnb%2FA%2BVj2o5lcOmHmz4duevjONtpj3w0Hrx22sRYi7qyc8iZmB%2BYcDpV22%2BDcCj2&X-Amz-Signature=97f7220b502c5440ffbe667541bab2d893930fcbb83f7213b12fbc81f5a47280&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XLHV64W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIAdxxOEns1gbk6SmAw%2BjB7QH%2FjoDgYgp4nrSgjiOcwhPAiB5X%2BnYYYlnq52lZhrGgxBJDbzhYuaDlVrtO%2FqVrBljRir%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIMx58DA%2FQoC61jtl02KtwD0n8m%2Bx%2FXfkvg9wZsbN9rgLochgRWJtgQxC12lEPQuUs6ZWvpuX9a7ahoDMO%2BwitMKjs9l56MzO%2BrqptTgVZhgUGSWW5KB5hZwr09bmBkGxRGtXMjCTB98QljYoc4zm7WxGmP%2BtqASDCFyMjKytflyoAfg5boSJvedxEYHhpQIC2XDwpASM1BdFjcPWg3ysVd2HqqTB9%2BeKEo31PXV%2B9Um1Yb7acyjs9wFNyM72YiZW3PutfRgdfi%2Bj2A9BIoL9ycPma7oYgcWB5O5AJHyoin2N8T6pwLFtzgcmdg%2FwvwyHMNaLDm7Tih%2FHs7MXaozBw1PB4Mwt%2B32SRMuoEpA29o8ML55Ib%2FOEjmv994%2F6HL2871ukXZzXkdSWIxccGazPiAcgnNDMCcXA5cLrvGI4WwFW%2Bxnd6BBqWmrm5w596oUUgmNijjgJbcn6arAe7Nbj%2BYlAMkE8kPK2DDSOPCmmrxOBFcLTTY11zHoQl4qE0aKUWvN0v%2F%2BrvjNQXiEI7qfYnkQMP47TCw3Nw6CYCOVkwFiyTGSTXChOkt%2BsSeGtM%2FnWLEcoJmBRPId9SLFYlqjAAU8X1y96KTDj3ejTD5Xg8ecpv5PQ%2B3NfAAoY9Vbr5Z4qAXvIXHs6L%2BT0GjlRkwytGRvQY6pgHRGBkLGvaxiL32FPrsmpeIZApKJTmd6uJheRkUTWrr9WNTF3MiSlXhHig0u4Rr9CBWMTcVfIWSXpalegZ%2FXtg2hAGzGmLWgHIe572nAbX85JZP2rO7a52iT%2Fpjzo3LbRJQsDf%2BaUU0ex7868xgihnFqlKKrt2hrnb%2FA%2BVj2o5lcOmHmz4duevjONtpj3w0Hrx22sRYi7qyc8iZmB%2BYcDpV22%2BDcCj2&X-Amz-Signature=6f564c8ac774562703ce976309c99231e0dc38152cb38fe1aa6aeafca1ee4c62&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAAFRLXD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIGsrKCl6kZ5TgIKH8%2BAfSuBnJyj4Xbxt%2FoX6YOjTE9%2BmAiBNsdm9oyJVn5%2FGmAQwdRngHtOGR77U6tGfdjuJ8uMgeyr%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIMnvFbLPxwbWnmewuMKtwDNt3XMnplylVRCqcUsN9%2B0dzuKUqLg5SKU3%2FR4Ux9jEvBGG1XbPLWOydRdQogpGBFv0tN7oE8mszvy2B5Y4yA8RtzgaHYHxW04vPkTWiMoaS0J9IUN7qqj9T9PiJQW2o%2Fj8a0bIpnsViLDcOAc0MmV2cITAk2JM395Ic9mD8gPEbH6a7oYZMiM%2F642SIlFRoAC8v%2F0Mo9AMF5QZgnb%2BKv4T%2B%2BuV7QbxyEOlAeHbuXq2IAiwdKfndJKibSiVKELBuk3DOgSWGin9kiS0l41%2F2c79hTJA%2FTIwUKIi6%2BjRdnRxzk5ikePnRUlPrSyUWd7Tze4R2%2FggSpPHrOSJN2V%2BfLxmQiWmjS5PR7YURGih%2F5BounxG8%2BOCxDU3pAKaq%2Fnz8Ie7uEjOtgO7l9G27rpg9tXj2QGbz0XMW%2FJgsUKOIWMiph0lyyzbw5Z7PhoIWpvREEgdSyWhG08iT0EtbGRqYgPQsgaM83oy3k7sE4bixVK%2F7O%2BwV1p1WgXmdC0FsxytSkhLQtkFu2yN5x0NBf073Z2ORfeaX7Cyz8Inab0Cix27voibbM3MYRqIElJovbsNJUgaAGCv6SOi2MwVLH5dymBd%2BzbQo8ky3STE8BZCMUYEWJ8HM0jlRJomvX1UgwxdGRvQY6pgEeYA0UpVJyyxCoUKbEFGJB6SF9zFOs%2B3asg4O63XxGnHd7X1EJGOHW4jb1PvS26jAvF%2Fhkkj9%2B0iIwjrpDlvUUEGsDxgab1U64Fdw1QHafA64O9VhTp0NWYd%2FEFmWWDPIJFZbf41nRPj%2BlmZQ3LmZ5HhKBmOzJorKYiKN1gNJSWg5hvHhqSoyQQY5lemXyTUY%2FefXqtbPSzVGQAzaymLKgqk9ARJzx&X-Amz-Signature=b9eeb245a0ff16b7c17ea59d82cc4d1f68f5d2b92a71a85077380f451810ebcb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAAFRLXD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIGsrKCl6kZ5TgIKH8%2BAfSuBnJyj4Xbxt%2FoX6YOjTE9%2BmAiBNsdm9oyJVn5%2FGmAQwdRngHtOGR77U6tGfdjuJ8uMgeyr%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIMnvFbLPxwbWnmewuMKtwDNt3XMnplylVRCqcUsN9%2B0dzuKUqLg5SKU3%2FR4Ux9jEvBGG1XbPLWOydRdQogpGBFv0tN7oE8mszvy2B5Y4yA8RtzgaHYHxW04vPkTWiMoaS0J9IUN7qqj9T9PiJQW2o%2Fj8a0bIpnsViLDcOAc0MmV2cITAk2JM395Ic9mD8gPEbH6a7oYZMiM%2F642SIlFRoAC8v%2F0Mo9AMF5QZgnb%2BKv4T%2B%2BuV7QbxyEOlAeHbuXq2IAiwdKfndJKibSiVKELBuk3DOgSWGin9kiS0l41%2F2c79hTJA%2FTIwUKIi6%2BjRdnRxzk5ikePnRUlPrSyUWd7Tze4R2%2FggSpPHrOSJN2V%2BfLxmQiWmjS5PR7YURGih%2F5BounxG8%2BOCxDU3pAKaq%2Fnz8Ie7uEjOtgO7l9G27rpg9tXj2QGbz0XMW%2FJgsUKOIWMiph0lyyzbw5Z7PhoIWpvREEgdSyWhG08iT0EtbGRqYgPQsgaM83oy3k7sE4bixVK%2F7O%2BwV1p1WgXmdC0FsxytSkhLQtkFu2yN5x0NBf073Z2ORfeaX7Cyz8Inab0Cix27voibbM3MYRqIElJovbsNJUgaAGCv6SOi2MwVLH5dymBd%2BzbQo8ky3STE8BZCMUYEWJ8HM0jlRJomvX1UgwxdGRvQY6pgEeYA0UpVJyyxCoUKbEFGJB6SF9zFOs%2B3asg4O63XxGnHd7X1EJGOHW4jb1PvS26jAvF%2Fhkkj9%2B0iIwjrpDlvUUEGsDxgab1U64Fdw1QHafA64O9VhTp0NWYd%2FEFmWWDPIJFZbf41nRPj%2BlmZQ3LmZ5HhKBmOzJorKYiKN1gNJSWg5hvHhqSoyQQY5lemXyTUY%2FefXqtbPSzVGQAzaymLKgqk9ARJzx&X-Amz-Signature=03ea3b02fc624993be89e6f0c30e965bfd0140a92878ec92f78400a001ce3b49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XLHV64W%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081921Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIAdxxOEns1gbk6SmAw%2BjB7QH%2FjoDgYgp4nrSgjiOcwhPAiB5X%2BnYYYlnq52lZhrGgxBJDbzhYuaDlVrtO%2FqVrBljRir%2FAwhZEAAaDDYzNzQyMzE4MzgwNSIMx58DA%2FQoC61jtl02KtwD0n8m%2Bx%2FXfkvg9wZsbN9rgLochgRWJtgQxC12lEPQuUs6ZWvpuX9a7ahoDMO%2BwitMKjs9l56MzO%2BrqptTgVZhgUGSWW5KB5hZwr09bmBkGxRGtXMjCTB98QljYoc4zm7WxGmP%2BtqASDCFyMjKytflyoAfg5boSJvedxEYHhpQIC2XDwpASM1BdFjcPWg3ysVd2HqqTB9%2BeKEo31PXV%2B9Um1Yb7acyjs9wFNyM72YiZW3PutfRgdfi%2Bj2A9BIoL9ycPma7oYgcWB5O5AJHyoin2N8T6pwLFtzgcmdg%2FwvwyHMNaLDm7Tih%2FHs7MXaozBw1PB4Mwt%2B32SRMuoEpA29o8ML55Ib%2FOEjmv994%2F6HL2871ukXZzXkdSWIxccGazPiAcgnNDMCcXA5cLrvGI4WwFW%2Bxnd6BBqWmrm5w596oUUgmNijjgJbcn6arAe7Nbj%2BYlAMkE8kPK2DDSOPCmmrxOBFcLTTY11zHoQl4qE0aKUWvN0v%2F%2BrvjNQXiEI7qfYnkQMP47TCw3Nw6CYCOVkwFiyTGSTXChOkt%2BsSeGtM%2FnWLEcoJmBRPId9SLFYlqjAAU8X1y96KTDj3ejTD5Xg8ecpv5PQ%2B3NfAAoY9Vbr5Z4qAXvIXHs6L%2BT0GjlRkwytGRvQY6pgHRGBkLGvaxiL32FPrsmpeIZApKJTmd6uJheRkUTWrr9WNTF3MiSlXhHig0u4Rr9CBWMTcVfIWSXpalegZ%2FXtg2hAGzGmLWgHIe572nAbX85JZP2rO7a52iT%2Fpjzo3LbRJQsDf%2BaUU0ex7868xgihnFqlKKrt2hrnb%2FA%2BVj2o5lcOmHmz4duevjONtpj3w0Hrx22sRYi7qyc8iZmB%2BYcDpV22%2BDcCj2&X-Amz-Signature=2738cdd982688c9da5b4b45024509534bf60e09e7c74ddb882ac987bb139cfdc&X-Amz-SignedHeaders=host&x-id=GetObject)
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