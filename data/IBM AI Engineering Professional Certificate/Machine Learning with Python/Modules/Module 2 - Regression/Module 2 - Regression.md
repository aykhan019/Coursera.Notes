

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRDCGXD2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTbVCoKOPfnicXZgGvBNlAf8KlImEZd%2BdJj8FIBbhXyAIgOajpQwMreQZ0%2B8LAzllNLq%2B4SemMVOufEr6YZZzx6OEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7ZdR5yU19V8Ak2HyrcA1yKDWALQHimaT9Ebc8gZAUSByzkzUWE1BSFywGMDnwoi6GVc%2BFtb5cTHPVQ20aVNij8zLBPVFl46WQ4IlictRkzeG5YDThgP01mSODu7tn4ODe9c1UJD7naGujmnLRGAVfd1fF%2B7SYQQnuQLVSRGnPovlLg3s0%2BF2hrxlMIYmqanktSF0QpFALEt0kJfkv4l6eUeDoVnLMoAIK1EUXy3fMp62exH90YeltckhkgzHEWb2zOy5Rv%2F3u6Dif%2BK%2FO32WtiuycVXlNORVHLmrD%2FFimffaIGSfLNy0qUJOpYuNwQHNyWCNH87G8fRcjny3mVKwA5i43q2B9KtksWcqHs3xCLCTeg%2BFiIJ48nJ0j3NreUYvDtxD3Hq6C2xDV81x46yPLKmTB2Ks1kZeXq30hO4VV52jd2ctAbGAJ5BYGTnp8LwrZdsn%2F9mDECOSRkAB%2FGYh34ipe1v6q8jgVJ4%2BTrbagLMoJr9%2FeQ4U3K8009BjnYGjLxn9MD6jlxf1JzmoOBR2aQVquaz8psw0Mma9z2QIW7AhF5B9yZOMPGQjWF6tMx3oOk6PdTSMzozbTgQsjEb3q4yEILLpV0QpFxMmzfiD9K7Q3sZ8VA%2FtdITOJjtiqGGsuv13pxfBnK7EuvMN3e%2FrwGOqUB1DYA3AUxZloK8qcPZi4V04WKIsLMaPWVVQUT0gwe%2F%2BQoC8hMpLvAA9f691i61Zpl2upTwexMZLfxGeJi5k8zS71%2FV7uaVrRoqpk%2FqFCA8%2Bn8tfb1nY1E55q9dj910O6aMOsB5BZq5C60dkmeVhFC55vqa%2B3uN%2FMZoQ5y8T61zaM9KaLpFOJgigZdvaa1SRF4yfkLI0vtNxKDLL11G%2FpZYMF1DqH6&X-Amz-Signature=c4c1fc33fda3223db4fcb315f23bc24f0737cf3a259075913d1a9a54c0d07021&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRDCGXD2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTbVCoKOPfnicXZgGvBNlAf8KlImEZd%2BdJj8FIBbhXyAIgOajpQwMreQZ0%2B8LAzllNLq%2B4SemMVOufEr6YZZzx6OEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7ZdR5yU19V8Ak2HyrcA1yKDWALQHimaT9Ebc8gZAUSByzkzUWE1BSFywGMDnwoi6GVc%2BFtb5cTHPVQ20aVNij8zLBPVFl46WQ4IlictRkzeG5YDThgP01mSODu7tn4ODe9c1UJD7naGujmnLRGAVfd1fF%2B7SYQQnuQLVSRGnPovlLg3s0%2BF2hrxlMIYmqanktSF0QpFALEt0kJfkv4l6eUeDoVnLMoAIK1EUXy3fMp62exH90YeltckhkgzHEWb2zOy5Rv%2F3u6Dif%2BK%2FO32WtiuycVXlNORVHLmrD%2FFimffaIGSfLNy0qUJOpYuNwQHNyWCNH87G8fRcjny3mVKwA5i43q2B9KtksWcqHs3xCLCTeg%2BFiIJ48nJ0j3NreUYvDtxD3Hq6C2xDV81x46yPLKmTB2Ks1kZeXq30hO4VV52jd2ctAbGAJ5BYGTnp8LwrZdsn%2F9mDECOSRkAB%2FGYh34ipe1v6q8jgVJ4%2BTrbagLMoJr9%2FeQ4U3K8009BjnYGjLxn9MD6jlxf1JzmoOBR2aQVquaz8psw0Mma9z2QIW7AhF5B9yZOMPGQjWF6tMx3oOk6PdTSMzozbTgQsjEb3q4yEILLpV0QpFxMmzfiD9K7Q3sZ8VA%2FtdITOJjtiqGGsuv13pxfBnK7EuvMN3e%2FrwGOqUB1DYA3AUxZloK8qcPZi4V04WKIsLMaPWVVQUT0gwe%2F%2BQoC8hMpLvAA9f691i61Zpl2upTwexMZLfxGeJi5k8zS71%2FV7uaVrRoqpk%2FqFCA8%2Bn8tfb1nY1E55q9dj910O6aMOsB5BZq5C60dkmeVhFC55vqa%2B3uN%2FMZoQ5y8T61zaM9KaLpFOJgigZdvaa1SRF4yfkLI0vtNxKDLL11G%2FpZYMF1DqH6&X-Amz-Signature=8f9bf1cd8c73cad549682dd1c50d8a7ffd48a2ca2dc7f7dc7ba614d8534af35b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRDCGXD2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTbVCoKOPfnicXZgGvBNlAf8KlImEZd%2BdJj8FIBbhXyAIgOajpQwMreQZ0%2B8LAzllNLq%2B4SemMVOufEr6YZZzx6OEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7ZdR5yU19V8Ak2HyrcA1yKDWALQHimaT9Ebc8gZAUSByzkzUWE1BSFywGMDnwoi6GVc%2BFtb5cTHPVQ20aVNij8zLBPVFl46WQ4IlictRkzeG5YDThgP01mSODu7tn4ODe9c1UJD7naGujmnLRGAVfd1fF%2B7SYQQnuQLVSRGnPovlLg3s0%2BF2hrxlMIYmqanktSF0QpFALEt0kJfkv4l6eUeDoVnLMoAIK1EUXy3fMp62exH90YeltckhkgzHEWb2zOy5Rv%2F3u6Dif%2BK%2FO32WtiuycVXlNORVHLmrD%2FFimffaIGSfLNy0qUJOpYuNwQHNyWCNH87G8fRcjny3mVKwA5i43q2B9KtksWcqHs3xCLCTeg%2BFiIJ48nJ0j3NreUYvDtxD3Hq6C2xDV81x46yPLKmTB2Ks1kZeXq30hO4VV52jd2ctAbGAJ5BYGTnp8LwrZdsn%2F9mDECOSRkAB%2FGYh34ipe1v6q8jgVJ4%2BTrbagLMoJr9%2FeQ4U3K8009BjnYGjLxn9MD6jlxf1JzmoOBR2aQVquaz8psw0Mma9z2QIW7AhF5B9yZOMPGQjWF6tMx3oOk6PdTSMzozbTgQsjEb3q4yEILLpV0QpFxMmzfiD9K7Q3sZ8VA%2FtdITOJjtiqGGsuv13pxfBnK7EuvMN3e%2FrwGOqUB1DYA3AUxZloK8qcPZi4V04WKIsLMaPWVVQUT0gwe%2F%2BQoC8hMpLvAA9f691i61Zpl2upTwexMZLfxGeJi5k8zS71%2FV7uaVrRoqpk%2FqFCA8%2Bn8tfb1nY1E55q9dj910O6aMOsB5BZq5C60dkmeVhFC55vqa%2B3uN%2FMZoQ5y8T61zaM9KaLpFOJgigZdvaa1SRF4yfkLI0vtNxKDLL11G%2FpZYMF1DqH6&X-Amz-Signature=6d54ad4502eeba7badca3d71ec2135602d36b5dc0508cd0eb852c4082a6d0d51&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRDCGXD2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTbVCoKOPfnicXZgGvBNlAf8KlImEZd%2BdJj8FIBbhXyAIgOajpQwMreQZ0%2B8LAzllNLq%2B4SemMVOufEr6YZZzx6OEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7ZdR5yU19V8Ak2HyrcA1yKDWALQHimaT9Ebc8gZAUSByzkzUWE1BSFywGMDnwoi6GVc%2BFtb5cTHPVQ20aVNij8zLBPVFl46WQ4IlictRkzeG5YDThgP01mSODu7tn4ODe9c1UJD7naGujmnLRGAVfd1fF%2B7SYQQnuQLVSRGnPovlLg3s0%2BF2hrxlMIYmqanktSF0QpFALEt0kJfkv4l6eUeDoVnLMoAIK1EUXy3fMp62exH90YeltckhkgzHEWb2zOy5Rv%2F3u6Dif%2BK%2FO32WtiuycVXlNORVHLmrD%2FFimffaIGSfLNy0qUJOpYuNwQHNyWCNH87G8fRcjny3mVKwA5i43q2B9KtksWcqHs3xCLCTeg%2BFiIJ48nJ0j3NreUYvDtxD3Hq6C2xDV81x46yPLKmTB2Ks1kZeXq30hO4VV52jd2ctAbGAJ5BYGTnp8LwrZdsn%2F9mDECOSRkAB%2FGYh34ipe1v6q8jgVJ4%2BTrbagLMoJr9%2FeQ4U3K8009BjnYGjLxn9MD6jlxf1JzmoOBR2aQVquaz8psw0Mma9z2QIW7AhF5B9yZOMPGQjWF6tMx3oOk6PdTSMzozbTgQsjEb3q4yEILLpV0QpFxMmzfiD9K7Q3sZ8VA%2FtdITOJjtiqGGsuv13pxfBnK7EuvMN3e%2FrwGOqUB1DYA3AUxZloK8qcPZi4V04WKIsLMaPWVVQUT0gwe%2F%2BQoC8hMpLvAA9f691i61Zpl2upTwexMZLfxGeJi5k8zS71%2FV7uaVrRoqpk%2FqFCA8%2Bn8tfb1nY1E55q9dj910O6aMOsB5BZq5C60dkmeVhFC55vqa%2B3uN%2FMZoQ5y8T61zaM9KaLpFOJgigZdvaa1SRF4yfkLI0vtNxKDLL11G%2FpZYMF1DqH6&X-Amz-Signature=858ba1d7eff48bc27f651e8f2be6b4dcdb7741ef64ff52ae69ea478833944bf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRDCGXD2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTbVCoKOPfnicXZgGvBNlAf8KlImEZd%2BdJj8FIBbhXyAIgOajpQwMreQZ0%2B8LAzllNLq%2B4SemMVOufEr6YZZzx6OEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7ZdR5yU19V8Ak2HyrcA1yKDWALQHimaT9Ebc8gZAUSByzkzUWE1BSFywGMDnwoi6GVc%2BFtb5cTHPVQ20aVNij8zLBPVFl46WQ4IlictRkzeG5YDThgP01mSODu7tn4ODe9c1UJD7naGujmnLRGAVfd1fF%2B7SYQQnuQLVSRGnPovlLg3s0%2BF2hrxlMIYmqanktSF0QpFALEt0kJfkv4l6eUeDoVnLMoAIK1EUXy3fMp62exH90YeltckhkgzHEWb2zOy5Rv%2F3u6Dif%2BK%2FO32WtiuycVXlNORVHLmrD%2FFimffaIGSfLNy0qUJOpYuNwQHNyWCNH87G8fRcjny3mVKwA5i43q2B9KtksWcqHs3xCLCTeg%2BFiIJ48nJ0j3NreUYvDtxD3Hq6C2xDV81x46yPLKmTB2Ks1kZeXq30hO4VV52jd2ctAbGAJ5BYGTnp8LwrZdsn%2F9mDECOSRkAB%2FGYh34ipe1v6q8jgVJ4%2BTrbagLMoJr9%2FeQ4U3K8009BjnYGjLxn9MD6jlxf1JzmoOBR2aQVquaz8psw0Mma9z2QIW7AhF5B9yZOMPGQjWF6tMx3oOk6PdTSMzozbTgQsjEb3q4yEILLpV0QpFxMmzfiD9K7Q3sZ8VA%2FtdITOJjtiqGGsuv13pxfBnK7EuvMN3e%2FrwGOqUB1DYA3AUxZloK8qcPZi4V04WKIsLMaPWVVQUT0gwe%2F%2BQoC8hMpLvAA9f691i61Zpl2upTwexMZLfxGeJi5k8zS71%2FV7uaVrRoqpk%2FqFCA8%2Bn8tfb1nY1E55q9dj910O6aMOsB5BZq5C60dkmeVhFC55vqa%2B3uN%2FMZoQ5y8T61zaM9KaLpFOJgigZdvaa1SRF4yfkLI0vtNxKDLL11G%2FpZYMF1DqH6&X-Amz-Signature=3bc94f67a39be3b636e0b4800ceb6ab77f62dd571bd8998b48dbe4c9672999bf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRDCGXD2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTbVCoKOPfnicXZgGvBNlAf8KlImEZd%2BdJj8FIBbhXyAIgOajpQwMreQZ0%2B8LAzllNLq%2B4SemMVOufEr6YZZzx6OEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7ZdR5yU19V8Ak2HyrcA1yKDWALQHimaT9Ebc8gZAUSByzkzUWE1BSFywGMDnwoi6GVc%2BFtb5cTHPVQ20aVNij8zLBPVFl46WQ4IlictRkzeG5YDThgP01mSODu7tn4ODe9c1UJD7naGujmnLRGAVfd1fF%2B7SYQQnuQLVSRGnPovlLg3s0%2BF2hrxlMIYmqanktSF0QpFALEt0kJfkv4l6eUeDoVnLMoAIK1EUXy3fMp62exH90YeltckhkgzHEWb2zOy5Rv%2F3u6Dif%2BK%2FO32WtiuycVXlNORVHLmrD%2FFimffaIGSfLNy0qUJOpYuNwQHNyWCNH87G8fRcjny3mVKwA5i43q2B9KtksWcqHs3xCLCTeg%2BFiIJ48nJ0j3NreUYvDtxD3Hq6C2xDV81x46yPLKmTB2Ks1kZeXq30hO4VV52jd2ctAbGAJ5BYGTnp8LwrZdsn%2F9mDECOSRkAB%2FGYh34ipe1v6q8jgVJ4%2BTrbagLMoJr9%2FeQ4U3K8009BjnYGjLxn9MD6jlxf1JzmoOBR2aQVquaz8psw0Mma9z2QIW7AhF5B9yZOMPGQjWF6tMx3oOk6PdTSMzozbTgQsjEb3q4yEILLpV0QpFxMmzfiD9K7Q3sZ8VA%2FtdITOJjtiqGGsuv13pxfBnK7EuvMN3e%2FrwGOqUB1DYA3AUxZloK8qcPZi4V04WKIsLMaPWVVQUT0gwe%2F%2BQoC8hMpLvAA9f691i61Zpl2upTwexMZLfxGeJi5k8zS71%2FV7uaVrRoqpk%2FqFCA8%2Bn8tfb1nY1E55q9dj910O6aMOsB5BZq5C60dkmeVhFC55vqa%2B3uN%2FMZoQ5y8T61zaM9KaLpFOJgigZdvaa1SRF4yfkLI0vtNxKDLL11G%2FpZYMF1DqH6&X-Amz-Signature=c0760b784f31685272ad30213a22a878a68a6d06841e88c2d5db2534293809e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRDCGXD2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTbVCoKOPfnicXZgGvBNlAf8KlImEZd%2BdJj8FIBbhXyAIgOajpQwMreQZ0%2B8LAzllNLq%2B4SemMVOufEr6YZZzx6OEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7ZdR5yU19V8Ak2HyrcA1yKDWALQHimaT9Ebc8gZAUSByzkzUWE1BSFywGMDnwoi6GVc%2BFtb5cTHPVQ20aVNij8zLBPVFl46WQ4IlictRkzeG5YDThgP01mSODu7tn4ODe9c1UJD7naGujmnLRGAVfd1fF%2B7SYQQnuQLVSRGnPovlLg3s0%2BF2hrxlMIYmqanktSF0QpFALEt0kJfkv4l6eUeDoVnLMoAIK1EUXy3fMp62exH90YeltckhkgzHEWb2zOy5Rv%2F3u6Dif%2BK%2FO32WtiuycVXlNORVHLmrD%2FFimffaIGSfLNy0qUJOpYuNwQHNyWCNH87G8fRcjny3mVKwA5i43q2B9KtksWcqHs3xCLCTeg%2BFiIJ48nJ0j3NreUYvDtxD3Hq6C2xDV81x46yPLKmTB2Ks1kZeXq30hO4VV52jd2ctAbGAJ5BYGTnp8LwrZdsn%2F9mDECOSRkAB%2FGYh34ipe1v6q8jgVJ4%2BTrbagLMoJr9%2FeQ4U3K8009BjnYGjLxn9MD6jlxf1JzmoOBR2aQVquaz8psw0Mma9z2QIW7AhF5B9yZOMPGQjWF6tMx3oOk6PdTSMzozbTgQsjEb3q4yEILLpV0QpFxMmzfiD9K7Q3sZ8VA%2FtdITOJjtiqGGsuv13pxfBnK7EuvMN3e%2FrwGOqUB1DYA3AUxZloK8qcPZi4V04WKIsLMaPWVVQUT0gwe%2F%2BQoC8hMpLvAA9f691i61Zpl2upTwexMZLfxGeJi5k8zS71%2FV7uaVrRoqpk%2FqFCA8%2Bn8tfb1nY1E55q9dj910O6aMOsB5BZq5C60dkmeVhFC55vqa%2B3uN%2FMZoQ5y8T61zaM9KaLpFOJgigZdvaa1SRF4yfkLI0vtNxKDLL11G%2FpZYMF1DqH6&X-Amz-Signature=2392e26fa9d228295fb6244dff28f55d5425e01113ae9a5d2032e92a5d4fb506&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRDCGXD2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTbVCoKOPfnicXZgGvBNlAf8KlImEZd%2BdJj8FIBbhXyAIgOajpQwMreQZ0%2B8LAzllNLq%2B4SemMVOufEr6YZZzx6OEqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7ZdR5yU19V8Ak2HyrcA1yKDWALQHimaT9Ebc8gZAUSByzkzUWE1BSFywGMDnwoi6GVc%2BFtb5cTHPVQ20aVNij8zLBPVFl46WQ4IlictRkzeG5YDThgP01mSODu7tn4ODe9c1UJD7naGujmnLRGAVfd1fF%2B7SYQQnuQLVSRGnPovlLg3s0%2BF2hrxlMIYmqanktSF0QpFALEt0kJfkv4l6eUeDoVnLMoAIK1EUXy3fMp62exH90YeltckhkgzHEWb2zOy5Rv%2F3u6Dif%2BK%2FO32WtiuycVXlNORVHLmrD%2FFimffaIGSfLNy0qUJOpYuNwQHNyWCNH87G8fRcjny3mVKwA5i43q2B9KtksWcqHs3xCLCTeg%2BFiIJ48nJ0j3NreUYvDtxD3Hq6C2xDV81x46yPLKmTB2Ks1kZeXq30hO4VV52jd2ctAbGAJ5BYGTnp8LwrZdsn%2F9mDECOSRkAB%2FGYh34ipe1v6q8jgVJ4%2BTrbagLMoJr9%2FeQ4U3K8009BjnYGjLxn9MD6jlxf1JzmoOBR2aQVquaz8psw0Mma9z2QIW7AhF5B9yZOMPGQjWF6tMx3oOk6PdTSMzozbTgQsjEb3q4yEILLpV0QpFxMmzfiD9K7Q3sZ8VA%2FtdITOJjtiqGGsuv13pxfBnK7EuvMN3e%2FrwGOqUB1DYA3AUxZloK8qcPZi4V04WKIsLMaPWVVQUT0gwe%2F%2BQoC8hMpLvAA9f691i61Zpl2upTwexMZLfxGeJi5k8zS71%2FV7uaVrRoqpk%2FqFCA8%2Bn8tfb1nY1E55q9dj910O6aMOsB5BZq5C60dkmeVhFC55vqa%2B3uN%2FMZoQ5y8T61zaM9KaLpFOJgigZdvaa1SRF4yfkLI0vtNxKDLL11G%2FpZYMF1DqH6&X-Amz-Signature=281b0efec1a9fc3db03070973497b507a111bde7aef405a0bf59062f82b9d797&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IQIPEEN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG6%2FzLdUeGcQGROJOCa4EgzKqmpnG9rg8nczMllfsZO9AiBvH3YXtlnKkDvS%2Bo5ML9y0jIV7i4wxbMDgL1%2FyyGz7XSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzJTBaa%2FYmo0BAqWJKtwD2xc9P4Ab%2F%2FBCj1dVQ5h2aK4rY91Ue9xkyjIHVN7DL4SbuOl27UNJPoWCJhEUlyrqRMQk13OxFZS5l9xI8d4xTRyo8R%2FI%2BWjBMdhnM6eg3qLBUaxpYPDGMCBjtpjguWksq8tgS%2Fh4bAyFRzhyxwOqOY1d8o9%2BsxZTOr7QaYWWvCXWoZGks7Id3cjgqG9ZKiKuaTerXEF7PAarOZY4fic47qjnM4vXzpMIMmi7j%2BukaU2zd9uB%2BTcg50M7OjlNCOMY7r8ZAVRdYfSw95S8H4jzohvAvzFpEiOKOMmNIulr9gxh0sBAZEnPX7uerDgLSsy9RCITy1sT8KzYyoBHt7AZA0xtgqe%2BuKitt%2BddNXHAm%2Fml8In9%2FW%2FoUGP0mFGkg5DjUT7UECg18j84eqgH%2BgN7pcaH%2BsqT7CT3v46K9ABhn%2Fi%2BU2py%2FT65RXo%2BuPyHGU11ElolO0FlfGmx2J7YqVUjyes2fC8RqmGSszl31f%2BP%2BziDMoJ%2BLsEqGxdw%2FJQDrHr6%2BeOpnMw%2FOO%2FZXiNvmoN6ZbySGykOqGrGEYFfRSGGMnZNllN4jTXzeY1wcqbWKhkLDsBf3bfebGdeUpOqwqIeDOIGvOe7GGD%2F2AL7R8vKQA%2B3wr8seOLCR508COIw9uH%2BvAY6pgHhPXRrDlOoEisVf4q6jNdrAZb%2FZOjKaHfALv5KYYe%2BenTksw5a2mHjatdNteiSaE7RNQFhQoRYLB5UtT9bUyx9CPgneXuIcABdStHawAUGsQzeSke9QhvYZEliYCtuh%2BY17d5%2FICW%2BMytyOTBxNY7GXSTcGGfaZrVIjKxP9zA8EdVg6YXfbmupBdxteAbLYBIO29SxFrGU7yzXAMWC%2F73MW2Ws4uxT&X-Amz-Signature=5348867d8f4397b967b027420bb8a701b944f766a7a71607adef37abba5dd00e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T73WLDRG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC4KUjiQZGHBcQR95ldf%2BvnVDSjNm5cNElhEbOynBR%2BDAiAwNy%2BHx07aCI4mB6ih3eVgeu6BTv%2BaZlN0a2%2BBmVJSZSqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMouleZOipPGOfT2qUKtwDaN%2BsMfTQkagxaN2BVY9Zbhbt4hbD6SM7EoyXUm5yZelUdgQ46Jc7EsthDGrZjMMzs8zfZB7BG%2BCWJMxCDRs%2BkVrNF7S3ddQZrvzfV3uCazkbhKCir3NOh69C72nJeEOj7AO5fdMeNUqFVzsA4fMtCzY8hsjiPWRHX3zIP%2BBPJw6NMDr1OAd6Ah1WhC5jBi7qdxO7YTLndTfmi2PwpPGrjZ83K0jRvGaDD8YPOoOmBwINCNhg48g84MxqRZuEXORqQRRD%2BqNx%2BsRV5lBYDaOIjfNqH1Cch81XWZ2Us%2FDgqmQj13ffQL1TEHQ5ZYNJZk8cWAc5rWBaBHm9qoEFEg9mFeYD0T7MQC%2FISSkKe4PGwqLYTAY%2B5ZTN1Gd8bovbwkhBcmeUdbdNjZEulwX99CPz0oDw0S5NAH7H3hwAwtUIL8C73uie5bMjJf8v1%2B%2F%2F%2BkbJHyTbBy8ysVy6jXIMtOYSKnF%2FgPQJfbkrznAN75MSj8E565Y3EIaXC3ZvP9z6iYAAEqPBXrimmHR3Jl3aZ6mdcKzR3qE6x0t%2B4DpOiH5Qah3ymrJUTgG0JMX%2FSbJ80LW%2B0gVSpdkdzZjn%2FCM3fApgsZ7uvaM1I6JGXKeuZLMiyQqZ02BMZWndunZhPkkw0Nb%2BvAY6pgGGQA0v4y0qkyp3LCKXYCxE3bJnV79V5XeUihN9Pmj2np3YWGYPsSag4JzvhkHBPtPppBwckVdO1T1xBc9EIoIJDXm28Z6VZrVygzQPtGfQx0wywJ0X76bnLNeWrEzJTXaZwzHvt%2FNcFHXqAQr0jHZV7iKvxYsVoSFqwMJKaxa2ZMVpaWg8o0J1b6SwZvzFM9F0alxMy1ZqMtMKF%2FiqIWJ9JcVBoTmd&X-Amz-Signature=e326a278492a19c053727db0b2d5a43441bdc0af7785be2956da5f545b8d1080&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Y5YQZKR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICGKcyF4nu3qyw%2BQlF3Aqd68S6lr%2BY%2B1mO%2FhLiRnijfSAiEAx6f88HY6dgpK4gJg9lPBzIiWZYtdbx9Icvb7FTh3qY0qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOGaQ9jfMWN5gcrrWCrcA3sUlpcvfAXzs8T1RrxzePRh9SAUuMhqU%2FZO63lBFDCP%2BRYRA0idWxZ5WrCDdNMznItEWllMoaLcOnZ7gIHW%2FIgSJHEuepVVu%2BZUAehNDLMFGVrAkV9Rb0OyRSaj6Z55K0P0HK1PRmKP8I%2F5Aq40v0Y8XeFpmBWRGB3YryZ74V5zKaQqda6WqZ0jc14PLo%2BDIZxboE9YHG4hlhdrkHZ29h9kLMGPm32vQF1N4CXIcUzIMiC7aFXnUPE8ZifcWiL0PcqmZFa2js6713mUFqQlo8WvOZiJmYUvuUji1jN7AUUcoAE7aUTIJTG8bzNTdlCWJ3zV5jhI6b2gPGpOc%2BC%2FGWPUato%2BYdATPhs7Rrf5Dz6nayX9oNXUdeNy0FA4fO6xraEYCVvrfSxZLKyLMgjzaxSGLVKcc8pogw2xsHmfDbNM0fA181KooraF9VHh9LHT%2Bsa3AU3n%2BGqCXSrQ6n%2Bp1TXGS9mF%2FdE0FU8v9BFkKIRsR5ERjyvKXylxyScS49GMo%2Fe3C6vJRIVa4UZt8Mug6Tmz3uMFr7J%2BlEabqqmdFHWc1f63hvt83Y13MlzJt7K4DYN3TijFeaxaVUdkKv03%2F4YlEgw668%2BYzPhytQHbwVMWVM%2F3FSmMMMzwAd9eMJzf%2FrwGOqUB669ywL%2BJsM8pf13CPCH2y7eQKF9Ze%2Bs0GVPA2NnVhoSbAMByJIdhmCwesy0qT3uZzv%2FwIUlarX8yS7IvsZiQmJRdoUnlKKWZ5SSWmy5Idi49gkRcPiUdinbJ7TpLJLUrDuyCFVDd1l5kaNiaPXvG1aPwMZ5H4KrrQpd5O3WIBO3I0eOxZcNqirHnP5P6xOCbIupkyFapiKaaoR8yQ94vxYzSkXBQ&X-Amz-Signature=31c8c840bae5cdc07ad993cb39660fb5ffd419aebbfde86d0f533efeea716656&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Y5YQZKR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICGKcyF4nu3qyw%2BQlF3Aqd68S6lr%2BY%2B1mO%2FhLiRnijfSAiEAx6f88HY6dgpK4gJg9lPBzIiWZYtdbx9Icvb7FTh3qY0qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOGaQ9jfMWN5gcrrWCrcA3sUlpcvfAXzs8T1RrxzePRh9SAUuMhqU%2FZO63lBFDCP%2BRYRA0idWxZ5WrCDdNMznItEWllMoaLcOnZ7gIHW%2FIgSJHEuepVVu%2BZUAehNDLMFGVrAkV9Rb0OyRSaj6Z55K0P0HK1PRmKP8I%2F5Aq40v0Y8XeFpmBWRGB3YryZ74V5zKaQqda6WqZ0jc14PLo%2BDIZxboE9YHG4hlhdrkHZ29h9kLMGPm32vQF1N4CXIcUzIMiC7aFXnUPE8ZifcWiL0PcqmZFa2js6713mUFqQlo8WvOZiJmYUvuUji1jN7AUUcoAE7aUTIJTG8bzNTdlCWJ3zV5jhI6b2gPGpOc%2BC%2FGWPUato%2BYdATPhs7Rrf5Dz6nayX9oNXUdeNy0FA4fO6xraEYCVvrfSxZLKyLMgjzaxSGLVKcc8pogw2xsHmfDbNM0fA181KooraF9VHh9LHT%2Bsa3AU3n%2BGqCXSrQ6n%2Bp1TXGS9mF%2FdE0FU8v9BFkKIRsR5ERjyvKXylxyScS49GMo%2Fe3C6vJRIVa4UZt8Mug6Tmz3uMFr7J%2BlEabqqmdFHWc1f63hvt83Y13MlzJt7K4DYN3TijFeaxaVUdkKv03%2F4YlEgw668%2BYzPhytQHbwVMWVM%2F3FSmMMMzwAd9eMJzf%2FrwGOqUB669ywL%2BJsM8pf13CPCH2y7eQKF9Ze%2Bs0GVPA2NnVhoSbAMByJIdhmCwesy0qT3uZzv%2FwIUlarX8yS7IvsZiQmJRdoUnlKKWZ5SSWmy5Idi49gkRcPiUdinbJ7TpLJLUrDuyCFVDd1l5kaNiaPXvG1aPwMZ5H4KrrQpd5O3WIBO3I0eOxZcNqirHnP5P6xOCbIupkyFapiKaaoR8yQ94vxYzSkXBQ&X-Amz-Signature=a4389f7b28da78a3ca8ab01a66791d86fa265e280a31de39f361f77095a073f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
