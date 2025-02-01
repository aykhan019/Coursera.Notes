

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHMLIOYJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEo2Pmm%2Bf9gVwt%2FOOjdxf6NXNBRoDk07NA8Ufg4%2B6%2BYnAiEAg8%2BwXzD4Wth%2FqmDTRVYtoeX%2B%2FPgeM3mAjJydJTzfXwIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJaB3CwNRYE1PQtiBCrcA7kSOiPAN%2FRyA%2BmXjv4rrOmK%2BpECMtrmIgHo1bw8L%2Fa2y2t60N8q9wsUELgwCFo11J1P3VQ5wsFuD2RKx%2FC9RSrB0nRHkSdGMFW%2BBuZh1zwVK0lefJqyOW6YveU0O9PK8B4O9hA%2B5ISP2ndgFbaHMXPAuXeXnXBIE3F%2FeIB7VZDSVhWZ4OmafZ2src76GXF7OaTDkCfsIS%2BBRq67QSw9ouBxhB6n7sZd6YBphgVK%2BF1WulAfFv5ja%2FI5u1XKrxUInEeLX5o7mf%2FI0K7Osdb26RMBDiyY%2FMcECmTETppeiZtCMIs%2B%2Ff3ZGbBnWMEwzi8WvhgVK5dgW%2BPWXH40itme7LRwq40VFIfvpmKMqdKuqfUk8y15q5WNRYmZZFOm%2FLrX4WotDlfBXtN6csE3lAFKmjKVPgS9ddsLTISecz7%2F1qrqpATYF1RaQI1GWfoAGVWD0V5iBPrBvPavGvRYbkXIFARp8GdvYVWObjTznlnf6SVhJa6uZdihGgIEQUhlEoYum%2FwsIn79z8qOEuYfnoll8mInj710%2Fwr1thema2hVFa5U8JW%2FwzhwljeoZBAtJf8N9kPLafJGVPQndeFwozIq%2FN8BpkoYLPEKvjMZHIN%2Fe50nQlJ1ruwlYD%2BRA4pbMMik97wGOqUB12gBSMSgcULnq2EU1UtubSyQ64XVcndShU632LIa437XZY2ZiO0MDeqgAwii8AgSUmn1R5f%2FOopLc6vQajKNwjGAP7hFhfssbC1qqjfRGlmsyAHmc%2BaWqRhRIcPU1XquD2DOwpc3zL69x%2BDUf7HVHrMU1g1oGgAR1rbRUnY%2Bys1L0GMX75yvwtggeFHoSmLOIVVJCpuYGN0lV9dRQQJAf7jtzrvv&X-Amz-Signature=b21f4b8c676f51aae8b25e2f22612003a2269417cc973217958a3a25362bf516&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHMLIOYJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEo2Pmm%2Bf9gVwt%2FOOjdxf6NXNBRoDk07NA8Ufg4%2B6%2BYnAiEAg8%2BwXzD4Wth%2FqmDTRVYtoeX%2B%2FPgeM3mAjJydJTzfXwIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJaB3CwNRYE1PQtiBCrcA7kSOiPAN%2FRyA%2BmXjv4rrOmK%2BpECMtrmIgHo1bw8L%2Fa2y2t60N8q9wsUELgwCFo11J1P3VQ5wsFuD2RKx%2FC9RSrB0nRHkSdGMFW%2BBuZh1zwVK0lefJqyOW6YveU0O9PK8B4O9hA%2B5ISP2ndgFbaHMXPAuXeXnXBIE3F%2FeIB7VZDSVhWZ4OmafZ2src76GXF7OaTDkCfsIS%2BBRq67QSw9ouBxhB6n7sZd6YBphgVK%2BF1WulAfFv5ja%2FI5u1XKrxUInEeLX5o7mf%2FI0K7Osdb26RMBDiyY%2FMcECmTETppeiZtCMIs%2B%2Ff3ZGbBnWMEwzi8WvhgVK5dgW%2BPWXH40itme7LRwq40VFIfvpmKMqdKuqfUk8y15q5WNRYmZZFOm%2FLrX4WotDlfBXtN6csE3lAFKmjKVPgS9ddsLTISecz7%2F1qrqpATYF1RaQI1GWfoAGVWD0V5iBPrBvPavGvRYbkXIFARp8GdvYVWObjTznlnf6SVhJa6uZdihGgIEQUhlEoYum%2FwsIn79z8qOEuYfnoll8mInj710%2Fwr1thema2hVFa5U8JW%2FwzhwljeoZBAtJf8N9kPLafJGVPQndeFwozIq%2FN8BpkoYLPEKvjMZHIN%2Fe50nQlJ1ruwlYD%2BRA4pbMMik97wGOqUB12gBSMSgcULnq2EU1UtubSyQ64XVcndShU632LIa437XZY2ZiO0MDeqgAwii8AgSUmn1R5f%2FOopLc6vQajKNwjGAP7hFhfssbC1qqjfRGlmsyAHmc%2BaWqRhRIcPU1XquD2DOwpc3zL69x%2BDUf7HVHrMU1g1oGgAR1rbRUnY%2Bys1L0GMX75yvwtggeFHoSmLOIVVJCpuYGN0lV9dRQQJAf7jtzrvv&X-Amz-Signature=369fb39cec5a3843587d53248199af017cd6a9f1c7ca3f697a71f3049da1c165&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHMLIOYJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEo2Pmm%2Bf9gVwt%2FOOjdxf6NXNBRoDk07NA8Ufg4%2B6%2BYnAiEAg8%2BwXzD4Wth%2FqmDTRVYtoeX%2B%2FPgeM3mAjJydJTzfXwIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJaB3CwNRYE1PQtiBCrcA7kSOiPAN%2FRyA%2BmXjv4rrOmK%2BpECMtrmIgHo1bw8L%2Fa2y2t60N8q9wsUELgwCFo11J1P3VQ5wsFuD2RKx%2FC9RSrB0nRHkSdGMFW%2BBuZh1zwVK0lefJqyOW6YveU0O9PK8B4O9hA%2B5ISP2ndgFbaHMXPAuXeXnXBIE3F%2FeIB7VZDSVhWZ4OmafZ2src76GXF7OaTDkCfsIS%2BBRq67QSw9ouBxhB6n7sZd6YBphgVK%2BF1WulAfFv5ja%2FI5u1XKrxUInEeLX5o7mf%2FI0K7Osdb26RMBDiyY%2FMcECmTETppeiZtCMIs%2B%2Ff3ZGbBnWMEwzi8WvhgVK5dgW%2BPWXH40itme7LRwq40VFIfvpmKMqdKuqfUk8y15q5WNRYmZZFOm%2FLrX4WotDlfBXtN6csE3lAFKmjKVPgS9ddsLTISecz7%2F1qrqpATYF1RaQI1GWfoAGVWD0V5iBPrBvPavGvRYbkXIFARp8GdvYVWObjTznlnf6SVhJa6uZdihGgIEQUhlEoYum%2FwsIn79z8qOEuYfnoll8mInj710%2Fwr1thema2hVFa5U8JW%2FwzhwljeoZBAtJf8N9kPLafJGVPQndeFwozIq%2FN8BpkoYLPEKvjMZHIN%2Fe50nQlJ1ruwlYD%2BRA4pbMMik97wGOqUB12gBSMSgcULnq2EU1UtubSyQ64XVcndShU632LIa437XZY2ZiO0MDeqgAwii8AgSUmn1R5f%2FOopLc6vQajKNwjGAP7hFhfssbC1qqjfRGlmsyAHmc%2BaWqRhRIcPU1XquD2DOwpc3zL69x%2BDUf7HVHrMU1g1oGgAR1rbRUnY%2Bys1L0GMX75yvwtggeFHoSmLOIVVJCpuYGN0lV9dRQQJAf7jtzrvv&X-Amz-Signature=af34f187dc865c5cf959f57451844d489d3a25fb5c65cb03b7b647f6544d786d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHMLIOYJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEo2Pmm%2Bf9gVwt%2FOOjdxf6NXNBRoDk07NA8Ufg4%2B6%2BYnAiEAg8%2BwXzD4Wth%2FqmDTRVYtoeX%2B%2FPgeM3mAjJydJTzfXwIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJaB3CwNRYE1PQtiBCrcA7kSOiPAN%2FRyA%2BmXjv4rrOmK%2BpECMtrmIgHo1bw8L%2Fa2y2t60N8q9wsUELgwCFo11J1P3VQ5wsFuD2RKx%2FC9RSrB0nRHkSdGMFW%2BBuZh1zwVK0lefJqyOW6YveU0O9PK8B4O9hA%2B5ISP2ndgFbaHMXPAuXeXnXBIE3F%2FeIB7VZDSVhWZ4OmafZ2src76GXF7OaTDkCfsIS%2BBRq67QSw9ouBxhB6n7sZd6YBphgVK%2BF1WulAfFv5ja%2FI5u1XKrxUInEeLX5o7mf%2FI0K7Osdb26RMBDiyY%2FMcECmTETppeiZtCMIs%2B%2Ff3ZGbBnWMEwzi8WvhgVK5dgW%2BPWXH40itme7LRwq40VFIfvpmKMqdKuqfUk8y15q5WNRYmZZFOm%2FLrX4WotDlfBXtN6csE3lAFKmjKVPgS9ddsLTISecz7%2F1qrqpATYF1RaQI1GWfoAGVWD0V5iBPrBvPavGvRYbkXIFARp8GdvYVWObjTznlnf6SVhJa6uZdihGgIEQUhlEoYum%2FwsIn79z8qOEuYfnoll8mInj710%2Fwr1thema2hVFa5U8JW%2FwzhwljeoZBAtJf8N9kPLafJGVPQndeFwozIq%2FN8BpkoYLPEKvjMZHIN%2Fe50nQlJ1ruwlYD%2BRA4pbMMik97wGOqUB12gBSMSgcULnq2EU1UtubSyQ64XVcndShU632LIa437XZY2ZiO0MDeqgAwii8AgSUmn1R5f%2FOopLc6vQajKNwjGAP7hFhfssbC1qqjfRGlmsyAHmc%2BaWqRhRIcPU1XquD2DOwpc3zL69x%2BDUf7HVHrMU1g1oGgAR1rbRUnY%2Bys1L0GMX75yvwtggeFHoSmLOIVVJCpuYGN0lV9dRQQJAf7jtzrvv&X-Amz-Signature=d7d6cf4ad36c9736d099c79c16a6c4ed4923a2b6609ac0bca48b8743502604ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHMLIOYJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEo2Pmm%2Bf9gVwt%2FOOjdxf6NXNBRoDk07NA8Ufg4%2B6%2BYnAiEAg8%2BwXzD4Wth%2FqmDTRVYtoeX%2B%2FPgeM3mAjJydJTzfXwIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJaB3CwNRYE1PQtiBCrcA7kSOiPAN%2FRyA%2BmXjv4rrOmK%2BpECMtrmIgHo1bw8L%2Fa2y2t60N8q9wsUELgwCFo11J1P3VQ5wsFuD2RKx%2FC9RSrB0nRHkSdGMFW%2BBuZh1zwVK0lefJqyOW6YveU0O9PK8B4O9hA%2B5ISP2ndgFbaHMXPAuXeXnXBIE3F%2FeIB7VZDSVhWZ4OmafZ2src76GXF7OaTDkCfsIS%2BBRq67QSw9ouBxhB6n7sZd6YBphgVK%2BF1WulAfFv5ja%2FI5u1XKrxUInEeLX5o7mf%2FI0K7Osdb26RMBDiyY%2FMcECmTETppeiZtCMIs%2B%2Ff3ZGbBnWMEwzi8WvhgVK5dgW%2BPWXH40itme7LRwq40VFIfvpmKMqdKuqfUk8y15q5WNRYmZZFOm%2FLrX4WotDlfBXtN6csE3lAFKmjKVPgS9ddsLTISecz7%2F1qrqpATYF1RaQI1GWfoAGVWD0V5iBPrBvPavGvRYbkXIFARp8GdvYVWObjTznlnf6SVhJa6uZdihGgIEQUhlEoYum%2FwsIn79z8qOEuYfnoll8mInj710%2Fwr1thema2hVFa5U8JW%2FwzhwljeoZBAtJf8N9kPLafJGVPQndeFwozIq%2FN8BpkoYLPEKvjMZHIN%2Fe50nQlJ1ruwlYD%2BRA4pbMMik97wGOqUB12gBSMSgcULnq2EU1UtubSyQ64XVcndShU632LIa437XZY2ZiO0MDeqgAwii8AgSUmn1R5f%2FOopLc6vQajKNwjGAP7hFhfssbC1qqjfRGlmsyAHmc%2BaWqRhRIcPU1XquD2DOwpc3zL69x%2BDUf7HVHrMU1g1oGgAR1rbRUnY%2Bys1L0GMX75yvwtggeFHoSmLOIVVJCpuYGN0lV9dRQQJAf7jtzrvv&X-Amz-Signature=634d853cd10e196978e0fec6e420dc81e2acfc8e548f98c092f3c1cc084911b3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHMLIOYJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEo2Pmm%2Bf9gVwt%2FOOjdxf6NXNBRoDk07NA8Ufg4%2B6%2BYnAiEAg8%2BwXzD4Wth%2FqmDTRVYtoeX%2B%2FPgeM3mAjJydJTzfXwIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJaB3CwNRYE1PQtiBCrcA7kSOiPAN%2FRyA%2BmXjv4rrOmK%2BpECMtrmIgHo1bw8L%2Fa2y2t60N8q9wsUELgwCFo11J1P3VQ5wsFuD2RKx%2FC9RSrB0nRHkSdGMFW%2BBuZh1zwVK0lefJqyOW6YveU0O9PK8B4O9hA%2B5ISP2ndgFbaHMXPAuXeXnXBIE3F%2FeIB7VZDSVhWZ4OmafZ2src76GXF7OaTDkCfsIS%2BBRq67QSw9ouBxhB6n7sZd6YBphgVK%2BF1WulAfFv5ja%2FI5u1XKrxUInEeLX5o7mf%2FI0K7Osdb26RMBDiyY%2FMcECmTETppeiZtCMIs%2B%2Ff3ZGbBnWMEwzi8WvhgVK5dgW%2BPWXH40itme7LRwq40VFIfvpmKMqdKuqfUk8y15q5WNRYmZZFOm%2FLrX4WotDlfBXtN6csE3lAFKmjKVPgS9ddsLTISecz7%2F1qrqpATYF1RaQI1GWfoAGVWD0V5iBPrBvPavGvRYbkXIFARp8GdvYVWObjTznlnf6SVhJa6uZdihGgIEQUhlEoYum%2FwsIn79z8qOEuYfnoll8mInj710%2Fwr1thema2hVFa5U8JW%2FwzhwljeoZBAtJf8N9kPLafJGVPQndeFwozIq%2FN8BpkoYLPEKvjMZHIN%2Fe50nQlJ1ruwlYD%2BRA4pbMMik97wGOqUB12gBSMSgcULnq2EU1UtubSyQ64XVcndShU632LIa437XZY2ZiO0MDeqgAwii8AgSUmn1R5f%2FOopLc6vQajKNwjGAP7hFhfssbC1qqjfRGlmsyAHmc%2BaWqRhRIcPU1XquD2DOwpc3zL69x%2BDUf7HVHrMU1g1oGgAR1rbRUnY%2Bys1L0GMX75yvwtggeFHoSmLOIVVJCpuYGN0lV9dRQQJAf7jtzrvv&X-Amz-Signature=5ad3073833a463ae42ed08ddf0839e44e9ecc176829a00aa2783eda3a66231c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHMLIOYJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEo2Pmm%2Bf9gVwt%2FOOjdxf6NXNBRoDk07NA8Ufg4%2B6%2BYnAiEAg8%2BwXzD4Wth%2FqmDTRVYtoeX%2B%2FPgeM3mAjJydJTzfXwIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJaB3CwNRYE1PQtiBCrcA7kSOiPAN%2FRyA%2BmXjv4rrOmK%2BpECMtrmIgHo1bw8L%2Fa2y2t60N8q9wsUELgwCFo11J1P3VQ5wsFuD2RKx%2FC9RSrB0nRHkSdGMFW%2BBuZh1zwVK0lefJqyOW6YveU0O9PK8B4O9hA%2B5ISP2ndgFbaHMXPAuXeXnXBIE3F%2FeIB7VZDSVhWZ4OmafZ2src76GXF7OaTDkCfsIS%2BBRq67QSw9ouBxhB6n7sZd6YBphgVK%2BF1WulAfFv5ja%2FI5u1XKrxUInEeLX5o7mf%2FI0K7Osdb26RMBDiyY%2FMcECmTETppeiZtCMIs%2B%2Ff3ZGbBnWMEwzi8WvhgVK5dgW%2BPWXH40itme7LRwq40VFIfvpmKMqdKuqfUk8y15q5WNRYmZZFOm%2FLrX4WotDlfBXtN6csE3lAFKmjKVPgS9ddsLTISecz7%2F1qrqpATYF1RaQI1GWfoAGVWD0V5iBPrBvPavGvRYbkXIFARp8GdvYVWObjTznlnf6SVhJa6uZdihGgIEQUhlEoYum%2FwsIn79z8qOEuYfnoll8mInj710%2Fwr1thema2hVFa5U8JW%2FwzhwljeoZBAtJf8N9kPLafJGVPQndeFwozIq%2FN8BpkoYLPEKvjMZHIN%2Fe50nQlJ1ruwlYD%2BRA4pbMMik97wGOqUB12gBSMSgcULnq2EU1UtubSyQ64XVcndShU632LIa437XZY2ZiO0MDeqgAwii8AgSUmn1R5f%2FOopLc6vQajKNwjGAP7hFhfssbC1qqjfRGlmsyAHmc%2BaWqRhRIcPU1XquD2DOwpc3zL69x%2BDUf7HVHrMU1g1oGgAR1rbRUnY%2Bys1L0GMX75yvwtggeFHoSmLOIVVJCpuYGN0lV9dRQQJAf7jtzrvv&X-Amz-Signature=d785e47293d0a2df69ff653f8b2e1e010f26f3cb43529cf32283d52f198d7d10&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHMLIOYJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEo2Pmm%2Bf9gVwt%2FOOjdxf6NXNBRoDk07NA8Ufg4%2B6%2BYnAiEAg8%2BwXzD4Wth%2FqmDTRVYtoeX%2B%2FPgeM3mAjJydJTzfXwIqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJaB3CwNRYE1PQtiBCrcA7kSOiPAN%2FRyA%2BmXjv4rrOmK%2BpECMtrmIgHo1bw8L%2Fa2y2t60N8q9wsUELgwCFo11J1P3VQ5wsFuD2RKx%2FC9RSrB0nRHkSdGMFW%2BBuZh1zwVK0lefJqyOW6YveU0O9PK8B4O9hA%2B5ISP2ndgFbaHMXPAuXeXnXBIE3F%2FeIB7VZDSVhWZ4OmafZ2src76GXF7OaTDkCfsIS%2BBRq67QSw9ouBxhB6n7sZd6YBphgVK%2BF1WulAfFv5ja%2FI5u1XKrxUInEeLX5o7mf%2FI0K7Osdb26RMBDiyY%2FMcECmTETppeiZtCMIs%2B%2Ff3ZGbBnWMEwzi8WvhgVK5dgW%2BPWXH40itme7LRwq40VFIfvpmKMqdKuqfUk8y15q5WNRYmZZFOm%2FLrX4WotDlfBXtN6csE3lAFKmjKVPgS9ddsLTISecz7%2F1qrqpATYF1RaQI1GWfoAGVWD0V5iBPrBvPavGvRYbkXIFARp8GdvYVWObjTznlnf6SVhJa6uZdihGgIEQUhlEoYum%2FwsIn79z8qOEuYfnoll8mInj710%2Fwr1thema2hVFa5U8JW%2FwzhwljeoZBAtJf8N9kPLafJGVPQndeFwozIq%2FN8BpkoYLPEKvjMZHIN%2Fe50nQlJ1ruwlYD%2BRA4pbMMik97wGOqUB12gBSMSgcULnq2EU1UtubSyQ64XVcndShU632LIa437XZY2ZiO0MDeqgAwii8AgSUmn1R5f%2FOopLc6vQajKNwjGAP7hFhfssbC1qqjfRGlmsyAHmc%2BaWqRhRIcPU1XquD2DOwpc3zL69x%2BDUf7HVHrMU1g1oGgAR1rbRUnY%2Bys1L0GMX75yvwtggeFHoSmLOIVVJCpuYGN0lV9dRQQJAf7jtzrvv&X-Amz-Signature=3d8db1aae7924553e2e7747570ed151e5b81040fcbeab72b3c82bf463531d595&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TEKTNPU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgG9s79hojCMlf%2BNUX4O%2FhngkPE1wEgB9MoC9sZCQtdgIgDRwmvaPGYQAhcJdrLFy0Gfd8SQr7cX4NSWZSBeqrP8wqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL72GR3QRUhdSD3AzyrcA4F8W33k70AylZfI6SKVx1Oc9nmU0TX7Y%2FonUF14JIn18NP7VhYi6xrxrBJwAfQqOkRpa2CDmSXkemGc4XJPJZgIjNpwe6KirLJ1%2FPYI34wO3ibFiCKSADbQG3ndHIzMVkH7teuWzyr5xt%2BBMY0XHgWhNPpVH3kD9hJuyH0NTm0VOBE%2FUHY1mgVEzCeIDju8Ufh9cCsn%2FoE9oMny%2BqUSKFSbiReAgNXhUD2i3tQdAzE4Jd7l62jghLTzv6QIXwf9mD6NJzcO91ni7mZaSLd2IhmXvGu6Qx8vNBmLHo5BtD2w4lr62MJj1mXenIzL7gWo0gOF0QO0vrf5KpN3Lxc%2FhvbnFGh7W86AnA6CSuEWICISOGssCUEkwv74MXmxzwjmIFcsLBaL7%2FfkwqNVtZEq1JTEV8274%2FS1IPmXi1epLZ24xsk2gWJk40Mhy8plVWhTK5ISY11lkstOL1rhOPl5VIXZKxPqtAOuGgud%2FAUylwZ7ysRY2%2FrIsUUfUtrkXk4BUhjxf8UQtWeXUFoiVzMip9pVep5GS43etgEnBXRwy1W1L5RF87vka0RvFIvHjxcCqLydXDKHgWehvcfAcViEmhU%2FWbCtmfT9gqbbhSggxKRyHD44FIMAZZqtD%2Bw7MKOk97wGOqUBC7CbUdj1e8ekHgwmARygOuAVQBjJdsY1dntqqg3CH9v%2BMxG1vPavQUm3rhHUgZeFZBmaKuIzrUCrbvZkrBGvn1vD6ELOtPkEZqCxPbXEOFGqZc7NNcAsi90N3Z305ACkdBeBsRSMXO1ICRBmB4yHN61leTJY%2BShA8LvC73h3J8CDza5tAVDM9qMgj0q0q4r3oEebfJMj4FQcJ%2BahGHtDZ5Ayokc9&X-Amz-Signature=7af4b30cccb99227589e37b3e8aed21b66821dbe0a3f4ddb7ddb8031e224d977&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YV3VOOM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBIju33PAD69rTqxQvMl75aiVV9M2b5sWsDduviQOsZXAiEArWzIksxaeSQ%2Fwj0QiNvtVM3ii7r2%2B67vUdueaEJSk5cqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDplp2vq5Tv1KolijyrcAxcQauBpIK66pFALLth87XHoqIFJmKz%2FOQYhJrYigOf7pt%2FJyDnOJ1co2P7q3ErOtOPczOOi3e5E9COt%2Fg7VRXyxU3frRXuw3uUFG5GbEmv7xRzhmxmKsCR4JvbaVA6lDA%2Fpn53dgWCwWhKkAVukE7JTIwNCRJiaC%2F1Uvkd9eZKWE5W3k9OFxeAHvA2NLmb5%2BWuUM3wlv5ZZpCK8cJlEA9jgQHvP5RSFrYe0REFwdnJxlTnNqITu842IQel7hXJFBG3dDOtfb2NG10yAFF%2BL%2FYjOXjF0NBN51VJ2Q1U%2FyjIgb4pk8K2EqFwrPBbTrdVnOcoNsJ%2BfO%2BN4c8KXcw403gsUI881yBpjTyj4QO3%2B06sHi8j3mty4kp6RIEviqfcqqfysPeUXEQwsmAkeV8ru7ZiHwiizyC%2By89nQlKOFD6OiEY5eox%2FpxP6Ld5KLDsLceyHtOiPpRp8gEHq4o3VMRpODQt3RcOK4UaYRkkFqpzs6Z92TFKgXTtEFu%2F71AfKa%2Fs5PRyYvguofdvbLkNB8POpqS9xpdf3zsfIZI7cSdIRQNUiADctniBJrOy8qlODhigBZMcRXADNh0khnbshGaffsU62zWKtKrxVdlz%2FL56hAyyq2jlgwbfoQQ%2FTAMPmk97wGOqUB%2F0R3QGujWM9nF2B9r2gJCGAtFMs2hcVax8f%2FANEK7I906a3H5nwqjemlbm8CgiPrSXJ5V6W0yji1ypvYdehPJFU7WE%2Fp2RQ6jaN4gJckFJziEMEnaY5vDOtGNyxuD9JS%2FpGpy555g%2FLL%2F4EKdA2pCs60zk%2BrIHvZszM65VeAG1h9AnW709JS%2FI2HJ89GGLDcxFWiv6hMRGgirjBKhrox7PmzjyaI&X-Amz-Signature=3377b157bd25046199e31a827775e2f0d2e99ae6a3a9b32b430947ea5d819cb9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLOEPUVN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHAvH3HRzfS%2Bqu7KuTV2SN3%2F3J37N2crOCEAl0CbMnlbAiEAjJvAFnLoUQCm5vbi39r8u3XQec1OgzXcERSXCRLW%2FqEqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLrljX41ap4Y1mJFDyrcAx0TKrZ8hOBwDfxQ%2BDfodx28UdYxjACpdy8iIN%2BLtjooghYRcRfpV8loTLaZA9CAFvRaT9Opa0%2Fp4bGk1a7lTWH8tz5cswGb0bAJpUuJkZUfQrqCdedBJYn27iJnP1C2dhfh1CnE%2F6rbF%2BZwGt%2BbEoszOD6eUnj8e4tJve4308W9hqmy7lK12ieejfL0C6ysnuRro8pn%2F%2FH08XVRLetKrTXClKEqMCTGJc4%2BUhwgKY5dw9SMmv5RpSQqK%2B8wZ33UVLz1dwJYTTzkfdpHJTYtG8CKcN99R%2FJWhoVEucs8vFk%2FehqvI7Sq%2BXKiOZ6YlMHzDk5Dryz7hbXiAfNihrGQsGDzCIXUJxMe6%2FTuxn6sPl%2Bnf%2F0nJjO9VnFyobi7nR%2Bdh1sGdfhvPtwVh0dUKgU%2FbCp%2FDfQTxmaYSQ5Ymg7mcJ8B%2BRRPOKip3sxxzr1eu%2BApz%2FBFW%2Bo3JqybsiteU26l32LDlePPeJjq3V6UZCeCZSLUz25v%2BFTKNjbx1NOGiXptaF7TGxuuR2Njs1qPlaaalmGXIGS5LJjp6YAsCgwdqvrbihm9nib5TZk03iTMszaUZwByqlZ3uz40x6UqctZnaGbux%2FSSATVqUdPRUF1Xfrzo%2Fxf1Uzqo1g3WudRuMNWk97wGOqUB6VOgQasGO7%2FvYN%2FbJp6IAmkeMmRFpeKKSC%2Bn719ATKwnqN71%2BDdKY1zyy1bgu6qasybaxLxBdlmJrzbb2OodcZrUjtifWZJr1xzU%2FqhJAb9mkKjINxR94vsaxeear6G50YIF1ul%2B3T39VEQmIh3x%2BGWwRMQGsv%2BrEeJMl1dJ0TcT0OYoc7fqCCkR7GhdsUIFwo%2BFg3NlDPmjK12p1DZdZ1AaypKy&X-Amz-Signature=97d131c85950d3864bb79d939a27f8e3527662ccb86f92840152c01f5b5ab314&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLOEPUVN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T101357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHAvH3HRzfS%2Bqu7KuTV2SN3%2F3J37N2crOCEAl0CbMnlbAiEAjJvAFnLoUQCm5vbi39r8u3XQec1OgzXcERSXCRLW%2FqEqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLrljX41ap4Y1mJFDyrcAx0TKrZ8hOBwDfxQ%2BDfodx28UdYxjACpdy8iIN%2BLtjooghYRcRfpV8loTLaZA9CAFvRaT9Opa0%2Fp4bGk1a7lTWH8tz5cswGb0bAJpUuJkZUfQrqCdedBJYn27iJnP1C2dhfh1CnE%2F6rbF%2BZwGt%2BbEoszOD6eUnj8e4tJve4308W9hqmy7lK12ieejfL0C6ysnuRro8pn%2F%2FH08XVRLetKrTXClKEqMCTGJc4%2BUhwgKY5dw9SMmv5RpSQqK%2B8wZ33UVLz1dwJYTTzkfdpHJTYtG8CKcN99R%2FJWhoVEucs8vFk%2FehqvI7Sq%2BXKiOZ6YlMHzDk5Dryz7hbXiAfNihrGQsGDzCIXUJxMe6%2FTuxn6sPl%2Bnf%2F0nJjO9VnFyobi7nR%2Bdh1sGdfhvPtwVh0dUKgU%2FbCp%2FDfQTxmaYSQ5Ymg7mcJ8B%2BRRPOKip3sxxzr1eu%2BApz%2FBFW%2Bo3JqybsiteU26l32LDlePPeJjq3V6UZCeCZSLUz25v%2BFTKNjbx1NOGiXptaF7TGxuuR2Njs1qPlaaalmGXIGS5LJjp6YAsCgwdqvrbihm9nib5TZk03iTMszaUZwByqlZ3uz40x6UqctZnaGbux%2FSSATVqUdPRUF1Xfrzo%2Fxf1Uzqo1g3WudRuMNWk97wGOqUB6VOgQasGO7%2FvYN%2FbJp6IAmkeMmRFpeKKSC%2Bn719ATKwnqN71%2BDdKY1zyy1bgu6qasybaxLxBdlmJrzbb2OodcZrUjtifWZJr1xzU%2FqhJAb9mkKjINxR94vsaxeear6G50YIF1ul%2B3T39VEQmIh3x%2BGWwRMQGsv%2BrEeJMl1dJ0TcT0OYoc7fqCCkR7GhdsUIFwo%2BFg3NlDPmjK12p1DZdZ1AaypKy&X-Amz-Signature=4b4d95671b2ba5864dfb83caae8ad28e92aa5529af90f06fa6d75403bbf71cf8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
