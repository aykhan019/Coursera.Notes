

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIQ6QRHA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE12Ct5rA2UpeiWfi4DH6jgEZXzoJx1M05YVEADZE2gWAiEAl6jNnBhZJstpVZJDA0VWHXoBcqHqNF3YCeccmxs4EvoqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEjg7Vin%2F43MPHnnVircA9wduA3ilBlVYMmIWSQ%2FUefTmoF%2FviDQ9zhNtqn%2Ffv7Wvf4tYT7iv7v3ficZC7D7cz7BhItztUE9aZqLHDPtJ9nmTUWF2MBFzv9DkosWW0%2FkfiBTWaS5xNwRSKiOBgLoKzBVVO%2FQrz2oYr7U2MXswDnpuzyP8wajl1YQ5p%2B17qxkBj16j%2FWu7FVb5OLchAdvv9S6p0V2FKmkYCpuvZyiLBvD%2B5P28t4sRlAgqilVJBNObWS1zme3WopbDIZIJf7Tsf9CX7UX6z9JBmC5k0dZaANPR3obyK06WpPPIfFMLu%2BaSxF1uQew8z3ZL7QzDhmqYQEqHCCzW59HcYyc8NradQcn%2Bwe9XjC07t%2BEVv3Wkfbu0oKZKbB07X9VUh91Wd7dkqYfKcEjmWMHdGNlludGpzEYZ5X6ekKLg817qviUNsXbsMUih1k1f1tEWlru5rMKHUDEdTm9CNLa4kbOzVv8WyJvr8cpSfV%2F%2BfiI1BB2JfpTrOZC5qJE047RUae6eMEkCD0NwzpLgqWRg7upfiW3k4bZ5VFXAyPxSrjJ6YmwQErHx0HQu353t%2FQ9fRnwhjzifv0NmEwOXPiMI4eSmxZ9n8ONPKqdSLkItqo2EScm%2Bhl%2FuNOiqeVcsMPxfrZlMO6G7LwGOqUBHFBb2KPxteq%2B1LaJFq7Vc9zQHynNdFa939e46ppX4jhC6nCJlzbMjQuw%2Fr0wIenBEEjXVrTfbxs%2Fk2UZI6YW%2BiunW3PoPzXnCiBRZNNzNB38XpnWg6hgjhNkUplGeB5M7xN0CTJ0ziOmWwDOCKFRowLUtxM4VtlwvTyz6AIlxlSOjpbT3hbhGTRfvJ1ccHPE2Wn7yHDNdcFrhqD%2BkcR2F2Jz8Bfr&X-Amz-Signature=83f3c3736e9717de5ed9784ad2f050b713daeac2e339f524aca3225c3c94cc42&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIQ6QRHA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE12Ct5rA2UpeiWfi4DH6jgEZXzoJx1M05YVEADZE2gWAiEAl6jNnBhZJstpVZJDA0VWHXoBcqHqNF3YCeccmxs4EvoqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEjg7Vin%2F43MPHnnVircA9wduA3ilBlVYMmIWSQ%2FUefTmoF%2FviDQ9zhNtqn%2Ffv7Wvf4tYT7iv7v3ficZC7D7cz7BhItztUE9aZqLHDPtJ9nmTUWF2MBFzv9DkosWW0%2FkfiBTWaS5xNwRSKiOBgLoKzBVVO%2FQrz2oYr7U2MXswDnpuzyP8wajl1YQ5p%2B17qxkBj16j%2FWu7FVb5OLchAdvv9S6p0V2FKmkYCpuvZyiLBvD%2B5P28t4sRlAgqilVJBNObWS1zme3WopbDIZIJf7Tsf9CX7UX6z9JBmC5k0dZaANPR3obyK06WpPPIfFMLu%2BaSxF1uQew8z3ZL7QzDhmqYQEqHCCzW59HcYyc8NradQcn%2Bwe9XjC07t%2BEVv3Wkfbu0oKZKbB07X9VUh91Wd7dkqYfKcEjmWMHdGNlludGpzEYZ5X6ekKLg817qviUNsXbsMUih1k1f1tEWlru5rMKHUDEdTm9CNLa4kbOzVv8WyJvr8cpSfV%2F%2BfiI1BB2JfpTrOZC5qJE047RUae6eMEkCD0NwzpLgqWRg7upfiW3k4bZ5VFXAyPxSrjJ6YmwQErHx0HQu353t%2FQ9fRnwhjzifv0NmEwOXPiMI4eSmxZ9n8ONPKqdSLkItqo2EScm%2Bhl%2FuNOiqeVcsMPxfrZlMO6G7LwGOqUBHFBb2KPxteq%2B1LaJFq7Vc9zQHynNdFa939e46ppX4jhC6nCJlzbMjQuw%2Fr0wIenBEEjXVrTfbxs%2Fk2UZI6YW%2BiunW3PoPzXnCiBRZNNzNB38XpnWg6hgjhNkUplGeB5M7xN0CTJ0ziOmWwDOCKFRowLUtxM4VtlwvTyz6AIlxlSOjpbT3hbhGTRfvJ1ccHPE2Wn7yHDNdcFrhqD%2BkcR2F2Jz8Bfr&X-Amz-Signature=470d57a8715523930e72944b5e2765cb9a7f4a196c994fa29df3d32b59391bb4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIQ6QRHA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE12Ct5rA2UpeiWfi4DH6jgEZXzoJx1M05YVEADZE2gWAiEAl6jNnBhZJstpVZJDA0VWHXoBcqHqNF3YCeccmxs4EvoqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEjg7Vin%2F43MPHnnVircA9wduA3ilBlVYMmIWSQ%2FUefTmoF%2FviDQ9zhNtqn%2Ffv7Wvf4tYT7iv7v3ficZC7D7cz7BhItztUE9aZqLHDPtJ9nmTUWF2MBFzv9DkosWW0%2FkfiBTWaS5xNwRSKiOBgLoKzBVVO%2FQrz2oYr7U2MXswDnpuzyP8wajl1YQ5p%2B17qxkBj16j%2FWu7FVb5OLchAdvv9S6p0V2FKmkYCpuvZyiLBvD%2B5P28t4sRlAgqilVJBNObWS1zme3WopbDIZIJf7Tsf9CX7UX6z9JBmC5k0dZaANPR3obyK06WpPPIfFMLu%2BaSxF1uQew8z3ZL7QzDhmqYQEqHCCzW59HcYyc8NradQcn%2Bwe9XjC07t%2BEVv3Wkfbu0oKZKbB07X9VUh91Wd7dkqYfKcEjmWMHdGNlludGpzEYZ5X6ekKLg817qviUNsXbsMUih1k1f1tEWlru5rMKHUDEdTm9CNLa4kbOzVv8WyJvr8cpSfV%2F%2BfiI1BB2JfpTrOZC5qJE047RUae6eMEkCD0NwzpLgqWRg7upfiW3k4bZ5VFXAyPxSrjJ6YmwQErHx0HQu353t%2FQ9fRnwhjzifv0NmEwOXPiMI4eSmxZ9n8ONPKqdSLkItqo2EScm%2Bhl%2FuNOiqeVcsMPxfrZlMO6G7LwGOqUBHFBb2KPxteq%2B1LaJFq7Vc9zQHynNdFa939e46ppX4jhC6nCJlzbMjQuw%2Fr0wIenBEEjXVrTfbxs%2Fk2UZI6YW%2BiunW3PoPzXnCiBRZNNzNB38XpnWg6hgjhNkUplGeB5M7xN0CTJ0ziOmWwDOCKFRowLUtxM4VtlwvTyz6AIlxlSOjpbT3hbhGTRfvJ1ccHPE2Wn7yHDNdcFrhqD%2BkcR2F2Jz8Bfr&X-Amz-Signature=aa7c04fc1e9c639bd4463609c99fb727fb026325534dc9d74b2a5197ce0c8184&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BU6I4XM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqaCB5wtoBAMnyQ5kFw%2FkL7EqFNRMreodVJY0jlgOItwIgD%2FNAnSQKOU4KFjN7KFtO17NZBKYsNXuk%2Boe%2FshrS7CIqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCXn6lrQ%2FuYuPhVGSSrcA5pk5vyAx3Yz3gJqF%2FB26ylYi3COQQyYBkHn8v5DUKreSNh48lYL746G5aO0ieO3VsYOgR8Q9y%2BICzHYRzOC6OIss0bw%2B9i5rfCib2iu%2Fwpm%2BBT%2Bh94gSw0RM%2FDfCxXkyAXjt7LryR603NTFwkbXoWOikjWgHDLBzhBD%2FA%2Fya1YIKESz%2FVwbhLFU407aVoc3ltJmgp69y1b2%2BWjckTAq1YizL2hoPg43c71k7wb4UKQUOrmSdwLs6T1nt%2BAlXvgR7AjtRUyoCQA9nzo0Q2y5JyNtYmz2dol%2FlYZTU%2FTq03rBe7RpvBVDPBpVwtqOqQ2QK5ero7WHeob7TzmUse4ClicKxJeae1eO%2Bm1t6RVSS1zxMmkSgUaWVvKpltr%2Fv0FsSicfF6pnfB32ep8jkjnX1d5viMnJbSEggoHefO3KTgrtpa%2BtBOivy99R5dbuuPIO7oRlM%2FQosbz0itHvoR76zZpxdev4y8e5kwofM%2BbpH4f%2BFOH1D3TLlHM4n7kIm94iwuldYr17HIP6l%2FuvcBEPTeyWgfX93QO5e1O3K4h5hLf8ivkr9uJJINfzpBpfsuWhtYdzTCYC2fiSB1aqT5gUsgvI9AmU9yH6Jgtvwido6S8M3irB4wmc4K8Npm9qMJuH7LwGOqUBbrHI6C15X7w8EcOjIv0qB%2BlnrNQq2YV4b2iq3qVCXMOTrdl8b1koPPk6F2YwfyKC%2F8JnkiDj9Uk8FDlPewZLm0eutIcvt0km%2FxeeTZz5LlE9eAWOogX%2BWjDVFChB3Lqf%2B6l6A%2B%2Fg1ZoL1cX%2FvyE2Dc5T51Vfu2olXxaLRqML%2FxjacOQULNz2i2moT6SoTcztQ4p7jn8GndMEljnN%2FE27cjf7L2sb&X-Amz-Signature=fb78f863d5378cb7baf5f2271cef457d755da4d4b2b11df0ad15052ea67c7dec&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BU6I4XM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqaCB5wtoBAMnyQ5kFw%2FkL7EqFNRMreodVJY0jlgOItwIgD%2FNAnSQKOU4KFjN7KFtO17NZBKYsNXuk%2Boe%2FshrS7CIqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCXn6lrQ%2FuYuPhVGSSrcA5pk5vyAx3Yz3gJqF%2FB26ylYi3COQQyYBkHn8v5DUKreSNh48lYL746G5aO0ieO3VsYOgR8Q9y%2BICzHYRzOC6OIss0bw%2B9i5rfCib2iu%2Fwpm%2BBT%2Bh94gSw0RM%2FDfCxXkyAXjt7LryR603NTFwkbXoWOikjWgHDLBzhBD%2FA%2Fya1YIKESz%2FVwbhLFU407aVoc3ltJmgp69y1b2%2BWjckTAq1YizL2hoPg43c71k7wb4UKQUOrmSdwLs6T1nt%2BAlXvgR7AjtRUyoCQA9nzo0Q2y5JyNtYmz2dol%2FlYZTU%2FTq03rBe7RpvBVDPBpVwtqOqQ2QK5ero7WHeob7TzmUse4ClicKxJeae1eO%2Bm1t6RVSS1zxMmkSgUaWVvKpltr%2Fv0FsSicfF6pnfB32ep8jkjnX1d5viMnJbSEggoHefO3KTgrtpa%2BtBOivy99R5dbuuPIO7oRlM%2FQosbz0itHvoR76zZpxdev4y8e5kwofM%2BbpH4f%2BFOH1D3TLlHM4n7kIm94iwuldYr17HIP6l%2FuvcBEPTeyWgfX93QO5e1O3K4h5hLf8ivkr9uJJINfzpBpfsuWhtYdzTCYC2fiSB1aqT5gUsgvI9AmU9yH6Jgtvwido6S8M3irB4wmc4K8Npm9qMJuH7LwGOqUBbrHI6C15X7w8EcOjIv0qB%2BlnrNQq2YV4b2iq3qVCXMOTrdl8b1koPPk6F2YwfyKC%2F8JnkiDj9Uk8FDlPewZLm0eutIcvt0km%2FxeeTZz5LlE9eAWOogX%2BWjDVFChB3Lqf%2B6l6A%2B%2Fg1ZoL1cX%2FvyE2Dc5T51Vfu2olXxaLRqML%2FxjacOQULNz2i2moT6SoTcztQ4p7jn8GndMEljnN%2FE27cjf7L2sb&X-Amz-Signature=bcad26ef20c1bf91b3052af0354a592d79ce85bd74e15a84901b7d1d5ae67a5c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIQ6QRHA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE12Ct5rA2UpeiWfi4DH6jgEZXzoJx1M05YVEADZE2gWAiEAl6jNnBhZJstpVZJDA0VWHXoBcqHqNF3YCeccmxs4EvoqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEjg7Vin%2F43MPHnnVircA9wduA3ilBlVYMmIWSQ%2FUefTmoF%2FviDQ9zhNtqn%2Ffv7Wvf4tYT7iv7v3ficZC7D7cz7BhItztUE9aZqLHDPtJ9nmTUWF2MBFzv9DkosWW0%2FkfiBTWaS5xNwRSKiOBgLoKzBVVO%2FQrz2oYr7U2MXswDnpuzyP8wajl1YQ5p%2B17qxkBj16j%2FWu7FVb5OLchAdvv9S6p0V2FKmkYCpuvZyiLBvD%2B5P28t4sRlAgqilVJBNObWS1zme3WopbDIZIJf7Tsf9CX7UX6z9JBmC5k0dZaANPR3obyK06WpPPIfFMLu%2BaSxF1uQew8z3ZL7QzDhmqYQEqHCCzW59HcYyc8NradQcn%2Bwe9XjC07t%2BEVv3Wkfbu0oKZKbB07X9VUh91Wd7dkqYfKcEjmWMHdGNlludGpzEYZ5X6ekKLg817qviUNsXbsMUih1k1f1tEWlru5rMKHUDEdTm9CNLa4kbOzVv8WyJvr8cpSfV%2F%2BfiI1BB2JfpTrOZC5qJE047RUae6eMEkCD0NwzpLgqWRg7upfiW3k4bZ5VFXAyPxSrjJ6YmwQErHx0HQu353t%2FQ9fRnwhjzifv0NmEwOXPiMI4eSmxZ9n8ONPKqdSLkItqo2EScm%2Bhl%2FuNOiqeVcsMPxfrZlMO6G7LwGOqUBHFBb2KPxteq%2B1LaJFq7Vc9zQHynNdFa939e46ppX4jhC6nCJlzbMjQuw%2Fr0wIenBEEjXVrTfbxs%2Fk2UZI6YW%2BiunW3PoPzXnCiBRZNNzNB38XpnWg6hgjhNkUplGeB5M7xN0CTJ0ziOmWwDOCKFRowLUtxM4VtlwvTyz6AIlxlSOjpbT3hbhGTRfvJ1ccHPE2Wn7yHDNdcFrhqD%2BkcR2F2Jz8Bfr&X-Amz-Signature=42463c4f007236792087eccd0dd38cb015fa8587771722ef3ca62855d0a4c253&X-Amz-SignedHeaders=host&x-id=GetObject)
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