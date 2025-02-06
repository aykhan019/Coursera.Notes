

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LSGP4LQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIDZHCGVRn4jq3896gOX66%2BeKnB09GNGxvbYMvP0p33XDAiEAzqoCzMiUJr1z5yoTuOjmwxsx7PeY8zKG5tTn7Y4eu5Yq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJLGPbtOEy64FDrB2yrcA4OJMfwXrLOCUOPqo75obcEvWQ9mq%2FT0wwyW9aopBG24DrvbZKl7FENRSLDfRdQQzgIS3ba5Jg7TvSSmDC6%2FSLT7VbEbzOea2wcOrbBuUW3mBE43gw43Vdo1Gv5pM5HJmq0u25jpJ0BmPCr0tGfX6xh5DKTclMS1a9H7e1VzxHNNv%2FojkIehSqNt0RcImMdwpmyY5%2B1N8FNeWRlm8gM%2FStPAHXP0nYBFJp1hnP744RD9r6v0cJJnIJnT2TRkopS8ltZ8XrvN0w6csVKeoa1dRIaUJDkNCjF3sK%2FMNOeGAkjyXreeusdmHyL3VizRZy46aWSqTg7N8qRzFsdg%2BJHHwRU89A98M1wTPjXTlGXzJ6xI3OihOuxVSuwlr%2FZH1ep4cBzVUUpJgUlaKKCzB7M3ej7XEDOqKTFBoSb090HCvBUlBiMvTDRZpEei1dNpWiNgmB%2Br34ZJyYobc6BlbAO02yj0Kzt8kvqcaJHn5rKR2k%2Fw6%2BfhRK4LoWDjYiOjvxbR%2BQwdhvHo2efSVFH0rikIesNIjN95CMyYBjD4uwapeD7Z7ienaOK%2BzvWrgSYd%2F7XlwK%2F6wP%2FCG8tiotPV8uhnsbIz8vFIFoOnpAWp4ASotHmS5U5rGxC15LHChHYNMNbrkb0GOqUB4J9GPDJMFLPHEvPSiA0kODXYr8mlM9K2%2Fk%2F6kln2TRCqeFgCEinZSQq2IPH098Bua2VoeJtnv981m6oAoRCOWRjWRSzxzvuo%2BHcdmWOeuAQoCYATi5ZW4mKKz7qTsCBiFEpyRGO3WPU6vY0l1pb8krajHWzO3DrXfj2uMKv3Rw0rjDtmcj9sgHE7JOF9DV2Dva4gkWxSYU7itZrtcCmuS1j0ksKf&X-Amz-Signature=ce99fb36b8a3990fe7ca6ee35b661e6ab897a0b63f1ec8483bfaa8ead788dca6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LSGP4LQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIDZHCGVRn4jq3896gOX66%2BeKnB09GNGxvbYMvP0p33XDAiEAzqoCzMiUJr1z5yoTuOjmwxsx7PeY8zKG5tTn7Y4eu5Yq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJLGPbtOEy64FDrB2yrcA4OJMfwXrLOCUOPqo75obcEvWQ9mq%2FT0wwyW9aopBG24DrvbZKl7FENRSLDfRdQQzgIS3ba5Jg7TvSSmDC6%2FSLT7VbEbzOea2wcOrbBuUW3mBE43gw43Vdo1Gv5pM5HJmq0u25jpJ0BmPCr0tGfX6xh5DKTclMS1a9H7e1VzxHNNv%2FojkIehSqNt0RcImMdwpmyY5%2B1N8FNeWRlm8gM%2FStPAHXP0nYBFJp1hnP744RD9r6v0cJJnIJnT2TRkopS8ltZ8XrvN0w6csVKeoa1dRIaUJDkNCjF3sK%2FMNOeGAkjyXreeusdmHyL3VizRZy46aWSqTg7N8qRzFsdg%2BJHHwRU89A98M1wTPjXTlGXzJ6xI3OihOuxVSuwlr%2FZH1ep4cBzVUUpJgUlaKKCzB7M3ej7XEDOqKTFBoSb090HCvBUlBiMvTDRZpEei1dNpWiNgmB%2Br34ZJyYobc6BlbAO02yj0Kzt8kvqcaJHn5rKR2k%2Fw6%2BfhRK4LoWDjYiOjvxbR%2BQwdhvHo2efSVFH0rikIesNIjN95CMyYBjD4uwapeD7Z7ienaOK%2BzvWrgSYd%2F7XlwK%2F6wP%2FCG8tiotPV8uhnsbIz8vFIFoOnpAWp4ASotHmS5U5rGxC15LHChHYNMNbrkb0GOqUB4J9GPDJMFLPHEvPSiA0kODXYr8mlM9K2%2Fk%2F6kln2TRCqeFgCEinZSQq2IPH098Bua2VoeJtnv981m6oAoRCOWRjWRSzxzvuo%2BHcdmWOeuAQoCYATi5ZW4mKKz7qTsCBiFEpyRGO3WPU6vY0l1pb8krajHWzO3DrXfj2uMKv3Rw0rjDtmcj9sgHE7JOF9DV2Dva4gkWxSYU7itZrtcCmuS1j0ksKf&X-Amz-Signature=3b8429e5c618ef38f333a4336e4fcf6ea1d981f57f89a918c55bccc9d287a8c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LSGP4LQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIDZHCGVRn4jq3896gOX66%2BeKnB09GNGxvbYMvP0p33XDAiEAzqoCzMiUJr1z5yoTuOjmwxsx7PeY8zKG5tTn7Y4eu5Yq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJLGPbtOEy64FDrB2yrcA4OJMfwXrLOCUOPqo75obcEvWQ9mq%2FT0wwyW9aopBG24DrvbZKl7FENRSLDfRdQQzgIS3ba5Jg7TvSSmDC6%2FSLT7VbEbzOea2wcOrbBuUW3mBE43gw43Vdo1Gv5pM5HJmq0u25jpJ0BmPCr0tGfX6xh5DKTclMS1a9H7e1VzxHNNv%2FojkIehSqNt0RcImMdwpmyY5%2B1N8FNeWRlm8gM%2FStPAHXP0nYBFJp1hnP744RD9r6v0cJJnIJnT2TRkopS8ltZ8XrvN0w6csVKeoa1dRIaUJDkNCjF3sK%2FMNOeGAkjyXreeusdmHyL3VizRZy46aWSqTg7N8qRzFsdg%2BJHHwRU89A98M1wTPjXTlGXzJ6xI3OihOuxVSuwlr%2FZH1ep4cBzVUUpJgUlaKKCzB7M3ej7XEDOqKTFBoSb090HCvBUlBiMvTDRZpEei1dNpWiNgmB%2Br34ZJyYobc6BlbAO02yj0Kzt8kvqcaJHn5rKR2k%2Fw6%2BfhRK4LoWDjYiOjvxbR%2BQwdhvHo2efSVFH0rikIesNIjN95CMyYBjD4uwapeD7Z7ienaOK%2BzvWrgSYd%2F7XlwK%2F6wP%2FCG8tiotPV8uhnsbIz8vFIFoOnpAWp4ASotHmS5U5rGxC15LHChHYNMNbrkb0GOqUB4J9GPDJMFLPHEvPSiA0kODXYr8mlM9K2%2Fk%2F6kln2TRCqeFgCEinZSQq2IPH098Bua2VoeJtnv981m6oAoRCOWRjWRSzxzvuo%2BHcdmWOeuAQoCYATi5ZW4mKKz7qTsCBiFEpyRGO3WPU6vY0l1pb8krajHWzO3DrXfj2uMKv3Rw0rjDtmcj9sgHE7JOF9DV2Dva4gkWxSYU7itZrtcCmuS1j0ksKf&X-Amz-Signature=7a7874dbc79bc3caaf621eb8cfc40672b2bea08aaa8a6e2cb0f21b1766beaf30&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466552KYLZH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIDtrB%2B%2Fl%2BAqj2hMHBS%2FouKhNcr3zg%2FtE%2B17pQ5zvbpNsAiEApDpK7mTkxV1JgEb%2BbLLF7KHQPDqKUEzMDGYJNibaXBoq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDN%2BfF5yzpcfO3rKX8yrcA%2BjjXDw8%2F24CCnPR3zwVsP8JMJ0al2OdTLayxQjVuumD7HnZ7Wi8iWOrEub2s0T4yevJCOUk1kjgx5FSbc%2F0wKNNtYoCFSbN%2F1TZMo9%2FInussIANgRfO1TBO9by7JBafQKkgPF4jPczCLu4IgFvDoPzGf0N0adcZbCgPS7JoSC0H%2Bpm2uOtVChTYhZCBC2JlD6oUOgiKRvceFz3qGSRE14IC2QrzcLzhxmogzMdU81g829nOUvbw5jv6REGeZCluUgeRtd8PB1OEptLTEPuNuJGuXVCtfA4%2BVfyZE7xGGPy2BJuNoUnzm6OWk8LN4yjCPNHjkn1ZvPcxWMtmSqsHpN72hW0LSylMy3SrgTvyV%2B1iqMC6IXUdbZgSpEDtPm3%2FlVrUsZ%2BfEFNnmKfpI2yIrEGdwALKRk7kDzDVZSdKrks06yikdsWJWCmKpcBq1AgtQ3tlljDgRpvD0IGYRP8IJHlYZfjJ3jFNeA3BJ2nz926I%2F996nBFIwdOA6xlLOdvJZOSzbqOZPu2v9Lr6d99KUXdVPi2LVdydEpLHyWp%2FnodwISZL1K2XBzybU6A51%2BRbDwt4h7fHcR3P4BtUnCQjaaGDYR0yJYXJTJOmzQDGEGFcPNxjHw4E0SC3pNl8MJHskb0GOqUB1F03pudAanJfRPLa980OhjyBFd485lt045AiUUwjvhcKu4AzSKAKwFg2VnCf37Vv3mOoli%2FaCAygqsBnzgE%2BdwJ8OjF8y0diaXy03bgkgPKkxCsNfVNr5wItlBXMJju5BD6iCWrvCW%2Fx6Q6nyQH60YRW26hvzHECHrmqvNFlNTQp1bubqUXdXpNsnRE%2B22cccxl75ddlTCoO5BYfGhGn%2FbD%2Bmf%2Fa&X-Amz-Signature=6f1879fc69825210cafbe5002fab1430a9a74b0b93796ccc295dc171a2ff6e17&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466552KYLZH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIDtrB%2B%2Fl%2BAqj2hMHBS%2FouKhNcr3zg%2FtE%2B17pQ5zvbpNsAiEApDpK7mTkxV1JgEb%2BbLLF7KHQPDqKUEzMDGYJNibaXBoq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDN%2BfF5yzpcfO3rKX8yrcA%2BjjXDw8%2F24CCnPR3zwVsP8JMJ0al2OdTLayxQjVuumD7HnZ7Wi8iWOrEub2s0T4yevJCOUk1kjgx5FSbc%2F0wKNNtYoCFSbN%2F1TZMo9%2FInussIANgRfO1TBO9by7JBafQKkgPF4jPczCLu4IgFvDoPzGf0N0adcZbCgPS7JoSC0H%2Bpm2uOtVChTYhZCBC2JlD6oUOgiKRvceFz3qGSRE14IC2QrzcLzhxmogzMdU81g829nOUvbw5jv6REGeZCluUgeRtd8PB1OEptLTEPuNuJGuXVCtfA4%2BVfyZE7xGGPy2BJuNoUnzm6OWk8LN4yjCPNHjkn1ZvPcxWMtmSqsHpN72hW0LSylMy3SrgTvyV%2B1iqMC6IXUdbZgSpEDtPm3%2FlVrUsZ%2BfEFNnmKfpI2yIrEGdwALKRk7kDzDVZSdKrks06yikdsWJWCmKpcBq1AgtQ3tlljDgRpvD0IGYRP8IJHlYZfjJ3jFNeA3BJ2nz926I%2F996nBFIwdOA6xlLOdvJZOSzbqOZPu2v9Lr6d99KUXdVPi2LVdydEpLHyWp%2FnodwISZL1K2XBzybU6A51%2BRbDwt4h7fHcR3P4BtUnCQjaaGDYR0yJYXJTJOmzQDGEGFcPNxjHw4E0SC3pNl8MJHskb0GOqUB1F03pudAanJfRPLa980OhjyBFd485lt045AiUUwjvhcKu4AzSKAKwFg2VnCf37Vv3mOoli%2FaCAygqsBnzgE%2BdwJ8OjF8y0diaXy03bgkgPKkxCsNfVNr5wItlBXMJju5BD6iCWrvCW%2Fx6Q6nyQH60YRW26hvzHECHrmqvNFlNTQp1bubqUXdXpNsnRE%2B22cccxl75ddlTCoO5BYfGhGn%2FbD%2Bmf%2Fa&X-Amz-Signature=d803bbee190848dc7bb9fbe7f578ad16c3b006954cc68a3d443c88dfba9fcf0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LSGP4LQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T091543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIDZHCGVRn4jq3896gOX66%2BeKnB09GNGxvbYMvP0p33XDAiEAzqoCzMiUJr1z5yoTuOjmwxsx7PeY8zKG5tTn7Y4eu5Yq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDJLGPbtOEy64FDrB2yrcA4OJMfwXrLOCUOPqo75obcEvWQ9mq%2FT0wwyW9aopBG24DrvbZKl7FENRSLDfRdQQzgIS3ba5Jg7TvSSmDC6%2FSLT7VbEbzOea2wcOrbBuUW3mBE43gw43Vdo1Gv5pM5HJmq0u25jpJ0BmPCr0tGfX6xh5DKTclMS1a9H7e1VzxHNNv%2FojkIehSqNt0RcImMdwpmyY5%2B1N8FNeWRlm8gM%2FStPAHXP0nYBFJp1hnP744RD9r6v0cJJnIJnT2TRkopS8ltZ8XrvN0w6csVKeoa1dRIaUJDkNCjF3sK%2FMNOeGAkjyXreeusdmHyL3VizRZy46aWSqTg7N8qRzFsdg%2BJHHwRU89A98M1wTPjXTlGXzJ6xI3OihOuxVSuwlr%2FZH1ep4cBzVUUpJgUlaKKCzB7M3ej7XEDOqKTFBoSb090HCvBUlBiMvTDRZpEei1dNpWiNgmB%2Br34ZJyYobc6BlbAO02yj0Kzt8kvqcaJHn5rKR2k%2Fw6%2BfhRK4LoWDjYiOjvxbR%2BQwdhvHo2efSVFH0rikIesNIjN95CMyYBjD4uwapeD7Z7ienaOK%2BzvWrgSYd%2F7XlwK%2F6wP%2FCG8tiotPV8uhnsbIz8vFIFoOnpAWp4ASotHmS5U5rGxC15LHChHYNMNbrkb0GOqUB4J9GPDJMFLPHEvPSiA0kODXYr8mlM9K2%2Fk%2F6kln2TRCqeFgCEinZSQq2IPH098Bua2VoeJtnv981m6oAoRCOWRjWRSzxzvuo%2BHcdmWOeuAQoCYATi5ZW4mKKz7qTsCBiFEpyRGO3WPU6vY0l1pb8krajHWzO3DrXfj2uMKv3Rw0rjDtmcj9sgHE7JOF9DV2Dva4gkWxSYU7itZrtcCmuS1j0ksKf&X-Amz-Signature=aa7e79832dd46f933f2e54876511d6047ee17cd85632144d485c27fb7dcfb3c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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