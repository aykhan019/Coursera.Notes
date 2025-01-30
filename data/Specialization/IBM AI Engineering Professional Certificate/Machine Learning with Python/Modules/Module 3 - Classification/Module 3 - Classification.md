

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSYVOPM2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGyv2BRc8QOPhW9kmJ15f%2Bai9pQEk9S6LXq%2B58M%2FxBpwIhAKJ15L6tY%2B30OUumOpsMjZqL9mO5HXFRC3pNBagTvtLUKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxu1kXMG3IWGp8B948q3AOxQb%2BpZTcD1C1IZ4Jq9xAxfy9jVcJjoUYJMOFSBp2BIhZyCnR6lur1E%2BN1xi2DAY4CdB%2BOFIKXzW99viMSsJK5appdy6Ky0bT6UIAeTGiILUlJl3Hu5owPI8lniJxutPnQttWSHuM7FlO8s36%2BxZXCyye2IFgcGnDKCd%2FuKBhxAZ9QXMAYzQQcKs1IVTrDH6UJvLlnsHrwxGS1n4ZKTUVrNmQVEdm7DFVn%2FfCqJH251%2Fahp4f6m8exiMZvZ7CQDdBErABLG3sRdLwzdYBLl72JUgDwfGxA5WwL9fGGLuMQePQcdU%2FV2W21He9lD%2FidZ1jdwtrEM8ZLWhKjIJJW%2BRm%2FmdnHlpEmeLR0kgqALt%2B0goqf0DwvHI%2FcHWpbFRC9XC2IuKlelvYrXaFuLVDtfYdyxLeVv5AwM%2F7hJmmBUKgbFxlwbD3kddRMl7ackjZDG8r49zYoXzk3E9eg7nf0WaLO2A8txTKKrL5Gpp%2FWYTiceIwTDWGwBcRMgc82Hlk6YPXFuCyPccznujwJloDcaTIMF3VeqXKlTNSIzVD9oQpsBmLX%2FKaGw7tBz0viL8PPGOpFE0aPu%2BxRe6UyTIzIY4lF1XU4X1QEzF70we0vWBcWYGjYn%2B48J6ve4ckIyDCv%2Fe%2B8BjqkAb4IX6Ga2IfeVk8SoxquBsu3PuGYpcpuxqSyf0bjNn3Mv%2BYbWR4%2B61ehd1vk1RNcnbGFMS3ATGx0UONKEFGqZeWEJaY3Sc2FxQIfurd7IRpvqp4nQvj8e%2BR7TJIaPB0HT%2FiV%2FvE4caZFR1Snq%2BOPGNxVcn3s35rmPN96EPIMcuCg6Mgx7f9ngi81c%2FXLc6%2BPM7JOfNPJlO68n4sKq7NZKolDDnB9&X-Amz-Signature=f576575f8c44f87a10d073de6ece72b13abcead935c3a05add8169b002d4577f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSYVOPM2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGyv2BRc8QOPhW9kmJ15f%2Bai9pQEk9S6LXq%2B58M%2FxBpwIhAKJ15L6tY%2B30OUumOpsMjZqL9mO5HXFRC3pNBagTvtLUKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxu1kXMG3IWGp8B948q3AOxQb%2BpZTcD1C1IZ4Jq9xAxfy9jVcJjoUYJMOFSBp2BIhZyCnR6lur1E%2BN1xi2DAY4CdB%2BOFIKXzW99viMSsJK5appdy6Ky0bT6UIAeTGiILUlJl3Hu5owPI8lniJxutPnQttWSHuM7FlO8s36%2BxZXCyye2IFgcGnDKCd%2FuKBhxAZ9QXMAYzQQcKs1IVTrDH6UJvLlnsHrwxGS1n4ZKTUVrNmQVEdm7DFVn%2FfCqJH251%2Fahp4f6m8exiMZvZ7CQDdBErABLG3sRdLwzdYBLl72JUgDwfGxA5WwL9fGGLuMQePQcdU%2FV2W21He9lD%2FidZ1jdwtrEM8ZLWhKjIJJW%2BRm%2FmdnHlpEmeLR0kgqALt%2B0goqf0DwvHI%2FcHWpbFRC9XC2IuKlelvYrXaFuLVDtfYdyxLeVv5AwM%2F7hJmmBUKgbFxlwbD3kddRMl7ackjZDG8r49zYoXzk3E9eg7nf0WaLO2A8txTKKrL5Gpp%2FWYTiceIwTDWGwBcRMgc82Hlk6YPXFuCyPccznujwJloDcaTIMF3VeqXKlTNSIzVD9oQpsBmLX%2FKaGw7tBz0viL8PPGOpFE0aPu%2BxRe6UyTIzIY4lF1XU4X1QEzF70we0vWBcWYGjYn%2B48J6ve4ckIyDCv%2Fe%2B8BjqkAb4IX6Ga2IfeVk8SoxquBsu3PuGYpcpuxqSyf0bjNn3Mv%2BYbWR4%2B61ehd1vk1RNcnbGFMS3ATGx0UONKEFGqZeWEJaY3Sc2FxQIfurd7IRpvqp4nQvj8e%2BR7TJIaPB0HT%2FiV%2FvE4caZFR1Snq%2BOPGNxVcn3s35rmPN96EPIMcuCg6Mgx7f9ngi81c%2FXLc6%2BPM7JOfNPJlO68n4sKq7NZKolDDnB9&X-Amz-Signature=c1ab47c59fede61b23bb9812126e1578442368ee6c55d44b616b3cfb63e2d6b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSYVOPM2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGyv2BRc8QOPhW9kmJ15f%2Bai9pQEk9S6LXq%2B58M%2FxBpwIhAKJ15L6tY%2B30OUumOpsMjZqL9mO5HXFRC3pNBagTvtLUKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxu1kXMG3IWGp8B948q3AOxQb%2BpZTcD1C1IZ4Jq9xAxfy9jVcJjoUYJMOFSBp2BIhZyCnR6lur1E%2BN1xi2DAY4CdB%2BOFIKXzW99viMSsJK5appdy6Ky0bT6UIAeTGiILUlJl3Hu5owPI8lniJxutPnQttWSHuM7FlO8s36%2BxZXCyye2IFgcGnDKCd%2FuKBhxAZ9QXMAYzQQcKs1IVTrDH6UJvLlnsHrwxGS1n4ZKTUVrNmQVEdm7DFVn%2FfCqJH251%2Fahp4f6m8exiMZvZ7CQDdBErABLG3sRdLwzdYBLl72JUgDwfGxA5WwL9fGGLuMQePQcdU%2FV2W21He9lD%2FidZ1jdwtrEM8ZLWhKjIJJW%2BRm%2FmdnHlpEmeLR0kgqALt%2B0goqf0DwvHI%2FcHWpbFRC9XC2IuKlelvYrXaFuLVDtfYdyxLeVv5AwM%2F7hJmmBUKgbFxlwbD3kddRMl7ackjZDG8r49zYoXzk3E9eg7nf0WaLO2A8txTKKrL5Gpp%2FWYTiceIwTDWGwBcRMgc82Hlk6YPXFuCyPccznujwJloDcaTIMF3VeqXKlTNSIzVD9oQpsBmLX%2FKaGw7tBz0viL8PPGOpFE0aPu%2BxRe6UyTIzIY4lF1XU4X1QEzF70we0vWBcWYGjYn%2B48J6ve4ckIyDCv%2Fe%2B8BjqkAb4IX6Ga2IfeVk8SoxquBsu3PuGYpcpuxqSyf0bjNn3Mv%2BYbWR4%2B61ehd1vk1RNcnbGFMS3ATGx0UONKEFGqZeWEJaY3Sc2FxQIfurd7IRpvqp4nQvj8e%2BR7TJIaPB0HT%2FiV%2FvE4caZFR1Snq%2BOPGNxVcn3s35rmPN96EPIMcuCg6Mgx7f9ngi81c%2FXLc6%2BPM7JOfNPJlO68n4sKq7NZKolDDnB9&X-Amz-Signature=68e978fbef394ce200e12c102a8d1958e7df3b6c19ad06c8b7f0fdf8fc06dac4&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IZJEGSQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfkLmNR5Wfxl9rRAGEJAMaJDurzqs2zYRtTT9KLFsZlwIgRImsVQpRUOnmo%2BmDKNQi%2BEFEoz0teaJvekDSTh%2F2p%2BUqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2F9IEp7r92mbP49XircA88A6CcrHUPOzdDmdvLMtgzuptNJ9RZKYTIvV3zZ7yYXDWR5f%2F%2FMVcskZL2ZeS0Rt%2BgudT%2B1wXJk5bPx2qPSO0IcMygjUKo4tp%2BqNw9mo%2BxBBSo%2BbgPfl2fxx58VEmM6NO7juT4pEMoW4yQ8FG9TIy4wlPq%2BCF%2FGwCtHSPEzXpqUwIbYi%2BtwabF8pNsgWlPp%2Fc4tcGGaIg1ARpU%2BPDrIuTscUZf7inDNCIlLPji9fnOAECWXVH05lWZDjDBMlTTq3cFhr0StN0BQXUxlDhHp1nwInyf1ygg8JSF47m%2BKVSZoL8z6Mcob4SqZyPb62LQyrOLjsI23aYV9oAHisKiZ%2BY1NkTuyganH6pG%2Bz0DY0EeANtBgxG8Mvli8yJIb%2FBCz9JUy4Uz7gOfo%2Fz2vUzoVnhp32VmRgzArhrXLR1O6b2vEwU6LHCaZygFu%2FC01MGeicaxOfpv%2BXMbsetb2ywYYs3zAZNMoc8MwQbDglV0Kpl5s6dH8Rm%2FJdnEn1i%2FXJuGsGRzVptNw%2FlUt7O6GKD1V%2F6QAO%2Fpdyya4URFH0VxZDBgzG%2BLXojgo7NgPdGwQuSeMAtJvpaSX%2F12MEuDn0vdW29I3p5BLYYzQCmRg1bLENy%2BaVaYT2sHFp4PDnJCqMKP977wGOqUBNigSRjq0wBIs5Lu51mEmT%2BuzjQpewHNkcb8m%2FHOoW1LFvHyJiTZgCibGRJ6SeGyrF92sssEp%2BYQCmIQg5ZUDWqwpVrkSlQD5F9Xe0EYkYnjlsesn%2BhdpuiCoyl%2B%2BlAXDaio5gtPhZ6tD2khNlY1%2FPHiI8NZwpNej%2BmW6cAiIoBDiHoTr2dDMcMDfdMlyn2zcxJ0TnILLcYs%2F025Om5V6H2cZRYhk&X-Amz-Signature=dcfb90f0cec671572e5ee232a91537e99fb8c907685624323e229712b395683f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IZJEGSQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfkLmNR5Wfxl9rRAGEJAMaJDurzqs2zYRtTT9KLFsZlwIgRImsVQpRUOnmo%2BmDKNQi%2BEFEoz0teaJvekDSTh%2F2p%2BUqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2F9IEp7r92mbP49XircA88A6CcrHUPOzdDmdvLMtgzuptNJ9RZKYTIvV3zZ7yYXDWR5f%2F%2FMVcskZL2ZeS0Rt%2BgudT%2B1wXJk5bPx2qPSO0IcMygjUKo4tp%2BqNw9mo%2BxBBSo%2BbgPfl2fxx58VEmM6NO7juT4pEMoW4yQ8FG9TIy4wlPq%2BCF%2FGwCtHSPEzXpqUwIbYi%2BtwabF8pNsgWlPp%2Fc4tcGGaIg1ARpU%2BPDrIuTscUZf7inDNCIlLPji9fnOAECWXVH05lWZDjDBMlTTq3cFhr0StN0BQXUxlDhHp1nwInyf1ygg8JSF47m%2BKVSZoL8z6Mcob4SqZyPb62LQyrOLjsI23aYV9oAHisKiZ%2BY1NkTuyganH6pG%2Bz0DY0EeANtBgxG8Mvli8yJIb%2FBCz9JUy4Uz7gOfo%2Fz2vUzoVnhp32VmRgzArhrXLR1O6b2vEwU6LHCaZygFu%2FC01MGeicaxOfpv%2BXMbsetb2ywYYs3zAZNMoc8MwQbDglV0Kpl5s6dH8Rm%2FJdnEn1i%2FXJuGsGRzVptNw%2FlUt7O6GKD1V%2F6QAO%2Fpdyya4URFH0VxZDBgzG%2BLXojgo7NgPdGwQuSeMAtJvpaSX%2F12MEuDn0vdW29I3p5BLYYzQCmRg1bLENy%2BaVaYT2sHFp4PDnJCqMKP977wGOqUBNigSRjq0wBIs5Lu51mEmT%2BuzjQpewHNkcb8m%2FHOoW1LFvHyJiTZgCibGRJ6SeGyrF92sssEp%2BYQCmIQg5ZUDWqwpVrkSlQD5F9Xe0EYkYnjlsesn%2BhdpuiCoyl%2B%2BlAXDaio5gtPhZ6tD2khNlY1%2FPHiI8NZwpNej%2BmW6cAiIoBDiHoTr2dDMcMDfdMlyn2zcxJ0TnILLcYs%2F025Om5V6H2cZRYhk&X-Amz-Signature=fb6ced2dd88196f224896035f95d673689e393b5a9be19a17c8ef1ff5cfb5657&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSYVOPM2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGyv2BRc8QOPhW9kmJ15f%2Bai9pQEk9S6LXq%2B58M%2FxBpwIhAKJ15L6tY%2B30OUumOpsMjZqL9mO5HXFRC3pNBagTvtLUKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxu1kXMG3IWGp8B948q3AOxQb%2BpZTcD1C1IZ4Jq9xAxfy9jVcJjoUYJMOFSBp2BIhZyCnR6lur1E%2BN1xi2DAY4CdB%2BOFIKXzW99viMSsJK5appdy6Ky0bT6UIAeTGiILUlJl3Hu5owPI8lniJxutPnQttWSHuM7FlO8s36%2BxZXCyye2IFgcGnDKCd%2FuKBhxAZ9QXMAYzQQcKs1IVTrDH6UJvLlnsHrwxGS1n4ZKTUVrNmQVEdm7DFVn%2FfCqJH251%2Fahp4f6m8exiMZvZ7CQDdBErABLG3sRdLwzdYBLl72JUgDwfGxA5WwL9fGGLuMQePQcdU%2FV2W21He9lD%2FidZ1jdwtrEM8ZLWhKjIJJW%2BRm%2FmdnHlpEmeLR0kgqALt%2B0goqf0DwvHI%2FcHWpbFRC9XC2IuKlelvYrXaFuLVDtfYdyxLeVv5AwM%2F7hJmmBUKgbFxlwbD3kddRMl7ackjZDG8r49zYoXzk3E9eg7nf0WaLO2A8txTKKrL5Gpp%2FWYTiceIwTDWGwBcRMgc82Hlk6YPXFuCyPccznujwJloDcaTIMF3VeqXKlTNSIzVD9oQpsBmLX%2FKaGw7tBz0viL8PPGOpFE0aPu%2BxRe6UyTIzIY4lF1XU4X1QEzF70we0vWBcWYGjYn%2B48J6ve4ckIyDCv%2Fe%2B8BjqkAb4IX6Ga2IfeVk8SoxquBsu3PuGYpcpuxqSyf0bjNn3Mv%2BYbWR4%2B61ehd1vk1RNcnbGFMS3ATGx0UONKEFGqZeWEJaY3Sc2FxQIfurd7IRpvqp4nQvj8e%2BR7TJIaPB0HT%2FiV%2FvE4caZFR1Snq%2BOPGNxVcn3s35rmPN96EPIMcuCg6Mgx7f9ngi81c%2FXLc6%2BPM7JOfNPJlO68n4sKq7NZKolDDnB9&X-Amz-Signature=7cef3d60053723e866437fd8e7a4cc583bc043819e9b9412cbcf365a62347322&X-Amz-SignedHeaders=host&x-id=GetObject)
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