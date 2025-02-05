

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T76DTWY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCID7htflT1ewhayUgoVueEJ2IB%2F1B8MR5556nlsFY7G2HAiEAhQHsKiQV8qMY2JnVgimSS8eNz964MMY%2Fb%2BdWbWc2vWUq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDFaikPSO%2BfvwZF%2FTwyrcA1OHjyI8yYv3DAn1Wg93Q0D31IyyvVWJNo1hxSa9Ct9ssCSuQFY%2BUHbPtg0QeHcBzjU7Q2v%2FhydssRIc7nqfZ94v%2Fgq6p9TmqnMHOEHGUEeUdCVeol%2BiKRwkqtcRTjH0pwTVXWMjPYtOVsH9vnMOf%2FUu0vdBItl6LlGLC5L0Gle5HF90iNtq9GJvlXTboeYhmQxtCP0DlQ3%2BKv5TAE%2FOW9W0Ji9EInPGsvXonvkVNwg5lBgxSLogioSN4gIYFXsqwOGjb3J6KMSjD91oK2R1BhN7D1diJU5scRdvFSlMiYSQBQzlngOJZ1lNGDCOn55CGF8LGXZ3ifqKsSIYHLVJYXUJ147sym51sTipsj5yIbDOmpaIGfZHIylks4povTS4IKGJNYJabPcJhCXmxXT8ckgOSQ42%2FkLJ%2BoTqrMkEIh6aA%2Brin4RiOcTUwMsIudTYKXcedNwigBraAVK4JJ24BHCXr6TFx%2F3t%2BKT4pgOZ25NDQZ2HqMMvI2ZPGWO%2BVPuq7jeOAkQSR0nMDqPeuLDt2akn2xBePA2eDKB7r%2BD2DWFOAcL0IlPYeEDThRT8BUZaUXZdxjwK8QF7NGBboYv3s%2BWJruXAyE4Ki2UsbBGUhUpxUv4ylFMcPotOajsXMMGdjr0GOqUBxUd7E9G679h9FHVARagQbOJVqHgmRhzoPzUdTdpz56WjJcaL8va3eRnhejVbL3waBdC4GTkxbm8YuzV5yg6My9oQ5hAbU3eAjcw9RLXY2Ha3FQsyLWWgZbAY0Ekmc7Q3%2BMkDezxtOGuNtJVuTtSDZXhwzvty4RWuIVii1t3gRMjIdyIUIxKHIq%2Bnw79%2BUEw7XVSlOUK2w8C2MA9mhtK42%2Fu5pX%2BU&X-Amz-Signature=d77d2bfd5cb4162b503a2ae0708c9d4aee14742bc41c24833b5faa1ade5fec10&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T76DTWY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCID7htflT1ewhayUgoVueEJ2IB%2F1B8MR5556nlsFY7G2HAiEAhQHsKiQV8qMY2JnVgimSS8eNz964MMY%2Fb%2BdWbWc2vWUq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDFaikPSO%2BfvwZF%2FTwyrcA1OHjyI8yYv3DAn1Wg93Q0D31IyyvVWJNo1hxSa9Ct9ssCSuQFY%2BUHbPtg0QeHcBzjU7Q2v%2FhydssRIc7nqfZ94v%2Fgq6p9TmqnMHOEHGUEeUdCVeol%2BiKRwkqtcRTjH0pwTVXWMjPYtOVsH9vnMOf%2FUu0vdBItl6LlGLC5L0Gle5HF90iNtq9GJvlXTboeYhmQxtCP0DlQ3%2BKv5TAE%2FOW9W0Ji9EInPGsvXonvkVNwg5lBgxSLogioSN4gIYFXsqwOGjb3J6KMSjD91oK2R1BhN7D1diJU5scRdvFSlMiYSQBQzlngOJZ1lNGDCOn55CGF8LGXZ3ifqKsSIYHLVJYXUJ147sym51sTipsj5yIbDOmpaIGfZHIylks4povTS4IKGJNYJabPcJhCXmxXT8ckgOSQ42%2FkLJ%2BoTqrMkEIh6aA%2Brin4RiOcTUwMsIudTYKXcedNwigBraAVK4JJ24BHCXr6TFx%2F3t%2BKT4pgOZ25NDQZ2HqMMvI2ZPGWO%2BVPuq7jeOAkQSR0nMDqPeuLDt2akn2xBePA2eDKB7r%2BD2DWFOAcL0IlPYeEDThRT8BUZaUXZdxjwK8QF7NGBboYv3s%2BWJruXAyE4Ki2UsbBGUhUpxUv4ylFMcPotOajsXMMGdjr0GOqUBxUd7E9G679h9FHVARagQbOJVqHgmRhzoPzUdTdpz56WjJcaL8va3eRnhejVbL3waBdC4GTkxbm8YuzV5yg6My9oQ5hAbU3eAjcw9RLXY2Ha3FQsyLWWgZbAY0Ekmc7Q3%2BMkDezxtOGuNtJVuTtSDZXhwzvty4RWuIVii1t3gRMjIdyIUIxKHIq%2Bnw79%2BUEw7XVSlOUK2w8C2MA9mhtK42%2Fu5pX%2BU&X-Amz-Signature=5cd1e684fcd6fbe98f00565c84b15952970969d2caf5282a832f9c69dceeeaea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T76DTWY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCID7htflT1ewhayUgoVueEJ2IB%2F1B8MR5556nlsFY7G2HAiEAhQHsKiQV8qMY2JnVgimSS8eNz964MMY%2Fb%2BdWbWc2vWUq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDFaikPSO%2BfvwZF%2FTwyrcA1OHjyI8yYv3DAn1Wg93Q0D31IyyvVWJNo1hxSa9Ct9ssCSuQFY%2BUHbPtg0QeHcBzjU7Q2v%2FhydssRIc7nqfZ94v%2Fgq6p9TmqnMHOEHGUEeUdCVeol%2BiKRwkqtcRTjH0pwTVXWMjPYtOVsH9vnMOf%2FUu0vdBItl6LlGLC5L0Gle5HF90iNtq9GJvlXTboeYhmQxtCP0DlQ3%2BKv5TAE%2FOW9W0Ji9EInPGsvXonvkVNwg5lBgxSLogioSN4gIYFXsqwOGjb3J6KMSjD91oK2R1BhN7D1diJU5scRdvFSlMiYSQBQzlngOJZ1lNGDCOn55CGF8LGXZ3ifqKsSIYHLVJYXUJ147sym51sTipsj5yIbDOmpaIGfZHIylks4povTS4IKGJNYJabPcJhCXmxXT8ckgOSQ42%2FkLJ%2BoTqrMkEIh6aA%2Brin4RiOcTUwMsIudTYKXcedNwigBraAVK4JJ24BHCXr6TFx%2F3t%2BKT4pgOZ25NDQZ2HqMMvI2ZPGWO%2BVPuq7jeOAkQSR0nMDqPeuLDt2akn2xBePA2eDKB7r%2BD2DWFOAcL0IlPYeEDThRT8BUZaUXZdxjwK8QF7NGBboYv3s%2BWJruXAyE4Ki2UsbBGUhUpxUv4ylFMcPotOajsXMMGdjr0GOqUBxUd7E9G679h9FHVARagQbOJVqHgmRhzoPzUdTdpz56WjJcaL8va3eRnhejVbL3waBdC4GTkxbm8YuzV5yg6My9oQ5hAbU3eAjcw9RLXY2Ha3FQsyLWWgZbAY0Ekmc7Q3%2BMkDezxtOGuNtJVuTtSDZXhwzvty4RWuIVii1t3gRMjIdyIUIxKHIq%2Bnw79%2BUEw7XVSlOUK2w8C2MA9mhtK42%2Fu5pX%2BU&X-Amz-Signature=c1c72f503a2c427234333b7427fdbdb6d11987e8475b1b7440100e33aac54837&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDOHLJZO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIGtM0hLO8z2W8dxUOV6BpxEyqwDUi4aUSUZ%2Fbv7BZhkQAiEA1H1TfclZYR4xfqUj0fUrA7kJMsmE2JLLE1731iiiGskq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDF9jzBRy8dVyF3YqCyrcA%2BQz4zIX4MuExEnlST4OXj%2BEBIjGLtMQTkw5rlnYwd65IygIKsfgdE8SOWw391X3x%2FqNCpdkX%2FBqjJb5iy7dJtInskhu4ycWjzuk35f6ZcQiNX7U2Fl4H4VS%2FAk%2BnDr7XlJVyhkStsLgOcIU%2FpYIAM1Hq8gMK4hFsO4l%2BZi47nlXTjaIwfVkOa1s%2F%2F27%2FxOBhWyVCV2WxJFaEv9V8ZF3UswIT2hvsBwI1rPecSDFEj5%2FFjMoMBP3L8bhQwxeL2mlSSojm7wjyYi0akfHAfRKZmYjIL3LoBy5Hd19LoDS%2FDXF%2BdVJtIUgDHf8A0BdsrQuBUld%2BuocOmHnYiNI3NEhwZpBtFReI002Aoq96o7nrbefze2mEzzDZc0Zv5yM0gQCnkUv1YnbRnQMQ%2BERod1TL%2FA2HWCm7u%2B7YOj59Yx9vZMlR3u0y9UKNaP6b9CfY1SsPqT3A04ii%2FipHruF7rmY6F%2FoJg8NubI0p7t%2BdDGiL01h%2B0IBu4Cr7D0qSc1Ew3KqSczUa03zwCh128GdSVKu0sfNb12107xXvRT3BLjn%2BeSOA2Zr%2FnUkm97iOB125isnGRUuvWG3fJvKCPquIIAIHzUf4gTZo%2FLOT1KORyn%2BJ2Lzc9mt5qNJhwQpP6nmMOidjr0GOqUBsjKzso78kWD%2B8K%2BaixJ2q1NCPH3UGTnPuPegDYWp78bs4Drpw0H5U7mnzfE%2FaA2G0MO6AZAbHnqKvaevKRRlsJ0DKAOfdgU2IyaCJKrqfVBKnK6vE8woS70hxCthSK52ZitwX8fFBCNJQZRbprn7%2FjdeIWz0u1qliJ9i30QZrIxWJvpu%2BzhJ0BQw9TgaP6Y8FM9tMfDYm1A7RFpEG%2FoevspZjiis&X-Amz-Signature=5d39322c70f748d076fbc0b05f279a3187bc5d5e670f2f86c6fbf61b5084a117&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDOHLJZO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIGtM0hLO8z2W8dxUOV6BpxEyqwDUi4aUSUZ%2Fbv7BZhkQAiEA1H1TfclZYR4xfqUj0fUrA7kJMsmE2JLLE1731iiiGskq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDF9jzBRy8dVyF3YqCyrcA%2BQz4zIX4MuExEnlST4OXj%2BEBIjGLtMQTkw5rlnYwd65IygIKsfgdE8SOWw391X3x%2FqNCpdkX%2FBqjJb5iy7dJtInskhu4ycWjzuk35f6ZcQiNX7U2Fl4H4VS%2FAk%2BnDr7XlJVyhkStsLgOcIU%2FpYIAM1Hq8gMK4hFsO4l%2BZi47nlXTjaIwfVkOa1s%2F%2F27%2FxOBhWyVCV2WxJFaEv9V8ZF3UswIT2hvsBwI1rPecSDFEj5%2FFjMoMBP3L8bhQwxeL2mlSSojm7wjyYi0akfHAfRKZmYjIL3LoBy5Hd19LoDS%2FDXF%2BdVJtIUgDHf8A0BdsrQuBUld%2BuocOmHnYiNI3NEhwZpBtFReI002Aoq96o7nrbefze2mEzzDZc0Zv5yM0gQCnkUv1YnbRnQMQ%2BERod1TL%2FA2HWCm7u%2B7YOj59Yx9vZMlR3u0y9UKNaP6b9CfY1SsPqT3A04ii%2FipHruF7rmY6F%2FoJg8NubI0p7t%2BdDGiL01h%2B0IBu4Cr7D0qSc1Ew3KqSczUa03zwCh128GdSVKu0sfNb12107xXvRT3BLjn%2BeSOA2Zr%2FnUkm97iOB125isnGRUuvWG3fJvKCPquIIAIHzUf4gTZo%2FLOT1KORyn%2BJ2Lzc9mt5qNJhwQpP6nmMOidjr0GOqUBsjKzso78kWD%2B8K%2BaixJ2q1NCPH3UGTnPuPegDYWp78bs4Drpw0H5U7mnzfE%2FaA2G0MO6AZAbHnqKvaevKRRlsJ0DKAOfdgU2IyaCJKrqfVBKnK6vE8woS70hxCthSK52ZitwX8fFBCNJQZRbprn7%2FjdeIWz0u1qliJ9i30QZrIxWJvpu%2BzhJ0BQw9TgaP6Y8FM9tMfDYm1A7RFpEG%2FoevspZjiis&X-Amz-Signature=c26abe7a25497f0964c42268e51c0be047335aeae8a51c2c1b2f743b771766c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T76DTWY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCID7htflT1ewhayUgoVueEJ2IB%2F1B8MR5556nlsFY7G2HAiEAhQHsKiQV8qMY2JnVgimSS8eNz964MMY%2Fb%2BdWbWc2vWUq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDFaikPSO%2BfvwZF%2FTwyrcA1OHjyI8yYv3DAn1Wg93Q0D31IyyvVWJNo1hxSa9Ct9ssCSuQFY%2BUHbPtg0QeHcBzjU7Q2v%2FhydssRIc7nqfZ94v%2Fgq6p9TmqnMHOEHGUEeUdCVeol%2BiKRwkqtcRTjH0pwTVXWMjPYtOVsH9vnMOf%2FUu0vdBItl6LlGLC5L0Gle5HF90iNtq9GJvlXTboeYhmQxtCP0DlQ3%2BKv5TAE%2FOW9W0Ji9EInPGsvXonvkVNwg5lBgxSLogioSN4gIYFXsqwOGjb3J6KMSjD91oK2R1BhN7D1diJU5scRdvFSlMiYSQBQzlngOJZ1lNGDCOn55CGF8LGXZ3ifqKsSIYHLVJYXUJ147sym51sTipsj5yIbDOmpaIGfZHIylks4povTS4IKGJNYJabPcJhCXmxXT8ckgOSQ42%2FkLJ%2BoTqrMkEIh6aA%2Brin4RiOcTUwMsIudTYKXcedNwigBraAVK4JJ24BHCXr6TFx%2F3t%2BKT4pgOZ25NDQZ2HqMMvI2ZPGWO%2BVPuq7jeOAkQSR0nMDqPeuLDt2akn2xBePA2eDKB7r%2BD2DWFOAcL0IlPYeEDThRT8BUZaUXZdxjwK8QF7NGBboYv3s%2BWJruXAyE4Ki2UsbBGUhUpxUv4ylFMcPotOajsXMMGdjr0GOqUBxUd7E9G679h9FHVARagQbOJVqHgmRhzoPzUdTdpz56WjJcaL8va3eRnhejVbL3waBdC4GTkxbm8YuzV5yg6My9oQ5hAbU3eAjcw9RLXY2Ha3FQsyLWWgZbAY0Ekmc7Q3%2BMkDezxtOGuNtJVuTtSDZXhwzvty4RWuIVii1t3gRMjIdyIUIxKHIq%2Bnw79%2BUEw7XVSlOUK2w8C2MA9mhtK42%2Fu5pX%2BU&X-Amz-Signature=1d4a57eacfba592f57e19d4dbc759dedd2b30ae26f2cba08d97023f94bb9a413&X-Amz-SignedHeaders=host&x-id=GetObject)
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