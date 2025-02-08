

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RON4HJBQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLD0vg9hPtrOSjHtbO%2B3A9vGiVzbytbi8DeJJM14N1NwIgenoJxcczzq4m5PrhK%2FNGYHTrUhTuQiuxaeo1dXLS3%2F8qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFKnmrmM6QtIlRqeircAwPYMWsIDHgIF9xxRmM%2B6%2BNj9IzVgpmG0MW65j7fCTHseabkcOztoDZdGLYUxq9gRfPcyCoXTNybR1M%2Bxux6%2ByWKUXszgFQsxFalUl63ZD5KNHKvDkG2evFdDKNZYaCOZB1gY9dngfAaYUCOaKNBrevaLennJ1k6MgZMRLpkys4yfXfCJAwDWttREA84Sj%2F5CvB89B82tubx6DCKxuggA97wOp8KmFtj4Euj%2F9zx3EN4Q%2BzltIUHcUPfodGh7FBdRnGVaOeZXQZgojaaQR47DVQ0i%2BfNwyPUh%2Fkvi1J3c1bHvbOz%2B2JKMuYXYEUbbP7pc%2Bzwj%2Bsh7IFd0HBG1bmQOK8kW6ZOrF5YEAZqoappV1pP6ms5TmSX%2B%2FNDaDUr6wAF7em2%2BUmePlt6yex7pnwcKmuiLTuz1kJmYRrJYwt%2Bfxnqfvof8VYvfgKfjnp%2FaLWorUFLalaqtOOcwa1dsRgJDDoNm4mVQd70jLnii5IYMTRTeDCmcHRqeE2OpGMA1R1hRGHxlWCMMqXfzjCYJ9cYaXgU2ny8bN67mxZ1gtXKocmWddJSqGpFce2OelcCP19AtRhGThOaH90jvjm6DYO%2F%2Ftbhx8MiAMn0r4IOB%2BHZAhFnc2Fc%2F0mhXg7a24IxMLWFnb0GOqUBeA2Xk1TApklRgq%2BOe2GQrhGjXQCC4ttytPMYtr%2FoYYE%2F5lGjJAtnMA%2FGybPEQhE%2FLy0d0wbRIA7hYbWHlEjlbsRiRXTqeQnnFlO1d%2FFq09BhJ1VVZNdZuVFb0kRjP7uGd%2BZ5ZFlop1ufGFQakHMNINascPiy3PwUJzXrjGZ4Dz0Ldye0yuDUBESeWEgjbu%2Bu%2BCOCAxT4MjcPa8qnEg2YZQ7IzYK6&X-Amz-Signature=e224a444062f13dbe9ce650bad4d716546fcaa349c0bcf049878d4766d58485f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RON4HJBQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLD0vg9hPtrOSjHtbO%2B3A9vGiVzbytbi8DeJJM14N1NwIgenoJxcczzq4m5PrhK%2FNGYHTrUhTuQiuxaeo1dXLS3%2F8qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFKnmrmM6QtIlRqeircAwPYMWsIDHgIF9xxRmM%2B6%2BNj9IzVgpmG0MW65j7fCTHseabkcOztoDZdGLYUxq9gRfPcyCoXTNybR1M%2Bxux6%2ByWKUXszgFQsxFalUl63ZD5KNHKvDkG2evFdDKNZYaCOZB1gY9dngfAaYUCOaKNBrevaLennJ1k6MgZMRLpkys4yfXfCJAwDWttREA84Sj%2F5CvB89B82tubx6DCKxuggA97wOp8KmFtj4Euj%2F9zx3EN4Q%2BzltIUHcUPfodGh7FBdRnGVaOeZXQZgojaaQR47DVQ0i%2BfNwyPUh%2Fkvi1J3c1bHvbOz%2B2JKMuYXYEUbbP7pc%2Bzwj%2Bsh7IFd0HBG1bmQOK8kW6ZOrF5YEAZqoappV1pP6ms5TmSX%2B%2FNDaDUr6wAF7em2%2BUmePlt6yex7pnwcKmuiLTuz1kJmYRrJYwt%2Bfxnqfvof8VYvfgKfjnp%2FaLWorUFLalaqtOOcwa1dsRgJDDoNm4mVQd70jLnii5IYMTRTeDCmcHRqeE2OpGMA1R1hRGHxlWCMMqXfzjCYJ9cYaXgU2ny8bN67mxZ1gtXKocmWddJSqGpFce2OelcCP19AtRhGThOaH90jvjm6DYO%2F%2Ftbhx8MiAMn0r4IOB%2BHZAhFnc2Fc%2F0mhXg7a24IxMLWFnb0GOqUBeA2Xk1TApklRgq%2BOe2GQrhGjXQCC4ttytPMYtr%2FoYYE%2F5lGjJAtnMA%2FGybPEQhE%2FLy0d0wbRIA7hYbWHlEjlbsRiRXTqeQnnFlO1d%2FFq09BhJ1VVZNdZuVFb0kRjP7uGd%2BZ5ZFlop1ufGFQakHMNINascPiy3PwUJzXrjGZ4Dz0Ldye0yuDUBESeWEgjbu%2Bu%2BCOCAxT4MjcPa8qnEg2YZQ7IzYK6&X-Amz-Signature=06258aec9c9bf774863b4c24494c55a283dfdf39a0b8d05c912c95e6e0c57966&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RON4HJBQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLD0vg9hPtrOSjHtbO%2B3A9vGiVzbytbi8DeJJM14N1NwIgenoJxcczzq4m5PrhK%2FNGYHTrUhTuQiuxaeo1dXLS3%2F8qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFKnmrmM6QtIlRqeircAwPYMWsIDHgIF9xxRmM%2B6%2BNj9IzVgpmG0MW65j7fCTHseabkcOztoDZdGLYUxq9gRfPcyCoXTNybR1M%2Bxux6%2ByWKUXszgFQsxFalUl63ZD5KNHKvDkG2evFdDKNZYaCOZB1gY9dngfAaYUCOaKNBrevaLennJ1k6MgZMRLpkys4yfXfCJAwDWttREA84Sj%2F5CvB89B82tubx6DCKxuggA97wOp8KmFtj4Euj%2F9zx3EN4Q%2BzltIUHcUPfodGh7FBdRnGVaOeZXQZgojaaQR47DVQ0i%2BfNwyPUh%2Fkvi1J3c1bHvbOz%2B2JKMuYXYEUbbP7pc%2Bzwj%2Bsh7IFd0HBG1bmQOK8kW6ZOrF5YEAZqoappV1pP6ms5TmSX%2B%2FNDaDUr6wAF7em2%2BUmePlt6yex7pnwcKmuiLTuz1kJmYRrJYwt%2Bfxnqfvof8VYvfgKfjnp%2FaLWorUFLalaqtOOcwa1dsRgJDDoNm4mVQd70jLnii5IYMTRTeDCmcHRqeE2OpGMA1R1hRGHxlWCMMqXfzjCYJ9cYaXgU2ny8bN67mxZ1gtXKocmWddJSqGpFce2OelcCP19AtRhGThOaH90jvjm6DYO%2F%2Ftbhx8MiAMn0r4IOB%2BHZAhFnc2Fc%2F0mhXg7a24IxMLWFnb0GOqUBeA2Xk1TApklRgq%2BOe2GQrhGjXQCC4ttytPMYtr%2FoYYE%2F5lGjJAtnMA%2FGybPEQhE%2FLy0d0wbRIA7hYbWHlEjlbsRiRXTqeQnnFlO1d%2FFq09BhJ1VVZNdZuVFb0kRjP7uGd%2BZ5ZFlop1ufGFQakHMNINascPiy3PwUJzXrjGZ4Dz0Ldye0yuDUBESeWEgjbu%2Bu%2BCOCAxT4MjcPa8qnEg2YZQ7IzYK6&X-Amz-Signature=f05b9d2055f2dfc09ac626c4be7c3a258c2a32bf03be8ba902506c7b53481ff9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RON4HJBQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLD0vg9hPtrOSjHtbO%2B3A9vGiVzbytbi8DeJJM14N1NwIgenoJxcczzq4m5PrhK%2FNGYHTrUhTuQiuxaeo1dXLS3%2F8qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFKnmrmM6QtIlRqeircAwPYMWsIDHgIF9xxRmM%2B6%2BNj9IzVgpmG0MW65j7fCTHseabkcOztoDZdGLYUxq9gRfPcyCoXTNybR1M%2Bxux6%2ByWKUXszgFQsxFalUl63ZD5KNHKvDkG2evFdDKNZYaCOZB1gY9dngfAaYUCOaKNBrevaLennJ1k6MgZMRLpkys4yfXfCJAwDWttREA84Sj%2F5CvB89B82tubx6DCKxuggA97wOp8KmFtj4Euj%2F9zx3EN4Q%2BzltIUHcUPfodGh7FBdRnGVaOeZXQZgojaaQR47DVQ0i%2BfNwyPUh%2Fkvi1J3c1bHvbOz%2B2JKMuYXYEUbbP7pc%2Bzwj%2Bsh7IFd0HBG1bmQOK8kW6ZOrF5YEAZqoappV1pP6ms5TmSX%2B%2FNDaDUr6wAF7em2%2BUmePlt6yex7pnwcKmuiLTuz1kJmYRrJYwt%2Bfxnqfvof8VYvfgKfjnp%2FaLWorUFLalaqtOOcwa1dsRgJDDoNm4mVQd70jLnii5IYMTRTeDCmcHRqeE2OpGMA1R1hRGHxlWCMMqXfzjCYJ9cYaXgU2ny8bN67mxZ1gtXKocmWddJSqGpFce2OelcCP19AtRhGThOaH90jvjm6DYO%2F%2Ftbhx8MiAMn0r4IOB%2BHZAhFnc2Fc%2F0mhXg7a24IxMLWFnb0GOqUBeA2Xk1TApklRgq%2BOe2GQrhGjXQCC4ttytPMYtr%2FoYYE%2F5lGjJAtnMA%2FGybPEQhE%2FLy0d0wbRIA7hYbWHlEjlbsRiRXTqeQnnFlO1d%2FFq09BhJ1VVZNdZuVFb0kRjP7uGd%2BZ5ZFlop1ufGFQakHMNINascPiy3PwUJzXrjGZ4Dz0Ldye0yuDUBESeWEgjbu%2Bu%2BCOCAxT4MjcPa8qnEg2YZQ7IzYK6&X-Amz-Signature=28dfe01136b9f5ced239fa705f6b31ff51f4b925d961fb106cad38715f3540c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RON4HJBQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLD0vg9hPtrOSjHtbO%2B3A9vGiVzbytbi8DeJJM14N1NwIgenoJxcczzq4m5PrhK%2FNGYHTrUhTuQiuxaeo1dXLS3%2F8qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFKnmrmM6QtIlRqeircAwPYMWsIDHgIF9xxRmM%2B6%2BNj9IzVgpmG0MW65j7fCTHseabkcOztoDZdGLYUxq9gRfPcyCoXTNybR1M%2Bxux6%2ByWKUXszgFQsxFalUl63ZD5KNHKvDkG2evFdDKNZYaCOZB1gY9dngfAaYUCOaKNBrevaLennJ1k6MgZMRLpkys4yfXfCJAwDWttREA84Sj%2F5CvB89B82tubx6DCKxuggA97wOp8KmFtj4Euj%2F9zx3EN4Q%2BzltIUHcUPfodGh7FBdRnGVaOeZXQZgojaaQR47DVQ0i%2BfNwyPUh%2Fkvi1J3c1bHvbOz%2B2JKMuYXYEUbbP7pc%2Bzwj%2Bsh7IFd0HBG1bmQOK8kW6ZOrF5YEAZqoappV1pP6ms5TmSX%2B%2FNDaDUr6wAF7em2%2BUmePlt6yex7pnwcKmuiLTuz1kJmYRrJYwt%2Bfxnqfvof8VYvfgKfjnp%2FaLWorUFLalaqtOOcwa1dsRgJDDoNm4mVQd70jLnii5IYMTRTeDCmcHRqeE2OpGMA1R1hRGHxlWCMMqXfzjCYJ9cYaXgU2ny8bN67mxZ1gtXKocmWddJSqGpFce2OelcCP19AtRhGThOaH90jvjm6DYO%2F%2Ftbhx8MiAMn0r4IOB%2BHZAhFnc2Fc%2F0mhXg7a24IxMLWFnb0GOqUBeA2Xk1TApklRgq%2BOe2GQrhGjXQCC4ttytPMYtr%2FoYYE%2F5lGjJAtnMA%2FGybPEQhE%2FLy0d0wbRIA7hYbWHlEjlbsRiRXTqeQnnFlO1d%2FFq09BhJ1VVZNdZuVFb0kRjP7uGd%2BZ5ZFlop1ufGFQakHMNINascPiy3PwUJzXrjGZ4Dz0Ldye0yuDUBESeWEgjbu%2Bu%2BCOCAxT4MjcPa8qnEg2YZQ7IzYK6&X-Amz-Signature=bf013909ac4d39414241e605d97ae17cf8c7c0c5f2dce6cfa523aa2d65aea8f8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RON4HJBQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLD0vg9hPtrOSjHtbO%2B3A9vGiVzbytbi8DeJJM14N1NwIgenoJxcczzq4m5PrhK%2FNGYHTrUhTuQiuxaeo1dXLS3%2F8qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFKnmrmM6QtIlRqeircAwPYMWsIDHgIF9xxRmM%2B6%2BNj9IzVgpmG0MW65j7fCTHseabkcOztoDZdGLYUxq9gRfPcyCoXTNybR1M%2Bxux6%2ByWKUXszgFQsxFalUl63ZD5KNHKvDkG2evFdDKNZYaCOZB1gY9dngfAaYUCOaKNBrevaLennJ1k6MgZMRLpkys4yfXfCJAwDWttREA84Sj%2F5CvB89B82tubx6DCKxuggA97wOp8KmFtj4Euj%2F9zx3EN4Q%2BzltIUHcUPfodGh7FBdRnGVaOeZXQZgojaaQR47DVQ0i%2BfNwyPUh%2Fkvi1J3c1bHvbOz%2B2JKMuYXYEUbbP7pc%2Bzwj%2Bsh7IFd0HBG1bmQOK8kW6ZOrF5YEAZqoappV1pP6ms5TmSX%2B%2FNDaDUr6wAF7em2%2BUmePlt6yex7pnwcKmuiLTuz1kJmYRrJYwt%2Bfxnqfvof8VYvfgKfjnp%2FaLWorUFLalaqtOOcwa1dsRgJDDoNm4mVQd70jLnii5IYMTRTeDCmcHRqeE2OpGMA1R1hRGHxlWCMMqXfzjCYJ9cYaXgU2ny8bN67mxZ1gtXKocmWddJSqGpFce2OelcCP19AtRhGThOaH90jvjm6DYO%2F%2Ftbhx8MiAMn0r4IOB%2BHZAhFnc2Fc%2F0mhXg7a24IxMLWFnb0GOqUBeA2Xk1TApklRgq%2BOe2GQrhGjXQCC4ttytPMYtr%2FoYYE%2F5lGjJAtnMA%2FGybPEQhE%2FLy0d0wbRIA7hYbWHlEjlbsRiRXTqeQnnFlO1d%2FFq09BhJ1VVZNdZuVFb0kRjP7uGd%2BZ5ZFlop1ufGFQakHMNINascPiy3PwUJzXrjGZ4Dz0Ldye0yuDUBESeWEgjbu%2Bu%2BCOCAxT4MjcPa8qnEg2YZQ7IzYK6&X-Amz-Signature=d36bb477794610ea646ee21dbb38a86f7a113b9543ebe72eab2e56ffe7b475cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RON4HJBQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLD0vg9hPtrOSjHtbO%2B3A9vGiVzbytbi8DeJJM14N1NwIgenoJxcczzq4m5PrhK%2FNGYHTrUhTuQiuxaeo1dXLS3%2F8qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFKnmrmM6QtIlRqeircAwPYMWsIDHgIF9xxRmM%2B6%2BNj9IzVgpmG0MW65j7fCTHseabkcOztoDZdGLYUxq9gRfPcyCoXTNybR1M%2Bxux6%2ByWKUXszgFQsxFalUl63ZD5KNHKvDkG2evFdDKNZYaCOZB1gY9dngfAaYUCOaKNBrevaLennJ1k6MgZMRLpkys4yfXfCJAwDWttREA84Sj%2F5CvB89B82tubx6DCKxuggA97wOp8KmFtj4Euj%2F9zx3EN4Q%2BzltIUHcUPfodGh7FBdRnGVaOeZXQZgojaaQR47DVQ0i%2BfNwyPUh%2Fkvi1J3c1bHvbOz%2B2JKMuYXYEUbbP7pc%2Bzwj%2Bsh7IFd0HBG1bmQOK8kW6ZOrF5YEAZqoappV1pP6ms5TmSX%2B%2FNDaDUr6wAF7em2%2BUmePlt6yex7pnwcKmuiLTuz1kJmYRrJYwt%2Bfxnqfvof8VYvfgKfjnp%2FaLWorUFLalaqtOOcwa1dsRgJDDoNm4mVQd70jLnii5IYMTRTeDCmcHRqeE2OpGMA1R1hRGHxlWCMMqXfzjCYJ9cYaXgU2ny8bN67mxZ1gtXKocmWddJSqGpFce2OelcCP19AtRhGThOaH90jvjm6DYO%2F%2Ftbhx8MiAMn0r4IOB%2BHZAhFnc2Fc%2F0mhXg7a24IxMLWFnb0GOqUBeA2Xk1TApklRgq%2BOe2GQrhGjXQCC4ttytPMYtr%2FoYYE%2F5lGjJAtnMA%2FGybPEQhE%2FLy0d0wbRIA7hYbWHlEjlbsRiRXTqeQnnFlO1d%2FFq09BhJ1VVZNdZuVFb0kRjP7uGd%2BZ5ZFlop1ufGFQakHMNINascPiy3PwUJzXrjGZ4Dz0Ldye0yuDUBESeWEgjbu%2Bu%2BCOCAxT4MjcPa8qnEg2YZQ7IzYK6&X-Amz-Signature=d2f3d90a8674661af5461ba30c588221a56087578e2d66ae976454a5a1bcbfa1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RON4HJBQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDLD0vg9hPtrOSjHtbO%2B3A9vGiVzbytbi8DeJJM14N1NwIgenoJxcczzq4m5PrhK%2FNGYHTrUhTuQiuxaeo1dXLS3%2F8qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFKnmrmM6QtIlRqeircAwPYMWsIDHgIF9xxRmM%2B6%2BNj9IzVgpmG0MW65j7fCTHseabkcOztoDZdGLYUxq9gRfPcyCoXTNybR1M%2Bxux6%2ByWKUXszgFQsxFalUl63ZD5KNHKvDkG2evFdDKNZYaCOZB1gY9dngfAaYUCOaKNBrevaLennJ1k6MgZMRLpkys4yfXfCJAwDWttREA84Sj%2F5CvB89B82tubx6DCKxuggA97wOp8KmFtj4Euj%2F9zx3EN4Q%2BzltIUHcUPfodGh7FBdRnGVaOeZXQZgojaaQR47DVQ0i%2BfNwyPUh%2Fkvi1J3c1bHvbOz%2B2JKMuYXYEUbbP7pc%2Bzwj%2Bsh7IFd0HBG1bmQOK8kW6ZOrF5YEAZqoappV1pP6ms5TmSX%2B%2FNDaDUr6wAF7em2%2BUmePlt6yex7pnwcKmuiLTuz1kJmYRrJYwt%2Bfxnqfvof8VYvfgKfjnp%2FaLWorUFLalaqtOOcwa1dsRgJDDoNm4mVQd70jLnii5IYMTRTeDCmcHRqeE2OpGMA1R1hRGHxlWCMMqXfzjCYJ9cYaXgU2ny8bN67mxZ1gtXKocmWddJSqGpFce2OelcCP19AtRhGThOaH90jvjm6DYO%2F%2Ftbhx8MiAMn0r4IOB%2BHZAhFnc2Fc%2F0mhXg7a24IxMLWFnb0GOqUBeA2Xk1TApklRgq%2BOe2GQrhGjXQCC4ttytPMYtr%2FoYYE%2F5lGjJAtnMA%2FGybPEQhE%2FLy0d0wbRIA7hYbWHlEjlbsRiRXTqeQnnFlO1d%2FFq09BhJ1VVZNdZuVFb0kRjP7uGd%2BZ5ZFlop1ufGFQakHMNINascPiy3PwUJzXrjGZ4Dz0Ldye0yuDUBESeWEgjbu%2Bu%2BCOCAxT4MjcPa8qnEg2YZQ7IzYK6&X-Amz-Signature=faa8611d967d2f5405ebafe1a2954e6b44212903a3ba9b63bc4e56548e9fb269&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DW4A3ZR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIBN1xx2oTO4ebHDptXhVBWHB9pZYQbcCcAt46APiNYivAiEAwcvjQ5aVt5Xc7oKsyatgljZmpKmKnAIT3Qi4QyNWl%2BcqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLG5kDEqw8K20FTCZircA%2FexK2iZzABXCi5peWdpe2qZJCwqS2VEdI9WJLTzQNhFMcFlx6HWcIcHTdgI%2FX975D0KZr%2FCuE%2BKDn8rIHNirPbaFy4gMVLusCWrhrJa9WfytJQnLZr%2FAOf6BbwwlDv8HZFOkTEY3D6bx8hKH4VomsGskZiamIAxnMH4ioh4Rd71lwsL0%2B498Xt5pUz2xssS0A%2BSo9VMO%2B%2FuKeB8QlUVCrJqEVQWl1qUWzjWGYxaLlyxxMmzrSzoInOfZNRYCAeyaln3EZ%2FposSwafQTgRGlnVmMa6PcIGLm7ZE3wBX%2F%2FXscC7q6K1yagC8rWZTldtagiaPS2Zn4wyHejULbQ81E38XpvCshYgtreM1dhQ7%2BQHCDp73lCTdYG%2FYRO8Sw2H6uE6cdNSjsJ4rq7oSbgOwgmILpbBfGera48fVXT05ZYyRpN7yCDXux%2BAQZDU9uCNK2ocFbRehiqwjTIjFDmS6SXcqhYc25D8lBJ2KSV16yDWHe5tjmk9K24MEP97MUX4S5F%2BDAkkTWq3xwbHBs%2BG02rjc6btBopxAbTqHg3IRcnVjV%2BeFnTS1Bfxxrh9898dJYvpBLNsI%2BsJQaRHEmnVw6ec41hDikdUHMp8Iz8jq31LvH%2BO%2B%2BoyHE5LNokEXuMKKFnb0GOqUBIW9p1cIrvqV3uRo%2FBsgiKNNCsvORH4RU%2FeDwaEq9K6MOI5nbuM6E3jp%2BPF3oCVcuQSE1IAFGeg8ch0jj6bSApUAd%2FPyeYrKGoFppJbc35NAuEc0JK6he5drADpQqcw5OX2nuGNpvAYbsOugSZ4rJlf64Uv98KrFTMrzIaUBrTlzCva16NU6otoWExrjotlnQcU0g1S430TM0b84uUExkZpqwgiBB&X-Amz-Signature=ee6c5de4aea572e038d8351ecd90597352f1fe60bc152973296d1303c81b5ca3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TCYMP3Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCTCqVsMsw%2B%2BpFraK2Pk%2FPt4z%2B31ZsDEsotFuwHcYVD0QIgOyEsiTftyND5PzLgEZ2uHN7d1Gd4FziQt33tFc5B434qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH1Y979zwCeV3Rv2pCrcA1L0JAjJNlguNdBRRd%2B03XqDsxvIG2B564DWJ3Ig%2BvYMKZYwYojC70F28yKNluiWCIvBKWIT1KoCh9bH37CrcgXx4Ruv0MLVxTTJ9d4nUR84nWnkaGwY948SCfEoA6k7%2BD454CKoLYMN6mK3pYNRKcVbd%2FCw6mDtkM6JKKDvJNNcE1FZkQDewOpThs6yET%2FaeolgfI%2FXkl2qST23IHQqhR%2B6VEwXzY0Yokchv0EN1HHWgLTxssic%2FOVjtvbHTqLZOB4Wafxj1OhohKbtR1gInHLjnBfEvWVs0vceS2a2BX3wbuGSTzkVUCVaoVoMkxI6zBkI3TyKhAns%2BOfDVTwOO%2BZHumqfRTd7nMwzuBjufd6QFfhUwk%2BXzKFiul%2BR7cEp8eBmIRONVva%2F7p4QwqLeo6Jyhb3FABA%2F0WbAj1BMcbuuYLKDZ%2Bd40uZL%2FMkpaE5tsJYSqbLp%2F%2FMhiViRX5UyakG0qLBo%2FiC0HlYtRLpGYo8MAaCctWwibEcullTpPOSdC6idF4R6FM2sANerzFWKuoyVO7rboqUbGcFBRB0Hx3x6q%2FijlCB5dIqfKm7fAvXQJZQ%2F2x6ueGg%2FtJ%2F9672xUAyh0RX0Qmh%2BH4ZcAbYDOGJLbCFTy6dLllWg4%2F6GMKmFnb0GOqUBj7eoN7lFLquoSgg9PsQpO5Udih7i6CWHDHWysAN4ncWueuHlcjaNBXE%2FG5gWIIMGQ7%2BGASWiYdBHTnJJbumrl45z44KvxmXy1YudR0P0jxn2Ow9uZ9uq6THOo%2Bzjrz1%2Fkh0Fadf6EYpgTS7A5JT1TE%2BwHFWgV6gmzIIyNBqPivYgKKG5PO3YIDOYdP8tUJngv9BRCR%2BDSnKPLEbB2qXJR2w41RSo&X-Amz-Signature=de47c1435b66008ea57b1b434376baabc3eb30ddab984266aee9845573e24e01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STKKAFL5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBAYPSOluPdOYmfr%2FO1ZAzP9Fw1RiWiQCvwO%2BergQ4iZAiAdgY%2FU%2FiYWQmSa2CXBWtYZJ0lwmV9qr2glbkgTD4%2FQ%2FyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBJ21sa6YFBeUrvVcKtwDdNsBo%2ByIyGTGgnkZd5yA6BU7QH0l48PJ1O4uGxmVcS2tcdG8L4Pry6hfgTGgiVv16vs6nFbFIhEoGBhCqQ9B2CR%2BqJZwGyGSziiFoKHGy0SdkfVQa%2Fa9W8f3EfwXiItijIDB4jRpOfcmyX%2BfyvR5j2775MCIVJEaX8CgxltK9PemDo62%2Fue9dvi8Bjscr8qw8Ax8KO%2BKc6ZbnBhvtXWx2R0qxvtC0nCcj%2FVrxMqbnORp4VwVsBVBdkMmJf%2BFACiPeG1Lfy6lGzwptG4swWlWrgaVDlnSe8OpEBNpMvZcfSRW%2B%2FU%2FuaIMtbMG5QpB6bZUkrSzhpp3hLwErBL6MZ2HTTu5tuNL7qxYNqRLFm2WX%2Flyu%2FuJGEUv%2Bp6asFHbwMgNJM%2BDUkbDUdgNiX8cmzJ5wfGgXDqPsNqiM%2FLMGDm1Jzur2Biuv4Sz0MJ1AS%2BKwF6R9CO7%2F61w3OTGbCILdNndKl9LvQXrjB7yAkNSmsyNkLQ8ZOFKqw55GVM73dhgPCwnN1f1Uclog45yd2I8CH3uutzxLIaJm%2F24%2B2ZDowzJfSKHS0qBkaFsGx65vfoduirdZCkDgykjjiRAiNLGm8iqZhsT1cC2CcLy7FPwBq5n2WnF75GoO%2F2CdsDiKd4wtYWdvQY6pgEF5eTOsxXBdmuRteYHEC%2BGVyH2br46FN1ZpU3qCH23pxkWtYrh%2FdB3rMIwvEk6RB0YN0%2Bv4g77E%2B4cfoXK0uKn62b7L1LEVqi7fbK8LqNiwR0FVExPfzDdM4QYQaYDFfHFRPDdSPr0h3LkEsgrIsRZ%2ByV8TUdc3fFAHZBZYj%2FQIbna0X5I2j0LuS2GJjJnEY%2B6UBSJTmnXeyIsr62OuprryyGis6GO&X-Amz-Signature=9eecdfe8f35c3a0516306864e3fa5ccfe608bd4ac5b40b9b30ae3275d6d57f03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STKKAFL5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIBAYPSOluPdOYmfr%2FO1ZAzP9Fw1RiWiQCvwO%2BergQ4iZAiAdgY%2FU%2FiYWQmSa2CXBWtYZJ0lwmV9qr2glbkgTD4%2FQ%2FyqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBJ21sa6YFBeUrvVcKtwDdNsBo%2ByIyGTGgnkZd5yA6BU7QH0l48PJ1O4uGxmVcS2tcdG8L4Pry6hfgTGgiVv16vs6nFbFIhEoGBhCqQ9B2CR%2BqJZwGyGSziiFoKHGy0SdkfVQa%2Fa9W8f3EfwXiItijIDB4jRpOfcmyX%2BfyvR5j2775MCIVJEaX8CgxltK9PemDo62%2Fue9dvi8Bjscr8qw8Ax8KO%2BKc6ZbnBhvtXWx2R0qxvtC0nCcj%2FVrxMqbnORp4VwVsBVBdkMmJf%2BFACiPeG1Lfy6lGzwptG4swWlWrgaVDlnSe8OpEBNpMvZcfSRW%2B%2FU%2FuaIMtbMG5QpB6bZUkrSzhpp3hLwErBL6MZ2HTTu5tuNL7qxYNqRLFm2WX%2Flyu%2FuJGEUv%2Bp6asFHbwMgNJM%2BDUkbDUdgNiX8cmzJ5wfGgXDqPsNqiM%2FLMGDm1Jzur2Biuv4Sz0MJ1AS%2BKwF6R9CO7%2F61w3OTGbCILdNndKl9LvQXrjB7yAkNSmsyNkLQ8ZOFKqw55GVM73dhgPCwnN1f1Uclog45yd2I8CH3uutzxLIaJm%2F24%2B2ZDowzJfSKHS0qBkaFsGx65vfoduirdZCkDgykjjiRAiNLGm8iqZhsT1cC2CcLy7FPwBq5n2WnF75GoO%2F2CdsDiKd4wtYWdvQY6pgEF5eTOsxXBdmuRteYHEC%2BGVyH2br46FN1ZpU3qCH23pxkWtYrh%2FdB3rMIwvEk6RB0YN0%2Bv4g77E%2B4cfoXK0uKn62b7L1LEVqi7fbK8LqNiwR0FVExPfzDdM4QYQaYDFfHFRPDdSPr0h3LkEsgrIsRZ%2ByV8TUdc3fFAHZBZYj%2FQIbna0X5I2j0LuS2GJjJnEY%2B6UBSJTmnXeyIsr62OuprryyGis6GO&X-Amz-Signature=682c842f4e37206e9e5842866ec7657e9a6c3ef4edcc07ff848f1c40cce89c93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
