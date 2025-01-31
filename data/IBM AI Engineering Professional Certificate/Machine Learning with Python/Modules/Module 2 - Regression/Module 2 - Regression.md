

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KFOOTIZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTSq4v1vTk9WFLBcqK2O5jNzRgvH%2F3jLRnwDxt5EaWegIhAIRfpiq9HLK2trlbhFE9F7TUYsMzgXYem%2FuTytdOCIS0KogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxghxCJ39j8outaUEcq3APC0uoEFELNH68JgtX8bqZPITVP0GWan4QtUf3T2%2FkW2OupSNdP8SCpfi3T65ERzXbkBJouBQViJFK%2FWjAEdX5jEwD1sR6syAxmx%2B%2FoZrX4ayeEvHPARbIT1ozDqKS7L%2FJy9lGZzQY1%2B4WKFNy9ps9xbQL0EsIOrGf6myp27MKVKjW8noG%2BoazXTrq93%2FInyHDkAWpoc33wYShaRgu6aWJwGx2pH1rFNQ4QEjd2hmSs22fjpak2iqZ9xgZgGiLirbOhWH23zNCbDUfj3iKuHU0A5vSd077y1E%2F6BrcCgn5j6qrkK3uxwna69IPsh63WuP29%2FFhKlpJCu0o0qgYmx%2Fy2XtxIy6NwwFN%2BzdySHkZXf1vibpCxSZzo1bFAidnr80PzDIY26xac%2FJkxnLeIXjML%2FQDJyuPtM8H3GaH%2FAitPTCAg8osqtu2fXFvWMdOvQe5TjcC99nYrzX3qv9qij0gW3H2IR%2BPMlriofHQyZS7TXtZXdaq1lFS%2FFtaOkJK%2B58LqpUvRmHVQXCKeHUJnpc0DVfjBDvC6OrQzit8P%2BKkHMCT1DV4sJ3w0JjF1yWM%2BdOZQbNOiM3PyE7OsROXsh2Qm2OoTUJtqrucIyoGVqUZrTEI9nD%2FX%2F0drDP2rYDD0j%2FO8BjqkAVgLGv1URleDc9Bp2G%2FxAyZwqYYl%2FsGWL4J0sU6Xc%2BXGyC1%2FwYUzm51OYIHenVzTrM4oSqRuTklBBaWkRALf1txrgKJ2i3cWjAn2vB3QNwFPiOdLM9M6jOrfNRKXdhczQbNKBtqFqQtQ7TpRHX6HqvNaDSIky35dGc9KzgCYku%2Bnka7ogle1MwZ7W9F%2BX2BL3wCuBNp2DDldISxqu6i4KjNvHbSC&X-Amz-Signature=a829cdddad1f26fe6fd4f2f91ab982a7e79bfa060998e727af27a50af2a1c86c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KFOOTIZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTSq4v1vTk9WFLBcqK2O5jNzRgvH%2F3jLRnwDxt5EaWegIhAIRfpiq9HLK2trlbhFE9F7TUYsMzgXYem%2FuTytdOCIS0KogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxghxCJ39j8outaUEcq3APC0uoEFELNH68JgtX8bqZPITVP0GWan4QtUf3T2%2FkW2OupSNdP8SCpfi3T65ERzXbkBJouBQViJFK%2FWjAEdX5jEwD1sR6syAxmx%2B%2FoZrX4ayeEvHPARbIT1ozDqKS7L%2FJy9lGZzQY1%2B4WKFNy9ps9xbQL0EsIOrGf6myp27MKVKjW8noG%2BoazXTrq93%2FInyHDkAWpoc33wYShaRgu6aWJwGx2pH1rFNQ4QEjd2hmSs22fjpak2iqZ9xgZgGiLirbOhWH23zNCbDUfj3iKuHU0A5vSd077y1E%2F6BrcCgn5j6qrkK3uxwna69IPsh63WuP29%2FFhKlpJCu0o0qgYmx%2Fy2XtxIy6NwwFN%2BzdySHkZXf1vibpCxSZzo1bFAidnr80PzDIY26xac%2FJkxnLeIXjML%2FQDJyuPtM8H3GaH%2FAitPTCAg8osqtu2fXFvWMdOvQe5TjcC99nYrzX3qv9qij0gW3H2IR%2BPMlriofHQyZS7TXtZXdaq1lFS%2FFtaOkJK%2B58LqpUvRmHVQXCKeHUJnpc0DVfjBDvC6OrQzit8P%2BKkHMCT1DV4sJ3w0JjF1yWM%2BdOZQbNOiM3PyE7OsROXsh2Qm2OoTUJtqrucIyoGVqUZrTEI9nD%2FX%2F0drDP2rYDD0j%2FO8BjqkAVgLGv1URleDc9Bp2G%2FxAyZwqYYl%2FsGWL4J0sU6Xc%2BXGyC1%2FwYUzm51OYIHenVzTrM4oSqRuTklBBaWkRALf1txrgKJ2i3cWjAn2vB3QNwFPiOdLM9M6jOrfNRKXdhczQbNKBtqFqQtQ7TpRHX6HqvNaDSIky35dGc9KzgCYku%2Bnka7ogle1MwZ7W9F%2BX2BL3wCuBNp2DDldISxqu6i4KjNvHbSC&X-Amz-Signature=78a1ce44866e2f8d3a680f8960a9e12a4dc60c9ba0b57ea220b4dbf1a2dc7793&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KFOOTIZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTSq4v1vTk9WFLBcqK2O5jNzRgvH%2F3jLRnwDxt5EaWegIhAIRfpiq9HLK2trlbhFE9F7TUYsMzgXYem%2FuTytdOCIS0KogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxghxCJ39j8outaUEcq3APC0uoEFELNH68JgtX8bqZPITVP0GWan4QtUf3T2%2FkW2OupSNdP8SCpfi3T65ERzXbkBJouBQViJFK%2FWjAEdX5jEwD1sR6syAxmx%2B%2FoZrX4ayeEvHPARbIT1ozDqKS7L%2FJy9lGZzQY1%2B4WKFNy9ps9xbQL0EsIOrGf6myp27MKVKjW8noG%2BoazXTrq93%2FInyHDkAWpoc33wYShaRgu6aWJwGx2pH1rFNQ4QEjd2hmSs22fjpak2iqZ9xgZgGiLirbOhWH23zNCbDUfj3iKuHU0A5vSd077y1E%2F6BrcCgn5j6qrkK3uxwna69IPsh63WuP29%2FFhKlpJCu0o0qgYmx%2Fy2XtxIy6NwwFN%2BzdySHkZXf1vibpCxSZzo1bFAidnr80PzDIY26xac%2FJkxnLeIXjML%2FQDJyuPtM8H3GaH%2FAitPTCAg8osqtu2fXFvWMdOvQe5TjcC99nYrzX3qv9qij0gW3H2IR%2BPMlriofHQyZS7TXtZXdaq1lFS%2FFtaOkJK%2B58LqpUvRmHVQXCKeHUJnpc0DVfjBDvC6OrQzit8P%2BKkHMCT1DV4sJ3w0JjF1yWM%2BdOZQbNOiM3PyE7OsROXsh2Qm2OoTUJtqrucIyoGVqUZrTEI9nD%2FX%2F0drDP2rYDD0j%2FO8BjqkAVgLGv1URleDc9Bp2G%2FxAyZwqYYl%2FsGWL4J0sU6Xc%2BXGyC1%2FwYUzm51OYIHenVzTrM4oSqRuTklBBaWkRALf1txrgKJ2i3cWjAn2vB3QNwFPiOdLM9M6jOrfNRKXdhczQbNKBtqFqQtQ7TpRHX6HqvNaDSIky35dGc9KzgCYku%2Bnka7ogle1MwZ7W9F%2BX2BL3wCuBNp2DDldISxqu6i4KjNvHbSC&X-Amz-Signature=8f5d809eb1129373317b24c35bb135b25217f8f9bc884d5be437f22ef29dca65&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KFOOTIZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTSq4v1vTk9WFLBcqK2O5jNzRgvH%2F3jLRnwDxt5EaWegIhAIRfpiq9HLK2trlbhFE9F7TUYsMzgXYem%2FuTytdOCIS0KogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxghxCJ39j8outaUEcq3APC0uoEFELNH68JgtX8bqZPITVP0GWan4QtUf3T2%2FkW2OupSNdP8SCpfi3T65ERzXbkBJouBQViJFK%2FWjAEdX5jEwD1sR6syAxmx%2B%2FoZrX4ayeEvHPARbIT1ozDqKS7L%2FJy9lGZzQY1%2B4WKFNy9ps9xbQL0EsIOrGf6myp27MKVKjW8noG%2BoazXTrq93%2FInyHDkAWpoc33wYShaRgu6aWJwGx2pH1rFNQ4QEjd2hmSs22fjpak2iqZ9xgZgGiLirbOhWH23zNCbDUfj3iKuHU0A5vSd077y1E%2F6BrcCgn5j6qrkK3uxwna69IPsh63WuP29%2FFhKlpJCu0o0qgYmx%2Fy2XtxIy6NwwFN%2BzdySHkZXf1vibpCxSZzo1bFAidnr80PzDIY26xac%2FJkxnLeIXjML%2FQDJyuPtM8H3GaH%2FAitPTCAg8osqtu2fXFvWMdOvQe5TjcC99nYrzX3qv9qij0gW3H2IR%2BPMlriofHQyZS7TXtZXdaq1lFS%2FFtaOkJK%2B58LqpUvRmHVQXCKeHUJnpc0DVfjBDvC6OrQzit8P%2BKkHMCT1DV4sJ3w0JjF1yWM%2BdOZQbNOiM3PyE7OsROXsh2Qm2OoTUJtqrucIyoGVqUZrTEI9nD%2FX%2F0drDP2rYDD0j%2FO8BjqkAVgLGv1URleDc9Bp2G%2FxAyZwqYYl%2FsGWL4J0sU6Xc%2BXGyC1%2FwYUzm51OYIHenVzTrM4oSqRuTklBBaWkRALf1txrgKJ2i3cWjAn2vB3QNwFPiOdLM9M6jOrfNRKXdhczQbNKBtqFqQtQ7TpRHX6HqvNaDSIky35dGc9KzgCYku%2Bnka7ogle1MwZ7W9F%2BX2BL3wCuBNp2DDldISxqu6i4KjNvHbSC&X-Amz-Signature=fa73ecdef41faa5ba13a8c50a989ecfbae05c1a6c136d96e4112000e185382eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KFOOTIZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTSq4v1vTk9WFLBcqK2O5jNzRgvH%2F3jLRnwDxt5EaWegIhAIRfpiq9HLK2trlbhFE9F7TUYsMzgXYem%2FuTytdOCIS0KogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxghxCJ39j8outaUEcq3APC0uoEFELNH68JgtX8bqZPITVP0GWan4QtUf3T2%2FkW2OupSNdP8SCpfi3T65ERzXbkBJouBQViJFK%2FWjAEdX5jEwD1sR6syAxmx%2B%2FoZrX4ayeEvHPARbIT1ozDqKS7L%2FJy9lGZzQY1%2B4WKFNy9ps9xbQL0EsIOrGf6myp27MKVKjW8noG%2BoazXTrq93%2FInyHDkAWpoc33wYShaRgu6aWJwGx2pH1rFNQ4QEjd2hmSs22fjpak2iqZ9xgZgGiLirbOhWH23zNCbDUfj3iKuHU0A5vSd077y1E%2F6BrcCgn5j6qrkK3uxwna69IPsh63WuP29%2FFhKlpJCu0o0qgYmx%2Fy2XtxIy6NwwFN%2BzdySHkZXf1vibpCxSZzo1bFAidnr80PzDIY26xac%2FJkxnLeIXjML%2FQDJyuPtM8H3GaH%2FAitPTCAg8osqtu2fXFvWMdOvQe5TjcC99nYrzX3qv9qij0gW3H2IR%2BPMlriofHQyZS7TXtZXdaq1lFS%2FFtaOkJK%2B58LqpUvRmHVQXCKeHUJnpc0DVfjBDvC6OrQzit8P%2BKkHMCT1DV4sJ3w0JjF1yWM%2BdOZQbNOiM3PyE7OsROXsh2Qm2OoTUJtqrucIyoGVqUZrTEI9nD%2FX%2F0drDP2rYDD0j%2FO8BjqkAVgLGv1URleDc9Bp2G%2FxAyZwqYYl%2FsGWL4J0sU6Xc%2BXGyC1%2FwYUzm51OYIHenVzTrM4oSqRuTklBBaWkRALf1txrgKJ2i3cWjAn2vB3QNwFPiOdLM9M6jOrfNRKXdhczQbNKBtqFqQtQ7TpRHX6HqvNaDSIky35dGc9KzgCYku%2Bnka7ogle1MwZ7W9F%2BX2BL3wCuBNp2DDldISxqu6i4KjNvHbSC&X-Amz-Signature=e296df1129d15c4d7b012211e3a2ffc4e026237ece2d0d4047c1ac02ccf20425&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KFOOTIZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTSq4v1vTk9WFLBcqK2O5jNzRgvH%2F3jLRnwDxt5EaWegIhAIRfpiq9HLK2trlbhFE9F7TUYsMzgXYem%2FuTytdOCIS0KogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxghxCJ39j8outaUEcq3APC0uoEFELNH68JgtX8bqZPITVP0GWan4QtUf3T2%2FkW2OupSNdP8SCpfi3T65ERzXbkBJouBQViJFK%2FWjAEdX5jEwD1sR6syAxmx%2B%2FoZrX4ayeEvHPARbIT1ozDqKS7L%2FJy9lGZzQY1%2B4WKFNy9ps9xbQL0EsIOrGf6myp27MKVKjW8noG%2BoazXTrq93%2FInyHDkAWpoc33wYShaRgu6aWJwGx2pH1rFNQ4QEjd2hmSs22fjpak2iqZ9xgZgGiLirbOhWH23zNCbDUfj3iKuHU0A5vSd077y1E%2F6BrcCgn5j6qrkK3uxwna69IPsh63WuP29%2FFhKlpJCu0o0qgYmx%2Fy2XtxIy6NwwFN%2BzdySHkZXf1vibpCxSZzo1bFAidnr80PzDIY26xac%2FJkxnLeIXjML%2FQDJyuPtM8H3GaH%2FAitPTCAg8osqtu2fXFvWMdOvQe5TjcC99nYrzX3qv9qij0gW3H2IR%2BPMlriofHQyZS7TXtZXdaq1lFS%2FFtaOkJK%2B58LqpUvRmHVQXCKeHUJnpc0DVfjBDvC6OrQzit8P%2BKkHMCT1DV4sJ3w0JjF1yWM%2BdOZQbNOiM3PyE7OsROXsh2Qm2OoTUJtqrucIyoGVqUZrTEI9nD%2FX%2F0drDP2rYDD0j%2FO8BjqkAVgLGv1URleDc9Bp2G%2FxAyZwqYYl%2FsGWL4J0sU6Xc%2BXGyC1%2FwYUzm51OYIHenVzTrM4oSqRuTklBBaWkRALf1txrgKJ2i3cWjAn2vB3QNwFPiOdLM9M6jOrfNRKXdhczQbNKBtqFqQtQ7TpRHX6HqvNaDSIky35dGc9KzgCYku%2Bnka7ogle1MwZ7W9F%2BX2BL3wCuBNp2DDldISxqu6i4KjNvHbSC&X-Amz-Signature=254f4487d729e1ca73fb91d29cc8b71acb9d7979811a64487693dd02e17780ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KFOOTIZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTSq4v1vTk9WFLBcqK2O5jNzRgvH%2F3jLRnwDxt5EaWegIhAIRfpiq9HLK2trlbhFE9F7TUYsMzgXYem%2FuTytdOCIS0KogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxghxCJ39j8outaUEcq3APC0uoEFELNH68JgtX8bqZPITVP0GWan4QtUf3T2%2FkW2OupSNdP8SCpfi3T65ERzXbkBJouBQViJFK%2FWjAEdX5jEwD1sR6syAxmx%2B%2FoZrX4ayeEvHPARbIT1ozDqKS7L%2FJy9lGZzQY1%2B4WKFNy9ps9xbQL0EsIOrGf6myp27MKVKjW8noG%2BoazXTrq93%2FInyHDkAWpoc33wYShaRgu6aWJwGx2pH1rFNQ4QEjd2hmSs22fjpak2iqZ9xgZgGiLirbOhWH23zNCbDUfj3iKuHU0A5vSd077y1E%2F6BrcCgn5j6qrkK3uxwna69IPsh63WuP29%2FFhKlpJCu0o0qgYmx%2Fy2XtxIy6NwwFN%2BzdySHkZXf1vibpCxSZzo1bFAidnr80PzDIY26xac%2FJkxnLeIXjML%2FQDJyuPtM8H3GaH%2FAitPTCAg8osqtu2fXFvWMdOvQe5TjcC99nYrzX3qv9qij0gW3H2IR%2BPMlriofHQyZS7TXtZXdaq1lFS%2FFtaOkJK%2B58LqpUvRmHVQXCKeHUJnpc0DVfjBDvC6OrQzit8P%2BKkHMCT1DV4sJ3w0JjF1yWM%2BdOZQbNOiM3PyE7OsROXsh2Qm2OoTUJtqrucIyoGVqUZrTEI9nD%2FX%2F0drDP2rYDD0j%2FO8BjqkAVgLGv1URleDc9Bp2G%2FxAyZwqYYl%2FsGWL4J0sU6Xc%2BXGyC1%2FwYUzm51OYIHenVzTrM4oSqRuTklBBaWkRALf1txrgKJ2i3cWjAn2vB3QNwFPiOdLM9M6jOrfNRKXdhczQbNKBtqFqQtQ7TpRHX6HqvNaDSIky35dGc9KzgCYku%2Bnka7ogle1MwZ7W9F%2BX2BL3wCuBNp2DDldISxqu6i4KjNvHbSC&X-Amz-Signature=d3583c655e28f016548658aa059f320028757c8f161ed5c12333ae132bed5b83&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KFOOTIZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTSq4v1vTk9WFLBcqK2O5jNzRgvH%2F3jLRnwDxt5EaWegIhAIRfpiq9HLK2trlbhFE9F7TUYsMzgXYem%2FuTytdOCIS0KogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxghxCJ39j8outaUEcq3APC0uoEFELNH68JgtX8bqZPITVP0GWan4QtUf3T2%2FkW2OupSNdP8SCpfi3T65ERzXbkBJouBQViJFK%2FWjAEdX5jEwD1sR6syAxmx%2B%2FoZrX4ayeEvHPARbIT1ozDqKS7L%2FJy9lGZzQY1%2B4WKFNy9ps9xbQL0EsIOrGf6myp27MKVKjW8noG%2BoazXTrq93%2FInyHDkAWpoc33wYShaRgu6aWJwGx2pH1rFNQ4QEjd2hmSs22fjpak2iqZ9xgZgGiLirbOhWH23zNCbDUfj3iKuHU0A5vSd077y1E%2F6BrcCgn5j6qrkK3uxwna69IPsh63WuP29%2FFhKlpJCu0o0qgYmx%2Fy2XtxIy6NwwFN%2BzdySHkZXf1vibpCxSZzo1bFAidnr80PzDIY26xac%2FJkxnLeIXjML%2FQDJyuPtM8H3GaH%2FAitPTCAg8osqtu2fXFvWMdOvQe5TjcC99nYrzX3qv9qij0gW3H2IR%2BPMlriofHQyZS7TXtZXdaq1lFS%2FFtaOkJK%2B58LqpUvRmHVQXCKeHUJnpc0DVfjBDvC6OrQzit8P%2BKkHMCT1DV4sJ3w0JjF1yWM%2BdOZQbNOiM3PyE7OsROXsh2Qm2OoTUJtqrucIyoGVqUZrTEI9nD%2FX%2F0drDP2rYDD0j%2FO8BjqkAVgLGv1URleDc9Bp2G%2FxAyZwqYYl%2FsGWL4J0sU6Xc%2BXGyC1%2FwYUzm51OYIHenVzTrM4oSqRuTklBBaWkRALf1txrgKJ2i3cWjAn2vB3QNwFPiOdLM9M6jOrfNRKXdhczQbNKBtqFqQtQ7TpRHX6HqvNaDSIky35dGc9KzgCYku%2Bnka7ogle1MwZ7W9F%2BX2BL3wCuBNp2DDldISxqu6i4KjNvHbSC&X-Amz-Signature=de25e434d7d75346ad2a8d15aad9d8ddf3fd4353361f4b5dc0fd008ef23627a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOYRHOI5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDohOu1aqkYD3%2FUoBKx%2BrAhxOSprYtEdB%2Bf2eX6qzXUKAiArrDwk0Z4Do3hBWMldL3Q7OHMlFJ2hOVjhStdxx9MGriqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvGkWett9Hh297iImKtwDBvTyysRhkB%2BuVTGZheYHMUZYFfSKO6vM0PPCq%2FyuuhYke43mOSUtgDzT4fhSUCdmXJ3HvlAd1zhNCmAsWoimlaRU7a%2BBc7Ky9TqojqDaralFbGzzExeIW%2BHeGOqnqrjZN74eonjQfHMeSj2YYt0G2LRhqwh6FNYuEiHtQ2CnRlE4WjYZlsOWq%2Bc43wSHIGtEjRow%2B4%2B3jVPCro72tGvG2JIkptlpGSjQtQ8ExU7SWGLAvEEtV2U%2BngPDNR%2BuTna%2B5vl1q7CcH0NUGyOkMZUAUA0I7EfdyjN%2BOtlcQnoNV352xPC0Tpiu69D8s6ru1IqK54w03Qj6Z%2FK54AN9ZzNbd6dq8ZU%2FApPAB3TfObt9O4%2FyP8Inks4nlN1ohY%2FV6oAwK5kdBq%2FjrUvR29ZzsnkMA2d4Us4cG6nUOCHJA%2FyOuw6y7JvrUPpGa6BdODjry0wpRqppqHKk%2B5drXQF75vI842Q3qJsKZtMXlq%2FB4V9xvr%2BIsrOlwqvu83xfwJyWnjETXx65i2T8EuXc%2FrHqRjmz1kOWS0NV0kQO7VoL45ul06LyMf2jSaCYO9qxZdtVUxuKtx8kiUvbK81JZh8IdmohKoLnorWjUf%2Byq9roqMRYo93lBfVERSmForBMxA4wqI%2FzvAY6pgF%2FmsRHobGPgceOs8iacB2f7d1hUodkeL8jl6yczgT6Q0XuZb%2B%2BnedmIFSdcrbM%2B9cJFMLuu9z8wLqGABr9tPCRB4XduPZL9rTwxVAKvc%2FhMq%2BYkFYVT4ltWbinqj1NmaooaXq9MJaiPbK6QhQBuOyel4xWjTrEdznKOb1PLHr16NUNsti5lDQFBi10DBuATdIta8EzP1E6qXuPzje3cdW7LqH5FLQG&X-Amz-Signature=b909f2d0a39375507323f57a236c8f398ad777b50a9a5f6bfc2171186573f6e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RMTSPXO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8pJZ0LoYTrwkDSKe2bSg%2FdTKCbnE9uEcxW5suJaivDAiBA6s9ulgu4lbFFJmzookEMgVV4WNUWRDOuk7YVke21WCqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwuE6t9c2bZmwf57QKtwD6UdgZlZftsksZORkCpcOI2%2FI%2FcA0mIUsm%2BVBHneTR16QQR92DokOKo8MYkHUcvRNjlXpCGR4R95w3h0HxaUUpV1bqGUS1FEdl%2F6U6p1f6deh2fbbHX20ZRyuZUrofSr4J%2Bebv4HSSizPjIeNC6S6euiqRExrGixKQxdzC%2BXPds1KzV96uo8lm3LypIEvmz7dPOCYTnbhHL8x8tuTpav0BLe6UgOPmyrU0ztqfZwL22e%2BHR5T0%2BpZC%2FahtEFhtC7GEwG2eOVCLSYTLAgB2SzDlmTSDLEmxVpb3PP7z%2BMO7CXHgoEMO3mf3qPcaSNinMY358c6v0G1ya%2F9bM4mL1DZPcNsNpRr%2Bhghr%2BCoE2pLxHJwiGeNvWvWbHS6ZHrWk0qfOGx1WpWTwK3vsjayi%2Bswp8wUwN3A%2BiPQVaIM7xmK3Q0Bd6rI8AzIJJmhPkznz9eTM%2BDb9jFjIvPMti2UnYWV8wOIfA%2BCSmIX7a24tcsmQR0hXeZ7hAVQ7PUMST0aI%2BLpKIHrziYjNTbYxtx1WqvWH%2FclqlcthZcVUbFdJuDvqW4p86DQMEw2OZBTywwrj8MEIwrV9nNmKkjBFG8YgnVpLDWeC7U7KSlwPeYTIVDxJFuY3SyXgYTf5ZX5FUMwxY%2FzvAY6pgHC7oWR7YthiUoyKxiWOJbHY0PUlxg9R2W%2FZrM%2FoV%2BMH7uFGqOTE4HFZzK73wmFbkrO7igpr3MnbcMiZ7xyQCpe7b%2BaT75029H4tjGTI3QcnUtqipXVt5JcYWGuowCOj8Ca9kFAxwhzFIql4Gt7iVevWHVH9IJ9GpAHt7lj8GBOmhC8xUgrXi5jbl4uJXOW4bne0IuQZW5Nri%2B8m0XNRACWtxULNrTH&X-Amz-Signature=f4d77d419b1813f93fe35b50bc9068a5d943943a359c58bbfea37629a1c9ced5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOGW3LJI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqpRM2JK2zr21OKoV7CbORnobZXDclFlzdnbmqtjJSQwIgEBpjWjC%2F6NRxLI%2Frov%2BkrNnP7UyMehToSSQZXiXpeUYqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE466LdUQFn7pSCyIyrcA5cIV9wJvx%2FHMO97YexcGyuwsB5OS7rEOFHYtZ%2FuGx9Q0jC%2BGMVVExPH3TZtIN9jjXAXes1a4x2VZCHIcLAM7E%2F1yN%2BnVAlnayikqlXUSpA7EA8ksTSUgSAYTR6CrIuv3bvsLKR3q3RZUZS46He%2F6ddhKEGgdQfR1exvt7geD%2FIGqxBmH1eZFz0Cpkyu%2BNT7RhkuY0H12rlbMheSdTEbNsNinqBabFyuxSLtaXDlM6%2FEIbFU33kZKlQdjIwDFKqBMP1incIBco86x5KVikolvcGxvE5nxPrWog07EA6lRQe6TVpR34I%2B%2FPjAmcNB1EixbNYvu8%2BNxfercm7L%2BVAaz4k6IAWQJH3blqq%2FFirvx%2FFjMCoKs5O4GZx6%2FRu6lR1xa7fYLpc8OLibZnkaHbRWjctLGsEuwNeJpAzw00%2Bw5Aeed2mxhUQ8bzRRGrHCP0ktwoWVox2O2qiQ49Uz%2Fxdze75KGkjFT072cK5CX8sVD8E%2BlWvgwFZlOCaegk%2FAhe%2Foup8gGTOfLKxhvUGP2onj2xO4VIsKkK%2FhVpa518ritnDYJFhBTnUzAYtgXMJqeONh0k%2Btz%2FUXLcsoU1gwpwYYZ090YlyfbEG5hx62Z0UJ8358kHYNqHCB%2Fr2rbj9KMJ2P87wGOqUBYa6GtTOHSCnAQRRnnKz9Oz9d0kZdxFgruOhC%2FKyevH7hjsI0vhXzPmzlpATavtTkUocjgoJO4AerWgnzt1DG9wuC7uVElsZTcKiKNF3%2FOdoyyLiGdWjKLSWOiXWt1rTbitssVm3ZQW%2F%2FuUizivkC%2FbqY%2BLe%2BT886TAUeePKRVsWWaAug4lKKZU91FMa%2BDrEu6CgX%2BTNzPimBcC9ujavEkkQu7Xtk&X-Amz-Signature=4f5edc1034b0d797d89eb6d6fa114015211a251a816fa8e65860ed26a93a9ca2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOGW3LJI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqpRM2JK2zr21OKoV7CbORnobZXDclFlzdnbmqtjJSQwIgEBpjWjC%2F6NRxLI%2Frov%2BkrNnP7UyMehToSSQZXiXpeUYqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE466LdUQFn7pSCyIyrcA5cIV9wJvx%2FHMO97YexcGyuwsB5OS7rEOFHYtZ%2FuGx9Q0jC%2BGMVVExPH3TZtIN9jjXAXes1a4x2VZCHIcLAM7E%2F1yN%2BnVAlnayikqlXUSpA7EA8ksTSUgSAYTR6CrIuv3bvsLKR3q3RZUZS46He%2F6ddhKEGgdQfR1exvt7geD%2FIGqxBmH1eZFz0Cpkyu%2BNT7RhkuY0H12rlbMheSdTEbNsNinqBabFyuxSLtaXDlM6%2FEIbFU33kZKlQdjIwDFKqBMP1incIBco86x5KVikolvcGxvE5nxPrWog07EA6lRQe6TVpR34I%2B%2FPjAmcNB1EixbNYvu8%2BNxfercm7L%2BVAaz4k6IAWQJH3blqq%2FFirvx%2FFjMCoKs5O4GZx6%2FRu6lR1xa7fYLpc8OLibZnkaHbRWjctLGsEuwNeJpAzw00%2Bw5Aeed2mxhUQ8bzRRGrHCP0ktwoWVox2O2qiQ49Uz%2Fxdze75KGkjFT072cK5CX8sVD8E%2BlWvgwFZlOCaegk%2FAhe%2Foup8gGTOfLKxhvUGP2onj2xO4VIsKkK%2FhVpa518ritnDYJFhBTnUzAYtgXMJqeONh0k%2Btz%2FUXLcsoU1gwpwYYZ090YlyfbEG5hx62Z0UJ8358kHYNqHCB%2Fr2rbj9KMJ2P87wGOqUBYa6GtTOHSCnAQRRnnKz9Oz9d0kZdxFgruOhC%2FKyevH7hjsI0vhXzPmzlpATavtTkUocjgoJO4AerWgnzt1DG9wuC7uVElsZTcKiKNF3%2FOdoyyLiGdWjKLSWOiXWt1rTbitssVm3ZQW%2F%2FuUizivkC%2FbqY%2BLe%2BT886TAUeePKRVsWWaAug4lKKZU91FMa%2BDrEu6CgX%2BTNzPimBcC9ujavEkkQu7Xtk&X-Amz-Signature=0885e87b0ac63d505649b58102207cd38efd5af1d4ec93c2304e5fad4e63069f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
