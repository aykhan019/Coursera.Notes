

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNQ6PW7Q%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIPOKolii%2BqWmC0F%2FLLRlPIus4HVn6uGPDn8t3WGrspQIgKJhIY44qaFqf%2B7ZzLclXeje%2BJkXQIFNJsI9JNxSQlQYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG88Mbbi3CarPkc2AyrcA4aGwX7g%2FuPU4L1pgll0IGUppkp1plUXsuQW9lxiRWrqHCZ9vO4L0rcg%2F2iu9h0nsHofg4yirIExn1gpzCO5YTNICsZOVpjB1M8J4i9hqDDbPYwOF6eaZeCHFfWOtIBWDTVw%2BAQXwp9hjY1EqYCGs%2F9ErfGMO1Cju5rsuZV51W5RCJZaC2oLL420lgdgleT3aQ%2Fcsi%2FAZGNE5FJIL%2Blipg5YokNYH%2BChgFqCfTGHMUZSMU30DzdPqlbs7b7%2B4V%2F4JBdvaDyoEsd%2BAfHiFH4SO%2BvH7jDawbZK%2BNRKzqe7lIf8ci0ZhrK3s3JYlhoGGPLoNr03xoILO%2BZNmC%2FKA5rFVU%2FID3X1BLfCON09kUaCuJn4MtjfotAF%2FTedI%2BoCPTq7VQoLIqZCNSmggd6t7jIorutMc%2FSf2ci1viXwjf8IhMGogNhQ1DawNl0a%2FAEwjeIeLhuAJxcQXFhswiFmK%2B4USIOzcMoKBdGY%2BULzwfpLUNMoniMJZm4ID0te%2F07ucyYp5a2rphUE00f8ta1yB3ZCB6SEr3sCrQZYmL4R6DCl3BEwltfDcj4xRYGyAOaT2mT1Yh6c5ohO8ZNhg5aR43RkTPKpvIcLC9vM9dKq%2BsmUeedywJ8YVejXC3XOS8bhMMzI87wGOqUB8f5rHaQAjqK0yAqfhODNQhVkfbch%2Bkn2ErsmDuO3ctfy3Q%2BRjPBaFeCEwSfSlgt1HJSY01lbAZeW9wDe1MRCf1TCP3bA9CLr2cpU0AbrsKYALND66yxA7g1FlYWCRPl4DG52bhv4kZd4lHKOo7dJd2YzFruhVjfx29cD3EtjC6JWMjNgTglHUzKum7bTJ2CpKIMTLJzByHiuQKWY3FWIA3md6KXp&X-Amz-Signature=79d991e0b48cb6280dc5a27413aee8ce2a04c8f4214f04d7f3762f98d61048f7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNQ6PW7Q%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIPOKolii%2BqWmC0F%2FLLRlPIus4HVn6uGPDn8t3WGrspQIgKJhIY44qaFqf%2B7ZzLclXeje%2BJkXQIFNJsI9JNxSQlQYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG88Mbbi3CarPkc2AyrcA4aGwX7g%2FuPU4L1pgll0IGUppkp1plUXsuQW9lxiRWrqHCZ9vO4L0rcg%2F2iu9h0nsHofg4yirIExn1gpzCO5YTNICsZOVpjB1M8J4i9hqDDbPYwOF6eaZeCHFfWOtIBWDTVw%2BAQXwp9hjY1EqYCGs%2F9ErfGMO1Cju5rsuZV51W5RCJZaC2oLL420lgdgleT3aQ%2Fcsi%2FAZGNE5FJIL%2Blipg5YokNYH%2BChgFqCfTGHMUZSMU30DzdPqlbs7b7%2B4V%2F4JBdvaDyoEsd%2BAfHiFH4SO%2BvH7jDawbZK%2BNRKzqe7lIf8ci0ZhrK3s3JYlhoGGPLoNr03xoILO%2BZNmC%2FKA5rFVU%2FID3X1BLfCON09kUaCuJn4MtjfotAF%2FTedI%2BoCPTq7VQoLIqZCNSmggd6t7jIorutMc%2FSf2ci1viXwjf8IhMGogNhQ1DawNl0a%2FAEwjeIeLhuAJxcQXFhswiFmK%2B4USIOzcMoKBdGY%2BULzwfpLUNMoniMJZm4ID0te%2F07ucyYp5a2rphUE00f8ta1yB3ZCB6SEr3sCrQZYmL4R6DCl3BEwltfDcj4xRYGyAOaT2mT1Yh6c5ohO8ZNhg5aR43RkTPKpvIcLC9vM9dKq%2BsmUeedywJ8YVejXC3XOS8bhMMzI87wGOqUB8f5rHaQAjqK0yAqfhODNQhVkfbch%2Bkn2ErsmDuO3ctfy3Q%2BRjPBaFeCEwSfSlgt1HJSY01lbAZeW9wDe1MRCf1TCP3bA9CLr2cpU0AbrsKYALND66yxA7g1FlYWCRPl4DG52bhv4kZd4lHKOo7dJd2YzFruhVjfx29cD3EtjC6JWMjNgTglHUzKum7bTJ2CpKIMTLJzByHiuQKWY3FWIA3md6KXp&X-Amz-Signature=23e4b35db48c05820c1b31335789989324e95e9c67197ab885e99a75b31c144b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNQ6PW7Q%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIPOKolii%2BqWmC0F%2FLLRlPIus4HVn6uGPDn8t3WGrspQIgKJhIY44qaFqf%2B7ZzLclXeje%2BJkXQIFNJsI9JNxSQlQYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG88Mbbi3CarPkc2AyrcA4aGwX7g%2FuPU4L1pgll0IGUppkp1plUXsuQW9lxiRWrqHCZ9vO4L0rcg%2F2iu9h0nsHofg4yirIExn1gpzCO5YTNICsZOVpjB1M8J4i9hqDDbPYwOF6eaZeCHFfWOtIBWDTVw%2BAQXwp9hjY1EqYCGs%2F9ErfGMO1Cju5rsuZV51W5RCJZaC2oLL420lgdgleT3aQ%2Fcsi%2FAZGNE5FJIL%2Blipg5YokNYH%2BChgFqCfTGHMUZSMU30DzdPqlbs7b7%2B4V%2F4JBdvaDyoEsd%2BAfHiFH4SO%2BvH7jDawbZK%2BNRKzqe7lIf8ci0ZhrK3s3JYlhoGGPLoNr03xoILO%2BZNmC%2FKA5rFVU%2FID3X1BLfCON09kUaCuJn4MtjfotAF%2FTedI%2BoCPTq7VQoLIqZCNSmggd6t7jIorutMc%2FSf2ci1viXwjf8IhMGogNhQ1DawNl0a%2FAEwjeIeLhuAJxcQXFhswiFmK%2B4USIOzcMoKBdGY%2BULzwfpLUNMoniMJZm4ID0te%2F07ucyYp5a2rphUE00f8ta1yB3ZCB6SEr3sCrQZYmL4R6DCl3BEwltfDcj4xRYGyAOaT2mT1Yh6c5ohO8ZNhg5aR43RkTPKpvIcLC9vM9dKq%2BsmUeedywJ8YVejXC3XOS8bhMMzI87wGOqUB8f5rHaQAjqK0yAqfhODNQhVkfbch%2Bkn2ErsmDuO3ctfy3Q%2BRjPBaFeCEwSfSlgt1HJSY01lbAZeW9wDe1MRCf1TCP3bA9CLr2cpU0AbrsKYALND66yxA7g1FlYWCRPl4DG52bhv4kZd4lHKOo7dJd2YzFruhVjfx29cD3EtjC6JWMjNgTglHUzKum7bTJ2CpKIMTLJzByHiuQKWY3FWIA3md6KXp&X-Amz-Signature=31b133f78fbc198743db4314338a885c77658f2512b5d43c7ee4df6a4448f5fa&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEIA7J7B%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1r4dHUecehX2xM8JQtk1VDrQ2ykYL50sYa5VfEGCDbAiEA3iT%2BYK3tCjjM5yWF9V7EVsWts8iQzfoAdOcCgHNdAC8qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH05hvTY%2FsrYvjoXESrcA%2BgIL6HV4M3NvLfAhZqBOwPQKf6pEO%2FXCXUzNlcGj4JfUISNGpJVVMaa%2B8J5QI6xUmWmSpvgYDL7G4OSj29a0LIgjyExNP9HjeNBs%2F4eV%2FJiIPZACqBlK1wPNJylqmr4HV9E9ABFYOVGdcbP04LN8a6F1gCOA55oJtIagHMWwHiPaWRoc3qNc8uRhk9LFXCIh9D00p7f1yWr59RYh1pJRo6WJe6K4jtKI%2BmQ%2FYNX59jxWqeicrnUDn9j2olKIl0AJZAr8aKZe6OLYmSfrwnIEILpoGcwNP5Pm054EWZ%2BBpf%2BSRK4Ep1iN3mVDDjklu2RlMulZZDYOnrP6VQAQuE5w9o3jr3noVTGPa03tjZQg5rRyPblkWmhF17hpREs4x4GjLrZAn%2FOWHUI9EYZ8sSR3Ys9h2u3Yy8SzCWZRhD77mh1xR4gNKxf2uXIXvg1TbficEGBXJZYeqQ1haU%2F8tN18lh2cGoj6HZ2QxLpWBE6h7YOqrvQRyCVRffk8nw26teZn96gaEL8pWAQcIfg1xwMpzNqOJOwEiSnkYA0hwTB%2BcGclorf8VcAAkhd75ILZS13lTB32c3pcxEjWiyOb3UNFUziH4Puf5wu0HajbZSUbh7hGl75glH%2F3f%2FO0WyNMIjI87wGOqUBVCbPdqFKkPCExlNQU%2FQpcqAxBqjsvaZRlz%2BGLG75WqjTA76foLTlgVWGDnP7XcQBKVEOKI%2FQiUCSqQFKr0grJWFCNRTPHaov8vRJ2tu%2FXoNGOJuWUZGPVeE9Zd6QlSdhGfvhbYfAb0Q9Z81xvTUkWzBHOHS6K8eC4TH7k5YpVMGOEA4k392bpWx8SL9HZ4xhur%2F0ytdkRSIbcVNKBUR31dvJ7WW6&X-Amz-Signature=5b518fe25e29ffbab1ad608b5ddb021dd9d6b54c52ee43a444679996bfe5b237&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEIA7J7B%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1r4dHUecehX2xM8JQtk1VDrQ2ykYL50sYa5VfEGCDbAiEA3iT%2BYK3tCjjM5yWF9V7EVsWts8iQzfoAdOcCgHNdAC8qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH05hvTY%2FsrYvjoXESrcA%2BgIL6HV4M3NvLfAhZqBOwPQKf6pEO%2FXCXUzNlcGj4JfUISNGpJVVMaa%2B8J5QI6xUmWmSpvgYDL7G4OSj29a0LIgjyExNP9HjeNBs%2F4eV%2FJiIPZACqBlK1wPNJylqmr4HV9E9ABFYOVGdcbP04LN8a6F1gCOA55oJtIagHMWwHiPaWRoc3qNc8uRhk9LFXCIh9D00p7f1yWr59RYh1pJRo6WJe6K4jtKI%2BmQ%2FYNX59jxWqeicrnUDn9j2olKIl0AJZAr8aKZe6OLYmSfrwnIEILpoGcwNP5Pm054EWZ%2BBpf%2BSRK4Ep1iN3mVDDjklu2RlMulZZDYOnrP6VQAQuE5w9o3jr3noVTGPa03tjZQg5rRyPblkWmhF17hpREs4x4GjLrZAn%2FOWHUI9EYZ8sSR3Ys9h2u3Yy8SzCWZRhD77mh1xR4gNKxf2uXIXvg1TbficEGBXJZYeqQ1haU%2F8tN18lh2cGoj6HZ2QxLpWBE6h7YOqrvQRyCVRffk8nw26teZn96gaEL8pWAQcIfg1xwMpzNqOJOwEiSnkYA0hwTB%2BcGclorf8VcAAkhd75ILZS13lTB32c3pcxEjWiyOb3UNFUziH4Puf5wu0HajbZSUbh7hGl75glH%2F3f%2FO0WyNMIjI87wGOqUBVCbPdqFKkPCExlNQU%2FQpcqAxBqjsvaZRlz%2BGLG75WqjTA76foLTlgVWGDnP7XcQBKVEOKI%2FQiUCSqQFKr0grJWFCNRTPHaov8vRJ2tu%2FXoNGOJuWUZGPVeE9Zd6QlSdhGfvhbYfAb0Q9Z81xvTUkWzBHOHS6K8eC4TH7k5YpVMGOEA4k392bpWx8SL9HZ4xhur%2F0ytdkRSIbcVNKBUR31dvJ7WW6&X-Amz-Signature=3088f1c475499026ec1454896abb56c2c02c088d7a2f1541477c9a5cdc8e3156&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNQ6PW7Q%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIPOKolii%2BqWmC0F%2FLLRlPIus4HVn6uGPDn8t3WGrspQIgKJhIY44qaFqf%2B7ZzLclXeje%2BJkXQIFNJsI9JNxSQlQYqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG88Mbbi3CarPkc2AyrcA4aGwX7g%2FuPU4L1pgll0IGUppkp1plUXsuQW9lxiRWrqHCZ9vO4L0rcg%2F2iu9h0nsHofg4yirIExn1gpzCO5YTNICsZOVpjB1M8J4i9hqDDbPYwOF6eaZeCHFfWOtIBWDTVw%2BAQXwp9hjY1EqYCGs%2F9ErfGMO1Cju5rsuZV51W5RCJZaC2oLL420lgdgleT3aQ%2Fcsi%2FAZGNE5FJIL%2Blipg5YokNYH%2BChgFqCfTGHMUZSMU30DzdPqlbs7b7%2B4V%2F4JBdvaDyoEsd%2BAfHiFH4SO%2BvH7jDawbZK%2BNRKzqe7lIf8ci0ZhrK3s3JYlhoGGPLoNr03xoILO%2BZNmC%2FKA5rFVU%2FID3X1BLfCON09kUaCuJn4MtjfotAF%2FTedI%2BoCPTq7VQoLIqZCNSmggd6t7jIorutMc%2FSf2ci1viXwjf8IhMGogNhQ1DawNl0a%2FAEwjeIeLhuAJxcQXFhswiFmK%2B4USIOzcMoKBdGY%2BULzwfpLUNMoniMJZm4ID0te%2F07ucyYp5a2rphUE00f8ta1yB3ZCB6SEr3sCrQZYmL4R6DCl3BEwltfDcj4xRYGyAOaT2mT1Yh6c5ohO8ZNhg5aR43RkTPKpvIcLC9vM9dKq%2BsmUeedywJ8YVejXC3XOS8bhMMzI87wGOqUB8f5rHaQAjqK0yAqfhODNQhVkfbch%2Bkn2ErsmDuO3ctfy3Q%2BRjPBaFeCEwSfSlgt1HJSY01lbAZeW9wDe1MRCf1TCP3bA9CLr2cpU0AbrsKYALND66yxA7g1FlYWCRPl4DG52bhv4kZd4lHKOo7dJd2YzFruhVjfx29cD3EtjC6JWMjNgTglHUzKum7bTJ2CpKIMTLJzByHiuQKWY3FWIA3md6KXp&X-Amz-Signature=ef297d1106b7068704cc54ec46825e617be4a9409e72703b04581571dc893df5&X-Amz-SignedHeaders=host&x-id=GetObject)
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