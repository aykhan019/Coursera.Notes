

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XGYOOGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCAJUkkytBfemv4Zg8s03BkYO3PZIQ%2FnFLYW2FtTMoitgIhAOEQxw5Z3FOqFo4855MrZdF9bAG7SpLa%2BBUPK2Mlbpb0Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzLc%2BiOabxFrgMq14Eq3ANF%2F%2BquOpVt0bYXfzHMdmPZrP5sUECri0TLc8bWzm7CJbJiQH1m86jkV4ZIrfPP2d8bZ2sqoDhE0CJhyzAMYfJ8clc4oe1H67w2KS%2Fa%2BQT6ajc4XCuX17ylfDwRqpSPwcb3BwuxNLFF8OWADMyv1mNt7y8%2BCO6UY1PHUWZjnU2hKlJylP0tbmGgZPrDf7apSywsyP5OLo3EXJ4yOqKgNv8CRsJC%2Bp8MOO1iLfN2CAsXXmwSQTQXnA%2BsLUHkHD%2B8IxnhlORI0p5q0V1qxnuZJp77qjKfGDrAau%2BoCftrtiQp6QXxXYuVg5r0kNtJ0E1KIMIJ7Gy35tg%2Bm60%2FNOyJwRPfeWjgD%2FFSI07K1qAY44rJxEPpKiGvXXI93UmE3KZyZEFgOH0TuI9TqE%2BsCsXJ4pkTr3jVRLPCWC26BG%2BFIvlVVvs0kOHnHq%2F2tF0EFNqFhRYB15A45FPXqsmMt1Lls9aAH98MHSceJeC6sfVWYVOTHFeWRGVJ3Q6ZsvIO1xIWgF2N9p9qUwt3rtObPNWE2gmRyXuxO35TxT%2B7OlCL%2BQsRhgZCu3%2B3q4tvqxAUAxnsVnn7BkNfdFz5kNBjwVcnUkwQp4v%2BwpSmqM%2B4Sp1SSrQgegqNHBYERpvykyzDfzDM6o%2B9BjqkAUwCVmtz4JuZbVoOU2BUGJY96Q4Rv%2BkXNlz1OBXJVxpFlxIT0KtOSvL6aLXP29bTQB53uC8KMIOpFCzAAjQSXJ%2FrCh%2BMWD75bc2bnuiOghObWXM3d%2BYR52bKhLAL0ruQOBvyhMtJYqkgztpVcwMXTCG%2FFT7gVxe71%2BOjQ%2BqhVW8DPSwfnI9sHBOOXkdRYSM%2FCWm64d%2FLPxTsisgol0j65eQer4%2Bx&X-Amz-Signature=a32f8db20b1489b59e375ee352e792d6accc6151885f20c61d04107193aa5eb2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XGYOOGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCAJUkkytBfemv4Zg8s03BkYO3PZIQ%2FnFLYW2FtTMoitgIhAOEQxw5Z3FOqFo4855MrZdF9bAG7SpLa%2BBUPK2Mlbpb0Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzLc%2BiOabxFrgMq14Eq3ANF%2F%2BquOpVt0bYXfzHMdmPZrP5sUECri0TLc8bWzm7CJbJiQH1m86jkV4ZIrfPP2d8bZ2sqoDhE0CJhyzAMYfJ8clc4oe1H67w2KS%2Fa%2BQT6ajc4XCuX17ylfDwRqpSPwcb3BwuxNLFF8OWADMyv1mNt7y8%2BCO6UY1PHUWZjnU2hKlJylP0tbmGgZPrDf7apSywsyP5OLo3EXJ4yOqKgNv8CRsJC%2Bp8MOO1iLfN2CAsXXmwSQTQXnA%2BsLUHkHD%2B8IxnhlORI0p5q0V1qxnuZJp77qjKfGDrAau%2BoCftrtiQp6QXxXYuVg5r0kNtJ0E1KIMIJ7Gy35tg%2Bm60%2FNOyJwRPfeWjgD%2FFSI07K1qAY44rJxEPpKiGvXXI93UmE3KZyZEFgOH0TuI9TqE%2BsCsXJ4pkTr3jVRLPCWC26BG%2BFIvlVVvs0kOHnHq%2F2tF0EFNqFhRYB15A45FPXqsmMt1Lls9aAH98MHSceJeC6sfVWYVOTHFeWRGVJ3Q6ZsvIO1xIWgF2N9p9qUwt3rtObPNWE2gmRyXuxO35TxT%2B7OlCL%2BQsRhgZCu3%2B3q4tvqxAUAxnsVnn7BkNfdFz5kNBjwVcnUkwQp4v%2BwpSmqM%2B4Sp1SSrQgegqNHBYERpvykyzDfzDM6o%2B9BjqkAUwCVmtz4JuZbVoOU2BUGJY96Q4Rv%2BkXNlz1OBXJVxpFlxIT0KtOSvL6aLXP29bTQB53uC8KMIOpFCzAAjQSXJ%2FrCh%2BMWD75bc2bnuiOghObWXM3d%2BYR52bKhLAL0ruQOBvyhMtJYqkgztpVcwMXTCG%2FFT7gVxe71%2BOjQ%2BqhVW8DPSwfnI9sHBOOXkdRYSM%2FCWm64d%2FLPxTsisgol0j65eQer4%2Bx&X-Amz-Signature=cce4a0852cbeb3378d64b55e15d6a1c16ca1216d9b9a33dd0b4f0eae67505329&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XGYOOGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCAJUkkytBfemv4Zg8s03BkYO3PZIQ%2FnFLYW2FtTMoitgIhAOEQxw5Z3FOqFo4855MrZdF9bAG7SpLa%2BBUPK2Mlbpb0Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzLc%2BiOabxFrgMq14Eq3ANF%2F%2BquOpVt0bYXfzHMdmPZrP5sUECri0TLc8bWzm7CJbJiQH1m86jkV4ZIrfPP2d8bZ2sqoDhE0CJhyzAMYfJ8clc4oe1H67w2KS%2Fa%2BQT6ajc4XCuX17ylfDwRqpSPwcb3BwuxNLFF8OWADMyv1mNt7y8%2BCO6UY1PHUWZjnU2hKlJylP0tbmGgZPrDf7apSywsyP5OLo3EXJ4yOqKgNv8CRsJC%2Bp8MOO1iLfN2CAsXXmwSQTQXnA%2BsLUHkHD%2B8IxnhlORI0p5q0V1qxnuZJp77qjKfGDrAau%2BoCftrtiQp6QXxXYuVg5r0kNtJ0E1KIMIJ7Gy35tg%2Bm60%2FNOyJwRPfeWjgD%2FFSI07K1qAY44rJxEPpKiGvXXI93UmE3KZyZEFgOH0TuI9TqE%2BsCsXJ4pkTr3jVRLPCWC26BG%2BFIvlVVvs0kOHnHq%2F2tF0EFNqFhRYB15A45FPXqsmMt1Lls9aAH98MHSceJeC6sfVWYVOTHFeWRGVJ3Q6ZsvIO1xIWgF2N9p9qUwt3rtObPNWE2gmRyXuxO35TxT%2B7OlCL%2BQsRhgZCu3%2B3q4tvqxAUAxnsVnn7BkNfdFz5kNBjwVcnUkwQp4v%2BwpSmqM%2B4Sp1SSrQgegqNHBYERpvykyzDfzDM6o%2B9BjqkAUwCVmtz4JuZbVoOU2BUGJY96Q4Rv%2BkXNlz1OBXJVxpFlxIT0KtOSvL6aLXP29bTQB53uC8KMIOpFCzAAjQSXJ%2FrCh%2BMWD75bc2bnuiOghObWXM3d%2BYR52bKhLAL0ruQOBvyhMtJYqkgztpVcwMXTCG%2FFT7gVxe71%2BOjQ%2BqhVW8DPSwfnI9sHBOOXkdRYSM%2FCWm64d%2FLPxTsisgol0j65eQer4%2Bx&X-Amz-Signature=588ff83fce78e94ce48f8fb38d36b0934c71a5903376a1159f1568ff692a983c&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAEZV5JW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIEGE4WhbXmXkca%2Ft3M%2F%2BzyBzxSvh83qcxXMxb0imh%2Bi2AiBdjILCeDitXESShiPn53KmVZgCSsHihgVWg3KrXksJTCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMsHmYypgv8EnQpLxjKtwDBCXsd3mrw5%2BeD8gNT2i%2FrrKdUNbilBHnMVZQLZuZlY%2FcnxkDXlWr9hd7EdeJwGh8gWCH6ef9Q%2B3my1RZOXB%2FE8rmlBqR47dNS%2B%2BlxWHQLtYMR0jBQvx8lz%2BFxnOFIF4RlJg1Ys4mLJ4zZU3ytzlC1s1fabfTwVzK8IeZjyopXYs%2BPd%2BGxucpR1IfRV1wDoKvuZJ%2FvCjEENXz%2BycYqmjHk82axXmYpsKXSfFvMh%2F3%2BglOWtQxWbuL8yzID%2FbFkq32H7hNyuurBgSgbFfXADtSNb70kigC%2FPdCRkTTnZ9qC59dKkWqaNAuQ28PBvwj05mIU62a6USQRihU4jH%2FVsLp8n7goMdHB96asPAru7sE2iBkN3TzQGgOAHJf4dvXwBta3AtcIHVs6JUODo6tYAj1lZCdYzcsuWMs09qidufvuwSjMXymDQFbiCGrUZ14aCquKFzVOJoCOGWhNbNjM7ADKbdFLhGDWmoUUZPCAauD%2FbgdE1AA8%2FlYoIgEjrJSsLMezafLDSAaJfDkH%2FWhsD6onOjr9SLpsyPuIJC%2B0Dk%2BvS02KqGgC0UHZy7yofAH2RPdoi7MEefVhAJaHTstU115iyplWAm0RM%2F%2BoCn7fOIZTI0PNQMAL5bKsQ86D%2BAwvuqPvQY6pgHDlEtl8uOf4w1I%2B6y2%2B29qiduaL%2FM2xwe8KjUCqKpwBn8YilD%2B7MT7GkwG2eco9qKEiTXc7YEVjFmlFaB03G2qAFjIMS3XZvUj1DzkzzvNUXlsaZJzQ31mVqLYMh2QQt75afMULrgDYVcou0V1SMhw6dZSC91X6DMZuY6KI4Eq2CUgrbGaKYSGc7BbJkEoFE46Rw9zmRPUOf%2FWV1TmSkZTcbd1oryZ&X-Amz-Signature=e066f99bae8d632d6784925c673dc78f7a9dff3dbe51dadbf7eb54ae3b83842d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAEZV5JW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIEGE4WhbXmXkca%2Ft3M%2F%2BzyBzxSvh83qcxXMxb0imh%2Bi2AiBdjILCeDitXESShiPn53KmVZgCSsHihgVWg3KrXksJTCr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMsHmYypgv8EnQpLxjKtwDBCXsd3mrw5%2BeD8gNT2i%2FrrKdUNbilBHnMVZQLZuZlY%2FcnxkDXlWr9hd7EdeJwGh8gWCH6ef9Q%2B3my1RZOXB%2FE8rmlBqR47dNS%2B%2BlxWHQLtYMR0jBQvx8lz%2BFxnOFIF4RlJg1Ys4mLJ4zZU3ytzlC1s1fabfTwVzK8IeZjyopXYs%2BPd%2BGxucpR1IfRV1wDoKvuZJ%2FvCjEENXz%2BycYqmjHk82axXmYpsKXSfFvMh%2F3%2BglOWtQxWbuL8yzID%2FbFkq32H7hNyuurBgSgbFfXADtSNb70kigC%2FPdCRkTTnZ9qC59dKkWqaNAuQ28PBvwj05mIU62a6USQRihU4jH%2FVsLp8n7goMdHB96asPAru7sE2iBkN3TzQGgOAHJf4dvXwBta3AtcIHVs6JUODo6tYAj1lZCdYzcsuWMs09qidufvuwSjMXymDQFbiCGrUZ14aCquKFzVOJoCOGWhNbNjM7ADKbdFLhGDWmoUUZPCAauD%2FbgdE1AA8%2FlYoIgEjrJSsLMezafLDSAaJfDkH%2FWhsD6onOjr9SLpsyPuIJC%2B0Dk%2BvS02KqGgC0UHZy7yofAH2RPdoi7MEefVhAJaHTstU115iyplWAm0RM%2F%2BoCn7fOIZTI0PNQMAL5bKsQ86D%2BAwvuqPvQY6pgHDlEtl8uOf4w1I%2B6y2%2B29qiduaL%2FM2xwe8KjUCqKpwBn8YilD%2B7MT7GkwG2eco9qKEiTXc7YEVjFmlFaB03G2qAFjIMS3XZvUj1DzkzzvNUXlsaZJzQ31mVqLYMh2QQt75afMULrgDYVcou0V1SMhw6dZSC91X6DMZuY6KI4Eq2CUgrbGaKYSGc7BbJkEoFE46Rw9zmRPUOf%2FWV1TmSkZTcbd1oryZ&X-Amz-Signature=eb52be01ca2a1da4e8756fa4ef0491f3da1b1a4109b1c3d37805c9afd1d52aa0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XGYOOGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCAJUkkytBfemv4Zg8s03BkYO3PZIQ%2FnFLYW2FtTMoitgIhAOEQxw5Z3FOqFo4855MrZdF9bAG7SpLa%2BBUPK2Mlbpb0Kv8DCFEQABoMNjM3NDIzMTgzODA1IgzLc%2BiOabxFrgMq14Eq3ANF%2F%2BquOpVt0bYXfzHMdmPZrP5sUECri0TLc8bWzm7CJbJiQH1m86jkV4ZIrfPP2d8bZ2sqoDhE0CJhyzAMYfJ8clc4oe1H67w2KS%2Fa%2BQT6ajc4XCuX17ylfDwRqpSPwcb3BwuxNLFF8OWADMyv1mNt7y8%2BCO6UY1PHUWZjnU2hKlJylP0tbmGgZPrDf7apSywsyP5OLo3EXJ4yOqKgNv8CRsJC%2Bp8MOO1iLfN2CAsXXmwSQTQXnA%2BsLUHkHD%2B8IxnhlORI0p5q0V1qxnuZJp77qjKfGDrAau%2BoCftrtiQp6QXxXYuVg5r0kNtJ0E1KIMIJ7Gy35tg%2Bm60%2FNOyJwRPfeWjgD%2FFSI07K1qAY44rJxEPpKiGvXXI93UmE3KZyZEFgOH0TuI9TqE%2BsCsXJ4pkTr3jVRLPCWC26BG%2BFIvlVVvs0kOHnHq%2F2tF0EFNqFhRYB15A45FPXqsmMt1Lls9aAH98MHSceJeC6sfVWYVOTHFeWRGVJ3Q6ZsvIO1xIWgF2N9p9qUwt3rtObPNWE2gmRyXuxO35TxT%2B7OlCL%2BQsRhgZCu3%2B3q4tvqxAUAxnsVnn7BkNfdFz5kNBjwVcnUkwQp4v%2BwpSmqM%2B4Sp1SSrQgegqNHBYERpvykyzDfzDM6o%2B9BjqkAUwCVmtz4JuZbVoOU2BUGJY96Q4Rv%2BkXNlz1OBXJVxpFlxIT0KtOSvL6aLXP29bTQB53uC8KMIOpFCzAAjQSXJ%2FrCh%2BMWD75bc2bnuiOghObWXM3d%2BYR52bKhLAL0ruQOBvyhMtJYqkgztpVcwMXTCG%2FFT7gVxe71%2BOjQ%2BqhVW8DPSwfnI9sHBOOXkdRYSM%2FCWm64d%2FLPxTsisgol0j65eQer4%2Bx&X-Amz-Signature=b7a75a6bad324d14f59e6163a40aa7aac1b07e51923ed4580784658a863aaeae&X-Amz-SignedHeaders=host&x-id=GetObject)
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