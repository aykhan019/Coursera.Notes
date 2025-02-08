

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4WXWKN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDYrWh%2BbbafGguGQvynBM8KuCqCtlJtd6jcZyQxVyGTJgIhAMH1XGhqFdbqHJ0j3npheLkHfi0Codr%2FF2g0PDXgfmtzKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz4fp4ueqwGQOJa2XYq3AM2dz60MBRIKIwnddCu%2BRwtheNGy5NH1i5wsRk0rMToBMw8ex9ui95AJiMyRQ%2BpfXcYFn5WwUKZ4tqAzD52JajQ%2FkWqGgrQmw%2BRGFYVgMKwS9eX3RgcRzaTDF1dunhb2S0Unuoy4vUopF%2FmywBj6YF3lNhwrIUQ0hYZhlKhEGZS03Ux%2FSVAluiA%2BGxN1JpCTonordf55LmgZtyygFh6OlM3qSEF2u96aeF99Nwu7wiRw7%2BEs30xaNINMYUb5261MHRbGRXcNiTlW9SaWdADIgbKYCPS3gzCntGKO9dYPORASK8BxuVceoIoirxRTpyn8EP%2BOx2zaOXO3qwdLRDkBOCRqnRK%2Btv8i3a2GwB6YdjbYdWX8OQJ6XchVppMEtR23OONHxB6rCaP8GJSVyKvBAeJyVnnFgrON5HTB7QT2T1tioXTepBPciAk3PHzXFNKy8fAAlirh8MxY96agvVBeoWUsJMe%2FTm0kd%2FebOJIQEVO%2BaPRRsN%2Bmn4uyVTW0cHX1oLT4YOvI0g4oFDtdfaBksZAv83Gf3rXEVI%2BTzXDLr1dGo8dAD7SzcU7xV2wrmK9mmbXAr%2FukCTSKg4nCWrMWxNK2UrgblM0XrwCMSw8MbdFPBkdh2CNzNJcs8XAlTC8hZ29BjqkAWnguuBW7YXdTrCPXplr%2BQa5MjixTlqs39r%2BKbbDKd3gbnlR8rJamkri3emgIroXTK33c6pyu5MjfFR8bTJJZzKmnq%2Fxu3Ci%2FoeCLrqfwJssZ4Ru3tmrcZAvNsq6o9ZHNWKIvxreCyNWkexEEzAz%2FIIEs%2BIRtRbpe%2FNyNfGUAtjSOZOO7oyT2e4BCChNC%2BbNDYDKmWrcZ%2FMrVwTv42h2lwpm3kaK&X-Amz-Signature=b7a440b6a9039d152fc033dea2a7e8b2d055ccac760b145f89663ff6b51aa15d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4WXWKN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDYrWh%2BbbafGguGQvynBM8KuCqCtlJtd6jcZyQxVyGTJgIhAMH1XGhqFdbqHJ0j3npheLkHfi0Codr%2FF2g0PDXgfmtzKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz4fp4ueqwGQOJa2XYq3AM2dz60MBRIKIwnddCu%2BRwtheNGy5NH1i5wsRk0rMToBMw8ex9ui95AJiMyRQ%2BpfXcYFn5WwUKZ4tqAzD52JajQ%2FkWqGgrQmw%2BRGFYVgMKwS9eX3RgcRzaTDF1dunhb2S0Unuoy4vUopF%2FmywBj6YF3lNhwrIUQ0hYZhlKhEGZS03Ux%2FSVAluiA%2BGxN1JpCTonordf55LmgZtyygFh6OlM3qSEF2u96aeF99Nwu7wiRw7%2BEs30xaNINMYUb5261MHRbGRXcNiTlW9SaWdADIgbKYCPS3gzCntGKO9dYPORASK8BxuVceoIoirxRTpyn8EP%2BOx2zaOXO3qwdLRDkBOCRqnRK%2Btv8i3a2GwB6YdjbYdWX8OQJ6XchVppMEtR23OONHxB6rCaP8GJSVyKvBAeJyVnnFgrON5HTB7QT2T1tioXTepBPciAk3PHzXFNKy8fAAlirh8MxY96agvVBeoWUsJMe%2FTm0kd%2FebOJIQEVO%2BaPRRsN%2Bmn4uyVTW0cHX1oLT4YOvI0g4oFDtdfaBksZAv83Gf3rXEVI%2BTzXDLr1dGo8dAD7SzcU7xV2wrmK9mmbXAr%2FukCTSKg4nCWrMWxNK2UrgblM0XrwCMSw8MbdFPBkdh2CNzNJcs8XAlTC8hZ29BjqkAWnguuBW7YXdTrCPXplr%2BQa5MjixTlqs39r%2BKbbDKd3gbnlR8rJamkri3emgIroXTK33c6pyu5MjfFR8bTJJZzKmnq%2Fxu3Ci%2FoeCLrqfwJssZ4Ru3tmrcZAvNsq6o9ZHNWKIvxreCyNWkexEEzAz%2FIIEs%2BIRtRbpe%2FNyNfGUAtjSOZOO7oyT2e4BCChNC%2BbNDYDKmWrcZ%2FMrVwTv42h2lwpm3kaK&X-Amz-Signature=83417c4c19c39bbf0d507d9d776804c76f0495d5f8d2386455b5354a5a534a6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4WXWKN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDYrWh%2BbbafGguGQvynBM8KuCqCtlJtd6jcZyQxVyGTJgIhAMH1XGhqFdbqHJ0j3npheLkHfi0Codr%2FF2g0PDXgfmtzKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz4fp4ueqwGQOJa2XYq3AM2dz60MBRIKIwnddCu%2BRwtheNGy5NH1i5wsRk0rMToBMw8ex9ui95AJiMyRQ%2BpfXcYFn5WwUKZ4tqAzD52JajQ%2FkWqGgrQmw%2BRGFYVgMKwS9eX3RgcRzaTDF1dunhb2S0Unuoy4vUopF%2FmywBj6YF3lNhwrIUQ0hYZhlKhEGZS03Ux%2FSVAluiA%2BGxN1JpCTonordf55LmgZtyygFh6OlM3qSEF2u96aeF99Nwu7wiRw7%2BEs30xaNINMYUb5261MHRbGRXcNiTlW9SaWdADIgbKYCPS3gzCntGKO9dYPORASK8BxuVceoIoirxRTpyn8EP%2BOx2zaOXO3qwdLRDkBOCRqnRK%2Btv8i3a2GwB6YdjbYdWX8OQJ6XchVppMEtR23OONHxB6rCaP8GJSVyKvBAeJyVnnFgrON5HTB7QT2T1tioXTepBPciAk3PHzXFNKy8fAAlirh8MxY96agvVBeoWUsJMe%2FTm0kd%2FebOJIQEVO%2BaPRRsN%2Bmn4uyVTW0cHX1oLT4YOvI0g4oFDtdfaBksZAv83Gf3rXEVI%2BTzXDLr1dGo8dAD7SzcU7xV2wrmK9mmbXAr%2FukCTSKg4nCWrMWxNK2UrgblM0XrwCMSw8MbdFPBkdh2CNzNJcs8XAlTC8hZ29BjqkAWnguuBW7YXdTrCPXplr%2BQa5MjixTlqs39r%2BKbbDKd3gbnlR8rJamkri3emgIroXTK33c6pyu5MjfFR8bTJJZzKmnq%2Fxu3Ci%2FoeCLrqfwJssZ4Ru3tmrcZAvNsq6o9ZHNWKIvxreCyNWkexEEzAz%2FIIEs%2BIRtRbpe%2FNyNfGUAtjSOZOO7oyT2e4BCChNC%2BbNDYDKmWrcZ%2FMrVwTv42h2lwpm3kaK&X-Amz-Signature=90b7bed49e09210864f9e5985aa0741de69f53b81e0f3ae2164f0844fb0e135a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4WXWKN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDYrWh%2BbbafGguGQvynBM8KuCqCtlJtd6jcZyQxVyGTJgIhAMH1XGhqFdbqHJ0j3npheLkHfi0Codr%2FF2g0PDXgfmtzKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz4fp4ueqwGQOJa2XYq3AM2dz60MBRIKIwnddCu%2BRwtheNGy5NH1i5wsRk0rMToBMw8ex9ui95AJiMyRQ%2BpfXcYFn5WwUKZ4tqAzD52JajQ%2FkWqGgrQmw%2BRGFYVgMKwS9eX3RgcRzaTDF1dunhb2S0Unuoy4vUopF%2FmywBj6YF3lNhwrIUQ0hYZhlKhEGZS03Ux%2FSVAluiA%2BGxN1JpCTonordf55LmgZtyygFh6OlM3qSEF2u96aeF99Nwu7wiRw7%2BEs30xaNINMYUb5261MHRbGRXcNiTlW9SaWdADIgbKYCPS3gzCntGKO9dYPORASK8BxuVceoIoirxRTpyn8EP%2BOx2zaOXO3qwdLRDkBOCRqnRK%2Btv8i3a2GwB6YdjbYdWX8OQJ6XchVppMEtR23OONHxB6rCaP8GJSVyKvBAeJyVnnFgrON5HTB7QT2T1tioXTepBPciAk3PHzXFNKy8fAAlirh8MxY96agvVBeoWUsJMe%2FTm0kd%2FebOJIQEVO%2BaPRRsN%2Bmn4uyVTW0cHX1oLT4YOvI0g4oFDtdfaBksZAv83Gf3rXEVI%2BTzXDLr1dGo8dAD7SzcU7xV2wrmK9mmbXAr%2FukCTSKg4nCWrMWxNK2UrgblM0XrwCMSw8MbdFPBkdh2CNzNJcs8XAlTC8hZ29BjqkAWnguuBW7YXdTrCPXplr%2BQa5MjixTlqs39r%2BKbbDKd3gbnlR8rJamkri3emgIroXTK33c6pyu5MjfFR8bTJJZzKmnq%2Fxu3Ci%2FoeCLrqfwJssZ4Ru3tmrcZAvNsq6o9ZHNWKIvxreCyNWkexEEzAz%2FIIEs%2BIRtRbpe%2FNyNfGUAtjSOZOO7oyT2e4BCChNC%2BbNDYDKmWrcZ%2FMrVwTv42h2lwpm3kaK&X-Amz-Signature=b843866183a1ff3e38acb0a073a270a969e47dabb722e1f040e4b252a10c2531&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4WXWKN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDYrWh%2BbbafGguGQvynBM8KuCqCtlJtd6jcZyQxVyGTJgIhAMH1XGhqFdbqHJ0j3npheLkHfi0Codr%2FF2g0PDXgfmtzKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz4fp4ueqwGQOJa2XYq3AM2dz60MBRIKIwnddCu%2BRwtheNGy5NH1i5wsRk0rMToBMw8ex9ui95AJiMyRQ%2BpfXcYFn5WwUKZ4tqAzD52JajQ%2FkWqGgrQmw%2BRGFYVgMKwS9eX3RgcRzaTDF1dunhb2S0Unuoy4vUopF%2FmywBj6YF3lNhwrIUQ0hYZhlKhEGZS03Ux%2FSVAluiA%2BGxN1JpCTonordf55LmgZtyygFh6OlM3qSEF2u96aeF99Nwu7wiRw7%2BEs30xaNINMYUb5261MHRbGRXcNiTlW9SaWdADIgbKYCPS3gzCntGKO9dYPORASK8BxuVceoIoirxRTpyn8EP%2BOx2zaOXO3qwdLRDkBOCRqnRK%2Btv8i3a2GwB6YdjbYdWX8OQJ6XchVppMEtR23OONHxB6rCaP8GJSVyKvBAeJyVnnFgrON5HTB7QT2T1tioXTepBPciAk3PHzXFNKy8fAAlirh8MxY96agvVBeoWUsJMe%2FTm0kd%2FebOJIQEVO%2BaPRRsN%2Bmn4uyVTW0cHX1oLT4YOvI0g4oFDtdfaBksZAv83Gf3rXEVI%2BTzXDLr1dGo8dAD7SzcU7xV2wrmK9mmbXAr%2FukCTSKg4nCWrMWxNK2UrgblM0XrwCMSw8MbdFPBkdh2CNzNJcs8XAlTC8hZ29BjqkAWnguuBW7YXdTrCPXplr%2BQa5MjixTlqs39r%2BKbbDKd3gbnlR8rJamkri3emgIroXTK33c6pyu5MjfFR8bTJJZzKmnq%2Fxu3Ci%2FoeCLrqfwJssZ4Ru3tmrcZAvNsq6o9ZHNWKIvxreCyNWkexEEzAz%2FIIEs%2BIRtRbpe%2FNyNfGUAtjSOZOO7oyT2e4BCChNC%2BbNDYDKmWrcZ%2FMrVwTv42h2lwpm3kaK&X-Amz-Signature=2db5a729fdd3ab07ea178be57859ee0af2362816169c297f1215c707a840e343&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4WXWKN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDYrWh%2BbbafGguGQvynBM8KuCqCtlJtd6jcZyQxVyGTJgIhAMH1XGhqFdbqHJ0j3npheLkHfi0Codr%2FF2g0PDXgfmtzKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz4fp4ueqwGQOJa2XYq3AM2dz60MBRIKIwnddCu%2BRwtheNGy5NH1i5wsRk0rMToBMw8ex9ui95AJiMyRQ%2BpfXcYFn5WwUKZ4tqAzD52JajQ%2FkWqGgrQmw%2BRGFYVgMKwS9eX3RgcRzaTDF1dunhb2S0Unuoy4vUopF%2FmywBj6YF3lNhwrIUQ0hYZhlKhEGZS03Ux%2FSVAluiA%2BGxN1JpCTonordf55LmgZtyygFh6OlM3qSEF2u96aeF99Nwu7wiRw7%2BEs30xaNINMYUb5261MHRbGRXcNiTlW9SaWdADIgbKYCPS3gzCntGKO9dYPORASK8BxuVceoIoirxRTpyn8EP%2BOx2zaOXO3qwdLRDkBOCRqnRK%2Btv8i3a2GwB6YdjbYdWX8OQJ6XchVppMEtR23OONHxB6rCaP8GJSVyKvBAeJyVnnFgrON5HTB7QT2T1tioXTepBPciAk3PHzXFNKy8fAAlirh8MxY96agvVBeoWUsJMe%2FTm0kd%2FebOJIQEVO%2BaPRRsN%2Bmn4uyVTW0cHX1oLT4YOvI0g4oFDtdfaBksZAv83Gf3rXEVI%2BTzXDLr1dGo8dAD7SzcU7xV2wrmK9mmbXAr%2FukCTSKg4nCWrMWxNK2UrgblM0XrwCMSw8MbdFPBkdh2CNzNJcs8XAlTC8hZ29BjqkAWnguuBW7YXdTrCPXplr%2BQa5MjixTlqs39r%2BKbbDKd3gbnlR8rJamkri3emgIroXTK33c6pyu5MjfFR8bTJJZzKmnq%2Fxu3Ci%2FoeCLrqfwJssZ4Ru3tmrcZAvNsq6o9ZHNWKIvxreCyNWkexEEzAz%2FIIEs%2BIRtRbpe%2FNyNfGUAtjSOZOO7oyT2e4BCChNC%2BbNDYDKmWrcZ%2FMrVwTv42h2lwpm3kaK&X-Amz-Signature=7b26007ac8241116bf7d86fc479aa5e54ab52f16cd9cdb8ed3f1d756fe03e0c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4WXWKN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDYrWh%2BbbafGguGQvynBM8KuCqCtlJtd6jcZyQxVyGTJgIhAMH1XGhqFdbqHJ0j3npheLkHfi0Codr%2FF2g0PDXgfmtzKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz4fp4ueqwGQOJa2XYq3AM2dz60MBRIKIwnddCu%2BRwtheNGy5NH1i5wsRk0rMToBMw8ex9ui95AJiMyRQ%2BpfXcYFn5WwUKZ4tqAzD52JajQ%2FkWqGgrQmw%2BRGFYVgMKwS9eX3RgcRzaTDF1dunhb2S0Unuoy4vUopF%2FmywBj6YF3lNhwrIUQ0hYZhlKhEGZS03Ux%2FSVAluiA%2BGxN1JpCTonordf55LmgZtyygFh6OlM3qSEF2u96aeF99Nwu7wiRw7%2BEs30xaNINMYUb5261MHRbGRXcNiTlW9SaWdADIgbKYCPS3gzCntGKO9dYPORASK8BxuVceoIoirxRTpyn8EP%2BOx2zaOXO3qwdLRDkBOCRqnRK%2Btv8i3a2GwB6YdjbYdWX8OQJ6XchVppMEtR23OONHxB6rCaP8GJSVyKvBAeJyVnnFgrON5HTB7QT2T1tioXTepBPciAk3PHzXFNKy8fAAlirh8MxY96agvVBeoWUsJMe%2FTm0kd%2FebOJIQEVO%2BaPRRsN%2Bmn4uyVTW0cHX1oLT4YOvI0g4oFDtdfaBksZAv83Gf3rXEVI%2BTzXDLr1dGo8dAD7SzcU7xV2wrmK9mmbXAr%2FukCTSKg4nCWrMWxNK2UrgblM0XrwCMSw8MbdFPBkdh2CNzNJcs8XAlTC8hZ29BjqkAWnguuBW7YXdTrCPXplr%2BQa5MjixTlqs39r%2BKbbDKd3gbnlR8rJamkri3emgIroXTK33c6pyu5MjfFR8bTJJZzKmnq%2Fxu3Ci%2FoeCLrqfwJssZ4Ru3tmrcZAvNsq6o9ZHNWKIvxreCyNWkexEEzAz%2FIIEs%2BIRtRbpe%2FNyNfGUAtjSOZOO7oyT2e4BCChNC%2BbNDYDKmWrcZ%2FMrVwTv42h2lwpm3kaK&X-Amz-Signature=d575a9befca89aa3697701656520992a8d408e801d3ad021fd57401e4be0d3a3&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4WXWKN7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDYrWh%2BbbafGguGQvynBM8KuCqCtlJtd6jcZyQxVyGTJgIhAMH1XGhqFdbqHJ0j3npheLkHfi0Codr%2FF2g0PDXgfmtzKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz4fp4ueqwGQOJa2XYq3AM2dz60MBRIKIwnddCu%2BRwtheNGy5NH1i5wsRk0rMToBMw8ex9ui95AJiMyRQ%2BpfXcYFn5WwUKZ4tqAzD52JajQ%2FkWqGgrQmw%2BRGFYVgMKwS9eX3RgcRzaTDF1dunhb2S0Unuoy4vUopF%2FmywBj6YF3lNhwrIUQ0hYZhlKhEGZS03Ux%2FSVAluiA%2BGxN1JpCTonordf55LmgZtyygFh6OlM3qSEF2u96aeF99Nwu7wiRw7%2BEs30xaNINMYUb5261MHRbGRXcNiTlW9SaWdADIgbKYCPS3gzCntGKO9dYPORASK8BxuVceoIoirxRTpyn8EP%2BOx2zaOXO3qwdLRDkBOCRqnRK%2Btv8i3a2GwB6YdjbYdWX8OQJ6XchVppMEtR23OONHxB6rCaP8GJSVyKvBAeJyVnnFgrON5HTB7QT2T1tioXTepBPciAk3PHzXFNKy8fAAlirh8MxY96agvVBeoWUsJMe%2FTm0kd%2FebOJIQEVO%2BaPRRsN%2Bmn4uyVTW0cHX1oLT4YOvI0g4oFDtdfaBksZAv83Gf3rXEVI%2BTzXDLr1dGo8dAD7SzcU7xV2wrmK9mmbXAr%2FukCTSKg4nCWrMWxNK2UrgblM0XrwCMSw8MbdFPBkdh2CNzNJcs8XAlTC8hZ29BjqkAWnguuBW7YXdTrCPXplr%2BQa5MjixTlqs39r%2BKbbDKd3gbnlR8rJamkri3emgIroXTK33c6pyu5MjfFR8bTJJZzKmnq%2Fxu3Ci%2FoeCLrqfwJssZ4Ru3tmrcZAvNsq6o9ZHNWKIvxreCyNWkexEEzAz%2FIIEs%2BIRtRbpe%2FNyNfGUAtjSOZOO7oyT2e4BCChNC%2BbNDYDKmWrcZ%2FMrVwTv42h2lwpm3kaK&X-Amz-Signature=ddf52051a933baf6bfe2bfb5095d98c52190e002cf0d326cb5dcf0f2a6469491&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VH3TXCZA%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCojoKf5bUVuHYzVKz8KGToJ%2F6lMQZ3U2zYqyrneCUsdgIgVAESaG873MMpZiPlmH3k9iSdYxBbr9aS7dv4ei104h0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPLRSJX86pHsxHPgxircA1hVFtEzIWZz9WjtYwTnOuTAxwe1q7XzMcvCZt8Z03bMZ9kw96%2Fv5qGM%2BStVYo1DdFQOwVuSg3Bzg4ba9AyMYINP9N%2FUPcZOQ5Woho%2BmxvugV%2F%2F8r7jl5wdf2eOYJAujlpiW59vUP3%2FnKps1MzFRDQmwz7iyZqqU0HV0sfJYoGIcu4BmPaYfgSxqk6onHlaDjYb26wKNlJ68wiBAGCmo2Vrffj4wRV3ZQpQBeVbylz18if5PPz2T8HKj4%2BLaP9cej6TeNOETJcvNUmGD1A19tGh0mDWKQmfwCpcoaflibrMopUvCSBqKzJnj6xSGZ2086P4T5n0PUeX0cS2xOnq74w05BxB61PA%2FzwxWZCWR3Kbw1IpOjpbfbw0xUFKMz5BDq%2FQsVNf8OLDHam9xIIcuFBryeTyBG12iJ7iZrJWx8VwDN5HYvqVR7r9orzKU0M%2FanPpI0k4ixMdz1Q%2FTQvjk%2B%2FFH8lXWV8H%2FQlemztnNOCu2bKnk8w1IMyl9%2FXngavR7AywhBmr%2FQg92hoEf6cjk2UYVu%2FST1N9CCucOw7OGbj3NkkZj9MhfsahPn83u22bwW%2FUlOZ6hUu1c2Jr%2BHvlE9AiDtDyj6CV%2FIB0UfhG9IzEF0l%2BKT4VCuZAPCaESMKmFnb0GOqUBwRDpfl6mlK10RpYiy%2FSoH0%2FXJZtpP58678DM6EqtGnVXpriHVxfougHsYFV%2BmBGyqicUzdiIuaiQliyzTTM8QK2UtFhSxWyDiWnaOU9wA2n0uZe13e%2B%2BqZmpwaYUVxQKMrKWmjjG4EVzUrBm1Hgwty0YLRHBfBCI%2FcklAW5R3aBIcRLyNClqLpM82MiD4VU7PY1t5%2F6oXYIbt5boH33OESFDTyLK&X-Amz-Signature=16150d60f9a9420f129b3b87d898b17a85a74c3dfe9bf4cf97448345b111d810&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OCWSBFL%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDFgHIvJR30VzWib1eZwV%2Fw959yuTygAZC%2BYyRBJrd3wAiEA2l3rG2li0ofL8BW%2FPlBJsARMrj2HPsxs1G%2BNe2U6QNEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG2gKJ6gc%2Fp0LNS%2ByrcA%2BQ4YnnQS2uKh9hUvzpgt0tC1627BOxQZsgM5Y5eQXyqLQmjnUWXoCv2rlW%2BlXvtMMktd%2F3ecmKGQWJKJV5qm0S73X2bMWBEPwF1vqTVfIxmmCvxwUlVku0%2BYgP4qNWp3a7NxK3PfG3rD%2FQ%2B2ZYEaSsZU6Y5t85XyAkIaCYHHM2skcb3eq%2FBMgzM02udtFYb%2Fb4grqobjkP532vzpD9uT7U5f%2FOEgkYA5Kq7to%2BPpZaGU%2F%2BVuYGomfnm9pSmXD%2BzTrqHP7D9tYs1NWtS3UAVSPjquQAvVax0VEWTQsRlyC5toCmt2u6V%2FMhiGPpofdQKCKIC0%2FU3%2Fai2CDXFAXekL%2BASnZyNAeB2ANKX2FJlvZJd4RAtZlARvJ9E0Psho5fTsjTcnKIbnpFgo525Z7Hz0iQlFzgGWo4e3Y%2B%2FwttDe2Smgf6vI5Ztd0tQGI7%2F2qmd52gtV66oelamDRrmm%2F7OZPsjFeff9n6S7rW0TQdPpAVXmUsvUq0jerwWuNoIfV5mnLxpCHrfdn1C2dqLhbwo3YIlqvRXx27B03bHwVPXxS%2Bn4Iie3%2BFIjQ3Vqb1AyWZo5ydGfaWAD%2FLfX0hvZhOVNQ1yG3Cb6ZZr02Nyta0iqoTNSv%2FKBW2fnSo1rt1nMKqFnb0GOqUB3OugnYT4XkSQUf8IFu3ky2vTnO3tt7PW3FYgVuBGTx2GMvx0jFW5Two3G11%2FG0b6qMZjnjk6GfML9M0abx62cwzi%2FDa6%2FX5Hb9phy9D0FqdNsXpzLmShBadwl%2FF29UhnkW5iHOsdtTiP1GemQaH0JbJ8cRlG9E7hdiKv4egQiVMoPoxUOmqCsE%2F4PYvfIe%2F8Rz8NX1sPsD2rCzY6dWm%2BpLz9vgY%2B&X-Amz-Signature=7b9bae3dac82f80dc9f13ab4a1764a6c25003fdf26fd348c67d33585fe983968&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEQVCPGN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFAgmv19va9sWNwPu3xltpNLtml7PRV5kerROV3O4NqxAiAYLtyGMX2yhDkm0aXt3q9kdb1xWyiVtRVaHyEVm%2BtdnCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe%2B6Xq6zcsNRunzpcKtwDLfLpP7mFQJ3vlaKyTBqt8%2BsZPYimAu%2Fe5f9I7RivqiK%2FPDqAT%2BWIz7gVrzYke1SYmjuqQfvN%2BDtKv0%2Ba0nBpcS61TMT1Y5D6hIO44gBhRCFPrWYK78ofTVvRPoj2rJYvTTxBb6hHmAX9KivszlqEBVBivvQXpaIIyAuwQBfljNHYK8fBKPMEMJtcnnW3RW1IAOH7gTym0VCdFsUGww%2BOQMRV1zXromZ%2B2p3vZ%2FB2Bo0eFXBAisy%2F26NYFbv5QdnY%2FKPsUgvc9fWEorxahJiF09Cqka45FzSEUdhE00o1F6kXY4DaK2gfXBd1TYntU89axdOS%2FHOacFnDkvRkkkL9H6g2R2nUCvt8tCFLZMkJLxaos%2Bvd3GbOamBSQfuok3b9JTIfw6xSRQONgqNyGEnPy%2Bl63779s3XxcM7fyHnhp23wahetqGpk%2Ftr2XfT0NKWsPcC4aK7dpQoUzhnhpW7gR2xyq6Cfm7KjXdsFz8%2Fmezi3lTce6xD1%2BFqUw%2FjVDwP3caX%2Ff5xY2TS92BLRJEnR5YLVOhQ0YLFojOg2cWGGxlRCieuU%2FQSs7o9b9Wu34FNztJ9uz27ty%2BZcN3euhG%2F9nnOK%2BrWYPfhcU0yZDGjqrBEaTcS9nsmo%2Bh4M%2B6UwoIWdvQY6pgEGxORWKxytMVEVUYZ8vhxi7SKWKlXrJR32pds6%2FY1Vwc5pHvcfNStFy6QGq132FYMMCZQVZdwEE4%2BLK0wV0fpL8hlso5cxFcdYsNJXw3u3zvPs1HI7cxUEmNe9tHBGxNIqZSx4aDXVm6qX7AP%2F1%2FfcJvQUE6K26Kll2fGmHukn4xK0pqr3xxJFEuuGJ8cKkJ%2FLAhZT9e6MBy1Q%2BOwceVVti%2FUNxA1O&X-Amz-Signature=2f6ff574ada0ae37516602b03f643d3962c94a23a811e2bfb269142977b420ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEQVCPGN%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFAgmv19va9sWNwPu3xltpNLtml7PRV5kerROV3O4NqxAiAYLtyGMX2yhDkm0aXt3q9kdb1xWyiVtRVaHyEVm%2BtdnCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe%2B6Xq6zcsNRunzpcKtwDLfLpP7mFQJ3vlaKyTBqt8%2BsZPYimAu%2Fe5f9I7RivqiK%2FPDqAT%2BWIz7gVrzYke1SYmjuqQfvN%2BDtKv0%2Ba0nBpcS61TMT1Y5D6hIO44gBhRCFPrWYK78ofTVvRPoj2rJYvTTxBb6hHmAX9KivszlqEBVBivvQXpaIIyAuwQBfljNHYK8fBKPMEMJtcnnW3RW1IAOH7gTym0VCdFsUGww%2BOQMRV1zXromZ%2B2p3vZ%2FB2Bo0eFXBAisy%2F26NYFbv5QdnY%2FKPsUgvc9fWEorxahJiF09Cqka45FzSEUdhE00o1F6kXY4DaK2gfXBd1TYntU89axdOS%2FHOacFnDkvRkkkL9H6g2R2nUCvt8tCFLZMkJLxaos%2Bvd3GbOamBSQfuok3b9JTIfw6xSRQONgqNyGEnPy%2Bl63779s3XxcM7fyHnhp23wahetqGpk%2Ftr2XfT0NKWsPcC4aK7dpQoUzhnhpW7gR2xyq6Cfm7KjXdsFz8%2Fmezi3lTce6xD1%2BFqUw%2FjVDwP3caX%2Ff5xY2TS92BLRJEnR5YLVOhQ0YLFojOg2cWGGxlRCieuU%2FQSs7o9b9Wu34FNztJ9uz27ty%2BZcN3euhG%2F9nnOK%2BrWYPfhcU0yZDGjqrBEaTcS9nsmo%2Bh4M%2B6UwoIWdvQY6pgEGxORWKxytMVEVUYZ8vhxi7SKWKlXrJR32pds6%2FY1Vwc5pHvcfNStFy6QGq132FYMMCZQVZdwEE4%2BLK0wV0fpL8hlso5cxFcdYsNJXw3u3zvPs1HI7cxUEmNe9tHBGxNIqZSx4aDXVm6qX7AP%2F1%2FfcJvQUE6K26Kll2fGmHukn4xK0pqr3xxJFEuuGJ8cKkJ%2FLAhZT9e6MBy1Q%2BOwceVVti%2FUNxA1O&X-Amz-Signature=0de8b8f0717c74a0476138bb0cb4d8e532a40eaadc2ac7400156e2395a40abd8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
