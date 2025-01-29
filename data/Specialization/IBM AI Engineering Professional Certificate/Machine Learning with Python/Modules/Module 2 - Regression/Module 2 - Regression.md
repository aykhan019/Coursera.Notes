

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHFOIDW4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoLA15rj3eKG6FeAydRmUwmeQUOZcI%2Fr8gOjBRbkiAZgIhAIX93gbOYGEwbbcJxKAYAybNqRTYe72%2FumHgclxwjCfBKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmikK9B4rPkDFXSuAq3AOOiVvqhbScfpZZN4oK4mxsdKhbodJ%2BbyZy4R%2BoNZbcNemERn3KaLyd%2FmbfDsGbW1zAu9%2BvNVvLDXqDGJn50SCxuU9L4l0N34nYD3fu31ZUDV%2F1a9B%2FPWticC1WL9IyFLGAHXRbH%2FyPW5OG%2FS1NQR1Uuk%2F%2BO8jkPYU%2FPU%2B%2BMJuKkcuGMVO0btpNw22i5MFx70uwHFBVPFO6ArxvUSKp%2FGv738hN7b%2B%2BWUqsUaCrc8ZmvGi5t0WHtYotAXZbTfgkFlrslNIXrzT8MVdKnVA002fTOnKeCsiIMgs1J9Gcvlwu2zLkAFId7ZKAOLQv7xArK7p2nM2%2B1zx96wv8cJqT2YUNMheVTvKi0a6%2FGd471yXPMZ5PhmU4B%2BqS1HrctFIbztU24l2%2Fprmjw7Ppcn9N6O2FOEvnStE%2BxTa5OSv%2FgYfHS%2FkkjwmXB8L4AAPV0GwGsPDL9olr3Pda%2BjG7jHRxtyA%2BbgMZIX5GenZJqDRW2PVIwpvmFo9EAOhzznnZ1l8VsZ3lwOosvyXWu0KD05ucq7jrsF6xG3myf9OQtn%2FtoKPJxx6s12tB9KdcFfn4p%2BQnakSFf1tR9H1YRziWUDVIzPTfOJstu5YRspN7FJO9EEqlDhuzO8keVOWHQcgnEjDqxeq8BjqkATkGqr65gJC0tHaVmrU0fquGcz7AGBQZnWXLnAfPV2gmlo1eQFj%2FQnLWCY03LxTL5h4nHkCCAAqVW6%2B2gDcicQXvZX72RIAf9m3fi7YBth6Ysgp7jKIRiFI35JzGOUmaYp0DNN6z9IUL3O5vyfn%2FH%2F7LNKlqAtV0yYMwEL0EREV7HmA%2BO7l2eU5gehTsCSGeeQTfzbOYQX2suGH3sVSgJh0MBi7x&X-Amz-Signature=e5f01900d2078247320f1e6c8a4c2078c309302667f2cd3331ec2e8e821a994d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHFOIDW4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoLA15rj3eKG6FeAydRmUwmeQUOZcI%2Fr8gOjBRbkiAZgIhAIX93gbOYGEwbbcJxKAYAybNqRTYe72%2FumHgclxwjCfBKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmikK9B4rPkDFXSuAq3AOOiVvqhbScfpZZN4oK4mxsdKhbodJ%2BbyZy4R%2BoNZbcNemERn3KaLyd%2FmbfDsGbW1zAu9%2BvNVvLDXqDGJn50SCxuU9L4l0N34nYD3fu31ZUDV%2F1a9B%2FPWticC1WL9IyFLGAHXRbH%2FyPW5OG%2FS1NQR1Uuk%2F%2BO8jkPYU%2FPU%2B%2BMJuKkcuGMVO0btpNw22i5MFx70uwHFBVPFO6ArxvUSKp%2FGv738hN7b%2B%2BWUqsUaCrc8ZmvGi5t0WHtYotAXZbTfgkFlrslNIXrzT8MVdKnVA002fTOnKeCsiIMgs1J9Gcvlwu2zLkAFId7ZKAOLQv7xArK7p2nM2%2B1zx96wv8cJqT2YUNMheVTvKi0a6%2FGd471yXPMZ5PhmU4B%2BqS1HrctFIbztU24l2%2Fprmjw7Ppcn9N6O2FOEvnStE%2BxTa5OSv%2FgYfHS%2FkkjwmXB8L4AAPV0GwGsPDL9olr3Pda%2BjG7jHRxtyA%2BbgMZIX5GenZJqDRW2PVIwpvmFo9EAOhzznnZ1l8VsZ3lwOosvyXWu0KD05ucq7jrsF6xG3myf9OQtn%2FtoKPJxx6s12tB9KdcFfn4p%2BQnakSFf1tR9H1YRziWUDVIzPTfOJstu5YRspN7FJO9EEqlDhuzO8keVOWHQcgnEjDqxeq8BjqkATkGqr65gJC0tHaVmrU0fquGcz7AGBQZnWXLnAfPV2gmlo1eQFj%2FQnLWCY03LxTL5h4nHkCCAAqVW6%2B2gDcicQXvZX72RIAf9m3fi7YBth6Ysgp7jKIRiFI35JzGOUmaYp0DNN6z9IUL3O5vyfn%2FH%2F7LNKlqAtV0yYMwEL0EREV7HmA%2BO7l2eU5gehTsCSGeeQTfzbOYQX2suGH3sVSgJh0MBi7x&X-Amz-Signature=4cc4cc341efc08e516dc6197465e7efda738249701c2cc874fdacc5eedaf86a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHFOIDW4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoLA15rj3eKG6FeAydRmUwmeQUOZcI%2Fr8gOjBRbkiAZgIhAIX93gbOYGEwbbcJxKAYAybNqRTYe72%2FumHgclxwjCfBKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmikK9B4rPkDFXSuAq3AOOiVvqhbScfpZZN4oK4mxsdKhbodJ%2BbyZy4R%2BoNZbcNemERn3KaLyd%2FmbfDsGbW1zAu9%2BvNVvLDXqDGJn50SCxuU9L4l0N34nYD3fu31ZUDV%2F1a9B%2FPWticC1WL9IyFLGAHXRbH%2FyPW5OG%2FS1NQR1Uuk%2F%2BO8jkPYU%2FPU%2B%2BMJuKkcuGMVO0btpNw22i5MFx70uwHFBVPFO6ArxvUSKp%2FGv738hN7b%2B%2BWUqsUaCrc8ZmvGi5t0WHtYotAXZbTfgkFlrslNIXrzT8MVdKnVA002fTOnKeCsiIMgs1J9Gcvlwu2zLkAFId7ZKAOLQv7xArK7p2nM2%2B1zx96wv8cJqT2YUNMheVTvKi0a6%2FGd471yXPMZ5PhmU4B%2BqS1HrctFIbztU24l2%2Fprmjw7Ppcn9N6O2FOEvnStE%2BxTa5OSv%2FgYfHS%2FkkjwmXB8L4AAPV0GwGsPDL9olr3Pda%2BjG7jHRxtyA%2BbgMZIX5GenZJqDRW2PVIwpvmFo9EAOhzznnZ1l8VsZ3lwOosvyXWu0KD05ucq7jrsF6xG3myf9OQtn%2FtoKPJxx6s12tB9KdcFfn4p%2BQnakSFf1tR9H1YRziWUDVIzPTfOJstu5YRspN7FJO9EEqlDhuzO8keVOWHQcgnEjDqxeq8BjqkATkGqr65gJC0tHaVmrU0fquGcz7AGBQZnWXLnAfPV2gmlo1eQFj%2FQnLWCY03LxTL5h4nHkCCAAqVW6%2B2gDcicQXvZX72RIAf9m3fi7YBth6Ysgp7jKIRiFI35JzGOUmaYp0DNN6z9IUL3O5vyfn%2FH%2F7LNKlqAtV0yYMwEL0EREV7HmA%2BO7l2eU5gehTsCSGeeQTfzbOYQX2suGH3sVSgJh0MBi7x&X-Amz-Signature=618bb8535f83155e6baa4a5d93cbba9a4059d66f65882ecbeb79136f6d43800c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHFOIDW4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoLA15rj3eKG6FeAydRmUwmeQUOZcI%2Fr8gOjBRbkiAZgIhAIX93gbOYGEwbbcJxKAYAybNqRTYe72%2FumHgclxwjCfBKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmikK9B4rPkDFXSuAq3AOOiVvqhbScfpZZN4oK4mxsdKhbodJ%2BbyZy4R%2BoNZbcNemERn3KaLyd%2FmbfDsGbW1zAu9%2BvNVvLDXqDGJn50SCxuU9L4l0N34nYD3fu31ZUDV%2F1a9B%2FPWticC1WL9IyFLGAHXRbH%2FyPW5OG%2FS1NQR1Uuk%2F%2BO8jkPYU%2FPU%2B%2BMJuKkcuGMVO0btpNw22i5MFx70uwHFBVPFO6ArxvUSKp%2FGv738hN7b%2B%2BWUqsUaCrc8ZmvGi5t0WHtYotAXZbTfgkFlrslNIXrzT8MVdKnVA002fTOnKeCsiIMgs1J9Gcvlwu2zLkAFId7ZKAOLQv7xArK7p2nM2%2B1zx96wv8cJqT2YUNMheVTvKi0a6%2FGd471yXPMZ5PhmU4B%2BqS1HrctFIbztU24l2%2Fprmjw7Ppcn9N6O2FOEvnStE%2BxTa5OSv%2FgYfHS%2FkkjwmXB8L4AAPV0GwGsPDL9olr3Pda%2BjG7jHRxtyA%2BbgMZIX5GenZJqDRW2PVIwpvmFo9EAOhzznnZ1l8VsZ3lwOosvyXWu0KD05ucq7jrsF6xG3myf9OQtn%2FtoKPJxx6s12tB9KdcFfn4p%2BQnakSFf1tR9H1YRziWUDVIzPTfOJstu5YRspN7FJO9EEqlDhuzO8keVOWHQcgnEjDqxeq8BjqkATkGqr65gJC0tHaVmrU0fquGcz7AGBQZnWXLnAfPV2gmlo1eQFj%2FQnLWCY03LxTL5h4nHkCCAAqVW6%2B2gDcicQXvZX72RIAf9m3fi7YBth6Ysgp7jKIRiFI35JzGOUmaYp0DNN6z9IUL3O5vyfn%2FH%2F7LNKlqAtV0yYMwEL0EREV7HmA%2BO7l2eU5gehTsCSGeeQTfzbOYQX2suGH3sVSgJh0MBi7x&X-Amz-Signature=ef8d5086d7e9df02aaf8ab74dc670285198589cc96becbe27e23c70228205d28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHFOIDW4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoLA15rj3eKG6FeAydRmUwmeQUOZcI%2Fr8gOjBRbkiAZgIhAIX93gbOYGEwbbcJxKAYAybNqRTYe72%2FumHgclxwjCfBKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmikK9B4rPkDFXSuAq3AOOiVvqhbScfpZZN4oK4mxsdKhbodJ%2BbyZy4R%2BoNZbcNemERn3KaLyd%2FmbfDsGbW1zAu9%2BvNVvLDXqDGJn50SCxuU9L4l0N34nYD3fu31ZUDV%2F1a9B%2FPWticC1WL9IyFLGAHXRbH%2FyPW5OG%2FS1NQR1Uuk%2F%2BO8jkPYU%2FPU%2B%2BMJuKkcuGMVO0btpNw22i5MFx70uwHFBVPFO6ArxvUSKp%2FGv738hN7b%2B%2BWUqsUaCrc8ZmvGi5t0WHtYotAXZbTfgkFlrslNIXrzT8MVdKnVA002fTOnKeCsiIMgs1J9Gcvlwu2zLkAFId7ZKAOLQv7xArK7p2nM2%2B1zx96wv8cJqT2YUNMheVTvKi0a6%2FGd471yXPMZ5PhmU4B%2BqS1HrctFIbztU24l2%2Fprmjw7Ppcn9N6O2FOEvnStE%2BxTa5OSv%2FgYfHS%2FkkjwmXB8L4AAPV0GwGsPDL9olr3Pda%2BjG7jHRxtyA%2BbgMZIX5GenZJqDRW2PVIwpvmFo9EAOhzznnZ1l8VsZ3lwOosvyXWu0KD05ucq7jrsF6xG3myf9OQtn%2FtoKPJxx6s12tB9KdcFfn4p%2BQnakSFf1tR9H1YRziWUDVIzPTfOJstu5YRspN7FJO9EEqlDhuzO8keVOWHQcgnEjDqxeq8BjqkATkGqr65gJC0tHaVmrU0fquGcz7AGBQZnWXLnAfPV2gmlo1eQFj%2FQnLWCY03LxTL5h4nHkCCAAqVW6%2B2gDcicQXvZX72RIAf9m3fi7YBth6Ysgp7jKIRiFI35JzGOUmaYp0DNN6z9IUL3O5vyfn%2FH%2F7LNKlqAtV0yYMwEL0EREV7HmA%2BO7l2eU5gehTsCSGeeQTfzbOYQX2suGH3sVSgJh0MBi7x&X-Amz-Signature=2a06cf0ec3be9ae1ca681c266122483dfab3cf45d4f0cca24a1372a1d5b468de&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHFOIDW4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoLA15rj3eKG6FeAydRmUwmeQUOZcI%2Fr8gOjBRbkiAZgIhAIX93gbOYGEwbbcJxKAYAybNqRTYe72%2FumHgclxwjCfBKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmikK9B4rPkDFXSuAq3AOOiVvqhbScfpZZN4oK4mxsdKhbodJ%2BbyZy4R%2BoNZbcNemERn3KaLyd%2FmbfDsGbW1zAu9%2BvNVvLDXqDGJn50SCxuU9L4l0N34nYD3fu31ZUDV%2F1a9B%2FPWticC1WL9IyFLGAHXRbH%2FyPW5OG%2FS1NQR1Uuk%2F%2BO8jkPYU%2FPU%2B%2BMJuKkcuGMVO0btpNw22i5MFx70uwHFBVPFO6ArxvUSKp%2FGv738hN7b%2B%2BWUqsUaCrc8ZmvGi5t0WHtYotAXZbTfgkFlrslNIXrzT8MVdKnVA002fTOnKeCsiIMgs1J9Gcvlwu2zLkAFId7ZKAOLQv7xArK7p2nM2%2B1zx96wv8cJqT2YUNMheVTvKi0a6%2FGd471yXPMZ5PhmU4B%2BqS1HrctFIbztU24l2%2Fprmjw7Ppcn9N6O2FOEvnStE%2BxTa5OSv%2FgYfHS%2FkkjwmXB8L4AAPV0GwGsPDL9olr3Pda%2BjG7jHRxtyA%2BbgMZIX5GenZJqDRW2PVIwpvmFo9EAOhzznnZ1l8VsZ3lwOosvyXWu0KD05ucq7jrsF6xG3myf9OQtn%2FtoKPJxx6s12tB9KdcFfn4p%2BQnakSFf1tR9H1YRziWUDVIzPTfOJstu5YRspN7FJO9EEqlDhuzO8keVOWHQcgnEjDqxeq8BjqkATkGqr65gJC0tHaVmrU0fquGcz7AGBQZnWXLnAfPV2gmlo1eQFj%2FQnLWCY03LxTL5h4nHkCCAAqVW6%2B2gDcicQXvZX72RIAf9m3fi7YBth6Ysgp7jKIRiFI35JzGOUmaYp0DNN6z9IUL3O5vyfn%2FH%2F7LNKlqAtV0yYMwEL0EREV7HmA%2BO7l2eU5gehTsCSGeeQTfzbOYQX2suGH3sVSgJh0MBi7x&X-Amz-Signature=6aba7bafe5d0f530668b1459e132e0158e0995a94580fdc7b774715c7806359f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHFOIDW4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoLA15rj3eKG6FeAydRmUwmeQUOZcI%2Fr8gOjBRbkiAZgIhAIX93gbOYGEwbbcJxKAYAybNqRTYe72%2FumHgclxwjCfBKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmikK9B4rPkDFXSuAq3AOOiVvqhbScfpZZN4oK4mxsdKhbodJ%2BbyZy4R%2BoNZbcNemERn3KaLyd%2FmbfDsGbW1zAu9%2BvNVvLDXqDGJn50SCxuU9L4l0N34nYD3fu31ZUDV%2F1a9B%2FPWticC1WL9IyFLGAHXRbH%2FyPW5OG%2FS1NQR1Uuk%2F%2BO8jkPYU%2FPU%2B%2BMJuKkcuGMVO0btpNw22i5MFx70uwHFBVPFO6ArxvUSKp%2FGv738hN7b%2B%2BWUqsUaCrc8ZmvGi5t0WHtYotAXZbTfgkFlrslNIXrzT8MVdKnVA002fTOnKeCsiIMgs1J9Gcvlwu2zLkAFId7ZKAOLQv7xArK7p2nM2%2B1zx96wv8cJqT2YUNMheVTvKi0a6%2FGd471yXPMZ5PhmU4B%2BqS1HrctFIbztU24l2%2Fprmjw7Ppcn9N6O2FOEvnStE%2BxTa5OSv%2FgYfHS%2FkkjwmXB8L4AAPV0GwGsPDL9olr3Pda%2BjG7jHRxtyA%2BbgMZIX5GenZJqDRW2PVIwpvmFo9EAOhzznnZ1l8VsZ3lwOosvyXWu0KD05ucq7jrsF6xG3myf9OQtn%2FtoKPJxx6s12tB9KdcFfn4p%2BQnakSFf1tR9H1YRziWUDVIzPTfOJstu5YRspN7FJO9EEqlDhuzO8keVOWHQcgnEjDqxeq8BjqkATkGqr65gJC0tHaVmrU0fquGcz7AGBQZnWXLnAfPV2gmlo1eQFj%2FQnLWCY03LxTL5h4nHkCCAAqVW6%2B2gDcicQXvZX72RIAf9m3fi7YBth6Ysgp7jKIRiFI35JzGOUmaYp0DNN6z9IUL3O5vyfn%2FH%2F7LNKlqAtV0yYMwEL0EREV7HmA%2BO7l2eU5gehTsCSGeeQTfzbOYQX2suGH3sVSgJh0MBi7x&X-Amz-Signature=a4f43d105e7e8e4e8736ae7bacf6701e65d0e147d6bfb65667339f01b8a769e6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHFOIDW4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoLA15rj3eKG6FeAydRmUwmeQUOZcI%2Fr8gOjBRbkiAZgIhAIX93gbOYGEwbbcJxKAYAybNqRTYe72%2FumHgclxwjCfBKogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzmikK9B4rPkDFXSuAq3AOOiVvqhbScfpZZN4oK4mxsdKhbodJ%2BbyZy4R%2BoNZbcNemERn3KaLyd%2FmbfDsGbW1zAu9%2BvNVvLDXqDGJn50SCxuU9L4l0N34nYD3fu31ZUDV%2F1a9B%2FPWticC1WL9IyFLGAHXRbH%2FyPW5OG%2FS1NQR1Uuk%2F%2BO8jkPYU%2FPU%2B%2BMJuKkcuGMVO0btpNw22i5MFx70uwHFBVPFO6ArxvUSKp%2FGv738hN7b%2B%2BWUqsUaCrc8ZmvGi5t0WHtYotAXZbTfgkFlrslNIXrzT8MVdKnVA002fTOnKeCsiIMgs1J9Gcvlwu2zLkAFId7ZKAOLQv7xArK7p2nM2%2B1zx96wv8cJqT2YUNMheVTvKi0a6%2FGd471yXPMZ5PhmU4B%2BqS1HrctFIbztU24l2%2Fprmjw7Ppcn9N6O2FOEvnStE%2BxTa5OSv%2FgYfHS%2FkkjwmXB8L4AAPV0GwGsPDL9olr3Pda%2BjG7jHRxtyA%2BbgMZIX5GenZJqDRW2PVIwpvmFo9EAOhzznnZ1l8VsZ3lwOosvyXWu0KD05ucq7jrsF6xG3myf9OQtn%2FtoKPJxx6s12tB9KdcFfn4p%2BQnakSFf1tR9H1YRziWUDVIzPTfOJstu5YRspN7FJO9EEqlDhuzO8keVOWHQcgnEjDqxeq8BjqkATkGqr65gJC0tHaVmrU0fquGcz7AGBQZnWXLnAfPV2gmlo1eQFj%2FQnLWCY03LxTL5h4nHkCCAAqVW6%2B2gDcicQXvZX72RIAf9m3fi7YBth6Ysgp7jKIRiFI35JzGOUmaYp0DNN6z9IUL3O5vyfn%2FH%2F7LNKlqAtV0yYMwEL0EREV7HmA%2BO7l2eU5gehTsCSGeeQTfzbOYQX2suGH3sVSgJh0MBi7x&X-Amz-Signature=179682697c51425c82657ee7801a135fa9c44cfb70c1bee8a6b3f28df1d031af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RW5BLWX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEvRutvM5rNdRVOehoLScpc%2BsCLb9MfK4fxxNl%2FwGQcAIhAO7kGu%2FRz8zW0SNAPdRQcG2obeaHgnFDBah8CmVylqa8KogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFHV5oYlsW3VYiNRkq3AOcK%2FmSNZMVS2a82hbm1zpJrgVPnCTAVfAZvHIdwzYnirrvuV6v1tsPnU%2BEEM47ecYXcj%2FGhQ8rl4b8maoKxM5HGpRSC88dVBL2VbqB56n%2F8NJPw66c0Fdmi69SNWFHuQbc4cxo5nYevMWY8SGCvHhmuvRVbxCS2DGRUfOQwkFiCOHyK1JZNNsuhw%2BFLgksQ6URhLupYiFHUzQB4udNGT%2FmcyFa0VEgYdNkogXapCLcTtDq8q7xPK43gExp4gf2dKO7N0jYNu1CN6zDM%2Bl5ou513zqkG8bu%2F4Tu0UBt43gtx%2FRLkzsOgkdG6vkDMJIaB8VrGIDKzuj3zC2A67szQKz6Wap5kxqNpSJUD7piR3WUxoDI45ggy6c592%2BKYl1IRtl0a9ZqEU9cGWCgVYVX9ePT3b2%2B68ptIHbghDTzWj2okXjeCmdpK4I%2FZUwwE6n2teWwkaX9OTNA4oMb69nVUS9hddZpoG653XwfR9wOZI%2FlmyTXnQy%2FJrISADWQbKnlkVvrZoCv7ECPV8zhnf6Q1JmZW%2BfiRIJHm4nz2AVlr8DOu6z3p3wgN1LoC2xJsPLsi2%2BtJ2SM8wf423UN%2BIJnXAwuwxaRg8qtVYcVdg8tNrKPYmNZbfd7r8t%2F4K4LkDDTxeq8BjqkAbwUbDW23zOKEN4DlGo%2FRVzK7FjgAf4RP18tTuNJMvDFpZduxRfKQMmqWzf%2BkM2j1DlsYVohVS42UpoSKGUrjyM983KCvLvzXNPvwIGVreZZSLj%2F%2BvHdoa%2FCQutPsZMo%2F9s3rzQwPcyKI6PZSrlL0BshIEnL3mewrPoIcUL0vxp4cjkGNqy%2F1lGZxsIpk%2Fb0yOoT0Ihc2TCjv1YbMgvizGX%2FB9BP&X-Amz-Signature=756f24af6986bef4d779ff26c1c73f4dbb8eac0d68684ccee156d41d8cc3957b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN354SMJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCT7cV7TLGx7vHKTrsJLbCnb7ELdO9VBKE%2FDDYzQss%2BwIhAIsVojgAcqhX60dpvBer7sXfQOG3QW%2FnxeeEz%2BZgYLN9KogECJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLumgVG%2BwD56c%2BYNAq3AMIz9zkiswMVRmUpWjwANptIoLMErxXqZGKrMVGoKGTjbSdfXLfDJ447EsGVDoziF7mL7cnuIkSMBv9f%2Fnzo8Xt3Q%2BfSuiv1JS8b0njsSJYLKNptnKxp%2B3QrC3W%2BZzI7A9lguPGPyXJ5FfVpuPO5n9ftTUb04pG5TV6Skr%2F4b2%2BKGLs6PlMY0I%2FLDI1hj6O0avCgG7u9bHNzFyt%2B%2BXh6AThZmBgrVXCPIfy6TUXlewWfChdT4LaLmtEe1zdrPswJcso%2FF4bIOz%2FtMJ02mcWD0YPPJDOEB6XA4TcNuYuBw4fUz33GsNK8OFr4El2XWVuowgaGZgb3jnDJ2g40ZdX7G58LaeSX7dZowtXvFfxV5cwZADzsszW5sPOb3Qld0Zh1uBrT0N9pgCwmaWhyLk31KO0Vgn08n%2BfCAnA95AWatWQL0XehIKbO6B5ncsmER7sgX1ky%2BGyPr5mENzUKP1B0fFAfSky0RfmfWaM94UrvwXbEf%2B6DVoJiL63p5d7oR%2BTjdHgrdXUo4iioMW8BkcoU9eOfUhgR%2F7crDA3s7FHGc0SpYd%2F%2BF84FEMT809uYqBjmj7jgLIbxwQE8eXsg7DhZdf8S8s05HDZ7%2BEF6mmvLOxebHGwQsPFJLsuBIcIaDCixuq8BjqkAdF1ibbTIZX6M7Msqw1tIQvxyPvxHD3zZgvdUXO5jJ9rCCRFzw15mhZfSWufEp4%2BwnwXAWbGohaxkE%2FaYFsu3f%2FKwwvnBGQeU6Epx35vqD77IcGF%2BtONlRNLRTD6UJH2y7ffpzKnRtH8dCrWtOoseoXzhdh%2FMRWDnv%2B5OmUsRcwMO7L3eTJz2mvayFphL%2FZZpb3jnhENErxpDcF5fiDfZ6iLDkiq&X-Amz-Signature=b1d830199770bf0c880850a8d4dba8075a438692e0a2b2680fc47f506603a89d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663S6F6Z4J%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiQj0OVXENnScFMZ6%2BYjPHscSTBYOCnpgmFYqfLOuX4AIgVDrV3SOpIQNmr7mMcS1OkelRZWIjVR3gAHRz8ck4yyUqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGtUPwyNBefVN4ASXCrcA4zkQVfDeiRqlHQdRc3W2kQqj5wKB6fgJdr%2BDgHeda0Re9zhV8BDS%2FmDJ63N3%2BV2jzaK0JUSaoPknkeHO7TOkMO7%2FqRwMO0kOpAGXy0ySxYlfNz%2FlGqHyM4i3YxISqM4Q1vDaJ1HUxLsOyWgSE5xMJuF%2FAF%2BKXpIgYwDySaWA8yuh23bDmbmDnCHmIb85Td0hhWj9jP3LGtwuKGpGSCJ%2BrVH%2FdVie%2BsJTwBSuE%2FRNGeWd3xqA2HGmO9Awb4uZC1fknuZ38xEwlGV6HAAuv2Zpsa%2FfTfFLRYhxAOYuiJze9zHFyEfTRu6J%2F0q0p%2BIa6d2Swwc%2BETc753TQUzeFqSUHU59XXpqq4fejCVXs49WQ80IYkpCLIt8mXSsXatC%2Bq5dD%2F3ABOmq2Luj23k%2FiqJtRbOc3kEkkQWqXLSacgwCJ2yxtGAkNECOoZD77do7cH6cO4lb5jcV9LMqwJq2YJ2kd4hYwh2o5Gj2RlxvqkLkoy3W8HXNSAUFgWPD5%2FWrJQpenpyUjXDkd74%2Bpoxafzi7%2FDIG0fCGG1JiGEjAVIbZ012mFTjc0iqxft1fqqjXX%2Fv%2F4oUH%2B81dj3L8t72kD1LoFXKCDVAWRy%2Bs99608sEI9Y%2B%2FOwnDF5lnVzWGb0eDMLTF6rwGOqUBpPEGlo2V2%2BvtmMqZkoa6ABDTinDtqLs4myX%2FWYZy1nW1qMVJ6iFbvKb4N8P8413tTXIsPm5K5wp6%2FJudrNQXneeH5B24Jwla3eIH5gZ%2BsOLTctjkVEcNQqB4ii%2FCigJufprjd5t8kuakvyv5S4mi1KEFmstc7%2FY7sv0WkfvL72IZUAIVMuVNMzrRrBwgFDkDLLKtgwvdcgQ8B3MmQjq7BOIAAzLM&X-Amz-Signature=35e1b0e874e8d3ced1946c262ca70f97fe2f421b18211b550bee6d3c45fc6ba2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663S6F6Z4J%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T231337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiQj0OVXENnScFMZ6%2BYjPHscSTBYOCnpgmFYqfLOuX4AIgVDrV3SOpIQNmr7mMcS1OkelRZWIjVR3gAHRz8ck4yyUqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGtUPwyNBefVN4ASXCrcA4zkQVfDeiRqlHQdRc3W2kQqj5wKB6fgJdr%2BDgHeda0Re9zhV8BDS%2FmDJ63N3%2BV2jzaK0JUSaoPknkeHO7TOkMO7%2FqRwMO0kOpAGXy0ySxYlfNz%2FlGqHyM4i3YxISqM4Q1vDaJ1HUxLsOyWgSE5xMJuF%2FAF%2BKXpIgYwDySaWA8yuh23bDmbmDnCHmIb85Td0hhWj9jP3LGtwuKGpGSCJ%2BrVH%2FdVie%2BsJTwBSuE%2FRNGeWd3xqA2HGmO9Awb4uZC1fknuZ38xEwlGV6HAAuv2Zpsa%2FfTfFLRYhxAOYuiJze9zHFyEfTRu6J%2F0q0p%2BIa6d2Swwc%2BETc753TQUzeFqSUHU59XXpqq4fejCVXs49WQ80IYkpCLIt8mXSsXatC%2Bq5dD%2F3ABOmq2Luj23k%2FiqJtRbOc3kEkkQWqXLSacgwCJ2yxtGAkNECOoZD77do7cH6cO4lb5jcV9LMqwJq2YJ2kd4hYwh2o5Gj2RlxvqkLkoy3W8HXNSAUFgWPD5%2FWrJQpenpyUjXDkd74%2Bpoxafzi7%2FDIG0fCGG1JiGEjAVIbZ012mFTjc0iqxft1fqqjXX%2Fv%2F4oUH%2B81dj3L8t72kD1LoFXKCDVAWRy%2Bs99608sEI9Y%2B%2FOwnDF5lnVzWGb0eDMLTF6rwGOqUBpPEGlo2V2%2BvtmMqZkoa6ABDTinDtqLs4myX%2FWYZy1nW1qMVJ6iFbvKb4N8P8413tTXIsPm5K5wp6%2FJudrNQXneeH5B24Jwla3eIH5gZ%2BsOLTctjkVEcNQqB4ii%2FCigJufprjd5t8kuakvyv5S4mi1KEFmstc7%2FY7sv0WkfvL72IZUAIVMuVNMzrRrBwgFDkDLLKtgwvdcgQ8B3MmQjq7BOIAAzLM&X-Amz-Signature=4d141371a069e609d22cf196eaa7ca10f1ba1f9d93959771f8b84fb8d416a9c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
