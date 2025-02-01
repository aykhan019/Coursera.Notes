

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGCYS6PY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTIjSJMPzPXIxqzqiJpzxwC73BFozqvgSePfuyvvh03AIhAPwRFsFODsY11isg87A%2FDqSjjx3kAHfuBtXHqThtqOt%2FKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyl2BiNoXLSFz2vJXMq3AP3XmaaAgYgIyFgpw%2F1zHB5L6ySSJO9hBFhL3sKFlaS9ZluLm1OzXJABHFxekDzUxekwQqklgpkGQ2LZE%2FKrIYwY9zCy1%2FlNXIQkjA39zIXKcFe%2F2NHr%2BLp9K1vZBDC8YXDyox%2F9qgqd19QWQU8dGnjNjSujs3dYqOeRJxnaw4owQQhCM%2FkcS32nJrLkPTn2nGjQXQDB0JkiLL3Ol1DcfVcgicBsmhAc5gUeqg%2Bh068JT99NJ%2BSQzQsSmd25bmKjDHcvfHboO%2B7IFt5oPK1w7Q864jsQtce31vfyeYXqrfUGqFbJy7XeF%2BynjBW%2FHIqnGunyDetJLnfn7UsMt0B1retT6nA7sYpv%2FkAk8WdaDZ1lt6s%2FuHnc7T2%2B4mPF1%2F5VChZaJtov5ROer305UwU%2FpaQTjyuXiXdfgyhcHkG6zTVFA3xCXce8KwUHjXX61IZWfoh%2BDbsWHoq5fowtG9qxqQRAJEm9wW7Spw6H8dTySEHAiQcLL8Cm8GhAy%2FYqmFpB%2FK0A6j3esteAEenzh8z%2BsGPg%2BG3sD%2BdDFIxwM4Co5h5Km7IlP4BJji13cOrZGm1n8UKQDcttluVQb6U4U5UIDK7jy21PL3B%2FmSHRUO5fKAxStsAxV3ePpuLouTb2TC2pPe8BjqkAYcQF3xGpTJOP7dWkx1etnzyPaxjz03VWLoJJEUhKZSHG8ejPzjZZ7DSx5kwCdIOIR6I56IOqxm6rEy5O%2F%2BFkFy6%2BE8Z0sF%2FG1%2FK16zs2NO3d%2BpXDb3oBmmQCafogJzt%2BY5LGB546xJvTavNpOXzcehwQMDOI9CkAwDibTG5F0rRDnObdwiCR1vUtKD8dg%2FteLyZGnaE0a%2B2XOgaumeE9GT5m0l7&X-Amz-Signature=93992e05b4bc3df566dc7d6e71d5721aee476b99406f1bac913e1772b1b59d84&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGCYS6PY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTIjSJMPzPXIxqzqiJpzxwC73BFozqvgSePfuyvvh03AIhAPwRFsFODsY11isg87A%2FDqSjjx3kAHfuBtXHqThtqOt%2FKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyl2BiNoXLSFz2vJXMq3AP3XmaaAgYgIyFgpw%2F1zHB5L6ySSJO9hBFhL3sKFlaS9ZluLm1OzXJABHFxekDzUxekwQqklgpkGQ2LZE%2FKrIYwY9zCy1%2FlNXIQkjA39zIXKcFe%2F2NHr%2BLp9K1vZBDC8YXDyox%2F9qgqd19QWQU8dGnjNjSujs3dYqOeRJxnaw4owQQhCM%2FkcS32nJrLkPTn2nGjQXQDB0JkiLL3Ol1DcfVcgicBsmhAc5gUeqg%2Bh068JT99NJ%2BSQzQsSmd25bmKjDHcvfHboO%2B7IFt5oPK1w7Q864jsQtce31vfyeYXqrfUGqFbJy7XeF%2BynjBW%2FHIqnGunyDetJLnfn7UsMt0B1retT6nA7sYpv%2FkAk8WdaDZ1lt6s%2FuHnc7T2%2B4mPF1%2F5VChZaJtov5ROer305UwU%2FpaQTjyuXiXdfgyhcHkG6zTVFA3xCXce8KwUHjXX61IZWfoh%2BDbsWHoq5fowtG9qxqQRAJEm9wW7Spw6H8dTySEHAiQcLL8Cm8GhAy%2FYqmFpB%2FK0A6j3esteAEenzh8z%2BsGPg%2BG3sD%2BdDFIxwM4Co5h5Km7IlP4BJji13cOrZGm1n8UKQDcttluVQb6U4U5UIDK7jy21PL3B%2FmSHRUO5fKAxStsAxV3ePpuLouTb2TC2pPe8BjqkAYcQF3xGpTJOP7dWkx1etnzyPaxjz03VWLoJJEUhKZSHG8ejPzjZZ7DSx5kwCdIOIR6I56IOqxm6rEy5O%2F%2BFkFy6%2BE8Z0sF%2FG1%2FK16zs2NO3d%2BpXDb3oBmmQCafogJzt%2BY5LGB546xJvTavNpOXzcehwQMDOI9CkAwDibTG5F0rRDnObdwiCR1vUtKD8dg%2FteLyZGnaE0a%2B2XOgaumeE9GT5m0l7&X-Amz-Signature=34fcb3c58cddae5875e08e769bd1cb197d11592d0f03db8d59eeda9fc5778893&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGCYS6PY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTIjSJMPzPXIxqzqiJpzxwC73BFozqvgSePfuyvvh03AIhAPwRFsFODsY11isg87A%2FDqSjjx3kAHfuBtXHqThtqOt%2FKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyl2BiNoXLSFz2vJXMq3AP3XmaaAgYgIyFgpw%2F1zHB5L6ySSJO9hBFhL3sKFlaS9ZluLm1OzXJABHFxekDzUxekwQqklgpkGQ2LZE%2FKrIYwY9zCy1%2FlNXIQkjA39zIXKcFe%2F2NHr%2BLp9K1vZBDC8YXDyox%2F9qgqd19QWQU8dGnjNjSujs3dYqOeRJxnaw4owQQhCM%2FkcS32nJrLkPTn2nGjQXQDB0JkiLL3Ol1DcfVcgicBsmhAc5gUeqg%2Bh068JT99NJ%2BSQzQsSmd25bmKjDHcvfHboO%2B7IFt5oPK1w7Q864jsQtce31vfyeYXqrfUGqFbJy7XeF%2BynjBW%2FHIqnGunyDetJLnfn7UsMt0B1retT6nA7sYpv%2FkAk8WdaDZ1lt6s%2FuHnc7T2%2B4mPF1%2F5VChZaJtov5ROer305UwU%2FpaQTjyuXiXdfgyhcHkG6zTVFA3xCXce8KwUHjXX61IZWfoh%2BDbsWHoq5fowtG9qxqQRAJEm9wW7Spw6H8dTySEHAiQcLL8Cm8GhAy%2FYqmFpB%2FK0A6j3esteAEenzh8z%2BsGPg%2BG3sD%2BdDFIxwM4Co5h5Km7IlP4BJji13cOrZGm1n8UKQDcttluVQb6U4U5UIDK7jy21PL3B%2FmSHRUO5fKAxStsAxV3ePpuLouTb2TC2pPe8BjqkAYcQF3xGpTJOP7dWkx1etnzyPaxjz03VWLoJJEUhKZSHG8ejPzjZZ7DSx5kwCdIOIR6I56IOqxm6rEy5O%2F%2BFkFy6%2BE8Z0sF%2FG1%2FK16zs2NO3d%2BpXDb3oBmmQCafogJzt%2BY5LGB546xJvTavNpOXzcehwQMDOI9CkAwDibTG5F0rRDnObdwiCR1vUtKD8dg%2FteLyZGnaE0a%2B2XOgaumeE9GT5m0l7&X-Amz-Signature=07fc8a5facac845c7f3324bcabdbc09c0e061fe0bca610da26ef8381289ab38e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGCYS6PY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTIjSJMPzPXIxqzqiJpzxwC73BFozqvgSePfuyvvh03AIhAPwRFsFODsY11isg87A%2FDqSjjx3kAHfuBtXHqThtqOt%2FKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyl2BiNoXLSFz2vJXMq3AP3XmaaAgYgIyFgpw%2F1zHB5L6ySSJO9hBFhL3sKFlaS9ZluLm1OzXJABHFxekDzUxekwQqklgpkGQ2LZE%2FKrIYwY9zCy1%2FlNXIQkjA39zIXKcFe%2F2NHr%2BLp9K1vZBDC8YXDyox%2F9qgqd19QWQU8dGnjNjSujs3dYqOeRJxnaw4owQQhCM%2FkcS32nJrLkPTn2nGjQXQDB0JkiLL3Ol1DcfVcgicBsmhAc5gUeqg%2Bh068JT99NJ%2BSQzQsSmd25bmKjDHcvfHboO%2B7IFt5oPK1w7Q864jsQtce31vfyeYXqrfUGqFbJy7XeF%2BynjBW%2FHIqnGunyDetJLnfn7UsMt0B1retT6nA7sYpv%2FkAk8WdaDZ1lt6s%2FuHnc7T2%2B4mPF1%2F5VChZaJtov5ROer305UwU%2FpaQTjyuXiXdfgyhcHkG6zTVFA3xCXce8KwUHjXX61IZWfoh%2BDbsWHoq5fowtG9qxqQRAJEm9wW7Spw6H8dTySEHAiQcLL8Cm8GhAy%2FYqmFpB%2FK0A6j3esteAEenzh8z%2BsGPg%2BG3sD%2BdDFIxwM4Co5h5Km7IlP4BJji13cOrZGm1n8UKQDcttluVQb6U4U5UIDK7jy21PL3B%2FmSHRUO5fKAxStsAxV3ePpuLouTb2TC2pPe8BjqkAYcQF3xGpTJOP7dWkx1etnzyPaxjz03VWLoJJEUhKZSHG8ejPzjZZ7DSx5kwCdIOIR6I56IOqxm6rEy5O%2F%2BFkFy6%2BE8Z0sF%2FG1%2FK16zs2NO3d%2BpXDb3oBmmQCafogJzt%2BY5LGB546xJvTavNpOXzcehwQMDOI9CkAwDibTG5F0rRDnObdwiCR1vUtKD8dg%2FteLyZGnaE0a%2B2XOgaumeE9GT5m0l7&X-Amz-Signature=fc0ae6ef9f616305c5758bc41534c3e6c0110a565a5cae9adcd0fdf309448600&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGCYS6PY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTIjSJMPzPXIxqzqiJpzxwC73BFozqvgSePfuyvvh03AIhAPwRFsFODsY11isg87A%2FDqSjjx3kAHfuBtXHqThtqOt%2FKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyl2BiNoXLSFz2vJXMq3AP3XmaaAgYgIyFgpw%2F1zHB5L6ySSJO9hBFhL3sKFlaS9ZluLm1OzXJABHFxekDzUxekwQqklgpkGQ2LZE%2FKrIYwY9zCy1%2FlNXIQkjA39zIXKcFe%2F2NHr%2BLp9K1vZBDC8YXDyox%2F9qgqd19QWQU8dGnjNjSujs3dYqOeRJxnaw4owQQhCM%2FkcS32nJrLkPTn2nGjQXQDB0JkiLL3Ol1DcfVcgicBsmhAc5gUeqg%2Bh068JT99NJ%2BSQzQsSmd25bmKjDHcvfHboO%2B7IFt5oPK1w7Q864jsQtce31vfyeYXqrfUGqFbJy7XeF%2BynjBW%2FHIqnGunyDetJLnfn7UsMt0B1retT6nA7sYpv%2FkAk8WdaDZ1lt6s%2FuHnc7T2%2B4mPF1%2F5VChZaJtov5ROer305UwU%2FpaQTjyuXiXdfgyhcHkG6zTVFA3xCXce8KwUHjXX61IZWfoh%2BDbsWHoq5fowtG9qxqQRAJEm9wW7Spw6H8dTySEHAiQcLL8Cm8GhAy%2FYqmFpB%2FK0A6j3esteAEenzh8z%2BsGPg%2BG3sD%2BdDFIxwM4Co5h5Km7IlP4BJji13cOrZGm1n8UKQDcttluVQb6U4U5UIDK7jy21PL3B%2FmSHRUO5fKAxStsAxV3ePpuLouTb2TC2pPe8BjqkAYcQF3xGpTJOP7dWkx1etnzyPaxjz03VWLoJJEUhKZSHG8ejPzjZZ7DSx5kwCdIOIR6I56IOqxm6rEy5O%2F%2BFkFy6%2BE8Z0sF%2FG1%2FK16zs2NO3d%2BpXDb3oBmmQCafogJzt%2BY5LGB546xJvTavNpOXzcehwQMDOI9CkAwDibTG5F0rRDnObdwiCR1vUtKD8dg%2FteLyZGnaE0a%2B2XOgaumeE9GT5m0l7&X-Amz-Signature=253ee64654fc1a43526686fb397329adb5a92a4d6005dad81a17931403b72a4f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGCYS6PY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTIjSJMPzPXIxqzqiJpzxwC73BFozqvgSePfuyvvh03AIhAPwRFsFODsY11isg87A%2FDqSjjx3kAHfuBtXHqThtqOt%2FKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyl2BiNoXLSFz2vJXMq3AP3XmaaAgYgIyFgpw%2F1zHB5L6ySSJO9hBFhL3sKFlaS9ZluLm1OzXJABHFxekDzUxekwQqklgpkGQ2LZE%2FKrIYwY9zCy1%2FlNXIQkjA39zIXKcFe%2F2NHr%2BLp9K1vZBDC8YXDyox%2F9qgqd19QWQU8dGnjNjSujs3dYqOeRJxnaw4owQQhCM%2FkcS32nJrLkPTn2nGjQXQDB0JkiLL3Ol1DcfVcgicBsmhAc5gUeqg%2Bh068JT99NJ%2BSQzQsSmd25bmKjDHcvfHboO%2B7IFt5oPK1w7Q864jsQtce31vfyeYXqrfUGqFbJy7XeF%2BynjBW%2FHIqnGunyDetJLnfn7UsMt0B1retT6nA7sYpv%2FkAk8WdaDZ1lt6s%2FuHnc7T2%2B4mPF1%2F5VChZaJtov5ROer305UwU%2FpaQTjyuXiXdfgyhcHkG6zTVFA3xCXce8KwUHjXX61IZWfoh%2BDbsWHoq5fowtG9qxqQRAJEm9wW7Spw6H8dTySEHAiQcLL8Cm8GhAy%2FYqmFpB%2FK0A6j3esteAEenzh8z%2BsGPg%2BG3sD%2BdDFIxwM4Co5h5Km7IlP4BJji13cOrZGm1n8UKQDcttluVQb6U4U5UIDK7jy21PL3B%2FmSHRUO5fKAxStsAxV3ePpuLouTb2TC2pPe8BjqkAYcQF3xGpTJOP7dWkx1etnzyPaxjz03VWLoJJEUhKZSHG8ejPzjZZ7DSx5kwCdIOIR6I56IOqxm6rEy5O%2F%2BFkFy6%2BE8Z0sF%2FG1%2FK16zs2NO3d%2BpXDb3oBmmQCafogJzt%2BY5LGB546xJvTavNpOXzcehwQMDOI9CkAwDibTG5F0rRDnObdwiCR1vUtKD8dg%2FteLyZGnaE0a%2B2XOgaumeE9GT5m0l7&X-Amz-Signature=32b1f596db9c3eac5d44da63951680087550c7d26f9af762ada3ad0717a44300&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGCYS6PY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTIjSJMPzPXIxqzqiJpzxwC73BFozqvgSePfuyvvh03AIhAPwRFsFODsY11isg87A%2FDqSjjx3kAHfuBtXHqThtqOt%2FKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyl2BiNoXLSFz2vJXMq3AP3XmaaAgYgIyFgpw%2F1zHB5L6ySSJO9hBFhL3sKFlaS9ZluLm1OzXJABHFxekDzUxekwQqklgpkGQ2LZE%2FKrIYwY9zCy1%2FlNXIQkjA39zIXKcFe%2F2NHr%2BLp9K1vZBDC8YXDyox%2F9qgqd19QWQU8dGnjNjSujs3dYqOeRJxnaw4owQQhCM%2FkcS32nJrLkPTn2nGjQXQDB0JkiLL3Ol1DcfVcgicBsmhAc5gUeqg%2Bh068JT99NJ%2BSQzQsSmd25bmKjDHcvfHboO%2B7IFt5oPK1w7Q864jsQtce31vfyeYXqrfUGqFbJy7XeF%2BynjBW%2FHIqnGunyDetJLnfn7UsMt0B1retT6nA7sYpv%2FkAk8WdaDZ1lt6s%2FuHnc7T2%2B4mPF1%2F5VChZaJtov5ROer305UwU%2FpaQTjyuXiXdfgyhcHkG6zTVFA3xCXce8KwUHjXX61IZWfoh%2BDbsWHoq5fowtG9qxqQRAJEm9wW7Spw6H8dTySEHAiQcLL8Cm8GhAy%2FYqmFpB%2FK0A6j3esteAEenzh8z%2BsGPg%2BG3sD%2BdDFIxwM4Co5h5Km7IlP4BJji13cOrZGm1n8UKQDcttluVQb6U4U5UIDK7jy21PL3B%2FmSHRUO5fKAxStsAxV3ePpuLouTb2TC2pPe8BjqkAYcQF3xGpTJOP7dWkx1etnzyPaxjz03VWLoJJEUhKZSHG8ejPzjZZ7DSx5kwCdIOIR6I56IOqxm6rEy5O%2F%2BFkFy6%2BE8Z0sF%2FG1%2FK16zs2NO3d%2BpXDb3oBmmQCafogJzt%2BY5LGB546xJvTavNpOXzcehwQMDOI9CkAwDibTG5F0rRDnObdwiCR1vUtKD8dg%2FteLyZGnaE0a%2B2XOgaumeE9GT5m0l7&X-Amz-Signature=37f79d538de64f7f65d7e8206001b34f7f260662a65c2b1c0c6baf7b2e07071b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGCYS6PY%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTIjSJMPzPXIxqzqiJpzxwC73BFozqvgSePfuyvvh03AIhAPwRFsFODsY11isg87A%2FDqSjjx3kAHfuBtXHqThtqOt%2FKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyl2BiNoXLSFz2vJXMq3AP3XmaaAgYgIyFgpw%2F1zHB5L6ySSJO9hBFhL3sKFlaS9ZluLm1OzXJABHFxekDzUxekwQqklgpkGQ2LZE%2FKrIYwY9zCy1%2FlNXIQkjA39zIXKcFe%2F2NHr%2BLp9K1vZBDC8YXDyox%2F9qgqd19QWQU8dGnjNjSujs3dYqOeRJxnaw4owQQhCM%2FkcS32nJrLkPTn2nGjQXQDB0JkiLL3Ol1DcfVcgicBsmhAc5gUeqg%2Bh068JT99NJ%2BSQzQsSmd25bmKjDHcvfHboO%2B7IFt5oPK1w7Q864jsQtce31vfyeYXqrfUGqFbJy7XeF%2BynjBW%2FHIqnGunyDetJLnfn7UsMt0B1retT6nA7sYpv%2FkAk8WdaDZ1lt6s%2FuHnc7T2%2B4mPF1%2F5VChZaJtov5ROer305UwU%2FpaQTjyuXiXdfgyhcHkG6zTVFA3xCXce8KwUHjXX61IZWfoh%2BDbsWHoq5fowtG9qxqQRAJEm9wW7Spw6H8dTySEHAiQcLL8Cm8GhAy%2FYqmFpB%2FK0A6j3esteAEenzh8z%2BsGPg%2BG3sD%2BdDFIxwM4Co5h5Km7IlP4BJji13cOrZGm1n8UKQDcttluVQb6U4U5UIDK7jy21PL3B%2FmSHRUO5fKAxStsAxV3ePpuLouTb2TC2pPe8BjqkAYcQF3xGpTJOP7dWkx1etnzyPaxjz03VWLoJJEUhKZSHG8ejPzjZZ7DSx5kwCdIOIR6I56IOqxm6rEy5O%2F%2BFkFy6%2BE8Z0sF%2FG1%2FK16zs2NO3d%2BpXDb3oBmmQCafogJzt%2BY5LGB546xJvTavNpOXzcehwQMDOI9CkAwDibTG5F0rRDnObdwiCR1vUtKD8dg%2FteLyZGnaE0a%2B2XOgaumeE9GT5m0l7&X-Amz-Signature=04ac631557cf7d673beaa1477a3374eb6d76080d9b28ab87ad628db9f52ae400&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMXBXT4C%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBalOdH2LnLxLp8Gxd18ME1mZfuXA1jAZNfYxho3HzvdAiAtOEH%2Fk76L6YaiAkq2jNMdgyi1Yt1Mom2r17tcJpvrQyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmiXYSMhUy35vn9aoKtwDuGc82eYgeuNqhDM8RIqOcuA7TwKuOSNPh9bYlvKdueJHexdwudO43QIL%2BqQ2whbRhwd4SjENeNFjRYJmyHCEHqNW%2BVuj9mAqHgvclzLyJ9u8ZyPhdgaEU2zuutjlyAtpgSASDaV1AlJz4eIPnNkR8TuARw%2FiMvA3aCS3I7HBIBeHB1P1aIRIlogS%2FbKJ8HhFURYWcNNyqASsen96JUxotnejDjWLuc0kjTLdpC4ZmlBXeDiJsLTWc50OTXJn%2FeT0GZvc%2BKkbPBl6Ut83QKw7z%2F6aTrGrWj0gaP9uNHAql0DgCjBSVYiGGGJVY4pPxHRNhvE0oRvwC4ofvXPKpS6qUzdCtrX5zzBNkswITO4oacl%2FaeqDF4n8Ja2kTcHRMjbB6wHC11i50R%2FZh%2BF2LBGZCfhUsOxXjHZdX4XFBf0wJ%2F%2BhfMf2V58lgIofcD8e%2Bf5qDtX87aZz77IDjvJYSid%2BmFt1uzEOH2Y5%2BdxnkJdvhv2qoY4A%2FB8lQE%2BHVZ8hUNuXivHPeKlDvFEIKq09XfnLElaNSHbhJGBsrAXPXLd3W%2FNI5GD%2Fn8oMFd7dLswXNpDmHrWNm0KtwEsx7t8yzHReV6M%2BmQFrBgLrcKHScj3Qxabw3%2BnSnYYQrizlsf8w6qT3vAY6pgEisRElkhmJXK2EgW5G6xMZoFjWUKgWpJuUqPELFzfiWYRa%2FSkOH%2BUr9Bdj4xFCdfsbMgvhhac6lCMW2yMbndoZ3zb4D6uNnNcH4bNo5TidFNMiDMPDe1svxX1Mjjb3JdohPIoVMzTr5ff%2Bu976bU2oVDoZ%2F3ksNYFcb4O06LnxPpxC0HQmHp5IYc2msq7j8thurQ3ImYC3C7Ya7E0alnReMAoz7Q9B&X-Amz-Signature=6d27249504d0e6ac7b03677de7c43a41225980365193795af462abd1163df955&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZUIPFHE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1Yx%2F%2FDrVkHt4FNs%2BM3XS0JUj%2BQoSh0ATtMftoM3G6CAIhALlyyJAjyUuS%2BoMlRD0Tl0ssCWYj9Xh%2FJ0nTP6E8VzOCKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydZd910C%2FdRmHG%2BCgq3AOWKg6eNWNtUWXhJYpdad3heyJseHuEYNPx7O09Im%2BxBQMbBxAGC4cOXD6qgLPt%2Bn7XemwprroL26E87Puuu9WuUaQkN%2BMags8rSluwrVKGxFYH7Q%2Fzf894dhTIFESXYOqgIGW%2FJMNVP%2FyAU3yPnj4kPpTZvcFttouHlA1i7BXV7KTNFMyBn4ncsZ%2FSQ6PxP2RP6NwiS3tzKbkrHxlt3FVL%2FvsSZTIhZoMEEVRmC%2F5p2OA%2BZRgSkRGOhiZ%2BwH93lEmpiyBc9xLVwM5HBi5AyuL2kPePt0RgbHJWlBITtZpNB%2FWM6P2lwTgJDd0ITALx6IVGzZlUL0pITbxNdr5u%2BK6opm%2FJ0LXZX09GKlVoSyBmTSnpLb0kDlzCBZChSpFKgdlo5jlf99h%2BWje4mxQrEBAVeZ4zPNig%2FSn0XEAH9nI9nztN2k%2FuOyo%2BbN4hD6UbCXBatnnkq6y72S8C9SByRqq%2B0ni3aLjVJiE4CONvrWKFI0kk4q3Dr2cpHPu35CugJ0z4dZvPAlMiQ1x01tAgmJ4y78BIX9o8Ii6N%2FAQPtV5YsPhCCV%2FPdxcZqfnf9gR6go3q20EPNmk7tiU%2BPY6n%2Bn81lJKAoOsHJsoPIOOwbhFwmQuLhoPM3jY55fDz8zDdpPe8BjqkAVHhIPSlXQDR8mcCIG3vEklQO5c2y%2Ffr%2FuR76XoF6czk2xH83FYXDdPliz%2FjsMJzISF%2BkDzBOdcefzpeFDVXzwOJgh1SuOC5pIPEOZWYHA%2BdtU88kQnBclfdWUO1bsoMuw19hnOcc287K79%2Bdbak8GuPcydWfV851VopMcov12Rnit3z5SBswMk2zg7ZqovMSkIB7U9w%2BpJvLUIeiQV9TF7fDu0F&X-Amz-Signature=15002a6bed26e80c4f1233ec6361122597f4270adcbef92f2376dd87f1d754d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7TRLT4W%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE3XW53CKpYaPUEp4ircKo8cQNultOsfy87bFAnGmfvbAiAmLVro1oTDxlUoIGtOZL8iCZhNb2%2FJNCKWlpcS8FxZeSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMID%2BqmXhST5r9CXHNKtwDlDVwLVU9xzNmreMpoySQ%2BKIi%2BSqgcsnNRjgojbOlEN4N6A6yy7ow0uFh9iSGCB%2FF671RhAedrW2Uz0oIf67OU0ID7II7rQfqc1ic9jtOXAcT%2BnjvTF51bGrcF6TK94aY7I%2F6MfKy4BirQfcYP9eDGWtLLHp%2BNk1usJ0Egshx3Y3phFgiP2ht%2FRjrpApMIZJhFlCMH3IXcRcCTd4T9%2FvUD%2BOP0dMnnf7sRBQ6a%2B5lHJWGseg%2BLzXJEKDqGg5ftN4I7h9i4RQhlkTn2O2OEFWTwAqwDXd1m1dkF4rVFtnS5eZgYvhIDE%2BeLz3bAwTMkm8RlDSKxOcA9IgG71y7Aw04dCE1g9tLLIXxQZ%2FoS6Jc%2FjdaIJuxLHTiHCNNRQ%2BB7BcQXokL2AqDENUPqX%2FOozKuhcNNkEH0OTd7THf3vvJnI1JikqUYVPbGgrk3MWrY70tiC4S0OddSRIrtfmTSskq4%2FZraTznxLhlTyOtK%2Fai3SuoKNXAYgKNvNGo3BYtYu6N27164sT6mSTRkxN74hWejBFdiWjUSuCASCulmD8vdHan6uYbtKwUpb%2F%2B7zQNCYeqlxcg0Lm9%2BzxNq%2FjUuQ0XNHNEyrIjprE1l2jh%2BjL6fMseuU6aKbktiMwyUvEsw26T3vAY6pgGKbMpAUIQyR5d51ZqkfcP0nh58Hloco9hmsYnKVlMiUzQJsvT3eHgO3I4%2F2sgAzxJUBELo25hfLNh8hQqbUsvQ96YRdqHVoEjCAU0BbZ4pMn7LFbkPLuPKfsHcscf1B8OOCij35XkTdk4Hmy%2BWOjkTaEwddjDEfw8lEfTP6PcLsEJxqjBmQ5KDhWIXQaQztRFk9HPgFFD%2Ft4RsNjS%2FNBhcfaI4lboH&X-Amz-Signature=dcc05fb5aaf0954e13cc3f91ca5ed8c3d8d4b8a9c03e1f46008d42d820e02686&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7TRLT4W%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE3XW53CKpYaPUEp4ircKo8cQNultOsfy87bFAnGmfvbAiAmLVro1oTDxlUoIGtOZL8iCZhNb2%2FJNCKWlpcS8FxZeSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMID%2BqmXhST5r9CXHNKtwDlDVwLVU9xzNmreMpoySQ%2BKIi%2BSqgcsnNRjgojbOlEN4N6A6yy7ow0uFh9iSGCB%2FF671RhAedrW2Uz0oIf67OU0ID7II7rQfqc1ic9jtOXAcT%2BnjvTF51bGrcF6TK94aY7I%2F6MfKy4BirQfcYP9eDGWtLLHp%2BNk1usJ0Egshx3Y3phFgiP2ht%2FRjrpApMIZJhFlCMH3IXcRcCTd4T9%2FvUD%2BOP0dMnnf7sRBQ6a%2B5lHJWGseg%2BLzXJEKDqGg5ftN4I7h9i4RQhlkTn2O2OEFWTwAqwDXd1m1dkF4rVFtnS5eZgYvhIDE%2BeLz3bAwTMkm8RlDSKxOcA9IgG71y7Aw04dCE1g9tLLIXxQZ%2FoS6Jc%2FjdaIJuxLHTiHCNNRQ%2BB7BcQXokL2AqDENUPqX%2FOozKuhcNNkEH0OTd7THf3vvJnI1JikqUYVPbGgrk3MWrY70tiC4S0OddSRIrtfmTSskq4%2FZraTznxLhlTyOtK%2Fai3SuoKNXAYgKNvNGo3BYtYu6N27164sT6mSTRkxN74hWejBFdiWjUSuCASCulmD8vdHan6uYbtKwUpb%2F%2B7zQNCYeqlxcg0Lm9%2BzxNq%2FjUuQ0XNHNEyrIjprE1l2jh%2BjL6fMseuU6aKbktiMwyUvEsw26T3vAY6pgGKbMpAUIQyR5d51ZqkfcP0nh58Hloco9hmsYnKVlMiUzQJsvT3eHgO3I4%2F2sgAzxJUBELo25hfLNh8hQqbUsvQ96YRdqHVoEjCAU0BbZ4pMn7LFbkPLuPKfsHcscf1B8OOCij35XkTdk4Hmy%2BWOjkTaEwddjDEfw8lEfTP6PcLsEJxqjBmQ5KDhWIXQaQztRFk9HPgFFD%2Ft4RsNjS%2FNBhcfaI4lboH&X-Amz-Signature=dee2c2723f514c0932fcaa4f54678125b3f6c9bebf61b86164408d07bfd84517&X-Amz-SignedHeaders=host&x-id=GetObject)
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
