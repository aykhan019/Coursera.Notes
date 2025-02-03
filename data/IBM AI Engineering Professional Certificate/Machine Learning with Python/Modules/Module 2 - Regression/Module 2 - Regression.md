

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEK2EEEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQD%2FYm%2F5%2BzIPEGisHIKbF2%2FZZvj3IKg5D%2Bj2TeFUQZJmAQIgPIIpmDnU0ytcvJO3HAz2M9Dsxcfd3jTZayAs9mlfFIsq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDCCmQG%2BQAKzkxfsZ8CrcA7E4sLjOJkXoRS5EYvM7OBCYLnGvUXaUgQ%2Bou1nh%2B2ci4ky7fdOSEp85%2Fg%2Fua0LCPHof5uC8TS0LllDCC1WWdBdNHnOAvQyWusBdI8WGD0KXs7cUkJzhN6B2HQqZtAkmjFkwc16ALIgshb0DxLxqP%2FIUQ0ycdTtrTZViswOFJy7yKIpNfWmnRvAud9XmigcU84BYh0wxdQWkyWAlBkLN1V9Fmnt77NVUA2Aqa9pwfYuk6ykNNJBldp2NWdjwlKUaGBExNDli70sqw1AmPbQLni5W7b0OvUWDh5ziHTWY%2Feqj7Harc1ETY%2FsN9nSw%2B8%2FvNGN24TMizQuxjLHkH7IjrpScq6mNkR2nsDCJVoRsUwbRGcShY1HF1bcQvl1sZjseBft92oqIENFV5E0t8hdo05dZtgWwuQC9Dy7DMyA6poPditmYmEaolU3wcgpjErOHXU89MWOGLYnUCbwBAwW5ohhtvH9vDRcmB0mwED7QlhjDh4ShdksUcNQ0lsnccPWyopMgDcPs%2FnYIvjPcWe4k2zqM7bLgwWhyADMZvtDCVwSMPSDLjjFx5LOzcppAKAKy9bAAI9akz8hhzll5ErOjBYCtk4XXKov8nwo%2Fh088lAMw1Bxu0WHEJ9faL%2BbuMOHZhL0GOqUBevUsGOi%2Feh7NIZu8WVdzFLkym8m2dQw%2F%2FBFz3fE6JhenabwpaoFpG8JS7JTM4CtoxAri7H04Q9cX79Qo9Cj%2BZarvb3hohcrCU3GOymPcZ%2FDSbq6i3JdyferCr32uTUqgFIcbr89hfa8BdtpU6097%2F0rhCKl%2FNigkCPPq0P4va6NsxTm%2BVOCJaqWZDZl1xnJ6rMHIjg6rJcZdyMWE8AB4pczjqGNo&X-Amz-Signature=ad47e6489659085e0f667e2e80703f5cb954801def21f3cf26e80919966993ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEK2EEEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQD%2FYm%2F5%2BzIPEGisHIKbF2%2FZZvj3IKg5D%2Bj2TeFUQZJmAQIgPIIpmDnU0ytcvJO3HAz2M9Dsxcfd3jTZayAs9mlfFIsq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDCCmQG%2BQAKzkxfsZ8CrcA7E4sLjOJkXoRS5EYvM7OBCYLnGvUXaUgQ%2Bou1nh%2B2ci4ky7fdOSEp85%2Fg%2Fua0LCPHof5uC8TS0LllDCC1WWdBdNHnOAvQyWusBdI8WGD0KXs7cUkJzhN6B2HQqZtAkmjFkwc16ALIgshb0DxLxqP%2FIUQ0ycdTtrTZViswOFJy7yKIpNfWmnRvAud9XmigcU84BYh0wxdQWkyWAlBkLN1V9Fmnt77NVUA2Aqa9pwfYuk6ykNNJBldp2NWdjwlKUaGBExNDli70sqw1AmPbQLni5W7b0OvUWDh5ziHTWY%2Feqj7Harc1ETY%2FsN9nSw%2B8%2FvNGN24TMizQuxjLHkH7IjrpScq6mNkR2nsDCJVoRsUwbRGcShY1HF1bcQvl1sZjseBft92oqIENFV5E0t8hdo05dZtgWwuQC9Dy7DMyA6poPditmYmEaolU3wcgpjErOHXU89MWOGLYnUCbwBAwW5ohhtvH9vDRcmB0mwED7QlhjDh4ShdksUcNQ0lsnccPWyopMgDcPs%2FnYIvjPcWe4k2zqM7bLgwWhyADMZvtDCVwSMPSDLjjFx5LOzcppAKAKy9bAAI9akz8hhzll5ErOjBYCtk4XXKov8nwo%2Fh088lAMw1Bxu0WHEJ9faL%2BbuMOHZhL0GOqUBevUsGOi%2Feh7NIZu8WVdzFLkym8m2dQw%2F%2FBFz3fE6JhenabwpaoFpG8JS7JTM4CtoxAri7H04Q9cX79Qo9Cj%2BZarvb3hohcrCU3GOymPcZ%2FDSbq6i3JdyferCr32uTUqgFIcbr89hfa8BdtpU6097%2F0rhCKl%2FNigkCPPq0P4va6NsxTm%2BVOCJaqWZDZl1xnJ6rMHIjg6rJcZdyMWE8AB4pczjqGNo&X-Amz-Signature=c0f6c72a4adccffabb2b781cf9de757d32674ca77a8cbf2845b9302981c440f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEK2EEEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQD%2FYm%2F5%2BzIPEGisHIKbF2%2FZZvj3IKg5D%2Bj2TeFUQZJmAQIgPIIpmDnU0ytcvJO3HAz2M9Dsxcfd3jTZayAs9mlfFIsq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDCCmQG%2BQAKzkxfsZ8CrcA7E4sLjOJkXoRS5EYvM7OBCYLnGvUXaUgQ%2Bou1nh%2B2ci4ky7fdOSEp85%2Fg%2Fua0LCPHof5uC8TS0LllDCC1WWdBdNHnOAvQyWusBdI8WGD0KXs7cUkJzhN6B2HQqZtAkmjFkwc16ALIgshb0DxLxqP%2FIUQ0ycdTtrTZViswOFJy7yKIpNfWmnRvAud9XmigcU84BYh0wxdQWkyWAlBkLN1V9Fmnt77NVUA2Aqa9pwfYuk6ykNNJBldp2NWdjwlKUaGBExNDli70sqw1AmPbQLni5W7b0OvUWDh5ziHTWY%2Feqj7Harc1ETY%2FsN9nSw%2B8%2FvNGN24TMizQuxjLHkH7IjrpScq6mNkR2nsDCJVoRsUwbRGcShY1HF1bcQvl1sZjseBft92oqIENFV5E0t8hdo05dZtgWwuQC9Dy7DMyA6poPditmYmEaolU3wcgpjErOHXU89MWOGLYnUCbwBAwW5ohhtvH9vDRcmB0mwED7QlhjDh4ShdksUcNQ0lsnccPWyopMgDcPs%2FnYIvjPcWe4k2zqM7bLgwWhyADMZvtDCVwSMPSDLjjFx5LOzcppAKAKy9bAAI9akz8hhzll5ErOjBYCtk4XXKov8nwo%2Fh088lAMw1Bxu0WHEJ9faL%2BbuMOHZhL0GOqUBevUsGOi%2Feh7NIZu8WVdzFLkym8m2dQw%2F%2FBFz3fE6JhenabwpaoFpG8JS7JTM4CtoxAri7H04Q9cX79Qo9Cj%2BZarvb3hohcrCU3GOymPcZ%2FDSbq6i3JdyferCr32uTUqgFIcbr89hfa8BdtpU6097%2F0rhCKl%2FNigkCPPq0P4va6NsxTm%2BVOCJaqWZDZl1xnJ6rMHIjg6rJcZdyMWE8AB4pczjqGNo&X-Amz-Signature=7e619f23790017bcbd366c7a88c0ff94379dd88337e04242a931605be490cdb6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEK2EEEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQD%2FYm%2F5%2BzIPEGisHIKbF2%2FZZvj3IKg5D%2Bj2TeFUQZJmAQIgPIIpmDnU0ytcvJO3HAz2M9Dsxcfd3jTZayAs9mlfFIsq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDCCmQG%2BQAKzkxfsZ8CrcA7E4sLjOJkXoRS5EYvM7OBCYLnGvUXaUgQ%2Bou1nh%2B2ci4ky7fdOSEp85%2Fg%2Fua0LCPHof5uC8TS0LllDCC1WWdBdNHnOAvQyWusBdI8WGD0KXs7cUkJzhN6B2HQqZtAkmjFkwc16ALIgshb0DxLxqP%2FIUQ0ycdTtrTZViswOFJy7yKIpNfWmnRvAud9XmigcU84BYh0wxdQWkyWAlBkLN1V9Fmnt77NVUA2Aqa9pwfYuk6ykNNJBldp2NWdjwlKUaGBExNDli70sqw1AmPbQLni5W7b0OvUWDh5ziHTWY%2Feqj7Harc1ETY%2FsN9nSw%2B8%2FvNGN24TMizQuxjLHkH7IjrpScq6mNkR2nsDCJVoRsUwbRGcShY1HF1bcQvl1sZjseBft92oqIENFV5E0t8hdo05dZtgWwuQC9Dy7DMyA6poPditmYmEaolU3wcgpjErOHXU89MWOGLYnUCbwBAwW5ohhtvH9vDRcmB0mwED7QlhjDh4ShdksUcNQ0lsnccPWyopMgDcPs%2FnYIvjPcWe4k2zqM7bLgwWhyADMZvtDCVwSMPSDLjjFx5LOzcppAKAKy9bAAI9akz8hhzll5ErOjBYCtk4XXKov8nwo%2Fh088lAMw1Bxu0WHEJ9faL%2BbuMOHZhL0GOqUBevUsGOi%2Feh7NIZu8WVdzFLkym8m2dQw%2F%2FBFz3fE6JhenabwpaoFpG8JS7JTM4CtoxAri7H04Q9cX79Qo9Cj%2BZarvb3hohcrCU3GOymPcZ%2FDSbq6i3JdyferCr32uTUqgFIcbr89hfa8BdtpU6097%2F0rhCKl%2FNigkCPPq0P4va6NsxTm%2BVOCJaqWZDZl1xnJ6rMHIjg6rJcZdyMWE8AB4pczjqGNo&X-Amz-Signature=7258386260afd8653a4472e51b0079819871d43a3c02c9f2bb16f8ba26dbedbc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEK2EEEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQD%2FYm%2F5%2BzIPEGisHIKbF2%2FZZvj3IKg5D%2Bj2TeFUQZJmAQIgPIIpmDnU0ytcvJO3HAz2M9Dsxcfd3jTZayAs9mlfFIsq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDCCmQG%2BQAKzkxfsZ8CrcA7E4sLjOJkXoRS5EYvM7OBCYLnGvUXaUgQ%2Bou1nh%2B2ci4ky7fdOSEp85%2Fg%2Fua0LCPHof5uC8TS0LllDCC1WWdBdNHnOAvQyWusBdI8WGD0KXs7cUkJzhN6B2HQqZtAkmjFkwc16ALIgshb0DxLxqP%2FIUQ0ycdTtrTZViswOFJy7yKIpNfWmnRvAud9XmigcU84BYh0wxdQWkyWAlBkLN1V9Fmnt77NVUA2Aqa9pwfYuk6ykNNJBldp2NWdjwlKUaGBExNDli70sqw1AmPbQLni5W7b0OvUWDh5ziHTWY%2Feqj7Harc1ETY%2FsN9nSw%2B8%2FvNGN24TMizQuxjLHkH7IjrpScq6mNkR2nsDCJVoRsUwbRGcShY1HF1bcQvl1sZjseBft92oqIENFV5E0t8hdo05dZtgWwuQC9Dy7DMyA6poPditmYmEaolU3wcgpjErOHXU89MWOGLYnUCbwBAwW5ohhtvH9vDRcmB0mwED7QlhjDh4ShdksUcNQ0lsnccPWyopMgDcPs%2FnYIvjPcWe4k2zqM7bLgwWhyADMZvtDCVwSMPSDLjjFx5LOzcppAKAKy9bAAI9akz8hhzll5ErOjBYCtk4XXKov8nwo%2Fh088lAMw1Bxu0WHEJ9faL%2BbuMOHZhL0GOqUBevUsGOi%2Feh7NIZu8WVdzFLkym8m2dQw%2F%2FBFz3fE6JhenabwpaoFpG8JS7JTM4CtoxAri7H04Q9cX79Qo9Cj%2BZarvb3hohcrCU3GOymPcZ%2FDSbq6i3JdyferCr32uTUqgFIcbr89hfa8BdtpU6097%2F0rhCKl%2FNigkCPPq0P4va6NsxTm%2BVOCJaqWZDZl1xnJ6rMHIjg6rJcZdyMWE8AB4pczjqGNo&X-Amz-Signature=22023d62fc72fdc2dcb50106534f58add54d9dd6a1b9697847d1d40f4675e7c9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEK2EEEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQD%2FYm%2F5%2BzIPEGisHIKbF2%2FZZvj3IKg5D%2Bj2TeFUQZJmAQIgPIIpmDnU0ytcvJO3HAz2M9Dsxcfd3jTZayAs9mlfFIsq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDCCmQG%2BQAKzkxfsZ8CrcA7E4sLjOJkXoRS5EYvM7OBCYLnGvUXaUgQ%2Bou1nh%2B2ci4ky7fdOSEp85%2Fg%2Fua0LCPHof5uC8TS0LllDCC1WWdBdNHnOAvQyWusBdI8WGD0KXs7cUkJzhN6B2HQqZtAkmjFkwc16ALIgshb0DxLxqP%2FIUQ0ycdTtrTZViswOFJy7yKIpNfWmnRvAud9XmigcU84BYh0wxdQWkyWAlBkLN1V9Fmnt77NVUA2Aqa9pwfYuk6ykNNJBldp2NWdjwlKUaGBExNDli70sqw1AmPbQLni5W7b0OvUWDh5ziHTWY%2Feqj7Harc1ETY%2FsN9nSw%2B8%2FvNGN24TMizQuxjLHkH7IjrpScq6mNkR2nsDCJVoRsUwbRGcShY1HF1bcQvl1sZjseBft92oqIENFV5E0t8hdo05dZtgWwuQC9Dy7DMyA6poPditmYmEaolU3wcgpjErOHXU89MWOGLYnUCbwBAwW5ohhtvH9vDRcmB0mwED7QlhjDh4ShdksUcNQ0lsnccPWyopMgDcPs%2FnYIvjPcWe4k2zqM7bLgwWhyADMZvtDCVwSMPSDLjjFx5LOzcppAKAKy9bAAI9akz8hhzll5ErOjBYCtk4XXKov8nwo%2Fh088lAMw1Bxu0WHEJ9faL%2BbuMOHZhL0GOqUBevUsGOi%2Feh7NIZu8WVdzFLkym8m2dQw%2F%2FBFz3fE6JhenabwpaoFpG8JS7JTM4CtoxAri7H04Q9cX79Qo9Cj%2BZarvb3hohcrCU3GOymPcZ%2FDSbq6i3JdyferCr32uTUqgFIcbr89hfa8BdtpU6097%2F0rhCKl%2FNigkCPPq0P4va6NsxTm%2BVOCJaqWZDZl1xnJ6rMHIjg6rJcZdyMWE8AB4pczjqGNo&X-Amz-Signature=8558cfae61655409801cb938bb2be9709f354570293b2b537385138c83ac5206&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEK2EEEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQD%2FYm%2F5%2BzIPEGisHIKbF2%2FZZvj3IKg5D%2Bj2TeFUQZJmAQIgPIIpmDnU0ytcvJO3HAz2M9Dsxcfd3jTZayAs9mlfFIsq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDCCmQG%2BQAKzkxfsZ8CrcA7E4sLjOJkXoRS5EYvM7OBCYLnGvUXaUgQ%2Bou1nh%2B2ci4ky7fdOSEp85%2Fg%2Fua0LCPHof5uC8TS0LllDCC1WWdBdNHnOAvQyWusBdI8WGD0KXs7cUkJzhN6B2HQqZtAkmjFkwc16ALIgshb0DxLxqP%2FIUQ0ycdTtrTZViswOFJy7yKIpNfWmnRvAud9XmigcU84BYh0wxdQWkyWAlBkLN1V9Fmnt77NVUA2Aqa9pwfYuk6ykNNJBldp2NWdjwlKUaGBExNDli70sqw1AmPbQLni5W7b0OvUWDh5ziHTWY%2Feqj7Harc1ETY%2FsN9nSw%2B8%2FvNGN24TMizQuxjLHkH7IjrpScq6mNkR2nsDCJVoRsUwbRGcShY1HF1bcQvl1sZjseBft92oqIENFV5E0t8hdo05dZtgWwuQC9Dy7DMyA6poPditmYmEaolU3wcgpjErOHXU89MWOGLYnUCbwBAwW5ohhtvH9vDRcmB0mwED7QlhjDh4ShdksUcNQ0lsnccPWyopMgDcPs%2FnYIvjPcWe4k2zqM7bLgwWhyADMZvtDCVwSMPSDLjjFx5LOzcppAKAKy9bAAI9akz8hhzll5ErOjBYCtk4XXKov8nwo%2Fh088lAMw1Bxu0WHEJ9faL%2BbuMOHZhL0GOqUBevUsGOi%2Feh7NIZu8WVdzFLkym8m2dQw%2F%2FBFz3fE6JhenabwpaoFpG8JS7JTM4CtoxAri7H04Q9cX79Qo9Cj%2BZarvb3hohcrCU3GOymPcZ%2FDSbq6i3JdyferCr32uTUqgFIcbr89hfa8BdtpU6097%2F0rhCKl%2FNigkCPPq0P4va6NsxTm%2BVOCJaqWZDZl1xnJ6rMHIjg6rJcZdyMWE8AB4pczjqGNo&X-Amz-Signature=34e156d9c17d218a96a00051fe7514eec663621394b419c5d54b136b4b5a8018&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEK2EEEI%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQD%2FYm%2F5%2BzIPEGisHIKbF2%2FZZvj3IKg5D%2Bj2TeFUQZJmAQIgPIIpmDnU0ytcvJO3HAz2M9Dsxcfd3jTZayAs9mlfFIsq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDCCmQG%2BQAKzkxfsZ8CrcA7E4sLjOJkXoRS5EYvM7OBCYLnGvUXaUgQ%2Bou1nh%2B2ci4ky7fdOSEp85%2Fg%2Fua0LCPHof5uC8TS0LllDCC1WWdBdNHnOAvQyWusBdI8WGD0KXs7cUkJzhN6B2HQqZtAkmjFkwc16ALIgshb0DxLxqP%2FIUQ0ycdTtrTZViswOFJy7yKIpNfWmnRvAud9XmigcU84BYh0wxdQWkyWAlBkLN1V9Fmnt77NVUA2Aqa9pwfYuk6ykNNJBldp2NWdjwlKUaGBExNDli70sqw1AmPbQLni5W7b0OvUWDh5ziHTWY%2Feqj7Harc1ETY%2FsN9nSw%2B8%2FvNGN24TMizQuxjLHkH7IjrpScq6mNkR2nsDCJVoRsUwbRGcShY1HF1bcQvl1sZjseBft92oqIENFV5E0t8hdo05dZtgWwuQC9Dy7DMyA6poPditmYmEaolU3wcgpjErOHXU89MWOGLYnUCbwBAwW5ohhtvH9vDRcmB0mwED7QlhjDh4ShdksUcNQ0lsnccPWyopMgDcPs%2FnYIvjPcWe4k2zqM7bLgwWhyADMZvtDCVwSMPSDLjjFx5LOzcppAKAKy9bAAI9akz8hhzll5ErOjBYCtk4XXKov8nwo%2Fh088lAMw1Bxu0WHEJ9faL%2BbuMOHZhL0GOqUBevUsGOi%2Feh7NIZu8WVdzFLkym8m2dQw%2F%2FBFz3fE6JhenabwpaoFpG8JS7JTM4CtoxAri7H04Q9cX79Qo9Cj%2BZarvb3hohcrCU3GOymPcZ%2FDSbq6i3JdyferCr32uTUqgFIcbr89hfa8BdtpU6097%2F0rhCKl%2FNigkCPPq0P4va6NsxTm%2BVOCJaqWZDZl1xnJ6rMHIjg6rJcZdyMWE8AB4pczjqGNo&X-Amz-Signature=6e7772ae13c7a330782af7c28f2960110088f83ec8d36f745f247ec177b4c797&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H3TVPT3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIDwDiYEtRQNFkFU9Qze4nvSPZmSun9gfMQhrkMM9OZffAiEA3mzUE65G9bZ%2FUBCJeJZrxREel4k3ye2iVKTirdoJUrQq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDM9YRhL%2BeXFaIZ0rjCrcA5PyB%2FXiYGaFzjBvqFQgIctuItxvbIrh%2FwcdyVR2j0sZP7RMygF2iBBxigKM6rvrNsAxCf6%2BGUJpk%2BdZM4Q0qjo40yjKau3lwWr2fITTBws1h8lKgJiSjzf5r0i2q0rCg8UlvhakNbXew1yDHL%2FyQNR87WFvVskEkx%2FI%2BTKObGROCBuKNQ9YHelJS4lGVG9qLiPO1ovb05QZgytORCbv6UyCGsAKB1QxlUaCdO4bZmJ2tK3ogVEPkCdERa1FiS4d96QdQURIj9p%2BunxSIwdHq8clOTmHNY%2FwBwhtSNkTaZ0Tm1jS%2FwGTtIKtDVGekkXtbnuH5g71p02L0C8LxDcDdYHclKqwxmgqN%2FRs2QlTPvaWbFWQZkLUJWLGuqRBnbDDAgW4SO7hU1xuLuN6hMJ0ZnmrwVZeowfn17a56oukEBZfikxwV%2BzyUmq8EqVD%2FST1OukRqeeHeYPOw7jiRo1EHE27SIZwP5gzKsk2oIQqVpTsSAo8Irjlj6g0%2B7mhXFPTdKZq5iWaeD6SKC8jD%2BXYJrbP%2BnWo2l3Zz2bdffSRshiRHSlPlJv4wzDXMQOca2G3l2mlcvHn8naTYmBNbQaprvsUO7vMcZGIiE%2FO5HtZY57mBXaKdNMobU3VYySWMOLZhL0GOqUBKQg8SCOXUDlQB36E0zijYeWGrSg3IC4weDVi4M1KuhUQCakhh9WtUvrZffoeW61wwPXJHEknoBvgg8oxGyqeIJ3rqxI1A6AgBetczPR7Ar4CdEG%2Bx8KbGom3pl%2B91PXQxwFu%2BvqYw%2BVRj9%2BTaVLedd9w29bM1cUTCS9iVuzmx950m%2F9DmrAVk6J3YXgTll7xJexdPnbEhHY76ayOgOP6yWv7BkDA&X-Amz-Signature=800291c04361f7109e4671ab596776606a8264cab2a8ac8272003eef2eb59aa9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGCC3YV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJIMEYCIQCsDSTb0Bi2blxErzeginRUH2QsBiPl%2FDV8TxWlXW45bQIhAOh8rT76AzH5Pkqj3PLLNUdYltgdMi1rXP2g1Zi8aKESKv8DCB4QABoMNjM3NDIzMTgzODA1Igxhi18ZVWOTG7nF0ZIq3AP2I5acMGe2E5MqY8%2BQbXuag%2BAIumXwFrCo5%2F9jLV837nEmdVHEYnVoNNFvkcryzlla4mnhutT21hkrY8Cmxa5bp2wa5rJiUYrjyYbwbe9TKbNsjyrCTjwzhUoq4lA5Xro%2BsAxPcw6JlhbUUovLppFc0e%2Fg2ISamsgKh4nEVHgSgydUr%2BDpeHrXkuNa8GbaBlX9xR72HSVfUepfWB%2FoMby4kJyejo2tYl1mOAqGDqAJQdCyVM2xGjivOcGfYbSpC88gsT7Kwq%2BOn8e8YhD87Nv3l9xr3GsCYD5VdvuFJf%2F6l0rt8OlOqmc%2FwUitEx131GvWpwiyJ5cvGF8JJ%2B6gLO7TRmaHviRTOzz2uKAm%2FhIdC%2F%2BIAF79sMueKJXyZ10%2FBymGQUQ4oB38W%2FCcqNv60ScIIKrtWmA0n3QFV7XAiJQEeuSILTVXRLs9rdOANOCxgU73d%2FJla2Dj5%2F3FJ14ZuO%2B3DiMAddk%2FReSFsmsORu1Ty3fO3ZaGaMlm2kJlQc8prOyEn0gETDD%2FyntGJmKGOnuUajLBL3khiMgaTZ6szQUltdiSPDY3M%2BeHKo4Vl51%2BpT4K6uQOl0PV1gDdTbU0mp2Hn1gFQncyC%2FSDn3GlWTNFWcZ9khnTYN0ZxqYzezDK2YS9BjqkAUUzlSLZE6dP5iVnfBZAYZFzFCXTqwDI1o9yq%2Fy7505Zdn4oL5kHvLHVOFzTCWWFwzm8B8J3gSyQoKwPJEoF8AEkV%2FbsMPuCuelUc%2BUiThfYeUzK7mAJjfeoou9kWYJ0GkL7cvxsG3uDxsCQpIGH6CNVsPdaMQTm86Xa8cYX66LfpCuMc%2BZKzjNLtVXFOWKhRVGfZyA8qDxLf88syw3kH5FjfOW4&X-Amz-Signature=4b1e1f7fd398962ce5ede7e8cc40f5444ad3eb82884bf7ea23ea6c5ecd7a6b87&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AHKQK7P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQDIoQbPW9EPVNzIgtoULD7TjqxndIQXnbfOKVq0SJOFPwIgXKWFc6Li5%2FD1HyYX%2FUZ%2Fc2kB50oz%2FTuNIuWxVNHvnVYq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDwyXJZMwXsiSqgLqCrcA3SSMz%2FGPWFvtR2YzbZbPHwxL266qtnGniiNDb4mxzuSfLT6ne2By5fhbg8K9MOsPZABMDYHGoeCT2ooPEDfUdTOVENC2GP0iZ%2B5I74WLxVaDYmu58za%2F25sWY47oDLRQ1%2BYleRFwlVFIuFKDgic4ebJgZZdf1sms%2BtJxvr%2FM%2B%2FWqtv%2BTkwCl1B%2BAYumYrLuDqyxSRsvBToWb5v14%2BrlueCVVOUJInWsl6OFJkkLZusDWCOqzJho7WtcvncT7RYZkFxU0SEchW2oTgDx6PVVfVJTlbUnV2DxyT0cDKWqfd5n4Drl1SNfKV8g2cdywehip7FRY8CmYnimG4iIZXkb7Q%2F2%2Fbms0rrerEfoxLnXmF6MUrbJ6XYVOANEDf5Vs7sokIoYUa%2BJaV8gqDuhqNj%2BBD377BhekpG4il0R5bLGogbModN8vpNVj6ZLesD1iR9yKN3SfLgdEyzpHWBOy9rXslCUCWYdLS60ZARJjNyYWE3igsQkBO1p%2Bm11%2FFnX6lTMsHFR%2FR%2BZDC9s5Y0PE8n5K9TJ1%2BPnc1Z9W37moxk7RW6RYv%2BDNXKMmVC3VLiDF4BNy2RgBWW6F%2BLbpO%2FFMjgVZwVfvV7ZLizyI9Lzc2nh2o%2BGo7kUhthJ%2FopOJJDLMNzZhL0GOqUBByTqg%2BkCGcz60J9u7YIm9MiLpA%2FX4np9tbU5vvRzJAek8LovvWTVeG%2BtUQCMtsD3F3Dx7fCYhps7zCrERSXoJijcIlB5EL9iJkS1ARPM5lnGBi4peUlItBspDEP4UR1wD%2Fw84IUt5irwpHs5cnUQKqewfxNEytOLT6YUlXYLznTJf%2FsseDVSMtxLxaf%2B9cwLrSh3Qwvcf4m7DzWNz7cXtja6cpZ4&X-Amz-Signature=600e5db8fdd27c164e828fe61c3db32d93441c267b7af22623ac4ee96867dac3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AHKQK7P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQDIoQbPW9EPVNzIgtoULD7TjqxndIQXnbfOKVq0SJOFPwIgXKWFc6Li5%2FD1HyYX%2FUZ%2Fc2kB50oz%2FTuNIuWxVNHvnVYq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDDwyXJZMwXsiSqgLqCrcA3SSMz%2FGPWFvtR2YzbZbPHwxL266qtnGniiNDb4mxzuSfLT6ne2By5fhbg8K9MOsPZABMDYHGoeCT2ooPEDfUdTOVENC2GP0iZ%2B5I74WLxVaDYmu58za%2F25sWY47oDLRQ1%2BYleRFwlVFIuFKDgic4ebJgZZdf1sms%2BtJxvr%2FM%2B%2FWqtv%2BTkwCl1B%2BAYumYrLuDqyxSRsvBToWb5v14%2BrlueCVVOUJInWsl6OFJkkLZusDWCOqzJho7WtcvncT7RYZkFxU0SEchW2oTgDx6PVVfVJTlbUnV2DxyT0cDKWqfd5n4Drl1SNfKV8g2cdywehip7FRY8CmYnimG4iIZXkb7Q%2F2%2Fbms0rrerEfoxLnXmF6MUrbJ6XYVOANEDf5Vs7sokIoYUa%2BJaV8gqDuhqNj%2BBD377BhekpG4il0R5bLGogbModN8vpNVj6ZLesD1iR9yKN3SfLgdEyzpHWBOy9rXslCUCWYdLS60ZARJjNyYWE3igsQkBO1p%2Bm11%2FFnX6lTMsHFR%2FR%2BZDC9s5Y0PE8n5K9TJ1%2BPnc1Z9W37moxk7RW6RYv%2BDNXKMmVC3VLiDF4BNy2RgBWW6F%2BLbpO%2FFMjgVZwVfvV7ZLizyI9Lzc2nh2o%2BGo7kUhthJ%2FopOJJDLMNzZhL0GOqUBByTqg%2BkCGcz60J9u7YIm9MiLpA%2FX4np9tbU5vvRzJAek8LovvWTVeG%2BtUQCMtsD3F3Dx7fCYhps7zCrERSXoJijcIlB5EL9iJkS1ARPM5lnGBi4peUlItBspDEP4UR1wD%2Fw84IUt5irwpHs5cnUQKqewfxNEytOLT6YUlXYLznTJf%2FsseDVSMtxLxaf%2B9cwLrSh3Qwvcf4m7DzWNz7cXtja6cpZ4&X-Amz-Signature=f679ea97567a3a5b2a8204559f0acfa1c18b8eaf0ba94e0c6d5d901778c2d007&X-Amz-SignedHeaders=host&x-id=GetObject)
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
