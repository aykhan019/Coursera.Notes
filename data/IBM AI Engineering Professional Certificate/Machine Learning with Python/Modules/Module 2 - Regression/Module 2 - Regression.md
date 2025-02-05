

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDRZS5QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCICpCPzMwL7mh7f8eaS3j%2B2NUH55sbggbA%2Fv6RfJkBMstAiBT3izGmBjCu57DmdTcCqSFaD27mg5RG4kFcckkIEamgyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMDsE9iKLwGvBiLWdhKtwDqli%2BLGVgZRdTvxfiOvnCL6jyGgZQEDZAunYHn%2FO6vMXGxU9Ue%2FguyqbzagdAzramgUhSx%2BSYp041h6sXNZgcGDfcrjgVjb6jJNoSztIPb6qAubpbUZshSSY1hk%2B53wBmiLcI2SeFOJBbBXSE624kCus5C%2FAd%2FxccZ2A42eJ6hzXHNskfYFExjX3xSdg33JpUxA8TZW8mM5581hHiDpG0VPm5MmcejRn14TJtkZ8Yw77ztNU2rBhA3hEuoQxLzcn%2FOkRljoNsWsgGA9C8sGdBkQ3pZDKT48iaS1ZzBsK6x%2BMG5Idn0aRr8Cd03HtgBnUX%2FmXFy4GjqhX%2Be%2FWmGvMrqT7be7H84h%2FGxBQmtsK%2FTHAFoutAKFrSDxHeleX0VCmmzwMy9sPxF0NDNnMU%2FcLlyWleopNbA4WgakYeQIg3UgnYcP%2BedUke%2FXConY8t3qU0d3trFh9mNWMxrOoZjMD4SbqFgTcwJLyAIuMxVDJ00Ins63oeDP5qAV%2Bp%2F4iRfXLasnJAjTYFFgNFP1ixruDxsIMlkFYyo7%2FJYuIIzHdVmTv4p%2FwGtNXBP1Ge3Esi6BAZMXJB%2FjQzRPIlxCheD0UJE7mVpi%2FBuEcwYqu1QyxJua1%2BX%2FqLUz79U5wzEu8wjO%2BMvQY6pgH%2F5P0uNgH3L2phVe%2B%2BIbKhwlltMlj9pF71Qum2eWHx1mR4RuZA5NJ9j8IHb09fmdxapnuq4c0jNDVhaPPZXfbNmIa3KHcFxOCaIA6ow5ZydRbS2NUcM4zh9%2BiEGftvsByeOpBaT0MKlaN%2Fa6xkoXFBOh2IlnmQB1w8NbVb0YDQv%2FsD2XRt96esUNbd%2F0LnH3GRZTPIOkbLKHHfe1Ju3jQEZH5%2Bpfe3&X-Amz-Signature=feeec14bbb2207c0fb3db628eda7b27a9f8df36f1382f14e56e0138d0b7878c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDRZS5QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCICpCPzMwL7mh7f8eaS3j%2B2NUH55sbggbA%2Fv6RfJkBMstAiBT3izGmBjCu57DmdTcCqSFaD27mg5RG4kFcckkIEamgyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMDsE9iKLwGvBiLWdhKtwDqli%2BLGVgZRdTvxfiOvnCL6jyGgZQEDZAunYHn%2FO6vMXGxU9Ue%2FguyqbzagdAzramgUhSx%2BSYp041h6sXNZgcGDfcrjgVjb6jJNoSztIPb6qAubpbUZshSSY1hk%2B53wBmiLcI2SeFOJBbBXSE624kCus5C%2FAd%2FxccZ2A42eJ6hzXHNskfYFExjX3xSdg33JpUxA8TZW8mM5581hHiDpG0VPm5MmcejRn14TJtkZ8Yw77ztNU2rBhA3hEuoQxLzcn%2FOkRljoNsWsgGA9C8sGdBkQ3pZDKT48iaS1ZzBsK6x%2BMG5Idn0aRr8Cd03HtgBnUX%2FmXFy4GjqhX%2Be%2FWmGvMrqT7be7H84h%2FGxBQmtsK%2FTHAFoutAKFrSDxHeleX0VCmmzwMy9sPxF0NDNnMU%2FcLlyWleopNbA4WgakYeQIg3UgnYcP%2BedUke%2FXConY8t3qU0d3trFh9mNWMxrOoZjMD4SbqFgTcwJLyAIuMxVDJ00Ins63oeDP5qAV%2Bp%2F4iRfXLasnJAjTYFFgNFP1ixruDxsIMlkFYyo7%2FJYuIIzHdVmTv4p%2FwGtNXBP1Ge3Esi6BAZMXJB%2FjQzRPIlxCheD0UJE7mVpi%2FBuEcwYqu1QyxJua1%2BX%2FqLUz79U5wzEu8wjO%2BMvQY6pgH%2F5P0uNgH3L2phVe%2B%2BIbKhwlltMlj9pF71Qum2eWHx1mR4RuZA5NJ9j8IHb09fmdxapnuq4c0jNDVhaPPZXfbNmIa3KHcFxOCaIA6ow5ZydRbS2NUcM4zh9%2BiEGftvsByeOpBaT0MKlaN%2Fa6xkoXFBOh2IlnmQB1w8NbVb0YDQv%2FsD2XRt96esUNbd%2F0LnH3GRZTPIOkbLKHHfe1Ju3jQEZH5%2Bpfe3&X-Amz-Signature=73d74bcacb0d86386e0c353c4f50201e41d56886e2a02fbaef66bfee9a01789f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDRZS5QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCICpCPzMwL7mh7f8eaS3j%2B2NUH55sbggbA%2Fv6RfJkBMstAiBT3izGmBjCu57DmdTcCqSFaD27mg5RG4kFcckkIEamgyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMDsE9iKLwGvBiLWdhKtwDqli%2BLGVgZRdTvxfiOvnCL6jyGgZQEDZAunYHn%2FO6vMXGxU9Ue%2FguyqbzagdAzramgUhSx%2BSYp041h6sXNZgcGDfcrjgVjb6jJNoSztIPb6qAubpbUZshSSY1hk%2B53wBmiLcI2SeFOJBbBXSE624kCus5C%2FAd%2FxccZ2A42eJ6hzXHNskfYFExjX3xSdg33JpUxA8TZW8mM5581hHiDpG0VPm5MmcejRn14TJtkZ8Yw77ztNU2rBhA3hEuoQxLzcn%2FOkRljoNsWsgGA9C8sGdBkQ3pZDKT48iaS1ZzBsK6x%2BMG5Idn0aRr8Cd03HtgBnUX%2FmXFy4GjqhX%2Be%2FWmGvMrqT7be7H84h%2FGxBQmtsK%2FTHAFoutAKFrSDxHeleX0VCmmzwMy9sPxF0NDNnMU%2FcLlyWleopNbA4WgakYeQIg3UgnYcP%2BedUke%2FXConY8t3qU0d3trFh9mNWMxrOoZjMD4SbqFgTcwJLyAIuMxVDJ00Ins63oeDP5qAV%2Bp%2F4iRfXLasnJAjTYFFgNFP1ixruDxsIMlkFYyo7%2FJYuIIzHdVmTv4p%2FwGtNXBP1Ge3Esi6BAZMXJB%2FjQzRPIlxCheD0UJE7mVpi%2FBuEcwYqu1QyxJua1%2BX%2FqLUz79U5wzEu8wjO%2BMvQY6pgH%2F5P0uNgH3L2phVe%2B%2BIbKhwlltMlj9pF71Qum2eWHx1mR4RuZA5NJ9j8IHb09fmdxapnuq4c0jNDVhaPPZXfbNmIa3KHcFxOCaIA6ow5ZydRbS2NUcM4zh9%2BiEGftvsByeOpBaT0MKlaN%2Fa6xkoXFBOh2IlnmQB1w8NbVb0YDQv%2FsD2XRt96esUNbd%2F0LnH3GRZTPIOkbLKHHfe1Ju3jQEZH5%2Bpfe3&X-Amz-Signature=1701523b5f3a2f1aba9a37ea8afda680109ff522f522a4987d6a4ff69b17b931&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDRZS5QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCICpCPzMwL7mh7f8eaS3j%2B2NUH55sbggbA%2Fv6RfJkBMstAiBT3izGmBjCu57DmdTcCqSFaD27mg5RG4kFcckkIEamgyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMDsE9iKLwGvBiLWdhKtwDqli%2BLGVgZRdTvxfiOvnCL6jyGgZQEDZAunYHn%2FO6vMXGxU9Ue%2FguyqbzagdAzramgUhSx%2BSYp041h6sXNZgcGDfcrjgVjb6jJNoSztIPb6qAubpbUZshSSY1hk%2B53wBmiLcI2SeFOJBbBXSE624kCus5C%2FAd%2FxccZ2A42eJ6hzXHNskfYFExjX3xSdg33JpUxA8TZW8mM5581hHiDpG0VPm5MmcejRn14TJtkZ8Yw77ztNU2rBhA3hEuoQxLzcn%2FOkRljoNsWsgGA9C8sGdBkQ3pZDKT48iaS1ZzBsK6x%2BMG5Idn0aRr8Cd03HtgBnUX%2FmXFy4GjqhX%2Be%2FWmGvMrqT7be7H84h%2FGxBQmtsK%2FTHAFoutAKFrSDxHeleX0VCmmzwMy9sPxF0NDNnMU%2FcLlyWleopNbA4WgakYeQIg3UgnYcP%2BedUke%2FXConY8t3qU0d3trFh9mNWMxrOoZjMD4SbqFgTcwJLyAIuMxVDJ00Ins63oeDP5qAV%2Bp%2F4iRfXLasnJAjTYFFgNFP1ixruDxsIMlkFYyo7%2FJYuIIzHdVmTv4p%2FwGtNXBP1Ge3Esi6BAZMXJB%2FjQzRPIlxCheD0UJE7mVpi%2FBuEcwYqu1QyxJua1%2BX%2FqLUz79U5wzEu8wjO%2BMvQY6pgH%2F5P0uNgH3L2phVe%2B%2BIbKhwlltMlj9pF71Qum2eWHx1mR4RuZA5NJ9j8IHb09fmdxapnuq4c0jNDVhaPPZXfbNmIa3KHcFxOCaIA6ow5ZydRbS2NUcM4zh9%2BiEGftvsByeOpBaT0MKlaN%2Fa6xkoXFBOh2IlnmQB1w8NbVb0YDQv%2FsD2XRt96esUNbd%2F0LnH3GRZTPIOkbLKHHfe1Ju3jQEZH5%2Bpfe3&X-Amz-Signature=30796b73d8abad8e2072171a43c5f058d0528c68e27d1cc3e95e6e94dc144fae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDRZS5QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCICpCPzMwL7mh7f8eaS3j%2B2NUH55sbggbA%2Fv6RfJkBMstAiBT3izGmBjCu57DmdTcCqSFaD27mg5RG4kFcckkIEamgyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMDsE9iKLwGvBiLWdhKtwDqli%2BLGVgZRdTvxfiOvnCL6jyGgZQEDZAunYHn%2FO6vMXGxU9Ue%2FguyqbzagdAzramgUhSx%2BSYp041h6sXNZgcGDfcrjgVjb6jJNoSztIPb6qAubpbUZshSSY1hk%2B53wBmiLcI2SeFOJBbBXSE624kCus5C%2FAd%2FxccZ2A42eJ6hzXHNskfYFExjX3xSdg33JpUxA8TZW8mM5581hHiDpG0VPm5MmcejRn14TJtkZ8Yw77ztNU2rBhA3hEuoQxLzcn%2FOkRljoNsWsgGA9C8sGdBkQ3pZDKT48iaS1ZzBsK6x%2BMG5Idn0aRr8Cd03HtgBnUX%2FmXFy4GjqhX%2Be%2FWmGvMrqT7be7H84h%2FGxBQmtsK%2FTHAFoutAKFrSDxHeleX0VCmmzwMy9sPxF0NDNnMU%2FcLlyWleopNbA4WgakYeQIg3UgnYcP%2BedUke%2FXConY8t3qU0d3trFh9mNWMxrOoZjMD4SbqFgTcwJLyAIuMxVDJ00Ins63oeDP5qAV%2Bp%2F4iRfXLasnJAjTYFFgNFP1ixruDxsIMlkFYyo7%2FJYuIIzHdVmTv4p%2FwGtNXBP1Ge3Esi6BAZMXJB%2FjQzRPIlxCheD0UJE7mVpi%2FBuEcwYqu1QyxJua1%2BX%2FqLUz79U5wzEu8wjO%2BMvQY6pgH%2F5P0uNgH3L2phVe%2B%2BIbKhwlltMlj9pF71Qum2eWHx1mR4RuZA5NJ9j8IHb09fmdxapnuq4c0jNDVhaPPZXfbNmIa3KHcFxOCaIA6ow5ZydRbS2NUcM4zh9%2BiEGftvsByeOpBaT0MKlaN%2Fa6xkoXFBOh2IlnmQB1w8NbVb0YDQv%2FsD2XRt96esUNbd%2F0LnH3GRZTPIOkbLKHHfe1Ju3jQEZH5%2Bpfe3&X-Amz-Signature=b5a13a58672e8e26c624e57debd00ae26cd72ca0a83b55e2de99b476fa4f27db&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDRZS5QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCICpCPzMwL7mh7f8eaS3j%2B2NUH55sbggbA%2Fv6RfJkBMstAiBT3izGmBjCu57DmdTcCqSFaD27mg5RG4kFcckkIEamgyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMDsE9iKLwGvBiLWdhKtwDqli%2BLGVgZRdTvxfiOvnCL6jyGgZQEDZAunYHn%2FO6vMXGxU9Ue%2FguyqbzagdAzramgUhSx%2BSYp041h6sXNZgcGDfcrjgVjb6jJNoSztIPb6qAubpbUZshSSY1hk%2B53wBmiLcI2SeFOJBbBXSE624kCus5C%2FAd%2FxccZ2A42eJ6hzXHNskfYFExjX3xSdg33JpUxA8TZW8mM5581hHiDpG0VPm5MmcejRn14TJtkZ8Yw77ztNU2rBhA3hEuoQxLzcn%2FOkRljoNsWsgGA9C8sGdBkQ3pZDKT48iaS1ZzBsK6x%2BMG5Idn0aRr8Cd03HtgBnUX%2FmXFy4GjqhX%2Be%2FWmGvMrqT7be7H84h%2FGxBQmtsK%2FTHAFoutAKFrSDxHeleX0VCmmzwMy9sPxF0NDNnMU%2FcLlyWleopNbA4WgakYeQIg3UgnYcP%2BedUke%2FXConY8t3qU0d3trFh9mNWMxrOoZjMD4SbqFgTcwJLyAIuMxVDJ00Ins63oeDP5qAV%2Bp%2F4iRfXLasnJAjTYFFgNFP1ixruDxsIMlkFYyo7%2FJYuIIzHdVmTv4p%2FwGtNXBP1Ge3Esi6BAZMXJB%2FjQzRPIlxCheD0UJE7mVpi%2FBuEcwYqu1QyxJua1%2BX%2FqLUz79U5wzEu8wjO%2BMvQY6pgH%2F5P0uNgH3L2phVe%2B%2BIbKhwlltMlj9pF71Qum2eWHx1mR4RuZA5NJ9j8IHb09fmdxapnuq4c0jNDVhaPPZXfbNmIa3KHcFxOCaIA6ow5ZydRbS2NUcM4zh9%2BiEGftvsByeOpBaT0MKlaN%2Fa6xkoXFBOh2IlnmQB1w8NbVb0YDQv%2FsD2XRt96esUNbd%2F0LnH3GRZTPIOkbLKHHfe1Ju3jQEZH5%2Bpfe3&X-Amz-Signature=f1acc82ab799f473051e67e4ed9b807379cdcaea0126854a072bfa6afed02c79&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDRZS5QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCICpCPzMwL7mh7f8eaS3j%2B2NUH55sbggbA%2Fv6RfJkBMstAiBT3izGmBjCu57DmdTcCqSFaD27mg5RG4kFcckkIEamgyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMDsE9iKLwGvBiLWdhKtwDqli%2BLGVgZRdTvxfiOvnCL6jyGgZQEDZAunYHn%2FO6vMXGxU9Ue%2FguyqbzagdAzramgUhSx%2BSYp041h6sXNZgcGDfcrjgVjb6jJNoSztIPb6qAubpbUZshSSY1hk%2B53wBmiLcI2SeFOJBbBXSE624kCus5C%2FAd%2FxccZ2A42eJ6hzXHNskfYFExjX3xSdg33JpUxA8TZW8mM5581hHiDpG0VPm5MmcejRn14TJtkZ8Yw77ztNU2rBhA3hEuoQxLzcn%2FOkRljoNsWsgGA9C8sGdBkQ3pZDKT48iaS1ZzBsK6x%2BMG5Idn0aRr8Cd03HtgBnUX%2FmXFy4GjqhX%2Be%2FWmGvMrqT7be7H84h%2FGxBQmtsK%2FTHAFoutAKFrSDxHeleX0VCmmzwMy9sPxF0NDNnMU%2FcLlyWleopNbA4WgakYeQIg3UgnYcP%2BedUke%2FXConY8t3qU0d3trFh9mNWMxrOoZjMD4SbqFgTcwJLyAIuMxVDJ00Ins63oeDP5qAV%2Bp%2F4iRfXLasnJAjTYFFgNFP1ixruDxsIMlkFYyo7%2FJYuIIzHdVmTv4p%2FwGtNXBP1Ge3Esi6BAZMXJB%2FjQzRPIlxCheD0UJE7mVpi%2FBuEcwYqu1QyxJua1%2BX%2FqLUz79U5wzEu8wjO%2BMvQY6pgH%2F5P0uNgH3L2phVe%2B%2BIbKhwlltMlj9pF71Qum2eWHx1mR4RuZA5NJ9j8IHb09fmdxapnuq4c0jNDVhaPPZXfbNmIa3KHcFxOCaIA6ow5ZydRbS2NUcM4zh9%2BiEGftvsByeOpBaT0MKlaN%2Fa6xkoXFBOh2IlnmQB1w8NbVb0YDQv%2FsD2XRt96esUNbd%2F0LnH3GRZTPIOkbLKHHfe1Ju3jQEZH5%2Bpfe3&X-Amz-Signature=60c439e38761d0098d593ad303960a5590f431ab73ffc5fd9d3edcdf266c8963&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDRZS5QX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCICpCPzMwL7mh7f8eaS3j%2B2NUH55sbggbA%2Fv6RfJkBMstAiBT3izGmBjCu57DmdTcCqSFaD27mg5RG4kFcckkIEamgyr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMDsE9iKLwGvBiLWdhKtwDqli%2BLGVgZRdTvxfiOvnCL6jyGgZQEDZAunYHn%2FO6vMXGxU9Ue%2FguyqbzagdAzramgUhSx%2BSYp041h6sXNZgcGDfcrjgVjb6jJNoSztIPb6qAubpbUZshSSY1hk%2B53wBmiLcI2SeFOJBbBXSE624kCus5C%2FAd%2FxccZ2A42eJ6hzXHNskfYFExjX3xSdg33JpUxA8TZW8mM5581hHiDpG0VPm5MmcejRn14TJtkZ8Yw77ztNU2rBhA3hEuoQxLzcn%2FOkRljoNsWsgGA9C8sGdBkQ3pZDKT48iaS1ZzBsK6x%2BMG5Idn0aRr8Cd03HtgBnUX%2FmXFy4GjqhX%2Be%2FWmGvMrqT7be7H84h%2FGxBQmtsK%2FTHAFoutAKFrSDxHeleX0VCmmzwMy9sPxF0NDNnMU%2FcLlyWleopNbA4WgakYeQIg3UgnYcP%2BedUke%2FXConY8t3qU0d3trFh9mNWMxrOoZjMD4SbqFgTcwJLyAIuMxVDJ00Ins63oeDP5qAV%2Bp%2F4iRfXLasnJAjTYFFgNFP1ixruDxsIMlkFYyo7%2FJYuIIzHdVmTv4p%2FwGtNXBP1Ge3Esi6BAZMXJB%2FjQzRPIlxCheD0UJE7mVpi%2FBuEcwYqu1QyxJua1%2BX%2FqLUz79U5wzEu8wjO%2BMvQY6pgH%2F5P0uNgH3L2phVe%2B%2BIbKhwlltMlj9pF71Qum2eWHx1mR4RuZA5NJ9j8IHb09fmdxapnuq4c0jNDVhaPPZXfbNmIa3KHcFxOCaIA6ow5ZydRbS2NUcM4zh9%2BiEGftvsByeOpBaT0MKlaN%2Fa6xkoXFBOh2IlnmQB1w8NbVb0YDQv%2FsD2XRt96esUNbd%2F0LnH3GRZTPIOkbLKHHfe1Ju3jQEZH5%2Bpfe3&X-Amz-Signature=57f75170ba84db9d2e7d7c19647039dbff1b6e3852aed24ea3a0fe0d5feea48e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXGQJ57T%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQDB7gjp0gkXG1KaOithH%2Fht%2BvMrThhS5TzAh%2B0Pj672SAIhAL159SHVZiyfDCzjiHAANsfGr5ZG5xKBmELpEbgeDyrQKv8DCEMQABoMNjM3NDIzMTgzODA1IgwyiC9hO%2BIJ1WtJU9gq3ANy%2FyDHUte2IoeFCq1f2n%2BIpDKORQ91yDTNCdkxrRa%2FM8tgYlJo9XHNQ%2BlyG%2BGTjQgBS%2FDZFbgM7ktGLyVB9HqxWeLo%2BuD7M9T%2BiXIjtLqu7dm3CB05ZZphfzheQl5nOW3Ac%2ByahgLlvcO4HwVby5mVK12GpzKUWck8HH1FiCL4D7yf8rXJNRorgz78IC3fP%2BQBtBa5gnpTJaf7aQL6F2kxLAOCtm3T2toEpECjsqs%2F1IvcgmJmOnVRnKcz0aQdw9g6ghAOVkUDlHDIKD1CfWBRIzVaRgRtuWc5iO6AmHJjh9%2FCcCeIQ%2B0ouRsSRPMwPXfvtcZffkKJcECdguESiTH6Kna7cH1XPSC2ivku3D0qE50ItRfAbD%2BwMVtMlwbRcecOxZjwxlhoN6UtM%2Fg5dP9rfTXYL34S6teWlgTECjACCr%2BCFi6Hb3DLg6zuzq6C62E0LYGSOJenRc95YVBs%2BurAM0FPEFAa11J1sZZKEwR1iqfgD7E4pCGrcYeZcDx5aCmj3LnI27HYnyVzkgmOMFHUke7w7qdhJAjq1fzy8ig9ew3IFm%2B581q3BeJHe%2BdI1BY7ycLEYGcTf4%2BNA6GwO0XkpvuQ2D6QJS5DCi5I21h6FBIi%2B2jEzZKKGZpLJDC374y9BjqkAUdNLIHfBERSbUCyaaKoUkZOw5OJCV5OJ84n7gzQIrNCehWEE30qcjKwFM%2BONsQQGUeGPkGgX16kySgcPUrCwBP3YcWNf65l4OLWl3hTubLqiLovgKvVr7m3qOaJIhU%2FXiPXcPg18Kzrs9ZrOjW60hrx5Y4N8n6RHw78GElJYchkkMMzIeHhOMBB9Z8RLWLP%2B6zkO%2F502hieGyV4gd7Yeg60mCdP&X-Amz-Signature=0735756f7ab70b2b4f9341801aeb194b00dfa9f8829df18f50738aa371c3a7eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GWUXT7Z%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCn3ZB2OgU1YoEx2vz51kLLEQBxiiWHRQeX%2FB%2Ff3ffoeAIhAImgSZhZWrtPPf1oNoXE9g36zH9uolg163DzLASSy5v9Kv8DCEMQABoMNjM3NDIzMTgzODA1IgwX%2FKfnr3LIUHs6DWwq3AOp9O0Tf7gzF1%2Bv7I59N5VM486gk2oHXUb6LqsPgg51ctR3t0DPuTdHy3tG%2FLECt23Tt%2FsLji7x3ETzwVStnVMpcP6u%2FoqKYYIS9c6tYXOVGobQ%2FSxZ2%2F5iPrFJxdWTWCringdGL8zJfc36tDZTfG9HLcyGpA1aOcVH5ZMPvQ6Cm7SEYTP8T%2BCxss07ZBkvvqPAmbGpAQ9ae%2BEnGWr9kknUJYO8OKZ7ZOkoq%2BdDIN7Ro6T8I8bkAEyWq1VOwDPXg74p%2BR4rqLteHu0uzd%2Fbn7AL8XbD%2BZzpyzSb28BlyIW7WVxvHbZnIa4FiNlPu4jVHmkqZTPbPFpR%2FEaY9vJ6Yc7JwQkkOmeiyWD4yjwTeT9hiolMx%2BFd78SitmWFyMI%2FAtv4hnZiQPZj3iuLonHTPMlDb1OFvWI5aucIrDJUY5JRjKoDS12DnjlRRJdOtO98JA8jXuWTsCrCe0O0EUBVxxQKXzVYwc9kBdgxchoJ5kQKVLaEpH7QU%2BIoy8%2F7BSVRkhxWFPpEKQwQhv%2FWx0fWlnlx%2FVGuiGNDmG5aQuMCjyjhrDzah145WFqXgzquBHQSHA3efkHLIf2t1u3GnVce2%2FOCaruz8pAAnGyIG3EMwRyr8vvVd5RTBmjSdCpttDCX74y9BjqkATCtM6UXE8aRxVvX3r7KC5rZp3TaHaPTT1fykgRzuXoI5bBD%2BdB8TSbA9eWb5y0LLXccrldZtsO5ONFsUcDk8QsO6MJmWk4PM1JtgWZ%2B5SYVdPbOXilNC6XuS6TiaJfKIG8wVYiZdw%2Bg3RWtElHbjm9fu82MvJf2Ghawfhp7%2FBQenxeDH42aHKoEkfls3R1Fe5f3PLlzNvzRx1iBIQP5fUHp858Q&X-Amz-Signature=0ae2fcfec27c03d259638c62b329f1ab9f6532ee68c6e6e3d7cfb7846fe4f638&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HXFSMXN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIC2beGdpByhMmLeAAxyayCbrfgqNyavSyx1TaV6Dtr5YAiEAtHdzPBTogqDmoMcs01zSknLHGglr898RvM9fRT9bptIq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKMfI%2BfCTX5VPiFPMircAzw%2FVQ3LVktIgwBZ9Wfm0QUaDDzk72ZaIwD4dlEq8KQqyG5WOjAMUvTbC3FSHcLCXxD9SbvuMi62mG%2BnAEuM1ZpuQ45YfNzIk2UcO9P2CX%2Fxgm88yRFu1y2x9NE%2B%2FUlvmbrYRhnz3XVmbDjurEFWHeqfCZGvHGLG%2F%2B9xNbU%2Bs%2Bj0cTZTsDO3l54sJjRqauzpUD9Qzphp7JdskBUJM3BMIRBBO0i7nfIOchgNfawGchxeSNbRSXyNEkCvDxtBNo%2Fk%2FGwFNeb9LGGrvrzlkztfSYmHQcmO%2FCwxM85yYsVBHPRQli2mvlX5DneNAeguCh2HOcEarpmVwbuNN7lpO8TavpsiaPAYXpdmuKLQqHOoZjmRIoo534yrifUswaAfDqUg0Xvl%2B7vTPFaUFK%2B2se%2B%2Bn0NM3BKBqdcFF06kXqgnglE%2Bpa8HI8iFxo57rPJR0jR93C2ThU3NnqwGIuiczRL4z%2F5bd8AakusMcekyH8bhep9Tg%2FcLYp4XnWLbPnBQlH1rW%2BBvLb9qdMUPAz3CDvBTRYDydb9E06Rd7j2DtFGOMYvCJ8mAuUnIjxNR1g%2B8TJ1D72GOhdaRJUdAW8%2B%2FRNKcY4NTD2NbNKKSHiWpiqK93Y8Vp1z1PIUmPkfiyGkHMKPvjL0GOqUBEHqvDbqAHTwTYhhgAujGnKv9i7bRLCKenEqxTaXuN7yJ%2FHhG7Aiatcb%2BuidkLaYI0fshX0Ja7gNN8ZpFABWbSnihHWIHG2Izk7S4BxK4ZUvc6co7s6PSzF9JHXlStQ3s9KgzBx0K9DqDKSvtC2K9VtbJSv62zoCuSEKrYC8AsIEfoC8f3dGawXgLKwAGpLjx7ZKorBJTDp2VGiqIpPpu2jDZINDx&X-Amz-Signature=f63278b9fac32eec6ee81229d2d67d49ef8fcde5b450a622a8415224af90fe0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HXFSMXN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIC2beGdpByhMmLeAAxyayCbrfgqNyavSyx1TaV6Dtr5YAiEAtHdzPBTogqDmoMcs01zSknLHGglr898RvM9fRT9bptIq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKMfI%2BfCTX5VPiFPMircAzw%2FVQ3LVktIgwBZ9Wfm0QUaDDzk72ZaIwD4dlEq8KQqyG5WOjAMUvTbC3FSHcLCXxD9SbvuMi62mG%2BnAEuM1ZpuQ45YfNzIk2UcO9P2CX%2Fxgm88yRFu1y2x9NE%2B%2FUlvmbrYRhnz3XVmbDjurEFWHeqfCZGvHGLG%2F%2B9xNbU%2Bs%2Bj0cTZTsDO3l54sJjRqauzpUD9Qzphp7JdskBUJM3BMIRBBO0i7nfIOchgNfawGchxeSNbRSXyNEkCvDxtBNo%2Fk%2FGwFNeb9LGGrvrzlkztfSYmHQcmO%2FCwxM85yYsVBHPRQli2mvlX5DneNAeguCh2HOcEarpmVwbuNN7lpO8TavpsiaPAYXpdmuKLQqHOoZjmRIoo534yrifUswaAfDqUg0Xvl%2B7vTPFaUFK%2B2se%2B%2Bn0NM3BKBqdcFF06kXqgnglE%2Bpa8HI8iFxo57rPJR0jR93C2ThU3NnqwGIuiczRL4z%2F5bd8AakusMcekyH8bhep9Tg%2FcLYp4XnWLbPnBQlH1rW%2BBvLb9qdMUPAz3CDvBTRYDydb9E06Rd7j2DtFGOMYvCJ8mAuUnIjxNR1g%2B8TJ1D72GOhdaRJUdAW8%2B%2FRNKcY4NTD2NbNKKSHiWpiqK93Y8Vp1z1PIUmPkfiyGkHMKPvjL0GOqUBEHqvDbqAHTwTYhhgAujGnKv9i7bRLCKenEqxTaXuN7yJ%2FHhG7Aiatcb%2BuidkLaYI0fshX0Ja7gNN8ZpFABWbSnihHWIHG2Izk7S4BxK4ZUvc6co7s6PSzF9JHXlStQ3s9KgzBx0K9DqDKSvtC2K9VtbJSv62zoCuSEKrYC8AsIEfoC8f3dGawXgLKwAGpLjx7ZKorBJTDp2VGiqIpPpu2jDZINDx&X-Amz-Signature=7ac93c8126f35d217c6eed33a69c6f818048a4691d7d98d95739e07508a5895c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
