

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZW572V6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID98wT9ZmEU3AYiROu598hxtjKmW4VWcLDrVn5BDAnYDAiBmByRNTsCOLLvqE2MZs0cQfNsPJeMS9O7GzpnE2FD0IiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDPQG%2BL4Fy2OGFD6tKtwDbrIFe0AeP6UiWvo9vdAalnFELtwh1SHcLD3UMk0egfzZd7EpxPDxHiDBBwuYkQxFjQBrUklYShLYsi330f%2BtMnt8QTaLd4eueJEW7TNgOK94PmYxKSNfMGcRkWevdB3hXA9QlmX0zMPP%2BG0QR0S3V1kSKzWREEcCVokrdg1lzoWr%2FzQ0UucnXtro4ZEND37V%2F27FA27vT8kOH3hc%2FzjhZlADTEKyYwFd5E1B4gkRTxF8JdC7oVfgKT%2BSLcXwf546boNa%2BxNB8616pDAwGGZr0smDLKMgPl2o289RmyykFSvR31mAQ7HiIrte%2BP%2FPOquoNE9iMORPfVR3a4kO8zqLoEKweppd9j6zx8X4AnF3Bq3yZeK105xhWuC%2FNGJuISPJYFBT3KsiGFOFV%2Bk%2FLamOt6paZdPpUdIlUpsaEpbazhr6y8JsauaI6KYMfUU2ApJZ6UWjTcAmZ1ZRmICQABNhj3djoDgq8Li15U%2FOhu8OXCZ5PEZOGzjZH7AFWM0a%2FDMrrqx%2BGLjIwZAr3lHokl63dik1wrOMnXrWFCpBYfIhuoNJxjV2ixY6j3zSoui3FGC5nEMJddejxbPfCd%2FOyGeW%2FFqt8vpJBXPCUxtuTAyoHSWt4tiIhjk%2BqKufMcAwwPXpvAY6pgHW9FoNRFINBj%2FIAuCOREYKOuRXJ83VvEp%2BkVT91ZAE8ceE2qjj%2FbZdhaq5nG7d86n2T0GhBpTrQUgpHOoSzVAm4kNE%2Bwb5ujxSMiCr%2FBCEtYW8HWDmgtbtBdJTNW99ffNFI%2B%2Fytj8eKOaD6Sl2tQtKbs26S6t5cJ5wDb4kvRHYjy%2BN2hxC1RuS9x4x3TBZ02GUof1yQIkq0TRwRR4mgZjG%2FcEVZnd2&X-Amz-Signature=dfe908475f4b7422f712aa5a0ec4b3563fac2eab4c4de929be263c4433d72d16&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZW572V6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID98wT9ZmEU3AYiROu598hxtjKmW4VWcLDrVn5BDAnYDAiBmByRNTsCOLLvqE2MZs0cQfNsPJeMS9O7GzpnE2FD0IiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDPQG%2BL4Fy2OGFD6tKtwDbrIFe0AeP6UiWvo9vdAalnFELtwh1SHcLD3UMk0egfzZd7EpxPDxHiDBBwuYkQxFjQBrUklYShLYsi330f%2BtMnt8QTaLd4eueJEW7TNgOK94PmYxKSNfMGcRkWevdB3hXA9QlmX0zMPP%2BG0QR0S3V1kSKzWREEcCVokrdg1lzoWr%2FzQ0UucnXtro4ZEND37V%2F27FA27vT8kOH3hc%2FzjhZlADTEKyYwFd5E1B4gkRTxF8JdC7oVfgKT%2BSLcXwf546boNa%2BxNB8616pDAwGGZr0smDLKMgPl2o289RmyykFSvR31mAQ7HiIrte%2BP%2FPOquoNE9iMORPfVR3a4kO8zqLoEKweppd9j6zx8X4AnF3Bq3yZeK105xhWuC%2FNGJuISPJYFBT3KsiGFOFV%2Bk%2FLamOt6paZdPpUdIlUpsaEpbazhr6y8JsauaI6KYMfUU2ApJZ6UWjTcAmZ1ZRmICQABNhj3djoDgq8Li15U%2FOhu8OXCZ5PEZOGzjZH7AFWM0a%2FDMrrqx%2BGLjIwZAr3lHokl63dik1wrOMnXrWFCpBYfIhuoNJxjV2ixY6j3zSoui3FGC5nEMJddejxbPfCd%2FOyGeW%2FFqt8vpJBXPCUxtuTAyoHSWt4tiIhjk%2BqKufMcAwwPXpvAY6pgHW9FoNRFINBj%2FIAuCOREYKOuRXJ83VvEp%2BkVT91ZAE8ceE2qjj%2FbZdhaq5nG7d86n2T0GhBpTrQUgpHOoSzVAm4kNE%2Bwb5ujxSMiCr%2FBCEtYW8HWDmgtbtBdJTNW99ffNFI%2B%2Fytj8eKOaD6Sl2tQtKbs26S6t5cJ5wDb4kvRHYjy%2BN2hxC1RuS9x4x3TBZ02GUof1yQIkq0TRwRR4mgZjG%2FcEVZnd2&X-Amz-Signature=dcea2a89073cdcb243c345bc4b1482122e722f7b66f5e9a9ac3a1398e09e88ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZW572V6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID98wT9ZmEU3AYiROu598hxtjKmW4VWcLDrVn5BDAnYDAiBmByRNTsCOLLvqE2MZs0cQfNsPJeMS9O7GzpnE2FD0IiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDPQG%2BL4Fy2OGFD6tKtwDbrIFe0AeP6UiWvo9vdAalnFELtwh1SHcLD3UMk0egfzZd7EpxPDxHiDBBwuYkQxFjQBrUklYShLYsi330f%2BtMnt8QTaLd4eueJEW7TNgOK94PmYxKSNfMGcRkWevdB3hXA9QlmX0zMPP%2BG0QR0S3V1kSKzWREEcCVokrdg1lzoWr%2FzQ0UucnXtro4ZEND37V%2F27FA27vT8kOH3hc%2FzjhZlADTEKyYwFd5E1B4gkRTxF8JdC7oVfgKT%2BSLcXwf546boNa%2BxNB8616pDAwGGZr0smDLKMgPl2o289RmyykFSvR31mAQ7HiIrte%2BP%2FPOquoNE9iMORPfVR3a4kO8zqLoEKweppd9j6zx8X4AnF3Bq3yZeK105xhWuC%2FNGJuISPJYFBT3KsiGFOFV%2Bk%2FLamOt6paZdPpUdIlUpsaEpbazhr6y8JsauaI6KYMfUU2ApJZ6UWjTcAmZ1ZRmICQABNhj3djoDgq8Li15U%2FOhu8OXCZ5PEZOGzjZH7AFWM0a%2FDMrrqx%2BGLjIwZAr3lHokl63dik1wrOMnXrWFCpBYfIhuoNJxjV2ixY6j3zSoui3FGC5nEMJddejxbPfCd%2FOyGeW%2FFqt8vpJBXPCUxtuTAyoHSWt4tiIhjk%2BqKufMcAwwPXpvAY6pgHW9FoNRFINBj%2FIAuCOREYKOuRXJ83VvEp%2BkVT91ZAE8ceE2qjj%2FbZdhaq5nG7d86n2T0GhBpTrQUgpHOoSzVAm4kNE%2Bwb5ujxSMiCr%2FBCEtYW8HWDmgtbtBdJTNW99ffNFI%2B%2Fytj8eKOaD6Sl2tQtKbs26S6t5cJ5wDb4kvRHYjy%2BN2hxC1RuS9x4x3TBZ02GUof1yQIkq0TRwRR4mgZjG%2FcEVZnd2&X-Amz-Signature=50bfa410742d149eb517657d1c5e8c4dc4e967b1c168ffa27d87383a7d9fa60b&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUIPIHUL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3mWS72Wn%2Fs4FMwORSn3rXFWXktdDKHGfd8VNQBdyr9QIhAOA60ajLOl%2Bzjn1CCQcbTvAHa9GasYKuKrZNFct901ieKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzs2OORofTWIjLK1koq3ANI8CLidk7RsWrmf3WJa4BmODhu52Q4VXk5xnBcXkSN1D3sXrD%2FMLQdJBA1Zkm%2FUxt3i%2F7jqlzrwxnVay48LQiUox9deyG4GwnCVCKgU1CnuVy0qgiTRpV9k6B5%2FqLso3kMBXH7aGDETrYQ8kERYo4TDfBv7an13%2FHl1OKY82hLixkpJ12XusFdQgst%2BqqkxBZK7m3Bso9Ozc99xo3A6nzDymz9lWs5Itp3Ca65jZGpefFCNWTKcCqRND1H%2BAd%2Bd1dRisUkF4ia96ue%2FUsfte7Z7JOQVDvLkQwDIFeFqWFTbr6TPuJSP9ZsRbd6y1xscgAlof1uEqZYGKC1BJr%2F8vL4WrD1W75Ms3er87BADsw3vtu22WhrKES%2B8w6gWonWueKOZC8a8zlbbovp%2FdsBCIB7JPVhHwEg8UfgzTqfsoFK2BPEgIpBlIG9pruiAo71gLGLpKuXh41uoHJ%2FAk%2BvYmpML76VQlrR9vOSdRYKqsoqV3fT0rmi5YJKZ06rvho1b0Bupqnot8DmIL%2FmCACAbdp0ELp2bjWtbD7GulgDgA0XV4hZFYPL98x5bLtEzdJHIOmLlL%2FYsSUdgeLfoSUOf%2FN2w2TI9M%2FFt2KbJ8RmBQBl23cz8oaVWye8I3ZwyTCd9em8BjqkARAZnwwdNGx0u%2FTznGUf%2FVBiiFQtIbQU7eTBwKa3r3juLL5WsgMPrzpdw8DfhPV%2FcS3kzWCTVnHfP3pNmlO5aPVwk872Bly%2FMzrY4lg9byKezCi%2BufBXsXZIGbY3c%2By7HbdkcFzF5AoPTB5vS3EJVagqYkKykFo1UpXmByKZf0a%2FR5YyhtL0eUwA7C9FcJEnakyMy4%2Fepc4Em6sEZLxHMRL%2BsPOx&X-Amz-Signature=1d1c0f62b77ceb5286f60fe3aa42a6344a9765d7d09f11d5b99699a7ea7db9f4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUIPIHUL%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3mWS72Wn%2Fs4FMwORSn3rXFWXktdDKHGfd8VNQBdyr9QIhAOA60ajLOl%2Bzjn1CCQcbTvAHa9GasYKuKrZNFct901ieKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzs2OORofTWIjLK1koq3ANI8CLidk7RsWrmf3WJa4BmODhu52Q4VXk5xnBcXkSN1D3sXrD%2FMLQdJBA1Zkm%2FUxt3i%2F7jqlzrwxnVay48LQiUox9deyG4GwnCVCKgU1CnuVy0qgiTRpV9k6B5%2FqLso3kMBXH7aGDETrYQ8kERYo4TDfBv7an13%2FHl1OKY82hLixkpJ12XusFdQgst%2BqqkxBZK7m3Bso9Ozc99xo3A6nzDymz9lWs5Itp3Ca65jZGpefFCNWTKcCqRND1H%2BAd%2Bd1dRisUkF4ia96ue%2FUsfte7Z7JOQVDvLkQwDIFeFqWFTbr6TPuJSP9ZsRbd6y1xscgAlof1uEqZYGKC1BJr%2F8vL4WrD1W75Ms3er87BADsw3vtu22WhrKES%2B8w6gWonWueKOZC8a8zlbbovp%2FdsBCIB7JPVhHwEg8UfgzTqfsoFK2BPEgIpBlIG9pruiAo71gLGLpKuXh41uoHJ%2FAk%2BvYmpML76VQlrR9vOSdRYKqsoqV3fT0rmi5YJKZ06rvho1b0Bupqnot8DmIL%2FmCACAbdp0ELp2bjWtbD7GulgDgA0XV4hZFYPL98x5bLtEzdJHIOmLlL%2FYsSUdgeLfoSUOf%2FN2w2TI9M%2FFt2KbJ8RmBQBl23cz8oaVWye8I3ZwyTCd9em8BjqkARAZnwwdNGx0u%2FTznGUf%2FVBiiFQtIbQU7eTBwKa3r3juLL5WsgMPrzpdw8DfhPV%2FcS3kzWCTVnHfP3pNmlO5aPVwk872Bly%2FMzrY4lg9byKezCi%2BufBXsXZIGbY3c%2By7HbdkcFzF5AoPTB5vS3EJVagqYkKykFo1UpXmByKZf0a%2FR5YyhtL0eUwA7C9FcJEnakyMy4%2Fepc4Em6sEZLxHMRL%2BsPOx&X-Amz-Signature=aa2d43da6c128f6ef6a6b8e3243b3a1a2d2733b52a6c25911e2603fb581a3f90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZW572V6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID98wT9ZmEU3AYiROu598hxtjKmW4VWcLDrVn5BDAnYDAiBmByRNTsCOLLvqE2MZs0cQfNsPJeMS9O7GzpnE2FD0IiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDPQG%2BL4Fy2OGFD6tKtwDbrIFe0AeP6UiWvo9vdAalnFELtwh1SHcLD3UMk0egfzZd7EpxPDxHiDBBwuYkQxFjQBrUklYShLYsi330f%2BtMnt8QTaLd4eueJEW7TNgOK94PmYxKSNfMGcRkWevdB3hXA9QlmX0zMPP%2BG0QR0S3V1kSKzWREEcCVokrdg1lzoWr%2FzQ0UucnXtro4ZEND37V%2F27FA27vT8kOH3hc%2FzjhZlADTEKyYwFd5E1B4gkRTxF8JdC7oVfgKT%2BSLcXwf546boNa%2BxNB8616pDAwGGZr0smDLKMgPl2o289RmyykFSvR31mAQ7HiIrte%2BP%2FPOquoNE9iMORPfVR3a4kO8zqLoEKweppd9j6zx8X4AnF3Bq3yZeK105xhWuC%2FNGJuISPJYFBT3KsiGFOFV%2Bk%2FLamOt6paZdPpUdIlUpsaEpbazhr6y8JsauaI6KYMfUU2ApJZ6UWjTcAmZ1ZRmICQABNhj3djoDgq8Li15U%2FOhu8OXCZ5PEZOGzjZH7AFWM0a%2FDMrrqx%2BGLjIwZAr3lHokl63dik1wrOMnXrWFCpBYfIhuoNJxjV2ixY6j3zSoui3FGC5nEMJddejxbPfCd%2FOyGeW%2FFqt8vpJBXPCUxtuTAyoHSWt4tiIhjk%2BqKufMcAwwPXpvAY6pgHW9FoNRFINBj%2FIAuCOREYKOuRXJ83VvEp%2BkVT91ZAE8ceE2qjj%2FbZdhaq5nG7d86n2T0GhBpTrQUgpHOoSzVAm4kNE%2Bwb5ujxSMiCr%2FBCEtYW8HWDmgtbtBdJTNW99ffNFI%2B%2Fytj8eKOaD6Sl2tQtKbs26S6t5cJ5wDb4kvRHYjy%2BN2hxC1RuS9x4x3TBZ02GUof1yQIkq0TRwRR4mgZjG%2FcEVZnd2&X-Amz-Signature=59eb6b26e16b82c1504d635e37d1d5e021f7fa9fcfc621320dfcc17f6c6f54d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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