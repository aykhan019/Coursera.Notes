

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YPGYDM6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDB%2BxPXQxXGrEYixSdtAA69V6wyiNHaeohMRjdct%2FR6fAiBoty47bgPf0PBFl0tZA2wuiXvIAnCuk7tVSeEZmsqCnSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVIMtNdG3FxmGDL3sKtwDkbGH1Z58IQjFDkj45Iv25fuodLyYnbTZshF2V81%2BGCgapRuGQtq6udcXWu%2BrMcHIlGe632SMa69EYPACH5hLLWII%2BQPoiIy0uuRLqPkTCC3XFFSZSwX3ZBqAivAP%2F5R3Is4fMfhlUtC6To3YeqMVPS%2BbJHCggpA2EICsphyEMWme9egO5hGBcFMrGhZggPatCO%2FEGgIP9BJW%2BP8czBcsuBlL13Ds%2B1HoIYCYUIgHfNtVdFtrBX6vltEjIrjMYMCxStsMHEh09hS7ogJi2mckbd9GSU9dVTjlnAodaTJTTB%2BAiEDfHHs7qkd9S6p7TB49YQFF51GWnM%2B5rD9mkTkXGhbro8DFHvJgGHbJaUcZ9ClPm%2FGIes93bvavKYfn1mNCUM6iW0UkWYO9Y7sLojjROYyqrzpG5Ga149duna0yC6EPlG6PMWoyh2KWcjj6hsber1OEUQRtTkQ2nsj2xldLqv1x9d%2FQizUq0vFs56NYzOsEbBKEzayWBXH2LITvTV1%2Fme0bCML8mhNAsHckNR6XeyTyVbM2jxyeekhVRiR%2Fc%2F11mzEctlfk0Ni3R1i51AdsdVlFjd3eEeTOzqkE8%2FZeaR0yFu6ADHyMgMq8wDxhYMen8A%2BKfEKRSz3HxOEw%2BfH6vAY6pgEV19huVumElKCiLIq%2BANcX3qyCVEOx%2B8HY1N6x8sp%2F%2FgXP%2F8BewjZM8DUOqQWYJFsC5E%2Fyc754NG%2BczBZ%2FIqe4H%2Bd0wtPh8cofTueIYTNNl5yvr6CKsRjQG%2FRT%2BkHogtrO0HdpW98zyT5o1Kv%2BUfvvNU%2BOi%2Bd6%2Fr9K5iAIdPcHqkDKRhIQCPKVUW%2BJi5clP4RYWx2lExLli76G8rcFlemVZyEy6QrX&X-Amz-Signature=2d28ebcdbf128a431acb1e096d1b6987be11f1aa3b8ca2bfe146ecfd957ae20b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YPGYDM6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDB%2BxPXQxXGrEYixSdtAA69V6wyiNHaeohMRjdct%2FR6fAiBoty47bgPf0PBFl0tZA2wuiXvIAnCuk7tVSeEZmsqCnSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVIMtNdG3FxmGDL3sKtwDkbGH1Z58IQjFDkj45Iv25fuodLyYnbTZshF2V81%2BGCgapRuGQtq6udcXWu%2BrMcHIlGe632SMa69EYPACH5hLLWII%2BQPoiIy0uuRLqPkTCC3XFFSZSwX3ZBqAivAP%2F5R3Is4fMfhlUtC6To3YeqMVPS%2BbJHCggpA2EICsphyEMWme9egO5hGBcFMrGhZggPatCO%2FEGgIP9BJW%2BP8czBcsuBlL13Ds%2B1HoIYCYUIgHfNtVdFtrBX6vltEjIrjMYMCxStsMHEh09hS7ogJi2mckbd9GSU9dVTjlnAodaTJTTB%2BAiEDfHHs7qkd9S6p7TB49YQFF51GWnM%2B5rD9mkTkXGhbro8DFHvJgGHbJaUcZ9ClPm%2FGIes93bvavKYfn1mNCUM6iW0UkWYO9Y7sLojjROYyqrzpG5Ga149duna0yC6EPlG6PMWoyh2KWcjj6hsber1OEUQRtTkQ2nsj2xldLqv1x9d%2FQizUq0vFs56NYzOsEbBKEzayWBXH2LITvTV1%2Fme0bCML8mhNAsHckNR6XeyTyVbM2jxyeekhVRiR%2Fc%2F11mzEctlfk0Ni3R1i51AdsdVlFjd3eEeTOzqkE8%2FZeaR0yFu6ADHyMgMq8wDxhYMen8A%2BKfEKRSz3HxOEw%2BfH6vAY6pgEV19huVumElKCiLIq%2BANcX3qyCVEOx%2B8HY1N6x8sp%2F%2FgXP%2F8BewjZM8DUOqQWYJFsC5E%2Fyc754NG%2BczBZ%2FIqe4H%2Bd0wtPh8cofTueIYTNNl5yvr6CKsRjQG%2FRT%2BkHogtrO0HdpW98zyT5o1Kv%2BUfvvNU%2BOi%2Bd6%2Fr9K5iAIdPcHqkDKRhIQCPKVUW%2BJi5clP4RYWx2lExLli76G8rcFlemVZyEy6QrX&X-Amz-Signature=ea288dda0de040a4b5438b75d8e529fff40872655bdcda544efb2c28a27e8d08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YPGYDM6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDB%2BxPXQxXGrEYixSdtAA69V6wyiNHaeohMRjdct%2FR6fAiBoty47bgPf0PBFl0tZA2wuiXvIAnCuk7tVSeEZmsqCnSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVIMtNdG3FxmGDL3sKtwDkbGH1Z58IQjFDkj45Iv25fuodLyYnbTZshF2V81%2BGCgapRuGQtq6udcXWu%2BrMcHIlGe632SMa69EYPACH5hLLWII%2BQPoiIy0uuRLqPkTCC3XFFSZSwX3ZBqAivAP%2F5R3Is4fMfhlUtC6To3YeqMVPS%2BbJHCggpA2EICsphyEMWme9egO5hGBcFMrGhZggPatCO%2FEGgIP9BJW%2BP8czBcsuBlL13Ds%2B1HoIYCYUIgHfNtVdFtrBX6vltEjIrjMYMCxStsMHEh09hS7ogJi2mckbd9GSU9dVTjlnAodaTJTTB%2BAiEDfHHs7qkd9S6p7TB49YQFF51GWnM%2B5rD9mkTkXGhbro8DFHvJgGHbJaUcZ9ClPm%2FGIes93bvavKYfn1mNCUM6iW0UkWYO9Y7sLojjROYyqrzpG5Ga149duna0yC6EPlG6PMWoyh2KWcjj6hsber1OEUQRtTkQ2nsj2xldLqv1x9d%2FQizUq0vFs56NYzOsEbBKEzayWBXH2LITvTV1%2Fme0bCML8mhNAsHckNR6XeyTyVbM2jxyeekhVRiR%2Fc%2F11mzEctlfk0Ni3R1i51AdsdVlFjd3eEeTOzqkE8%2FZeaR0yFu6ADHyMgMq8wDxhYMen8A%2BKfEKRSz3HxOEw%2BfH6vAY6pgEV19huVumElKCiLIq%2BANcX3qyCVEOx%2B8HY1N6x8sp%2F%2FgXP%2F8BewjZM8DUOqQWYJFsC5E%2Fyc754NG%2BczBZ%2FIqe4H%2Bd0wtPh8cofTueIYTNNl5yvr6CKsRjQG%2FRT%2BkHogtrO0HdpW98zyT5o1Kv%2BUfvvNU%2BOi%2Bd6%2Fr9K5iAIdPcHqkDKRhIQCPKVUW%2BJi5clP4RYWx2lExLli76G8rcFlemVZyEy6QrX&X-Amz-Signature=65f9c44d83b953e38708d0bd48d5e62347991a2c42fe5b8ab8b40e1554e6e926&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YPGYDM6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDB%2BxPXQxXGrEYixSdtAA69V6wyiNHaeohMRjdct%2FR6fAiBoty47bgPf0PBFl0tZA2wuiXvIAnCuk7tVSeEZmsqCnSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVIMtNdG3FxmGDL3sKtwDkbGH1Z58IQjFDkj45Iv25fuodLyYnbTZshF2V81%2BGCgapRuGQtq6udcXWu%2BrMcHIlGe632SMa69EYPACH5hLLWII%2BQPoiIy0uuRLqPkTCC3XFFSZSwX3ZBqAivAP%2F5R3Is4fMfhlUtC6To3YeqMVPS%2BbJHCggpA2EICsphyEMWme9egO5hGBcFMrGhZggPatCO%2FEGgIP9BJW%2BP8czBcsuBlL13Ds%2B1HoIYCYUIgHfNtVdFtrBX6vltEjIrjMYMCxStsMHEh09hS7ogJi2mckbd9GSU9dVTjlnAodaTJTTB%2BAiEDfHHs7qkd9S6p7TB49YQFF51GWnM%2B5rD9mkTkXGhbro8DFHvJgGHbJaUcZ9ClPm%2FGIes93bvavKYfn1mNCUM6iW0UkWYO9Y7sLojjROYyqrzpG5Ga149duna0yC6EPlG6PMWoyh2KWcjj6hsber1OEUQRtTkQ2nsj2xldLqv1x9d%2FQizUq0vFs56NYzOsEbBKEzayWBXH2LITvTV1%2Fme0bCML8mhNAsHckNR6XeyTyVbM2jxyeekhVRiR%2Fc%2F11mzEctlfk0Ni3R1i51AdsdVlFjd3eEeTOzqkE8%2FZeaR0yFu6ADHyMgMq8wDxhYMen8A%2BKfEKRSz3HxOEw%2BfH6vAY6pgEV19huVumElKCiLIq%2BANcX3qyCVEOx%2B8HY1N6x8sp%2F%2FgXP%2F8BewjZM8DUOqQWYJFsC5E%2Fyc754NG%2BczBZ%2FIqe4H%2Bd0wtPh8cofTueIYTNNl5yvr6CKsRjQG%2FRT%2BkHogtrO0HdpW98zyT5o1Kv%2BUfvvNU%2BOi%2Bd6%2Fr9K5iAIdPcHqkDKRhIQCPKVUW%2BJi5clP4RYWx2lExLli76G8rcFlemVZyEy6QrX&X-Amz-Signature=23b842822753b2d1327f3b4eddd67bb552993bcb71e813307206134ace8559d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YPGYDM6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDB%2BxPXQxXGrEYixSdtAA69V6wyiNHaeohMRjdct%2FR6fAiBoty47bgPf0PBFl0tZA2wuiXvIAnCuk7tVSeEZmsqCnSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVIMtNdG3FxmGDL3sKtwDkbGH1Z58IQjFDkj45Iv25fuodLyYnbTZshF2V81%2BGCgapRuGQtq6udcXWu%2BrMcHIlGe632SMa69EYPACH5hLLWII%2BQPoiIy0uuRLqPkTCC3XFFSZSwX3ZBqAivAP%2F5R3Is4fMfhlUtC6To3YeqMVPS%2BbJHCggpA2EICsphyEMWme9egO5hGBcFMrGhZggPatCO%2FEGgIP9BJW%2BP8czBcsuBlL13Ds%2B1HoIYCYUIgHfNtVdFtrBX6vltEjIrjMYMCxStsMHEh09hS7ogJi2mckbd9GSU9dVTjlnAodaTJTTB%2BAiEDfHHs7qkd9S6p7TB49YQFF51GWnM%2B5rD9mkTkXGhbro8DFHvJgGHbJaUcZ9ClPm%2FGIes93bvavKYfn1mNCUM6iW0UkWYO9Y7sLojjROYyqrzpG5Ga149duna0yC6EPlG6PMWoyh2KWcjj6hsber1OEUQRtTkQ2nsj2xldLqv1x9d%2FQizUq0vFs56NYzOsEbBKEzayWBXH2LITvTV1%2Fme0bCML8mhNAsHckNR6XeyTyVbM2jxyeekhVRiR%2Fc%2F11mzEctlfk0Ni3R1i51AdsdVlFjd3eEeTOzqkE8%2FZeaR0yFu6ADHyMgMq8wDxhYMen8A%2BKfEKRSz3HxOEw%2BfH6vAY6pgEV19huVumElKCiLIq%2BANcX3qyCVEOx%2B8HY1N6x8sp%2F%2FgXP%2F8BewjZM8DUOqQWYJFsC5E%2Fyc754NG%2BczBZ%2FIqe4H%2Bd0wtPh8cofTueIYTNNl5yvr6CKsRjQG%2FRT%2BkHogtrO0HdpW98zyT5o1Kv%2BUfvvNU%2BOi%2Bd6%2Fr9K5iAIdPcHqkDKRhIQCPKVUW%2BJi5clP4RYWx2lExLli76G8rcFlemVZyEy6QrX&X-Amz-Signature=da58052e8cc71c1928abe72f3a3bd016d98bc4d2fa6a685f788aa9c41a6d1582&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YPGYDM6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDB%2BxPXQxXGrEYixSdtAA69V6wyiNHaeohMRjdct%2FR6fAiBoty47bgPf0PBFl0tZA2wuiXvIAnCuk7tVSeEZmsqCnSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVIMtNdG3FxmGDL3sKtwDkbGH1Z58IQjFDkj45Iv25fuodLyYnbTZshF2V81%2BGCgapRuGQtq6udcXWu%2BrMcHIlGe632SMa69EYPACH5hLLWII%2BQPoiIy0uuRLqPkTCC3XFFSZSwX3ZBqAivAP%2F5R3Is4fMfhlUtC6To3YeqMVPS%2BbJHCggpA2EICsphyEMWme9egO5hGBcFMrGhZggPatCO%2FEGgIP9BJW%2BP8czBcsuBlL13Ds%2B1HoIYCYUIgHfNtVdFtrBX6vltEjIrjMYMCxStsMHEh09hS7ogJi2mckbd9GSU9dVTjlnAodaTJTTB%2BAiEDfHHs7qkd9S6p7TB49YQFF51GWnM%2B5rD9mkTkXGhbro8DFHvJgGHbJaUcZ9ClPm%2FGIes93bvavKYfn1mNCUM6iW0UkWYO9Y7sLojjROYyqrzpG5Ga149duna0yC6EPlG6PMWoyh2KWcjj6hsber1OEUQRtTkQ2nsj2xldLqv1x9d%2FQizUq0vFs56NYzOsEbBKEzayWBXH2LITvTV1%2Fme0bCML8mhNAsHckNR6XeyTyVbM2jxyeekhVRiR%2Fc%2F11mzEctlfk0Ni3R1i51AdsdVlFjd3eEeTOzqkE8%2FZeaR0yFu6ADHyMgMq8wDxhYMen8A%2BKfEKRSz3HxOEw%2BfH6vAY6pgEV19huVumElKCiLIq%2BANcX3qyCVEOx%2B8HY1N6x8sp%2F%2FgXP%2F8BewjZM8DUOqQWYJFsC5E%2Fyc754NG%2BczBZ%2FIqe4H%2Bd0wtPh8cofTueIYTNNl5yvr6CKsRjQG%2FRT%2BkHogtrO0HdpW98zyT5o1Kv%2BUfvvNU%2BOi%2Bd6%2Fr9K5iAIdPcHqkDKRhIQCPKVUW%2BJi5clP4RYWx2lExLli76G8rcFlemVZyEy6QrX&X-Amz-Signature=6a2f8e8eb2018f5a93ef4e7be2ee039690f1a4172d81758cc4f86cd2c3b7b417&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YPGYDM6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDB%2BxPXQxXGrEYixSdtAA69V6wyiNHaeohMRjdct%2FR6fAiBoty47bgPf0PBFl0tZA2wuiXvIAnCuk7tVSeEZmsqCnSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVIMtNdG3FxmGDL3sKtwDkbGH1Z58IQjFDkj45Iv25fuodLyYnbTZshF2V81%2BGCgapRuGQtq6udcXWu%2BrMcHIlGe632SMa69EYPACH5hLLWII%2BQPoiIy0uuRLqPkTCC3XFFSZSwX3ZBqAivAP%2F5R3Is4fMfhlUtC6To3YeqMVPS%2BbJHCggpA2EICsphyEMWme9egO5hGBcFMrGhZggPatCO%2FEGgIP9BJW%2BP8czBcsuBlL13Ds%2B1HoIYCYUIgHfNtVdFtrBX6vltEjIrjMYMCxStsMHEh09hS7ogJi2mckbd9GSU9dVTjlnAodaTJTTB%2BAiEDfHHs7qkd9S6p7TB49YQFF51GWnM%2B5rD9mkTkXGhbro8DFHvJgGHbJaUcZ9ClPm%2FGIes93bvavKYfn1mNCUM6iW0UkWYO9Y7sLojjROYyqrzpG5Ga149duna0yC6EPlG6PMWoyh2KWcjj6hsber1OEUQRtTkQ2nsj2xldLqv1x9d%2FQizUq0vFs56NYzOsEbBKEzayWBXH2LITvTV1%2Fme0bCML8mhNAsHckNR6XeyTyVbM2jxyeekhVRiR%2Fc%2F11mzEctlfk0Ni3R1i51AdsdVlFjd3eEeTOzqkE8%2FZeaR0yFu6ADHyMgMq8wDxhYMen8A%2BKfEKRSz3HxOEw%2BfH6vAY6pgEV19huVumElKCiLIq%2BANcX3qyCVEOx%2B8HY1N6x8sp%2F%2FgXP%2F8BewjZM8DUOqQWYJFsC5E%2Fyc754NG%2BczBZ%2FIqe4H%2Bd0wtPh8cofTueIYTNNl5yvr6CKsRjQG%2FRT%2BkHogtrO0HdpW98zyT5o1Kv%2BUfvvNU%2BOi%2Bd6%2Fr9K5iAIdPcHqkDKRhIQCPKVUW%2BJi5clP4RYWx2lExLli76G8rcFlemVZyEy6QrX&X-Amz-Signature=154cdc2e5b3648fbf403398702eda7034e4ed76ae230b38998616bd83e917284&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YPGYDM6%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDB%2BxPXQxXGrEYixSdtAA69V6wyiNHaeohMRjdct%2FR6fAiBoty47bgPf0PBFl0tZA2wuiXvIAnCuk7tVSeEZmsqCnSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVIMtNdG3FxmGDL3sKtwDkbGH1Z58IQjFDkj45Iv25fuodLyYnbTZshF2V81%2BGCgapRuGQtq6udcXWu%2BrMcHIlGe632SMa69EYPACH5hLLWII%2BQPoiIy0uuRLqPkTCC3XFFSZSwX3ZBqAivAP%2F5R3Is4fMfhlUtC6To3YeqMVPS%2BbJHCggpA2EICsphyEMWme9egO5hGBcFMrGhZggPatCO%2FEGgIP9BJW%2BP8czBcsuBlL13Ds%2B1HoIYCYUIgHfNtVdFtrBX6vltEjIrjMYMCxStsMHEh09hS7ogJi2mckbd9GSU9dVTjlnAodaTJTTB%2BAiEDfHHs7qkd9S6p7TB49YQFF51GWnM%2B5rD9mkTkXGhbro8DFHvJgGHbJaUcZ9ClPm%2FGIes93bvavKYfn1mNCUM6iW0UkWYO9Y7sLojjROYyqrzpG5Ga149duna0yC6EPlG6PMWoyh2KWcjj6hsber1OEUQRtTkQ2nsj2xldLqv1x9d%2FQizUq0vFs56NYzOsEbBKEzayWBXH2LITvTV1%2Fme0bCML8mhNAsHckNR6XeyTyVbM2jxyeekhVRiR%2Fc%2F11mzEctlfk0Ni3R1i51AdsdVlFjd3eEeTOzqkE8%2FZeaR0yFu6ADHyMgMq8wDxhYMen8A%2BKfEKRSz3HxOEw%2BfH6vAY6pgEV19huVumElKCiLIq%2BANcX3qyCVEOx%2B8HY1N6x8sp%2F%2FgXP%2F8BewjZM8DUOqQWYJFsC5E%2Fyc754NG%2BczBZ%2FIqe4H%2Bd0wtPh8cofTueIYTNNl5yvr6CKsRjQG%2FRT%2BkHogtrO0HdpW98zyT5o1Kv%2BUfvvNU%2BOi%2Bd6%2Fr9K5iAIdPcHqkDKRhIQCPKVUW%2BJi5clP4RYWx2lExLli76G8rcFlemVZyEy6QrX&X-Amz-Signature=5a8f624de258a1fb8a970c1640c8212275326acad86b8c334e309bec2248b218&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7H2TJMV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBThCIkIUzDLMeWVjoYwX9fZnV9McbaHI3s6hwe1W1dAIgPPjWXCCWVvrmt4aHTEuN%2FplPQHN5vUU2t3k8iEFGDKQqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2wJ4y%2FWD%2FxoIiHECrcA3STlgfhfCxQiSzCo9%2BIO7jpPayCEqDaxMEWkll4E8IWDMDjbDod1wAnEcmpHNaBnH5SjfL4YTOXRXscICONWmmOnMVM%2Fn2M3DwNRgXOwHsHlfUq%2Fnx5OgvcMiirKPM6x%2BPrmCcnexHE08I6yHWwfT%2FPlscyPqgSrrt0zXYJ6Ih3ltkiv7DbmUY020llHji9SBvJiJBZBjQ7ypG7a5DG5mkMhB3moJbNT1qBF5W86JOJC32bv3YT0JW6ozlkDJ%2BB6MWYxuAs4gZlnnON5e1z3%2FuO8jlamtuTmDQ6xv5PCTWo7OH3ndd8JXAdTcWx2X%2BofhbiXl%2BY38GinvCbj0Yb%2BqHEkCR%2B2VQKGdbBQQd7ICpvxJ5ra6NvavP3CpfG75b1O8NlbeIxoCyUWmOCEV3oj8pwt5TzaUw29YNSO3p5xdGw1Nq7zUoumwVW7OM%2FPuUfkRxws1qjpgRd0oKFuerGWv3q%2FhI5pIILUr31unsrr0j0tWv8Efc%2FRjUIieDl52Iu%2FvWnBbnV0jai8d3HOcNKQC5u39aAkqDrXiz76KNu8XBqt4PLDOWSgvY1OKbLYEipXE%2BtM8O28t7S%2BvVFwi75WaXbtu9Np%2FNZ5cnZraFNxz7faxVZzQZVY1Buhj0hMNHx%2BrwGOqUBRUjbJ2KDku19eAzM1dQhptV1xOoe0qP67WJ%2BCw6aRFetFyT5g1MTeq9GilQ0e46ZowXXfXqHcL57WGB1kj35%2Ben3aNvY%2FyssEJmR2PBsAobaabxTYkRBFmvkMO7ZlnAqGF%2BFY8goMjH2FWPpDtuJdTMXFmOeFGV5EekU4zWlr64nFPrG1pvZtHy9G4e5MATITKLZIRcBjErRFhQmGLtgJl7wlzEg&X-Amz-Signature=121ef6dfaed5e06992fa6a7a8be2cfd3a91b4791d389e06e721b472ef44e6ae9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZYUY43V%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FNE7VR6xNm1VolG%2FFilK6GE%2FLW9fClN0MiH7Bq0m7XwIgevBXtpoSaRPkdd7sRU8cn52YtiUw%2BxUA03Cjm%2FlT54gqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2yyh1HmXhGBeIpmCrcA1QrvOAnhqJIHIf1HXP2zPqWQR3F3O7Uv2cbNbdw5rvLWR3VUluQt1OQDRA70F%2FdWIYBBMZRiml5%2FVSBD4VzpEG5tMIGhVLJpAdiSjYBRBctUcYE1233rQSTqAEXSfyWvLxQ28Oa8VyrA3P86hSD6%2FyYOw3d1Z8nEPTLYYWsc%2B8aujIZBSJdxWshTfIj1VVeyVoLyPXmAMOk6GepS9RnzGiU%2BYQs7efePHVEs0qRGCoihrWxI8v8ZDztwkuXovAhWYC%2FAVj6GTZ9Iv%2BluOUwH2SubjBgonZJwKqJ9jQth8kmlh7Ljjs5rBp6uLTg78BIRsZKRq9yAmvibbmzMSWHbGFtdwntZ2JT6snJGUr6%2FGPeag2KyyTjFqobt7heREHQeHJqEYkBAUdZqzC0%2BGdB6sT8i4lmX44w%2FTwQWZ8dQdJOVCK92uUQv97ap7C1lKaWW0jZDRBZAuvoHw18IbxMpPxyIkMKr22ZgDIkG1YH5ZTTEmvKjn5CvcKNhc%2BvDcxy2hpiTVpKZlQ7IEVTmJ8ZMFK3xrSsSlf3EuXkNjg5kitewh0ieECMaP3BBHMGOUHJigOua0mv4zNA%2FwXNq8Ruc3%2BBzgss3OL2cOzvt6JAVUIuAYZaKgRoSCnmhSqeMPXx%2BrwGOqUBitjxGxN6JeHN%2BFWjkckL5BPn8Z27dApyRN2UqMMd4YbRkG6oF48ybVK4AblRAOFE%2BnOvb9l%2BUlqYDwypG9wI6%2BRZcuXHh2WYPdo5W7%2Ft6QbvJfs5EAWv56vpt36XI5pV7FyIn9RaXcWuHl%2FtqmL71mU%2FgmCksdYRN05CXPOBjIb6z%2FH6LGnWPkWhATFvStnTHjda%2FwlmHCO8F8Hp6hlba%2Bz8z8O0&X-Amz-Signature=4a63256e6c5a3401d2e98a4f8a9c314a8664d5eb622e0ed96405ec4b94db0c46&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BDGOV7Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiPVf2xHgpjQNZgUJdLSsL7%2FKoh0StwVjj2HCY13zG5wIhAJN%2FYFEuBNCfnHOnCtRyy4BbFjkjGK%2FgpmGg%2BJjJqNQ2KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyP%2Fr2ZTL9jfU5JA%2B4q3APOioPVqUpEwULp9DuqUNGLpr5NXzgJhXa43JhZsu6RXvx7x5mzF%2FG%2Bu1ut2yXCtlhkNYGJtqLJXSnUT2DDZBDO9J3p7D3EJzFhcqwJjKcerccpkdwmPC1WwgiWWuh0qjQ%2FYMH8Tz3ROPqK0HRDVTfKDj2KAdGRVG5pYXyCgklwy9t59gBW1Ubu7LOCKB3JM73B4R7jSvWpOa1tpPxTycpYKJdXNTBjJATkcemv%2F4DBYRI7SZTlC0t%2F91ye%2BfTlTKtpFFaM4z50CBp8hSCMM4XTCHlZAtOdNkHSwq23QBcE0u1GJglbPjCbwCtFaujAi7RxAuVweifjgPq04N845igkJWMspZOGDGk%2Fsbj8WCF83ChJwHkxbtGbrzavg9YXE%2B6z2iiGLZnHIoi7ek6dENkDwn2OVWD494ATdr2zIKgimurrf2XUpzwGDs75p1EKDOrI4J1GoR9%2FizOUTj7lYyMEeY4T8iyY7no7LQ2fe5YlWVCJO%2BcWAM2QogETQvtIDE8QibPX8LcqizSWtz70nx7mLkLTO5gfBbdiZkyQEoR%2F1%2BWzIlCXzns6YPywN%2FcQAgpJ%2BG%2Btt%2Bjjq04dLiLvyVeOGUvp7kyW9z8KZrBe9KWk3AnlNmOWiws%2FY7I33zCH8vq8BjqkAdjqYklA2kgQ8K6B8r1jdXWX5KTxWDmxHJBN165cUzEUwFBTcxmjfUBNFcdB%2F4r8rPPjm7s08TsNKkNtI9MtsnNXwapTp0cPmK0RJg%2B0beZhZrxmX2lsJQkBUR2YORdmgK7%2Fy4lquBPtfjyh179VkmY3%2Fr5LJjKmpMxZUIF3l0bzLXiLWsivHfAZ6mCVwke9KUlwW%2BaDd2j8YvWuLFNpgbSCHs%2Bq&X-Amz-Signature=558f4fc17c5eb1092f1dc60832b14d3695d60af17b35a0a440d414546adb2b23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BDGOV7Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiPVf2xHgpjQNZgUJdLSsL7%2FKoh0StwVjj2HCY13zG5wIhAJN%2FYFEuBNCfnHOnCtRyy4BbFjkjGK%2FgpmGg%2BJjJqNQ2KogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyP%2Fr2ZTL9jfU5JA%2B4q3APOioPVqUpEwULp9DuqUNGLpr5NXzgJhXa43JhZsu6RXvx7x5mzF%2FG%2Bu1ut2yXCtlhkNYGJtqLJXSnUT2DDZBDO9J3p7D3EJzFhcqwJjKcerccpkdwmPC1WwgiWWuh0qjQ%2FYMH8Tz3ROPqK0HRDVTfKDj2KAdGRVG5pYXyCgklwy9t59gBW1Ubu7LOCKB3JM73B4R7jSvWpOa1tpPxTycpYKJdXNTBjJATkcemv%2F4DBYRI7SZTlC0t%2F91ye%2BfTlTKtpFFaM4z50CBp8hSCMM4XTCHlZAtOdNkHSwq23QBcE0u1GJglbPjCbwCtFaujAi7RxAuVweifjgPq04N845igkJWMspZOGDGk%2Fsbj8WCF83ChJwHkxbtGbrzavg9YXE%2B6z2iiGLZnHIoi7ek6dENkDwn2OVWD494ATdr2zIKgimurrf2XUpzwGDs75p1EKDOrI4J1GoR9%2FizOUTj7lYyMEeY4T8iyY7no7LQ2fe5YlWVCJO%2BcWAM2QogETQvtIDE8QibPX8LcqizSWtz70nx7mLkLTO5gfBbdiZkyQEoR%2F1%2BWzIlCXzns6YPywN%2FcQAgpJ%2BG%2Btt%2Bjjq04dLiLvyVeOGUvp7kyW9z8KZrBe9KWk3AnlNmOWiws%2FY7I33zCH8vq8BjqkAdjqYklA2kgQ8K6B8r1jdXWX5KTxWDmxHJBN165cUzEUwFBTcxmjfUBNFcdB%2F4r8rPPjm7s08TsNKkNtI9MtsnNXwapTp0cPmK0RJg%2B0beZhZrxmX2lsJQkBUR2YORdmgK7%2Fy4lquBPtfjyh179VkmY3%2Fr5LJjKmpMxZUIF3l0bzLXiLWsivHfAZ6mCVwke9KUlwW%2BaDd2j8YvWuLFNpgbSCHs%2Bq&X-Amz-Signature=43926cca25f3269e64c85bddfdbe7bafbc459b6a153b0de648de9628bc4decd3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
