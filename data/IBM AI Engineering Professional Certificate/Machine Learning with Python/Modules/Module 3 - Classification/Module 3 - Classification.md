

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJKP5QT4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkrBZmkgHQTVTSltf%2BeJbXrOiJB3vL7OrMRj5wtOiZ7AiBC5ib1%2BgZ1UUDJu5ezCewGcwzguGEG68Huv8tX1aWZeCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2dL8Cnrw5RFvnFdyKtwDf2KGeymr%2FiFAO5DAS71VS9Sa8%2Fmar26mresgEYKGg7f1zLEbxNabKLlnSlK4YaTYAJOLsCz22f2Hm3b9MsWDnCN9JqJOx4otqD57wGa1TBfN%2BaxZA29C6nKkx7vz0aDEM0ougLwXO1wQRI7RF5IS9JXectMu8yLT9O8KRtF1GAdE3qw2Dg%2BEgIekqohIZAApc45Uk841%2BiRlHAfdyjGjcU1u7Eprbve5uoefxbzt5YlOwADhe1Jw8aN%2FiCj6klgylwtPIv48llABLu6Gpkxvz6Oie%2FEMIt0nEae%2BEKXm6oxWhlVVGIU3ChdSmA%2BuVTiSXCZaF29gP%2FEK6iALK3bYjYfrDUCoWY0oJoTPKqxEpOnTTTH2DjO%2FbACXxJaIv1p4ZU5zfFL25bIb030Vl3Y6yotbBB51eYrZY2ZoYMmxwnh6yUpnTNhyIwnJS%2BUIAu98XHRvNyJyeDbuwpOYiloYUUAHs2gFld4vPY%2F5JvtL2ALHPEtEc5RlPtds00wnaaxE2i7eFUXUENDEp3Kgd5u07UY2sGf%2FVsntYVZiLDdb3m5deeOwEo2psQSyIWzjgNHFcMOhHEzhyamepfWROZm6W5crJ%2BbZIjiS0VmNv1DliNXFYqn9tU7es5V0J4wwwNX%2BvAY6pgF%2B6FhWpaGIrvmZDqy080hwOcHmbCd5%2FGehhqvXHB9rhM5j9ia3452RD6VCnLs2dLwH2%2B1Hy4nLG5ITlCz9a1XpgqBudzh8UzD83Dal%2Fqd9xS9FcB6Wip2URR4iEBG95cbu2%2FE7XFrvpsWEYRXKYBEhBAks%2F14g%2FrhqPn9bLfHLnXekBgmLo7EiTPn%2FCpW%2FxdvePtwng6YzY72l14T7eMpi%2BTLu6%2BX6&X-Amz-Signature=0143b422f89773f4f3149667d01dd8c8b84b6ccf482e35aae97bcf59a216ba41&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJKP5QT4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkrBZmkgHQTVTSltf%2BeJbXrOiJB3vL7OrMRj5wtOiZ7AiBC5ib1%2BgZ1UUDJu5ezCewGcwzguGEG68Huv8tX1aWZeCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2dL8Cnrw5RFvnFdyKtwDf2KGeymr%2FiFAO5DAS71VS9Sa8%2Fmar26mresgEYKGg7f1zLEbxNabKLlnSlK4YaTYAJOLsCz22f2Hm3b9MsWDnCN9JqJOx4otqD57wGa1TBfN%2BaxZA29C6nKkx7vz0aDEM0ougLwXO1wQRI7RF5IS9JXectMu8yLT9O8KRtF1GAdE3qw2Dg%2BEgIekqohIZAApc45Uk841%2BiRlHAfdyjGjcU1u7Eprbve5uoefxbzt5YlOwADhe1Jw8aN%2FiCj6klgylwtPIv48llABLu6Gpkxvz6Oie%2FEMIt0nEae%2BEKXm6oxWhlVVGIU3ChdSmA%2BuVTiSXCZaF29gP%2FEK6iALK3bYjYfrDUCoWY0oJoTPKqxEpOnTTTH2DjO%2FbACXxJaIv1p4ZU5zfFL25bIb030Vl3Y6yotbBB51eYrZY2ZoYMmxwnh6yUpnTNhyIwnJS%2BUIAu98XHRvNyJyeDbuwpOYiloYUUAHs2gFld4vPY%2F5JvtL2ALHPEtEc5RlPtds00wnaaxE2i7eFUXUENDEp3Kgd5u07UY2sGf%2FVsntYVZiLDdb3m5deeOwEo2psQSyIWzjgNHFcMOhHEzhyamepfWROZm6W5crJ%2BbZIjiS0VmNv1DliNXFYqn9tU7es5V0J4wwwNX%2BvAY6pgF%2B6FhWpaGIrvmZDqy080hwOcHmbCd5%2FGehhqvXHB9rhM5j9ia3452RD6VCnLs2dLwH2%2B1Hy4nLG5ITlCz9a1XpgqBudzh8UzD83Dal%2Fqd9xS9FcB6Wip2URR4iEBG95cbu2%2FE7XFrvpsWEYRXKYBEhBAks%2F14g%2FrhqPn9bLfHLnXekBgmLo7EiTPn%2FCpW%2FxdvePtwng6YzY72l14T7eMpi%2BTLu6%2BX6&X-Amz-Signature=2ae0745780dc1f3fad2140a7b72ad938ffd58f1117ca3ceebe4f89816f5d5a80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJKP5QT4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkrBZmkgHQTVTSltf%2BeJbXrOiJB3vL7OrMRj5wtOiZ7AiBC5ib1%2BgZ1UUDJu5ezCewGcwzguGEG68Huv8tX1aWZeCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2dL8Cnrw5RFvnFdyKtwDf2KGeymr%2FiFAO5DAS71VS9Sa8%2Fmar26mresgEYKGg7f1zLEbxNabKLlnSlK4YaTYAJOLsCz22f2Hm3b9MsWDnCN9JqJOx4otqD57wGa1TBfN%2BaxZA29C6nKkx7vz0aDEM0ougLwXO1wQRI7RF5IS9JXectMu8yLT9O8KRtF1GAdE3qw2Dg%2BEgIekqohIZAApc45Uk841%2BiRlHAfdyjGjcU1u7Eprbve5uoefxbzt5YlOwADhe1Jw8aN%2FiCj6klgylwtPIv48llABLu6Gpkxvz6Oie%2FEMIt0nEae%2BEKXm6oxWhlVVGIU3ChdSmA%2BuVTiSXCZaF29gP%2FEK6iALK3bYjYfrDUCoWY0oJoTPKqxEpOnTTTH2DjO%2FbACXxJaIv1p4ZU5zfFL25bIb030Vl3Y6yotbBB51eYrZY2ZoYMmxwnh6yUpnTNhyIwnJS%2BUIAu98XHRvNyJyeDbuwpOYiloYUUAHs2gFld4vPY%2F5JvtL2ALHPEtEc5RlPtds00wnaaxE2i7eFUXUENDEp3Kgd5u07UY2sGf%2FVsntYVZiLDdb3m5deeOwEo2psQSyIWzjgNHFcMOhHEzhyamepfWROZm6W5crJ%2BbZIjiS0VmNv1DliNXFYqn9tU7es5V0J4wwwNX%2BvAY6pgF%2B6FhWpaGIrvmZDqy080hwOcHmbCd5%2FGehhqvXHB9rhM5j9ia3452RD6VCnLs2dLwH2%2B1Hy4nLG5ITlCz9a1XpgqBudzh8UzD83Dal%2Fqd9xS9FcB6Wip2URR4iEBG95cbu2%2FE7XFrvpsWEYRXKYBEhBAks%2F14g%2FrhqPn9bLfHLnXekBgmLo7EiTPn%2FCpW%2FxdvePtwng6YzY72l14T7eMpi%2BTLu6%2BX6&X-Amz-Signature=02c5c2398f39e1c5eab714d05c9232ce38ca997f9c6611c4bba877f9246a0ec9&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUE2HDQN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCM52vzeU9ax2G7m6xv44xtb%2Fi1%2BUj%2FYx4%2BbRzJ7w4jQQIgTUrba13mFEJLz9G%2FpLGUZh2OeBO%2BoHRhFs1QfGgER6YqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOXjRriL%2BOY0QG5BEyrcA4kUtBxskcP8vG%2B8UgpcV2NwsgSD4XDp59nEV3jrDA9bSR4Qohr6%2F9rcl%2BuzV%2BNmPtQjbOPlCHZym6NQUphzvfCklx0rMMzjxquTwf8Zcc4U096jBh56hf933cdeP4xFfE1Ub1gR%2BR%2FZZJW%2BIie4HQ3SQFYquGKuBjLhr6bSNJc4yxbwc08POEf2IiU%2FSLQCR5A0NQ7YN3%2BRIwTj8lPuh94HGF7ht%2B234vU0j%2FkaU78m%2BYquhRR6RZ1R7HBxbJKZx2zbyLR8JxpiCmgW9T3nfuwGb24ZjscF7whnSD1MGVybuCKdeR1US1waiqztEDWWhThRAaBOzaUIyjGxL1bmp3iqiextn6CEqyxUQaT2PRMHTyRA3wgpHFMHJsrpduWYfgqOejxaLD54XkcXLFwomkmrchanEHUEOlBcMp6ZN67A8jB2XnTUAOqCtMr58AfiwCA1EsJqCLk%2BShHMKRkihvFbL1rjDMgFNZU164ih9Kl1%2B1Kfr9fWMMScL%2Btv8DYjrs4zI1Eby4rP3KGhx0pFjRuFb48BVmyqtmg0PdolEUwlYksEaLmqSiRE4PvsFkDrLq%2FqnwWtIXml4zsotxyWhsjOxVnH7gAU9FqpyR4QOWuxnCdRRFmWQb2hLiIcMKGT%2FrwGOqUBm79CNpPUKHmzDBVTqLIxnkN1U0tp6PwkMJLNz4bUmsHI0VjRq%2F%2BnrLw4GxN8iqOOQJ6zuVkE4mkKMUAjhAe1vmWXgNVfPTbkAxgB05%2B6NS5Hc3v0NIr8%2BumgX2R7xQqYPZU9a60kzNfJXpbXLuLESwTJycpRz1XlZ1%2FJbzvMmj7S8ALrvqkan4yETm%2BREVEdnzQC76%2BczX%2B4v66duFqphSHdTdUT&X-Amz-Signature=098813716b3f9256aa69a1893cda1732b1230a3f9a7b377ac2c015f6c6b3fc31&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUE2HDQN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCM52vzeU9ax2G7m6xv44xtb%2Fi1%2BUj%2FYx4%2BbRzJ7w4jQQIgTUrba13mFEJLz9G%2FpLGUZh2OeBO%2BoHRhFs1QfGgER6YqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOXjRriL%2BOY0QG5BEyrcA4kUtBxskcP8vG%2B8UgpcV2NwsgSD4XDp59nEV3jrDA9bSR4Qohr6%2F9rcl%2BuzV%2BNmPtQjbOPlCHZym6NQUphzvfCklx0rMMzjxquTwf8Zcc4U096jBh56hf933cdeP4xFfE1Ub1gR%2BR%2FZZJW%2BIie4HQ3SQFYquGKuBjLhr6bSNJc4yxbwc08POEf2IiU%2FSLQCR5A0NQ7YN3%2BRIwTj8lPuh94HGF7ht%2B234vU0j%2FkaU78m%2BYquhRR6RZ1R7HBxbJKZx2zbyLR8JxpiCmgW9T3nfuwGb24ZjscF7whnSD1MGVybuCKdeR1US1waiqztEDWWhThRAaBOzaUIyjGxL1bmp3iqiextn6CEqyxUQaT2PRMHTyRA3wgpHFMHJsrpduWYfgqOejxaLD54XkcXLFwomkmrchanEHUEOlBcMp6ZN67A8jB2XnTUAOqCtMr58AfiwCA1EsJqCLk%2BShHMKRkihvFbL1rjDMgFNZU164ih9Kl1%2B1Kfr9fWMMScL%2Btv8DYjrs4zI1Eby4rP3KGhx0pFjRuFb48BVmyqtmg0PdolEUwlYksEaLmqSiRE4PvsFkDrLq%2FqnwWtIXml4zsotxyWhsjOxVnH7gAU9FqpyR4QOWuxnCdRRFmWQb2hLiIcMKGT%2FrwGOqUBm79CNpPUKHmzDBVTqLIxnkN1U0tp6PwkMJLNz4bUmsHI0VjRq%2F%2BnrLw4GxN8iqOOQJ6zuVkE4mkKMUAjhAe1vmWXgNVfPTbkAxgB05%2B6NS5Hc3v0NIr8%2BumgX2R7xQqYPZU9a60kzNfJXpbXLuLESwTJycpRz1XlZ1%2FJbzvMmj7S8ALrvqkan4yETm%2BREVEdnzQC76%2BczX%2B4v66duFqphSHdTdUT&X-Amz-Signature=eb920feef151849847da67e64ff1d643b93c1f7b674f4b77721cb0f468f4fe6d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJKP5QT4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkrBZmkgHQTVTSltf%2BeJbXrOiJB3vL7OrMRj5wtOiZ7AiBC5ib1%2BgZ1UUDJu5ezCewGcwzguGEG68Huv8tX1aWZeCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2dL8Cnrw5RFvnFdyKtwDf2KGeymr%2FiFAO5DAS71VS9Sa8%2Fmar26mresgEYKGg7f1zLEbxNabKLlnSlK4YaTYAJOLsCz22f2Hm3b9MsWDnCN9JqJOx4otqD57wGa1TBfN%2BaxZA29C6nKkx7vz0aDEM0ougLwXO1wQRI7RF5IS9JXectMu8yLT9O8KRtF1GAdE3qw2Dg%2BEgIekqohIZAApc45Uk841%2BiRlHAfdyjGjcU1u7Eprbve5uoefxbzt5YlOwADhe1Jw8aN%2FiCj6klgylwtPIv48llABLu6Gpkxvz6Oie%2FEMIt0nEae%2BEKXm6oxWhlVVGIU3ChdSmA%2BuVTiSXCZaF29gP%2FEK6iALK3bYjYfrDUCoWY0oJoTPKqxEpOnTTTH2DjO%2FbACXxJaIv1p4ZU5zfFL25bIb030Vl3Y6yotbBB51eYrZY2ZoYMmxwnh6yUpnTNhyIwnJS%2BUIAu98XHRvNyJyeDbuwpOYiloYUUAHs2gFld4vPY%2F5JvtL2ALHPEtEc5RlPtds00wnaaxE2i7eFUXUENDEp3Kgd5u07UY2sGf%2FVsntYVZiLDdb3m5deeOwEo2psQSyIWzjgNHFcMOhHEzhyamepfWROZm6W5crJ%2BbZIjiS0VmNv1DliNXFYqn9tU7es5V0J4wwwNX%2BvAY6pgF%2B6FhWpaGIrvmZDqy080hwOcHmbCd5%2FGehhqvXHB9rhM5j9ia3452RD6VCnLs2dLwH2%2B1Hy4nLG5ITlCz9a1XpgqBudzh8UzD83Dal%2Fqd9xS9FcB6Wip2URR4iEBG95cbu2%2FE7XFrvpsWEYRXKYBEhBAks%2F14g%2FrhqPn9bLfHLnXekBgmLo7EiTPn%2FCpW%2FxdvePtwng6YzY72l14T7eMpi%2BTLu6%2BX6&X-Amz-Signature=4d5ccf318917c846180e9c8ff45bda4c71ad4f9040f4d216bf9f3cb457c32aa2&X-Amz-SignedHeaders=host&x-id=GetObject)
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