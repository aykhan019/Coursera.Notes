

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBDO2DMY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdIR6yxCinrQ2DKGRjdqUdjasFAqMk2HhMBafYe3lAfwIgPNp77GGHU6Y%2FZRw2r7pp6VmaBMsVeWiqZVWGUqQkMqYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDPG%2Bw0wFCyJljKn8nSrcA6Pl72Ov%2FdJKWzqqD1YGIoJLAx7cIbGo5nN%2FM8GptM%2BDRzoGRkIe9QtfL4UUy8ZnXCHFIoQq8Diiu8LWVE7cGRANvP4%2FDxiQDs07LAuYeCqJMq9WUDxQ72uAObOvDbcdwom3dd9DhtGhC3Mb%2FncLANdfdv2mAW2lZuAnQCWqwsdHYdcoV3sb43KwIDWbJJBnwQ4BTun9ckvGjSdBYN9ugSJ8FcrgUYGm3YTedyIN%2Bfdqd9dsbqRCUR2e2ZqF5xoTXGvR%2BTqVzVqIpW7hHkbz2APIDJ%2BC3DSdnZNVoz9TNX8CtEX34TGYudSoH0vsMFD5SdcanzABwdHGnftvVpDMIwuEiwG10udVCXqp%2FJPh8kYPNqSCey8zAa5woHN5vwPMlJxBNSVtXwrTVAHjW1KJvGCpbFccbXEfCmnFWx4ZwUADFUMUkqHlHBsTAo1DqVZUPPP2fUtV9vEmC1TpH3aFD3bWPxsc8h1ennIfA3AcGAOLJWdZsTlGpqn1ojLYJEllhPINjLfFGaRWEgIppJ5mLWB9E1lNKdh3B5ajriCYGIrvEPQzt887%2F%2BU04y9SpvCQNvd5DI5Zt6aQLzQYTaaffzxSDI%2FWmGK4IwCffVDJ7uYwh5IRoCjWT01i0PlaMLbzgb0GOqUBXABR4yZE0spSD4KovvfkBp7MNCWVrrGfZMkuHRcW%2F02ic0ayQO%2BEFRZDqmJAEMXgHCQsJaoBFfiia2OF30P%2Bjh1QN%2B%2BEdxiM2dBd3Kw4G5pulitkTP9xl6%2BQiIPPmh3u5XQVghnu1bBJQTaNYg7jIJ45lEPm65QmBhQn%2FK0SGpX3yWdJ9lqOyXUICq2lNvD5P5laHT%2FbJM%2BB2emhWf69gsuPC39p&X-Amz-Signature=e627c617df979980008274d2b17d27a9dee387b30bed9c37fcfb6f25eff4b48f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBDO2DMY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdIR6yxCinrQ2DKGRjdqUdjasFAqMk2HhMBafYe3lAfwIgPNp77GGHU6Y%2FZRw2r7pp6VmaBMsVeWiqZVWGUqQkMqYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDPG%2Bw0wFCyJljKn8nSrcA6Pl72Ov%2FdJKWzqqD1YGIoJLAx7cIbGo5nN%2FM8GptM%2BDRzoGRkIe9QtfL4UUy8ZnXCHFIoQq8Diiu8LWVE7cGRANvP4%2FDxiQDs07LAuYeCqJMq9WUDxQ72uAObOvDbcdwom3dd9DhtGhC3Mb%2FncLANdfdv2mAW2lZuAnQCWqwsdHYdcoV3sb43KwIDWbJJBnwQ4BTun9ckvGjSdBYN9ugSJ8FcrgUYGm3YTedyIN%2Bfdqd9dsbqRCUR2e2ZqF5xoTXGvR%2BTqVzVqIpW7hHkbz2APIDJ%2BC3DSdnZNVoz9TNX8CtEX34TGYudSoH0vsMFD5SdcanzABwdHGnftvVpDMIwuEiwG10udVCXqp%2FJPh8kYPNqSCey8zAa5woHN5vwPMlJxBNSVtXwrTVAHjW1KJvGCpbFccbXEfCmnFWx4ZwUADFUMUkqHlHBsTAo1DqVZUPPP2fUtV9vEmC1TpH3aFD3bWPxsc8h1ennIfA3AcGAOLJWdZsTlGpqn1ojLYJEllhPINjLfFGaRWEgIppJ5mLWB9E1lNKdh3B5ajriCYGIrvEPQzt887%2F%2BU04y9SpvCQNvd5DI5Zt6aQLzQYTaaffzxSDI%2FWmGK4IwCffVDJ7uYwh5IRoCjWT01i0PlaMLbzgb0GOqUBXABR4yZE0spSD4KovvfkBp7MNCWVrrGfZMkuHRcW%2F02ic0ayQO%2BEFRZDqmJAEMXgHCQsJaoBFfiia2OF30P%2Bjh1QN%2B%2BEdxiM2dBd3Kw4G5pulitkTP9xl6%2BQiIPPmh3u5XQVghnu1bBJQTaNYg7jIJ45lEPm65QmBhQn%2FK0SGpX3yWdJ9lqOyXUICq2lNvD5P5laHT%2FbJM%2BB2emhWf69gsuPC39p&X-Amz-Signature=2ff8385d8b836768f74d0add4b290d3785cbac0e0901380b285885f8f1809c9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBDO2DMY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdIR6yxCinrQ2DKGRjdqUdjasFAqMk2HhMBafYe3lAfwIgPNp77GGHU6Y%2FZRw2r7pp6VmaBMsVeWiqZVWGUqQkMqYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDPG%2Bw0wFCyJljKn8nSrcA6Pl72Ov%2FdJKWzqqD1YGIoJLAx7cIbGo5nN%2FM8GptM%2BDRzoGRkIe9QtfL4UUy8ZnXCHFIoQq8Diiu8LWVE7cGRANvP4%2FDxiQDs07LAuYeCqJMq9WUDxQ72uAObOvDbcdwom3dd9DhtGhC3Mb%2FncLANdfdv2mAW2lZuAnQCWqwsdHYdcoV3sb43KwIDWbJJBnwQ4BTun9ckvGjSdBYN9ugSJ8FcrgUYGm3YTedyIN%2Bfdqd9dsbqRCUR2e2ZqF5xoTXGvR%2BTqVzVqIpW7hHkbz2APIDJ%2BC3DSdnZNVoz9TNX8CtEX34TGYudSoH0vsMFD5SdcanzABwdHGnftvVpDMIwuEiwG10udVCXqp%2FJPh8kYPNqSCey8zAa5woHN5vwPMlJxBNSVtXwrTVAHjW1KJvGCpbFccbXEfCmnFWx4ZwUADFUMUkqHlHBsTAo1DqVZUPPP2fUtV9vEmC1TpH3aFD3bWPxsc8h1ennIfA3AcGAOLJWdZsTlGpqn1ojLYJEllhPINjLfFGaRWEgIppJ5mLWB9E1lNKdh3B5ajriCYGIrvEPQzt887%2F%2BU04y9SpvCQNvd5DI5Zt6aQLzQYTaaffzxSDI%2FWmGK4IwCffVDJ7uYwh5IRoCjWT01i0PlaMLbzgb0GOqUBXABR4yZE0spSD4KovvfkBp7MNCWVrrGfZMkuHRcW%2F02ic0ayQO%2BEFRZDqmJAEMXgHCQsJaoBFfiia2OF30P%2Bjh1QN%2B%2BEdxiM2dBd3Kw4G5pulitkTP9xl6%2BQiIPPmh3u5XQVghnu1bBJQTaNYg7jIJ45lEPm65QmBhQn%2FK0SGpX3yWdJ9lqOyXUICq2lNvD5P5laHT%2FbJM%2BB2emhWf69gsuPC39p&X-Amz-Signature=6cf75f0831f48b0abaabab2dd3cbae93504ec2c48fe39df14dcf003abec5a43e&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PG5S2RS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICnIs7FNvpkN0IboZiZ4h%2BjXcfNiZyxYxs7SF1yq3Q%2BeAiEAqwbPiWyg%2BZG5XtDJ1W13gcwmFB1025ITlwiFHzM%2FkFIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDCd2Vx7DouUFm2GUACrcA91g1dp8U%2FsJtFz8B%2F2sYiwH71UpVcViETkzRNeD5mEfOgjArs1eqVtdg%2FHtX7Su3E8N%2BMe5dd8Wo9bcBmnECaSzHFCPElccAy2%2FspW30nhRiU9Xoke2OdRZDZMMo%2Fz2aG2dcqWtsdkwlUP2qeOiaAhWFMBgPuBn4CLdtRmR0pP1PvkkE303j1AJVGwzquQH3VnGwhr6lnzCuaWFhGM8%2ByhJH4x0s3tXLgIeDAT6poo7O3dmb9f5l5DIp6Qpu75kGXM7SGv31WkNF7WHPuoPOGFwiVH%2FaXijUZ%2B4Zuaqk5MJgHyR2pJ2YcCo8NwrmbRthZLboGfWYLr7126GK030iNkpqFRKQffuVuYJd2%2FfdN9PlqqZkIP8ESkQCDCjXy7T%2BJCaKpnH6Ahr40aP6kBE5OoQ9WejJoD8mARygkVo3fRl%2FVjFjx6NLY1l2E4K77GNWQX67%2FDsLMb5EdRSfVwFuRvhZGnhkUJGaDBSKSS7Ka3S3v1hihwYCJyz50NG33WIy1t3CrK27REBqJSYccX%2BgqeNbdaF3AyYKSrPhSpwyGiNiFJemx5MyjjmNHB9D9tmUGBpI0SnZDoDAmqHCoBl53zgV8lNweU6xKGCIFMi%2FQCBOums3qW8lLll7PdMMJ%2Fzgb0GOqUBwnJ84XPccZ%2BIj2xiXaAJhD2213U8ZYHUGLKuzbt72blYgSXmK2ULIdGhkTzzmpGy3PbaGf08MC7LmVahMbiw9jPSwLYW0erS4uv58C4vhBUEUd5M3QcqwWY6s06Ezw17TtUyHWEMEQPF3sfU6PvcwjCWvXBo3kmCWObrmXPWDZUz8f3coqTTPfLDLpTeekM8pwbGmVFwpbNWBJ%2B7xly%2BlY3qZqE%2B&X-Amz-Signature=4348535c7dcf0473618e8d6082fcc0d9785a7b027dfeeb5ca5cc1b7d716131d2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PG5S2RS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICnIs7FNvpkN0IboZiZ4h%2BjXcfNiZyxYxs7SF1yq3Q%2BeAiEAqwbPiWyg%2BZG5XtDJ1W13gcwmFB1025ITlwiFHzM%2FkFIq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDCd2Vx7DouUFm2GUACrcA91g1dp8U%2FsJtFz8B%2F2sYiwH71UpVcViETkzRNeD5mEfOgjArs1eqVtdg%2FHtX7Su3E8N%2BMe5dd8Wo9bcBmnECaSzHFCPElccAy2%2FspW30nhRiU9Xoke2OdRZDZMMo%2Fz2aG2dcqWtsdkwlUP2qeOiaAhWFMBgPuBn4CLdtRmR0pP1PvkkE303j1AJVGwzquQH3VnGwhr6lnzCuaWFhGM8%2ByhJH4x0s3tXLgIeDAT6poo7O3dmb9f5l5DIp6Qpu75kGXM7SGv31WkNF7WHPuoPOGFwiVH%2FaXijUZ%2B4Zuaqk5MJgHyR2pJ2YcCo8NwrmbRthZLboGfWYLr7126GK030iNkpqFRKQffuVuYJd2%2FfdN9PlqqZkIP8ESkQCDCjXy7T%2BJCaKpnH6Ahr40aP6kBE5OoQ9WejJoD8mARygkVo3fRl%2FVjFjx6NLY1l2E4K77GNWQX67%2FDsLMb5EdRSfVwFuRvhZGnhkUJGaDBSKSS7Ka3S3v1hihwYCJyz50NG33WIy1t3CrK27REBqJSYccX%2BgqeNbdaF3AyYKSrPhSpwyGiNiFJemx5MyjjmNHB9D9tmUGBpI0SnZDoDAmqHCoBl53zgV8lNweU6xKGCIFMi%2FQCBOums3qW8lLll7PdMMJ%2Fzgb0GOqUBwnJ84XPccZ%2BIj2xiXaAJhD2213U8ZYHUGLKuzbt72blYgSXmK2ULIdGhkTzzmpGy3PbaGf08MC7LmVahMbiw9jPSwLYW0erS4uv58C4vhBUEUd5M3QcqwWY6s06Ezw17TtUyHWEMEQPF3sfU6PvcwjCWvXBo3kmCWObrmXPWDZUz8f3coqTTPfLDLpTeekM8pwbGmVFwpbNWBJ%2B7xly%2BlY3qZqE%2B&X-Amz-Signature=01e70e8f602966147282f3ee1706098f1e5bee18b675b14fa53586091cd935fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBDO2DMY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdIR6yxCinrQ2DKGRjdqUdjasFAqMk2HhMBafYe3lAfwIgPNp77GGHU6Y%2FZRw2r7pp6VmaBMsVeWiqZVWGUqQkMqYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDPG%2Bw0wFCyJljKn8nSrcA6Pl72Ov%2FdJKWzqqD1YGIoJLAx7cIbGo5nN%2FM8GptM%2BDRzoGRkIe9QtfL4UUy8ZnXCHFIoQq8Diiu8LWVE7cGRANvP4%2FDxiQDs07LAuYeCqJMq9WUDxQ72uAObOvDbcdwom3dd9DhtGhC3Mb%2FncLANdfdv2mAW2lZuAnQCWqwsdHYdcoV3sb43KwIDWbJJBnwQ4BTun9ckvGjSdBYN9ugSJ8FcrgUYGm3YTedyIN%2Bfdqd9dsbqRCUR2e2ZqF5xoTXGvR%2BTqVzVqIpW7hHkbz2APIDJ%2BC3DSdnZNVoz9TNX8CtEX34TGYudSoH0vsMFD5SdcanzABwdHGnftvVpDMIwuEiwG10udVCXqp%2FJPh8kYPNqSCey8zAa5woHN5vwPMlJxBNSVtXwrTVAHjW1KJvGCpbFccbXEfCmnFWx4ZwUADFUMUkqHlHBsTAo1DqVZUPPP2fUtV9vEmC1TpH3aFD3bWPxsc8h1ennIfA3AcGAOLJWdZsTlGpqn1ojLYJEllhPINjLfFGaRWEgIppJ5mLWB9E1lNKdh3B5ajriCYGIrvEPQzt887%2F%2BU04y9SpvCQNvd5DI5Zt6aQLzQYTaaffzxSDI%2FWmGK4IwCffVDJ7uYwh5IRoCjWT01i0PlaMLbzgb0GOqUBXABR4yZE0spSD4KovvfkBp7MNCWVrrGfZMkuHRcW%2F02ic0ayQO%2BEFRZDqmJAEMXgHCQsJaoBFfiia2OF30P%2Bjh1QN%2B%2BEdxiM2dBd3Kw4G5pulitkTP9xl6%2BQiIPPmh3u5XQVghnu1bBJQTaNYg7jIJ45lEPm65QmBhQn%2FK0SGpX3yWdJ9lqOyXUICq2lNvD5P5laHT%2FbJM%2BB2emhWf69gsuPC39p&X-Amz-Signature=42542c7e3203bfd59cc21165b946d2a6d9fb9081593e047c298acb0c5ab037e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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