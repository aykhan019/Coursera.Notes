

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EW4I6ZT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIH2Z6wSv%2FQOahY3GeC%2FMkKW3rnmbW2zK7E6fH6hDwCeuAiEA%2Fl5gkmeZqbD67CLmzjKaaunJJE0vb9Zgp4vl5oV7WHkq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJoEhiRvuWnfmspU%2FCrcA3aDBb833nUD4ExtKJVaaxrP2oWadA9cPzRtSTpu35wd%2Fu412pTpCWxJZfFXTZS86MfsaGg27vuwFT4Rbev%2F6t%2B13thDmnTBdZuh4cQcuBXBbQWG0c45bO4LmEl4GiETCyZ8n%2Fr1VVYTWXa%2FmAY4MsO8VonpGDDtAD7djZgEhrGy5NOzGAKnMEUPY0%2BUTFRkZwMLIUQiyB%2FKhA8j6FS67RYKi9Ku%2B8uvIfKHjoIldkjOIPlOtUn6uMXpzc5ZS9y%2B6uJf2teUyh9zJW%2FQQIw6nnzeirjVA5517v6fAU8clK7UfVImU39w6x9V%2FbWTiEZc%2B7veEnX2FVpc0p0jCsga%2B9%2BgBX%2BTvxyF%2F7HPikWB3%2B5w9EkK1R1kDnXoDs2iy1N9UzIcopAlfN1hgy5nKyZrtw5s8WjrNeVY%2ByVX%2FiRR3Ldb9pYbePOxE0hQohnVuACC3yBeQTYJEGJc39S2V6ne1S61oKyn7KL%2B2weXZxZTpaG7%2FRSyWvNS18eGSYAzfdFRWKlPL%2FDsbJZEdRgUJIqrDe5v08kk2bykgMQtOpX0LE04aMsmd%2FbEcTFYij2hROBJT2faUb6U%2BA%2Bz1P%2B1kkBxJ43yLfuyDY8lEG86PvEh5ysL%2BoTs4rzDLZuq6LexMPmbk70GOqUBuXVhjjWhqO0YU2ZtAdZvauXCtJUV5yAGV0DU4%2F0MWpyAKS2WSQ8rXOLoTvOn%2Bjej5GBf9smr5u8IPLmcG6kwavMYX719IJgclrBWt2UXwjtYGPQjud6PIIIgWWQHR0vIgBmLMGkPcXt0Z%2FES8aIN37DtwF93%2BpkKbG0zXjS%2FO6qMVzYqL6ODyDMJ5R19kDeEqffLZKMtn6bboL36rATstROh3poA&X-Amz-Signature=5e5eb4a4bd49923251bafb91ee992fd01f3a6ead2e48ca19c80e3be01606397c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EW4I6ZT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIH2Z6wSv%2FQOahY3GeC%2FMkKW3rnmbW2zK7E6fH6hDwCeuAiEA%2Fl5gkmeZqbD67CLmzjKaaunJJE0vb9Zgp4vl5oV7WHkq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJoEhiRvuWnfmspU%2FCrcA3aDBb833nUD4ExtKJVaaxrP2oWadA9cPzRtSTpu35wd%2Fu412pTpCWxJZfFXTZS86MfsaGg27vuwFT4Rbev%2F6t%2B13thDmnTBdZuh4cQcuBXBbQWG0c45bO4LmEl4GiETCyZ8n%2Fr1VVYTWXa%2FmAY4MsO8VonpGDDtAD7djZgEhrGy5NOzGAKnMEUPY0%2BUTFRkZwMLIUQiyB%2FKhA8j6FS67RYKi9Ku%2B8uvIfKHjoIldkjOIPlOtUn6uMXpzc5ZS9y%2B6uJf2teUyh9zJW%2FQQIw6nnzeirjVA5517v6fAU8clK7UfVImU39w6x9V%2FbWTiEZc%2B7veEnX2FVpc0p0jCsga%2B9%2BgBX%2BTvxyF%2F7HPikWB3%2B5w9EkK1R1kDnXoDs2iy1N9UzIcopAlfN1hgy5nKyZrtw5s8WjrNeVY%2ByVX%2FiRR3Ldb9pYbePOxE0hQohnVuACC3yBeQTYJEGJc39S2V6ne1S61oKyn7KL%2B2weXZxZTpaG7%2FRSyWvNS18eGSYAzfdFRWKlPL%2FDsbJZEdRgUJIqrDe5v08kk2bykgMQtOpX0LE04aMsmd%2FbEcTFYij2hROBJT2faUb6U%2BA%2Bz1P%2B1kkBxJ43yLfuyDY8lEG86PvEh5ysL%2BoTs4rzDLZuq6LexMPmbk70GOqUBuXVhjjWhqO0YU2ZtAdZvauXCtJUV5yAGV0DU4%2F0MWpyAKS2WSQ8rXOLoTvOn%2Bjej5GBf9smr5u8IPLmcG6kwavMYX719IJgclrBWt2UXwjtYGPQjud6PIIIgWWQHR0vIgBmLMGkPcXt0Z%2FES8aIN37DtwF93%2BpkKbG0zXjS%2FO6qMVzYqL6ODyDMJ5R19kDeEqffLZKMtn6bboL36rATstROh3poA&X-Amz-Signature=33896448a5388038cfeb4a913f2f7f4f3ecfb0325259634dd9e8d4bb95d65ea8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EW4I6ZT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIH2Z6wSv%2FQOahY3GeC%2FMkKW3rnmbW2zK7E6fH6hDwCeuAiEA%2Fl5gkmeZqbD67CLmzjKaaunJJE0vb9Zgp4vl5oV7WHkq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJoEhiRvuWnfmspU%2FCrcA3aDBb833nUD4ExtKJVaaxrP2oWadA9cPzRtSTpu35wd%2Fu412pTpCWxJZfFXTZS86MfsaGg27vuwFT4Rbev%2F6t%2B13thDmnTBdZuh4cQcuBXBbQWG0c45bO4LmEl4GiETCyZ8n%2Fr1VVYTWXa%2FmAY4MsO8VonpGDDtAD7djZgEhrGy5NOzGAKnMEUPY0%2BUTFRkZwMLIUQiyB%2FKhA8j6FS67RYKi9Ku%2B8uvIfKHjoIldkjOIPlOtUn6uMXpzc5ZS9y%2B6uJf2teUyh9zJW%2FQQIw6nnzeirjVA5517v6fAU8clK7UfVImU39w6x9V%2FbWTiEZc%2B7veEnX2FVpc0p0jCsga%2B9%2BgBX%2BTvxyF%2F7HPikWB3%2B5w9EkK1R1kDnXoDs2iy1N9UzIcopAlfN1hgy5nKyZrtw5s8WjrNeVY%2ByVX%2FiRR3Ldb9pYbePOxE0hQohnVuACC3yBeQTYJEGJc39S2V6ne1S61oKyn7KL%2B2weXZxZTpaG7%2FRSyWvNS18eGSYAzfdFRWKlPL%2FDsbJZEdRgUJIqrDe5v08kk2bykgMQtOpX0LE04aMsmd%2FbEcTFYij2hROBJT2faUb6U%2BA%2Bz1P%2B1kkBxJ43yLfuyDY8lEG86PvEh5ysL%2BoTs4rzDLZuq6LexMPmbk70GOqUBuXVhjjWhqO0YU2ZtAdZvauXCtJUV5yAGV0DU4%2F0MWpyAKS2WSQ8rXOLoTvOn%2Bjej5GBf9smr5u8IPLmcG6kwavMYX719IJgclrBWt2UXwjtYGPQjud6PIIIgWWQHR0vIgBmLMGkPcXt0Z%2FES8aIN37DtwF93%2BpkKbG0zXjS%2FO6qMVzYqL6ODyDMJ5R19kDeEqffLZKMtn6bboL36rATstROh3poA&X-Amz-Signature=67e46c530fae72fda7627c0605d1ee4b561523165e48d8cfd654d9eef37c863a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EW4I6ZT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIH2Z6wSv%2FQOahY3GeC%2FMkKW3rnmbW2zK7E6fH6hDwCeuAiEA%2Fl5gkmeZqbD67CLmzjKaaunJJE0vb9Zgp4vl5oV7WHkq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJoEhiRvuWnfmspU%2FCrcA3aDBb833nUD4ExtKJVaaxrP2oWadA9cPzRtSTpu35wd%2Fu412pTpCWxJZfFXTZS86MfsaGg27vuwFT4Rbev%2F6t%2B13thDmnTBdZuh4cQcuBXBbQWG0c45bO4LmEl4GiETCyZ8n%2Fr1VVYTWXa%2FmAY4MsO8VonpGDDtAD7djZgEhrGy5NOzGAKnMEUPY0%2BUTFRkZwMLIUQiyB%2FKhA8j6FS67RYKi9Ku%2B8uvIfKHjoIldkjOIPlOtUn6uMXpzc5ZS9y%2B6uJf2teUyh9zJW%2FQQIw6nnzeirjVA5517v6fAU8clK7UfVImU39w6x9V%2FbWTiEZc%2B7veEnX2FVpc0p0jCsga%2B9%2BgBX%2BTvxyF%2F7HPikWB3%2B5w9EkK1R1kDnXoDs2iy1N9UzIcopAlfN1hgy5nKyZrtw5s8WjrNeVY%2ByVX%2FiRR3Ldb9pYbePOxE0hQohnVuACC3yBeQTYJEGJc39S2V6ne1S61oKyn7KL%2B2weXZxZTpaG7%2FRSyWvNS18eGSYAzfdFRWKlPL%2FDsbJZEdRgUJIqrDe5v08kk2bykgMQtOpX0LE04aMsmd%2FbEcTFYij2hROBJT2faUb6U%2BA%2Bz1P%2B1kkBxJ43yLfuyDY8lEG86PvEh5ysL%2BoTs4rzDLZuq6LexMPmbk70GOqUBuXVhjjWhqO0YU2ZtAdZvauXCtJUV5yAGV0DU4%2F0MWpyAKS2WSQ8rXOLoTvOn%2Bjej5GBf9smr5u8IPLmcG6kwavMYX719IJgclrBWt2UXwjtYGPQjud6PIIIgWWQHR0vIgBmLMGkPcXt0Z%2FES8aIN37DtwF93%2BpkKbG0zXjS%2FO6qMVzYqL6ODyDMJ5R19kDeEqffLZKMtn6bboL36rATstROh3poA&X-Amz-Signature=38be4e893dec2047aec4cf133937fb6563c80f0e2c4b447d2a4893546f115203&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EW4I6ZT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIH2Z6wSv%2FQOahY3GeC%2FMkKW3rnmbW2zK7E6fH6hDwCeuAiEA%2Fl5gkmeZqbD67CLmzjKaaunJJE0vb9Zgp4vl5oV7WHkq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJoEhiRvuWnfmspU%2FCrcA3aDBb833nUD4ExtKJVaaxrP2oWadA9cPzRtSTpu35wd%2Fu412pTpCWxJZfFXTZS86MfsaGg27vuwFT4Rbev%2F6t%2B13thDmnTBdZuh4cQcuBXBbQWG0c45bO4LmEl4GiETCyZ8n%2Fr1VVYTWXa%2FmAY4MsO8VonpGDDtAD7djZgEhrGy5NOzGAKnMEUPY0%2BUTFRkZwMLIUQiyB%2FKhA8j6FS67RYKi9Ku%2B8uvIfKHjoIldkjOIPlOtUn6uMXpzc5ZS9y%2B6uJf2teUyh9zJW%2FQQIw6nnzeirjVA5517v6fAU8clK7UfVImU39w6x9V%2FbWTiEZc%2B7veEnX2FVpc0p0jCsga%2B9%2BgBX%2BTvxyF%2F7HPikWB3%2B5w9EkK1R1kDnXoDs2iy1N9UzIcopAlfN1hgy5nKyZrtw5s8WjrNeVY%2ByVX%2FiRR3Ldb9pYbePOxE0hQohnVuACC3yBeQTYJEGJc39S2V6ne1S61oKyn7KL%2B2weXZxZTpaG7%2FRSyWvNS18eGSYAzfdFRWKlPL%2FDsbJZEdRgUJIqrDe5v08kk2bykgMQtOpX0LE04aMsmd%2FbEcTFYij2hROBJT2faUb6U%2BA%2Bz1P%2B1kkBxJ43yLfuyDY8lEG86PvEh5ysL%2BoTs4rzDLZuq6LexMPmbk70GOqUBuXVhjjWhqO0YU2ZtAdZvauXCtJUV5yAGV0DU4%2F0MWpyAKS2WSQ8rXOLoTvOn%2Bjej5GBf9smr5u8IPLmcG6kwavMYX719IJgclrBWt2UXwjtYGPQjud6PIIIgWWQHR0vIgBmLMGkPcXt0Z%2FES8aIN37DtwF93%2BpkKbG0zXjS%2FO6qMVzYqL6ODyDMJ5R19kDeEqffLZKMtn6bboL36rATstROh3poA&X-Amz-Signature=1f6577aa5f236e2df5227d706dbd2968e14650aedfb2f8ace6000e96307a8ff7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EW4I6ZT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIH2Z6wSv%2FQOahY3GeC%2FMkKW3rnmbW2zK7E6fH6hDwCeuAiEA%2Fl5gkmeZqbD67CLmzjKaaunJJE0vb9Zgp4vl5oV7WHkq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJoEhiRvuWnfmspU%2FCrcA3aDBb833nUD4ExtKJVaaxrP2oWadA9cPzRtSTpu35wd%2Fu412pTpCWxJZfFXTZS86MfsaGg27vuwFT4Rbev%2F6t%2B13thDmnTBdZuh4cQcuBXBbQWG0c45bO4LmEl4GiETCyZ8n%2Fr1VVYTWXa%2FmAY4MsO8VonpGDDtAD7djZgEhrGy5NOzGAKnMEUPY0%2BUTFRkZwMLIUQiyB%2FKhA8j6FS67RYKi9Ku%2B8uvIfKHjoIldkjOIPlOtUn6uMXpzc5ZS9y%2B6uJf2teUyh9zJW%2FQQIw6nnzeirjVA5517v6fAU8clK7UfVImU39w6x9V%2FbWTiEZc%2B7veEnX2FVpc0p0jCsga%2B9%2BgBX%2BTvxyF%2F7HPikWB3%2B5w9EkK1R1kDnXoDs2iy1N9UzIcopAlfN1hgy5nKyZrtw5s8WjrNeVY%2ByVX%2FiRR3Ldb9pYbePOxE0hQohnVuACC3yBeQTYJEGJc39S2V6ne1S61oKyn7KL%2B2weXZxZTpaG7%2FRSyWvNS18eGSYAzfdFRWKlPL%2FDsbJZEdRgUJIqrDe5v08kk2bykgMQtOpX0LE04aMsmd%2FbEcTFYij2hROBJT2faUb6U%2BA%2Bz1P%2B1kkBxJ43yLfuyDY8lEG86PvEh5ysL%2BoTs4rzDLZuq6LexMPmbk70GOqUBuXVhjjWhqO0YU2ZtAdZvauXCtJUV5yAGV0DU4%2F0MWpyAKS2WSQ8rXOLoTvOn%2Bjej5GBf9smr5u8IPLmcG6kwavMYX719IJgclrBWt2UXwjtYGPQjud6PIIIgWWQHR0vIgBmLMGkPcXt0Z%2FES8aIN37DtwF93%2BpkKbG0zXjS%2FO6qMVzYqL6ODyDMJ5R19kDeEqffLZKMtn6bboL36rATstROh3poA&X-Amz-Signature=fec0e90deec5f67ed1b3de4e0bca6c9465be7d9cce9b84f4aadb2299bdc81226&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EW4I6ZT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIH2Z6wSv%2FQOahY3GeC%2FMkKW3rnmbW2zK7E6fH6hDwCeuAiEA%2Fl5gkmeZqbD67CLmzjKaaunJJE0vb9Zgp4vl5oV7WHkq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJoEhiRvuWnfmspU%2FCrcA3aDBb833nUD4ExtKJVaaxrP2oWadA9cPzRtSTpu35wd%2Fu412pTpCWxJZfFXTZS86MfsaGg27vuwFT4Rbev%2F6t%2B13thDmnTBdZuh4cQcuBXBbQWG0c45bO4LmEl4GiETCyZ8n%2Fr1VVYTWXa%2FmAY4MsO8VonpGDDtAD7djZgEhrGy5NOzGAKnMEUPY0%2BUTFRkZwMLIUQiyB%2FKhA8j6FS67RYKi9Ku%2B8uvIfKHjoIldkjOIPlOtUn6uMXpzc5ZS9y%2B6uJf2teUyh9zJW%2FQQIw6nnzeirjVA5517v6fAU8clK7UfVImU39w6x9V%2FbWTiEZc%2B7veEnX2FVpc0p0jCsga%2B9%2BgBX%2BTvxyF%2F7HPikWB3%2B5w9EkK1R1kDnXoDs2iy1N9UzIcopAlfN1hgy5nKyZrtw5s8WjrNeVY%2ByVX%2FiRR3Ldb9pYbePOxE0hQohnVuACC3yBeQTYJEGJc39S2V6ne1S61oKyn7KL%2B2weXZxZTpaG7%2FRSyWvNS18eGSYAzfdFRWKlPL%2FDsbJZEdRgUJIqrDe5v08kk2bykgMQtOpX0LE04aMsmd%2FbEcTFYij2hROBJT2faUb6U%2BA%2Bz1P%2B1kkBxJ43yLfuyDY8lEG86PvEh5ysL%2BoTs4rzDLZuq6LexMPmbk70GOqUBuXVhjjWhqO0YU2ZtAdZvauXCtJUV5yAGV0DU4%2F0MWpyAKS2WSQ8rXOLoTvOn%2Bjej5GBf9smr5u8IPLmcG6kwavMYX719IJgclrBWt2UXwjtYGPQjud6PIIIgWWQHR0vIgBmLMGkPcXt0Z%2FES8aIN37DtwF93%2BpkKbG0zXjS%2FO6qMVzYqL6ODyDMJ5R19kDeEqffLZKMtn6bboL36rATstROh3poA&X-Amz-Signature=e2822045c8ac7e545f82dad6321964d6830f677350056ec32dff153c1fa9b7d7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EW4I6ZT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIH2Z6wSv%2FQOahY3GeC%2FMkKW3rnmbW2zK7E6fH6hDwCeuAiEA%2Fl5gkmeZqbD67CLmzjKaaunJJE0vb9Zgp4vl5oV7WHkq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJoEhiRvuWnfmspU%2FCrcA3aDBb833nUD4ExtKJVaaxrP2oWadA9cPzRtSTpu35wd%2Fu412pTpCWxJZfFXTZS86MfsaGg27vuwFT4Rbev%2F6t%2B13thDmnTBdZuh4cQcuBXBbQWG0c45bO4LmEl4GiETCyZ8n%2Fr1VVYTWXa%2FmAY4MsO8VonpGDDtAD7djZgEhrGy5NOzGAKnMEUPY0%2BUTFRkZwMLIUQiyB%2FKhA8j6FS67RYKi9Ku%2B8uvIfKHjoIldkjOIPlOtUn6uMXpzc5ZS9y%2B6uJf2teUyh9zJW%2FQQIw6nnzeirjVA5517v6fAU8clK7UfVImU39w6x9V%2FbWTiEZc%2B7veEnX2FVpc0p0jCsga%2B9%2BgBX%2BTvxyF%2F7HPikWB3%2B5w9EkK1R1kDnXoDs2iy1N9UzIcopAlfN1hgy5nKyZrtw5s8WjrNeVY%2ByVX%2FiRR3Ldb9pYbePOxE0hQohnVuACC3yBeQTYJEGJc39S2V6ne1S61oKyn7KL%2B2weXZxZTpaG7%2FRSyWvNS18eGSYAzfdFRWKlPL%2FDsbJZEdRgUJIqrDe5v08kk2bykgMQtOpX0LE04aMsmd%2FbEcTFYij2hROBJT2faUb6U%2BA%2Bz1P%2B1kkBxJ43yLfuyDY8lEG86PvEh5ysL%2BoTs4rzDLZuq6LexMPmbk70GOqUBuXVhjjWhqO0YU2ZtAdZvauXCtJUV5yAGV0DU4%2F0MWpyAKS2WSQ8rXOLoTvOn%2Bjej5GBf9smr5u8IPLmcG6kwavMYX719IJgclrBWt2UXwjtYGPQjud6PIIIgWWQHR0vIgBmLMGkPcXt0Z%2FES8aIN37DtwF93%2BpkKbG0zXjS%2FO6qMVzYqL6ODyDMJ5R19kDeEqffLZKMtn6bboL36rATstROh3poA&X-Amz-Signature=a553194c6605654ba9109772ac0ae287bccd28441233912710742b8675fbaf47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KG77TZG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDMiiYo03jD%2FlB8jTW2avA4tvOPM8o5fTmhsTG4eur9fAIhAO0oj43PhnEK97KwGASl9vwaANyHn1qC2ZUzpGEzhdqbKv8DCGAQABoMNjM3NDIzMTgzODA1Igx%2FkG7xZ9xNmsBY9hQq3AN6dF3qNwP4tkYY%2BS8MIuQw0bfbc4ozRdnU0RJtWMBC%2Bw2pyGigZLNn8eI7%2BeQl23WD9hvczcQGBAByt7sT3whx6iQCWgDP5ZhAaWS3MfnGNmj4q1xBpcbAMJs5MfIPKTsm%2FH4bcGFbFb7rDK8sKlPCSr5TzYILxWa9kDDa9YVh449so%2Fr%2BwhvdH%2FbQ2XdOOEmtvoVYQkTfBYqNzye7i8HTOr9GMYYEfVc9sZUjuuYmdhZVbCgpsAqB7bzw8aHPR0Yx8ffQZY4zDNvKwniJQ6R%2BkadAl1hg12vmTQ4FgTww6sx3XdDTUkpMepUpDE54k6u6IT3XzlR8mH1ReBsC9Dk56Q3kNCYacOngLR3rGo07p6F%2F9I96UapwSULgzmF2U61rlzfI0Qkkdc2u0E3KgWeBNwJtngSow3yA0A8SwVpZFNaV6siQeeUTe7ZW6RkoFlS8gRF9pvq9%2Bzn1k5PThhJl%2F5suScmWWwE%2Bylwpvqb703p6%2BNQx1sRyUVf1LgvG%2BZI2GZwmdCC1sm8QM9G35c5fgazmeIDwDhsfnCwmhBmDCdsVZ6NZ5ig3mbzD2lGYlUq4i7IuPN2Fp8EPV8CccdrBIxgIwkNQ33u0JgsHfbev7c2MezylX4tEVajr%2FzCOnJO9BjqkAUyylZzwKT4TCBho7N2yAkL%2FM4cG7eExFzCvlpgx%2Fdphq1K%2BVCo%2BOtwJ%2FdNZBSvwESb31NWDGo7AMBeGhmZ2AhHMiewCtccpaMzhrkGrsfRs%2BKvekzNB4MnHj16o1mD1IFxS1hTD9t8i6eiTPNpdbB49v%2BfPYTwkVmVJfgbBybjuAvN5ZGjJIIo%2BPquXV1eQl%2BJaW8H9u0LXdm36kbpfgoryg4Jy&X-Amz-Signature=10070b15c0965a569e6caf80c4f373b2f9a2610b6f4fefde653f3066ef163520&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4FPNKYX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIGsRLuefs2eYSThaA0G8gipYVhnMW0CoSxzjMJZ%2BzA%2FPAiEAsCRgcpAl6c1T7KeEtB2NWj7qmjjvs8LPRXc%2F%2BQC5nZIq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDJ%2FdFJIzCsMUyDX2ryrcAzFRZ8QASQv40GJLAm96toB0vQ0xk8gcgPlhlJun0GShEyiFGaXif1ZOng7xOzRN8KK14Zh6tatuxTPf%2Bi0zdzM2NLcV2LwcIBgyto3y%2BUS1iNBKC%2FplktKNjuekZLg0u1vU5Oea%2BbqnNy71hb7qCrdAMTCdAVsIMJVcLkVxtJJWrhLqaI%2FBt6PM2h27fZ40ogfJ%2B4NXQ8w1HhfWnR%2FQybMyKaFo9cLVt9FfIUNTMI%2BwGUmq4CeTBcvFa%2FTtCr2VhG9K8WivZPqClKSXx4SuLpV%2BdNwH3J%2BctEtZsXoWlYUPUuXbI9OKFEJ7liW9Q1agnNMZHVHb6Mvu3njqSLowgiBQaslf364RFmYqIMEU%2F%2FKrBt9%2BYj90wR0W7Gcv58UlaalvVCUgajFaWBAhQF2%2FZIf9PVhF4vJH%2F9G9GZPcS82%2FtwrsA00n58eLO1%2B%2FoGtBPBih5Te%2B2gfM62RiU7spp4DycIgE5pQj3cyWCRMimoB8Gb72MOUvdK9iqxla0muAWb6mpml1q4qNCsb64xXxdYlFN%2B6sYxhoFqFsdDqDWtBgcaQ7NR18neCgmAdx44oXr%2Fizuj4MA0ELzgHOWZrzAhdZRJI6iXj7wcf9ax3vlAl5iZMucZScgRQa5G0pMJuck70GOqUBd9qcJMVa47NRrXa%2FXVYYd8a3EI9XJiaXooYYX1Ny3xGMfheH%2BK2qzvWzl4RYmJuQC5dqshwZUWlXSLf7gOi1Iic9O2CIH0q5QX8fydPy2HMHRU0Q1IzQ%2F3vnVc%2FizNDzTw50tpLIsUNxSCQC3L8hBOeRQRmeT0O4M4p7qg7aO2r73CkXhSCgqHJ81w7W9HwhyuW6WbBBmRVO87W0lZqOEBJ6Raua&X-Amz-Signature=6276f5e85bdd48ad4f0984da04881b92ffc78eb7bf05cede19f17b5218857201&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X522CI2T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQCsQ6cIlVQK5a2gRVmRRw8Sko%2BCGbafvw1rHqD1D9uJvQIgJqhnbUoZhJY%2FyuY9VDCxQw%2FsUUL9sIE3bPKECBk1%2FkEq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDFFdpecbGmZqyiUCjyrcAwrP%2F0npMCQRh8HZSvHbdyXBc0MSh%2FJx21bEMO24hyu5Qh6%2FNMOlUMKS0hpWMdj2TWZQx121h8LKybzDUvsKjoKNq2ZLUEyotP%2FsKKJtvP%2B1axBUu3jVw4aajI5BfKrsHZKShwZSYofKExm8CFV%2Bed8GeDvunLq%2BtlOwdkFm6rSFUgnhcbmDGddyxawTAvqoU3XSqXyrnVPdY4Ds0gg0boKT8N9NsbjcSizLrUGqUQRYTSlBKNtmlPyr4US5tdXHjGiUi3p7wvACq2jnq2fr02ZT%2BuG6GK5dV2pPkuUk1uLxJW6KHY%2FtGcYsuiuUJCpM3YpXZa2yw4Bp3h1xfI9IYVmK67Ryuq5lgtHLzpcAUMIL0EauYh99UDkUyUspNsgxHmiIPOTRGwu8AH%2FBMadttMIwbcekrFY3F%2BDRnJgegTKc%2BTtRQz3gTTRDrP4ePMmro6nWTckfyPhLUKhOfgGBjv5zf%2FlfW1g%2BFY97RINU2gir2%2ForsX3J%2F2aApmAIRDvw0mBQYMCoFEKpU6BuEXLDWsj4xT%2Bec%2Ffdqq3qGMvON24V2eOG7FzfAegjActLeCdyABnYmj06e8Uoi%2FV%2FO%2B6rOl3vc5J56TtMf%2FOEVYA6EjufhkfMMF%2Fs3Ewx0ixCMLuck70GOqUBwFEDvkEb1bNgrIHMV5DyANz8lGocdsk3wUeLqLMHt1y4u7VYylkESBiIifhSZrovO%2FmOLm558BclM0xYPtCjkHh22vmnDgYwfoG1Xzcp2YjJpgYuk2CM49G8iao0OFgd83FzHvFqNSmTE9FAhICVFE9ZdueaSkIHP4ZumK0rBunqdMGpTuFu1drobVsCcvFdT7N0Ig3pUA%2BIvDxrPsP%2FxOpCU%2BEu&X-Amz-Signature=24da05103ceb8960f4b214282afa94142c97d59b15520396aa0d347ec589cd16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X522CI2T%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQCsQ6cIlVQK5a2gRVmRRw8Sko%2BCGbafvw1rHqD1D9uJvQIgJqhnbUoZhJY%2FyuY9VDCxQw%2FsUUL9sIE3bPKECBk1%2FkEq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDFFdpecbGmZqyiUCjyrcAwrP%2F0npMCQRh8HZSvHbdyXBc0MSh%2FJx21bEMO24hyu5Qh6%2FNMOlUMKS0hpWMdj2TWZQx121h8LKybzDUvsKjoKNq2ZLUEyotP%2FsKKJtvP%2B1axBUu3jVw4aajI5BfKrsHZKShwZSYofKExm8CFV%2Bed8GeDvunLq%2BtlOwdkFm6rSFUgnhcbmDGddyxawTAvqoU3XSqXyrnVPdY4Ds0gg0boKT8N9NsbjcSizLrUGqUQRYTSlBKNtmlPyr4US5tdXHjGiUi3p7wvACq2jnq2fr02ZT%2BuG6GK5dV2pPkuUk1uLxJW6KHY%2FtGcYsuiuUJCpM3YpXZa2yw4Bp3h1xfI9IYVmK67Ryuq5lgtHLzpcAUMIL0EauYh99UDkUyUspNsgxHmiIPOTRGwu8AH%2FBMadttMIwbcekrFY3F%2BDRnJgegTKc%2BTtRQz3gTTRDrP4ePMmro6nWTckfyPhLUKhOfgGBjv5zf%2FlfW1g%2BFY97RINU2gir2%2ForsX3J%2F2aApmAIRDvw0mBQYMCoFEKpU6BuEXLDWsj4xT%2Bec%2Ffdqq3qGMvON24V2eOG7FzfAegjActLeCdyABnYmj06e8Uoi%2FV%2FO%2B6rOl3vc5J56TtMf%2FOEVYA6EjufhkfMMF%2Fs3Ewx0ixCMLuck70GOqUBwFEDvkEb1bNgrIHMV5DyANz8lGocdsk3wUeLqLMHt1y4u7VYylkESBiIifhSZrovO%2FmOLm558BclM0xYPtCjkHh22vmnDgYwfoG1Xzcp2YjJpgYuk2CM49G8iao0OFgd83FzHvFqNSmTE9FAhICVFE9ZdueaSkIHP4ZumK0rBunqdMGpTuFu1drobVsCcvFdT7N0Ig3pUA%2BIvDxrPsP%2FxOpCU%2BEu&X-Amz-Signature=37104306df41722289e00debddc71f6516acf71c6123890a85fdd1436fa54c83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
