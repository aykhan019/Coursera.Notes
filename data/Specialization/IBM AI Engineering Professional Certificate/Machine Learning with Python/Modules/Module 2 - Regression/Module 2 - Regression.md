

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UT2RB5B3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcdJ0uakwamyZQ1lqLWczy%2BI1NLFFcKtjRCdriIEJNUAiB%2B7UE4ariN4eSeyrVJOiesL9XLs0h74ewg1py%2BvnI5niqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3ZAIjEq7jHrMnxHzKtwDRWzzgzZd5cW3o67UkEBLYwYhMArfRcfyz2KU8%2FNsgQulgSKAIlFfeJPbmbJ1MG9BQuSt08PUv4mZ6lxquSc2D2Q6GWS9w7J94GswdbB6uTDElAOVNgsuEah8ZWIhmvHpXuA1B3%2BdDX%2Byb%2FK%2FnsI9FF54XdxE4dLJ38f%2FEVKQCNIvUKFI7BLqlibYMvBNQA3nGcfW9ZTnWLk5QFOA5i1lFKviQ6KaKtYw14P3T8oqm4I%2BCCb%2B4Femnfnxk%2F%2BfzhanunSTWXn7AU8sUnuRrqlM43PdvlEwXoItRBtE4Ql8FCVXtXpzUvkLCSaB9Dhxc3L%2BBz7U24U8i9%2BjHn8PZHaA%2BB0xJVXoRCCfhzyNRhU%2FO373lniMdHz2xgf8akMw9bAzjAhg0xZjE1S1OVtN49Z4UlyjweXn%2FQvXxJECyBo57%2FbY5SkoxE3yy3p%2BPHsxFhXRVYtGgiYAyvg1mqk4NAhUeIGFOKNXp5cAtGhHyD4NhzjHIA79SqVnKn9NCWIokvBh2v2G4AXzJ4K1CK7s7LeCCBeLcEgCx3hSA2xIHdPulOMVQzMq6DXq2MCqOUmGq3lLxqFX0tKTz6jk4G1L2itVhrmeToCUIHlbZxUx3ZCkpIghVFh%2Bm6rY2M0dr0kwis7rvAY6pgEtF%2BkdF3CiV8p%2FxKbaa67JSCgDzstwETCM57P6Lz4%2B7H2XEuUObXBhCD5UApERawmZuv6iHLWJRNaIXZPNT165rCfsUsKVDBCKGuZhg%2B%2Fhw02aVYb1NqtAJMijqlwtp6MvTkvqsJZjGK2z8E%2F8x1Vl5%2B%2BzXvTT%2FyOHzrBOhVAJeMeIRNNJEuRFMFtsHbkbd%2BVKNP1%2BS34FP1ih31Gs5mqmCbzRnv%2Fk&X-Amz-Signature=cd43c2472bbef63e92ab59d8cec8ce53a1c93d2bdca1b528c546c3b7dbc7e2ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UT2RB5B3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcdJ0uakwamyZQ1lqLWczy%2BI1NLFFcKtjRCdriIEJNUAiB%2B7UE4ariN4eSeyrVJOiesL9XLs0h74ewg1py%2BvnI5niqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3ZAIjEq7jHrMnxHzKtwDRWzzgzZd5cW3o67UkEBLYwYhMArfRcfyz2KU8%2FNsgQulgSKAIlFfeJPbmbJ1MG9BQuSt08PUv4mZ6lxquSc2D2Q6GWS9w7J94GswdbB6uTDElAOVNgsuEah8ZWIhmvHpXuA1B3%2BdDX%2Byb%2FK%2FnsI9FF54XdxE4dLJ38f%2FEVKQCNIvUKFI7BLqlibYMvBNQA3nGcfW9ZTnWLk5QFOA5i1lFKviQ6KaKtYw14P3T8oqm4I%2BCCb%2B4Femnfnxk%2F%2BfzhanunSTWXn7AU8sUnuRrqlM43PdvlEwXoItRBtE4Ql8FCVXtXpzUvkLCSaB9Dhxc3L%2BBz7U24U8i9%2BjHn8PZHaA%2BB0xJVXoRCCfhzyNRhU%2FO373lniMdHz2xgf8akMw9bAzjAhg0xZjE1S1OVtN49Z4UlyjweXn%2FQvXxJECyBo57%2FbY5SkoxE3yy3p%2BPHsxFhXRVYtGgiYAyvg1mqk4NAhUeIGFOKNXp5cAtGhHyD4NhzjHIA79SqVnKn9NCWIokvBh2v2G4AXzJ4K1CK7s7LeCCBeLcEgCx3hSA2xIHdPulOMVQzMq6DXq2MCqOUmGq3lLxqFX0tKTz6jk4G1L2itVhrmeToCUIHlbZxUx3ZCkpIghVFh%2Bm6rY2M0dr0kwis7rvAY6pgEtF%2BkdF3CiV8p%2FxKbaa67JSCgDzstwETCM57P6Lz4%2B7H2XEuUObXBhCD5UApERawmZuv6iHLWJRNaIXZPNT165rCfsUsKVDBCKGuZhg%2B%2Fhw02aVYb1NqtAJMijqlwtp6MvTkvqsJZjGK2z8E%2F8x1Vl5%2B%2BzXvTT%2FyOHzrBOhVAJeMeIRNNJEuRFMFtsHbkbd%2BVKNP1%2BS34FP1ih31Gs5mqmCbzRnv%2Fk&X-Amz-Signature=248990c80dc6f8c6ae4d094314403e92dcbcb29e336ac995b563d8364c3a979d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UT2RB5B3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcdJ0uakwamyZQ1lqLWczy%2BI1NLFFcKtjRCdriIEJNUAiB%2B7UE4ariN4eSeyrVJOiesL9XLs0h74ewg1py%2BvnI5niqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3ZAIjEq7jHrMnxHzKtwDRWzzgzZd5cW3o67UkEBLYwYhMArfRcfyz2KU8%2FNsgQulgSKAIlFfeJPbmbJ1MG9BQuSt08PUv4mZ6lxquSc2D2Q6GWS9w7J94GswdbB6uTDElAOVNgsuEah8ZWIhmvHpXuA1B3%2BdDX%2Byb%2FK%2FnsI9FF54XdxE4dLJ38f%2FEVKQCNIvUKFI7BLqlibYMvBNQA3nGcfW9ZTnWLk5QFOA5i1lFKviQ6KaKtYw14P3T8oqm4I%2BCCb%2B4Femnfnxk%2F%2BfzhanunSTWXn7AU8sUnuRrqlM43PdvlEwXoItRBtE4Ql8FCVXtXpzUvkLCSaB9Dhxc3L%2BBz7U24U8i9%2BjHn8PZHaA%2BB0xJVXoRCCfhzyNRhU%2FO373lniMdHz2xgf8akMw9bAzjAhg0xZjE1S1OVtN49Z4UlyjweXn%2FQvXxJECyBo57%2FbY5SkoxE3yy3p%2BPHsxFhXRVYtGgiYAyvg1mqk4NAhUeIGFOKNXp5cAtGhHyD4NhzjHIA79SqVnKn9NCWIokvBh2v2G4AXzJ4K1CK7s7LeCCBeLcEgCx3hSA2xIHdPulOMVQzMq6DXq2MCqOUmGq3lLxqFX0tKTz6jk4G1L2itVhrmeToCUIHlbZxUx3ZCkpIghVFh%2Bm6rY2M0dr0kwis7rvAY6pgEtF%2BkdF3CiV8p%2FxKbaa67JSCgDzstwETCM57P6Lz4%2B7H2XEuUObXBhCD5UApERawmZuv6iHLWJRNaIXZPNT165rCfsUsKVDBCKGuZhg%2B%2Fhw02aVYb1NqtAJMijqlwtp6MvTkvqsJZjGK2z8E%2F8x1Vl5%2B%2BzXvTT%2FyOHzrBOhVAJeMeIRNNJEuRFMFtsHbkbd%2BVKNP1%2BS34FP1ih31Gs5mqmCbzRnv%2Fk&X-Amz-Signature=6eb4c301cbed4ec132f27411e1d97b49bdad65603167252395485d9f76cdb5fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UT2RB5B3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcdJ0uakwamyZQ1lqLWczy%2BI1NLFFcKtjRCdriIEJNUAiB%2B7UE4ariN4eSeyrVJOiesL9XLs0h74ewg1py%2BvnI5niqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3ZAIjEq7jHrMnxHzKtwDRWzzgzZd5cW3o67UkEBLYwYhMArfRcfyz2KU8%2FNsgQulgSKAIlFfeJPbmbJ1MG9BQuSt08PUv4mZ6lxquSc2D2Q6GWS9w7J94GswdbB6uTDElAOVNgsuEah8ZWIhmvHpXuA1B3%2BdDX%2Byb%2FK%2FnsI9FF54XdxE4dLJ38f%2FEVKQCNIvUKFI7BLqlibYMvBNQA3nGcfW9ZTnWLk5QFOA5i1lFKviQ6KaKtYw14P3T8oqm4I%2BCCb%2B4Femnfnxk%2F%2BfzhanunSTWXn7AU8sUnuRrqlM43PdvlEwXoItRBtE4Ql8FCVXtXpzUvkLCSaB9Dhxc3L%2BBz7U24U8i9%2BjHn8PZHaA%2BB0xJVXoRCCfhzyNRhU%2FO373lniMdHz2xgf8akMw9bAzjAhg0xZjE1S1OVtN49Z4UlyjweXn%2FQvXxJECyBo57%2FbY5SkoxE3yy3p%2BPHsxFhXRVYtGgiYAyvg1mqk4NAhUeIGFOKNXp5cAtGhHyD4NhzjHIA79SqVnKn9NCWIokvBh2v2G4AXzJ4K1CK7s7LeCCBeLcEgCx3hSA2xIHdPulOMVQzMq6DXq2MCqOUmGq3lLxqFX0tKTz6jk4G1L2itVhrmeToCUIHlbZxUx3ZCkpIghVFh%2Bm6rY2M0dr0kwis7rvAY6pgEtF%2BkdF3CiV8p%2FxKbaa67JSCgDzstwETCM57P6Lz4%2B7H2XEuUObXBhCD5UApERawmZuv6iHLWJRNaIXZPNT165rCfsUsKVDBCKGuZhg%2B%2Fhw02aVYb1NqtAJMijqlwtp6MvTkvqsJZjGK2z8E%2F8x1Vl5%2B%2BzXvTT%2FyOHzrBOhVAJeMeIRNNJEuRFMFtsHbkbd%2BVKNP1%2BS34FP1ih31Gs5mqmCbzRnv%2Fk&X-Amz-Signature=fa163e1d3e4d17330644414b0a5e4e98708042e5ff6dd9908b79e40fe65684f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UT2RB5B3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcdJ0uakwamyZQ1lqLWczy%2BI1NLFFcKtjRCdriIEJNUAiB%2B7UE4ariN4eSeyrVJOiesL9XLs0h74ewg1py%2BvnI5niqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3ZAIjEq7jHrMnxHzKtwDRWzzgzZd5cW3o67UkEBLYwYhMArfRcfyz2KU8%2FNsgQulgSKAIlFfeJPbmbJ1MG9BQuSt08PUv4mZ6lxquSc2D2Q6GWS9w7J94GswdbB6uTDElAOVNgsuEah8ZWIhmvHpXuA1B3%2BdDX%2Byb%2FK%2FnsI9FF54XdxE4dLJ38f%2FEVKQCNIvUKFI7BLqlibYMvBNQA3nGcfW9ZTnWLk5QFOA5i1lFKviQ6KaKtYw14P3T8oqm4I%2BCCb%2B4Femnfnxk%2F%2BfzhanunSTWXn7AU8sUnuRrqlM43PdvlEwXoItRBtE4Ql8FCVXtXpzUvkLCSaB9Dhxc3L%2BBz7U24U8i9%2BjHn8PZHaA%2BB0xJVXoRCCfhzyNRhU%2FO373lniMdHz2xgf8akMw9bAzjAhg0xZjE1S1OVtN49Z4UlyjweXn%2FQvXxJECyBo57%2FbY5SkoxE3yy3p%2BPHsxFhXRVYtGgiYAyvg1mqk4NAhUeIGFOKNXp5cAtGhHyD4NhzjHIA79SqVnKn9NCWIokvBh2v2G4AXzJ4K1CK7s7LeCCBeLcEgCx3hSA2xIHdPulOMVQzMq6DXq2MCqOUmGq3lLxqFX0tKTz6jk4G1L2itVhrmeToCUIHlbZxUx3ZCkpIghVFh%2Bm6rY2M0dr0kwis7rvAY6pgEtF%2BkdF3CiV8p%2FxKbaa67JSCgDzstwETCM57P6Lz4%2B7H2XEuUObXBhCD5UApERawmZuv6iHLWJRNaIXZPNT165rCfsUsKVDBCKGuZhg%2B%2Fhw02aVYb1NqtAJMijqlwtp6MvTkvqsJZjGK2z8E%2F8x1Vl5%2B%2BzXvTT%2FyOHzrBOhVAJeMeIRNNJEuRFMFtsHbkbd%2BVKNP1%2BS34FP1ih31Gs5mqmCbzRnv%2Fk&X-Amz-Signature=cb3438507904a6f1199edd811ad342534bb884e5b7368cd7604bf73f1af0f9cd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UT2RB5B3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcdJ0uakwamyZQ1lqLWczy%2BI1NLFFcKtjRCdriIEJNUAiB%2B7UE4ariN4eSeyrVJOiesL9XLs0h74ewg1py%2BvnI5niqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3ZAIjEq7jHrMnxHzKtwDRWzzgzZd5cW3o67UkEBLYwYhMArfRcfyz2KU8%2FNsgQulgSKAIlFfeJPbmbJ1MG9BQuSt08PUv4mZ6lxquSc2D2Q6GWS9w7J94GswdbB6uTDElAOVNgsuEah8ZWIhmvHpXuA1B3%2BdDX%2Byb%2FK%2FnsI9FF54XdxE4dLJ38f%2FEVKQCNIvUKFI7BLqlibYMvBNQA3nGcfW9ZTnWLk5QFOA5i1lFKviQ6KaKtYw14P3T8oqm4I%2BCCb%2B4Femnfnxk%2F%2BfzhanunSTWXn7AU8sUnuRrqlM43PdvlEwXoItRBtE4Ql8FCVXtXpzUvkLCSaB9Dhxc3L%2BBz7U24U8i9%2BjHn8PZHaA%2BB0xJVXoRCCfhzyNRhU%2FO373lniMdHz2xgf8akMw9bAzjAhg0xZjE1S1OVtN49Z4UlyjweXn%2FQvXxJECyBo57%2FbY5SkoxE3yy3p%2BPHsxFhXRVYtGgiYAyvg1mqk4NAhUeIGFOKNXp5cAtGhHyD4NhzjHIA79SqVnKn9NCWIokvBh2v2G4AXzJ4K1CK7s7LeCCBeLcEgCx3hSA2xIHdPulOMVQzMq6DXq2MCqOUmGq3lLxqFX0tKTz6jk4G1L2itVhrmeToCUIHlbZxUx3ZCkpIghVFh%2Bm6rY2M0dr0kwis7rvAY6pgEtF%2BkdF3CiV8p%2FxKbaa67JSCgDzstwETCM57P6Lz4%2B7H2XEuUObXBhCD5UApERawmZuv6iHLWJRNaIXZPNT165rCfsUsKVDBCKGuZhg%2B%2Fhw02aVYb1NqtAJMijqlwtp6MvTkvqsJZjGK2z8E%2F8x1Vl5%2B%2BzXvTT%2FyOHzrBOhVAJeMeIRNNJEuRFMFtsHbkbd%2BVKNP1%2BS34FP1ih31Gs5mqmCbzRnv%2Fk&X-Amz-Signature=4838c77f86422843f53c77459f1f2b04ad6d7f0d65adbc611b99d8002b432b4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UT2RB5B3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcdJ0uakwamyZQ1lqLWczy%2BI1NLFFcKtjRCdriIEJNUAiB%2B7UE4ariN4eSeyrVJOiesL9XLs0h74ewg1py%2BvnI5niqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3ZAIjEq7jHrMnxHzKtwDRWzzgzZd5cW3o67UkEBLYwYhMArfRcfyz2KU8%2FNsgQulgSKAIlFfeJPbmbJ1MG9BQuSt08PUv4mZ6lxquSc2D2Q6GWS9w7J94GswdbB6uTDElAOVNgsuEah8ZWIhmvHpXuA1B3%2BdDX%2Byb%2FK%2FnsI9FF54XdxE4dLJ38f%2FEVKQCNIvUKFI7BLqlibYMvBNQA3nGcfW9ZTnWLk5QFOA5i1lFKviQ6KaKtYw14P3T8oqm4I%2BCCb%2B4Femnfnxk%2F%2BfzhanunSTWXn7AU8sUnuRrqlM43PdvlEwXoItRBtE4Ql8FCVXtXpzUvkLCSaB9Dhxc3L%2BBz7U24U8i9%2BjHn8PZHaA%2BB0xJVXoRCCfhzyNRhU%2FO373lniMdHz2xgf8akMw9bAzjAhg0xZjE1S1OVtN49Z4UlyjweXn%2FQvXxJECyBo57%2FbY5SkoxE3yy3p%2BPHsxFhXRVYtGgiYAyvg1mqk4NAhUeIGFOKNXp5cAtGhHyD4NhzjHIA79SqVnKn9NCWIokvBh2v2G4AXzJ4K1CK7s7LeCCBeLcEgCx3hSA2xIHdPulOMVQzMq6DXq2MCqOUmGq3lLxqFX0tKTz6jk4G1L2itVhrmeToCUIHlbZxUx3ZCkpIghVFh%2Bm6rY2M0dr0kwis7rvAY6pgEtF%2BkdF3CiV8p%2FxKbaa67JSCgDzstwETCM57P6Lz4%2B7H2XEuUObXBhCD5UApERawmZuv6iHLWJRNaIXZPNT165rCfsUsKVDBCKGuZhg%2B%2Fhw02aVYb1NqtAJMijqlwtp6MvTkvqsJZjGK2z8E%2F8x1Vl5%2B%2BzXvTT%2FyOHzrBOhVAJeMeIRNNJEuRFMFtsHbkbd%2BVKNP1%2BS34FP1ih31Gs5mqmCbzRnv%2Fk&X-Amz-Signature=e471a2e2ef72ab470bf25a550cada1f4fd912c0d9596d3513b1462b9b8456e9d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UT2RB5B3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICcdJ0uakwamyZQ1lqLWczy%2BI1NLFFcKtjRCdriIEJNUAiB%2B7UE4ariN4eSeyrVJOiesL9XLs0h74ewg1py%2BvnI5niqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3ZAIjEq7jHrMnxHzKtwDRWzzgzZd5cW3o67UkEBLYwYhMArfRcfyz2KU8%2FNsgQulgSKAIlFfeJPbmbJ1MG9BQuSt08PUv4mZ6lxquSc2D2Q6GWS9w7J94GswdbB6uTDElAOVNgsuEah8ZWIhmvHpXuA1B3%2BdDX%2Byb%2FK%2FnsI9FF54XdxE4dLJ38f%2FEVKQCNIvUKFI7BLqlibYMvBNQA3nGcfW9ZTnWLk5QFOA5i1lFKviQ6KaKtYw14P3T8oqm4I%2BCCb%2B4Femnfnxk%2F%2BfzhanunSTWXn7AU8sUnuRrqlM43PdvlEwXoItRBtE4Ql8FCVXtXpzUvkLCSaB9Dhxc3L%2BBz7U24U8i9%2BjHn8PZHaA%2BB0xJVXoRCCfhzyNRhU%2FO373lniMdHz2xgf8akMw9bAzjAhg0xZjE1S1OVtN49Z4UlyjweXn%2FQvXxJECyBo57%2FbY5SkoxE3yy3p%2BPHsxFhXRVYtGgiYAyvg1mqk4NAhUeIGFOKNXp5cAtGhHyD4NhzjHIA79SqVnKn9NCWIokvBh2v2G4AXzJ4K1CK7s7LeCCBeLcEgCx3hSA2xIHdPulOMVQzMq6DXq2MCqOUmGq3lLxqFX0tKTz6jk4G1L2itVhrmeToCUIHlbZxUx3ZCkpIghVFh%2Bm6rY2M0dr0kwis7rvAY6pgEtF%2BkdF3CiV8p%2FxKbaa67JSCgDzstwETCM57P6Lz4%2B7H2XEuUObXBhCD5UApERawmZuv6iHLWJRNaIXZPNT165rCfsUsKVDBCKGuZhg%2B%2Fhw02aVYb1NqtAJMijqlwtp6MvTkvqsJZjGK2z8E%2F8x1Vl5%2B%2BzXvTT%2FyOHzrBOhVAJeMeIRNNJEuRFMFtsHbkbd%2BVKNP1%2BS34FP1ih31Gs5mqmCbzRnv%2Fk&X-Amz-Signature=ec9cf1fc51566554bba07a2da7641781f75a1329e891dda81102a9909022975c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664S5IN3QB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFXwPE%2B38%2ByX7uI7tRB1pZRORzcw0oyXNR9Fp%2FzuACnbAiEA46bMeV%2FIqpDLSFGNbiyEJPv8mczYrR9DePdI514IA9oqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD1W6it3894ZLXR2zircA9mKzfSZkRDA%2BxI904p%2FG0x9k7HzGVDjH79RRZeFB7tPKuwziVB%2B0%2FgHR9RQP4ztb388x%2BEF5duYzQOW%2Bdq8WgOGhSajBRvEZUGnmrsctJP7whliz7SxpQyjZrjlV5gkhtYfH0QrjEDRun14p5v8Ej3it9hZuE10L%2FUAbWSnmQ4%2BlROxg4LAi4SSblfvESPYZ2vRnJrMTV6yVo5pK5C8Ia%2BcTCTuiMTyFgeK1UmNaw33vpelcZC%2Bb0rPzpCvzhnmoBB33mqtRacbOSlpEdxUC%2FEQczcR06Y51XjJEbnqEh%2FvL0j0Zl9bhHmnaFBGltZitJ7RQuAe%2F2yJZfGla9toLVVfTMFNV2XeEqrKT5fuDSUBz2TmQ%2BP9vkWbXlDqYrnMovHZHtZvr5Ru%2F49zja1EgBK%2FIxvZaeOeF8Xn%2B7gXXB%2BzvEvuxMyYy%2FB5%2B6pAaykKcAX4gL%2B6IXRRU%2FSw6fWvq%2BwtKhXZMM5CU047M2n2I8U32Gn9EmAoCiU8xAIfGveXhAZxyo7BevbR%2Fci%2F6KUtlQjpI5m4VisZn5BUQfBxQi1d2fJlL6MtvqDjHf80Vh6aFt5yuDgul0%2B98obFP1m1eNgQCy2Xmdj29FBjeo3knxMfmrZxtcw6R6swqxhGMIfO67wGOqUBk8KD67xSnIa83kkpwII9gt7T2nkyZJerZe8aOmdt2tYA%2BYblC1ifjmBGKI7wsYKkQsacFRt2iI6lyEa%2FjZJuFQchLoDH4fu%2FFXJlcJSsVeYE0%2FEHS043SIWWZj%2BBUg924UwYls8lRlb2wS7FiQnj6FZQNWe5OCOFSqLsAKo3U7WHzDmADy9Qw9BH5LcEFeuGIZChoImBuNYwr0iyHcXYFhSL5To8&X-Amz-Signature=941169850b08521932e0c3e05d94a1217b649ebf4dc970b87b647e2620d1e497&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ODX6FCA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF3MWVV7TfekFYzqZagj6uS5BNWyWSbdPoi3ouaXe8dJAiAvsYBzY1La2I6jOd6AhCo6tZfzafMlmx9Uz9AMFh6APCqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWuUHTdHTWs3MB3QlKtwDg767e0BrFcYyadJtDKoGuGKG1ysIQD%2BjtjEBa7Ix1UU%2FwwgA1Xz7TtPRHHsKGZuCc1YfkFnwMuFWB3NDI8bgkCcWPNFF92yS45JmadsdJiJz0aRPDhlQucdAw9p14DWeAapF1vzpv0%2BjwZYW%2BKX7y7F9QtdZfcjPHm8ff49qllbAhcwXvgyMjRrrCKV3TZ9PHbplG2TJ22r9jjdzS9cs6N14roSbBRzglDXmSMxTxvOtYxUA979KE32XUiuqmL%2Fl57q49n9dSDNSbN0lovuniEcy8VJaKY6658h9m%2FE4yGnoFBTYH4LqOD%2B5entbqzgfKbWvEwdeCUBfFyiugYu1t%2FCVP6nLhhd1Fwv%2FkuZvvniiRbye4uHgmJlfCHRCmP4MpnvVSXYZlbyBFYOsRSDjvHByjuuyNRIDmPrKa4ZVxukOyISaCalmj2yuqlgS%2Bkqc0E0FVDN3WnpR81tchqcxDU7qV%2FtcOVD5eEx47daRESx8j6B8nxyoGPCnFsHNM8OWIugWG17LG5LJMAeLDYpDtrWVaBqkQ6pa30vyd5NdKgYhB%2BkbB4EBOS6BZAGjIKLZg%2FEl4dOgc9h3lyHDSClgQOPuz4DBtJSqRes0686%2B4XUaX7oDZpCo%2B6JBx%2F4wzc%2FrvAY6pgHcLOLKcAOYRaRF5L%2FKRnfpLzvPouKinZ4WFQUbAw6VHzwMbMjfq9L4DMpVz3NO91QmB1403XEGM43kgfguuwe4EXMEAF1CvZZpr9SvMFxBvMo5b9Az%2F6V2o3SstECBe3LTZ10dfqbrbPH53Z60YDT39tb2UK79WdBZG8fQJSojXCtPxuzWT7IWHdD0CDsHTyRInRnAJOlkwPNTsnPK0ZCah8oEb6oT&X-Amz-Signature=2c93236b8d38290ac9d5d7d4939befb4bd8de165d3cdb12bc0762054e41727b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPULKJZY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsXrcFWqr508TbTi%2BZJxL4BnC7iYu9qjaOYOQqs1vcNAIgRlwgIjaJKcuk9ertNcioKPJtJmHcEDGjggBjyQ882ywqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDCMuVBV2z8lTvu5XCrcAzrrRAgoXDJbDc6Io%2FPwzmWdPc8eP2TqrLSVZhkQ1wjUdegi3uARiHB76e0jJCKfv%2BW5R6e9ne%2BedWih29FU3H9T%2FbD50doDTOPkryYdY6u8PIQme5umup1noAUKedFmI40mC00tT9PvVi1fvY%2BHpLZdY04NzWkHCOzdsjYwOiWr7hwZksOZt7A14G7dtiMk0JvzHCymU6SFHPjuTpMDGP%2F7YsCuVmBySr9j2gvIRc%2BVGqVv5mkYHmlJG9iOykj5hWI71wDzRHEcYWFoxMh8JK3tFBL5lxTQzBOsU%2F3DecigNSKQXyUKXj7DIZ4cxEfMvKUB0WenPjfuDtp8Nwav8ZTFgFYfpjLOERGM01w5TojRjYxUIOKnKqkaUem3CGPrtY7X3gDoFamMzGGO6ZmL2vUUHEsMXz6fB3Myj14YCfu82MSn11lEYL7X4rjllaPdUbi1aNIjsU%2Bt79UbYqDBR9G7UAeTsxU%2FFanXFGXmu5RhckiCPzXJDu9bzY8ILn9z9e%2B98k9vWivRX%2BdOMG0JZ1ym5MDJqpQZWQfzpFA3JxHZ22HJ2iVG6CA9%2BPgZ9S7prGHKVsd7U7Qa3NkFgGbJEXsqzBIrWtoQxsy2fwU7aZSFb%2ByZHA%2FC%2FzOdeEZnMMPO67wGOqUBHRnhzlsW2%2BHLH60a1RlwqcJHo11xrxMA26nG5767imRc8rhISLcpw86XF0E9Blk3k49D87dYiXqk1kuUCYfszJDfhXPSgXHHsj0HqaSqsKg%2Bss7NX1v%2BctQ7vgwALBIeXmSroESaGquoYQDRtJ9lqQEn8fo1PaR02lnzMLqD%2BUdhHtLZGNPzDuspxkKjUx4gK7suVppQirL%2Fgfrv0UfKZM4P9Glg&X-Amz-Signature=ae9786892e6d36d7233c6e6aa149eba27dc807af90855c2af91cece98fa1177c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPULKJZY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsXrcFWqr508TbTi%2BZJxL4BnC7iYu9qjaOYOQqs1vcNAIgRlwgIjaJKcuk9ertNcioKPJtJmHcEDGjggBjyQ882ywqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDCMuVBV2z8lTvu5XCrcAzrrRAgoXDJbDc6Io%2FPwzmWdPc8eP2TqrLSVZhkQ1wjUdegi3uARiHB76e0jJCKfv%2BW5R6e9ne%2BedWih29FU3H9T%2FbD50doDTOPkryYdY6u8PIQme5umup1noAUKedFmI40mC00tT9PvVi1fvY%2BHpLZdY04NzWkHCOzdsjYwOiWr7hwZksOZt7A14G7dtiMk0JvzHCymU6SFHPjuTpMDGP%2F7YsCuVmBySr9j2gvIRc%2BVGqVv5mkYHmlJG9iOykj5hWI71wDzRHEcYWFoxMh8JK3tFBL5lxTQzBOsU%2F3DecigNSKQXyUKXj7DIZ4cxEfMvKUB0WenPjfuDtp8Nwav8ZTFgFYfpjLOERGM01w5TojRjYxUIOKnKqkaUem3CGPrtY7X3gDoFamMzGGO6ZmL2vUUHEsMXz6fB3Myj14YCfu82MSn11lEYL7X4rjllaPdUbi1aNIjsU%2Bt79UbYqDBR9G7UAeTsxU%2FFanXFGXmu5RhckiCPzXJDu9bzY8ILn9z9e%2B98k9vWivRX%2BdOMG0JZ1ym5MDJqpQZWQfzpFA3JxHZ22HJ2iVG6CA9%2BPgZ9S7prGHKVsd7U7Qa3NkFgGbJEXsqzBIrWtoQxsy2fwU7aZSFb%2ByZHA%2FC%2FzOdeEZnMMPO67wGOqUBHRnhzlsW2%2BHLH60a1RlwqcJHo11xrxMA26nG5767imRc8rhISLcpw86XF0E9Blk3k49D87dYiXqk1kuUCYfszJDfhXPSgXHHsj0HqaSqsKg%2Bss7NX1v%2BctQ7vgwALBIeXmSroESaGquoYQDRtJ9lqQEn8fo1PaR02lnzMLqD%2BUdhHtLZGNPzDuspxkKjUx4gK7suVppQirL%2Fgfrv0UfKZM4P9Glg&X-Amz-Signature=509192b0b4ee1afce069dbd468705258f3e100257fc90bc7ebfd081770c9f5a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
