

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=2dd8a03430425f470984d0b8895ce5fe3f1165c0e150482e571dba41b426a547&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=08832843949a4bb903dd2cc71f38db30c6a6989be5f647dc67e26d16048dc6fa&X-Amz-SignedHeaders=host&x-id=GetObject)
**Example Code**:
```python
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# X_train: Training data for the predictors
# X_test: Testing data for the predictors
# y_train: Training data for the target variable
# y_test: Testing data for the target variable
# test_size=0.3: 30% of the data will be used for testing, and 70% will be used for training
# random_state=42:Ensures reproducibility of the split. Using the same random state will produce the same split every time
```
### Generalization Error
- **Generalization Error**: Measures how well the model predicts new data. The error obtained using testing data approximates this error.
### Cross-Validation
**Cross-Validation**: A technique to assess the model's performance and estimate generalization error by splitting the data into multiple folds.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=7c6f7acd60be438b7d35566e3f2ef149d73571e12d8eac328337228b47d9c8cc&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=dd38cb404d6634158dd44f9e6ee22041373b5343aacdd24219ce1dadbc42f549&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=500fd2400f5cbc0aadbed76b27d7a54babcbf8a0c47478b99e82ffe94a1bf944&X-Amz-SignedHeaders=host&x-id=GetObject)
### Cross-Val Predict
**cross_val_predict** is used when you want to obtain the predicted values for each test fold during the cross-validation process. It returns the prediction for each data point when it was in the test set. This is useful for:
5. **Visualizing Predictions**: You can plot the predicted values against the actual values to see how well the model performs across the entire dataset.
6. **Diagnostics**: It helps in analyzing the residuals (differences between actual and predicted values) to diagnose model performance.
#### Example in Python
Here's an example using `cross_val_predict`:
```python
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Example dataset
X = np.random.rand(100, 5)
y = np.random.rand(100)

# Initialize the model
model = LinearRegression()

# Get cross-validated predictions
y_pred = cross_val_predict(model, X, y, cv=5)

# Plot actual vs. predicted values
plt.scatter(y, y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Cross-Validated Predictions')
plt.show()
```
In this example:
- `cross_val_predict` returns the predicted values for each test fold during the 5-fold cross-validation.
- A scatter plot is created to visualize the actual vs. predicted values.
#### Summary
- **Training Set**: Used to build the model.
- **Testing Set**: Used to evaluate model performance.
- **Cross-Validation**: Provides a robust estimate of model performance by averaging results across multiple folds.
___
## Model Selection and Polynomial Regression
When selecting the best polynomial order, our goal is to provide the best estimate of the
function $ y(x) $.
### Noise in Data
**Noise** in data refers to random variations or errors that obscure the true underlying patterns or relationships. It can come from various sources and affects the accuracy of models.
### **Underfitting** 
**Underfitting** occurs when the model is too simple to fit the data:
- Example: Fitting a linear function to data generated from a higher-order polynomial plus noise results in many errors.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=bc6f712e0185e41a8afe7e6eadabd170cf3b6eeb278c5397b64343df6f7478c2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=3ee267fae46779b63ef92e655283c7d83d0f01795253efae25c9c3355678906c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=d2bada4a4104bfc9ff0aaf93e5f80988dfd6865cff8a24719e6d981cd027e07d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=469963d0a2786818e5f83bfdc431fedc7f36f802d59e8cd93dc2ffaadb4b0ec5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NLGVP62%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC63ZZdmNM1%2Bp6EhiICAZK6Ozy9UtznapohefrU1vM5sAiEA%2BdfoYlYuVhOeVp82hz9XjomjIRi72hQQrk8vx7g%2BNFEqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPchAbY3S96x5wyN1yrcA8NBPS7RzegLeXuiNQOu9LvIWkQT0U7JQw7cwLtjZkLoq8D94GJgKAVlTqfehLBGmJDsRqXlCf43bZuUT%2FVO41F2RSQ0fzn8gCq%2BuzvW3Paj%2BixuOd4xOeh1bLVVeS50NTb227VnQjZ1UBReVfS6dyHTQttjWz3OwAUlCLhHIPLphFtUqbjkQftQDjx4yxRnELTW6mFJKvbl3%2FoUe6elsyDjEe0d6KkclQ6nws4YIl9UWntUmZlJf4CFAC6mHq5O%2BCzC9ktoxwtNNLNCJHhEcgeLezwUuz%2FzynVigOUjDtYsELOWUJrfMM%2BlJx2BoVlMkhLLYZse8cqwC6slChczjKrTzccrTSq8kP8IyMrjwDSG1hUkCaqbITq0NwBSwkrQHQKb3SSDx%2FjNTZiLOehCuiLSSKb6MAFl9vNltDuvbFYoATt%2FZFO7DG3tqNukJYBeaBy%2BSh8d7t8ZokPkFYeFfqzwbEefKNzCKKgovWKnnH4AthGirE99f3J9svLNLbns5DsNUCYBsnNiIDoL9CluoQhedDGGwuFjQ8fQUZ%2Fll5o%2BAxHk60R9AdsbC80CSbRvxx5kMGCn0zm6iffwUEc7p6GrrxXJmXOALwqM4GsQk0UwB6E%2Bz7qd6AragyHBMNXr7LwGOqUBl10X3tRWe4fZEhvBcbn3CTTeaCHahbMDTgj0d5O1Wqhz9NcUBZSFGhIxutLQBZN8KQ2X5WyIovuOzNwV71zhOzFueH%2BEgXL%2BdqFTOhXI5s0rK%2Bdxkt384xJ9ST2Ny%2FNx43GRwrD8hXOTz%2FiYEBKB86zT8lO8%2FfzbxiogUc3NCQ03Yzs%2B4YEI%2FO6YfZlftZRttEx9MmlKXqNKeXv0qxAyHjmD3hUh&X-Amz-Signature=6f7c33765ff255da4672903fdc937d5a98e7639e87ea9e2c4e688135bae75884&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NLGVP62%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC63ZZdmNM1%2Bp6EhiICAZK6Ozy9UtznapohefrU1vM5sAiEA%2BdfoYlYuVhOeVp82hz9XjomjIRi72hQQrk8vx7g%2BNFEqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPchAbY3S96x5wyN1yrcA8NBPS7RzegLeXuiNQOu9LvIWkQT0U7JQw7cwLtjZkLoq8D94GJgKAVlTqfehLBGmJDsRqXlCf43bZuUT%2FVO41F2RSQ0fzn8gCq%2BuzvW3Paj%2BixuOd4xOeh1bLVVeS50NTb227VnQjZ1UBReVfS6dyHTQttjWz3OwAUlCLhHIPLphFtUqbjkQftQDjx4yxRnELTW6mFJKvbl3%2FoUe6elsyDjEe0d6KkclQ6nws4YIl9UWntUmZlJf4CFAC6mHq5O%2BCzC9ktoxwtNNLNCJHhEcgeLezwUuz%2FzynVigOUjDtYsELOWUJrfMM%2BlJx2BoVlMkhLLYZse8cqwC6slChczjKrTzccrTSq8kP8IyMrjwDSG1hUkCaqbITq0NwBSwkrQHQKb3SSDx%2FjNTZiLOehCuiLSSKb6MAFl9vNltDuvbFYoATt%2FZFO7DG3tqNukJYBeaBy%2BSh8d7t8ZokPkFYeFfqzwbEefKNzCKKgovWKnnH4AthGirE99f3J9svLNLbns5DsNUCYBsnNiIDoL9CluoQhedDGGwuFjQ8fQUZ%2Fll5o%2BAxHk60R9AdsbC80CSbRvxx5kMGCn0zm6iffwUEc7p6GrrxXJmXOALwqM4GsQk0UwB6E%2Bz7qd6AragyHBMNXr7LwGOqUBl10X3tRWe4fZEhvBcbn3CTTeaCHahbMDTgj0d5O1Wqhz9NcUBZSFGhIxutLQBZN8KQ2X5WyIovuOzNwV71zhOzFueH%2BEgXL%2BdqFTOhXI5s0rK%2Bdxkt384xJ9ST2Ny%2FNx43GRwrD8hXOTz%2FiYEBKB86zT8lO8%2FfzbxiogUc3NCQ03Yzs%2B4YEI%2FO6YfZlftZRttEx9MmlKXqNKeXv0qxAyHjmD3hUh&X-Amz-Signature=e6b28207597931e53c49002125f5385fd55908d581697dd0bbf45a4dd72ea869&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NLGVP62%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC63ZZdmNM1%2Bp6EhiICAZK6Ozy9UtznapohefrU1vM5sAiEA%2BdfoYlYuVhOeVp82hz9XjomjIRi72hQQrk8vx7g%2BNFEqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPchAbY3S96x5wyN1yrcA8NBPS7RzegLeXuiNQOu9LvIWkQT0U7JQw7cwLtjZkLoq8D94GJgKAVlTqfehLBGmJDsRqXlCf43bZuUT%2FVO41F2RSQ0fzn8gCq%2BuzvW3Paj%2BixuOd4xOeh1bLVVeS50NTb227VnQjZ1UBReVfS6dyHTQttjWz3OwAUlCLhHIPLphFtUqbjkQftQDjx4yxRnELTW6mFJKvbl3%2FoUe6elsyDjEe0d6KkclQ6nws4YIl9UWntUmZlJf4CFAC6mHq5O%2BCzC9ktoxwtNNLNCJHhEcgeLezwUuz%2FzynVigOUjDtYsELOWUJrfMM%2BlJx2BoVlMkhLLYZse8cqwC6slChczjKrTzccrTSq8kP8IyMrjwDSG1hUkCaqbITq0NwBSwkrQHQKb3SSDx%2FjNTZiLOehCuiLSSKb6MAFl9vNltDuvbFYoATt%2FZFO7DG3tqNukJYBeaBy%2BSh8d7t8ZokPkFYeFfqzwbEefKNzCKKgovWKnnH4AthGirE99f3J9svLNLbns5DsNUCYBsnNiIDoL9CluoQhedDGGwuFjQ8fQUZ%2Fll5o%2BAxHk60R9AdsbC80CSbRvxx5kMGCn0zm6iffwUEc7p6GrrxXJmXOALwqM4GsQk0UwB6E%2Bz7qd6AragyHBMNXr7LwGOqUBl10X3tRWe4fZEhvBcbn3CTTeaCHahbMDTgj0d5O1Wqhz9NcUBZSFGhIxutLQBZN8KQ2X5WyIovuOzNwV71zhOzFueH%2BEgXL%2BdqFTOhXI5s0rK%2Bdxkt384xJ9ST2Ny%2FNx43GRwrD8hXOTz%2FiYEBKB86zT8lO8%2FfzbxiogUc3NCQ03Yzs%2B4YEI%2FO6YfZlftZRttEx9MmlKXqNKeXv0qxAyHjmD3hUh&X-Amz-Signature=26e906e207f025a783115068d99c9cd08ed6894ca42b74fdbd27bd7983b2ff88&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=50b18d779a20fdefac33cbe8c3e2b622a8f6077d4bd71a52cb2a8ba316f28a2a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Calculating R-squared Values**
7. Create an empty list to store R^2 values.
8. Create a list of different polynomial orders.
9. Iterate through the list using a loop:
	- Create a polynomial feature object with the order as a parameter.
	- Transform the training and test data into polynomial features using the `fit_transform` method.
	- Fit the regression model using the transformed data.
	- Calculate the R^2 value using the test data and store it in the list.
Here's an example of how you can implement this in Python:
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# Store R^2 values
r2_values = []

# List of polynomial orders
orders = [1, 2, 3, 4]

# Iterate through polynomial orders
for order in orders:
    # Create polynomial features
    poly = PolynomialFeatures(degree=order)
    x_poly = poly.fit_transform(x.reshape(-1, 1))

    # Fit the model
    model = LinearRegression()
    model.fit(x_poly, y)

    # Predict and calculate R^2
    y_pred = model.predict(x_poly)
    r2 = r2_score(y, y_pred)
    r2_values.append(r2)

# Plot R^2 values
plt.plot(orders, r2_values, marker='o')
plt.xlabel('Order of Polynomial')
plt.ylabel('R^2 Value')
plt.title('R^2 Value vs. Polynomial Order')
plt.show()
```
Output:
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=01ec36b3cb2b288dd08c88d31a813af0db24df98010478ce0c958a39027dd456&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=91461c5a8abf7bff6d8ea06f592f0f960ca98d7a4050115dc92ec62a31d2415f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=e83f8adbe396ce8741a4b31e3c82d0a1903295ea7e9bf6c3560727a2b490ef67&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=aa2e8e1f1503db1f703c0be733234c980a0064e1a96fff5de19021a65470a4ab&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RI6RU5IP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPv4N%2FnLN8D2J3FfFXbssE1JaG16o303fZ23p3ImVaYgIhAJ9TJfXoVVzc7B7rgOpdGCAE8ZgQOo3Wn%2FnNCBQKKd3gKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUVTWyG%2FUaLFNuJqQq3AOT2ZpSJLdFjOp4G4oHpDYJET30W0gmRbZjqNvpP%2BUVaj6kJqFMelysaB%2B6rzvWz9i%2FxwTfZSW%2FIFG5PWv%2BNYd9zPpHVhGuMQ00FPUeM0PrsFGDgSfzdT3GiiB6HAHSQsqXzd3xd%2FJB7JHtW0lu1zOkFrd4jdh3Unl7wGvJcd3QIG%2B0uruvwuITktsiEPSE%2BgE0uLrB7O2a9CSdLVrX1t6LuS61RdENsaopUsAoi4Hqcia6lW38GiozSZT2Ma026o9vYzkuD04lhWXRBlr6Cv3vUyozhYGjVN6ltIM4YTjIAdBneirWv9f1ybZ%2BSjwNoJ36%2F0oiW%2BYL7M8ftPLLuWbDZDunRWu56ROCVpMue1h7N%2FKy%2Fx9wOFwnTLu78TY0fwmWg0rElTG6IUmICAYUhLEVPyxNOkhQVTcgfgjHCXmYjPMCVn1KSmIQIJDDVVYH%2FSkfKiGqlDkGt8%2BPAN%2FVHD23z7OhKK85gyTiKdJ9zxn2JVSFaJGvYWUPvsVBBM3a74vFchI7%2FaL3rOYyPGr72%2BNZHOAUZ1nYXyNgvSOS%2BcqdTY71%2FW%2BLcOxbR95MjnADMggPqN4ltDIUrK7Kct27seInMxGR2YSsSBN00Ed7yEoFOb24rV1VcYrXTX%2FVzTCP6%2By8BjqkASt5fryoEBNXT95wC0Dx5y%2BAEhqvBVd80o2vJrnB9Rtbs6MukK4v0aGEnDMcEXBMPZCyDEOIWp4tZpwq5HQsEkWRrL7xJLn7pozmtbeCJUa%2BpkoOG4wuMhNlVEOcPX4n%2BCm7HcHwzDHgyn0dIySwjEaXodOj%2FH0b71gAclkPWwEH8SMg136wJtk%2FHldjOszBfvjO8zbMQIuBFFIffeg7EYr5K0Jf&X-Amz-Signature=08daabe88713e5d6a5ad818c28041e8b4e2f2b3da37b2059835e0e1f5cb4ccb0&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3NJL2TT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMK32JTEaCHHd%2BPKKGQ7TAK%2FZk0%2BR5DB0EDw%2FhB4gU5gIgTZ1XrUfgom9WXHkAtc98lJDYzUxAf6qJmVR%2FRYjKE5QqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLh87UhVq0CdbSgw8ircA87nulxizegu5qXSEoc640n%2Bxouc4TUdKxnDOqwsJ1hwwN4rLlOPKQquvWGqnnFgVNMIrCJfN%2FfiEnFCov5OsdJTSBcHjLnFsCaXaLM01sXPnGsOfLobdlzZTPmct0%2FADUe58z9ZnJproZNggaKRmOu3ZI7QxKtVwYyRZoNo2FVk8%2BX4lKjvxGhJfYFJJOIw0fM5BO%2FGW6PM3rkuwHmA3KLXELbTKgxtQTqIuBprvIKtq1kMl%2FIjjrE5lRdR%2FplmF5GD%2B9yhMQTNp3WRFyKVANVzNdIIlp4UXCTEdog7WaPdeRWyUdmWY7FJErDjlGW%2F3rQfnPw5otEnYskZ0DIMsUXA%2BV0sM3BCHtxt1bL3HvFjsSwSscTZvRUdzaVi6YDQ70X5lfRnu9YOI8iCgblvexl%2F41LU28Miz7b4p2U28XDJ2NqcyPz0K7SCfNbKP1b1x0q2VKNii8H5Fyc2d1jPoc3E00rZzrXgj2ZXnXKG9jwtfC7X2RnHNJSjyUOmo6E2JEqviPq07R2EFSNNgi4tmVweeWVafSpZzbNxYQG%2FnTJW5aNLduKDacIBaZ3EDuvmMcK59tbJD%2BNipfZA35asQW3yAvenF%2FBrusRssndYPAeQs2kARTxIdNRsoLFJMNDr7LwGOqUBVgeRW2Ce3jyv%2Bd4Z%2BYe9QYMnav2KuDM8RVyyqT8i4d7yKuZBGoqDXs6n2UN9mlTR3k44k0b8qTulny9exK%2F%2BJu9zLNH3Kb7ThYiu%2BcY2o2wSQJvMv138fBwmAUiC%2FQmxHiW%2FAhCtg5t%2BOD61a7SoSuc0U4SwOrlQvRASPu3dma6TqOQgGeYh0ATfP2Gq8PIXQd1YSwdmbl%2BM0Ep54N3yBPE%2FgxlZ&X-Amz-Signature=70301c8dacbb13b4d32d82d1f53c90d357b9a404c88f6ed3387e9698b2c9f0ce&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3NJL2TT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMK32JTEaCHHd%2BPKKGQ7TAK%2FZk0%2BR5DB0EDw%2FhB4gU5gIgTZ1XrUfgom9WXHkAtc98lJDYzUxAf6qJmVR%2FRYjKE5QqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLh87UhVq0CdbSgw8ircA87nulxizegu5qXSEoc640n%2Bxouc4TUdKxnDOqwsJ1hwwN4rLlOPKQquvWGqnnFgVNMIrCJfN%2FfiEnFCov5OsdJTSBcHjLnFsCaXaLM01sXPnGsOfLobdlzZTPmct0%2FADUe58z9ZnJproZNggaKRmOu3ZI7QxKtVwYyRZoNo2FVk8%2BX4lKjvxGhJfYFJJOIw0fM5BO%2FGW6PM3rkuwHmA3KLXELbTKgxtQTqIuBprvIKtq1kMl%2FIjjrE5lRdR%2FplmF5GD%2B9yhMQTNp3WRFyKVANVzNdIIlp4UXCTEdog7WaPdeRWyUdmWY7FJErDjlGW%2F3rQfnPw5otEnYskZ0DIMsUXA%2BV0sM3BCHtxt1bL3HvFjsSwSscTZvRUdzaVi6YDQ70X5lfRnu9YOI8iCgblvexl%2F41LU28Miz7b4p2U28XDJ2NqcyPz0K7SCfNbKP1b1x0q2VKNii8H5Fyc2d1jPoc3E00rZzrXgj2ZXnXKG9jwtfC7X2RnHNJSjyUOmo6E2JEqviPq07R2EFSNNgi4tmVweeWVafSpZzbNxYQG%2FnTJW5aNLduKDacIBaZ3EDuvmMcK59tbJD%2BNipfZA35asQW3yAvenF%2FBrusRssndYPAeQs2kARTxIdNRsoLFJMNDr7LwGOqUBVgeRW2Ce3jyv%2Bd4Z%2BYe9QYMnav2KuDM8RVyyqT8i4d7yKuZBGoqDXs6n2UN9mlTR3k44k0b8qTulny9exK%2F%2BJu9zLNH3Kb7ThYiu%2BcY2o2wSQJvMv138fBwmAUiC%2FQmxHiW%2FAhCtg5t%2BOD61a7SoSuc0U4SwOrlQvRASPu3dma6TqOQgGeYh0ATfP2Gq8PIXQd1YSwdmbl%2BM0Ep54N3yBPE%2FgxlZ&X-Amz-Signature=c8826e957330e856ffd8792590f9d082cb494456abb543a9a46999f3e838577b&X-Amz-SignedHeaders=host&x-id=GetObject)
12. **Model Training**:
	- **Procedure**: Use cross-validation to select the optimal Alpha. Split the data into training and validation sets.
	- **Steps**:
		1. **Train Model**: Fit the model using different values of Alpha.
		2. **Predict & Evaluate**: Use validation data to make predictions and calculate the R^2 or other metrics.
		3. **Select Alpha**: Choose the Alpha that maximizes the R^2 on validation data.
13. **Implementation in Python**:
	- **Import**:
```python
from sklearn.linear_model import Ridge
```
	- **Create & Fit Model**:
```python
ridge = Ridge(alpha=1.0)  # Set the desired alpha value
ridge.fit(X_train, y_train)
```
	- **Predict**:
```python
y_pred = ridge.predict(X_test)
```
14. **Cross-Validation**:
	- **Purpose**: Used to determine the best Alpha by comparing performance metrics (e.g., R^2) across different Alpha values.
	- **Process**: Train with various Alpha values, evaluate with validation data, and select the best-performing Alpha.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXHUQNLH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjs%2BVEattGWT6OWchnHiv%2BKXvDVK%2BLCFSRv4POPaY5HAiAsYTy38m1YI1mkUzDXm6Ljr1F%2B0mnFTtdwjkX9bp2U4SqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGZO%2B82LYnsNIEjTFKtwDek%2Fm8GttlqPzbNFcyMqBiTCb9XIQ3pX9FXRnrXSOlHcqNM9XSlBMc%2FMnSf%2FyBeTfUZgtoXwXYzCHDOX7D1QuBw0rxfLX6GH3dI2yZ6oYaVRj88Qi2NiAmslxCHHxWkAnaZ4DtXWCTILF9hKgRia9Z9Qtqgef%2BV5geazEZ1b%2FWsuPXmsKiwxp1xrXDvKAiOOx%2BdvkiBir8r%2B2o67FBRkm%2Bb2AEEWR2NV6f2Pi%2Bq3ZDkIhyxfO%2BGtt%2BgwbuT2ZI0VsZtqvB1wUhFutID6QSO7%2B4piYWEXhCUxwPDdV9%2FL1utNTQfHjvB30OIcYgesUI6TbiaEcb7RdtOK2tHDLF7BqfLSFXsPxJJXw5atPsoHL6f3ZGLdwiOPqBqwM%2FzCkaWgltvRlUcxw191BOBmfvyaRzoonXNHYin6c%2FEVnxMGAvOCjR9fmFoD3ZH7zuQ9aktjk5LM7hWQeOVBNg1a5Oq9h9lYn4C94dOdHvM4IlNgoB4nrDGnn0lX6AWnT2ubmaNzAQ2YmbyPqqoCaFoIpbRYjKi2ekkDp39MxT22qusWPdKRBR7QLS5xp%2FqcaOixSYUF2R0Smgj1y41MzlPYlCYUtpjz0D7qPFVG8806ZaVUSeFUAEYVW3DmKrpc%2B0qkwoevsvAY6pgH0FIoy8AONcX6O%2BaIvdnatWrR4dFR%2BbjGDBm4kCKH6SVy9c8ksB55CGTmsP8mxNzYtA1A%2BImb7%2FQSLwg9SY5zjRBLi9E84rc6u3Gxp62R%2B9g%2FsQ2%2FlqPrV4BuwWp2owTvKTU6jfzMeL4d2mk7RB3q1b1IRggJKaEyf0Tg8BJ1nUP9LU3sgLHG64FzCLx2RiVXTfG8P1e%2FZcnxuJsXdDlPvrtJMgltq&X-Amz-Signature=05a6e64723b7f7de588d63f686cab06ed85d0b2b0481ed10e5e7ff2a77c838a4&X-Amz-SignedHeaders=host&x-id=GetObject)
15. **Example Visualization**:
	- **Plot**: Shows R^2 values vs. different Alpha values for training and validation data.
	- **Interpretation**:
		- **Training Data**: R^2 might increase with Alpha but eventually converge.
		- **Validation Data**: R^2 may decrease with high Alpha due to reduced model flexibility.
___
## Grid Search for Hyperparameter Tuning
### **Grid Search**
A method for finding the best hyperparameters for a model by systematically evaluating different combinations.
- **Hyperparameters**: Values like Alpha in Ridge Regression that are not learned from the data but set before the training process.
- **Process**:
	1. **Define Hyperparameters**: Set up a grid of hyperparameter values to test. For Ridge Regression, this might include values for Alpha and normalization options.
	2. **Train and Evaluate**: Train the model using each combination of hyperparameters. Evaluate each model using cross-validation, typically using metrics like R² or Mean Squared Error (MSE).
	3. **Select Best Parameters**: Choose the hyperparameters that give the best performance based on the evaluation metric.
### **Implementation in Scikit-learn**
```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25])

# Define parameter grid
param_grid = {
    'alpha': [0.1, 1, 10],
    'normalize': [True, False]
}

# Initialize Ridge model
ridge = Ridge()

# Initialize GridSearchCV
grid_search = GridSearchCV(estimator=ridge, param_grid=param_grid, scoring='r2', cv=5)

# Fit GridSearchCV
grid_search.fit(X, y)

# Get best parameters
best_params = grid_search.best_params_
best_score = grid_search.best_score_
best_estimator = grid_search.best_estimator_
cv_results = grid_search.cv_results_

# Results
print("Best Parameters:", best_params)
print("Best Score:", best_score)
print("Best Estimator:", best_estimator)
print("CV Results:", cv_results)
```
**Example Result:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QXQX7OW%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUzO2HiFDYYlwaDLujs0JQIdYcRP%2Bd%2FFEFdUKC16dzhAiAzUTFWbL0pK2BlLHeDCD96nYu1HCFSulxbd7ePzmPjQiqIBAih%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcifJkxcrF3yKwzP9KtwDVRLYlqflBZEFLr3pkBW7m9d5aROY5hYtjR9QUTwmqvOgiLoJbhg9qo1jRkq%2FoHsLR9xOeoM2MOVAVkijVgcBTVbo2YGt2KvaHCrh8xh0a%2FObgW05fBY%2F9EnopWdbzZ3Fev1gz%2Fco3ww0B1Xi%2F6Nfg4%2FBiXrC8%2Ba7Et9uJpQmwQ6G%2BexgpunGGSDgZ6OYMcZe1yB4ssmT%2BIe8UkDUS%2FFwKVTKrBKRqG2qU%2BNV3O%2BIPZvpCwCx4zklpP5rggOMvzsrQY%2BO7jMbY4PW4Wi1F8EYEZU%2FWNZ9IckqqzywyT8PFvjH8%2BdouEBwrWkulozsALsJPyrmy44VFW6HY7uZ%2BqsslBSGBpuhpr%2BKn%2BQwQAbkPOa4yPgj6aSsMxBdm78AaOW54jtLWm2k6fMxbs6IL1YB6qh4hqxsRLApvLspEKKH3LpCbI68euzqdUId5A3a%2BkEEWt9%2Fm%2Fsv%2FCPF6bFlv4bdW5tmLKd2fSdMRdp0muQgf5ipjV0qCmzvn%2BUBE%2F4ZZtvZ4dlqxSvJbsAnqncazGjh1%2FlLMooF0855bACJfscO2RZvob7KHIWwMbRQ0sHBc16x5i0CcUpbYpKHu8rOv6snDpoVD7P5wk2uckpcaS7tA3m5kgqurYXyQoHW%2FgUw2%2BvsvAY6pgHHrDWbMHm6PNEU70A69Fg9O5CBcZbDi2VylfGhbAfyZ4Wgp%2BY71aS05stVnYnSWxPfSdQF8Yr66NB8cUQnvkAUPGTnspETFaWypgnuq5bjWzYoFZTebztC%2Foa5CP1E2pyhQwmg1CILNZ8qOt5tOeNwmHTKPZm18VUQgVmfBz%2Bu8%2FG7o3Y6rw%2BIbUmMFmByP5hLaJndNjMpJAVhQjHq3ZBTe%2BHes0Ai&X-Amz-Signature=47c3b52c00a33e9e8a90c4c8a07103f999713f2596a6d7c4ab0cbe9ee8105b0c&X-Amz-SignedHeaders=host&x-id=GetObject)
- **Key Attributes**:
	- `**best_estimator_**`: Best model found.
	- `**cv_results_**`: Detailed results for each hyperparameter combination, including scores and parameters.
- **Advantages**: Efficiently explores multiple hyperparameter values to find the best combination, reducing the manual effort required for model tuning.
___
## Cheat Sheet: Model Evaluation and Refinement
### Splitting Data for Training and Testing
The process involves separating the target attribute from the rest of the data, treating it as the output, and the rest as input. Then, split these into training and testing subsets.
```python
from sklearn.model_selection import train_test_split

# Define target and features
y_data = df['target_attribute']
x_data = df.drop('target_attribute', axis=1)

# Split into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.10, random_state=1)
```
### Cross Validation Score
Cross-validation involves creating multiple subsets of training and testing data to evaluate the model’s performance using the R² value.
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Initialize the model
lre = LinearRegression()

# Perform cross-validation
Rcross = cross_val_score(lre, x_data[['attribute_1']], y_data, cv=n)

# Calculate mean and standard deviation of scores
Mean = Rcross.mean()
Std_dev = Rcross.std()
```
### Cross Validation Prediction
Generate predictions using a cross-validated model.
```python
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression

# Initialize the model
lre = LinearRegression()

# Perform cross-validation prediction
yhat = cross_val_predict(lre, x_data[['attribute_1']], y_data, cv=4)
```
### Ridge Regression and Prediction
Use Ridge regression to create a model that avoids overfitting by adjusting the alpha parameter and making predictions.
```python
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures

# Initialize polynomial features
pr = PolynomialFeatures(degree=2)

# Transform features
x_train_pr = pr.fit_transform(x_train[['attribute_1', 'attribute_2']])
x_test_pr = pr.transform(x_test[['attribute_1', 'attribute_2']])

# Initialize Ridge model
RigeModel = Ridge(alpha=1)

# Fit the model
RigeModel.fit(x_train_pr, y_train)

# Make predictions
yhat = RigeModel.predict(x_test_pr)
```
### Grid Search
Use Grid Search to find the optimal alpha value for Ridge regression by performing cross-validation.
```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

# Define parameter grid
parameters = [{'alpha': [0.001, 0.1, 1, 10, 100, 1000, 10000]}]

# Initialize Ridge model
RR = Ridge()

# Initialize GridSearchCV
Grid1 = GridSearchCV(RR, parameters, cv=4)

# Fit GridSearchCV
Grid1.fit(x_data[['attribute_1', 'attribute_2']], y_data)

# Get the best model
BestRR = Grid1.best_estimator_

# Evaluate the model
score = BestRR.score(x_test[['attribute_1', 'attribute_2']], y_test)
```
___