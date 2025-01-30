

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA3BQSRE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6SRtGrNZIWdVaXtwm%2BQkCoIqf3fhfQOJ6NOQfPEVuQwIgItX89vX8Ilq5Iz70V%2BXNXsC3FAJ%2FkYFMlFxdK5m3YtsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBvUIhKdBrSqUlKwBSrcA%2BdRqUIIlN1bLBZR6HYBN7Ayb4hcx1eDZQ8Mx2VNgIQd4cJAW%2BA9h9Q%2F1A7TNIg%2FuFculAhySvANpmdvVDCrumFgrorS0epNmVVMgKRgNto1m5CrIipje%2BcT1mmxZoP%2Fn6D%2FzoVIRbvWboBh0C78Tb0UPQcTu0q64eBPS6dQFpd6X%2FNKAd%2BYaBuSkU0%2BQVtvhSKaHDU8YmzoFIXeBgHYX7%2FRpqa5JgPCemfQTvxlqctEXI7NR6B723pVcAO5h6gC%2BtnQZuYTGBdNEPP9%2FjZQouXmcadjW2iFMd2hDO9IM7Aeh0SUepkkTx3sH8tFWy4M9neaW%2BjFEBHWCp5i%2Fbl0WVO0RD3yGr3V6ckz5dTAoGiVGlkOYOpsH7x9nLb17q3NZCVkID2Np5RciHgZ%2F%2B1sasPzgZBvm8S47XcvN8v8Ne2VYVg8SqxO7tB0KeTwG%2FeFwqOgJiqm2CRUzdPb6iezwzhUKEXJ6FGc%2BihgT7W8VSZ5ondQMLDM1dLuLs9PBBikt%2FxkWVmu27%2BUlVlDkij0uybr7Zvu7EmumFLgTnWl3pdeQMuFk66gdb0Wrkew0j%2F84zwQLia8JA%2BU%2Brv%2FKE9fVVISxN%2FTaSFPjf7ZFznJ1EZzIiwORrPxEbYkdWqYMI3f7bwGOqUB1q2fCj5nDIGTSr4KUf6qPfhMgsJQW6bMNe4jqHTaN4keu25KUwXEFhEH60b6ziLanhhjCbNh%2FPXpyhS2QjnKw54DYF5Wvn16BSsTknuwG1ZopULWDpOZ88t%2Bg7fvvVn46CXTU9Mxzndxam9drLTPQ9Ou2zfDxoGzPd3Y3vafXb7mheNuS%2FzrpbcAciiAsb0UmLwOVAPHuA%2FgcPHv8%2BaB2%2FPnCfQb&X-Amz-Signature=d8b1ac47fb397fb8a8d0615bc3c4277921f9bc1ff4dd7a0f242c326b17c90ee0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA3BQSRE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6SRtGrNZIWdVaXtwm%2BQkCoIqf3fhfQOJ6NOQfPEVuQwIgItX89vX8Ilq5Iz70V%2BXNXsC3FAJ%2FkYFMlFxdK5m3YtsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBvUIhKdBrSqUlKwBSrcA%2BdRqUIIlN1bLBZR6HYBN7Ayb4hcx1eDZQ8Mx2VNgIQd4cJAW%2BA9h9Q%2F1A7TNIg%2FuFculAhySvANpmdvVDCrumFgrorS0epNmVVMgKRgNto1m5CrIipje%2BcT1mmxZoP%2Fn6D%2FzoVIRbvWboBh0C78Tb0UPQcTu0q64eBPS6dQFpd6X%2FNKAd%2BYaBuSkU0%2BQVtvhSKaHDU8YmzoFIXeBgHYX7%2FRpqa5JgPCemfQTvxlqctEXI7NR6B723pVcAO5h6gC%2BtnQZuYTGBdNEPP9%2FjZQouXmcadjW2iFMd2hDO9IM7Aeh0SUepkkTx3sH8tFWy4M9neaW%2BjFEBHWCp5i%2Fbl0WVO0RD3yGr3V6ckz5dTAoGiVGlkOYOpsH7x9nLb17q3NZCVkID2Np5RciHgZ%2F%2B1sasPzgZBvm8S47XcvN8v8Ne2VYVg8SqxO7tB0KeTwG%2FeFwqOgJiqm2CRUzdPb6iezwzhUKEXJ6FGc%2BihgT7W8VSZ5ondQMLDM1dLuLs9PBBikt%2FxkWVmu27%2BUlVlDkij0uybr7Zvu7EmumFLgTnWl3pdeQMuFk66gdb0Wrkew0j%2F84zwQLia8JA%2BU%2Brv%2FKE9fVVISxN%2FTaSFPjf7ZFznJ1EZzIiwORrPxEbYkdWqYMI3f7bwGOqUB1q2fCj5nDIGTSr4KUf6qPfhMgsJQW6bMNe4jqHTaN4keu25KUwXEFhEH60b6ziLanhhjCbNh%2FPXpyhS2QjnKw54DYF5Wvn16BSsTknuwG1ZopULWDpOZ88t%2Bg7fvvVn46CXTU9Mxzndxam9drLTPQ9Ou2zfDxoGzPd3Y3vafXb7mheNuS%2FzrpbcAciiAsb0UmLwOVAPHuA%2FgcPHv8%2BaB2%2FPnCfQb&X-Amz-Signature=24d45bf562a5c9b3ac4db26ba28c11e5bd21640ce201376f2d78dbdfa1fb8127&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA3BQSRE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6SRtGrNZIWdVaXtwm%2BQkCoIqf3fhfQOJ6NOQfPEVuQwIgItX89vX8Ilq5Iz70V%2BXNXsC3FAJ%2FkYFMlFxdK5m3YtsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBvUIhKdBrSqUlKwBSrcA%2BdRqUIIlN1bLBZR6HYBN7Ayb4hcx1eDZQ8Mx2VNgIQd4cJAW%2BA9h9Q%2F1A7TNIg%2FuFculAhySvANpmdvVDCrumFgrorS0epNmVVMgKRgNto1m5CrIipje%2BcT1mmxZoP%2Fn6D%2FzoVIRbvWboBh0C78Tb0UPQcTu0q64eBPS6dQFpd6X%2FNKAd%2BYaBuSkU0%2BQVtvhSKaHDU8YmzoFIXeBgHYX7%2FRpqa5JgPCemfQTvxlqctEXI7NR6B723pVcAO5h6gC%2BtnQZuYTGBdNEPP9%2FjZQouXmcadjW2iFMd2hDO9IM7Aeh0SUepkkTx3sH8tFWy4M9neaW%2BjFEBHWCp5i%2Fbl0WVO0RD3yGr3V6ckz5dTAoGiVGlkOYOpsH7x9nLb17q3NZCVkID2Np5RciHgZ%2F%2B1sasPzgZBvm8S47XcvN8v8Ne2VYVg8SqxO7tB0KeTwG%2FeFwqOgJiqm2CRUzdPb6iezwzhUKEXJ6FGc%2BihgT7W8VSZ5ondQMLDM1dLuLs9PBBikt%2FxkWVmu27%2BUlVlDkij0uybr7Zvu7EmumFLgTnWl3pdeQMuFk66gdb0Wrkew0j%2F84zwQLia8JA%2BU%2Brv%2FKE9fVVISxN%2FTaSFPjf7ZFznJ1EZzIiwORrPxEbYkdWqYMI3f7bwGOqUB1q2fCj5nDIGTSr4KUf6qPfhMgsJQW6bMNe4jqHTaN4keu25KUwXEFhEH60b6ziLanhhjCbNh%2FPXpyhS2QjnKw54DYF5Wvn16BSsTknuwG1ZopULWDpOZ88t%2Bg7fvvVn46CXTU9Mxzndxam9drLTPQ9Ou2zfDxoGzPd3Y3vafXb7mheNuS%2FzrpbcAciiAsb0UmLwOVAPHuA%2FgcPHv8%2BaB2%2FPnCfQb&X-Amz-Signature=1b634de00c7b2ca379c85694dd18f672673db08082280646e7835e2938c31bd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA3BQSRE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6SRtGrNZIWdVaXtwm%2BQkCoIqf3fhfQOJ6NOQfPEVuQwIgItX89vX8Ilq5Iz70V%2BXNXsC3FAJ%2FkYFMlFxdK5m3YtsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBvUIhKdBrSqUlKwBSrcA%2BdRqUIIlN1bLBZR6HYBN7Ayb4hcx1eDZQ8Mx2VNgIQd4cJAW%2BA9h9Q%2F1A7TNIg%2FuFculAhySvANpmdvVDCrumFgrorS0epNmVVMgKRgNto1m5CrIipje%2BcT1mmxZoP%2Fn6D%2FzoVIRbvWboBh0C78Tb0UPQcTu0q64eBPS6dQFpd6X%2FNKAd%2BYaBuSkU0%2BQVtvhSKaHDU8YmzoFIXeBgHYX7%2FRpqa5JgPCemfQTvxlqctEXI7NR6B723pVcAO5h6gC%2BtnQZuYTGBdNEPP9%2FjZQouXmcadjW2iFMd2hDO9IM7Aeh0SUepkkTx3sH8tFWy4M9neaW%2BjFEBHWCp5i%2Fbl0WVO0RD3yGr3V6ckz5dTAoGiVGlkOYOpsH7x9nLb17q3NZCVkID2Np5RciHgZ%2F%2B1sasPzgZBvm8S47XcvN8v8Ne2VYVg8SqxO7tB0KeTwG%2FeFwqOgJiqm2CRUzdPb6iezwzhUKEXJ6FGc%2BihgT7W8VSZ5ondQMLDM1dLuLs9PBBikt%2FxkWVmu27%2BUlVlDkij0uybr7Zvu7EmumFLgTnWl3pdeQMuFk66gdb0Wrkew0j%2F84zwQLia8JA%2BU%2Brv%2FKE9fVVISxN%2FTaSFPjf7ZFznJ1EZzIiwORrPxEbYkdWqYMI3f7bwGOqUB1q2fCj5nDIGTSr4KUf6qPfhMgsJQW6bMNe4jqHTaN4keu25KUwXEFhEH60b6ziLanhhjCbNh%2FPXpyhS2QjnKw54DYF5Wvn16BSsTknuwG1ZopULWDpOZ88t%2Bg7fvvVn46CXTU9Mxzndxam9drLTPQ9Ou2zfDxoGzPd3Y3vafXb7mheNuS%2FzrpbcAciiAsb0UmLwOVAPHuA%2FgcPHv8%2BaB2%2FPnCfQb&X-Amz-Signature=fff41222b3debd12b3f504e603f277362e6991312c462f71b1eaf929de5c1393&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA3BQSRE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6SRtGrNZIWdVaXtwm%2BQkCoIqf3fhfQOJ6NOQfPEVuQwIgItX89vX8Ilq5Iz70V%2BXNXsC3FAJ%2FkYFMlFxdK5m3YtsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBvUIhKdBrSqUlKwBSrcA%2BdRqUIIlN1bLBZR6HYBN7Ayb4hcx1eDZQ8Mx2VNgIQd4cJAW%2BA9h9Q%2F1A7TNIg%2FuFculAhySvANpmdvVDCrumFgrorS0epNmVVMgKRgNto1m5CrIipje%2BcT1mmxZoP%2Fn6D%2FzoVIRbvWboBh0C78Tb0UPQcTu0q64eBPS6dQFpd6X%2FNKAd%2BYaBuSkU0%2BQVtvhSKaHDU8YmzoFIXeBgHYX7%2FRpqa5JgPCemfQTvxlqctEXI7NR6B723pVcAO5h6gC%2BtnQZuYTGBdNEPP9%2FjZQouXmcadjW2iFMd2hDO9IM7Aeh0SUepkkTx3sH8tFWy4M9neaW%2BjFEBHWCp5i%2Fbl0WVO0RD3yGr3V6ckz5dTAoGiVGlkOYOpsH7x9nLb17q3NZCVkID2Np5RciHgZ%2F%2B1sasPzgZBvm8S47XcvN8v8Ne2VYVg8SqxO7tB0KeTwG%2FeFwqOgJiqm2CRUzdPb6iezwzhUKEXJ6FGc%2BihgT7W8VSZ5ondQMLDM1dLuLs9PBBikt%2FxkWVmu27%2BUlVlDkij0uybr7Zvu7EmumFLgTnWl3pdeQMuFk66gdb0Wrkew0j%2F84zwQLia8JA%2BU%2Brv%2FKE9fVVISxN%2FTaSFPjf7ZFznJ1EZzIiwORrPxEbYkdWqYMI3f7bwGOqUB1q2fCj5nDIGTSr4KUf6qPfhMgsJQW6bMNe4jqHTaN4keu25KUwXEFhEH60b6ziLanhhjCbNh%2FPXpyhS2QjnKw54DYF5Wvn16BSsTknuwG1ZopULWDpOZ88t%2Bg7fvvVn46CXTU9Mxzndxam9drLTPQ9Ou2zfDxoGzPd3Y3vafXb7mheNuS%2FzrpbcAciiAsb0UmLwOVAPHuA%2FgcPHv8%2BaB2%2FPnCfQb&X-Amz-Signature=1abeeeb6be57f08f863dd04c066cc392aabbab2873b4a8907d120dbd11413a2b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA3BQSRE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6SRtGrNZIWdVaXtwm%2BQkCoIqf3fhfQOJ6NOQfPEVuQwIgItX89vX8Ilq5Iz70V%2BXNXsC3FAJ%2FkYFMlFxdK5m3YtsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBvUIhKdBrSqUlKwBSrcA%2BdRqUIIlN1bLBZR6HYBN7Ayb4hcx1eDZQ8Mx2VNgIQd4cJAW%2BA9h9Q%2F1A7TNIg%2FuFculAhySvANpmdvVDCrumFgrorS0epNmVVMgKRgNto1m5CrIipje%2BcT1mmxZoP%2Fn6D%2FzoVIRbvWboBh0C78Tb0UPQcTu0q64eBPS6dQFpd6X%2FNKAd%2BYaBuSkU0%2BQVtvhSKaHDU8YmzoFIXeBgHYX7%2FRpqa5JgPCemfQTvxlqctEXI7NR6B723pVcAO5h6gC%2BtnQZuYTGBdNEPP9%2FjZQouXmcadjW2iFMd2hDO9IM7Aeh0SUepkkTx3sH8tFWy4M9neaW%2BjFEBHWCp5i%2Fbl0WVO0RD3yGr3V6ckz5dTAoGiVGlkOYOpsH7x9nLb17q3NZCVkID2Np5RciHgZ%2F%2B1sasPzgZBvm8S47XcvN8v8Ne2VYVg8SqxO7tB0KeTwG%2FeFwqOgJiqm2CRUzdPb6iezwzhUKEXJ6FGc%2BihgT7W8VSZ5ondQMLDM1dLuLs9PBBikt%2FxkWVmu27%2BUlVlDkij0uybr7Zvu7EmumFLgTnWl3pdeQMuFk66gdb0Wrkew0j%2F84zwQLia8JA%2BU%2Brv%2FKE9fVVISxN%2FTaSFPjf7ZFznJ1EZzIiwORrPxEbYkdWqYMI3f7bwGOqUB1q2fCj5nDIGTSr4KUf6qPfhMgsJQW6bMNe4jqHTaN4keu25KUwXEFhEH60b6ziLanhhjCbNh%2FPXpyhS2QjnKw54DYF5Wvn16BSsTknuwG1ZopULWDpOZ88t%2Bg7fvvVn46CXTU9Mxzndxam9drLTPQ9Ou2zfDxoGzPd3Y3vafXb7mheNuS%2FzrpbcAciiAsb0UmLwOVAPHuA%2FgcPHv8%2BaB2%2FPnCfQb&X-Amz-Signature=9cbacc2c9cdc4d40ee1ceb0acab800cf256200866cf5ef32e1f0a6f17e48ff43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA3BQSRE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6SRtGrNZIWdVaXtwm%2BQkCoIqf3fhfQOJ6NOQfPEVuQwIgItX89vX8Ilq5Iz70V%2BXNXsC3FAJ%2FkYFMlFxdK5m3YtsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBvUIhKdBrSqUlKwBSrcA%2BdRqUIIlN1bLBZR6HYBN7Ayb4hcx1eDZQ8Mx2VNgIQd4cJAW%2BA9h9Q%2F1A7TNIg%2FuFculAhySvANpmdvVDCrumFgrorS0epNmVVMgKRgNto1m5CrIipje%2BcT1mmxZoP%2Fn6D%2FzoVIRbvWboBh0C78Tb0UPQcTu0q64eBPS6dQFpd6X%2FNKAd%2BYaBuSkU0%2BQVtvhSKaHDU8YmzoFIXeBgHYX7%2FRpqa5JgPCemfQTvxlqctEXI7NR6B723pVcAO5h6gC%2BtnQZuYTGBdNEPP9%2FjZQouXmcadjW2iFMd2hDO9IM7Aeh0SUepkkTx3sH8tFWy4M9neaW%2BjFEBHWCp5i%2Fbl0WVO0RD3yGr3V6ckz5dTAoGiVGlkOYOpsH7x9nLb17q3NZCVkID2Np5RciHgZ%2F%2B1sasPzgZBvm8S47XcvN8v8Ne2VYVg8SqxO7tB0KeTwG%2FeFwqOgJiqm2CRUzdPb6iezwzhUKEXJ6FGc%2BihgT7W8VSZ5ondQMLDM1dLuLs9PBBikt%2FxkWVmu27%2BUlVlDkij0uybr7Zvu7EmumFLgTnWl3pdeQMuFk66gdb0Wrkew0j%2F84zwQLia8JA%2BU%2Brv%2FKE9fVVISxN%2FTaSFPjf7ZFznJ1EZzIiwORrPxEbYkdWqYMI3f7bwGOqUB1q2fCj5nDIGTSr4KUf6qPfhMgsJQW6bMNe4jqHTaN4keu25KUwXEFhEH60b6ziLanhhjCbNh%2FPXpyhS2QjnKw54DYF5Wvn16BSsTknuwG1ZopULWDpOZ88t%2Bg7fvvVn46CXTU9Mxzndxam9drLTPQ9Ou2zfDxoGzPd3Y3vafXb7mheNuS%2FzrpbcAciiAsb0UmLwOVAPHuA%2FgcPHv8%2BaB2%2FPnCfQb&X-Amz-Signature=e81f5e30c22ca74f71c0d79f9835d1640d07bfa11519894a448bb4f1d7d4c0a2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA3BQSRE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6SRtGrNZIWdVaXtwm%2BQkCoIqf3fhfQOJ6NOQfPEVuQwIgItX89vX8Ilq5Iz70V%2BXNXsC3FAJ%2FkYFMlFxdK5m3YtsqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBvUIhKdBrSqUlKwBSrcA%2BdRqUIIlN1bLBZR6HYBN7Ayb4hcx1eDZQ8Mx2VNgIQd4cJAW%2BA9h9Q%2F1A7TNIg%2FuFculAhySvANpmdvVDCrumFgrorS0epNmVVMgKRgNto1m5CrIipje%2BcT1mmxZoP%2Fn6D%2FzoVIRbvWboBh0C78Tb0UPQcTu0q64eBPS6dQFpd6X%2FNKAd%2BYaBuSkU0%2BQVtvhSKaHDU8YmzoFIXeBgHYX7%2FRpqa5JgPCemfQTvxlqctEXI7NR6B723pVcAO5h6gC%2BtnQZuYTGBdNEPP9%2FjZQouXmcadjW2iFMd2hDO9IM7Aeh0SUepkkTx3sH8tFWy4M9neaW%2BjFEBHWCp5i%2Fbl0WVO0RD3yGr3V6ckz5dTAoGiVGlkOYOpsH7x9nLb17q3NZCVkID2Np5RciHgZ%2F%2B1sasPzgZBvm8S47XcvN8v8Ne2VYVg8SqxO7tB0KeTwG%2FeFwqOgJiqm2CRUzdPb6iezwzhUKEXJ6FGc%2BihgT7W8VSZ5ondQMLDM1dLuLs9PBBikt%2FxkWVmu27%2BUlVlDkij0uybr7Zvu7EmumFLgTnWl3pdeQMuFk66gdb0Wrkew0j%2F84zwQLia8JA%2BU%2Brv%2FKE9fVVISxN%2FTaSFPjf7ZFznJ1EZzIiwORrPxEbYkdWqYMI3f7bwGOqUB1q2fCj5nDIGTSr4KUf6qPfhMgsJQW6bMNe4jqHTaN4keu25KUwXEFhEH60b6ziLanhhjCbNh%2FPXpyhS2QjnKw54DYF5Wvn16BSsTknuwG1ZopULWDpOZ88t%2Bg7fvvVn46CXTU9Mxzndxam9drLTPQ9Ou2zfDxoGzPd3Y3vafXb7mheNuS%2FzrpbcAciiAsb0UmLwOVAPHuA%2FgcPHv8%2BaB2%2FPnCfQb&X-Amz-Signature=2c3f13948000b039d140dbfc520de56b5492193b345729e9d807a19a6d534905&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665HHN7AH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0ZnW1%2BCoJ43%2BB6WYQ3M0%2BshmfCM3gmS2UfAZsNws9oQIhAK%2BZwpZx3flKTw7jDC%2FEOvCok1bJU5xPnoeENaNAIUBxKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybkTgNEPQoBQPcQikq3AOgsAVRW7fR1kcAE7Mp7nYMidsS93IyHYrBivoZmXQEQPd5gUeO7ZQSvw6Irj8r5sMgmH9XyfxJ%2BHvLv5g9fWYSBlOxCDKtorG99y8ef66yeZIIvnuzL7kMWGWcmJHoFa6BpWIPBu2eshGZJbNuLnPyitt%2F%2ByuBv1lwvn8ZIQNv9dJ%2BC2ElPyh2qbMHlpQLQYhJbGTdUDfayr0s9JLvuGc83a7X18nt%2FA3S6Y%2F810EyouY%2BQz1xNClL3eKUxxLA7HgVbRJC%2B8BWuAIaiWPRy2qzVFFERqNO%2FIO%2BpO8iiQOfbjZ%2FzUwGCmvuQh1NDuCeurBAWYLteqU%2FDo7srlp1yFu8X5auJ1pT0J2ARyp5dQz%2Bad5B7KamNoUc8WhBoNWuc%2BvceD1eJsgfufgD5%2BOu%2BPu1vFOpDtVxQh6ed%2FokBIUTPHPWVuRU%2BOPcD4JZbxrLh01p6qdzJsLtw49dDWpt%2F81zKcA7fD5wTbqHcERw3p0Yp1DDWPkmWh1lRKBbXus%2FBgBWB67dRRGG%2BD4uuEYPJ2HHBiRDbNjVsUIaG7WT%2Bf%2BVUpsVOCwQY3%2BFDBsxKi8wW0ujl1MeEu%2BPk0rtbqp%2BwYg0t623xxJQXnTIIS8wz%2FFeTXKMZT8kE7pZGIc4dTCz3u28BjqkAT9ETrtvmmxmmrzxaQripZDb39W3XttkO%2BnYVThwBzl06H0mqAQkk%2FSaRHJIJu%2FQ7dLO%2FlyJtecF9lb53gUfKopoFj%2BwNpAwG%2BwJfHmkFk4xTm4IFGw8sUPOaXUSmLE7CF90DuWL7xPh5EocUGFuMqUJcPvIjnD9QkJLFA61H4%2FZOVejZ0VlXllTFFR%2FOYt9JTp3xcyoeuBAUG1RC4jRz0y1StEy&X-Amz-Signature=26b7a6d7661398a632781b687317b10550fedaaa2e9df0bc6f0b75cf92fd2c1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653T5LSD2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE%2Bi%2BRMhbxJv6oNEwZLjaOvbZUTw2%2FOwW%2BxPX0PNX6mwAiEA4tLf5FUQTcUQk9TOEnnOMSPb3SvsxBqb74E%2FxCIzaVsqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGCjVZ%2Bl7XxtDp63GSrcA4fLxqagvT6HseUuDyEFT9Df9yu%2BheAI0ZSyznoTmPFNzM5xFDj0TSo03i%2FmMD2yGDVilksLDk34Qf8Kwci3LsLATyIBkG9%2BFSDu9gK10b9J1u9ttyXhQGX4xRXlsuz5FVVufa2gOFlPtH2mUOQ91UZuF6G0kWMkeR4K%2BsQCEONo8XAtalNRt8zsNsSqH2OiVs4JC0UPsr7orEZbZuJTrb2OncrosGRiMekcR5bdkLrcBd%2FBqIVAsOfh%2BwdKOMaF%2Fp8DmcdU2xymcvZH4DDZqrjDcwMNQAXxmy7dvHi4XRKFOWJDyQsrauW0Xnp2lDaJX13%2Bsh%2BcOGTvj4%2B6m6y2EMmVi1I%2Bddcwjub7GOULyDRry5mph50Qn0%2B8147wg%2BqMeTSrBtUId5nUQg2HADRw59woO%2BDA%2FKuub1d%2FEyBQ%2BH25EVjB2vSlATak199cY5fTa7IiTr%2BJ%2Flezgqgb08Ag3ivDQR4xiFyeXTCvzAlJxV6knIqNW62RCztc7UceHq3nDiC3nVomW%2BRmet2eTtVkyhVfAabiVQrptTePSyYsN7hgugJamQK3m90WWSr%2FTFhc3V4mJQaJudMq1tieR1l%2FNxyqfsO9byLHd1ljBgPyckmTAs8CxQCeAqR5cb%2FxML7e7bwGOqUBjAnG6OM28INPIatbdRr5lT6uOlbWrL3Dh02tJ40cVdw8ypAJBMf%2Bi5P1HIIB2LnFOoQgGqCRmko6BleLCfkNZEuCpugRYjmC3JAklWvxxBkkZJ758MUhtgsCWLVt54bOhKT9nIOocSc9HQEUvKCrIgfXw7zHz5uGeQDrBtcSHCemlTCIcmkv0J7x%2FIHDbx6rm53Fe2PIqUvNejrcXnqFx6yyFFCS&X-Amz-Signature=ce0745ab1e20d27130f328ff728040d47b9439570f37693e3774eecf75085708&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PFKHETS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDSixLPTgBqZ9Zd1dFgpPqHCw3X3UQXvBSwZfbFWca5XwIhAKEExUg4LGXHB6gXOSEdy2%2B5dubgbqCXTygaiHLKCGDHKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcjrKuaI22X%2FBUdZoq3AP0i3w8KbEev3zY%2BNEBRIaaZAsh71de9FDb9RPoULN1fH3FreAM8wr76IKwRRkZvXdPit0nl7yvR6YlCuXf5HKRBZajYwNXCtcEgC8AmKdXx1tNg4Pncbwvnp7tRwXjb17CVyxBBGs6VguQGA4%2Bd4%2FigxULYHUpTyXN8HqOXKS2m7CcDjyyCZ6SMxUkghQ%2Fs8nro%2Bp60BxN6IWWT5INUFcxuBFC%2F5bgdGiIqBP7AD1UmxoGl0GUYch8eb7EI8Qu8s6K53dSKVg8%2B%2BWyh4%2Ff%2Bl2I01yTbHXb6yF5B5yP3I5jziCsgWHfnbhndK6ykqSXhwSFrA4BmS%2BfK5A%2Bgo4RJt2xGFF%2FiTdSGJLZ4HYM%2F8zdBU7jbuLhTPGcMfCEnfg52N2TkiQRc5DPkWjMSfTNIBaEqyXzJnun9z2i2dm5nczq2XuXIFoKMEyvJAvB%2FXnwsNmkRZLpfxAbYavyGLU4KkU6m7xV7%2Bi%2BX3UrzZoV4cacURrNva5PdJJFZRiekIKzw2FHiVemdFOW9UJjI2egAaTIHTRcicd0ceu3vscA2bd4GK4q4oq1Nrt7%2B4YI%2FjPsdGg1KiUpRki6RKVPiiOrTIxid3k4jmwn3fkzIzqUnyhdFMHj4PNfS3%2B1rGUHYDCP3%2B28BjqkAZm%2BQDt%2Bcea8XQqXwPJ8f5RjSiUWCdTIZG%2Bp4STFt1EvUOA%2FNh1WPSo6%2Fev3gaCTPgkSkXwFcuVn05K2ovT6JVyp0DBFh8x9NU2hsYO2MXLdbhhNOkkvxaiM7cOfdR6hyuuwFrgteGcfn4eH8r0y4lJ9t0Fy6gefikrtIoo4%2Bu9%2B32Z%2FfjGNnfvLVcoDdnj8oCu2Pl3KqHD%2FB%2F9kjuXaQYfIoPgM&X-Amz-Signature=5cc938cc6f17ac16490e8132cc27c9d81cacdf8b0f309551dbfde7b663d69f90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PFKHETS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDSixLPTgBqZ9Zd1dFgpPqHCw3X3UQXvBSwZfbFWca5XwIhAKEExUg4LGXHB6gXOSEdy2%2B5dubgbqCXTygaiHLKCGDHKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcjrKuaI22X%2FBUdZoq3AP0i3w8KbEev3zY%2BNEBRIaaZAsh71de9FDb9RPoULN1fH3FreAM8wr76IKwRRkZvXdPit0nl7yvR6YlCuXf5HKRBZajYwNXCtcEgC8AmKdXx1tNg4Pncbwvnp7tRwXjb17CVyxBBGs6VguQGA4%2Bd4%2FigxULYHUpTyXN8HqOXKS2m7CcDjyyCZ6SMxUkghQ%2Fs8nro%2Bp60BxN6IWWT5INUFcxuBFC%2F5bgdGiIqBP7AD1UmxoGl0GUYch8eb7EI8Qu8s6K53dSKVg8%2B%2BWyh4%2Ff%2Bl2I01yTbHXb6yF5B5yP3I5jziCsgWHfnbhndK6ykqSXhwSFrA4BmS%2BfK5A%2Bgo4RJt2xGFF%2FiTdSGJLZ4HYM%2F8zdBU7jbuLhTPGcMfCEnfg52N2TkiQRc5DPkWjMSfTNIBaEqyXzJnun9z2i2dm5nczq2XuXIFoKMEyvJAvB%2FXnwsNmkRZLpfxAbYavyGLU4KkU6m7xV7%2Bi%2BX3UrzZoV4cacURrNva5PdJJFZRiekIKzw2FHiVemdFOW9UJjI2egAaTIHTRcicd0ceu3vscA2bd4GK4q4oq1Nrt7%2B4YI%2FjPsdGg1KiUpRki6RKVPiiOrTIxid3k4jmwn3fkzIzqUnyhdFMHj4PNfS3%2B1rGUHYDCP3%2B28BjqkAZm%2BQDt%2Bcea8XQqXwPJ8f5RjSiUWCdTIZG%2Bp4STFt1EvUOA%2FNh1WPSo6%2Fev3gaCTPgkSkXwFcuVn05K2ovT6JVyp0DBFh8x9NU2hsYO2MXLdbhhNOkkvxaiM7cOfdR6hyuuwFrgteGcfn4eH8r0y4lJ9t0Fy6gefikrtIoo4%2Bu9%2B32Z%2FfjGNnfvLVcoDdnj8oCu2Pl3KqHD%2FB%2F9kjuXaQYfIoPgM&X-Amz-Signature=9c94c180742031ab3f089c46f28b82ac6f6b539325c276ed37b85b893f4aa90b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
