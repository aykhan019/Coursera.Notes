

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWIPDRM3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIEjhYG0QlXWBf%2Bt0r2ZGhW4IMozBbjGF1q8Y%2BYupNfenAiEArO7dO65KTeR0wS%2BhA3WXWz%2FHQjGH9dPtnTSOMiRmDCwq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDL9smVSepsDpTjHCxSrcA1kApagaubqqBqYblnGx6kyzAYEwgWehlTdm2uAyKjnPrmruGeGFVY6xEoymLdxYco00YgdAvk1zBVuajxkr0tB5B1oSbr8kGiHuddQzb9REZQqMOeLENrWe5vBLcNzYMlSW3EJYKLWwqC%2FA2AuclzGeDeH2T%2F8GUkb4V1dpj8Rv2BW9cHTZyXEm93rgOxN%2FfLh%2FZSRc62SanrfkTd9epb0j2t9dT33u3VLlYnTn%2B%2FE9CYUnMFgScr2L8pziJXMMnZJsi1DUlRfshmGVkgoJmq%2FsvEl8mICsQmYrQj3WKbEBHGcTmYveFLm4%2B6xTHJ0C1yxmoq%2BccrzYB9tO6hKT7wK%2FsVob22XVDFNCuB9yDMHEu8Fp2wCg4d7cCAFwVBy5fIJj25k6y%2Bj7QqZ6IWHTarPPHLhNdnjX0OWB0z0FAuTnwfOC31sRIAXAhOsPH3MaxAP0tE%2FJTRZxVUWlO6vZ4a%2BXKY0BuvNlkI5c3oxMpQeNND66V6mbqj1wsDsQ3uLZdAlq27pAlMSuLiid8cd5e3wF0j6s7P2hGUh%2BnYdj3I23ggnMQEOGuHw2FU4EZIP1JUF1J6ja0jxA8%2Bj5ayye85gBLTdp7HMv5q%2F5a1APcNziuNzvx9fAJJs7Unu9MIXaj70GOqUB3IPhdCUCSVZRF%2BXgMvSBjQj9AV9kiUVFHDWAi4yjLHjEcqBYadP93oSnZfsjYaDgUiDFAmn5OlLELrSwPIMbZJ6COdhNhYtOzE5N2AhSsPvBymUepKvHEIxJ3x7TiipCtEdHeEblwhDD86N%2Fym0kHCiJRWbPl%2F2AWKYSjxay4lqm130jjDqVml%2BT56xgUAeQqJLIf7Y52UhV2GGno%2BBZ52Pqyx4h&X-Amz-Signature=507e40deafd7256012692961573edb8521a58304eb8ae986a810caba6baeea9a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWIPDRM3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIEjhYG0QlXWBf%2Bt0r2ZGhW4IMozBbjGF1q8Y%2BYupNfenAiEArO7dO65KTeR0wS%2BhA3WXWz%2FHQjGH9dPtnTSOMiRmDCwq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDL9smVSepsDpTjHCxSrcA1kApagaubqqBqYblnGx6kyzAYEwgWehlTdm2uAyKjnPrmruGeGFVY6xEoymLdxYco00YgdAvk1zBVuajxkr0tB5B1oSbr8kGiHuddQzb9REZQqMOeLENrWe5vBLcNzYMlSW3EJYKLWwqC%2FA2AuclzGeDeH2T%2F8GUkb4V1dpj8Rv2BW9cHTZyXEm93rgOxN%2FfLh%2FZSRc62SanrfkTd9epb0j2t9dT33u3VLlYnTn%2B%2FE9CYUnMFgScr2L8pziJXMMnZJsi1DUlRfshmGVkgoJmq%2FsvEl8mICsQmYrQj3WKbEBHGcTmYveFLm4%2B6xTHJ0C1yxmoq%2BccrzYB9tO6hKT7wK%2FsVob22XVDFNCuB9yDMHEu8Fp2wCg4d7cCAFwVBy5fIJj25k6y%2Bj7QqZ6IWHTarPPHLhNdnjX0OWB0z0FAuTnwfOC31sRIAXAhOsPH3MaxAP0tE%2FJTRZxVUWlO6vZ4a%2BXKY0BuvNlkI5c3oxMpQeNND66V6mbqj1wsDsQ3uLZdAlq27pAlMSuLiid8cd5e3wF0j6s7P2hGUh%2BnYdj3I23ggnMQEOGuHw2FU4EZIP1JUF1J6ja0jxA8%2Bj5ayye85gBLTdp7HMv5q%2F5a1APcNziuNzvx9fAJJs7Unu9MIXaj70GOqUB3IPhdCUCSVZRF%2BXgMvSBjQj9AV9kiUVFHDWAi4yjLHjEcqBYadP93oSnZfsjYaDgUiDFAmn5OlLELrSwPIMbZJ6COdhNhYtOzE5N2AhSsPvBymUepKvHEIxJ3x7TiipCtEdHeEblwhDD86N%2Fym0kHCiJRWbPl%2F2AWKYSjxay4lqm130jjDqVml%2BT56xgUAeQqJLIf7Y52UhV2GGno%2BBZ52Pqyx4h&X-Amz-Signature=ac8b6acfc5568091dfb34bae7773958c9619995ea1f96f7597d2efb38c923683&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWIPDRM3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIEjhYG0QlXWBf%2Bt0r2ZGhW4IMozBbjGF1q8Y%2BYupNfenAiEArO7dO65KTeR0wS%2BhA3WXWz%2FHQjGH9dPtnTSOMiRmDCwq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDL9smVSepsDpTjHCxSrcA1kApagaubqqBqYblnGx6kyzAYEwgWehlTdm2uAyKjnPrmruGeGFVY6xEoymLdxYco00YgdAvk1zBVuajxkr0tB5B1oSbr8kGiHuddQzb9REZQqMOeLENrWe5vBLcNzYMlSW3EJYKLWwqC%2FA2AuclzGeDeH2T%2F8GUkb4V1dpj8Rv2BW9cHTZyXEm93rgOxN%2FfLh%2FZSRc62SanrfkTd9epb0j2t9dT33u3VLlYnTn%2B%2FE9CYUnMFgScr2L8pziJXMMnZJsi1DUlRfshmGVkgoJmq%2FsvEl8mICsQmYrQj3WKbEBHGcTmYveFLm4%2B6xTHJ0C1yxmoq%2BccrzYB9tO6hKT7wK%2FsVob22XVDFNCuB9yDMHEu8Fp2wCg4d7cCAFwVBy5fIJj25k6y%2Bj7QqZ6IWHTarPPHLhNdnjX0OWB0z0FAuTnwfOC31sRIAXAhOsPH3MaxAP0tE%2FJTRZxVUWlO6vZ4a%2BXKY0BuvNlkI5c3oxMpQeNND66V6mbqj1wsDsQ3uLZdAlq27pAlMSuLiid8cd5e3wF0j6s7P2hGUh%2BnYdj3I23ggnMQEOGuHw2FU4EZIP1JUF1J6ja0jxA8%2Bj5ayye85gBLTdp7HMv5q%2F5a1APcNziuNzvx9fAJJs7Unu9MIXaj70GOqUB3IPhdCUCSVZRF%2BXgMvSBjQj9AV9kiUVFHDWAi4yjLHjEcqBYadP93oSnZfsjYaDgUiDFAmn5OlLELrSwPIMbZJ6COdhNhYtOzE5N2AhSsPvBymUepKvHEIxJ3x7TiipCtEdHeEblwhDD86N%2Fym0kHCiJRWbPl%2F2AWKYSjxay4lqm130jjDqVml%2BT56xgUAeQqJLIf7Y52UhV2GGno%2BBZ52Pqyx4h&X-Amz-Signature=db467af4e167870a87c5a8141b310a22f06f03505df33e23712e914392748381&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZN3RAYT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIQCGJWqJyDXV7JWZN%2B0pdsAcA8sfuN%2B2tp5KkINTqEH6BQIgUsl2F3wq04ECgh4zlBXODNo9B%2BxaWL2n8XKqnX2cNswq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDLezhGu1lO1rC2bwMircA0aCK9zHwdKg9ecwMeiy9K2xQO3sggnz5%2F0pNsCd6Lsu%2B12fT94rWfhb4zHlf800NeHRbyPvlZ7xVcKXLsJpJ2KMBv4dmRLym81ZojlEpuKghdUMgen%2BpJxKwT729WPbhAFSSIsx3ro78DLbGH%2FyqO3xhgFuMuhZT0YwNRV7N39MNE52CNmhTdZkeV2t90Tz%2FEj9atoxH5YEt%2B2uSc3X9ZNgZoh28e6%2F0vhfPgNYUz%2BZF5K4qyXTSWVnsU6JDtGXT5repABE%2BT2uu5QAWlbBgpsxqvOCWYDQKHN%2FwMgbKPGTZ%2BeItyKdjtNkN2GEPespRDYcflGG4y5fClMoJ1XmYC34Np8mlYv9BJqKe33Ls2zAqo6Ub4mRtgVvcyjVlEJbJpZLyIIqEE27%2FhkOlqSjJUaiNkMkyIWnO6UogrKnbaj8Sy9cVmpKU%2B8nLaXrTZucO8wdRLDMz2%2BkcnygBwHhwM4Hqn167ggr376GGFYcPOblqzzAmmAvT2QD8k15%2BluKsbFe96hkVf9%2Buy9CUVH0SGeMvXdsIiXDJeB1GbmAS2fv7kyK8r%2BDcQW%2B0eVS4IExXQ5ZlXwZcnbzJsEDU07qHfCPkjfJmVMewtG5UTyVf5f4U78c8cAQqZpsPyJ7MLLej70GOqUBy8wFWBTQiPjVRCImGQ3a9SsDyfvZ1vnyHXOhP8AHMOreieEgrve02jfPVuATJqKsIkF0TTBuPyrvzMEoOLGbcxmUOI6mSZqoHtMHhZBLkReJZISiaZPMXYijao1Z%2BkkzPqa4dlSnHNrgr6BfTZc9KsRUlVUYTANTevHc%2FXh0VPj5nencQnokFcFIG7RoD44PHeR3VBguCbyaaJtiGHAh7lnBVfyc&X-Amz-Signature=8eb5ebc1762caf462fdccc3f0bdb01d93cc0743989709a7f3c1e67080f1aecae&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZN3RAYT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIQCGJWqJyDXV7JWZN%2B0pdsAcA8sfuN%2B2tp5KkINTqEH6BQIgUsl2F3wq04ECgh4zlBXODNo9B%2BxaWL2n8XKqnX2cNswq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDLezhGu1lO1rC2bwMircA0aCK9zHwdKg9ecwMeiy9K2xQO3sggnz5%2F0pNsCd6Lsu%2B12fT94rWfhb4zHlf800NeHRbyPvlZ7xVcKXLsJpJ2KMBv4dmRLym81ZojlEpuKghdUMgen%2BpJxKwT729WPbhAFSSIsx3ro78DLbGH%2FyqO3xhgFuMuhZT0YwNRV7N39MNE52CNmhTdZkeV2t90Tz%2FEj9atoxH5YEt%2B2uSc3X9ZNgZoh28e6%2F0vhfPgNYUz%2BZF5K4qyXTSWVnsU6JDtGXT5repABE%2BT2uu5QAWlbBgpsxqvOCWYDQKHN%2FwMgbKPGTZ%2BeItyKdjtNkN2GEPespRDYcflGG4y5fClMoJ1XmYC34Np8mlYv9BJqKe33Ls2zAqo6Ub4mRtgVvcyjVlEJbJpZLyIIqEE27%2FhkOlqSjJUaiNkMkyIWnO6UogrKnbaj8Sy9cVmpKU%2B8nLaXrTZucO8wdRLDMz2%2BkcnygBwHhwM4Hqn167ggr376GGFYcPOblqzzAmmAvT2QD8k15%2BluKsbFe96hkVf9%2Buy9CUVH0SGeMvXdsIiXDJeB1GbmAS2fv7kyK8r%2BDcQW%2B0eVS4IExXQ5ZlXwZcnbzJsEDU07qHfCPkjfJmVMewtG5UTyVf5f4U78c8cAQqZpsPyJ7MLLej70GOqUBy8wFWBTQiPjVRCImGQ3a9SsDyfvZ1vnyHXOhP8AHMOreieEgrve02jfPVuATJqKsIkF0TTBuPyrvzMEoOLGbcxmUOI6mSZqoHtMHhZBLkReJZISiaZPMXYijao1Z%2BkkzPqa4dlSnHNrgr6BfTZc9KsRUlVUYTANTevHc%2FXh0VPj5nencQnokFcFIG7RoD44PHeR3VBguCbyaaJtiGHAh7lnBVfyc&X-Amz-Signature=dddbc5a81a78074288dc849522c019ccb94acfac646fe62388aedb7d88321228&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWIPDRM3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIEjhYG0QlXWBf%2Bt0r2ZGhW4IMozBbjGF1q8Y%2BYupNfenAiEArO7dO65KTeR0wS%2BhA3WXWz%2FHQjGH9dPtnTSOMiRmDCwq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDL9smVSepsDpTjHCxSrcA1kApagaubqqBqYblnGx6kyzAYEwgWehlTdm2uAyKjnPrmruGeGFVY6xEoymLdxYco00YgdAvk1zBVuajxkr0tB5B1oSbr8kGiHuddQzb9REZQqMOeLENrWe5vBLcNzYMlSW3EJYKLWwqC%2FA2AuclzGeDeH2T%2F8GUkb4V1dpj8Rv2BW9cHTZyXEm93rgOxN%2FfLh%2FZSRc62SanrfkTd9epb0j2t9dT33u3VLlYnTn%2B%2FE9CYUnMFgScr2L8pziJXMMnZJsi1DUlRfshmGVkgoJmq%2FsvEl8mICsQmYrQj3WKbEBHGcTmYveFLm4%2B6xTHJ0C1yxmoq%2BccrzYB9tO6hKT7wK%2FsVob22XVDFNCuB9yDMHEu8Fp2wCg4d7cCAFwVBy5fIJj25k6y%2Bj7QqZ6IWHTarPPHLhNdnjX0OWB0z0FAuTnwfOC31sRIAXAhOsPH3MaxAP0tE%2FJTRZxVUWlO6vZ4a%2BXKY0BuvNlkI5c3oxMpQeNND66V6mbqj1wsDsQ3uLZdAlq27pAlMSuLiid8cd5e3wF0j6s7P2hGUh%2BnYdj3I23ggnMQEOGuHw2FU4EZIP1JUF1J6ja0jxA8%2Bj5ayye85gBLTdp7HMv5q%2F5a1APcNziuNzvx9fAJJs7Unu9MIXaj70GOqUB3IPhdCUCSVZRF%2BXgMvSBjQj9AV9kiUVFHDWAi4yjLHjEcqBYadP93oSnZfsjYaDgUiDFAmn5OlLELrSwPIMbZJ6COdhNhYtOzE5N2AhSsPvBymUepKvHEIxJ3x7TiipCtEdHeEblwhDD86N%2Fym0kHCiJRWbPl%2F2AWKYSjxay4lqm130jjDqVml%2BT56xgUAeQqJLIf7Y52UhV2GGno%2BBZ52Pqyx4h&X-Amz-Signature=fc7adc6c468696f2abac0c8e5df9930407b6a2d99b5ad09c7b351926e26c835a&X-Amz-SignedHeaders=host&x-id=GetObject)
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