

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGTBW76P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDp3Dtz7YUOY5sXQ1deZ9fcmwTgjIzMn8KGPCkqEh7aUgIgXpg%2FcJofis1LVGNuGsWiTDRK5sv0OuTI5NDNh9xx7ewqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCjueeUddU%2Ffl45NsSrcA9R9zBciBsfv9ltkS5fWa%2BsGUvrAVf12han4YDjzwwgCulJNEqw%2Bdgt%2BL7Zd9XHT6KR0l2hBzNcmcP3PZJo4pw%2FVEbwHZo96LZ%2FIho5EFLcS%2FGvN4dFfD8OFfHRtbMmg8QbQ0wvnhtrL7Svqq9FLdKXFYlp%2FNW3xlikNEtGloIfl5eX4eSlbK7raIG2pp3KK2fqG7%2FVvtZwi1dWSC3ZoSeqG7UVqC%2FNqe9LhG%2BK7Hc4zh8kSf%2BPlghiIyW0wTYiMzQBWj2%2BgR0gBX3OiV22%2B9NBeezg5WODSc1fu8HeBQ%2BcHYG49W%2F3nNAUu3UEqkZqvn9KB8rwmVVTu9ZiaatPkOC3eEC%2FapRIQNVFnbSLNeyITNFd2dky4z0Jx%2Ftb6TJUDzfWcDEJXvIPxV2ClormnrnMWcw7bdD2Seic2ADMP88VF9rWfLdFkKb%2FJN8B0HtlKZoi%2Fd%2Bwo1D5oSHuxMGEMPXLxmfrNmZUgVxMykegl9g639zGxEOs4i0keGr8p%2BDKrhJZY8OhScqT1xfSld3wPEo6HqMj7MvF%2FCqVORyJM5YzFji1alCxfWyq3jxidFxdqICtMPM6uu6bBcv1XM%2FvzrHOZ%2BNeJjrHxKcIC5mahyOc1cUX9UUD3gSItZdnrMPaT%2BrwGOqUBSwyo7nLZZKGyXgBdCV50dx0qMJkWItBozylFS7g%2BQwK%2FyxiC4cznSh19E5kJN2R8L08RvSESvAiR7%2FFGK05oJVCYuUZTbV3exAwKlwz3uj01vIuFku%2FSHya3vufmMGzGtz6%2BLhICKiEAWPpAICAQK5v6QKtcYPndp%2Fw%2FZf0i7TB%2BcUJB%2FfR4jOXxrydTYdwMx%2ByjexVaI9ZHrobfynFFL6ROD6za&X-Amz-Signature=31eb61b817114a88867169ddbccad3dc167f048a5eee96de4b8333d716eac215&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGTBW76P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDp3Dtz7YUOY5sXQ1deZ9fcmwTgjIzMn8KGPCkqEh7aUgIgXpg%2FcJofis1LVGNuGsWiTDRK5sv0OuTI5NDNh9xx7ewqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCjueeUddU%2Ffl45NsSrcA9R9zBciBsfv9ltkS5fWa%2BsGUvrAVf12han4YDjzwwgCulJNEqw%2Bdgt%2BL7Zd9XHT6KR0l2hBzNcmcP3PZJo4pw%2FVEbwHZo96LZ%2FIho5EFLcS%2FGvN4dFfD8OFfHRtbMmg8QbQ0wvnhtrL7Svqq9FLdKXFYlp%2FNW3xlikNEtGloIfl5eX4eSlbK7raIG2pp3KK2fqG7%2FVvtZwi1dWSC3ZoSeqG7UVqC%2FNqe9LhG%2BK7Hc4zh8kSf%2BPlghiIyW0wTYiMzQBWj2%2BgR0gBX3OiV22%2B9NBeezg5WODSc1fu8HeBQ%2BcHYG49W%2F3nNAUu3UEqkZqvn9KB8rwmVVTu9ZiaatPkOC3eEC%2FapRIQNVFnbSLNeyITNFd2dky4z0Jx%2Ftb6TJUDzfWcDEJXvIPxV2ClormnrnMWcw7bdD2Seic2ADMP88VF9rWfLdFkKb%2FJN8B0HtlKZoi%2Fd%2Bwo1D5oSHuxMGEMPXLxmfrNmZUgVxMykegl9g639zGxEOs4i0keGr8p%2BDKrhJZY8OhScqT1xfSld3wPEo6HqMj7MvF%2FCqVORyJM5YzFji1alCxfWyq3jxidFxdqICtMPM6uu6bBcv1XM%2FvzrHOZ%2BNeJjrHxKcIC5mahyOc1cUX9UUD3gSItZdnrMPaT%2BrwGOqUBSwyo7nLZZKGyXgBdCV50dx0qMJkWItBozylFS7g%2BQwK%2FyxiC4cznSh19E5kJN2R8L08RvSESvAiR7%2FFGK05oJVCYuUZTbV3exAwKlwz3uj01vIuFku%2FSHya3vufmMGzGtz6%2BLhICKiEAWPpAICAQK5v6QKtcYPndp%2Fw%2FZf0i7TB%2BcUJB%2FfR4jOXxrydTYdwMx%2ByjexVaI9ZHrobfynFFL6ROD6za&X-Amz-Signature=5315047043a001c81678b32c0cebceee54ebeb8dc0cb8cbfc5d7f31e3d96b19f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGTBW76P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDp3Dtz7YUOY5sXQ1deZ9fcmwTgjIzMn8KGPCkqEh7aUgIgXpg%2FcJofis1LVGNuGsWiTDRK5sv0OuTI5NDNh9xx7ewqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCjueeUddU%2Ffl45NsSrcA9R9zBciBsfv9ltkS5fWa%2BsGUvrAVf12han4YDjzwwgCulJNEqw%2Bdgt%2BL7Zd9XHT6KR0l2hBzNcmcP3PZJo4pw%2FVEbwHZo96LZ%2FIho5EFLcS%2FGvN4dFfD8OFfHRtbMmg8QbQ0wvnhtrL7Svqq9FLdKXFYlp%2FNW3xlikNEtGloIfl5eX4eSlbK7raIG2pp3KK2fqG7%2FVvtZwi1dWSC3ZoSeqG7UVqC%2FNqe9LhG%2BK7Hc4zh8kSf%2BPlghiIyW0wTYiMzQBWj2%2BgR0gBX3OiV22%2B9NBeezg5WODSc1fu8HeBQ%2BcHYG49W%2F3nNAUu3UEqkZqvn9KB8rwmVVTu9ZiaatPkOC3eEC%2FapRIQNVFnbSLNeyITNFd2dky4z0Jx%2Ftb6TJUDzfWcDEJXvIPxV2ClormnrnMWcw7bdD2Seic2ADMP88VF9rWfLdFkKb%2FJN8B0HtlKZoi%2Fd%2Bwo1D5oSHuxMGEMPXLxmfrNmZUgVxMykegl9g639zGxEOs4i0keGr8p%2BDKrhJZY8OhScqT1xfSld3wPEo6HqMj7MvF%2FCqVORyJM5YzFji1alCxfWyq3jxidFxdqICtMPM6uu6bBcv1XM%2FvzrHOZ%2BNeJjrHxKcIC5mahyOc1cUX9UUD3gSItZdnrMPaT%2BrwGOqUBSwyo7nLZZKGyXgBdCV50dx0qMJkWItBozylFS7g%2BQwK%2FyxiC4cznSh19E5kJN2R8L08RvSESvAiR7%2FFGK05oJVCYuUZTbV3exAwKlwz3uj01vIuFku%2FSHya3vufmMGzGtz6%2BLhICKiEAWPpAICAQK5v6QKtcYPndp%2Fw%2FZf0i7TB%2BcUJB%2FfR4jOXxrydTYdwMx%2ByjexVaI9ZHrobfynFFL6ROD6za&X-Amz-Signature=bc0c7347db8de0ca0768bdca9f85300601a93f8b0b865668b716bb773d12e9af&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A32ABSR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgiM61O28FIT1y7SP1tbaUKWx8Aum%2FLteM6I74uAHqgQIgMnQXfAG%2FOrOOzuHpC2xfW7m1XXug0cvWK0JuYAzzrm8qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLT%2Fcn5I3OlMa9bUJCrcA%2BVVOAEAOaR%2FnrumU2Q6OsM93%2B%2F8iG0znzLCJRWlhtV%2BWupsATsTpWB10z7hQJFTvslYdwTxx7z4Pfrl%2FA0GjgXMRK1L%2BvznAPo2BMZDbclBn2qIKZhkk8poKMqw%2Fp0ic2Tgcx5DhwR1rJKuINBvQQmEzJPBICKlEen6Sj7A3vnW0Oc%2FPp0MmjExK5eRNcniyV8BUyHJjymMvtzzOON814hyitmFkXv%2BsnO%2BT5IOXXQMER%2FvBNvi2HyLTsIxnQB2e1oYQDuUvYlTZDEUFc7GuUVANRX2R6mntVNpqUnRnSQjdf4mbrOy4rBqhWInp41enVnPk36h3G2OHTIJG6uPpYfWK3QAbgJ%2BqbHPTtSQ2pPpWZySwwHiAk%2Fisx6xt3DpI%2FeVP9Bp2vzd3DGA8bWEarAwNI5dK35RF64effF%2FJ%2BT4CFTF9TWjPxVw4yqGsy9X66RTCYy1OO9Q56aDMyacQbLivgdLtRrnwFRToZl1GxXWNdoCxShqZTarvOzxAFVr1SJMckvteJjUUxGGdN3gRaYzSnVI4YeXU24oYp6TAXRHuVdRaJxuuDEjSnBsi%2BzxOuVYK%2FVLJuCXgDBmwO9%2FeQeQMdDf1oKRrSTwVfuAXeG86tpQ5nqGPxyYGGIsMJ6U%2BrwGOqUB9SAjXJhTuT41QiGaU1eenfFsbruxxR4CLcl8YV1RUrFZYcigf7S%2F6WvvS%2B%2FYSVsvMqrHEcHVU7H4%2FOJbHeOvJ%2Fen%2B6i4unLV15Wt%2FEvlDEJZI1G3Bhdrhoaahq2kPvcef9Bo0usWw4GqYjOXB0J9TfWgnDZDo9k%2FDNVU1tOmPo%2FB%2B2LYXGNXs3LJ5uXbUYBw7NH8rkWlrSfJrdwKPoRVP3Fw7tru&X-Amz-Signature=e92bcf99303599873c73ce064f6f9703e3232f91f38f185f09f06c42bd134efc&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A32ABSR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgiM61O28FIT1y7SP1tbaUKWx8Aum%2FLteM6I74uAHqgQIgMnQXfAG%2FOrOOzuHpC2xfW7m1XXug0cvWK0JuYAzzrm8qiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLT%2Fcn5I3OlMa9bUJCrcA%2BVVOAEAOaR%2FnrumU2Q6OsM93%2B%2F8iG0znzLCJRWlhtV%2BWupsATsTpWB10z7hQJFTvslYdwTxx7z4Pfrl%2FA0GjgXMRK1L%2BvznAPo2BMZDbclBn2qIKZhkk8poKMqw%2Fp0ic2Tgcx5DhwR1rJKuINBvQQmEzJPBICKlEen6Sj7A3vnW0Oc%2FPp0MmjExK5eRNcniyV8BUyHJjymMvtzzOON814hyitmFkXv%2BsnO%2BT5IOXXQMER%2FvBNvi2HyLTsIxnQB2e1oYQDuUvYlTZDEUFc7GuUVANRX2R6mntVNpqUnRnSQjdf4mbrOy4rBqhWInp41enVnPk36h3G2OHTIJG6uPpYfWK3QAbgJ%2BqbHPTtSQ2pPpWZySwwHiAk%2Fisx6xt3DpI%2FeVP9Bp2vzd3DGA8bWEarAwNI5dK35RF64effF%2FJ%2BT4CFTF9TWjPxVw4yqGsy9X66RTCYy1OO9Q56aDMyacQbLivgdLtRrnwFRToZl1GxXWNdoCxShqZTarvOzxAFVr1SJMckvteJjUUxGGdN3gRaYzSnVI4YeXU24oYp6TAXRHuVdRaJxuuDEjSnBsi%2BzxOuVYK%2FVLJuCXgDBmwO9%2FeQeQMdDf1oKRrSTwVfuAXeG86tpQ5nqGPxyYGGIsMJ6U%2BrwGOqUB9SAjXJhTuT41QiGaU1eenfFsbruxxR4CLcl8YV1RUrFZYcigf7S%2F6WvvS%2B%2FYSVsvMqrHEcHVU7H4%2FOJbHeOvJ%2Fen%2B6i4unLV15Wt%2FEvlDEJZI1G3Bhdrhoaahq2kPvcef9Bo0usWw4GqYjOXB0J9TfWgnDZDo9k%2FDNVU1tOmPo%2FB%2B2LYXGNXs3LJ5uXbUYBw7NH8rkWlrSfJrdwKPoRVP3Fw7tru&X-Amz-Signature=6e75bd63bc45defc21d6ebdeb271e1fe9b4f0cab5f6976dfcd5e14952c41fa8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGTBW76P%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T211309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDp3Dtz7YUOY5sXQ1deZ9fcmwTgjIzMn8KGPCkqEh7aUgIgXpg%2FcJofis1LVGNuGsWiTDRK5sv0OuTI5NDNh9xx7ewqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCjueeUddU%2Ffl45NsSrcA9R9zBciBsfv9ltkS5fWa%2BsGUvrAVf12han4YDjzwwgCulJNEqw%2Bdgt%2BL7Zd9XHT6KR0l2hBzNcmcP3PZJo4pw%2FVEbwHZo96LZ%2FIho5EFLcS%2FGvN4dFfD8OFfHRtbMmg8QbQ0wvnhtrL7Svqq9FLdKXFYlp%2FNW3xlikNEtGloIfl5eX4eSlbK7raIG2pp3KK2fqG7%2FVvtZwi1dWSC3ZoSeqG7UVqC%2FNqe9LhG%2BK7Hc4zh8kSf%2BPlghiIyW0wTYiMzQBWj2%2BgR0gBX3OiV22%2B9NBeezg5WODSc1fu8HeBQ%2BcHYG49W%2F3nNAUu3UEqkZqvn9KB8rwmVVTu9ZiaatPkOC3eEC%2FapRIQNVFnbSLNeyITNFd2dky4z0Jx%2Ftb6TJUDzfWcDEJXvIPxV2ClormnrnMWcw7bdD2Seic2ADMP88VF9rWfLdFkKb%2FJN8B0HtlKZoi%2Fd%2Bwo1D5oSHuxMGEMPXLxmfrNmZUgVxMykegl9g639zGxEOs4i0keGr8p%2BDKrhJZY8OhScqT1xfSld3wPEo6HqMj7MvF%2FCqVORyJM5YzFji1alCxfWyq3jxidFxdqICtMPM6uu6bBcv1XM%2FvzrHOZ%2BNeJjrHxKcIC5mahyOc1cUX9UUD3gSItZdnrMPaT%2BrwGOqUBSwyo7nLZZKGyXgBdCV50dx0qMJkWItBozylFS7g%2BQwK%2FyxiC4cznSh19E5kJN2R8L08RvSESvAiR7%2FFGK05oJVCYuUZTbV3exAwKlwz3uj01vIuFku%2FSHya3vufmMGzGtz6%2BLhICKiEAWPpAICAQK5v6QKtcYPndp%2Fw%2FZf0i7TB%2BcUJB%2FfR4jOXxrydTYdwMx%2ByjexVaI9ZHrobfynFFL6ROD6za&X-Amz-Signature=c16aba74671d4e6aebc0b19d9be0598780691f0ec8937d54b1ac928bf7c1aa2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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