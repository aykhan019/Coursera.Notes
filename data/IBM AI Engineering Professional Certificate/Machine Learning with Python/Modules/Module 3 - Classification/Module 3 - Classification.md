

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPX2UAWN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAdluXtJLfKjOFMXmTBzL1jncHAzSa6VMaGME4uokuhnAiEA1b9sDnUokS8Nx0b9f6GQoX7jr1VDnmaIxMbUBneIB4gq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDGWcaGqw1u3LgLIgoCrcAyV%2FZh2aeWcBIq8yIAz1q9fK39KtAT9OEoSWfm%2BMM3ooOQmQ6mPJSKcr%2BNchLbG%2F7lQiEgdGwwaVVDKILJLe3jUlXn1ZSjx8I9bqoAfuqlJi%2Bx%2FCiA8JbPfAwSFjHiuDDAm5gvBPWl%2FXToNYCJV3FG4t4WincUhMF2h243Es20BLipUNuMz%2FeWqYXkoDe13UO2CG9guJekMWxQYvQ5z4nN9LBSR5wiwF%2Bix%2FnyYhc4M%2FUzUlbi99grACi7MrzkAs5jGVQy6ZZdBge7upaYH3lot8oEy2Vjk6WSr9xmEY%2F9YRwtc6yRigollzTNciPDQa7TI2MUsGuzq17oi9CW6qIVthYMNVs8W%2FbpTiYKjCwbN8flkvXMZHCwsc21FSAsn6T4Ar7C%2BN8%2BgUthSlWAeXxRjCRnqh7aPRZ9rnXmJUm%2BIDw1erqKVAEMkx5teV22EQAxMzS4EQ18DcI79aBZ8DKsAv3Dk%2BkcsSl8PuNZlAyznsqOzQVjqDXMQqXEe%2FbxPJ1lKoDbYPVGvPkghTS00zOindXkjIfokz4cHpgMaPxzpq5BibEJ8U82CjbwsXVdcpqCZI%2Bl6vQosfVTL81tjX9mMOiCc4BbVVtCcA5giETnp9hnKoXsM0DY18vMESMKzWgb0GOqUB71zxtlMgkaOAiuDzQ1euXRlKUuhVSM7zS0HAgiKKPKHvelS71wHTICRJ41uiCelgoIVeymmVLciytw3rzZLixoEnEp6haiQEd5JBHqagcrkqzsQgiSqLzsVhAVUJoRMwA3ozCf1kVbfCecWPK91Jx72PK23NvnyUdpfjxXqXvRedJ7rx4mFt1sbq8Y%2BURehuqSrRcjQDBUUVqe1Cz6oqxbrTa3ry&X-Amz-Signature=f7dec45a7bff75c1bc509252c297e87bcdec17805272e45fcc50eb5bad862851&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPX2UAWN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAdluXtJLfKjOFMXmTBzL1jncHAzSa6VMaGME4uokuhnAiEA1b9sDnUokS8Nx0b9f6GQoX7jr1VDnmaIxMbUBneIB4gq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDGWcaGqw1u3LgLIgoCrcAyV%2FZh2aeWcBIq8yIAz1q9fK39KtAT9OEoSWfm%2BMM3ooOQmQ6mPJSKcr%2BNchLbG%2F7lQiEgdGwwaVVDKILJLe3jUlXn1ZSjx8I9bqoAfuqlJi%2Bx%2FCiA8JbPfAwSFjHiuDDAm5gvBPWl%2FXToNYCJV3FG4t4WincUhMF2h243Es20BLipUNuMz%2FeWqYXkoDe13UO2CG9guJekMWxQYvQ5z4nN9LBSR5wiwF%2Bix%2FnyYhc4M%2FUzUlbi99grACi7MrzkAs5jGVQy6ZZdBge7upaYH3lot8oEy2Vjk6WSr9xmEY%2F9YRwtc6yRigollzTNciPDQa7TI2MUsGuzq17oi9CW6qIVthYMNVs8W%2FbpTiYKjCwbN8flkvXMZHCwsc21FSAsn6T4Ar7C%2BN8%2BgUthSlWAeXxRjCRnqh7aPRZ9rnXmJUm%2BIDw1erqKVAEMkx5teV22EQAxMzS4EQ18DcI79aBZ8DKsAv3Dk%2BkcsSl8PuNZlAyznsqOzQVjqDXMQqXEe%2FbxPJ1lKoDbYPVGvPkghTS00zOindXkjIfokz4cHpgMaPxzpq5BibEJ8U82CjbwsXVdcpqCZI%2Bl6vQosfVTL81tjX9mMOiCc4BbVVtCcA5giETnp9hnKoXsM0DY18vMESMKzWgb0GOqUB71zxtlMgkaOAiuDzQ1euXRlKUuhVSM7zS0HAgiKKPKHvelS71wHTICRJ41uiCelgoIVeymmVLciytw3rzZLixoEnEp6haiQEd5JBHqagcrkqzsQgiSqLzsVhAVUJoRMwA3ozCf1kVbfCecWPK91Jx72PK23NvnyUdpfjxXqXvRedJ7rx4mFt1sbq8Y%2BURehuqSrRcjQDBUUVqe1Cz6oqxbrTa3ry&X-Amz-Signature=764b34569837ba66514d15b6b8913c827a5da9108a92a25acfa899dc3e74d7d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPX2UAWN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAdluXtJLfKjOFMXmTBzL1jncHAzSa6VMaGME4uokuhnAiEA1b9sDnUokS8Nx0b9f6GQoX7jr1VDnmaIxMbUBneIB4gq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDGWcaGqw1u3LgLIgoCrcAyV%2FZh2aeWcBIq8yIAz1q9fK39KtAT9OEoSWfm%2BMM3ooOQmQ6mPJSKcr%2BNchLbG%2F7lQiEgdGwwaVVDKILJLe3jUlXn1ZSjx8I9bqoAfuqlJi%2Bx%2FCiA8JbPfAwSFjHiuDDAm5gvBPWl%2FXToNYCJV3FG4t4WincUhMF2h243Es20BLipUNuMz%2FeWqYXkoDe13UO2CG9guJekMWxQYvQ5z4nN9LBSR5wiwF%2Bix%2FnyYhc4M%2FUzUlbi99grACi7MrzkAs5jGVQy6ZZdBge7upaYH3lot8oEy2Vjk6WSr9xmEY%2F9YRwtc6yRigollzTNciPDQa7TI2MUsGuzq17oi9CW6qIVthYMNVs8W%2FbpTiYKjCwbN8flkvXMZHCwsc21FSAsn6T4Ar7C%2BN8%2BgUthSlWAeXxRjCRnqh7aPRZ9rnXmJUm%2BIDw1erqKVAEMkx5teV22EQAxMzS4EQ18DcI79aBZ8DKsAv3Dk%2BkcsSl8PuNZlAyznsqOzQVjqDXMQqXEe%2FbxPJ1lKoDbYPVGvPkghTS00zOindXkjIfokz4cHpgMaPxzpq5BibEJ8U82CjbwsXVdcpqCZI%2Bl6vQosfVTL81tjX9mMOiCc4BbVVtCcA5giETnp9hnKoXsM0DY18vMESMKzWgb0GOqUB71zxtlMgkaOAiuDzQ1euXRlKUuhVSM7zS0HAgiKKPKHvelS71wHTICRJ41uiCelgoIVeymmVLciytw3rzZLixoEnEp6haiQEd5JBHqagcrkqzsQgiSqLzsVhAVUJoRMwA3ozCf1kVbfCecWPK91Jx72PK23NvnyUdpfjxXqXvRedJ7rx4mFt1sbq8Y%2BURehuqSrRcjQDBUUVqe1Cz6oqxbrTa3ry&X-Amz-Signature=8e113c55df99768e6e4d84004b09c864494b6529afcc1ef160058940a78f20d2&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5BPFH63%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPvvofiSsflglq%2B%2FFs6HsZfY89e5%2BPLLyz3clJY6dDWAiEA4ZFBNSo7%2FPhzVxVUDD9zLPIoxGlluD2jBSWFtrAhAAgq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDItIgHVnEkoPF5vQPircA0mFCEuVR2CMY4iQ8%2BPUtxl45rXH7fDRDAdmR%2BtQjh%2F9g6phL5MF8oSpvoFg0WqoHYriwN6HSoSlojiRn4%2FM%2BrfoEn2sQUeSbVfuj5lMr3WTrqV%2FO7HByoOd1WgXgTAhJXysuE79qV%2BIcWnmpLm5YozTz%2FdlLodwhFk9SVGEitZdtknNL1pIQ%2FVqaz0%2BAX87wMLjDCIcEyuw%2FeM%2FONXOUjCm%2FDlkJ46xBxfVd%2FjHHif82APZbV23JqZA7jHVUKjMiwa2bCi8NY7hJAemUT4qyvHdgWoW7iC%2B649hJnxitPJ3LlIDiYM2cRKhuqnya4cRW43FactjVL9N0Jl0WR%2BJhI9WjlGm6VIuSIPu3v9v8UemYAWh6MH9rV4c9T83%2FI8BYBmf%2FyMvfERSGTiQFHs8Ft8532vJ7rF375DuKTyPWle3T7A8yhWr%2F4XGUgxnNTp3%2F7TZYZ9lTGgwQq6Q44GAwxi5MobcChy3sP7%2BfvZ1NO1tfUTplYN%2FWVAbvgPhYxyLCdgTnaOTsSqWKaG2Z7ra0dZ23Gp2PvqRpnUHq9wUDv8FvKFHMdRpiypZuCH4bhHMDx2pWxzJXpehKZVAvUe7XeIOuMVb6r9YDaVW8j0tWyiLPG57nylM26YAz9tqMPnVgb0GOqUBJ%2BNjHGvW7fBUVpviYMiqPHIGBH5WzcZdvRdK%2FrOqiSVfSIVgiY7D1T%2BvdbroKLf5L5dz5TMGfzPJ9HWBuQjOw3uQZNL9qbJc7xwx0MxpHIRjG2vd6sA7AvHQdOTpMN%2FctyzBtJudg%2FlWXjXaZi9A7NH%2Bpl0IiGMN1%2Fw2emdehXlkZRhkJgYgee9j7auaQy1KiODKf07tbHaAKcCKUPB43Uv4IVIN&X-Amz-Signature=cfec53163a87a5aa8344cda1db69b5764661bed7cc4b319d8be70e5307dace43&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5BPFH63%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPvvofiSsflglq%2B%2FFs6HsZfY89e5%2BPLLyz3clJY6dDWAiEA4ZFBNSo7%2FPhzVxVUDD9zLPIoxGlluD2jBSWFtrAhAAgq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDItIgHVnEkoPF5vQPircA0mFCEuVR2CMY4iQ8%2BPUtxl45rXH7fDRDAdmR%2BtQjh%2F9g6phL5MF8oSpvoFg0WqoHYriwN6HSoSlojiRn4%2FM%2BrfoEn2sQUeSbVfuj5lMr3WTrqV%2FO7HByoOd1WgXgTAhJXysuE79qV%2BIcWnmpLm5YozTz%2FdlLodwhFk9SVGEitZdtknNL1pIQ%2FVqaz0%2BAX87wMLjDCIcEyuw%2FeM%2FONXOUjCm%2FDlkJ46xBxfVd%2FjHHif82APZbV23JqZA7jHVUKjMiwa2bCi8NY7hJAemUT4qyvHdgWoW7iC%2B649hJnxitPJ3LlIDiYM2cRKhuqnya4cRW43FactjVL9N0Jl0WR%2BJhI9WjlGm6VIuSIPu3v9v8UemYAWh6MH9rV4c9T83%2FI8BYBmf%2FyMvfERSGTiQFHs8Ft8532vJ7rF375DuKTyPWle3T7A8yhWr%2F4XGUgxnNTp3%2F7TZYZ9lTGgwQq6Q44GAwxi5MobcChy3sP7%2BfvZ1NO1tfUTplYN%2FWVAbvgPhYxyLCdgTnaOTsSqWKaG2Z7ra0dZ23Gp2PvqRpnUHq9wUDv8FvKFHMdRpiypZuCH4bhHMDx2pWxzJXpehKZVAvUe7XeIOuMVb6r9YDaVW8j0tWyiLPG57nylM26YAz9tqMPnVgb0GOqUBJ%2BNjHGvW7fBUVpviYMiqPHIGBH5WzcZdvRdK%2FrOqiSVfSIVgiY7D1T%2BvdbroKLf5L5dz5TMGfzPJ9HWBuQjOw3uQZNL9qbJc7xwx0MxpHIRjG2vd6sA7AvHQdOTpMN%2FctyzBtJudg%2FlWXjXaZi9A7NH%2Bpl0IiGMN1%2Fw2emdehXlkZRhkJgYgee9j7auaQy1KiODKf07tbHaAKcCKUPB43Uv4IVIN&X-Amz-Signature=8ba7bdbdb10d229bb6e456447f738f830cc11e17049fe00ff11fe2d1531cb825&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPX2UAWN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAdluXtJLfKjOFMXmTBzL1jncHAzSa6VMaGME4uokuhnAiEA1b9sDnUokS8Nx0b9f6GQoX7jr1VDnmaIxMbUBneIB4gq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDGWcaGqw1u3LgLIgoCrcAyV%2FZh2aeWcBIq8yIAz1q9fK39KtAT9OEoSWfm%2BMM3ooOQmQ6mPJSKcr%2BNchLbG%2F7lQiEgdGwwaVVDKILJLe3jUlXn1ZSjx8I9bqoAfuqlJi%2Bx%2FCiA8JbPfAwSFjHiuDDAm5gvBPWl%2FXToNYCJV3FG4t4WincUhMF2h243Es20BLipUNuMz%2FeWqYXkoDe13UO2CG9guJekMWxQYvQ5z4nN9LBSR5wiwF%2Bix%2FnyYhc4M%2FUzUlbi99grACi7MrzkAs5jGVQy6ZZdBge7upaYH3lot8oEy2Vjk6WSr9xmEY%2F9YRwtc6yRigollzTNciPDQa7TI2MUsGuzq17oi9CW6qIVthYMNVs8W%2FbpTiYKjCwbN8flkvXMZHCwsc21FSAsn6T4Ar7C%2BN8%2BgUthSlWAeXxRjCRnqh7aPRZ9rnXmJUm%2BIDw1erqKVAEMkx5teV22EQAxMzS4EQ18DcI79aBZ8DKsAv3Dk%2BkcsSl8PuNZlAyznsqOzQVjqDXMQqXEe%2FbxPJ1lKoDbYPVGvPkghTS00zOindXkjIfokz4cHpgMaPxzpq5BibEJ8U82CjbwsXVdcpqCZI%2Bl6vQosfVTL81tjX9mMOiCc4BbVVtCcA5giETnp9hnKoXsM0DY18vMESMKzWgb0GOqUB71zxtlMgkaOAiuDzQ1euXRlKUuhVSM7zS0HAgiKKPKHvelS71wHTICRJ41uiCelgoIVeymmVLciytw3rzZLixoEnEp6haiQEd5JBHqagcrkqzsQgiSqLzsVhAVUJoRMwA3ozCf1kVbfCecWPK91Jx72PK23NvnyUdpfjxXqXvRedJ7rx4mFt1sbq8Y%2BURehuqSrRcjQDBUUVqe1Cz6oqxbrTa3ry&X-Amz-Signature=dc0865dfa8db093c15daa749f8e0cdcb6e97a3ab0825812fd1adcdd10def2c8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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