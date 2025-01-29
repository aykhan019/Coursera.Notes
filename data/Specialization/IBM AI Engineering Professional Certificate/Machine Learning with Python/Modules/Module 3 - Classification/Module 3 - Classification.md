

# Module 3: Classification
## Introduction to Classification
Classification is a supervised learning approach used to categorize items into discrete classes. It aims to learn the relationship between feature variables and a target variable, which is categorical.
### How Classification Works
Given training data with target labels, a classification model predicts the class label for new, unlabeled data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ebd9db3c-b793-47e8-9f00-a93662961e2a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X2DK5YG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDallEY17c%2F0UABhVver%2BlB%2FLop%2FSiA%2FZKg87icJTBS1AiEAvQQQEV%2FBfekOK5Wa59WHknRjbhRKENnLAOK3jdqMFlAqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOkJyoQhRT1xZCcpSrcA0KM9B1MoMCNZCsXimhR7Ykv8Npi48Pkx6MGq%2FYaewJp6hTlHSjihzVmSpSEX9AK8UhoetuEnXI9NQ5S6n06FCOImN9YlD1ME2ljkgFVvn8Ec0wquX7knM0XdvoKw2wheR6r2a1Pr11JbpNC0Md7FiKet6Yad6P2rdqk4%2FZdZXazcr3pqW9sGZDwq3w45mUN5CPClVbBFF3UlkYikDN3iyaQkzyd%2B80PueRuqyuTCc3LCfPRvvCFFWkMD0PthA0xiRkwMqkNcibCXJkMweldfICD4cv9fF3skVMIz20a06Hkm0J1rLMZBaX6SfCe3f9jRR8J3%2FKrXiRocU9eUsUMSnz%2BhUV%2BWTPK0AsaPYME6Q7%2Fbed4JHNyUU%2FcKPadX7vCurmfOplcuA1fo5zHUUvaPUO1TNpDUQPBt2FHekZPi8VTMRybfnKa1KWmzifhH1DibESyBLeQ6sqzYI6a%2BPIZco9SMcRfzy5QXLkSF67P9XCDHkgIFFxns6tce3Fi%2BkxA6GmDfZbzFpSxYiCF9p%2BI78S40xC1H2%2F6C2AhfxNPXHDHwu90sTYC6FTHfUwRMxPvfIpwSBS6zXvphpZiA6n%2FbFJuE5Oyr%2B5ZEj7N6w7xQKAmypbiLPiUuDc8INLiMKXM6LwGOqUBoT48SkKVnBXK%2Fzb0dXMRExpaxTbbSQdMLX5RsQf%2Be7O8DKpImxQ3hNEgHp4GvI%2Fod5DpT36XnGO9904fgxlVwYeCt01eGGwbLErda%2BohRgyMtcsr7JKTLA7CHUpBFuZYv4a1N10X0dhKJVjy9hrgIURc7iRFE5PaUG12W%2F231DutlAB5kwkAWeFl81YsEU4QhCpCMvj8X%2BBYLnAXfNvq2XP63a3Z&X-Amz-Signature=c0e74a080ca645ac890cb0eee7f6f02d620424678fa6dafc02ff0ace9daa0686&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example:
A loan default predictor uses historical data (e.g., age, income) to classify customers as defaulters or non-defaulters.
### Types of Classification
#### Binary Classification
Predicts one of two possible classes (e.g., defaulter vs. non-defaulter).
#### Multi-class Classification
Predicts among more than two classes (e.g., which medication is appropriate for a patient).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0a87923-2ee4-4428-9a12-9e906d1d7355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X2DK5YG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDallEY17c%2F0UABhVver%2BlB%2FLop%2FSiA%2FZKg87icJTBS1AiEAvQQQEV%2FBfekOK5Wa59WHknRjbhRKENnLAOK3jdqMFlAqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOkJyoQhRT1xZCcpSrcA0KM9B1MoMCNZCsXimhR7Ykv8Npi48Pkx6MGq%2FYaewJp6hTlHSjihzVmSpSEX9AK8UhoetuEnXI9NQ5S6n06FCOImN9YlD1ME2ljkgFVvn8Ec0wquX7knM0XdvoKw2wheR6r2a1Pr11JbpNC0Md7FiKet6Yad6P2rdqk4%2FZdZXazcr3pqW9sGZDwq3w45mUN5CPClVbBFF3UlkYikDN3iyaQkzyd%2B80PueRuqyuTCc3LCfPRvvCFFWkMD0PthA0xiRkwMqkNcibCXJkMweldfICD4cv9fF3skVMIz20a06Hkm0J1rLMZBaX6SfCe3f9jRR8J3%2FKrXiRocU9eUsUMSnz%2BhUV%2BWTPK0AsaPYME6Q7%2Fbed4JHNyUU%2FcKPadX7vCurmfOplcuA1fo5zHUUvaPUO1TNpDUQPBt2FHekZPi8VTMRybfnKa1KWmzifhH1DibESyBLeQ6sqzYI6a%2BPIZco9SMcRfzy5QXLkSF67P9XCDHkgIFFxns6tce3Fi%2BkxA6GmDfZbzFpSxYiCF9p%2BI78S40xC1H2%2F6C2AhfxNPXHDHwu90sTYC6FTHfUwRMxPvfIpwSBS6zXvphpZiA6n%2FbFJuE5Oyr%2B5ZEj7N6w7xQKAmypbiLPiUuDc8INLiMKXM6LwGOqUBoT48SkKVnBXK%2Fzb0dXMRExpaxTbbSQdMLX5RsQf%2Be7O8DKpImxQ3hNEgHp4GvI%2Fod5DpT36XnGO9904fgxlVwYeCt01eGGwbLErda%2BohRgyMtcsr7JKTLA7CHUpBFuZYv4a1N10X0dhKJVjy9hrgIURc7iRFE5PaUG12W%2F231DutlAB5kwkAWeFl81YsEU4QhCpCMvj8X%2BBYLnAXfNvq2XP63a3Z&X-Amz-Signature=c26255e8089075c686741f9bd7f17f3d39b11f9c0e3e707721781a12e4b6ddee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e36aac8a-7cd7-46a1-abe2-4cec9840fab1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X2DK5YG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDallEY17c%2F0UABhVver%2BlB%2FLop%2FSiA%2FZKg87icJTBS1AiEAvQQQEV%2FBfekOK5Wa59WHknRjbhRKENnLAOK3jdqMFlAqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOkJyoQhRT1xZCcpSrcA0KM9B1MoMCNZCsXimhR7Ykv8Npi48Pkx6MGq%2FYaewJp6hTlHSjihzVmSpSEX9AK8UhoetuEnXI9NQ5S6n06FCOImN9YlD1ME2ljkgFVvn8Ec0wquX7knM0XdvoKw2wheR6r2a1Pr11JbpNC0Md7FiKet6Yad6P2rdqk4%2FZdZXazcr3pqW9sGZDwq3w45mUN5CPClVbBFF3UlkYikDN3iyaQkzyd%2B80PueRuqyuTCc3LCfPRvvCFFWkMD0PthA0xiRkwMqkNcibCXJkMweldfICD4cv9fF3skVMIz20a06Hkm0J1rLMZBaX6SfCe3f9jRR8J3%2FKrXiRocU9eUsUMSnz%2BhUV%2BWTPK0AsaPYME6Q7%2Fbed4JHNyUU%2FcKPadX7vCurmfOplcuA1fo5zHUUvaPUO1TNpDUQPBt2FHekZPi8VTMRybfnKa1KWmzifhH1DibESyBLeQ6sqzYI6a%2BPIZco9SMcRfzy5QXLkSF67P9XCDHkgIFFxns6tce3Fi%2BkxA6GmDfZbzFpSxYiCF9p%2BI78S40xC1H2%2F6C2AhfxNPXHDHwu90sTYC6FTHfUwRMxPvfIpwSBS6zXvphpZiA6n%2FbFJuE5Oyr%2B5ZEj7N6w7xQKAmypbiLPiUuDc8INLiMKXM6LwGOqUBoT48SkKVnBXK%2Fzb0dXMRExpaxTbbSQdMLX5RsQf%2Be7O8DKpImxQ3hNEgHp4GvI%2Fod5DpT36XnGO9904fgxlVwYeCt01eGGwbLErda%2BohRgyMtcsr7JKTLA7CHUpBFuZYv4a1N10X0dhKJVjy9hrgIURc7iRFE5PaUG12W%2F231DutlAB5kwkAWeFl81YsEU4QhCpCMvj8X%2BBYLnAXfNvq2XP63a3Z&X-Amz-Signature=81ec34783172a3f2bf48ee730a29484aea7e8ffb3986cf8b400edec0fd9f997d&X-Amz-SignedHeaders=host&x-id=GetObject)
### How K-Nearest Neighbors Works
1. **Choosing the Number of Neighbors (K)**: The number of neighbors (K) to consider is specified by the user.
2. **Calculating Distance**: For a new data point, the algorithm calculates the distance between this point and all other points in the dataset. Common distance metrics include Euclidean distance.
3. **Finding the Nearest Neighbors**: The K data points that are closest to the new data point are identified.
4. **Assigning a Class Label**: The new data point is assigned the class label that is most common among its K nearest neighbors.
#### Example of KNN Classification
- **Scenario**: A new customer’s demographic data (e.g., age and income) is available. The goal is to classify this customer into one of four service groups.
- **Process**:
	- If K=1, the new customer is assigned the same class as the closest existing customer.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/52e428c2-67d2-47dc-9e61-836eccce6be2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YJNLTHU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGodW6NXT5YwkgHTPes8DysgR5VEgPJc%2FToiHgHLvetdAiEAwJiK9oMywCY%2FjvBOSUGPv4sOq0aRKg5YduHYzP5%2BVKcqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKwmt0mB4HYpN0xKircAwZ49QrPaBi6GLoxa9QONtuEwGkwY2yDjY%2BuGOXL%2By1Fzzb%2FtDbhjrbVKbdjZdWzRO9G%2BerSLIq%2FWF5jEBvTXvL%2Bwmw7PgQiw2v38%2Fls41P461gglKrOmAfh08b5arDN3dQLamlrAGJn9kxeV7u%2BRUQeTTAhW6GffjjasX96BI%2BP9RUnge6mON2YGI4AfPGinX1eVw1Vft7vNuiHpYuoAPNxjn7mRVbkdRL%2FH3u7ZGt3%2BTiAtPFuiAQZi3EthDrXrtPDLryaR39aOnKUcln%2Fu1UQiSxYqxGi7CYZLyv453cuHAEgxor8d8psfMq%2BxS0rCbqzNHgLFw3Krk3zf87Mansn%2B21B1UJrpwL3srrFTlr8lR6UsLNFkOa2Js0awOejxldFaYY0sLUyz3cIAK2nci0tjRm0NNlNs7%2BWLIzAdP0DUI6sRXFF%2F46S7ecGxr8%2FBi2TfmMo8XRkcpgaVV4ru%2FJGn3kQdWwhHyJG3pJkjqh01RC2lS4oKladDQeROvZBZVZfiQWRfpJsJHna4WXYXHv%2BzwtbN1PrnglnXJTskAlROrJvRt%2FXCWWMdj1ggjWOHUjAIAlFPxKEeXvy3%2F5%2FQn%2FgQO7DpRGpCHCc7ZyX%2FDHukTqi36Z8UgREh7tMMN%2FL6LwGOqUB9jHwak1DjGrp5C52Czp8L4nc2OmR%2BAFIlzZyYp3XoYnnIGMIpyVqkWPtMjz6obXYAPwCW%2BcuEWxG%2Bz4OwQJyOSJ2NRNLWlJFFmaEVONqc7%2B%2FnYFxYj9br6CdclhP8vfE4Zd71YIPMPWONT0BG3Se6zK9tqHTRhYcn1O%2BjDAOgGoELNdZaM3R22yFCU%2FPsIbdslg4EEjs%2FL2UNW%2BBEKLZX18NQQQy&X-Amz-Signature=0f51460eb2780a55247a5786c2f8632699aeee1129f3b61dfc4e35335c1ab0b4&X-Amz-SignedHeaders=host&x-id=GetObject)
	- If K=5, the new customer is assigned the class that is most frequent among the 5 nearest neighbors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/43d3ac68-3aef-49d9-8585-3354324ac454/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YJNLTHU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGodW6NXT5YwkgHTPes8DysgR5VEgPJc%2FToiHgHLvetdAiEAwJiK9oMywCY%2FjvBOSUGPv4sOq0aRKg5YduHYzP5%2BVKcqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKwmt0mB4HYpN0xKircAwZ49QrPaBi6GLoxa9QONtuEwGkwY2yDjY%2BuGOXL%2By1Fzzb%2FtDbhjrbVKbdjZdWzRO9G%2BerSLIq%2FWF5jEBvTXvL%2Bwmw7PgQiw2v38%2Fls41P461gglKrOmAfh08b5arDN3dQLamlrAGJn9kxeV7u%2BRUQeTTAhW6GffjjasX96BI%2BP9RUnge6mON2YGI4AfPGinX1eVw1Vft7vNuiHpYuoAPNxjn7mRVbkdRL%2FH3u7ZGt3%2BTiAtPFuiAQZi3EthDrXrtPDLryaR39aOnKUcln%2Fu1UQiSxYqxGi7CYZLyv453cuHAEgxor8d8psfMq%2BxS0rCbqzNHgLFw3Krk3zf87Mansn%2B21B1UJrpwL3srrFTlr8lR6UsLNFkOa2Js0awOejxldFaYY0sLUyz3cIAK2nci0tjRm0NNlNs7%2BWLIzAdP0DUI6sRXFF%2F46S7ecGxr8%2FBi2TfmMo8XRkcpgaVV4ru%2FJGn3kQdWwhHyJG3pJkjqh01RC2lS4oKladDQeROvZBZVZfiQWRfpJsJHna4WXYXHv%2BzwtbN1PrnglnXJTskAlROrJvRt%2FXCWWMdj1ggjWOHUjAIAlFPxKEeXvy3%2F5%2FQn%2FgQO7DpRGpCHCc7ZyX%2FDHukTqi36Z8UgREh7tMMN%2FL6LwGOqUB9jHwak1DjGrp5C52Czp8L4nc2OmR%2BAFIlzZyYp3XoYnnIGMIpyVqkWPtMjz6obXYAPwCW%2BcuEWxG%2Bz4OwQJyOSJ2NRNLWlJFFmaEVONqc7%2B%2FnYFxYj9br6CdclhP8vfE4Zd71YIPMPWONT0BG3Se6zK9tqHTRhYcn1O%2BjDAOgGoELNdZaM3R22yFCU%2FPsIbdslg4EEjs%2FL2UNW%2BBEKLZX18NQQQy&X-Amz-Signature=821555f0d562ebb25ce3d4d26f64d822e44ac381e3f3fc9bfade3c11d7df17c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/70cad103-c369-453a-a601-9beda28c647e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X2DK5YG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDallEY17c%2F0UABhVver%2BlB%2FLop%2FSiA%2FZKg87icJTBS1AiEAvQQQEV%2FBfekOK5Wa59WHknRjbhRKENnLAOK3jdqMFlAqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOkJyoQhRT1xZCcpSrcA0KM9B1MoMCNZCsXimhR7Ykv8Npi48Pkx6MGq%2FYaewJp6hTlHSjihzVmSpSEX9AK8UhoetuEnXI9NQ5S6n06FCOImN9YlD1ME2ljkgFVvn8Ec0wquX7knM0XdvoKw2wheR6r2a1Pr11JbpNC0Md7FiKet6Yad6P2rdqk4%2FZdZXazcr3pqW9sGZDwq3w45mUN5CPClVbBFF3UlkYikDN3iyaQkzyd%2B80PueRuqyuTCc3LCfPRvvCFFWkMD0PthA0xiRkwMqkNcibCXJkMweldfICD4cv9fF3skVMIz20a06Hkm0J1rLMZBaX6SfCe3f9jRR8J3%2FKrXiRocU9eUsUMSnz%2BhUV%2BWTPK0AsaPYME6Q7%2Fbed4JHNyUU%2FcKPadX7vCurmfOplcuA1fo5zHUUvaPUO1TNpDUQPBt2FHekZPi8VTMRybfnKa1KWmzifhH1DibESyBLeQ6sqzYI6a%2BPIZco9SMcRfzy5QXLkSF67P9XCDHkgIFFxns6tce3Fi%2BkxA6GmDfZbzFpSxYiCF9p%2BI78S40xC1H2%2F6C2AhfxNPXHDHwu90sTYC6FTHfUwRMxPvfIpwSBS6zXvphpZiA6n%2FbFJuE5Oyr%2B5ZEj7N6w7xQKAmypbiLPiUuDc8INLiMKXM6LwGOqUBoT48SkKVnBXK%2Fzb0dXMRExpaxTbbSQdMLX5RsQf%2Be7O8DKpImxQ3hNEgHp4GvI%2Fod5DpT36XnGO9904fgxlVwYeCt01eGGwbLErda%2BohRgyMtcsr7JKTLA7CHUpBFuZYv4a1N10X0dhKJVjy9hrgIURc7iRFE5PaUG12W%2F231DutlAB5kwkAWeFl81YsEU4QhCpCMvj8X%2BBYLnAXfNvq2XP63a3Z&X-Amz-Signature=e635439a64ce5e155bc92d1cf79e1ede147b3386c7e9caeb0f7353b3c6225dc7&X-Amz-SignedHeaders=host&x-id=GetObject)
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