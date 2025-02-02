

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2UWM3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8XXoipkylp4YMaSnPnnVWmMSONvCI1Nuc3e5IFTE%2FAiEAkOp3OzPXWv0klkre2zVzHaU7w0%2Bcs%2FCXwiNwG3QzXtQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG94ijDWvCa6BBtdlSrcA9s9bcnXgDQn12lwT%2FWRhX2NZxzn%2B9oalQCNs7CnNfghslS7ho0QInZQyiOyRWI4Q%2B80J5%2FXrqiLL5bi2mmcMFH7jaBy%2BTSJ5R%2FgngdqCYMZaaWyQ547LD9cQz3qBcuS4zc5JF8vmM4YaIM2o2nb8PSL078AssIsbBGNDz74ouCuiG6upvV6lvbq1YGxEp4Qk1Z8RHY8NOYwEjOjhWlUIwmmjHQMJr5CFmxMf1H%2FaSZc2w0LzxblczrX7XdBGfjpLn46%2FhkJlvyXoqmMW9nyfv2K8S%2F8e3LlptraaxwOVlpwPsHePdQpl%2F8rnL%2BOY%2BnxCF4drO5Uy3MZdJm3M3X%2Fy%2B3w4eQuFgHQoKdsMnKSqxJYSGPuqs4IcOI5m4NUFmhfju7g%2B%2BmJOfhE6tB4B%2B21mDfTFAZocLdppXQ%2FEXLnQm9I%2FlK6WL18LXoepldfah%2BAr2sOvzY9zQFyCZaXNRixOtw%2BNX%2BIU%2BtJGM0cA2rQVxtlDs4oJM5X8Y2vXzv8zt2R4rTIlR3VXJBtAtjSV3bzD1EEPXHwHxv8jKt0fGlS4qit9PjIzkxW%2F1rgux4WF3ywTm2wGVp2X%2Fh8MskmgpJLWkFRAbPMh7DkN9G%2FBM%2BcyirnEEyf6x815ptX9rmJMKrX%2FrwGOqUBiH9%2BYc6w2v6DGVJjJtXzdNoc6vAT%2BeJRPQ7TOF5IgX3R0Jg4zURwADOTiZJ%2Fbb%2F7QayHnaqqVRcZwWW4975QBXwyoLgWXaID0T9pMrVPl3Oy7j8wjLspzstoiJZ5SRU4T9SUs2MGV%2BfyYkas70PHWiF74YBhrZD7Q9L2jKeqJPb9E%2FYAGXpa9Xe%2FnzZ%2BbeSas3EdHyBltXqGH%2BTYbP4ak93zFwIX&X-Amz-Signature=08caf474a313744f83b67e15abd0076c48c102744292e296e4366e23f836fb16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2UWM3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8XXoipkylp4YMaSnPnnVWmMSONvCI1Nuc3e5IFTE%2FAiEAkOp3OzPXWv0klkre2zVzHaU7w0%2Bcs%2FCXwiNwG3QzXtQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG94ijDWvCa6BBtdlSrcA9s9bcnXgDQn12lwT%2FWRhX2NZxzn%2B9oalQCNs7CnNfghslS7ho0QInZQyiOyRWI4Q%2B80J5%2FXrqiLL5bi2mmcMFH7jaBy%2BTSJ5R%2FgngdqCYMZaaWyQ547LD9cQz3qBcuS4zc5JF8vmM4YaIM2o2nb8PSL078AssIsbBGNDz74ouCuiG6upvV6lvbq1YGxEp4Qk1Z8RHY8NOYwEjOjhWlUIwmmjHQMJr5CFmxMf1H%2FaSZc2w0LzxblczrX7XdBGfjpLn46%2FhkJlvyXoqmMW9nyfv2K8S%2F8e3LlptraaxwOVlpwPsHePdQpl%2F8rnL%2BOY%2BnxCF4drO5Uy3MZdJm3M3X%2Fy%2B3w4eQuFgHQoKdsMnKSqxJYSGPuqs4IcOI5m4NUFmhfju7g%2B%2BmJOfhE6tB4B%2B21mDfTFAZocLdppXQ%2FEXLnQm9I%2FlK6WL18LXoepldfah%2BAr2sOvzY9zQFyCZaXNRixOtw%2BNX%2BIU%2BtJGM0cA2rQVxtlDs4oJM5X8Y2vXzv8zt2R4rTIlR3VXJBtAtjSV3bzD1EEPXHwHxv8jKt0fGlS4qit9PjIzkxW%2F1rgux4WF3ywTm2wGVp2X%2Fh8MskmgpJLWkFRAbPMh7DkN9G%2FBM%2BcyirnEEyf6x815ptX9rmJMKrX%2FrwGOqUBiH9%2BYc6w2v6DGVJjJtXzdNoc6vAT%2BeJRPQ7TOF5IgX3R0Jg4zURwADOTiZJ%2Fbb%2F7QayHnaqqVRcZwWW4975QBXwyoLgWXaID0T9pMrVPl3Oy7j8wjLspzstoiJZ5SRU4T9SUs2MGV%2BfyYkas70PHWiF74YBhrZD7Q9L2jKeqJPb9E%2FYAGXpa9Xe%2FnzZ%2BbeSas3EdHyBltXqGH%2BTYbP4ak93zFwIX&X-Amz-Signature=2fa6ddfea05d82bee1e6b8edbfbbb1f4abd838a235de8e656d21512cd98f9fe6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2UWM3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8XXoipkylp4YMaSnPnnVWmMSONvCI1Nuc3e5IFTE%2FAiEAkOp3OzPXWv0klkre2zVzHaU7w0%2Bcs%2FCXwiNwG3QzXtQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG94ijDWvCa6BBtdlSrcA9s9bcnXgDQn12lwT%2FWRhX2NZxzn%2B9oalQCNs7CnNfghslS7ho0QInZQyiOyRWI4Q%2B80J5%2FXrqiLL5bi2mmcMFH7jaBy%2BTSJ5R%2FgngdqCYMZaaWyQ547LD9cQz3qBcuS4zc5JF8vmM4YaIM2o2nb8PSL078AssIsbBGNDz74ouCuiG6upvV6lvbq1YGxEp4Qk1Z8RHY8NOYwEjOjhWlUIwmmjHQMJr5CFmxMf1H%2FaSZc2w0LzxblczrX7XdBGfjpLn46%2FhkJlvyXoqmMW9nyfv2K8S%2F8e3LlptraaxwOVlpwPsHePdQpl%2F8rnL%2BOY%2BnxCF4drO5Uy3MZdJm3M3X%2Fy%2B3w4eQuFgHQoKdsMnKSqxJYSGPuqs4IcOI5m4NUFmhfju7g%2B%2BmJOfhE6tB4B%2B21mDfTFAZocLdppXQ%2FEXLnQm9I%2FlK6WL18LXoepldfah%2BAr2sOvzY9zQFyCZaXNRixOtw%2BNX%2BIU%2BtJGM0cA2rQVxtlDs4oJM5X8Y2vXzv8zt2R4rTIlR3VXJBtAtjSV3bzD1EEPXHwHxv8jKt0fGlS4qit9PjIzkxW%2F1rgux4WF3ywTm2wGVp2X%2Fh8MskmgpJLWkFRAbPMh7DkN9G%2FBM%2BcyirnEEyf6x815ptX9rmJMKrX%2FrwGOqUBiH9%2BYc6w2v6DGVJjJtXzdNoc6vAT%2BeJRPQ7TOF5IgX3R0Jg4zURwADOTiZJ%2Fbb%2F7QayHnaqqVRcZwWW4975QBXwyoLgWXaID0T9pMrVPl3Oy7j8wjLspzstoiJZ5SRU4T9SUs2MGV%2BfyYkas70PHWiF74YBhrZD7Q9L2jKeqJPb9E%2FYAGXpa9Xe%2FnzZ%2BbeSas3EdHyBltXqGH%2BTYbP4ak93zFwIX&X-Amz-Signature=192d981e46edccdf1aebf9b1cd73bb1964e4d4d9117ae9bd54f0fc95862106f1&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2UWM3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8XXoipkylp4YMaSnPnnVWmMSONvCI1Nuc3e5IFTE%2FAiEAkOp3OzPXWv0klkre2zVzHaU7w0%2Bcs%2FCXwiNwG3QzXtQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG94ijDWvCa6BBtdlSrcA9s9bcnXgDQn12lwT%2FWRhX2NZxzn%2B9oalQCNs7CnNfghslS7ho0QInZQyiOyRWI4Q%2B80J5%2FXrqiLL5bi2mmcMFH7jaBy%2BTSJ5R%2FgngdqCYMZaaWyQ547LD9cQz3qBcuS4zc5JF8vmM4YaIM2o2nb8PSL078AssIsbBGNDz74ouCuiG6upvV6lvbq1YGxEp4Qk1Z8RHY8NOYwEjOjhWlUIwmmjHQMJr5CFmxMf1H%2FaSZc2w0LzxblczrX7XdBGfjpLn46%2FhkJlvyXoqmMW9nyfv2K8S%2F8e3LlptraaxwOVlpwPsHePdQpl%2F8rnL%2BOY%2BnxCF4drO5Uy3MZdJm3M3X%2Fy%2B3w4eQuFgHQoKdsMnKSqxJYSGPuqs4IcOI5m4NUFmhfju7g%2B%2BmJOfhE6tB4B%2B21mDfTFAZocLdppXQ%2FEXLnQm9I%2FlK6WL18LXoepldfah%2BAr2sOvzY9zQFyCZaXNRixOtw%2BNX%2BIU%2BtJGM0cA2rQVxtlDs4oJM5X8Y2vXzv8zt2R4rTIlR3VXJBtAtjSV3bzD1EEPXHwHxv8jKt0fGlS4qit9PjIzkxW%2F1rgux4WF3ywTm2wGVp2X%2Fh8MskmgpJLWkFRAbPMh7DkN9G%2FBM%2BcyirnEEyf6x815ptX9rmJMKrX%2FrwGOqUBiH9%2BYc6w2v6DGVJjJtXzdNoc6vAT%2BeJRPQ7TOF5IgX3R0Jg4zURwADOTiZJ%2Fbb%2F7QayHnaqqVRcZwWW4975QBXwyoLgWXaID0T9pMrVPl3Oy7j8wjLspzstoiJZ5SRU4T9SUs2MGV%2BfyYkas70PHWiF74YBhrZD7Q9L2jKeqJPb9E%2FYAGXpa9Xe%2FnzZ%2BbeSas3EdHyBltXqGH%2BTYbP4ak93zFwIX&X-Amz-Signature=c17c2e80df2ff0eab054dab2d7c862041439376ffa65ac53681ff05da855ffc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2UWM3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8XXoipkylp4YMaSnPnnVWmMSONvCI1Nuc3e5IFTE%2FAiEAkOp3OzPXWv0klkre2zVzHaU7w0%2Bcs%2FCXwiNwG3QzXtQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG94ijDWvCa6BBtdlSrcA9s9bcnXgDQn12lwT%2FWRhX2NZxzn%2B9oalQCNs7CnNfghslS7ho0QInZQyiOyRWI4Q%2B80J5%2FXrqiLL5bi2mmcMFH7jaBy%2BTSJ5R%2FgngdqCYMZaaWyQ547LD9cQz3qBcuS4zc5JF8vmM4YaIM2o2nb8PSL078AssIsbBGNDz74ouCuiG6upvV6lvbq1YGxEp4Qk1Z8RHY8NOYwEjOjhWlUIwmmjHQMJr5CFmxMf1H%2FaSZc2w0LzxblczrX7XdBGfjpLn46%2FhkJlvyXoqmMW9nyfv2K8S%2F8e3LlptraaxwOVlpwPsHePdQpl%2F8rnL%2BOY%2BnxCF4drO5Uy3MZdJm3M3X%2Fy%2B3w4eQuFgHQoKdsMnKSqxJYSGPuqs4IcOI5m4NUFmhfju7g%2B%2BmJOfhE6tB4B%2B21mDfTFAZocLdppXQ%2FEXLnQm9I%2FlK6WL18LXoepldfah%2BAr2sOvzY9zQFyCZaXNRixOtw%2BNX%2BIU%2BtJGM0cA2rQVxtlDs4oJM5X8Y2vXzv8zt2R4rTIlR3VXJBtAtjSV3bzD1EEPXHwHxv8jKt0fGlS4qit9PjIzkxW%2F1rgux4WF3ywTm2wGVp2X%2Fh8MskmgpJLWkFRAbPMh7DkN9G%2FBM%2BcyirnEEyf6x815ptX9rmJMKrX%2FrwGOqUBiH9%2BYc6w2v6DGVJjJtXzdNoc6vAT%2BeJRPQ7TOF5IgX3R0Jg4zURwADOTiZJ%2Fbb%2F7QayHnaqqVRcZwWW4975QBXwyoLgWXaID0T9pMrVPl3Oy7j8wjLspzstoiJZ5SRU4T9SUs2MGV%2BfyYkas70PHWiF74YBhrZD7Q9L2jKeqJPb9E%2FYAGXpa9Xe%2FnzZ%2BbeSas3EdHyBltXqGH%2BTYbP4ak93zFwIX&X-Amz-Signature=9f47cc226efecbb46cf392dd8935bd1b206ea7d0fa54bcc17ab6b9559db2cbee&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2UWM3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8XXoipkylp4YMaSnPnnVWmMSONvCI1Nuc3e5IFTE%2FAiEAkOp3OzPXWv0klkre2zVzHaU7w0%2Bcs%2FCXwiNwG3QzXtQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG94ijDWvCa6BBtdlSrcA9s9bcnXgDQn12lwT%2FWRhX2NZxzn%2B9oalQCNs7CnNfghslS7ho0QInZQyiOyRWI4Q%2B80J5%2FXrqiLL5bi2mmcMFH7jaBy%2BTSJ5R%2FgngdqCYMZaaWyQ547LD9cQz3qBcuS4zc5JF8vmM4YaIM2o2nb8PSL078AssIsbBGNDz74ouCuiG6upvV6lvbq1YGxEp4Qk1Z8RHY8NOYwEjOjhWlUIwmmjHQMJr5CFmxMf1H%2FaSZc2w0LzxblczrX7XdBGfjpLn46%2FhkJlvyXoqmMW9nyfv2K8S%2F8e3LlptraaxwOVlpwPsHePdQpl%2F8rnL%2BOY%2BnxCF4drO5Uy3MZdJm3M3X%2Fy%2B3w4eQuFgHQoKdsMnKSqxJYSGPuqs4IcOI5m4NUFmhfju7g%2B%2BmJOfhE6tB4B%2B21mDfTFAZocLdppXQ%2FEXLnQm9I%2FlK6WL18LXoepldfah%2BAr2sOvzY9zQFyCZaXNRixOtw%2BNX%2BIU%2BtJGM0cA2rQVxtlDs4oJM5X8Y2vXzv8zt2R4rTIlR3VXJBtAtjSV3bzD1EEPXHwHxv8jKt0fGlS4qit9PjIzkxW%2F1rgux4WF3ywTm2wGVp2X%2Fh8MskmgpJLWkFRAbPMh7DkN9G%2FBM%2BcyirnEEyf6x815ptX9rmJMKrX%2FrwGOqUBiH9%2BYc6w2v6DGVJjJtXzdNoc6vAT%2BeJRPQ7TOF5IgX3R0Jg4zURwADOTiZJ%2Fbb%2F7QayHnaqqVRcZwWW4975QBXwyoLgWXaID0T9pMrVPl3Oy7j8wjLspzstoiJZ5SRU4T9SUs2MGV%2BfyYkas70PHWiF74YBhrZD7Q9L2jKeqJPb9E%2FYAGXpa9Xe%2FnzZ%2BbeSas3EdHyBltXqGH%2BTYbP4ak93zFwIX&X-Amz-Signature=0c69783417e96424ef7d606e65841ea60c5fc0eb37345c3af80d8c3c93e3e6a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2UWM3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8XXoipkylp4YMaSnPnnVWmMSONvCI1Nuc3e5IFTE%2FAiEAkOp3OzPXWv0klkre2zVzHaU7w0%2Bcs%2FCXwiNwG3QzXtQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG94ijDWvCa6BBtdlSrcA9s9bcnXgDQn12lwT%2FWRhX2NZxzn%2B9oalQCNs7CnNfghslS7ho0QInZQyiOyRWI4Q%2B80J5%2FXrqiLL5bi2mmcMFH7jaBy%2BTSJ5R%2FgngdqCYMZaaWyQ547LD9cQz3qBcuS4zc5JF8vmM4YaIM2o2nb8PSL078AssIsbBGNDz74ouCuiG6upvV6lvbq1YGxEp4Qk1Z8RHY8NOYwEjOjhWlUIwmmjHQMJr5CFmxMf1H%2FaSZc2w0LzxblczrX7XdBGfjpLn46%2FhkJlvyXoqmMW9nyfv2K8S%2F8e3LlptraaxwOVlpwPsHePdQpl%2F8rnL%2BOY%2BnxCF4drO5Uy3MZdJm3M3X%2Fy%2B3w4eQuFgHQoKdsMnKSqxJYSGPuqs4IcOI5m4NUFmhfju7g%2B%2BmJOfhE6tB4B%2B21mDfTFAZocLdppXQ%2FEXLnQm9I%2FlK6WL18LXoepldfah%2BAr2sOvzY9zQFyCZaXNRixOtw%2BNX%2BIU%2BtJGM0cA2rQVxtlDs4oJM5X8Y2vXzv8zt2R4rTIlR3VXJBtAtjSV3bzD1EEPXHwHxv8jKt0fGlS4qit9PjIzkxW%2F1rgux4WF3ywTm2wGVp2X%2Fh8MskmgpJLWkFRAbPMh7DkN9G%2FBM%2BcyirnEEyf6x815ptX9rmJMKrX%2FrwGOqUBiH9%2BYc6w2v6DGVJjJtXzdNoc6vAT%2BeJRPQ7TOF5IgX3R0Jg4zURwADOTiZJ%2Fbb%2F7QayHnaqqVRcZwWW4975QBXwyoLgWXaID0T9pMrVPl3Oy7j8wjLspzstoiJZ5SRU4T9SUs2MGV%2BfyYkas70PHWiF74YBhrZD7Q9L2jKeqJPb9E%2FYAGXpa9Xe%2FnzZ%2BbeSas3EdHyBltXqGH%2BTYbP4ak93zFwIX&X-Amz-Signature=10911f6fb6648ecf33a5ff47b816ddf2ee4ef911ba74c8cc904dcbb8775532bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2UWM3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8XXoipkylp4YMaSnPnnVWmMSONvCI1Nuc3e5IFTE%2FAiEAkOp3OzPXWv0klkre2zVzHaU7w0%2Bcs%2FCXwiNwG3QzXtQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG94ijDWvCa6BBtdlSrcA9s9bcnXgDQn12lwT%2FWRhX2NZxzn%2B9oalQCNs7CnNfghslS7ho0QInZQyiOyRWI4Q%2B80J5%2FXrqiLL5bi2mmcMFH7jaBy%2BTSJ5R%2FgngdqCYMZaaWyQ547LD9cQz3qBcuS4zc5JF8vmM4YaIM2o2nb8PSL078AssIsbBGNDz74ouCuiG6upvV6lvbq1YGxEp4Qk1Z8RHY8NOYwEjOjhWlUIwmmjHQMJr5CFmxMf1H%2FaSZc2w0LzxblczrX7XdBGfjpLn46%2FhkJlvyXoqmMW9nyfv2K8S%2F8e3LlptraaxwOVlpwPsHePdQpl%2F8rnL%2BOY%2BnxCF4drO5Uy3MZdJm3M3X%2Fy%2B3w4eQuFgHQoKdsMnKSqxJYSGPuqs4IcOI5m4NUFmhfju7g%2B%2BmJOfhE6tB4B%2B21mDfTFAZocLdppXQ%2FEXLnQm9I%2FlK6WL18LXoepldfah%2BAr2sOvzY9zQFyCZaXNRixOtw%2BNX%2BIU%2BtJGM0cA2rQVxtlDs4oJM5X8Y2vXzv8zt2R4rTIlR3VXJBtAtjSV3bzD1EEPXHwHxv8jKt0fGlS4qit9PjIzkxW%2F1rgux4WF3ywTm2wGVp2X%2Fh8MskmgpJLWkFRAbPMh7DkN9G%2FBM%2BcyirnEEyf6x815ptX9rmJMKrX%2FrwGOqUBiH9%2BYc6w2v6DGVJjJtXzdNoc6vAT%2BeJRPQ7TOF5IgX3R0Jg4zURwADOTiZJ%2Fbb%2F7QayHnaqqVRcZwWW4975QBXwyoLgWXaID0T9pMrVPl3Oy7j8wjLspzstoiJZ5SRU4T9SUs2MGV%2BfyYkas70PHWiF74YBhrZD7Q9L2jKeqJPb9E%2FYAGXpa9Xe%2FnzZ%2BbeSas3EdHyBltXqGH%2BTYbP4ak93zFwIX&X-Amz-Signature=2308507ca512f14f1471c923d00cce96d3019ed39a92aa1b0680556ade26809a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2UWM3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8XXoipkylp4YMaSnPnnVWmMSONvCI1Nuc3e5IFTE%2FAiEAkOp3OzPXWv0klkre2zVzHaU7w0%2Bcs%2FCXwiNwG3QzXtQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG94ijDWvCa6BBtdlSrcA9s9bcnXgDQn12lwT%2FWRhX2NZxzn%2B9oalQCNs7CnNfghslS7ho0QInZQyiOyRWI4Q%2B80J5%2FXrqiLL5bi2mmcMFH7jaBy%2BTSJ5R%2FgngdqCYMZaaWyQ547LD9cQz3qBcuS4zc5JF8vmM4YaIM2o2nb8PSL078AssIsbBGNDz74ouCuiG6upvV6lvbq1YGxEp4Qk1Z8RHY8NOYwEjOjhWlUIwmmjHQMJr5CFmxMf1H%2FaSZc2w0LzxblczrX7XdBGfjpLn46%2FhkJlvyXoqmMW9nyfv2K8S%2F8e3LlptraaxwOVlpwPsHePdQpl%2F8rnL%2BOY%2BnxCF4drO5Uy3MZdJm3M3X%2Fy%2B3w4eQuFgHQoKdsMnKSqxJYSGPuqs4IcOI5m4NUFmhfju7g%2B%2BmJOfhE6tB4B%2B21mDfTFAZocLdppXQ%2FEXLnQm9I%2FlK6WL18LXoepldfah%2BAr2sOvzY9zQFyCZaXNRixOtw%2BNX%2BIU%2BtJGM0cA2rQVxtlDs4oJM5X8Y2vXzv8zt2R4rTIlR3VXJBtAtjSV3bzD1EEPXHwHxv8jKt0fGlS4qit9PjIzkxW%2F1rgux4WF3ywTm2wGVp2X%2Fh8MskmgpJLWkFRAbPMh7DkN9G%2FBM%2BcyirnEEyf6x815ptX9rmJMKrX%2FrwGOqUBiH9%2BYc6w2v6DGVJjJtXzdNoc6vAT%2BeJRPQ7TOF5IgX3R0Jg4zURwADOTiZJ%2Fbb%2F7QayHnaqqVRcZwWW4975QBXwyoLgWXaID0T9pMrVPl3Oy7j8wjLspzstoiJZ5SRU4T9SUs2MGV%2BfyYkas70PHWiF74YBhrZD7Q9L2jKeqJPb9E%2FYAGXpa9Xe%2FnzZ%2BbeSas3EdHyBltXqGH%2BTYbP4ak93zFwIX&X-Amz-Signature=574f81d526644a7a7fdafb72ed172b02f5ca8bb3e088c4c9298b72c586da28b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2UWM3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8XXoipkylp4YMaSnPnnVWmMSONvCI1Nuc3e5IFTE%2FAiEAkOp3OzPXWv0klkre2zVzHaU7w0%2Bcs%2FCXwiNwG3QzXtQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG94ijDWvCa6BBtdlSrcA9s9bcnXgDQn12lwT%2FWRhX2NZxzn%2B9oalQCNs7CnNfghslS7ho0QInZQyiOyRWI4Q%2B80J5%2FXrqiLL5bi2mmcMFH7jaBy%2BTSJ5R%2FgngdqCYMZaaWyQ547LD9cQz3qBcuS4zc5JF8vmM4YaIM2o2nb8PSL078AssIsbBGNDz74ouCuiG6upvV6lvbq1YGxEp4Qk1Z8RHY8NOYwEjOjhWlUIwmmjHQMJr5CFmxMf1H%2FaSZc2w0LzxblczrX7XdBGfjpLn46%2FhkJlvyXoqmMW9nyfv2K8S%2F8e3LlptraaxwOVlpwPsHePdQpl%2F8rnL%2BOY%2BnxCF4drO5Uy3MZdJm3M3X%2Fy%2B3w4eQuFgHQoKdsMnKSqxJYSGPuqs4IcOI5m4NUFmhfju7g%2B%2BmJOfhE6tB4B%2B21mDfTFAZocLdppXQ%2FEXLnQm9I%2FlK6WL18LXoepldfah%2BAr2sOvzY9zQFyCZaXNRixOtw%2BNX%2BIU%2BtJGM0cA2rQVxtlDs4oJM5X8Y2vXzv8zt2R4rTIlR3VXJBtAtjSV3bzD1EEPXHwHxv8jKt0fGlS4qit9PjIzkxW%2F1rgux4WF3ywTm2wGVp2X%2Fh8MskmgpJLWkFRAbPMh7DkN9G%2FBM%2BcyirnEEyf6x815ptX9rmJMKrX%2FrwGOqUBiH9%2BYc6w2v6DGVJjJtXzdNoc6vAT%2BeJRPQ7TOF5IgX3R0Jg4zURwADOTiZJ%2Fbb%2F7QayHnaqqVRcZwWW4975QBXwyoLgWXaID0T9pMrVPl3Oy7j8wjLspzstoiJZ5SRU4T9SUs2MGV%2BfyYkas70PHWiF74YBhrZD7Q9L2jKeqJPb9E%2FYAGXpa9Xe%2FnzZ%2BbeSas3EdHyBltXqGH%2BTYbP4ak93zFwIX&X-Amz-Signature=973d8eeaacc085398df34c582d3deee6f014bb33c1a9031589e55fde25ce4701&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2UWM3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8XXoipkylp4YMaSnPnnVWmMSONvCI1Nuc3e5IFTE%2FAiEAkOp3OzPXWv0klkre2zVzHaU7w0%2Bcs%2FCXwiNwG3QzXtQqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG94ijDWvCa6BBtdlSrcA9s9bcnXgDQn12lwT%2FWRhX2NZxzn%2B9oalQCNs7CnNfghslS7ho0QInZQyiOyRWI4Q%2B80J5%2FXrqiLL5bi2mmcMFH7jaBy%2BTSJ5R%2FgngdqCYMZaaWyQ547LD9cQz3qBcuS4zc5JF8vmM4YaIM2o2nb8PSL078AssIsbBGNDz74ouCuiG6upvV6lvbq1YGxEp4Qk1Z8RHY8NOYwEjOjhWlUIwmmjHQMJr5CFmxMf1H%2FaSZc2w0LzxblczrX7XdBGfjpLn46%2FhkJlvyXoqmMW9nyfv2K8S%2F8e3LlptraaxwOVlpwPsHePdQpl%2F8rnL%2BOY%2BnxCF4drO5Uy3MZdJm3M3X%2Fy%2B3w4eQuFgHQoKdsMnKSqxJYSGPuqs4IcOI5m4NUFmhfju7g%2B%2BmJOfhE6tB4B%2B21mDfTFAZocLdppXQ%2FEXLnQm9I%2FlK6WL18LXoepldfah%2BAr2sOvzY9zQFyCZaXNRixOtw%2BNX%2BIU%2BtJGM0cA2rQVxtlDs4oJM5X8Y2vXzv8zt2R4rTIlR3VXJBtAtjSV3bzD1EEPXHwHxv8jKt0fGlS4qit9PjIzkxW%2F1rgux4WF3ywTm2wGVp2X%2Fh8MskmgpJLWkFRAbPMh7DkN9G%2FBM%2BcyirnEEyf6x815ptX9rmJMKrX%2FrwGOqUBiH9%2BYc6w2v6DGVJjJtXzdNoc6vAT%2BeJRPQ7TOF5IgX3R0Jg4zURwADOTiZJ%2Fbb%2F7QayHnaqqVRcZwWW4975QBXwyoLgWXaID0T9pMrVPl3Oy7j8wjLspzstoiJZ5SRU4T9SUs2MGV%2BfyYkas70PHWiF74YBhrZD7Q9L2jKeqJPb9E%2FYAGXpa9Xe%2FnzZ%2BbeSas3EdHyBltXqGH%2BTYbP4ak93zFwIX&X-Amz-Signature=a5e6711fd6bd1929171925b4ffd2c91bf8a2e5a5869f4fdf2cf316934039c878&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNXTC2BS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHeP7ORyOXuVz4FLAP6RG%2Bb0yWOp7HDXwfzJaSMtLbiyAiEAjAcT%2FmU%2BDezU3SUHJxIexQp3UeEqAOmf8swcEkXmLsEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDq4vZqH64DUWf1BsyrcA%2FqpvYA4t7H3BusGK64VGjWfTREHskFNLm0xckmgYm5524NnRb6oI3xnd6cgK%2BF8JXkEB%2Fce7MZ3o17Z1MTjFd%2F68HAzt1G264hOjg14L9U0BUhULXf9qvDFY1W6G5YO410PEbNAM%2FaRBYUH8eOQPmfVRm4P7ksJzltW39KQO2YYtJ09h8Wu7aERgvJDUQgQLDqYbYJJK%2BUVSg9am%2BngVOnzqTEylxceFrMI3YLYubgJnihXzxXjYc9yn7CfcSUaqx207HC3lQICFfjS85FghsP9bZt3b%2BnzFB3bRomomTHEnqbhi0x0U%2Fln9Pf5LbTFDp18J5Rjr9HI4y40Wo05FZgz2Psahh5J%2BlwmcxdQmBHu2vQrZyZz5S2p%2FKQNMt3KZO6cL7eAyOF6owjPvJbwIvD5cilknTzfataJ4zBl%2B38zjPbtTRmObXIsMssvShVqxWCtr1J9Re8eV0zQwPZwFKVcHsRkARu56HsxKKHS4lvfQauWHzUm8UXwjXwA%2BFhV%2F8%2BjiWj1omb77WTpMB0aZzwugpDq9WPCa1eWOytNwfjMwFf7KYlfkThvhk8IVt9do%2BuXvXb4a5RrhgV68JFVKEzbYibKWKJ38VwVKnBZ5%2B5RX7aMwq%2Bca56v4FKRMITk%2FrwGOqUBdcbMrgqBqWStz%2B7ydtLUeowcUcLOoyKzHwip6PnFcdFQZ6xGUfbXudmYWy8Vvh6nm8OuZDX8LDmmHsJtBdOoK27dS%2FjVadbHy2b6jK3p%2F0NkfiTEaoeaStPpQYUkt4b7pDRUXT9wKkLQUYdO9PY%2BqCHDCS05%2FaTQDKNdwKxeFQxmS0sHN5uxVkHKhwi3RmNwecPpvp4nK1SEtlAP5m5kaFKOH%2BOI&X-Amz-Signature=88fbf177d48efe6442c3eddc1d4d472cd02c0d3422bf16e6453343c481264c39&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNXTC2BS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHeP7ORyOXuVz4FLAP6RG%2Bb0yWOp7HDXwfzJaSMtLbiyAiEAjAcT%2FmU%2BDezU3SUHJxIexQp3UeEqAOmf8swcEkXmLsEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDq4vZqH64DUWf1BsyrcA%2FqpvYA4t7H3BusGK64VGjWfTREHskFNLm0xckmgYm5524NnRb6oI3xnd6cgK%2BF8JXkEB%2Fce7MZ3o17Z1MTjFd%2F68HAzt1G264hOjg14L9U0BUhULXf9qvDFY1W6G5YO410PEbNAM%2FaRBYUH8eOQPmfVRm4P7ksJzltW39KQO2YYtJ09h8Wu7aERgvJDUQgQLDqYbYJJK%2BUVSg9am%2BngVOnzqTEylxceFrMI3YLYubgJnihXzxXjYc9yn7CfcSUaqx207HC3lQICFfjS85FghsP9bZt3b%2BnzFB3bRomomTHEnqbhi0x0U%2Fln9Pf5LbTFDp18J5Rjr9HI4y40Wo05FZgz2Psahh5J%2BlwmcxdQmBHu2vQrZyZz5S2p%2FKQNMt3KZO6cL7eAyOF6owjPvJbwIvD5cilknTzfataJ4zBl%2B38zjPbtTRmObXIsMssvShVqxWCtr1J9Re8eV0zQwPZwFKVcHsRkARu56HsxKKHS4lvfQauWHzUm8UXwjXwA%2BFhV%2F8%2BjiWj1omb77WTpMB0aZzwugpDq9WPCa1eWOytNwfjMwFf7KYlfkThvhk8IVt9do%2BuXvXb4a5RrhgV68JFVKEzbYibKWKJ38VwVKnBZ5%2B5RX7aMwq%2Bca56v4FKRMITk%2FrwGOqUBdcbMrgqBqWStz%2B7ydtLUeowcUcLOoyKzHwip6PnFcdFQZ6xGUfbXudmYWy8Vvh6nm8OuZDX8LDmmHsJtBdOoK27dS%2FjVadbHy2b6jK3p%2F0NkfiTEaoeaStPpQYUkt4b7pDRUXT9wKkLQUYdO9PY%2BqCHDCS05%2FaTQDKNdwKxeFQxmS0sHN5uxVkHKhwi3RmNwecPpvp4nK1SEtlAP5m5kaFKOH%2BOI&X-Amz-Signature=08702e3ec03318cf1ae5a08e33e62fbbfc6835183587910cd229003fea6769ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNXTC2BS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHeP7ORyOXuVz4FLAP6RG%2Bb0yWOp7HDXwfzJaSMtLbiyAiEAjAcT%2FmU%2BDezU3SUHJxIexQp3UeEqAOmf8swcEkXmLsEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDq4vZqH64DUWf1BsyrcA%2FqpvYA4t7H3BusGK64VGjWfTREHskFNLm0xckmgYm5524NnRb6oI3xnd6cgK%2BF8JXkEB%2Fce7MZ3o17Z1MTjFd%2F68HAzt1G264hOjg14L9U0BUhULXf9qvDFY1W6G5YO410PEbNAM%2FaRBYUH8eOQPmfVRm4P7ksJzltW39KQO2YYtJ09h8Wu7aERgvJDUQgQLDqYbYJJK%2BUVSg9am%2BngVOnzqTEylxceFrMI3YLYubgJnihXzxXjYc9yn7CfcSUaqx207HC3lQICFfjS85FghsP9bZt3b%2BnzFB3bRomomTHEnqbhi0x0U%2Fln9Pf5LbTFDp18J5Rjr9HI4y40Wo05FZgz2Psahh5J%2BlwmcxdQmBHu2vQrZyZz5S2p%2FKQNMt3KZO6cL7eAyOF6owjPvJbwIvD5cilknTzfataJ4zBl%2B38zjPbtTRmObXIsMssvShVqxWCtr1J9Re8eV0zQwPZwFKVcHsRkARu56HsxKKHS4lvfQauWHzUm8UXwjXwA%2BFhV%2F8%2BjiWj1omb77WTpMB0aZzwugpDq9WPCa1eWOytNwfjMwFf7KYlfkThvhk8IVt9do%2BuXvXb4a5RrhgV68JFVKEzbYibKWKJ38VwVKnBZ5%2B5RX7aMwq%2Bca56v4FKRMITk%2FrwGOqUBdcbMrgqBqWStz%2B7ydtLUeowcUcLOoyKzHwip6PnFcdFQZ6xGUfbXudmYWy8Vvh6nm8OuZDX8LDmmHsJtBdOoK27dS%2FjVadbHy2b6jK3p%2F0NkfiTEaoeaStPpQYUkt4b7pDRUXT9wKkLQUYdO9PY%2BqCHDCS05%2FaTQDKNdwKxeFQxmS0sHN5uxVkHKhwi3RmNwecPpvp4nK1SEtlAP5m5kaFKOH%2BOI&X-Amz-Signature=34a005c31ac28aeadf61961cd6269268c25ce0d3723c887fd7b4334f72301f81&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNXTC2BS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHeP7ORyOXuVz4FLAP6RG%2Bb0yWOp7HDXwfzJaSMtLbiyAiEAjAcT%2FmU%2BDezU3SUHJxIexQp3UeEqAOmf8swcEkXmLsEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDq4vZqH64DUWf1BsyrcA%2FqpvYA4t7H3BusGK64VGjWfTREHskFNLm0xckmgYm5524NnRb6oI3xnd6cgK%2BF8JXkEB%2Fce7MZ3o17Z1MTjFd%2F68HAzt1G264hOjg14L9U0BUhULXf9qvDFY1W6G5YO410PEbNAM%2FaRBYUH8eOQPmfVRm4P7ksJzltW39KQO2YYtJ09h8Wu7aERgvJDUQgQLDqYbYJJK%2BUVSg9am%2BngVOnzqTEylxceFrMI3YLYubgJnihXzxXjYc9yn7CfcSUaqx207HC3lQICFfjS85FghsP9bZt3b%2BnzFB3bRomomTHEnqbhi0x0U%2Fln9Pf5LbTFDp18J5Rjr9HI4y40Wo05FZgz2Psahh5J%2BlwmcxdQmBHu2vQrZyZz5S2p%2FKQNMt3KZO6cL7eAyOF6owjPvJbwIvD5cilknTzfataJ4zBl%2B38zjPbtTRmObXIsMssvShVqxWCtr1J9Re8eV0zQwPZwFKVcHsRkARu56HsxKKHS4lvfQauWHzUm8UXwjXwA%2BFhV%2F8%2BjiWj1omb77WTpMB0aZzwugpDq9WPCa1eWOytNwfjMwFf7KYlfkThvhk8IVt9do%2BuXvXb4a5RrhgV68JFVKEzbYibKWKJ38VwVKnBZ5%2B5RX7aMwq%2Bca56v4FKRMITk%2FrwGOqUBdcbMrgqBqWStz%2B7ydtLUeowcUcLOoyKzHwip6PnFcdFQZ6xGUfbXudmYWy8Vvh6nm8OuZDX8LDmmHsJtBdOoK27dS%2FjVadbHy2b6jK3p%2F0NkfiTEaoeaStPpQYUkt4b7pDRUXT9wKkLQUYdO9PY%2BqCHDCS05%2FaTQDKNdwKxeFQxmS0sHN5uxVkHKhwi3RmNwecPpvp4nK1SEtlAP5m5kaFKOH%2BOI&X-Amz-Signature=4bd9023145c2f373bb685a4a028bcc46333339661b8ca1f633b55b8d7e6b97f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663OIKBZW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGrNGjweM8JEutsvU1CW4k%2BuRDawl0t4ju1m8gcitIu3AiBxGAVrh7krO%2Fp9cfqWO5CT%2F3MVCG4FbwkrJ8otVGMOWCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkLAfCGkdN4xIuVMYKtwD3rPRtsRfwWjPfuSKjtymygsU9T17VnSlFMUAA8jcsC%2BoucREexW7pPIvw%2Bdx3DZZUh4eoCqxcgYn3MLZZqZF0xznaNpMDppBWB2SUu9wyLSB%2Fcoi062O99ShHpi5qC3JTUF071bKM5vekBG0tL5MhFYi%2FbQ9bepMURmgDp1tK90CFx4Bv2SPZM72Abh52%2BGQUPuu5%2B%2F%2BCFUbIMmFGvQFaZQtnuy6TjUxtQh3SqzHTJgGVyRBye3CkUtwEZ4ggo9UQT3IUCJeWRPPXjrN3UO8hS1RFmZKaxHllhCVqAQ9euTQM7O%2FU2EIlPawRmIqGhdYlRXJWTZdWA7jhyW3jQOkU1VKaKRrUeMcpSEWbPlZQlKWymqDWBwjP75TDOifuXfBWx8wBlZLqD%2FL9v3lpaw64XKbjNTlMjYx5QseFstuGidn7QM6bTitUxZAJOn%2BiKXc6J1hm1c0qmF18p4YarCmxna%2B%2FkliNYTQcXeYWm0TjCMGWfIxxojPpeB6VI6hxIlFCajjRi56Mwpp82araMDpItPUTeRq1qbe2uBPiMBdTUD%2Bx5z9BSHpGhBto5t7K05CTELihDatgIOygneAhD%2FgHzeC3l2Pnt1RLwEun7eLETTPK8BUAETSYMkbB2YwpeX%2BvAY6pgHdaxdPaaY0UGUhjw2Hyb6MzVtErb98FHlpPH8MC5ty8jsLivplBsNm2Vrxn3OMu5lXDZ%2FyPPvTE1909ZMBHbVPkDCl%2F9EsHYt53EK1Hs07ADBItNcWFt5iMJXJpn3mysEQPtQnw5nklewN6gQxtplPdZY5OX5zT%2BiSqsQvPHEq9rv%2FcHiXPV90XNdXYkCpuA9%2BqrCfXuJgP1NJXhQ7CbysEhPKJshD&X-Amz-Signature=f31577d13716cec7ff2da2f83d1fcd94ee38de6a58d01d6d443a893feea0f015&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663OIKBZW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGrNGjweM8JEutsvU1CW4k%2BuRDawl0t4ju1m8gcitIu3AiBxGAVrh7krO%2Fp9cfqWO5CT%2F3MVCG4FbwkrJ8otVGMOWCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkLAfCGkdN4xIuVMYKtwD3rPRtsRfwWjPfuSKjtymygsU9T17VnSlFMUAA8jcsC%2BoucREexW7pPIvw%2Bdx3DZZUh4eoCqxcgYn3MLZZqZF0xznaNpMDppBWB2SUu9wyLSB%2Fcoi062O99ShHpi5qC3JTUF071bKM5vekBG0tL5MhFYi%2FbQ9bepMURmgDp1tK90CFx4Bv2SPZM72Abh52%2BGQUPuu5%2B%2F%2BCFUbIMmFGvQFaZQtnuy6TjUxtQh3SqzHTJgGVyRBye3CkUtwEZ4ggo9UQT3IUCJeWRPPXjrN3UO8hS1RFmZKaxHllhCVqAQ9euTQM7O%2FU2EIlPawRmIqGhdYlRXJWTZdWA7jhyW3jQOkU1VKaKRrUeMcpSEWbPlZQlKWymqDWBwjP75TDOifuXfBWx8wBlZLqD%2FL9v3lpaw64XKbjNTlMjYx5QseFstuGidn7QM6bTitUxZAJOn%2BiKXc6J1hm1c0qmF18p4YarCmxna%2B%2FkliNYTQcXeYWm0TjCMGWfIxxojPpeB6VI6hxIlFCajjRi56Mwpp82araMDpItPUTeRq1qbe2uBPiMBdTUD%2Bx5z9BSHpGhBto5t7K05CTELihDatgIOygneAhD%2FgHzeC3l2Pnt1RLwEun7eLETTPK8BUAETSYMkbB2YwpeX%2BvAY6pgHdaxdPaaY0UGUhjw2Hyb6MzVtErb98FHlpPH8MC5ty8jsLivplBsNm2Vrxn3OMu5lXDZ%2FyPPvTE1909ZMBHbVPkDCl%2F9EsHYt53EK1Hs07ADBItNcWFt5iMJXJpn3mysEQPtQnw5nklewN6gQxtplPdZY5OX5zT%2BiSqsQvPHEq9rv%2FcHiXPV90XNdXYkCpuA9%2BqrCfXuJgP1NJXhQ7CbysEhPKJshD&X-Amz-Signature=1afb88d9628c578076b035cbfab2d1e33e407abefa3dd63818244eb59d5b0330&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663OIKBZW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGrNGjweM8JEutsvU1CW4k%2BuRDawl0t4ju1m8gcitIu3AiBxGAVrh7krO%2Fp9cfqWO5CT%2F3MVCG4FbwkrJ8otVGMOWCqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkLAfCGkdN4xIuVMYKtwD3rPRtsRfwWjPfuSKjtymygsU9T17VnSlFMUAA8jcsC%2BoucREexW7pPIvw%2Bdx3DZZUh4eoCqxcgYn3MLZZqZF0xznaNpMDppBWB2SUu9wyLSB%2Fcoi062O99ShHpi5qC3JTUF071bKM5vekBG0tL5MhFYi%2FbQ9bepMURmgDp1tK90CFx4Bv2SPZM72Abh52%2BGQUPuu5%2B%2F%2BCFUbIMmFGvQFaZQtnuy6TjUxtQh3SqzHTJgGVyRBye3CkUtwEZ4ggo9UQT3IUCJeWRPPXjrN3UO8hS1RFmZKaxHllhCVqAQ9euTQM7O%2FU2EIlPawRmIqGhdYlRXJWTZdWA7jhyW3jQOkU1VKaKRrUeMcpSEWbPlZQlKWymqDWBwjP75TDOifuXfBWx8wBlZLqD%2FL9v3lpaw64XKbjNTlMjYx5QseFstuGidn7QM6bTitUxZAJOn%2BiKXc6J1hm1c0qmF18p4YarCmxna%2B%2FkliNYTQcXeYWm0TjCMGWfIxxojPpeB6VI6hxIlFCajjRi56Mwpp82araMDpItPUTeRq1qbe2uBPiMBdTUD%2Bx5z9BSHpGhBto5t7K05CTELihDatgIOygneAhD%2FgHzeC3l2Pnt1RLwEun7eLETTPK8BUAETSYMkbB2YwpeX%2BvAY6pgHdaxdPaaY0UGUhjw2Hyb6MzVtErb98FHlpPH8MC5ty8jsLivplBsNm2Vrxn3OMu5lXDZ%2FyPPvTE1909ZMBHbVPkDCl%2F9EsHYt53EK1Hs07ADBItNcWFt5iMJXJpn3mysEQPtQnw5nklewN6gQxtplPdZY5OX5zT%2BiSqsQvPHEq9rv%2FcHiXPV90XNdXYkCpuA9%2BqrCfXuJgP1NJXhQ7CbysEhPKJshD&X-Amz-Signature=30df064099c2670782ec356dd31aa7b6a28437b9491ddc3226a48ec39fbb9406&X-Amz-SignedHeaders=host&x-id=GetObject)
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

