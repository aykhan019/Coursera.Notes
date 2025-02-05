

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JTETVRK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBbVCSuq8%2BQ%2FF%2BDN7JSec%2B5DeiyNyzyFZ737WTNZdmkEAiEAnM%2By7XJfMHu7fM8CSQpwbYxk%2FTAyq2EAgYey%2ByRFZx0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAEcZauJAiffm%2Bt5fyrcA4EzavE2mmli3vud9AcSLcpH8FmQTEUnnloR%2FZr4W7NXrkzGTeQGrU67q3J5ybF5C%2F9QKt7YR%2FsZ1ZPjKLg75gONr8pxBW17y2GJNjUsBzc%2F0puLaDE%2Fbg0CYvVVHOIstk5dzBGE8PZTMeBiqeT6ZcZYJxxqki0u%2BMkeSi%2FlNA%2Bw1zsD7wlVJVdqnig7KenSjcD4TgN9YsdOSJJsV077m9H%2B46xLZ5h7ajzjJF1%2FCYdipWr2TB89bnUQf3dvdAto9NSnmzJB%2F15ur%2B3Am1u36btGu7pLjENEzHJgd3htjyrE3iB02gNwkYVQuWF3bwj69R16gUqccFNqasxMNYu5LenLkZWWvq7kgmJ5mYhZqOi08YIwIZZwtMhvNDkmNt4wFSNbTomp1PRA4Cv42SnJv5usFdXQge3JMOzH3djaskMtsNQHxLmTtyoLogsOefNxBoNhRxSQSs%2F16GcNDXBxCBTbxNq1p%2BCD%2FifshfkUlQpYUQA4Ytmr0KxGWJgMdMaq%2BpiaQmoTZXczsdTLDDyHeIPSOIfE4vQ%2F9ivWQ3x97n%2FSbc272ZhoGLQobgQzdOKpaMtJ%2FL9DXyFRs9sV71H1GFJC%2Bn7sFSFndep1TWnBO6gFPAskGpv8VOhZoximMKzNir0GOqUBoq3PmjRFtq0h19S022QMJcofEkT5LNIOHkDzqEM1XRkVsq1Q9X73gQnRrXSdfo7XaOaXN1frJR98d3dXBQLqHu4EgyBFlGa4Md%2FobZ6jQoRfs23n7sRs7f1KX0bLsxH6DXtekg11C8GyyBiqhmAkkhjsEgubBNGixLd2z8lbXzjh733T6a6IRYsDDiTMJJ8o4Lc23WakDP0CCiBZy%2FSdOIwKapI2&X-Amz-Signature=6dac8bc60176fae83ba3767faff8ee0d4ff62addfb6c5a917c2528ea25121380&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JTETVRK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBbVCSuq8%2BQ%2FF%2BDN7JSec%2B5DeiyNyzyFZ737WTNZdmkEAiEAnM%2By7XJfMHu7fM8CSQpwbYxk%2FTAyq2EAgYey%2ByRFZx0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAEcZauJAiffm%2Bt5fyrcA4EzavE2mmli3vud9AcSLcpH8FmQTEUnnloR%2FZr4W7NXrkzGTeQGrU67q3J5ybF5C%2F9QKt7YR%2FsZ1ZPjKLg75gONr8pxBW17y2GJNjUsBzc%2F0puLaDE%2Fbg0CYvVVHOIstk5dzBGE8PZTMeBiqeT6ZcZYJxxqki0u%2BMkeSi%2FlNA%2Bw1zsD7wlVJVdqnig7KenSjcD4TgN9YsdOSJJsV077m9H%2B46xLZ5h7ajzjJF1%2FCYdipWr2TB89bnUQf3dvdAto9NSnmzJB%2F15ur%2B3Am1u36btGu7pLjENEzHJgd3htjyrE3iB02gNwkYVQuWF3bwj69R16gUqccFNqasxMNYu5LenLkZWWvq7kgmJ5mYhZqOi08YIwIZZwtMhvNDkmNt4wFSNbTomp1PRA4Cv42SnJv5usFdXQge3JMOzH3djaskMtsNQHxLmTtyoLogsOefNxBoNhRxSQSs%2F16GcNDXBxCBTbxNq1p%2BCD%2FifshfkUlQpYUQA4Ytmr0KxGWJgMdMaq%2BpiaQmoTZXczsdTLDDyHeIPSOIfE4vQ%2F9ivWQ3x97n%2FSbc272ZhoGLQobgQzdOKpaMtJ%2FL9DXyFRs9sV71H1GFJC%2Bn7sFSFndep1TWnBO6gFPAskGpv8VOhZoximMKzNir0GOqUBoq3PmjRFtq0h19S022QMJcofEkT5LNIOHkDzqEM1XRkVsq1Q9X73gQnRrXSdfo7XaOaXN1frJR98d3dXBQLqHu4EgyBFlGa4Md%2FobZ6jQoRfs23n7sRs7f1KX0bLsxH6DXtekg11C8GyyBiqhmAkkhjsEgubBNGixLd2z8lbXzjh733T6a6IRYsDDiTMJJ8o4Lc23WakDP0CCiBZy%2FSdOIwKapI2&X-Amz-Signature=21d9bea4028e35f5e22a5b81b877e6f05e303b91a304c0fad5b0f9c876b2758b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JTETVRK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBbVCSuq8%2BQ%2FF%2BDN7JSec%2B5DeiyNyzyFZ737WTNZdmkEAiEAnM%2By7XJfMHu7fM8CSQpwbYxk%2FTAyq2EAgYey%2ByRFZx0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAEcZauJAiffm%2Bt5fyrcA4EzavE2mmli3vud9AcSLcpH8FmQTEUnnloR%2FZr4W7NXrkzGTeQGrU67q3J5ybF5C%2F9QKt7YR%2FsZ1ZPjKLg75gONr8pxBW17y2GJNjUsBzc%2F0puLaDE%2Fbg0CYvVVHOIstk5dzBGE8PZTMeBiqeT6ZcZYJxxqki0u%2BMkeSi%2FlNA%2Bw1zsD7wlVJVdqnig7KenSjcD4TgN9YsdOSJJsV077m9H%2B46xLZ5h7ajzjJF1%2FCYdipWr2TB89bnUQf3dvdAto9NSnmzJB%2F15ur%2B3Am1u36btGu7pLjENEzHJgd3htjyrE3iB02gNwkYVQuWF3bwj69R16gUqccFNqasxMNYu5LenLkZWWvq7kgmJ5mYhZqOi08YIwIZZwtMhvNDkmNt4wFSNbTomp1PRA4Cv42SnJv5usFdXQge3JMOzH3djaskMtsNQHxLmTtyoLogsOefNxBoNhRxSQSs%2F16GcNDXBxCBTbxNq1p%2BCD%2FifshfkUlQpYUQA4Ytmr0KxGWJgMdMaq%2BpiaQmoTZXczsdTLDDyHeIPSOIfE4vQ%2F9ivWQ3x97n%2FSbc272ZhoGLQobgQzdOKpaMtJ%2FL9DXyFRs9sV71H1GFJC%2Bn7sFSFndep1TWnBO6gFPAskGpv8VOhZoximMKzNir0GOqUBoq3PmjRFtq0h19S022QMJcofEkT5LNIOHkDzqEM1XRkVsq1Q9X73gQnRrXSdfo7XaOaXN1frJR98d3dXBQLqHu4EgyBFlGa4Md%2FobZ6jQoRfs23n7sRs7f1KX0bLsxH6DXtekg11C8GyyBiqhmAkkhjsEgubBNGixLd2z8lbXzjh733T6a6IRYsDDiTMJJ8o4Lc23WakDP0CCiBZy%2FSdOIwKapI2&X-Amz-Signature=94a525ebfe3c1491d976c7a15a3c833c0b252c7d48bbcfabaf774e148da682df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JTETVRK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBbVCSuq8%2BQ%2FF%2BDN7JSec%2B5DeiyNyzyFZ737WTNZdmkEAiEAnM%2By7XJfMHu7fM8CSQpwbYxk%2FTAyq2EAgYey%2ByRFZx0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAEcZauJAiffm%2Bt5fyrcA4EzavE2mmli3vud9AcSLcpH8FmQTEUnnloR%2FZr4W7NXrkzGTeQGrU67q3J5ybF5C%2F9QKt7YR%2FsZ1ZPjKLg75gONr8pxBW17y2GJNjUsBzc%2F0puLaDE%2Fbg0CYvVVHOIstk5dzBGE8PZTMeBiqeT6ZcZYJxxqki0u%2BMkeSi%2FlNA%2Bw1zsD7wlVJVdqnig7KenSjcD4TgN9YsdOSJJsV077m9H%2B46xLZ5h7ajzjJF1%2FCYdipWr2TB89bnUQf3dvdAto9NSnmzJB%2F15ur%2B3Am1u36btGu7pLjENEzHJgd3htjyrE3iB02gNwkYVQuWF3bwj69R16gUqccFNqasxMNYu5LenLkZWWvq7kgmJ5mYhZqOi08YIwIZZwtMhvNDkmNt4wFSNbTomp1PRA4Cv42SnJv5usFdXQge3JMOzH3djaskMtsNQHxLmTtyoLogsOefNxBoNhRxSQSs%2F16GcNDXBxCBTbxNq1p%2BCD%2FifshfkUlQpYUQA4Ytmr0KxGWJgMdMaq%2BpiaQmoTZXczsdTLDDyHeIPSOIfE4vQ%2F9ivWQ3x97n%2FSbc272ZhoGLQobgQzdOKpaMtJ%2FL9DXyFRs9sV71H1GFJC%2Bn7sFSFndep1TWnBO6gFPAskGpv8VOhZoximMKzNir0GOqUBoq3PmjRFtq0h19S022QMJcofEkT5LNIOHkDzqEM1XRkVsq1Q9X73gQnRrXSdfo7XaOaXN1frJR98d3dXBQLqHu4EgyBFlGa4Md%2FobZ6jQoRfs23n7sRs7f1KX0bLsxH6DXtekg11C8GyyBiqhmAkkhjsEgubBNGixLd2z8lbXzjh733T6a6IRYsDDiTMJJ8o4Lc23WakDP0CCiBZy%2FSdOIwKapI2&X-Amz-Signature=4c0e36455c3cf6942923e0f8b0a61c35fa80e692da041c0cdd80e7924895ccdd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JTETVRK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBbVCSuq8%2BQ%2FF%2BDN7JSec%2B5DeiyNyzyFZ737WTNZdmkEAiEAnM%2By7XJfMHu7fM8CSQpwbYxk%2FTAyq2EAgYey%2ByRFZx0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAEcZauJAiffm%2Bt5fyrcA4EzavE2mmli3vud9AcSLcpH8FmQTEUnnloR%2FZr4W7NXrkzGTeQGrU67q3J5ybF5C%2F9QKt7YR%2FsZ1ZPjKLg75gONr8pxBW17y2GJNjUsBzc%2F0puLaDE%2Fbg0CYvVVHOIstk5dzBGE8PZTMeBiqeT6ZcZYJxxqki0u%2BMkeSi%2FlNA%2Bw1zsD7wlVJVdqnig7KenSjcD4TgN9YsdOSJJsV077m9H%2B46xLZ5h7ajzjJF1%2FCYdipWr2TB89bnUQf3dvdAto9NSnmzJB%2F15ur%2B3Am1u36btGu7pLjENEzHJgd3htjyrE3iB02gNwkYVQuWF3bwj69R16gUqccFNqasxMNYu5LenLkZWWvq7kgmJ5mYhZqOi08YIwIZZwtMhvNDkmNt4wFSNbTomp1PRA4Cv42SnJv5usFdXQge3JMOzH3djaskMtsNQHxLmTtyoLogsOefNxBoNhRxSQSs%2F16GcNDXBxCBTbxNq1p%2BCD%2FifshfkUlQpYUQA4Ytmr0KxGWJgMdMaq%2BpiaQmoTZXczsdTLDDyHeIPSOIfE4vQ%2F9ivWQ3x97n%2FSbc272ZhoGLQobgQzdOKpaMtJ%2FL9DXyFRs9sV71H1GFJC%2Bn7sFSFndep1TWnBO6gFPAskGpv8VOhZoximMKzNir0GOqUBoq3PmjRFtq0h19S022QMJcofEkT5LNIOHkDzqEM1XRkVsq1Q9X73gQnRrXSdfo7XaOaXN1frJR98d3dXBQLqHu4EgyBFlGa4Md%2FobZ6jQoRfs23n7sRs7f1KX0bLsxH6DXtekg11C8GyyBiqhmAkkhjsEgubBNGixLd2z8lbXzjh733T6a6IRYsDDiTMJJ8o4Lc23WakDP0CCiBZy%2FSdOIwKapI2&X-Amz-Signature=70bad03540834a3ade42c399c10f676e37a393bb8bc3f79170b6b666648b8df3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JTETVRK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBbVCSuq8%2BQ%2FF%2BDN7JSec%2B5DeiyNyzyFZ737WTNZdmkEAiEAnM%2By7XJfMHu7fM8CSQpwbYxk%2FTAyq2EAgYey%2ByRFZx0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAEcZauJAiffm%2Bt5fyrcA4EzavE2mmli3vud9AcSLcpH8FmQTEUnnloR%2FZr4W7NXrkzGTeQGrU67q3J5ybF5C%2F9QKt7YR%2FsZ1ZPjKLg75gONr8pxBW17y2GJNjUsBzc%2F0puLaDE%2Fbg0CYvVVHOIstk5dzBGE8PZTMeBiqeT6ZcZYJxxqki0u%2BMkeSi%2FlNA%2Bw1zsD7wlVJVdqnig7KenSjcD4TgN9YsdOSJJsV077m9H%2B46xLZ5h7ajzjJF1%2FCYdipWr2TB89bnUQf3dvdAto9NSnmzJB%2F15ur%2B3Am1u36btGu7pLjENEzHJgd3htjyrE3iB02gNwkYVQuWF3bwj69R16gUqccFNqasxMNYu5LenLkZWWvq7kgmJ5mYhZqOi08YIwIZZwtMhvNDkmNt4wFSNbTomp1PRA4Cv42SnJv5usFdXQge3JMOzH3djaskMtsNQHxLmTtyoLogsOefNxBoNhRxSQSs%2F16GcNDXBxCBTbxNq1p%2BCD%2FifshfkUlQpYUQA4Ytmr0KxGWJgMdMaq%2BpiaQmoTZXczsdTLDDyHeIPSOIfE4vQ%2F9ivWQ3x97n%2FSbc272ZhoGLQobgQzdOKpaMtJ%2FL9DXyFRs9sV71H1GFJC%2Bn7sFSFndep1TWnBO6gFPAskGpv8VOhZoximMKzNir0GOqUBoq3PmjRFtq0h19S022QMJcofEkT5LNIOHkDzqEM1XRkVsq1Q9X73gQnRrXSdfo7XaOaXN1frJR98d3dXBQLqHu4EgyBFlGa4Md%2FobZ6jQoRfs23n7sRs7f1KX0bLsxH6DXtekg11C8GyyBiqhmAkkhjsEgubBNGixLd2z8lbXzjh733T6a6IRYsDDiTMJJ8o4Lc23WakDP0CCiBZy%2FSdOIwKapI2&X-Amz-Signature=509b5baaf254b9822445d6a71ea8ad02e626a4a4b2ebca93a61d5ca9879dad66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JTETVRK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBbVCSuq8%2BQ%2FF%2BDN7JSec%2B5DeiyNyzyFZ737WTNZdmkEAiEAnM%2By7XJfMHu7fM8CSQpwbYxk%2FTAyq2EAgYey%2ByRFZx0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAEcZauJAiffm%2Bt5fyrcA4EzavE2mmli3vud9AcSLcpH8FmQTEUnnloR%2FZr4W7NXrkzGTeQGrU67q3J5ybF5C%2F9QKt7YR%2FsZ1ZPjKLg75gONr8pxBW17y2GJNjUsBzc%2F0puLaDE%2Fbg0CYvVVHOIstk5dzBGE8PZTMeBiqeT6ZcZYJxxqki0u%2BMkeSi%2FlNA%2Bw1zsD7wlVJVdqnig7KenSjcD4TgN9YsdOSJJsV077m9H%2B46xLZ5h7ajzjJF1%2FCYdipWr2TB89bnUQf3dvdAto9NSnmzJB%2F15ur%2B3Am1u36btGu7pLjENEzHJgd3htjyrE3iB02gNwkYVQuWF3bwj69R16gUqccFNqasxMNYu5LenLkZWWvq7kgmJ5mYhZqOi08YIwIZZwtMhvNDkmNt4wFSNbTomp1PRA4Cv42SnJv5usFdXQge3JMOzH3djaskMtsNQHxLmTtyoLogsOefNxBoNhRxSQSs%2F16GcNDXBxCBTbxNq1p%2BCD%2FifshfkUlQpYUQA4Ytmr0KxGWJgMdMaq%2BpiaQmoTZXczsdTLDDyHeIPSOIfE4vQ%2F9ivWQ3x97n%2FSbc272ZhoGLQobgQzdOKpaMtJ%2FL9DXyFRs9sV71H1GFJC%2Bn7sFSFndep1TWnBO6gFPAskGpv8VOhZoximMKzNir0GOqUBoq3PmjRFtq0h19S022QMJcofEkT5LNIOHkDzqEM1XRkVsq1Q9X73gQnRrXSdfo7XaOaXN1frJR98d3dXBQLqHu4EgyBFlGa4Md%2FobZ6jQoRfs23n7sRs7f1KX0bLsxH6DXtekg11C8GyyBiqhmAkkhjsEgubBNGixLd2z8lbXzjh733T6a6IRYsDDiTMJJ8o4Lc23WakDP0CCiBZy%2FSdOIwKapI2&X-Amz-Signature=51aabeb87c0366a14a7bec06dadfaa2c75343d48dcdd880b6349e54dcbd91c88&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JTETVRK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIBbVCSuq8%2BQ%2FF%2BDN7JSec%2B5DeiyNyzyFZ737WTNZdmkEAiEAnM%2By7XJfMHu7fM8CSQpwbYxk%2FTAyq2EAgYey%2ByRFZx0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDAEcZauJAiffm%2Bt5fyrcA4EzavE2mmli3vud9AcSLcpH8FmQTEUnnloR%2FZr4W7NXrkzGTeQGrU67q3J5ybF5C%2F9QKt7YR%2FsZ1ZPjKLg75gONr8pxBW17y2GJNjUsBzc%2F0puLaDE%2Fbg0CYvVVHOIstk5dzBGE8PZTMeBiqeT6ZcZYJxxqki0u%2BMkeSi%2FlNA%2Bw1zsD7wlVJVdqnig7KenSjcD4TgN9YsdOSJJsV077m9H%2B46xLZ5h7ajzjJF1%2FCYdipWr2TB89bnUQf3dvdAto9NSnmzJB%2F15ur%2B3Am1u36btGu7pLjENEzHJgd3htjyrE3iB02gNwkYVQuWF3bwj69R16gUqccFNqasxMNYu5LenLkZWWvq7kgmJ5mYhZqOi08YIwIZZwtMhvNDkmNt4wFSNbTomp1PRA4Cv42SnJv5usFdXQge3JMOzH3djaskMtsNQHxLmTtyoLogsOefNxBoNhRxSQSs%2F16GcNDXBxCBTbxNq1p%2BCD%2FifshfkUlQpYUQA4Ytmr0KxGWJgMdMaq%2BpiaQmoTZXczsdTLDDyHeIPSOIfE4vQ%2F9ivWQ3x97n%2FSbc272ZhoGLQobgQzdOKpaMtJ%2FL9DXyFRs9sV71H1GFJC%2Bn7sFSFndep1TWnBO6gFPAskGpv8VOhZoximMKzNir0GOqUBoq3PmjRFtq0h19S022QMJcofEkT5LNIOHkDzqEM1XRkVsq1Q9X73gQnRrXSdfo7XaOaXN1frJR98d3dXBQLqHu4EgyBFlGa4Md%2FobZ6jQoRfs23n7sRs7f1KX0bLsxH6DXtekg11C8GyyBiqhmAkkhjsEgubBNGixLd2z8lbXzjh733T6a6IRYsDDiTMJJ8o4Lc23WakDP0CCiBZy%2FSdOIwKapI2&X-Amz-Signature=f9c86f4b793e52e078ae546e2e4374378144ece8b2f75e21f268df90a9fc3289&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666OIGZ7Q%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIB4goPSoD25WKnaqKGtDqXYvO5B98%2BFAMQcgDvwH%2FugUAiEA09UdAnTAeeWNdFUWhzBDaSzc8HpKJax3LpkkiVJiVbYq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDKLiUmoGj%2F9n4ulnPCrcA8WVZui2tJZ7975BOhrnJxukXUW6ZXUl6axCte8G%2BLK5h29qizhaXSuzuphu%2FYK%2Fvsfyj8AvE2NQjfy%2BToAPKU47nO9nmFIOuicFzdkZARhv%2ByyrN7ykWu7Unnz2TwxViq6ykEpeoHQ5RRiim9ubg%2F2FsoYSVRFs56UCfwx5jlhQVXQgTyYitBvDbBzupFAD0A%2BkqKO1N9Ftxy9%2BJjGAW4kAVlMqv8zii39sSupmFuaIwMpIdOCRQ0FQ7ZTbpss3iURljHkNrwzc0QFSYlRq295nGBaZFIYxEm38LniKdfbDPL6tS3TnIrAZxptiDh6TYjH73qiso342oO4cOoj5fmzX47Mt97Q2epk6uaJ3yNK60SpBgXUg7IZMHocxqORkDyjTfyWLySyRIxCTmMcyPh%2Bw0vc%2F5SV%2BBZCGYgpPvGh8Ypoh1IQur7wRcEsHvmIrEa%2BSb0tMqms16H0dPIRusMBnXIPRXvcyIj9U5SMR5VLNbw43GrS5yQUK7GXMMdhezlXFo7ZdidT3kH%2BZXpHDK8XeRpxZoOLZs92JMbeTY%2BO1OwvftgTH7uZTDFkB1z%2B1Iiqkd5nhaZvIvGuzpxYGPCoaQfa7qzCa1KNbilfBMFW8g%2BXsKflIzoKQO0NiMJTNir0GOqUB0bGt%2B6Z3ieUIbusAvDk3BgIbqFZg18htvAHv8NKDnb%2B5EIG6grh3KcqHhbDSiQ5NZaKYx2W1ubbcNBpZZd301mdeUlA%2B%2BLXQw5V8VIFFq9zYPFcyF9pzjmUPJhDLMx2rBSpsjGUuVRhf0DT9AQMohHrKW%2F2iwV4uGboyr64P1zYc6G0Vp03ueZToHOSNCX2Q2usrrJOwoPsViKm6dNlv4byH6uiN&X-Amz-Signature=56022765f86f968f1cba0ef9f35694d504569c8d2c7cb069cbb7c2b025856935&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IMEEGD3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIFaaDFt89ZCOUMtuCB3r%2Fh%2FhWK3rJCbiXg75Ez486rpUAiEAoiezVfJDDX2hk8JHo96ERt2jlyWhDlki6%2Bu%2FZAT3BE4q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDPVBMwIg%2B8HK5HfExyrcA%2Bwmp4kuksUfzbyP9ByTWDrfUIpXAyjSSBYElYn7Cp5zwHFLe1XEME3P70cxjucYEjWUTfN4kitrZMU8wRBk6sDHoPPCW9baIymC0pDqpzuIm%2FAK6FiG%2FQ0zgfY4o%2FLIOVag0kyHowoxPIDErbBv%2BNgPppq09lcVNL8tsilO3PlLjGIYeGsrad%2Fume%2F5u1g9Qa8KV3WtDu4RW1AsddpERuLfuPCDP3SAF98%2F9gEzZzxO0YBklg9NFM9OABXv1xbFS3WtUrZoyAWGy7pmMtDKVD8ZGHSgjbswfRmvKNWlqSFHKg0n3R%2FeEqt%2BceBTMmxSIbOCF4stwn0o3tpmbJMHOp9sBGpUXUKQo6GWsUnanuZVhXdXN1hfJaR3u0QW8mEPNsMuErH%2BTALaYuX8sZaBayyKP7qWkshYWInZFDc0aWnBTXhhQ4lEN1nvsXCD%2Fg2HcXvmxkLpIsUkpsvh7UW3GYHGmG4RiSEOlAc%2BhLRH7bCxSbAVV%2BZP%2FTkcvoUYTTLoufp9shLXih%2B%2FDFa7ap%2Bqcw5P%2FlUsxlBhg82CNkCyuyl8IScgGE3AoOtgA7pKqD1nIv8uxONq3NtJ8b9UC3sjWul0oxqeYUTkqh8m6bXoBY%2F24yPoBqaTQZi1aiGnMOfMir0GOqUBPqe%2FdmE1iMSA3y3RVirPu8b6baVfEymtV2jua692JH3gVUPrMjYXCGL6P%2FkKTXeosMG66uK3GunDNgkPqOL8QVR%2B%2BY0vhd%2FHAfmsbl91g7AQ7T2NBKBgqR%2FNgGMEjdfYio8nhPTv16hQb4sjpPbHZ6NI8THbvaHfaT6up6JZJmTumQcfL%2B1ngZ3UkdfHAf2ITfKuIvat0vJ4RCb4ZFddLGdw5F0J&X-Amz-Signature=c53ed36ff21a17ea635c0abe9f2be6da2ace9662516abf54038a794b246e9ea1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THO5L5RW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDNJq8Ts7Y%2F8khtZWyk5VeN5hvCbbIiQxuqk%2FbF4gC47AiEArWOarmp5DOewuRVQt1bs8Ppv7Djl29bQI4aIlvrG0rMq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDKbop0SVWw84NivPByrcA76EZOpLwb7mCGKlJGxSFRHuYItZY4oqXxd8x3mxfeYU4wgACej47fb87OLld2y3KPOOLjgKp6himsP3%2FuDS07TIcuWRbLS2RVHEM%2BJt9bS95yiQeRAoUup1iFu6nAHjDwzYkxKWNYG5GbFnWb%2FQ1PnHgQ3PAW7MFSg4F%2BLvxog%2BD0aAf1enZiEDtx8epTz8ZMrM%2BEyQQJ3UW%2BUZCRZm1iGe1g%2FFKYQOwFTswhh%2BTakBdCweCRMUS5cb0D3o7V4pFNyplYep4sybaqZ218Os2ATT8q0%2BDoAN0k6%2BvEQT24ED51AXDCrhLVc9x7M%2BA%2BPoVw9%2F0FIpRKiPgwtdDizBZCPRC6AgzXyahPc%2FsAvqgfXtuH560zCVsPCHBjB%2FcSJAH16%2F5NX5pEcqm14UEQjPMG4zj3KBbvFFKkXV890CulbjGhYoRbZ3PjGVvl5xGqbE1Qns97Nbv4DjxJd0tkeUzKVwhGGnavVh3WCOsscztbKH2z7i4FW3AXU9r80mbV359MoLr5hhX2w%2BGC%2FDGz1oSzDJvdWrnizoCsWm7AdhkU59E0VPnk9osE4iXp6%2BaEvQ%2FQFMZI8yMMdoXj19DIZLDiwAd7zZYmc3ZLRBC4K3UMf8jfAXi9EIVWQmJrCeMOzMir0GOqUB3NINgWKIttSzcu4PpUux7JhkwlZU4WxallzZ6SbzI7YGcIbNH%2B5snoPVi6VLTD9yGWCsAdP0vr6XT74Q8hFa9cj%2BDUBlqZmTr1MDs8LO4xT3yXlkD4DgCUxhd%2BQc1wJTxSFvMX0tECHIQVgxHu%2F3o%2BbFkbzT0AgwlT0BIcZF7zyRSTFTW4shTY25BPZNoUGiGKt596hQYIhPNUu4w3elMt5JrjnM&X-Amz-Signature=492818164779f45ecbe49a3944052fb6486e8d1824281a76fd51900986f324fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THO5L5RW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDNJq8Ts7Y%2F8khtZWyk5VeN5hvCbbIiQxuqk%2FbF4gC47AiEArWOarmp5DOewuRVQt1bs8Ppv7Djl29bQI4aIlvrG0rMq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDKbop0SVWw84NivPByrcA76EZOpLwb7mCGKlJGxSFRHuYItZY4oqXxd8x3mxfeYU4wgACej47fb87OLld2y3KPOOLjgKp6himsP3%2FuDS07TIcuWRbLS2RVHEM%2BJt9bS95yiQeRAoUup1iFu6nAHjDwzYkxKWNYG5GbFnWb%2FQ1PnHgQ3PAW7MFSg4F%2BLvxog%2BD0aAf1enZiEDtx8epTz8ZMrM%2BEyQQJ3UW%2BUZCRZm1iGe1g%2FFKYQOwFTswhh%2BTakBdCweCRMUS5cb0D3o7V4pFNyplYep4sybaqZ218Os2ATT8q0%2BDoAN0k6%2BvEQT24ED51AXDCrhLVc9x7M%2BA%2BPoVw9%2F0FIpRKiPgwtdDizBZCPRC6AgzXyahPc%2FsAvqgfXtuH560zCVsPCHBjB%2FcSJAH16%2F5NX5pEcqm14UEQjPMG4zj3KBbvFFKkXV890CulbjGhYoRbZ3PjGVvl5xGqbE1Qns97Nbv4DjxJd0tkeUzKVwhGGnavVh3WCOsscztbKH2z7i4FW3AXU9r80mbV359MoLr5hhX2w%2BGC%2FDGz1oSzDJvdWrnizoCsWm7AdhkU59E0VPnk9osE4iXp6%2BaEvQ%2FQFMZI8yMMdoXj19DIZLDiwAd7zZYmc3ZLRBC4K3UMf8jfAXi9EIVWQmJrCeMOzMir0GOqUB3NINgWKIttSzcu4PpUux7JhkwlZU4WxallzZ6SbzI7YGcIbNH%2B5snoPVi6VLTD9yGWCsAdP0vr6XT74Q8hFa9cj%2BDUBlqZmTr1MDs8LO4xT3yXlkD4DgCUxhd%2BQc1wJTxSFvMX0tECHIQVgxHu%2F3o%2BbFkbzT0AgwlT0BIcZF7zyRSTFTW4shTY25BPZNoUGiGKt596hQYIhPNUu4w3elMt5JrjnM&X-Amz-Signature=22e2f41985c7b5c927123a94fee48b80fb59a4cd0c34093387e9ec2efd621c16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
