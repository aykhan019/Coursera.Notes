

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UTKTNOT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCIGMt4ioP0R9XlaowaSSa8fKEAJVD5llLPJ8g7htQb4wIhANaoZM%2FkYprG1IrhO9uaogGYkuY8jajxxXbaRUvdSR8hKv8DCCoQABoMNjM3NDIzMTgzODA1Igz78qHuiJ2EDZluHw8q3AOn5dPBgfKLnpnwzSN%2B6snY3xQj8m14sk2fyMWulKiq418z3%2FchYsGPHQWTeNeCnecZJDe8BWwkzOwjoq6IpRS7AoUML%2B%2By5%2BO8zNVH5Tui0IsZrQWYjKZq2UL%2BKvyy%2FEKY4O342IeJb503kEr8ZgJ8bu8u%2BERMVRVHFYiW0TNjAFlZApGD8MaVaaXxEfxKIvkDqFm1v8tJJ6kX4pzIMyunw56jfDVNrxnJBiW5lOCbhqMnSNAdBALz93QIl5iKxK7fY3ndf7OoDLejyjTpDPmi6tX9zHHjdmG%2FnKJn0oAa6BEXLWfpJAaQuryWrK8nUmYHJRW3LKNYxaUSrzSuyyPLky050ILdPM5aPgsb8CvUJ2fbMgbZBGupckbRYlmWInKzpILH3JMzpx8xy4BKANRPV5mvKSOk8fmKxRhKzOTfiNDb4ApKJoQZtYTaUKte%2B8%2FKYpT0JutfSyUTZ3Bcq8sodTYbrjNGpdaTtkC4%2FJxjqyZ%2BYDGqua%2BsoVUQcr5hUQvFkMhMZjJByzjwjPmixhwVtGDli2XEmW8dnVjhTW7BvTT6yNdMp6Gp%2FZDwNj3TF8ewag1huebh7BsCmiZG97kLUQSaySFCn3IrVuSgwSnxVBSDCPeR4gRAlMMfZDDOroe9BjqkAVvw%2BR8Pl%2F9tcUp7EpDit3fNfyRTQ1hSg0xp6LBid8oo9X9311q1GdQ%2BnbyXiHdutVlkh0zJ5zazLzoea4JtAEhgAiXOcAnmNHFBOWM8Lj0kPwicfoX6U%2FsXQcVw5H3v8nsgJ6mfBPVaYFyRvCOACRXMnjTvm0IVXTHZ4pK3dH5BSeDGWafdQy9CK29UHhDqnvdHEdns522NxBii6YW3E5BkToXI&X-Amz-Signature=5c1ce04af1745934fa32c9be64b3fbc2a2418994030c436affeaca5f030e7495&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UTKTNOT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCIGMt4ioP0R9XlaowaSSa8fKEAJVD5llLPJ8g7htQb4wIhANaoZM%2FkYprG1IrhO9uaogGYkuY8jajxxXbaRUvdSR8hKv8DCCoQABoMNjM3NDIzMTgzODA1Igz78qHuiJ2EDZluHw8q3AOn5dPBgfKLnpnwzSN%2B6snY3xQj8m14sk2fyMWulKiq418z3%2FchYsGPHQWTeNeCnecZJDe8BWwkzOwjoq6IpRS7AoUML%2B%2By5%2BO8zNVH5Tui0IsZrQWYjKZq2UL%2BKvyy%2FEKY4O342IeJb503kEr8ZgJ8bu8u%2BERMVRVHFYiW0TNjAFlZApGD8MaVaaXxEfxKIvkDqFm1v8tJJ6kX4pzIMyunw56jfDVNrxnJBiW5lOCbhqMnSNAdBALz93QIl5iKxK7fY3ndf7OoDLejyjTpDPmi6tX9zHHjdmG%2FnKJn0oAa6BEXLWfpJAaQuryWrK8nUmYHJRW3LKNYxaUSrzSuyyPLky050ILdPM5aPgsb8CvUJ2fbMgbZBGupckbRYlmWInKzpILH3JMzpx8xy4BKANRPV5mvKSOk8fmKxRhKzOTfiNDb4ApKJoQZtYTaUKte%2B8%2FKYpT0JutfSyUTZ3Bcq8sodTYbrjNGpdaTtkC4%2FJxjqyZ%2BYDGqua%2BsoVUQcr5hUQvFkMhMZjJByzjwjPmixhwVtGDli2XEmW8dnVjhTW7BvTT6yNdMp6Gp%2FZDwNj3TF8ewag1huebh7BsCmiZG97kLUQSaySFCn3IrVuSgwSnxVBSDCPeR4gRAlMMfZDDOroe9BjqkAVvw%2BR8Pl%2F9tcUp7EpDit3fNfyRTQ1hSg0xp6LBid8oo9X9311q1GdQ%2BnbyXiHdutVlkh0zJ5zazLzoea4JtAEhgAiXOcAnmNHFBOWM8Lj0kPwicfoX6U%2FsXQcVw5H3v8nsgJ6mfBPVaYFyRvCOACRXMnjTvm0IVXTHZ4pK3dH5BSeDGWafdQy9CK29UHhDqnvdHEdns522NxBii6YW3E5BkToXI&X-Amz-Signature=dd4b341d7f4bf7ab43b938990c119875a6d2e5f5a7027b8fe88ee02920da2ae0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UTKTNOT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCIGMt4ioP0R9XlaowaSSa8fKEAJVD5llLPJ8g7htQb4wIhANaoZM%2FkYprG1IrhO9uaogGYkuY8jajxxXbaRUvdSR8hKv8DCCoQABoMNjM3NDIzMTgzODA1Igz78qHuiJ2EDZluHw8q3AOn5dPBgfKLnpnwzSN%2B6snY3xQj8m14sk2fyMWulKiq418z3%2FchYsGPHQWTeNeCnecZJDe8BWwkzOwjoq6IpRS7AoUML%2B%2By5%2BO8zNVH5Tui0IsZrQWYjKZq2UL%2BKvyy%2FEKY4O342IeJb503kEr8ZgJ8bu8u%2BERMVRVHFYiW0TNjAFlZApGD8MaVaaXxEfxKIvkDqFm1v8tJJ6kX4pzIMyunw56jfDVNrxnJBiW5lOCbhqMnSNAdBALz93QIl5iKxK7fY3ndf7OoDLejyjTpDPmi6tX9zHHjdmG%2FnKJn0oAa6BEXLWfpJAaQuryWrK8nUmYHJRW3LKNYxaUSrzSuyyPLky050ILdPM5aPgsb8CvUJ2fbMgbZBGupckbRYlmWInKzpILH3JMzpx8xy4BKANRPV5mvKSOk8fmKxRhKzOTfiNDb4ApKJoQZtYTaUKte%2B8%2FKYpT0JutfSyUTZ3Bcq8sodTYbrjNGpdaTtkC4%2FJxjqyZ%2BYDGqua%2BsoVUQcr5hUQvFkMhMZjJByzjwjPmixhwVtGDli2XEmW8dnVjhTW7BvTT6yNdMp6Gp%2FZDwNj3TF8ewag1huebh7BsCmiZG97kLUQSaySFCn3IrVuSgwSnxVBSDCPeR4gRAlMMfZDDOroe9BjqkAVvw%2BR8Pl%2F9tcUp7EpDit3fNfyRTQ1hSg0xp6LBid8oo9X9311q1GdQ%2BnbyXiHdutVlkh0zJ5zazLzoea4JtAEhgAiXOcAnmNHFBOWM8Lj0kPwicfoX6U%2FsXQcVw5H3v8nsgJ6mfBPVaYFyRvCOACRXMnjTvm0IVXTHZ4pK3dH5BSeDGWafdQy9CK29UHhDqnvdHEdns522NxBii6YW3E5BkToXI&X-Amz-Signature=20e24ab62ca8b162d972c5630829d5a547f0da774c5c06bd8b36ee646d10f3a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UTKTNOT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCIGMt4ioP0R9XlaowaSSa8fKEAJVD5llLPJ8g7htQb4wIhANaoZM%2FkYprG1IrhO9uaogGYkuY8jajxxXbaRUvdSR8hKv8DCCoQABoMNjM3NDIzMTgzODA1Igz78qHuiJ2EDZluHw8q3AOn5dPBgfKLnpnwzSN%2B6snY3xQj8m14sk2fyMWulKiq418z3%2FchYsGPHQWTeNeCnecZJDe8BWwkzOwjoq6IpRS7AoUML%2B%2By5%2BO8zNVH5Tui0IsZrQWYjKZq2UL%2BKvyy%2FEKY4O342IeJb503kEr8ZgJ8bu8u%2BERMVRVHFYiW0TNjAFlZApGD8MaVaaXxEfxKIvkDqFm1v8tJJ6kX4pzIMyunw56jfDVNrxnJBiW5lOCbhqMnSNAdBALz93QIl5iKxK7fY3ndf7OoDLejyjTpDPmi6tX9zHHjdmG%2FnKJn0oAa6BEXLWfpJAaQuryWrK8nUmYHJRW3LKNYxaUSrzSuyyPLky050ILdPM5aPgsb8CvUJ2fbMgbZBGupckbRYlmWInKzpILH3JMzpx8xy4BKANRPV5mvKSOk8fmKxRhKzOTfiNDb4ApKJoQZtYTaUKte%2B8%2FKYpT0JutfSyUTZ3Bcq8sodTYbrjNGpdaTtkC4%2FJxjqyZ%2BYDGqua%2BsoVUQcr5hUQvFkMhMZjJByzjwjPmixhwVtGDli2XEmW8dnVjhTW7BvTT6yNdMp6Gp%2FZDwNj3TF8ewag1huebh7BsCmiZG97kLUQSaySFCn3IrVuSgwSnxVBSDCPeR4gRAlMMfZDDOroe9BjqkAVvw%2BR8Pl%2F9tcUp7EpDit3fNfyRTQ1hSg0xp6LBid8oo9X9311q1GdQ%2BnbyXiHdutVlkh0zJ5zazLzoea4JtAEhgAiXOcAnmNHFBOWM8Lj0kPwicfoX6U%2FsXQcVw5H3v8nsgJ6mfBPVaYFyRvCOACRXMnjTvm0IVXTHZ4pK3dH5BSeDGWafdQy9CK29UHhDqnvdHEdns522NxBii6YW3E5BkToXI&X-Amz-Signature=bc43d39f306eb196168bf297f0ef11edd1794b0a3098355be102025a27fd1b45&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UTKTNOT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCIGMt4ioP0R9XlaowaSSa8fKEAJVD5llLPJ8g7htQb4wIhANaoZM%2FkYprG1IrhO9uaogGYkuY8jajxxXbaRUvdSR8hKv8DCCoQABoMNjM3NDIzMTgzODA1Igz78qHuiJ2EDZluHw8q3AOn5dPBgfKLnpnwzSN%2B6snY3xQj8m14sk2fyMWulKiq418z3%2FchYsGPHQWTeNeCnecZJDe8BWwkzOwjoq6IpRS7AoUML%2B%2By5%2BO8zNVH5Tui0IsZrQWYjKZq2UL%2BKvyy%2FEKY4O342IeJb503kEr8ZgJ8bu8u%2BERMVRVHFYiW0TNjAFlZApGD8MaVaaXxEfxKIvkDqFm1v8tJJ6kX4pzIMyunw56jfDVNrxnJBiW5lOCbhqMnSNAdBALz93QIl5iKxK7fY3ndf7OoDLejyjTpDPmi6tX9zHHjdmG%2FnKJn0oAa6BEXLWfpJAaQuryWrK8nUmYHJRW3LKNYxaUSrzSuyyPLky050ILdPM5aPgsb8CvUJ2fbMgbZBGupckbRYlmWInKzpILH3JMzpx8xy4BKANRPV5mvKSOk8fmKxRhKzOTfiNDb4ApKJoQZtYTaUKte%2B8%2FKYpT0JutfSyUTZ3Bcq8sodTYbrjNGpdaTtkC4%2FJxjqyZ%2BYDGqua%2BsoVUQcr5hUQvFkMhMZjJByzjwjPmixhwVtGDli2XEmW8dnVjhTW7BvTT6yNdMp6Gp%2FZDwNj3TF8ewag1huebh7BsCmiZG97kLUQSaySFCn3IrVuSgwSnxVBSDCPeR4gRAlMMfZDDOroe9BjqkAVvw%2BR8Pl%2F9tcUp7EpDit3fNfyRTQ1hSg0xp6LBid8oo9X9311q1GdQ%2BnbyXiHdutVlkh0zJ5zazLzoea4JtAEhgAiXOcAnmNHFBOWM8Lj0kPwicfoX6U%2FsXQcVw5H3v8nsgJ6mfBPVaYFyRvCOACRXMnjTvm0IVXTHZ4pK3dH5BSeDGWafdQy9CK29UHhDqnvdHEdns522NxBii6YW3E5BkToXI&X-Amz-Signature=514b829615358b8b66981ccc0e619b8632d23b03ca9956df56d5401d837d3af5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UTKTNOT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCIGMt4ioP0R9XlaowaSSa8fKEAJVD5llLPJ8g7htQb4wIhANaoZM%2FkYprG1IrhO9uaogGYkuY8jajxxXbaRUvdSR8hKv8DCCoQABoMNjM3NDIzMTgzODA1Igz78qHuiJ2EDZluHw8q3AOn5dPBgfKLnpnwzSN%2B6snY3xQj8m14sk2fyMWulKiq418z3%2FchYsGPHQWTeNeCnecZJDe8BWwkzOwjoq6IpRS7AoUML%2B%2By5%2BO8zNVH5Tui0IsZrQWYjKZq2UL%2BKvyy%2FEKY4O342IeJb503kEr8ZgJ8bu8u%2BERMVRVHFYiW0TNjAFlZApGD8MaVaaXxEfxKIvkDqFm1v8tJJ6kX4pzIMyunw56jfDVNrxnJBiW5lOCbhqMnSNAdBALz93QIl5iKxK7fY3ndf7OoDLejyjTpDPmi6tX9zHHjdmG%2FnKJn0oAa6BEXLWfpJAaQuryWrK8nUmYHJRW3LKNYxaUSrzSuyyPLky050ILdPM5aPgsb8CvUJ2fbMgbZBGupckbRYlmWInKzpILH3JMzpx8xy4BKANRPV5mvKSOk8fmKxRhKzOTfiNDb4ApKJoQZtYTaUKte%2B8%2FKYpT0JutfSyUTZ3Bcq8sodTYbrjNGpdaTtkC4%2FJxjqyZ%2BYDGqua%2BsoVUQcr5hUQvFkMhMZjJByzjwjPmixhwVtGDli2XEmW8dnVjhTW7BvTT6yNdMp6Gp%2FZDwNj3TF8ewag1huebh7BsCmiZG97kLUQSaySFCn3IrVuSgwSnxVBSDCPeR4gRAlMMfZDDOroe9BjqkAVvw%2BR8Pl%2F9tcUp7EpDit3fNfyRTQ1hSg0xp6LBid8oo9X9311q1GdQ%2BnbyXiHdutVlkh0zJ5zazLzoea4JtAEhgAiXOcAnmNHFBOWM8Lj0kPwicfoX6U%2FsXQcVw5H3v8nsgJ6mfBPVaYFyRvCOACRXMnjTvm0IVXTHZ4pK3dH5BSeDGWafdQy9CK29UHhDqnvdHEdns522NxBii6YW3E5BkToXI&X-Amz-Signature=323d76516f0eb3d327fa1da21f211e2bc413a9f3b0f23769e5c36e77215fd033&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UTKTNOT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCIGMt4ioP0R9XlaowaSSa8fKEAJVD5llLPJ8g7htQb4wIhANaoZM%2FkYprG1IrhO9uaogGYkuY8jajxxXbaRUvdSR8hKv8DCCoQABoMNjM3NDIzMTgzODA1Igz78qHuiJ2EDZluHw8q3AOn5dPBgfKLnpnwzSN%2B6snY3xQj8m14sk2fyMWulKiq418z3%2FchYsGPHQWTeNeCnecZJDe8BWwkzOwjoq6IpRS7AoUML%2B%2By5%2BO8zNVH5Tui0IsZrQWYjKZq2UL%2BKvyy%2FEKY4O342IeJb503kEr8ZgJ8bu8u%2BERMVRVHFYiW0TNjAFlZApGD8MaVaaXxEfxKIvkDqFm1v8tJJ6kX4pzIMyunw56jfDVNrxnJBiW5lOCbhqMnSNAdBALz93QIl5iKxK7fY3ndf7OoDLejyjTpDPmi6tX9zHHjdmG%2FnKJn0oAa6BEXLWfpJAaQuryWrK8nUmYHJRW3LKNYxaUSrzSuyyPLky050ILdPM5aPgsb8CvUJ2fbMgbZBGupckbRYlmWInKzpILH3JMzpx8xy4BKANRPV5mvKSOk8fmKxRhKzOTfiNDb4ApKJoQZtYTaUKte%2B8%2FKYpT0JutfSyUTZ3Bcq8sodTYbrjNGpdaTtkC4%2FJxjqyZ%2BYDGqua%2BsoVUQcr5hUQvFkMhMZjJByzjwjPmixhwVtGDli2XEmW8dnVjhTW7BvTT6yNdMp6Gp%2FZDwNj3TF8ewag1huebh7BsCmiZG97kLUQSaySFCn3IrVuSgwSnxVBSDCPeR4gRAlMMfZDDOroe9BjqkAVvw%2BR8Pl%2F9tcUp7EpDit3fNfyRTQ1hSg0xp6LBid8oo9X9311q1GdQ%2BnbyXiHdutVlkh0zJ5zazLzoea4JtAEhgAiXOcAnmNHFBOWM8Lj0kPwicfoX6U%2FsXQcVw5H3v8nsgJ6mfBPVaYFyRvCOACRXMnjTvm0IVXTHZ4pK3dH5BSeDGWafdQy9CK29UHhDqnvdHEdns522NxBii6YW3E5BkToXI&X-Amz-Signature=2c2bc72d7d3a2ada1f4c5dd925b5b8d823c38aebea7fc06c6a4ff53970e0ded7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UTKTNOT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCIGMt4ioP0R9XlaowaSSa8fKEAJVD5llLPJ8g7htQb4wIhANaoZM%2FkYprG1IrhO9uaogGYkuY8jajxxXbaRUvdSR8hKv8DCCoQABoMNjM3NDIzMTgzODA1Igz78qHuiJ2EDZluHw8q3AOn5dPBgfKLnpnwzSN%2B6snY3xQj8m14sk2fyMWulKiq418z3%2FchYsGPHQWTeNeCnecZJDe8BWwkzOwjoq6IpRS7AoUML%2B%2By5%2BO8zNVH5Tui0IsZrQWYjKZq2UL%2BKvyy%2FEKY4O342IeJb503kEr8ZgJ8bu8u%2BERMVRVHFYiW0TNjAFlZApGD8MaVaaXxEfxKIvkDqFm1v8tJJ6kX4pzIMyunw56jfDVNrxnJBiW5lOCbhqMnSNAdBALz93QIl5iKxK7fY3ndf7OoDLejyjTpDPmi6tX9zHHjdmG%2FnKJn0oAa6BEXLWfpJAaQuryWrK8nUmYHJRW3LKNYxaUSrzSuyyPLky050ILdPM5aPgsb8CvUJ2fbMgbZBGupckbRYlmWInKzpILH3JMzpx8xy4BKANRPV5mvKSOk8fmKxRhKzOTfiNDb4ApKJoQZtYTaUKte%2B8%2FKYpT0JutfSyUTZ3Bcq8sodTYbrjNGpdaTtkC4%2FJxjqyZ%2BYDGqua%2BsoVUQcr5hUQvFkMhMZjJByzjwjPmixhwVtGDli2XEmW8dnVjhTW7BvTT6yNdMp6Gp%2FZDwNj3TF8ewag1huebh7BsCmiZG97kLUQSaySFCn3IrVuSgwSnxVBSDCPeR4gRAlMMfZDDOroe9BjqkAVvw%2BR8Pl%2F9tcUp7EpDit3fNfyRTQ1hSg0xp6LBid8oo9X9311q1GdQ%2BnbyXiHdutVlkh0zJ5zazLzoea4JtAEhgAiXOcAnmNHFBOWM8Lj0kPwicfoX6U%2FsXQcVw5H3v8nsgJ6mfBPVaYFyRvCOACRXMnjTvm0IVXTHZ4pK3dH5BSeDGWafdQy9CK29UHhDqnvdHEdns522NxBii6YW3E5BkToXI&X-Amz-Signature=bdc246e308b2a67f8a74d427389a99977500e8a897c51c746f45e553a973f14e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667S4WDTHR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIF2GphEg%2FUaX7Gj9dFtiKGyixGC%2F7eKk8fQDZ%2B6BtLQUAiEAgtV9deH3RWemfBDiRDI14kHdrd%2BKxaSXJRJ13yQpRKsq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDODHIdfcGfRrFHfi7SrcAyoNZS6CtaMcd0cLK%2F1Pd%2FTd9isJqeruRs8wPF%2B8Lo6kwzerBZH6PDd1TA%2BwRu0LH043x0CK1gSEaZWawdyqSqQTq8N%2FskEkcfvzsPYujEfz2qBwC6QWeXKbapNqk4YykAoGmE3dxNqAamZg655IeMCZ0jTt%2BYaklJHd8sQYAHM%2BzbzQjj5DTbt1kLYgbtmnORtV1mQV4E6l2%2B1CV2qWYKVZvGyFaDYsWMXN5RQ1jDnorLhUB5aFpWKgAInHZfNMY9Te2CtrwvG7YZDuuKrEoY5KzKgZMZXSi5t5lNcUp5UwJKjW87y8YXY8ACm%2FDqkWTBS1RS3nnzsei6CD%2FMH%2BXHcaEIY7FXA0RuFkXGXSr1ktUrn%2FaJRVwtNj3OEfAWsL6oNGIR0Ugt2qm2taQ9Uz%2Bm59iWrjFZrmXTLkmEjl4VLHrG92FeUPQ2Wqeb1Eq9yY9qonicsTnU5My%2FPzdTSZ3N2NYf7CSEhW4ps2S3MKPHDmLa2%2FbRm3sb3xYEmmbKurwMY417%2Bl9TT%2F%2FCcMzSaJdXj6R0rDCd3KxK%2BDiAU1xXXTg1NHH8cxslDR6npwjf5ylRTQA8QUBLR6WvW07hyem2Tkqppnv%2F0JYaWWHs9uBc4riT0Y0qo9V2ypn%2BuQMJOuh70GOqUBpqPJwRXRz4HAfZOF01ONllMb5H5VbhVg0Jvjfj%2FfVahH77mOQwDz7%2FvM1szB3JGfWecW%2B88NdMWikeeYCo0y9ps3yHd3dBMIcP1EgTe3od8YqOBX6fzkqEYPIg7ZZSXDx4SqY7bEuj66CdVFpdYh3YnMqFzBFgjvKyyAlHQx9VHBQm1dyaYV9jGu%2Fd9Sha%2BQ5mCPkimhCzwAyVs5SWmFX6ST67xa&X-Amz-Signature=ffdcd334336e06b22afc271702b3ea22557f98f067cba67eff780d3653cc1bfe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPNEY4LE%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIChMeCNH1Xxqi2rgtizkUvkgzL5r8Sxij2uWX3BMkmbsAiEA%2F563rUWBRZWOtE501WmRY2nYObXadH6c7H8NIG6wiA0q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDJvpxyh8fUlDf21eXyrcA0tf2uWIcdjawwj9WOfyCPjgnrJ2X7omZYWMuShUDo4uZ1pMmZv2s6pUPc5I5WtoAQ3v%2FsG8x1RkzhvSjcPQoKHxxfJyC4lUgXUQXOCOKrKXbqx3qbkbhEaW9918cHkblcM8HqNfUu6r7%2FfxBbTtZCY4YEaEAYNrHsWSNlM%2FWZA6ZevJ15pkcpELmqWwHA1fxCcDrgPK6iVlyqmqNtFlO%2Bsz9Z5yvlfAvvcOURSz9nBmim%2FXtr0DQQIxWkXlTZUTZ7s330VlbiGoPHlM7ctU2cEBwlncU89KJ3nMQz1PdNfXeKsnJ%2FqJiZLyjFILjzE5lR4NaELWj7WBK8m4RgfBmOFalpjGzt75QiAFZjTD1YoqYy3swai5hMngseUohJmVKNa2ocu3NeIjw%2FzNh84ctP8KZn6jALTtzpMCL75XALoN7exvtI%2BBAbbxbrIL2e1EBUrnV3DqBWq16KbHa4kYuKjmCmJgi1GgB6LOJh2478AIXqSFiuGsT%2BLtYTaLKjmYmzn5ZsnJIjgM0zpiCKOJLyf5GkaQyWPEBC2NOKhmeOFNy2XZV0NEjopX05pt8UYwTmhTDeIJl%2BPSpHeqZUCrCxrZJJiI5EdfsDKHZAXGc2hpd5lp8%2BknYnHV7eN8MMuuh70GOqUBEAhP7IxQnYUys5%2BhKd4fFAriuhO7ArZOr4Iu%2FAgacb55kBuATkx76jyGox6kPY9cQfgnp5SwTiYlc7o5uMAQOwQh%2B07igofhQ3%2FPXIrd1EDYYOhbnKXy5XY5L7aYY6FyEC71yVMvFA7YQVDKxib%2FGIKjcddwilS%2FYYrqqwqmFfmxMT8mft4ItEmaZRlKE%2BViE23vhG4Rc6spsx2QYI0gTTuwpCmd&X-Amz-Signature=93fea95aca9763fbdf3acce65f30d3cde83a4ce3fc2fca2634396fb39ad445e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HLDUXZO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCCnHPfR1rzWMjYU3krD8EJb30hubC2RPY%2FpdByI%2FRwTQIhAMBZx8DfEz2kV54guX6fywWVnKv0amBvDORGwBZnMV3DKv8DCCoQABoMNjM3NDIzMTgzODA1IgzhX%2BpWDQ5u%2BHNW8%2FMq3APRHwtPkOAHe35pqLOvGj6Uh007ijO1UVsZ%2B4Uwk9wzTFUnKYyL7LmVL7FiHS1OLbht%2Br46g6JLXNMkLvuV13YIrLqALbGbGMdQoFhfGKz37o2UhOzAG1iz5Ic%2FkaX3ruOS0pQKY%2F2MHV2GtiL7ZTdhcFcdSfEKxGDcKHsojOefvFLsCLv7Z8ml1d5h%2BE6aHJi4w0NzmrPX4UGSeBQL93SyK8Hq%2B%2FaH6TrRhtwRU21J5G3cC9o0L2hwkBP20WwE4KfN73Wvu08AuvkEG%2FN1n3S4UsmPL7BV4vV7sLIakm27L5jMgB6m7e2FU0sJ6GUnyp2QB2UtDyOxIxHLAtfIEK3mF8m35nWEqOT65kFVO5TMhV%2F7FI5VMZaAtnhNq3jVv1x%2FlKwWe%2F27XAwgqShViNdSM%2F3I8Hf34EphwFosVzUSC4xNSBpQRlvm9qjifUaEVaIogkEGADfLzQ5lwo4sRek4%2BEH21%2Bcl5aciX9YBADG5VJWGJxzOq3VhwzCPD%2BDokm7L6EzQ4%2BZiYVOTXI9BMXDXr3JKL1FrQVTE0ll%2Fb6VeEsUU4huGKBrM1r2S8bfwqf2ne9uSLjJne0AwwUjcbRRCimlP%2BtLIWRD4YqHo8EmDt5N0Fv4BEQPTJ0YJxTDjroe9BjqkAe2tqlbH46RemXlbKHFbPpsTbGH8F6CxVoe7FSuXTjDMrD7By%2FuQvED0dNbjOT8SgjiIXd3wytVmpgOSfYs%2B1p4%2F1wBz1DtLPbbf9UKNW3fvWH1BlJORsgHOzPaowkfATOrYoG1a%2FULJR%2FAfM3EnmjyJFOENnDbovarrkwVtuQABoivlsGO1TwoMO%2ByebkJPEtPemyKQVcB8mjc2%2BfoLEZtPmUgQ&X-Amz-Signature=4b0d6dd2c3264f180730a744d5305c622fa38a8fde818ed10f5f7e2f00851421&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HLDUXZO%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQCCnHPfR1rzWMjYU3krD8EJb30hubC2RPY%2FpdByI%2FRwTQIhAMBZx8DfEz2kV54guX6fywWVnKv0amBvDORGwBZnMV3DKv8DCCoQABoMNjM3NDIzMTgzODA1IgzhX%2BpWDQ5u%2BHNW8%2FMq3APRHwtPkOAHe35pqLOvGj6Uh007ijO1UVsZ%2B4Uwk9wzTFUnKYyL7LmVL7FiHS1OLbht%2Br46g6JLXNMkLvuV13YIrLqALbGbGMdQoFhfGKz37o2UhOzAG1iz5Ic%2FkaX3ruOS0pQKY%2F2MHV2GtiL7ZTdhcFcdSfEKxGDcKHsojOefvFLsCLv7Z8ml1d5h%2BE6aHJi4w0NzmrPX4UGSeBQL93SyK8Hq%2B%2FaH6TrRhtwRU21J5G3cC9o0L2hwkBP20WwE4KfN73Wvu08AuvkEG%2FN1n3S4UsmPL7BV4vV7sLIakm27L5jMgB6m7e2FU0sJ6GUnyp2QB2UtDyOxIxHLAtfIEK3mF8m35nWEqOT65kFVO5TMhV%2F7FI5VMZaAtnhNq3jVv1x%2FlKwWe%2F27XAwgqShViNdSM%2F3I8Hf34EphwFosVzUSC4xNSBpQRlvm9qjifUaEVaIogkEGADfLzQ5lwo4sRek4%2BEH21%2Bcl5aciX9YBADG5VJWGJxzOq3VhwzCPD%2BDokm7L6EzQ4%2BZiYVOTXI9BMXDXr3JKL1FrQVTE0ll%2Fb6VeEsUU4huGKBrM1r2S8bfwqf2ne9uSLjJne0AwwUjcbRRCimlP%2BtLIWRD4YqHo8EmDt5N0Fv4BEQPTJ0YJxTDjroe9BjqkAe2tqlbH46RemXlbKHFbPpsTbGH8F6CxVoe7FSuXTjDMrD7By%2FuQvED0dNbjOT8SgjiIXd3wytVmpgOSfYs%2B1p4%2F1wBz1DtLPbbf9UKNW3fvWH1BlJORsgHOzPaowkfATOrYoG1a%2FULJR%2FAfM3EnmjyJFOENnDbovarrkwVtuQABoivlsGO1TwoMO%2ByebkJPEtPemyKQVcB8mjc2%2BfoLEZtPmUgQ&X-Amz-Signature=9682fd93c21792c72978e6e7ed232674343c90d5eade3c63142ff2ca1f06541b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
