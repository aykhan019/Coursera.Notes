

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPD5TKQ7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHI64zh8vV7%2BrDuRp0Ta22hkSDUc4pVNKEQBXxqicShfAiEA7qyM7M9ti%2FBGQgBVy5HJO5uR3SEvsBTDM%2BZUqGAz4Ncq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDLHEKTEhpop2cvHMYyrcA0Eo7jcN4RI5J%2BBYBdaKrZUO4q7XTrGP1uqIu1z%2F2KiT6d857Lx7l9m%2BvxUw0FXFMFVbgflhUWtTzg5Mwr0Im9rrkoXwTIOWVdzHTIYnkuTRL3YELyqtwR1er8mIzWYAo6wCrIm%2F69iNJnxIB87H753%2BTQcRcXIx%2BM2W5zljNzZu6tuFPKQygudKmwFsAnvmAAYEFzoraDBGsjS%2B2fduPxlZatuC7lQZCBdAp8qCCpr%2B76zPYOYJXuYRe%2BI07ZJeeBxxC0KcNJPysJ4Ogj2a%2BLu4ZSDAKnvp9iFp9Vh7a8w7Tj0skRGSIn7Oa9xUJVENP91UHCOpx3wYC98pfRoEwVmrljag%2FHziZZ8h36D9yRU0HLZOOQIn%2BJKFzMLxIaIokKrm8lffZ2cLCzeuLxcNhxSQxRrJc7XotJC7G9Fy04AWb8oMzZsiGWF%2FIr5ouk3bsBxRR62xxSDbnnV0BMalsX1UkswGhDyunJZBKJS7eH0ndhsFMpU9ubUonSM4KOjpg7IDk%2FuX%2FvZapQOozP8kxp5Q86dOqyIjVEn3a%2FkSeahmbQ48H2DEzzXU6dS9FcJVUwPn5QxxCkD74dnq9Ywx08R1MMo66fWN%2FF4kw8CvcGvtdTsekoL2dqQdo8HzMNXfkL0GOqUBOVnIOtxQL2cugCzeH%2FN5yDcaZXpanQSksskrB6lqSG0W1zDXrDv%2Bn0%2BG3ididzVSgNEcavOELac0fW%2FW91mjYmDuEgkwlXZZg9O8eoqi9M%2FTk60F6QjdZAa48%2B4m3soLePva7wPgedQMuM0ZBwgaxMpXZTC5KiJDgIDwufE6VJhxD8m%2Bjflojb5HgMOngjlzRbk6cqJ77r5eaB%2FV1sngNOzB%2B8K2&X-Amz-Signature=931d3f29663a50be0ee52bcf1626cb303bc3eaaeb341b2dbd13a85966d68b013&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPD5TKQ7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHI64zh8vV7%2BrDuRp0Ta22hkSDUc4pVNKEQBXxqicShfAiEA7qyM7M9ti%2FBGQgBVy5HJO5uR3SEvsBTDM%2BZUqGAz4Ncq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDLHEKTEhpop2cvHMYyrcA0Eo7jcN4RI5J%2BBYBdaKrZUO4q7XTrGP1uqIu1z%2F2KiT6d857Lx7l9m%2BvxUw0FXFMFVbgflhUWtTzg5Mwr0Im9rrkoXwTIOWVdzHTIYnkuTRL3YELyqtwR1er8mIzWYAo6wCrIm%2F69iNJnxIB87H753%2BTQcRcXIx%2BM2W5zljNzZu6tuFPKQygudKmwFsAnvmAAYEFzoraDBGsjS%2B2fduPxlZatuC7lQZCBdAp8qCCpr%2B76zPYOYJXuYRe%2BI07ZJeeBxxC0KcNJPysJ4Ogj2a%2BLu4ZSDAKnvp9iFp9Vh7a8w7Tj0skRGSIn7Oa9xUJVENP91UHCOpx3wYC98pfRoEwVmrljag%2FHziZZ8h36D9yRU0HLZOOQIn%2BJKFzMLxIaIokKrm8lffZ2cLCzeuLxcNhxSQxRrJc7XotJC7G9Fy04AWb8oMzZsiGWF%2FIr5ouk3bsBxRR62xxSDbnnV0BMalsX1UkswGhDyunJZBKJS7eH0ndhsFMpU9ubUonSM4KOjpg7IDk%2FuX%2FvZapQOozP8kxp5Q86dOqyIjVEn3a%2FkSeahmbQ48H2DEzzXU6dS9FcJVUwPn5QxxCkD74dnq9Ywx08R1MMo66fWN%2FF4kw8CvcGvtdTsekoL2dqQdo8HzMNXfkL0GOqUBOVnIOtxQL2cugCzeH%2FN5yDcaZXpanQSksskrB6lqSG0W1zDXrDv%2Bn0%2BG3ididzVSgNEcavOELac0fW%2FW91mjYmDuEgkwlXZZg9O8eoqi9M%2FTk60F6QjdZAa48%2B4m3soLePva7wPgedQMuM0ZBwgaxMpXZTC5KiJDgIDwufE6VJhxD8m%2Bjflojb5HgMOngjlzRbk6cqJ77r5eaB%2FV1sngNOzB%2B8K2&X-Amz-Signature=f25d4a079ee0f4def39b725f16f3d546b2e61ef5df99740abdc5bcf28090ebb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPD5TKQ7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHI64zh8vV7%2BrDuRp0Ta22hkSDUc4pVNKEQBXxqicShfAiEA7qyM7M9ti%2FBGQgBVy5HJO5uR3SEvsBTDM%2BZUqGAz4Ncq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDLHEKTEhpop2cvHMYyrcA0Eo7jcN4RI5J%2BBYBdaKrZUO4q7XTrGP1uqIu1z%2F2KiT6d857Lx7l9m%2BvxUw0FXFMFVbgflhUWtTzg5Mwr0Im9rrkoXwTIOWVdzHTIYnkuTRL3YELyqtwR1er8mIzWYAo6wCrIm%2F69iNJnxIB87H753%2BTQcRcXIx%2BM2W5zljNzZu6tuFPKQygudKmwFsAnvmAAYEFzoraDBGsjS%2B2fduPxlZatuC7lQZCBdAp8qCCpr%2B76zPYOYJXuYRe%2BI07ZJeeBxxC0KcNJPysJ4Ogj2a%2BLu4ZSDAKnvp9iFp9Vh7a8w7Tj0skRGSIn7Oa9xUJVENP91UHCOpx3wYC98pfRoEwVmrljag%2FHziZZ8h36D9yRU0HLZOOQIn%2BJKFzMLxIaIokKrm8lffZ2cLCzeuLxcNhxSQxRrJc7XotJC7G9Fy04AWb8oMzZsiGWF%2FIr5ouk3bsBxRR62xxSDbnnV0BMalsX1UkswGhDyunJZBKJS7eH0ndhsFMpU9ubUonSM4KOjpg7IDk%2FuX%2FvZapQOozP8kxp5Q86dOqyIjVEn3a%2FkSeahmbQ48H2DEzzXU6dS9FcJVUwPn5QxxCkD74dnq9Ywx08R1MMo66fWN%2FF4kw8CvcGvtdTsekoL2dqQdo8HzMNXfkL0GOqUBOVnIOtxQL2cugCzeH%2FN5yDcaZXpanQSksskrB6lqSG0W1zDXrDv%2Bn0%2BG3ididzVSgNEcavOELac0fW%2FW91mjYmDuEgkwlXZZg9O8eoqi9M%2FTk60F6QjdZAa48%2B4m3soLePva7wPgedQMuM0ZBwgaxMpXZTC5KiJDgIDwufE6VJhxD8m%2Bjflojb5HgMOngjlzRbk6cqJ77r5eaB%2FV1sngNOzB%2B8K2&X-Amz-Signature=a34b7e331f970d8a41540ffad5212b1bbc860130468c0bc33831120be2b26387&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPD5TKQ7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHI64zh8vV7%2BrDuRp0Ta22hkSDUc4pVNKEQBXxqicShfAiEA7qyM7M9ti%2FBGQgBVy5HJO5uR3SEvsBTDM%2BZUqGAz4Ncq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDLHEKTEhpop2cvHMYyrcA0Eo7jcN4RI5J%2BBYBdaKrZUO4q7XTrGP1uqIu1z%2F2KiT6d857Lx7l9m%2BvxUw0FXFMFVbgflhUWtTzg5Mwr0Im9rrkoXwTIOWVdzHTIYnkuTRL3YELyqtwR1er8mIzWYAo6wCrIm%2F69iNJnxIB87H753%2BTQcRcXIx%2BM2W5zljNzZu6tuFPKQygudKmwFsAnvmAAYEFzoraDBGsjS%2B2fduPxlZatuC7lQZCBdAp8qCCpr%2B76zPYOYJXuYRe%2BI07ZJeeBxxC0KcNJPysJ4Ogj2a%2BLu4ZSDAKnvp9iFp9Vh7a8w7Tj0skRGSIn7Oa9xUJVENP91UHCOpx3wYC98pfRoEwVmrljag%2FHziZZ8h36D9yRU0HLZOOQIn%2BJKFzMLxIaIokKrm8lffZ2cLCzeuLxcNhxSQxRrJc7XotJC7G9Fy04AWb8oMzZsiGWF%2FIr5ouk3bsBxRR62xxSDbnnV0BMalsX1UkswGhDyunJZBKJS7eH0ndhsFMpU9ubUonSM4KOjpg7IDk%2FuX%2FvZapQOozP8kxp5Q86dOqyIjVEn3a%2FkSeahmbQ48H2DEzzXU6dS9FcJVUwPn5QxxCkD74dnq9Ywx08R1MMo66fWN%2FF4kw8CvcGvtdTsekoL2dqQdo8HzMNXfkL0GOqUBOVnIOtxQL2cugCzeH%2FN5yDcaZXpanQSksskrB6lqSG0W1zDXrDv%2Bn0%2BG3ididzVSgNEcavOELac0fW%2FW91mjYmDuEgkwlXZZg9O8eoqi9M%2FTk60F6QjdZAa48%2B4m3soLePva7wPgedQMuM0ZBwgaxMpXZTC5KiJDgIDwufE6VJhxD8m%2Bjflojb5HgMOngjlzRbk6cqJ77r5eaB%2FV1sngNOzB%2B8K2&X-Amz-Signature=d09995b6e3593f1f7cad85a54498a147049249d267e41ff0a106ac5689cbfb0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPD5TKQ7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHI64zh8vV7%2BrDuRp0Ta22hkSDUc4pVNKEQBXxqicShfAiEA7qyM7M9ti%2FBGQgBVy5HJO5uR3SEvsBTDM%2BZUqGAz4Ncq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDLHEKTEhpop2cvHMYyrcA0Eo7jcN4RI5J%2BBYBdaKrZUO4q7XTrGP1uqIu1z%2F2KiT6d857Lx7l9m%2BvxUw0FXFMFVbgflhUWtTzg5Mwr0Im9rrkoXwTIOWVdzHTIYnkuTRL3YELyqtwR1er8mIzWYAo6wCrIm%2F69iNJnxIB87H753%2BTQcRcXIx%2BM2W5zljNzZu6tuFPKQygudKmwFsAnvmAAYEFzoraDBGsjS%2B2fduPxlZatuC7lQZCBdAp8qCCpr%2B76zPYOYJXuYRe%2BI07ZJeeBxxC0KcNJPysJ4Ogj2a%2BLu4ZSDAKnvp9iFp9Vh7a8w7Tj0skRGSIn7Oa9xUJVENP91UHCOpx3wYC98pfRoEwVmrljag%2FHziZZ8h36D9yRU0HLZOOQIn%2BJKFzMLxIaIokKrm8lffZ2cLCzeuLxcNhxSQxRrJc7XotJC7G9Fy04AWb8oMzZsiGWF%2FIr5ouk3bsBxRR62xxSDbnnV0BMalsX1UkswGhDyunJZBKJS7eH0ndhsFMpU9ubUonSM4KOjpg7IDk%2FuX%2FvZapQOozP8kxp5Q86dOqyIjVEn3a%2FkSeahmbQ48H2DEzzXU6dS9FcJVUwPn5QxxCkD74dnq9Ywx08R1MMo66fWN%2FF4kw8CvcGvtdTsekoL2dqQdo8HzMNXfkL0GOqUBOVnIOtxQL2cugCzeH%2FN5yDcaZXpanQSksskrB6lqSG0W1zDXrDv%2Bn0%2BG3ididzVSgNEcavOELac0fW%2FW91mjYmDuEgkwlXZZg9O8eoqi9M%2FTk60F6QjdZAa48%2B4m3soLePva7wPgedQMuM0ZBwgaxMpXZTC5KiJDgIDwufE6VJhxD8m%2Bjflojb5HgMOngjlzRbk6cqJ77r5eaB%2FV1sngNOzB%2B8K2&X-Amz-Signature=6e9175367e67fc0bb9685c59b1b7b2b429a999a3e3d6d841d6bd0dc1a1d1006f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPD5TKQ7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHI64zh8vV7%2BrDuRp0Ta22hkSDUc4pVNKEQBXxqicShfAiEA7qyM7M9ti%2FBGQgBVy5HJO5uR3SEvsBTDM%2BZUqGAz4Ncq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDLHEKTEhpop2cvHMYyrcA0Eo7jcN4RI5J%2BBYBdaKrZUO4q7XTrGP1uqIu1z%2F2KiT6d857Lx7l9m%2BvxUw0FXFMFVbgflhUWtTzg5Mwr0Im9rrkoXwTIOWVdzHTIYnkuTRL3YELyqtwR1er8mIzWYAo6wCrIm%2F69iNJnxIB87H753%2BTQcRcXIx%2BM2W5zljNzZu6tuFPKQygudKmwFsAnvmAAYEFzoraDBGsjS%2B2fduPxlZatuC7lQZCBdAp8qCCpr%2B76zPYOYJXuYRe%2BI07ZJeeBxxC0KcNJPysJ4Ogj2a%2BLu4ZSDAKnvp9iFp9Vh7a8w7Tj0skRGSIn7Oa9xUJVENP91UHCOpx3wYC98pfRoEwVmrljag%2FHziZZ8h36D9yRU0HLZOOQIn%2BJKFzMLxIaIokKrm8lffZ2cLCzeuLxcNhxSQxRrJc7XotJC7G9Fy04AWb8oMzZsiGWF%2FIr5ouk3bsBxRR62xxSDbnnV0BMalsX1UkswGhDyunJZBKJS7eH0ndhsFMpU9ubUonSM4KOjpg7IDk%2FuX%2FvZapQOozP8kxp5Q86dOqyIjVEn3a%2FkSeahmbQ48H2DEzzXU6dS9FcJVUwPn5QxxCkD74dnq9Ywx08R1MMo66fWN%2FF4kw8CvcGvtdTsekoL2dqQdo8HzMNXfkL0GOqUBOVnIOtxQL2cugCzeH%2FN5yDcaZXpanQSksskrB6lqSG0W1zDXrDv%2Bn0%2BG3ididzVSgNEcavOELac0fW%2FW91mjYmDuEgkwlXZZg9O8eoqi9M%2FTk60F6QjdZAa48%2B4m3soLePva7wPgedQMuM0ZBwgaxMpXZTC5KiJDgIDwufE6VJhxD8m%2Bjflojb5HgMOngjlzRbk6cqJ77r5eaB%2FV1sngNOzB%2B8K2&X-Amz-Signature=7ffedbd8e7f642882671c6c01087cb7caa476771c15edc7ee0d4765395c72770&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPD5TKQ7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHI64zh8vV7%2BrDuRp0Ta22hkSDUc4pVNKEQBXxqicShfAiEA7qyM7M9ti%2FBGQgBVy5HJO5uR3SEvsBTDM%2BZUqGAz4Ncq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDLHEKTEhpop2cvHMYyrcA0Eo7jcN4RI5J%2BBYBdaKrZUO4q7XTrGP1uqIu1z%2F2KiT6d857Lx7l9m%2BvxUw0FXFMFVbgflhUWtTzg5Mwr0Im9rrkoXwTIOWVdzHTIYnkuTRL3YELyqtwR1er8mIzWYAo6wCrIm%2F69iNJnxIB87H753%2BTQcRcXIx%2BM2W5zljNzZu6tuFPKQygudKmwFsAnvmAAYEFzoraDBGsjS%2B2fduPxlZatuC7lQZCBdAp8qCCpr%2B76zPYOYJXuYRe%2BI07ZJeeBxxC0KcNJPysJ4Ogj2a%2BLu4ZSDAKnvp9iFp9Vh7a8w7Tj0skRGSIn7Oa9xUJVENP91UHCOpx3wYC98pfRoEwVmrljag%2FHziZZ8h36D9yRU0HLZOOQIn%2BJKFzMLxIaIokKrm8lffZ2cLCzeuLxcNhxSQxRrJc7XotJC7G9Fy04AWb8oMzZsiGWF%2FIr5ouk3bsBxRR62xxSDbnnV0BMalsX1UkswGhDyunJZBKJS7eH0ndhsFMpU9ubUonSM4KOjpg7IDk%2FuX%2FvZapQOozP8kxp5Q86dOqyIjVEn3a%2FkSeahmbQ48H2DEzzXU6dS9FcJVUwPn5QxxCkD74dnq9Ywx08R1MMo66fWN%2FF4kw8CvcGvtdTsekoL2dqQdo8HzMNXfkL0GOqUBOVnIOtxQL2cugCzeH%2FN5yDcaZXpanQSksskrB6lqSG0W1zDXrDv%2Bn0%2BG3ididzVSgNEcavOELac0fW%2FW91mjYmDuEgkwlXZZg9O8eoqi9M%2FTk60F6QjdZAa48%2B4m3soLePva7wPgedQMuM0ZBwgaxMpXZTC5KiJDgIDwufE6VJhxD8m%2Bjflojb5HgMOngjlzRbk6cqJ77r5eaB%2FV1sngNOzB%2B8K2&X-Amz-Signature=ab99ac3d6e52bbf758fdad6c0765a9a973f001b293ef2f4fe1043f8b15eef0ff&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPD5TKQ7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHI64zh8vV7%2BrDuRp0Ta22hkSDUc4pVNKEQBXxqicShfAiEA7qyM7M9ti%2FBGQgBVy5HJO5uR3SEvsBTDM%2BZUqGAz4Ncq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDLHEKTEhpop2cvHMYyrcA0Eo7jcN4RI5J%2BBYBdaKrZUO4q7XTrGP1uqIu1z%2F2KiT6d857Lx7l9m%2BvxUw0FXFMFVbgflhUWtTzg5Mwr0Im9rrkoXwTIOWVdzHTIYnkuTRL3YELyqtwR1er8mIzWYAo6wCrIm%2F69iNJnxIB87H753%2BTQcRcXIx%2BM2W5zljNzZu6tuFPKQygudKmwFsAnvmAAYEFzoraDBGsjS%2B2fduPxlZatuC7lQZCBdAp8qCCpr%2B76zPYOYJXuYRe%2BI07ZJeeBxxC0KcNJPysJ4Ogj2a%2BLu4ZSDAKnvp9iFp9Vh7a8w7Tj0skRGSIn7Oa9xUJVENP91UHCOpx3wYC98pfRoEwVmrljag%2FHziZZ8h36D9yRU0HLZOOQIn%2BJKFzMLxIaIokKrm8lffZ2cLCzeuLxcNhxSQxRrJc7XotJC7G9Fy04AWb8oMzZsiGWF%2FIr5ouk3bsBxRR62xxSDbnnV0BMalsX1UkswGhDyunJZBKJS7eH0ndhsFMpU9ubUonSM4KOjpg7IDk%2FuX%2FvZapQOozP8kxp5Q86dOqyIjVEn3a%2FkSeahmbQ48H2DEzzXU6dS9FcJVUwPn5QxxCkD74dnq9Ywx08R1MMo66fWN%2FF4kw8CvcGvtdTsekoL2dqQdo8HzMNXfkL0GOqUBOVnIOtxQL2cugCzeH%2FN5yDcaZXpanQSksskrB6lqSG0W1zDXrDv%2Bn0%2BG3ididzVSgNEcavOELac0fW%2FW91mjYmDuEgkwlXZZg9O8eoqi9M%2FTk60F6QjdZAa48%2B4m3soLePva7wPgedQMuM0ZBwgaxMpXZTC5KiJDgIDwufE6VJhxD8m%2Bjflojb5HgMOngjlzRbk6cqJ77r5eaB%2FV1sngNOzB%2B8K2&X-Amz-Signature=6e7156f1aa3293be0cd1d612c6b14838f2f9c06e2c61c11fb352cc184200ec50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CDHEXEE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC3HLMtTyWCgqh3%2F5XBnTGzpXHfUgveqa2%2B4Ng3SdS8ogIgOSQc0Fr%2BYrlYhFs1zCuu59mrBAEbo6ZQF046KgCcHX8q%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDLZ9%2BYUUzYezfvLZNSrcA51S%2BM8YWe%2Fac1KcaCwxQjnzO02BdHMLtz2eZT1TMNOkF6fm3SK9i0l9NOPJZNZ070QFK6irjjc8KM8wJqiN46xaqx%2FMUU7JcC9L4Yrs6jYId69d26tVoyL6bEEZzTpT%2FGWINWRTeI7MQoaNWn31UsAT3Au6xx06mxDU18Wyq5HbT66O1k%2BQMjF4UwsTudKVUNCSvVFJdq3vx34V1d8GfFK4dlNwZdSlC1wZuZRD0aSpVIXgnXcFnaMPDtF2X9KjCW2vWFZ5BtwYFjrvRPZtPYXYYE2GfvwO%2Fvdbw2KEQvv%2BJ6TVHY%2BGsTJI9YU%2BWFlkMOxO1hR5vSsoB9HCEscwyO8fRExR8FyWdIXZ9N5fY5iVmhf3iKngaejTyvEEAzDSz%2BGePeL411BJLrZRJaSKbIFZZir%2Bju%2FYU50PO5VQilS2DnHS9Hp5lxB6dcSlnqzJM1Ilv%2FtHYnNAxFBADDgowZFna97tGg5W%2FzQB8Ze1yP1wCtTeSDpfLc5GTsLRB3jPt432%2BWSS%2F3XrzZZAylmxmd0FuLkQzfvBAIsfIuPokV8MTN5dzGBYWgbdbe%2FyhM1jUfLSa%2FPzN4BPszxItOII0GNS4mUbKpBl4jaddhtKlikMexKU2SpCt1Y3XN4sMLffkL0GOqUBuL%2F7DqWCgD4fm2Mzv2DtIUHC%2BsFQV7krTQlAyaxA%2Bk0L8Ogdov8ylwiYcw2Nsyq2oec9EK153McsrjYGQewStZ3IcWjh25iuH2NgXgasLbsyLE6PMl6owVGXKnSaaoR2cHntgWsdU0B750blebjZPVSOoZ8CL3zq%2BupIxpaCuqfMaoXGQ0bg%2FKF85IJhEVmHOPpW6gd6YUC8UPLZwC%2FLRwtpJbUD&X-Amz-Signature=090afade695ef80e4b1aab83aeed320b8129e96c2bf79ad10769ec68c8598af5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NULVS23%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIBO0M8eqHP8mrLUN2WwruuFGsRqXkbvczkztqR09VHbtAiAVa0GToODnIf3XbHAI%2FlGKGI3rWzS3UgelAfkke1RvACr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIM0ISsJYynKsMvaCSGKtwDTTE5Z2RhcU8G61z6bmNufU8f2bxkQqAxkaFjLfGUx02vP5DBpdW%2FbulSu%2FKZVy%2BK%2BwYlXE7JNkv%2B3dJwZhGZJImi3TzRk42ZpSc1JsAvfHECFdhgZ%2BUB9G%2F1zNV25A6O2l482TAeDlsgpMG6qZQ0jZGumXhZ%2Bc270gHAgQmb45%2BRDAMAwXuuNapr5vTpv7GkBc8YCTH5E5E7%2FrqZlys1ZzdnuQknQkzqhoPiWVsucDgmegHAO0OFYVGQXtXZivg0QGRIG9uJVisJqnnCEE4bZWi1eC72rBoPkdjlolhm8x%2Fvi0ezRRQuSjiL08Rf%2BWkV1iDMH61m%2FkoBnC%2BeInqIu9Gk4m5%2BY7HfBrPmns1Qb8nm%2B2%2Fk7tYRn%2BtjTZVNWngZcZ7ZV%2Bu2jpQuVRohmbNoKxLNloYjO0BuXXzCxAlYVt4W7zWU6Amken7SQAUbdQXxf6KRRB2qzFmAiWklNfYz%2FweDBtCgxnqX7LFRS8f8nL1dEnbJkmDUrN%2FKeDmpqKrMhmOUVj%2BpfGNtv5fV2DX1LlsW3%2BkKCjbb2GcJ4nr4YQ%2FRuS%2F2ACrtKiBxKT4soKilWLuMM2mN26cWpFmIso2ZxHVGE2YiH7Em6GVbEeoKAAZ77J3KHVg%2BX2uApcQw4d%2BQvQY6pgELA7o84mu6A16APnsRfiOc7BMsMSaz7mp52whBqu2lgyuloGSbo7IZHCp4rFFG4nRCewsvtuAzUE%2FGJJBMSKloYhOqKnhXWNadc%2Fvx%2F%2BijNLsIBOhn1vHWfek1nAhD8c5k%2BUSGZ2blYZYxRVP1%2Bvf7AMqhKPvXzA5tX0yBPxyjwYH%2B6Ks2B%2BrS2VLV0rnBuN90zklvyk64St2Hw7d5GaZr8NsAFihQ&X-Amz-Signature=902d54362eac9c229f784e76924af3ea3b34f9703c3916d9f32078185205e37a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ULAUD4N%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHt7QPd%2BJnpT18aiOxrF%2FNazLoCL5Adt5ZoJgpdcwgIPAiEAqa75FGZt40xqi2scN09qB6Jngi%2BFmTt%2F49pHmnmWxlcq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDE%2FONukley61ftDe6ircA9GacgBZs92VrWMsMieV3FthIaK77mSE57H4qpgWVmEq%2FPpCwAAjwhsZxQPVU051scsDn4g8igY33mcN44cguLmXpPOHGcws9ODzj8c%2FRlr6Gae6%2FZ%2B9sKeROR%2F1TjS0HlND%2BnLEgl%2FINh4prB2%2F7Dqcf0C58ueq%2BMrdCCIJmnlDeIgC4Yyvk%2BcmyFTWOxWgh6nJWAkp3Ro2OZUQzZsTlzrQkrdQGRRUmM%2B0t8a2IM83W7unsYZmLeJrRGw7F2sR8wnRGWxI730bC20U2zDjDgguTWxeFnJC6i8J1326VnsAyuwNWi2hmmpu0JGT0yMZJmWy%2F1nPdb7aYrRWPu1YXZYqAZLP1pfG5yur5l073A8W30CO2kh6dxu8TKmg4kMvUHQePLClZlYtfl3e9y11KQQ%2B1CEwUvYJCcRDaeBg4ivoSzavABY5PqqDJ9j1pa5sNUYJFbBlDlyhsQEGQVoBqCbtwga0p39Km8SXkqENyWBFxFOyoAIw2XvmJrj9DbxDp8j2mXFPMTFxPkwBSHIJI8woMPUYGYzn08pZ44vtNOykcU0UFc2C3ABpMUpnr6IsgQB4t6ShLosAPlbDAkoVWETLq3o5n%2FH6pL2cavxsYrEI%2F%2BiL%2Bi6AdEynswTzMP3fkL0GOqUBLPNeoE4jsZG5SIXIcU0a%2B6yyo4gO5qzLmJon1thnO9N5O%2BNWB5C2bESxlye78TtQ5m2kImBDn8%2BdDUo7fe9na5JYvNPu%2Fumw3NQUw6D0YjOulNMh4nhLR6lkvkfVuFWV5b8ylkQu0KyUsDqlFAoxMxcxmKpgcbdvrLRqQXVc6M6gjBM3uBXruv%2FveAdPBuZTVzPUQZCQpCCCerZEf%2FrLso6rFFeG&X-Amz-Signature=0d45cfafa76b18f996f1b13a2a6d69b45a4560668b6b32615737b4d9d5700394&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ULAUD4N%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIHt7QPd%2BJnpT18aiOxrF%2FNazLoCL5Adt5ZoJgpdcwgIPAiEAqa75FGZt40xqi2scN09qB6Jngi%2BFmTt%2F49pHmnmWxlcq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDE%2FONukley61ftDe6ircA9GacgBZs92VrWMsMieV3FthIaK77mSE57H4qpgWVmEq%2FPpCwAAjwhsZxQPVU051scsDn4g8igY33mcN44cguLmXpPOHGcws9ODzj8c%2FRlr6Gae6%2FZ%2B9sKeROR%2F1TjS0HlND%2BnLEgl%2FINh4prB2%2F7Dqcf0C58ueq%2BMrdCCIJmnlDeIgC4Yyvk%2BcmyFTWOxWgh6nJWAkp3Ro2OZUQzZsTlzrQkrdQGRRUmM%2B0t8a2IM83W7unsYZmLeJrRGw7F2sR8wnRGWxI730bC20U2zDjDgguTWxeFnJC6i8J1326VnsAyuwNWi2hmmpu0JGT0yMZJmWy%2F1nPdb7aYrRWPu1YXZYqAZLP1pfG5yur5l073A8W30CO2kh6dxu8TKmg4kMvUHQePLClZlYtfl3e9y11KQQ%2B1CEwUvYJCcRDaeBg4ivoSzavABY5PqqDJ9j1pa5sNUYJFbBlDlyhsQEGQVoBqCbtwga0p39Km8SXkqENyWBFxFOyoAIw2XvmJrj9DbxDp8j2mXFPMTFxPkwBSHIJI8woMPUYGYzn08pZ44vtNOykcU0UFc2C3ABpMUpnr6IsgQB4t6ShLosAPlbDAkoVWETLq3o5n%2FH6pL2cavxsYrEI%2F%2BiL%2Bi6AdEynswTzMP3fkL0GOqUBLPNeoE4jsZG5SIXIcU0a%2B6yyo4gO5qzLmJon1thnO9N5O%2BNWB5C2bESxlye78TtQ5m2kImBDn8%2BdDUo7fe9na5JYvNPu%2Fumw3NQUw6D0YjOulNMh4nhLR6lkvkfVuFWV5b8ylkQu0KyUsDqlFAoxMxcxmKpgcbdvrLRqQXVc6M6gjBM3uBXruv%2FveAdPBuZTVzPUQZCQpCCCerZEf%2FrLso6rFFeG&X-Amz-Signature=5048ca7e9cbc0cca8db617cd634c1602c28235381f80c86c147d8f63cf397761&X-Amz-SignedHeaders=host&x-id=GetObject)
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
