

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA5UG3OR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGh7ZH%2Bh3qA3rTi1JFaKQsUWwAuRTbjVzqJne7NK0uPfAiEAxMbV0FXhXQ2iKjOp2ce%2Boh3yup0dr7%2BJGYYUHSl5kQMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLxIT643rzMiaPbhCrcA4k7qnvLcspKys4lAcS%2B2uSroDgLiBv0FL4zrZKNEx%2BgZd1tdpQ7wxlP5Pwms1bQr0B%2F1Dbjh4000tRioIxk%2FabG1LYuQubiP%2FnJQukAJJvyTGhHLLkyZofeNO1l68LQL2pMIT5cluMEdBFClzmnQc%2FpVLvOqmwHD72C2jWfUz0gGfITIdHywTYww7P92cwJqN5hggSbwOuTbd4%2BPs1kQjfCE7Txyg6kF6FJkdg2LnsaJeowJRw6KF61axUwzQI45zwET0L9dQPqP2fg%2FXb6i2LRbqRJ4%2FT9GDrhE%2FF%2FHsxfPul4ROrsR5ByEggzm4b8JDZEmn4zB4TYiIgDBT9zFgpXhhu7kd00tIYq34G4igVqe3s8saSXaaVJQ31oX9%2F1E1JkBW4KvKcvon0lN40TW2tCeotb1fggp2vkTn0Vpmor8W4K8Z57LFgDQkPT86TA2PlGFu2iCR%2F1x0hMY6v2oB%2F57VdbYQhO5PuRaOnQoZ5zRuyBClmto0XBKeLP0tzk%2BpAsYswrUYGG5ZvTFWXbSkSeLxa1l7wUdSiKVeDS3MUd22yu%2FXKF7tAGEFvnl3nGKdaBvdHanDtSfrK75eN48iNdPTKcAAjEc4P43HTnAtOZWqDKBms9qHsMBS2SMM%2FB%2FbwGOqUBSlVHi%2B3lJFyEvyo14bvig8lYmLkJrpUGYv0xlKfK049zPrYj8cqNMzGxUs8sePPKEiJTFf54dnP4xY8hWSVPNgSk6R2xasIo5TwUin%2FkF2hQCsfCRhsl%2FkYe8sT2InoM%2FpRmA%2FH6pvODimLW3ofWBUHwyhVyyTem1csqCr8thfJX8CGgCEC%2F%2FzCJOYVwv0DKORAhXpZ0DRzBXSQSBl%2F4NXFtyWu6&X-Amz-Signature=2cabfd7d713863fd3bb79d2e210aa14aaa59318e527074cfd9e2caa6a651d846&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA5UG3OR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGh7ZH%2Bh3qA3rTi1JFaKQsUWwAuRTbjVzqJne7NK0uPfAiEAxMbV0FXhXQ2iKjOp2ce%2Boh3yup0dr7%2BJGYYUHSl5kQMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLxIT643rzMiaPbhCrcA4k7qnvLcspKys4lAcS%2B2uSroDgLiBv0FL4zrZKNEx%2BgZd1tdpQ7wxlP5Pwms1bQr0B%2F1Dbjh4000tRioIxk%2FabG1LYuQubiP%2FnJQukAJJvyTGhHLLkyZofeNO1l68LQL2pMIT5cluMEdBFClzmnQc%2FpVLvOqmwHD72C2jWfUz0gGfITIdHywTYww7P92cwJqN5hggSbwOuTbd4%2BPs1kQjfCE7Txyg6kF6FJkdg2LnsaJeowJRw6KF61axUwzQI45zwET0L9dQPqP2fg%2FXb6i2LRbqRJ4%2FT9GDrhE%2FF%2FHsxfPul4ROrsR5ByEggzm4b8JDZEmn4zB4TYiIgDBT9zFgpXhhu7kd00tIYq34G4igVqe3s8saSXaaVJQ31oX9%2F1E1JkBW4KvKcvon0lN40TW2tCeotb1fggp2vkTn0Vpmor8W4K8Z57LFgDQkPT86TA2PlGFu2iCR%2F1x0hMY6v2oB%2F57VdbYQhO5PuRaOnQoZ5zRuyBClmto0XBKeLP0tzk%2BpAsYswrUYGG5ZvTFWXbSkSeLxa1l7wUdSiKVeDS3MUd22yu%2FXKF7tAGEFvnl3nGKdaBvdHanDtSfrK75eN48iNdPTKcAAjEc4P43HTnAtOZWqDKBms9qHsMBS2SMM%2FB%2FbwGOqUBSlVHi%2B3lJFyEvyo14bvig8lYmLkJrpUGYv0xlKfK049zPrYj8cqNMzGxUs8sePPKEiJTFf54dnP4xY8hWSVPNgSk6R2xasIo5TwUin%2FkF2hQCsfCRhsl%2FkYe8sT2InoM%2FpRmA%2FH6pvODimLW3ofWBUHwyhVyyTem1csqCr8thfJX8CGgCEC%2F%2FzCJOYVwv0DKORAhXpZ0DRzBXSQSBl%2F4NXFtyWu6&X-Amz-Signature=ce81568d4736c42d6efe88efd2010d79fc3ea0f6644447560bf68156445cc97d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA5UG3OR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGh7ZH%2Bh3qA3rTi1JFaKQsUWwAuRTbjVzqJne7NK0uPfAiEAxMbV0FXhXQ2iKjOp2ce%2Boh3yup0dr7%2BJGYYUHSl5kQMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLxIT643rzMiaPbhCrcA4k7qnvLcspKys4lAcS%2B2uSroDgLiBv0FL4zrZKNEx%2BgZd1tdpQ7wxlP5Pwms1bQr0B%2F1Dbjh4000tRioIxk%2FabG1LYuQubiP%2FnJQukAJJvyTGhHLLkyZofeNO1l68LQL2pMIT5cluMEdBFClzmnQc%2FpVLvOqmwHD72C2jWfUz0gGfITIdHywTYww7P92cwJqN5hggSbwOuTbd4%2BPs1kQjfCE7Txyg6kF6FJkdg2LnsaJeowJRw6KF61axUwzQI45zwET0L9dQPqP2fg%2FXb6i2LRbqRJ4%2FT9GDrhE%2FF%2FHsxfPul4ROrsR5ByEggzm4b8JDZEmn4zB4TYiIgDBT9zFgpXhhu7kd00tIYq34G4igVqe3s8saSXaaVJQ31oX9%2F1E1JkBW4KvKcvon0lN40TW2tCeotb1fggp2vkTn0Vpmor8W4K8Z57LFgDQkPT86TA2PlGFu2iCR%2F1x0hMY6v2oB%2F57VdbYQhO5PuRaOnQoZ5zRuyBClmto0XBKeLP0tzk%2BpAsYswrUYGG5ZvTFWXbSkSeLxa1l7wUdSiKVeDS3MUd22yu%2FXKF7tAGEFvnl3nGKdaBvdHanDtSfrK75eN48iNdPTKcAAjEc4P43HTnAtOZWqDKBms9qHsMBS2SMM%2FB%2FbwGOqUBSlVHi%2B3lJFyEvyo14bvig8lYmLkJrpUGYv0xlKfK049zPrYj8cqNMzGxUs8sePPKEiJTFf54dnP4xY8hWSVPNgSk6R2xasIo5TwUin%2FkF2hQCsfCRhsl%2FkYe8sT2InoM%2FpRmA%2FH6pvODimLW3ofWBUHwyhVyyTem1csqCr8thfJX8CGgCEC%2F%2FzCJOYVwv0DKORAhXpZ0DRzBXSQSBl%2F4NXFtyWu6&X-Amz-Signature=544d77ef784d83701d0863b6f7dee862bee2553d226083725f76eaebf00f091f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA5UG3OR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGh7ZH%2Bh3qA3rTi1JFaKQsUWwAuRTbjVzqJne7NK0uPfAiEAxMbV0FXhXQ2iKjOp2ce%2Boh3yup0dr7%2BJGYYUHSl5kQMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLxIT643rzMiaPbhCrcA4k7qnvLcspKys4lAcS%2B2uSroDgLiBv0FL4zrZKNEx%2BgZd1tdpQ7wxlP5Pwms1bQr0B%2F1Dbjh4000tRioIxk%2FabG1LYuQubiP%2FnJQukAJJvyTGhHLLkyZofeNO1l68LQL2pMIT5cluMEdBFClzmnQc%2FpVLvOqmwHD72C2jWfUz0gGfITIdHywTYww7P92cwJqN5hggSbwOuTbd4%2BPs1kQjfCE7Txyg6kF6FJkdg2LnsaJeowJRw6KF61axUwzQI45zwET0L9dQPqP2fg%2FXb6i2LRbqRJ4%2FT9GDrhE%2FF%2FHsxfPul4ROrsR5ByEggzm4b8JDZEmn4zB4TYiIgDBT9zFgpXhhu7kd00tIYq34G4igVqe3s8saSXaaVJQ31oX9%2F1E1JkBW4KvKcvon0lN40TW2tCeotb1fggp2vkTn0Vpmor8W4K8Z57LFgDQkPT86TA2PlGFu2iCR%2F1x0hMY6v2oB%2F57VdbYQhO5PuRaOnQoZ5zRuyBClmto0XBKeLP0tzk%2BpAsYswrUYGG5ZvTFWXbSkSeLxa1l7wUdSiKVeDS3MUd22yu%2FXKF7tAGEFvnl3nGKdaBvdHanDtSfrK75eN48iNdPTKcAAjEc4P43HTnAtOZWqDKBms9qHsMBS2SMM%2FB%2FbwGOqUBSlVHi%2B3lJFyEvyo14bvig8lYmLkJrpUGYv0xlKfK049zPrYj8cqNMzGxUs8sePPKEiJTFf54dnP4xY8hWSVPNgSk6R2xasIo5TwUin%2FkF2hQCsfCRhsl%2FkYe8sT2InoM%2FpRmA%2FH6pvODimLW3ofWBUHwyhVyyTem1csqCr8thfJX8CGgCEC%2F%2FzCJOYVwv0DKORAhXpZ0DRzBXSQSBl%2F4NXFtyWu6&X-Amz-Signature=6acc1745f344fcea0600914210a6f9c860965c207be16d4a22b9fa9c279e1201&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA5UG3OR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGh7ZH%2Bh3qA3rTi1JFaKQsUWwAuRTbjVzqJne7NK0uPfAiEAxMbV0FXhXQ2iKjOp2ce%2Boh3yup0dr7%2BJGYYUHSl5kQMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLxIT643rzMiaPbhCrcA4k7qnvLcspKys4lAcS%2B2uSroDgLiBv0FL4zrZKNEx%2BgZd1tdpQ7wxlP5Pwms1bQr0B%2F1Dbjh4000tRioIxk%2FabG1LYuQubiP%2FnJQukAJJvyTGhHLLkyZofeNO1l68LQL2pMIT5cluMEdBFClzmnQc%2FpVLvOqmwHD72C2jWfUz0gGfITIdHywTYww7P92cwJqN5hggSbwOuTbd4%2BPs1kQjfCE7Txyg6kF6FJkdg2LnsaJeowJRw6KF61axUwzQI45zwET0L9dQPqP2fg%2FXb6i2LRbqRJ4%2FT9GDrhE%2FF%2FHsxfPul4ROrsR5ByEggzm4b8JDZEmn4zB4TYiIgDBT9zFgpXhhu7kd00tIYq34G4igVqe3s8saSXaaVJQ31oX9%2F1E1JkBW4KvKcvon0lN40TW2tCeotb1fggp2vkTn0Vpmor8W4K8Z57LFgDQkPT86TA2PlGFu2iCR%2F1x0hMY6v2oB%2F57VdbYQhO5PuRaOnQoZ5zRuyBClmto0XBKeLP0tzk%2BpAsYswrUYGG5ZvTFWXbSkSeLxa1l7wUdSiKVeDS3MUd22yu%2FXKF7tAGEFvnl3nGKdaBvdHanDtSfrK75eN48iNdPTKcAAjEc4P43HTnAtOZWqDKBms9qHsMBS2SMM%2FB%2FbwGOqUBSlVHi%2B3lJFyEvyo14bvig8lYmLkJrpUGYv0xlKfK049zPrYj8cqNMzGxUs8sePPKEiJTFf54dnP4xY8hWSVPNgSk6R2xasIo5TwUin%2FkF2hQCsfCRhsl%2FkYe8sT2InoM%2FpRmA%2FH6pvODimLW3ofWBUHwyhVyyTem1csqCr8thfJX8CGgCEC%2F%2FzCJOYVwv0DKORAhXpZ0DRzBXSQSBl%2F4NXFtyWu6&X-Amz-Signature=572c091ef7ce80bf6dfdad6c12eb4a219d38e0771c82f22ff563b9e13607686c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA5UG3OR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGh7ZH%2Bh3qA3rTi1JFaKQsUWwAuRTbjVzqJne7NK0uPfAiEAxMbV0FXhXQ2iKjOp2ce%2Boh3yup0dr7%2BJGYYUHSl5kQMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLxIT643rzMiaPbhCrcA4k7qnvLcspKys4lAcS%2B2uSroDgLiBv0FL4zrZKNEx%2BgZd1tdpQ7wxlP5Pwms1bQr0B%2F1Dbjh4000tRioIxk%2FabG1LYuQubiP%2FnJQukAJJvyTGhHLLkyZofeNO1l68LQL2pMIT5cluMEdBFClzmnQc%2FpVLvOqmwHD72C2jWfUz0gGfITIdHywTYww7P92cwJqN5hggSbwOuTbd4%2BPs1kQjfCE7Txyg6kF6FJkdg2LnsaJeowJRw6KF61axUwzQI45zwET0L9dQPqP2fg%2FXb6i2LRbqRJ4%2FT9GDrhE%2FF%2FHsxfPul4ROrsR5ByEggzm4b8JDZEmn4zB4TYiIgDBT9zFgpXhhu7kd00tIYq34G4igVqe3s8saSXaaVJQ31oX9%2F1E1JkBW4KvKcvon0lN40TW2tCeotb1fggp2vkTn0Vpmor8W4K8Z57LFgDQkPT86TA2PlGFu2iCR%2F1x0hMY6v2oB%2F57VdbYQhO5PuRaOnQoZ5zRuyBClmto0XBKeLP0tzk%2BpAsYswrUYGG5ZvTFWXbSkSeLxa1l7wUdSiKVeDS3MUd22yu%2FXKF7tAGEFvnl3nGKdaBvdHanDtSfrK75eN48iNdPTKcAAjEc4P43HTnAtOZWqDKBms9qHsMBS2SMM%2FB%2FbwGOqUBSlVHi%2B3lJFyEvyo14bvig8lYmLkJrpUGYv0xlKfK049zPrYj8cqNMzGxUs8sePPKEiJTFf54dnP4xY8hWSVPNgSk6R2xasIo5TwUin%2FkF2hQCsfCRhsl%2FkYe8sT2InoM%2FpRmA%2FH6pvODimLW3ofWBUHwyhVyyTem1csqCr8thfJX8CGgCEC%2F%2FzCJOYVwv0DKORAhXpZ0DRzBXSQSBl%2F4NXFtyWu6&X-Amz-Signature=7137c934e4c945f0d4e1a7afdc837833da1b686522cdca4d5e907ccce5bdf0e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA5UG3OR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGh7ZH%2Bh3qA3rTi1JFaKQsUWwAuRTbjVzqJne7NK0uPfAiEAxMbV0FXhXQ2iKjOp2ce%2Boh3yup0dr7%2BJGYYUHSl5kQMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLxIT643rzMiaPbhCrcA4k7qnvLcspKys4lAcS%2B2uSroDgLiBv0FL4zrZKNEx%2BgZd1tdpQ7wxlP5Pwms1bQr0B%2F1Dbjh4000tRioIxk%2FabG1LYuQubiP%2FnJQukAJJvyTGhHLLkyZofeNO1l68LQL2pMIT5cluMEdBFClzmnQc%2FpVLvOqmwHD72C2jWfUz0gGfITIdHywTYww7P92cwJqN5hggSbwOuTbd4%2BPs1kQjfCE7Txyg6kF6FJkdg2LnsaJeowJRw6KF61axUwzQI45zwET0L9dQPqP2fg%2FXb6i2LRbqRJ4%2FT9GDrhE%2FF%2FHsxfPul4ROrsR5ByEggzm4b8JDZEmn4zB4TYiIgDBT9zFgpXhhu7kd00tIYq34G4igVqe3s8saSXaaVJQ31oX9%2F1E1JkBW4KvKcvon0lN40TW2tCeotb1fggp2vkTn0Vpmor8W4K8Z57LFgDQkPT86TA2PlGFu2iCR%2F1x0hMY6v2oB%2F57VdbYQhO5PuRaOnQoZ5zRuyBClmto0XBKeLP0tzk%2BpAsYswrUYGG5ZvTFWXbSkSeLxa1l7wUdSiKVeDS3MUd22yu%2FXKF7tAGEFvnl3nGKdaBvdHanDtSfrK75eN48iNdPTKcAAjEc4P43HTnAtOZWqDKBms9qHsMBS2SMM%2FB%2FbwGOqUBSlVHi%2B3lJFyEvyo14bvig8lYmLkJrpUGYv0xlKfK049zPrYj8cqNMzGxUs8sePPKEiJTFf54dnP4xY8hWSVPNgSk6R2xasIo5TwUin%2FkF2hQCsfCRhsl%2FkYe8sT2InoM%2FpRmA%2FH6pvODimLW3ofWBUHwyhVyyTem1csqCr8thfJX8CGgCEC%2F%2FzCJOYVwv0DKORAhXpZ0DRzBXSQSBl%2F4NXFtyWu6&X-Amz-Signature=13cc6d8460a0237e7d69f453bc726d533afa6ce440dec3d52c6685dd3d758b4c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YA5UG3OR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGh7ZH%2Bh3qA3rTi1JFaKQsUWwAuRTbjVzqJne7NK0uPfAiEAxMbV0FXhXQ2iKjOp2ce%2Boh3yup0dr7%2BJGYYUHSl5kQMqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLxIT643rzMiaPbhCrcA4k7qnvLcspKys4lAcS%2B2uSroDgLiBv0FL4zrZKNEx%2BgZd1tdpQ7wxlP5Pwms1bQr0B%2F1Dbjh4000tRioIxk%2FabG1LYuQubiP%2FnJQukAJJvyTGhHLLkyZofeNO1l68LQL2pMIT5cluMEdBFClzmnQc%2FpVLvOqmwHD72C2jWfUz0gGfITIdHywTYww7P92cwJqN5hggSbwOuTbd4%2BPs1kQjfCE7Txyg6kF6FJkdg2LnsaJeowJRw6KF61axUwzQI45zwET0L9dQPqP2fg%2FXb6i2LRbqRJ4%2FT9GDrhE%2FF%2FHsxfPul4ROrsR5ByEggzm4b8JDZEmn4zB4TYiIgDBT9zFgpXhhu7kd00tIYq34G4igVqe3s8saSXaaVJQ31oX9%2F1E1JkBW4KvKcvon0lN40TW2tCeotb1fggp2vkTn0Vpmor8W4K8Z57LFgDQkPT86TA2PlGFu2iCR%2F1x0hMY6v2oB%2F57VdbYQhO5PuRaOnQoZ5zRuyBClmto0XBKeLP0tzk%2BpAsYswrUYGG5ZvTFWXbSkSeLxa1l7wUdSiKVeDS3MUd22yu%2FXKF7tAGEFvnl3nGKdaBvdHanDtSfrK75eN48iNdPTKcAAjEc4P43HTnAtOZWqDKBms9qHsMBS2SMM%2FB%2FbwGOqUBSlVHi%2B3lJFyEvyo14bvig8lYmLkJrpUGYv0xlKfK049zPrYj8cqNMzGxUs8sePPKEiJTFf54dnP4xY8hWSVPNgSk6R2xasIo5TwUin%2FkF2hQCsfCRhsl%2FkYe8sT2InoM%2FpRmA%2FH6pvODimLW3ofWBUHwyhVyyTem1csqCr8thfJX8CGgCEC%2F%2FzCJOYVwv0DKORAhXpZ0DRzBXSQSBl%2F4NXFtyWu6&X-Amz-Signature=d5bc4206623bf82173ad51426fc067169a62ddea1dbaa7ee5b25986644cb0a12&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSS3K6AH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqLuaH6PS8cV0N9RLYhMPSo6xNTzM4yfEnMPReA3L9agIhAPJs3tf4msnZNRKpORYofWWvQ4v%2FT0INPeJntJ6NEHWtKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FYvrJwlDcV2sK%2BZgq3ANaBVGoKCx7qAwsm4pHLdBSMsnkbgca%2B8yesTpBIe9Xc0PXO1WFsqY%2FNRidbBpZ5%2B8juTP%2BT7GuuZO25mtmwpzMNyikkH%2FEwsKv0kv0DJe7N8ML0OJEucvFhICuKQqP7c%2BYHlOyMSKWIEM0Tt1edNKVlPIWnJnfIN7%2F5gbRC1E0mCvvbD%2B%2BX6jynIPPFo3KKUT6s4nMOvCU%2FO0nvL9Tqd44s%2FQ7k2mkUui%2BdjqJzyFwN5yYF8mLoN2LzZrr6Vu4cBlqN%2FyxqKLDRWhWk85EikjMXH9U8MrZKzh0lnOItqZMXCYGkLK4zCvqMVKJ%2BTjXFxp1aTJslLyyZGBSk6RKYeVYnL0LtlM%2BOqqTBMgnykR1mRAmWuPklezLviMS6mF9AddtT02WEKwf70ZcAu%2FpDCY1WrOhxFDxxgM8hTnK2xFMHMpF3GL2yGMwmhhuIqp0UDCMNGNxbOjSWl%2FVckIarqOfqYzj8MIbTcybxYG%2BLLKQY99WP0NNM1GHXq6Fc%2BfpUgl51Vkv67gkPg8Lh4YDw0gWM1UtRqsFuo2AAVBVN6nHW9hvcOOJeSeaIJhq01RLxfNytN1P7tcutyvdw4NVBmeVp0%2FxHCmsWmc5tGjA03EjtP0mrFeS%2BXSFewmz5jCFuv28BjqkAV4Vv7nnvFN7egW3YcmvCoJ3ncrIe1cnl2GjApgAFHAj5jtse89eSLOsoqdDXZuC7kCqEQJ3zqlDmw9YF7l4JoNFWOtP3Tww0Cbe5xyocvXySYa2DtDFqaSXZWvG5dNfXNNuygv74v3qg8oOJBbUhcJ1efteNvgpP5%2BeJdTNDOx%2FlzkN50%2FzWcjmHJuYTnvFik5E%2BeQ0Oqco22JY26DH7K2VOKvb&X-Amz-Signature=716fcf34a27d1151797cd04d1c29134dd6d9e1db16ca8f57b18cd38761a35fb5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HXXVJXL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE6hAb8CpuGTOUDFOjiOn4x3SG%2BPUPSMqMYinvklyS7MAiBnEeW49MIpGstXqUH0IT6LWRWuEAjRsWXGIttdky%2FS7CqIBAjq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKrIQkCHUZhybN1LjKtwDjAwDfOWV4%2FHXitB6rvLwS1m1PDRM1fCKTO5lJkqdP%2BUVHWwtLR%2BWJyrHIiPCDkYjGeqZvnnEXpHe%2BpxbVmmf7hvEFTUv8vMoKjmB7Fa4AafTiWSkJccwV2PJO7NE2cRn%2Fr3dGNMnDAp7Re%2BdnyYcIfHzXYHKJPUjDCgWwajp4ww44vIzfizkujyK%2Bn3zSxR92BB4Cl12WhDYEiK2yqDyO9VlENOzxe3h51FGrQ5fDHnEamIzYfl0uy43O1mfD%2FTvbLYWxhUEfPop7fW8rueQBl6SolH9VgHkEaBuA4g1aVL0RSjgBIjCML0qyUo5o2kju%2B2u96uLpHRKcGppCqny6vpKK0KZa7q2zR53Z6jIW8QRbTeF6VOiDPBYIVbWYU1HHKvwProgmchplvvBJbVRiqz1zIaRq2M6HmENItCPp%2Bw47HVwDvi0kDRtxzqkn4A4%2BIp2k8Fs8EPNQeU8jWMjQMxG%2BTW%2BX66nfPP7BZ3fpWM4WVygP%2BFSTjm7%2FI939SlhzpqYCOZlSHIUfYWEkrOMwrCFnH03GaHHslcbqJUsvdKfOpmyauIqQaQLgKtPrmXSg5i3xeoAt7kkOEVrXyoWN%2FqLAqEYKunG2C%2BvqKF68Z9477D%2Fbmfp%2BQBMwdMw2O78vAY6pgEUsPX0K5eQB%2FmSS0qZw8SdShU8kH%2BA%2FvHCB8cKOiK0JTXYhgHzIkZEGZDQzUyk%2BdkHUCVPsBKFAfVWGQL3y3sNLPkaGXOZlgQutiYn7Z47Ho%2Fvd82P5vjJB%2B0qO9z4yZoWt%2B4XIalXIKngDr4jNgMtQUCVCA7QMyG5eZRkcfVVG59ia%2FiPp0EC4gVQB1TTu4yLqhYBOy%2F36CTdYshkB%2Fo2B8bmF2t2&X-Amz-Signature=3f76588829ca36c7e9c8e395563b2e66cd936b0e4af1cdfe637c7226e825d8d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5224KGZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID20DSmqAxnEK2r3Twh804jkdwTpHrCoyvLBuhbyrAJNAiEA2Qa9yASSYt2Fx9bVCmaTOZERhv9TXC72CTGzmZZm2KgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHTx%2FhTsA5nsh71xVSrcA9%2B2mLo1zGh3wvk8qv2v6PUGR66Zrap6otkNW2b5tJzMgaMHrw4iu2w6oL4EUp8EIr16imTVKxfrhX4V6dclurHqriNbGMaOO%2BQ2UDS64PRreff8EWR3nYq8oIEHIoMwKZNQXtmQCf13JREjVcyqRHzRvR66AJfbf9AmnDgYMjjwL0buN8noGUsyxJpSN3WKo8UONwESUAxIYxEpjGE%2BCyWgW5nXaoctSiOz3k%2BOj%2BBaOd2PSdhvwksOnuSFnj5v83qBBC%2Bn6VGVZPhSy6f7rNHy1AmHH%2FoveYr7hdHmTvRXDuZOwfFC1YqaQrT4EES%2FMHBRtRQxlS42YOnkqzE%2B%2BLKdcwCqGPPqodv%2BHd36vFOLhisgpJ1pPTY8BBcDPc8SGcx8%2BrUawITHj6ToQRVUKRH15g6Xg%2Bp8XAU4tHMAjs5Y7PWbHAXIJxQ3VIzFlGrk8xCl8qiwCHVq4pUmjCTpTouWNDJkfWJ9FYKYDfTE3a1ZYkeI8xA9Ueb9Rqf%2BOCoczoeSHIRSZQ1JciLJigwd8Kcizs7xtO5qh2Teggzfy3sfd0TtBpjHRiSN3DC2fufVXYINiYTgKFHR2%2FBiAurwpPxscB6ADjKZkxUJoB4vebby0nqU7UDZSFNcXRKfMJC5%2FbwGOqUBzwSf2RPIp1NUKQ%2B%2BwM6WgWIL2HdnB5zhJHs7cVlPcIBSQw75qQ5KU9Tztyhr6mDCHO%2B39wNwpWwMYW2t1bzzSz4Ew4X%2BUbWF12D1ZLICuCMOQs8S6BY%2FwyGp9lvte%2BOSeHzEJ1E1AU0KMLoK0QoMzh8yqw0mVahtTl1yRNGgRtbB9v3OhhEZ6Zo8EM2uqs4SC1wm5E8J9j2ruh7%2BMmtpGH7UagvQ&X-Amz-Signature=ca6faf27a59d6d6040220bfe7a7173bf44213a094d0975697efdb6d4a85a4f3f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5224KGZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID20DSmqAxnEK2r3Twh804jkdwTpHrCoyvLBuhbyrAJNAiEA2Qa9yASSYt2Fx9bVCmaTOZERhv9TXC72CTGzmZZm2KgqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHTx%2FhTsA5nsh71xVSrcA9%2B2mLo1zGh3wvk8qv2v6PUGR66Zrap6otkNW2b5tJzMgaMHrw4iu2w6oL4EUp8EIr16imTVKxfrhX4V6dclurHqriNbGMaOO%2BQ2UDS64PRreff8EWR3nYq8oIEHIoMwKZNQXtmQCf13JREjVcyqRHzRvR66AJfbf9AmnDgYMjjwL0buN8noGUsyxJpSN3WKo8UONwESUAxIYxEpjGE%2BCyWgW5nXaoctSiOz3k%2BOj%2BBaOd2PSdhvwksOnuSFnj5v83qBBC%2Bn6VGVZPhSy6f7rNHy1AmHH%2FoveYr7hdHmTvRXDuZOwfFC1YqaQrT4EES%2FMHBRtRQxlS42YOnkqzE%2B%2BLKdcwCqGPPqodv%2BHd36vFOLhisgpJ1pPTY8BBcDPc8SGcx8%2BrUawITHj6ToQRVUKRH15g6Xg%2Bp8XAU4tHMAjs5Y7PWbHAXIJxQ3VIzFlGrk8xCl8qiwCHVq4pUmjCTpTouWNDJkfWJ9FYKYDfTE3a1ZYkeI8xA9Ueb9Rqf%2BOCoczoeSHIRSZQ1JciLJigwd8Kcizs7xtO5qh2Teggzfy3sfd0TtBpjHRiSN3DC2fufVXYINiYTgKFHR2%2FBiAurwpPxscB6ADjKZkxUJoB4vebby0nqU7UDZSFNcXRKfMJC5%2FbwGOqUBzwSf2RPIp1NUKQ%2B%2BwM6WgWIL2HdnB5zhJHs7cVlPcIBSQw75qQ5KU9Tztyhr6mDCHO%2B39wNwpWwMYW2t1bzzSz4Ew4X%2BUbWF12D1ZLICuCMOQs8S6BY%2FwyGp9lvte%2BOSeHzEJ1E1AU0KMLoK0QoMzh8yqw0mVahtTl1yRNGgRtbB9v3OhhEZ6Zo8EM2uqs4SC1wm5E8J9j2ruh7%2BMmtpGH7UagvQ&X-Amz-Signature=7cf41962f5a0113ee50b2739723ab6b78c36ed0a439da003733956be09578a7b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
