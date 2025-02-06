

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAXLPHCD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIDVQt92RkkzZVa0FnR0eoZRFaPBXGMBAYa%2BG97BUVEBrAiEAuatBeOmLPKf0U1svRR9HegH5%2B1Fqk1LJporvt%2FchniYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGPD3ur8ZApuA7cNWCrcAy%2F76L%2FSiPN8VTWyQXYaxyvIFJoOHLKwhe0JW%2FuhpX1x7BLh4fPDF%2BRwLySGGRNRaaMRwoFfdwHitnzLIDe2hD5qnhkHJzEHFm8yFnkhk8wBlwSENc7hkKZ1%2BncaBykj6KfKWpwp2wItt1fPUtACnze1AK8GRz8VJYiWdV4m7F2fRUImC2cJuySaVU99Mx7JgsbpVr3KGcaPNI6yn5BLNAK1oZd2t99QBtuHj%2F%2FayAZqq03yU2LL6WWGUNk5Sp5P771Z9QwHlRIItxeTiQT4TUQDJxhRSWlqRF9tLIcn7uWHmBvoBmXvL5kfFVbMSu0I9N624%2FCt4PzdOumfBKZwPqGAE6ervFWPVQ1XjXgyDxzTgV0Lzu%2BosG42vOsMavDRTgI28nCzBj62qlIKOeE9PbqneD4aUDR0poYmPaGkhv328vrTVMreXZb3WsV%2F9oPrPYXyeqgdsiRdleOy0QLhSwC119LbWafj3F4orsR3%2FZM8Xrc2FJBLsACnpnBSMO2%2Bzqf%2F8t5YLGw05VnpHSdLiLycdjM07ytOr807zqKa3cPmN9x2cAbXrHRv6ryWtGwDquSffgTo8uRWFvZWYa0hS1QxQwnl8uJTBVNzBGcurKHz9LDbdL%2BVMjQ8dS%2FLMMbRk70GOqUBTCfMM5Jf4N6F6450Cd2z1ndi5QTXF9%2F0B5QE7e7qJ%2Bw%2FYKQQw6Pbz26rLjhba%2BY7lI6aP5jxmZLzW0a6548YctxuNE5ncAth78%2BBqSXxYO8LHOGOMeMHZfpk551zZ642GBgsM4mLgUBGjQ3QOAuUihI9hZ6AKAcLrqHbrFQ9UGUDV4elJVJVMVCWRvUQsQgtNIYHryCJS1OozwUTLWs4ebYtop1P&X-Amz-Signature=1b3f2553d4ebfa9a85dad05e3c2ea90e897bafa611d0c0aa72b5d0041778d28f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAXLPHCD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIDVQt92RkkzZVa0FnR0eoZRFaPBXGMBAYa%2BG97BUVEBrAiEAuatBeOmLPKf0U1svRR9HegH5%2B1Fqk1LJporvt%2FchniYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGPD3ur8ZApuA7cNWCrcAy%2F76L%2FSiPN8VTWyQXYaxyvIFJoOHLKwhe0JW%2FuhpX1x7BLh4fPDF%2BRwLySGGRNRaaMRwoFfdwHitnzLIDe2hD5qnhkHJzEHFm8yFnkhk8wBlwSENc7hkKZ1%2BncaBykj6KfKWpwp2wItt1fPUtACnze1AK8GRz8VJYiWdV4m7F2fRUImC2cJuySaVU99Mx7JgsbpVr3KGcaPNI6yn5BLNAK1oZd2t99QBtuHj%2F%2FayAZqq03yU2LL6WWGUNk5Sp5P771Z9QwHlRIItxeTiQT4TUQDJxhRSWlqRF9tLIcn7uWHmBvoBmXvL5kfFVbMSu0I9N624%2FCt4PzdOumfBKZwPqGAE6ervFWPVQ1XjXgyDxzTgV0Lzu%2BosG42vOsMavDRTgI28nCzBj62qlIKOeE9PbqneD4aUDR0poYmPaGkhv328vrTVMreXZb3WsV%2F9oPrPYXyeqgdsiRdleOy0QLhSwC119LbWafj3F4orsR3%2FZM8Xrc2FJBLsACnpnBSMO2%2Bzqf%2F8t5YLGw05VnpHSdLiLycdjM07ytOr807zqKa3cPmN9x2cAbXrHRv6ryWtGwDquSffgTo8uRWFvZWYa0hS1QxQwnl8uJTBVNzBGcurKHz9LDbdL%2BVMjQ8dS%2FLMMbRk70GOqUBTCfMM5Jf4N6F6450Cd2z1ndi5QTXF9%2F0B5QE7e7qJ%2Bw%2FYKQQw6Pbz26rLjhba%2BY7lI6aP5jxmZLzW0a6548YctxuNE5ncAth78%2BBqSXxYO8LHOGOMeMHZfpk551zZ642GBgsM4mLgUBGjQ3QOAuUihI9hZ6AKAcLrqHbrFQ9UGUDV4elJVJVMVCWRvUQsQgtNIYHryCJS1OozwUTLWs4ebYtop1P&X-Amz-Signature=45d4e0143b8588f0a69f32896770ac1cbe26f99286e5c4754f71ee391628b2ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAXLPHCD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIDVQt92RkkzZVa0FnR0eoZRFaPBXGMBAYa%2BG97BUVEBrAiEAuatBeOmLPKf0U1svRR9HegH5%2B1Fqk1LJporvt%2FchniYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGPD3ur8ZApuA7cNWCrcAy%2F76L%2FSiPN8VTWyQXYaxyvIFJoOHLKwhe0JW%2FuhpX1x7BLh4fPDF%2BRwLySGGRNRaaMRwoFfdwHitnzLIDe2hD5qnhkHJzEHFm8yFnkhk8wBlwSENc7hkKZ1%2BncaBykj6KfKWpwp2wItt1fPUtACnze1AK8GRz8VJYiWdV4m7F2fRUImC2cJuySaVU99Mx7JgsbpVr3KGcaPNI6yn5BLNAK1oZd2t99QBtuHj%2F%2FayAZqq03yU2LL6WWGUNk5Sp5P771Z9QwHlRIItxeTiQT4TUQDJxhRSWlqRF9tLIcn7uWHmBvoBmXvL5kfFVbMSu0I9N624%2FCt4PzdOumfBKZwPqGAE6ervFWPVQ1XjXgyDxzTgV0Lzu%2BosG42vOsMavDRTgI28nCzBj62qlIKOeE9PbqneD4aUDR0poYmPaGkhv328vrTVMreXZb3WsV%2F9oPrPYXyeqgdsiRdleOy0QLhSwC119LbWafj3F4orsR3%2FZM8Xrc2FJBLsACnpnBSMO2%2Bzqf%2F8t5YLGw05VnpHSdLiLycdjM07ytOr807zqKa3cPmN9x2cAbXrHRv6ryWtGwDquSffgTo8uRWFvZWYa0hS1QxQwnl8uJTBVNzBGcurKHz9LDbdL%2BVMjQ8dS%2FLMMbRk70GOqUBTCfMM5Jf4N6F6450Cd2z1ndi5QTXF9%2F0B5QE7e7qJ%2Bw%2FYKQQw6Pbz26rLjhba%2BY7lI6aP5jxmZLzW0a6548YctxuNE5ncAth78%2BBqSXxYO8LHOGOMeMHZfpk551zZ642GBgsM4mLgUBGjQ3QOAuUihI9hZ6AKAcLrqHbrFQ9UGUDV4elJVJVMVCWRvUQsQgtNIYHryCJS1OozwUTLWs4ebYtop1P&X-Amz-Signature=18b6e9433d60005b4d564b785b63aaa78097774785c0a291e25c7a1336e4aa1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAXLPHCD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIDVQt92RkkzZVa0FnR0eoZRFaPBXGMBAYa%2BG97BUVEBrAiEAuatBeOmLPKf0U1svRR9HegH5%2B1Fqk1LJporvt%2FchniYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGPD3ur8ZApuA7cNWCrcAy%2F76L%2FSiPN8VTWyQXYaxyvIFJoOHLKwhe0JW%2FuhpX1x7BLh4fPDF%2BRwLySGGRNRaaMRwoFfdwHitnzLIDe2hD5qnhkHJzEHFm8yFnkhk8wBlwSENc7hkKZ1%2BncaBykj6KfKWpwp2wItt1fPUtACnze1AK8GRz8VJYiWdV4m7F2fRUImC2cJuySaVU99Mx7JgsbpVr3KGcaPNI6yn5BLNAK1oZd2t99QBtuHj%2F%2FayAZqq03yU2LL6WWGUNk5Sp5P771Z9QwHlRIItxeTiQT4TUQDJxhRSWlqRF9tLIcn7uWHmBvoBmXvL5kfFVbMSu0I9N624%2FCt4PzdOumfBKZwPqGAE6ervFWPVQ1XjXgyDxzTgV0Lzu%2BosG42vOsMavDRTgI28nCzBj62qlIKOeE9PbqneD4aUDR0poYmPaGkhv328vrTVMreXZb3WsV%2F9oPrPYXyeqgdsiRdleOy0QLhSwC119LbWafj3F4orsR3%2FZM8Xrc2FJBLsACnpnBSMO2%2Bzqf%2F8t5YLGw05VnpHSdLiLycdjM07ytOr807zqKa3cPmN9x2cAbXrHRv6ryWtGwDquSffgTo8uRWFvZWYa0hS1QxQwnl8uJTBVNzBGcurKHz9LDbdL%2BVMjQ8dS%2FLMMbRk70GOqUBTCfMM5Jf4N6F6450Cd2z1ndi5QTXF9%2F0B5QE7e7qJ%2Bw%2FYKQQw6Pbz26rLjhba%2BY7lI6aP5jxmZLzW0a6548YctxuNE5ncAth78%2BBqSXxYO8LHOGOMeMHZfpk551zZ642GBgsM4mLgUBGjQ3QOAuUihI9hZ6AKAcLrqHbrFQ9UGUDV4elJVJVMVCWRvUQsQgtNIYHryCJS1OozwUTLWs4ebYtop1P&X-Amz-Signature=da3a94fb74934bf20cc745a58cc747f226e32e0548cc90f4d0b623fad26ee534&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAXLPHCD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIDVQt92RkkzZVa0FnR0eoZRFaPBXGMBAYa%2BG97BUVEBrAiEAuatBeOmLPKf0U1svRR9HegH5%2B1Fqk1LJporvt%2FchniYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGPD3ur8ZApuA7cNWCrcAy%2F76L%2FSiPN8VTWyQXYaxyvIFJoOHLKwhe0JW%2FuhpX1x7BLh4fPDF%2BRwLySGGRNRaaMRwoFfdwHitnzLIDe2hD5qnhkHJzEHFm8yFnkhk8wBlwSENc7hkKZ1%2BncaBykj6KfKWpwp2wItt1fPUtACnze1AK8GRz8VJYiWdV4m7F2fRUImC2cJuySaVU99Mx7JgsbpVr3KGcaPNI6yn5BLNAK1oZd2t99QBtuHj%2F%2FayAZqq03yU2LL6WWGUNk5Sp5P771Z9QwHlRIItxeTiQT4TUQDJxhRSWlqRF9tLIcn7uWHmBvoBmXvL5kfFVbMSu0I9N624%2FCt4PzdOumfBKZwPqGAE6ervFWPVQ1XjXgyDxzTgV0Lzu%2BosG42vOsMavDRTgI28nCzBj62qlIKOeE9PbqneD4aUDR0poYmPaGkhv328vrTVMreXZb3WsV%2F9oPrPYXyeqgdsiRdleOy0QLhSwC119LbWafj3F4orsR3%2FZM8Xrc2FJBLsACnpnBSMO2%2Bzqf%2F8t5YLGw05VnpHSdLiLycdjM07ytOr807zqKa3cPmN9x2cAbXrHRv6ryWtGwDquSffgTo8uRWFvZWYa0hS1QxQwnl8uJTBVNzBGcurKHz9LDbdL%2BVMjQ8dS%2FLMMbRk70GOqUBTCfMM5Jf4N6F6450Cd2z1ndi5QTXF9%2F0B5QE7e7qJ%2Bw%2FYKQQw6Pbz26rLjhba%2BY7lI6aP5jxmZLzW0a6548YctxuNE5ncAth78%2BBqSXxYO8LHOGOMeMHZfpk551zZ642GBgsM4mLgUBGjQ3QOAuUihI9hZ6AKAcLrqHbrFQ9UGUDV4elJVJVMVCWRvUQsQgtNIYHryCJS1OozwUTLWs4ebYtop1P&X-Amz-Signature=fba8a8fc21e5d0addf86b0b78426f0d43e2e195c05778421cb69cae41c171ce9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAXLPHCD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIDVQt92RkkzZVa0FnR0eoZRFaPBXGMBAYa%2BG97BUVEBrAiEAuatBeOmLPKf0U1svRR9HegH5%2B1Fqk1LJporvt%2FchniYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGPD3ur8ZApuA7cNWCrcAy%2F76L%2FSiPN8VTWyQXYaxyvIFJoOHLKwhe0JW%2FuhpX1x7BLh4fPDF%2BRwLySGGRNRaaMRwoFfdwHitnzLIDe2hD5qnhkHJzEHFm8yFnkhk8wBlwSENc7hkKZ1%2BncaBykj6KfKWpwp2wItt1fPUtACnze1AK8GRz8VJYiWdV4m7F2fRUImC2cJuySaVU99Mx7JgsbpVr3KGcaPNI6yn5BLNAK1oZd2t99QBtuHj%2F%2FayAZqq03yU2LL6WWGUNk5Sp5P771Z9QwHlRIItxeTiQT4TUQDJxhRSWlqRF9tLIcn7uWHmBvoBmXvL5kfFVbMSu0I9N624%2FCt4PzdOumfBKZwPqGAE6ervFWPVQ1XjXgyDxzTgV0Lzu%2BosG42vOsMavDRTgI28nCzBj62qlIKOeE9PbqneD4aUDR0poYmPaGkhv328vrTVMreXZb3WsV%2F9oPrPYXyeqgdsiRdleOy0QLhSwC119LbWafj3F4orsR3%2FZM8Xrc2FJBLsACnpnBSMO2%2Bzqf%2F8t5YLGw05VnpHSdLiLycdjM07ytOr807zqKa3cPmN9x2cAbXrHRv6ryWtGwDquSffgTo8uRWFvZWYa0hS1QxQwnl8uJTBVNzBGcurKHz9LDbdL%2BVMjQ8dS%2FLMMbRk70GOqUBTCfMM5Jf4N6F6450Cd2z1ndi5QTXF9%2F0B5QE7e7qJ%2Bw%2FYKQQw6Pbz26rLjhba%2BY7lI6aP5jxmZLzW0a6548YctxuNE5ncAth78%2BBqSXxYO8LHOGOMeMHZfpk551zZ642GBgsM4mLgUBGjQ3QOAuUihI9hZ6AKAcLrqHbrFQ9UGUDV4elJVJVMVCWRvUQsQgtNIYHryCJS1OozwUTLWs4ebYtop1P&X-Amz-Signature=e5cad1d6d38c37aba056883539fe24e5a768f7dc589604b342bac3abc67fd615&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAXLPHCD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIDVQt92RkkzZVa0FnR0eoZRFaPBXGMBAYa%2BG97BUVEBrAiEAuatBeOmLPKf0U1svRR9HegH5%2B1Fqk1LJporvt%2FchniYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGPD3ur8ZApuA7cNWCrcAy%2F76L%2FSiPN8VTWyQXYaxyvIFJoOHLKwhe0JW%2FuhpX1x7BLh4fPDF%2BRwLySGGRNRaaMRwoFfdwHitnzLIDe2hD5qnhkHJzEHFm8yFnkhk8wBlwSENc7hkKZ1%2BncaBykj6KfKWpwp2wItt1fPUtACnze1AK8GRz8VJYiWdV4m7F2fRUImC2cJuySaVU99Mx7JgsbpVr3KGcaPNI6yn5BLNAK1oZd2t99QBtuHj%2F%2FayAZqq03yU2LL6WWGUNk5Sp5P771Z9QwHlRIItxeTiQT4TUQDJxhRSWlqRF9tLIcn7uWHmBvoBmXvL5kfFVbMSu0I9N624%2FCt4PzdOumfBKZwPqGAE6ervFWPVQ1XjXgyDxzTgV0Lzu%2BosG42vOsMavDRTgI28nCzBj62qlIKOeE9PbqneD4aUDR0poYmPaGkhv328vrTVMreXZb3WsV%2F9oPrPYXyeqgdsiRdleOy0QLhSwC119LbWafj3F4orsR3%2FZM8Xrc2FJBLsACnpnBSMO2%2Bzqf%2F8t5YLGw05VnpHSdLiLycdjM07ytOr807zqKa3cPmN9x2cAbXrHRv6ryWtGwDquSffgTo8uRWFvZWYa0hS1QxQwnl8uJTBVNzBGcurKHz9LDbdL%2BVMjQ8dS%2FLMMbRk70GOqUBTCfMM5Jf4N6F6450Cd2z1ndi5QTXF9%2F0B5QE7e7qJ%2Bw%2FYKQQw6Pbz26rLjhba%2BY7lI6aP5jxmZLzW0a6548YctxuNE5ncAth78%2BBqSXxYO8LHOGOMeMHZfpk551zZ642GBgsM4mLgUBGjQ3QOAuUihI9hZ6AKAcLrqHbrFQ9UGUDV4elJVJVMVCWRvUQsQgtNIYHryCJS1OozwUTLWs4ebYtop1P&X-Amz-Signature=77b7d949da4be51c9fa0f02e2b17e77dcc65419e9b5b1ffcb183a0e9b65e8c10&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAXLPHCD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIDVQt92RkkzZVa0FnR0eoZRFaPBXGMBAYa%2BG97BUVEBrAiEAuatBeOmLPKf0U1svRR9HegH5%2B1Fqk1LJporvt%2FchniYq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDGPD3ur8ZApuA7cNWCrcAy%2F76L%2FSiPN8VTWyQXYaxyvIFJoOHLKwhe0JW%2FuhpX1x7BLh4fPDF%2BRwLySGGRNRaaMRwoFfdwHitnzLIDe2hD5qnhkHJzEHFm8yFnkhk8wBlwSENc7hkKZ1%2BncaBykj6KfKWpwp2wItt1fPUtACnze1AK8GRz8VJYiWdV4m7F2fRUImC2cJuySaVU99Mx7JgsbpVr3KGcaPNI6yn5BLNAK1oZd2t99QBtuHj%2F%2FayAZqq03yU2LL6WWGUNk5Sp5P771Z9QwHlRIItxeTiQT4TUQDJxhRSWlqRF9tLIcn7uWHmBvoBmXvL5kfFVbMSu0I9N624%2FCt4PzdOumfBKZwPqGAE6ervFWPVQ1XjXgyDxzTgV0Lzu%2BosG42vOsMavDRTgI28nCzBj62qlIKOeE9PbqneD4aUDR0poYmPaGkhv328vrTVMreXZb3WsV%2F9oPrPYXyeqgdsiRdleOy0QLhSwC119LbWafj3F4orsR3%2FZM8Xrc2FJBLsACnpnBSMO2%2Bzqf%2F8t5YLGw05VnpHSdLiLycdjM07ytOr807zqKa3cPmN9x2cAbXrHRv6ryWtGwDquSffgTo8uRWFvZWYa0hS1QxQwnl8uJTBVNzBGcurKHz9LDbdL%2BVMjQ8dS%2FLMMbRk70GOqUBTCfMM5Jf4N6F6450Cd2z1ndi5QTXF9%2F0B5QE7e7qJ%2Bw%2FYKQQw6Pbz26rLjhba%2BY7lI6aP5jxmZLzW0a6548YctxuNE5ncAth78%2BBqSXxYO8LHOGOMeMHZfpk551zZ642GBgsM4mLgUBGjQ3QOAuUihI9hZ6AKAcLrqHbrFQ9UGUDV4elJVJVMVCWRvUQsQgtNIYHryCJS1OozwUTLWs4ebYtop1P&X-Amz-Signature=1d0f378854dc845d124ed559bdd63364042d44e89b5866bf4e463e115e161b0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF3MLLMJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDwEm2faGhuAq5BBWx0toRPZ1DE13LpPboQRCY32MRaiAiAVfCOK%2FEY6BgUHW8PVCXqKgDQ8yzJGmn4n0uBvTECmGyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMJDtHlACVbP%2FVi%2FBuKtwDlnInW4JBKO%2BN1HpAqy2F7laZCF5SUrs%2FNV9Wlvls3jlTQv7HboRwVk%2BlYrGvRdC0JZOcf5JR6Ns4rmkYh%2B0EcfJbZwsR35gNTLfU3HAVl74%2BGB7ewlYMm%2BfhyvTNtJi1Ei%2FS2NLTRvRQloQ%2Fz87s6Rao5gsCXy%2FzqiOtIA9WAgGpJO8RF%2BXzfNt8rlMTvDDOCQlG0aSYaYLloMpElb4gFzxYJu%2FdO12khpG7kxdkmcw9J8%2BAW4dHh5pmGqOhxpM2ZTZJQawRlHEHg3y80BIH4dhX7%2Fo09O5%2BgEFmKsI%2BfgaZxSRz2K%2BsZocN3BxN0tww2i%2F44Y%2FIAsfDSo9vyVzLq2dE3Xu%2BoJbBztku8rxiYLiavZ3Yqwv7AVSbcXbr5S%2FKBTcWwWaEvGXRZzQZYBl8RzwXwabAHVJiWVFjhMCkLRP4ZcWW3U0ZI3nDy%2BFlLNZdsG4D%2FVeLYxana9sPQDch2IoNFXT2cfdcHNXqiBgQzXLSyxMWrzdEH0A9%2F2rz1kXVgTUpO2RcjBUz9wv%2FOnUxpRWLaOSI%2B8aE7285iJUjNhyG8f9dfsqSzpfrWj6%2FTU7PqsHfv5%2BfKt50yKpX%2BpfdXYR%2F29MN5x2iWBr1PzgktiY3xOzKXFMZ5sIDZpUwltKTvQY6pgGtYbp%2FlynmUWk7RJZXby7we2ikO7kBaxKGlgZIs71lLhpWQQTLwTqnHsQoxa5KGzdKES3NUPxrhGw7TfyJ4uyAmTinGjY5o6NpsfCQyUZ%2Bt24o4SvGpUp6Nnqdw96hmw%2BpQiUqBgVUGJEdVyEpK5nYJ3qJNr0UlY5nio8k1HGVjHFt%2BGGN3owOrr1m7Z4pW9b2M9mIWBdsIyTOKAAD4OcmBjES8Zdy&X-Amz-Signature=33bf07f4b8b1d8f7a3322f54a1e1696212a47a929521978dfe21f86b8d4fbe2e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNVYUBW5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIHyH%2BjS2knsTyauLYYbwrFnOOi6Ta%2B9N4JJPNDOuYXufAiAkUHMpKzT5wILI0C9k%2B%2FINUzD4rYGay24B2m7zQIfC%2Fyr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMpAorvGtwwej1y%2FxDKtwDc48I7Y3OpIlxhLs4cwSPdFBgH6rkNrps0WqnJEDxEv3eD2eQDy24yu4lv46vvq9kGWKzDLHbP4Vgri4EJaGeoj2S0EMFzclGSmkRt8ppFJeC1Wn84Ja7Ljasao3iozKK%2FjMviOZ8gicKp3jfG%2BEkCmngY3%2BTr70v1M7aJY3Y15wH3L3BF7FlCgpfcJxqgvj65Q%2BqRQ1RIK1UHgInohF4K69CAdQj2iLfsGHnMR3vA0XYOiwayHqOkiTBPjjLVf4jQRUfC7xJ3qoeCfkXsCLAFIbPGSsb9%2B9iWgymeNzIsBIBS3KbHMI%2Fp8sVKqwp05ZBfS1bOqJ9H0kdM04%2B%2BOqCEYWHhiJFAfTosZb%2FLD1A%2Fg1sWM7Ae4RKb7Vll%2Fgt4ud08q%2BXUvXpFqdtLNwll76P7IzggkljdS5Hq779CJKfNv3mIV1%2BvA%2B5SvUgZU%2Bx%2Fdzqn3Vw6CdKTs8aZ1WZTakxEk%2FJtRO9kXk%2FugcerfCKiWyz8iBjjoJEu3Vp66ss6BkUhZ12PMblKyfqa6iddrnaEn6O25r0oKTFPzLHwPE%2Be9cr3Mv7yy9yS2txGSWTg3QQ3BHvVyhMpSSpoN7mx6wcdaaKmAtc5usYbMZZ%2FHMOEuPs1D8ByTUQzR2b1%2BMw3NGTvQY6pgG4EjZ2KCmTwDwSiGP%2Brj9zCmGTPZqC4td%2BeUVN1d%2BGKB5IprxEFhwAQiMIh7IDZ9DbMcFGlecgFn2o8nYBCeORag%2BmLZiM%2BqObHnbVoszG6J3Eu3usUptiD3s7boGnYaiJifFCF50PP%2BXuS2YMEXdaY37iAwbNXV%2FX9qFtGVDrDkXoEAsMdHk68dFN9uJLroJJjO%2Fqgu7fPqeEGcp48G2qN7ELD0KQ&X-Amz-Signature=e1ab542ee56728295f0fbbb5994e7785a6246efd7fceccc9ec721c297bbea4bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFWXG77K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDfi2%2F4bcd3w6wYzRvOWroei35pzsKe1k8sFgbS05QVxAiAlUO7QubgwXVMNFjsn5%2BrUoA1%2FDp2DZk%2BYlKqKBXOAlCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMD0Y9PiFYb3iwTGkEKtwDb%2B6aAJfLR8YD8dfjkxffN2ngbD7QyCOWB3vnIIA36r0PYq8NpENAjSR%2B2tgg2Nox72Fg9vsneF6ZP2DXoPclQwK6FIn%2FST2vR9kZ7vdqiXncHMAnCYgig7az1astdNXjuSSGiJE5HLCQT%2FrUzA0T5%2FnQCXtVTf8nDUPOMniSX028WYmkw0ulPGDqQQuPrzhs4K1P4ZoX6WZQoUQdpR6e5vzwOkky7QdATgvPTWyosqLicl%2FDClIaODNg%2B81WtbeCzbPwfY1NMMm%2FyCP27BfKXaWtwtYXrvx2rn37tmReUHHA3ZmWR%2BcSG71mrELItyeYRjTbNKU3pWRh86MIqrVL9mAAvWBLgYEElKnmGqWLChzJHsDGBY6wQD9pH7dzpdarAiNn8MSdKQTaDWebrHDgNKj9BDWk8QwmH%2F5u2pYCJVmPZXg5SiDbUvXtRyV2cXUQAHu%2F16ELhXbnR%2B2bJsUWQbN0JyOwU45L3JHxkXp0LOc6pQELs5hr3m9jo29nSMTJFIXOz2qYIZEKO0lUtopCNyXCCWm5dj9ZmDD5xkaKiLcKSmXbsY1zxnr91UHg%2F6jKIkmSPVRXHSYNsK4yPb4iR1Qc2FoLAFsYMuhZIsTe1E0DWl9R9FXyIjr6LqAwoNGTvQY6pgELL4Dgl5kaDZy7aCB8zx4YVHZ9umWi1ylsMe1Sin%2B50h%2F5rmh0zb0fa%2B3ehgxurjxq3MuF%2FyO8M6Tp%2BZTIlkAgJOBevb8pVJ7HtLl%2BIzHTSkcuQ%2BxQBFZceftfpW%2B6k25uw2PO%2BFXtiouOJ7hzismjmLTKMUTQoU8RyNw4Sa8fRDUscYCYHHzkd6Mvsq2c4bDNgBxbbZMXLOlw7CVaaLelXSj2imrc&X-Amz-Signature=d5d4d59b4e9c58fbb3fad9e0ae6a307eaaf87afd18855ddd973b25723bf59736&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFWXG77K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIDfi2%2F4bcd3w6wYzRvOWroei35pzsKe1k8sFgbS05QVxAiAlUO7QubgwXVMNFjsn5%2BrUoA1%2FDp2DZk%2BYlKqKBXOAlCr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMD0Y9PiFYb3iwTGkEKtwDb%2B6aAJfLR8YD8dfjkxffN2ngbD7QyCOWB3vnIIA36r0PYq8NpENAjSR%2B2tgg2Nox72Fg9vsneF6ZP2DXoPclQwK6FIn%2FST2vR9kZ7vdqiXncHMAnCYgig7az1astdNXjuSSGiJE5HLCQT%2FrUzA0T5%2FnQCXtVTf8nDUPOMniSX028WYmkw0ulPGDqQQuPrzhs4K1P4ZoX6WZQoUQdpR6e5vzwOkky7QdATgvPTWyosqLicl%2FDClIaODNg%2B81WtbeCzbPwfY1NMMm%2FyCP27BfKXaWtwtYXrvx2rn37tmReUHHA3ZmWR%2BcSG71mrELItyeYRjTbNKU3pWRh86MIqrVL9mAAvWBLgYEElKnmGqWLChzJHsDGBY6wQD9pH7dzpdarAiNn8MSdKQTaDWebrHDgNKj9BDWk8QwmH%2F5u2pYCJVmPZXg5SiDbUvXtRyV2cXUQAHu%2F16ELhXbnR%2B2bJsUWQbN0JyOwU45L3JHxkXp0LOc6pQELs5hr3m9jo29nSMTJFIXOz2qYIZEKO0lUtopCNyXCCWm5dj9ZmDD5xkaKiLcKSmXbsY1zxnr91UHg%2F6jKIkmSPVRXHSYNsK4yPb4iR1Qc2FoLAFsYMuhZIsTe1E0DWl9R9FXyIjr6LqAwoNGTvQY6pgELL4Dgl5kaDZy7aCB8zx4YVHZ9umWi1ylsMe1Sin%2B50h%2F5rmh0zb0fa%2B3ehgxurjxq3MuF%2FyO8M6Tp%2BZTIlkAgJOBevb8pVJ7HtLl%2BIzHTSkcuQ%2BxQBFZceftfpW%2B6k25uw2PO%2BFXtiouOJ7hzismjmLTKMUTQoU8RyNw4Sa8fRDUscYCYHHzkd6Mvsq2c4bDNgBxbbZMXLOlw7CVaaLelXSj2imrc&X-Amz-Signature=daf160532e2870f3a5718ba54d69126104c0645646876784634b97fa51dcdb23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
