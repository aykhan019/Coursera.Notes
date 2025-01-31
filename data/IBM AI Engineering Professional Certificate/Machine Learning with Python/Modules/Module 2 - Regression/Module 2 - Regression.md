

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627Q72RPT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBf4doei%2FNbZEr4obgtvcoxldXimaH3GZoaEC0SNqgrcAiEA1v32jdkCqs3uQwwfT3BrYx5bvb2H5ovFwmLCrC1XMtsqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFv1ALP5l1LIyVDJLCrcA5skVH6Cs8KckNUwAko4j93icj0cSoG8CiRXEp87KXfQp5fwpCUJweyTdmcGFXT3YK74G8HmSlKQrL1GRAsrUwjPZWdpwGwWMcX%2FN9oBwoxbPn373JDUXqrVhDZVR28Xps3Xyj%2BgOAgHn9Oy33O5PP6olXCjVCCMRJ%2Bwd6VphoMtER%2FphrDy8LvO4N71G3XO%2By5Dl3tJxkO%2FO06Ja11gMrtuPudRaTCLlQlluvzn0o3Wy4lwuLfd68gB042FWmVU%2Fr6YsZx16fDpxzesUqT6%2F4h2E8UCvtBlQUMJqCJxa7pAI1gycDvdckklixT%2BT2hyyKgQoYbqdYvNyHLkN6Ln9GBUZi9Xqkor%2BoUDVrBbWCvcnEPvO7hBwqgbn%2Bx45ste2qjbyPxtXecN7etc0lQ1UeDuoUS1VJ%2FLSR5O8XkwmlhRpCjy55gWd4EYzloimIuyWwOhZNjbj3TYElBSVK0i2Y7F5yjc0OwEdzxR8AVfNDBYxcBZIuzUSj6X6txH1wuPL3zGGwvhtthshpODTd2tKc2wVIWI3qbrCUv5w%2FKKEYeJ4%2F7YSSEV4yt7YW5CT77huxkNT%2BF%2BZYqN1aDx5%2FaKi3vDqcp64Tew6airU7gea6H5eSaJjBIcndHe2wL3MOOj9LwGOqUBUqoXV9l5McIrLvAJRqiIU3UlWIerKhKdaSpYCz4%2BhEcTMkB3b%2BnZCoSuKqQjgdtQHBbXwb4oKN%2BFldnXKuS9FElFeYAfISJ%2FbsQYo%2FfZccSCBukaKWU14nqJImlhzl0onSQmmszO%2FwqAP0F8Vx63ch14I4txEjShiqa9YF%2B2kosIL1RrhpruSBFLPCf5SHYpx4jnX2BkjpKIQxuERRhKw1pCqMEh&X-Amz-Signature=d2683cd8db04f7a8a956b2e383faabeb03fb8faf582fbf8d226daac39d981349&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627Q72RPT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBf4doei%2FNbZEr4obgtvcoxldXimaH3GZoaEC0SNqgrcAiEA1v32jdkCqs3uQwwfT3BrYx5bvb2H5ovFwmLCrC1XMtsqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFv1ALP5l1LIyVDJLCrcA5skVH6Cs8KckNUwAko4j93icj0cSoG8CiRXEp87KXfQp5fwpCUJweyTdmcGFXT3YK74G8HmSlKQrL1GRAsrUwjPZWdpwGwWMcX%2FN9oBwoxbPn373JDUXqrVhDZVR28Xps3Xyj%2BgOAgHn9Oy33O5PP6olXCjVCCMRJ%2Bwd6VphoMtER%2FphrDy8LvO4N71G3XO%2By5Dl3tJxkO%2FO06Ja11gMrtuPudRaTCLlQlluvzn0o3Wy4lwuLfd68gB042FWmVU%2Fr6YsZx16fDpxzesUqT6%2F4h2E8UCvtBlQUMJqCJxa7pAI1gycDvdckklixT%2BT2hyyKgQoYbqdYvNyHLkN6Ln9GBUZi9Xqkor%2BoUDVrBbWCvcnEPvO7hBwqgbn%2Bx45ste2qjbyPxtXecN7etc0lQ1UeDuoUS1VJ%2FLSR5O8XkwmlhRpCjy55gWd4EYzloimIuyWwOhZNjbj3TYElBSVK0i2Y7F5yjc0OwEdzxR8AVfNDBYxcBZIuzUSj6X6txH1wuPL3zGGwvhtthshpODTd2tKc2wVIWI3qbrCUv5w%2FKKEYeJ4%2F7YSSEV4yt7YW5CT77huxkNT%2BF%2BZYqN1aDx5%2FaKi3vDqcp64Tew6airU7gea6H5eSaJjBIcndHe2wL3MOOj9LwGOqUBUqoXV9l5McIrLvAJRqiIU3UlWIerKhKdaSpYCz4%2BhEcTMkB3b%2BnZCoSuKqQjgdtQHBbXwb4oKN%2BFldnXKuS9FElFeYAfISJ%2FbsQYo%2FfZccSCBukaKWU14nqJImlhzl0onSQmmszO%2FwqAP0F8Vx63ch14I4txEjShiqa9YF%2B2kosIL1RrhpruSBFLPCf5SHYpx4jnX2BkjpKIQxuERRhKw1pCqMEh&X-Amz-Signature=78a94906e9d199c3d3cd290a5bf6f74cc549221c186bf21801cd085d7056a9e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627Q72RPT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBf4doei%2FNbZEr4obgtvcoxldXimaH3GZoaEC0SNqgrcAiEA1v32jdkCqs3uQwwfT3BrYx5bvb2H5ovFwmLCrC1XMtsqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFv1ALP5l1LIyVDJLCrcA5skVH6Cs8KckNUwAko4j93icj0cSoG8CiRXEp87KXfQp5fwpCUJweyTdmcGFXT3YK74G8HmSlKQrL1GRAsrUwjPZWdpwGwWMcX%2FN9oBwoxbPn373JDUXqrVhDZVR28Xps3Xyj%2BgOAgHn9Oy33O5PP6olXCjVCCMRJ%2Bwd6VphoMtER%2FphrDy8LvO4N71G3XO%2By5Dl3tJxkO%2FO06Ja11gMrtuPudRaTCLlQlluvzn0o3Wy4lwuLfd68gB042FWmVU%2Fr6YsZx16fDpxzesUqT6%2F4h2E8UCvtBlQUMJqCJxa7pAI1gycDvdckklixT%2BT2hyyKgQoYbqdYvNyHLkN6Ln9GBUZi9Xqkor%2BoUDVrBbWCvcnEPvO7hBwqgbn%2Bx45ste2qjbyPxtXecN7etc0lQ1UeDuoUS1VJ%2FLSR5O8XkwmlhRpCjy55gWd4EYzloimIuyWwOhZNjbj3TYElBSVK0i2Y7F5yjc0OwEdzxR8AVfNDBYxcBZIuzUSj6X6txH1wuPL3zGGwvhtthshpODTd2tKc2wVIWI3qbrCUv5w%2FKKEYeJ4%2F7YSSEV4yt7YW5CT77huxkNT%2BF%2BZYqN1aDx5%2FaKi3vDqcp64Tew6airU7gea6H5eSaJjBIcndHe2wL3MOOj9LwGOqUBUqoXV9l5McIrLvAJRqiIU3UlWIerKhKdaSpYCz4%2BhEcTMkB3b%2BnZCoSuKqQjgdtQHBbXwb4oKN%2BFldnXKuS9FElFeYAfISJ%2FbsQYo%2FfZccSCBukaKWU14nqJImlhzl0onSQmmszO%2FwqAP0F8Vx63ch14I4txEjShiqa9YF%2B2kosIL1RrhpruSBFLPCf5SHYpx4jnX2BkjpKIQxuERRhKw1pCqMEh&X-Amz-Signature=1916f5b6fa51a52673a460d7597ee59139fc264c7f345a766410858a3c20ae5c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627Q72RPT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBf4doei%2FNbZEr4obgtvcoxldXimaH3GZoaEC0SNqgrcAiEA1v32jdkCqs3uQwwfT3BrYx5bvb2H5ovFwmLCrC1XMtsqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFv1ALP5l1LIyVDJLCrcA5skVH6Cs8KckNUwAko4j93icj0cSoG8CiRXEp87KXfQp5fwpCUJweyTdmcGFXT3YK74G8HmSlKQrL1GRAsrUwjPZWdpwGwWMcX%2FN9oBwoxbPn373JDUXqrVhDZVR28Xps3Xyj%2BgOAgHn9Oy33O5PP6olXCjVCCMRJ%2Bwd6VphoMtER%2FphrDy8LvO4N71G3XO%2By5Dl3tJxkO%2FO06Ja11gMrtuPudRaTCLlQlluvzn0o3Wy4lwuLfd68gB042FWmVU%2Fr6YsZx16fDpxzesUqT6%2F4h2E8UCvtBlQUMJqCJxa7pAI1gycDvdckklixT%2BT2hyyKgQoYbqdYvNyHLkN6Ln9GBUZi9Xqkor%2BoUDVrBbWCvcnEPvO7hBwqgbn%2Bx45ste2qjbyPxtXecN7etc0lQ1UeDuoUS1VJ%2FLSR5O8XkwmlhRpCjy55gWd4EYzloimIuyWwOhZNjbj3TYElBSVK0i2Y7F5yjc0OwEdzxR8AVfNDBYxcBZIuzUSj6X6txH1wuPL3zGGwvhtthshpODTd2tKc2wVIWI3qbrCUv5w%2FKKEYeJ4%2F7YSSEV4yt7YW5CT77huxkNT%2BF%2BZYqN1aDx5%2FaKi3vDqcp64Tew6airU7gea6H5eSaJjBIcndHe2wL3MOOj9LwGOqUBUqoXV9l5McIrLvAJRqiIU3UlWIerKhKdaSpYCz4%2BhEcTMkB3b%2BnZCoSuKqQjgdtQHBbXwb4oKN%2BFldnXKuS9FElFeYAfISJ%2FbsQYo%2FfZccSCBukaKWU14nqJImlhzl0onSQmmszO%2FwqAP0F8Vx63ch14I4txEjShiqa9YF%2B2kosIL1RrhpruSBFLPCf5SHYpx4jnX2BkjpKIQxuERRhKw1pCqMEh&X-Amz-Signature=9cc100ddcc359ec5482e31e4f6ab8d1da4ab599a3c3f3301c2c5597fd55c35e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627Q72RPT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBf4doei%2FNbZEr4obgtvcoxldXimaH3GZoaEC0SNqgrcAiEA1v32jdkCqs3uQwwfT3BrYx5bvb2H5ovFwmLCrC1XMtsqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFv1ALP5l1LIyVDJLCrcA5skVH6Cs8KckNUwAko4j93icj0cSoG8CiRXEp87KXfQp5fwpCUJweyTdmcGFXT3YK74G8HmSlKQrL1GRAsrUwjPZWdpwGwWMcX%2FN9oBwoxbPn373JDUXqrVhDZVR28Xps3Xyj%2BgOAgHn9Oy33O5PP6olXCjVCCMRJ%2Bwd6VphoMtER%2FphrDy8LvO4N71G3XO%2By5Dl3tJxkO%2FO06Ja11gMrtuPudRaTCLlQlluvzn0o3Wy4lwuLfd68gB042FWmVU%2Fr6YsZx16fDpxzesUqT6%2F4h2E8UCvtBlQUMJqCJxa7pAI1gycDvdckklixT%2BT2hyyKgQoYbqdYvNyHLkN6Ln9GBUZi9Xqkor%2BoUDVrBbWCvcnEPvO7hBwqgbn%2Bx45ste2qjbyPxtXecN7etc0lQ1UeDuoUS1VJ%2FLSR5O8XkwmlhRpCjy55gWd4EYzloimIuyWwOhZNjbj3TYElBSVK0i2Y7F5yjc0OwEdzxR8AVfNDBYxcBZIuzUSj6X6txH1wuPL3zGGwvhtthshpODTd2tKc2wVIWI3qbrCUv5w%2FKKEYeJ4%2F7YSSEV4yt7YW5CT77huxkNT%2BF%2BZYqN1aDx5%2FaKi3vDqcp64Tew6airU7gea6H5eSaJjBIcndHe2wL3MOOj9LwGOqUBUqoXV9l5McIrLvAJRqiIU3UlWIerKhKdaSpYCz4%2BhEcTMkB3b%2BnZCoSuKqQjgdtQHBbXwb4oKN%2BFldnXKuS9FElFeYAfISJ%2FbsQYo%2FfZccSCBukaKWU14nqJImlhzl0onSQmmszO%2FwqAP0F8Vx63ch14I4txEjShiqa9YF%2B2kosIL1RrhpruSBFLPCf5SHYpx4jnX2BkjpKIQxuERRhKw1pCqMEh&X-Amz-Signature=9451be8e5eb1e4d5814800b8230133d20461a3f5675ca42b243e2685684ecb61&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627Q72RPT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBf4doei%2FNbZEr4obgtvcoxldXimaH3GZoaEC0SNqgrcAiEA1v32jdkCqs3uQwwfT3BrYx5bvb2H5ovFwmLCrC1XMtsqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFv1ALP5l1LIyVDJLCrcA5skVH6Cs8KckNUwAko4j93icj0cSoG8CiRXEp87KXfQp5fwpCUJweyTdmcGFXT3YK74G8HmSlKQrL1GRAsrUwjPZWdpwGwWMcX%2FN9oBwoxbPn373JDUXqrVhDZVR28Xps3Xyj%2BgOAgHn9Oy33O5PP6olXCjVCCMRJ%2Bwd6VphoMtER%2FphrDy8LvO4N71G3XO%2By5Dl3tJxkO%2FO06Ja11gMrtuPudRaTCLlQlluvzn0o3Wy4lwuLfd68gB042FWmVU%2Fr6YsZx16fDpxzesUqT6%2F4h2E8UCvtBlQUMJqCJxa7pAI1gycDvdckklixT%2BT2hyyKgQoYbqdYvNyHLkN6Ln9GBUZi9Xqkor%2BoUDVrBbWCvcnEPvO7hBwqgbn%2Bx45ste2qjbyPxtXecN7etc0lQ1UeDuoUS1VJ%2FLSR5O8XkwmlhRpCjy55gWd4EYzloimIuyWwOhZNjbj3TYElBSVK0i2Y7F5yjc0OwEdzxR8AVfNDBYxcBZIuzUSj6X6txH1wuPL3zGGwvhtthshpODTd2tKc2wVIWI3qbrCUv5w%2FKKEYeJ4%2F7YSSEV4yt7YW5CT77huxkNT%2BF%2BZYqN1aDx5%2FaKi3vDqcp64Tew6airU7gea6H5eSaJjBIcndHe2wL3MOOj9LwGOqUBUqoXV9l5McIrLvAJRqiIU3UlWIerKhKdaSpYCz4%2BhEcTMkB3b%2BnZCoSuKqQjgdtQHBbXwb4oKN%2BFldnXKuS9FElFeYAfISJ%2FbsQYo%2FfZccSCBukaKWU14nqJImlhzl0onSQmmszO%2FwqAP0F8Vx63ch14I4txEjShiqa9YF%2B2kosIL1RrhpruSBFLPCf5SHYpx4jnX2BkjpKIQxuERRhKw1pCqMEh&X-Amz-Signature=305b8d92048c55dfbcbf93af4a061d16ab430db7ac7fe0bcfc9acc33afef9bf9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627Q72RPT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBf4doei%2FNbZEr4obgtvcoxldXimaH3GZoaEC0SNqgrcAiEA1v32jdkCqs3uQwwfT3BrYx5bvb2H5ovFwmLCrC1XMtsqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFv1ALP5l1LIyVDJLCrcA5skVH6Cs8KckNUwAko4j93icj0cSoG8CiRXEp87KXfQp5fwpCUJweyTdmcGFXT3YK74G8HmSlKQrL1GRAsrUwjPZWdpwGwWMcX%2FN9oBwoxbPn373JDUXqrVhDZVR28Xps3Xyj%2BgOAgHn9Oy33O5PP6olXCjVCCMRJ%2Bwd6VphoMtER%2FphrDy8LvO4N71G3XO%2By5Dl3tJxkO%2FO06Ja11gMrtuPudRaTCLlQlluvzn0o3Wy4lwuLfd68gB042FWmVU%2Fr6YsZx16fDpxzesUqT6%2F4h2E8UCvtBlQUMJqCJxa7pAI1gycDvdckklixT%2BT2hyyKgQoYbqdYvNyHLkN6Ln9GBUZi9Xqkor%2BoUDVrBbWCvcnEPvO7hBwqgbn%2Bx45ste2qjbyPxtXecN7etc0lQ1UeDuoUS1VJ%2FLSR5O8XkwmlhRpCjy55gWd4EYzloimIuyWwOhZNjbj3TYElBSVK0i2Y7F5yjc0OwEdzxR8AVfNDBYxcBZIuzUSj6X6txH1wuPL3zGGwvhtthshpODTd2tKc2wVIWI3qbrCUv5w%2FKKEYeJ4%2F7YSSEV4yt7YW5CT77huxkNT%2BF%2BZYqN1aDx5%2FaKi3vDqcp64Tew6airU7gea6H5eSaJjBIcndHe2wL3MOOj9LwGOqUBUqoXV9l5McIrLvAJRqiIU3UlWIerKhKdaSpYCz4%2BhEcTMkB3b%2BnZCoSuKqQjgdtQHBbXwb4oKN%2BFldnXKuS9FElFeYAfISJ%2FbsQYo%2FfZccSCBukaKWU14nqJImlhzl0onSQmmszO%2FwqAP0F8Vx63ch14I4txEjShiqa9YF%2B2kosIL1RrhpruSBFLPCf5SHYpx4jnX2BkjpKIQxuERRhKw1pCqMEh&X-Amz-Signature=87a2c35b3a73c37d70adde0aba859ee6ad2b4e1d577b166145f7a83a18135e24&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627Q72RPT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBf4doei%2FNbZEr4obgtvcoxldXimaH3GZoaEC0SNqgrcAiEA1v32jdkCqs3uQwwfT3BrYx5bvb2H5ovFwmLCrC1XMtsqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFv1ALP5l1LIyVDJLCrcA5skVH6Cs8KckNUwAko4j93icj0cSoG8CiRXEp87KXfQp5fwpCUJweyTdmcGFXT3YK74G8HmSlKQrL1GRAsrUwjPZWdpwGwWMcX%2FN9oBwoxbPn373JDUXqrVhDZVR28Xps3Xyj%2BgOAgHn9Oy33O5PP6olXCjVCCMRJ%2Bwd6VphoMtER%2FphrDy8LvO4N71G3XO%2By5Dl3tJxkO%2FO06Ja11gMrtuPudRaTCLlQlluvzn0o3Wy4lwuLfd68gB042FWmVU%2Fr6YsZx16fDpxzesUqT6%2F4h2E8UCvtBlQUMJqCJxa7pAI1gycDvdckklixT%2BT2hyyKgQoYbqdYvNyHLkN6Ln9GBUZi9Xqkor%2BoUDVrBbWCvcnEPvO7hBwqgbn%2Bx45ste2qjbyPxtXecN7etc0lQ1UeDuoUS1VJ%2FLSR5O8XkwmlhRpCjy55gWd4EYzloimIuyWwOhZNjbj3TYElBSVK0i2Y7F5yjc0OwEdzxR8AVfNDBYxcBZIuzUSj6X6txH1wuPL3zGGwvhtthshpODTd2tKc2wVIWI3qbrCUv5w%2FKKEYeJ4%2F7YSSEV4yt7YW5CT77huxkNT%2BF%2BZYqN1aDx5%2FaKi3vDqcp64Tew6airU7gea6H5eSaJjBIcndHe2wL3MOOj9LwGOqUBUqoXV9l5McIrLvAJRqiIU3UlWIerKhKdaSpYCz4%2BhEcTMkB3b%2BnZCoSuKqQjgdtQHBbXwb4oKN%2BFldnXKuS9FElFeYAfISJ%2FbsQYo%2FfZccSCBukaKWU14nqJImlhzl0onSQmmszO%2FwqAP0F8Vx63ch14I4txEjShiqa9YF%2B2kosIL1RrhpruSBFLPCf5SHYpx4jnX2BkjpKIQxuERRhKw1pCqMEh&X-Amz-Signature=a8d4e0718babf4841520f17d95cc84dbc029c204534633aa58219de0ab7c2d73&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBM2ZBZF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2BNWj6oyw1zg44C2brra0HvSoYRbiseVMh17lnrsE3oAiAmVyrzBr1IEyInJg2%2BODDbw5%2FJ1cW4mGoCM9rECgjM4iqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjbfBBGsu8mvd%2BRzMKtwDuV%2FQD9OoDfx2ycUGzKDvWiGlutIUhcmeTKMtGZ2sbyW75tw1mVGH5aokCGscNajvzMG0LlfbZV6AzOVcYyg%2FhTpLNj3zrpmMAlXxKFIsDqvUpn9%2BBo6kaIidB71rBDTgSnY2RwA%2Frttx0i5w%2B7fbvvUfcJCoP%2BtYKYwviePpTHHT1XXfdZPTfIrJbzBwcmxVUAwzZJQE2Xzj4f1MrRhhNtcdDru6Ht9v3SD07GhbMgneZB0W8IZ9UX7KrZ3vNlc5fnCW2GpHe4Oi1TH4w2qFUQBiquZ11NSbxUgLwKn0nX%2BwegCVYExvvOovoxrVbUtW9ijbgcGv8%2FQcSrrUIkFuCFMFwXv%2F1IuahnwcjF8syuADTAQRUA7Df0ofhUSFMZCpIbjWpAIflTSYy2gnwHJ6g%2F5sy7gckh%2Fj8q6v3ALmHoxYmv%2BOUbHjUaTDWamvvCf%2BZimkuH3WLmV8ZxhHPyfixH272wrMARguXKytD35rVaQfV02hs0eRtn9kclIOsPfKRmxWc%2BYrGExkJxdQDsT4oqCezNw0IfOMo2iiK7JAtBZsWkEYk5KL0GC2nKE69qdCG4%2FMfVLnBEJtpj1ltYLlC%2Bqe6ti0%2F3iakVY1hnKCaKXthVHezh9Xf01WTCgw6KP0vAY6pgGNeLLT4CWiQbWSL8aoXCv3yyk1TX5%2FmBePV631KbzbkS1BPAyI1JMYizwIx7tg4HGx9MPz5MQue4zv7Jcmb3QRH8ZW%2BbEI0%2BeKZP3Y6kNVla7y3ImQPz79%2FQR7GoviDY8FPMN4hDKlo02s5oV5MAc5uGfAl2K9u%2By5R9J5pHgfbm04HBDzLH0msSbIzmp19RcabDHAP2LcQvcGXV6fziXw9%2BwkpwVz&X-Amz-Signature=73f8270e5c1810c3ebddf8eb857d2d8a88a617b91669986b651765f29318dc16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHG27UQN%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBclYAk8KfkEKY5xzmHuJS4ntJd2%2BR55HmHv00Q2Wk6PAiEA5x3H%2B%2BJdGTWoOl7ofcyNfcFGJ1whLqxL%2FlSujEH0%2Bx8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLv4KkF%2FW6Exz92MJCrcA0HQKPzoMf44Y1BWnugULxAEi4OacXsZ5JxiQJEd%2Fgk%2BOf%2F4zcywbXjRPUi6%2F%2BVFU61SzjpGcXREr1XlVyIe7EKRNiGG4dkH4mV1iXProy5qBLm7%2BinsICx9NaYmyJEpw9WDBYF%2BJAb1M9zN6d67iSTxVK1G9E1FSpHoS6sfNW0eEX9XVQiyK6fjuzAtjPIj%2FaoB55bgIj%2FVQ4jot7hyhVGZC7z%2F6A3QkaGW2SzFRAw9QF%2BO8jj%2B3OVtBHWQ53rKCzxhvjBsOTIPiS%2BT1UEWshk%2FMRNRgVKVhS3QObnM%2FWj8orZV3h4O71sanmYOpTw1ASuwt5E%2Bu8g%2BfVfERXbqezagZVf77NbE%2F1dEfoaUfIcdo0NtcU0Bb%2Fq5HuCITrwjG7UTU9WpRpz6fuYzhQJWd6lDG8v1RhaJ6qLfQ2U2HMKNpo50bKvI7JD9KlewhO8FWZvS%2Fn2S49G0rifmbOGSfY1mb%2FiQNV1cfInimU73mkw%2BEx7BOUAuV8BJmFqke4njMvwZPZwUZrHNqyPv7HMsj8KaW7wOZcylOTx3QmGtSMXKUWBt0oUsJkwJtiyyr2%2FLek9xav6zRfkQyp50L5uWKYptVSoYWSZk2qgVHkhrwP9zEmEmuLwB%2BCNgm2cyMIKk9LwGOqUBL8uudhWKQCM7INOKl1Sj2HvjWdfYWmWIwFbRVh%2FHaCSJg3CIlcFV%2BUMbIFrUv47vqTjlnWhfGWKNnpbWZe0u9KERlB7HC%2FuKoqV8Sf6dgG5o4itzDL1AGOdDajpTOeBX0qsMldAcWAr%2BWc0gMzQ%2FL1kfZiFpkvj7M9%2BLO10vMTZSz0daZYP26xrLsMvjO0u3%2B7kvgDdHSGMat8JoAuNcPe1xAqpH&X-Amz-Signature=a666e94134aae8c9606f87f04bbb24e2cff9ea1c564cf6203e0207d087429a03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MSHMZ7S%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEVFeg1ATURvUPApIuE3rWVkpAxoxpFUaYzUFoMnxEaCAiAs%2FKZ5ruDzMSgUeAKVaS2HA6H3h1nNut4L7JklqAP6QSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMefA0L0r%2FsbBkMVUqKtwDBckatk%2F2T33%2BmE4G%2B2O3mOEMC4MD476nT1kikx1rzZfa%2B9bFplWkVUeepng3d5pxwJyLzAUodttmHhYb%2BGEqo0GlUxekuEVsomi%2FHtQW89PHMWD7KkKvxKxiIBv31MfG%2FSkjPbFzxBt%2BiqjtZ%2FnVEY37aZNy0jT%2FXcCyrvVaE9aOQdHTwEjS%2BaChziMfhmXrDgi412X7FdRkFHABf9lC7RGWEYoi3Xxm%2F5BuPiIo4p835YYBobIr7l2FDc6btglMDjGNfF5wPgGxP1RI503hfjYGGvbc8DTruQJv1caBl4BUY%2FRdzPPHSo%2FYX8OabsayywfjuitLXzSkP6g%2B9WYMYNEFPJxeRI5Tn53Bn95W17MDYdMEPplXQ5XpFhKwzAFY3wLj5cIurQQV59%2B172AzAOflUqeDjhqBUfz6JeWdlVy5lhn9qlkhiNRA3%2B5McVuhTqmosV12tXlv14zEc57SrMIDVW3g2g5s6A3drjRWzXDZ5RdtcVdPBvJ%2B%2Fx8UHbOb3VS1CncGnm2HV4cwHPXTQziFLm3pvQMwg0qchFgXhlgHSiEcjezHeRII6ny5TKWM1YmQLxVphcafZFwgBDmZ0XSY09MHjjmDzisR6vqXtuRYFsifYTgCNKJ1ZOMw5KP0vAY6pgH6DiOsN5Bk4UJx%2B0aDLukH%2Bave7DVl7u7QaBkGD1O07gsxoTQ5ojTdSuKKxLwJdtpLLhHEB2bmcckUwNys1KgU2MYvGzTrkMdi9bEzZpBk%2F1eit8spItdvNZrXLUtYsY%2BHI%2F%2BOqML%2FeEbAkb3ytQPpXhmZDEW6x0qQjOfqNchT2M%2BSgQbzFP9l2M1Dpha8F7bbhisPqDrdkciJz8yC1HPSDr3Ne2%2Fh&X-Amz-Signature=b8fb316e3bc7bba617cb01d4e8e5ab112094b5c7c4a3fb3d225ac9b2100be4c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MSHMZ7S%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T181935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEVFeg1ATURvUPApIuE3rWVkpAxoxpFUaYzUFoMnxEaCAiAs%2FKZ5ruDzMSgUeAKVaS2HA6H3h1nNut4L7JklqAP6QSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMefA0L0r%2FsbBkMVUqKtwDBckatk%2F2T33%2BmE4G%2B2O3mOEMC4MD476nT1kikx1rzZfa%2B9bFplWkVUeepng3d5pxwJyLzAUodttmHhYb%2BGEqo0GlUxekuEVsomi%2FHtQW89PHMWD7KkKvxKxiIBv31MfG%2FSkjPbFzxBt%2BiqjtZ%2FnVEY37aZNy0jT%2FXcCyrvVaE9aOQdHTwEjS%2BaChziMfhmXrDgi412X7FdRkFHABf9lC7RGWEYoi3Xxm%2F5BuPiIo4p835YYBobIr7l2FDc6btglMDjGNfF5wPgGxP1RI503hfjYGGvbc8DTruQJv1caBl4BUY%2FRdzPPHSo%2FYX8OabsayywfjuitLXzSkP6g%2B9WYMYNEFPJxeRI5Tn53Bn95W17MDYdMEPplXQ5XpFhKwzAFY3wLj5cIurQQV59%2B172AzAOflUqeDjhqBUfz6JeWdlVy5lhn9qlkhiNRA3%2B5McVuhTqmosV12tXlv14zEc57SrMIDVW3g2g5s6A3drjRWzXDZ5RdtcVdPBvJ%2B%2Fx8UHbOb3VS1CncGnm2HV4cwHPXTQziFLm3pvQMwg0qchFgXhlgHSiEcjezHeRII6ny5TKWM1YmQLxVphcafZFwgBDmZ0XSY09MHjjmDzisR6vqXtuRYFsifYTgCNKJ1ZOMw5KP0vAY6pgH6DiOsN5Bk4UJx%2B0aDLukH%2Bave7DVl7u7QaBkGD1O07gsxoTQ5ojTdSuKKxLwJdtpLLhHEB2bmcckUwNys1KgU2MYvGzTrkMdi9bEzZpBk%2F1eit8spItdvNZrXLUtYsY%2BHI%2F%2BOqML%2FeEbAkb3ytQPpXhmZDEW6x0qQjOfqNchT2M%2BSgQbzFP9l2M1Dpha8F7bbhisPqDrdkciJz8yC1HPSDr3Ne2%2Fh&X-Amz-Signature=43226502de19f31d3a79c04f437ab878446e2ccb6a4bd561c248197c19a0cfb1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
