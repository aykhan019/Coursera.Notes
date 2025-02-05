

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ2PUFID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIFDpG3FzsMXJTwVNSCScWw0DfeJh4P9goZSBTDwBDm0LAiEAmsPdp1C2djB6XX0z7e19GrnXKPOoO7Dn507U4glJ%2Br0q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDK92BiJO%2B6SX19hRVCrcAyKQ8AERFr3jiiL2XB1fXIaA5wjYVTVS8QB8Yo%2BPNfGsArjLxkH2bQwsES93qB6x1z7EMNg4ilEBCDxSBv2%2BHNVwjEBDbnkbGIwpeAHiAaMfZZch4wUExKfP523XoNGrKTqm%2FzfWvpZCEdsKsD7ynvPdVvYd2NboYaG9ih%2FZTyvENRPt6NKCaQQKqZH8RRmdDyxDb1HYuE2lpERsJtkiC%2BzQ7uLzcXuhVdzuyXzHuFxblV%2Bv7Et7ATk2YqGmLJah8t0wuvXnnbzwRfuhkU%2Baek0o6OUi9C7XQEu0ChM%2BOdbF8lx0hlkAN1287NXQdfMTmzKAB9675RruMILGb3w5zRzIMV9MgNwQrgMFgfPBoWpsQ2WQi0OOnba2rJzz5xOyrQUL1dVp0O7dYL0SUqajE33trbvh52OiF16zFYTB9mUE%2BqXAj11RVYHBDOm5YCgdhH7CAvo%2FEjRnoZRz7qvVP3SCemn%2B5TlCh8iGt8vXqWZybC3oKE%2FeaEPKlv%2F31myaI1Eti3iMMS0zeIiv6oPhyxoj%2FXV9ugCS0cjF9lZikaR%2FDluTEnSSUbFwSJnEaPIcbm9ajimomhEka3OxXkdnxO%2FxQarXNF%2FWOt7TYCXOgIQNX%2F%2Fte962JOtXHDw8MK%2Bdjr0GOqUBP9UC8jeYAP9pfW5J89kxNG%2BUS1BqoSKz1777XGe15dmnUswyW%2BxDcDiqZ%2FQlsKiRR5aP74LihaPYIJcRttZrqBD2EJNH%2FltAQiVL9ui797JqhA7Aye7h1F%2B0Dof3%2F9hOTVGt5HGjP6I5m5sJP8e7dRExigosGg7v0vI6WLwzsN2ViZPFqwYH6SB%2F67e36cVzd26G14QEEmd54CIbGw%2BOK7TGNuOW&X-Amz-Signature=be29296133b625c0443e75c0fcff08afdba03b8231d1307d9c0a216266681d14&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ2PUFID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIFDpG3FzsMXJTwVNSCScWw0DfeJh4P9goZSBTDwBDm0LAiEAmsPdp1C2djB6XX0z7e19GrnXKPOoO7Dn507U4glJ%2Br0q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDK92BiJO%2B6SX19hRVCrcAyKQ8AERFr3jiiL2XB1fXIaA5wjYVTVS8QB8Yo%2BPNfGsArjLxkH2bQwsES93qB6x1z7EMNg4ilEBCDxSBv2%2BHNVwjEBDbnkbGIwpeAHiAaMfZZch4wUExKfP523XoNGrKTqm%2FzfWvpZCEdsKsD7ynvPdVvYd2NboYaG9ih%2FZTyvENRPt6NKCaQQKqZH8RRmdDyxDb1HYuE2lpERsJtkiC%2BzQ7uLzcXuhVdzuyXzHuFxblV%2Bv7Et7ATk2YqGmLJah8t0wuvXnnbzwRfuhkU%2Baek0o6OUi9C7XQEu0ChM%2BOdbF8lx0hlkAN1287NXQdfMTmzKAB9675RruMILGb3w5zRzIMV9MgNwQrgMFgfPBoWpsQ2WQi0OOnba2rJzz5xOyrQUL1dVp0O7dYL0SUqajE33trbvh52OiF16zFYTB9mUE%2BqXAj11RVYHBDOm5YCgdhH7CAvo%2FEjRnoZRz7qvVP3SCemn%2B5TlCh8iGt8vXqWZybC3oKE%2FeaEPKlv%2F31myaI1Eti3iMMS0zeIiv6oPhyxoj%2FXV9ugCS0cjF9lZikaR%2FDluTEnSSUbFwSJnEaPIcbm9ajimomhEka3OxXkdnxO%2FxQarXNF%2FWOt7TYCXOgIQNX%2F%2Fte962JOtXHDw8MK%2Bdjr0GOqUBP9UC8jeYAP9pfW5J89kxNG%2BUS1BqoSKz1777XGe15dmnUswyW%2BxDcDiqZ%2FQlsKiRR5aP74LihaPYIJcRttZrqBD2EJNH%2FltAQiVL9ui797JqhA7Aye7h1F%2B0Dof3%2F9hOTVGt5HGjP6I5m5sJP8e7dRExigosGg7v0vI6WLwzsN2ViZPFqwYH6SB%2F67e36cVzd26G14QEEmd54CIbGw%2BOK7TGNuOW&X-Amz-Signature=02c8ed9860456b0e46316ba7db50e18aaae1560c58d2aba2938fc40592e4f51b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ2PUFID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIFDpG3FzsMXJTwVNSCScWw0DfeJh4P9goZSBTDwBDm0LAiEAmsPdp1C2djB6XX0z7e19GrnXKPOoO7Dn507U4glJ%2Br0q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDK92BiJO%2B6SX19hRVCrcAyKQ8AERFr3jiiL2XB1fXIaA5wjYVTVS8QB8Yo%2BPNfGsArjLxkH2bQwsES93qB6x1z7EMNg4ilEBCDxSBv2%2BHNVwjEBDbnkbGIwpeAHiAaMfZZch4wUExKfP523XoNGrKTqm%2FzfWvpZCEdsKsD7ynvPdVvYd2NboYaG9ih%2FZTyvENRPt6NKCaQQKqZH8RRmdDyxDb1HYuE2lpERsJtkiC%2BzQ7uLzcXuhVdzuyXzHuFxblV%2Bv7Et7ATk2YqGmLJah8t0wuvXnnbzwRfuhkU%2Baek0o6OUi9C7XQEu0ChM%2BOdbF8lx0hlkAN1287NXQdfMTmzKAB9675RruMILGb3w5zRzIMV9MgNwQrgMFgfPBoWpsQ2WQi0OOnba2rJzz5xOyrQUL1dVp0O7dYL0SUqajE33trbvh52OiF16zFYTB9mUE%2BqXAj11RVYHBDOm5YCgdhH7CAvo%2FEjRnoZRz7qvVP3SCemn%2B5TlCh8iGt8vXqWZybC3oKE%2FeaEPKlv%2F31myaI1Eti3iMMS0zeIiv6oPhyxoj%2FXV9ugCS0cjF9lZikaR%2FDluTEnSSUbFwSJnEaPIcbm9ajimomhEka3OxXkdnxO%2FxQarXNF%2FWOt7TYCXOgIQNX%2F%2Fte962JOtXHDw8MK%2Bdjr0GOqUBP9UC8jeYAP9pfW5J89kxNG%2BUS1BqoSKz1777XGe15dmnUswyW%2BxDcDiqZ%2FQlsKiRR5aP74LihaPYIJcRttZrqBD2EJNH%2FltAQiVL9ui797JqhA7Aye7h1F%2B0Dof3%2F9hOTVGt5HGjP6I5m5sJP8e7dRExigosGg7v0vI6WLwzsN2ViZPFqwYH6SB%2F67e36cVzd26G14QEEmd54CIbGw%2BOK7TGNuOW&X-Amz-Signature=9fe5d1f2ac7dc0e8a42b6e0ccb7bd2b522576ad093fc2e71c9c4b24d321ecd45&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVHUA7D5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIGHsqh2pfVwjeRYOY3IzCFwgp6thX4S9yKYTPtPRE4%2BlAiA9wNo95%2BPXYg1a0cHzddmC1LhJsM9PTv9J6DtrDDZGHCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMApvnJpfENTrHHb3rKtwDNy4SdF1nVmkveEE6Io7Vwj4JzhjdBKVH4318%2FlWz%2B0dg1HPejAoGKvDl%2FtL%2B70CaBJKgZjz%2B76CpBuwEwOc28mGewQBLuNOQ1F73Ju47J3yxXIYiHMsz6U%2BXwilh7y%2FD5fDafALAIVoejBHqcSxWbWgdQQQchbxw2Z%2B2E%2FfIk6xL7LvqwmtZyPAycd5C0ircae%2Bv3M%2FQE8O3ROPk9j8PWTcH3NhzDTa4%2Fji6817ysng0IfS26tB7LZS7u7nYT7%2FG7vtP8Gh5QZZHLcArTTynQF8GsWEIwVSpdUQY2YiseSEYMXuptH5Oj4Y9%2FFgSiqpirn7k4UQAII4d%2FJzNais%2BpGzZeWimFWBwg0FHPWhRn7E7FRipd7Rvhi25VzG7toG6Yysa44UvyyEIXQXxEbQueTbDqYVVKZuXkIf%2BXVGu4UdH%2BUK00fdEPmA4v1JuPsj8EqGMca1CgzdHDkVkbvEGbiZj11kMT0Dl5Qx8wOZAooJgUna5Na5uAnPJcqogsBydAyGDBwinMKXSiw6w%2FR3d3gP28Dk3NboWzsARbr85Yixl4iKC%2Bu1AagJL1LXQeeEHdzJN4978NMuNjjMvOoIMrWC3xMWrgVOIND7QCIFFWpRhsxzaFa4VfCofqhIw6J2OvQY6pgHjNCNvhNKpH0BhOXN7EhGZ8%2B9S4YvrWO7ns%2FSeJ66ocJDLpnCu7DbpO0QdyXBUEJ48nWygfJl4uB8crr8xsW3UxqugcH4VsuMeUT56Gz09mlrIih1onYb4BdPpfBOox%2FMzDg524xGvdvYfC1J7QkETbEWt0gZVCQnvFXMwrOnzL6Jiod%2BTcci646ivKfvSTuWhNf6K3gRADvE2odykljVgqEoKLp9O&X-Amz-Signature=ae2bb198f7b4dbf7a3bd2313ca87355ac498b8ae12b941f2a149b5e3a810ff5d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVHUA7D5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIGHsqh2pfVwjeRYOY3IzCFwgp6thX4S9yKYTPtPRE4%2BlAiA9wNo95%2BPXYg1a0cHzddmC1LhJsM9PTv9J6DtrDDZGHCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMApvnJpfENTrHHb3rKtwDNy4SdF1nVmkveEE6Io7Vwj4JzhjdBKVH4318%2FlWz%2B0dg1HPejAoGKvDl%2FtL%2B70CaBJKgZjz%2B76CpBuwEwOc28mGewQBLuNOQ1F73Ju47J3yxXIYiHMsz6U%2BXwilh7y%2FD5fDafALAIVoejBHqcSxWbWgdQQQchbxw2Z%2B2E%2FfIk6xL7LvqwmtZyPAycd5C0ircae%2Bv3M%2FQE8O3ROPk9j8PWTcH3NhzDTa4%2Fji6817ysng0IfS26tB7LZS7u7nYT7%2FG7vtP8Gh5QZZHLcArTTynQF8GsWEIwVSpdUQY2YiseSEYMXuptH5Oj4Y9%2FFgSiqpirn7k4UQAII4d%2FJzNais%2BpGzZeWimFWBwg0FHPWhRn7E7FRipd7Rvhi25VzG7toG6Yysa44UvyyEIXQXxEbQueTbDqYVVKZuXkIf%2BXVGu4UdH%2BUK00fdEPmA4v1JuPsj8EqGMca1CgzdHDkVkbvEGbiZj11kMT0Dl5Qx8wOZAooJgUna5Na5uAnPJcqogsBydAyGDBwinMKXSiw6w%2FR3d3gP28Dk3NboWzsARbr85Yixl4iKC%2Bu1AagJL1LXQeeEHdzJN4978NMuNjjMvOoIMrWC3xMWrgVOIND7QCIFFWpRhsxzaFa4VfCofqhIw6J2OvQY6pgHjNCNvhNKpH0BhOXN7EhGZ8%2B9S4YvrWO7ns%2FSeJ66ocJDLpnCu7DbpO0QdyXBUEJ48nWygfJl4uB8crr8xsW3UxqugcH4VsuMeUT56Gz09mlrIih1onYb4BdPpfBOox%2FMzDg524xGvdvYfC1J7QkETbEWt0gZVCQnvFXMwrOnzL6Jiod%2BTcci646ivKfvSTuWhNf6K3gRADvE2odykljVgqEoKLp9O&X-Amz-Signature=0811ba67e42d413c629407c27722e8d9c40193054d3df00bad25ba4cc1fa6ba6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ2PUFID%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIFDpG3FzsMXJTwVNSCScWw0DfeJh4P9goZSBTDwBDm0LAiEAmsPdp1C2djB6XX0z7e19GrnXKPOoO7Dn507U4glJ%2Br0q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDK92BiJO%2B6SX19hRVCrcAyKQ8AERFr3jiiL2XB1fXIaA5wjYVTVS8QB8Yo%2BPNfGsArjLxkH2bQwsES93qB6x1z7EMNg4ilEBCDxSBv2%2BHNVwjEBDbnkbGIwpeAHiAaMfZZch4wUExKfP523XoNGrKTqm%2FzfWvpZCEdsKsD7ynvPdVvYd2NboYaG9ih%2FZTyvENRPt6NKCaQQKqZH8RRmdDyxDb1HYuE2lpERsJtkiC%2BzQ7uLzcXuhVdzuyXzHuFxblV%2Bv7Et7ATk2YqGmLJah8t0wuvXnnbzwRfuhkU%2Baek0o6OUi9C7XQEu0ChM%2BOdbF8lx0hlkAN1287NXQdfMTmzKAB9675RruMILGb3w5zRzIMV9MgNwQrgMFgfPBoWpsQ2WQi0OOnba2rJzz5xOyrQUL1dVp0O7dYL0SUqajE33trbvh52OiF16zFYTB9mUE%2BqXAj11RVYHBDOm5YCgdhH7CAvo%2FEjRnoZRz7qvVP3SCemn%2B5TlCh8iGt8vXqWZybC3oKE%2FeaEPKlv%2F31myaI1Eti3iMMS0zeIiv6oPhyxoj%2FXV9ugCS0cjF9lZikaR%2FDluTEnSSUbFwSJnEaPIcbm9ajimomhEka3OxXkdnxO%2FxQarXNF%2FWOt7TYCXOgIQNX%2F%2Fte962JOtXHDw8MK%2Bdjr0GOqUBP9UC8jeYAP9pfW5J89kxNG%2BUS1BqoSKz1777XGe15dmnUswyW%2BxDcDiqZ%2FQlsKiRR5aP74LihaPYIJcRttZrqBD2EJNH%2FltAQiVL9ui797JqhA7Aye7h1F%2B0Dof3%2F9hOTVGt5HGjP6I5m5sJP8e7dRExigosGg7v0vI6WLwzsN2ViZPFqwYH6SB%2F67e36cVzd26G14QEEmd54CIbGw%2BOK7TGNuOW&X-Amz-Signature=fa6afb46a66e26369f3e418b1d9503ea3f22de2109f479f672d344b7e9ffcfb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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