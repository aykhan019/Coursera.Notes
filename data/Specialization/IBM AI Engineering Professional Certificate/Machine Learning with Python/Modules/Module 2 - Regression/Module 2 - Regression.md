

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMVXKPV6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGp0ckii1G1o%2Bifpzc9eld3erY%2BBYXQNhB1ZKdpzgq8pAiBPv7QfOQMWZscBpCncz4GdXFIAA8oc%2F%2BrcZRtbSN5tqyqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpcNYnotvHlL7WeJ4KtwDf8uYJa6r8oJP9Sr9Rs21yF%2FcW6gVgz2OgpEbqU58cNdjtN01ALfpvXFW2bLHp4ymaDgqd%2BsqtgFpy6%2FjPQDgrKgjmUBQNw%2FWIhDkHIl8p7FTgMa92EeHjPWPrCqzGbxfOkarSzPYNrt175etIUpdatJxdSzy5FEqv3y%2FizbFi0RB5rzOmQlIMsRiOe%2BDEmwe4G3d5tq%2FIdo8dQ37Y5A4mLfxExY5r%2Ft601NqPs5QN4rfDkdgpY%2BRHUJzxidBTIFltUHQ1KujEw%2BuDVcAe40YC7x1Y6gDBlzneOrb2oVEJ69GBvdjTH6PlH7BCOb%2B%2BXzO9RcoH3uOP1dsgX2P1%2BYc%2BpEEpcRd2AXJFCQWiTjjCsgsIMiDN%2B1v6JZREnrlOB5ERydAx5Ml75EbSgao9pLWXF8aumWIeJdQRtLJPDrhde5JLV4R1lRoyI7jXtzod9%2FRv9NvO%2Fn%2FuvQCOp6TTEnYEeryRWte8ctVSIqW2YLtquiA2FWREJayDZ%2FxK0LuenOTkyHWeSJq8YLRHaf26xNZYVh27CZFXgL9xtcrldwU4k4DTTY%2FYhnu3nOx%2FfXZ7wZoHgMcMTNytdqT4M9xSQWseYmT3tubf0bVcKcjIGCa2nqoY4cdABDbwuH8MXYw1uDvvAY6pgFkDnO%2BSvn%2FDP1SCgapSs5wOclW%2BZJX9Uozq2Yk5mSyP0t4IUvX0Zy%2Bd3LPLa34Nf1BNs1W4m44dF8GI52eU0INhi8jzT2%2Fllf242zUzv9XqKNOn0mEnpTSZoL3ZTITfWcK8TikOGof1wfxnxIiMqQqfTebranDeEGVy82zigjsq32%2BnxFUXlGgMK017CQ6Dp9ybCzCdEGHAixXPuaNZlWUD06%2Beo%2FJ&X-Amz-Signature=bb52e43675399f1091404d1014ce6b63d15d0e545c826c37c5111ee2d0416e23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMVXKPV6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGp0ckii1G1o%2Bifpzc9eld3erY%2BBYXQNhB1ZKdpzgq8pAiBPv7QfOQMWZscBpCncz4GdXFIAA8oc%2F%2BrcZRtbSN5tqyqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpcNYnotvHlL7WeJ4KtwDf8uYJa6r8oJP9Sr9Rs21yF%2FcW6gVgz2OgpEbqU58cNdjtN01ALfpvXFW2bLHp4ymaDgqd%2BsqtgFpy6%2FjPQDgrKgjmUBQNw%2FWIhDkHIl8p7FTgMa92EeHjPWPrCqzGbxfOkarSzPYNrt175etIUpdatJxdSzy5FEqv3y%2FizbFi0RB5rzOmQlIMsRiOe%2BDEmwe4G3d5tq%2FIdo8dQ37Y5A4mLfxExY5r%2Ft601NqPs5QN4rfDkdgpY%2BRHUJzxidBTIFltUHQ1KujEw%2BuDVcAe40YC7x1Y6gDBlzneOrb2oVEJ69GBvdjTH6PlH7BCOb%2B%2BXzO9RcoH3uOP1dsgX2P1%2BYc%2BpEEpcRd2AXJFCQWiTjjCsgsIMiDN%2B1v6JZREnrlOB5ERydAx5Ml75EbSgao9pLWXF8aumWIeJdQRtLJPDrhde5JLV4R1lRoyI7jXtzod9%2FRv9NvO%2Fn%2FuvQCOp6TTEnYEeryRWte8ctVSIqW2YLtquiA2FWREJayDZ%2FxK0LuenOTkyHWeSJq8YLRHaf26xNZYVh27CZFXgL9xtcrldwU4k4DTTY%2FYhnu3nOx%2FfXZ7wZoHgMcMTNytdqT4M9xSQWseYmT3tubf0bVcKcjIGCa2nqoY4cdABDbwuH8MXYw1uDvvAY6pgFkDnO%2BSvn%2FDP1SCgapSs5wOclW%2BZJX9Uozq2Yk5mSyP0t4IUvX0Zy%2Bd3LPLa34Nf1BNs1W4m44dF8GI52eU0INhi8jzT2%2Fllf242zUzv9XqKNOn0mEnpTSZoL3ZTITfWcK8TikOGof1wfxnxIiMqQqfTebranDeEGVy82zigjsq32%2BnxFUXlGgMK017CQ6Dp9ybCzCdEGHAixXPuaNZlWUD06%2Beo%2FJ&X-Amz-Signature=74c2eeca50b7994734b95ea306e6ebcc6caedb1075940602f5a5137e8c949e75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMVXKPV6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGp0ckii1G1o%2Bifpzc9eld3erY%2BBYXQNhB1ZKdpzgq8pAiBPv7QfOQMWZscBpCncz4GdXFIAA8oc%2F%2BrcZRtbSN5tqyqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpcNYnotvHlL7WeJ4KtwDf8uYJa6r8oJP9Sr9Rs21yF%2FcW6gVgz2OgpEbqU58cNdjtN01ALfpvXFW2bLHp4ymaDgqd%2BsqtgFpy6%2FjPQDgrKgjmUBQNw%2FWIhDkHIl8p7FTgMa92EeHjPWPrCqzGbxfOkarSzPYNrt175etIUpdatJxdSzy5FEqv3y%2FizbFi0RB5rzOmQlIMsRiOe%2BDEmwe4G3d5tq%2FIdo8dQ37Y5A4mLfxExY5r%2Ft601NqPs5QN4rfDkdgpY%2BRHUJzxidBTIFltUHQ1KujEw%2BuDVcAe40YC7x1Y6gDBlzneOrb2oVEJ69GBvdjTH6PlH7BCOb%2B%2BXzO9RcoH3uOP1dsgX2P1%2BYc%2BpEEpcRd2AXJFCQWiTjjCsgsIMiDN%2B1v6JZREnrlOB5ERydAx5Ml75EbSgao9pLWXF8aumWIeJdQRtLJPDrhde5JLV4R1lRoyI7jXtzod9%2FRv9NvO%2Fn%2FuvQCOp6TTEnYEeryRWte8ctVSIqW2YLtquiA2FWREJayDZ%2FxK0LuenOTkyHWeSJq8YLRHaf26xNZYVh27CZFXgL9xtcrldwU4k4DTTY%2FYhnu3nOx%2FfXZ7wZoHgMcMTNytdqT4M9xSQWseYmT3tubf0bVcKcjIGCa2nqoY4cdABDbwuH8MXYw1uDvvAY6pgFkDnO%2BSvn%2FDP1SCgapSs5wOclW%2BZJX9Uozq2Yk5mSyP0t4IUvX0Zy%2Bd3LPLa34Nf1BNs1W4m44dF8GI52eU0INhi8jzT2%2Fllf242zUzv9XqKNOn0mEnpTSZoL3ZTITfWcK8TikOGof1wfxnxIiMqQqfTebranDeEGVy82zigjsq32%2BnxFUXlGgMK017CQ6Dp9ybCzCdEGHAixXPuaNZlWUD06%2Beo%2FJ&X-Amz-Signature=b4fe0622117f5534ecf613a587349ca62fb979c23d232c159509597447793832&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMVXKPV6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGp0ckii1G1o%2Bifpzc9eld3erY%2BBYXQNhB1ZKdpzgq8pAiBPv7QfOQMWZscBpCncz4GdXFIAA8oc%2F%2BrcZRtbSN5tqyqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpcNYnotvHlL7WeJ4KtwDf8uYJa6r8oJP9Sr9Rs21yF%2FcW6gVgz2OgpEbqU58cNdjtN01ALfpvXFW2bLHp4ymaDgqd%2BsqtgFpy6%2FjPQDgrKgjmUBQNw%2FWIhDkHIl8p7FTgMa92EeHjPWPrCqzGbxfOkarSzPYNrt175etIUpdatJxdSzy5FEqv3y%2FizbFi0RB5rzOmQlIMsRiOe%2BDEmwe4G3d5tq%2FIdo8dQ37Y5A4mLfxExY5r%2Ft601NqPs5QN4rfDkdgpY%2BRHUJzxidBTIFltUHQ1KujEw%2BuDVcAe40YC7x1Y6gDBlzneOrb2oVEJ69GBvdjTH6PlH7BCOb%2B%2BXzO9RcoH3uOP1dsgX2P1%2BYc%2BpEEpcRd2AXJFCQWiTjjCsgsIMiDN%2B1v6JZREnrlOB5ERydAx5Ml75EbSgao9pLWXF8aumWIeJdQRtLJPDrhde5JLV4R1lRoyI7jXtzod9%2FRv9NvO%2Fn%2FuvQCOp6TTEnYEeryRWte8ctVSIqW2YLtquiA2FWREJayDZ%2FxK0LuenOTkyHWeSJq8YLRHaf26xNZYVh27CZFXgL9xtcrldwU4k4DTTY%2FYhnu3nOx%2FfXZ7wZoHgMcMTNytdqT4M9xSQWseYmT3tubf0bVcKcjIGCa2nqoY4cdABDbwuH8MXYw1uDvvAY6pgFkDnO%2BSvn%2FDP1SCgapSs5wOclW%2BZJX9Uozq2Yk5mSyP0t4IUvX0Zy%2Bd3LPLa34Nf1BNs1W4m44dF8GI52eU0INhi8jzT2%2Fllf242zUzv9XqKNOn0mEnpTSZoL3ZTITfWcK8TikOGof1wfxnxIiMqQqfTebranDeEGVy82zigjsq32%2BnxFUXlGgMK017CQ6Dp9ybCzCdEGHAixXPuaNZlWUD06%2Beo%2FJ&X-Amz-Signature=16d17813ca6b289ff4d196482b1bef6c6964a6c2016327cc4b51be4f3c78b856&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMVXKPV6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGp0ckii1G1o%2Bifpzc9eld3erY%2BBYXQNhB1ZKdpzgq8pAiBPv7QfOQMWZscBpCncz4GdXFIAA8oc%2F%2BrcZRtbSN5tqyqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpcNYnotvHlL7WeJ4KtwDf8uYJa6r8oJP9Sr9Rs21yF%2FcW6gVgz2OgpEbqU58cNdjtN01ALfpvXFW2bLHp4ymaDgqd%2BsqtgFpy6%2FjPQDgrKgjmUBQNw%2FWIhDkHIl8p7FTgMa92EeHjPWPrCqzGbxfOkarSzPYNrt175etIUpdatJxdSzy5FEqv3y%2FizbFi0RB5rzOmQlIMsRiOe%2BDEmwe4G3d5tq%2FIdo8dQ37Y5A4mLfxExY5r%2Ft601NqPs5QN4rfDkdgpY%2BRHUJzxidBTIFltUHQ1KujEw%2BuDVcAe40YC7x1Y6gDBlzneOrb2oVEJ69GBvdjTH6PlH7BCOb%2B%2BXzO9RcoH3uOP1dsgX2P1%2BYc%2BpEEpcRd2AXJFCQWiTjjCsgsIMiDN%2B1v6JZREnrlOB5ERydAx5Ml75EbSgao9pLWXF8aumWIeJdQRtLJPDrhde5JLV4R1lRoyI7jXtzod9%2FRv9NvO%2Fn%2FuvQCOp6TTEnYEeryRWte8ctVSIqW2YLtquiA2FWREJayDZ%2FxK0LuenOTkyHWeSJq8YLRHaf26xNZYVh27CZFXgL9xtcrldwU4k4DTTY%2FYhnu3nOx%2FfXZ7wZoHgMcMTNytdqT4M9xSQWseYmT3tubf0bVcKcjIGCa2nqoY4cdABDbwuH8MXYw1uDvvAY6pgFkDnO%2BSvn%2FDP1SCgapSs5wOclW%2BZJX9Uozq2Yk5mSyP0t4IUvX0Zy%2Bd3LPLa34Nf1BNs1W4m44dF8GI52eU0INhi8jzT2%2Fllf242zUzv9XqKNOn0mEnpTSZoL3ZTITfWcK8TikOGof1wfxnxIiMqQqfTebranDeEGVy82zigjsq32%2BnxFUXlGgMK017CQ6Dp9ybCzCdEGHAixXPuaNZlWUD06%2Beo%2FJ&X-Amz-Signature=6e03265a5adba1a0f68362e442b05d724251e4d1d4ec2c319826a6e5e01a69f8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMVXKPV6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGp0ckii1G1o%2Bifpzc9eld3erY%2BBYXQNhB1ZKdpzgq8pAiBPv7QfOQMWZscBpCncz4GdXFIAA8oc%2F%2BrcZRtbSN5tqyqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpcNYnotvHlL7WeJ4KtwDf8uYJa6r8oJP9Sr9Rs21yF%2FcW6gVgz2OgpEbqU58cNdjtN01ALfpvXFW2bLHp4ymaDgqd%2BsqtgFpy6%2FjPQDgrKgjmUBQNw%2FWIhDkHIl8p7FTgMa92EeHjPWPrCqzGbxfOkarSzPYNrt175etIUpdatJxdSzy5FEqv3y%2FizbFi0RB5rzOmQlIMsRiOe%2BDEmwe4G3d5tq%2FIdo8dQ37Y5A4mLfxExY5r%2Ft601NqPs5QN4rfDkdgpY%2BRHUJzxidBTIFltUHQ1KujEw%2BuDVcAe40YC7x1Y6gDBlzneOrb2oVEJ69GBvdjTH6PlH7BCOb%2B%2BXzO9RcoH3uOP1dsgX2P1%2BYc%2BpEEpcRd2AXJFCQWiTjjCsgsIMiDN%2B1v6JZREnrlOB5ERydAx5Ml75EbSgao9pLWXF8aumWIeJdQRtLJPDrhde5JLV4R1lRoyI7jXtzod9%2FRv9NvO%2Fn%2FuvQCOp6TTEnYEeryRWte8ctVSIqW2YLtquiA2FWREJayDZ%2FxK0LuenOTkyHWeSJq8YLRHaf26xNZYVh27CZFXgL9xtcrldwU4k4DTTY%2FYhnu3nOx%2FfXZ7wZoHgMcMTNytdqT4M9xSQWseYmT3tubf0bVcKcjIGCa2nqoY4cdABDbwuH8MXYw1uDvvAY6pgFkDnO%2BSvn%2FDP1SCgapSs5wOclW%2BZJX9Uozq2Yk5mSyP0t4IUvX0Zy%2Bd3LPLa34Nf1BNs1W4m44dF8GI52eU0INhi8jzT2%2Fllf242zUzv9XqKNOn0mEnpTSZoL3ZTITfWcK8TikOGof1wfxnxIiMqQqfTebranDeEGVy82zigjsq32%2BnxFUXlGgMK017CQ6Dp9ybCzCdEGHAixXPuaNZlWUD06%2Beo%2FJ&X-Amz-Signature=253a5db15e9ad12b9e98567a9ae3e258929daed7692ee2c4a5a0dc8425a612a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMVXKPV6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGp0ckii1G1o%2Bifpzc9eld3erY%2BBYXQNhB1ZKdpzgq8pAiBPv7QfOQMWZscBpCncz4GdXFIAA8oc%2F%2BrcZRtbSN5tqyqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpcNYnotvHlL7WeJ4KtwDf8uYJa6r8oJP9Sr9Rs21yF%2FcW6gVgz2OgpEbqU58cNdjtN01ALfpvXFW2bLHp4ymaDgqd%2BsqtgFpy6%2FjPQDgrKgjmUBQNw%2FWIhDkHIl8p7FTgMa92EeHjPWPrCqzGbxfOkarSzPYNrt175etIUpdatJxdSzy5FEqv3y%2FizbFi0RB5rzOmQlIMsRiOe%2BDEmwe4G3d5tq%2FIdo8dQ37Y5A4mLfxExY5r%2Ft601NqPs5QN4rfDkdgpY%2BRHUJzxidBTIFltUHQ1KujEw%2BuDVcAe40YC7x1Y6gDBlzneOrb2oVEJ69GBvdjTH6PlH7BCOb%2B%2BXzO9RcoH3uOP1dsgX2P1%2BYc%2BpEEpcRd2AXJFCQWiTjjCsgsIMiDN%2B1v6JZREnrlOB5ERydAx5Ml75EbSgao9pLWXF8aumWIeJdQRtLJPDrhde5JLV4R1lRoyI7jXtzod9%2FRv9NvO%2Fn%2FuvQCOp6TTEnYEeryRWte8ctVSIqW2YLtquiA2FWREJayDZ%2FxK0LuenOTkyHWeSJq8YLRHaf26xNZYVh27CZFXgL9xtcrldwU4k4DTTY%2FYhnu3nOx%2FfXZ7wZoHgMcMTNytdqT4M9xSQWseYmT3tubf0bVcKcjIGCa2nqoY4cdABDbwuH8MXYw1uDvvAY6pgFkDnO%2BSvn%2FDP1SCgapSs5wOclW%2BZJX9Uozq2Yk5mSyP0t4IUvX0Zy%2Bd3LPLa34Nf1BNs1W4m44dF8GI52eU0INhi8jzT2%2Fllf242zUzv9XqKNOn0mEnpTSZoL3ZTITfWcK8TikOGof1wfxnxIiMqQqfTebranDeEGVy82zigjsq32%2BnxFUXlGgMK017CQ6Dp9ybCzCdEGHAixXPuaNZlWUD06%2Beo%2FJ&X-Amz-Signature=6264475565209f6c545e6a105e73341d442a82185ff9ebf12d8d2e72faf1008f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMVXKPV6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGp0ckii1G1o%2Bifpzc9eld3erY%2BBYXQNhB1ZKdpzgq8pAiBPv7QfOQMWZscBpCncz4GdXFIAA8oc%2F%2BrcZRtbSN5tqyqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpcNYnotvHlL7WeJ4KtwDf8uYJa6r8oJP9Sr9Rs21yF%2FcW6gVgz2OgpEbqU58cNdjtN01ALfpvXFW2bLHp4ymaDgqd%2BsqtgFpy6%2FjPQDgrKgjmUBQNw%2FWIhDkHIl8p7FTgMa92EeHjPWPrCqzGbxfOkarSzPYNrt175etIUpdatJxdSzy5FEqv3y%2FizbFi0RB5rzOmQlIMsRiOe%2BDEmwe4G3d5tq%2FIdo8dQ37Y5A4mLfxExY5r%2Ft601NqPs5QN4rfDkdgpY%2BRHUJzxidBTIFltUHQ1KujEw%2BuDVcAe40YC7x1Y6gDBlzneOrb2oVEJ69GBvdjTH6PlH7BCOb%2B%2BXzO9RcoH3uOP1dsgX2P1%2BYc%2BpEEpcRd2AXJFCQWiTjjCsgsIMiDN%2B1v6JZREnrlOB5ERydAx5Ml75EbSgao9pLWXF8aumWIeJdQRtLJPDrhde5JLV4R1lRoyI7jXtzod9%2FRv9NvO%2Fn%2FuvQCOp6TTEnYEeryRWte8ctVSIqW2YLtquiA2FWREJayDZ%2FxK0LuenOTkyHWeSJq8YLRHaf26xNZYVh27CZFXgL9xtcrldwU4k4DTTY%2FYhnu3nOx%2FfXZ7wZoHgMcMTNytdqT4M9xSQWseYmT3tubf0bVcKcjIGCa2nqoY4cdABDbwuH8MXYw1uDvvAY6pgFkDnO%2BSvn%2FDP1SCgapSs5wOclW%2BZJX9Uozq2Yk5mSyP0t4IUvX0Zy%2Bd3LPLa34Nf1BNs1W4m44dF8GI52eU0INhi8jzT2%2Fllf242zUzv9XqKNOn0mEnpTSZoL3ZTITfWcK8TikOGof1wfxnxIiMqQqfTebranDeEGVy82zigjsq32%2BnxFUXlGgMK017CQ6Dp9ybCzCdEGHAixXPuaNZlWUD06%2Beo%2FJ&X-Amz-Signature=37a4dffc9e4e645259d4442aec747e828bdade33266be7c4021d6a26c16e006f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676VQ4VUA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzk327x5NaKxu6vYJ2aESJgWFLvjtdIVE6fmBZkSs2lgIga6Hrs1jh29oEUFonfgNXSSeYw057%2BEtiLCAxTu9WVaMqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOCvUu2dA%2BVLHPKAXircAx5l5GqOPbc2ptnI2mk1tea4D%2FvsxQfUDTl7MCmddYlPrDaddhoPKp6LTiWEtwbAyPbfBX3pYexPlrffjaITiM7HnwYQz9JuqcC06qrsNhHxqzFUzZ2GwF0gnx94MWcoP4sNNLVHegt4GUORao%2B5Kz4S3YVzUgCKUeO6cRnPsQonxDD3MgThBgS%2BkxZ6hhJ%2BlhvPMBvnZWyLDRF3Dr0ZHN%2FE3YE8qYyWFLzpLtSPctwEZivqD5bl5I4Q4d7X04Q%2B7KhkSkVYyCjFbDgMUDvoLA0FXNlbE8bMpubyOJmhszTiWBKjQYQBj370YhYkSDGVqTxkJUbKqdL71IWwWbWce2pSkmrT2UsEEwmrNJc4XRKYnOgjCqaU%2BdDSk5LRenpJNSjB2W%2FBAOlJkrM5cFARoShxKw%2FcezYeB%2B%2F8%2B93aFxRAWDD4g7hqnN0d9YFEu0zlua02%2B0TOPx0Wb7ZsiPTuP7ngm0xeQseCdqikPKYHyyeNmUxl77rrpQ1hl1OI%2Bi7eGJbVd29D77ubIbk009LXF11TXFozRFDn1nIZ23%2BrmbnWbiuz0r5SXejzOLUns18U9Psq5HMyLwFd4q9tYE5OuU0u%2FPAhyZ3u13%2BEwLHPGrGKd24uBd2cUxOH2lfhMPTg77wGOqUBkA1b%2FoPNNbrbkDfF4LsU8rp%2B1cZTZD2rPXcxLJURt5W6vVTDjQ%2BMySke6E%2FWr04EpmlcZoLZt74h3AHroX1CnwbHVwpn7gD9%2Btp3p%2FgarMzrvYUVhBFPIUxI2mjdVvFW%2B1p3AWdA80%2FPJiIvjJPp8OuJ06OxsX2SryG0yDLEdoknGpj8IqLyz15j5wlA7mr9RJlwmhLHYAFx7uJASrhL43IeSJ3g&X-Amz-Signature=865a5bcb7c2e287158e45641cd8b0f75e4066a386741e790ffeb5c6063844abc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5WNPWR6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID%2BamxLsh3SSZnBR%2F1dQXI0oL%2BhsByVOyi2mtzLRJBz0AiAB2zyqcoAaYE2uGwoiluQP%2Fq1xdMTA39sS4pwvtCEtqCqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG%2FsMYUgGv9W1BjmUKtwDoyVfsxL48Y3onIZSta%2BcjpZOti7MZyFB1RDyuY9EzJoJ36B5DYf0%2F2%2Bey6Ifg6ywA6Equ6ga6HfvHjHzeb36vGQZCJfX6EHlB1QllqnAP9XqMGNanP%2B%2Bae05Pi8HL9b1wRPZVJJB5rd3X%2BacTsPZdAbZJcQYfp4yCOTciICLDa9L2PLiT4OgJwSFU2tEcQJg1%2Fq%2B8yQXqQbQ8FENibc9raQudLfEzdJjtnvU%2FfqMoxzQRTbtkARCanXnkQPghB%2FoHvtnmQPPQKaMSDGz0AfCGWDNsFZeZ8sDM%2FgsMaIt8r1KW8fXhNlDu5uQ9izv6UV3m%2BmgC9X%2FX4y%2F5q3jZrTaJvGo7MgXI7qOAxka%2BdHpv6RCN80TG4dXpR4kvjgEukbMdQT46OqnEVOWcPDUPQgCakatVkI28z%2F74057DQb1NS2ny4AeaBOmDpnI64fa0TepGi4tC92h68vT0KQEePGxSxjEzgniwIYL3FCDXWIF1%2FpYGF3Z40%2FqgO5avy9Y%2B7fIzXpnbR7%2FZVHa1zrhVe8o8th2UkisII0JDfQG5PLNhMVq5pBAWKM1tr7RpWfFc1T0s%2Bc%2Fw1NMVCtPWQbKs9q%2FZ5b59YfhOxTcb%2BEnWDQz9GiruG3qFCKeWhlhjCYwxeHvvAY6pgEY2cYbdO4PMqR32KbS7KQpbSG8EthrRkSRpWp58ek25bC5XU08dss9x7ohFa3UzyrgdZLxOKwMjEvomQUl%2F6u13%2BrAfDR2imsKeTDe5SKOCEXjzYvSs8N0tbSjfO9fpV5gViYwq%2FNpPf8GHbR6bbY8S2kqYCxufo0rGGEE%2BG38aZkHHmh5P0EJf7VHb5Hq%2BzpYDGERGnN7rW%2BUGBlDycS7CBnDNtQB&X-Amz-Signature=428faa931e415b143760d726d5da03833daf14473c7a31a0c03e57f04bc784f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUNKSLME%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDsWlVzQ%2Bvvx%2F2gL9DaBWx5UAyXM3Osm0srgCo%2BKcFp0AiEAlXDauXmKzvR4UzYmU3UcbF%2BU%2B7fusaz4oDgCy%2BSDxAwqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB7uchclYHo2WVCmbSrcAxkJoqkbRye71VOyyIBxhZmgkj6kDUvjcL3bQrWYUxFSOk72HK2Z8jyQpKL7ftasVb9s%2FlMA%2Bv%2F5D7318PpvmU%2BHA%2B3wXJdpHGemdZ%2FkCCuQz%2Fk%2F%2FFy%2BaFv%2FZu19lj%2BMxAbOhxiEHGAxr%2FHjZdT7fs2TwyQ0i6q9Z3JDEm2O1zjM8HEni1BtKGLTnUTKB1jxLsxAk3yBMAmIAeAOPdsgC7YnABSxv9rX%2FZVryRpr0nuA4dTBLvqHnwGLx2a0%2FVm2GO8lh9qSsV6%2FGqp51GwnbOfeewIH0k7WDBGEPY9xgOhS17vBwX5qy3eD9pIBcoz%2BLfFrYF2BAfIbn%2FgABmMZ%2FKQGP3mkWPKh3zg1fO1sPVMxRIC1%2B5pALi7TnjyCWAtOg5zs8lyNzwpV%2BgJWgcVwsKD4d7x%2FqRWebneYzpAt8KhUrutEqfSQa%2B%2By5xSvzR%2BmkWto%2BgPLWS4L2Kqvg58obdp%2FRZU9EkiwnOOr4L8qaRVrWY3WDpGBBgC3q%2B4DLTc7sxh5PIKMzS%2Fhs1QiMozcxeuhx94EdObkkIxgSkk27LsPJv2pAse47K6dZrwOufz6sfdX%2BCQ1mCjbp4EHiZdCp0s62eS7gX8RaoO2RF3xo1vvtmtijoOTwBkOx0YrMJrh77wGOqUB6Kvb6awuV6dtnjf6E3mWoF%2BwB6vRRia9ueqr9lfad%2Ff6eWUh%2Fs8hN96m4j6CoR7xrS1MSkQ4aP9hmsFnjisuh2XtV72pHqaTIH%2F8jwNq1fPZapzmIU%2BSMIX0AnyI%2BKZA4hyIyo%2F%2BP4jWnA5HH%2FeoWuTEDIR74bHWy2QNhXmNIwZIwdbhK5lO3iOzyUjlxPzrhCujsW7Z5cIfWPokRIhluArt%2BIkG&X-Amz-Signature=bbe96efa9195eedd9d5f69ddec9264bd9e98f7929d677f48f53bb7f654bb0ff8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUNKSLME%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDsWlVzQ%2Bvvx%2F2gL9DaBWx5UAyXM3Osm0srgCo%2BKcFp0AiEAlXDauXmKzvR4UzYmU3UcbF%2BU%2B7fusaz4oDgCy%2BSDxAwqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB7uchclYHo2WVCmbSrcAxkJoqkbRye71VOyyIBxhZmgkj6kDUvjcL3bQrWYUxFSOk72HK2Z8jyQpKL7ftasVb9s%2FlMA%2Bv%2F5D7318PpvmU%2BHA%2B3wXJdpHGemdZ%2FkCCuQz%2Fk%2F%2FFy%2BaFv%2FZu19lj%2BMxAbOhxiEHGAxr%2FHjZdT7fs2TwyQ0i6q9Z3JDEm2O1zjM8HEni1BtKGLTnUTKB1jxLsxAk3yBMAmIAeAOPdsgC7YnABSxv9rX%2FZVryRpr0nuA4dTBLvqHnwGLx2a0%2FVm2GO8lh9qSsV6%2FGqp51GwnbOfeewIH0k7WDBGEPY9xgOhS17vBwX5qy3eD9pIBcoz%2BLfFrYF2BAfIbn%2FgABmMZ%2FKQGP3mkWPKh3zg1fO1sPVMxRIC1%2B5pALi7TnjyCWAtOg5zs8lyNzwpV%2BgJWgcVwsKD4d7x%2FqRWebneYzpAt8KhUrutEqfSQa%2B%2By5xSvzR%2BmkWto%2BgPLWS4L2Kqvg58obdp%2FRZU9EkiwnOOr4L8qaRVrWY3WDpGBBgC3q%2B4DLTc7sxh5PIKMzS%2Fhs1QiMozcxeuhx94EdObkkIxgSkk27LsPJv2pAse47K6dZrwOufz6sfdX%2BCQ1mCjbp4EHiZdCp0s62eS7gX8RaoO2RF3xo1vvtmtijoOTwBkOx0YrMJrh77wGOqUB6Kvb6awuV6dtnjf6E3mWoF%2BwB6vRRia9ueqr9lfad%2Ff6eWUh%2Fs8hN96m4j6CoR7xrS1MSkQ4aP9hmsFnjisuh2XtV72pHqaTIH%2F8jwNq1fPZapzmIU%2BSMIX0AnyI%2BKZA4hyIyo%2F%2BP4jWnA5HH%2FeoWuTEDIR74bHWy2QNhXmNIwZIwdbhK5lO3iOzyUjlxPzrhCujsW7Z5cIfWPokRIhluArt%2BIkG&X-Amz-Signature=1b20332432f9e175916d800816eb38950fd42ab09e7d15482fc2a8e81981c3b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
