

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=0e27350c1c02401fa211cdd4d023e718d1c7f6c181a46a306eadfb7a2053c7ba&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=e42dcb6a665a2b60ef77369a0f5159fadac151305619f19dd909d3448cf88633&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=322411aa0603e45258ecc8c56e8f73c9ca1a6d2094cb556620200fd92e463f0f&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=f31edff9e47b92bdc57351291a43c09235d449d12ba29a42af5f75a52e1d2036&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=8e0b36424cb87c6a629b52424ca5cd44333aef909151e5a6af5f7c003681014f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=8440313a0860c8db5db33b5c26aef4e0e175116fb0ef5230a5ed09ef5ef58fbd&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=477d04b90a121edb79d03fe1c5119a2da6d75f19244fbf9fd0530b5b00734579&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=6cd41ed5c19d9d99f160deb8ed78ded7c71adf0faaf22f6ccdcb5355e787c1b5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=a251d060abfe330a8d3f8013512fef1eadacdb696c89cd66a88060ed495adac4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQZ4BRB5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTj5sJ7XSA6ifuRyb48K%2FfgK%2Fbfvt9wugmVLko%2FcyQcgIgbxE3gVZdjhATgfrnJgTmubwfY%2FTZ%2BxIJpjPeFtVbvhYqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNNDkQAVHaOTelR0CircA1nxv7XEm3kZHY%2Ff0nO1%2FJvk%2BYIT1bTNO3zsBD9bx1htZLyB%2F18T3CJLzVnSijq3q2npQrRYpqlQUgtWxVZyAFtvlrm7UdzhYSlKCA3kVOCga1FB1qbX6QQoMwaRPEIA68FVP2d9Ar0gipphldtocP7vURA1phZ6afABXf1%2FCXh4GzlVWpKwA1ac%2Bu5L4TzFzytOCdZ986nJi4Ff2n4TSzgj%2BroTHFxYn%2BK%2FuJxlT28dhphgslgKyZih%2B%2BTcJK90OZ0aJoSueKSRks2vttG%2B0AdHU9EWmXkqjVaqUz4eaBvqoSsdcDYGorQuW%2FQb4MC6Koyg8mB%2FHhxgQLc6wRSaXBjnRB9H8qSgIUVIFi2b1fmYPeAWPVxfSX%2FI5xWYz7giXBtOJrCQnht0stmT1vG0AzXoYsQsgPQLdjGmKxclr0XkmjWYCH%2FumD0IPWKzyIvSRXsMPTxF6ylixkzbSkFESqWduj1cSCyJsMFZ9JjW8S1LKkl64xwrAeHr076%2FqUvlXlw%2Fn3KoPNcNi1nQiSpBBYEF6UZSaSJLvK8cCYj%2BBTq0qVAXmAGLJQ7P2UKyBo9K9Q9Ceq720A4W%2BC5nzEeuTsigZ%2FgtfRbVjG3NCRPNlzRR0vMIsS5eRbhx%2FV2XMJyq77wGOqUB%2Fzypll94vVHW%2BwzSp0yTe6lW%2Blo2pIs53Dbh2Rrd79g9f3ucV2xLo9ThUEgbp9SVOFOU5wuAMRiL1B8mno%2B%2FpGEsMRd%2BFvq8atyOYtA%2BfaYD6XivTVJW6i%2BXVloIr20ZdyhlEFDf12OgdO5RPtao9YfqzQQE0pZDWvDN46h6UVCZtVt1bdOl%2FGFhpfkiMx3I%2BQLxo9sAfaJiut5PYOEFL7Ooq7Y%2B&X-Amz-Signature=0d4db1ba5b023e65ea536e939589ee71b197a8704cfc5e31bade3a3219b7652f&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQZ4BRB5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTj5sJ7XSA6ifuRyb48K%2FfgK%2Fbfvt9wugmVLko%2FcyQcgIgbxE3gVZdjhATgfrnJgTmubwfY%2FTZ%2BxIJpjPeFtVbvhYqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNNDkQAVHaOTelR0CircA1nxv7XEm3kZHY%2Ff0nO1%2FJvk%2BYIT1bTNO3zsBD9bx1htZLyB%2F18T3CJLzVnSijq3q2npQrRYpqlQUgtWxVZyAFtvlrm7UdzhYSlKCA3kVOCga1FB1qbX6QQoMwaRPEIA68FVP2d9Ar0gipphldtocP7vURA1phZ6afABXf1%2FCXh4GzlVWpKwA1ac%2Bu5L4TzFzytOCdZ986nJi4Ff2n4TSzgj%2BroTHFxYn%2BK%2FuJxlT28dhphgslgKyZih%2B%2BTcJK90OZ0aJoSueKSRks2vttG%2B0AdHU9EWmXkqjVaqUz4eaBvqoSsdcDYGorQuW%2FQb4MC6Koyg8mB%2FHhxgQLc6wRSaXBjnRB9H8qSgIUVIFi2b1fmYPeAWPVxfSX%2FI5xWYz7giXBtOJrCQnht0stmT1vG0AzXoYsQsgPQLdjGmKxclr0XkmjWYCH%2FumD0IPWKzyIvSRXsMPTxF6ylixkzbSkFESqWduj1cSCyJsMFZ9JjW8S1LKkl64xwrAeHr076%2FqUvlXlw%2Fn3KoPNcNi1nQiSpBBYEF6UZSaSJLvK8cCYj%2BBTq0qVAXmAGLJQ7P2UKyBo9K9Q9Ceq720A4W%2BC5nzEeuTsigZ%2FgtfRbVjG3NCRPNlzRR0vMIsS5eRbhx%2FV2XMJyq77wGOqUB%2Fzypll94vVHW%2BwzSp0yTe6lW%2Blo2pIs53Dbh2Rrd79g9f3ucV2xLo9ThUEgbp9SVOFOU5wuAMRiL1B8mno%2B%2FpGEsMRd%2BFvq8atyOYtA%2BfaYD6XivTVJW6i%2BXVloIr20ZdyhlEFDf12OgdO5RPtao9YfqzQQE0pZDWvDN46h6UVCZtVt1bdOl%2FGFhpfkiMx3I%2BQLxo9sAfaJiut5PYOEFL7Ooq7Y%2B&X-Amz-Signature=d33fca4f717bdf1c3e2a671ffa53f6e7b7a950b885faec1731182e144c815616&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQZ4BRB5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTj5sJ7XSA6ifuRyb48K%2FfgK%2Fbfvt9wugmVLko%2FcyQcgIgbxE3gVZdjhATgfrnJgTmubwfY%2FTZ%2BxIJpjPeFtVbvhYqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNNDkQAVHaOTelR0CircA1nxv7XEm3kZHY%2Ff0nO1%2FJvk%2BYIT1bTNO3zsBD9bx1htZLyB%2F18T3CJLzVnSijq3q2npQrRYpqlQUgtWxVZyAFtvlrm7UdzhYSlKCA3kVOCga1FB1qbX6QQoMwaRPEIA68FVP2d9Ar0gipphldtocP7vURA1phZ6afABXf1%2FCXh4GzlVWpKwA1ac%2Bu5L4TzFzytOCdZ986nJi4Ff2n4TSzgj%2BroTHFxYn%2BK%2FuJxlT28dhphgslgKyZih%2B%2BTcJK90OZ0aJoSueKSRks2vttG%2B0AdHU9EWmXkqjVaqUz4eaBvqoSsdcDYGorQuW%2FQb4MC6Koyg8mB%2FHhxgQLc6wRSaXBjnRB9H8qSgIUVIFi2b1fmYPeAWPVxfSX%2FI5xWYz7giXBtOJrCQnht0stmT1vG0AzXoYsQsgPQLdjGmKxclr0XkmjWYCH%2FumD0IPWKzyIvSRXsMPTxF6ylixkzbSkFESqWduj1cSCyJsMFZ9JjW8S1LKkl64xwrAeHr076%2FqUvlXlw%2Fn3KoPNcNi1nQiSpBBYEF6UZSaSJLvK8cCYj%2BBTq0qVAXmAGLJQ7P2UKyBo9K9Q9Ceq720A4W%2BC5nzEeuTsigZ%2FgtfRbVjG3NCRPNlzRR0vMIsS5eRbhx%2FV2XMJyq77wGOqUB%2Fzypll94vVHW%2BwzSp0yTe6lW%2Blo2pIs53Dbh2Rrd79g9f3ucV2xLo9ThUEgbp9SVOFOU5wuAMRiL1B8mno%2B%2FpGEsMRd%2BFvq8atyOYtA%2BfaYD6XivTVJW6i%2BXVloIr20ZdyhlEFDf12OgdO5RPtao9YfqzQQE0pZDWvDN46h6UVCZtVt1bdOl%2FGFhpfkiMx3I%2BQLxo9sAfaJiut5PYOEFL7Ooq7Y%2B&X-Amz-Signature=d576eadb89a880f54684b2795f60fcf1ae01970666fc7e6606c7b492be0f9966&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=bf2d0c4640d5d6ae00f2f54f1169d9fa1f7c3f712e0a688222bd08ce87c87356&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=52eca39c8d25bc30c67b212ce9af2bf09e64d17c216800413313c56ef121ef37&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=75d639c55c7fae3b2661cafacd53235ed962ac4f22b211d20023e0fe75aa469b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=b4d671753eeecf598ee5aa28fbda4312572117d4866e99fe6f43847224eec029&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=991e75196e264442282cf387e3e91993198aeb9688f04642808ac0d6379c1e8c&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UJBWMPS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDi3wd9ZOgjjr6jvB0vnVNJdOUSvUl6huMOIWDtgGwfcQIgK2DFiQqpVeLT965brxbnl6Y%2BEJOKCt4Zq%2BTTvPu%2FnUsqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFCtSxdcYqiRw6Ka5SrcAzdKC%2FiIXJtKCTDLl02t7ovJNQAprsQr%2BQjNgkPdTKr6%2F2UEFuSVdpVR%2ByAeL7VT1kJ%2BLPnup%2BYo2rYjlTMkuGv%2BkXNbl4ptII0BltjEFCu7dJ9U7YO1RAd9deQLK%2Fx0ukndM1%2FfSPwwanFS0ZeTnD3WrCDzMOcZOYhPkk7GiPmMFU6jn0tcXeGMeODU92PFCO4rdwB6c2sBr7EaaT%2F16A0ZM%2B0%2B%2BD1IZ24trqSVPQv52M1bKl3hcuMkiO0FUHx9Yfb30JbjAyz8p9bLUDHaggEbUwQqZ0Sdze8OIIlBpaSitWRMIFySC63LF7n%2BczNyUE93lc%2FmnG6%2ByAGUSk7PGC2pFyFtDg8iQsl9Njfm5xc%2Bt90yXXUKmJxzUTVSGBcHW65RCOs%2BgXw0ha4Mb9O1%2BU%2F4dyaWN1GRC2YWV6JGdb2hJWzaZpK5tt25%2BnwiHWWb2vXkxwKU9%2BhEQEy%2BbcKIZD%2F5f2xfGg9kTYmySzgWK36kMAKXkkOPST2F0mkHJ%2BRvkVqYRemYJvakCb7%2FVHyc4o31XeOrDUGEltvjND6lEFlr45tzOhr9M5XZnbNufh6PDq7saO5AWiDY4CcCHwYTpQ9hd1fICaLRcDOhyivUaj7Z4K278MUAB59Up5TEMM%2Bp77wGOqUB9iO1u6ifPePF9%2BdA9MjIo0d9G6cQzKeHbjAuiIxDeVFt6V8f6pJCSUxPftQrzMv5dxck28rPYDoyAcXGT0AeNe1Iw%2Fs84LOnrqVqbMGnYCjk%2FvZRggD1Ii3A4eoW%2BnBqI1RcUqyPy43zCr05TB8iBXGZ%2Fd5fju5lMXyccrVILq8cJJx0BNVq6n7VorlKAL7tp46M%2Bkne14GxSZ6PeSMlvSwoM3RD&X-Amz-Signature=0235cdb26fa7c8fbe25958ac1525bd28f6352362818e57bbc0cd84b9cc32adc9&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U35GEK3F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeth6VUicfRbc1%2F8opi93hyYcNSBlaxdiN%2BfsYMVCRwgIhAP8R%2Fq8DA0SAPT8oYDc9JGSKsRa7jzZNH50dcgFqWYDLKogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfxinwOHrRnljc%2F4wq3APlzyHSk0UpaTxteWuHGdWnkpU%2BTpo4j3%2BIa8H1KxLj7Kw9y%2B%2BaWspt%2BeBIX21sM4Rcxo5EyxCwBPx0PT04kqZv2SL78%2FlE3Np12h48GIB32KxUtZaJm8ZEl%2BdrgbkVWX7fjJ9nVuddPPB7V3uvKCfPn3kCIMrGpdM5QM0Zc7BmGi%2B3dTp%2BdR9B%2Bdf7PyYL82dJalTXUC3C4ePS3KQzCsJwnOxza%2FhNmhTTvLDG9FjvVcCI7ANYsNxl26vLRpD1X%2FC5hhebPXT%2BwcG6ea8159Sd8J%2Bxr%2FAK17XegdWT9kIq7xZLrx2EDDFBl4uoPC9Dv%2F8o5S3GHh3rhkwQ%2BBK6ffqu4z%2B7X51e%2FVNIT5lG0JsPkDtb2emGCwEVILUojZATcl4m6OTvZ9nOGKzIhLAzJkJlLwdGaMs%2FJ8bEpLiiZnweWT%2FTmcC5dAMMqz6z3S3IZ0TZN0I8uWqCTFWtBjwzhi%2FtgHh17H1lUj3H%2FT8TAjpsxnl4KrZfSe3P9H8%2Fu3Ip0mJxEBtGX12Oc3JmrWO%2BElzKGcKc187pohp7S6ySIqpLEVPSJBTT13xFLiQSDIW19WhRBgJwnlAy8BOJXq9AEsp7P4%2Be7TIOIE59WbiU%2BxrtA8LLZ2EpNoSB%2FJlHIjCSqu%2B8BjqkAS6BgMhsAmUWX%2BlqGHGSj7%2Fj0zCvdYPSMwqQvKmaoo3hACHt4DqyVvFcPe7SnbuDEChmIdXb4Mw8agWzvp76H5lh8s0cvskHSwStwyXBiFQjD2z7Rm7ksWmi4ZUVKn%2FDL7iTeZx7WDQFaZVbPMApj9CDMUV%2BGBb1hN1gMWsBjOxzLvxehcFz5QPxMdUBb3TXgp6S8fBL9olUgY8Gc06%2Fo%2BeX5ZtR&X-Amz-Signature=b6b2aca5f249c317824e12895cf357fdfcb60e7e55c0380fa816e319b0bf4357&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U35GEK3F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeth6VUicfRbc1%2F8opi93hyYcNSBlaxdiN%2BfsYMVCRwgIhAP8R%2Fq8DA0SAPT8oYDc9JGSKsRa7jzZNH50dcgFqWYDLKogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfxinwOHrRnljc%2F4wq3APlzyHSk0UpaTxteWuHGdWnkpU%2BTpo4j3%2BIa8H1KxLj7Kw9y%2B%2BaWspt%2BeBIX21sM4Rcxo5EyxCwBPx0PT04kqZv2SL78%2FlE3Np12h48GIB32KxUtZaJm8ZEl%2BdrgbkVWX7fjJ9nVuddPPB7V3uvKCfPn3kCIMrGpdM5QM0Zc7BmGi%2B3dTp%2BdR9B%2Bdf7PyYL82dJalTXUC3C4ePS3KQzCsJwnOxza%2FhNmhTTvLDG9FjvVcCI7ANYsNxl26vLRpD1X%2FC5hhebPXT%2BwcG6ea8159Sd8J%2Bxr%2FAK17XegdWT9kIq7xZLrx2EDDFBl4uoPC9Dv%2F8o5S3GHh3rhkwQ%2BBK6ffqu4z%2B7X51e%2FVNIT5lG0JsPkDtb2emGCwEVILUojZATcl4m6OTvZ9nOGKzIhLAzJkJlLwdGaMs%2FJ8bEpLiiZnweWT%2FTmcC5dAMMqz6z3S3IZ0TZN0I8uWqCTFWtBjwzhi%2FtgHh17H1lUj3H%2FT8TAjpsxnl4KrZfSe3P9H8%2Fu3Ip0mJxEBtGX12Oc3JmrWO%2BElzKGcKc187pohp7S6ySIqpLEVPSJBTT13xFLiQSDIW19WhRBgJwnlAy8BOJXq9AEsp7P4%2Be7TIOIE59WbiU%2BxrtA8LLZ2EpNoSB%2FJlHIjCSqu%2B8BjqkAS6BgMhsAmUWX%2BlqGHGSj7%2Fj0zCvdYPSMwqQvKmaoo3hACHt4DqyVvFcPe7SnbuDEChmIdXb4Mw8agWzvp76H5lh8s0cvskHSwStwyXBiFQjD2z7Rm7ksWmi4ZUVKn%2FDL7iTeZx7WDQFaZVbPMApj9CDMUV%2BGBb1hN1gMWsBjOxzLvxehcFz5QPxMdUBb3TXgp6S8fBL9olUgY8Gc06%2Fo%2BeX5ZtR&X-Amz-Signature=d511e8a8a307cbbf1496ae9e476d27e0ecdcfdf26bd59073dafc0975788d3342&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PPN2366%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFkGnpIAGaxDaIfWx1djAbEIwjebQhUNLSNpNbjv%2BLZAiEAkKgkV5CRA9DouYkEDjVUxv%2Br4I31mB6IZ9aepfM5%2FUkqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMO4ztt4RuKWwdZ0%2BSrcAy0Bai%2FyNXlrFBIu4acqV%2FVpbNC8RoRJlLem%2BRkPL9aAoXhNsEO0VgV%2BMkpImlw8CrsMlHLHzxyuVUD9FU2dSfc9BxRTFeMQpwYY04ixaUtwJgyhSdwaXCliXgRQ5Q0TyTcsyJ%2BUDehjKN8iSRnAUG4HJo3Z7%2BG1nlnq33%2B9Oi3%2BQ5vz2kYEPFMRF8jHODV3v24%2FHNAR3xcrVLBvYl2BlZCkAJf5DSIP8t88SnIR5CpuoDJ8HNQ0YqwJKTxsfxm1138XGzhSnToj1ef3yVHKx4QUYCJEVvQp3ED%2BBbHJvgY%2FkBzu2sdTvQS5eQ5B3tzrnZ10OCT31IV1HwQiNfBTVAj%2FilRi8V81iuwyp1irJKIAP86Lk5WhSakGQzOVD41%2BfpKlqUm7jj6a81o1%2Fk2iEqCxkJ%2BkKkPvvssrECm6r0XmQPAbw31Ubzz2MREkOJQMCPKsfxrzckjVABMs1r7DXoTRBb8yuCTJ6j857HGhzMA8NugKRG4MTDuXozJm5JUj8kEaBIhrdo30oUwjRPinvIxqFUpJJMIEuT8cpORQ%2FetB9Y%2B%2FHUNDNuAVJ1NvfhxMs%2Fdc0wXQBLFJ%2BaG7NnCyLsq1EMv1M3SqDQ%2BYNsE34FEqx3uG6iScoVGtJm%2FzMPCp77wGOqUBpjurO5sxPheLiRVaCuBaLFBVajlA29MJdSjhTudahgmNP7WA6rpEbQIzTPDRGgkiNz7mwwwyXvjd66365K5DBAS76ABKRykoXhmbzEMxgPU6gtB0ysDVqj8pEbyhaW5jtVza3%2B8hF0Z9CR%2B%2Bd2vrctGz%2FGqj7ThF0ALPmtOijLDEswNKxkinVbsQwpbfpJES31kKfjzX3heUJm5Bxydtegre%2B05%2B&X-Amz-Signature=f9c6adcc06b353dfeaaefc79738e05c7cfe0981f84a0a88ea83d92d4a0c21c62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXDHECEZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjQrGGvlWtfS9GOj51lOfxH2EqkgJQt1F4NR9qtRfpdQIgFoTph3gdYls6VdNhcyJMPNLZo9dtUqNC3vYqqJw%2Bg0UqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCBIXsliZTm9TfZ37yrcA5G%2Fk6ksTPlMZyXbcPM2s9lQ1tLwVPRZ02eBYERbEawDLfhPdkBOpVTNAMYkmDMZTQkDw4mbUkjtxb5LihxuFy4Zehv5sodxRnJpk3%2BicUROskK3TN2mHi%2FOJPhJR9SANuYkrjoBmh3Z4jGdaNdfGbbFfAcibHQl5lYAY7Aacr1mw45lDmCgL1ez5SKVfTF7HBnGVDmTb0y7MODSZhdXyo1rpfn9lKkCDKRuSpzitF3yPmykRMzRhYog67nmc0sH%2F6W10D2GsFQQ2bZKXVp5%2BK3jAvRsoWfk5niG52jND1PPvlAjPFRXTsqDoOoVnySSy2l%2FiERHmJd9dCyzZYwWDdYZ%2BYt%2FG78VmIVefywALufEmKdOHMi%2B72jSIZaXIPUCebO9NVXXLPGoCkvJu0TmpRqOaM21ZV9P6zsm3FeqtxpVn5rccmf18GI47U0TMekr%2B5ImP4mtfiLetkzM1Gqe%2Fy0JnaE0PxkIYOYeMAuPJxkyiC7hNV2SomGKkT0QUPsuitGz4JhuTdNg8h6eZnC%2BP5nsImld9DTVcQmQSt3UWbV8i6hzN%2BHAJHLUIfCTukp%2FyzqIOqROKmNSSi%2FXfn8DGT4q18lM5QDdFM%2F8KohO1AC4j0SOj1xm04VtmK5AMOyp77wGOqUBuflrt%2F9rqcRW%2BFrTxW5xsRTR6bf9gRlAmi2lPGnN3AzU6jhzsyhTGbs%2FVXBuhT4ifCAs7Q99GRaqZfoXILsAvw8kqfPU%2F0O2G0GGSifUAdcbTiW536SOm0nKAzVKrd%2BEro7ixQ92XWf%2FRn%2BZ%2F4%2BNcNBfyFzqECYoKpNcovv5467FCzO3Gh5UM0KbyToCPgM%2Bkuu4W%2FRjEnY%2FQKbdJsbrLMvG68MP&X-Amz-Signature=c5eb74eae801a1ff1f6b97d11e0ac43947a360ed6ee9bd6db4fe2683a438cd0e&X-Amz-SignedHeaders=host&x-id=GetObject)
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