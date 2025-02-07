

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SRRTDVM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDKG8S2hDI4f3Y41EimccCcHvydJ%2BB6O6OMZcIRsEELeQIgYq6yymLLqVPw7aOvKyu%2BKWxmlQm%2BPNCHa3tAaz1KYjAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFm1kyw3baoDi%2BQChCrcA1gPH4Uktsvk3SGnzNlLMHZq3wd8RRUCuUMLmVD3w7LZHgfrF8cTCWT%2F1WIfV%2FUP29DQKk5GTZl7BaESgQN9m1LZuCs8BKQhOpRgTH%2BntTEB6KRzZYpuPPIvsEsbt8R%2BGMYonCxfzp%2FMPPF9gYRZWyAIAYyBhx6fbjC5Gbb3Zf8IU%2FbKGgALPrHR0Ant4XuwLnbJAi9szvJwOfCbUHnb6L7C%2FhXd50VYrgqHSzhz5u2pr6jvZ1rd6Z4FA0ng8dP3z2TcfIjeitiZT5dXODiDQXOAAsNXhFoaiRoiceQhHuGyMFSzuDmF0s6%2BjBNaIcEx5laEfCbuJRDZ%2FXuBzh8zhOvyPskD%2BbDoaxGb1lIfoqMS3uLZAoYR7XNW%2FoZnhpr2EwoTQy%2FaGZKe4mClKCb6q1%2BjZWbP5r38N9ygnQQAENZJhuniiNbXSFKfzxUgZ0jTEXju%2Bj8GVR2sT%2BJswNkKAhPJO6bkRJM9epbWqH0txZSSHuzSqAO2lZrbVvTNzFCnQP6LiNN%2FB%2FBJwJHr1ogva8S68R22A%2Bd1g7syZa49VRuNvbbqBV7slcRi9h0Zj7hniDbjsqX7IOBmt446gMo7NkImNFmHV3z0srkET8hNC3vjrPkx5L3r2QzaTrmaMNr%2Bmb0GOqUBPa6q8uRnwtDn37ppEz%2BsCndjFQz1yoqHY3KGKenu8y9bjD6sWY6dNB9sIhsu2bwGUOMGge8MKRpvct7yjpZCOK8TO9QJTPVXoxCYsKe7i%2FrAsujbwy4U3Rsx8QHZyk6QLwsIpol2RuYgm%2Fe3c7skZ16vR72bokixCZ2%2FAKGGquAB9KXXuPX7Iv2%2Bm2kHwemdnAokcHfS03jiHsofnpzq%2BIE67PHU&X-Amz-Signature=fdf0c3607291b5e9525e5508e411ece335dee1acede94deb8b40b2a7eaa07bf2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SRRTDVM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDKG8S2hDI4f3Y41EimccCcHvydJ%2BB6O6OMZcIRsEELeQIgYq6yymLLqVPw7aOvKyu%2BKWxmlQm%2BPNCHa3tAaz1KYjAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFm1kyw3baoDi%2BQChCrcA1gPH4Uktsvk3SGnzNlLMHZq3wd8RRUCuUMLmVD3w7LZHgfrF8cTCWT%2F1WIfV%2FUP29DQKk5GTZl7BaESgQN9m1LZuCs8BKQhOpRgTH%2BntTEB6KRzZYpuPPIvsEsbt8R%2BGMYonCxfzp%2FMPPF9gYRZWyAIAYyBhx6fbjC5Gbb3Zf8IU%2FbKGgALPrHR0Ant4XuwLnbJAi9szvJwOfCbUHnb6L7C%2FhXd50VYrgqHSzhz5u2pr6jvZ1rd6Z4FA0ng8dP3z2TcfIjeitiZT5dXODiDQXOAAsNXhFoaiRoiceQhHuGyMFSzuDmF0s6%2BjBNaIcEx5laEfCbuJRDZ%2FXuBzh8zhOvyPskD%2BbDoaxGb1lIfoqMS3uLZAoYR7XNW%2FoZnhpr2EwoTQy%2FaGZKe4mClKCb6q1%2BjZWbP5r38N9ygnQQAENZJhuniiNbXSFKfzxUgZ0jTEXju%2Bj8GVR2sT%2BJswNkKAhPJO6bkRJM9epbWqH0txZSSHuzSqAO2lZrbVvTNzFCnQP6LiNN%2FB%2FBJwJHr1ogva8S68R22A%2Bd1g7syZa49VRuNvbbqBV7slcRi9h0Zj7hniDbjsqX7IOBmt446gMo7NkImNFmHV3z0srkET8hNC3vjrPkx5L3r2QzaTrmaMNr%2Bmb0GOqUBPa6q8uRnwtDn37ppEz%2BsCndjFQz1yoqHY3KGKenu8y9bjD6sWY6dNB9sIhsu2bwGUOMGge8MKRpvct7yjpZCOK8TO9QJTPVXoxCYsKe7i%2FrAsujbwy4U3Rsx8QHZyk6QLwsIpol2RuYgm%2Fe3c7skZ16vR72bokixCZ2%2FAKGGquAB9KXXuPX7Iv2%2Bm2kHwemdnAokcHfS03jiHsofnpzq%2BIE67PHU&X-Amz-Signature=64de217a663b8e47eb553bf18f498d1884606c7ee06f1745966d67c837d9e679&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SRRTDVM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDKG8S2hDI4f3Y41EimccCcHvydJ%2BB6O6OMZcIRsEELeQIgYq6yymLLqVPw7aOvKyu%2BKWxmlQm%2BPNCHa3tAaz1KYjAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFm1kyw3baoDi%2BQChCrcA1gPH4Uktsvk3SGnzNlLMHZq3wd8RRUCuUMLmVD3w7LZHgfrF8cTCWT%2F1WIfV%2FUP29DQKk5GTZl7BaESgQN9m1LZuCs8BKQhOpRgTH%2BntTEB6KRzZYpuPPIvsEsbt8R%2BGMYonCxfzp%2FMPPF9gYRZWyAIAYyBhx6fbjC5Gbb3Zf8IU%2FbKGgALPrHR0Ant4XuwLnbJAi9szvJwOfCbUHnb6L7C%2FhXd50VYrgqHSzhz5u2pr6jvZ1rd6Z4FA0ng8dP3z2TcfIjeitiZT5dXODiDQXOAAsNXhFoaiRoiceQhHuGyMFSzuDmF0s6%2BjBNaIcEx5laEfCbuJRDZ%2FXuBzh8zhOvyPskD%2BbDoaxGb1lIfoqMS3uLZAoYR7XNW%2FoZnhpr2EwoTQy%2FaGZKe4mClKCb6q1%2BjZWbP5r38N9ygnQQAENZJhuniiNbXSFKfzxUgZ0jTEXju%2Bj8GVR2sT%2BJswNkKAhPJO6bkRJM9epbWqH0txZSSHuzSqAO2lZrbVvTNzFCnQP6LiNN%2FB%2FBJwJHr1ogva8S68R22A%2Bd1g7syZa49VRuNvbbqBV7slcRi9h0Zj7hniDbjsqX7IOBmt446gMo7NkImNFmHV3z0srkET8hNC3vjrPkx5L3r2QzaTrmaMNr%2Bmb0GOqUBPa6q8uRnwtDn37ppEz%2BsCndjFQz1yoqHY3KGKenu8y9bjD6sWY6dNB9sIhsu2bwGUOMGge8MKRpvct7yjpZCOK8TO9QJTPVXoxCYsKe7i%2FrAsujbwy4U3Rsx8QHZyk6QLwsIpol2RuYgm%2Fe3c7skZ16vR72bokixCZ2%2FAKGGquAB9KXXuPX7Iv2%2Bm2kHwemdnAokcHfS03jiHsofnpzq%2BIE67PHU&X-Amz-Signature=4268e2a7c825c1f996919158ba7762947358ae91f582854d7a0985e586918662&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FWRLXLF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEYqM%2F19ssPyadGseMWLb8OG4HghS3o6Tl2YauoYmBh3AiEA8p1rDKU%2FOyRLsl6fD50LL8e0DPba7Y161Z1gw5l1GpIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFAanfRdhrlTkgpu%2FSrcA%2B%2BxEt8gQmlxd1BMvESVF74xDpz%2BozQF8eK%2B%2Fl6atzIzrCJXJwtYpi3lt51awvPMv9hdtRAA0F%2Fp5mYoAEdxQGup%2BBlcnTQlVLi8ebuiKibFQ%2BazoNs2YjGNQ%2FOkJhkWFeBt6sy%2FeDvJ6uFOVorEGhTnDhRfWEmM5iVAKB%2BhyVs15Dx%2Bvyv6GyvgQ6Y4RcCcOEx3PEs6z%2BOzdyyHp7tHn65xugPO%2F1hSZK61HXGludfVwdVFuPiBSGZQls1kyhuVqMb7ED7V0DCC1GjOuD8Bz1Ebe%2FM2FShxqzNaaMbhGYpB2rl%2FNerTe5o2ohMBLqQGMJNlNIgwwUL9Z8BnjHyfwOm2%2B4FG9r7hEWglzcl1vHsGLW1db%2Fm183%2BF9YKPP%2FIbh%2FchVsCmvpIQd1DUKGUvoXXA25P1bQy99VGyxl6PJqJ5kRs3Iu8l8tuMDVQa4nLJP8itePZLi2Hacxmgi%2B4%2FwPvBqAxxinb9MbJtAOJYvyWJ9lciId%2BhoDvnPGvc1FVDJLxrWPENFQmMsAB0jhARu%2FclhWnfMBCSLuu72rHO%2FpQ8Xfu6QZAd1usP9WSk09CF3kyJer8Hv6lrRNh3rAojSBPa6aHHFpnITRYjm54%2FwqcByzx7l1pZy3ZlFQ69MKD%2Bmb0GOqUBqrv3U2hN6xfkSsr%2Bl2Ea%2BedJuE2gLeYjRzaq2GLESZoB2e74JronREm27Cp%2BLdPE51%2FM6EjWYV6P5htn8bvsMFZ0xgiksKTkmj8dXemaEtimawgtBq7HsifIl0VxyPtfdYDdNXPQoWAAS08EUMLZ%2F7JAhx2VYb0blvtzYkuCFSjNTpgu5wtvHxFCjxZviMcBsOpNM3VcoR6j9QXixnaMZOKCqWNN&X-Amz-Signature=0a7a1bf100641f6181e06d342b62e4dcf4bd4870d5ac348cbb83602356a639f1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FWRLXLF%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIEYqM%2F19ssPyadGseMWLb8OG4HghS3o6Tl2YauoYmBh3AiEA8p1rDKU%2FOyRLsl6fD50LL8e0DPba7Y161Z1gw5l1GpIq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFAanfRdhrlTkgpu%2FSrcA%2B%2BxEt8gQmlxd1BMvESVF74xDpz%2BozQF8eK%2B%2Fl6atzIzrCJXJwtYpi3lt51awvPMv9hdtRAA0F%2Fp5mYoAEdxQGup%2BBlcnTQlVLi8ebuiKibFQ%2BazoNs2YjGNQ%2FOkJhkWFeBt6sy%2FeDvJ6uFOVorEGhTnDhRfWEmM5iVAKB%2BhyVs15Dx%2Bvyv6GyvgQ6Y4RcCcOEx3PEs6z%2BOzdyyHp7tHn65xugPO%2F1hSZK61HXGludfVwdVFuPiBSGZQls1kyhuVqMb7ED7V0DCC1GjOuD8Bz1Ebe%2FM2FShxqzNaaMbhGYpB2rl%2FNerTe5o2ohMBLqQGMJNlNIgwwUL9Z8BnjHyfwOm2%2B4FG9r7hEWglzcl1vHsGLW1db%2Fm183%2BF9YKPP%2FIbh%2FchVsCmvpIQd1DUKGUvoXXA25P1bQy99VGyxl6PJqJ5kRs3Iu8l8tuMDVQa4nLJP8itePZLi2Hacxmgi%2B4%2FwPvBqAxxinb9MbJtAOJYvyWJ9lciId%2BhoDvnPGvc1FVDJLxrWPENFQmMsAB0jhARu%2FclhWnfMBCSLuu72rHO%2FpQ8Xfu6QZAd1usP9WSk09CF3kyJer8Hv6lrRNh3rAojSBPa6aHHFpnITRYjm54%2FwqcByzx7l1pZy3ZlFQ69MKD%2Bmb0GOqUBqrv3U2hN6xfkSsr%2Bl2Ea%2BedJuE2gLeYjRzaq2GLESZoB2e74JronREm27Cp%2BLdPE51%2FM6EjWYV6P5htn8bvsMFZ0xgiksKTkmj8dXemaEtimawgtBq7HsifIl0VxyPtfdYDdNXPQoWAAS08EUMLZ%2F7JAhx2VYb0blvtzYkuCFSjNTpgu5wtvHxFCjxZviMcBsOpNM3VcoR6j9QXixnaMZOKCqWNN&X-Amz-Signature=df5942daaad6fc163c978857694ecb110851810ae11ce4a9290cfbba425062cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SRRTDVM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDKG8S2hDI4f3Y41EimccCcHvydJ%2BB6O6OMZcIRsEELeQIgYq6yymLLqVPw7aOvKyu%2BKWxmlQm%2BPNCHa3tAaz1KYjAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFm1kyw3baoDi%2BQChCrcA1gPH4Uktsvk3SGnzNlLMHZq3wd8RRUCuUMLmVD3w7LZHgfrF8cTCWT%2F1WIfV%2FUP29DQKk5GTZl7BaESgQN9m1LZuCs8BKQhOpRgTH%2BntTEB6KRzZYpuPPIvsEsbt8R%2BGMYonCxfzp%2FMPPF9gYRZWyAIAYyBhx6fbjC5Gbb3Zf8IU%2FbKGgALPrHR0Ant4XuwLnbJAi9szvJwOfCbUHnb6L7C%2FhXd50VYrgqHSzhz5u2pr6jvZ1rd6Z4FA0ng8dP3z2TcfIjeitiZT5dXODiDQXOAAsNXhFoaiRoiceQhHuGyMFSzuDmF0s6%2BjBNaIcEx5laEfCbuJRDZ%2FXuBzh8zhOvyPskD%2BbDoaxGb1lIfoqMS3uLZAoYR7XNW%2FoZnhpr2EwoTQy%2FaGZKe4mClKCb6q1%2BjZWbP5r38N9ygnQQAENZJhuniiNbXSFKfzxUgZ0jTEXju%2Bj8GVR2sT%2BJswNkKAhPJO6bkRJM9epbWqH0txZSSHuzSqAO2lZrbVvTNzFCnQP6LiNN%2FB%2FBJwJHr1ogva8S68R22A%2Bd1g7syZa49VRuNvbbqBV7slcRi9h0Zj7hniDbjsqX7IOBmt446gMo7NkImNFmHV3z0srkET8hNC3vjrPkx5L3r2QzaTrmaMNr%2Bmb0GOqUBPa6q8uRnwtDn37ppEz%2BsCndjFQz1yoqHY3KGKenu8y9bjD6sWY6dNB9sIhsu2bwGUOMGge8MKRpvct7yjpZCOK8TO9QJTPVXoxCYsKe7i%2FrAsujbwy4U3Rsx8QHZyk6QLwsIpol2RuYgm%2Fe3c7skZ16vR72bokixCZ2%2FAKGGquAB9KXXuPX7Iv2%2Bm2kHwemdnAokcHfS03jiHsofnpzq%2BIE67PHU&X-Amz-Signature=0512fd4f7553be3fa4e81138ded35062760b0ff0b21c5364cbceaabbcca17b0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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