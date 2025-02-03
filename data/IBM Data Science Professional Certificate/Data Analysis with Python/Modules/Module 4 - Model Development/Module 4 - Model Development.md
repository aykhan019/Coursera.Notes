

# Module 4: Model Development
## Introduction to Model Development
This module delves into the process of model development, focusing on predictive modeling using datasets. It covers various regression techniques, model evaluation methods, and the importance of accurate data in making predictions.
### Key Concepts
#### **1. Simple and Multiple Linear Regression**:
- Use linear regression to predict outcomes based on one or more independent variables.
#### **2. Model Evaluation Using Visualization**:
- Visually assess the performance of models.
#### **3. Polynomial Regression and Pipelines**:
- Employ polynomial regression to capture non-linear relationships and implement pipelines for streamlined model building.
#### **4. R-squared and Mean Squared Error (MSE)**:
- Evaluate model performance using metrics such as R-squared and MSE to determine prediction accuracy.
#### **5. Prediction and Decision Making**:
- Utilize models to make informed predictions and decisions based on the data.
### Importance of Data
A model, or estimator, is essentially a mathematical equation that predicts a value based on one or more other values. It relates one or more independent variables (features) to dependent variables (outcomes). The accuracy of the model often improves with the relevance and quantity of data. Including multiple independent variables can lead to more precise predictions.
For instance, consider a scenario where predicting an outcome is based on several features. If the model's independent variables do not include a crucial feature, predictions may be inaccurate. Therefore, gathering more relevant data and exploring different types of models is cru1cial for robust model development.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWJ2H6E4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCS7Uh83vQSL%2BN%2F79wTgXZzWspH32%2B4qE4NACZYLfc1rwIhAJGtQm9egT8Hnm9IPKziPr6Q9QsfjP914emo%2Fo0OtQnUKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLhZzYCb5Ur%2BQOKJ8q3AOZPCOE%2BemQ%2B6mTmSuPSV48Yz835GKm46Ccmf7VaOKdK%2FG3JH%2FvNy1FkYrHv1MNdHKMdwID95G2BrRfVHSFxCZgMGrelhtDXkmnb6LoHE1B8rgApa020S2aNqXL%2FgCAkllDT310EzLX5OkSOwEzoGExo7mSgOybOeYdQMYlzGdx5F43Ag4MbBkVagYNLgAEFgAI8cp%2FarTHKXYtUPtXnv93sSnH0PCuBnQNtvyPGZornersH1e%2FsTW9Koxky%2BYb0I261BHdlz8JL6BiRA%2BBaZN5GxFYqP1CukmFV1JdICLiWdzXE%2BH9F2aMnL0thJMjDcol563fCjbQuTjlb%2FJk2VXvoUTF97kTZd76C%2B0I1GPDMrJkbTSdB1W1bKyv6Da%2FUU8hURh%2BQTt3KV9MD4qTpAvByotIfkBB87t5WSBks9nxa%2FYmzzx6n%2Bxd3fJ91yksg8iPuOkzAszaEGvNC%2FKzWiVpapynn2jBKx91I0XdKZ5XTuSP1dRlI3tvyAtWa%2B9d7AVN2nOUukp2yOFSepoICzSK3Zc0%2BouQ%2FFGPe6TjRUvAfOI39qYvmlLhoP9tPRuDFo0%2B2CUs%2FpAb7RnxXWdMrOAAK%2FCFmdgEObsEV22rbi5MJYgAVemPgmMV36C1bzCvv4C9BjqkAeR14eOe9mblbwledMf%2B6%2FVTrUta34uY4l2HXSMGExPfHcvWGYM%2FTfexs2QE9a6GVk31XT4n3x18pRz5jpKTriwJjv87Ei%2BClfWnu9pUW6do0GKfc9dyUmRc0oGC5KQXXwNttHkKKZPIIt6V%2BwC0N0ZwvTU4ckGKWulh5N7f7t8%2BkwjhSc1ogn2FdMyvSRrUh1UnI4pIZrDKvUlvJ0v02WZdvbUT&X-Amz-Signature=c99e4929a2930aaf8a52e6fcf174e31297dcaaa9044f5db928bb85ca7f4a9b35&X-Amz-SignedHeaders=host&x-id=GetObject)
___

## **1. Simple and Multiple Linear Regression**
### Linear Regression
Linear regression predicts a target value using one or more independent variables.
### 1.1 Simple Linear Regression (SLR)
SLR examines the relationship between two variables:
- Predictor (independent variable $ x $)
- Target (dependent variable $ y $)
The relationship is defined as:
$ y = b_0 + b_1 x $
- $ b_0 $: Intercept
- $ b_1  $: Slope
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWJ2H6E4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCS7Uh83vQSL%2BN%2F79wTgXZzWspH32%2B4qE4NACZYLfc1rwIhAJGtQm9egT8Hnm9IPKziPr6Q9QsfjP914emo%2Fo0OtQnUKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLhZzYCb5Ur%2BQOKJ8q3AOZPCOE%2BemQ%2B6mTmSuPSV48Yz835GKm46Ccmf7VaOKdK%2FG3JH%2FvNy1FkYrHv1MNdHKMdwID95G2BrRfVHSFxCZgMGrelhtDXkmnb6LoHE1B8rgApa020S2aNqXL%2FgCAkllDT310EzLX5OkSOwEzoGExo7mSgOybOeYdQMYlzGdx5F43Ag4MbBkVagYNLgAEFgAI8cp%2FarTHKXYtUPtXnv93sSnH0PCuBnQNtvyPGZornersH1e%2FsTW9Koxky%2BYb0I261BHdlz8JL6BiRA%2BBaZN5GxFYqP1CukmFV1JdICLiWdzXE%2BH9F2aMnL0thJMjDcol563fCjbQuTjlb%2FJk2VXvoUTF97kTZd76C%2B0I1GPDMrJkbTSdB1W1bKyv6Da%2FUU8hURh%2BQTt3KV9MD4qTpAvByotIfkBB87t5WSBks9nxa%2FYmzzx6n%2Bxd3fJ91yksg8iPuOkzAszaEGvNC%2FKzWiVpapynn2jBKx91I0XdKZ5XTuSP1dRlI3tvyAtWa%2B9d7AVN2nOUukp2yOFSepoICzSK3Zc0%2BouQ%2FFGPe6TjRUvAfOI39qYvmlLhoP9tPRuDFo0%2B2CUs%2FpAb7RnxXWdMrOAAK%2FCFmdgEObsEV22rbi5MJYgAVemPgmMV36C1bzCvv4C9BjqkAeR14eOe9mblbwledMf%2B6%2FVTrUta34uY4l2HXSMGExPfHcvWGYM%2FTfexs2QE9a6GVk31XT4n3x18pRz5jpKTriwJjv87Ei%2BClfWnu9pUW6do0GKfc9dyUmRc0oGC5KQXXwNttHkKKZPIIt6V%2BwC0N0ZwvTU4ckGKWulh5N7f7t8%2BkwjhSc1ogn2FdMyvSRrUh1UnI4pIZrDKvUlvJ0v02WZdvbUT&X-Amz-Signature=9ce3382f5e4c8b43250baa07d678e17e854e9f328b36cc3a97fb9ff2b05d70e8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Step
If highway miles per gallon is 20, a linear model might predict the car price as $22,000, assuming a linear relationship.
#### Training the Model
Data points are stored in data frames or NumPy arrays. The predictor values ($ x $) and target values    ($ y $) are stored separately. The model is trained using these data points to determine the parameters $ b_0 $ and .
#### Handling Uncertainty
Factors like car make and age influence car prices. Uncertainty in the model is addressed by adding a small random value (noise) to the line. The noise is usually a small positive or negative value.
#### Python Implementation
```python
from sklearn.linear_model import LinearRegression

# Create a linear regression object
lm = LinearRegression()

# Define predictor (x) and target (y) variables
x = ...
y = ...

# Fit the model
lm.fit(x, y)

# Make predictions
predicted_values = lm.predict(x)

# Model parameters
intercept = lm.intercept_
slope = lm.coef_
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWJ2H6E4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCS7Uh83vQSL%2BN%2F79wTgXZzWspH32%2B4qE4NACZYLfc1rwIhAJGtQm9egT8Hnm9IPKziPr6Q9QsfjP914emo%2Fo0OtQnUKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLhZzYCb5Ur%2BQOKJ8q3AOZPCOE%2BemQ%2B6mTmSuPSV48Yz835GKm46Ccmf7VaOKdK%2FG3JH%2FvNy1FkYrHv1MNdHKMdwID95G2BrRfVHSFxCZgMGrelhtDXkmnb6LoHE1B8rgApa020S2aNqXL%2FgCAkllDT310EzLX5OkSOwEzoGExo7mSgOybOeYdQMYlzGdx5F43Ag4MbBkVagYNLgAEFgAI8cp%2FarTHKXYtUPtXnv93sSnH0PCuBnQNtvyPGZornersH1e%2FsTW9Koxky%2BYb0I261BHdlz8JL6BiRA%2BBaZN5GxFYqP1CukmFV1JdICLiWdzXE%2BH9F2aMnL0thJMjDcol563fCjbQuTjlb%2FJk2VXvoUTF97kTZd76C%2B0I1GPDMrJkbTSdB1W1bKyv6Da%2FUU8hURh%2BQTt3KV9MD4qTpAvByotIfkBB87t5WSBks9nxa%2FYmzzx6n%2Bxd3fJ91yksg8iPuOkzAszaEGvNC%2FKzWiVpapynn2jBKx91I0XdKZ5XTuSP1dRlI3tvyAtWa%2B9d7AVN2nOUukp2yOFSepoICzSK3Zc0%2BouQ%2FFGPe6TjRUvAfOI39qYvmlLhoP9tPRuDFo0%2B2CUs%2FpAb7RnxXWdMrOAAK%2FCFmdgEObsEV22rbi5MJYgAVemPgmMV36C1bzCvv4C9BjqkAeR14eOe9mblbwledMf%2B6%2FVTrUta34uY4l2HXSMGExPfHcvWGYM%2FTfexs2QE9a6GVk31XT4n3x18pRz5jpKTriwJjv87Ei%2BClfWnu9pUW6do0GKfc9dyUmRc0oGC5KQXXwNttHkKKZPIIt6V%2BwC0N0ZwvTU4ckGKWulh5N7f7t8%2BkwjhSc1ogn2FdMyvSRrUh1UnI4pIZrDKvUlvJ0v02WZdvbUT&X-Amz-Signature=2395f9b9e949ae04ce02e51c40042c3c7f3b41acf20f3aa43e0e5d48fdaea06d&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWJ2H6E4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCS7Uh83vQSL%2BN%2F79wTgXZzWspH32%2B4qE4NACZYLfc1rwIhAJGtQm9egT8Hnm9IPKziPr6Q9QsfjP914emo%2Fo0OtQnUKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLhZzYCb5Ur%2BQOKJ8q3AOZPCOE%2BemQ%2B6mTmSuPSV48Yz835GKm46Ccmf7VaOKdK%2FG3JH%2FvNy1FkYrHv1MNdHKMdwID95G2BrRfVHSFxCZgMGrelhtDXkmnb6LoHE1B8rgApa020S2aNqXL%2FgCAkllDT310EzLX5OkSOwEzoGExo7mSgOybOeYdQMYlzGdx5F43Ag4MbBkVagYNLgAEFgAI8cp%2FarTHKXYtUPtXnv93sSnH0PCuBnQNtvyPGZornersH1e%2FsTW9Koxky%2BYb0I261BHdlz8JL6BiRA%2BBaZN5GxFYqP1CukmFV1JdICLiWdzXE%2BH9F2aMnL0thJMjDcol563fCjbQuTjlb%2FJk2VXvoUTF97kTZd76C%2B0I1GPDMrJkbTSdB1W1bKyv6Da%2FUU8hURh%2BQTt3KV9MD4qTpAvByotIfkBB87t5WSBks9nxa%2FYmzzx6n%2Bxd3fJ91yksg8iPuOkzAszaEGvNC%2FKzWiVpapynn2jBKx91I0XdKZ5XTuSP1dRlI3tvyAtWa%2B9d7AVN2nOUukp2yOFSepoICzSK3Zc0%2BouQ%2FFGPe6TjRUvAfOI39qYvmlLhoP9tPRuDFo0%2B2CUs%2FpAb7RnxXWdMrOAAK%2FCFmdgEObsEV22rbi5MJYgAVemPgmMV36C1bzCvv4C9BjqkAeR14eOe9mblbwledMf%2B6%2FVTrUta34uY4l2HXSMGExPfHcvWGYM%2FTfexs2QE9a6GVk31XT4n3x18pRz5jpKTriwJjv87Ei%2BClfWnu9pUW6do0GKfc9dyUmRc0oGC5KQXXwNttHkKKZPIIt6V%2BwC0N0ZwvTU4ckGKWulh5N7f7t8%2BkwjhSc1ogn2FdMyvSRrUh1UnI4pIZrDKvUlvJ0v02WZdvbUT&X-Amz-Signature=bc82fd0e76167ba8b7e4a997e7a633cb047cee8b2584a8a5f871b41e63de7a8f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Visualization and Training
With two predictor variables ($ x_1 $ and ), data points are mapped on a 2D plane, and () values are mapped vertically.
#### Python Implementation
```python
from sklearn.linear_model import LinearRegression

# Create a linear regression object
lm = LinearRegression()

# Define predictor variables (z) and target (y)
z = ...
y = ...

# Fit the model
lm.fit(z, y)

# Make predictions
predicted_values = lm.predict(z)

# Model parameters
intercept = lm.intercept_
coefficients = lm.coef_
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWJ2H6E4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCS7Uh83vQSL%2BN%2F79wTgXZzWspH32%2B4qE4NACZYLfc1rwIhAJGtQm9egT8Hnm9IPKziPr6Q9QsfjP914emo%2Fo0OtQnUKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLhZzYCb5Ur%2BQOKJ8q3AOZPCOE%2BemQ%2B6mTmSuPSV48Yz835GKm46Ccmf7VaOKdK%2FG3JH%2FvNy1FkYrHv1MNdHKMdwID95G2BrRfVHSFxCZgMGrelhtDXkmnb6LoHE1B8rgApa020S2aNqXL%2FgCAkllDT310EzLX5OkSOwEzoGExo7mSgOybOeYdQMYlzGdx5F43Ag4MbBkVagYNLgAEFgAI8cp%2FarTHKXYtUPtXnv93sSnH0PCuBnQNtvyPGZornersH1e%2FsTW9Koxky%2BYb0I261BHdlz8JL6BiRA%2BBaZN5GxFYqP1CukmFV1JdICLiWdzXE%2BH9F2aMnL0thJMjDcol563fCjbQuTjlb%2FJk2VXvoUTF97kTZd76C%2B0I1GPDMrJkbTSdB1W1bKyv6Da%2FUU8hURh%2BQTt3KV9MD4qTpAvByotIfkBB87t5WSBks9nxa%2FYmzzx6n%2Bxd3fJ91yksg8iPuOkzAszaEGvNC%2FKzWiVpapynn2jBKx91I0XdKZ5XTuSP1dRlI3tvyAtWa%2B9d7AVN2nOUukp2yOFSepoICzSK3Zc0%2BouQ%2FFGPe6TjRUvAfOI39qYvmlLhoP9tPRuDFo0%2B2CUs%2FpAb7RnxXWdMrOAAK%2FCFmdgEObsEV22rbi5MJYgAVemPgmMV36C1bzCvv4C9BjqkAeR14eOe9mblbwledMf%2B6%2FVTrUta34uY4l2HXSMGExPfHcvWGYM%2FTfexs2QE9a6GVk31XT4n3x18pRz5jpKTriwJjv87Ei%2BClfWnu9pUW6do0GKfc9dyUmRc0oGC5KQXXwNttHkKKZPIIt6V%2BwC0N0ZwvTU4ckGKWulh5N7f7t8%2BkwjhSc1ogn2FdMyvSRrUh1UnI4pIZrDKvUlvJ0v02WZdvbUT&X-Amz-Signature=ef06a444e47fa41926d26ea852116c95fd5829e859aaeafcc1b8ce6f9ae88591&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWJ2H6E4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCS7Uh83vQSL%2BN%2F79wTgXZzWspH32%2B4qE4NACZYLfc1rwIhAJGtQm9egT8Hnm9IPKziPr6Q9QsfjP914emo%2Fo0OtQnUKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLhZzYCb5Ur%2BQOKJ8q3AOZPCOE%2BemQ%2B6mTmSuPSV48Yz835GKm46Ccmf7VaOKdK%2FG3JH%2FvNy1FkYrHv1MNdHKMdwID95G2BrRfVHSFxCZgMGrelhtDXkmnb6LoHE1B8rgApa020S2aNqXL%2FgCAkllDT310EzLX5OkSOwEzoGExo7mSgOybOeYdQMYlzGdx5F43Ag4MbBkVagYNLgAEFgAI8cp%2FarTHKXYtUPtXnv93sSnH0PCuBnQNtvyPGZornersH1e%2FsTW9Koxky%2BYb0I261BHdlz8JL6BiRA%2BBaZN5GxFYqP1CukmFV1JdICLiWdzXE%2BH9F2aMnL0thJMjDcol563fCjbQuTjlb%2FJk2VXvoUTF97kTZd76C%2B0I1GPDMrJkbTSdB1W1bKyv6Da%2FUU8hURh%2BQTt3KV9MD4qTpAvByotIfkBB87t5WSBks9nxa%2FYmzzx6n%2Bxd3fJ91yksg8iPuOkzAszaEGvNC%2FKzWiVpapynn2jBKx91I0XdKZ5XTuSP1dRlI3tvyAtWa%2B9d7AVN2nOUukp2yOFSepoICzSK3Zc0%2BouQ%2FFGPe6TjRUvAfOI39qYvmlLhoP9tPRuDFo0%2B2CUs%2FpAb7RnxXWdMrOAAK%2FCFmdgEObsEV22rbi5MJYgAVemPgmMV36C1bzCvv4C9BjqkAeR14eOe9mblbwledMf%2B6%2FVTrUta34uY4l2HXSMGExPfHcvWGYM%2FTfexs2QE9a6GVk31XT4n3x18pRz5jpKTriwJjv87Ei%2BClfWnu9pUW6do0GKfc9dyUmRc0oGC5KQXXwNttHkKKZPIIt6V%2BwC0N0ZwvTU4ckGKWulh5N7f7t8%2BkwjhSc1ogn2FdMyvSRrUh1UnI4pIZrDKvUlvJ0v02WZdvbUT&X-Amz-Signature=1106289e1b0a183d0501732421438eba62a5455ae71cc1d2b812a5e64b2cf657&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 2. Model Evaluation Using Visualization
### 1. Regression Plots
Regression plots estimate the relationship between two variables, showing the strength and direction of the correlation.
- **Horizontal Axis**: Independent variable.
- **Vertical Axis**: Dependent variable.
- **Points**: Represent different target points.
- **Fitted Line**: Represents predicted values.
#### Creating a Regression Plot
1. **Import Seaborn**:
```python
import seaborn as sns
```
2. **Use **`**regplot**`** Function**:
	- **Parameters**:
		- `x`: Independent variable column.
		- `y`: Dependent variable column.
		- `data`: Name of the DataFrame.
```python
sns.regplot(x='feature', y='target', data=df)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWJ2H6E4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCS7Uh83vQSL%2BN%2F79wTgXZzWspH32%2B4qE4NACZYLfc1rwIhAJGtQm9egT8Hnm9IPKziPr6Q9QsfjP914emo%2Fo0OtQnUKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLhZzYCb5Ur%2BQOKJ8q3AOZPCOE%2BemQ%2B6mTmSuPSV48Yz835GKm46Ccmf7VaOKdK%2FG3JH%2FvNy1FkYrHv1MNdHKMdwID95G2BrRfVHSFxCZgMGrelhtDXkmnb6LoHE1B8rgApa020S2aNqXL%2FgCAkllDT310EzLX5OkSOwEzoGExo7mSgOybOeYdQMYlzGdx5F43Ag4MbBkVagYNLgAEFgAI8cp%2FarTHKXYtUPtXnv93sSnH0PCuBnQNtvyPGZornersH1e%2FsTW9Koxky%2BYb0I261BHdlz8JL6BiRA%2BBaZN5GxFYqP1CukmFV1JdICLiWdzXE%2BH9F2aMnL0thJMjDcol563fCjbQuTjlb%2FJk2VXvoUTF97kTZd76C%2B0I1GPDMrJkbTSdB1W1bKyv6Da%2FUU8hURh%2BQTt3KV9MD4qTpAvByotIfkBB87t5WSBks9nxa%2FYmzzx6n%2Bxd3fJ91yksg8iPuOkzAszaEGvNC%2FKzWiVpapynn2jBKx91I0XdKZ5XTuSP1dRlI3tvyAtWa%2B9d7AVN2nOUukp2yOFSepoICzSK3Zc0%2BouQ%2FFGPe6TjRUvAfOI39qYvmlLhoP9tPRuDFo0%2B2CUs%2FpAb7RnxXWdMrOAAK%2FCFmdgEObsEV22rbi5MJYgAVemPgmMV36C1bzCvv4C9BjqkAeR14eOe9mblbwledMf%2B6%2FVTrUta34uY4l2HXSMGExPfHcvWGYM%2FTfexs2QE9a6GVk31XT4n3x18pRz5jpKTriwJjv87Ei%2BClfWnu9pUW6do0GKfc9dyUmRc0oGC5KQXXwNttHkKKZPIIt6V%2BwC0N0ZwvTU4ckGKWulh5N7f7t8%2BkwjhSc1ogn2FdMyvSRrUh1UnI4pIZrDKvUlvJ0v02WZdvbUT&X-Amz-Signature=4a8665b17330393416162d9e2356132897eaf80ada67dd15653b0a5dbe934e0a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 2. Residual Plots
Residual plots represent the error between actual and predicted values.
- **Process**:
	- Subtract predicted value from actual target value.
	- Plot the error on the vertical axis, dependent variable on the horizontal axis.
- **Insights**:
	- Zero mean distributed evenly around the x-axis indicates a linear model.
	- Curvature in residuals suggests a nonlinear model.
#### Creating a Residual Plot
3. **Import Seaborn**:
```python
import seaborn as sns
```
4. **Use **`**residplot**`** Function**:
	- **Parameters**:
		- Series of dependent variable (feature).
		- Series of target variable.
```python
sns.residplot(x='feature', y='target', data=df)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWJ2H6E4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCS7Uh83vQSL%2BN%2F79wTgXZzWspH32%2B4qE4NACZYLfc1rwIhAJGtQm9egT8Hnm9IPKziPr6Q9QsfjP914emo%2Fo0OtQnUKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLhZzYCb5Ur%2BQOKJ8q3AOZPCOE%2BemQ%2B6mTmSuPSV48Yz835GKm46Ccmf7VaOKdK%2FG3JH%2FvNy1FkYrHv1MNdHKMdwID95G2BrRfVHSFxCZgMGrelhtDXkmnb6LoHE1B8rgApa020S2aNqXL%2FgCAkllDT310EzLX5OkSOwEzoGExo7mSgOybOeYdQMYlzGdx5F43Ag4MbBkVagYNLgAEFgAI8cp%2FarTHKXYtUPtXnv93sSnH0PCuBnQNtvyPGZornersH1e%2FsTW9Koxky%2BYb0I261BHdlz8JL6BiRA%2BBaZN5GxFYqP1CukmFV1JdICLiWdzXE%2BH9F2aMnL0thJMjDcol563fCjbQuTjlb%2FJk2VXvoUTF97kTZd76C%2B0I1GPDMrJkbTSdB1W1bKyv6Da%2FUU8hURh%2BQTt3KV9MD4qTpAvByotIfkBB87t5WSBks9nxa%2FYmzzx6n%2Bxd3fJ91yksg8iPuOkzAszaEGvNC%2FKzWiVpapynn2jBKx91I0XdKZ5XTuSP1dRlI3tvyAtWa%2B9d7AVN2nOUukp2yOFSepoICzSK3Zc0%2BouQ%2FFGPe6TjRUvAfOI39qYvmlLhoP9tPRuDFo0%2B2CUs%2FpAb7RnxXWdMrOAAK%2FCFmdgEObsEV22rbi5MJYgAVemPgmMV36C1bzCvv4C9BjqkAeR14eOe9mblbwledMf%2B6%2FVTrUta34uY4l2HXSMGExPfHcvWGYM%2FTfexs2QE9a6GVk31XT4n3x18pRz5jpKTriwJjv87Ei%2BClfWnu9pUW6do0GKfc9dyUmRc0oGC5KQXXwNttHkKKZPIIt6V%2BwC0N0ZwvTU4ckGKWulh5N7f7t8%2BkwjhSc1ogn2FdMyvSRrUh1UnI4pIZrDKvUlvJ0v02WZdvbUT&X-Amz-Signature=5b2a80874ab90a4426e0eb727f9266f31410aeaa040956212d96c6915b48c670&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWJ2H6E4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCS7Uh83vQSL%2BN%2F79wTgXZzWspH32%2B4qE4NACZYLfc1rwIhAJGtQm9egT8Hnm9IPKziPr6Q9QsfjP914emo%2Fo0OtQnUKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLhZzYCb5Ur%2BQOKJ8q3AOZPCOE%2BemQ%2B6mTmSuPSV48Yz835GKm46Ccmf7VaOKdK%2FG3JH%2FvNy1FkYrHv1MNdHKMdwID95G2BrRfVHSFxCZgMGrelhtDXkmnb6LoHE1B8rgApa020S2aNqXL%2FgCAkllDT310EzLX5OkSOwEzoGExo7mSgOybOeYdQMYlzGdx5F43Ag4MbBkVagYNLgAEFgAI8cp%2FarTHKXYtUPtXnv93sSnH0PCuBnQNtvyPGZornersH1e%2FsTW9Koxky%2BYb0I261BHdlz8JL6BiRA%2BBaZN5GxFYqP1CukmFV1JdICLiWdzXE%2BH9F2aMnL0thJMjDcol563fCjbQuTjlb%2FJk2VXvoUTF97kTZd76C%2B0I1GPDMrJkbTSdB1W1bKyv6Da%2FUU8hURh%2BQTt3KV9MD4qTpAvByotIfkBB87t5WSBks9nxa%2FYmzzx6n%2Bxd3fJ91yksg8iPuOkzAszaEGvNC%2FKzWiVpapynn2jBKx91I0XdKZ5XTuSP1dRlI3tvyAtWa%2B9d7AVN2nOUukp2yOFSepoICzSK3Zc0%2BouQ%2FFGPe6TjRUvAfOI39qYvmlLhoP9tPRuDFo0%2B2CUs%2FpAb7RnxXWdMrOAAK%2FCFmdgEObsEV22rbi5MJYgAVemPgmMV36C1bzCvv4C9BjqkAeR14eOe9mblbwledMf%2B6%2FVTrUta34uY4l2HXSMGExPfHcvWGYM%2FTfexs2QE9a6GVk31XT4n3x18pRz5jpKTriwJjv87Ei%2BClfWnu9pUW6do0GKfc9dyUmRc0oGC5KQXXwNttHkKKZPIIt6V%2BwC0N0ZwvTU4ckGKWulh5N7f7t8%2BkwjhSc1ogn2FdMyvSRrUh1UnI4pIZrDKvUlvJ0v02WZdvbUT&X-Amz-Signature=0c66afb72c35fe01bc74e21630bd00f9aa12073784eb2711fb5a51dec3a173e2&X-Amz-SignedHeaders=host&x-id=GetObject)
### 3. Distribution Plots
Distribution plots visualize predicted versus actual values.
- **Use**: Helpful for models with multiple independent variables.
#### Process
- Count and plot the predicted points approximately equal to a target value.
- Repeat for various target values.
#### Creating a Distribution Plot
5. **Import Pandas** and **Seaborn**:
```python
import pandas as pd
import seaborn as sns
```
6. **Use Seaborn's Distribution Plot**:
	- **Parameters**:
		- `hist`: Set to `False` for a distribution.
		- `color`: Set to desired color.
		- `label`: Include label for legend.
```python
sns.kdeplot(predicted_values, color='blue', label='Predicted')
sns.kdeplot(actual_values, color='red', label='Actual')
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWJ2H6E4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCS7Uh83vQSL%2BN%2F79wTgXZzWspH32%2B4qE4NACZYLfc1rwIhAJGtQm9egT8Hnm9IPKziPr6Q9QsfjP914emo%2Fo0OtQnUKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLhZzYCb5Ur%2BQOKJ8q3AOZPCOE%2BemQ%2B6mTmSuPSV48Yz835GKm46Ccmf7VaOKdK%2FG3JH%2FvNy1FkYrHv1MNdHKMdwID95G2BrRfVHSFxCZgMGrelhtDXkmnb6LoHE1B8rgApa020S2aNqXL%2FgCAkllDT310EzLX5OkSOwEzoGExo7mSgOybOeYdQMYlzGdx5F43Ag4MbBkVagYNLgAEFgAI8cp%2FarTHKXYtUPtXnv93sSnH0PCuBnQNtvyPGZornersH1e%2FsTW9Koxky%2BYb0I261BHdlz8JL6BiRA%2BBaZN5GxFYqP1CukmFV1JdICLiWdzXE%2BH9F2aMnL0thJMjDcol563fCjbQuTjlb%2FJk2VXvoUTF97kTZd76C%2B0I1GPDMrJkbTSdB1W1bKyv6Da%2FUU8hURh%2BQTt3KV9MD4qTpAvByotIfkBB87t5WSBks9nxa%2FYmzzx6n%2Bxd3fJ91yksg8iPuOkzAszaEGvNC%2FKzWiVpapynn2jBKx91I0XdKZ5XTuSP1dRlI3tvyAtWa%2B9d7AVN2nOUukp2yOFSepoICzSK3Zc0%2BouQ%2FFGPe6TjRUvAfOI39qYvmlLhoP9tPRuDFo0%2B2CUs%2FpAb7RnxXWdMrOAAK%2FCFmdgEObsEV22rbi5MJYgAVemPgmMV36C1bzCvv4C9BjqkAeR14eOe9mblbwledMf%2B6%2FVTrUta34uY4l2HXSMGExPfHcvWGYM%2FTfexs2QE9a6GVk31XT4n3x18pRz5jpKTriwJjv87Ei%2BClfWnu9pUW6do0GKfc9dyUmRc0oGC5KQXXwNttHkKKZPIIt6V%2BwC0N0ZwvTU4ckGKWulh5N7f7t8%2BkwjhSc1ogn2FdMyvSRrUh1UnI4pIZrDKvUlvJ0v02WZdvbUT&X-Amz-Signature=4385ef9c67ea1b81566c2728b81b430122d9e3d2e710db035ff6af339bae9c19&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWJ2H6E4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCS7Uh83vQSL%2BN%2F79wTgXZzWspH32%2B4qE4NACZYLfc1rwIhAJGtQm9egT8Hnm9IPKziPr6Q9QsfjP914emo%2Fo0OtQnUKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLhZzYCb5Ur%2BQOKJ8q3AOZPCOE%2BemQ%2B6mTmSuPSV48Yz835GKm46Ccmf7VaOKdK%2FG3JH%2FvNy1FkYrHv1MNdHKMdwID95G2BrRfVHSFxCZgMGrelhtDXkmnb6LoHE1B8rgApa020S2aNqXL%2FgCAkllDT310EzLX5OkSOwEzoGExo7mSgOybOeYdQMYlzGdx5F43Ag4MbBkVagYNLgAEFgAI8cp%2FarTHKXYtUPtXnv93sSnH0PCuBnQNtvyPGZornersH1e%2FsTW9Koxky%2BYb0I261BHdlz8JL6BiRA%2BBaZN5GxFYqP1CukmFV1JdICLiWdzXE%2BH9F2aMnL0thJMjDcol563fCjbQuTjlb%2FJk2VXvoUTF97kTZd76C%2B0I1GPDMrJkbTSdB1W1bKyv6Da%2FUU8hURh%2BQTt3KV9MD4qTpAvByotIfkBB87t5WSBks9nxa%2FYmzzx6n%2Bxd3fJ91yksg8iPuOkzAszaEGvNC%2FKzWiVpapynn2jBKx91I0XdKZ5XTuSP1dRlI3tvyAtWa%2B9d7AVN2nOUukp2yOFSepoICzSK3Zc0%2BouQ%2FFGPe6TjRUvAfOI39qYvmlLhoP9tPRuDFo0%2B2CUs%2FpAb7RnxXWdMrOAAK%2FCFmdgEObsEV22rbi5MJYgAVemPgmMV36C1bzCvv4C9BjqkAeR14eOe9mblbwledMf%2B6%2FVTrUta34uY4l2HXSMGExPfHcvWGYM%2FTfexs2QE9a6GVk31XT4n3x18pRz5jpKTriwJjv87Ei%2BClfWnu9pUW6do0GKfc9dyUmRc0oGC5KQXXwNttHkKKZPIIt6V%2BwC0N0ZwvTU4ckGKWulh5N7f7t8%2BkwjhSc1ogn2FdMyvSRrUh1UnI4pIZrDKvUlvJ0v02WZdvbUT&X-Amz-Signature=3a5c29551cda5fd7eb240f1e4a37b96bf5b11ff38768a13019227e7c55559785&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Types of Polynomial Models
- **Quadratic (2nd Order)**: Includes squared terms.
- **Cubic (3rd Order)**: Includes cubed terms.
- **Higher-Order**: Used for complex relationships.
#### Example Model
- **3rd Order Polynomial**:
$$ −1.557x^3+204.8x^2+8965x+1.37×105 $$
#### Implementation in Python
- **Using NumPy**:
```python
import numpy as np
coefficients = np.polyfit(x, y, 3)
```
- **For Multidimensional**:
Use `scikit-learn` for more complex models.
#### Polynomial Features with Scikit-learn
7. **Import the Library**:
```python
from sklearn.preprocessing import PolynomialFeatures
```
8. **Create Polynomial Features**:
```python
from sklearn.linear_model import LinearRegression

# Create a PolynomialFeatures object with the desired degree
poly = PolynomialFeatures(degree=3)

# Fit and transform your data
X_poly = poly.fit_transform(X)

# Create LinearRegression model
model = LinearRegression()

# Fit the model with the polynomial features
model.fit(X_poly, y)
```
In this code:
- `degree=3` specifies the degree of the polynomial features.
- `fit_transform(X)` generates the polynomial features for your dataset `X`.
### Normalization
#### Why Normalize?
- **Purpose**: Standardize data for better model performance.
#### How to Normalize
- **Using StandardScaler**:
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
```
### Pipelines
#### What are Pipelines?
- **Purpose**: Efficiently automate data preprocessing and model training.
- **Benefit**: Simplifies complex workflows by chaining multiple steps into a single process.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VA7KVYI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHuE5iGQpaVmO7yBhEpStz7zKKRBhSWbHOeVoyFqq%2FkgIgWEqGoptHbEq6HvmnDKUgDuE5BP24lGmyaKVgp%2F5m3kkqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC41Tppugyvce7Tu%2BircA1pH9P%2BVy4gpdKmepSAPM94aMC%2FkkrKPmreIzyrSS6t418PGftu3GQGsKD9llr5WUly81deRXhLnpiI4CQon1nN5wS8pegJqVlicH4nTIiVQnBW%2FRFNanMzH6bmmf7C0WvzwbtYKvKZPVlZCnCr0dpq%2BizDdY7qB2vc8dIJQeUqsMKWOWowBgKJNSE8o3jPHB1GGLuc26oV2M3%2FK2Exu3ZXoCRr05k08wAvzpIfOZJVu%2BDLxC3%2BP5MHqoAFnUvb8MuZJ6eK87h%2FbIt%2FxVWWBF1K%2FjGdfEW%2BRQ%2F02hW6J0k1BqUMcYyGHvVNpS1PAJOEfKcsu%2FPkhEMtKMAunqOaYbxmU5UoLlNO8ZRN4ZNK9%2FWQ2RW1FRCZdxqJhyRB8ASPnts2FlP8DINTK1rPCPeH%2BTWI3vwgzbhque1aKCWHY9vgbHucMZz7S4cBucSK%2Br41MKxs0GM3B1E5Sg9veNVHI4r8ZDZPaxQK3F7gh8wiUBlvuTQw7jGqLy0kHuo48HyhqW9cUYGlFTiwfxeeUmIAl4pdusjkl3n9fWjLqVvFWKD3%2BQRuKetvjNuJMevCNcynpLltbgseu6LEuethPcKWKPWrDvVCBcYU%2BA67rptu6pSbySBFsNZ%2F9PRd2Ijb3ML%2B%2FgL0GOqUBS2sZk1%2BCZj8hqq%2BRPsxlgVlCUYMXrbCPK96F6AMeci2TQzrILccUV7He9CsKCZF%2FX18sJzC1%2FkZpOt31L0voGyWPsJD%2FMSzHQvec0gEOjwyGr3qbGZ7N0YVUk8VOh5eC7mKLIIHOWHJLl8LRgi4qz5kFf2Ey1XAySsZ0yz62AqQKLXZZEO9j0F%2BInMKgQ6hUM%2BuYR5a71T0n04%2FpDbMcZXL8qpmG&X-Amz-Signature=a335f951ff27ed4b58c9105ee4345ea1c968307b2e268269c8914133c4896485&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Benefits
- **Efficiency**: Simplifies code by chaining steps.
- **Maintainability**: Makes workflow clearer.
#### Creating a Pipeline
9. **Import Pipeline**:
```python
from sklearn.pipeline import Pipeline
```
10. **Define Steps**:
```python
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures(degree=3)),
    ('model', LinearRegression())
])
```
11. **Train and Predict**:
```python
pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_test)
```
#### Key Points
- **Sequential Processing**: Automates the flow from preprocessing to prediction.
- **Versatile**: Easily adjust steps and parameters.
Use polynomial regression and pipelines to enhance model accuracy and streamline your machine learning workflow.

### Note:
#### Simple Linear Regression (SLR)
- **Definition**: Models the relationship between two variables by fitting a linear equation.
- **Equation**: $ y = b_0 + b_1x $
- **Use Case**: One independent variable predicts a dependent variable.
#### Multiple Linear Regression (MLR)
- **Definition**: Extends SLR to include multiple independent variables.
- **Equation**: $ y=b_0+b_1x_1+b_2x_2+…+b_nx_n $
- **Use Case**: Accounts for multiple factors affecting the outcome.
#### Polynomial Regression
- **Definition**: A form of regression where the relationship is modeled as an nth degree polynomial.
- **Equation**: $ y = b_0 + b_1x + b_2x^2 + \ldots + b_nx^n $
- **Use Case**: Captures non-linear relationships by transforming features.
#### Key Differences
- **SLR**: Linear relationship with one predictor.
- **MLR**: Linear relationships with multiple predictors.
- **Polynomial Regression**: Non-linear relationships using polynomial terms.
#### Example Code
```python
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Simple Linear Regression
X_slr = np.array([[20], [30], [40]])
y_slr = np.array([15000, 13000, 12000])

model_slr = LinearRegression()
model_slr.fit(X_slr, y_slr)
predicted_slr = model_slr.predict([[30]])
print("SLR Predicted Price:", predicted_slr[0])

# Multiple Linear Regression
X_mlr = np.array([[20, 5], [30, 4], [40, 6]])
y_mlr = np.array([15000, 13000, 12000])

model_mlr = LinearRegression()
model_mlr.fit(X_mlr, y_mlr)
predicted_mlr = model_mlr.predict([[30, 5]])
print("MLR Predicted Price:", predicted_mlr[0])

# Polynomial Regression
X_poly = np.array([[20], [30], [40]])
y_poly = np.array([15000, 13000, 12000])

poly = PolynomialFeatures(degree=2)
X_poly_transformed = poly.fit_transform(X_poly)

model_poly = LinearRegression()
model_poly.fit(X_poly_transformed, y_poly)
predicted_poly = model_poly.predict(poly.transform([[30]]))
print("Polynomial Predicted Price:", predicted_poly[0])
```
___
## 4. Model Evaluation Metrics
### Mean Squared Error (MSE)
- **Definition**: Measures the average squared difference between actual and predicted values. It indicates how close predictions are to the actual values.
- **Formula**: $  \text{MSE} = \frac{1}{n} \sum (y - \hat{y})^2 $
- **Python**: Use `mean_squared_error` from `sklearn.metrics`.
#### Example
**Scenario**: Predicting house prices based on size.
- **Actual Prices**: [200, 250, 300]
- **Predicted Prices**: [210, 240, 310]
**Calculation**:
$ \text{MSE} = \frac{1}{3} ((200-210)^2 + (250-240)^2 + (300-310)^2) = \frac{1}{3} (100 + 100 + 100) = 100
 $
**Python Code**:
```python
from sklearn.metrics import mean_squared_error

actual = [200, 250, 300]
predicted = [210, 240, 310]
mse = mean_squared_error(actual, predicted)
print("MSE:", mse)  # Output: MSE: 100.0
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VA7KVYI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHuE5iGQpaVmO7yBhEpStz7zKKRBhSWbHOeVoyFqq%2FkgIgWEqGoptHbEq6HvmnDKUgDuE5BP24lGmyaKVgp%2F5m3kkqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC41Tppugyvce7Tu%2BircA1pH9P%2BVy4gpdKmepSAPM94aMC%2FkkrKPmreIzyrSS6t418PGftu3GQGsKD9llr5WUly81deRXhLnpiI4CQon1nN5wS8pegJqVlicH4nTIiVQnBW%2FRFNanMzH6bmmf7C0WvzwbtYKvKZPVlZCnCr0dpq%2BizDdY7qB2vc8dIJQeUqsMKWOWowBgKJNSE8o3jPHB1GGLuc26oV2M3%2FK2Exu3ZXoCRr05k08wAvzpIfOZJVu%2BDLxC3%2BP5MHqoAFnUvb8MuZJ6eK87h%2FbIt%2FxVWWBF1K%2FjGdfEW%2BRQ%2F02hW6J0k1BqUMcYyGHvVNpS1PAJOEfKcsu%2FPkhEMtKMAunqOaYbxmU5UoLlNO8ZRN4ZNK9%2FWQ2RW1FRCZdxqJhyRB8ASPnts2FlP8DINTK1rPCPeH%2BTWI3vwgzbhque1aKCWHY9vgbHucMZz7S4cBucSK%2Br41MKxs0GM3B1E5Sg9veNVHI4r8ZDZPaxQK3F7gh8wiUBlvuTQw7jGqLy0kHuo48HyhqW9cUYGlFTiwfxeeUmIAl4pdusjkl3n9fWjLqVvFWKD3%2BQRuKetvjNuJMevCNcynpLltbgseu6LEuethPcKWKPWrDvVCBcYU%2BA67rptu6pSbySBFsNZ%2F9PRd2Ijb3ML%2B%2FgL0GOqUBS2sZk1%2BCZj8hqq%2BRPsxlgVlCUYMXrbCPK96F6AMeci2TQzrILccUV7He9CsKCZF%2FX18sJzC1%2FkZpOt31L0voGyWPsJD%2FMSzHQvec0gEOjwyGr3qbGZ7N0YVUk8VOh5eC7mKLIIHOWHJLl8LRgi4qz5kFf2Ey1XAySsZ0yz62AqQKLXZZEO9j0F%2BInMKgQ6hUM%2BuYR5a71T0n04%2FpDbMcZXL8qpmG&X-Amz-Signature=f369af7c6f5cbf10b6414960efc17821a1af0b99489fc2de7765d5b31146213e&X-Amz-SignedHeaders=host&x-id=GetObject)
### R-squared (Coefficient of Determination)
- **Definition**: Indicates how well the data fits the regression line. Values range from 0 to 1, with values closer to 1 indicating a better fit.
- **Formula**: $ R^2 = 1 - \frac{\text{MSE of regression}}{\text{MSE of mean}} $
- **Python**: Use `score` method in the linear regression object.
#### Example
**Scenario**: Predicting test scores based on study hours.
**Interpretation**:
- **Good Fit**: R² = 0.9 (90% of variance explained)
- **Poor Fit**: R² = 0.2 (20% of variance explained)
**Python Code**:
```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([2, 3, 5])
model = LinearRegression()
model.fit(X, y)

r_squared = model.score(X, y)
print("R-squared:", r_squared)  # Output: R-squared: 0.9642857142857143
```
#### Example Interpretation
- **Good Fit**: Small MSE for regression, larger for mean → $ R^2 $ near 1.
- **Poor Fit**: Similar MSE for regression and mean → $ R^2 $ near 0.
- **Negative **$ R^2 $: Possible overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VA7KVYI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHuE5iGQpaVmO7yBhEpStz7zKKRBhSWbHOeVoyFqq%2FkgIgWEqGoptHbEq6HvmnDKUgDuE5BP24lGmyaKVgp%2F5m3kkqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC41Tppugyvce7Tu%2BircA1pH9P%2BVy4gpdKmepSAPM94aMC%2FkkrKPmreIzyrSS6t418PGftu3GQGsKD9llr5WUly81deRXhLnpiI4CQon1nN5wS8pegJqVlicH4nTIiVQnBW%2FRFNanMzH6bmmf7C0WvzwbtYKvKZPVlZCnCr0dpq%2BizDdY7qB2vc8dIJQeUqsMKWOWowBgKJNSE8o3jPHB1GGLuc26oV2M3%2FK2Exu3ZXoCRr05k08wAvzpIfOZJVu%2BDLxC3%2BP5MHqoAFnUvb8MuZJ6eK87h%2FbIt%2FxVWWBF1K%2FjGdfEW%2BRQ%2F02hW6J0k1BqUMcYyGHvVNpS1PAJOEfKcsu%2FPkhEMtKMAunqOaYbxmU5UoLlNO8ZRN4ZNK9%2FWQ2RW1FRCZdxqJhyRB8ASPnts2FlP8DINTK1rPCPeH%2BTWI3vwgzbhque1aKCWHY9vgbHucMZz7S4cBucSK%2Br41MKxs0GM3B1E5Sg9veNVHI4r8ZDZPaxQK3F7gh8wiUBlvuTQw7jGqLy0kHuo48HyhqW9cUYGlFTiwfxeeUmIAl4pdusjkl3n9fWjLqVvFWKD3%2BQRuKetvjNuJMevCNcynpLltbgseu6LEuethPcKWKPWrDvVCBcYU%2BA67rptu6pSbySBFsNZ%2F9PRd2Ijb3ML%2B%2FgL0GOqUBS2sZk1%2BCZj8hqq%2BRPsxlgVlCUYMXrbCPK96F6AMeci2TQzrILccUV7He9CsKCZF%2FX18sJzC1%2FkZpOt31L0voGyWPsJD%2FMSzHQvec0gEOjwyGr3qbGZ7N0YVUk8VOh5eC7mKLIIHOWHJLl8LRgi4qz5kFf2Ey1XAySsZ0yz62AqQKLXZZEO9j0F%2BInMKgQ6hUM%2BuYR5a71T0n04%2FpDbMcZXL8qpmG&X-Amz-Signature=d4784f6dcc245f5082f7619b29103629ec826e1fc557bed0a57899f4cd43498f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VA7KVYI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHuE5iGQpaVmO7yBhEpStz7zKKRBhSWbHOeVoyFqq%2FkgIgWEqGoptHbEq6HvmnDKUgDuE5BP24lGmyaKVgp%2F5m3kkqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC41Tppugyvce7Tu%2BircA1pH9P%2BVy4gpdKmepSAPM94aMC%2FkkrKPmreIzyrSS6t418PGftu3GQGsKD9llr5WUly81deRXhLnpiI4CQon1nN5wS8pegJqVlicH4nTIiVQnBW%2FRFNanMzH6bmmf7C0WvzwbtYKvKZPVlZCnCr0dpq%2BizDdY7qB2vc8dIJQeUqsMKWOWowBgKJNSE8o3jPHB1GGLuc26oV2M3%2FK2Exu3ZXoCRr05k08wAvzpIfOZJVu%2BDLxC3%2BP5MHqoAFnUvb8MuZJ6eK87h%2FbIt%2FxVWWBF1K%2FjGdfEW%2BRQ%2F02hW6J0k1BqUMcYyGHvVNpS1PAJOEfKcsu%2FPkhEMtKMAunqOaYbxmU5UoLlNO8ZRN4ZNK9%2FWQ2RW1FRCZdxqJhyRB8ASPnts2FlP8DINTK1rPCPeH%2BTWI3vwgzbhque1aKCWHY9vgbHucMZz7S4cBucSK%2Br41MKxs0GM3B1E5Sg9veNVHI4r8ZDZPaxQK3F7gh8wiUBlvuTQw7jGqLy0kHuo48HyhqW9cUYGlFTiwfxeeUmIAl4pdusjkl3n9fWjLqVvFWKD3%2BQRuKetvjNuJMevCNcynpLltbgseu6LEuethPcKWKPWrDvVCBcYU%2BA67rptu6pSbySBFsNZ%2F9PRd2Ijb3ML%2B%2FgL0GOqUBS2sZk1%2BCZj8hqq%2BRPsxlgVlCUYMXrbCPK96F6AMeci2TQzrILccUV7He9CsKCZF%2FX18sJzC1%2FkZpOt31L0voGyWPsJD%2FMSzHQvec0gEOjwyGr3qbGZ7N0YVUk8VOh5eC7mKLIIHOWHJLl8LRgi4qz5kFf2Ey1XAySsZ0yz62AqQKLXZZEO9j0F%2BInMKgQ6hUM%2BuYR5a71T0n04%2FpDbMcZXL8qpmG&X-Amz-Signature=a3c03884ceeebf2121ae13db81502fd605da614c3f5c19d5b4aa33271158d263&X-Amz-SignedHeaders=host&x-id=GetObject)
### Example: Predicting Car Price
- **Scenario**: Predict price for a car with 30 highway mpg.
- **Result**: Price = $13,771.30 (reasonable value).
#### Coefficient Interpretation
An increase of 1 mpg decreases price by $821.
#### Potential Issues
Unrealistic predictions may indicate:
- Incorrect assumptions
- Lack of data in certain ranges
### Generating Predictions
- Use NumPy's `arange` to create sequences for prediction.
```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([[20], [30], [40]])
y = np.array([15000, 13000, 12000])

# Model training
model = LinearRegression()
model.fit(X, y)

# Generating a sequence for prediction
mpg_values = np.arange(1, 101, 1)  # From 1 to 100 with step 1
predicted_prices = model.predict(mpg_values.reshape(-1, 1))

# Example prediction for 30 mpg
predicted_price = model.predict([[30]])
print("Predicted Price:", predicted_price[0])
```
#### Explanation
- `**np.arange(1, 101, 1)**`: Creates an array from 1 to 100 with a step of 1.
- `**reshape(-1, 1)**`: Reshapes the array for prediction.
### Visualization Techniques
- **Regression Plot**: Shows data trend and potential non-linear behavior.
- **Residual Plot**: Curvature indicates non-linear relationships.
- **Distribution Plot**: Highlights prediction accuracy in certain ranges.
### Evaluating Models
#### Mean Squared Error (MSE)
- **Interpretation**: Average squared difference between actual and predicted values.
**Example MSEs:**
- 495 (good fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM63LQX5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMj3d5khOt0B5pjVx3sNPhcQFamVKFwXU267ehq%2FXkXwIgQedkh9UlSYJJ4upLDjw2hEN8SNv6F7ajZGCzscNorccqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAVpBsmLeF0OxuJx1yrcAzeIiO1QTmgthzuJYmd0B8Rq33XpvYNKWqvUT2cLjfmWdoeCMekmUQ9BawVhl87is5BZY8Fr%2Bpis%2FqIfGjadDLVqex06gICyC%2FiV29PZeUeZIH9ASB5aJ9JVucb6a8TXUEEt4aeTJpqL%2BNOjsgzlVnhf8%2FT8a700cIVVQdrc9VMktifgHgOsMC1276tfk8fELIxE2t%2B6ewLD%2B2Doq9%2FwAJkUI9ySSlwoh4UrQolwJsdU3F2n8S3gCiMdI%2BOF%2FZ9HjBIZZH2mEYvLJ3%2FNKPKPjqAvLH%2BvsY1cTmE8z6AGKxu9jVxLgFS9Rmqsi0W3acRXeydzrYRbYwkM5Tq1mYGGgmjLPNpK0EpIc9DMrChqylh4AuKzT%2FkQWQ70KKMOG%2B5DCEPHF%2BWOfOFEnKm6z4ZEqJRBYNIlntyfDwLerHNXZZ%2FbOtBYXmPI7kTAMdH2JadkVtIgRcdxe1ecEE%2BHWAlH%2FhF00ImVXeqHY%2BEEvgHj25hkY%2B8W2skWBErkD7GnqzU05Eg%2Bb7f%2BTLb8QYhPQPrJDuYl2ZEtTCHxBeoarEC8qx65yesn4iPNKRRUtYZuKT4%2B4SnEvE8T0ohVWShlASduUTa%2BGSrWse%2FzGTjSfBNoOTNHZhtyhVfY79sFOS31MPO%2FgL0GOqUBuvg1tgVmCMN6jureV092DFIjG6LRcWF0n8qLixQErFHEcxK2hamoUr%2FX99G0NrBjvTp68k78CBlMC2uP9AkOblN2FkWmHuZ%2FgdKBgNsIKeFclE9ObwEUD%2FbkwhIHbSRTdoUld6UvdpuBrrbAe9l%2BepHeX0yDjB%2BdJw2FamZuaXIlr5Gc9PavHbKp61jZw5SDidLy5duFczQRlzmil641bYj0Epha&X-Amz-Signature=3c4c09251e977756066612cf362e1e5f234e45a66935ea01259864b5c211606a&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM63LQX5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMj3d5khOt0B5pjVx3sNPhcQFamVKFwXU267ehq%2FXkXwIgQedkh9UlSYJJ4upLDjw2hEN8SNv6F7ajZGCzscNorccqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAVpBsmLeF0OxuJx1yrcAzeIiO1QTmgthzuJYmd0B8Rq33XpvYNKWqvUT2cLjfmWdoeCMekmUQ9BawVhl87is5BZY8Fr%2Bpis%2FqIfGjadDLVqex06gICyC%2FiV29PZeUeZIH9ASB5aJ9JVucb6a8TXUEEt4aeTJpqL%2BNOjsgzlVnhf8%2FT8a700cIVVQdrc9VMktifgHgOsMC1276tfk8fELIxE2t%2B6ewLD%2B2Doq9%2FwAJkUI9ySSlwoh4UrQolwJsdU3F2n8S3gCiMdI%2BOF%2FZ9HjBIZZH2mEYvLJ3%2FNKPKPjqAvLH%2BvsY1cTmE8z6AGKxu9jVxLgFS9Rmqsi0W3acRXeydzrYRbYwkM5Tq1mYGGgmjLPNpK0EpIc9DMrChqylh4AuKzT%2FkQWQ70KKMOG%2B5DCEPHF%2BWOfOFEnKm6z4ZEqJRBYNIlntyfDwLerHNXZZ%2FbOtBYXmPI7kTAMdH2JadkVtIgRcdxe1ecEE%2BHWAlH%2FhF00ImVXeqHY%2BEEvgHj25hkY%2B8W2skWBErkD7GnqzU05Eg%2Bb7f%2BTLb8QYhPQPrJDuYl2ZEtTCHxBeoarEC8qx65yesn4iPNKRRUtYZuKT4%2B4SnEvE8T0ohVWShlASduUTa%2BGSrWse%2FzGTjSfBNoOTNHZhtyhVfY79sFOS31MPO%2FgL0GOqUBuvg1tgVmCMN6jureV092DFIjG6LRcWF0n8qLixQErFHEcxK2hamoUr%2FX99G0NrBjvTp68k78CBlMC2uP9AkOblN2FkWmHuZ%2FgdKBgNsIKeFclE9ObwEUD%2FbkwhIHbSRTdoUld6UvdpuBrrbAe9l%2BepHeX0yDjB%2BdJw2FamZuaXIlr5Gc9PavHbKp61jZw5SDidLy5duFczQRlzmil641bYj0Epha&X-Amz-Signature=953ac0c463fd0b270a8f9aadb639db6c8743928764595e824f32ba4d5ed7ca7a&X-Amz-SignedHeaders=host&x-id=GetObject)

**Code Example:**
```python
from sklearn.metrics import mean_squared_error

# Actual and predicted values
actual = [15000, 13000, 12000]
predicted = model.predict(X)

# Calculate MSE
mse = mean_squared_error(actual, predicted)
print("MSE:", mse)
```

#### R-squared (R²)
- **Definition**: Indicates how well data fits the regression line.
Example R² Values:
- 0.9986 (excellent fit)
- 0.61 (weak linear relation)
```python
# Calculate R-squared
r_squared = model.score(X, y)
print("R-squared:", r_squared) 
```
### Model Comparison
- **MLR vs. SLR**: More variables can lower MSE, but not always a better fit.
- **Polynomial Regression**: Generally has lower MSE compared to linear regression.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VM63LQX5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T024223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMj3d5khOt0B5pjVx3sNPhcQFamVKFwXU267ehq%2FXkXwIgQedkh9UlSYJJ4upLDjw2hEN8SNv6F7ajZGCzscNorccqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAVpBsmLeF0OxuJx1yrcAzeIiO1QTmgthzuJYmd0B8Rq33XpvYNKWqvUT2cLjfmWdoeCMekmUQ9BawVhl87is5BZY8Fr%2Bpis%2FqIfGjadDLVqex06gICyC%2FiV29PZeUeZIH9ASB5aJ9JVucb6a8TXUEEt4aeTJpqL%2BNOjsgzlVnhf8%2FT8a700cIVVQdrc9VMktifgHgOsMC1276tfk8fELIxE2t%2B6ewLD%2B2Doq9%2FwAJkUI9ySSlwoh4UrQolwJsdU3F2n8S3gCiMdI%2BOF%2FZ9HjBIZZH2mEYvLJ3%2FNKPKPjqAvLH%2BvsY1cTmE8z6AGKxu9jVxLgFS9Rmqsi0W3acRXeydzrYRbYwkM5Tq1mYGGgmjLPNpK0EpIc9DMrChqylh4AuKzT%2FkQWQ70KKMOG%2B5DCEPHF%2BWOfOFEnKm6z4ZEqJRBYNIlntyfDwLerHNXZZ%2FbOtBYXmPI7kTAMdH2JadkVtIgRcdxe1ecEE%2BHWAlH%2FhF00ImVXeqHY%2BEEvgHj25hkY%2B8W2skWBErkD7GnqzU05Eg%2Bb7f%2BTLb8QYhPQPrJDuYl2ZEtTCHxBeoarEC8qx65yesn4iPNKRRUtYZuKT4%2B4SnEvE8T0ohVWShlASduUTa%2BGSrWse%2FzGTjSfBNoOTNHZhtyhVfY79sFOS31MPO%2FgL0GOqUBuvg1tgVmCMN6jureV092DFIjG6LRcWF0n8qLixQErFHEcxK2hamoUr%2FX99G0NrBjvTp68k78CBlMC2uP9AkOblN2FkWmHuZ%2FgdKBgNsIKeFclE9ObwEUD%2FbkwhIHbSRTdoUld6UvdpuBrrbAe9l%2BepHeX0yDjB%2BdJw2FamZuaXIlr5Gc9PavHbKp61jZw5SDidLy5duFczQRlzmil641bYj0Epha&X-Amz-Signature=c4a45ede64289677e79df5cad8e7ed6426d165d2169354395ac662e0904d8e5d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Conclusion
- Evaluate models using both visualization and numerical metrics.
- Consider context and domain for interpreting R² and MSE values.
___

## Notes
### Regression Plot
When it comes to simple linear regression, an excellent way to visualize the fit of our model is by using **regression plots**.
This plot will show a combination of scattered data points (a **scatterplot**), as well as the fitted **linear regression** line going through the data. This will give us a reasonable estimate of the relationship between the two variables, the strength of the correlation, as well as the direction (positive or negative correlation).
### Residual Plot
A good way to visualize the variance of the data is to use a residual plot.
What is a **residual**?
The difference between the observed value (y) and the predicted value (ŷ) is called the residual (e). When we look at a regression plot, the residual is the distance from the data point to the fitted regression line.
So what is a **residual plot**?
A residual plot is a graph that shows the residuals on the vertical y-axis and the independent variable on the horizontal x-axis.
What do we pay attention to when looking at a residual plot?
We look at the spread of the residuals:
- If the points in a residual plot are **randomly spread out around the x-axis**, then a **linear model is appropriate** for the data.
Why is that? Randomly spread out residuals mean that the variance is constant, and thus the linear model is a good fit for this data.
### **Simple Linear Regression**
One example of a Data Model that we will be using is **Simple Linear Regression**.
Simple Linear Regression is a method to help us understand the relationship between two variables:
- The predictor/independent variable (X)
- The response/dependent variable (that we want to predict) (Y)
The result of Linear Regression is a **linear function** that predicts the response (dependent) variable as a function of the predictor (independent) variable.
### **Multiple Linear Regression**
What if we want to predict car price using more than one variable?
If we want to use more variables in our model to predict car price, we can use **Multiple Linear Regression**. Multiple Linear Regression is very similar to Simple Linear Regression, but this method is used to explain the relationship between one continuous response (dependent) variable and **two or more** predictor (independent) variables. Most of the real-world regression models involve multiple predictors. We will illustrate the structure by using four predictor variables, but these results can generalize to any number.
### **Polynomial Regression**
**Polynomial regression** is a particular case of the general linear regression model or multiple linear regression models.
We get non-linear relationships by squaring or setting higher-order terms of the predictor variables.
### Measures for In-Sample Evaluation
When evaluating our models, not only do we want to visualize the results, but we also need a quantitative measure to determine how accurate the model is.
Two very important measures that are often used in statistics to assess the accuracy of a model are:
- **R² / R-squared (The Coefficient of Determination)**
- **Mean Squared Error (MSE)**
#### R-squared
R-squared, also known as the coefficient of determination, measures how closely the data aligns with the fitted regression line.
The R-squared value represents the percentage of variation in the response variable (y) that is explained by the linear model.
#### Mean Squared Error (MSE)
The Mean Squared Error (MSE) measures the average of the squares of the errors. In other words, it calculates the difference between the actual values (y) and the estimated values (ŷ).
___
## **Cheat Sheet: Model Development**
### Linear Regression
- **Process**: Create a Linear Regression model object
- **Description**: Create an instance of the `LinearRegression` model.
- **Code Example**:
```python
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
```
### Train Linear Regression Model
- **Process**: Train the Linear Regression model
- **Description**: Fit the model on the input and output data. If there’s only one input attribute, it’s simple linear regression. If there are multiple attributes, it’s multiple linear regression.
- **Code Example**:
```python
X = df[['attribute_1', 'attribute_2', ...]]
Y = df['target_attribute']

lr.fit(X, Y)
```
### Generate Output Predictions
- **Process**: Predict the output for given input attributes
- **Description**: Use the trained model to predict the output values based on the input attributes.
- **Code Example**:
```python
Y_hat = lr.predict(X)
```
### Identify the Coefficient and Intercept
- **Process**: Retrieve the model’s coefficient and intercept
- **Description**: Access the slope coefficient and intercept values of the linear regression model.
- **Code Example**:
```python
coeff = lr.coef_
intercept = lr.intercept_
```
### Residual Plot
- **Process**: Create a Residual Plot
- **Description**: Plot the residuals (the differences between observed and predicted values) to assess the goodness of fit.
- **Code Example**:
```python
import seaborn as sns

sns.residplot(x=df['attribute_1'], y=df['attribute_2'])
```
### Distribution Plot
- **Process**: Create a Distribution Plot
- **Description**: Plot the distribution of a given attribute’s data.
- **Code Example**:
```python
import seaborn as sns

sns.distplot(df['attribute_name'], hist=False)
```
### Polynomial Regression
- **Process**: Perform Polynomial Regression
- **Description**: Fit a polynomial model to the data using NumPy.
- **Code Example**:
```python
import numpy as np

f = np.polyfit(x, y, n)
p = np.poly1d(f)
Y_hat = p(x)
```
### Multi-variate Polynomial Regression
- **Process**: Create Polynomial Features
- **Description**: Generate polynomial combinations of features up to a specified degree.
- **Code Example**:
```python
from sklearn.preprocessing import PolynomialFeatures

Z = df[['attribute_1', 'attribute_2', ...]]
pr = PolynomialFeatures(degree=n)
Z_pr = pr.fit_transform(Z)
```
### Pipeline
- **Process**: Create a Data Pipeline
- **Description**: Simplify the steps of processing data by creating a pipeline with a sequence of steps.
- **Code Example**:
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

Input = [
    ('scale', StandardScaler()),
    ('polynomial', PolynomialFeatures(include_bias=False)),
    ('model', LinearRegression())
]
pipe = Pipeline(Input)
Z = Z.astype(float)
pipe.fit(Z, y)
ypipe = pipe.predict(Z)
```
### R² Value
- **Process**: Calculate R² Value
- **Description**: Measure how well the model’s predictions fit the data. This is the proportion of variance explained by the model.
- **Code Example**:
	- For Linear Regression:
```python
from sklearn.metrics import r2_score

R2_score = lr.score(X, Y)
```
	- For Polynomial Regression:
```python
from sklearn.metrics import r2_score
import numpy as np

f = np.polyfit(x, y, n)
p = np.poly1d(f)
R2_score = r2_score(y, p(x))
```
### Mean Squared Error (MSE) Value
- **Process**: Calculate Mean Squared Error (MSE)
- **Description**: Measure the average of the squares of the errors, which are the differences between actual values and the estimated values.
- **Code Example**:
```python
from sklearn.metrics import mean_squared_error

MSE = mean_squared_error(Y, Y_hat)
```
___

