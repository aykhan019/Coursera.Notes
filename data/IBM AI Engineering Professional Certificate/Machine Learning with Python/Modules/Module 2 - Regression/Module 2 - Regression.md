

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF4K36DK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIHEWygUdBnyt3T0GLD2fDaEpW4XdUbK9Oe7oLh2JYG%2FmAiEA3msEPYlGXEDYh%2BsM8BnnCVXzH0HsTyaU0Uai2T9d6koq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIKi5w2e0iW3dBOKrircA0JN3cyZQfRwg5TUSbaOQy%2BmSwfajd8%2BcUNjxzn7x4crVxRsMGHwo1NZ09JJ0yVPWzzlPdXWH%2BTU6qMvFExREhLienTGPRDFRcdnRYDWOEM6ypxeuWxBk%2BXFYF%2FDuMjvf9aP2TxfIz%2FLqxXJIUgCa%2F7OHEPLJzWE1ReRnVNdDLibDC6oueMU2KSE%2BTUU7ILyvF1WoRPxPhNA5Ttr%2FsM12x6yxnweaWB5p616am2NT6P9RZKsdIAteaneNHbYvs7RWU284nZAeaYVijJ0cCwgg12opGiytphsLVj0AZx5VcYHWhjYPVXKBBh8n60qZS%2F62Xcp3X8Pb70rO2qmcWHKXMw0FMPaph1PXpqPZPsuxDsVDwqz1SHX38%2B9SsdtmrXICdHvl7UoGMmyL7ocBM%2Bjebjz%2F6IjS%2FOxpBLrdY5zUM4IqG5sU07g1OSMwlrN7oz%2BrozXVh7gWkeIWZFrpL3dS%2F%2FG%2FDMOLBONL3EX0qRvRgWxmdekPxQE3%2BM%2FMCqXk0P8A71KY9qGzXUgSVqLqFXt3OH5kKbXImFxvPcojmarZyguAhf5g6%2BLz3NRGKRj7XQ0nbklhupB%2FzrN5PmQCVeSmmzle5pPfnI4QCiGJQ800vARl3U1hzE1KjudDO%2BkMKT8mL0GOqUBLLDzY6Sqa2RUpr095IeS3TsEYz1LHJzAhXyAFghIhqkIcQFKcav0n6Grq1vr6KrLMtmOP7c8EJmu8b2NAEvNFPDrznpbbVb1dL7%2FgetBB68NqGu6Hi8FOCg%2B5ekP4dZ0P1W8CN%2BZ8UXIMKpFLQQ0yvHCarQiWtPrFd%2F%2FYukcqkEFwZbzBjQPaOk24b%2FrIPL33l6Kpmt3n5zYqv2qMaFPiJKPTtNZ&X-Amz-Signature=b2e3df8daecdadeca6b8638db9b1720eadfd4f960556cae49e31f586a4d4d29b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF4K36DK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIHEWygUdBnyt3T0GLD2fDaEpW4XdUbK9Oe7oLh2JYG%2FmAiEA3msEPYlGXEDYh%2BsM8BnnCVXzH0HsTyaU0Uai2T9d6koq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIKi5w2e0iW3dBOKrircA0JN3cyZQfRwg5TUSbaOQy%2BmSwfajd8%2BcUNjxzn7x4crVxRsMGHwo1NZ09JJ0yVPWzzlPdXWH%2BTU6qMvFExREhLienTGPRDFRcdnRYDWOEM6ypxeuWxBk%2BXFYF%2FDuMjvf9aP2TxfIz%2FLqxXJIUgCa%2F7OHEPLJzWE1ReRnVNdDLibDC6oueMU2KSE%2BTUU7ILyvF1WoRPxPhNA5Ttr%2FsM12x6yxnweaWB5p616am2NT6P9RZKsdIAteaneNHbYvs7RWU284nZAeaYVijJ0cCwgg12opGiytphsLVj0AZx5VcYHWhjYPVXKBBh8n60qZS%2F62Xcp3X8Pb70rO2qmcWHKXMw0FMPaph1PXpqPZPsuxDsVDwqz1SHX38%2B9SsdtmrXICdHvl7UoGMmyL7ocBM%2Bjebjz%2F6IjS%2FOxpBLrdY5zUM4IqG5sU07g1OSMwlrN7oz%2BrozXVh7gWkeIWZFrpL3dS%2F%2FG%2FDMOLBONL3EX0qRvRgWxmdekPxQE3%2BM%2FMCqXk0P8A71KY9qGzXUgSVqLqFXt3OH5kKbXImFxvPcojmarZyguAhf5g6%2BLz3NRGKRj7XQ0nbklhupB%2FzrN5PmQCVeSmmzle5pPfnI4QCiGJQ800vARl3U1hzE1KjudDO%2BkMKT8mL0GOqUBLLDzY6Sqa2RUpr095IeS3TsEYz1LHJzAhXyAFghIhqkIcQFKcav0n6Grq1vr6KrLMtmOP7c8EJmu8b2NAEvNFPDrznpbbVb1dL7%2FgetBB68NqGu6Hi8FOCg%2B5ekP4dZ0P1W8CN%2BZ8UXIMKpFLQQ0yvHCarQiWtPrFd%2F%2FYukcqkEFwZbzBjQPaOk24b%2FrIPL33l6Kpmt3n5zYqv2qMaFPiJKPTtNZ&X-Amz-Signature=088b56107fece145ddc5310a5eba8d02c61dcfda6079d798874bab673fe7a9ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF4K36DK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIHEWygUdBnyt3T0GLD2fDaEpW4XdUbK9Oe7oLh2JYG%2FmAiEA3msEPYlGXEDYh%2BsM8BnnCVXzH0HsTyaU0Uai2T9d6koq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIKi5w2e0iW3dBOKrircA0JN3cyZQfRwg5TUSbaOQy%2BmSwfajd8%2BcUNjxzn7x4crVxRsMGHwo1NZ09JJ0yVPWzzlPdXWH%2BTU6qMvFExREhLienTGPRDFRcdnRYDWOEM6ypxeuWxBk%2BXFYF%2FDuMjvf9aP2TxfIz%2FLqxXJIUgCa%2F7OHEPLJzWE1ReRnVNdDLibDC6oueMU2KSE%2BTUU7ILyvF1WoRPxPhNA5Ttr%2FsM12x6yxnweaWB5p616am2NT6P9RZKsdIAteaneNHbYvs7RWU284nZAeaYVijJ0cCwgg12opGiytphsLVj0AZx5VcYHWhjYPVXKBBh8n60qZS%2F62Xcp3X8Pb70rO2qmcWHKXMw0FMPaph1PXpqPZPsuxDsVDwqz1SHX38%2B9SsdtmrXICdHvl7UoGMmyL7ocBM%2Bjebjz%2F6IjS%2FOxpBLrdY5zUM4IqG5sU07g1OSMwlrN7oz%2BrozXVh7gWkeIWZFrpL3dS%2F%2FG%2FDMOLBONL3EX0qRvRgWxmdekPxQE3%2BM%2FMCqXk0P8A71KY9qGzXUgSVqLqFXt3OH5kKbXImFxvPcojmarZyguAhf5g6%2BLz3NRGKRj7XQ0nbklhupB%2FzrN5PmQCVeSmmzle5pPfnI4QCiGJQ800vARl3U1hzE1KjudDO%2BkMKT8mL0GOqUBLLDzY6Sqa2RUpr095IeS3TsEYz1LHJzAhXyAFghIhqkIcQFKcav0n6Grq1vr6KrLMtmOP7c8EJmu8b2NAEvNFPDrznpbbVb1dL7%2FgetBB68NqGu6Hi8FOCg%2B5ekP4dZ0P1W8CN%2BZ8UXIMKpFLQQ0yvHCarQiWtPrFd%2F%2FYukcqkEFwZbzBjQPaOk24b%2FrIPL33l6Kpmt3n5zYqv2qMaFPiJKPTtNZ&X-Amz-Signature=6a11169d2638ca15574a88b442d98407d531486cb2eb378ad07f8b83abe8d63c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF4K36DK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIHEWygUdBnyt3T0GLD2fDaEpW4XdUbK9Oe7oLh2JYG%2FmAiEA3msEPYlGXEDYh%2BsM8BnnCVXzH0HsTyaU0Uai2T9d6koq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIKi5w2e0iW3dBOKrircA0JN3cyZQfRwg5TUSbaOQy%2BmSwfajd8%2BcUNjxzn7x4crVxRsMGHwo1NZ09JJ0yVPWzzlPdXWH%2BTU6qMvFExREhLienTGPRDFRcdnRYDWOEM6ypxeuWxBk%2BXFYF%2FDuMjvf9aP2TxfIz%2FLqxXJIUgCa%2F7OHEPLJzWE1ReRnVNdDLibDC6oueMU2KSE%2BTUU7ILyvF1WoRPxPhNA5Ttr%2FsM12x6yxnweaWB5p616am2NT6P9RZKsdIAteaneNHbYvs7RWU284nZAeaYVijJ0cCwgg12opGiytphsLVj0AZx5VcYHWhjYPVXKBBh8n60qZS%2F62Xcp3X8Pb70rO2qmcWHKXMw0FMPaph1PXpqPZPsuxDsVDwqz1SHX38%2B9SsdtmrXICdHvl7UoGMmyL7ocBM%2Bjebjz%2F6IjS%2FOxpBLrdY5zUM4IqG5sU07g1OSMwlrN7oz%2BrozXVh7gWkeIWZFrpL3dS%2F%2FG%2FDMOLBONL3EX0qRvRgWxmdekPxQE3%2BM%2FMCqXk0P8A71KY9qGzXUgSVqLqFXt3OH5kKbXImFxvPcojmarZyguAhf5g6%2BLz3NRGKRj7XQ0nbklhupB%2FzrN5PmQCVeSmmzle5pPfnI4QCiGJQ800vARl3U1hzE1KjudDO%2BkMKT8mL0GOqUBLLDzY6Sqa2RUpr095IeS3TsEYz1LHJzAhXyAFghIhqkIcQFKcav0n6Grq1vr6KrLMtmOP7c8EJmu8b2NAEvNFPDrznpbbVb1dL7%2FgetBB68NqGu6Hi8FOCg%2B5ekP4dZ0P1W8CN%2BZ8UXIMKpFLQQ0yvHCarQiWtPrFd%2F%2FYukcqkEFwZbzBjQPaOk24b%2FrIPL33l6Kpmt3n5zYqv2qMaFPiJKPTtNZ&X-Amz-Signature=9bc378cce411b38b6461e54f0b3eb39452eea2a2181780f948f3403fb7bc882e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF4K36DK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIHEWygUdBnyt3T0GLD2fDaEpW4XdUbK9Oe7oLh2JYG%2FmAiEA3msEPYlGXEDYh%2BsM8BnnCVXzH0HsTyaU0Uai2T9d6koq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIKi5w2e0iW3dBOKrircA0JN3cyZQfRwg5TUSbaOQy%2BmSwfajd8%2BcUNjxzn7x4crVxRsMGHwo1NZ09JJ0yVPWzzlPdXWH%2BTU6qMvFExREhLienTGPRDFRcdnRYDWOEM6ypxeuWxBk%2BXFYF%2FDuMjvf9aP2TxfIz%2FLqxXJIUgCa%2F7OHEPLJzWE1ReRnVNdDLibDC6oueMU2KSE%2BTUU7ILyvF1WoRPxPhNA5Ttr%2FsM12x6yxnweaWB5p616am2NT6P9RZKsdIAteaneNHbYvs7RWU284nZAeaYVijJ0cCwgg12opGiytphsLVj0AZx5VcYHWhjYPVXKBBh8n60qZS%2F62Xcp3X8Pb70rO2qmcWHKXMw0FMPaph1PXpqPZPsuxDsVDwqz1SHX38%2B9SsdtmrXICdHvl7UoGMmyL7ocBM%2Bjebjz%2F6IjS%2FOxpBLrdY5zUM4IqG5sU07g1OSMwlrN7oz%2BrozXVh7gWkeIWZFrpL3dS%2F%2FG%2FDMOLBONL3EX0qRvRgWxmdekPxQE3%2BM%2FMCqXk0P8A71KY9qGzXUgSVqLqFXt3OH5kKbXImFxvPcojmarZyguAhf5g6%2BLz3NRGKRj7XQ0nbklhupB%2FzrN5PmQCVeSmmzle5pPfnI4QCiGJQ800vARl3U1hzE1KjudDO%2BkMKT8mL0GOqUBLLDzY6Sqa2RUpr095IeS3TsEYz1LHJzAhXyAFghIhqkIcQFKcav0n6Grq1vr6KrLMtmOP7c8EJmu8b2NAEvNFPDrznpbbVb1dL7%2FgetBB68NqGu6Hi8FOCg%2B5ekP4dZ0P1W8CN%2BZ8UXIMKpFLQQ0yvHCarQiWtPrFd%2F%2FYukcqkEFwZbzBjQPaOk24b%2FrIPL33l6Kpmt3n5zYqv2qMaFPiJKPTtNZ&X-Amz-Signature=19baacb1feb648fb7b77dc343a3956cb0c50da16eef899caa220775a37a05312&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF4K36DK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIHEWygUdBnyt3T0GLD2fDaEpW4XdUbK9Oe7oLh2JYG%2FmAiEA3msEPYlGXEDYh%2BsM8BnnCVXzH0HsTyaU0Uai2T9d6koq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIKi5w2e0iW3dBOKrircA0JN3cyZQfRwg5TUSbaOQy%2BmSwfajd8%2BcUNjxzn7x4crVxRsMGHwo1NZ09JJ0yVPWzzlPdXWH%2BTU6qMvFExREhLienTGPRDFRcdnRYDWOEM6ypxeuWxBk%2BXFYF%2FDuMjvf9aP2TxfIz%2FLqxXJIUgCa%2F7OHEPLJzWE1ReRnVNdDLibDC6oueMU2KSE%2BTUU7ILyvF1WoRPxPhNA5Ttr%2FsM12x6yxnweaWB5p616am2NT6P9RZKsdIAteaneNHbYvs7RWU284nZAeaYVijJ0cCwgg12opGiytphsLVj0AZx5VcYHWhjYPVXKBBh8n60qZS%2F62Xcp3X8Pb70rO2qmcWHKXMw0FMPaph1PXpqPZPsuxDsVDwqz1SHX38%2B9SsdtmrXICdHvl7UoGMmyL7ocBM%2Bjebjz%2F6IjS%2FOxpBLrdY5zUM4IqG5sU07g1OSMwlrN7oz%2BrozXVh7gWkeIWZFrpL3dS%2F%2FG%2FDMOLBONL3EX0qRvRgWxmdekPxQE3%2BM%2FMCqXk0P8A71KY9qGzXUgSVqLqFXt3OH5kKbXImFxvPcojmarZyguAhf5g6%2BLz3NRGKRj7XQ0nbklhupB%2FzrN5PmQCVeSmmzle5pPfnI4QCiGJQ800vARl3U1hzE1KjudDO%2BkMKT8mL0GOqUBLLDzY6Sqa2RUpr095IeS3TsEYz1LHJzAhXyAFghIhqkIcQFKcav0n6Grq1vr6KrLMtmOP7c8EJmu8b2NAEvNFPDrznpbbVb1dL7%2FgetBB68NqGu6Hi8FOCg%2B5ekP4dZ0P1W8CN%2BZ8UXIMKpFLQQ0yvHCarQiWtPrFd%2F%2FYukcqkEFwZbzBjQPaOk24b%2FrIPL33l6Kpmt3n5zYqv2qMaFPiJKPTtNZ&X-Amz-Signature=d3b660285e910688fbc880e7b9dfe78ad4e753cb8e4f1286c14712ea7200a8f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF4K36DK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIHEWygUdBnyt3T0GLD2fDaEpW4XdUbK9Oe7oLh2JYG%2FmAiEA3msEPYlGXEDYh%2BsM8BnnCVXzH0HsTyaU0Uai2T9d6koq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIKi5w2e0iW3dBOKrircA0JN3cyZQfRwg5TUSbaOQy%2BmSwfajd8%2BcUNjxzn7x4crVxRsMGHwo1NZ09JJ0yVPWzzlPdXWH%2BTU6qMvFExREhLienTGPRDFRcdnRYDWOEM6ypxeuWxBk%2BXFYF%2FDuMjvf9aP2TxfIz%2FLqxXJIUgCa%2F7OHEPLJzWE1ReRnVNdDLibDC6oueMU2KSE%2BTUU7ILyvF1WoRPxPhNA5Ttr%2FsM12x6yxnweaWB5p616am2NT6P9RZKsdIAteaneNHbYvs7RWU284nZAeaYVijJ0cCwgg12opGiytphsLVj0AZx5VcYHWhjYPVXKBBh8n60qZS%2F62Xcp3X8Pb70rO2qmcWHKXMw0FMPaph1PXpqPZPsuxDsVDwqz1SHX38%2B9SsdtmrXICdHvl7UoGMmyL7ocBM%2Bjebjz%2F6IjS%2FOxpBLrdY5zUM4IqG5sU07g1OSMwlrN7oz%2BrozXVh7gWkeIWZFrpL3dS%2F%2FG%2FDMOLBONL3EX0qRvRgWxmdekPxQE3%2BM%2FMCqXk0P8A71KY9qGzXUgSVqLqFXt3OH5kKbXImFxvPcojmarZyguAhf5g6%2BLz3NRGKRj7XQ0nbklhupB%2FzrN5PmQCVeSmmzle5pPfnI4QCiGJQ800vARl3U1hzE1KjudDO%2BkMKT8mL0GOqUBLLDzY6Sqa2RUpr095IeS3TsEYz1LHJzAhXyAFghIhqkIcQFKcav0n6Grq1vr6KrLMtmOP7c8EJmu8b2NAEvNFPDrznpbbVb1dL7%2FgetBB68NqGu6Hi8FOCg%2B5ekP4dZ0P1W8CN%2BZ8UXIMKpFLQQ0yvHCarQiWtPrFd%2F%2FYukcqkEFwZbzBjQPaOk24b%2FrIPL33l6Kpmt3n5zYqv2qMaFPiJKPTtNZ&X-Amz-Signature=587c3523825218951aac860ba651f06494a44f7570b0538f5961b9313e09beb0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF4K36DK%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIHEWygUdBnyt3T0GLD2fDaEpW4XdUbK9Oe7oLh2JYG%2FmAiEA3msEPYlGXEDYh%2BsM8BnnCVXzH0HsTyaU0Uai2T9d6koq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIKi5w2e0iW3dBOKrircA0JN3cyZQfRwg5TUSbaOQy%2BmSwfajd8%2BcUNjxzn7x4crVxRsMGHwo1NZ09JJ0yVPWzzlPdXWH%2BTU6qMvFExREhLienTGPRDFRcdnRYDWOEM6ypxeuWxBk%2BXFYF%2FDuMjvf9aP2TxfIz%2FLqxXJIUgCa%2F7OHEPLJzWE1ReRnVNdDLibDC6oueMU2KSE%2BTUU7ILyvF1WoRPxPhNA5Ttr%2FsM12x6yxnweaWB5p616am2NT6P9RZKsdIAteaneNHbYvs7RWU284nZAeaYVijJ0cCwgg12opGiytphsLVj0AZx5VcYHWhjYPVXKBBh8n60qZS%2F62Xcp3X8Pb70rO2qmcWHKXMw0FMPaph1PXpqPZPsuxDsVDwqz1SHX38%2B9SsdtmrXICdHvl7UoGMmyL7ocBM%2Bjebjz%2F6IjS%2FOxpBLrdY5zUM4IqG5sU07g1OSMwlrN7oz%2BrozXVh7gWkeIWZFrpL3dS%2F%2FG%2FDMOLBONL3EX0qRvRgWxmdekPxQE3%2BM%2FMCqXk0P8A71KY9qGzXUgSVqLqFXt3OH5kKbXImFxvPcojmarZyguAhf5g6%2BLz3NRGKRj7XQ0nbklhupB%2FzrN5PmQCVeSmmzle5pPfnI4QCiGJQ800vARl3U1hzE1KjudDO%2BkMKT8mL0GOqUBLLDzY6Sqa2RUpr095IeS3TsEYz1LHJzAhXyAFghIhqkIcQFKcav0n6Grq1vr6KrLMtmOP7c8EJmu8b2NAEvNFPDrznpbbVb1dL7%2FgetBB68NqGu6Hi8FOCg%2B5ekP4dZ0P1W8CN%2BZ8UXIMKpFLQQ0yvHCarQiWtPrFd%2F%2FYukcqkEFwZbzBjQPaOk24b%2FrIPL33l6Kpmt3n5zYqv2qMaFPiJKPTtNZ&X-Amz-Signature=b4a2ab21399b5f88c163f8708a0b1bd1d3b109c08a114ed4fa4a742b2e988f68&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5VNIZ3S%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQD9Qn8VRtoXb21RM7W6AUf5RvWS%2FFlrZj9NkILD%2BWWBzgIhAKmA2HzVjURErxrgCd%2Fe3m7vPbT%2BRAOZK9kBBB36UHGfKv8DCHoQABoMNjM3NDIzMTgzODA1IgwmtEKBC8RGIPFZqrQq3AM6RfQDU%2F%2B7DgqNhogiM4g4Jvsq9ohkqyBeKIXY3%2BX1L2H4QJQF5gbpiDe7acNyE9gLAwMr%2FAu1A1znsy%2Bt9y%2B9hzqYdnoMfteHpmAw%2B7ua%2BlLSs0tV%2F%2F7VF%2F0oh9ggNkAw53AK3U5NUfGD1NIlaPdVjzUL7QG9%2BOtcDCmo%2F%2F9UXcoNu2fK52%2Bow0x%2FTE2FNxGYwBaChD2bkejQ4FAXL%2FMog7uL%2FrN6HoAVMUiMI4O6nNEg8NQgWhs2V%2FL609KWKtqMUlGH4YfwfsO2QoXK9TzbraO5ujuZvc3edKVONOvgh6QPDE7Ghu5TSc9ui3X0ZwtrDeDbBfX3QDeC3WquD0OoRmAyTZs68rInn2b%2F7uw73WlN2zBRCVZfLnFKz3mXyaPpI4s30sLCiO%2BqIS1Mg%2FDLKPJXwh8EUmbHV892whaKv7Cytwhgi59tuUlpSSaQ%2BCcrepi74%2B%2B52l8V1ymFRlv0Tjfrm1jQgg6q2LwAlT%2FWX2a%2FJJaAsCEdU49Ga1mpTUFTmA2JqvHpz3v9yMIdrqRHRq0YFmuC54O%2BRrLjnN9QMVGmg%2FKp3QB9m3kWUpgcN%2FQBIUciEjDvlDNhq%2BiheaougwikR1uJS%2FAtIfn1rIlO3xD9lJAdw2KqUjG4cTDk%2B5i9BjqkAeYarqwjfdPYZZcdCMP4cJzzn4cN7GwgT8rWfimK5gl%2B4APRHw9tGWotCwi0brjHE7SocN6tlDtYqorAr0dsVnRRiuYqrjurh71XZ8Apq9ee4DUhjOC6X5I7hKJI4EgWRoJM6TH8ZrIXwClBZb2eAQNT9y23u90sckgDOICuukS5MeWu8z6zCAUW5SQZLrT8cLk%2FtL5rDCxyWOa4H%2BYCImnGzR2Y&X-Amz-Signature=85a52e87e54eda06cc7852c50119d60ebc29c8d7b6ed65165b47e3653bc1c1ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SMQHDWX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQCEQfRaPu43Ws83fEjTYV8m107uw1A78Jaq4jl82IgAdQIgSoVj0S%2Bm55DCUc91b0vdh4RxcitIEU47Q0Abk%2BETY80q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDBBfvXv3PIwR0Ed8xCrcA2qRYDrpkpP9IkHGH%2Fk6BvGmqKnUcVq9N2I2J7gO4F%2BUbwsswGlUTbblTaT5476jTNv%2B3ZssUafHFa7mGb4vnjbJPHw%2Fw0DK6fccIzwdx%2F1%2Bc6wvVOI971TsPjtcOp7nFb6oshP14wjjLDRMhlO0ToMIgeRskEdv0lK8wpp533FzR8suPjWGjyQyYdD%2BwhIDAAmaa0uvrRlHZTeUYs2DF7BnIc8wWVi6O6CMpWvqmrviciGaQQlM9X%2FsNHUjBCLiErANCtWsTrvt9mtJpL3xuiCnr8Ni0FLIQ%2BZAACTyYenrX6jYR827A3cVzpkcE31czkmQ6sJzkGJ7zmztWAmiXXwGJiw0MuBnzrOlM%2BKLeu2i%2FBF8mjIhpWwbUysZZSe6u135gVSnxf9t256clVtjgYrkcNHIzSH5gPvOw60DTw9t2EAbNV%2Ftw3fE7G499OHW3O%2FaE%2Bcx1Oxj9387kLFm0BuyuwtEcJOwrXzJOZhXL4tXkqoGVR2%2BEoJ33AIec6hun79qVsp3yh1DQEtF%2B4K3ZEHI5ODHO1zCloR8ag4YoBqLQ8%2Ff5M0nRmwYOOUrQYFGcDq%2F02%2Fu15hyr%2FlBddy4e1cl1%2FoaoYIgYQxA2lwe60trrDLkb%2FXeVAueh7jHMMv7mL0GOqUBViIOv2bD1x2DetUfS8ydwAO%2BleL%2Fz2lct89jUidRklpIAh5A3cHH3v1wwJNj1nn5X%2Byr7NK2zOYejuVkEjGvGxNaCR8t%2BfZZuZd6NbvdzR5B2H%2FxEteD1KS9FlCrhxbdwcsXkiZEhX6dcFlx6hxL8YbQ2rbnnDv8qLPX7SoBO6V7i2roB%2B9nD32TSkfBNnl7yD%2Fyr8lRHKa3dljsAzmcsYdOGxvh&X-Amz-Signature=05c513d2df677f959f18fc0cb5cc1e2b2fca9a2a755eec2ac120b221f53b7cd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XLZCYEJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIFwG7NHHgcPfDhlRkJFbyzb7b01GQKenVcFk35WZGQKeAiEA8D%2BKYtr8OzEcwPrmwwzK4Z5b%2B9FMtko8E2xyEKxTpAEq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDEj9sJ7rxXEKko379yrcA6xALSlk8Ud6kULzw8%2FcRY0M%2FoT6bBAKFClr7NhnyI%2Ff7gFoIw5IFi8pVlgcXaV1uF161e%2FbiyDxIKyBdKPId62Fkk5BxH3TGRBMM4Nu5CZr2%2F%2BWAomtwU3JvGa9VsAKmxmQbdkTQbC1VCP79jE6v5%2F7OjZPoOKIWB1lhNsfxa6V0xj7cj4RRoWp4PpPHoPyNTuadQU9wRYU1f%2FAgdzMcOwOWi4wHB604U0x8HoUTVkqvht1jYpwWSL46nDDkE%2B7KGX7csRwRmEOa6fWucWtVxoYzMNLTCsQUCkv8mGMLFwmB8F3H6TUXaADIIvbKQ2RXVMdvGAWCoP%2BaaHWJ4Nt2oClOdBl2btVZ%2BSod%2FZ2puLHFhnZo%2F2gdnwFVYIpjwmo9adiSGocnAhvHSgqeBnsaGWU4Lk%2FcmYGCf3IkPAgTFPyLS8A74TjesGs5tlyCBUWXN7pgMUZEOb0H36B3s982epO1G9EZUhw2eEdjk2K5AsVWRPLGHb8TsgGtCHMRw5tHyXRdtm0FRLDPFKtoGqxtwcvXljE1rSQCQFsQCvprXzMkYWYRHCgogYdE1Ogv%2FDT%2Fuzy7ZMtuaBLpbElu8YUtlRgiV626Sy0PtwTS5fviC6xC0rnmh1gcZY%2Bk0ogMPD7mL0GOqUBzLSA69gAHgxHj5ZrGtb9WYl5e2%2FWFNnv1hLF4mG7MIejISKoNM0W%2Fsy8ZPzo%2F%2BhjYilZjkW%2BIa9AdLkp6gv3CGiwcgkAESKBARFeW6aZtufbKaAk2CUEo%2BmR8w3jkQKxD4%2FCA%2BaV1HseZ3OQHvds8xaeMQZGh5ObG2so8HS6K8O04I4hd0WegpVMIXRUUX0yIr3TZVQnOqOe9pOsl4efmSpjekuY&X-Amz-Signature=395054a2050cac114ef001302e427ae1f2b76852e072a150b13b6278cc31caf8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XLZCYEJ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIFwG7NHHgcPfDhlRkJFbyzb7b01GQKenVcFk35WZGQKeAiEA8D%2BKYtr8OzEcwPrmwwzK4Z5b%2B9FMtko8E2xyEKxTpAEq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDEj9sJ7rxXEKko379yrcA6xALSlk8Ud6kULzw8%2FcRY0M%2FoT6bBAKFClr7NhnyI%2Ff7gFoIw5IFi8pVlgcXaV1uF161e%2FbiyDxIKyBdKPId62Fkk5BxH3TGRBMM4Nu5CZr2%2F%2BWAomtwU3JvGa9VsAKmxmQbdkTQbC1VCP79jE6v5%2F7OjZPoOKIWB1lhNsfxa6V0xj7cj4RRoWp4PpPHoPyNTuadQU9wRYU1f%2FAgdzMcOwOWi4wHB604U0x8HoUTVkqvht1jYpwWSL46nDDkE%2B7KGX7csRwRmEOa6fWucWtVxoYzMNLTCsQUCkv8mGMLFwmB8F3H6TUXaADIIvbKQ2RXVMdvGAWCoP%2BaaHWJ4Nt2oClOdBl2btVZ%2BSod%2FZ2puLHFhnZo%2F2gdnwFVYIpjwmo9adiSGocnAhvHSgqeBnsaGWU4Lk%2FcmYGCf3IkPAgTFPyLS8A74TjesGs5tlyCBUWXN7pgMUZEOb0H36B3s982epO1G9EZUhw2eEdjk2K5AsVWRPLGHb8TsgGtCHMRw5tHyXRdtm0FRLDPFKtoGqxtwcvXljE1rSQCQFsQCvprXzMkYWYRHCgogYdE1Ogv%2FDT%2Fuzy7ZMtuaBLpbElu8YUtlRgiV626Sy0PtwTS5fviC6xC0rnmh1gcZY%2Bk0ogMPD7mL0GOqUBzLSA69gAHgxHj5ZrGtb9WYl5e2%2FWFNnv1hLF4mG7MIejISKoNM0W%2Fsy8ZPzo%2F%2BhjYilZjkW%2BIa9AdLkp6gv3CGiwcgkAESKBARFeW6aZtufbKaAk2CUEo%2BmR8w3jkQKxD4%2FCA%2BaV1HseZ3OQHvds8xaeMQZGh5ObG2so8HS6K8O04I4hd0WegpVMIXRUUX0yIr3TZVQnOqOe9pOsl4efmSpjekuY&X-Amz-Signature=2e596021ff96a8b994b6038d590d5447d01c5b597e9e30bbcb9c117e8444f634&X-Amz-SignedHeaders=host&x-id=GetObject)
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
