

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXH5BIOY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEP7lKXOLp0e%2Bw5Fqpg9SD4Eu1P8fgCrvzqbYlavwxjxAiBrF5GkoXP5%2B%2FB%2BQS9I8aNdihn2S4YfdW0nNuSDNvImoiqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcV7afvTbkDr8WM2SKtwDlc0UtoydbT8s3whbarf4oiI5FCE0xsNj7uZSreaqxvHyt3xqg2IZyyK2kSEHTT53kM1GmC7HJF2Z7mGixhF3b9cHTr2u%2FN1lPMRlK3%2FP2SRRTf%2FRMMXlHKF2%2BDDKau2IKSf%2BnKKAUINXFQ1umkDEikig6QCPoQ52N1rs1FMKk91x8Av4I9oY7pR2TybXTJ9LKKS%2FcGBm3yJzxIxg6dV1cK88DLJA96xW7KsdKGDTGkK2RlbDIGiZaeO%2FWI9Sdvhi1uCJO5%2BNECsoMgHX%2FZHo1YXyqvXLaemMXtWtJRpNlICrGkIE1R0fWiRKMKevxc%2FkGKnPye%2F7gspfkeBY1Efoo3leonSItBQrCFvnNw67fIMbeiv%2BJquhLcLT8osaOa3G30I5hFjiWiGqz6OuGhD4yz7Ebsz4Xke0EnD%2BPnEI5X%2F9DH7HKwejboDo2O8wBUeoTmOQ%2Bqvu69HA%2BN16kefG5wmwe0C01IRv5xay8GqIy6AU%2BVHHQ5biVCuNUNmwee5khZm6zDAbqb3UAHm39b7JPePK0iBN6DEi33KopBUtxSbPBfhwxq5KpxE2UWWXv8d59NUHrRZTxrh6c3IN3FW%2Fc6dYuYFWo9bv40%2F%2Fg6IfA6aPt%2FiIAI%2Fk6%2Bp67kwwz932vAY6pgEsgGZQ0GoTm0c%2BPHsYljFDxMC%2F5afc6UqBLkEuvUzmHRytAXUypxx941mEu6Bubgei1eWVJBUvbQ64H0e4%2BFvSRlyabFbzbcCxb27qSvOwFGLJpGt2628N5xhd2YvCW9rQN7oxuy%2F4%2F0uTJklP3XVMfPOnYj3Mwd6jImF1PcYP3EhoUkW%2B4PhdZS8CesbbomnRyNaG96eTsTG8fN%2BIdVSqh0hrYv4n&X-Amz-Signature=f6a4ba3432c1b4424ca14f90594864267cc734a65ba1f70182da851778f20a13&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXH5BIOY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEP7lKXOLp0e%2Bw5Fqpg9SD4Eu1P8fgCrvzqbYlavwxjxAiBrF5GkoXP5%2B%2FB%2BQS9I8aNdihn2S4YfdW0nNuSDNvImoiqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcV7afvTbkDr8WM2SKtwDlc0UtoydbT8s3whbarf4oiI5FCE0xsNj7uZSreaqxvHyt3xqg2IZyyK2kSEHTT53kM1GmC7HJF2Z7mGixhF3b9cHTr2u%2FN1lPMRlK3%2FP2SRRTf%2FRMMXlHKF2%2BDDKau2IKSf%2BnKKAUINXFQ1umkDEikig6QCPoQ52N1rs1FMKk91x8Av4I9oY7pR2TybXTJ9LKKS%2FcGBm3yJzxIxg6dV1cK88DLJA96xW7KsdKGDTGkK2RlbDIGiZaeO%2FWI9Sdvhi1uCJO5%2BNECsoMgHX%2FZHo1YXyqvXLaemMXtWtJRpNlICrGkIE1R0fWiRKMKevxc%2FkGKnPye%2F7gspfkeBY1Efoo3leonSItBQrCFvnNw67fIMbeiv%2BJquhLcLT8osaOa3G30I5hFjiWiGqz6OuGhD4yz7Ebsz4Xke0EnD%2BPnEI5X%2F9DH7HKwejboDo2O8wBUeoTmOQ%2Bqvu69HA%2BN16kefG5wmwe0C01IRv5xay8GqIy6AU%2BVHHQ5biVCuNUNmwee5khZm6zDAbqb3UAHm39b7JPePK0iBN6DEi33KopBUtxSbPBfhwxq5KpxE2UWWXv8d59NUHrRZTxrh6c3IN3FW%2Fc6dYuYFWo9bv40%2F%2Fg6IfA6aPt%2FiIAI%2Fk6%2Bp67kwwz932vAY6pgEsgGZQ0GoTm0c%2BPHsYljFDxMC%2F5afc6UqBLkEuvUzmHRytAXUypxx941mEu6Bubgei1eWVJBUvbQ64H0e4%2BFvSRlyabFbzbcCxb27qSvOwFGLJpGt2628N5xhd2YvCW9rQN7oxuy%2F4%2F0uTJklP3XVMfPOnYj3Mwd6jImF1PcYP3EhoUkW%2B4PhdZS8CesbbomnRyNaG96eTsTG8fN%2BIdVSqh0hrYv4n&X-Amz-Signature=227363c2ff2beab56b51ac4e743c71e7958a06202a31dd39f6d3cff5c996ec6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXH5BIOY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEP7lKXOLp0e%2Bw5Fqpg9SD4Eu1P8fgCrvzqbYlavwxjxAiBrF5GkoXP5%2B%2FB%2BQS9I8aNdihn2S4YfdW0nNuSDNvImoiqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcV7afvTbkDr8WM2SKtwDlc0UtoydbT8s3whbarf4oiI5FCE0xsNj7uZSreaqxvHyt3xqg2IZyyK2kSEHTT53kM1GmC7HJF2Z7mGixhF3b9cHTr2u%2FN1lPMRlK3%2FP2SRRTf%2FRMMXlHKF2%2BDDKau2IKSf%2BnKKAUINXFQ1umkDEikig6QCPoQ52N1rs1FMKk91x8Av4I9oY7pR2TybXTJ9LKKS%2FcGBm3yJzxIxg6dV1cK88DLJA96xW7KsdKGDTGkK2RlbDIGiZaeO%2FWI9Sdvhi1uCJO5%2BNECsoMgHX%2FZHo1YXyqvXLaemMXtWtJRpNlICrGkIE1R0fWiRKMKevxc%2FkGKnPye%2F7gspfkeBY1Efoo3leonSItBQrCFvnNw67fIMbeiv%2BJquhLcLT8osaOa3G30I5hFjiWiGqz6OuGhD4yz7Ebsz4Xke0EnD%2BPnEI5X%2F9DH7HKwejboDo2O8wBUeoTmOQ%2Bqvu69HA%2BN16kefG5wmwe0C01IRv5xay8GqIy6AU%2BVHHQ5biVCuNUNmwee5khZm6zDAbqb3UAHm39b7JPePK0iBN6DEi33KopBUtxSbPBfhwxq5KpxE2UWWXv8d59NUHrRZTxrh6c3IN3FW%2Fc6dYuYFWo9bv40%2F%2Fg6IfA6aPt%2FiIAI%2Fk6%2Bp67kwwz932vAY6pgEsgGZQ0GoTm0c%2BPHsYljFDxMC%2F5afc6UqBLkEuvUzmHRytAXUypxx941mEu6Bubgei1eWVJBUvbQ64H0e4%2BFvSRlyabFbzbcCxb27qSvOwFGLJpGt2628N5xhd2YvCW9rQN7oxuy%2F4%2F0uTJklP3XVMfPOnYj3Mwd6jImF1PcYP3EhoUkW%2B4PhdZS8CesbbomnRyNaG96eTsTG8fN%2BIdVSqh0hrYv4n&X-Amz-Signature=d191c1d74a0d6b8221f51f7be456393d7eb923cc59c0c326566ccee5447ef369&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXH5BIOY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEP7lKXOLp0e%2Bw5Fqpg9SD4Eu1P8fgCrvzqbYlavwxjxAiBrF5GkoXP5%2B%2FB%2BQS9I8aNdihn2S4YfdW0nNuSDNvImoiqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcV7afvTbkDr8WM2SKtwDlc0UtoydbT8s3whbarf4oiI5FCE0xsNj7uZSreaqxvHyt3xqg2IZyyK2kSEHTT53kM1GmC7HJF2Z7mGixhF3b9cHTr2u%2FN1lPMRlK3%2FP2SRRTf%2FRMMXlHKF2%2BDDKau2IKSf%2BnKKAUINXFQ1umkDEikig6QCPoQ52N1rs1FMKk91x8Av4I9oY7pR2TybXTJ9LKKS%2FcGBm3yJzxIxg6dV1cK88DLJA96xW7KsdKGDTGkK2RlbDIGiZaeO%2FWI9Sdvhi1uCJO5%2BNECsoMgHX%2FZHo1YXyqvXLaemMXtWtJRpNlICrGkIE1R0fWiRKMKevxc%2FkGKnPye%2F7gspfkeBY1Efoo3leonSItBQrCFvnNw67fIMbeiv%2BJquhLcLT8osaOa3G30I5hFjiWiGqz6OuGhD4yz7Ebsz4Xke0EnD%2BPnEI5X%2F9DH7HKwejboDo2O8wBUeoTmOQ%2Bqvu69HA%2BN16kefG5wmwe0C01IRv5xay8GqIy6AU%2BVHHQ5biVCuNUNmwee5khZm6zDAbqb3UAHm39b7JPePK0iBN6DEi33KopBUtxSbPBfhwxq5KpxE2UWWXv8d59NUHrRZTxrh6c3IN3FW%2Fc6dYuYFWo9bv40%2F%2Fg6IfA6aPt%2FiIAI%2Fk6%2Bp67kwwz932vAY6pgEsgGZQ0GoTm0c%2BPHsYljFDxMC%2F5afc6UqBLkEuvUzmHRytAXUypxx941mEu6Bubgei1eWVJBUvbQ64H0e4%2BFvSRlyabFbzbcCxb27qSvOwFGLJpGt2628N5xhd2YvCW9rQN7oxuy%2F4%2F0uTJklP3XVMfPOnYj3Mwd6jImF1PcYP3EhoUkW%2B4PhdZS8CesbbomnRyNaG96eTsTG8fN%2BIdVSqh0hrYv4n&X-Amz-Signature=4e430067ba6bd2aec2236c43ecbb74cd00ce884b0acc2a2a2abae2a7e0e151b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXH5BIOY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEP7lKXOLp0e%2Bw5Fqpg9SD4Eu1P8fgCrvzqbYlavwxjxAiBrF5GkoXP5%2B%2FB%2BQS9I8aNdihn2S4YfdW0nNuSDNvImoiqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcV7afvTbkDr8WM2SKtwDlc0UtoydbT8s3whbarf4oiI5FCE0xsNj7uZSreaqxvHyt3xqg2IZyyK2kSEHTT53kM1GmC7HJF2Z7mGixhF3b9cHTr2u%2FN1lPMRlK3%2FP2SRRTf%2FRMMXlHKF2%2BDDKau2IKSf%2BnKKAUINXFQ1umkDEikig6QCPoQ52N1rs1FMKk91x8Av4I9oY7pR2TybXTJ9LKKS%2FcGBm3yJzxIxg6dV1cK88DLJA96xW7KsdKGDTGkK2RlbDIGiZaeO%2FWI9Sdvhi1uCJO5%2BNECsoMgHX%2FZHo1YXyqvXLaemMXtWtJRpNlICrGkIE1R0fWiRKMKevxc%2FkGKnPye%2F7gspfkeBY1Efoo3leonSItBQrCFvnNw67fIMbeiv%2BJquhLcLT8osaOa3G30I5hFjiWiGqz6OuGhD4yz7Ebsz4Xke0EnD%2BPnEI5X%2F9DH7HKwejboDo2O8wBUeoTmOQ%2Bqvu69HA%2BN16kefG5wmwe0C01IRv5xay8GqIy6AU%2BVHHQ5biVCuNUNmwee5khZm6zDAbqb3UAHm39b7JPePK0iBN6DEi33KopBUtxSbPBfhwxq5KpxE2UWWXv8d59NUHrRZTxrh6c3IN3FW%2Fc6dYuYFWo9bv40%2F%2Fg6IfA6aPt%2FiIAI%2Fk6%2Bp67kwwz932vAY6pgEsgGZQ0GoTm0c%2BPHsYljFDxMC%2F5afc6UqBLkEuvUzmHRytAXUypxx941mEu6Bubgei1eWVJBUvbQ64H0e4%2BFvSRlyabFbzbcCxb27qSvOwFGLJpGt2628N5xhd2YvCW9rQN7oxuy%2F4%2F0uTJklP3XVMfPOnYj3Mwd6jImF1PcYP3EhoUkW%2B4PhdZS8CesbbomnRyNaG96eTsTG8fN%2BIdVSqh0hrYv4n&X-Amz-Signature=e2d5c82884acc7721da30ec49808881f6110e131c3fa79aa39f339057a5c0273&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXH5BIOY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEP7lKXOLp0e%2Bw5Fqpg9SD4Eu1P8fgCrvzqbYlavwxjxAiBrF5GkoXP5%2B%2FB%2BQS9I8aNdihn2S4YfdW0nNuSDNvImoiqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcV7afvTbkDr8WM2SKtwDlc0UtoydbT8s3whbarf4oiI5FCE0xsNj7uZSreaqxvHyt3xqg2IZyyK2kSEHTT53kM1GmC7HJF2Z7mGixhF3b9cHTr2u%2FN1lPMRlK3%2FP2SRRTf%2FRMMXlHKF2%2BDDKau2IKSf%2BnKKAUINXFQ1umkDEikig6QCPoQ52N1rs1FMKk91x8Av4I9oY7pR2TybXTJ9LKKS%2FcGBm3yJzxIxg6dV1cK88DLJA96xW7KsdKGDTGkK2RlbDIGiZaeO%2FWI9Sdvhi1uCJO5%2BNECsoMgHX%2FZHo1YXyqvXLaemMXtWtJRpNlICrGkIE1R0fWiRKMKevxc%2FkGKnPye%2F7gspfkeBY1Efoo3leonSItBQrCFvnNw67fIMbeiv%2BJquhLcLT8osaOa3G30I5hFjiWiGqz6OuGhD4yz7Ebsz4Xke0EnD%2BPnEI5X%2F9DH7HKwejboDo2O8wBUeoTmOQ%2Bqvu69HA%2BN16kefG5wmwe0C01IRv5xay8GqIy6AU%2BVHHQ5biVCuNUNmwee5khZm6zDAbqb3UAHm39b7JPePK0iBN6DEi33KopBUtxSbPBfhwxq5KpxE2UWWXv8d59NUHrRZTxrh6c3IN3FW%2Fc6dYuYFWo9bv40%2F%2Fg6IfA6aPt%2FiIAI%2Fk6%2Bp67kwwz932vAY6pgEsgGZQ0GoTm0c%2BPHsYljFDxMC%2F5afc6UqBLkEuvUzmHRytAXUypxx941mEu6Bubgei1eWVJBUvbQ64H0e4%2BFvSRlyabFbzbcCxb27qSvOwFGLJpGt2628N5xhd2YvCW9rQN7oxuy%2F4%2F0uTJklP3XVMfPOnYj3Mwd6jImF1PcYP3EhoUkW%2B4PhdZS8CesbbomnRyNaG96eTsTG8fN%2BIdVSqh0hrYv4n&X-Amz-Signature=2f70a370c56fc2ff72aa24fcc7aee8bd5acca96e6dba5521238ddcdcd3576154&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXH5BIOY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEP7lKXOLp0e%2Bw5Fqpg9SD4Eu1P8fgCrvzqbYlavwxjxAiBrF5GkoXP5%2B%2FB%2BQS9I8aNdihn2S4YfdW0nNuSDNvImoiqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcV7afvTbkDr8WM2SKtwDlc0UtoydbT8s3whbarf4oiI5FCE0xsNj7uZSreaqxvHyt3xqg2IZyyK2kSEHTT53kM1GmC7HJF2Z7mGixhF3b9cHTr2u%2FN1lPMRlK3%2FP2SRRTf%2FRMMXlHKF2%2BDDKau2IKSf%2BnKKAUINXFQ1umkDEikig6QCPoQ52N1rs1FMKk91x8Av4I9oY7pR2TybXTJ9LKKS%2FcGBm3yJzxIxg6dV1cK88DLJA96xW7KsdKGDTGkK2RlbDIGiZaeO%2FWI9Sdvhi1uCJO5%2BNECsoMgHX%2FZHo1YXyqvXLaemMXtWtJRpNlICrGkIE1R0fWiRKMKevxc%2FkGKnPye%2F7gspfkeBY1Efoo3leonSItBQrCFvnNw67fIMbeiv%2BJquhLcLT8osaOa3G30I5hFjiWiGqz6OuGhD4yz7Ebsz4Xke0EnD%2BPnEI5X%2F9DH7HKwejboDo2O8wBUeoTmOQ%2Bqvu69HA%2BN16kefG5wmwe0C01IRv5xay8GqIy6AU%2BVHHQ5biVCuNUNmwee5khZm6zDAbqb3UAHm39b7JPePK0iBN6DEi33KopBUtxSbPBfhwxq5KpxE2UWWXv8d59NUHrRZTxrh6c3IN3FW%2Fc6dYuYFWo9bv40%2F%2Fg6IfA6aPt%2FiIAI%2Fk6%2Bp67kwwz932vAY6pgEsgGZQ0GoTm0c%2BPHsYljFDxMC%2F5afc6UqBLkEuvUzmHRytAXUypxx941mEu6Bubgei1eWVJBUvbQ64H0e4%2BFvSRlyabFbzbcCxb27qSvOwFGLJpGt2628N5xhd2YvCW9rQN7oxuy%2F4%2F0uTJklP3XVMfPOnYj3Mwd6jImF1PcYP3EhoUkW%2B4PhdZS8CesbbomnRyNaG96eTsTG8fN%2BIdVSqh0hrYv4n&X-Amz-Signature=52a7e6451108059b8a10dce812ceaef456624f91a344e2cab3ccbdc230dadd45&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXH5BIOY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEP7lKXOLp0e%2Bw5Fqpg9SD4Eu1P8fgCrvzqbYlavwxjxAiBrF5GkoXP5%2B%2FB%2BQS9I8aNdihn2S4YfdW0nNuSDNvImoiqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcV7afvTbkDr8WM2SKtwDlc0UtoydbT8s3whbarf4oiI5FCE0xsNj7uZSreaqxvHyt3xqg2IZyyK2kSEHTT53kM1GmC7HJF2Z7mGixhF3b9cHTr2u%2FN1lPMRlK3%2FP2SRRTf%2FRMMXlHKF2%2BDDKau2IKSf%2BnKKAUINXFQ1umkDEikig6QCPoQ52N1rs1FMKk91x8Av4I9oY7pR2TybXTJ9LKKS%2FcGBm3yJzxIxg6dV1cK88DLJA96xW7KsdKGDTGkK2RlbDIGiZaeO%2FWI9Sdvhi1uCJO5%2BNECsoMgHX%2FZHo1YXyqvXLaemMXtWtJRpNlICrGkIE1R0fWiRKMKevxc%2FkGKnPye%2F7gspfkeBY1Efoo3leonSItBQrCFvnNw67fIMbeiv%2BJquhLcLT8osaOa3G30I5hFjiWiGqz6OuGhD4yz7Ebsz4Xke0EnD%2BPnEI5X%2F9DH7HKwejboDo2O8wBUeoTmOQ%2Bqvu69HA%2BN16kefG5wmwe0C01IRv5xay8GqIy6AU%2BVHHQ5biVCuNUNmwee5khZm6zDAbqb3UAHm39b7JPePK0iBN6DEi33KopBUtxSbPBfhwxq5KpxE2UWWXv8d59NUHrRZTxrh6c3IN3FW%2Fc6dYuYFWo9bv40%2F%2Fg6IfA6aPt%2FiIAI%2Fk6%2Bp67kwwz932vAY6pgEsgGZQ0GoTm0c%2BPHsYljFDxMC%2F5afc6UqBLkEuvUzmHRytAXUypxx941mEu6Bubgei1eWVJBUvbQ64H0e4%2BFvSRlyabFbzbcCxb27qSvOwFGLJpGt2628N5xhd2YvCW9rQN7oxuy%2F4%2F0uTJklP3XVMfPOnYj3Mwd6jImF1PcYP3EhoUkW%2B4PhdZS8CesbbomnRyNaG96eTsTG8fN%2BIdVSqh0hrYv4n&X-Amz-Signature=26f7b3c8a69a2f2da6d2816c7f86a203fea580dabe76fc4af2880aed55b1cf26&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Y2PFIZU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEif4%2Br7DkXIvMnc7UYghQmoeZvgLFFTTS4NrXo%2B%2F%2Bx9AiBLpKSv6oqgLzMROIM4ujXsAF607do4v2UQdNUMp8tkkSqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4wKQWrztH78nwG0sKtwDdQOC4bcRiQcGQxW2DoHV3LVRAF6jYgh83R7DXuabEDcPiH2KUCBgCPvhIS56tQ4FFZ%2B0IRzmFt9k7Ot05pwdDs%2BKqRwRSu%2B5NE2A%2BsNNaC96t4ZFlzeXQ5sNeW3QZvH%2FGgTr80MtHEdSPD0WbXrIvosVIue87G%2B38y8OaeCO0pgicNd85gl1IWsk%2BjVRCdI7UAFoxQo1VyWWK0Jc%2B2Ymr1h2qObm%2Fzm%2BSMDq5okKPTaNiQRuEFR7NNxrcVzWLUKK9byyfInNeEYU5gXUXzeYIbrbSjJLINb8K4Y1x6iLOUwQ%2B%2BB8QfjPD0As3cTDcROJUFG2NcC8GkPOOuLOGAjwmMIgKCdx4YigpckXC5BDORsYtGNS93ss9PYKcQus0WbbuP2Ma9PfzRExuS7HX7DqM0NXCnrqY0klbTnhIl%2FlnrqBImDkZZTpvuSoqZsU3WeZ22RpttVsV%2BYl%2FeKrIV9WiVlBgFKnqpJnHkExhkz2DZQf%2BH60SQtNKPetSasjJY400u5bfXMSGdVuCM%2FRpD7l86m%2FQIjpdfGp5pYP%2FLbxhaCU6Y2OuTRAUQwMnGwdJUGRTpFW77Vs5UzXkZWmDZaObZ6UM%2FcYE1HQjXVtZSXGDOwmbItX0h1dCR6exf4wxN32vAY6pgELtonsiL0o2naRG8YgNTKBSL6sba%2FpnEuASM5Tl3ChMb3iLeV3lfbET66mM3%2BYMY0r5KL4wsNp%2BcAb0Lxri5giVhKLmUR5m3Ti41EQ5wOi%2FSFiENcAkfhuAj1PZ8pyR2LyyNGXp5W8FiFalXeQ%2BmLvS5GW61Y79xH5a%2FdixruD6tguXEgm4kAAOI8KWBndBPlebtp5x%2FF3jJ3DnAEbyV4Im%2FoLr%2B6r&X-Amz-Signature=7013d5611d366431aed25ef0244fd07c0226884cd38c9d33e1d917400fb07858&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645JZVUQU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3jqwYef7ooD0RPPaTRUp6NVCp6yD4CF7%2BYA1six74kwIhAPiAumn5pwL4ENCSKZFxfijKUAumpHacr5w%2FOxdrrEvpKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlV8fAaIP5j5hW3GYq3AN80qCq12RPbSkz%2FxXVfOu%2FSaX0oZdAFiYEbYHmexjT0J8SlFUTjUGIsCdrYfNMhSZmvzMX%2B3hr%2BnWl28vQ3SFFenWDLjS6jnnPKEZ2naLFsMI1u48dvZJ3JjDPR%2Bi8JWEggOCVdOno98tXyuJaGCl6GFGnGvZAnnbFfl0BLn%2Bf8otrivx65LdUrcuPBjOySKRZHbTOUBkrAi7praay77qRQSoBIK9S6v1pP5MO6JZcvKAQhbLPMjBJnuwUVJNUk9XOeLfgFzYf3s5uyH%2BU7LeyyorgUm4v%2B0rRbUPKaHZRiISlqyYxprK9pOxFIT9oPqgYUpjXnwO%2BnintaA7GYlbnOtHhTyPfR282rOBGVKoLgdbT0P%2F71P0vL7%2BOOrXmvnxQG8DqG7VQAX49sOIwm8iZmer4CPeFRlEu0u%2Bu06HCruujAIauTQReZOzJMESqmD0auGd%2B%2Fcjcj1BixjjgQECmDYzf4Jg9XkNoYQAuNY78I6s2R%2Fh2G%2FG%2BT37zPv9RFuZP%2BvPTsQ40GY9XTCaeL6RYZi0Sfx5Lxa%2F%2B95gQhQItXm6UJX6uhhAZVRQnNznW%2BLVSd3zgNRDWiUGAL6iy%2F9KqJZnHbCZ5Pf3pAReYGmF93ruKfHglPzVixVlePzC13fa8BjqkAVB6Ajj%2BnIGZgAmbrxctRGcD%2FbwKJq9PXsGsPa4%2BJVnb5MyhKIIgDyrMo7etkEiz78rISqDJ1%2FyX0vhh7iO4Wagf3kx2bgQ5g9mLGf2CBIeuulsuwuIB4vdCe33ikBLdRgLoULOpuYUoZkd5BQOrUOPo3O%2FPbEMv2nrQfN3PuH5%2BNQECTX2rzCWg1ZuiawNpXbHgWFDHyvU730YJdDGN%2BVK4PN4S&X-Amz-Signature=b7436d85ec6c39074cf71d7fd00b6ff23cc2d50a8a82cbbfe298d77ecf5b0577&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF46KMLH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2B1iLT423Ic66c4JhfsEr5qIwu7YfVPV3l5bFaRmcQIAiAimX%2BdzMDpL673YdC6D8UNPieCwz0yM%2Fycup%2FshfkSkiqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsDDPi4CFDfQp0rb2KtwD7t6ofvWWwNaae6n%2FFGVUjUjza4nFIPNTOza9piS0ZcX8YENuJ6DSu4O%2FihyKpwdgdyFz8%2BCu3yo18H7mfsJ9pT4Ztx5FSjv07A9sIhi6V00XufFoD4KMNOAEtrwU0KoKIXjgd8LTkkeieGhisvSBNLnvMpvB4gnBvjF9cf%2FU%2FhMREnkm0qSunVMusoFHGRHOWWW24qcWGpw5qI%2FY6y3eoYyME86rOvin1oqOIV8Tu2P7qqBZ%2F4h45QgP8hoGxMyg%2B0MITnBLDJ3pwuv7KUtMmJpnGkiuhth5anbhwVqz%2Bd%2BykKbByN5GdqSqdEekUKP2tTJUG7jGs8u4uGR92wi8k3XkbOpE3j9rCZXVHAXIEc51zliml3w5YA95cqvO0SagwJ8d3DQjK2V9%2F1ZyM7hyvMsbI4YXa1%2FN%2FcGB8TGiTfPuK2W12GssFKa3afYQcWRW7pgRj8IHmq2PKhgUDb2ycCI%2B5cQ5s9Cun03cDWuHOyYhm5OfOiBxJz%2FE%2BG6rPrfajQolunaHf7ObO%2FNC2gQQhtZMGLdIJpUhFU%2Fq5%2FtpgCLMjgbqSEdn%2BBrFf6ziwEUt5loknGG4qrWN3nfplOniwskS2QyxNsLCCiPZJyIJXpFqwwakir4PFSFS%2BgUwn932vAY6pgF2upqzDgGvfeaRc1B95eWHUX%2BntUxdqJ1v6YAcKrjiACX%2BDT5%2BzJ92dl4hDvV%2FhQ8NBnewDrRcr8VRwAzlCZPTkeU2xgIibWKzKApcRK4c6%2FD0N2JDGU6FDVyLtMVQnXtsqVNjupxwF6UZvqxNoqCggVGYjqgHNlBg4WpexTrUSUNS1oex22nLQYGXM75LwEG%2FIwn4jITc9apgRBX5vQYmm6HZPsrz&X-Amz-Signature=48cdfa276cbb4fece3d6bd7539fd7f8480120c92147034e28b10efcb36285dbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF46KMLH%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2B1iLT423Ic66c4JhfsEr5qIwu7YfVPV3l5bFaRmcQIAiAimX%2BdzMDpL673YdC6D8UNPieCwz0yM%2Fycup%2FshfkSkiqIBAjO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsDDPi4CFDfQp0rb2KtwD7t6ofvWWwNaae6n%2FFGVUjUjza4nFIPNTOza9piS0ZcX8YENuJ6DSu4O%2FihyKpwdgdyFz8%2BCu3yo18H7mfsJ9pT4Ztx5FSjv07A9sIhi6V00XufFoD4KMNOAEtrwU0KoKIXjgd8LTkkeieGhisvSBNLnvMpvB4gnBvjF9cf%2FU%2FhMREnkm0qSunVMusoFHGRHOWWW24qcWGpw5qI%2FY6y3eoYyME86rOvin1oqOIV8Tu2P7qqBZ%2F4h45QgP8hoGxMyg%2B0MITnBLDJ3pwuv7KUtMmJpnGkiuhth5anbhwVqz%2Bd%2BykKbByN5GdqSqdEekUKP2tTJUG7jGs8u4uGR92wi8k3XkbOpE3j9rCZXVHAXIEc51zliml3w5YA95cqvO0SagwJ8d3DQjK2V9%2F1ZyM7hyvMsbI4YXa1%2FN%2FcGB8TGiTfPuK2W12GssFKa3afYQcWRW7pgRj8IHmq2PKhgUDb2ycCI%2B5cQ5s9Cun03cDWuHOyYhm5OfOiBxJz%2FE%2BG6rPrfajQolunaHf7ObO%2FNC2gQQhtZMGLdIJpUhFU%2Fq5%2FtpgCLMjgbqSEdn%2BBrFf6ziwEUt5loknGG4qrWN3nfplOniwskS2QyxNsLCCiPZJyIJXpFqwwakir4PFSFS%2BgUwn932vAY6pgF2upqzDgGvfeaRc1B95eWHUX%2BntUxdqJ1v6YAcKrjiACX%2BDT5%2BzJ92dl4hDvV%2FhQ8NBnewDrRcr8VRwAzlCZPTkeU2xgIibWKzKApcRK4c6%2FD0N2JDGU6FDVyLtMVQnXtsqVNjupxwF6UZvqxNoqCggVGYjqgHNlBg4WpexTrUSUNS1oex22nLQYGXM75LwEG%2FIwn4jITc9apgRBX5vQYmm6HZPsrz&X-Amz-Signature=82c920ec6094ab9cf3de7d58d5ad8143902626b8d6b073038b3ef16adb62a0a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
