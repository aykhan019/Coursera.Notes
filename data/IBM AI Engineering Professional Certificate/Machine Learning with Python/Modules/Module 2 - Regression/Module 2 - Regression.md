

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY2DH56R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtDpgmPz8gthY6gPvgP3zgwfZsgPtm9V07Lo7uTyjCwAIgV7tppet1g4pKHJedRrFKFSnF8b1ZfWt%2FwBhyV2Y7aisqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMsxTcbvzYTYpHc39SrcAwkDy0DsmHi%2BaSb1TkqMnT7gLnUtfzp001PO6s%2BeoK189IbLVzO4%2FxKAHAhRQaVj5AqTeQPp1P2%2BlfNomA2jcWaMO76vNrrZqpjvgQSqLRgqiQ8DoJlwR711fQuQep2FWVfFYVPAAkTHiYoFrc9ctq60BVByfWaHXcDsLm%2FydLBqeoUPrePVdpiL1W8D%2Bh8%2FOdERPbRGOGjvAH0g79KjcKodfD3VVh5m8IXh3USR2W7Q7pXFW5QPMfO%2BHlSRb9%2F7rDiIrZsy8So3U6sr3ZXhQf8kK4Zee4Qeh9Qg0jhjZnI4xc9LRv3s9JMNPEoPwH4H7EBc3xwW8QthWYYF%2BfcZj6MgxoS0YtedeGIC5BEQQRtpYLmpatOj8IUueh%2BO73ONU82BpY6L8lXYlH%2FIOT%2FYTjA%2FG5kK8kUwREG099vYM52CBj6vxjvuB79%2F%2FaY%2FNSWTlb528k0fJ6lqQf0hdb%2F%2BlmxXjobeBOLjBgelKVZb%2F77jcWMn0uYDQ0DxW5FE%2B9HFCZ%2FpnDtdCnAT96AWk3eB2uXVco4MX5RvwSBSGGYD3%2F3l%2Bq2GF79QS7yPk2ayHl%2FN6124PVb3Fikeoc7VBJq7vmMmt6MQUhc%2Bw6IoLBvKSO3ICqG8Vs3hgzw48N56MOTe%2FrwGOqUB14lPCVIJ4O6A6Bvt2%2F3wl0XJhwYTOu3YG7ivPQvGU85W7tYYSMOwZJptb%2FeVd4q8sPhd7V2FuEn0jGJPBzYN1ICPPJwrRmIx447ByflQkntrC3oeDmDmqZ6H9NHHjNQIc2HThJ%2BLX9NIed2Z%2Fqg1JNUe1IggfgHBAeAqK9X3DniED2WyR0RBbXw91JyOP9KPPDRwrpNg%2FXpxWrLWYyHjtbhZcvQR&X-Amz-Signature=473dc47391b3afcee8bf7ad28bd1b1231fa0fbe2a454faa93dc7c1222ac33942&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY2DH56R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtDpgmPz8gthY6gPvgP3zgwfZsgPtm9V07Lo7uTyjCwAIgV7tppet1g4pKHJedRrFKFSnF8b1ZfWt%2FwBhyV2Y7aisqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMsxTcbvzYTYpHc39SrcAwkDy0DsmHi%2BaSb1TkqMnT7gLnUtfzp001PO6s%2BeoK189IbLVzO4%2FxKAHAhRQaVj5AqTeQPp1P2%2BlfNomA2jcWaMO76vNrrZqpjvgQSqLRgqiQ8DoJlwR711fQuQep2FWVfFYVPAAkTHiYoFrc9ctq60BVByfWaHXcDsLm%2FydLBqeoUPrePVdpiL1W8D%2Bh8%2FOdERPbRGOGjvAH0g79KjcKodfD3VVh5m8IXh3USR2W7Q7pXFW5QPMfO%2BHlSRb9%2F7rDiIrZsy8So3U6sr3ZXhQf8kK4Zee4Qeh9Qg0jhjZnI4xc9LRv3s9JMNPEoPwH4H7EBc3xwW8QthWYYF%2BfcZj6MgxoS0YtedeGIC5BEQQRtpYLmpatOj8IUueh%2BO73ONU82BpY6L8lXYlH%2FIOT%2FYTjA%2FG5kK8kUwREG099vYM52CBj6vxjvuB79%2F%2FaY%2FNSWTlb528k0fJ6lqQf0hdb%2F%2BlmxXjobeBOLjBgelKVZb%2F77jcWMn0uYDQ0DxW5FE%2B9HFCZ%2FpnDtdCnAT96AWk3eB2uXVco4MX5RvwSBSGGYD3%2F3l%2Bq2GF79QS7yPk2ayHl%2FN6124PVb3Fikeoc7VBJq7vmMmt6MQUhc%2Bw6IoLBvKSO3ICqG8Vs3hgzw48N56MOTe%2FrwGOqUB14lPCVIJ4O6A6Bvt2%2F3wl0XJhwYTOu3YG7ivPQvGU85W7tYYSMOwZJptb%2FeVd4q8sPhd7V2FuEn0jGJPBzYN1ICPPJwrRmIx447ByflQkntrC3oeDmDmqZ6H9NHHjNQIc2HThJ%2BLX9NIed2Z%2Fqg1JNUe1IggfgHBAeAqK9X3DniED2WyR0RBbXw91JyOP9KPPDRwrpNg%2FXpxWrLWYyHjtbhZcvQR&X-Amz-Signature=fc041033ceddd676824fbe3bc1fc4bcb7301754f8476a89df8a7e1c233511539&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY2DH56R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtDpgmPz8gthY6gPvgP3zgwfZsgPtm9V07Lo7uTyjCwAIgV7tppet1g4pKHJedRrFKFSnF8b1ZfWt%2FwBhyV2Y7aisqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMsxTcbvzYTYpHc39SrcAwkDy0DsmHi%2BaSb1TkqMnT7gLnUtfzp001PO6s%2BeoK189IbLVzO4%2FxKAHAhRQaVj5AqTeQPp1P2%2BlfNomA2jcWaMO76vNrrZqpjvgQSqLRgqiQ8DoJlwR711fQuQep2FWVfFYVPAAkTHiYoFrc9ctq60BVByfWaHXcDsLm%2FydLBqeoUPrePVdpiL1W8D%2Bh8%2FOdERPbRGOGjvAH0g79KjcKodfD3VVh5m8IXh3USR2W7Q7pXFW5QPMfO%2BHlSRb9%2F7rDiIrZsy8So3U6sr3ZXhQf8kK4Zee4Qeh9Qg0jhjZnI4xc9LRv3s9JMNPEoPwH4H7EBc3xwW8QthWYYF%2BfcZj6MgxoS0YtedeGIC5BEQQRtpYLmpatOj8IUueh%2BO73ONU82BpY6L8lXYlH%2FIOT%2FYTjA%2FG5kK8kUwREG099vYM52CBj6vxjvuB79%2F%2FaY%2FNSWTlb528k0fJ6lqQf0hdb%2F%2BlmxXjobeBOLjBgelKVZb%2F77jcWMn0uYDQ0DxW5FE%2B9HFCZ%2FpnDtdCnAT96AWk3eB2uXVco4MX5RvwSBSGGYD3%2F3l%2Bq2GF79QS7yPk2ayHl%2FN6124PVb3Fikeoc7VBJq7vmMmt6MQUhc%2Bw6IoLBvKSO3ICqG8Vs3hgzw48N56MOTe%2FrwGOqUB14lPCVIJ4O6A6Bvt2%2F3wl0XJhwYTOu3YG7ivPQvGU85W7tYYSMOwZJptb%2FeVd4q8sPhd7V2FuEn0jGJPBzYN1ICPPJwrRmIx447ByflQkntrC3oeDmDmqZ6H9NHHjNQIc2HThJ%2BLX9NIed2Z%2Fqg1JNUe1IggfgHBAeAqK9X3DniED2WyR0RBbXw91JyOP9KPPDRwrpNg%2FXpxWrLWYyHjtbhZcvQR&X-Amz-Signature=0c0867cd19ab120f6e3b33947bc58e71669d698782ba4822877ee44ee275e8c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY2DH56R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtDpgmPz8gthY6gPvgP3zgwfZsgPtm9V07Lo7uTyjCwAIgV7tppet1g4pKHJedRrFKFSnF8b1ZfWt%2FwBhyV2Y7aisqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMsxTcbvzYTYpHc39SrcAwkDy0DsmHi%2BaSb1TkqMnT7gLnUtfzp001PO6s%2BeoK189IbLVzO4%2FxKAHAhRQaVj5AqTeQPp1P2%2BlfNomA2jcWaMO76vNrrZqpjvgQSqLRgqiQ8DoJlwR711fQuQep2FWVfFYVPAAkTHiYoFrc9ctq60BVByfWaHXcDsLm%2FydLBqeoUPrePVdpiL1W8D%2Bh8%2FOdERPbRGOGjvAH0g79KjcKodfD3VVh5m8IXh3USR2W7Q7pXFW5QPMfO%2BHlSRb9%2F7rDiIrZsy8So3U6sr3ZXhQf8kK4Zee4Qeh9Qg0jhjZnI4xc9LRv3s9JMNPEoPwH4H7EBc3xwW8QthWYYF%2BfcZj6MgxoS0YtedeGIC5BEQQRtpYLmpatOj8IUueh%2BO73ONU82BpY6L8lXYlH%2FIOT%2FYTjA%2FG5kK8kUwREG099vYM52CBj6vxjvuB79%2F%2FaY%2FNSWTlb528k0fJ6lqQf0hdb%2F%2BlmxXjobeBOLjBgelKVZb%2F77jcWMn0uYDQ0DxW5FE%2B9HFCZ%2FpnDtdCnAT96AWk3eB2uXVco4MX5RvwSBSGGYD3%2F3l%2Bq2GF79QS7yPk2ayHl%2FN6124PVb3Fikeoc7VBJq7vmMmt6MQUhc%2Bw6IoLBvKSO3ICqG8Vs3hgzw48N56MOTe%2FrwGOqUB14lPCVIJ4O6A6Bvt2%2F3wl0XJhwYTOu3YG7ivPQvGU85W7tYYSMOwZJptb%2FeVd4q8sPhd7V2FuEn0jGJPBzYN1ICPPJwrRmIx447ByflQkntrC3oeDmDmqZ6H9NHHjNQIc2HThJ%2BLX9NIed2Z%2Fqg1JNUe1IggfgHBAeAqK9X3DniED2WyR0RBbXw91JyOP9KPPDRwrpNg%2FXpxWrLWYyHjtbhZcvQR&X-Amz-Signature=2abbadeebc0fe9556f250b83be067994e1419c0e1f549f1a34143d482755edd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY2DH56R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtDpgmPz8gthY6gPvgP3zgwfZsgPtm9V07Lo7uTyjCwAIgV7tppet1g4pKHJedRrFKFSnF8b1ZfWt%2FwBhyV2Y7aisqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMsxTcbvzYTYpHc39SrcAwkDy0DsmHi%2BaSb1TkqMnT7gLnUtfzp001PO6s%2BeoK189IbLVzO4%2FxKAHAhRQaVj5AqTeQPp1P2%2BlfNomA2jcWaMO76vNrrZqpjvgQSqLRgqiQ8DoJlwR711fQuQep2FWVfFYVPAAkTHiYoFrc9ctq60BVByfWaHXcDsLm%2FydLBqeoUPrePVdpiL1W8D%2Bh8%2FOdERPbRGOGjvAH0g79KjcKodfD3VVh5m8IXh3USR2W7Q7pXFW5QPMfO%2BHlSRb9%2F7rDiIrZsy8So3U6sr3ZXhQf8kK4Zee4Qeh9Qg0jhjZnI4xc9LRv3s9JMNPEoPwH4H7EBc3xwW8QthWYYF%2BfcZj6MgxoS0YtedeGIC5BEQQRtpYLmpatOj8IUueh%2BO73ONU82BpY6L8lXYlH%2FIOT%2FYTjA%2FG5kK8kUwREG099vYM52CBj6vxjvuB79%2F%2FaY%2FNSWTlb528k0fJ6lqQf0hdb%2F%2BlmxXjobeBOLjBgelKVZb%2F77jcWMn0uYDQ0DxW5FE%2B9HFCZ%2FpnDtdCnAT96AWk3eB2uXVco4MX5RvwSBSGGYD3%2F3l%2Bq2GF79QS7yPk2ayHl%2FN6124PVb3Fikeoc7VBJq7vmMmt6MQUhc%2Bw6IoLBvKSO3ICqG8Vs3hgzw48N56MOTe%2FrwGOqUB14lPCVIJ4O6A6Bvt2%2F3wl0XJhwYTOu3YG7ivPQvGU85W7tYYSMOwZJptb%2FeVd4q8sPhd7V2FuEn0jGJPBzYN1ICPPJwrRmIx447ByflQkntrC3oeDmDmqZ6H9NHHjNQIc2HThJ%2BLX9NIed2Z%2Fqg1JNUe1IggfgHBAeAqK9X3DniED2WyR0RBbXw91JyOP9KPPDRwrpNg%2FXpxWrLWYyHjtbhZcvQR&X-Amz-Signature=2f563d6d4953718acdb1a045b641ce25277940a1a877923542b5516c1f55c5a1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY2DH56R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtDpgmPz8gthY6gPvgP3zgwfZsgPtm9V07Lo7uTyjCwAIgV7tppet1g4pKHJedRrFKFSnF8b1ZfWt%2FwBhyV2Y7aisqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMsxTcbvzYTYpHc39SrcAwkDy0DsmHi%2BaSb1TkqMnT7gLnUtfzp001PO6s%2BeoK189IbLVzO4%2FxKAHAhRQaVj5AqTeQPp1P2%2BlfNomA2jcWaMO76vNrrZqpjvgQSqLRgqiQ8DoJlwR711fQuQep2FWVfFYVPAAkTHiYoFrc9ctq60BVByfWaHXcDsLm%2FydLBqeoUPrePVdpiL1W8D%2Bh8%2FOdERPbRGOGjvAH0g79KjcKodfD3VVh5m8IXh3USR2W7Q7pXFW5QPMfO%2BHlSRb9%2F7rDiIrZsy8So3U6sr3ZXhQf8kK4Zee4Qeh9Qg0jhjZnI4xc9LRv3s9JMNPEoPwH4H7EBc3xwW8QthWYYF%2BfcZj6MgxoS0YtedeGIC5BEQQRtpYLmpatOj8IUueh%2BO73ONU82BpY6L8lXYlH%2FIOT%2FYTjA%2FG5kK8kUwREG099vYM52CBj6vxjvuB79%2F%2FaY%2FNSWTlb528k0fJ6lqQf0hdb%2F%2BlmxXjobeBOLjBgelKVZb%2F77jcWMn0uYDQ0DxW5FE%2B9HFCZ%2FpnDtdCnAT96AWk3eB2uXVco4MX5RvwSBSGGYD3%2F3l%2Bq2GF79QS7yPk2ayHl%2FN6124PVb3Fikeoc7VBJq7vmMmt6MQUhc%2Bw6IoLBvKSO3ICqG8Vs3hgzw48N56MOTe%2FrwGOqUB14lPCVIJ4O6A6Bvt2%2F3wl0XJhwYTOu3YG7ivPQvGU85W7tYYSMOwZJptb%2FeVd4q8sPhd7V2FuEn0jGJPBzYN1ICPPJwrRmIx447ByflQkntrC3oeDmDmqZ6H9NHHjNQIc2HThJ%2BLX9NIed2Z%2Fqg1JNUe1IggfgHBAeAqK9X3DniED2WyR0RBbXw91JyOP9KPPDRwrpNg%2FXpxWrLWYyHjtbhZcvQR&X-Amz-Signature=e0e4834c10cd8bc16e3ed7acbbaaee74b235512c9adb9b14993a7ca43c4f6bf3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY2DH56R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtDpgmPz8gthY6gPvgP3zgwfZsgPtm9V07Lo7uTyjCwAIgV7tppet1g4pKHJedRrFKFSnF8b1ZfWt%2FwBhyV2Y7aisqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMsxTcbvzYTYpHc39SrcAwkDy0DsmHi%2BaSb1TkqMnT7gLnUtfzp001PO6s%2BeoK189IbLVzO4%2FxKAHAhRQaVj5AqTeQPp1P2%2BlfNomA2jcWaMO76vNrrZqpjvgQSqLRgqiQ8DoJlwR711fQuQep2FWVfFYVPAAkTHiYoFrc9ctq60BVByfWaHXcDsLm%2FydLBqeoUPrePVdpiL1W8D%2Bh8%2FOdERPbRGOGjvAH0g79KjcKodfD3VVh5m8IXh3USR2W7Q7pXFW5QPMfO%2BHlSRb9%2F7rDiIrZsy8So3U6sr3ZXhQf8kK4Zee4Qeh9Qg0jhjZnI4xc9LRv3s9JMNPEoPwH4H7EBc3xwW8QthWYYF%2BfcZj6MgxoS0YtedeGIC5BEQQRtpYLmpatOj8IUueh%2BO73ONU82BpY6L8lXYlH%2FIOT%2FYTjA%2FG5kK8kUwREG099vYM52CBj6vxjvuB79%2F%2FaY%2FNSWTlb528k0fJ6lqQf0hdb%2F%2BlmxXjobeBOLjBgelKVZb%2F77jcWMn0uYDQ0DxW5FE%2B9HFCZ%2FpnDtdCnAT96AWk3eB2uXVco4MX5RvwSBSGGYD3%2F3l%2Bq2GF79QS7yPk2ayHl%2FN6124PVb3Fikeoc7VBJq7vmMmt6MQUhc%2Bw6IoLBvKSO3ICqG8Vs3hgzw48N56MOTe%2FrwGOqUB14lPCVIJ4O6A6Bvt2%2F3wl0XJhwYTOu3YG7ivPQvGU85W7tYYSMOwZJptb%2FeVd4q8sPhd7V2FuEn0jGJPBzYN1ICPPJwrRmIx447ByflQkntrC3oeDmDmqZ6H9NHHjNQIc2HThJ%2BLX9NIed2Z%2Fqg1JNUe1IggfgHBAeAqK9X3DniED2WyR0RBbXw91JyOP9KPPDRwrpNg%2FXpxWrLWYyHjtbhZcvQR&X-Amz-Signature=0d466ea41455304125a9f584ce2dee42f5862bcdb923b3bcac7799e5ab3b84fd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY2DH56R%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtDpgmPz8gthY6gPvgP3zgwfZsgPtm9V07Lo7uTyjCwAIgV7tppet1g4pKHJedRrFKFSnF8b1ZfWt%2FwBhyV2Y7aisqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMsxTcbvzYTYpHc39SrcAwkDy0DsmHi%2BaSb1TkqMnT7gLnUtfzp001PO6s%2BeoK189IbLVzO4%2FxKAHAhRQaVj5AqTeQPp1P2%2BlfNomA2jcWaMO76vNrrZqpjvgQSqLRgqiQ8DoJlwR711fQuQep2FWVfFYVPAAkTHiYoFrc9ctq60BVByfWaHXcDsLm%2FydLBqeoUPrePVdpiL1W8D%2Bh8%2FOdERPbRGOGjvAH0g79KjcKodfD3VVh5m8IXh3USR2W7Q7pXFW5QPMfO%2BHlSRb9%2F7rDiIrZsy8So3U6sr3ZXhQf8kK4Zee4Qeh9Qg0jhjZnI4xc9LRv3s9JMNPEoPwH4H7EBc3xwW8QthWYYF%2BfcZj6MgxoS0YtedeGIC5BEQQRtpYLmpatOj8IUueh%2BO73ONU82BpY6L8lXYlH%2FIOT%2FYTjA%2FG5kK8kUwREG099vYM52CBj6vxjvuB79%2F%2FaY%2FNSWTlb528k0fJ6lqQf0hdb%2F%2BlmxXjobeBOLjBgelKVZb%2F77jcWMn0uYDQ0DxW5FE%2B9HFCZ%2FpnDtdCnAT96AWk3eB2uXVco4MX5RvwSBSGGYD3%2F3l%2Bq2GF79QS7yPk2ayHl%2FN6124PVb3Fikeoc7VBJq7vmMmt6MQUhc%2Bw6IoLBvKSO3ICqG8Vs3hgzw48N56MOTe%2FrwGOqUB14lPCVIJ4O6A6Bvt2%2F3wl0XJhwYTOu3YG7ivPQvGU85W7tYYSMOwZJptb%2FeVd4q8sPhd7V2FuEn0jGJPBzYN1ICPPJwrRmIx447ByflQkntrC3oeDmDmqZ6H9NHHjNQIc2HThJ%2BLX9NIed2Z%2Fqg1JNUe1IggfgHBAeAqK9X3DniED2WyR0RBbXw91JyOP9KPPDRwrpNg%2FXpxWrLWYyHjtbhZcvQR&X-Amz-Signature=5b629ab0297c063ff914cba74e35d87c401c9257f12edef9284f083088381e55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W54FNHAB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFsE9OJLzQ7rmzKXQHIkpQhymlRdWnHGxD9YDcviGYrJAiEAvfvkjvvefP5YWkzH29OqdM1%2FhDfT0G%2BV8qB7prSBfI8qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDASMF8ftlyezzj6UoSrcAwqwF4nmfux9xKgDUd2zFE%2BMxjb%2Bc6g55GLNmToUzRTJXanRjro9bDv9YiWO3ZAkIPI26zsvK%2FSa15AuGV8GAhFO6d09YUPQ9UCAnGz881ar%2F%2Byuz0tjpYLeTmIl%2FNfjfCSfbxQHO1%2BSEPQ9L9QJhVQe5K1SXBwLjMtrYDmheTrpDXD7inuUIn%2FvacRiyAWbhJ14Ftsu7bns2f9pHUGXgrNrqRyBH0qQlRytbuiRJRxnSCxycf7VrU7eQvcddeMfvQ58bRsHTNGWSgwDelu0n5EMN5K4CoxSawRt%2FpxER2Ek9BQW9xSgRtscTAXAlPSi7tiCgEd4N3xbn%2BPCsHe4yAa68rEMlL1c0jZTwiNhfEZvLxQK6ew3TNqXpLgoM094bi4M6dJdFcvYp65Gr0gzbiRaCH%2FBOluT5AtlbBea%2Fz5rbrrHYot8N5eiWjxBws4muwBPQHZ1lWCUVfn0YSU6Ur6Cnpdjfxjb82GOmhu3%2Fa4w7NVFKAmNOcX0j7AvLERALfGuum3%2FTlC1vqQGZg6x8irOTjDXQRjjt1h7s%2FO1%2FXMS%2FPDCPN3AsJjmD%2BSSAzY%2B8srMV766%2BJ%2FXgxNCYuvgUhzeVSA59QnS5KIqCAdr5gj6TrEiefdPo8B2v6IFMITk%2FrwGOqUBAFD0jt7UuZbgdxgtZyHSu0VAbegnhvnlOKQJAO%2BNM7YNJdpo8naQYZEHm%2BhygS2F7jvuVS3hrvjgKPOGm6HPnyKJoSr1sixTfHW5CyvBPIa76UNUx%2FEsOyBjG2FIzyg2XkXpFrGVqTAIv0rK7e0nvD4SYlPXFduQevDwrdxJCe3NBmz9xCVd66wJnERmWWBB0VqIkGXnlY6dnMuzw2geEwQG%2FA8s&X-Amz-Signature=de33f2f725b6b516e5d1f71d09a59ada8fc2fcbd7dd1ac4085f491c0ffb4f3b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KS7G3OZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrAXImr8Gsi%2BftOQwbGkURBhBkYrHj22WV9SmabCceZAIhAMAB3w4tyQkRQWORwy%2BN2Y%2FZSxBxc0mRIzZLMtQXnMaUKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxxZQHqRsbM775OEj0q3APHvZTh0%2BpCHzcHIn4e%2FeoeA4vUV%2F5Cs3wZKqog3rH6HPalKVHI2P%2B1lh9e3x6n2%2BU9ycvPiHW3M2BQ%2B9GZjM8igFtDmwASOxC5CPppKrP96rjttxeY3lYqkDWw8GBGk7rikMvaf5ybVU1R6x9eWrdKX%2Bj5qlPEldujiXP3WRXEnzjNKJyG2Jc1uzIhg9VfykbvGHBrSY%2FC9Zzd5kdAEDJybhCtoASQnGb39k0T7rBfRLu%2FVABY7gmYuk7Ly9M%2FTlbffQoom7tqJThtQ75SPzdpkbsxb%2FdoAzZpyGpMX9sMWjqus87duOq%2Fm%2FQjtKvSQjOO%2FkI9p0k1wtbyfeh62tGpN2MdvbCb22zNKghMjSGrDVfMhIn5wEYd9RTuCf8iXoAg%2BztvTd0BmKXiUqYs%2F1J4nDV11Yz5kS6ierS0nfG1%2Fqr4smhQNrukfDQipW%2B5sXR9cOdA4t4BNDguXShpntwbm5ueJQvNFqOD%2FJAnsi%2FySE9XTQtcLEUdjAtDX%2FwgunQjJ2d%2FG5VvYcejzQV9QaIvaHFFCoKPbVLykafWY2Vatl4C5vk5MNT5NihjvEfKYKdiPQJ1PBKmolKRh4Wk2UDIsGe3rlCVUeJV%2B0jmSaOxt%2FjK4PUcRjmOoEroSzCS0%2F68BjqkAZrXRepiSOZT%2BGIx%2FX7IHsY9rOf%2FVWw3Jjzr5joR2LE5HaeAVY6QY2k1%2B601C9p3M3N6hl%2Fez2heB7Qcqq1LqtDe%2BfLm%2F%2FEzqOFohnGo5BT7%2BMGvBeV%2BQ2ffdG%2BuVnLht0%2FA8RXjAKwBLUp4wURvy%2BvSjM9jf8W0wPK7SDDBJkTZbZ26eD0QPz6Wrjd9nEP8%2FyeP0LvVNEOTi0lnrhaAjQ747q0m&X-Amz-Signature=398eea849f4ff3a6b780fad4191bc7f9ddf54163e9a2eeb0ce274e756d1b5fec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX7DW4DY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC5sIsEvhnTQYTB3kLKJSbs%2BwCDB5LWrup6o0iYxcOGqAiEA8wzVE%2BL07zhZRUkiG4X0I3YJqz4Er6KkrZY2x5EpUdIqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3J5vG3OBUswFZThyrcAwZDQR5NIXW7rkD1a1r5b5H1szjv60Vc%2Fl6Bvm%2FmDhHAijr6PLgiddyj5rztDgiHWn11JFpJsK0y3Wm9E2LIKYG7VGerf%2F2LFNpZuCDPc8nsTHVP8fYqX%2B%2F70S51ZmaFs31l8ZWlsCsB0TUWP4DOpr814NJ60vGpTJKsLUGNVf98O2ZLzfSik7GBii%2FQqW380dQIHIxbyE%2F0qFGPS1yNElYQnMlmsZub8sc8E2dUMip4ZKJEiPFoa2ZsJRqWi1jLxxTvebdC1NaYo8L5GDULOu1ve8pEYYX2il47iHB9bmi%2BsAORjNe6hxJR60%2Bb1XMujLmM69uxD0iAURj17X1XLdHSBHpRXydYQHRNkv%2BjK0hcGB8GOzNl8gj6HHy6di%2BvFEHkN5YqTmqZqDMMc9cIdMGslToVVofT2WCdCfHMyeoY3T39848oDn%2BlML1CXEz0Ko279KtQF4p%2BwgvwEkFyPXvf%2BghdS%2FStqnZtV%2FCN%2FGCiVdV3YrSFWcbnRiiKNeRMyFMM9QB7XtQpegnMzAPvz0zEYYytVb3pt4nk4OP3JD6ooRMMwqRKzfmZ9BKKndTC5HU6acmGbtK7nTPwNVo02eyJW%2B6u5inebKmYWBmsbzHP8Sa3LqGpX4FKXfSQMKLj%2FrwGOqUBvx%2B8jJhpLGOrD3QuGcsyO3UYr0JhdtbI5WcGwUfXINvvD1g5%2FUulJwDMSPYCvReI4lEjskbQkS7jVKuPItdZtYylsuoLCcdxMd6LMzZ5QJfr%2FfkYsSWd5WT4DiR0IHciPvJH7Njh%2FoVAlMw9t%2BVlw4j9Rdsz9mfU2DhjpAVUoGbK7WgL9N%2FzoOMj%2F5wC0btn5BIPo%2Fjhs7F1CPGarLK3lAmxljN5&X-Amz-Signature=cede4e72bc3ddc10f9eb4c372f36866e7e8850de9e3cb70f7795cc2c410cd9da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX7DW4DY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC5sIsEvhnTQYTB3kLKJSbs%2BwCDB5LWrup6o0iYxcOGqAiEA8wzVE%2BL07zhZRUkiG4X0I3YJqz4Er6KkrZY2x5EpUdIqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3J5vG3OBUswFZThyrcAwZDQR5NIXW7rkD1a1r5b5H1szjv60Vc%2Fl6Bvm%2FmDhHAijr6PLgiddyj5rztDgiHWn11JFpJsK0y3Wm9E2LIKYG7VGerf%2F2LFNpZuCDPc8nsTHVP8fYqX%2B%2F70S51ZmaFs31l8ZWlsCsB0TUWP4DOpr814NJ60vGpTJKsLUGNVf98O2ZLzfSik7GBii%2FQqW380dQIHIxbyE%2F0qFGPS1yNElYQnMlmsZub8sc8E2dUMip4ZKJEiPFoa2ZsJRqWi1jLxxTvebdC1NaYo8L5GDULOu1ve8pEYYX2il47iHB9bmi%2BsAORjNe6hxJR60%2Bb1XMujLmM69uxD0iAURj17X1XLdHSBHpRXydYQHRNkv%2BjK0hcGB8GOzNl8gj6HHy6di%2BvFEHkN5YqTmqZqDMMc9cIdMGslToVVofT2WCdCfHMyeoY3T39848oDn%2BlML1CXEz0Ko279KtQF4p%2BwgvwEkFyPXvf%2BghdS%2FStqnZtV%2FCN%2FGCiVdV3YrSFWcbnRiiKNeRMyFMM9QB7XtQpegnMzAPvz0zEYYytVb3pt4nk4OP3JD6ooRMMwqRKzfmZ9BKKndTC5HU6acmGbtK7nTPwNVo02eyJW%2B6u5inebKmYWBmsbzHP8Sa3LqGpX4FKXfSQMKLj%2FrwGOqUBvx%2B8jJhpLGOrD3QuGcsyO3UYr0JhdtbI5WcGwUfXINvvD1g5%2FUulJwDMSPYCvReI4lEjskbQkS7jVKuPItdZtYylsuoLCcdxMd6LMzZ5QJfr%2FfkYsSWd5WT4DiR0IHciPvJH7Njh%2FoVAlMw9t%2BVlw4j9Rdsz9mfU2DhjpAVUoGbK7WgL9N%2FzoOMj%2F5wC0btn5BIPo%2Fjhs7F1CPGarLK3lAmxljN5&X-Amz-Signature=8a961533ddf2326f5680606b89c11d2d6d630f4bf0c406383fdc298fd3050e80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
