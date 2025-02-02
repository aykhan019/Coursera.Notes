

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=3974f0d9a42db4908e905050cd1a1f4385002dfa5dc9df92317110d0d1d11d25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=643c1dc289a0f11e04209a4faacc39924940462fdb163f0ddfb8e5c973d039b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=79e0ffbba521b07c349fa1116afc23585ffe306be1604704d739d39afe51aae9&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=681277a62035dc86db82a842adc5882d37140c90f62e932549b7544867eb1f3a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=859a72e9c57c5bb7af27d9369b0d67a342dff979f477652d57e111a4aa205c98&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=6f05a321fabea9078cebf060fe7131ca82c4e11771be69a5f8f68c5c97f24731&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=a6ea21d9288b6a6b8533ecb1ab25ffbe21e48420972af45e26f3de1f8bb6769a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=7c4c8af1ee45d81a702bf977526f810907ceb70b85a1c786708e3eb78234f2b3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=19028f5a508a8ccaed5cdac68454f3b07484ee7c4e12d32fdde21bf0e79d056e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=aef4b4872c90e72493baf7bb573b827f0faee704f46b5da170374f0e1c60b4ee&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LL7M7QS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFlDDADwpgeU%2BVUZRSafdjrW9xhzZd4%2BXoHORZrso5lFAiEAubzWGL7A%2FZlwYxUJ0YxBWgJ%2BoVHPdlpx8tF%2FPLG31A0qiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMYg%2BknZC3In5Uv5rircA7QSjzijk2zX8Qff7hNn1bpbzDdK5ODFq4%2FrX05414qQvt3ANpK3uESOlLUr0GX%2Bqp1zb%2BlARS%2FA6x%2FRUSJwjKK1xvAW%2B5gi%2B932RbZ1KmCvRJDq9AQwgkcOdsfH3eIZcS5M6gBGtz2RS0rKtnXfi9h2IGkMUWMUSgAw1oOAHk55cQSzZ3E7Adlk78yGkf0OGDD0CCwHUVOU3xClOa859pVAoAqLw7rR%2FF0W6SXcRJ%2FqK4F8twJi2pWzqgGh4F2tKdkSJHHRecNik55bty3M1IxxtfOnBcufNCH%2Fd3cUqKeG58DSkL1iIx%2FqQo33nyf18RP3rohKjustfkFj4wiqSpQaoX%2BO7zCq8BJ98nfny%2Fu4ztdwZErgvWbq0u5IHllILjhq%2Fpu9Mie5Z3I1mGt5n%2Bi0JfHvfxyrshb9rjfT%2Ft2rREkiH6aF0x%2B4lAaZKqI6diUic1ZbNTUmuAIXyT%2FWoEKYNNDtBDOPQMOChOZvVC%2FmnL1Nkze%2B2ZXlNP%2BMLHIlSzKzU2OEQCNJGFETvky109IaWT5BASsAf%2BJx1QIeC2oWzn%2F2vNZFWuCfiGmZVxDmTRp4%2FgR%2BoFe4MvcF5Aj7u55lAqpjxCCSgJjJ2iYoiemAZ%2F6mAxmyUrWefQPwMO%2BT%2FrwGOqUBB8mkO9n3FzAY2QjgvGbl9WDw926aLwDIj%2F1VTlY%2B9LNyBxc5hCVRMeWp5Q%2BUkBfXFFwTwgsmz2%2FbD4o234yoQelgaFwRXyJahJhnr%2B2mX4gzObp9UnwOflCQgxM8pQ3yie4s6C8Sss%2BZEOK6%2Fcbr3v5osWCq62yEmTaR0jwS%2Bs0cLoyd52jt%2FaOndomor3gD0cvm%2BuPZuUZyR1EDC4hCnf%2F2Fb7d&X-Amz-Signature=f6f12fcb6fdb7110765fd091a3bbc190f2b3f53435191fbcd5e70f35ec258e47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ6Z77IE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIdL2vYut3uGjZN%2FhjWRiOii3XusZiy4MyB4jem2EECAiBDR55wzYTu0wj7xtu8XkI9BncY0rcZlFjSQGNcfGnuRSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjmx1QJpgBbBc3NkMKtwDZfFO9u13US2O4jf0i8YEtF4SUtJbVJgd2uC0F6vlS4oCM9OzXssb6jBUwKFMUdVvn5CahHlJhUXhGxP6xrr7cI08IJxAZ4J3JAGLYf7QuU5FiLGRWiFfaGd5uVhQtYAMQ807iThffHQpF5vegnjcEEG8DZb%2BTXOYAXGwK8fZGClUp3FrYG1%2BnfZdjwMLQRQtLTjgQ3%2BNWISy%2Bkyj%2B3ybD3NpHCg19NoPuJ%2Fj%2B5UJj%2BkQZuFYtUlkI%2FTOCW4NaLtSM8269JDTQPSEy29krs807VfXuJi2GCAt5I2RYxj1JVAzD05d0aY%2FI8zJIE9CXWytN%2Bcd7t9quyTcwww2dDTDNAR6O3lYk2pwwOgpHSvv%2FjmV%2Bp4r8mnVIF6PKGBTt4v2SOsOQNhBtuJREWHu7EhBuDH3FCCXyRt3skkOUXTze%2F%2FwPO7Yb2RJgVSEZJ7aD1mnf%2FDLDYjn2cCYChuxkYwIDA4FHy%2BUnnMPflx8kkvh8c70iDSf4cHKuxtV%2F6EnKQ7L8dCDNi7zJcfFAycgp%2FgMpAjP5s5uW6pqddCR%2B6rLRzcf%2FIskfrlSa5T3oXF5g2dzLpcGOrZth7lS1%2FIQfQONEP6LmshHBONVSGTmJzYjimamV3uK0s9m2KqehbQwjt3%2BvAY6pgGaAMq6IQYP1e6PkeK%2B4JvjYSqRvzN7FHLLwfIEoZNxRTGtYFAvUOv%2FnpEL%2Bv6lQSbGH7aMVRhZJduXUTE7v2E4kCSCZJXLFHPZ0pFf4HtFtNPT%2FPihiJQo8TuzGg3%2FIMPgmmDRZLcpgleFJf0yqACdct9urPft35wVlvXEDzFTw19PczGZm89tsETtMyBsFwbSqYK3yWbYcUpkXzqyrWZ8%2BLDXqYBq&X-Amz-Signature=d4ca5e7ac4531b4905bad9c0d9a0a7ca68cb375ba46306a5a8698ac24d8fc340&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ6Z77IE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIdL2vYut3uGjZN%2FhjWRiOii3XusZiy4MyB4jem2EECAiBDR55wzYTu0wj7xtu8XkI9BncY0rcZlFjSQGNcfGnuRSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjmx1QJpgBbBc3NkMKtwDZfFO9u13US2O4jf0i8YEtF4SUtJbVJgd2uC0F6vlS4oCM9OzXssb6jBUwKFMUdVvn5CahHlJhUXhGxP6xrr7cI08IJxAZ4J3JAGLYf7QuU5FiLGRWiFfaGd5uVhQtYAMQ807iThffHQpF5vegnjcEEG8DZb%2BTXOYAXGwK8fZGClUp3FrYG1%2BnfZdjwMLQRQtLTjgQ3%2BNWISy%2Bkyj%2B3ybD3NpHCg19NoPuJ%2Fj%2B5UJj%2BkQZuFYtUlkI%2FTOCW4NaLtSM8269JDTQPSEy29krs807VfXuJi2GCAt5I2RYxj1JVAzD05d0aY%2FI8zJIE9CXWytN%2Bcd7t9quyTcwww2dDTDNAR6O3lYk2pwwOgpHSvv%2FjmV%2Bp4r8mnVIF6PKGBTt4v2SOsOQNhBtuJREWHu7EhBuDH3FCCXyRt3skkOUXTze%2F%2FwPO7Yb2RJgVSEZJ7aD1mnf%2FDLDYjn2cCYChuxkYwIDA4FHy%2BUnnMPflx8kkvh8c70iDSf4cHKuxtV%2F6EnKQ7L8dCDNi7zJcfFAycgp%2FgMpAjP5s5uW6pqddCR%2B6rLRzcf%2FIskfrlSa5T3oXF5g2dzLpcGOrZth7lS1%2FIQfQONEP6LmshHBONVSGTmJzYjimamV3uK0s9m2KqehbQwjt3%2BvAY6pgGaAMq6IQYP1e6PkeK%2B4JvjYSqRvzN7FHLLwfIEoZNxRTGtYFAvUOv%2FnpEL%2Bv6lQSbGH7aMVRhZJduXUTE7v2E4kCSCZJXLFHPZ0pFf4HtFtNPT%2FPihiJQo8TuzGg3%2FIMPgmmDRZLcpgleFJf0yqACdct9urPft35wVlvXEDzFTw19PczGZm89tsETtMyBsFwbSqYK3yWbYcUpkXzqyrWZ8%2BLDXqYBq&X-Amz-Signature=23c4adcc383edfab086648dec49373fe05eaab478a115ccbd3d41cdf336c0b01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ6Z77IE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIdL2vYut3uGjZN%2FhjWRiOii3XusZiy4MyB4jem2EECAiBDR55wzYTu0wj7xtu8XkI9BncY0rcZlFjSQGNcfGnuRSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjmx1QJpgBbBc3NkMKtwDZfFO9u13US2O4jf0i8YEtF4SUtJbVJgd2uC0F6vlS4oCM9OzXssb6jBUwKFMUdVvn5CahHlJhUXhGxP6xrr7cI08IJxAZ4J3JAGLYf7QuU5FiLGRWiFfaGd5uVhQtYAMQ807iThffHQpF5vegnjcEEG8DZb%2BTXOYAXGwK8fZGClUp3FrYG1%2BnfZdjwMLQRQtLTjgQ3%2BNWISy%2Bkyj%2B3ybD3NpHCg19NoPuJ%2Fj%2B5UJj%2BkQZuFYtUlkI%2FTOCW4NaLtSM8269JDTQPSEy29krs807VfXuJi2GCAt5I2RYxj1JVAzD05d0aY%2FI8zJIE9CXWytN%2Bcd7t9quyTcwww2dDTDNAR6O3lYk2pwwOgpHSvv%2FjmV%2Bp4r8mnVIF6PKGBTt4v2SOsOQNhBtuJREWHu7EhBuDH3FCCXyRt3skkOUXTze%2F%2FwPO7Yb2RJgVSEZJ7aD1mnf%2FDLDYjn2cCYChuxkYwIDA4FHy%2BUnnMPflx8kkvh8c70iDSf4cHKuxtV%2F6EnKQ7L8dCDNi7zJcfFAycgp%2FgMpAjP5s5uW6pqddCR%2B6rLRzcf%2FIskfrlSa5T3oXF5g2dzLpcGOrZth7lS1%2FIQfQONEP6LmshHBONVSGTmJzYjimamV3uK0s9m2KqehbQwjt3%2BvAY6pgGaAMq6IQYP1e6PkeK%2B4JvjYSqRvzN7FHLLwfIEoZNxRTGtYFAvUOv%2FnpEL%2Bv6lQSbGH7aMVRhZJduXUTE7v2E4kCSCZJXLFHPZ0pFf4HtFtNPT%2FPihiJQo8TuzGg3%2FIMPgmmDRZLcpgleFJf0yqACdct9urPft35wVlvXEDzFTw19PczGZm89tsETtMyBsFwbSqYK3yWbYcUpkXzqyrWZ8%2BLDXqYBq&X-Amz-Signature=99e77fee71bfc734beeb9fd93807822eb8e65dee73ea6d8721a1473cee5bf7d2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ6Z77IE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIdL2vYut3uGjZN%2FhjWRiOii3XusZiy4MyB4jem2EECAiBDR55wzYTu0wj7xtu8XkI9BncY0rcZlFjSQGNcfGnuRSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjmx1QJpgBbBc3NkMKtwDZfFO9u13US2O4jf0i8YEtF4SUtJbVJgd2uC0F6vlS4oCM9OzXssb6jBUwKFMUdVvn5CahHlJhUXhGxP6xrr7cI08IJxAZ4J3JAGLYf7QuU5FiLGRWiFfaGd5uVhQtYAMQ807iThffHQpF5vegnjcEEG8DZb%2BTXOYAXGwK8fZGClUp3FrYG1%2BnfZdjwMLQRQtLTjgQ3%2BNWISy%2Bkyj%2B3ybD3NpHCg19NoPuJ%2Fj%2B5UJj%2BkQZuFYtUlkI%2FTOCW4NaLtSM8269JDTQPSEy29krs807VfXuJi2GCAt5I2RYxj1JVAzD05d0aY%2FI8zJIE9CXWytN%2Bcd7t9quyTcwww2dDTDNAR6O3lYk2pwwOgpHSvv%2FjmV%2Bp4r8mnVIF6PKGBTt4v2SOsOQNhBtuJREWHu7EhBuDH3FCCXyRt3skkOUXTze%2F%2FwPO7Yb2RJgVSEZJ7aD1mnf%2FDLDYjn2cCYChuxkYwIDA4FHy%2BUnnMPflx8kkvh8c70iDSf4cHKuxtV%2F6EnKQ7L8dCDNi7zJcfFAycgp%2FgMpAjP5s5uW6pqddCR%2B6rLRzcf%2FIskfrlSa5T3oXF5g2dzLpcGOrZth7lS1%2FIQfQONEP6LmshHBONVSGTmJzYjimamV3uK0s9m2KqehbQwjt3%2BvAY6pgGaAMq6IQYP1e6PkeK%2B4JvjYSqRvzN7FHLLwfIEoZNxRTGtYFAvUOv%2FnpEL%2Bv6lQSbGH7aMVRhZJduXUTE7v2E4kCSCZJXLFHPZ0pFf4HtFtNPT%2FPihiJQo8TuzGg3%2FIMPgmmDRZLcpgleFJf0yqACdct9urPft35wVlvXEDzFTw19PczGZm89tsETtMyBsFwbSqYK3yWbYcUpkXzqyrWZ8%2BLDXqYBq&X-Amz-Signature=b397d663738777f79c49f96caece6912f1f8d748a3688c74d6207deec9e20e11&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5XCK3IQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6MGbk91rZVKGF%2FZ8Wnq4fYm%2FTk2cfdtRk%2FIrHt%2B8YuQIhAOranuTnfAPmKkppTI%2FIkMfClNEwnJ36%2B1Gs3hAdQek3KogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx99EM5P4vOjkvUxZYq3AOlRZnWrCegzGy3Xi4Zd0mI28E5jylyeJFrvEMcxZesd2ZH7gQ3uX2T7bYcN%2B97jRDAQCGUwG9oqGEzBbWtHMZd2YGlXjc5qiXf%2FsudFfvGM7%2BWmB7ITnW0wR%2F2jL1EFN0fTDOTAuGIP%2Bfn%2BrT13HDT7bGHq114FoS1c38pP6ACHBz4qMQBNmCkmkiE2tL3BQ0lbjSTgRZNtCComkV2vgc6OSHWdCR1VGpMu%2B5PFT2PbJntHeASnjHT4ru62DmNDRKJHJ5giAovsiSci9ppAJ6J3oVdS%2FdfJs9XoxbyLm%2Fd4jtXR%2BZLR3KnLNFzj1HUVkOhKRfE26qdA2zA%2F1sZ9fNQlZH16xJBdISeuCjdLnocfI8doiZkdz%2B7Eg31ryo5RR%2BIDTAZ6D483HRKe%2BA6x6nRR2ZOmFqnMuWsiTr%2BTS3qBznLIz%2BUSfxzHG13V9BOJQQew4RJOCLqPD2Xh4l2M8Ozzu8Gxvh3aQI08UNMvS%2B1kZhdy%2Br%2BxeMUq%2Fg87EZZ7UnN6xNf7aTbl5ZpwwROoUXksaoYjFh5ZNPq%2BU8DDf3UnxcFD4IxQxAM%2ByfnLSEjieJPHs8Ymzth9tZYYo0rLlfZi8wzvDKK%2FZeShrYH2KXxVJ%2BRs8nfXUs1ToQr0jCR3f68BjqkAXXVFTQukMPwENzP9YUIexevgsXhUBv5vjlCJuO4U5IylSP2ZP7F6Yb31DQO5K%2Fk51XcaltSJajTChBCB29SiedLW04qSqiMYCmDNIzktTSSJ%2B8Sx1%2FBRBvpO6XjBOGFuvwEiQQUb%2BH%2BMOTXDHtOVtoGGsymOm1oIc6S0MgG14yOLke5dATy7cMpCgtUmt2bf%2FubTvHSJCkaRe55Yr6QCPOQJGFa&X-Amz-Signature=feb5d2a463737288fa9e3a569883a1564cf14cbfb7990c77088fb57fa39fa6ca&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5XCK3IQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6MGbk91rZVKGF%2FZ8Wnq4fYm%2FTk2cfdtRk%2FIrHt%2B8YuQIhAOranuTnfAPmKkppTI%2FIkMfClNEwnJ36%2B1Gs3hAdQek3KogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx99EM5P4vOjkvUxZYq3AOlRZnWrCegzGy3Xi4Zd0mI28E5jylyeJFrvEMcxZesd2ZH7gQ3uX2T7bYcN%2B97jRDAQCGUwG9oqGEzBbWtHMZd2YGlXjc5qiXf%2FsudFfvGM7%2BWmB7ITnW0wR%2F2jL1EFN0fTDOTAuGIP%2Bfn%2BrT13HDT7bGHq114FoS1c38pP6ACHBz4qMQBNmCkmkiE2tL3BQ0lbjSTgRZNtCComkV2vgc6OSHWdCR1VGpMu%2B5PFT2PbJntHeASnjHT4ru62DmNDRKJHJ5giAovsiSci9ppAJ6J3oVdS%2FdfJs9XoxbyLm%2Fd4jtXR%2BZLR3KnLNFzj1HUVkOhKRfE26qdA2zA%2F1sZ9fNQlZH16xJBdISeuCjdLnocfI8doiZkdz%2B7Eg31ryo5RR%2BIDTAZ6D483HRKe%2BA6x6nRR2ZOmFqnMuWsiTr%2BTS3qBznLIz%2BUSfxzHG13V9BOJQQew4RJOCLqPD2Xh4l2M8Ozzu8Gxvh3aQI08UNMvS%2B1kZhdy%2Br%2BxeMUq%2Fg87EZZ7UnN6xNf7aTbl5ZpwwROoUXksaoYjFh5ZNPq%2BU8DDf3UnxcFD4IxQxAM%2ByfnLSEjieJPHs8Ymzth9tZYYo0rLlfZi8wzvDKK%2FZeShrYH2KXxVJ%2BRs8nfXUs1ToQr0jCR3f68BjqkAXXVFTQukMPwENzP9YUIexevgsXhUBv5vjlCJuO4U5IylSP2ZP7F6Yb31DQO5K%2Fk51XcaltSJajTChBCB29SiedLW04qSqiMYCmDNIzktTSSJ%2B8Sx1%2FBRBvpO6XjBOGFuvwEiQQUb%2BH%2BMOTXDHtOVtoGGsymOm1oIc6S0MgG14yOLke5dATy7cMpCgtUmt2bf%2FubTvHSJCkaRe55Yr6QCPOQJGFa&X-Amz-Signature=2cfa1b9c65d7dd224f798b1557e1b4cdbb409375f84a336014cca431ed6599f3&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5XCK3IQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6MGbk91rZVKGF%2FZ8Wnq4fYm%2FTk2cfdtRk%2FIrHt%2B8YuQIhAOranuTnfAPmKkppTI%2FIkMfClNEwnJ36%2B1Gs3hAdQek3KogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx99EM5P4vOjkvUxZYq3AOlRZnWrCegzGy3Xi4Zd0mI28E5jylyeJFrvEMcxZesd2ZH7gQ3uX2T7bYcN%2B97jRDAQCGUwG9oqGEzBbWtHMZd2YGlXjc5qiXf%2FsudFfvGM7%2BWmB7ITnW0wR%2F2jL1EFN0fTDOTAuGIP%2Bfn%2BrT13HDT7bGHq114FoS1c38pP6ACHBz4qMQBNmCkmkiE2tL3BQ0lbjSTgRZNtCComkV2vgc6OSHWdCR1VGpMu%2B5PFT2PbJntHeASnjHT4ru62DmNDRKJHJ5giAovsiSci9ppAJ6J3oVdS%2FdfJs9XoxbyLm%2Fd4jtXR%2BZLR3KnLNFzj1HUVkOhKRfE26qdA2zA%2F1sZ9fNQlZH16xJBdISeuCjdLnocfI8doiZkdz%2B7Eg31ryo5RR%2BIDTAZ6D483HRKe%2BA6x6nRR2ZOmFqnMuWsiTr%2BTS3qBznLIz%2BUSfxzHG13V9BOJQQew4RJOCLqPD2Xh4l2M8Ozzu8Gxvh3aQI08UNMvS%2B1kZhdy%2Br%2BxeMUq%2Fg87EZZ7UnN6xNf7aTbl5ZpwwROoUXksaoYjFh5ZNPq%2BU8DDf3UnxcFD4IxQxAM%2ByfnLSEjieJPHs8Ymzth9tZYYo0rLlfZi8wzvDKK%2FZeShrYH2KXxVJ%2BRs8nfXUs1ToQr0jCR3f68BjqkAXXVFTQukMPwENzP9YUIexevgsXhUBv5vjlCJuO4U5IylSP2ZP7F6Yb31DQO5K%2Fk51XcaltSJajTChBCB29SiedLW04qSqiMYCmDNIzktTSSJ%2B8Sx1%2FBRBvpO6XjBOGFuvwEiQQUb%2BH%2BMOTXDHtOVtoGGsymOm1oIc6S0MgG14yOLke5dATy7cMpCgtUmt2bf%2FubTvHSJCkaRe55Yr6QCPOQJGFa&X-Amz-Signature=ae45ab030c130931f036a67b7db1f55d31124448e136f20048e118d7899f63fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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

