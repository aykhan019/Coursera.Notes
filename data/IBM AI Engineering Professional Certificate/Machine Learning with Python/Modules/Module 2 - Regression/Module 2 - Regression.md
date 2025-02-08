

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYM4VK3G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGPCV1ThLrfgVvhJz%2FVWvgOGn0Swa446P2IVncr4zJ5sAiEAr8YBEQTBt6hlndP79BKArCd32qpjW5d2KuZbo1IKw8MqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnLxP0ydaZitfrtfircAw8t9fQhp1Bgr1R%2BuF9OKWFavij2ubGXOWrXcSCAlv3AggWRmNtoQohL6n1x2AYvAYaM9eew9TdMv%2Fcbf3uAk7MaTbpmnFS%2FSnJDq456hygvhFg4Ax%2BDDm1KJ3ixSO9r%2FO5JflI%2BiJBLfYl2fkWPyz5LAtP8w8CIYxnT7yZxXVRPDgTE6WmIcispIPpRlf5zurTvI1xb9FbmkVEduxUrOWL41H3iQ16RXtRnIDl9TTk6cftJuPEMRdIjolOCpOf%2BGydTf04KQs45j44TqV%2FEhxcwUm%2B7cCoqr441yiAaXRuPXb1949jCd5RyHx2Xp%2FieJmae2g15c4QyybKCKIq7GbJF%2FCdLTCglONVaBHGQmH2Fa73xWBBd3HFv8Z6fii8UxXnCSQtO011AIl7fmlAFEFWVKSrYcoqJi%2F2vILanaBQ4LMkBooEVzK5TusCXq62m3ft0qNt9X%2BMCUydL3M9pHot6dH8DR1co%2BpQ0F8yp6cdqV9VU8dv2xUotcHbNhXgSUR9MBAo3VrxaBrYAb2Wp%2BZ8PDJgqc8BFRl9S3IZnZRuQC7dH%2BfLaugMA6szPBTidyp8DK%2FRppRMoP1AzoVrdwdxo6AENbIxUKfCFmVD2GyAKLxbH6TdW7uiilvlVMPeNnL0GOqUBCBBhQY%2BCuiGJtXqTtQfPPMa0DDJ4nzBAVwDfzMDiMgfA%2FheuapgUo0DEWuCiQZjLxXOMipNvO2Qqt1ar4FMe5uophwOvTfVA%2FKajg6O9LvzACo%2FUF7f8dw5WvOfQNlaP4%2FIlkYRCvVcvWPCmFesdX7lRw%2BmTvkTTj19XYJPQSXswsRs53i4FxhrDw6QtQLMMenxDxwC7ifrr%2BMB92c1hRJlfZ5%2Bx&X-Amz-Signature=629f6a1f140563979dd1693e3068d6151af21e2d27667d8c72466f950bebaea8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYM4VK3G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGPCV1ThLrfgVvhJz%2FVWvgOGn0Swa446P2IVncr4zJ5sAiEAr8YBEQTBt6hlndP79BKArCd32qpjW5d2KuZbo1IKw8MqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnLxP0ydaZitfrtfircAw8t9fQhp1Bgr1R%2BuF9OKWFavij2ubGXOWrXcSCAlv3AggWRmNtoQohL6n1x2AYvAYaM9eew9TdMv%2Fcbf3uAk7MaTbpmnFS%2FSnJDq456hygvhFg4Ax%2BDDm1KJ3ixSO9r%2FO5JflI%2BiJBLfYl2fkWPyz5LAtP8w8CIYxnT7yZxXVRPDgTE6WmIcispIPpRlf5zurTvI1xb9FbmkVEduxUrOWL41H3iQ16RXtRnIDl9TTk6cftJuPEMRdIjolOCpOf%2BGydTf04KQs45j44TqV%2FEhxcwUm%2B7cCoqr441yiAaXRuPXb1949jCd5RyHx2Xp%2FieJmae2g15c4QyybKCKIq7GbJF%2FCdLTCglONVaBHGQmH2Fa73xWBBd3HFv8Z6fii8UxXnCSQtO011AIl7fmlAFEFWVKSrYcoqJi%2F2vILanaBQ4LMkBooEVzK5TusCXq62m3ft0qNt9X%2BMCUydL3M9pHot6dH8DR1co%2BpQ0F8yp6cdqV9VU8dv2xUotcHbNhXgSUR9MBAo3VrxaBrYAb2Wp%2BZ8PDJgqc8BFRl9S3IZnZRuQC7dH%2BfLaugMA6szPBTidyp8DK%2FRppRMoP1AzoVrdwdxo6AENbIxUKfCFmVD2GyAKLxbH6TdW7uiilvlVMPeNnL0GOqUBCBBhQY%2BCuiGJtXqTtQfPPMa0DDJ4nzBAVwDfzMDiMgfA%2FheuapgUo0DEWuCiQZjLxXOMipNvO2Qqt1ar4FMe5uophwOvTfVA%2FKajg6O9LvzACo%2FUF7f8dw5WvOfQNlaP4%2FIlkYRCvVcvWPCmFesdX7lRw%2BmTvkTTj19XYJPQSXswsRs53i4FxhrDw6QtQLMMenxDxwC7ifrr%2BMB92c1hRJlfZ5%2Bx&X-Amz-Signature=da31a352825ff244b6f3add62e91095407433826fc7a9d8828245f51d02bc19c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYM4VK3G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGPCV1ThLrfgVvhJz%2FVWvgOGn0Swa446P2IVncr4zJ5sAiEAr8YBEQTBt6hlndP79BKArCd32qpjW5d2KuZbo1IKw8MqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnLxP0ydaZitfrtfircAw8t9fQhp1Bgr1R%2BuF9OKWFavij2ubGXOWrXcSCAlv3AggWRmNtoQohL6n1x2AYvAYaM9eew9TdMv%2Fcbf3uAk7MaTbpmnFS%2FSnJDq456hygvhFg4Ax%2BDDm1KJ3ixSO9r%2FO5JflI%2BiJBLfYl2fkWPyz5LAtP8w8CIYxnT7yZxXVRPDgTE6WmIcispIPpRlf5zurTvI1xb9FbmkVEduxUrOWL41H3iQ16RXtRnIDl9TTk6cftJuPEMRdIjolOCpOf%2BGydTf04KQs45j44TqV%2FEhxcwUm%2B7cCoqr441yiAaXRuPXb1949jCd5RyHx2Xp%2FieJmae2g15c4QyybKCKIq7GbJF%2FCdLTCglONVaBHGQmH2Fa73xWBBd3HFv8Z6fii8UxXnCSQtO011AIl7fmlAFEFWVKSrYcoqJi%2F2vILanaBQ4LMkBooEVzK5TusCXq62m3ft0qNt9X%2BMCUydL3M9pHot6dH8DR1co%2BpQ0F8yp6cdqV9VU8dv2xUotcHbNhXgSUR9MBAo3VrxaBrYAb2Wp%2BZ8PDJgqc8BFRl9S3IZnZRuQC7dH%2BfLaugMA6szPBTidyp8DK%2FRppRMoP1AzoVrdwdxo6AENbIxUKfCFmVD2GyAKLxbH6TdW7uiilvlVMPeNnL0GOqUBCBBhQY%2BCuiGJtXqTtQfPPMa0DDJ4nzBAVwDfzMDiMgfA%2FheuapgUo0DEWuCiQZjLxXOMipNvO2Qqt1ar4FMe5uophwOvTfVA%2FKajg6O9LvzACo%2FUF7f8dw5WvOfQNlaP4%2FIlkYRCvVcvWPCmFesdX7lRw%2BmTvkTTj19XYJPQSXswsRs53i4FxhrDw6QtQLMMenxDxwC7ifrr%2BMB92c1hRJlfZ5%2Bx&X-Amz-Signature=cc93fb76ebd98543860d82b46a3c2ca789293b1dc55a433297c47e31a4135205&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYM4VK3G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGPCV1ThLrfgVvhJz%2FVWvgOGn0Swa446P2IVncr4zJ5sAiEAr8YBEQTBt6hlndP79BKArCd32qpjW5d2KuZbo1IKw8MqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnLxP0ydaZitfrtfircAw8t9fQhp1Bgr1R%2BuF9OKWFavij2ubGXOWrXcSCAlv3AggWRmNtoQohL6n1x2AYvAYaM9eew9TdMv%2Fcbf3uAk7MaTbpmnFS%2FSnJDq456hygvhFg4Ax%2BDDm1KJ3ixSO9r%2FO5JflI%2BiJBLfYl2fkWPyz5LAtP8w8CIYxnT7yZxXVRPDgTE6WmIcispIPpRlf5zurTvI1xb9FbmkVEduxUrOWL41H3iQ16RXtRnIDl9TTk6cftJuPEMRdIjolOCpOf%2BGydTf04KQs45j44TqV%2FEhxcwUm%2B7cCoqr441yiAaXRuPXb1949jCd5RyHx2Xp%2FieJmae2g15c4QyybKCKIq7GbJF%2FCdLTCglONVaBHGQmH2Fa73xWBBd3HFv8Z6fii8UxXnCSQtO011AIl7fmlAFEFWVKSrYcoqJi%2F2vILanaBQ4LMkBooEVzK5TusCXq62m3ft0qNt9X%2BMCUydL3M9pHot6dH8DR1co%2BpQ0F8yp6cdqV9VU8dv2xUotcHbNhXgSUR9MBAo3VrxaBrYAb2Wp%2BZ8PDJgqc8BFRl9S3IZnZRuQC7dH%2BfLaugMA6szPBTidyp8DK%2FRppRMoP1AzoVrdwdxo6AENbIxUKfCFmVD2GyAKLxbH6TdW7uiilvlVMPeNnL0GOqUBCBBhQY%2BCuiGJtXqTtQfPPMa0DDJ4nzBAVwDfzMDiMgfA%2FheuapgUo0DEWuCiQZjLxXOMipNvO2Qqt1ar4FMe5uophwOvTfVA%2FKajg6O9LvzACo%2FUF7f8dw5WvOfQNlaP4%2FIlkYRCvVcvWPCmFesdX7lRw%2BmTvkTTj19XYJPQSXswsRs53i4FxhrDw6QtQLMMenxDxwC7ifrr%2BMB92c1hRJlfZ5%2Bx&X-Amz-Signature=0a62cf0404dac8ff2468f809bd2963ef7f9e496458ea735e6de35738ac0ccb0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYM4VK3G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGPCV1ThLrfgVvhJz%2FVWvgOGn0Swa446P2IVncr4zJ5sAiEAr8YBEQTBt6hlndP79BKArCd32qpjW5d2KuZbo1IKw8MqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnLxP0ydaZitfrtfircAw8t9fQhp1Bgr1R%2BuF9OKWFavij2ubGXOWrXcSCAlv3AggWRmNtoQohL6n1x2AYvAYaM9eew9TdMv%2Fcbf3uAk7MaTbpmnFS%2FSnJDq456hygvhFg4Ax%2BDDm1KJ3ixSO9r%2FO5JflI%2BiJBLfYl2fkWPyz5LAtP8w8CIYxnT7yZxXVRPDgTE6WmIcispIPpRlf5zurTvI1xb9FbmkVEduxUrOWL41H3iQ16RXtRnIDl9TTk6cftJuPEMRdIjolOCpOf%2BGydTf04KQs45j44TqV%2FEhxcwUm%2B7cCoqr441yiAaXRuPXb1949jCd5RyHx2Xp%2FieJmae2g15c4QyybKCKIq7GbJF%2FCdLTCglONVaBHGQmH2Fa73xWBBd3HFv8Z6fii8UxXnCSQtO011AIl7fmlAFEFWVKSrYcoqJi%2F2vILanaBQ4LMkBooEVzK5TusCXq62m3ft0qNt9X%2BMCUydL3M9pHot6dH8DR1co%2BpQ0F8yp6cdqV9VU8dv2xUotcHbNhXgSUR9MBAo3VrxaBrYAb2Wp%2BZ8PDJgqc8BFRl9S3IZnZRuQC7dH%2BfLaugMA6szPBTidyp8DK%2FRppRMoP1AzoVrdwdxo6AENbIxUKfCFmVD2GyAKLxbH6TdW7uiilvlVMPeNnL0GOqUBCBBhQY%2BCuiGJtXqTtQfPPMa0DDJ4nzBAVwDfzMDiMgfA%2FheuapgUo0DEWuCiQZjLxXOMipNvO2Qqt1ar4FMe5uophwOvTfVA%2FKajg6O9LvzACo%2FUF7f8dw5WvOfQNlaP4%2FIlkYRCvVcvWPCmFesdX7lRw%2BmTvkTTj19XYJPQSXswsRs53i4FxhrDw6QtQLMMenxDxwC7ifrr%2BMB92c1hRJlfZ5%2Bx&X-Amz-Signature=70f57f3d6c3b8de23b3408652082b9640956e122553c568479ddcbb807419273&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYM4VK3G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGPCV1ThLrfgVvhJz%2FVWvgOGn0Swa446P2IVncr4zJ5sAiEAr8YBEQTBt6hlndP79BKArCd32qpjW5d2KuZbo1IKw8MqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnLxP0ydaZitfrtfircAw8t9fQhp1Bgr1R%2BuF9OKWFavij2ubGXOWrXcSCAlv3AggWRmNtoQohL6n1x2AYvAYaM9eew9TdMv%2Fcbf3uAk7MaTbpmnFS%2FSnJDq456hygvhFg4Ax%2BDDm1KJ3ixSO9r%2FO5JflI%2BiJBLfYl2fkWPyz5LAtP8w8CIYxnT7yZxXVRPDgTE6WmIcispIPpRlf5zurTvI1xb9FbmkVEduxUrOWL41H3iQ16RXtRnIDl9TTk6cftJuPEMRdIjolOCpOf%2BGydTf04KQs45j44TqV%2FEhxcwUm%2B7cCoqr441yiAaXRuPXb1949jCd5RyHx2Xp%2FieJmae2g15c4QyybKCKIq7GbJF%2FCdLTCglONVaBHGQmH2Fa73xWBBd3HFv8Z6fii8UxXnCSQtO011AIl7fmlAFEFWVKSrYcoqJi%2F2vILanaBQ4LMkBooEVzK5TusCXq62m3ft0qNt9X%2BMCUydL3M9pHot6dH8DR1co%2BpQ0F8yp6cdqV9VU8dv2xUotcHbNhXgSUR9MBAo3VrxaBrYAb2Wp%2BZ8PDJgqc8BFRl9S3IZnZRuQC7dH%2BfLaugMA6szPBTidyp8DK%2FRppRMoP1AzoVrdwdxo6AENbIxUKfCFmVD2GyAKLxbH6TdW7uiilvlVMPeNnL0GOqUBCBBhQY%2BCuiGJtXqTtQfPPMa0DDJ4nzBAVwDfzMDiMgfA%2FheuapgUo0DEWuCiQZjLxXOMipNvO2Qqt1ar4FMe5uophwOvTfVA%2FKajg6O9LvzACo%2FUF7f8dw5WvOfQNlaP4%2FIlkYRCvVcvWPCmFesdX7lRw%2BmTvkTTj19XYJPQSXswsRs53i4FxhrDw6QtQLMMenxDxwC7ifrr%2BMB92c1hRJlfZ5%2Bx&X-Amz-Signature=096310238e78f5397ec8e0a074255816447159e38d38441f70aca499fd861ea6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYM4VK3G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGPCV1ThLrfgVvhJz%2FVWvgOGn0Swa446P2IVncr4zJ5sAiEAr8YBEQTBt6hlndP79BKArCd32qpjW5d2KuZbo1IKw8MqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnLxP0ydaZitfrtfircAw8t9fQhp1Bgr1R%2BuF9OKWFavij2ubGXOWrXcSCAlv3AggWRmNtoQohL6n1x2AYvAYaM9eew9TdMv%2Fcbf3uAk7MaTbpmnFS%2FSnJDq456hygvhFg4Ax%2BDDm1KJ3ixSO9r%2FO5JflI%2BiJBLfYl2fkWPyz5LAtP8w8CIYxnT7yZxXVRPDgTE6WmIcispIPpRlf5zurTvI1xb9FbmkVEduxUrOWL41H3iQ16RXtRnIDl9TTk6cftJuPEMRdIjolOCpOf%2BGydTf04KQs45j44TqV%2FEhxcwUm%2B7cCoqr441yiAaXRuPXb1949jCd5RyHx2Xp%2FieJmae2g15c4QyybKCKIq7GbJF%2FCdLTCglONVaBHGQmH2Fa73xWBBd3HFv8Z6fii8UxXnCSQtO011AIl7fmlAFEFWVKSrYcoqJi%2F2vILanaBQ4LMkBooEVzK5TusCXq62m3ft0qNt9X%2BMCUydL3M9pHot6dH8DR1co%2BpQ0F8yp6cdqV9VU8dv2xUotcHbNhXgSUR9MBAo3VrxaBrYAb2Wp%2BZ8PDJgqc8BFRl9S3IZnZRuQC7dH%2BfLaugMA6szPBTidyp8DK%2FRppRMoP1AzoVrdwdxo6AENbIxUKfCFmVD2GyAKLxbH6TdW7uiilvlVMPeNnL0GOqUBCBBhQY%2BCuiGJtXqTtQfPPMa0DDJ4nzBAVwDfzMDiMgfA%2FheuapgUo0DEWuCiQZjLxXOMipNvO2Qqt1ar4FMe5uophwOvTfVA%2FKajg6O9LvzACo%2FUF7f8dw5WvOfQNlaP4%2FIlkYRCvVcvWPCmFesdX7lRw%2BmTvkTTj19XYJPQSXswsRs53i4FxhrDw6QtQLMMenxDxwC7ifrr%2BMB92c1hRJlfZ5%2Bx&X-Amz-Signature=2f9f82a71978a408e214638d7f7c292a80e00efbad6a8ef5181977eda65aa51b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYM4VK3G%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIGPCV1ThLrfgVvhJz%2FVWvgOGn0Swa446P2IVncr4zJ5sAiEAr8YBEQTBt6hlndP79BKArCd32qpjW5d2KuZbo1IKw8MqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnLxP0ydaZitfrtfircAw8t9fQhp1Bgr1R%2BuF9OKWFavij2ubGXOWrXcSCAlv3AggWRmNtoQohL6n1x2AYvAYaM9eew9TdMv%2Fcbf3uAk7MaTbpmnFS%2FSnJDq456hygvhFg4Ax%2BDDm1KJ3ixSO9r%2FO5JflI%2BiJBLfYl2fkWPyz5LAtP8w8CIYxnT7yZxXVRPDgTE6WmIcispIPpRlf5zurTvI1xb9FbmkVEduxUrOWL41H3iQ16RXtRnIDl9TTk6cftJuPEMRdIjolOCpOf%2BGydTf04KQs45j44TqV%2FEhxcwUm%2B7cCoqr441yiAaXRuPXb1949jCd5RyHx2Xp%2FieJmae2g15c4QyybKCKIq7GbJF%2FCdLTCglONVaBHGQmH2Fa73xWBBd3HFv8Z6fii8UxXnCSQtO011AIl7fmlAFEFWVKSrYcoqJi%2F2vILanaBQ4LMkBooEVzK5TusCXq62m3ft0qNt9X%2BMCUydL3M9pHot6dH8DR1co%2BpQ0F8yp6cdqV9VU8dv2xUotcHbNhXgSUR9MBAo3VrxaBrYAb2Wp%2BZ8PDJgqc8BFRl9S3IZnZRuQC7dH%2BfLaugMA6szPBTidyp8DK%2FRppRMoP1AzoVrdwdxo6AENbIxUKfCFmVD2GyAKLxbH6TdW7uiilvlVMPeNnL0GOqUBCBBhQY%2BCuiGJtXqTtQfPPMa0DDJ4nzBAVwDfzMDiMgfA%2FheuapgUo0DEWuCiQZjLxXOMipNvO2Qqt1ar4FMe5uophwOvTfVA%2FKajg6O9LvzACo%2FUF7f8dw5WvOfQNlaP4%2FIlkYRCvVcvWPCmFesdX7lRw%2BmTvkTTj19XYJPQSXswsRs53i4FxhrDw6QtQLMMenxDxwC7ifrr%2BMB92c1hRJlfZ5%2Bx&X-Amz-Signature=021b0644c6f2c20eb25d82e1714fd73cc3e42d8d9d5c5a472e834ba0cec7e64f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6GTNKCP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQD1BuxgwdhoinMYeNpwj8Hs0%2FRhuUILUBo1YGgD%2B3CTkQIhAIxbQrYW3qwEGUlnGwXwh2Ff894phL7KuhqEX8tGvSC7KogECIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyyQtLIFZqwCcsTygUq3APbWAFCGWnuo3oiqvFDc2kM5Igkyc0aJYOA8Fz7Um61Ln9huD8yhN66SRIOQkdjqsTEIoiuRuXIuTNsOIiKubHmxSQIbO9hJE702oGaS4IiGYdxTXHcWfaDfaUb3JIBHCsCWmUkloNZWQbriRH7RdVEEq0cvR3KeLiAEujt5K%2F6MfaSgmXA8nxljtc6qEgArmU6b%2BsBk7oo%2FNdNWbfpqrbiCzzWmF%2BCsLXNJm%2FOjph%2Fzbs25x0kZsd7EumFNB5yjCd7bjolgbjC8xC%2Bg9klXQo%2FU5SoLKdP%2B%2FC6b3d3GIgo656Laws2jk20lYjLXgziIE0Yf4yZpNzPhLVMtgmuuo4utA2l7Zg02HWpdPRyjDJlNulDKDIqr%2FEBtEC8gi5CS%2BZZX7icqRSVldxNHVm0zyKMeruQK7PSKBHESynBaV7ob76CNJlkEhe9oGMOemk4EZqPpHFQRVmjZ5gYWdANgv8im6cWDm7hS6GycZSBnNW%2FSJDz8V4c53C1pPshSE6dGwlqxZ%2FhrennJH055xdDwCYv69x3ZBUJKiyDTODYavMDSBb9vGP%2BlGDJTpO9SlfTrsPJHEGvH45TQpjc3VrDStvzr90TF3VOoERGW4oby5q387kJAgJbwUia7rxGlTCYjpy9BjqkARE66N2%2FuXA4nGeDQmwTV07giONOmnAIAbSsYVjRAndbEjyQobZBsp%2Baq0hDXLRzA%2FSevZxRi8Dp5gMXZIXq2GcnAZGzixUJDVm%2F%2FR0uW1JVJoq2iDFsFMy2stmK%2F2bgCz3qQLL39KPxk9C6bxJu7QTyhpYSBZyZ4wegQa1iNzpc8Q6%2BPbFePHhzyEbyMDsdWlQs9%2F2MApc0suAY593cHPH%2FyyrQ&X-Amz-Signature=6358ba759dd436e8e9434e27dab1290776bc4f7ecd24e0bce9525dde8c692348&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3CXQZPY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIFURnNUItQUKVOP0vQJDfmeTNadgM%2FRP4OCE3deU%2FG8lAiAo1yZhGQ1DPjTolQHHYh617WpcDxlb6oUhiKcHset3gyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSKH9%2B0njEqmeINUjKtwD6QCSdZFUOHMu0%2B61cKcbG%2FiACqcWO0Q%2FRebhGYSZtU0bTIoFdt38O9O5TDPU1SPb%2B%2FuHWI8h%2BSWVSg7Y%2BczNgph5rWBHrMGHLz3YhXSPqYVVBhG%2F%2F5jfCJ8E6KCGjeh8Z56GZhaA1iEf2wiZ8%2BKTUvTdEmlnOr6Iy%2BC6B%2FoK%2FDwEV1RiNqN%2FqHvnBG1K%2FRxQQolm6Z6nJzT6%2FLag0bdpyg%2Fy%2F8MB0xmlc9Ku7WkZuMh26JylXiOy%2BI%2BtjL6tCiNGyDXGB7gamzwO6%2BGE6ogjfaJ%2FNicVHBYVPgFRwAuRHtjnR3xTkmrfnrmAjlrFKEOoRDd6SpHt1B6l3R4wnyja2XXD470xMW7fIs5xMca6sz37CtCCPH7nsXjGbQEzgsA1W90z942IfFWdv10oSf%2F9Z6J7%2FvDnZbXuy3CY0rpPInCW1Su1Do9YeOIYR8MMY5eYOs%2F4%2Fi9yGUStR%2B3OwSL1%2FbbDJViXXlruuylHusWovyP3EsX3hFh1odUZJy%2Bxezb3BI5BnyK7IO8NF4Ca4pli6Mg3jBwu7GvtkCwS17e8X3YSApvKHnDBA580k80Sx6kZfHVMinpO%2Bf40tsMSvq%2BT8WTMT9BygIcVclHO3pxufA6Px0osYJh4sdgPCaYw642cvQY6pgHLP9fyAnt2e80pXlHEoxat7%2Bd2Uo0qLxl7a%2F%2Fiis6whcba4gfx%2B%2BkhSy4wLokynS7qIAkAS3kvRQYNhIGAeSotkzVDswadcYfbEeNQwxbyr2fFssq7R7%2BqfB8cVXUiS1rRtmlnbXiiAMV%2BL4TkyomyquYj4MBOsUBAG9qw%2FmB9L0j7CvEmcewubYAlOcoIqBCpz94Esom5KVWpPQDumz5x4B78DmAZ&X-Amz-Signature=5c2f9b1658df82d6c140fa7dae0678ce19857e82ae79c3d2b31f6fcd58ac7f34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4FWWM5S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCjj%2FywoUFefI14t3OzqWaTEcAqU5rX%2BiOc18uNEve%2FYQIhAMV0hbwL3LVT89cs6m1o%2BOMe23kraAxx0%2Fgv0XiHGVwuKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNTEI8lqjklHUOptMq3AO9sRBQBQ8n%2Be3%2BZ36mvTf5yzrvtEbP6hi2Ts1RtfeH4wEoQfM8WjXG27%2BZR9nsfXYkytZO0DT84LQyd1BJASNTaNayrJA%2FfcRbY91h0Xxa6GKVjGENaEQ%2B9zFUkNzOc8lh%2F0RXZ7501aSNmas1ac8LyfDNinBpx0G3ss4KaXD%2FUL8rxEiaPNOxenqaRyxR112rJ9XXHPJIYlpZTqPcZLdGh1NRmkRSb1pQix5rV5s6zxrj3wJpH1fPGa4I9MSLSYBuOJIlxHakxQxnRTsfrC3EJiNE0Pi596Or67MhGQim4FrNFG%2F%2B3lDXI33zQkG4BRwmBFHbtIbz%2BAlba1TXFZy9MEjYbH2ULLRFoPVY78Js2%2FHUnwUat8BzzSwxjucVEXwZiixh6uO%2Bdm2kwxg28P8jZOG%2FQiO0dWXvb9%2BtWLMAxyUJBW2CfarkAqKTso7xIOc1kT2O6DFaMQTBgOlWBLktO7zDElqnYyaL%2FYcl%2BQGklRbEyYEkVGVr0C73yS3gUfucJFV44d0ybZjaAgbxS1FFmsnJm6U4Csr%2Fizt146tdDt%2BabZsj5Z2cFtrHB4CWcaD0FfAsTVQuBmLTzJboOODiAZZ%2F1QOBj5MowPA9UQq3JG7H7ncXN%2FX%2FkgOIFTDDjpy9BjqkAVae%2BLsn7KAToig7dC0cA4QK1ogWoaQVQ98NNxgRKTCgFLIgnIs8zzZCNnhAz10pBxCQ2GZqMskbRbO1kd7UagVsgR0XgT%2FPG1WmiezQs4KwJExA%2FDGMPEuw9RK6EUXqvwBl1wI7fOECy2k2grzmZLkLQsH2LAZ%2FClspaK7YbImnU9SrW2nVs%2F2wHNSEnQfVyLw9%2FYI6%2Fv85YLwyQqWlcz2HmRqM&X-Amz-Signature=cff0da66e9c5125eac407c3d8bc5c07901899800d331bb88564dd6be054f6520&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4FWWM5S%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T081758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCjj%2FywoUFefI14t3OzqWaTEcAqU5rX%2BiOc18uNEve%2FYQIhAMV0hbwL3LVT89cs6m1o%2BOMe23kraAxx0%2Fgv0XiHGVwuKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNTEI8lqjklHUOptMq3AO9sRBQBQ8n%2Be3%2BZ36mvTf5yzrvtEbP6hi2Ts1RtfeH4wEoQfM8WjXG27%2BZR9nsfXYkytZO0DT84LQyd1BJASNTaNayrJA%2FfcRbY91h0Xxa6GKVjGENaEQ%2B9zFUkNzOc8lh%2F0RXZ7501aSNmas1ac8LyfDNinBpx0G3ss4KaXD%2FUL8rxEiaPNOxenqaRyxR112rJ9XXHPJIYlpZTqPcZLdGh1NRmkRSb1pQix5rV5s6zxrj3wJpH1fPGa4I9MSLSYBuOJIlxHakxQxnRTsfrC3EJiNE0Pi596Or67MhGQim4FrNFG%2F%2B3lDXI33zQkG4BRwmBFHbtIbz%2BAlba1TXFZy9MEjYbH2ULLRFoPVY78Js2%2FHUnwUat8BzzSwxjucVEXwZiixh6uO%2Bdm2kwxg28P8jZOG%2FQiO0dWXvb9%2BtWLMAxyUJBW2CfarkAqKTso7xIOc1kT2O6DFaMQTBgOlWBLktO7zDElqnYyaL%2FYcl%2BQGklRbEyYEkVGVr0C73yS3gUfucJFV44d0ybZjaAgbxS1FFmsnJm6U4Csr%2Fizt146tdDt%2BabZsj5Z2cFtrHB4CWcaD0FfAsTVQuBmLTzJboOODiAZZ%2F1QOBj5MowPA9UQq3JG7H7ncXN%2FX%2FkgOIFTDDjpy9BjqkAVae%2BLsn7KAToig7dC0cA4QK1ogWoaQVQ98NNxgRKTCgFLIgnIs8zzZCNnhAz10pBxCQ2GZqMskbRbO1kd7UagVsgR0XgT%2FPG1WmiezQs4KwJExA%2FDGMPEuw9RK6EUXqvwBl1wI7fOECy2k2grzmZLkLQsH2LAZ%2FClspaK7YbImnU9SrW2nVs%2F2wHNSEnQfVyLw9%2FYI6%2Fv85YLwyQqWlcz2HmRqM&X-Amz-Signature=7e332f5c3659d723afc48cd7b5e9da146c0835e3f4f4beab872c8b15213c6f41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
