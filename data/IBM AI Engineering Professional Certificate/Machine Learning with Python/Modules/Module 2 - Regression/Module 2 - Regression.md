

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5OKR4B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIBIy%2BshMRgMw2b1adCzaoFBboVzrAsERY8xtESEYLh41AiEAmj2oo0pue%2BREuECTr0w9hoAk%2Btsbszly%2BpgaaHbt1lEq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDO717Qq5UI2VxC4pHircA5KdDpMXKfAVkQgPPsgzK3Kec0lCnOW1ceBsWvXcCR%2BDyEQLtP8JE5AFsCjQPbiZtSDpbW8NRpGSxpEPLcbrny%2F8E707j486YXg6eqMOW03Nrgp9q0Ns9ORQ2TLoAN7a0QNl1gR%2BWaWG%2FE5SyLx8MHGEvbTjpXSVXt8W7PZCiApPmmF8fob4v4%2BW33vxT65gmfHGi8%2FiK7tpvkhg1nPr0mOOx0aswdbUW54S8mbu04r2Q0tGEtthWqZ0boyGaTuiXMFe0rtEGPmcEVY751yjnjRjeTBj2bVB%2Bq1MSekDothOON9Pjhk1UjA4nZA%2B3gg2QCmbE9hI0MoL8K0WTrmyhMIK%2FVWkEc%2FdN9%2Bl5xApsCgxDKgUe8PB8PBWuc%2FUKfZFtXo%2FeSBRvNezmnok9Ru9Wcz04Mk8pAVdQbaCnajo1Wr1n40x%2Fx%2Fm6ejZhwRBIQgr5f4%2FSCTEraj118Z0vlohGXAWyWxC7tMf4FIzZ1G38L3Jmn8IoqWfGyVIN30jZkw5mTjLVY3WCTTCrewwsuwxeiAhclwn1W%2FeVsQXVbPDx8dwyODgpzBea4%2BTNBDb7%2BkhzyE7kZSc9rSSekdFFizKpGt%2FQnAjGuf9XI1vgsLDWEUWIBWJf9eK4hUWypZwMJydjr0GOqUBXp0qJ74bAkrFFUMSZeZhz73Da%2BkMUDYvONBQIK3zrBOzJIhYq38pCPuhtv6DUXo5cQijKRDzxUECF2uvwDsqOmcRdu1poG4kxobJ6COnbXjmNhdp0zRovoPKtA9m04GXKfsOhXo8YTBCWdGHBqh733L95Af%2FUmKsrtzeALjoJ%2FjS%2Bi7jxSrHw0kx29pV9YgX8aLXjGcT992zv0YOJkTSoT0cnsN%2F&X-Amz-Signature=e4e77a8b9ce66b776743047cf7cd7dc1bf0ff5ea9d5be3701bc00235a8e606f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5OKR4B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIBIy%2BshMRgMw2b1adCzaoFBboVzrAsERY8xtESEYLh41AiEAmj2oo0pue%2BREuECTr0w9hoAk%2Btsbszly%2BpgaaHbt1lEq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDO717Qq5UI2VxC4pHircA5KdDpMXKfAVkQgPPsgzK3Kec0lCnOW1ceBsWvXcCR%2BDyEQLtP8JE5AFsCjQPbiZtSDpbW8NRpGSxpEPLcbrny%2F8E707j486YXg6eqMOW03Nrgp9q0Ns9ORQ2TLoAN7a0QNl1gR%2BWaWG%2FE5SyLx8MHGEvbTjpXSVXt8W7PZCiApPmmF8fob4v4%2BW33vxT65gmfHGi8%2FiK7tpvkhg1nPr0mOOx0aswdbUW54S8mbu04r2Q0tGEtthWqZ0boyGaTuiXMFe0rtEGPmcEVY751yjnjRjeTBj2bVB%2Bq1MSekDothOON9Pjhk1UjA4nZA%2B3gg2QCmbE9hI0MoL8K0WTrmyhMIK%2FVWkEc%2FdN9%2Bl5xApsCgxDKgUe8PB8PBWuc%2FUKfZFtXo%2FeSBRvNezmnok9Ru9Wcz04Mk8pAVdQbaCnajo1Wr1n40x%2Fx%2Fm6ejZhwRBIQgr5f4%2FSCTEraj118Z0vlohGXAWyWxC7tMf4FIzZ1G38L3Jmn8IoqWfGyVIN30jZkw5mTjLVY3WCTTCrewwsuwxeiAhclwn1W%2FeVsQXVbPDx8dwyODgpzBea4%2BTNBDb7%2BkhzyE7kZSc9rSSekdFFizKpGt%2FQnAjGuf9XI1vgsLDWEUWIBWJf9eK4hUWypZwMJydjr0GOqUBXp0qJ74bAkrFFUMSZeZhz73Da%2BkMUDYvONBQIK3zrBOzJIhYq38pCPuhtv6DUXo5cQijKRDzxUECF2uvwDsqOmcRdu1poG4kxobJ6COnbXjmNhdp0zRovoPKtA9m04GXKfsOhXo8YTBCWdGHBqh733L95Af%2FUmKsrtzeALjoJ%2FjS%2Bi7jxSrHw0kx29pV9YgX8aLXjGcT992zv0YOJkTSoT0cnsN%2F&X-Amz-Signature=bd21213bc363b0bc101dfb5b4e8dc5b27bc655c9c59356791fee50d2c2b93240&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5OKR4B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIBIy%2BshMRgMw2b1adCzaoFBboVzrAsERY8xtESEYLh41AiEAmj2oo0pue%2BREuECTr0w9hoAk%2Btsbszly%2BpgaaHbt1lEq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDO717Qq5UI2VxC4pHircA5KdDpMXKfAVkQgPPsgzK3Kec0lCnOW1ceBsWvXcCR%2BDyEQLtP8JE5AFsCjQPbiZtSDpbW8NRpGSxpEPLcbrny%2F8E707j486YXg6eqMOW03Nrgp9q0Ns9ORQ2TLoAN7a0QNl1gR%2BWaWG%2FE5SyLx8MHGEvbTjpXSVXt8W7PZCiApPmmF8fob4v4%2BW33vxT65gmfHGi8%2FiK7tpvkhg1nPr0mOOx0aswdbUW54S8mbu04r2Q0tGEtthWqZ0boyGaTuiXMFe0rtEGPmcEVY751yjnjRjeTBj2bVB%2Bq1MSekDothOON9Pjhk1UjA4nZA%2B3gg2QCmbE9hI0MoL8K0WTrmyhMIK%2FVWkEc%2FdN9%2Bl5xApsCgxDKgUe8PB8PBWuc%2FUKfZFtXo%2FeSBRvNezmnok9Ru9Wcz04Mk8pAVdQbaCnajo1Wr1n40x%2Fx%2Fm6ejZhwRBIQgr5f4%2FSCTEraj118Z0vlohGXAWyWxC7tMf4FIzZ1G38L3Jmn8IoqWfGyVIN30jZkw5mTjLVY3WCTTCrewwsuwxeiAhclwn1W%2FeVsQXVbPDx8dwyODgpzBea4%2BTNBDb7%2BkhzyE7kZSc9rSSekdFFizKpGt%2FQnAjGuf9XI1vgsLDWEUWIBWJf9eK4hUWypZwMJydjr0GOqUBXp0qJ74bAkrFFUMSZeZhz73Da%2BkMUDYvONBQIK3zrBOzJIhYq38pCPuhtv6DUXo5cQijKRDzxUECF2uvwDsqOmcRdu1poG4kxobJ6COnbXjmNhdp0zRovoPKtA9m04GXKfsOhXo8YTBCWdGHBqh733L95Af%2FUmKsrtzeALjoJ%2FjS%2Bi7jxSrHw0kx29pV9YgX8aLXjGcT992zv0YOJkTSoT0cnsN%2F&X-Amz-Signature=bf4f90f0512550fdd5e8e948e252b3bc2c389ca12308d127bfaa4390152b2398&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5OKR4B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIBIy%2BshMRgMw2b1adCzaoFBboVzrAsERY8xtESEYLh41AiEAmj2oo0pue%2BREuECTr0w9hoAk%2Btsbszly%2BpgaaHbt1lEq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDO717Qq5UI2VxC4pHircA5KdDpMXKfAVkQgPPsgzK3Kec0lCnOW1ceBsWvXcCR%2BDyEQLtP8JE5AFsCjQPbiZtSDpbW8NRpGSxpEPLcbrny%2F8E707j486YXg6eqMOW03Nrgp9q0Ns9ORQ2TLoAN7a0QNl1gR%2BWaWG%2FE5SyLx8MHGEvbTjpXSVXt8W7PZCiApPmmF8fob4v4%2BW33vxT65gmfHGi8%2FiK7tpvkhg1nPr0mOOx0aswdbUW54S8mbu04r2Q0tGEtthWqZ0boyGaTuiXMFe0rtEGPmcEVY751yjnjRjeTBj2bVB%2Bq1MSekDothOON9Pjhk1UjA4nZA%2B3gg2QCmbE9hI0MoL8K0WTrmyhMIK%2FVWkEc%2FdN9%2Bl5xApsCgxDKgUe8PB8PBWuc%2FUKfZFtXo%2FeSBRvNezmnok9Ru9Wcz04Mk8pAVdQbaCnajo1Wr1n40x%2Fx%2Fm6ejZhwRBIQgr5f4%2FSCTEraj118Z0vlohGXAWyWxC7tMf4FIzZ1G38L3Jmn8IoqWfGyVIN30jZkw5mTjLVY3WCTTCrewwsuwxeiAhclwn1W%2FeVsQXVbPDx8dwyODgpzBea4%2BTNBDb7%2BkhzyE7kZSc9rSSekdFFizKpGt%2FQnAjGuf9XI1vgsLDWEUWIBWJf9eK4hUWypZwMJydjr0GOqUBXp0qJ74bAkrFFUMSZeZhz73Da%2BkMUDYvONBQIK3zrBOzJIhYq38pCPuhtv6DUXo5cQijKRDzxUECF2uvwDsqOmcRdu1poG4kxobJ6COnbXjmNhdp0zRovoPKtA9m04GXKfsOhXo8YTBCWdGHBqh733L95Af%2FUmKsrtzeALjoJ%2FjS%2Bi7jxSrHw0kx29pV9YgX8aLXjGcT992zv0YOJkTSoT0cnsN%2F&X-Amz-Signature=bc360b5d66add758bfc5b056094c3a2aa8571b4d0c108d72cd9eb488cce5e3af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5OKR4B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIBIy%2BshMRgMw2b1adCzaoFBboVzrAsERY8xtESEYLh41AiEAmj2oo0pue%2BREuECTr0w9hoAk%2Btsbszly%2BpgaaHbt1lEq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDO717Qq5UI2VxC4pHircA5KdDpMXKfAVkQgPPsgzK3Kec0lCnOW1ceBsWvXcCR%2BDyEQLtP8JE5AFsCjQPbiZtSDpbW8NRpGSxpEPLcbrny%2F8E707j486YXg6eqMOW03Nrgp9q0Ns9ORQ2TLoAN7a0QNl1gR%2BWaWG%2FE5SyLx8MHGEvbTjpXSVXt8W7PZCiApPmmF8fob4v4%2BW33vxT65gmfHGi8%2FiK7tpvkhg1nPr0mOOx0aswdbUW54S8mbu04r2Q0tGEtthWqZ0boyGaTuiXMFe0rtEGPmcEVY751yjnjRjeTBj2bVB%2Bq1MSekDothOON9Pjhk1UjA4nZA%2B3gg2QCmbE9hI0MoL8K0WTrmyhMIK%2FVWkEc%2FdN9%2Bl5xApsCgxDKgUe8PB8PBWuc%2FUKfZFtXo%2FeSBRvNezmnok9Ru9Wcz04Mk8pAVdQbaCnajo1Wr1n40x%2Fx%2Fm6ejZhwRBIQgr5f4%2FSCTEraj118Z0vlohGXAWyWxC7tMf4FIzZ1G38L3Jmn8IoqWfGyVIN30jZkw5mTjLVY3WCTTCrewwsuwxeiAhclwn1W%2FeVsQXVbPDx8dwyODgpzBea4%2BTNBDb7%2BkhzyE7kZSc9rSSekdFFizKpGt%2FQnAjGuf9XI1vgsLDWEUWIBWJf9eK4hUWypZwMJydjr0GOqUBXp0qJ74bAkrFFUMSZeZhz73Da%2BkMUDYvONBQIK3zrBOzJIhYq38pCPuhtv6DUXo5cQijKRDzxUECF2uvwDsqOmcRdu1poG4kxobJ6COnbXjmNhdp0zRovoPKtA9m04GXKfsOhXo8YTBCWdGHBqh733L95Af%2FUmKsrtzeALjoJ%2FjS%2Bi7jxSrHw0kx29pV9YgX8aLXjGcT992zv0YOJkTSoT0cnsN%2F&X-Amz-Signature=d7d22db1b72435fa361492e4ab9a045dce98cbf6606d8e57eed93297f20b2aa3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5OKR4B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIBIy%2BshMRgMw2b1adCzaoFBboVzrAsERY8xtESEYLh41AiEAmj2oo0pue%2BREuECTr0w9hoAk%2Btsbszly%2BpgaaHbt1lEq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDO717Qq5UI2VxC4pHircA5KdDpMXKfAVkQgPPsgzK3Kec0lCnOW1ceBsWvXcCR%2BDyEQLtP8JE5AFsCjQPbiZtSDpbW8NRpGSxpEPLcbrny%2F8E707j486YXg6eqMOW03Nrgp9q0Ns9ORQ2TLoAN7a0QNl1gR%2BWaWG%2FE5SyLx8MHGEvbTjpXSVXt8W7PZCiApPmmF8fob4v4%2BW33vxT65gmfHGi8%2FiK7tpvkhg1nPr0mOOx0aswdbUW54S8mbu04r2Q0tGEtthWqZ0boyGaTuiXMFe0rtEGPmcEVY751yjnjRjeTBj2bVB%2Bq1MSekDothOON9Pjhk1UjA4nZA%2B3gg2QCmbE9hI0MoL8K0WTrmyhMIK%2FVWkEc%2FdN9%2Bl5xApsCgxDKgUe8PB8PBWuc%2FUKfZFtXo%2FeSBRvNezmnok9Ru9Wcz04Mk8pAVdQbaCnajo1Wr1n40x%2Fx%2Fm6ejZhwRBIQgr5f4%2FSCTEraj118Z0vlohGXAWyWxC7tMf4FIzZ1G38L3Jmn8IoqWfGyVIN30jZkw5mTjLVY3WCTTCrewwsuwxeiAhclwn1W%2FeVsQXVbPDx8dwyODgpzBea4%2BTNBDb7%2BkhzyE7kZSc9rSSekdFFizKpGt%2FQnAjGuf9XI1vgsLDWEUWIBWJf9eK4hUWypZwMJydjr0GOqUBXp0qJ74bAkrFFUMSZeZhz73Da%2BkMUDYvONBQIK3zrBOzJIhYq38pCPuhtv6DUXo5cQijKRDzxUECF2uvwDsqOmcRdu1poG4kxobJ6COnbXjmNhdp0zRovoPKtA9m04GXKfsOhXo8YTBCWdGHBqh733L95Af%2FUmKsrtzeALjoJ%2FjS%2Bi7jxSrHw0kx29pV9YgX8aLXjGcT992zv0YOJkTSoT0cnsN%2F&X-Amz-Signature=309915d48baa6a1490a6d913e69acafd8b5bb6311b9dab639cd9fec3e65e9e18&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5OKR4B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIBIy%2BshMRgMw2b1adCzaoFBboVzrAsERY8xtESEYLh41AiEAmj2oo0pue%2BREuECTr0w9hoAk%2Btsbszly%2BpgaaHbt1lEq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDO717Qq5UI2VxC4pHircA5KdDpMXKfAVkQgPPsgzK3Kec0lCnOW1ceBsWvXcCR%2BDyEQLtP8JE5AFsCjQPbiZtSDpbW8NRpGSxpEPLcbrny%2F8E707j486YXg6eqMOW03Nrgp9q0Ns9ORQ2TLoAN7a0QNl1gR%2BWaWG%2FE5SyLx8MHGEvbTjpXSVXt8W7PZCiApPmmF8fob4v4%2BW33vxT65gmfHGi8%2FiK7tpvkhg1nPr0mOOx0aswdbUW54S8mbu04r2Q0tGEtthWqZ0boyGaTuiXMFe0rtEGPmcEVY751yjnjRjeTBj2bVB%2Bq1MSekDothOON9Pjhk1UjA4nZA%2B3gg2QCmbE9hI0MoL8K0WTrmyhMIK%2FVWkEc%2FdN9%2Bl5xApsCgxDKgUe8PB8PBWuc%2FUKfZFtXo%2FeSBRvNezmnok9Ru9Wcz04Mk8pAVdQbaCnajo1Wr1n40x%2Fx%2Fm6ejZhwRBIQgr5f4%2FSCTEraj118Z0vlohGXAWyWxC7tMf4FIzZ1G38L3Jmn8IoqWfGyVIN30jZkw5mTjLVY3WCTTCrewwsuwxeiAhclwn1W%2FeVsQXVbPDx8dwyODgpzBea4%2BTNBDb7%2BkhzyE7kZSc9rSSekdFFizKpGt%2FQnAjGuf9XI1vgsLDWEUWIBWJf9eK4hUWypZwMJydjr0GOqUBXp0qJ74bAkrFFUMSZeZhz73Da%2BkMUDYvONBQIK3zrBOzJIhYq38pCPuhtv6DUXo5cQijKRDzxUECF2uvwDsqOmcRdu1poG4kxobJ6COnbXjmNhdp0zRovoPKtA9m04GXKfsOhXo8YTBCWdGHBqh733L95Af%2FUmKsrtzeALjoJ%2FjS%2Bi7jxSrHw0kx29pV9YgX8aLXjGcT992zv0YOJkTSoT0cnsN%2F&X-Amz-Signature=105331ce6dd75abead2773f8c9a92679a320dcdec0c52a29119d3b8dd2f38fe8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M5OKR4B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIBIy%2BshMRgMw2b1adCzaoFBboVzrAsERY8xtESEYLh41AiEAmj2oo0pue%2BREuECTr0w9hoAk%2Btsbszly%2BpgaaHbt1lEq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDO717Qq5UI2VxC4pHircA5KdDpMXKfAVkQgPPsgzK3Kec0lCnOW1ceBsWvXcCR%2BDyEQLtP8JE5AFsCjQPbiZtSDpbW8NRpGSxpEPLcbrny%2F8E707j486YXg6eqMOW03Nrgp9q0Ns9ORQ2TLoAN7a0QNl1gR%2BWaWG%2FE5SyLx8MHGEvbTjpXSVXt8W7PZCiApPmmF8fob4v4%2BW33vxT65gmfHGi8%2FiK7tpvkhg1nPr0mOOx0aswdbUW54S8mbu04r2Q0tGEtthWqZ0boyGaTuiXMFe0rtEGPmcEVY751yjnjRjeTBj2bVB%2Bq1MSekDothOON9Pjhk1UjA4nZA%2B3gg2QCmbE9hI0MoL8K0WTrmyhMIK%2FVWkEc%2FdN9%2Bl5xApsCgxDKgUe8PB8PBWuc%2FUKfZFtXo%2FeSBRvNezmnok9Ru9Wcz04Mk8pAVdQbaCnajo1Wr1n40x%2Fx%2Fm6ejZhwRBIQgr5f4%2FSCTEraj118Z0vlohGXAWyWxC7tMf4FIzZ1G38L3Jmn8IoqWfGyVIN30jZkw5mTjLVY3WCTTCrewwsuwxeiAhclwn1W%2FeVsQXVbPDx8dwyODgpzBea4%2BTNBDb7%2BkhzyE7kZSc9rSSekdFFizKpGt%2FQnAjGuf9XI1vgsLDWEUWIBWJf9eK4hUWypZwMJydjr0GOqUBXp0qJ74bAkrFFUMSZeZhz73Da%2BkMUDYvONBQIK3zrBOzJIhYq38pCPuhtv6DUXo5cQijKRDzxUECF2uvwDsqOmcRdu1poG4kxobJ6COnbXjmNhdp0zRovoPKtA9m04GXKfsOhXo8YTBCWdGHBqh733L95Af%2FUmKsrtzeALjoJ%2FjS%2Bi7jxSrHw0kx29pV9YgX8aLXjGcT992zv0YOJkTSoT0cnsN%2F&X-Amz-Signature=52e01fcd81682cc994d7e6065ef754d77aca04952230071aedb7c9fe931f49c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625KJPGVC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIAkJjpIILdZAWLAJf5S1Exp72iV9lQ29x3%2BIZSDkjQtdAiAzlMKJg0WO1Z8KqaZFfZ9kD7HBGWKFVtW3NGJe8AZrUSr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMMzMD9iPINSUkYcyfKtwDdeQidIel1UJQnqRpNEAyfcxqjP%2BzTEip4g656XTzoPNz4Qx5yBVLD0dcxcJg9UtFEyGEQwroH4CeNOWn7J8%2F1YM8BvUIZLPFlmN3r3WSI4knLzekiloGB0NrCB0IVtdm8P%2Fj4a0%2BVafoOU5B49dPEFIZgN227mHNlahtoJNhWRCCMl%2FswlDWElE7%2FvX%2F%2BsBVdlzPqq30ZgxJ59b2B2M%2FFPu0aiLoVf7DbrWkKMw1TUl0zLsVAfF1s%2BfD%2BAIlyPGz3UNMMpamS4qn%2FlHou3qzVXnjBNZtdKXiP7FHAI8Yse21WNEzSIZhSjJ7Ioh6CB2WJFI91kG3nAYUOuaHhTlTGDdb7ZgOjBnQGacGfTw%2BXCbhkjeFk1so4WowOpTugGtzgY2oN7Y%2BBpXYiScmawov6UvUvU4ZQcWDhrBFe%2Fqv%2B5M3TVAGpB91bG598F%2BWoSIZgMiITAD9OsfPvxibrQBn4gEzFfE5RuG6GvwYOc%2BmFbY1kXrBLXbvsoU7XjLLEsAsB0bFRNHvaQnlhtVIAgwOv0kDEz6trDRqaPhSr9rZ5S07vbSXwaWA9dxP3C6ag6Xg4wonD%2BM1gLykAfBWyTyxWBj%2FGzGW2weijD%2BuUR514IHvqMmFRjkJoQGOOYQwwZ2OvQY6pgGrmf7kCgr98vsdQ8NCEXo7NSLvH53g0Y6h%2F6CmVe5OT%2BwCDUP9XK3j9Jt9d7fzD0mc01rWypF%2B8R6yJZL%2B%2FiS7eNqImCYVMRdAncku6%2Fax2PmRx5nah4ldR9YDfcCcnqzBCHQGPsHJS9PysP3aS1Uz22WPuXm6wnMhpkmqJhfGPWOgxvBKtdAY4aTefXtaG9Hl9DGJ5Bj91epyK1fhr0PB6vkDrJ7g&X-Amz-Signature=e71a6b2b74a1758a4a1497e4515b1822734bae44de8563d867391847b81a6920&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FUGRTKB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQDMHaOZzosUsPQ4McMIAj9LfOlXDTZSzRpdUEXA%2FGdOOgIhAO8tpw1QUw3MZsBvP7aVdCQLCt6VSE5hAHDrAaZg0hd7Kv8DCEkQABoMNjM3NDIzMTgzODA1IgyRj%2FOmAnd07s0Cft8q3AO%2B3TcnfD8h5Gna9dCzd5072uPc7kY8Dj1Vw%2FfZoP3a8AOTaWiCj0jl%2FzeoSHwe9trGaGS2WlooHknlgQEvW4Q61GKIrg13idIjJ%2BxP5upRgh%2B2bCnq2a9FULMutfWxP9IPirAlB6y8Fh3wwFxVlMgC4CEqtMb60gQrVLqqOwUX2lZMnshSgqYQ8JnxKiK4N9HuS4r1nE94LVPSebVfMe6qnhQgrbZBKfev5sPSQ7ppSRWVAmdE4vFpyrkM3ronZwd8BXnxMZuS3CDa6oKwQWgpP%2FEuLNss6QhKQrMNE1FUuclhQs%2FBsg1NXaK404m6oP3zCKHhSv%2Ff%2Bbx%2F7oYFyjr3ZqunDSrTHCIOUj9CXoagsKScqMaDe7BS8PdqUrXKnLXaytI%2FK3TlDJn2FLSt6qqmi0BYmUimi9IORnHNr5eO3rlbx%2FVKZCP9gN%2F1b9enAYcp18ZpE2QlSLBLLW8uKUQGGX24OcKNdjbZkQQGa5RBYPkm311HnOioNAkJgbnv5Wvct1LwZ2jlT96tO8R7ZiZ45Y6V56RmaCmvztxiDssNlDYxtTE2cjyIjT%2BIeY80K95vjJQWBM5bKAYu0ZoBnmcf0%2FGD7ikANYIMjDkNuOuzPK%2FL0Fq2pC05duIImzD0nY69BjqkASc1MrPScseSnlMXaxrrngDfBPRbclkBfQZLBV8IRFMxoFXdFjSfFaqyRYXN96vowI8E0vwEihOTjYBB1wLn0yeMWKFV%2FmGySkGQnmf6gTkTarVH3neLWQuzfJTEZj3U%2Fvx6iBBB9wu67TsRy0denHxExRqqOr%2FDob85icRv0257pGHdWR6oKCMn2AcIFpEmuaFlhRNgOwU0PtZFUbH3wG%2F1UuBv&X-Amz-Signature=bda2086194628412341f7efb0702b3e08f456c54d39cebe2d97f02870a4b6f50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XU6TRGHR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCK9b1SjSMjz0xAIlNFko0MFL2FtiMD0rLklIg1llM%2B8gIhAIlwG7M8R8rjJqKKuyxWugipckJnZcQDnAx2APdZgSaUKv8DCEkQABoMNjM3NDIzMTgzODA1IgzglVIhicpH3zOV5cIq3APLQCF3slq5e6h9%2FM7YbcOthSOPR9TMBIZreTgZ0Y1uILRg4xKMxtP%2BV%2FwV%2BKkFk%2FGBf%2BQwAcXe%2FyNpZedAoWLhWIkWa3IsEn%2Bxyu5LMn6N6x4Lo8bX0EkpOVuXDVRO%2FccV1Nf5Vn7ptgk%2B%2FonSf4ORNC06Gcw3DEfpQFrbziUHg9wPlgoaH3gtVktqAGqTnrGKcfFPVJ47jGCjpuAhEhRc7KFnVWiH6zdkK1p0aoJHrBsxyk5rCzz5nIl7TzDVRRC0DX7EqhVNKgatb9P4aUnLkv01CD8apb82TMzXiasfB3DZ9swdlxkGAEz6Bq0CgcCHVEVIC4ljSuHn5cv%2BaNjzokuZv5TI420sLOq81FRclC21o0f32qDF%2B6iqCsxpFqZc77su5Ck9mWqVsfp2nsADF4s8CTwJVpv%2F4wRJWlvnu79mXFhQvTJJ6f2IfTRD%2FY5bg4j1a886kDSksfz1kYlORMoIi3KZnmw3hAjRD7xg9XAeLP3oFE%2B%2FPzdeMs%2FCEGWO2YJbkbb10eEkGzg4QV8rG%2F2N7jlU0s16f5GJJQj1Ul87veZgLr8fNi4VdrefZjvUUR2xLrf7E%2Ft3pqqDNcv3aw%2F4NdV7t5J%2BUGTjlDitQf6znUGJFYWbGwLuyTD2nY69BjqkAZdQfXMmgfDB%2FirDHT06H1GlGz08Nto2nXoY37g9xmhzwvL1PCNMgnlQxW8x%2F1bIAqppo41VigeNHIxyZWGZl78v50c0tCPFP73F%2BGlnle9VzNHdqapz1%2BRfcxHKcA2awc%2FaMNSb%2B%2B74ojvLOpycmEwGglabRcN%2FMpsoUPy%2Bukth24y%2BvowPHtJ2csqzky%2BtD4bm6cPsHpuX0m%2Bg2GyXhxQU%2F49M&X-Amz-Signature=14b2c593748c6e92b4db5b8c2d39d33d4a9311c9758ae01b54f184290044cd55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XU6TRGHR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCK9b1SjSMjz0xAIlNFko0MFL2FtiMD0rLklIg1llM%2B8gIhAIlwG7M8R8rjJqKKuyxWugipckJnZcQDnAx2APdZgSaUKv8DCEkQABoMNjM3NDIzMTgzODA1IgzglVIhicpH3zOV5cIq3APLQCF3slq5e6h9%2FM7YbcOthSOPR9TMBIZreTgZ0Y1uILRg4xKMxtP%2BV%2FwV%2BKkFk%2FGBf%2BQwAcXe%2FyNpZedAoWLhWIkWa3IsEn%2Bxyu5LMn6N6x4Lo8bX0EkpOVuXDVRO%2FccV1Nf5Vn7ptgk%2B%2FonSf4ORNC06Gcw3DEfpQFrbziUHg9wPlgoaH3gtVktqAGqTnrGKcfFPVJ47jGCjpuAhEhRc7KFnVWiH6zdkK1p0aoJHrBsxyk5rCzz5nIl7TzDVRRC0DX7EqhVNKgatb9P4aUnLkv01CD8apb82TMzXiasfB3DZ9swdlxkGAEz6Bq0CgcCHVEVIC4ljSuHn5cv%2BaNjzokuZv5TI420sLOq81FRclC21o0f32qDF%2B6iqCsxpFqZc77su5Ck9mWqVsfp2nsADF4s8CTwJVpv%2F4wRJWlvnu79mXFhQvTJJ6f2IfTRD%2FY5bg4j1a886kDSksfz1kYlORMoIi3KZnmw3hAjRD7xg9XAeLP3oFE%2B%2FPzdeMs%2FCEGWO2YJbkbb10eEkGzg4QV8rG%2F2N7jlU0s16f5GJJQj1Ul87veZgLr8fNi4VdrefZjvUUR2xLrf7E%2Ft3pqqDNcv3aw%2F4NdV7t5J%2BUGTjlDitQf6znUGJFYWbGwLuyTD2nY69BjqkAZdQfXMmgfDB%2FirDHT06H1GlGz08Nto2nXoY37g9xmhzwvL1PCNMgnlQxW8x%2F1bIAqppo41VigeNHIxyZWGZl78v50c0tCPFP73F%2BGlnle9VzNHdqapz1%2BRfcxHKcA2awc%2FaMNSb%2B%2B74ojvLOpycmEwGglabRcN%2FMpsoUPy%2Bukth24y%2BvowPHtJ2csqzky%2BtD4bm6cPsHpuX0m%2Bg2GyXhxQU%2F49M&X-Amz-Signature=5055c15a93cf606276b9a9d19abee9e699fa45aef02a10f1c6e356c9147597e5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
