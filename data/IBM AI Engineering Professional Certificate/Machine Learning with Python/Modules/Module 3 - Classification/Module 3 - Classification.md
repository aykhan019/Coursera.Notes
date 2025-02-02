

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ6MQBSO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6vR2gaa%2FOoUsaS6%2FBHIUB4VFfZ2o54TCUX2hLVqQO8gIgRapWhTIv3y5kka9MKb6tlH46Bt9C1%2FqxkabxGWHj04oqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAAPaRqGnX6gpNJ0vCrcAyZDOgcxatHVLAmtdp5R7%2BxqlJ3PZ5wCKCc0d4CgUvCpX8XFR5%2Be9tRC4arb%2FaG80Je7l9GyG0F%2Bk%2B0J5q0SOObYyEdblT7k%2F1KKncusPHude1UrQZuT9QAOWn84IlIBJ6PcHjLIRqCLaPbtrcxRyIo0qnJs8JxIg3NRslyBWjGs89PA0l3NTphB87%2FyRAL6ToQWDdBf7nq6FGJUoaRSa5WibMbqJyj%2B94UCZ9PfjpC8%2BfQ%2B4wjIPYvxqqNqyh%2FR372%2FTl5A55v9er8MwimxGbfh9aoWKgeWnSB99tk9oJ5C%2BLZrxqBH67iOdjbighnp%2BoGSRDCOnfnHRyh%2BhN%2FUHrnvpujw%2Ba%2BhrbBr%2Fyz6hYiY2n%2FVxglDxK48CWqYdYsbQIdggF4rsSFDF%2FO0vljHYx%2FlABud6e%2B%2B1VxcEKD79H%2BJsdfuG6i5hqpQtGSoLNhn0eNq6Atriv%2Bqf%2Fti59uxlAR5jKLWXxWPpfloY2DYLtHuSb6WsX4JVOQZgv7Uaxb0UQOKWDaHAE9IwIU80bA7LEhpjNoclnGDjoXkMxWzfz3%2FvG0jjXGa0zIhw9vekuTfReIMwMCVzrzD4%2B6bnWsF9R5ueZvgScKlBRB4jiTPwtBGadTkJC894o%2Fcs7YMMJe7%2B7wGOqUBuzIXkJqXZ%2BYlQKlaMlTVNCz3yhs6tA%2FeynAw9L6QXLHzRXzpIX9jdJP6gzvnrHRu9qhuiMY72nD9iC0sVKxvg6xmPEFaf2Uw8zbRPVIErwpEtaeM%2Be1YCEJIvlgVzlEfhI6QZyAHp0hokCJ6bJIXHee4j6g89G7iF2PW%2FYXUspSJF67C3ewKbzQgyUcQAmLWDXZ5PiGsHqKSGjGirsaKW1Pp%2BAZd&X-Amz-Signature=e5441a24c5b6cb38aa143be719523498ad2a5ee8d1369e35dcf292e0ca22b126&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ6MQBSO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6vR2gaa%2FOoUsaS6%2FBHIUB4VFfZ2o54TCUX2hLVqQO8gIgRapWhTIv3y5kka9MKb6tlH46Bt9C1%2FqxkabxGWHj04oqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAAPaRqGnX6gpNJ0vCrcAyZDOgcxatHVLAmtdp5R7%2BxqlJ3PZ5wCKCc0d4CgUvCpX8XFR5%2Be9tRC4arb%2FaG80Je7l9GyG0F%2Bk%2B0J5q0SOObYyEdblT7k%2F1KKncusPHude1UrQZuT9QAOWn84IlIBJ6PcHjLIRqCLaPbtrcxRyIo0qnJs8JxIg3NRslyBWjGs89PA0l3NTphB87%2FyRAL6ToQWDdBf7nq6FGJUoaRSa5WibMbqJyj%2B94UCZ9PfjpC8%2BfQ%2B4wjIPYvxqqNqyh%2FR372%2FTl5A55v9er8MwimxGbfh9aoWKgeWnSB99tk9oJ5C%2BLZrxqBH67iOdjbighnp%2BoGSRDCOnfnHRyh%2BhN%2FUHrnvpujw%2Ba%2BhrbBr%2Fyz6hYiY2n%2FVxglDxK48CWqYdYsbQIdggF4rsSFDF%2FO0vljHYx%2FlABud6e%2B%2B1VxcEKD79H%2BJsdfuG6i5hqpQtGSoLNhn0eNq6Atriv%2Bqf%2Fti59uxlAR5jKLWXxWPpfloY2DYLtHuSb6WsX4JVOQZgv7Uaxb0UQOKWDaHAE9IwIU80bA7LEhpjNoclnGDjoXkMxWzfz3%2FvG0jjXGa0zIhw9vekuTfReIMwMCVzrzD4%2B6bnWsF9R5ueZvgScKlBRB4jiTPwtBGadTkJC894o%2Fcs7YMMJe7%2B7wGOqUBuzIXkJqXZ%2BYlQKlaMlTVNCz3yhs6tA%2FeynAw9L6QXLHzRXzpIX9jdJP6gzvnrHRu9qhuiMY72nD9iC0sVKxvg6xmPEFaf2Uw8zbRPVIErwpEtaeM%2Be1YCEJIvlgVzlEfhI6QZyAHp0hokCJ6bJIXHee4j6g89G7iF2PW%2FYXUspSJF67C3ewKbzQgyUcQAmLWDXZ5PiGsHqKSGjGirsaKW1Pp%2BAZd&X-Amz-Signature=f5e8224be8165d906d2b1046527b873e3956d99779c5e14e2b57ffc7436a4e78&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ6MQBSO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6vR2gaa%2FOoUsaS6%2FBHIUB4VFfZ2o54TCUX2hLVqQO8gIgRapWhTIv3y5kka9MKb6tlH46Bt9C1%2FqxkabxGWHj04oqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAAPaRqGnX6gpNJ0vCrcAyZDOgcxatHVLAmtdp5R7%2BxqlJ3PZ5wCKCc0d4CgUvCpX8XFR5%2Be9tRC4arb%2FaG80Je7l9GyG0F%2Bk%2B0J5q0SOObYyEdblT7k%2F1KKncusPHude1UrQZuT9QAOWn84IlIBJ6PcHjLIRqCLaPbtrcxRyIo0qnJs8JxIg3NRslyBWjGs89PA0l3NTphB87%2FyRAL6ToQWDdBf7nq6FGJUoaRSa5WibMbqJyj%2B94UCZ9PfjpC8%2BfQ%2B4wjIPYvxqqNqyh%2FR372%2FTl5A55v9er8MwimxGbfh9aoWKgeWnSB99tk9oJ5C%2BLZrxqBH67iOdjbighnp%2BoGSRDCOnfnHRyh%2BhN%2FUHrnvpujw%2Ba%2BhrbBr%2Fyz6hYiY2n%2FVxglDxK48CWqYdYsbQIdggF4rsSFDF%2FO0vljHYx%2FlABud6e%2B%2B1VxcEKD79H%2BJsdfuG6i5hqpQtGSoLNhn0eNq6Atriv%2Bqf%2Fti59uxlAR5jKLWXxWPpfloY2DYLtHuSb6WsX4JVOQZgv7Uaxb0UQOKWDaHAE9IwIU80bA7LEhpjNoclnGDjoXkMxWzfz3%2FvG0jjXGa0zIhw9vekuTfReIMwMCVzrzD4%2B6bnWsF9R5ueZvgScKlBRB4jiTPwtBGadTkJC894o%2Fcs7YMMJe7%2B7wGOqUBuzIXkJqXZ%2BYlQKlaMlTVNCz3yhs6tA%2FeynAw9L6QXLHzRXzpIX9jdJP6gzvnrHRu9qhuiMY72nD9iC0sVKxvg6xmPEFaf2Uw8zbRPVIErwpEtaeM%2Be1YCEJIvlgVzlEfhI6QZyAHp0hokCJ6bJIXHee4j6g89G7iF2PW%2FYXUspSJF67C3ewKbzQgyUcQAmLWDXZ5PiGsHqKSGjGirsaKW1Pp%2BAZd&X-Amz-Signature=01089d5d174675a1f15844a1c375a6ec259fa8a3c1a84a62a00ee8e21e96af2f&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655KMNQS5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4L%2FSHAUYZ%2BIBAUv027tarMek6%2BGj00EFsHfTsaPr96QIhAIS9nW8e5IoucmVC3oziWLJ3aWOuiJpqluc4WMw7yBRBKogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz3t%2B7z4qMdxSz4W0q3AMu8PYBOILNG8C6E6ypTEIsPFX2%2FEOvttPtCe%2B6WftwFl%2B0g6vgJEJNuKAXnlIKGj8g7yD7MQrABi%2BX7355h%2FyVFrtbluPx2hbKidyQ75NbqRY6B8EU4uVa5sDk0mgHsHykl954flSeq3nZ6bRWOqmWudp%2FIsHszF4ilAd7V%2FhMb6P6EUHDK8NRlNjf3NS%2BYpKW9fk1BRgoux2GKmy3nC8N%2BR%2Btgd5UNxghGGBc6s9VhdMp9UtnXdbXuMDCMLkE%2F6t2ZiuO0ucK3F28E%2FZk4mQqRtaESiHY7hH17SdbUAIUo5C79RHfUdTvx%2BydvaZaO7poKXgPcFVbdU3n5X1vKIyHmeLiWCd24gQ48AusdB%2FzVmeh%2BEqSU0J3hKNh8DFb6mwFarp7cXf4GPIyVI94XdTCTBHs%2BU%2BpyBaZqpgzvGAAFq%2BobfcZb%2FC%2FIqdBnnEVAkslCFLNuZJoQqtS8vzXdv0%2BQWCosyyATSyBdTqjs3ctyOMFXp6pjTmlTvA5RwwZh9E12NAzZsT%2FjvComs3SOCBc4j4WI73S5bg1%2FU9xlFj13qJHLdqJuEGs4qdUQohtte1HoLdNzcuVTTkq1ci2O5Ju83iVVwLrQPUNXRdcsbU%2BGYj5me0UmNegpRHQLzC3u%2Fu8BjqkAWLS9bBfz5JuZETMejFZVIAh5hu8kuJqY5iP97NzulYxZqqpJIwLcf5XAbBnnAK1B%2FH5aXv%2BsVCTXblFurXEZmEPhmsbG4emfMaMDT2wAKJIY3hWMpQt2uRD2o3n8QP6REzjPZpj7TUmRfjN8eIvqtFHW7nPDhpWrlzYiG9p1qdm5bjnKkKUDpeSp7GkPNtWM584BRDaLTxDSB5DvWewo%2FOnh9y%2F&X-Amz-Signature=fdf36215decd1c9cbca087b6b9219071725f0f5be20854491fb3dcb871ff29e5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655KMNQS5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4L%2FSHAUYZ%2BIBAUv027tarMek6%2BGj00EFsHfTsaPr96QIhAIS9nW8e5IoucmVC3oziWLJ3aWOuiJpqluc4WMw7yBRBKogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzz3t%2B7z4qMdxSz4W0q3AMu8PYBOILNG8C6E6ypTEIsPFX2%2FEOvttPtCe%2B6WftwFl%2B0g6vgJEJNuKAXnlIKGj8g7yD7MQrABi%2BX7355h%2FyVFrtbluPx2hbKidyQ75NbqRY6B8EU4uVa5sDk0mgHsHykl954flSeq3nZ6bRWOqmWudp%2FIsHszF4ilAd7V%2FhMb6P6EUHDK8NRlNjf3NS%2BYpKW9fk1BRgoux2GKmy3nC8N%2BR%2Btgd5UNxghGGBc6s9VhdMp9UtnXdbXuMDCMLkE%2F6t2ZiuO0ucK3F28E%2FZk4mQqRtaESiHY7hH17SdbUAIUo5C79RHfUdTvx%2BydvaZaO7poKXgPcFVbdU3n5X1vKIyHmeLiWCd24gQ48AusdB%2FzVmeh%2BEqSU0J3hKNh8DFb6mwFarp7cXf4GPIyVI94XdTCTBHs%2BU%2BpyBaZqpgzvGAAFq%2BobfcZb%2FC%2FIqdBnnEVAkslCFLNuZJoQqtS8vzXdv0%2BQWCosyyATSyBdTqjs3ctyOMFXp6pjTmlTvA5RwwZh9E12NAzZsT%2FjvComs3SOCBc4j4WI73S5bg1%2FU9xlFj13qJHLdqJuEGs4qdUQohtte1HoLdNzcuVTTkq1ci2O5Ju83iVVwLrQPUNXRdcsbU%2BGYj5me0UmNegpRHQLzC3u%2Fu8BjqkAWLS9bBfz5JuZETMejFZVIAh5hu8kuJqY5iP97NzulYxZqqpJIwLcf5XAbBnnAK1B%2FH5aXv%2BsVCTXblFurXEZmEPhmsbG4emfMaMDT2wAKJIY3hWMpQt2uRD2o3n8QP6REzjPZpj7TUmRfjN8eIvqtFHW7nPDhpWrlzYiG9p1qdm5bjnKkKUDpeSp7GkPNtWM584BRDaLTxDSB5DvWewo%2FOnh9y%2F&X-Amz-Signature=f0ac0e15d763d39817080ed88da20dde351ed65a0edf3973344ee15c29254ddb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ6MQBSO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6vR2gaa%2FOoUsaS6%2FBHIUB4VFfZ2o54TCUX2hLVqQO8gIgRapWhTIv3y5kka9MKb6tlH46Bt9C1%2FqxkabxGWHj04oqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAAPaRqGnX6gpNJ0vCrcAyZDOgcxatHVLAmtdp5R7%2BxqlJ3PZ5wCKCc0d4CgUvCpX8XFR5%2Be9tRC4arb%2FaG80Je7l9GyG0F%2Bk%2B0J5q0SOObYyEdblT7k%2F1KKncusPHude1UrQZuT9QAOWn84IlIBJ6PcHjLIRqCLaPbtrcxRyIo0qnJs8JxIg3NRslyBWjGs89PA0l3NTphB87%2FyRAL6ToQWDdBf7nq6FGJUoaRSa5WibMbqJyj%2B94UCZ9PfjpC8%2BfQ%2B4wjIPYvxqqNqyh%2FR372%2FTl5A55v9er8MwimxGbfh9aoWKgeWnSB99tk9oJ5C%2BLZrxqBH67iOdjbighnp%2BoGSRDCOnfnHRyh%2BhN%2FUHrnvpujw%2Ba%2BhrbBr%2Fyz6hYiY2n%2FVxglDxK48CWqYdYsbQIdggF4rsSFDF%2FO0vljHYx%2FlABud6e%2B%2B1VxcEKD79H%2BJsdfuG6i5hqpQtGSoLNhn0eNq6Atriv%2Bqf%2Fti59uxlAR5jKLWXxWPpfloY2DYLtHuSb6WsX4JVOQZgv7Uaxb0UQOKWDaHAE9IwIU80bA7LEhpjNoclnGDjoXkMxWzfz3%2FvG0jjXGa0zIhw9vekuTfReIMwMCVzrzD4%2B6bnWsF9R5ueZvgScKlBRB4jiTPwtBGadTkJC894o%2Fcs7YMMJe7%2B7wGOqUBuzIXkJqXZ%2BYlQKlaMlTVNCz3yhs6tA%2FeynAw9L6QXLHzRXzpIX9jdJP6gzvnrHRu9qhuiMY72nD9iC0sVKxvg6xmPEFaf2Uw8zbRPVIErwpEtaeM%2Be1YCEJIvlgVzlEfhI6QZyAHp0hokCJ6bJIXHee4j6g89G7iF2PW%2FYXUspSJF67C3ewKbzQgyUcQAmLWDXZ5PiGsHqKSGjGirsaKW1Pp%2BAZd&X-Amz-Signature=3541ee54ad97fd1fdea6a415ad659e80d0dd1896fce417ca1109987e560c4f7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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