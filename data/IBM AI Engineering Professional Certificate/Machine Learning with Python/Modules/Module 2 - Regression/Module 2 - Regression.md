

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX3QI7SW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCID7me5Fm2DRu7gO3OhnjAohfWMzyaOa0ocJq6rn4eCmEAiEAnkt%2FRp9CLIi1EFyt9PAVNl26nEtrUr6Sg61pEhfjR9Mq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGwNyA%2BExqknPoPq3SrcA9ZPPpXKlXjGV3fxkTR2jx0C7SDN73UHKEFvdJxblYY%2BCDmn7as9dqCbUI8%2B6WuOWuRPmq1UptUHy6yug6JnlC2S8C%2BglSzusjpb%2Bd3b39VddF%2B8UwsV0cDpUgfy8OtFxPrOE%2Fyn2SG%2BhtVM22gMMyogSFERx3rnzyOJJLsdlNSYFAeK4YQhkrjzGUpPr7F4Ub1Yb%2BmLruFy39G5763c8gV0YFxi6zL%2BeZjj80pvhF8FiOj9JPwnw7epyX8WXu9umIIi0Je5I3Cgmm0p7yCQEAvwUSlVg%2FykAmtOoS53qxsbF8TbgcNgBgGV5%2BkHzF1PdZB%2BbGEZXxL3U9uk04bIb9TObQcz0V7buM2gul2aSku8%2FDbAR%2Fp9r5U3290ygiy7sTnsl0Ew95DIZ8S33Irt6r3pxF1iwwMl7ZTpQTefrfOn9%2FvFLvIYlka5%2B6ufSpnpG9FkHoNzd0tSlU7FpzbrfcA3KK5QtqGRU4BbpcfwqhoLLhXspHrrUstytG4NmWKCfWkmzgNh6o7lw%2F0%2BhjUel0cq1Ur8%2BJoQ148O9MsxBnrQhv65ZAAhQUNrTSXhGoDzrf7LsxZoCEzmmpOwsumraZCC1gpE903bQPoEhZXzV8n9n2G9cZtSQ076OGW0MPL%2Bmb0GOqUBjtpaVtso9dvwk4x1663Kk5TEMS6Hmh2P3idzbTxc4JJ0N1TSN8FfkCyNcmVt0S8GUs5Pk%2B0zN9bA%2BVw45GPc5YQJQsPmtr0DRL3rpVr%2FLUfGtnRFHmcWVb6b0mjbvr2pvF9JP2Avn72yN%2BjL7orj6HxsEB%2F4kNSpUglx6ByGeWXzUb0%2BsoxvERIlVrVbsa5p3sOkaLNRM59TchvlNEerlOiePAHD&X-Amz-Signature=507ce14ef6fa72743f1ab2888cdc4bcc5776adb87d60ecc592f3b960180ce2cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX3QI7SW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCID7me5Fm2DRu7gO3OhnjAohfWMzyaOa0ocJq6rn4eCmEAiEAnkt%2FRp9CLIi1EFyt9PAVNl26nEtrUr6Sg61pEhfjR9Mq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGwNyA%2BExqknPoPq3SrcA9ZPPpXKlXjGV3fxkTR2jx0C7SDN73UHKEFvdJxblYY%2BCDmn7as9dqCbUI8%2B6WuOWuRPmq1UptUHy6yug6JnlC2S8C%2BglSzusjpb%2Bd3b39VddF%2B8UwsV0cDpUgfy8OtFxPrOE%2Fyn2SG%2BhtVM22gMMyogSFERx3rnzyOJJLsdlNSYFAeK4YQhkrjzGUpPr7F4Ub1Yb%2BmLruFy39G5763c8gV0YFxi6zL%2BeZjj80pvhF8FiOj9JPwnw7epyX8WXu9umIIi0Je5I3Cgmm0p7yCQEAvwUSlVg%2FykAmtOoS53qxsbF8TbgcNgBgGV5%2BkHzF1PdZB%2BbGEZXxL3U9uk04bIb9TObQcz0V7buM2gul2aSku8%2FDbAR%2Fp9r5U3290ygiy7sTnsl0Ew95DIZ8S33Irt6r3pxF1iwwMl7ZTpQTefrfOn9%2FvFLvIYlka5%2B6ufSpnpG9FkHoNzd0tSlU7FpzbrfcA3KK5QtqGRU4BbpcfwqhoLLhXspHrrUstytG4NmWKCfWkmzgNh6o7lw%2F0%2BhjUel0cq1Ur8%2BJoQ148O9MsxBnrQhv65ZAAhQUNrTSXhGoDzrf7LsxZoCEzmmpOwsumraZCC1gpE903bQPoEhZXzV8n9n2G9cZtSQ076OGW0MPL%2Bmb0GOqUBjtpaVtso9dvwk4x1663Kk5TEMS6Hmh2P3idzbTxc4JJ0N1TSN8FfkCyNcmVt0S8GUs5Pk%2B0zN9bA%2BVw45GPc5YQJQsPmtr0DRL3rpVr%2FLUfGtnRFHmcWVb6b0mjbvr2pvF9JP2Avn72yN%2BjL7orj6HxsEB%2F4kNSpUglx6ByGeWXzUb0%2BsoxvERIlVrVbsa5p3sOkaLNRM59TchvlNEerlOiePAHD&X-Amz-Signature=630a06e46ecd61a39649d908f1843db1d1d47143cc8dd297f249dbb8d80706b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX3QI7SW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCID7me5Fm2DRu7gO3OhnjAohfWMzyaOa0ocJq6rn4eCmEAiEAnkt%2FRp9CLIi1EFyt9PAVNl26nEtrUr6Sg61pEhfjR9Mq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGwNyA%2BExqknPoPq3SrcA9ZPPpXKlXjGV3fxkTR2jx0C7SDN73UHKEFvdJxblYY%2BCDmn7as9dqCbUI8%2B6WuOWuRPmq1UptUHy6yug6JnlC2S8C%2BglSzusjpb%2Bd3b39VddF%2B8UwsV0cDpUgfy8OtFxPrOE%2Fyn2SG%2BhtVM22gMMyogSFERx3rnzyOJJLsdlNSYFAeK4YQhkrjzGUpPr7F4Ub1Yb%2BmLruFy39G5763c8gV0YFxi6zL%2BeZjj80pvhF8FiOj9JPwnw7epyX8WXu9umIIi0Je5I3Cgmm0p7yCQEAvwUSlVg%2FykAmtOoS53qxsbF8TbgcNgBgGV5%2BkHzF1PdZB%2BbGEZXxL3U9uk04bIb9TObQcz0V7buM2gul2aSku8%2FDbAR%2Fp9r5U3290ygiy7sTnsl0Ew95DIZ8S33Irt6r3pxF1iwwMl7ZTpQTefrfOn9%2FvFLvIYlka5%2B6ufSpnpG9FkHoNzd0tSlU7FpzbrfcA3KK5QtqGRU4BbpcfwqhoLLhXspHrrUstytG4NmWKCfWkmzgNh6o7lw%2F0%2BhjUel0cq1Ur8%2BJoQ148O9MsxBnrQhv65ZAAhQUNrTSXhGoDzrf7LsxZoCEzmmpOwsumraZCC1gpE903bQPoEhZXzV8n9n2G9cZtSQ076OGW0MPL%2Bmb0GOqUBjtpaVtso9dvwk4x1663Kk5TEMS6Hmh2P3idzbTxc4JJ0N1TSN8FfkCyNcmVt0S8GUs5Pk%2B0zN9bA%2BVw45GPc5YQJQsPmtr0DRL3rpVr%2FLUfGtnRFHmcWVb6b0mjbvr2pvF9JP2Avn72yN%2BjL7orj6HxsEB%2F4kNSpUglx6ByGeWXzUb0%2BsoxvERIlVrVbsa5p3sOkaLNRM59TchvlNEerlOiePAHD&X-Amz-Signature=20f5baea6456c5afcd0b8304190e80dbb307013e366db873a81f28492e037ee0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX3QI7SW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCID7me5Fm2DRu7gO3OhnjAohfWMzyaOa0ocJq6rn4eCmEAiEAnkt%2FRp9CLIi1EFyt9PAVNl26nEtrUr6Sg61pEhfjR9Mq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGwNyA%2BExqknPoPq3SrcA9ZPPpXKlXjGV3fxkTR2jx0C7SDN73UHKEFvdJxblYY%2BCDmn7as9dqCbUI8%2B6WuOWuRPmq1UptUHy6yug6JnlC2S8C%2BglSzusjpb%2Bd3b39VddF%2B8UwsV0cDpUgfy8OtFxPrOE%2Fyn2SG%2BhtVM22gMMyogSFERx3rnzyOJJLsdlNSYFAeK4YQhkrjzGUpPr7F4Ub1Yb%2BmLruFy39G5763c8gV0YFxi6zL%2BeZjj80pvhF8FiOj9JPwnw7epyX8WXu9umIIi0Je5I3Cgmm0p7yCQEAvwUSlVg%2FykAmtOoS53qxsbF8TbgcNgBgGV5%2BkHzF1PdZB%2BbGEZXxL3U9uk04bIb9TObQcz0V7buM2gul2aSku8%2FDbAR%2Fp9r5U3290ygiy7sTnsl0Ew95DIZ8S33Irt6r3pxF1iwwMl7ZTpQTefrfOn9%2FvFLvIYlka5%2B6ufSpnpG9FkHoNzd0tSlU7FpzbrfcA3KK5QtqGRU4BbpcfwqhoLLhXspHrrUstytG4NmWKCfWkmzgNh6o7lw%2F0%2BhjUel0cq1Ur8%2BJoQ148O9MsxBnrQhv65ZAAhQUNrTSXhGoDzrf7LsxZoCEzmmpOwsumraZCC1gpE903bQPoEhZXzV8n9n2G9cZtSQ076OGW0MPL%2Bmb0GOqUBjtpaVtso9dvwk4x1663Kk5TEMS6Hmh2P3idzbTxc4JJ0N1TSN8FfkCyNcmVt0S8GUs5Pk%2B0zN9bA%2BVw45GPc5YQJQsPmtr0DRL3rpVr%2FLUfGtnRFHmcWVb6b0mjbvr2pvF9JP2Avn72yN%2BjL7orj6HxsEB%2F4kNSpUglx6ByGeWXzUb0%2BsoxvERIlVrVbsa5p3sOkaLNRM59TchvlNEerlOiePAHD&X-Amz-Signature=2b4775518ba32b75d0a2fcb96f9103c460f6e898cdf76718dd3682af2e5b5bf9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX3QI7SW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCID7me5Fm2DRu7gO3OhnjAohfWMzyaOa0ocJq6rn4eCmEAiEAnkt%2FRp9CLIi1EFyt9PAVNl26nEtrUr6Sg61pEhfjR9Mq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGwNyA%2BExqknPoPq3SrcA9ZPPpXKlXjGV3fxkTR2jx0C7SDN73UHKEFvdJxblYY%2BCDmn7as9dqCbUI8%2B6WuOWuRPmq1UptUHy6yug6JnlC2S8C%2BglSzusjpb%2Bd3b39VddF%2B8UwsV0cDpUgfy8OtFxPrOE%2Fyn2SG%2BhtVM22gMMyogSFERx3rnzyOJJLsdlNSYFAeK4YQhkrjzGUpPr7F4Ub1Yb%2BmLruFy39G5763c8gV0YFxi6zL%2BeZjj80pvhF8FiOj9JPwnw7epyX8WXu9umIIi0Je5I3Cgmm0p7yCQEAvwUSlVg%2FykAmtOoS53qxsbF8TbgcNgBgGV5%2BkHzF1PdZB%2BbGEZXxL3U9uk04bIb9TObQcz0V7buM2gul2aSku8%2FDbAR%2Fp9r5U3290ygiy7sTnsl0Ew95DIZ8S33Irt6r3pxF1iwwMl7ZTpQTefrfOn9%2FvFLvIYlka5%2B6ufSpnpG9FkHoNzd0tSlU7FpzbrfcA3KK5QtqGRU4BbpcfwqhoLLhXspHrrUstytG4NmWKCfWkmzgNh6o7lw%2F0%2BhjUel0cq1Ur8%2BJoQ148O9MsxBnrQhv65ZAAhQUNrTSXhGoDzrf7LsxZoCEzmmpOwsumraZCC1gpE903bQPoEhZXzV8n9n2G9cZtSQ076OGW0MPL%2Bmb0GOqUBjtpaVtso9dvwk4x1663Kk5TEMS6Hmh2P3idzbTxc4JJ0N1TSN8FfkCyNcmVt0S8GUs5Pk%2B0zN9bA%2BVw45GPc5YQJQsPmtr0DRL3rpVr%2FLUfGtnRFHmcWVb6b0mjbvr2pvF9JP2Avn72yN%2BjL7orj6HxsEB%2F4kNSpUglx6ByGeWXzUb0%2BsoxvERIlVrVbsa5p3sOkaLNRM59TchvlNEerlOiePAHD&X-Amz-Signature=7ebc270f7fc2c40faba9d7882fba3e56e6eaa25f5dea2bbc15d8fd4325598694&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX3QI7SW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCID7me5Fm2DRu7gO3OhnjAohfWMzyaOa0ocJq6rn4eCmEAiEAnkt%2FRp9CLIi1EFyt9PAVNl26nEtrUr6Sg61pEhfjR9Mq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGwNyA%2BExqknPoPq3SrcA9ZPPpXKlXjGV3fxkTR2jx0C7SDN73UHKEFvdJxblYY%2BCDmn7as9dqCbUI8%2B6WuOWuRPmq1UptUHy6yug6JnlC2S8C%2BglSzusjpb%2Bd3b39VddF%2B8UwsV0cDpUgfy8OtFxPrOE%2Fyn2SG%2BhtVM22gMMyogSFERx3rnzyOJJLsdlNSYFAeK4YQhkrjzGUpPr7F4Ub1Yb%2BmLruFy39G5763c8gV0YFxi6zL%2BeZjj80pvhF8FiOj9JPwnw7epyX8WXu9umIIi0Je5I3Cgmm0p7yCQEAvwUSlVg%2FykAmtOoS53qxsbF8TbgcNgBgGV5%2BkHzF1PdZB%2BbGEZXxL3U9uk04bIb9TObQcz0V7buM2gul2aSku8%2FDbAR%2Fp9r5U3290ygiy7sTnsl0Ew95DIZ8S33Irt6r3pxF1iwwMl7ZTpQTefrfOn9%2FvFLvIYlka5%2B6ufSpnpG9FkHoNzd0tSlU7FpzbrfcA3KK5QtqGRU4BbpcfwqhoLLhXspHrrUstytG4NmWKCfWkmzgNh6o7lw%2F0%2BhjUel0cq1Ur8%2BJoQ148O9MsxBnrQhv65ZAAhQUNrTSXhGoDzrf7LsxZoCEzmmpOwsumraZCC1gpE903bQPoEhZXzV8n9n2G9cZtSQ076OGW0MPL%2Bmb0GOqUBjtpaVtso9dvwk4x1663Kk5TEMS6Hmh2P3idzbTxc4JJ0N1TSN8FfkCyNcmVt0S8GUs5Pk%2B0zN9bA%2BVw45GPc5YQJQsPmtr0DRL3rpVr%2FLUfGtnRFHmcWVb6b0mjbvr2pvF9JP2Avn72yN%2BjL7orj6HxsEB%2F4kNSpUglx6ByGeWXzUb0%2BsoxvERIlVrVbsa5p3sOkaLNRM59TchvlNEerlOiePAHD&X-Amz-Signature=b206f5260b7b088f4cb755cc9f0cfd702555bc899ff0e29419afc5f9ca96c399&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX3QI7SW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCID7me5Fm2DRu7gO3OhnjAohfWMzyaOa0ocJq6rn4eCmEAiEAnkt%2FRp9CLIi1EFyt9PAVNl26nEtrUr6Sg61pEhfjR9Mq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGwNyA%2BExqknPoPq3SrcA9ZPPpXKlXjGV3fxkTR2jx0C7SDN73UHKEFvdJxblYY%2BCDmn7as9dqCbUI8%2B6WuOWuRPmq1UptUHy6yug6JnlC2S8C%2BglSzusjpb%2Bd3b39VddF%2B8UwsV0cDpUgfy8OtFxPrOE%2Fyn2SG%2BhtVM22gMMyogSFERx3rnzyOJJLsdlNSYFAeK4YQhkrjzGUpPr7F4Ub1Yb%2BmLruFy39G5763c8gV0YFxi6zL%2BeZjj80pvhF8FiOj9JPwnw7epyX8WXu9umIIi0Je5I3Cgmm0p7yCQEAvwUSlVg%2FykAmtOoS53qxsbF8TbgcNgBgGV5%2BkHzF1PdZB%2BbGEZXxL3U9uk04bIb9TObQcz0V7buM2gul2aSku8%2FDbAR%2Fp9r5U3290ygiy7sTnsl0Ew95DIZ8S33Irt6r3pxF1iwwMl7ZTpQTefrfOn9%2FvFLvIYlka5%2B6ufSpnpG9FkHoNzd0tSlU7FpzbrfcA3KK5QtqGRU4BbpcfwqhoLLhXspHrrUstytG4NmWKCfWkmzgNh6o7lw%2F0%2BhjUel0cq1Ur8%2BJoQ148O9MsxBnrQhv65ZAAhQUNrTSXhGoDzrf7LsxZoCEzmmpOwsumraZCC1gpE903bQPoEhZXzV8n9n2G9cZtSQ076OGW0MPL%2Bmb0GOqUBjtpaVtso9dvwk4x1663Kk5TEMS6Hmh2P3idzbTxc4JJ0N1TSN8FfkCyNcmVt0S8GUs5Pk%2B0zN9bA%2BVw45GPc5YQJQsPmtr0DRL3rpVr%2FLUfGtnRFHmcWVb6b0mjbvr2pvF9JP2Avn72yN%2BjL7orj6HxsEB%2F4kNSpUglx6ByGeWXzUb0%2BsoxvERIlVrVbsa5p3sOkaLNRM59TchvlNEerlOiePAHD&X-Amz-Signature=7d09dc185fe77bdca5150bcf84ecaec1e5b0996072881c475f3664682493e7f9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX3QI7SW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCID7me5Fm2DRu7gO3OhnjAohfWMzyaOa0ocJq6rn4eCmEAiEAnkt%2FRp9CLIi1EFyt9PAVNl26nEtrUr6Sg61pEhfjR9Mq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDGwNyA%2BExqknPoPq3SrcA9ZPPpXKlXjGV3fxkTR2jx0C7SDN73UHKEFvdJxblYY%2BCDmn7as9dqCbUI8%2B6WuOWuRPmq1UptUHy6yug6JnlC2S8C%2BglSzusjpb%2Bd3b39VddF%2B8UwsV0cDpUgfy8OtFxPrOE%2Fyn2SG%2BhtVM22gMMyogSFERx3rnzyOJJLsdlNSYFAeK4YQhkrjzGUpPr7F4Ub1Yb%2BmLruFy39G5763c8gV0YFxi6zL%2BeZjj80pvhF8FiOj9JPwnw7epyX8WXu9umIIi0Je5I3Cgmm0p7yCQEAvwUSlVg%2FykAmtOoS53qxsbF8TbgcNgBgGV5%2BkHzF1PdZB%2BbGEZXxL3U9uk04bIb9TObQcz0V7buM2gul2aSku8%2FDbAR%2Fp9r5U3290ygiy7sTnsl0Ew95DIZ8S33Irt6r3pxF1iwwMl7ZTpQTefrfOn9%2FvFLvIYlka5%2B6ufSpnpG9FkHoNzd0tSlU7FpzbrfcA3KK5QtqGRU4BbpcfwqhoLLhXspHrrUstytG4NmWKCfWkmzgNh6o7lw%2F0%2BhjUel0cq1Ur8%2BJoQ148O9MsxBnrQhv65ZAAhQUNrTSXhGoDzrf7LsxZoCEzmmpOwsumraZCC1gpE903bQPoEhZXzV8n9n2G9cZtSQ076OGW0MPL%2Bmb0GOqUBjtpaVtso9dvwk4x1663Kk5TEMS6Hmh2P3idzbTxc4JJ0N1TSN8FfkCyNcmVt0S8GUs5Pk%2B0zN9bA%2BVw45GPc5YQJQsPmtr0DRL3rpVr%2FLUfGtnRFHmcWVb6b0mjbvr2pvF9JP2Avn72yN%2BjL7orj6HxsEB%2F4kNSpUglx6ByGeWXzUb0%2BsoxvERIlVrVbsa5p3sOkaLNRM59TchvlNEerlOiePAHD&X-Amz-Signature=6ccae831e9cbb65f0790033c28a9a7c2d6f912e12388c77c1ae5b1a7385a231f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQLHHRB6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIA%2BrH%2Bu9oi6c5mUJhabVD3cH8zJpZTdkF3PsGOB1codnAiEAtDdf2Rn7Tk0frgl%2Bk0wyNQEtZkf67X2WXB3IdhSyOm8q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDNZXx5WytyCtpXSBoSrcA18Zyw8BiKzijYqntqSqUQY6SGE%2FTNDb3J41g2oK%2Fu97KrCgRUqv7oecUb%2FgO%2Bkpn95vBaqv4GVNoIsC2EpbLmRkXfsvqE7fajjawprSuan5qb5TEPHJXoIge4mpFZI6X45nOMmOn%2Bk2wh7RtY6sGjAiz2vuyQ%2BC%2F79%2BjJxx5hxD2fg%2FVfnEghxX0hVbRJhrFeqPm5OSNQen6S%2BPyzyEOKF5mZCUhi59uk%2B0z8KSjPui6nZlJE4gLRpWEcFjmraUs7eseHtyztiQF44Ob6T%2BuNCM8FEW%2FcDroTsKnoe3FH310GgkrUW5uFAP6v4C8xX5HXqIBdg1yNnlZmHHORIrK08DIRfpmOIq8cR5DlckApnpNc%2BxLVGjkbwlIKxET8XCrMqxo9vf%2BmNzdk45N2vO6JdMFDG%2FgNSjSnpPddsAZCWzhd5QuABMTb87pu0nLBFN%2B%2FViJ0GZAlrHyutvcJnvUWAT3cdaX%2BuWYMvBAc1djIbigzSmGvlqTX%2BRXQbE%2FJce5%2FihTo2wYbWezcjqftr3al5mSBKaKrySR6pciSathr0KP3v%2BjqQUvp0ITJIw8vwIE4Ck2a5dcbXKx0XoBu8EEL5TH%2B3MFEOQ8v%2B5H5E5WTkcGF5JLDUIlgnNWp8QMOX%2Bmb0GOqUBZfxAdnw7kkr0FTRVH3qNLnEoBsrZRJDLy0CxojoBZ9sDHqjZE37pXvPfkMHJNWtRqms5uF1MDXMGAZek%2BwWPDZ8awveSUzAun2SAM2I1RxZPNACFeIgibpxwKD5hn%2B8cDORVsyHHiASxrJQW9CHj3772VdfatQjdp4cl1fdI61ltyqNqMb%2FASk%2BYVg7X4vdy6ljkbIQEPHsWEJaWvZWZQSZKEVAx&X-Amz-Signature=c08520a101a6ba6cdf7d15e101d0d2a26561a49529420bdbf0a8dc4510b9b26c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FZWVQR6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQDDZ2v13jz6AXaeETx3Dt8fWOAH0fyHVxaNsMsixE4KiwIgM6SckaFpkdIuHgYKFCFrcuMLIKweQGyA4OCLDqYCtQsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDLvSrW454m%2F1ZISc3ircA%2FsRgmar%2FT0qVJvP6%2FcjLgaNk8qMf%2F9AccG6Be4XtZiwKUeRDYxQpPLgcYlh7V45RSfnSQQr%2FSKZhsO9lcBptC8HP8Jpt2ESZ2xFSPyD2BWpCc5uzOt9FqRhNuMLWxr8RYMbR6KmXt4LumuIRifpKtaRTUpaAfg0uplV%2F2xZmjg40Z84u4wfpbClRGLhQ0ap4o4ZD3czLLcHF2M%2FnT9TjU8r2EsNWc47c06uDs7AvRVo2%2FjouH%2B%2Fp8V2KpUeukmlGY9YejJly2gYzUsGZY5UFO1%2FUW5mXRRCipTf6p91tdQOEFh%2FJwksr55cFwsoozsW%2BGuWM26O2%2FVRMXahdCy9JjNEQMRJzBCotJar1YUxnmrgf26L2BFrOfJwpwXDhTmX%2BxPYECHOkPHuJJPUu3%2FdyaKUt1nESd1NFrwv46iJEglAvYZERp8a4OMxOYbE3SwnEw6nNaWR3YnAMKa1yxLOXeCtuZ2YIRJS90sx8Sfa%2BlkzIC5XrmI689ESDZsyxTfx90mtJx3F%2BNn5YqSCnPgsTGMhRmgypKhx8F8ngkPkFYu3Pjpg8eAFQqA%2FTnVcPK%2FYcrhVxH%2BBPu92GQqfcTrzPMeqmZTACKLphAMm2QNDabqDX43FV7sk8E52cmWuMKj%2Bmb0GOqUBrHVTgMF2rSDk3u1BIjholceEHhcrs0xGHwifomy%2FgHsFO%2BXa%2BD%2Fo%2BCdX7fSOMkXLIU4kDuwMMxevjCrDBdVakcPiFuSGBrFv5lBZkpcmuXdglunOD017HcPqQU0dHUx7PSvAZHHcI2WL7MQ0cAHi8%2Bdhy2XK%2FbT1vbwYWKOLNFyQ3IdiWqQRcIIZXKQGR%2BOu%2FL2JNq4mtlB4eR5dLOi48AoNKOT7&X-Amz-Signature=5d3ad9057c3d5241a1d0c8e1d215d0876dbc713e49fdaa20dbfd6db4bccedc2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRKESURL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQD067aFbVjerCuoJRchNOWQvrWK5ksbyocvXus9Oso7QgIgSL2ch5rcxAUjXfnnxQdVCdux34Hr6Cidtybby5ZsxWMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFigos0aENiVTHILLyrcA%2FGRnpvJ%2FzHvd%2BUSADZF7nRDQwL8AUGec9yqArQvfGD4yMS1RIGRrPNR6Y9E59SqdJ8s%2B1iCfYlI7Wv%2B%2BiQijvxoxU2ZB4y1qhtk22fV193bYUcFby5dLZ0l%2BmE87fgwGHs0%2FTFweK77hfHyLzDR3NYTiLjdX3WRShMIT1tBW%2FdU%2FpToPlSHKnFjr4x5Dn9jTqYbTv3iMnSm2oDzIOUA69nuR3mnHBwPnn1NaFF0Auoa1Y9FvvIzntpkLxlCiwl3QZAxVqWChywh8auiPQsSSDzy9RnSkK9vH6e4M7ZF2heKA%2B92fBKZZ8gtCDIiTCyusi4drOsVKVLxGUNR%2BHn0sz%2FfbGts0%2FTUrOYrB9iYXZ9ujUp2VJbdvM7dhl%2BRI3x1U8O%2Fr9529gS%2BccplX0AesffuHeNQ85f7Q5nFPvpkqdxiaNFOWziKqbARSpQB2MOj23dFqeDIHPpZHuXS%2Fj9eyiwLhlupuSCvNVi5rX9BpAelNJVFGbMx2OWtwz0qfb%2FXRooeRK8uBrDvQP0t3%2FDZTf6Y3frITPGfRZ0PIc9DuyUcAwQRpADJuzIXM4lN9V23x0x9tRG%2BH2LAP605EztR3PVudHND8wtV6FOd5%2F2Ts%2BfzvcUSM6C9%2F%2BIvCWiiMND%2Bmb0GOqUBMB707uJvzTbz0zDj1QYQyLWYe3zkB1pWxl4WokY7rWt3IX7v6NqSfdj3p7EDWvZVBc0SsScaW0kqRO7ukQ9DbA4HsMMz7s1zTMQPJ5OXAILVvKv4nEf8qUYIWHFGb2FTZpXQaEgtg31%2B5GTXQlw8o8iWbiNv1np6mLjOD%2FWgBizyNPdVUCAWSkjgZKS%2BzCx%2BAlYxCn5v3CB1c2rpg%2Bm%2F7%2B6IsoJB&X-Amz-Signature=f4856b6bfba0c330872d66d03a7b334b2b1cac4448fa363689632148e709cdf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRKESURL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQD067aFbVjerCuoJRchNOWQvrWK5ksbyocvXus9Oso7QgIgSL2ch5rcxAUjXfnnxQdVCdux34Hr6Cidtybby5ZsxWMq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFigos0aENiVTHILLyrcA%2FGRnpvJ%2FzHvd%2BUSADZF7nRDQwL8AUGec9yqArQvfGD4yMS1RIGRrPNR6Y9E59SqdJ8s%2B1iCfYlI7Wv%2B%2BiQijvxoxU2ZB4y1qhtk22fV193bYUcFby5dLZ0l%2BmE87fgwGHs0%2FTFweK77hfHyLzDR3NYTiLjdX3WRShMIT1tBW%2FdU%2FpToPlSHKnFjr4x5Dn9jTqYbTv3iMnSm2oDzIOUA69nuR3mnHBwPnn1NaFF0Auoa1Y9FvvIzntpkLxlCiwl3QZAxVqWChywh8auiPQsSSDzy9RnSkK9vH6e4M7ZF2heKA%2B92fBKZZ8gtCDIiTCyusi4drOsVKVLxGUNR%2BHn0sz%2FfbGts0%2FTUrOYrB9iYXZ9ujUp2VJbdvM7dhl%2BRI3x1U8O%2Fr9529gS%2BccplX0AesffuHeNQ85f7Q5nFPvpkqdxiaNFOWziKqbARSpQB2MOj23dFqeDIHPpZHuXS%2Fj9eyiwLhlupuSCvNVi5rX9BpAelNJVFGbMx2OWtwz0qfb%2FXRooeRK8uBrDvQP0t3%2FDZTf6Y3frITPGfRZ0PIc9DuyUcAwQRpADJuzIXM4lN9V23x0x9tRG%2BH2LAP605EztR3PVudHND8wtV6FOd5%2F2Ts%2BfzvcUSM6C9%2F%2BIvCWiiMND%2Bmb0GOqUBMB707uJvzTbz0zDj1QYQyLWYe3zkB1pWxl4WokY7rWt3IX7v6NqSfdj3p7EDWvZVBc0SsScaW0kqRO7ukQ9DbA4HsMMz7s1zTMQPJ5OXAILVvKv4nEf8qUYIWHFGb2FTZpXQaEgtg31%2B5GTXQlw8o8iWbiNv1np6mLjOD%2FWgBizyNPdVUCAWSkjgZKS%2BzCx%2BAlYxCn5v3CB1c2rpg%2Bm%2F7%2B6IsoJB&X-Amz-Signature=9b4dc42c4b0858e9a504d03211e87c3742a097fec7a85ec1b7ac6de9842fd282&X-Amz-SignedHeaders=host&x-id=GetObject)
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
