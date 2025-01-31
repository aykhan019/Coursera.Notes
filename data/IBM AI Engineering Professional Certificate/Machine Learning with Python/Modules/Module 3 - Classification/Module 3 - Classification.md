

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7SLO3WA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAmXM7BjaFO8C7EhX3cYMxslqsVnbbxCDFluc9Za%2FQttAiEA%2FpEJibh0AiyQjvBY5FZmI9eLl3f%2FT2ixLJFwsvRN6V0qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXif8w8l8y0gKAloircA1f2jdWixJHJgnP189l3n%2FmsV%2FswcmEf5CCGbcxUFHikcD%2BLmt0emTnnhq%2FVBZXSuVD9JgPR3Id17sk399fRAUJXJpmiUVZxM3qJLqe3r73yr7W7WJVi%2BVBc3zm9OlMOe07wJprxPTV704evzNYGEwB%2B3%2FkV6W6fkjIblI0x4AKjgK6pk12z4jRdEeoFS%2FhSL19ZCiTQaFTOMC2801y2sdaTWODSGYHcBe%2FEGePUf1UuIM8Ueh9zcUaBRp7U0wqeCTJyN1XGV4vjuRq9GTez4e9MnhtgliSBDNLSFPJ0A8oWNEL9ufvFYTxbs020W1mTGS3YOus34nV%2BR8DM0ZWj%2ByZGaWZvEXcDBfwlDXMBp7Kb5FubHLOBDsdimt1qvNPnOnueWd5bRkWrZVU8lKTIZbdlaxMsxtLjX8jtjinm%2BYaiD0%2FQ%2FTatsNTkaTC8VKC8WlmbHIiEbcHb7AIstcBiW3HrcmTR%2BaYyPQjvvwj%2FJvWjCivLVLSytE%2BRDPxLhlZdoRpmU2kYqxuo%2BY0B2ryDYk5jvZDF8uwEsGYHB1KahK2JHxKosvBLBhIi4PwGzh09LPefbtNY1jLahsIeDkwupNFF6gqqZIlXzhNmn5p3kuHt6j0bbim091XD9xrzMM%2Bj9LwGOqUB800dSVVquVLjoEp3hTvLPOFaSZrow8WVRP7NgI6zHaAW0MpYucKh3a%2FfLtyS%2F26%2BtDsnPKjeQ%2FZQyycb8Hp7IPdbEWjq5bwA5oIYIHnQvQxJQa5NEa8VA2zTcsZpofCGVIt09ICQfjjKelBMIQzYR8U5SG%2BweKtb7PCbilQXpMotygi7T1TS7stPeLpGumj6RjGKLwLM3m%2B2W4AocCe9N7ykN8gh&X-Amz-Signature=0594ac6b97f63f2f50560fe83a28e2d079a3e2328e7df112df37965824861073&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7SLO3WA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAmXM7BjaFO8C7EhX3cYMxslqsVnbbxCDFluc9Za%2FQttAiEA%2FpEJibh0AiyQjvBY5FZmI9eLl3f%2FT2ixLJFwsvRN6V0qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXif8w8l8y0gKAloircA1f2jdWixJHJgnP189l3n%2FmsV%2FswcmEf5CCGbcxUFHikcD%2BLmt0emTnnhq%2FVBZXSuVD9JgPR3Id17sk399fRAUJXJpmiUVZxM3qJLqe3r73yr7W7WJVi%2BVBc3zm9OlMOe07wJprxPTV704evzNYGEwB%2B3%2FkV6W6fkjIblI0x4AKjgK6pk12z4jRdEeoFS%2FhSL19ZCiTQaFTOMC2801y2sdaTWODSGYHcBe%2FEGePUf1UuIM8Ueh9zcUaBRp7U0wqeCTJyN1XGV4vjuRq9GTez4e9MnhtgliSBDNLSFPJ0A8oWNEL9ufvFYTxbs020W1mTGS3YOus34nV%2BR8DM0ZWj%2ByZGaWZvEXcDBfwlDXMBp7Kb5FubHLOBDsdimt1qvNPnOnueWd5bRkWrZVU8lKTIZbdlaxMsxtLjX8jtjinm%2BYaiD0%2FQ%2FTatsNTkaTC8VKC8WlmbHIiEbcHb7AIstcBiW3HrcmTR%2BaYyPQjvvwj%2FJvWjCivLVLSytE%2BRDPxLhlZdoRpmU2kYqxuo%2BY0B2ryDYk5jvZDF8uwEsGYHB1KahK2JHxKosvBLBhIi4PwGzh09LPefbtNY1jLahsIeDkwupNFF6gqqZIlXzhNmn5p3kuHt6j0bbim091XD9xrzMM%2Bj9LwGOqUB800dSVVquVLjoEp3hTvLPOFaSZrow8WVRP7NgI6zHaAW0MpYucKh3a%2FfLtyS%2F26%2BtDsnPKjeQ%2FZQyycb8Hp7IPdbEWjq5bwA5oIYIHnQvQxJQa5NEa8VA2zTcsZpofCGVIt09ICQfjjKelBMIQzYR8U5SG%2BweKtb7PCbilQXpMotygi7T1TS7stPeLpGumj6RjGKLwLM3m%2B2W4AocCe9N7ykN8gh&X-Amz-Signature=cdbac782605c1658d4453add48370af3660f11a37011e18c016fc301a58eb0a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7SLO3WA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAmXM7BjaFO8C7EhX3cYMxslqsVnbbxCDFluc9Za%2FQttAiEA%2FpEJibh0AiyQjvBY5FZmI9eLl3f%2FT2ixLJFwsvRN6V0qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXif8w8l8y0gKAloircA1f2jdWixJHJgnP189l3n%2FmsV%2FswcmEf5CCGbcxUFHikcD%2BLmt0emTnnhq%2FVBZXSuVD9JgPR3Id17sk399fRAUJXJpmiUVZxM3qJLqe3r73yr7W7WJVi%2BVBc3zm9OlMOe07wJprxPTV704evzNYGEwB%2B3%2FkV6W6fkjIblI0x4AKjgK6pk12z4jRdEeoFS%2FhSL19ZCiTQaFTOMC2801y2sdaTWODSGYHcBe%2FEGePUf1UuIM8Ueh9zcUaBRp7U0wqeCTJyN1XGV4vjuRq9GTez4e9MnhtgliSBDNLSFPJ0A8oWNEL9ufvFYTxbs020W1mTGS3YOus34nV%2BR8DM0ZWj%2ByZGaWZvEXcDBfwlDXMBp7Kb5FubHLOBDsdimt1qvNPnOnueWd5bRkWrZVU8lKTIZbdlaxMsxtLjX8jtjinm%2BYaiD0%2FQ%2FTatsNTkaTC8VKC8WlmbHIiEbcHb7AIstcBiW3HrcmTR%2BaYyPQjvvwj%2FJvWjCivLVLSytE%2BRDPxLhlZdoRpmU2kYqxuo%2BY0B2ryDYk5jvZDF8uwEsGYHB1KahK2JHxKosvBLBhIi4PwGzh09LPefbtNY1jLahsIeDkwupNFF6gqqZIlXzhNmn5p3kuHt6j0bbim091XD9xrzMM%2Bj9LwGOqUB800dSVVquVLjoEp3hTvLPOFaSZrow8WVRP7NgI6zHaAW0MpYucKh3a%2FfLtyS%2F26%2BtDsnPKjeQ%2FZQyycb8Hp7IPdbEWjq5bwA5oIYIHnQvQxJQa5NEa8VA2zTcsZpofCGVIt09ICQfjjKelBMIQzYR8U5SG%2BweKtb7PCbilQXpMotygi7T1TS7stPeLpGumj6RjGKLwLM3m%2B2W4AocCe9N7ykN8gh&X-Amz-Signature=4d6a3cf0519eb507af9c08778375590dcc2bfdce35ee77a06581bb3c933d3316&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDQOL2WY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BfBiW71pmxf7d%2FdkLSXWN9tKLq2nz5Tiej%2BIfIiLDLQIhAOqbEj88gSv1iOUflOPkWSeeNcypraxBoLw9xGJQ8a4ZKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igykjn%2BUowyjy7OiGw8q3ANB3yLuKsXsOzCyQOZ58oOMPhuURbV1P6Lt1is2cNGYHKwPw%2BfbWDKSS8W1LmsK9AGoCdj7Sv7cOZPWcMaFZu3L2c0fvLrvZtctGPa7rgfFk9dL9gBPBpND8HkyTWLjKAtaeThg2J7f2znh5Z70CedvFFBQ%2BL8zHEVF6yowF%2FKSoKPlDGZwzKvXfC23uEQrB3B%2B947zfgLw1qry9xX5YoJO95GDpxk5GlowTHFNAZmgdjYth76DZFIRHjjomhzfKbUoF%2FXLOpiHDJd1D5vQfm7kyTume6k%2FACFKXODBE55Vxw8RRPpmMwG%2Fk3zw2B3O%2FvzHoXKpXdUHUVd92tbPH2si2a9bOG6J1BA%2BlWge7CNqC4ZKdPziJ5d9dPSKXznMNGoI94Xh5uQXbK3vqupljEWWMEvneEkX5D0MlWztcjap0rO9omYRfhK5g92aveYmIiPnKr7aSO19%2FHxqdZcN6m57nTZpXTulvG9Zw1sQcX2FNQpMO3z7dnvfhI2YbI%2BzhC3LqIKCQcOa%2FOVHgdaCxLn1FFcjVb3gm2YFxPYFyAx3uCDYMMqFhEnZLCyqXIaDEL%2F4WCaNIVoReAH3Ht%2B%2FWb16keXyLMYIn2m4hd1r7kfS39yytOowyx2zVWMzpjCcpPS8BjqkAUiLXtdpLgNidqanTFHJAM0ti0kLPAjo1EJUgjGF43t0oWC2DfUxZ20OZKpbONw17NjUxlxQhpzpzT%2FlMs8H6uSFchlr7nbyQRvKIAsvzaHpV55YgyTrDGjEJeN9xn1kfa%2BnX7wflJ8xaTfFCg%2FU6GM6rcRBy4PqTvF3Xvh1%2FAhrw8ngHLUGVkC4dEBMfKVGb4dPF8%2FmzkMx%2BpelH0MebYFF6Gzg&X-Amz-Signature=8e069251c8c234d58c91600c9ac41762b787c2b35e90c56985e46390f2cb230e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDQOL2WY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BfBiW71pmxf7d%2FdkLSXWN9tKLq2nz5Tiej%2BIfIiLDLQIhAOqbEj88gSv1iOUflOPkWSeeNcypraxBoLw9xGJQ8a4ZKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igykjn%2BUowyjy7OiGw8q3ANB3yLuKsXsOzCyQOZ58oOMPhuURbV1P6Lt1is2cNGYHKwPw%2BfbWDKSS8W1LmsK9AGoCdj7Sv7cOZPWcMaFZu3L2c0fvLrvZtctGPa7rgfFk9dL9gBPBpND8HkyTWLjKAtaeThg2J7f2znh5Z70CedvFFBQ%2BL8zHEVF6yowF%2FKSoKPlDGZwzKvXfC23uEQrB3B%2B947zfgLw1qry9xX5YoJO95GDpxk5GlowTHFNAZmgdjYth76DZFIRHjjomhzfKbUoF%2FXLOpiHDJd1D5vQfm7kyTume6k%2FACFKXODBE55Vxw8RRPpmMwG%2Fk3zw2B3O%2FvzHoXKpXdUHUVd92tbPH2si2a9bOG6J1BA%2BlWge7CNqC4ZKdPziJ5d9dPSKXznMNGoI94Xh5uQXbK3vqupljEWWMEvneEkX5D0MlWztcjap0rO9omYRfhK5g92aveYmIiPnKr7aSO19%2FHxqdZcN6m57nTZpXTulvG9Zw1sQcX2FNQpMO3z7dnvfhI2YbI%2BzhC3LqIKCQcOa%2FOVHgdaCxLn1FFcjVb3gm2YFxPYFyAx3uCDYMMqFhEnZLCyqXIaDEL%2F4WCaNIVoReAH3Ht%2B%2FWb16keXyLMYIn2m4hd1r7kfS39yytOowyx2zVWMzpjCcpPS8BjqkAUiLXtdpLgNidqanTFHJAM0ti0kLPAjo1EJUgjGF43t0oWC2DfUxZ20OZKpbONw17NjUxlxQhpzpzT%2FlMs8H6uSFchlr7nbyQRvKIAsvzaHpV55YgyTrDGjEJeN9xn1kfa%2BnX7wflJ8xaTfFCg%2FU6GM6rcRBy4PqTvF3Xvh1%2FAhrw8ngHLUGVkC4dEBMfKVGb4dPF8%2FmzkMx%2BpelH0MebYFF6Gzg&X-Amz-Signature=2e14fa0393138fe6be916eec1542ea16dff1cb4978009187b9ff8c216a2a5286&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7SLO3WA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAmXM7BjaFO8C7EhX3cYMxslqsVnbbxCDFluc9Za%2FQttAiEA%2FpEJibh0AiyQjvBY5FZmI9eLl3f%2FT2ixLJFwsvRN6V0qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEXif8w8l8y0gKAloircA1f2jdWixJHJgnP189l3n%2FmsV%2FswcmEf5CCGbcxUFHikcD%2BLmt0emTnnhq%2FVBZXSuVD9JgPR3Id17sk399fRAUJXJpmiUVZxM3qJLqe3r73yr7W7WJVi%2BVBc3zm9OlMOe07wJprxPTV704evzNYGEwB%2B3%2FkV6W6fkjIblI0x4AKjgK6pk12z4jRdEeoFS%2FhSL19ZCiTQaFTOMC2801y2sdaTWODSGYHcBe%2FEGePUf1UuIM8Ueh9zcUaBRp7U0wqeCTJyN1XGV4vjuRq9GTez4e9MnhtgliSBDNLSFPJ0A8oWNEL9ufvFYTxbs020W1mTGS3YOus34nV%2BR8DM0ZWj%2ByZGaWZvEXcDBfwlDXMBp7Kb5FubHLOBDsdimt1qvNPnOnueWd5bRkWrZVU8lKTIZbdlaxMsxtLjX8jtjinm%2BYaiD0%2FQ%2FTatsNTkaTC8VKC8WlmbHIiEbcHb7AIstcBiW3HrcmTR%2BaYyPQjvvwj%2FJvWjCivLVLSytE%2BRDPxLhlZdoRpmU2kYqxuo%2BY0B2ryDYk5jvZDF8uwEsGYHB1KahK2JHxKosvBLBhIi4PwGzh09LPefbtNY1jLahsIeDkwupNFF6gqqZIlXzhNmn5p3kuHt6j0bbim091XD9xrzMM%2Bj9LwGOqUB800dSVVquVLjoEp3hTvLPOFaSZrow8WVRP7NgI6zHaAW0MpYucKh3a%2FfLtyS%2F26%2BtDsnPKjeQ%2FZQyycb8Hp7IPdbEWjq5bwA5oIYIHnQvQxJQa5NEa8VA2zTcsZpofCGVIt09ICQfjjKelBMIQzYR8U5SG%2BweKtb7PCbilQXpMotygi7T1TS7stPeLpGumj6RjGKLwLM3m%2B2W4AocCe9N7ykN8gh&X-Amz-Signature=73aaf9865a9ed144256cb514ce709ed1ef5c57d808ee0e62a2cc008f59da4ec2&X-Amz-SignedHeaders=host&x-id=GetObject)
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