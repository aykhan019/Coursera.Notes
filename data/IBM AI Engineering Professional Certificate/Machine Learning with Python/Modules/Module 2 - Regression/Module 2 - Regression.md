

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WNXNZOV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FWMrrCQ6g2SkdU4PLC9Ri5%2FF9LB6V53%2Bn44GFNxC9LgIgIGbppJxgDdrEL%2FqvybyLZOixhpd8iLBt5w%2FFvGu2ASAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhATCBBjCcDkvcgySrcAz8qz%2B68s9490H5qs2k9BTR9ZCck4G9Oev41Rd%2B4p8TVzqKacAG2WiNcNcGRD4jpBiJzSBRrU6JAV52hhU4tjgF5zXQ5BuJCwgxhUs6pR8dz8BLjIRQyKhoJEySlve792BpqKreI3nFgc2uI863jsPJbCVxHsVHkmNUF6QmJYQ%2FdrqMNok3CGoCmJigwMcA40%2FAdN4%2BHCRSUPoko%2FIgM%2FDDsx1ULyj23OTIcmnKJoN05SD2ckVizZb0PbF%2FoqjRkezg00nMkUkaCthgGRK14WQp2RPbTx5x0ZsKld%2FfBie0q4FowcE%2FZPjTjH%2FrG1wPkiPHhKjfkAo4%2FBWPEAMFjM0baBzEPBtQZIdWRgobQhargmMXsXy7W6SheOpMzV18jCVMaQvoLzmYOdbEkw2Pdi2Ph8VEXAjgPWXvZ6gz50jpCZdqe13w7N%2BBgwJ6DJUepvH5W%2FedV%2BOC7VbPKsIp4d8wfu1Q5ApY8mVaouxEEUS2IK7LuXuzmkrBDIh82UYvNr%2FynrSl4hsXoxuRMu2WVNU%2FsUeGPTpu1G4zvKCZvD0LWTku52xmJrZGMLmHbCpTpm1I%2F%2FAs91U%2Fcbx4t1nNguvUGe98m%2BLzdLW336wxXZ9%2F8E0npG72IbV6BdSDRMIy4%2FbwGOqUBgmXlRI9z1wtkDI6MXszJ7gD%2F%2BhlcEJeXcxM1cQMCqWs8qSvdtMFBHWAXcCUPZfz%2Ff%2F54gL56Fs%2Bh%2FpQbWKQ%2BkmugaW8K%2BhW2WthR10TE3QLnFT%2BY4TY4Nf2WUlAJHwEM0%2BfRYlCfefa%2Byq1ogNg3FGEubYyTb7Kg3PQjjZHAXjtHQTv5fnr95OQ9KqrNLCFI6TBebwIx7KsYHaGN%2Fghk%2FZR8uHOK&X-Amz-Signature=52d339847335a66703be451cc6e0e0acd7b5ce4ee13a82e1eb1b8c146f78dd5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WNXNZOV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FWMrrCQ6g2SkdU4PLC9Ri5%2FF9LB6V53%2Bn44GFNxC9LgIgIGbppJxgDdrEL%2FqvybyLZOixhpd8iLBt5w%2FFvGu2ASAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhATCBBjCcDkvcgySrcAz8qz%2B68s9490H5qs2k9BTR9ZCck4G9Oev41Rd%2B4p8TVzqKacAG2WiNcNcGRD4jpBiJzSBRrU6JAV52hhU4tjgF5zXQ5BuJCwgxhUs6pR8dz8BLjIRQyKhoJEySlve792BpqKreI3nFgc2uI863jsPJbCVxHsVHkmNUF6QmJYQ%2FdrqMNok3CGoCmJigwMcA40%2FAdN4%2BHCRSUPoko%2FIgM%2FDDsx1ULyj23OTIcmnKJoN05SD2ckVizZb0PbF%2FoqjRkezg00nMkUkaCthgGRK14WQp2RPbTx5x0ZsKld%2FfBie0q4FowcE%2FZPjTjH%2FrG1wPkiPHhKjfkAo4%2FBWPEAMFjM0baBzEPBtQZIdWRgobQhargmMXsXy7W6SheOpMzV18jCVMaQvoLzmYOdbEkw2Pdi2Ph8VEXAjgPWXvZ6gz50jpCZdqe13w7N%2BBgwJ6DJUepvH5W%2FedV%2BOC7VbPKsIp4d8wfu1Q5ApY8mVaouxEEUS2IK7LuXuzmkrBDIh82UYvNr%2FynrSl4hsXoxuRMu2WVNU%2FsUeGPTpu1G4zvKCZvD0LWTku52xmJrZGMLmHbCpTpm1I%2F%2FAs91U%2Fcbx4t1nNguvUGe98m%2BLzdLW336wxXZ9%2F8E0npG72IbV6BdSDRMIy4%2FbwGOqUBgmXlRI9z1wtkDI6MXszJ7gD%2F%2BhlcEJeXcxM1cQMCqWs8qSvdtMFBHWAXcCUPZfz%2Ff%2F54gL56Fs%2Bh%2FpQbWKQ%2BkmugaW8K%2BhW2WthR10TE3QLnFT%2BY4TY4Nf2WUlAJHwEM0%2BfRYlCfefa%2Byq1ogNg3FGEubYyTb7Kg3PQjjZHAXjtHQTv5fnr95OQ9KqrNLCFI6TBebwIx7KsYHaGN%2Fghk%2FZR8uHOK&X-Amz-Signature=4fc329bb1fa726f617092d6770b35d85a298cb283eef00ff251c2278b9ba3671&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WNXNZOV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FWMrrCQ6g2SkdU4PLC9Ri5%2FF9LB6V53%2Bn44GFNxC9LgIgIGbppJxgDdrEL%2FqvybyLZOixhpd8iLBt5w%2FFvGu2ASAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhATCBBjCcDkvcgySrcAz8qz%2B68s9490H5qs2k9BTR9ZCck4G9Oev41Rd%2B4p8TVzqKacAG2WiNcNcGRD4jpBiJzSBRrU6JAV52hhU4tjgF5zXQ5BuJCwgxhUs6pR8dz8BLjIRQyKhoJEySlve792BpqKreI3nFgc2uI863jsPJbCVxHsVHkmNUF6QmJYQ%2FdrqMNok3CGoCmJigwMcA40%2FAdN4%2BHCRSUPoko%2FIgM%2FDDsx1ULyj23OTIcmnKJoN05SD2ckVizZb0PbF%2FoqjRkezg00nMkUkaCthgGRK14WQp2RPbTx5x0ZsKld%2FfBie0q4FowcE%2FZPjTjH%2FrG1wPkiPHhKjfkAo4%2FBWPEAMFjM0baBzEPBtQZIdWRgobQhargmMXsXy7W6SheOpMzV18jCVMaQvoLzmYOdbEkw2Pdi2Ph8VEXAjgPWXvZ6gz50jpCZdqe13w7N%2BBgwJ6DJUepvH5W%2FedV%2BOC7VbPKsIp4d8wfu1Q5ApY8mVaouxEEUS2IK7LuXuzmkrBDIh82UYvNr%2FynrSl4hsXoxuRMu2WVNU%2FsUeGPTpu1G4zvKCZvD0LWTku52xmJrZGMLmHbCpTpm1I%2F%2FAs91U%2Fcbx4t1nNguvUGe98m%2BLzdLW336wxXZ9%2F8E0npG72IbV6BdSDRMIy4%2FbwGOqUBgmXlRI9z1wtkDI6MXszJ7gD%2F%2BhlcEJeXcxM1cQMCqWs8qSvdtMFBHWAXcCUPZfz%2Ff%2F54gL56Fs%2Bh%2FpQbWKQ%2BkmugaW8K%2BhW2WthR10TE3QLnFT%2BY4TY4Nf2WUlAJHwEM0%2BfRYlCfefa%2Byq1ogNg3FGEubYyTb7Kg3PQjjZHAXjtHQTv5fnr95OQ9KqrNLCFI6TBebwIx7KsYHaGN%2Fghk%2FZR8uHOK&X-Amz-Signature=9c476363dba419ffdcc9b7ae0a5add883bbdf541755fe1873d1863e3e375cd24&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WNXNZOV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FWMrrCQ6g2SkdU4PLC9Ri5%2FF9LB6V53%2Bn44GFNxC9LgIgIGbppJxgDdrEL%2FqvybyLZOixhpd8iLBt5w%2FFvGu2ASAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhATCBBjCcDkvcgySrcAz8qz%2B68s9490H5qs2k9BTR9ZCck4G9Oev41Rd%2B4p8TVzqKacAG2WiNcNcGRD4jpBiJzSBRrU6JAV52hhU4tjgF5zXQ5BuJCwgxhUs6pR8dz8BLjIRQyKhoJEySlve792BpqKreI3nFgc2uI863jsPJbCVxHsVHkmNUF6QmJYQ%2FdrqMNok3CGoCmJigwMcA40%2FAdN4%2BHCRSUPoko%2FIgM%2FDDsx1ULyj23OTIcmnKJoN05SD2ckVizZb0PbF%2FoqjRkezg00nMkUkaCthgGRK14WQp2RPbTx5x0ZsKld%2FfBie0q4FowcE%2FZPjTjH%2FrG1wPkiPHhKjfkAo4%2FBWPEAMFjM0baBzEPBtQZIdWRgobQhargmMXsXy7W6SheOpMzV18jCVMaQvoLzmYOdbEkw2Pdi2Ph8VEXAjgPWXvZ6gz50jpCZdqe13w7N%2BBgwJ6DJUepvH5W%2FedV%2BOC7VbPKsIp4d8wfu1Q5ApY8mVaouxEEUS2IK7LuXuzmkrBDIh82UYvNr%2FynrSl4hsXoxuRMu2WVNU%2FsUeGPTpu1G4zvKCZvD0LWTku52xmJrZGMLmHbCpTpm1I%2F%2FAs91U%2Fcbx4t1nNguvUGe98m%2BLzdLW336wxXZ9%2F8E0npG72IbV6BdSDRMIy4%2FbwGOqUBgmXlRI9z1wtkDI6MXszJ7gD%2F%2BhlcEJeXcxM1cQMCqWs8qSvdtMFBHWAXcCUPZfz%2Ff%2F54gL56Fs%2Bh%2FpQbWKQ%2BkmugaW8K%2BhW2WthR10TE3QLnFT%2BY4TY4Nf2WUlAJHwEM0%2BfRYlCfefa%2Byq1ogNg3FGEubYyTb7Kg3PQjjZHAXjtHQTv5fnr95OQ9KqrNLCFI6TBebwIx7KsYHaGN%2Fghk%2FZR8uHOK&X-Amz-Signature=33639ed94c78f988577bcae74321b68a6ca8aac45626f107f1a338d411bd5563&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WNXNZOV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FWMrrCQ6g2SkdU4PLC9Ri5%2FF9LB6V53%2Bn44GFNxC9LgIgIGbppJxgDdrEL%2FqvybyLZOixhpd8iLBt5w%2FFvGu2ASAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhATCBBjCcDkvcgySrcAz8qz%2B68s9490H5qs2k9BTR9ZCck4G9Oev41Rd%2B4p8TVzqKacAG2WiNcNcGRD4jpBiJzSBRrU6JAV52hhU4tjgF5zXQ5BuJCwgxhUs6pR8dz8BLjIRQyKhoJEySlve792BpqKreI3nFgc2uI863jsPJbCVxHsVHkmNUF6QmJYQ%2FdrqMNok3CGoCmJigwMcA40%2FAdN4%2BHCRSUPoko%2FIgM%2FDDsx1ULyj23OTIcmnKJoN05SD2ckVizZb0PbF%2FoqjRkezg00nMkUkaCthgGRK14WQp2RPbTx5x0ZsKld%2FfBie0q4FowcE%2FZPjTjH%2FrG1wPkiPHhKjfkAo4%2FBWPEAMFjM0baBzEPBtQZIdWRgobQhargmMXsXy7W6SheOpMzV18jCVMaQvoLzmYOdbEkw2Pdi2Ph8VEXAjgPWXvZ6gz50jpCZdqe13w7N%2BBgwJ6DJUepvH5W%2FedV%2BOC7VbPKsIp4d8wfu1Q5ApY8mVaouxEEUS2IK7LuXuzmkrBDIh82UYvNr%2FynrSl4hsXoxuRMu2WVNU%2FsUeGPTpu1G4zvKCZvD0LWTku52xmJrZGMLmHbCpTpm1I%2F%2FAs91U%2Fcbx4t1nNguvUGe98m%2BLzdLW336wxXZ9%2F8E0npG72IbV6BdSDRMIy4%2FbwGOqUBgmXlRI9z1wtkDI6MXszJ7gD%2F%2BhlcEJeXcxM1cQMCqWs8qSvdtMFBHWAXcCUPZfz%2Ff%2F54gL56Fs%2Bh%2FpQbWKQ%2BkmugaW8K%2BhW2WthR10TE3QLnFT%2BY4TY4Nf2WUlAJHwEM0%2BfRYlCfefa%2Byq1ogNg3FGEubYyTb7Kg3PQjjZHAXjtHQTv5fnr95OQ9KqrNLCFI6TBebwIx7KsYHaGN%2Fghk%2FZR8uHOK&X-Amz-Signature=83aa5959757433762a63be578d48fb0f180bea3e30b1fab8531fa20132da0fc7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WNXNZOV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FWMrrCQ6g2SkdU4PLC9Ri5%2FF9LB6V53%2Bn44GFNxC9LgIgIGbppJxgDdrEL%2FqvybyLZOixhpd8iLBt5w%2FFvGu2ASAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhATCBBjCcDkvcgySrcAz8qz%2B68s9490H5qs2k9BTR9ZCck4G9Oev41Rd%2B4p8TVzqKacAG2WiNcNcGRD4jpBiJzSBRrU6JAV52hhU4tjgF5zXQ5BuJCwgxhUs6pR8dz8BLjIRQyKhoJEySlve792BpqKreI3nFgc2uI863jsPJbCVxHsVHkmNUF6QmJYQ%2FdrqMNok3CGoCmJigwMcA40%2FAdN4%2BHCRSUPoko%2FIgM%2FDDsx1ULyj23OTIcmnKJoN05SD2ckVizZb0PbF%2FoqjRkezg00nMkUkaCthgGRK14WQp2RPbTx5x0ZsKld%2FfBie0q4FowcE%2FZPjTjH%2FrG1wPkiPHhKjfkAo4%2FBWPEAMFjM0baBzEPBtQZIdWRgobQhargmMXsXy7W6SheOpMzV18jCVMaQvoLzmYOdbEkw2Pdi2Ph8VEXAjgPWXvZ6gz50jpCZdqe13w7N%2BBgwJ6DJUepvH5W%2FedV%2BOC7VbPKsIp4d8wfu1Q5ApY8mVaouxEEUS2IK7LuXuzmkrBDIh82UYvNr%2FynrSl4hsXoxuRMu2WVNU%2FsUeGPTpu1G4zvKCZvD0LWTku52xmJrZGMLmHbCpTpm1I%2F%2FAs91U%2Fcbx4t1nNguvUGe98m%2BLzdLW336wxXZ9%2F8E0npG72IbV6BdSDRMIy4%2FbwGOqUBgmXlRI9z1wtkDI6MXszJ7gD%2F%2BhlcEJeXcxM1cQMCqWs8qSvdtMFBHWAXcCUPZfz%2Ff%2F54gL56Fs%2Bh%2FpQbWKQ%2BkmugaW8K%2BhW2WthR10TE3QLnFT%2BY4TY4Nf2WUlAJHwEM0%2BfRYlCfefa%2Byq1ogNg3FGEubYyTb7Kg3PQjjZHAXjtHQTv5fnr95OQ9KqrNLCFI6TBebwIx7KsYHaGN%2Fghk%2FZR8uHOK&X-Amz-Signature=55febb047b9aa1e29379b57cf90e88c8a6a59443e099464e14e8648f2da1b2b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WNXNZOV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FWMrrCQ6g2SkdU4PLC9Ri5%2FF9LB6V53%2Bn44GFNxC9LgIgIGbppJxgDdrEL%2FqvybyLZOixhpd8iLBt5w%2FFvGu2ASAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhATCBBjCcDkvcgySrcAz8qz%2B68s9490H5qs2k9BTR9ZCck4G9Oev41Rd%2B4p8TVzqKacAG2WiNcNcGRD4jpBiJzSBRrU6JAV52hhU4tjgF5zXQ5BuJCwgxhUs6pR8dz8BLjIRQyKhoJEySlve792BpqKreI3nFgc2uI863jsPJbCVxHsVHkmNUF6QmJYQ%2FdrqMNok3CGoCmJigwMcA40%2FAdN4%2BHCRSUPoko%2FIgM%2FDDsx1ULyj23OTIcmnKJoN05SD2ckVizZb0PbF%2FoqjRkezg00nMkUkaCthgGRK14WQp2RPbTx5x0ZsKld%2FfBie0q4FowcE%2FZPjTjH%2FrG1wPkiPHhKjfkAo4%2FBWPEAMFjM0baBzEPBtQZIdWRgobQhargmMXsXy7W6SheOpMzV18jCVMaQvoLzmYOdbEkw2Pdi2Ph8VEXAjgPWXvZ6gz50jpCZdqe13w7N%2BBgwJ6DJUepvH5W%2FedV%2BOC7VbPKsIp4d8wfu1Q5ApY8mVaouxEEUS2IK7LuXuzmkrBDIh82UYvNr%2FynrSl4hsXoxuRMu2WVNU%2FsUeGPTpu1G4zvKCZvD0LWTku52xmJrZGMLmHbCpTpm1I%2F%2FAs91U%2Fcbx4t1nNguvUGe98m%2BLzdLW336wxXZ9%2F8E0npG72IbV6BdSDRMIy4%2FbwGOqUBgmXlRI9z1wtkDI6MXszJ7gD%2F%2BhlcEJeXcxM1cQMCqWs8qSvdtMFBHWAXcCUPZfz%2Ff%2F54gL56Fs%2Bh%2FpQbWKQ%2BkmugaW8K%2BhW2WthR10TE3QLnFT%2BY4TY4Nf2WUlAJHwEM0%2BfRYlCfefa%2Byq1ogNg3FGEubYyTb7Kg3PQjjZHAXjtHQTv5fnr95OQ9KqrNLCFI6TBebwIx7KsYHaGN%2Fghk%2FZR8uHOK&X-Amz-Signature=4390e257fbfbadfcf2bb309e10d75ed1308c6e2e82ee1dc6240cc8b0fc7a6dd0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WNXNZOV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FWMrrCQ6g2SkdU4PLC9Ri5%2FF9LB6V53%2Bn44GFNxC9LgIgIGbppJxgDdrEL%2FqvybyLZOixhpd8iLBt5w%2FFvGu2ASAqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhATCBBjCcDkvcgySrcAz8qz%2B68s9490H5qs2k9BTR9ZCck4G9Oev41Rd%2B4p8TVzqKacAG2WiNcNcGRD4jpBiJzSBRrU6JAV52hhU4tjgF5zXQ5BuJCwgxhUs6pR8dz8BLjIRQyKhoJEySlve792BpqKreI3nFgc2uI863jsPJbCVxHsVHkmNUF6QmJYQ%2FdrqMNok3CGoCmJigwMcA40%2FAdN4%2BHCRSUPoko%2FIgM%2FDDsx1ULyj23OTIcmnKJoN05SD2ckVizZb0PbF%2FoqjRkezg00nMkUkaCthgGRK14WQp2RPbTx5x0ZsKld%2FfBie0q4FowcE%2FZPjTjH%2FrG1wPkiPHhKjfkAo4%2FBWPEAMFjM0baBzEPBtQZIdWRgobQhargmMXsXy7W6SheOpMzV18jCVMaQvoLzmYOdbEkw2Pdi2Ph8VEXAjgPWXvZ6gz50jpCZdqe13w7N%2BBgwJ6DJUepvH5W%2FedV%2BOC7VbPKsIp4d8wfu1Q5ApY8mVaouxEEUS2IK7LuXuzmkrBDIh82UYvNr%2FynrSl4hsXoxuRMu2WVNU%2FsUeGPTpu1G4zvKCZvD0LWTku52xmJrZGMLmHbCpTpm1I%2F%2FAs91U%2Fcbx4t1nNguvUGe98m%2BLzdLW336wxXZ9%2F8E0npG72IbV6BdSDRMIy4%2FbwGOqUBgmXlRI9z1wtkDI6MXszJ7gD%2F%2BhlcEJeXcxM1cQMCqWs8qSvdtMFBHWAXcCUPZfz%2Ff%2F54gL56Fs%2Bh%2FpQbWKQ%2BkmugaW8K%2BhW2WthR10TE3QLnFT%2BY4TY4Nf2WUlAJHwEM0%2BfRYlCfefa%2Byq1ogNg3FGEubYyTb7Kg3PQjjZHAXjtHQTv5fnr95OQ9KqrNLCFI6TBebwIx7KsYHaGN%2Fghk%2FZR8uHOK&X-Amz-Signature=805f38704cad70cdcd3d8a96c4b2732487e7d62aedec52034b9a609a4211642b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD6DABS3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGK9vd0h3k3gpssDb%2F4lyzDaaZPPspSFhMH35qr8kQDaAiEAkHKOCgyr0AJW2eoTN7Hl%2FZcVqPoFN4ad7ss1T6lCfMMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJE4%2BTKWhZx1lU5VGCrcA2heE4FVtdcONIxknWdxilsoMIo3zpApHRfxAF4iOf5EsNB89S4N%2BrENHgSPjUezzezk30zW%2BPdAdq9TnitVD%2FG7N7KdbOvjY76fjO8qPXrIpveSqHuh0QXHFAQzWgQHhma5%2B9FkC3J%2FUa8caOAfvflKCIbiovWihhJaSMlZ4I1Z9qXcyzohaC%2FtISatqUyFfv8e40WPQ95Bs3zHpxG%2BZ1qCEdEnAV6MN2wiK%2BFdNIf3UMDNWAPTouX%2FXHQjzJyAeE7L%2BBBWOiisHnon%2BRSyLE6xSuZq%2FI8E3IKA9fcfYqcCBE5ZBreukVTkAUdRZJkaW3IDz5HwSFuIOs7X6rLGpTEJQI4QkcTyX2lfA9%2BxQ3zPB2yxI8iMNo0TZrFfYKlV5dWHp%2B5Pei8anfXzPToH1x8FWJqxz2KyzMgg%2FNiMlio047oiIGf3%2B%2BbLcUUOE2yVLqZaA9coMWAU7Kd0d6LHNCIz3%2FvCEgmDcJAnOppbfE4r0pdTn%2FB1p%2FXH%2FQ4STOuTZmhmF5S7jR7%2Fb%2Bc0eyRGntxZFYxXZkGmQpQgV4Kc4eWYRGyLdlH1yoQoQwsVEGBDdAIFCjv93uZPZGV9yOxR3P6gX8A6uPqEhVUBSy3JmqhJB87ggbksRJbdIQI1MNy1%2FbwGOqUBQ8Hj1L8B7wMqbLdAJZvd2NIVWQ1qBukkX15e4hkB9xgy1UTE2GYx%2BwA37tOtyvJBJuhO4G6X%2FXzdm0MqhPaAPWN%2FPDUudUg8KMMXpa49mBPWSz2YoBhMtOltKg%2FPTCbvsZCvLJ4Ju3ffDhTEfh6dUBCHUheA4xvtHQUx0aw20pxLnFiKMLrrlzJkuz%2BexBOOf9JlcRiODL2%2FtLnDRWpPtth9plyX&X-Amz-Signature=e2ad97e316829ab94d4df21beef94867befd04420f2c985bb29f15e77e0cb4fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBWAQVN5%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmk1bMcJGWnl0l%2B9ASCO87rFAXhWTBEkUj023d5EP0qgIhAMZYYX6poGoBUTWz%2FJH8zx7sU1mOvQIN%2BxxRHjEWSlIkKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwTtM2LA12jzgZHfWkq3AO7e1BfvQ9KB%2FO%2BDF1LnwiAE7axs%2BXcGQY2XCn9pqGDHDhaCf%2F%2BmZ29NpIEF7H4jL%2FBrE7If9GR%2Fp7b7eKuuXcILFBVefFYoFj46M2CaqYnzvugJKi0JFxz0Tfpgc6sGO%2BqJXtvZgI4SqmvOM0ETxxdjlwreIQl7SXU8eMlqDlecSZx6rqYkURetwwqUPZyhkMc3lZrySl1VnLtOGkp%2B91WkWEZTucJ%2BbieH9cfKZsdJ3F3SIr6SLWk5QeY1R7KlaBNi76zUcbFJaUSvOJX0utuKhHWy7mpoZPzyUHLILSHeXVDPi1SrHveELPSybTHoxA9YGeX0X%2BnpMt3wKgsVFBk169e6V5PyDzSu0QAupQIHmZbmhgV6rrr2c5PNelQntRh2pTL%2FGKFgb2pbKPpZEwT9y9J1SWupIIgmPC9%2BJh36ue8yW7LQmfnEDWn2YiQxBP0Tc2wjaTDK8qXT4BSv1T19DgfCE%2FA75OcWliwxQQLOuc9r6Qpi74gNRYxP3bfqzDjiW%2FIr3xFAr%2ByzctEGNbSQaHdXkM3yN7obatY9jXK1os98uvikGRX3iHYt6ZYQ1lHu5L9kwgqMNwRGllTuZPCFbvYuANJfD2TC7A3mPpGV9KQfRVkaZEIn0QkyjDzuv28BjqkAVcoctynyLAzlseJhYQ9%2BvSiGRM2%2BH8pjov2DZ%2B9AaGX0eGOtPLs29KkRohRwcbh5109C5btMI0n3aMEfG9wG1L%2BPByamLHXKjzBEC8LSxDaIL7jkKhlAOPdX8EDF%2Bnk8m%2FrVFElnS3rt1VgDH6lRM8hr9e%2FQFzZztTJhopmmAk2xx%2Bc4TKsUBlmji6g%2FUsukcPz3goFvaqhkAPTeBvx14RZ6obn&X-Amz-Signature=c3809a21ef9dd362b799e4ba69bbaf758d85d7e618e1207bf4120decb7523254&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664P7DTERB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaZDS9YEbwsGvS6HDMBzYrKZFqLZWwhDtqpAXY%2B4huGAIhAMLvG%2FLrbtgMzWX7OmifZdQ6RtHAO9Sldr%2Bk9MFZKer6KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFIhq3cme8Qkxrbn4q3APYnD9aMrrZfNgrLmJowTxBdppqN5Tz2DPeZfTp4gfifcgNQKJcsDndAukIoPIuVXyFNSdS7752b9D0SdySQbqIuowOdGoNn0KRnkkJ8soMjnO2l%2BLeoVq830oiUsM%2BbLrhlWl77%2Bjq7r%2Bv1yqoDn2X7NxefsF048VDmtbnUsvm%2B1%2FbcLCyXpRqPxvtWgS7PbGskRULzInvHmZymFWwlfaV6Pl3to%2FZS6ZEkr7TxgpVIGy0GNt12%2BtE95Q%2FkJFmVBf4IwparxAanEq%2F1U%2B4Jz7PAGp40B437MJSA7rnYwcltOHtHYZ2iRoPOie0BxREmJAjZQXqQjVMvACvPS6EEZklwoKWpJeJHLSnR9ylLZUVXS3aJndjEkkmybo3x4OFUgF5y77dmMEqpkDI5%2BggxHHk%2BqTB7LV4ttjOu7mWr8vwJgMag6Nat5dP7rOPL9pVylt6WYW0lPpDk%2BZf1AkXqbvRcGk4bBbhhM0gh5bkW8HuqDVIkVhvPR7J0KK2T6OSxdHQUGr8LjEnUn1OsCKZmIKConqaleGYIEPqBQjKsV6MDxbM5oB%2B0yIkfKrN8MMyY82Q49UefMk7mrVXzIcUZbyYChM1qlKM6TtgxyseJJDQ2aDUCBAG9tPK25mzSDCvvP28BjqkAUhlCMgV5HW2fw9slPiFfWZK4jReD%2F7hX9sJJW0Kn1Cj6oLIOidFfGEoLptxE0A1LB2mVYlyI9QelWucFes4nd3vZrEZtjBnTaw%2BBlnzxSRWuAf6ZPvP1UBQRu4KqkjG2iOgBjk91F5iDKZwCbnImCzaT4o9yhfMVpf8Y1yfEEydxm6Cnye0Qlyw4t%2FMKKlFQwsImqZSTsHtMhXGVpdaO3C21GRm&X-Amz-Signature=b359e41abc26a973dc80ce3ddf245f7dd1ea6490d60a8af112586a7e61b22baf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664P7DTERB%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T151451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaZDS9YEbwsGvS6HDMBzYrKZFqLZWwhDtqpAXY%2B4huGAIhAMLvG%2FLrbtgMzWX7OmifZdQ6RtHAO9Sldr%2Bk9MFZKer6KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzFIhq3cme8Qkxrbn4q3APYnD9aMrrZfNgrLmJowTxBdppqN5Tz2DPeZfTp4gfifcgNQKJcsDndAukIoPIuVXyFNSdS7752b9D0SdySQbqIuowOdGoNn0KRnkkJ8soMjnO2l%2BLeoVq830oiUsM%2BbLrhlWl77%2Bjq7r%2Bv1yqoDn2X7NxefsF048VDmtbnUsvm%2B1%2FbcLCyXpRqPxvtWgS7PbGskRULzInvHmZymFWwlfaV6Pl3to%2FZS6ZEkr7TxgpVIGy0GNt12%2BtE95Q%2FkJFmVBf4IwparxAanEq%2F1U%2B4Jz7PAGp40B437MJSA7rnYwcltOHtHYZ2iRoPOie0BxREmJAjZQXqQjVMvACvPS6EEZklwoKWpJeJHLSnR9ylLZUVXS3aJndjEkkmybo3x4OFUgF5y77dmMEqpkDI5%2BggxHHk%2BqTB7LV4ttjOu7mWr8vwJgMag6Nat5dP7rOPL9pVylt6WYW0lPpDk%2BZf1AkXqbvRcGk4bBbhhM0gh5bkW8HuqDVIkVhvPR7J0KK2T6OSxdHQUGr8LjEnUn1OsCKZmIKConqaleGYIEPqBQjKsV6MDxbM5oB%2B0yIkfKrN8MMyY82Q49UefMk7mrVXzIcUZbyYChM1qlKM6TtgxyseJJDQ2aDUCBAG9tPK25mzSDCvvP28BjqkAUhlCMgV5HW2fw9slPiFfWZK4jReD%2F7hX9sJJW0Kn1Cj6oLIOidFfGEoLptxE0A1LB2mVYlyI9QelWucFes4nd3vZrEZtjBnTaw%2BBlnzxSRWuAf6ZPvP1UBQRu4KqkjG2iOgBjk91F5iDKZwCbnImCzaT4o9yhfMVpf8Y1yfEEydxm6Cnye0Qlyw4t%2FMKKlFQwsImqZSTsHtMhXGVpdaO3C21GRm&X-Amz-Signature=4424fcc6cab273d640f63525de02352c876e66df620648953e16831e457157dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
