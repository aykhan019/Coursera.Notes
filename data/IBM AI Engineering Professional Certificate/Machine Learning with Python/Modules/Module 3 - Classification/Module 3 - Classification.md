

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GRBQLQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIHlHy0546pSgA39s%2BprpCXZwXBci%2Bf52VBwn8yYawrc2Ah9h%2BkUq5gBFJlsoQ7PuDYGzD8%2Fjo4vUyV1tJSy3TygHKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVoKiJwkxVXowd44q3AOSq3LAn03NVJkSzMmipn%2BM%2BCWwVBbVt%2FuazZR3ZtoFLIS27QRy0SnTfa9TDVoIQOIgRIqWCCjcMB8k0YqLOzflW08EToi0uSoth10fLSkvTewS2EUH5OKs1%2FMEZEmsngM3z%2F1pPwCMZzkIoxLK5M%2Fqw0iXY7WVcIjiIXkAPgjA7xhnN9tihGh6nktAh4eR%2BPt3D2SIctZo2tW4T%2F0Onlb%2FltxOFYOVDRUuoqYimV%2F84I9F58WTMxqwjoKRrkl3o%2B5w6xvHQ%2FBAnUCCsqlwsxu9jSQ6OoYhlvRelEpZaEEf1jl2f6cObSUoUa%2B2XmoDS77LKu8RADlWdcvxF7V92%2F64p%2FMmK6ncRE3XlOIeRSn94%2Bd%2FSNOiHLHg8EGQl0WX86dbF9V1koVQsmGkS%2BGzSbCoDmfeejkuTCIdOFz72l59Zzxo7YFrPzLkOCCAanGZy5ZZ2FD07ArqgfQ3rA92vZU4xAhJbJ1avGFlR04Q9H8hoFLrgKPriSzhoRrEVAtIP1%2FwUSeSJhhFmJGZdKrFNAAdTVZlRcnUjn7qEs0FMJllB1snLfj0%2BIaOP6kmHZnHBG9lyjl3V7WlmSt8Loe%2B5rW%2F9IyQqs38slDXGMLDrLlEnkffWvZax5nMmZoSmTCNv4C9BjqnAXinwz3d7IQ2NlOCwBRqUmqb%2BoNEp8X7FOAL8maJG%2FIE6bzwf6EmXtMwY8N2hGYUNXcuGcVowEC%2BwUkiam4Mly0VIZYC8qA6Gghr8YvYX39AaGQD1%2BfAKyKHwm%2F2jUWdGJNVUr2b4Ry1dRairlf1IzJONcFm2nWIxIp3v2mbaZZ7s65H8%2B%2FVfKRgMkydzZW%2BEy6KerQJQStnuPItpAT%2FO5%2BHWW7PatmJ&X-Amz-Signature=e19b26a00c14ad8e5cdd350c037dca9703d664adf41e646024b1f64b5065f6de&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GRBQLQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIHlHy0546pSgA39s%2BprpCXZwXBci%2Bf52VBwn8yYawrc2Ah9h%2BkUq5gBFJlsoQ7PuDYGzD8%2Fjo4vUyV1tJSy3TygHKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVoKiJwkxVXowd44q3AOSq3LAn03NVJkSzMmipn%2BM%2BCWwVBbVt%2FuazZR3ZtoFLIS27QRy0SnTfa9TDVoIQOIgRIqWCCjcMB8k0YqLOzflW08EToi0uSoth10fLSkvTewS2EUH5OKs1%2FMEZEmsngM3z%2F1pPwCMZzkIoxLK5M%2Fqw0iXY7WVcIjiIXkAPgjA7xhnN9tihGh6nktAh4eR%2BPt3D2SIctZo2tW4T%2F0Onlb%2FltxOFYOVDRUuoqYimV%2F84I9F58WTMxqwjoKRrkl3o%2B5w6xvHQ%2FBAnUCCsqlwsxu9jSQ6OoYhlvRelEpZaEEf1jl2f6cObSUoUa%2B2XmoDS77LKu8RADlWdcvxF7V92%2F64p%2FMmK6ncRE3XlOIeRSn94%2Bd%2FSNOiHLHg8EGQl0WX86dbF9V1koVQsmGkS%2BGzSbCoDmfeejkuTCIdOFz72l59Zzxo7YFrPzLkOCCAanGZy5ZZ2FD07ArqgfQ3rA92vZU4xAhJbJ1avGFlR04Q9H8hoFLrgKPriSzhoRrEVAtIP1%2FwUSeSJhhFmJGZdKrFNAAdTVZlRcnUjn7qEs0FMJllB1snLfj0%2BIaOP6kmHZnHBG9lyjl3V7WlmSt8Loe%2B5rW%2F9IyQqs38slDXGMLDrLlEnkffWvZax5nMmZoSmTCNv4C9BjqnAXinwz3d7IQ2NlOCwBRqUmqb%2BoNEp8X7FOAL8maJG%2FIE6bzwf6EmXtMwY8N2hGYUNXcuGcVowEC%2BwUkiam4Mly0VIZYC8qA6Gghr8YvYX39AaGQD1%2BfAKyKHwm%2F2jUWdGJNVUr2b4Ry1dRairlf1IzJONcFm2nWIxIp3v2mbaZZ7s65H8%2B%2FVfKRgMkydzZW%2BEy6KerQJQStnuPItpAT%2FO5%2BHWW7PatmJ&X-Amz-Signature=569c42f84c1f7a583c03f5098e919235e0ba59a7e4bfeb220ac160955dbed644&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GRBQLQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIHlHy0546pSgA39s%2BprpCXZwXBci%2Bf52VBwn8yYawrc2Ah9h%2BkUq5gBFJlsoQ7PuDYGzD8%2Fjo4vUyV1tJSy3TygHKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVoKiJwkxVXowd44q3AOSq3LAn03NVJkSzMmipn%2BM%2BCWwVBbVt%2FuazZR3ZtoFLIS27QRy0SnTfa9TDVoIQOIgRIqWCCjcMB8k0YqLOzflW08EToi0uSoth10fLSkvTewS2EUH5OKs1%2FMEZEmsngM3z%2F1pPwCMZzkIoxLK5M%2Fqw0iXY7WVcIjiIXkAPgjA7xhnN9tihGh6nktAh4eR%2BPt3D2SIctZo2tW4T%2F0Onlb%2FltxOFYOVDRUuoqYimV%2F84I9F58WTMxqwjoKRrkl3o%2B5w6xvHQ%2FBAnUCCsqlwsxu9jSQ6OoYhlvRelEpZaEEf1jl2f6cObSUoUa%2B2XmoDS77LKu8RADlWdcvxF7V92%2F64p%2FMmK6ncRE3XlOIeRSn94%2Bd%2FSNOiHLHg8EGQl0WX86dbF9V1koVQsmGkS%2BGzSbCoDmfeejkuTCIdOFz72l59Zzxo7YFrPzLkOCCAanGZy5ZZ2FD07ArqgfQ3rA92vZU4xAhJbJ1avGFlR04Q9H8hoFLrgKPriSzhoRrEVAtIP1%2FwUSeSJhhFmJGZdKrFNAAdTVZlRcnUjn7qEs0FMJllB1snLfj0%2BIaOP6kmHZnHBG9lyjl3V7WlmSt8Loe%2B5rW%2F9IyQqs38slDXGMLDrLlEnkffWvZax5nMmZoSmTCNv4C9BjqnAXinwz3d7IQ2NlOCwBRqUmqb%2BoNEp8X7FOAL8maJG%2FIE6bzwf6EmXtMwY8N2hGYUNXcuGcVowEC%2BwUkiam4Mly0VIZYC8qA6Gghr8YvYX39AaGQD1%2BfAKyKHwm%2F2jUWdGJNVUr2b4Ry1dRairlf1IzJONcFm2nWIxIp3v2mbaZZ7s65H8%2B%2FVfKRgMkydzZW%2BEy6KerQJQStnuPItpAT%2FO5%2BHWW7PatmJ&X-Amz-Signature=aa9a4917cf646be1733e2c1f63298756ee8bf63ee057b5abac814b33108fb374&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHHWQ4GA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDNRtNEuVRiqFlqZH7qcmzzRicdI9agN1lgBAxiaFtCwQIgS9QVqeNt30kFVnn1DDgOaMyWNunHJDtoy0mdpohrfxsqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO810Ki5UWlaR3310SrcA1tnHlkmAtOBNOI67uiK%2BvWHOMi7sgKiu%2BFpFRwpyXQAsDOWarHwU%2BjFZsa8oIYXajkXS5nS2TCuZETQo6GvZPFq%2FgcroBw8839ivWVdZLMPpFWExwLG8TckeQaJGV68fXTIDRLbOLhz%2BGAphbigbTNvAkn8PByA0U6Oc50NuOKWruXCwB7gy7oxltEdxr0G9kY5kG1lK7LdgVMOF%2BoH6zGGM3cdW15SiJNWqm118K8cvwD20bj2VPcvJlYkXC2uGEEs3wM6EgmHnupLMpTuWvlLXW%2BF5NBq%2BR1lj0GnfbHsHE2QFCx1kkPv2GN%2FNi75C1WzlcvNCczHcId%2FKAVhPapW3vTzDFN%2FLnlc4uat3AdO%2BKyPEqohQ7uHIhhiEZ6rxayl4OISxI%2B7Dj2z6EZz7ZYMr0u7E3tmB1T%2FQspP4SaKGZHMKMPl7iOf5tdGhdkGFxT4DJ3PLAnt9TugfdUECarPmaQk6nzmAF20ZWvMOQJxWA2%2B09mhhMCuyJSdJL9yNmMxgPVGwoxwsgtX%2BQYNiMO0YPu9ghh3znPLSHGKM7pOeyZCdbB9Llvbt3z5VlqHyrN9SHYVVxPfOKFJ1Vtd29RE6KVoBFUBtSwDGY5FrNFDFs%2FFDzvXa88XbFrRML%2B%2FgL0GOqUBlpOJluMYTtLZ9os60l6XAgKo8wiYFVavTpqKEAyerPyEf02y4bRsJjRDCf6ee%2Bz8e9nxtm05lzX9QPrH6F6zLZcObat4ZBOhbivVio57%2FGEGBCkHAnwyS3l%2BRIUJUyuh2wO9YauLEkeshMNEeXYZe%2FoUc50DZdZVv6%2BRANi4ZyYL9jdXG%2BIHvk9HnMmPUB%2FH8WmczH2lL%2B98Aehiiqp6SBEEaMmB&X-Amz-Signature=eb4ac5d6cc394fcfdbaf5bd5ec08964cdc3b24850a6f09a58c3a1f292256c10a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHHWQ4GA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDNRtNEuVRiqFlqZH7qcmzzRicdI9agN1lgBAxiaFtCwQIgS9QVqeNt30kFVnn1DDgOaMyWNunHJDtoy0mdpohrfxsqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO810Ki5UWlaR3310SrcA1tnHlkmAtOBNOI67uiK%2BvWHOMi7sgKiu%2BFpFRwpyXQAsDOWarHwU%2BjFZsa8oIYXajkXS5nS2TCuZETQo6GvZPFq%2FgcroBw8839ivWVdZLMPpFWExwLG8TckeQaJGV68fXTIDRLbOLhz%2BGAphbigbTNvAkn8PByA0U6Oc50NuOKWruXCwB7gy7oxltEdxr0G9kY5kG1lK7LdgVMOF%2BoH6zGGM3cdW15SiJNWqm118K8cvwD20bj2VPcvJlYkXC2uGEEs3wM6EgmHnupLMpTuWvlLXW%2BF5NBq%2BR1lj0GnfbHsHE2QFCx1kkPv2GN%2FNi75C1WzlcvNCczHcId%2FKAVhPapW3vTzDFN%2FLnlc4uat3AdO%2BKyPEqohQ7uHIhhiEZ6rxayl4OISxI%2B7Dj2z6EZz7ZYMr0u7E3tmB1T%2FQspP4SaKGZHMKMPl7iOf5tdGhdkGFxT4DJ3PLAnt9TugfdUECarPmaQk6nzmAF20ZWvMOQJxWA2%2B09mhhMCuyJSdJL9yNmMxgPVGwoxwsgtX%2BQYNiMO0YPu9ghh3znPLSHGKM7pOeyZCdbB9Llvbt3z5VlqHyrN9SHYVVxPfOKFJ1Vtd29RE6KVoBFUBtSwDGY5FrNFDFs%2FFDzvXa88XbFrRML%2B%2FgL0GOqUBlpOJluMYTtLZ9os60l6XAgKo8wiYFVavTpqKEAyerPyEf02y4bRsJjRDCf6ee%2Bz8e9nxtm05lzX9QPrH6F6zLZcObat4ZBOhbivVio57%2FGEGBCkHAnwyS3l%2BRIUJUyuh2wO9YauLEkeshMNEeXYZe%2FoUc50DZdZVv6%2BRANi4ZyYL9jdXG%2BIHvk9HnMmPUB%2FH8WmczH2lL%2B98Aehiiqp6SBEEaMmB&X-Amz-Signature=a86a2fed715ede18c32ef81a2c06fe95a0ce052542ef2ccc3757af3370cc67c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GRBQLQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIHlHy0546pSgA39s%2BprpCXZwXBci%2Bf52VBwn8yYawrc2Ah9h%2BkUq5gBFJlsoQ7PuDYGzD8%2Fjo4vUyV1tJSy3TygHKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwjVoKiJwkxVXowd44q3AOSq3LAn03NVJkSzMmipn%2BM%2BCWwVBbVt%2FuazZR3ZtoFLIS27QRy0SnTfa9TDVoIQOIgRIqWCCjcMB8k0YqLOzflW08EToi0uSoth10fLSkvTewS2EUH5OKs1%2FMEZEmsngM3z%2F1pPwCMZzkIoxLK5M%2Fqw0iXY7WVcIjiIXkAPgjA7xhnN9tihGh6nktAh4eR%2BPt3D2SIctZo2tW4T%2F0Onlb%2FltxOFYOVDRUuoqYimV%2F84I9F58WTMxqwjoKRrkl3o%2B5w6xvHQ%2FBAnUCCsqlwsxu9jSQ6OoYhlvRelEpZaEEf1jl2f6cObSUoUa%2B2XmoDS77LKu8RADlWdcvxF7V92%2F64p%2FMmK6ncRE3XlOIeRSn94%2Bd%2FSNOiHLHg8EGQl0WX86dbF9V1koVQsmGkS%2BGzSbCoDmfeejkuTCIdOFz72l59Zzxo7YFrPzLkOCCAanGZy5ZZ2FD07ArqgfQ3rA92vZU4xAhJbJ1avGFlR04Q9H8hoFLrgKPriSzhoRrEVAtIP1%2FwUSeSJhhFmJGZdKrFNAAdTVZlRcnUjn7qEs0FMJllB1snLfj0%2BIaOP6kmHZnHBG9lyjl3V7WlmSt8Loe%2B5rW%2F9IyQqs38slDXGMLDrLlEnkffWvZax5nMmZoSmTCNv4C9BjqnAXinwz3d7IQ2NlOCwBRqUmqb%2BoNEp8X7FOAL8maJG%2FIE6bzwf6EmXtMwY8N2hGYUNXcuGcVowEC%2BwUkiam4Mly0VIZYC8qA6Gghr8YvYX39AaGQD1%2BfAKyKHwm%2F2jUWdGJNVUr2b4Ry1dRairlf1IzJONcFm2nWIxIp3v2mbaZZ7s65H8%2B%2FVfKRgMkydzZW%2BEy6KerQJQStnuPItpAT%2FO5%2BHWW7PatmJ&X-Amz-Signature=46be3b234755feb1d4aadeca2600592a0780a47918413b28f7c72dc76c6c835b&X-Amz-SignedHeaders=host&x-id=GetObject)
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