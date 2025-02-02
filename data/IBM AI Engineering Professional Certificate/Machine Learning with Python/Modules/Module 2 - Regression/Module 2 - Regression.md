

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUR76Y7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS1DEOxgwnueQqKNmNzhYN%2FzZOCETmlCsRoycAQ8%2FoFgIhAJkvVNaem6RrGMs4A8IrJeJEiQjQNejtt1Zbr5HjU0IkKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzseG0HZilbKN%2BbmYwq3AMh7EOt5wW%2BsQCKtk8o1dbH9l5ZZvkrhXZV%2FedWDs%2Bv5NdhuWLioPDQrDdFs9F0Shen%2B6RpjLkuUrdbiBUXnDmVeY5pM3bY%2FWzFNDVOTQUOqlX5v1LBP3Tq0KwgF5YU5yV%2Bre3vHU%2FATXB%2FTT%2FrW0VphXRbjoVmYTQAplebhXqLweFgrIGRnghtAsBa8PfMevMUUTcQm2ae1aGoRejid%2BJ%2BTbFLBx1BNuUpeCePnzdo6bnBhRFDlXZJr9Dtcq0v4majpT17%2Br7ABzbH0NunN%2Fnb1jz39Lc6IRIzelnFde3vhGE9wAzmIKFFePSz%2Bf6FpgrbfLgVBk8lsyN36qOw1EcMmGKoSgc1wTrCDSbTDt1oB66e%2BBVCiEeWMKi4BunQu3zX%2Fo5c4yvb2k%2FKjxftWpTGWtFQx%2BNjwO8Ni0yPATLg0JG%2Fvo69KOoc3mmGcB5PvxhWY7lWW6QqVnj8ycWWJh%2F7APsfc6iuDnQyQ%2B4SrwW%2BdlS4sMFrPHDajasG6nfjEvDzbfJuS5d53BOI%2Bb8T56gfy4Wsms9HumTUEgPPz7YLk1fbUegkzN5WDy2VGNz02GvL%2FEa2JY2RO6GxG9ZTWbJFThge1Nfd5brku4WconOP0uKxFbfPH69%2Fz%2FwVSjC4t%2F28BjqkAeFhCTg5KgtX7bQVFlbs6FmAb3Nr%2BQrD9aV0%2FbbSDY%2BA3x%2F6PVsqoZqBb60%2FbsWxUISa59KVBoEle7H8LMFsK9jncKq1TN%2BnaBMQojsaoCCombJwjsbAjf0EqMZEU4Ke%2BNp8kMMEmi3IqS35ShSLPkJ%2FHtONoP50zS7ZzaEh1K6EAvz5shUg9eEs1WZOdMeis7bW1iY7crAl3Ej31OqjdvUYPXcN&X-Amz-Signature=021bb0ab2ac17419a1a63350014353035902f85fb028ee5cb2a1500494364b68&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUR76Y7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS1DEOxgwnueQqKNmNzhYN%2FzZOCETmlCsRoycAQ8%2FoFgIhAJkvVNaem6RrGMs4A8IrJeJEiQjQNejtt1Zbr5HjU0IkKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzseG0HZilbKN%2BbmYwq3AMh7EOt5wW%2BsQCKtk8o1dbH9l5ZZvkrhXZV%2FedWDs%2Bv5NdhuWLioPDQrDdFs9F0Shen%2B6RpjLkuUrdbiBUXnDmVeY5pM3bY%2FWzFNDVOTQUOqlX5v1LBP3Tq0KwgF5YU5yV%2Bre3vHU%2FATXB%2FTT%2FrW0VphXRbjoVmYTQAplebhXqLweFgrIGRnghtAsBa8PfMevMUUTcQm2ae1aGoRejid%2BJ%2BTbFLBx1BNuUpeCePnzdo6bnBhRFDlXZJr9Dtcq0v4majpT17%2Br7ABzbH0NunN%2Fnb1jz39Lc6IRIzelnFde3vhGE9wAzmIKFFePSz%2Bf6FpgrbfLgVBk8lsyN36qOw1EcMmGKoSgc1wTrCDSbTDt1oB66e%2BBVCiEeWMKi4BunQu3zX%2Fo5c4yvb2k%2FKjxftWpTGWtFQx%2BNjwO8Ni0yPATLg0JG%2Fvo69KOoc3mmGcB5PvxhWY7lWW6QqVnj8ycWWJh%2F7APsfc6iuDnQyQ%2B4SrwW%2BdlS4sMFrPHDajasG6nfjEvDzbfJuS5d53BOI%2Bb8T56gfy4Wsms9HumTUEgPPz7YLk1fbUegkzN5WDy2VGNz02GvL%2FEa2JY2RO6GxG9ZTWbJFThge1Nfd5brku4WconOP0uKxFbfPH69%2Fz%2FwVSjC4t%2F28BjqkAeFhCTg5KgtX7bQVFlbs6FmAb3Nr%2BQrD9aV0%2FbbSDY%2BA3x%2F6PVsqoZqBb60%2FbsWxUISa59KVBoEle7H8LMFsK9jncKq1TN%2BnaBMQojsaoCCombJwjsbAjf0EqMZEU4Ke%2BNp8kMMEmi3IqS35ShSLPkJ%2FHtONoP50zS7ZzaEh1K6EAvz5shUg9eEs1WZOdMeis7bW1iY7crAl3Ej31OqjdvUYPXcN&X-Amz-Signature=d1bc3dbcb54683027585f38ea8e9e2f926502af006fc0cc62b78df53c7227a1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUR76Y7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS1DEOxgwnueQqKNmNzhYN%2FzZOCETmlCsRoycAQ8%2FoFgIhAJkvVNaem6RrGMs4A8IrJeJEiQjQNejtt1Zbr5HjU0IkKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzseG0HZilbKN%2BbmYwq3AMh7EOt5wW%2BsQCKtk8o1dbH9l5ZZvkrhXZV%2FedWDs%2Bv5NdhuWLioPDQrDdFs9F0Shen%2B6RpjLkuUrdbiBUXnDmVeY5pM3bY%2FWzFNDVOTQUOqlX5v1LBP3Tq0KwgF5YU5yV%2Bre3vHU%2FATXB%2FTT%2FrW0VphXRbjoVmYTQAplebhXqLweFgrIGRnghtAsBa8PfMevMUUTcQm2ae1aGoRejid%2BJ%2BTbFLBx1BNuUpeCePnzdo6bnBhRFDlXZJr9Dtcq0v4majpT17%2Br7ABzbH0NunN%2Fnb1jz39Lc6IRIzelnFde3vhGE9wAzmIKFFePSz%2Bf6FpgrbfLgVBk8lsyN36qOw1EcMmGKoSgc1wTrCDSbTDt1oB66e%2BBVCiEeWMKi4BunQu3zX%2Fo5c4yvb2k%2FKjxftWpTGWtFQx%2BNjwO8Ni0yPATLg0JG%2Fvo69KOoc3mmGcB5PvxhWY7lWW6QqVnj8ycWWJh%2F7APsfc6iuDnQyQ%2B4SrwW%2BdlS4sMFrPHDajasG6nfjEvDzbfJuS5d53BOI%2Bb8T56gfy4Wsms9HumTUEgPPz7YLk1fbUegkzN5WDy2VGNz02GvL%2FEa2JY2RO6GxG9ZTWbJFThge1Nfd5brku4WconOP0uKxFbfPH69%2Fz%2FwVSjC4t%2F28BjqkAeFhCTg5KgtX7bQVFlbs6FmAb3Nr%2BQrD9aV0%2FbbSDY%2BA3x%2F6PVsqoZqBb60%2FbsWxUISa59KVBoEle7H8LMFsK9jncKq1TN%2BnaBMQojsaoCCombJwjsbAjf0EqMZEU4Ke%2BNp8kMMEmi3IqS35ShSLPkJ%2FHtONoP50zS7ZzaEh1K6EAvz5shUg9eEs1WZOdMeis7bW1iY7crAl3Ej31OqjdvUYPXcN&X-Amz-Signature=db9e218853b8b4860ec188b603114805109d0f66f6956d022ba06c55996a200b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUR76Y7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS1DEOxgwnueQqKNmNzhYN%2FzZOCETmlCsRoycAQ8%2FoFgIhAJkvVNaem6RrGMs4A8IrJeJEiQjQNejtt1Zbr5HjU0IkKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzseG0HZilbKN%2BbmYwq3AMh7EOt5wW%2BsQCKtk8o1dbH9l5ZZvkrhXZV%2FedWDs%2Bv5NdhuWLioPDQrDdFs9F0Shen%2B6RpjLkuUrdbiBUXnDmVeY5pM3bY%2FWzFNDVOTQUOqlX5v1LBP3Tq0KwgF5YU5yV%2Bre3vHU%2FATXB%2FTT%2FrW0VphXRbjoVmYTQAplebhXqLweFgrIGRnghtAsBa8PfMevMUUTcQm2ae1aGoRejid%2BJ%2BTbFLBx1BNuUpeCePnzdo6bnBhRFDlXZJr9Dtcq0v4majpT17%2Br7ABzbH0NunN%2Fnb1jz39Lc6IRIzelnFde3vhGE9wAzmIKFFePSz%2Bf6FpgrbfLgVBk8lsyN36qOw1EcMmGKoSgc1wTrCDSbTDt1oB66e%2BBVCiEeWMKi4BunQu3zX%2Fo5c4yvb2k%2FKjxftWpTGWtFQx%2BNjwO8Ni0yPATLg0JG%2Fvo69KOoc3mmGcB5PvxhWY7lWW6QqVnj8ycWWJh%2F7APsfc6iuDnQyQ%2B4SrwW%2BdlS4sMFrPHDajasG6nfjEvDzbfJuS5d53BOI%2Bb8T56gfy4Wsms9HumTUEgPPz7YLk1fbUegkzN5WDy2VGNz02GvL%2FEa2JY2RO6GxG9ZTWbJFThge1Nfd5brku4WconOP0uKxFbfPH69%2Fz%2FwVSjC4t%2F28BjqkAeFhCTg5KgtX7bQVFlbs6FmAb3Nr%2BQrD9aV0%2FbbSDY%2BA3x%2F6PVsqoZqBb60%2FbsWxUISa59KVBoEle7H8LMFsK9jncKq1TN%2BnaBMQojsaoCCombJwjsbAjf0EqMZEU4Ke%2BNp8kMMEmi3IqS35ShSLPkJ%2FHtONoP50zS7ZzaEh1K6EAvz5shUg9eEs1WZOdMeis7bW1iY7crAl3Ej31OqjdvUYPXcN&X-Amz-Signature=6886ebb90c85100e34b4f1659c181e760cbdca042231b92018cd6d2f8631f019&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUR76Y7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS1DEOxgwnueQqKNmNzhYN%2FzZOCETmlCsRoycAQ8%2FoFgIhAJkvVNaem6RrGMs4A8IrJeJEiQjQNejtt1Zbr5HjU0IkKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzseG0HZilbKN%2BbmYwq3AMh7EOt5wW%2BsQCKtk8o1dbH9l5ZZvkrhXZV%2FedWDs%2Bv5NdhuWLioPDQrDdFs9F0Shen%2B6RpjLkuUrdbiBUXnDmVeY5pM3bY%2FWzFNDVOTQUOqlX5v1LBP3Tq0KwgF5YU5yV%2Bre3vHU%2FATXB%2FTT%2FrW0VphXRbjoVmYTQAplebhXqLweFgrIGRnghtAsBa8PfMevMUUTcQm2ae1aGoRejid%2BJ%2BTbFLBx1BNuUpeCePnzdo6bnBhRFDlXZJr9Dtcq0v4majpT17%2Br7ABzbH0NunN%2Fnb1jz39Lc6IRIzelnFde3vhGE9wAzmIKFFePSz%2Bf6FpgrbfLgVBk8lsyN36qOw1EcMmGKoSgc1wTrCDSbTDt1oB66e%2BBVCiEeWMKi4BunQu3zX%2Fo5c4yvb2k%2FKjxftWpTGWtFQx%2BNjwO8Ni0yPATLg0JG%2Fvo69KOoc3mmGcB5PvxhWY7lWW6QqVnj8ycWWJh%2F7APsfc6iuDnQyQ%2B4SrwW%2BdlS4sMFrPHDajasG6nfjEvDzbfJuS5d53BOI%2Bb8T56gfy4Wsms9HumTUEgPPz7YLk1fbUegkzN5WDy2VGNz02GvL%2FEa2JY2RO6GxG9ZTWbJFThge1Nfd5brku4WconOP0uKxFbfPH69%2Fz%2FwVSjC4t%2F28BjqkAeFhCTg5KgtX7bQVFlbs6FmAb3Nr%2BQrD9aV0%2FbbSDY%2BA3x%2F6PVsqoZqBb60%2FbsWxUISa59KVBoEle7H8LMFsK9jncKq1TN%2BnaBMQojsaoCCombJwjsbAjf0EqMZEU4Ke%2BNp8kMMEmi3IqS35ShSLPkJ%2FHtONoP50zS7ZzaEh1K6EAvz5shUg9eEs1WZOdMeis7bW1iY7crAl3Ej31OqjdvUYPXcN&X-Amz-Signature=461f18c0c30f46ef0f47ca6c5cf4948a9e56e91a96572c35decd555588aa9f98&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUR76Y7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS1DEOxgwnueQqKNmNzhYN%2FzZOCETmlCsRoycAQ8%2FoFgIhAJkvVNaem6RrGMs4A8IrJeJEiQjQNejtt1Zbr5HjU0IkKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzseG0HZilbKN%2BbmYwq3AMh7EOt5wW%2BsQCKtk8o1dbH9l5ZZvkrhXZV%2FedWDs%2Bv5NdhuWLioPDQrDdFs9F0Shen%2B6RpjLkuUrdbiBUXnDmVeY5pM3bY%2FWzFNDVOTQUOqlX5v1LBP3Tq0KwgF5YU5yV%2Bre3vHU%2FATXB%2FTT%2FrW0VphXRbjoVmYTQAplebhXqLweFgrIGRnghtAsBa8PfMevMUUTcQm2ae1aGoRejid%2BJ%2BTbFLBx1BNuUpeCePnzdo6bnBhRFDlXZJr9Dtcq0v4majpT17%2Br7ABzbH0NunN%2Fnb1jz39Lc6IRIzelnFde3vhGE9wAzmIKFFePSz%2Bf6FpgrbfLgVBk8lsyN36qOw1EcMmGKoSgc1wTrCDSbTDt1oB66e%2BBVCiEeWMKi4BunQu3zX%2Fo5c4yvb2k%2FKjxftWpTGWtFQx%2BNjwO8Ni0yPATLg0JG%2Fvo69KOoc3mmGcB5PvxhWY7lWW6QqVnj8ycWWJh%2F7APsfc6iuDnQyQ%2B4SrwW%2BdlS4sMFrPHDajasG6nfjEvDzbfJuS5d53BOI%2Bb8T56gfy4Wsms9HumTUEgPPz7YLk1fbUegkzN5WDy2VGNz02GvL%2FEa2JY2RO6GxG9ZTWbJFThge1Nfd5brku4WconOP0uKxFbfPH69%2Fz%2FwVSjC4t%2F28BjqkAeFhCTg5KgtX7bQVFlbs6FmAb3Nr%2BQrD9aV0%2FbbSDY%2BA3x%2F6PVsqoZqBb60%2FbsWxUISa59KVBoEle7H8LMFsK9jncKq1TN%2BnaBMQojsaoCCombJwjsbAjf0EqMZEU4Ke%2BNp8kMMEmi3IqS35ShSLPkJ%2FHtONoP50zS7ZzaEh1K6EAvz5shUg9eEs1WZOdMeis7bW1iY7crAl3Ej31OqjdvUYPXcN&X-Amz-Signature=4d0d6f63e7b70c1d356382968a8808d9028db9f51001ac613a0b9f3fefa0fe60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUR76Y7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS1DEOxgwnueQqKNmNzhYN%2FzZOCETmlCsRoycAQ8%2FoFgIhAJkvVNaem6RrGMs4A8IrJeJEiQjQNejtt1Zbr5HjU0IkKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzseG0HZilbKN%2BbmYwq3AMh7EOt5wW%2BsQCKtk8o1dbH9l5ZZvkrhXZV%2FedWDs%2Bv5NdhuWLioPDQrDdFs9F0Shen%2B6RpjLkuUrdbiBUXnDmVeY5pM3bY%2FWzFNDVOTQUOqlX5v1LBP3Tq0KwgF5YU5yV%2Bre3vHU%2FATXB%2FTT%2FrW0VphXRbjoVmYTQAplebhXqLweFgrIGRnghtAsBa8PfMevMUUTcQm2ae1aGoRejid%2BJ%2BTbFLBx1BNuUpeCePnzdo6bnBhRFDlXZJr9Dtcq0v4majpT17%2Br7ABzbH0NunN%2Fnb1jz39Lc6IRIzelnFde3vhGE9wAzmIKFFePSz%2Bf6FpgrbfLgVBk8lsyN36qOw1EcMmGKoSgc1wTrCDSbTDt1oB66e%2BBVCiEeWMKi4BunQu3zX%2Fo5c4yvb2k%2FKjxftWpTGWtFQx%2BNjwO8Ni0yPATLg0JG%2Fvo69KOoc3mmGcB5PvxhWY7lWW6QqVnj8ycWWJh%2F7APsfc6iuDnQyQ%2B4SrwW%2BdlS4sMFrPHDajasG6nfjEvDzbfJuS5d53BOI%2Bb8T56gfy4Wsms9HumTUEgPPz7YLk1fbUegkzN5WDy2VGNz02GvL%2FEa2JY2RO6GxG9ZTWbJFThge1Nfd5brku4WconOP0uKxFbfPH69%2Fz%2FwVSjC4t%2F28BjqkAeFhCTg5KgtX7bQVFlbs6FmAb3Nr%2BQrD9aV0%2FbbSDY%2BA3x%2F6PVsqoZqBb60%2FbsWxUISa59KVBoEle7H8LMFsK9jncKq1TN%2BnaBMQojsaoCCombJwjsbAjf0EqMZEU4Ke%2BNp8kMMEmi3IqS35ShSLPkJ%2FHtONoP50zS7ZzaEh1K6EAvz5shUg9eEs1WZOdMeis7bW1iY7crAl3Ej31OqjdvUYPXcN&X-Amz-Signature=f07529a7b08b927a55b6e0c861ca098d1235ff5700cd76acd81dfeefb988756c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUR76Y7M%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDS1DEOxgwnueQqKNmNzhYN%2FzZOCETmlCsRoycAQ8%2FoFgIhAJkvVNaem6RrGMs4A8IrJeJEiQjQNejtt1Zbr5HjU0IkKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzseG0HZilbKN%2BbmYwq3AMh7EOt5wW%2BsQCKtk8o1dbH9l5ZZvkrhXZV%2FedWDs%2Bv5NdhuWLioPDQrDdFs9F0Shen%2B6RpjLkuUrdbiBUXnDmVeY5pM3bY%2FWzFNDVOTQUOqlX5v1LBP3Tq0KwgF5YU5yV%2Bre3vHU%2FATXB%2FTT%2FrW0VphXRbjoVmYTQAplebhXqLweFgrIGRnghtAsBa8PfMevMUUTcQm2ae1aGoRejid%2BJ%2BTbFLBx1BNuUpeCePnzdo6bnBhRFDlXZJr9Dtcq0v4majpT17%2Br7ABzbH0NunN%2Fnb1jz39Lc6IRIzelnFde3vhGE9wAzmIKFFePSz%2Bf6FpgrbfLgVBk8lsyN36qOw1EcMmGKoSgc1wTrCDSbTDt1oB66e%2BBVCiEeWMKi4BunQu3zX%2Fo5c4yvb2k%2FKjxftWpTGWtFQx%2BNjwO8Ni0yPATLg0JG%2Fvo69KOoc3mmGcB5PvxhWY7lWW6QqVnj8ycWWJh%2F7APsfc6iuDnQyQ%2B4SrwW%2BdlS4sMFrPHDajasG6nfjEvDzbfJuS5d53BOI%2Bb8T56gfy4Wsms9HumTUEgPPz7YLk1fbUegkzN5WDy2VGNz02GvL%2FEa2JY2RO6GxG9ZTWbJFThge1Nfd5brku4WconOP0uKxFbfPH69%2Fz%2FwVSjC4t%2F28BjqkAeFhCTg5KgtX7bQVFlbs6FmAb3Nr%2BQrD9aV0%2FbbSDY%2BA3x%2F6PVsqoZqBb60%2FbsWxUISa59KVBoEle7H8LMFsK9jncKq1TN%2BnaBMQojsaoCCombJwjsbAjf0EqMZEU4Ke%2BNp8kMMEmi3IqS35ShSLPkJ%2FHtONoP50zS7ZzaEh1K6EAvz5shUg9eEs1WZOdMeis7bW1iY7crAl3Ej31OqjdvUYPXcN&X-Amz-Signature=3f118dc2419cd6720949d1685c7d3ef4ae8267cd6dd1afb4470507df69a71750&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWDM2Z6X%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF81RE3q16x9bwfHLCIHs9hqUY%2FVHpFrzL88FM52%2FAsFAiAIgudATtNKxdaoFwKNpGnMhoMusNto43RpqsGStBB7DCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpa81FT1Hx0mQiK9GKtwDpN06%2FAc7732%2B9zw6nwWYp3nVM7u5aZA2rHYUy8MfeTKIlFNv4o0lCuUTUE2MOr%2BOKRaoJRNi7f%2B8yu7Yho4t59imW5BZyEjEFVfXtWrV1kalKHBy%2BzZ%2BR03Py%2F%2BhwNy4zsKIFwh5C3Aw3I1Ed9%2F1xwte5kMFHkjSxlRDx5DwdFQ9byHCsoSSjcM2V0KStZb6mm4C1VckZV0OWdD3wLjk1IfRITWpKhhLMjWU%2Fg2l2egRgpoHT7ACacI5%2BKWIQk48XC2eOv%2FUpEDoB2vQSuqMT7VTK%2F3adoApcLnvqSm41fm%2BXeH277%2Fl22dUJvAydg8IcPJ7wlwS6MbjR5OFnQlbCbAJFGDgsp%2BLD6nn2wILj%2FGvDi7jHEKqYTjx0Xqt3665Yjq%2FuZRyDbjqW1tnmQCfSOyd%2BfDs6N45zPZ%2FHH%2FuJ7dIehRyoDaHRsDF7%2FoB6THBkCMOfkmYstmjYNIX7kNpqD8gKCgf56n9wVkLS8LI8Dj%2FuQYTWg%2BvpGdUDXyAYHRyfTEPPAiOOQhk9RBFRByYv1%2F6ANanZw%2FboDF%2Flf%2Fhb2h7hHeyf7s8mhx24TOWr1Bc9lrvGQehkBzlwW69cACehL%2FhJ1%2BRfj0DigeGBF7y9bgqeOJ0uPrveHI7I%2Fgw4Lv9vAY6pgH765mRRb1PSrVnM5fgswCKDAmTZb3v%2BM3xfbh9gomGQcrprjvCoXmkNcYnxnqMna3URJwkDmsG9CZwNxpalkac%2BNS9Pwqn32V7fLK%2FOT6Zm8%2FbaCUmLZp4whs%2B%2Fwc%2BUxhA56Kts1ka1acdQhcEiT2%2FYtaLSMbsRaiW%2BcQX%2FEmkk8AJByHyxcvxE5Ylr1jOnaSdRV41%2Bsrp02AJ1EN1DinAU2IRC%2FSx&X-Amz-Signature=756fd01e490d49a996e52e556f7fbdbcfc6da2b3e94ef08f780cd0ead91d247f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R2IJJJL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBsOmqKwK8j0m01yP%2FpZi925njI7K5q%2BGXj3GSJg20yuAiEAo0aHUxSsSelWVETM%2FtieSXpYBbn%2FOd6zhY4YGuuywzgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIUDs2EgwECUFDL48SrcA7ArK4i%2F0s%2FeicWfa5%2BU9rh3GWsOLHsFpx8GeD4NnuqWMpaXqwxVSgjYakRwtpuDJTcGAPudBT7sZUuCrHJCkxYhOpQ%2Bnq0DZM3xamNblfRA6bAxin4LqAbEByWmiZlJ3rZgF0VRBgXo8pDvyos2Ny51FXAs%2Bwg1Y4fzF0V2J8WJM3GbUqVq%2F09nGsytqSytlNC9kK2RfuVezCm5nJyjPO32arVe3q29OpDFLS9oylDgOjlQqBAHcVEyX2GW7noEhLevlVFd02tEo25Dkp5%2FyXm3sf64SFx0nUF6w%2Bf1C4M7CrEB4cwzCBomvOr0o2vMvjRS6QjJKjSdak%2FLd7GmbFHx0BQrssWvItIJuW7%2FBudlRpzcd4vglY8unmmCmlHLuQHPCl8fH4t1wM2PWdxqivoI7BOO4JsmRB9Sy8clOVKzKDeqbEThnruI24R7iKx7bvgVpBKMYldxgHx95flo%2BZjQrZMmqxFmuQZgZlQHtpQZgap4SFjn5CQ3Rtv3QydIGQTG0Uf8SKNWthBDsM3iXrBGJKy4T4NdtWB7YskJiulMLWf8wzboRo2AvZJLP5pKUATxVD%2B%2Fk%2BtAFMIa36%2FPy4pmWjmzV71NnWrlc9KgOxANThTBfpDQVxa1SrbcMP6%2F%2FbwGOqUBlAG0K3yIH%2FC0lrBw7ud9Zokg7Bugy6GmI9FvmdBRfndDEAMH%2BSrxs9zVBX2ypA2f9pCs7c3ibQybkfAMY4P1FjCOCNGxtYSJpoErXZwl3097XdFVLK6gyhOPmmMet%2B%2Bw7rgiQUf%2Foj%2BCwy%2FRbybhT17oHRI3vp%2FBkVcQ3Xr3FKpiM1dp6r1Pzf4R59wq4kHpSQ9MCPo4ea3XuN5FzA2HxVF57lSw&X-Amz-Signature=bdb6429dea0ec4e7bd9607f94dc25febadf2d64e78c63e56a9568e64c6158562&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CIG2TAW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnfvwT6WLS%2BkdsR3m2tC3DXXfQ1OE0tJL%2FgO7cljTveAIgTazjpYM4ICOEedj%2BZaBS9lTeeGguZPqUlEEoC%2FX826UqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNEzQL5bZkWA6bZcXyrcA%2BLHUprWO%2BWVJQWk6pXtMxmUjJtbUDPAnU0tOPG4vtGBPBEmgi7%2B%2FNdLi49oDFT7pWVlYdScWS6tSyo213YkC055o%2BbnWuUFVLajA%2B%2B%2B12fO1Adi3jBopvs6FomiDbhVSt9YYX0j5KbCV8pEpbxu171a5Bsazujv7%2BeWH3CrL68txO8QIE0Bgp4ZdjBw5ZDFGTaGWv3SUn9SrikkWsInSBpMvIqmh8BIuOdCccTP%2FXM%2FQvSzccLpv5TdYpypsM3GDVtNb%2BiTs3cEzETmOIqLuyj9t%2BWKvb3SOpKYqpmnbSeo0sZoTfopQLXT0Cp4gkLm8g%2BaCyoev59QvqR25sIn6VaWQc6MAyN7UWjWUIqM9uT6nHTbs0gZg5S2mv8wBrCm0z%2BhgGYEvT%2Fq4RGaqkwoz6nV9CSLT%2FI8btTB53oa12OY%2BYhOubf1VprrfJAtlxYVZwSbVmQYlRJwZTiCR%2BpVwf2%2BWuuapbxCfDjInLfp%2BNltk9kiNblYhWMWZscCfICxjamDwBEFIr87GPKe%2BspEZz2ZZAhaW2kinZuJcUFTp97v7TqedxfO3LQzXqVnBYJRE4Aa3mqKBoYfYRazuTPdD8Ero7rskufctMicQG7m5J5obAY4wYWBDR%2BGh%2BWZMI%2B%2F%2FbwGOqUB%2FFVDm9ZR0Leaat40Fv02yIdv9%2F1F%2FVDbvSJCWCYM2NhojIvxTjDThF%2Fy1oL1S2Qh4sKxyphFDwNsWxlUBczIWYJ%2B6RvgBDy%2BdJJ%2B64l%2BznMV7DdE7%2Bk6ZrLWtA31HWpQB5%2FYTPbr8FFYiqC0VdpGM0uu4A4j3DMaoIZ2ipzgJnHIEbUM8QalqAeXRGpy38KPu9dAozMNhCU6uGOSJT3eEI%2F7pJQf&X-Amz-Signature=ca9a0eb3c55663771961df2b67c836b5b68b8a6a71f10854f6bae76ea9fd5916&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CIG2TAW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnfvwT6WLS%2BkdsR3m2tC3DXXfQ1OE0tJL%2FgO7cljTveAIgTazjpYM4ICOEedj%2BZaBS9lTeeGguZPqUlEEoC%2FX826UqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNEzQL5bZkWA6bZcXyrcA%2BLHUprWO%2BWVJQWk6pXtMxmUjJtbUDPAnU0tOPG4vtGBPBEmgi7%2B%2FNdLi49oDFT7pWVlYdScWS6tSyo213YkC055o%2BbnWuUFVLajA%2B%2B%2B12fO1Adi3jBopvs6FomiDbhVSt9YYX0j5KbCV8pEpbxu171a5Bsazujv7%2BeWH3CrL68txO8QIE0Bgp4ZdjBw5ZDFGTaGWv3SUn9SrikkWsInSBpMvIqmh8BIuOdCccTP%2FXM%2FQvSzccLpv5TdYpypsM3GDVtNb%2BiTs3cEzETmOIqLuyj9t%2BWKvb3SOpKYqpmnbSeo0sZoTfopQLXT0Cp4gkLm8g%2BaCyoev59QvqR25sIn6VaWQc6MAyN7UWjWUIqM9uT6nHTbs0gZg5S2mv8wBrCm0z%2BhgGYEvT%2Fq4RGaqkwoz6nV9CSLT%2FI8btTB53oa12OY%2BYhOubf1VprrfJAtlxYVZwSbVmQYlRJwZTiCR%2BpVwf2%2BWuuapbxCfDjInLfp%2BNltk9kiNblYhWMWZscCfICxjamDwBEFIr87GPKe%2BspEZz2ZZAhaW2kinZuJcUFTp97v7TqedxfO3LQzXqVnBYJRE4Aa3mqKBoYfYRazuTPdD8Ero7rskufctMicQG7m5J5obAY4wYWBDR%2BGh%2BWZMI%2B%2F%2FbwGOqUB%2FFVDm9ZR0Leaat40Fv02yIdv9%2F1F%2FVDbvSJCWCYM2NhojIvxTjDThF%2Fy1oL1S2Qh4sKxyphFDwNsWxlUBczIWYJ%2B6RvgBDy%2BdJJ%2B64l%2BznMV7DdE7%2Bk6ZrLWtA31HWpQB5%2FYTPbr8FFYiqC0VdpGM0uu4A4j3DMaoIZ2ipzgJnHIEbUM8QalqAeXRGpy38KPu9dAozMNhCU6uGOSJT3eEI%2F7pJQf&X-Amz-Signature=1b366780ef07583c4c3e9f93ceb31b624987920f5a8e3cfd50f134abce13c62b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
