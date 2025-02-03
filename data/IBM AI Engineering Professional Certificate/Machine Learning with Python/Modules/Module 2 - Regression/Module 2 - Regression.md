

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RA63BZ2Y%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxHfc7QQooF4bNs%2B0IUysX62I4SCXPI%2Fh5sQU8xtvUpQIgVqtgDAEgcIpHj%2Bzh5VLBGfFLvKyrkLzTMTQYU4ZPPjkq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG%2BmfpaUXyOFwVbOlCrcA2rVXD1L0%2FE%2FPY65lZqewX3iyutmsP2BFKLzKXK63n0o7MuHdJy6lMCAc1YZE6TPwT9ajWfLMa5ayhcbqqMtM%2BpUpC4YIydSFYThuipuXbJXAbz1H7zPrmyQtGqTH4IItARvJK4AXDvbV5aTQVV58mM9oj%2Bhn9VADDWwLGJLsy%2Bs%2FS%2F2v0LoC3IgnaIHJDTqg8cDTDPhqAGAvueSv%2Botsjb1f05kHsL3OYwNiLWQc622tpjdoau4kUZ6fMTYqQ60LdClAfU8CVdgpSpqBLnFQJZQG4P9CmLJ3biSxYfECZmaMbD%2F5ZtjO9Q8rmmJRUhKrlZLT0HkwPqM%2Bk4mPZN0DQjsR4sRdQpZiiMpYDSKnV87oBzoy8dt39c4W%2FNEvfI9KSzETxD%2BUhv1TJ%2BAujlGjb0rYVXEa4y59%2BOEuoUQDiusqHM%2BMprfI28qV4ORgtqXxK0ttQLhNoHOQOJtL8ZYK7MXzHmob45qTJuSQGyY4t3Oj3WBuK7KaQ2ZSZzsBqBKG734BzY%2F%2FJKGL4okFIlPyfS7KyOBO2S4dFgu0HQ6s68WpkjmAPqKsJFkhnY7cIZPTD2EcEWzwTi3zrGubh1I7Ngp6OR8lvATK3fgl5j9BJhw3YlB%2BDeXGXOR1jYPMLy0gr0GOqUBiZG8iLtOv0x1AWkaJA%2F8vQLdxt9a1tFLuzJLKj8WKazJmLHRV8rsugtXjEXLFPL8sLS%2FzGapKpYxG7Ro%2B8oem09WnuvQgVf11Hn7lh9784ABwL8tDZoweSb4OxYKObw2rCYpsRNRBrpOx%2B1wvG5%2FbiegesQMfZBSIOzowmXs9XWnCy8ceF%2F5r4CFkITgoox84vMuDJD51ypzf8ESlsOpyHZkbWHv&X-Amz-Signature=39276a735e086b343a5cf1750a9047d6377f3da19411c158a151fa3f48f5d72f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RA63BZ2Y%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxHfc7QQooF4bNs%2B0IUysX62I4SCXPI%2Fh5sQU8xtvUpQIgVqtgDAEgcIpHj%2Bzh5VLBGfFLvKyrkLzTMTQYU4ZPPjkq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG%2BmfpaUXyOFwVbOlCrcA2rVXD1L0%2FE%2FPY65lZqewX3iyutmsP2BFKLzKXK63n0o7MuHdJy6lMCAc1YZE6TPwT9ajWfLMa5ayhcbqqMtM%2BpUpC4YIydSFYThuipuXbJXAbz1H7zPrmyQtGqTH4IItARvJK4AXDvbV5aTQVV58mM9oj%2Bhn9VADDWwLGJLsy%2Bs%2FS%2F2v0LoC3IgnaIHJDTqg8cDTDPhqAGAvueSv%2Botsjb1f05kHsL3OYwNiLWQc622tpjdoau4kUZ6fMTYqQ60LdClAfU8CVdgpSpqBLnFQJZQG4P9CmLJ3biSxYfECZmaMbD%2F5ZtjO9Q8rmmJRUhKrlZLT0HkwPqM%2Bk4mPZN0DQjsR4sRdQpZiiMpYDSKnV87oBzoy8dt39c4W%2FNEvfI9KSzETxD%2BUhv1TJ%2BAujlGjb0rYVXEa4y59%2BOEuoUQDiusqHM%2BMprfI28qV4ORgtqXxK0ttQLhNoHOQOJtL8ZYK7MXzHmob45qTJuSQGyY4t3Oj3WBuK7KaQ2ZSZzsBqBKG734BzY%2F%2FJKGL4okFIlPyfS7KyOBO2S4dFgu0HQ6s68WpkjmAPqKsJFkhnY7cIZPTD2EcEWzwTi3zrGubh1I7Ngp6OR8lvATK3fgl5j9BJhw3YlB%2BDeXGXOR1jYPMLy0gr0GOqUBiZG8iLtOv0x1AWkaJA%2F8vQLdxt9a1tFLuzJLKj8WKazJmLHRV8rsugtXjEXLFPL8sLS%2FzGapKpYxG7Ro%2B8oem09WnuvQgVf11Hn7lh9784ABwL8tDZoweSb4OxYKObw2rCYpsRNRBrpOx%2B1wvG5%2FbiegesQMfZBSIOzowmXs9XWnCy8ceF%2F5r4CFkITgoox84vMuDJD51ypzf8ESlsOpyHZkbWHv&X-Amz-Signature=b85c95351a422bb734dbfc083778e15146177a831f7882a40b3aac0aadc6145e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RA63BZ2Y%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxHfc7QQooF4bNs%2B0IUysX62I4SCXPI%2Fh5sQU8xtvUpQIgVqtgDAEgcIpHj%2Bzh5VLBGfFLvKyrkLzTMTQYU4ZPPjkq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG%2BmfpaUXyOFwVbOlCrcA2rVXD1L0%2FE%2FPY65lZqewX3iyutmsP2BFKLzKXK63n0o7MuHdJy6lMCAc1YZE6TPwT9ajWfLMa5ayhcbqqMtM%2BpUpC4YIydSFYThuipuXbJXAbz1H7zPrmyQtGqTH4IItARvJK4AXDvbV5aTQVV58mM9oj%2Bhn9VADDWwLGJLsy%2Bs%2FS%2F2v0LoC3IgnaIHJDTqg8cDTDPhqAGAvueSv%2Botsjb1f05kHsL3OYwNiLWQc622tpjdoau4kUZ6fMTYqQ60LdClAfU8CVdgpSpqBLnFQJZQG4P9CmLJ3biSxYfECZmaMbD%2F5ZtjO9Q8rmmJRUhKrlZLT0HkwPqM%2Bk4mPZN0DQjsR4sRdQpZiiMpYDSKnV87oBzoy8dt39c4W%2FNEvfI9KSzETxD%2BUhv1TJ%2BAujlGjb0rYVXEa4y59%2BOEuoUQDiusqHM%2BMprfI28qV4ORgtqXxK0ttQLhNoHOQOJtL8ZYK7MXzHmob45qTJuSQGyY4t3Oj3WBuK7KaQ2ZSZzsBqBKG734BzY%2F%2FJKGL4okFIlPyfS7KyOBO2S4dFgu0HQ6s68WpkjmAPqKsJFkhnY7cIZPTD2EcEWzwTi3zrGubh1I7Ngp6OR8lvATK3fgl5j9BJhw3YlB%2BDeXGXOR1jYPMLy0gr0GOqUBiZG8iLtOv0x1AWkaJA%2F8vQLdxt9a1tFLuzJLKj8WKazJmLHRV8rsugtXjEXLFPL8sLS%2FzGapKpYxG7Ro%2B8oem09WnuvQgVf11Hn7lh9784ABwL8tDZoweSb4OxYKObw2rCYpsRNRBrpOx%2B1wvG5%2FbiegesQMfZBSIOzowmXs9XWnCy8ceF%2F5r4CFkITgoox84vMuDJD51ypzf8ESlsOpyHZkbWHv&X-Amz-Signature=7672b44a99bd7014126fb66799417fe97e284cb2fc7705907a11255a64e711e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RA63BZ2Y%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxHfc7QQooF4bNs%2B0IUysX62I4SCXPI%2Fh5sQU8xtvUpQIgVqtgDAEgcIpHj%2Bzh5VLBGfFLvKyrkLzTMTQYU4ZPPjkq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG%2BmfpaUXyOFwVbOlCrcA2rVXD1L0%2FE%2FPY65lZqewX3iyutmsP2BFKLzKXK63n0o7MuHdJy6lMCAc1YZE6TPwT9ajWfLMa5ayhcbqqMtM%2BpUpC4YIydSFYThuipuXbJXAbz1H7zPrmyQtGqTH4IItARvJK4AXDvbV5aTQVV58mM9oj%2Bhn9VADDWwLGJLsy%2Bs%2FS%2F2v0LoC3IgnaIHJDTqg8cDTDPhqAGAvueSv%2Botsjb1f05kHsL3OYwNiLWQc622tpjdoau4kUZ6fMTYqQ60LdClAfU8CVdgpSpqBLnFQJZQG4P9CmLJ3biSxYfECZmaMbD%2F5ZtjO9Q8rmmJRUhKrlZLT0HkwPqM%2Bk4mPZN0DQjsR4sRdQpZiiMpYDSKnV87oBzoy8dt39c4W%2FNEvfI9KSzETxD%2BUhv1TJ%2BAujlGjb0rYVXEa4y59%2BOEuoUQDiusqHM%2BMprfI28qV4ORgtqXxK0ttQLhNoHOQOJtL8ZYK7MXzHmob45qTJuSQGyY4t3Oj3WBuK7KaQ2ZSZzsBqBKG734BzY%2F%2FJKGL4okFIlPyfS7KyOBO2S4dFgu0HQ6s68WpkjmAPqKsJFkhnY7cIZPTD2EcEWzwTi3zrGubh1I7Ngp6OR8lvATK3fgl5j9BJhw3YlB%2BDeXGXOR1jYPMLy0gr0GOqUBiZG8iLtOv0x1AWkaJA%2F8vQLdxt9a1tFLuzJLKj8WKazJmLHRV8rsugtXjEXLFPL8sLS%2FzGapKpYxG7Ro%2B8oem09WnuvQgVf11Hn7lh9784ABwL8tDZoweSb4OxYKObw2rCYpsRNRBrpOx%2B1wvG5%2FbiegesQMfZBSIOzowmXs9XWnCy8ceF%2F5r4CFkITgoox84vMuDJD51ypzf8ESlsOpyHZkbWHv&X-Amz-Signature=738e12ce7e771ab048504d6dec83824d61a9802c9d672475b895e78de9f7b9eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RA63BZ2Y%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxHfc7QQooF4bNs%2B0IUysX62I4SCXPI%2Fh5sQU8xtvUpQIgVqtgDAEgcIpHj%2Bzh5VLBGfFLvKyrkLzTMTQYU4ZPPjkq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG%2BmfpaUXyOFwVbOlCrcA2rVXD1L0%2FE%2FPY65lZqewX3iyutmsP2BFKLzKXK63n0o7MuHdJy6lMCAc1YZE6TPwT9ajWfLMa5ayhcbqqMtM%2BpUpC4YIydSFYThuipuXbJXAbz1H7zPrmyQtGqTH4IItARvJK4AXDvbV5aTQVV58mM9oj%2Bhn9VADDWwLGJLsy%2Bs%2FS%2F2v0LoC3IgnaIHJDTqg8cDTDPhqAGAvueSv%2Botsjb1f05kHsL3OYwNiLWQc622tpjdoau4kUZ6fMTYqQ60LdClAfU8CVdgpSpqBLnFQJZQG4P9CmLJ3biSxYfECZmaMbD%2F5ZtjO9Q8rmmJRUhKrlZLT0HkwPqM%2Bk4mPZN0DQjsR4sRdQpZiiMpYDSKnV87oBzoy8dt39c4W%2FNEvfI9KSzETxD%2BUhv1TJ%2BAujlGjb0rYVXEa4y59%2BOEuoUQDiusqHM%2BMprfI28qV4ORgtqXxK0ttQLhNoHOQOJtL8ZYK7MXzHmob45qTJuSQGyY4t3Oj3WBuK7KaQ2ZSZzsBqBKG734BzY%2F%2FJKGL4okFIlPyfS7KyOBO2S4dFgu0HQ6s68WpkjmAPqKsJFkhnY7cIZPTD2EcEWzwTi3zrGubh1I7Ngp6OR8lvATK3fgl5j9BJhw3YlB%2BDeXGXOR1jYPMLy0gr0GOqUBiZG8iLtOv0x1AWkaJA%2F8vQLdxt9a1tFLuzJLKj8WKazJmLHRV8rsugtXjEXLFPL8sLS%2FzGapKpYxG7Ro%2B8oem09WnuvQgVf11Hn7lh9784ABwL8tDZoweSb4OxYKObw2rCYpsRNRBrpOx%2B1wvG5%2FbiegesQMfZBSIOzowmXs9XWnCy8ceF%2F5r4CFkITgoox84vMuDJD51ypzf8ESlsOpyHZkbWHv&X-Amz-Signature=a93e11dfbdc7dc460223018bbdc4f0ef61f4bffd34f9e83336bc3b499ff72a4d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RA63BZ2Y%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxHfc7QQooF4bNs%2B0IUysX62I4SCXPI%2Fh5sQU8xtvUpQIgVqtgDAEgcIpHj%2Bzh5VLBGfFLvKyrkLzTMTQYU4ZPPjkq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG%2BmfpaUXyOFwVbOlCrcA2rVXD1L0%2FE%2FPY65lZqewX3iyutmsP2BFKLzKXK63n0o7MuHdJy6lMCAc1YZE6TPwT9ajWfLMa5ayhcbqqMtM%2BpUpC4YIydSFYThuipuXbJXAbz1H7zPrmyQtGqTH4IItARvJK4AXDvbV5aTQVV58mM9oj%2Bhn9VADDWwLGJLsy%2Bs%2FS%2F2v0LoC3IgnaIHJDTqg8cDTDPhqAGAvueSv%2Botsjb1f05kHsL3OYwNiLWQc622tpjdoau4kUZ6fMTYqQ60LdClAfU8CVdgpSpqBLnFQJZQG4P9CmLJ3biSxYfECZmaMbD%2F5ZtjO9Q8rmmJRUhKrlZLT0HkwPqM%2Bk4mPZN0DQjsR4sRdQpZiiMpYDSKnV87oBzoy8dt39c4W%2FNEvfI9KSzETxD%2BUhv1TJ%2BAujlGjb0rYVXEa4y59%2BOEuoUQDiusqHM%2BMprfI28qV4ORgtqXxK0ttQLhNoHOQOJtL8ZYK7MXzHmob45qTJuSQGyY4t3Oj3WBuK7KaQ2ZSZzsBqBKG734BzY%2F%2FJKGL4okFIlPyfS7KyOBO2S4dFgu0HQ6s68WpkjmAPqKsJFkhnY7cIZPTD2EcEWzwTi3zrGubh1I7Ngp6OR8lvATK3fgl5j9BJhw3YlB%2BDeXGXOR1jYPMLy0gr0GOqUBiZG8iLtOv0x1AWkaJA%2F8vQLdxt9a1tFLuzJLKj8WKazJmLHRV8rsugtXjEXLFPL8sLS%2FzGapKpYxG7Ro%2B8oem09WnuvQgVf11Hn7lh9784ABwL8tDZoweSb4OxYKObw2rCYpsRNRBrpOx%2B1wvG5%2FbiegesQMfZBSIOzowmXs9XWnCy8ceF%2F5r4CFkITgoox84vMuDJD51ypzf8ESlsOpyHZkbWHv&X-Amz-Signature=c83b7304476e4267a2a5940f7616a59982e20aaac408b159ada956fc1104189a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RA63BZ2Y%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxHfc7QQooF4bNs%2B0IUysX62I4SCXPI%2Fh5sQU8xtvUpQIgVqtgDAEgcIpHj%2Bzh5VLBGfFLvKyrkLzTMTQYU4ZPPjkq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG%2BmfpaUXyOFwVbOlCrcA2rVXD1L0%2FE%2FPY65lZqewX3iyutmsP2BFKLzKXK63n0o7MuHdJy6lMCAc1YZE6TPwT9ajWfLMa5ayhcbqqMtM%2BpUpC4YIydSFYThuipuXbJXAbz1H7zPrmyQtGqTH4IItARvJK4AXDvbV5aTQVV58mM9oj%2Bhn9VADDWwLGJLsy%2Bs%2FS%2F2v0LoC3IgnaIHJDTqg8cDTDPhqAGAvueSv%2Botsjb1f05kHsL3OYwNiLWQc622tpjdoau4kUZ6fMTYqQ60LdClAfU8CVdgpSpqBLnFQJZQG4P9CmLJ3biSxYfECZmaMbD%2F5ZtjO9Q8rmmJRUhKrlZLT0HkwPqM%2Bk4mPZN0DQjsR4sRdQpZiiMpYDSKnV87oBzoy8dt39c4W%2FNEvfI9KSzETxD%2BUhv1TJ%2BAujlGjb0rYVXEa4y59%2BOEuoUQDiusqHM%2BMprfI28qV4ORgtqXxK0ttQLhNoHOQOJtL8ZYK7MXzHmob45qTJuSQGyY4t3Oj3WBuK7KaQ2ZSZzsBqBKG734BzY%2F%2FJKGL4okFIlPyfS7KyOBO2S4dFgu0HQ6s68WpkjmAPqKsJFkhnY7cIZPTD2EcEWzwTi3zrGubh1I7Ngp6OR8lvATK3fgl5j9BJhw3YlB%2BDeXGXOR1jYPMLy0gr0GOqUBiZG8iLtOv0x1AWkaJA%2F8vQLdxt9a1tFLuzJLKj8WKazJmLHRV8rsugtXjEXLFPL8sLS%2FzGapKpYxG7Ro%2B8oem09WnuvQgVf11Hn7lh9784ABwL8tDZoweSb4OxYKObw2rCYpsRNRBrpOx%2B1wvG5%2FbiegesQMfZBSIOzowmXs9XWnCy8ceF%2F5r4CFkITgoox84vMuDJD51ypzf8ESlsOpyHZkbWHv&X-Amz-Signature=aca82a5277619e5976740123a4606d9b748dfc6b822c852f0e5e0b43aa6063d4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RA63BZ2Y%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxHfc7QQooF4bNs%2B0IUysX62I4SCXPI%2Fh5sQU8xtvUpQIgVqtgDAEgcIpHj%2Bzh5VLBGfFLvKyrkLzTMTQYU4ZPPjkq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG%2BmfpaUXyOFwVbOlCrcA2rVXD1L0%2FE%2FPY65lZqewX3iyutmsP2BFKLzKXK63n0o7MuHdJy6lMCAc1YZE6TPwT9ajWfLMa5ayhcbqqMtM%2BpUpC4YIydSFYThuipuXbJXAbz1H7zPrmyQtGqTH4IItARvJK4AXDvbV5aTQVV58mM9oj%2Bhn9VADDWwLGJLsy%2Bs%2FS%2F2v0LoC3IgnaIHJDTqg8cDTDPhqAGAvueSv%2Botsjb1f05kHsL3OYwNiLWQc622tpjdoau4kUZ6fMTYqQ60LdClAfU8CVdgpSpqBLnFQJZQG4P9CmLJ3biSxYfECZmaMbD%2F5ZtjO9Q8rmmJRUhKrlZLT0HkwPqM%2Bk4mPZN0DQjsR4sRdQpZiiMpYDSKnV87oBzoy8dt39c4W%2FNEvfI9KSzETxD%2BUhv1TJ%2BAujlGjb0rYVXEa4y59%2BOEuoUQDiusqHM%2BMprfI28qV4ORgtqXxK0ttQLhNoHOQOJtL8ZYK7MXzHmob45qTJuSQGyY4t3Oj3WBuK7KaQ2ZSZzsBqBKG734BzY%2F%2FJKGL4okFIlPyfS7KyOBO2S4dFgu0HQ6s68WpkjmAPqKsJFkhnY7cIZPTD2EcEWzwTi3zrGubh1I7Ngp6OR8lvATK3fgl5j9BJhw3YlB%2BDeXGXOR1jYPMLy0gr0GOqUBiZG8iLtOv0x1AWkaJA%2F8vQLdxt9a1tFLuzJLKj8WKazJmLHRV8rsugtXjEXLFPL8sLS%2FzGapKpYxG7Ro%2B8oem09WnuvQgVf11Hn7lh9784ABwL8tDZoweSb4OxYKObw2rCYpsRNRBrpOx%2B1wvG5%2FbiegesQMfZBSIOzowmXs9XWnCy8ceF%2F5r4CFkITgoox84vMuDJD51ypzf8ESlsOpyHZkbWHv&X-Amz-Signature=22a6d705cc19215a9d26bd68ebf931673d35ef575bd5b275bbad81d81eaedb0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QH7Y5IFB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDkvejUSI6tSeS3JXpelKp%2FXCvG45RczABKNwXRROOoMAiAr1r73D5SPqK3IB5ZXlsjGT0cTAD6%2FNAId5JDnoBK3Xyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMC9mA9%2FsLT5j05BGNKtwD1wxzecpITlymxSRMt9doIQVwP8xhHlnhK%2Bb%2F2jv6HWMHytQST04Ve%2FYkEtl3BHX01UKlAj9hOCkW7dnG2MQPYdc3Y9L%2Bn3OX3Ft27pFo6zfyql0GFk8XQLqI8eEXJWDVWLlB8isrJMLfKfNX4%2BDkOo2FEq58uc6sMDS7CODlGyVXNybd66b0y2hgdzEpijXCfCttPVFkOdLkLtUhzzmPNnrnfeeFEi3DzDbtzGBpoE7NgyAq%2FGvrhY8R6LqqdPyeTORJqKgVgcOaeYNQYSOfHAFy6I59uX7XFGOdx1%2FPKs0ZuTjiJd181EBPYBi9hnbyiEYh6tKY9ptQI3chN8zigwq89JCcC9N9jkoMul46kXm6oyNBeUNYatQActTMzbDaXXyN2iL0z5suBFoE4pp3%2FGwEgUvYmZtxv7QuePgPbtPAUvs0UUyAyb0YA92qPWCFiD5VrbPjyX8djYXiDTeTEfQ3v0JOCm2qyou5%2B90JDx0VAa%2FslPSBImQPw82La2LZcvZrO%2BvOZOd68wZniBn7m6mZa7ama%2BbH%2B14RbOL9oJU4omA4dUfLkyNjJmvVhf45%2FYOFwyniidcjYrCGB9yDs1l6qVLOGlKHOj%2Bi3sCQUxwdITtAZWWnVHv5%2FsEwz7WCvQY6pgFbim%2BVyjbVQEyaC9XTt04x83aWMirTY0oCT5j6y5J56Ok6eC0yind6X3Mgrv0KIQ0LBLkuL5fxCezMcsbEtxRKMMHopgez3Yz4yEoLJjOEU4XhlWGDMQJS8zrvuKHVWUwMGZX2G6uL7DO6pmisz8gk58N8WPHUbMkveTXw%2F2a1gjPjRQcV7CCrC6LkO2YFCsg86XMtxDD7g6oH%2B6c475Z3V3DglmgZ&X-Amz-Signature=75290ddee75c0ef6112d66093bc40009fb172ece85a0f06f17ac7d59be38e577&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCLO6N6E%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGa5Y%2Bi5bu7%2BfOum7LK7X9pFDCBlsw6lgMD%2B%2BZJjRthLAiAH%2BYlayctyBH7aTSHEfppocnBK0Mxry22oSc7eM7SoQir%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIM6SeM%2B5klxZdOStKmKtwDE3WeJNvofzSFuV1va62hLhAygFzJTANb%2ByXsss5hkclRWHQ4kVsfGSvzxmJPb7PlP7Nu%2FpVHPH5X8lSjnMtXeURYguTTvrzovGuEIftjmFTKSdvK5BWl0yCZN7bQWMOioHn%2FTCMPDO0%2FQPqNMJnFv7AU0AmOIQOZh3AFKJmCeWHrVIE6G2Aw2Kw1njeSCGaWE5v3ufFH39DybBISMqvZFAwhxj3iqKWqNHsax%2BiNoOkYCdM5TX9u7q38cQQjEJSxvZHYn2%2Bzk%2FLUVpERwVyO1CsGLUD67dM1u3ioDAM%2Fi3I2G9RdOvZUx0rLdRbx0I5064t2CWarl63NhRBbeduv%2BQm8tRcR%2BDsvMYUeEFF8HnBiu4AxKuubMdBUb6YkNFUYM2XeWYSL2BzZEvELl9suKv6RnuVJ3Q7MTkDVTwFWx1UQevHxTUaOPY1UwcRPgn5mCmDFCHCVwCSeoWgWQzdxsn%2FXaXuFE3Sil8j0aWvLj3OJ4r4mVovQ6gw972OM7EIw3rOr3jU%2Fpc0YFVc00ZyGfTM3fB3zUFqzNCaAnS5jZ5ciIOcFcD3QWjLooC%2Bsh8ggMVveEAbXROieDw1S2RG%2Fv%2BScoAIDLs%2F1CqgCdTKii5fM7fdAeDzYatX4O5AwvrSCvQY6pgEy1n%2BnuTDl9jpUYjsgrcmfz3fzskdMOeJjIf4oLm0cO7b1e9b4YKZjaxSuzOCSOSwEv0QMecDEdZdDvJsdR0VfoCmjm0RTFtnnKBOKyl0cSKqqb9Lyu7ReEwAHpSHCMV5L3i16h2U2T6LuhQ1W52SwlrA5VNJAVGAX7Mq4DicFBduQJlFGIvaQWXv%2FyObVA8bKo6jtjKrasex%2BBEuyqMMLUPqvkrrr&X-Amz-Signature=aca9eb7a473f7cc24af866bd4f2bc4981a59bff37baf64939873fff4bd526901&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EHFTF44%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn3KCav9cpMXsudZl70sstTV6yiQTIkWDYdeLAWV8NDQIgfTiWUkz7J4D12tWWaHUxsQup4TpmxQB%2FzxIsJx0b1Tgq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDDIbDL1qXXC1RcPCoyrcA177u4kGmQGH3jsPLhULmIJTqdbrWcfocBqcrgwdoXP6RIlqzzzYvNrsFx8EQSuBYvVkqDRu0fTcFqbK7FZ8S9RA9mdvWlpFKvBIu0A87ieqDGt48JegyGfWmyWKbF8lFLNB2Y7KawQ2s4yDHBO5xV5KePDhsh8y%2BW%2Bty5V%2Bozhgy6VLB1Bkgu3NWGl1PsU82sO2re5JgaMHJswVvow%2B%2Fmc25WwtZ32T9m6TmjUopBQSCohDgUwBP1L1WAFJrmP0YIITFXw7ZAFLWLY%2FHWUb9vQy2KbrmgGHfG4JjFrhKTuDZ76tR%2FpGoJwZnJDLz%2Biq3d5UWyC7PoUKrRmPZCtC75BgmLHDQ9N3zfRF0svLmifqnOTJivynmrwjgGF%2B0QQ5lxh8hWDTZMZT38swDT7FU2GYEEoruHnAoG3ZsMFgbXh8FSxSfOMjQFlhJ83BHOiX9%2Fy3G5FCAlRszgYIMvr7OgGlbsQ5e92XDXZcofxMBeF%2F2VHUPZc64yk3kthlodwsaf6KXqO5uP1oC3rpkKO%2FUgqZ6Jrxy7CI3Rol4ttsE7IEhO4hYijx%2B4M34LqdQHefNozyfKxzyRZe3ymorKsLWQmizhURQoS4kQJlitUfY7Es3QhVZFZT8JbZSEjzMNm0gr0GOqUB9WxG0JrE7Mc0eErDpl875dqk2FnY3dXehsf85NmLyT3dOGAKd5WMkuUelQj2BS3N8mLEg8LPJYYrlFOLq8LzGOSsAHWi0wMnnuh%2FcsMETD5ZhXLKx9rFRXhJ6WRNGpiENXfiKB4%2FojGTWvAyqX4z5KlW5M6N7sn6Lnh%2Fl2DoR%2F4n%2BSkhX3vRGc%2FLPB2cRm8SoZgD%2BUcVu33tVvPx7S%2BuNTFYDLnz&X-Amz-Signature=4a02346681f03f1f8268de9d628f1d8c21e7d44490ed19aa99e3064d0270c394&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EHFTF44%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn3KCav9cpMXsudZl70sstTV6yiQTIkWDYdeLAWV8NDQIgfTiWUkz7J4D12tWWaHUxsQup4TpmxQB%2FzxIsJx0b1Tgq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDDIbDL1qXXC1RcPCoyrcA177u4kGmQGH3jsPLhULmIJTqdbrWcfocBqcrgwdoXP6RIlqzzzYvNrsFx8EQSuBYvVkqDRu0fTcFqbK7FZ8S9RA9mdvWlpFKvBIu0A87ieqDGt48JegyGfWmyWKbF8lFLNB2Y7KawQ2s4yDHBO5xV5KePDhsh8y%2BW%2Bty5V%2Bozhgy6VLB1Bkgu3NWGl1PsU82sO2re5JgaMHJswVvow%2B%2Fmc25WwtZ32T9m6TmjUopBQSCohDgUwBP1L1WAFJrmP0YIITFXw7ZAFLWLY%2FHWUb9vQy2KbrmgGHfG4JjFrhKTuDZ76tR%2FpGoJwZnJDLz%2Biq3d5UWyC7PoUKrRmPZCtC75BgmLHDQ9N3zfRF0svLmifqnOTJivynmrwjgGF%2B0QQ5lxh8hWDTZMZT38swDT7FU2GYEEoruHnAoG3ZsMFgbXh8FSxSfOMjQFlhJ83BHOiX9%2Fy3G5FCAlRszgYIMvr7OgGlbsQ5e92XDXZcofxMBeF%2F2VHUPZc64yk3kthlodwsaf6KXqO5uP1oC3rpkKO%2FUgqZ6Jrxy7CI3Rol4ttsE7IEhO4hYijx%2B4M34LqdQHefNozyfKxzyRZe3ymorKsLWQmizhURQoS4kQJlitUfY7Es3QhVZFZT8JbZSEjzMNm0gr0GOqUB9WxG0JrE7Mc0eErDpl875dqk2FnY3dXehsf85NmLyT3dOGAKd5WMkuUelQj2BS3N8mLEg8LPJYYrlFOLq8LzGOSsAHWi0wMnnuh%2FcsMETD5ZhXLKx9rFRXhJ6WRNGpiENXfiKB4%2FojGTWvAyqX4z5KlW5M6N7sn6Lnh%2Fl2DoR%2F4n%2BSkhX3vRGc%2FLPB2cRm8SoZgD%2BUcVu33tVvPx7S%2BuNTFYDLnz&X-Amz-Signature=7e5d27e31bd3b72eada95ecfb5afc3fd746b8637853f28bd05c15deefd07b04b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
