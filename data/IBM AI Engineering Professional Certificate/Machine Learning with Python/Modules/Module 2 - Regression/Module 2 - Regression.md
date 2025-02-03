

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSWEIKHU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHlJFzyCRLJB2VgUoUOINyAoWwT7QzBbCSufqwED8U%2FVAiEA0Biu1pIptn9jry5mnKmX2jg7MOn0GlqAZBj3kpAWGV8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkDlsm2scHqC2p7uircA7gkalh77lCxNIEanEEKhXL4Xu3zN0cJmWtjEr2xaL%2BMBvoxjvfxyvdYSponbpNrbJ7s%2FoKzaSUXukXdkjJREuU%2Bz9n6%2FA8nWoZ3vAdazefRhaUTpIAilzto6XSapRx%2FWOn%2BibkxBrD4%2FdonZbo1zfI%2FuQPTkDBSHofUiITDwht5Y%2FrGbIfo2GX9KUxx5ErGOUzyApJpeyRe5uq41QxO%2FJmiLKCv%2BERdN%2FujIW4I2Lb0%2FLjfjnGtkApNZkeQ53egPijWXckcfqX9mPteDsPKkBSgaiTx345dC6Aqn%2BU3dpQlBX%2FYaH0W%2FhFIMvUgRsWSmeeuWOXy3qVvqGCv6CoUh4Z1ZUyk8hOLFwI0A1p41NLJI44Uiaqi3RIFQ5ZTX%2F3K3qdF3g2dXcLDVOh1Mv8R1w6bBnoNj%2FRgW1oRzA7PGYG2idZbZbLmfhVhvhdsKR8CL8qJdXxxcmjOr3%2FdoNF8vOqgS5o%2Fc2TPHTZKI88QYT6tXSn9dcXy%2BpW2erCW3GEt1xOJpbUn%2FhG0Xcmh8%2FVMekRnMMbLUOZDA%2BmWrdbq5tEnqGpX3l8KSqSVcjReyFVewj%2BLMEFOifFF3a0HvE4865BOo0PB6ZmYFjojbLw9CJGFVlGF6yyoufTiK2ezMNLk%2F7wGOqUBdq96Z2kjX%2BVsd007JOcWC9xMCW2wVITd8E3QzHelvDxM5TvFnFtlgzIZpCEGXOFzbgVIHDMdSRZFFxEzgM%2FdrJ1Cbq8DyjyMotpvPeFBjWiVN0DcrbRA%2Bs6Y75ZW3%2FqiFScgyf%2FOANKTYkP9XZknXtb30l3%2BDPqf9F3Ta49I2NP%2B9YeYJnDER1v%2F1BCkkU9%2BveRXQmbqPS5HLZG968C3R0mW%2BwS7&X-Amz-Signature=5b9ea3074363e0891e71cf88f6a1157fa571079de3e253fec6951e5148b2f313&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSWEIKHU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHlJFzyCRLJB2VgUoUOINyAoWwT7QzBbCSufqwED8U%2FVAiEA0Biu1pIptn9jry5mnKmX2jg7MOn0GlqAZBj3kpAWGV8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkDlsm2scHqC2p7uircA7gkalh77lCxNIEanEEKhXL4Xu3zN0cJmWtjEr2xaL%2BMBvoxjvfxyvdYSponbpNrbJ7s%2FoKzaSUXukXdkjJREuU%2Bz9n6%2FA8nWoZ3vAdazefRhaUTpIAilzto6XSapRx%2FWOn%2BibkxBrD4%2FdonZbo1zfI%2FuQPTkDBSHofUiITDwht5Y%2FrGbIfo2GX9KUxx5ErGOUzyApJpeyRe5uq41QxO%2FJmiLKCv%2BERdN%2FujIW4I2Lb0%2FLjfjnGtkApNZkeQ53egPijWXckcfqX9mPteDsPKkBSgaiTx345dC6Aqn%2BU3dpQlBX%2FYaH0W%2FhFIMvUgRsWSmeeuWOXy3qVvqGCv6CoUh4Z1ZUyk8hOLFwI0A1p41NLJI44Uiaqi3RIFQ5ZTX%2F3K3qdF3g2dXcLDVOh1Mv8R1w6bBnoNj%2FRgW1oRzA7PGYG2idZbZbLmfhVhvhdsKR8CL8qJdXxxcmjOr3%2FdoNF8vOqgS5o%2Fc2TPHTZKI88QYT6tXSn9dcXy%2BpW2erCW3GEt1xOJpbUn%2FhG0Xcmh8%2FVMekRnMMbLUOZDA%2BmWrdbq5tEnqGpX3l8KSqSVcjReyFVewj%2BLMEFOifFF3a0HvE4865BOo0PB6ZmYFjojbLw9CJGFVlGF6yyoufTiK2ezMNLk%2F7wGOqUBdq96Z2kjX%2BVsd007JOcWC9xMCW2wVITd8E3QzHelvDxM5TvFnFtlgzIZpCEGXOFzbgVIHDMdSRZFFxEzgM%2FdrJ1Cbq8DyjyMotpvPeFBjWiVN0DcrbRA%2Bs6Y75ZW3%2FqiFScgyf%2FOANKTYkP9XZknXtb30l3%2BDPqf9F3Ta49I2NP%2B9YeYJnDER1v%2F1BCkkU9%2BveRXQmbqPS5HLZG968C3R0mW%2BwS7&X-Amz-Signature=70cf9f5e7126291f1039dd0faef7cb7fcd08b86ceb5c96a43552dd5497c1c58a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSWEIKHU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHlJFzyCRLJB2VgUoUOINyAoWwT7QzBbCSufqwED8U%2FVAiEA0Biu1pIptn9jry5mnKmX2jg7MOn0GlqAZBj3kpAWGV8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkDlsm2scHqC2p7uircA7gkalh77lCxNIEanEEKhXL4Xu3zN0cJmWtjEr2xaL%2BMBvoxjvfxyvdYSponbpNrbJ7s%2FoKzaSUXukXdkjJREuU%2Bz9n6%2FA8nWoZ3vAdazefRhaUTpIAilzto6XSapRx%2FWOn%2BibkxBrD4%2FdonZbo1zfI%2FuQPTkDBSHofUiITDwht5Y%2FrGbIfo2GX9KUxx5ErGOUzyApJpeyRe5uq41QxO%2FJmiLKCv%2BERdN%2FujIW4I2Lb0%2FLjfjnGtkApNZkeQ53egPijWXckcfqX9mPteDsPKkBSgaiTx345dC6Aqn%2BU3dpQlBX%2FYaH0W%2FhFIMvUgRsWSmeeuWOXy3qVvqGCv6CoUh4Z1ZUyk8hOLFwI0A1p41NLJI44Uiaqi3RIFQ5ZTX%2F3K3qdF3g2dXcLDVOh1Mv8R1w6bBnoNj%2FRgW1oRzA7PGYG2idZbZbLmfhVhvhdsKR8CL8qJdXxxcmjOr3%2FdoNF8vOqgS5o%2Fc2TPHTZKI88QYT6tXSn9dcXy%2BpW2erCW3GEt1xOJpbUn%2FhG0Xcmh8%2FVMekRnMMbLUOZDA%2BmWrdbq5tEnqGpX3l8KSqSVcjReyFVewj%2BLMEFOifFF3a0HvE4865BOo0PB6ZmYFjojbLw9CJGFVlGF6yyoufTiK2ezMNLk%2F7wGOqUBdq96Z2kjX%2BVsd007JOcWC9xMCW2wVITd8E3QzHelvDxM5TvFnFtlgzIZpCEGXOFzbgVIHDMdSRZFFxEzgM%2FdrJ1Cbq8DyjyMotpvPeFBjWiVN0DcrbRA%2Bs6Y75ZW3%2FqiFScgyf%2FOANKTYkP9XZknXtb30l3%2BDPqf9F3Ta49I2NP%2B9YeYJnDER1v%2F1BCkkU9%2BveRXQmbqPS5HLZG968C3R0mW%2BwS7&X-Amz-Signature=f6a9d2796d31ac204bc0f1557ae878bef268a3f82ee768b0f0aee1dbbafc1a4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSWEIKHU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHlJFzyCRLJB2VgUoUOINyAoWwT7QzBbCSufqwED8U%2FVAiEA0Biu1pIptn9jry5mnKmX2jg7MOn0GlqAZBj3kpAWGV8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkDlsm2scHqC2p7uircA7gkalh77lCxNIEanEEKhXL4Xu3zN0cJmWtjEr2xaL%2BMBvoxjvfxyvdYSponbpNrbJ7s%2FoKzaSUXukXdkjJREuU%2Bz9n6%2FA8nWoZ3vAdazefRhaUTpIAilzto6XSapRx%2FWOn%2BibkxBrD4%2FdonZbo1zfI%2FuQPTkDBSHofUiITDwht5Y%2FrGbIfo2GX9KUxx5ErGOUzyApJpeyRe5uq41QxO%2FJmiLKCv%2BERdN%2FujIW4I2Lb0%2FLjfjnGtkApNZkeQ53egPijWXckcfqX9mPteDsPKkBSgaiTx345dC6Aqn%2BU3dpQlBX%2FYaH0W%2FhFIMvUgRsWSmeeuWOXy3qVvqGCv6CoUh4Z1ZUyk8hOLFwI0A1p41NLJI44Uiaqi3RIFQ5ZTX%2F3K3qdF3g2dXcLDVOh1Mv8R1w6bBnoNj%2FRgW1oRzA7PGYG2idZbZbLmfhVhvhdsKR8CL8qJdXxxcmjOr3%2FdoNF8vOqgS5o%2Fc2TPHTZKI88QYT6tXSn9dcXy%2BpW2erCW3GEt1xOJpbUn%2FhG0Xcmh8%2FVMekRnMMbLUOZDA%2BmWrdbq5tEnqGpX3l8KSqSVcjReyFVewj%2BLMEFOifFF3a0HvE4865BOo0PB6ZmYFjojbLw9CJGFVlGF6yyoufTiK2ezMNLk%2F7wGOqUBdq96Z2kjX%2BVsd007JOcWC9xMCW2wVITd8E3QzHelvDxM5TvFnFtlgzIZpCEGXOFzbgVIHDMdSRZFFxEzgM%2FdrJ1Cbq8DyjyMotpvPeFBjWiVN0DcrbRA%2Bs6Y75ZW3%2FqiFScgyf%2FOANKTYkP9XZknXtb30l3%2BDPqf9F3Ta49I2NP%2B9YeYJnDER1v%2F1BCkkU9%2BveRXQmbqPS5HLZG968C3R0mW%2BwS7&X-Amz-Signature=7582a059bca4286fb1d59fc5198145a45bc41763c5a00977e39db3956cb86a15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSWEIKHU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHlJFzyCRLJB2VgUoUOINyAoWwT7QzBbCSufqwED8U%2FVAiEA0Biu1pIptn9jry5mnKmX2jg7MOn0GlqAZBj3kpAWGV8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkDlsm2scHqC2p7uircA7gkalh77lCxNIEanEEKhXL4Xu3zN0cJmWtjEr2xaL%2BMBvoxjvfxyvdYSponbpNrbJ7s%2FoKzaSUXukXdkjJREuU%2Bz9n6%2FA8nWoZ3vAdazefRhaUTpIAilzto6XSapRx%2FWOn%2BibkxBrD4%2FdonZbo1zfI%2FuQPTkDBSHofUiITDwht5Y%2FrGbIfo2GX9KUxx5ErGOUzyApJpeyRe5uq41QxO%2FJmiLKCv%2BERdN%2FujIW4I2Lb0%2FLjfjnGtkApNZkeQ53egPijWXckcfqX9mPteDsPKkBSgaiTx345dC6Aqn%2BU3dpQlBX%2FYaH0W%2FhFIMvUgRsWSmeeuWOXy3qVvqGCv6CoUh4Z1ZUyk8hOLFwI0A1p41NLJI44Uiaqi3RIFQ5ZTX%2F3K3qdF3g2dXcLDVOh1Mv8R1w6bBnoNj%2FRgW1oRzA7PGYG2idZbZbLmfhVhvhdsKR8CL8qJdXxxcmjOr3%2FdoNF8vOqgS5o%2Fc2TPHTZKI88QYT6tXSn9dcXy%2BpW2erCW3GEt1xOJpbUn%2FhG0Xcmh8%2FVMekRnMMbLUOZDA%2BmWrdbq5tEnqGpX3l8KSqSVcjReyFVewj%2BLMEFOifFF3a0HvE4865BOo0PB6ZmYFjojbLw9CJGFVlGF6yyoufTiK2ezMNLk%2F7wGOqUBdq96Z2kjX%2BVsd007JOcWC9xMCW2wVITd8E3QzHelvDxM5TvFnFtlgzIZpCEGXOFzbgVIHDMdSRZFFxEzgM%2FdrJ1Cbq8DyjyMotpvPeFBjWiVN0DcrbRA%2Bs6Y75ZW3%2FqiFScgyf%2FOANKTYkP9XZknXtb30l3%2BDPqf9F3Ta49I2NP%2B9YeYJnDER1v%2F1BCkkU9%2BveRXQmbqPS5HLZG968C3R0mW%2BwS7&X-Amz-Signature=9bcba7fb20df75dc273c4a1180e6020e01810e31e97640321c59b1807eb3950c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSWEIKHU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHlJFzyCRLJB2VgUoUOINyAoWwT7QzBbCSufqwED8U%2FVAiEA0Biu1pIptn9jry5mnKmX2jg7MOn0GlqAZBj3kpAWGV8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkDlsm2scHqC2p7uircA7gkalh77lCxNIEanEEKhXL4Xu3zN0cJmWtjEr2xaL%2BMBvoxjvfxyvdYSponbpNrbJ7s%2FoKzaSUXukXdkjJREuU%2Bz9n6%2FA8nWoZ3vAdazefRhaUTpIAilzto6XSapRx%2FWOn%2BibkxBrD4%2FdonZbo1zfI%2FuQPTkDBSHofUiITDwht5Y%2FrGbIfo2GX9KUxx5ErGOUzyApJpeyRe5uq41QxO%2FJmiLKCv%2BERdN%2FujIW4I2Lb0%2FLjfjnGtkApNZkeQ53egPijWXckcfqX9mPteDsPKkBSgaiTx345dC6Aqn%2BU3dpQlBX%2FYaH0W%2FhFIMvUgRsWSmeeuWOXy3qVvqGCv6CoUh4Z1ZUyk8hOLFwI0A1p41NLJI44Uiaqi3RIFQ5ZTX%2F3K3qdF3g2dXcLDVOh1Mv8R1w6bBnoNj%2FRgW1oRzA7PGYG2idZbZbLmfhVhvhdsKR8CL8qJdXxxcmjOr3%2FdoNF8vOqgS5o%2Fc2TPHTZKI88QYT6tXSn9dcXy%2BpW2erCW3GEt1xOJpbUn%2FhG0Xcmh8%2FVMekRnMMbLUOZDA%2BmWrdbq5tEnqGpX3l8KSqSVcjReyFVewj%2BLMEFOifFF3a0HvE4865BOo0PB6ZmYFjojbLw9CJGFVlGF6yyoufTiK2ezMNLk%2F7wGOqUBdq96Z2kjX%2BVsd007JOcWC9xMCW2wVITd8E3QzHelvDxM5TvFnFtlgzIZpCEGXOFzbgVIHDMdSRZFFxEzgM%2FdrJ1Cbq8DyjyMotpvPeFBjWiVN0DcrbRA%2Bs6Y75ZW3%2FqiFScgyf%2FOANKTYkP9XZknXtb30l3%2BDPqf9F3Ta49I2NP%2B9YeYJnDER1v%2F1BCkkU9%2BveRXQmbqPS5HLZG968C3R0mW%2BwS7&X-Amz-Signature=cb6694c96970ea243458a8f5138dcde362304230a1b6c373c5f1fc7b73b9c041&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSWEIKHU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHlJFzyCRLJB2VgUoUOINyAoWwT7QzBbCSufqwED8U%2FVAiEA0Biu1pIptn9jry5mnKmX2jg7MOn0GlqAZBj3kpAWGV8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkDlsm2scHqC2p7uircA7gkalh77lCxNIEanEEKhXL4Xu3zN0cJmWtjEr2xaL%2BMBvoxjvfxyvdYSponbpNrbJ7s%2FoKzaSUXukXdkjJREuU%2Bz9n6%2FA8nWoZ3vAdazefRhaUTpIAilzto6XSapRx%2FWOn%2BibkxBrD4%2FdonZbo1zfI%2FuQPTkDBSHofUiITDwht5Y%2FrGbIfo2GX9KUxx5ErGOUzyApJpeyRe5uq41QxO%2FJmiLKCv%2BERdN%2FujIW4I2Lb0%2FLjfjnGtkApNZkeQ53egPijWXckcfqX9mPteDsPKkBSgaiTx345dC6Aqn%2BU3dpQlBX%2FYaH0W%2FhFIMvUgRsWSmeeuWOXy3qVvqGCv6CoUh4Z1ZUyk8hOLFwI0A1p41NLJI44Uiaqi3RIFQ5ZTX%2F3K3qdF3g2dXcLDVOh1Mv8R1w6bBnoNj%2FRgW1oRzA7PGYG2idZbZbLmfhVhvhdsKR8CL8qJdXxxcmjOr3%2FdoNF8vOqgS5o%2Fc2TPHTZKI88QYT6tXSn9dcXy%2BpW2erCW3GEt1xOJpbUn%2FhG0Xcmh8%2FVMekRnMMbLUOZDA%2BmWrdbq5tEnqGpX3l8KSqSVcjReyFVewj%2BLMEFOifFF3a0HvE4865BOo0PB6ZmYFjojbLw9CJGFVlGF6yyoufTiK2ezMNLk%2F7wGOqUBdq96Z2kjX%2BVsd007JOcWC9xMCW2wVITd8E3QzHelvDxM5TvFnFtlgzIZpCEGXOFzbgVIHDMdSRZFFxEzgM%2FdrJ1Cbq8DyjyMotpvPeFBjWiVN0DcrbRA%2Bs6Y75ZW3%2FqiFScgyf%2FOANKTYkP9XZknXtb30l3%2BDPqf9F3Ta49I2NP%2B9YeYJnDER1v%2F1BCkkU9%2BveRXQmbqPS5HLZG968C3R0mW%2BwS7&X-Amz-Signature=d96610f57df4b29944bc6ffeec39d4b15b99aea87e4dd09d75cbefc7dd9a4125&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSWEIKHU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHlJFzyCRLJB2VgUoUOINyAoWwT7QzBbCSufqwED8U%2FVAiEA0Biu1pIptn9jry5mnKmX2jg7MOn0GlqAZBj3kpAWGV8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkDlsm2scHqC2p7uircA7gkalh77lCxNIEanEEKhXL4Xu3zN0cJmWtjEr2xaL%2BMBvoxjvfxyvdYSponbpNrbJ7s%2FoKzaSUXukXdkjJREuU%2Bz9n6%2FA8nWoZ3vAdazefRhaUTpIAilzto6XSapRx%2FWOn%2BibkxBrD4%2FdonZbo1zfI%2FuQPTkDBSHofUiITDwht5Y%2FrGbIfo2GX9KUxx5ErGOUzyApJpeyRe5uq41QxO%2FJmiLKCv%2BERdN%2FujIW4I2Lb0%2FLjfjnGtkApNZkeQ53egPijWXckcfqX9mPteDsPKkBSgaiTx345dC6Aqn%2BU3dpQlBX%2FYaH0W%2FhFIMvUgRsWSmeeuWOXy3qVvqGCv6CoUh4Z1ZUyk8hOLFwI0A1p41NLJI44Uiaqi3RIFQ5ZTX%2F3K3qdF3g2dXcLDVOh1Mv8R1w6bBnoNj%2FRgW1oRzA7PGYG2idZbZbLmfhVhvhdsKR8CL8qJdXxxcmjOr3%2FdoNF8vOqgS5o%2Fc2TPHTZKI88QYT6tXSn9dcXy%2BpW2erCW3GEt1xOJpbUn%2FhG0Xcmh8%2FVMekRnMMbLUOZDA%2BmWrdbq5tEnqGpX3l8KSqSVcjReyFVewj%2BLMEFOifFF3a0HvE4865BOo0PB6ZmYFjojbLw9CJGFVlGF6yyoufTiK2ezMNLk%2F7wGOqUBdq96Z2kjX%2BVsd007JOcWC9xMCW2wVITd8E3QzHelvDxM5TvFnFtlgzIZpCEGXOFzbgVIHDMdSRZFFxEzgM%2FdrJ1Cbq8DyjyMotpvPeFBjWiVN0DcrbRA%2Bs6Y75ZW3%2FqiFScgyf%2FOANKTYkP9XZknXtb30l3%2BDPqf9F3Ta49I2NP%2B9YeYJnDER1v%2F1BCkkU9%2BveRXQmbqPS5HLZG968C3R0mW%2BwS7&X-Amz-Signature=2d47beb7f2b96ebdcc47e274c48bf13e550c72fcd617d053c8d4d9c2670fcb90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675YEPOVQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBkT3FKk1G3Vnu3EMnWzrIJS2z5Gf41qLF%2F5lTWP%2Bh%2FxAiAM8MBDf6x4J%2BSRSCjTHoxd2wAG52mNyyvAn9ib0U%2FdNCqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2nHO482RsTvEZE9TKtwD57JzJoeLQprlcpGBmrHzYWtUaNqEONnnvC26Vn9deDsdLqyVOQgupPxFy6CdiIYtvT0mbPR84VQr0%2Bgb7HGM9RS8qQi%2FZav46fzYvy23nkEePsQrT8LqHje9jMk35qFrY4jqN75Md1C1%2Fhhw%2BJ1HXNS6IthgO7Z2bXm%2BwEazNxMMRvI9AaWjyI%2F1jg2%2Bu3l2PyKjGGXgoatmnrgZFLCZXDvPUSmpX2s81T8SQ74RiYwXaE7SBvnclGf3coK2GTXAHiRnRTHwpWtMU67MEtp6FNQB9meHQVE3Q53h8aa2TqN%2Bcf%2BlS%2BLpwTAvtTz52odt2qnK2MhjhjeqL6vjb2b%2FAhQICWKxYlknuL5QgnVcmaj3dGw4HfkFv3PMWx0egngPX0GzBd%2F%2BpeFMrLlDfZsr%2FN7JAx1dibfO3qPVvwdX8CptooVyUp4U02Nib1SVV5M2TAu1IPG%2FDIjk9u3BpLZxyHY0903RXzKO9PpwFVICSUAChs2xarFqLmr5avxiaU26OK%2BJn5PEh%2BdLMTQ5z3%2FqXJ5Bnd37T4UcAJYq4iBKIVIUagYatgHH%2BgggU60vIgTdlGE%2B2BOxo%2FVLJHsalKNJbjcJIOk%2FDl82FtVltBa3aGk8aJr6CCKK5jEMl3cwh%2BX%2FvAY6pgEhfRnsph25iFvblOlx6Wn3RhNoLNYJqNhumZMWHCrwUM7T3nH%2FKNJorFNRpMz90XAEzV8ebqKBaSd4HYBB%2BKzEydfh1d2O5sCwgtaR3e7M6q%2B3fRIUw%2BMH3Qe%2Bp45Ca76E4W08OaI6E4OUkbu2SPurAkGJjuAjElthydmF2AYFP3KU%2BRwJ%2BiT46XnxNtnvqKnpDli0pctf2EqLk5LvGWiCGVtAlzYk&X-Amz-Signature=0567e81c3d3a32fc8d1abd98844a2d47cfcfdfe6c5a4a30b82cb1e1feed2b92a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZLRWWXN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIATVtWZjAsSPPKdW8MGoUcCVrO6X%2FepDJQ3sHgC5684QAiEAw3WFEWaNC62x%2BGW%2FYkchOuBjELlLzjcaUHAWUii0HrgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyX3dVGznAElGR0XCrcA%2FoiTgm3yPq1hriFlxZ0Ujy6meqbG4i5ivr3Cj6cFDsLXRaodWtFG61q1oP8Z2fAr0X%2B3Gygc4hCId1UBqO%2FsQDKpOR62u5s13VheF8PlMTsN6mHLfcceo5kB%2FBgNkRz91aJxf3IxpxW17GJWkX6kK6qn0NS9CUV36U6fccxKEArr3Awl4WW%2FF1zoQnl4y%2BnOunRycSxvtFC2hKnYvurrHgRhj54u5BwLpk9UX%2BEQF7SawoRQCNv368xyOGSho4dMMJ4pB2%2FBWdAcdRw8yfzP3iMC34cPTfmQvRKzYKodt%2FYLYqrkX7jD%2FgFhbyMoCmIQJt0Q5DsTxELKRUseuP%2FJjCSHF2E1x7ckUr3iu%2F8WL0c3lNK0FdahcjaRfEegeY8YdBzwW6ag%2FsaCBEeO9N39cR6V53O44fNB7LqkOhptFK9GakVPWBWbxTy8t9xt6RgT7TsVxZerMFmnLPq7dkgg5QuiJ8hYwd2aPm2XORJbGEtgwIjWtoonccFV8fkTS2mPwM5Pz5ZJEP7mGWpxzttB2XmtSJeTdmIA8S%2BhwTMnhTst5BJ2M5CJu8ygEie5qZ5UUr%2FupAlNmNebe7BJsnTLfgv6GuNeAUsZ2fMA1lvubUegIQpNLO5R1IIz2ofMKXk%2F7wGOqUBySTBEu%2BV7HD16sXmIMSabAiOnfMTVS2BX2ImFaROXBjxq2Tig1eerQmZsTZtqv8MYbaedI0u2xNzIDZfWYzSiNNsojrQTyqIcxVM%2B6bauSShkF8VtsFwPtNV67SCNp2nVFr1FChoVQm83%2BtayPDlmhTJwzC9U4hDkNngAJ2pe0PJmumxoxzofBwL3fTm3zwk9dsXA3OnRfZLhoJZtNr6nbmGyuZ%2F&X-Amz-Signature=1b6bfba1b74f75890f9091ac4daaf77f32c8daffb8143b1a2b738e2a7447d4eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YT4V5OB5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAs83%2BbRwbxXT76DRrkm5yLoSXL%2FxCy1KFXlQRYZbawAAiEAmGqSo1yGXCRoLD8lfoZAEQazyzftY1jbxYle4b4LCwsqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBFyZZcnpn4njPnAEircA%2FLa28gTywdyBq75nm%2B2aKaX%2BsjCRsIlvlWMOeLdgaKzxJ%2ByDVwP98HiCxh4pbsrSNr7bE1ozF4MYGsKwEDDzyOVJnHan7AzxWKfsubX8kkDP%2BznGqbwrhfu7WVzo2VXAxLfh9SVW2L1w54k0UU9cqxeksAubYigyEsBoB7V8cVr%2BKLzZ9sZF%2BsevN7nRprGSPjKJlXwbmH2ZQyN7wKHcP1J9j5scJr%2BSuoKBV5Hho6Tw61y9PQz9dVbmVyoXnyQ3J3oRZafULmfK4vzlDth6uVAG7QfLCX2Wd2Tm7nrVPxdg5KCaJYib13UwWhopHcloqGL4Yh37wJhntQyhZ1KgV6%2FV1JjADgiX6MKGqV8etk%2FRdY%2B1TmHoZ9Z5Dgof3wIXbPuL0knN8TrXWYnH30ujAs05K4g8qEX7T1cYtoPLK4m4P1ToBrdX0nNZMrKVdRFaoLY6Dsi%2FoZy3OPmuia1o7edvHV%2BygN8%2FPaL95oS7Of%2BU%2B5g4emGEytT9HrblODdHFD4xhOLxuzVupD6PjIIuLKxVb7qQAhQkuiRTCINQSLg1bbkHC%2BIMQcZxz43%2BGLibP9MnDmBIsEz3GpqzeNnirsnLc2JhJUtcWGwxCyxenV5hP5daCE8s0xAkfLwMJ3k%2F7wGOqUBOOE2ojJr0C6JVGeBDwiphoTx6Kw3ugPdBS5k0E4lXoHXOWIZWrz4j8eBigz1W3eTYynGy%2FzZ3vWt3bvqsMwFbGC34VkRd19u%2FoedQMt%2F%2BYDGUuApb6CFCG0uAmFmweSkiSpAkR%2B%2FcPVHz7LQ8jYQwVd29RqgPe9WejQFV0GpdIX3PQ6BRq7qlfQhwOTJk5iptaDBxTQGjM25VL3QaP4mka0Cd0Wo&X-Amz-Signature=7dab2b8ff5708b88361f57ef6d54ffd34bdc9a99b2fe1f95fdd834e842bb627c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YT4V5OB5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAs83%2BbRwbxXT76DRrkm5yLoSXL%2FxCy1KFXlQRYZbawAAiEAmGqSo1yGXCRoLD8lfoZAEQazyzftY1jbxYle4b4LCwsqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBFyZZcnpn4njPnAEircA%2FLa28gTywdyBq75nm%2B2aKaX%2BsjCRsIlvlWMOeLdgaKzxJ%2ByDVwP98HiCxh4pbsrSNr7bE1ozF4MYGsKwEDDzyOVJnHan7AzxWKfsubX8kkDP%2BznGqbwrhfu7WVzo2VXAxLfh9SVW2L1w54k0UU9cqxeksAubYigyEsBoB7V8cVr%2BKLzZ9sZF%2BsevN7nRprGSPjKJlXwbmH2ZQyN7wKHcP1J9j5scJr%2BSuoKBV5Hho6Tw61y9PQz9dVbmVyoXnyQ3J3oRZafULmfK4vzlDth6uVAG7QfLCX2Wd2Tm7nrVPxdg5KCaJYib13UwWhopHcloqGL4Yh37wJhntQyhZ1KgV6%2FV1JjADgiX6MKGqV8etk%2FRdY%2B1TmHoZ9Z5Dgof3wIXbPuL0knN8TrXWYnH30ujAs05K4g8qEX7T1cYtoPLK4m4P1ToBrdX0nNZMrKVdRFaoLY6Dsi%2FoZy3OPmuia1o7edvHV%2BygN8%2FPaL95oS7Of%2BU%2B5g4emGEytT9HrblODdHFD4xhOLxuzVupD6PjIIuLKxVb7qQAhQkuiRTCINQSLg1bbkHC%2BIMQcZxz43%2BGLibP9MnDmBIsEz3GpqzeNnirsnLc2JhJUtcWGwxCyxenV5hP5daCE8s0xAkfLwMJ3k%2F7wGOqUBOOE2ojJr0C6JVGeBDwiphoTx6Kw3ugPdBS5k0E4lXoHXOWIZWrz4j8eBigz1W3eTYynGy%2FzZ3vWt3bvqsMwFbGC34VkRd19u%2FoedQMt%2F%2BYDGUuApb6CFCG0uAmFmweSkiSpAkR%2B%2FcPVHz7LQ8jYQwVd29RqgPe9WejQFV0GpdIX3PQ6BRq7qlfQhwOTJk5iptaDBxTQGjM25VL3QaP4mka0Cd0Wo&X-Amz-Signature=e57318fbadc5803cbbd3612dc97cdeac94774aef2c836236a2ff294d73d563e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
