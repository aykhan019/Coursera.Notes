

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R42SUGEE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDk2hFruZFdIzDwzcjZvmBZBvvcu20maqlXlZPd%2FoH2gwIgB%2BZbjbySfpogDN0liIZVYYm1alEDeOr3k6qoFQUFN0QqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKW1H7V%2B7zTkwv1npyrcAzhUG4nfKY0tzvbLzumhP%2BfYSAnQkcbfjtW%2F7ZZwLrrySg1Ljm1%2FtDLrtUAodv%2B30IuVeXihCqMTPvC0Emr2t6azUghs7BPk3v%2BjPxaMPVaXgzQUNUAanbLu5INHvA83WxvLWz0H0p4KQaXRxYbQ3KTI%2B2eQi7n2mvLRr8rWNpvpdj8nevDt6ViY8BO%2BJWiORfkv5THJkDYQqz%2BpW9MAR%2FqA0y3VrL4RGYUOUGxvNphA5fultbmfxlKOAyJ%2Fya1BEmGNpDuQGP3hVVZp4LqRzKrhiZNmgKGzJOjZc6O2pQnwO1pMvOU0rWpxmlBvM0E6EficYQ1LvXtYPWWhKHpQ13aHuOoCry%2B%2F80PgFLsA6PTZRwVPWFdpTk%2FOpirLyNucxQXN%2Blr7D%2F7mhdqUick7VYCWOdNx9LS0cXVd%2BS8VOGY3T8Vky%2FIeKjIc8cCcgZ%2FXmEpOiMFLB0AZf8e6cKkcDLfccv%2FFoy0dfbixBwzuN%2BgyaBRmOAjX788d2yWIrvB4ecOb%2FgezNage7ZQ75p%2F%2BPTiISy%2FxZ8J2VYg3zJDRNMbgYxPJJchWnj9JPTKGq0BHTzN%2Fo7COZqaVjiLcaAiKgbqe4pMujvnqd81sgFTk9QbKlWjzJLJVsl2%2FIGwEMPip77wGOqUBPewuMz6%2B9moZCO%2F9fw4OZgDYnQDX%2BQKCSQv0sp7EpwDnxvSOZz7xM9K3CrWyQozRY8FBpXSES8kysJVmEnsIp4oS728jYA3TL%2FusAnsxeJa6LmbR2jMMcaKIKCTU7CsdFTPEpeHY%2FlPL0YsjB6vupGYLV%2Fktbk9XWvmzyvaoJV0JfXiUS2ZuT7QSzLaWTblpm%2B0lhvU4ehfXzrBvqSST1SfukANf&X-Amz-Signature=46c2fb447102d4d57cf3d81cb9b51ff5c917fbc4379aa2df32d7e8ada0e79710&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R42SUGEE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDk2hFruZFdIzDwzcjZvmBZBvvcu20maqlXlZPd%2FoH2gwIgB%2BZbjbySfpogDN0liIZVYYm1alEDeOr3k6qoFQUFN0QqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKW1H7V%2B7zTkwv1npyrcAzhUG4nfKY0tzvbLzumhP%2BfYSAnQkcbfjtW%2F7ZZwLrrySg1Ljm1%2FtDLrtUAodv%2B30IuVeXihCqMTPvC0Emr2t6azUghs7BPk3v%2BjPxaMPVaXgzQUNUAanbLu5INHvA83WxvLWz0H0p4KQaXRxYbQ3KTI%2B2eQi7n2mvLRr8rWNpvpdj8nevDt6ViY8BO%2BJWiORfkv5THJkDYQqz%2BpW9MAR%2FqA0y3VrL4RGYUOUGxvNphA5fultbmfxlKOAyJ%2Fya1BEmGNpDuQGP3hVVZp4LqRzKrhiZNmgKGzJOjZc6O2pQnwO1pMvOU0rWpxmlBvM0E6EficYQ1LvXtYPWWhKHpQ13aHuOoCry%2B%2F80PgFLsA6PTZRwVPWFdpTk%2FOpirLyNucxQXN%2Blr7D%2F7mhdqUick7VYCWOdNx9LS0cXVd%2BS8VOGY3T8Vky%2FIeKjIc8cCcgZ%2FXmEpOiMFLB0AZf8e6cKkcDLfccv%2FFoy0dfbixBwzuN%2BgyaBRmOAjX788d2yWIrvB4ecOb%2FgezNage7ZQ75p%2F%2BPTiISy%2FxZ8J2VYg3zJDRNMbgYxPJJchWnj9JPTKGq0BHTzN%2Fo7COZqaVjiLcaAiKgbqe4pMujvnqd81sgFTk9QbKlWjzJLJVsl2%2FIGwEMPip77wGOqUBPewuMz6%2B9moZCO%2F9fw4OZgDYnQDX%2BQKCSQv0sp7EpwDnxvSOZz7xM9K3CrWyQozRY8FBpXSES8kysJVmEnsIp4oS728jYA3TL%2FusAnsxeJa6LmbR2jMMcaKIKCTU7CsdFTPEpeHY%2FlPL0YsjB6vupGYLV%2Fktbk9XWvmzyvaoJV0JfXiUS2ZuT7QSzLaWTblpm%2B0lhvU4ehfXzrBvqSST1SfukANf&X-Amz-Signature=b80a35ddd2f66bba13664be4d837454b6d6828358f1325e0f1a76c9f355ffce1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R42SUGEE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDk2hFruZFdIzDwzcjZvmBZBvvcu20maqlXlZPd%2FoH2gwIgB%2BZbjbySfpogDN0liIZVYYm1alEDeOr3k6qoFQUFN0QqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKW1H7V%2B7zTkwv1npyrcAzhUG4nfKY0tzvbLzumhP%2BfYSAnQkcbfjtW%2F7ZZwLrrySg1Ljm1%2FtDLrtUAodv%2B30IuVeXihCqMTPvC0Emr2t6azUghs7BPk3v%2BjPxaMPVaXgzQUNUAanbLu5INHvA83WxvLWz0H0p4KQaXRxYbQ3KTI%2B2eQi7n2mvLRr8rWNpvpdj8nevDt6ViY8BO%2BJWiORfkv5THJkDYQqz%2BpW9MAR%2FqA0y3VrL4RGYUOUGxvNphA5fultbmfxlKOAyJ%2Fya1BEmGNpDuQGP3hVVZp4LqRzKrhiZNmgKGzJOjZc6O2pQnwO1pMvOU0rWpxmlBvM0E6EficYQ1LvXtYPWWhKHpQ13aHuOoCry%2B%2F80PgFLsA6PTZRwVPWFdpTk%2FOpirLyNucxQXN%2Blr7D%2F7mhdqUick7VYCWOdNx9LS0cXVd%2BS8VOGY3T8Vky%2FIeKjIc8cCcgZ%2FXmEpOiMFLB0AZf8e6cKkcDLfccv%2FFoy0dfbixBwzuN%2BgyaBRmOAjX788d2yWIrvB4ecOb%2FgezNage7ZQ75p%2F%2BPTiISy%2FxZ8J2VYg3zJDRNMbgYxPJJchWnj9JPTKGq0BHTzN%2Fo7COZqaVjiLcaAiKgbqe4pMujvnqd81sgFTk9QbKlWjzJLJVsl2%2FIGwEMPip77wGOqUBPewuMz6%2B9moZCO%2F9fw4OZgDYnQDX%2BQKCSQv0sp7EpwDnxvSOZz7xM9K3CrWyQozRY8FBpXSES8kysJVmEnsIp4oS728jYA3TL%2FusAnsxeJa6LmbR2jMMcaKIKCTU7CsdFTPEpeHY%2FlPL0YsjB6vupGYLV%2Fktbk9XWvmzyvaoJV0JfXiUS2ZuT7QSzLaWTblpm%2B0lhvU4ehfXzrBvqSST1SfukANf&X-Amz-Signature=1001d522becc6e342192b763989c48b86a9eaae758f00731d357554f7f569135&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R42SUGEE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDk2hFruZFdIzDwzcjZvmBZBvvcu20maqlXlZPd%2FoH2gwIgB%2BZbjbySfpogDN0liIZVYYm1alEDeOr3k6qoFQUFN0QqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKW1H7V%2B7zTkwv1npyrcAzhUG4nfKY0tzvbLzumhP%2BfYSAnQkcbfjtW%2F7ZZwLrrySg1Ljm1%2FtDLrtUAodv%2B30IuVeXihCqMTPvC0Emr2t6azUghs7BPk3v%2BjPxaMPVaXgzQUNUAanbLu5INHvA83WxvLWz0H0p4KQaXRxYbQ3KTI%2B2eQi7n2mvLRr8rWNpvpdj8nevDt6ViY8BO%2BJWiORfkv5THJkDYQqz%2BpW9MAR%2FqA0y3VrL4RGYUOUGxvNphA5fultbmfxlKOAyJ%2Fya1BEmGNpDuQGP3hVVZp4LqRzKrhiZNmgKGzJOjZc6O2pQnwO1pMvOU0rWpxmlBvM0E6EficYQ1LvXtYPWWhKHpQ13aHuOoCry%2B%2F80PgFLsA6PTZRwVPWFdpTk%2FOpirLyNucxQXN%2Blr7D%2F7mhdqUick7VYCWOdNx9LS0cXVd%2BS8VOGY3T8Vky%2FIeKjIc8cCcgZ%2FXmEpOiMFLB0AZf8e6cKkcDLfccv%2FFoy0dfbixBwzuN%2BgyaBRmOAjX788d2yWIrvB4ecOb%2FgezNage7ZQ75p%2F%2BPTiISy%2FxZ8J2VYg3zJDRNMbgYxPJJchWnj9JPTKGq0BHTzN%2Fo7COZqaVjiLcaAiKgbqe4pMujvnqd81sgFTk9QbKlWjzJLJVsl2%2FIGwEMPip77wGOqUBPewuMz6%2B9moZCO%2F9fw4OZgDYnQDX%2BQKCSQv0sp7EpwDnxvSOZz7xM9K3CrWyQozRY8FBpXSES8kysJVmEnsIp4oS728jYA3TL%2FusAnsxeJa6LmbR2jMMcaKIKCTU7CsdFTPEpeHY%2FlPL0YsjB6vupGYLV%2Fktbk9XWvmzyvaoJV0JfXiUS2ZuT7QSzLaWTblpm%2B0lhvU4ehfXzrBvqSST1SfukANf&X-Amz-Signature=652177487d75dfe36524ae1eeee3b54b0b3f529d44e878ddb015ca7d462e41f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R42SUGEE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDk2hFruZFdIzDwzcjZvmBZBvvcu20maqlXlZPd%2FoH2gwIgB%2BZbjbySfpogDN0liIZVYYm1alEDeOr3k6qoFQUFN0QqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKW1H7V%2B7zTkwv1npyrcAzhUG4nfKY0tzvbLzumhP%2BfYSAnQkcbfjtW%2F7ZZwLrrySg1Ljm1%2FtDLrtUAodv%2B30IuVeXihCqMTPvC0Emr2t6azUghs7BPk3v%2BjPxaMPVaXgzQUNUAanbLu5INHvA83WxvLWz0H0p4KQaXRxYbQ3KTI%2B2eQi7n2mvLRr8rWNpvpdj8nevDt6ViY8BO%2BJWiORfkv5THJkDYQqz%2BpW9MAR%2FqA0y3VrL4RGYUOUGxvNphA5fultbmfxlKOAyJ%2Fya1BEmGNpDuQGP3hVVZp4LqRzKrhiZNmgKGzJOjZc6O2pQnwO1pMvOU0rWpxmlBvM0E6EficYQ1LvXtYPWWhKHpQ13aHuOoCry%2B%2F80PgFLsA6PTZRwVPWFdpTk%2FOpirLyNucxQXN%2Blr7D%2F7mhdqUick7VYCWOdNx9LS0cXVd%2BS8VOGY3T8Vky%2FIeKjIc8cCcgZ%2FXmEpOiMFLB0AZf8e6cKkcDLfccv%2FFoy0dfbixBwzuN%2BgyaBRmOAjX788d2yWIrvB4ecOb%2FgezNage7ZQ75p%2F%2BPTiISy%2FxZ8J2VYg3zJDRNMbgYxPJJchWnj9JPTKGq0BHTzN%2Fo7COZqaVjiLcaAiKgbqe4pMujvnqd81sgFTk9QbKlWjzJLJVsl2%2FIGwEMPip77wGOqUBPewuMz6%2B9moZCO%2F9fw4OZgDYnQDX%2BQKCSQv0sp7EpwDnxvSOZz7xM9K3CrWyQozRY8FBpXSES8kysJVmEnsIp4oS728jYA3TL%2FusAnsxeJa6LmbR2jMMcaKIKCTU7CsdFTPEpeHY%2FlPL0YsjB6vupGYLV%2Fktbk9XWvmzyvaoJV0JfXiUS2ZuT7QSzLaWTblpm%2B0lhvU4ehfXzrBvqSST1SfukANf&X-Amz-Signature=8990fee745f42cb2020498d9d3bb98d62d2b92e85033acea37a4f62eae76e24e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R42SUGEE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDk2hFruZFdIzDwzcjZvmBZBvvcu20maqlXlZPd%2FoH2gwIgB%2BZbjbySfpogDN0liIZVYYm1alEDeOr3k6qoFQUFN0QqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKW1H7V%2B7zTkwv1npyrcAzhUG4nfKY0tzvbLzumhP%2BfYSAnQkcbfjtW%2F7ZZwLrrySg1Ljm1%2FtDLrtUAodv%2B30IuVeXihCqMTPvC0Emr2t6azUghs7BPk3v%2BjPxaMPVaXgzQUNUAanbLu5INHvA83WxvLWz0H0p4KQaXRxYbQ3KTI%2B2eQi7n2mvLRr8rWNpvpdj8nevDt6ViY8BO%2BJWiORfkv5THJkDYQqz%2BpW9MAR%2FqA0y3VrL4RGYUOUGxvNphA5fultbmfxlKOAyJ%2Fya1BEmGNpDuQGP3hVVZp4LqRzKrhiZNmgKGzJOjZc6O2pQnwO1pMvOU0rWpxmlBvM0E6EficYQ1LvXtYPWWhKHpQ13aHuOoCry%2B%2F80PgFLsA6PTZRwVPWFdpTk%2FOpirLyNucxQXN%2Blr7D%2F7mhdqUick7VYCWOdNx9LS0cXVd%2BS8VOGY3T8Vky%2FIeKjIc8cCcgZ%2FXmEpOiMFLB0AZf8e6cKkcDLfccv%2FFoy0dfbixBwzuN%2BgyaBRmOAjX788d2yWIrvB4ecOb%2FgezNage7ZQ75p%2F%2BPTiISy%2FxZ8J2VYg3zJDRNMbgYxPJJchWnj9JPTKGq0BHTzN%2Fo7COZqaVjiLcaAiKgbqe4pMujvnqd81sgFTk9QbKlWjzJLJVsl2%2FIGwEMPip77wGOqUBPewuMz6%2B9moZCO%2F9fw4OZgDYnQDX%2BQKCSQv0sp7EpwDnxvSOZz7xM9K3CrWyQozRY8FBpXSES8kysJVmEnsIp4oS728jYA3TL%2FusAnsxeJa6LmbR2jMMcaKIKCTU7CsdFTPEpeHY%2FlPL0YsjB6vupGYLV%2Fktbk9XWvmzyvaoJV0JfXiUS2ZuT7QSzLaWTblpm%2B0lhvU4ehfXzrBvqSST1SfukANf&X-Amz-Signature=0de5959ff26ef48fe1f822eda52df2f907e891732f0cd861e2af89bcb557d6d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R42SUGEE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDk2hFruZFdIzDwzcjZvmBZBvvcu20maqlXlZPd%2FoH2gwIgB%2BZbjbySfpogDN0liIZVYYm1alEDeOr3k6qoFQUFN0QqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKW1H7V%2B7zTkwv1npyrcAzhUG4nfKY0tzvbLzumhP%2BfYSAnQkcbfjtW%2F7ZZwLrrySg1Ljm1%2FtDLrtUAodv%2B30IuVeXihCqMTPvC0Emr2t6azUghs7BPk3v%2BjPxaMPVaXgzQUNUAanbLu5INHvA83WxvLWz0H0p4KQaXRxYbQ3KTI%2B2eQi7n2mvLRr8rWNpvpdj8nevDt6ViY8BO%2BJWiORfkv5THJkDYQqz%2BpW9MAR%2FqA0y3VrL4RGYUOUGxvNphA5fultbmfxlKOAyJ%2Fya1BEmGNpDuQGP3hVVZp4LqRzKrhiZNmgKGzJOjZc6O2pQnwO1pMvOU0rWpxmlBvM0E6EficYQ1LvXtYPWWhKHpQ13aHuOoCry%2B%2F80PgFLsA6PTZRwVPWFdpTk%2FOpirLyNucxQXN%2Blr7D%2F7mhdqUick7VYCWOdNx9LS0cXVd%2BS8VOGY3T8Vky%2FIeKjIc8cCcgZ%2FXmEpOiMFLB0AZf8e6cKkcDLfccv%2FFoy0dfbixBwzuN%2BgyaBRmOAjX788d2yWIrvB4ecOb%2FgezNage7ZQ75p%2F%2BPTiISy%2FxZ8J2VYg3zJDRNMbgYxPJJchWnj9JPTKGq0BHTzN%2Fo7COZqaVjiLcaAiKgbqe4pMujvnqd81sgFTk9QbKlWjzJLJVsl2%2FIGwEMPip77wGOqUBPewuMz6%2B9moZCO%2F9fw4OZgDYnQDX%2BQKCSQv0sp7EpwDnxvSOZz7xM9K3CrWyQozRY8FBpXSES8kysJVmEnsIp4oS728jYA3TL%2FusAnsxeJa6LmbR2jMMcaKIKCTU7CsdFTPEpeHY%2FlPL0YsjB6vupGYLV%2Fktbk9XWvmzyvaoJV0JfXiUS2ZuT7QSzLaWTblpm%2B0lhvU4ehfXzrBvqSST1SfukANf&X-Amz-Signature=cd91aa122dd2f0555011b13d0eb425591034be1a01fda8b005d8c2c3c9690952&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R42SUGEE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDk2hFruZFdIzDwzcjZvmBZBvvcu20maqlXlZPd%2FoH2gwIgB%2BZbjbySfpogDN0liIZVYYm1alEDeOr3k6qoFQUFN0QqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKW1H7V%2B7zTkwv1npyrcAzhUG4nfKY0tzvbLzumhP%2BfYSAnQkcbfjtW%2F7ZZwLrrySg1Ljm1%2FtDLrtUAodv%2B30IuVeXihCqMTPvC0Emr2t6azUghs7BPk3v%2BjPxaMPVaXgzQUNUAanbLu5INHvA83WxvLWz0H0p4KQaXRxYbQ3KTI%2B2eQi7n2mvLRr8rWNpvpdj8nevDt6ViY8BO%2BJWiORfkv5THJkDYQqz%2BpW9MAR%2FqA0y3VrL4RGYUOUGxvNphA5fultbmfxlKOAyJ%2Fya1BEmGNpDuQGP3hVVZp4LqRzKrhiZNmgKGzJOjZc6O2pQnwO1pMvOU0rWpxmlBvM0E6EficYQ1LvXtYPWWhKHpQ13aHuOoCry%2B%2F80PgFLsA6PTZRwVPWFdpTk%2FOpirLyNucxQXN%2Blr7D%2F7mhdqUick7VYCWOdNx9LS0cXVd%2BS8VOGY3T8Vky%2FIeKjIc8cCcgZ%2FXmEpOiMFLB0AZf8e6cKkcDLfccv%2FFoy0dfbixBwzuN%2BgyaBRmOAjX788d2yWIrvB4ecOb%2FgezNage7ZQ75p%2F%2BPTiISy%2FxZ8J2VYg3zJDRNMbgYxPJJchWnj9JPTKGq0BHTzN%2Fo7COZqaVjiLcaAiKgbqe4pMujvnqd81sgFTk9QbKlWjzJLJVsl2%2FIGwEMPip77wGOqUBPewuMz6%2B9moZCO%2F9fw4OZgDYnQDX%2BQKCSQv0sp7EpwDnxvSOZz7xM9K3CrWyQozRY8FBpXSES8kysJVmEnsIp4oS728jYA3TL%2FusAnsxeJa6LmbR2jMMcaKIKCTU7CsdFTPEpeHY%2FlPL0YsjB6vupGYLV%2Fktbk9XWvmzyvaoJV0JfXiUS2ZuT7QSzLaWTblpm%2B0lhvU4ehfXzrBvqSST1SfukANf&X-Amz-Signature=75c257b54897dc39b07c6f0a6dfe9680acf6f0f3849dfcbc5f6abbd4a70122e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627J4CFEP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDfoHAyQUU6eBD75lehKK4%2BsN%2BWwghRxXUXhdj4U9CLXwIhAJ72A2%2FfZpnOA5XjbLPBePi4WDf%2FRWTq9shWWQEkk7kuKogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx277pbbVsAkDZ3OcYq3AO6%2B9%2FWOea1WAn19hhqGABNa9fKVXcaSDET2YXDhM%2FakYS15%2B%2FV7Y9nrfU2tmXkutwRURWdj5PAkMbD6A4umMwIZOEoSdJv%2FEVL4Tv%2Bfk97Etvxkpm79T0s435KhP6PIABh0%2FPnqx5XM%2B712CZvMUKbQuq%2Ft%2Fmz5A0ZTD1Dqt9mwAALbRCmXUmWERegH8XxyM86AutMB8ExLpDcUtV%2FfkR61YOfdjvRsxc80%2BmOsj8CBSQZKCnMkaqSTS0FezLpzcB2lagUWp5THrOxFtPmQY41IwNdtuRfGY08XsRGStp3M%2BUZiUw5DTaloxJcW07bGSs4PoOkhiFGAmXrpjFdGwwfxKGbkGDCmwOL5WnjaXyTz83YfB6GyvZcyPaV3mVpPWXcy2MGoqeydQuom3UcHSlEf99fyBMeVUa3FEOA%2BA3uRjkSHAPizCRTtJ7rmCVtRmhSpEj1qIARVrvnB30fbkl6mUPBCL%2FOxdOvNQ7zAc%2FmzGRqjJE94jO34W9c6ai%2FvXXZVNksSZaWRZ%2B7WDH3YH3HiRmEpRrvwGoWUG%2BrY9JFSONSGOjrMq4PXD4sSOgNcXSReI7AFpyBnN%2FqkmSineDoVDXV0O34Sx0btQorkATDM7mlSnfWtYMYyq%2F3tTD9qe%2B8BjqkAQ2Uff0GZcx2%2F8iUEK9dDE74NEEZ6Rotr1hImJgnTsFFuB1sLlwl7CfywYgJtyFbfJX2DFOu4ffRkgBEI2VJxCqexnOMtXrjUKgvuXgYOv4cJ6zByJ1o42NRUix8YFLcNm07OomSDFOuSZjfPe%2BbYSOYOzorc3kEYTVmfnI%2Fj6wfk2hMosBX%2F3xNmE1ByVcxgJtLgqzAgZwarOMqnS2t9MUicXBj&X-Amz-Signature=0526596ecad5619f4fa7553931cb3091df9f169232b51c376459ba07ee3ffc30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZZR2AST%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBHH5bV1i4zvRjIWf4B2VEK3pbuXrhLmMXm7ZlmEYoHlAiEA%2BhuLhVJHOgDm5IP4fixuUw5DselmNw61eMmGQwYZ%2BNcqiAQIrf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA47n112wn2gWM4mzyrcAz2EZkwkTyZrTG%2FvG4oKSfTimwK74ThNBpRiH0dAFTYm47FRDDYbexBZLFnBaL7ZhQbDoQvg90c45iAGvQEx4rQ3vJn902GdJWwjqJ99YvOll2SUap0h2mO71ClR7TGQf%2FKmcMd2AoiL8GvnaWIevA2b1tnuyrR2lGdAVLeH7rXhtgOHyr%2Fb0XvU%2FIM54SVLFcjIB8kbobkAvsLGUW6YIPSsJEojmDyoYhwP4fQp7%2FMNJ%2Fvi1jCwQJ9Frt2l8Z3Rube90cqq6hvSjwEGY2l7QRN1OGehWbk8GI9AWI2VGneQCMVgmzRdshJUmMi%2BtwaLEpqjdCHPwAUnDKAFWTZjqIppocG2jKOeMRscX%2FKn4qpKRB5dWwtoOLxX1VUNYIFuFGzTxiSrldJmnJEZcKwpW7Oqx1p0kqsMGPXiB8qomzFhA2hJe4XmfmmvfIvAKB6fL6o%2FHuj6PqvdOO0sLk%2B8brExD%2Fsb7SY7U%2FIhy8dACxu65oJXn3QnUveO4Wdv6bPFkvzb2AQIwZ4ltQe70XzCqRUWQ2jgWxSsc8FwZ8i7DYcf2Wo26xD0%2B9yzBCEh%2FDN9gUJ%2BmyEhacmaUp8PuvFdOxjmK4SMJW5S%2BKxbpRvt0bOoxLLNJzsQQebSK8rwMNCp77wGOqUBbegbi0Gdf9V7xPciDJgFISbB0%2Fx4TaOJxEfrAglt7pkqHDGHJq0abtbeVMGiVZPzYnxuhDqjs9Auy0g8FWEUQsmpVGO8bL7M8mOCQOKGRnVJGRGUaPLyLRBBD%2BWtv1EXThy3i6hdsCeY4UFZAVNCoYYG0%2B6DXLX6r%2FqS3UneDOeuZr19Rhh4eYtMalCzPYg5PLgT3FMAlvJHcQW2yVC0StaY1M%2B3&X-Amz-Signature=fe668d30c5164d282e8861a418b61a7cf135efee3e7c30df910170ea62f59b69&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Y7XMXN3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5NIxHo8sxDyBZq41gIGxDsXkCFt%2B%2Bbq6kgURcauVEcgIhANKVZh3IAcrBFLmTTTmqXF3NKulD3wXPyfPLQMgl9fEgKogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxQSrbiAqq8j%2BtWz3Uq3AOtdU7qD1n332K4n2V8pywWPWdmE%2FgEjCG2njP9o%2FjPsULH4Unj9v7KnzWWlEJafD%2BFaMRhi1hiwIxq1gbNQwAouwwzFmSwurobAAI4rrl3PIcsx985i%2BQ9RgQMRZy5FdfkoL1lidml07xKXgT%2B8u09HAqbQBwK4sgCu7AnHfe4NDTM4vqSPmWeSthp2X06w%2F8i%2FBsXlCRXkrjtapsbHQZue1tCMixN%2BVmPBvf22foUmDr0dV9B2Dwm8%2F%2FPo7DoHY0p%2B4hFZmQhO0sT43NoOyXtIf7Um7FT1boIeL4Bo7A%2FaOLzmLEE76FuKRBZVa3I2aYUxHgCxrcj36KQIIZ2J%2F2NGiXjqRMrHb9EuUKgoWaHIhwVFIZmlnU6eFE575fJ5KihiK1PG9CwTxyDMzBRgP7dT8TyxCagQJBnVterhGfYXJdaBomasuZs%2F0tAavDLIckYGGvv4rXNI8jX4UGUjNd8irYaOKMLiA4kK%2BfKcQwvTZqHxW6o5PCCIUJjdU2V9WqjsFm6njiZpQI2SYdMIzQ3B94DWB1Iz0xuBeCZTrIhjYFpIQEAVcnogYeMWe9z5m3%2F8ItEajTz0MrMYNsi%2FeeEV%2B5UM6uItkc%2BJWI9E3h5ZcGxbBamjdO%2BtLqkTDDrqe%2B8BjqkAZG9TKEyKB8XDqiyuzWcpfc%2BmY9TldBQJHqLyYNTYH8dm0vJCdqk6Sy0cdT7%2BrB6SmveRzCIDqKpyp4xiZRCGTsGFAYqb076XE6a7g3vVATMMWgKAZl0pUVJtL%2B451VO1qZooUsQt3QfFb%2B2i%2Fzao9CjzL1d5HEhTDg6%2B27A56nfmXMogF80Zax3aglHPoG11IWd6YBMDGrtHZfrqzyi51EU0Mat&X-Amz-Signature=5e1aba7984ff7a7b35ccfd56d47ec88ef973814bf2cf121c08f9eb1c47f1bf96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Y7XMXN3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T201543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5NIxHo8sxDyBZq41gIGxDsXkCFt%2B%2Bbq6kgURcauVEcgIhANKVZh3IAcrBFLmTTTmqXF3NKulD3wXPyfPLQMgl9fEgKogECK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxQSrbiAqq8j%2BtWz3Uq3AOtdU7qD1n332K4n2V8pywWPWdmE%2FgEjCG2njP9o%2FjPsULH4Unj9v7KnzWWlEJafD%2BFaMRhi1hiwIxq1gbNQwAouwwzFmSwurobAAI4rrl3PIcsx985i%2BQ9RgQMRZy5FdfkoL1lidml07xKXgT%2B8u09HAqbQBwK4sgCu7AnHfe4NDTM4vqSPmWeSthp2X06w%2F8i%2FBsXlCRXkrjtapsbHQZue1tCMixN%2BVmPBvf22foUmDr0dV9B2Dwm8%2F%2FPo7DoHY0p%2B4hFZmQhO0sT43NoOyXtIf7Um7FT1boIeL4Bo7A%2FaOLzmLEE76FuKRBZVa3I2aYUxHgCxrcj36KQIIZ2J%2F2NGiXjqRMrHb9EuUKgoWaHIhwVFIZmlnU6eFE575fJ5KihiK1PG9CwTxyDMzBRgP7dT8TyxCagQJBnVterhGfYXJdaBomasuZs%2F0tAavDLIckYGGvv4rXNI8jX4UGUjNd8irYaOKMLiA4kK%2BfKcQwvTZqHxW6o5PCCIUJjdU2V9WqjsFm6njiZpQI2SYdMIzQ3B94DWB1Iz0xuBeCZTrIhjYFpIQEAVcnogYeMWe9z5m3%2F8ItEajTz0MrMYNsi%2FeeEV%2B5UM6uItkc%2BJWI9E3h5ZcGxbBamjdO%2BtLqkTDDrqe%2B8BjqkAZG9TKEyKB8XDqiyuzWcpfc%2BmY9TldBQJHqLyYNTYH8dm0vJCdqk6Sy0cdT7%2BrB6SmveRzCIDqKpyp4xiZRCGTsGFAYqb076XE6a7g3vVATMMWgKAZl0pUVJtL%2B451VO1qZooUsQt3QfFb%2B2i%2Fzao9CjzL1d5HEhTDg6%2B27A56nfmXMogF80Zax3aglHPoG11IWd6YBMDGrtHZfrqzyi51EU0Mat&X-Amz-Signature=4efd7dd0e3c0912974350c62e5691fb73e957165df8beea92ee373ab0bde08f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
