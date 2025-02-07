

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3BMSE2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIC48FEl4QIoMuhTjjXmL2ebUpiDBGaeqwlchOOqRdl4jAiARkQ6wRIFSpUl%2F480gsMCB5xpM07xZHeuvfjIF1kcWJir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM4AjZOtz8hoqBFmlRKtwDxEG81UFOW60t7cV33ayY9O1Hj1ScYLvnQCC3cXUrqEjP7mFMWCtO0OqMf7r1gITvHm9tevNL2RGStz46O001m%2FfSmXwxYNYkGD6iFsPTqP%2F90bSF5Ef%2BGAj24zANiZ44lQjfU5xkh7bWjKRvXw%2Fl0H4WWPmZ4kezcU6ZUXyrBOkA1OKb7J3ynFOKjpWHRmh3OM%2Bn2Wx3EdvSLEWwGBIgEB%2FMcbYm5Xn8XxDRxu7OD9RxkDYwvdEZ8GEcq4LazpBSWA%2FLZLpiGZh67m%2Brvsf%2BWk0OxG95LimV3dYrD%2FJ1yZ87%2Ftc2Szmb8lx9VyFiszEYu2%2Bnqry9jmrS3KYd1Cnx83iBgFmS%2F2gAwsJUhn1Kv2aXif4sgBqPgk3q%2B19IBWfjYxEZiqaNjHRpGgaZvS5tRksIrC8n7UHPTk5GfWfoDBk8X03e8BOf8pJZbXv6rb6QSeYpAqa1oDQQewylWQnOIRGL36YzVKLkCELiXuAbFVq7%2Fz9pf93MjLBmrAlEImtZQbEO4kB0%2BXhmWOHygmxq5uBBIeQ%2BMk4SviFFAMsYhAEqvX%2FeF4DNTphTtjS5SI%2FMS%2FiS9VaEegRSoQBRiRs1tsvj8KzwprNj1LT3VAJpEVMFlkSls1ZhYnT0h1QwupmZvQY6pgHqad8Sp3W8gZlUUXC%2Bno2q%2BgmlsyF2lGe7oWHLbQE3Il9jjD2JqGfZTfGKEa%2BTWVgKDyecztJ7WfM36iOTZMBOse%2BzZJkhZhp4PnUit3YvBHPiZT7ykHlhpFTO5uuZ40guwNsEFelT8fw1hQS59mVNPyv%2BGeTvEaaqKgNLQYNqkJF6yzetjQ3PpB2N8V1rlRxReXiv%2BHxH2ldQiiadnt8X0mNF8m73&X-Amz-Signature=1787ac814e55747b145651671e08bb04846820ef084f216fef88487cab6d6cfe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3BMSE2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIC48FEl4QIoMuhTjjXmL2ebUpiDBGaeqwlchOOqRdl4jAiARkQ6wRIFSpUl%2F480gsMCB5xpM07xZHeuvfjIF1kcWJir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM4AjZOtz8hoqBFmlRKtwDxEG81UFOW60t7cV33ayY9O1Hj1ScYLvnQCC3cXUrqEjP7mFMWCtO0OqMf7r1gITvHm9tevNL2RGStz46O001m%2FfSmXwxYNYkGD6iFsPTqP%2F90bSF5Ef%2BGAj24zANiZ44lQjfU5xkh7bWjKRvXw%2Fl0H4WWPmZ4kezcU6ZUXyrBOkA1OKb7J3ynFOKjpWHRmh3OM%2Bn2Wx3EdvSLEWwGBIgEB%2FMcbYm5Xn8XxDRxu7OD9RxkDYwvdEZ8GEcq4LazpBSWA%2FLZLpiGZh67m%2Brvsf%2BWk0OxG95LimV3dYrD%2FJ1yZ87%2Ftc2Szmb8lx9VyFiszEYu2%2Bnqry9jmrS3KYd1Cnx83iBgFmS%2F2gAwsJUhn1Kv2aXif4sgBqPgk3q%2B19IBWfjYxEZiqaNjHRpGgaZvS5tRksIrC8n7UHPTk5GfWfoDBk8X03e8BOf8pJZbXv6rb6QSeYpAqa1oDQQewylWQnOIRGL36YzVKLkCELiXuAbFVq7%2Fz9pf93MjLBmrAlEImtZQbEO4kB0%2BXhmWOHygmxq5uBBIeQ%2BMk4SviFFAMsYhAEqvX%2FeF4DNTphTtjS5SI%2FMS%2FiS9VaEegRSoQBRiRs1tsvj8KzwprNj1LT3VAJpEVMFlkSls1ZhYnT0h1QwupmZvQY6pgHqad8Sp3W8gZlUUXC%2Bno2q%2BgmlsyF2lGe7oWHLbQE3Il9jjD2JqGfZTfGKEa%2BTWVgKDyecztJ7WfM36iOTZMBOse%2BzZJkhZhp4PnUit3YvBHPiZT7ykHlhpFTO5uuZ40guwNsEFelT8fw1hQS59mVNPyv%2BGeTvEaaqKgNLQYNqkJF6yzetjQ3PpB2N8V1rlRxReXiv%2BHxH2ldQiiadnt8X0mNF8m73&X-Amz-Signature=a17dc08f2446ab7d177662520c5cec12a0257a56baa5c49d4982fd7ae9fbaa82&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3BMSE2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIC48FEl4QIoMuhTjjXmL2ebUpiDBGaeqwlchOOqRdl4jAiARkQ6wRIFSpUl%2F480gsMCB5xpM07xZHeuvfjIF1kcWJir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM4AjZOtz8hoqBFmlRKtwDxEG81UFOW60t7cV33ayY9O1Hj1ScYLvnQCC3cXUrqEjP7mFMWCtO0OqMf7r1gITvHm9tevNL2RGStz46O001m%2FfSmXwxYNYkGD6iFsPTqP%2F90bSF5Ef%2BGAj24zANiZ44lQjfU5xkh7bWjKRvXw%2Fl0H4WWPmZ4kezcU6ZUXyrBOkA1OKb7J3ynFOKjpWHRmh3OM%2Bn2Wx3EdvSLEWwGBIgEB%2FMcbYm5Xn8XxDRxu7OD9RxkDYwvdEZ8GEcq4LazpBSWA%2FLZLpiGZh67m%2Brvsf%2BWk0OxG95LimV3dYrD%2FJ1yZ87%2Ftc2Szmb8lx9VyFiszEYu2%2Bnqry9jmrS3KYd1Cnx83iBgFmS%2F2gAwsJUhn1Kv2aXif4sgBqPgk3q%2B19IBWfjYxEZiqaNjHRpGgaZvS5tRksIrC8n7UHPTk5GfWfoDBk8X03e8BOf8pJZbXv6rb6QSeYpAqa1oDQQewylWQnOIRGL36YzVKLkCELiXuAbFVq7%2Fz9pf93MjLBmrAlEImtZQbEO4kB0%2BXhmWOHygmxq5uBBIeQ%2BMk4SviFFAMsYhAEqvX%2FeF4DNTphTtjS5SI%2FMS%2FiS9VaEegRSoQBRiRs1tsvj8KzwprNj1LT3VAJpEVMFlkSls1ZhYnT0h1QwupmZvQY6pgHqad8Sp3W8gZlUUXC%2Bno2q%2BgmlsyF2lGe7oWHLbQE3Il9jjD2JqGfZTfGKEa%2BTWVgKDyecztJ7WfM36iOTZMBOse%2BzZJkhZhp4PnUit3YvBHPiZT7ykHlhpFTO5uuZ40guwNsEFelT8fw1hQS59mVNPyv%2BGeTvEaaqKgNLQYNqkJF6yzetjQ3PpB2N8V1rlRxReXiv%2BHxH2ldQiiadnt8X0mNF8m73&X-Amz-Signature=3a6564faebdc2a981ba0a09baf6854cd3a234c7c892e326c66ac4a0b9f9d633a&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3BMSE2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIC48FEl4QIoMuhTjjXmL2ebUpiDBGaeqwlchOOqRdl4jAiARkQ6wRIFSpUl%2F480gsMCB5xpM07xZHeuvfjIF1kcWJir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM4AjZOtz8hoqBFmlRKtwDxEG81UFOW60t7cV33ayY9O1Hj1ScYLvnQCC3cXUrqEjP7mFMWCtO0OqMf7r1gITvHm9tevNL2RGStz46O001m%2FfSmXwxYNYkGD6iFsPTqP%2F90bSF5Ef%2BGAj24zANiZ44lQjfU5xkh7bWjKRvXw%2Fl0H4WWPmZ4kezcU6ZUXyrBOkA1OKb7J3ynFOKjpWHRmh3OM%2Bn2Wx3EdvSLEWwGBIgEB%2FMcbYm5Xn8XxDRxu7OD9RxkDYwvdEZ8GEcq4LazpBSWA%2FLZLpiGZh67m%2Brvsf%2BWk0OxG95LimV3dYrD%2FJ1yZ87%2Ftc2Szmb8lx9VyFiszEYu2%2Bnqry9jmrS3KYd1Cnx83iBgFmS%2F2gAwsJUhn1Kv2aXif4sgBqPgk3q%2B19IBWfjYxEZiqaNjHRpGgaZvS5tRksIrC8n7UHPTk5GfWfoDBk8X03e8BOf8pJZbXv6rb6QSeYpAqa1oDQQewylWQnOIRGL36YzVKLkCELiXuAbFVq7%2Fz9pf93MjLBmrAlEImtZQbEO4kB0%2BXhmWOHygmxq5uBBIeQ%2BMk4SviFFAMsYhAEqvX%2FeF4DNTphTtjS5SI%2FMS%2FiS9VaEegRSoQBRiRs1tsvj8KzwprNj1LT3VAJpEVMFlkSls1ZhYnT0h1QwupmZvQY6pgHqad8Sp3W8gZlUUXC%2Bno2q%2BgmlsyF2lGe7oWHLbQE3Il9jjD2JqGfZTfGKEa%2BTWVgKDyecztJ7WfM36iOTZMBOse%2BzZJkhZhp4PnUit3YvBHPiZT7ykHlhpFTO5uuZ40guwNsEFelT8fw1hQS59mVNPyv%2BGeTvEaaqKgNLQYNqkJF6yzetjQ3PpB2N8V1rlRxReXiv%2BHxH2ldQiiadnt8X0mNF8m73&X-Amz-Signature=8a5bf62032add68f0a7b5d8c41e1c592ce48ac7ce5b11dd891fb31bc98829d26&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3BMSE2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIC48FEl4QIoMuhTjjXmL2ebUpiDBGaeqwlchOOqRdl4jAiARkQ6wRIFSpUl%2F480gsMCB5xpM07xZHeuvfjIF1kcWJir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM4AjZOtz8hoqBFmlRKtwDxEG81UFOW60t7cV33ayY9O1Hj1ScYLvnQCC3cXUrqEjP7mFMWCtO0OqMf7r1gITvHm9tevNL2RGStz46O001m%2FfSmXwxYNYkGD6iFsPTqP%2F90bSF5Ef%2BGAj24zANiZ44lQjfU5xkh7bWjKRvXw%2Fl0H4WWPmZ4kezcU6ZUXyrBOkA1OKb7J3ynFOKjpWHRmh3OM%2Bn2Wx3EdvSLEWwGBIgEB%2FMcbYm5Xn8XxDRxu7OD9RxkDYwvdEZ8GEcq4LazpBSWA%2FLZLpiGZh67m%2Brvsf%2BWk0OxG95LimV3dYrD%2FJ1yZ87%2Ftc2Szmb8lx9VyFiszEYu2%2Bnqry9jmrS3KYd1Cnx83iBgFmS%2F2gAwsJUhn1Kv2aXif4sgBqPgk3q%2B19IBWfjYxEZiqaNjHRpGgaZvS5tRksIrC8n7UHPTk5GfWfoDBk8X03e8BOf8pJZbXv6rb6QSeYpAqa1oDQQewylWQnOIRGL36YzVKLkCELiXuAbFVq7%2Fz9pf93MjLBmrAlEImtZQbEO4kB0%2BXhmWOHygmxq5uBBIeQ%2BMk4SviFFAMsYhAEqvX%2FeF4DNTphTtjS5SI%2FMS%2FiS9VaEegRSoQBRiRs1tsvj8KzwprNj1LT3VAJpEVMFlkSls1ZhYnT0h1QwupmZvQY6pgHqad8Sp3W8gZlUUXC%2Bno2q%2BgmlsyF2lGe7oWHLbQE3Il9jjD2JqGfZTfGKEa%2BTWVgKDyecztJ7WfM36iOTZMBOse%2BzZJkhZhp4PnUit3YvBHPiZT7ykHlhpFTO5uuZ40guwNsEFelT8fw1hQS59mVNPyv%2BGeTvEaaqKgNLQYNqkJF6yzetjQ3PpB2N8V1rlRxReXiv%2BHxH2ldQiiadnt8X0mNF8m73&X-Amz-Signature=23dd48bd325e5d042b34f97650e4e0999bbfeb7c92c046aede60bdc4addfb709&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3BMSE2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIC48FEl4QIoMuhTjjXmL2ebUpiDBGaeqwlchOOqRdl4jAiARkQ6wRIFSpUl%2F480gsMCB5xpM07xZHeuvfjIF1kcWJir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM4AjZOtz8hoqBFmlRKtwDxEG81UFOW60t7cV33ayY9O1Hj1ScYLvnQCC3cXUrqEjP7mFMWCtO0OqMf7r1gITvHm9tevNL2RGStz46O001m%2FfSmXwxYNYkGD6iFsPTqP%2F90bSF5Ef%2BGAj24zANiZ44lQjfU5xkh7bWjKRvXw%2Fl0H4WWPmZ4kezcU6ZUXyrBOkA1OKb7J3ynFOKjpWHRmh3OM%2Bn2Wx3EdvSLEWwGBIgEB%2FMcbYm5Xn8XxDRxu7OD9RxkDYwvdEZ8GEcq4LazpBSWA%2FLZLpiGZh67m%2Brvsf%2BWk0OxG95LimV3dYrD%2FJ1yZ87%2Ftc2Szmb8lx9VyFiszEYu2%2Bnqry9jmrS3KYd1Cnx83iBgFmS%2F2gAwsJUhn1Kv2aXif4sgBqPgk3q%2B19IBWfjYxEZiqaNjHRpGgaZvS5tRksIrC8n7UHPTk5GfWfoDBk8X03e8BOf8pJZbXv6rb6QSeYpAqa1oDQQewylWQnOIRGL36YzVKLkCELiXuAbFVq7%2Fz9pf93MjLBmrAlEImtZQbEO4kB0%2BXhmWOHygmxq5uBBIeQ%2BMk4SviFFAMsYhAEqvX%2FeF4DNTphTtjS5SI%2FMS%2FiS9VaEegRSoQBRiRs1tsvj8KzwprNj1LT3VAJpEVMFlkSls1ZhYnT0h1QwupmZvQY6pgHqad8Sp3W8gZlUUXC%2Bno2q%2BgmlsyF2lGe7oWHLbQE3Il9jjD2JqGfZTfGKEa%2BTWVgKDyecztJ7WfM36iOTZMBOse%2BzZJkhZhp4PnUit3YvBHPiZT7ykHlhpFTO5uuZ40guwNsEFelT8fw1hQS59mVNPyv%2BGeTvEaaqKgNLQYNqkJF6yzetjQ3PpB2N8V1rlRxReXiv%2BHxH2ldQiiadnt8X0mNF8m73&X-Amz-Signature=f4aa059f853cab5d313e039affae54463acec678567dcf0dadcfdddbcad41e34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3BMSE2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIC48FEl4QIoMuhTjjXmL2ebUpiDBGaeqwlchOOqRdl4jAiARkQ6wRIFSpUl%2F480gsMCB5xpM07xZHeuvfjIF1kcWJir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM4AjZOtz8hoqBFmlRKtwDxEG81UFOW60t7cV33ayY9O1Hj1ScYLvnQCC3cXUrqEjP7mFMWCtO0OqMf7r1gITvHm9tevNL2RGStz46O001m%2FfSmXwxYNYkGD6iFsPTqP%2F90bSF5Ef%2BGAj24zANiZ44lQjfU5xkh7bWjKRvXw%2Fl0H4WWPmZ4kezcU6ZUXyrBOkA1OKb7J3ynFOKjpWHRmh3OM%2Bn2Wx3EdvSLEWwGBIgEB%2FMcbYm5Xn8XxDRxu7OD9RxkDYwvdEZ8GEcq4LazpBSWA%2FLZLpiGZh67m%2Brvsf%2BWk0OxG95LimV3dYrD%2FJ1yZ87%2Ftc2Szmb8lx9VyFiszEYu2%2Bnqry9jmrS3KYd1Cnx83iBgFmS%2F2gAwsJUhn1Kv2aXif4sgBqPgk3q%2B19IBWfjYxEZiqaNjHRpGgaZvS5tRksIrC8n7UHPTk5GfWfoDBk8X03e8BOf8pJZbXv6rb6QSeYpAqa1oDQQewylWQnOIRGL36YzVKLkCELiXuAbFVq7%2Fz9pf93MjLBmrAlEImtZQbEO4kB0%2BXhmWOHygmxq5uBBIeQ%2BMk4SviFFAMsYhAEqvX%2FeF4DNTphTtjS5SI%2FMS%2FiS9VaEegRSoQBRiRs1tsvj8KzwprNj1LT3VAJpEVMFlkSls1ZhYnT0h1QwupmZvQY6pgHqad8Sp3W8gZlUUXC%2Bno2q%2BgmlsyF2lGe7oWHLbQE3Il9jjD2JqGfZTfGKEa%2BTWVgKDyecztJ7WfM36iOTZMBOse%2BzZJkhZhp4PnUit3YvBHPiZT7ykHlhpFTO5uuZ40guwNsEFelT8fw1hQS59mVNPyv%2BGeTvEaaqKgNLQYNqkJF6yzetjQ3PpB2N8V1rlRxReXiv%2BHxH2ldQiiadnt8X0mNF8m73&X-Amz-Signature=3a3f0a60aea079d651b81aa203796109a6a90f8efafcb004ef920c30254f9771&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3BMSE2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIC48FEl4QIoMuhTjjXmL2ebUpiDBGaeqwlchOOqRdl4jAiARkQ6wRIFSpUl%2F480gsMCB5xpM07xZHeuvfjIF1kcWJir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM4AjZOtz8hoqBFmlRKtwDxEG81UFOW60t7cV33ayY9O1Hj1ScYLvnQCC3cXUrqEjP7mFMWCtO0OqMf7r1gITvHm9tevNL2RGStz46O001m%2FfSmXwxYNYkGD6iFsPTqP%2F90bSF5Ef%2BGAj24zANiZ44lQjfU5xkh7bWjKRvXw%2Fl0H4WWPmZ4kezcU6ZUXyrBOkA1OKb7J3ynFOKjpWHRmh3OM%2Bn2Wx3EdvSLEWwGBIgEB%2FMcbYm5Xn8XxDRxu7OD9RxkDYwvdEZ8GEcq4LazpBSWA%2FLZLpiGZh67m%2Brvsf%2BWk0OxG95LimV3dYrD%2FJ1yZ87%2Ftc2Szmb8lx9VyFiszEYu2%2Bnqry9jmrS3KYd1Cnx83iBgFmS%2F2gAwsJUhn1Kv2aXif4sgBqPgk3q%2B19IBWfjYxEZiqaNjHRpGgaZvS5tRksIrC8n7UHPTk5GfWfoDBk8X03e8BOf8pJZbXv6rb6QSeYpAqa1oDQQewylWQnOIRGL36YzVKLkCELiXuAbFVq7%2Fz9pf93MjLBmrAlEImtZQbEO4kB0%2BXhmWOHygmxq5uBBIeQ%2BMk4SviFFAMsYhAEqvX%2FeF4DNTphTtjS5SI%2FMS%2FiS9VaEegRSoQBRiRs1tsvj8KzwprNj1LT3VAJpEVMFlkSls1ZhYnT0h1QwupmZvQY6pgHqad8Sp3W8gZlUUXC%2Bno2q%2BgmlsyF2lGe7oWHLbQE3Il9jjD2JqGfZTfGKEa%2BTWVgKDyecztJ7WfM36iOTZMBOse%2BzZJkhZhp4PnUit3YvBHPiZT7ykHlhpFTO5uuZ40guwNsEFelT8fw1hQS59mVNPyv%2BGeTvEaaqKgNLQYNqkJF6yzetjQ3PpB2N8V1rlRxReXiv%2BHxH2ldQiiadnt8X0mNF8m73&X-Amz-Signature=007a600e6666c3326fd6819e3fc76529661511e0c7e96c28fc360af96ffc290e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3BMSE2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIC48FEl4QIoMuhTjjXmL2ebUpiDBGaeqwlchOOqRdl4jAiARkQ6wRIFSpUl%2F480gsMCB5xpM07xZHeuvfjIF1kcWJir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM4AjZOtz8hoqBFmlRKtwDxEG81UFOW60t7cV33ayY9O1Hj1ScYLvnQCC3cXUrqEjP7mFMWCtO0OqMf7r1gITvHm9tevNL2RGStz46O001m%2FfSmXwxYNYkGD6iFsPTqP%2F90bSF5Ef%2BGAj24zANiZ44lQjfU5xkh7bWjKRvXw%2Fl0H4WWPmZ4kezcU6ZUXyrBOkA1OKb7J3ynFOKjpWHRmh3OM%2Bn2Wx3EdvSLEWwGBIgEB%2FMcbYm5Xn8XxDRxu7OD9RxkDYwvdEZ8GEcq4LazpBSWA%2FLZLpiGZh67m%2Brvsf%2BWk0OxG95LimV3dYrD%2FJ1yZ87%2Ftc2Szmb8lx9VyFiszEYu2%2Bnqry9jmrS3KYd1Cnx83iBgFmS%2F2gAwsJUhn1Kv2aXif4sgBqPgk3q%2B19IBWfjYxEZiqaNjHRpGgaZvS5tRksIrC8n7UHPTk5GfWfoDBk8X03e8BOf8pJZbXv6rb6QSeYpAqa1oDQQewylWQnOIRGL36YzVKLkCELiXuAbFVq7%2Fz9pf93MjLBmrAlEImtZQbEO4kB0%2BXhmWOHygmxq5uBBIeQ%2BMk4SviFFAMsYhAEqvX%2FeF4DNTphTtjS5SI%2FMS%2FiS9VaEegRSoQBRiRs1tsvj8KzwprNj1LT3VAJpEVMFlkSls1ZhYnT0h1QwupmZvQY6pgHqad8Sp3W8gZlUUXC%2Bno2q%2BgmlsyF2lGe7oWHLbQE3Il9jjD2JqGfZTfGKEa%2BTWVgKDyecztJ7WfM36iOTZMBOse%2BzZJkhZhp4PnUit3YvBHPiZT7ykHlhpFTO5uuZ40guwNsEFelT8fw1hQS59mVNPyv%2BGeTvEaaqKgNLQYNqkJF6yzetjQ3PpB2N8V1rlRxReXiv%2BHxH2ldQiiadnt8X0mNF8m73&X-Amz-Signature=4ff8ba236530eed56b6317521d5929dcf30fb3dc34ae66e4d97357e47cb22bac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3BMSE2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIC48FEl4QIoMuhTjjXmL2ebUpiDBGaeqwlchOOqRdl4jAiARkQ6wRIFSpUl%2F480gsMCB5xpM07xZHeuvfjIF1kcWJir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM4AjZOtz8hoqBFmlRKtwDxEG81UFOW60t7cV33ayY9O1Hj1ScYLvnQCC3cXUrqEjP7mFMWCtO0OqMf7r1gITvHm9tevNL2RGStz46O001m%2FfSmXwxYNYkGD6iFsPTqP%2F90bSF5Ef%2BGAj24zANiZ44lQjfU5xkh7bWjKRvXw%2Fl0H4WWPmZ4kezcU6ZUXyrBOkA1OKb7J3ynFOKjpWHRmh3OM%2Bn2Wx3EdvSLEWwGBIgEB%2FMcbYm5Xn8XxDRxu7OD9RxkDYwvdEZ8GEcq4LazpBSWA%2FLZLpiGZh67m%2Brvsf%2BWk0OxG95LimV3dYrD%2FJ1yZ87%2Ftc2Szmb8lx9VyFiszEYu2%2Bnqry9jmrS3KYd1Cnx83iBgFmS%2F2gAwsJUhn1Kv2aXif4sgBqPgk3q%2B19IBWfjYxEZiqaNjHRpGgaZvS5tRksIrC8n7UHPTk5GfWfoDBk8X03e8BOf8pJZbXv6rb6QSeYpAqa1oDQQewylWQnOIRGL36YzVKLkCELiXuAbFVq7%2Fz9pf93MjLBmrAlEImtZQbEO4kB0%2BXhmWOHygmxq5uBBIeQ%2BMk4SviFFAMsYhAEqvX%2FeF4DNTphTtjS5SI%2FMS%2FiS9VaEegRSoQBRiRs1tsvj8KzwprNj1LT3VAJpEVMFlkSls1ZhYnT0h1QwupmZvQY6pgHqad8Sp3W8gZlUUXC%2Bno2q%2BgmlsyF2lGe7oWHLbQE3Il9jjD2JqGfZTfGKEa%2BTWVgKDyecztJ7WfM36iOTZMBOse%2BzZJkhZhp4PnUit3YvBHPiZT7ykHlhpFTO5uuZ40guwNsEFelT8fw1hQS59mVNPyv%2BGeTvEaaqKgNLQYNqkJF6yzetjQ3PpB2N8V1rlRxReXiv%2BHxH2ldQiiadnt8X0mNF8m73&X-Amz-Signature=7663caa6ead66ebacd4a454f1f95e478ab6e77667a05d5c5d557be946042f127&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3BMSE2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIC48FEl4QIoMuhTjjXmL2ebUpiDBGaeqwlchOOqRdl4jAiARkQ6wRIFSpUl%2F480gsMCB5xpM07xZHeuvfjIF1kcWJir%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIM4AjZOtz8hoqBFmlRKtwDxEG81UFOW60t7cV33ayY9O1Hj1ScYLvnQCC3cXUrqEjP7mFMWCtO0OqMf7r1gITvHm9tevNL2RGStz46O001m%2FfSmXwxYNYkGD6iFsPTqP%2F90bSF5Ef%2BGAj24zANiZ44lQjfU5xkh7bWjKRvXw%2Fl0H4WWPmZ4kezcU6ZUXyrBOkA1OKb7J3ynFOKjpWHRmh3OM%2Bn2Wx3EdvSLEWwGBIgEB%2FMcbYm5Xn8XxDRxu7OD9RxkDYwvdEZ8GEcq4LazpBSWA%2FLZLpiGZh67m%2Brvsf%2BWk0OxG95LimV3dYrD%2FJ1yZ87%2Ftc2Szmb8lx9VyFiszEYu2%2Bnqry9jmrS3KYd1Cnx83iBgFmS%2F2gAwsJUhn1Kv2aXif4sgBqPgk3q%2B19IBWfjYxEZiqaNjHRpGgaZvS5tRksIrC8n7UHPTk5GfWfoDBk8X03e8BOf8pJZbXv6rb6QSeYpAqa1oDQQewylWQnOIRGL36YzVKLkCELiXuAbFVq7%2Fz9pf93MjLBmrAlEImtZQbEO4kB0%2BXhmWOHygmxq5uBBIeQ%2BMk4SviFFAMsYhAEqvX%2FeF4DNTphTtjS5SI%2FMS%2FiS9VaEegRSoQBRiRs1tsvj8KzwprNj1LT3VAJpEVMFlkSls1ZhYnT0h1QwupmZvQY6pgHqad8Sp3W8gZlUUXC%2Bno2q%2BgmlsyF2lGe7oWHLbQE3Il9jjD2JqGfZTfGKEa%2BTWVgKDyecztJ7WfM36iOTZMBOse%2BzZJkhZhp4PnUit3YvBHPiZT7ykHlhpFTO5uuZ40guwNsEFelT8fw1hQS59mVNPyv%2BGeTvEaaqKgNLQYNqkJF6yzetjQ3PpB2N8V1rlRxReXiv%2BHxH2ldQiiadnt8X0mNF8m73&X-Amz-Signature=1c8f0c47d298690dceb20a5869865767e23ed61a4e6a6d17f8e6749f1bd2d554&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3ZGUBRY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIGPJHOSz5YdTBbuZ5uUB7isiW4wNyUltpx%2BPUWnybSxvAiEAlPJuNa%2FDaPmnmULNCfVOY4Hp7GfXr4o8oK1quhTheZAq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDIFDrglXok0cSp5L%2BSrcA2H3KwozLQYUaY4cld2E0hljdVSmHUiG%2B%2FU3Nl7b2uUMqI3buzttzeY%2Fm1kenGnkuz%2BTUqNZSl8GEJifbr8uY00sow4inSIhbyRTRkzfQrON0j%2BdRe5BTs9wPIkiDLGuhzkCFFURfa4wEKSNup3pDY5UFy82Mo5qR05vywFe%2FZKrSlLl6BhVr5Fhc1G6X7XrKFOvQozcEZ%2F6n71hLyMb9rOU19WVB78BZtscaQgcR%2FoegIgHl8X8%2Boq24eaYbwMqi3yKvvdO1PjIpuG6Vr0yrdQOj%2BIQdgkVCkzoPyKQ0GgBTM4R%2BZON1Zpsg%2F%2BG%2BbqNq0M16Ngr92V65P0DeFzbd9ZaqXpbB%2FQ06Gl2bNYsWVJb1e2ZTxG6LFe%2BT6K5ZZQ%2B%2Bg4LTn6pEgUVgPYkKGUFN8RFg7QG5AZjMQx%2F1vK%2F7YJ%2BCcP23er2qmECJcXV1OBInqufjbPnC2QzOD8pR7Th5wuTpSDONtShO8rWHFiqFDhTI3xxksvK7f6Q2Cn1wBiBbCnz81celcaLQyLBGqYpUWWzbx3S%2B2s%2FKXbD9uZSSYCUJiuoeIyd3jNhUufHtGJvAIvBtbQlp5CbYsl%2FHJ%2BWk%2BDwLwUk4i21E1GCqV2jsVulqaOFo6agtRZ96wJxML%2BZmb0GOqUB9BuGGYW%2FNa9YiIpC3WG9%2Fz4kHcr8F5GunuYv9bX7sN0LqPElb7Y0BX9y5tAX2frjegy30uOLybOEaQ4vcYL%2FvhPxYAFdGYm2BXL2DSEMrPZoSno%2F0JDdzDKiFyldKRacRq5rmp9WYR0p7OoXLvQk0jLaIKLOqV6yPz0lUc8txxKr0tJtakvdu9EssD7WU%2BT3Qde89tVtpEOk1DABt4FdxMmQolZm&X-Amz-Signature=3bc9c69ea3030fbdd5cb69b79ace0f0709afe832663828a685d4a05657cb377d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3ZGUBRY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIGPJHOSz5YdTBbuZ5uUB7isiW4wNyUltpx%2BPUWnybSxvAiEAlPJuNa%2FDaPmnmULNCfVOY4Hp7GfXr4o8oK1quhTheZAq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDIFDrglXok0cSp5L%2BSrcA2H3KwozLQYUaY4cld2E0hljdVSmHUiG%2B%2FU3Nl7b2uUMqI3buzttzeY%2Fm1kenGnkuz%2BTUqNZSl8GEJifbr8uY00sow4inSIhbyRTRkzfQrON0j%2BdRe5BTs9wPIkiDLGuhzkCFFURfa4wEKSNup3pDY5UFy82Mo5qR05vywFe%2FZKrSlLl6BhVr5Fhc1G6X7XrKFOvQozcEZ%2F6n71hLyMb9rOU19WVB78BZtscaQgcR%2FoegIgHl8X8%2Boq24eaYbwMqi3yKvvdO1PjIpuG6Vr0yrdQOj%2BIQdgkVCkzoPyKQ0GgBTM4R%2BZON1Zpsg%2F%2BG%2BbqNq0M16Ngr92V65P0DeFzbd9ZaqXpbB%2FQ06Gl2bNYsWVJb1e2ZTxG6LFe%2BT6K5ZZQ%2B%2Bg4LTn6pEgUVgPYkKGUFN8RFg7QG5AZjMQx%2F1vK%2F7YJ%2BCcP23er2qmECJcXV1OBInqufjbPnC2QzOD8pR7Th5wuTpSDONtShO8rWHFiqFDhTI3xxksvK7f6Q2Cn1wBiBbCnz81celcaLQyLBGqYpUWWzbx3S%2B2s%2FKXbD9uZSSYCUJiuoeIyd3jNhUufHtGJvAIvBtbQlp5CbYsl%2FHJ%2BWk%2BDwLwUk4i21E1GCqV2jsVulqaOFo6agtRZ96wJxML%2BZmb0GOqUB9BuGGYW%2FNa9YiIpC3WG9%2Fz4kHcr8F5GunuYv9bX7sN0LqPElb7Y0BX9y5tAX2frjegy30uOLybOEaQ4vcYL%2FvhPxYAFdGYm2BXL2DSEMrPZoSno%2F0JDdzDKiFyldKRacRq5rmp9WYR0p7OoXLvQk0jLaIKLOqV6yPz0lUc8txxKr0tJtakvdu9EssD7WU%2BT3Qde89tVtpEOk1DABt4FdxMmQolZm&X-Amz-Signature=6543b0ed3d55c7919cf8923f77e06748c8b2dd9db8d12f39f3def54a42b198e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3ZGUBRY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIGPJHOSz5YdTBbuZ5uUB7isiW4wNyUltpx%2BPUWnybSxvAiEAlPJuNa%2FDaPmnmULNCfVOY4Hp7GfXr4o8oK1quhTheZAq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDIFDrglXok0cSp5L%2BSrcA2H3KwozLQYUaY4cld2E0hljdVSmHUiG%2B%2FU3Nl7b2uUMqI3buzttzeY%2Fm1kenGnkuz%2BTUqNZSl8GEJifbr8uY00sow4inSIhbyRTRkzfQrON0j%2BdRe5BTs9wPIkiDLGuhzkCFFURfa4wEKSNup3pDY5UFy82Mo5qR05vywFe%2FZKrSlLl6BhVr5Fhc1G6X7XrKFOvQozcEZ%2F6n71hLyMb9rOU19WVB78BZtscaQgcR%2FoegIgHl8X8%2Boq24eaYbwMqi3yKvvdO1PjIpuG6Vr0yrdQOj%2BIQdgkVCkzoPyKQ0GgBTM4R%2BZON1Zpsg%2F%2BG%2BbqNq0M16Ngr92V65P0DeFzbd9ZaqXpbB%2FQ06Gl2bNYsWVJb1e2ZTxG6LFe%2BT6K5ZZQ%2B%2Bg4LTn6pEgUVgPYkKGUFN8RFg7QG5AZjMQx%2F1vK%2F7YJ%2BCcP23er2qmECJcXV1OBInqufjbPnC2QzOD8pR7Th5wuTpSDONtShO8rWHFiqFDhTI3xxksvK7f6Q2Cn1wBiBbCnz81celcaLQyLBGqYpUWWzbx3S%2B2s%2FKXbD9uZSSYCUJiuoeIyd3jNhUufHtGJvAIvBtbQlp5CbYsl%2FHJ%2BWk%2BDwLwUk4i21E1GCqV2jsVulqaOFo6agtRZ96wJxML%2BZmb0GOqUB9BuGGYW%2FNa9YiIpC3WG9%2Fz4kHcr8F5GunuYv9bX7sN0LqPElb7Y0BX9y5tAX2frjegy30uOLybOEaQ4vcYL%2FvhPxYAFdGYm2BXL2DSEMrPZoSno%2F0JDdzDKiFyldKRacRq5rmp9WYR0p7OoXLvQk0jLaIKLOqV6yPz0lUc8txxKr0tJtakvdu9EssD7WU%2BT3Qde89tVtpEOk1DABt4FdxMmQolZm&X-Amz-Signature=ab4fbe9212f168ce38dd0c9e9e037e3dd1b11f465a9a154308cba6c299c75440&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3ZGUBRY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIGPJHOSz5YdTBbuZ5uUB7isiW4wNyUltpx%2BPUWnybSxvAiEAlPJuNa%2FDaPmnmULNCfVOY4Hp7GfXr4o8oK1quhTheZAq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDIFDrglXok0cSp5L%2BSrcA2H3KwozLQYUaY4cld2E0hljdVSmHUiG%2B%2FU3Nl7b2uUMqI3buzttzeY%2Fm1kenGnkuz%2BTUqNZSl8GEJifbr8uY00sow4inSIhbyRTRkzfQrON0j%2BdRe5BTs9wPIkiDLGuhzkCFFURfa4wEKSNup3pDY5UFy82Mo5qR05vywFe%2FZKrSlLl6BhVr5Fhc1G6X7XrKFOvQozcEZ%2F6n71hLyMb9rOU19WVB78BZtscaQgcR%2FoegIgHl8X8%2Boq24eaYbwMqi3yKvvdO1PjIpuG6Vr0yrdQOj%2BIQdgkVCkzoPyKQ0GgBTM4R%2BZON1Zpsg%2F%2BG%2BbqNq0M16Ngr92V65P0DeFzbd9ZaqXpbB%2FQ06Gl2bNYsWVJb1e2ZTxG6LFe%2BT6K5ZZQ%2B%2Bg4LTn6pEgUVgPYkKGUFN8RFg7QG5AZjMQx%2F1vK%2F7YJ%2BCcP23er2qmECJcXV1OBInqufjbPnC2QzOD8pR7Th5wuTpSDONtShO8rWHFiqFDhTI3xxksvK7f6Q2Cn1wBiBbCnz81celcaLQyLBGqYpUWWzbx3S%2B2s%2FKXbD9uZSSYCUJiuoeIyd3jNhUufHtGJvAIvBtbQlp5CbYsl%2FHJ%2BWk%2BDwLwUk4i21E1GCqV2jsVulqaOFo6agtRZ96wJxML%2BZmb0GOqUB9BuGGYW%2FNa9YiIpC3WG9%2Fz4kHcr8F5GunuYv9bX7sN0LqPElb7Y0BX9y5tAX2frjegy30uOLybOEaQ4vcYL%2FvhPxYAFdGYm2BXL2DSEMrPZoSno%2F0JDdzDKiFyldKRacRq5rmp9WYR0p7OoXLvQk0jLaIKLOqV6yPz0lUc8txxKr0tJtakvdu9EssD7WU%2BT3Qde89tVtpEOk1DABt4FdxMmQolZm&X-Amz-Signature=f08013ec32a062820fc6e985f820956f6894c42da842fbb82d68d9c46d5a28b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLN3IKJB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDWEsXfvuX8cVjFt7Hw5%2FLX7P9%2FGjVY970X6BcueQh5kQIhANv%2BvyOYphY%2B5ExlUEhLkkvoY%2FzPGiXvv6hJr6rC8NLdKv8DCHsQABoMNjM3NDIzMTgzODA1IgzCnzbgAq%2BVinfW1c4q3APIhs5SHGc0hd5hco5ESUeQ0bpH3410KKZzVGqtQg9T1MNlavEjNP%2BosjtOKTswO2fw4JmtQPJ9bBFLf8UE%2F2CF4WUnTiQUCTdjvE127XcABbnLq7Kzk%2F0nRQsn6BJ2%2BotTBvV2V53Qn3OIt7nzuLLt3pPOWtBfOpgVXuZxjGWTb2lSSttmtoruIi%2FxpzXNSXQzFogHH7s1O5wtne7zzxE3ffM6%2FqWV96LAav3vvYi2FF3yBdS1%2FxbQKTKIWDWY9G6uTtMq1GpQUuLDziS6kFfy%2FTyu7Jsntj8%2FPixGcD1XcWT0wgS3s%2FwcaTTp2ogZZHF7QrKthsHgcfOmuf7mW4bnVYjJfZY8VH3LGT0PMssstWDXZBTmdLbZ3fUU7ookrGnO5G3hwIJsqa4RIpUi0lHrosVIPnKu%2Bu4v2jOoi2pILgSsedbLIwSE79jQoHAp5jYOabk8vmfeEcQiO%2B0cDhOurC3zbTfAcmIJwBJy%2F2mf26wXXR29TWb9prwddk86ETqEsup94BXDHYEFLChCGjhr1km2k8d3bmVgmvijnnB24W8e5AA7tgO%2FPziG2RKRDeA41MS95yrPir%2BMEiuB4uUmw%2BHNKWzVM0Q3qVxoag6t%2FRilNek6zUJItTRf8DCYmZm9BjqkAe7%2Fz0ZPuXAF401ThoTtRp7U%2FSwv8%2BBN8U92GubPevxdOlxufAAE9giHxsy3f%2B8oIidW1OHnUiunu%2FHZSExizGH2IyWOTMBX%2Bbn%2BSaIvGfu%2Fgnn6eYmZJrmahNW%2BV17StslcSE0OVXP479z9VKEh%2FQyIWl1W7fPjd03qud0k3YGKw1B4lawlgRYaDcF9yfm1BxNTQOtTzoOJbUAhW7cKj8GKqhn9&X-Amz-Signature=c4e964dac1b32fe81295daa61bdb9a9f929aee102af145a951dcdd9d38d6171e&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLN3IKJB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDWEsXfvuX8cVjFt7Hw5%2FLX7P9%2FGjVY970X6BcueQh5kQIhANv%2BvyOYphY%2B5ExlUEhLkkvoY%2FzPGiXvv6hJr6rC8NLdKv8DCHsQABoMNjM3NDIzMTgzODA1IgzCnzbgAq%2BVinfW1c4q3APIhs5SHGc0hd5hco5ESUeQ0bpH3410KKZzVGqtQg9T1MNlavEjNP%2BosjtOKTswO2fw4JmtQPJ9bBFLf8UE%2F2CF4WUnTiQUCTdjvE127XcABbnLq7Kzk%2F0nRQsn6BJ2%2BotTBvV2V53Qn3OIt7nzuLLt3pPOWtBfOpgVXuZxjGWTb2lSSttmtoruIi%2FxpzXNSXQzFogHH7s1O5wtne7zzxE3ffM6%2FqWV96LAav3vvYi2FF3yBdS1%2FxbQKTKIWDWY9G6uTtMq1GpQUuLDziS6kFfy%2FTyu7Jsntj8%2FPixGcD1XcWT0wgS3s%2FwcaTTp2ogZZHF7QrKthsHgcfOmuf7mW4bnVYjJfZY8VH3LGT0PMssstWDXZBTmdLbZ3fUU7ookrGnO5G3hwIJsqa4RIpUi0lHrosVIPnKu%2Bu4v2jOoi2pILgSsedbLIwSE79jQoHAp5jYOabk8vmfeEcQiO%2B0cDhOurC3zbTfAcmIJwBJy%2F2mf26wXXR29TWb9prwddk86ETqEsup94BXDHYEFLChCGjhr1km2k8d3bmVgmvijnnB24W8e5AA7tgO%2FPziG2RKRDeA41MS95yrPir%2BMEiuB4uUmw%2BHNKWzVM0Q3qVxoag6t%2FRilNek6zUJItTRf8DCYmZm9BjqkAe7%2Fz0ZPuXAF401ThoTtRp7U%2FSwv8%2BBN8U92GubPevxdOlxufAAE9giHxsy3f%2B8oIidW1OHnUiunu%2FHZSExizGH2IyWOTMBX%2Bbn%2BSaIvGfu%2Fgnn6eYmZJrmahNW%2BV17StslcSE0OVXP479z9VKEh%2FQyIWl1W7fPjd03qud0k3YGKw1B4lawlgRYaDcF9yfm1BxNTQOtTzoOJbUAhW7cKj8GKqhn9&X-Amz-Signature=bc45aa2e8c5c939bdb1e338d4470114b4e9c047af36cbd6d575f7bf08420734c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLN3IKJB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDWEsXfvuX8cVjFt7Hw5%2FLX7P9%2FGjVY970X6BcueQh5kQIhANv%2BvyOYphY%2B5ExlUEhLkkvoY%2FzPGiXvv6hJr6rC8NLdKv8DCHsQABoMNjM3NDIzMTgzODA1IgzCnzbgAq%2BVinfW1c4q3APIhs5SHGc0hd5hco5ESUeQ0bpH3410KKZzVGqtQg9T1MNlavEjNP%2BosjtOKTswO2fw4JmtQPJ9bBFLf8UE%2F2CF4WUnTiQUCTdjvE127XcABbnLq7Kzk%2F0nRQsn6BJ2%2BotTBvV2V53Qn3OIt7nzuLLt3pPOWtBfOpgVXuZxjGWTb2lSSttmtoruIi%2FxpzXNSXQzFogHH7s1O5wtne7zzxE3ffM6%2FqWV96LAav3vvYi2FF3yBdS1%2FxbQKTKIWDWY9G6uTtMq1GpQUuLDziS6kFfy%2FTyu7Jsntj8%2FPixGcD1XcWT0wgS3s%2FwcaTTp2ogZZHF7QrKthsHgcfOmuf7mW4bnVYjJfZY8VH3LGT0PMssstWDXZBTmdLbZ3fUU7ookrGnO5G3hwIJsqa4RIpUi0lHrosVIPnKu%2Bu4v2jOoi2pILgSsedbLIwSE79jQoHAp5jYOabk8vmfeEcQiO%2B0cDhOurC3zbTfAcmIJwBJy%2F2mf26wXXR29TWb9prwddk86ETqEsup94BXDHYEFLChCGjhr1km2k8d3bmVgmvijnnB24W8e5AA7tgO%2FPziG2RKRDeA41MS95yrPir%2BMEiuB4uUmw%2BHNKWzVM0Q3qVxoag6t%2FRilNek6zUJItTRf8DCYmZm9BjqkAe7%2Fz0ZPuXAF401ThoTtRp7U%2FSwv8%2BBN8U92GubPevxdOlxufAAE9giHxsy3f%2B8oIidW1OHnUiunu%2FHZSExizGH2IyWOTMBX%2Bbn%2BSaIvGfu%2Fgnn6eYmZJrmahNW%2BV17StslcSE0OVXP479z9VKEh%2FQyIWl1W7fPjd03qud0k3YGKw1B4lawlgRYaDcF9yfm1BxNTQOtTzoOJbUAhW7cKj8GKqhn9&X-Amz-Signature=e1de1930f6ac17b68d6c11f6dfc4523f60376f5f4a26f80743456f825e36f930&X-Amz-SignedHeaders=host&x-id=GetObject)
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

