

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MIQWVVX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDdFO0iYtdimhXwGzG62iKPuDlzTlBkBytMPJtMT8rdaAIgAMigP%2BLUthYii33W%2F9dPDDixHK%2B5kQqfZmN%2F%2Fe0Tnnsq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHyZXCYVu42qAnVf1CrcA7RFN0h498f6%2BRTbFSgOFZ2pcPY1Z1fXj%2BRhS4pJikYDSwgc9NOMnxK9HlYEHtR0n4Msh2CGGk4QoXKQlVTVGH2D8fpDbys0Qh90fMEukyOkB%2Ftd4Lhs47In5hegYmx6y6RwTAjfYlIlsCX7TbtYjPA79vihk6cXPWIBUvJGrLfwX%2FltZvliUfWnx999x9aG2bsXklpdUIV5w6OQ3GFjbhk%2Fmxnl53voq3uP5LIdFD6nxTeC75Vg8LC2CBj65mWEryIffysl7LTVFwMirVrNIBmfgXKp1olwFiYpA52giz1kRFBBu4nmMAEADxwnqGOn7aDvdmi8hznZP9A381IHdbg4Ky0If3pYsCD6SlGcCaWatRLzHdasglpByAL1V5Atr2t3G5pX6dtuvrB8PexxznviYM%2B4v%2FUfdsQcrF39cYive1qLQy77kTUAZGgXHi%2F1kmn%2FcUhkl9pooo%2FSXbZd7rkLN3T9DVRDBMsnp4Ragh%2BtGltM7F2EHEp%2FePOHidNUZ9%2BI3zM8hs%2BPaP%2B9LnM81V7lIY7T2tZ%2BUhnbLuXVMc3XoP5AAy60OjVA8u%2F%2FQJmlHhm7qgXmUmXpqvC%2B9OKV9Aiyx8shGtJaW4k72CXZh7x6TzOs7Borc2PV%2F3jXMLuLmL0GOqUBtI9Dcq6aqH%2BI2jDypg35XKL6I6MJCs%2BlmkuZDvNudI%2Fikb4vSJ2V6I%2Fvs8I7kvP2%2B1cPnRzIgfRj3OE%2FR5WRK07a8ivD8sIXCRKNBaTfb4IS7nls1xGvUvAU2QZo5wEIbC1AD2xmnFNpr2Sn2CsiYD7Gm%2FUw3ap46nmpY%2BSTmBPxsRa%2B2yCUx8V1VNluquPKz4y7QS%2Fv%2FmiGAf%2FiHOihYLO%2BzoJD&X-Amz-Signature=b62ef73b3d11ee872223c07d2aeac0de97e7ce3c98985f5ab643f51bf9d67f9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MIQWVVX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDdFO0iYtdimhXwGzG62iKPuDlzTlBkBytMPJtMT8rdaAIgAMigP%2BLUthYii33W%2F9dPDDixHK%2B5kQqfZmN%2F%2Fe0Tnnsq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHyZXCYVu42qAnVf1CrcA7RFN0h498f6%2BRTbFSgOFZ2pcPY1Z1fXj%2BRhS4pJikYDSwgc9NOMnxK9HlYEHtR0n4Msh2CGGk4QoXKQlVTVGH2D8fpDbys0Qh90fMEukyOkB%2Ftd4Lhs47In5hegYmx6y6RwTAjfYlIlsCX7TbtYjPA79vihk6cXPWIBUvJGrLfwX%2FltZvliUfWnx999x9aG2bsXklpdUIV5w6OQ3GFjbhk%2Fmxnl53voq3uP5LIdFD6nxTeC75Vg8LC2CBj65mWEryIffysl7LTVFwMirVrNIBmfgXKp1olwFiYpA52giz1kRFBBu4nmMAEADxwnqGOn7aDvdmi8hznZP9A381IHdbg4Ky0If3pYsCD6SlGcCaWatRLzHdasglpByAL1V5Atr2t3G5pX6dtuvrB8PexxznviYM%2B4v%2FUfdsQcrF39cYive1qLQy77kTUAZGgXHi%2F1kmn%2FcUhkl9pooo%2FSXbZd7rkLN3T9DVRDBMsnp4Ragh%2BtGltM7F2EHEp%2FePOHidNUZ9%2BI3zM8hs%2BPaP%2B9LnM81V7lIY7T2tZ%2BUhnbLuXVMc3XoP5AAy60OjVA8u%2F%2FQJmlHhm7qgXmUmXpqvC%2B9OKV9Aiyx8shGtJaW4k72CXZh7x6TzOs7Borc2PV%2F3jXMLuLmL0GOqUBtI9Dcq6aqH%2BI2jDypg35XKL6I6MJCs%2BlmkuZDvNudI%2Fikb4vSJ2V6I%2Fvs8I7kvP2%2B1cPnRzIgfRj3OE%2FR5WRK07a8ivD8sIXCRKNBaTfb4IS7nls1xGvUvAU2QZo5wEIbC1AD2xmnFNpr2Sn2CsiYD7Gm%2FUw3ap46nmpY%2BSTmBPxsRa%2B2yCUx8V1VNluquPKz4y7QS%2Fv%2FmiGAf%2FiHOihYLO%2BzoJD&X-Amz-Signature=71a62ebadccc7355dab87cda5920218b3c850cc52841e6b6d986a6f289b1fe69&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MIQWVVX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDdFO0iYtdimhXwGzG62iKPuDlzTlBkBytMPJtMT8rdaAIgAMigP%2BLUthYii33W%2F9dPDDixHK%2B5kQqfZmN%2F%2Fe0Tnnsq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHyZXCYVu42qAnVf1CrcA7RFN0h498f6%2BRTbFSgOFZ2pcPY1Z1fXj%2BRhS4pJikYDSwgc9NOMnxK9HlYEHtR0n4Msh2CGGk4QoXKQlVTVGH2D8fpDbys0Qh90fMEukyOkB%2Ftd4Lhs47In5hegYmx6y6RwTAjfYlIlsCX7TbtYjPA79vihk6cXPWIBUvJGrLfwX%2FltZvliUfWnx999x9aG2bsXklpdUIV5w6OQ3GFjbhk%2Fmxnl53voq3uP5LIdFD6nxTeC75Vg8LC2CBj65mWEryIffysl7LTVFwMirVrNIBmfgXKp1olwFiYpA52giz1kRFBBu4nmMAEADxwnqGOn7aDvdmi8hznZP9A381IHdbg4Ky0If3pYsCD6SlGcCaWatRLzHdasglpByAL1V5Atr2t3G5pX6dtuvrB8PexxznviYM%2B4v%2FUfdsQcrF39cYive1qLQy77kTUAZGgXHi%2F1kmn%2FcUhkl9pooo%2FSXbZd7rkLN3T9DVRDBMsnp4Ragh%2BtGltM7F2EHEp%2FePOHidNUZ9%2BI3zM8hs%2BPaP%2B9LnM81V7lIY7T2tZ%2BUhnbLuXVMc3XoP5AAy60OjVA8u%2F%2FQJmlHhm7qgXmUmXpqvC%2B9OKV9Aiyx8shGtJaW4k72CXZh7x6TzOs7Borc2PV%2F3jXMLuLmL0GOqUBtI9Dcq6aqH%2BI2jDypg35XKL6I6MJCs%2BlmkuZDvNudI%2Fikb4vSJ2V6I%2Fvs8I7kvP2%2B1cPnRzIgfRj3OE%2FR5WRK07a8ivD8sIXCRKNBaTfb4IS7nls1xGvUvAU2QZo5wEIbC1AD2xmnFNpr2Sn2CsiYD7Gm%2FUw3ap46nmpY%2BSTmBPxsRa%2B2yCUx8V1VNluquPKz4y7QS%2Fv%2FmiGAf%2FiHOihYLO%2BzoJD&X-Amz-Signature=ac0252d984d6b94602da0f03cd0457dffce1f2d0c804b9a9cb8334eb2e6cee4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MIQWVVX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDdFO0iYtdimhXwGzG62iKPuDlzTlBkBytMPJtMT8rdaAIgAMigP%2BLUthYii33W%2F9dPDDixHK%2B5kQqfZmN%2F%2Fe0Tnnsq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHyZXCYVu42qAnVf1CrcA7RFN0h498f6%2BRTbFSgOFZ2pcPY1Z1fXj%2BRhS4pJikYDSwgc9NOMnxK9HlYEHtR0n4Msh2CGGk4QoXKQlVTVGH2D8fpDbys0Qh90fMEukyOkB%2Ftd4Lhs47In5hegYmx6y6RwTAjfYlIlsCX7TbtYjPA79vihk6cXPWIBUvJGrLfwX%2FltZvliUfWnx999x9aG2bsXklpdUIV5w6OQ3GFjbhk%2Fmxnl53voq3uP5LIdFD6nxTeC75Vg8LC2CBj65mWEryIffysl7LTVFwMirVrNIBmfgXKp1olwFiYpA52giz1kRFBBu4nmMAEADxwnqGOn7aDvdmi8hznZP9A381IHdbg4Ky0If3pYsCD6SlGcCaWatRLzHdasglpByAL1V5Atr2t3G5pX6dtuvrB8PexxznviYM%2B4v%2FUfdsQcrF39cYive1qLQy77kTUAZGgXHi%2F1kmn%2FcUhkl9pooo%2FSXbZd7rkLN3T9DVRDBMsnp4Ragh%2BtGltM7F2EHEp%2FePOHidNUZ9%2BI3zM8hs%2BPaP%2B9LnM81V7lIY7T2tZ%2BUhnbLuXVMc3XoP5AAy60OjVA8u%2F%2FQJmlHhm7qgXmUmXpqvC%2B9OKV9Aiyx8shGtJaW4k72CXZh7x6TzOs7Borc2PV%2F3jXMLuLmL0GOqUBtI9Dcq6aqH%2BI2jDypg35XKL6I6MJCs%2BlmkuZDvNudI%2Fikb4vSJ2V6I%2Fvs8I7kvP2%2B1cPnRzIgfRj3OE%2FR5WRK07a8ivD8sIXCRKNBaTfb4IS7nls1xGvUvAU2QZo5wEIbC1AD2xmnFNpr2Sn2CsiYD7Gm%2FUw3ap46nmpY%2BSTmBPxsRa%2B2yCUx8V1VNluquPKz4y7QS%2Fv%2FmiGAf%2FiHOihYLO%2BzoJD&X-Amz-Signature=02a7fcc52ea4ab6154459610b46b425e1e046e0383e711d457ad9cf183730692&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MIQWVVX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDdFO0iYtdimhXwGzG62iKPuDlzTlBkBytMPJtMT8rdaAIgAMigP%2BLUthYii33W%2F9dPDDixHK%2B5kQqfZmN%2F%2Fe0Tnnsq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHyZXCYVu42qAnVf1CrcA7RFN0h498f6%2BRTbFSgOFZ2pcPY1Z1fXj%2BRhS4pJikYDSwgc9NOMnxK9HlYEHtR0n4Msh2CGGk4QoXKQlVTVGH2D8fpDbys0Qh90fMEukyOkB%2Ftd4Lhs47In5hegYmx6y6RwTAjfYlIlsCX7TbtYjPA79vihk6cXPWIBUvJGrLfwX%2FltZvliUfWnx999x9aG2bsXklpdUIV5w6OQ3GFjbhk%2Fmxnl53voq3uP5LIdFD6nxTeC75Vg8LC2CBj65mWEryIffysl7LTVFwMirVrNIBmfgXKp1olwFiYpA52giz1kRFBBu4nmMAEADxwnqGOn7aDvdmi8hznZP9A381IHdbg4Ky0If3pYsCD6SlGcCaWatRLzHdasglpByAL1V5Atr2t3G5pX6dtuvrB8PexxznviYM%2B4v%2FUfdsQcrF39cYive1qLQy77kTUAZGgXHi%2F1kmn%2FcUhkl9pooo%2FSXbZd7rkLN3T9DVRDBMsnp4Ragh%2BtGltM7F2EHEp%2FePOHidNUZ9%2BI3zM8hs%2BPaP%2B9LnM81V7lIY7T2tZ%2BUhnbLuXVMc3XoP5AAy60OjVA8u%2F%2FQJmlHhm7qgXmUmXpqvC%2B9OKV9Aiyx8shGtJaW4k72CXZh7x6TzOs7Borc2PV%2F3jXMLuLmL0GOqUBtI9Dcq6aqH%2BI2jDypg35XKL6I6MJCs%2BlmkuZDvNudI%2Fikb4vSJ2V6I%2Fvs8I7kvP2%2B1cPnRzIgfRj3OE%2FR5WRK07a8ivD8sIXCRKNBaTfb4IS7nls1xGvUvAU2QZo5wEIbC1AD2xmnFNpr2Sn2CsiYD7Gm%2FUw3ap46nmpY%2BSTmBPxsRa%2B2yCUx8V1VNluquPKz4y7QS%2Fv%2FmiGAf%2FiHOihYLO%2BzoJD&X-Amz-Signature=db3817542ab85f56a9fe1306e9143a64b9bb5764573a0f8e13a9cbee6acf4c6a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MIQWVVX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDdFO0iYtdimhXwGzG62iKPuDlzTlBkBytMPJtMT8rdaAIgAMigP%2BLUthYii33W%2F9dPDDixHK%2B5kQqfZmN%2F%2Fe0Tnnsq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHyZXCYVu42qAnVf1CrcA7RFN0h498f6%2BRTbFSgOFZ2pcPY1Z1fXj%2BRhS4pJikYDSwgc9NOMnxK9HlYEHtR0n4Msh2CGGk4QoXKQlVTVGH2D8fpDbys0Qh90fMEukyOkB%2Ftd4Lhs47In5hegYmx6y6RwTAjfYlIlsCX7TbtYjPA79vihk6cXPWIBUvJGrLfwX%2FltZvliUfWnx999x9aG2bsXklpdUIV5w6OQ3GFjbhk%2Fmxnl53voq3uP5LIdFD6nxTeC75Vg8LC2CBj65mWEryIffysl7LTVFwMirVrNIBmfgXKp1olwFiYpA52giz1kRFBBu4nmMAEADxwnqGOn7aDvdmi8hznZP9A381IHdbg4Ky0If3pYsCD6SlGcCaWatRLzHdasglpByAL1V5Atr2t3G5pX6dtuvrB8PexxznviYM%2B4v%2FUfdsQcrF39cYive1qLQy77kTUAZGgXHi%2F1kmn%2FcUhkl9pooo%2FSXbZd7rkLN3T9DVRDBMsnp4Ragh%2BtGltM7F2EHEp%2FePOHidNUZ9%2BI3zM8hs%2BPaP%2B9LnM81V7lIY7T2tZ%2BUhnbLuXVMc3XoP5AAy60OjVA8u%2F%2FQJmlHhm7qgXmUmXpqvC%2B9OKV9Aiyx8shGtJaW4k72CXZh7x6TzOs7Borc2PV%2F3jXMLuLmL0GOqUBtI9Dcq6aqH%2BI2jDypg35XKL6I6MJCs%2BlmkuZDvNudI%2Fikb4vSJ2V6I%2Fvs8I7kvP2%2B1cPnRzIgfRj3OE%2FR5WRK07a8ivD8sIXCRKNBaTfb4IS7nls1xGvUvAU2QZo5wEIbC1AD2xmnFNpr2Sn2CsiYD7Gm%2FUw3ap46nmpY%2BSTmBPxsRa%2B2yCUx8V1VNluquPKz4y7QS%2Fv%2FmiGAf%2FiHOihYLO%2BzoJD&X-Amz-Signature=c930ff9d07b9d96595a2b7d18360fb11bb19ea6c8d23302dc7f6b68134cd754a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MIQWVVX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDdFO0iYtdimhXwGzG62iKPuDlzTlBkBytMPJtMT8rdaAIgAMigP%2BLUthYii33W%2F9dPDDixHK%2B5kQqfZmN%2F%2Fe0Tnnsq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHyZXCYVu42qAnVf1CrcA7RFN0h498f6%2BRTbFSgOFZ2pcPY1Z1fXj%2BRhS4pJikYDSwgc9NOMnxK9HlYEHtR0n4Msh2CGGk4QoXKQlVTVGH2D8fpDbys0Qh90fMEukyOkB%2Ftd4Lhs47In5hegYmx6y6RwTAjfYlIlsCX7TbtYjPA79vihk6cXPWIBUvJGrLfwX%2FltZvliUfWnx999x9aG2bsXklpdUIV5w6OQ3GFjbhk%2Fmxnl53voq3uP5LIdFD6nxTeC75Vg8LC2CBj65mWEryIffysl7LTVFwMirVrNIBmfgXKp1olwFiYpA52giz1kRFBBu4nmMAEADxwnqGOn7aDvdmi8hznZP9A381IHdbg4Ky0If3pYsCD6SlGcCaWatRLzHdasglpByAL1V5Atr2t3G5pX6dtuvrB8PexxznviYM%2B4v%2FUfdsQcrF39cYive1qLQy77kTUAZGgXHi%2F1kmn%2FcUhkl9pooo%2FSXbZd7rkLN3T9DVRDBMsnp4Ragh%2BtGltM7F2EHEp%2FePOHidNUZ9%2BI3zM8hs%2BPaP%2B9LnM81V7lIY7T2tZ%2BUhnbLuXVMc3XoP5AAy60OjVA8u%2F%2FQJmlHhm7qgXmUmXpqvC%2B9OKV9Aiyx8shGtJaW4k72CXZh7x6TzOs7Borc2PV%2F3jXMLuLmL0GOqUBtI9Dcq6aqH%2BI2jDypg35XKL6I6MJCs%2BlmkuZDvNudI%2Fikb4vSJ2V6I%2Fvs8I7kvP2%2B1cPnRzIgfRj3OE%2FR5WRK07a8ivD8sIXCRKNBaTfb4IS7nls1xGvUvAU2QZo5wEIbC1AD2xmnFNpr2Sn2CsiYD7Gm%2FUw3ap46nmpY%2BSTmBPxsRa%2B2yCUx8V1VNluquPKz4y7QS%2Fv%2FmiGAf%2FiHOihYLO%2BzoJD&X-Amz-Signature=360a628bd99bade29186a9fab823b96d31a88249a23c5852b36c08836ff035f5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MIQWVVX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDdFO0iYtdimhXwGzG62iKPuDlzTlBkBytMPJtMT8rdaAIgAMigP%2BLUthYii33W%2F9dPDDixHK%2B5kQqfZmN%2F%2Fe0Tnnsq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHyZXCYVu42qAnVf1CrcA7RFN0h498f6%2BRTbFSgOFZ2pcPY1Z1fXj%2BRhS4pJikYDSwgc9NOMnxK9HlYEHtR0n4Msh2CGGk4QoXKQlVTVGH2D8fpDbys0Qh90fMEukyOkB%2Ftd4Lhs47In5hegYmx6y6RwTAjfYlIlsCX7TbtYjPA79vihk6cXPWIBUvJGrLfwX%2FltZvliUfWnx999x9aG2bsXklpdUIV5w6OQ3GFjbhk%2Fmxnl53voq3uP5LIdFD6nxTeC75Vg8LC2CBj65mWEryIffysl7LTVFwMirVrNIBmfgXKp1olwFiYpA52giz1kRFBBu4nmMAEADxwnqGOn7aDvdmi8hznZP9A381IHdbg4Ky0If3pYsCD6SlGcCaWatRLzHdasglpByAL1V5Atr2t3G5pX6dtuvrB8PexxznviYM%2B4v%2FUfdsQcrF39cYive1qLQy77kTUAZGgXHi%2F1kmn%2FcUhkl9pooo%2FSXbZd7rkLN3T9DVRDBMsnp4Ragh%2BtGltM7F2EHEp%2FePOHidNUZ9%2BI3zM8hs%2BPaP%2B9LnM81V7lIY7T2tZ%2BUhnbLuXVMc3XoP5AAy60OjVA8u%2F%2FQJmlHhm7qgXmUmXpqvC%2B9OKV9Aiyx8shGtJaW4k72CXZh7x6TzOs7Borc2PV%2F3jXMLuLmL0GOqUBtI9Dcq6aqH%2BI2jDypg35XKL6I6MJCs%2BlmkuZDvNudI%2Fikb4vSJ2V6I%2Fvs8I7kvP2%2B1cPnRzIgfRj3OE%2FR5WRK07a8ivD8sIXCRKNBaTfb4IS7nls1xGvUvAU2QZo5wEIbC1AD2xmnFNpr2Sn2CsiYD7Gm%2FUw3ap46nmpY%2BSTmBPxsRa%2B2yCUx8V1VNluquPKz4y7QS%2Fv%2FmiGAf%2FiHOihYLO%2BzoJD&X-Amz-Signature=331601867381c0d18b48c481295d326ce15a32a7e9194ad781d2aea417ff6d0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMWBXF6D%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCICrlMG5I95taIKBvuaDv4KhZoTnvC39%2BHUSMg%2FtKX1yoAiEAofS%2BZ3CF4Hw0G%2FDU1VFuo4ZMFnu0Jc35EIgPxIwUnBUq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDGQfyEnopUxkEN1PQircA3cqZ6GrhRNjSHbMcC29%2B7TSxDdIz%2FZAfcP0FyLMutCz1p6vOcLtecJ%2BENv8PcioFTwoSTbpnvKHiQgwp3SJB1fdtB7Bsk0L3LJlSxO516lZHl3TUl4VIWsGBV8rvFwS%2FVu9QyMUD0BA%2Fn4DourBM5Vm9YAV2qhrJPyQFtHQAz6MtiRB91I4F2q%2BTmOfYAIyRtbQknWmrHtHHIkicGF3ucIDl5nzJSLBCoIyBNEsA3ZocqBo01jnfu57Op9wDFxNjlepkfOMRFCxjmTJTgYO7SMo3d0kHB4HUewONYmAOHc%2BVOsqCzGjjwcsGNNv5%2Fg1SaygIQgnM54hVI12FkuLNRsuf6vdK3D2m%2BdxI6xaxbk6v9rjMMDJVa4Juzrn3US6PU4LDeKIZt52X5FDfBHUEJl2%2FAfcr%2Fp5jPKuH6mRLm1PpzvcNsXvmkmP3pAX%2BahNSNS03aqtf50uDV2Hcn%2BF0OH3CTheG2FMfXsfXyLG%2F8EUCwZZjaQgIUzJwu0WmRKkhg7rwYWW4KBHyrxQdPHM6fgIQgZp2XRJ5d25VsOHmUrJiJ8st14nD3dc0yh%2BIy3JeThx6OhLY3%2BL%2BaejP%2FI7k99lG8JYLL1s%2FGR5CtYgnSiuZbt%2BlM%2FXe1qUTkHyMOCKmL0GOqUBev%2BPYRQHlRI9nKrs1c%2BXoEkyvhvtIF2sc4VeD57N4D1IgGHCLlvm6ugygP1otRA%2BIZP%2BeOtfs0h%2F%2FTPNkq46ovCpVMmMDz0XD2TtDGwm%2Bxjp3UsCgqWKi9segj6x5cVwsU8zzFv6lk6JlMFBaChR5VduBHGtNYmi2fsZbNufc4ZsESyhpc29YA%2Bk5zXRyLNJfwXsodljq%2F7vOnvlFN1YWAlB2ipb&X-Amz-Signature=e405e855329a479fd55da700fcef260f99ea74aa6a1bb8c4edad0726d1e08afd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TBBU6DU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIEBqk5fX6kCbp7Wt1TJm5LmPOXsAfZNH1TedtObfLSKqAiEAuTfr%2FUjTKU%2FHjuZxRl88Ko8e0Rkpp9LQ9Fb%2FSXT%2BJ2Aq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDNBO3URx8Wh8wFpxuCrcAzjkdxmG7O7%2Fi%2B%2Fz178g%2FO95NOI6S8n0i3gbhvRwHd3A78bjenyMEA%2B9p%2BHoOqfxJ65tk%2B%2FDuyquMEp0GpaA23JrcKqUZpQGboYrfceK1npGO8EkXyby6qLoVOdoFw29QXyIc2ECwe0RQnGF8HbX%2FdS4YVFjrSV5Lcf0cQC40AfKgF1prvIdbG1%2Fx5G9Vo7G1JehbtR2b%2BERE%2BWM2fosH2JqEuFlh9569Y8yG5zKUA96Mrdb2OoeJq5FGZH8bfkiib13Urxn%2B5YgrPYTJInnrxqWyavI9PYtRSMrKKoZOPnxLfn2g29zH5p2eIwzXRX0zRVznWUoTkDpZf1KRstvv7cUIYYmMHDm6gxqYmBoYuU%2FacZd18bGU5%2Bl08FP8HUhYSOZtKBbLHmLnq6BZFsYvhHtWaviKkMPZQJg9LKClbPtrWufdyPg1HwMeIjVHWV6%2Fb79XPPZxmqZ0OEGBkXqKq3Oq0R1Bhx5sq%2FUSb8HB%2FfF0bFeK1AnMG4z5uTBJyGfNg4sfV1xGiAVWLEwXI32lwQegqcEJJoH1hp%2FMHSkgA7qyHfdj6B%2FrCDV6A9n69x6uoQVqA0x9N0%2FGghHaQikDPcrV31x4rfRRpeALUyc2w6ZYr%2BIrBlRu%2F6OuddoMOmKmL0GOqUBfwuKkwEt1K9Tu%2BNNx1Xdkmk5rkIEHCm1Z4EdhuOpbO%2FywyZGZwqJoJQiQ8OLDBa33yEnl5N8Fr7T92JwOpCzPsP8rikS6Kp1VYkJBmCjUMRrFEq80Wtt8EG718EbZbAsYGSkpRnV5BZvTntR8mIwHvDBdKiMiTnMF5v4UJ1yJ0MvcUgFBSF%2Btvj3IGoQdwOVELzmer4CGSZqLowqSZ4yoLPxxawf&X-Amz-Signature=48d698e637f2d078eda88eaf6e3a5c6926a19740322a3cd659a9ce8e909deac6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6V4DVM5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCICHEO2q%2ByYpYLktzpZE62QfC4ez5z1JcJok5BGu6efNWAiEA49yylz%2FvvaS7xOo7eiMjIRxoHpexIBtEqY7NHQG6%2FMsq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCTlHOBnk5d6mDGjDCrcAxWUf%2F1hocaPrCrjOuvTzMsdR2s3Cq0UryeuEjhEr9GY6neQy7n9ptOv%2B6cbBeIpp%2FOOoTZfteiZK0Z9TCElLeG9JFKs33hzDuhPYinq79AJM85UiLPy5%2FOlbKqMOhB0tdnlJVEFrNGeR%2FpE1v9fLOijKUqNHHEO8VQm%2FyD3hXuv299QByNF6i3%2FLDO7YLrl8PCu8Ssz0zTar5jf7%2BBu8TXoNHEi4nyjWkoQyDDCs%2FNHXt%2FOD%2FXNDg4qXqLkcRklrgmLHo7iA9Amksw7GzoBcA8DIa882LhLN0Jc3BBmI1QTR3UnhxBLak2N6aPjeOqmqfMGEdlFSLjdo4Ea%2B1WwFa9zXHtEkRBKQloGQaT7QNq0%2FMF9ayua3nmGqfF4KZ4xmqnmf%2ByiYjqF39F30ilDLe3cDgTrZTuu8YTHjQq2%2BDBaulYCah2KRUDX0IrGVFb37lhPkH3YpK7N2z%2B176IJBcFbOz42P1cc5Kni1E8ZNCpPRr6hc9nPYe7Jg71s%2F8%2BEXNVycCT6U02SVVb76r3F9Nr0Z35aEQlks1Ks6m%2FKmJjPpM%2BdFQzq5vbyLgBQoGrbaUl4xPDIah0p72LgOwme02tlFKSw5Wg5m1LbzzCvv4WORKs95pbZqtbff3SlMO2KmL0GOqUBs0IEPcAWafu06N0qFCYnWUvz2CNZhX4WYGNy29AVr6HKoGxs5sc%2B%2BGw8KcU6JsR7YX5haeGFPp4RemI79K64z1HXanQuo5v2PElx0gFHgVJ2m%2BqgWo%2B5oxicpv8ZpsTeJ1lj%2FGrUKn2VixIBaXxXZ8vZ1PalDeh7en%2FwOYxHIqbiX9Ahp7J1ZvW7eiP8bjV9uj9Jc0N4XfG19Xz7sVZSigilME%2Bq&X-Amz-Signature=028627f74c4dfca8991b483ae47c818b6a223f4acfb64204c65b5c1d84f19303&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6V4DVM5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T132013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCICHEO2q%2ByYpYLktzpZE62QfC4ez5z1JcJok5BGu6efNWAiEA49yylz%2FvvaS7xOo7eiMjIRxoHpexIBtEqY7NHQG6%2FMsq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCTlHOBnk5d6mDGjDCrcAxWUf%2F1hocaPrCrjOuvTzMsdR2s3Cq0UryeuEjhEr9GY6neQy7n9ptOv%2B6cbBeIpp%2FOOoTZfteiZK0Z9TCElLeG9JFKs33hzDuhPYinq79AJM85UiLPy5%2FOlbKqMOhB0tdnlJVEFrNGeR%2FpE1v9fLOijKUqNHHEO8VQm%2FyD3hXuv299QByNF6i3%2FLDO7YLrl8PCu8Ssz0zTar5jf7%2BBu8TXoNHEi4nyjWkoQyDDCs%2FNHXt%2FOD%2FXNDg4qXqLkcRklrgmLHo7iA9Amksw7GzoBcA8DIa882LhLN0Jc3BBmI1QTR3UnhxBLak2N6aPjeOqmqfMGEdlFSLjdo4Ea%2B1WwFa9zXHtEkRBKQloGQaT7QNq0%2FMF9ayua3nmGqfF4KZ4xmqnmf%2ByiYjqF39F30ilDLe3cDgTrZTuu8YTHjQq2%2BDBaulYCah2KRUDX0IrGVFb37lhPkH3YpK7N2z%2B176IJBcFbOz42P1cc5Kni1E8ZNCpPRr6hc9nPYe7Jg71s%2F8%2BEXNVycCT6U02SVVb76r3F9Nr0Z35aEQlks1Ks6m%2FKmJjPpM%2BdFQzq5vbyLgBQoGrbaUl4xPDIah0p72LgOwme02tlFKSw5Wg5m1LbzzCvv4WORKs95pbZqtbff3SlMO2KmL0GOqUBs0IEPcAWafu06N0qFCYnWUvz2CNZhX4WYGNy29AVr6HKoGxs5sc%2B%2BGw8KcU6JsR7YX5haeGFPp4RemI79K64z1HXanQuo5v2PElx0gFHgVJ2m%2BqgWo%2B5oxicpv8ZpsTeJ1lj%2FGrUKn2VixIBaXxXZ8vZ1PalDeh7en%2FwOYxHIqbiX9Ahp7J1ZvW7eiP8bjV9uj9Jc0N4XfG19Xz7sVZSigilME%2Bq&X-Amz-Signature=279c5150ff61a8fb1ff37217b417444fa84ec735c348b6268394e32a0238b352&X-Amz-SignedHeaders=host&x-id=GetObject)
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
