

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=e3c15907c1866d723e2aca5676a345af7bcfc92487ba5f31b502c212195910c2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=f8a0d4763b9a4ee458065e111ab31641b00715ddc25626f6d0355f89d4a5e193&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=f3c5e912286eb920d0f706ee954b3acd6bea3de653ac4afd79cc42c471e59914&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=eb6ad385edd58908c3bbf6f354b41300f2f203696a2c60a56c3cc6bc8017328a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=6a5107bba30f61ef83d207e272b4c074e9bc6974f7ebac8eb56fd36be490fe83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=2f20a46534c9acd4273fa72553e05fbc0ce5933201b2db7ee5b08baae9c42259&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=17e57da399ee2de8753c614e68fd2b3f52233e3d80a2a5c9548fa161c73c2359&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=e68f0856e0b05e009b5403766c396510fea079dedc87732a5bbfd38745e0c5ae&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=f5c0758f7a5ed8a107844006d17e7cf65f3068aad90d96177826311ed2866170&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635A6RZDR%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQDtz%2FIBN8APuutPf1zKBW3R8%2FVHgsXs09vPVP6q9ydDlwIgHu0O0i7CkEpnxnqys74Ad3ffjjqw9%2FC4%2BuYiFDSUZH0q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDPNeBHs53G0qt4AMZCrcA6yahV0vhhOb8EdmCgx39wr7vE9b4spUK2NVqJW%2Fz9Ogr9qRO4Z36vIOfEhMX%2FWVMf1S7QgSYuyj5bxWwLoGQX60NM2ysTUIIguXzwVrK3MVX2WkysZA04bsL4RPxPC5G5Ac9jcZfpOIkgnnpTPR4FBA5PnPlMmfLFdi9JwX2JHZZ7brGcy7m2vnshYFJ7xUSVp0E1x0jluRWya%2Bu5qxaF%2Bz%2F%2F542KCgvmSQdKk7Gjzo8uHj%2F8EgsNgLD1QT0iX6Zl%2BXdSbaDfYBlJ4dJHBcc9mM%2FEo8w5vK%2FVLnNQB29CVoIWG876fyohaxiH7jfVUx4SPasIn0r6KxDm473odiTmwtJrQJ7%2BDlin%2FPvB5EzvlTCDMoXllU0dNUVqp9t%2FNdpH1dW2GtTyrvqdmG9z5yqobGclnPo0OQJAsyXtUROVGhbJzW3HV%2BmGo94JAofb9gn5ReQsjjEKKjx4JXtTLpyy1eiB2a0VYP2PO%2FWzjH3JPokxb%2FzKV8bObiEqaKLxPP5NoJx4F7Y4QrPpovadZ31BzJL%2BEV5I1tQw5sHF8DPK%2FG9hM8vw8F3VS1k4UIOKlgwmvZRIqGBIQidVdkyx%2BSuXj1z3cdPwibBU81L4JIydIgYgalZ2JLZdnP7JeiMNH55LwGOqUBmbclmaG5NaeOjZgcxmZphVHo94SqBQhWqM6jLpsKEEiUWTKd2nuneL1J5143dqPYr8h%2FjfpWOLmJf7HMvBQO5277xLVFGlNYrCAGWxAWseRd2uoY2U3X7I%2B2nmQZsM1L2NizYdXLdJw6FI8tlDDK%2FQ9ANwZGlrmGd9RNhMvbQQ1PdY7hu6yVKW8Zs3yvdATWlLqv7NA1iBqymkSWniHcArWLivkF&X-Amz-Signature=57460b4c96fe64115c1418292f7157b5e0b15fe8484a3e1cce3f9caffde1e06e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635A6RZDR%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQDtz%2FIBN8APuutPf1zKBW3R8%2FVHgsXs09vPVP6q9ydDlwIgHu0O0i7CkEpnxnqys74Ad3ffjjqw9%2FC4%2BuYiFDSUZH0q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDPNeBHs53G0qt4AMZCrcA6yahV0vhhOb8EdmCgx39wr7vE9b4spUK2NVqJW%2Fz9Ogr9qRO4Z36vIOfEhMX%2FWVMf1S7QgSYuyj5bxWwLoGQX60NM2ysTUIIguXzwVrK3MVX2WkysZA04bsL4RPxPC5G5Ac9jcZfpOIkgnnpTPR4FBA5PnPlMmfLFdi9JwX2JHZZ7brGcy7m2vnshYFJ7xUSVp0E1x0jluRWya%2Bu5qxaF%2Bz%2F%2F542KCgvmSQdKk7Gjzo8uHj%2F8EgsNgLD1QT0iX6Zl%2BXdSbaDfYBlJ4dJHBcc9mM%2FEo8w5vK%2FVLnNQB29CVoIWG876fyohaxiH7jfVUx4SPasIn0r6KxDm473odiTmwtJrQJ7%2BDlin%2FPvB5EzvlTCDMoXllU0dNUVqp9t%2FNdpH1dW2GtTyrvqdmG9z5yqobGclnPo0OQJAsyXtUROVGhbJzW3HV%2BmGo94JAofb9gn5ReQsjjEKKjx4JXtTLpyy1eiB2a0VYP2PO%2FWzjH3JPokxb%2FzKV8bObiEqaKLxPP5NoJx4F7Y4QrPpovadZ31BzJL%2BEV5I1tQw5sHF8DPK%2FG9hM8vw8F3VS1k4UIOKlgwmvZRIqGBIQidVdkyx%2BSuXj1z3cdPwibBU81L4JIydIgYgalZ2JLZdnP7JeiMNH55LwGOqUBmbclmaG5NaeOjZgcxmZphVHo94SqBQhWqM6jLpsKEEiUWTKd2nuneL1J5143dqPYr8h%2FjfpWOLmJf7HMvBQO5277xLVFGlNYrCAGWxAWseRd2uoY2U3X7I%2B2nmQZsM1L2NizYdXLdJw6FI8tlDDK%2FQ9ANwZGlrmGd9RNhMvbQQ1PdY7hu6yVKW8Zs3yvdATWlLqv7NA1iBqymkSWniHcArWLivkF&X-Amz-Signature=22b64489eed42cd41c8fc4e1037f3fac9eeb41eb8a1881b98fe9c306bb428746&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635A6RZDR%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQDtz%2FIBN8APuutPf1zKBW3R8%2FVHgsXs09vPVP6q9ydDlwIgHu0O0i7CkEpnxnqys74Ad3ffjjqw9%2FC4%2BuYiFDSUZH0q%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDPNeBHs53G0qt4AMZCrcA6yahV0vhhOb8EdmCgx39wr7vE9b4spUK2NVqJW%2Fz9Ogr9qRO4Z36vIOfEhMX%2FWVMf1S7QgSYuyj5bxWwLoGQX60NM2ysTUIIguXzwVrK3MVX2WkysZA04bsL4RPxPC5G5Ac9jcZfpOIkgnnpTPR4FBA5PnPlMmfLFdi9JwX2JHZZ7brGcy7m2vnshYFJ7xUSVp0E1x0jluRWya%2Bu5qxaF%2Bz%2F%2F542KCgvmSQdKk7Gjzo8uHj%2F8EgsNgLD1QT0iX6Zl%2BXdSbaDfYBlJ4dJHBcc9mM%2FEo8w5vK%2FVLnNQB29CVoIWG876fyohaxiH7jfVUx4SPasIn0r6KxDm473odiTmwtJrQJ7%2BDlin%2FPvB5EzvlTCDMoXllU0dNUVqp9t%2FNdpH1dW2GtTyrvqdmG9z5yqobGclnPo0OQJAsyXtUROVGhbJzW3HV%2BmGo94JAofb9gn5ReQsjjEKKjx4JXtTLpyy1eiB2a0VYP2PO%2FWzjH3JPokxb%2FzKV8bObiEqaKLxPP5NoJx4F7Y4QrPpovadZ31BzJL%2BEV5I1tQw5sHF8DPK%2FG9hM8vw8F3VS1k4UIOKlgwmvZRIqGBIQidVdkyx%2BSuXj1z3cdPwibBU81L4JIydIgYgalZ2JLZdnP7JeiMNH55LwGOqUBmbclmaG5NaeOjZgcxmZphVHo94SqBQhWqM6jLpsKEEiUWTKd2nuneL1J5143dqPYr8h%2FjfpWOLmJf7HMvBQO5277xLVFGlNYrCAGWxAWseRd2uoY2U3X7I%2B2nmQZsM1L2NizYdXLdJw6FI8tlDDK%2FQ9ANwZGlrmGd9RNhMvbQQ1PdY7hu6yVKW8Zs3yvdATWlLqv7NA1iBqymkSWniHcArWLivkF&X-Amz-Signature=bcaf5b343e21acb6937784e925b32f357bfd5601ffcdb07641f2b4783c0b24b0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=fdaac6ec644a39cdee8f18b37d54f0d96269e05537911fc6526b4dcceb580621&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=28a08ee4c665f00fbbb64c2055aa1c701df113f04825cd0e1776fc8f17670eb7&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=83b9e2c5381a3923d9458de8684e58232a8390ce73325d943e7d42ab39eecf49&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=58b3580e1fccb762f02d8953404ab100041f6090ec71c91cc473a39800a7dfaf&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=afc7b74b3328189f6f9392732fe296cc30b8281986f878b34a9bc5c7f0c4ad63&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2H5CM7I%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIByQK%2BZ5Xb2wuTiwsDGxXWS5%2F7nAyEM1RRIKEXfriC8LAiBQjzcTyh1XpwCvH%2BmVSy1paDsMVAFnC8NKDbp1K5OIDyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMS%2B10NqbgOFQv2hxzKtwDfh%2BP1sdRo4%2BSm2CcOi8W6odiesptXHJem7RQ%2BAqovJoqNxiUh2Kdi38e%2B3Ya%2FC2YZKcfyf6DjJoqByOy%2ByNT9s6sSqgB%2FqqP%2BejlKp1Ok9LfS8vBZp47QoH8apHY6oLnvrYU2fDayXElwdPpmuZ2D586v4qby2R6uUFgLBxMeSmr7s4GJ31vEpdYgOqxHY%2B4ixD2amKQMQuI3lLAmI2kllkvT%2B94b7uXUcXh7EgpstPyghS3Age8CD1kRwgGPzUI6Y5l3kpT6bnspEno3LjGM2s%2FWXc6T4SC1aIZqqiTO1dMuTnG8Cm1DRhMvZCWXiPa3ZW5RkrKmt8iLwNEeeFbgJBuVHCOOlVqZFzaT2lv7PwD7zLfhDC8Ass6YwK%2BoAX4UIdKMGam9IvxBQZ9ghsl%2FQwBZnnxWTuPMxxSwdpyjleLRzeG7upPZ4uhLdtOE2luywXzA%2BKvBPChay%2FhVgPNpGg6VdcTjRmgYaaFL4xmnH8H5k4I%2B5NI%2Bt4%2BQ6Mx6%2BIwXq6ABWwygTFTej6EnmzK46POOGk2PP0bBWZQ%2B7c%2B5roMmXNChXSyvYdJZpZKYuYYidhbq3f%2Fz0MOwuuwe2wYI8XpTjVP4Ul1PIHFs24np3MIylv%2FCdLQlHIQgb4wvfnkvAY6pgHANpp33ejTI%2Bw0ACbglX8ieIaP5tgcTm7zSgMln28uZUEab4wIfuXE6TVF4ZT3JX6XcworBp01wtUuSW5rbu1Pt3ditiLePYYqKRDxyg8aIirhymBZYLVATBQ%2FrKiilAHu%2FPdKsbkAg7nYzs0jo%2BoTP6vXvpUFN2x%2B6I%2FEoKKr7bvYUS1yfmn%2FXzht%2BPWgsAsQ3M4xFQWhOf1nVy8Qz4UvInjQQX%2BZ&X-Amz-Signature=b2613b1376758c70c7b6d830a5d6f4ad60df2dbd61ea58ffda59029682333056&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KHJLXXS%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQD634o9Oib1XEdkHsT4HRcltSIyf8i%2FoPSxJbU1cjuO0QIgFBIISEZzfAHejL0Fz5FXeipwJMmi7EJvAEFFkpet0Gcq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDKWZYWUHBCMuj53FMircA%2FSaQ6BKSvVjC5PbKKIUpO3o8AM0KU8bCGH96u9cuDH3X361JR%2FLYAbXV9iG5CrDfw3THMDh%2Bcn1o%2BZfXr2nIj%2BmrbumnLvirnLB9WfR5tmrTEt%2F91xZuLp7pSuKM5xq9rw4KOYbOMXPAsX62wA39oo%2F5PtCPKiChIhgDGay6W%2FAAmGuKaxPvGXjoVjHT0hqky9krGzJyYmbmxwjlercsrq5P1XV2kMG9HdYebPBMStvbN2ufMxXDasRubwXaX74td3SAOFMiZ4Fr6riBHupPP986gYu%2BQEola%2FlHoGd2Gtk5%2BhA1Um4eY3daW2MxeJsW8va3Yt8r55v2GNHxCr1yby2pEoM8HQEaEZykv7HmSDxC83vAq0DRynFCs6roGBh9rIK%2BdKmpHYgfuQvXBwcPLrhlCbFC5sIU9cG57HBVf4ci6ShCGNtMGqaqwaZuIKQ5r80o%2F1GPijQgWD%2Bj59VkK5Ylc3ZeUdXSSAY0yw56venEzgA6XYPietJ1w09tSiVfqkaYz3pX0b954%2B5dRybsFXYKmmuX6%2FfvbfW6pG4%2Fk8z3%2FBp4hLCJ5diM%2FX77WpPgjNsNE4n34OpQg%2BnncDxOPWqXx29BqnCORffOoUKFVIKCJJcb3UAudp59VQRMI765LwGOqUBgyQXd6duIEkIVkrqq%2BZpyYM4annh%2FsJ2Nq63QED9xMu1Ha%2Bq27NonpAn%2Fky6zKYBQUatyD2%2BDvs%2BXu6u%2BfPuIYm4GfCjOEgsERNTRV0dZKvEptBYq1wtouTAWS6h9lBx9Jc9HI5yQs0%2BiMF2%2Flf%2FvJLhJZR6%2F%2BvjPQRWFh0dOuSxLem82YTop%2Bmt8MJKoedOypqW%2FUeTKpCu5bPNPD3Vq1%2BHjalx&X-Amz-Signature=a783cf6ff54af982e9033c972abc22fc515bbf6791c3c334df96e0a84391591f&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KHJLXXS%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQD634o9Oib1XEdkHsT4HRcltSIyf8i%2FoPSxJbU1cjuO0QIgFBIISEZzfAHejL0Fz5FXeipwJMmi7EJvAEFFkpet0Gcq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDKWZYWUHBCMuj53FMircA%2FSaQ6BKSvVjC5PbKKIUpO3o8AM0KU8bCGH96u9cuDH3X361JR%2FLYAbXV9iG5CrDfw3THMDh%2Bcn1o%2BZfXr2nIj%2BmrbumnLvirnLB9WfR5tmrTEt%2F91xZuLp7pSuKM5xq9rw4KOYbOMXPAsX62wA39oo%2F5PtCPKiChIhgDGay6W%2FAAmGuKaxPvGXjoVjHT0hqky9krGzJyYmbmxwjlercsrq5P1XV2kMG9HdYebPBMStvbN2ufMxXDasRubwXaX74td3SAOFMiZ4Fr6riBHupPP986gYu%2BQEola%2FlHoGd2Gtk5%2BhA1Um4eY3daW2MxeJsW8va3Yt8r55v2GNHxCr1yby2pEoM8HQEaEZykv7HmSDxC83vAq0DRynFCs6roGBh9rIK%2BdKmpHYgfuQvXBwcPLrhlCbFC5sIU9cG57HBVf4ci6ShCGNtMGqaqwaZuIKQ5r80o%2F1GPijQgWD%2Bj59VkK5Ylc3ZeUdXSSAY0yw56venEzgA6XYPietJ1w09tSiVfqkaYz3pX0b954%2B5dRybsFXYKmmuX6%2FfvbfW6pG4%2Fk8z3%2FBp4hLCJ5diM%2FX77WpPgjNsNE4n34OpQg%2BnncDxOPWqXx29BqnCORffOoUKFVIKCJJcb3UAudp59VQRMI765LwGOqUBgyQXd6duIEkIVkrqq%2BZpyYM4annh%2FsJ2Nq63QED9xMu1Ha%2Bq27NonpAn%2Fky6zKYBQUatyD2%2BDvs%2BXu6u%2BfPuIYm4GfCjOEgsERNTRV0dZKvEptBYq1wtouTAWS6h9lBx9Jc9HI5yQs0%2BiMF2%2Flf%2FvJLhJZR6%2F%2BvjPQRWFh0dOuSxLem82YTop%2Bmt8MJKoedOypqW%2FUeTKpCu5bPNPD3Vq1%2BHjalx&X-Amz-Signature=6df85652d0fcf1f9c586ada9d0295bc21175926150b8af21cd87d8e66561a2f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSJ6OVRC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIH%2FGrxx1bxNRg8E%2BjDKw7vCGn5S2OOvNLxWvUgsbq1qvAiEA4k2sb9IX2XK4OvJHA3XAyYfA8FgRVs1v4oVq8gt2QtAq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDEoZDhQs19EdCHAMcCrcA1IVoCHnwRUylm9v5eaDhu4bVe2rehyhp3MzGs6F6M9r6n2bV495dl0gv4e3qUjBX210F2nn%2F%2B%2FuXwXQN4OtQTluCzXjg0JTdyGqDz06GHSzCclVfCKWFq1sKkdSfmeFoV34COPGz4CTqcx%2FjJUZwKYAdHzpo48hmKylnJzwYI3l9CyddJ1NxMmdsWx6n4YkczCA2T1nvNike1onUHEO77y7MSCwHTqpZVjRmUKMriPWBr0FkefFXxbjS5FtXTuZVD5hJ6sdEvRJmxIO8kSIurswEWLzMq4uH9B5fq6B%2FJVkn145FfOh8ONBwE0tqwEOyace9LD%2FNouksjiUDYTT4r38GH9tdswsenRadExhLM2ETmGa86q7SGJbcDJlh0fUyLx0NWsycy%2Fp5XwCyiKxb72WF7Qi4WHd0IQh1hAcGA%2F7%2BmfHr2jpfKThBLiwUIi675b3wdw4glr%2BfgUjJ%2Br31%2B26aOQ9tTxXDbOoF5BQP5KLG2zdSkNkF7dioZTDRWSnPMMJ78uHV5xP%2FkOlewbClCFEraZ7Fx3IYwvfK8k%2BamUMN4q4PkTXIy3BftURal3wJ%2BfcUNa9qI2QVnkGuPtYax1h0%2BREOVrzKjCtXmEIiOQBIEn3J67RC8V93VGUMJL75LwGOqUBHWN29FC3TvmNCJxrbRdY9l%2BYppSYWPNSgKdV%2Fzh%2FsjkyR9k39gr%2FchGMoxJqYUM8xUClMNsQG3OFqMdxsBkiUvJ9zdq73yw1yKwI9yAerAT%2F%2BBxmgNCBw5J3kSKcGmZ5IQeu7q9vKp5dulo1iDGRs6uLFdek0N0%2F%2BQPZE2MZlm%2FOR3HWgj42AvASBcCu0M6Bj1Hsk6U7MqUBXliLajCqpyV5TIkQ&X-Amz-Signature=80e98e65a2e2efdd7af94fa08d77f8c5e37d7ee7d759c94e798a34be26e2016c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5UW2GTL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG%2FRIRu4oBeOY8gCOHpy%2BEDkd13rwUwtrwfqT1t07rNLAiEAv0ZvkrdR5Aace6BucKpWe5b1fSURhNkRN4D4mik8Xn0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDhkBdARMwBdBryfICrcAyHsyFzvE6Gw42p9e6u2xTwRoJWYdpURsq2yXu8Nz0mJ3hCqc6Xrx1Dv0AiwsGwlgdfOUbaxvMGOhLKxnKLschI4hBpn8Sdc3n4S5Go%2BliwbfhtyiyjZPtXdzTyxYoxJ8GRACi%2BTXCe58%2BgiO1lJ%2BuN%2BzE%2F4M2T5rcZPJiaa6xlJQ8SEvfK2atYoWUU3PvfsqUV8kaie0WjpZ%2FViHI0a1Zc%2FSQW%2FiZTek32b84YUJQSJU%2Bixv34YzBAetw4QOEuf8d6Zi8w9CkBwLQDBziqatuzt4cwPCrOiJeP8J9%2Bq6hWcLO96PRAFTL0tSdiVAA2K9%2FlEMEFZdLa%2BtKQqqZLWutzuBVaIONkTRykNLC40QmJcUB1bYbVKOCHb%2F7sxFjFsXPWYk8jQk1JpPbiwRHgc4lFEpn6PGcghiBc6axTO6%2FV7inQ5rP6TGG%2F6LfNE1%2FLYwaIbcP8o5dElbHl9vId3Ta3jSsLSBxDzEGiMMO6iBKRczKFoQ0beWt1RQ5i8aY4Ry%2BQcdo%2B6JMRgXR0LXUb63DMBOKXVZKvb92QCruV190Znmk6DRV82Dure11sAKQkCBiMSf613tkjlF9ZtCKGeNZhDeYe%2FDbyPrHiwAi8EbATolFEPjI7320tuFmYZMIL65LwGOqUBZCc9OgNlzFhNXnUNcqvRQsTkxtgIvJlHxm4%2Bc2oWrApgnHKkcW%2FVxXREWtje0e1jvLu8D5%2B7JfYmTTOkS2jd8%2FUTtAnH1QWCd1CwrbWXbAOyHuRnu7WxJ0O9Tk4rMbiPUwSGJqDuYZvlL3S4eTtGhoFBWIknl3V03onOkb7CQ9fO22C0mwV95lXLy6TutOL57VPtBsxJ%2BjY8vm7wRW5amCw6VHPh&X-Amz-Signature=f32d8d1b1c49a5711fe0856b1ce93e33a66838c8cf515cddeb3ddf906c7e4828&X-Amz-SignedHeaders=host&x-id=GetObject)
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