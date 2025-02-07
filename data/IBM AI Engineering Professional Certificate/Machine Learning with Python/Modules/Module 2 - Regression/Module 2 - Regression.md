

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XEDSGXB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBdHoKHshoF9ScU8GMgX3W8d3FDJ0EYbEflM8v7MJnVSAiA3tJq4S0vvYqYmbg96L%2BDd9KteL%2FLPz%2Fv8dbT3YXEHIir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMEyTCQdvs54ShVvjjKtwDRiQ2lzA7F0nfSvB%2FGYbveIj9WfnQD99Ym%2Btj0yGCx2r97YnhJDhezCYJDuqH1%2BxdNki5wufD0rKq9qp%2FLExjTBPNVTm28nxwk%2B9qZDdc3QgemCaBlt7nMzCdBHq3qWZmjySSUrIamur4YkFamIGw5uoHPsnvB11r5FPAv2MvmZv%2FX2lhFIGlr%2BjTmBiyhJhu8NBuqEzcoiG4tfmi1zfE7XYWsjO%2B4GBEbtKbQWYyopdFEKnrMC6%2B5MSqIuEj7cA95jLbH0pSP5is%2B6%2BhEWQ2jayBmdVLiufDwaw86%2F0S%2F1rjFzdVWdynvY%2BZihC8u1h8X5F4gJXq5gtT1X8em6EE0kngXFE7BBjXZGIfTgm4%2B6jve9kb4Z4krIntprpv93C7KDQfxTAsRmTSpEx3V3G%2FspEBzSER0IFXponQk37Avq%2FX13aJsPElgusBJvwVVZn9yVsG%2Bo%2FjuAhj%2BSQcdRbEheH0yq6ARIE4LHeL27CYsIzO7Ogs2bkO9hwJ%2F647CQeuKjMHJg3UhpC5t5iTBiJLO36xEH%2FpVd09GvOLGLPtBMZ8qcuFDXTkh6uSSp0K3iZTAq%2BahOe2pHz6btv8JbLaybsj2t7ucxnYadFyfMvX5mYnep8QEWt9PvElVt8wnouYvQY6pgEom6PgrwZX1Tqt2lxnnXihADqRsd8piDamMrCm2yXtKoHkGGzekHBWTppN7kfrT%2FdOjrz8%2B%2BwoGuQRQGbEoJTNKKG3U%2BT1wAGXpWyapNPUyLveKISL0i5Y8knBc%2BnYFcE2LCtOuTnucq%2FM%2BhJuJObXCUdctXtHH%2FZ23Yp1FnNZaeEPxOcXxNOh%2BGfldF7ivHFY46stoQRjNobnQn7hk6V2mrPh5evP&X-Amz-Signature=4843aae473d2fd884a4660a65a23f1212ad8f7857ddc8e3b965caf36caecbbf4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XEDSGXB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBdHoKHshoF9ScU8GMgX3W8d3FDJ0EYbEflM8v7MJnVSAiA3tJq4S0vvYqYmbg96L%2BDd9KteL%2FLPz%2Fv8dbT3YXEHIir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMEyTCQdvs54ShVvjjKtwDRiQ2lzA7F0nfSvB%2FGYbveIj9WfnQD99Ym%2Btj0yGCx2r97YnhJDhezCYJDuqH1%2BxdNki5wufD0rKq9qp%2FLExjTBPNVTm28nxwk%2B9qZDdc3QgemCaBlt7nMzCdBHq3qWZmjySSUrIamur4YkFamIGw5uoHPsnvB11r5FPAv2MvmZv%2FX2lhFIGlr%2BjTmBiyhJhu8NBuqEzcoiG4tfmi1zfE7XYWsjO%2B4GBEbtKbQWYyopdFEKnrMC6%2B5MSqIuEj7cA95jLbH0pSP5is%2B6%2BhEWQ2jayBmdVLiufDwaw86%2F0S%2F1rjFzdVWdynvY%2BZihC8u1h8X5F4gJXq5gtT1X8em6EE0kngXFE7BBjXZGIfTgm4%2B6jve9kb4Z4krIntprpv93C7KDQfxTAsRmTSpEx3V3G%2FspEBzSER0IFXponQk37Avq%2FX13aJsPElgusBJvwVVZn9yVsG%2Bo%2FjuAhj%2BSQcdRbEheH0yq6ARIE4LHeL27CYsIzO7Ogs2bkO9hwJ%2F647CQeuKjMHJg3UhpC5t5iTBiJLO36xEH%2FpVd09GvOLGLPtBMZ8qcuFDXTkh6uSSp0K3iZTAq%2BahOe2pHz6btv8JbLaybsj2t7ucxnYadFyfMvX5mYnep8QEWt9PvElVt8wnouYvQY6pgEom6PgrwZX1Tqt2lxnnXihADqRsd8piDamMrCm2yXtKoHkGGzekHBWTppN7kfrT%2FdOjrz8%2B%2BwoGuQRQGbEoJTNKKG3U%2BT1wAGXpWyapNPUyLveKISL0i5Y8knBc%2BnYFcE2LCtOuTnucq%2FM%2BhJuJObXCUdctXtHH%2FZ23Yp1FnNZaeEPxOcXxNOh%2BGfldF7ivHFY46stoQRjNobnQn7hk6V2mrPh5evP&X-Amz-Signature=2138b41b328d15103224cc1fbfbc1df71e47dbf9e29ab8ef5b3ba764b0163d95&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XEDSGXB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBdHoKHshoF9ScU8GMgX3W8d3FDJ0EYbEflM8v7MJnVSAiA3tJq4S0vvYqYmbg96L%2BDd9KteL%2FLPz%2Fv8dbT3YXEHIir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMEyTCQdvs54ShVvjjKtwDRiQ2lzA7F0nfSvB%2FGYbveIj9WfnQD99Ym%2Btj0yGCx2r97YnhJDhezCYJDuqH1%2BxdNki5wufD0rKq9qp%2FLExjTBPNVTm28nxwk%2B9qZDdc3QgemCaBlt7nMzCdBHq3qWZmjySSUrIamur4YkFamIGw5uoHPsnvB11r5FPAv2MvmZv%2FX2lhFIGlr%2BjTmBiyhJhu8NBuqEzcoiG4tfmi1zfE7XYWsjO%2B4GBEbtKbQWYyopdFEKnrMC6%2B5MSqIuEj7cA95jLbH0pSP5is%2B6%2BhEWQ2jayBmdVLiufDwaw86%2F0S%2F1rjFzdVWdynvY%2BZihC8u1h8X5F4gJXq5gtT1X8em6EE0kngXFE7BBjXZGIfTgm4%2B6jve9kb4Z4krIntprpv93C7KDQfxTAsRmTSpEx3V3G%2FspEBzSER0IFXponQk37Avq%2FX13aJsPElgusBJvwVVZn9yVsG%2Bo%2FjuAhj%2BSQcdRbEheH0yq6ARIE4LHeL27CYsIzO7Ogs2bkO9hwJ%2F647CQeuKjMHJg3UhpC5t5iTBiJLO36xEH%2FpVd09GvOLGLPtBMZ8qcuFDXTkh6uSSp0K3iZTAq%2BahOe2pHz6btv8JbLaybsj2t7ucxnYadFyfMvX5mYnep8QEWt9PvElVt8wnouYvQY6pgEom6PgrwZX1Tqt2lxnnXihADqRsd8piDamMrCm2yXtKoHkGGzekHBWTppN7kfrT%2FdOjrz8%2B%2BwoGuQRQGbEoJTNKKG3U%2BT1wAGXpWyapNPUyLveKISL0i5Y8knBc%2BnYFcE2LCtOuTnucq%2FM%2BhJuJObXCUdctXtHH%2FZ23Yp1FnNZaeEPxOcXxNOh%2BGfldF7ivHFY46stoQRjNobnQn7hk6V2mrPh5evP&X-Amz-Signature=4adc6591d01c9b8cfc7385b5518c28e1a77d6236c1ad1ae107199d8489c84551&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XEDSGXB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBdHoKHshoF9ScU8GMgX3W8d3FDJ0EYbEflM8v7MJnVSAiA3tJq4S0vvYqYmbg96L%2BDd9KteL%2FLPz%2Fv8dbT3YXEHIir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMEyTCQdvs54ShVvjjKtwDRiQ2lzA7F0nfSvB%2FGYbveIj9WfnQD99Ym%2Btj0yGCx2r97YnhJDhezCYJDuqH1%2BxdNki5wufD0rKq9qp%2FLExjTBPNVTm28nxwk%2B9qZDdc3QgemCaBlt7nMzCdBHq3qWZmjySSUrIamur4YkFamIGw5uoHPsnvB11r5FPAv2MvmZv%2FX2lhFIGlr%2BjTmBiyhJhu8NBuqEzcoiG4tfmi1zfE7XYWsjO%2B4GBEbtKbQWYyopdFEKnrMC6%2B5MSqIuEj7cA95jLbH0pSP5is%2B6%2BhEWQ2jayBmdVLiufDwaw86%2F0S%2F1rjFzdVWdynvY%2BZihC8u1h8X5F4gJXq5gtT1X8em6EE0kngXFE7BBjXZGIfTgm4%2B6jve9kb4Z4krIntprpv93C7KDQfxTAsRmTSpEx3V3G%2FspEBzSER0IFXponQk37Avq%2FX13aJsPElgusBJvwVVZn9yVsG%2Bo%2FjuAhj%2BSQcdRbEheH0yq6ARIE4LHeL27CYsIzO7Ogs2bkO9hwJ%2F647CQeuKjMHJg3UhpC5t5iTBiJLO36xEH%2FpVd09GvOLGLPtBMZ8qcuFDXTkh6uSSp0K3iZTAq%2BahOe2pHz6btv8JbLaybsj2t7ucxnYadFyfMvX5mYnep8QEWt9PvElVt8wnouYvQY6pgEom6PgrwZX1Tqt2lxnnXihADqRsd8piDamMrCm2yXtKoHkGGzekHBWTppN7kfrT%2FdOjrz8%2B%2BwoGuQRQGbEoJTNKKG3U%2BT1wAGXpWyapNPUyLveKISL0i5Y8knBc%2BnYFcE2LCtOuTnucq%2FM%2BhJuJObXCUdctXtHH%2FZ23Yp1FnNZaeEPxOcXxNOh%2BGfldF7ivHFY46stoQRjNobnQn7hk6V2mrPh5evP&X-Amz-Signature=a7cc1b5c5de13d1d50b86bbb9d82f97b858c6201de4d0ff0d98e3203ac9e8201&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XEDSGXB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBdHoKHshoF9ScU8GMgX3W8d3FDJ0EYbEflM8v7MJnVSAiA3tJq4S0vvYqYmbg96L%2BDd9KteL%2FLPz%2Fv8dbT3YXEHIir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMEyTCQdvs54ShVvjjKtwDRiQ2lzA7F0nfSvB%2FGYbveIj9WfnQD99Ym%2Btj0yGCx2r97YnhJDhezCYJDuqH1%2BxdNki5wufD0rKq9qp%2FLExjTBPNVTm28nxwk%2B9qZDdc3QgemCaBlt7nMzCdBHq3qWZmjySSUrIamur4YkFamIGw5uoHPsnvB11r5FPAv2MvmZv%2FX2lhFIGlr%2BjTmBiyhJhu8NBuqEzcoiG4tfmi1zfE7XYWsjO%2B4GBEbtKbQWYyopdFEKnrMC6%2B5MSqIuEj7cA95jLbH0pSP5is%2B6%2BhEWQ2jayBmdVLiufDwaw86%2F0S%2F1rjFzdVWdynvY%2BZihC8u1h8X5F4gJXq5gtT1X8em6EE0kngXFE7BBjXZGIfTgm4%2B6jve9kb4Z4krIntprpv93C7KDQfxTAsRmTSpEx3V3G%2FspEBzSER0IFXponQk37Avq%2FX13aJsPElgusBJvwVVZn9yVsG%2Bo%2FjuAhj%2BSQcdRbEheH0yq6ARIE4LHeL27CYsIzO7Ogs2bkO9hwJ%2F647CQeuKjMHJg3UhpC5t5iTBiJLO36xEH%2FpVd09GvOLGLPtBMZ8qcuFDXTkh6uSSp0K3iZTAq%2BahOe2pHz6btv8JbLaybsj2t7ucxnYadFyfMvX5mYnep8QEWt9PvElVt8wnouYvQY6pgEom6PgrwZX1Tqt2lxnnXihADqRsd8piDamMrCm2yXtKoHkGGzekHBWTppN7kfrT%2FdOjrz8%2B%2BwoGuQRQGbEoJTNKKG3U%2BT1wAGXpWyapNPUyLveKISL0i5Y8knBc%2BnYFcE2LCtOuTnucq%2FM%2BhJuJObXCUdctXtHH%2FZ23Yp1FnNZaeEPxOcXxNOh%2BGfldF7ivHFY46stoQRjNobnQn7hk6V2mrPh5evP&X-Amz-Signature=9a30d76751f8dd555751cb0e97c70840d6bea457090370fac339a58dc98877d1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XEDSGXB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBdHoKHshoF9ScU8GMgX3W8d3FDJ0EYbEflM8v7MJnVSAiA3tJq4S0vvYqYmbg96L%2BDd9KteL%2FLPz%2Fv8dbT3YXEHIir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMEyTCQdvs54ShVvjjKtwDRiQ2lzA7F0nfSvB%2FGYbveIj9WfnQD99Ym%2Btj0yGCx2r97YnhJDhezCYJDuqH1%2BxdNki5wufD0rKq9qp%2FLExjTBPNVTm28nxwk%2B9qZDdc3QgemCaBlt7nMzCdBHq3qWZmjySSUrIamur4YkFamIGw5uoHPsnvB11r5FPAv2MvmZv%2FX2lhFIGlr%2BjTmBiyhJhu8NBuqEzcoiG4tfmi1zfE7XYWsjO%2B4GBEbtKbQWYyopdFEKnrMC6%2B5MSqIuEj7cA95jLbH0pSP5is%2B6%2BhEWQ2jayBmdVLiufDwaw86%2F0S%2F1rjFzdVWdynvY%2BZihC8u1h8X5F4gJXq5gtT1X8em6EE0kngXFE7BBjXZGIfTgm4%2B6jve9kb4Z4krIntprpv93C7KDQfxTAsRmTSpEx3V3G%2FspEBzSER0IFXponQk37Avq%2FX13aJsPElgusBJvwVVZn9yVsG%2Bo%2FjuAhj%2BSQcdRbEheH0yq6ARIE4LHeL27CYsIzO7Ogs2bkO9hwJ%2F647CQeuKjMHJg3UhpC5t5iTBiJLO36xEH%2FpVd09GvOLGLPtBMZ8qcuFDXTkh6uSSp0K3iZTAq%2BahOe2pHz6btv8JbLaybsj2t7ucxnYadFyfMvX5mYnep8QEWt9PvElVt8wnouYvQY6pgEom6PgrwZX1Tqt2lxnnXihADqRsd8piDamMrCm2yXtKoHkGGzekHBWTppN7kfrT%2FdOjrz8%2B%2BwoGuQRQGbEoJTNKKG3U%2BT1wAGXpWyapNPUyLveKISL0i5Y8knBc%2BnYFcE2LCtOuTnucq%2FM%2BhJuJObXCUdctXtHH%2FZ23Yp1FnNZaeEPxOcXxNOh%2BGfldF7ivHFY46stoQRjNobnQn7hk6V2mrPh5evP&X-Amz-Signature=2e4788ef224064bea1ed5fa21ffa905e0aa9539a8ae82e40664b6c843a6ced22&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XEDSGXB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBdHoKHshoF9ScU8GMgX3W8d3FDJ0EYbEflM8v7MJnVSAiA3tJq4S0vvYqYmbg96L%2BDd9KteL%2FLPz%2Fv8dbT3YXEHIir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMEyTCQdvs54ShVvjjKtwDRiQ2lzA7F0nfSvB%2FGYbveIj9WfnQD99Ym%2Btj0yGCx2r97YnhJDhezCYJDuqH1%2BxdNki5wufD0rKq9qp%2FLExjTBPNVTm28nxwk%2B9qZDdc3QgemCaBlt7nMzCdBHq3qWZmjySSUrIamur4YkFamIGw5uoHPsnvB11r5FPAv2MvmZv%2FX2lhFIGlr%2BjTmBiyhJhu8NBuqEzcoiG4tfmi1zfE7XYWsjO%2B4GBEbtKbQWYyopdFEKnrMC6%2B5MSqIuEj7cA95jLbH0pSP5is%2B6%2BhEWQ2jayBmdVLiufDwaw86%2F0S%2F1rjFzdVWdynvY%2BZihC8u1h8X5F4gJXq5gtT1X8em6EE0kngXFE7BBjXZGIfTgm4%2B6jve9kb4Z4krIntprpv93C7KDQfxTAsRmTSpEx3V3G%2FspEBzSER0IFXponQk37Avq%2FX13aJsPElgusBJvwVVZn9yVsG%2Bo%2FjuAhj%2BSQcdRbEheH0yq6ARIE4LHeL27CYsIzO7Ogs2bkO9hwJ%2F647CQeuKjMHJg3UhpC5t5iTBiJLO36xEH%2FpVd09GvOLGLPtBMZ8qcuFDXTkh6uSSp0K3iZTAq%2BahOe2pHz6btv8JbLaybsj2t7ucxnYadFyfMvX5mYnep8QEWt9PvElVt8wnouYvQY6pgEom6PgrwZX1Tqt2lxnnXihADqRsd8piDamMrCm2yXtKoHkGGzekHBWTppN7kfrT%2FdOjrz8%2B%2BwoGuQRQGbEoJTNKKG3U%2BT1wAGXpWyapNPUyLveKISL0i5Y8knBc%2BnYFcE2LCtOuTnucq%2FM%2BhJuJObXCUdctXtHH%2FZ23Yp1FnNZaeEPxOcXxNOh%2BGfldF7ivHFY46stoQRjNobnQn7hk6V2mrPh5evP&X-Amz-Signature=a4a8d2ddca21db985f1a8789909fbf4f94bd6bb236b7ecbc52bf5ca2c5ccd54d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XEDSGXB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIBdHoKHshoF9ScU8GMgX3W8d3FDJ0EYbEflM8v7MJnVSAiA3tJq4S0vvYqYmbg96L%2BDd9KteL%2FLPz%2Fv8dbT3YXEHIir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMEyTCQdvs54ShVvjjKtwDRiQ2lzA7F0nfSvB%2FGYbveIj9WfnQD99Ym%2Btj0yGCx2r97YnhJDhezCYJDuqH1%2BxdNki5wufD0rKq9qp%2FLExjTBPNVTm28nxwk%2B9qZDdc3QgemCaBlt7nMzCdBHq3qWZmjySSUrIamur4YkFamIGw5uoHPsnvB11r5FPAv2MvmZv%2FX2lhFIGlr%2BjTmBiyhJhu8NBuqEzcoiG4tfmi1zfE7XYWsjO%2B4GBEbtKbQWYyopdFEKnrMC6%2B5MSqIuEj7cA95jLbH0pSP5is%2B6%2BhEWQ2jayBmdVLiufDwaw86%2F0S%2F1rjFzdVWdynvY%2BZihC8u1h8X5F4gJXq5gtT1X8em6EE0kngXFE7BBjXZGIfTgm4%2B6jve9kb4Z4krIntprpv93C7KDQfxTAsRmTSpEx3V3G%2FspEBzSER0IFXponQk37Avq%2FX13aJsPElgusBJvwVVZn9yVsG%2Bo%2FjuAhj%2BSQcdRbEheH0yq6ARIE4LHeL27CYsIzO7Ogs2bkO9hwJ%2F647CQeuKjMHJg3UhpC5t5iTBiJLO36xEH%2FpVd09GvOLGLPtBMZ8qcuFDXTkh6uSSp0K3iZTAq%2BahOe2pHz6btv8JbLaybsj2t7ucxnYadFyfMvX5mYnep8QEWt9PvElVt8wnouYvQY6pgEom6PgrwZX1Tqt2lxnnXihADqRsd8piDamMrCm2yXtKoHkGGzekHBWTppN7kfrT%2FdOjrz8%2B%2BwoGuQRQGbEoJTNKKG3U%2BT1wAGXpWyapNPUyLveKISL0i5Y8knBc%2BnYFcE2LCtOuTnucq%2FM%2BhJuJObXCUdctXtHH%2FZ23Yp1FnNZaeEPxOcXxNOh%2BGfldF7ivHFY46stoQRjNobnQn7hk6V2mrPh5evP&X-Amz-Signature=f09b77812fc45834d6518d825819560294e80b142af3047f82bddbeb95eb1ce0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXM4E5MN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIB9ygNbyu91Fq5MRIpXdvfUzXHiUVV%2Bnu%2BwmgkrNH%2F8YAiAhbncm45KDRZz6TnhU7%2FP8OlleYD64tudISlfodY7aGSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMgvQglgh%2Bz5QNBAz4KtwDE77%2Fqv8nC%2FBxTRVf%2B7Hn2%2F7v3HquaytbltSiRx0nU%2FPp8emt8p90fb2TNTcRDlHEmx%2BbBqHgp3aGRZUVIlWzW99qP5ZLUZ7t1T8d9mSytXITT9Y%2F03iZ4H20lLK3b%2B1j7JZPpBEDTDS6L%2BI9JR%2BNh216GgdgEhUy%2Fm7p1TQ6vj6WfCb%2BjSPnv1NO5XIEcbdjAN62gmy03eKL9E9X99UzG9KamFNCnFTNWczfpcsHkYSd2dIcmbl2yVD%2FRPlyuaFG99Rb%2FWnzp2Yj0Xpw3izoLvJtwppFs%2F%2B7IjHRhwgW%2Ff1tJaYTSkXa5TCgDdeL3sbvf1QycNXKlXHVtGV0rAiLRl4ioGUy4v4xdDEAQjdAm2RY9iiM3MKUaZ1jtytFODT27tRdsyvT6o57jkLkyewAnTgXDgyWPjhBThZBpMYs%2BE%2BYvbZYD3N171ehg5dikCQ%2Fnnm8fFaWKtW6uovQc%2FHGvMa%2FAJmdiy3do1SoZmNhK1F%2F%2F8BAiAe9aECUst2A8tmHfeTswUtKpK7Ch%2BUEWdR2sGrk%2Fbd32iU4IhEn218fO5%2FSocF1iKh0OyFedetNiPQBGl%2FQ1vMvFms3rukH6CAF5HxyGExNOrmCRUo8Dudarh2bK50VoRN1WP4deigwsIuYvQY6pgFLGxkMB1sC0Iq3FyZrqPariS3Y5WXv4I8CMlefYibf3AnYlvc3CxpcOlTFFPMBXqx9VFRcDypD1GfNZkTC2qBkDoaAV9fodP7g0ejDpCbnAo19Jwg%2F0kgih0Q5RbtPXWLyXuXDpkUS6Q%2BQgScSGElZChVfqGIp6FYwo%2F4zGJeNbWPuE2wWvXpg4DRTNJEMCQAyG5BkDclNQ2h3eEa9FqlpwW6zywDZ&X-Amz-Signature=50190368e455dda17d0abcd058fc0f99575726cb86c6661566ac2c808ebad7a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T6YKPG6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCrHpJHQTGgeYERLQra6klTnjRLTxjpXOoRes8Fjf6vigIgXZPWxcup%2FjZjMHUDu1yNnCK8kmfnwJ9UaghKG4tuSewq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDKdPdrxq%2BXlI4k%2BKfCrcA46rpkSzFs1%2FE%2FhDzsIT9PfBGpT5I74U7XMeB0AbmCDUPmRCy5wpJki1qCNqqh3%2BweqSuflvtrT3VuN46tJZbaeMQXNUEH6LJG%2BfGY%2FEq%2FYhluzWvy8SQ%2FCgJNFRFWs2OSC72f22jypn8qyYdLzFSY2jLs1lC31wmcfMJcPHZCnTRcGRwoW1vk3pYJm7ij5%2BnwvAzD5rLgYXRXmYSck9D06owjsAIYAALgRqhn4DOzvZhUqTQFSROdSU6FVR74K9MVhwH%2BCVmV3nmeq%2F0anIlQqfuN9KF%2BEgBM1nsBmxK%2BebDT4SZbIco06ghisGtQs7G1WED7fworUNjbmzLG9yAhjW7J6%2Fk8bS3D1SPb5IuXQavdtJ4OVv4vL8%2FhBCJu8mEyZtwZjV1NrR6KDoGwvNMYS5T01Zyqi2RgaC8ZcrRDRpqJRJAZB4a3EW4oW326offckEgNEuUOWk9tdk1NK0myhvxAIWZds961rPYh94lfpW62SkUkFP2LDBaX6YxupIdSbJ7F%2BJoCfCWFG3%2F3f8vtz9%2BJxjSnYXKaQjnIgQ44%2BJ5RupZ%2B2E2W%2FTktR%2BNSXmPR53oh8KqC90ZvbfeSOyjdhgIeZ%2BEMy%2BxuqhEJYkwfvDCvGWMrUmIZNRSQcaMIeLmL0GOqUBD07tUIrHGsHVcITKj0JRj2SEYJraiJ0HPbiPHdXM%2BRJ2l1HywL992e%2BJdt8bJYCLgBRhcUnbYFOF8bhmV%2FDyJoOHKmQWH%2B9vCIpBJtqYPi3ie3imhQqiWoLfLITORi%2FbQgX0b22JOGodyD4VOKevF0pkbi6fo1v0DOGEGprp6NJ2F9U3jFfZHEnRCFRmqbjhUDuq5f0uw%2FKq3XuDtf9gDwQylljL&X-Amz-Signature=7e57b1029dc18a56781b9733465443a238db2a8a7643facbea9368f66fd0e0dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642OOMVDE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEVmB4t3XJU9vqXLPRS4RKyDjcGk7Jqj4hwAecfVTztHAiA3gcDrDDDkGv4u4gn0D9E%2B98DlodL7G2MdzJR8S3Z73ir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIM2X0svYE5Z0PRx3VGKtwDv9OM32OQLWT5wVTeUWYC5Cv3dl8xdvfoaK%2BpdrroL448HrNjbPPmw0omyLGZmZQ5oI79u9wxXN%2Bo9q9JtX%2B%2BAFwlsSkLH4%2BLwblgwAT2o0O%2FfhkquxQa0lHGF3K4Si6nfurPERhq5rKCeoOn3aEJYW%2Fbf1cB3nDI8TCFET0ZTGWqtUW9ymrs5GdCEDeka3hGty6gfgM4buKfUdr84y2L6T911wpDHKaiwEhkLEjfz3uiq0TWYR4u8%2Fmdp2FGmbIXmHzJ60sNQwqbKQgs7mgTyZYIh40rEmEc5TPpeG%2FisqwCddCRKq4z1HJcJFr%2FX4f9%2F%2BVtqUYoPXI%2FeNDntoA2QhVowbV54lWv0R8nRcSvjBp9DIS5xgBrEQ%2FR4do1FqXi%2Bl8xQLJ4jYTukcrgy8Y5chjdrzXs68avlAugihQZMGWOiimdGzRf6o7p1Yvukp5gcxgyoSOWVM%2Bzn9TYgA9uPKJ7NbtRjMJK9oyMJEq6XntbscihkV8%2BYLeSLEIhGVt6f72mp%2FzXTMsdqJvZGhA7xJRbeyZ2%2FxBrdKhM2qLfkADYP3LmeF7WGR2JdPRr07%2FA3Lb%2FeJHJuRyMMOUJxFTP%2F7Tmgy%2FFQvPg7S%2FpMcHTI4s6Ek9fPujWFV2fCI0wlIuYvQY6pgGxoKb7CHEY1r00NntkpUKlmtkeOtAz8QJ%2FceD0PKJfmAn4KEow7KweN%2FWyDSg%2FH6J62sR%2BO5ILoaZGfbO6PQHgDu5KqLroZ9iF7pt9GlYUmqDc7nbfwy12IP32TIzMCz0YrUK5OQF2VpqHA%2BWpbaoxIckwT2Mi51v%2BFzyXKXCiHgUJyJx3eZi0fxkYQRosafzT0ptbtHhf8LVr%2BR0de0tNdWSrURXk&X-Amz-Signature=4bf2aac1d93f7471fc3c601e2c93dd566b96c7b70fab8e48b22b583b057f3e4a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642OOMVDE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEVmB4t3XJU9vqXLPRS4RKyDjcGk7Jqj4hwAecfVTztHAiA3gcDrDDDkGv4u4gn0D9E%2B98DlodL7G2MdzJR8S3Z73ir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIM2X0svYE5Z0PRx3VGKtwDv9OM32OQLWT5wVTeUWYC5Cv3dl8xdvfoaK%2BpdrroL448HrNjbPPmw0omyLGZmZQ5oI79u9wxXN%2Bo9q9JtX%2B%2BAFwlsSkLH4%2BLwblgwAT2o0O%2FfhkquxQa0lHGF3K4Si6nfurPERhq5rKCeoOn3aEJYW%2Fbf1cB3nDI8TCFET0ZTGWqtUW9ymrs5GdCEDeka3hGty6gfgM4buKfUdr84y2L6T911wpDHKaiwEhkLEjfz3uiq0TWYR4u8%2Fmdp2FGmbIXmHzJ60sNQwqbKQgs7mgTyZYIh40rEmEc5TPpeG%2FisqwCddCRKq4z1HJcJFr%2FX4f9%2F%2BVtqUYoPXI%2FeNDntoA2QhVowbV54lWv0R8nRcSvjBp9DIS5xgBrEQ%2FR4do1FqXi%2Bl8xQLJ4jYTukcrgy8Y5chjdrzXs68avlAugihQZMGWOiimdGzRf6o7p1Yvukp5gcxgyoSOWVM%2Bzn9TYgA9uPKJ7NbtRjMJK9oyMJEq6XntbscihkV8%2BYLeSLEIhGVt6f72mp%2FzXTMsdqJvZGhA7xJRbeyZ2%2FxBrdKhM2qLfkADYP3LmeF7WGR2JdPRr07%2FA3Lb%2FeJHJuRyMMOUJxFTP%2F7Tmgy%2FFQvPg7S%2FpMcHTI4s6Ek9fPujWFV2fCI0wlIuYvQY6pgGxoKb7CHEY1r00NntkpUKlmtkeOtAz8QJ%2FceD0PKJfmAn4KEow7KweN%2FWyDSg%2FH6J62sR%2BO5ILoaZGfbO6PQHgDu5KqLroZ9iF7pt9GlYUmqDc7nbfwy12IP32TIzMCz0YrUK5OQF2VpqHA%2BWpbaoxIckwT2Mi51v%2BFzyXKXCiHgUJyJx3eZi0fxkYQRosafzT0ptbtHhf8LVr%2BR0de0tNdWSrURXk&X-Amz-Signature=a192c4342408189dd84411ba8a7bfff464193b866b7980ef93117f48005d68ff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
