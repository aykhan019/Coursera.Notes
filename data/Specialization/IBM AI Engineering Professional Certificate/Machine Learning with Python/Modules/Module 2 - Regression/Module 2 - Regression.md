

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSFTK6QE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFN49EWPOH5Q6LTQ0uuJsFDdPAprF3JW0OIpDkvgVmcCAiAR8fjfegSWcD%2BEYIlllkjaTPkgsuownrqVnXn5c%2Fw6tiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxewYmX3HWnR8PWSwKtwDVrDGBtzyXeOqtx3X0x2cb%2Bxbs%2BIs3FiDae7qQw1kcAEd9yie%2FzzC2O6LNHF94LGvgcluU2GNNhCc7LumD%2FF2KOxbMasNGh5N5loVtPGivLQugTRy4uXSrt%2BbLzJ%2F38vzWp1Osoqy56wiSpf7N7O377YKnGDAeEfAFZIhSrquCpIabofg8xBSt4JEMjRpuYy1O1FkUuPkZs8ItA42noX7EsUFNy%2BofbzA6Oi0BsTZi7kf%2FE8QmBH8dvDVgklhNdx99UVPTlpqEQgk5jCNQNETgWidxgxbUlo7Iye8amEXCm%2F%2BwrMLtaA4kD4%2BJB101dayww7EOr6pBx6UMGkCQF1Hk9Uu60lmho9dDKAUXIV%2BqP6alD8Z9cWIf%2BFDEla61BTDq3y3HLni73AJWITJtGIcak2P9D8mgvJ3V1yIm1zq8Y8AH8T%2FvvKPy23YblON9yTxkTd7pSAF%2B7BRGUwkpbcEA3cOEKdN9bc7Dj8RPp%2FO6wsS19WlSejvKQx5xzZmlUYMfZov78lxUKhHZRqA1UD9%2BBXyXbRxT13%2Fe3eVPdmGia5ruWMpGzYSyCE5W00%2Fyo2IZozcTzqzm2TcLZObu%2BHoCQslrZ%2BhQvjJUghrsyy0u1YFxm9dhUwi6SNUBKEw2aLsvAY6pgHGNveE%2B8PCXVCydleF1K9NX4AEEuF254CJ41fQHAw%2Fkd8BOugrUWZ3dH%2Bfi57HTj%2BVOeAAGAR3UtNUWtcQ80Au%2Baba7AEhRhLHFFBKLiuRoUz3vxBXkrhzxOErGlgK9BOnO8OOUnh1UXQ3mNZrjhOwn7Ri0oYo%2FCTeeexu6ZENtiIteu6rqPDV%2F9FkFMxACJZiJdam58phcdAEg2dAhN4f09wrd2jv&X-Amz-Signature=193f9606dce36aebe7200c6404f8df68651d3285be1923f3666bbe409f817bf7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSFTK6QE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFN49EWPOH5Q6LTQ0uuJsFDdPAprF3JW0OIpDkvgVmcCAiAR8fjfegSWcD%2BEYIlllkjaTPkgsuownrqVnXn5c%2Fw6tiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxewYmX3HWnR8PWSwKtwDVrDGBtzyXeOqtx3X0x2cb%2Bxbs%2BIs3FiDae7qQw1kcAEd9yie%2FzzC2O6LNHF94LGvgcluU2GNNhCc7LumD%2FF2KOxbMasNGh5N5loVtPGivLQugTRy4uXSrt%2BbLzJ%2F38vzWp1Osoqy56wiSpf7N7O377YKnGDAeEfAFZIhSrquCpIabofg8xBSt4JEMjRpuYy1O1FkUuPkZs8ItA42noX7EsUFNy%2BofbzA6Oi0BsTZi7kf%2FE8QmBH8dvDVgklhNdx99UVPTlpqEQgk5jCNQNETgWidxgxbUlo7Iye8amEXCm%2F%2BwrMLtaA4kD4%2BJB101dayww7EOr6pBx6UMGkCQF1Hk9Uu60lmho9dDKAUXIV%2BqP6alD8Z9cWIf%2BFDEla61BTDq3y3HLni73AJWITJtGIcak2P9D8mgvJ3V1yIm1zq8Y8AH8T%2FvvKPy23YblON9yTxkTd7pSAF%2B7BRGUwkpbcEA3cOEKdN9bc7Dj8RPp%2FO6wsS19WlSejvKQx5xzZmlUYMfZov78lxUKhHZRqA1UD9%2BBXyXbRxT13%2Fe3eVPdmGia5ruWMpGzYSyCE5W00%2Fyo2IZozcTzqzm2TcLZObu%2BHoCQslrZ%2BhQvjJUghrsyy0u1YFxm9dhUwi6SNUBKEw2aLsvAY6pgHGNveE%2B8PCXVCydleF1K9NX4AEEuF254CJ41fQHAw%2Fkd8BOugrUWZ3dH%2Bfi57HTj%2BVOeAAGAR3UtNUWtcQ80Au%2Baba7AEhRhLHFFBKLiuRoUz3vxBXkrhzxOErGlgK9BOnO8OOUnh1UXQ3mNZrjhOwn7Ri0oYo%2FCTeeexu6ZENtiIteu6rqPDV%2F9FkFMxACJZiJdam58phcdAEg2dAhN4f09wrd2jv&X-Amz-Signature=5d5e8e39a526227035538a6d7c54515c3dd3e6f5125c5f38c8fe2ee50db5157f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSFTK6QE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFN49EWPOH5Q6LTQ0uuJsFDdPAprF3JW0OIpDkvgVmcCAiAR8fjfegSWcD%2BEYIlllkjaTPkgsuownrqVnXn5c%2Fw6tiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxewYmX3HWnR8PWSwKtwDVrDGBtzyXeOqtx3X0x2cb%2Bxbs%2BIs3FiDae7qQw1kcAEd9yie%2FzzC2O6LNHF94LGvgcluU2GNNhCc7LumD%2FF2KOxbMasNGh5N5loVtPGivLQugTRy4uXSrt%2BbLzJ%2F38vzWp1Osoqy56wiSpf7N7O377YKnGDAeEfAFZIhSrquCpIabofg8xBSt4JEMjRpuYy1O1FkUuPkZs8ItA42noX7EsUFNy%2BofbzA6Oi0BsTZi7kf%2FE8QmBH8dvDVgklhNdx99UVPTlpqEQgk5jCNQNETgWidxgxbUlo7Iye8amEXCm%2F%2BwrMLtaA4kD4%2BJB101dayww7EOr6pBx6UMGkCQF1Hk9Uu60lmho9dDKAUXIV%2BqP6alD8Z9cWIf%2BFDEla61BTDq3y3HLni73AJWITJtGIcak2P9D8mgvJ3V1yIm1zq8Y8AH8T%2FvvKPy23YblON9yTxkTd7pSAF%2B7BRGUwkpbcEA3cOEKdN9bc7Dj8RPp%2FO6wsS19WlSejvKQx5xzZmlUYMfZov78lxUKhHZRqA1UD9%2BBXyXbRxT13%2Fe3eVPdmGia5ruWMpGzYSyCE5W00%2Fyo2IZozcTzqzm2TcLZObu%2BHoCQslrZ%2BhQvjJUghrsyy0u1YFxm9dhUwi6SNUBKEw2aLsvAY6pgHGNveE%2B8PCXVCydleF1K9NX4AEEuF254CJ41fQHAw%2Fkd8BOugrUWZ3dH%2Bfi57HTj%2BVOeAAGAR3UtNUWtcQ80Au%2Baba7AEhRhLHFFBKLiuRoUz3vxBXkrhzxOErGlgK9BOnO8OOUnh1UXQ3mNZrjhOwn7Ri0oYo%2FCTeeexu6ZENtiIteu6rqPDV%2F9FkFMxACJZiJdam58phcdAEg2dAhN4f09wrd2jv&X-Amz-Signature=45bb87716be8a8fbac1a43518200de491189313f22258af1a46d6d3a3fb89dcc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSFTK6QE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFN49EWPOH5Q6LTQ0uuJsFDdPAprF3JW0OIpDkvgVmcCAiAR8fjfegSWcD%2BEYIlllkjaTPkgsuownrqVnXn5c%2Fw6tiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxewYmX3HWnR8PWSwKtwDVrDGBtzyXeOqtx3X0x2cb%2Bxbs%2BIs3FiDae7qQw1kcAEd9yie%2FzzC2O6LNHF94LGvgcluU2GNNhCc7LumD%2FF2KOxbMasNGh5N5loVtPGivLQugTRy4uXSrt%2BbLzJ%2F38vzWp1Osoqy56wiSpf7N7O377YKnGDAeEfAFZIhSrquCpIabofg8xBSt4JEMjRpuYy1O1FkUuPkZs8ItA42noX7EsUFNy%2BofbzA6Oi0BsTZi7kf%2FE8QmBH8dvDVgklhNdx99UVPTlpqEQgk5jCNQNETgWidxgxbUlo7Iye8amEXCm%2F%2BwrMLtaA4kD4%2BJB101dayww7EOr6pBx6UMGkCQF1Hk9Uu60lmho9dDKAUXIV%2BqP6alD8Z9cWIf%2BFDEla61BTDq3y3HLni73AJWITJtGIcak2P9D8mgvJ3V1yIm1zq8Y8AH8T%2FvvKPy23YblON9yTxkTd7pSAF%2B7BRGUwkpbcEA3cOEKdN9bc7Dj8RPp%2FO6wsS19WlSejvKQx5xzZmlUYMfZov78lxUKhHZRqA1UD9%2BBXyXbRxT13%2Fe3eVPdmGia5ruWMpGzYSyCE5W00%2Fyo2IZozcTzqzm2TcLZObu%2BHoCQslrZ%2BhQvjJUghrsyy0u1YFxm9dhUwi6SNUBKEw2aLsvAY6pgHGNveE%2B8PCXVCydleF1K9NX4AEEuF254CJ41fQHAw%2Fkd8BOugrUWZ3dH%2Bfi57HTj%2BVOeAAGAR3UtNUWtcQ80Au%2Baba7AEhRhLHFFBKLiuRoUz3vxBXkrhzxOErGlgK9BOnO8OOUnh1UXQ3mNZrjhOwn7Ri0oYo%2FCTeeexu6ZENtiIteu6rqPDV%2F9FkFMxACJZiJdam58phcdAEg2dAhN4f09wrd2jv&X-Amz-Signature=af083a9959c997bf37fe049984f155aad6986264549e201103f15b8aafd604cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSFTK6QE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFN49EWPOH5Q6LTQ0uuJsFDdPAprF3JW0OIpDkvgVmcCAiAR8fjfegSWcD%2BEYIlllkjaTPkgsuownrqVnXn5c%2Fw6tiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxewYmX3HWnR8PWSwKtwDVrDGBtzyXeOqtx3X0x2cb%2Bxbs%2BIs3FiDae7qQw1kcAEd9yie%2FzzC2O6LNHF94LGvgcluU2GNNhCc7LumD%2FF2KOxbMasNGh5N5loVtPGivLQugTRy4uXSrt%2BbLzJ%2F38vzWp1Osoqy56wiSpf7N7O377YKnGDAeEfAFZIhSrquCpIabofg8xBSt4JEMjRpuYy1O1FkUuPkZs8ItA42noX7EsUFNy%2BofbzA6Oi0BsTZi7kf%2FE8QmBH8dvDVgklhNdx99UVPTlpqEQgk5jCNQNETgWidxgxbUlo7Iye8amEXCm%2F%2BwrMLtaA4kD4%2BJB101dayww7EOr6pBx6UMGkCQF1Hk9Uu60lmho9dDKAUXIV%2BqP6alD8Z9cWIf%2BFDEla61BTDq3y3HLni73AJWITJtGIcak2P9D8mgvJ3V1yIm1zq8Y8AH8T%2FvvKPy23YblON9yTxkTd7pSAF%2B7BRGUwkpbcEA3cOEKdN9bc7Dj8RPp%2FO6wsS19WlSejvKQx5xzZmlUYMfZov78lxUKhHZRqA1UD9%2BBXyXbRxT13%2Fe3eVPdmGia5ruWMpGzYSyCE5W00%2Fyo2IZozcTzqzm2TcLZObu%2BHoCQslrZ%2BhQvjJUghrsyy0u1YFxm9dhUwi6SNUBKEw2aLsvAY6pgHGNveE%2B8PCXVCydleF1K9NX4AEEuF254CJ41fQHAw%2Fkd8BOugrUWZ3dH%2Bfi57HTj%2BVOeAAGAR3UtNUWtcQ80Au%2Baba7AEhRhLHFFBKLiuRoUz3vxBXkrhzxOErGlgK9BOnO8OOUnh1UXQ3mNZrjhOwn7Ri0oYo%2FCTeeexu6ZENtiIteu6rqPDV%2F9FkFMxACJZiJdam58phcdAEg2dAhN4f09wrd2jv&X-Amz-Signature=3193ea02ded0e041773245dd651d6b821e4a84706e059a09628f5d11804a3d4b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSFTK6QE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFN49EWPOH5Q6LTQ0uuJsFDdPAprF3JW0OIpDkvgVmcCAiAR8fjfegSWcD%2BEYIlllkjaTPkgsuownrqVnXn5c%2Fw6tiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxewYmX3HWnR8PWSwKtwDVrDGBtzyXeOqtx3X0x2cb%2Bxbs%2BIs3FiDae7qQw1kcAEd9yie%2FzzC2O6LNHF94LGvgcluU2GNNhCc7LumD%2FF2KOxbMasNGh5N5loVtPGivLQugTRy4uXSrt%2BbLzJ%2F38vzWp1Osoqy56wiSpf7N7O377YKnGDAeEfAFZIhSrquCpIabofg8xBSt4JEMjRpuYy1O1FkUuPkZs8ItA42noX7EsUFNy%2BofbzA6Oi0BsTZi7kf%2FE8QmBH8dvDVgklhNdx99UVPTlpqEQgk5jCNQNETgWidxgxbUlo7Iye8amEXCm%2F%2BwrMLtaA4kD4%2BJB101dayww7EOr6pBx6UMGkCQF1Hk9Uu60lmho9dDKAUXIV%2BqP6alD8Z9cWIf%2BFDEla61BTDq3y3HLni73AJWITJtGIcak2P9D8mgvJ3V1yIm1zq8Y8AH8T%2FvvKPy23YblON9yTxkTd7pSAF%2B7BRGUwkpbcEA3cOEKdN9bc7Dj8RPp%2FO6wsS19WlSejvKQx5xzZmlUYMfZov78lxUKhHZRqA1UD9%2BBXyXbRxT13%2Fe3eVPdmGia5ruWMpGzYSyCE5W00%2Fyo2IZozcTzqzm2TcLZObu%2BHoCQslrZ%2BhQvjJUghrsyy0u1YFxm9dhUwi6SNUBKEw2aLsvAY6pgHGNveE%2B8PCXVCydleF1K9NX4AEEuF254CJ41fQHAw%2Fkd8BOugrUWZ3dH%2Bfi57HTj%2BVOeAAGAR3UtNUWtcQ80Au%2Baba7AEhRhLHFFBKLiuRoUz3vxBXkrhzxOErGlgK9BOnO8OOUnh1UXQ3mNZrjhOwn7Ri0oYo%2FCTeeexu6ZENtiIteu6rqPDV%2F9FkFMxACJZiJdam58phcdAEg2dAhN4f09wrd2jv&X-Amz-Signature=609fb12444905db5b7fdfe973beb466d310839b1d127c71e9c7f8d6ff50e360d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSFTK6QE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFN49EWPOH5Q6LTQ0uuJsFDdPAprF3JW0OIpDkvgVmcCAiAR8fjfegSWcD%2BEYIlllkjaTPkgsuownrqVnXn5c%2Fw6tiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxewYmX3HWnR8PWSwKtwDVrDGBtzyXeOqtx3X0x2cb%2Bxbs%2BIs3FiDae7qQw1kcAEd9yie%2FzzC2O6LNHF94LGvgcluU2GNNhCc7LumD%2FF2KOxbMasNGh5N5loVtPGivLQugTRy4uXSrt%2BbLzJ%2F38vzWp1Osoqy56wiSpf7N7O377YKnGDAeEfAFZIhSrquCpIabofg8xBSt4JEMjRpuYy1O1FkUuPkZs8ItA42noX7EsUFNy%2BofbzA6Oi0BsTZi7kf%2FE8QmBH8dvDVgklhNdx99UVPTlpqEQgk5jCNQNETgWidxgxbUlo7Iye8amEXCm%2F%2BwrMLtaA4kD4%2BJB101dayww7EOr6pBx6UMGkCQF1Hk9Uu60lmho9dDKAUXIV%2BqP6alD8Z9cWIf%2BFDEla61BTDq3y3HLni73AJWITJtGIcak2P9D8mgvJ3V1yIm1zq8Y8AH8T%2FvvKPy23YblON9yTxkTd7pSAF%2B7BRGUwkpbcEA3cOEKdN9bc7Dj8RPp%2FO6wsS19WlSejvKQx5xzZmlUYMfZov78lxUKhHZRqA1UD9%2BBXyXbRxT13%2Fe3eVPdmGia5ruWMpGzYSyCE5W00%2Fyo2IZozcTzqzm2TcLZObu%2BHoCQslrZ%2BhQvjJUghrsyy0u1YFxm9dhUwi6SNUBKEw2aLsvAY6pgHGNveE%2B8PCXVCydleF1K9NX4AEEuF254CJ41fQHAw%2Fkd8BOugrUWZ3dH%2Bfi57HTj%2BVOeAAGAR3UtNUWtcQ80Au%2Baba7AEhRhLHFFBKLiuRoUz3vxBXkrhzxOErGlgK9BOnO8OOUnh1UXQ3mNZrjhOwn7Ri0oYo%2FCTeeexu6ZENtiIteu6rqPDV%2F9FkFMxACJZiJdam58phcdAEg2dAhN4f09wrd2jv&X-Amz-Signature=c1d76ce56d24c93787936ce6ffa6ca7eeec7445af4a9ec7a13e4b2b79fac2a75&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSFTK6QE%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFN49EWPOH5Q6LTQ0uuJsFDdPAprF3JW0OIpDkvgVmcCAiAR8fjfegSWcD%2BEYIlllkjaTPkgsuownrqVnXn5c%2Fw6tiqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxewYmX3HWnR8PWSwKtwDVrDGBtzyXeOqtx3X0x2cb%2Bxbs%2BIs3FiDae7qQw1kcAEd9yie%2FzzC2O6LNHF94LGvgcluU2GNNhCc7LumD%2FF2KOxbMasNGh5N5loVtPGivLQugTRy4uXSrt%2BbLzJ%2F38vzWp1Osoqy56wiSpf7N7O377YKnGDAeEfAFZIhSrquCpIabofg8xBSt4JEMjRpuYy1O1FkUuPkZs8ItA42noX7EsUFNy%2BofbzA6Oi0BsTZi7kf%2FE8QmBH8dvDVgklhNdx99UVPTlpqEQgk5jCNQNETgWidxgxbUlo7Iye8amEXCm%2F%2BwrMLtaA4kD4%2BJB101dayww7EOr6pBx6UMGkCQF1Hk9Uu60lmho9dDKAUXIV%2BqP6alD8Z9cWIf%2BFDEla61BTDq3y3HLni73AJWITJtGIcak2P9D8mgvJ3V1yIm1zq8Y8AH8T%2FvvKPy23YblON9yTxkTd7pSAF%2B7BRGUwkpbcEA3cOEKdN9bc7Dj8RPp%2FO6wsS19WlSejvKQx5xzZmlUYMfZov78lxUKhHZRqA1UD9%2BBXyXbRxT13%2Fe3eVPdmGia5ruWMpGzYSyCE5W00%2Fyo2IZozcTzqzm2TcLZObu%2BHoCQslrZ%2BhQvjJUghrsyy0u1YFxm9dhUwi6SNUBKEw2aLsvAY6pgHGNveE%2B8PCXVCydleF1K9NX4AEEuF254CJ41fQHAw%2Fkd8BOugrUWZ3dH%2Bfi57HTj%2BVOeAAGAR3UtNUWtcQ80Au%2Baba7AEhRhLHFFBKLiuRoUz3vxBXkrhzxOErGlgK9BOnO8OOUnh1UXQ3mNZrjhOwn7Ri0oYo%2FCTeeexu6ZENtiIteu6rqPDV%2F9FkFMxACJZiJdam58phcdAEg2dAhN4f09wrd2jv&X-Amz-Signature=a92531b21f8427bacf4bcd36ce41a17bd1198f7ab42a10fa7f7577d1f8123187&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IAO35E7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQDD1zvKKPBcekLneXhFaQ9F165zpS2V9FtaaXS9BcEU7wIfNulfgkOcvwHdnisdrLVPUPs%2FzSXr1C15hUjS1OGqzCqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaXlWQCA%2Bm8bxJBr9KtwD23zkro44CQ3PbBp%2BEHqdSHihMcTkb0%2FXZ2LQN%2Flo8%2BRgnU9Bzx2%2FXmrON81YqdTQI%2BxYAwdVCtzIKoCWWldTXEcMNL5KZ%2BcWhqBPXHWHtT1FswYHfhYdFzzQkaIml3pQOB6xk9zLmzY7Bqeq5Hx4H7sIobHHVqlv7C7AwDwgIZ54vsaYwDR4FVXSMbvFs0fMsT1%2F8hKtNLkTk7Sn%2BWRsC9xxlYKr%2BFtuSHf9fxrE2BgjjH09NdFIU%2FmatchD%2BZJrGmXhQcMttp7kdbJ%2BqmncGI%2FyqGBXbN3TQ1cT4Flv44eoWdXqcLz1y7OW%2BkP1S%2B2W7oLnsttKiylijiyKpJIyh%2BLOv128s%2BmlFQ8Oe2GyX20EWCpEqPl0roih0TCXEurbwGPe30b58CvziQWiIZS9i2LrsBiymWwBxpYjXBAIB%2FfHEJhuUJy0CSIuG6ggZuioEVvEs%2B1fNSIl02Hwn3emX84gt5vC%2FqgkclBAHH4AkNCWqmYirDebxPJw8yv4zLKpxqG%2BoC%2B8aZTU0EvIUcveFRtuyS8NwI%2BX9sR5b7cvYTREhmFK9r0iZ8k2Oe7%2FRrjYEpfjSeCKMkZgQeGJoxUGOvOgPTrPO4hG9IFTXgkMeHuM%2BiwgFtf%2F%2B2RBehgwqqPsvAY6pgGB87EZHYydR0CO%2B4AUZO39yfvWEtXE2LG0irPNU0cl%2B8Tx%2BYkXB7kwRWZBI0W7%2Fw%2FtjEGsjNumdI7DYu1deBR9D7NJ3DS3ezFHSRlvjUOzVVDx%2FGiQq4W9Yhb75JB78cQnaCZvME2OYnV%2BJDW4uHxFwkJFD%2FDXdvjkPJdNT7KfdFRTFQi%2FjucsglJ6Zv4BDaZ77nG9%2FflrVp1hK59nZ6IReuyxe2Ej&X-Amz-Signature=1f759073fa2c032f7c97fb453370297af252781373e8459d8f283d871e6f9daa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DAYA5FR%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGiwRe%2FDaQ7VQoAG6kywG3qDrD8DdYmwvV4hyn5vnADAAiAR5QduLRWUsnc4vhGtUglGHcpwYDxmJVFRp9uANb8L8CqIBAif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyys0uzVbvxjxhTk7KtwDe3Rno6jHubS8Y2dIlo%2F5wCio%2FbNgf4pGklSIG4wiL%2FhDdSp6w8XpoyxL44I55qsRykcVVfFpbpO9gWjps8%2B4AvS0MNGTmLE13MqXZGp3ET88ySNFvjdobw3gesVen8EhqozPuqqu7vvkwyQKnim7xQ4mUm744o3xCi2f%2Bm6lg2mBardbFPakpZJ1S7BXFPBLbDYSVew%2BOy%2BP09pi%2BiDmnsnPTXEjgWzfd6z0V1kFpf8JXWdJpk6rHIrAXc%2BzphKmdG6AI2FrBVAZH4y1vvwwkSHn%2BuwIeFrXOXAXQkWLKEeLsEDcDZ1jWjIbLuUkQCpIM5uZQ0qSOtIztHeeAv15u1pLaRmcxIk57vAsVFP88mnrDXa7TtypVmgBrrk6n45kIbPIOUlBgs%2BfkIbs8BCLddWWFVfduqoHfczDnwSRX9Clsu%2Bb3RZCGrHIsybNoOOXgPrnX5uDg7fweHP11qhHGc4YMGP3x7cw%2FbJN64mrY%2FL%2FSZUTv%2B9XndjrUBENYhSEq%2FRUtDqbLsEYUgptq4AqNXuoIhz3RuClfkUZhYJuzxOCQ%2F6Uqjst5CsnrEAtCctzCEne6IjRu9Sq5BxGtaqJDQPUQr9t2CLLSIVbrfYSPZS8ZJprpHRtTJHhBbIw5KLsvAY6pgGf62jGB4lDgmIhZ7Hp1et6ZphrJgC3D6UM46PKN0OooWqhol9yjIfxKt6hgZU487RKwbVrSTwevmJ53%2FBvZQWmvsPXEpNV673%2BSTYqPMQ%2BB55FuCQebasAdfTEhGl1Fy90vEVBYHU6oaNEQa2r6Ixvsr84TUFix%2BIqmjygBagxv8Hr60UVoxLJkyK%2FQ%2F8wzuXTZ776Q7y2fLdp%2B2J3t6tW8KP8eu3S&X-Amz-Signature=953bd4a3dacd81c039308a12298c31c8ae454d00444c8824676b912064cd78da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMFG5I4H%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPCSQJJ%2BewKodmtzCyoBylkuO8oJ%2FVSKdbWUK%2Fw2P4gwIgek7cuiVFs6LTk3ELrWqAImOaqtdYxY5qg%2BmwP%2FFw0uYqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF8C104WdDpJnKMe8SrcA4RlrmduB28UhjnAMmG1KTbB3pSmbw%2BgDBhOI%2F9ts1EoPrlE9kXOypQyvZUwA8df9%2BZUejm2w9HP3BA61YnPpNl%2BAQiCxmSKzUaZEs8SQWo1WK8CGE6wWn%2FVLtxEnPwR89W1TGKPJkCGggvQXwxHdrdrg95vJ%2BFriU28eAw1q4a5JePSLjsMbzPHNgrBI%2BFd5sJ7g9Ig%2FlFz%2FiOzWW%2BCaYsMNfyCGQ0OUnGq7sqMVFGDSAyLlV44yKAgcQ3NqLA8H5OFSs6v67ThSTuuImyftmCiRoqJbve6V6lmsxOkojXH6s3N%2BT4FI4xPbVSqjKn0y2vGOGOfGr%2Fg8QaoSZfobGhhm0N6einX9r7yYKvBIMUaCia36idpVFqcbMZa50glrRQW4IMaojr26beg8ASeOvof6Bj5sapGZsxxg243PkjH%2B583NqfygcK%2BoADlnHCa9ABYb3Pl3K8HLrkUoFbHiT4QGMUOzqtIBP1KVtibsfosDNqRR4iRSBPyoHejlgP21MKIguymBAUWyWvew7bCeqNZq2y2MWe82DTo0ErNBe9o%2BgHO4f8EuczfR4omnIpDNLpdfN1c3M%2FkVukLRMh%2Fy4M9Hi5KsSkQV2k74t6UiSCFzC8TFdayerFDmSG%2FMP6i7LwGOqUBevZLC%2BEufPonhWWNnDV%2BJMgL%2BZifYS6dWC9bqFGCulmqp2evgXqiM%2BAmYcWxhL0C%2BWJZx4zs4VeLIjuDWWDq6fi4Nm4QGN9WWAG8vvmt88VaH8KlL1C3M8Hqy9Zqi9vhZkXUVHlZnHrsXVUh4YFkt5QMMm2mDVudPc%2FiXJTjCvBI6r%2FzPLtPCZXVWBpmVrbCyTn3i1ueKE%2BJ0OMxbtAtSFycz5y3&X-Amz-Signature=9fbd584a04574796526a090e6af0e92bd9d71f0b2b02314b782f409af183b4ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMFG5I4H%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T071325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPCSQJJ%2BewKodmtzCyoBylkuO8oJ%2FVSKdbWUK%2Fw2P4gwIgek7cuiVFs6LTk3ELrWqAImOaqtdYxY5qg%2BmwP%2FFw0uYqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF8C104WdDpJnKMe8SrcA4RlrmduB28UhjnAMmG1KTbB3pSmbw%2BgDBhOI%2F9ts1EoPrlE9kXOypQyvZUwA8df9%2BZUejm2w9HP3BA61YnPpNl%2BAQiCxmSKzUaZEs8SQWo1WK8CGE6wWn%2FVLtxEnPwR89W1TGKPJkCGggvQXwxHdrdrg95vJ%2BFriU28eAw1q4a5JePSLjsMbzPHNgrBI%2BFd5sJ7g9Ig%2FlFz%2FiOzWW%2BCaYsMNfyCGQ0OUnGq7sqMVFGDSAyLlV44yKAgcQ3NqLA8H5OFSs6v67ThSTuuImyftmCiRoqJbve6V6lmsxOkojXH6s3N%2BT4FI4xPbVSqjKn0y2vGOGOfGr%2Fg8QaoSZfobGhhm0N6einX9r7yYKvBIMUaCia36idpVFqcbMZa50glrRQW4IMaojr26beg8ASeOvof6Bj5sapGZsxxg243PkjH%2B583NqfygcK%2BoADlnHCa9ABYb3Pl3K8HLrkUoFbHiT4QGMUOzqtIBP1KVtibsfosDNqRR4iRSBPyoHejlgP21MKIguymBAUWyWvew7bCeqNZq2y2MWe82DTo0ErNBe9o%2BgHO4f8EuczfR4omnIpDNLpdfN1c3M%2FkVukLRMh%2Fy4M9Hi5KsSkQV2k74t6UiSCFzC8TFdayerFDmSG%2FMP6i7LwGOqUBevZLC%2BEufPonhWWNnDV%2BJMgL%2BZifYS6dWC9bqFGCulmqp2evgXqiM%2BAmYcWxhL0C%2BWJZx4zs4VeLIjuDWWDq6fi4Nm4QGN9WWAG8vvmt88VaH8KlL1C3M8Hqy9Zqi9vhZkXUVHlZnHrsXVUh4YFkt5QMMm2mDVudPc%2FiXJTjCvBI6r%2FzPLtPCZXVWBpmVrbCyTn3i1ueKE%2BJ0OMxbtAtSFycz5y3&X-Amz-Signature=ea5948f27563f83fd200f062bf3cd79273645da2fb3f2583f4f1dfd71156f099&X-Amz-SignedHeaders=host&x-id=GetObject)
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
