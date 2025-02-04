

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBPGRGK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQD0yEn1CnLpCDCOuHPTfMvT3Ac%2FMIytI8IK0eP6rBto%2FwIhAP8VLrM1etHQemV%2Fb9Ry9CKBjxlXAghDd5gZExR3aAawKv8DCDUQABoMNjM3NDIzMTgzODA1IgygDAhOmYpEgdN5QkAq3APZ9Od30wjvlWPk8efRRIEKJ4u07ALZyNvVFPXXISoy6HumwOFyI%2Fw0OfBfnpbyByviC0LgFP%2Fa8vquIc8SIcSyXOvcn3mm7e7ry9b41gtUyB0AC1K8vcdpwj4vOYgp4qod4gar1nlZofMogn9K63Uoj%2BhqiPanMvBNF8H%2BycJnSO5ZtYToQtNhNDs8fBIWGVxTHISFfA%2BP3xTTCf8kbyadZPIhY1wtT6QOwZaIX60tm6DuguvN%2BtD9K%2BLDX3BFQFDEhWAhgSkKEAqvX1E1%2BXMOFCG3TD8oxASz94SO%2B%2FdszUHJXPoUw2M6xxQcKkvJT%2FuyldfRuKyzC37MfRo1zUNcvdRn5IwV4lIMjkhNs8EFhNabazcyGjX8OGbe4UuriLQ8ivxqO2mkTvBashSIEQGzYK4qPWcJ%2B%2BXiuh%2FurvWWLJMGI3DPsoq8v%2BR2II3qE9Pnl8iN82M7Uxfm9CZe86zTjfDY5EBYNZxcO0OpDMyIJ3iQEXfAbCQ16J3wc%2BuCwA7d7JHqB0mjnLq%2BpcS95XIzHP4mkL5pWJjko50a4UU4vlW3qxuXvrjVfoMpw%2F88AlQaUSLB%2FcNqUdGVz5iqzM9VnCgKc1Byh5wfX9EsGk5uMM1Iff7lNwnEvaYw%2FzCO3Ym9BjqkATA%2B%2BSglkRsrfcphKmYm2K7aid%2BMwUnx7bw0f%2BgvjI5l7axzSzJyCrr9XfG6yYBbXJxwpx%2BAeGmN8PT4lAHHMYQHUD%2FcuHx3%2FJPOaqyCm9lqcnOW7OR1bz0UCV%2FiupL2nGUxfnXWI3tmZjyTpIRwPsc7KEdP7ic3djvCOS%2BZlZkzH4NkNiTJcxW3rcl7Ed7YwdD06jZkm%2Feb76G%2BLk%2BZCSxJFmem&X-Amz-Signature=d9ae46a39cada0708870857c2c8ca44fed29fd996318c798a54d0c88b77dfc7b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBPGRGK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQD0yEn1CnLpCDCOuHPTfMvT3Ac%2FMIytI8IK0eP6rBto%2FwIhAP8VLrM1etHQemV%2Fb9Ry9CKBjxlXAghDd5gZExR3aAawKv8DCDUQABoMNjM3NDIzMTgzODA1IgygDAhOmYpEgdN5QkAq3APZ9Od30wjvlWPk8efRRIEKJ4u07ALZyNvVFPXXISoy6HumwOFyI%2Fw0OfBfnpbyByviC0LgFP%2Fa8vquIc8SIcSyXOvcn3mm7e7ry9b41gtUyB0AC1K8vcdpwj4vOYgp4qod4gar1nlZofMogn9K63Uoj%2BhqiPanMvBNF8H%2BycJnSO5ZtYToQtNhNDs8fBIWGVxTHISFfA%2BP3xTTCf8kbyadZPIhY1wtT6QOwZaIX60tm6DuguvN%2BtD9K%2BLDX3BFQFDEhWAhgSkKEAqvX1E1%2BXMOFCG3TD8oxASz94SO%2B%2FdszUHJXPoUw2M6xxQcKkvJT%2FuyldfRuKyzC37MfRo1zUNcvdRn5IwV4lIMjkhNs8EFhNabazcyGjX8OGbe4UuriLQ8ivxqO2mkTvBashSIEQGzYK4qPWcJ%2B%2BXiuh%2FurvWWLJMGI3DPsoq8v%2BR2II3qE9Pnl8iN82M7Uxfm9CZe86zTjfDY5EBYNZxcO0OpDMyIJ3iQEXfAbCQ16J3wc%2BuCwA7d7JHqB0mjnLq%2BpcS95XIzHP4mkL5pWJjko50a4UU4vlW3qxuXvrjVfoMpw%2F88AlQaUSLB%2FcNqUdGVz5iqzM9VnCgKc1Byh5wfX9EsGk5uMM1Iff7lNwnEvaYw%2FzCO3Ym9BjqkATA%2B%2BSglkRsrfcphKmYm2K7aid%2BMwUnx7bw0f%2BgvjI5l7axzSzJyCrr9XfG6yYBbXJxwpx%2BAeGmN8PT4lAHHMYQHUD%2FcuHx3%2FJPOaqyCm9lqcnOW7OR1bz0UCV%2FiupL2nGUxfnXWI3tmZjyTpIRwPsc7KEdP7ic3djvCOS%2BZlZkzH4NkNiTJcxW3rcl7Ed7YwdD06jZkm%2Feb76G%2BLk%2BZCSxJFmem&X-Amz-Signature=c7719c4de8b583e1b0e5bcf866fdba16897f29ce018629591455e7edf7a36501&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBPGRGK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQD0yEn1CnLpCDCOuHPTfMvT3Ac%2FMIytI8IK0eP6rBto%2FwIhAP8VLrM1etHQemV%2Fb9Ry9CKBjxlXAghDd5gZExR3aAawKv8DCDUQABoMNjM3NDIzMTgzODA1IgygDAhOmYpEgdN5QkAq3APZ9Od30wjvlWPk8efRRIEKJ4u07ALZyNvVFPXXISoy6HumwOFyI%2Fw0OfBfnpbyByviC0LgFP%2Fa8vquIc8SIcSyXOvcn3mm7e7ry9b41gtUyB0AC1K8vcdpwj4vOYgp4qod4gar1nlZofMogn9K63Uoj%2BhqiPanMvBNF8H%2BycJnSO5ZtYToQtNhNDs8fBIWGVxTHISFfA%2BP3xTTCf8kbyadZPIhY1wtT6QOwZaIX60tm6DuguvN%2BtD9K%2BLDX3BFQFDEhWAhgSkKEAqvX1E1%2BXMOFCG3TD8oxASz94SO%2B%2FdszUHJXPoUw2M6xxQcKkvJT%2FuyldfRuKyzC37MfRo1zUNcvdRn5IwV4lIMjkhNs8EFhNabazcyGjX8OGbe4UuriLQ8ivxqO2mkTvBashSIEQGzYK4qPWcJ%2B%2BXiuh%2FurvWWLJMGI3DPsoq8v%2BR2II3qE9Pnl8iN82M7Uxfm9CZe86zTjfDY5EBYNZxcO0OpDMyIJ3iQEXfAbCQ16J3wc%2BuCwA7d7JHqB0mjnLq%2BpcS95XIzHP4mkL5pWJjko50a4UU4vlW3qxuXvrjVfoMpw%2F88AlQaUSLB%2FcNqUdGVz5iqzM9VnCgKc1Byh5wfX9EsGk5uMM1Iff7lNwnEvaYw%2FzCO3Ym9BjqkATA%2B%2BSglkRsrfcphKmYm2K7aid%2BMwUnx7bw0f%2BgvjI5l7axzSzJyCrr9XfG6yYBbXJxwpx%2BAeGmN8PT4lAHHMYQHUD%2FcuHx3%2FJPOaqyCm9lqcnOW7OR1bz0UCV%2FiupL2nGUxfnXWI3tmZjyTpIRwPsc7KEdP7ic3djvCOS%2BZlZkzH4NkNiTJcxW3rcl7Ed7YwdD06jZkm%2Feb76G%2BLk%2BZCSxJFmem&X-Amz-Signature=7990dbdb174c729367fb627af11e26c6b30fd61e9af9ae0dd4c0944fbb95ae97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBPGRGK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQD0yEn1CnLpCDCOuHPTfMvT3Ac%2FMIytI8IK0eP6rBto%2FwIhAP8VLrM1etHQemV%2Fb9Ry9CKBjxlXAghDd5gZExR3aAawKv8DCDUQABoMNjM3NDIzMTgzODA1IgygDAhOmYpEgdN5QkAq3APZ9Od30wjvlWPk8efRRIEKJ4u07ALZyNvVFPXXISoy6HumwOFyI%2Fw0OfBfnpbyByviC0LgFP%2Fa8vquIc8SIcSyXOvcn3mm7e7ry9b41gtUyB0AC1K8vcdpwj4vOYgp4qod4gar1nlZofMogn9K63Uoj%2BhqiPanMvBNF8H%2BycJnSO5ZtYToQtNhNDs8fBIWGVxTHISFfA%2BP3xTTCf8kbyadZPIhY1wtT6QOwZaIX60tm6DuguvN%2BtD9K%2BLDX3BFQFDEhWAhgSkKEAqvX1E1%2BXMOFCG3TD8oxASz94SO%2B%2FdszUHJXPoUw2M6xxQcKkvJT%2FuyldfRuKyzC37MfRo1zUNcvdRn5IwV4lIMjkhNs8EFhNabazcyGjX8OGbe4UuriLQ8ivxqO2mkTvBashSIEQGzYK4qPWcJ%2B%2BXiuh%2FurvWWLJMGI3DPsoq8v%2BR2II3qE9Pnl8iN82M7Uxfm9CZe86zTjfDY5EBYNZxcO0OpDMyIJ3iQEXfAbCQ16J3wc%2BuCwA7d7JHqB0mjnLq%2BpcS95XIzHP4mkL5pWJjko50a4UU4vlW3qxuXvrjVfoMpw%2F88AlQaUSLB%2FcNqUdGVz5iqzM9VnCgKc1Byh5wfX9EsGk5uMM1Iff7lNwnEvaYw%2FzCO3Ym9BjqkATA%2B%2BSglkRsrfcphKmYm2K7aid%2BMwUnx7bw0f%2BgvjI5l7axzSzJyCrr9XfG6yYBbXJxwpx%2BAeGmN8PT4lAHHMYQHUD%2FcuHx3%2FJPOaqyCm9lqcnOW7OR1bz0UCV%2FiupL2nGUxfnXWI3tmZjyTpIRwPsc7KEdP7ic3djvCOS%2BZlZkzH4NkNiTJcxW3rcl7Ed7YwdD06jZkm%2Feb76G%2BLk%2BZCSxJFmem&X-Amz-Signature=fd955e081364fdb2e75cd137c749dd1fcba98cc8b641e453092dc93da85fba4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBPGRGK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQD0yEn1CnLpCDCOuHPTfMvT3Ac%2FMIytI8IK0eP6rBto%2FwIhAP8VLrM1etHQemV%2Fb9Ry9CKBjxlXAghDd5gZExR3aAawKv8DCDUQABoMNjM3NDIzMTgzODA1IgygDAhOmYpEgdN5QkAq3APZ9Od30wjvlWPk8efRRIEKJ4u07ALZyNvVFPXXISoy6HumwOFyI%2Fw0OfBfnpbyByviC0LgFP%2Fa8vquIc8SIcSyXOvcn3mm7e7ry9b41gtUyB0AC1K8vcdpwj4vOYgp4qod4gar1nlZofMogn9K63Uoj%2BhqiPanMvBNF8H%2BycJnSO5ZtYToQtNhNDs8fBIWGVxTHISFfA%2BP3xTTCf8kbyadZPIhY1wtT6QOwZaIX60tm6DuguvN%2BtD9K%2BLDX3BFQFDEhWAhgSkKEAqvX1E1%2BXMOFCG3TD8oxASz94SO%2B%2FdszUHJXPoUw2M6xxQcKkvJT%2FuyldfRuKyzC37MfRo1zUNcvdRn5IwV4lIMjkhNs8EFhNabazcyGjX8OGbe4UuriLQ8ivxqO2mkTvBashSIEQGzYK4qPWcJ%2B%2BXiuh%2FurvWWLJMGI3DPsoq8v%2BR2II3qE9Pnl8iN82M7Uxfm9CZe86zTjfDY5EBYNZxcO0OpDMyIJ3iQEXfAbCQ16J3wc%2BuCwA7d7JHqB0mjnLq%2BpcS95XIzHP4mkL5pWJjko50a4UU4vlW3qxuXvrjVfoMpw%2F88AlQaUSLB%2FcNqUdGVz5iqzM9VnCgKc1Byh5wfX9EsGk5uMM1Iff7lNwnEvaYw%2FzCO3Ym9BjqkATA%2B%2BSglkRsrfcphKmYm2K7aid%2BMwUnx7bw0f%2BgvjI5l7axzSzJyCrr9XfG6yYBbXJxwpx%2BAeGmN8PT4lAHHMYQHUD%2FcuHx3%2FJPOaqyCm9lqcnOW7OR1bz0UCV%2FiupL2nGUxfnXWI3tmZjyTpIRwPsc7KEdP7ic3djvCOS%2BZlZkzH4NkNiTJcxW3rcl7Ed7YwdD06jZkm%2Feb76G%2BLk%2BZCSxJFmem&X-Amz-Signature=edec18c5631272698e2c1add4a3fa656002914d392d82817f4b7c6b7ce1d6d22&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBPGRGK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQD0yEn1CnLpCDCOuHPTfMvT3Ac%2FMIytI8IK0eP6rBto%2FwIhAP8VLrM1etHQemV%2Fb9Ry9CKBjxlXAghDd5gZExR3aAawKv8DCDUQABoMNjM3NDIzMTgzODA1IgygDAhOmYpEgdN5QkAq3APZ9Od30wjvlWPk8efRRIEKJ4u07ALZyNvVFPXXISoy6HumwOFyI%2Fw0OfBfnpbyByviC0LgFP%2Fa8vquIc8SIcSyXOvcn3mm7e7ry9b41gtUyB0AC1K8vcdpwj4vOYgp4qod4gar1nlZofMogn9K63Uoj%2BhqiPanMvBNF8H%2BycJnSO5ZtYToQtNhNDs8fBIWGVxTHISFfA%2BP3xTTCf8kbyadZPIhY1wtT6QOwZaIX60tm6DuguvN%2BtD9K%2BLDX3BFQFDEhWAhgSkKEAqvX1E1%2BXMOFCG3TD8oxASz94SO%2B%2FdszUHJXPoUw2M6xxQcKkvJT%2FuyldfRuKyzC37MfRo1zUNcvdRn5IwV4lIMjkhNs8EFhNabazcyGjX8OGbe4UuriLQ8ivxqO2mkTvBashSIEQGzYK4qPWcJ%2B%2BXiuh%2FurvWWLJMGI3DPsoq8v%2BR2II3qE9Pnl8iN82M7Uxfm9CZe86zTjfDY5EBYNZxcO0OpDMyIJ3iQEXfAbCQ16J3wc%2BuCwA7d7JHqB0mjnLq%2BpcS95XIzHP4mkL5pWJjko50a4UU4vlW3qxuXvrjVfoMpw%2F88AlQaUSLB%2FcNqUdGVz5iqzM9VnCgKc1Byh5wfX9EsGk5uMM1Iff7lNwnEvaYw%2FzCO3Ym9BjqkATA%2B%2BSglkRsrfcphKmYm2K7aid%2BMwUnx7bw0f%2BgvjI5l7axzSzJyCrr9XfG6yYBbXJxwpx%2BAeGmN8PT4lAHHMYQHUD%2FcuHx3%2FJPOaqyCm9lqcnOW7OR1bz0UCV%2FiupL2nGUxfnXWI3tmZjyTpIRwPsc7KEdP7ic3djvCOS%2BZlZkzH4NkNiTJcxW3rcl7Ed7YwdD06jZkm%2Feb76G%2BLk%2BZCSxJFmem&X-Amz-Signature=85ec210c024427d9847703696be3e1fc6c4e0eb51a089855660ed58189a126da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBPGRGK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQD0yEn1CnLpCDCOuHPTfMvT3Ac%2FMIytI8IK0eP6rBto%2FwIhAP8VLrM1etHQemV%2Fb9Ry9CKBjxlXAghDd5gZExR3aAawKv8DCDUQABoMNjM3NDIzMTgzODA1IgygDAhOmYpEgdN5QkAq3APZ9Od30wjvlWPk8efRRIEKJ4u07ALZyNvVFPXXISoy6HumwOFyI%2Fw0OfBfnpbyByviC0LgFP%2Fa8vquIc8SIcSyXOvcn3mm7e7ry9b41gtUyB0AC1K8vcdpwj4vOYgp4qod4gar1nlZofMogn9K63Uoj%2BhqiPanMvBNF8H%2BycJnSO5ZtYToQtNhNDs8fBIWGVxTHISFfA%2BP3xTTCf8kbyadZPIhY1wtT6QOwZaIX60tm6DuguvN%2BtD9K%2BLDX3BFQFDEhWAhgSkKEAqvX1E1%2BXMOFCG3TD8oxASz94SO%2B%2FdszUHJXPoUw2M6xxQcKkvJT%2FuyldfRuKyzC37MfRo1zUNcvdRn5IwV4lIMjkhNs8EFhNabazcyGjX8OGbe4UuriLQ8ivxqO2mkTvBashSIEQGzYK4qPWcJ%2B%2BXiuh%2FurvWWLJMGI3DPsoq8v%2BR2II3qE9Pnl8iN82M7Uxfm9CZe86zTjfDY5EBYNZxcO0OpDMyIJ3iQEXfAbCQ16J3wc%2BuCwA7d7JHqB0mjnLq%2BpcS95XIzHP4mkL5pWJjko50a4UU4vlW3qxuXvrjVfoMpw%2F88AlQaUSLB%2FcNqUdGVz5iqzM9VnCgKc1Byh5wfX9EsGk5uMM1Iff7lNwnEvaYw%2FzCO3Ym9BjqkATA%2B%2BSglkRsrfcphKmYm2K7aid%2BMwUnx7bw0f%2BgvjI5l7axzSzJyCrr9XfG6yYBbXJxwpx%2BAeGmN8PT4lAHHMYQHUD%2FcuHx3%2FJPOaqyCm9lqcnOW7OR1bz0UCV%2FiupL2nGUxfnXWI3tmZjyTpIRwPsc7KEdP7ic3djvCOS%2BZlZkzH4NkNiTJcxW3rcl7Ed7YwdD06jZkm%2Feb76G%2BLk%2BZCSxJFmem&X-Amz-Signature=2d0c14061ca2f6ed7b36a67f602ca2b4723563715f2ec3cb74ebdb7742f84b8d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYBPGRGK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQD0yEn1CnLpCDCOuHPTfMvT3Ac%2FMIytI8IK0eP6rBto%2FwIhAP8VLrM1etHQemV%2Fb9Ry9CKBjxlXAghDd5gZExR3aAawKv8DCDUQABoMNjM3NDIzMTgzODA1IgygDAhOmYpEgdN5QkAq3APZ9Od30wjvlWPk8efRRIEKJ4u07ALZyNvVFPXXISoy6HumwOFyI%2Fw0OfBfnpbyByviC0LgFP%2Fa8vquIc8SIcSyXOvcn3mm7e7ry9b41gtUyB0AC1K8vcdpwj4vOYgp4qod4gar1nlZofMogn9K63Uoj%2BhqiPanMvBNF8H%2BycJnSO5ZtYToQtNhNDs8fBIWGVxTHISFfA%2BP3xTTCf8kbyadZPIhY1wtT6QOwZaIX60tm6DuguvN%2BtD9K%2BLDX3BFQFDEhWAhgSkKEAqvX1E1%2BXMOFCG3TD8oxASz94SO%2B%2FdszUHJXPoUw2M6xxQcKkvJT%2FuyldfRuKyzC37MfRo1zUNcvdRn5IwV4lIMjkhNs8EFhNabazcyGjX8OGbe4UuriLQ8ivxqO2mkTvBashSIEQGzYK4qPWcJ%2B%2BXiuh%2FurvWWLJMGI3DPsoq8v%2BR2II3qE9Pnl8iN82M7Uxfm9CZe86zTjfDY5EBYNZxcO0OpDMyIJ3iQEXfAbCQ16J3wc%2BuCwA7d7JHqB0mjnLq%2BpcS95XIzHP4mkL5pWJjko50a4UU4vlW3qxuXvrjVfoMpw%2F88AlQaUSLB%2FcNqUdGVz5iqzM9VnCgKc1Byh5wfX9EsGk5uMM1Iff7lNwnEvaYw%2FzCO3Ym9BjqkATA%2B%2BSglkRsrfcphKmYm2K7aid%2BMwUnx7bw0f%2BgvjI5l7axzSzJyCrr9XfG6yYBbXJxwpx%2BAeGmN8PT4lAHHMYQHUD%2FcuHx3%2FJPOaqyCm9lqcnOW7OR1bz0UCV%2FiupL2nGUxfnXWI3tmZjyTpIRwPsc7KEdP7ic3djvCOS%2BZlZkzH4NkNiTJcxW3rcl7Ed7YwdD06jZkm%2Feb76G%2BLk%2BZCSxJFmem&X-Amz-Signature=80bd5cb8d5ea192e3583cd1a2d33a858a593468dc72a202a71b3dbda3adadb4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5NIC2GP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIGpX%2BKW2%2Bcuhz6YHNQcDodiPoTY04Oi6g6vJBADgwhiJAiEA%2B1BfR30fTrqJq3jUUSZspkwv2Lsw2xpHcXJ2RgsncoMq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDJIBZbBBLVx3wQ2D%2FCrcA0P7cdWhRpTm%2FxDErX2vd9LN6EkoH3rMjCV6sx03o5iTVWdy5%2FpDZHCXXyKVb7qrufZb2KF7akNZOQbANLU%2F0DH0SUd0diAiN77SxXV4tbQUT5Sa1tyqYkRCtbgTdPhLTAUYu4oupKhLd7FRSqs6%2BeWPWqTUpqqjznkSBTwAte0fR%2FGqT6mqUNsSKYlc4yh1VNLX12Rj3%2Fr9T94pwKnB9vEV46P0Q8uAvItIIkmBW2WT2RKPxMQIR88KcvGhfMUw8eyIWG9CImMqRg9WlltyJFeik5fKCSymzgStvfNkGORkBFkFixDnjLIPb7ioS8XjJrueHY15rH0ItBHdmWlVWQnaUdWAoaXdDYaZnPE4M9Pa0uidJhXidN1KTMSzw3s6brQRH0RZBmMK1YPzv94FSqS3U7ytmIIAGhsiEWLKVAfKFFyn24rS8Xlo5DLfP9NKwQ%2FWWEek64yHeD%2FDtbh0ESjMToQSiEVH%2BGiQUcTiLksLBFmftAV3CU%2BGA36rLcasi3M5clh58zcuHcS7knQPsZ2%2B%2BT4w6HobbHNAQHClunJbR4m0ZuKTzgKdrnylwAt1FmQEin0UlS7GNyBzGh8PcX6nV3ns1pEjxxXdKmOu4WM8kUUVVO4DzAHm9AI9MJrdib0GOqUB7TbFoaAXCxfAg9BIxSVIfzh1p%2BorPaO6w%2BE5b9U5gc8u%2BgAFqQJA3CAruGM4v%2FN3vXZ7LNdHj2w%2B%2FdiR06%2BmsN1tAOChV3sHTGaYAxXrHHDEKfxBaqV%2FsE4bIi1VV1tLAfYF2Qer%2B0M%2FT0RZd%2Ft8hfQWp6iN%2BKIvNII0n0rtBY55%2BzyyUXRCmjZH5hphOBultWNlGQz%2Fxg45pnNwQ%2F9eeqHxlVfk&X-Amz-Signature=6aeabad55409af4dd5157e0ca31c35756486d5899e69a8f197715be30be4cd8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2U3AHY6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIDpqgEsL5x%2F7HAyEmq%2BAIhlHddIQa7KT%2F0tCcFWfr7wRAiEAz%2FMfHqSlUxIqLgAcn7XKPSsp39kAurgrailB2TSsbZIq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDKw4I8Bd3ILzGaYDYircAzdg27wb22MZJq%2FJpNUHVRe39gkAkyZIrlJzRbohO6vXTxqY3zqBm9ZuCREKIA6Wo7eFsa9uMOlyIA5h%2FZ1viwE9jXBmwE9QgIaW9tGcRbTjIruZY7XDkoB33iLRes83CLuWrt95KQ%2FdwrL3XchjfZ582UhynY4MzWGyWQFQ7Q3N2KW4xgYeVmur8r7D9N2%2B4qvnP3db2jfaN7KWaCCsrCpnZU4mB%2BOYIs0ySCr1gKiBTcSFkvNTqNjnJ3p5ragNxZ7ENXxEC2lRKVjF2eorXK1Lr1T%2FTtc3s16M%2BeqVFevJnTAOqoC5%2BngE6iUkPax1FdgQeQcM5XthBZKOk5XcMWYyY6M%2Fm0UVbUeDoDDnyw%2BFZikGDaQnw90l3irfHzNjPmejmUUUnQBEGuf7raN0FSjzyH5VWgKlAHYnt7irpAoIsRmHY8zNxpMjNMzcAjVP3yD9Pk67qBlQGptxSRlH7ddv%2F%2Fp65sC0SJddHlPIOfa4c7q5A3X28C2YegEYrzy45ImbWdzZ30poVaA%2BEVQ%2FNz1ey8JWQEpmKSx2UPx8B9ryeFVkRr2NUkas99yCPRckRpTL5eHS4W7%2FfamGiCQ75m6JxqrZLS1KkRq%2FeIKlL96adTBuKgs5KlaYlSUYMLXdib0GOqUBcDTB90YuJPEcU2A8eNsb2GAbf0yAndY%2F6ehSGv1%2BcOFVp2OwKY6cCkGPIMPUaBoxNNN1sQ4MLB8z3zE%2BZTjen4dr%2BQVjTgYKILKXkAZGo74i5RGmfguQLTe1%2Bu%2BF%2Bw9pU1fzMEdMRP6B3k3TXZorkb2aULsG9vacWaPtZnsa2K8m7syF3HZCv9eqHXHGaZS0NBCyE4aPs1%2BYPvZxOZXGiVEN6nYd&X-Amz-Signature=c461536bf72c1b7ee417f889057028cca24b482a70f96086acb40e1216ffa17a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPYKJTJ6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIF9uzIVJjHVh6DtU5bnxVG74PzlDl2HuDrSZm9EuHHU%2FAiEAzTNUHYEXDHpbKQpzMQMOH%2Be6QXsyaR%2F7%2FwMfpK89XSAq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDN1x1ng0XGBdT2U%2FSyrcAxBzNZLaOV69LvaGFoYVUR0PNV6qEbkrnSS92oJhh1oLhkagwetEoIxLV7vIfQFOh5D2hbToOI%2FM%2BS4bYTVPu3T%2Bwu5hw%2FomUsqTOtmJ04k12Cb2%2BGaDs5AEOkVIdoEfsfFwgaehzHMH3jUmm%2BEk779zdehuLyoehXr8EBb1rKjfS2Cldl3jjwNtcSu0qIYS%2BKBRWf4iCT0ek5%2FtA4Sa9fD91tJb6N14dsepnRAdVuPf6u4z%2BUD9wWehoUma%2FsalpLSPXGf57gxrGckWYbHhr1pbw48IS8y62Xz6v0UY0qgRkmXuYMNMvcaCT0bTlMHzcIJ3fSIcvQQGwl%2FWD9%2Be4AOu0HO9cAt58W2wRSERjhHCeNtE0sJpva49lKbiXBgzOQaE3bA2V0w38Fs%2B%2B6NKcjPzEBFmRJOZJjt9bQ%2FPGn%2FO3Es8bJC8P%2BQxy4WN2YlwsYk3FoWLNXgWGHjFkewsOrQlSOP%2BKyA0zvfdsAJVZa5dRVqqdwcR%2Btj9QXotQJe9wPYsASncJRZ%2F38nc%2FLmucilKtcStcu7QTq%2F8huzG1LDCSniCtzOMS%2BH4%2Fri3Bsj08m0oDjZXBK0NP7cpwiLzFdPbzOHtkPMW7vUMhLWKkfXR8e81wJdiWSRhjddZMLXdib0GOqUBvOG7OJnQnr2bomASjKD7RF%2F3Mflb2XlyKR9VNu3qC61dxXNmtMMbn%2B6XLdoDAqcuUpYaTa89icKX%2FID%2BlGKbBi1b49oCApe2DCv7AZHld94RQPlCTthSSgeslEKb5o8dg0kd4HyvOl8NLMnjXRlsjF4ckbf5FEpV3GHNspvNMDzsJt%2FnbVxEaxTCnZWPjjBycsyeYhrmInbcR5Sec1MsRZWkCrCz&X-Amz-Signature=8d40d8f376f7a9ccfd2ba79a9b0d15888a2768277007b8876c4854d295df6e7d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPYKJTJ6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIF9uzIVJjHVh6DtU5bnxVG74PzlDl2HuDrSZm9EuHHU%2FAiEAzTNUHYEXDHpbKQpzMQMOH%2Be6QXsyaR%2F7%2FwMfpK89XSAq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDN1x1ng0XGBdT2U%2FSyrcAxBzNZLaOV69LvaGFoYVUR0PNV6qEbkrnSS92oJhh1oLhkagwetEoIxLV7vIfQFOh5D2hbToOI%2FM%2BS4bYTVPu3T%2Bwu5hw%2FomUsqTOtmJ04k12Cb2%2BGaDs5AEOkVIdoEfsfFwgaehzHMH3jUmm%2BEk779zdehuLyoehXr8EBb1rKjfS2Cldl3jjwNtcSu0qIYS%2BKBRWf4iCT0ek5%2FtA4Sa9fD91tJb6N14dsepnRAdVuPf6u4z%2BUD9wWehoUma%2FsalpLSPXGf57gxrGckWYbHhr1pbw48IS8y62Xz6v0UY0qgRkmXuYMNMvcaCT0bTlMHzcIJ3fSIcvQQGwl%2FWD9%2Be4AOu0HO9cAt58W2wRSERjhHCeNtE0sJpva49lKbiXBgzOQaE3bA2V0w38Fs%2B%2B6NKcjPzEBFmRJOZJjt9bQ%2FPGn%2FO3Es8bJC8P%2BQxy4WN2YlwsYk3FoWLNXgWGHjFkewsOrQlSOP%2BKyA0zvfdsAJVZa5dRVqqdwcR%2Btj9QXotQJe9wPYsASncJRZ%2F38nc%2FLmucilKtcStcu7QTq%2F8huzG1LDCSniCtzOMS%2BH4%2Fri3Bsj08m0oDjZXBK0NP7cpwiLzFdPbzOHtkPMW7vUMhLWKkfXR8e81wJdiWSRhjddZMLXdib0GOqUBvOG7OJnQnr2bomASjKD7RF%2F3Mflb2XlyKR9VNu3qC61dxXNmtMMbn%2B6XLdoDAqcuUpYaTa89icKX%2FID%2BlGKbBi1b49oCApe2DCv7AZHld94RQPlCTthSSgeslEKb5o8dg0kd4HyvOl8NLMnjXRlsjF4ckbf5FEpV3GHNspvNMDzsJt%2FnbVxEaxTCnZWPjjBycsyeYhrmInbcR5Sec1MsRZWkCrCz&X-Amz-Signature=d280cad376b65e85ba26905334dbcb9cddb5aeac7e646ab47a547dfc9f0c5d7b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
