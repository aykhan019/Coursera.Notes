

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQ5SOG2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEg97X%2FjheQ6UiLVCdvLhi3jNKM5mWVCCHgRPH1Ve8VDAiB9EOkiscgxyUDTcKzNkmbz4hdjmXTq73tVlbnq5EDimiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI1EafNkzWf5HTCLVKtwDJD9glCTg8KuSFXetsDuNtVrSj7im28z9C%2ByK5mDesYHGjy5bgMBXc4tqVHxe4ZuSNXRLGqLtyT%2FCG6NkwoqOl59TN%2FDHR9Q%2BAo1ecUv4SeOPVKMngCZiboSgj%2BteeNZWlcyOsOPLd1JAhw16gkgK2STbZ57oogVYRD2b6uS50IpBZgKARCVWz%2FC%2FoXQpcVMhjmsXPrPOIHWt6QpQluIUDE4n7DuHWwSxZYJHu1hof%2BlPYhzpehbGWnEtPpJei7mdmwSrP%2BVpkPvmDuIPT2O7r7sxgINNHh8Jmir5bEM8uAD%2BbG3CoFN2miPM8yFWvXMiTKJAAlZFZxyHNW8SK8coRokiWTtJAdANn1R%2B1CA8oxH8xTacDDedDdRHEsZgtfjZYbdgLNBcbYiZRG7n5XsZtBcMpbOnW37G%2B92YA4uMidGGBnvMBukvG9B47K%2FNdxlCtNVb9%2BcD7YXoArf5LRZA%2Fz67OgwHQDmO6wAEP6U%2B1DudRKn9dBxcLqIJxFcoACMtVaMx8u49T1czTVJp5fVIbvvnLdb0uMGsRQleYD1X3D%2Fpcgs2V1Ci5AUMKC3NNXcIvZFMiHgDiidV%2BzPbxgh%2BgGL1Y7hF%2Fw4rQOK8fwhzpvRcE5LuMzR5tlP1wk8wqLH6vAY6pgHhwD8fdKHVW9erguf9bLROxEy24y%2BxGSOiQ0DNrFEIwAb8sW1NMjnuqLH%2F4zqQOeO8sqT95IaEtvD5qeMExnXOknpQEk0%2Bi7k9PKyv00ViEN3Y%2Btc3c1ezxX0lEw6BsJ7sjfK3n%2FVT2Wb6aCLIJsOXfZdMdru9BcK0AfN%2B49F%2Fr2aPLjZonPDaXcHmnsXGx8IdS%2FkEXqwKtICyWONa2WfpNmpEwDC2&X-Amz-Signature=a97e1013be93e02c2c7fa6065ac450ba2540bb02e5659ce253cffcc4a060f17d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQ5SOG2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEg97X%2FjheQ6UiLVCdvLhi3jNKM5mWVCCHgRPH1Ve8VDAiB9EOkiscgxyUDTcKzNkmbz4hdjmXTq73tVlbnq5EDimiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI1EafNkzWf5HTCLVKtwDJD9glCTg8KuSFXetsDuNtVrSj7im28z9C%2ByK5mDesYHGjy5bgMBXc4tqVHxe4ZuSNXRLGqLtyT%2FCG6NkwoqOl59TN%2FDHR9Q%2BAo1ecUv4SeOPVKMngCZiboSgj%2BteeNZWlcyOsOPLd1JAhw16gkgK2STbZ57oogVYRD2b6uS50IpBZgKARCVWz%2FC%2FoXQpcVMhjmsXPrPOIHWt6QpQluIUDE4n7DuHWwSxZYJHu1hof%2BlPYhzpehbGWnEtPpJei7mdmwSrP%2BVpkPvmDuIPT2O7r7sxgINNHh8Jmir5bEM8uAD%2BbG3CoFN2miPM8yFWvXMiTKJAAlZFZxyHNW8SK8coRokiWTtJAdANn1R%2B1CA8oxH8xTacDDedDdRHEsZgtfjZYbdgLNBcbYiZRG7n5XsZtBcMpbOnW37G%2B92YA4uMidGGBnvMBukvG9B47K%2FNdxlCtNVb9%2BcD7YXoArf5LRZA%2Fz67OgwHQDmO6wAEP6U%2B1DudRKn9dBxcLqIJxFcoACMtVaMx8u49T1czTVJp5fVIbvvnLdb0uMGsRQleYD1X3D%2Fpcgs2V1Ci5AUMKC3NNXcIvZFMiHgDiidV%2BzPbxgh%2BgGL1Y7hF%2Fw4rQOK8fwhzpvRcE5LuMzR5tlP1wk8wqLH6vAY6pgHhwD8fdKHVW9erguf9bLROxEy24y%2BxGSOiQ0DNrFEIwAb8sW1NMjnuqLH%2F4zqQOeO8sqT95IaEtvD5qeMExnXOknpQEk0%2Bi7k9PKyv00ViEN3Y%2Btc3c1ezxX0lEw6BsJ7sjfK3n%2FVT2Wb6aCLIJsOXfZdMdru9BcK0AfN%2B49F%2Fr2aPLjZonPDaXcHmnsXGx8IdS%2FkEXqwKtICyWONa2WfpNmpEwDC2&X-Amz-Signature=37050ad6fabb3c9f2704e65b67d2d2376eb583de8a0da5e4ef7ae39ec8caa65d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQ5SOG2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEg97X%2FjheQ6UiLVCdvLhi3jNKM5mWVCCHgRPH1Ve8VDAiB9EOkiscgxyUDTcKzNkmbz4hdjmXTq73tVlbnq5EDimiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI1EafNkzWf5HTCLVKtwDJD9glCTg8KuSFXetsDuNtVrSj7im28z9C%2ByK5mDesYHGjy5bgMBXc4tqVHxe4ZuSNXRLGqLtyT%2FCG6NkwoqOl59TN%2FDHR9Q%2BAo1ecUv4SeOPVKMngCZiboSgj%2BteeNZWlcyOsOPLd1JAhw16gkgK2STbZ57oogVYRD2b6uS50IpBZgKARCVWz%2FC%2FoXQpcVMhjmsXPrPOIHWt6QpQluIUDE4n7DuHWwSxZYJHu1hof%2BlPYhzpehbGWnEtPpJei7mdmwSrP%2BVpkPvmDuIPT2O7r7sxgINNHh8Jmir5bEM8uAD%2BbG3CoFN2miPM8yFWvXMiTKJAAlZFZxyHNW8SK8coRokiWTtJAdANn1R%2B1CA8oxH8xTacDDedDdRHEsZgtfjZYbdgLNBcbYiZRG7n5XsZtBcMpbOnW37G%2B92YA4uMidGGBnvMBukvG9B47K%2FNdxlCtNVb9%2BcD7YXoArf5LRZA%2Fz67OgwHQDmO6wAEP6U%2B1DudRKn9dBxcLqIJxFcoACMtVaMx8u49T1czTVJp5fVIbvvnLdb0uMGsRQleYD1X3D%2Fpcgs2V1Ci5AUMKC3NNXcIvZFMiHgDiidV%2BzPbxgh%2BgGL1Y7hF%2Fw4rQOK8fwhzpvRcE5LuMzR5tlP1wk8wqLH6vAY6pgHhwD8fdKHVW9erguf9bLROxEy24y%2BxGSOiQ0DNrFEIwAb8sW1NMjnuqLH%2F4zqQOeO8sqT95IaEtvD5qeMExnXOknpQEk0%2Bi7k9PKyv00ViEN3Y%2Btc3c1ezxX0lEw6BsJ7sjfK3n%2FVT2Wb6aCLIJsOXfZdMdru9BcK0AfN%2B49F%2Fr2aPLjZonPDaXcHmnsXGx8IdS%2FkEXqwKtICyWONa2WfpNmpEwDC2&X-Amz-Signature=f665d066f0773dd71899088eee6cd16ed3a379c748bb7012898ebc4761d41bfa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQ5SOG2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEg97X%2FjheQ6UiLVCdvLhi3jNKM5mWVCCHgRPH1Ve8VDAiB9EOkiscgxyUDTcKzNkmbz4hdjmXTq73tVlbnq5EDimiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI1EafNkzWf5HTCLVKtwDJD9glCTg8KuSFXetsDuNtVrSj7im28z9C%2ByK5mDesYHGjy5bgMBXc4tqVHxe4ZuSNXRLGqLtyT%2FCG6NkwoqOl59TN%2FDHR9Q%2BAo1ecUv4SeOPVKMngCZiboSgj%2BteeNZWlcyOsOPLd1JAhw16gkgK2STbZ57oogVYRD2b6uS50IpBZgKARCVWz%2FC%2FoXQpcVMhjmsXPrPOIHWt6QpQluIUDE4n7DuHWwSxZYJHu1hof%2BlPYhzpehbGWnEtPpJei7mdmwSrP%2BVpkPvmDuIPT2O7r7sxgINNHh8Jmir5bEM8uAD%2BbG3CoFN2miPM8yFWvXMiTKJAAlZFZxyHNW8SK8coRokiWTtJAdANn1R%2B1CA8oxH8xTacDDedDdRHEsZgtfjZYbdgLNBcbYiZRG7n5XsZtBcMpbOnW37G%2B92YA4uMidGGBnvMBukvG9B47K%2FNdxlCtNVb9%2BcD7YXoArf5LRZA%2Fz67OgwHQDmO6wAEP6U%2B1DudRKn9dBxcLqIJxFcoACMtVaMx8u49T1czTVJp5fVIbvvnLdb0uMGsRQleYD1X3D%2Fpcgs2V1Ci5AUMKC3NNXcIvZFMiHgDiidV%2BzPbxgh%2BgGL1Y7hF%2Fw4rQOK8fwhzpvRcE5LuMzR5tlP1wk8wqLH6vAY6pgHhwD8fdKHVW9erguf9bLROxEy24y%2BxGSOiQ0DNrFEIwAb8sW1NMjnuqLH%2F4zqQOeO8sqT95IaEtvD5qeMExnXOknpQEk0%2Bi7k9PKyv00ViEN3Y%2Btc3c1ezxX0lEw6BsJ7sjfK3n%2FVT2Wb6aCLIJsOXfZdMdru9BcK0AfN%2B49F%2Fr2aPLjZonPDaXcHmnsXGx8IdS%2FkEXqwKtICyWONa2WfpNmpEwDC2&X-Amz-Signature=a1107b8cc4aa3bad57c9ae1b683c071b275bc4ea17c1843cb9613472a2d703f4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQ5SOG2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEg97X%2FjheQ6UiLVCdvLhi3jNKM5mWVCCHgRPH1Ve8VDAiB9EOkiscgxyUDTcKzNkmbz4hdjmXTq73tVlbnq5EDimiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI1EafNkzWf5HTCLVKtwDJD9glCTg8KuSFXetsDuNtVrSj7im28z9C%2ByK5mDesYHGjy5bgMBXc4tqVHxe4ZuSNXRLGqLtyT%2FCG6NkwoqOl59TN%2FDHR9Q%2BAo1ecUv4SeOPVKMngCZiboSgj%2BteeNZWlcyOsOPLd1JAhw16gkgK2STbZ57oogVYRD2b6uS50IpBZgKARCVWz%2FC%2FoXQpcVMhjmsXPrPOIHWt6QpQluIUDE4n7DuHWwSxZYJHu1hof%2BlPYhzpehbGWnEtPpJei7mdmwSrP%2BVpkPvmDuIPT2O7r7sxgINNHh8Jmir5bEM8uAD%2BbG3CoFN2miPM8yFWvXMiTKJAAlZFZxyHNW8SK8coRokiWTtJAdANn1R%2B1CA8oxH8xTacDDedDdRHEsZgtfjZYbdgLNBcbYiZRG7n5XsZtBcMpbOnW37G%2B92YA4uMidGGBnvMBukvG9B47K%2FNdxlCtNVb9%2BcD7YXoArf5LRZA%2Fz67OgwHQDmO6wAEP6U%2B1DudRKn9dBxcLqIJxFcoACMtVaMx8u49T1czTVJp5fVIbvvnLdb0uMGsRQleYD1X3D%2Fpcgs2V1Ci5AUMKC3NNXcIvZFMiHgDiidV%2BzPbxgh%2BgGL1Y7hF%2Fw4rQOK8fwhzpvRcE5LuMzR5tlP1wk8wqLH6vAY6pgHhwD8fdKHVW9erguf9bLROxEy24y%2BxGSOiQ0DNrFEIwAb8sW1NMjnuqLH%2F4zqQOeO8sqT95IaEtvD5qeMExnXOknpQEk0%2Bi7k9PKyv00ViEN3Y%2Btc3c1ezxX0lEw6BsJ7sjfK3n%2FVT2Wb6aCLIJsOXfZdMdru9BcK0AfN%2B49F%2Fr2aPLjZonPDaXcHmnsXGx8IdS%2FkEXqwKtICyWONa2WfpNmpEwDC2&X-Amz-Signature=c595667d01da731a4d79badbc46f368c02c4f22587c18c955c4382a8894ed51c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQ5SOG2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEg97X%2FjheQ6UiLVCdvLhi3jNKM5mWVCCHgRPH1Ve8VDAiB9EOkiscgxyUDTcKzNkmbz4hdjmXTq73tVlbnq5EDimiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI1EafNkzWf5HTCLVKtwDJD9glCTg8KuSFXetsDuNtVrSj7im28z9C%2ByK5mDesYHGjy5bgMBXc4tqVHxe4ZuSNXRLGqLtyT%2FCG6NkwoqOl59TN%2FDHR9Q%2BAo1ecUv4SeOPVKMngCZiboSgj%2BteeNZWlcyOsOPLd1JAhw16gkgK2STbZ57oogVYRD2b6uS50IpBZgKARCVWz%2FC%2FoXQpcVMhjmsXPrPOIHWt6QpQluIUDE4n7DuHWwSxZYJHu1hof%2BlPYhzpehbGWnEtPpJei7mdmwSrP%2BVpkPvmDuIPT2O7r7sxgINNHh8Jmir5bEM8uAD%2BbG3CoFN2miPM8yFWvXMiTKJAAlZFZxyHNW8SK8coRokiWTtJAdANn1R%2B1CA8oxH8xTacDDedDdRHEsZgtfjZYbdgLNBcbYiZRG7n5XsZtBcMpbOnW37G%2B92YA4uMidGGBnvMBukvG9B47K%2FNdxlCtNVb9%2BcD7YXoArf5LRZA%2Fz67OgwHQDmO6wAEP6U%2B1DudRKn9dBxcLqIJxFcoACMtVaMx8u49T1czTVJp5fVIbvvnLdb0uMGsRQleYD1X3D%2Fpcgs2V1Ci5AUMKC3NNXcIvZFMiHgDiidV%2BzPbxgh%2BgGL1Y7hF%2Fw4rQOK8fwhzpvRcE5LuMzR5tlP1wk8wqLH6vAY6pgHhwD8fdKHVW9erguf9bLROxEy24y%2BxGSOiQ0DNrFEIwAb8sW1NMjnuqLH%2F4zqQOeO8sqT95IaEtvD5qeMExnXOknpQEk0%2Bi7k9PKyv00ViEN3Y%2Btc3c1ezxX0lEw6BsJ7sjfK3n%2FVT2Wb6aCLIJsOXfZdMdru9BcK0AfN%2B49F%2Fr2aPLjZonPDaXcHmnsXGx8IdS%2FkEXqwKtICyWONa2WfpNmpEwDC2&X-Amz-Signature=6f1aec7840269e316fe94d6696ac92782debfcdd6f6855845a3a56d9d37d8b0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQ5SOG2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEg97X%2FjheQ6UiLVCdvLhi3jNKM5mWVCCHgRPH1Ve8VDAiB9EOkiscgxyUDTcKzNkmbz4hdjmXTq73tVlbnq5EDimiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI1EafNkzWf5HTCLVKtwDJD9glCTg8KuSFXetsDuNtVrSj7im28z9C%2ByK5mDesYHGjy5bgMBXc4tqVHxe4ZuSNXRLGqLtyT%2FCG6NkwoqOl59TN%2FDHR9Q%2BAo1ecUv4SeOPVKMngCZiboSgj%2BteeNZWlcyOsOPLd1JAhw16gkgK2STbZ57oogVYRD2b6uS50IpBZgKARCVWz%2FC%2FoXQpcVMhjmsXPrPOIHWt6QpQluIUDE4n7DuHWwSxZYJHu1hof%2BlPYhzpehbGWnEtPpJei7mdmwSrP%2BVpkPvmDuIPT2O7r7sxgINNHh8Jmir5bEM8uAD%2BbG3CoFN2miPM8yFWvXMiTKJAAlZFZxyHNW8SK8coRokiWTtJAdANn1R%2B1CA8oxH8xTacDDedDdRHEsZgtfjZYbdgLNBcbYiZRG7n5XsZtBcMpbOnW37G%2B92YA4uMidGGBnvMBukvG9B47K%2FNdxlCtNVb9%2BcD7YXoArf5LRZA%2Fz67OgwHQDmO6wAEP6U%2B1DudRKn9dBxcLqIJxFcoACMtVaMx8u49T1czTVJp5fVIbvvnLdb0uMGsRQleYD1X3D%2Fpcgs2V1Ci5AUMKC3NNXcIvZFMiHgDiidV%2BzPbxgh%2BgGL1Y7hF%2Fw4rQOK8fwhzpvRcE5LuMzR5tlP1wk8wqLH6vAY6pgHhwD8fdKHVW9erguf9bLROxEy24y%2BxGSOiQ0DNrFEIwAb8sW1NMjnuqLH%2F4zqQOeO8sqT95IaEtvD5qeMExnXOknpQEk0%2Bi7k9PKyv00ViEN3Y%2Btc3c1ezxX0lEw6BsJ7sjfK3n%2FVT2Wb6aCLIJsOXfZdMdru9BcK0AfN%2B49F%2Fr2aPLjZonPDaXcHmnsXGx8IdS%2FkEXqwKtICyWONa2WfpNmpEwDC2&X-Amz-Signature=27a5ee2aa07afe0430cbb5df617c614d86f2eb4927b22816fc018300258cba92&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GQ5SOG2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEg97X%2FjheQ6UiLVCdvLhi3jNKM5mWVCCHgRPH1Ve8VDAiB9EOkiscgxyUDTcKzNkmbz4hdjmXTq73tVlbnq5EDimiqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI1EafNkzWf5HTCLVKtwDJD9glCTg8KuSFXetsDuNtVrSj7im28z9C%2ByK5mDesYHGjy5bgMBXc4tqVHxe4ZuSNXRLGqLtyT%2FCG6NkwoqOl59TN%2FDHR9Q%2BAo1ecUv4SeOPVKMngCZiboSgj%2BteeNZWlcyOsOPLd1JAhw16gkgK2STbZ57oogVYRD2b6uS50IpBZgKARCVWz%2FC%2FoXQpcVMhjmsXPrPOIHWt6QpQluIUDE4n7DuHWwSxZYJHu1hof%2BlPYhzpehbGWnEtPpJei7mdmwSrP%2BVpkPvmDuIPT2O7r7sxgINNHh8Jmir5bEM8uAD%2BbG3CoFN2miPM8yFWvXMiTKJAAlZFZxyHNW8SK8coRokiWTtJAdANn1R%2B1CA8oxH8xTacDDedDdRHEsZgtfjZYbdgLNBcbYiZRG7n5XsZtBcMpbOnW37G%2B92YA4uMidGGBnvMBukvG9B47K%2FNdxlCtNVb9%2BcD7YXoArf5LRZA%2Fz67OgwHQDmO6wAEP6U%2B1DudRKn9dBxcLqIJxFcoACMtVaMx8u49T1czTVJp5fVIbvvnLdb0uMGsRQleYD1X3D%2Fpcgs2V1Ci5AUMKC3NNXcIvZFMiHgDiidV%2BzPbxgh%2BgGL1Y7hF%2Fw4rQOK8fwhzpvRcE5LuMzR5tlP1wk8wqLH6vAY6pgHhwD8fdKHVW9erguf9bLROxEy24y%2BxGSOiQ0DNrFEIwAb8sW1NMjnuqLH%2F4zqQOeO8sqT95IaEtvD5qeMExnXOknpQEk0%2Bi7k9PKyv00ViEN3Y%2Btc3c1ezxX0lEw6BsJ7sjfK3n%2FVT2Wb6aCLIJsOXfZdMdru9BcK0AfN%2B49F%2Fr2aPLjZonPDaXcHmnsXGx8IdS%2FkEXqwKtICyWONa2WfpNmpEwDC2&X-Amz-Signature=9ec9eaf3ed5aa375472fde7010cc0292a06d2aa6aea56b0394e7434b4d55e077&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USR326RK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2F5R1l109o6uqLCUtjAEyXtic722X4fU6iQqzhfZ94dAiEA7tNN4fcuA4OJRX80CNBVgDbyePKSxAWJ4tS39Q9bFgMqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNT9VFJ6%2FIDj6VBQISrcAwI8e2Zmc4Qq4NgMI38yU3%2BHaBV3B%2FWPGMlzPbCHVAwXioPAMWMyM3nrdqpV4jh1bGTXdRTC7m7Tq14jpZpOi5z4Liquk1ucmEOHZlkDRs0fDcz0W8hNdH2h0FaFt6zq6puWN8jXCSxkyyW5Aq7kP28icd50583LAKKwYzrQICn%2BpHZs0ZTHkv%2B1wxhyv%2F6%2FRuLzTFC5MA8ys1xZuQIVE2ZPXAsUpXtELVklJ8e2R1Pc222PO6SpqUaxbj2UOCotcpKtLvVKtKQFaV3mr57zPpGq4mdf6jPPEmLU7MCd%2FYDez0h6q3ebsWRfqyRT9EfSQGBOLldXbGgXM7j0hnme4sVj4lRs2U5IIdR2FGtLSljPY%2BWFbfPjMsdEQ%2FsJMshU9FrbsRgrKZzreLolpsmrl2KbCJA9%2BMm5%2FwYgXl%2BNv0MDq0GHHy5ycD4vr9o%2FU5J%2Fs2X6INXHIB8halX%2Flra3rCLRTZQ%2FsstlcroixA%2BlFP%2By1F11e9sLJOA6vifh2qrrRDohA0YFYpgHSH8AntdjteoGaKQpzXaDk8A388osv%2FgHXMdZTWDaxPMO5pjB3Pxs%2BZ0swlrlZhsm5qV8rHX3z0Bq5sfaJuL12zipzv8ItjvdBRz3zsCmwpG5gLxaMKix%2BrwGOqUBJZOA8G%2FNrOhRJfLUbpWhZSEtUzvloZPOpcrMmmzReQFG3N9rgmbwBmZTDapgh5Oqm15WGjsJXwrxYysP8eB4%2FzP6wzwLfY8nryMOEJLg6glQDC%2B1KkW%2BCaBqT7qVlhbeWJ%2FGk0DtaqBAd7JSQ4oeBBAkq0AEtV0rFHiQbN73nuz2LthlPYlC7hSSXTKBtQ%2F5c%2BNO70NKls2vYC2rwzkARr5Ly7wj&X-Amz-Signature=ca01aa326eb729c41b6d555368628bc2a767c8c1c2f04bf27c1c619d2c119a44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZN5XKPR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID8XnJIWQi7ECXyI0rlCcfF7OLWTDHMbx%2F6EHKwfTRgwAiBPpqG%2BajimqbUeDdVhmp%2Fe3ypMFDqtHCrZJFjSE3sIJCqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWH0x2EPOMR%2FSdxFKtwD6I6tp%2FMTe8KqnCxSp71%2B5AfxuwzHhiyfnVGl5EhpRaUmXNLZkQiywr7r7%2Bt%2FK9yWMzVbFw1MURJT4dwA6cjtwbiuuKXJ5l%2FtXBtlIuy4n3%2BSJs7Rtl06XXjEaW8GqRI47uS9fYRds%2FiLHXEw4vIhssnyiiRBeX5lbjuBeVL4RsX8TDe334uXII5Kb2mp2CCoaHhs3LHs24hIqtracFnqxLbDQ8XWkQDq4GPkA3N2IQrFNCEWuLd%2F7yRFpDHeXjIg97yOtZAvZ8LcXZqwjyiwD%2BV0UAJOwlmFUJHhqE7CV08mx4EBCy07Xqddo%2BGAxHCHteNoMKvgyOzlAFVIL%2BI2tPt8cGpbyKfIqwTuQG712M8GXSeyMVwgRivAP4Tw4nYtQm69IjdJhp8KT9eHQkGOQX8R%2FAbm0wgpvMWEMBURu8h6HjNO4ivIEOKJIXlZaKOKZ16jF%2BNMfLUvW0qpiI3OpyhhIRSMYVm2F7ksE2fgKUAwyNu2MMv%2B0ad8%2BxwRuz9ZgLhbqNdp0gwhDlqR5mIIMRYwvUKskqEQVIvgxl%2Bc3tHwxBrIhB%2B26Vp25iLuegbEqxNxYNt5i%2FthBNx8DH%2BxMDmURZgi0BhkruL0kNrgPgaCIJiC%2FGArTDyD1Dkw7LD6vAY6pgHPAafiFWOqcJgkGztY%2BQgf1qn9CGT%2BGSfBSysyo8HJmX7msWzuGDUrXM29kegggnax%2F0Fs5PYCZqjlbwLLqb9UJuiJiConIp2jccMYa275xgfKw5UMG0ELtlzboyf86lO6wi1h4X6fcr82v%2FfsFSQW6nQuWv5Wm3NfueAazMEIiA%2FFMQoDhQ3oo2geGK0tt9y3bzHGE5HMC0q6ZgeBGoR7wjFiORoh&X-Amz-Signature=4ad1e52c365b63b54404219a9bfc67cea33c95442d5fa65a4720dc8c10418314&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRSSIFE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwW5CiwefJuA6dTYaMnpw%2BKVibLAIj2dZi8J18RfWDZAiAIbO4O4HTc3llpXW0PbiCS0SM1WtNtWLHb22hjIyKBmyqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPgDRJymAWa5nJr6aKtwDDzcT4JzC00dkWSl3y%2Fk9M%2BigEJ8DknQjbeyxYaE02xlBJCIXzT6X8CbDJ1HniXw3XJ7V4DZF6C977qKymD5fzd2FayCPa7bWLsE8b4rv3XQ2%2F6eD01tZn5%2BGJVPXPhtq2W6snC40a2Tr1ZxBVVgaFpCPjh7beoCjEWrOPwX6HJ6lsVO0jCjAPlb1cgNBUs7bIFOsco6bIsplH399wgcgNu384BLUi0Q%2Bo2EYALK9oS6Mnqei4n15uoWlEoN6%2FOuVEs8%2BN2WPiV0OBJMtZzwlRRS8e63t6aSfXaHZKol%2B2zp9UhnOuV1%2BUfhTWAT3s51tvH4Noke8BCJ7tVXb4yuzSHuZNNZhaWCF%2Faj7DlOtzGq0VX5ft9PwpXeG8f31cKxvsWN032fLKecLnrOOxNYbpRgyDkD84VR7Kv%2B5ZOaUSrJ1OxGAXYGcWaFfPGP10GslS1BmKbZHH41E5XKq61KfkMJsa8NH%2Fb%2BW7s2nnM14KOxuwUn%2Fgh2Lt%2Fh1KWQ813Svc8PeQps8gd3noMtk1qMt5k3gBLtAnEI4ZN7O9E4X2nUtVgw4qyjIUYDC37Kq%2FqydmWg3Jkk5uhnNYs4Xwkc42VXMbZif6F7MqFB3NeZ4wmArqeLPmESEc054OAow9bD6vAY6pgH5zqCQP4l7eieURosxuTKLQRAvPWmIOPDgyIc9rlBhTu4I2AI8DKmm6XvhpTvpjDFAkJjRMdxyMmTRgogow9FERLEKM5PXxhmcLr9If2oal9Wczp9dWejcQlPLnPF319ZYWMRoHrRw0zcfHJ05GIgAwJ7jQnUIUUklrV9GeZQSJvj0CWNt1rZi5WH35U9Z%2BQ6LSGDoaCFEOlHvqDI0buHi1LVjWxAv&X-Amz-Signature=e2b8febf3a9ada61ab8162a8d356a08ee6355afe4b79e57a8f0f01c978bbc84b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRSSIFE4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwW5CiwefJuA6dTYaMnpw%2BKVibLAIj2dZi8J18RfWDZAiAIbO4O4HTc3llpXW0PbiCS0SM1WtNtWLHb22hjIyKBmyqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPgDRJymAWa5nJr6aKtwDDzcT4JzC00dkWSl3y%2Fk9M%2BigEJ8DknQjbeyxYaE02xlBJCIXzT6X8CbDJ1HniXw3XJ7V4DZF6C977qKymD5fzd2FayCPa7bWLsE8b4rv3XQ2%2F6eD01tZn5%2BGJVPXPhtq2W6snC40a2Tr1ZxBVVgaFpCPjh7beoCjEWrOPwX6HJ6lsVO0jCjAPlb1cgNBUs7bIFOsco6bIsplH399wgcgNu384BLUi0Q%2Bo2EYALK9oS6Mnqei4n15uoWlEoN6%2FOuVEs8%2BN2WPiV0OBJMtZzwlRRS8e63t6aSfXaHZKol%2B2zp9UhnOuV1%2BUfhTWAT3s51tvH4Noke8BCJ7tVXb4yuzSHuZNNZhaWCF%2Faj7DlOtzGq0VX5ft9PwpXeG8f31cKxvsWN032fLKecLnrOOxNYbpRgyDkD84VR7Kv%2B5ZOaUSrJ1OxGAXYGcWaFfPGP10GslS1BmKbZHH41E5XKq61KfkMJsa8NH%2Fb%2BW7s2nnM14KOxuwUn%2Fgh2Lt%2Fh1KWQ813Svc8PeQps8gd3noMtk1qMt5k3gBLtAnEI4ZN7O9E4X2nUtVgw4qyjIUYDC37Kq%2FqydmWg3Jkk5uhnNYs4Xwkc42VXMbZif6F7MqFB3NeZ4wmArqeLPmESEc054OAow9bD6vAY6pgH5zqCQP4l7eieURosxuTKLQRAvPWmIOPDgyIc9rlBhTu4I2AI8DKmm6XvhpTvpjDFAkJjRMdxyMmTRgogow9FERLEKM5PXxhmcLr9If2oal9Wczp9dWejcQlPLnPF319ZYWMRoHrRw0zcfHJ05GIgAwJ7jQnUIUUklrV9GeZQSJvj0CWNt1rZi5WH35U9Z%2BQ6LSGDoaCFEOlHvqDI0buHi1LVjWxAv&X-Amz-Signature=fb8b06f7fb0ecfc7c70f249993575fc36dd7509a73aa64e07f61df7f442d6f30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
