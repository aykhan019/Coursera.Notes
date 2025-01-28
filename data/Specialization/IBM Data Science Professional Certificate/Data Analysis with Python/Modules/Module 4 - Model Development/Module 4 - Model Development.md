

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG4JHLET%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIBUCmFre2aAw9cogwx4UugWguN74ur4HNLTghK%2B0pWs%2FAiEAv7FCivuZy8fR0r8DnOrk%2Bqpx%2F9LIO2eGqK4pLTxFALUq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEftR4wVfUksgR19dCrcA7r%2B%2F8DGjQGfhS0YQaf%2BFtZ0t5J6Iv4ZOWvq0MOXcCFzlEBTyFTSJ2fSK6t9ai6eO1SEBwdr%2B48pciZoJvDhpo53xUO81BrIhECOP6G%2BHdy7%2FGPwVPGhxf8vJcrTgwtKQ%2F3h9ihXIbbT24X70NQa6k40nEwmIiG3h10dcY%2B8%2BGfXUmP%2FA1Ah1W4xLpxj8Kc31UDMpaXVavjfyT2YSRCMMKwLKjd%2BMTIn%2BnInyhenkSj7bWPMwO313OBA096wlZH4nGGh3LPKJg4g%2FKlsSWoasSR7u76KMpC0VSYuD3NTwu3sK6rkRaqhi9py6wXu6lOcWt1MDd0iXCcoEUyAHtFZBKWrht9sDC0fwao128zPaZ4Nu%2Fqvaa49pK%2BTi6sqv93qTOP1V8iNGnD0Bcsbie8s7vtFDvSegaNWsBDPPuYJA%2B%2BN%2FNPAKCbjSXEDT%2BERnanCvvYTvBbsWX9yrF9GPfZEOMLr9yKUFfJDPwEgIcPE0C%2B%2By8euI4KlUu8m8H0AXEJqt1oLaW%2FrWZXFAp9Ztza1wn1QbPVEdQYcdsTa6rzHw4YLyq0teWuZu9gZ0fUv3hOVEjSMdFX%2B35qj%2FSdoemruzNq9Z4aLokm%2BY9GJkw77DiTSFa5vEgoKXEH03Ur4MKv65LwGOqUBrMh3QS9OtQ9taDgJJ69JrO7tuV79pjlquhQLbz0Ib%2F2bLUgsA3Tr8aoc5Su%2BOHA4Jnvu6vgWbfEbLQaiGjL%2Bx0YwidNm6yulTl9KrI%2B0nG4xhb20uh0FmVDgOtTTYpejFvcUUBGxBjkGkQDBdJDdggxM8BRJBfjpj0qJgZGY7wJpVnsW58H2cjE%2BXNJVs%2BxgqDTf5IY4D33KcA%2B5zE566VrNa5OE&X-Amz-Signature=b1ea92d15cf70b6138ebb19320fce76a29591caf18e3ae51d60cb72647eabf80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG4JHLET%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIBUCmFre2aAw9cogwx4UugWguN74ur4HNLTghK%2B0pWs%2FAiEAv7FCivuZy8fR0r8DnOrk%2Bqpx%2F9LIO2eGqK4pLTxFALUq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEftR4wVfUksgR19dCrcA7r%2B%2F8DGjQGfhS0YQaf%2BFtZ0t5J6Iv4ZOWvq0MOXcCFzlEBTyFTSJ2fSK6t9ai6eO1SEBwdr%2B48pciZoJvDhpo53xUO81BrIhECOP6G%2BHdy7%2FGPwVPGhxf8vJcrTgwtKQ%2F3h9ihXIbbT24X70NQa6k40nEwmIiG3h10dcY%2B8%2BGfXUmP%2FA1Ah1W4xLpxj8Kc31UDMpaXVavjfyT2YSRCMMKwLKjd%2BMTIn%2BnInyhenkSj7bWPMwO313OBA096wlZH4nGGh3LPKJg4g%2FKlsSWoasSR7u76KMpC0VSYuD3NTwu3sK6rkRaqhi9py6wXu6lOcWt1MDd0iXCcoEUyAHtFZBKWrht9sDC0fwao128zPaZ4Nu%2Fqvaa49pK%2BTi6sqv93qTOP1V8iNGnD0Bcsbie8s7vtFDvSegaNWsBDPPuYJA%2B%2BN%2FNPAKCbjSXEDT%2BERnanCvvYTvBbsWX9yrF9GPfZEOMLr9yKUFfJDPwEgIcPE0C%2B%2By8euI4KlUu8m8H0AXEJqt1oLaW%2FrWZXFAp9Ztza1wn1QbPVEdQYcdsTa6rzHw4YLyq0teWuZu9gZ0fUv3hOVEjSMdFX%2B35qj%2FSdoemruzNq9Z4aLokm%2BY9GJkw77DiTSFa5vEgoKXEH03Ur4MKv65LwGOqUBrMh3QS9OtQ9taDgJJ69JrO7tuV79pjlquhQLbz0Ib%2F2bLUgsA3Tr8aoc5Su%2BOHA4Jnvu6vgWbfEbLQaiGjL%2Bx0YwidNm6yulTl9KrI%2B0nG4xhb20uh0FmVDgOtTTYpejFvcUUBGxBjkGkQDBdJDdggxM8BRJBfjpj0qJgZGY7wJpVnsW58H2cjE%2BXNJVs%2BxgqDTf5IY4D33KcA%2B5zE566VrNa5OE&X-Amz-Signature=5f7ec127091550b2236afb0c83ecf0e162239fffcd1cccb01c551891540329c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG4JHLET%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIBUCmFre2aAw9cogwx4UugWguN74ur4HNLTghK%2B0pWs%2FAiEAv7FCivuZy8fR0r8DnOrk%2Bqpx%2F9LIO2eGqK4pLTxFALUq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEftR4wVfUksgR19dCrcA7r%2B%2F8DGjQGfhS0YQaf%2BFtZ0t5J6Iv4ZOWvq0MOXcCFzlEBTyFTSJ2fSK6t9ai6eO1SEBwdr%2B48pciZoJvDhpo53xUO81BrIhECOP6G%2BHdy7%2FGPwVPGhxf8vJcrTgwtKQ%2F3h9ihXIbbT24X70NQa6k40nEwmIiG3h10dcY%2B8%2BGfXUmP%2FA1Ah1W4xLpxj8Kc31UDMpaXVavjfyT2YSRCMMKwLKjd%2BMTIn%2BnInyhenkSj7bWPMwO313OBA096wlZH4nGGh3LPKJg4g%2FKlsSWoasSR7u76KMpC0VSYuD3NTwu3sK6rkRaqhi9py6wXu6lOcWt1MDd0iXCcoEUyAHtFZBKWrht9sDC0fwao128zPaZ4Nu%2Fqvaa49pK%2BTi6sqv93qTOP1V8iNGnD0Bcsbie8s7vtFDvSegaNWsBDPPuYJA%2B%2BN%2FNPAKCbjSXEDT%2BERnanCvvYTvBbsWX9yrF9GPfZEOMLr9yKUFfJDPwEgIcPE0C%2B%2By8euI4KlUu8m8H0AXEJqt1oLaW%2FrWZXFAp9Ztza1wn1QbPVEdQYcdsTa6rzHw4YLyq0teWuZu9gZ0fUv3hOVEjSMdFX%2B35qj%2FSdoemruzNq9Z4aLokm%2BY9GJkw77DiTSFa5vEgoKXEH03Ur4MKv65LwGOqUBrMh3QS9OtQ9taDgJJ69JrO7tuV79pjlquhQLbz0Ib%2F2bLUgsA3Tr8aoc5Su%2BOHA4Jnvu6vgWbfEbLQaiGjL%2Bx0YwidNm6yulTl9KrI%2B0nG4xhb20uh0FmVDgOtTTYpejFvcUUBGxBjkGkQDBdJDdggxM8BRJBfjpj0qJgZGY7wJpVnsW58H2cjE%2BXNJVs%2BxgqDTf5IY4D33KcA%2B5zE566VrNa5OE&X-Amz-Signature=0da32019960268e6c5783cb05ddaef2adcfab6392d58fae81b613f44dd2de209&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG4JHLET%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIBUCmFre2aAw9cogwx4UugWguN74ur4HNLTghK%2B0pWs%2FAiEAv7FCivuZy8fR0r8DnOrk%2Bqpx%2F9LIO2eGqK4pLTxFALUq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEftR4wVfUksgR19dCrcA7r%2B%2F8DGjQGfhS0YQaf%2BFtZ0t5J6Iv4ZOWvq0MOXcCFzlEBTyFTSJ2fSK6t9ai6eO1SEBwdr%2B48pciZoJvDhpo53xUO81BrIhECOP6G%2BHdy7%2FGPwVPGhxf8vJcrTgwtKQ%2F3h9ihXIbbT24X70NQa6k40nEwmIiG3h10dcY%2B8%2BGfXUmP%2FA1Ah1W4xLpxj8Kc31UDMpaXVavjfyT2YSRCMMKwLKjd%2BMTIn%2BnInyhenkSj7bWPMwO313OBA096wlZH4nGGh3LPKJg4g%2FKlsSWoasSR7u76KMpC0VSYuD3NTwu3sK6rkRaqhi9py6wXu6lOcWt1MDd0iXCcoEUyAHtFZBKWrht9sDC0fwao128zPaZ4Nu%2Fqvaa49pK%2BTi6sqv93qTOP1V8iNGnD0Bcsbie8s7vtFDvSegaNWsBDPPuYJA%2B%2BN%2FNPAKCbjSXEDT%2BERnanCvvYTvBbsWX9yrF9GPfZEOMLr9yKUFfJDPwEgIcPE0C%2B%2By8euI4KlUu8m8H0AXEJqt1oLaW%2FrWZXFAp9Ztza1wn1QbPVEdQYcdsTa6rzHw4YLyq0teWuZu9gZ0fUv3hOVEjSMdFX%2B35qj%2FSdoemruzNq9Z4aLokm%2BY9GJkw77DiTSFa5vEgoKXEH03Ur4MKv65LwGOqUBrMh3QS9OtQ9taDgJJ69JrO7tuV79pjlquhQLbz0Ib%2F2bLUgsA3Tr8aoc5Su%2BOHA4Jnvu6vgWbfEbLQaiGjL%2Bx0YwidNm6yulTl9KrI%2B0nG4xhb20uh0FmVDgOtTTYpejFvcUUBGxBjkGkQDBdJDdggxM8BRJBfjpj0qJgZGY7wJpVnsW58H2cjE%2BXNJVs%2BxgqDTf5IY4D33KcA%2B5zE566VrNa5OE&X-Amz-Signature=e31d5228192197e59506b4319935e0cbc4af0d7376fb7760a8e7d5bdfd76f880&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG4JHLET%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIBUCmFre2aAw9cogwx4UugWguN74ur4HNLTghK%2B0pWs%2FAiEAv7FCivuZy8fR0r8DnOrk%2Bqpx%2F9LIO2eGqK4pLTxFALUq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEftR4wVfUksgR19dCrcA7r%2B%2F8DGjQGfhS0YQaf%2BFtZ0t5J6Iv4ZOWvq0MOXcCFzlEBTyFTSJ2fSK6t9ai6eO1SEBwdr%2B48pciZoJvDhpo53xUO81BrIhECOP6G%2BHdy7%2FGPwVPGhxf8vJcrTgwtKQ%2F3h9ihXIbbT24X70NQa6k40nEwmIiG3h10dcY%2B8%2BGfXUmP%2FA1Ah1W4xLpxj8Kc31UDMpaXVavjfyT2YSRCMMKwLKjd%2BMTIn%2BnInyhenkSj7bWPMwO313OBA096wlZH4nGGh3LPKJg4g%2FKlsSWoasSR7u76KMpC0VSYuD3NTwu3sK6rkRaqhi9py6wXu6lOcWt1MDd0iXCcoEUyAHtFZBKWrht9sDC0fwao128zPaZ4Nu%2Fqvaa49pK%2BTi6sqv93qTOP1V8iNGnD0Bcsbie8s7vtFDvSegaNWsBDPPuYJA%2B%2BN%2FNPAKCbjSXEDT%2BERnanCvvYTvBbsWX9yrF9GPfZEOMLr9yKUFfJDPwEgIcPE0C%2B%2By8euI4KlUu8m8H0AXEJqt1oLaW%2FrWZXFAp9Ztza1wn1QbPVEdQYcdsTa6rzHw4YLyq0teWuZu9gZ0fUv3hOVEjSMdFX%2B35qj%2FSdoemruzNq9Z4aLokm%2BY9GJkw77DiTSFa5vEgoKXEH03Ur4MKv65LwGOqUBrMh3QS9OtQ9taDgJJ69JrO7tuV79pjlquhQLbz0Ib%2F2bLUgsA3Tr8aoc5Su%2BOHA4Jnvu6vgWbfEbLQaiGjL%2Bx0YwidNm6yulTl9KrI%2B0nG4xhb20uh0FmVDgOtTTYpejFvcUUBGxBjkGkQDBdJDdggxM8BRJBfjpj0qJgZGY7wJpVnsW58H2cjE%2BXNJVs%2BxgqDTf5IY4D33KcA%2B5zE566VrNa5OE&X-Amz-Signature=eea83759b97490ef3952e04af4177bfba0c134cf0712e214f481878aa1522576&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG4JHLET%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIBUCmFre2aAw9cogwx4UugWguN74ur4HNLTghK%2B0pWs%2FAiEAv7FCivuZy8fR0r8DnOrk%2Bqpx%2F9LIO2eGqK4pLTxFALUq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEftR4wVfUksgR19dCrcA7r%2B%2F8DGjQGfhS0YQaf%2BFtZ0t5J6Iv4ZOWvq0MOXcCFzlEBTyFTSJ2fSK6t9ai6eO1SEBwdr%2B48pciZoJvDhpo53xUO81BrIhECOP6G%2BHdy7%2FGPwVPGhxf8vJcrTgwtKQ%2F3h9ihXIbbT24X70NQa6k40nEwmIiG3h10dcY%2B8%2BGfXUmP%2FA1Ah1W4xLpxj8Kc31UDMpaXVavjfyT2YSRCMMKwLKjd%2BMTIn%2BnInyhenkSj7bWPMwO313OBA096wlZH4nGGh3LPKJg4g%2FKlsSWoasSR7u76KMpC0VSYuD3NTwu3sK6rkRaqhi9py6wXu6lOcWt1MDd0iXCcoEUyAHtFZBKWrht9sDC0fwao128zPaZ4Nu%2Fqvaa49pK%2BTi6sqv93qTOP1V8iNGnD0Bcsbie8s7vtFDvSegaNWsBDPPuYJA%2B%2BN%2FNPAKCbjSXEDT%2BERnanCvvYTvBbsWX9yrF9GPfZEOMLr9yKUFfJDPwEgIcPE0C%2B%2By8euI4KlUu8m8H0AXEJqt1oLaW%2FrWZXFAp9Ztza1wn1QbPVEdQYcdsTa6rzHw4YLyq0teWuZu9gZ0fUv3hOVEjSMdFX%2B35qj%2FSdoemruzNq9Z4aLokm%2BY9GJkw77DiTSFa5vEgoKXEH03Ur4MKv65LwGOqUBrMh3QS9OtQ9taDgJJ69JrO7tuV79pjlquhQLbz0Ib%2F2bLUgsA3Tr8aoc5Su%2BOHA4Jnvu6vgWbfEbLQaiGjL%2Bx0YwidNm6yulTl9KrI%2B0nG4xhb20uh0FmVDgOtTTYpejFvcUUBGxBjkGkQDBdJDdggxM8BRJBfjpj0qJgZGY7wJpVnsW58H2cjE%2BXNJVs%2BxgqDTf5IY4D33KcA%2B5zE566VrNa5OE&X-Amz-Signature=465136b753d09899c38e8795ce1ba98d9ab7d763f4a2294845d4e1f798ce2758&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG4JHLET%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIBUCmFre2aAw9cogwx4UugWguN74ur4HNLTghK%2B0pWs%2FAiEAv7FCivuZy8fR0r8DnOrk%2Bqpx%2F9LIO2eGqK4pLTxFALUq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEftR4wVfUksgR19dCrcA7r%2B%2F8DGjQGfhS0YQaf%2BFtZ0t5J6Iv4ZOWvq0MOXcCFzlEBTyFTSJ2fSK6t9ai6eO1SEBwdr%2B48pciZoJvDhpo53xUO81BrIhECOP6G%2BHdy7%2FGPwVPGhxf8vJcrTgwtKQ%2F3h9ihXIbbT24X70NQa6k40nEwmIiG3h10dcY%2B8%2BGfXUmP%2FA1Ah1W4xLpxj8Kc31UDMpaXVavjfyT2YSRCMMKwLKjd%2BMTIn%2BnInyhenkSj7bWPMwO313OBA096wlZH4nGGh3LPKJg4g%2FKlsSWoasSR7u76KMpC0VSYuD3NTwu3sK6rkRaqhi9py6wXu6lOcWt1MDd0iXCcoEUyAHtFZBKWrht9sDC0fwao128zPaZ4Nu%2Fqvaa49pK%2BTi6sqv93qTOP1V8iNGnD0Bcsbie8s7vtFDvSegaNWsBDPPuYJA%2B%2BN%2FNPAKCbjSXEDT%2BERnanCvvYTvBbsWX9yrF9GPfZEOMLr9yKUFfJDPwEgIcPE0C%2B%2By8euI4KlUu8m8H0AXEJqt1oLaW%2FrWZXFAp9Ztza1wn1QbPVEdQYcdsTa6rzHw4YLyq0teWuZu9gZ0fUv3hOVEjSMdFX%2B35qj%2FSdoemruzNq9Z4aLokm%2BY9GJkw77DiTSFa5vEgoKXEH03Ur4MKv65LwGOqUBrMh3QS9OtQ9taDgJJ69JrO7tuV79pjlquhQLbz0Ib%2F2bLUgsA3Tr8aoc5Su%2BOHA4Jnvu6vgWbfEbLQaiGjL%2Bx0YwidNm6yulTl9KrI%2B0nG4xhb20uh0FmVDgOtTTYpejFvcUUBGxBjkGkQDBdJDdggxM8BRJBfjpj0qJgZGY7wJpVnsW58H2cjE%2BXNJVs%2BxgqDTf5IY4D33KcA%2B5zE566VrNa5OE&X-Amz-Signature=3f8764b0902d438c999f55069c46029d2c75d620cec36f22230fd7bf791868a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG4JHLET%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIBUCmFre2aAw9cogwx4UugWguN74ur4HNLTghK%2B0pWs%2FAiEAv7FCivuZy8fR0r8DnOrk%2Bqpx%2F9LIO2eGqK4pLTxFALUq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEftR4wVfUksgR19dCrcA7r%2B%2F8DGjQGfhS0YQaf%2BFtZ0t5J6Iv4ZOWvq0MOXcCFzlEBTyFTSJ2fSK6t9ai6eO1SEBwdr%2B48pciZoJvDhpo53xUO81BrIhECOP6G%2BHdy7%2FGPwVPGhxf8vJcrTgwtKQ%2F3h9ihXIbbT24X70NQa6k40nEwmIiG3h10dcY%2B8%2BGfXUmP%2FA1Ah1W4xLpxj8Kc31UDMpaXVavjfyT2YSRCMMKwLKjd%2BMTIn%2BnInyhenkSj7bWPMwO313OBA096wlZH4nGGh3LPKJg4g%2FKlsSWoasSR7u76KMpC0VSYuD3NTwu3sK6rkRaqhi9py6wXu6lOcWt1MDd0iXCcoEUyAHtFZBKWrht9sDC0fwao128zPaZ4Nu%2Fqvaa49pK%2BTi6sqv93qTOP1V8iNGnD0Bcsbie8s7vtFDvSegaNWsBDPPuYJA%2B%2BN%2FNPAKCbjSXEDT%2BERnanCvvYTvBbsWX9yrF9GPfZEOMLr9yKUFfJDPwEgIcPE0C%2B%2By8euI4KlUu8m8H0AXEJqt1oLaW%2FrWZXFAp9Ztza1wn1QbPVEdQYcdsTa6rzHw4YLyq0teWuZu9gZ0fUv3hOVEjSMdFX%2B35qj%2FSdoemruzNq9Z4aLokm%2BY9GJkw77DiTSFa5vEgoKXEH03Ur4MKv65LwGOqUBrMh3QS9OtQ9taDgJJ69JrO7tuV79pjlquhQLbz0Ib%2F2bLUgsA3Tr8aoc5Su%2BOHA4Jnvu6vgWbfEbLQaiGjL%2Bx0YwidNm6yulTl9KrI%2B0nG4xhb20uh0FmVDgOtTTYpejFvcUUBGxBjkGkQDBdJDdggxM8BRJBfjpj0qJgZGY7wJpVnsW58H2cjE%2BXNJVs%2BxgqDTf5IY4D33KcA%2B5zE566VrNa5OE&X-Amz-Signature=6f841144074254ffbd44b30e5a127610d2a0c7aa6a558752429934b252bca24b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG4JHLET%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIBUCmFre2aAw9cogwx4UugWguN74ur4HNLTghK%2B0pWs%2FAiEAv7FCivuZy8fR0r8DnOrk%2Bqpx%2F9LIO2eGqK4pLTxFALUq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEftR4wVfUksgR19dCrcA7r%2B%2F8DGjQGfhS0YQaf%2BFtZ0t5J6Iv4ZOWvq0MOXcCFzlEBTyFTSJ2fSK6t9ai6eO1SEBwdr%2B48pciZoJvDhpo53xUO81BrIhECOP6G%2BHdy7%2FGPwVPGhxf8vJcrTgwtKQ%2F3h9ihXIbbT24X70NQa6k40nEwmIiG3h10dcY%2B8%2BGfXUmP%2FA1Ah1W4xLpxj8Kc31UDMpaXVavjfyT2YSRCMMKwLKjd%2BMTIn%2BnInyhenkSj7bWPMwO313OBA096wlZH4nGGh3LPKJg4g%2FKlsSWoasSR7u76KMpC0VSYuD3NTwu3sK6rkRaqhi9py6wXu6lOcWt1MDd0iXCcoEUyAHtFZBKWrht9sDC0fwao128zPaZ4Nu%2Fqvaa49pK%2BTi6sqv93qTOP1V8iNGnD0Bcsbie8s7vtFDvSegaNWsBDPPuYJA%2B%2BN%2FNPAKCbjSXEDT%2BERnanCvvYTvBbsWX9yrF9GPfZEOMLr9yKUFfJDPwEgIcPE0C%2B%2By8euI4KlUu8m8H0AXEJqt1oLaW%2FrWZXFAp9Ztza1wn1QbPVEdQYcdsTa6rzHw4YLyq0teWuZu9gZ0fUv3hOVEjSMdFX%2B35qj%2FSdoemruzNq9Z4aLokm%2BY9GJkw77DiTSFa5vEgoKXEH03Ur4MKv65LwGOqUBrMh3QS9OtQ9taDgJJ69JrO7tuV79pjlquhQLbz0Ib%2F2bLUgsA3Tr8aoc5Su%2BOHA4Jnvu6vgWbfEbLQaiGjL%2Bx0YwidNm6yulTl9KrI%2B0nG4xhb20uh0FmVDgOtTTYpejFvcUUBGxBjkGkQDBdJDdggxM8BRJBfjpj0qJgZGY7wJpVnsW58H2cjE%2BXNJVs%2BxgqDTf5IY4D33KcA%2B5zE566VrNa5OE&X-Amz-Signature=0cd6ae96717de487d82c89bade31031eca64f63ed4c500859b27678576cea985&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG4JHLET%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIBUCmFre2aAw9cogwx4UugWguN74ur4HNLTghK%2B0pWs%2FAiEAv7FCivuZy8fR0r8DnOrk%2Bqpx%2F9LIO2eGqK4pLTxFALUq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEftR4wVfUksgR19dCrcA7r%2B%2F8DGjQGfhS0YQaf%2BFtZ0t5J6Iv4ZOWvq0MOXcCFzlEBTyFTSJ2fSK6t9ai6eO1SEBwdr%2B48pciZoJvDhpo53xUO81BrIhECOP6G%2BHdy7%2FGPwVPGhxf8vJcrTgwtKQ%2F3h9ihXIbbT24X70NQa6k40nEwmIiG3h10dcY%2B8%2BGfXUmP%2FA1Ah1W4xLpxj8Kc31UDMpaXVavjfyT2YSRCMMKwLKjd%2BMTIn%2BnInyhenkSj7bWPMwO313OBA096wlZH4nGGh3LPKJg4g%2FKlsSWoasSR7u76KMpC0VSYuD3NTwu3sK6rkRaqhi9py6wXu6lOcWt1MDd0iXCcoEUyAHtFZBKWrht9sDC0fwao128zPaZ4Nu%2Fqvaa49pK%2BTi6sqv93qTOP1V8iNGnD0Bcsbie8s7vtFDvSegaNWsBDPPuYJA%2B%2BN%2FNPAKCbjSXEDT%2BERnanCvvYTvBbsWX9yrF9GPfZEOMLr9yKUFfJDPwEgIcPE0C%2B%2By8euI4KlUu8m8H0AXEJqt1oLaW%2FrWZXFAp9Ztza1wn1QbPVEdQYcdsTa6rzHw4YLyq0teWuZu9gZ0fUv3hOVEjSMdFX%2B35qj%2FSdoemruzNq9Z4aLokm%2BY9GJkw77DiTSFa5vEgoKXEH03Ur4MKv65LwGOqUBrMh3QS9OtQ9taDgJJ69JrO7tuV79pjlquhQLbz0Ib%2F2bLUgsA3Tr8aoc5Su%2BOHA4Jnvu6vgWbfEbLQaiGjL%2Bx0YwidNm6yulTl9KrI%2B0nG4xhb20uh0FmVDgOtTTYpejFvcUUBGxBjkGkQDBdJDdggxM8BRJBfjpj0qJgZGY7wJpVnsW58H2cjE%2BXNJVs%2BxgqDTf5IY4D33KcA%2B5zE566VrNa5OE&X-Amz-Signature=38de42fcb84614122bd0d71a31c34f71b4a9713395b061c2d8a1fac21333b783&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG4JHLET%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIBUCmFre2aAw9cogwx4UugWguN74ur4HNLTghK%2B0pWs%2FAiEAv7FCivuZy8fR0r8DnOrk%2Bqpx%2F9LIO2eGqK4pLTxFALUq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDEftR4wVfUksgR19dCrcA7r%2B%2F8DGjQGfhS0YQaf%2BFtZ0t5J6Iv4ZOWvq0MOXcCFzlEBTyFTSJ2fSK6t9ai6eO1SEBwdr%2B48pciZoJvDhpo53xUO81BrIhECOP6G%2BHdy7%2FGPwVPGhxf8vJcrTgwtKQ%2F3h9ihXIbbT24X70NQa6k40nEwmIiG3h10dcY%2B8%2BGfXUmP%2FA1Ah1W4xLpxj8Kc31UDMpaXVavjfyT2YSRCMMKwLKjd%2BMTIn%2BnInyhenkSj7bWPMwO313OBA096wlZH4nGGh3LPKJg4g%2FKlsSWoasSR7u76KMpC0VSYuD3NTwu3sK6rkRaqhi9py6wXu6lOcWt1MDd0iXCcoEUyAHtFZBKWrht9sDC0fwao128zPaZ4Nu%2Fqvaa49pK%2BTi6sqv93qTOP1V8iNGnD0Bcsbie8s7vtFDvSegaNWsBDPPuYJA%2B%2BN%2FNPAKCbjSXEDT%2BERnanCvvYTvBbsWX9yrF9GPfZEOMLr9yKUFfJDPwEgIcPE0C%2B%2By8euI4KlUu8m8H0AXEJqt1oLaW%2FrWZXFAp9Ztza1wn1QbPVEdQYcdsTa6rzHw4YLyq0teWuZu9gZ0fUv3hOVEjSMdFX%2B35qj%2FSdoemruzNq9Z4aLokm%2BY9GJkw77DiTSFa5vEgoKXEH03Ur4MKv65LwGOqUBrMh3QS9OtQ9taDgJJ69JrO7tuV79pjlquhQLbz0Ib%2F2bLUgsA3Tr8aoc5Su%2BOHA4Jnvu6vgWbfEbLQaiGjL%2Bx0YwidNm6yulTl9KrI%2B0nG4xhb20uh0FmVDgOtTTYpejFvcUUBGxBjkGkQDBdJDdggxM8BRJBfjpj0qJgZGY7wJpVnsW58H2cjE%2BXNJVs%2BxgqDTf5IY4D33KcA%2B5zE566VrNa5OE&X-Amz-Signature=670a67a5f9b68bd01b2a812f7dc4bc3030103849f014e01ed8182dc6963d282c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TMICWVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIGGHX9oSeFpkbZjMCLovC7vjReKaGTpSapULlkBVqwtLAiEAxZq6O1Suyq%2FOZ6wI0Mfrtve4F%2FoxlVo0yh04Mf8IhMsq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDKym9gTBLi2gFu1elyrcA5SpUOYCLHCZLxS%2FKMzmzWyW90KkgKmE6hl76K9BOcMjdw9KgKcIaJ0QDtu%2BBm7wHq7cCtlr9AxtLXQV4K%2F6rmLTdErTP9qEw7MwmlHuMRgOHWZjKEKQs%2F0uPGfkVDyHAh%2BTD8AzvFhQpaRjoOvWW%2BXy6bbYR9rbhuf%2Blt9ZHycSLxMUPPLZ1d8pSGXT38DOVbXlD2HIo%2F69LngIH8HDVAuPDjH4SQHvjhBmFqjFFh9jsyD6%2Bi5u%2BU4OAaPpNhVq7Q0fUFM1oV79kSwQKfwtRP%2FVx3DYdlG03BO7V0E54484skUc72ewWvrqhEWTewK%2BjQKKrDPV0hbO72LA4azyvmZjPXT9GVrsRMjNxliYJp5QoHtAX5%2FWvSJBxvKBeKVW6RgpZojir82Z9hK5TnZ%2F1Kv73iHVq23ZgVjSWVCOQZZ6E3zUmEn4tIUkKMvMDyzCa1j0MS8i6qB2HldssijEtXW0Y5MLIUetDJFlvAAmB7BbjA27hxPzos3aNLhPCPCTXIOdOvfr70%2Fp8Y7zEbvbd0GKgYkPEahUm%2F5%2BbkFFpwnj0g%2BAE6Ju4E3jnZUgLVV9DMwOAyib%2BZYHHflWk8UA6Uix2D3e5gQ8%2BS0hezsi2JIPetaxBBs833dx3%2FZhMMf55LwGOqUB7OY%2F1KnAnBZFdli7l%2FPkqsL5%2FD%2FYbxqVTuTyPJe5gKfgPdvWGGzrRSdlWbZI16RbQgFLoWvNCdidFKm%2Bai1c0%2B9mOEUXmgs%2FRsEvrX9DO3yiSiys4rUb2Y8sr5HReGMtU4adXNipWTSR4zvhCxjaF%2FW52CPthe2WBks8TGecR4j6e5IDD1POkzZTvHv%2Bx8YILuydPNZ58io6w8ABVII4TySJvKIK&X-Amz-Signature=6d141323bfeb3f4abd169b88457ec9caed6c85baae7404088656cf597dfae4ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TMICWVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIGGHX9oSeFpkbZjMCLovC7vjReKaGTpSapULlkBVqwtLAiEAxZq6O1Suyq%2FOZ6wI0Mfrtve4F%2FoxlVo0yh04Mf8IhMsq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDKym9gTBLi2gFu1elyrcA5SpUOYCLHCZLxS%2FKMzmzWyW90KkgKmE6hl76K9BOcMjdw9KgKcIaJ0QDtu%2BBm7wHq7cCtlr9AxtLXQV4K%2F6rmLTdErTP9qEw7MwmlHuMRgOHWZjKEKQs%2F0uPGfkVDyHAh%2BTD8AzvFhQpaRjoOvWW%2BXy6bbYR9rbhuf%2Blt9ZHycSLxMUPPLZ1d8pSGXT38DOVbXlD2HIo%2F69LngIH8HDVAuPDjH4SQHvjhBmFqjFFh9jsyD6%2Bi5u%2BU4OAaPpNhVq7Q0fUFM1oV79kSwQKfwtRP%2FVx3DYdlG03BO7V0E54484skUc72ewWvrqhEWTewK%2BjQKKrDPV0hbO72LA4azyvmZjPXT9GVrsRMjNxliYJp5QoHtAX5%2FWvSJBxvKBeKVW6RgpZojir82Z9hK5TnZ%2F1Kv73iHVq23ZgVjSWVCOQZZ6E3zUmEn4tIUkKMvMDyzCa1j0MS8i6qB2HldssijEtXW0Y5MLIUetDJFlvAAmB7BbjA27hxPzos3aNLhPCPCTXIOdOvfr70%2Fp8Y7zEbvbd0GKgYkPEahUm%2F5%2BbkFFpwnj0g%2BAE6Ju4E3jnZUgLVV9DMwOAyib%2BZYHHflWk8UA6Uix2D3e5gQ8%2BS0hezsi2JIPetaxBBs833dx3%2FZhMMf55LwGOqUB7OY%2F1KnAnBZFdli7l%2FPkqsL5%2FD%2FYbxqVTuTyPJe5gKfgPdvWGGzrRSdlWbZI16RbQgFLoWvNCdidFKm%2Bai1c0%2B9mOEUXmgs%2FRsEvrX9DO3yiSiys4rUb2Y8sr5HReGMtU4adXNipWTSR4zvhCxjaF%2FW52CPthe2WBks8TGecR4j6e5IDD1POkzZTvHv%2Bx8YILuydPNZ58io6w8ABVII4TySJvKIK&X-Amz-Signature=9f592b08d832d1c7ac6600368c7742b30d337e972b84e1d879a4a4a51fe8edba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TMICWVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIGGHX9oSeFpkbZjMCLovC7vjReKaGTpSapULlkBVqwtLAiEAxZq6O1Suyq%2FOZ6wI0Mfrtve4F%2FoxlVo0yh04Mf8IhMsq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDKym9gTBLi2gFu1elyrcA5SpUOYCLHCZLxS%2FKMzmzWyW90KkgKmE6hl76K9BOcMjdw9KgKcIaJ0QDtu%2BBm7wHq7cCtlr9AxtLXQV4K%2F6rmLTdErTP9qEw7MwmlHuMRgOHWZjKEKQs%2F0uPGfkVDyHAh%2BTD8AzvFhQpaRjoOvWW%2BXy6bbYR9rbhuf%2Blt9ZHycSLxMUPPLZ1d8pSGXT38DOVbXlD2HIo%2F69LngIH8HDVAuPDjH4SQHvjhBmFqjFFh9jsyD6%2Bi5u%2BU4OAaPpNhVq7Q0fUFM1oV79kSwQKfwtRP%2FVx3DYdlG03BO7V0E54484skUc72ewWvrqhEWTewK%2BjQKKrDPV0hbO72LA4azyvmZjPXT9GVrsRMjNxliYJp5QoHtAX5%2FWvSJBxvKBeKVW6RgpZojir82Z9hK5TnZ%2F1Kv73iHVq23ZgVjSWVCOQZZ6E3zUmEn4tIUkKMvMDyzCa1j0MS8i6qB2HldssijEtXW0Y5MLIUetDJFlvAAmB7BbjA27hxPzos3aNLhPCPCTXIOdOvfr70%2Fp8Y7zEbvbd0GKgYkPEahUm%2F5%2BbkFFpwnj0g%2BAE6Ju4E3jnZUgLVV9DMwOAyib%2BZYHHflWk8UA6Uix2D3e5gQ8%2BS0hezsi2JIPetaxBBs833dx3%2FZhMMf55LwGOqUB7OY%2F1KnAnBZFdli7l%2FPkqsL5%2FD%2FYbxqVTuTyPJe5gKfgPdvWGGzrRSdlWbZI16RbQgFLoWvNCdidFKm%2Bai1c0%2B9mOEUXmgs%2FRsEvrX9DO3yiSiys4rUb2Y8sr5HReGMtU4adXNipWTSR4zvhCxjaF%2FW52CPthe2WBks8TGecR4j6e5IDD1POkzZTvHv%2Bx8YILuydPNZ58io6w8ABVII4TySJvKIK&X-Amz-Signature=064498bba65c5fe11d539623164f57e697c601d06dddce35f927e24555e458ca&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TMICWVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIGGHX9oSeFpkbZjMCLovC7vjReKaGTpSapULlkBVqwtLAiEAxZq6O1Suyq%2FOZ6wI0Mfrtve4F%2FoxlVo0yh04Mf8IhMsq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDKym9gTBLi2gFu1elyrcA5SpUOYCLHCZLxS%2FKMzmzWyW90KkgKmE6hl76K9BOcMjdw9KgKcIaJ0QDtu%2BBm7wHq7cCtlr9AxtLXQV4K%2F6rmLTdErTP9qEw7MwmlHuMRgOHWZjKEKQs%2F0uPGfkVDyHAh%2BTD8AzvFhQpaRjoOvWW%2BXy6bbYR9rbhuf%2Blt9ZHycSLxMUPPLZ1d8pSGXT38DOVbXlD2HIo%2F69LngIH8HDVAuPDjH4SQHvjhBmFqjFFh9jsyD6%2Bi5u%2BU4OAaPpNhVq7Q0fUFM1oV79kSwQKfwtRP%2FVx3DYdlG03BO7V0E54484skUc72ewWvrqhEWTewK%2BjQKKrDPV0hbO72LA4azyvmZjPXT9GVrsRMjNxliYJp5QoHtAX5%2FWvSJBxvKBeKVW6RgpZojir82Z9hK5TnZ%2F1Kv73iHVq23ZgVjSWVCOQZZ6E3zUmEn4tIUkKMvMDyzCa1j0MS8i6qB2HldssijEtXW0Y5MLIUetDJFlvAAmB7BbjA27hxPzos3aNLhPCPCTXIOdOvfr70%2Fp8Y7zEbvbd0GKgYkPEahUm%2F5%2BbkFFpwnj0g%2BAE6Ju4E3jnZUgLVV9DMwOAyib%2BZYHHflWk8UA6Uix2D3e5gQ8%2BS0hezsi2JIPetaxBBs833dx3%2FZhMMf55LwGOqUB7OY%2F1KnAnBZFdli7l%2FPkqsL5%2FD%2FYbxqVTuTyPJe5gKfgPdvWGGzrRSdlWbZI16RbQgFLoWvNCdidFKm%2Bai1c0%2B9mOEUXmgs%2FRsEvrX9DO3yiSiys4rUb2Y8sr5HReGMtU4adXNipWTSR4zvhCxjaF%2FW52CPthe2WBks8TGecR4j6e5IDD1POkzZTvHv%2Bx8YILuydPNZ58io6w8ABVII4TySJvKIK&X-Amz-Signature=e0c98963cd89a7817eeef667f8748eb0de6708f4aa68fa4183da627a043ede35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OBPI7OU%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQD%2FYby87pINHuhvAEpRgFecEawuYux%2BNZrQuVfeaezt7QIhAN7HaWcrtdrkf6T2v6rOYa5bPq6NOeySr3fifg9PGIHVKv8DCH0QABoMNjM3NDIzMTgzODA1IgyyzBmU5yEUP6nppMAq3AOsKH97VOpZRvdwF881YzZ%2FHcMYLe8eQsIkFT1tEN1fxLNdpkj5afXoA5WVjvlRPROP9vrjLbaZ9FLfw5ZscoK69LoDhGqpQxC%2BdCVdJO0lK9g0jdYx7uQWS8UGoYxq3jquYBf9XF3Gh%2BKnQhJJdogNwyPlkna03YzBY3frjRy2R7hv9Vs9jYHmnfKQnPX9NekNqIVEpflMZP575LwlTFEPeakqP%2Fga8HAG1SgI4BFQFHM1Lv0SMchyPduy4hquwPM88ni%2BvZEIQ1KCAQ%2F58EKu7PUoUz9PxYaWGFDB5Gk2X3dAFTiV1R14kvYUB5YQxfzfM4qNCk%2BgCFNzleMRrU9f3cHJjIQX2344IVF9ul1bIqc%2BpGbIhnmhtAVdUeyBNN%2BRtNsXK%2F3rkLG9USvue%2BJZ%2B3cYs9mEvLMNqsuiJHau2JWdbASP%2FsSWCzKQ%2FRDFxOaNa2MJIvdk9X1mWtvZ2vNV58bJ8Oqtz9okC9wK0xjuq1U1pFgYi2dFQdxOZXBYI5uEToqazCdaBkYGYpYdjxChGxQtIDSt%2BRF5pVySKdhwRzNM9a5xWefYKmmr7pMr%2F3SVGg2tjNX8a5njTNxnf%2BzbExHaTrW6ZL9uphi%2FY8FsQl5tmAaUSZqxS2nIwzDS%2BeS8BjqkAf7c4gb7NP4HpzgscDKgliDj19356O%2B9Jp59HOFJwf6lNi0uaekmGvBnmVG8fKNPo25K8HGjSi15b4ujqUWFcp3b3P5g%2B2XvlrSZlfwrazfJ7VWJk88s5ORTkT0H7CHjYSjZfUGdchrDgJyiwnTyLn4BHgX3J7zIvUASBziVNVGRolsfdlUGebvtfHWwMfHP2jEP1VsMmQAx9dCJmKHEqrgwYXCk&X-Amz-Signature=f7f6c7bae43cfeadbe93d54411d541af206820b77a17a5d56d04dd0d953c71d6&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OBPI7OU%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQD%2FYby87pINHuhvAEpRgFecEawuYux%2BNZrQuVfeaezt7QIhAN7HaWcrtdrkf6T2v6rOYa5bPq6NOeySr3fifg9PGIHVKv8DCH0QABoMNjM3NDIzMTgzODA1IgyyzBmU5yEUP6nppMAq3AOsKH97VOpZRvdwF881YzZ%2FHcMYLe8eQsIkFT1tEN1fxLNdpkj5afXoA5WVjvlRPROP9vrjLbaZ9FLfw5ZscoK69LoDhGqpQxC%2BdCVdJO0lK9g0jdYx7uQWS8UGoYxq3jquYBf9XF3Gh%2BKnQhJJdogNwyPlkna03YzBY3frjRy2R7hv9Vs9jYHmnfKQnPX9NekNqIVEpflMZP575LwlTFEPeakqP%2Fga8HAG1SgI4BFQFHM1Lv0SMchyPduy4hquwPM88ni%2BvZEIQ1KCAQ%2F58EKu7PUoUz9PxYaWGFDB5Gk2X3dAFTiV1R14kvYUB5YQxfzfM4qNCk%2BgCFNzleMRrU9f3cHJjIQX2344IVF9ul1bIqc%2BpGbIhnmhtAVdUeyBNN%2BRtNsXK%2F3rkLG9USvue%2BJZ%2B3cYs9mEvLMNqsuiJHau2JWdbASP%2FsSWCzKQ%2FRDFxOaNa2MJIvdk9X1mWtvZ2vNV58bJ8Oqtz9okC9wK0xjuq1U1pFgYi2dFQdxOZXBYI5uEToqazCdaBkYGYpYdjxChGxQtIDSt%2BRF5pVySKdhwRzNM9a5xWefYKmmr7pMr%2F3SVGg2tjNX8a5njTNxnf%2BzbExHaTrW6ZL9uphi%2FY8FsQl5tmAaUSZqxS2nIwzDS%2BeS8BjqkAf7c4gb7NP4HpzgscDKgliDj19356O%2B9Jp59HOFJwf6lNi0uaekmGvBnmVG8fKNPo25K8HGjSi15b4ujqUWFcp3b3P5g%2B2XvlrSZlfwrazfJ7VWJk88s5ORTkT0H7CHjYSjZfUGdchrDgJyiwnTyLn4BHgX3J7zIvUASBziVNVGRolsfdlUGebvtfHWwMfHP2jEP1VsMmQAx9dCJmKHEqrgwYXCk&X-Amz-Signature=605a44c9b92acb0be0f424bad72f72565684f1a5f2b69776c7de2fd8264176d3&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OBPI7OU%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQD%2FYby87pINHuhvAEpRgFecEawuYux%2BNZrQuVfeaezt7QIhAN7HaWcrtdrkf6T2v6rOYa5bPq6NOeySr3fifg9PGIHVKv8DCH0QABoMNjM3NDIzMTgzODA1IgyyzBmU5yEUP6nppMAq3AOsKH97VOpZRvdwF881YzZ%2FHcMYLe8eQsIkFT1tEN1fxLNdpkj5afXoA5WVjvlRPROP9vrjLbaZ9FLfw5ZscoK69LoDhGqpQxC%2BdCVdJO0lK9g0jdYx7uQWS8UGoYxq3jquYBf9XF3Gh%2BKnQhJJdogNwyPlkna03YzBY3frjRy2R7hv9Vs9jYHmnfKQnPX9NekNqIVEpflMZP575LwlTFEPeakqP%2Fga8HAG1SgI4BFQFHM1Lv0SMchyPduy4hquwPM88ni%2BvZEIQ1KCAQ%2F58EKu7PUoUz9PxYaWGFDB5Gk2X3dAFTiV1R14kvYUB5YQxfzfM4qNCk%2BgCFNzleMRrU9f3cHJjIQX2344IVF9ul1bIqc%2BpGbIhnmhtAVdUeyBNN%2BRtNsXK%2F3rkLG9USvue%2BJZ%2B3cYs9mEvLMNqsuiJHau2JWdbASP%2FsSWCzKQ%2FRDFxOaNa2MJIvdk9X1mWtvZ2vNV58bJ8Oqtz9okC9wK0xjuq1U1pFgYi2dFQdxOZXBYI5uEToqazCdaBkYGYpYdjxChGxQtIDSt%2BRF5pVySKdhwRzNM9a5xWefYKmmr7pMr%2F3SVGg2tjNX8a5njTNxnf%2BzbExHaTrW6ZL9uphi%2FY8FsQl5tmAaUSZqxS2nIwzDS%2BeS8BjqkAf7c4gb7NP4HpzgscDKgliDj19356O%2B9Jp59HOFJwf6lNi0uaekmGvBnmVG8fKNPo25K8HGjSi15b4ujqUWFcp3b3P5g%2B2XvlrSZlfwrazfJ7VWJk88s5ORTkT0H7CHjYSjZfUGdchrDgJyiwnTyLn4BHgX3J7zIvUASBziVNVGRolsfdlUGebvtfHWwMfHP2jEP1VsMmQAx9dCJmKHEqrgwYXCk&X-Amz-Signature=7ab52639c5ff04e4c39dfbc4767c9e770c4d2a18389a0cd74735765f074c3f77&X-Amz-SignedHeaders=host&x-id=GetObject)
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

