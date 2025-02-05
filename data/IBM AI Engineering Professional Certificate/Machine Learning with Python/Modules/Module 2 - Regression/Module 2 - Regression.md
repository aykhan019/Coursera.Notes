

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JJ55YU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBqNTzsKYvdkXEwyBX9FgLKamNz78ULTwX84jIsUEDf%2FAiA3cUNs4ugSNftmpMzz1uI164AGyaxH7%2BYkfz2r93ohzir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMGOU%2FwtzwcKcQSnMMKtwDUzm8BA2xHeubFltpK9HlXCyP4Xm4MV6Uzpn521%2BiM%2Filc%2FQjNYbrOvFHY%2BowmJnx2ybCg3OvPxA8JkWpnzu78sSaavrgCocy7ra%2BrTHIImSuN1wNoz%2BOQ3mNYemxYg8kTW1ITPBBmdlbyNbVYl%2B9Yht5gpP3uABwpj2%2FqjErHExzHuMtLWL5UMpuIzZlg89WcpL3BH7Vv%2BmUVmRc%2FrIOX9iw%2FDDa4ipB%2F1vtx0xKtQsbS2fNFVYX%2Fe1MNefIaYQQEaykvNyuNEWh298%2FCVxKq7o4Zx1SFWIM%2BuklrWY32U8f1YgaYieOj2BY4sMDRL8Gdg58J3jRRBIIndsqhZzSQ%2BEynAeSPo7aj4vI1cubx%2BVJGFIR0%2ButQIfdoVbELIqbuZ8SypLKHzfgE5ZUxglWhiM7BlFUJOPvZhqXp2i%2BSdBJvlAUt%2BtaUUZh0tHOLJEq8tgqyV12uqy99IWawvlO0tqUY53XE3guFjB36xluiPs7e4lft%2Fx8SMPIBm%2F7bI07pWP2e%2F%2FTQoYd7cf0eM3Gpyz6%2Bb5tSQ5unperfD1wS5UX2OcjaQnHrjuQs2NOy7Q3z4qmqw2qRud%2FFZDHDv0A%2F%2BKBkgn4lUDhOmBp%2FHXrRTlb5PR%2BQfrn%2B1shrkAwmbqOvQY6pgHQL1Uvr4aWs%2B3w9K79VCcw9MIKnS2AC1k1Ues4%2BvI0yKtmbwAE00TZV823APrHpAE9WlX%2Fp5AN1S6tMZsMFrpLSrh8YZWMlsUdsWysSf12n2JxjT93smxAZhzeVLKE4cXhW2778GCp0d4DFGRXk6YALAK8KDV8STwwsQtgmhoo3LXtL04ySM1R%2FZjIlHVnre3YP5hPXw2g9K9lyQggGakrAEUmweFy&X-Amz-Signature=23146b855968d5b290e2d5d9fc6ebd8c216edaecc4a0ff2b13586e11282b34b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JJ55YU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBqNTzsKYvdkXEwyBX9FgLKamNz78ULTwX84jIsUEDf%2FAiA3cUNs4ugSNftmpMzz1uI164AGyaxH7%2BYkfz2r93ohzir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMGOU%2FwtzwcKcQSnMMKtwDUzm8BA2xHeubFltpK9HlXCyP4Xm4MV6Uzpn521%2BiM%2Filc%2FQjNYbrOvFHY%2BowmJnx2ybCg3OvPxA8JkWpnzu78sSaavrgCocy7ra%2BrTHIImSuN1wNoz%2BOQ3mNYemxYg8kTW1ITPBBmdlbyNbVYl%2B9Yht5gpP3uABwpj2%2FqjErHExzHuMtLWL5UMpuIzZlg89WcpL3BH7Vv%2BmUVmRc%2FrIOX9iw%2FDDa4ipB%2F1vtx0xKtQsbS2fNFVYX%2Fe1MNefIaYQQEaykvNyuNEWh298%2FCVxKq7o4Zx1SFWIM%2BuklrWY32U8f1YgaYieOj2BY4sMDRL8Gdg58J3jRRBIIndsqhZzSQ%2BEynAeSPo7aj4vI1cubx%2BVJGFIR0%2ButQIfdoVbELIqbuZ8SypLKHzfgE5ZUxglWhiM7BlFUJOPvZhqXp2i%2BSdBJvlAUt%2BtaUUZh0tHOLJEq8tgqyV12uqy99IWawvlO0tqUY53XE3guFjB36xluiPs7e4lft%2Fx8SMPIBm%2F7bI07pWP2e%2F%2FTQoYd7cf0eM3Gpyz6%2Bb5tSQ5unperfD1wS5UX2OcjaQnHrjuQs2NOy7Q3z4qmqw2qRud%2FFZDHDv0A%2F%2BKBkgn4lUDhOmBp%2FHXrRTlb5PR%2BQfrn%2B1shrkAwmbqOvQY6pgHQL1Uvr4aWs%2B3w9K79VCcw9MIKnS2AC1k1Ues4%2BvI0yKtmbwAE00TZV823APrHpAE9WlX%2Fp5AN1S6tMZsMFrpLSrh8YZWMlsUdsWysSf12n2JxjT93smxAZhzeVLKE4cXhW2778GCp0d4DFGRXk6YALAK8KDV8STwwsQtgmhoo3LXtL04ySM1R%2FZjIlHVnre3YP5hPXw2g9K9lyQggGakrAEUmweFy&X-Amz-Signature=52ace1519506df76f7752c2fc50874b08d52de1abd2816304951e0e9a861d863&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JJ55YU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBqNTzsKYvdkXEwyBX9FgLKamNz78ULTwX84jIsUEDf%2FAiA3cUNs4ugSNftmpMzz1uI164AGyaxH7%2BYkfz2r93ohzir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMGOU%2FwtzwcKcQSnMMKtwDUzm8BA2xHeubFltpK9HlXCyP4Xm4MV6Uzpn521%2BiM%2Filc%2FQjNYbrOvFHY%2BowmJnx2ybCg3OvPxA8JkWpnzu78sSaavrgCocy7ra%2BrTHIImSuN1wNoz%2BOQ3mNYemxYg8kTW1ITPBBmdlbyNbVYl%2B9Yht5gpP3uABwpj2%2FqjErHExzHuMtLWL5UMpuIzZlg89WcpL3BH7Vv%2BmUVmRc%2FrIOX9iw%2FDDa4ipB%2F1vtx0xKtQsbS2fNFVYX%2Fe1MNefIaYQQEaykvNyuNEWh298%2FCVxKq7o4Zx1SFWIM%2BuklrWY32U8f1YgaYieOj2BY4sMDRL8Gdg58J3jRRBIIndsqhZzSQ%2BEynAeSPo7aj4vI1cubx%2BVJGFIR0%2ButQIfdoVbELIqbuZ8SypLKHzfgE5ZUxglWhiM7BlFUJOPvZhqXp2i%2BSdBJvlAUt%2BtaUUZh0tHOLJEq8tgqyV12uqy99IWawvlO0tqUY53XE3guFjB36xluiPs7e4lft%2Fx8SMPIBm%2F7bI07pWP2e%2F%2FTQoYd7cf0eM3Gpyz6%2Bb5tSQ5unperfD1wS5UX2OcjaQnHrjuQs2NOy7Q3z4qmqw2qRud%2FFZDHDv0A%2F%2BKBkgn4lUDhOmBp%2FHXrRTlb5PR%2BQfrn%2B1shrkAwmbqOvQY6pgHQL1Uvr4aWs%2B3w9K79VCcw9MIKnS2AC1k1Ues4%2BvI0yKtmbwAE00TZV823APrHpAE9WlX%2Fp5AN1S6tMZsMFrpLSrh8YZWMlsUdsWysSf12n2JxjT93smxAZhzeVLKE4cXhW2778GCp0d4DFGRXk6YALAK8KDV8STwwsQtgmhoo3LXtL04ySM1R%2FZjIlHVnre3YP5hPXw2g9K9lyQggGakrAEUmweFy&X-Amz-Signature=40949a15737a21800f31515b6d6be3fcec8e2abb1bf580c94df0b32605056bfc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JJ55YU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBqNTzsKYvdkXEwyBX9FgLKamNz78ULTwX84jIsUEDf%2FAiA3cUNs4ugSNftmpMzz1uI164AGyaxH7%2BYkfz2r93ohzir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMGOU%2FwtzwcKcQSnMMKtwDUzm8BA2xHeubFltpK9HlXCyP4Xm4MV6Uzpn521%2BiM%2Filc%2FQjNYbrOvFHY%2BowmJnx2ybCg3OvPxA8JkWpnzu78sSaavrgCocy7ra%2BrTHIImSuN1wNoz%2BOQ3mNYemxYg8kTW1ITPBBmdlbyNbVYl%2B9Yht5gpP3uABwpj2%2FqjErHExzHuMtLWL5UMpuIzZlg89WcpL3BH7Vv%2BmUVmRc%2FrIOX9iw%2FDDa4ipB%2F1vtx0xKtQsbS2fNFVYX%2Fe1MNefIaYQQEaykvNyuNEWh298%2FCVxKq7o4Zx1SFWIM%2BuklrWY32U8f1YgaYieOj2BY4sMDRL8Gdg58J3jRRBIIndsqhZzSQ%2BEynAeSPo7aj4vI1cubx%2BVJGFIR0%2ButQIfdoVbELIqbuZ8SypLKHzfgE5ZUxglWhiM7BlFUJOPvZhqXp2i%2BSdBJvlAUt%2BtaUUZh0tHOLJEq8tgqyV12uqy99IWawvlO0tqUY53XE3guFjB36xluiPs7e4lft%2Fx8SMPIBm%2F7bI07pWP2e%2F%2FTQoYd7cf0eM3Gpyz6%2Bb5tSQ5unperfD1wS5UX2OcjaQnHrjuQs2NOy7Q3z4qmqw2qRud%2FFZDHDv0A%2F%2BKBkgn4lUDhOmBp%2FHXrRTlb5PR%2BQfrn%2B1shrkAwmbqOvQY6pgHQL1Uvr4aWs%2B3w9K79VCcw9MIKnS2AC1k1Ues4%2BvI0yKtmbwAE00TZV823APrHpAE9WlX%2Fp5AN1S6tMZsMFrpLSrh8YZWMlsUdsWysSf12n2JxjT93smxAZhzeVLKE4cXhW2778GCp0d4DFGRXk6YALAK8KDV8STwwsQtgmhoo3LXtL04ySM1R%2FZjIlHVnre3YP5hPXw2g9K9lyQggGakrAEUmweFy&X-Amz-Signature=6875eba3fd1eb1e5a13522f132fdfee1a973a4a98a1753b572ebe16ecad07540&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JJ55YU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBqNTzsKYvdkXEwyBX9FgLKamNz78ULTwX84jIsUEDf%2FAiA3cUNs4ugSNftmpMzz1uI164AGyaxH7%2BYkfz2r93ohzir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMGOU%2FwtzwcKcQSnMMKtwDUzm8BA2xHeubFltpK9HlXCyP4Xm4MV6Uzpn521%2BiM%2Filc%2FQjNYbrOvFHY%2BowmJnx2ybCg3OvPxA8JkWpnzu78sSaavrgCocy7ra%2BrTHIImSuN1wNoz%2BOQ3mNYemxYg8kTW1ITPBBmdlbyNbVYl%2B9Yht5gpP3uABwpj2%2FqjErHExzHuMtLWL5UMpuIzZlg89WcpL3BH7Vv%2BmUVmRc%2FrIOX9iw%2FDDa4ipB%2F1vtx0xKtQsbS2fNFVYX%2Fe1MNefIaYQQEaykvNyuNEWh298%2FCVxKq7o4Zx1SFWIM%2BuklrWY32U8f1YgaYieOj2BY4sMDRL8Gdg58J3jRRBIIndsqhZzSQ%2BEynAeSPo7aj4vI1cubx%2BVJGFIR0%2ButQIfdoVbELIqbuZ8SypLKHzfgE5ZUxglWhiM7BlFUJOPvZhqXp2i%2BSdBJvlAUt%2BtaUUZh0tHOLJEq8tgqyV12uqy99IWawvlO0tqUY53XE3guFjB36xluiPs7e4lft%2Fx8SMPIBm%2F7bI07pWP2e%2F%2FTQoYd7cf0eM3Gpyz6%2Bb5tSQ5unperfD1wS5UX2OcjaQnHrjuQs2NOy7Q3z4qmqw2qRud%2FFZDHDv0A%2F%2BKBkgn4lUDhOmBp%2FHXrRTlb5PR%2BQfrn%2B1shrkAwmbqOvQY6pgHQL1Uvr4aWs%2B3w9K79VCcw9MIKnS2AC1k1Ues4%2BvI0yKtmbwAE00TZV823APrHpAE9WlX%2Fp5AN1S6tMZsMFrpLSrh8YZWMlsUdsWysSf12n2JxjT93smxAZhzeVLKE4cXhW2778GCp0d4DFGRXk6YALAK8KDV8STwwsQtgmhoo3LXtL04ySM1R%2FZjIlHVnre3YP5hPXw2g9K9lyQggGakrAEUmweFy&X-Amz-Signature=3bb7596d7275069261921325651b710990233b79d517f9875ee28adeec88919b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JJ55YU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBqNTzsKYvdkXEwyBX9FgLKamNz78ULTwX84jIsUEDf%2FAiA3cUNs4ugSNftmpMzz1uI164AGyaxH7%2BYkfz2r93ohzir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMGOU%2FwtzwcKcQSnMMKtwDUzm8BA2xHeubFltpK9HlXCyP4Xm4MV6Uzpn521%2BiM%2Filc%2FQjNYbrOvFHY%2BowmJnx2ybCg3OvPxA8JkWpnzu78sSaavrgCocy7ra%2BrTHIImSuN1wNoz%2BOQ3mNYemxYg8kTW1ITPBBmdlbyNbVYl%2B9Yht5gpP3uABwpj2%2FqjErHExzHuMtLWL5UMpuIzZlg89WcpL3BH7Vv%2BmUVmRc%2FrIOX9iw%2FDDa4ipB%2F1vtx0xKtQsbS2fNFVYX%2Fe1MNefIaYQQEaykvNyuNEWh298%2FCVxKq7o4Zx1SFWIM%2BuklrWY32U8f1YgaYieOj2BY4sMDRL8Gdg58J3jRRBIIndsqhZzSQ%2BEynAeSPo7aj4vI1cubx%2BVJGFIR0%2ButQIfdoVbELIqbuZ8SypLKHzfgE5ZUxglWhiM7BlFUJOPvZhqXp2i%2BSdBJvlAUt%2BtaUUZh0tHOLJEq8tgqyV12uqy99IWawvlO0tqUY53XE3guFjB36xluiPs7e4lft%2Fx8SMPIBm%2F7bI07pWP2e%2F%2FTQoYd7cf0eM3Gpyz6%2Bb5tSQ5unperfD1wS5UX2OcjaQnHrjuQs2NOy7Q3z4qmqw2qRud%2FFZDHDv0A%2F%2BKBkgn4lUDhOmBp%2FHXrRTlb5PR%2BQfrn%2B1shrkAwmbqOvQY6pgHQL1Uvr4aWs%2B3w9K79VCcw9MIKnS2AC1k1Ues4%2BvI0yKtmbwAE00TZV823APrHpAE9WlX%2Fp5AN1S6tMZsMFrpLSrh8YZWMlsUdsWysSf12n2JxjT93smxAZhzeVLKE4cXhW2778GCp0d4DFGRXk6YALAK8KDV8STwwsQtgmhoo3LXtL04ySM1R%2FZjIlHVnre3YP5hPXw2g9K9lyQggGakrAEUmweFy&X-Amz-Signature=a8f5bf00028a8f5c1311a509bef3861f04dbc745107967c9c1ba1d0fa7a2b73b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JJ55YU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBqNTzsKYvdkXEwyBX9FgLKamNz78ULTwX84jIsUEDf%2FAiA3cUNs4ugSNftmpMzz1uI164AGyaxH7%2BYkfz2r93ohzir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMGOU%2FwtzwcKcQSnMMKtwDUzm8BA2xHeubFltpK9HlXCyP4Xm4MV6Uzpn521%2BiM%2Filc%2FQjNYbrOvFHY%2BowmJnx2ybCg3OvPxA8JkWpnzu78sSaavrgCocy7ra%2BrTHIImSuN1wNoz%2BOQ3mNYemxYg8kTW1ITPBBmdlbyNbVYl%2B9Yht5gpP3uABwpj2%2FqjErHExzHuMtLWL5UMpuIzZlg89WcpL3BH7Vv%2BmUVmRc%2FrIOX9iw%2FDDa4ipB%2F1vtx0xKtQsbS2fNFVYX%2Fe1MNefIaYQQEaykvNyuNEWh298%2FCVxKq7o4Zx1SFWIM%2BuklrWY32U8f1YgaYieOj2BY4sMDRL8Gdg58J3jRRBIIndsqhZzSQ%2BEynAeSPo7aj4vI1cubx%2BVJGFIR0%2ButQIfdoVbELIqbuZ8SypLKHzfgE5ZUxglWhiM7BlFUJOPvZhqXp2i%2BSdBJvlAUt%2BtaUUZh0tHOLJEq8tgqyV12uqy99IWawvlO0tqUY53XE3guFjB36xluiPs7e4lft%2Fx8SMPIBm%2F7bI07pWP2e%2F%2FTQoYd7cf0eM3Gpyz6%2Bb5tSQ5unperfD1wS5UX2OcjaQnHrjuQs2NOy7Q3z4qmqw2qRud%2FFZDHDv0A%2F%2BKBkgn4lUDhOmBp%2FHXrRTlb5PR%2BQfrn%2B1shrkAwmbqOvQY6pgHQL1Uvr4aWs%2B3w9K79VCcw9MIKnS2AC1k1Ues4%2BvI0yKtmbwAE00TZV823APrHpAE9WlX%2Fp5AN1S6tMZsMFrpLSrh8YZWMlsUdsWysSf12n2JxjT93smxAZhzeVLKE4cXhW2778GCp0d4DFGRXk6YALAK8KDV8STwwsQtgmhoo3LXtL04ySM1R%2FZjIlHVnre3YP5hPXw2g9K9lyQggGakrAEUmweFy&X-Amz-Signature=4fd7943c15f6653e01827296a0fc14b53d67483fa2fa4d454d0bc46fc6da7420&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674JJ55YU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBqNTzsKYvdkXEwyBX9FgLKamNz78ULTwX84jIsUEDf%2FAiA3cUNs4ugSNftmpMzz1uI164AGyaxH7%2BYkfz2r93ohzir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMGOU%2FwtzwcKcQSnMMKtwDUzm8BA2xHeubFltpK9HlXCyP4Xm4MV6Uzpn521%2BiM%2Filc%2FQjNYbrOvFHY%2BowmJnx2ybCg3OvPxA8JkWpnzu78sSaavrgCocy7ra%2BrTHIImSuN1wNoz%2BOQ3mNYemxYg8kTW1ITPBBmdlbyNbVYl%2B9Yht5gpP3uABwpj2%2FqjErHExzHuMtLWL5UMpuIzZlg89WcpL3BH7Vv%2BmUVmRc%2FrIOX9iw%2FDDa4ipB%2F1vtx0xKtQsbS2fNFVYX%2Fe1MNefIaYQQEaykvNyuNEWh298%2FCVxKq7o4Zx1SFWIM%2BuklrWY32U8f1YgaYieOj2BY4sMDRL8Gdg58J3jRRBIIndsqhZzSQ%2BEynAeSPo7aj4vI1cubx%2BVJGFIR0%2ButQIfdoVbELIqbuZ8SypLKHzfgE5ZUxglWhiM7BlFUJOPvZhqXp2i%2BSdBJvlAUt%2BtaUUZh0tHOLJEq8tgqyV12uqy99IWawvlO0tqUY53XE3guFjB36xluiPs7e4lft%2Fx8SMPIBm%2F7bI07pWP2e%2F%2FTQoYd7cf0eM3Gpyz6%2Bb5tSQ5unperfD1wS5UX2OcjaQnHrjuQs2NOy7Q3z4qmqw2qRud%2FFZDHDv0A%2F%2BKBkgn4lUDhOmBp%2FHXrRTlb5PR%2BQfrn%2B1shrkAwmbqOvQY6pgHQL1Uvr4aWs%2B3w9K79VCcw9MIKnS2AC1k1Ues4%2BvI0yKtmbwAE00TZV823APrHpAE9WlX%2Fp5AN1S6tMZsMFrpLSrh8YZWMlsUdsWysSf12n2JxjT93smxAZhzeVLKE4cXhW2778GCp0d4DFGRXk6YALAK8KDV8STwwsQtgmhoo3LXtL04ySM1R%2FZjIlHVnre3YP5hPXw2g9K9lyQggGakrAEUmweFy&X-Amz-Signature=e9952641879ed8e07e0f56e75dc280f7991c77448694e09b3aa9497041384256&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUJPTAIO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCwg0z18lC8tHKCsU6MSeSLY%2FKM1Lct4i%2FY%2B5Xa5gH0LwIgVmDjproedjvmIwYgvnB%2Fa7Yt7SwSAZjPjMevwfEJt4Qq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDGh3iCbrUfj5dalgHircA2s6Ap2ib%2FRK57j1VCxYIUUtt5v71zyBtBhxET6ax4ejTaor0IHDKZj6csnIY6Z4EwmOIc6JLR0ZSn9LshF0MOkJV4xFKyelO4ueE1Gev6mhHqfuT5vWqVJMYUAcT8KvTftN5%2BXzoc73RNLkjpKqfrfljMJE4ve8QW5RZ5xjpo1YOv0U8DrWI8%2FZCGbhve2SCMoAV%2F1xn789EuEPBQSxOdQORSToyu3MWxnhLTpqoRUAGoatkgUAawg6WXpPRxtrmDilcCUBeNUyqjF6H23K30ceRbsWw5q%2FmO5SfgmImkqgGRIHrstr5R7Ibf%2BBX5AF3vp0OmeudaBDaMZtgOpRMLuE%2FcpS94KkMOibXJ1h7%2FSicr6xvo6zCSlu3j2i7KyIovinYE5lTUVgOEV8xYufvVGHbcANZgn6zKXZSWRR3ers8nLiOMfvBUT4%2BabZit2uBph9FBUf4oy1nZJWuzBRNf%2BaOyVMfTe1l5v6YYiXrFlJkymCKn68DrqgmkTgYSxQkgMKfYJLIejDKXsaRXavrlfgDocdBIXWX79yX4izRt3JQlFxuJzyXsfT3NAmn4S6sIhe%2BPatxFOK32T2pUONyqB4MPtOkRGDMC%2B8ZGI8Esb7I3Nv37INi2asqMoXMOW6jr0GOqUBoX9rJejfQo%2Bdjhct2YQyO%2F9OYGnKWXEqEeyhfDaWxaO4R1kMf7k6cMQFp%2Fxe%2FMVXFWllt%2BZ9zetCAIh2lob%2FB84EKC8WDAi9ixE1tIqrMZQ7a8LNv%2FQtHvAHAA%2FByKG0Zq%2BgPpWP2e%2FVdVFw7vAhKV9KXfNN0eedVFKxR%2Bhv5d8GRjkJ54CisQ%2BGOB0vBaDHSl72%2BqzXJaZ1NeH%2FcjpeWyzeF8Hn&X-Amz-Signature=8f8efee051df04628abd9199e9e982e4aec08613b18e8b617242c05185dfbe07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKLAD2R5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIH9KjZ0fB%2Fe1iodX2lOijNu2t8gxetY9%2FddFCwtvoJU8AiAlFpNel86f5jLneyk58%2BShNZ5Ib6l7cXQJ%2FVmatczy9yr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM7LTTArSks%2BBo8tfJKtwDdoG4Su%2BRXxeTgJJoeNits2vwMwVnC2MhvZJ7ATai7ZnMHagFsq8d8vgmbk1KN2WXyxjEKFTLEj6wNiyC0UEQxU1W95iZ2t9CyucaIkquUbRmTEJbwSI4h5ZDmorVMXfe9oai10nsk6qvtgCuj7FzFImeFHrAhd9cFDFn5xQ8dd2o80eBqGk%2BGuIDeRXCRvsm1u6VFIcsFOPKbd8%2FBYKv%2FhQKziUz2ndUmtdwGfil2Ewj9O%2FdvTmS%2FkWAyPKNu6AE16Mt8y23fJpe3JH5pUl3hVZ6BN7J4%2F5vZ2FPlcJYX1WenU6r3LL%2BRvxvxlK3RBJb0BowxAPBIZCPoBVnHhIfIpIvShLFn8bq7T24dxcxq2X0q7POBv8IMJ97WtgyS9Kpy5EYEo1KX9kfTgAwVdXhL9KBZf40GW0fZ1d76iwMqqIC2y1OXhb5WyFNW2PTsLX4sWLCn3kTHEmEIE6wgc%2FIGmqtQgRZcQMji%2F54R3djZFLXU0qn6GzCUveP%2FwP7J8WHWDzTT35dfKjf%2BB6dyfYaJU4rhUi7%2B8DQ%2F8bovahLj8iBdFdkF5b%2F0WzJIJ4J4koIVcUBwKE%2FZ9Aie%2BxvgY7jn7Muh%2Fh8928eE99kKD3abkaVhuhG9JsexbVDzH8w2rqOvQY6pgFj3ZtootrKw9%2F2k6QtmyK9wrm6w3bOZrumF5GmiYBBMXJD%2FSsQPUVJHCeFS0eV9vzPo55VhbRHKmLhGVrAr5XETfQHTRBkdRQwhW02tqchTWry3onrzaaDio46ueOgME15x8pJZilVqInO1%2FynJxrNLARY0H0hS9qzlwzGoEb%2FGzHbpP2cKzfeWmbIYeK7HR6LNTXOFfdQTqINa9GDpVltMIGiS93n&X-Amz-Signature=711a580bbf5698887d6a16ed6f394bcc4285500977566e6e79ecb44e03a54fca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEIUTW4N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCic2Fkt9SvVT%2B61RsTVhZijMXxYRbo7aPfTY0oVcT1VAIhAPQtW7okQurXDqFFCZco9vBS5Ojs4g%2F%2BA%2BEFdq6om2O%2FKv8DCEoQABoMNjM3NDIzMTgzODA1IgzaYOoTJs6bxGGFzdoq3AOxePKvNamD0%2BmGCm4sgDdkMjLFx3sfKz4Nb6xo1CnCBjiKQYU8dbIC4DJZZbn0bamLl%2FoRqBpLkIGTk0ElDYAVvZoVPvILXIQ705XQBow5evTlLO5h%2F%2BFA%2FeyoyszpxBptVBHsuc5vm9Eghq0OHA%2BbzQF63ocaReuNMy1HnN5PCiqWe1NB06UCWm03vF9muBDRsvyDe8O7d96QV7g10fH17gXp0gfRUlL9HXL%2BQXE%2B3l2xTQ6RVU2G2KTRIrHFBT2g5fIAAcx60owBL4WKiQDBHyo9Rys5niAXFBFFcyVMqMCFppBitTdnHbThnAFQuUbpymY7dU4JLfNz6%2BKg%2BEJKx8YxOGh8r6quFe%2FDvONmo%2Fa8lQYPSFBusl9jYZaispRxyo95yUQG4ivxrqKRoVvF9P5cyl3oHKkHHn%2FLOna4uhs03hpHp%2BbWkYZfdMW0ue%2BDebAS%2Fjaj95GoYM8qIqDzJ8rWXHnYB6l5tMnz7MN%2FRxsGKSarfz9mzGQ%2B7ldsd2L5wF5L33cNbTAAETBlTKvsda31%2BnPLqdngASC5bnD9x%2FLioM9RSRw8A9FZl%2FTkFlA3l440Gs3Ye5wt9PcdioaPw7majmMQ%2BlDIzc8R2FDwM0Lyt5ZrlXnLD38WfTDnuo69BjqkAeudhrEhdj88xY4eIGQ0Ejrl00htyAF4%2FA6kuf7p7QCJ5pS6e%2BRM%2B%2B70Jqin0fW5hCUg8IRVppeh2bfnyDZZBWGukfpG6Shy41OVHeMWcupgBzn1Ov0Ze8K1TuE2gLJLlCKHWUEgVe2nOMpaJ3eGB3vEGeV4H24DYOb2qo7s%2BwhpwA18t8hW3jcN%2Bx5%2Fb0r3bbEytfjuO9tzDkWvd7sm%2Fl4RaUSb&X-Amz-Signature=c5cb05d5592ccfd86a29d5d608936560a799f4d1e1def4b1e90e9683025fb69b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEIUTW4N%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQCic2Fkt9SvVT%2B61RsTVhZijMXxYRbo7aPfTY0oVcT1VAIhAPQtW7okQurXDqFFCZco9vBS5Ojs4g%2F%2BA%2BEFdq6om2O%2FKv8DCEoQABoMNjM3NDIzMTgzODA1IgzaYOoTJs6bxGGFzdoq3AOxePKvNamD0%2BmGCm4sgDdkMjLFx3sfKz4Nb6xo1CnCBjiKQYU8dbIC4DJZZbn0bamLl%2FoRqBpLkIGTk0ElDYAVvZoVPvILXIQ705XQBow5evTlLO5h%2F%2BFA%2FeyoyszpxBptVBHsuc5vm9Eghq0OHA%2BbzQF63ocaReuNMy1HnN5PCiqWe1NB06UCWm03vF9muBDRsvyDe8O7d96QV7g10fH17gXp0gfRUlL9HXL%2BQXE%2B3l2xTQ6RVU2G2KTRIrHFBT2g5fIAAcx60owBL4WKiQDBHyo9Rys5niAXFBFFcyVMqMCFppBitTdnHbThnAFQuUbpymY7dU4JLfNz6%2BKg%2BEJKx8YxOGh8r6quFe%2FDvONmo%2Fa8lQYPSFBusl9jYZaispRxyo95yUQG4ivxrqKRoVvF9P5cyl3oHKkHHn%2FLOna4uhs03hpHp%2BbWkYZfdMW0ue%2BDebAS%2Fjaj95GoYM8qIqDzJ8rWXHnYB6l5tMnz7MN%2FRxsGKSarfz9mzGQ%2B7ldsd2L5wF5L33cNbTAAETBlTKvsda31%2BnPLqdngASC5bnD9x%2FLioM9RSRw8A9FZl%2FTkFlA3l440Gs3Ye5wt9PcdioaPw7majmMQ%2BlDIzc8R2FDwM0Lyt5ZrlXnLD38WfTDnuo69BjqkAeudhrEhdj88xY4eIGQ0Ejrl00htyAF4%2FA6kuf7p7QCJ5pS6e%2BRM%2B%2B70Jqin0fW5hCUg8IRVppeh2bfnyDZZBWGukfpG6Shy41OVHeMWcupgBzn1Ov0Ze8K1TuE2gLJLlCKHWUEgVe2nOMpaJ3eGB3vEGeV4H24DYOb2qo7s%2BwhpwA18t8hW3jcN%2Bx5%2Fb0r3bbEytfjuO9tzDkWvd7sm%2Fl4RaUSb&X-Amz-Signature=0ecabafe72a746bb94d382410eb6f946bd6adc9052348e7223edbf3f00423497&X-Amz-SignedHeaders=host&x-id=GetObject)
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
