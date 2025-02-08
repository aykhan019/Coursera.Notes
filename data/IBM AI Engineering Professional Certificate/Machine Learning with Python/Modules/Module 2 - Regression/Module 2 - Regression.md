

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TRXN2OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHskKMJyFzbD6WunhVDwY7S60rVKwkjBqi0%2FHv14LFo2AiEAmb%2FFCLcEYpxj2fjQt8cu21hb1hg%2BocHSmerjXlH%2FD%2BMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJBHU8acMIjq%2FdfBQSrcA9FNuqLZH297CxIZL8C8WEmuUqJEnUBhqJJeC5qV6y0gRPS%2FqKp0J4roNS0m%2FwQIypaSAoOwGLPpcaoyOSwnKXBTC5Q1W0kNKDiCp8emSHzeSBCogzPrHoHAPEDqUCWK6gW%2F24FyzEErY%2B3%2BnN97WGAwTdJrC7o7y3jk5G1JXjowqXTGAhw5GWahBZ4DsU3lhOGdDWXdfYH3pp5g1Mu%2FqePyR%2ByZdwBhR%2FW3krS84deeenPZWGmHi3AUEGsls1F%2FsRRic68MySKQr6Yfja597z0YF58FmrU9RMk4KMYSzJE3Z7DSZaKyDCwwJA7%2F8Zr8Up89AP3qdOGADhy2Xr0yfKhhlabILf0uoREbkB9XupYn1V6SOArlDz4eC4Ve08oZa2IXB5Y5soiHQG7f3uP78L62dR%2F8WqocDmwAuJQAXHbWQzz2KTrTHQIFhycXGeqQQYMpdJk95YJ2YAOYFtn9796iP%2FkmQffXNISpvh3YBAGyP%2FpGGsezIvc4molf8zh%2BPDS2QxezXQcNIc1qEgDkKT%2FxOYP5e3u48IBvG685lE5XTCvP%2B82j09Uolp4E%2Fi%2BHtsSl7k2coE6ahYHeuMHEtpX2mBi%2FF0WOwtH5lfdmKa80QIZeOnEa2GQiMn%2F6MNaFnb0GOqUBVsp7Dcd%2FGc0dOVseo5gpOio6hBMVL1UOczk%2BRkuLOlUm14ehHkgFADyf0a5gafdXyCErzuKCzXctVuhoM%2B5CvsnhictaRlA4I5CCptZjJB6GgVXJKpoYkCcK6rDsjPvZFY44hHoOYB2quFbHP01%2B%2BmrtnLWrHcZP7B%2BapoUxebz4JlH8k94QyfN7aww8NjenWKpEW3MEK%2FYJBSG72Ftul6l5MaHc&X-Amz-Signature=e4521edddbcd1454110e8307aa0df636d62c771b3c5644a0ebf86c5f536a4b37&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TRXN2OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHskKMJyFzbD6WunhVDwY7S60rVKwkjBqi0%2FHv14LFo2AiEAmb%2FFCLcEYpxj2fjQt8cu21hb1hg%2BocHSmerjXlH%2FD%2BMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJBHU8acMIjq%2FdfBQSrcA9FNuqLZH297CxIZL8C8WEmuUqJEnUBhqJJeC5qV6y0gRPS%2FqKp0J4roNS0m%2FwQIypaSAoOwGLPpcaoyOSwnKXBTC5Q1W0kNKDiCp8emSHzeSBCogzPrHoHAPEDqUCWK6gW%2F24FyzEErY%2B3%2BnN97WGAwTdJrC7o7y3jk5G1JXjowqXTGAhw5GWahBZ4DsU3lhOGdDWXdfYH3pp5g1Mu%2FqePyR%2ByZdwBhR%2FW3krS84deeenPZWGmHi3AUEGsls1F%2FsRRic68MySKQr6Yfja597z0YF58FmrU9RMk4KMYSzJE3Z7DSZaKyDCwwJA7%2F8Zr8Up89AP3qdOGADhy2Xr0yfKhhlabILf0uoREbkB9XupYn1V6SOArlDz4eC4Ve08oZa2IXB5Y5soiHQG7f3uP78L62dR%2F8WqocDmwAuJQAXHbWQzz2KTrTHQIFhycXGeqQQYMpdJk95YJ2YAOYFtn9796iP%2FkmQffXNISpvh3YBAGyP%2FpGGsezIvc4molf8zh%2BPDS2QxezXQcNIc1qEgDkKT%2FxOYP5e3u48IBvG685lE5XTCvP%2B82j09Uolp4E%2Fi%2BHtsSl7k2coE6ahYHeuMHEtpX2mBi%2FF0WOwtH5lfdmKa80QIZeOnEa2GQiMn%2F6MNaFnb0GOqUBVsp7Dcd%2FGc0dOVseo5gpOio6hBMVL1UOczk%2BRkuLOlUm14ehHkgFADyf0a5gafdXyCErzuKCzXctVuhoM%2B5CvsnhictaRlA4I5CCptZjJB6GgVXJKpoYkCcK6rDsjPvZFY44hHoOYB2quFbHP01%2B%2BmrtnLWrHcZP7B%2BapoUxebz4JlH8k94QyfN7aww8NjenWKpEW3MEK%2FYJBSG72Ftul6l5MaHc&X-Amz-Signature=02699d898e9ad8cd3bc054c9870c566239a0119e12ea21db16d530c44c30460a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TRXN2OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHskKMJyFzbD6WunhVDwY7S60rVKwkjBqi0%2FHv14LFo2AiEAmb%2FFCLcEYpxj2fjQt8cu21hb1hg%2BocHSmerjXlH%2FD%2BMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJBHU8acMIjq%2FdfBQSrcA9FNuqLZH297CxIZL8C8WEmuUqJEnUBhqJJeC5qV6y0gRPS%2FqKp0J4roNS0m%2FwQIypaSAoOwGLPpcaoyOSwnKXBTC5Q1W0kNKDiCp8emSHzeSBCogzPrHoHAPEDqUCWK6gW%2F24FyzEErY%2B3%2BnN97WGAwTdJrC7o7y3jk5G1JXjowqXTGAhw5GWahBZ4DsU3lhOGdDWXdfYH3pp5g1Mu%2FqePyR%2ByZdwBhR%2FW3krS84deeenPZWGmHi3AUEGsls1F%2FsRRic68MySKQr6Yfja597z0YF58FmrU9RMk4KMYSzJE3Z7DSZaKyDCwwJA7%2F8Zr8Up89AP3qdOGADhy2Xr0yfKhhlabILf0uoREbkB9XupYn1V6SOArlDz4eC4Ve08oZa2IXB5Y5soiHQG7f3uP78L62dR%2F8WqocDmwAuJQAXHbWQzz2KTrTHQIFhycXGeqQQYMpdJk95YJ2YAOYFtn9796iP%2FkmQffXNISpvh3YBAGyP%2FpGGsezIvc4molf8zh%2BPDS2QxezXQcNIc1qEgDkKT%2FxOYP5e3u48IBvG685lE5XTCvP%2B82j09Uolp4E%2Fi%2BHtsSl7k2coE6ahYHeuMHEtpX2mBi%2FF0WOwtH5lfdmKa80QIZeOnEa2GQiMn%2F6MNaFnb0GOqUBVsp7Dcd%2FGc0dOVseo5gpOio6hBMVL1UOczk%2BRkuLOlUm14ehHkgFADyf0a5gafdXyCErzuKCzXctVuhoM%2B5CvsnhictaRlA4I5CCptZjJB6GgVXJKpoYkCcK6rDsjPvZFY44hHoOYB2quFbHP01%2B%2BmrtnLWrHcZP7B%2BapoUxebz4JlH8k94QyfN7aww8NjenWKpEW3MEK%2FYJBSG72Ftul6l5MaHc&X-Amz-Signature=80292f3bbf7f66b1395e296d0d3cca46b5fcff616f46aa850ba8100cf0813b6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TRXN2OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHskKMJyFzbD6WunhVDwY7S60rVKwkjBqi0%2FHv14LFo2AiEAmb%2FFCLcEYpxj2fjQt8cu21hb1hg%2BocHSmerjXlH%2FD%2BMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJBHU8acMIjq%2FdfBQSrcA9FNuqLZH297CxIZL8C8WEmuUqJEnUBhqJJeC5qV6y0gRPS%2FqKp0J4roNS0m%2FwQIypaSAoOwGLPpcaoyOSwnKXBTC5Q1W0kNKDiCp8emSHzeSBCogzPrHoHAPEDqUCWK6gW%2F24FyzEErY%2B3%2BnN97WGAwTdJrC7o7y3jk5G1JXjowqXTGAhw5GWahBZ4DsU3lhOGdDWXdfYH3pp5g1Mu%2FqePyR%2ByZdwBhR%2FW3krS84deeenPZWGmHi3AUEGsls1F%2FsRRic68MySKQr6Yfja597z0YF58FmrU9RMk4KMYSzJE3Z7DSZaKyDCwwJA7%2F8Zr8Up89AP3qdOGADhy2Xr0yfKhhlabILf0uoREbkB9XupYn1V6SOArlDz4eC4Ve08oZa2IXB5Y5soiHQG7f3uP78L62dR%2F8WqocDmwAuJQAXHbWQzz2KTrTHQIFhycXGeqQQYMpdJk95YJ2YAOYFtn9796iP%2FkmQffXNISpvh3YBAGyP%2FpGGsezIvc4molf8zh%2BPDS2QxezXQcNIc1qEgDkKT%2FxOYP5e3u48IBvG685lE5XTCvP%2B82j09Uolp4E%2Fi%2BHtsSl7k2coE6ahYHeuMHEtpX2mBi%2FF0WOwtH5lfdmKa80QIZeOnEa2GQiMn%2F6MNaFnb0GOqUBVsp7Dcd%2FGc0dOVseo5gpOio6hBMVL1UOczk%2BRkuLOlUm14ehHkgFADyf0a5gafdXyCErzuKCzXctVuhoM%2B5CvsnhictaRlA4I5CCptZjJB6GgVXJKpoYkCcK6rDsjPvZFY44hHoOYB2quFbHP01%2B%2BmrtnLWrHcZP7B%2BapoUxebz4JlH8k94QyfN7aww8NjenWKpEW3MEK%2FYJBSG72Ftul6l5MaHc&X-Amz-Signature=d1031663f2a26807fb5374fcfa1322f4177a19e4f56d0ace2090993a4cbd0aeb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TRXN2OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHskKMJyFzbD6WunhVDwY7S60rVKwkjBqi0%2FHv14LFo2AiEAmb%2FFCLcEYpxj2fjQt8cu21hb1hg%2BocHSmerjXlH%2FD%2BMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJBHU8acMIjq%2FdfBQSrcA9FNuqLZH297CxIZL8C8WEmuUqJEnUBhqJJeC5qV6y0gRPS%2FqKp0J4roNS0m%2FwQIypaSAoOwGLPpcaoyOSwnKXBTC5Q1W0kNKDiCp8emSHzeSBCogzPrHoHAPEDqUCWK6gW%2F24FyzEErY%2B3%2BnN97WGAwTdJrC7o7y3jk5G1JXjowqXTGAhw5GWahBZ4DsU3lhOGdDWXdfYH3pp5g1Mu%2FqePyR%2ByZdwBhR%2FW3krS84deeenPZWGmHi3AUEGsls1F%2FsRRic68MySKQr6Yfja597z0YF58FmrU9RMk4KMYSzJE3Z7DSZaKyDCwwJA7%2F8Zr8Up89AP3qdOGADhy2Xr0yfKhhlabILf0uoREbkB9XupYn1V6SOArlDz4eC4Ve08oZa2IXB5Y5soiHQG7f3uP78L62dR%2F8WqocDmwAuJQAXHbWQzz2KTrTHQIFhycXGeqQQYMpdJk95YJ2YAOYFtn9796iP%2FkmQffXNISpvh3YBAGyP%2FpGGsezIvc4molf8zh%2BPDS2QxezXQcNIc1qEgDkKT%2FxOYP5e3u48IBvG685lE5XTCvP%2B82j09Uolp4E%2Fi%2BHtsSl7k2coE6ahYHeuMHEtpX2mBi%2FF0WOwtH5lfdmKa80QIZeOnEa2GQiMn%2F6MNaFnb0GOqUBVsp7Dcd%2FGc0dOVseo5gpOio6hBMVL1UOczk%2BRkuLOlUm14ehHkgFADyf0a5gafdXyCErzuKCzXctVuhoM%2B5CvsnhictaRlA4I5CCptZjJB6GgVXJKpoYkCcK6rDsjPvZFY44hHoOYB2quFbHP01%2B%2BmrtnLWrHcZP7B%2BapoUxebz4JlH8k94QyfN7aww8NjenWKpEW3MEK%2FYJBSG72Ftul6l5MaHc&X-Amz-Signature=5a8147fcda55ff59a113bf11879e3d34f3076e3de88857396a627b4e1b7952a9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TRXN2OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHskKMJyFzbD6WunhVDwY7S60rVKwkjBqi0%2FHv14LFo2AiEAmb%2FFCLcEYpxj2fjQt8cu21hb1hg%2BocHSmerjXlH%2FD%2BMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJBHU8acMIjq%2FdfBQSrcA9FNuqLZH297CxIZL8C8WEmuUqJEnUBhqJJeC5qV6y0gRPS%2FqKp0J4roNS0m%2FwQIypaSAoOwGLPpcaoyOSwnKXBTC5Q1W0kNKDiCp8emSHzeSBCogzPrHoHAPEDqUCWK6gW%2F24FyzEErY%2B3%2BnN97WGAwTdJrC7o7y3jk5G1JXjowqXTGAhw5GWahBZ4DsU3lhOGdDWXdfYH3pp5g1Mu%2FqePyR%2ByZdwBhR%2FW3krS84deeenPZWGmHi3AUEGsls1F%2FsRRic68MySKQr6Yfja597z0YF58FmrU9RMk4KMYSzJE3Z7DSZaKyDCwwJA7%2F8Zr8Up89AP3qdOGADhy2Xr0yfKhhlabILf0uoREbkB9XupYn1V6SOArlDz4eC4Ve08oZa2IXB5Y5soiHQG7f3uP78L62dR%2F8WqocDmwAuJQAXHbWQzz2KTrTHQIFhycXGeqQQYMpdJk95YJ2YAOYFtn9796iP%2FkmQffXNISpvh3YBAGyP%2FpGGsezIvc4molf8zh%2BPDS2QxezXQcNIc1qEgDkKT%2FxOYP5e3u48IBvG685lE5XTCvP%2B82j09Uolp4E%2Fi%2BHtsSl7k2coE6ahYHeuMHEtpX2mBi%2FF0WOwtH5lfdmKa80QIZeOnEa2GQiMn%2F6MNaFnb0GOqUBVsp7Dcd%2FGc0dOVseo5gpOio6hBMVL1UOczk%2BRkuLOlUm14ehHkgFADyf0a5gafdXyCErzuKCzXctVuhoM%2B5CvsnhictaRlA4I5CCptZjJB6GgVXJKpoYkCcK6rDsjPvZFY44hHoOYB2quFbHP01%2B%2BmrtnLWrHcZP7B%2BapoUxebz4JlH8k94QyfN7aww8NjenWKpEW3MEK%2FYJBSG72Ftul6l5MaHc&X-Amz-Signature=8e7fbce9ec285a446f77dfdca12f2751bbc3f9d1ee5ac7a0fd108c28aba9cf04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TRXN2OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHskKMJyFzbD6WunhVDwY7S60rVKwkjBqi0%2FHv14LFo2AiEAmb%2FFCLcEYpxj2fjQt8cu21hb1hg%2BocHSmerjXlH%2FD%2BMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJBHU8acMIjq%2FdfBQSrcA9FNuqLZH297CxIZL8C8WEmuUqJEnUBhqJJeC5qV6y0gRPS%2FqKp0J4roNS0m%2FwQIypaSAoOwGLPpcaoyOSwnKXBTC5Q1W0kNKDiCp8emSHzeSBCogzPrHoHAPEDqUCWK6gW%2F24FyzEErY%2B3%2BnN97WGAwTdJrC7o7y3jk5G1JXjowqXTGAhw5GWahBZ4DsU3lhOGdDWXdfYH3pp5g1Mu%2FqePyR%2ByZdwBhR%2FW3krS84deeenPZWGmHi3AUEGsls1F%2FsRRic68MySKQr6Yfja597z0YF58FmrU9RMk4KMYSzJE3Z7DSZaKyDCwwJA7%2F8Zr8Up89AP3qdOGADhy2Xr0yfKhhlabILf0uoREbkB9XupYn1V6SOArlDz4eC4Ve08oZa2IXB5Y5soiHQG7f3uP78L62dR%2F8WqocDmwAuJQAXHbWQzz2KTrTHQIFhycXGeqQQYMpdJk95YJ2YAOYFtn9796iP%2FkmQffXNISpvh3YBAGyP%2FpGGsezIvc4molf8zh%2BPDS2QxezXQcNIc1qEgDkKT%2FxOYP5e3u48IBvG685lE5XTCvP%2B82j09Uolp4E%2Fi%2BHtsSl7k2coE6ahYHeuMHEtpX2mBi%2FF0WOwtH5lfdmKa80QIZeOnEa2GQiMn%2F6MNaFnb0GOqUBVsp7Dcd%2FGc0dOVseo5gpOio6hBMVL1UOczk%2BRkuLOlUm14ehHkgFADyf0a5gafdXyCErzuKCzXctVuhoM%2B5CvsnhictaRlA4I5CCptZjJB6GgVXJKpoYkCcK6rDsjPvZFY44hHoOYB2quFbHP01%2B%2BmrtnLWrHcZP7B%2BapoUxebz4JlH8k94QyfN7aww8NjenWKpEW3MEK%2FYJBSG72Ftul6l5MaHc&X-Amz-Signature=bfaba88a0cda371a63465eb9f692d77e2463e81bac0403f47c5c96c4fd26fb53&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TRXN2OP%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHskKMJyFzbD6WunhVDwY7S60rVKwkjBqi0%2FHv14LFo2AiEAmb%2FFCLcEYpxj2fjQt8cu21hb1hg%2BocHSmerjXlH%2FD%2BMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJBHU8acMIjq%2FdfBQSrcA9FNuqLZH297CxIZL8C8WEmuUqJEnUBhqJJeC5qV6y0gRPS%2FqKp0J4roNS0m%2FwQIypaSAoOwGLPpcaoyOSwnKXBTC5Q1W0kNKDiCp8emSHzeSBCogzPrHoHAPEDqUCWK6gW%2F24FyzEErY%2B3%2BnN97WGAwTdJrC7o7y3jk5G1JXjowqXTGAhw5GWahBZ4DsU3lhOGdDWXdfYH3pp5g1Mu%2FqePyR%2ByZdwBhR%2FW3krS84deeenPZWGmHi3AUEGsls1F%2FsRRic68MySKQr6Yfja597z0YF58FmrU9RMk4KMYSzJE3Z7DSZaKyDCwwJA7%2F8Zr8Up89AP3qdOGADhy2Xr0yfKhhlabILf0uoREbkB9XupYn1V6SOArlDz4eC4Ve08oZa2IXB5Y5soiHQG7f3uP78L62dR%2F8WqocDmwAuJQAXHbWQzz2KTrTHQIFhycXGeqQQYMpdJk95YJ2YAOYFtn9796iP%2FkmQffXNISpvh3YBAGyP%2FpGGsezIvc4molf8zh%2BPDS2QxezXQcNIc1qEgDkKT%2FxOYP5e3u48IBvG685lE5XTCvP%2B82j09Uolp4E%2Fi%2BHtsSl7k2coE6ahYHeuMHEtpX2mBi%2FF0WOwtH5lfdmKa80QIZeOnEa2GQiMn%2F6MNaFnb0GOqUBVsp7Dcd%2FGc0dOVseo5gpOio6hBMVL1UOczk%2BRkuLOlUm14ehHkgFADyf0a5gafdXyCErzuKCzXctVuhoM%2B5CvsnhictaRlA4I5CCptZjJB6GgVXJKpoYkCcK6rDsjPvZFY44hHoOYB2quFbHP01%2B%2BmrtnLWrHcZP7B%2BapoUxebz4JlH8k94QyfN7aww8NjenWKpEW3MEK%2FYJBSG72Ftul6l5MaHc&X-Amz-Signature=6477623e73bfe3ed2cde503e13d1a8fbc0e1ba992e8e9cc51dd9bac3b1b901fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664A4ZKSZ5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQC76JWFuJ%2FzCAGQ1Ce7CC3har9EYBVFgoLECNSCnAH63QIhANYY4vP8MXQsNsAj66y0GA6%2B%2BMfAgED0vnzi1yIGzOyjKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvMsNLlpgeF0tdUjoq3AP0bEBQyDY0glboqbtiYWFHd%2F3MLpn6UG4EDDcSizKRmSZ6rMrSfHOdzFX5J0ZwIrPnREUZAcJP6cDPBSBBwgyWoABISRGQ7xiZfYsNN2Uo%2BdIUxELFzFqZFhH8Jd6NyJqFPo2dmhYeaW0kSGWI9EPwZFmAnIRhmbJaOjawHTHxw6DtWSkoFtpVzdzr3AuWU71ZD3NRIcTBjR8kAHH5mgo0lblLKNnT7gAMaSpIM8u%2FxyKsO%2BOzwBjgyTLKOYldHYClxpNGrCfUhLajuMei0TO%2BRVx8dTmPMvhVrkeVmi95Gcxedo6s%2Br5VfkAv%2Ffis1XHaQxja3uGq7FXfgbiuIx6xiHeTGMy9CdeQbO7m6uKKL7xNGrD3oWQZU%2FoKxKmokPSjbn2iXMl1Mk00ZrIwJIy23RHwFYAh%2BaILV7L143aptfV7Ai3MJdvSKkxHHaIBKBJ%2FWYazNlO5wwm2hxDrz8w2bfHItjem2vZXL7mpOBL2o5IoVpkqUydmU0PhHIxN%2FP6PHNqROTYVH0Fc%2FVXUimuTsLqUpVpj%2FsG%2FmvKTUtroL8VuQg3mDmArsQDJYHwEoW6f1WpVln8I3D9JOK9F1GAIh50HucGegVEwzWYIksedyfSI3sbQ1qC8A8dnYjCMhp29BjqkAQjmVRXftBOguqsRhEMoIYWtdSImYO0b8d2QuXHDmu0GfzyR8CtFYRjIEWo1hHrz3wyxAdFHrjcm3LkD2%2BSDZmqB2Ghq840vsHo1cwqHyL4hnZRusorNIS%2BI7mLz19TGMXIPuzP%2BxsM6UjWnl4LvE9wninz%2BgUIJ2NLQ00umrU9xt%2B%2Bxaewkbe%2FeymbRChttP6apwUt51PhtrV4pU0YxvlpvDS5R&X-Amz-Signature=e81003e1d123a27a0991561948d14d2d1510e29f675cb6f909f1cb3505e338a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5SXSSRD%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQC8crjjz1DqMFTGMT%2FJPdk29s5n2v3ZjGv3GZMrROR0ZQIgKM%2BXGvzYGrCR4px7fg8cG3baZOml8d7DC7eNxPaMsoEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHHYPW7ezqKPJa2WyrcA6X9Tdsy8y%2FYRJVpQTvTpXQyK2zTdwjhxf%2FaH8SlWKa5a%2BaVMTfmIwsXjxruJKxbsYl28SNSoKbgLtVwqEr%2F%2FlKYs36HqI5905m%2FurDQU73ma6ruCZKsLqXIOhBVBWip5e%2Fz5MZT1VOYqHx6GyS2ce20d%2BhKwq8lXfeH4a1QXvRSnuuWEmb44JlDwPePIIqMSC1A6KuVucVxH2uubXRBl2Lv1rOc9O2Gpt0DG4Mx97beU3LmcAKw6RcAElhoZRAMAYEssM0zh6FXxhI8TIlFR3hP00m7AWvI%2FWD1vRWPqFflThq86BHQLIimX9VIlr9CMaAgUmBpO7wGyUp6BOy4zDLtjLcfRFSu5RRfW3rEsY%2Fn4bJ1ZbTT3sCh25Pc9L69NVL2mx%2B%2FYJ%2FyGLuNihnhW4X6gdjeN4BJ77jVqorGiR3y%2BrMQhBEPyG2%2FM1h8fJhRjMXHNH4OSiJxUQWoOfBjc27z20r5Fc2Yg8jBjEO3nqf8EIFC4JyPPuGWpOY9AMydSloHrZ2U%2BviVnSTyGeAyFYByqhcRiD%2FTlYq4eGcZLCWHtI3nVaweq4mnC6V9Z4skuz0Jk92id6YZfc2SZq%2BqfmnNxw5ePN4wVeJMyN6B49PuWYPzCsQ8NkUcG%2Fo8MPyEnb0GOqUB9bW360MhVoUNQkdjigppTz5c50uf3iX0QGVOCO0XsBQLyDMgFv0EdFy5SYvQfuf7JOPpFqTS1Z%2FV0FAP8XSIhXj8gjm8Mr6ZnIB%2Bh%2BHw1svUG7ilDWfpilRLuFEi%2BYgh5smnDp4I0ExWlVZd%2FdaWgPOD%2BpwVpX0Ui9g3yrhTa1vKr4SgvnsXXhfuUABfV0Fi04R%2BvIKgWTyS2ezJOcv8ImTKkKcY&X-Amz-Signature=e5ada6cb2808f49ba1adcc4c6a0667cb92c6edac6477bbed624c73459d5246da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GSHJT4J%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDjdCtZ1Dseb%2FM6cc8drAakJqOLnMmsf3M82ZzSdHXxsgIgbtpRvTfnw7A4nbxldeO8RMrWArdKFM7N49WrpUBOYesqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHJWZsd4%2BFtDlHjCircA6aAZMoTMyOSCU%2FqBoXN23ArpJhtSS1AMh%2BHAh8F58saEeMqmL3rKrzI9dG%2BABJhv3sT9%2FCRClKhWeqDZp7URSd0aQ08WINXy0f72Pl97%2Fh4%2FdpCNPXkKfG3b9Z350a7wyYbP0qBPH0zbunjq97rR94Ji%2FGYOp2NGHKp4JunaBQWWVqxpIdGaKdJiK6u0WbLgiQmXdGAIawga0yHVhKY%2FwIzTa2N5W7ESaHyvN4BqQ6opMTvPo6M7%2Flple2twJqj9ZCpxSPB6lkJfPRm3P%2FK0w1ysx%2BTO8iMWWlrdkuBAl49TA0RnuODhmIdXhPC9lZFybvG04U%2FCA20Wo7iorsFSYgEUdBpOwjQc1z1xk1SkaR49%2FPb62B5%2BtP4L5dQsCxTbFxMkLM0gtMcObelkHghSKs2hKqkhLpeLtheKPKSTctO2euK8rGYza093%2FYj0OP8IvhQw32aejIK%2BFp9bsWRLNjjZBYjUtMYrhp1gs50IDmSPWIW9ydsSiolGvNDM0ZtOuUq6VC6zPf2u%2FPECLG7%2BZSaBM7hmb%2B4HSjqDM2yn2b2VytoEdOuV5zi2tAX1X9Go6EBsvUcNE%2BV4q7FCO7pt5H8cxFGeC9v5AF90pX52IclWIoQGyy2lMo9XRYPMKmFnb0GOqUBLblkC9Cuz6aMYP1i9XJK%2F6TjlufzIeccc97OMIFe1YLuan2PkQQ0bs4MWnvdjWiUe26Ap%2FbvmVx2VunziAq6C5mO7h3c8o7KGl2k7EF2qGojt1ozNcAT%2BPZxFu1x8seLdiqb4gqA%2F5oNgp3RalFGugcoEad7caBpBJS6E3aKSL8xBIXQubN%2B1V8eGX1oywrwQXPb%2By8IICnxHIieI%2Fq%2Bd75AO5%2FO&X-Amz-Signature=71e0c081f2d539f77727739a3401fa45da87fb8ea6f64629a85bade5b54fdf30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GSHJT4J%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDjdCtZ1Dseb%2FM6cc8drAakJqOLnMmsf3M82ZzSdHXxsgIgbtpRvTfnw7A4nbxldeO8RMrWArdKFM7N49WrpUBOYesqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFHJWZsd4%2BFtDlHjCircA6aAZMoTMyOSCU%2FqBoXN23ArpJhtSS1AMh%2BHAh8F58saEeMqmL3rKrzI9dG%2BABJhv3sT9%2FCRClKhWeqDZp7URSd0aQ08WINXy0f72Pl97%2Fh4%2FdpCNPXkKfG3b9Z350a7wyYbP0qBPH0zbunjq97rR94Ji%2FGYOp2NGHKp4JunaBQWWVqxpIdGaKdJiK6u0WbLgiQmXdGAIawga0yHVhKY%2FwIzTa2N5W7ESaHyvN4BqQ6opMTvPo6M7%2Flple2twJqj9ZCpxSPB6lkJfPRm3P%2FK0w1ysx%2BTO8iMWWlrdkuBAl49TA0RnuODhmIdXhPC9lZFybvG04U%2FCA20Wo7iorsFSYgEUdBpOwjQc1z1xk1SkaR49%2FPb62B5%2BtP4L5dQsCxTbFxMkLM0gtMcObelkHghSKs2hKqkhLpeLtheKPKSTctO2euK8rGYza093%2FYj0OP8IvhQw32aejIK%2BFp9bsWRLNjjZBYjUtMYrhp1gs50IDmSPWIW9ydsSiolGvNDM0ZtOuUq6VC6zPf2u%2FPECLG7%2BZSaBM7hmb%2B4HSjqDM2yn2b2VytoEdOuV5zi2tAX1X9Go6EBsvUcNE%2BV4q7FCO7pt5H8cxFGeC9v5AF90pX52IclWIoQGyy2lMo9XRYPMKmFnb0GOqUBLblkC9Cuz6aMYP1i9XJK%2F6TjlufzIeccc97OMIFe1YLuan2PkQQ0bs4MWnvdjWiUe26Ap%2FbvmVx2VunziAq6C5mO7h3c8o7KGl2k7EF2qGojt1ozNcAT%2BPZxFu1x8seLdiqb4gqA%2F5oNgp3RalFGugcoEad7caBpBJS6E3aKSL8xBIXQubN%2B1V8eGX1oywrwQXPb%2By8IICnxHIieI%2Fq%2Bd75AO5%2FO&X-Amz-Signature=d95738c2733f90d126c097e73c08068980dc986d85bf75914e28f0fe227bafb8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
