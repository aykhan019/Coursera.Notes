

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SADBUIM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDEyaLrMrpnJIep2miToHBpGbZ9puh20oP6u02wfNI1ZAIgZI7AhXfaimBb7lwajdn%2FWV8Hf6tppAMofHqxr%2Fw1qXYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNIBHOVoJWZeIz7GOCrcA%2Bz44EqzK2ojOAKN3%2B6w3qtLlDM0wuoxR4obA1OB9x0rpWqjAsA%2FLuktJs8AF75Jp%2BY2AljSOagrY0alIG3d8Kfe5UpNO5HCJ8Hi2Zjr1xCSnhc%2Bvdf%2BI%2BtsJUDo7tiB63G7Q2jwhOyP9SBVivKmCW0AB5mQxHQMjdtQOdyL2FLj2fKntrNQMiM1NbA9%2BUooH8hib3mpAdsQrTybThhkN0KkGgWxHIb0AKf4t%2BFZUeRDk4WoDf7n57boN7M4cwdfVtV%2FfYl1FQPKgm4WpZP%2F5hUjfW%2BXIH0ocwkPY%2BkWTjLdR%2BEVetZpqf6rr%2BjnPsgFzF%2BWfK1ILgQj41XeqklYRnb%2FdM3IBx7fo6SrGzcWGFbeKZcn3aFA4kPK%2FpKy4qLch3abrJ3N9qFuKW7cmHWNc8meu0EvFI7HRkhB58D%2FG%2BTEJwmSzc%2BRbP3rtjBh4LxOXRERrRCCi0TlULWs7FnpWvFVsdPkybJR0g6hh3kzHxfBCcVXGQFH%2FIdDz37QfbqW28bElvemHPhtO1btzOd0kHUtXlDFRpPipC6TRNuG5CCV9DESks4nLHlDyMKJGu2kk%2F4NZBVed6M8199N3Qfw0rTNu9jXjwOFGWBj2hOzFzqFOGm3wRM%2FAk2PMKWMMJm6jr0GOqUBDQbuCt19V%2Bs1oOcd%2BiejxanqkBb7Z4OV5cbpQ8uLpeIc0BFp%2FntSuVjb%2Fb8vbTqd4ekK07HtqTIBx0EXW7Sk2EaeB4FACFVvH58E1twPxIoD7T%2BHQAIR%2BmY%2BE4Oufg%2BCo740uQU1J%2B6ZcYcfewT%2BgcLUvZwYOWC8F7mMjkTew3KfGAVYA6TWgjEwqQteMYlmtzfuO55bkzy1yQ8tBJxsUuls%2FIEm&X-Amz-Signature=74c70ee7ef6d78a1f2b5f3f757bf13f570c980468b0930f4ae462784a3187b8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SADBUIM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDEyaLrMrpnJIep2miToHBpGbZ9puh20oP6u02wfNI1ZAIgZI7AhXfaimBb7lwajdn%2FWV8Hf6tppAMofHqxr%2Fw1qXYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNIBHOVoJWZeIz7GOCrcA%2Bz44EqzK2ojOAKN3%2B6w3qtLlDM0wuoxR4obA1OB9x0rpWqjAsA%2FLuktJs8AF75Jp%2BY2AljSOagrY0alIG3d8Kfe5UpNO5HCJ8Hi2Zjr1xCSnhc%2Bvdf%2BI%2BtsJUDo7tiB63G7Q2jwhOyP9SBVivKmCW0AB5mQxHQMjdtQOdyL2FLj2fKntrNQMiM1NbA9%2BUooH8hib3mpAdsQrTybThhkN0KkGgWxHIb0AKf4t%2BFZUeRDk4WoDf7n57boN7M4cwdfVtV%2FfYl1FQPKgm4WpZP%2F5hUjfW%2BXIH0ocwkPY%2BkWTjLdR%2BEVetZpqf6rr%2BjnPsgFzF%2BWfK1ILgQj41XeqklYRnb%2FdM3IBx7fo6SrGzcWGFbeKZcn3aFA4kPK%2FpKy4qLch3abrJ3N9qFuKW7cmHWNc8meu0EvFI7HRkhB58D%2FG%2BTEJwmSzc%2BRbP3rtjBh4LxOXRERrRCCi0TlULWs7FnpWvFVsdPkybJR0g6hh3kzHxfBCcVXGQFH%2FIdDz37QfbqW28bElvemHPhtO1btzOd0kHUtXlDFRpPipC6TRNuG5CCV9DESks4nLHlDyMKJGu2kk%2F4NZBVed6M8199N3Qfw0rTNu9jXjwOFGWBj2hOzFzqFOGm3wRM%2FAk2PMKWMMJm6jr0GOqUBDQbuCt19V%2Bs1oOcd%2BiejxanqkBb7Z4OV5cbpQ8uLpeIc0BFp%2FntSuVjb%2Fb8vbTqd4ekK07HtqTIBx0EXW7Sk2EaeB4FACFVvH58E1twPxIoD7T%2BHQAIR%2BmY%2BE4Oufg%2BCo740uQU1J%2B6ZcYcfewT%2BgcLUvZwYOWC8F7mMjkTew3KfGAVYA6TWgjEwqQteMYlmtzfuO55bkzy1yQ8tBJxsUuls%2FIEm&X-Amz-Signature=7a162a445e04a3eeb18fb259cd226f8038b23e881e3e70b10e3e476092ec78c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SADBUIM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDEyaLrMrpnJIep2miToHBpGbZ9puh20oP6u02wfNI1ZAIgZI7AhXfaimBb7lwajdn%2FWV8Hf6tppAMofHqxr%2Fw1qXYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNIBHOVoJWZeIz7GOCrcA%2Bz44EqzK2ojOAKN3%2B6w3qtLlDM0wuoxR4obA1OB9x0rpWqjAsA%2FLuktJs8AF75Jp%2BY2AljSOagrY0alIG3d8Kfe5UpNO5HCJ8Hi2Zjr1xCSnhc%2Bvdf%2BI%2BtsJUDo7tiB63G7Q2jwhOyP9SBVivKmCW0AB5mQxHQMjdtQOdyL2FLj2fKntrNQMiM1NbA9%2BUooH8hib3mpAdsQrTybThhkN0KkGgWxHIb0AKf4t%2BFZUeRDk4WoDf7n57boN7M4cwdfVtV%2FfYl1FQPKgm4WpZP%2F5hUjfW%2BXIH0ocwkPY%2BkWTjLdR%2BEVetZpqf6rr%2BjnPsgFzF%2BWfK1ILgQj41XeqklYRnb%2FdM3IBx7fo6SrGzcWGFbeKZcn3aFA4kPK%2FpKy4qLch3abrJ3N9qFuKW7cmHWNc8meu0EvFI7HRkhB58D%2FG%2BTEJwmSzc%2BRbP3rtjBh4LxOXRERrRCCi0TlULWs7FnpWvFVsdPkybJR0g6hh3kzHxfBCcVXGQFH%2FIdDz37QfbqW28bElvemHPhtO1btzOd0kHUtXlDFRpPipC6TRNuG5CCV9DESks4nLHlDyMKJGu2kk%2F4NZBVed6M8199N3Qfw0rTNu9jXjwOFGWBj2hOzFzqFOGm3wRM%2FAk2PMKWMMJm6jr0GOqUBDQbuCt19V%2Bs1oOcd%2BiejxanqkBb7Z4OV5cbpQ8uLpeIc0BFp%2FntSuVjb%2Fb8vbTqd4ekK07HtqTIBx0EXW7Sk2EaeB4FACFVvH58E1twPxIoD7T%2BHQAIR%2BmY%2BE4Oufg%2BCo740uQU1J%2B6ZcYcfewT%2BgcLUvZwYOWC8F7mMjkTew3KfGAVYA6TWgjEwqQteMYlmtzfuO55bkzy1yQ8tBJxsUuls%2FIEm&X-Amz-Signature=222e48969340e2621d466ed3825a23fabf7bd109d5f2761d82489d35b3b5f7fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SADBUIM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDEyaLrMrpnJIep2miToHBpGbZ9puh20oP6u02wfNI1ZAIgZI7AhXfaimBb7lwajdn%2FWV8Hf6tppAMofHqxr%2Fw1qXYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNIBHOVoJWZeIz7GOCrcA%2Bz44EqzK2ojOAKN3%2B6w3qtLlDM0wuoxR4obA1OB9x0rpWqjAsA%2FLuktJs8AF75Jp%2BY2AljSOagrY0alIG3d8Kfe5UpNO5HCJ8Hi2Zjr1xCSnhc%2Bvdf%2BI%2BtsJUDo7tiB63G7Q2jwhOyP9SBVivKmCW0AB5mQxHQMjdtQOdyL2FLj2fKntrNQMiM1NbA9%2BUooH8hib3mpAdsQrTybThhkN0KkGgWxHIb0AKf4t%2BFZUeRDk4WoDf7n57boN7M4cwdfVtV%2FfYl1FQPKgm4WpZP%2F5hUjfW%2BXIH0ocwkPY%2BkWTjLdR%2BEVetZpqf6rr%2BjnPsgFzF%2BWfK1ILgQj41XeqklYRnb%2FdM3IBx7fo6SrGzcWGFbeKZcn3aFA4kPK%2FpKy4qLch3abrJ3N9qFuKW7cmHWNc8meu0EvFI7HRkhB58D%2FG%2BTEJwmSzc%2BRbP3rtjBh4LxOXRERrRCCi0TlULWs7FnpWvFVsdPkybJR0g6hh3kzHxfBCcVXGQFH%2FIdDz37QfbqW28bElvemHPhtO1btzOd0kHUtXlDFRpPipC6TRNuG5CCV9DESks4nLHlDyMKJGu2kk%2F4NZBVed6M8199N3Qfw0rTNu9jXjwOFGWBj2hOzFzqFOGm3wRM%2FAk2PMKWMMJm6jr0GOqUBDQbuCt19V%2Bs1oOcd%2BiejxanqkBb7Z4OV5cbpQ8uLpeIc0BFp%2FntSuVjb%2Fb8vbTqd4ekK07HtqTIBx0EXW7Sk2EaeB4FACFVvH58E1twPxIoD7T%2BHQAIR%2BmY%2BE4Oufg%2BCo740uQU1J%2B6ZcYcfewT%2BgcLUvZwYOWC8F7mMjkTew3KfGAVYA6TWgjEwqQteMYlmtzfuO55bkzy1yQ8tBJxsUuls%2FIEm&X-Amz-Signature=1f71c026f74a77041fced63fa43cca15e73dca0bbb8c99e52ab5734a532c2435&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SADBUIM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDEyaLrMrpnJIep2miToHBpGbZ9puh20oP6u02wfNI1ZAIgZI7AhXfaimBb7lwajdn%2FWV8Hf6tppAMofHqxr%2Fw1qXYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNIBHOVoJWZeIz7GOCrcA%2Bz44EqzK2ojOAKN3%2B6w3qtLlDM0wuoxR4obA1OB9x0rpWqjAsA%2FLuktJs8AF75Jp%2BY2AljSOagrY0alIG3d8Kfe5UpNO5HCJ8Hi2Zjr1xCSnhc%2Bvdf%2BI%2BtsJUDo7tiB63G7Q2jwhOyP9SBVivKmCW0AB5mQxHQMjdtQOdyL2FLj2fKntrNQMiM1NbA9%2BUooH8hib3mpAdsQrTybThhkN0KkGgWxHIb0AKf4t%2BFZUeRDk4WoDf7n57boN7M4cwdfVtV%2FfYl1FQPKgm4WpZP%2F5hUjfW%2BXIH0ocwkPY%2BkWTjLdR%2BEVetZpqf6rr%2BjnPsgFzF%2BWfK1ILgQj41XeqklYRnb%2FdM3IBx7fo6SrGzcWGFbeKZcn3aFA4kPK%2FpKy4qLch3abrJ3N9qFuKW7cmHWNc8meu0EvFI7HRkhB58D%2FG%2BTEJwmSzc%2BRbP3rtjBh4LxOXRERrRCCi0TlULWs7FnpWvFVsdPkybJR0g6hh3kzHxfBCcVXGQFH%2FIdDz37QfbqW28bElvemHPhtO1btzOd0kHUtXlDFRpPipC6TRNuG5CCV9DESks4nLHlDyMKJGu2kk%2F4NZBVed6M8199N3Qfw0rTNu9jXjwOFGWBj2hOzFzqFOGm3wRM%2FAk2PMKWMMJm6jr0GOqUBDQbuCt19V%2Bs1oOcd%2BiejxanqkBb7Z4OV5cbpQ8uLpeIc0BFp%2FntSuVjb%2Fb8vbTqd4ekK07HtqTIBx0EXW7Sk2EaeB4FACFVvH58E1twPxIoD7T%2BHQAIR%2BmY%2BE4Oufg%2BCo740uQU1J%2B6ZcYcfewT%2BgcLUvZwYOWC8F7mMjkTew3KfGAVYA6TWgjEwqQteMYlmtzfuO55bkzy1yQ8tBJxsUuls%2FIEm&X-Amz-Signature=508445f630704b68c3a93a9268429e1d75f659431e68571823046c5afa70c084&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SADBUIM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDEyaLrMrpnJIep2miToHBpGbZ9puh20oP6u02wfNI1ZAIgZI7AhXfaimBb7lwajdn%2FWV8Hf6tppAMofHqxr%2Fw1qXYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNIBHOVoJWZeIz7GOCrcA%2Bz44EqzK2ojOAKN3%2B6w3qtLlDM0wuoxR4obA1OB9x0rpWqjAsA%2FLuktJs8AF75Jp%2BY2AljSOagrY0alIG3d8Kfe5UpNO5HCJ8Hi2Zjr1xCSnhc%2Bvdf%2BI%2BtsJUDo7tiB63G7Q2jwhOyP9SBVivKmCW0AB5mQxHQMjdtQOdyL2FLj2fKntrNQMiM1NbA9%2BUooH8hib3mpAdsQrTybThhkN0KkGgWxHIb0AKf4t%2BFZUeRDk4WoDf7n57boN7M4cwdfVtV%2FfYl1FQPKgm4WpZP%2F5hUjfW%2BXIH0ocwkPY%2BkWTjLdR%2BEVetZpqf6rr%2BjnPsgFzF%2BWfK1ILgQj41XeqklYRnb%2FdM3IBx7fo6SrGzcWGFbeKZcn3aFA4kPK%2FpKy4qLch3abrJ3N9qFuKW7cmHWNc8meu0EvFI7HRkhB58D%2FG%2BTEJwmSzc%2BRbP3rtjBh4LxOXRERrRCCi0TlULWs7FnpWvFVsdPkybJR0g6hh3kzHxfBCcVXGQFH%2FIdDz37QfbqW28bElvemHPhtO1btzOd0kHUtXlDFRpPipC6TRNuG5CCV9DESks4nLHlDyMKJGu2kk%2F4NZBVed6M8199N3Qfw0rTNu9jXjwOFGWBj2hOzFzqFOGm3wRM%2FAk2PMKWMMJm6jr0GOqUBDQbuCt19V%2Bs1oOcd%2BiejxanqkBb7Z4OV5cbpQ8uLpeIc0BFp%2FntSuVjb%2Fb8vbTqd4ekK07HtqTIBx0EXW7Sk2EaeB4FACFVvH58E1twPxIoD7T%2BHQAIR%2BmY%2BE4Oufg%2BCo740uQU1J%2B6ZcYcfewT%2BgcLUvZwYOWC8F7mMjkTew3KfGAVYA6TWgjEwqQteMYlmtzfuO55bkzy1yQ8tBJxsUuls%2FIEm&X-Amz-Signature=3320934c0bbdf0f239f2b8ae29e88820659fd43a44791089d311d47b28ec94d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SADBUIM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDEyaLrMrpnJIep2miToHBpGbZ9puh20oP6u02wfNI1ZAIgZI7AhXfaimBb7lwajdn%2FWV8Hf6tppAMofHqxr%2Fw1qXYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNIBHOVoJWZeIz7GOCrcA%2Bz44EqzK2ojOAKN3%2B6w3qtLlDM0wuoxR4obA1OB9x0rpWqjAsA%2FLuktJs8AF75Jp%2BY2AljSOagrY0alIG3d8Kfe5UpNO5HCJ8Hi2Zjr1xCSnhc%2Bvdf%2BI%2BtsJUDo7tiB63G7Q2jwhOyP9SBVivKmCW0AB5mQxHQMjdtQOdyL2FLj2fKntrNQMiM1NbA9%2BUooH8hib3mpAdsQrTybThhkN0KkGgWxHIb0AKf4t%2BFZUeRDk4WoDf7n57boN7M4cwdfVtV%2FfYl1FQPKgm4WpZP%2F5hUjfW%2BXIH0ocwkPY%2BkWTjLdR%2BEVetZpqf6rr%2BjnPsgFzF%2BWfK1ILgQj41XeqklYRnb%2FdM3IBx7fo6SrGzcWGFbeKZcn3aFA4kPK%2FpKy4qLch3abrJ3N9qFuKW7cmHWNc8meu0EvFI7HRkhB58D%2FG%2BTEJwmSzc%2BRbP3rtjBh4LxOXRERrRCCi0TlULWs7FnpWvFVsdPkybJR0g6hh3kzHxfBCcVXGQFH%2FIdDz37QfbqW28bElvemHPhtO1btzOd0kHUtXlDFRpPipC6TRNuG5CCV9DESks4nLHlDyMKJGu2kk%2F4NZBVed6M8199N3Qfw0rTNu9jXjwOFGWBj2hOzFzqFOGm3wRM%2FAk2PMKWMMJm6jr0GOqUBDQbuCt19V%2Bs1oOcd%2BiejxanqkBb7Z4OV5cbpQ8uLpeIc0BFp%2FntSuVjb%2Fb8vbTqd4ekK07HtqTIBx0EXW7Sk2EaeB4FACFVvH58E1twPxIoD7T%2BHQAIR%2BmY%2BE4Oufg%2BCo740uQU1J%2B6ZcYcfewT%2BgcLUvZwYOWC8F7mMjkTew3KfGAVYA6TWgjEwqQteMYlmtzfuO55bkzy1yQ8tBJxsUuls%2FIEm&X-Amz-Signature=7c3370bdb6449ae9f05efb6ea769e72946f450faaa5a0ab86eef8ffc4289b87e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SADBUIM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDEyaLrMrpnJIep2miToHBpGbZ9puh20oP6u02wfNI1ZAIgZI7AhXfaimBb7lwajdn%2FWV8Hf6tppAMofHqxr%2Fw1qXYq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDNIBHOVoJWZeIz7GOCrcA%2Bz44EqzK2ojOAKN3%2B6w3qtLlDM0wuoxR4obA1OB9x0rpWqjAsA%2FLuktJs8AF75Jp%2BY2AljSOagrY0alIG3d8Kfe5UpNO5HCJ8Hi2Zjr1xCSnhc%2Bvdf%2BI%2BtsJUDo7tiB63G7Q2jwhOyP9SBVivKmCW0AB5mQxHQMjdtQOdyL2FLj2fKntrNQMiM1NbA9%2BUooH8hib3mpAdsQrTybThhkN0KkGgWxHIb0AKf4t%2BFZUeRDk4WoDf7n57boN7M4cwdfVtV%2FfYl1FQPKgm4WpZP%2F5hUjfW%2BXIH0ocwkPY%2BkWTjLdR%2BEVetZpqf6rr%2BjnPsgFzF%2BWfK1ILgQj41XeqklYRnb%2FdM3IBx7fo6SrGzcWGFbeKZcn3aFA4kPK%2FpKy4qLch3abrJ3N9qFuKW7cmHWNc8meu0EvFI7HRkhB58D%2FG%2BTEJwmSzc%2BRbP3rtjBh4LxOXRERrRCCi0TlULWs7FnpWvFVsdPkybJR0g6hh3kzHxfBCcVXGQFH%2FIdDz37QfbqW28bElvemHPhtO1btzOd0kHUtXlDFRpPipC6TRNuG5CCV9DESks4nLHlDyMKJGu2kk%2F4NZBVed6M8199N3Qfw0rTNu9jXjwOFGWBj2hOzFzqFOGm3wRM%2FAk2PMKWMMJm6jr0GOqUBDQbuCt19V%2Bs1oOcd%2BiejxanqkBb7Z4OV5cbpQ8uLpeIc0BFp%2FntSuVjb%2Fb8vbTqd4ekK07HtqTIBx0EXW7Sk2EaeB4FACFVvH58E1twPxIoD7T%2BHQAIR%2BmY%2BE4Oufg%2BCo740uQU1J%2B6ZcYcfewT%2BgcLUvZwYOWC8F7mMjkTew3KfGAVYA6TWgjEwqQteMYlmtzfuO55bkzy1yQ8tBJxsUuls%2FIEm&X-Amz-Signature=9c293fb88e9666ea56d042a0c274868421aa4d0650ca94bb499306b3db4f6f7e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYBDPEMP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIGwZVaSgL5xYPZJMWkTVDMsX8irvHUhS0048k8Ku03HcAiBhxBuJsz61O%2B51nl8Dbwbt%2FnWd38306ie2sUmZRX1uayr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMhklRuT3TVHVB%2FmqRKtwDRgsEYBvhKyr6XI1vzbFpy%2Brbc2EEmr6%2FRnao2zlH2fhhMoP9xHFjNCJCG2nLshR2riB%2Bipsap%2FpkVgGgSnx7Z98yeP5ArOBFA2tRmd1sYnd9z0ZKoAKNs2ZfTLlpwd0Lg5hVpNKH5OtaTsyO24frB07B8%2BcInEE3%2Fd%2F%2BdTE1jUVWzjMKrsoD21%2Bw4IEQWcBgSf0gYSS95v6aZmfyCsTHZAiQx4s0FE3D%2BYJdautA4qP%2B5hlNFybRnDojZjZK93bvAauxUuuUx55BHU38%2BuPUN%2BBehbG%2F0kSHzGBoAhqBdVq4BZ1eJtws7r3IlgACxHLjtddHJ60EPY63%2FPhqFsJ6FtdJl0paJ5Ihxa0whicu7IyIPjr9BxGZgW4SA17%2BrfmWRwa%2BDVUQyP4uvv%2FNSG09XVmMd8RP7sr6yXZt%2FpwT%2BtbaJw5DIwDw5eoJzhv%2FMUIsoZBmG6hrhhqUD0CmACeQDYCQ%2BMV3MbDVhtRltufpG8YjucvYS4S48wvTaONAXZD05p3g%2FcqsEAyn2vSayXgPdV7oeYwJoCJYxWy9XDZfDn%2FjRXk3xRQL2J1QDP9w7xCOQNxThApnJhftsHxAJj45N6dTQPUGrblb314zwKxMkLjzUFqijUvyYSEMnCowiLyOvQY6pgFKF5fPLr1YknA2Xy5dsVicvK0ZIFg3vNjuTfjDVS1o1NyWKuaZE2V%2BDmxqazncisv%2BtMjQsU5%2FSZ39BrJO4%2FQRKgPh9Knd6D2hP4JQxmx1CoPLCbSskTz3xDkKGWtt2kA8ITEOyIHfC06wW9T53tlchXBIRK5bAfQX1ilBWo4GL%2F6v3eGDAoaXEHn7eWgBAi5ox7W7mXtup25mPon8JNap5aX6%2FuQy&X-Amz-Signature=c609ffad470520f309639a440cc27452a86d4b1623dabca6a083647685b235bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QH7O7HXH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIH7j6hX%2Fct%2F0gcKft0dsxj9bbTKYUrjZ78aXKH4PCv8eAiEA7HLe315lRsUdB19xRIidxvR7zdiPRdXowNNRek%2B5sWoq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDJgTIiSkg6uxKUuk6ircA6ipDfXWeupuyOMmsbfcpGGzPSQbOWzreLc%2BWOmt4l%2BK2hxaH%2FUUbnES5pUmNIGng34%2FPGZgym%2FL2GWe5wFxrDldtgv%2BH9RUUnJBZQ4XHICsn9tso3d5L5xSZ1h3%2B2jz6UWbtiF1Kk%2FNueu0M8f8b1J%2BjmZ1PT4F%2Fjubx%2FAVKxxuo0G22tacauG6ogf3EIki2W%2BDaJLIubY2NKcrL9o8A13ordgxBcanZAyEUKWUSnjclAkOr%2Fzx%2B%2BOvMDWpm6cUtBETUFOkKqe9rvbVvmTnjWe9DiWACGRaGJocG%2FkMaqDzj8Bqdq1nDUyOSJSRzODFZ4qukXrVI0tMvmvbzcWyulOV7sp9FS3zjKPTmbUaq48c1xHx8HM4xbk7KTtnkyFzWpCpcRQ1%2BDwh48%2FoZBeykmltZgK1FrrchL2iSOWtqk8J8UgfH7CGW2ZUPrcefM8%2F3LwDuIVXVZnTro02NCbA7ayCN6JnbMlj0UbLYx7R4mJztHpkUdRzbSynyMrPdtxpK%2FloW4eW3q%2BQKRgF4fk1a0fgYTOBtMPME98%2FVvVpKiVFykIFJN8UvhncWZNQysX1wBA%2FdhXCUMgSPWZsnNkHLKEkUi1vsI1Vsuzo%2FImGFZ6l82D3gei7R28%2FIzaOMKu6jr0GOqUB%2FtEDWXInJlEyKOgT7txqDtekVrnvYz6L6PVy12jDEn7X8a2i58VYScNH0FCWkqiPpZ7OI%2ByWnK%2FvtSYw2V28OHpsJxFg2Hk9R4XAaPO5vScnhjd8ZykEzUNWTNyxHIfn5s%2FeUb%2BEyvZrqCf2x3d2Yku7PAy0UIIdr30wp%2FH2EJ0fFaFEjqq7tafiea%2B0pHr37cNupLMRfpGHfUnNc%2BBNT%2B9H1dtD&X-Amz-Signature=cc5b427c6c69b9dc42fbe064084a6c447bf15d8cf02c49747b69316c46daf3b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WEH3YVD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDCeYHtFP5hyKVfQnRTNYNG8cg4Droq5KL7US2upW8stAIgGX9GEmIxsem9jVW%2B%2F%2B4sxSfKQ%2F433fnvIReFlSyiwSUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDJjvdMXVL3dY5yFtlircA82Knfb9ZZBraAwmu6bjpxC3nCFMnqggKaWevT%2FwOkFmzbGNSwmEIbtu9ZXSxcG7UljtfL169oZ2j6pHFxrTsRGI9bZJdPBhnMcoTZZxUw2sO4sPothoKe1OiyNIDT2lZchXxLoMDt7%2Fsq5cZN%2Fx64kXCUuxkFCyryzFRDnVKoFrj4x0zBJpTgHAvNky3KVDParOhb%2FGLYJ3jnzVSAShh78Cjwe9MRpTNtHoZQ4BbZTAmjMzy12YU8ekzJ7vdAs%2BXcYxYYdavKE4Ryi7JNhDi10OAvR8q%2FlYf5mvw9Vd0%2B2Q1R7hYZwyTYnPvVdglBAcbJCSHUNgEwCy1Wwto64IZbt8tRcSGebuP7pu4%2Bjuts%2BXLdUftM3qBmykEmh3jTrkIonkV9gu6Y5PavcXqXT7K1EZ7CEARppMQVaL94YZw6oCmrZ4IA7EaxMPqjSz6BeMvWnwMUiIQGdl8d5k3wZGZoKxlXp4NUYx3otxpvvNJCEd3g%2Bhm84e3o6jtjiMuFWvocM0HrMfZJHPkozIl8vz5cOiFa3M9eQpuS%2BSi50d8pd0NMQf4ASfznQBAlFEHY%2B6gzEyH0rHcKOMAZi0eSYanoAkoToCJ2c22oixM8f7zvVLakN1VZCbFpJMdsYyMMq6jr0GOqUBkLuEr2y8ybFWRQSuxyI1nVa%2BrortGU7VvYFJvWxmOMN4bAZmmlAl4OkISmVphda4%2B7SU8N%2BaxCYfInoDCCKb8DgQTPkh3Yw2IzT4ylqhJTq6Q%2Bf8klIrdgBZJ%2B1cSzI%2FuJUzYnU38VamAEFKG6TGimZqUvPaTVEqasbv8%2FVOP9fR4v5Iai2R7BFr%2BqXipD6otKI%2Bfqh6LiMZ1WJGd25Cs%2B4oHzn7&X-Amz-Signature=df506e4a158fbf80e922d92f70ccd64b5e172470691e372eb9d486f16b468b61&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WEH3YVD%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDCeYHtFP5hyKVfQnRTNYNG8cg4Droq5KL7US2upW8stAIgGX9GEmIxsem9jVW%2B%2F%2B4sxSfKQ%2F433fnvIReFlSyiwSUq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDJjvdMXVL3dY5yFtlircA82Knfb9ZZBraAwmu6bjpxC3nCFMnqggKaWevT%2FwOkFmzbGNSwmEIbtu9ZXSxcG7UljtfL169oZ2j6pHFxrTsRGI9bZJdPBhnMcoTZZxUw2sO4sPothoKe1OiyNIDT2lZchXxLoMDt7%2Fsq5cZN%2Fx64kXCUuxkFCyryzFRDnVKoFrj4x0zBJpTgHAvNky3KVDParOhb%2FGLYJ3jnzVSAShh78Cjwe9MRpTNtHoZQ4BbZTAmjMzy12YU8ekzJ7vdAs%2BXcYxYYdavKE4Ryi7JNhDi10OAvR8q%2FlYf5mvw9Vd0%2B2Q1R7hYZwyTYnPvVdglBAcbJCSHUNgEwCy1Wwto64IZbt8tRcSGebuP7pu4%2Bjuts%2BXLdUftM3qBmykEmh3jTrkIonkV9gu6Y5PavcXqXT7K1EZ7CEARppMQVaL94YZw6oCmrZ4IA7EaxMPqjSz6BeMvWnwMUiIQGdl8d5k3wZGZoKxlXp4NUYx3otxpvvNJCEd3g%2Bhm84e3o6jtjiMuFWvocM0HrMfZJHPkozIl8vz5cOiFa3M9eQpuS%2BSi50d8pd0NMQf4ASfznQBAlFEHY%2B6gzEyH0rHcKOMAZi0eSYanoAkoToCJ2c22oixM8f7zvVLakN1VZCbFpJMdsYyMMq6jr0GOqUBkLuEr2y8ybFWRQSuxyI1nVa%2BrortGU7VvYFJvWxmOMN4bAZmmlAl4OkISmVphda4%2B7SU8N%2BaxCYfInoDCCKb8DgQTPkh3Yw2IzT4ylqhJTq6Q%2Bf8klIrdgBZJ%2B1cSzI%2FuJUzYnU38VamAEFKG6TGimZqUvPaTVEqasbv8%2FVOP9fR4v5Iai2R7BFr%2BqXipD6otKI%2Bfqh6LiMZ1WJGd25Cs%2B4oHzn7&X-Amz-Signature=f8a5af291414665112c5c6125f96e6c7ec10a679df1bf0002866b506a902934d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
