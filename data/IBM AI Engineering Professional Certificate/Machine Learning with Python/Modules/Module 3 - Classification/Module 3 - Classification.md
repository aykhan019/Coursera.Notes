

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ6Z77IE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIdL2vYut3uGjZN%2FhjWRiOii3XusZiy4MyB4jem2EECAiBDR55wzYTu0wj7xtu8XkI9BncY0rcZlFjSQGNcfGnuRSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjmx1QJpgBbBc3NkMKtwDZfFO9u13US2O4jf0i8YEtF4SUtJbVJgd2uC0F6vlS4oCM9OzXssb6jBUwKFMUdVvn5CahHlJhUXhGxP6xrr7cI08IJxAZ4J3JAGLYf7QuU5FiLGRWiFfaGd5uVhQtYAMQ807iThffHQpF5vegnjcEEG8DZb%2BTXOYAXGwK8fZGClUp3FrYG1%2BnfZdjwMLQRQtLTjgQ3%2BNWISy%2Bkyj%2B3ybD3NpHCg19NoPuJ%2Fj%2B5UJj%2BkQZuFYtUlkI%2FTOCW4NaLtSM8269JDTQPSEy29krs807VfXuJi2GCAt5I2RYxj1JVAzD05d0aY%2FI8zJIE9CXWytN%2Bcd7t9quyTcwww2dDTDNAR6O3lYk2pwwOgpHSvv%2FjmV%2Bp4r8mnVIF6PKGBTt4v2SOsOQNhBtuJREWHu7EhBuDH3FCCXyRt3skkOUXTze%2F%2FwPO7Yb2RJgVSEZJ7aD1mnf%2FDLDYjn2cCYChuxkYwIDA4FHy%2BUnnMPflx8kkvh8c70iDSf4cHKuxtV%2F6EnKQ7L8dCDNi7zJcfFAycgp%2FgMpAjP5s5uW6pqddCR%2B6rLRzcf%2FIskfrlSa5T3oXF5g2dzLpcGOrZth7lS1%2FIQfQONEP6LmshHBONVSGTmJzYjimamV3uK0s9m2KqehbQwjt3%2BvAY6pgGaAMq6IQYP1e6PkeK%2B4JvjYSqRvzN7FHLLwfIEoZNxRTGtYFAvUOv%2FnpEL%2Bv6lQSbGH7aMVRhZJduXUTE7v2E4kCSCZJXLFHPZ0pFf4HtFtNPT%2FPihiJQo8TuzGg3%2FIMPgmmDRZLcpgleFJf0yqACdct9urPft35wVlvXEDzFTw19PczGZm89tsETtMyBsFwbSqYK3yWbYcUpkXzqyrWZ8%2BLDXqYBq&X-Amz-Signature=2567486c977e6985cda3cc7d258393c903f3ae320c2e26192e920ebeec28b32a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ6Z77IE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIdL2vYut3uGjZN%2FhjWRiOii3XusZiy4MyB4jem2EECAiBDR55wzYTu0wj7xtu8XkI9BncY0rcZlFjSQGNcfGnuRSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjmx1QJpgBbBc3NkMKtwDZfFO9u13US2O4jf0i8YEtF4SUtJbVJgd2uC0F6vlS4oCM9OzXssb6jBUwKFMUdVvn5CahHlJhUXhGxP6xrr7cI08IJxAZ4J3JAGLYf7QuU5FiLGRWiFfaGd5uVhQtYAMQ807iThffHQpF5vegnjcEEG8DZb%2BTXOYAXGwK8fZGClUp3FrYG1%2BnfZdjwMLQRQtLTjgQ3%2BNWISy%2Bkyj%2B3ybD3NpHCg19NoPuJ%2Fj%2B5UJj%2BkQZuFYtUlkI%2FTOCW4NaLtSM8269JDTQPSEy29krs807VfXuJi2GCAt5I2RYxj1JVAzD05d0aY%2FI8zJIE9CXWytN%2Bcd7t9quyTcwww2dDTDNAR6O3lYk2pwwOgpHSvv%2FjmV%2Bp4r8mnVIF6PKGBTt4v2SOsOQNhBtuJREWHu7EhBuDH3FCCXyRt3skkOUXTze%2F%2FwPO7Yb2RJgVSEZJ7aD1mnf%2FDLDYjn2cCYChuxkYwIDA4FHy%2BUnnMPflx8kkvh8c70iDSf4cHKuxtV%2F6EnKQ7L8dCDNi7zJcfFAycgp%2FgMpAjP5s5uW6pqddCR%2B6rLRzcf%2FIskfrlSa5T3oXF5g2dzLpcGOrZth7lS1%2FIQfQONEP6LmshHBONVSGTmJzYjimamV3uK0s9m2KqehbQwjt3%2BvAY6pgGaAMq6IQYP1e6PkeK%2B4JvjYSqRvzN7FHLLwfIEoZNxRTGtYFAvUOv%2FnpEL%2Bv6lQSbGH7aMVRhZJduXUTE7v2E4kCSCZJXLFHPZ0pFf4HtFtNPT%2FPihiJQo8TuzGg3%2FIMPgmmDRZLcpgleFJf0yqACdct9urPft35wVlvXEDzFTw19PczGZm89tsETtMyBsFwbSqYK3yWbYcUpkXzqyrWZ8%2BLDXqYBq&X-Amz-Signature=c4aa8b1b0a08cd45e94debed7ef12f49a7a4ae3789e3b4f9f35c8cb1243055d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ6Z77IE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIdL2vYut3uGjZN%2FhjWRiOii3XusZiy4MyB4jem2EECAiBDR55wzYTu0wj7xtu8XkI9BncY0rcZlFjSQGNcfGnuRSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjmx1QJpgBbBc3NkMKtwDZfFO9u13US2O4jf0i8YEtF4SUtJbVJgd2uC0F6vlS4oCM9OzXssb6jBUwKFMUdVvn5CahHlJhUXhGxP6xrr7cI08IJxAZ4J3JAGLYf7QuU5FiLGRWiFfaGd5uVhQtYAMQ807iThffHQpF5vegnjcEEG8DZb%2BTXOYAXGwK8fZGClUp3FrYG1%2BnfZdjwMLQRQtLTjgQ3%2BNWISy%2Bkyj%2B3ybD3NpHCg19NoPuJ%2Fj%2B5UJj%2BkQZuFYtUlkI%2FTOCW4NaLtSM8269JDTQPSEy29krs807VfXuJi2GCAt5I2RYxj1JVAzD05d0aY%2FI8zJIE9CXWytN%2Bcd7t9quyTcwww2dDTDNAR6O3lYk2pwwOgpHSvv%2FjmV%2Bp4r8mnVIF6PKGBTt4v2SOsOQNhBtuJREWHu7EhBuDH3FCCXyRt3skkOUXTze%2F%2FwPO7Yb2RJgVSEZJ7aD1mnf%2FDLDYjn2cCYChuxkYwIDA4FHy%2BUnnMPflx8kkvh8c70iDSf4cHKuxtV%2F6EnKQ7L8dCDNi7zJcfFAycgp%2FgMpAjP5s5uW6pqddCR%2B6rLRzcf%2FIskfrlSa5T3oXF5g2dzLpcGOrZth7lS1%2FIQfQONEP6LmshHBONVSGTmJzYjimamV3uK0s9m2KqehbQwjt3%2BvAY6pgGaAMq6IQYP1e6PkeK%2B4JvjYSqRvzN7FHLLwfIEoZNxRTGtYFAvUOv%2FnpEL%2Bv6lQSbGH7aMVRhZJduXUTE7v2E4kCSCZJXLFHPZ0pFf4HtFtNPT%2FPihiJQo8TuzGg3%2FIMPgmmDRZLcpgleFJf0yqACdct9urPft35wVlvXEDzFTw19PczGZm89tsETtMyBsFwbSqYK3yWbYcUpkXzqyrWZ8%2BLDXqYBq&X-Amz-Signature=96b584e979feeb68a05f0ca53f07ce64b83f04f2c79bac718d5832adc94d4b8c&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP3AFG2A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMOaMdERrt4%2FlHEUGgukKa39IigXqyXZV8zwYNeAaquAIhANoNziT3UXveEIgUbsYY%2BjjRqO7FVNcQERsNVOJei5ClKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxw%2BGYZSgnqnUnMlcQq3ANHSPAzo2K67r7owA1nrRfZ969DSPOI7FjI8m7ffSaJqt24xWXcZ0t97NgojqnSya%2B8hV9ucrqZYolFE6BqwuNv3gU1OtPqNdr58VJoptxXSYi6%2BAElPBO6tuJKVIPYSLogo6%2BOBpYLELl%2F2ywPxv70SFCstVM%2BMEspHwD7767bhoQQxcs0qjo9TjbUN5WfFmWhlU7%2BNHJtectU7pGyHP%2BPutYSuG2d3vHx2lRvtr78CIMxGZMLbMbLyXwcVBMYeIT2%2Ftr6uKh1DjN6JvMKBBuzcHVJnSjQmWXyLEUXBhUkr6tVnqJz4a9g880ywHMW8ewhrhC%2B3PGhXQqdd7FEEwj%2FX3Ta3i4Ed6K%2Bfpej84rOm5Jwn98nCD%2FD0jeX%2F%2FSqC6eB5%2BLZpCx1FKnGKtM%2BaaG%2FvZuUZmOXOCKGWdGRsMl3SQcNYHLJlmxAEBYaV3dq1GtQkmngmF7wX%2FrIxTP%2BKV1zsHF6pvWq19i%2F8Cm9ebvbYtaQXfn3fZaoL5760%2BdqDbqSWSPvW4WTJjSL5viOgU%2Fk%2BXb8d9Fr5EX0Dg1lcq2PB6jBUHj8f2y%2FXRdi7NsQMDL0IfFK4sK3zeqRU4x3hNe1gfuSGchxWX6VzTRhvFLHjTggZgM2dtypq6ErWzC92v68BjqkAQ2nrL1JhXVfnQiNBX37ZCNRkqO1Ide8CP93ra245XyaIofS6zUH5wJmQCrcPshLTJnQshvTHRSBouaJdL5g1hmm2jxTSVPZtrun2D%2BOGpbQTj0FV%2FL32HVTFiCrBxb%2FKtRXWObbI4RadnPx3ALcTrds%2BDeh2Xlf%2BpOWqf0Gb9%2BDf7I58McJ%2BaJznVHBvzWIsyydjdzjWxV02SuH32ph2bSvKUXK&X-Amz-Signature=7f34f269e0468ce45904d558621278921aab08e7e9c640a172c3e5ccd303adc9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP3AFG2A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMOaMdERrt4%2FlHEUGgukKa39IigXqyXZV8zwYNeAaquAIhANoNziT3UXveEIgUbsYY%2BjjRqO7FVNcQERsNVOJei5ClKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxw%2BGYZSgnqnUnMlcQq3ANHSPAzo2K67r7owA1nrRfZ969DSPOI7FjI8m7ffSaJqt24xWXcZ0t97NgojqnSya%2B8hV9ucrqZYolFE6BqwuNv3gU1OtPqNdr58VJoptxXSYi6%2BAElPBO6tuJKVIPYSLogo6%2BOBpYLELl%2F2ywPxv70SFCstVM%2BMEspHwD7767bhoQQxcs0qjo9TjbUN5WfFmWhlU7%2BNHJtectU7pGyHP%2BPutYSuG2d3vHx2lRvtr78CIMxGZMLbMbLyXwcVBMYeIT2%2Ftr6uKh1DjN6JvMKBBuzcHVJnSjQmWXyLEUXBhUkr6tVnqJz4a9g880ywHMW8ewhrhC%2B3PGhXQqdd7FEEwj%2FX3Ta3i4Ed6K%2Bfpej84rOm5Jwn98nCD%2FD0jeX%2F%2FSqC6eB5%2BLZpCx1FKnGKtM%2BaaG%2FvZuUZmOXOCKGWdGRsMl3SQcNYHLJlmxAEBYaV3dq1GtQkmngmF7wX%2FrIxTP%2BKV1zsHF6pvWq19i%2F8Cm9ebvbYtaQXfn3fZaoL5760%2BdqDbqSWSPvW4WTJjSL5viOgU%2Fk%2BXb8d9Fr5EX0Dg1lcq2PB6jBUHj8f2y%2FXRdi7NsQMDL0IfFK4sK3zeqRU4x3hNe1gfuSGchxWX6VzTRhvFLHjTggZgM2dtypq6ErWzC92v68BjqkAQ2nrL1JhXVfnQiNBX37ZCNRkqO1Ide8CP93ra245XyaIofS6zUH5wJmQCrcPshLTJnQshvTHRSBouaJdL5g1hmm2jxTSVPZtrun2D%2BOGpbQTj0FV%2FL32HVTFiCrBxb%2FKtRXWObbI4RadnPx3ALcTrds%2BDeh2Xlf%2BpOWqf0Gb9%2BDf7I58McJ%2BaJznVHBvzWIsyydjdzjWxV02SuH32ph2bSvKUXK&X-Amz-Signature=fb379f21a687cf16fa3d293abb845d0c1b131d411fe6495e36c970bf7fac8811&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ6Z77IE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIdL2vYut3uGjZN%2FhjWRiOii3XusZiy4MyB4jem2EECAiBDR55wzYTu0wj7xtu8XkI9BncY0rcZlFjSQGNcfGnuRSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjmx1QJpgBbBc3NkMKtwDZfFO9u13US2O4jf0i8YEtF4SUtJbVJgd2uC0F6vlS4oCM9OzXssb6jBUwKFMUdVvn5CahHlJhUXhGxP6xrr7cI08IJxAZ4J3JAGLYf7QuU5FiLGRWiFfaGd5uVhQtYAMQ807iThffHQpF5vegnjcEEG8DZb%2BTXOYAXGwK8fZGClUp3FrYG1%2BnfZdjwMLQRQtLTjgQ3%2BNWISy%2Bkyj%2B3ybD3NpHCg19NoPuJ%2Fj%2B5UJj%2BkQZuFYtUlkI%2FTOCW4NaLtSM8269JDTQPSEy29krs807VfXuJi2GCAt5I2RYxj1JVAzD05d0aY%2FI8zJIE9CXWytN%2Bcd7t9quyTcwww2dDTDNAR6O3lYk2pwwOgpHSvv%2FjmV%2Bp4r8mnVIF6PKGBTt4v2SOsOQNhBtuJREWHu7EhBuDH3FCCXyRt3skkOUXTze%2F%2FwPO7Yb2RJgVSEZJ7aD1mnf%2FDLDYjn2cCYChuxkYwIDA4FHy%2BUnnMPflx8kkvh8c70iDSf4cHKuxtV%2F6EnKQ7L8dCDNi7zJcfFAycgp%2FgMpAjP5s5uW6pqddCR%2B6rLRzcf%2FIskfrlSa5T3oXF5g2dzLpcGOrZth7lS1%2FIQfQONEP6LmshHBONVSGTmJzYjimamV3uK0s9m2KqehbQwjt3%2BvAY6pgGaAMq6IQYP1e6PkeK%2B4JvjYSqRvzN7FHLLwfIEoZNxRTGtYFAvUOv%2FnpEL%2Bv6lQSbGH7aMVRhZJduXUTE7v2E4kCSCZJXLFHPZ0pFf4HtFtNPT%2FPihiJQo8TuzGg3%2FIMPgmmDRZLcpgleFJf0yqACdct9urPft35wVlvXEDzFTw19PczGZm89tsETtMyBsFwbSqYK3yWbYcUpkXzqyrWZ8%2BLDXqYBq&X-Amz-Signature=abbb9f3829b2258236cd430df0d019e3ce8d93196e293be146c093725f16fb3d&X-Amz-SignedHeaders=host&x-id=GetObject)
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