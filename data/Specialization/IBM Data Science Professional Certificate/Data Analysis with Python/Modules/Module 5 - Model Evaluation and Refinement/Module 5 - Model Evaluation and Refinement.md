

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=bf90c4c560c1ad538d15a54546374a2886715c5a49dfad4c2883ca33c97da4be&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=18d56b012d60fa4e244cdcd35e42d36e420d17ef9a796b0c8f718cce0014a71b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=0d0bfac274c5fa5efddd3bbe9dca5baf8b848515e0c1ee555f76ade9ac1ee725&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=e05ba263870df760252be6b85e69a2313358b967f95086f51728e25fd84f2e31&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=3c6a78531ad335f0a5670cb06ba53828629bade23474d787e600fcfc0e40bb3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=52e2ced52ef205883598136a3bd081942d7cf01328bb3aa0a07df50111418bb6&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=e866ec0a3aecf625939d025e9dcd949f35cb8209c7f57abe8ab24a9eb9397a99&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=0607dd3a272c8a7a7e66c5ea7b277d46ef60201f0993c9abc7187608b11ea6dd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=4d5a6e674384bde26b54a22161a0f3116aec408a859866455c9716e7a7890f2f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5247QHR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F2pD4VFEgBuDNuR2WTO0WHzgiMS789Kc4bkHpANqhjAIgUAQWC8rLZWseCsu4gF0gn%2BKYsEtLHLv6p%2FKujKAaOTcqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCTC77OLVF5LFi3RGCrcA3Oru1Ab%2FliAiv3ruJL4G2Bn2cNrB92VCPQbaUKrAAuE%2FfPGaP%2FZV5Uc5K%2BVsINP3HMZhROIaDvt6gtCQ8z%2BpbIJVKTuQl0NR0dFxjE%2FYC9CwKiKjBdLvRkokp5LoFY2pqGUZg4aGdJ%2BpTLJBSuNgwNwYDHBpHtLBxYYHIzf6rQWYy8lzW0Sva9KsAnOft%2FeEkJtjCqyXSml1uRjPhP7puDMCv6cqY%2B3DlE49Iaozt6yWXUIEcPVq8ulfBc0hDdYl4Yq%2BaEhq4toXycVVpQxmbspPsvdr%2FXmat2bFROkolNLBrc80WcE8uSoXafvM6uTwD1zDohSdwQpX12CVW8BPfZcxkB3S8KpYmLpknkPw%2FPNLpQKgXnET5z0zPdp52nUyZ6r2aZrXGoqBv3ZdQNlFjnVoc6WBGw20CdQB5bsaCAv7H0EISQpi65Mm5dAKQeK3iRnV2OdJ7GJg%2FoX%2BF%2B44nDipAepFo6aklAN8PPAzZ4egjvgHVMVNMyq2%2FZyuCe5vW3k3U2bbCzaiQtYA4MbDkKVRHJQkikZJY%2BTklPJ0ex7LQ9JLz3xI06BlQezsadnJWIk%2BFJDoLcR5HDSdP8MfZg8MiEHciyIpgv5ZzEN25RMFec2vbLhi8r4mq3KMIOj7LwGOqUBss32jDOaP2LVYxZvnJtc7BKxwqrKJTR%2B2k%2F1VUprt2FV%2F6QrI9PRj4nwPZBCKNVbZtKsZSg3wNH1IoMV1eRZlj0NP3YcFFmPqdaHSKlqrtCvRK3das7kplnQrUG26qLFwurg3xICwE7pmoRwvKov6eZp0jvt0SIJC6CAOmDFkoRem8WL2sjCeNmXDPGrwBntg0wXN%2Fe77Ta%2FgRJNSSPFxhG3E59Z&X-Amz-Signature=38ef23a0b40b99e1be49128ada40c7f94929392c815b691f1e7b28c357a57e78&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5247QHR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F2pD4VFEgBuDNuR2WTO0WHzgiMS789Kc4bkHpANqhjAIgUAQWC8rLZWseCsu4gF0gn%2BKYsEtLHLv6p%2FKujKAaOTcqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCTC77OLVF5LFi3RGCrcA3Oru1Ab%2FliAiv3ruJL4G2Bn2cNrB92VCPQbaUKrAAuE%2FfPGaP%2FZV5Uc5K%2BVsINP3HMZhROIaDvt6gtCQ8z%2BpbIJVKTuQl0NR0dFxjE%2FYC9CwKiKjBdLvRkokp5LoFY2pqGUZg4aGdJ%2BpTLJBSuNgwNwYDHBpHtLBxYYHIzf6rQWYy8lzW0Sva9KsAnOft%2FeEkJtjCqyXSml1uRjPhP7puDMCv6cqY%2B3DlE49Iaozt6yWXUIEcPVq8ulfBc0hDdYl4Yq%2BaEhq4toXycVVpQxmbspPsvdr%2FXmat2bFROkolNLBrc80WcE8uSoXafvM6uTwD1zDohSdwQpX12CVW8BPfZcxkB3S8KpYmLpknkPw%2FPNLpQKgXnET5z0zPdp52nUyZ6r2aZrXGoqBv3ZdQNlFjnVoc6WBGw20CdQB5bsaCAv7H0EISQpi65Mm5dAKQeK3iRnV2OdJ7GJg%2FoX%2BF%2B44nDipAepFo6aklAN8PPAzZ4egjvgHVMVNMyq2%2FZyuCe5vW3k3U2bbCzaiQtYA4MbDkKVRHJQkikZJY%2BTklPJ0ex7LQ9JLz3xI06BlQezsadnJWIk%2BFJDoLcR5HDSdP8MfZg8MiEHciyIpgv5ZzEN25RMFec2vbLhi8r4mq3KMIOj7LwGOqUBss32jDOaP2LVYxZvnJtc7BKxwqrKJTR%2B2k%2F1VUprt2FV%2F6QrI9PRj4nwPZBCKNVbZtKsZSg3wNH1IoMV1eRZlj0NP3YcFFmPqdaHSKlqrtCvRK3das7kplnQrUG26qLFwurg3xICwE7pmoRwvKov6eZp0jvt0SIJC6CAOmDFkoRem8WL2sjCeNmXDPGrwBntg0wXN%2Fe77Ta%2FgRJNSSPFxhG3E59Z&X-Amz-Signature=bfafdecaceac12cd64e30b55cd80748a4d74f3c5fc7d97daf86c82dbaa7dd42f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5247QHR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2F2pD4VFEgBuDNuR2WTO0WHzgiMS789Kc4bkHpANqhjAIgUAQWC8rLZWseCsu4gF0gn%2BKYsEtLHLv6p%2FKujKAaOTcqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCTC77OLVF5LFi3RGCrcA3Oru1Ab%2FliAiv3ruJL4G2Bn2cNrB92VCPQbaUKrAAuE%2FfPGaP%2FZV5Uc5K%2BVsINP3HMZhROIaDvt6gtCQ8z%2BpbIJVKTuQl0NR0dFxjE%2FYC9CwKiKjBdLvRkokp5LoFY2pqGUZg4aGdJ%2BpTLJBSuNgwNwYDHBpHtLBxYYHIzf6rQWYy8lzW0Sva9KsAnOft%2FeEkJtjCqyXSml1uRjPhP7puDMCv6cqY%2B3DlE49Iaozt6yWXUIEcPVq8ulfBc0hDdYl4Yq%2BaEhq4toXycVVpQxmbspPsvdr%2FXmat2bFROkolNLBrc80WcE8uSoXafvM6uTwD1zDohSdwQpX12CVW8BPfZcxkB3S8KpYmLpknkPw%2FPNLpQKgXnET5z0zPdp52nUyZ6r2aZrXGoqBv3ZdQNlFjnVoc6WBGw20CdQB5bsaCAv7H0EISQpi65Mm5dAKQeK3iRnV2OdJ7GJg%2FoX%2BF%2B44nDipAepFo6aklAN8PPAzZ4egjvgHVMVNMyq2%2FZyuCe5vW3k3U2bbCzaiQtYA4MbDkKVRHJQkikZJY%2BTklPJ0ex7LQ9JLz3xI06BlQezsadnJWIk%2BFJDoLcR5HDSdP8MfZg8MiEHciyIpgv5ZzEN25RMFec2vbLhi8r4mq3KMIOj7LwGOqUBss32jDOaP2LVYxZvnJtc7BKxwqrKJTR%2B2k%2F1VUprt2FV%2F6QrI9PRj4nwPZBCKNVbZtKsZSg3wNH1IoMV1eRZlj0NP3YcFFmPqdaHSKlqrtCvRK3das7kplnQrUG26qLFwurg3xICwE7pmoRwvKov6eZp0jvt0SIJC6CAOmDFkoRem8WL2sjCeNmXDPGrwBntg0wXN%2Fe77Ta%2FgRJNSSPFxhG3E59Z&X-Amz-Signature=a6e8e3c4cc74d5c76ea136dc95566636585b5cc047caa4683019fea9785fc629&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=f3d3082eb886da34c3910fd02450d2013afef181863847a2a7a02041982886e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=407d479883ba7e7d49c26ea001626853197e68ba76e8b7dddb030c574bd43c54&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=e40fcb42abf10e8761874803022ca22b02c7a0d662b5c6f2c7dc6a6752cf45d5&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=5faa2a11d422673d063a30ef99c7309b12d9827a119da959dd970946c6ccf560&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=47e1362406f61112a299883c5545185e8edb963dc742ad683b6ff89651c17c57&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOBXMDON%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDs5Of1IxSMjn25BfWdtwwOHhEHIjlEIyMyLubSJ%2Fpg7wIgLAEytxOBb6j72W7hzIuhMLCM7ykBFKarqEP7ro%2BCTxsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD0ztiOmYp%2FqsuVHRCrcA5mBzmEs9y7XPDKioTjwjmkEYPoxl4WtBH3ox1bU0mrMgbCSH1pPOFRX19OFeHHkrLpT5BBtd1nFYRPAT9DdRua7olCy9k30MoHSTkqqTDQVheOLymn2bePxO1mK7TyUhP%2BA%2BzgyTGD0VAhQNHrDEspjcEwBqNViVGeq5GDgcmGKwinmWwMgmwiO1w7hyvjE%2FejZY3daSTCkOmCPZ%2FeTS1YrV0%2BWHaZt29Eg4qX3hi0YVmJonYdwEs3nMdaWfNFjT7SS69S8TTfoXiw2SprhKYR7Dxy8jPFq1IB%2FWaMnbSw2GdmTKVN17n%2BQOgNHPZu1%2Fi9QR3f5UwYuG3HmmEiBWnT0VdERloqnEmlD5HmNLmFLxh0MsOH8JkWZYsRoqxAIEVCzpdIIhbmSVmQ8vAdLuhC83in%2BAhr7O9BtWmyl3wjxMpQBUT89I9e7Iz%2FN4JLFVmBLIdeEZiQX1Mvw2bpLCXj8He1sXh1GmejJlBrhZBwoEV0EQMb2Y%2FZHz%2FnOcJue9KQL%2FohHizSaORuQwF%2Bdm5V9YWhl5CKR8Ep4QX4dkNqxwulwb%2Bnn4%2FQJwyGJzE334khTLr1%2Fa%2F2hyjWQo4tKEV%2Bw2qpbhHzXP%2FGel9G7Ln41ZqcqgU9etYJWMmp5MJyj7LwGOqUBrmwAEksOuI4QbcITAjwTO6Sfk%2Bci7uxJ%2BzFmGIERtQmJ5j50TRQgOXZTpD4T%2B7zj1MuMb%2F6ooqy%2BnVuepb%2FIshdp%2FNMRn1vRRSYan%2FQcccCFcHOnJ8vBjztc9w%2BPY%2BlZSWtP4daj4%2F097OOxfadunHTsi%2F3az9vgRjJc1T8%2FnADTfKOSrrU4iU8pr1TDE0LnNKuXFzS%2F2UVr8DnPss1zs%2FOPbQcK&X-Amz-Signature=7e7af667214b6fbbf9ca10148a83ed7cdb976a8700624d01d880fd9828910d49&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4C4V75V%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFQfVvkla6ZTPSl0E8t7o%2F9KU44t5yUmqfF0%2FiewfxSAiAAuLvHGXGLE8bg4ES2%2BztRZKF9wj0xon2IYkZEALgE8iqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgur%2BsXEbNEhycFq2KtwDtJE4tAUx1D4akZqgNapZYRFcLbzHpnxYQUIAuahULECH1NsEFSo1eORIC4IbA2e7xk%2FYNB73o%2BBFAiSVLtDWTzY6s31E8jx6XV8E7dxm4qvHInfDhHXa9wENRqalKWkWfzo8k2dujn17ijiHqjz6qnNrNNVZ%2BUerOjJFbYq5MKmLuIAbIa8wZ%2FLHQGfhd0AbLlg5AkHiVmYyWvgDISBZVzIfycEa5PzG166WApEuwac9hCy1EDoWKPA8f4%2FDj59GSrXZyl0aojQRUcip4o332p83RLuDB5ENIJ%2FDXSV0ARWCTasSagb9zcGo45ZewW7rxdScwyNnsDv4W0sYoxU5SV7Wizg8Pdd%2FjUn7s1TI4ppTob5SDMT%2Bzm3UcyV%2Be5jGfbhQoehnFLUMcIO3YwohaQlWm51FHfRRo3uFffkZkmmksIsN1MJmOJpGMP2ixd3AvuTM3R5Tkx73%2BogfyPFuN7Pm2%2F2kXCkfDi9dUOgyWJNYCqODPkUN%2BxJbUUoWyk4lhFlXzV%2BoYDIwj813T2oV9stU1ipISZFeTEewA3b8GoC3l1Z%2B1%2BBgIk1CZMMwwIWqb5%2FkEdAPqBxslFt7nC1hNrdjNtXoQHvoOyW6clyUzp8%2FiZrqqlrN0pAf2k0whaPsvAY6pgEt0AITUBqpBTlicJTSR1xkweKle25Qt43FrNOfaG8QUsv3nYCipJ6x3Jr6uJUXVRtDvz3MaX%2B%2BlV21icCwrdn3Haf5dE8jDnp3gOinX4z2ty2U%2BvwGfBH6GQJwdwdCIRDlgXOvqLGhZdK2aYldYnHVASOED0kfurs2zseAfODdrAQkyGkd9CRrblHJXJx0QyJADqtVHBwYeQSbgEtYW44bAM%2FEE%2BKG&X-Amz-Signature=cebc736ee25f7da174b994b59683069c9e5427e084b709dfddbc9ed2db62f0f1&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4C4V75V%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBFQfVvkla6ZTPSl0E8t7o%2F9KU44t5yUmqfF0%2FiewfxSAiAAuLvHGXGLE8bg4ES2%2BztRZKF9wj0xon2IYkZEALgE8iqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgur%2BsXEbNEhycFq2KtwDtJE4tAUx1D4akZqgNapZYRFcLbzHpnxYQUIAuahULECH1NsEFSo1eORIC4IbA2e7xk%2FYNB73o%2BBFAiSVLtDWTzY6s31E8jx6XV8E7dxm4qvHInfDhHXa9wENRqalKWkWfzo8k2dujn17ijiHqjz6qnNrNNVZ%2BUerOjJFbYq5MKmLuIAbIa8wZ%2FLHQGfhd0AbLlg5AkHiVmYyWvgDISBZVzIfycEa5PzG166WApEuwac9hCy1EDoWKPA8f4%2FDj59GSrXZyl0aojQRUcip4o332p83RLuDB5ENIJ%2FDXSV0ARWCTasSagb9zcGo45ZewW7rxdScwyNnsDv4W0sYoxU5SV7Wizg8Pdd%2FjUn7s1TI4ppTob5SDMT%2Bzm3UcyV%2Be5jGfbhQoehnFLUMcIO3YwohaQlWm51FHfRRo3uFffkZkmmksIsN1MJmOJpGMP2ixd3AvuTM3R5Tkx73%2BogfyPFuN7Pm2%2F2kXCkfDi9dUOgyWJNYCqODPkUN%2BxJbUUoWyk4lhFlXzV%2BoYDIwj813T2oV9stU1ipISZFeTEewA3b8GoC3l1Z%2B1%2BBgIk1CZMMwwIWqb5%2FkEdAPqBxslFt7nC1hNrdjNtXoQHvoOyW6clyUzp8%2FiZrqqlrN0pAf2k0whaPsvAY6pgEt0AITUBqpBTlicJTSR1xkweKle25Qt43FrNOfaG8QUsv3nYCipJ6x3Jr6uJUXVRtDvz3MaX%2B%2BlV21icCwrdn3Haf5dE8jDnp3gOinX4z2ty2U%2BvwGfBH6GQJwdwdCIRDlgXOvqLGhZdK2aYldYnHVASOED0kfurs2zseAfODdrAQkyGkd9CRrblHJXJx0QyJADqtVHBwYeQSbgEtYW44bAM%2FEE%2BKG&X-Amz-Signature=d923ea3708da34888f1bf626cc3daf7eaee07cfacb02306f970d8be618c65760&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VE5RUMDO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWZWADonMuPO0Am0gEDgPYsVhwyKliHx3dIaDU%2FBN20gIhAOchVJQ8QRPLqDW4FVOCQvMKg5epLFozbAIUXXNfZuj5KogECJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzKf726Pijv76p7JvQq3APUNKq9Zqkleaz8tXfH%2Bd1ylzJYb6kNGhjvMuA5g8LGf2nOFsZew9F5NhnV2RyE5mXviJfoNVUG81bYL2soNdUp%2F%2F8QDe6XctrAqR1QQvt3dfpFMzbx0u%2ByznC5iKKOXmD4%2Bg3WPnA1dIn%2FATwQSjShS6RjfnWVUi2Kvp%2BSRTmQbA3Lh7l39MEehWLHuM3Fd2Hvx0WhzKJsKTQXUzy8wi2jdR3w8K8n1HkC0XJeniOhIDiUrQaFKqeD5e%2BFv51XqCqlid5H72OMYfUp%2BlFx9pbkUli57V%2B12GH1QsPd%2B%2BeZ8Yq74dxcgfXQfUps1nyFhhXF%2F0i9DlSDxklq%2BR4TeFT1R5iEab5xYwZkcN8cpqfppSVtmcwtcBFdft1rOBBWQ86X7tnf8XO09IiFZiQsYykjpYjwap490trjk8NyiktzMm2%2FWoyqOH5PPrn2Gwi1BxudPe0eoVXvssAfM1aIsLYtDqJq7ktPTfIlvqQqcy7l70G7mHP%2BhiZgfiixHOyZRtMyzzwS%2B57dhD%2Bf8DHX87ndUFF%2BGOkBhkyXvE8kA%2B5UBN%2F0z9H2NPHvl8ZKmyt4Ai3f%2FRKT%2Bya9v4xLqSEKx0W8tHpXe00ZWmbjW9ZIyWehsTQiqQjGaeTPMjEpuDCco%2By8BjqkARkRtRCU0q2HBRccGW40qyJDctuEEteQ%2B5vaB1UEYoOPrdPZYGTkddXEn7CVovkcjtCA3mrHFfzkOtQ%2BZ7AUbp4n0nSHgg8YBJsGdaW6J%2F0Di6cSn%2Bm5zxXKMz%2FUc3vN5b8T46O9mA5wd1yynFLB9f9cQKYSmMI9cYoWjJpJeBz2Kn1wVbYW%2BG7%2BMiRtWRf4fWj8ZesQKYAQZ6grdiIJS%2B5OxnYz&X-Amz-Signature=c8927e0e6683d37062421f8fc13da53af0d5572cfa6ac5b66d644c0f29e4f50d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPGN4B6D%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCATP9ZJ%2Bi0IT%2FeKGjvOlBKsY4I6qS7BwCb8Kxa3V6R5QIgLgOXK1UQ%2Ffcz7Y6BSf4foMcOTYxOohc%2Fs%2Fn44KEoc9MqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9YZjNDTOi7wGB5HircA4Aalw1btWZdowgKy8kwjWOOLKBZmrNU%2F%2Fb4sY1FmQRD9xfzc79tihOS6RcV5OmnDBL%2FCvigZq0TL744kjrEn2W7ee9qR%2Bqp0uUpSWPGP3ixJArfuulTevs4nLloyOAKaqh05537sTLCLXz%2BFam1CfOe6uDVL8RG%2BpcolxCQu1RsfkeF0BGmddPeZsDE3c%2BDG6B5RpYphRiy1TGGioJ3q4qdCN3CtQFsX0k98dzCtJhc18tW5Yt0XGcN5e3%2F99zQL93TY2jmDGxkcEISRDqB3bCnGaB%2BevDq%2B%2BFbMTSvf5u%2BdrW%2BxRo74Xe0rYsBihdO%2BMlVRFJ%2BDP%2B1kbO3K9ZpO2Mb5blBrpDbMVfvz%2BRKXrOBeEuCuJvgB3yJnil80rrMaN4UWW1CO7yljpk4BokR2LXSmclOhjNWtkA79x91ICWD99AVLuG0C4MxQI1QuvPzMu4%2FbBMTrbsJ%2Bw%2F8ZxUPX88G62ZwxV%2B%2BgQ7olZM58sOaTwGPcymx3PvCtYKoNr1f9cgJEAGPqhCYMAbQRxOpenW1OWSy8jFOcUQPVLklqpawwVMYzFzHYljbjshjtL0k%2B5TAPPxWxmykgP1CGchhA%2BI8wqGMOvxlLNqyMgoN2LeyFlsQII79s27xt5VgMOei7LwGOqUBOQe2ZLQuCDZ4XuRTLjE9WisIwez0HCXHY7yIT%2F9cU7wis6PJL5H%2Byvtn4qP2zrklzxD%2FpkNCov%2FAVmAPKbTGdndgpAqVynJOcBAhk44o1Lw5luRsji0p%2BHMhizuXnE6c1CK7nYd4wuizytVffZOJgDC8eundFlnZCc2aCcRzsdkfwiIReLrktaJup42YH%2FBsQQcrl0xIZSHicwNIL%2FwqHVEzyqIr&X-Amz-Signature=2fa858f4de0d4247e4803847e44682aeca027d98d45dc751ab32af63c67eead1&X-Amz-SignedHeaders=host&x-id=GetObject)
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