

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656NAQGBA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCbyuL72A%2FeeUk2bG6CX2zECXEQDTB5tW53L1GtnHNZkgIhAI%2FoyM5g6X7ZwjGXp29nD7GPY4aGHVIQ978UepY9IbmrKv8DCBwQABoMNjM3NDIzMTgzODA1IgyHMMfbMN5FPQXYlUIq3AOTSBPFGBYhis0ueBImHEDj1uMfox8CpgwdfbovxYVo7TARYxpTutNBjMcJp7qizHOUsDG6fBfqr0QwRG%2B%2FpxGsXnjDnz%2FSIHdNTw%2Fk78JjTdMF9%2FjEQkWtrFeTWNiO2jOaXlg0%2Bbf6OaQVdVw4RN%2BsTPNdVdvZjM0QlqyJ1lgOeTiAtEuuroVY%2FGnP1z%2FU6qrnqLechrJDUqlbILSqMNhWN4wtvwNDIrCnNjNK2HnOObQldGy%2Fv2M6PaWUPmhDL35mhWFTKRezdD2eCf57dhQfQYbFeTr1C0vX9%2BL5LE5gNlw%2FHhCNesQ%2Fy0AKSQy2%2FtvOYaaSgcui7dD4Bo353pRJw2UN8iPJznPZ5bNJQVUlovg00ID6Fkx8XRYJ9dYtwk40Qc%2BlOpnKD4nYR3Xnv1%2B3YJTByB3DhRs35le5GTCa3LMrtgglnXxbw6sp8vCDtj7%2FExFEMICpUBFcaINCzXp%2FKQekNuDFt454budDbnVB9FSI522Om%2FvtEOL9ZtpDj8mz18MpV79gSGycx7nD8%2FbdV5g%2BNw4GWS1l4m4t5Vtq10kWw2w3b2EfgeINmeokmyNdJdUXmsyJXdhsATjNILCb%2BAAlGqETqXWAUI40gsLFZreKth2UqpGqYbflLjC7ooS9BjqkAepSka3OB%2BU3BTgWt6WcYdO2t6jc8H2K721zwOc0rP9u4TsMrTtsuhg1QvPK19nfti%2FluvgcS0LH6sk9u1SOQvExuB45i9tLHHDzIn9YgFDZuYwrBxxn41cfwRIutw7zZ5C3XlZ0EHnxfwggtxKcYd4cuqUQ3jlLN1UeeD%2F6Ke6TFGTNvdKkcUjW1SyjpOf7IxGzVgiJrDoPnPReD6KaxlzNJ%2FS4&X-Amz-Signature=411048261565041a062ffd6284da93305faa2fe24f7b4d2099e15ca8081cbccb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656NAQGBA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCbyuL72A%2FeeUk2bG6CX2zECXEQDTB5tW53L1GtnHNZkgIhAI%2FoyM5g6X7ZwjGXp29nD7GPY4aGHVIQ978UepY9IbmrKv8DCBwQABoMNjM3NDIzMTgzODA1IgyHMMfbMN5FPQXYlUIq3AOTSBPFGBYhis0ueBImHEDj1uMfox8CpgwdfbovxYVo7TARYxpTutNBjMcJp7qizHOUsDG6fBfqr0QwRG%2B%2FpxGsXnjDnz%2FSIHdNTw%2Fk78JjTdMF9%2FjEQkWtrFeTWNiO2jOaXlg0%2Bbf6OaQVdVw4RN%2BsTPNdVdvZjM0QlqyJ1lgOeTiAtEuuroVY%2FGnP1z%2FU6qrnqLechrJDUqlbILSqMNhWN4wtvwNDIrCnNjNK2HnOObQldGy%2Fv2M6PaWUPmhDL35mhWFTKRezdD2eCf57dhQfQYbFeTr1C0vX9%2BL5LE5gNlw%2FHhCNesQ%2Fy0AKSQy2%2FtvOYaaSgcui7dD4Bo353pRJw2UN8iPJznPZ5bNJQVUlovg00ID6Fkx8XRYJ9dYtwk40Qc%2BlOpnKD4nYR3Xnv1%2B3YJTByB3DhRs35le5GTCa3LMrtgglnXxbw6sp8vCDtj7%2FExFEMICpUBFcaINCzXp%2FKQekNuDFt454budDbnVB9FSI522Om%2FvtEOL9ZtpDj8mz18MpV79gSGycx7nD8%2FbdV5g%2BNw4GWS1l4m4t5Vtq10kWw2w3b2EfgeINmeokmyNdJdUXmsyJXdhsATjNILCb%2BAAlGqETqXWAUI40gsLFZreKth2UqpGqYbflLjC7ooS9BjqkAepSka3OB%2BU3BTgWt6WcYdO2t6jc8H2K721zwOc0rP9u4TsMrTtsuhg1QvPK19nfti%2FluvgcS0LH6sk9u1SOQvExuB45i9tLHHDzIn9YgFDZuYwrBxxn41cfwRIutw7zZ5C3XlZ0EHnxfwggtxKcYd4cuqUQ3jlLN1UeeD%2F6Ke6TFGTNvdKkcUjW1SyjpOf7IxGzVgiJrDoPnPReD6KaxlzNJ%2FS4&X-Amz-Signature=fb76df243d55fdcd14ff52f3d5cf1d744ad2ab0506ec54653e4af331acc81fdf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656NAQGBA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCbyuL72A%2FeeUk2bG6CX2zECXEQDTB5tW53L1GtnHNZkgIhAI%2FoyM5g6X7ZwjGXp29nD7GPY4aGHVIQ978UepY9IbmrKv8DCBwQABoMNjM3NDIzMTgzODA1IgyHMMfbMN5FPQXYlUIq3AOTSBPFGBYhis0ueBImHEDj1uMfox8CpgwdfbovxYVo7TARYxpTutNBjMcJp7qizHOUsDG6fBfqr0QwRG%2B%2FpxGsXnjDnz%2FSIHdNTw%2Fk78JjTdMF9%2FjEQkWtrFeTWNiO2jOaXlg0%2Bbf6OaQVdVw4RN%2BsTPNdVdvZjM0QlqyJ1lgOeTiAtEuuroVY%2FGnP1z%2FU6qrnqLechrJDUqlbILSqMNhWN4wtvwNDIrCnNjNK2HnOObQldGy%2Fv2M6PaWUPmhDL35mhWFTKRezdD2eCf57dhQfQYbFeTr1C0vX9%2BL5LE5gNlw%2FHhCNesQ%2Fy0AKSQy2%2FtvOYaaSgcui7dD4Bo353pRJw2UN8iPJznPZ5bNJQVUlovg00ID6Fkx8XRYJ9dYtwk40Qc%2BlOpnKD4nYR3Xnv1%2B3YJTByB3DhRs35le5GTCa3LMrtgglnXxbw6sp8vCDtj7%2FExFEMICpUBFcaINCzXp%2FKQekNuDFt454budDbnVB9FSI522Om%2FvtEOL9ZtpDj8mz18MpV79gSGycx7nD8%2FbdV5g%2BNw4GWS1l4m4t5Vtq10kWw2w3b2EfgeINmeokmyNdJdUXmsyJXdhsATjNILCb%2BAAlGqETqXWAUI40gsLFZreKth2UqpGqYbflLjC7ooS9BjqkAepSka3OB%2BU3BTgWt6WcYdO2t6jc8H2K721zwOc0rP9u4TsMrTtsuhg1QvPK19nfti%2FluvgcS0LH6sk9u1SOQvExuB45i9tLHHDzIn9YgFDZuYwrBxxn41cfwRIutw7zZ5C3XlZ0EHnxfwggtxKcYd4cuqUQ3jlLN1UeeD%2F6Ke6TFGTNvdKkcUjW1SyjpOf7IxGzVgiJrDoPnPReD6KaxlzNJ%2FS4&X-Amz-Signature=e1543a09995a40d0c4996ed5ce083da1dad314880d36937502e250e20e8e09a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656NAQGBA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCbyuL72A%2FeeUk2bG6CX2zECXEQDTB5tW53L1GtnHNZkgIhAI%2FoyM5g6X7ZwjGXp29nD7GPY4aGHVIQ978UepY9IbmrKv8DCBwQABoMNjM3NDIzMTgzODA1IgyHMMfbMN5FPQXYlUIq3AOTSBPFGBYhis0ueBImHEDj1uMfox8CpgwdfbovxYVo7TARYxpTutNBjMcJp7qizHOUsDG6fBfqr0QwRG%2B%2FpxGsXnjDnz%2FSIHdNTw%2Fk78JjTdMF9%2FjEQkWtrFeTWNiO2jOaXlg0%2Bbf6OaQVdVw4RN%2BsTPNdVdvZjM0QlqyJ1lgOeTiAtEuuroVY%2FGnP1z%2FU6qrnqLechrJDUqlbILSqMNhWN4wtvwNDIrCnNjNK2HnOObQldGy%2Fv2M6PaWUPmhDL35mhWFTKRezdD2eCf57dhQfQYbFeTr1C0vX9%2BL5LE5gNlw%2FHhCNesQ%2Fy0AKSQy2%2FtvOYaaSgcui7dD4Bo353pRJw2UN8iPJznPZ5bNJQVUlovg00ID6Fkx8XRYJ9dYtwk40Qc%2BlOpnKD4nYR3Xnv1%2B3YJTByB3DhRs35le5GTCa3LMrtgglnXxbw6sp8vCDtj7%2FExFEMICpUBFcaINCzXp%2FKQekNuDFt454budDbnVB9FSI522Om%2FvtEOL9ZtpDj8mz18MpV79gSGycx7nD8%2FbdV5g%2BNw4GWS1l4m4t5Vtq10kWw2w3b2EfgeINmeokmyNdJdUXmsyJXdhsATjNILCb%2BAAlGqETqXWAUI40gsLFZreKth2UqpGqYbflLjC7ooS9BjqkAepSka3OB%2BU3BTgWt6WcYdO2t6jc8H2K721zwOc0rP9u4TsMrTtsuhg1QvPK19nfti%2FluvgcS0LH6sk9u1SOQvExuB45i9tLHHDzIn9YgFDZuYwrBxxn41cfwRIutw7zZ5C3XlZ0EHnxfwggtxKcYd4cuqUQ3jlLN1UeeD%2F6Ke6TFGTNvdKkcUjW1SyjpOf7IxGzVgiJrDoPnPReD6KaxlzNJ%2FS4&X-Amz-Signature=e019bf69bca3d1ab974c52da0cf258c0dfaa59098d55e71c674cfcf32cae04e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656NAQGBA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCbyuL72A%2FeeUk2bG6CX2zECXEQDTB5tW53L1GtnHNZkgIhAI%2FoyM5g6X7ZwjGXp29nD7GPY4aGHVIQ978UepY9IbmrKv8DCBwQABoMNjM3NDIzMTgzODA1IgyHMMfbMN5FPQXYlUIq3AOTSBPFGBYhis0ueBImHEDj1uMfox8CpgwdfbovxYVo7TARYxpTutNBjMcJp7qizHOUsDG6fBfqr0QwRG%2B%2FpxGsXnjDnz%2FSIHdNTw%2Fk78JjTdMF9%2FjEQkWtrFeTWNiO2jOaXlg0%2Bbf6OaQVdVw4RN%2BsTPNdVdvZjM0QlqyJ1lgOeTiAtEuuroVY%2FGnP1z%2FU6qrnqLechrJDUqlbILSqMNhWN4wtvwNDIrCnNjNK2HnOObQldGy%2Fv2M6PaWUPmhDL35mhWFTKRezdD2eCf57dhQfQYbFeTr1C0vX9%2BL5LE5gNlw%2FHhCNesQ%2Fy0AKSQy2%2FtvOYaaSgcui7dD4Bo353pRJw2UN8iPJznPZ5bNJQVUlovg00ID6Fkx8XRYJ9dYtwk40Qc%2BlOpnKD4nYR3Xnv1%2B3YJTByB3DhRs35le5GTCa3LMrtgglnXxbw6sp8vCDtj7%2FExFEMICpUBFcaINCzXp%2FKQekNuDFt454budDbnVB9FSI522Om%2FvtEOL9ZtpDj8mz18MpV79gSGycx7nD8%2FbdV5g%2BNw4GWS1l4m4t5Vtq10kWw2w3b2EfgeINmeokmyNdJdUXmsyJXdhsATjNILCb%2BAAlGqETqXWAUI40gsLFZreKth2UqpGqYbflLjC7ooS9BjqkAepSka3OB%2BU3BTgWt6WcYdO2t6jc8H2K721zwOc0rP9u4TsMrTtsuhg1QvPK19nfti%2FluvgcS0LH6sk9u1SOQvExuB45i9tLHHDzIn9YgFDZuYwrBxxn41cfwRIutw7zZ5C3XlZ0EHnxfwggtxKcYd4cuqUQ3jlLN1UeeD%2F6Ke6TFGTNvdKkcUjW1SyjpOf7IxGzVgiJrDoPnPReD6KaxlzNJ%2FS4&X-Amz-Signature=a80fbe235bae79b7020cf4a3399d5d7cf09aea075421f00905c3aa18595eeb0c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656NAQGBA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCbyuL72A%2FeeUk2bG6CX2zECXEQDTB5tW53L1GtnHNZkgIhAI%2FoyM5g6X7ZwjGXp29nD7GPY4aGHVIQ978UepY9IbmrKv8DCBwQABoMNjM3NDIzMTgzODA1IgyHMMfbMN5FPQXYlUIq3AOTSBPFGBYhis0ueBImHEDj1uMfox8CpgwdfbovxYVo7TARYxpTutNBjMcJp7qizHOUsDG6fBfqr0QwRG%2B%2FpxGsXnjDnz%2FSIHdNTw%2Fk78JjTdMF9%2FjEQkWtrFeTWNiO2jOaXlg0%2Bbf6OaQVdVw4RN%2BsTPNdVdvZjM0QlqyJ1lgOeTiAtEuuroVY%2FGnP1z%2FU6qrnqLechrJDUqlbILSqMNhWN4wtvwNDIrCnNjNK2HnOObQldGy%2Fv2M6PaWUPmhDL35mhWFTKRezdD2eCf57dhQfQYbFeTr1C0vX9%2BL5LE5gNlw%2FHhCNesQ%2Fy0AKSQy2%2FtvOYaaSgcui7dD4Bo353pRJw2UN8iPJznPZ5bNJQVUlovg00ID6Fkx8XRYJ9dYtwk40Qc%2BlOpnKD4nYR3Xnv1%2B3YJTByB3DhRs35le5GTCa3LMrtgglnXxbw6sp8vCDtj7%2FExFEMICpUBFcaINCzXp%2FKQekNuDFt454budDbnVB9FSI522Om%2FvtEOL9ZtpDj8mz18MpV79gSGycx7nD8%2FbdV5g%2BNw4GWS1l4m4t5Vtq10kWw2w3b2EfgeINmeokmyNdJdUXmsyJXdhsATjNILCb%2BAAlGqETqXWAUI40gsLFZreKth2UqpGqYbflLjC7ooS9BjqkAepSka3OB%2BU3BTgWt6WcYdO2t6jc8H2K721zwOc0rP9u4TsMrTtsuhg1QvPK19nfti%2FluvgcS0LH6sk9u1SOQvExuB45i9tLHHDzIn9YgFDZuYwrBxxn41cfwRIutw7zZ5C3XlZ0EHnxfwggtxKcYd4cuqUQ3jlLN1UeeD%2F6Ke6TFGTNvdKkcUjW1SyjpOf7IxGzVgiJrDoPnPReD6KaxlzNJ%2FS4&X-Amz-Signature=036e181fc3ecd72812852427ec5f345589428b3708f222d8d8ff4f70993ecceb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656NAQGBA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCbyuL72A%2FeeUk2bG6CX2zECXEQDTB5tW53L1GtnHNZkgIhAI%2FoyM5g6X7ZwjGXp29nD7GPY4aGHVIQ978UepY9IbmrKv8DCBwQABoMNjM3NDIzMTgzODA1IgyHMMfbMN5FPQXYlUIq3AOTSBPFGBYhis0ueBImHEDj1uMfox8CpgwdfbovxYVo7TARYxpTutNBjMcJp7qizHOUsDG6fBfqr0QwRG%2B%2FpxGsXnjDnz%2FSIHdNTw%2Fk78JjTdMF9%2FjEQkWtrFeTWNiO2jOaXlg0%2Bbf6OaQVdVw4RN%2BsTPNdVdvZjM0QlqyJ1lgOeTiAtEuuroVY%2FGnP1z%2FU6qrnqLechrJDUqlbILSqMNhWN4wtvwNDIrCnNjNK2HnOObQldGy%2Fv2M6PaWUPmhDL35mhWFTKRezdD2eCf57dhQfQYbFeTr1C0vX9%2BL5LE5gNlw%2FHhCNesQ%2Fy0AKSQy2%2FtvOYaaSgcui7dD4Bo353pRJw2UN8iPJznPZ5bNJQVUlovg00ID6Fkx8XRYJ9dYtwk40Qc%2BlOpnKD4nYR3Xnv1%2B3YJTByB3DhRs35le5GTCa3LMrtgglnXxbw6sp8vCDtj7%2FExFEMICpUBFcaINCzXp%2FKQekNuDFt454budDbnVB9FSI522Om%2FvtEOL9ZtpDj8mz18MpV79gSGycx7nD8%2FbdV5g%2BNw4GWS1l4m4t5Vtq10kWw2w3b2EfgeINmeokmyNdJdUXmsyJXdhsATjNILCb%2BAAlGqETqXWAUI40gsLFZreKth2UqpGqYbflLjC7ooS9BjqkAepSka3OB%2BU3BTgWt6WcYdO2t6jc8H2K721zwOc0rP9u4TsMrTtsuhg1QvPK19nfti%2FluvgcS0LH6sk9u1SOQvExuB45i9tLHHDzIn9YgFDZuYwrBxxn41cfwRIutw7zZ5C3XlZ0EHnxfwggtxKcYd4cuqUQ3jlLN1UeeD%2F6Ke6TFGTNvdKkcUjW1SyjpOf7IxGzVgiJrDoPnPReD6KaxlzNJ%2FS4&X-Amz-Signature=ebbc8452299b268c2c95c8ca9e8c0508ec0d35b3c793820e78143a71cf044e06&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656NAQGBA%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCbyuL72A%2FeeUk2bG6CX2zECXEQDTB5tW53L1GtnHNZkgIhAI%2FoyM5g6X7ZwjGXp29nD7GPY4aGHVIQ978UepY9IbmrKv8DCBwQABoMNjM3NDIzMTgzODA1IgyHMMfbMN5FPQXYlUIq3AOTSBPFGBYhis0ueBImHEDj1uMfox8CpgwdfbovxYVo7TARYxpTutNBjMcJp7qizHOUsDG6fBfqr0QwRG%2B%2FpxGsXnjDnz%2FSIHdNTw%2Fk78JjTdMF9%2FjEQkWtrFeTWNiO2jOaXlg0%2Bbf6OaQVdVw4RN%2BsTPNdVdvZjM0QlqyJ1lgOeTiAtEuuroVY%2FGnP1z%2FU6qrnqLechrJDUqlbILSqMNhWN4wtvwNDIrCnNjNK2HnOObQldGy%2Fv2M6PaWUPmhDL35mhWFTKRezdD2eCf57dhQfQYbFeTr1C0vX9%2BL5LE5gNlw%2FHhCNesQ%2Fy0AKSQy2%2FtvOYaaSgcui7dD4Bo353pRJw2UN8iPJznPZ5bNJQVUlovg00ID6Fkx8XRYJ9dYtwk40Qc%2BlOpnKD4nYR3Xnv1%2B3YJTByB3DhRs35le5GTCa3LMrtgglnXxbw6sp8vCDtj7%2FExFEMICpUBFcaINCzXp%2FKQekNuDFt454budDbnVB9FSI522Om%2FvtEOL9ZtpDj8mz18MpV79gSGycx7nD8%2FbdV5g%2BNw4GWS1l4m4t5Vtq10kWw2w3b2EfgeINmeokmyNdJdUXmsyJXdhsATjNILCb%2BAAlGqETqXWAUI40gsLFZreKth2UqpGqYbflLjC7ooS9BjqkAepSka3OB%2BU3BTgWt6WcYdO2t6jc8H2K721zwOc0rP9u4TsMrTtsuhg1QvPK19nfti%2FluvgcS0LH6sk9u1SOQvExuB45i9tLHHDzIn9YgFDZuYwrBxxn41cfwRIutw7zZ5C3XlZ0EHnxfwggtxKcYd4cuqUQ3jlLN1UeeD%2F6Ke6TFGTNvdKkcUjW1SyjpOf7IxGzVgiJrDoPnPReD6KaxlzNJ%2FS4&X-Amz-Signature=4758228918085c11d07f0398fee44921f4c6f238d7a1defd7c5b17ac6abc86e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZUBGUI5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIAd0r%2FnFVflCXa2dL6JWcPbnRPB7tdshMfm8wL80FH8vAiEAs6v6q%2BdqcjpiIP2lbndJsU8K0ggyEhHp34nPTm6LR%2Bgq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDAlmJ7hFNURmupdNYircA1qrRrUfzXUSPdUH3EYZd5r5HGKnpToXcWTpHw%2FkvQnABcLWhkDAjFuENBbyMdHYQuO5oWLiG5pDm2wFWtMpR8iNZ2KSA3fsT0DsL2RGi3rEdHY1hRwc9dPvdJm5%2B8V7XkrBEV8wRKnsZYzGRRy3xdUVO4tO%2Bn4eGCHEAY2KaprkNzvoRZegvyJT7VLzuTEuip%2Bd2uplLGpLMDwvVJWQTpYxN2Pt1xB4TWz0tsP00PCdspxqom2UEkgxOxJ2ks1mKxFXL4dgkfziLA0vmHPiHOCRNgr%2FDUPTnqs2l6Jy2kdpcFItiUVFcf0YWlh3VsVJHOHr4zYPBLTx%2FYM4P6wLZ98OBsTsM6qfscm77dsS70E3PrOyQfi015eg4o78dZKIaH2z7rav2FaxlFQkLTW%2ByjCh6rs1HcIOK2Gezvj19nc2neuZSv1p%2BaLXBYmKe5lfwOWyUQSVPgL%2FoGrQWCmArZJkiLy8uyPgXQcM0yI9PjfCwdaDPdzfyqhGxDyoGle6qIymIYLegyMTlxnxcC2RgiM3887yY5S3S3ziN4UhAaFEX319I37Ve%2Fh8e42gpXy0MwAVBJ8FP7Jnk6gHFgnQQxaAN50VWP9HHtJ9CtLPWeY91uQW1TEje%2B6pUUYWMPyghL0GOqUBK%2FQH4SUrz3iG7MCRG1SYHPdbngbxACyda1SxLPtryVBYLv4sRYwoP4GlhMYeyEHDp6r1YNMHUOEZ9x1bbU%2BLuTShqZjuEiY5iszvc85vqG5iWHTuY5ivo4PiSxlB%2FxsU%2Bi%2FsIMFwGCGUiWDJBymCzO0K5g1kPMeg2Ua%2F5JnEnD8ScrWGbhVRagho5iitFCWvBelH5ib3R3FZrfDC8cJZkwiZu3jv&X-Amz-Signature=4b4a99985584c607fcb9c2967bf1683b7e3e827991904c9a5edf1263a068f2da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X4PTWCN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIAR3Y5i7ttuIUzOiTsOEQg9poHtDodmqKAK5SsPbHkymAiEAnZ5gEZZOshZqiolKaoZNzPCFKPo%2BdNMPDwtOY6VHZJMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDAKKftNxoDVHTUz4jircA2FbFQyrLf0hTfTFLmuXXqm%2BbaVH1V7oVAy8hysNKt6t%2FT474diIvjEgePVi6jcsZBe%2BvjrEYuqYPIIDooP%2BUdIImT5u03MaDEfuo0edHMf3srDc42KqKzrxixoMyuzq4BFzh26IzY%2FFZ80IUTxNtMIIlhBakWoyHy9osqr304XYS8jxVkRTZjYe8S2hEtxni%2Fxxfd0xSQQl%2BlKvt%2B12PkFWKJE%2FHrGM4ztnQ7WiRqYBWaEDpop98EhTHNWQ%2BI3JmCzhetE%2F%2BfLw%2BC%2FATJLvkpI2jFXdv7qrVqRF8Mfu7nR7Dzm0wobfw6xHat7qF%2Futm9Kg1kaviB2z6NOHRmpXliLhsCp4N19hbkfVnlED1erH26kFHTacg7tXbXCkynvuaiFgvURezChZGloP7dKyMyAxlZSJbzWBubC5WixdCo9azToqWymFvQHG86m2lkBLyZ9dg8KDVJBJW%2Fp1oE9AHO7UZJ74EAASUx5caq3ZKo1eWKapDQYigAF0ZcWQo%2BXOgA%2FLfZvQvwDnQ81kh6Pnp%2B%2F40LguqTgJ9Lr8HoAdijBCwbda5hrqcqOwBymh6s%2BLSxxjv1oHUS5sTUPWVwggA8nP7QNuffe2cTwL6WvVFYQI%2FbeNOIwb6MRqZgBFMJaihL0GOqUB5pgC%2BVElGekpKjuzGKtInaPUuX410kBmiM0zI6d5G9ghFovgsVcXPS%2B6yozwcdiQBGC8bbWxdWAEH%2F62t2LpJ7JNqLhlwuVnHdEb0vAu7s84HyXAc9oV9MdVsHRDkBuebNdGOL5sfCqE3Qslt8oG58I%2BimB0MDqTngvXQG5x21FggKakPrCMMwRbw3kEGT0gRrxFjUdDSXf86TSuyROOPDs5lfOp&X-Amz-Signature=b0bcf2811fb71fd9138062a493ddfd966e2e31b777d984476ab8a6c61d6d29a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMFXGNDY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDYWxUR3MTc13sOjB76cC4F6eGfRGT3KXdpSybL8AzgZwIgDDSC86iFr1tmD02zLG%2F56w3aiZuOxvyai9VQ4VIMwGEq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDEpsgu71RENbzahDKyrcA5xE5DOGq1thCltXRmyfm0gOY3VYGdr0BuazShErYjyWGcBeaq9Vkk93BhPu7m4OZTtme3T2%2Fv%2F2KPesb4rstp7J2d12iKYbu112XJSJiNvv6rEiaTcy3%2FrMbj7tAEJHvlfWYAur783He8LCiaULMyh4THOJbSjJdevbk8du8XkS2I4DZV%2FeWryCceurFTNdLwJsOghyZiBsrvCWH%2FZqDKNSJUs5KsuCiYArQNSnUsxqOOROBkY%2Fg4Nb21oqxWI%2BguyqsNghyi2ZvpgWUspoEjyqZ%2FKldLYXs9R1V8f4DWIQXLNZUShgT6yw%2FyH0XrKKcpGiGYwU9aSzLDAA4Um0SC67xe5i%2FsLUmbAX3zfYJcT9ehHvSnoTJadOHPY2HnEr1Oz8%2BkfBW0mzq0ekX05yTt2Y6SFPi1R3xlgHR7ai18Sx2fvmx7JHjeeUjQqZAa4zwp3J%2BH%2B8%2B4cbXSWnG%2FCwBcx%2BIK0mR5Rzvl2WUVKZv1EWanHBSD6KvhNZAaPtp6mo6UH3fd104RfTqXLdcIx%2BCkFOBq59%2BDcaACSJeeXOmK0qlTssGyAC4KlBzG4rIxvPRodsOAMv1gvPLCKT%2FnP4pUsW%2Fkdnj0I05G2LU4kyzgdLFBHPqzrDpdZuBmK3MLeihL0GOqUBNyMlfEVISO8Qdgy1YM01fRGoPWRfYpqmeLbrOXOb4RML5ve6bi9%2FpWQSGO5ui41L%2FJkKUNJ248YpiQObkE4Lvaym5Cg7B%2BTwDnWe71UTmh0bw%2FqeaO7gNPyvMDc%2BTpCzpvM34rqyjQfebJE2wIRshfjqHOIyQ3M0KTusMWLTy9BPSFrgHkUwaDNJuK7AWkDzTr6pEawEqvpt7FNS7T95G1In3Paj&X-Amz-Signature=465a5cb440001ac879fcf4c3e9d93e2d4041be941661cebf2de26d5946efd204&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMFXGNDY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDYWxUR3MTc13sOjB76cC4F6eGfRGT3KXdpSybL8AzgZwIgDDSC86iFr1tmD02zLG%2F56w3aiZuOxvyai9VQ4VIMwGEq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDEpsgu71RENbzahDKyrcA5xE5DOGq1thCltXRmyfm0gOY3VYGdr0BuazShErYjyWGcBeaq9Vkk93BhPu7m4OZTtme3T2%2Fv%2F2KPesb4rstp7J2d12iKYbu112XJSJiNvv6rEiaTcy3%2FrMbj7tAEJHvlfWYAur783He8LCiaULMyh4THOJbSjJdevbk8du8XkS2I4DZV%2FeWryCceurFTNdLwJsOghyZiBsrvCWH%2FZqDKNSJUs5KsuCiYArQNSnUsxqOOROBkY%2Fg4Nb21oqxWI%2BguyqsNghyi2ZvpgWUspoEjyqZ%2FKldLYXs9R1V8f4DWIQXLNZUShgT6yw%2FyH0XrKKcpGiGYwU9aSzLDAA4Um0SC67xe5i%2FsLUmbAX3zfYJcT9ehHvSnoTJadOHPY2HnEr1Oz8%2BkfBW0mzq0ekX05yTt2Y6SFPi1R3xlgHR7ai18Sx2fvmx7JHjeeUjQqZAa4zwp3J%2BH%2B8%2B4cbXSWnG%2FCwBcx%2BIK0mR5Rzvl2WUVKZv1EWanHBSD6KvhNZAaPtp6mo6UH3fd104RfTqXLdcIx%2BCkFOBq59%2BDcaACSJeeXOmK0qlTssGyAC4KlBzG4rIxvPRodsOAMv1gvPLCKT%2FnP4pUsW%2Fkdnj0I05G2LU4kyzgdLFBHPqzrDpdZuBmK3MLeihL0GOqUBNyMlfEVISO8Qdgy1YM01fRGoPWRfYpqmeLbrOXOb4RML5ve6bi9%2FpWQSGO5ui41L%2FJkKUNJ248YpiQObkE4Lvaym5Cg7B%2BTwDnWe71UTmh0bw%2FqeaO7gNPyvMDc%2BTpCzpvM34rqyjQfebJE2wIRshfjqHOIyQ3M0KTusMWLTy9BPSFrgHkUwaDNJuK7AWkDzTr6pEawEqvpt7FNS7T95G1In3Paj&X-Amz-Signature=96dfd08b458cfe469d7a089e3f9b0d3c0864987b00b3b676fdcab280e64b7986&X-Amz-SignedHeaders=host&x-id=GetObject)
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
