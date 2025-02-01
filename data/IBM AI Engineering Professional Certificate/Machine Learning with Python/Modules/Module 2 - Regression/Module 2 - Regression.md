

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQE2SQTO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDleNRklK9W70yWfGqu%2Bl1IJZwv0OlOLT%2BLK1T8jpFy%2FwIhAN845NJ3SgAsbQzHzB7ZOw%2FpQ7LV5uAb4lRRS%2BU0OYRHKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0fiWu6MxPaR3rWbIq3AOUJ6J75ChJEnI%2BI5oKf7rLFzsSipCthw%2BNllHffLhom5%2FU6WPwyHXTPbjnfj91sDFpUOAca3GI0JvDMhNyKvY%2BT4ZbPKuaVigAdRfNQO9gbsqbYNEX8io%2BnHKImPiepiPRbjzxS6xJpgZe81ZbyQs5uQ1OKjKN0AmQQC%2B6oThmZSckuHZimsENgEDYAjCmmns3KX0e7%2FhIOT24VOHNmHz8y1oJiw3s0pxNtjX%2FQk4eK1DzQKZebn%2B5qKuXx9gRmjx%2B17KUznGOgQn9vviLUlyVsQXoWmGxDL6sUNXxn%2BVMbmeIuKKwThps6aYY3AAtn7s1CUADP%2BBc2JJI1Rsr2q5AClG5tMgG9fp1qV1wTDtUmLfnpR93gL17fB5HDlonHPdz%2FRklYyhy0rmrMwGVlp2pVMFTzOMjhn9bm3VLYoeUGGUJxrrwxY9MBHL7RSobJpOH3PFSCQPesVAB25H5UqcahdTatfBc10Md8O%2BEbK1RFqC0GZoCBEp9V%2FlbE963XJCkmlIURA5mrny62Xofj9cGjV0GSZOIg68nZUtQAq4AIDI25onS14X9fX8uPSu%2F6qvAQSt%2FWW2vU6bQeWY1E9618%2Fu%2B1NG2JEwSWonQLrfM66BR77l%2B8XvXa%2BasezC%2FpPe8BjqkATKt2uLLp9ZRCEssYW3F5Dhev3Wc%2BLYbaY7gZp14YlaEy%2B0XOSg05Shk%2B4viT2B1X6BYthRMSU3Xy%2B9Nrw2WzBScdwII9VkJ5dSZE5eTW0RZqFINI1evSVE6VSh12TJmDzQSR1rfNQEazJG2t9cnuZZUsUpgl2HVrtcHcEx0rco2F9b6Xy5NKJq5H3ma9iiJ5aV9H15cg9XX9LV%2Fladd77uu9zli&X-Amz-Signature=84aa20e40bd40ca1d24394792e8a0f5800a160ddb450bc855ccc2b31331081a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQE2SQTO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDleNRklK9W70yWfGqu%2Bl1IJZwv0OlOLT%2BLK1T8jpFy%2FwIhAN845NJ3SgAsbQzHzB7ZOw%2FpQ7LV5uAb4lRRS%2BU0OYRHKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0fiWu6MxPaR3rWbIq3AOUJ6J75ChJEnI%2BI5oKf7rLFzsSipCthw%2BNllHffLhom5%2FU6WPwyHXTPbjnfj91sDFpUOAca3GI0JvDMhNyKvY%2BT4ZbPKuaVigAdRfNQO9gbsqbYNEX8io%2BnHKImPiepiPRbjzxS6xJpgZe81ZbyQs5uQ1OKjKN0AmQQC%2B6oThmZSckuHZimsENgEDYAjCmmns3KX0e7%2FhIOT24VOHNmHz8y1oJiw3s0pxNtjX%2FQk4eK1DzQKZebn%2B5qKuXx9gRmjx%2B17KUznGOgQn9vviLUlyVsQXoWmGxDL6sUNXxn%2BVMbmeIuKKwThps6aYY3AAtn7s1CUADP%2BBc2JJI1Rsr2q5AClG5tMgG9fp1qV1wTDtUmLfnpR93gL17fB5HDlonHPdz%2FRklYyhy0rmrMwGVlp2pVMFTzOMjhn9bm3VLYoeUGGUJxrrwxY9MBHL7RSobJpOH3PFSCQPesVAB25H5UqcahdTatfBc10Md8O%2BEbK1RFqC0GZoCBEp9V%2FlbE963XJCkmlIURA5mrny62Xofj9cGjV0GSZOIg68nZUtQAq4AIDI25onS14X9fX8uPSu%2F6qvAQSt%2FWW2vU6bQeWY1E9618%2Fu%2B1NG2JEwSWonQLrfM66BR77l%2B8XvXa%2BasezC%2FpPe8BjqkATKt2uLLp9ZRCEssYW3F5Dhev3Wc%2BLYbaY7gZp14YlaEy%2B0XOSg05Shk%2B4viT2B1X6BYthRMSU3Xy%2B9Nrw2WzBScdwII9VkJ5dSZE5eTW0RZqFINI1evSVE6VSh12TJmDzQSR1rfNQEazJG2t9cnuZZUsUpgl2HVrtcHcEx0rco2F9b6Xy5NKJq5H3ma9iiJ5aV9H15cg9XX9LV%2Fladd77uu9zli&X-Amz-Signature=80f93e574bfaff58db08afdea72e9f069cfcb902fe5442fd369e86d6368c3074&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQE2SQTO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDleNRklK9W70yWfGqu%2Bl1IJZwv0OlOLT%2BLK1T8jpFy%2FwIhAN845NJ3SgAsbQzHzB7ZOw%2FpQ7LV5uAb4lRRS%2BU0OYRHKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0fiWu6MxPaR3rWbIq3AOUJ6J75ChJEnI%2BI5oKf7rLFzsSipCthw%2BNllHffLhom5%2FU6WPwyHXTPbjnfj91sDFpUOAca3GI0JvDMhNyKvY%2BT4ZbPKuaVigAdRfNQO9gbsqbYNEX8io%2BnHKImPiepiPRbjzxS6xJpgZe81ZbyQs5uQ1OKjKN0AmQQC%2B6oThmZSckuHZimsENgEDYAjCmmns3KX0e7%2FhIOT24VOHNmHz8y1oJiw3s0pxNtjX%2FQk4eK1DzQKZebn%2B5qKuXx9gRmjx%2B17KUznGOgQn9vviLUlyVsQXoWmGxDL6sUNXxn%2BVMbmeIuKKwThps6aYY3AAtn7s1CUADP%2BBc2JJI1Rsr2q5AClG5tMgG9fp1qV1wTDtUmLfnpR93gL17fB5HDlonHPdz%2FRklYyhy0rmrMwGVlp2pVMFTzOMjhn9bm3VLYoeUGGUJxrrwxY9MBHL7RSobJpOH3PFSCQPesVAB25H5UqcahdTatfBc10Md8O%2BEbK1RFqC0GZoCBEp9V%2FlbE963XJCkmlIURA5mrny62Xofj9cGjV0GSZOIg68nZUtQAq4AIDI25onS14X9fX8uPSu%2F6qvAQSt%2FWW2vU6bQeWY1E9618%2Fu%2B1NG2JEwSWonQLrfM66BR77l%2B8XvXa%2BasezC%2FpPe8BjqkATKt2uLLp9ZRCEssYW3F5Dhev3Wc%2BLYbaY7gZp14YlaEy%2B0XOSg05Shk%2B4viT2B1X6BYthRMSU3Xy%2B9Nrw2WzBScdwII9VkJ5dSZE5eTW0RZqFINI1evSVE6VSh12TJmDzQSR1rfNQEazJG2t9cnuZZUsUpgl2HVrtcHcEx0rco2F9b6Xy5NKJq5H3ma9iiJ5aV9H15cg9XX9LV%2Fladd77uu9zli&X-Amz-Signature=544779e6a1c627a1812d53befaaa0574b19595f8c07793418b6983fac43acde4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQE2SQTO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDleNRklK9W70yWfGqu%2Bl1IJZwv0OlOLT%2BLK1T8jpFy%2FwIhAN845NJ3SgAsbQzHzB7ZOw%2FpQ7LV5uAb4lRRS%2BU0OYRHKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0fiWu6MxPaR3rWbIq3AOUJ6J75ChJEnI%2BI5oKf7rLFzsSipCthw%2BNllHffLhom5%2FU6WPwyHXTPbjnfj91sDFpUOAca3GI0JvDMhNyKvY%2BT4ZbPKuaVigAdRfNQO9gbsqbYNEX8io%2BnHKImPiepiPRbjzxS6xJpgZe81ZbyQs5uQ1OKjKN0AmQQC%2B6oThmZSckuHZimsENgEDYAjCmmns3KX0e7%2FhIOT24VOHNmHz8y1oJiw3s0pxNtjX%2FQk4eK1DzQKZebn%2B5qKuXx9gRmjx%2B17KUznGOgQn9vviLUlyVsQXoWmGxDL6sUNXxn%2BVMbmeIuKKwThps6aYY3AAtn7s1CUADP%2BBc2JJI1Rsr2q5AClG5tMgG9fp1qV1wTDtUmLfnpR93gL17fB5HDlonHPdz%2FRklYyhy0rmrMwGVlp2pVMFTzOMjhn9bm3VLYoeUGGUJxrrwxY9MBHL7RSobJpOH3PFSCQPesVAB25H5UqcahdTatfBc10Md8O%2BEbK1RFqC0GZoCBEp9V%2FlbE963XJCkmlIURA5mrny62Xofj9cGjV0GSZOIg68nZUtQAq4AIDI25onS14X9fX8uPSu%2F6qvAQSt%2FWW2vU6bQeWY1E9618%2Fu%2B1NG2JEwSWonQLrfM66BR77l%2B8XvXa%2BasezC%2FpPe8BjqkATKt2uLLp9ZRCEssYW3F5Dhev3Wc%2BLYbaY7gZp14YlaEy%2B0XOSg05Shk%2B4viT2B1X6BYthRMSU3Xy%2B9Nrw2WzBScdwII9VkJ5dSZE5eTW0RZqFINI1evSVE6VSh12TJmDzQSR1rfNQEazJG2t9cnuZZUsUpgl2HVrtcHcEx0rco2F9b6Xy5NKJq5H3ma9iiJ5aV9H15cg9XX9LV%2Fladd77uu9zli&X-Amz-Signature=5619b8bcd354eb8e87815775fe40e90022aee4623888c1adc00963af22b0fc65&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQE2SQTO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDleNRklK9W70yWfGqu%2Bl1IJZwv0OlOLT%2BLK1T8jpFy%2FwIhAN845NJ3SgAsbQzHzB7ZOw%2FpQ7LV5uAb4lRRS%2BU0OYRHKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0fiWu6MxPaR3rWbIq3AOUJ6J75ChJEnI%2BI5oKf7rLFzsSipCthw%2BNllHffLhom5%2FU6WPwyHXTPbjnfj91sDFpUOAca3GI0JvDMhNyKvY%2BT4ZbPKuaVigAdRfNQO9gbsqbYNEX8io%2BnHKImPiepiPRbjzxS6xJpgZe81ZbyQs5uQ1OKjKN0AmQQC%2B6oThmZSckuHZimsENgEDYAjCmmns3KX0e7%2FhIOT24VOHNmHz8y1oJiw3s0pxNtjX%2FQk4eK1DzQKZebn%2B5qKuXx9gRmjx%2B17KUznGOgQn9vviLUlyVsQXoWmGxDL6sUNXxn%2BVMbmeIuKKwThps6aYY3AAtn7s1CUADP%2BBc2JJI1Rsr2q5AClG5tMgG9fp1qV1wTDtUmLfnpR93gL17fB5HDlonHPdz%2FRklYyhy0rmrMwGVlp2pVMFTzOMjhn9bm3VLYoeUGGUJxrrwxY9MBHL7RSobJpOH3PFSCQPesVAB25H5UqcahdTatfBc10Md8O%2BEbK1RFqC0GZoCBEp9V%2FlbE963XJCkmlIURA5mrny62Xofj9cGjV0GSZOIg68nZUtQAq4AIDI25onS14X9fX8uPSu%2F6qvAQSt%2FWW2vU6bQeWY1E9618%2Fu%2B1NG2JEwSWonQLrfM66BR77l%2B8XvXa%2BasezC%2FpPe8BjqkATKt2uLLp9ZRCEssYW3F5Dhev3Wc%2BLYbaY7gZp14YlaEy%2B0XOSg05Shk%2B4viT2B1X6BYthRMSU3Xy%2B9Nrw2WzBScdwII9VkJ5dSZE5eTW0RZqFINI1evSVE6VSh12TJmDzQSR1rfNQEazJG2t9cnuZZUsUpgl2HVrtcHcEx0rco2F9b6Xy5NKJq5H3ma9iiJ5aV9H15cg9XX9LV%2Fladd77uu9zli&X-Amz-Signature=cd7a7bed5c1c3fc37f90e890d1cb9d9e4e4f106f299cef4f19c4bbcb3b7a4d68&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQE2SQTO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDleNRklK9W70yWfGqu%2Bl1IJZwv0OlOLT%2BLK1T8jpFy%2FwIhAN845NJ3SgAsbQzHzB7ZOw%2FpQ7LV5uAb4lRRS%2BU0OYRHKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0fiWu6MxPaR3rWbIq3AOUJ6J75ChJEnI%2BI5oKf7rLFzsSipCthw%2BNllHffLhom5%2FU6WPwyHXTPbjnfj91sDFpUOAca3GI0JvDMhNyKvY%2BT4ZbPKuaVigAdRfNQO9gbsqbYNEX8io%2BnHKImPiepiPRbjzxS6xJpgZe81ZbyQs5uQ1OKjKN0AmQQC%2B6oThmZSckuHZimsENgEDYAjCmmns3KX0e7%2FhIOT24VOHNmHz8y1oJiw3s0pxNtjX%2FQk4eK1DzQKZebn%2B5qKuXx9gRmjx%2B17KUznGOgQn9vviLUlyVsQXoWmGxDL6sUNXxn%2BVMbmeIuKKwThps6aYY3AAtn7s1CUADP%2BBc2JJI1Rsr2q5AClG5tMgG9fp1qV1wTDtUmLfnpR93gL17fB5HDlonHPdz%2FRklYyhy0rmrMwGVlp2pVMFTzOMjhn9bm3VLYoeUGGUJxrrwxY9MBHL7RSobJpOH3PFSCQPesVAB25H5UqcahdTatfBc10Md8O%2BEbK1RFqC0GZoCBEp9V%2FlbE963XJCkmlIURA5mrny62Xofj9cGjV0GSZOIg68nZUtQAq4AIDI25onS14X9fX8uPSu%2F6qvAQSt%2FWW2vU6bQeWY1E9618%2Fu%2B1NG2JEwSWonQLrfM66BR77l%2B8XvXa%2BasezC%2FpPe8BjqkATKt2uLLp9ZRCEssYW3F5Dhev3Wc%2BLYbaY7gZp14YlaEy%2B0XOSg05Shk%2B4viT2B1X6BYthRMSU3Xy%2B9Nrw2WzBScdwII9VkJ5dSZE5eTW0RZqFINI1evSVE6VSh12TJmDzQSR1rfNQEazJG2t9cnuZZUsUpgl2HVrtcHcEx0rco2F9b6Xy5NKJq5H3ma9iiJ5aV9H15cg9XX9LV%2Fladd77uu9zli&X-Amz-Signature=de24b81fd6002af1820da53fd6b16e9a7f189f6bc671268033faa31513264a9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQE2SQTO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDleNRklK9W70yWfGqu%2Bl1IJZwv0OlOLT%2BLK1T8jpFy%2FwIhAN845NJ3SgAsbQzHzB7ZOw%2FpQ7LV5uAb4lRRS%2BU0OYRHKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0fiWu6MxPaR3rWbIq3AOUJ6J75ChJEnI%2BI5oKf7rLFzsSipCthw%2BNllHffLhom5%2FU6WPwyHXTPbjnfj91sDFpUOAca3GI0JvDMhNyKvY%2BT4ZbPKuaVigAdRfNQO9gbsqbYNEX8io%2BnHKImPiepiPRbjzxS6xJpgZe81ZbyQs5uQ1OKjKN0AmQQC%2B6oThmZSckuHZimsENgEDYAjCmmns3KX0e7%2FhIOT24VOHNmHz8y1oJiw3s0pxNtjX%2FQk4eK1DzQKZebn%2B5qKuXx9gRmjx%2B17KUznGOgQn9vviLUlyVsQXoWmGxDL6sUNXxn%2BVMbmeIuKKwThps6aYY3AAtn7s1CUADP%2BBc2JJI1Rsr2q5AClG5tMgG9fp1qV1wTDtUmLfnpR93gL17fB5HDlonHPdz%2FRklYyhy0rmrMwGVlp2pVMFTzOMjhn9bm3VLYoeUGGUJxrrwxY9MBHL7RSobJpOH3PFSCQPesVAB25H5UqcahdTatfBc10Md8O%2BEbK1RFqC0GZoCBEp9V%2FlbE963XJCkmlIURA5mrny62Xofj9cGjV0GSZOIg68nZUtQAq4AIDI25onS14X9fX8uPSu%2F6qvAQSt%2FWW2vU6bQeWY1E9618%2Fu%2B1NG2JEwSWonQLrfM66BR77l%2B8XvXa%2BasezC%2FpPe8BjqkATKt2uLLp9ZRCEssYW3F5Dhev3Wc%2BLYbaY7gZp14YlaEy%2B0XOSg05Shk%2B4viT2B1X6BYthRMSU3Xy%2B9Nrw2WzBScdwII9VkJ5dSZE5eTW0RZqFINI1evSVE6VSh12TJmDzQSR1rfNQEazJG2t9cnuZZUsUpgl2HVrtcHcEx0rco2F9b6Xy5NKJq5H3ma9iiJ5aV9H15cg9XX9LV%2Fladd77uu9zli&X-Amz-Signature=e15b9813a69d6ce40cccac6cae1e76f64c80b21711368a8792fa024da542559e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQE2SQTO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDleNRklK9W70yWfGqu%2Bl1IJZwv0OlOLT%2BLK1T8jpFy%2FwIhAN845NJ3SgAsbQzHzB7ZOw%2FpQ7LV5uAb4lRRS%2BU0OYRHKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0fiWu6MxPaR3rWbIq3AOUJ6J75ChJEnI%2BI5oKf7rLFzsSipCthw%2BNllHffLhom5%2FU6WPwyHXTPbjnfj91sDFpUOAca3GI0JvDMhNyKvY%2BT4ZbPKuaVigAdRfNQO9gbsqbYNEX8io%2BnHKImPiepiPRbjzxS6xJpgZe81ZbyQs5uQ1OKjKN0AmQQC%2B6oThmZSckuHZimsENgEDYAjCmmns3KX0e7%2FhIOT24VOHNmHz8y1oJiw3s0pxNtjX%2FQk4eK1DzQKZebn%2B5qKuXx9gRmjx%2B17KUznGOgQn9vviLUlyVsQXoWmGxDL6sUNXxn%2BVMbmeIuKKwThps6aYY3AAtn7s1CUADP%2BBc2JJI1Rsr2q5AClG5tMgG9fp1qV1wTDtUmLfnpR93gL17fB5HDlonHPdz%2FRklYyhy0rmrMwGVlp2pVMFTzOMjhn9bm3VLYoeUGGUJxrrwxY9MBHL7RSobJpOH3PFSCQPesVAB25H5UqcahdTatfBc10Md8O%2BEbK1RFqC0GZoCBEp9V%2FlbE963XJCkmlIURA5mrny62Xofj9cGjV0GSZOIg68nZUtQAq4AIDI25onS14X9fX8uPSu%2F6qvAQSt%2FWW2vU6bQeWY1E9618%2Fu%2B1NG2JEwSWonQLrfM66BR77l%2B8XvXa%2BasezC%2FpPe8BjqkATKt2uLLp9ZRCEssYW3F5Dhev3Wc%2BLYbaY7gZp14YlaEy%2B0XOSg05Shk%2B4viT2B1X6BYthRMSU3Xy%2B9Nrw2WzBScdwII9VkJ5dSZE5eTW0RZqFINI1evSVE6VSh12TJmDzQSR1rfNQEazJG2t9cnuZZUsUpgl2HVrtcHcEx0rco2F9b6Xy5NKJq5H3ma9iiJ5aV9H15cg9XX9LV%2Fladd77uu9zli&X-Amz-Signature=2214f9fd7e292141335a147e9fca9ac91d475680d360920c27e0b43ae8561b47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDNJD3SE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDKSSDnsEUlHp8xK%2FN225BwtEJxf0K4cEXAnJOKShczhAiEA8S32TZP0iWxne%2F85DixYIdSQa7k3IMpSm9p%2BydaaW6MqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBfJ7ygcV5sPRvUhFCrcA8tbdE5XAZxDoBp5%2BPD422ZGjl34A82%2F83nTssbyixR4jJ9ign5QZkSWA66dwbDvpKh6%2FaI4BppfrKBlwlY8Ez3aQV2RADUNG3ezd7gns7h%2FQjE%2BdPQAXaa2gtvTLJA8ngtwCuvXJvl1pVsCQJwUjV6fqqnj0FOT7uqW4SFCoGM491Ts4wI2YSbiJ9sxF3FfdF%2B2j6OZx2AkKArV9qLO0v0JZayhparSJZCOeuPtrex5N7Fa81shsIs0Y%2BZgYe7hO7hBRGaPEHxuriWSQEjz%2FjhI4dGdRzLDDy3TUwMA0FG4f307%2FnAPDCVe%2FaMKOn%2BWFeJLdjx7eqJNVSNV6qdJsyXh0MFfSoMmOge8Yiqxywfv0afiqRuI%2F7kpst5iyzh0Fp4XLpIewuvfOWANIwnZgyhUrU%2FqGunDrcbJ%2B3YiZspQCt8V47BrS%2BKU6GzQAWAqG1jeBD2D6w5Xzwj%2Flkx7TsItCQeamgps2Ro0G1UYfKq7nsGlqQbhdOkWxnPKWBdA52yq8DIq3ZlTdUkzFF3pqRZA0VeJqY1oOUaO4Psl1Aq5DOzxOR1ZyIM8KAhLhHwkyqPzcdcwP2tOkmjFFoZh6UdSQ%2F%2FvkQRc8lMwjQPVjsw9kOqh110xx25pDM7VML%2Bk97wGOqUBuGby%2FFl3Fgd%2B6fJwQiVtlcMBmhxi%2BwxkQ4LrMpv9HAD6oPRAt15UtMCvapJXQq3kDIjuBE1kVOACHp9yCxy6uxbh3xonY4sZP9qeCorVBzN1bIX0T%2F553h8XP%2B6rTJ7bfC6yLo4SFRlvRWopvPx89vrsYOuHnqnz2PBFF3Sfn8Lt0sxFBhLin%2BDcGo5XK8c%2FRhVyVszRVLJfHza049gaBtReb0qq&X-Amz-Signature=e468795310345cdb0cff16f515002721ca974b46cf298982bb6f117b8eb2fb51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNVS2D6D%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2B0MuF%2FBVE2PQBshUhqatBlI0kYrmfO%2BeO%2Fy4TCf9r3gIhANQsYlxgMLfmbS3e3APw0gNzTGlN%2FtAjEGLVbPX6pQxHKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZkWDADArsaMBEsBIq3APx%2F10tOlRojC6SZfCFQbnEzdegF7DxNYN9SjMLbWbquwNaUw1H0eLXw1aGF923vAyOFhYHX8Os1n0gUlcP32UEJv%2Fg0u62xfCDjaIsWMbelFgTCNd%2B0dcZyXUxVGI52gaGTPE%2BNI%2FHnDA1RU%2BnUvRYMK1%2BCOIOzixDMzEOcAeFl50MkSRh6opQuDiGdGxbe%2Fw09uaqxvynPucITIc%2BUkDDgo%2BcTOD8%2FMhXNOEaL3Xgy8KY6BvL3wQuIoHU%2FR9FEfwlwdM77EkUM9v0qir9CmopnPhBqJqS4Qz%2BkuWd%2FGKUA1OfhC4O1i6mbNiKVr2dWCFI2gseYGa2ZZMavn5TkRSAVdt%2BJdjTDySk7h0BRa5RGsH3JTWCkLgAztVQ%2F70%2BvIRukf4VSgSSZy14P%2BSiFKnCWq%2Fb7y8YBVSzG%2BpQq4DySJgRAKcfpwPtzoRoSrZyo8Hp%2BJLH6Qb5KTlzCXdOy%2FxF4hv4tC0bW3ZfkPTi1YeYcKPK4mzWSz%2FD2s%2BDFh9VPvGCdRF0%2BwNZFZ8GEKWhrbIDsrwZUNrCIeoTa0GCvsxNoSHduLtOzU8cRu9C%2FwW%2F415LZu0Ej8bNFkIRtHcrlrTKhXPT1BtXQaY0ZrxDS4cIr6YGXZf%2BxNtQOtdrPTCbpfe8BjqkAeMtBJAkwfMsyhMew6hCJw6L9H5OBe1ZgAeKh49uBae1aQWBV%2B22VPQ3%2Fl%2Fb4ShqAEmhlWOBBrf%2FG5pxL5a0c0fCAZaZgwxdZcn%2B10AB7dtnwkISfsvPupmNYp%2B5ur2GgcXuWU9HWBTm3m628q5U%2FXSCLzEydrxRXvRLi3qAwgz0k8WosmJfLebLl60jycBZzEY57sQwOdLvM%2BJYfw%2FPO6oJ%2F2ed&X-Amz-Signature=e7ed02bda44c19a1b908287eaf200dcce7fdfaa71e2573a3b996bdf09d5e39c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKH2TFZW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4R14Ns6ZxJ%2FrRQw%2FkNxROzcohTArYXQDmfJFpHhx9XQIgYouZOnLLcVce%2BUhKUEAdx%2BfxX9VTHRYQRuRXZ3FibvkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF79xH5bLAWympNHeSrcA8oNqMNeRLNvnHB%2BRiSYyIHYt5FmHhpo9tHQPBG%2BenFjQPC8mRrOdVbL7qCuJ%2FZJ6VOihoX6oD6o0bKY0vDtOWXa8pGUtzR3n%2Ffl%2BV6L%2B0p1dgBTWhF%2FTccBbXqKgcGtXZ0MrDMbtS9wSTxpymEh32NeAQI9n%2FXeMbsq4UiO6btRxCNlUqCmV4mtpA%2BOvFooO32nSpCvt71oYcOSwfhCxPe2zXwFzpfMOEyRtubRMPbrTsyk%2FxWBj4Gfaj6Z1G4ckjI6f0WVZ2rUztRLXf9QMRtujzgoDBDUGaP0b9rjO9sF8RE%2BXwitQHfC3Q06eJWe2fSY%2BPvdkyaRUwYyx12aYD5pVvSCEAGdBOavGTm%2FN8VdErZGry15ODDFFsRKX1sFHE9azaR7tMWnrx4llwwUCkqT4Mb0ckTNeTzfAXvmuObwqSvx26h2MZk7%2FBWHp8BS%2B9qMjs7XSqgbLVsmuJqZjmdtYBzkwvxHVYPOfNJzQUQHtNnCJG9i9fFZlH7aIiFwKCjXVn31F3U8u4JAqDjdaC5Ji%2B%2BA3onMJGgOfgVKYRdphfc0kXDz3GDwpozZ2QyigboiNa1YC2f7EuOYT3ZpcgtmJV9MDJUc5oAWRt1tD%2Bo5RiS%2FA0OeNpsS%2FSr4MKyk97wGOqUBJgrbzeh00h%2BZuZUy%2Fe9vx6qafXqKnOHgBd1Ly9WlhsuebfxLwbehm1y%2F01FXeu74iZhMWsRq28bZnC53pJacya6%2BITg9KRUt%2B1ya0PN5EY276ZqvLtYuWWqoOYGZUyY7jdJw5ImNLVLPrJY%2FSUd2A2LwEZvbJY38ln%2BhWdcPuyShkI9UmeFg54qn4UZrC2SrRMXI7KoZZSxv%2FuCNp4tyDF8WQiAp&X-Amz-Signature=33cea8d91ce55c62ff62f07cfc897eb00f1c323f70fb8f7c10f65363c3d6bfb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKH2TFZW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4R14Ns6ZxJ%2FrRQw%2FkNxROzcohTArYXQDmfJFpHhx9XQIgYouZOnLLcVce%2BUhKUEAdx%2BfxX9VTHRYQRuRXZ3FibvkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF79xH5bLAWympNHeSrcA8oNqMNeRLNvnHB%2BRiSYyIHYt5FmHhpo9tHQPBG%2BenFjQPC8mRrOdVbL7qCuJ%2FZJ6VOihoX6oD6o0bKY0vDtOWXa8pGUtzR3n%2Ffl%2BV6L%2B0p1dgBTWhF%2FTccBbXqKgcGtXZ0MrDMbtS9wSTxpymEh32NeAQI9n%2FXeMbsq4UiO6btRxCNlUqCmV4mtpA%2BOvFooO32nSpCvt71oYcOSwfhCxPe2zXwFzpfMOEyRtubRMPbrTsyk%2FxWBj4Gfaj6Z1G4ckjI6f0WVZ2rUztRLXf9QMRtujzgoDBDUGaP0b9rjO9sF8RE%2BXwitQHfC3Q06eJWe2fSY%2BPvdkyaRUwYyx12aYD5pVvSCEAGdBOavGTm%2FN8VdErZGry15ODDFFsRKX1sFHE9azaR7tMWnrx4llwwUCkqT4Mb0ckTNeTzfAXvmuObwqSvx26h2MZk7%2FBWHp8BS%2B9qMjs7XSqgbLVsmuJqZjmdtYBzkwvxHVYPOfNJzQUQHtNnCJG9i9fFZlH7aIiFwKCjXVn31F3U8u4JAqDjdaC5Ji%2B%2BA3onMJGgOfgVKYRdphfc0kXDz3GDwpozZ2QyigboiNa1YC2f7EuOYT3ZpcgtmJV9MDJUc5oAWRt1tD%2Bo5RiS%2FA0OeNpsS%2FSr4MKyk97wGOqUBJgrbzeh00h%2BZuZUy%2Fe9vx6qafXqKnOHgBd1Ly9WlhsuebfxLwbehm1y%2F01FXeu74iZhMWsRq28bZnC53pJacya6%2BITg9KRUt%2B1ya0PN5EY276ZqvLtYuWWqoOYGZUyY7jdJw5ImNLVLPrJY%2FSUd2A2LwEZvbJY38ln%2BhWdcPuyShkI9UmeFg54qn4UZrC2SrRMXI7KoZZSxv%2FuCNp4tyDF8WQiAp&X-Amz-Signature=a33ce4541f3c241decda51a0f7d8257ee7483d11d2b615893b1e76792862a45f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
