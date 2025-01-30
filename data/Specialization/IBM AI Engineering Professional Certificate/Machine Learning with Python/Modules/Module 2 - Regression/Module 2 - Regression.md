

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMU4FHQH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWT0OjDdO%2BD1ettIFVIfDRqpNsJ9VSqsbANJJSDXVX1AiEAzyKgVBDfAfeqO5GysrrhvdaDObo07ddrVmgzCqLBlukqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC2h7W5%2FJhsxiB29WCrcA%2B%2BGxqN8lAtDWydVNxBBNaCG0IdOI5KK981kQ%2F%2BDJlMWbSsRP2sn2m8bt48GxZlAngtqNWEPpgxORauCnDO%2BEaKIKfosj9PN8nK%2Bg3eKcoKt3fI2mtW81CoLMeTKltW7WAZP%2FAoguswcn7Hp5SSPgtspPIAo6vNv3i0gp3CE6U82ud2S3iiQQUYPy3jBKZpArw656GY%2FkIWVL9Qj%2FyuEpwveQKxijStxl2qvcmm3mLifjSEfXf9vKvtkNrOxU%2F4f5nD%2BzX72PDEZ6dNVI1LfFhPE2z6R13nV%2BE3gjJWNGh0gDVaJ58Xr5yLZT9RXCQ%2BFxukOIzvqnaZzrvEgXD4Ub6FB%2B8pnkKaDRPZIOZF0IthvEL1EUzclgkybCgTgbtEMmjVUmy2H2jdGoTevi8u5YNgmGFNQiHuKfLFQHU1TMskydC6tCUAj3SLGY8GCEKf%2FWoeGLd1T1L%2FaX4%2BNHYwlgCCPK2Bw4gpvvlUnfg2Hj1nMdkSMqg2GKBym36AM6n9bj0i3XEL3dWmYzA4MxM81pE1edBSNZMvMUyco%2FqH%2FmkawgchcSIaAtNZBCbUuLkZHfx%2BLqsFkD7pOEXcproVz%2FGrXmPPgLxD0P5CGwNRSmZyUdyg5Z2Ga5RGnC02EMMeL7bwGOqUBp%2B3o05Z0XitxUWxBYrHhbB7wYAi%2BDcVuXq3LXgXdGwLszaDdIgPQd5xMMyqoqv9svSGO8FgQuQ6jzMiNCuwKkB6XdAz4xMYfW06yUesTCqUMzb6bfX6EhIviuT0aQAhzp48WRw7TwMwCXecH2QNubBdDvUQ6YbFkflcf16FMcfhodEukk7xAPWplNgchXDgIwBE%2FEdq1bJtn301Wjktlbuk4vugH&X-Amz-Signature=b0964b20196e1819bf46434395b4312fb61607d637215ae66d70a36818aa5043&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMU4FHQH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWT0OjDdO%2BD1ettIFVIfDRqpNsJ9VSqsbANJJSDXVX1AiEAzyKgVBDfAfeqO5GysrrhvdaDObo07ddrVmgzCqLBlukqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC2h7W5%2FJhsxiB29WCrcA%2B%2BGxqN8lAtDWydVNxBBNaCG0IdOI5KK981kQ%2F%2BDJlMWbSsRP2sn2m8bt48GxZlAngtqNWEPpgxORauCnDO%2BEaKIKfosj9PN8nK%2Bg3eKcoKt3fI2mtW81CoLMeTKltW7WAZP%2FAoguswcn7Hp5SSPgtspPIAo6vNv3i0gp3CE6U82ud2S3iiQQUYPy3jBKZpArw656GY%2FkIWVL9Qj%2FyuEpwveQKxijStxl2qvcmm3mLifjSEfXf9vKvtkNrOxU%2F4f5nD%2BzX72PDEZ6dNVI1LfFhPE2z6R13nV%2BE3gjJWNGh0gDVaJ58Xr5yLZT9RXCQ%2BFxukOIzvqnaZzrvEgXD4Ub6FB%2B8pnkKaDRPZIOZF0IthvEL1EUzclgkybCgTgbtEMmjVUmy2H2jdGoTevi8u5YNgmGFNQiHuKfLFQHU1TMskydC6tCUAj3SLGY8GCEKf%2FWoeGLd1T1L%2FaX4%2BNHYwlgCCPK2Bw4gpvvlUnfg2Hj1nMdkSMqg2GKBym36AM6n9bj0i3XEL3dWmYzA4MxM81pE1edBSNZMvMUyco%2FqH%2FmkawgchcSIaAtNZBCbUuLkZHfx%2BLqsFkD7pOEXcproVz%2FGrXmPPgLxD0P5CGwNRSmZyUdyg5Z2Ga5RGnC02EMMeL7bwGOqUBp%2B3o05Z0XitxUWxBYrHhbB7wYAi%2BDcVuXq3LXgXdGwLszaDdIgPQd5xMMyqoqv9svSGO8FgQuQ6jzMiNCuwKkB6XdAz4xMYfW06yUesTCqUMzb6bfX6EhIviuT0aQAhzp48WRw7TwMwCXecH2QNubBdDvUQ6YbFkflcf16FMcfhodEukk7xAPWplNgchXDgIwBE%2FEdq1bJtn301Wjktlbuk4vugH&X-Amz-Signature=5690478ede30262bcbb08d07b5f8ad61e490cb02320e805d0a5f31c0fdb8c2b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMU4FHQH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWT0OjDdO%2BD1ettIFVIfDRqpNsJ9VSqsbANJJSDXVX1AiEAzyKgVBDfAfeqO5GysrrhvdaDObo07ddrVmgzCqLBlukqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC2h7W5%2FJhsxiB29WCrcA%2B%2BGxqN8lAtDWydVNxBBNaCG0IdOI5KK981kQ%2F%2BDJlMWbSsRP2sn2m8bt48GxZlAngtqNWEPpgxORauCnDO%2BEaKIKfosj9PN8nK%2Bg3eKcoKt3fI2mtW81CoLMeTKltW7WAZP%2FAoguswcn7Hp5SSPgtspPIAo6vNv3i0gp3CE6U82ud2S3iiQQUYPy3jBKZpArw656GY%2FkIWVL9Qj%2FyuEpwveQKxijStxl2qvcmm3mLifjSEfXf9vKvtkNrOxU%2F4f5nD%2BzX72PDEZ6dNVI1LfFhPE2z6R13nV%2BE3gjJWNGh0gDVaJ58Xr5yLZT9RXCQ%2BFxukOIzvqnaZzrvEgXD4Ub6FB%2B8pnkKaDRPZIOZF0IthvEL1EUzclgkybCgTgbtEMmjVUmy2H2jdGoTevi8u5YNgmGFNQiHuKfLFQHU1TMskydC6tCUAj3SLGY8GCEKf%2FWoeGLd1T1L%2FaX4%2BNHYwlgCCPK2Bw4gpvvlUnfg2Hj1nMdkSMqg2GKBym36AM6n9bj0i3XEL3dWmYzA4MxM81pE1edBSNZMvMUyco%2FqH%2FmkawgchcSIaAtNZBCbUuLkZHfx%2BLqsFkD7pOEXcproVz%2FGrXmPPgLxD0P5CGwNRSmZyUdyg5Z2Ga5RGnC02EMMeL7bwGOqUBp%2B3o05Z0XitxUWxBYrHhbB7wYAi%2BDcVuXq3LXgXdGwLszaDdIgPQd5xMMyqoqv9svSGO8FgQuQ6jzMiNCuwKkB6XdAz4xMYfW06yUesTCqUMzb6bfX6EhIviuT0aQAhzp48WRw7TwMwCXecH2QNubBdDvUQ6YbFkflcf16FMcfhodEukk7xAPWplNgchXDgIwBE%2FEdq1bJtn301Wjktlbuk4vugH&X-Amz-Signature=f53a88029a7bbda2d99c06f077ec1ce5b5a3e7b1d4947c4014fd47d5f8ea8027&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMU4FHQH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWT0OjDdO%2BD1ettIFVIfDRqpNsJ9VSqsbANJJSDXVX1AiEAzyKgVBDfAfeqO5GysrrhvdaDObo07ddrVmgzCqLBlukqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC2h7W5%2FJhsxiB29WCrcA%2B%2BGxqN8lAtDWydVNxBBNaCG0IdOI5KK981kQ%2F%2BDJlMWbSsRP2sn2m8bt48GxZlAngtqNWEPpgxORauCnDO%2BEaKIKfosj9PN8nK%2Bg3eKcoKt3fI2mtW81CoLMeTKltW7WAZP%2FAoguswcn7Hp5SSPgtspPIAo6vNv3i0gp3CE6U82ud2S3iiQQUYPy3jBKZpArw656GY%2FkIWVL9Qj%2FyuEpwveQKxijStxl2qvcmm3mLifjSEfXf9vKvtkNrOxU%2F4f5nD%2BzX72PDEZ6dNVI1LfFhPE2z6R13nV%2BE3gjJWNGh0gDVaJ58Xr5yLZT9RXCQ%2BFxukOIzvqnaZzrvEgXD4Ub6FB%2B8pnkKaDRPZIOZF0IthvEL1EUzclgkybCgTgbtEMmjVUmy2H2jdGoTevi8u5YNgmGFNQiHuKfLFQHU1TMskydC6tCUAj3SLGY8GCEKf%2FWoeGLd1T1L%2FaX4%2BNHYwlgCCPK2Bw4gpvvlUnfg2Hj1nMdkSMqg2GKBym36AM6n9bj0i3XEL3dWmYzA4MxM81pE1edBSNZMvMUyco%2FqH%2FmkawgchcSIaAtNZBCbUuLkZHfx%2BLqsFkD7pOEXcproVz%2FGrXmPPgLxD0P5CGwNRSmZyUdyg5Z2Ga5RGnC02EMMeL7bwGOqUBp%2B3o05Z0XitxUWxBYrHhbB7wYAi%2BDcVuXq3LXgXdGwLszaDdIgPQd5xMMyqoqv9svSGO8FgQuQ6jzMiNCuwKkB6XdAz4xMYfW06yUesTCqUMzb6bfX6EhIviuT0aQAhzp48WRw7TwMwCXecH2QNubBdDvUQ6YbFkflcf16FMcfhodEukk7xAPWplNgchXDgIwBE%2FEdq1bJtn301Wjktlbuk4vugH&X-Amz-Signature=0a5038139874cc336e51436084739780ceeb2f647dec39928a390a7973b4646b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMU4FHQH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWT0OjDdO%2BD1ettIFVIfDRqpNsJ9VSqsbANJJSDXVX1AiEAzyKgVBDfAfeqO5GysrrhvdaDObo07ddrVmgzCqLBlukqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC2h7W5%2FJhsxiB29WCrcA%2B%2BGxqN8lAtDWydVNxBBNaCG0IdOI5KK981kQ%2F%2BDJlMWbSsRP2sn2m8bt48GxZlAngtqNWEPpgxORauCnDO%2BEaKIKfosj9PN8nK%2Bg3eKcoKt3fI2mtW81CoLMeTKltW7WAZP%2FAoguswcn7Hp5SSPgtspPIAo6vNv3i0gp3CE6U82ud2S3iiQQUYPy3jBKZpArw656GY%2FkIWVL9Qj%2FyuEpwveQKxijStxl2qvcmm3mLifjSEfXf9vKvtkNrOxU%2F4f5nD%2BzX72PDEZ6dNVI1LfFhPE2z6R13nV%2BE3gjJWNGh0gDVaJ58Xr5yLZT9RXCQ%2BFxukOIzvqnaZzrvEgXD4Ub6FB%2B8pnkKaDRPZIOZF0IthvEL1EUzclgkybCgTgbtEMmjVUmy2H2jdGoTevi8u5YNgmGFNQiHuKfLFQHU1TMskydC6tCUAj3SLGY8GCEKf%2FWoeGLd1T1L%2FaX4%2BNHYwlgCCPK2Bw4gpvvlUnfg2Hj1nMdkSMqg2GKBym36AM6n9bj0i3XEL3dWmYzA4MxM81pE1edBSNZMvMUyco%2FqH%2FmkawgchcSIaAtNZBCbUuLkZHfx%2BLqsFkD7pOEXcproVz%2FGrXmPPgLxD0P5CGwNRSmZyUdyg5Z2Ga5RGnC02EMMeL7bwGOqUBp%2B3o05Z0XitxUWxBYrHhbB7wYAi%2BDcVuXq3LXgXdGwLszaDdIgPQd5xMMyqoqv9svSGO8FgQuQ6jzMiNCuwKkB6XdAz4xMYfW06yUesTCqUMzb6bfX6EhIviuT0aQAhzp48WRw7TwMwCXecH2QNubBdDvUQ6YbFkflcf16FMcfhodEukk7xAPWplNgchXDgIwBE%2FEdq1bJtn301Wjktlbuk4vugH&X-Amz-Signature=a37ed20db47a7c5d0c727a1a049a11d43f97f19aa832680a7f1badd93f57d367&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMU4FHQH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWT0OjDdO%2BD1ettIFVIfDRqpNsJ9VSqsbANJJSDXVX1AiEAzyKgVBDfAfeqO5GysrrhvdaDObo07ddrVmgzCqLBlukqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC2h7W5%2FJhsxiB29WCrcA%2B%2BGxqN8lAtDWydVNxBBNaCG0IdOI5KK981kQ%2F%2BDJlMWbSsRP2sn2m8bt48GxZlAngtqNWEPpgxORauCnDO%2BEaKIKfosj9PN8nK%2Bg3eKcoKt3fI2mtW81CoLMeTKltW7WAZP%2FAoguswcn7Hp5SSPgtspPIAo6vNv3i0gp3CE6U82ud2S3iiQQUYPy3jBKZpArw656GY%2FkIWVL9Qj%2FyuEpwveQKxijStxl2qvcmm3mLifjSEfXf9vKvtkNrOxU%2F4f5nD%2BzX72PDEZ6dNVI1LfFhPE2z6R13nV%2BE3gjJWNGh0gDVaJ58Xr5yLZT9RXCQ%2BFxukOIzvqnaZzrvEgXD4Ub6FB%2B8pnkKaDRPZIOZF0IthvEL1EUzclgkybCgTgbtEMmjVUmy2H2jdGoTevi8u5YNgmGFNQiHuKfLFQHU1TMskydC6tCUAj3SLGY8GCEKf%2FWoeGLd1T1L%2FaX4%2BNHYwlgCCPK2Bw4gpvvlUnfg2Hj1nMdkSMqg2GKBym36AM6n9bj0i3XEL3dWmYzA4MxM81pE1edBSNZMvMUyco%2FqH%2FmkawgchcSIaAtNZBCbUuLkZHfx%2BLqsFkD7pOEXcproVz%2FGrXmPPgLxD0P5CGwNRSmZyUdyg5Z2Ga5RGnC02EMMeL7bwGOqUBp%2B3o05Z0XitxUWxBYrHhbB7wYAi%2BDcVuXq3LXgXdGwLszaDdIgPQd5xMMyqoqv9svSGO8FgQuQ6jzMiNCuwKkB6XdAz4xMYfW06yUesTCqUMzb6bfX6EhIviuT0aQAhzp48WRw7TwMwCXecH2QNubBdDvUQ6YbFkflcf16FMcfhodEukk7xAPWplNgchXDgIwBE%2FEdq1bJtn301Wjktlbuk4vugH&X-Amz-Signature=840cb4666f1d5a73d3d5f599f8da4b647a795ecfc12bdd6f1fe453768daecf63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMU4FHQH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWT0OjDdO%2BD1ettIFVIfDRqpNsJ9VSqsbANJJSDXVX1AiEAzyKgVBDfAfeqO5GysrrhvdaDObo07ddrVmgzCqLBlukqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC2h7W5%2FJhsxiB29WCrcA%2B%2BGxqN8lAtDWydVNxBBNaCG0IdOI5KK981kQ%2F%2BDJlMWbSsRP2sn2m8bt48GxZlAngtqNWEPpgxORauCnDO%2BEaKIKfosj9PN8nK%2Bg3eKcoKt3fI2mtW81CoLMeTKltW7WAZP%2FAoguswcn7Hp5SSPgtspPIAo6vNv3i0gp3CE6U82ud2S3iiQQUYPy3jBKZpArw656GY%2FkIWVL9Qj%2FyuEpwveQKxijStxl2qvcmm3mLifjSEfXf9vKvtkNrOxU%2F4f5nD%2BzX72PDEZ6dNVI1LfFhPE2z6R13nV%2BE3gjJWNGh0gDVaJ58Xr5yLZT9RXCQ%2BFxukOIzvqnaZzrvEgXD4Ub6FB%2B8pnkKaDRPZIOZF0IthvEL1EUzclgkybCgTgbtEMmjVUmy2H2jdGoTevi8u5YNgmGFNQiHuKfLFQHU1TMskydC6tCUAj3SLGY8GCEKf%2FWoeGLd1T1L%2FaX4%2BNHYwlgCCPK2Bw4gpvvlUnfg2Hj1nMdkSMqg2GKBym36AM6n9bj0i3XEL3dWmYzA4MxM81pE1edBSNZMvMUyco%2FqH%2FmkawgchcSIaAtNZBCbUuLkZHfx%2BLqsFkD7pOEXcproVz%2FGrXmPPgLxD0P5CGwNRSmZyUdyg5Z2Ga5RGnC02EMMeL7bwGOqUBp%2B3o05Z0XitxUWxBYrHhbB7wYAi%2BDcVuXq3LXgXdGwLszaDdIgPQd5xMMyqoqv9svSGO8FgQuQ6jzMiNCuwKkB6XdAz4xMYfW06yUesTCqUMzb6bfX6EhIviuT0aQAhzp48WRw7TwMwCXecH2QNubBdDvUQ6YbFkflcf16FMcfhodEukk7xAPWplNgchXDgIwBE%2FEdq1bJtn301Wjktlbuk4vugH&X-Amz-Signature=6f94c443ca6d6b4e3de439629123454dce122d45c2d430a81b1756e758fbdc3a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMU4FHQH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAWT0OjDdO%2BD1ettIFVIfDRqpNsJ9VSqsbANJJSDXVX1AiEAzyKgVBDfAfeqO5GysrrhvdaDObo07ddrVmgzCqLBlukqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC2h7W5%2FJhsxiB29WCrcA%2B%2BGxqN8lAtDWydVNxBBNaCG0IdOI5KK981kQ%2F%2BDJlMWbSsRP2sn2m8bt48GxZlAngtqNWEPpgxORauCnDO%2BEaKIKfosj9PN8nK%2Bg3eKcoKt3fI2mtW81CoLMeTKltW7WAZP%2FAoguswcn7Hp5SSPgtspPIAo6vNv3i0gp3CE6U82ud2S3iiQQUYPy3jBKZpArw656GY%2FkIWVL9Qj%2FyuEpwveQKxijStxl2qvcmm3mLifjSEfXf9vKvtkNrOxU%2F4f5nD%2BzX72PDEZ6dNVI1LfFhPE2z6R13nV%2BE3gjJWNGh0gDVaJ58Xr5yLZT9RXCQ%2BFxukOIzvqnaZzrvEgXD4Ub6FB%2B8pnkKaDRPZIOZF0IthvEL1EUzclgkybCgTgbtEMmjVUmy2H2jdGoTevi8u5YNgmGFNQiHuKfLFQHU1TMskydC6tCUAj3SLGY8GCEKf%2FWoeGLd1T1L%2FaX4%2BNHYwlgCCPK2Bw4gpvvlUnfg2Hj1nMdkSMqg2GKBym36AM6n9bj0i3XEL3dWmYzA4MxM81pE1edBSNZMvMUyco%2FqH%2FmkawgchcSIaAtNZBCbUuLkZHfx%2BLqsFkD7pOEXcproVz%2FGrXmPPgLxD0P5CGwNRSmZyUdyg5Z2Ga5RGnC02EMMeL7bwGOqUBp%2B3o05Z0XitxUWxBYrHhbB7wYAi%2BDcVuXq3LXgXdGwLszaDdIgPQd5xMMyqoqv9svSGO8FgQuQ6jzMiNCuwKkB6XdAz4xMYfW06yUesTCqUMzb6bfX6EhIviuT0aQAhzp48WRw7TwMwCXecH2QNubBdDvUQ6YbFkflcf16FMcfhodEukk7xAPWplNgchXDgIwBE%2FEdq1bJtn301Wjktlbuk4vugH&X-Amz-Signature=ab0cb5ed774540e97de6c652084850121cfe63045b4d9b8fe4ce0584ce035304&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWKBQPQN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAUW51SoV9WAjMz2YemXOKfQjtj%2BDpSLej1tOUKDx4lmAiBq7jwDvMZ%2BWzQvi4Gx7SS%2B18SwrTDEjYavdzDYbNOFSSqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrb8u56xxTXp4enqMKtwDljwRp6f3jGHgg3TxqS2mZlU7QFyo4DNI5jn3euoIb6vQXR7%2ByAIDx4YPg6AyvFHC9HsmEFUzzt5xX27aAEpCH0Am1U5D5TYNHYjsIrL63aEztscJ6mFbzN5hYmLfpJJCR%2F%2FBWYfHthVrPPyM7Fm9Jj2YSvq1FVqRQwSTT6U3moNZZ3vFvCcXmR58VGYUux26h0vDX%2BrAaWLJtvXcuMdaO8ic63mPDgQE0ioJB4OTTLCPjcqSeCAYs97TLEoKKXoezY3Kyz5vntGvgAO7woeAcV2%2FYX2wI7kwzezWWdvQADRUpeLG9g0V57pgud8%2FBC2RyTfUsYe9t2BqT0uPr%2FupyIrFAUUZ%2B3leR9%2FbG82yridK7SKpmo4wrezvQBmh45zcVLydP%2Fti22e6XXJ1Mpj7IRmZp3G4Kl4E5mANQA4sU%2FPCG%2Bp%2BcHmUiZlkQUX6RDnZHQZzT%2FxQ2j83F2l%2F9pDFxPvfC4O1voqyZSHF3%2Fs241tQyq%2FwX5POnbqEnp0DSgQ44nPPKEgYoGekgVHPXvpSAFvoaXNd9RGlk6mKoI1uNCZ9deuLzC4EIAGAYSbk0RC0Xjal9B%2Ftn%2BVaYFQG9M3Rk6ijo3Ysj5x0mxvykOr2tAVqdBKy5xjUsh8qCkYwiIvtvAY6pgF2ADMOhRljkNaFjhwlLLEXjPKI4DYYqY5C1EU9Pq1vd%2FkiDUcAyt0Dux3nxx3MomaCDQAt427DpqdotNeZfoX0wjdR9ne6zhi2mjTIlt2p43pMw8aw9teTb2z%2FmqiV2PbmUpjDy6Nl8%2FKVF1Dqli74kz20fkIytvrRPFqF9jhU%2F8seFVYuz2Kfd%2BGXSIy%2B599NJoLiK6XY1n3KVQNx0OrwC%2FwINqTq&X-Amz-Signature=2fc0d517d0d8949e44330f9b06c06cdf6dfa3b5feff0e50d5696a1bdaf872322&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647RF7GX3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtRcq4J8GUOGn46fXuxZS7D%2Bwk3I39OoAuAlNtnslrOgIgbOxofAllklzOitfgIatFDiJTYn6pqIgDdcm40G1LSSoqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA7V7cyTwOxDEDG8%2FircAxIaK%2FupWKlwvhJBCEtvYFvZ7Iufm9lidjsN0iOILoxJl7meqBMmk30oo0BNdKSiguCgYK96Z87adgC4w%2Fm0chmWkoD%2Fb7LmMwHRhXsxL%2FY8FjJ9Dxm7g5WglHmXDQ4TwGC%2FRoeRsS4U0Jo2unPlbIlY8DwlcteOE67w%2FjYWpOEtd1Q%2FJc1y5KtYDFdGWiKsYJX%2FuPRJkC2WyFnzkJFEuR1ekbOfvDHQEkGoXDr8mx5LJWEsM1VAAaodFK%2BSzV0uXnRAIWGRptW3XsK4WpRFBq07O1hJDqptjGq%2BBZ2QfGl9KAsdbgAL%2FbIwcT%2BX%2B86Tq%2FVUONth28BoEW91Zgoh3TkUiW6JcwwkCbxT83TJR2uerDWmr5TwI7dtkmSH3Ovyd6vffr%2B8pbCki5BZZSLGivLjf470aGtWXVS%2BkfB0C66gIhcbKAwteN30eoGLmQo%2F7kWJ48K6JjTUWt4asLkKQI6BS7vl5%2B7UiuC01EOOQhIahIegt8Mxq2V92SwnPw3DfqMF4Y4Y0GQ00%2BeFxtJ%2FIB3FNMZ2hBIpRTsWbKBxV7OWENCVs9N%2FD%2BQPCnFx53kWf5TXPTI1JyiB06P%2BdyOXpIM8WYgxX%2F5DchN56hxvye%2FemDaR1%2Bk%2FOcruEl7xMPKK7bwGOqUBWraPIzj8Fy8u%2BZSZh6lGFQbTUT1rqRehzegIzijbOtP6YrvNlU93t%2F0rz7rU9UhmlZOOR3eRJzzs8I%2BrOBT8N6Mw%2FxXXbjxCzWomQWLLPTGLqn29o9x8VQo92uZNR9EDVztebMpxt3qDEDWR02Hdwv4XkKmtbkjsuR%2BDL9fvt6OcbLmSJSrRa%2BmAR1HKfgkLaAsD%2F%2ByCSUtDybNh5QZLX31ORz%2B2&X-Amz-Signature=3f074232de09290f103540b136b640bee4f85670b77e66022b292b7e237d24e8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDLVOFI2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwrWFRlak0k8581ktzWfojhODByngPBgWpbbAs4qSUbAIhAJ1dIudMC70ig9VzhPLUddUFrp%2BDKqr2RINEY4JRaEoWKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9XzUxozeBrx8Yeewq3APkqXQwA5tM%2Fb8JMy5zoul3u3V1jBbesuCRzfwk1U3a8E2ATEtJUwhtzxdeKxjhS239gnMBf0%2FSr%2BE%2B4rQiRA0zNcGLYXjAIFDt6dXBtrT%2BHle9Tu%2BbNpn%2FCHdlxAYDBuchnYz1VQBiyM3xRGZwKOwd%2FxsBAi%2FC3yPPXZL1A%2B598yH1SnzMOpfmRfjG3pAHJCbvougwLYyK5CURFj3WXLJGWWFO4%2FRHhyEBz8L4eHXfsh5APbGQUPwd6apYT41jnT0rlMN7EWweuW4queabVIdihYY7TxyPhCBFgaAJJw1QWoeYS%2FAv2Iy0PWPS3lNmtoY6k5CF9ugvEc1mHBhQTyZa6IV1xWQwfum5SkM%2BSlaXM6fEnobwffzlY2TizN7nY6W4zpBnsfnFoYD1XA9mc8ox2Exv%2FEs1A9%2BF0MADe47CpHVPGyZcpBeMrBOqBqs9%2FsqfElNT34qEXfo5yqERG394zDS3TQ6JgtfZ7W9lDNA15FXGK8QsPU0irZRR6%2FjWZCXuKAXLYXUg2oamC4mOuxc%2FLLDzc5EmwK5yu9adWLbrvnsS4bGr6fgAGuiI9kNtcP5IkEYF0bYJApr0aYRG8YEAmPdGVAklftyi5ju6v%2FolJePO%2FxlMNTTenHpw3DD3iu28BjqkASgdxJFOjJXxXHSyKQNEwvS9T9EDsARk6G08YrgI1H%2BDkdpSKGjqOllx5WAGXnwDyiavcYkJFet3j19BN4gNYOQ%2F42xoRD4qO1Wzhy4jqOY%2FDP%2FTsGB0%2FUkLg1oSENU6CkZHEiqsiSPNXANQvN9Mfce23tvJyvthLu6x653ZgCxosUwX%2BKdx1mO%2FG02X%2FFj%2F3BOTkBuaGXlVtm1fkmoWb1AZuwQC&X-Amz-Signature=84dc1fc52bb57c62eb5af9a30117aca1a3ff70147774706e9fc7d97e151612b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDLVOFI2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T101519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwrWFRlak0k8581ktzWfojhODByngPBgWpbbAs4qSUbAIhAJ1dIudMC70ig9VzhPLUddUFrp%2BDKqr2RINEY4JRaEoWKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9XzUxozeBrx8Yeewq3APkqXQwA5tM%2Fb8JMy5zoul3u3V1jBbesuCRzfwk1U3a8E2ATEtJUwhtzxdeKxjhS239gnMBf0%2FSr%2BE%2B4rQiRA0zNcGLYXjAIFDt6dXBtrT%2BHle9Tu%2BbNpn%2FCHdlxAYDBuchnYz1VQBiyM3xRGZwKOwd%2FxsBAi%2FC3yPPXZL1A%2B598yH1SnzMOpfmRfjG3pAHJCbvougwLYyK5CURFj3WXLJGWWFO4%2FRHhyEBz8L4eHXfsh5APbGQUPwd6apYT41jnT0rlMN7EWweuW4queabVIdihYY7TxyPhCBFgaAJJw1QWoeYS%2FAv2Iy0PWPS3lNmtoY6k5CF9ugvEc1mHBhQTyZa6IV1xWQwfum5SkM%2BSlaXM6fEnobwffzlY2TizN7nY6W4zpBnsfnFoYD1XA9mc8ox2Exv%2FEs1A9%2BF0MADe47CpHVPGyZcpBeMrBOqBqs9%2FsqfElNT34qEXfo5yqERG394zDS3TQ6JgtfZ7W9lDNA15FXGK8QsPU0irZRR6%2FjWZCXuKAXLYXUg2oamC4mOuxc%2FLLDzc5EmwK5yu9adWLbrvnsS4bGr6fgAGuiI9kNtcP5IkEYF0bYJApr0aYRG8YEAmPdGVAklftyi5ju6v%2FolJePO%2FxlMNTTenHpw3DD3iu28BjqkASgdxJFOjJXxXHSyKQNEwvS9T9EDsARk6G08YrgI1H%2BDkdpSKGjqOllx5WAGXnwDyiavcYkJFet3j19BN4gNYOQ%2F42xoRD4qO1Wzhy4jqOY%2FDP%2FTsGB0%2FUkLg1oSENU6CkZHEiqsiSPNXANQvN9Mfce23tvJyvthLu6x653ZgCxosUwX%2BKdx1mO%2FG02X%2FFj%2F3BOTkBuaGXlVtm1fkmoWb1AZuwQC&X-Amz-Signature=eda01faae4bc1becbbac59a5aca0801c8350d4f82ad5d469fa343d4c41e9e121&X-Amz-SignedHeaders=host&x-id=GetObject)
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
