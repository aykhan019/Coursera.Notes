

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SQPJQVH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIAYVEsCTVmXOjBdjogDKb43%2BEB9COaDZ76v6rAorB6XYAiB0gs89RfjjfWX%2BpTHdC0jEgJU1w66wG3NTcxxS63IQLSr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMzQi3p0rPq8VOGknoKtwDohniNkyTJ5y4UUpqUlILRjzL82p6AA%2BDQ7xfwXuC2TTb9Gwgmowt3quxtZSg9yrmxbShOH5iu3gG5u4hknEjP5KJl3aeKgsRUK8O%2BsE1dsuRlzz3JGW7L4%2BlCxonSzsNA796kyYLKhhrcg8yZe8acAzjWqA7ALegKjg2JgwujfHre%2BUSamcMmD2bq8n%2Bm5vWuttf4%2BF0AbyiPRNN5XHo33V%2BIEZQiAOZ7fzkkA81dClZb8mdjCxdOIpN84ImlxOxYfcn0sqtOXuXmuuAUG3jPJMsIytguHDGSonJY5wrfL3pyO7VFMSv0TuM0b8tRhc9zOvGVBa8ItpTOeNxXjLYUpNZegKxZMl0npnW7lETHWFmF%2FoeVnkwQhJUnYy2%2Fl1UoJDRdV7AlrieNhznvweSYaVJqRYzG5%2FDdpHbi4Xgj750jpS3RuhGwELR4P1VF0kfcGbwrCYMvNFoSsgBGAZHgJujNa9NGbz8n6Y28u3iK7C%2Bl0NfSDOM0LO88fXXi5EnpbJfJKF7HLa2uVyZAXIxy1fU8z%2BCjLWoMvXxlp0ofEPEufqSmicbpu0VSU9BRU8OD13hBWi1EJPtQtAASYQdlge2VOEELJOJscIy5TnWY3EYSs913aPfFzf%2BB6ww2sqHvQY6pgHA7iiWf%2Fvr1wQEkY1XY%2Fn0SalGttvL4UvyfLMSzm7sGqFOfuof3zZlxMjcUrgpG%2Ffl7Hz%2Fhb8GVQh11SmvdM87oARCNEhWbEByUIIA0hF8HEM%2FZ2O%2BgKwaWqqwQF0clFDRGxAu0PwFNwUQEymikIj2KEwpj3VnikQBpq5f1xfgr9pXgNPD0MS2K5sQPsilnKSVAoHMGyteNF5vKlNAW8AIjeRHISe9&X-Amz-Signature=f3812b154d6ff2e0803464e852ef48d47df5bd3a040af1507f4d7b9b436036f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SQPJQVH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIAYVEsCTVmXOjBdjogDKb43%2BEB9COaDZ76v6rAorB6XYAiB0gs89RfjjfWX%2BpTHdC0jEgJU1w66wG3NTcxxS63IQLSr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMzQi3p0rPq8VOGknoKtwDohniNkyTJ5y4UUpqUlILRjzL82p6AA%2BDQ7xfwXuC2TTb9Gwgmowt3quxtZSg9yrmxbShOH5iu3gG5u4hknEjP5KJl3aeKgsRUK8O%2BsE1dsuRlzz3JGW7L4%2BlCxonSzsNA796kyYLKhhrcg8yZe8acAzjWqA7ALegKjg2JgwujfHre%2BUSamcMmD2bq8n%2Bm5vWuttf4%2BF0AbyiPRNN5XHo33V%2BIEZQiAOZ7fzkkA81dClZb8mdjCxdOIpN84ImlxOxYfcn0sqtOXuXmuuAUG3jPJMsIytguHDGSonJY5wrfL3pyO7VFMSv0TuM0b8tRhc9zOvGVBa8ItpTOeNxXjLYUpNZegKxZMl0npnW7lETHWFmF%2FoeVnkwQhJUnYy2%2Fl1UoJDRdV7AlrieNhznvweSYaVJqRYzG5%2FDdpHbi4Xgj750jpS3RuhGwELR4P1VF0kfcGbwrCYMvNFoSsgBGAZHgJujNa9NGbz8n6Y28u3iK7C%2Bl0NfSDOM0LO88fXXi5EnpbJfJKF7HLa2uVyZAXIxy1fU8z%2BCjLWoMvXxlp0ofEPEufqSmicbpu0VSU9BRU8OD13hBWi1EJPtQtAASYQdlge2VOEELJOJscIy5TnWY3EYSs913aPfFzf%2BB6ww2sqHvQY6pgHA7iiWf%2Fvr1wQEkY1XY%2Fn0SalGttvL4UvyfLMSzm7sGqFOfuof3zZlxMjcUrgpG%2Ffl7Hz%2Fhb8GVQh11SmvdM87oARCNEhWbEByUIIA0hF8HEM%2FZ2O%2BgKwaWqqwQF0clFDRGxAu0PwFNwUQEymikIj2KEwpj3VnikQBpq5f1xfgr9pXgNPD0MS2K5sQPsilnKSVAoHMGyteNF5vKlNAW8AIjeRHISe9&X-Amz-Signature=78d08a8271869f3608446ad23fe159967306ca16ccca8ad3dc10ed8c1c94196c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SQPJQVH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIAYVEsCTVmXOjBdjogDKb43%2BEB9COaDZ76v6rAorB6XYAiB0gs89RfjjfWX%2BpTHdC0jEgJU1w66wG3NTcxxS63IQLSr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMzQi3p0rPq8VOGknoKtwDohniNkyTJ5y4UUpqUlILRjzL82p6AA%2BDQ7xfwXuC2TTb9Gwgmowt3quxtZSg9yrmxbShOH5iu3gG5u4hknEjP5KJl3aeKgsRUK8O%2BsE1dsuRlzz3JGW7L4%2BlCxonSzsNA796kyYLKhhrcg8yZe8acAzjWqA7ALegKjg2JgwujfHre%2BUSamcMmD2bq8n%2Bm5vWuttf4%2BF0AbyiPRNN5XHo33V%2BIEZQiAOZ7fzkkA81dClZb8mdjCxdOIpN84ImlxOxYfcn0sqtOXuXmuuAUG3jPJMsIytguHDGSonJY5wrfL3pyO7VFMSv0TuM0b8tRhc9zOvGVBa8ItpTOeNxXjLYUpNZegKxZMl0npnW7lETHWFmF%2FoeVnkwQhJUnYy2%2Fl1UoJDRdV7AlrieNhznvweSYaVJqRYzG5%2FDdpHbi4Xgj750jpS3RuhGwELR4P1VF0kfcGbwrCYMvNFoSsgBGAZHgJujNa9NGbz8n6Y28u3iK7C%2Bl0NfSDOM0LO88fXXi5EnpbJfJKF7HLa2uVyZAXIxy1fU8z%2BCjLWoMvXxlp0ofEPEufqSmicbpu0VSU9BRU8OD13hBWi1EJPtQtAASYQdlge2VOEELJOJscIy5TnWY3EYSs913aPfFzf%2BB6ww2sqHvQY6pgHA7iiWf%2Fvr1wQEkY1XY%2Fn0SalGttvL4UvyfLMSzm7sGqFOfuof3zZlxMjcUrgpG%2Ffl7Hz%2Fhb8GVQh11SmvdM87oARCNEhWbEByUIIA0hF8HEM%2FZ2O%2BgKwaWqqwQF0clFDRGxAu0PwFNwUQEymikIj2KEwpj3VnikQBpq5f1xfgr9pXgNPD0MS2K5sQPsilnKSVAoHMGyteNF5vKlNAW8AIjeRHISe9&X-Amz-Signature=ceda0a6ad13c1c6cb1e3d23fecf97c3d7064e17b74ce42a3da2de15cf04a245e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SQPJQVH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIAYVEsCTVmXOjBdjogDKb43%2BEB9COaDZ76v6rAorB6XYAiB0gs89RfjjfWX%2BpTHdC0jEgJU1w66wG3NTcxxS63IQLSr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMzQi3p0rPq8VOGknoKtwDohniNkyTJ5y4UUpqUlILRjzL82p6AA%2BDQ7xfwXuC2TTb9Gwgmowt3quxtZSg9yrmxbShOH5iu3gG5u4hknEjP5KJl3aeKgsRUK8O%2BsE1dsuRlzz3JGW7L4%2BlCxonSzsNA796kyYLKhhrcg8yZe8acAzjWqA7ALegKjg2JgwujfHre%2BUSamcMmD2bq8n%2Bm5vWuttf4%2BF0AbyiPRNN5XHo33V%2BIEZQiAOZ7fzkkA81dClZb8mdjCxdOIpN84ImlxOxYfcn0sqtOXuXmuuAUG3jPJMsIytguHDGSonJY5wrfL3pyO7VFMSv0TuM0b8tRhc9zOvGVBa8ItpTOeNxXjLYUpNZegKxZMl0npnW7lETHWFmF%2FoeVnkwQhJUnYy2%2Fl1UoJDRdV7AlrieNhznvweSYaVJqRYzG5%2FDdpHbi4Xgj750jpS3RuhGwELR4P1VF0kfcGbwrCYMvNFoSsgBGAZHgJujNa9NGbz8n6Y28u3iK7C%2Bl0NfSDOM0LO88fXXi5EnpbJfJKF7HLa2uVyZAXIxy1fU8z%2BCjLWoMvXxlp0ofEPEufqSmicbpu0VSU9BRU8OD13hBWi1EJPtQtAASYQdlge2VOEELJOJscIy5TnWY3EYSs913aPfFzf%2BB6ww2sqHvQY6pgHA7iiWf%2Fvr1wQEkY1XY%2Fn0SalGttvL4UvyfLMSzm7sGqFOfuof3zZlxMjcUrgpG%2Ffl7Hz%2Fhb8GVQh11SmvdM87oARCNEhWbEByUIIA0hF8HEM%2FZ2O%2BgKwaWqqwQF0clFDRGxAu0PwFNwUQEymikIj2KEwpj3VnikQBpq5f1xfgr9pXgNPD0MS2K5sQPsilnKSVAoHMGyteNF5vKlNAW8AIjeRHISe9&X-Amz-Signature=a6625014fbad69f8a13844e02f0e16a6f01bdbd02cf62400716d1f12998d7711&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SQPJQVH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIAYVEsCTVmXOjBdjogDKb43%2BEB9COaDZ76v6rAorB6XYAiB0gs89RfjjfWX%2BpTHdC0jEgJU1w66wG3NTcxxS63IQLSr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMzQi3p0rPq8VOGknoKtwDohniNkyTJ5y4UUpqUlILRjzL82p6AA%2BDQ7xfwXuC2TTb9Gwgmowt3quxtZSg9yrmxbShOH5iu3gG5u4hknEjP5KJl3aeKgsRUK8O%2BsE1dsuRlzz3JGW7L4%2BlCxonSzsNA796kyYLKhhrcg8yZe8acAzjWqA7ALegKjg2JgwujfHre%2BUSamcMmD2bq8n%2Bm5vWuttf4%2BF0AbyiPRNN5XHo33V%2BIEZQiAOZ7fzkkA81dClZb8mdjCxdOIpN84ImlxOxYfcn0sqtOXuXmuuAUG3jPJMsIytguHDGSonJY5wrfL3pyO7VFMSv0TuM0b8tRhc9zOvGVBa8ItpTOeNxXjLYUpNZegKxZMl0npnW7lETHWFmF%2FoeVnkwQhJUnYy2%2Fl1UoJDRdV7AlrieNhznvweSYaVJqRYzG5%2FDdpHbi4Xgj750jpS3RuhGwELR4P1VF0kfcGbwrCYMvNFoSsgBGAZHgJujNa9NGbz8n6Y28u3iK7C%2Bl0NfSDOM0LO88fXXi5EnpbJfJKF7HLa2uVyZAXIxy1fU8z%2BCjLWoMvXxlp0ofEPEufqSmicbpu0VSU9BRU8OD13hBWi1EJPtQtAASYQdlge2VOEELJOJscIy5TnWY3EYSs913aPfFzf%2BB6ww2sqHvQY6pgHA7iiWf%2Fvr1wQEkY1XY%2Fn0SalGttvL4UvyfLMSzm7sGqFOfuof3zZlxMjcUrgpG%2Ffl7Hz%2Fhb8GVQh11SmvdM87oARCNEhWbEByUIIA0hF8HEM%2FZ2O%2BgKwaWqqwQF0clFDRGxAu0PwFNwUQEymikIj2KEwpj3VnikQBpq5f1xfgr9pXgNPD0MS2K5sQPsilnKSVAoHMGyteNF5vKlNAW8AIjeRHISe9&X-Amz-Signature=c6d836983979ff15088e03cc4312acb092bde431f0f65008d40e2ac966db760a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SQPJQVH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIAYVEsCTVmXOjBdjogDKb43%2BEB9COaDZ76v6rAorB6XYAiB0gs89RfjjfWX%2BpTHdC0jEgJU1w66wG3NTcxxS63IQLSr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMzQi3p0rPq8VOGknoKtwDohniNkyTJ5y4UUpqUlILRjzL82p6AA%2BDQ7xfwXuC2TTb9Gwgmowt3quxtZSg9yrmxbShOH5iu3gG5u4hknEjP5KJl3aeKgsRUK8O%2BsE1dsuRlzz3JGW7L4%2BlCxonSzsNA796kyYLKhhrcg8yZe8acAzjWqA7ALegKjg2JgwujfHre%2BUSamcMmD2bq8n%2Bm5vWuttf4%2BF0AbyiPRNN5XHo33V%2BIEZQiAOZ7fzkkA81dClZb8mdjCxdOIpN84ImlxOxYfcn0sqtOXuXmuuAUG3jPJMsIytguHDGSonJY5wrfL3pyO7VFMSv0TuM0b8tRhc9zOvGVBa8ItpTOeNxXjLYUpNZegKxZMl0npnW7lETHWFmF%2FoeVnkwQhJUnYy2%2Fl1UoJDRdV7AlrieNhznvweSYaVJqRYzG5%2FDdpHbi4Xgj750jpS3RuhGwELR4P1VF0kfcGbwrCYMvNFoSsgBGAZHgJujNa9NGbz8n6Y28u3iK7C%2Bl0NfSDOM0LO88fXXi5EnpbJfJKF7HLa2uVyZAXIxy1fU8z%2BCjLWoMvXxlp0ofEPEufqSmicbpu0VSU9BRU8OD13hBWi1EJPtQtAASYQdlge2VOEELJOJscIy5TnWY3EYSs913aPfFzf%2BB6ww2sqHvQY6pgHA7iiWf%2Fvr1wQEkY1XY%2Fn0SalGttvL4UvyfLMSzm7sGqFOfuof3zZlxMjcUrgpG%2Ffl7Hz%2Fhb8GVQh11SmvdM87oARCNEhWbEByUIIA0hF8HEM%2FZ2O%2BgKwaWqqwQF0clFDRGxAu0PwFNwUQEymikIj2KEwpj3VnikQBpq5f1xfgr9pXgNPD0MS2K5sQPsilnKSVAoHMGyteNF5vKlNAW8AIjeRHISe9&X-Amz-Signature=eb2e3d81fe35da882db8e8dfffcdc005faeff5c187ab1658c30a634fdf139eb5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SQPJQVH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIAYVEsCTVmXOjBdjogDKb43%2BEB9COaDZ76v6rAorB6XYAiB0gs89RfjjfWX%2BpTHdC0jEgJU1w66wG3NTcxxS63IQLSr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMzQi3p0rPq8VOGknoKtwDohniNkyTJ5y4UUpqUlILRjzL82p6AA%2BDQ7xfwXuC2TTb9Gwgmowt3quxtZSg9yrmxbShOH5iu3gG5u4hknEjP5KJl3aeKgsRUK8O%2BsE1dsuRlzz3JGW7L4%2BlCxonSzsNA796kyYLKhhrcg8yZe8acAzjWqA7ALegKjg2JgwujfHre%2BUSamcMmD2bq8n%2Bm5vWuttf4%2BF0AbyiPRNN5XHo33V%2BIEZQiAOZ7fzkkA81dClZb8mdjCxdOIpN84ImlxOxYfcn0sqtOXuXmuuAUG3jPJMsIytguHDGSonJY5wrfL3pyO7VFMSv0TuM0b8tRhc9zOvGVBa8ItpTOeNxXjLYUpNZegKxZMl0npnW7lETHWFmF%2FoeVnkwQhJUnYy2%2Fl1UoJDRdV7AlrieNhznvweSYaVJqRYzG5%2FDdpHbi4Xgj750jpS3RuhGwELR4P1VF0kfcGbwrCYMvNFoSsgBGAZHgJujNa9NGbz8n6Y28u3iK7C%2Bl0NfSDOM0LO88fXXi5EnpbJfJKF7HLa2uVyZAXIxy1fU8z%2BCjLWoMvXxlp0ofEPEufqSmicbpu0VSU9BRU8OD13hBWi1EJPtQtAASYQdlge2VOEELJOJscIy5TnWY3EYSs913aPfFzf%2BB6ww2sqHvQY6pgHA7iiWf%2Fvr1wQEkY1XY%2Fn0SalGttvL4UvyfLMSzm7sGqFOfuof3zZlxMjcUrgpG%2Ffl7Hz%2Fhb8GVQh11SmvdM87oARCNEhWbEByUIIA0hF8HEM%2FZ2O%2BgKwaWqqwQF0clFDRGxAu0PwFNwUQEymikIj2KEwpj3VnikQBpq5f1xfgr9pXgNPD0MS2K5sQPsilnKSVAoHMGyteNF5vKlNAW8AIjeRHISe9&X-Amz-Signature=bef4ceb4bb39b469b702afd2a21cc09c24cbc499f49643da7e6980b2cfeca2c8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SQPJQVH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIAYVEsCTVmXOjBdjogDKb43%2BEB9COaDZ76v6rAorB6XYAiB0gs89RfjjfWX%2BpTHdC0jEgJU1w66wG3NTcxxS63IQLSr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMzQi3p0rPq8VOGknoKtwDohniNkyTJ5y4UUpqUlILRjzL82p6AA%2BDQ7xfwXuC2TTb9Gwgmowt3quxtZSg9yrmxbShOH5iu3gG5u4hknEjP5KJl3aeKgsRUK8O%2BsE1dsuRlzz3JGW7L4%2BlCxonSzsNA796kyYLKhhrcg8yZe8acAzjWqA7ALegKjg2JgwujfHre%2BUSamcMmD2bq8n%2Bm5vWuttf4%2BF0AbyiPRNN5XHo33V%2BIEZQiAOZ7fzkkA81dClZb8mdjCxdOIpN84ImlxOxYfcn0sqtOXuXmuuAUG3jPJMsIytguHDGSonJY5wrfL3pyO7VFMSv0TuM0b8tRhc9zOvGVBa8ItpTOeNxXjLYUpNZegKxZMl0npnW7lETHWFmF%2FoeVnkwQhJUnYy2%2Fl1UoJDRdV7AlrieNhznvweSYaVJqRYzG5%2FDdpHbi4Xgj750jpS3RuhGwELR4P1VF0kfcGbwrCYMvNFoSsgBGAZHgJujNa9NGbz8n6Y28u3iK7C%2Bl0NfSDOM0LO88fXXi5EnpbJfJKF7HLa2uVyZAXIxy1fU8z%2BCjLWoMvXxlp0ofEPEufqSmicbpu0VSU9BRU8OD13hBWi1EJPtQtAASYQdlge2VOEELJOJscIy5TnWY3EYSs913aPfFzf%2BB6ww2sqHvQY6pgHA7iiWf%2Fvr1wQEkY1XY%2Fn0SalGttvL4UvyfLMSzm7sGqFOfuof3zZlxMjcUrgpG%2Ffl7Hz%2Fhb8GVQh11SmvdM87oARCNEhWbEByUIIA0hF8HEM%2FZ2O%2BgKwaWqqwQF0clFDRGxAu0PwFNwUQEymikIj2KEwpj3VnikQBpq5f1xfgr9pXgNPD0MS2K5sQPsilnKSVAoHMGyteNF5vKlNAW8AIjeRHISe9&X-Amz-Signature=2a2046c465e18aab1bd3e79928f628f553cae7e60b9fccb9d014c8e0594a613b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IRKZXA7%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDrEqL5Yc11WcXi0muDpq5i%2F1hETG%2BFkvVwEmQ6fpRGPAIhAOvNnMBLk%2FQWDL%2FRXGa7Pdtgifj9K9THIhVX40SeO2ueKv8DCCsQABoMNjM3NDIzMTgzODA1IgwuE3GrHfbGJ6PbcLMq3AOHjh99K0L9GoiZS9KXRCGCqZNa5MvPlY%2FlYJTAd2fTcOoEi%2Bty%2FV2qoDYRAVlb1%2BqA6iLW%2Fi9aZnDclVjxuf31Vh%2F4dAFSXHZZ2zgaZNzRJf3wy34egBMPLbR41zNywr%2FjWQsf3ZfAaIuUY%2BCOnU9mMaQcphikW5SmOLNRcMr%2FTGLEci9sUaYoeYtgTQpFRIMOKqm%2B9j0BmZkWQr0TAHJKFHRbjkm%2Fd5kTontTZMX%2B3I17NaO7rkHvifhkpjB3WS7pwHJD3t5yJ%2BD5bXnrZeZSox6x6dD1Wjw8FpUgIJVrHItHhxyInyr5Uh79iTGKViVd%2FB8v6VJMeFwxb8yf41OeDH6GM52y4%2BDcZ%2BwMwUkildp7umJop%2B2iiVWpiGc9P%2F%2Bvo8xiVcSRSjrM%2F0zbWp2NshBpwOk51FOB1eDsnLY9U77gr13C87g9BsfNnRfADSWM1YmTVpvwTQ8fwgR9Yosa7gevCHGN1UG1Ero7JdGZNZkxWlA9JsKCeDzogDuDYVQLEWaoyZ9MMPEtU2EZPu3oB61VZ8lnQN%2BxFsTOUy3MuwuSFUxl%2FUGfsFUR8sPOBkaNIJDV78r5nR2OOoBwexdar6vM3ZyBd4kBy4UX9GKLezDrESSsWPNWRuZ%2BTjCRyoe9BjqkAVGWkfnWQeAUGoxdFq26GaMe8bdifI9L6ffAxt2HrPAyKjy6PUDxSa5nCWcGWqRfiV5F3QNXZQ0TXz%2BN6%2Bg3fEBixUQwhSFG%2Fkn2W%2FfXNwDDoZdxJE1QjEEhrTREVPiLND3kXoOMAefISzdi2mhZQeCcKAummwlqEDLcGKzS3wqeVtotWH%2BMWKJU4P6MlxlP8DAYxVM4P5GpEMg3TRgYQY4bwcO2&X-Amz-Signature=fd1b50e2059f2f79344c96e4948bb454b924f85f81d78e09745607e5952f4b79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CPIIZMT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDczqVvFTw0ByDhKa%2BB%2BNwJwMFOaNCJYQ8yVquGRG5MbQIgCUTjqBsooH1MiOylOCo1SGoLDLnC29hF3Ne19QiXZ%2Foq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDLzKoHl%2F%2F%2Fxr8SKhBSrcA8AWvxtP%2BEouLAgwyfW25tzeBDV54fChnEVwTECvdWg769rFt0oj9KFg1QKP7LOZG6fFRLLtxFG0mDmWigPowO5d4NcIJQRlMuDYZpoz1jId0tLTqR1nWbRBzdLaTQCHULyFBia9adl7tRuBU5gWRbnYnlEGyyDUFvAqgvmX7nwEIQMPbI7DZrUtBgSm8kwjs405NknyYvf6BDzbeVU5dSekzIMRfbmW%2FujfYn4OopTenvETJI2E7pnRzpgs1UnqBrTBB%2BKwD0oVcwi5vcfvPOfydLBuFluDR9l81NVQ6M7y1O2ek55yR47kncW456RVdGzEmXGR1w40bN%2FZ6mJ5iqEdfF5wsGtycBim1qv1mnjDFQwrRsZSuqUhG7ae5BKSN12VMOZE3riNLItA4NGwmUtg19id%2FMReEOPm7J2%2FOHJp%2FioIVVZXapHP2ztULTvF5fUorRVzerdEEqycRdugQ0tFF6BtWnBABkwXiHdbPZQQcOmQP2mhrZrfMlARd8jdIUYTAaPvwx4%2B9wleRnL0nIK0%2BFyigID7vdnoiIVqIlSwCZH1qhIaR9YIl8N49n9sXZNHiYlj1aepltsZr4N6aeB3lH5aQ2GWUD5jshlC3JtR6K7Kiui%2Bi4n0UceLMMjLh70GOqUBCVnJvERln160o68%2BjcIzcbiBWI%2FnZNwKqFCJ1D1iO%2FTXvoVc45OSVjvwVUNE0E12swDm3bSf84Dcf95R4FJpe8gQnKMCCjFQs7g0%2FpG8ASPw0LXIpR0wi94I3wqL3pkIBr1u40dpAUDqDUI%2FTUHeTyr5q64GO5AaDFNJk5UNaz0rbB4lDMFGI%2Fam8PkY0vxwuEW2C81XqWAE%2B2HDJ8rYZzVeRdhb&X-Amz-Signature=12d1238ccdd6b9b4d2b7e7936052e5293198dd875a4260f97115f43f2dcdcd7f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RODHWU5S%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIB%2BwpVFDTagdsLbphDM6HFnmhrg0jVdWj%2BcKfA9xNaVWAiBJistKff1xWGk6X3PKD4wmQG77gT44bFfxrQDsQaT%2B8Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMjlFaPQOR1RbzipA2KtwD1e9JWlcIFbumbADdbJ1M2lkld1js%2FxQbR05v5GSXDISwPKnRbnAS%2FF5Tm0nttqll2G895zATMYzLRqpn9iWhXLfhophdawIAFrg6ndO2zY7SAyaNO4vyQfXO1%2FIWm%2FKINzHDHHE%2FaYgQ5ISMfbWSciX01jvL%2BcjGNQ%2BBrYgX2cYP51wBAV%2FltZSMQrZ5LIJKRxUAM5Y%2FIewfeZeruUyERGMDkZ7WuWzwxYVlbnaGdFMeP7CreUUkFdMC%2B1GVHaSsIeYwEZrbdja6EqdE293KXGKQp6uCGnyEnca7grHIukzFRqCUOFJ1%2FCDI1rdSw%2F7kYx5D%2BlFK5SjIISMnqIL4Yas4%2BTJN3FFgRd6LbtJzl2Bbc2ITSQnbQVcBWXiRixBXMy3MGBGNuqAo0WHyD8OjMoqTR%2F%2BLl0ODyHT72uNYIqdqWXkiLukKftU6CPZrY69BiI5ALjU%2BX%2BLp2UGlfNVWlCDgCdWPujEf9AD2G1k0iaOSM4O98mPJT6vEbXv0JYfclsBtWI%2B8tViQ7dqQ1wdLpIANXTESSNOSDyMwMEzjrOd98kKifij1OLEnWpi0C7jOWvLStvO0YUNqR87TuYUMBkrFCmLNyuqsFg0%2BCZR%2Bxt0bxJS9yAgXild78aIw8MqHvQY6pgGQbhRWa54%2F%2BhwnOjTlKW2xRdK3GzfVEzPhtS9raN%2BVFRnXVZp1jLgukP%2Buu1txHPVEUJYR2zdv3eJ4LqdvcwzDh%2B2dnrYLoA8dYij%2BvJNM1Yyo3ewtJuXgFEevJjsynaobVQJqjPnefe%2B1dyVf0xpg67wDJP2b%2B1%2B%2FquFEhyXYFz9ORX5RkeGEb4%2FQsZ90mnTQZ9q4HMV35UHfZ5hzEu%2B6K0JvIFw9&X-Amz-Signature=1cf1b3fc6836023e47246ccbdeabc0216930aad4c15d30eb528440657d98becb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RODHWU5S%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIB%2BwpVFDTagdsLbphDM6HFnmhrg0jVdWj%2BcKfA9xNaVWAiBJistKff1xWGk6X3PKD4wmQG77gT44bFfxrQDsQaT%2B8Cr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMjlFaPQOR1RbzipA2KtwD1e9JWlcIFbumbADdbJ1M2lkld1js%2FxQbR05v5GSXDISwPKnRbnAS%2FF5Tm0nttqll2G895zATMYzLRqpn9iWhXLfhophdawIAFrg6ndO2zY7SAyaNO4vyQfXO1%2FIWm%2FKINzHDHHE%2FaYgQ5ISMfbWSciX01jvL%2BcjGNQ%2BBrYgX2cYP51wBAV%2FltZSMQrZ5LIJKRxUAM5Y%2FIewfeZeruUyERGMDkZ7WuWzwxYVlbnaGdFMeP7CreUUkFdMC%2B1GVHaSsIeYwEZrbdja6EqdE293KXGKQp6uCGnyEnca7grHIukzFRqCUOFJ1%2FCDI1rdSw%2F7kYx5D%2BlFK5SjIISMnqIL4Yas4%2BTJN3FFgRd6LbtJzl2Bbc2ITSQnbQVcBWXiRixBXMy3MGBGNuqAo0WHyD8OjMoqTR%2F%2BLl0ODyHT72uNYIqdqWXkiLukKftU6CPZrY69BiI5ALjU%2BX%2BLp2UGlfNVWlCDgCdWPujEf9AD2G1k0iaOSM4O98mPJT6vEbXv0JYfclsBtWI%2B8tViQ7dqQ1wdLpIANXTESSNOSDyMwMEzjrOd98kKifij1OLEnWpi0C7jOWvLStvO0YUNqR87TuYUMBkrFCmLNyuqsFg0%2BCZR%2Bxt0bxJS9yAgXild78aIw8MqHvQY6pgGQbhRWa54%2F%2BhwnOjTlKW2xRdK3GzfVEzPhtS9raN%2BVFRnXVZp1jLgukP%2Buu1txHPVEUJYR2zdv3eJ4LqdvcwzDh%2B2dnrYLoA8dYij%2BvJNM1Yyo3ewtJuXgFEevJjsynaobVQJqjPnefe%2B1dyVf0xpg67wDJP2b%2B1%2B%2FquFEhyXYFz9ORX5RkeGEb4%2FQsZ90mnTQZ9q4HMV35UHfZ5hzEu%2B6K0JvIFw9&X-Amz-Signature=cc18b2667d800a6d3733b5d0962415cb37dbdc48e3a9e1b70959fb18d37ca8ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
