

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7XWG4T3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICj0b4NZwrkqIo030X%2B7joLtCSR%2F7ofyX5ywXu0Ip1usAiEAnf4mpkzuKjPGfoasVXzoQeKn4aU6g5XO7HAp1HTQd6Iq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBYO4cXijZEmDZavpCrcA9lCa%2BYVwVz%2BuDjbAiyXJKkWPqSYOos85BOE%2FidBhp2BWKYH15b47z5JSeRVedLbWvjqJ0TKhsk5VAMEmcldq9GSTzM2ME9yhYix230RB%2ByVYBrDR%2BEWdewkFpqnc0ywUAwd%2BN74Rnw1QXE1uzahW8HlDJd38w1ebWG2aV0KQ9kIFXEP%2B%2BABC9G7Q154r5Z%2BE7FGny%2Fmsj5a2DEV5eK9M1THUZHItjZlX1koFhenwa4qa7JF7%2FDOPa6xa%2Bbv9ncB%2BkO%2BLtTEWzjpW0RnzDnmBpLwU7bVUAgskXnbEJNPFOjGQXbvQ6ScPJ%2BiA8yXHxhkE%2FKJQT2zEb4zU9nyzNZZLbnCbgubZjSdIyCYicRr0h3%2BqDZpS9aDYVH44vSd80GhjuRrapscfSbi%2FfFoIeky79Vas9pwWskXGIrg8bekmc7dIVb8hS%2BNz6RhFSlxrDRklt%2FKRwX6de%2BqyegK0sEezzMm%2BiiV%2BuOvrGDxv5lMTY1xiN%2F7ggX%2BwQzMRR90%2Fh7%2BcVpISTy4J3zwMT1jB8hCXJy%2Bk6Yk%2FbWTbNlagsFUGcKRAQJakMBGPdxmAbn9HMt9AmtU7JE3GvvnVkQggtpvhUFP6Z0pEruP8zDyNdEn77%2FOWWE6KILp6JdXENq0MOXMir0GOqUBUdzNqZumGZQEgmH88nHtTHHe5%2FWsQ%2B3h67uSQZ%2FG6Op8OsGJ5oD9Nob6EVBtJFDLDXdL5XLffJYX%2Bqq%2FT0FFrBt8dXZdLAPLO%2BavfbKH1RaVjSH6pZD6AG3svataIKjAJjXScvDoQVwylIour8psaPHK1Gk%2Fvegx5IIYfmmjPMEN4WZgrsn%2F%2BuGfHPdgM5wEPIIjAJQrBADCBNmDpsy56zUh1DDO&X-Amz-Signature=b3c09a4948c052014da066eae18b842eef4e9d8b33442438024b8dbabf5f9c23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7XWG4T3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICj0b4NZwrkqIo030X%2B7joLtCSR%2F7ofyX5ywXu0Ip1usAiEAnf4mpkzuKjPGfoasVXzoQeKn4aU6g5XO7HAp1HTQd6Iq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBYO4cXijZEmDZavpCrcA9lCa%2BYVwVz%2BuDjbAiyXJKkWPqSYOos85BOE%2FidBhp2BWKYH15b47z5JSeRVedLbWvjqJ0TKhsk5VAMEmcldq9GSTzM2ME9yhYix230RB%2ByVYBrDR%2BEWdewkFpqnc0ywUAwd%2BN74Rnw1QXE1uzahW8HlDJd38w1ebWG2aV0KQ9kIFXEP%2B%2BABC9G7Q154r5Z%2BE7FGny%2Fmsj5a2DEV5eK9M1THUZHItjZlX1koFhenwa4qa7JF7%2FDOPa6xa%2Bbv9ncB%2BkO%2BLtTEWzjpW0RnzDnmBpLwU7bVUAgskXnbEJNPFOjGQXbvQ6ScPJ%2BiA8yXHxhkE%2FKJQT2zEb4zU9nyzNZZLbnCbgubZjSdIyCYicRr0h3%2BqDZpS9aDYVH44vSd80GhjuRrapscfSbi%2FfFoIeky79Vas9pwWskXGIrg8bekmc7dIVb8hS%2BNz6RhFSlxrDRklt%2FKRwX6de%2BqyegK0sEezzMm%2BiiV%2BuOvrGDxv5lMTY1xiN%2F7ggX%2BwQzMRR90%2Fh7%2BcVpISTy4J3zwMT1jB8hCXJy%2Bk6Yk%2FbWTbNlagsFUGcKRAQJakMBGPdxmAbn9HMt9AmtU7JE3GvvnVkQggtpvhUFP6Z0pEruP8zDyNdEn77%2FOWWE6KILp6JdXENq0MOXMir0GOqUBUdzNqZumGZQEgmH88nHtTHHe5%2FWsQ%2B3h67uSQZ%2FG6Op8OsGJ5oD9Nob6EVBtJFDLDXdL5XLffJYX%2Bqq%2FT0FFrBt8dXZdLAPLO%2BavfbKH1RaVjSH6pZD6AG3svataIKjAJjXScvDoQVwylIour8psaPHK1Gk%2Fvegx5IIYfmmjPMEN4WZgrsn%2F%2BuGfHPdgM5wEPIIjAJQrBADCBNmDpsy56zUh1DDO&X-Amz-Signature=b7a2f998106e7f6cd16fc3f19fa2afda65d073238167694d6e6fabc437da529f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7XWG4T3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICj0b4NZwrkqIo030X%2B7joLtCSR%2F7ofyX5ywXu0Ip1usAiEAnf4mpkzuKjPGfoasVXzoQeKn4aU6g5XO7HAp1HTQd6Iq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBYO4cXijZEmDZavpCrcA9lCa%2BYVwVz%2BuDjbAiyXJKkWPqSYOos85BOE%2FidBhp2BWKYH15b47z5JSeRVedLbWvjqJ0TKhsk5VAMEmcldq9GSTzM2ME9yhYix230RB%2ByVYBrDR%2BEWdewkFpqnc0ywUAwd%2BN74Rnw1QXE1uzahW8HlDJd38w1ebWG2aV0KQ9kIFXEP%2B%2BABC9G7Q154r5Z%2BE7FGny%2Fmsj5a2DEV5eK9M1THUZHItjZlX1koFhenwa4qa7JF7%2FDOPa6xa%2Bbv9ncB%2BkO%2BLtTEWzjpW0RnzDnmBpLwU7bVUAgskXnbEJNPFOjGQXbvQ6ScPJ%2BiA8yXHxhkE%2FKJQT2zEb4zU9nyzNZZLbnCbgubZjSdIyCYicRr0h3%2BqDZpS9aDYVH44vSd80GhjuRrapscfSbi%2FfFoIeky79Vas9pwWskXGIrg8bekmc7dIVb8hS%2BNz6RhFSlxrDRklt%2FKRwX6de%2BqyegK0sEezzMm%2BiiV%2BuOvrGDxv5lMTY1xiN%2F7ggX%2BwQzMRR90%2Fh7%2BcVpISTy4J3zwMT1jB8hCXJy%2Bk6Yk%2FbWTbNlagsFUGcKRAQJakMBGPdxmAbn9HMt9AmtU7JE3GvvnVkQggtpvhUFP6Z0pEruP8zDyNdEn77%2FOWWE6KILp6JdXENq0MOXMir0GOqUBUdzNqZumGZQEgmH88nHtTHHe5%2FWsQ%2B3h67uSQZ%2FG6Op8OsGJ5oD9Nob6EVBtJFDLDXdL5XLffJYX%2Bqq%2FT0FFrBt8dXZdLAPLO%2BavfbKH1RaVjSH6pZD6AG3svataIKjAJjXScvDoQVwylIour8psaPHK1Gk%2Fvegx5IIYfmmjPMEN4WZgrsn%2F%2BuGfHPdgM5wEPIIjAJQrBADCBNmDpsy56zUh1DDO&X-Amz-Signature=fbfe464e0b6ab75e8fb750440886c051b667173f5f7a9374f8811f1ae23d9483&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7XWG4T3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICj0b4NZwrkqIo030X%2B7joLtCSR%2F7ofyX5ywXu0Ip1usAiEAnf4mpkzuKjPGfoasVXzoQeKn4aU6g5XO7HAp1HTQd6Iq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBYO4cXijZEmDZavpCrcA9lCa%2BYVwVz%2BuDjbAiyXJKkWPqSYOos85BOE%2FidBhp2BWKYH15b47z5JSeRVedLbWvjqJ0TKhsk5VAMEmcldq9GSTzM2ME9yhYix230RB%2ByVYBrDR%2BEWdewkFpqnc0ywUAwd%2BN74Rnw1QXE1uzahW8HlDJd38w1ebWG2aV0KQ9kIFXEP%2B%2BABC9G7Q154r5Z%2BE7FGny%2Fmsj5a2DEV5eK9M1THUZHItjZlX1koFhenwa4qa7JF7%2FDOPa6xa%2Bbv9ncB%2BkO%2BLtTEWzjpW0RnzDnmBpLwU7bVUAgskXnbEJNPFOjGQXbvQ6ScPJ%2BiA8yXHxhkE%2FKJQT2zEb4zU9nyzNZZLbnCbgubZjSdIyCYicRr0h3%2BqDZpS9aDYVH44vSd80GhjuRrapscfSbi%2FfFoIeky79Vas9pwWskXGIrg8bekmc7dIVb8hS%2BNz6RhFSlxrDRklt%2FKRwX6de%2BqyegK0sEezzMm%2BiiV%2BuOvrGDxv5lMTY1xiN%2F7ggX%2BwQzMRR90%2Fh7%2BcVpISTy4J3zwMT1jB8hCXJy%2Bk6Yk%2FbWTbNlagsFUGcKRAQJakMBGPdxmAbn9HMt9AmtU7JE3GvvnVkQggtpvhUFP6Z0pEruP8zDyNdEn77%2FOWWE6KILp6JdXENq0MOXMir0GOqUBUdzNqZumGZQEgmH88nHtTHHe5%2FWsQ%2B3h67uSQZ%2FG6Op8OsGJ5oD9Nob6EVBtJFDLDXdL5XLffJYX%2Bqq%2FT0FFrBt8dXZdLAPLO%2BavfbKH1RaVjSH6pZD6AG3svataIKjAJjXScvDoQVwylIour8psaPHK1Gk%2Fvegx5IIYfmmjPMEN4WZgrsn%2F%2BuGfHPdgM5wEPIIjAJQrBADCBNmDpsy56zUh1DDO&X-Amz-Signature=5a08099c945153d336dc603391475b1dc112e2b9850a1cef32b5a2ff7ba488ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7XWG4T3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICj0b4NZwrkqIo030X%2B7joLtCSR%2F7ofyX5ywXu0Ip1usAiEAnf4mpkzuKjPGfoasVXzoQeKn4aU6g5XO7HAp1HTQd6Iq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBYO4cXijZEmDZavpCrcA9lCa%2BYVwVz%2BuDjbAiyXJKkWPqSYOos85BOE%2FidBhp2BWKYH15b47z5JSeRVedLbWvjqJ0TKhsk5VAMEmcldq9GSTzM2ME9yhYix230RB%2ByVYBrDR%2BEWdewkFpqnc0ywUAwd%2BN74Rnw1QXE1uzahW8HlDJd38w1ebWG2aV0KQ9kIFXEP%2B%2BABC9G7Q154r5Z%2BE7FGny%2Fmsj5a2DEV5eK9M1THUZHItjZlX1koFhenwa4qa7JF7%2FDOPa6xa%2Bbv9ncB%2BkO%2BLtTEWzjpW0RnzDnmBpLwU7bVUAgskXnbEJNPFOjGQXbvQ6ScPJ%2BiA8yXHxhkE%2FKJQT2zEb4zU9nyzNZZLbnCbgubZjSdIyCYicRr0h3%2BqDZpS9aDYVH44vSd80GhjuRrapscfSbi%2FfFoIeky79Vas9pwWskXGIrg8bekmc7dIVb8hS%2BNz6RhFSlxrDRklt%2FKRwX6de%2BqyegK0sEezzMm%2BiiV%2BuOvrGDxv5lMTY1xiN%2F7ggX%2BwQzMRR90%2Fh7%2BcVpISTy4J3zwMT1jB8hCXJy%2Bk6Yk%2FbWTbNlagsFUGcKRAQJakMBGPdxmAbn9HMt9AmtU7JE3GvvnVkQggtpvhUFP6Z0pEruP8zDyNdEn77%2FOWWE6KILp6JdXENq0MOXMir0GOqUBUdzNqZumGZQEgmH88nHtTHHe5%2FWsQ%2B3h67uSQZ%2FG6Op8OsGJ5oD9Nob6EVBtJFDLDXdL5XLffJYX%2Bqq%2FT0FFrBt8dXZdLAPLO%2BavfbKH1RaVjSH6pZD6AG3svataIKjAJjXScvDoQVwylIour8psaPHK1Gk%2Fvegx5IIYfmmjPMEN4WZgrsn%2F%2BuGfHPdgM5wEPIIjAJQrBADCBNmDpsy56zUh1DDO&X-Amz-Signature=c1c44cfb8ce5bae25a0c9317c0a5334f02fb99e640e64a7111838e044f7d0676&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7XWG4T3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICj0b4NZwrkqIo030X%2B7joLtCSR%2F7ofyX5ywXu0Ip1usAiEAnf4mpkzuKjPGfoasVXzoQeKn4aU6g5XO7HAp1HTQd6Iq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBYO4cXijZEmDZavpCrcA9lCa%2BYVwVz%2BuDjbAiyXJKkWPqSYOos85BOE%2FidBhp2BWKYH15b47z5JSeRVedLbWvjqJ0TKhsk5VAMEmcldq9GSTzM2ME9yhYix230RB%2ByVYBrDR%2BEWdewkFpqnc0ywUAwd%2BN74Rnw1QXE1uzahW8HlDJd38w1ebWG2aV0KQ9kIFXEP%2B%2BABC9G7Q154r5Z%2BE7FGny%2Fmsj5a2DEV5eK9M1THUZHItjZlX1koFhenwa4qa7JF7%2FDOPa6xa%2Bbv9ncB%2BkO%2BLtTEWzjpW0RnzDnmBpLwU7bVUAgskXnbEJNPFOjGQXbvQ6ScPJ%2BiA8yXHxhkE%2FKJQT2zEb4zU9nyzNZZLbnCbgubZjSdIyCYicRr0h3%2BqDZpS9aDYVH44vSd80GhjuRrapscfSbi%2FfFoIeky79Vas9pwWskXGIrg8bekmc7dIVb8hS%2BNz6RhFSlxrDRklt%2FKRwX6de%2BqyegK0sEezzMm%2BiiV%2BuOvrGDxv5lMTY1xiN%2F7ggX%2BwQzMRR90%2Fh7%2BcVpISTy4J3zwMT1jB8hCXJy%2Bk6Yk%2FbWTbNlagsFUGcKRAQJakMBGPdxmAbn9HMt9AmtU7JE3GvvnVkQggtpvhUFP6Z0pEruP8zDyNdEn77%2FOWWE6KILp6JdXENq0MOXMir0GOqUBUdzNqZumGZQEgmH88nHtTHHe5%2FWsQ%2B3h67uSQZ%2FG6Op8OsGJ5oD9Nob6EVBtJFDLDXdL5XLffJYX%2Bqq%2FT0FFrBt8dXZdLAPLO%2BavfbKH1RaVjSH6pZD6AG3svataIKjAJjXScvDoQVwylIour8psaPHK1Gk%2Fvegx5IIYfmmjPMEN4WZgrsn%2F%2BuGfHPdgM5wEPIIjAJQrBADCBNmDpsy56zUh1DDO&X-Amz-Signature=8f0d34dc31a1a3d62f96fc9f5cf91152f5ff455a4065ae78e473857af1e2ef83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7XWG4T3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICj0b4NZwrkqIo030X%2B7joLtCSR%2F7ofyX5ywXu0Ip1usAiEAnf4mpkzuKjPGfoasVXzoQeKn4aU6g5XO7HAp1HTQd6Iq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBYO4cXijZEmDZavpCrcA9lCa%2BYVwVz%2BuDjbAiyXJKkWPqSYOos85BOE%2FidBhp2BWKYH15b47z5JSeRVedLbWvjqJ0TKhsk5VAMEmcldq9GSTzM2ME9yhYix230RB%2ByVYBrDR%2BEWdewkFpqnc0ywUAwd%2BN74Rnw1QXE1uzahW8HlDJd38w1ebWG2aV0KQ9kIFXEP%2B%2BABC9G7Q154r5Z%2BE7FGny%2Fmsj5a2DEV5eK9M1THUZHItjZlX1koFhenwa4qa7JF7%2FDOPa6xa%2Bbv9ncB%2BkO%2BLtTEWzjpW0RnzDnmBpLwU7bVUAgskXnbEJNPFOjGQXbvQ6ScPJ%2BiA8yXHxhkE%2FKJQT2zEb4zU9nyzNZZLbnCbgubZjSdIyCYicRr0h3%2BqDZpS9aDYVH44vSd80GhjuRrapscfSbi%2FfFoIeky79Vas9pwWskXGIrg8bekmc7dIVb8hS%2BNz6RhFSlxrDRklt%2FKRwX6de%2BqyegK0sEezzMm%2BiiV%2BuOvrGDxv5lMTY1xiN%2F7ggX%2BwQzMRR90%2Fh7%2BcVpISTy4J3zwMT1jB8hCXJy%2Bk6Yk%2FbWTbNlagsFUGcKRAQJakMBGPdxmAbn9HMt9AmtU7JE3GvvnVkQggtpvhUFP6Z0pEruP8zDyNdEn77%2FOWWE6KILp6JdXENq0MOXMir0GOqUBUdzNqZumGZQEgmH88nHtTHHe5%2FWsQ%2B3h67uSQZ%2FG6Op8OsGJ5oD9Nob6EVBtJFDLDXdL5XLffJYX%2Bqq%2FT0FFrBt8dXZdLAPLO%2BavfbKH1RaVjSH6pZD6AG3svataIKjAJjXScvDoQVwylIour8psaPHK1Gk%2Fvegx5IIYfmmjPMEN4WZgrsn%2F%2BuGfHPdgM5wEPIIjAJQrBADCBNmDpsy56zUh1DDO&X-Amz-Signature=9f04a22b2f3662ae96e07ae1230ffd6070f58bf6670db9a938f087ffa50d1a3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7XWG4T3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICj0b4NZwrkqIo030X%2B7joLtCSR%2F7ofyX5ywXu0Ip1usAiEAnf4mpkzuKjPGfoasVXzoQeKn4aU6g5XO7HAp1HTQd6Iq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBYO4cXijZEmDZavpCrcA9lCa%2BYVwVz%2BuDjbAiyXJKkWPqSYOos85BOE%2FidBhp2BWKYH15b47z5JSeRVedLbWvjqJ0TKhsk5VAMEmcldq9GSTzM2ME9yhYix230RB%2ByVYBrDR%2BEWdewkFpqnc0ywUAwd%2BN74Rnw1QXE1uzahW8HlDJd38w1ebWG2aV0KQ9kIFXEP%2B%2BABC9G7Q154r5Z%2BE7FGny%2Fmsj5a2DEV5eK9M1THUZHItjZlX1koFhenwa4qa7JF7%2FDOPa6xa%2Bbv9ncB%2BkO%2BLtTEWzjpW0RnzDnmBpLwU7bVUAgskXnbEJNPFOjGQXbvQ6ScPJ%2BiA8yXHxhkE%2FKJQT2zEb4zU9nyzNZZLbnCbgubZjSdIyCYicRr0h3%2BqDZpS9aDYVH44vSd80GhjuRrapscfSbi%2FfFoIeky79Vas9pwWskXGIrg8bekmc7dIVb8hS%2BNz6RhFSlxrDRklt%2FKRwX6de%2BqyegK0sEezzMm%2BiiV%2BuOvrGDxv5lMTY1xiN%2F7ggX%2BwQzMRR90%2Fh7%2BcVpISTy4J3zwMT1jB8hCXJy%2Bk6Yk%2FbWTbNlagsFUGcKRAQJakMBGPdxmAbn9HMt9AmtU7JE3GvvnVkQggtpvhUFP6Z0pEruP8zDyNdEn77%2FOWWE6KILp6JdXENq0MOXMir0GOqUBUdzNqZumGZQEgmH88nHtTHHe5%2FWsQ%2B3h67uSQZ%2FG6Op8OsGJ5oD9Nob6EVBtJFDLDXdL5XLffJYX%2Bqq%2FT0FFrBt8dXZdLAPLO%2BavfbKH1RaVjSH6pZD6AG3svataIKjAJjXScvDoQVwylIour8psaPHK1Gk%2Fvegx5IIYfmmjPMEN4WZgrsn%2F%2BuGfHPdgM5wEPIIjAJQrBADCBNmDpsy56zUh1DDO&X-Amz-Signature=3fad11ba744a289047fe97f396dda2c42ef002307df98da7a8eac3ef45b0b55c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7XWG4T3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICj0b4NZwrkqIo030X%2B7joLtCSR%2F7ofyX5ywXu0Ip1usAiEAnf4mpkzuKjPGfoasVXzoQeKn4aU6g5XO7HAp1HTQd6Iq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBYO4cXijZEmDZavpCrcA9lCa%2BYVwVz%2BuDjbAiyXJKkWPqSYOos85BOE%2FidBhp2BWKYH15b47z5JSeRVedLbWvjqJ0TKhsk5VAMEmcldq9GSTzM2ME9yhYix230RB%2ByVYBrDR%2BEWdewkFpqnc0ywUAwd%2BN74Rnw1QXE1uzahW8HlDJd38w1ebWG2aV0KQ9kIFXEP%2B%2BABC9G7Q154r5Z%2BE7FGny%2Fmsj5a2DEV5eK9M1THUZHItjZlX1koFhenwa4qa7JF7%2FDOPa6xa%2Bbv9ncB%2BkO%2BLtTEWzjpW0RnzDnmBpLwU7bVUAgskXnbEJNPFOjGQXbvQ6ScPJ%2BiA8yXHxhkE%2FKJQT2zEb4zU9nyzNZZLbnCbgubZjSdIyCYicRr0h3%2BqDZpS9aDYVH44vSd80GhjuRrapscfSbi%2FfFoIeky79Vas9pwWskXGIrg8bekmc7dIVb8hS%2BNz6RhFSlxrDRklt%2FKRwX6de%2BqyegK0sEezzMm%2BiiV%2BuOvrGDxv5lMTY1xiN%2F7ggX%2BwQzMRR90%2Fh7%2BcVpISTy4J3zwMT1jB8hCXJy%2Bk6Yk%2FbWTbNlagsFUGcKRAQJakMBGPdxmAbn9HMt9AmtU7JE3GvvnVkQggtpvhUFP6Z0pEruP8zDyNdEn77%2FOWWE6KILp6JdXENq0MOXMir0GOqUBUdzNqZumGZQEgmH88nHtTHHe5%2FWsQ%2B3h67uSQZ%2FG6Op8OsGJ5oD9Nob6EVBtJFDLDXdL5XLffJYX%2Bqq%2FT0FFrBt8dXZdLAPLO%2BavfbKH1RaVjSH6pZD6AG3svataIKjAJjXScvDoQVwylIour8psaPHK1Gk%2Fvegx5IIYfmmjPMEN4WZgrsn%2F%2BuGfHPdgM5wEPIIjAJQrBADCBNmDpsy56zUh1DDO&X-Amz-Signature=14e50f527342af95ce94ea3a061bb0bc649effb67ed1e3c9ce5989e7ecde2a43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7XWG4T3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICj0b4NZwrkqIo030X%2B7joLtCSR%2F7ofyX5ywXu0Ip1usAiEAnf4mpkzuKjPGfoasVXzoQeKn4aU6g5XO7HAp1HTQd6Iq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBYO4cXijZEmDZavpCrcA9lCa%2BYVwVz%2BuDjbAiyXJKkWPqSYOos85BOE%2FidBhp2BWKYH15b47z5JSeRVedLbWvjqJ0TKhsk5VAMEmcldq9GSTzM2ME9yhYix230RB%2ByVYBrDR%2BEWdewkFpqnc0ywUAwd%2BN74Rnw1QXE1uzahW8HlDJd38w1ebWG2aV0KQ9kIFXEP%2B%2BABC9G7Q154r5Z%2BE7FGny%2Fmsj5a2DEV5eK9M1THUZHItjZlX1koFhenwa4qa7JF7%2FDOPa6xa%2Bbv9ncB%2BkO%2BLtTEWzjpW0RnzDnmBpLwU7bVUAgskXnbEJNPFOjGQXbvQ6ScPJ%2BiA8yXHxhkE%2FKJQT2zEb4zU9nyzNZZLbnCbgubZjSdIyCYicRr0h3%2BqDZpS9aDYVH44vSd80GhjuRrapscfSbi%2FfFoIeky79Vas9pwWskXGIrg8bekmc7dIVb8hS%2BNz6RhFSlxrDRklt%2FKRwX6de%2BqyegK0sEezzMm%2BiiV%2BuOvrGDxv5lMTY1xiN%2F7ggX%2BwQzMRR90%2Fh7%2BcVpISTy4J3zwMT1jB8hCXJy%2Bk6Yk%2FbWTbNlagsFUGcKRAQJakMBGPdxmAbn9HMt9AmtU7JE3GvvnVkQggtpvhUFP6Z0pEruP8zDyNdEn77%2FOWWE6KILp6JdXENq0MOXMir0GOqUBUdzNqZumGZQEgmH88nHtTHHe5%2FWsQ%2B3h67uSQZ%2FG6Op8OsGJ5oD9Nob6EVBtJFDLDXdL5XLffJYX%2Bqq%2FT0FFrBt8dXZdLAPLO%2BavfbKH1RaVjSH6pZD6AG3svataIKjAJjXScvDoQVwylIour8psaPHK1Gk%2Fvegx5IIYfmmjPMEN4WZgrsn%2F%2BuGfHPdgM5wEPIIjAJQrBADCBNmDpsy56zUh1DDO&X-Amz-Signature=18087b8b48456e1a4abc5f7fb04fd82008fc2d36fa751216ef1407ae70c39a1b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7XWG4T3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCICj0b4NZwrkqIo030X%2B7joLtCSR%2F7ofyX5ywXu0Ip1usAiEAnf4mpkzuKjPGfoasVXzoQeKn4aU6g5XO7HAp1HTQd6Iq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBYO4cXijZEmDZavpCrcA9lCa%2BYVwVz%2BuDjbAiyXJKkWPqSYOos85BOE%2FidBhp2BWKYH15b47z5JSeRVedLbWvjqJ0TKhsk5VAMEmcldq9GSTzM2ME9yhYix230RB%2ByVYBrDR%2BEWdewkFpqnc0ywUAwd%2BN74Rnw1QXE1uzahW8HlDJd38w1ebWG2aV0KQ9kIFXEP%2B%2BABC9G7Q154r5Z%2BE7FGny%2Fmsj5a2DEV5eK9M1THUZHItjZlX1koFhenwa4qa7JF7%2FDOPa6xa%2Bbv9ncB%2BkO%2BLtTEWzjpW0RnzDnmBpLwU7bVUAgskXnbEJNPFOjGQXbvQ6ScPJ%2BiA8yXHxhkE%2FKJQT2zEb4zU9nyzNZZLbnCbgubZjSdIyCYicRr0h3%2BqDZpS9aDYVH44vSd80GhjuRrapscfSbi%2FfFoIeky79Vas9pwWskXGIrg8bekmc7dIVb8hS%2BNz6RhFSlxrDRklt%2FKRwX6de%2BqyegK0sEezzMm%2BiiV%2BuOvrGDxv5lMTY1xiN%2F7ggX%2BwQzMRR90%2Fh7%2BcVpISTy4J3zwMT1jB8hCXJy%2Bk6Yk%2FbWTbNlagsFUGcKRAQJakMBGPdxmAbn9HMt9AmtU7JE3GvvnVkQggtpvhUFP6Z0pEruP8zDyNdEn77%2FOWWE6KILp6JdXENq0MOXMir0GOqUBUdzNqZumGZQEgmH88nHtTHHe5%2FWsQ%2B3h67uSQZ%2FG6Op8OsGJ5oD9Nob6EVBtJFDLDXdL5XLffJYX%2Bqq%2FT0FFrBt8dXZdLAPLO%2BavfbKH1RaVjSH6pZD6AG3svataIKjAJjXScvDoQVwylIour8psaPHK1Gk%2Fvegx5IIYfmmjPMEN4WZgrsn%2F%2BuGfHPdgM5wEPIIjAJQrBADCBNmDpsy56zUh1DDO&X-Amz-Signature=2c3bdbfc48341e328bd562ebfa0b12c6f7a21608e0e1258d66a376279ffb7565&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EI53FRR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIBBUH%2Fq447lHTa3ER4cH1xa3w8JuAXinaHXymNF%2BkJ5rAiAdaNnUUCFMsTf9AsVFSVpNHWG7ScahD6Hg4kNDEz8aRir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMAAjKyfnmTLy5ASJBKtwDW3Dk7q5rnbDOLIuMg7jx1kAhyVYlEI4OadCweviAgqTzDwuv4QrAPe0Zs7HP8iDmBf1qnM%2B67b4Xw7r%2B010U9eMGVsykm4pepTJrjgELaeWnJ%2ByPHogL8d1s89HvRHv5NNs0La4KJDR8huA9LNuh2PXgdJEfQE%2FHupXImnJXoReuaTb%2Fk2JKwmKaiJtXKpPv%2FX5TIl8ZC6erj5C3qPVrHEdIvuqu9OmhJDJdQAkDy466ux7B6xuyfNbP7dsjPM0r0Oi2QRRw6d6e%2BJx4TeqlhTCndiFOxc5IkrumIYzRY5fskYRjK5k752APuDhjHeEOAvnwcUwBegfc7UBZCwI8OJ7MtH8JyBgn4s79kVsgimj24l%2FPEnc3FownNtUGN%2B6QYanKhG5e0Nk%2FHM3%2FftpyQydYK4xeuYZ017X%2BOcoaXVt3xEmrYLR3h3Lhk0UPKa8wYrSVMG2kQ7EBBsHlAOUzozWYwHGNcd4Qrn2HqoP6zbYjaHAKHVhCm6d5GH6BfmxaSGlKJZ7L1gtjKt0MKp3FsINU8S8FOLHuQIa7q0mzuSC%2F24NzFF0jPNuhG%2B6LeOxX2l6csJdQrT69%2BZiFlFoTrOSfZfTK%2F0T2yUgxCf%2BZXTCnjM%2BJYb%2ByxFt4wd4w0s2KvQY6pgG9PkXn0b47K8RbdHqHE72qNnOQW3JybENJhQOI3vAC%2FAZYk7gVrPWRI4QNC8q%2BVy3uLyY8mYz6isItdeq0OCrrgejGLigAHOfD23ynw61Vu0DY90DNyNReNwF7jSvktHuvRPwR3xd4K1m0rYgfD6xc8ClPIG07U3L5DBC6pv%2BfFCFeKfjCWsdhrfIgiP6BbABW1x%2BlhlqiworaOEK7qUE6f1KgbkVS&X-Amz-Signature=2644cecb9ce7a26887d64b55a7a9fe4cb9d9d9217e536e0f9e91c28710f22633&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EI53FRR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIBBUH%2Fq447lHTa3ER4cH1xa3w8JuAXinaHXymNF%2BkJ5rAiAdaNnUUCFMsTf9AsVFSVpNHWG7ScahD6Hg4kNDEz8aRir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMAAjKyfnmTLy5ASJBKtwDW3Dk7q5rnbDOLIuMg7jx1kAhyVYlEI4OadCweviAgqTzDwuv4QrAPe0Zs7HP8iDmBf1qnM%2B67b4Xw7r%2B010U9eMGVsykm4pepTJrjgELaeWnJ%2ByPHogL8d1s89HvRHv5NNs0La4KJDR8huA9LNuh2PXgdJEfQE%2FHupXImnJXoReuaTb%2Fk2JKwmKaiJtXKpPv%2FX5TIl8ZC6erj5C3qPVrHEdIvuqu9OmhJDJdQAkDy466ux7B6xuyfNbP7dsjPM0r0Oi2QRRw6d6e%2BJx4TeqlhTCndiFOxc5IkrumIYzRY5fskYRjK5k752APuDhjHeEOAvnwcUwBegfc7UBZCwI8OJ7MtH8JyBgn4s79kVsgimj24l%2FPEnc3FownNtUGN%2B6QYanKhG5e0Nk%2FHM3%2FftpyQydYK4xeuYZ017X%2BOcoaXVt3xEmrYLR3h3Lhk0UPKa8wYrSVMG2kQ7EBBsHlAOUzozWYwHGNcd4Qrn2HqoP6zbYjaHAKHVhCm6d5GH6BfmxaSGlKJZ7L1gtjKt0MKp3FsINU8S8FOLHuQIa7q0mzuSC%2F24NzFF0jPNuhG%2B6LeOxX2l6csJdQrT69%2BZiFlFoTrOSfZfTK%2F0T2yUgxCf%2BZXTCnjM%2BJYb%2ByxFt4wd4w0s2KvQY6pgG9PkXn0b47K8RbdHqHE72qNnOQW3JybENJhQOI3vAC%2FAZYk7gVrPWRI4QNC8q%2BVy3uLyY8mYz6isItdeq0OCrrgejGLigAHOfD23ynw61Vu0DY90DNyNReNwF7jSvktHuvRPwR3xd4K1m0rYgfD6xc8ClPIG07U3L5DBC6pv%2BfFCFeKfjCWsdhrfIgiP6BbABW1x%2BlhlqiworaOEK7qUE6f1KgbkVS&X-Amz-Signature=72d61a1eadfd01df4f15c5685b50e4abb26728518551fb1d1c59af8075e594d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EI53FRR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIBBUH%2Fq447lHTa3ER4cH1xa3w8JuAXinaHXymNF%2BkJ5rAiAdaNnUUCFMsTf9AsVFSVpNHWG7ScahD6Hg4kNDEz8aRir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMAAjKyfnmTLy5ASJBKtwDW3Dk7q5rnbDOLIuMg7jx1kAhyVYlEI4OadCweviAgqTzDwuv4QrAPe0Zs7HP8iDmBf1qnM%2B67b4Xw7r%2B010U9eMGVsykm4pepTJrjgELaeWnJ%2ByPHogL8d1s89HvRHv5NNs0La4KJDR8huA9LNuh2PXgdJEfQE%2FHupXImnJXoReuaTb%2Fk2JKwmKaiJtXKpPv%2FX5TIl8ZC6erj5C3qPVrHEdIvuqu9OmhJDJdQAkDy466ux7B6xuyfNbP7dsjPM0r0Oi2QRRw6d6e%2BJx4TeqlhTCndiFOxc5IkrumIYzRY5fskYRjK5k752APuDhjHeEOAvnwcUwBegfc7UBZCwI8OJ7MtH8JyBgn4s79kVsgimj24l%2FPEnc3FownNtUGN%2B6QYanKhG5e0Nk%2FHM3%2FftpyQydYK4xeuYZ017X%2BOcoaXVt3xEmrYLR3h3Lhk0UPKa8wYrSVMG2kQ7EBBsHlAOUzozWYwHGNcd4Qrn2HqoP6zbYjaHAKHVhCm6d5GH6BfmxaSGlKJZ7L1gtjKt0MKp3FsINU8S8FOLHuQIa7q0mzuSC%2F24NzFF0jPNuhG%2B6LeOxX2l6csJdQrT69%2BZiFlFoTrOSfZfTK%2F0T2yUgxCf%2BZXTCnjM%2BJYb%2ByxFt4wd4w0s2KvQY6pgG9PkXn0b47K8RbdHqHE72qNnOQW3JybENJhQOI3vAC%2FAZYk7gVrPWRI4QNC8q%2BVy3uLyY8mYz6isItdeq0OCrrgejGLigAHOfD23ynw61Vu0DY90DNyNReNwF7jSvktHuvRPwR3xd4K1m0rYgfD6xc8ClPIG07U3L5DBC6pv%2BfFCFeKfjCWsdhrfIgiP6BbABW1x%2BlhlqiworaOEK7qUE6f1KgbkVS&X-Amz-Signature=c17e1eeec122113cb579013a456c5ea99d96da181252e0ac14c8c0feb7cb7ce7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EI53FRR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIBBUH%2Fq447lHTa3ER4cH1xa3w8JuAXinaHXymNF%2BkJ5rAiAdaNnUUCFMsTf9AsVFSVpNHWG7ScahD6Hg4kNDEz8aRir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMAAjKyfnmTLy5ASJBKtwDW3Dk7q5rnbDOLIuMg7jx1kAhyVYlEI4OadCweviAgqTzDwuv4QrAPe0Zs7HP8iDmBf1qnM%2B67b4Xw7r%2B010U9eMGVsykm4pepTJrjgELaeWnJ%2ByPHogL8d1s89HvRHv5NNs0La4KJDR8huA9LNuh2PXgdJEfQE%2FHupXImnJXoReuaTb%2Fk2JKwmKaiJtXKpPv%2FX5TIl8ZC6erj5C3qPVrHEdIvuqu9OmhJDJdQAkDy466ux7B6xuyfNbP7dsjPM0r0Oi2QRRw6d6e%2BJx4TeqlhTCndiFOxc5IkrumIYzRY5fskYRjK5k752APuDhjHeEOAvnwcUwBegfc7UBZCwI8OJ7MtH8JyBgn4s79kVsgimj24l%2FPEnc3FownNtUGN%2B6QYanKhG5e0Nk%2FHM3%2FftpyQydYK4xeuYZ017X%2BOcoaXVt3xEmrYLR3h3Lhk0UPKa8wYrSVMG2kQ7EBBsHlAOUzozWYwHGNcd4Qrn2HqoP6zbYjaHAKHVhCm6d5GH6BfmxaSGlKJZ7L1gtjKt0MKp3FsINU8S8FOLHuQIa7q0mzuSC%2F24NzFF0jPNuhG%2B6LeOxX2l6csJdQrT69%2BZiFlFoTrOSfZfTK%2F0T2yUgxCf%2BZXTCnjM%2BJYb%2ByxFt4wd4w0s2KvQY6pgG9PkXn0b47K8RbdHqHE72qNnOQW3JybENJhQOI3vAC%2FAZYk7gVrPWRI4QNC8q%2BVy3uLyY8mYz6isItdeq0OCrrgejGLigAHOfD23ynw61Vu0DY90DNyNReNwF7jSvktHuvRPwR3xd4K1m0rYgfD6xc8ClPIG07U3L5DBC6pv%2BfFCFeKfjCWsdhrfIgiP6BbABW1x%2BlhlqiworaOEK7qUE6f1KgbkVS&X-Amz-Signature=4d65aa0cd94c2000ecc0182a02818e385614c3d7403e9e51b401c8fb14dfbea1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665K44XS75%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQC57RZO4bij3Mj99SGyI76yZLGDfOUwBC2qTVH%2BNv1g%2FwIgTsA0rm2JiYW1lftI9bch6p7POS6DWiK6%2BDKnGGpeMukq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNytq0JnxP63yBMKryrcA8Nc252VelOZAy0%2BMSd09hlL%2FH5fnvfV7ssO9Mn0sFwWQWGZeyJZ1gocejqkNnendDHfMavEINkkn0xt6ruvIgpzHGcYMclGoi%2BExypianvXskKL894GMrP%2BvrMVdF9hxjC3ZL57vA7V4k25x3Vdt0vgNmXwCkrAMGtz2ubuhHVowF3yIriEkV5de7uKlN35H6cco%2FzrPifbj5Me700RVZyETnyZczWmQci8zAv0hxV%2BONtVTOP%2FU9RQUInYFlgm08pyRNbF9vVFzCw1x9ZLOVSCzEAb1CGhI7V7UUtm6GIpx6c0f1CoHTb0C3LMPBZR6T%2B4Offg6dbC8Z4VaXuIhhfavHiVxUjdZID9WXjWSyKunoDaBJ4FtjYDxn%2BBg3Nm4n0wGhFHBg0OYCh%2B0Mf7G211h%2F416uAXbFuOuTNM%2BKRTDkKvU2P8fxGTZEOog6UpLo235BPS43faIAfhVggNXyVkH%2FXA0VFqFZ0lWiRW%2B4Vi%2FXSlZA9uVTNR%2BrRY5feWXTTRR9zM7C5MBrrWJv%2B03%2BIMdSjH%2BNUatQlmnC%2Bcppa5TXbknGlFtnxcRDWI4SzYhayeMqOytByZp4Hz078ZZX4CIsuo7LY%2BC%2F%2FREdx0hfrXdfoVjiJpfjWedi%2FxMKHNir0GOqUBAqi5phFfGmVDgIZMxu%2B3z6B1iQ27q357aza%2F19Uv01FX47vWezSTrV3AA3XTPWBDLinXoFsP81MSShWP4A1mpxsU5uWIrSbP6lCjJ6KcHnJu9AD4ZM3SGXlgifPxkt%2BSMbNNfIFqCbXCOE%2FBX2QPyjp%2B7rXYXsB8kRVsZxoPIwT1uz6VHJpsj9L2cBpukG9E52k1GCDbhKvpiadEyhjRvQRskHvT&X-Amz-Signature=55413d148977e76406c9b40b94b1e55fd689b27d3fb33f6b0f0fcc328ea4c966&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665K44XS75%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQC57RZO4bij3Mj99SGyI76yZLGDfOUwBC2qTVH%2BNv1g%2FwIgTsA0rm2JiYW1lftI9bch6p7POS6DWiK6%2BDKnGGpeMukq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNytq0JnxP63yBMKryrcA8Nc252VelOZAy0%2BMSd09hlL%2FH5fnvfV7ssO9Mn0sFwWQWGZeyJZ1gocejqkNnendDHfMavEINkkn0xt6ruvIgpzHGcYMclGoi%2BExypianvXskKL894GMrP%2BvrMVdF9hxjC3ZL57vA7V4k25x3Vdt0vgNmXwCkrAMGtz2ubuhHVowF3yIriEkV5de7uKlN35H6cco%2FzrPifbj5Me700RVZyETnyZczWmQci8zAv0hxV%2BONtVTOP%2FU9RQUInYFlgm08pyRNbF9vVFzCw1x9ZLOVSCzEAb1CGhI7V7UUtm6GIpx6c0f1CoHTb0C3LMPBZR6T%2B4Offg6dbC8Z4VaXuIhhfavHiVxUjdZID9WXjWSyKunoDaBJ4FtjYDxn%2BBg3Nm4n0wGhFHBg0OYCh%2B0Mf7G211h%2F416uAXbFuOuTNM%2BKRTDkKvU2P8fxGTZEOog6UpLo235BPS43faIAfhVggNXyVkH%2FXA0VFqFZ0lWiRW%2B4Vi%2FXSlZA9uVTNR%2BrRY5feWXTTRR9zM7C5MBrrWJv%2B03%2BIMdSjH%2BNUatQlmnC%2Bcppa5TXbknGlFtnxcRDWI4SzYhayeMqOytByZp4Hz078ZZX4CIsuo7LY%2BC%2F%2FREdx0hfrXdfoVjiJpfjWedi%2FxMKHNir0GOqUBAqi5phFfGmVDgIZMxu%2B3z6B1iQ27q357aza%2F19Uv01FX47vWezSTrV3AA3XTPWBDLinXoFsP81MSShWP4A1mpxsU5uWIrSbP6lCjJ6KcHnJu9AD4ZM3SGXlgifPxkt%2BSMbNNfIFqCbXCOE%2FBX2QPyjp%2B7rXYXsB8kRVsZxoPIwT1uz6VHJpsj9L2cBpukG9E52k1GCDbhKvpiadEyhjRvQRskHvT&X-Amz-Signature=24db054ab77bc8bc82cf42971c148e10524f2dfef9d4fb0a269e05d852f1eeef&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665K44XS75%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQC57RZO4bij3Mj99SGyI76yZLGDfOUwBC2qTVH%2BNv1g%2FwIgTsA0rm2JiYW1lftI9bch6p7POS6DWiK6%2BDKnGGpeMukq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDNytq0JnxP63yBMKryrcA8Nc252VelOZAy0%2BMSd09hlL%2FH5fnvfV7ssO9Mn0sFwWQWGZeyJZ1gocejqkNnendDHfMavEINkkn0xt6ruvIgpzHGcYMclGoi%2BExypianvXskKL894GMrP%2BvrMVdF9hxjC3ZL57vA7V4k25x3Vdt0vgNmXwCkrAMGtz2ubuhHVowF3yIriEkV5de7uKlN35H6cco%2FzrPifbj5Me700RVZyETnyZczWmQci8zAv0hxV%2BONtVTOP%2FU9RQUInYFlgm08pyRNbF9vVFzCw1x9ZLOVSCzEAb1CGhI7V7UUtm6GIpx6c0f1CoHTb0C3LMPBZR6T%2B4Offg6dbC8Z4VaXuIhhfavHiVxUjdZID9WXjWSyKunoDaBJ4FtjYDxn%2BBg3Nm4n0wGhFHBg0OYCh%2B0Mf7G211h%2F416uAXbFuOuTNM%2BKRTDkKvU2P8fxGTZEOog6UpLo235BPS43faIAfhVggNXyVkH%2FXA0VFqFZ0lWiRW%2B4Vi%2FXSlZA9uVTNR%2BrRY5feWXTTRR9zM7C5MBrrWJv%2B03%2BIMdSjH%2BNUatQlmnC%2Bcppa5TXbknGlFtnxcRDWI4SzYhayeMqOytByZp4Hz078ZZX4CIsuo7LY%2BC%2F%2FREdx0hfrXdfoVjiJpfjWedi%2FxMKHNir0GOqUBAqi5phFfGmVDgIZMxu%2B3z6B1iQ27q357aza%2F19Uv01FX47vWezSTrV3AA3XTPWBDLinXoFsP81MSShWP4A1mpxsU5uWIrSbP6lCjJ6KcHnJu9AD4ZM3SGXlgifPxkt%2BSMbNNfIFqCbXCOE%2FBX2QPyjp%2B7rXYXsB8kRVsZxoPIwT1uz6VHJpsj9L2cBpukG9E52k1GCDbhKvpiadEyhjRvQRskHvT&X-Amz-Signature=eb749090d0bd60f7ee4085ede17442b69b17e13f7f695a4e4fa40e0e9bfad8d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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

