

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T53BIYI2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFSuq16lDnamo9oN4s1ZDdwQb%2BL0xw63wkJF3X6Xl8FqAiEA3vLK2sw9GJEhBFasFEDPVMR8tGK8hR8pdzLBMvOAaz8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJjXs%2Flw%2FgO%2FEmfS%2FCrcA7GHrA5XttnX20Curr3q5vNXAve3lbbKV5Tv7pyqqaBqRvmQAT%2FWruiud5mF77iA9u3HcFSJ51eEuIKN%2FvikaCobGRNveAkaCsQ5nC4GzQ1F%2BFya%2BAPHsLmBNegsACCqzeG3DDK4YcggYcWy1j%2FxFu6XU1n4HNei8AxyEMtCxO96sG9wVhT1tiGXSJqDgoC%2B7O2qk50dGRKnxzQTHREFVRKYsUhQxksEA%2FY4IY30aHXkthnl9IEchz4SnKNUxnw6popyUxOnGQVGDPmWclPoeXxf7hCpUPz%2B7wNppZWHm3uFmf0oeWgsDso8F9fGgAYJAmHLByrifVHO3yhEZZWEfZw8uDG%2FIxZeEev7laLFo6TBDtxyUA6M8qai0RfxByLgKeaTlRbWIV8gqwDm4qmJae6WpzuzAlQjUSUw8Hwpk3TxDXzTXvYXJWxBiMfYMhGoUgkSajsjAy5ZWq9ZOCUSNksyZdUHeloa1FRgcdvsQjZiucGWfKGaIc%2BXUMeuF43C3pQjQDlZeefYytohFdcY2q2tJDNxI5XJ4hX0kwAFqKGaW84CjVuhUa2QWlN%2F12GkLnZ7FI44kBQ8eH5256r8%2F22lFHY4JHHEWTfcN4pNsqPKEka37Ctmm8He7YlpMMPl%2F7wGOqUBR6ixHsLp5Ky9oY65%2FiZhlOpV6AMULmTz%2Bu1EVAEP8XCRUWfRhqoB1%2FX5imZdImqy2ZZU1osUI03D3vDBriTwZu%2B1OkGWxInPfTurGfNh0fRQEUvs2Y5Zp1Sez%2BXDNFn3aRujuZisGzUp5ttVo6t2UvSRqY88bfDILNfY9uOBzJpr3MmwqLTd2K2i8OggnfBPoW2iP3xFkAvcSOc9VemBElhYucgj&X-Amz-Signature=9502a3feb4adb25300e650c16765172b03e68dac9879e0a959e3af3c8fe45da8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T53BIYI2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFSuq16lDnamo9oN4s1ZDdwQb%2BL0xw63wkJF3X6Xl8FqAiEA3vLK2sw9GJEhBFasFEDPVMR8tGK8hR8pdzLBMvOAaz8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJjXs%2Flw%2FgO%2FEmfS%2FCrcA7GHrA5XttnX20Curr3q5vNXAve3lbbKV5Tv7pyqqaBqRvmQAT%2FWruiud5mF77iA9u3HcFSJ51eEuIKN%2FvikaCobGRNveAkaCsQ5nC4GzQ1F%2BFya%2BAPHsLmBNegsACCqzeG3DDK4YcggYcWy1j%2FxFu6XU1n4HNei8AxyEMtCxO96sG9wVhT1tiGXSJqDgoC%2B7O2qk50dGRKnxzQTHREFVRKYsUhQxksEA%2FY4IY30aHXkthnl9IEchz4SnKNUxnw6popyUxOnGQVGDPmWclPoeXxf7hCpUPz%2B7wNppZWHm3uFmf0oeWgsDso8F9fGgAYJAmHLByrifVHO3yhEZZWEfZw8uDG%2FIxZeEev7laLFo6TBDtxyUA6M8qai0RfxByLgKeaTlRbWIV8gqwDm4qmJae6WpzuzAlQjUSUw8Hwpk3TxDXzTXvYXJWxBiMfYMhGoUgkSajsjAy5ZWq9ZOCUSNksyZdUHeloa1FRgcdvsQjZiucGWfKGaIc%2BXUMeuF43C3pQjQDlZeefYytohFdcY2q2tJDNxI5XJ4hX0kwAFqKGaW84CjVuhUa2QWlN%2F12GkLnZ7FI44kBQ8eH5256r8%2F22lFHY4JHHEWTfcN4pNsqPKEka37Ctmm8He7YlpMMPl%2F7wGOqUBR6ixHsLp5Ky9oY65%2FiZhlOpV6AMULmTz%2Bu1EVAEP8XCRUWfRhqoB1%2FX5imZdImqy2ZZU1osUI03D3vDBriTwZu%2B1OkGWxInPfTurGfNh0fRQEUvs2Y5Zp1Sez%2BXDNFn3aRujuZisGzUp5ttVo6t2UvSRqY88bfDILNfY9uOBzJpr3MmwqLTd2K2i8OggnfBPoW2iP3xFkAvcSOc9VemBElhYucgj&X-Amz-Signature=c9a9fe147d1cafe88226b166e72681f5cef7d19e906891121d414b0920a51d1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T53BIYI2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFSuq16lDnamo9oN4s1ZDdwQb%2BL0xw63wkJF3X6Xl8FqAiEA3vLK2sw9GJEhBFasFEDPVMR8tGK8hR8pdzLBMvOAaz8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJjXs%2Flw%2FgO%2FEmfS%2FCrcA7GHrA5XttnX20Curr3q5vNXAve3lbbKV5Tv7pyqqaBqRvmQAT%2FWruiud5mF77iA9u3HcFSJ51eEuIKN%2FvikaCobGRNveAkaCsQ5nC4GzQ1F%2BFya%2BAPHsLmBNegsACCqzeG3DDK4YcggYcWy1j%2FxFu6XU1n4HNei8AxyEMtCxO96sG9wVhT1tiGXSJqDgoC%2B7O2qk50dGRKnxzQTHREFVRKYsUhQxksEA%2FY4IY30aHXkthnl9IEchz4SnKNUxnw6popyUxOnGQVGDPmWclPoeXxf7hCpUPz%2B7wNppZWHm3uFmf0oeWgsDso8F9fGgAYJAmHLByrifVHO3yhEZZWEfZw8uDG%2FIxZeEev7laLFo6TBDtxyUA6M8qai0RfxByLgKeaTlRbWIV8gqwDm4qmJae6WpzuzAlQjUSUw8Hwpk3TxDXzTXvYXJWxBiMfYMhGoUgkSajsjAy5ZWq9ZOCUSNksyZdUHeloa1FRgcdvsQjZiucGWfKGaIc%2BXUMeuF43C3pQjQDlZeefYytohFdcY2q2tJDNxI5XJ4hX0kwAFqKGaW84CjVuhUa2QWlN%2F12GkLnZ7FI44kBQ8eH5256r8%2F22lFHY4JHHEWTfcN4pNsqPKEka37Ctmm8He7YlpMMPl%2F7wGOqUBR6ixHsLp5Ky9oY65%2FiZhlOpV6AMULmTz%2Bu1EVAEP8XCRUWfRhqoB1%2FX5imZdImqy2ZZU1osUI03D3vDBriTwZu%2B1OkGWxInPfTurGfNh0fRQEUvs2Y5Zp1Sez%2BXDNFn3aRujuZisGzUp5ttVo6t2UvSRqY88bfDILNfY9uOBzJpr3MmwqLTd2K2i8OggnfBPoW2iP3xFkAvcSOc9VemBElhYucgj&X-Amz-Signature=1f62b749b8fe2ff744f92f1ffa94485e62221ce1ece54b41de311b70cd8a7f28&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBQJRAWD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJHl%2BKi44U5IA1MMWZCceuMeuoP2lIJPVT%2FzJ%2FKavX9gIgb0bu%2FZH%2BNhnwfBa8BrL08GgIwx%2Fyn5pTaTz9aGcXE6UqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSt%2FLGY5kTVcqb97ircAwVKuhsZvlAiMNvJHMmBhNUrTxEbQ6ajErwwarp1hPOLvWxd8JTwoPg%2BeWlNfuDw6DqxXPA7fVlZi5mDSgcsT1X0yFWGj1AvGaV6NX7Z9h51aMnBgcxlC9LvAXsFKx5Ls6iTpLspYdRo9MeYc5nLIdpPk5f4wNKSqwgnGknuKqjIGAvh2YpqjTNFDbPOD2RcGGETvs%2BrYsQpOinQhKSof%2BKg2wyWhIDv2TwMZtEtO81C1OjxVFt6N2WqEdmfwX4U7hgQ7CCdSniUN7JdXYqbYfiz4e9p%2FxpCZNYAMkTxFspiIqgrJcFBZTPAvbh3lmbG2T%2Fz43aV7nE5FElEgkKnDRmOd7uRhWJqxXcMBMGLAQfFMbFm2na1%2FYc0LjeAO1EUHER7LI50VSUZVkZhV5ADQVwUlgnsq6Sbaa1fNz%2BffO6KNLmdgBIZNmGegD2%2F271CxqZQIPD0cbgUGaZn44FUleSxLPomAF1DvZb6MraNeUtz5d9FYzpj8UnHEIM3ZmPJuvM%2BZAYTJcmli4SLLaCo%2BOinrPP%2FRGqzYPHB1DG7AOVOe9n9uSFu0IpsNG%2BNnuvHiaaM6MbTgY5CHXkBrloigxvzfcoelczuktuaWgaR2vU%2B0mVkz%2F45oRePp8GJMKTk%2F7wGOqUBmG0XXnmUAGkj0wG9DQfDVdQ9qk946ZREQcTU8GMFYngyAHd%2BXztL954ouWe62NoV0PqtqYRoA0snOXx%2FEgp%2BVK%2BWgfov86hFw4dSh2KUKFWPQ4yLcRzH3ryUNiWhgVdWZ6y6Hs4k8hqF2wvnytud6x1vWb24aKMYRukR9cLlmCeQ6YIsSLU1uMGtAVkDKLRvlhMZqeIRM9c3GOgouF3x9tTHylsM&X-Amz-Signature=091da68f6bb789dca375de423d4e07da382cc221411e36446792083d55057041&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBQJRAWD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJHl%2BKi44U5IA1MMWZCceuMeuoP2lIJPVT%2FzJ%2FKavX9gIgb0bu%2FZH%2BNhnwfBa8BrL08GgIwx%2Fyn5pTaTz9aGcXE6UqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBSt%2FLGY5kTVcqb97ircAwVKuhsZvlAiMNvJHMmBhNUrTxEbQ6ajErwwarp1hPOLvWxd8JTwoPg%2BeWlNfuDw6DqxXPA7fVlZi5mDSgcsT1X0yFWGj1AvGaV6NX7Z9h51aMnBgcxlC9LvAXsFKx5Ls6iTpLspYdRo9MeYc5nLIdpPk5f4wNKSqwgnGknuKqjIGAvh2YpqjTNFDbPOD2RcGGETvs%2BrYsQpOinQhKSof%2BKg2wyWhIDv2TwMZtEtO81C1OjxVFt6N2WqEdmfwX4U7hgQ7CCdSniUN7JdXYqbYfiz4e9p%2FxpCZNYAMkTxFspiIqgrJcFBZTPAvbh3lmbG2T%2Fz43aV7nE5FElEgkKnDRmOd7uRhWJqxXcMBMGLAQfFMbFm2na1%2FYc0LjeAO1EUHER7LI50VSUZVkZhV5ADQVwUlgnsq6Sbaa1fNz%2BffO6KNLmdgBIZNmGegD2%2F271CxqZQIPD0cbgUGaZn44FUleSxLPomAF1DvZb6MraNeUtz5d9FYzpj8UnHEIM3ZmPJuvM%2BZAYTJcmli4SLLaCo%2BOinrPP%2FRGqzYPHB1DG7AOVOe9n9uSFu0IpsNG%2BNnuvHiaaM6MbTgY5CHXkBrloigxvzfcoelczuktuaWgaR2vU%2B0mVkz%2F45oRePp8GJMKTk%2F7wGOqUBmG0XXnmUAGkj0wG9DQfDVdQ9qk946ZREQcTU8GMFYngyAHd%2BXztL954ouWe62NoV0PqtqYRoA0snOXx%2FEgp%2BVK%2BWgfov86hFw4dSh2KUKFWPQ4yLcRzH3ryUNiWhgVdWZ6y6Hs4k8hqF2wvnytud6x1vWb24aKMYRukR9cLlmCeQ6YIsSLU1uMGtAVkDKLRvlhMZqeIRM9c3GOgouF3x9tTHylsM&X-Amz-Signature=70a5947e3d5b35ed99fc38d6b296b741c45a2c260c9688ebcb95705d46834dd9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T53BIYI2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFSuq16lDnamo9oN4s1ZDdwQb%2BL0xw63wkJF3X6Xl8FqAiEA3vLK2sw9GJEhBFasFEDPVMR8tGK8hR8pdzLBMvOAaz8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJjXs%2Flw%2FgO%2FEmfS%2FCrcA7GHrA5XttnX20Curr3q5vNXAve3lbbKV5Tv7pyqqaBqRvmQAT%2FWruiud5mF77iA9u3HcFSJ51eEuIKN%2FvikaCobGRNveAkaCsQ5nC4GzQ1F%2BFya%2BAPHsLmBNegsACCqzeG3DDK4YcggYcWy1j%2FxFu6XU1n4HNei8AxyEMtCxO96sG9wVhT1tiGXSJqDgoC%2B7O2qk50dGRKnxzQTHREFVRKYsUhQxksEA%2FY4IY30aHXkthnl9IEchz4SnKNUxnw6popyUxOnGQVGDPmWclPoeXxf7hCpUPz%2B7wNppZWHm3uFmf0oeWgsDso8F9fGgAYJAmHLByrifVHO3yhEZZWEfZw8uDG%2FIxZeEev7laLFo6TBDtxyUA6M8qai0RfxByLgKeaTlRbWIV8gqwDm4qmJae6WpzuzAlQjUSUw8Hwpk3TxDXzTXvYXJWxBiMfYMhGoUgkSajsjAy5ZWq9ZOCUSNksyZdUHeloa1FRgcdvsQjZiucGWfKGaIc%2BXUMeuF43C3pQjQDlZeefYytohFdcY2q2tJDNxI5XJ4hX0kwAFqKGaW84CjVuhUa2QWlN%2F12GkLnZ7FI44kBQ8eH5256r8%2F22lFHY4JHHEWTfcN4pNsqPKEka37Ctmm8He7YlpMMPl%2F7wGOqUBR6ixHsLp5Ky9oY65%2FiZhlOpV6AMULmTz%2Bu1EVAEP8XCRUWfRhqoB1%2FX5imZdImqy2ZZU1osUI03D3vDBriTwZu%2B1OkGWxInPfTurGfNh0fRQEUvs2Y5Zp1Sez%2BXDNFn3aRujuZisGzUp5ttVo6t2UvSRqY88bfDILNfY9uOBzJpr3MmwqLTd2K2i8OggnfBPoW2iP3xFkAvcSOc9VemBElhYucgj&X-Amz-Signature=263181baf3ac0ac996ca7870df6220119dc6b24e389a691cc0ed37528473d137&X-Amz-SignedHeaders=host&x-id=GetObject)
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