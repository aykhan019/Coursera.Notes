

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF67VJ5I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJFMEMCIGtgKCuPH5PXz6bxiIvT8OYV52qn9fNm6RXSagfoBEVNAh8iYfiI6TubvdzDQ7%2FVVXZmE%2FqL1FzaBQYyzoz3Ch2jKv8DCGkQABoMNjM3NDIzMTgzODA1Igx4QHZ7Y7zEtrqXivkq3AO2TORptG61zud24NK6cSfey2i4Ont228VBzqCsngz23zRTLQHPtQ26moRGk4X4eEJyenI%2F%2BbpDN7EVzt06PMRnr9ag1H%2FYsp2t0%2BjKUbGQna6shoOO%2FHPyd5jhA1HPoCs9qvJLjhLI4GtEUfAKefYBkv8s9KmE9vhSFgPur7TcnhTkjEymCR9hgbIQvhevMbV3VpVgx9Nac5S%2BMUBQ4m7j1fZxFY66ALvdhya7Y3nGaze7nQTZMnUL%2Fv%2BiHrTP0pY277ivsriHlDlN%2F5Ur3fy1PQ48EmHC3dpbM4P7w%2B2JOIGuLSw7uI1liixP9w7STyoJH9If54gQBZWJ6NUOAatkf1pSkBXtfonZhTvzkvYZtOAuVs%2FQi82DBGhQS5IR0K4aNPdtaY8vhY%2BufBpXubRyjQq%2BlGCRz8TfBGKHw2R%2FWtZQLQrD%2B6PyA2YRGMTPUbhemWtbP%2B4Jeyv0AtaX0aJCBLcIArM%2Ffk2KlKp4IbxlVrBl8IMY19VLzhpNx81FgyDWARRU6CyONKHrf87gDuwoU0L6Y%2Flui1m5AihT2SGvfp3MMMX9X%2BYG2j9NqfoOH5TX0BuaCO1kLTlclIH2TPD%2BEQl7wQcdsnQmbcwBA9TNvfg%2BHmOdHVzYsyooETD7mZW9BjqnAY%2FBBUUChppBhJCFmR6RmuxI6CEjfzakZ3kPKPMYTyHzNAOTM9iCwphTRSo00efh7mgDwm3IQH1GzIuMikIYhUswWMBgzufd2qNx6InP%2BbECiB%2F7%2BoEC5vWXoplw6NKXLL0lJ2GBowI4UZOKUImxchTlPwiS0Ctm%2FxsrIJAjrGiTUkL%2BLANJ1Hn1WdSgX%2Fow8NCBIDZWV%2BkQZIHRGeNGw5GgmyGVUV58&X-Amz-Signature=f345ce5145b03656ffa4d626a13d757d5dd534d41e7a33edafc9a4506c3d6228&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF67VJ5I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJFMEMCIGtgKCuPH5PXz6bxiIvT8OYV52qn9fNm6RXSagfoBEVNAh8iYfiI6TubvdzDQ7%2FVVXZmE%2FqL1FzaBQYyzoz3Ch2jKv8DCGkQABoMNjM3NDIzMTgzODA1Igx4QHZ7Y7zEtrqXivkq3AO2TORptG61zud24NK6cSfey2i4Ont228VBzqCsngz23zRTLQHPtQ26moRGk4X4eEJyenI%2F%2BbpDN7EVzt06PMRnr9ag1H%2FYsp2t0%2BjKUbGQna6shoOO%2FHPyd5jhA1HPoCs9qvJLjhLI4GtEUfAKefYBkv8s9KmE9vhSFgPur7TcnhTkjEymCR9hgbIQvhevMbV3VpVgx9Nac5S%2BMUBQ4m7j1fZxFY66ALvdhya7Y3nGaze7nQTZMnUL%2Fv%2BiHrTP0pY277ivsriHlDlN%2F5Ur3fy1PQ48EmHC3dpbM4P7w%2B2JOIGuLSw7uI1liixP9w7STyoJH9If54gQBZWJ6NUOAatkf1pSkBXtfonZhTvzkvYZtOAuVs%2FQi82DBGhQS5IR0K4aNPdtaY8vhY%2BufBpXubRyjQq%2BlGCRz8TfBGKHw2R%2FWtZQLQrD%2B6PyA2YRGMTPUbhemWtbP%2B4Jeyv0AtaX0aJCBLcIArM%2Ffk2KlKp4IbxlVrBl8IMY19VLzhpNx81FgyDWARRU6CyONKHrf87gDuwoU0L6Y%2Flui1m5AihT2SGvfp3MMMX9X%2BYG2j9NqfoOH5TX0BuaCO1kLTlclIH2TPD%2BEQl7wQcdsnQmbcwBA9TNvfg%2BHmOdHVzYsyooETD7mZW9BjqnAY%2FBBUUChppBhJCFmR6RmuxI6CEjfzakZ3kPKPMYTyHzNAOTM9iCwphTRSo00efh7mgDwm3IQH1GzIuMikIYhUswWMBgzufd2qNx6InP%2BbECiB%2F7%2BoEC5vWXoplw6NKXLL0lJ2GBowI4UZOKUImxchTlPwiS0Ctm%2FxsrIJAjrGiTUkL%2BLANJ1Hn1WdSgX%2Fow8NCBIDZWV%2BkQZIHRGeNGw5GgmyGVUV58&X-Amz-Signature=b0c2402786154e7dc079010af281847bae0300f3ae5a192150b181814820c615&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF67VJ5I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJFMEMCIGtgKCuPH5PXz6bxiIvT8OYV52qn9fNm6RXSagfoBEVNAh8iYfiI6TubvdzDQ7%2FVVXZmE%2FqL1FzaBQYyzoz3Ch2jKv8DCGkQABoMNjM3NDIzMTgzODA1Igx4QHZ7Y7zEtrqXivkq3AO2TORptG61zud24NK6cSfey2i4Ont228VBzqCsngz23zRTLQHPtQ26moRGk4X4eEJyenI%2F%2BbpDN7EVzt06PMRnr9ag1H%2FYsp2t0%2BjKUbGQna6shoOO%2FHPyd5jhA1HPoCs9qvJLjhLI4GtEUfAKefYBkv8s9KmE9vhSFgPur7TcnhTkjEymCR9hgbIQvhevMbV3VpVgx9Nac5S%2BMUBQ4m7j1fZxFY66ALvdhya7Y3nGaze7nQTZMnUL%2Fv%2BiHrTP0pY277ivsriHlDlN%2F5Ur3fy1PQ48EmHC3dpbM4P7w%2B2JOIGuLSw7uI1liixP9w7STyoJH9If54gQBZWJ6NUOAatkf1pSkBXtfonZhTvzkvYZtOAuVs%2FQi82DBGhQS5IR0K4aNPdtaY8vhY%2BufBpXubRyjQq%2BlGCRz8TfBGKHw2R%2FWtZQLQrD%2B6PyA2YRGMTPUbhemWtbP%2B4Jeyv0AtaX0aJCBLcIArM%2Ffk2KlKp4IbxlVrBl8IMY19VLzhpNx81FgyDWARRU6CyONKHrf87gDuwoU0L6Y%2Flui1m5AihT2SGvfp3MMMX9X%2BYG2j9NqfoOH5TX0BuaCO1kLTlclIH2TPD%2BEQl7wQcdsnQmbcwBA9TNvfg%2BHmOdHVzYsyooETD7mZW9BjqnAY%2FBBUUChppBhJCFmR6RmuxI6CEjfzakZ3kPKPMYTyHzNAOTM9iCwphTRSo00efh7mgDwm3IQH1GzIuMikIYhUswWMBgzufd2qNx6InP%2BbECiB%2F7%2BoEC5vWXoplw6NKXLL0lJ2GBowI4UZOKUImxchTlPwiS0Ctm%2FxsrIJAjrGiTUkL%2BLANJ1Hn1WdSgX%2Fow8NCBIDZWV%2BkQZIHRGeNGw5GgmyGVUV58&X-Amz-Signature=9683eb1442a617c855b25c47b0641627953e5e8ca3e98fd5f8145a50a6033a29&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUQ2MHSB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIEV%2BCazFuzu2CMeXNn6SPV9v0e40vMqudzPFOYE1rtCMAiAZzwxgJ6Cp%2Bmddz6dwatTTsgVZHURjAAm%2BQw%2BopJLd9Cr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIM%2Bf9%2BYWuSw64dUGALKtwD86XVwS8pUE4n%2FKyrDS5%2BGXHfn44AUGfY7sWqMVAV66lUOaL6fpy5UlOpxoi%2BAKeI9YTUP65L5VWx23uFqNHEAng9%2F4NbZJQk9dNqDzR7wO6npkvl8W0%2FZd4%2BLIGI8qochgBAnLpwJbOrBDbtjJe927W%2Bo%2F8TDpZDee3Wy%2B5%2BrOyM%2FBSbHZSxljHY4IdXKW3Sdi4dJ4baQ4Y5MxrZ%2BqANubPgs1KVthQhc60Vsytz4o9Yw%2BGse4COhFLhwPaHo31H75jW5iLVJgzAn43is43i%2F%2FRIll6bpNmzWR2QzhmovxrtoTYjalxMoGkch3BG5fF4hxbsEO3vCOy7G811EwrYS4HUgZMh6V4Wk6hB1rzE5G3wKfK4Cs4sC25S1baL1K6W9DryyXsfDkCgPme2WWtik2yWtw%2F3noI8cAgAVHBX8THk2ggA%2BBFhSoMZzT%2BIUaPOwoIXWYqCkKGJL38aQY%2BlS1qMeIM%2F5PEIJYX7nkMnrOPc7NHcyAmwKHlmtSGhKS3FJNQ%2B24zRurgSoJgA7F0ISUMPROGfETHV%2BPqGhcxMByxDIMeIfmaRqODpLLpWgQkVmgSvjAQRVZJMveFc44Ub4VaM6yoOoi6vzBVF5EdqFHRC7dALojNlzCLj7HEw5JmVvQY6pgE05e60VUq8Qi2sXJi55UTNtEOjcKVpd2CIYel5kLk0kfwbG1RhT9pMmyitzhTpi2LYmHynrP%2FTP2TkvpExx%2Fdk78gl5DwMZmmau7SRlsr%2BUdoUBI57Ln5cB7NDf6IacrPFeTBs4XygtBSRj293QatmN0X5n4F8AAqxOYbej4NHMeVRVl4%2Bhoc0k4MtErdFT7w1qLv0MSp%2FDcBcXQ9RAUpKpMSnLxwp&X-Amz-Signature=9a5df668f279e9169da4f7925366522f63cdc833745e32f7fb93cd769bc4a463&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUQ2MHSB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIEV%2BCazFuzu2CMeXNn6SPV9v0e40vMqudzPFOYE1rtCMAiAZzwxgJ6Cp%2Bmddz6dwatTTsgVZHURjAAm%2BQw%2BopJLd9Cr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIM%2Bf9%2BYWuSw64dUGALKtwD86XVwS8pUE4n%2FKyrDS5%2BGXHfn44AUGfY7sWqMVAV66lUOaL6fpy5UlOpxoi%2BAKeI9YTUP65L5VWx23uFqNHEAng9%2F4NbZJQk9dNqDzR7wO6npkvl8W0%2FZd4%2BLIGI8qochgBAnLpwJbOrBDbtjJe927W%2Bo%2F8TDpZDee3Wy%2B5%2BrOyM%2FBSbHZSxljHY4IdXKW3Sdi4dJ4baQ4Y5MxrZ%2BqANubPgs1KVthQhc60Vsytz4o9Yw%2BGse4COhFLhwPaHo31H75jW5iLVJgzAn43is43i%2F%2FRIll6bpNmzWR2QzhmovxrtoTYjalxMoGkch3BG5fF4hxbsEO3vCOy7G811EwrYS4HUgZMh6V4Wk6hB1rzE5G3wKfK4Cs4sC25S1baL1K6W9DryyXsfDkCgPme2WWtik2yWtw%2F3noI8cAgAVHBX8THk2ggA%2BBFhSoMZzT%2BIUaPOwoIXWYqCkKGJL38aQY%2BlS1qMeIM%2F5PEIJYX7nkMnrOPc7NHcyAmwKHlmtSGhKS3FJNQ%2B24zRurgSoJgA7F0ISUMPROGfETHV%2BPqGhcxMByxDIMeIfmaRqODpLLpWgQkVmgSvjAQRVZJMveFc44Ub4VaM6yoOoi6vzBVF5EdqFHRC7dALojNlzCLj7HEw5JmVvQY6pgE05e60VUq8Qi2sXJi55UTNtEOjcKVpd2CIYel5kLk0kfwbG1RhT9pMmyitzhTpi2LYmHynrP%2FTP2TkvpExx%2Fdk78gl5DwMZmmau7SRlsr%2BUdoUBI57Ln5cB7NDf6IacrPFeTBs4XygtBSRj293QatmN0X5n4F8AAqxOYbej4NHMeVRVl4%2Bhoc0k4MtErdFT7w1qLv0MSp%2FDcBcXQ9RAUpKpMSnLxwp&X-Amz-Signature=114b3205d8b97d2803b77e47d8b868c4de8babbc70b2efdefd69961cc73603b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF67VJ5I%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJFMEMCIGtgKCuPH5PXz6bxiIvT8OYV52qn9fNm6RXSagfoBEVNAh8iYfiI6TubvdzDQ7%2FVVXZmE%2FqL1FzaBQYyzoz3Ch2jKv8DCGkQABoMNjM3NDIzMTgzODA1Igx4QHZ7Y7zEtrqXivkq3AO2TORptG61zud24NK6cSfey2i4Ont228VBzqCsngz23zRTLQHPtQ26moRGk4X4eEJyenI%2F%2BbpDN7EVzt06PMRnr9ag1H%2FYsp2t0%2BjKUbGQna6shoOO%2FHPyd5jhA1HPoCs9qvJLjhLI4GtEUfAKefYBkv8s9KmE9vhSFgPur7TcnhTkjEymCR9hgbIQvhevMbV3VpVgx9Nac5S%2BMUBQ4m7j1fZxFY66ALvdhya7Y3nGaze7nQTZMnUL%2Fv%2BiHrTP0pY277ivsriHlDlN%2F5Ur3fy1PQ48EmHC3dpbM4P7w%2B2JOIGuLSw7uI1liixP9w7STyoJH9If54gQBZWJ6NUOAatkf1pSkBXtfonZhTvzkvYZtOAuVs%2FQi82DBGhQS5IR0K4aNPdtaY8vhY%2BufBpXubRyjQq%2BlGCRz8TfBGKHw2R%2FWtZQLQrD%2B6PyA2YRGMTPUbhemWtbP%2B4Jeyv0AtaX0aJCBLcIArM%2Ffk2KlKp4IbxlVrBl8IMY19VLzhpNx81FgyDWARRU6CyONKHrf87gDuwoU0L6Y%2Flui1m5AihT2SGvfp3MMMX9X%2BYG2j9NqfoOH5TX0BuaCO1kLTlclIH2TPD%2BEQl7wQcdsnQmbcwBA9TNvfg%2BHmOdHVzYsyooETD7mZW9BjqnAY%2FBBUUChppBhJCFmR6RmuxI6CEjfzakZ3kPKPMYTyHzNAOTM9iCwphTRSo00efh7mgDwm3IQH1GzIuMikIYhUswWMBgzufd2qNx6InP%2BbECiB%2F7%2BoEC5vWXoplw6NKXLL0lJ2GBowI4UZOKUImxchTlPwiS0Ctm%2FxsrIJAjrGiTUkL%2BLANJ1Hn1WdSgX%2Fow8NCBIDZWV%2BkQZIHRGeNGw5GgmyGVUV58&X-Amz-Signature=cb1a4975da5bd10fcb83e0004a4c1965a2bfd273a19a705bca321ab067a8dc60&X-Amz-SignedHeaders=host&x-id=GetObject)
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