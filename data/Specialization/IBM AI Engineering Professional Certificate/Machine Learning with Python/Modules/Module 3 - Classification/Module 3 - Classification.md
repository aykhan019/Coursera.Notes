

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDSPE7W%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHNxOG9clpsMPKp59zh%2FbLglyJQ6uu9ypP7%2BxE00vcOAiBMzCQf7JWwf77g%2F798YncvV7zLrt27U2CoLEGsXP4bYyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoKzmBgYbeqUUSplzKtwDkfZT%2FayCGr8HiLaUX%2FeUHwofoIFiK%2B276jD0dkwdVAoRn6YItS92uSzF%2F2jtibDWxqC%2BFHdLXQR1276A5L1R6jDlPr2%2F0EGGce%2Fm7XKi6GmaEJ4Z9PMgq09qWF0X%2ByT%2FrEhJVmNHOFvj%2F0yYC5I5Q1CGXZT346MuWr4ApPQSq35E3MerLGDA8%2BsxFjV8eezS72458Rw%2FhXm3H66vq5M6A52dM0NgPTYcSxjpD1BeRH5hoIZvTWOotFB3pZTICfUHKkg2ApJmF5YfHfRZgdyJYES7hnBGYIpRIZ3E8%2BKo7iqpXUpraCTpvWUCrdK54N94SRia03K%2BbKeSESHlA%2B8Eke5tuqdlcpSuslheNPXf60bdvkXXutGj7XdzyjNCKgzX8DY5Fh4yacrnAMH3R%2FMqPq%2FnXtt8bW%2BMNXv%2B22e7OopztHVHoo197dR0eSTvmGMy%2FXAuMWtzWwofEihWhHnYYLWoiCdj4EzcF%2BKD3xxmSao8hgg%2BqDdHCdatw5xpJ3sCW5oEk%2B6bDBJxSQxDj8vsD9Wexyp9ErtespX8yf3Htk%2BNPGm%2BZT3OVDLDBaLNLY8CVWwf7o65wNOJgOxcKkdeg9f47MAre%2BOSvzdQhaWAXX6XPQYvufU3kOvfvTow19jpvAY6pgHzm0VP26gC0pDYeMd2BVdwp6CQ5U7xcld%2BzWW8htmuwOBfbGIgtH05MzzZsN%2Fff8QsoJktrHdqfdeHibYRmuFOYwyOCJr3Qryw9cpxPM%2FmsV1DbXoGnR69HZH6SCCoM0xytKEY%2BbDCAmDELIyiTuY1NpRwaYYYf2AE8gJPuPDU%2FqaDSLp3X7%2FuCKehdX1uNuz2BfdGrQ%2FD81RvGhlz%2Fc%2F2X%2FBe4msY&X-Amz-Signature=7b0e8f774a5fd1a3f1666800518b7646f25e38444299d467972a7c40a448237e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDSPE7W%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHNxOG9clpsMPKp59zh%2FbLglyJQ6uu9ypP7%2BxE00vcOAiBMzCQf7JWwf77g%2F798YncvV7zLrt27U2CoLEGsXP4bYyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoKzmBgYbeqUUSplzKtwDkfZT%2FayCGr8HiLaUX%2FeUHwofoIFiK%2B276jD0dkwdVAoRn6YItS92uSzF%2F2jtibDWxqC%2BFHdLXQR1276A5L1R6jDlPr2%2F0EGGce%2Fm7XKi6GmaEJ4Z9PMgq09qWF0X%2ByT%2FrEhJVmNHOFvj%2F0yYC5I5Q1CGXZT346MuWr4ApPQSq35E3MerLGDA8%2BsxFjV8eezS72458Rw%2FhXm3H66vq5M6A52dM0NgPTYcSxjpD1BeRH5hoIZvTWOotFB3pZTICfUHKkg2ApJmF5YfHfRZgdyJYES7hnBGYIpRIZ3E8%2BKo7iqpXUpraCTpvWUCrdK54N94SRia03K%2BbKeSESHlA%2B8Eke5tuqdlcpSuslheNPXf60bdvkXXutGj7XdzyjNCKgzX8DY5Fh4yacrnAMH3R%2FMqPq%2FnXtt8bW%2BMNXv%2B22e7OopztHVHoo197dR0eSTvmGMy%2FXAuMWtzWwofEihWhHnYYLWoiCdj4EzcF%2BKD3xxmSao8hgg%2BqDdHCdatw5xpJ3sCW5oEk%2B6bDBJxSQxDj8vsD9Wexyp9ErtespX8yf3Htk%2BNPGm%2BZT3OVDLDBaLNLY8CVWwf7o65wNOJgOxcKkdeg9f47MAre%2BOSvzdQhaWAXX6XPQYvufU3kOvfvTow19jpvAY6pgHzm0VP26gC0pDYeMd2BVdwp6CQ5U7xcld%2BzWW8htmuwOBfbGIgtH05MzzZsN%2Fff8QsoJktrHdqfdeHibYRmuFOYwyOCJr3Qryw9cpxPM%2FmsV1DbXoGnR69HZH6SCCoM0xytKEY%2BbDCAmDELIyiTuY1NpRwaYYYf2AE8gJPuPDU%2FqaDSLp3X7%2FuCKehdX1uNuz2BfdGrQ%2FD81RvGhlz%2Fc%2F2X%2FBe4msY&X-Amz-Signature=272a257f6f52e2677ae692f249bc8a9c11a4fb72d4ec7cef1dadce7b4ce4d4a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDSPE7W%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHNxOG9clpsMPKp59zh%2FbLglyJQ6uu9ypP7%2BxE00vcOAiBMzCQf7JWwf77g%2F798YncvV7zLrt27U2CoLEGsXP4bYyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoKzmBgYbeqUUSplzKtwDkfZT%2FayCGr8HiLaUX%2FeUHwofoIFiK%2B276jD0dkwdVAoRn6YItS92uSzF%2F2jtibDWxqC%2BFHdLXQR1276A5L1R6jDlPr2%2F0EGGce%2Fm7XKi6GmaEJ4Z9PMgq09qWF0X%2ByT%2FrEhJVmNHOFvj%2F0yYC5I5Q1CGXZT346MuWr4ApPQSq35E3MerLGDA8%2BsxFjV8eezS72458Rw%2FhXm3H66vq5M6A52dM0NgPTYcSxjpD1BeRH5hoIZvTWOotFB3pZTICfUHKkg2ApJmF5YfHfRZgdyJYES7hnBGYIpRIZ3E8%2BKo7iqpXUpraCTpvWUCrdK54N94SRia03K%2BbKeSESHlA%2B8Eke5tuqdlcpSuslheNPXf60bdvkXXutGj7XdzyjNCKgzX8DY5Fh4yacrnAMH3R%2FMqPq%2FnXtt8bW%2BMNXv%2B22e7OopztHVHoo197dR0eSTvmGMy%2FXAuMWtzWwofEihWhHnYYLWoiCdj4EzcF%2BKD3xxmSao8hgg%2BqDdHCdatw5xpJ3sCW5oEk%2B6bDBJxSQxDj8vsD9Wexyp9ErtespX8yf3Htk%2BNPGm%2BZT3OVDLDBaLNLY8CVWwf7o65wNOJgOxcKkdeg9f47MAre%2BOSvzdQhaWAXX6XPQYvufU3kOvfvTow19jpvAY6pgHzm0VP26gC0pDYeMd2BVdwp6CQ5U7xcld%2BzWW8htmuwOBfbGIgtH05MzzZsN%2Fff8QsoJktrHdqfdeHibYRmuFOYwyOCJr3Qryw9cpxPM%2FmsV1DbXoGnR69HZH6SCCoM0xytKEY%2BbDCAmDELIyiTuY1NpRwaYYYf2AE8gJPuPDU%2FqaDSLp3X7%2FuCKehdX1uNuz2BfdGrQ%2FD81RvGhlz%2Fc%2F2X%2FBe4msY&X-Amz-Signature=3136f7ad40cb7f7abb8704033777cf8e7b6daf24739ac98532420ae70f5efe91&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVRRFTWI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHo%2FgJ%2BoVprT7AUxytywoNaDYRCeW2JQ5WlO7sEdEi60AiEAkGPQUCEa9wVEBHYCUxyZMJgBB9KoRNCMOXmTg8hkGywqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjagPCKXjBy5Q7eGyrcA5w6R9n955ntDF%2BgXAwzaWoMLyataouEMceTBrznxc3IoX%2FYC57D%2BmAVqaj2OFh9%2FRh%2B%2BQAc%2FYKYrWxvyKUIlke8zIz0j74y0H2qSF5du8jiGXQPdtMtj8QReQIPgdI27cbkjGeKuFAp%2FEwcizpzogA%2BkoYt4JrEaI6nti%2F9Fp96sCdmlDtgu0hPPAnpZNJG1ByvUU49i4KP%2BZ7NITk%2FgHaMJn6yprBzoogLDIR2GfVHvx44acJw8pJ5GyGdC%2Fn356e8auMxQDjIYGZGDmrTGH%2For03J4JAo3akaDLEkOevRcDHzN0NYI5MHlqfSIfSO1P6XZmKmnYgVIU4deEhfiy7ye43HK9uC6GO2ZHT%2FjSI9%2F3MTn1buBm7wRnRdZck75oqCyskX6GJDlsw0095OECOBJSEG74Bs6hePrdrsAK6ElESXu9UH9MkLbguYKtnb8lhCLp6itU%2BIQvw3IfWUN2auYpqZwHQEuhOZd%2Bl9wxOEDvH9RsYJHvgi2jX4exH6xK4CTfjb4L5DTf4ks0smXV4jIqpjzEV78tBdJdFtLIm6y65sT2dBuSC13TjB7mn8rzl%2FpwdMEjvh0%2BI4lwEoUlPuEL%2F5Z76QrhSpXYonCEHXMdGDEF84SGJXNR4oMOLY6bwGOqUBDRikgJ7aLnSYJOzV0HioLlU6SgLP3OOBD0rkF18HBYyqraekr0czvlGW%2BpT0U4mgWt5%2BxWoP64Jqz09KycKSEjeM3DLvTiaHtfKp84xw1vc13%2FRWl1AnfyF1mcoI4Eqc3IYS%2FkQVKuS3mELJNe0PrsRx0aI9kFaOUMo%2Fp%2FtnC7EH%2F8t9WiYN7b%2FwmhFqmpt%2BQuO4FMoHbph%2F90C85X6xaWEt7VVq&X-Amz-Signature=504d56f68c5098e30ff78d88a948deed2721be8dac2377f0bf3b2592646a8538&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVRRFTWI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHo%2FgJ%2BoVprT7AUxytywoNaDYRCeW2JQ5WlO7sEdEi60AiEAkGPQUCEa9wVEBHYCUxyZMJgBB9KoRNCMOXmTg8hkGywqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMjagPCKXjBy5Q7eGyrcA5w6R9n955ntDF%2BgXAwzaWoMLyataouEMceTBrznxc3IoX%2FYC57D%2BmAVqaj2OFh9%2FRh%2B%2BQAc%2FYKYrWxvyKUIlke8zIz0j74y0H2qSF5du8jiGXQPdtMtj8QReQIPgdI27cbkjGeKuFAp%2FEwcizpzogA%2BkoYt4JrEaI6nti%2F9Fp96sCdmlDtgu0hPPAnpZNJG1ByvUU49i4KP%2BZ7NITk%2FgHaMJn6yprBzoogLDIR2GfVHvx44acJw8pJ5GyGdC%2Fn356e8auMxQDjIYGZGDmrTGH%2For03J4JAo3akaDLEkOevRcDHzN0NYI5MHlqfSIfSO1P6XZmKmnYgVIU4deEhfiy7ye43HK9uC6GO2ZHT%2FjSI9%2F3MTn1buBm7wRnRdZck75oqCyskX6GJDlsw0095OECOBJSEG74Bs6hePrdrsAK6ElESXu9UH9MkLbguYKtnb8lhCLp6itU%2BIQvw3IfWUN2auYpqZwHQEuhOZd%2Bl9wxOEDvH9RsYJHvgi2jX4exH6xK4CTfjb4L5DTf4ks0smXV4jIqpjzEV78tBdJdFtLIm6y65sT2dBuSC13TjB7mn8rzl%2FpwdMEjvh0%2BI4lwEoUlPuEL%2F5Z76QrhSpXYonCEHXMdGDEF84SGJXNR4oMOLY6bwGOqUBDRikgJ7aLnSYJOzV0HioLlU6SgLP3OOBD0rkF18HBYyqraekr0czvlGW%2BpT0U4mgWt5%2BxWoP64Jqz09KycKSEjeM3DLvTiaHtfKp84xw1vc13%2FRWl1AnfyF1mcoI4Eqc3IYS%2FkQVKuS3mELJNe0PrsRx0aI9kFaOUMo%2Fp%2FtnC7EH%2F8t9WiYN7b%2FwmhFqmpt%2BQuO4FMoHbph%2F90C85X6xaWEt7VVq&X-Amz-Signature=3af9f2da1308311145968fc31752383b28fdd48f1e71e6605c9f60376176d801&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDSPE7W%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHNxOG9clpsMPKp59zh%2FbLglyJQ6uu9ypP7%2BxE00vcOAiBMzCQf7JWwf77g%2F798YncvV7zLrt27U2CoLEGsXP4bYyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoKzmBgYbeqUUSplzKtwDkfZT%2FayCGr8HiLaUX%2FeUHwofoIFiK%2B276jD0dkwdVAoRn6YItS92uSzF%2F2jtibDWxqC%2BFHdLXQR1276A5L1R6jDlPr2%2F0EGGce%2Fm7XKi6GmaEJ4Z9PMgq09qWF0X%2ByT%2FrEhJVmNHOFvj%2F0yYC5I5Q1CGXZT346MuWr4ApPQSq35E3MerLGDA8%2BsxFjV8eezS72458Rw%2FhXm3H66vq5M6A52dM0NgPTYcSxjpD1BeRH5hoIZvTWOotFB3pZTICfUHKkg2ApJmF5YfHfRZgdyJYES7hnBGYIpRIZ3E8%2BKo7iqpXUpraCTpvWUCrdK54N94SRia03K%2BbKeSESHlA%2B8Eke5tuqdlcpSuslheNPXf60bdvkXXutGj7XdzyjNCKgzX8DY5Fh4yacrnAMH3R%2FMqPq%2FnXtt8bW%2BMNXv%2B22e7OopztHVHoo197dR0eSTvmGMy%2FXAuMWtzWwofEihWhHnYYLWoiCdj4EzcF%2BKD3xxmSao8hgg%2BqDdHCdatw5xpJ3sCW5oEk%2B6bDBJxSQxDj8vsD9Wexyp9ErtespX8yf3Htk%2BNPGm%2BZT3OVDLDBaLNLY8CVWwf7o65wNOJgOxcKkdeg9f47MAre%2BOSvzdQhaWAXX6XPQYvufU3kOvfvTow19jpvAY6pgHzm0VP26gC0pDYeMd2BVdwp6CQ5U7xcld%2BzWW8htmuwOBfbGIgtH05MzzZsN%2Fff8QsoJktrHdqfdeHibYRmuFOYwyOCJr3Qryw9cpxPM%2FmsV1DbXoGnR69HZH6SCCoM0xytKEY%2BbDCAmDELIyiTuY1NpRwaYYYf2AE8gJPuPDU%2FqaDSLp3X7%2FuCKehdX1uNuz2BfdGrQ%2FD81RvGhlz%2Fc%2F2X%2FBe4msY&X-Amz-Signature=ce48342ac57822f56bb91242c50c75ad03c71a682df2d5b18a44b6dccffd4c1b&X-Amz-SignedHeaders=host&x-id=GetObject)
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