

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PG2GOAZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLDjCVeo%2BU6J8uUbeR2RdOWuWdi7gnvwBsNaR2Zy0kDwIgI5zs%2FvYKpc3Q1fKDzQe4nuLLoa%2BgIpn8JD%2BqAj7yzbgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGbktNYppah7NCbqDSrcA5FWACQBUh1tu%2Bn4BRpXxQqyFiJxd06GuEozcaf3PahTYB2ieMMalIzVNn2RGT3N2rKpJC1UBjkdyXUTQW1QOy69%2Bdq3Y%2FJPfF3gIuSf56h%2FR90vHpBnncNwfCtH%2BudaDbFdlzgkaqmZjvhVzoABbH6yPTTYr5d52soHGWdpf7SoOQe4gGHMCKNxxYRmEPI2ueNb7Oe%2B9BloCIj%2Bxl%2FmDxMAV9TnCPhuSG34Ns%2FpT5LEQLJjAHEYW3JtDHyjwnLZByz%2Bkb52zhiushYk1Hwh2NVTS2b0mWScMdpVVjnU7pCO%2Fjr2Y1kBvYtB6DZoAFAGjF%2FyzUZ9%2F0br2dAWB5JOqvZFSylCmQhuDtWzP8avjreJT%2FH1pxr2Qhi2%2F0MJK5YICLNLKuAyGN4tIGQbBwcnlzZQj3l0Dd1fD%2F48AhNiOkJRZHq%2BzrqiyYhmrRffTc%2FCso3Qgo0oyT4K21bSHun188Ybic2ETYgoLcuEQqxz4gY2POOWhxZqrCCASvS7Z5SEkOTAVt1zlxMTfX78u04MPBwhLZVsa7IpIA%2BiVUUgSI1mT2wkEo52bAtKy5AOhPJ8KhYh2K2VDeGCe%2B1KNZlK0x0tICDOVSNAUtljSL%2BdWgp%2FZRj%2Fsf8ef3bF%2BsMeMIW8%2FbwGOqUBSlQZKUPDcS7fzBDWx5hFHPqjJ52AS5VivacwxDDzveBewfjUayhBHDI9Ucdbbbqe1ZdUYedfWCgr6uAHuoytTj%2BFJINpk5wVpPj1bA3WOXxRJ0Fr7zwGX4ZpNkbsFEvUeXWfCbX5hGaUwTpAw3knN5geMUajkbxtBSNftq%2Fre7RK%2BmaQOj%2FVQjBkaXcgPjd6Fn%2Bjxbzd3bjxr8wE6IADODTf6hxB&X-Amz-Signature=dd31880143c92c083cedcf30c75d76496fafa6fd8438a0087207493833986957&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PG2GOAZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLDjCVeo%2BU6J8uUbeR2RdOWuWdi7gnvwBsNaR2Zy0kDwIgI5zs%2FvYKpc3Q1fKDzQe4nuLLoa%2BgIpn8JD%2BqAj7yzbgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGbktNYppah7NCbqDSrcA5FWACQBUh1tu%2Bn4BRpXxQqyFiJxd06GuEozcaf3PahTYB2ieMMalIzVNn2RGT3N2rKpJC1UBjkdyXUTQW1QOy69%2Bdq3Y%2FJPfF3gIuSf56h%2FR90vHpBnncNwfCtH%2BudaDbFdlzgkaqmZjvhVzoABbH6yPTTYr5d52soHGWdpf7SoOQe4gGHMCKNxxYRmEPI2ueNb7Oe%2B9BloCIj%2Bxl%2FmDxMAV9TnCPhuSG34Ns%2FpT5LEQLJjAHEYW3JtDHyjwnLZByz%2Bkb52zhiushYk1Hwh2NVTS2b0mWScMdpVVjnU7pCO%2Fjr2Y1kBvYtB6DZoAFAGjF%2FyzUZ9%2F0br2dAWB5JOqvZFSylCmQhuDtWzP8avjreJT%2FH1pxr2Qhi2%2F0MJK5YICLNLKuAyGN4tIGQbBwcnlzZQj3l0Dd1fD%2F48AhNiOkJRZHq%2BzrqiyYhmrRffTc%2FCso3Qgo0oyT4K21bSHun188Ybic2ETYgoLcuEQqxz4gY2POOWhxZqrCCASvS7Z5SEkOTAVt1zlxMTfX78u04MPBwhLZVsa7IpIA%2BiVUUgSI1mT2wkEo52bAtKy5AOhPJ8KhYh2K2VDeGCe%2B1KNZlK0x0tICDOVSNAUtljSL%2BdWgp%2FZRj%2Fsf8ef3bF%2BsMeMIW8%2FbwGOqUBSlQZKUPDcS7fzBDWx5hFHPqjJ52AS5VivacwxDDzveBewfjUayhBHDI9Ucdbbbqe1ZdUYedfWCgr6uAHuoytTj%2BFJINpk5wVpPj1bA3WOXxRJ0Fr7zwGX4ZpNkbsFEvUeXWfCbX5hGaUwTpAw3knN5geMUajkbxtBSNftq%2Fre7RK%2BmaQOj%2FVQjBkaXcgPjd6Fn%2Bjxbzd3bjxr8wE6IADODTf6hxB&X-Amz-Signature=8467e9a5668062529f90ee1f18f4f8d2b95bd1742b6d6ddbc2ad99ed3f564389&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PG2GOAZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLDjCVeo%2BU6J8uUbeR2RdOWuWdi7gnvwBsNaR2Zy0kDwIgI5zs%2FvYKpc3Q1fKDzQe4nuLLoa%2BgIpn8JD%2BqAj7yzbgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGbktNYppah7NCbqDSrcA5FWACQBUh1tu%2Bn4BRpXxQqyFiJxd06GuEozcaf3PahTYB2ieMMalIzVNn2RGT3N2rKpJC1UBjkdyXUTQW1QOy69%2Bdq3Y%2FJPfF3gIuSf56h%2FR90vHpBnncNwfCtH%2BudaDbFdlzgkaqmZjvhVzoABbH6yPTTYr5d52soHGWdpf7SoOQe4gGHMCKNxxYRmEPI2ueNb7Oe%2B9BloCIj%2Bxl%2FmDxMAV9TnCPhuSG34Ns%2FpT5LEQLJjAHEYW3JtDHyjwnLZByz%2Bkb52zhiushYk1Hwh2NVTS2b0mWScMdpVVjnU7pCO%2Fjr2Y1kBvYtB6DZoAFAGjF%2FyzUZ9%2F0br2dAWB5JOqvZFSylCmQhuDtWzP8avjreJT%2FH1pxr2Qhi2%2F0MJK5YICLNLKuAyGN4tIGQbBwcnlzZQj3l0Dd1fD%2F48AhNiOkJRZHq%2BzrqiyYhmrRffTc%2FCso3Qgo0oyT4K21bSHun188Ybic2ETYgoLcuEQqxz4gY2POOWhxZqrCCASvS7Z5SEkOTAVt1zlxMTfX78u04MPBwhLZVsa7IpIA%2BiVUUgSI1mT2wkEo52bAtKy5AOhPJ8KhYh2K2VDeGCe%2B1KNZlK0x0tICDOVSNAUtljSL%2BdWgp%2FZRj%2Fsf8ef3bF%2BsMeMIW8%2FbwGOqUBSlQZKUPDcS7fzBDWx5hFHPqjJ52AS5VivacwxDDzveBewfjUayhBHDI9Ucdbbbqe1ZdUYedfWCgr6uAHuoytTj%2BFJINpk5wVpPj1bA3WOXxRJ0Fr7zwGX4ZpNkbsFEvUeXWfCbX5hGaUwTpAw3knN5geMUajkbxtBSNftq%2Fre7RK%2BmaQOj%2FVQjBkaXcgPjd6Fn%2Bjxbzd3bjxr8wE6IADODTf6hxB&X-Amz-Signature=292a7c241496e382eff1b975fa2ba847857e08997129cca1187c4a6eb0426760&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMSUR23N%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZNeVnyKzJQttNc%2F0MjPEG2Cp0U30PcjNg1P5fsNRIyAIgCV0m1QaZDwWhRlS9VANiI6bIf8jEMN8DbfKtoTbzE%2FMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHfAgYLAivoVkkR0vircAyInl%2BWcMnMo%2FMMlaBTaF8VNdtJeGbs68zmDvDCN7U9BZalvAbPr6RvnAjUO591E5Bz4fQVk0DVX7h3uod3ye3sMOr0N6Uzc%2F6ejVy9Eh8VVa%2F8n9JeKfSQvWAQqYqNlhiLVDryzO%2F0RLbhWUoKCDtpgAov10CBb2YbYimVPcG4tCI99R9oXI1g1lrjhkRfb41T4ft%2F8uQzEcdvBzl2P6ntVrEelGHiDdqcZgFH3FBxpEaLHUblzN7ClbDRrM3vlVO5%2BcsWCvw%2F8Q4kBg1%2FeugteGt1BRX7vO%2FAyQR3Ai1j7MzjK%2FICGf022tjaQb756gwRxedziJMgDqJKgAzbrUNWG%2B0HHXrZlvLKgn8udU4KHGnLXZclGt5owf1UbyDCHKb8O4bsAi20vA%2BOsSz3foW1AgbfPjg%2Fb0Ujnp1jIo8%2FMY4ysO2afbfVE%2Fb3CjdAvo1fuAWQqHmv6A4X9UKqTs9%2FaQTai3qa1QPPotNc4KU2CyZTsE5LChYxkLAkVmGm3Gk2mFTEPW4qcKW%2FX5yzlRXCRg803SIgOKd5aUlDqOJGRgxPHEGUrhjSt%2FB%2FlU5RIiVGywigNQ5kHe7DNPoMQiGYf2JpRf8mACWwEAc3CVrgpapowmojD38zlZQdDMOe8%2FbwGOqUBALRDaDwU3KiqGcdb1mjOVaigu%2BIdvvsGS6KM2a7xuHtY%2FaXsgmLZ%2FHGgX5MGlfQm77P7GyPOKFl%2BQmW7AHyXNjS3OZEIuuGHMPENdXKLyTwc5g3WycjgNihmZxPqqJ3y19HlxMthB0%2FOE5E0N18r1V9RXM59VQ0WeoGMpPLxZjbTKyN8RP8SQ2NVCF9raJEoYVTH1H8p53xS0WTC47x77WJ6Jof%2F&X-Amz-Signature=dda1bbd9dc442e643ae7d6fec46434d74adb14294758feaa42632793d9698673&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMSUR23N%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZNeVnyKzJQttNc%2F0MjPEG2Cp0U30PcjNg1P5fsNRIyAIgCV0m1QaZDwWhRlS9VANiI6bIf8jEMN8DbfKtoTbzE%2FMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHfAgYLAivoVkkR0vircAyInl%2BWcMnMo%2FMMlaBTaF8VNdtJeGbs68zmDvDCN7U9BZalvAbPr6RvnAjUO591E5Bz4fQVk0DVX7h3uod3ye3sMOr0N6Uzc%2F6ejVy9Eh8VVa%2F8n9JeKfSQvWAQqYqNlhiLVDryzO%2F0RLbhWUoKCDtpgAov10CBb2YbYimVPcG4tCI99R9oXI1g1lrjhkRfb41T4ft%2F8uQzEcdvBzl2P6ntVrEelGHiDdqcZgFH3FBxpEaLHUblzN7ClbDRrM3vlVO5%2BcsWCvw%2F8Q4kBg1%2FeugteGt1BRX7vO%2FAyQR3Ai1j7MzjK%2FICGf022tjaQb756gwRxedziJMgDqJKgAzbrUNWG%2B0HHXrZlvLKgn8udU4KHGnLXZclGt5owf1UbyDCHKb8O4bsAi20vA%2BOsSz3foW1AgbfPjg%2Fb0Ujnp1jIo8%2FMY4ysO2afbfVE%2Fb3CjdAvo1fuAWQqHmv6A4X9UKqTs9%2FaQTai3qa1QPPotNc4KU2CyZTsE5LChYxkLAkVmGm3Gk2mFTEPW4qcKW%2FX5yzlRXCRg803SIgOKd5aUlDqOJGRgxPHEGUrhjSt%2FB%2FlU5RIiVGywigNQ5kHe7DNPoMQiGYf2JpRf8mACWwEAc3CVrgpapowmojD38zlZQdDMOe8%2FbwGOqUBALRDaDwU3KiqGcdb1mjOVaigu%2BIdvvsGS6KM2a7xuHtY%2FaXsgmLZ%2FHGgX5MGlfQm77P7GyPOKFl%2BQmW7AHyXNjS3OZEIuuGHMPENdXKLyTwc5g3WycjgNihmZxPqqJ3y19HlxMthB0%2FOE5E0N18r1V9RXM59VQ0WeoGMpPLxZjbTKyN8RP8SQ2NVCF9raJEoYVTH1H8p53xS0WTC47x77WJ6Jof%2F&X-Amz-Signature=1582e4db4d8e1fe280444050b8382e2d475c9a4851e303830f60a88f12e3e839&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PG2GOAZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLDjCVeo%2BU6J8uUbeR2RdOWuWdi7gnvwBsNaR2Zy0kDwIgI5zs%2FvYKpc3Q1fKDzQe4nuLLoa%2BgIpn8JD%2BqAj7yzbgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGbktNYppah7NCbqDSrcA5FWACQBUh1tu%2Bn4BRpXxQqyFiJxd06GuEozcaf3PahTYB2ieMMalIzVNn2RGT3N2rKpJC1UBjkdyXUTQW1QOy69%2Bdq3Y%2FJPfF3gIuSf56h%2FR90vHpBnncNwfCtH%2BudaDbFdlzgkaqmZjvhVzoABbH6yPTTYr5d52soHGWdpf7SoOQe4gGHMCKNxxYRmEPI2ueNb7Oe%2B9BloCIj%2Bxl%2FmDxMAV9TnCPhuSG34Ns%2FpT5LEQLJjAHEYW3JtDHyjwnLZByz%2Bkb52zhiushYk1Hwh2NVTS2b0mWScMdpVVjnU7pCO%2Fjr2Y1kBvYtB6DZoAFAGjF%2FyzUZ9%2F0br2dAWB5JOqvZFSylCmQhuDtWzP8avjreJT%2FH1pxr2Qhi2%2F0MJK5YICLNLKuAyGN4tIGQbBwcnlzZQj3l0Dd1fD%2F48AhNiOkJRZHq%2BzrqiyYhmrRffTc%2FCso3Qgo0oyT4K21bSHun188Ybic2ETYgoLcuEQqxz4gY2POOWhxZqrCCASvS7Z5SEkOTAVt1zlxMTfX78u04MPBwhLZVsa7IpIA%2BiVUUgSI1mT2wkEo52bAtKy5AOhPJ8KhYh2K2VDeGCe%2B1KNZlK0x0tICDOVSNAUtljSL%2BdWgp%2FZRj%2Fsf8ef3bF%2BsMeMIW8%2FbwGOqUBSlQZKUPDcS7fzBDWx5hFHPqjJ52AS5VivacwxDDzveBewfjUayhBHDI9Ucdbbbqe1ZdUYedfWCgr6uAHuoytTj%2BFJINpk5wVpPj1bA3WOXxRJ0Fr7zwGX4ZpNkbsFEvUeXWfCbX5hGaUwTpAw3knN5geMUajkbxtBSNftq%2Fre7RK%2BmaQOj%2FVQjBkaXcgPjd6Fn%2Bjxbzd3bjxr8wE6IADODTf6hxB&X-Amz-Signature=dce00e10b321cf1721bea1bfe07ed33ed3002afbad2fc1c2bec7b41967b99067&X-Amz-SignedHeaders=host&x-id=GetObject)
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