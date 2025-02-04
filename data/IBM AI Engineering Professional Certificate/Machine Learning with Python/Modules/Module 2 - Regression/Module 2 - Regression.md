

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7PWUNCM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCfZ6spCA8cNntXFtiQ33PqxoFFUB61%2FASFnRbCUIVZ4wIgVPNPFW%2BEzRbVPuD30yXUXWIYtSdfECQUAOZk4Z2G0Pgq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDDZpYdNarM7g36gK8ircAwzQoQ%2BsR7IiOXeyde8uH6qKLZZ17DScuT9uZb%2BP5moZWBGaKDEBoUtHPs4%2BfCyy5Zlrp6%2FjYm97ZJr27%2B1ZtE4ZpyJvg78lUdRy%2FY24izqBpcMou5d2QQTnBRm2KD9%2FvYThrp95AyJs5N8qe%2FAXc67OUFHTC3b%2BJcs8rmLt1FUBlF0cm2S%2B5hpxUkCmVLCd3bbuc5l2hCCp8%2FuIMbvb1mopnDW2RrWGA3hZHQgWFzxtOR9OfEyzdbvI47JU0ExBGAcLxL4ter1%2FScScWbPLSqV60oxeTJRZ7PMgz5hMSXWV8ulTxCN%2BdNbVazqO1BTApCdkmTA8O2sGjk4voaddiav5Sqpw2ZdjlZgkC229tQM8agI%2BFwhxMJ521c5oymY%2FKPt4puDwVoABTBRudpmqvHIUj54IscJaybnsr600tivn1kwT8x2yBO6J3W%2FOSQTFgqcvuecfrY9gDtTmzyF8lDkSUggtZ4j43QNcCsOEF2O4wOzp0sggKx0qNJc3zsNX7MRY%2FxL5qb7rXC1CW%2FRwz%2BnJ%2B55KNxhV7XqHbf7ke%2BrWEhERyAYsBAqb88bWYrEOBbeLK6E2cJvPfIaunHI2MSLDIO1ulYFqkRhHug1p18PetY03iEffX55hxD%2BxMIKihr0GOqUBlY9rWGfpCdpP4QAQDUgVHzwzJoDnvnCKjWSbBM1HcAXF0AVg69bHuXtiz6wTheUSmVUJd%2F1GuHujSRBtGCnR%2FVAl825mWabEVgOQkNylN70lw8JP9N50uPPup%2FjfXXbn5c3FQGCBJ%2F%2FKcNwAAw%2BT5i%2BbUbyQ52zSllwcykwEjSfsI7e%2Fp%2BYXHIYEUdzeXyMmxbc7w7QYIVBK%2BSnc93R8P6z9STa7&X-Amz-Signature=0d1309e4d916b84e1fc8f1e744a8343584230e0bbeb8ba92fccf9b4b38a46480&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7PWUNCM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCfZ6spCA8cNntXFtiQ33PqxoFFUB61%2FASFnRbCUIVZ4wIgVPNPFW%2BEzRbVPuD30yXUXWIYtSdfECQUAOZk4Z2G0Pgq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDDZpYdNarM7g36gK8ircAwzQoQ%2BsR7IiOXeyde8uH6qKLZZ17DScuT9uZb%2BP5moZWBGaKDEBoUtHPs4%2BfCyy5Zlrp6%2FjYm97ZJr27%2B1ZtE4ZpyJvg78lUdRy%2FY24izqBpcMou5d2QQTnBRm2KD9%2FvYThrp95AyJs5N8qe%2FAXc67OUFHTC3b%2BJcs8rmLt1FUBlF0cm2S%2B5hpxUkCmVLCd3bbuc5l2hCCp8%2FuIMbvb1mopnDW2RrWGA3hZHQgWFzxtOR9OfEyzdbvI47JU0ExBGAcLxL4ter1%2FScScWbPLSqV60oxeTJRZ7PMgz5hMSXWV8ulTxCN%2BdNbVazqO1BTApCdkmTA8O2sGjk4voaddiav5Sqpw2ZdjlZgkC229tQM8agI%2BFwhxMJ521c5oymY%2FKPt4puDwVoABTBRudpmqvHIUj54IscJaybnsr600tivn1kwT8x2yBO6J3W%2FOSQTFgqcvuecfrY9gDtTmzyF8lDkSUggtZ4j43QNcCsOEF2O4wOzp0sggKx0qNJc3zsNX7MRY%2FxL5qb7rXC1CW%2FRwz%2BnJ%2B55KNxhV7XqHbf7ke%2BrWEhERyAYsBAqb88bWYrEOBbeLK6E2cJvPfIaunHI2MSLDIO1ulYFqkRhHug1p18PetY03iEffX55hxD%2BxMIKihr0GOqUBlY9rWGfpCdpP4QAQDUgVHzwzJoDnvnCKjWSbBM1HcAXF0AVg69bHuXtiz6wTheUSmVUJd%2F1GuHujSRBtGCnR%2FVAl825mWabEVgOQkNylN70lw8JP9N50uPPup%2FjfXXbn5c3FQGCBJ%2F%2FKcNwAAw%2BT5i%2BbUbyQ52zSllwcykwEjSfsI7e%2Fp%2BYXHIYEUdzeXyMmxbc7w7QYIVBK%2BSnc93R8P6z9STa7&X-Amz-Signature=f9a3d13d5dea67c546a6801b893bfd0c8b961a05c607f3c8af2c00b55d57b06e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7PWUNCM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCfZ6spCA8cNntXFtiQ33PqxoFFUB61%2FASFnRbCUIVZ4wIgVPNPFW%2BEzRbVPuD30yXUXWIYtSdfECQUAOZk4Z2G0Pgq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDDZpYdNarM7g36gK8ircAwzQoQ%2BsR7IiOXeyde8uH6qKLZZ17DScuT9uZb%2BP5moZWBGaKDEBoUtHPs4%2BfCyy5Zlrp6%2FjYm97ZJr27%2B1ZtE4ZpyJvg78lUdRy%2FY24izqBpcMou5d2QQTnBRm2KD9%2FvYThrp95AyJs5N8qe%2FAXc67OUFHTC3b%2BJcs8rmLt1FUBlF0cm2S%2B5hpxUkCmVLCd3bbuc5l2hCCp8%2FuIMbvb1mopnDW2RrWGA3hZHQgWFzxtOR9OfEyzdbvI47JU0ExBGAcLxL4ter1%2FScScWbPLSqV60oxeTJRZ7PMgz5hMSXWV8ulTxCN%2BdNbVazqO1BTApCdkmTA8O2sGjk4voaddiav5Sqpw2ZdjlZgkC229tQM8agI%2BFwhxMJ521c5oymY%2FKPt4puDwVoABTBRudpmqvHIUj54IscJaybnsr600tivn1kwT8x2yBO6J3W%2FOSQTFgqcvuecfrY9gDtTmzyF8lDkSUggtZ4j43QNcCsOEF2O4wOzp0sggKx0qNJc3zsNX7MRY%2FxL5qb7rXC1CW%2FRwz%2BnJ%2B55KNxhV7XqHbf7ke%2BrWEhERyAYsBAqb88bWYrEOBbeLK6E2cJvPfIaunHI2MSLDIO1ulYFqkRhHug1p18PetY03iEffX55hxD%2BxMIKihr0GOqUBlY9rWGfpCdpP4QAQDUgVHzwzJoDnvnCKjWSbBM1HcAXF0AVg69bHuXtiz6wTheUSmVUJd%2F1GuHujSRBtGCnR%2FVAl825mWabEVgOQkNylN70lw8JP9N50uPPup%2FjfXXbn5c3FQGCBJ%2F%2FKcNwAAw%2BT5i%2BbUbyQ52zSllwcykwEjSfsI7e%2Fp%2BYXHIYEUdzeXyMmxbc7w7QYIVBK%2BSnc93R8P6z9STa7&X-Amz-Signature=c27581d1909bf7cafd5a206ffe16bc8193d5db1f8086fb2f0f9f9d9a46c03782&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7PWUNCM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCfZ6spCA8cNntXFtiQ33PqxoFFUB61%2FASFnRbCUIVZ4wIgVPNPFW%2BEzRbVPuD30yXUXWIYtSdfECQUAOZk4Z2G0Pgq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDDZpYdNarM7g36gK8ircAwzQoQ%2BsR7IiOXeyde8uH6qKLZZ17DScuT9uZb%2BP5moZWBGaKDEBoUtHPs4%2BfCyy5Zlrp6%2FjYm97ZJr27%2B1ZtE4ZpyJvg78lUdRy%2FY24izqBpcMou5d2QQTnBRm2KD9%2FvYThrp95AyJs5N8qe%2FAXc67OUFHTC3b%2BJcs8rmLt1FUBlF0cm2S%2B5hpxUkCmVLCd3bbuc5l2hCCp8%2FuIMbvb1mopnDW2RrWGA3hZHQgWFzxtOR9OfEyzdbvI47JU0ExBGAcLxL4ter1%2FScScWbPLSqV60oxeTJRZ7PMgz5hMSXWV8ulTxCN%2BdNbVazqO1BTApCdkmTA8O2sGjk4voaddiav5Sqpw2ZdjlZgkC229tQM8agI%2BFwhxMJ521c5oymY%2FKPt4puDwVoABTBRudpmqvHIUj54IscJaybnsr600tivn1kwT8x2yBO6J3W%2FOSQTFgqcvuecfrY9gDtTmzyF8lDkSUggtZ4j43QNcCsOEF2O4wOzp0sggKx0qNJc3zsNX7MRY%2FxL5qb7rXC1CW%2FRwz%2BnJ%2B55KNxhV7XqHbf7ke%2BrWEhERyAYsBAqb88bWYrEOBbeLK6E2cJvPfIaunHI2MSLDIO1ulYFqkRhHug1p18PetY03iEffX55hxD%2BxMIKihr0GOqUBlY9rWGfpCdpP4QAQDUgVHzwzJoDnvnCKjWSbBM1HcAXF0AVg69bHuXtiz6wTheUSmVUJd%2F1GuHujSRBtGCnR%2FVAl825mWabEVgOQkNylN70lw8JP9N50uPPup%2FjfXXbn5c3FQGCBJ%2F%2FKcNwAAw%2BT5i%2BbUbyQ52zSllwcykwEjSfsI7e%2Fp%2BYXHIYEUdzeXyMmxbc7w7QYIVBK%2BSnc93R8P6z9STa7&X-Amz-Signature=a8cf2467e373c4000b1026d0ab5eb8821ee28cd070389845bec0b843611ceb8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7PWUNCM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCfZ6spCA8cNntXFtiQ33PqxoFFUB61%2FASFnRbCUIVZ4wIgVPNPFW%2BEzRbVPuD30yXUXWIYtSdfECQUAOZk4Z2G0Pgq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDDZpYdNarM7g36gK8ircAwzQoQ%2BsR7IiOXeyde8uH6qKLZZ17DScuT9uZb%2BP5moZWBGaKDEBoUtHPs4%2BfCyy5Zlrp6%2FjYm97ZJr27%2B1ZtE4ZpyJvg78lUdRy%2FY24izqBpcMou5d2QQTnBRm2KD9%2FvYThrp95AyJs5N8qe%2FAXc67OUFHTC3b%2BJcs8rmLt1FUBlF0cm2S%2B5hpxUkCmVLCd3bbuc5l2hCCp8%2FuIMbvb1mopnDW2RrWGA3hZHQgWFzxtOR9OfEyzdbvI47JU0ExBGAcLxL4ter1%2FScScWbPLSqV60oxeTJRZ7PMgz5hMSXWV8ulTxCN%2BdNbVazqO1BTApCdkmTA8O2sGjk4voaddiav5Sqpw2ZdjlZgkC229tQM8agI%2BFwhxMJ521c5oymY%2FKPt4puDwVoABTBRudpmqvHIUj54IscJaybnsr600tivn1kwT8x2yBO6J3W%2FOSQTFgqcvuecfrY9gDtTmzyF8lDkSUggtZ4j43QNcCsOEF2O4wOzp0sggKx0qNJc3zsNX7MRY%2FxL5qb7rXC1CW%2FRwz%2BnJ%2B55KNxhV7XqHbf7ke%2BrWEhERyAYsBAqb88bWYrEOBbeLK6E2cJvPfIaunHI2MSLDIO1ulYFqkRhHug1p18PetY03iEffX55hxD%2BxMIKihr0GOqUBlY9rWGfpCdpP4QAQDUgVHzwzJoDnvnCKjWSbBM1HcAXF0AVg69bHuXtiz6wTheUSmVUJd%2F1GuHujSRBtGCnR%2FVAl825mWabEVgOQkNylN70lw8JP9N50uPPup%2FjfXXbn5c3FQGCBJ%2F%2FKcNwAAw%2BT5i%2BbUbyQ52zSllwcykwEjSfsI7e%2Fp%2BYXHIYEUdzeXyMmxbc7w7QYIVBK%2BSnc93R8P6z9STa7&X-Amz-Signature=cad1ebd71bfcdd6556a7ed75a8f109e12bef7c0c7866e34c8f7a37c30eb8ec44&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7PWUNCM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCfZ6spCA8cNntXFtiQ33PqxoFFUB61%2FASFnRbCUIVZ4wIgVPNPFW%2BEzRbVPuD30yXUXWIYtSdfECQUAOZk4Z2G0Pgq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDDZpYdNarM7g36gK8ircAwzQoQ%2BsR7IiOXeyde8uH6qKLZZ17DScuT9uZb%2BP5moZWBGaKDEBoUtHPs4%2BfCyy5Zlrp6%2FjYm97ZJr27%2B1ZtE4ZpyJvg78lUdRy%2FY24izqBpcMou5d2QQTnBRm2KD9%2FvYThrp95AyJs5N8qe%2FAXc67OUFHTC3b%2BJcs8rmLt1FUBlF0cm2S%2B5hpxUkCmVLCd3bbuc5l2hCCp8%2FuIMbvb1mopnDW2RrWGA3hZHQgWFzxtOR9OfEyzdbvI47JU0ExBGAcLxL4ter1%2FScScWbPLSqV60oxeTJRZ7PMgz5hMSXWV8ulTxCN%2BdNbVazqO1BTApCdkmTA8O2sGjk4voaddiav5Sqpw2ZdjlZgkC229tQM8agI%2BFwhxMJ521c5oymY%2FKPt4puDwVoABTBRudpmqvHIUj54IscJaybnsr600tivn1kwT8x2yBO6J3W%2FOSQTFgqcvuecfrY9gDtTmzyF8lDkSUggtZ4j43QNcCsOEF2O4wOzp0sggKx0qNJc3zsNX7MRY%2FxL5qb7rXC1CW%2FRwz%2BnJ%2B55KNxhV7XqHbf7ke%2BrWEhERyAYsBAqb88bWYrEOBbeLK6E2cJvPfIaunHI2MSLDIO1ulYFqkRhHug1p18PetY03iEffX55hxD%2BxMIKihr0GOqUBlY9rWGfpCdpP4QAQDUgVHzwzJoDnvnCKjWSbBM1HcAXF0AVg69bHuXtiz6wTheUSmVUJd%2F1GuHujSRBtGCnR%2FVAl825mWabEVgOQkNylN70lw8JP9N50uPPup%2FjfXXbn5c3FQGCBJ%2F%2FKcNwAAw%2BT5i%2BbUbyQ52zSllwcykwEjSfsI7e%2Fp%2BYXHIYEUdzeXyMmxbc7w7QYIVBK%2BSnc93R8P6z9STa7&X-Amz-Signature=dd31e496dd5979e5b0359e8412a014775e2d7c6a63b68f9bb2a52eb5402eada6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7PWUNCM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCfZ6spCA8cNntXFtiQ33PqxoFFUB61%2FASFnRbCUIVZ4wIgVPNPFW%2BEzRbVPuD30yXUXWIYtSdfECQUAOZk4Z2G0Pgq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDDZpYdNarM7g36gK8ircAwzQoQ%2BsR7IiOXeyde8uH6qKLZZ17DScuT9uZb%2BP5moZWBGaKDEBoUtHPs4%2BfCyy5Zlrp6%2FjYm97ZJr27%2B1ZtE4ZpyJvg78lUdRy%2FY24izqBpcMou5d2QQTnBRm2KD9%2FvYThrp95AyJs5N8qe%2FAXc67OUFHTC3b%2BJcs8rmLt1FUBlF0cm2S%2B5hpxUkCmVLCd3bbuc5l2hCCp8%2FuIMbvb1mopnDW2RrWGA3hZHQgWFzxtOR9OfEyzdbvI47JU0ExBGAcLxL4ter1%2FScScWbPLSqV60oxeTJRZ7PMgz5hMSXWV8ulTxCN%2BdNbVazqO1BTApCdkmTA8O2sGjk4voaddiav5Sqpw2ZdjlZgkC229tQM8agI%2BFwhxMJ521c5oymY%2FKPt4puDwVoABTBRudpmqvHIUj54IscJaybnsr600tivn1kwT8x2yBO6J3W%2FOSQTFgqcvuecfrY9gDtTmzyF8lDkSUggtZ4j43QNcCsOEF2O4wOzp0sggKx0qNJc3zsNX7MRY%2FxL5qb7rXC1CW%2FRwz%2BnJ%2B55KNxhV7XqHbf7ke%2BrWEhERyAYsBAqb88bWYrEOBbeLK6E2cJvPfIaunHI2MSLDIO1ulYFqkRhHug1p18PetY03iEffX55hxD%2BxMIKihr0GOqUBlY9rWGfpCdpP4QAQDUgVHzwzJoDnvnCKjWSbBM1HcAXF0AVg69bHuXtiz6wTheUSmVUJd%2F1GuHujSRBtGCnR%2FVAl825mWabEVgOQkNylN70lw8JP9N50uPPup%2FjfXXbn5c3FQGCBJ%2F%2FKcNwAAw%2BT5i%2BbUbyQ52zSllwcykwEjSfsI7e%2Fp%2BYXHIYEUdzeXyMmxbc7w7QYIVBK%2BSnc93R8P6z9STa7&X-Amz-Signature=169866098c2628741e3e85fd3e979ed08ef8b17aafc7a97aad1eb870953ee727&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7PWUNCM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCfZ6spCA8cNntXFtiQ33PqxoFFUB61%2FASFnRbCUIVZ4wIgVPNPFW%2BEzRbVPuD30yXUXWIYtSdfECQUAOZk4Z2G0Pgq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDDZpYdNarM7g36gK8ircAwzQoQ%2BsR7IiOXeyde8uH6qKLZZ17DScuT9uZb%2BP5moZWBGaKDEBoUtHPs4%2BfCyy5Zlrp6%2FjYm97ZJr27%2B1ZtE4ZpyJvg78lUdRy%2FY24izqBpcMou5d2QQTnBRm2KD9%2FvYThrp95AyJs5N8qe%2FAXc67OUFHTC3b%2BJcs8rmLt1FUBlF0cm2S%2B5hpxUkCmVLCd3bbuc5l2hCCp8%2FuIMbvb1mopnDW2RrWGA3hZHQgWFzxtOR9OfEyzdbvI47JU0ExBGAcLxL4ter1%2FScScWbPLSqV60oxeTJRZ7PMgz5hMSXWV8ulTxCN%2BdNbVazqO1BTApCdkmTA8O2sGjk4voaddiav5Sqpw2ZdjlZgkC229tQM8agI%2BFwhxMJ521c5oymY%2FKPt4puDwVoABTBRudpmqvHIUj54IscJaybnsr600tivn1kwT8x2yBO6J3W%2FOSQTFgqcvuecfrY9gDtTmzyF8lDkSUggtZ4j43QNcCsOEF2O4wOzp0sggKx0qNJc3zsNX7MRY%2FxL5qb7rXC1CW%2FRwz%2BnJ%2B55KNxhV7XqHbf7ke%2BrWEhERyAYsBAqb88bWYrEOBbeLK6E2cJvPfIaunHI2MSLDIO1ulYFqkRhHug1p18PetY03iEffX55hxD%2BxMIKihr0GOqUBlY9rWGfpCdpP4QAQDUgVHzwzJoDnvnCKjWSbBM1HcAXF0AVg69bHuXtiz6wTheUSmVUJd%2F1GuHujSRBtGCnR%2FVAl825mWabEVgOQkNylN70lw8JP9N50uPPup%2FjfXXbn5c3FQGCBJ%2F%2FKcNwAAw%2BT5i%2BbUbyQ52zSllwcykwEjSfsI7e%2Fp%2BYXHIYEUdzeXyMmxbc7w7QYIVBK%2BSnc93R8P6z9STa7&X-Amz-Signature=898745f2e0be4e0ea135a8873e70bb1a70ecab113d7a06d0e0372ce92022e011&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U576V2N2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQCidM9EWuoJej67f2ZNO2y4pBWILAEE18BE%2FQNd0h397QIhAKDEPG2UYtWJT9EMEOLd1VBvPY6LnHHyoilAKautUfV%2FKv8DCCUQABoMNjM3NDIzMTgzODA1IgzV6a8Y43rX4mRved0q3AMAaOB197Hif5pifSJ2KwXWtxQpw%2Bejaqls5CzRwxdlLzrQ46anNaQNzL7gS66S1NxyMeZxc2OMXk9ILGHvnNGugtLlHJ0aZJGc4owRluX4LMPsVeqP2NGYBiZcBK8wdsBRPa8rbKvse4H9nNXfu7NaL1oAnzI%2F7OpwXbOovvKywoKvBVXstuRU6zzeCEkCe5D%2FOAGiTeS9y0MayKD3xy4%2F4yJmACtARi3NAsiKZzG0PWpVXpw7MqLaX9yhmpaqIuWZ9a%2B%2FbouEFUmQrxh3vr9UbqoN6f7GtNuGfrmB%2FmqX6g%2BRolOaRuBopq0diD9WrLZOK2RyGUftLLGxK2BPljRCZLeLelvsT3Cvd35ME6%2BC5dcvBC4CEb0p%2BYN3sCahskTQUHyWnebpD4GO9FpR%2B0aJyrGMUrxP%2BPA3%2FDXAunQfcX12vVkFs2mnCHRtwrSO2iSEtUwP4r438qB0gHJRNohY4UsgHTcNnjHhGB8aHm2dCww%2BpXBetJmHv3r4xZCk%2BJIZOnylSzR%2F4tC2XPa37JHcCVA8lhOHLxt48CUvLVIc871nXrXfjXbcnaDzieCH2xjQbgRZ%2BjIWUA1XWIhLy7sErJ6BJsx2AJtjawDXL%2FRh73%2BRdObxyCH0foYBljDkooa9BjqkARGWkQ2%2BK060rqfTWZkBTQALzf8LegM8lZZRMYnretR%2B40j%2B2pR1BqCSYHqoUv5RndmYdy4mvyTdepQovav97qmfScthlo5ov5UaAAZCAQp8y%2FKVFY4iu%2FyuU63xxaf1JaNBaauCqu228VTdSO6912jwXdO5FJ73P3QDDrupBWhjo3cI%2FWcBpLHfQ2GrVqMN84b1jJEOY9aB8F8qDeEzdbQIPuVp&X-Amz-Signature=0328054bbb979067c9a7741da6404ba3481dc65a4f9ee5fc8bc711c69c34a46e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUWOLMUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIB06Zz%2Bxnkjr6o%2B5fRmW7QkRE2Rz3ADkm7A0ebUVUxA%2BAiEAymD5OoOPNtFV4sG6AwVCF3WIi%2BFSW0C%2B7YMvJIy5Ot8q%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDCtzsEhdq4FttUMDICrcA%2FMZsmsS7ab%2F6MEQ1Vb0ggj3ty2%2BTrDNF%2BmDs4VU5dUDknC%2BsaqSM75xBbCyptRU5TlZ0XNFoWbOAWUNpFQaEWt5iJqmCDlY46Amcu4RJOrhNpHC223AqUhGbVlKKI5KB%2FzS2KNKgpSptP%2BNLHIucvRyB895W%2FepWSX28BG3Wfvrg4ZJeUE09X%2FTzH1asedDPVDnOhdkqB7v983WrnkucdwF4GsP3AhWYZV49%2FmiqLF%2Fz0vaSyBfzdgCCXlDlKGIGIb62rj3mY%2ByRyxIYpnIUWrk4HHKJJwSoerXyTK4fgAlOJM7b1r7YxWeDDbxRApj7plU8EjBS%2FI9vyuBhhl%2FcrpOHQoe2rfSm8wyjdM4CmYOinRGuPrdwY23nM%2FxnHvIiKxHkspASGiGx9UicxA6LOZQoQFsDYt69mlmh58mBHHnXeYEexSQrFaN3aTcCPJPwGVpr1oxUs9DvKgaJlojBNozElSqT75Fo4T1KV3KVrCdWCTBdhRDnkbccj6lOu0g0UyBk8eqb1JF%2B4fm9eG7Jmu8ObSZVQWbxKl7yInnP7hZFb6nqsxvH%2FYLY3hKUJ3KC3I8ckF9273kkkdy4krQuBCREi83XZRSqf5RszIyB%2BaitmJtve0pupL6y1QaMOahhr0GOqUBiqCimSUOavB60Vm1%2BEYcIZCRqlpLhcFYegzLFkNUSmqJuDtEM6G%2FEQtHd2%2FkX02y1R8F%2FcLSI%2F7ezF%2BnBc0dfYyOFZSw7qYRV%2FSfhiEY3bdF1SvgVKafZYt%2F4Q8zOMWT%2FiXB2Q%2FkZ3NQZKFQoo2Oja1R4g8%2F5j%2B51CCzWKFx9VQEO4bZJcwO2d9WkTehHQ6kc%2FhFLEHiyQp7cM1qOFif6NroLNxL&X-Amz-Signature=53cce6c6f4d0f67ccff7fbc4bcc87bd9fd02564d2ff6f8d6429394f58fa3ce39&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYTYXRHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIHOgFwkVH%2Bd%2BbnGQiLnDb2Gdq8CmabnFpIjbDzsuNtGbAiA4HToGDDc98uaa4b4l9nPNe4aUUA%2FNYjQjPSnBGD3GwSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMoPlJ9mZiTYs%2FCR%2FbKtwDUcioeJEjTo1VB87tP1F8d%2FE0miRcDmHZTEQQ4bTGrDHL%2Bf52pC7f7jjPz2sO9YyD8859OKjwZaGRWM%2FG%2FdlczqUdh%2BJfimV%2FSdxxMamO0B%2BGuuaeIhlnZlDVSMLvv05akBE%2F%2F2E7eMQ7S4BA%2FcWCwPIvjOtjjGOfonC37NXB5F%2BsDVk%2Fz9KSCQ1r6LQHHYqPiz5qcWRABq4Soahduri%2FcSo56bZf3YyhWCZx9ZjpaPup%2B2bnrOyPwAU17QnM3UfS%2FMU9xMCdVVnYfv0syggQkJ6jr57ePUnVP5riqjZ2y5W2Njb6ujbo2xJ5MhDh2EfTRBIBggo4w4XlgojL6ESdll02peyu5i17qGkEoXAtYphJz8hFl3DPbciVkvz%2BH3Urr2NL1pGOG7Qui5qWBRJEvcDooC80nPO67qxHgTaNvc3PXoYsMkwRA59PmuWT5juFjuSgIic5J073ThIKj3SgYikvOTYa2XCZSH45xeOXzaN5%2FUS8W2X%2BjIQ7OF59wuhYrI47u4Hoo9tkVET91wcM07CjQ5UXZAS%2FVPabyu4P34gK8i18zZUYVMeSQTgL1CAbOdj%2FOx4jSUynhUxkPN1baJwyPQw42vteekOnvxJLc85Nw4Eganiqf%2Fuykz0w5KKGvQY6pgH3e1%2FRj1UbtURY5CVwKMmfAwOpMZOeyYxNryAl%2B7E81Qqb4%2Fvq%2FO3NoNvxCvdwQo9oJJZ8nxnQtwMiAb%2FmtYMkCg%2FgcMqGHBErKviIdIIyKETR59kb%2BCwtq6Z4IPdWJf7WWrD3EW8ZiUvj0UrZUklmLEa2ziC1U1cG6oUySu4jkyWQXRf3V8OBELLiAZWxnWcBERIJsLL0b8Y347saUTAlwrfg%2Bu94&X-Amz-Signature=0dc2ce1f57ab7872ce0c98cced9ac0232c75598c48872c95da61eae001b83f0a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYTYXRHB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIHOgFwkVH%2Bd%2BbnGQiLnDb2Gdq8CmabnFpIjbDzsuNtGbAiA4HToGDDc98uaa4b4l9nPNe4aUUA%2FNYjQjPSnBGD3GwSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMoPlJ9mZiTYs%2FCR%2FbKtwDUcioeJEjTo1VB87tP1F8d%2FE0miRcDmHZTEQQ4bTGrDHL%2Bf52pC7f7jjPz2sO9YyD8859OKjwZaGRWM%2FG%2FdlczqUdh%2BJfimV%2FSdxxMamO0B%2BGuuaeIhlnZlDVSMLvv05akBE%2F%2F2E7eMQ7S4BA%2FcWCwPIvjOtjjGOfonC37NXB5F%2BsDVk%2Fz9KSCQ1r6LQHHYqPiz5qcWRABq4Soahduri%2FcSo56bZf3YyhWCZx9ZjpaPup%2B2bnrOyPwAU17QnM3UfS%2FMU9xMCdVVnYfv0syggQkJ6jr57ePUnVP5riqjZ2y5W2Njb6ujbo2xJ5MhDh2EfTRBIBggo4w4XlgojL6ESdll02peyu5i17qGkEoXAtYphJz8hFl3DPbciVkvz%2BH3Urr2NL1pGOG7Qui5qWBRJEvcDooC80nPO67qxHgTaNvc3PXoYsMkwRA59PmuWT5juFjuSgIic5J073ThIKj3SgYikvOTYa2XCZSH45xeOXzaN5%2FUS8W2X%2BjIQ7OF59wuhYrI47u4Hoo9tkVET91wcM07CjQ5UXZAS%2FVPabyu4P34gK8i18zZUYVMeSQTgL1CAbOdj%2FOx4jSUynhUxkPN1baJwyPQw42vteekOnvxJLc85Nw4Eganiqf%2Fuykz0w5KKGvQY6pgH3e1%2FRj1UbtURY5CVwKMmfAwOpMZOeyYxNryAl%2B7E81Qqb4%2Fvq%2FO3NoNvxCvdwQo9oJJZ8nxnQtwMiAb%2FmtYMkCg%2FgcMqGHBErKviIdIIyKETR59kb%2BCwtq6Z4IPdWJf7WWrD3EW8ZiUvj0UrZUklmLEa2ziC1U1cG6oUySu4jkyWQXRf3V8OBELLiAZWxnWcBERIJsLL0b8Y347saUTAlwrfg%2Bu94&X-Amz-Signature=fb2aed018937cf5ffa858fb1668ddf708f2f4c1fdf48cef69663eb29bcb4a6f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
