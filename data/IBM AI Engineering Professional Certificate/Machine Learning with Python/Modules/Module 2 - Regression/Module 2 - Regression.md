

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT4PIUY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIGoMeXU7d2Vn1uy8WB0MOr3WIZjQKvGNDAidVH82tULDAiAmDLMYLYLXpuzIHOvKQJGuYNhtxzuw2eQDdkxkH4JQeCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMyyUrDyTW0UFyDME%2FKtwD8X33RBEn95RBJsF5VRGDc0noBoBwQUgGCPp%2Fe0BEJOumW3qMaMrVRkpOx8rtKYCvNSH3L50lxiQLWHGLWJWcuCo2k63KAPS7gDU%2B9L8EvQ7IUaJsHZ4F5FE5lHq0TDmlnDrHUvyeMJtMQuX%2FceS7V48mT2iwSkz2VcTghtsJKPvY5y1FaFy91HCGfDsjwxVIa%2FWPet5MG5UysgEX52GUDachReCPxgaycGgHiijckR8HXGFNNWG8cp8Fx%2F5Ih9qtUISBAepaWJkHHNoLHoEqVxZM9pRQ1g1kEgFVs5Wwe7xHbtmX6leg8HqLVMjeT65TED61WXDvsAa3OavSKnQg%2Bu4eu9eBuDccoMCkFmMrEjkeSnFIIh1SQPJnc8GpoOXnBC2LoxXxWEKs8xF1HFu5Azg%2FyEHW8Nt4AykFY5DKSjsxWw6zUw4mVVuRcE2lW1yV2dLXgF1nXj9WZHUlpFQ4lbySi1DeJLnC8C1jwskuRA4mgNeTMs0usdw%2Fhh3HUMUiESCrVjVjwOG2qTQdUts2sxzOGkfpTapw0Qt7gHom1pWYN1%2FZPwRi0vJAsza%2FNLdBJ6dNb0kPLAclKk1AF9fgmycr%2Bzf1a2WIuXkJb8cNqdz4nOql4Su9yxZpyXAwnYuNvQY6pgG%2FPmeOjIrn0%2Buod7gdNCuf065iVtrjKwJb0rVwPnvy196tqveX7qeLbBixo5bnIcFiaRpDgszZAfFrceLVcyvVUJ%2B%2BtuX85ZK112dloM1NoR6B%2BDD08BWU75R38iVcGOgQatGmLwFAnkr99xq0omjnI7BXX9d9dSvpn3gjEjA5osKonR76XjmOjjrzRnV%2FlAfbhp7YsrAMNpmDixLtXZD6%2BBUNHkdz&X-Amz-Signature=e4981b4316253161857947151f9ca0923d016c06c7883a6424312cf802dd4a1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT4PIUY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIGoMeXU7d2Vn1uy8WB0MOr3WIZjQKvGNDAidVH82tULDAiAmDLMYLYLXpuzIHOvKQJGuYNhtxzuw2eQDdkxkH4JQeCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMyyUrDyTW0UFyDME%2FKtwD8X33RBEn95RBJsF5VRGDc0noBoBwQUgGCPp%2Fe0BEJOumW3qMaMrVRkpOx8rtKYCvNSH3L50lxiQLWHGLWJWcuCo2k63KAPS7gDU%2B9L8EvQ7IUaJsHZ4F5FE5lHq0TDmlnDrHUvyeMJtMQuX%2FceS7V48mT2iwSkz2VcTghtsJKPvY5y1FaFy91HCGfDsjwxVIa%2FWPet5MG5UysgEX52GUDachReCPxgaycGgHiijckR8HXGFNNWG8cp8Fx%2F5Ih9qtUISBAepaWJkHHNoLHoEqVxZM9pRQ1g1kEgFVs5Wwe7xHbtmX6leg8HqLVMjeT65TED61WXDvsAa3OavSKnQg%2Bu4eu9eBuDccoMCkFmMrEjkeSnFIIh1SQPJnc8GpoOXnBC2LoxXxWEKs8xF1HFu5Azg%2FyEHW8Nt4AykFY5DKSjsxWw6zUw4mVVuRcE2lW1yV2dLXgF1nXj9WZHUlpFQ4lbySi1DeJLnC8C1jwskuRA4mgNeTMs0usdw%2Fhh3HUMUiESCrVjVjwOG2qTQdUts2sxzOGkfpTapw0Qt7gHom1pWYN1%2FZPwRi0vJAsza%2FNLdBJ6dNb0kPLAclKk1AF9fgmycr%2Bzf1a2WIuXkJb8cNqdz4nOql4Su9yxZpyXAwnYuNvQY6pgG%2FPmeOjIrn0%2Buod7gdNCuf065iVtrjKwJb0rVwPnvy196tqveX7qeLbBixo5bnIcFiaRpDgszZAfFrceLVcyvVUJ%2B%2BtuX85ZK112dloM1NoR6B%2BDD08BWU75R38iVcGOgQatGmLwFAnkr99xq0omjnI7BXX9d9dSvpn3gjEjA5osKonR76XjmOjjrzRnV%2FlAfbhp7YsrAMNpmDixLtXZD6%2BBUNHkdz&X-Amz-Signature=8aba41259642a3bf55d6331c03c87a1d81ba553aa185aaea9f7e374f069c759a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT4PIUY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIGoMeXU7d2Vn1uy8WB0MOr3WIZjQKvGNDAidVH82tULDAiAmDLMYLYLXpuzIHOvKQJGuYNhtxzuw2eQDdkxkH4JQeCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMyyUrDyTW0UFyDME%2FKtwD8X33RBEn95RBJsF5VRGDc0noBoBwQUgGCPp%2Fe0BEJOumW3qMaMrVRkpOx8rtKYCvNSH3L50lxiQLWHGLWJWcuCo2k63KAPS7gDU%2B9L8EvQ7IUaJsHZ4F5FE5lHq0TDmlnDrHUvyeMJtMQuX%2FceS7V48mT2iwSkz2VcTghtsJKPvY5y1FaFy91HCGfDsjwxVIa%2FWPet5MG5UysgEX52GUDachReCPxgaycGgHiijckR8HXGFNNWG8cp8Fx%2F5Ih9qtUISBAepaWJkHHNoLHoEqVxZM9pRQ1g1kEgFVs5Wwe7xHbtmX6leg8HqLVMjeT65TED61WXDvsAa3OavSKnQg%2Bu4eu9eBuDccoMCkFmMrEjkeSnFIIh1SQPJnc8GpoOXnBC2LoxXxWEKs8xF1HFu5Azg%2FyEHW8Nt4AykFY5DKSjsxWw6zUw4mVVuRcE2lW1yV2dLXgF1nXj9WZHUlpFQ4lbySi1DeJLnC8C1jwskuRA4mgNeTMs0usdw%2Fhh3HUMUiESCrVjVjwOG2qTQdUts2sxzOGkfpTapw0Qt7gHom1pWYN1%2FZPwRi0vJAsza%2FNLdBJ6dNb0kPLAclKk1AF9fgmycr%2Bzf1a2WIuXkJb8cNqdz4nOql4Su9yxZpyXAwnYuNvQY6pgG%2FPmeOjIrn0%2Buod7gdNCuf065iVtrjKwJb0rVwPnvy196tqveX7qeLbBixo5bnIcFiaRpDgszZAfFrceLVcyvVUJ%2B%2BtuX85ZK112dloM1NoR6B%2BDD08BWU75R38iVcGOgQatGmLwFAnkr99xq0omjnI7BXX9d9dSvpn3gjEjA5osKonR76XjmOjjrzRnV%2FlAfbhp7YsrAMNpmDixLtXZD6%2BBUNHkdz&X-Amz-Signature=904cbaa768665634c4314fa6faaaeb306e33141911bbb35a254ef4af487d209e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT4PIUY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIGoMeXU7d2Vn1uy8WB0MOr3WIZjQKvGNDAidVH82tULDAiAmDLMYLYLXpuzIHOvKQJGuYNhtxzuw2eQDdkxkH4JQeCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMyyUrDyTW0UFyDME%2FKtwD8X33RBEn95RBJsF5VRGDc0noBoBwQUgGCPp%2Fe0BEJOumW3qMaMrVRkpOx8rtKYCvNSH3L50lxiQLWHGLWJWcuCo2k63KAPS7gDU%2B9L8EvQ7IUaJsHZ4F5FE5lHq0TDmlnDrHUvyeMJtMQuX%2FceS7V48mT2iwSkz2VcTghtsJKPvY5y1FaFy91HCGfDsjwxVIa%2FWPet5MG5UysgEX52GUDachReCPxgaycGgHiijckR8HXGFNNWG8cp8Fx%2F5Ih9qtUISBAepaWJkHHNoLHoEqVxZM9pRQ1g1kEgFVs5Wwe7xHbtmX6leg8HqLVMjeT65TED61WXDvsAa3OavSKnQg%2Bu4eu9eBuDccoMCkFmMrEjkeSnFIIh1SQPJnc8GpoOXnBC2LoxXxWEKs8xF1HFu5Azg%2FyEHW8Nt4AykFY5DKSjsxWw6zUw4mVVuRcE2lW1yV2dLXgF1nXj9WZHUlpFQ4lbySi1DeJLnC8C1jwskuRA4mgNeTMs0usdw%2Fhh3HUMUiESCrVjVjwOG2qTQdUts2sxzOGkfpTapw0Qt7gHom1pWYN1%2FZPwRi0vJAsza%2FNLdBJ6dNb0kPLAclKk1AF9fgmycr%2Bzf1a2WIuXkJb8cNqdz4nOql4Su9yxZpyXAwnYuNvQY6pgG%2FPmeOjIrn0%2Buod7gdNCuf065iVtrjKwJb0rVwPnvy196tqveX7qeLbBixo5bnIcFiaRpDgszZAfFrceLVcyvVUJ%2B%2BtuX85ZK112dloM1NoR6B%2BDD08BWU75R38iVcGOgQatGmLwFAnkr99xq0omjnI7BXX9d9dSvpn3gjEjA5osKonR76XjmOjjrzRnV%2FlAfbhp7YsrAMNpmDixLtXZD6%2BBUNHkdz&X-Amz-Signature=0eeb340b18cbb1443524d7169775b3106c01b8f6587dae0536f2dfad85182550&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT4PIUY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIGoMeXU7d2Vn1uy8WB0MOr3WIZjQKvGNDAidVH82tULDAiAmDLMYLYLXpuzIHOvKQJGuYNhtxzuw2eQDdkxkH4JQeCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMyyUrDyTW0UFyDME%2FKtwD8X33RBEn95RBJsF5VRGDc0noBoBwQUgGCPp%2Fe0BEJOumW3qMaMrVRkpOx8rtKYCvNSH3L50lxiQLWHGLWJWcuCo2k63KAPS7gDU%2B9L8EvQ7IUaJsHZ4F5FE5lHq0TDmlnDrHUvyeMJtMQuX%2FceS7V48mT2iwSkz2VcTghtsJKPvY5y1FaFy91HCGfDsjwxVIa%2FWPet5MG5UysgEX52GUDachReCPxgaycGgHiijckR8HXGFNNWG8cp8Fx%2F5Ih9qtUISBAepaWJkHHNoLHoEqVxZM9pRQ1g1kEgFVs5Wwe7xHbtmX6leg8HqLVMjeT65TED61WXDvsAa3OavSKnQg%2Bu4eu9eBuDccoMCkFmMrEjkeSnFIIh1SQPJnc8GpoOXnBC2LoxXxWEKs8xF1HFu5Azg%2FyEHW8Nt4AykFY5DKSjsxWw6zUw4mVVuRcE2lW1yV2dLXgF1nXj9WZHUlpFQ4lbySi1DeJLnC8C1jwskuRA4mgNeTMs0usdw%2Fhh3HUMUiESCrVjVjwOG2qTQdUts2sxzOGkfpTapw0Qt7gHom1pWYN1%2FZPwRi0vJAsza%2FNLdBJ6dNb0kPLAclKk1AF9fgmycr%2Bzf1a2WIuXkJb8cNqdz4nOql4Su9yxZpyXAwnYuNvQY6pgG%2FPmeOjIrn0%2Buod7gdNCuf065iVtrjKwJb0rVwPnvy196tqveX7qeLbBixo5bnIcFiaRpDgszZAfFrceLVcyvVUJ%2B%2BtuX85ZK112dloM1NoR6B%2BDD08BWU75R38iVcGOgQatGmLwFAnkr99xq0omjnI7BXX9d9dSvpn3gjEjA5osKonR76XjmOjjrzRnV%2FlAfbhp7YsrAMNpmDixLtXZD6%2BBUNHkdz&X-Amz-Signature=57d95da1136bd0dda087d3834f136d540855a1043319c4924f93a443e234bf94&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT4PIUY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIGoMeXU7d2Vn1uy8WB0MOr3WIZjQKvGNDAidVH82tULDAiAmDLMYLYLXpuzIHOvKQJGuYNhtxzuw2eQDdkxkH4JQeCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMyyUrDyTW0UFyDME%2FKtwD8X33RBEn95RBJsF5VRGDc0noBoBwQUgGCPp%2Fe0BEJOumW3qMaMrVRkpOx8rtKYCvNSH3L50lxiQLWHGLWJWcuCo2k63KAPS7gDU%2B9L8EvQ7IUaJsHZ4F5FE5lHq0TDmlnDrHUvyeMJtMQuX%2FceS7V48mT2iwSkz2VcTghtsJKPvY5y1FaFy91HCGfDsjwxVIa%2FWPet5MG5UysgEX52GUDachReCPxgaycGgHiijckR8HXGFNNWG8cp8Fx%2F5Ih9qtUISBAepaWJkHHNoLHoEqVxZM9pRQ1g1kEgFVs5Wwe7xHbtmX6leg8HqLVMjeT65TED61WXDvsAa3OavSKnQg%2Bu4eu9eBuDccoMCkFmMrEjkeSnFIIh1SQPJnc8GpoOXnBC2LoxXxWEKs8xF1HFu5Azg%2FyEHW8Nt4AykFY5DKSjsxWw6zUw4mVVuRcE2lW1yV2dLXgF1nXj9WZHUlpFQ4lbySi1DeJLnC8C1jwskuRA4mgNeTMs0usdw%2Fhh3HUMUiESCrVjVjwOG2qTQdUts2sxzOGkfpTapw0Qt7gHom1pWYN1%2FZPwRi0vJAsza%2FNLdBJ6dNb0kPLAclKk1AF9fgmycr%2Bzf1a2WIuXkJb8cNqdz4nOql4Su9yxZpyXAwnYuNvQY6pgG%2FPmeOjIrn0%2Buod7gdNCuf065iVtrjKwJb0rVwPnvy196tqveX7qeLbBixo5bnIcFiaRpDgszZAfFrceLVcyvVUJ%2B%2BtuX85ZK112dloM1NoR6B%2BDD08BWU75R38iVcGOgQatGmLwFAnkr99xq0omjnI7BXX9d9dSvpn3gjEjA5osKonR76XjmOjjrzRnV%2FlAfbhp7YsrAMNpmDixLtXZD6%2BBUNHkdz&X-Amz-Signature=df0bbabf441e35549898070c395e23293de59cd02c2e3aab5701a0afbe9b8ef6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT4PIUY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIGoMeXU7d2Vn1uy8WB0MOr3WIZjQKvGNDAidVH82tULDAiAmDLMYLYLXpuzIHOvKQJGuYNhtxzuw2eQDdkxkH4JQeCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMyyUrDyTW0UFyDME%2FKtwD8X33RBEn95RBJsF5VRGDc0noBoBwQUgGCPp%2Fe0BEJOumW3qMaMrVRkpOx8rtKYCvNSH3L50lxiQLWHGLWJWcuCo2k63KAPS7gDU%2B9L8EvQ7IUaJsHZ4F5FE5lHq0TDmlnDrHUvyeMJtMQuX%2FceS7V48mT2iwSkz2VcTghtsJKPvY5y1FaFy91HCGfDsjwxVIa%2FWPet5MG5UysgEX52GUDachReCPxgaycGgHiijckR8HXGFNNWG8cp8Fx%2F5Ih9qtUISBAepaWJkHHNoLHoEqVxZM9pRQ1g1kEgFVs5Wwe7xHbtmX6leg8HqLVMjeT65TED61WXDvsAa3OavSKnQg%2Bu4eu9eBuDccoMCkFmMrEjkeSnFIIh1SQPJnc8GpoOXnBC2LoxXxWEKs8xF1HFu5Azg%2FyEHW8Nt4AykFY5DKSjsxWw6zUw4mVVuRcE2lW1yV2dLXgF1nXj9WZHUlpFQ4lbySi1DeJLnC8C1jwskuRA4mgNeTMs0usdw%2Fhh3HUMUiESCrVjVjwOG2qTQdUts2sxzOGkfpTapw0Qt7gHom1pWYN1%2FZPwRi0vJAsza%2FNLdBJ6dNb0kPLAclKk1AF9fgmycr%2Bzf1a2WIuXkJb8cNqdz4nOql4Su9yxZpyXAwnYuNvQY6pgG%2FPmeOjIrn0%2Buod7gdNCuf065iVtrjKwJb0rVwPnvy196tqveX7qeLbBixo5bnIcFiaRpDgszZAfFrceLVcyvVUJ%2B%2BtuX85ZK112dloM1NoR6B%2BDD08BWU75R38iVcGOgQatGmLwFAnkr99xq0omjnI7BXX9d9dSvpn3gjEjA5osKonR76XjmOjjrzRnV%2FlAfbhp7YsrAMNpmDixLtXZD6%2BBUNHkdz&X-Amz-Signature=e9b1e8939d88979254bea2b960a6a222a6a9ff74f0109dc111dc42d259112a49&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TT4PIUY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIGoMeXU7d2Vn1uy8WB0MOr3WIZjQKvGNDAidVH82tULDAiAmDLMYLYLXpuzIHOvKQJGuYNhtxzuw2eQDdkxkH4JQeCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMyyUrDyTW0UFyDME%2FKtwD8X33RBEn95RBJsF5VRGDc0noBoBwQUgGCPp%2Fe0BEJOumW3qMaMrVRkpOx8rtKYCvNSH3L50lxiQLWHGLWJWcuCo2k63KAPS7gDU%2B9L8EvQ7IUaJsHZ4F5FE5lHq0TDmlnDrHUvyeMJtMQuX%2FceS7V48mT2iwSkz2VcTghtsJKPvY5y1FaFy91HCGfDsjwxVIa%2FWPet5MG5UysgEX52GUDachReCPxgaycGgHiijckR8HXGFNNWG8cp8Fx%2F5Ih9qtUISBAepaWJkHHNoLHoEqVxZM9pRQ1g1kEgFVs5Wwe7xHbtmX6leg8HqLVMjeT65TED61WXDvsAa3OavSKnQg%2Bu4eu9eBuDccoMCkFmMrEjkeSnFIIh1SQPJnc8GpoOXnBC2LoxXxWEKs8xF1HFu5Azg%2FyEHW8Nt4AykFY5DKSjsxWw6zUw4mVVuRcE2lW1yV2dLXgF1nXj9WZHUlpFQ4lbySi1DeJLnC8C1jwskuRA4mgNeTMs0usdw%2Fhh3HUMUiESCrVjVjwOG2qTQdUts2sxzOGkfpTapw0Qt7gHom1pWYN1%2FZPwRi0vJAsza%2FNLdBJ6dNb0kPLAclKk1AF9fgmycr%2Bzf1a2WIuXkJb8cNqdz4nOql4Su9yxZpyXAwnYuNvQY6pgG%2FPmeOjIrn0%2Buod7gdNCuf065iVtrjKwJb0rVwPnvy196tqveX7qeLbBixo5bnIcFiaRpDgszZAfFrceLVcyvVUJ%2B%2BtuX85ZK112dloM1NoR6B%2BDD08BWU75R38iVcGOgQatGmLwFAnkr99xq0omjnI7BXX9d9dSvpn3gjEjA5osKonR76XjmOjjrzRnV%2FlAfbhp7YsrAMNpmDixLtXZD6%2BBUNHkdz&X-Amz-Signature=b842141142b0886b20d334434a380e528c0368929176908c20db3442a5bdbd9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WOK4LR7J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCICj7CLla%2BLE8eYIQAF3R%2Byz9C%2B8UDuxR1unpQHi3AZEWAiBA4vRXPtVZcYixol%2BTsQUF0WwalMud3Px8QtYNyCL57Sr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMhF7Euv0fGTTSFRWFKtwDptQja6dx%2FF9cU0eVqE3oNkCng5%2BhsXwKNb%2FtzgOc58wzW5J8sWbjc5cP2jzHiTXMcRhx0A6WgibiLVf48v13NVZVvohzXgA1jJo33p6u1lROYbeW4uej39mViHz%2Fm%2BuYfjFzXIShs0JvWt8Q6a5FKajZPYoe0mSCIiD%2By3aLvu0ZO%2Fh%2BkyFqhTydXpfB33l7c4Bn0bpkYRMOMXH1ram%2FSYjGpDJQjfW1IWTNpq9siw3v%2F3aCxg4%2F8JSlKhAnymP6HUzuR8i2abjjDHjuhPX2np7hd4hJm6fkDuPVAHFszjaycbhZT8R6asCbauaC4A9p%2FFD8hlBi4E0BDsuFeHh4lgzsu4I1nepOkAbZnBSzvuwlVfsCmnnueiu0DM4KSHxCN%2BQfUNAs5qdhJ6LK5X6iXx6uXwFl3AA%2BNsbKx7oaa1okpLJaspIA2zo4kKQBWIzN3vS7Qs%2Bh7UI1yAhIZ%2F6h7SwPtC98vJKGWmKym4o%2Fb7%2Fma5yxQnKdH85xD9PDFdfUKdIzkgDAyKYtyB%2BiU9HUfbzENIMivCvl4afnhzfoa50bgCBasdqYpovbMYWq%2Fr30rJGH8nxRKcnD6ZjxE%2BWH08WG46tdu55RRekbsp5ixpNBBkVnAOb9fvYbTDUwlIuNvQY6pgFWM5yO20Cg3iG%2BzQGEHJBzNDXDCSv6C9%2FLDcW8B884Sk376jfr1ibMD75IV97svD9h3xkXGDAQlHgnypQuXAZDi4D9j7aaZmydTCGpLpZmpjHUg9oPZsZWv%2BHyMvcKa0NT%2FV5Y%2FGhJZEDgHLDDFeqoUDTAzVdWmug8%2F4bagkI0VOhgUoHx9lR%2FNxK6exP027GJMfDXts4PfI5fxTfFkiH1XrIqZJXD&X-Amz-Signature=4084ad239b77c60ee0586e664501c52f3de0d7830ee659bbae07b1cd72463ff6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S52Q2HCR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCWbAsjtB%2F%2BB%2Bi0Eq%2F3ia9R2JlgLLi8DIdwciWPr%2Faw9wIhAPYfJS8BOB7CqOqq8Rox25m%2F2hZCsvV5LYoxd6gXU9CjKv8DCEQQABoMNjM3NDIzMTgzODA1IgzO1bKYTkzmJ2bq8xEq3ANc7B7dUzAZxa%2BS%2FGnQtTt7OIEZ5Uuy0Df%2BbZ%2F3i9LwpLeT2nnqeQjDY2Yp77%2B9hcKv3RGgBieba%2BnlXZAbSjRwIVGbqtwq6CYMo5EpHUyEItgoe8OqLiYQZlpERHPw4mMOhG6XrYxaTGsMtQQOIjhzsSW7OaE3oN1DtAV1Sm1zmI%2FYEFkkv5k7fz25LrKkWw8PHwsxtGzuMVmeULueKGavhDUkZPMxt5eTTSY4OExPhfOcJ8RDzaMBK66goCiBLrwL9KFI9d0ahdLkIP35CUbjG2mw2P6lBtwnCMcIcHk8R5npScVqGJnRRqAy7WKt55GXBaBjl18Tm4r8sAKLxa8OpYaoMp%2Fmurd%2BiYICtvwB4EGXsI4tLDZL%2Bc83ecnBch3efLQZ0kbMMBdj7hTe56HrnnhYT8AtGzboHdpldyoRxzU2UjbwA0RZDZyvUI225rPPC2cD8gHpri7N3pgYWiH8udZP6tkOXLt3S5dDfgGy58LvXQkP8mePNBeH2vEYEnmnBnBu9NXuaW9FtnzEm1e749alC4dZOGWjn%2FY1LVTs0cqGvHmne3H6DsI4V01pvxWE%2F2T1WJcUgxOWXA8lM4vsBi2Nf5QX0ztiRt0VAOgwc%2FM6l09RDpjthbOW%2BTDcio29BjqkAbREUwfZBkZm%2BVAF6zf%2Be9H4rPwzYqmzZCBtUmGuLqCb%2FQ%2F8CwyVHgsF1pds4OM86LulGrSkvc3K%2BEuhsYZRl6R2nESFv%2F4Y0lwnScbO2XMXrJ2EXHyhwKbXVC2xkQa24MozM41EodTqlkSnf%2BvppXzTIpZySDebX2kkQjBi%2Brqru5qvBYGIDtx51rQqJQIez6c%2BKTTdSvw11FTFeKAfT2FQNIGC&X-Amz-Signature=73e0af333c563476aa1e60f6411df417c5fec83d7efc24eacfff189bcffbb5c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXVTJFB6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDf4m1TPEiEmkuPS1IGCeZH0rwQRhOLPA1lGBr8%2B99HkAIhAN63JMRzXzVqQ8S%2BQqhi%2FpOgfKBklUDkpVREEMII0Ay9Kv8DCEQQABoMNjM3NDIzMTgzODA1IgxuHkIpsk6ek8OWf38q3AN0o8%2FbvDu%2Bziv9V%2BR3aEaSb2d5%2Fwfvr3VCqW7Pm97ceADfzJF08WrAv5dqkeXuC3gEmvBra89MzIHUwd4eH4fzkflCcZNBVCbZ9Wy1H9O5DiCQ85V0kr%2FY2RCVJofbT0Ehe1rnN%2B26lOv0raw%2BNR03XRwOJOrcxb0nYje2vZB%2B%2BmmwAHoBJwnN01nxa6OvZhuWLEHbsv2gZs21ZE2wCkvqJ1QrkjIS290XDsw8XpGrsx3JkhIBTK3bLk84zLVDrohvaZekkTLtS6Od6mnSehjcpV5ge8VmDw%2FTvbVVLBcKnJHzZ1Q61IBm1XJh%2FSkldQqe3ET0jTro7UDwLEBPmP7qofB7%2FYWItwQelLWZGmWvtUCelJxlhnOaW60JHd056xPA7BkDA8IbjF71ZH%2FeQ8cJxL70lWZcNa90eStdcLKKnMQcNBAoOOwiEMlaPlSkufyqkc3TPaLawh09mZRbVmKd15cjN6xXMB%2F9L%2BgEaH9VP7fzRga8bqZ1EmhbYTkOKaYcJca6FraYldePOT%2BTkurYskOL6Gmxst8RXC77epsnpl8CtP8gzNnivR6t23W%2BfGFkF82n%2F7dVaFBZ95jXgmP6g9%2F12WUw2lsE%2FzvHNmUqI8KKaAK44ObEYwiDEDC0i429BjqkAW%2FcLsfPTYZZJdrpouczx%2BiZXBMZgIV2yMk2yp9Ze7yxR3o3tU%2B5KqLSjPuROLJVDn35X%2BilsrDle2Y0jJpWEw97ILgKEsJCTdRU0JBzr7ncusr%2BvB2Zg9zhrGVwzrKKUOzjL2c9FjMlFCelporIPSF2mHSixu1xZazX%2FqaAKXUKEubR0%2FJoAEBvJLg8Kks3bPIMpFb60IUGPdT0t3u7SSieT01y&X-Amz-Signature=365308b6943c4c01310c9205d9e54ba1b48b210bbfa558745f7f52b9253bd2b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXVTJFB6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDf4m1TPEiEmkuPS1IGCeZH0rwQRhOLPA1lGBr8%2B99HkAIhAN63JMRzXzVqQ8S%2BQqhi%2FpOgfKBklUDkpVREEMII0Ay9Kv8DCEQQABoMNjM3NDIzMTgzODA1IgxuHkIpsk6ek8OWf38q3AN0o8%2FbvDu%2Bziv9V%2BR3aEaSb2d5%2Fwfvr3VCqW7Pm97ceADfzJF08WrAv5dqkeXuC3gEmvBra89MzIHUwd4eH4fzkflCcZNBVCbZ9Wy1H9O5DiCQ85V0kr%2FY2RCVJofbT0Ehe1rnN%2B26lOv0raw%2BNR03XRwOJOrcxb0nYje2vZB%2B%2BmmwAHoBJwnN01nxa6OvZhuWLEHbsv2gZs21ZE2wCkvqJ1QrkjIS290XDsw8XpGrsx3JkhIBTK3bLk84zLVDrohvaZekkTLtS6Od6mnSehjcpV5ge8VmDw%2FTvbVVLBcKnJHzZ1Q61IBm1XJh%2FSkldQqe3ET0jTro7UDwLEBPmP7qofB7%2FYWItwQelLWZGmWvtUCelJxlhnOaW60JHd056xPA7BkDA8IbjF71ZH%2FeQ8cJxL70lWZcNa90eStdcLKKnMQcNBAoOOwiEMlaPlSkufyqkc3TPaLawh09mZRbVmKd15cjN6xXMB%2F9L%2BgEaH9VP7fzRga8bqZ1EmhbYTkOKaYcJca6FraYldePOT%2BTkurYskOL6Gmxst8RXC77epsnpl8CtP8gzNnivR6t23W%2BfGFkF82n%2F7dVaFBZ95jXgmP6g9%2F12WUw2lsE%2FzvHNmUqI8KKaAK44ObEYwiDEDC0i429BjqkAW%2FcLsfPTYZZJdrpouczx%2BiZXBMZgIV2yMk2yp9Ze7yxR3o3tU%2B5KqLSjPuROLJVDn35X%2BilsrDle2Y0jJpWEw97ILgKEsJCTdRU0JBzr7ncusr%2BvB2Zg9zhrGVwzrKKUOzjL2c9FjMlFCelporIPSF2mHSixu1xZazX%2FqaAKXUKEubR0%2FJoAEBvJLg8Kks3bPIMpFb60IUGPdT0t3u7SSieT01y&X-Amz-Signature=d18498bc56b4f4c46e782fe0fdb3f9df845a90512a009058bbf35d6ade9fb5c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
