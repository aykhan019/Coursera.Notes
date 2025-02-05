

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677GDIYK3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDBeBp2fdNhdSiA3TUJVvobC9z5PxPPjn5Zd09qW%2F2OMgIgORnCn5gQL8%2B5WlceHaA4%2FBEIpcWOd6ljaTY6k7rfZZYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDDgx7EJ7GydhvjCb1CrcA%2BVgKa%2Fr4i7RWg3iv%2F1Gd0DvbODOjMyuMeJe0zgdL2NOnVhicLsMCSl52pJSeFGVzIL7z6tykYvztasPSoga1j%2BkIwDn2F1b0in0UeYhvsce8fp6HV2OSUIymnNlp3lMYQZUswGvFSs4OcO%2FZ3aNSDIZyAYmESwJRJhA17Lej%2BVxSJNBFi3xsJwdj3%2F%2BC3BgTN%2FzSuJDVKk%2BAZ%2BkvHVRa5h2Ni7BNinkHmNrYuC04wZhlVaxFrFsYag38pl29214HgMGq9nAQFg9C645Jqa8kLnBblC4t6KFeU992f%2BK3bQ7vUmFPioM3rvZvsV3BdNvpvAhKqeX9Khhg4O6ov2Iy0vPbgdgD%2FG%2FoqojrEKzX9Ozsx4oDMPtEcoFPjn7Na6RH9rr3G%2Bd6bXgp%2B6eT1FjBk6FuJZRMeLWQEL9aW0G8JBwEcFhIUFkCcWwaW%2BWMljD3xz1pJEGe9%2FwExBuPJDPO%2Bo73ZVYH0JeHtRPEBqAvN%2F2jPtdcuuOv5XyHHoEO8Y0Y0qF0cOEnJW0O%2FGrtrPuyQAG3diCyiVg13BhZ8W1hQp5Z3bqJTNn1L7msqDuZchY5yJ4sYaAS%2BYraxidjZ%2BqFGmDfqt%2FAPVh0GqTuxq1QksfWb%2F561z22rV%2BOYpzMMj5i70GOqUBMIXU5VX0jS4VWzArCHulGXBZocAMoRpneEhFRqo5zQ5fIG1%2BR7FII9yBdfNSts%2ByGl%2F5kpf8mIq%2BZYmA0JCRrE8MrPbiep2qljo%2FYSxaeXwoVRZsYEybd8sXqbyvCB7jPuF1igk8ZN71vhRCZVY2TK2354110VSS%2BAsnrCjgi51GBoTWJ4Doaonzx1bpW%2FRtjgQHlQbZTR9np2sv13rgi%2B0g85mT&X-Amz-Signature=95ad8e3d1271f5cae44568889307b6903a8ae77b3890c0581d8ec8f478b7c537&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677GDIYK3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDBeBp2fdNhdSiA3TUJVvobC9z5PxPPjn5Zd09qW%2F2OMgIgORnCn5gQL8%2B5WlceHaA4%2FBEIpcWOd6ljaTY6k7rfZZYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDDgx7EJ7GydhvjCb1CrcA%2BVgKa%2Fr4i7RWg3iv%2F1Gd0DvbODOjMyuMeJe0zgdL2NOnVhicLsMCSl52pJSeFGVzIL7z6tykYvztasPSoga1j%2BkIwDn2F1b0in0UeYhvsce8fp6HV2OSUIymnNlp3lMYQZUswGvFSs4OcO%2FZ3aNSDIZyAYmESwJRJhA17Lej%2BVxSJNBFi3xsJwdj3%2F%2BC3BgTN%2FzSuJDVKk%2BAZ%2BkvHVRa5h2Ni7BNinkHmNrYuC04wZhlVaxFrFsYag38pl29214HgMGq9nAQFg9C645Jqa8kLnBblC4t6KFeU992f%2BK3bQ7vUmFPioM3rvZvsV3BdNvpvAhKqeX9Khhg4O6ov2Iy0vPbgdgD%2FG%2FoqojrEKzX9Ozsx4oDMPtEcoFPjn7Na6RH9rr3G%2Bd6bXgp%2B6eT1FjBk6FuJZRMeLWQEL9aW0G8JBwEcFhIUFkCcWwaW%2BWMljD3xz1pJEGe9%2FwExBuPJDPO%2Bo73ZVYH0JeHtRPEBqAvN%2F2jPtdcuuOv5XyHHoEO8Y0Y0qF0cOEnJW0O%2FGrtrPuyQAG3diCyiVg13BhZ8W1hQp5Z3bqJTNn1L7msqDuZchY5yJ4sYaAS%2BYraxidjZ%2BqFGmDfqt%2FAPVh0GqTuxq1QksfWb%2F561z22rV%2BOYpzMMj5i70GOqUBMIXU5VX0jS4VWzArCHulGXBZocAMoRpneEhFRqo5zQ5fIG1%2BR7FII9yBdfNSts%2ByGl%2F5kpf8mIq%2BZYmA0JCRrE8MrPbiep2qljo%2FYSxaeXwoVRZsYEybd8sXqbyvCB7jPuF1igk8ZN71vhRCZVY2TK2354110VSS%2BAsnrCjgi51GBoTWJ4Doaonzx1bpW%2FRtjgQHlQbZTR9np2sv13rgi%2B0g85mT&X-Amz-Signature=563bd87298185997bae99ae0c7ad5bb97ab38dea9a1bc85ce4cd02e59fd47781&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677GDIYK3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDBeBp2fdNhdSiA3TUJVvobC9z5PxPPjn5Zd09qW%2F2OMgIgORnCn5gQL8%2B5WlceHaA4%2FBEIpcWOd6ljaTY6k7rfZZYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDDgx7EJ7GydhvjCb1CrcA%2BVgKa%2Fr4i7RWg3iv%2F1Gd0DvbODOjMyuMeJe0zgdL2NOnVhicLsMCSl52pJSeFGVzIL7z6tykYvztasPSoga1j%2BkIwDn2F1b0in0UeYhvsce8fp6HV2OSUIymnNlp3lMYQZUswGvFSs4OcO%2FZ3aNSDIZyAYmESwJRJhA17Lej%2BVxSJNBFi3xsJwdj3%2F%2BC3BgTN%2FzSuJDVKk%2BAZ%2BkvHVRa5h2Ni7BNinkHmNrYuC04wZhlVaxFrFsYag38pl29214HgMGq9nAQFg9C645Jqa8kLnBblC4t6KFeU992f%2BK3bQ7vUmFPioM3rvZvsV3BdNvpvAhKqeX9Khhg4O6ov2Iy0vPbgdgD%2FG%2FoqojrEKzX9Ozsx4oDMPtEcoFPjn7Na6RH9rr3G%2Bd6bXgp%2B6eT1FjBk6FuJZRMeLWQEL9aW0G8JBwEcFhIUFkCcWwaW%2BWMljD3xz1pJEGe9%2FwExBuPJDPO%2Bo73ZVYH0JeHtRPEBqAvN%2F2jPtdcuuOv5XyHHoEO8Y0Y0qF0cOEnJW0O%2FGrtrPuyQAG3diCyiVg13BhZ8W1hQp5Z3bqJTNn1L7msqDuZchY5yJ4sYaAS%2BYraxidjZ%2BqFGmDfqt%2FAPVh0GqTuxq1QksfWb%2F561z22rV%2BOYpzMMj5i70GOqUBMIXU5VX0jS4VWzArCHulGXBZocAMoRpneEhFRqo5zQ5fIG1%2BR7FII9yBdfNSts%2ByGl%2F5kpf8mIq%2BZYmA0JCRrE8MrPbiep2qljo%2FYSxaeXwoVRZsYEybd8sXqbyvCB7jPuF1igk8ZN71vhRCZVY2TK2354110VSS%2BAsnrCjgi51GBoTWJ4Doaonzx1bpW%2FRtjgQHlQbZTR9np2sv13rgi%2B0g85mT&X-Amz-Signature=cbec6d7f5ceec0130fe0479be9d928bc44addf9460e70b742f670cb31e6947c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677GDIYK3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDBeBp2fdNhdSiA3TUJVvobC9z5PxPPjn5Zd09qW%2F2OMgIgORnCn5gQL8%2B5WlceHaA4%2FBEIpcWOd6ljaTY6k7rfZZYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDDgx7EJ7GydhvjCb1CrcA%2BVgKa%2Fr4i7RWg3iv%2F1Gd0DvbODOjMyuMeJe0zgdL2NOnVhicLsMCSl52pJSeFGVzIL7z6tykYvztasPSoga1j%2BkIwDn2F1b0in0UeYhvsce8fp6HV2OSUIymnNlp3lMYQZUswGvFSs4OcO%2FZ3aNSDIZyAYmESwJRJhA17Lej%2BVxSJNBFi3xsJwdj3%2F%2BC3BgTN%2FzSuJDVKk%2BAZ%2BkvHVRa5h2Ni7BNinkHmNrYuC04wZhlVaxFrFsYag38pl29214HgMGq9nAQFg9C645Jqa8kLnBblC4t6KFeU992f%2BK3bQ7vUmFPioM3rvZvsV3BdNvpvAhKqeX9Khhg4O6ov2Iy0vPbgdgD%2FG%2FoqojrEKzX9Ozsx4oDMPtEcoFPjn7Na6RH9rr3G%2Bd6bXgp%2B6eT1FjBk6FuJZRMeLWQEL9aW0G8JBwEcFhIUFkCcWwaW%2BWMljD3xz1pJEGe9%2FwExBuPJDPO%2Bo73ZVYH0JeHtRPEBqAvN%2F2jPtdcuuOv5XyHHoEO8Y0Y0qF0cOEnJW0O%2FGrtrPuyQAG3diCyiVg13BhZ8W1hQp5Z3bqJTNn1L7msqDuZchY5yJ4sYaAS%2BYraxidjZ%2BqFGmDfqt%2FAPVh0GqTuxq1QksfWb%2F561z22rV%2BOYpzMMj5i70GOqUBMIXU5VX0jS4VWzArCHulGXBZocAMoRpneEhFRqo5zQ5fIG1%2BR7FII9yBdfNSts%2ByGl%2F5kpf8mIq%2BZYmA0JCRrE8MrPbiep2qljo%2FYSxaeXwoVRZsYEybd8sXqbyvCB7jPuF1igk8ZN71vhRCZVY2TK2354110VSS%2BAsnrCjgi51GBoTWJ4Doaonzx1bpW%2FRtjgQHlQbZTR9np2sv13rgi%2B0g85mT&X-Amz-Signature=46719d5fd9684fc31ee7f2fd4e09d36511914c135cad047789fdae72331aaec4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677GDIYK3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDBeBp2fdNhdSiA3TUJVvobC9z5PxPPjn5Zd09qW%2F2OMgIgORnCn5gQL8%2B5WlceHaA4%2FBEIpcWOd6ljaTY6k7rfZZYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDDgx7EJ7GydhvjCb1CrcA%2BVgKa%2Fr4i7RWg3iv%2F1Gd0DvbODOjMyuMeJe0zgdL2NOnVhicLsMCSl52pJSeFGVzIL7z6tykYvztasPSoga1j%2BkIwDn2F1b0in0UeYhvsce8fp6HV2OSUIymnNlp3lMYQZUswGvFSs4OcO%2FZ3aNSDIZyAYmESwJRJhA17Lej%2BVxSJNBFi3xsJwdj3%2F%2BC3BgTN%2FzSuJDVKk%2BAZ%2BkvHVRa5h2Ni7BNinkHmNrYuC04wZhlVaxFrFsYag38pl29214HgMGq9nAQFg9C645Jqa8kLnBblC4t6KFeU992f%2BK3bQ7vUmFPioM3rvZvsV3BdNvpvAhKqeX9Khhg4O6ov2Iy0vPbgdgD%2FG%2FoqojrEKzX9Ozsx4oDMPtEcoFPjn7Na6RH9rr3G%2Bd6bXgp%2B6eT1FjBk6FuJZRMeLWQEL9aW0G8JBwEcFhIUFkCcWwaW%2BWMljD3xz1pJEGe9%2FwExBuPJDPO%2Bo73ZVYH0JeHtRPEBqAvN%2F2jPtdcuuOv5XyHHoEO8Y0Y0qF0cOEnJW0O%2FGrtrPuyQAG3diCyiVg13BhZ8W1hQp5Z3bqJTNn1L7msqDuZchY5yJ4sYaAS%2BYraxidjZ%2BqFGmDfqt%2FAPVh0GqTuxq1QksfWb%2F561z22rV%2BOYpzMMj5i70GOqUBMIXU5VX0jS4VWzArCHulGXBZocAMoRpneEhFRqo5zQ5fIG1%2BR7FII9yBdfNSts%2ByGl%2F5kpf8mIq%2BZYmA0JCRrE8MrPbiep2qljo%2FYSxaeXwoVRZsYEybd8sXqbyvCB7jPuF1igk8ZN71vhRCZVY2TK2354110VSS%2BAsnrCjgi51GBoTWJ4Doaonzx1bpW%2FRtjgQHlQbZTR9np2sv13rgi%2B0g85mT&X-Amz-Signature=a0bb89e94abe6132d14a14812d915f40c6e39d5e995ffa844c31ede54de81bd9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677GDIYK3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDBeBp2fdNhdSiA3TUJVvobC9z5PxPPjn5Zd09qW%2F2OMgIgORnCn5gQL8%2B5WlceHaA4%2FBEIpcWOd6ljaTY6k7rfZZYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDDgx7EJ7GydhvjCb1CrcA%2BVgKa%2Fr4i7RWg3iv%2F1Gd0DvbODOjMyuMeJe0zgdL2NOnVhicLsMCSl52pJSeFGVzIL7z6tykYvztasPSoga1j%2BkIwDn2F1b0in0UeYhvsce8fp6HV2OSUIymnNlp3lMYQZUswGvFSs4OcO%2FZ3aNSDIZyAYmESwJRJhA17Lej%2BVxSJNBFi3xsJwdj3%2F%2BC3BgTN%2FzSuJDVKk%2BAZ%2BkvHVRa5h2Ni7BNinkHmNrYuC04wZhlVaxFrFsYag38pl29214HgMGq9nAQFg9C645Jqa8kLnBblC4t6KFeU992f%2BK3bQ7vUmFPioM3rvZvsV3BdNvpvAhKqeX9Khhg4O6ov2Iy0vPbgdgD%2FG%2FoqojrEKzX9Ozsx4oDMPtEcoFPjn7Na6RH9rr3G%2Bd6bXgp%2B6eT1FjBk6FuJZRMeLWQEL9aW0G8JBwEcFhIUFkCcWwaW%2BWMljD3xz1pJEGe9%2FwExBuPJDPO%2Bo73ZVYH0JeHtRPEBqAvN%2F2jPtdcuuOv5XyHHoEO8Y0Y0qF0cOEnJW0O%2FGrtrPuyQAG3diCyiVg13BhZ8W1hQp5Z3bqJTNn1L7msqDuZchY5yJ4sYaAS%2BYraxidjZ%2BqFGmDfqt%2FAPVh0GqTuxq1QksfWb%2F561z22rV%2BOYpzMMj5i70GOqUBMIXU5VX0jS4VWzArCHulGXBZocAMoRpneEhFRqo5zQ5fIG1%2BR7FII9yBdfNSts%2ByGl%2F5kpf8mIq%2BZYmA0JCRrE8MrPbiep2qljo%2FYSxaeXwoVRZsYEybd8sXqbyvCB7jPuF1igk8ZN71vhRCZVY2TK2354110VSS%2BAsnrCjgi51GBoTWJ4Doaonzx1bpW%2FRtjgQHlQbZTR9np2sv13rgi%2B0g85mT&X-Amz-Signature=0b84072a2637bf175150811214daaf90d0887f19f40ed80af1df89b2cfbab1c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677GDIYK3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDBeBp2fdNhdSiA3TUJVvobC9z5PxPPjn5Zd09qW%2F2OMgIgORnCn5gQL8%2B5WlceHaA4%2FBEIpcWOd6ljaTY6k7rfZZYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDDgx7EJ7GydhvjCb1CrcA%2BVgKa%2Fr4i7RWg3iv%2F1Gd0DvbODOjMyuMeJe0zgdL2NOnVhicLsMCSl52pJSeFGVzIL7z6tykYvztasPSoga1j%2BkIwDn2F1b0in0UeYhvsce8fp6HV2OSUIymnNlp3lMYQZUswGvFSs4OcO%2FZ3aNSDIZyAYmESwJRJhA17Lej%2BVxSJNBFi3xsJwdj3%2F%2BC3BgTN%2FzSuJDVKk%2BAZ%2BkvHVRa5h2Ni7BNinkHmNrYuC04wZhlVaxFrFsYag38pl29214HgMGq9nAQFg9C645Jqa8kLnBblC4t6KFeU992f%2BK3bQ7vUmFPioM3rvZvsV3BdNvpvAhKqeX9Khhg4O6ov2Iy0vPbgdgD%2FG%2FoqojrEKzX9Ozsx4oDMPtEcoFPjn7Na6RH9rr3G%2Bd6bXgp%2B6eT1FjBk6FuJZRMeLWQEL9aW0G8JBwEcFhIUFkCcWwaW%2BWMljD3xz1pJEGe9%2FwExBuPJDPO%2Bo73ZVYH0JeHtRPEBqAvN%2F2jPtdcuuOv5XyHHoEO8Y0Y0qF0cOEnJW0O%2FGrtrPuyQAG3diCyiVg13BhZ8W1hQp5Z3bqJTNn1L7msqDuZchY5yJ4sYaAS%2BYraxidjZ%2BqFGmDfqt%2FAPVh0GqTuxq1QksfWb%2F561z22rV%2BOYpzMMj5i70GOqUBMIXU5VX0jS4VWzArCHulGXBZocAMoRpneEhFRqo5zQ5fIG1%2BR7FII9yBdfNSts%2ByGl%2F5kpf8mIq%2BZYmA0JCRrE8MrPbiep2qljo%2FYSxaeXwoVRZsYEybd8sXqbyvCB7jPuF1igk8ZN71vhRCZVY2TK2354110VSS%2BAsnrCjgi51GBoTWJ4Doaonzx1bpW%2FRtjgQHlQbZTR9np2sv13rgi%2B0g85mT&X-Amz-Signature=db439917c205a0b2a0f93d215be27859354ad35ca567222fc1d4c92d96d4d825&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677GDIYK3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDBeBp2fdNhdSiA3TUJVvobC9z5PxPPjn5Zd09qW%2F2OMgIgORnCn5gQL8%2B5WlceHaA4%2FBEIpcWOd6ljaTY6k7rfZZYq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDDgx7EJ7GydhvjCb1CrcA%2BVgKa%2Fr4i7RWg3iv%2F1Gd0DvbODOjMyuMeJe0zgdL2NOnVhicLsMCSl52pJSeFGVzIL7z6tykYvztasPSoga1j%2BkIwDn2F1b0in0UeYhvsce8fp6HV2OSUIymnNlp3lMYQZUswGvFSs4OcO%2FZ3aNSDIZyAYmESwJRJhA17Lej%2BVxSJNBFi3xsJwdj3%2F%2BC3BgTN%2FzSuJDVKk%2BAZ%2BkvHVRa5h2Ni7BNinkHmNrYuC04wZhlVaxFrFsYag38pl29214HgMGq9nAQFg9C645Jqa8kLnBblC4t6KFeU992f%2BK3bQ7vUmFPioM3rvZvsV3BdNvpvAhKqeX9Khhg4O6ov2Iy0vPbgdgD%2FG%2FoqojrEKzX9Ozsx4oDMPtEcoFPjn7Na6RH9rr3G%2Bd6bXgp%2B6eT1FjBk6FuJZRMeLWQEL9aW0G8JBwEcFhIUFkCcWwaW%2BWMljD3xz1pJEGe9%2FwExBuPJDPO%2Bo73ZVYH0JeHtRPEBqAvN%2F2jPtdcuuOv5XyHHoEO8Y0Y0qF0cOEnJW0O%2FGrtrPuyQAG3diCyiVg13BhZ8W1hQp5Z3bqJTNn1L7msqDuZchY5yJ4sYaAS%2BYraxidjZ%2BqFGmDfqt%2FAPVh0GqTuxq1QksfWb%2F561z22rV%2BOYpzMMj5i70GOqUBMIXU5VX0jS4VWzArCHulGXBZocAMoRpneEhFRqo5zQ5fIG1%2BR7FII9yBdfNSts%2ByGl%2F5kpf8mIq%2BZYmA0JCRrE8MrPbiep2qljo%2FYSxaeXwoVRZsYEybd8sXqbyvCB7jPuF1igk8ZN71vhRCZVY2TK2354110VSS%2BAsnrCjgi51GBoTWJ4Doaonzx1bpW%2FRtjgQHlQbZTR9np2sv13rgi%2B0g85mT&X-Amz-Signature=3cc2683932dfee73c23a9fc526c80045079bfcd80d70a2dfe78cc25eab5344fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWGLR3G7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIGmYb3fFVKxL8%2BuWHY%2BsZ3NDMpACJzJiveDc4%2Fc2%2Fh%2BGAiB5w46nYfuyaSXJcE1E1gTm3bZJqNoueBg5vkEhG8r%2FTSr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMKSa4a9UvMXAIxbYVKtwDzNswlfthRQQWEbYUJ8MNJJ3cHeFuh4iSnFgzUo%2BxjfXSGRlo0eZyXEH%2B2InPmitZ1MRJ91apkVFIVlOrMLm7Z975QUiY7zKvPD4NwgzFiWIlWnkv%2FoXw5lyKsjDcbdSnWp7T1GjUfKZNAM5tJpJao8EHpUC12xFnuUgqbDNj4P%2FNNm39%2BPpYUVnFzdcKz2cJUngB6N3FhN4EBJx8%2BlyNPTypTmitK8EC5kc6RJM%2FkxG4VS7dt7M0k49CXXnYBzYvvpehD9zmGM5VxDcmhgCYPQQ6kOvasvrklSKUZ7cM9IL1psankR%2FefRVi7RjOMvMSlvmZTS9WxD5OQ%2FD%2FGsWumCbfJV0P2oJ2pf4fmbsWP8aiT2jRU1FQGJG0jvrfxb0YpU%2BI3pmU0jI3klM7ZXhGqY4%2FNOsz1ZWp1Hmh7VsaCHyWTJ1USVQ69mxqs0kbdNEveUgfR8YdGhnrSIETjiPzSDStzKV7SomsezbKGYYQAcN8S1CmD1c0VPCeQdF41Ot3h2MJRloznL5lzo41VlufftO1jOyGQdQ9pdp4wskPufS73aLV584e8Voh9hZl8%2BVPsFKdXYA%2BlauoTId8gUwVgdEDsBYsQqPlXFMMwu8t1yplI8%2BQLd51hulUHyAwq%2FmLvQY6pgHbXgjAgPfjBQpb%2BECHO1Xx2sP7CCc7KxYnWU7zTwsAo6gbrlddEgQKZ1ofqoLnJbOJ%2BAZ6XFaveTuMSB4NBg3Y0dA0GEz2r8JQyD7MHEVvcRtb6IoMfB%2FmaNOU5iI7qx26yC5InN1z4PIWoaA1XXJhc5rkAEBPZ67DGtF6Sys2pPgm495c2w%2BRPASJUbLzpBJgE9dXLmrZEYJNPWGPEj3MKASPIuRW&X-Amz-Signature=d23c943e21f6451331f4feec84dce4cea6b40f943035248383ea83fc857fef52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMMSMQ3C%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQDI0EbLfxfky8e3BJW2zoaRPTuuh8MtWG0pH9c%2Fa3r1lAIgWiZowmusCDROAfBBskdBfC0y1Z4w%2B8gGeV4GVX8xSKAq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDI1F6CfCJvgQjBVpXSrcA%2F4pZXhRNPvjp%2FmlfMtEJf0YH34x8ZvrtUny1Dz9oRBPexbePm%2BgBE0lZUHQFYKdrecI5c8IUbUzHWCilvpWK5kJlvnCzdgYY%2FYRo2ALT5mXXuPcEepnL1bxBUqqbdu%2FO4ME2PVp9hFtAZmRGyX5bT9zkUi%2BdHHl4nYjV7O3DcLNag1qfS4pIXt5fftDu8XbSzZMukWBo5BNX3CMnJ%2FkVex4dZpGrMTyfKY2e29O4gI6QpYUy%2BANrJCtsXIvGsnRL1IqL5IaW39SIYhdLyrQguVdjhcsSw18ZnkA57aTTI0kl7jXDtpsLDC4jI5fvW9Ty3LYCeMnDZYt2LElY0sGfvvfyzGVHfc57Urf53i5yEYccpuRrPriYe8PHklhmDvet6150Y28WemVFFcoVqMu8ZdB3remXLQwyDz1p01Grtt6minY57UcpZY422iU4RigxNRYqoD97eVpJvmtTb2uRqER%2FfhKAZ8PaLnt7rX5Z6UW28gAEp8TmD4GoFBYaepn0U9hfN7DMT7zbQm62RZmVj46NUNs0SiUMospPx8Qgqy%2FypMRQ8STQD7F7cs4o9dYL4o05EaNfZu2arOoSEQbMCTHqACLFvyd6RXzsszGMkcrWcuYSmri2vf%2BCmAqMKv5i70GOqUBISp9osI5WeXVLVe63jDN8WBk025wXH25QQmGMEbgmlKpdL2ackOXwMt40IzWWsGMFVFRTOT18HjhfzPgOEp46ynbKsK1vTPMU9b%2BuehoAKhppTLE2MYD0NdhTN%2FnskSO%2FqEVKkhWDU8I%2FM1wBLn8seoy2WmMFHGEIGLfhf%2BJIUKtV4znucduvybdvGhGhja3nwNZDmbX7JvtYGlA5nA8REezeHDj&X-Amz-Signature=87c5897ff2d797756b246278295af2572fcd74b92e94ab4325dabf3c382cef4a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZD4BYHM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQCs9rdhvirC%2Fb0P86DgfRnwARBmSaHOQvDM0%2Bs1pNWA1QIhAJAg4Kh4X4Y8xBfXnnCU3JD2STyxXqnFv7MzhnBBayT8Kv8DCD8QABoMNjM3NDIzMTgzODA1IgxPPnt8dGFK3m8jPO8q3AM8W0G%2BnuuHThjfDuxl0Pnd2jFXYcMlRT0n1npaBHiznXoK3Q%2Bczy%2FY1bW6U%2FGdI8%2BFF6gE64iRT8VZFwYn13n66iM%2BNNfU2plduyJiLgb0OWbCUJ23hLQhhEaLZSAXUwXED1LaipFH6VG1aUz3%2FAy3Ri40pVkWzAyMOXvQ206Dfo%2BgJygkNyzj8Cc3yrYKKkBlsymahNQBxPSsqgNTCAMlfT2zmqQtml7zm2woMczBAKRXWVlzI%2BpuQemXjYlluI9Tbmvnz9C9ouRw%2BYtkVG9CydsXSt1tA5nHmSEjy5OsyWFzpYwna%2BjwJ8XW5Ec%2FItaie23UmBxHj78nAEtqOO9v19w4BXHgtchp3S4jqlaETXRulAQw3WXFS00RE9ZTntA2IQvUFOP7Biwyjy6%2BqH8wBfRWYhZXezLnqqLrq1%2FG7qHSVdBGxyhUWYkYwmLaZFgyjOs0PlR%2B78%2BWC86DO55yqSTbNjukOXAW%2BkMrDthIfycNdb9TrPnO6oIvq%2FCapvuc9NrlGwIfMGwzacmfVf%2FqHeZ3tUDhyjvg6gvcFZ%2BhKFay698uqoRa2g0iVAq183ecWwW9c%2BsvdcHtIrl2K%2FEabTbqZaP6ecyvP7F3iVfm6j%2F%2BIdKuhMiCvXwMTzD%2F%2BYu9BjqkAUNrpjRrf6cHXhEaIVltT9L3F5WloVkgx4UYuS7AgjeFWq1bCVEa3pXNzDvUdD2e8oE0bFGPz2lzJqSsV88wadsC8C8yYEVq5UUMmYr5n%2FAiWvyIJzyoEKvn85V1b6nFvi%2FDz0URvsTRguRFSs7HnxFHlOwBcLoBehVgJyAZ6TQgiibeeQmR01LKmCLGTtORIEM7IzSIxNOoETT4i48LffP6x%2BPJ&X-Amz-Signature=a0f2f450cf25a746a9ac2637f1ff6c3c2277b635933cb20ed941e3f7341996dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZD4BYHM%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T062031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQCs9rdhvirC%2Fb0P86DgfRnwARBmSaHOQvDM0%2Bs1pNWA1QIhAJAg4Kh4X4Y8xBfXnnCU3JD2STyxXqnFv7MzhnBBayT8Kv8DCD8QABoMNjM3NDIzMTgzODA1IgxPPnt8dGFK3m8jPO8q3AM8W0G%2BnuuHThjfDuxl0Pnd2jFXYcMlRT0n1npaBHiznXoK3Q%2Bczy%2FY1bW6U%2FGdI8%2BFF6gE64iRT8VZFwYn13n66iM%2BNNfU2plduyJiLgb0OWbCUJ23hLQhhEaLZSAXUwXED1LaipFH6VG1aUz3%2FAy3Ri40pVkWzAyMOXvQ206Dfo%2BgJygkNyzj8Cc3yrYKKkBlsymahNQBxPSsqgNTCAMlfT2zmqQtml7zm2woMczBAKRXWVlzI%2BpuQemXjYlluI9Tbmvnz9C9ouRw%2BYtkVG9CydsXSt1tA5nHmSEjy5OsyWFzpYwna%2BjwJ8XW5Ec%2FItaie23UmBxHj78nAEtqOO9v19w4BXHgtchp3S4jqlaETXRulAQw3WXFS00RE9ZTntA2IQvUFOP7Biwyjy6%2BqH8wBfRWYhZXezLnqqLrq1%2FG7qHSVdBGxyhUWYkYwmLaZFgyjOs0PlR%2B78%2BWC86DO55yqSTbNjukOXAW%2BkMrDthIfycNdb9TrPnO6oIvq%2FCapvuc9NrlGwIfMGwzacmfVf%2FqHeZ3tUDhyjvg6gvcFZ%2BhKFay698uqoRa2g0iVAq183ecWwW9c%2BsvdcHtIrl2K%2FEabTbqZaP6ecyvP7F3iVfm6j%2F%2BIdKuhMiCvXwMTzD%2F%2BYu9BjqkAUNrpjRrf6cHXhEaIVltT9L3F5WloVkgx4UYuS7AgjeFWq1bCVEa3pXNzDvUdD2e8oE0bFGPz2lzJqSsV88wadsC8C8yYEVq5UUMmYr5n%2FAiWvyIJzyoEKvn85V1b6nFvi%2FDz0URvsTRguRFSs7HnxFHlOwBcLoBehVgJyAZ6TQgiibeeQmR01LKmCLGTtORIEM7IzSIxNOoETT4i48LffP6x%2BPJ&X-Amz-Signature=abe31bc435373107c7b6c16d918c1b44b22715a4dce04a7a972300885071da3a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
