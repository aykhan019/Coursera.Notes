

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0fa3b083-9d5c-4760-a35a-e329e27bc8a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOH2YVFO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCG8hefRpHc882k1ON7cVxYESjlkXNb36DlW2L70sUMmgIgDvQeCkzz7e%2FTtj7RblmNJpfWxRMnkQHqHhXiP6sfqlsq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKjqZvOx6jHggUpaRyrcA41bSoBagNZ5ggVXlK8sMxdDkpGm0smcLRX3PtJnFXtiaHjZOQVFPJfyzfhkrZpfRCbuV8COCrprtIQPTKbM8EQthcTCU4WzDdrAXF2iZAkWn%2BceJ587%2B6P4gPB5i8llKw78C5I1mTbcwW7r0BK6coy%2FZJV3EVjDOU7t%2BIRyUM5qgctHmwzRUmN7T61tUC0%2BkjnsDoOuF05QAtNCIyg0XOjb2fwFGFx1THn0C3PBizg%2BXEk5TSkJN0izv5eJ1dLAGFbcmaR%2FpLv2YXlDT0%2BbXQf4eP0zwV44MzQCAanJIQOHPGaOHEPZK2KleWwIrTE5Cb4RNo0vamU3sycUUyxJXDXUmlMwmVMEOR8O2BjvsZjcBMdwLEEt622DQMNLvJtH4%2BVsa5jtS1IenMIQDjKR0zIWwJJueF4chJv6OdtRuxmnZ6XXooPWofmxING%2BehYIwbwQl6XAekbV70P6EF9LsIbQUo%2BwNMH%2FzxHrU8IG11CYAPcv0cBk4sWRxDrBz%2BROqmucqWXUWC8PnDhTkdDHmnNwabC%2FOsh8Cn5tDDrdaACTIKsM9pCUb3ImZaPwI%2FbNWdTEdAL89FxLUGu9C2Uj15H9pY5%2FfxjQ%2FyntPP2sBTpCxF0GtmoChiuExuLAMPrOjL0GOqUBqu%2BWss7IRFbDdB3KIXNTP3lCevGNlQBUKUCqV5kxlar8ppc%2BLou4Al4ipQV7iUxijBWPKDxrziySaubEJT%2FZz1iMAS8vV4ywhFOCmqj83TyO7iRJqznGtWbjWhyOqp8nk%2BTJHXy0jv2NXtouhBdku6jkP8cHO04ENJdBMc0N8lGJn4OXaknR7x%2F5P10RrTRdvC9PnWtFz3Ex765ELcwmiaOnYtYl&X-Amz-Signature=e97a6f7092af9bf48667d3160c59e45a4764d15cb91496fdf01a6b1e1ae911ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/dcc48d7a-ddef-4556-8880-b765ffea5656/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOH2YVFO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCG8hefRpHc882k1ON7cVxYESjlkXNb36DlW2L70sUMmgIgDvQeCkzz7e%2FTtj7RblmNJpfWxRMnkQHqHhXiP6sfqlsq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKjqZvOx6jHggUpaRyrcA41bSoBagNZ5ggVXlK8sMxdDkpGm0smcLRX3PtJnFXtiaHjZOQVFPJfyzfhkrZpfRCbuV8COCrprtIQPTKbM8EQthcTCU4WzDdrAXF2iZAkWn%2BceJ587%2B6P4gPB5i8llKw78C5I1mTbcwW7r0BK6coy%2FZJV3EVjDOU7t%2BIRyUM5qgctHmwzRUmN7T61tUC0%2BkjnsDoOuF05QAtNCIyg0XOjb2fwFGFx1THn0C3PBizg%2BXEk5TSkJN0izv5eJ1dLAGFbcmaR%2FpLv2YXlDT0%2BbXQf4eP0zwV44MzQCAanJIQOHPGaOHEPZK2KleWwIrTE5Cb4RNo0vamU3sycUUyxJXDXUmlMwmVMEOR8O2BjvsZjcBMdwLEEt622DQMNLvJtH4%2BVsa5jtS1IenMIQDjKR0zIWwJJueF4chJv6OdtRuxmnZ6XXooPWofmxING%2BehYIwbwQl6XAekbV70P6EF9LsIbQUo%2BwNMH%2FzxHrU8IG11CYAPcv0cBk4sWRxDrBz%2BROqmucqWXUWC8PnDhTkdDHmnNwabC%2FOsh8Cn5tDDrdaACTIKsM9pCUb3ImZaPwI%2FbNWdTEdAL89FxLUGu9C2Uj15H9pY5%2FfxjQ%2FyntPP2sBTpCxF0GtmoChiuExuLAMPrOjL0GOqUBqu%2BWss7IRFbDdB3KIXNTP3lCevGNlQBUKUCqV5kxlar8ppc%2BLou4Al4ipQV7iUxijBWPKDxrziySaubEJT%2FZz1iMAS8vV4ywhFOCmqj83TyO7iRJqznGtWbjWhyOqp8nk%2BTJHXy0jv2NXtouhBdku6jkP8cHO04ENJdBMc0N8lGJn4OXaknR7x%2F5P10RrTRdvC9PnWtFz3Ex765ELcwmiaOnYtYl&X-Amz-Signature=33a31f0cdf3327b5c3a62bc3fcbcd6a5829efe5727bfaeffd200a1442f4cb689&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7c5736c8-35a4-49b8-9fb9-74d756a8b7b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOH2YVFO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCG8hefRpHc882k1ON7cVxYESjlkXNb36DlW2L70sUMmgIgDvQeCkzz7e%2FTtj7RblmNJpfWxRMnkQHqHhXiP6sfqlsq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKjqZvOx6jHggUpaRyrcA41bSoBagNZ5ggVXlK8sMxdDkpGm0smcLRX3PtJnFXtiaHjZOQVFPJfyzfhkrZpfRCbuV8COCrprtIQPTKbM8EQthcTCU4WzDdrAXF2iZAkWn%2BceJ587%2B6P4gPB5i8llKw78C5I1mTbcwW7r0BK6coy%2FZJV3EVjDOU7t%2BIRyUM5qgctHmwzRUmN7T61tUC0%2BkjnsDoOuF05QAtNCIyg0XOjb2fwFGFx1THn0C3PBizg%2BXEk5TSkJN0izv5eJ1dLAGFbcmaR%2FpLv2YXlDT0%2BbXQf4eP0zwV44MzQCAanJIQOHPGaOHEPZK2KleWwIrTE5Cb4RNo0vamU3sycUUyxJXDXUmlMwmVMEOR8O2BjvsZjcBMdwLEEt622DQMNLvJtH4%2BVsa5jtS1IenMIQDjKR0zIWwJJueF4chJv6OdtRuxmnZ6XXooPWofmxING%2BehYIwbwQl6XAekbV70P6EF9LsIbQUo%2BwNMH%2FzxHrU8IG11CYAPcv0cBk4sWRxDrBz%2BROqmucqWXUWC8PnDhTkdDHmnNwabC%2FOsh8Cn5tDDrdaACTIKsM9pCUb3ImZaPwI%2FbNWdTEdAL89FxLUGu9C2Uj15H9pY5%2FfxjQ%2FyntPP2sBTpCxF0GtmoChiuExuLAMPrOjL0GOqUBqu%2BWss7IRFbDdB3KIXNTP3lCevGNlQBUKUCqV5kxlar8ppc%2BLou4Al4ipQV7iUxijBWPKDxrziySaubEJT%2FZz1iMAS8vV4ywhFOCmqj83TyO7iRJqznGtWbjWhyOqp8nk%2BTJHXy0jv2NXtouhBdku6jkP8cHO04ENJdBMc0N8lGJn4OXaknR7x%2F5P10RrTRdvC9PnWtFz3Ex765ELcwmiaOnYtYl&X-Amz-Signature=e1ce6cd4c83450e0a5fe295f919b3bc06235bceecd53d8697dbe24c9797819cd&X-Amz-SignedHeaders=host&x-id=GetObject)
### 1.2 Multiple Linear Regression (MLR)
Multiple linear regression (MLR) extends SLR to include multiple predictor variables 
($ x1,x2, \ldots,xn $) to predict a continuous target variable ($ y $):
$$ y=b_0+b_1x_1+b_2x_2+...+bn_xn_y  $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/74364aba-71e9-4c9f-bbb9-b7e62620571b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOH2YVFO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCG8hefRpHc882k1ON7cVxYESjlkXNb36DlW2L70sUMmgIgDvQeCkzz7e%2FTtj7RblmNJpfWxRMnkQHqHhXiP6sfqlsq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKjqZvOx6jHggUpaRyrcA41bSoBagNZ5ggVXlK8sMxdDkpGm0smcLRX3PtJnFXtiaHjZOQVFPJfyzfhkrZpfRCbuV8COCrprtIQPTKbM8EQthcTCU4WzDdrAXF2iZAkWn%2BceJ587%2B6P4gPB5i8llKw78C5I1mTbcwW7r0BK6coy%2FZJV3EVjDOU7t%2BIRyUM5qgctHmwzRUmN7T61tUC0%2BkjnsDoOuF05QAtNCIyg0XOjb2fwFGFx1THn0C3PBizg%2BXEk5TSkJN0izv5eJ1dLAGFbcmaR%2FpLv2YXlDT0%2BbXQf4eP0zwV44MzQCAanJIQOHPGaOHEPZK2KleWwIrTE5Cb4RNo0vamU3sycUUyxJXDXUmlMwmVMEOR8O2BjvsZjcBMdwLEEt622DQMNLvJtH4%2BVsa5jtS1IenMIQDjKR0zIWwJJueF4chJv6OdtRuxmnZ6XXooPWofmxING%2BehYIwbwQl6XAekbV70P6EF9LsIbQUo%2BwNMH%2FzxHrU8IG11CYAPcv0cBk4sWRxDrBz%2BROqmucqWXUWC8PnDhTkdDHmnNwabC%2FOsh8Cn5tDDrdaACTIKsM9pCUb3ImZaPwI%2FbNWdTEdAL89FxLUGu9C2Uj15H9pY5%2FfxjQ%2FyntPP2sBTpCxF0GtmoChiuExuLAMPrOjL0GOqUBqu%2BWss7IRFbDdB3KIXNTP3lCevGNlQBUKUCqV5kxlar8ppc%2BLou4Al4ipQV7iUxijBWPKDxrziySaubEJT%2FZz1iMAS8vV4ywhFOCmqj83TyO7iRJqznGtWbjWhyOqp8nk%2BTJHXy0jv2NXtouhBdku6jkP8cHO04ENJdBMc0N8lGJn4OXaknR7x%2F5P10RrTRdvC9PnWtFz3Ex765ELcwmiaOnYtYl&X-Amz-Signature=def6de295c1db331d5dc1e3d182e4aca0b76d2c9b93bc5ac4466fcdf0c98944d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2469ceef-2ef8-43f5-8ce1-bd5b5d12a495/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOH2YVFO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCG8hefRpHc882k1ON7cVxYESjlkXNb36DlW2L70sUMmgIgDvQeCkzz7e%2FTtj7RblmNJpfWxRMnkQHqHhXiP6sfqlsq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKjqZvOx6jHggUpaRyrcA41bSoBagNZ5ggVXlK8sMxdDkpGm0smcLRX3PtJnFXtiaHjZOQVFPJfyzfhkrZpfRCbuV8COCrprtIQPTKbM8EQthcTCU4WzDdrAXF2iZAkWn%2BceJ587%2B6P4gPB5i8llKw78C5I1mTbcwW7r0BK6coy%2FZJV3EVjDOU7t%2BIRyUM5qgctHmwzRUmN7T61tUC0%2BkjnsDoOuF05QAtNCIyg0XOjb2fwFGFx1THn0C3PBizg%2BXEk5TSkJN0izv5eJ1dLAGFbcmaR%2FpLv2YXlDT0%2BbXQf4eP0zwV44MzQCAanJIQOHPGaOHEPZK2KleWwIrTE5Cb4RNo0vamU3sycUUyxJXDXUmlMwmVMEOR8O2BjvsZjcBMdwLEEt622DQMNLvJtH4%2BVsa5jtS1IenMIQDjKR0zIWwJJueF4chJv6OdtRuxmnZ6XXooPWofmxING%2BehYIwbwQl6XAekbV70P6EF9LsIbQUo%2BwNMH%2FzxHrU8IG11CYAPcv0cBk4sWRxDrBz%2BROqmucqWXUWC8PnDhTkdDHmnNwabC%2FOsh8Cn5tDDrdaACTIKsM9pCUb3ImZaPwI%2FbNWdTEdAL89FxLUGu9C2Uj15H9pY5%2FfxjQ%2FyntPP2sBTpCxF0GtmoChiuExuLAMPrOjL0GOqUBqu%2BWss7IRFbDdB3KIXNTP3lCevGNlQBUKUCqV5kxlar8ppc%2BLou4Al4ipQV7iUxijBWPKDxrziySaubEJT%2FZz1iMAS8vV4ywhFOCmqj83TyO7iRJqznGtWbjWhyOqp8nk%2BTJHXy0jv2NXtouhBdku6jkP8cHO04ENJdBMc0N8lGJn4OXaknR7x%2F5P10RrTRdvC9PnWtFz3Ex765ELcwmiaOnYtYl&X-Amz-Signature=25a7e97858208baf55cc18d3016333e2d06ca334ba97fe04b98b0570f2be5b29&X-Amz-SignedHeaders=host&x-id=GetObject)

In summary, SLR and MLR provide methods to model relationships between variables, helping predict outcomes based on data observations.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9dfa2a06-f57b-44f8-8e17-9cb0123300c1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOH2YVFO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCG8hefRpHc882k1ON7cVxYESjlkXNb36DlW2L70sUMmgIgDvQeCkzz7e%2FTtj7RblmNJpfWxRMnkQHqHhXiP6sfqlsq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKjqZvOx6jHggUpaRyrcA41bSoBagNZ5ggVXlK8sMxdDkpGm0smcLRX3PtJnFXtiaHjZOQVFPJfyzfhkrZpfRCbuV8COCrprtIQPTKbM8EQthcTCU4WzDdrAXF2iZAkWn%2BceJ587%2B6P4gPB5i8llKw78C5I1mTbcwW7r0BK6coy%2FZJV3EVjDOU7t%2BIRyUM5qgctHmwzRUmN7T61tUC0%2BkjnsDoOuF05QAtNCIyg0XOjb2fwFGFx1THn0C3PBizg%2BXEk5TSkJN0izv5eJ1dLAGFbcmaR%2FpLv2YXlDT0%2BbXQf4eP0zwV44MzQCAanJIQOHPGaOHEPZK2KleWwIrTE5Cb4RNo0vamU3sycUUyxJXDXUmlMwmVMEOR8O2BjvsZjcBMdwLEEt622DQMNLvJtH4%2BVsa5jtS1IenMIQDjKR0zIWwJJueF4chJv6OdtRuxmnZ6XXooPWofmxING%2BehYIwbwQl6XAekbV70P6EF9LsIbQUo%2BwNMH%2FzxHrU8IG11CYAPcv0cBk4sWRxDrBz%2BROqmucqWXUWC8PnDhTkdDHmnNwabC%2FOsh8Cn5tDDrdaACTIKsM9pCUb3ImZaPwI%2FbNWdTEdAL89FxLUGu9C2Uj15H9pY5%2FfxjQ%2FyntPP2sBTpCxF0GtmoChiuExuLAMPrOjL0GOqUBqu%2BWss7IRFbDdB3KIXNTP3lCevGNlQBUKUCqV5kxlar8ppc%2BLou4Al4ipQV7iUxijBWPKDxrziySaubEJT%2FZz1iMAS8vV4ywhFOCmqj83TyO7iRJqznGtWbjWhyOqp8nk%2BTJHXy0jv2NXtouhBdku6jkP8cHO04ENJdBMc0N8lGJn4OXaknR7x%2F5P10RrTRdvC9PnWtFz3Ex765ELcwmiaOnYtYl&X-Amz-Signature=9c587161606b7819a516abb31edfdb8252d1c01ce5086b1fd1d5ffdadc2bee32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/efc9c4a9-2fea-4b28-87e0-d9eb9e2462e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOH2YVFO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCG8hefRpHc882k1ON7cVxYESjlkXNb36DlW2L70sUMmgIgDvQeCkzz7e%2FTtj7RblmNJpfWxRMnkQHqHhXiP6sfqlsq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKjqZvOx6jHggUpaRyrcA41bSoBagNZ5ggVXlK8sMxdDkpGm0smcLRX3PtJnFXtiaHjZOQVFPJfyzfhkrZpfRCbuV8COCrprtIQPTKbM8EQthcTCU4WzDdrAXF2iZAkWn%2BceJ587%2B6P4gPB5i8llKw78C5I1mTbcwW7r0BK6coy%2FZJV3EVjDOU7t%2BIRyUM5qgctHmwzRUmN7T61tUC0%2BkjnsDoOuF05QAtNCIyg0XOjb2fwFGFx1THn0C3PBizg%2BXEk5TSkJN0izv5eJ1dLAGFbcmaR%2FpLv2YXlDT0%2BbXQf4eP0zwV44MzQCAanJIQOHPGaOHEPZK2KleWwIrTE5Cb4RNo0vamU3sycUUyxJXDXUmlMwmVMEOR8O2BjvsZjcBMdwLEEt622DQMNLvJtH4%2BVsa5jtS1IenMIQDjKR0zIWwJJueF4chJv6OdtRuxmnZ6XXooPWofmxING%2BehYIwbwQl6XAekbV70P6EF9LsIbQUo%2BwNMH%2FzxHrU8IG11CYAPcv0cBk4sWRxDrBz%2BROqmucqWXUWC8PnDhTkdDHmnNwabC%2FOsh8Cn5tDDrdaACTIKsM9pCUb3ImZaPwI%2FbNWdTEdAL89FxLUGu9C2Uj15H9pY5%2FfxjQ%2FyntPP2sBTpCxF0GtmoChiuExuLAMPrOjL0GOqUBqu%2BWss7IRFbDdB3KIXNTP3lCevGNlQBUKUCqV5kxlar8ppc%2BLou4Al4ipQV7iUxijBWPKDxrziySaubEJT%2FZz1iMAS8vV4ywhFOCmqj83TyO7iRJqznGtWbjWhyOqp8nk%2BTJHXy0jv2NXtouhBdku6jkP8cHO04ENJdBMc0N8lGJn4OXaknR7x%2F5P10RrTRdvC9PnWtFz3Ex765ELcwmiaOnYtYl&X-Amz-Signature=d1502137ea2639eaefd5ae105c4b99cf7e89b808beee458c7452eb92161e5209&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8865a7c4-6c3a-4eb0-9992-911cb30106fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOH2YVFO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCG8hefRpHc882k1ON7cVxYESjlkXNb36DlW2L70sUMmgIgDvQeCkzz7e%2FTtj7RblmNJpfWxRMnkQHqHhXiP6sfqlsq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKjqZvOx6jHggUpaRyrcA41bSoBagNZ5ggVXlK8sMxdDkpGm0smcLRX3PtJnFXtiaHjZOQVFPJfyzfhkrZpfRCbuV8COCrprtIQPTKbM8EQthcTCU4WzDdrAXF2iZAkWn%2BceJ587%2B6P4gPB5i8llKw78C5I1mTbcwW7r0BK6coy%2FZJV3EVjDOU7t%2BIRyUM5qgctHmwzRUmN7T61tUC0%2BkjnsDoOuF05QAtNCIyg0XOjb2fwFGFx1THn0C3PBizg%2BXEk5TSkJN0izv5eJ1dLAGFbcmaR%2FpLv2YXlDT0%2BbXQf4eP0zwV44MzQCAanJIQOHPGaOHEPZK2KleWwIrTE5Cb4RNo0vamU3sycUUyxJXDXUmlMwmVMEOR8O2BjvsZjcBMdwLEEt622DQMNLvJtH4%2BVsa5jtS1IenMIQDjKR0zIWwJJueF4chJv6OdtRuxmnZ6XXooPWofmxING%2BehYIwbwQl6XAekbV70P6EF9LsIbQUo%2BwNMH%2FzxHrU8IG11CYAPcv0cBk4sWRxDrBz%2BROqmucqWXUWC8PnDhTkdDHmnNwabC%2FOsh8Cn5tDDrdaACTIKsM9pCUb3ImZaPwI%2FbNWdTEdAL89FxLUGu9C2Uj15H9pY5%2FfxjQ%2FyntPP2sBTpCxF0GtmoChiuExuLAMPrOjL0GOqUBqu%2BWss7IRFbDdB3KIXNTP3lCevGNlQBUKUCqV5kxlar8ppc%2BLou4Al4ipQV7iUxijBWPKDxrziySaubEJT%2FZz1iMAS8vV4ywhFOCmqj83TyO7iRJqznGtWbjWhyOqp8nk%2BTJHXy0jv2NXtouhBdku6jkP8cHO04ENJdBMc0N8lGJn4OXaknR7x%2F5P10RrTRdvC9PnWtFz3Ex765ELcwmiaOnYtYl&X-Amz-Signature=35f22ab8b064f668371b0994eba5386eeb104db83e3b2b948625f835aae33f65&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1238ba33-ad66-4d1d-9992-f51741c0b69b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOH2YVFO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCG8hefRpHc882k1ON7cVxYESjlkXNb36DlW2L70sUMmgIgDvQeCkzz7e%2FTtj7RblmNJpfWxRMnkQHqHhXiP6sfqlsq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKjqZvOx6jHggUpaRyrcA41bSoBagNZ5ggVXlK8sMxdDkpGm0smcLRX3PtJnFXtiaHjZOQVFPJfyzfhkrZpfRCbuV8COCrprtIQPTKbM8EQthcTCU4WzDdrAXF2iZAkWn%2BceJ587%2B6P4gPB5i8llKw78C5I1mTbcwW7r0BK6coy%2FZJV3EVjDOU7t%2BIRyUM5qgctHmwzRUmN7T61tUC0%2BkjnsDoOuF05QAtNCIyg0XOjb2fwFGFx1THn0C3PBizg%2BXEk5TSkJN0izv5eJ1dLAGFbcmaR%2FpLv2YXlDT0%2BbXQf4eP0zwV44MzQCAanJIQOHPGaOHEPZK2KleWwIrTE5Cb4RNo0vamU3sycUUyxJXDXUmlMwmVMEOR8O2BjvsZjcBMdwLEEt622DQMNLvJtH4%2BVsa5jtS1IenMIQDjKR0zIWwJJueF4chJv6OdtRuxmnZ6XXooPWofmxING%2BehYIwbwQl6XAekbV70P6EF9LsIbQUo%2BwNMH%2FzxHrU8IG11CYAPcv0cBk4sWRxDrBz%2BROqmucqWXUWC8PnDhTkdDHmnNwabC%2FOsh8Cn5tDDrdaACTIKsM9pCUb3ImZaPwI%2FbNWdTEdAL89FxLUGu9C2Uj15H9pY5%2FfxjQ%2FyntPP2sBTpCxF0GtmoChiuExuLAMPrOjL0GOqUBqu%2BWss7IRFbDdB3KIXNTP3lCevGNlQBUKUCqV5kxlar8ppc%2BLou4Al4ipQV7iUxijBWPKDxrziySaubEJT%2FZz1iMAS8vV4ywhFOCmqj83TyO7iRJqznGtWbjWhyOqp8nk%2BTJHXy0jv2NXtouhBdku6jkP8cHO04ENJdBMc0N8lGJn4OXaknR7x%2F5P10RrTRdvC9PnWtFz3Ex765ELcwmiaOnYtYl&X-Amz-Signature=0f97b0567455aa1caae87e29ab1a8c47bcfb56d5214567b224113debaa3b6b82&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d5eed59c-92aa-4f87-88cf-1e131752a312/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOH2YVFO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCG8hefRpHc882k1ON7cVxYESjlkXNb36DlW2L70sUMmgIgDvQeCkzz7e%2FTtj7RblmNJpfWxRMnkQHqHhXiP6sfqlsq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKjqZvOx6jHggUpaRyrcA41bSoBagNZ5ggVXlK8sMxdDkpGm0smcLRX3PtJnFXtiaHjZOQVFPJfyzfhkrZpfRCbuV8COCrprtIQPTKbM8EQthcTCU4WzDdrAXF2iZAkWn%2BceJ587%2B6P4gPB5i8llKw78C5I1mTbcwW7r0BK6coy%2FZJV3EVjDOU7t%2BIRyUM5qgctHmwzRUmN7T61tUC0%2BkjnsDoOuF05QAtNCIyg0XOjb2fwFGFx1THn0C3PBizg%2BXEk5TSkJN0izv5eJ1dLAGFbcmaR%2FpLv2YXlDT0%2BbXQf4eP0zwV44MzQCAanJIQOHPGaOHEPZK2KleWwIrTE5Cb4RNo0vamU3sycUUyxJXDXUmlMwmVMEOR8O2BjvsZjcBMdwLEEt622DQMNLvJtH4%2BVsa5jtS1IenMIQDjKR0zIWwJJueF4chJv6OdtRuxmnZ6XXooPWofmxING%2BehYIwbwQl6XAekbV70P6EF9LsIbQUo%2BwNMH%2FzxHrU8IG11CYAPcv0cBk4sWRxDrBz%2BROqmucqWXUWC8PnDhTkdDHmnNwabC%2FOsh8Cn5tDDrdaACTIKsM9pCUb3ImZaPwI%2FbNWdTEdAL89FxLUGu9C2Uj15H9pY5%2FfxjQ%2FyntPP2sBTpCxF0GtmoChiuExuLAMPrOjL0GOqUBqu%2BWss7IRFbDdB3KIXNTP3lCevGNlQBUKUCqV5kxlar8ppc%2BLou4Al4ipQV7iUxijBWPKDxrziySaubEJT%2FZz1iMAS8vV4ywhFOCmqj83TyO7iRJqznGtWbjWhyOqp8nk%2BTJHXy0jv2NXtouhBdku6jkP8cHO04ENJdBMc0N8lGJn4OXaknR7x%2F5P10RrTRdvC9PnWtFz3Ex765ELcwmiaOnYtYl&X-Amz-Signature=41ef996d0943c2a45bb35ff7d448df256713d395c4b4f8b7035f6826d9985d98&X-Amz-SignedHeaders=host&x-id=GetObject)
**Observation**: Prices in range from 40,000 to 50,000 are inaccurate, while 10,000 to 20,000 are closer to target values.
___
## 3. Polynomial Regression and Pipelines
### Polynomial Regression
#### What is Polynomial Regression?
- **Purpose**: Used when linear regression isn't suitable.
- **Approach**: Transforms data into polynomial form to capture curvilinear relationships.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fefee895-81df-48b5-91f0-788641b6045e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QOH2YVFO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCG8hefRpHc882k1ON7cVxYESjlkXNb36DlW2L70sUMmgIgDvQeCkzz7e%2FTtj7RblmNJpfWxRMnkQHqHhXiP6sfqlsq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKjqZvOx6jHggUpaRyrcA41bSoBagNZ5ggVXlK8sMxdDkpGm0smcLRX3PtJnFXtiaHjZOQVFPJfyzfhkrZpfRCbuV8COCrprtIQPTKbM8EQthcTCU4WzDdrAXF2iZAkWn%2BceJ587%2B6P4gPB5i8llKw78C5I1mTbcwW7r0BK6coy%2FZJV3EVjDOU7t%2BIRyUM5qgctHmwzRUmN7T61tUC0%2BkjnsDoOuF05QAtNCIyg0XOjb2fwFGFx1THn0C3PBizg%2BXEk5TSkJN0izv5eJ1dLAGFbcmaR%2FpLv2YXlDT0%2BbXQf4eP0zwV44MzQCAanJIQOHPGaOHEPZK2KleWwIrTE5Cb4RNo0vamU3sycUUyxJXDXUmlMwmVMEOR8O2BjvsZjcBMdwLEEt622DQMNLvJtH4%2BVsa5jtS1IenMIQDjKR0zIWwJJueF4chJv6OdtRuxmnZ6XXooPWofmxING%2BehYIwbwQl6XAekbV70P6EF9LsIbQUo%2BwNMH%2FzxHrU8IG11CYAPcv0cBk4sWRxDrBz%2BROqmucqWXUWC8PnDhTkdDHmnNwabC%2FOsh8Cn5tDDrdaACTIKsM9pCUb3ImZaPwI%2FbNWdTEdAL89FxLUGu9C2Uj15H9pY5%2FfxjQ%2FyntPP2sBTpCxF0GtmoChiuExuLAMPrOjL0GOqUBqu%2BWss7IRFbDdB3KIXNTP3lCevGNlQBUKUCqV5kxlar8ppc%2BLou4Al4ipQV7iUxijBWPKDxrziySaubEJT%2FZz1iMAS8vV4ywhFOCmqj83TyO7iRJqznGtWbjWhyOqp8nk%2BTJHXy0jv2NXtouhBdku6jkP8cHO04ENJdBMc0N8lGJn4OXaknR7x%2F5P10RrTRdvC9PnWtFz3Ex765ELcwmiaOnYtYl&X-Amz-Signature=093f239ac438f6b3bf1c9934621e29f9b9dceebb0b0b656a1fc072e22ffbf25e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62869ea-d1f8-44c7-9aec-aa8514f03e4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNWHAGYI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDPU0pYYmNs9eeyGmgDpjOFCPD3dwd8nXe0H3ivrqogWAIgOi721tJTqcTp0QkqY3Qsl0WF5FjeT8QnZbdRSYhxqVEq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDPF1M%2F%2Bw5obN4%2BGAsCrcA7QiiCiJaS86ECeMkaKh482fTR0%2B%2FFWx9JdWOf0nanguJJe3jHkYgw%2FtlCh9txYYLD2HBo9L3T5i6VmzDKLt2N48eIVXOLzO%2B8un0WHHraUfVJi6OpKFy2pjRBeL27aqD0vVgbf%2Fwe12v96eRi3i68ha2ulYwq0G6Wh47Xy%2Ba74A1fX%2Fqld9HeW0N%2BKCYaFEBZH%2B2mcAcVqNWrP6imLFbf9lkRJPBKWkrgE3C28Y%2B1VekAsqZvsbT38raIFEsRZUJ61a%2Fp3LjecErvNAzBc8LKCLU0Vfv%2Fy3xM%2Ful5CQJ0R%2Bo92Lel8QRI3ZrTgq9nXjDpwjbpYGYmbjHaPA9MoUsadpT%2FMctau4F73dg13%2F1Pb%2FTMqbp9riwzupS1L72OKs5BqW94gGC%2F13%2FEbsz8wWCG1%2FkLBm79gQwZtpIw9goWEZ%2BJVJyAmvBpS0K5PO%2BzHBOXg1TJC%2Fv4NyCRaurWSPKeyUbCfLtLSV2CTG%2Br1pyhs4CldwJEoEcIXPArYu%2B1pTUU6s%2FijuBL8B1hJzUqCG3I1CidYY7nEGztEr28797NUnENCgrCCPh1BJCZzaDBh1Z5jl7IKBetbF0bQ0Xh9y5BcxgBXiQoCWnZaQN0xCZ1cflo61vYyVknvnhOwhML7PjL0GOqUBq%2F3IUdFI0KgNSR%2BfsuXNjv%2FRvSgiDOYlA5ccn25yzz8n4P%2F7wABwM1N7t2zoyEwpeM86yRmU24Q5fjPdVBQDRwZHBMhpopTAhcVvdRXYDIibM5D%2BfKF%2FFGVve1CI838ROUFQpI3lq96MMbCAHhvCbw9oQFdn5HSRnbd2n4jUa7YchM4uHyzFrLd2GSuGUZ%2B1GO90Os2%2FttYV9hsGStjTKYNceadj&X-Amz-Signature=e2c0dd1db5aebb3d1f7ec472ff78d1a12264010328fe6d96c12d107dceb66575&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f5a8ae27-cc45-4723-aa6a-c8dbc6527bdf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNWHAGYI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDPU0pYYmNs9eeyGmgDpjOFCPD3dwd8nXe0H3ivrqogWAIgOi721tJTqcTp0QkqY3Qsl0WF5FjeT8QnZbdRSYhxqVEq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDPF1M%2F%2Bw5obN4%2BGAsCrcA7QiiCiJaS86ECeMkaKh482fTR0%2B%2FFWx9JdWOf0nanguJJe3jHkYgw%2FtlCh9txYYLD2HBo9L3T5i6VmzDKLt2N48eIVXOLzO%2B8un0WHHraUfVJi6OpKFy2pjRBeL27aqD0vVgbf%2Fwe12v96eRi3i68ha2ulYwq0G6Wh47Xy%2Ba74A1fX%2Fqld9HeW0N%2BKCYaFEBZH%2B2mcAcVqNWrP6imLFbf9lkRJPBKWkrgE3C28Y%2B1VekAsqZvsbT38raIFEsRZUJ61a%2Fp3LjecErvNAzBc8LKCLU0Vfv%2Fy3xM%2Ful5CQJ0R%2Bo92Lel8QRI3ZrTgq9nXjDpwjbpYGYmbjHaPA9MoUsadpT%2FMctau4F73dg13%2F1Pb%2FTMqbp9riwzupS1L72OKs5BqW94gGC%2F13%2FEbsz8wWCG1%2FkLBm79gQwZtpIw9goWEZ%2BJVJyAmvBpS0K5PO%2BzHBOXg1TJC%2Fv4NyCRaurWSPKeyUbCfLtLSV2CTG%2Br1pyhs4CldwJEoEcIXPArYu%2B1pTUU6s%2FijuBL8B1hJzUqCG3I1CidYY7nEGztEr28797NUnENCgrCCPh1BJCZzaDBh1Z5jl7IKBetbF0bQ0Xh9y5BcxgBXiQoCWnZaQN0xCZ1cflo61vYyVknvnhOwhML7PjL0GOqUBq%2F3IUdFI0KgNSR%2BfsuXNjv%2FRvSgiDOYlA5ccn25yzz8n4P%2F7wABwM1N7t2zoyEwpeM86yRmU24Q5fjPdVBQDRwZHBMhpopTAhcVvdRXYDIibM5D%2BfKF%2FFGVve1CI838ROUFQpI3lq96MMbCAHhvCbw9oQFdn5HSRnbd2n4jUa7YchM4uHyzFrLd2GSuGUZ%2B1GO90Os2%2FttYV9hsGStjTKYNceadj&X-Amz-Signature=11ba9187e0b40bcc79ab1b296da9c634a54e5eef9bc813cd7c1d5eb496f0e9eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9a75a205-fac8-4bc5-9a37-0e919c9dae58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNWHAGYI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDPU0pYYmNs9eeyGmgDpjOFCPD3dwd8nXe0H3ivrqogWAIgOi721tJTqcTp0QkqY3Qsl0WF5FjeT8QnZbdRSYhxqVEq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDPF1M%2F%2Bw5obN4%2BGAsCrcA7QiiCiJaS86ECeMkaKh482fTR0%2B%2FFWx9JdWOf0nanguJJe3jHkYgw%2FtlCh9txYYLD2HBo9L3T5i6VmzDKLt2N48eIVXOLzO%2B8un0WHHraUfVJi6OpKFy2pjRBeL27aqD0vVgbf%2Fwe12v96eRi3i68ha2ulYwq0G6Wh47Xy%2Ba74A1fX%2Fqld9HeW0N%2BKCYaFEBZH%2B2mcAcVqNWrP6imLFbf9lkRJPBKWkrgE3C28Y%2B1VekAsqZvsbT38raIFEsRZUJ61a%2Fp3LjecErvNAzBc8LKCLU0Vfv%2Fy3xM%2Ful5CQJ0R%2Bo92Lel8QRI3ZrTgq9nXjDpwjbpYGYmbjHaPA9MoUsadpT%2FMctau4F73dg13%2F1Pb%2FTMqbp9riwzupS1L72OKs5BqW94gGC%2F13%2FEbsz8wWCG1%2FkLBm79gQwZtpIw9goWEZ%2BJVJyAmvBpS0K5PO%2BzHBOXg1TJC%2Fv4NyCRaurWSPKeyUbCfLtLSV2CTG%2Br1pyhs4CldwJEoEcIXPArYu%2B1pTUU6s%2FijuBL8B1hJzUqCG3I1CidYY7nEGztEr28797NUnENCgrCCPh1BJCZzaDBh1Z5jl7IKBetbF0bQ0Xh9y5BcxgBXiQoCWnZaQN0xCZ1cflo61vYyVknvnhOwhML7PjL0GOqUBq%2F3IUdFI0KgNSR%2BfsuXNjv%2FRvSgiDOYlA5ccn25yzz8n4P%2F7wABwM1N7t2zoyEwpeM86yRmU24Q5fjPdVBQDRwZHBMhpopTAhcVvdRXYDIibM5D%2BfKF%2FFGVve1CI838ROUFQpI3lq96MMbCAHhvCbw9oQFdn5HSRnbd2n4jUa7YchM4uHyzFrLd2GSuGUZ%2B1GO90Os2%2FttYV9hsGStjTKYNceadj&X-Amz-Signature=c91901a95e239befaab09dad02bd157144b19c51b448c8674c89bc10ad4b4d48&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## 5. Prediction and Decision Making
### Model Evaluation
To ensure a model's validity, use:
- **Visualization**: Plot data to check trends and anomalies.
- **Numerical Measures**: Metrics like MSE and R-squared.
- **Comparison**: Evaluate different models.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/1ed3169f-d09f-4aa9-bda2-6b975ae8b131/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNWHAGYI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDPU0pYYmNs9eeyGmgDpjOFCPD3dwd8nXe0H3ivrqogWAIgOi721tJTqcTp0QkqY3Qsl0WF5FjeT8QnZbdRSYhxqVEq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDPF1M%2F%2Bw5obN4%2BGAsCrcA7QiiCiJaS86ECeMkaKh482fTR0%2B%2FFWx9JdWOf0nanguJJe3jHkYgw%2FtlCh9txYYLD2HBo9L3T5i6VmzDKLt2N48eIVXOLzO%2B8un0WHHraUfVJi6OpKFy2pjRBeL27aqD0vVgbf%2Fwe12v96eRi3i68ha2ulYwq0G6Wh47Xy%2Ba74A1fX%2Fqld9HeW0N%2BKCYaFEBZH%2B2mcAcVqNWrP6imLFbf9lkRJPBKWkrgE3C28Y%2B1VekAsqZvsbT38raIFEsRZUJ61a%2Fp3LjecErvNAzBc8LKCLU0Vfv%2Fy3xM%2Ful5CQJ0R%2Bo92Lel8QRI3ZrTgq9nXjDpwjbpYGYmbjHaPA9MoUsadpT%2FMctau4F73dg13%2F1Pb%2FTMqbp9riwzupS1L72OKs5BqW94gGC%2F13%2FEbsz8wWCG1%2FkLBm79gQwZtpIw9goWEZ%2BJVJyAmvBpS0K5PO%2BzHBOXg1TJC%2Fv4NyCRaurWSPKeyUbCfLtLSV2CTG%2Br1pyhs4CldwJEoEcIXPArYu%2B1pTUU6s%2FijuBL8B1hJzUqCG3I1CidYY7nEGztEr28797NUnENCgrCCPh1BJCZzaDBh1Z5jl7IKBetbF0bQ0Xh9y5BcxgBXiQoCWnZaQN0xCZ1cflo61vYyVknvnhOwhML7PjL0GOqUBq%2F3IUdFI0KgNSR%2BfsuXNjv%2FRvSgiDOYlA5ccn25yzz8n4P%2F7wABwM1N7t2zoyEwpeM86yRmU24Q5fjPdVBQDRwZHBMhpopTAhcVvdRXYDIibM5D%2BfKF%2FFGVve1CI838ROUFQpI3lq96MMbCAHhvCbw9oQFdn5HSRnbd2n4jUa7YchM4uHyzFrLd2GSuGUZ%2B1GO90Os2%2FttYV9hsGStjTKYNceadj&X-Amz-Signature=4b409e4543460ff97c5957d88ecd4be287c1a9006b54772ca3bfb53f613c841e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f986486a-7f71-47fb-b7a9-99fe89631b3b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W5K3777%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDeQ5Xf8LKBRuT9idz8zEKpiS3JhVSuVfj27%2Fcoa3%2FSrgIgYImyUHBe0v2guTmni617khTJRql%2FJj6u%2Bxb3jKuEKeoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKcTod7vDHgUhrs7USrcAyW4%2B%2FKJxSoqgHD5qQZbsRDYJWvqLuWsGazib6tVdd%2FMwQMpoPIMY%2BagtUulorM2w%2By15lqWQhnM%2FymQM9P2XuU4zGY%2By73LHziDaYX%2FbmfZ6TkLutNYnsktRiQMquG7frltoEHu65IeBfIcooEwQw08KZAPZW%2Bc48nnmoqJxzLKuLx6XHuWErHA7R6iC4%2B%2BCxqhnT4VW1P66YiNhtz4GIFv%2FUsGvFruxTrK3SJT24yj%2Bohh%2Bx2ANijuV3UH2qVfOTl3QSpEe9QU2n9ZobDeA3D9W%2BpC%2BS67FCO9G3Fi%2FWe9DOsKlGL11pqR7zYRPPo8bpqP2iJWSmi2rYZfsWcg%2Fm0zekjMtyiAkTERk7CuK09dlnKPF8EkAvDcpvuw1ryl1T8J1leXyyNEbYGsWNGziBu51nWIKjomkzfG32ReajpbhfmPw3ZqsXYMmwVcAbrSTS%2FM9CGbEwCvrTTr7okPt9lBRvxRHuMtsuoOUttqp3cl%2FMg93hzxn6yw2N6GmU4GXvYnSAJY59Z8GCIemq1Qk58rkyMOLGlOIx9KyFytW2ZBS%2BCn1qww1BwIMoA6bZzEPdWkve2iRaNhtmFwQ%2Fr%2F7%2FDNt48hVllGXxhF8mM%2Bm7ZY9oUIQOTHnCWOANaEMJXPjL0GOqUBigqenOF7ru98UeKL%2FP8we04nvWsI5h%2BPg39m%2F4eezXqJK7GOt5ETFOpVCTQ3Us3At%2BB9goTJ6znEWLPDyyg5gtLVQr6M8My8%2BiD5Tzx%2FAvUprCL9AexlT1m5JkTK4Nr%2BiqZxsMwE1tQmRJYmRxQDVzUHSub87oRhm8X5bR2d7Brx7OeB9cyj8DEAFCLga8AYBfvS5Cnb6S14BL1NVUWcnCYj0mRo&X-Amz-Signature=bea982f305a91cac2986beaa660bd709aa1c4a1e103073d762610d9f1837cabe&X-Amz-SignedHeaders=host&x-id=GetObject)
- 12,870 (poor fit)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4f3ee92f-9d24-4aa2-a4c1-99dd746b3e26/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W5K3777%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDeQ5Xf8LKBRuT9idz8zEKpiS3JhVSuVfj27%2Fcoa3%2FSrgIgYImyUHBe0v2guTmni617khTJRql%2FJj6u%2Bxb3jKuEKeoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKcTod7vDHgUhrs7USrcAyW4%2B%2FKJxSoqgHD5qQZbsRDYJWvqLuWsGazib6tVdd%2FMwQMpoPIMY%2BagtUulorM2w%2By15lqWQhnM%2FymQM9P2XuU4zGY%2By73LHziDaYX%2FbmfZ6TkLutNYnsktRiQMquG7frltoEHu65IeBfIcooEwQw08KZAPZW%2Bc48nnmoqJxzLKuLx6XHuWErHA7R6iC4%2B%2BCxqhnT4VW1P66YiNhtz4GIFv%2FUsGvFruxTrK3SJT24yj%2Bohh%2Bx2ANijuV3UH2qVfOTl3QSpEe9QU2n9ZobDeA3D9W%2BpC%2BS67FCO9G3Fi%2FWe9DOsKlGL11pqR7zYRPPo8bpqP2iJWSmi2rYZfsWcg%2Fm0zekjMtyiAkTERk7CuK09dlnKPF8EkAvDcpvuw1ryl1T8J1leXyyNEbYGsWNGziBu51nWIKjomkzfG32ReajpbhfmPw3ZqsXYMmwVcAbrSTS%2FM9CGbEwCvrTTr7okPt9lBRvxRHuMtsuoOUttqp3cl%2FMg93hzxn6yw2N6GmU4GXvYnSAJY59Z8GCIemq1Qk58rkyMOLGlOIx9KyFytW2ZBS%2BCn1qww1BwIMoA6bZzEPdWkve2iRaNhtmFwQ%2Fr%2F7%2FDNt48hVllGXxhF8mM%2Bm7ZY9oUIQOTHnCWOANaEMJXPjL0GOqUBigqenOF7ru98UeKL%2FP8we04nvWsI5h%2BPg39m%2F4eezXqJK7GOt5ETFOpVCTQ3Us3At%2BB9goTJ6znEWLPDyyg5gtLVQr6M8My8%2BiD5Tzx%2FAvUprCL9AexlT1m5JkTK4Nr%2BiqZxsMwE1tQmRJYmRxQDVzUHSub87oRhm8X5bR2d7Brx7OeB9cyj8DEAFCLga8AYBfvS5Cnb6S14BL1NVUWcnCYj0mRo&X-Amz-Signature=e776d25c9242caa1bf4fb9898bf9f96d22f212aea3a06b52259610993cf2ed86&X-Amz-SignedHeaders=host&x-id=GetObject)

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9c93d33a-293b-48ea-a149-5cc33936fd0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W5K3777%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDeQ5Xf8LKBRuT9idz8zEKpiS3JhVSuVfj27%2Fcoa3%2FSrgIgYImyUHBe0v2guTmni617khTJRql%2FJj6u%2Bxb3jKuEKeoq%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDKcTod7vDHgUhrs7USrcAyW4%2B%2FKJxSoqgHD5qQZbsRDYJWvqLuWsGazib6tVdd%2FMwQMpoPIMY%2BagtUulorM2w%2By15lqWQhnM%2FymQM9P2XuU4zGY%2By73LHziDaYX%2FbmfZ6TkLutNYnsktRiQMquG7frltoEHu65IeBfIcooEwQw08KZAPZW%2Bc48nnmoqJxzLKuLx6XHuWErHA7R6iC4%2B%2BCxqhnT4VW1P66YiNhtz4GIFv%2FUsGvFruxTrK3SJT24yj%2Bohh%2Bx2ANijuV3UH2qVfOTl3QSpEe9QU2n9ZobDeA3D9W%2BpC%2BS67FCO9G3Fi%2FWe9DOsKlGL11pqR7zYRPPo8bpqP2iJWSmi2rYZfsWcg%2Fm0zekjMtyiAkTERk7CuK09dlnKPF8EkAvDcpvuw1ryl1T8J1leXyyNEbYGsWNGziBu51nWIKjomkzfG32ReajpbhfmPw3ZqsXYMmwVcAbrSTS%2FM9CGbEwCvrTTr7okPt9lBRvxRHuMtsuoOUttqp3cl%2FMg93hzxn6yw2N6GmU4GXvYnSAJY59Z8GCIemq1Qk58rkyMOLGlOIx9KyFytW2ZBS%2BCn1qww1BwIMoA6bZzEPdWkve2iRaNhtmFwQ%2Fr%2F7%2FDNt48hVllGXxhF8mM%2Bm7ZY9oUIQOTHnCWOANaEMJXPjL0GOqUBigqenOF7ru98UeKL%2FP8we04nvWsI5h%2BPg39m%2F4eezXqJK7GOt5ETFOpVCTQ3Us3At%2BB9goTJ6znEWLPDyyg5gtLVQr6M8My8%2BiD5Tzx%2FAvUprCL9AexlT1m5JkTK4Nr%2BiqZxsMwE1tQmRJYmRxQDVzUHSub87oRhm8X5bR2d7Brx7OeB9cyj8DEAFCLga8AYBfvS5Cnb6S14BL1NVUWcnCYj0mRo&X-Amz-Signature=e12fad73088c72a27bcb515f845210e165360df5b3557dde92f1a4f9e3abd60f&X-Amz-SignedHeaders=host&x-id=GetObject)
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

