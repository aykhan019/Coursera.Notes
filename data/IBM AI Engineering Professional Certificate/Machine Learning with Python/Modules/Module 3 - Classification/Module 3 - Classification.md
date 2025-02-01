

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4RXLOE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEhYnFYysoaVJ1QWKUZL1842m0nn5UjDnLVEP5vRiymQIhALR2tqdt%2BGzVn9HTBJ8miE442AWZb7ufO4RdHrtL8fRBKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ8brbrgI6KpfRx8sq3APs1OffjWSKyrOJ4XSTNJgYzcqGekcNtOXrgk55wcUl9hxZNOIcmD1%2FbfCgI%2F1KjB5mSzzA4v%2BoqHn90Uug5FyhBOV6VQebr0vwAydNSWGqINfKiCqzbRerheHz%2FGpKrrgWr3j%2FBjjzV7kNlSf%2Bo9GlpOxhvlWU%2FDeK480U9KY%2BePpukCViadD0iitKLJnod0rRIkj7UvSwMiALUB4hh51GgO5FzVER0fg%2FrPxyAEIpGZXoBa%2FTwxGX5%2F90dLK5Pa5fezFGF7eHWYsvgGXy2PB1JX8nFPCOCAr4Z%2BXobS1ydhAKk3fkxNIaT%2FjY26tb63S8QlvxziAgAkpRNOyzA1L1rsyYCqk0wFhv6z%2FoKMzgx%2Fz1KBUyEMY3KeOiNTZYeo0Z2wZzGrNZgGMMBaFH4nVM6mXmW8IOoXeIAOLlfIcJN5EGrBEw3wLUY3Fpj2m5B3UCffkyAtukiubxH74xlD2wztdJo6Q142r3pmaZhZBHXiZYpplBDwaok%2BA4HlhNYoLrYoTVAnb6lzk9LdRtJezZJjlGMzYTUXXdWNddlNoWLMKauBiI9vM5ODOgFiMqgLzIva577EksLUZ68P8%2Fpqy0osM4v12fdJui4tM6qU2p41aD1XLc33QWIsMa6DCVsfq8BjqkAVlPDWBGxz%2FKppH38qaIq%2BRv144aRq4D1O3%2B%2FafbkcE%2FCsgKW5vh%2BXLAwevd4wmlmqbf02eKw4ROQxC%2Fz%2F7jZWQTf0bdSl%2FXmkbmX4VJ3cCZ%2FSeEL142ZPpsyYwQsEyQhM%2Fk9Y8YjOmBjJtXt%2Bo39VFS2s6qo3H38QYD6sSpf%2BzI1Gxv8OZ49M9xSmhn9idpGpoxToyZPXy%2FN2M47jpoT3PEHyK6&X-Amz-Signature=53fd156e7e27ea50cff5e4550aea6f70edbfcfd6b3a57500030f0d5cabbe83af&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4RXLOE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEhYnFYysoaVJ1QWKUZL1842m0nn5UjDnLVEP5vRiymQIhALR2tqdt%2BGzVn9HTBJ8miE442AWZb7ufO4RdHrtL8fRBKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ8brbrgI6KpfRx8sq3APs1OffjWSKyrOJ4XSTNJgYzcqGekcNtOXrgk55wcUl9hxZNOIcmD1%2FbfCgI%2F1KjB5mSzzA4v%2BoqHn90Uug5FyhBOV6VQebr0vwAydNSWGqINfKiCqzbRerheHz%2FGpKrrgWr3j%2FBjjzV7kNlSf%2Bo9GlpOxhvlWU%2FDeK480U9KY%2BePpukCViadD0iitKLJnod0rRIkj7UvSwMiALUB4hh51GgO5FzVER0fg%2FrPxyAEIpGZXoBa%2FTwxGX5%2F90dLK5Pa5fezFGF7eHWYsvgGXy2PB1JX8nFPCOCAr4Z%2BXobS1ydhAKk3fkxNIaT%2FjY26tb63S8QlvxziAgAkpRNOyzA1L1rsyYCqk0wFhv6z%2FoKMzgx%2Fz1KBUyEMY3KeOiNTZYeo0Z2wZzGrNZgGMMBaFH4nVM6mXmW8IOoXeIAOLlfIcJN5EGrBEw3wLUY3Fpj2m5B3UCffkyAtukiubxH74xlD2wztdJo6Q142r3pmaZhZBHXiZYpplBDwaok%2BA4HlhNYoLrYoTVAnb6lzk9LdRtJezZJjlGMzYTUXXdWNddlNoWLMKauBiI9vM5ODOgFiMqgLzIva577EksLUZ68P8%2Fpqy0osM4v12fdJui4tM6qU2p41aD1XLc33QWIsMa6DCVsfq8BjqkAVlPDWBGxz%2FKppH38qaIq%2BRv144aRq4D1O3%2B%2FafbkcE%2FCsgKW5vh%2BXLAwevd4wmlmqbf02eKw4ROQxC%2Fz%2F7jZWQTf0bdSl%2FXmkbmX4VJ3cCZ%2FSeEL142ZPpsyYwQsEyQhM%2Fk9Y8YjOmBjJtXt%2Bo39VFS2s6qo3H38QYD6sSpf%2BzI1Gxv8OZ49M9xSmhn9idpGpoxToyZPXy%2FN2M47jpoT3PEHyK6&X-Amz-Signature=5b9dd2c9f52668d0b17576d95e964adcdc402fa2211e0c44d0c946d7233a1a25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4RXLOE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEhYnFYysoaVJ1QWKUZL1842m0nn5UjDnLVEP5vRiymQIhALR2tqdt%2BGzVn9HTBJ8miE442AWZb7ufO4RdHrtL8fRBKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ8brbrgI6KpfRx8sq3APs1OffjWSKyrOJ4XSTNJgYzcqGekcNtOXrgk55wcUl9hxZNOIcmD1%2FbfCgI%2F1KjB5mSzzA4v%2BoqHn90Uug5FyhBOV6VQebr0vwAydNSWGqINfKiCqzbRerheHz%2FGpKrrgWr3j%2FBjjzV7kNlSf%2Bo9GlpOxhvlWU%2FDeK480U9KY%2BePpukCViadD0iitKLJnod0rRIkj7UvSwMiALUB4hh51GgO5FzVER0fg%2FrPxyAEIpGZXoBa%2FTwxGX5%2F90dLK5Pa5fezFGF7eHWYsvgGXy2PB1JX8nFPCOCAr4Z%2BXobS1ydhAKk3fkxNIaT%2FjY26tb63S8QlvxziAgAkpRNOyzA1L1rsyYCqk0wFhv6z%2FoKMzgx%2Fz1KBUyEMY3KeOiNTZYeo0Z2wZzGrNZgGMMBaFH4nVM6mXmW8IOoXeIAOLlfIcJN5EGrBEw3wLUY3Fpj2m5B3UCffkyAtukiubxH74xlD2wztdJo6Q142r3pmaZhZBHXiZYpplBDwaok%2BA4HlhNYoLrYoTVAnb6lzk9LdRtJezZJjlGMzYTUXXdWNddlNoWLMKauBiI9vM5ODOgFiMqgLzIva577EksLUZ68P8%2Fpqy0osM4v12fdJui4tM6qU2p41aD1XLc33QWIsMa6DCVsfq8BjqkAVlPDWBGxz%2FKppH38qaIq%2BRv144aRq4D1O3%2B%2FafbkcE%2FCsgKW5vh%2BXLAwevd4wmlmqbf02eKw4ROQxC%2Fz%2F7jZWQTf0bdSl%2FXmkbmX4VJ3cCZ%2FSeEL142ZPpsyYwQsEyQhM%2Fk9Y8YjOmBjJtXt%2Bo39VFS2s6qo3H38QYD6sSpf%2BzI1Gxv8OZ49M9xSmhn9idpGpoxToyZPXy%2FN2M47jpoT3PEHyK6&X-Amz-Signature=d756404dd8fbefdf043e1bd41bf923f3bb62d35b871023cf72bea21c325284a0&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UPHU3ZT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEe14%2Bc1y9lSRoYbBQyNbaDzo1S9anY8duX3NePzWjMoAiEAy1pyIrIlqDaF7JpsUTCBCHaYbxwxRqk06yfk2BTvaxUqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBex0OFLjJK6GnbBdircAxUyi5WFYhzn1BiAzhL78vE2p2tKNr3fcsp51cnkrX%2BXeYZKSRPWsh94%2FYyyumpH%2BmQPJseg6Ay8fblIq4co5SeNeMpniCZlR0%2B5AXf0lhTGR9hbaYiSpQd%2FRO%2BiIf%2B1DGLfkPipLBigQ2Tym4f5%2FCzyeElkhPEsc1sW11G1COet%2FUXm95ib9vyMFxat7R4owO53eeYln2wyHvUyMUCUki98eXcLzq%2F6Unu3E%2B%2BNEYvLJzdfxhX0MhIhGYfo79TOWb0%2BbTudtXpH7gFfMeNZVevnfOSxqAY%2FMN5bXCw%2FWH1rrq09mhVRAPg%2FHGiDYwizZJESBk06ZksNs34aCzGURo7uoe9SxkTYZgQW2bkyEoLGdzUAWwc3WVFf7BFUG0k0jL7YkcyEpTCmLCkaXRGEHnqpo%2FweQGWjT8O%2Bmv23NeCKUb7%2F0gceGXOGyaOaVpaz9gu0SnUYYZg%2B9XQPx0gKYE2PvQ2Jc%2FdtGGudTqzQPzsIWeXNaA4t7LcasXreOB17nbARlgX8CcShloCOMn4j2X6CU7atcA1mP7mhiL5s1HCH%2FlBFxuR1KYnqvP3VOqXJmca5PtxfNVU98dE9xUxrXIsGaAw37bsybHybiPsuHLvVqMGdkjdywHKqIFAiMIKx%2BrwGOqUBOEZGVGF3aq1LkoJ66mBGtgrWuGU0kOD1OW4YM3vqAAh6EFFLnNbzPDTams46t%2FGOXLbuZ22UdIT9vJsAfRaiRuMMClvgBz6wMhUt4RFhl5CAYNMgKe7AtTYnDokUAhORvsSlQ3y3Xr0jb7EXD0xjsEnS%2FtYtf4JIJ2vc14DXWsfIojZ5YzhEpLiOcrc22QDrAISCxgzv8qO6LNbJ%2BWpGn6sJjhrt&X-Amz-Signature=bf15f24edfd2845438f34ca85ec9e157cb9ff817dae296b2cd4a12a1456b246f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UPHU3ZT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEe14%2Bc1y9lSRoYbBQyNbaDzo1S9anY8duX3NePzWjMoAiEAy1pyIrIlqDaF7JpsUTCBCHaYbxwxRqk06yfk2BTvaxUqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBex0OFLjJK6GnbBdircAxUyi5WFYhzn1BiAzhL78vE2p2tKNr3fcsp51cnkrX%2BXeYZKSRPWsh94%2FYyyumpH%2BmQPJseg6Ay8fblIq4co5SeNeMpniCZlR0%2B5AXf0lhTGR9hbaYiSpQd%2FRO%2BiIf%2B1DGLfkPipLBigQ2Tym4f5%2FCzyeElkhPEsc1sW11G1COet%2FUXm95ib9vyMFxat7R4owO53eeYln2wyHvUyMUCUki98eXcLzq%2F6Unu3E%2B%2BNEYvLJzdfxhX0MhIhGYfo79TOWb0%2BbTudtXpH7gFfMeNZVevnfOSxqAY%2FMN5bXCw%2FWH1rrq09mhVRAPg%2FHGiDYwizZJESBk06ZksNs34aCzGURo7uoe9SxkTYZgQW2bkyEoLGdzUAWwc3WVFf7BFUG0k0jL7YkcyEpTCmLCkaXRGEHnqpo%2FweQGWjT8O%2Bmv23NeCKUb7%2F0gceGXOGyaOaVpaz9gu0SnUYYZg%2B9XQPx0gKYE2PvQ2Jc%2FdtGGudTqzQPzsIWeXNaA4t7LcasXreOB17nbARlgX8CcShloCOMn4j2X6CU7atcA1mP7mhiL5s1HCH%2FlBFxuR1KYnqvP3VOqXJmca5PtxfNVU98dE9xUxrXIsGaAw37bsybHybiPsuHLvVqMGdkjdywHKqIFAiMIKx%2BrwGOqUBOEZGVGF3aq1LkoJ66mBGtgrWuGU0kOD1OW4YM3vqAAh6EFFLnNbzPDTams46t%2FGOXLbuZ22UdIT9vJsAfRaiRuMMClvgBz6wMhUt4RFhl5CAYNMgKe7AtTYnDokUAhORvsSlQ3y3Xr0jb7EXD0xjsEnS%2FtYtf4JIJ2vc14DXWsfIojZ5YzhEpLiOcrc22QDrAISCxgzv8qO6LNbJ%2BWpGn6sJjhrt&X-Amz-Signature=2bcaf5094aed933057cce53e3fbd5a195e2a917a303e534c5c3dfe799fa9a068&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4RXLOE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEhYnFYysoaVJ1QWKUZL1842m0nn5UjDnLVEP5vRiymQIhALR2tqdt%2BGzVn9HTBJ8miE442AWZb7ufO4RdHrtL8fRBKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQ8brbrgI6KpfRx8sq3APs1OffjWSKyrOJ4XSTNJgYzcqGekcNtOXrgk55wcUl9hxZNOIcmD1%2FbfCgI%2F1KjB5mSzzA4v%2BoqHn90Uug5FyhBOV6VQebr0vwAydNSWGqINfKiCqzbRerheHz%2FGpKrrgWr3j%2FBjjzV7kNlSf%2Bo9GlpOxhvlWU%2FDeK480U9KY%2BePpukCViadD0iitKLJnod0rRIkj7UvSwMiALUB4hh51GgO5FzVER0fg%2FrPxyAEIpGZXoBa%2FTwxGX5%2F90dLK5Pa5fezFGF7eHWYsvgGXy2PB1JX8nFPCOCAr4Z%2BXobS1ydhAKk3fkxNIaT%2FjY26tb63S8QlvxziAgAkpRNOyzA1L1rsyYCqk0wFhv6z%2FoKMzgx%2Fz1KBUyEMY3KeOiNTZYeo0Z2wZzGrNZgGMMBaFH4nVM6mXmW8IOoXeIAOLlfIcJN5EGrBEw3wLUY3Fpj2m5B3UCffkyAtukiubxH74xlD2wztdJo6Q142r3pmaZhZBHXiZYpplBDwaok%2BA4HlhNYoLrYoTVAnb6lzk9LdRtJezZJjlGMzYTUXXdWNddlNoWLMKauBiI9vM5ODOgFiMqgLzIva577EksLUZ68P8%2Fpqy0osM4v12fdJui4tM6qU2p41aD1XLc33QWIsMa6DCVsfq8BjqkAVlPDWBGxz%2FKppH38qaIq%2BRv144aRq4D1O3%2B%2FafbkcE%2FCsgKW5vh%2BXLAwevd4wmlmqbf02eKw4ROQxC%2Fz%2F7jZWQTf0bdSl%2FXmkbmX4VJ3cCZ%2FSeEL142ZPpsyYwQsEyQhM%2Fk9Y8YjOmBjJtXt%2Bo39VFS2s6qo3H38QYD6sSpf%2BzI1Gxv8OZ49M9xSmhn9idpGpoxToyZPXy%2FN2M47jpoT3PEHyK6&X-Amz-Signature=6218cd642f92063ac4da3fc4f3f2a27ea487dda828b3fd0dbd8d38c0ea6b0ec2&X-Amz-SignedHeaders=host&x-id=GetObject)
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