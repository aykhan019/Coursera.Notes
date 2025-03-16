

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZBHIORF%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICr%2BSwznbl8MyEUbyU3T6AongDLls4BishtRH1HZP46uAiEAqQJY5PYiUt82lBlyMSB20k3rUuGMv5a268u1%2Fl8CaPAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDBUaghJbJwMGK6QY6CrcAzne6uFIXxCuvm2NMn59%2BV01anDNLMyZhAP3yCb0W890R6oP9mODGqpogjIZDgCZnCzybH%2Fy%2FCETt0QIMiT8jZWC0PIXhBuvbJ7tOko1kbaEpDGZIvkZls%2BwTXQzbXcE6JS9%2FhBI6NXXsukxS8QhOfbTsIilQgW1V2d3YjIcyWELLDOx5gA2kA8GZ8Pke94GAXHQrD%2FlH0HYSW9dr0F2Zuyivm1ji3uc4vVcU00PX9cCh5BTyZGJQt5bmBuZFYxGQTVGUOa%2Bz8kQqTCq1q%2FNwgatqVuy7UYnfj0UbhrRvaTRHNXErD1AhGd%2FnnNu2ovMvXQygnMxV8eCWgPfAlTmAoD1UmHStx3tZK0JjoISF1fPgZ4kyrcdfwyjVvq9CPDPubqJfyiZ24kbJt49g6K2vUgkNsN7tg6OoXMSbMN3tvPwABJuhNo8kWEy10gDVhljFRur8Rb8EsThGEqpYnapZ3l7%2FHvUh4m0iQyWHYbhwgHDODoKzkomToapMcsAoWuAQguzS0wtTXnDF%2B9rfYyNpuJpMBetddvvBOTyglfOaGZjqX8LT5CrcjGeUGRxLsCnELk8ArW%2FSilE4ZubYAyJNaN0tBrd6ywDsTO4Gw8G7sgkExh%2FocS6EL9XbuAdMMr%2F174GOqUB4RhIfcRtvzKyz2MqPfdDw4wyh%2FJydR2Q3MppBf2PwXyt3EvbOTYzBDW6%2BtWYkow8rNzeLNSo0wX9MzJSncfv3k6ganmC0EawY6dfMOvSYTEjIgP9EaQUoAXNF1mZM1%2FlwGiJYvSqrpq7XbzmAqweMbCiJ4Mho3%2BedC1zHXO%2B%2F51CW%2FPy7huOzYPYlAE6pgggPplztXEUg%2B65kMJYSA7KlCSLfLpz&X-Amz-Signature=b266677317bfa55514f6b198e3ba6e30897c165f501a6ef926717029fc4534b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZBHIORF%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICr%2BSwznbl8MyEUbyU3T6AongDLls4BishtRH1HZP46uAiEAqQJY5PYiUt82lBlyMSB20k3rUuGMv5a268u1%2Fl8CaPAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDBUaghJbJwMGK6QY6CrcAzne6uFIXxCuvm2NMn59%2BV01anDNLMyZhAP3yCb0W890R6oP9mODGqpogjIZDgCZnCzybH%2Fy%2FCETt0QIMiT8jZWC0PIXhBuvbJ7tOko1kbaEpDGZIvkZls%2BwTXQzbXcE6JS9%2FhBI6NXXsukxS8QhOfbTsIilQgW1V2d3YjIcyWELLDOx5gA2kA8GZ8Pke94GAXHQrD%2FlH0HYSW9dr0F2Zuyivm1ji3uc4vVcU00PX9cCh5BTyZGJQt5bmBuZFYxGQTVGUOa%2Bz8kQqTCq1q%2FNwgatqVuy7UYnfj0UbhrRvaTRHNXErD1AhGd%2FnnNu2ovMvXQygnMxV8eCWgPfAlTmAoD1UmHStx3tZK0JjoISF1fPgZ4kyrcdfwyjVvq9CPDPubqJfyiZ24kbJt49g6K2vUgkNsN7tg6OoXMSbMN3tvPwABJuhNo8kWEy10gDVhljFRur8Rb8EsThGEqpYnapZ3l7%2FHvUh4m0iQyWHYbhwgHDODoKzkomToapMcsAoWuAQguzS0wtTXnDF%2B9rfYyNpuJpMBetddvvBOTyglfOaGZjqX8LT5CrcjGeUGRxLsCnELk8ArW%2FSilE4ZubYAyJNaN0tBrd6ywDsTO4Gw8G7sgkExh%2FocS6EL9XbuAdMMr%2F174GOqUB4RhIfcRtvzKyz2MqPfdDw4wyh%2FJydR2Q3MppBf2PwXyt3EvbOTYzBDW6%2BtWYkow8rNzeLNSo0wX9MzJSncfv3k6ganmC0EawY6dfMOvSYTEjIgP9EaQUoAXNF1mZM1%2FlwGiJYvSqrpq7XbzmAqweMbCiJ4Mho3%2BedC1zHXO%2B%2F51CW%2FPy7huOzYPYlAE6pgggPplztXEUg%2B65kMJYSA7KlCSLfLpz&X-Amz-Signature=723a062fe3f2938d7a9e7b2c6d2457f5a0493f56496aa8c6802e0dbdac070635&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZBHIORF%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICr%2BSwznbl8MyEUbyU3T6AongDLls4BishtRH1HZP46uAiEAqQJY5PYiUt82lBlyMSB20k3rUuGMv5a268u1%2Fl8CaPAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDBUaghJbJwMGK6QY6CrcAzne6uFIXxCuvm2NMn59%2BV01anDNLMyZhAP3yCb0W890R6oP9mODGqpogjIZDgCZnCzybH%2Fy%2FCETt0QIMiT8jZWC0PIXhBuvbJ7tOko1kbaEpDGZIvkZls%2BwTXQzbXcE6JS9%2FhBI6NXXsukxS8QhOfbTsIilQgW1V2d3YjIcyWELLDOx5gA2kA8GZ8Pke94GAXHQrD%2FlH0HYSW9dr0F2Zuyivm1ji3uc4vVcU00PX9cCh5BTyZGJQt5bmBuZFYxGQTVGUOa%2Bz8kQqTCq1q%2FNwgatqVuy7UYnfj0UbhrRvaTRHNXErD1AhGd%2FnnNu2ovMvXQygnMxV8eCWgPfAlTmAoD1UmHStx3tZK0JjoISF1fPgZ4kyrcdfwyjVvq9CPDPubqJfyiZ24kbJt49g6K2vUgkNsN7tg6OoXMSbMN3tvPwABJuhNo8kWEy10gDVhljFRur8Rb8EsThGEqpYnapZ3l7%2FHvUh4m0iQyWHYbhwgHDODoKzkomToapMcsAoWuAQguzS0wtTXnDF%2B9rfYyNpuJpMBetddvvBOTyglfOaGZjqX8LT5CrcjGeUGRxLsCnELk8ArW%2FSilE4ZubYAyJNaN0tBrd6ywDsTO4Gw8G7sgkExh%2FocS6EL9XbuAdMMr%2F174GOqUB4RhIfcRtvzKyz2MqPfdDw4wyh%2FJydR2Q3MppBf2PwXyt3EvbOTYzBDW6%2BtWYkow8rNzeLNSo0wX9MzJSncfv3k6ganmC0EawY6dfMOvSYTEjIgP9EaQUoAXNF1mZM1%2FlwGiJYvSqrpq7XbzmAqweMbCiJ4Mho3%2BedC1zHXO%2B%2F51CW%2FPy7huOzYPYlAE6pgggPplztXEUg%2B65kMJYSA7KlCSLfLpz&X-Amz-Signature=5cd90148354b48740d7f9fb6f581481132fb861dc881e075adf174e750602ea5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZBHIORF%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICr%2BSwznbl8MyEUbyU3T6AongDLls4BishtRH1HZP46uAiEAqQJY5PYiUt82lBlyMSB20k3rUuGMv5a268u1%2Fl8CaPAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDBUaghJbJwMGK6QY6CrcAzne6uFIXxCuvm2NMn59%2BV01anDNLMyZhAP3yCb0W890R6oP9mODGqpogjIZDgCZnCzybH%2Fy%2FCETt0QIMiT8jZWC0PIXhBuvbJ7tOko1kbaEpDGZIvkZls%2BwTXQzbXcE6JS9%2FhBI6NXXsukxS8QhOfbTsIilQgW1V2d3YjIcyWELLDOx5gA2kA8GZ8Pke94GAXHQrD%2FlH0HYSW9dr0F2Zuyivm1ji3uc4vVcU00PX9cCh5BTyZGJQt5bmBuZFYxGQTVGUOa%2Bz8kQqTCq1q%2FNwgatqVuy7UYnfj0UbhrRvaTRHNXErD1AhGd%2FnnNu2ovMvXQygnMxV8eCWgPfAlTmAoD1UmHStx3tZK0JjoISF1fPgZ4kyrcdfwyjVvq9CPDPubqJfyiZ24kbJt49g6K2vUgkNsN7tg6OoXMSbMN3tvPwABJuhNo8kWEy10gDVhljFRur8Rb8EsThGEqpYnapZ3l7%2FHvUh4m0iQyWHYbhwgHDODoKzkomToapMcsAoWuAQguzS0wtTXnDF%2B9rfYyNpuJpMBetddvvBOTyglfOaGZjqX8LT5CrcjGeUGRxLsCnELk8ArW%2FSilE4ZubYAyJNaN0tBrd6ywDsTO4Gw8G7sgkExh%2FocS6EL9XbuAdMMr%2F174GOqUB4RhIfcRtvzKyz2MqPfdDw4wyh%2FJydR2Q3MppBf2PwXyt3EvbOTYzBDW6%2BtWYkow8rNzeLNSo0wX9MzJSncfv3k6ganmC0EawY6dfMOvSYTEjIgP9EaQUoAXNF1mZM1%2FlwGiJYvSqrpq7XbzmAqweMbCiJ4Mho3%2BedC1zHXO%2B%2F51CW%2FPy7huOzYPYlAE6pgggPplztXEUg%2B65kMJYSA7KlCSLfLpz&X-Amz-Signature=8954d58ef6dfc2921f61cb9d5f7fe663a78978f82d8dcaeb8eaf50eab29cf7f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZBHIORF%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICr%2BSwznbl8MyEUbyU3T6AongDLls4BishtRH1HZP46uAiEAqQJY5PYiUt82lBlyMSB20k3rUuGMv5a268u1%2Fl8CaPAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDBUaghJbJwMGK6QY6CrcAzne6uFIXxCuvm2NMn59%2BV01anDNLMyZhAP3yCb0W890R6oP9mODGqpogjIZDgCZnCzybH%2Fy%2FCETt0QIMiT8jZWC0PIXhBuvbJ7tOko1kbaEpDGZIvkZls%2BwTXQzbXcE6JS9%2FhBI6NXXsukxS8QhOfbTsIilQgW1V2d3YjIcyWELLDOx5gA2kA8GZ8Pke94GAXHQrD%2FlH0HYSW9dr0F2Zuyivm1ji3uc4vVcU00PX9cCh5BTyZGJQt5bmBuZFYxGQTVGUOa%2Bz8kQqTCq1q%2FNwgatqVuy7UYnfj0UbhrRvaTRHNXErD1AhGd%2FnnNu2ovMvXQygnMxV8eCWgPfAlTmAoD1UmHStx3tZK0JjoISF1fPgZ4kyrcdfwyjVvq9CPDPubqJfyiZ24kbJt49g6K2vUgkNsN7tg6OoXMSbMN3tvPwABJuhNo8kWEy10gDVhljFRur8Rb8EsThGEqpYnapZ3l7%2FHvUh4m0iQyWHYbhwgHDODoKzkomToapMcsAoWuAQguzS0wtTXnDF%2B9rfYyNpuJpMBetddvvBOTyglfOaGZjqX8LT5CrcjGeUGRxLsCnELk8ArW%2FSilE4ZubYAyJNaN0tBrd6ywDsTO4Gw8G7sgkExh%2FocS6EL9XbuAdMMr%2F174GOqUB4RhIfcRtvzKyz2MqPfdDw4wyh%2FJydR2Q3MppBf2PwXyt3EvbOTYzBDW6%2BtWYkow8rNzeLNSo0wX9MzJSncfv3k6ganmC0EawY6dfMOvSYTEjIgP9EaQUoAXNF1mZM1%2FlwGiJYvSqrpq7XbzmAqweMbCiJ4Mho3%2BedC1zHXO%2B%2F51CW%2FPy7huOzYPYlAE6pgggPplztXEUg%2B65kMJYSA7KlCSLfLpz&X-Amz-Signature=0f9c6b7a5c524bfc2ed7641fa2fd47aade65e4dea5cb7d3507c54343f9ab1670&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZBHIORF%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICr%2BSwznbl8MyEUbyU3T6AongDLls4BishtRH1HZP46uAiEAqQJY5PYiUt82lBlyMSB20k3rUuGMv5a268u1%2Fl8CaPAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDBUaghJbJwMGK6QY6CrcAzne6uFIXxCuvm2NMn59%2BV01anDNLMyZhAP3yCb0W890R6oP9mODGqpogjIZDgCZnCzybH%2Fy%2FCETt0QIMiT8jZWC0PIXhBuvbJ7tOko1kbaEpDGZIvkZls%2BwTXQzbXcE6JS9%2FhBI6NXXsukxS8QhOfbTsIilQgW1V2d3YjIcyWELLDOx5gA2kA8GZ8Pke94GAXHQrD%2FlH0HYSW9dr0F2Zuyivm1ji3uc4vVcU00PX9cCh5BTyZGJQt5bmBuZFYxGQTVGUOa%2Bz8kQqTCq1q%2FNwgatqVuy7UYnfj0UbhrRvaTRHNXErD1AhGd%2FnnNu2ovMvXQygnMxV8eCWgPfAlTmAoD1UmHStx3tZK0JjoISF1fPgZ4kyrcdfwyjVvq9CPDPubqJfyiZ24kbJt49g6K2vUgkNsN7tg6OoXMSbMN3tvPwABJuhNo8kWEy10gDVhljFRur8Rb8EsThGEqpYnapZ3l7%2FHvUh4m0iQyWHYbhwgHDODoKzkomToapMcsAoWuAQguzS0wtTXnDF%2B9rfYyNpuJpMBetddvvBOTyglfOaGZjqX8LT5CrcjGeUGRxLsCnELk8ArW%2FSilE4ZubYAyJNaN0tBrd6ywDsTO4Gw8G7sgkExh%2FocS6EL9XbuAdMMr%2F174GOqUB4RhIfcRtvzKyz2MqPfdDw4wyh%2FJydR2Q3MppBf2PwXyt3EvbOTYzBDW6%2BtWYkow8rNzeLNSo0wX9MzJSncfv3k6ganmC0EawY6dfMOvSYTEjIgP9EaQUoAXNF1mZM1%2FlwGiJYvSqrpq7XbzmAqweMbCiJ4Mho3%2BedC1zHXO%2B%2F51CW%2FPy7huOzYPYlAE6pgggPplztXEUg%2B65kMJYSA7KlCSLfLpz&X-Amz-Signature=bda5aa89c780d414bad0ff8464b40457c6611e11d99d3167eada35cf2dc24800&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZBHIORF%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICr%2BSwznbl8MyEUbyU3T6AongDLls4BishtRH1HZP46uAiEAqQJY5PYiUt82lBlyMSB20k3rUuGMv5a268u1%2Fl8CaPAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDBUaghJbJwMGK6QY6CrcAzne6uFIXxCuvm2NMn59%2BV01anDNLMyZhAP3yCb0W890R6oP9mODGqpogjIZDgCZnCzybH%2Fy%2FCETt0QIMiT8jZWC0PIXhBuvbJ7tOko1kbaEpDGZIvkZls%2BwTXQzbXcE6JS9%2FhBI6NXXsukxS8QhOfbTsIilQgW1V2d3YjIcyWELLDOx5gA2kA8GZ8Pke94GAXHQrD%2FlH0HYSW9dr0F2Zuyivm1ji3uc4vVcU00PX9cCh5BTyZGJQt5bmBuZFYxGQTVGUOa%2Bz8kQqTCq1q%2FNwgatqVuy7UYnfj0UbhrRvaTRHNXErD1AhGd%2FnnNu2ovMvXQygnMxV8eCWgPfAlTmAoD1UmHStx3tZK0JjoISF1fPgZ4kyrcdfwyjVvq9CPDPubqJfyiZ24kbJt49g6K2vUgkNsN7tg6OoXMSbMN3tvPwABJuhNo8kWEy10gDVhljFRur8Rb8EsThGEqpYnapZ3l7%2FHvUh4m0iQyWHYbhwgHDODoKzkomToapMcsAoWuAQguzS0wtTXnDF%2B9rfYyNpuJpMBetddvvBOTyglfOaGZjqX8LT5CrcjGeUGRxLsCnELk8ArW%2FSilE4ZubYAyJNaN0tBrd6ywDsTO4Gw8G7sgkExh%2FocS6EL9XbuAdMMr%2F174GOqUB4RhIfcRtvzKyz2MqPfdDw4wyh%2FJydR2Q3MppBf2PwXyt3EvbOTYzBDW6%2BtWYkow8rNzeLNSo0wX9MzJSncfv3k6ganmC0EawY6dfMOvSYTEjIgP9EaQUoAXNF1mZM1%2FlwGiJYvSqrpq7XbzmAqweMbCiJ4Mho3%2BedC1zHXO%2B%2F51CW%2FPy7huOzYPYlAE6pgggPplztXEUg%2B65kMJYSA7KlCSLfLpz&X-Amz-Signature=715e790456a6e3e30fc230837644e3dd586e0ca8f5b32f6880047ecaa448aae3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZBHIORF%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICr%2BSwznbl8MyEUbyU3T6AongDLls4BishtRH1HZP46uAiEAqQJY5PYiUt82lBlyMSB20k3rUuGMv5a268u1%2Fl8CaPAq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDBUaghJbJwMGK6QY6CrcAzne6uFIXxCuvm2NMn59%2BV01anDNLMyZhAP3yCb0W890R6oP9mODGqpogjIZDgCZnCzybH%2Fy%2FCETt0QIMiT8jZWC0PIXhBuvbJ7tOko1kbaEpDGZIvkZls%2BwTXQzbXcE6JS9%2FhBI6NXXsukxS8QhOfbTsIilQgW1V2d3YjIcyWELLDOx5gA2kA8GZ8Pke94GAXHQrD%2FlH0HYSW9dr0F2Zuyivm1ji3uc4vVcU00PX9cCh5BTyZGJQt5bmBuZFYxGQTVGUOa%2Bz8kQqTCq1q%2FNwgatqVuy7UYnfj0UbhrRvaTRHNXErD1AhGd%2FnnNu2ovMvXQygnMxV8eCWgPfAlTmAoD1UmHStx3tZK0JjoISF1fPgZ4kyrcdfwyjVvq9CPDPubqJfyiZ24kbJt49g6K2vUgkNsN7tg6OoXMSbMN3tvPwABJuhNo8kWEy10gDVhljFRur8Rb8EsThGEqpYnapZ3l7%2FHvUh4m0iQyWHYbhwgHDODoKzkomToapMcsAoWuAQguzS0wtTXnDF%2B9rfYyNpuJpMBetddvvBOTyglfOaGZjqX8LT5CrcjGeUGRxLsCnELk8ArW%2FSilE4ZubYAyJNaN0tBrd6ywDsTO4Gw8G7sgkExh%2FocS6EL9XbuAdMMr%2F174GOqUB4RhIfcRtvzKyz2MqPfdDw4wyh%2FJydR2Q3MppBf2PwXyt3EvbOTYzBDW6%2BtWYkow8rNzeLNSo0wX9MzJSncfv3k6ganmC0EawY6dfMOvSYTEjIgP9EaQUoAXNF1mZM1%2FlwGiJYvSqrpq7XbzmAqweMbCiJ4Mho3%2BedC1zHXO%2B%2F51CW%2FPy7huOzYPYlAE6pgggPplztXEUg%2B65kMJYSA7KlCSLfLpz&X-Amz-Signature=a15757a88dfb7fa5fbdb70b5de21f3501beb3c359b28a0457c0e2a2a3162bd4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZJJ5T5N%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDdCwxeLStTWepvEaauAls6tLbP5Ppa8YEJhEdZpxbrIAiAeBxAI9Y2JzbBK8hTSCT74t3od4Mz8Q6IRwjPii5qaTir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMIJNiugDYDPKzt7TFKtwD1CF2%2BQzsrfuU07dlyIHUPKnpc5IgwoBU%2Fu3mvLmPUiaFyQ2mwpghfX7E1eZZI%2BsBubViQOx58qJZdSKX%2F3brm%2Fzj%2BobdWSkhFf9m0r8uNZO2ioQsowEi87SYWoYUa0aghB2lqvorsDlqm%2BK2k98V3jKm28GpeBYIr8fXrCVa0gIHUl8qzbWaZD9zc7vIkTxLBKzPrJt1FfDYsqw1rOjUvpzSV%2BM4KVmUOqtMI1mF%2B0%2FwZfe9rDH4RYhNJNkO2apVm0YhX2FLlG%2FIhXO%2FTZz18w%2FztlBOI3unkSXOq%2FESowZd0%2FQ%2FiL73nkiZFZHz6Fh4aTeajBhbBz%2FvbK5r7sA3M3F8hjAMl4dXAgEihICZU8t9ntabQyzVUbl3mgGuTFPgh27dTUrvonB8AQYss7PXu4Tf0LiQkdmAG0%2B2SYQ7TdjH6JtPmv5xkeVJV5zh5fVbCz11r3Y8OKkA%2FUsclhyWxnLSVGTIuWJVBAuXUOLGyESN0341dpX2g5BP84iv4XEqH3HzYtGhiiQ7uaGNLjb15v6GD1MxRcegIKKm%2BEzLyDwPS0bQWant8XrFbTdVV7kHjfIqZrFPSiWeeb8aKMUzE%2FcSU3%2FOggFEwttZ48RaSObOyJFXBG82QLF0tgQwm%2F%2FXvgY6pgEKGcuPzpIpIiK%2Bv%2FcypXoBSujk8kveCouLSIwCqEi8nNb8Q%2Bm9Aq4MEOQQqOLekP5dPTfUqdsGa%2FTeWP0VCriY6sYndBQ9GbxJTvDgtl66R46o0MY6lZcja7Qyh78efXHrdTn71JkWSEk4Nol%2Bn97Lz1OkDyFW%2BlHIG6t0240mlQfG7XJFNN6m27TpGwJBFY80vr%2BidG59m1ZXwHj5bgcQ65fAdmIv&X-Amz-Signature=1554b2e0bb7d5f7edb419a22a07d48d25eed24c50fc09f02172c2ad0c24b6e19&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJAXS5RJ%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDLwi2Jj99HBCd%2FiebTHp%2Bdo%2B7FaPHs8Jm9jCL%2BbQ%2FoeAiEAmMoRDuz%2BQss8dbzXyWp3l17Lecg%2Fx0QiwS6DszqO%2BsQq%2FwMIIBAAGgw2Mzc0MjMxODM4MDUiDNnIHxoV7IbJ9WHhVSrcA6zSLZlZUvR7cLVeJeqWiT28GONUTXcimTo0meHazdxDEkm3GjGag6khCdlBjEW9FkwSqgqS51CdFENMg9DmtuM%2BH1allG%2BB7I3hQg9Gdu0t%2BDlXx0EzVXrvp8zzQ7%2FI%2BKsVTtb18EK7m7Dny8Rex1us%2FUXs8hugcxtL%2Bu5EMzOL36tI8WnSKz%2FAG1Jg6UZAWyXm4Gc9kqOkTPMBRvheeZYE75Sd6Mhjsh0vzYz2LfGDhozJkFBJkxLOKz8i8o2WOSoLeyjtrRSVj8PgZGTcYUh%2BthbBurVRyEN43cO4DMK6mm5fWZ7m9hpdXigNbgNcRswPoYuBN6sfRrZy1rLCZulH3hwvvV9PSejyiBBQ0phZZ5%2FhB9CSvmOBUhgrF%2F9b1Qk3HnrMuIeDeYNLYiLZw5CD8Nc7AM3w9tM%2F55cfvcqQtg2gqj02X8WI09a1AEwbTP38NCTzGklZbQTpmNHVv918INvzLEn6lJ%2FEAJxYKkn%2BbDjPjumLMcR%2BA2z4WhOIn%2Fx1mcAdDvAr%2BaXRTas1d7X8ZOsDpKYm8NL305V1sBH6SBXIeQZ0NusL3cb5DRvQ3dl4smBKYZGTmAP26ilsrxitlPZ%2FTPYx8R3W%2FXHnacCG0NqTqYw%2FW%2BfsvyydMMT%2F174GOqUBS9Lf7VSCvzdFQQAcRk5K%2B2rFtHHVs3xehJEEkI7zoE1U8ipBfJvRC%2B37%2BaP3vhPcxI9NDqkyCI9rjr5w%2B%2FjDrhNvovhy7FSXmigTq0HWXyyztFXi7UpH7L%2BbevnmONOPYu6BBtA%2F%2BUMZA%2FBKOjUnGLjKxtozOOnWQPimZptzYNz7kEhwrlQ%2F8YMk9nFykAN4yTcYgNuAarh6%2FqSwSmc27jovZlYb&X-Amz-Signature=11d23eaf35aa4bfeed38cdcf5bf2a9b3c3dd28c9727f8b4bc6723aeda3a39c0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JU46QTF%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDRGN7ZGR8MnFhNkNb96J7CA6jySBiyCT00p%2BbK0rgVMAiBgJpFHFLpBGjukU9GENP3JTx0gTMYW9ReOBwp471YQfCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMmXWq5Yvc9KHcG1eDKtwDsk8N9frIAHoIe84RObRENTb%2FAZb5oAT99ypXJNhXMAgz4vlVoG0rlaBIU31madXFf5l79URI3n%2FritLzxb%2BdgrOr0mxQgQ22WiAGNqVL22t0E75XwJ%2BZjbeQModvFvK3zN8NBwF6tga6cwv9GZRew8snydlqzl%2BqJhgPCJl6Vt%2B8%2Fm4vWzR%2BKgpUaYzX3p8kI%2Fww%2BSiNdE%2BFluTTz%2BeK18z95IVXX%2B5DELG3N5nKzP%2FFMCLcNhgXszJlRS%2BrIfIzjn51Yw1NTXDdDFw4U%2Fs6AmmjMgSBGrbjJiN3YdP%2FQhqI9E1ECfiqir0vTHNypq%2FPifFFfAb%2FdBY23fkHglMS%2FH9nt%2FojJj3c%2Boofmw2Azi%2B5BlxF3rYvjjVdD5duwt6YKYQlrleyPOK4OUALS3I98owrC5uzX9%2BOEJrCm2ezTwSeKWImqwrXz0SMiZUlFOWNhBX7%2FZPZC9ni2WkAmdcQ5VVluvAYPoHd8bwV%2BgrsQJhpZfKmP79WNsNxZEpONHJU5j%2FqPUl3AiZ4PDUba9Kvt0%2Fiz3B2dNuS4Tk4pxOB%2FazSk8JHClnXJ7IMOf38DFynKhwpor1lpYz9K9YoVyko%2B%2BzUsZyh4%2FRdKk71LtruqgQ%2FFyrMuLBOHBSUkr4w4f%2FXvgY6pgGuOqRFNJILwYyJgrwpKoraaDAkNYhMbKrbzThzG0fKhKN1JvJYPJ3NLUolxp9MbpWEbwOGtCa%2FJQDfSnMnjH1Xd4Vq1rajmVxmhenn7qhspW%2BzZ9BAsZIw9WZt5iT5nQs%2Fvw1N%2FSJ3Y97odh%2FGPI9ZtOYW7lJwbGEorVQfjCWKIV4uq%2FmpBitKD61dgLolH8p1aBenyHB9eTyelvWvgO%2B1gFRxdcoP&X-Amz-Signature=d9fbd34e1f7a561479cc01cb01d5883292a0535029332460ef0a46d84c3fc048&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JU46QTF%2F20250316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250316T004410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDRGN7ZGR8MnFhNkNb96J7CA6jySBiyCT00p%2BbK0rgVMAiBgJpFHFLpBGjukU9GENP3JTx0gTMYW9ReOBwp471YQfCr%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMmXWq5Yvc9KHcG1eDKtwDsk8N9frIAHoIe84RObRENTb%2FAZb5oAT99ypXJNhXMAgz4vlVoG0rlaBIU31madXFf5l79URI3n%2FritLzxb%2BdgrOr0mxQgQ22WiAGNqVL22t0E75XwJ%2BZjbeQModvFvK3zN8NBwF6tga6cwv9GZRew8snydlqzl%2BqJhgPCJl6Vt%2B8%2Fm4vWzR%2BKgpUaYzX3p8kI%2Fww%2BSiNdE%2BFluTTz%2BeK18z95IVXX%2B5DELG3N5nKzP%2FFMCLcNhgXszJlRS%2BrIfIzjn51Yw1NTXDdDFw4U%2Fs6AmmjMgSBGrbjJiN3YdP%2FQhqI9E1ECfiqir0vTHNypq%2FPifFFfAb%2FdBY23fkHglMS%2FH9nt%2FojJj3c%2Boofmw2Azi%2B5BlxF3rYvjjVdD5duwt6YKYQlrleyPOK4OUALS3I98owrC5uzX9%2BOEJrCm2ezTwSeKWImqwrXz0SMiZUlFOWNhBX7%2FZPZC9ni2WkAmdcQ5VVluvAYPoHd8bwV%2BgrsQJhpZfKmP79WNsNxZEpONHJU5j%2FqPUl3AiZ4PDUba9Kvt0%2Fiz3B2dNuS4Tk4pxOB%2FazSk8JHClnXJ7IMOf38DFynKhwpor1lpYz9K9YoVyko%2B%2BzUsZyh4%2FRdKk71LtruqgQ%2FFyrMuLBOHBSUkr4w4f%2FXvgY6pgGuOqRFNJILwYyJgrwpKoraaDAkNYhMbKrbzThzG0fKhKN1JvJYPJ3NLUolxp9MbpWEbwOGtCa%2FJQDfSnMnjH1Xd4Vq1rajmVxmhenn7qhspW%2BzZ9BAsZIw9WZt5iT5nQs%2Fvw1N%2FSJ3Y97odh%2FGPI9ZtOYW7lJwbGEorVQfjCWKIV4uq%2FmpBitKD61dgLolH8p1aBenyHB9eTyelvWvgO%2B1gFRxdcoP&X-Amz-Signature=5a0ab71cf11c55eaadb6591dd4f9a341d76aecb04dcab82e0bb6f5ac68f50f3d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
