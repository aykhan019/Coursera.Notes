

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIHGUHOV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCICW%2FNzCBcUo1%2BBy9zcun9I0pO1b6tRH4fN2uRdPbdLaEAiEAkBtr7UD4Yb45mLIoNnprFfuz%2BnEbG8L9Ct%2F5DCbwlzAq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDNYG0TFGD1bPcjd3hCrcA8%2BeBSxj8d8rVTiqNi3z8OWsxWZEr53l4aGEPDYdATPv0b6Y6VL0rXkrwlFYBpW%2FiNK3EtuDCSTKYnKAJBsEn61emicx6E14c7xXwmbkzmQ0HuxdsKywubd9dpZtcZNcqYC0vJpFfkKu8l0PRLFJeZlIUj8H58wKZ%2F3N%2FT0VzcFKPNQPe6%2Bx4QGTPYRCw9MdU0XIvuYx33bPte1evnQHHhmRSaJEnGtMVn8EgHaMz0zFHQ4xDyO%2FDSHDSKgIhE5WLu3IHkKskP0pN8FfMx5SPHvZaNroIL31753O0JAUmaLOeQefSBW4drwqs2zl87Y7Dev%2FDhmJ%2BCyZgvHlb6Bbeb8gW391CPQNtYx01ulA07fcE%2FcYcJPnvcNlZjDOZ%2FjhEV1qgCA%2BI47DYWoE4Y4y35rKmuq8N4P8uTi5nt69oh%2BUaRBvuGMVyBRaAsMwxQ%2B8ZpoKJTv9LkjDnDDEgGtFLr8PEm%2Ff32%2FaDLNsiHG8OpWKrn3xma5X%2F%2FBHh%2BO6Q0c1oKXXp3Iuu5QRqiE3DUV14UVeFcFxa%2FRE3fDNx%2BMnU8aMX%2F5G99IhODjXXvoxvXZZdpp%2Frp3wl5%2BGqtpBldED2MMDiK5Zhep%2FpS70r%2BWBEg%2Fq9Mm9MYk3z0XqbOJBMNqgib0GOqUBhNnJv37nPgQxtajXqq3S99yNlLKmytRSpJjPzsUpcnqaRwUKKCrV2YUIUwOgj2BWCqe9382iOjzi1POun6rSAE55d23tC0tvkzjRo4SoG2kA0RKn7kPCDMU5qK6Ht6Ig4p2ZtIpiqYKoqIgRgU9HhmsTn8sP9R9AOvrFY0aC5nWmiXh7%2FMZsSEmsQuQxB5FsgOMOgbs6Fbw4dOqSkI7eCGfjk0Ko&X-Amz-Signature=b9e5772b159f4fe91c4a386c1dfe35e887beca7a676efaf78135c8761d0bf7ec&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIHGUHOV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCICW%2FNzCBcUo1%2BBy9zcun9I0pO1b6tRH4fN2uRdPbdLaEAiEAkBtr7UD4Yb45mLIoNnprFfuz%2BnEbG8L9Ct%2F5DCbwlzAq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDNYG0TFGD1bPcjd3hCrcA8%2BeBSxj8d8rVTiqNi3z8OWsxWZEr53l4aGEPDYdATPv0b6Y6VL0rXkrwlFYBpW%2FiNK3EtuDCSTKYnKAJBsEn61emicx6E14c7xXwmbkzmQ0HuxdsKywubd9dpZtcZNcqYC0vJpFfkKu8l0PRLFJeZlIUj8H58wKZ%2F3N%2FT0VzcFKPNQPe6%2Bx4QGTPYRCw9MdU0XIvuYx33bPte1evnQHHhmRSaJEnGtMVn8EgHaMz0zFHQ4xDyO%2FDSHDSKgIhE5WLu3IHkKskP0pN8FfMx5SPHvZaNroIL31753O0JAUmaLOeQefSBW4drwqs2zl87Y7Dev%2FDhmJ%2BCyZgvHlb6Bbeb8gW391CPQNtYx01ulA07fcE%2FcYcJPnvcNlZjDOZ%2FjhEV1qgCA%2BI47DYWoE4Y4y35rKmuq8N4P8uTi5nt69oh%2BUaRBvuGMVyBRaAsMwxQ%2B8ZpoKJTv9LkjDnDDEgGtFLr8PEm%2Ff32%2FaDLNsiHG8OpWKrn3xma5X%2F%2FBHh%2BO6Q0c1oKXXp3Iuu5QRqiE3DUV14UVeFcFxa%2FRE3fDNx%2BMnU8aMX%2F5G99IhODjXXvoxvXZZdpp%2Frp3wl5%2BGqtpBldED2MMDiK5Zhep%2FpS70r%2BWBEg%2Fq9Mm9MYk3z0XqbOJBMNqgib0GOqUBhNnJv37nPgQxtajXqq3S99yNlLKmytRSpJjPzsUpcnqaRwUKKCrV2YUIUwOgj2BWCqe9382iOjzi1POun6rSAE55d23tC0tvkzjRo4SoG2kA0RKn7kPCDMU5qK6Ht6Ig4p2ZtIpiqYKoqIgRgU9HhmsTn8sP9R9AOvrFY0aC5nWmiXh7%2FMZsSEmsQuQxB5FsgOMOgbs6Fbw4dOqSkI7eCGfjk0Ko&X-Amz-Signature=89695c367d8313715304bf7525a596139555a25829256a2f35885e79d49c9dd7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIHGUHOV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCICW%2FNzCBcUo1%2BBy9zcun9I0pO1b6tRH4fN2uRdPbdLaEAiEAkBtr7UD4Yb45mLIoNnprFfuz%2BnEbG8L9Ct%2F5DCbwlzAq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDNYG0TFGD1bPcjd3hCrcA8%2BeBSxj8d8rVTiqNi3z8OWsxWZEr53l4aGEPDYdATPv0b6Y6VL0rXkrwlFYBpW%2FiNK3EtuDCSTKYnKAJBsEn61emicx6E14c7xXwmbkzmQ0HuxdsKywubd9dpZtcZNcqYC0vJpFfkKu8l0PRLFJeZlIUj8H58wKZ%2F3N%2FT0VzcFKPNQPe6%2Bx4QGTPYRCw9MdU0XIvuYx33bPte1evnQHHhmRSaJEnGtMVn8EgHaMz0zFHQ4xDyO%2FDSHDSKgIhE5WLu3IHkKskP0pN8FfMx5SPHvZaNroIL31753O0JAUmaLOeQefSBW4drwqs2zl87Y7Dev%2FDhmJ%2BCyZgvHlb6Bbeb8gW391CPQNtYx01ulA07fcE%2FcYcJPnvcNlZjDOZ%2FjhEV1qgCA%2BI47DYWoE4Y4y35rKmuq8N4P8uTi5nt69oh%2BUaRBvuGMVyBRaAsMwxQ%2B8ZpoKJTv9LkjDnDDEgGtFLr8PEm%2Ff32%2FaDLNsiHG8OpWKrn3xma5X%2F%2FBHh%2BO6Q0c1oKXXp3Iuu5QRqiE3DUV14UVeFcFxa%2FRE3fDNx%2BMnU8aMX%2F5G99IhODjXXvoxvXZZdpp%2Frp3wl5%2BGqtpBldED2MMDiK5Zhep%2FpS70r%2BWBEg%2Fq9Mm9MYk3z0XqbOJBMNqgib0GOqUBhNnJv37nPgQxtajXqq3S99yNlLKmytRSpJjPzsUpcnqaRwUKKCrV2YUIUwOgj2BWCqe9382iOjzi1POun6rSAE55d23tC0tvkzjRo4SoG2kA0RKn7kPCDMU5qK6Ht6Ig4p2ZtIpiqYKoqIgRgU9HhmsTn8sP9R9AOvrFY0aC5nWmiXh7%2FMZsSEmsQuQxB5FsgOMOgbs6Fbw4dOqSkI7eCGfjk0Ko&X-Amz-Signature=d49dcfe88fb5b091a020fd4a73e4debb465e1006e84887c3442d78dc26cf8256&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMCDYJYZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIH%2FsxQpLd5ggYs9eVOlT5OPisX2qd9%2FE7VU%2BTEozjwNgAiEA%2FrmELQGup38U414hL%2Fb3cYw%2BPXTUo780iFdriGXRxqgq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDNNuvzNac1GFxLvluSrcA5RY1MxRfEt4Yy6lqgwUayNKg%2BsqFhbceZQvKToN%2BLlIvejHXCSrUVT08jdx9OHFFUeoc5gOXQy3Yoqt1OXI%2B%2BYEJUQhJRHEmGgLRRDHNE489fKrdP9d%2FOz4kQUr5M%2BLJWEnWPjNGLj2xh0ZBcGs%2BOg8FXgmNntG%2F1oGMW%2BsXvbIeOtJEGAZ%2BcZUkpCWcvaL0A75Ai%2BmSKSJp%2FAkyUlMdcoqbeCIgPH3k99vwd9uDicaqocrmNZVjaUeSu%2B4QvW6cjorsj8PaoJelBWtykhBBywt6obXD%2Fsje4ePKuHOjISfTMUvnc2EzEMZWeOAOPv%2BNpt%2F%2BwN5grN5nQ0Cd%2Bik2F1l%2FDVr4fvkHhvpZt3F7yjWHgY7axPIwuaQ8wGUVBOWdItNkG7mExarlgJvUcgmkyiHSRxY%2FOMUuaKX5mvtfAy5OBVdi77NEsjGOOgbSCU23PHsJuY8tzxm6GZphzDeOChG9UR5V6HsO1fOuA0zF9OP95PMooi7JC%2FUyCsQY0%2F6%2BnCtAHB%2Btgda5kTftLtDk6671%2F1PFYnqvLw6Ec5N0%2B4fhqGhYoa9Fi5%2FmeLIBpRQAWEtj3rV69alAE7SMquuKfxXnbWmM%2FUthzO9hOu4GGll4fgaB%2BHCbNRgQuRIMKWhib0GOqUBjA%2BkfZ1I%2FwgtxpAefOpbD3F0l3%2F6hP2Uek4E238w6WF7WdPaZ3Cbn7uFiFvy1JETrva5dErH%2F7T8bTxgYb%2B068O6A1RzHC7ChfUkKTKmTB59s1k7v9WTeyL40sS7XelKdiR5QcHoMxn8LdReWYm8ETCmEgAj6bTGxpFAPMEAYKiKx6EEZcUc%2FOEW1ABYDrWiT3aYL%2FIH4%2BJHZKghD5kQCOQyv04V&X-Amz-Signature=eaf3cd3882a9f1aa8f62e2ffe9fa1727e6b60d50683a4bc88eba66672fc77ed4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMCDYJYZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIH%2FsxQpLd5ggYs9eVOlT5OPisX2qd9%2FE7VU%2BTEozjwNgAiEA%2FrmELQGup38U414hL%2Fb3cYw%2BPXTUo780iFdriGXRxqgq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDNNuvzNac1GFxLvluSrcA5RY1MxRfEt4Yy6lqgwUayNKg%2BsqFhbceZQvKToN%2BLlIvejHXCSrUVT08jdx9OHFFUeoc5gOXQy3Yoqt1OXI%2B%2BYEJUQhJRHEmGgLRRDHNE489fKrdP9d%2FOz4kQUr5M%2BLJWEnWPjNGLj2xh0ZBcGs%2BOg8FXgmNntG%2F1oGMW%2BsXvbIeOtJEGAZ%2BcZUkpCWcvaL0A75Ai%2BmSKSJp%2FAkyUlMdcoqbeCIgPH3k99vwd9uDicaqocrmNZVjaUeSu%2B4QvW6cjorsj8PaoJelBWtykhBBywt6obXD%2Fsje4ePKuHOjISfTMUvnc2EzEMZWeOAOPv%2BNpt%2F%2BwN5grN5nQ0Cd%2Bik2F1l%2FDVr4fvkHhvpZt3F7yjWHgY7axPIwuaQ8wGUVBOWdItNkG7mExarlgJvUcgmkyiHSRxY%2FOMUuaKX5mvtfAy5OBVdi77NEsjGOOgbSCU23PHsJuY8tzxm6GZphzDeOChG9UR5V6HsO1fOuA0zF9OP95PMooi7JC%2FUyCsQY0%2F6%2BnCtAHB%2Btgda5kTftLtDk6671%2F1PFYnqvLw6Ec5N0%2B4fhqGhYoa9Fi5%2FmeLIBpRQAWEtj3rV69alAE7SMquuKfxXnbWmM%2FUthzO9hOu4GGll4fgaB%2BHCbNRgQuRIMKWhib0GOqUBjA%2BkfZ1I%2FwgtxpAefOpbD3F0l3%2F6hP2Uek4E238w6WF7WdPaZ3Cbn7uFiFvy1JETrva5dErH%2F7T8bTxgYb%2B068O6A1RzHC7ChfUkKTKmTB59s1k7v9WTeyL40sS7XelKdiR5QcHoMxn8LdReWYm8ETCmEgAj6bTGxpFAPMEAYKiKx6EEZcUc%2FOEW1ABYDrWiT3aYL%2FIH4%2BJHZKghD5kQCOQyv04V&X-Amz-Signature=a7d5140b40d8cd2cb5ecea79e1db9076381a79120dbba52a23bf2b16b788ebfa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIHGUHOV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCICW%2FNzCBcUo1%2BBy9zcun9I0pO1b6tRH4fN2uRdPbdLaEAiEAkBtr7UD4Yb45mLIoNnprFfuz%2BnEbG8L9Ct%2F5DCbwlzAq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDNYG0TFGD1bPcjd3hCrcA8%2BeBSxj8d8rVTiqNi3z8OWsxWZEr53l4aGEPDYdATPv0b6Y6VL0rXkrwlFYBpW%2FiNK3EtuDCSTKYnKAJBsEn61emicx6E14c7xXwmbkzmQ0HuxdsKywubd9dpZtcZNcqYC0vJpFfkKu8l0PRLFJeZlIUj8H58wKZ%2F3N%2FT0VzcFKPNQPe6%2Bx4QGTPYRCw9MdU0XIvuYx33bPte1evnQHHhmRSaJEnGtMVn8EgHaMz0zFHQ4xDyO%2FDSHDSKgIhE5WLu3IHkKskP0pN8FfMx5SPHvZaNroIL31753O0JAUmaLOeQefSBW4drwqs2zl87Y7Dev%2FDhmJ%2BCyZgvHlb6Bbeb8gW391CPQNtYx01ulA07fcE%2FcYcJPnvcNlZjDOZ%2FjhEV1qgCA%2BI47DYWoE4Y4y35rKmuq8N4P8uTi5nt69oh%2BUaRBvuGMVyBRaAsMwxQ%2B8ZpoKJTv9LkjDnDDEgGtFLr8PEm%2Ff32%2FaDLNsiHG8OpWKrn3xma5X%2F%2FBHh%2BO6Q0c1oKXXp3Iuu5QRqiE3DUV14UVeFcFxa%2FRE3fDNx%2BMnU8aMX%2F5G99IhODjXXvoxvXZZdpp%2Frp3wl5%2BGqtpBldED2MMDiK5Zhep%2FpS70r%2BWBEg%2Fq9Mm9MYk3z0XqbOJBMNqgib0GOqUBhNnJv37nPgQxtajXqq3S99yNlLKmytRSpJjPzsUpcnqaRwUKKCrV2YUIUwOgj2BWCqe9382iOjzi1POun6rSAE55d23tC0tvkzjRo4SoG2kA0RKn7kPCDMU5qK6Ht6Ig4p2ZtIpiqYKoqIgRgU9HhmsTn8sP9R9AOvrFY0aC5nWmiXh7%2FMZsSEmsQuQxB5FsgOMOgbs6Fbw4dOqSkI7eCGfjk0Ko&X-Amz-Signature=f72f005db4ae7f8941f2603f9c28acb29262446babc37a6a990fa69e1c08d80d&X-Amz-SignedHeaders=host&x-id=GetObject)
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