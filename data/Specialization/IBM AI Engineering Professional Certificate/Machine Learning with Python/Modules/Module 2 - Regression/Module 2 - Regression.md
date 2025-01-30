

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623BC56Z3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBrbIWVquKCBspxX%2F5%2F4rpngzHWErF4Nmqx41bzQGDnMAiBLoLZ2HHKa64At5%2BjzHcqBSBSWSNXKt9GbxvN%2FMWpMLyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNC%2FJYJ9KDRBw%2FZFCKtwDaPReOlYpfdXRLGaNVAxj%2FxC0KOQ4RHrMkhJPH8mYFfZZHWM9G%2FyXXtLSBNfCK0NrhB%2BLuIxiJbs84akQpiRXK7fCttGUc3XEDZxDXSfKZw2%2Bvlyvj9LeLrPD%2F%2F20l2yDlqB%2BUI7JoJxLYQjVnEFFM0dXkrX1BjeD%2FgsQQDHIG0fezJcePozGa7%2FI%2FAPnHoQKvu9FM09%2FI2N3vBvqm%2BUX8Ny8IX2UeZ9o3g0Y0b7gGVlEjy0qEJacjMFTLrTZtAp9sADvLPCAn%2FDPIeX%2B4RZK%2FBbtG973CtIKNF54dLHAe7K3k16Pdhem72PJy35bkx0PFccqyMpBg%2B1cMmR%2BviEST%2Frb5IM8JntyBjCFboL1B%2B9n9JiSHL4DGher5A%2BHRel4IBML9OiET51mVCG%2BhchQ2ranQL1byxnAeGPzKE7dfon004ld8hCBIOy%2B2a9j96L7A%2BUsWAjP0njgHLfsPbDKmkogu6ydGuZ%2BLpQd1srhOpRxJ%2BuN9fYNKOqZyXLCmiGOD4L40rr4cvTuYos9N7vhVs%2Bu8TA%2BoLKv44foeAAGCUWnIg41N%2Fo34eUiVGhxG%2BTbaLkPctky2olbXiBBMe8o1PEl3YrbzDKiHgkvxU1bZZJfqLNmuizdNQIdiu8wofLuvAY6pgGxTZ2hlucKd%2B0dOZxbeL8QiLCRHGEiBmaA2SbuqwFlEKs8TRKZ9JNDLVD3JWWSAFSR%2BNeJG1WW%2F0pV4EU2mrQLXdGLSNKKS7mR2Ioli3C%2BX6Z2HtB3CTceNDyopb7SJ%2BRuuzGU13fLMe%2F0kb0OtwhLCO68zai5NXcUAvaqjLEsMiHNFhOIHIT9%2BHxHFwyZaE2YtTeIqEz5UkRa%2BzU3%2B5zmAMsfeWMD&X-Amz-Signature=881dcec8a4168c579d0d3543389c4de704b34856c947267df60317480c55e642&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623BC56Z3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBrbIWVquKCBspxX%2F5%2F4rpngzHWErF4Nmqx41bzQGDnMAiBLoLZ2HHKa64At5%2BjzHcqBSBSWSNXKt9GbxvN%2FMWpMLyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNC%2FJYJ9KDRBw%2FZFCKtwDaPReOlYpfdXRLGaNVAxj%2FxC0KOQ4RHrMkhJPH8mYFfZZHWM9G%2FyXXtLSBNfCK0NrhB%2BLuIxiJbs84akQpiRXK7fCttGUc3XEDZxDXSfKZw2%2Bvlyvj9LeLrPD%2F%2F20l2yDlqB%2BUI7JoJxLYQjVnEFFM0dXkrX1BjeD%2FgsQQDHIG0fezJcePozGa7%2FI%2FAPnHoQKvu9FM09%2FI2N3vBvqm%2BUX8Ny8IX2UeZ9o3g0Y0b7gGVlEjy0qEJacjMFTLrTZtAp9sADvLPCAn%2FDPIeX%2B4RZK%2FBbtG973CtIKNF54dLHAe7K3k16Pdhem72PJy35bkx0PFccqyMpBg%2B1cMmR%2BviEST%2Frb5IM8JntyBjCFboL1B%2B9n9JiSHL4DGher5A%2BHRel4IBML9OiET51mVCG%2BhchQ2ranQL1byxnAeGPzKE7dfon004ld8hCBIOy%2B2a9j96L7A%2BUsWAjP0njgHLfsPbDKmkogu6ydGuZ%2BLpQd1srhOpRxJ%2BuN9fYNKOqZyXLCmiGOD4L40rr4cvTuYos9N7vhVs%2Bu8TA%2BoLKv44foeAAGCUWnIg41N%2Fo34eUiVGhxG%2BTbaLkPctky2olbXiBBMe8o1PEl3YrbzDKiHgkvxU1bZZJfqLNmuizdNQIdiu8wofLuvAY6pgGxTZ2hlucKd%2B0dOZxbeL8QiLCRHGEiBmaA2SbuqwFlEKs8TRKZ9JNDLVD3JWWSAFSR%2BNeJG1WW%2F0pV4EU2mrQLXdGLSNKKS7mR2Ioli3C%2BX6Z2HtB3CTceNDyopb7SJ%2BRuuzGU13fLMe%2F0kb0OtwhLCO68zai5NXcUAvaqjLEsMiHNFhOIHIT9%2BHxHFwyZaE2YtTeIqEz5UkRa%2BzU3%2B5zmAMsfeWMD&X-Amz-Signature=152a06fbe069204a63997645da812941fbbe5c70f3a6efa49cdc33d5325d791b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623BC56Z3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBrbIWVquKCBspxX%2F5%2F4rpngzHWErF4Nmqx41bzQGDnMAiBLoLZ2HHKa64At5%2BjzHcqBSBSWSNXKt9GbxvN%2FMWpMLyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNC%2FJYJ9KDRBw%2FZFCKtwDaPReOlYpfdXRLGaNVAxj%2FxC0KOQ4RHrMkhJPH8mYFfZZHWM9G%2FyXXtLSBNfCK0NrhB%2BLuIxiJbs84akQpiRXK7fCttGUc3XEDZxDXSfKZw2%2Bvlyvj9LeLrPD%2F%2F20l2yDlqB%2BUI7JoJxLYQjVnEFFM0dXkrX1BjeD%2FgsQQDHIG0fezJcePozGa7%2FI%2FAPnHoQKvu9FM09%2FI2N3vBvqm%2BUX8Ny8IX2UeZ9o3g0Y0b7gGVlEjy0qEJacjMFTLrTZtAp9sADvLPCAn%2FDPIeX%2B4RZK%2FBbtG973CtIKNF54dLHAe7K3k16Pdhem72PJy35bkx0PFccqyMpBg%2B1cMmR%2BviEST%2Frb5IM8JntyBjCFboL1B%2B9n9JiSHL4DGher5A%2BHRel4IBML9OiET51mVCG%2BhchQ2ranQL1byxnAeGPzKE7dfon004ld8hCBIOy%2B2a9j96L7A%2BUsWAjP0njgHLfsPbDKmkogu6ydGuZ%2BLpQd1srhOpRxJ%2BuN9fYNKOqZyXLCmiGOD4L40rr4cvTuYos9N7vhVs%2Bu8TA%2BoLKv44foeAAGCUWnIg41N%2Fo34eUiVGhxG%2BTbaLkPctky2olbXiBBMe8o1PEl3YrbzDKiHgkvxU1bZZJfqLNmuizdNQIdiu8wofLuvAY6pgGxTZ2hlucKd%2B0dOZxbeL8QiLCRHGEiBmaA2SbuqwFlEKs8TRKZ9JNDLVD3JWWSAFSR%2BNeJG1WW%2F0pV4EU2mrQLXdGLSNKKS7mR2Ioli3C%2BX6Z2HtB3CTceNDyopb7SJ%2BRuuzGU13fLMe%2F0kb0OtwhLCO68zai5NXcUAvaqjLEsMiHNFhOIHIT9%2BHxHFwyZaE2YtTeIqEz5UkRa%2BzU3%2B5zmAMsfeWMD&X-Amz-Signature=308ebe558c2c2981d56cffffdd6e28d84f3658a388b67e68777d74de0968bf2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623BC56Z3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBrbIWVquKCBspxX%2F5%2F4rpngzHWErF4Nmqx41bzQGDnMAiBLoLZ2HHKa64At5%2BjzHcqBSBSWSNXKt9GbxvN%2FMWpMLyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNC%2FJYJ9KDRBw%2FZFCKtwDaPReOlYpfdXRLGaNVAxj%2FxC0KOQ4RHrMkhJPH8mYFfZZHWM9G%2FyXXtLSBNfCK0NrhB%2BLuIxiJbs84akQpiRXK7fCttGUc3XEDZxDXSfKZw2%2Bvlyvj9LeLrPD%2F%2F20l2yDlqB%2BUI7JoJxLYQjVnEFFM0dXkrX1BjeD%2FgsQQDHIG0fezJcePozGa7%2FI%2FAPnHoQKvu9FM09%2FI2N3vBvqm%2BUX8Ny8IX2UeZ9o3g0Y0b7gGVlEjy0qEJacjMFTLrTZtAp9sADvLPCAn%2FDPIeX%2B4RZK%2FBbtG973CtIKNF54dLHAe7K3k16Pdhem72PJy35bkx0PFccqyMpBg%2B1cMmR%2BviEST%2Frb5IM8JntyBjCFboL1B%2B9n9JiSHL4DGher5A%2BHRel4IBML9OiET51mVCG%2BhchQ2ranQL1byxnAeGPzKE7dfon004ld8hCBIOy%2B2a9j96L7A%2BUsWAjP0njgHLfsPbDKmkogu6ydGuZ%2BLpQd1srhOpRxJ%2BuN9fYNKOqZyXLCmiGOD4L40rr4cvTuYos9N7vhVs%2Bu8TA%2BoLKv44foeAAGCUWnIg41N%2Fo34eUiVGhxG%2BTbaLkPctky2olbXiBBMe8o1PEl3YrbzDKiHgkvxU1bZZJfqLNmuizdNQIdiu8wofLuvAY6pgGxTZ2hlucKd%2B0dOZxbeL8QiLCRHGEiBmaA2SbuqwFlEKs8TRKZ9JNDLVD3JWWSAFSR%2BNeJG1WW%2F0pV4EU2mrQLXdGLSNKKS7mR2Ioli3C%2BX6Z2HtB3CTceNDyopb7SJ%2BRuuzGU13fLMe%2F0kb0OtwhLCO68zai5NXcUAvaqjLEsMiHNFhOIHIT9%2BHxHFwyZaE2YtTeIqEz5UkRa%2BzU3%2B5zmAMsfeWMD&X-Amz-Signature=325c6e8c8924db1d45295993e4070eee401149da809b3c4acee3d3520ff24984&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623BC56Z3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBrbIWVquKCBspxX%2F5%2F4rpngzHWErF4Nmqx41bzQGDnMAiBLoLZ2HHKa64At5%2BjzHcqBSBSWSNXKt9GbxvN%2FMWpMLyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNC%2FJYJ9KDRBw%2FZFCKtwDaPReOlYpfdXRLGaNVAxj%2FxC0KOQ4RHrMkhJPH8mYFfZZHWM9G%2FyXXtLSBNfCK0NrhB%2BLuIxiJbs84akQpiRXK7fCttGUc3XEDZxDXSfKZw2%2Bvlyvj9LeLrPD%2F%2F20l2yDlqB%2BUI7JoJxLYQjVnEFFM0dXkrX1BjeD%2FgsQQDHIG0fezJcePozGa7%2FI%2FAPnHoQKvu9FM09%2FI2N3vBvqm%2BUX8Ny8IX2UeZ9o3g0Y0b7gGVlEjy0qEJacjMFTLrTZtAp9sADvLPCAn%2FDPIeX%2B4RZK%2FBbtG973CtIKNF54dLHAe7K3k16Pdhem72PJy35bkx0PFccqyMpBg%2B1cMmR%2BviEST%2Frb5IM8JntyBjCFboL1B%2B9n9JiSHL4DGher5A%2BHRel4IBML9OiET51mVCG%2BhchQ2ranQL1byxnAeGPzKE7dfon004ld8hCBIOy%2B2a9j96L7A%2BUsWAjP0njgHLfsPbDKmkogu6ydGuZ%2BLpQd1srhOpRxJ%2BuN9fYNKOqZyXLCmiGOD4L40rr4cvTuYos9N7vhVs%2Bu8TA%2BoLKv44foeAAGCUWnIg41N%2Fo34eUiVGhxG%2BTbaLkPctky2olbXiBBMe8o1PEl3YrbzDKiHgkvxU1bZZJfqLNmuizdNQIdiu8wofLuvAY6pgGxTZ2hlucKd%2B0dOZxbeL8QiLCRHGEiBmaA2SbuqwFlEKs8TRKZ9JNDLVD3JWWSAFSR%2BNeJG1WW%2F0pV4EU2mrQLXdGLSNKKS7mR2Ioli3C%2BX6Z2HtB3CTceNDyopb7SJ%2BRuuzGU13fLMe%2F0kb0OtwhLCO68zai5NXcUAvaqjLEsMiHNFhOIHIT9%2BHxHFwyZaE2YtTeIqEz5UkRa%2BzU3%2B5zmAMsfeWMD&X-Amz-Signature=323070fe6ea8e437c0ab487df1cf59eaa619bb3455152a5b427c756e2b580c7d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623BC56Z3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBrbIWVquKCBspxX%2F5%2F4rpngzHWErF4Nmqx41bzQGDnMAiBLoLZ2HHKa64At5%2BjzHcqBSBSWSNXKt9GbxvN%2FMWpMLyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNC%2FJYJ9KDRBw%2FZFCKtwDaPReOlYpfdXRLGaNVAxj%2FxC0KOQ4RHrMkhJPH8mYFfZZHWM9G%2FyXXtLSBNfCK0NrhB%2BLuIxiJbs84akQpiRXK7fCttGUc3XEDZxDXSfKZw2%2Bvlyvj9LeLrPD%2F%2F20l2yDlqB%2BUI7JoJxLYQjVnEFFM0dXkrX1BjeD%2FgsQQDHIG0fezJcePozGa7%2FI%2FAPnHoQKvu9FM09%2FI2N3vBvqm%2BUX8Ny8IX2UeZ9o3g0Y0b7gGVlEjy0qEJacjMFTLrTZtAp9sADvLPCAn%2FDPIeX%2B4RZK%2FBbtG973CtIKNF54dLHAe7K3k16Pdhem72PJy35bkx0PFccqyMpBg%2B1cMmR%2BviEST%2Frb5IM8JntyBjCFboL1B%2B9n9JiSHL4DGher5A%2BHRel4IBML9OiET51mVCG%2BhchQ2ranQL1byxnAeGPzKE7dfon004ld8hCBIOy%2B2a9j96L7A%2BUsWAjP0njgHLfsPbDKmkogu6ydGuZ%2BLpQd1srhOpRxJ%2BuN9fYNKOqZyXLCmiGOD4L40rr4cvTuYos9N7vhVs%2Bu8TA%2BoLKv44foeAAGCUWnIg41N%2Fo34eUiVGhxG%2BTbaLkPctky2olbXiBBMe8o1PEl3YrbzDKiHgkvxU1bZZJfqLNmuizdNQIdiu8wofLuvAY6pgGxTZ2hlucKd%2B0dOZxbeL8QiLCRHGEiBmaA2SbuqwFlEKs8TRKZ9JNDLVD3JWWSAFSR%2BNeJG1WW%2F0pV4EU2mrQLXdGLSNKKS7mR2Ioli3C%2BX6Z2HtB3CTceNDyopb7SJ%2BRuuzGU13fLMe%2F0kb0OtwhLCO68zai5NXcUAvaqjLEsMiHNFhOIHIT9%2BHxHFwyZaE2YtTeIqEz5UkRa%2BzU3%2B5zmAMsfeWMD&X-Amz-Signature=0ea241e1b122a3c339fa6e1f6fe3e45fa6eb61af30c8c3e4d58031502efc8110&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623BC56Z3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBrbIWVquKCBspxX%2F5%2F4rpngzHWErF4Nmqx41bzQGDnMAiBLoLZ2HHKa64At5%2BjzHcqBSBSWSNXKt9GbxvN%2FMWpMLyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNC%2FJYJ9KDRBw%2FZFCKtwDaPReOlYpfdXRLGaNVAxj%2FxC0KOQ4RHrMkhJPH8mYFfZZHWM9G%2FyXXtLSBNfCK0NrhB%2BLuIxiJbs84akQpiRXK7fCttGUc3XEDZxDXSfKZw2%2Bvlyvj9LeLrPD%2F%2F20l2yDlqB%2BUI7JoJxLYQjVnEFFM0dXkrX1BjeD%2FgsQQDHIG0fezJcePozGa7%2FI%2FAPnHoQKvu9FM09%2FI2N3vBvqm%2BUX8Ny8IX2UeZ9o3g0Y0b7gGVlEjy0qEJacjMFTLrTZtAp9sADvLPCAn%2FDPIeX%2B4RZK%2FBbtG973CtIKNF54dLHAe7K3k16Pdhem72PJy35bkx0PFccqyMpBg%2B1cMmR%2BviEST%2Frb5IM8JntyBjCFboL1B%2B9n9JiSHL4DGher5A%2BHRel4IBML9OiET51mVCG%2BhchQ2ranQL1byxnAeGPzKE7dfon004ld8hCBIOy%2B2a9j96L7A%2BUsWAjP0njgHLfsPbDKmkogu6ydGuZ%2BLpQd1srhOpRxJ%2BuN9fYNKOqZyXLCmiGOD4L40rr4cvTuYos9N7vhVs%2Bu8TA%2BoLKv44foeAAGCUWnIg41N%2Fo34eUiVGhxG%2BTbaLkPctky2olbXiBBMe8o1PEl3YrbzDKiHgkvxU1bZZJfqLNmuizdNQIdiu8wofLuvAY6pgGxTZ2hlucKd%2B0dOZxbeL8QiLCRHGEiBmaA2SbuqwFlEKs8TRKZ9JNDLVD3JWWSAFSR%2BNeJG1WW%2F0pV4EU2mrQLXdGLSNKKS7mR2Ioli3C%2BX6Z2HtB3CTceNDyopb7SJ%2BRuuzGU13fLMe%2F0kb0OtwhLCO68zai5NXcUAvaqjLEsMiHNFhOIHIT9%2BHxHFwyZaE2YtTeIqEz5UkRa%2BzU3%2B5zmAMsfeWMD&X-Amz-Signature=6cee05bed63a647216b1322fa940d183abc2391d9dac514167a76fe7ba42bea4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623BC56Z3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBrbIWVquKCBspxX%2F5%2F4rpngzHWErF4Nmqx41bzQGDnMAiBLoLZ2HHKa64At5%2BjzHcqBSBSWSNXKt9GbxvN%2FMWpMLyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNC%2FJYJ9KDRBw%2FZFCKtwDaPReOlYpfdXRLGaNVAxj%2FxC0KOQ4RHrMkhJPH8mYFfZZHWM9G%2FyXXtLSBNfCK0NrhB%2BLuIxiJbs84akQpiRXK7fCttGUc3XEDZxDXSfKZw2%2Bvlyvj9LeLrPD%2F%2F20l2yDlqB%2BUI7JoJxLYQjVnEFFM0dXkrX1BjeD%2FgsQQDHIG0fezJcePozGa7%2FI%2FAPnHoQKvu9FM09%2FI2N3vBvqm%2BUX8Ny8IX2UeZ9o3g0Y0b7gGVlEjy0qEJacjMFTLrTZtAp9sADvLPCAn%2FDPIeX%2B4RZK%2FBbtG973CtIKNF54dLHAe7K3k16Pdhem72PJy35bkx0PFccqyMpBg%2B1cMmR%2BviEST%2Frb5IM8JntyBjCFboL1B%2B9n9JiSHL4DGher5A%2BHRel4IBML9OiET51mVCG%2BhchQ2ranQL1byxnAeGPzKE7dfon004ld8hCBIOy%2B2a9j96L7A%2BUsWAjP0njgHLfsPbDKmkogu6ydGuZ%2BLpQd1srhOpRxJ%2BuN9fYNKOqZyXLCmiGOD4L40rr4cvTuYos9N7vhVs%2Bu8TA%2BoLKv44foeAAGCUWnIg41N%2Fo34eUiVGhxG%2BTbaLkPctky2olbXiBBMe8o1PEl3YrbzDKiHgkvxU1bZZJfqLNmuizdNQIdiu8wofLuvAY6pgGxTZ2hlucKd%2B0dOZxbeL8QiLCRHGEiBmaA2SbuqwFlEKs8TRKZ9JNDLVD3JWWSAFSR%2BNeJG1WW%2F0pV4EU2mrQLXdGLSNKKS7mR2Ioli3C%2BX6Z2HtB3CTceNDyopb7SJ%2BRuuzGU13fLMe%2F0kb0OtwhLCO68zai5NXcUAvaqjLEsMiHNFhOIHIT9%2BHxHFwyZaE2YtTeIqEz5UkRa%2BzU3%2B5zmAMsfeWMD&X-Amz-Signature=575d4df1a13d25e17e6526d7e216d7cf2271a00b56de24cee5ad138af551a836&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLK6JK7R%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwhHFq7Bo%2BpoCCDzQ8ndgY7Ro2sWvNyYmO8W8zFTwaeAiBChkZwz%2Ff6443FHFXmo20aqA5xqXNmfaLjxzkYbzZJoiqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM13gUhRc9s%2B5iMklOKtwDPBXJ0Bf88ViCVlfM8WmSWUaj3S6STT9CjV%2Bb8XT9rS3b4j0J0Wiq9Vs2VG6MkFXm9VhGJAGqhUKRFLnfdN6MlduGPwk%2BCeWaNlNbpfKrh3oQ%2FEHINfld%2F6CQV6yzZVXEAykcGm8%2B%2FiNBubiX5rBcH5YrGOM0tdGgoNkpqjNzv%2Fs401%2Bi8xteXsHCJlNzSx3bm7PAT40HDQ7sbJPzf4kFmuOeqKdA%2FoTYHL7zc%2F7KcavskVGrqK2MsgF6B%2BLN2dDDRZTXmeNHuIKf1xRMf6wfNeHpvBegvAEmy2oD7ZPT3uXKEPdQ%2F5vLgpHaIYnrUPqF5NvBvDj0vWpdc93QR6yFwpoZjzmZVdLMS2BkSB29ze3cOwvO6Kvgw0iXIAIxjvFWYL5Y2WtobK9Enf4WmA33vwFiwHiW6zR%2BO20QvFGv8cBXmX%2F7nuVwcThIe%2Bn76I09dwHuCTF7cYDI62yqxgp46mnx5iUgVC7cFhdrvaAYZQvyPB1AxVzQd0FZe1h5bKSJSeW22cemL%2BwBwtEMS4QyeVWLA9IpAnwfvy9k6x9cie0JZnvZc2XdH2sqfg%2FrYP6K%2BsSIKCE2nBGSdbdSY5AvZH0%2FYgbJ4%2FgFTpfPkaZwYDeuqaf4SrAhUwYY0N8wk%2FPuvAY6pgHhv3CRHQjnC%2BR%2BaxD%2BHp1n47exTKGH1xwBTvrNmDA5Dbul9S0GZ7OQVYcuGGEgJyvsAgI6RhkL1XMy1gmUeLeNUpMWyQZoXDY%2BHI6lzu%2FVdgOmfjOIQEr3QvOqXi0aHJJMfDz6CyYgDCNi%2BA64KHUiiI4thm1zdHqKrh13ekHVi%2BG%2BRAcO1SSlhAOE%2B%2FG7gU59FK%2B5ff1B1T0qc2oseCWSs4rBLX%2B3&X-Amz-Signature=cf93dda28e6cc8db48320758c54c657cc3b5bcd7d9a697f2190b04ce31dc90bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVRTAD7M%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCXbVdXTo3B9fLJL7%2BCjhaxXEkrtScwgJDPXQEj6ATjyAIgC%2FopMthUU0o7rSHjvIfJHfKBYRhCKYSanmXvRNnfcygqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNMgE3jfi%2F6j8GrhCircA7bP%2FVR5%2B8PPSgYJFo4ZUX%2Fg%2Baey38D3qLYqPmnvxlwJR3cbGbcT%2FznyHHYsI4tYXqjb1MuFQaPft7VU61Qej%2FiaHEa9KgX%2FcPrRniHJz9k2jHdGBNr%2FxrbDVcdg0H1cLpWIhbC%2BmhcA9tBtoHCk8d8SL3XJ9XgkFy%2FpepVVulOJORZEOoOLFGvcAhzyC3z01YMtxoP%2FVH%2B%2Fa%2BjD1hkWob7lJlbvur6J4kw58izfn4wVqdHPHUjNfJETSG9MinRwp%2FisUcMzXHFXD3x%2Fx1gIWHleNAGeP2%2BUwOVZU9obHMNL35TcLKvhfm07ba399VGKts%2FUOsI1q56%2B%2BNsL481QRRIdBIP0iKJ%2FumtWnCxH6nCulCBBlSI2qmjpjk3j8TxXis%2B2Dm3YkpbP4IZF5zMUAEOduRq95Ss%2FlyYy3HHAC9MhHp9HcH3ZwM5BRYj7VOvHsMTeC%2FSAj9FUSJoImIWOdGEBWjiJ05mkBYlnAzmGjwrcppWzxkLGl2csgkeTnasrYyx8wGkKWPHjaoHPygCg5dRhyCY3Zf0PMZ7TDn0ARiUKGiE0bNkPFtDNRru49bKBvFB0ClyvnDpxqetCiMU4t39zObdVLNEkQS7RS90h9elvUgZFRv%2BP5DoOLvFKMLPy7rwGOqUB2S3A4vN1jbBBellqWZb9hpfMViEk6JOzzle836vGBbaIadgkXRtqKz717mV1hUagH7Jkv8p3MOMlsNMeP8DJMKmxLUYBSWy3HlNZDubZoyAEKFtmlXu%2BBsKIzovfgvPAFa%2BeOvYtC0uKro0JgGA1TLyiaoSAElC9gsBDLoMTBifVhDi%2BQmeOlZzohYIYd14gXUORdT0zV6cRmuoyqivfBuk%2BFsdZ&X-Amz-Signature=e02cc06fecd8394422450ae54268928f614bda8c77379f56fc3654a1fa361bd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PJPZ5FT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGqS1GoaTdKI9YXn6qvUj59WwFNuAWPrw3cT7MwSoeKjAiEA1vBiDOUdEuwjEb6ojva%2FOvoelbs9SvI4zdzSsqykK%2BAqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL9kknRxmeEqGqu4PCrcA7fMy88EgiVkvmcVsOxIkuR5JeZxryMEy1QJ%2BtPMRRc%2Ft3u8iy5gpgDVQKYDVqsp6qpobLD9KKo6DHGXreb2oJ5vBnxrHJWzeJ9zep%2BEvv3o%2BkmZufgLOMNsieCdg0yLgdfKd7lkwQdwj6xSN4Ljt37DHOgBloogZ03tiGfSr3Idfs6rnHIHiyATIPnGlGseTegIDiOO51QGY9Lb4odxMWKwPmvKbgXsBVvDs8yxY5HRscWC5YZhvjXFl2ihfFPClZSgxLslOSFX%2B2cIdccylaERWtC5%2FS8mj0lQqcRdGLqLWAcIw6yX2EHFonutSX4LS0xtT7QSbtDXHJhJ9E%2FUmi3w4Mq1IQr9tdc3apwWEuNljlghtgyMohlwcaUrFhY4aY7yJgkU2PXwbNqsX%2BR4%2ByQ0yrHwTAgxqTYJh981cSE7yH1N63TXeinROBIpbHqfBqSrrcDmxzvNWmUnpgZcGOxb4KTIa02OMkRbGNRK6cGTKRIPsiyRhkCeJDeuNDHowNE608%2FkFoxfFoHsqB7Z8BwIXs00D2IIhncH7x73XLhlD35EuQ74q9oLm48WRZBaF5PdcQxIyvCNyZjMdhso%2Bu3jy5xpEFST1DS45eP6AoQEwLSf9Vknd%2B1Vaaf4MJ7y7rwGOqUBZKspZqKgfzN%2BXFJTybyK0NLqLqsimjKhPmgfDybb1KiVR4xu8mQhNzcCUekH4D9ZrSMaIehgb7%2B1pJDCvZH1G4olXekOLALnxaDUGMMxUugV60Q3foytGZy5o5m%2B5PaMBRx%2FmLjNV4weP5JlH3x5U2rGNCe4ETQRDk3IQy3z4YQvd2dfbQppKWhjF%2BDbcUoPNd%2FwyhQNhI8cWcD7RN6BRAK321z1&X-Amz-Signature=faffca84d991eccf3edec61b2ff9be4435297ba9313ebe8e43396938800e8a14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PJPZ5FT%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGqS1GoaTdKI9YXn6qvUj59WwFNuAWPrw3cT7MwSoeKjAiEA1vBiDOUdEuwjEb6ojva%2FOvoelbs9SvI4zdzSsqykK%2BAqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL9kknRxmeEqGqu4PCrcA7fMy88EgiVkvmcVsOxIkuR5JeZxryMEy1QJ%2BtPMRRc%2Ft3u8iy5gpgDVQKYDVqsp6qpobLD9KKo6DHGXreb2oJ5vBnxrHJWzeJ9zep%2BEvv3o%2BkmZufgLOMNsieCdg0yLgdfKd7lkwQdwj6xSN4Ljt37DHOgBloogZ03tiGfSr3Idfs6rnHIHiyATIPnGlGseTegIDiOO51QGY9Lb4odxMWKwPmvKbgXsBVvDs8yxY5HRscWC5YZhvjXFl2ihfFPClZSgxLslOSFX%2B2cIdccylaERWtC5%2FS8mj0lQqcRdGLqLWAcIw6yX2EHFonutSX4LS0xtT7QSbtDXHJhJ9E%2FUmi3w4Mq1IQr9tdc3apwWEuNljlghtgyMohlwcaUrFhY4aY7yJgkU2PXwbNqsX%2BR4%2ByQ0yrHwTAgxqTYJh981cSE7yH1N63TXeinROBIpbHqfBqSrrcDmxzvNWmUnpgZcGOxb4KTIa02OMkRbGNRK6cGTKRIPsiyRhkCeJDeuNDHowNE608%2FkFoxfFoHsqB7Z8BwIXs00D2IIhncH7x73XLhlD35EuQ74q9oLm48WRZBaF5PdcQxIyvCNyZjMdhso%2Bu3jy5xpEFST1DS45eP6AoQEwLSf9Vknd%2B1Vaaf4MJ7y7rwGOqUBZKspZqKgfzN%2BXFJTybyK0NLqLqsimjKhPmgfDybb1KiVR4xu8mQhNzcCUekH4D9ZrSMaIehgb7%2B1pJDCvZH1G4olXekOLALnxaDUGMMxUugV60Q3foytGZy5o5m%2B5PaMBRx%2FmLjNV4weP5JlH3x5U2rGNCe4ETQRDk3IQy3z4YQvd2dfbQppKWhjF%2BDbcUoPNd%2FwyhQNhI8cWcD7RN6BRAK321z1&X-Amz-Signature=61f4763b7c8c9c55beab58fc7f780b7c832413644c48c6568cfba6d0c92ad970&X-Amz-SignedHeaders=host&x-id=GetObject)
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
