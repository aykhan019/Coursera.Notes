

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5GPHYS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDsCwZs1JeA%2FAEZXFT74vYL8TzltqrzTa4fGJw%2FLuKuTAiEAmXRL5%2BrSsAm9wbhd411bGA3Z2Z0YJomPig7z26j0Y04q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBVPogjBxqHMAYrN%2ByrcA%2BFthawnViPyU9IJ8%2BJQTcEKAOrwoJL49nsfnONwGWVc8wal6K8B5afssY6hoKZdM3nCspXzwgiOwB6vMXoMUqeMlDKgBlkahUK9LocQ65QlP4XJ5lFqey%2BQfOccHEpUjbgLiiD1p2sRVQkovYHc1mOkc%2FcUs17Ayj71sYPOT4drAv590%2F%2BL0kZiCblydL3GbpcscZwHwPno%2BS4TEwZ%2FSj7PDlhNL64GPV6veTm%2FsVSTLizkkS57ppaQxPEjiWzDrOOhJvhWshtCSROUrJlKASY%2FgfPjHVskeRR0wt3N0tY2sDVeMZlNYuXHgt4vAsKs5s333V4l%2BfvVIH5iR7W4JwAZ%2B8KjjglHiqLsU6xMO9tX4VC5yV49JIOIjohzUa%2BxKd5Dfzb2eBJ10oPU1yV44lNc4wpaMHnBeBN6Egby8XapBXTvCg50cKF0zS0FFKELi4dBURn1g04GK3z74lhBBA4oeMk67TwVLfDsyUHQkLgLjJejpF%2FrxiGbnhsxvckbHon8C95DvdBS0XtaVCYbMElT20VU8FSjewcBC2gQzS828u0q9G5PcdsIRd6uY5tmrk6M%2FBUj8H1y1pLP0m35rTy7HR3oQzm0UtAWn7ZZSxumAUunGx1UNL77UZt8ML2alb0GOqUBC7Yp1Qg7%2FFfM0WgoW%2BJPlIDKL1s8Y1U4iQlbjyW%2FvGej%2B%2FqfZC3Vfl%2BMSJVqPTVd6v%2FJgvsGvD5GTDRXV%2Fba%2FXZ8tPNv9ZqsizEZsKDOVLvBdrOiueAXvO9TT9tbGZxHrCrfxnBGn7TT2zg2PwLR8S8ntwQH6IxvR0DzvUQcHc7duumSW8%2Fv0o%2FfJ0ahvRMrUrp2jmLKIbekId030JBFijQoR5p%2F&X-Amz-Signature=d0a9caa750d79fe52c8e1425a2e69d298a6f95424de887e42ba31af7ebbe0a8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5GPHYS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDsCwZs1JeA%2FAEZXFT74vYL8TzltqrzTa4fGJw%2FLuKuTAiEAmXRL5%2BrSsAm9wbhd411bGA3Z2Z0YJomPig7z26j0Y04q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBVPogjBxqHMAYrN%2ByrcA%2BFthawnViPyU9IJ8%2BJQTcEKAOrwoJL49nsfnONwGWVc8wal6K8B5afssY6hoKZdM3nCspXzwgiOwB6vMXoMUqeMlDKgBlkahUK9LocQ65QlP4XJ5lFqey%2BQfOccHEpUjbgLiiD1p2sRVQkovYHc1mOkc%2FcUs17Ayj71sYPOT4drAv590%2F%2BL0kZiCblydL3GbpcscZwHwPno%2BS4TEwZ%2FSj7PDlhNL64GPV6veTm%2FsVSTLizkkS57ppaQxPEjiWzDrOOhJvhWshtCSROUrJlKASY%2FgfPjHVskeRR0wt3N0tY2sDVeMZlNYuXHgt4vAsKs5s333V4l%2BfvVIH5iR7W4JwAZ%2B8KjjglHiqLsU6xMO9tX4VC5yV49JIOIjohzUa%2BxKd5Dfzb2eBJ10oPU1yV44lNc4wpaMHnBeBN6Egby8XapBXTvCg50cKF0zS0FFKELi4dBURn1g04GK3z74lhBBA4oeMk67TwVLfDsyUHQkLgLjJejpF%2FrxiGbnhsxvckbHon8C95DvdBS0XtaVCYbMElT20VU8FSjewcBC2gQzS828u0q9G5PcdsIRd6uY5tmrk6M%2FBUj8H1y1pLP0m35rTy7HR3oQzm0UtAWn7ZZSxumAUunGx1UNL77UZt8ML2alb0GOqUBC7Yp1Qg7%2FFfM0WgoW%2BJPlIDKL1s8Y1U4iQlbjyW%2FvGej%2B%2FqfZC3Vfl%2BMSJVqPTVd6v%2FJgvsGvD5GTDRXV%2Fba%2FXZ8tPNv9ZqsizEZsKDOVLvBdrOiueAXvO9TT9tbGZxHrCrfxnBGn7TT2zg2PwLR8S8ntwQH6IxvR0DzvUQcHc7duumSW8%2Fv0o%2FfJ0ahvRMrUrp2jmLKIbekId030JBFijQoR5p%2F&X-Amz-Signature=f5170104367e61aef79d66ebb5eb23cd65c44d26ecdf7ed8bfcfbb1eeca0b6b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5GPHYS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDsCwZs1JeA%2FAEZXFT74vYL8TzltqrzTa4fGJw%2FLuKuTAiEAmXRL5%2BrSsAm9wbhd411bGA3Z2Z0YJomPig7z26j0Y04q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBVPogjBxqHMAYrN%2ByrcA%2BFthawnViPyU9IJ8%2BJQTcEKAOrwoJL49nsfnONwGWVc8wal6K8B5afssY6hoKZdM3nCspXzwgiOwB6vMXoMUqeMlDKgBlkahUK9LocQ65QlP4XJ5lFqey%2BQfOccHEpUjbgLiiD1p2sRVQkovYHc1mOkc%2FcUs17Ayj71sYPOT4drAv590%2F%2BL0kZiCblydL3GbpcscZwHwPno%2BS4TEwZ%2FSj7PDlhNL64GPV6veTm%2FsVSTLizkkS57ppaQxPEjiWzDrOOhJvhWshtCSROUrJlKASY%2FgfPjHVskeRR0wt3N0tY2sDVeMZlNYuXHgt4vAsKs5s333V4l%2BfvVIH5iR7W4JwAZ%2B8KjjglHiqLsU6xMO9tX4VC5yV49JIOIjohzUa%2BxKd5Dfzb2eBJ10oPU1yV44lNc4wpaMHnBeBN6Egby8XapBXTvCg50cKF0zS0FFKELi4dBURn1g04GK3z74lhBBA4oeMk67TwVLfDsyUHQkLgLjJejpF%2FrxiGbnhsxvckbHon8C95DvdBS0XtaVCYbMElT20VU8FSjewcBC2gQzS828u0q9G5PcdsIRd6uY5tmrk6M%2FBUj8H1y1pLP0m35rTy7HR3oQzm0UtAWn7ZZSxumAUunGx1UNL77UZt8ML2alb0GOqUBC7Yp1Qg7%2FFfM0WgoW%2BJPlIDKL1s8Y1U4iQlbjyW%2FvGej%2B%2FqfZC3Vfl%2BMSJVqPTVd6v%2FJgvsGvD5GTDRXV%2Fba%2FXZ8tPNv9ZqsizEZsKDOVLvBdrOiueAXvO9TT9tbGZxHrCrfxnBGn7TT2zg2PwLR8S8ntwQH6IxvR0DzvUQcHc7duumSW8%2Fv0o%2FfJ0ahvRMrUrp2jmLKIbekId030JBFijQoR5p%2F&X-Amz-Signature=508462fc9750dbed90476840e07a80aa35a29f7c7a46a4a580c1d261919c56df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5GPHYS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDsCwZs1JeA%2FAEZXFT74vYL8TzltqrzTa4fGJw%2FLuKuTAiEAmXRL5%2BrSsAm9wbhd411bGA3Z2Z0YJomPig7z26j0Y04q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBVPogjBxqHMAYrN%2ByrcA%2BFthawnViPyU9IJ8%2BJQTcEKAOrwoJL49nsfnONwGWVc8wal6K8B5afssY6hoKZdM3nCspXzwgiOwB6vMXoMUqeMlDKgBlkahUK9LocQ65QlP4XJ5lFqey%2BQfOccHEpUjbgLiiD1p2sRVQkovYHc1mOkc%2FcUs17Ayj71sYPOT4drAv590%2F%2BL0kZiCblydL3GbpcscZwHwPno%2BS4TEwZ%2FSj7PDlhNL64GPV6veTm%2FsVSTLizkkS57ppaQxPEjiWzDrOOhJvhWshtCSROUrJlKASY%2FgfPjHVskeRR0wt3N0tY2sDVeMZlNYuXHgt4vAsKs5s333V4l%2BfvVIH5iR7W4JwAZ%2B8KjjglHiqLsU6xMO9tX4VC5yV49JIOIjohzUa%2BxKd5Dfzb2eBJ10oPU1yV44lNc4wpaMHnBeBN6Egby8XapBXTvCg50cKF0zS0FFKELi4dBURn1g04GK3z74lhBBA4oeMk67TwVLfDsyUHQkLgLjJejpF%2FrxiGbnhsxvckbHon8C95DvdBS0XtaVCYbMElT20VU8FSjewcBC2gQzS828u0q9G5PcdsIRd6uY5tmrk6M%2FBUj8H1y1pLP0m35rTy7HR3oQzm0UtAWn7ZZSxumAUunGx1UNL77UZt8ML2alb0GOqUBC7Yp1Qg7%2FFfM0WgoW%2BJPlIDKL1s8Y1U4iQlbjyW%2FvGej%2B%2FqfZC3Vfl%2BMSJVqPTVd6v%2FJgvsGvD5GTDRXV%2Fba%2FXZ8tPNv9ZqsizEZsKDOVLvBdrOiueAXvO9TT9tbGZxHrCrfxnBGn7TT2zg2PwLR8S8ntwQH6IxvR0DzvUQcHc7duumSW8%2Fv0o%2FfJ0ahvRMrUrp2jmLKIbekId030JBFijQoR5p%2F&X-Amz-Signature=2a6a2095ea8e416ee775671232779c11a862d4acf1078306de207cb67f6882dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5GPHYS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDsCwZs1JeA%2FAEZXFT74vYL8TzltqrzTa4fGJw%2FLuKuTAiEAmXRL5%2BrSsAm9wbhd411bGA3Z2Z0YJomPig7z26j0Y04q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBVPogjBxqHMAYrN%2ByrcA%2BFthawnViPyU9IJ8%2BJQTcEKAOrwoJL49nsfnONwGWVc8wal6K8B5afssY6hoKZdM3nCspXzwgiOwB6vMXoMUqeMlDKgBlkahUK9LocQ65QlP4XJ5lFqey%2BQfOccHEpUjbgLiiD1p2sRVQkovYHc1mOkc%2FcUs17Ayj71sYPOT4drAv590%2F%2BL0kZiCblydL3GbpcscZwHwPno%2BS4TEwZ%2FSj7PDlhNL64GPV6veTm%2FsVSTLizkkS57ppaQxPEjiWzDrOOhJvhWshtCSROUrJlKASY%2FgfPjHVskeRR0wt3N0tY2sDVeMZlNYuXHgt4vAsKs5s333V4l%2BfvVIH5iR7W4JwAZ%2B8KjjglHiqLsU6xMO9tX4VC5yV49JIOIjohzUa%2BxKd5Dfzb2eBJ10oPU1yV44lNc4wpaMHnBeBN6Egby8XapBXTvCg50cKF0zS0FFKELi4dBURn1g04GK3z74lhBBA4oeMk67TwVLfDsyUHQkLgLjJejpF%2FrxiGbnhsxvckbHon8C95DvdBS0XtaVCYbMElT20VU8FSjewcBC2gQzS828u0q9G5PcdsIRd6uY5tmrk6M%2FBUj8H1y1pLP0m35rTy7HR3oQzm0UtAWn7ZZSxumAUunGx1UNL77UZt8ML2alb0GOqUBC7Yp1Qg7%2FFfM0WgoW%2BJPlIDKL1s8Y1U4iQlbjyW%2FvGej%2B%2FqfZC3Vfl%2BMSJVqPTVd6v%2FJgvsGvD5GTDRXV%2Fba%2FXZ8tPNv9ZqsizEZsKDOVLvBdrOiueAXvO9TT9tbGZxHrCrfxnBGn7TT2zg2PwLR8S8ntwQH6IxvR0DzvUQcHc7duumSW8%2Fv0o%2FfJ0ahvRMrUrp2jmLKIbekId030JBFijQoR5p%2F&X-Amz-Signature=b19ce8351bab039fdaff9333eba27b6c8d22cfead7fbd37cb2cb8c18b04385b6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5GPHYS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDsCwZs1JeA%2FAEZXFT74vYL8TzltqrzTa4fGJw%2FLuKuTAiEAmXRL5%2BrSsAm9wbhd411bGA3Z2Z0YJomPig7z26j0Y04q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBVPogjBxqHMAYrN%2ByrcA%2BFthawnViPyU9IJ8%2BJQTcEKAOrwoJL49nsfnONwGWVc8wal6K8B5afssY6hoKZdM3nCspXzwgiOwB6vMXoMUqeMlDKgBlkahUK9LocQ65QlP4XJ5lFqey%2BQfOccHEpUjbgLiiD1p2sRVQkovYHc1mOkc%2FcUs17Ayj71sYPOT4drAv590%2F%2BL0kZiCblydL3GbpcscZwHwPno%2BS4TEwZ%2FSj7PDlhNL64GPV6veTm%2FsVSTLizkkS57ppaQxPEjiWzDrOOhJvhWshtCSROUrJlKASY%2FgfPjHVskeRR0wt3N0tY2sDVeMZlNYuXHgt4vAsKs5s333V4l%2BfvVIH5iR7W4JwAZ%2B8KjjglHiqLsU6xMO9tX4VC5yV49JIOIjohzUa%2BxKd5Dfzb2eBJ10oPU1yV44lNc4wpaMHnBeBN6Egby8XapBXTvCg50cKF0zS0FFKELi4dBURn1g04GK3z74lhBBA4oeMk67TwVLfDsyUHQkLgLjJejpF%2FrxiGbnhsxvckbHon8C95DvdBS0XtaVCYbMElT20VU8FSjewcBC2gQzS828u0q9G5PcdsIRd6uY5tmrk6M%2FBUj8H1y1pLP0m35rTy7HR3oQzm0UtAWn7ZZSxumAUunGx1UNL77UZt8ML2alb0GOqUBC7Yp1Qg7%2FFfM0WgoW%2BJPlIDKL1s8Y1U4iQlbjyW%2FvGej%2B%2FqfZC3Vfl%2BMSJVqPTVd6v%2FJgvsGvD5GTDRXV%2Fba%2FXZ8tPNv9ZqsizEZsKDOVLvBdrOiueAXvO9TT9tbGZxHrCrfxnBGn7TT2zg2PwLR8S8ntwQH6IxvR0DzvUQcHc7duumSW8%2Fv0o%2FfJ0ahvRMrUrp2jmLKIbekId030JBFijQoR5p%2F&X-Amz-Signature=a97d83c9be2d527edc295b5aafa81294652e2d1612c3c922575d50df19054494&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5GPHYS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDsCwZs1JeA%2FAEZXFT74vYL8TzltqrzTa4fGJw%2FLuKuTAiEAmXRL5%2BrSsAm9wbhd411bGA3Z2Z0YJomPig7z26j0Y04q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBVPogjBxqHMAYrN%2ByrcA%2BFthawnViPyU9IJ8%2BJQTcEKAOrwoJL49nsfnONwGWVc8wal6K8B5afssY6hoKZdM3nCspXzwgiOwB6vMXoMUqeMlDKgBlkahUK9LocQ65QlP4XJ5lFqey%2BQfOccHEpUjbgLiiD1p2sRVQkovYHc1mOkc%2FcUs17Ayj71sYPOT4drAv590%2F%2BL0kZiCblydL3GbpcscZwHwPno%2BS4TEwZ%2FSj7PDlhNL64GPV6veTm%2FsVSTLizkkS57ppaQxPEjiWzDrOOhJvhWshtCSROUrJlKASY%2FgfPjHVskeRR0wt3N0tY2sDVeMZlNYuXHgt4vAsKs5s333V4l%2BfvVIH5iR7W4JwAZ%2B8KjjglHiqLsU6xMO9tX4VC5yV49JIOIjohzUa%2BxKd5Dfzb2eBJ10oPU1yV44lNc4wpaMHnBeBN6Egby8XapBXTvCg50cKF0zS0FFKELi4dBURn1g04GK3z74lhBBA4oeMk67TwVLfDsyUHQkLgLjJejpF%2FrxiGbnhsxvckbHon8C95DvdBS0XtaVCYbMElT20VU8FSjewcBC2gQzS828u0q9G5PcdsIRd6uY5tmrk6M%2FBUj8H1y1pLP0m35rTy7HR3oQzm0UtAWn7ZZSxumAUunGx1UNL77UZt8ML2alb0GOqUBC7Yp1Qg7%2FFfM0WgoW%2BJPlIDKL1s8Y1U4iQlbjyW%2FvGej%2B%2FqfZC3Vfl%2BMSJVqPTVd6v%2FJgvsGvD5GTDRXV%2Fba%2FXZ8tPNv9ZqsizEZsKDOVLvBdrOiueAXvO9TT9tbGZxHrCrfxnBGn7TT2zg2PwLR8S8ntwQH6IxvR0DzvUQcHc7duumSW8%2Fv0o%2FfJ0ahvRMrUrp2jmLKIbekId030JBFijQoR5p%2F&X-Amz-Signature=bbe16ffe1e11c4b95ed08e983de1cd7d9d40defe166e4e6e6876fe76aab7ca86&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA5GPHYS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIDsCwZs1JeA%2FAEZXFT74vYL8TzltqrzTa4fGJw%2FLuKuTAiEAmXRL5%2BrSsAm9wbhd411bGA3Z2Z0YJomPig7z26j0Y04q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDBVPogjBxqHMAYrN%2ByrcA%2BFthawnViPyU9IJ8%2BJQTcEKAOrwoJL49nsfnONwGWVc8wal6K8B5afssY6hoKZdM3nCspXzwgiOwB6vMXoMUqeMlDKgBlkahUK9LocQ65QlP4XJ5lFqey%2BQfOccHEpUjbgLiiD1p2sRVQkovYHc1mOkc%2FcUs17Ayj71sYPOT4drAv590%2F%2BL0kZiCblydL3GbpcscZwHwPno%2BS4TEwZ%2FSj7PDlhNL64GPV6veTm%2FsVSTLizkkS57ppaQxPEjiWzDrOOhJvhWshtCSROUrJlKASY%2FgfPjHVskeRR0wt3N0tY2sDVeMZlNYuXHgt4vAsKs5s333V4l%2BfvVIH5iR7W4JwAZ%2B8KjjglHiqLsU6xMO9tX4VC5yV49JIOIjohzUa%2BxKd5Dfzb2eBJ10oPU1yV44lNc4wpaMHnBeBN6Egby8XapBXTvCg50cKF0zS0FFKELi4dBURn1g04GK3z74lhBBA4oeMk67TwVLfDsyUHQkLgLjJejpF%2FrxiGbnhsxvckbHon8C95DvdBS0XtaVCYbMElT20VU8FSjewcBC2gQzS828u0q9G5PcdsIRd6uY5tmrk6M%2FBUj8H1y1pLP0m35rTy7HR3oQzm0UtAWn7ZZSxumAUunGx1UNL77UZt8ML2alb0GOqUBC7Yp1Qg7%2FFfM0WgoW%2BJPlIDKL1s8Y1U4iQlbjyW%2FvGej%2B%2FqfZC3Vfl%2BMSJVqPTVd6v%2FJgvsGvD5GTDRXV%2Fba%2FXZ8tPNv9ZqsizEZsKDOVLvBdrOiueAXvO9TT9tbGZxHrCrfxnBGn7TT2zg2PwLR8S8ntwQH6IxvR0DzvUQcHc7duumSW8%2Fv0o%2FfJ0ahvRMrUrp2jmLKIbekId030JBFijQoR5p%2F&X-Amz-Signature=7a0cd108214012deae949b2c900ee2b155a3305c80c8a1516932d80130baffc9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKS34HIC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQDZnq6TrcMeku%2FtQ6VccUroSdeTtScP1S%2F3tDP4VNy65gIhAOKypfymUTLP6wFARcP9gSzhfnyb4gU02sBGZu7fgx1LKv8DCGkQABoMNjM3NDIzMTgzODA1IgzIxgTA5l99hV9I3ggq3AO6Tgp%2FLPFQVqCCwwB81org5Li6EPnOghuLvU6VLwujf5g7WP2Jwy0DAqCENtH770NcsZj8bcRkV4kS8OlR9jfTBhB8lSgE%2BIpdys%2BEhr41TEhkRERwaQAuZ1V9EJzYzhJphsfZ7xKLQnZSi8ncWBhCCB1oNe1efoIoAv%2Bt%2FMweDOD%2BovpHzfEnnqmC84PZp21oDBadL5GkSKYtlWuw3%2BCATJbBUa9%2B8uNZoCMcsxu2GuZQqrWPlqH2aa6JgtUbM1SmxxeObMuPiR7LIxcC2qTnb5Khur8qODVF8tquOvnxVs9EDPec%2BjhVpXaiPPy0kaOSHHi80FS6T45rLT12iS6P2I8TkUx1f%2FxEKMXPZ2SWtbRfxPRUxcilkjfC8vu%2FDio%2BXVMXHYIntbVIv92U1l0sBSSiOfNiALKLcggztHvnxHhoeLMSXCoT3UWxKWOh1N6j83qwokx4h3Oy2Z1j5MPTilLJxmBMg7RMtpASyN%2B%2BJqtudy2JG%2FAYFgkMpiRHGNjqNfaZdXrJkmh1bETctLi4bmRUL6OBT7%2FUMiol%2Bctiz16Ym1ETgCSpBlF3%2BJIXP9YijshHMkuxbt4HEwEOkerzR2VV0%2Bk%2Fusz%2FdLxM9Ub8F7KG3vB2CMM0HZNIiDD3mZW9BjqkARlF2aZtysqs6rvPwiD9%2FEZVin3utCCp9n6cNdS1ZYNF9RJa0dJnHvAIkd3jIXXW4yJUOo5ycni1dynKvsbPwHvcHFn0Bbjgm4RbTAkRy42RZlZwX0z%2FTRtkEEsEYrBOW7W3ha6wQkigD3CIKdDlxabVKAGPD53iEpMPOlyxrUfMREfcFf15wywV0gh6mwTcyPy0mHb%2BUweaTFRFObF7HTnC8wUv&X-Amz-Signature=a8a5230de9e4c4489cd3aefb581ba546a333b2b57908e0eac50c1f4e59dfb664&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPJRYJAR%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCblHiPrkPGzGzy0cWNSWaFHXyjGU7VY%2BxgWr7FlkXH9gIgUlB0XVlFkc102t1ysfBzONJOr6jmAg6Su7zSbdnJ9Cwq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDILXhOiYDavfjL%2BcqSrcAwKKAORAMtUAch3tTGgLapppUd7yYK8yPmeV7bvDrv193EEPAfJvTkoDbuoLGl9K9NOjVkJRPjmhHWzgFtL%2BKAGsVyMf2DrW4m2nK9j3B7%2F4aDduLTtdO30BUw7jIMEGZ82u7zW8M%2FjhNvW4aIMghPKCmIK3Ne7z1pSNpkAc4pmdANichQcRdBFRNWx%2FDUlkShBCn88iKVDLHvNz3pGpuPHZrNevLWxx%2B271HJ1bZzYer6NkYcUgvhix1UriITj0xPfplkcSCyV71JY3nXsTY%2BPc0VnqbRbh8TH30ecgeYz2A0svYjsqtohEnFRLAbjq4ty10Pt4KGqDh5CyB72mu01fdM9uRmslcTajzGqmcmSczru5nRd6o%2F19ATYm2QSq8Sf3qr6JAUxf8FEyG9jVSLKTf%2FyZV4I8k2ZIg4R4fSX4OHhbnpP1eWMrP0HdPrckfjNHJm0LLgrOCahp6T4R5UYsxvAhqiIx5ck7MAfec6XmRZYrW2%2FFHnr60x5CNlOacNrS9RaBUJ4dpsGWQZXmzYKbsT7mn%2BktM65AlsZZOrVjFHsp3MRxtTITHPV6g3b%2BLxmTDFSTaMOyLz5tys6DxCqz8Ou8BPsoDDjUErJ8%2Brsuk5oeHc9EAcDq0GEHMJqalb0GOqUBVJjyOMpt4Demeqd%2BxdDVb9uuC89wXymh1Kgn4wBJ1XQanK0X%2Fdryt%2FxWSDtVepWdY14%2Fort1qpUdTefIYGOmu3GpGS%2BpwraIy%2BNtKv%2FteOiSUfACsPC%2B6iTelR4Lvy%2BfdHyAks4YUyZYP7Itn74JOeGLBE7wps7exxlYT2Im%2FppUQBeGxxBZnawX9vVpBlitI8eVUIxRCj9%2FBuDkd%2BMo2lFZm%2BZQ&X-Amz-Signature=bb3da33c9a52992c08ecf05d3926bf7a86451821a5dd9a9d4a590d1778a4226e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC5BOTED%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD379iEgL9diIkwBlFyPxOesK0sFyYrmBGs%2FWM9G11spwIgOmVJXZjZgHk4ej202TGjx8IHOgk%2BwKHJNXzzAY4j07Yq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDGtNQYHChBoTHA0IxSrcA%2FtQ6Vs693wzXkjRrt8GXTVjSSOiJcA%2Bb0nL4S7OY9EUqfwMkGuaYd0nwXm8MDbZE81X4G%2F%2BdlkiJhLhxYzNFE3W1vvbfHVBjJyzblgSqa564QOE9bupVQWa8FpHrQrGwChoJF5BdFaQl4J1CnWarJwXlaiJJObdvAwuQmwTeHv%2BBNV9M4N9a1NICCyavDUE%2FxFc3krvb%2Fz1dwAfIDz0ZEEfN8bsvMuoc2WfNVpQk%2BnyzAEU%2B%2FFnWd18y%2BjrS2b%2FxOnbaNLit%2FCWM3xqntAgbFtF%2F3iRnToL%2FmrH2G3shqADhN444n45N0KWJotknisWPw%2FqgcMCp7Z%2B1Hmvi5PJLceuOS23icU1LDkrbUmi4JqzzQvahzyMS%2FVHG7xsfLJmvRN2%2FI95E%2FstSB2U9WTduEqn02GWOb2O9%2BrfbTFwvNjac3RXfMaFm8%2F3vOuMKalpEAWF8yj3ss%2FALqNwwn4kZqEUvX87QXLZ7cHKiEfNf%2FhUkBUZnrkm%2FTcn1wtNne3MqkKJlhqVQeTJwmHDvSC2VNlCeIDnbMxFyebyCmohjL9r6JliorFXwpOQfwhZ5ZneBS3bn15dm671hTzDgqkb8x8YKWxdQXj55DX8El9zXVN07YDzeDLbQoRWFdZ3MJualb0GOqUBGaOlrF4Ng2kdWSStekICmNfHHYCiCeJ7SjPoIk5Fqqaf%2Bc5qK1wMGin2h6RApY%2Bxoo50S1ZQT8BYPtiFe63jhae6oWqoLYSA26QYEdFS04j4ZFqdEpFJXCn4SxFpvQ1%2Fx2j6GSwpa0zPgEtQ1E5sGwI%2BjV77uOhi5%2Beetz72cSFLiPk9hWx5Dm7VKm8xRAnsOL4pu6aE1W%2FH7gc9R3cNnOa27HbR&X-Amz-Signature=881b76959a15beaf1cc33baca285c316c3feee1af7e1f370b0d7f52b774794c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC5BOTED%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQD379iEgL9diIkwBlFyPxOesK0sFyYrmBGs%2FWM9G11spwIgOmVJXZjZgHk4ej202TGjx8IHOgk%2BwKHJNXzzAY4j07Yq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDGtNQYHChBoTHA0IxSrcA%2FtQ6Vs693wzXkjRrt8GXTVjSSOiJcA%2Bb0nL4S7OY9EUqfwMkGuaYd0nwXm8MDbZE81X4G%2F%2BdlkiJhLhxYzNFE3W1vvbfHVBjJyzblgSqa564QOE9bupVQWa8FpHrQrGwChoJF5BdFaQl4J1CnWarJwXlaiJJObdvAwuQmwTeHv%2BBNV9M4N9a1NICCyavDUE%2FxFc3krvb%2Fz1dwAfIDz0ZEEfN8bsvMuoc2WfNVpQk%2BnyzAEU%2B%2FFnWd18y%2BjrS2b%2FxOnbaNLit%2FCWM3xqntAgbFtF%2F3iRnToL%2FmrH2G3shqADhN444n45N0KWJotknisWPw%2FqgcMCp7Z%2B1Hmvi5PJLceuOS23icU1LDkrbUmi4JqzzQvahzyMS%2FVHG7xsfLJmvRN2%2FI95E%2FstSB2U9WTduEqn02GWOb2O9%2BrfbTFwvNjac3RXfMaFm8%2F3vOuMKalpEAWF8yj3ss%2FALqNwwn4kZqEUvX87QXLZ7cHKiEfNf%2FhUkBUZnrkm%2FTcn1wtNne3MqkKJlhqVQeTJwmHDvSC2VNlCeIDnbMxFyebyCmohjL9r6JliorFXwpOQfwhZ5ZneBS3bn15dm671hTzDgqkb8x8YKWxdQXj55DX8El9zXVN07YDzeDLbQoRWFdZ3MJualb0GOqUBGaOlrF4Ng2kdWSStekICmNfHHYCiCeJ7SjPoIk5Fqqaf%2Bc5qK1wMGin2h6RApY%2Bxoo50S1ZQT8BYPtiFe63jhae6oWqoLYSA26QYEdFS04j4ZFqdEpFJXCn4SxFpvQ1%2Fx2j6GSwpa0zPgEtQ1E5sGwI%2BjV77uOhi5%2Beetz72cSFLiPk9hWx5Dm7VKm8xRAnsOL4pu6aE1W%2FH7gc9R3cNnOa27HbR&X-Amz-Signature=045f8eebc6d282b1e81304ce0238187d3bd5f109d2650537ca1b3300a9c6ab8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
