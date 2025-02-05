

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUS7PNAH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIDqvDABAACxIDRCxHO779YD3J2tTOnAtIwQSSqrpgmdfAiEA7NMSZL6yK8541braCIEjscrdAzdq5BW1EzZJ9aMccLgq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHmzSTLoPadHpCizyCrcA5egaEUC5nyAVbKm9jSlQJDYm%2BmxiEHeKU4BAAQksUvb1W%2FE4abuD3ERzGuD4o4PwzFeWHs59Gwzsp2sXbE2cBO848pIXIzEa3OItQUM13Ex1%2BVs%2BdwfO%2Fps3Dib0gHRop5Qe%2FdU0rJiMNsYwzjSaf6VzEI1sStvLk90TzQz3Qhpo%2BoH33WShWOCVw7W70ugmHNYnSNvxoJEnFm4rUmg6YCr7U7ykdS1YNy85JMrFpeTiTZhhCQBIbn73pv9myLT9YTtucUxjENwRo8xot9DZcFALfJf0ZKo0jazXbCueCmrrqEkD8nFM0q1E6y02RCzWCvi%2ByEiEjjsodOfsA4t5XW9ONeOHKGU1h2oWpSJQbk4nUwvVvWPneENDZJo%2B3Bp40oTj%2Fvqx%2BSP1zhTEmjRFQCjqNuEIqvNPOkAPr5bnmnxuI21K8iChReZjgTv0KW4hYkVH4B8OkX3dspvgb0T1Y%2FQIvYtpOAq%2B8Barx9hzI5Ro4XUhu%2FCKNILvlT2IHzRzN0rAzg2Mkfn%2Bdnmc7ubmGPj6o1N7%2Bhzyih0RvRDmox8GCsimKbntyaSuTmYEOPu6AhRBEcLytpMfiRe4prOYbZhekLIxnXWbKM2G7kROvG0zrj5lWtE5SrpUUpBMK66jr0GOqUBamRGEhqeQNWWjPBP9RuIpETjHFi5O1NxG9fjIHq0qNuKOGR%2Fd2EH3npsKhx13b3w%2FlBDGauq7nP%2FNiTSv4HE5iZjsGTa7Y%2FOKrXlW3Tw0qNz8JPzmz%2BTNTYiOQYUA9m3xVCMaO0umqR7YIWuUrtLIr87JtpTDY%2BJwPdNGH2Pn%2Bxg2GU3XI%2BVEZsWEyZM6ZrEe%2BZuBbYMB0LzUI%2F2szvteAKshAl8&X-Amz-Signature=4235f803649d7314dabbca93e5deaba6093cf020d9f140bca9ccd1bf7e8482a4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUS7PNAH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIDqvDABAACxIDRCxHO779YD3J2tTOnAtIwQSSqrpgmdfAiEA7NMSZL6yK8541braCIEjscrdAzdq5BW1EzZJ9aMccLgq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHmzSTLoPadHpCizyCrcA5egaEUC5nyAVbKm9jSlQJDYm%2BmxiEHeKU4BAAQksUvb1W%2FE4abuD3ERzGuD4o4PwzFeWHs59Gwzsp2sXbE2cBO848pIXIzEa3OItQUM13Ex1%2BVs%2BdwfO%2Fps3Dib0gHRop5Qe%2FdU0rJiMNsYwzjSaf6VzEI1sStvLk90TzQz3Qhpo%2BoH33WShWOCVw7W70ugmHNYnSNvxoJEnFm4rUmg6YCr7U7ykdS1YNy85JMrFpeTiTZhhCQBIbn73pv9myLT9YTtucUxjENwRo8xot9DZcFALfJf0ZKo0jazXbCueCmrrqEkD8nFM0q1E6y02RCzWCvi%2ByEiEjjsodOfsA4t5XW9ONeOHKGU1h2oWpSJQbk4nUwvVvWPneENDZJo%2B3Bp40oTj%2Fvqx%2BSP1zhTEmjRFQCjqNuEIqvNPOkAPr5bnmnxuI21K8iChReZjgTv0KW4hYkVH4B8OkX3dspvgb0T1Y%2FQIvYtpOAq%2B8Barx9hzI5Ro4XUhu%2FCKNILvlT2IHzRzN0rAzg2Mkfn%2Bdnmc7ubmGPj6o1N7%2Bhzyih0RvRDmox8GCsimKbntyaSuTmYEOPu6AhRBEcLytpMfiRe4prOYbZhekLIxnXWbKM2G7kROvG0zrj5lWtE5SrpUUpBMK66jr0GOqUBamRGEhqeQNWWjPBP9RuIpETjHFi5O1NxG9fjIHq0qNuKOGR%2Fd2EH3npsKhx13b3w%2FlBDGauq7nP%2FNiTSv4HE5iZjsGTa7Y%2FOKrXlW3Tw0qNz8JPzmz%2BTNTYiOQYUA9m3xVCMaO0umqR7YIWuUrtLIr87JtpTDY%2BJwPdNGH2Pn%2Bxg2GU3XI%2BVEZsWEyZM6ZrEe%2BZuBbYMB0LzUI%2F2szvteAKshAl8&X-Amz-Signature=e0253a5650729622b7a593a8b176252adaba3090ea8da61bbaff480162650d35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUS7PNAH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIDqvDABAACxIDRCxHO779YD3J2tTOnAtIwQSSqrpgmdfAiEA7NMSZL6yK8541braCIEjscrdAzdq5BW1EzZJ9aMccLgq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHmzSTLoPadHpCizyCrcA5egaEUC5nyAVbKm9jSlQJDYm%2BmxiEHeKU4BAAQksUvb1W%2FE4abuD3ERzGuD4o4PwzFeWHs59Gwzsp2sXbE2cBO848pIXIzEa3OItQUM13Ex1%2BVs%2BdwfO%2Fps3Dib0gHRop5Qe%2FdU0rJiMNsYwzjSaf6VzEI1sStvLk90TzQz3Qhpo%2BoH33WShWOCVw7W70ugmHNYnSNvxoJEnFm4rUmg6YCr7U7ykdS1YNy85JMrFpeTiTZhhCQBIbn73pv9myLT9YTtucUxjENwRo8xot9DZcFALfJf0ZKo0jazXbCueCmrrqEkD8nFM0q1E6y02RCzWCvi%2ByEiEjjsodOfsA4t5XW9ONeOHKGU1h2oWpSJQbk4nUwvVvWPneENDZJo%2B3Bp40oTj%2Fvqx%2BSP1zhTEmjRFQCjqNuEIqvNPOkAPr5bnmnxuI21K8iChReZjgTv0KW4hYkVH4B8OkX3dspvgb0T1Y%2FQIvYtpOAq%2B8Barx9hzI5Ro4XUhu%2FCKNILvlT2IHzRzN0rAzg2Mkfn%2Bdnmc7ubmGPj6o1N7%2Bhzyih0RvRDmox8GCsimKbntyaSuTmYEOPu6AhRBEcLytpMfiRe4prOYbZhekLIxnXWbKM2G7kROvG0zrj5lWtE5SrpUUpBMK66jr0GOqUBamRGEhqeQNWWjPBP9RuIpETjHFi5O1NxG9fjIHq0qNuKOGR%2Fd2EH3npsKhx13b3w%2FlBDGauq7nP%2FNiTSv4HE5iZjsGTa7Y%2FOKrXlW3Tw0qNz8JPzmz%2BTNTYiOQYUA9m3xVCMaO0umqR7YIWuUrtLIr87JtpTDY%2BJwPdNGH2Pn%2Bxg2GU3XI%2BVEZsWEyZM6ZrEe%2BZuBbYMB0LzUI%2F2szvteAKshAl8&X-Amz-Signature=74f97f42e0752a293ea4c665110076dc3a578596e6d3bad602ccc7b2bfbfb1d2&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624JATCPK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD9Sr3iGMKBITCl4InWWuPey1rUfR4AtpFjB%2BFXxYsRDAIhAKwPoMjU9QFi5SLlakbVlXmsMQYfIdX0LFQVTV5u%2FNm0Kv8DCEoQABoMNjM3NDIzMTgzODA1IgzQqTEzF8nkTJJklLcq3AOVnpwVf%2F0ApUe6JcpPqeal1FSE3Pq60%2FZ5zk4WgMkEmRHOAS%2Bbn7hljUePfqnP4zzx9hMlZO4pcP3lfUGZFm5Zo9rJiRXtLaykjg9wOPEZhW2nc8FrAdntdBtLIeybcW5Hgl8TM271pEp67R9OXI2Vmg%2FyAgA2pV0Wdqnw8UcJcsY81ikE%2BkACwn3mF1Y4%2F6YtCR01F89uJyTCKteBTlGhAFBP8JdwCmPYVq0Gj%2Fekm4RVcr942AX3bic7846hwjTkwJoTD9A2gb4TC49KuO8rOu0klkJEj2I%2F8lNBhL2WxN1LcpqV%2FvtexD5hRAmoaISSapkEsNQ15Sd6Cwzi2Va8vR1QyX8wlS0kLy3Qr1KKRljJFCc5HtVC8rewIroivFzkTrR3y7AEuy3iW7qTOCrQGJtK%2BRYchr4NMTXhJPJoJFR0oamjLcKmCY%2Bo8IJXZ7ffNzjfirYVa%2BNmPtw2lzTbP8NJlXTjL4ALuSV6JKgyTFjBcRtJk5qnqYUj0mkinVrmNwMzOmdMnPOHdJqv8TMZ7FiemhSUv1pFvSgpcu8SCrmTYqrKOiGhbFVxspXtmixU4MaxIkmoDodT%2BHdQ%2BvYw76Qw0L9tFrQ2%2FU1eqwa%2BpMkBHrFhdPOzdamanjDEuo69BjqkAUEUVrljq4X%2FAOAUhWjVahWVcnUhIdcdu8ObSs5os4IRJdG%2Fp84sr%2FitPK6yTHa9NhBoAeB%2FkQ0phoDJ2v36ZqfzoVAT3u7VLMEcXtBccCTaVmXUGluo0hlWfZV7ItHlVeUxKQHvVF3qweH6eeGlcH7kFRqja7JqiGXZ6E40nD%2B91Gqc5RnDV9U8vIUmYyms35yzkzju0i1msG471a6QUino4GcZ&X-Amz-Signature=4b6d85b5e6af0a152f01f4c6e9a4694f86166ad7abc479d985214becbc978756&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624JATCPK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD9Sr3iGMKBITCl4InWWuPey1rUfR4AtpFjB%2BFXxYsRDAIhAKwPoMjU9QFi5SLlakbVlXmsMQYfIdX0LFQVTV5u%2FNm0Kv8DCEoQABoMNjM3NDIzMTgzODA1IgzQqTEzF8nkTJJklLcq3AOVnpwVf%2F0ApUe6JcpPqeal1FSE3Pq60%2FZ5zk4WgMkEmRHOAS%2Bbn7hljUePfqnP4zzx9hMlZO4pcP3lfUGZFm5Zo9rJiRXtLaykjg9wOPEZhW2nc8FrAdntdBtLIeybcW5Hgl8TM271pEp67R9OXI2Vmg%2FyAgA2pV0Wdqnw8UcJcsY81ikE%2BkACwn3mF1Y4%2F6YtCR01F89uJyTCKteBTlGhAFBP8JdwCmPYVq0Gj%2Fekm4RVcr942AX3bic7846hwjTkwJoTD9A2gb4TC49KuO8rOu0klkJEj2I%2F8lNBhL2WxN1LcpqV%2FvtexD5hRAmoaISSapkEsNQ15Sd6Cwzi2Va8vR1QyX8wlS0kLy3Qr1KKRljJFCc5HtVC8rewIroivFzkTrR3y7AEuy3iW7qTOCrQGJtK%2BRYchr4NMTXhJPJoJFR0oamjLcKmCY%2Bo8IJXZ7ffNzjfirYVa%2BNmPtw2lzTbP8NJlXTjL4ALuSV6JKgyTFjBcRtJk5qnqYUj0mkinVrmNwMzOmdMnPOHdJqv8TMZ7FiemhSUv1pFvSgpcu8SCrmTYqrKOiGhbFVxspXtmixU4MaxIkmoDodT%2BHdQ%2BvYw76Qw0L9tFrQ2%2FU1eqwa%2BpMkBHrFhdPOzdamanjDEuo69BjqkAUEUVrljq4X%2FAOAUhWjVahWVcnUhIdcdu8ObSs5os4IRJdG%2Fp84sr%2FitPK6yTHa9NhBoAeB%2FkQ0phoDJ2v36ZqfzoVAT3u7VLMEcXtBccCTaVmXUGluo0hlWfZV7ItHlVeUxKQHvVF3qweH6eeGlcH7kFRqja7JqiGXZ6E40nD%2B91Gqc5RnDV9U8vIUmYyms35yzkzju0i1msG471a6QUino4GcZ&X-Amz-Signature=b085c82ded7f66e58a56831b2dfc74fd217e8e9e4c7982f987674188ac638d8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUS7PNAH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIDqvDABAACxIDRCxHO779YD3J2tTOnAtIwQSSqrpgmdfAiEA7NMSZL6yK8541braCIEjscrdAzdq5BW1EzZJ9aMccLgq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHmzSTLoPadHpCizyCrcA5egaEUC5nyAVbKm9jSlQJDYm%2BmxiEHeKU4BAAQksUvb1W%2FE4abuD3ERzGuD4o4PwzFeWHs59Gwzsp2sXbE2cBO848pIXIzEa3OItQUM13Ex1%2BVs%2BdwfO%2Fps3Dib0gHRop5Qe%2FdU0rJiMNsYwzjSaf6VzEI1sStvLk90TzQz3Qhpo%2BoH33WShWOCVw7W70ugmHNYnSNvxoJEnFm4rUmg6YCr7U7ykdS1YNy85JMrFpeTiTZhhCQBIbn73pv9myLT9YTtucUxjENwRo8xot9DZcFALfJf0ZKo0jazXbCueCmrrqEkD8nFM0q1E6y02RCzWCvi%2ByEiEjjsodOfsA4t5XW9ONeOHKGU1h2oWpSJQbk4nUwvVvWPneENDZJo%2B3Bp40oTj%2Fvqx%2BSP1zhTEmjRFQCjqNuEIqvNPOkAPr5bnmnxuI21K8iChReZjgTv0KW4hYkVH4B8OkX3dspvgb0T1Y%2FQIvYtpOAq%2B8Barx9hzI5Ro4XUhu%2FCKNILvlT2IHzRzN0rAzg2Mkfn%2Bdnmc7ubmGPj6o1N7%2Bhzyih0RvRDmox8GCsimKbntyaSuTmYEOPu6AhRBEcLytpMfiRe4prOYbZhekLIxnXWbKM2G7kROvG0zrj5lWtE5SrpUUpBMK66jr0GOqUBamRGEhqeQNWWjPBP9RuIpETjHFi5O1NxG9fjIHq0qNuKOGR%2Fd2EH3npsKhx13b3w%2FlBDGauq7nP%2FNiTSv4HE5iZjsGTa7Y%2FOKrXlW3Tw0qNz8JPzmz%2BTNTYiOQYUA9m3xVCMaO0umqR7YIWuUrtLIr87JtpTDY%2BJwPdNGH2Pn%2Bxg2GU3XI%2BVEZsWEyZM6ZrEe%2BZuBbYMB0LzUI%2F2szvteAKshAl8&X-Amz-Signature=30d485cd617a1c0e753c37b656f6d0ec70c3cf7b510d4e2537e41d424269296c&X-Amz-SignedHeaders=host&x-id=GetObject)
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