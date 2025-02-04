

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD3T6VD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCMarE7o58kpgUMJ51Mwo4acnh%2BpwpVWzxKQTl%2B1CYn4AIhAOazrH2ijTROjXfiVL5Ebsx4POrwApgwMkfUryXYl56fKv8DCDEQABoMNjM3NDIzMTgzODA1IgyJfdxftCUMipZ%2FLOAq3ANqQRTT4iLdL4MrhbtxcKhw17FMDx1Re163TCDa00hIqCrXOOQ2ahfH0L0YajFGtRYZdTuQh8yRebN4tYYg2rJVkI0omiaN%2BIqLkw0DEOp3LD8kwijNK8vntkE%2BjprdgU33Uuylyc846wegmEAvG1v%2BGTjhv9n5alTdiOU4nnG5zDZwmO%2BuKWxDUtYcEP5LI50YXecB%2FCwp%2FER0PubmI6R1KNLqRAF64DG%2FAXKCGfeYffLcx%2BNDPio2NeKqPATIq8JgYVt6g64u91NQEbuFN9VHXnR1lwEbxYt93i%2Fo0OEcPlbmyPvhWZhYPuL%2BCAlrlGxYW%2F5T6JCbnzF%2BXue4Lu%2BxAQXi7UmiOzaidBsuDIJR1frYAQfdO94DZ9fSaxAHCarMbKgrcO%2BlCqiseXNpqsKdjcjPMQkOIxL2yyT3LxnXfSp69ki0redVbt90JqjeQZBJFR%2BVbuDNlK7UznQz3kA%2BA5hUhGxX%2FJRDvsMlVw%2FwMAtZZvOcVV6Bn%2FRyiXkaPwH9TALNMFrvkiltM3IA4y76vGLdTSZeGE5GJpDsFCi2t4zH%2B%2FgoXeLlsZuZwJrnVy%2BAs0jlU69cv8MJbOHCT14OPKu3HjDcjDugWvpMkUgaNpVJkZ6eIXK%2F3gHuKDCO54i9BjqkAQKHAdLRIhsERuBW6OYT%2BJRCglZL1%2BsMamZQnwE2G8FK2uQGK%2FWbypkrsvxnkYJ5XUkP574%2BrpsnS4LGimLuGx9Rjy8di0rYzm%2F8bOdYa8kECCTqh%2Ff4ImqW%2Fh%2FQX1Z5uSRPW6uFaOsRk1fcwcLbT%2FTjsBVp%2BXn6hwpQaAoqi9zqdL%2FFw4yAH1jxON4WGHxKM8pan4MSY%2Fo1KacVYNcp45PLVdqI&X-Amz-Signature=d45fe0c2233b55ead1770a4036115961b166627bf46e4c3c68295eda22d7e6f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD3T6VD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCMarE7o58kpgUMJ51Mwo4acnh%2BpwpVWzxKQTl%2B1CYn4AIhAOazrH2ijTROjXfiVL5Ebsx4POrwApgwMkfUryXYl56fKv8DCDEQABoMNjM3NDIzMTgzODA1IgyJfdxftCUMipZ%2FLOAq3ANqQRTT4iLdL4MrhbtxcKhw17FMDx1Re163TCDa00hIqCrXOOQ2ahfH0L0YajFGtRYZdTuQh8yRebN4tYYg2rJVkI0omiaN%2BIqLkw0DEOp3LD8kwijNK8vntkE%2BjprdgU33Uuylyc846wegmEAvG1v%2BGTjhv9n5alTdiOU4nnG5zDZwmO%2BuKWxDUtYcEP5LI50YXecB%2FCwp%2FER0PubmI6R1KNLqRAF64DG%2FAXKCGfeYffLcx%2BNDPio2NeKqPATIq8JgYVt6g64u91NQEbuFN9VHXnR1lwEbxYt93i%2Fo0OEcPlbmyPvhWZhYPuL%2BCAlrlGxYW%2F5T6JCbnzF%2BXue4Lu%2BxAQXi7UmiOzaidBsuDIJR1frYAQfdO94DZ9fSaxAHCarMbKgrcO%2BlCqiseXNpqsKdjcjPMQkOIxL2yyT3LxnXfSp69ki0redVbt90JqjeQZBJFR%2BVbuDNlK7UznQz3kA%2BA5hUhGxX%2FJRDvsMlVw%2FwMAtZZvOcVV6Bn%2FRyiXkaPwH9TALNMFrvkiltM3IA4y76vGLdTSZeGE5GJpDsFCi2t4zH%2B%2FgoXeLlsZuZwJrnVy%2BAs0jlU69cv8MJbOHCT14OPKu3HjDcjDugWvpMkUgaNpVJkZ6eIXK%2F3gHuKDCO54i9BjqkAQKHAdLRIhsERuBW6OYT%2BJRCglZL1%2BsMamZQnwE2G8FK2uQGK%2FWbypkrsvxnkYJ5XUkP574%2BrpsnS4LGimLuGx9Rjy8di0rYzm%2F8bOdYa8kECCTqh%2Ff4ImqW%2Fh%2FQX1Z5uSRPW6uFaOsRk1fcwcLbT%2FTjsBVp%2BXn6hwpQaAoqi9zqdL%2FFw4yAH1jxON4WGHxKM8pan4MSY%2Fo1KacVYNcp45PLVdqI&X-Amz-Signature=5a60a0139fab5813a307aba22280534cb2c0f3fd158718314b67a34149647694&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD3T6VD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCMarE7o58kpgUMJ51Mwo4acnh%2BpwpVWzxKQTl%2B1CYn4AIhAOazrH2ijTROjXfiVL5Ebsx4POrwApgwMkfUryXYl56fKv8DCDEQABoMNjM3NDIzMTgzODA1IgyJfdxftCUMipZ%2FLOAq3ANqQRTT4iLdL4MrhbtxcKhw17FMDx1Re163TCDa00hIqCrXOOQ2ahfH0L0YajFGtRYZdTuQh8yRebN4tYYg2rJVkI0omiaN%2BIqLkw0DEOp3LD8kwijNK8vntkE%2BjprdgU33Uuylyc846wegmEAvG1v%2BGTjhv9n5alTdiOU4nnG5zDZwmO%2BuKWxDUtYcEP5LI50YXecB%2FCwp%2FER0PubmI6R1KNLqRAF64DG%2FAXKCGfeYffLcx%2BNDPio2NeKqPATIq8JgYVt6g64u91NQEbuFN9VHXnR1lwEbxYt93i%2Fo0OEcPlbmyPvhWZhYPuL%2BCAlrlGxYW%2F5T6JCbnzF%2BXue4Lu%2BxAQXi7UmiOzaidBsuDIJR1frYAQfdO94DZ9fSaxAHCarMbKgrcO%2BlCqiseXNpqsKdjcjPMQkOIxL2yyT3LxnXfSp69ki0redVbt90JqjeQZBJFR%2BVbuDNlK7UznQz3kA%2BA5hUhGxX%2FJRDvsMlVw%2FwMAtZZvOcVV6Bn%2FRyiXkaPwH9TALNMFrvkiltM3IA4y76vGLdTSZeGE5GJpDsFCi2t4zH%2B%2FgoXeLlsZuZwJrnVy%2BAs0jlU69cv8MJbOHCT14OPKu3HjDcjDugWvpMkUgaNpVJkZ6eIXK%2F3gHuKDCO54i9BjqkAQKHAdLRIhsERuBW6OYT%2BJRCglZL1%2BsMamZQnwE2G8FK2uQGK%2FWbypkrsvxnkYJ5XUkP574%2BrpsnS4LGimLuGx9Rjy8di0rYzm%2F8bOdYa8kECCTqh%2Ff4ImqW%2Fh%2FQX1Z5uSRPW6uFaOsRk1fcwcLbT%2FTjsBVp%2BXn6hwpQaAoqi9zqdL%2FFw4yAH1jxON4WGHxKM8pan4MSY%2Fo1KacVYNcp45PLVdqI&X-Amz-Signature=502ae4eecdbc95df1e38a759255e22a8734b9907762905fd49298b293453f504&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD3T6VD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCMarE7o58kpgUMJ51Mwo4acnh%2BpwpVWzxKQTl%2B1CYn4AIhAOazrH2ijTROjXfiVL5Ebsx4POrwApgwMkfUryXYl56fKv8DCDEQABoMNjM3NDIzMTgzODA1IgyJfdxftCUMipZ%2FLOAq3ANqQRTT4iLdL4MrhbtxcKhw17FMDx1Re163TCDa00hIqCrXOOQ2ahfH0L0YajFGtRYZdTuQh8yRebN4tYYg2rJVkI0omiaN%2BIqLkw0DEOp3LD8kwijNK8vntkE%2BjprdgU33Uuylyc846wegmEAvG1v%2BGTjhv9n5alTdiOU4nnG5zDZwmO%2BuKWxDUtYcEP5LI50YXecB%2FCwp%2FER0PubmI6R1KNLqRAF64DG%2FAXKCGfeYffLcx%2BNDPio2NeKqPATIq8JgYVt6g64u91NQEbuFN9VHXnR1lwEbxYt93i%2Fo0OEcPlbmyPvhWZhYPuL%2BCAlrlGxYW%2F5T6JCbnzF%2BXue4Lu%2BxAQXi7UmiOzaidBsuDIJR1frYAQfdO94DZ9fSaxAHCarMbKgrcO%2BlCqiseXNpqsKdjcjPMQkOIxL2yyT3LxnXfSp69ki0redVbt90JqjeQZBJFR%2BVbuDNlK7UznQz3kA%2BA5hUhGxX%2FJRDvsMlVw%2FwMAtZZvOcVV6Bn%2FRyiXkaPwH9TALNMFrvkiltM3IA4y76vGLdTSZeGE5GJpDsFCi2t4zH%2B%2FgoXeLlsZuZwJrnVy%2BAs0jlU69cv8MJbOHCT14OPKu3HjDcjDugWvpMkUgaNpVJkZ6eIXK%2F3gHuKDCO54i9BjqkAQKHAdLRIhsERuBW6OYT%2BJRCglZL1%2BsMamZQnwE2G8FK2uQGK%2FWbypkrsvxnkYJ5XUkP574%2BrpsnS4LGimLuGx9Rjy8di0rYzm%2F8bOdYa8kECCTqh%2Ff4ImqW%2Fh%2FQX1Z5uSRPW6uFaOsRk1fcwcLbT%2FTjsBVp%2BXn6hwpQaAoqi9zqdL%2FFw4yAH1jxON4WGHxKM8pan4MSY%2Fo1KacVYNcp45PLVdqI&X-Amz-Signature=00041e685f013d5a108146619e193974259e99bfb3069ecb1fb11cef6294111e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD3T6VD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCMarE7o58kpgUMJ51Mwo4acnh%2BpwpVWzxKQTl%2B1CYn4AIhAOazrH2ijTROjXfiVL5Ebsx4POrwApgwMkfUryXYl56fKv8DCDEQABoMNjM3NDIzMTgzODA1IgyJfdxftCUMipZ%2FLOAq3ANqQRTT4iLdL4MrhbtxcKhw17FMDx1Re163TCDa00hIqCrXOOQ2ahfH0L0YajFGtRYZdTuQh8yRebN4tYYg2rJVkI0omiaN%2BIqLkw0DEOp3LD8kwijNK8vntkE%2BjprdgU33Uuylyc846wegmEAvG1v%2BGTjhv9n5alTdiOU4nnG5zDZwmO%2BuKWxDUtYcEP5LI50YXecB%2FCwp%2FER0PubmI6R1KNLqRAF64DG%2FAXKCGfeYffLcx%2BNDPio2NeKqPATIq8JgYVt6g64u91NQEbuFN9VHXnR1lwEbxYt93i%2Fo0OEcPlbmyPvhWZhYPuL%2BCAlrlGxYW%2F5T6JCbnzF%2BXue4Lu%2BxAQXi7UmiOzaidBsuDIJR1frYAQfdO94DZ9fSaxAHCarMbKgrcO%2BlCqiseXNpqsKdjcjPMQkOIxL2yyT3LxnXfSp69ki0redVbt90JqjeQZBJFR%2BVbuDNlK7UznQz3kA%2BA5hUhGxX%2FJRDvsMlVw%2FwMAtZZvOcVV6Bn%2FRyiXkaPwH9TALNMFrvkiltM3IA4y76vGLdTSZeGE5GJpDsFCi2t4zH%2B%2FgoXeLlsZuZwJrnVy%2BAs0jlU69cv8MJbOHCT14OPKu3HjDcjDugWvpMkUgaNpVJkZ6eIXK%2F3gHuKDCO54i9BjqkAQKHAdLRIhsERuBW6OYT%2BJRCglZL1%2BsMamZQnwE2G8FK2uQGK%2FWbypkrsvxnkYJ5XUkP574%2BrpsnS4LGimLuGx9Rjy8di0rYzm%2F8bOdYa8kECCTqh%2Ff4ImqW%2Fh%2FQX1Z5uSRPW6uFaOsRk1fcwcLbT%2FTjsBVp%2BXn6hwpQaAoqi9zqdL%2FFw4yAH1jxON4WGHxKM8pan4MSY%2Fo1KacVYNcp45PLVdqI&X-Amz-Signature=6c63f5dea1aa330abd7da5abc6ab803b99c08a6d67394f7473c66df3dc6b3193&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD3T6VD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCMarE7o58kpgUMJ51Mwo4acnh%2BpwpVWzxKQTl%2B1CYn4AIhAOazrH2ijTROjXfiVL5Ebsx4POrwApgwMkfUryXYl56fKv8DCDEQABoMNjM3NDIzMTgzODA1IgyJfdxftCUMipZ%2FLOAq3ANqQRTT4iLdL4MrhbtxcKhw17FMDx1Re163TCDa00hIqCrXOOQ2ahfH0L0YajFGtRYZdTuQh8yRebN4tYYg2rJVkI0omiaN%2BIqLkw0DEOp3LD8kwijNK8vntkE%2BjprdgU33Uuylyc846wegmEAvG1v%2BGTjhv9n5alTdiOU4nnG5zDZwmO%2BuKWxDUtYcEP5LI50YXecB%2FCwp%2FER0PubmI6R1KNLqRAF64DG%2FAXKCGfeYffLcx%2BNDPio2NeKqPATIq8JgYVt6g64u91NQEbuFN9VHXnR1lwEbxYt93i%2Fo0OEcPlbmyPvhWZhYPuL%2BCAlrlGxYW%2F5T6JCbnzF%2BXue4Lu%2BxAQXi7UmiOzaidBsuDIJR1frYAQfdO94DZ9fSaxAHCarMbKgrcO%2BlCqiseXNpqsKdjcjPMQkOIxL2yyT3LxnXfSp69ki0redVbt90JqjeQZBJFR%2BVbuDNlK7UznQz3kA%2BA5hUhGxX%2FJRDvsMlVw%2FwMAtZZvOcVV6Bn%2FRyiXkaPwH9TALNMFrvkiltM3IA4y76vGLdTSZeGE5GJpDsFCi2t4zH%2B%2FgoXeLlsZuZwJrnVy%2BAs0jlU69cv8MJbOHCT14OPKu3HjDcjDugWvpMkUgaNpVJkZ6eIXK%2F3gHuKDCO54i9BjqkAQKHAdLRIhsERuBW6OYT%2BJRCglZL1%2BsMamZQnwE2G8FK2uQGK%2FWbypkrsvxnkYJ5XUkP574%2BrpsnS4LGimLuGx9Rjy8di0rYzm%2F8bOdYa8kECCTqh%2Ff4ImqW%2Fh%2FQX1Z5uSRPW6uFaOsRk1fcwcLbT%2FTjsBVp%2BXn6hwpQaAoqi9zqdL%2FFw4yAH1jxON4WGHxKM8pan4MSY%2Fo1KacVYNcp45PLVdqI&X-Amz-Signature=2b37c8ca7ac4a2e802c9849ff50f591087c3c570ab5ff19ab6e51654b6558ad9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD3T6VD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCMarE7o58kpgUMJ51Mwo4acnh%2BpwpVWzxKQTl%2B1CYn4AIhAOazrH2ijTROjXfiVL5Ebsx4POrwApgwMkfUryXYl56fKv8DCDEQABoMNjM3NDIzMTgzODA1IgyJfdxftCUMipZ%2FLOAq3ANqQRTT4iLdL4MrhbtxcKhw17FMDx1Re163TCDa00hIqCrXOOQ2ahfH0L0YajFGtRYZdTuQh8yRebN4tYYg2rJVkI0omiaN%2BIqLkw0DEOp3LD8kwijNK8vntkE%2BjprdgU33Uuylyc846wegmEAvG1v%2BGTjhv9n5alTdiOU4nnG5zDZwmO%2BuKWxDUtYcEP5LI50YXecB%2FCwp%2FER0PubmI6R1KNLqRAF64DG%2FAXKCGfeYffLcx%2BNDPio2NeKqPATIq8JgYVt6g64u91NQEbuFN9VHXnR1lwEbxYt93i%2Fo0OEcPlbmyPvhWZhYPuL%2BCAlrlGxYW%2F5T6JCbnzF%2BXue4Lu%2BxAQXi7UmiOzaidBsuDIJR1frYAQfdO94DZ9fSaxAHCarMbKgrcO%2BlCqiseXNpqsKdjcjPMQkOIxL2yyT3LxnXfSp69ki0redVbt90JqjeQZBJFR%2BVbuDNlK7UznQz3kA%2BA5hUhGxX%2FJRDvsMlVw%2FwMAtZZvOcVV6Bn%2FRyiXkaPwH9TALNMFrvkiltM3IA4y76vGLdTSZeGE5GJpDsFCi2t4zH%2B%2FgoXeLlsZuZwJrnVy%2BAs0jlU69cv8MJbOHCT14OPKu3HjDcjDugWvpMkUgaNpVJkZ6eIXK%2F3gHuKDCO54i9BjqkAQKHAdLRIhsERuBW6OYT%2BJRCglZL1%2BsMamZQnwE2G8FK2uQGK%2FWbypkrsvxnkYJ5XUkP574%2BrpsnS4LGimLuGx9Rjy8di0rYzm%2F8bOdYa8kECCTqh%2Ff4ImqW%2Fh%2FQX1Z5uSRPW6uFaOsRk1fcwcLbT%2FTjsBVp%2BXn6hwpQaAoqi9zqdL%2FFw4yAH1jxON4WGHxKM8pan4MSY%2Fo1KacVYNcp45PLVdqI&X-Amz-Signature=9391aaef94a0b51db9c5435bfa6904dd63face3c4944ce55cdd8486227b249d5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD3T6VD7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQCMarE7o58kpgUMJ51Mwo4acnh%2BpwpVWzxKQTl%2B1CYn4AIhAOazrH2ijTROjXfiVL5Ebsx4POrwApgwMkfUryXYl56fKv8DCDEQABoMNjM3NDIzMTgzODA1IgyJfdxftCUMipZ%2FLOAq3ANqQRTT4iLdL4MrhbtxcKhw17FMDx1Re163TCDa00hIqCrXOOQ2ahfH0L0YajFGtRYZdTuQh8yRebN4tYYg2rJVkI0omiaN%2BIqLkw0DEOp3LD8kwijNK8vntkE%2BjprdgU33Uuylyc846wegmEAvG1v%2BGTjhv9n5alTdiOU4nnG5zDZwmO%2BuKWxDUtYcEP5LI50YXecB%2FCwp%2FER0PubmI6R1KNLqRAF64DG%2FAXKCGfeYffLcx%2BNDPio2NeKqPATIq8JgYVt6g64u91NQEbuFN9VHXnR1lwEbxYt93i%2Fo0OEcPlbmyPvhWZhYPuL%2BCAlrlGxYW%2F5T6JCbnzF%2BXue4Lu%2BxAQXi7UmiOzaidBsuDIJR1frYAQfdO94DZ9fSaxAHCarMbKgrcO%2BlCqiseXNpqsKdjcjPMQkOIxL2yyT3LxnXfSp69ki0redVbt90JqjeQZBJFR%2BVbuDNlK7UznQz3kA%2BA5hUhGxX%2FJRDvsMlVw%2FwMAtZZvOcVV6Bn%2FRyiXkaPwH9TALNMFrvkiltM3IA4y76vGLdTSZeGE5GJpDsFCi2t4zH%2B%2FgoXeLlsZuZwJrnVy%2BAs0jlU69cv8MJbOHCT14OPKu3HjDcjDugWvpMkUgaNpVJkZ6eIXK%2F3gHuKDCO54i9BjqkAQKHAdLRIhsERuBW6OYT%2BJRCglZL1%2BsMamZQnwE2G8FK2uQGK%2FWbypkrsvxnkYJ5XUkP574%2BrpsnS4LGimLuGx9Rjy8di0rYzm%2F8bOdYa8kECCTqh%2Ff4ImqW%2Fh%2FQX1Z5uSRPW6uFaOsRk1fcwcLbT%2FTjsBVp%2BXn6hwpQaAoqi9zqdL%2FFw4yAH1jxON4WGHxKM8pan4MSY%2Fo1KacVYNcp45PLVdqI&X-Amz-Signature=8d8e2466f9c0ff8946b259b5965b0aba57888f759e9f20803d2ee2a23869afd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWR2U7U7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDYzX%2BUmRcqjdcyYg5%2BFpGqFKxQr750N%2BCSkWB5Hu5KLwIgDEPzU1gKx%2BFIG0MEOsREz7wT1qdBSUfvOlH0wkUa5osq%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDDrFcLZtRxlv9jYoTCrcA%2FUJMFEeNq0%2Fcx05UQ3%2Bgy7wJHBc4oNonvbDs0sdT%2BvOlstqjTP6uo4oekZcqSxPkt0%2FwId28GznZI3HtFDUhY2jrNjVMDOwPCRLCk%2B1gxYAr566v8nY23mTiUiLqJYwwryeQuzpOXQHawoD50zDjq4kDtzRLUr14%2BImqgTEaKioweS3v%2Bc8Sc0GXLLfD3bOySMfUjCY7dPne3x94VC7bewXDA8Q0GiLMKdVBfTl7p21%2BnmnoAoO0rfpEJ7tmM2m3cS%2BZPmSbrccYNlzPP3hT%2F5cXjeEdIaToBrMLNjYJ1SjCvYOYW9rNi6JylxvvVh0fbduLgTwkrXJfPoDgJQuDKcqq4aOYrjQ6SAhOY0rKjbuFpi4s1QSCb1XJB4PP0BXFMOlDvnBynoInIstpi6CQcynommnXUYoONUouQv4WnLKhotf8HqSLja5oDXMh10HlAut4v8oS5818aY6CsUTu40HKSpWaQFfC%2FTTkMV5%2FVNLbozenLrTJLZlWIOawwJdy2Yr8rwitApSYHCqahmIfy5U%2F9HURpr5HDu1mB%2FlbiTFPzX%2BKF4Dj4oNba791h0O6jFYino5btOAygSSfxSSzZ4VVBIWbZ1hqTJ9fMsRj1EKErFJ8IOqZhNx90EuMI%2FoiL0GOqUBBHfYmWSjD3nEs7eFZ7InjmZXdta4UIlHG2UAHUkD8hnmBshmbp3%2F7wfpnnd3DyJCiLJxFc5JTp8umOUAzm1r7qEvGcPF1o1QhIJw1m1QoROSqf%2B6qwV4YHFC8yZ%2FlppFAI%2Frnh9nUUrUxR3p3YkuWOxVe5cyN1eTk7badCSkc54ZJin9TOJNQRQkcoELhqkP1GFYzc26m4n24mnJwYUQt7zkcd7X&X-Amz-Signature=e8238a846743d846c90592ad68c2a70059e49f54a920d4d94ee1c5d070818bbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676UJU237%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIA7lk6PiWY99EMl76KwcY5LumevG6yxGkKO0K2FqJzjmAiB4WEbf8aPsG8qG6BgUmO4S11Did%2FW258zRYQKbhQQRlyr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIMuYLCqGXnhWhvfEAqKtwDUfNeUJnNIBKQnouXu%2FIlIKr850VXFHxSoH8wAH3S5tP3wRhd0bPKtVS3z7uQxuZqhjIBlI65T8nOR1iIh6gKW9bv6qOwV2ZNQ1pDE9I0BjsRlcYwKZggxxl%2B%2B1wlWXuT%2FQ335X4D0zVXptOH9ja%2B%2FfZ51%2B8n2JEAtj3vnCcL%2FyFRs6Yb1LAcVNSZI4lOI5MjAsavv80PZXZ6%2BG4B8ps6hdA42OUGcc9QAmq7kgZUDElMDGkDJSOUDiTDeHAkG%2B0nKeSz2z0d7AMzxOA2iNXR7bhilwfWACoXqHot%2FusUZuXy9BkaZxfIbeUZZU6W%2BUalXVE1WqJeqiPbvyqjDnyB1diPeYhqNlE4mUmi0FscGD8yagBFzJUUaUG%2FvruO1sbf11cRxooDidIQrLJra3iqge%2BwLSPk2rCsmSSHhSNDVDx%2BWmrQF1BC%2FxPg%2BL11WE0CE2h4xsuxG96fu1rTdmJvF4kP24qJubFeplyCymDbCkszawEYm6WdT0ZCe4fR1MFukUM0w5tifUoTMOm74IGHe0i4%2FzBXx17EgAXD4vIxrig69Z0pxAfDtY5BFSKHharobACAWGihnesdn8lFsTFdKggpDu%2Ba5HXs4SgYepLIUzojnEUnaFBOZABgEOIwxeaIvQY6pgGwe1GgA0od97i1tpMnT8aSgW6RLdc7SmQ9YpFU0GQJjcgNzh7Y0csjE9SV74JZ2LJnz3nDeYWr9TRp6g4pJMbmEt4aTzUH2I8DUo1L4FqxMieH3Xd516t%2FXAQg1jtvBh5cUxuEzSZbvD27Q1etEFPDJ4hyboIW85%2FxaLvHxUXwDNH1zlNblfX9bc0eK8XSoHBiZ4VKuyWBgPC%2FZhpbTiL6L0KhtqQf&X-Amz-Signature=c152b59d11fddc3503d7d292c8d4d1f14ae9407582945c71478a603854816e80&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WCZ74NZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIDf1ik%2BPgYmx7Kea2MnVrFO%2FdcMBHC3e0%2BDOXTbB8wa9AiEA4rOPcPr2gN3H7SHO9h1a3ZYYV60X7FqICgkzsM56Pe4q%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDH0DUVJFvRAPIfMRrCrcAzXS0%2BAVIGURvN6PXV0U4lyqR0%2BIWNx9RISRKN%2Flnkl3X38Gj4ka%2FWorKReR%2FFD4DrZSf%2BCurUpCQ1VBay%2F792swy0XtyEtRX7BJfOO2szk3o5Yd0QDCRrShM4QPxH9jIN1DfAKVy5a2V8FrOIkPreQK3RENPFZX9DuX%2B4cegJUovhUKkr%2BBot51cL5GCySF8sYew7h944tUWQDRhtgg5qZN52SzRrf9tYczHlRi4Tz1zOuI1gHSnACTe3fQ%2BYjt7OA4yqcbyiRU81V0tzGHoiii%2BRe4A4cwSdlKGNbVWawQncMM5q5GEN%2FeCI7C2RCvvCk009UY0XpAtms1j4zghFfeBzvE3Iwc0hMby8i7mWvqeJAKOKA0cblIdflAjj1JR5cZFjG4ctVmsaDi8KOYJqwC505EjmnY4bw1OEO45i0XxgUKJa5wL%2Brfukmhbs6aGZCwn5%2F%2FvdY1PMDAMoyuiK4sG%2FkuqjLfuWKSL%2FHq49YFjyq7OP%2FBFdDPPQztMGTwtXfu9YSxSaIkLm9NnuY%2FT46OreltRAIoxnSdVdilFMB6VzDH4a2QzZLoadUl7Tm5%2FH874Wtrm4Pdraxv0sIxSjXOf%2B%2FOWrCrI3NjFk5lNmt8QvIU4tHMAubbypNfMPfmiL0GOqUBnzzdXTvtPMRZImDeQGt1qgs%2BrzmPO%2B6V70oiZl7ozXJk5Grbg14gvCVNctYd4EqTsIUfGRc%2B8%2Fz%2FjHhJNKRf%2FWrJI4wUusujMRNhPC3W%2B1WIxp%2BL1%2BvbYSKnOhWN0ocy2roIo%2BNahWkxURwR9uBRh%2BlYzYZbWu8qm6SFVhlLbkGiftTTGt9tdhvs2npE5vibvhOx1giaGbow9mjiZsaavGmjVBBE&X-Amz-Signature=a30d60645ebcc6e59495cc9e2d9e74b33982cc8c4852fd3ab3776516792fbd62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WCZ74NZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIDf1ik%2BPgYmx7Kea2MnVrFO%2FdcMBHC3e0%2BDOXTbB8wa9AiEA4rOPcPr2gN3H7SHO9h1a3ZYYV60X7FqICgkzsM56Pe4q%2FwMIMRAAGgw2Mzc0MjMxODM4MDUiDH0DUVJFvRAPIfMRrCrcAzXS0%2BAVIGURvN6PXV0U4lyqR0%2BIWNx9RISRKN%2Flnkl3X38Gj4ka%2FWorKReR%2FFD4DrZSf%2BCurUpCQ1VBay%2F792swy0XtyEtRX7BJfOO2szk3o5Yd0QDCRrShM4QPxH9jIN1DfAKVy5a2V8FrOIkPreQK3RENPFZX9DuX%2B4cegJUovhUKkr%2BBot51cL5GCySF8sYew7h944tUWQDRhtgg5qZN52SzRrf9tYczHlRi4Tz1zOuI1gHSnACTe3fQ%2BYjt7OA4yqcbyiRU81V0tzGHoiii%2BRe4A4cwSdlKGNbVWawQncMM5q5GEN%2FeCI7C2RCvvCk009UY0XpAtms1j4zghFfeBzvE3Iwc0hMby8i7mWvqeJAKOKA0cblIdflAjj1JR5cZFjG4ctVmsaDi8KOYJqwC505EjmnY4bw1OEO45i0XxgUKJa5wL%2Brfukmhbs6aGZCwn5%2F%2FvdY1PMDAMoyuiK4sG%2FkuqjLfuWKSL%2FHq49YFjyq7OP%2FBFdDPPQztMGTwtXfu9YSxSaIkLm9NnuY%2FT46OreltRAIoxnSdVdilFMB6VzDH4a2QzZLoadUl7Tm5%2FH874Wtrm4Pdraxv0sIxSjXOf%2B%2FOWrCrI3NjFk5lNmt8QvIU4tHMAubbypNfMPfmiL0GOqUBnzzdXTvtPMRZImDeQGt1qgs%2BrzmPO%2B6V70oiZl7ozXJk5Grbg14gvCVNctYd4EqTsIUfGRc%2B8%2Fz%2FjHhJNKRf%2FWrJI4wUusujMRNhPC3W%2B1WIxp%2BL1%2BvbYSKnOhWN0ocy2roIo%2BNahWkxURwR9uBRh%2BlYzYZbWu8qm6SFVhlLbkGiftTTGt9tdhvs2npE5vibvhOx1giaGbow9mjiZsaavGmjVBBE&X-Amz-Signature=83c13268b47342384e40ba53965846755c9ebe705142bd1cc731cf0cae9de1dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
