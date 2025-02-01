

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSVCDT6W%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1VWFDF9M%2B9x9o8fTU%2F30avDyTaTB8E2jhETZbk3ezwAiEA4Fjt9zBObw0osA4c9mr72vPgQg07YGsTRGUeZYFlyPYqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO4aGFML91IUaVYNzCrcA3118LsKQucHHWnQZiy5sCCzvr0O6ENiBj0ptctsO5R5pEcKjgkOJbFkMIXKjmkGgmuXltQRPOQiEAKacu9bzjZKKUmUG4m7ByFcS6r22ZcNJ6NFHbKmfSh7IVwV%2FPeDkJ1HJfN89Yi9H2k0B5Co%2FzKpo%2FF%2FqjZfyFuG4n2NdVWDQ2mss7V1iaZjhOY4Sul08dfjEC27MLpvBljOBNsjmr0swlYc%2B%2F%2B2aDK02LDn%2FpkWnIyYVjgT9e3qpQgbvXTTY7MOggqv8TGZLKmcNGMBfMkw%2F5nW5Z6FEl%2BiEzgiPIc5YLvx9ff7Wc%2FLkY%2FLAKFBViRxdqqpEEqzTFcnPzNAbM5EC3iB1fLAVzG6Crt3SHU%2BfEmXlUDyaqnBPSpSruM5iNS6GjyT6bJ6u80vdhAxghZbkbEWLIOMaFaegCngqzqsdfOMcVelqqmqu9NSyCSnzJ27lYVZvNE5M3FkBuSZkGJ764A0DiTwK5WYoDgCyxcfvr1dIOPumjUWingJC%2BYhU2pdzlvq3x3cdk8g%2Bqeilt7teaacNPLFIERUTmSfzLkZLvVOaoEE8PWCLxxVPb3tdBcSj5NRDvte6b4gFMhR84zP20mMlsHAl%2FVJV%2BLczvecCgZEaDUv2trpHm04MO%2Fs9bwGOqUB5aLt%2Biliuo7C1HUoj6K1hXIwngyhHQ%2F1COlyBt6H4y17%2Fc4F1yR1FIukpccvsX5kKs%2FWhQeP%2BSxnk4iDJ270C5v42JYxt2YTn%2BziDtDEy3E4mgVe9UbkO%2BfSxDK9W3tyst6YKzAurxad7XzcBCpKXIQGzz0qDIDqD%2Ftnbx2M%2Fa6GlEIEUo%2FzWXAffwWf3XTzt3cmxJLTWR8n5x8f5B8aug9u209K&X-Amz-Signature=2caeec38be5985e26f9acce1395a1f9c3494f93a9b9c8ccd4b6670b89a08c30f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSVCDT6W%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1VWFDF9M%2B9x9o8fTU%2F30avDyTaTB8E2jhETZbk3ezwAiEA4Fjt9zBObw0osA4c9mr72vPgQg07YGsTRGUeZYFlyPYqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO4aGFML91IUaVYNzCrcA3118LsKQucHHWnQZiy5sCCzvr0O6ENiBj0ptctsO5R5pEcKjgkOJbFkMIXKjmkGgmuXltQRPOQiEAKacu9bzjZKKUmUG4m7ByFcS6r22ZcNJ6NFHbKmfSh7IVwV%2FPeDkJ1HJfN89Yi9H2k0B5Co%2FzKpo%2FF%2FqjZfyFuG4n2NdVWDQ2mss7V1iaZjhOY4Sul08dfjEC27MLpvBljOBNsjmr0swlYc%2B%2F%2B2aDK02LDn%2FpkWnIyYVjgT9e3qpQgbvXTTY7MOggqv8TGZLKmcNGMBfMkw%2F5nW5Z6FEl%2BiEzgiPIc5YLvx9ff7Wc%2FLkY%2FLAKFBViRxdqqpEEqzTFcnPzNAbM5EC3iB1fLAVzG6Crt3SHU%2BfEmXlUDyaqnBPSpSruM5iNS6GjyT6bJ6u80vdhAxghZbkbEWLIOMaFaegCngqzqsdfOMcVelqqmqu9NSyCSnzJ27lYVZvNE5M3FkBuSZkGJ764A0DiTwK5WYoDgCyxcfvr1dIOPumjUWingJC%2BYhU2pdzlvq3x3cdk8g%2Bqeilt7teaacNPLFIERUTmSfzLkZLvVOaoEE8PWCLxxVPb3tdBcSj5NRDvte6b4gFMhR84zP20mMlsHAl%2FVJV%2BLczvecCgZEaDUv2trpHm04MO%2Fs9bwGOqUB5aLt%2Biliuo7C1HUoj6K1hXIwngyhHQ%2F1COlyBt6H4y17%2Fc4F1yR1FIukpccvsX5kKs%2FWhQeP%2BSxnk4iDJ270C5v42JYxt2YTn%2BziDtDEy3E4mgVe9UbkO%2BfSxDK9W3tyst6YKzAurxad7XzcBCpKXIQGzz0qDIDqD%2Ftnbx2M%2Fa6GlEIEUo%2FzWXAffwWf3XTzt3cmxJLTWR8n5x8f5B8aug9u209K&X-Amz-Signature=1258464ce07539c3b17d53e426709b21d18e76dd37c89dde8e11e30106f754fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSVCDT6W%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1VWFDF9M%2B9x9o8fTU%2F30avDyTaTB8E2jhETZbk3ezwAiEA4Fjt9zBObw0osA4c9mr72vPgQg07YGsTRGUeZYFlyPYqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO4aGFML91IUaVYNzCrcA3118LsKQucHHWnQZiy5sCCzvr0O6ENiBj0ptctsO5R5pEcKjgkOJbFkMIXKjmkGgmuXltQRPOQiEAKacu9bzjZKKUmUG4m7ByFcS6r22ZcNJ6NFHbKmfSh7IVwV%2FPeDkJ1HJfN89Yi9H2k0B5Co%2FzKpo%2FF%2FqjZfyFuG4n2NdVWDQ2mss7V1iaZjhOY4Sul08dfjEC27MLpvBljOBNsjmr0swlYc%2B%2F%2B2aDK02LDn%2FpkWnIyYVjgT9e3qpQgbvXTTY7MOggqv8TGZLKmcNGMBfMkw%2F5nW5Z6FEl%2BiEzgiPIc5YLvx9ff7Wc%2FLkY%2FLAKFBViRxdqqpEEqzTFcnPzNAbM5EC3iB1fLAVzG6Crt3SHU%2BfEmXlUDyaqnBPSpSruM5iNS6GjyT6bJ6u80vdhAxghZbkbEWLIOMaFaegCngqzqsdfOMcVelqqmqu9NSyCSnzJ27lYVZvNE5M3FkBuSZkGJ764A0DiTwK5WYoDgCyxcfvr1dIOPumjUWingJC%2BYhU2pdzlvq3x3cdk8g%2Bqeilt7teaacNPLFIERUTmSfzLkZLvVOaoEE8PWCLxxVPb3tdBcSj5NRDvte6b4gFMhR84zP20mMlsHAl%2FVJV%2BLczvecCgZEaDUv2trpHm04MO%2Fs9bwGOqUB5aLt%2Biliuo7C1HUoj6K1hXIwngyhHQ%2F1COlyBt6H4y17%2Fc4F1yR1FIukpccvsX5kKs%2FWhQeP%2BSxnk4iDJ270C5v42JYxt2YTn%2BziDtDEy3E4mgVe9UbkO%2BfSxDK9W3tyst6YKzAurxad7XzcBCpKXIQGzz0qDIDqD%2Ftnbx2M%2Fa6GlEIEUo%2FzWXAffwWf3XTzt3cmxJLTWR8n5x8f5B8aug9u209K&X-Amz-Signature=7fbb42e9c25106bf374784a5bf962abf82c418ad116d80aacdd218b69aa22baf&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSWLZIWS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzrL0m%2F5FWBRltQQL%2B6RKgytkPMVpyvCPE0Kh8ZKFKiAIhAJHG%2BXJs3kzH3xPXFqTWDIyiVVpWOHY0TuoZRkyH5nKlKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUkO%2BFQc5NTcU9CIYq3AOv7eDKlZnw6BEqd8%2BHGHlt2a9KA1ZcvWmBoykt51FMko5JtXXyk88%2BZ6LAss1Z%2B6JBcxn9c2fI6bvqFXfpOq%2FOUUOn%2Be%2FDL%2Feya6DmYttZdEgOXNkn%2Fl1uYG8QTO6f8NWXuIBmhHGVmAiCfHPJLVFfWZAbnz63OPEaxUbtNdGgW7B9J8GfpZfQpqZL521Kt79kqVjYSZeBkS98t7qRA0KK%2BeuGFzxLdTHMVph%2BzK6fh7f7N2Be0kG4BtwABo9rXJChRosO2CK%2Fgya2j8Q3o%2Btu1FU%2B9KWCwe4wicrjqbFP0GUPnympTpsaSYd%2FxGfjjkcNjnIh%2FbOIrY8canHv8Bb2kSrsZSNo6vpHUSjXFCJvz48%2BjJXVEspaGIN0yGiD55xjcd22fraL2wE%2BxoJ7XnSc3CBwS1yA4S%2BeAO9aOeDE0LQz9DuYiVIHOqpsRYfljjLJYnCBZa3pl9uvwI2aotmZ01OfWZbPdD%2FE%2BLdBe7X%2Ff59zINJjVwut3djNWRlz0xef75m1v2A%2B1IF7GNmzukVQhfbojgIgqSQjqViAG%2BQ7%2FhDpMmPcHj6EDEMKgf%2B6x62%2FJd58rqbmr12nI0qwXEf1GFlmeJFvwY%2B9CljfGVo07b6fXpQo7j6McVjppTCb7PW8BjqkAeSS6YUQ23EunF2BrgiKcrnH%2BZcc%2FL6JOlQWFf9wtyuZSsDoaq9qDyqLZRNgOvB2KqRCjvO2OjpDqoTpXV6M40KUM4Gr%2FPYhvHv42TkM8JSmUOpXaH1ozwWJ04zeEPUM%2BqSpDrxmWaIdlV1UC44KKdKYzDzpRp1OZS6aP5Pp0NDFQMW7ULZqZo2lvX1xhFOH2g6a7TXEiHNbDF8RG6zmeSvRiW9r&X-Amz-Signature=d333ae7c8c8497288aba35e3317c34483e7d6da54538274004d9e52ad9068b93&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSWLZIWS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzrL0m%2F5FWBRltQQL%2B6RKgytkPMVpyvCPE0Kh8ZKFKiAIhAJHG%2BXJs3kzH3xPXFqTWDIyiVVpWOHY0TuoZRkyH5nKlKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUkO%2BFQc5NTcU9CIYq3AOv7eDKlZnw6BEqd8%2BHGHlt2a9KA1ZcvWmBoykt51FMko5JtXXyk88%2BZ6LAss1Z%2B6JBcxn9c2fI6bvqFXfpOq%2FOUUOn%2Be%2FDL%2Feya6DmYttZdEgOXNkn%2Fl1uYG8QTO6f8NWXuIBmhHGVmAiCfHPJLVFfWZAbnz63OPEaxUbtNdGgW7B9J8GfpZfQpqZL521Kt79kqVjYSZeBkS98t7qRA0KK%2BeuGFzxLdTHMVph%2BzK6fh7f7N2Be0kG4BtwABo9rXJChRosO2CK%2Fgya2j8Q3o%2Btu1FU%2B9KWCwe4wicrjqbFP0GUPnympTpsaSYd%2FxGfjjkcNjnIh%2FbOIrY8canHv8Bb2kSrsZSNo6vpHUSjXFCJvz48%2BjJXVEspaGIN0yGiD55xjcd22fraL2wE%2BxoJ7XnSc3CBwS1yA4S%2BeAO9aOeDE0LQz9DuYiVIHOqpsRYfljjLJYnCBZa3pl9uvwI2aotmZ01OfWZbPdD%2FE%2BLdBe7X%2Ff59zINJjVwut3djNWRlz0xef75m1v2A%2B1IF7GNmzukVQhfbojgIgqSQjqViAG%2BQ7%2FhDpMmPcHj6EDEMKgf%2B6x62%2FJd58rqbmr12nI0qwXEf1GFlmeJFvwY%2B9CljfGVo07b6fXpQo7j6McVjppTCb7PW8BjqkAeSS6YUQ23EunF2BrgiKcrnH%2BZcc%2FL6JOlQWFf9wtyuZSsDoaq9qDyqLZRNgOvB2KqRCjvO2OjpDqoTpXV6M40KUM4Gr%2FPYhvHv42TkM8JSmUOpXaH1ozwWJ04zeEPUM%2BqSpDrxmWaIdlV1UC44KKdKYzDzpRp1OZS6aP5Pp0NDFQMW7ULZqZo2lvX1xhFOH2g6a7TXEiHNbDF8RG6zmeSvRiW9r&X-Amz-Signature=39c531b8f0a7f4458e14d13cc58010a8fe0d4d2132412d66ab9f2faf9b4c2a45&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSVCDT6W%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1VWFDF9M%2B9x9o8fTU%2F30avDyTaTB8E2jhETZbk3ezwAiEA4Fjt9zBObw0osA4c9mr72vPgQg07YGsTRGUeZYFlyPYqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO4aGFML91IUaVYNzCrcA3118LsKQucHHWnQZiy5sCCzvr0O6ENiBj0ptctsO5R5pEcKjgkOJbFkMIXKjmkGgmuXltQRPOQiEAKacu9bzjZKKUmUG4m7ByFcS6r22ZcNJ6NFHbKmfSh7IVwV%2FPeDkJ1HJfN89Yi9H2k0B5Co%2FzKpo%2FF%2FqjZfyFuG4n2NdVWDQ2mss7V1iaZjhOY4Sul08dfjEC27MLpvBljOBNsjmr0swlYc%2B%2F%2B2aDK02LDn%2FpkWnIyYVjgT9e3qpQgbvXTTY7MOggqv8TGZLKmcNGMBfMkw%2F5nW5Z6FEl%2BiEzgiPIc5YLvx9ff7Wc%2FLkY%2FLAKFBViRxdqqpEEqzTFcnPzNAbM5EC3iB1fLAVzG6Crt3SHU%2BfEmXlUDyaqnBPSpSruM5iNS6GjyT6bJ6u80vdhAxghZbkbEWLIOMaFaegCngqzqsdfOMcVelqqmqu9NSyCSnzJ27lYVZvNE5M3FkBuSZkGJ764A0DiTwK5WYoDgCyxcfvr1dIOPumjUWingJC%2BYhU2pdzlvq3x3cdk8g%2Bqeilt7teaacNPLFIERUTmSfzLkZLvVOaoEE8PWCLxxVPb3tdBcSj5NRDvte6b4gFMhR84zP20mMlsHAl%2FVJV%2BLczvecCgZEaDUv2trpHm04MO%2Fs9bwGOqUB5aLt%2Biliuo7C1HUoj6K1hXIwngyhHQ%2F1COlyBt6H4y17%2Fc4F1yR1FIukpccvsX5kKs%2FWhQeP%2BSxnk4iDJ270C5v42JYxt2YTn%2BziDtDEy3E4mgVe9UbkO%2BfSxDK9W3tyst6YKzAurxad7XzcBCpKXIQGzz0qDIDqD%2Ftnbx2M%2Fa6GlEIEUo%2FzWXAffwWf3XTzt3cmxJLTWR8n5x8f5B8aug9u209K&X-Amz-Signature=2a5acc62d197285287c4f0987ced71effedb501030f95e6023e701393b5e5bc1&X-Amz-SignedHeaders=host&x-id=GetObject)
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