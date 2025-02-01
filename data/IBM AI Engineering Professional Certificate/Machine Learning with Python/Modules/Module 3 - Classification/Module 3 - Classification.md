

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633TYUWUR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCaZcuiB3C1dG2lyiYf8smpjJj2bzVbttDA1afN1vqFWwIhAP9qIIyBGBMLonYhvoUdckGI%2BPzW723t2tIIIboFntNMKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzV0x%2FccYp9dMzQ0QMq3AOKOW73Yal%2BPOvsAdPlfEkIBSlB5bxFQn2fih6ZaVZqjIe0KAHf4L3pQP9F8ZC5hZge6pNnmTcNVmUMnd%2FrG0UbI0pW7FrNnLXsOnHD%2Fto3u9fGAkvj6yjAACzs8CMK%2FFz4Nji%2FuPL2OxVs5vEb%2F9fQkV%2FN8eH7JCE7P3gc%2Bof1QrbDgP2ixpSSAUVGAGQ33oGmkF%2B%2F46AucoTVaiA%2BzJIaig5nXuN76oc%2BkEOU9v%2Fne02prEKC%2B7yhYQSj%2BBeNZDGsU7GWNIbuZIg3dYJ0sJEwWMu17Yy2V5xYi7ApKtFQobHOfheL%2BiDsx8Jwu7zq8rNYyzj3IFrxptdwOiAoG84gOZyCH1bP0gfuOeDqVibumCgHaaS8bqz%2FXN%2FngKnEJA%2FXl9j6tNGNdhTHb4%2BqpF5l%2BQYLToOl0nMJu4GxIoF5DIc8Wly30q6RkjhEDGxjPibKnQGyWZ469WmUD%2FHp6tvQttX%2Frvv4diDJhOi8TFVYU5GUkrR6RCrQo7LWZO2iP0vh89jbfMUGXlSdW1DVdjSV3TVo5Sk7ulxraeRRsnSGam6SeWhhUC7EOWO7xb8oDML3GA2MtGFeqZer8tm7mcxnM6UtJR%2FfK1hY4LxPdgvLnheqvTwvmSurx8nt%2FTDJxvi8BjqkAdzKF1BChac6tsK65ZaNHrOjKWt%2Blq1l%2FolwTL%2BHcg%2BIVMr25oYXf5iH9hrfYRtIOhSM5zuMn%2BPRx02bX4%2BnV4gf95rXreIwesrIwmN5OtiFV7vUAE5DMZRvqMi9r9os2GVIbWXlmmvKv1S9GC%2BwDD6Uk9Q9k%2Bova29fkWN2itIxNAazYfa7wk7wJx3i23RLMc2YaQ%2Bbys0AoLnz8mfWoSxpw0ug&X-Amz-Signature=6c7a5e03984b274011e46159c9cf02f9980c3a200edf4a8f62415206fac13972&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633TYUWUR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCaZcuiB3C1dG2lyiYf8smpjJj2bzVbttDA1afN1vqFWwIhAP9qIIyBGBMLonYhvoUdckGI%2BPzW723t2tIIIboFntNMKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzV0x%2FccYp9dMzQ0QMq3AOKOW73Yal%2BPOvsAdPlfEkIBSlB5bxFQn2fih6ZaVZqjIe0KAHf4L3pQP9F8ZC5hZge6pNnmTcNVmUMnd%2FrG0UbI0pW7FrNnLXsOnHD%2Fto3u9fGAkvj6yjAACzs8CMK%2FFz4Nji%2FuPL2OxVs5vEb%2F9fQkV%2FN8eH7JCE7P3gc%2Bof1QrbDgP2ixpSSAUVGAGQ33oGmkF%2B%2F46AucoTVaiA%2BzJIaig5nXuN76oc%2BkEOU9v%2Fne02prEKC%2B7yhYQSj%2BBeNZDGsU7GWNIbuZIg3dYJ0sJEwWMu17Yy2V5xYi7ApKtFQobHOfheL%2BiDsx8Jwu7zq8rNYyzj3IFrxptdwOiAoG84gOZyCH1bP0gfuOeDqVibumCgHaaS8bqz%2FXN%2FngKnEJA%2FXl9j6tNGNdhTHb4%2BqpF5l%2BQYLToOl0nMJu4GxIoF5DIc8Wly30q6RkjhEDGxjPibKnQGyWZ469WmUD%2FHp6tvQttX%2Frvv4diDJhOi8TFVYU5GUkrR6RCrQo7LWZO2iP0vh89jbfMUGXlSdW1DVdjSV3TVo5Sk7ulxraeRRsnSGam6SeWhhUC7EOWO7xb8oDML3GA2MtGFeqZer8tm7mcxnM6UtJR%2FfK1hY4LxPdgvLnheqvTwvmSurx8nt%2FTDJxvi8BjqkAdzKF1BChac6tsK65ZaNHrOjKWt%2Blq1l%2FolwTL%2BHcg%2BIVMr25oYXf5iH9hrfYRtIOhSM5zuMn%2BPRx02bX4%2BnV4gf95rXreIwesrIwmN5OtiFV7vUAE5DMZRvqMi9r9os2GVIbWXlmmvKv1S9GC%2BwDD6Uk9Q9k%2Bova29fkWN2itIxNAazYfa7wk7wJx3i23RLMc2YaQ%2Bbys0AoLnz8mfWoSxpw0ug&X-Amz-Signature=ef1f8c3ac5706311b7362cc2be48196ecfc9f3c647905c4859d9698406dd88b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633TYUWUR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCaZcuiB3C1dG2lyiYf8smpjJj2bzVbttDA1afN1vqFWwIhAP9qIIyBGBMLonYhvoUdckGI%2BPzW723t2tIIIboFntNMKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzV0x%2FccYp9dMzQ0QMq3AOKOW73Yal%2BPOvsAdPlfEkIBSlB5bxFQn2fih6ZaVZqjIe0KAHf4L3pQP9F8ZC5hZge6pNnmTcNVmUMnd%2FrG0UbI0pW7FrNnLXsOnHD%2Fto3u9fGAkvj6yjAACzs8CMK%2FFz4Nji%2FuPL2OxVs5vEb%2F9fQkV%2FN8eH7JCE7P3gc%2Bof1QrbDgP2ixpSSAUVGAGQ33oGmkF%2B%2F46AucoTVaiA%2BzJIaig5nXuN76oc%2BkEOU9v%2Fne02prEKC%2B7yhYQSj%2BBeNZDGsU7GWNIbuZIg3dYJ0sJEwWMu17Yy2V5xYi7ApKtFQobHOfheL%2BiDsx8Jwu7zq8rNYyzj3IFrxptdwOiAoG84gOZyCH1bP0gfuOeDqVibumCgHaaS8bqz%2FXN%2FngKnEJA%2FXl9j6tNGNdhTHb4%2BqpF5l%2BQYLToOl0nMJu4GxIoF5DIc8Wly30q6RkjhEDGxjPibKnQGyWZ469WmUD%2FHp6tvQttX%2Frvv4diDJhOi8TFVYU5GUkrR6RCrQo7LWZO2iP0vh89jbfMUGXlSdW1DVdjSV3TVo5Sk7ulxraeRRsnSGam6SeWhhUC7EOWO7xb8oDML3GA2MtGFeqZer8tm7mcxnM6UtJR%2FfK1hY4LxPdgvLnheqvTwvmSurx8nt%2FTDJxvi8BjqkAdzKF1BChac6tsK65ZaNHrOjKWt%2Blq1l%2FolwTL%2BHcg%2BIVMr25oYXf5iH9hrfYRtIOhSM5zuMn%2BPRx02bX4%2BnV4gf95rXreIwesrIwmN5OtiFV7vUAE5DMZRvqMi9r9os2GVIbWXlmmvKv1S9GC%2BwDD6Uk9Q9k%2Bova29fkWN2itIxNAazYfa7wk7wJx3i23RLMc2YaQ%2Bbys0AoLnz8mfWoSxpw0ug&X-Amz-Signature=da3a508a2f6d7f0143c8a5ccf64f2af52b6e972e310282a81b65b375db8d28cc&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AQ2OFNC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKQRmrywFrx5sMwi65HgKh04VxfBiRjoqrt2WzSvGlqgIhAL26DHiQSTp%2FtKf56eAWxKOjG%2FJoNLaXcMvUacQ%2F2z2RKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzgL04k%2Fo3UVCpvCdMq3AO%2BxWYRb03VCmFKw9kbp1VzJWH8ADGWI%2BBwyreUotKdoMUGZ1Z3gQlVyYGJh45o%2BXhWReJCwhvdOR33GeuKj8NyTRaCSjIj1yWZ%2Bj11ZGJk52ru08TsGFaLqn30qfoEIfz2Zr7hLtgKQaNalImaiucDvpoNgkWKXZiQMUQZlXRn2dPlqUL69NYVFtpl9Un5bU8XlJEM5dY76YsmuOMUh6CO0%2B6%2B4UTiZjXZIIW%2BZj923O8xyY2lEy2ZvoHlFA7vjs4WHYD1%2F3ZoEA9x%2F0MhxmI%2Fyydxc%2BVCXUNFfPG7QGGfSu1nM%2FaGYdJKZPCrdpPvRYUzw9XQbext8bBv%2FQzE9ReCAuGJss1NGouvHZBcrsHMLV2C6wH5zqs9ZpBureff32icPkQaW9pU0Kx5gCt2adPup2kqaBVrd%2F%2Fkxj0XxcRaGzrznj3reJ%2BqITcq7O8MTBkBo%2BZmxmPVlfZQ43Q24FYkScMet4RIpOY4lhDnW1A5VRCT0ZmmB5rjwUFG4ulyIzL8tktgCRQIU2LZkWyYecawroEDJmwvNlB89Jq3qgJoiRDluSNU%2F2P0e3gcjWa2Mb2OBMnwBGRi7dw7JElMIggs8fSig2atKac9CkDdU9AP3f5%2B%2Bfc3kMyAnrNFCTDax%2Fi8BjqkAXlc20WU1oIP265slNardh%2BGVGPHihgaJKt4R25N5Omx9GSWPGw6I48vrT9o7moTrf1REDj0SMULYVW3%2BszVWbb%2FJz%2BuQKtl7BqnYBUQK%2FtNDvNQJXNMHeaU802ssYtUiPwQ%2BCw7rLTAiSPhsosHb0bGCEnwPUYSP98RnayKR3t5iEkpJqHg9VNnTuOehqIXkaBVoEfSZwQvwKVER9tw6fvFBdwj&X-Amz-Signature=ad35cdb55606ec7b7110c6f9aeb2f20a4b30a3a0fbb37ad165b7441443edd881&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AQ2OFNC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDKQRmrywFrx5sMwi65HgKh04VxfBiRjoqrt2WzSvGlqgIhAL26DHiQSTp%2FtKf56eAWxKOjG%2FJoNLaXcMvUacQ%2F2z2RKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzgL04k%2Fo3UVCpvCdMq3AO%2BxWYRb03VCmFKw9kbp1VzJWH8ADGWI%2BBwyreUotKdoMUGZ1Z3gQlVyYGJh45o%2BXhWReJCwhvdOR33GeuKj8NyTRaCSjIj1yWZ%2Bj11ZGJk52ru08TsGFaLqn30qfoEIfz2Zr7hLtgKQaNalImaiucDvpoNgkWKXZiQMUQZlXRn2dPlqUL69NYVFtpl9Un5bU8XlJEM5dY76YsmuOMUh6CO0%2B6%2B4UTiZjXZIIW%2BZj923O8xyY2lEy2ZvoHlFA7vjs4WHYD1%2F3ZoEA9x%2F0MhxmI%2Fyydxc%2BVCXUNFfPG7QGGfSu1nM%2FaGYdJKZPCrdpPvRYUzw9XQbext8bBv%2FQzE9ReCAuGJss1NGouvHZBcrsHMLV2C6wH5zqs9ZpBureff32icPkQaW9pU0Kx5gCt2adPup2kqaBVrd%2F%2Fkxj0XxcRaGzrznj3reJ%2BqITcq7O8MTBkBo%2BZmxmPVlfZQ43Q24FYkScMet4RIpOY4lhDnW1A5VRCT0ZmmB5rjwUFG4ulyIzL8tktgCRQIU2LZkWyYecawroEDJmwvNlB89Jq3qgJoiRDluSNU%2F2P0e3gcjWa2Mb2OBMnwBGRi7dw7JElMIggs8fSig2atKac9CkDdU9AP3f5%2B%2Bfc3kMyAnrNFCTDax%2Fi8BjqkAXlc20WU1oIP265slNardh%2BGVGPHihgaJKt4R25N5Omx9GSWPGw6I48vrT9o7moTrf1REDj0SMULYVW3%2BszVWbb%2FJz%2BuQKtl7BqnYBUQK%2FtNDvNQJXNMHeaU802ssYtUiPwQ%2BCw7rLTAiSPhsosHb0bGCEnwPUYSP98RnayKR3t5iEkpJqHg9VNnTuOehqIXkaBVoEfSZwQvwKVER9tw6fvFBdwj&X-Amz-Signature=e2bc48952c5fe34f939b9ee49743de59a7d18c78be99e1b3c96d183e9f8e0598&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633TYUWUR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T181741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCaZcuiB3C1dG2lyiYf8smpjJj2bzVbttDA1afN1vqFWwIhAP9qIIyBGBMLonYhvoUdckGI%2BPzW723t2tIIIboFntNMKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzV0x%2FccYp9dMzQ0QMq3AOKOW73Yal%2BPOvsAdPlfEkIBSlB5bxFQn2fih6ZaVZqjIe0KAHf4L3pQP9F8ZC5hZge6pNnmTcNVmUMnd%2FrG0UbI0pW7FrNnLXsOnHD%2Fto3u9fGAkvj6yjAACzs8CMK%2FFz4Nji%2FuPL2OxVs5vEb%2F9fQkV%2FN8eH7JCE7P3gc%2Bof1QrbDgP2ixpSSAUVGAGQ33oGmkF%2B%2F46AucoTVaiA%2BzJIaig5nXuN76oc%2BkEOU9v%2Fne02prEKC%2B7yhYQSj%2BBeNZDGsU7GWNIbuZIg3dYJ0sJEwWMu17Yy2V5xYi7ApKtFQobHOfheL%2BiDsx8Jwu7zq8rNYyzj3IFrxptdwOiAoG84gOZyCH1bP0gfuOeDqVibumCgHaaS8bqz%2FXN%2FngKnEJA%2FXl9j6tNGNdhTHb4%2BqpF5l%2BQYLToOl0nMJu4GxIoF5DIc8Wly30q6RkjhEDGxjPibKnQGyWZ469WmUD%2FHp6tvQttX%2Frvv4diDJhOi8TFVYU5GUkrR6RCrQo7LWZO2iP0vh89jbfMUGXlSdW1DVdjSV3TVo5Sk7ulxraeRRsnSGam6SeWhhUC7EOWO7xb8oDML3GA2MtGFeqZer8tm7mcxnM6UtJR%2FfK1hY4LxPdgvLnheqvTwvmSurx8nt%2FTDJxvi8BjqkAdzKF1BChac6tsK65ZaNHrOjKWt%2Blq1l%2FolwTL%2BHcg%2BIVMr25oYXf5iH9hrfYRtIOhSM5zuMn%2BPRx02bX4%2BnV4gf95rXreIwesrIwmN5OtiFV7vUAE5DMZRvqMi9r9os2GVIbWXlmmvKv1S9GC%2BwDD6Uk9Q9k%2Bova29fkWN2itIxNAazYfa7wk7wJx3i23RLMc2YaQ%2Bbys0AoLnz8mfWoSxpw0ug&X-Amz-Signature=df9f0406eef4cdbfc499ba2dd306530ea7a2557e522b57b197e93dade60fbf9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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