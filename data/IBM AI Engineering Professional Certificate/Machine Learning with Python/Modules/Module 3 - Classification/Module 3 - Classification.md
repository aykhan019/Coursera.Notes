

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THK6BDIM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFtjCVte%2BxCCgC4jp9nIYbz2Qr8CzczbzEy13JofDEVLAiEA%2FXhYqYwOpMCN8Puq336m0Xqqd3s50aOucVLWjv%2B2%2F%2BEq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOf3vpuqseVU6%2Fdo8ircA1NX4VgpuPT2%2FHOoVRwa9npMvTuatmP8q2urm%2F3ENhMBt2xhPAmkyQsAQ9eGWAdsRX20k7%2FYv%2BIzGPVB9Cm9Ylk9MtrXIYkQj7umpBY2DbucHOZchvSQIT9hn1BTGW2UKjsyhldXr6D1cQi0KGI%2FFnU257ewiI0%2BaXZV9KthL6yYnunA5KFM0yFpg4iMM9P3WPbs0yq7qjcS5g%2BK%2Bh2Xmn%2FdnO42pj9eKu0p0V69b5IJd2BpHJTPyrXPRBH7FdtFWkefNr3T9jXUOrMa9%2FkTfFgwWmvvs1TT%2B%2BqUJ6QiJZQYrbpG8J8yZK7n98BCWzdPOpzNkos3RhfQ0jY8xY1mXb6ZPT6zH3%2Fpufi7VMmEONJo7fMcmTzhfek2H1zoG%2BRZIk2bwiWSVtWj31db1XTXt8asui5qhDgu2B5n3%2BG%2FRs%2BGUwo46D5prmJqRmDPvW5C7usIuvmdXHjZiWGR4gx3ifcYkx4oZ4Npl1DDdu226wUfotQWyXcDk3szre%2Biy7P63lp2Yv1%2BAlNMZUy%2F8Mcqzf%2F%2Bv8tSOsGVAWZuMDyGi8uF1aa3ZVYoXoLneHBiacjOTyKIYXdMFxhefe0%2B%2FKCBQ%2FD9SoScurKEYrPjcAIGks8aXhhhVcr%2F0%2FxjTnU0MOq8hL0GOqUB5P1aZFE2ZQAqBZM2fn5wypZAnu5yXCGrVoC5N4cfzSDrcv2CKaGqWf%2B5EOv69mVfsAAOenFXWwoe9Ysy6y5kOY2OTA62RIfwHxvRGTNCJGu6TgkSxU211keV8%2B5dayCVsWPb5KNMNVa1pkosSy9u%2BApVXDEo0%2B83IKn63m0a0ctdpUJQOJC5lz54GoA0IXqQ05gE%2B3gsXIjTRtGVBI8jKtTcw%2BFN&X-Amz-Signature=2738e0a545e161b079e9be826bf8963273ec50ac604d948716588c737478f19b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THK6BDIM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFtjCVte%2BxCCgC4jp9nIYbz2Qr8CzczbzEy13JofDEVLAiEA%2FXhYqYwOpMCN8Puq336m0Xqqd3s50aOucVLWjv%2B2%2F%2BEq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOf3vpuqseVU6%2Fdo8ircA1NX4VgpuPT2%2FHOoVRwa9npMvTuatmP8q2urm%2F3ENhMBt2xhPAmkyQsAQ9eGWAdsRX20k7%2FYv%2BIzGPVB9Cm9Ylk9MtrXIYkQj7umpBY2DbucHOZchvSQIT9hn1BTGW2UKjsyhldXr6D1cQi0KGI%2FFnU257ewiI0%2BaXZV9KthL6yYnunA5KFM0yFpg4iMM9P3WPbs0yq7qjcS5g%2BK%2Bh2Xmn%2FdnO42pj9eKu0p0V69b5IJd2BpHJTPyrXPRBH7FdtFWkefNr3T9jXUOrMa9%2FkTfFgwWmvvs1TT%2B%2BqUJ6QiJZQYrbpG8J8yZK7n98BCWzdPOpzNkos3RhfQ0jY8xY1mXb6ZPT6zH3%2Fpufi7VMmEONJo7fMcmTzhfek2H1zoG%2BRZIk2bwiWSVtWj31db1XTXt8asui5qhDgu2B5n3%2BG%2FRs%2BGUwo46D5prmJqRmDPvW5C7usIuvmdXHjZiWGR4gx3ifcYkx4oZ4Npl1DDdu226wUfotQWyXcDk3szre%2Biy7P63lp2Yv1%2BAlNMZUy%2F8Mcqzf%2F%2Bv8tSOsGVAWZuMDyGi8uF1aa3ZVYoXoLneHBiacjOTyKIYXdMFxhefe0%2B%2FKCBQ%2FD9SoScurKEYrPjcAIGks8aXhhhVcr%2F0%2FxjTnU0MOq8hL0GOqUB5P1aZFE2ZQAqBZM2fn5wypZAnu5yXCGrVoC5N4cfzSDrcv2CKaGqWf%2B5EOv69mVfsAAOenFXWwoe9Ysy6y5kOY2OTA62RIfwHxvRGTNCJGu6TgkSxU211keV8%2B5dayCVsWPb5KNMNVa1pkosSy9u%2BApVXDEo0%2B83IKn63m0a0ctdpUJQOJC5lz54GoA0IXqQ05gE%2B3gsXIjTRtGVBI8jKtTcw%2BFN&X-Amz-Signature=2980c1a3f63447ee88845fb778142e1c669ed55c235cec565d708bb59e727dc0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THK6BDIM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFtjCVte%2BxCCgC4jp9nIYbz2Qr8CzczbzEy13JofDEVLAiEA%2FXhYqYwOpMCN8Puq336m0Xqqd3s50aOucVLWjv%2B2%2F%2BEq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOf3vpuqseVU6%2Fdo8ircA1NX4VgpuPT2%2FHOoVRwa9npMvTuatmP8q2urm%2F3ENhMBt2xhPAmkyQsAQ9eGWAdsRX20k7%2FYv%2BIzGPVB9Cm9Ylk9MtrXIYkQj7umpBY2DbucHOZchvSQIT9hn1BTGW2UKjsyhldXr6D1cQi0KGI%2FFnU257ewiI0%2BaXZV9KthL6yYnunA5KFM0yFpg4iMM9P3WPbs0yq7qjcS5g%2BK%2Bh2Xmn%2FdnO42pj9eKu0p0V69b5IJd2BpHJTPyrXPRBH7FdtFWkefNr3T9jXUOrMa9%2FkTfFgwWmvvs1TT%2B%2BqUJ6QiJZQYrbpG8J8yZK7n98BCWzdPOpzNkos3RhfQ0jY8xY1mXb6ZPT6zH3%2Fpufi7VMmEONJo7fMcmTzhfek2H1zoG%2BRZIk2bwiWSVtWj31db1XTXt8asui5qhDgu2B5n3%2BG%2FRs%2BGUwo46D5prmJqRmDPvW5C7usIuvmdXHjZiWGR4gx3ifcYkx4oZ4Npl1DDdu226wUfotQWyXcDk3szre%2Biy7P63lp2Yv1%2BAlNMZUy%2F8Mcqzf%2F%2Bv8tSOsGVAWZuMDyGi8uF1aa3ZVYoXoLneHBiacjOTyKIYXdMFxhefe0%2B%2FKCBQ%2FD9SoScurKEYrPjcAIGks8aXhhhVcr%2F0%2FxjTnU0MOq8hL0GOqUB5P1aZFE2ZQAqBZM2fn5wypZAnu5yXCGrVoC5N4cfzSDrcv2CKaGqWf%2B5EOv69mVfsAAOenFXWwoe9Ysy6y5kOY2OTA62RIfwHxvRGTNCJGu6TgkSxU211keV8%2B5dayCVsWPb5KNMNVa1pkosSy9u%2BApVXDEo0%2B83IKn63m0a0ctdpUJQOJC5lz54GoA0IXqQ05gE%2B3gsXIjTRtGVBI8jKtTcw%2BFN&X-Amz-Signature=6e06d9f3cb3411d79a1e078c08bf19866367f92d99f6587963f228f73848c51a&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRZ5WRLF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDI4Ng4PTaLk4VBnwoz4aDLeiI8GoNu00swHPU4eYHY4wIhAPfGxAzfWn2y6GkJxupvUlrYP0bEGEz0TLZA5YahNtREKv8DCB0QABoMNjM3NDIzMTgzODA1IgwSG2N%2BxpK6EvvxX9Qq3AOWyaO44C4cqfycBRCSDdDMtYMM0AkpGSdxEEDgsvCcz0HRc0x5GznGWQWzyhiYELKYZGrxzIfzVznnbG074w4Zw3u8TOAblpWYsbUw%2FZEYAB9Ak3dIeeQPBRlngeRLsYmw9W6jh1hnr7g9wb4HBPrqwArVjwv%2BG79RGrX8mN%2BRhmE7YHYJ6iiytI1g1MUt6D%2BbOXyvy2iACc2LyAqJSNZ5UniWWdHcPelqiN78ffeTpeoq7LpzVb6ulguZtNnjmGR7lBXuW5leVECDSkFslq0bFOCSj8m0TV3PGUmEYggNrh4xPrRtR19kvqC6WgeVGzUGd12J1JrcGlbq6Drdyd1Q4cIzEnBiibolyMGPBvwbQEy0XKeJxQ3f8a2RvgyMU6aaXrmryWdvv1mfAj5kxomcy5kNNn6l%2FnVbg0dbgz7miaSPzRvICQSQaHBGcsa778O9r3mnB6RBmpRh39ZKN1DC%2FUXPEE5kp6npX3wdL399oiJWdplflYjqH%2BGco3siwx%2BO4tCOyK%2FvBEpsESTm6rHSzO%2BS4jYTDKXXFzJDHJjFXqtL8vCD0pOGBNj6LHzNfZTUHYr7oLbyNL0N67y5x0iBOIiiW7%2BwxW2Qn9%2B1VKiaHpGm7Y%2B15xBaT91P4TCUvYS9BjqkATPzzOLpdl9ReDEqMfG%2FbwHXFpauvsQIQWHwLmvclxDSZCO%2F4AqxFoeH5ErnYhMo7zLI6gHLYuAMkbbUHRI5h%2FqW1moJu61ZKvaaAPGL2D3dJJPS016XMD90UixFfiQ9Ast0eYIfoLhlddq3fU06S3NmRQR9r3NxGyDQipi5LmAnQwxMVXn0f%2B7ls7gG%2ByKi6fZVp8OTLBy2r3VYEMeK8cFbqHSc&X-Amz-Signature=5e0b0e156d640994afb6660fd270c41254b36b13e2464bb55140117ef924f5a2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRZ5WRLF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQDI4Ng4PTaLk4VBnwoz4aDLeiI8GoNu00swHPU4eYHY4wIhAPfGxAzfWn2y6GkJxupvUlrYP0bEGEz0TLZA5YahNtREKv8DCB0QABoMNjM3NDIzMTgzODA1IgwSG2N%2BxpK6EvvxX9Qq3AOWyaO44C4cqfycBRCSDdDMtYMM0AkpGSdxEEDgsvCcz0HRc0x5GznGWQWzyhiYELKYZGrxzIfzVznnbG074w4Zw3u8TOAblpWYsbUw%2FZEYAB9Ak3dIeeQPBRlngeRLsYmw9W6jh1hnr7g9wb4HBPrqwArVjwv%2BG79RGrX8mN%2BRhmE7YHYJ6iiytI1g1MUt6D%2BbOXyvy2iACc2LyAqJSNZ5UniWWdHcPelqiN78ffeTpeoq7LpzVb6ulguZtNnjmGR7lBXuW5leVECDSkFslq0bFOCSj8m0TV3PGUmEYggNrh4xPrRtR19kvqC6WgeVGzUGd12J1JrcGlbq6Drdyd1Q4cIzEnBiibolyMGPBvwbQEy0XKeJxQ3f8a2RvgyMU6aaXrmryWdvv1mfAj5kxomcy5kNNn6l%2FnVbg0dbgz7miaSPzRvICQSQaHBGcsa778O9r3mnB6RBmpRh39ZKN1DC%2FUXPEE5kp6npX3wdL399oiJWdplflYjqH%2BGco3siwx%2BO4tCOyK%2FvBEpsESTm6rHSzO%2BS4jYTDKXXFzJDHJjFXqtL8vCD0pOGBNj6LHzNfZTUHYr7oLbyNL0N67y5x0iBOIiiW7%2BwxW2Qn9%2B1VKiaHpGm7Y%2B15xBaT91P4TCUvYS9BjqkATPzzOLpdl9ReDEqMfG%2FbwHXFpauvsQIQWHwLmvclxDSZCO%2F4AqxFoeH5ErnYhMo7zLI6gHLYuAMkbbUHRI5h%2FqW1moJu61ZKvaaAPGL2D3dJJPS016XMD90UixFfiQ9Ast0eYIfoLhlddq3fU06S3NmRQR9r3NxGyDQipi5LmAnQwxMVXn0f%2B7ls7gG%2ByKi6fZVp8OTLBy2r3VYEMeK8cFbqHSc&X-Amz-Signature=17250718fc6f196adfec39427642d135efa1d9face463f856e13729d44b13dcd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THK6BDIM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIFtjCVte%2BxCCgC4jp9nIYbz2Qr8CzczbzEy13JofDEVLAiEA%2FXhYqYwOpMCN8Puq336m0Xqqd3s50aOucVLWjv%2B2%2F%2BEq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOf3vpuqseVU6%2Fdo8ircA1NX4VgpuPT2%2FHOoVRwa9npMvTuatmP8q2urm%2F3ENhMBt2xhPAmkyQsAQ9eGWAdsRX20k7%2FYv%2BIzGPVB9Cm9Ylk9MtrXIYkQj7umpBY2DbucHOZchvSQIT9hn1BTGW2UKjsyhldXr6D1cQi0KGI%2FFnU257ewiI0%2BaXZV9KthL6yYnunA5KFM0yFpg4iMM9P3WPbs0yq7qjcS5g%2BK%2Bh2Xmn%2FdnO42pj9eKu0p0V69b5IJd2BpHJTPyrXPRBH7FdtFWkefNr3T9jXUOrMa9%2FkTfFgwWmvvs1TT%2B%2BqUJ6QiJZQYrbpG8J8yZK7n98BCWzdPOpzNkos3RhfQ0jY8xY1mXb6ZPT6zH3%2Fpufi7VMmEONJo7fMcmTzhfek2H1zoG%2BRZIk2bwiWSVtWj31db1XTXt8asui5qhDgu2B5n3%2BG%2FRs%2BGUwo46D5prmJqRmDPvW5C7usIuvmdXHjZiWGR4gx3ifcYkx4oZ4Npl1DDdu226wUfotQWyXcDk3szre%2Biy7P63lp2Yv1%2BAlNMZUy%2F8Mcqzf%2F%2Bv8tSOsGVAWZuMDyGi8uF1aa3ZVYoXoLneHBiacjOTyKIYXdMFxhefe0%2B%2FKCBQ%2FD9SoScurKEYrPjcAIGks8aXhhhVcr%2F0%2FxjTnU0MOq8hL0GOqUB5P1aZFE2ZQAqBZM2fn5wypZAnu5yXCGrVoC5N4cfzSDrcv2CKaGqWf%2B5EOv69mVfsAAOenFXWwoe9Ysy6y5kOY2OTA62RIfwHxvRGTNCJGu6TgkSxU211keV8%2B5dayCVsWPb5KNMNVa1pkosSy9u%2BApVXDEo0%2B83IKn63m0a0ctdpUJQOJC5lz54GoA0IXqQ05gE%2B3gsXIjTRtGVBI8jKtTcw%2BFN&X-Amz-Signature=acb4f8bf7cdceee5720312d3f6ebcd95465c53d09684fbd5a0aed11cc0ecf92d&X-Amz-SignedHeaders=host&x-id=GetObject)
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