

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5OEA6CR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFp92Fw7l70bCobrAuoyrt6dKlfNOXq9fjLb5XCHlJsIAiEAivCswa7UwcVL14HFGRL315ROKAVrL6oceLsxRKy%2FkPgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7yP52mq6ogsbPBqSrcA9zg8nEHYrg9Qo4gALg5bd1%2F0%2BWzAbxvrBXhFLj1ScchvnVOXDmKPgIEo78cfLZA%2FanvcMv9X2s873vIb9ip%2BCOf0R1dq57YKGqv%2FKcltj6fZEvNB4U0BoLuADse9Z%2BFlF%2B8xk1rn%2B0ANp4W00a5wTtctd1Cun%2FfQuf2ns%2FgPl8HJcBZ421pi4UVY6cfnDw%2FdOLHjfFxkKa0Cf5OMpVEpc9Cqd3QPRDCozDQ8FMKsyU2dMMaqWR5mXLhP%2FzouASVM5SkeJVh9sZ4x0GEg1grjQkUWEu42QxugxBYowL%2F4Z8c9WFcmt489AnBPsEXhIKMf8AYOg5cZYabJ4ZsrwGqe7l6RtifCYbjjk7CWdmsMl7JWdE4Qsgdteo9N4yWH6FYhjXctG7Up7%2FLUcmBqWr6NO%2BX4v%2Brjtk7D7I4VSCsNv65iBEbgGM%2Fd6sPkyA1BL7yld4zcpg2Csq7BG%2BAN3OxswRsLnwe1jo2K0HmwzCo%2BE0DQuqj4a5zsGt3%2BQri3mxWSHuas0hee7BWNzXnmXgaqe60wpAqyirLfaX%2FFSnWcah3VSl4ib7WYmHayiYEn5RzfyBq43Wm%2FNKxpohSk4pWjpvZu2t%2BXPXnWGwA6%2BN2v40V2uc1Dyy8jESvchL3ML6k97wGOqUB06Aif4xB9kdpip90NDSNCh%2FpFqRHJEKsMW3KpJPwGS3sLK37jtPPqOLYJLCwPD%2BmtMZShBkqkBD3%2B%2BiX1%2BEePRB0KWgEaPwEHCH0q%2F%2BZdWNHdFnaLOXHVxdLg%2BweMu6WUNoUG%2FgOGIcUVRIZcrtNHGzBI7posSUbQJ5jyyGYdZdvIJXI%2B1vF40PtF7zFb1O0SBNt6nZ5OwPkTL0bXrVWJItFMt%2F8&X-Amz-Signature=e4ecd0b6ae84a2b77e4581a76ffe9c2de3669e0a187ca17d496a8d6e3c42395c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5OEA6CR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFp92Fw7l70bCobrAuoyrt6dKlfNOXq9fjLb5XCHlJsIAiEAivCswa7UwcVL14HFGRL315ROKAVrL6oceLsxRKy%2FkPgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7yP52mq6ogsbPBqSrcA9zg8nEHYrg9Qo4gALg5bd1%2F0%2BWzAbxvrBXhFLj1ScchvnVOXDmKPgIEo78cfLZA%2FanvcMv9X2s873vIb9ip%2BCOf0R1dq57YKGqv%2FKcltj6fZEvNB4U0BoLuADse9Z%2BFlF%2B8xk1rn%2B0ANp4W00a5wTtctd1Cun%2FfQuf2ns%2FgPl8HJcBZ421pi4UVY6cfnDw%2FdOLHjfFxkKa0Cf5OMpVEpc9Cqd3QPRDCozDQ8FMKsyU2dMMaqWR5mXLhP%2FzouASVM5SkeJVh9sZ4x0GEg1grjQkUWEu42QxugxBYowL%2F4Z8c9WFcmt489AnBPsEXhIKMf8AYOg5cZYabJ4ZsrwGqe7l6RtifCYbjjk7CWdmsMl7JWdE4Qsgdteo9N4yWH6FYhjXctG7Up7%2FLUcmBqWr6NO%2BX4v%2Brjtk7D7I4VSCsNv65iBEbgGM%2Fd6sPkyA1BL7yld4zcpg2Csq7BG%2BAN3OxswRsLnwe1jo2K0HmwzCo%2BE0DQuqj4a5zsGt3%2BQri3mxWSHuas0hee7BWNzXnmXgaqe60wpAqyirLfaX%2FFSnWcah3VSl4ib7WYmHayiYEn5RzfyBq43Wm%2FNKxpohSk4pWjpvZu2t%2BXPXnWGwA6%2BN2v40V2uc1Dyy8jESvchL3ML6k97wGOqUB06Aif4xB9kdpip90NDSNCh%2FpFqRHJEKsMW3KpJPwGS3sLK37jtPPqOLYJLCwPD%2BmtMZShBkqkBD3%2B%2BiX1%2BEePRB0KWgEaPwEHCH0q%2F%2BZdWNHdFnaLOXHVxdLg%2BweMu6WUNoUG%2FgOGIcUVRIZcrtNHGzBI7posSUbQJ5jyyGYdZdvIJXI%2B1vF40PtF7zFb1O0SBNt6nZ5OwPkTL0bXrVWJItFMt%2F8&X-Amz-Signature=9a33b8fe18b64b990b0a9f3724b8c718b8dd555f6f65a1c287b598cc7d5a7048&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5OEA6CR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFp92Fw7l70bCobrAuoyrt6dKlfNOXq9fjLb5XCHlJsIAiEAivCswa7UwcVL14HFGRL315ROKAVrL6oceLsxRKy%2FkPgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7yP52mq6ogsbPBqSrcA9zg8nEHYrg9Qo4gALg5bd1%2F0%2BWzAbxvrBXhFLj1ScchvnVOXDmKPgIEo78cfLZA%2FanvcMv9X2s873vIb9ip%2BCOf0R1dq57YKGqv%2FKcltj6fZEvNB4U0BoLuADse9Z%2BFlF%2B8xk1rn%2B0ANp4W00a5wTtctd1Cun%2FfQuf2ns%2FgPl8HJcBZ421pi4UVY6cfnDw%2FdOLHjfFxkKa0Cf5OMpVEpc9Cqd3QPRDCozDQ8FMKsyU2dMMaqWR5mXLhP%2FzouASVM5SkeJVh9sZ4x0GEg1grjQkUWEu42QxugxBYowL%2F4Z8c9WFcmt489AnBPsEXhIKMf8AYOg5cZYabJ4ZsrwGqe7l6RtifCYbjjk7CWdmsMl7JWdE4Qsgdteo9N4yWH6FYhjXctG7Up7%2FLUcmBqWr6NO%2BX4v%2Brjtk7D7I4VSCsNv65iBEbgGM%2Fd6sPkyA1BL7yld4zcpg2Csq7BG%2BAN3OxswRsLnwe1jo2K0HmwzCo%2BE0DQuqj4a5zsGt3%2BQri3mxWSHuas0hee7BWNzXnmXgaqe60wpAqyirLfaX%2FFSnWcah3VSl4ib7WYmHayiYEn5RzfyBq43Wm%2FNKxpohSk4pWjpvZu2t%2BXPXnWGwA6%2BN2v40V2uc1Dyy8jESvchL3ML6k97wGOqUB06Aif4xB9kdpip90NDSNCh%2FpFqRHJEKsMW3KpJPwGS3sLK37jtPPqOLYJLCwPD%2BmtMZShBkqkBD3%2B%2BiX1%2BEePRB0KWgEaPwEHCH0q%2F%2BZdWNHdFnaLOXHVxdLg%2BweMu6WUNoUG%2FgOGIcUVRIZcrtNHGzBI7posSUbQJ5jyyGYdZdvIJXI%2B1vF40PtF7zFb1O0SBNt6nZ5OwPkTL0bXrVWJItFMt%2F8&X-Amz-Signature=4e6ea21c81bc981a72f2ef1fb04d2e03eeec53c9ea5aa2d60990ea1217aff4f3&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=eaf774fd5828241ca6fe86deec4c26b4283d969d8fdd4eaa69988a0f2960a407&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PNKTDTT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1u20Mio6AfNabtSdJCJJFWvPHaOVZBC4iRs1IucV6gAIhALmuI8cxZlQVfeuPsaUCPDM81Hz7WbmjeapV8nmHXDETKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvypCRy9pT3ldMT1Iq3AMNvZout6CR%2BKznoYT6PpmOtoGd4f0RL2ykgJnLby62udj5W59%2F9xzInIsZv%2F%2Fe89kqvjn87CMaGr6NSdCrgSiTQtNYFUuE%2BVN5K3g8qk7eW0gaNT8N2dAUxHRzfPCXjTUlDoYefVOtFHx4ySRIELSkWcsQfDV9l2jzSkDlwhb25XSDNichOWcoRuw4oemDFz%2FpKl93FDKcTpaoqxaXOUEmfI1Ocznr1y6qrjLoMcY%2BB%2FSMAOj9AOJqBbgESMGIfxec1ctwlb2ubsDKlUlL3gtYmmjcZ22SRozp8ROn4eqmI6U1Al%2Bf0bNA%2FF5A138iGjq3TLsvKEfC3awcJtU0pmfGGNFQI9nSgw9M8ypr%2BvVoS9SuebFOlUdibm4ErYuVhIddvKean7qyDtizLqY6WHb%2FhJJU%2BMhmFJOeTA8tpXJDxp0Dd2wjqQtoF9lEQiIABGoS6DDz7ZQiBqse3WIqEJ1yR9o2Ti52vql4jv1YlVJGScelE43ZZWWUF108Cbq1tjyxm7Of2xaMP4hI2kXS1I08oBpqohSsSQAPfjOOL9FbY%2FJ3%2F7zOSFhlNJ7Yamx%2FZsn9iRuq%2Bo3f1TYQ7sBH06Iy9l5nbF%2BzQQOKu07j3YS%2F90kGX7U%2FCBCQgMRF1DDRpPe8BjqkAe9jDsXntGYsjjj%2FvKlKNDMNUkd1trsvdnfmMtZ4jvqcodokjQc2F4Rzg3lLaU6mY80wKZ3wzeGLYrAzAwPIJVlqHH93KBZh3m8kvr%2FA3IdK4d3sM4m%2FSbxNn5SRpdx07bkSlZUi4HU6iNCFtnWBGwZ%2FB4TOwlZVdKo8je4wV2IsO5b4nrXb5uumvhsCARnXQxONFvbyiWU2YIhmaVEeugs%2BWD2k&X-Amz-Signature=f4a2758768b88bacf57d50f301e5640599fbd07879976f05007002bbec76039f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5OEA6CR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFp92Fw7l70bCobrAuoyrt6dKlfNOXq9fjLb5XCHlJsIAiEAivCswa7UwcVL14HFGRL315ROKAVrL6oceLsxRKy%2FkPgqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG7yP52mq6ogsbPBqSrcA9zg8nEHYrg9Qo4gALg5bd1%2F0%2BWzAbxvrBXhFLj1ScchvnVOXDmKPgIEo78cfLZA%2FanvcMv9X2s873vIb9ip%2BCOf0R1dq57YKGqv%2FKcltj6fZEvNB4U0BoLuADse9Z%2BFlF%2B8xk1rn%2B0ANp4W00a5wTtctd1Cun%2FfQuf2ns%2FgPl8HJcBZ421pi4UVY6cfnDw%2FdOLHjfFxkKa0Cf5OMpVEpc9Cqd3QPRDCozDQ8FMKsyU2dMMaqWR5mXLhP%2FzouASVM5SkeJVh9sZ4x0GEg1grjQkUWEu42QxugxBYowL%2F4Z8c9WFcmt489AnBPsEXhIKMf8AYOg5cZYabJ4ZsrwGqe7l6RtifCYbjjk7CWdmsMl7JWdE4Qsgdteo9N4yWH6FYhjXctG7Up7%2FLUcmBqWr6NO%2BX4v%2Brjtk7D7I4VSCsNv65iBEbgGM%2Fd6sPkyA1BL7yld4zcpg2Csq7BG%2BAN3OxswRsLnwe1jo2K0HmwzCo%2BE0DQuqj4a5zsGt3%2BQri3mxWSHuas0hee7BWNzXnmXgaqe60wpAqyirLfaX%2FFSnWcah3VSl4ib7WYmHayiYEn5RzfyBq43Wm%2FNKxpohSk4pWjpvZu2t%2BXPXnWGwA6%2BN2v40V2uc1Dyy8jESvchL3ML6k97wGOqUB06Aif4xB9kdpip90NDSNCh%2FpFqRHJEKsMW3KpJPwGS3sLK37jtPPqOLYJLCwPD%2BmtMZShBkqkBD3%2B%2BiX1%2BEePRB0KWgEaPwEHCH0q%2F%2BZdWNHdFnaLOXHVxdLg%2BweMu6WUNoUG%2FgOGIcUVRIZcrtNHGzBI7posSUbQJ5jyyGYdZdvIJXI%2B1vF40PtF7zFb1O0SBNt6nZ5OwPkTL0bXrVWJItFMt%2F8&X-Amz-Signature=839a1795bb82489b45b966242ee08c2529d4dab8c90154e20792f0b118008a89&X-Amz-SignedHeaders=host&x-id=GetObject)
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