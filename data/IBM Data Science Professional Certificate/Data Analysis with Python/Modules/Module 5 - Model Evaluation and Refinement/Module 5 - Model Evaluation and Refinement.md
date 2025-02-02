

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=48ee391450a23a130f7799968973e1b7961b207ee93f7ad6f7b498cf584236b5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=05ce7e29905233395fb68d3c85b83402b8fa0c9877160e8dc0afbcfadd8f685e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=fb510c1da38a953ccd435e1b5ef3fc73a31df16d4eaa5533e1132f3601955913&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=e98e877a5552e3e4ae32b75fdc023a366d5a279fedc1006ffab2dd2caf79279d&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=4f7c150d76ce48cedb1d3a39da0f71eaf0a0c534c61f87d5c783b52759e1da70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=46f5808fd59faf2118043474c9eb6fb807f1209273808ffc98f0939fd96abc22&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=a37626ac1a1d1160e19e3ee135064a59929844d4954a5b1bdacfa79ec53a8fdd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=69b41f42a37875bf9edcee801bed433159f878299eb8494772c2b8a83a784f2a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=151731b961a9867287ea4da1152444a3b216d6d3012e9884d3126417a0a3e41a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T7A4GRP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDapWPm3LVSiKPcZjctcJNvVUBVlBONda1soTnji2vtBQIgDpJzy4VgFM%2Fs2IFpjGztfnKkC0uNvkSVDXzrPb1RxiAqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHTrdKXI00eHaruFiyrcAyTaTDTd9TJ9VPXZPUyQHswqki8GyLoG30jYwqkNtVac1O3HbYZ1Z9H%2BAj%2F8woCDnceXgqSIq0CNs54nN8TKimPWKyj%2FnfC0I%2BTBrQyl7AYVZhhcqaPHL0WVrzhultAi%2F5o98yu4P1kT7vUTQC5pq%2F9sRPX8DUW4ulkwNEzBWaAKfmYiH3S%2BqB74WwVPEZBMb0YExVz3Ser8rbPaAE7PyX73KPJJqVOrmUS3juVZiXlXm1mYdsjWhOOalf1qIQXFORJpVZ4MEf9N%2Bsa7zsAN253yuwep2KN%2F%2BOCA6SWTkuRblTWAbi2pp8KCPjFoX6zUtYCzkPQypGYjMJjEJ9Mia4gnQmsO52VSlPhKdJoq5nKhGYydmckk7GbIdSu5IshB9CIPJ2C2Ru50SXhXJ7yDpKK6SJe5S22Tj6C3%2Fq2odRJZ63CB%2Fn8ZE%2BWX5wjLdsymhV%2F9QXK5%2FJ%2Fm2df4AYrxdYrAkLCfrfdBaPTjbV3BA4k2RGRx9bISBFtchqNlKQzLoHEO3um%2B8DdAQa%2BFe92qFQGWIMhX7KUnFhujmIWN9gaZoLXKsdHRh2NDwd%2FtP5orbdcTv0Hf93uH%2B61E24SH0vNu%2BO6sbMomh3Zr502NR1NWO8OCVLcFx%2FIK%2FHaMMJSc%2FLwGOqUBVWU5xGutbQeTVtycRx0qrmakuTpRBL6rm3ce2zzVXPR1EuNRDrqQR5HCx%2BtBQCWZVTBhqzmi%2BQm9uAVlFHNdHa8LCfJV0hhIoP2L%2BHIQI2mdBm842Wh6vhzl%2BzPza%2BtINJ49LeJmi8Gfdk6osJ9AE7TzgKlQGDnltRpBYgldChtOYMkc0181vB%2FGAlPxIbCfPC2yTPimqSfJzhsu7i5JddN5QsKg&X-Amz-Signature=88c701775aad7bbb8fde2b52fe15760035f1af2bdb73ac8409616eb6f2ad38fb&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T7A4GRP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDapWPm3LVSiKPcZjctcJNvVUBVlBONda1soTnji2vtBQIgDpJzy4VgFM%2Fs2IFpjGztfnKkC0uNvkSVDXzrPb1RxiAqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHTrdKXI00eHaruFiyrcAyTaTDTd9TJ9VPXZPUyQHswqki8GyLoG30jYwqkNtVac1O3HbYZ1Z9H%2BAj%2F8woCDnceXgqSIq0CNs54nN8TKimPWKyj%2FnfC0I%2BTBrQyl7AYVZhhcqaPHL0WVrzhultAi%2F5o98yu4P1kT7vUTQC5pq%2F9sRPX8DUW4ulkwNEzBWaAKfmYiH3S%2BqB74WwVPEZBMb0YExVz3Ser8rbPaAE7PyX73KPJJqVOrmUS3juVZiXlXm1mYdsjWhOOalf1qIQXFORJpVZ4MEf9N%2Bsa7zsAN253yuwep2KN%2F%2BOCA6SWTkuRblTWAbi2pp8KCPjFoX6zUtYCzkPQypGYjMJjEJ9Mia4gnQmsO52VSlPhKdJoq5nKhGYydmckk7GbIdSu5IshB9CIPJ2C2Ru50SXhXJ7yDpKK6SJe5S22Tj6C3%2Fq2odRJZ63CB%2Fn8ZE%2BWX5wjLdsymhV%2F9QXK5%2FJ%2Fm2df4AYrxdYrAkLCfrfdBaPTjbV3BA4k2RGRx9bISBFtchqNlKQzLoHEO3um%2B8DdAQa%2BFe92qFQGWIMhX7KUnFhujmIWN9gaZoLXKsdHRh2NDwd%2FtP5orbdcTv0Hf93uH%2B61E24SH0vNu%2BO6sbMomh3Zr502NR1NWO8OCVLcFx%2FIK%2FHaMMJSc%2FLwGOqUBVWU5xGutbQeTVtycRx0qrmakuTpRBL6rm3ce2zzVXPR1EuNRDrqQR5HCx%2BtBQCWZVTBhqzmi%2BQm9uAVlFHNdHa8LCfJV0hhIoP2L%2BHIQI2mdBm842Wh6vhzl%2BzPza%2BtINJ49LeJmi8Gfdk6osJ9AE7TzgKlQGDnltRpBYgldChtOYMkc0181vB%2FGAlPxIbCfPC2yTPimqSfJzhsu7i5JddN5QsKg&X-Amz-Signature=2ef088f53508931dd58e56cb00983c7cb17be23008711f9ce244dcca4ab1957d&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T7A4GRP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDapWPm3LVSiKPcZjctcJNvVUBVlBONda1soTnji2vtBQIgDpJzy4VgFM%2Fs2IFpjGztfnKkC0uNvkSVDXzrPb1RxiAqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHTrdKXI00eHaruFiyrcAyTaTDTd9TJ9VPXZPUyQHswqki8GyLoG30jYwqkNtVac1O3HbYZ1Z9H%2BAj%2F8woCDnceXgqSIq0CNs54nN8TKimPWKyj%2FnfC0I%2BTBrQyl7AYVZhhcqaPHL0WVrzhultAi%2F5o98yu4P1kT7vUTQC5pq%2F9sRPX8DUW4ulkwNEzBWaAKfmYiH3S%2BqB74WwVPEZBMb0YExVz3Ser8rbPaAE7PyX73KPJJqVOrmUS3juVZiXlXm1mYdsjWhOOalf1qIQXFORJpVZ4MEf9N%2Bsa7zsAN253yuwep2KN%2F%2BOCA6SWTkuRblTWAbi2pp8KCPjFoX6zUtYCzkPQypGYjMJjEJ9Mia4gnQmsO52VSlPhKdJoq5nKhGYydmckk7GbIdSu5IshB9CIPJ2C2Ru50SXhXJ7yDpKK6SJe5S22Tj6C3%2Fq2odRJZ63CB%2Fn8ZE%2BWX5wjLdsymhV%2F9QXK5%2FJ%2Fm2df4AYrxdYrAkLCfrfdBaPTjbV3BA4k2RGRx9bISBFtchqNlKQzLoHEO3um%2B8DdAQa%2BFe92qFQGWIMhX7KUnFhujmIWN9gaZoLXKsdHRh2NDwd%2FtP5orbdcTv0Hf93uH%2B61E24SH0vNu%2BO6sbMomh3Zr502NR1NWO8OCVLcFx%2FIK%2FHaMMJSc%2FLwGOqUBVWU5xGutbQeTVtycRx0qrmakuTpRBL6rm3ce2zzVXPR1EuNRDrqQR5HCx%2BtBQCWZVTBhqzmi%2BQm9uAVlFHNdHa8LCfJV0hhIoP2L%2BHIQI2mdBm842Wh6vhzl%2BzPza%2BtINJ49LeJmi8Gfdk6osJ9AE7TzgKlQGDnltRpBYgldChtOYMkc0181vB%2FGAlPxIbCfPC2yTPimqSfJzhsu7i5JddN5QsKg&X-Amz-Signature=0f4a3347a8ef73a3517b9ba15d1c14ab24a3b1bb08e0b01c665edeb6406166cc&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=d679601e2e8dfc84be104cc031ac060af5f49ac7ffd5817ce0174823b54f1322&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=e479ac44b5fee0a78c681628112fe6ca3ac6a563851a7e4cd86be63322d9a447&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=07129907c07badd87cf0331434deb3d430723b9b58f38df57db6bd7b455ef06f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=f7bbf2da2e23eafbca5d6932e686577e70193ce9d32f4b7bce0857f8ecd7ed60&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=904cdf693756c6fe93a6382ddf40587e7b7a815e5f54c75557081e20a611a9d5&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JWMJEF2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdMAEgeIziZlulFNMOFyI4NVODVHZjhuA0w5rDY%2FgnzAIgDBUDIjTvr1ym61LOIcdFZWJ79LmC5EPn3Kdkfp96ad8qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLWwOLU%2FrNE7JOmPircA4nAECu7J6O%2Fi9x%2FFkKPOZVCIV80jbIoIRJfqRcMkAQE7NXXUKhid4LBIDX3Fme6DGlLtCrHD2Waa4TL3I%2FNkg676C5vkh2p1EZK919aoc3fP2lgno3lEdBAeHl0P95uH8M1HcBpHVvCPWvN9vIlOnHLQblftDw5gVRBbyZade5dUHoFs1f60qubm%2B5uxJeKDtqfLmMKd5HcWBBS7tFEGQZgZdnyRNGuAhZv1jBM%2BjrCd6JPDW4k%2B9YmCHoZF%2Bj3C7EW9OdOkX2NPxwOcCpiuRooA5rvUKsX8pBdpgpb6482JhHRdOMuQG%2ByY1GxGKadsJHSzs07%2BcPqlw9v52o%2BagSdZp26Ei14TvZD99W%2Fg3%2BgbZzehILuG7cAbKs6xPHtS3Ihwis1i20nduiReyAWkaTp2ZCbOxPAQxUGRPzw%2FeivxnWPH1QMVIgSxtQ7fKB%2FklAoI8bCCnBA1ZEV%2F63LjaTUHWqXMtu%2FsvzHCCImgIMB1zwKpBOupHWIHnLEUy3FelWxGNQsNAG7wBaEN0et98fHLoOFTX%2BVWpagEZSZ0qPIi%2Bj3cXgNSgwWG%2Fobt5yFN5gAHvJBmlDo%2FFOmNEdKbRoSW%2FS7tRUD80PCwrRKDpu1sVLJJypZ2LdDk5%2B9MKKc%2FLwGOqUBakdtpeqlK893a5p0uimnyf2FoHf5sBylwaE5VZaKwKI41a5AOhbpP0g4PF2j%2FRwmkFf0xnnsDDOQpgaVoEs4rPyJShUaesAPQNUl4clreN8GOPWuiyrd%2FxwNSfRfgmBS%2B458ij1etFw%2Fmgh9cWuQI5roYwHAg%2B2j%2BNCL1bJVD%2FmA%2BhjiO311TgLg8DqjeC%2FdvrmMftac8pnBvHyhyePYAe23gkSq&X-Amz-Signature=b4eed23303736a553be88d8c22884a27aaab6266dc43670d186f041e314622d1&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2UHPETS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHgkIc8YRTYTqd7cUDC5NoQHrq5HaENBwxXvp2SwR3EhAiEA2aGA6wF6r4AUN84aIRPI%2Bca%2FFa%2Fzv5llstNK7Da0sVgqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB8IJpX%2FZxP1Dt2O%2BCrcA6HJ9h3asj2ttgQJDgkeix3QpSRN0Mx1a%2BKjHIGdSbtPv0xyEIwOn0dH2MFINwQUoKthp9BKWRxbvVqEkN87s5VvJ3q%2FRhQFwOZT3wVv8KIZscMQS3QMeHl1KCvbyx8%2Bhp3kh%2FdNCKNdD48%2FOptGdN%2FJfki3WWSGkKUXD9OMNPZsTRn7FnN9KcZvfp7xUR4x24h4SDghFe6GYveaBnuAreCLrtjrJIL2tSsNrnfl5xfnJYTQiQoMWlUXJhV2aiEkzV%2FUyy1%2Fai1Umt0Ucftf34P9aR3%2FY%2FWyjYF6wdb07ilBsKz5YPPiR%2FpEtJ%2FLJYSymlBguiUA84Nw6PpdF%2BCNzfUC2zqdPNPpl951YGbpivFB1rUMhyr14x231l14WtNUjpCqn1hpHfH3fj03rFaPrHNUIE8zwpKLwmSK5xhs4ZQBYSJ%2FaG1AhgReLa1VBhfgXfJN7F0TvQP9Ks9I22TWgtn%2FWj1FgCeGiWVhAiaD53LGg86UJkGobXTRFEoRzqn2BjWbVtCHu8XG6P6LGdoSdUOAMU%2BCn06opajDv0DnSiX%2F2gucEYNnm6uPFNDbzXxzUYeBY%2BZUZ8pntJi1rH17jQa6zVoRR2H02rx1VCwetc8OOOkB0L5VTCqe5WvXMKqc%2FLwGOqUBrI17J0CjwtNMrSPt2zoINCfmiCbskFBhl9y2IE3ZQsK5%2F7GFBSinQI7ud7JuGab3CqPqYFH6EB85bCh0VlG3RGWcSHKG5ww0mMebga5gEdOHje28OssBIaLCsYabDdDN0pOjAlpDcS4uDliSqC2ClycutsnHib%2F6jOn%2FYeSPS9uE0PuyCNz789qdxNZXJCIEH0tEZ36DqlQLF9ljeNEzgtCA21kp&X-Amz-Signature=d968dd19a63d6e90557219f4c16bfa89d301ab14b12a70b4b28c60d7d56f432d&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2UHPETS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHgkIc8YRTYTqd7cUDC5NoQHrq5HaENBwxXvp2SwR3EhAiEA2aGA6wF6r4AUN84aIRPI%2Bca%2FFa%2Fzv5llstNK7Da0sVgqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB8IJpX%2FZxP1Dt2O%2BCrcA6HJ9h3asj2ttgQJDgkeix3QpSRN0Mx1a%2BKjHIGdSbtPv0xyEIwOn0dH2MFINwQUoKthp9BKWRxbvVqEkN87s5VvJ3q%2FRhQFwOZT3wVv8KIZscMQS3QMeHl1KCvbyx8%2Bhp3kh%2FdNCKNdD48%2FOptGdN%2FJfki3WWSGkKUXD9OMNPZsTRn7FnN9KcZvfp7xUR4x24h4SDghFe6GYveaBnuAreCLrtjrJIL2tSsNrnfl5xfnJYTQiQoMWlUXJhV2aiEkzV%2FUyy1%2Fai1Umt0Ucftf34P9aR3%2FY%2FWyjYF6wdb07ilBsKz5YPPiR%2FpEtJ%2FLJYSymlBguiUA84Nw6PpdF%2BCNzfUC2zqdPNPpl951YGbpivFB1rUMhyr14x231l14WtNUjpCqn1hpHfH3fj03rFaPrHNUIE8zwpKLwmSK5xhs4ZQBYSJ%2FaG1AhgReLa1VBhfgXfJN7F0TvQP9Ks9I22TWgtn%2FWj1FgCeGiWVhAiaD53LGg86UJkGobXTRFEoRzqn2BjWbVtCHu8XG6P6LGdoSdUOAMU%2BCn06opajDv0DnSiX%2F2gucEYNnm6uPFNDbzXxzUYeBY%2BZUZ8pntJi1rH17jQa6zVoRR2H02rx1VCwetc8OOOkB0L5VTCqe5WvXMKqc%2FLwGOqUBrI17J0CjwtNMrSPt2zoINCfmiCbskFBhl9y2IE3ZQsK5%2F7GFBSinQI7ud7JuGab3CqPqYFH6EB85bCh0VlG3RGWcSHKG5ww0mMebga5gEdOHje28OssBIaLCsYabDdDN0pOjAlpDcS4uDliSqC2ClycutsnHib%2F6jOn%2FYeSPS9uE0PuyCNz789qdxNZXJCIEH0tEZ36DqlQLF9ljeNEzgtCA21kp&X-Amz-Signature=382e5949eb3492712108a27780465b44515db2c5ab3234bb98e751226ad4d064&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVPKGR3O%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDIDqNEzfH0lJsFF4dTeH0PTIn21WlL0y02408H6nPLwAiBKItg20FDhuMryyfk44msUUiDMIlTf7DNwpGuzO0x1OSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM60GGyxHIDqihCnKeKtwDj0LxwOB%2B1%2BqndzdJIe3KCIrc6towTc2g8LalIJvL8ZsO%2FkzYZLQ1sIqDr9zXuovJuizruqu%2BZO8KYzs9nluuZtAq%2B7WAcJ84UDriZwicby3ygIeh7g0tJ3IBk7m6QxrCf0Ne3QXGNqhjkoeeEC1zAKTyLM38yaj9KAJkUXabTE7gE0go851dspMaAKkFfzseiee4IVmal5PY2rWckc9AgCaU9mmkh2ndiI6d5tjYm7xFg%2FOlz2PvW0Tll%2FXogM553HNDoqaA%2F%2BCLXYFLfUcr12uatOM%2Bix1%2B7zNMTk3lcZZ0H0dQxNIdY7WRlavEWHHEq6rO8Hzvr9VlgUA12aZ1j64TBr08UQ56tzvfoOwfBh94aJgoYFzyoT1fS05EcCOLKp64D222RA8bWmmRgNTUM4yf5cml9vANcF4VZ%2B8fFSQmHN0iQDfsrfmG5BtzkCI%2FVvhenEIMlfsbkFwsVjB6SukvYTl3YuGFoWhuAqjLonwI6CnLsmDrk7xsPPaGp3NvfqXqcCSz9ofD77H%2B1J9QeRovRyfbeJlE6pas1aidAeIRN%2BGH%2BG9%2BmWjgNSRteQgzuzmerHaqT%2FzGF1igiLjMeV78tMlXbInoWOCJ219OtX%2BUkRgKHExNStv0MhMwoZz8vAY6pgFdlP33yESY%2BGein2DyaiBMSXxnFlbCPBE7d4ST8%2BYNA56pPVldFHbHc3ZhpudrMtpJ11xhH8jX%2BBYg9s%2BBjP0MwU0XBAq2ZqvF3BLvNN%2FdHnaVRjZnEcWxLFaA5%2F6kbZkBEJrKeU4z%2FyGoaD4hjF%2FRO3UlV2JcbtcaoPCeWBpAqURs%2BFJAikppWOZxBw5h3zswyPFhLU2S8BwDiD4IwgA0rtMtRX7W&X-Amz-Signature=64e27b326e232f1daae600742f17641c79308d428d7519ec99a0802e9a6d93c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN3MHDYT%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T101345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1JZBQy7BCqZKJUad2HwIvK0ObupdtV%2BIRajdDpfV24AiEAhQg%2BR9dPLXtuCV8CNYsMfWT%2BZwWBAiEV4y2BoUmiH%2FMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrMmfgwiLoNCzQwpircA7igXB9AakY4kUE2yUsUtKojn3bctj9cv%2BMHp8Ty%2B0ipSlEVvNmyr6nP5Rt4IsRYLM84zI%2Bb96O75eK8lx5orgF4QlR9dWlQ7n0EXmNfj0JlDxuuRtztUj%2BL6uku1dwTFQmoXgJO0Kffw%2BaXTN8VxAgWNNQD638uBp4EWY74VIiE2iIiQl59TBiSn9lYefmD0jukWAg8jLFeRamcaeXV%2BOa670iBk5%2BufSUOQdnSgffqyBbGS%2FbNeiQPs8RYBn2RcewGOwX6beIPFEPXcFTFFUypuhtwz04bprxs0RTpx%2B2Qkoz7GAFH1%2FzCccQfh1hg1xq6Y3%2F6Rql7uCYuOHOSUNdG63n0qLFcY%2F2RDDV%2F4f2Kg3IWsna5Sdn15pjRpgAcYrk%2Fb0ynaE%2BjMDViOz6PHpiA2Kgenmox8YoGetOok2LIb%2F1XMuJ2ZpFvkEntVVau5YnKCRjCyUdypvVVG7n1uM2bgGKCQcx9Z0PP2ovSDeHaDdsyxIQ1VOBPfWSYskxaNKCLYzTAxxr7a0yOKF9IM1H1huJheBuO8pXgKpeWj1j%2F0aF0tUj9nU%2B46bozSuZ8J7D7%2F%2F7yvLKPEc8JNjkWhzqQmdXSf6dBEoM4MXl%2BKpMfYNsJ%2BOvC3FqO0YtZMKac%2FLwGOqUBY84RtZRP3IpFlsR4ShoRmjWrZcCK8T%2BCTf3VV%2FB%2BwOLPeshyZ3hZjfvLyRNsAowl4dBx3%2BmIqhTptQPFKptldZ4CEqNdld%2BffQ1wwxr2N0qVdcupA0Ezqbke8273U3EgJ8084K9RZrlFqDqvfKP3DNyQ63g4%2B1Tgl2IFKHFCgwti71MSIEPkZUShc68Iqc2ADrVkHHscBxvOGQ2a59oyQMJYnfZJ&X-Amz-Signature=9a9d3ecfe2d8d16ec8afde91faf1c62a6cd74c3ba9935ae25dba46dc2164bf28&X-Amz-SignedHeaders=host&x-id=GetObject)
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