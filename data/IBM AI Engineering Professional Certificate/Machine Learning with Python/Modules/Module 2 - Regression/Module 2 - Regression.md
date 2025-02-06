

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657SDNCNJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDmc%2BpJ7oeL8jNP9U4djdVH11vvVnyaxc7o0MrXJDaJfwIgNzAGhYVun2aJvcWNjRTj7%2BqFpNu6fJkw7zc7uMinA%2FYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHtls%2BrpplvKUCVK2CrcA3toAcHGu7d0SfHwosgu%2BM1aOJ5f%2FWUYemaCWoqxV01oWsG6aWWn9e8qPaRMcobs1QFheUCOQY%2BLeCTzFHjxVy5X91Z3ud%2BY7RsjZx%2F8f%2Bk2Wwl8nCVgCNHnc%2BhIjqDzD8Mf6WloGxzVrioBPW4kvk%2FpN%2BG2DSVIGQi4o%2F%2FvnyKU4PvMQFPi9Pc4zIiyAx3%2FWtLDLf38AfDD6vyJYg45xcKnHf74FA5IGXOyhRMJnOR9%2Fh1deWIQ9JCOKdgSylUdLZi52NEBn%2BakgAGHpROO7Kv2S9UXNqeF7w3cOoPbgwdSbHkOgBtXzJVz2U2iI3UNjRALfd%2BG2BrGO3eyMecJB7dzlWbqo%2B46fqiWuVIkUlxZANDdm7UClcEmnbhuuOfH7mMD33C3RvTAcvB5kQfNKRU7mff%2BVfFQbP%2BSjW37yt%2BMoWtpqIQbeDDd5Ar7kOKHirV69XslzLazPU4DbUwlI7rS7ZpvhCx5C0SiAVuWsG8Wbo%2FB6oBzsQgm1u5er5XSyg5JQuTXo9VkSE3j716cl8Jah5x6ASMPlSJUj%2Fm64lNJe2k%2BbxnhONKHB46m3kOPkycgklyJkuFDmcHG2tK9Vl5MovE%2BFrYvSLz8zZ5cisXofgO5Lcajl1Fyt52EMPbDkr0GOqUBLgiXtMYXfNLSMK1epu6CVCuIsU5IYkCfsiTO9Cv%2FrYTKa4FKC4R3G%2BBvgOIyyhtOhAoh%2FnobWZIH7VTRatcqmGu2Cnl3yEGne838q8IZT%2F4PGJTzi0%2BB8qt8cYsv59Df7VM4V%2BrK%2Fi7ah2%2Bz%2FYRbG3BcoJbvNIoaxp5cFOQuEw711Xl%2BmVOHMMsbuBDxtQo3DYIm8Pz92H2DTkBWptFTBaqsbY8%2F&X-Amz-Signature=3e40c99a7f1dcc0b29b6084a6a6b01252c73d85e8b0cbda757b4c904a3671f2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657SDNCNJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDmc%2BpJ7oeL8jNP9U4djdVH11vvVnyaxc7o0MrXJDaJfwIgNzAGhYVun2aJvcWNjRTj7%2BqFpNu6fJkw7zc7uMinA%2FYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHtls%2BrpplvKUCVK2CrcA3toAcHGu7d0SfHwosgu%2BM1aOJ5f%2FWUYemaCWoqxV01oWsG6aWWn9e8qPaRMcobs1QFheUCOQY%2BLeCTzFHjxVy5X91Z3ud%2BY7RsjZx%2F8f%2Bk2Wwl8nCVgCNHnc%2BhIjqDzD8Mf6WloGxzVrioBPW4kvk%2FpN%2BG2DSVIGQi4o%2F%2FvnyKU4PvMQFPi9Pc4zIiyAx3%2FWtLDLf38AfDD6vyJYg45xcKnHf74FA5IGXOyhRMJnOR9%2Fh1deWIQ9JCOKdgSylUdLZi52NEBn%2BakgAGHpROO7Kv2S9UXNqeF7w3cOoPbgwdSbHkOgBtXzJVz2U2iI3UNjRALfd%2BG2BrGO3eyMecJB7dzlWbqo%2B46fqiWuVIkUlxZANDdm7UClcEmnbhuuOfH7mMD33C3RvTAcvB5kQfNKRU7mff%2BVfFQbP%2BSjW37yt%2BMoWtpqIQbeDDd5Ar7kOKHirV69XslzLazPU4DbUwlI7rS7ZpvhCx5C0SiAVuWsG8Wbo%2FB6oBzsQgm1u5er5XSyg5JQuTXo9VkSE3j716cl8Jah5x6ASMPlSJUj%2Fm64lNJe2k%2BbxnhONKHB46m3kOPkycgklyJkuFDmcHG2tK9Vl5MovE%2BFrYvSLz8zZ5cisXofgO5Lcajl1Fyt52EMPbDkr0GOqUBLgiXtMYXfNLSMK1epu6CVCuIsU5IYkCfsiTO9Cv%2FrYTKa4FKC4R3G%2BBvgOIyyhtOhAoh%2FnobWZIH7VTRatcqmGu2Cnl3yEGne838q8IZT%2F4PGJTzi0%2BB8qt8cYsv59Df7VM4V%2BrK%2Fi7ah2%2Bz%2FYRbG3BcoJbvNIoaxp5cFOQuEw711Xl%2BmVOHMMsbuBDxtQo3DYIm8Pz92H2DTkBWptFTBaqsbY8%2F&X-Amz-Signature=8edd1fb3752f54b6c86291f913f5b8c41fb97bd59ed12fc9b9410b9a507d5385&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657SDNCNJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDmc%2BpJ7oeL8jNP9U4djdVH11vvVnyaxc7o0MrXJDaJfwIgNzAGhYVun2aJvcWNjRTj7%2BqFpNu6fJkw7zc7uMinA%2FYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHtls%2BrpplvKUCVK2CrcA3toAcHGu7d0SfHwosgu%2BM1aOJ5f%2FWUYemaCWoqxV01oWsG6aWWn9e8qPaRMcobs1QFheUCOQY%2BLeCTzFHjxVy5X91Z3ud%2BY7RsjZx%2F8f%2Bk2Wwl8nCVgCNHnc%2BhIjqDzD8Mf6WloGxzVrioBPW4kvk%2FpN%2BG2DSVIGQi4o%2F%2FvnyKU4PvMQFPi9Pc4zIiyAx3%2FWtLDLf38AfDD6vyJYg45xcKnHf74FA5IGXOyhRMJnOR9%2Fh1deWIQ9JCOKdgSylUdLZi52NEBn%2BakgAGHpROO7Kv2S9UXNqeF7w3cOoPbgwdSbHkOgBtXzJVz2U2iI3UNjRALfd%2BG2BrGO3eyMecJB7dzlWbqo%2B46fqiWuVIkUlxZANDdm7UClcEmnbhuuOfH7mMD33C3RvTAcvB5kQfNKRU7mff%2BVfFQbP%2BSjW37yt%2BMoWtpqIQbeDDd5Ar7kOKHirV69XslzLazPU4DbUwlI7rS7ZpvhCx5C0SiAVuWsG8Wbo%2FB6oBzsQgm1u5er5XSyg5JQuTXo9VkSE3j716cl8Jah5x6ASMPlSJUj%2Fm64lNJe2k%2BbxnhONKHB46m3kOPkycgklyJkuFDmcHG2tK9Vl5MovE%2BFrYvSLz8zZ5cisXofgO5Lcajl1Fyt52EMPbDkr0GOqUBLgiXtMYXfNLSMK1epu6CVCuIsU5IYkCfsiTO9Cv%2FrYTKa4FKC4R3G%2BBvgOIyyhtOhAoh%2FnobWZIH7VTRatcqmGu2Cnl3yEGne838q8IZT%2F4PGJTzi0%2BB8qt8cYsv59Df7VM4V%2BrK%2Fi7ah2%2Bz%2FYRbG3BcoJbvNIoaxp5cFOQuEw711Xl%2BmVOHMMsbuBDxtQo3DYIm8Pz92H2DTkBWptFTBaqsbY8%2F&X-Amz-Signature=b1cbbb3331fbfd519c410d043e46068307a390ad3a3e4180c1399b94f11225d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657SDNCNJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDmc%2BpJ7oeL8jNP9U4djdVH11vvVnyaxc7o0MrXJDaJfwIgNzAGhYVun2aJvcWNjRTj7%2BqFpNu6fJkw7zc7uMinA%2FYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHtls%2BrpplvKUCVK2CrcA3toAcHGu7d0SfHwosgu%2BM1aOJ5f%2FWUYemaCWoqxV01oWsG6aWWn9e8qPaRMcobs1QFheUCOQY%2BLeCTzFHjxVy5X91Z3ud%2BY7RsjZx%2F8f%2Bk2Wwl8nCVgCNHnc%2BhIjqDzD8Mf6WloGxzVrioBPW4kvk%2FpN%2BG2DSVIGQi4o%2F%2FvnyKU4PvMQFPi9Pc4zIiyAx3%2FWtLDLf38AfDD6vyJYg45xcKnHf74FA5IGXOyhRMJnOR9%2Fh1deWIQ9JCOKdgSylUdLZi52NEBn%2BakgAGHpROO7Kv2S9UXNqeF7w3cOoPbgwdSbHkOgBtXzJVz2U2iI3UNjRALfd%2BG2BrGO3eyMecJB7dzlWbqo%2B46fqiWuVIkUlxZANDdm7UClcEmnbhuuOfH7mMD33C3RvTAcvB5kQfNKRU7mff%2BVfFQbP%2BSjW37yt%2BMoWtpqIQbeDDd5Ar7kOKHirV69XslzLazPU4DbUwlI7rS7ZpvhCx5C0SiAVuWsG8Wbo%2FB6oBzsQgm1u5er5XSyg5JQuTXo9VkSE3j716cl8Jah5x6ASMPlSJUj%2Fm64lNJe2k%2BbxnhONKHB46m3kOPkycgklyJkuFDmcHG2tK9Vl5MovE%2BFrYvSLz8zZ5cisXofgO5Lcajl1Fyt52EMPbDkr0GOqUBLgiXtMYXfNLSMK1epu6CVCuIsU5IYkCfsiTO9Cv%2FrYTKa4FKC4R3G%2BBvgOIyyhtOhAoh%2FnobWZIH7VTRatcqmGu2Cnl3yEGne838q8IZT%2F4PGJTzi0%2BB8qt8cYsv59Df7VM4V%2BrK%2Fi7ah2%2Bz%2FYRbG3BcoJbvNIoaxp5cFOQuEw711Xl%2BmVOHMMsbuBDxtQo3DYIm8Pz92H2DTkBWptFTBaqsbY8%2F&X-Amz-Signature=e51ba85627208fa72a5f3e7d6f66d8bab4ca7a502f5dc921c434db48795100c0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657SDNCNJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDmc%2BpJ7oeL8jNP9U4djdVH11vvVnyaxc7o0MrXJDaJfwIgNzAGhYVun2aJvcWNjRTj7%2BqFpNu6fJkw7zc7uMinA%2FYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHtls%2BrpplvKUCVK2CrcA3toAcHGu7d0SfHwosgu%2BM1aOJ5f%2FWUYemaCWoqxV01oWsG6aWWn9e8qPaRMcobs1QFheUCOQY%2BLeCTzFHjxVy5X91Z3ud%2BY7RsjZx%2F8f%2Bk2Wwl8nCVgCNHnc%2BhIjqDzD8Mf6WloGxzVrioBPW4kvk%2FpN%2BG2DSVIGQi4o%2F%2FvnyKU4PvMQFPi9Pc4zIiyAx3%2FWtLDLf38AfDD6vyJYg45xcKnHf74FA5IGXOyhRMJnOR9%2Fh1deWIQ9JCOKdgSylUdLZi52NEBn%2BakgAGHpROO7Kv2S9UXNqeF7w3cOoPbgwdSbHkOgBtXzJVz2U2iI3UNjRALfd%2BG2BrGO3eyMecJB7dzlWbqo%2B46fqiWuVIkUlxZANDdm7UClcEmnbhuuOfH7mMD33C3RvTAcvB5kQfNKRU7mff%2BVfFQbP%2BSjW37yt%2BMoWtpqIQbeDDd5Ar7kOKHirV69XslzLazPU4DbUwlI7rS7ZpvhCx5C0SiAVuWsG8Wbo%2FB6oBzsQgm1u5er5XSyg5JQuTXo9VkSE3j716cl8Jah5x6ASMPlSJUj%2Fm64lNJe2k%2BbxnhONKHB46m3kOPkycgklyJkuFDmcHG2tK9Vl5MovE%2BFrYvSLz8zZ5cisXofgO5Lcajl1Fyt52EMPbDkr0GOqUBLgiXtMYXfNLSMK1epu6CVCuIsU5IYkCfsiTO9Cv%2FrYTKa4FKC4R3G%2BBvgOIyyhtOhAoh%2FnobWZIH7VTRatcqmGu2Cnl3yEGne838q8IZT%2F4PGJTzi0%2BB8qt8cYsv59Df7VM4V%2BrK%2Fi7ah2%2Bz%2FYRbG3BcoJbvNIoaxp5cFOQuEw711Xl%2BmVOHMMsbuBDxtQo3DYIm8Pz92H2DTkBWptFTBaqsbY8%2F&X-Amz-Signature=b451545302b6cd43f5ce1dbf71411f5a09a234e58b12bb323477e5e8c6b330d3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657SDNCNJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDmc%2BpJ7oeL8jNP9U4djdVH11vvVnyaxc7o0MrXJDaJfwIgNzAGhYVun2aJvcWNjRTj7%2BqFpNu6fJkw7zc7uMinA%2FYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHtls%2BrpplvKUCVK2CrcA3toAcHGu7d0SfHwosgu%2BM1aOJ5f%2FWUYemaCWoqxV01oWsG6aWWn9e8qPaRMcobs1QFheUCOQY%2BLeCTzFHjxVy5X91Z3ud%2BY7RsjZx%2F8f%2Bk2Wwl8nCVgCNHnc%2BhIjqDzD8Mf6WloGxzVrioBPW4kvk%2FpN%2BG2DSVIGQi4o%2F%2FvnyKU4PvMQFPi9Pc4zIiyAx3%2FWtLDLf38AfDD6vyJYg45xcKnHf74FA5IGXOyhRMJnOR9%2Fh1deWIQ9JCOKdgSylUdLZi52NEBn%2BakgAGHpROO7Kv2S9UXNqeF7w3cOoPbgwdSbHkOgBtXzJVz2U2iI3UNjRALfd%2BG2BrGO3eyMecJB7dzlWbqo%2B46fqiWuVIkUlxZANDdm7UClcEmnbhuuOfH7mMD33C3RvTAcvB5kQfNKRU7mff%2BVfFQbP%2BSjW37yt%2BMoWtpqIQbeDDd5Ar7kOKHirV69XslzLazPU4DbUwlI7rS7ZpvhCx5C0SiAVuWsG8Wbo%2FB6oBzsQgm1u5er5XSyg5JQuTXo9VkSE3j716cl8Jah5x6ASMPlSJUj%2Fm64lNJe2k%2BbxnhONKHB46m3kOPkycgklyJkuFDmcHG2tK9Vl5MovE%2BFrYvSLz8zZ5cisXofgO5Lcajl1Fyt52EMPbDkr0GOqUBLgiXtMYXfNLSMK1epu6CVCuIsU5IYkCfsiTO9Cv%2FrYTKa4FKC4R3G%2BBvgOIyyhtOhAoh%2FnobWZIH7VTRatcqmGu2Cnl3yEGne838q8IZT%2F4PGJTzi0%2BB8qt8cYsv59Df7VM4V%2BrK%2Fi7ah2%2Bz%2FYRbG3BcoJbvNIoaxp5cFOQuEw711Xl%2BmVOHMMsbuBDxtQo3DYIm8Pz92H2DTkBWptFTBaqsbY8%2F&X-Amz-Signature=11daf060fe901817326e435e4d4a010c1e10a06c167e00ecc770e51858f2a89d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657SDNCNJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDmc%2BpJ7oeL8jNP9U4djdVH11vvVnyaxc7o0MrXJDaJfwIgNzAGhYVun2aJvcWNjRTj7%2BqFpNu6fJkw7zc7uMinA%2FYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHtls%2BrpplvKUCVK2CrcA3toAcHGu7d0SfHwosgu%2BM1aOJ5f%2FWUYemaCWoqxV01oWsG6aWWn9e8qPaRMcobs1QFheUCOQY%2BLeCTzFHjxVy5X91Z3ud%2BY7RsjZx%2F8f%2Bk2Wwl8nCVgCNHnc%2BhIjqDzD8Mf6WloGxzVrioBPW4kvk%2FpN%2BG2DSVIGQi4o%2F%2FvnyKU4PvMQFPi9Pc4zIiyAx3%2FWtLDLf38AfDD6vyJYg45xcKnHf74FA5IGXOyhRMJnOR9%2Fh1deWIQ9JCOKdgSylUdLZi52NEBn%2BakgAGHpROO7Kv2S9UXNqeF7w3cOoPbgwdSbHkOgBtXzJVz2U2iI3UNjRALfd%2BG2BrGO3eyMecJB7dzlWbqo%2B46fqiWuVIkUlxZANDdm7UClcEmnbhuuOfH7mMD33C3RvTAcvB5kQfNKRU7mff%2BVfFQbP%2BSjW37yt%2BMoWtpqIQbeDDd5Ar7kOKHirV69XslzLazPU4DbUwlI7rS7ZpvhCx5C0SiAVuWsG8Wbo%2FB6oBzsQgm1u5er5XSyg5JQuTXo9VkSE3j716cl8Jah5x6ASMPlSJUj%2Fm64lNJe2k%2BbxnhONKHB46m3kOPkycgklyJkuFDmcHG2tK9Vl5MovE%2BFrYvSLz8zZ5cisXofgO5Lcajl1Fyt52EMPbDkr0GOqUBLgiXtMYXfNLSMK1epu6CVCuIsU5IYkCfsiTO9Cv%2FrYTKa4FKC4R3G%2BBvgOIyyhtOhAoh%2FnobWZIH7VTRatcqmGu2Cnl3yEGne838q8IZT%2F4PGJTzi0%2BB8qt8cYsv59Df7VM4V%2BrK%2Fi7ah2%2Bz%2FYRbG3BcoJbvNIoaxp5cFOQuEw711Xl%2BmVOHMMsbuBDxtQo3DYIm8Pz92H2DTkBWptFTBaqsbY8%2F&X-Amz-Signature=b6e4b1fc722ef12a39d0a9df2fabeb2c9df9206dd649ba0ab24af762fbce514e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657SDNCNJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDmc%2BpJ7oeL8jNP9U4djdVH11vvVnyaxc7o0MrXJDaJfwIgNzAGhYVun2aJvcWNjRTj7%2BqFpNu6fJkw7zc7uMinA%2FYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHtls%2BrpplvKUCVK2CrcA3toAcHGu7d0SfHwosgu%2BM1aOJ5f%2FWUYemaCWoqxV01oWsG6aWWn9e8qPaRMcobs1QFheUCOQY%2BLeCTzFHjxVy5X91Z3ud%2BY7RsjZx%2F8f%2Bk2Wwl8nCVgCNHnc%2BhIjqDzD8Mf6WloGxzVrioBPW4kvk%2FpN%2BG2DSVIGQi4o%2F%2FvnyKU4PvMQFPi9Pc4zIiyAx3%2FWtLDLf38AfDD6vyJYg45xcKnHf74FA5IGXOyhRMJnOR9%2Fh1deWIQ9JCOKdgSylUdLZi52NEBn%2BakgAGHpROO7Kv2S9UXNqeF7w3cOoPbgwdSbHkOgBtXzJVz2U2iI3UNjRALfd%2BG2BrGO3eyMecJB7dzlWbqo%2B46fqiWuVIkUlxZANDdm7UClcEmnbhuuOfH7mMD33C3RvTAcvB5kQfNKRU7mff%2BVfFQbP%2BSjW37yt%2BMoWtpqIQbeDDd5Ar7kOKHirV69XslzLazPU4DbUwlI7rS7ZpvhCx5C0SiAVuWsG8Wbo%2FB6oBzsQgm1u5er5XSyg5JQuTXo9VkSE3j716cl8Jah5x6ASMPlSJUj%2Fm64lNJe2k%2BbxnhONKHB46m3kOPkycgklyJkuFDmcHG2tK9Vl5MovE%2BFrYvSLz8zZ5cisXofgO5Lcajl1Fyt52EMPbDkr0GOqUBLgiXtMYXfNLSMK1epu6CVCuIsU5IYkCfsiTO9Cv%2FrYTKa4FKC4R3G%2BBvgOIyyhtOhAoh%2FnobWZIH7VTRatcqmGu2Cnl3yEGne838q8IZT%2F4PGJTzi0%2BB8qt8cYsv59Df7VM4V%2BrK%2Fi7ah2%2Bz%2FYRbG3BcoJbvNIoaxp5cFOQuEw711Xl%2BmVOHMMsbuBDxtQo3DYIm8Pz92H2DTkBWptFTBaqsbY8%2F&X-Amz-Signature=385d1635390e269e922f3af4bd3be2831e7ba2ec88e607fcbe11ff51117c6723&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAZCXSG6%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCAbJHYmkMAoPIx6HdKcLUUq7BzFcFjiNwimw5ZlUuISQIgD67E3UAxdRA%2BezbWwPu3fxX46qfR17uYvZWHOPkFA6Qq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDNfdZVb6%2FtKJWKSvoSrcA5JMi4u1Khs%2Bw9HnJZqEqpMw8dgeWK4x8rCzxydu52%2FWECcCbTb%2B79V6R4YCXgpIwvlT%2B%2FHhzirgAfnkNxOOPAVUWkI6jEaF3UzHdDNHR2ofUDDzkhCAORr8u6KekhIqMy9XET9NR05%2BLY4BS4VncsYvn1GAu4zAj%2FDm78LXjDi9WVHsHSnazuiOb5tVuZesEurtqAH6WhpTl2K6DI5ljV3cVHL1jyNfFxadBeUGGfLu3W1WQBJyHVqi0ymntgNPgdOlRKgKDAGAelBRHk3dZv1iQduYYmIGsSe1HSFfuzcqAoGRGLqrYVy05batDRDA7hLCYf5CK36%2FMTcMaGtb0DLRIyoE711HymzVEY39NYiYvPF%2BZMcLNex8XsE6yRd%2F898IJlh8Y6TnHQsnFWeZq4Fkhb1L6M9zGvsRvVm9dxGDdufFLeVnPIZYDTVi8UnjgJDh%2BetZJdHdTfM3uD6j0hZDrPXkOJy%2Fk9gdB4ql8e3sHPBRoeArkrRLYKA2omVrWXdd7ZR%2FBjQvTLBuDStnFu11V2jrw7IRXMJvvyVnemZAaeSvWV7G57r2NAdKev5S%2FdPPAFoRdCGOcTFKARAKImX61sTs73zyT6ZIWaIy4CvG1okOPFooRv37HAbkMN7Dkr0GOqUBjupO27QKSb1iGikTbRgu5cUkGRyE2WEDSiYFvbOo7%2FU3CWDLI6zbQdz90FOMXbYaqOpcS1Hayxcmga54R6gxvN3P6KOoLXfkDQw9syMM%2BoB4vUl0OZfi979PXNhSlv06yVQkO8uuh%2BCQoEmMe0EQ9%2FoP5XKhS0nPT0Xz3va08RksNgaYAvO7wPph1akNcapMPdL%2B0rqJ%2B%2Flob7Vi8GQde4Pz4ew8&X-Amz-Signature=24bd699737899407214a346c2ab379af49ac59262bc4b64a4d0fb25811e589f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MW3RFQG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCCb%2BFpfFlV%2B5oBVDS99x1DYkCN40GLKeJNxOYeyMPa4QIgNsY5m0Bji%2BQLrp3AJJBljViftgQB58JhcReG5y6BGfIq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDD6UhhNQIOKjVaW0VCrcA%2FL%2FUbf%2FFzKvtrhhf%2BvikemCZG1bYTucZAIo1oWV8NkKUY8zzX%2FpBbplIlLx%2BHsUhZy1KGJW4tghtj4st9FzZApJ5L4PJRPhFwj%2Bk80BlR8T60VYR%2BFpoUIEbpp5D8ZVYFFb2dlg0dQxJtaKesBbs8szmgnR6Lk5mMcdG6G0zDWv7fMo0Cbew3MSJHO9X0StvuTUEACIqwOmmr8PeYXmorLklfYRUCjqaFaitxrjL6OuUjgrpFKUl2e5Yz1wpZvD%2B30%2FIgSEVfZrwWa34ULrsD9swvT19tT%2FU%2BjYlWdJjvNdfOOZCQzkTxMxLc0Hg1f5v0U9y0aXrb3MDPLap7Pu%2Bnez1XwqI4y8ChSKgI9SmBX0WYaDQSlrSGQ33K9Z%2BQSiu%2ByZ4oh1Zmqr%2FiarS9CWu%2FFh6Qq88OQWTWUnwXk9yJvy3jutHgJk69oK4DEYg3HJu9pcxvdt9sJzwkOe13r10e3Z2w65vcraTTgzDKvZk3bBhN9bbqSz1vMPJr74uKxV9Acem3tSukx%2B3b4yGhMyfYAHaIEk5tw3atwajalNe6YWhZVD3jJvNbOcC0MEbeDbB6D%2FbwzW%2Fi%2FDluc56RO%2BqPVGvFCJNy4VMwTMjYYXm3FCoaBoJ0SV9YGQ%2F2%2BLMM7Dkr0GOqUB%2F1sH7Q88R2nPWWMmpYStT9zAJEAQ77UV6OdCeQEwA22qSktmVFkOHNXECXa%2BPIP0qNiQ%2F3MBZLfyV%2Fo2YwxpKGahJFxoEw%2FmZrFk2KxamDNKsXuNXCiC%2FZItK6hoyrAJykkEH33AhWdobif4QTSVtKDuPt6Jpj2KD1VePUWE5BcfhKUE7K42LaqYMbZKtEQ5PwON5XWfUAs%2BZbTXUoI7IsyJ6i9v&X-Amz-Signature=1b07d0111b71f2d27667e599fc05cd4cdcda3560862e03d4c2a3b68582241d00&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNTERLBJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJFMEMCIEvkvYKTFPf0iiFTi9o9WDbQKwf7PdPevQeFVmn5Mo1yAh9LX0z%2Fg6L20pZQ1lPr7OTgxMiCgRNmtCsbkqIPa5rgKv8DCF0QABoMNjM3NDIzMTgzODA1IgyNpQRqlduMq1%2F29fgq3AN%2F%2BX1ME26stWvnDmN5pgXuoIfx2iBs8ngul9kxVJEBVW8gMkI5MdcDSz1OQcZasJQPB8gkIlh08I6RlaMeXKJaEwDAlxwmuHa8Lyzmc30a0Z1Co2NqoQi9FWbXC4a6TR8nxprjzSJ%2BTGiBzx1%2FcLi9mOJ2Qx0jqg2zN%2FDsQ%2FINsGUD%2BvKFH8qlWQKECOnLCRA6qTEEJRFbC%2FvZ6f4jtw%2BfhiLNexxi5E%2FG%2BIiwBRJ8CdcwKJz52FxqlAMJs6w%2F0VvhGlrWIeE9HGzwgVJ646Un6e1rLc1y3lG98QiqgaWb20JjkoJ0XAXCeQULVdH1QInD8shCgapc%2Fq1dkxPmg%2Fg9ddrNXEsejRBFK6D2wM0slTi4k1GfaVSLWoJILJXKmbQDgYLYDUoacJN1oxrUNAXYVlQYw1O09DNTJToXWoSalzZIdzzEkJfQ5LoKTSRzF9dj09RblCFAe7txbUxgeQZbNo6Mo%2FXqnUFBi6Pbu01qThcQ4n3%2FDDEhFaGQthhI%2FwONM66nIrRMV0CFo73K8hZ7HShm8M2CupoSNoiiWad7dGlMILdXxyQM%2BSyne7mKRlctPGmRfd0kg1RiZ4VkJXrUv74DZPNcKh19wPsA4lYDYixJB%2F2jsISxBWHLYzCbxJK9BjqnAaLW8O5IohZnGkiDUlFJ1MR%2Fx4Wovd7bn9jstpdU3nDpZQcH4uB85mNxGCGBl4DdqQ%2FLUO%2FBeSrmuWXQV4fs4l0BocSHVoqZ6pvWQcMMMTpkif8CaSuH7f9Vs6NMrTDSi03%2BOcoE4nEL4Vo5eB8QfnOMr%2BSK5BP5%2FFSwXnSMU%2Bkd10GiPgdOAJmq4K1YQiDtTTlvBBqzsuD3fmLw1AkoMn1tV3L%2BwmSB&X-Amz-Signature=0482ed6f74ffd0c935e8b712c9de2c6993372a017be00e55799cdeb98d5a8f6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNTERLBJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJFMEMCIEvkvYKTFPf0iiFTi9o9WDbQKwf7PdPevQeFVmn5Mo1yAh9LX0z%2Fg6L20pZQ1lPr7OTgxMiCgRNmtCsbkqIPa5rgKv8DCF0QABoMNjM3NDIzMTgzODA1IgyNpQRqlduMq1%2F29fgq3AN%2F%2BX1ME26stWvnDmN5pgXuoIfx2iBs8ngul9kxVJEBVW8gMkI5MdcDSz1OQcZasJQPB8gkIlh08I6RlaMeXKJaEwDAlxwmuHa8Lyzmc30a0Z1Co2NqoQi9FWbXC4a6TR8nxprjzSJ%2BTGiBzx1%2FcLi9mOJ2Qx0jqg2zN%2FDsQ%2FINsGUD%2BvKFH8qlWQKECOnLCRA6qTEEJRFbC%2FvZ6f4jtw%2BfhiLNexxi5E%2FG%2BIiwBRJ8CdcwKJz52FxqlAMJs6w%2F0VvhGlrWIeE9HGzwgVJ646Un6e1rLc1y3lG98QiqgaWb20JjkoJ0XAXCeQULVdH1QInD8shCgapc%2Fq1dkxPmg%2Fg9ddrNXEsejRBFK6D2wM0slTi4k1GfaVSLWoJILJXKmbQDgYLYDUoacJN1oxrUNAXYVlQYw1O09DNTJToXWoSalzZIdzzEkJfQ5LoKTSRzF9dj09RblCFAe7txbUxgeQZbNo6Mo%2FXqnUFBi6Pbu01qThcQ4n3%2FDDEhFaGQthhI%2FwONM66nIrRMV0CFo73K8hZ7HShm8M2CupoSNoiiWad7dGlMILdXxyQM%2BSyne7mKRlctPGmRfd0kg1RiZ4VkJXrUv74DZPNcKh19wPsA4lYDYixJB%2F2jsISxBWHLYzCbxJK9BjqnAaLW8O5IohZnGkiDUlFJ1MR%2Fx4Wovd7bn9jstpdU3nDpZQcH4uB85mNxGCGBl4DdqQ%2FLUO%2FBeSrmuWXQV4fs4l0BocSHVoqZ6pvWQcMMMTpkif8CaSuH7f9Vs6NMrTDSi03%2BOcoE4nEL4Vo5eB8QfnOMr%2BSK5BP5%2FFSwXnSMU%2Bkd10GiPgdOAJmq4K1YQiDtTTlvBBqzsuD3fmLw1AkoMn1tV3L%2BwmSB&X-Amz-Signature=6aec5857161abcaf4fe928cc1bd02a724e3d466587b9962617f843bd72af606d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
