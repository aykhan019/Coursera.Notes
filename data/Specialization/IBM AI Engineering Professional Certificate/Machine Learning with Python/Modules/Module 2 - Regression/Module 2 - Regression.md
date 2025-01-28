

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YB2RXCQY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIE9sWZZrIi4xPZIZDHWMGq%2Bm2ESte8kM%2BpXw5yWFI8xvAiByU%2BBqJ3xPbyOXyEc0GVsD4lpVCFYqckmFwH10wNTM7yr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM%2BEo1qdLLFWCYRcexKtwDWhb69TpjUAFBjoVmgSg9tISW6%2Bj6U7VjKZFc7fdRON27gPmi%2F%2BSd1A4A3uJITq72AaJ47znsorsD2AsYeh9luuIDc4sWTgX4mAmELLBWvCvRa9gqtRt1EXMUzw8MfS5DhJkmcEUHkootxbxWG2uIqZK5F7vzqQ6BW0AsLaifjFJ8%2BnwJQHyJnPigr6k4ovsFTB8uxgG%2FNA45JUa7Rl5HCp9fZqaO%2FZXR2P9JJzUzj%2B0L6d8RCc4g1yTleCRHT8Nd8SMZtZcthTGDfZ4%2FNtMBJn8Xlt3Edzn3dIWwUliyRfP3%2BQkY8bq%2F73sIc%2Bn%2F9lZFTSF%2FszT7%2Bvp13GFB%2FPik8%2BbvLcxfDYvQWmb9bvU50Ne75FLQ1sYJTjLvOh2O4VlgaGmgeoubfSyMtevGPk6s0L8p7LTIoVUVQ0LXH1W27AxeJGe9yiGc9xQZ5JzJH1nmYBiIjyXM3ocJKnDIGKRvcrznICULnjGeUJ8pJUXdHg%2FpvBnGkg%2BSRpN8cYI5M0afyxOVJszl%2Bk4o6BgH2nC4QEqXCkJj40WD11G8xYb%2FvddT4qks6i3emWcdWGyEuaRoiWd6K9HvU1PB27MWZ1%2BT6udm58sKpV%2FhVhcIykqK1tvFeQypKBPEz3sHD6gwiPrkvAY6pgGFvZK4HCOy27EUJePNYji6h8C8w3MHMBGFdEGFUqvKyyE6QxbuWJfrG5J1ghb78rqhem6wtuOTI6rcOfONANfL4%2BVT%2Bq7CAxx7FY%2FTnxg3M1ov4%2FAHCm26Jv4rMOZKCoYjACdnOqTJ8yVhqt0anWI%2F8jdWUtDvzwfsxVjnWChKH%2FEkKk5%2Brxp4h9xaNDWNqVg3XeQxnz7iqWDg6UVq%2FF%2Bq6pJZhZHj&X-Amz-Signature=ba14073c26c475055e0a9e830d737a5cbef14c42e976b5953fbb8c8471d3caa3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YB2RXCQY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIE9sWZZrIi4xPZIZDHWMGq%2Bm2ESte8kM%2BpXw5yWFI8xvAiByU%2BBqJ3xPbyOXyEc0GVsD4lpVCFYqckmFwH10wNTM7yr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM%2BEo1qdLLFWCYRcexKtwDWhb69TpjUAFBjoVmgSg9tISW6%2Bj6U7VjKZFc7fdRON27gPmi%2F%2BSd1A4A3uJITq72AaJ47znsorsD2AsYeh9luuIDc4sWTgX4mAmELLBWvCvRa9gqtRt1EXMUzw8MfS5DhJkmcEUHkootxbxWG2uIqZK5F7vzqQ6BW0AsLaifjFJ8%2BnwJQHyJnPigr6k4ovsFTB8uxgG%2FNA45JUa7Rl5HCp9fZqaO%2FZXR2P9JJzUzj%2B0L6d8RCc4g1yTleCRHT8Nd8SMZtZcthTGDfZ4%2FNtMBJn8Xlt3Edzn3dIWwUliyRfP3%2BQkY8bq%2F73sIc%2Bn%2F9lZFTSF%2FszT7%2Bvp13GFB%2FPik8%2BbvLcxfDYvQWmb9bvU50Ne75FLQ1sYJTjLvOh2O4VlgaGmgeoubfSyMtevGPk6s0L8p7LTIoVUVQ0LXH1W27AxeJGe9yiGc9xQZ5JzJH1nmYBiIjyXM3ocJKnDIGKRvcrznICULnjGeUJ8pJUXdHg%2FpvBnGkg%2BSRpN8cYI5M0afyxOVJszl%2Bk4o6BgH2nC4QEqXCkJj40WD11G8xYb%2FvddT4qks6i3emWcdWGyEuaRoiWd6K9HvU1PB27MWZ1%2BT6udm58sKpV%2FhVhcIykqK1tvFeQypKBPEz3sHD6gwiPrkvAY6pgGFvZK4HCOy27EUJePNYji6h8C8w3MHMBGFdEGFUqvKyyE6QxbuWJfrG5J1ghb78rqhem6wtuOTI6rcOfONANfL4%2BVT%2Bq7CAxx7FY%2FTnxg3M1ov4%2FAHCm26Jv4rMOZKCoYjACdnOqTJ8yVhqt0anWI%2F8jdWUtDvzwfsxVjnWChKH%2FEkKk5%2Brxp4h9xaNDWNqVg3XeQxnz7iqWDg6UVq%2FF%2Bq6pJZhZHj&X-Amz-Signature=b8c063967a5ce9397528c97ac843616d61bc533a9cb6b9be2e1bbdec1fbcb586&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YB2RXCQY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIE9sWZZrIi4xPZIZDHWMGq%2Bm2ESte8kM%2BpXw5yWFI8xvAiByU%2BBqJ3xPbyOXyEc0GVsD4lpVCFYqckmFwH10wNTM7yr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM%2BEo1qdLLFWCYRcexKtwDWhb69TpjUAFBjoVmgSg9tISW6%2Bj6U7VjKZFc7fdRON27gPmi%2F%2BSd1A4A3uJITq72AaJ47znsorsD2AsYeh9luuIDc4sWTgX4mAmELLBWvCvRa9gqtRt1EXMUzw8MfS5DhJkmcEUHkootxbxWG2uIqZK5F7vzqQ6BW0AsLaifjFJ8%2BnwJQHyJnPigr6k4ovsFTB8uxgG%2FNA45JUa7Rl5HCp9fZqaO%2FZXR2P9JJzUzj%2B0L6d8RCc4g1yTleCRHT8Nd8SMZtZcthTGDfZ4%2FNtMBJn8Xlt3Edzn3dIWwUliyRfP3%2BQkY8bq%2F73sIc%2Bn%2F9lZFTSF%2FszT7%2Bvp13GFB%2FPik8%2BbvLcxfDYvQWmb9bvU50Ne75FLQ1sYJTjLvOh2O4VlgaGmgeoubfSyMtevGPk6s0L8p7LTIoVUVQ0LXH1W27AxeJGe9yiGc9xQZ5JzJH1nmYBiIjyXM3ocJKnDIGKRvcrznICULnjGeUJ8pJUXdHg%2FpvBnGkg%2BSRpN8cYI5M0afyxOVJszl%2Bk4o6BgH2nC4QEqXCkJj40WD11G8xYb%2FvddT4qks6i3emWcdWGyEuaRoiWd6K9HvU1PB27MWZ1%2BT6udm58sKpV%2FhVhcIykqK1tvFeQypKBPEz3sHD6gwiPrkvAY6pgGFvZK4HCOy27EUJePNYji6h8C8w3MHMBGFdEGFUqvKyyE6QxbuWJfrG5J1ghb78rqhem6wtuOTI6rcOfONANfL4%2BVT%2Bq7CAxx7FY%2FTnxg3M1ov4%2FAHCm26Jv4rMOZKCoYjACdnOqTJ8yVhqt0anWI%2F8jdWUtDvzwfsxVjnWChKH%2FEkKk5%2Brxp4h9xaNDWNqVg3XeQxnz7iqWDg6UVq%2FF%2Bq6pJZhZHj&X-Amz-Signature=208fea9b859f9b35cafbf0d5d2aaa9fb58852e3ac91635fa39e6d84f40253d9a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YB2RXCQY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIE9sWZZrIi4xPZIZDHWMGq%2Bm2ESte8kM%2BpXw5yWFI8xvAiByU%2BBqJ3xPbyOXyEc0GVsD4lpVCFYqckmFwH10wNTM7yr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM%2BEo1qdLLFWCYRcexKtwDWhb69TpjUAFBjoVmgSg9tISW6%2Bj6U7VjKZFc7fdRON27gPmi%2F%2BSd1A4A3uJITq72AaJ47znsorsD2AsYeh9luuIDc4sWTgX4mAmELLBWvCvRa9gqtRt1EXMUzw8MfS5DhJkmcEUHkootxbxWG2uIqZK5F7vzqQ6BW0AsLaifjFJ8%2BnwJQHyJnPigr6k4ovsFTB8uxgG%2FNA45JUa7Rl5HCp9fZqaO%2FZXR2P9JJzUzj%2B0L6d8RCc4g1yTleCRHT8Nd8SMZtZcthTGDfZ4%2FNtMBJn8Xlt3Edzn3dIWwUliyRfP3%2BQkY8bq%2F73sIc%2Bn%2F9lZFTSF%2FszT7%2Bvp13GFB%2FPik8%2BbvLcxfDYvQWmb9bvU50Ne75FLQ1sYJTjLvOh2O4VlgaGmgeoubfSyMtevGPk6s0L8p7LTIoVUVQ0LXH1W27AxeJGe9yiGc9xQZ5JzJH1nmYBiIjyXM3ocJKnDIGKRvcrznICULnjGeUJ8pJUXdHg%2FpvBnGkg%2BSRpN8cYI5M0afyxOVJszl%2Bk4o6BgH2nC4QEqXCkJj40WD11G8xYb%2FvddT4qks6i3emWcdWGyEuaRoiWd6K9HvU1PB27MWZ1%2BT6udm58sKpV%2FhVhcIykqK1tvFeQypKBPEz3sHD6gwiPrkvAY6pgGFvZK4HCOy27EUJePNYji6h8C8w3MHMBGFdEGFUqvKyyE6QxbuWJfrG5J1ghb78rqhem6wtuOTI6rcOfONANfL4%2BVT%2Bq7CAxx7FY%2FTnxg3M1ov4%2FAHCm26Jv4rMOZKCoYjACdnOqTJ8yVhqt0anWI%2F8jdWUtDvzwfsxVjnWChKH%2FEkKk5%2Brxp4h9xaNDWNqVg3XeQxnz7iqWDg6UVq%2FF%2Bq6pJZhZHj&X-Amz-Signature=b2cb1f3d8e1824c95fe484d1c1ef91748dfac20076fd18048cede29f0b5acef4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YB2RXCQY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIE9sWZZrIi4xPZIZDHWMGq%2Bm2ESte8kM%2BpXw5yWFI8xvAiByU%2BBqJ3xPbyOXyEc0GVsD4lpVCFYqckmFwH10wNTM7yr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM%2BEo1qdLLFWCYRcexKtwDWhb69TpjUAFBjoVmgSg9tISW6%2Bj6U7VjKZFc7fdRON27gPmi%2F%2BSd1A4A3uJITq72AaJ47znsorsD2AsYeh9luuIDc4sWTgX4mAmELLBWvCvRa9gqtRt1EXMUzw8MfS5DhJkmcEUHkootxbxWG2uIqZK5F7vzqQ6BW0AsLaifjFJ8%2BnwJQHyJnPigr6k4ovsFTB8uxgG%2FNA45JUa7Rl5HCp9fZqaO%2FZXR2P9JJzUzj%2B0L6d8RCc4g1yTleCRHT8Nd8SMZtZcthTGDfZ4%2FNtMBJn8Xlt3Edzn3dIWwUliyRfP3%2BQkY8bq%2F73sIc%2Bn%2F9lZFTSF%2FszT7%2Bvp13GFB%2FPik8%2BbvLcxfDYvQWmb9bvU50Ne75FLQ1sYJTjLvOh2O4VlgaGmgeoubfSyMtevGPk6s0L8p7LTIoVUVQ0LXH1W27AxeJGe9yiGc9xQZ5JzJH1nmYBiIjyXM3ocJKnDIGKRvcrznICULnjGeUJ8pJUXdHg%2FpvBnGkg%2BSRpN8cYI5M0afyxOVJszl%2Bk4o6BgH2nC4QEqXCkJj40WD11G8xYb%2FvddT4qks6i3emWcdWGyEuaRoiWd6K9HvU1PB27MWZ1%2BT6udm58sKpV%2FhVhcIykqK1tvFeQypKBPEz3sHD6gwiPrkvAY6pgGFvZK4HCOy27EUJePNYji6h8C8w3MHMBGFdEGFUqvKyyE6QxbuWJfrG5J1ghb78rqhem6wtuOTI6rcOfONANfL4%2BVT%2Bq7CAxx7FY%2FTnxg3M1ov4%2FAHCm26Jv4rMOZKCoYjACdnOqTJ8yVhqt0anWI%2F8jdWUtDvzwfsxVjnWChKH%2FEkKk5%2Brxp4h9xaNDWNqVg3XeQxnz7iqWDg6UVq%2FF%2Bq6pJZhZHj&X-Amz-Signature=6e6d0190b82c117ee46c3d5af828cffd9fd6345158d9c93faa0ed1bf53207f3c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YB2RXCQY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIE9sWZZrIi4xPZIZDHWMGq%2Bm2ESte8kM%2BpXw5yWFI8xvAiByU%2BBqJ3xPbyOXyEc0GVsD4lpVCFYqckmFwH10wNTM7yr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM%2BEo1qdLLFWCYRcexKtwDWhb69TpjUAFBjoVmgSg9tISW6%2Bj6U7VjKZFc7fdRON27gPmi%2F%2BSd1A4A3uJITq72AaJ47znsorsD2AsYeh9luuIDc4sWTgX4mAmELLBWvCvRa9gqtRt1EXMUzw8MfS5DhJkmcEUHkootxbxWG2uIqZK5F7vzqQ6BW0AsLaifjFJ8%2BnwJQHyJnPigr6k4ovsFTB8uxgG%2FNA45JUa7Rl5HCp9fZqaO%2FZXR2P9JJzUzj%2B0L6d8RCc4g1yTleCRHT8Nd8SMZtZcthTGDfZ4%2FNtMBJn8Xlt3Edzn3dIWwUliyRfP3%2BQkY8bq%2F73sIc%2Bn%2F9lZFTSF%2FszT7%2Bvp13GFB%2FPik8%2BbvLcxfDYvQWmb9bvU50Ne75FLQ1sYJTjLvOh2O4VlgaGmgeoubfSyMtevGPk6s0L8p7LTIoVUVQ0LXH1W27AxeJGe9yiGc9xQZ5JzJH1nmYBiIjyXM3ocJKnDIGKRvcrznICULnjGeUJ8pJUXdHg%2FpvBnGkg%2BSRpN8cYI5M0afyxOVJszl%2Bk4o6BgH2nC4QEqXCkJj40WD11G8xYb%2FvddT4qks6i3emWcdWGyEuaRoiWd6K9HvU1PB27MWZ1%2BT6udm58sKpV%2FhVhcIykqK1tvFeQypKBPEz3sHD6gwiPrkvAY6pgGFvZK4HCOy27EUJePNYji6h8C8w3MHMBGFdEGFUqvKyyE6QxbuWJfrG5J1ghb78rqhem6wtuOTI6rcOfONANfL4%2BVT%2Bq7CAxx7FY%2FTnxg3M1ov4%2FAHCm26Jv4rMOZKCoYjACdnOqTJ8yVhqt0anWI%2F8jdWUtDvzwfsxVjnWChKH%2FEkKk5%2Brxp4h9xaNDWNqVg3XeQxnz7iqWDg6UVq%2FF%2Bq6pJZhZHj&X-Amz-Signature=db722b4545c3392b6960b2b7cf865ba7e8fdc4ed70a001a7d86c865ab55726d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YB2RXCQY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIE9sWZZrIi4xPZIZDHWMGq%2Bm2ESte8kM%2BpXw5yWFI8xvAiByU%2BBqJ3xPbyOXyEc0GVsD4lpVCFYqckmFwH10wNTM7yr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM%2BEo1qdLLFWCYRcexKtwDWhb69TpjUAFBjoVmgSg9tISW6%2Bj6U7VjKZFc7fdRON27gPmi%2F%2BSd1A4A3uJITq72AaJ47znsorsD2AsYeh9luuIDc4sWTgX4mAmELLBWvCvRa9gqtRt1EXMUzw8MfS5DhJkmcEUHkootxbxWG2uIqZK5F7vzqQ6BW0AsLaifjFJ8%2BnwJQHyJnPigr6k4ovsFTB8uxgG%2FNA45JUa7Rl5HCp9fZqaO%2FZXR2P9JJzUzj%2B0L6d8RCc4g1yTleCRHT8Nd8SMZtZcthTGDfZ4%2FNtMBJn8Xlt3Edzn3dIWwUliyRfP3%2BQkY8bq%2F73sIc%2Bn%2F9lZFTSF%2FszT7%2Bvp13GFB%2FPik8%2BbvLcxfDYvQWmb9bvU50Ne75FLQ1sYJTjLvOh2O4VlgaGmgeoubfSyMtevGPk6s0L8p7LTIoVUVQ0LXH1W27AxeJGe9yiGc9xQZ5JzJH1nmYBiIjyXM3ocJKnDIGKRvcrznICULnjGeUJ8pJUXdHg%2FpvBnGkg%2BSRpN8cYI5M0afyxOVJszl%2Bk4o6BgH2nC4QEqXCkJj40WD11G8xYb%2FvddT4qks6i3emWcdWGyEuaRoiWd6K9HvU1PB27MWZ1%2BT6udm58sKpV%2FhVhcIykqK1tvFeQypKBPEz3sHD6gwiPrkvAY6pgGFvZK4HCOy27EUJePNYji6h8C8w3MHMBGFdEGFUqvKyyE6QxbuWJfrG5J1ghb78rqhem6wtuOTI6rcOfONANfL4%2BVT%2Bq7CAxx7FY%2FTnxg3M1ov4%2FAHCm26Jv4rMOZKCoYjACdnOqTJ8yVhqt0anWI%2F8jdWUtDvzwfsxVjnWChKH%2FEkKk5%2Brxp4h9xaNDWNqVg3XeQxnz7iqWDg6UVq%2FF%2Bq6pJZhZHj&X-Amz-Signature=12e094ed8f1652c117467f8761751a20b905ef4490e73dbcf1c7e9818375ed45&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YB2RXCQY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIE9sWZZrIi4xPZIZDHWMGq%2Bm2ESte8kM%2BpXw5yWFI8xvAiByU%2BBqJ3xPbyOXyEc0GVsD4lpVCFYqckmFwH10wNTM7yr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIM%2BEo1qdLLFWCYRcexKtwDWhb69TpjUAFBjoVmgSg9tISW6%2Bj6U7VjKZFc7fdRON27gPmi%2F%2BSd1A4A3uJITq72AaJ47znsorsD2AsYeh9luuIDc4sWTgX4mAmELLBWvCvRa9gqtRt1EXMUzw8MfS5DhJkmcEUHkootxbxWG2uIqZK5F7vzqQ6BW0AsLaifjFJ8%2BnwJQHyJnPigr6k4ovsFTB8uxgG%2FNA45JUa7Rl5HCp9fZqaO%2FZXR2P9JJzUzj%2B0L6d8RCc4g1yTleCRHT8Nd8SMZtZcthTGDfZ4%2FNtMBJn8Xlt3Edzn3dIWwUliyRfP3%2BQkY8bq%2F73sIc%2Bn%2F9lZFTSF%2FszT7%2Bvp13GFB%2FPik8%2BbvLcxfDYvQWmb9bvU50Ne75FLQ1sYJTjLvOh2O4VlgaGmgeoubfSyMtevGPk6s0L8p7LTIoVUVQ0LXH1W27AxeJGe9yiGc9xQZ5JzJH1nmYBiIjyXM3ocJKnDIGKRvcrznICULnjGeUJ8pJUXdHg%2FpvBnGkg%2BSRpN8cYI5M0afyxOVJszl%2Bk4o6BgH2nC4QEqXCkJj40WD11G8xYb%2FvddT4qks6i3emWcdWGyEuaRoiWd6K9HvU1PB27MWZ1%2BT6udm58sKpV%2FhVhcIykqK1tvFeQypKBPEz3sHD6gwiPrkvAY6pgGFvZK4HCOy27EUJePNYji6h8C8w3MHMBGFdEGFUqvKyyE6QxbuWJfrG5J1ghb78rqhem6wtuOTI6rcOfONANfL4%2BVT%2Bq7CAxx7FY%2FTnxg3M1ov4%2FAHCm26Jv4rMOZKCoYjACdnOqTJ8yVhqt0anWI%2F8jdWUtDvzwfsxVjnWChKH%2FEkKk5%2Brxp4h9xaNDWNqVg3XeQxnz7iqWDg6UVq%2FF%2Bq6pJZhZHj&X-Amz-Signature=2db35cec1322719754460fed1dcce43070e13a56d6c8bf1976475231ac4e9e45&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WKQ4PMP%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIGFftS8ALkDqm%2BJRRJ1wFaEpH%2B4ijP1Sc5jOIQtB1zHQAiEA1BO2AWzLNWv2rz4VsShBVHMoTwSg%2BtDjxLOQHtPkQXAq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDCqXr7CmE31%2BDg1HxCrcA5CwEU06RS5F6ac%2Fm0uIANQIFBNe3Rk2ZIgrsOgf2%2F%2BlueKOL7Hnxeuxk0Nj2%2FRd1Ek44e1Tm2F8KJHLLu3ABv9pvcgVyAbseZknLuznm4mJcY5i9%2FKGR8521Uk4xocwEEoUXzXyfBRwwlpyMTjrRlG65sUOt75ci7HWPFqGcJdvhYBbXsf7qsvuurLLPiz%2FjltbmnWkvAvbID5xxxuSfI7s3QkRpEL%2Br%2Fzt%2FaeMyqP84taMnvbayt8oZlZYweZtfOIr4Pe0Mdq%2FFwJEXZI1bG3XLJg74YWhHWd45c0qYK2QOM3%2FT6Yg0hvzNk%2F%2FF8Kg0DdWcP0CpKHkK3bPtK6Y1kdWdQwRL2XTiMtTCK9e05uzns0FIGaunaFeZMhYndWzbgEh0F3%2FQ2X%2FGfSOO27rJodMsV9KTZgUcpWyG4byRTqHYQr087HxBhmklFJlmPOhzkWv6B%2Bkb%2Fxhccc0OEMURdoeAnxCGudMTAfmJto44MJledGsNOelWspYKX3RqtQjH33c7lHUcZu2k7bL5kNNU0jG03x8JY2lHRX5m5kogL7thuEeFe%2FRFfyiEbc2HRZrNjcnaMV06lszQnAgIvUl9esuErDA6RkQVPVaEaXn5cGSlwf7yjAKx3cGZ51NMPD55LwGOqUB%2BUbhSRSIPxX3ri68eUEa5aQm8vPWFLD91TfYSzKihGMMg9LZ49p04mCSArjff9I9swp06%2FEv4Q5pNJR03o9%2BO51OBA4dEstwn7iq1gIQO4zlLpFthqNxq5LGMLG9ArL1fpkwBtvP3ShSb308iqCl%2B%2FOIblWs33WoDd07WlONDlwo9uakf%2F7j9dvXCIgthwRUW5fTFJ7gmvHKbtzj5IkWKr%2FWKFC2&X-Amz-Signature=8b73d74cdbd5d8b6b4784e4815497d702e5de7f7b35e18cabf14444b9e328872&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UJK7YUY%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIEC1lrWF1rqAEdAXkOUtk5tRj9dxqq0YVtxBipngWBA7AiBOByT4EWiyj5y%2FC4zPXBIjNXyFscYLwqyCnThyoKcgQir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMusiMDBFZToHgImpmKtwD4SrTnb8265hC3ix3V6%2Bfnvd%2FQGs%2Bzq6U29UT9Gnm3hfFWBPSgdBXOB%2F2TzKERbTvftJWcxd4lnsJydhRd4yJu%2BIvPCyh%2FTNSTgycNExgaMK2K7sHUBJWzE8ICL0rrY%2FEW2S4Y2UUa6RLjNiB%2FimmPJ0XBUFBINYMUuC4eij%2BxvQ%2BPqHaiIZavMXu91moEkwSubTpjcxPxvhvG9t6%2FArPvofiIvY26f5XxpAHxgW2TPLw%2FygxWGGL2qyxenLw3JkxwgO24%2FZvi%2BizvGxGWQ0gxwxyYzaJ2tVUrv%2B0XjE1QfatXLbjylJ%2FiCiZIO6NNFpXMe9EXu%2Bls3ByGOsuheoJaszIn2L%2Bq1GY7RLyKKvWF773igHCkLLpX6X5csGzKPyTLpmt6uzNJeQnLLGCuDCf8bSv%2F05vMUhvZcXkBiSyXAv3XxIQXZ7oU3zdj%2Bhkht%2BL259ucFubGKdmvMj9Z%2BzZbW2HLXr32l%2BKqUzVwepav0Sz85J46EQpwLZbRpkGI%2Fcr4SKg3FRVPmIV6DTd1DbHMMmMTh4M8DD6GmiErNfU7V9FSPP8AKOKT1WpHyVDP09NVBHKPOzTWeoPYQL0rWlbaZ6WFxwE8uzplRiopFmrnAfqm3fmeJn7YlDKHOYw4%2FnkvAY6pgGZtQ%2FiZw9qtv5cWYlnm5aGkp9aN%2F1Bn3RnA9wL3tzJr9n6HUaH8MmYlCoMqE58QHbKNIyLyJXe8dQUsBBFCIeITVhoRdxmJ3bn1rLLy%2FmXV%2B8GO%2BNdI6hNgJav47xyR5Z4FTsZeWuO%2BmuCOw0rXoJDS9YmiFbtS8A3Jo5JbD5PQQXpg%2BW0E25liq8%2BzlRvOTSNkwpDXdUS1stOIkuw%2B3ivMyXAAyaN&X-Amz-Signature=6050e1cff9980ba456611e6dfd8abfc6379556347724d319caada0a9e6b402dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TMICWVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIGGHX9oSeFpkbZjMCLovC7vjReKaGTpSapULlkBVqwtLAiEAxZq6O1Suyq%2FOZ6wI0Mfrtve4F%2FoxlVo0yh04Mf8IhMsq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDKym9gTBLi2gFu1elyrcA5SpUOYCLHCZLxS%2FKMzmzWyW90KkgKmE6hl76K9BOcMjdw9KgKcIaJ0QDtu%2BBm7wHq7cCtlr9AxtLXQV4K%2F6rmLTdErTP9qEw7MwmlHuMRgOHWZjKEKQs%2F0uPGfkVDyHAh%2BTD8AzvFhQpaRjoOvWW%2BXy6bbYR9rbhuf%2Blt9ZHycSLxMUPPLZ1d8pSGXT38DOVbXlD2HIo%2F69LngIH8HDVAuPDjH4SQHvjhBmFqjFFh9jsyD6%2Bi5u%2BU4OAaPpNhVq7Q0fUFM1oV79kSwQKfwtRP%2FVx3DYdlG03BO7V0E54484skUc72ewWvrqhEWTewK%2BjQKKrDPV0hbO72LA4azyvmZjPXT9GVrsRMjNxliYJp5QoHtAX5%2FWvSJBxvKBeKVW6RgpZojir82Z9hK5TnZ%2F1Kv73iHVq23ZgVjSWVCOQZZ6E3zUmEn4tIUkKMvMDyzCa1j0MS8i6qB2HldssijEtXW0Y5MLIUetDJFlvAAmB7BbjA27hxPzos3aNLhPCPCTXIOdOvfr70%2Fp8Y7zEbvbd0GKgYkPEahUm%2F5%2BbkFFpwnj0g%2BAE6Ju4E3jnZUgLVV9DMwOAyib%2BZYHHflWk8UA6Uix2D3e5gQ8%2BS0hezsi2JIPetaxBBs833dx3%2FZhMMf55LwGOqUB7OY%2F1KnAnBZFdli7l%2FPkqsL5%2FD%2FYbxqVTuTyPJe5gKfgPdvWGGzrRSdlWbZI16RbQgFLoWvNCdidFKm%2Bai1c0%2B9mOEUXmgs%2FRsEvrX9DO3yiSiys4rUb2Y8sr5HReGMtU4adXNipWTSR4zvhCxjaF%2FW52CPthe2WBks8TGecR4j6e5IDD1POkzZTvHv%2Bx8YILuydPNZ58io6w8ABVII4TySJvKIK&X-Amz-Signature=632e5e59f834d955a84407b93153c209ee2ea60a276a8e182c920f2bf685e061&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TMICWVF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIGGHX9oSeFpkbZjMCLovC7vjReKaGTpSapULlkBVqwtLAiEAxZq6O1Suyq%2FOZ6wI0Mfrtve4F%2FoxlVo0yh04Mf8IhMsq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDKym9gTBLi2gFu1elyrcA5SpUOYCLHCZLxS%2FKMzmzWyW90KkgKmE6hl76K9BOcMjdw9KgKcIaJ0QDtu%2BBm7wHq7cCtlr9AxtLXQV4K%2F6rmLTdErTP9qEw7MwmlHuMRgOHWZjKEKQs%2F0uPGfkVDyHAh%2BTD8AzvFhQpaRjoOvWW%2BXy6bbYR9rbhuf%2Blt9ZHycSLxMUPPLZ1d8pSGXT38DOVbXlD2HIo%2F69LngIH8HDVAuPDjH4SQHvjhBmFqjFFh9jsyD6%2Bi5u%2BU4OAaPpNhVq7Q0fUFM1oV79kSwQKfwtRP%2FVx3DYdlG03BO7V0E54484skUc72ewWvrqhEWTewK%2BjQKKrDPV0hbO72LA4azyvmZjPXT9GVrsRMjNxliYJp5QoHtAX5%2FWvSJBxvKBeKVW6RgpZojir82Z9hK5TnZ%2F1Kv73iHVq23ZgVjSWVCOQZZ6E3zUmEn4tIUkKMvMDyzCa1j0MS8i6qB2HldssijEtXW0Y5MLIUetDJFlvAAmB7BbjA27hxPzos3aNLhPCPCTXIOdOvfr70%2Fp8Y7zEbvbd0GKgYkPEahUm%2F5%2BbkFFpwnj0g%2BAE6Ju4E3jnZUgLVV9DMwOAyib%2BZYHHflWk8UA6Uix2D3e5gQ8%2BS0hezsi2JIPetaxBBs833dx3%2FZhMMf55LwGOqUB7OY%2F1KnAnBZFdli7l%2FPkqsL5%2FD%2FYbxqVTuTyPJe5gKfgPdvWGGzrRSdlWbZI16RbQgFLoWvNCdidFKm%2Bai1c0%2B9mOEUXmgs%2FRsEvrX9DO3yiSiys4rUb2Y8sr5HReGMtU4adXNipWTSR4zvhCxjaF%2FW52CPthe2WBks8TGecR4j6e5IDD1POkzZTvHv%2Bx8YILuydPNZ58io6w8ABVII4TySJvKIK&X-Amz-Signature=fe33067ab60d1c59fa8a00cc1ba731c1f43cfb9ad53669d4f61c4cf0724c380f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
