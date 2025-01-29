

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXDY4NMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQD2RiAwMBjH7ImB1ngKazfJBbY2UUVux63EKAD5qq6gmAIgOy9u3Jv4r8CPuZ10bY0tVqoL0QkYPILWCMmZnKOqVnIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjIvZtaAOjWITno2SrcAzoEeMBYiORLZeWCigSsAH%2FuLc6O2m7VMEQ4yA4MQwezQmBp%2F7RLPaiVGshJ6MWro0qaqj7igmSaUqeKwZQHeU9xWASXUCwVhx5xgydxXSiQDvLO8sMGz5hpDvhHL3jaNpRnmLsRrOjWbTt7Oc515yUmsgYnrlK5nQ0mCiZ00RpT61RMqLsZvv74lutZ59EGh71d8H9oIvtCQeXGH4U6WlfUa1DLuWIs5mD2wgZcGWEGh5UMbK9Rzn7JrUqxciAPElZwI%2BQiKogf5qQ4t%2BIajs6ZLihIz5cGwldWmPxCM4BmBahR%2BXYPHocJteo1VNjBxjEn8zutkERBnnAuUrcKmZJFKE%2BYnAoB6TAbcq7jeMksHhwxgpJ63pKnExxpWdHwCCEyMRg0Tj6QkLCFqQpIYqFzWsnJfikRGA3SDuTclZdpugwxK6HzBp3P8xH1x4jy%2BUlLli7koqPl%2BAqoJTD6kD4PNiOp0WT%2FdjNK18bL2G7WDWzG9VW8IN6QWTyb4OVX2P%2FGeBpxq7dtU%2BGJEpqtU7%2B6MRR9Ws9xyfEARHiG6GGNZadeX73ptM%2B6ZneIfC5UCIC1ZVC548wGKSoHdVz6FbcRBH%2FpmQXCqGi%2FiiR%2Fl%2FQFkRVPFfeyDQ8s8KUiMKm75rwGOqUBkQaYE%2FASIWGL6RX7ZmTr3PwMnHKaRjXlrS0mgPn9j0o8PvkhKeLnjExNQUStE48JCyNOVkK66Ss784tGpl8Z0n6EoG2uEkQd18n%2Bdqbphdmy0r1o2e6J%2FkybNZWELPKJtVo12tiwEWwRdavzsRlCJEhM6TcgrDjRuBoX4DK7ejbu6coJk7V8MA4a1MsfbSKwvxZk3S5M4gnIyAMzLxytUZJ3Sk%2F2&X-Amz-Signature=59ca18050666f29c7984f29d71a00570d0a4136be30e0405c1cb05e399a172d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXDY4NMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQD2RiAwMBjH7ImB1ngKazfJBbY2UUVux63EKAD5qq6gmAIgOy9u3Jv4r8CPuZ10bY0tVqoL0QkYPILWCMmZnKOqVnIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjIvZtaAOjWITno2SrcAzoEeMBYiORLZeWCigSsAH%2FuLc6O2m7VMEQ4yA4MQwezQmBp%2F7RLPaiVGshJ6MWro0qaqj7igmSaUqeKwZQHeU9xWASXUCwVhx5xgydxXSiQDvLO8sMGz5hpDvhHL3jaNpRnmLsRrOjWbTt7Oc515yUmsgYnrlK5nQ0mCiZ00RpT61RMqLsZvv74lutZ59EGh71d8H9oIvtCQeXGH4U6WlfUa1DLuWIs5mD2wgZcGWEGh5UMbK9Rzn7JrUqxciAPElZwI%2BQiKogf5qQ4t%2BIajs6ZLihIz5cGwldWmPxCM4BmBahR%2BXYPHocJteo1VNjBxjEn8zutkERBnnAuUrcKmZJFKE%2BYnAoB6TAbcq7jeMksHhwxgpJ63pKnExxpWdHwCCEyMRg0Tj6QkLCFqQpIYqFzWsnJfikRGA3SDuTclZdpugwxK6HzBp3P8xH1x4jy%2BUlLli7koqPl%2BAqoJTD6kD4PNiOp0WT%2FdjNK18bL2G7WDWzG9VW8IN6QWTyb4OVX2P%2FGeBpxq7dtU%2BGJEpqtU7%2B6MRR9Ws9xyfEARHiG6GGNZadeX73ptM%2B6ZneIfC5UCIC1ZVC548wGKSoHdVz6FbcRBH%2FpmQXCqGi%2FiiR%2Fl%2FQFkRVPFfeyDQ8s8KUiMKm75rwGOqUBkQaYE%2FASIWGL6RX7ZmTr3PwMnHKaRjXlrS0mgPn9j0o8PvkhKeLnjExNQUStE48JCyNOVkK66Ss784tGpl8Z0n6EoG2uEkQd18n%2Bdqbphdmy0r1o2e6J%2FkybNZWELPKJtVo12tiwEWwRdavzsRlCJEhM6TcgrDjRuBoX4DK7ejbu6coJk7V8MA4a1MsfbSKwvxZk3S5M4gnIyAMzLxytUZJ3Sk%2F2&X-Amz-Signature=36eefc14e10b8466081da7f3ab6b3f166fbada19f74324f228119b79ce2d7a74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXDY4NMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQD2RiAwMBjH7ImB1ngKazfJBbY2UUVux63EKAD5qq6gmAIgOy9u3Jv4r8CPuZ10bY0tVqoL0QkYPILWCMmZnKOqVnIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjIvZtaAOjWITno2SrcAzoEeMBYiORLZeWCigSsAH%2FuLc6O2m7VMEQ4yA4MQwezQmBp%2F7RLPaiVGshJ6MWro0qaqj7igmSaUqeKwZQHeU9xWASXUCwVhx5xgydxXSiQDvLO8sMGz5hpDvhHL3jaNpRnmLsRrOjWbTt7Oc515yUmsgYnrlK5nQ0mCiZ00RpT61RMqLsZvv74lutZ59EGh71d8H9oIvtCQeXGH4U6WlfUa1DLuWIs5mD2wgZcGWEGh5UMbK9Rzn7JrUqxciAPElZwI%2BQiKogf5qQ4t%2BIajs6ZLihIz5cGwldWmPxCM4BmBahR%2BXYPHocJteo1VNjBxjEn8zutkERBnnAuUrcKmZJFKE%2BYnAoB6TAbcq7jeMksHhwxgpJ63pKnExxpWdHwCCEyMRg0Tj6QkLCFqQpIYqFzWsnJfikRGA3SDuTclZdpugwxK6HzBp3P8xH1x4jy%2BUlLli7koqPl%2BAqoJTD6kD4PNiOp0WT%2FdjNK18bL2G7WDWzG9VW8IN6QWTyb4OVX2P%2FGeBpxq7dtU%2BGJEpqtU7%2B6MRR9Ws9xyfEARHiG6GGNZadeX73ptM%2B6ZneIfC5UCIC1ZVC548wGKSoHdVz6FbcRBH%2FpmQXCqGi%2FiiR%2Fl%2FQFkRVPFfeyDQ8s8KUiMKm75rwGOqUBkQaYE%2FASIWGL6RX7ZmTr3PwMnHKaRjXlrS0mgPn9j0o8PvkhKeLnjExNQUStE48JCyNOVkK66Ss784tGpl8Z0n6EoG2uEkQd18n%2Bdqbphdmy0r1o2e6J%2FkybNZWELPKJtVo12tiwEWwRdavzsRlCJEhM6TcgrDjRuBoX4DK7ejbu6coJk7V8MA4a1MsfbSKwvxZk3S5M4gnIyAMzLxytUZJ3Sk%2F2&X-Amz-Signature=a43d76a00912600c9f2ac30710f8761f1a6193ea58dfc92a2215154b1e154d62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXDY4NMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQD2RiAwMBjH7ImB1ngKazfJBbY2UUVux63EKAD5qq6gmAIgOy9u3Jv4r8CPuZ10bY0tVqoL0QkYPILWCMmZnKOqVnIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjIvZtaAOjWITno2SrcAzoEeMBYiORLZeWCigSsAH%2FuLc6O2m7VMEQ4yA4MQwezQmBp%2F7RLPaiVGshJ6MWro0qaqj7igmSaUqeKwZQHeU9xWASXUCwVhx5xgydxXSiQDvLO8sMGz5hpDvhHL3jaNpRnmLsRrOjWbTt7Oc515yUmsgYnrlK5nQ0mCiZ00RpT61RMqLsZvv74lutZ59EGh71d8H9oIvtCQeXGH4U6WlfUa1DLuWIs5mD2wgZcGWEGh5UMbK9Rzn7JrUqxciAPElZwI%2BQiKogf5qQ4t%2BIajs6ZLihIz5cGwldWmPxCM4BmBahR%2BXYPHocJteo1VNjBxjEn8zutkERBnnAuUrcKmZJFKE%2BYnAoB6TAbcq7jeMksHhwxgpJ63pKnExxpWdHwCCEyMRg0Tj6QkLCFqQpIYqFzWsnJfikRGA3SDuTclZdpugwxK6HzBp3P8xH1x4jy%2BUlLli7koqPl%2BAqoJTD6kD4PNiOp0WT%2FdjNK18bL2G7WDWzG9VW8IN6QWTyb4OVX2P%2FGeBpxq7dtU%2BGJEpqtU7%2B6MRR9Ws9xyfEARHiG6GGNZadeX73ptM%2B6ZneIfC5UCIC1ZVC548wGKSoHdVz6FbcRBH%2FpmQXCqGi%2FiiR%2Fl%2FQFkRVPFfeyDQ8s8KUiMKm75rwGOqUBkQaYE%2FASIWGL6RX7ZmTr3PwMnHKaRjXlrS0mgPn9j0o8PvkhKeLnjExNQUStE48JCyNOVkK66Ss784tGpl8Z0n6EoG2uEkQd18n%2Bdqbphdmy0r1o2e6J%2FkybNZWELPKJtVo12tiwEWwRdavzsRlCJEhM6TcgrDjRuBoX4DK7ejbu6coJk7V8MA4a1MsfbSKwvxZk3S5M4gnIyAMzLxytUZJ3Sk%2F2&X-Amz-Signature=375ec0801df6ebaf76812b771b5bc4e2fe4d38bc878486ff7f65d0b45069fe93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXDY4NMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQD2RiAwMBjH7ImB1ngKazfJBbY2UUVux63EKAD5qq6gmAIgOy9u3Jv4r8CPuZ10bY0tVqoL0QkYPILWCMmZnKOqVnIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjIvZtaAOjWITno2SrcAzoEeMBYiORLZeWCigSsAH%2FuLc6O2m7VMEQ4yA4MQwezQmBp%2F7RLPaiVGshJ6MWro0qaqj7igmSaUqeKwZQHeU9xWASXUCwVhx5xgydxXSiQDvLO8sMGz5hpDvhHL3jaNpRnmLsRrOjWbTt7Oc515yUmsgYnrlK5nQ0mCiZ00RpT61RMqLsZvv74lutZ59EGh71d8H9oIvtCQeXGH4U6WlfUa1DLuWIs5mD2wgZcGWEGh5UMbK9Rzn7JrUqxciAPElZwI%2BQiKogf5qQ4t%2BIajs6ZLihIz5cGwldWmPxCM4BmBahR%2BXYPHocJteo1VNjBxjEn8zutkERBnnAuUrcKmZJFKE%2BYnAoB6TAbcq7jeMksHhwxgpJ63pKnExxpWdHwCCEyMRg0Tj6QkLCFqQpIYqFzWsnJfikRGA3SDuTclZdpugwxK6HzBp3P8xH1x4jy%2BUlLli7koqPl%2BAqoJTD6kD4PNiOp0WT%2FdjNK18bL2G7WDWzG9VW8IN6QWTyb4OVX2P%2FGeBpxq7dtU%2BGJEpqtU7%2B6MRR9Ws9xyfEARHiG6GGNZadeX73ptM%2B6ZneIfC5UCIC1ZVC548wGKSoHdVz6FbcRBH%2FpmQXCqGi%2FiiR%2Fl%2FQFkRVPFfeyDQ8s8KUiMKm75rwGOqUBkQaYE%2FASIWGL6RX7ZmTr3PwMnHKaRjXlrS0mgPn9j0o8PvkhKeLnjExNQUStE48JCyNOVkK66Ss784tGpl8Z0n6EoG2uEkQd18n%2Bdqbphdmy0r1o2e6J%2FkybNZWELPKJtVo12tiwEWwRdavzsRlCJEhM6TcgrDjRuBoX4DK7ejbu6coJk7V8MA4a1MsfbSKwvxZk3S5M4gnIyAMzLxytUZJ3Sk%2F2&X-Amz-Signature=c3b26562b48c76af0a4a6ad85252e47e88be421fd1aefec35eb3b469494c3c9f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXDY4NMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQD2RiAwMBjH7ImB1ngKazfJBbY2UUVux63EKAD5qq6gmAIgOy9u3Jv4r8CPuZ10bY0tVqoL0QkYPILWCMmZnKOqVnIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjIvZtaAOjWITno2SrcAzoEeMBYiORLZeWCigSsAH%2FuLc6O2m7VMEQ4yA4MQwezQmBp%2F7RLPaiVGshJ6MWro0qaqj7igmSaUqeKwZQHeU9xWASXUCwVhx5xgydxXSiQDvLO8sMGz5hpDvhHL3jaNpRnmLsRrOjWbTt7Oc515yUmsgYnrlK5nQ0mCiZ00RpT61RMqLsZvv74lutZ59EGh71d8H9oIvtCQeXGH4U6WlfUa1DLuWIs5mD2wgZcGWEGh5UMbK9Rzn7JrUqxciAPElZwI%2BQiKogf5qQ4t%2BIajs6ZLihIz5cGwldWmPxCM4BmBahR%2BXYPHocJteo1VNjBxjEn8zutkERBnnAuUrcKmZJFKE%2BYnAoB6TAbcq7jeMksHhwxgpJ63pKnExxpWdHwCCEyMRg0Tj6QkLCFqQpIYqFzWsnJfikRGA3SDuTclZdpugwxK6HzBp3P8xH1x4jy%2BUlLli7koqPl%2BAqoJTD6kD4PNiOp0WT%2FdjNK18bL2G7WDWzG9VW8IN6QWTyb4OVX2P%2FGeBpxq7dtU%2BGJEpqtU7%2B6MRR9Ws9xyfEARHiG6GGNZadeX73ptM%2B6ZneIfC5UCIC1ZVC548wGKSoHdVz6FbcRBH%2FpmQXCqGi%2FiiR%2Fl%2FQFkRVPFfeyDQ8s8KUiMKm75rwGOqUBkQaYE%2FASIWGL6RX7ZmTr3PwMnHKaRjXlrS0mgPn9j0o8PvkhKeLnjExNQUStE48JCyNOVkK66Ss784tGpl8Z0n6EoG2uEkQd18n%2Bdqbphdmy0r1o2e6J%2FkybNZWELPKJtVo12tiwEWwRdavzsRlCJEhM6TcgrDjRuBoX4DK7ejbu6coJk7V8MA4a1MsfbSKwvxZk3S5M4gnIyAMzLxytUZJ3Sk%2F2&X-Amz-Signature=1472ae729c9e9861d6d6960617f387e5c4b5d586419589219d7b6b11ab8e1bc0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXDY4NMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQD2RiAwMBjH7ImB1ngKazfJBbY2UUVux63EKAD5qq6gmAIgOy9u3Jv4r8CPuZ10bY0tVqoL0QkYPILWCMmZnKOqVnIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjIvZtaAOjWITno2SrcAzoEeMBYiORLZeWCigSsAH%2FuLc6O2m7VMEQ4yA4MQwezQmBp%2F7RLPaiVGshJ6MWro0qaqj7igmSaUqeKwZQHeU9xWASXUCwVhx5xgydxXSiQDvLO8sMGz5hpDvhHL3jaNpRnmLsRrOjWbTt7Oc515yUmsgYnrlK5nQ0mCiZ00RpT61RMqLsZvv74lutZ59EGh71d8H9oIvtCQeXGH4U6WlfUa1DLuWIs5mD2wgZcGWEGh5UMbK9Rzn7JrUqxciAPElZwI%2BQiKogf5qQ4t%2BIajs6ZLihIz5cGwldWmPxCM4BmBahR%2BXYPHocJteo1VNjBxjEn8zutkERBnnAuUrcKmZJFKE%2BYnAoB6TAbcq7jeMksHhwxgpJ63pKnExxpWdHwCCEyMRg0Tj6QkLCFqQpIYqFzWsnJfikRGA3SDuTclZdpugwxK6HzBp3P8xH1x4jy%2BUlLli7koqPl%2BAqoJTD6kD4PNiOp0WT%2FdjNK18bL2G7WDWzG9VW8IN6QWTyb4OVX2P%2FGeBpxq7dtU%2BGJEpqtU7%2B6MRR9Ws9xyfEARHiG6GGNZadeX73ptM%2B6ZneIfC5UCIC1ZVC548wGKSoHdVz6FbcRBH%2FpmQXCqGi%2FiiR%2Fl%2FQFkRVPFfeyDQ8s8KUiMKm75rwGOqUBkQaYE%2FASIWGL6RX7ZmTr3PwMnHKaRjXlrS0mgPn9j0o8PvkhKeLnjExNQUStE48JCyNOVkK66Ss784tGpl8Z0n6EoG2uEkQd18n%2Bdqbphdmy0r1o2e6J%2FkybNZWELPKJtVo12tiwEWwRdavzsRlCJEhM6TcgrDjRuBoX4DK7ejbu6coJk7V8MA4a1MsfbSKwvxZk3S5M4gnIyAMzLxytUZJ3Sk%2F2&X-Amz-Signature=a8139c5c367869c5a14a23cbd9d634d517b524d40118201dcb36c3a82ef5df46&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXDY4NMI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQD2RiAwMBjH7ImB1ngKazfJBbY2UUVux63EKAD5qq6gmAIgOy9u3Jv4r8CPuZ10bY0tVqoL0QkYPILWCMmZnKOqVnIqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjIvZtaAOjWITno2SrcAzoEeMBYiORLZeWCigSsAH%2FuLc6O2m7VMEQ4yA4MQwezQmBp%2F7RLPaiVGshJ6MWro0qaqj7igmSaUqeKwZQHeU9xWASXUCwVhx5xgydxXSiQDvLO8sMGz5hpDvhHL3jaNpRnmLsRrOjWbTt7Oc515yUmsgYnrlK5nQ0mCiZ00RpT61RMqLsZvv74lutZ59EGh71d8H9oIvtCQeXGH4U6WlfUa1DLuWIs5mD2wgZcGWEGh5UMbK9Rzn7JrUqxciAPElZwI%2BQiKogf5qQ4t%2BIajs6ZLihIz5cGwldWmPxCM4BmBahR%2BXYPHocJteo1VNjBxjEn8zutkERBnnAuUrcKmZJFKE%2BYnAoB6TAbcq7jeMksHhwxgpJ63pKnExxpWdHwCCEyMRg0Tj6QkLCFqQpIYqFzWsnJfikRGA3SDuTclZdpugwxK6HzBp3P8xH1x4jy%2BUlLli7koqPl%2BAqoJTD6kD4PNiOp0WT%2FdjNK18bL2G7WDWzG9VW8IN6QWTyb4OVX2P%2FGeBpxq7dtU%2BGJEpqtU7%2B6MRR9Ws9xyfEARHiG6GGNZadeX73ptM%2B6ZneIfC5UCIC1ZVC548wGKSoHdVz6FbcRBH%2FpmQXCqGi%2FiiR%2Fl%2FQFkRVPFfeyDQ8s8KUiMKm75rwGOqUBkQaYE%2FASIWGL6RX7ZmTr3PwMnHKaRjXlrS0mgPn9j0o8PvkhKeLnjExNQUStE48JCyNOVkK66Ss784tGpl8Z0n6EoG2uEkQd18n%2Bdqbphdmy0r1o2e6J%2FkybNZWELPKJtVo12tiwEWwRdavzsRlCJEhM6TcgrDjRuBoX4DK7ejbu6coJk7V8MA4a1MsfbSKwvxZk3S5M4gnIyAMzLxytUZJ3Sk%2F2&X-Amz-Signature=12fc5f0f7a767cd308ec15e90a5c5a995ea8083af48cbaada0d3f9cfd8f29565&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BPJJLBC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCk%2FBZFKqrXvnN0VLHxjs76IDx7VNZJon9Rj989Z%2F6SQAIhAO1GMloodwg85unm1zxq%2Bc%2B84c695RotCwS%2FVq7ffTEDKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy3SPTsGHh97%2BWT%2Ff4q3AMtktWqx5C75HBahEd7WyUZN1s%2B9T9oJJf50CBVBOke5rywcpnq33W%2FYu4meihRsk7HQuTlxuWhRv3V%2FFg%2F%2BrSgF68DGZ3bs1q%2FDIvM7cBJBVSaFSKcwJrn0qaJ%2FbD6mX6TUK9qWWXWLYACJ0c4StaOpHoe7%2BpG8zKy2vjzk5Lv6wt8tpbc1AWpRUsZzg3l8Awq8F%2FbkOtJp8txxhgl7PK5nhOHT6zgJFZ5tChlQ22DwOXcaGPytcSKmHsH0b2cTvsPUILWvCUB2u15RmRkUyWS5aW3ORnzlDT9Jeb%2BAoV%2F3fieb8Otd9MznXGiptHT%2BaZ3hwIxznbIlUNw6gjGBR%2Bo2LCWWmDpm2uoZBtm5oEeVK76t%2Fc%2F1WcfUXF9J8gqRaRMPNQ8wVoSxmhXvJ9Z7J7P4odSZd4xHAfguPJjfrjh7rqh4xVoiwGcehe%2BMaJnj0QYC0vekfSwHWVh5I%2FuxFHQdZEATjiRQ9uidYUJu8HFyZw6PsHrcMrYpx%2FYEDeQekqb5jHlUc9bkvZTSPn7MBgaSBNUx5VzUqcQ0ow%2FQuPJm4OeEgchoPsxqXmmczw8BCILatXIT8aOVRKT9nTqXHhkUwCkvRWW051pXP%2BJwEdUH2WGbP4SmenkBp3YMzDLuua8BjqkAZfN0HVlPfhsH7K3rqVeOgAxmVaI7jT4Kr1X33Ff1d%2FhRpcJJu2pCDCl09SlI0Orn26n4uWlgeTBgxz4WJfEC6eaHI4w9X5YUjSgpfgSE8pW9SDWMs6JWAcEqxeJlvwwvvvXqrLFz3%2FFndYF2La%2B27zZfVv08iaWmlWKpy%2BY5DZ5na66h9UdwHNtTkxLunCWY7HuBcXFdnb8uVo9uwFgNiTKOI2g&X-Amz-Signature=7a1a55c6a8530eba89cae1542db032af963ca1e75852dc085016a395b770118b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXTCTGLV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFebHkjCGRODoUkBnTuExGCC1Qwboono6nLhIrgEeGN%2FAiA6K8dXDl9oT90apYsnQNvFYok2kG7m%2FRJC08klm7Q6eCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEAIuXtbGnSQ5XUwKKtwDo%2FORLCAxVMVDT2MOfY7loKtp0XDHdi1IykGoJ5aqsz%2FRMKgPeZwz%2FTT8OJtj3x3lRfBhvNP84EjJZuTim%2B19ZKYoUVwzyUJr52Q5SwulC0BiY4Pk6wA3%2BDuozv2VorDzjt5UKCMlvVPranyD1i5Em1FJsy6mw5HiMyAdxNgTZYnA%2FHu3kTb%2F468k%2FKbBU4D0XqvXDt0Delwdj74dZVn063eZkyaceHP7NVFMuzYoWgcwYRSMg%2BgRhlwf1Oh4bIhJ8%2BKpiL9Or3W3LoLWdDDM5Inrocl9RqJdVxi%2Bkdfm67kNu4wuqig9sR13L4DSOLfAcT1qzespwu%2Fp%2BhtK%2FSgS5Au6gMMNI8I9BgvJZ07Y%2BVnKbeEvRygdsmpQc8hYuLrRgq%2BGX%2FR%2FR41k6JVbxKDYPLiHQQfMIJge40jb6%2FeJEK%2B2cCTr0dREebkZuNuyQSuSjY8XkHjVc1NFM%2BgSYfkPpmVTIcbuZxR6g8XxXOtwc3EfGT6V2b2UmzWtLAp%2BtafhDpNL8DWTLafv%2BbJgTMnxF4zH4WYaybdW1zF2u%2BTOX6rc%2FBW1WI2JDR9E4rfGx72nZfIRH7BjYIJ07S9g00sNOxqSxF98cRBVzNoX7G0HdedhAAMbxI1K7rvOdrUwqrvmvAY6pgEePucjjWXN77bBYZcIFefBQT22JQdJsrlM6OY4nz2Q7pek1tiDmGUvwyoHU1Fhr7XF%2FuTbHhgL5ZHL8e%2BMWTuootn%2Bzl0Yvkl68JRfas7cqhZCHTxM7EXurieH4jqNM55F2rzVXnvu%2FzmtzDvug4GLQO4sxTUHnucE9Ysdwm0Eu48h6cko%2BKGtkCvFL4DN%2BRNyZl%2BbxL4fFUvyGVtlVIlViBE6d0pX&X-Amz-Signature=057ef04102eb9eb3544454f53d9aaa34532e5b8f9708c9da738973294c969f9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAK26IHF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIAR9mrGSMPOOhG%2FfBzekYbwnwWRIZkdtYM2UBdEEPvaaAiEAnEF2sso7FHqk8ch5KiF6JMF%2BQcjUZrLgD%2BT37leKQGcqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHX3ioxiSzLEleDKWyrcAzs691EMs9nzsl%2Ba8xnxo%2BMhbzS6EVsj2eO2etHZqePyKyodE%2FAafQqmXjBHP1h6Bo3hrQ%2BueTNW22yaaSTttBPr98sVcie4aZHzKBg2bJNcMryT2nkCGH4iree44DHdPbd2QjmOwZm17oAvmdWfnaJ0YGDWpYRZWYazXoHb14DYvmI0zn4Vc90TvrB4HujywR9UKFxU5poD9RpAVSBGwf%2FxfJLRoOh83AbfFBI7Ogx%2FHLAj6AQC62qf6KB2kX3dRh4sECRlFoZJh8oHxEUw1%2F3SKc4tk%2F%2BBRsXU4MUgYxhb24XEnhDGrORGP6l%2BNNvz3cBjWIUQ2g1XvkdqdRYzuawnDPLFeiEyTh7bGL30wZqa9yAcoVI72M0g0UFF%2BB95a8XolOVYVSuMq3YVuG6jK0xtMABapghAd%2BIG8eGjXRB%2B%2F9ClDINuYCReXmQLxb0euLtYFL64F8bUQYwrm66BAyPTGxepLqeJRjJfcTOyFHDNmIaL9CwAKqFEe%2F7SkmdlgTK6XHFtYcgrNaRUCRbLChPUurHzMj0z3TTnAhoJ3YLyWR%2F7tPp7vQdVZEUs4iRHwc32Vydj3wFyHVx4%2BK%2BGDJim7WnE2K7AQrycI6Nwl0069ye9wqiNN5aqUxPLMJe75rwGOqUBV8D1bcdDLxWDc12xyvK4HPq3JUm4lu4S0D6P6vNquNL4IPNch%2F3b27S8loDXjr1r0kCg18gRyYir85%2BbKo9I6E00umv%2FajDVMVAYsDasYTzfml66B1Y6nYwHvdFmM90j%2FjSK3EPZw6VyTYiUhjiz7nHzaSxK%2BoTij94LnBwR3auBoXPUUM2RvBlJMTCHTl0ZAcr3xy22dRR6ccjc6ESIddiMO9Zy&X-Amz-Signature=9540ee650c7dcf3b73b7dcec7cf1456972e4391cca6438ebb6faddaa478fc666&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAK26IHF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T051411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIAR9mrGSMPOOhG%2FfBzekYbwnwWRIZkdtYM2UBdEEPvaaAiEAnEF2sso7FHqk8ch5KiF6JMF%2BQcjUZrLgD%2BT37leKQGcqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHX3ioxiSzLEleDKWyrcAzs691EMs9nzsl%2Ba8xnxo%2BMhbzS6EVsj2eO2etHZqePyKyodE%2FAafQqmXjBHP1h6Bo3hrQ%2BueTNW22yaaSTttBPr98sVcie4aZHzKBg2bJNcMryT2nkCGH4iree44DHdPbd2QjmOwZm17oAvmdWfnaJ0YGDWpYRZWYazXoHb14DYvmI0zn4Vc90TvrB4HujywR9UKFxU5poD9RpAVSBGwf%2FxfJLRoOh83AbfFBI7Ogx%2FHLAj6AQC62qf6KB2kX3dRh4sECRlFoZJh8oHxEUw1%2F3SKc4tk%2F%2BBRsXU4MUgYxhb24XEnhDGrORGP6l%2BNNvz3cBjWIUQ2g1XvkdqdRYzuawnDPLFeiEyTh7bGL30wZqa9yAcoVI72M0g0UFF%2BB95a8XolOVYVSuMq3YVuG6jK0xtMABapghAd%2BIG8eGjXRB%2B%2F9ClDINuYCReXmQLxb0euLtYFL64F8bUQYwrm66BAyPTGxepLqeJRjJfcTOyFHDNmIaL9CwAKqFEe%2F7SkmdlgTK6XHFtYcgrNaRUCRbLChPUurHzMj0z3TTnAhoJ3YLyWR%2F7tPp7vQdVZEUs4iRHwc32Vydj3wFyHVx4%2BK%2BGDJim7WnE2K7AQrycI6Nwl0069ye9wqiNN5aqUxPLMJe75rwGOqUBV8D1bcdDLxWDc12xyvK4HPq3JUm4lu4S0D6P6vNquNL4IPNch%2F3b27S8loDXjr1r0kCg18gRyYir85%2BbKo9I6E00umv%2FajDVMVAYsDasYTzfml66B1Y6nYwHvdFmM90j%2FjSK3EPZw6VyTYiUhjiz7nHzaSxK%2BoTij94LnBwR3auBoXPUUM2RvBlJMTCHTl0ZAcr3xy22dRR6ccjc6ESIddiMO9Zy&X-Amz-Signature=f004a4a39b293d6666660e8421d29fcba6650858096b6a9c698d3b594284fe08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
