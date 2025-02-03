

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5NSWJUT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDERF3XcCee0hxLDZfx9807%2BMDM3rKRBzrqFt11vA8RfgIgelPA%2Bz7eG3ZDSG3dXXLpT99WhH%2FUn%2FhRKeBuHvowwucq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJrPnjKd0falZNv6wyrcA%2B6SOHs%2Fy1uWUtM%2Byk1K%2FWkv5Mj98nIDUc%2BvVJyZ9mriN3goO03kE71nxs%2BJH8zJXoJW12zKbWRjV8MxvP70m7MmfljIFRS%2FoSHb7RHmqYQ9Io0vj1WziJOSt9E3UUuea%2Bqm9ZbY6aXV%2FP%2B80MfZNJYzizxGY5SAWi6fYrah4%2FjKKXD4JhxSNJsgN6ubcGeCYaOOIHFzmKa4UWUWR0n0rtLGNNo4qMBVMd5VIlhdc%2FvuSkKcxbrVxyjqOToWGFJZY6F%2BG6aD8xBzdHdV4oPdghjsx42nAQdOsMScptIwlT7DByKjZIk9uYxUJumMlycIriFRhDeZZhOwigCc%2F%2FlmLkNsbvNqMG6S2RdFOZl7pZnDFGmZwRjoYxWjnuDnLDpSlXmPtsWaqaOTRlCQx%2FrWjpymTU04qxJtvmCW6bZR9VU32VQMw8svuUpfbkTsgdkVYhyVOUWnk%2BIK0wWy1ZRorkUy8x4CVqsv3UTgfDeq1B62B3Gh3v64xZPb%2Fa7NZGx8yykrwO%2BFGSCMZU55sCisok%2BPiHiKUg2yKhR%2FoMV93gsvPU9AwA6bta%2BNbu57CI2%2F9bhCMAGfJeJCu%2Fq%2Fbyl7LZ0tToonA9pWFms77xfAYqSoW4xzykbTtcd1Ndx%2BMPHVgb0GOqUBGNyChotWJHInpeHBlaUBfingO8GfRpKsgp0tLPTshxMdx7W5%2F0RAdyR7PggGCprmfcBTQ0UVG8DvDrwM8BLgUQK1I%2FTf7RE7zir2rQxOYbtBRGHMgyqgnNTLtURzpwT%2BoJ%2BcVsmCIJWj8RsTwWIhe5mIw74%2FZoCInK4zxassn4cCrVBtGQuABjR%2F2FKadvXDJmm7pIBSJijvzGdZxJrgO8FxgI11&X-Amz-Signature=6d147eaa3d60642f176629744c26dc723e9ea8d75887d5f118fdb6cfa1e3ba2d&X-Amz-SignedHeaders=host&x-id=GetObject)
### Example Dataset
Consider a dataset related to CO2 emissions from different cars. The dataset includes:
- Engine size
- Number of cylinders
- Fuel consumption
- CO2 emission
#### Predictive Question
Given this dataset, is it possible to predict the CO2 emission of a car using other fields such as engine size or cylinders? → Yes
### Historical Data and Prediction
Assume there is historical data from different cars. The goal is to estimate the CO2 emission of a new or unknown car, such as the one in row 9, which hasn't been manufactured yet. Regression methods can be used to make this prediction.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5NSWJUT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDERF3XcCee0hxLDZfx9807%2BMDM3rKRBzrqFt11vA8RfgIgelPA%2Bz7eG3ZDSG3dXXLpT99WhH%2FUn%2FhRKeBuHvowwucq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJrPnjKd0falZNv6wyrcA%2B6SOHs%2Fy1uWUtM%2Byk1K%2FWkv5Mj98nIDUc%2BvVJyZ9mriN3goO03kE71nxs%2BJH8zJXoJW12zKbWRjV8MxvP70m7MmfljIFRS%2FoSHb7RHmqYQ9Io0vj1WziJOSt9E3UUuea%2Bqm9ZbY6aXV%2FP%2B80MfZNJYzizxGY5SAWi6fYrah4%2FjKKXD4JhxSNJsgN6ubcGeCYaOOIHFzmKa4UWUWR0n0rtLGNNo4qMBVMd5VIlhdc%2FvuSkKcxbrVxyjqOToWGFJZY6F%2BG6aD8xBzdHdV4oPdghjsx42nAQdOsMScptIwlT7DByKjZIk9uYxUJumMlycIriFRhDeZZhOwigCc%2F%2FlmLkNsbvNqMG6S2RdFOZl7pZnDFGmZwRjoYxWjnuDnLDpSlXmPtsWaqaOTRlCQx%2FrWjpymTU04qxJtvmCW6bZR9VU32VQMw8svuUpfbkTsgdkVYhyVOUWnk%2BIK0wWy1ZRorkUy8x4CVqsv3UTgfDeq1B62B3Gh3v64xZPb%2Fa7NZGx8yykrwO%2BFGSCMZU55sCisok%2BPiHiKUg2yKhR%2FoMV93gsvPU9AwA6bta%2BNbu57CI2%2F9bhCMAGfJeJCu%2Fq%2Fbyl7LZ0tToonA9pWFms77xfAYqSoW4xzykbTtcd1Ndx%2BMPHVgb0GOqUBGNyChotWJHInpeHBlaUBfingO8GfRpKsgp0tLPTshxMdx7W5%2F0RAdyR7PggGCprmfcBTQ0UVG8DvDrwM8BLgUQK1I%2FTf7RE7zir2rQxOYbtBRGHMgyqgnNTLtURzpwT%2BoJ%2BcVsmCIJWj8RsTwWIhe5mIw74%2FZoCInK4zxassn4cCrVBtGQuABjR%2F2FKadvXDJmm7pIBSJijvzGdZxJrgO8FxgI11&X-Amz-Signature=0f2d1e16189e5bcfdc4eb7b7aa87b58f0ae5604dd1d44e53f5424961b109c3fc&X-Amz-SignedHeaders=host&x-id=GetObject)
### Types of Variables in Regression
- **Dependent Variable (Y):** The state, target, or final goal to be predicted.
- **Independent Variables (X):** The causes or explanatory variables.
### Types of Regression Models
#### Simple Regression
- **Definition:** Uses one independent variable to estimate a dependent variable.
- **Example:** Predicting CO2 emission using the variable of engine size.
- **Nature:** Can be linear or non-linear based on the relationship between the independent and dependent variables.
#### Multiple Regression
- **Definition:** Uses more than one independent variable to estimate a dependent variable.
- **Example:** Predicting CO2 emission using engine size and the number of cylinders.
- **Nature:** Can be linear or non-linear depending on the relationship between the dependent and independent variables.
### Applications of Regression
#### Sales Forecasting
Predicting a salesperson's total yearly sales using independent variables such as age, education, and years of experience.
#### Psychology
Determining individual satisfaction based on demographic and psychological factors.
#### Real Estate
Predicting the price of a house based on its size, number of bedrooms, and other features.
#### Employment Income
Predicting employment income using variables such as hours of work, education, occupation, age, and years of experience.
#### Other Fields
Regression analysis is also useful in finance, healthcare, retail, and more.
### Conclusion
Regression analysis has numerous applications across various fields. It helps in estimating continuous values using historical data and independent variables. Various regression algorithms exist, each suited to specific conditions, providing a foundation for exploring different regression techniques.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5NSWJUT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDERF3XcCee0hxLDZfx9807%2BMDM3rKRBzrqFt11vA8RfgIgelPA%2Bz7eG3ZDSG3dXXLpT99WhH%2FUn%2FhRKeBuHvowwucq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJrPnjKd0falZNv6wyrcA%2B6SOHs%2Fy1uWUtM%2Byk1K%2FWkv5Mj98nIDUc%2BvVJyZ9mriN3goO03kE71nxs%2BJH8zJXoJW12zKbWRjV8MxvP70m7MmfljIFRS%2FoSHb7RHmqYQ9Io0vj1WziJOSt9E3UUuea%2Bqm9ZbY6aXV%2FP%2B80MfZNJYzizxGY5SAWi6fYrah4%2FjKKXD4JhxSNJsgN6ubcGeCYaOOIHFzmKa4UWUWR0n0rtLGNNo4qMBVMd5VIlhdc%2FvuSkKcxbrVxyjqOToWGFJZY6F%2BG6aD8xBzdHdV4oPdghjsx42nAQdOsMScptIwlT7DByKjZIk9uYxUJumMlycIriFRhDeZZhOwigCc%2F%2FlmLkNsbvNqMG6S2RdFOZl7pZnDFGmZwRjoYxWjnuDnLDpSlXmPtsWaqaOTRlCQx%2FrWjpymTU04qxJtvmCW6bZR9VU32VQMw8svuUpfbkTsgdkVYhyVOUWnk%2BIK0wWy1ZRorkUy8x4CVqsv3UTgfDeq1B62B3Gh3v64xZPb%2Fa7NZGx8yykrwO%2BFGSCMZU55sCisok%2BPiHiKUg2yKhR%2FoMV93gsvPU9AwA6bta%2BNbu57CI2%2F9bhCMAGfJeJCu%2Fq%2Fbyl7LZ0tToonA9pWFms77xfAYqSoW4xzykbTtcd1Ndx%2BMPHVgb0GOqUBGNyChotWJHInpeHBlaUBfingO8GfRpKsgp0tLPTshxMdx7W5%2F0RAdyR7PggGCprmfcBTQ0UVG8DvDrwM8BLgUQK1I%2FTf7RE7zir2rQxOYbtBRGHMgyqgnNTLtURzpwT%2BoJ%2BcVsmCIJWj8RsTwWIhe5mIw74%2FZoCInK4zxassn4cCrVBtGQuABjR%2F2FKadvXDJmm7pIBSJijvzGdZxJrgO8FxgI11&X-Amz-Signature=3bb75d468b54884d237b1cf1d923abebd117abf1e479530fd582bcc152dc4145&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## Introduction to Linear Regression
Linear regression is an effective method for predicting a continuous value using other variables. This introduction provides the necessary background to use linear regression effectively.
### Dataset Overview
Consider a dataset related to CO2 emissions of different cars. The dataset includes:
- Engine size
- Number of cylinders
- Fuel consumption
- CO2 emissions
The goal is to predict the CO2 emission of a car using another field, such as engine size. Linear regression can be used for this purpose.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5NSWJUT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDERF3XcCee0hxLDZfx9807%2BMDM3rKRBzrqFt11vA8RfgIgelPA%2Bz7eG3ZDSG3dXXLpT99WhH%2FUn%2FhRKeBuHvowwucq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJrPnjKd0falZNv6wyrcA%2B6SOHs%2Fy1uWUtM%2Byk1K%2FWkv5Mj98nIDUc%2BvVJyZ9mriN3goO03kE71nxs%2BJH8zJXoJW12zKbWRjV8MxvP70m7MmfljIFRS%2FoSHb7RHmqYQ9Io0vj1WziJOSt9E3UUuea%2Bqm9ZbY6aXV%2FP%2B80MfZNJYzizxGY5SAWi6fYrah4%2FjKKXD4JhxSNJsgN6ubcGeCYaOOIHFzmKa4UWUWR0n0rtLGNNo4qMBVMd5VIlhdc%2FvuSkKcxbrVxyjqOToWGFJZY6F%2BG6aD8xBzdHdV4oPdghjsx42nAQdOsMScptIwlT7DByKjZIk9uYxUJumMlycIriFRhDeZZhOwigCc%2F%2FlmLkNsbvNqMG6S2RdFOZl7pZnDFGmZwRjoYxWjnuDnLDpSlXmPtsWaqaOTRlCQx%2FrWjpymTU04qxJtvmCW6bZR9VU32VQMw8svuUpfbkTsgdkVYhyVOUWnk%2BIK0wWy1ZRorkUy8x4CVqsv3UTgfDeq1B62B3Gh3v64xZPb%2Fa7NZGx8yykrwO%2BFGSCMZU55sCisok%2BPiHiKUg2yKhR%2FoMV93gsvPU9AwA6bta%2BNbu57CI2%2F9bhCMAGfJeJCu%2Fq%2Fbyl7LZ0tToonA9pWFms77xfAYqSoW4xzykbTtcd1Ndx%2BMPHVgb0GOqUBGNyChotWJHInpeHBlaUBfingO8GfRpKsgp0tLPTshxMdx7W5%2F0RAdyR7PggGCprmfcBTQ0UVG8DvDrwM8BLgUQK1I%2FTf7RE7zir2rQxOYbtBRGHMgyqgnNTLtURzpwT%2BoJ%2BcVsmCIJWj8RsTwWIhe5mIw74%2FZoCInK4zxassn4cCrVBtGQuABjR%2F2FKadvXDJmm7pIBSJijvzGdZxJrgO8FxgI11&X-Amz-Signature=529a5b1ac70029876e01c6d0915d7ea44809151f3a09566e7641623865cb3343&X-Amz-SignedHeaders=host&x-id=GetObject)
### Linear Regression Basics
Linear regression is the approximation of a linear model to describe the relationship between two or more variables.
#### Variables in Linear Regression
- **Dependent Variable (Y):** The continuous value being predicted.
- **Independent Variable (X):** The explanatory variable(s), which can be categorical or continuous.
#### Types of Linear Regression
1. **Simple Linear Regression:**
	- Uses one independent variable to estimate a dependent variable.
	- Example: Predicting CO2 emission using engine size.
2. **Multiple Linear Regression:**
	- Uses more than one independent variable to estimate a dependent variable.
	- Example: Predicting CO2 emission using engine size and number of cylinders.
### How Linear Regression Works
#### Scatter Plot
A scatter plot can be used to visualize the relationship between variables, such as engine size (independent variable) and CO2 emission (dependent variable). The plot helps to identify if the variables are linearly related.
#### Fitting a Line
Linear regression fits a line through the data points. For example, as the engine size increases, the CO2 emissions also increase. The objective is to find a line that best fits the data, which can be used to predict CO2 emissions.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5NSWJUT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDERF3XcCee0hxLDZfx9807%2BMDM3rKRBzrqFt11vA8RfgIgelPA%2Bz7eG3ZDSG3dXXLpT99WhH%2FUn%2FhRKeBuHvowwucq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJrPnjKd0falZNv6wyrcA%2B6SOHs%2Fy1uWUtM%2Byk1K%2FWkv5Mj98nIDUc%2BvVJyZ9mriN3goO03kE71nxs%2BJH8zJXoJW12zKbWRjV8MxvP70m7MmfljIFRS%2FoSHb7RHmqYQ9Io0vj1WziJOSt9E3UUuea%2Bqm9ZbY6aXV%2FP%2B80MfZNJYzizxGY5SAWi6fYrah4%2FjKKXD4JhxSNJsgN6ubcGeCYaOOIHFzmKa4UWUWR0n0rtLGNNo4qMBVMd5VIlhdc%2FvuSkKcxbrVxyjqOToWGFJZY6F%2BG6aD8xBzdHdV4oPdghjsx42nAQdOsMScptIwlT7DByKjZIk9uYxUJumMlycIriFRhDeZZhOwigCc%2F%2FlmLkNsbvNqMG6S2RdFOZl7pZnDFGmZwRjoYxWjnuDnLDpSlXmPtsWaqaOTRlCQx%2FrWjpymTU04qxJtvmCW6bZR9VU32VQMw8svuUpfbkTsgdkVYhyVOUWnk%2BIK0wWy1ZRorkUy8x4CVqsv3UTgfDeq1B62B3Gh3v64xZPb%2Fa7NZGx8yykrwO%2BFGSCMZU55sCisok%2BPiHiKUg2yKhR%2FoMV93gsvPU9AwA6bta%2BNbu57CI2%2F9bhCMAGfJeJCu%2Fq%2Fbyl7LZ0tToonA9pWFms77xfAYqSoW4xzykbTtcd1Ndx%2BMPHVgb0GOqUBGNyChotWJHInpeHBlaUBfingO8GfRpKsgp0tLPTshxMdx7W5%2F0RAdyR7PggGCprmfcBTQ0UVG8DvDrwM8BLgUQK1I%2FTf7RE7zir2rQxOYbtBRGHMgyqgnNTLtURzpwT%2BoJ%2BcVsmCIJWj8RsTwWIhe5mIw74%2FZoCInK4zxassn4cCrVBtGQuABjR%2F2FKadvXDJmm7pIBSJijvzGdZxJrgO8FxgI11&X-Amz-Signature=8f31f4bec205a16d806946a5c979a4bc58b368f78aea116834ce7125075649d4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5NSWJUT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDERF3XcCee0hxLDZfx9807%2BMDM3rKRBzrqFt11vA8RfgIgelPA%2Bz7eG3ZDSG3dXXLpT99WhH%2FUn%2FhRKeBuHvowwucq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJrPnjKd0falZNv6wyrcA%2B6SOHs%2Fy1uWUtM%2Byk1K%2FWkv5Mj98nIDUc%2BvVJyZ9mriN3goO03kE71nxs%2BJH8zJXoJW12zKbWRjV8MxvP70m7MmfljIFRS%2FoSHb7RHmqYQ9Io0vj1WziJOSt9E3UUuea%2Bqm9ZbY6aXV%2FP%2B80MfZNJYzizxGY5SAWi6fYrah4%2FjKKXD4JhxSNJsgN6ubcGeCYaOOIHFzmKa4UWUWR0n0rtLGNNo4qMBVMd5VIlhdc%2FvuSkKcxbrVxyjqOToWGFJZY6F%2BG6aD8xBzdHdV4oPdghjsx42nAQdOsMScptIwlT7DByKjZIk9uYxUJumMlycIriFRhDeZZhOwigCc%2F%2FlmLkNsbvNqMG6S2RdFOZl7pZnDFGmZwRjoYxWjnuDnLDpSlXmPtsWaqaOTRlCQx%2FrWjpymTU04qxJtvmCW6bZR9VU32VQMw8svuUpfbkTsgdkVYhyVOUWnk%2BIK0wWy1ZRorkUy8x4CVqsv3UTgfDeq1B62B3Gh3v64xZPb%2Fa7NZGx8yykrwO%2BFGSCMZU55sCisok%2BPiHiKUg2yKhR%2FoMV93gsvPU9AwA6bta%2BNbu57CI2%2F9bhCMAGfJeJCu%2Fq%2Fbyl7LZ0tToonA9pWFms77xfAYqSoW4xzykbTtcd1Ndx%2BMPHVgb0GOqUBGNyChotWJHInpeHBlaUBfingO8GfRpKsgp0tLPTshxMdx7W5%2F0RAdyR7PggGCprmfcBTQ0UVG8DvDrwM8BLgUQK1I%2FTf7RE7zir2rQxOYbtBRGHMgyqgnNTLtURzpwT%2BoJ%2BcVsmCIJWj8RsTwWIhe5mIw74%2FZoCInK4zxassn4cCrVBtGQuABjR%2F2FKadvXDJmm7pIBSJijvzGdZxJrgO8FxgI11&X-Amz-Signature=fa387c9ddfa100e3878bbefc1a5a75ef9875cefd35b06beef86d61409ce336aa&X-Amz-SignedHeaders=host&x-id=GetObject)
### Mathematical Representation
The fitted line in linear regression is represented as a polynomial. For a simple linear regression with one independent variable , the model is:
$ \hat{y} = \theta_0 + \theta_1 x_1 $
- $ \hat{y} $: Predicted value (dependent variable)
- $ x_1 $: Independent variable
- $ \theta_0 $: Intercept
- $ \theta_1 $: Slope or gradient of the line
#### Estimating Coefficients
- $ \theta_0 $ (intercept) and $ θ_1 $ (slope) are the parameters of the line that need to be adjusted to minimize the error.
- The goal is to minimize the mean squared error (MSE), which is the mean of all residual errors (the distance from data points to the fitted line).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5NSWJUT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDERF3XcCee0hxLDZfx9807%2BMDM3rKRBzrqFt11vA8RfgIgelPA%2Bz7eG3ZDSG3dXXLpT99WhH%2FUn%2FhRKeBuHvowwucq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJrPnjKd0falZNv6wyrcA%2B6SOHs%2Fy1uWUtM%2Byk1K%2FWkv5Mj98nIDUc%2BvVJyZ9mriN3goO03kE71nxs%2BJH8zJXoJW12zKbWRjV8MxvP70m7MmfljIFRS%2FoSHb7RHmqYQ9Io0vj1WziJOSt9E3UUuea%2Bqm9ZbY6aXV%2FP%2B80MfZNJYzizxGY5SAWi6fYrah4%2FjKKXD4JhxSNJsgN6ubcGeCYaOOIHFzmKa4UWUWR0n0rtLGNNo4qMBVMd5VIlhdc%2FvuSkKcxbrVxyjqOToWGFJZY6F%2BG6aD8xBzdHdV4oPdghjsx42nAQdOsMScptIwlT7DByKjZIk9uYxUJumMlycIriFRhDeZZhOwigCc%2F%2FlmLkNsbvNqMG6S2RdFOZl7pZnDFGmZwRjoYxWjnuDnLDpSlXmPtsWaqaOTRlCQx%2FrWjpymTU04qxJtvmCW6bZR9VU32VQMw8svuUpfbkTsgdkVYhyVOUWnk%2BIK0wWy1ZRorkUy8x4CVqsv3UTgfDeq1B62B3Gh3v64xZPb%2Fa7NZGx8yykrwO%2BFGSCMZU55sCisok%2BPiHiKUg2yKhR%2FoMV93gsvPU9AwA6bta%2BNbu57CI2%2F9bhCMAGfJeJCu%2Fq%2Fbyl7LZ0tToonA9pWFms77xfAYqSoW4xzykbTtcd1Ndx%2BMPHVgb0GOqUBGNyChotWJHInpeHBlaUBfingO8GfRpKsgp0tLPTshxMdx7W5%2F0RAdyR7PggGCprmfcBTQ0UVG8DvDrwM8BLgUQK1I%2FTf7RE7zir2rQxOYbtBRGHMgyqgnNTLtURzpwT%2BoJ%2BcVsmCIJWj8RsTwWIhe5mIw74%2FZoCInK4zxassn4cCrVBtGQuABjR%2F2FKadvXDJmm7pIBSJijvzGdZxJrgO8FxgI11&X-Amz-Signature=6cfdbebcc19568b798badb44303e03da1110e3dace9efee1bfd5fd5a83aad20e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5NSWJUT%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDERF3XcCee0hxLDZfx9807%2BMDM3rKRBzrqFt11vA8RfgIgelPA%2Bz7eG3ZDSG3dXXLpT99WhH%2FUn%2FhRKeBuHvowwucq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDJrPnjKd0falZNv6wyrcA%2B6SOHs%2Fy1uWUtM%2Byk1K%2FWkv5Mj98nIDUc%2BvVJyZ9mriN3goO03kE71nxs%2BJH8zJXoJW12zKbWRjV8MxvP70m7MmfljIFRS%2FoSHb7RHmqYQ9Io0vj1WziJOSt9E3UUuea%2Bqm9ZbY6aXV%2FP%2B80MfZNJYzizxGY5SAWi6fYrah4%2FjKKXD4JhxSNJsgN6ubcGeCYaOOIHFzmKa4UWUWR0n0rtLGNNo4qMBVMd5VIlhdc%2FvuSkKcxbrVxyjqOToWGFJZY6F%2BG6aD8xBzdHdV4oPdghjsx42nAQdOsMScptIwlT7DByKjZIk9uYxUJumMlycIriFRhDeZZhOwigCc%2F%2FlmLkNsbvNqMG6S2RdFOZl7pZnDFGmZwRjoYxWjnuDnLDpSlXmPtsWaqaOTRlCQx%2FrWjpymTU04qxJtvmCW6bZR9VU32VQMw8svuUpfbkTsgdkVYhyVOUWnk%2BIK0wWy1ZRorkUy8x4CVqsv3UTgfDeq1B62B3Gh3v64xZPb%2Fa7NZGx8yykrwO%2BFGSCMZU55sCisok%2BPiHiKUg2yKhR%2FoMV93gsvPU9AwA6bta%2BNbu57CI2%2F9bhCMAGfJeJCu%2Fq%2Fbyl7LZ0tToonA9pWFms77xfAYqSoW4xzykbTtcd1Ndx%2BMPHVgb0GOqUBGNyChotWJHInpeHBlaUBfingO8GfRpKsgp0tLPTshxMdx7W5%2F0RAdyR7PggGCprmfcBTQ0UVG8DvDrwM8BLgUQK1I%2FTf7RE7zir2rQxOYbtBRGHMgyqgnNTLtURzpwT%2BoJ%2BcVsmCIJWj8RsTwWIhe5mIw74%2FZoCInK4zxassn4cCrVBtGQuABjR%2F2FKadvXDJmm7pIBSJijvzGdZxJrgO8FxgI11&X-Amz-Signature=96363c608aa65994a944e42ca07069e74b66626c016d2f9b1e67820d280cb4b0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Example Calculation
For a dataset with known values:
- If $ θ_1 $= 43.98 and $  θ_0 $ = 92.94, the linear model is:
$$ CO2Emission=92.94+43.98×EngineSize $$
#### Prediction Example
For a car with an engine size of 2.4:
$$ CO2Emission=92.94+43.98×2.4=198.492 $$
### Why Linear Regression is Useful
- **Simplicity:** Easy to use and understand.
- **Speed:** Fast and efficient.
- **No Parameter Tuning:** Does not require parameter tuning like other algorithms (e.g., k-nearest neighbors, neural networks).
- **Interpretability:** Highly interpretable and provides clear insights into relationships between variables.
___

## Model Evaluation in Regression
Model evaluation in regression aims to assess how well a model can predict unknown data. Two main evaluation approaches are commonly used: train and test on the same dataset, and train/test split. Additionally, K-fold cross-validation is introduced as a more advanced method to address some limitations of the other two approaches.
### Evaluation Approaches
6. **Train and Test on the Same Dataset:**
	- **Process:**
		- Use the entire dataset to train the model.
		- Select a portion of the dataset as the test set (without labels during prediction).
		- Predict target values using the model.
		- Compare predicted values with actual values to calculate accuracy.
	- **Metrics:**
		- Compare actual values y with predicted values $ \hat{y} $.
		- Calculate the error as the average difference between predicted and actual values.
	- **Advantages:**
		- Simple and straightforward.
	- **Disadvantages:**
		- High training accuracy but low out-of-sample accuracy due to overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDAZGJFR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMTfU16LcmM98WgeOlvEntAAl3V3y531HcEz9dLoI%2BFgIhAKfk8mIhlg8pP8CLzJzPtBbClk6x6XqJp9k9%2Fnuj%2BZDnKv8DCBAQABoMNjM3NDIzMTgzODA1Igw4e2IbGJCGEdJiD%2BEq3AN1jsr8vlxczaZPb%2BE%2FKkJwuGgJ%2B5bWe9PeP%2BrEZW9YUhth71JdOIMxdPVCoLGTli07IqfKIN0voJ3OSRgJ%2F5AXO4pAWVjP%2Bm7xKf6X9sio4Mn0sl9KTHwh63ikunmKHB%2Bm1Im4Xd23aR%2FGCVcS1OYJxURte9mv%2BAAYnFsNI8DhD7wYubz8Rqq5okCdzJ4u%2BMYMDpx%2F2lTrkBbrpLhj1pSU7Vqjf4ew0vkIs6%2FA6L8ynTgFa2KkuF4eep%2BjQX752xc%2FBbvpXq9HD%2Bp44OG9AaeyZhupt%2F8mSZmgb1Iy56HVNN3Sv%2FvMSHexRWLOLNwrRlwze%2B9T2jNhKZJDYJSg9asTwXqG4QIUzQeBXrt2etHZLPlnJybMOm8XN6Ld9yANFK%2Bpgjqrla7Kkk6s8LUFMMczHrwWMEez25KodUA8OSzE5k%2B6m%2BuoH5eLC6NeDrb2%2BuRtP3wo0SIV7c65bUXXQg2s7zVTUvNXuQPWNYYOvnO6mGTpK1yDrs8Z0TqZ2g3vdjNh8%2Bx%2Fc9zxUPeGxWU%2BYemVMkL1FHp%2Bqg20mH%2FVq%2FsTfpRXjfGK%2F663LT0hW8fFR4OpXgfGcn6Kk4XzHY8kGa%2FRCtfvUQJMiI27cPQEknegqyjQt3JTD0MFGa4RlzC71oG9BjqkAYZLUq9Uvx5SaScdfyaJpkncUhNx15Ya2ldBbAKfNH5fBu42Ow8JoKmUxwsZ%2BgzweT5iNrYIhgQ56xsO0ayqCdFlbDOE73k4ixab5Grc63sd5IJqqOOsQmb%2FMY2%2FXKeUyXsRtblMk52kpdrj63PX9ue12BVf1EMxfQloCERKIie5BzrPsmQpactstPR6PSYTCizfHlDFc02HuIgy8I0sQ1EnBbC%2F&X-Amz-Signature=8672df6eff3ab19e4bd02197db173c7c8a708803fea1ebba4ba29420fd1d64d3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# Predict on the same dataset
predictions = model.predict(X)

# Calculate training accuracy (MSE)
mse = mean_squared_error(y, predictions)
print(f'Mean Squared Error: {mse}')
```
7. **Train/Test Split:**
	- **Process:**
		- Split the dataset into training and testing sets (mutually exclusive).
		- Train the model on the training set.
		- Test the model on the test set by predicting target values.
		- Compare predicted values with actual values to calculate accuracy.
	- **Advantages:**
		- Provides a better evaluation of out-of-sample accuracy.
		- More realistic for real-world problems.
	- **Disadvantages:**
		- Dependent on the specific split of the dataset, which can introduce variation.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQG2W4NK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID2YBqMPXaFhSOPhc4qcBJdVNGSFDHs9W%2BddZK0JdQkuAiBSV5ont0jjUpqLSAsqNLk7uZNjmYACzcAxG9WU1VTOvSr%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMY9WHPNHIs%2B84g%2FXTKtwDNe744bsrrSUawG6rxUl2%2BJsK8o8%2FgF7a5McYpCWYQTkNsLLlNHEW98nE0%2F5DE1wG4dvnzXorYnqIRoeOcKfjfsxt5Y7wTkCg7gzo%2BOH4cIvLMb2OjFIgbutk5wlJK2Z7LyUfuQwCw%2BhB58rdbDlK8POeJOfFiDWctTUBIF8hMpp74IBhDos1b1lssX8YnoqEtN264wWnYGIYoCMZqz9fYgVKubxrqtaNk%2Fpjd%2BNbr%2Bxu69C0Wv7PrChIwOijzr%2BO1NRVCMOg0CbFft1MbNjZKsFACDQjvr8Au6B8dkNoYXOQaQed7FZEe8ZNCGBdymLOzq2VrPSwVZG%2Fv9ZRErloXYwXjwNmCB8WsbcCZk3jFsmR2LxMq8zTB1XcewU2boUyXFPtvMRPNJbZMdcMGb4nJXA3yhHZnV%2BjE8MpLOZimesOW4QtOlNcyZn7d5FcTVo%2FDZVEfVp7IoVOXRFn8zNG2dDtNhTBdh9sSmGeXbcYm7DloCubXpTeRcbWydR%2FCpRG1iwBDSU7XgVO3j1vrglZRYgjGZtTpGKj8A5BE%2FAuDmShCUK2mpDLkF2XMQv1BmAP14M%2B4LwwPE%2Fel0AhPrcnX5ybJmbw%2F0SxBLzfjFynOD4wo2WswwRlL0h6TgowvdaBvQY6pgH46D%2BuZXsWgdihdalcmADNS0iIdvjnluUHy%2FOCgiTpwMniZGvskvo3tfPGNiWGaWL1yBLbTgBW3Dt7UQrT6VqFtjg4CqsSp%2Bzk%2F4YM%2FwfU%2B8XYXKaJwdLIRurxXEXTN86lv7v%2FzbZRjFD6bBijPxz9eSGBuSPqYOxd6i6pF%2BfXRf%2B95TkEjamnWO3kmU6v%2Fv35Dz5sax4uNjTDR%2BNBTQt6UAsOYd%2BO&X-Amz-Signature=2ae19e5afd65fb2db08588d16d9558fd8a7ffbaac35ed096e3832fff2ac1a9ff&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.model_selection import train_test_split

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Test the model on the test set
predictions = model.predict(X_test)

# Calculate out-of-sample accuracy (MSE)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error on Test Set: {mse}')
```
### Key Concepts
- **Training Accuracy:** The percentage of correct predictions the model makes on the training dataset. High training accuracy may indicate overfitting.
- **Out-of-Sample Accuracy:** The percentage of correct predictions the model makes on data it has not been trained on. High out-of-sample accuracy indicates better generalization to new data.
### K-Fold Cross-Validation
K-fold cross-validation is a method to address the dependency and variation issues in the train/test split approach. It provides a more consistent measure of out-of-sample accuracy by performing multiple train/test splits.
- **Process:**
	- Divide the dataset into  equal folds.
	- For each fold:
		- Use one fold as the test set and the remaining $ K−1 $ folds as the training set.
		- Train the model on the training set and evaluate it on the test set.
	- Repeat the process for each fold.
	- Average the accuracy results from all folds to obtain a final evaluation metric.
**Example with **$ K=4 $
- Split the dataset into 4 equal parts.
- In each iteration, use a different part as the test set and the rest as the training set.
- Compute accuracy for each fold and average the results.
**Advantages of K-Fold Cross-Validation:**
- Reduces the dependency on a specific train/test split.
- Provides a more reliable estimate of out-of-sample accuracy.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JS5RBVV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdfX7bE%2FtZoawE%2BS3fynALoxxFwzkKzYnqihNMTAT%2BewIgTz8FaPCZaiqxMS4nk8pz1cYETLJjzsvDIyA6yU4o07kq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDCTiiQRFDC2u32XtYircA5VlrvRFyWQcFyO9AHbnluOALalTWnG1d0MjAnXqI7v36N%2F%2FGbOWkpzFwWq%2FLSagnxswW%2BlNw10obCvE%2BpyVM1LWmbKhZoBkXfDVMJrKs6nzdp39QYvQ9ZyvsySEjlrRj2597y4Ss88ZYNQFcYFd6Pg4SIgm9evGkKC%2B8OuJsyT%2BTb5Z3BfyY4cUprdreudLKFzy%2BKhBYOiR6PaW%2FBN6iBGErZDFK5A4lj7WQTUKWx4CxyFjsK2cw9VlXZHmESolHtGHxu6noF2rwRlnu4CapUC3MtlUuB9s9mfDUIeTm6ANF7G9dbbGhOboYY0LQrQNkhntIPBAcVsXycwyk1WsqvT7GZqir3ZHiNQNOoo%2B0XiZW8Afm3LP%2B2JKDMfdcIf4lexcbJMWhLNVdvrFtCIsYp3E6boRuFS7CJxBwesKfFtqemlP3btHUhviyIJY%2BmcjW9YRqmkHhW%2BZZjLQIjP%2FWADdYM1SNaGpOvdPw5yeRebH4XBKXQ0HrkJkzZEnaLBclHqOUO6pDQApQvYe8eWvj6fPrs5uVB4Tvmd8ehmmvktCYFGvKDzjG7gjNhOhDGIIWrutukNKg4hn1En%2F5RlyJf8Vn1F1xoQFftHycSBBoVAfVl3H8vwyhg6ppS3UMKnWgb0GOqUBOQXm8v6DN1QbNf%2BLl%2FR%2FGZ%2Bo4picPHmmyW5Cm1pKtXtBoSr5bhMR4BnrTfZZ7H8do0DQv05L8RNvsDPWl%2B6HrHoerwIHc%2B7BQm5dTxSZ%2BMaFSydW9mNczVQUHaTaul2JgV1lcbvQp3DvJaTD6Vbm2p6jNC7xSJ%2BmG6nsMy1c2SXsnGkHS9wdNtgtukLt17OYISbAvpw%2FI8N1sl7r87g8JXVyxUNK&X-Amz-Signature=b2d65633931f53595e0fd557289e68bd5a2c1111c2acf4742d90ad4bc0a5a500&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
```python
from sklearn.model_selection import cross_val_score

# Example data
X = [[1, 2], [2, 3], [4, 5], [3, 6]]  # Independent variables
y = [2, 3, 5, 7]                      # Dependent variable

# Perform K-Fold Cross-Validation
scores = cross_val_score(model, X, y, cv=4, scoring='neg_mean_squared_error')
mse_scores = -scores
print(f'Mean Squared Error for each fold: {mse_scores}')
print(f'Average Mean Squared Error: {mse_scores.mean()}')
```
### **Formula for Mean Squared Error (MSE):**
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
 $$
Where $ y_i  $ are the actual values, $ \hat{y}_i  $ are the predicted values, and $ n  $ is the number of observations.
### Summary
- **Train and Test on the Same Dataset:** Simple but prone to overfitting with high training accuracy and low out-of-sample accuracy.
- **Train/Test Split:** Provides better out-of-sample accuracy but can still be affected by dataset dependency.
- **K-Fold Cross-Validation:** Mitigates issues of train/test split by averaging results over multiple splits, offering a more consistent evaluation metric.
___
## Model Evaluation Metrics for Regression
### Introduction
Evaluation metrics are essential for assessing the performance of a regression model. These metrics compare actual values to predicted values, providing insights into areas needing improvement. Several key metrics are used to evaluate regression models, including Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Relative Absolute Error (RAE), Relative Squared Error (RSE), and R-squared ($ R^2 $).
### Error Definition
In regression, the error is the difference between the actual data points and the predicted values from the model. This difference can be measured in various ways.
### Mean Absolute Error (MAE)
Mean Absolute Error is the average of the absolute differences between actual and predicted values. It is easy to understand and represents the average error in the same units as the data.
$$ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
 $$
#### Code Example
```python
from sklearn.metrics import mean_absolute_error

# Example data
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Calculate MAE
mae = mean_absolute_error(y_true, y_pred)
print(f"Mean Absolute Error: {mae}")
```
### Mean Squared Error (MSE)
Mean Squared Error is the average of the squared differences between actual and predicted values. It emphasizes larger errors more than smaller ones due to the squaring term, making it more sensitive to outliers.
$$ \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \frac{RSS}{n} $$
#### Code Example
```python
from sklearn.metrics import mean_squared_error

# Calculate MSE
mse = mean_squared_error(y_true, y_pred)
print(f"Mean Squared Error: {mse}")
```
### Root Mean Squared Error (RMSE)
Root Mean Squared Error is the square root of the mean squared error. It is popular because it is in the same units as the response variable, making it easier to interpret.
$$ \text{RMSE} = \sqrt{\text{MSE}} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
 $$
#### Code Example
```python
import numpy as np

# Calculate RMSE
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")
```
### Relative Absolute Error (RAE)
Relative Absolute Error (RAE) is a metric expressed as a ratio normalizing the absolute error. It measures the average absolute difference between the actual and predicted values relative to the average absolute difference between the actual values and their mean.
$$ \text{RAE} = \frac{\sum_{i=1}^{n} |y_i - \hat{y}_i|}{\sum_{i=1}^{n} |y_i - \bar{y}|}
 $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
# Calculate RAE
rae = np.sum(np.abs(y_true - y_pred)) / np.sum(np.abs(y_true - np.mean(y_true)))
print(f"Relative Absolute Error: {rae}")
```
### Relative Squared Error (RSE)
Relative Squared Error is similar to RAE but uses squared differences. It is widely adopted for calculating $ R^2 $.
$$ \text{RSE} = \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
# Calculate RSE
rse = np.sum((y_true - y_pred) ** 2) / np.sum((y_true - np.mean(y_true)) ** 2)
print(f"Relative Squared Error: {rse}")
```
### R-squared ($ R^2 $)
R-squared is not an error metric per se (by itself), but it is a popular measure of model accuracy. It indicates how close the data points are to the fitted regression line. A higher $ R^2 $ value indicates a better fit.
$$ R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} = 1 - RSE $$
where $ \bar{y} $ is the mean of the actual values.
#### Code Example
```python
from sklearn.metrics import r2_score

# Calculate R-squared
r2 = r2_score(y_true, y_pred)
print(f"R-squared: {r2}")
```
### Residual Sum of Squares (RSS)
The Residual Sum of Squares (RSS) is a measure of the discrepancy between the data and an estimation model. It is calculated as the sum of the squared differences between the observed actual outcomes and the outcomes predicted by the model.
$$ \text{RSS} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = MSE * n $$
#### Code Example
```python
# Calculate RSS
rss = np.sum((y_true - y_pred) ** 2)
print(f"Residual Sum of Squares: {rss}")
```
### Summary
Each of these metrics quantifies different aspects of model performance. The choice of metric depends on the specific model, data type, and domain knowledge. Understanding and selecting the appropriate metric is crucial for evaluating and improving regression models.
___
## Multiple Linear Regression
### **Linear Regression Models**
- **Simple Linear Regression**: Utilizes one independent variable to estimate a dependent variable (e.g., predicting CO₂ emissions based on engine size).
- **Multiple Linear Regression**: Involves multiple independent variables to predict a dependent variable (e.g., predicting CO₂ emissions using engine size and the number of cylinders).
### **Applications of Multiple Linear Regression**
8. **Identifying Effect Strength**: Determines how independent variables affect the dependent variable. For instance, assessing how revision time, test anxiety, lecture attendance, and gender influence student exam performance.
9. **Predicting Impact of Changes**: Evaluates how changes in independent variables affect the dependent variable. For example, predicting how a patient's blood pressure changes with variations in body mass index, keeping other factors constant.
### **Model Representation**
- **Equation**: The model can be expressed as $ \hat{y}=θ_0+θ_1x_1+θ_2x_2+…+θ_nx_n $.
- **Vector Form**: In multidimensional space, the model is represented as $ \theta^T x $, where $ θ $ is the vector of parameters and $ x $ is the feature set. The first element of $ x $ is set to one to account for the intercept ($ \theta_0 $).
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JS5RBVV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdfX7bE%2FtZoawE%2BS3fynALoxxFwzkKzYnqihNMTAT%2BewIgTz8FaPCZaiqxMS4nk8pz1cYETLJjzsvDIyA6yU4o07kq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDCTiiQRFDC2u32XtYircA5VlrvRFyWQcFyO9AHbnluOALalTWnG1d0MjAnXqI7v36N%2F%2FGbOWkpzFwWq%2FLSagnxswW%2BlNw10obCvE%2BpyVM1LWmbKhZoBkXfDVMJrKs6nzdp39QYvQ9ZyvsySEjlrRj2597y4Ss88ZYNQFcYFd6Pg4SIgm9evGkKC%2B8OuJsyT%2BTb5Z3BfyY4cUprdreudLKFzy%2BKhBYOiR6PaW%2FBN6iBGErZDFK5A4lj7WQTUKWx4CxyFjsK2cw9VlXZHmESolHtGHxu6noF2rwRlnu4CapUC3MtlUuB9s9mfDUIeTm6ANF7G9dbbGhOboYY0LQrQNkhntIPBAcVsXycwyk1WsqvT7GZqir3ZHiNQNOoo%2B0XiZW8Afm3LP%2B2JKDMfdcIf4lexcbJMWhLNVdvrFtCIsYp3E6boRuFS7CJxBwesKfFtqemlP3btHUhviyIJY%2BmcjW9YRqmkHhW%2BZZjLQIjP%2FWADdYM1SNaGpOvdPw5yeRebH4XBKXQ0HrkJkzZEnaLBclHqOUO6pDQApQvYe8eWvj6fPrs5uVB4Tvmd8ehmmvktCYFGvKDzjG7gjNhOhDGIIWrutukNKg4hn1En%2F5RlyJf8Vn1F1xoQFftHycSBBoVAfVl3H8vwyhg6ppS3UMKnWgb0GOqUBOQXm8v6DN1QbNf%2BLl%2FR%2FGZ%2Bo4picPHmmyW5Cm1pKtXtBoSr5bhMR4BnrTfZZ7H8do0DQv05L8RNvsDPWl%2B6HrHoerwIHc%2B7BQm5dTxSZ%2BMaFSydW9mNczVQUHaTaul2JgV1lcbvQp3DvJaTD6Vbm2p6jNC7xSJ%2BmG6nsMy1c2SXsnGkHS9wdNtgtukLt17OYISbAvpw%2FI8N1sl7r87g8JXVyxUNK&X-Amz-Signature=be6ef567730812f83ea4013f59b90c4fb2bfca56fd124e22d256da72db96c53f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### **Code Example:**
Here’s an example of implementing Multiple Linear Regression in Python using `scikit-learn`:
```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Example data
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])  # Independent variables
y = np.array([2, 3, 5, 7])                      # Dependent variable

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Coefficients and intercept
print(f'Intercept: {model.intercept_}')
print(f'Coefficients: {model.coef_}')

# Making predictions
predictions = model.predict(X)
print(f'Predictions: {predictions}')
```
### **Error and Optimization**
- **Error Calculation**: The error for a prediction is the difference between the actual and predicted values. For example, if the actual value $  y $ is 196 and the predicted value $ \hat{y} $ is 140, the error is $ 196−140=56 $.
- **Mean Squared Error (MSE)**: The average of the squared errors across all predictions. The objective is to minimize MSE to find the best parameters.
### **Parameter Estimation Methods**
10. **Ordinary Least Squares (OLS)**: Estimates coefficients by minimizing MSE using matrix operations. Suitable for smaller datasets but can be slow for larger ones.
11. **Optimization Algorithms**: Methods like `Gradient Descent` iteratively adjust coefficients to minimize error. Suitable for large datasets. Some Optimization Algorithms:` Gradient Descent, Stochastic Gradient Descent, Newton’s Metho`
#### **Code Example:**
Here's a simple implementation of Gradient Descent for linear regression:
```python
import numpy as np

def gradient_descent(X, y, learning_rate=0.01, iterations=1000):
    m, n = X.shape
    theta = np.zeros(n)
    for _ in range(iterations):
        gradient = X.T @ (X @ theta - y) / m
        theta -= learning_rate * gradient
    return theta

# Example data
X = np.array([[1, 2], [2, 3], [4, 5], [3, 6]])  # Independent variables
y = np.array([2, 3, 5, 7])                      # Dependent variable

# Adding intercept term (column of ones)
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# Apply gradient descent
theta = gradient_descent(X_b, y)
print(f'Optimized coefficients: {theta}')
```
### **Prediction Phase**
- **Using Parameters**: Once parameters are found, predictions are made by plugging input values into the model equation. For instance, with $ \theta_0 = 125 $, $ \theta_1 = 6.2 $, $ \theta_2 = 14 $, and input values, CO₂ emissions for a car can be predicted.
### **Concerns in Multiple Linear Regression**
- **Number of Variables**: Adding too many variables without justification can lead to overfitting, where the model becomes too complex and less generalizable.
- **Variable Types**: Categorical variables can be included by converting them to numerical values (e.g., coding car type as 0 or 1).
- **Linearity**: Ensure a linear relationship between the dependent variable and independent variables (maybe scatterplot). Non-linear relationships may require non-linear regression.
___
