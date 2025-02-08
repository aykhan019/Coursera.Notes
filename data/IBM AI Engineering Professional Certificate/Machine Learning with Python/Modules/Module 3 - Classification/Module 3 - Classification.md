

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYBCLMFS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGohdqhAjVcjXWtVPwkFBn%2FhfD97YHd13rZGVwvdEU7jAiEAtklaufNpU85VNzxxJMmZi%2Bd14hvPNssBtEjc6OvEJ5EqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDE2kCddkvlfpCAl3SrcA0TwFKYF0e47rGEmGGroSVX2UvviHKoKE1Wyux%2BAersbqutbQ6nLL9X3twStMeCdoXW1R6%2BNbgCj9Q9sWYBKDGpSdBoHSbLoTtQuYtCvezWaOob0JtIUiW3k8U%2Fiaq%2BbTjHjtgs9o4f5FcoslCKd47pSg%2Bx7CvwFBREEI%2Bf647tLZdJ3IL7PcUbIPAAqCWUlMeLnxwPVmdRTriCKKC2qE%2Fg7jKyofaHCEYBCn2OkdcWoVQLeFQ32oi0NOAVrgHiymC83bvOsrFjePiUwVI%2Bqw48idko8fCj9%2FMKpLp15PXS7%2FP507PRAnUYDUaRYFizN%2FdsUl6VxpS3spOYJ%2F7acl4Ye45YxBjhYKNrA4kQ2FVWlyd2lqWUJR7M8cM3q9obW17vaztPi%2BwA3PlhD5xNMqV3zoR02G1x53wWfQOrA5bjpBPqXt39upquH%2BRG5Bm9DIBlpJtBiqfE0%2F8gEAHk%2BFNtaN4j8KY17HLEJaotE6F3GipLpQLNu7o1UmPRCBeKJEynIMAl6hu4QSjYJV%2BOOTJhgQ5zC7%2BPLC9gGWkKg5UX111HnO0YbVB76MRHR%2F2dPhounDJ7vMcZtklhhvBTNG96nDacgSfxMPLU7cxliGJnmIBqr%2B5%2FS5za5bNY%2BMKmFnb0GOqUBY6mTx9SmMm7NieS1hRscBiMIy4CA%2FLWmT%2FQ7dZIS%2Bve%2B3sMLT5s2Gh6r2VJA2jZgm7m2pELa%2BJSWjVKqkOIJI4RUr60DwUCBaCBGk3jVz75ElVQOGnCSWhqXtIb%2BAJPrzJjqjOxUZB907sACxVg5xNaOf339bsRqriV06t0HtpRky31MG3mM6Na32kxPkV3U31d7P9iHBgDpsqW7OHk%2Fm%2FYMh6px&X-Amz-Signature=fce5c9fefcc4e914fed6e53966e01805ddda33b3c425a6d54c40aad7fe4946f8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYBCLMFS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGohdqhAjVcjXWtVPwkFBn%2FhfD97YHd13rZGVwvdEU7jAiEAtklaufNpU85VNzxxJMmZi%2Bd14hvPNssBtEjc6OvEJ5EqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDE2kCddkvlfpCAl3SrcA0TwFKYF0e47rGEmGGroSVX2UvviHKoKE1Wyux%2BAersbqutbQ6nLL9X3twStMeCdoXW1R6%2BNbgCj9Q9sWYBKDGpSdBoHSbLoTtQuYtCvezWaOob0JtIUiW3k8U%2Fiaq%2BbTjHjtgs9o4f5FcoslCKd47pSg%2Bx7CvwFBREEI%2Bf647tLZdJ3IL7PcUbIPAAqCWUlMeLnxwPVmdRTriCKKC2qE%2Fg7jKyofaHCEYBCn2OkdcWoVQLeFQ32oi0NOAVrgHiymC83bvOsrFjePiUwVI%2Bqw48idko8fCj9%2FMKpLp15PXS7%2FP507PRAnUYDUaRYFizN%2FdsUl6VxpS3spOYJ%2F7acl4Ye45YxBjhYKNrA4kQ2FVWlyd2lqWUJR7M8cM3q9obW17vaztPi%2BwA3PlhD5xNMqV3zoR02G1x53wWfQOrA5bjpBPqXt39upquH%2BRG5Bm9DIBlpJtBiqfE0%2F8gEAHk%2BFNtaN4j8KY17HLEJaotE6F3GipLpQLNu7o1UmPRCBeKJEynIMAl6hu4QSjYJV%2BOOTJhgQ5zC7%2BPLC9gGWkKg5UX111HnO0YbVB76MRHR%2F2dPhounDJ7vMcZtklhhvBTNG96nDacgSfxMPLU7cxliGJnmIBqr%2B5%2FS5za5bNY%2BMKmFnb0GOqUBY6mTx9SmMm7NieS1hRscBiMIy4CA%2FLWmT%2FQ7dZIS%2Bve%2B3sMLT5s2Gh6r2VJA2jZgm7m2pELa%2BJSWjVKqkOIJI4RUr60DwUCBaCBGk3jVz75ElVQOGnCSWhqXtIb%2BAJPrzJjqjOxUZB907sACxVg5xNaOf339bsRqriV06t0HtpRky31MG3mM6Na32kxPkV3U31d7P9iHBgDpsqW7OHk%2Fm%2FYMh6px&X-Amz-Signature=dbb37839e19bb85f782a7224837ab984211f0696bda2be6728c63fced8bd75b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYBCLMFS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGohdqhAjVcjXWtVPwkFBn%2FhfD97YHd13rZGVwvdEU7jAiEAtklaufNpU85VNzxxJMmZi%2Bd14hvPNssBtEjc6OvEJ5EqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDE2kCddkvlfpCAl3SrcA0TwFKYF0e47rGEmGGroSVX2UvviHKoKE1Wyux%2BAersbqutbQ6nLL9X3twStMeCdoXW1R6%2BNbgCj9Q9sWYBKDGpSdBoHSbLoTtQuYtCvezWaOob0JtIUiW3k8U%2Fiaq%2BbTjHjtgs9o4f5FcoslCKd47pSg%2Bx7CvwFBREEI%2Bf647tLZdJ3IL7PcUbIPAAqCWUlMeLnxwPVmdRTriCKKC2qE%2Fg7jKyofaHCEYBCn2OkdcWoVQLeFQ32oi0NOAVrgHiymC83bvOsrFjePiUwVI%2Bqw48idko8fCj9%2FMKpLp15PXS7%2FP507PRAnUYDUaRYFizN%2FdsUl6VxpS3spOYJ%2F7acl4Ye45YxBjhYKNrA4kQ2FVWlyd2lqWUJR7M8cM3q9obW17vaztPi%2BwA3PlhD5xNMqV3zoR02G1x53wWfQOrA5bjpBPqXt39upquH%2BRG5Bm9DIBlpJtBiqfE0%2F8gEAHk%2BFNtaN4j8KY17HLEJaotE6F3GipLpQLNu7o1UmPRCBeKJEynIMAl6hu4QSjYJV%2BOOTJhgQ5zC7%2BPLC9gGWkKg5UX111HnO0YbVB76MRHR%2F2dPhounDJ7vMcZtklhhvBTNG96nDacgSfxMPLU7cxliGJnmIBqr%2B5%2FS5za5bNY%2BMKmFnb0GOqUBY6mTx9SmMm7NieS1hRscBiMIy4CA%2FLWmT%2FQ7dZIS%2Bve%2B3sMLT5s2Gh6r2VJA2jZgm7m2pELa%2BJSWjVKqkOIJI4RUr60DwUCBaCBGk3jVz75ElVQOGnCSWhqXtIb%2BAJPrzJjqjOxUZB907sACxVg5xNaOf339bsRqriV06t0HtpRky31MG3mM6Na32kxPkV3U31d7P9iHBgDpsqW7OHk%2Fm%2FYMh6px&X-Amz-Signature=250c4957adcc8c3cff63dc129cbfd3ab0843cd9e61543eb528f6093afc187322&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRNQQ74Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQD8fzdpmg%2BLKCv%2BFYLfrZxighmTQAOklqktxnNYeDSlLQIgVfPAPtwYZxsDPL5V784QIUxZ4fgKqzGETVHR2yU64AcqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD1g3ZGdmZ9A%2B5s3ryrcA8VYbgIE84AGG%2FOak5URFTdGhUWY0%2FSu5QbJMdPwUOW7WCawJbZfebtwYoV2uxwnErE6vrXYV4ROcjSd46%2BinThOxj5npVth2pIIdeztNMjJEEZkRzKAxV6psakAnjXaJutS50tdQEwKzojEcNsLMS2alI8godMplQYVpjRuaNon3uc%2BjS8GTYJR06vo%2BN%2BPs5I5%2BgKDlYO0FEPF2MTfkpVpToxVDfPkOuqfDAXNxP6dA1pRuNF3KYrWv7LXOyFvXsTVMlGwcqqu1kq9hdF1mqDlzVxgcrsX5HnPQ9PHpvANrE8ynI13LvBwB3T6LGXVm6GMBILb0A0QDpyWA6HyJ80kFuQqCnNcuKXfdN8d%2FWmApB6OqNhMS2WA0KFclecuo3K3jS8jl%2Fa5CqUSe2vBdh648o3DvrF83cZwSECuE2QCFX7hb5iehYrUMYAkMasbOvTOfpCP6BLtBPaj3X78U5%2FOx0UxhGI8VHAiitrgyHDcmVtiBbv5nK52sLRvBjVAYmGDOAoBR5fVSak77WmR5m7MF%2Bydmd%2FpL%2FXkqNuJfk4pPyYhecz6mciLQfSRhpQfoyVhBteCa0PxSGbQ5WNO%2Bfc1eximPey9UiQG%2FofU2tq41V74t5IpssrCPvzzMJCFnb0GOqUBeaAZio9Y8QmyHFNQmSsWqjh0%2BiLGZVMqY7Nk0fcYbep7odsRFqgHBXbrEpd81O5c3Z57RdmlqDwqDNZ%2Bb8%2BddXbdYFMVI0cUhAXTfLGvYyXdwC06cDKjxgUB8woPJaGyeFSIQo7DG6OnZjRs%2BS8iRzwiuseq6c2OETeobjkZ%2FN1JL%2BWWC6W3mi959vMp4l6c5lJA7UEsrJlarpRISJ34xAlOxVNZ&X-Amz-Signature=dd44f490155d4bddada0a410e976e764bc30945b5b98d5fd3a51d60f05642053&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRNQQ74Q%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQD8fzdpmg%2BLKCv%2BFYLfrZxighmTQAOklqktxnNYeDSlLQIgVfPAPtwYZxsDPL5V784QIUxZ4fgKqzGETVHR2yU64AcqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD1g3ZGdmZ9A%2B5s3ryrcA8VYbgIE84AGG%2FOak5URFTdGhUWY0%2FSu5QbJMdPwUOW7WCawJbZfebtwYoV2uxwnErE6vrXYV4ROcjSd46%2BinThOxj5npVth2pIIdeztNMjJEEZkRzKAxV6psakAnjXaJutS50tdQEwKzojEcNsLMS2alI8godMplQYVpjRuaNon3uc%2BjS8GTYJR06vo%2BN%2BPs5I5%2BgKDlYO0FEPF2MTfkpVpToxVDfPkOuqfDAXNxP6dA1pRuNF3KYrWv7LXOyFvXsTVMlGwcqqu1kq9hdF1mqDlzVxgcrsX5HnPQ9PHpvANrE8ynI13LvBwB3T6LGXVm6GMBILb0A0QDpyWA6HyJ80kFuQqCnNcuKXfdN8d%2FWmApB6OqNhMS2WA0KFclecuo3K3jS8jl%2Fa5CqUSe2vBdh648o3DvrF83cZwSECuE2QCFX7hb5iehYrUMYAkMasbOvTOfpCP6BLtBPaj3X78U5%2FOx0UxhGI8VHAiitrgyHDcmVtiBbv5nK52sLRvBjVAYmGDOAoBR5fVSak77WmR5m7MF%2Bydmd%2FpL%2FXkqNuJfk4pPyYhecz6mciLQfSRhpQfoyVhBteCa0PxSGbQ5WNO%2Bfc1eximPey9UiQG%2FofU2tq41V74t5IpssrCPvzzMJCFnb0GOqUBeaAZio9Y8QmyHFNQmSsWqjh0%2BiLGZVMqY7Nk0fcYbep7odsRFqgHBXbrEpd81O5c3Z57RdmlqDwqDNZ%2Bb8%2BddXbdYFMVI0cUhAXTfLGvYyXdwC06cDKjxgUB8woPJaGyeFSIQo7DG6OnZjRs%2BS8iRzwiuseq6c2OETeobjkZ%2FN1JL%2BWWC6W3mi959vMp4l6c5lJA7UEsrJlarpRISJ34xAlOxVNZ&X-Amz-Signature=c359a1e5311144a7c47d12c96e17c08158831aecb39557292cc8d4e987342170&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYBCLMFS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIGohdqhAjVcjXWtVPwkFBn%2FhfD97YHd13rZGVwvdEU7jAiEAtklaufNpU85VNzxxJMmZi%2Bd14hvPNssBtEjc6OvEJ5EqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDE2kCddkvlfpCAl3SrcA0TwFKYF0e47rGEmGGroSVX2UvviHKoKE1Wyux%2BAersbqutbQ6nLL9X3twStMeCdoXW1R6%2BNbgCj9Q9sWYBKDGpSdBoHSbLoTtQuYtCvezWaOob0JtIUiW3k8U%2Fiaq%2BbTjHjtgs9o4f5FcoslCKd47pSg%2Bx7CvwFBREEI%2Bf647tLZdJ3IL7PcUbIPAAqCWUlMeLnxwPVmdRTriCKKC2qE%2Fg7jKyofaHCEYBCn2OkdcWoVQLeFQ32oi0NOAVrgHiymC83bvOsrFjePiUwVI%2Bqw48idko8fCj9%2FMKpLp15PXS7%2FP507PRAnUYDUaRYFizN%2FdsUl6VxpS3spOYJ%2F7acl4Ye45YxBjhYKNrA4kQ2FVWlyd2lqWUJR7M8cM3q9obW17vaztPi%2BwA3PlhD5xNMqV3zoR02G1x53wWfQOrA5bjpBPqXt39upquH%2BRG5Bm9DIBlpJtBiqfE0%2F8gEAHk%2BFNtaN4j8KY17HLEJaotE6F3GipLpQLNu7o1UmPRCBeKJEynIMAl6hu4QSjYJV%2BOOTJhgQ5zC7%2BPLC9gGWkKg5UX111HnO0YbVB76MRHR%2F2dPhounDJ7vMcZtklhhvBTNG96nDacgSfxMPLU7cxliGJnmIBqr%2B5%2FS5za5bNY%2BMKmFnb0GOqUBY6mTx9SmMm7NieS1hRscBiMIy4CA%2FLWmT%2FQ7dZIS%2Bve%2B3sMLT5s2Gh6r2VJA2jZgm7m2pELa%2BJSWjVKqkOIJI4RUr60DwUCBaCBGk3jVz75ElVQOGnCSWhqXtIb%2BAJPrzJjqjOxUZB907sACxVg5xNaOf339bsRqriV06t0HtpRky31MG3mM6Na32kxPkV3U31d7P9iHBgDpsqW7OHk%2Fm%2FYMh6px&X-Amz-Signature=6386d8db6a25a9b72ff4f986d1a8cf167a04542bf296e2830d9b14ceac5f3096&X-Amz-SignedHeaders=host&x-id=GetObject)
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