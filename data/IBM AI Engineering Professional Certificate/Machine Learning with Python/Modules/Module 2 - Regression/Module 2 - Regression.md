

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVMM6SER%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCdS7UqB0d0XBFdKXdF47dPjeEqmngvZbYw8m30zLxJQgIhAOxSYIE2GX5HpbMUM86BPVSnScyv%2Bu2OefFDj1Mr7gSDKv8DCHkQABoMNjM3NDIzMTgzODA1IgyW22HtXVQEDQKTqfUq3ANAYVEIDk5fCQthzj8CDjxi7IrvXEA%2FibbWCz0j64eJD4hKcnaD00hncsSOGCgAWYLyNO6%2FdcJWwA5XBAbdRb3%2BjUEOHoLjTdIbQrJOYQqLh3%2By6QvldsC1NA3nWkEv%2Bg1JDfN3%2FeKA1MOzp5qFN7uFmmcwiAb3qy36S7p405pzZbxddfFUL1Hlw8V3QSCZRzFKIQvDHHnC%2BBPdf6kPLxTFhg7LPzpwTtQobX0Zfj2h4yQWBeoxHS6boZP5WvfC9cY4SRnHd5%2FR%2BGO6AdujYbl%2F2HINg95mtSJrnE4ebsBZR0C0i4CYhp0kbqFaU9NSt55qm8cbv%2BYLJNDHU4sNXIOAdQrgHrOJ%2Bc6mVY4bOx1ex9DdQ7t4ebiKqtaYPhK0pRevD7D9zV7RABPWL%2BaqwNDBEslsK%2Bc%2FZ9JSPsfEeSbq3jB6lyvD4w9BXhD4QhA3qHQk4DM3n37JEhWX2Pk6HLCqREKxeEXok6DfFRm0RP6t5ug2avZ9%2FuNUI2Whe4LMx5DMjVxf4HfHu%2FvqExi3e2Gcq2EDWhWXVRNhLp8ClVYQTbl9NLdf7N%2FkYMJ6BjoBfOtVlv2YoFoTf74EDPgDKb3BgG9upOU9e9Zs%2BPbK15rdR2B66AsWN2Wn22aYeTCw4Ji9BjqkAY2qfg5D3tR2MpYdb0j55oVjk3OzxFoLpdR4x2Mno8NBXWTTwgM0LKBmwR0lv05o%2B3ftd0BIyDFM5woZO2BJv%2BZwWoKqWuEmdzyqyV7UyUaN0cRJTiTqWg9Fu1XgBP8l49wZVET9o6QpMptMRcgwzCflany9DfyQy3S9WtQSVw7i5o%2FjwDEg9gQqdyF6vxYzji1XYt1PWCMpWngI1zQtJHKLt1C2&X-Amz-Signature=13bde3aa562a33cb8eaf93a1cddd24e6c7db768a9fe7a2723535165ed55acf09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVMM6SER%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCdS7UqB0d0XBFdKXdF47dPjeEqmngvZbYw8m30zLxJQgIhAOxSYIE2GX5HpbMUM86BPVSnScyv%2Bu2OefFDj1Mr7gSDKv8DCHkQABoMNjM3NDIzMTgzODA1IgyW22HtXVQEDQKTqfUq3ANAYVEIDk5fCQthzj8CDjxi7IrvXEA%2FibbWCz0j64eJD4hKcnaD00hncsSOGCgAWYLyNO6%2FdcJWwA5XBAbdRb3%2BjUEOHoLjTdIbQrJOYQqLh3%2By6QvldsC1NA3nWkEv%2Bg1JDfN3%2FeKA1MOzp5qFN7uFmmcwiAb3qy36S7p405pzZbxddfFUL1Hlw8V3QSCZRzFKIQvDHHnC%2BBPdf6kPLxTFhg7LPzpwTtQobX0Zfj2h4yQWBeoxHS6boZP5WvfC9cY4SRnHd5%2FR%2BGO6AdujYbl%2F2HINg95mtSJrnE4ebsBZR0C0i4CYhp0kbqFaU9NSt55qm8cbv%2BYLJNDHU4sNXIOAdQrgHrOJ%2Bc6mVY4bOx1ex9DdQ7t4ebiKqtaYPhK0pRevD7D9zV7RABPWL%2BaqwNDBEslsK%2Bc%2FZ9JSPsfEeSbq3jB6lyvD4w9BXhD4QhA3qHQk4DM3n37JEhWX2Pk6HLCqREKxeEXok6DfFRm0RP6t5ug2avZ9%2FuNUI2Whe4LMx5DMjVxf4HfHu%2FvqExi3e2Gcq2EDWhWXVRNhLp8ClVYQTbl9NLdf7N%2FkYMJ6BjoBfOtVlv2YoFoTf74EDPgDKb3BgG9upOU9e9Zs%2BPbK15rdR2B66AsWN2Wn22aYeTCw4Ji9BjqkAY2qfg5D3tR2MpYdb0j55oVjk3OzxFoLpdR4x2Mno8NBXWTTwgM0LKBmwR0lv05o%2B3ftd0BIyDFM5woZO2BJv%2BZwWoKqWuEmdzyqyV7UyUaN0cRJTiTqWg9Fu1XgBP8l49wZVET9o6QpMptMRcgwzCflany9DfyQy3S9WtQSVw7i5o%2FjwDEg9gQqdyF6vxYzji1XYt1PWCMpWngI1zQtJHKLt1C2&X-Amz-Signature=d35202ec4f20fd93191ebed502119d190c531cf0f1ed50741511dc7e77d8793d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVMM6SER%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCdS7UqB0d0XBFdKXdF47dPjeEqmngvZbYw8m30zLxJQgIhAOxSYIE2GX5HpbMUM86BPVSnScyv%2Bu2OefFDj1Mr7gSDKv8DCHkQABoMNjM3NDIzMTgzODA1IgyW22HtXVQEDQKTqfUq3ANAYVEIDk5fCQthzj8CDjxi7IrvXEA%2FibbWCz0j64eJD4hKcnaD00hncsSOGCgAWYLyNO6%2FdcJWwA5XBAbdRb3%2BjUEOHoLjTdIbQrJOYQqLh3%2By6QvldsC1NA3nWkEv%2Bg1JDfN3%2FeKA1MOzp5qFN7uFmmcwiAb3qy36S7p405pzZbxddfFUL1Hlw8V3QSCZRzFKIQvDHHnC%2BBPdf6kPLxTFhg7LPzpwTtQobX0Zfj2h4yQWBeoxHS6boZP5WvfC9cY4SRnHd5%2FR%2BGO6AdujYbl%2F2HINg95mtSJrnE4ebsBZR0C0i4CYhp0kbqFaU9NSt55qm8cbv%2BYLJNDHU4sNXIOAdQrgHrOJ%2Bc6mVY4bOx1ex9DdQ7t4ebiKqtaYPhK0pRevD7D9zV7RABPWL%2BaqwNDBEslsK%2Bc%2FZ9JSPsfEeSbq3jB6lyvD4w9BXhD4QhA3qHQk4DM3n37JEhWX2Pk6HLCqREKxeEXok6DfFRm0RP6t5ug2avZ9%2FuNUI2Whe4LMx5DMjVxf4HfHu%2FvqExi3e2Gcq2EDWhWXVRNhLp8ClVYQTbl9NLdf7N%2FkYMJ6BjoBfOtVlv2YoFoTf74EDPgDKb3BgG9upOU9e9Zs%2BPbK15rdR2B66AsWN2Wn22aYeTCw4Ji9BjqkAY2qfg5D3tR2MpYdb0j55oVjk3OzxFoLpdR4x2Mno8NBXWTTwgM0LKBmwR0lv05o%2B3ftd0BIyDFM5woZO2BJv%2BZwWoKqWuEmdzyqyV7UyUaN0cRJTiTqWg9Fu1XgBP8l49wZVET9o6QpMptMRcgwzCflany9DfyQy3S9WtQSVw7i5o%2FjwDEg9gQqdyF6vxYzji1XYt1PWCMpWngI1zQtJHKLt1C2&X-Amz-Signature=5d7e7854f4413831ff94d6e681f0b635efdc20cb400884cd5392a52bd665b168&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVMM6SER%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCdS7UqB0d0XBFdKXdF47dPjeEqmngvZbYw8m30zLxJQgIhAOxSYIE2GX5HpbMUM86BPVSnScyv%2Bu2OefFDj1Mr7gSDKv8DCHkQABoMNjM3NDIzMTgzODA1IgyW22HtXVQEDQKTqfUq3ANAYVEIDk5fCQthzj8CDjxi7IrvXEA%2FibbWCz0j64eJD4hKcnaD00hncsSOGCgAWYLyNO6%2FdcJWwA5XBAbdRb3%2BjUEOHoLjTdIbQrJOYQqLh3%2By6QvldsC1NA3nWkEv%2Bg1JDfN3%2FeKA1MOzp5qFN7uFmmcwiAb3qy36S7p405pzZbxddfFUL1Hlw8V3QSCZRzFKIQvDHHnC%2BBPdf6kPLxTFhg7LPzpwTtQobX0Zfj2h4yQWBeoxHS6boZP5WvfC9cY4SRnHd5%2FR%2BGO6AdujYbl%2F2HINg95mtSJrnE4ebsBZR0C0i4CYhp0kbqFaU9NSt55qm8cbv%2BYLJNDHU4sNXIOAdQrgHrOJ%2Bc6mVY4bOx1ex9DdQ7t4ebiKqtaYPhK0pRevD7D9zV7RABPWL%2BaqwNDBEslsK%2Bc%2FZ9JSPsfEeSbq3jB6lyvD4w9BXhD4QhA3qHQk4DM3n37JEhWX2Pk6HLCqREKxeEXok6DfFRm0RP6t5ug2avZ9%2FuNUI2Whe4LMx5DMjVxf4HfHu%2FvqExi3e2Gcq2EDWhWXVRNhLp8ClVYQTbl9NLdf7N%2FkYMJ6BjoBfOtVlv2YoFoTf74EDPgDKb3BgG9upOU9e9Zs%2BPbK15rdR2B66AsWN2Wn22aYeTCw4Ji9BjqkAY2qfg5D3tR2MpYdb0j55oVjk3OzxFoLpdR4x2Mno8NBXWTTwgM0LKBmwR0lv05o%2B3ftd0BIyDFM5woZO2BJv%2BZwWoKqWuEmdzyqyV7UyUaN0cRJTiTqWg9Fu1XgBP8l49wZVET9o6QpMptMRcgwzCflany9DfyQy3S9WtQSVw7i5o%2FjwDEg9gQqdyF6vxYzji1XYt1PWCMpWngI1zQtJHKLt1C2&X-Amz-Signature=65f9e12d4e711a2f8dc8fea0a9625b0222dea0a9afa6af564902459d3c3d819b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVMM6SER%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCdS7UqB0d0XBFdKXdF47dPjeEqmngvZbYw8m30zLxJQgIhAOxSYIE2GX5HpbMUM86BPVSnScyv%2Bu2OefFDj1Mr7gSDKv8DCHkQABoMNjM3NDIzMTgzODA1IgyW22HtXVQEDQKTqfUq3ANAYVEIDk5fCQthzj8CDjxi7IrvXEA%2FibbWCz0j64eJD4hKcnaD00hncsSOGCgAWYLyNO6%2FdcJWwA5XBAbdRb3%2BjUEOHoLjTdIbQrJOYQqLh3%2By6QvldsC1NA3nWkEv%2Bg1JDfN3%2FeKA1MOzp5qFN7uFmmcwiAb3qy36S7p405pzZbxddfFUL1Hlw8V3QSCZRzFKIQvDHHnC%2BBPdf6kPLxTFhg7LPzpwTtQobX0Zfj2h4yQWBeoxHS6boZP5WvfC9cY4SRnHd5%2FR%2BGO6AdujYbl%2F2HINg95mtSJrnE4ebsBZR0C0i4CYhp0kbqFaU9NSt55qm8cbv%2BYLJNDHU4sNXIOAdQrgHrOJ%2Bc6mVY4bOx1ex9DdQ7t4ebiKqtaYPhK0pRevD7D9zV7RABPWL%2BaqwNDBEslsK%2Bc%2FZ9JSPsfEeSbq3jB6lyvD4w9BXhD4QhA3qHQk4DM3n37JEhWX2Pk6HLCqREKxeEXok6DfFRm0RP6t5ug2avZ9%2FuNUI2Whe4LMx5DMjVxf4HfHu%2FvqExi3e2Gcq2EDWhWXVRNhLp8ClVYQTbl9NLdf7N%2FkYMJ6BjoBfOtVlv2YoFoTf74EDPgDKb3BgG9upOU9e9Zs%2BPbK15rdR2B66AsWN2Wn22aYeTCw4Ji9BjqkAY2qfg5D3tR2MpYdb0j55oVjk3OzxFoLpdR4x2Mno8NBXWTTwgM0LKBmwR0lv05o%2B3ftd0BIyDFM5woZO2BJv%2BZwWoKqWuEmdzyqyV7UyUaN0cRJTiTqWg9Fu1XgBP8l49wZVET9o6QpMptMRcgwzCflany9DfyQy3S9WtQSVw7i5o%2FjwDEg9gQqdyF6vxYzji1XYt1PWCMpWngI1zQtJHKLt1C2&X-Amz-Signature=f0e7b8277b0c120341e9c0aa64ad05d0d4dd1a658e0156f8beba6a5028128349&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVMM6SER%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCdS7UqB0d0XBFdKXdF47dPjeEqmngvZbYw8m30zLxJQgIhAOxSYIE2GX5HpbMUM86BPVSnScyv%2Bu2OefFDj1Mr7gSDKv8DCHkQABoMNjM3NDIzMTgzODA1IgyW22HtXVQEDQKTqfUq3ANAYVEIDk5fCQthzj8CDjxi7IrvXEA%2FibbWCz0j64eJD4hKcnaD00hncsSOGCgAWYLyNO6%2FdcJWwA5XBAbdRb3%2BjUEOHoLjTdIbQrJOYQqLh3%2By6QvldsC1NA3nWkEv%2Bg1JDfN3%2FeKA1MOzp5qFN7uFmmcwiAb3qy36S7p405pzZbxddfFUL1Hlw8V3QSCZRzFKIQvDHHnC%2BBPdf6kPLxTFhg7LPzpwTtQobX0Zfj2h4yQWBeoxHS6boZP5WvfC9cY4SRnHd5%2FR%2BGO6AdujYbl%2F2HINg95mtSJrnE4ebsBZR0C0i4CYhp0kbqFaU9NSt55qm8cbv%2BYLJNDHU4sNXIOAdQrgHrOJ%2Bc6mVY4bOx1ex9DdQ7t4ebiKqtaYPhK0pRevD7D9zV7RABPWL%2BaqwNDBEslsK%2Bc%2FZ9JSPsfEeSbq3jB6lyvD4w9BXhD4QhA3qHQk4DM3n37JEhWX2Pk6HLCqREKxeEXok6DfFRm0RP6t5ug2avZ9%2FuNUI2Whe4LMx5DMjVxf4HfHu%2FvqExi3e2Gcq2EDWhWXVRNhLp8ClVYQTbl9NLdf7N%2FkYMJ6BjoBfOtVlv2YoFoTf74EDPgDKb3BgG9upOU9e9Zs%2BPbK15rdR2B66AsWN2Wn22aYeTCw4Ji9BjqkAY2qfg5D3tR2MpYdb0j55oVjk3OzxFoLpdR4x2Mno8NBXWTTwgM0LKBmwR0lv05o%2B3ftd0BIyDFM5woZO2BJv%2BZwWoKqWuEmdzyqyV7UyUaN0cRJTiTqWg9Fu1XgBP8l49wZVET9o6QpMptMRcgwzCflany9DfyQy3S9WtQSVw7i5o%2FjwDEg9gQqdyF6vxYzji1XYt1PWCMpWngI1zQtJHKLt1C2&X-Amz-Signature=45a1a5219e928d8df6cc10a883ce72de63bb91e0d7c7134dcacd4f255dd13ea9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVMM6SER%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCdS7UqB0d0XBFdKXdF47dPjeEqmngvZbYw8m30zLxJQgIhAOxSYIE2GX5HpbMUM86BPVSnScyv%2Bu2OefFDj1Mr7gSDKv8DCHkQABoMNjM3NDIzMTgzODA1IgyW22HtXVQEDQKTqfUq3ANAYVEIDk5fCQthzj8CDjxi7IrvXEA%2FibbWCz0j64eJD4hKcnaD00hncsSOGCgAWYLyNO6%2FdcJWwA5XBAbdRb3%2BjUEOHoLjTdIbQrJOYQqLh3%2By6QvldsC1NA3nWkEv%2Bg1JDfN3%2FeKA1MOzp5qFN7uFmmcwiAb3qy36S7p405pzZbxddfFUL1Hlw8V3QSCZRzFKIQvDHHnC%2BBPdf6kPLxTFhg7LPzpwTtQobX0Zfj2h4yQWBeoxHS6boZP5WvfC9cY4SRnHd5%2FR%2BGO6AdujYbl%2F2HINg95mtSJrnE4ebsBZR0C0i4CYhp0kbqFaU9NSt55qm8cbv%2BYLJNDHU4sNXIOAdQrgHrOJ%2Bc6mVY4bOx1ex9DdQ7t4ebiKqtaYPhK0pRevD7D9zV7RABPWL%2BaqwNDBEslsK%2Bc%2FZ9JSPsfEeSbq3jB6lyvD4w9BXhD4QhA3qHQk4DM3n37JEhWX2Pk6HLCqREKxeEXok6DfFRm0RP6t5ug2avZ9%2FuNUI2Whe4LMx5DMjVxf4HfHu%2FvqExi3e2Gcq2EDWhWXVRNhLp8ClVYQTbl9NLdf7N%2FkYMJ6BjoBfOtVlv2YoFoTf74EDPgDKb3BgG9upOU9e9Zs%2BPbK15rdR2B66AsWN2Wn22aYeTCw4Ji9BjqkAY2qfg5D3tR2MpYdb0j55oVjk3OzxFoLpdR4x2Mno8NBXWTTwgM0LKBmwR0lv05o%2B3ftd0BIyDFM5woZO2BJv%2BZwWoKqWuEmdzyqyV7UyUaN0cRJTiTqWg9Fu1XgBP8l49wZVET9o6QpMptMRcgwzCflany9DfyQy3S9WtQSVw7i5o%2FjwDEg9gQqdyF6vxYzji1XYt1PWCMpWngI1zQtJHKLt1C2&X-Amz-Signature=8fd1c134523405e8c609f373a159935cd6ffb94b8645036e651b0f027a64c227&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVMM6SER%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQCdS7UqB0d0XBFdKXdF47dPjeEqmngvZbYw8m30zLxJQgIhAOxSYIE2GX5HpbMUM86BPVSnScyv%2Bu2OefFDj1Mr7gSDKv8DCHkQABoMNjM3NDIzMTgzODA1IgyW22HtXVQEDQKTqfUq3ANAYVEIDk5fCQthzj8CDjxi7IrvXEA%2FibbWCz0j64eJD4hKcnaD00hncsSOGCgAWYLyNO6%2FdcJWwA5XBAbdRb3%2BjUEOHoLjTdIbQrJOYQqLh3%2By6QvldsC1NA3nWkEv%2Bg1JDfN3%2FeKA1MOzp5qFN7uFmmcwiAb3qy36S7p405pzZbxddfFUL1Hlw8V3QSCZRzFKIQvDHHnC%2BBPdf6kPLxTFhg7LPzpwTtQobX0Zfj2h4yQWBeoxHS6boZP5WvfC9cY4SRnHd5%2FR%2BGO6AdujYbl%2F2HINg95mtSJrnE4ebsBZR0C0i4CYhp0kbqFaU9NSt55qm8cbv%2BYLJNDHU4sNXIOAdQrgHrOJ%2Bc6mVY4bOx1ex9DdQ7t4ebiKqtaYPhK0pRevD7D9zV7RABPWL%2BaqwNDBEslsK%2Bc%2FZ9JSPsfEeSbq3jB6lyvD4w9BXhD4QhA3qHQk4DM3n37JEhWX2Pk6HLCqREKxeEXok6DfFRm0RP6t5ug2avZ9%2FuNUI2Whe4LMx5DMjVxf4HfHu%2FvqExi3e2Gcq2EDWhWXVRNhLp8ClVYQTbl9NLdf7N%2FkYMJ6BjoBfOtVlv2YoFoTf74EDPgDKb3BgG9upOU9e9Zs%2BPbK15rdR2B66AsWN2Wn22aYeTCw4Ji9BjqkAY2qfg5D3tR2MpYdb0j55oVjk3OzxFoLpdR4x2Mno8NBXWTTwgM0LKBmwR0lv05o%2B3ftd0BIyDFM5woZO2BJv%2BZwWoKqWuEmdzyqyV7UyUaN0cRJTiTqWg9Fu1XgBP8l49wZVET9o6QpMptMRcgwzCflany9DfyQy3S9WtQSVw7i5o%2FjwDEg9gQqdyF6vxYzji1XYt1PWCMpWngI1zQtJHKLt1C2&X-Amz-Signature=a4320f91b427dfcd891405d60493a041b57667c08c56121fb4b9103f03c6507a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VD7R3HU7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIEolX05fvLkC2Txt%2FgmhrTUSIF8%2B2MvKAgK4%2B7v%2B2EU6AiAcmcfgCalCZoY%2BxlA6knKOatkus30Z1EHGYkUa6Da27Sr%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIM2swRCFbLkGH2%2BZNhKtwD05skv29WoDTSoea35Vp%2FDT1NXJIz4%2BMRU6C1%2FBaoplIQgbN9lYzkp3o8mbjldgu5LQt%2FXZTlgaLVB6Lf1OtnD399%2BsaJHV0ZllO5EEHVHYhKh5CsHmAzO9ZmhQiZUu6S54PV2QVo%2FSXAdMOXUn9OlijGqhLYRT0e5CRzEk45G5VIytXDIoPZrnA%2BlJJIWde1ki7PeDfVqRRidRcJ3ME4Src9m9CAnDIVD9POq7C5RPyUg8SSpjBGELFzZEPBbCODfLrJ3dkq652XAyEfFfEX37CUROCOJ1hjSjEM86IJgLpPhh381ViI%2FCH4SVd%2BH98jGSe8MBcRPfLvcvZw%2FjAqY1y5sZOpg4ZNqfjzyUXFuM%2B6xnLVM8iGo61PNFRX2K8qi1TThrxpIEt3GIJ2lJbH0O7tLFDdZmmGN1zcsfDt76nEW4AQ3KBm3xIfpxpNDlNY0guIhOma4zEMJB3Dqpkvqid6mft0kivv5vUukPsy2zDLtU%2B2Tn72CB5rlwOLUM7DlYZ%2FILVybRrxxIj%2BTqHmTZwQYbbKBgctmw2lqYjOIuIc9OoLP6gXx8dbzbrEKdp5XDZ39eBllzVLWZl7HyrfZYof9d%2FzyZqdjzt4xtWtZkrGaWfjodUOJy4i7yAwseCYvQY6pgH9LCdoWH%2FyVQJ9QzcJtt2L%2BR7eSJqDS3eEqyIM0x6XYMHKPgKaifr7zIrALxE7YWRZPScKL2M1gU3JjOXJOSqUY%2BJnGJyow9dirIxXNSbsxqPPu3G1ntzqMCf%2Fyi016EwKEsoH7KKrKYk%2BGHuhTVX4T6TEWk8SgArvxokC5e26KZ3%2FveFVFmAlrEKzKNHO3GedaAZONpJ4UgCjpjGovLeiaMI5JeO5&X-Amz-Signature=1e69947bf7c924e3d5d5586abc25996b5fac61dbb3ba52d1888456460300c0c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXLQ2TMX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQClfUadPikOe2%2FGjZAKkJ3oJk2VIO6jWpE734ocz3ArXAIgT751ouk0qk%2BvcC8bgqSmKlhYNr15hOVPyQ9lL2aKCPUq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDMHOQ3yRrglDwveJPCrcAzHy25s5XhQY01odfz4Uc0pMSNNknG1jJ6wgsckvk6%2FzA03XLQ8EVQ%2FY40WyJ2JaGDVuGikj6%2F9uPrmPR%2FwTkBJEqGgGacIrDUcRsO9orftF3smtuo0IS0B%2FvX9CKGkqRDStxISenPM%2B8xh9MbO5oDpNgm2Me88WPTvflJT1YnrFpQh53n3TlHcW7uhAIPkMR4NY4T1KwI9mcrfjjooYbp%2FbpnXHrLpjz1IS3tir9AjMGAFsg%2BWv0h1uR%2FD7jcGJL4pdS63Amc4UwKP%2FWdlpRAkhrpsJaVrxuaTNzwU4PVn%2BdDQJlyW%2BQXRlgHPbS%2F%2Bqe11GCB6zi8Z0AdOOqW0UYcQWhDxHkzMBHH7dNKZI4TRZu8L5qV%2FEcyNA2tV8zUgbdDAsh4tCBUnhmfCSxVQTbw0maIpUslCXrDPEYsJ0XQq2b6X7cOl%2BbHZdEdWYjJvaHpfohysVxMWbhH%2BUvjOhuzB962PNTnukfXMFMl8p6FsPicx0AiwuViW5B%2FcDJDrdYqG58YxQYoCqzkkh2xcoQMRcqoqLB466RJcZxebXsaQinJSI%2BsXGqOUWVgbQ4IH8MvGL5WQrT%2FcBQgMSGQ%2BOzeVUQJyIDac5cQgrejYWTGiOOy5DuW5ximaUsS15MKjgmL0GOqUBmkOKNDlwMsPBYwVOqwXSSE3h%2BKQKqjHDnx%2Bba3SJkKu10ePR%2B4Oht%2Fgi%2BiuUa6BodYRUOG93jF2XLGx2gwuWc1m3LTKnCH2RG7MrjMF8T5rYkAktWGSMCzCgv5NOmiAdh3jJRrqiYDg%2BP8Ph9ycF%2BDPuiH3CH%2BMu9vn72kSG1ZmouhMGZfw7M2t2YHvAskqjg80HvWtPxQtxF3kVJn5elsCVEUYJ&X-Amz-Signature=1bf3885bd471e3b47dc6b2b0af0f3a97b25e6bc5f34ec0d141db1a7a8cb4a9bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMKKRN3H%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIFjL7%2FzohKTgtOLJPukM4QHUq%2BvjnV8fhYx3vbcyoy7iAiBRkkdbA%2FucH77zZRovZfysQQEk9CmQYoJuWnXXm9XVayr%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMFB5gYa5ZoS4xNw1wKtwDPKTr0VkPPspBitGx3%2FZ4kq5ulvKT7Mgr4k9BwgwjLGYyYONTUtsewGQpUxkocRwT%2BKZNrqT4D4%2BtLl3E6DMKO7u4%2FSkqX%2BLX%2B6gWmL2Y5jwFKgAxlkuDxw7x1dHKZ0iATbrsWycOyZehWLKIFceXyzzyUU0Ui7Tumhid1YefYcevpWBRQ8dSKpyoQCt5thkuF4U8q6LjMVwlLctwUSWXk6tzHsmqt6Ey%2Bt0AKQ4YSkSMQZzPbHxaZ6H0tdSq%2FfEhco6C032%2BBaXZ4L3XI441vAzgrejQYPXIUbwF8jKIAwpxZLKra9HajkKGbtCaVn8q1RFYIeTinIUkLygBc3DmDtQ9rlr2iG8Fu2nWzfCtLd3Kj%2FVE%2FfpqWMd3eWOofpjbmMXEcamI27KWJQu8FWyR89CPu7LWgPto1aGsp%2BYLX23IMqYUgh%2B5iBZa%2FiXqcE%2BV9s5kfvHrhVRWp4cotF1QwX7iSzVHWZWJQ7go%2BcXBTO0VxWoyVpZ4jgoPD3b729bBo3inSpyiOQpUiqkw7Mzn7wYcMLk2DqC%2BURZeySlh4y3guav46MHG94BJUbZhFT9Bxx1qi7r1%2BuQsntKrtSxoiaoqATTPUjiTC5z%2F5A%2FV0IDZyy5AHuTd4ciTciYwpuCYvQY6pgEMhsseT%2BCJiMAwZgPEpDZ2VlAB%2BDyujnOhYX%2BbbIzXH70BJAaHoxLicrgWOs6Cbxf4HwrHdhRb6%2FB553PJdm4yNmyB6l5qpPnjOEdTf4V2CgLrrR89Gs9Mx%2BY7VQP5PGW0benewkhz7Kx%2FMyIL2v0d4B0FBFrz2IiMye3NoZCVN9cgyij0x6yrOJsbClXBX1v1yv9ll0%2B8JLpJCHVS9vYzJmCP64ws&X-Amz-Signature=b54fa7227c9b1286be4eb30435dabbc906251385d44c02958ebcad86e0d330df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMKKRN3H%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIFjL7%2FzohKTgtOLJPukM4QHUq%2BvjnV8fhYx3vbcyoy7iAiBRkkdbA%2FucH77zZRovZfysQQEk9CmQYoJuWnXXm9XVayr%2FAwh5EAAaDDYzNzQyMzE4MzgwNSIMFB5gYa5ZoS4xNw1wKtwDPKTr0VkPPspBitGx3%2FZ4kq5ulvKT7Mgr4k9BwgwjLGYyYONTUtsewGQpUxkocRwT%2BKZNrqT4D4%2BtLl3E6DMKO7u4%2FSkqX%2BLX%2B6gWmL2Y5jwFKgAxlkuDxw7x1dHKZ0iATbrsWycOyZehWLKIFceXyzzyUU0Ui7Tumhid1YefYcevpWBRQ8dSKpyoQCt5thkuF4U8q6LjMVwlLctwUSWXk6tzHsmqt6Ey%2Bt0AKQ4YSkSMQZzPbHxaZ6H0tdSq%2FfEhco6C032%2BBaXZ4L3XI441vAzgrejQYPXIUbwF8jKIAwpxZLKra9HajkKGbtCaVn8q1RFYIeTinIUkLygBc3DmDtQ9rlr2iG8Fu2nWzfCtLd3Kj%2FVE%2FfpqWMd3eWOofpjbmMXEcamI27KWJQu8FWyR89CPu7LWgPto1aGsp%2BYLX23IMqYUgh%2B5iBZa%2FiXqcE%2BV9s5kfvHrhVRWp4cotF1QwX7iSzVHWZWJQ7go%2BcXBTO0VxWoyVpZ4jgoPD3b729bBo3inSpyiOQpUiqkw7Mzn7wYcMLk2DqC%2BURZeySlh4y3guav46MHG94BJUbZhFT9Bxx1qi7r1%2BuQsntKrtSxoiaoqATTPUjiTC5z%2F5A%2FV0IDZyy5AHuTd4ciTciYwpuCYvQY6pgEMhsseT%2BCJiMAwZgPEpDZ2VlAB%2BDyujnOhYX%2BbbIzXH70BJAaHoxLicrgWOs6Cbxf4HwrHdhRb6%2FB553PJdm4yNmyB6l5qpPnjOEdTf4V2CgLrrR89Gs9Mx%2BY7VQP5PGW0benewkhz7Kx%2FMyIL2v0d4B0FBFrz2IiMye3NoZCVN9cgyij0x6yrOJsbClXBX1v1yv9ll0%2B8JLpJCHVS9vYzJmCP64ws&X-Amz-Signature=b6b6a4a9049292ef7f685064851d9a76c2fa4577890b54ac2702e5ccae186dc8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
