

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTYENOLL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDge2Ahez%2FfIfiqUg%2Br2YJsvgbRQltu7Shm%2Fzfe9ZfE%2BwIgG6SCCq8YbKo3nBFd7PN6ObfGVTlpEbaK%2BMkrurj731MqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgCLhQXXYEpQzT90ircA%2BD898JpLUO6yH1cEEMb%2BKSg5BJYKuT5VzW%2Bfao3qwLZTl3Ie3DCa8KG9P3GqFbqd5MuEUjFsSIC9nO%2F1fBIRdMWuwhaZk18Awc1%2B4sHZ8G31KJGjVsH%2Bwxi7l8Pi9nT%2Fg4F3G%2BMWs7IZ%2Fa9MbrzQOHKukzkcdLp%2FnxfN0gl8lCRbo0LnRTrBZDyx5mbJXJTRIRKKaFyuVKf7O1NTqndVKrd20KE1w9AkYjeZNJLZB0X%2B6gBKnksbnt1YqAMzjfBdJMT%2FecRCI%2BtuSt%2BFNZJJLQdnjZkLgHAKt9uqSH5%2FnO4dEDBr3I2PyvTFmICXAvohUsYNwIeezhcE9r8dJq0XXq9lcaBxKfV9n4eCk6lCJqAM%2FDKlrZSgH2I23CdJKL9AqdSR8d7CVg3YG0pQTfwBB9jGRrC9tKFVU3kir6Ec28YHGUuJ7eZSX7%2F%2BngxFxeV006nl7p4udDdeVqzYV5i9i1Nn%2FxRKp89ReCQ367G3vCNBbG60vCqelog9E27DhdDgCdVZvv2etYjHQopbTTyKRPyZiRh3aH338Qc8%2BL1EDv3%2BMxelcTdLYDK5DskEe%2FqQW2NHwiDTba8qtdoM%2FKx7ZkAiXEflZBR2dp8THxM10aa5xDrn6BgbLCwkEvpMLnk%2F7wGOqUB%2Fe8QyItLMW%2Bun4JyCLwoVSbxkVqL7Kw5cXD2yRTKnTE3uo4qkHATTf2l9PNeJbIs7x2PT%2BA6hNV5bWsizbY%2Fy2qn91R8Ep8cTCVAmYSvo3hkkdLLh1Np3VpdEAHyQBIoONaPfdnHsLHlRJsD9lu%2FZO%2Bs2T%2BSlscc%2FmYpE0w7tJ%2BtznR4Puj1gutagmwdBkdaWVu71qX7%2BcNfWioEM53LYrtTnZXz&X-Amz-Signature=de2f881ada841fe486c8bf196f02cf4b5ecba68782d452ac1556ff2d0c8add9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTYENOLL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDge2Ahez%2FfIfiqUg%2Br2YJsvgbRQltu7Shm%2Fzfe9ZfE%2BwIgG6SCCq8YbKo3nBFd7PN6ObfGVTlpEbaK%2BMkrurj731MqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgCLhQXXYEpQzT90ircA%2BD898JpLUO6yH1cEEMb%2BKSg5BJYKuT5VzW%2Bfao3qwLZTl3Ie3DCa8KG9P3GqFbqd5MuEUjFsSIC9nO%2F1fBIRdMWuwhaZk18Awc1%2B4sHZ8G31KJGjVsH%2Bwxi7l8Pi9nT%2Fg4F3G%2BMWs7IZ%2Fa9MbrzQOHKukzkcdLp%2FnxfN0gl8lCRbo0LnRTrBZDyx5mbJXJTRIRKKaFyuVKf7O1NTqndVKrd20KE1w9AkYjeZNJLZB0X%2B6gBKnksbnt1YqAMzjfBdJMT%2FecRCI%2BtuSt%2BFNZJJLQdnjZkLgHAKt9uqSH5%2FnO4dEDBr3I2PyvTFmICXAvohUsYNwIeezhcE9r8dJq0XXq9lcaBxKfV9n4eCk6lCJqAM%2FDKlrZSgH2I23CdJKL9AqdSR8d7CVg3YG0pQTfwBB9jGRrC9tKFVU3kir6Ec28YHGUuJ7eZSX7%2F%2BngxFxeV006nl7p4udDdeVqzYV5i9i1Nn%2FxRKp89ReCQ367G3vCNBbG60vCqelog9E27DhdDgCdVZvv2etYjHQopbTTyKRPyZiRh3aH338Qc8%2BL1EDv3%2BMxelcTdLYDK5DskEe%2FqQW2NHwiDTba8qtdoM%2FKx7ZkAiXEflZBR2dp8THxM10aa5xDrn6BgbLCwkEvpMLnk%2F7wGOqUB%2Fe8QyItLMW%2Bun4JyCLwoVSbxkVqL7Kw5cXD2yRTKnTE3uo4qkHATTf2l9PNeJbIs7x2PT%2BA6hNV5bWsizbY%2Fy2qn91R8Ep8cTCVAmYSvo3hkkdLLh1Np3VpdEAHyQBIoONaPfdnHsLHlRJsD9lu%2FZO%2Bs2T%2BSlscc%2FmYpE0w7tJ%2BtznR4Puj1gutagmwdBkdaWVu71qX7%2BcNfWioEM53LYrtTnZXz&X-Amz-Signature=8df8caecae3ce7ebfcda9ddb35abee99d8e696fbf923e621ef5364ad74c91235&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTYENOLL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDge2Ahez%2FfIfiqUg%2Br2YJsvgbRQltu7Shm%2Fzfe9ZfE%2BwIgG6SCCq8YbKo3nBFd7PN6ObfGVTlpEbaK%2BMkrurj731MqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgCLhQXXYEpQzT90ircA%2BD898JpLUO6yH1cEEMb%2BKSg5BJYKuT5VzW%2Bfao3qwLZTl3Ie3DCa8KG9P3GqFbqd5MuEUjFsSIC9nO%2F1fBIRdMWuwhaZk18Awc1%2B4sHZ8G31KJGjVsH%2Bwxi7l8Pi9nT%2Fg4F3G%2BMWs7IZ%2Fa9MbrzQOHKukzkcdLp%2FnxfN0gl8lCRbo0LnRTrBZDyx5mbJXJTRIRKKaFyuVKf7O1NTqndVKrd20KE1w9AkYjeZNJLZB0X%2B6gBKnksbnt1YqAMzjfBdJMT%2FecRCI%2BtuSt%2BFNZJJLQdnjZkLgHAKt9uqSH5%2FnO4dEDBr3I2PyvTFmICXAvohUsYNwIeezhcE9r8dJq0XXq9lcaBxKfV9n4eCk6lCJqAM%2FDKlrZSgH2I23CdJKL9AqdSR8d7CVg3YG0pQTfwBB9jGRrC9tKFVU3kir6Ec28YHGUuJ7eZSX7%2F%2BngxFxeV006nl7p4udDdeVqzYV5i9i1Nn%2FxRKp89ReCQ367G3vCNBbG60vCqelog9E27DhdDgCdVZvv2etYjHQopbTTyKRPyZiRh3aH338Qc8%2BL1EDv3%2BMxelcTdLYDK5DskEe%2FqQW2NHwiDTba8qtdoM%2FKx7ZkAiXEflZBR2dp8THxM10aa5xDrn6BgbLCwkEvpMLnk%2F7wGOqUB%2Fe8QyItLMW%2Bun4JyCLwoVSbxkVqL7Kw5cXD2yRTKnTE3uo4qkHATTf2l9PNeJbIs7x2PT%2BA6hNV5bWsizbY%2Fy2qn91R8Ep8cTCVAmYSvo3hkkdLLh1Np3VpdEAHyQBIoONaPfdnHsLHlRJsD9lu%2FZO%2Bs2T%2BSlscc%2FmYpE0w7tJ%2BtznR4Puj1gutagmwdBkdaWVu71qX7%2BcNfWioEM53LYrtTnZXz&X-Amz-Signature=f14e1f324509d478c4cd35a522abb6d9e81b0e7f0742c6a6c2116def6ce6ed43&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTYENOLL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDge2Ahez%2FfIfiqUg%2Br2YJsvgbRQltu7Shm%2Fzfe9ZfE%2BwIgG6SCCq8YbKo3nBFd7PN6ObfGVTlpEbaK%2BMkrurj731MqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgCLhQXXYEpQzT90ircA%2BD898JpLUO6yH1cEEMb%2BKSg5BJYKuT5VzW%2Bfao3qwLZTl3Ie3DCa8KG9P3GqFbqd5MuEUjFsSIC9nO%2F1fBIRdMWuwhaZk18Awc1%2B4sHZ8G31KJGjVsH%2Bwxi7l8Pi9nT%2Fg4F3G%2BMWs7IZ%2Fa9MbrzQOHKukzkcdLp%2FnxfN0gl8lCRbo0LnRTrBZDyx5mbJXJTRIRKKaFyuVKf7O1NTqndVKrd20KE1w9AkYjeZNJLZB0X%2B6gBKnksbnt1YqAMzjfBdJMT%2FecRCI%2BtuSt%2BFNZJJLQdnjZkLgHAKt9uqSH5%2FnO4dEDBr3I2PyvTFmICXAvohUsYNwIeezhcE9r8dJq0XXq9lcaBxKfV9n4eCk6lCJqAM%2FDKlrZSgH2I23CdJKL9AqdSR8d7CVg3YG0pQTfwBB9jGRrC9tKFVU3kir6Ec28YHGUuJ7eZSX7%2F%2BngxFxeV006nl7p4udDdeVqzYV5i9i1Nn%2FxRKp89ReCQ367G3vCNBbG60vCqelog9E27DhdDgCdVZvv2etYjHQopbTTyKRPyZiRh3aH338Qc8%2BL1EDv3%2BMxelcTdLYDK5DskEe%2FqQW2NHwiDTba8qtdoM%2FKx7ZkAiXEflZBR2dp8THxM10aa5xDrn6BgbLCwkEvpMLnk%2F7wGOqUB%2Fe8QyItLMW%2Bun4JyCLwoVSbxkVqL7Kw5cXD2yRTKnTE3uo4qkHATTf2l9PNeJbIs7x2PT%2BA6hNV5bWsizbY%2Fy2qn91R8Ep8cTCVAmYSvo3hkkdLLh1Np3VpdEAHyQBIoONaPfdnHsLHlRJsD9lu%2FZO%2Bs2T%2BSlscc%2FmYpE0w7tJ%2BtznR4Puj1gutagmwdBkdaWVu71qX7%2BcNfWioEM53LYrtTnZXz&X-Amz-Signature=6125059c8be0c23fcf4e5795ef8c2524300eb7003ddfe1f7596cfc91a71cd292&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTYENOLL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDge2Ahez%2FfIfiqUg%2Br2YJsvgbRQltu7Shm%2Fzfe9ZfE%2BwIgG6SCCq8YbKo3nBFd7PN6ObfGVTlpEbaK%2BMkrurj731MqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgCLhQXXYEpQzT90ircA%2BD898JpLUO6yH1cEEMb%2BKSg5BJYKuT5VzW%2Bfao3qwLZTl3Ie3DCa8KG9P3GqFbqd5MuEUjFsSIC9nO%2F1fBIRdMWuwhaZk18Awc1%2B4sHZ8G31KJGjVsH%2Bwxi7l8Pi9nT%2Fg4F3G%2BMWs7IZ%2Fa9MbrzQOHKukzkcdLp%2FnxfN0gl8lCRbo0LnRTrBZDyx5mbJXJTRIRKKaFyuVKf7O1NTqndVKrd20KE1w9AkYjeZNJLZB0X%2B6gBKnksbnt1YqAMzjfBdJMT%2FecRCI%2BtuSt%2BFNZJJLQdnjZkLgHAKt9uqSH5%2FnO4dEDBr3I2PyvTFmICXAvohUsYNwIeezhcE9r8dJq0XXq9lcaBxKfV9n4eCk6lCJqAM%2FDKlrZSgH2I23CdJKL9AqdSR8d7CVg3YG0pQTfwBB9jGRrC9tKFVU3kir6Ec28YHGUuJ7eZSX7%2F%2BngxFxeV006nl7p4udDdeVqzYV5i9i1Nn%2FxRKp89ReCQ367G3vCNBbG60vCqelog9E27DhdDgCdVZvv2etYjHQopbTTyKRPyZiRh3aH338Qc8%2BL1EDv3%2BMxelcTdLYDK5DskEe%2FqQW2NHwiDTba8qtdoM%2FKx7ZkAiXEflZBR2dp8THxM10aa5xDrn6BgbLCwkEvpMLnk%2F7wGOqUB%2Fe8QyItLMW%2Bun4JyCLwoVSbxkVqL7Kw5cXD2yRTKnTE3uo4qkHATTf2l9PNeJbIs7x2PT%2BA6hNV5bWsizbY%2Fy2qn91R8Ep8cTCVAmYSvo3hkkdLLh1Np3VpdEAHyQBIoONaPfdnHsLHlRJsD9lu%2FZO%2Bs2T%2BSlscc%2FmYpE0w7tJ%2BtznR4Puj1gutagmwdBkdaWVu71qX7%2BcNfWioEM53LYrtTnZXz&X-Amz-Signature=c287e6df00f7bdf2773ee60ce7782e26c85b66584b54aa24162bc70011de7a50&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTYENOLL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDge2Ahez%2FfIfiqUg%2Br2YJsvgbRQltu7Shm%2Fzfe9ZfE%2BwIgG6SCCq8YbKo3nBFd7PN6ObfGVTlpEbaK%2BMkrurj731MqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgCLhQXXYEpQzT90ircA%2BD898JpLUO6yH1cEEMb%2BKSg5BJYKuT5VzW%2Bfao3qwLZTl3Ie3DCa8KG9P3GqFbqd5MuEUjFsSIC9nO%2F1fBIRdMWuwhaZk18Awc1%2B4sHZ8G31KJGjVsH%2Bwxi7l8Pi9nT%2Fg4F3G%2BMWs7IZ%2Fa9MbrzQOHKukzkcdLp%2FnxfN0gl8lCRbo0LnRTrBZDyx5mbJXJTRIRKKaFyuVKf7O1NTqndVKrd20KE1w9AkYjeZNJLZB0X%2B6gBKnksbnt1YqAMzjfBdJMT%2FecRCI%2BtuSt%2BFNZJJLQdnjZkLgHAKt9uqSH5%2FnO4dEDBr3I2PyvTFmICXAvohUsYNwIeezhcE9r8dJq0XXq9lcaBxKfV9n4eCk6lCJqAM%2FDKlrZSgH2I23CdJKL9AqdSR8d7CVg3YG0pQTfwBB9jGRrC9tKFVU3kir6Ec28YHGUuJ7eZSX7%2F%2BngxFxeV006nl7p4udDdeVqzYV5i9i1Nn%2FxRKp89ReCQ367G3vCNBbG60vCqelog9E27DhdDgCdVZvv2etYjHQopbTTyKRPyZiRh3aH338Qc8%2BL1EDv3%2BMxelcTdLYDK5DskEe%2FqQW2NHwiDTba8qtdoM%2FKx7ZkAiXEflZBR2dp8THxM10aa5xDrn6BgbLCwkEvpMLnk%2F7wGOqUB%2Fe8QyItLMW%2Bun4JyCLwoVSbxkVqL7Kw5cXD2yRTKnTE3uo4qkHATTf2l9PNeJbIs7x2PT%2BA6hNV5bWsizbY%2Fy2qn91R8Ep8cTCVAmYSvo3hkkdLLh1Np3VpdEAHyQBIoONaPfdnHsLHlRJsD9lu%2FZO%2Bs2T%2BSlscc%2FmYpE0w7tJ%2BtznR4Puj1gutagmwdBkdaWVu71qX7%2BcNfWioEM53LYrtTnZXz&X-Amz-Signature=b99e0839f7eeed08a3e39a2c666b400d970e65e0f60ccfa75c7f1964cf5ad8a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTYENOLL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDge2Ahez%2FfIfiqUg%2Br2YJsvgbRQltu7Shm%2Fzfe9ZfE%2BwIgG6SCCq8YbKo3nBFd7PN6ObfGVTlpEbaK%2BMkrurj731MqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgCLhQXXYEpQzT90ircA%2BD898JpLUO6yH1cEEMb%2BKSg5BJYKuT5VzW%2Bfao3qwLZTl3Ie3DCa8KG9P3GqFbqd5MuEUjFsSIC9nO%2F1fBIRdMWuwhaZk18Awc1%2B4sHZ8G31KJGjVsH%2Bwxi7l8Pi9nT%2Fg4F3G%2BMWs7IZ%2Fa9MbrzQOHKukzkcdLp%2FnxfN0gl8lCRbo0LnRTrBZDyx5mbJXJTRIRKKaFyuVKf7O1NTqndVKrd20KE1w9AkYjeZNJLZB0X%2B6gBKnksbnt1YqAMzjfBdJMT%2FecRCI%2BtuSt%2BFNZJJLQdnjZkLgHAKt9uqSH5%2FnO4dEDBr3I2PyvTFmICXAvohUsYNwIeezhcE9r8dJq0XXq9lcaBxKfV9n4eCk6lCJqAM%2FDKlrZSgH2I23CdJKL9AqdSR8d7CVg3YG0pQTfwBB9jGRrC9tKFVU3kir6Ec28YHGUuJ7eZSX7%2F%2BngxFxeV006nl7p4udDdeVqzYV5i9i1Nn%2FxRKp89ReCQ367G3vCNBbG60vCqelog9E27DhdDgCdVZvv2etYjHQopbTTyKRPyZiRh3aH338Qc8%2BL1EDv3%2BMxelcTdLYDK5DskEe%2FqQW2NHwiDTba8qtdoM%2FKx7ZkAiXEflZBR2dp8THxM10aa5xDrn6BgbLCwkEvpMLnk%2F7wGOqUB%2Fe8QyItLMW%2Bun4JyCLwoVSbxkVqL7Kw5cXD2yRTKnTE3uo4qkHATTf2l9PNeJbIs7x2PT%2BA6hNV5bWsizbY%2Fy2qn91R8Ep8cTCVAmYSvo3hkkdLLh1Np3VpdEAHyQBIoONaPfdnHsLHlRJsD9lu%2FZO%2Bs2T%2BSlscc%2FmYpE0w7tJ%2BtznR4Puj1gutagmwdBkdaWVu71qX7%2BcNfWioEM53LYrtTnZXz&X-Amz-Signature=aa83b66e1e0fa4c35d7d428d8489b7376de6edb3cc583ea1b6bb222182e62b14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTYENOLL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDge2Ahez%2FfIfiqUg%2Br2YJsvgbRQltu7Shm%2Fzfe9ZfE%2BwIgG6SCCq8YbKo3nBFd7PN6ObfGVTlpEbaK%2BMkrurj731MqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgCLhQXXYEpQzT90ircA%2BD898JpLUO6yH1cEEMb%2BKSg5BJYKuT5VzW%2Bfao3qwLZTl3Ie3DCa8KG9P3GqFbqd5MuEUjFsSIC9nO%2F1fBIRdMWuwhaZk18Awc1%2B4sHZ8G31KJGjVsH%2Bwxi7l8Pi9nT%2Fg4F3G%2BMWs7IZ%2Fa9MbrzQOHKukzkcdLp%2FnxfN0gl8lCRbo0LnRTrBZDyx5mbJXJTRIRKKaFyuVKf7O1NTqndVKrd20KE1w9AkYjeZNJLZB0X%2B6gBKnksbnt1YqAMzjfBdJMT%2FecRCI%2BtuSt%2BFNZJJLQdnjZkLgHAKt9uqSH5%2FnO4dEDBr3I2PyvTFmICXAvohUsYNwIeezhcE9r8dJq0XXq9lcaBxKfV9n4eCk6lCJqAM%2FDKlrZSgH2I23CdJKL9AqdSR8d7CVg3YG0pQTfwBB9jGRrC9tKFVU3kir6Ec28YHGUuJ7eZSX7%2F%2BngxFxeV006nl7p4udDdeVqzYV5i9i1Nn%2FxRKp89ReCQ367G3vCNBbG60vCqelog9E27DhdDgCdVZvv2etYjHQopbTTyKRPyZiRh3aH338Qc8%2BL1EDv3%2BMxelcTdLYDK5DskEe%2FqQW2NHwiDTba8qtdoM%2FKx7ZkAiXEflZBR2dp8THxM10aa5xDrn6BgbLCwkEvpMLnk%2F7wGOqUB%2Fe8QyItLMW%2Bun4JyCLwoVSbxkVqL7Kw5cXD2yRTKnTE3uo4qkHATTf2l9PNeJbIs7x2PT%2BA6hNV5bWsizbY%2Fy2qn91R8Ep8cTCVAmYSvo3hkkdLLh1Np3VpdEAHyQBIoONaPfdnHsLHlRJsD9lu%2FZO%2Bs2T%2BSlscc%2FmYpE0w7tJ%2BtznR4Puj1gutagmwdBkdaWVu71qX7%2BcNfWioEM53LYrtTnZXz&X-Amz-Signature=d8fea21f8569397f0d5a5c26d16a1c54ddea12b88495b4dda6d414c820a100d3&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTYENOLL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDge2Ahez%2FfIfiqUg%2Br2YJsvgbRQltu7Shm%2Fzfe9ZfE%2BwIgG6SCCq8YbKo3nBFd7PN6ObfGVTlpEbaK%2BMkrurj731MqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgCLhQXXYEpQzT90ircA%2BD898JpLUO6yH1cEEMb%2BKSg5BJYKuT5VzW%2Bfao3qwLZTl3Ie3DCa8KG9P3GqFbqd5MuEUjFsSIC9nO%2F1fBIRdMWuwhaZk18Awc1%2B4sHZ8G31KJGjVsH%2Bwxi7l8Pi9nT%2Fg4F3G%2BMWs7IZ%2Fa9MbrzQOHKukzkcdLp%2FnxfN0gl8lCRbo0LnRTrBZDyx5mbJXJTRIRKKaFyuVKf7O1NTqndVKrd20KE1w9AkYjeZNJLZB0X%2B6gBKnksbnt1YqAMzjfBdJMT%2FecRCI%2BtuSt%2BFNZJJLQdnjZkLgHAKt9uqSH5%2FnO4dEDBr3I2PyvTFmICXAvohUsYNwIeezhcE9r8dJq0XXq9lcaBxKfV9n4eCk6lCJqAM%2FDKlrZSgH2I23CdJKL9AqdSR8d7CVg3YG0pQTfwBB9jGRrC9tKFVU3kir6Ec28YHGUuJ7eZSX7%2F%2BngxFxeV006nl7p4udDdeVqzYV5i9i1Nn%2FxRKp89ReCQ367G3vCNBbG60vCqelog9E27DhdDgCdVZvv2etYjHQopbTTyKRPyZiRh3aH338Qc8%2BL1EDv3%2BMxelcTdLYDK5DskEe%2FqQW2NHwiDTba8qtdoM%2FKx7ZkAiXEflZBR2dp8THxM10aa5xDrn6BgbLCwkEvpMLnk%2F7wGOqUB%2Fe8QyItLMW%2Bun4JyCLwoVSbxkVqL7Kw5cXD2yRTKnTE3uo4qkHATTf2l9PNeJbIs7x2PT%2BA6hNV5bWsizbY%2Fy2qn91R8Ep8cTCVAmYSvo3hkkdLLh1Np3VpdEAHyQBIoONaPfdnHsLHlRJsD9lu%2FZO%2Bs2T%2BSlscc%2FmYpE0w7tJ%2BtznR4Puj1gutagmwdBkdaWVu71qX7%2BcNfWioEM53LYrtTnZXz&X-Amz-Signature=bb31e4d33be0eafd579dadbbf2a6aa4fd0188f77cb7614e30c17ff8d16f78886&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTYENOLL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDge2Ahez%2FfIfiqUg%2Br2YJsvgbRQltu7Shm%2Fzfe9ZfE%2BwIgG6SCCq8YbKo3nBFd7PN6ObfGVTlpEbaK%2BMkrurj731MqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgCLhQXXYEpQzT90ircA%2BD898JpLUO6yH1cEEMb%2BKSg5BJYKuT5VzW%2Bfao3qwLZTl3Ie3DCa8KG9P3GqFbqd5MuEUjFsSIC9nO%2F1fBIRdMWuwhaZk18Awc1%2B4sHZ8G31KJGjVsH%2Bwxi7l8Pi9nT%2Fg4F3G%2BMWs7IZ%2Fa9MbrzQOHKukzkcdLp%2FnxfN0gl8lCRbo0LnRTrBZDyx5mbJXJTRIRKKaFyuVKf7O1NTqndVKrd20KE1w9AkYjeZNJLZB0X%2B6gBKnksbnt1YqAMzjfBdJMT%2FecRCI%2BtuSt%2BFNZJJLQdnjZkLgHAKt9uqSH5%2FnO4dEDBr3I2PyvTFmICXAvohUsYNwIeezhcE9r8dJq0XXq9lcaBxKfV9n4eCk6lCJqAM%2FDKlrZSgH2I23CdJKL9AqdSR8d7CVg3YG0pQTfwBB9jGRrC9tKFVU3kir6Ec28YHGUuJ7eZSX7%2F%2BngxFxeV006nl7p4udDdeVqzYV5i9i1Nn%2FxRKp89ReCQ367G3vCNBbG60vCqelog9E27DhdDgCdVZvv2etYjHQopbTTyKRPyZiRh3aH338Qc8%2BL1EDv3%2BMxelcTdLYDK5DskEe%2FqQW2NHwiDTba8qtdoM%2FKx7ZkAiXEflZBR2dp8THxM10aa5xDrn6BgbLCwkEvpMLnk%2F7wGOqUB%2Fe8QyItLMW%2Bun4JyCLwoVSbxkVqL7Kw5cXD2yRTKnTE3uo4qkHATTf2l9PNeJbIs7x2PT%2BA6hNV5bWsizbY%2Fy2qn91R8Ep8cTCVAmYSvo3hkkdLLh1Np3VpdEAHyQBIoONaPfdnHsLHlRJsD9lu%2FZO%2Bs2T%2BSlscc%2FmYpE0w7tJ%2BtznR4Puj1gutagmwdBkdaWVu71qX7%2BcNfWioEM53LYrtTnZXz&X-Amz-Signature=9cd9eef77dadd934211ce696c1af3db93a38d495068ba3ef7f5a560d3204e6cc&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTYENOLL%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDge2Ahez%2FfIfiqUg%2Br2YJsvgbRQltu7Shm%2Fzfe9ZfE%2BwIgG6SCCq8YbKo3nBFd7PN6ObfGVTlpEbaK%2BMkrurj731MqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKgCLhQXXYEpQzT90ircA%2BD898JpLUO6yH1cEEMb%2BKSg5BJYKuT5VzW%2Bfao3qwLZTl3Ie3DCa8KG9P3GqFbqd5MuEUjFsSIC9nO%2F1fBIRdMWuwhaZk18Awc1%2B4sHZ8G31KJGjVsH%2Bwxi7l8Pi9nT%2Fg4F3G%2BMWs7IZ%2Fa9MbrzQOHKukzkcdLp%2FnxfN0gl8lCRbo0LnRTrBZDyx5mbJXJTRIRKKaFyuVKf7O1NTqndVKrd20KE1w9AkYjeZNJLZB0X%2B6gBKnksbnt1YqAMzjfBdJMT%2FecRCI%2BtuSt%2BFNZJJLQdnjZkLgHAKt9uqSH5%2FnO4dEDBr3I2PyvTFmICXAvohUsYNwIeezhcE9r8dJq0XXq9lcaBxKfV9n4eCk6lCJqAM%2FDKlrZSgH2I23CdJKL9AqdSR8d7CVg3YG0pQTfwBB9jGRrC9tKFVU3kir6Ec28YHGUuJ7eZSX7%2F%2BngxFxeV006nl7p4udDdeVqzYV5i9i1Nn%2FxRKp89ReCQ367G3vCNBbG60vCqelog9E27DhdDgCdVZvv2etYjHQopbTTyKRPyZiRh3aH338Qc8%2BL1EDv3%2BMxelcTdLYDK5DskEe%2FqQW2NHwiDTba8qtdoM%2FKx7ZkAiXEflZBR2dp8THxM10aa5xDrn6BgbLCwkEvpMLnk%2F7wGOqUB%2Fe8QyItLMW%2Bun4JyCLwoVSbxkVqL7Kw5cXD2yRTKnTE3uo4qkHATTf2l9PNeJbIs7x2PT%2BA6hNV5bWsizbY%2Fy2qn91R8Ep8cTCVAmYSvo3hkkdLLh1Np3VpdEAHyQBIoONaPfdnHsLHlRJsD9lu%2FZO%2Bs2T%2BSlscc%2FmYpE0w7tJ%2BtznR4Puj1gutagmwdBkdaWVu71qX7%2BcNfWioEM53LYrtTnZXz&X-Amz-Signature=ea90fea54deefaccc99c9c6c79c2c804bdea07c00ff59fbe4c93683ae8de3a36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBXGH4M%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCebgw0%2Fui3I%2FnQX5t1TwglNBwz0%2BDvrj1zmSLgVESLtwIgJEYJkGDABeSVvTZq%2FGKgfJG1KCqF6TTTx%2FnXha0gfKgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7%2BOVFswS49TmXnEyrcA0WwX85Y3oKpgKtcEUKMLW5cZJhdIBm6vLdtQ1i0PwBhlBqLU0KVmPQwFqakHaT37SyVB28wW%2F5ogCBBBIe07ep1Gu%2FPyum5BTOsLl2AiYNFXEK94XCsSmJTBmKJ7Qr5aGqaRZ4VQ0cEqLRQYMZ7cHrPLrb%2Fc44Hz7D0WhxaHl2U71bTFPfdWJx7MvnCAT8u%2Fpldp7%2FAOPPO876BvE5zIOyhHl9LDzQpbzY434vIYfh%2BlSEwfsGvoU6FIsi4sge4Y7nZfh0eTPPq5HOHtB1qH5o04r%2Fbw8vVuY63enyVlQkgBRwNtbPQO%2FVWz6ZTfiCg5207UjCtO6dXFDI64DUmE2kTnuDZm%2FwV7UBnL3bwC%2BwcX5sdTQ0TPEbtTpT4MTkM%2B64OEF0cFAT5bfXnOfymwClYmp7NlQEBtbh8jA0cTh0FLnzjpC%2FVxJDXANj%2B6bWWyEM9bvfLZ51UXw8GvkURj0pUVQBb7QhFBlyeuIXs1zs8R49OxOYMFp7h0cWuTKy8KmmYhnkLEox0fumzqLp1MSS5mtsHvDDiEb88yzPIs4QHw3B%2F%2FALcBvC9SFdZweYHQ%2FYT0cDsSNIqPAHvWJ7XbAbg4j5%2FMzaFzu1L%2BT5YMdZluHe5k2GqlnUxUzrlMMDl%2F7wGOqUBbhmrecihyY9R5MmwccC6GRRrSfVHxHNEIeA6tB65cGcA6%2FqiKvgZzwJjzJMr5sUAnG1MSKjZ38sIyLBosbFNU0QqNK8n512%2BJdtxF%2BbqO%2F6uEM8oewF7Ohg5JngfJqxcM8gXU8DGu%2Fl%2BkM7Nq2CmrT%2Fu30EAzfyykM6RBeMkL6kA158%2FMipr2kkHUV6JtUUSZszcWrBwhOGzbKJhyEUDXt%2BV58Ad&X-Amz-Signature=3c4bea5060a026a7fc6a0c23d9007db0422ecac5dcdb80cd88d518517dcc722a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBXGH4M%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCebgw0%2Fui3I%2FnQX5t1TwglNBwz0%2BDvrj1zmSLgVESLtwIgJEYJkGDABeSVvTZq%2FGKgfJG1KCqF6TTTx%2FnXha0gfKgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7%2BOVFswS49TmXnEyrcA0WwX85Y3oKpgKtcEUKMLW5cZJhdIBm6vLdtQ1i0PwBhlBqLU0KVmPQwFqakHaT37SyVB28wW%2F5ogCBBBIe07ep1Gu%2FPyum5BTOsLl2AiYNFXEK94XCsSmJTBmKJ7Qr5aGqaRZ4VQ0cEqLRQYMZ7cHrPLrb%2Fc44Hz7D0WhxaHl2U71bTFPfdWJx7MvnCAT8u%2Fpldp7%2FAOPPO876BvE5zIOyhHl9LDzQpbzY434vIYfh%2BlSEwfsGvoU6FIsi4sge4Y7nZfh0eTPPq5HOHtB1qH5o04r%2Fbw8vVuY63enyVlQkgBRwNtbPQO%2FVWz6ZTfiCg5207UjCtO6dXFDI64DUmE2kTnuDZm%2FwV7UBnL3bwC%2BwcX5sdTQ0TPEbtTpT4MTkM%2B64OEF0cFAT5bfXnOfymwClYmp7NlQEBtbh8jA0cTh0FLnzjpC%2FVxJDXANj%2B6bWWyEM9bvfLZ51UXw8GvkURj0pUVQBb7QhFBlyeuIXs1zs8R49OxOYMFp7h0cWuTKy8KmmYhnkLEox0fumzqLp1MSS5mtsHvDDiEb88yzPIs4QHw3B%2F%2FALcBvC9SFdZweYHQ%2FYT0cDsSNIqPAHvWJ7XbAbg4j5%2FMzaFzu1L%2BT5YMdZluHe5k2GqlnUxUzrlMMDl%2F7wGOqUBbhmrecihyY9R5MmwccC6GRRrSfVHxHNEIeA6tB65cGcA6%2FqiKvgZzwJjzJMr5sUAnG1MSKjZ38sIyLBosbFNU0QqNK8n512%2BJdtxF%2BbqO%2F6uEM8oewF7Ohg5JngfJqxcM8gXU8DGu%2Fl%2BkM7Nq2CmrT%2Fu30EAzfyykM6RBeMkL6kA158%2FMipr2kkHUV6JtUUSZszcWrBwhOGzbKJhyEUDXt%2BV58Ad&X-Amz-Signature=8983f92ca0e0d01862f9d87fc6cdd88fe85381174f448df23258de8d45b662f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBXGH4M%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCebgw0%2Fui3I%2FnQX5t1TwglNBwz0%2BDvrj1zmSLgVESLtwIgJEYJkGDABeSVvTZq%2FGKgfJG1KCqF6TTTx%2FnXha0gfKgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7%2BOVFswS49TmXnEyrcA0WwX85Y3oKpgKtcEUKMLW5cZJhdIBm6vLdtQ1i0PwBhlBqLU0KVmPQwFqakHaT37SyVB28wW%2F5ogCBBBIe07ep1Gu%2FPyum5BTOsLl2AiYNFXEK94XCsSmJTBmKJ7Qr5aGqaRZ4VQ0cEqLRQYMZ7cHrPLrb%2Fc44Hz7D0WhxaHl2U71bTFPfdWJx7MvnCAT8u%2Fpldp7%2FAOPPO876BvE5zIOyhHl9LDzQpbzY434vIYfh%2BlSEwfsGvoU6FIsi4sge4Y7nZfh0eTPPq5HOHtB1qH5o04r%2Fbw8vVuY63enyVlQkgBRwNtbPQO%2FVWz6ZTfiCg5207UjCtO6dXFDI64DUmE2kTnuDZm%2FwV7UBnL3bwC%2BwcX5sdTQ0TPEbtTpT4MTkM%2B64OEF0cFAT5bfXnOfymwClYmp7NlQEBtbh8jA0cTh0FLnzjpC%2FVxJDXANj%2B6bWWyEM9bvfLZ51UXw8GvkURj0pUVQBb7QhFBlyeuIXs1zs8R49OxOYMFp7h0cWuTKy8KmmYhnkLEox0fumzqLp1MSS5mtsHvDDiEb88yzPIs4QHw3B%2F%2FALcBvC9SFdZweYHQ%2FYT0cDsSNIqPAHvWJ7XbAbg4j5%2FMzaFzu1L%2BT5YMdZluHe5k2GqlnUxUzrlMMDl%2F7wGOqUBbhmrecihyY9R5MmwccC6GRRrSfVHxHNEIeA6tB65cGcA6%2FqiKvgZzwJjzJMr5sUAnG1MSKjZ38sIyLBosbFNU0QqNK8n512%2BJdtxF%2BbqO%2F6uEM8oewF7Ohg5JngfJqxcM8gXU8DGu%2Fl%2BkM7Nq2CmrT%2Fu30EAzfyykM6RBeMkL6kA158%2FMipr2kkHUV6JtUUSZszcWrBwhOGzbKJhyEUDXt%2BV58Ad&X-Amz-Signature=d673a00b935905e61a9635fa3a996d560523a45fe6d3f34dc8181e6648a0e84b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBXGH4M%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCebgw0%2Fui3I%2FnQX5t1TwglNBwz0%2BDvrj1zmSLgVESLtwIgJEYJkGDABeSVvTZq%2FGKgfJG1KCqF6TTTx%2FnXha0gfKgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7%2BOVFswS49TmXnEyrcA0WwX85Y3oKpgKtcEUKMLW5cZJhdIBm6vLdtQ1i0PwBhlBqLU0KVmPQwFqakHaT37SyVB28wW%2F5ogCBBBIe07ep1Gu%2FPyum5BTOsLl2AiYNFXEK94XCsSmJTBmKJ7Qr5aGqaRZ4VQ0cEqLRQYMZ7cHrPLrb%2Fc44Hz7D0WhxaHl2U71bTFPfdWJx7MvnCAT8u%2Fpldp7%2FAOPPO876BvE5zIOyhHl9LDzQpbzY434vIYfh%2BlSEwfsGvoU6FIsi4sge4Y7nZfh0eTPPq5HOHtB1qH5o04r%2Fbw8vVuY63enyVlQkgBRwNtbPQO%2FVWz6ZTfiCg5207UjCtO6dXFDI64DUmE2kTnuDZm%2FwV7UBnL3bwC%2BwcX5sdTQ0TPEbtTpT4MTkM%2B64OEF0cFAT5bfXnOfymwClYmp7NlQEBtbh8jA0cTh0FLnzjpC%2FVxJDXANj%2B6bWWyEM9bvfLZ51UXw8GvkURj0pUVQBb7QhFBlyeuIXs1zs8R49OxOYMFp7h0cWuTKy8KmmYhnkLEox0fumzqLp1MSS5mtsHvDDiEb88yzPIs4QHw3B%2F%2FALcBvC9SFdZweYHQ%2FYT0cDsSNIqPAHvWJ7XbAbg4j5%2FMzaFzu1L%2BT5YMdZluHe5k2GqlnUxUzrlMMDl%2F7wGOqUBbhmrecihyY9R5MmwccC6GRRrSfVHxHNEIeA6tB65cGcA6%2FqiKvgZzwJjzJMr5sUAnG1MSKjZ38sIyLBosbFNU0QqNK8n512%2BJdtxF%2BbqO%2F6uEM8oewF7Ohg5JngfJqxcM8gXU8DGu%2Fl%2BkM7Nq2CmrT%2Fu30EAzfyykM6RBeMkL6kA158%2FMipr2kkHUV6JtUUSZszcWrBwhOGzbKJhyEUDXt%2BV58Ad&X-Amz-Signature=991b1879eeaa25c05a16b84ddc8661ea13318a5b1a6d93fad0972a8da6643fb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZSH3FKI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZiH9PzxgG1S%2BqTKi3t%2FWCUzwyytT%2FFUJZsuGtIb2goAIgRdCHNC4hYYJM%2BY2eEWKKj%2BesKtniHv571ajVd%2FZNOUMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF9iOTUv6U8d6nIL%2FSrcA3dXKUnsA0U5JQhL6UzUwxS1jwTKoTA1PNv7Jm1xAEB5drYtd0E9nNxdY73hgoFL7AW17sZslk8dHIvyJew0t99AGsLR9KsAgRGbTZm3nW%2FFW9rZHs2SRM6JHRH6VsSp8IoZXMijdyHYQERl8JMpnPNDFr1llWzqMpDtLxgF1EjUH0hgRRSWmk4jTlXQQB%2BNSZUYc5mjFXE5tWmwhitakAYcLRpaWBXzOBH1jQDVNTs8IisYWfYeYk49nWoAABbqYBCZxRAAmJmKNk%2BdP63F6afa%2FsdAHzAx97oNMZ1I71xHFrC49I0aIY8pMNj8SNRpWp3ZyHkz%2FF%2FwrrorS2hwwDv6OF2ACtxzslfkarNlgKSLr5aPDbH3NVNGLqnxklGtmfCtCMGtiB7XE8t5kiQ1w2hVgp5t1%2F94eJXMPfhdCtFCWzcqaF02bV1TZibRmBiylWPAfbPIIpJSvD6oJ2wPCK3z8DjwiAxSOkQC4QH2Q0hGdlaIWHtpBG%2F7hCgFY8lDJO3S5JcX02M0R%2Bf2vFGgQImw7xx8gqSM%2BnsJnHaYMMY5ZhM1O222JsmS4V8oCf%2FTFazbY5zgF05LHjTs91zIvdCqf9uLu9bvgQZWTdW6DWK7ja%2FnmAIUncbiOVHCMLPl%2F7wGOqUBzWpex7w3yr2%2FBiXRUAXo2LiFTQ9TgA%2BDV8PcVcT64miSdvdAK79L3CDcvUBnpfacIKywLPrb1iZ3hQ4h6LfFK0Ug%2F0baU6AYgJ097M3qmwiSyFQUnT9yrB3EFHZIzHYdDn2RpVrcSNOW6zZMCe3zWWEFfuCQsf%2BGxw3PkVf2broC8TBrT7QTQzLbeeMHH36UqkiGx0QAenbuV2sBoeJMg0mIX%2BFc&X-Amz-Signature=35fd7325d7464bb89db68579b9872742f6b6b847e0bd39527eff86771e788ffa&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZSH3FKI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZiH9PzxgG1S%2BqTKi3t%2FWCUzwyytT%2FFUJZsuGtIb2goAIgRdCHNC4hYYJM%2BY2eEWKKj%2BesKtniHv571ajVd%2FZNOUMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF9iOTUv6U8d6nIL%2FSrcA3dXKUnsA0U5JQhL6UzUwxS1jwTKoTA1PNv7Jm1xAEB5drYtd0E9nNxdY73hgoFL7AW17sZslk8dHIvyJew0t99AGsLR9KsAgRGbTZm3nW%2FFW9rZHs2SRM6JHRH6VsSp8IoZXMijdyHYQERl8JMpnPNDFr1llWzqMpDtLxgF1EjUH0hgRRSWmk4jTlXQQB%2BNSZUYc5mjFXE5tWmwhitakAYcLRpaWBXzOBH1jQDVNTs8IisYWfYeYk49nWoAABbqYBCZxRAAmJmKNk%2BdP63F6afa%2FsdAHzAx97oNMZ1I71xHFrC49I0aIY8pMNj8SNRpWp3ZyHkz%2FF%2FwrrorS2hwwDv6OF2ACtxzslfkarNlgKSLr5aPDbH3NVNGLqnxklGtmfCtCMGtiB7XE8t5kiQ1w2hVgp5t1%2F94eJXMPfhdCtFCWzcqaF02bV1TZibRmBiylWPAfbPIIpJSvD6oJ2wPCK3z8DjwiAxSOkQC4QH2Q0hGdlaIWHtpBG%2F7hCgFY8lDJO3S5JcX02M0R%2Bf2vFGgQImw7xx8gqSM%2BnsJnHaYMMY5ZhM1O222JsmS4V8oCf%2FTFazbY5zgF05LHjTs91zIvdCqf9uLu9bvgQZWTdW6DWK7ja%2FnmAIUncbiOVHCMLPl%2F7wGOqUBzWpex7w3yr2%2FBiXRUAXo2LiFTQ9TgA%2BDV8PcVcT64miSdvdAK79L3CDcvUBnpfacIKywLPrb1iZ3hQ4h6LfFK0Ug%2F0baU6AYgJ097M3qmwiSyFQUnT9yrB3EFHZIzHYdDn2RpVrcSNOW6zZMCe3zWWEFfuCQsf%2BGxw3PkVf2broC8TBrT7QTQzLbeeMHH36UqkiGx0QAenbuV2sBoeJMg0mIX%2BFc&X-Amz-Signature=10507c3051dfa5adf141e9dde2fd1dde47ce13353084b6718896330bbecdb2a1&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZSH3FKI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZiH9PzxgG1S%2BqTKi3t%2FWCUzwyytT%2FFUJZsuGtIb2goAIgRdCHNC4hYYJM%2BY2eEWKKj%2BesKtniHv571ajVd%2FZNOUMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF9iOTUv6U8d6nIL%2FSrcA3dXKUnsA0U5JQhL6UzUwxS1jwTKoTA1PNv7Jm1xAEB5drYtd0E9nNxdY73hgoFL7AW17sZslk8dHIvyJew0t99AGsLR9KsAgRGbTZm3nW%2FFW9rZHs2SRM6JHRH6VsSp8IoZXMijdyHYQERl8JMpnPNDFr1llWzqMpDtLxgF1EjUH0hgRRSWmk4jTlXQQB%2BNSZUYc5mjFXE5tWmwhitakAYcLRpaWBXzOBH1jQDVNTs8IisYWfYeYk49nWoAABbqYBCZxRAAmJmKNk%2BdP63F6afa%2FsdAHzAx97oNMZ1I71xHFrC49I0aIY8pMNj8SNRpWp3ZyHkz%2FF%2FwrrorS2hwwDv6OF2ACtxzslfkarNlgKSLr5aPDbH3NVNGLqnxklGtmfCtCMGtiB7XE8t5kiQ1w2hVgp5t1%2F94eJXMPfhdCtFCWzcqaF02bV1TZibRmBiylWPAfbPIIpJSvD6oJ2wPCK3z8DjwiAxSOkQC4QH2Q0hGdlaIWHtpBG%2F7hCgFY8lDJO3S5JcX02M0R%2Bf2vFGgQImw7xx8gqSM%2BnsJnHaYMMY5ZhM1O222JsmS4V8oCf%2FTFazbY5zgF05LHjTs91zIvdCqf9uLu9bvgQZWTdW6DWK7ja%2FnmAIUncbiOVHCMLPl%2F7wGOqUBzWpex7w3yr2%2FBiXRUAXo2LiFTQ9TgA%2BDV8PcVcT64miSdvdAK79L3CDcvUBnpfacIKywLPrb1iZ3hQ4h6LfFK0Ug%2F0baU6AYgJ097M3qmwiSyFQUnT9yrB3EFHZIzHYdDn2RpVrcSNOW6zZMCe3zWWEFfuCQsf%2BGxw3PkVf2broC8TBrT7QTQzLbeeMHH36UqkiGx0QAenbuV2sBoeJMg0mIX%2BFc&X-Amz-Signature=5b7a1fb003fe65de73a1903e18c2369760a2f6769facc7f35e4505ba3d0b99b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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

