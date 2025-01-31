

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BXVQSWK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA4LKlla%2FeZtToG6wOm5IBhRoJd7nCy0uZIP8ZjZIQrGAiBKJv%2B7MFWc5yYsQzZb00klo7%2B2ulxa4YL4f6cDRDuyuiqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMABA9KHdj1qCRO4hPKtwDVUNUTP1EbFxYxsnntKLpZYAXYzEwEv3Dqfozq1Tz3MI308lUXymhrit7iYQI%2Fry0vilcXdSxyKLXORXOr3JWPqxPQd3sesdTw9HCU13EYkS8MyD%2BvrSuxm7J1hJ6yo6qP2ascMzASpdXFqHV7e6mPfYepGZVNfSw%2BH5RLqRUn1Tj2R9weD%2FA3gSL4%2FCp3SZ9EJonrb1Sd0WGpVlyiByhETqPY9yeQq1giXGhEO7HcaDQSPoKKETdNqdikf0mrLjRRd4jYFJUyaGIdSJltopaLvxdTJY9X68vSu%2FcNUiHkHLUrB3ymHejTy2fKYwsQO0FSdMz83bMiQSXOIpMhYmT5%2BHtOlloq8nfC5ARRwnjhdRKgzm%2Fbty%2BhQK5wo6xTPTwTQTEo4UDFDx4A9cc4DWATU5vG4BdspUWPBVzM1NSn8v7YDteFQWSZxSs%2F1wCBDooTUFcdHy0j9ZAquyscsWo%2F6B6%2B%2B7e8JturN%2Bb2kxKJ7FhIBBfC%2BLOxBO%2BcCLgx7o%2Fu12R9X84YxP6jdxmkWUfgUgCLeWVQWMlzcefwtMBwjoiJA%2FUATLhNKudMyGoKMLpkMvk%2B9tUNH79pdIr5DVJFS5T4DUcVe7nc4N%2FmeKlyDfNxA5lCuv9XmImg7kw8rTwvAY6pgEZtvmd9IdGR5xtwHiUdSET3QFrnc2hop3KER%2BEdxFxa8WG4JbitqWJ%2Bi0l%2FFsjERo%2B030AavgJ2wno1%2FFkdMjrhbdF3ZRmvObb4Fw98pN5b28%2FCw2%2BpDkNBhhDJih%2BuG0H1RI%2FO%2FU%2BvvGqxbXuBp1%2BrTKzjIeimNtU%2B%2BxKkfEZI8aJauN2CSADV1Q18IPOefQ6vbaVN4zpRGCHd3WQ03Y2mGk%2FdPx9&X-Amz-Signature=973171b22557d8dfced73ee4abca3372d8798c4154db3934612ef2215ebec22f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BXVQSWK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA4LKlla%2FeZtToG6wOm5IBhRoJd7nCy0uZIP8ZjZIQrGAiBKJv%2B7MFWc5yYsQzZb00klo7%2B2ulxa4YL4f6cDRDuyuiqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMABA9KHdj1qCRO4hPKtwDVUNUTP1EbFxYxsnntKLpZYAXYzEwEv3Dqfozq1Tz3MI308lUXymhrit7iYQI%2Fry0vilcXdSxyKLXORXOr3JWPqxPQd3sesdTw9HCU13EYkS8MyD%2BvrSuxm7J1hJ6yo6qP2ascMzASpdXFqHV7e6mPfYepGZVNfSw%2BH5RLqRUn1Tj2R9weD%2FA3gSL4%2FCp3SZ9EJonrb1Sd0WGpVlyiByhETqPY9yeQq1giXGhEO7HcaDQSPoKKETdNqdikf0mrLjRRd4jYFJUyaGIdSJltopaLvxdTJY9X68vSu%2FcNUiHkHLUrB3ymHejTy2fKYwsQO0FSdMz83bMiQSXOIpMhYmT5%2BHtOlloq8nfC5ARRwnjhdRKgzm%2Fbty%2BhQK5wo6xTPTwTQTEo4UDFDx4A9cc4DWATU5vG4BdspUWPBVzM1NSn8v7YDteFQWSZxSs%2F1wCBDooTUFcdHy0j9ZAquyscsWo%2F6B6%2B%2B7e8JturN%2Bb2kxKJ7FhIBBfC%2BLOxBO%2BcCLgx7o%2Fu12R9X84YxP6jdxmkWUfgUgCLeWVQWMlzcefwtMBwjoiJA%2FUATLhNKudMyGoKMLpkMvk%2B9tUNH79pdIr5DVJFS5T4DUcVe7nc4N%2FmeKlyDfNxA5lCuv9XmImg7kw8rTwvAY6pgEZtvmd9IdGR5xtwHiUdSET3QFrnc2hop3KER%2BEdxFxa8WG4JbitqWJ%2Bi0l%2FFsjERo%2B030AavgJ2wno1%2FFkdMjrhbdF3ZRmvObb4Fw98pN5b28%2FCw2%2BpDkNBhhDJih%2BuG0H1RI%2FO%2FU%2BvvGqxbXuBp1%2BrTKzjIeimNtU%2B%2BxKkfEZI8aJauN2CSADV1Q18IPOefQ6vbaVN4zpRGCHd3WQ03Y2mGk%2FdPx9&X-Amz-Signature=0a39eb326c2cbd398b7c3258bcc67aa774ed3095fe111c57be5c723a5d6efbeb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BXVQSWK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA4LKlla%2FeZtToG6wOm5IBhRoJd7nCy0uZIP8ZjZIQrGAiBKJv%2B7MFWc5yYsQzZb00klo7%2B2ulxa4YL4f6cDRDuyuiqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMABA9KHdj1qCRO4hPKtwDVUNUTP1EbFxYxsnntKLpZYAXYzEwEv3Dqfozq1Tz3MI308lUXymhrit7iYQI%2Fry0vilcXdSxyKLXORXOr3JWPqxPQd3sesdTw9HCU13EYkS8MyD%2BvrSuxm7J1hJ6yo6qP2ascMzASpdXFqHV7e6mPfYepGZVNfSw%2BH5RLqRUn1Tj2R9weD%2FA3gSL4%2FCp3SZ9EJonrb1Sd0WGpVlyiByhETqPY9yeQq1giXGhEO7HcaDQSPoKKETdNqdikf0mrLjRRd4jYFJUyaGIdSJltopaLvxdTJY9X68vSu%2FcNUiHkHLUrB3ymHejTy2fKYwsQO0FSdMz83bMiQSXOIpMhYmT5%2BHtOlloq8nfC5ARRwnjhdRKgzm%2Fbty%2BhQK5wo6xTPTwTQTEo4UDFDx4A9cc4DWATU5vG4BdspUWPBVzM1NSn8v7YDteFQWSZxSs%2F1wCBDooTUFcdHy0j9ZAquyscsWo%2F6B6%2B%2B7e8JturN%2Bb2kxKJ7FhIBBfC%2BLOxBO%2BcCLgx7o%2Fu12R9X84YxP6jdxmkWUfgUgCLeWVQWMlzcefwtMBwjoiJA%2FUATLhNKudMyGoKMLpkMvk%2B9tUNH79pdIr5DVJFS5T4DUcVe7nc4N%2FmeKlyDfNxA5lCuv9XmImg7kw8rTwvAY6pgEZtvmd9IdGR5xtwHiUdSET3QFrnc2hop3KER%2BEdxFxa8WG4JbitqWJ%2Bi0l%2FFsjERo%2B030AavgJ2wno1%2FFkdMjrhbdF3ZRmvObb4Fw98pN5b28%2FCw2%2BpDkNBhhDJih%2BuG0H1RI%2FO%2FU%2BvvGqxbXuBp1%2BrTKzjIeimNtU%2B%2BxKkfEZI8aJauN2CSADV1Q18IPOefQ6vbaVN4zpRGCHd3WQ03Y2mGk%2FdPx9&X-Amz-Signature=1a011aa8733e89800caaa4f83ab16071966b0e60004ae60c661b818cfa532638&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMGZ6EKO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAxLLwSvVrg0%2BusFCgW%2FbmjFSIhC6wASOjolUIRJMeVKAiAGDDXyLzTEr4WfFUst54P3uXpJ6LZzaRVVQFDD4%2BrUxyqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMamiIf2EbZcNsHi4JKtwDem7Agca3F%2BX%2F8fBrwE5U2O9%2BijwvUQmmAmGcyBmouFaMgTiO1h23hGrOuf0jJuy39BG13zNeDPbARhO%2F8YRwJP9T7OPYKm%2FIUJNhmr3bb3kSJXpREJd2VCHOZEmOeAaCvS%2BQkhQMTz2ADFVHsMlWDYyHC5kHb7G33Ge5D9gUjpqRVEUwCAZyifKVZQ0tYVkB7yvvoh9%2BP0cfJQsHn0khir6SxZp6O7yXaLc3dVyqKEeVM07NoLicQFRz%2FpbgrASd1X%2FnV2b6kgk42KrndPai7QRThl4kdrfPWtFutACtE4PD5AcnVNPdbUuQ8uOg7cvu9KOLJCiSkZYG4fYbzdcnMUM9Xmo80dcNGXy1w%2BkB4%2B7e0Vef3GCgUepBoZFa1HlZWpxnfuHLl%2BRKNOY8uuylc5TpjoLwjqliIPIRffgV9wEgsqu9Am4tvpixuGMiHyj8XhgWxAq0Q%2B16R8ysWeTd9MrCSusjlj%2FVMqZTYJAfIRAPumywXsNsMPontoME988X89DG0nNql0yzPEVxBk4yRdM5QKvdBPM43VzrhvFOH0OPYtsok4k0m2uou3WQJaCcJHVfM7DGzi%2BMM30wbag1DVeTqDndhXWLAOM9nm8YnrU4q%2FusI3i7UVuZJM8w1bTwvAY6pgFbR9E%2B4sITcjqBobH1wUxji6Jq1CaqHeeVrdiqSi5IFLjV0pEJEqhBGDCzhLdgMEKDmjbfw5zYvQWom%2BE5AE9vBv0DdKAkPCJk1KHXoRKG8ENukxAVxIU8UOE2tiQsFPi9cHk91Fkm2oAVsP5T%2FCYeWoeP%2B7c8jVfVj9DLFM1UcXzBx%2Bu0AtutO9W1Mcqf%2F%2BaliZDpfyH0XxU9LqNE%2FeYXr02L8I%2FU&X-Amz-Signature=8c6d6e266dabc8fb577751533c27c9c188abecff765693099141778e346cc013&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMGZ6EKO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAxLLwSvVrg0%2BusFCgW%2FbmjFSIhC6wASOjolUIRJMeVKAiAGDDXyLzTEr4WfFUst54P3uXpJ6LZzaRVVQFDD4%2BrUxyqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMamiIf2EbZcNsHi4JKtwDem7Agca3F%2BX%2F8fBrwE5U2O9%2BijwvUQmmAmGcyBmouFaMgTiO1h23hGrOuf0jJuy39BG13zNeDPbARhO%2F8YRwJP9T7OPYKm%2FIUJNhmr3bb3kSJXpREJd2VCHOZEmOeAaCvS%2BQkhQMTz2ADFVHsMlWDYyHC5kHb7G33Ge5D9gUjpqRVEUwCAZyifKVZQ0tYVkB7yvvoh9%2BP0cfJQsHn0khir6SxZp6O7yXaLc3dVyqKEeVM07NoLicQFRz%2FpbgrASd1X%2FnV2b6kgk42KrndPai7QRThl4kdrfPWtFutACtE4PD5AcnVNPdbUuQ8uOg7cvu9KOLJCiSkZYG4fYbzdcnMUM9Xmo80dcNGXy1w%2BkB4%2B7e0Vef3GCgUepBoZFa1HlZWpxnfuHLl%2BRKNOY8uuylc5TpjoLwjqliIPIRffgV9wEgsqu9Am4tvpixuGMiHyj8XhgWxAq0Q%2B16R8ysWeTd9MrCSusjlj%2FVMqZTYJAfIRAPumywXsNsMPontoME988X89DG0nNql0yzPEVxBk4yRdM5QKvdBPM43VzrhvFOH0OPYtsok4k0m2uou3WQJaCcJHVfM7DGzi%2BMM30wbag1DVeTqDndhXWLAOM9nm8YnrU4q%2FusI3i7UVuZJM8w1bTwvAY6pgFbR9E%2B4sITcjqBobH1wUxji6Jq1CaqHeeVrdiqSi5IFLjV0pEJEqhBGDCzhLdgMEKDmjbfw5zYvQWom%2BE5AE9vBv0DdKAkPCJk1KHXoRKG8ENukxAVxIU8UOE2tiQsFPi9cHk91Fkm2oAVsP5T%2FCYeWoeP%2B7c8jVfVj9DLFM1UcXzBx%2Bu0AtutO9W1Mcqf%2F%2BaliZDpfyH0XxU9LqNE%2FeYXr02L8I%2FU&X-Amz-Signature=fd32cc569aa19468082dbcde217ae9e5d51bdd744b19f51bcee54d86e34c3b73&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BXVQSWK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA4LKlla%2FeZtToG6wOm5IBhRoJd7nCy0uZIP8ZjZIQrGAiBKJv%2B7MFWc5yYsQzZb00klo7%2B2ulxa4YL4f6cDRDuyuiqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMABA9KHdj1qCRO4hPKtwDVUNUTP1EbFxYxsnntKLpZYAXYzEwEv3Dqfozq1Tz3MI308lUXymhrit7iYQI%2Fry0vilcXdSxyKLXORXOr3JWPqxPQd3sesdTw9HCU13EYkS8MyD%2BvrSuxm7J1hJ6yo6qP2ascMzASpdXFqHV7e6mPfYepGZVNfSw%2BH5RLqRUn1Tj2R9weD%2FA3gSL4%2FCp3SZ9EJonrb1Sd0WGpVlyiByhETqPY9yeQq1giXGhEO7HcaDQSPoKKETdNqdikf0mrLjRRd4jYFJUyaGIdSJltopaLvxdTJY9X68vSu%2FcNUiHkHLUrB3ymHejTy2fKYwsQO0FSdMz83bMiQSXOIpMhYmT5%2BHtOlloq8nfC5ARRwnjhdRKgzm%2Fbty%2BhQK5wo6xTPTwTQTEo4UDFDx4A9cc4DWATU5vG4BdspUWPBVzM1NSn8v7YDteFQWSZxSs%2F1wCBDooTUFcdHy0j9ZAquyscsWo%2F6B6%2B%2B7e8JturN%2Bb2kxKJ7FhIBBfC%2BLOxBO%2BcCLgx7o%2Fu12R9X84YxP6jdxmkWUfgUgCLeWVQWMlzcefwtMBwjoiJA%2FUATLhNKudMyGoKMLpkMvk%2B9tUNH79pdIr5DVJFS5T4DUcVe7nc4N%2FmeKlyDfNxA5lCuv9XmImg7kw8rTwvAY6pgEZtvmd9IdGR5xtwHiUdSET3QFrnc2hop3KER%2BEdxFxa8WG4JbitqWJ%2Bi0l%2FFsjERo%2B030AavgJ2wno1%2FFkdMjrhbdF3ZRmvObb4Fw98pN5b28%2FCw2%2BpDkNBhhDJih%2BuG0H1RI%2FO%2FU%2BvvGqxbXuBp1%2BrTKzjIeimNtU%2B%2BxKkfEZI8aJauN2CSADV1Q18IPOefQ6vbaVN4zpRGCHd3WQ03Y2mGk%2FdPx9&X-Amz-Signature=3c2ac0bccf8dd95bd5d9ec3ccf034dc8e3e7ccb96ad77b68f0502f31451f33fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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