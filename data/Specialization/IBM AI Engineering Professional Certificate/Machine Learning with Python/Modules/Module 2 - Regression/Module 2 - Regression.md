

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CAD33XV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPwkKhPbBpcHF40TYxoqfBSatBuxDudl4HWSR8huSWaAiEAjEEkTS0G4SHVS32f4zCgf%2FE7LGCdtJzuvebMGvykBvoqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkc8NB%2FxkHDH6FHbCrcA%2F0SQdunCkMsyp53CEkJUmm87wH%2BJmwjXjdC5zn8Ce7OwAHuR0x%2FJ4saDrJQa4oAGl8p%2Fyp7Vd243cZmeYKtpmOfilDCuH7j9YoqZQs%2FsIGDPhMctVd4Q8M70CqI%2BxtpJB%2FkzDlpMYGI2vL6uwCWy1dRpnbAZEl9Jv2bpwOv4MenM6IPG1wJyeojdWMWHnM12VspLLdmAUo5hqejGu%2FlgBTJvTrU%2B%2B4qyJsUhANJWcZWYGbNCKyUo17aLA0udu1Qlv5%2BvJw31p87v61CxdhJvHUlyb42KvJhMWszmIa%2FyHavMEYSKpcOlMyR7XF%2FiMQti1VZ8W3S6ggPSGqz%2FWw5HXHbe5cUcBvR99XFZsH%2Bd29SzdeNY9rk97ZDjzq5MQ6vgogUHmwLoMi7pcsqZ%2BbY%2FRr0i6tTLo0AMk5vhnNrdcXWY%2FbaVGqsdoLNQIwKPbYWdXS04hc1yroLK1gcTkHCPTtVsmrqqOVg4UKbKcDKeAOtB%2BDwF4Y9oNU7NJGEH308W9YV%2FYJqzpjG3kF%2BP5Lc42SizkAG0HLijaBoKEQKxFH%2FOBfDuwdmKSe9QQk5JEq0ZloFZo3eEwOkDnJY1P02gECNRHT%2FRb7eC90d2DjLuB0L66LUX4vRE5hmKCr0MPyn7bwGOqUBOa%2BVdm3jYxAWmXav6R8bBg7XvTgPqjMAbJiBbOQZm5hACsGdUlXuhfeJF5aNng6Io1jB5qx372BNh98cY%2FFEaDjMXylPQHGBWkg%2BJ8b5oFzssQ85ihsw7clhsGkDYxRJtrRUaAO1Os71j12AOc6mehAcn0tMDpDeX%2FRuwUfaXOPXZd3bRcKe3%2BELhtQi%2F7Q%2FuQdFnBnSCb9iec%2ByZox70qmq4Tv6&X-Amz-Signature=e52b712a0d881d13212c94221e79cfb3e0d599e75afad0eee54d90936fe535b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CAD33XV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPwkKhPbBpcHF40TYxoqfBSatBuxDudl4HWSR8huSWaAiEAjEEkTS0G4SHVS32f4zCgf%2FE7LGCdtJzuvebMGvykBvoqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkc8NB%2FxkHDH6FHbCrcA%2F0SQdunCkMsyp53CEkJUmm87wH%2BJmwjXjdC5zn8Ce7OwAHuR0x%2FJ4saDrJQa4oAGl8p%2Fyp7Vd243cZmeYKtpmOfilDCuH7j9YoqZQs%2FsIGDPhMctVd4Q8M70CqI%2BxtpJB%2FkzDlpMYGI2vL6uwCWy1dRpnbAZEl9Jv2bpwOv4MenM6IPG1wJyeojdWMWHnM12VspLLdmAUo5hqejGu%2FlgBTJvTrU%2B%2B4qyJsUhANJWcZWYGbNCKyUo17aLA0udu1Qlv5%2BvJw31p87v61CxdhJvHUlyb42KvJhMWszmIa%2FyHavMEYSKpcOlMyR7XF%2FiMQti1VZ8W3S6ggPSGqz%2FWw5HXHbe5cUcBvR99XFZsH%2Bd29SzdeNY9rk97ZDjzq5MQ6vgogUHmwLoMi7pcsqZ%2BbY%2FRr0i6tTLo0AMk5vhnNrdcXWY%2FbaVGqsdoLNQIwKPbYWdXS04hc1yroLK1gcTkHCPTtVsmrqqOVg4UKbKcDKeAOtB%2BDwF4Y9oNU7NJGEH308W9YV%2FYJqzpjG3kF%2BP5Lc42SizkAG0HLijaBoKEQKxFH%2FOBfDuwdmKSe9QQk5JEq0ZloFZo3eEwOkDnJY1P02gECNRHT%2FRb7eC90d2DjLuB0L66LUX4vRE5hmKCr0MPyn7bwGOqUBOa%2BVdm3jYxAWmXav6R8bBg7XvTgPqjMAbJiBbOQZm5hACsGdUlXuhfeJF5aNng6Io1jB5qx372BNh98cY%2FFEaDjMXylPQHGBWkg%2BJ8b5oFzssQ85ihsw7clhsGkDYxRJtrRUaAO1Os71j12AOc6mehAcn0tMDpDeX%2FRuwUfaXOPXZd3bRcKe3%2BELhtQi%2F7Q%2FuQdFnBnSCb9iec%2ByZox70qmq4Tv6&X-Amz-Signature=9a513dafd405cd4aa85d1f48bb009bee81dc822fcecebfb4002e3b2414fdebbc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CAD33XV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPwkKhPbBpcHF40TYxoqfBSatBuxDudl4HWSR8huSWaAiEAjEEkTS0G4SHVS32f4zCgf%2FE7LGCdtJzuvebMGvykBvoqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkc8NB%2FxkHDH6FHbCrcA%2F0SQdunCkMsyp53CEkJUmm87wH%2BJmwjXjdC5zn8Ce7OwAHuR0x%2FJ4saDrJQa4oAGl8p%2Fyp7Vd243cZmeYKtpmOfilDCuH7j9YoqZQs%2FsIGDPhMctVd4Q8M70CqI%2BxtpJB%2FkzDlpMYGI2vL6uwCWy1dRpnbAZEl9Jv2bpwOv4MenM6IPG1wJyeojdWMWHnM12VspLLdmAUo5hqejGu%2FlgBTJvTrU%2B%2B4qyJsUhANJWcZWYGbNCKyUo17aLA0udu1Qlv5%2BvJw31p87v61CxdhJvHUlyb42KvJhMWszmIa%2FyHavMEYSKpcOlMyR7XF%2FiMQti1VZ8W3S6ggPSGqz%2FWw5HXHbe5cUcBvR99XFZsH%2Bd29SzdeNY9rk97ZDjzq5MQ6vgogUHmwLoMi7pcsqZ%2BbY%2FRr0i6tTLo0AMk5vhnNrdcXWY%2FbaVGqsdoLNQIwKPbYWdXS04hc1yroLK1gcTkHCPTtVsmrqqOVg4UKbKcDKeAOtB%2BDwF4Y9oNU7NJGEH308W9YV%2FYJqzpjG3kF%2BP5Lc42SizkAG0HLijaBoKEQKxFH%2FOBfDuwdmKSe9QQk5JEq0ZloFZo3eEwOkDnJY1P02gECNRHT%2FRb7eC90d2DjLuB0L66LUX4vRE5hmKCr0MPyn7bwGOqUBOa%2BVdm3jYxAWmXav6R8bBg7XvTgPqjMAbJiBbOQZm5hACsGdUlXuhfeJF5aNng6Io1jB5qx372BNh98cY%2FFEaDjMXylPQHGBWkg%2BJ8b5oFzssQ85ihsw7clhsGkDYxRJtrRUaAO1Os71j12AOc6mehAcn0tMDpDeX%2FRuwUfaXOPXZd3bRcKe3%2BELhtQi%2F7Q%2FuQdFnBnSCb9iec%2ByZox70qmq4Tv6&X-Amz-Signature=0c39acc8e0445d4f93cc05bf360dce8f4c46fad5afacab7c6f2a9fa76f1696bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CAD33XV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPwkKhPbBpcHF40TYxoqfBSatBuxDudl4HWSR8huSWaAiEAjEEkTS0G4SHVS32f4zCgf%2FE7LGCdtJzuvebMGvykBvoqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkc8NB%2FxkHDH6FHbCrcA%2F0SQdunCkMsyp53CEkJUmm87wH%2BJmwjXjdC5zn8Ce7OwAHuR0x%2FJ4saDrJQa4oAGl8p%2Fyp7Vd243cZmeYKtpmOfilDCuH7j9YoqZQs%2FsIGDPhMctVd4Q8M70CqI%2BxtpJB%2FkzDlpMYGI2vL6uwCWy1dRpnbAZEl9Jv2bpwOv4MenM6IPG1wJyeojdWMWHnM12VspLLdmAUo5hqejGu%2FlgBTJvTrU%2B%2B4qyJsUhANJWcZWYGbNCKyUo17aLA0udu1Qlv5%2BvJw31p87v61CxdhJvHUlyb42KvJhMWszmIa%2FyHavMEYSKpcOlMyR7XF%2FiMQti1VZ8W3S6ggPSGqz%2FWw5HXHbe5cUcBvR99XFZsH%2Bd29SzdeNY9rk97ZDjzq5MQ6vgogUHmwLoMi7pcsqZ%2BbY%2FRr0i6tTLo0AMk5vhnNrdcXWY%2FbaVGqsdoLNQIwKPbYWdXS04hc1yroLK1gcTkHCPTtVsmrqqOVg4UKbKcDKeAOtB%2BDwF4Y9oNU7NJGEH308W9YV%2FYJqzpjG3kF%2BP5Lc42SizkAG0HLijaBoKEQKxFH%2FOBfDuwdmKSe9QQk5JEq0ZloFZo3eEwOkDnJY1P02gECNRHT%2FRb7eC90d2DjLuB0L66LUX4vRE5hmKCr0MPyn7bwGOqUBOa%2BVdm3jYxAWmXav6R8bBg7XvTgPqjMAbJiBbOQZm5hACsGdUlXuhfeJF5aNng6Io1jB5qx372BNh98cY%2FFEaDjMXylPQHGBWkg%2BJ8b5oFzssQ85ihsw7clhsGkDYxRJtrRUaAO1Os71j12AOc6mehAcn0tMDpDeX%2FRuwUfaXOPXZd3bRcKe3%2BELhtQi%2F7Q%2FuQdFnBnSCb9iec%2ByZox70qmq4Tv6&X-Amz-Signature=9b99bd79f3657306c51e1d1b707999615794ae2345c4e5f818754c464edee889&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CAD33XV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPwkKhPbBpcHF40TYxoqfBSatBuxDudl4HWSR8huSWaAiEAjEEkTS0G4SHVS32f4zCgf%2FE7LGCdtJzuvebMGvykBvoqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkc8NB%2FxkHDH6FHbCrcA%2F0SQdunCkMsyp53CEkJUmm87wH%2BJmwjXjdC5zn8Ce7OwAHuR0x%2FJ4saDrJQa4oAGl8p%2Fyp7Vd243cZmeYKtpmOfilDCuH7j9YoqZQs%2FsIGDPhMctVd4Q8M70CqI%2BxtpJB%2FkzDlpMYGI2vL6uwCWy1dRpnbAZEl9Jv2bpwOv4MenM6IPG1wJyeojdWMWHnM12VspLLdmAUo5hqejGu%2FlgBTJvTrU%2B%2B4qyJsUhANJWcZWYGbNCKyUo17aLA0udu1Qlv5%2BvJw31p87v61CxdhJvHUlyb42KvJhMWszmIa%2FyHavMEYSKpcOlMyR7XF%2FiMQti1VZ8W3S6ggPSGqz%2FWw5HXHbe5cUcBvR99XFZsH%2Bd29SzdeNY9rk97ZDjzq5MQ6vgogUHmwLoMi7pcsqZ%2BbY%2FRr0i6tTLo0AMk5vhnNrdcXWY%2FbaVGqsdoLNQIwKPbYWdXS04hc1yroLK1gcTkHCPTtVsmrqqOVg4UKbKcDKeAOtB%2BDwF4Y9oNU7NJGEH308W9YV%2FYJqzpjG3kF%2BP5Lc42SizkAG0HLijaBoKEQKxFH%2FOBfDuwdmKSe9QQk5JEq0ZloFZo3eEwOkDnJY1P02gECNRHT%2FRb7eC90d2DjLuB0L66LUX4vRE5hmKCr0MPyn7bwGOqUBOa%2BVdm3jYxAWmXav6R8bBg7XvTgPqjMAbJiBbOQZm5hACsGdUlXuhfeJF5aNng6Io1jB5qx372BNh98cY%2FFEaDjMXylPQHGBWkg%2BJ8b5oFzssQ85ihsw7clhsGkDYxRJtrRUaAO1Os71j12AOc6mehAcn0tMDpDeX%2FRuwUfaXOPXZd3bRcKe3%2BELhtQi%2F7Q%2FuQdFnBnSCb9iec%2ByZox70qmq4Tv6&X-Amz-Signature=25bf75ccb793394c0334e19b598a9b2bf1b49e9bdc00e7b85e7e9772ead64c9a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CAD33XV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPwkKhPbBpcHF40TYxoqfBSatBuxDudl4HWSR8huSWaAiEAjEEkTS0G4SHVS32f4zCgf%2FE7LGCdtJzuvebMGvykBvoqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkc8NB%2FxkHDH6FHbCrcA%2F0SQdunCkMsyp53CEkJUmm87wH%2BJmwjXjdC5zn8Ce7OwAHuR0x%2FJ4saDrJQa4oAGl8p%2Fyp7Vd243cZmeYKtpmOfilDCuH7j9YoqZQs%2FsIGDPhMctVd4Q8M70CqI%2BxtpJB%2FkzDlpMYGI2vL6uwCWy1dRpnbAZEl9Jv2bpwOv4MenM6IPG1wJyeojdWMWHnM12VspLLdmAUo5hqejGu%2FlgBTJvTrU%2B%2B4qyJsUhANJWcZWYGbNCKyUo17aLA0udu1Qlv5%2BvJw31p87v61CxdhJvHUlyb42KvJhMWszmIa%2FyHavMEYSKpcOlMyR7XF%2FiMQti1VZ8W3S6ggPSGqz%2FWw5HXHbe5cUcBvR99XFZsH%2Bd29SzdeNY9rk97ZDjzq5MQ6vgogUHmwLoMi7pcsqZ%2BbY%2FRr0i6tTLo0AMk5vhnNrdcXWY%2FbaVGqsdoLNQIwKPbYWdXS04hc1yroLK1gcTkHCPTtVsmrqqOVg4UKbKcDKeAOtB%2BDwF4Y9oNU7NJGEH308W9YV%2FYJqzpjG3kF%2BP5Lc42SizkAG0HLijaBoKEQKxFH%2FOBfDuwdmKSe9QQk5JEq0ZloFZo3eEwOkDnJY1P02gECNRHT%2FRb7eC90d2DjLuB0L66LUX4vRE5hmKCr0MPyn7bwGOqUBOa%2BVdm3jYxAWmXav6R8bBg7XvTgPqjMAbJiBbOQZm5hACsGdUlXuhfeJF5aNng6Io1jB5qx372BNh98cY%2FFEaDjMXylPQHGBWkg%2BJ8b5oFzssQ85ihsw7clhsGkDYxRJtrRUaAO1Os71j12AOc6mehAcn0tMDpDeX%2FRuwUfaXOPXZd3bRcKe3%2BELhtQi%2F7Q%2FuQdFnBnSCb9iec%2ByZox70qmq4Tv6&X-Amz-Signature=87a4afcee24add6700f456d27c22716c49d5aa30f571fcf387e57791f9749c6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CAD33XV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPwkKhPbBpcHF40TYxoqfBSatBuxDudl4HWSR8huSWaAiEAjEEkTS0G4SHVS32f4zCgf%2FE7LGCdtJzuvebMGvykBvoqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkc8NB%2FxkHDH6FHbCrcA%2F0SQdunCkMsyp53CEkJUmm87wH%2BJmwjXjdC5zn8Ce7OwAHuR0x%2FJ4saDrJQa4oAGl8p%2Fyp7Vd243cZmeYKtpmOfilDCuH7j9YoqZQs%2FsIGDPhMctVd4Q8M70CqI%2BxtpJB%2FkzDlpMYGI2vL6uwCWy1dRpnbAZEl9Jv2bpwOv4MenM6IPG1wJyeojdWMWHnM12VspLLdmAUo5hqejGu%2FlgBTJvTrU%2B%2B4qyJsUhANJWcZWYGbNCKyUo17aLA0udu1Qlv5%2BvJw31p87v61CxdhJvHUlyb42KvJhMWszmIa%2FyHavMEYSKpcOlMyR7XF%2FiMQti1VZ8W3S6ggPSGqz%2FWw5HXHbe5cUcBvR99XFZsH%2Bd29SzdeNY9rk97ZDjzq5MQ6vgogUHmwLoMi7pcsqZ%2BbY%2FRr0i6tTLo0AMk5vhnNrdcXWY%2FbaVGqsdoLNQIwKPbYWdXS04hc1yroLK1gcTkHCPTtVsmrqqOVg4UKbKcDKeAOtB%2BDwF4Y9oNU7NJGEH308W9YV%2FYJqzpjG3kF%2BP5Lc42SizkAG0HLijaBoKEQKxFH%2FOBfDuwdmKSe9QQk5JEq0ZloFZo3eEwOkDnJY1P02gECNRHT%2FRb7eC90d2DjLuB0L66LUX4vRE5hmKCr0MPyn7bwGOqUBOa%2BVdm3jYxAWmXav6R8bBg7XvTgPqjMAbJiBbOQZm5hACsGdUlXuhfeJF5aNng6Io1jB5qx372BNh98cY%2FFEaDjMXylPQHGBWkg%2BJ8b5oFzssQ85ihsw7clhsGkDYxRJtrRUaAO1Os71j12AOc6mehAcn0tMDpDeX%2FRuwUfaXOPXZd3bRcKe3%2BELhtQi%2F7Q%2FuQdFnBnSCb9iec%2ByZox70qmq4Tv6&X-Amz-Signature=0c917917c11716b90f5ebccea0f8230c1323fbf442ce60e6181eb39a3704a296&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CAD33XV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPwkKhPbBpcHF40TYxoqfBSatBuxDudl4HWSR8huSWaAiEAjEEkTS0G4SHVS32f4zCgf%2FE7LGCdtJzuvebMGvykBvoqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPkc8NB%2FxkHDH6FHbCrcA%2F0SQdunCkMsyp53CEkJUmm87wH%2BJmwjXjdC5zn8Ce7OwAHuR0x%2FJ4saDrJQa4oAGl8p%2Fyp7Vd243cZmeYKtpmOfilDCuH7j9YoqZQs%2FsIGDPhMctVd4Q8M70CqI%2BxtpJB%2FkzDlpMYGI2vL6uwCWy1dRpnbAZEl9Jv2bpwOv4MenM6IPG1wJyeojdWMWHnM12VspLLdmAUo5hqejGu%2FlgBTJvTrU%2B%2B4qyJsUhANJWcZWYGbNCKyUo17aLA0udu1Qlv5%2BvJw31p87v61CxdhJvHUlyb42KvJhMWszmIa%2FyHavMEYSKpcOlMyR7XF%2FiMQti1VZ8W3S6ggPSGqz%2FWw5HXHbe5cUcBvR99XFZsH%2Bd29SzdeNY9rk97ZDjzq5MQ6vgogUHmwLoMi7pcsqZ%2BbY%2FRr0i6tTLo0AMk5vhnNrdcXWY%2FbaVGqsdoLNQIwKPbYWdXS04hc1yroLK1gcTkHCPTtVsmrqqOVg4UKbKcDKeAOtB%2BDwF4Y9oNU7NJGEH308W9YV%2FYJqzpjG3kF%2BP5Lc42SizkAG0HLijaBoKEQKxFH%2FOBfDuwdmKSe9QQk5JEq0ZloFZo3eEwOkDnJY1P02gECNRHT%2FRb7eC90d2DjLuB0L66LUX4vRE5hmKCr0MPyn7bwGOqUBOa%2BVdm3jYxAWmXav6R8bBg7XvTgPqjMAbJiBbOQZm5hACsGdUlXuhfeJF5aNng6Io1jB5qx372BNh98cY%2FFEaDjMXylPQHGBWkg%2BJ8b5oFzssQ85ihsw7clhsGkDYxRJtrRUaAO1Os71j12AOc6mehAcn0tMDpDeX%2FRuwUfaXOPXZd3bRcKe3%2BELhtQi%2F7Q%2FuQdFnBnSCb9iec%2ByZox70qmq4Tv6&X-Amz-Signature=83b438d038666fc26d4f2eff94018db64b68a73da89c06d6b71be61d207731f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCCRPJSD%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBXDkIyZMahOq7IIL8D67SPvPmuRmGtuqazyRpn7bJZKAiBDtnNnT0VxmaZtoxN25LU3VPXC3y9qG%2BmxJgmuWLRTaCqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuD2SPIyjdIS7CVsLKtwDa1%2BaahNS3IUEFhvJ81ChkItvpy8RJpZzAgTF9MycaG1d6iz3JX0jkcYYakgTGGcN8biCDnxk8ZeHfRIHOkoIN4Z99gRJ8F05%2B9VpSA5hPaQxfyeGTlTqoubjK01tAk8eQG99BlGN%2B2TCcvMSJ66Ydq1zntVzl76F%2FRBXLnLGS7Kb0Cr%2FUppA8n5nVNXT%2BWKYeSpWrpAU%2F8YL%2F44r71xA0r%2F2ZM%2BnKtBKouK%2FUYszVKRel6MN3aCiXXPA9aaTyJrOlSNRKfQSu6oyt2v9Dqd7I2gP8cr3%2Fmzdf49r28fB4x1hYxQVX918E6FcgoEjiOicTfDcPd4QyymC99RnD%2Fzg3Yk61OBUWL4HLVDMAi%2FU%2Br3%2FYL%2FNKvA1%2FiH8YrEi%2BBun5kVsCMnvPHpkOC7E1ZCSEy5nE%2FMDqMnQuv%2BvmJeMH7Dy6C2m6OzxNe5OnEYQ88ezmAcIaOGwqz3vjGFpdX3ly47iltEvIoN6coeWJdo%2BBlwgCBFutzXMYPmbgRBQdHQyd1t4BeoLoKYX39VrBiRWbRXMITuIN1xNS7EEkAt963DjuUj7957XC3GjTL9mWRwHJ336fjF%2Fi0iQtMGnq796sZThPceLvFEzulzPtpSYJP3%2F4J8RCBJ0jYIz4Dswu6jtvAY6pgG1q8QhNMhG%2FHAa%2BUnY0l8qLWcMcP4Vqf8oBCpVuoS8cddimP6QlXCPNIjat6kr83WMD0Z2WFb%2BsoQDhRGEa%2F642Cyx5%2FW40I2Is8FmEX3eIvy%2B5jzX%2F3wLZFBvIQdxE4po4G3GLzbO2zmTEA8AFBX8%2FfHzmQmSf8bnirDDJxqdAzyNyMp%2BMEk1a0%2Ff4YjAMSZ%2Bl4EbKSvOWX8etyEhlWm%2FgcSMJQJu&X-Amz-Signature=e01b82955162146aa5140bb11eb8d424aa825885b9ff179953d99b29caeb228b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664OJ3JES%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3MWJRtKZUvTtZnhAd7ECKiPxRG26eU43SrB9Xolyd1wIhAPNHi6h2QmaIZKzxD2KluqUhsJNbkum2M9qVnm7UJBr6KogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4i60%2B%2FYvO1P0ixzcq3AMysQSFz3GImF0OnDTAiq9LmlIL9fudoII7jRuY6vfXEOwAxmIEBgzTc24OY5265R4jhHdPCF%2BpGfPczWQHr8ayBqLCm37FWp5Y5WjeLJHH2m0XzyLHD2Z00iucW203kIeB4ptlmVudVzk6JEBKJSwtyoP%2Ba8Uak%2FNPdgC7N51usz64wTnPictRm2emuiKlK5AyOe8Ev5Actf1KlvviOu2A0pgWVo2Ai00VRFUkPc%2BnK%2FgJfIByTf4I4IbLq48Sc3kFswChT%2B8Wdld81NahGqjCVgQIEMyl45HrNQTLg%2Bd1qKBs2sBnDGBDJ7539E45EIQfgS64YKoWsx%2BzihNKsTSQ92d5pZfvHS47bVKFgzC3%2BBEV6vrtxCf3AhymDfTPqu2c%2FokoSrFnhAXAGbpBaxNhSaQ4owxQ5%2BhMhuZncsccVn%2Bq4s8pr51RwnSW%2BEgb5rXg%2Br2HadzwBZMppD0kedAFmlfFtCsO3XbaPTbwjXuTddBbkpPVfo3cQonWZ91lR5JQYKnJoLWkIFYcOSOBzbudLCrLB26X9WILKOl8YdCkz7a2I62uSutgEBZBNh6Vw%2Bg%2FicVhzf4bnddHjzWEEEWropIFjNHR7ad1GPmbP%2FEzyVnyOTnoXoib0%2BL6gDCDqO28BjqkAWdP3NxjhtQ5A%2FPzh%2FxS958Infoox22%2FTP1L1MKKopsmk9N5XZqSxXlAebCKt%2Fw14lQZGdIq1CAD6oK4ayx4aQ9X8HTndxreGCmJ6vWI8SLny2Szu6mBTdTva5HkVCDLBB33MP2c30YoZJotTzhWjJ9Y%2BXpf6RgPoT6ZAWtykQBk14ttc%2BEwpQUHroNLBY1KpWaYlOAf44%2B%2BrbJHlVGHIJ3K7Y3K&X-Amz-Signature=4234d812f9a205bd3252cba8bf41766ab169bc60ce35ac1b3b6855ff45f44c7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TW5E7F3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEddBxRFa3zqM4Rqe5tK8kzrnMuLP9CYl71OYY6eKkJeAiEA118odFtKJ1vOnEP28RbYzxWt8UkVxshSkIJ0xEENewgqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlP0s69NiGlBZQoBircA9uP5WIp0ZPSO9FgwRMQrZKE%2B%2BLaQeIZ0v%2BVv3e4zTpK8xmf4MsrjvU8zMiG%2BqfGWOM5Bs%2BLgBpnWOsoYbEyoMUGLkw1VyDrCsE0B9zQ5lTeCFh6%2BgOn8HkgZbluS1u7MwfOnt7cWOEOGo818uvSg%2FhW%2F3bSTH6vxRwI%2FoCziegA%2BPKbAZ3kC2gxZhVaY7LiOmHcIXtCUJeqH3FIV7hdN%2F4AFJNwqYJT3bqZ870O5Nk1ih6U0XnoA1a3GVBgwYL1WH6IfExpf%2BmCSrHZ8a7bP7OAX2EAFta0CaskhtaxdQXbOtzirFXvJDz75o6MKxOGI6RepTPAW3IRW64oiVIyFNXlZvXtN0kRDNiKNtejmFIHAMkwQK%2F7lYYCamVwHaIGX88z%2BD6GtPRzv1xauU7ZnTxsWk5kpx9m8ywwEPnZSiHRPrEEeMGzp3oaHHw0loorZ7rLqsmcDUey%2BgON56xWjRbx1W6nnKcr7l%2FxygZt8%2F9rGnWgRiSHUnyKPM9lgbqp4i7f6XroZHRfQp4AuPGcr3OT5FtgTdseJjG5RPDcn%2FEFzg9o%2F4STqIlFeKQ7pc37XSap0cOFmGzTevIsSxB6PP8dD8ObBu8j9SPDgkUR%2BWbn7pU%2FQJLfSzQFjnYoMN2o7bwGOqUBj6aNIZ1B6ay4ApvZhI%2B608aKZzWMjHyclkgCgwEzkpOJp8PQT%2BHfsoo3bPX3VuIl3X9BZjUWDqO3ZrWpuui4QTYS3Mz0PIqfnWsssfaoK%2BOeh7HnJ7Y9hGGJFC6u9emJBSbIv8hD48Owz7jQ8VC4JKIpPsUzuTJCocIPyKsJ5nKgJHXJgjgaiZafetmAEzGmZYrAEFRiXHu2B7P7U7mLjMAE1QGl&X-Amz-Signature=fcc16185dc6c9c4df35b0e695c16a65a95f38f5212925988595805c73d65da71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TW5E7F3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEddBxRFa3zqM4Rqe5tK8kzrnMuLP9CYl71OYY6eKkJeAiEA118odFtKJ1vOnEP28RbYzxWt8UkVxshSkIJ0xEENewgqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlP0s69NiGlBZQoBircA9uP5WIp0ZPSO9FgwRMQrZKE%2B%2BLaQeIZ0v%2BVv3e4zTpK8xmf4MsrjvU8zMiG%2BqfGWOM5Bs%2BLgBpnWOsoYbEyoMUGLkw1VyDrCsE0B9zQ5lTeCFh6%2BgOn8HkgZbluS1u7MwfOnt7cWOEOGo818uvSg%2FhW%2F3bSTH6vxRwI%2FoCziegA%2BPKbAZ3kC2gxZhVaY7LiOmHcIXtCUJeqH3FIV7hdN%2F4AFJNwqYJT3bqZ870O5Nk1ih6U0XnoA1a3GVBgwYL1WH6IfExpf%2BmCSrHZ8a7bP7OAX2EAFta0CaskhtaxdQXbOtzirFXvJDz75o6MKxOGI6RepTPAW3IRW64oiVIyFNXlZvXtN0kRDNiKNtejmFIHAMkwQK%2F7lYYCamVwHaIGX88z%2BD6GtPRzv1xauU7ZnTxsWk5kpx9m8ywwEPnZSiHRPrEEeMGzp3oaHHw0loorZ7rLqsmcDUey%2BgON56xWjRbx1W6nnKcr7l%2FxygZt8%2F9rGnWgRiSHUnyKPM9lgbqp4i7f6XroZHRfQp4AuPGcr3OT5FtgTdseJjG5RPDcn%2FEFzg9o%2F4STqIlFeKQ7pc37XSap0cOFmGzTevIsSxB6PP8dD8ObBu8j9SPDgkUR%2BWbn7pU%2FQJLfSzQFjnYoMN2o7bwGOqUBj6aNIZ1B6ay4ApvZhI%2B608aKZzWMjHyclkgCgwEzkpOJp8PQT%2BHfsoo3bPX3VuIl3X9BZjUWDqO3ZrWpuui4QTYS3Mz0PIqfnWsssfaoK%2BOeh7HnJ7Y9hGGJFC6u9emJBSbIv8hD48Owz7jQ8VC4JKIpPsUzuTJCocIPyKsJ5nKgJHXJgjgaiZafetmAEzGmZYrAEFRiXHu2B7P7U7mLjMAE1QGl&X-Amz-Signature=2bf14ff5ce6fe411ef0445b6823fa03b54fa6b4665c42473e33dbe80fda16fdf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
