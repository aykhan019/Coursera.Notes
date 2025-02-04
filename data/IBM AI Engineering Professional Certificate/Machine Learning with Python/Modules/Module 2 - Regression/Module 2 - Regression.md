

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XIZZGBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDWm50vIJnk6wo%2BT3uWRq0JdmZyZTrvBkRy606amfSqaAIhAMUQebxyVNb0KnwGQnshSloMYzm15rwlw8wXugJwYftpKv8DCCYQABoMNjM3NDIzMTgzODA1IgwgEs2e3WPM8V7R4G4q3AN10KNujVWH3TWGjMqGz%2FUvA4JJj32O3jKImv7JMjiQjF6Rp9fRohoctcXbgJLE38CnRzOvxS5b3EJ2zg1c9suxfLI4JYQMw8DgTQ5bBZfbiEPeiKutzx96Jv3AN2McPOMBfnL0uAyCvBlINwUuXQ6JhPZUvOlY4wQFKztr7nycwXAWBP9CeMX0yRfupWSptu8VgJzjlTIwUtjrI30piFYc6oEFBB7iFX%2FIS%2B450RutJ2GweBYnhzWowuvxV005%2FCEMAF4trQto60E2aoMuZjH6iuEHXb%2Fw84ti%2Bf9cjKo1dPKpDQOPFnZ6UzfJWcElF2Ue%2BDwQ7SFe65VL%2BhpBqyZjLr4YvETZUuoGoXQr9D%2BsaanKSj5RcoeSWOWqzeKxcJ%2BAmOH4OFlM7w3A6REoabW9R4PVJorcq6EM70OfxoBgvX0vfQ%2FUVamJC3VpbrAVuBwVlBsE9l%2FXuejR1VoED%2F6MrW5xonVkoWQQs1O%2BeCD1dcqrwK1VmTIkbh7cy88xhH5axOGEEfU5NIirCdhhyHPxw8wYZ2fiQ3Vw7MWb%2BAmbIEVRi3j8%2F7%2FGoJ%2BWi%2FNwMf8sUapG9RguzfkfBSfshN%2FKc8LqORlV0BxoykI2Z%2FNKRpkuGvAxEK0W9uVxJzDEv4a9BjqkAYXmMrWwMcFy0aaq%2FDFZiqwN1um5%2B25dCRXHJLlnWXxzAXP0gt%2BuYoTvXAEMQAXC0h%2FwBV0Q4Ymfp4voxGuDxJq%2BGaZCedR92EqSChQhQqeJ19rDI5XDDdIq3F7X1j8ElvBgofk1ewBTI6OQ2M%2FmUIK%2BPG5%2F3SYkcI60gx8q3aAvL%2Bg4sbcEEwrCFzed9%2B3FR5%2BcS5r%2BXzK0QXi0rqHwCeTv3qjc&X-Amz-Signature=0744de1eb1f2a424220d36f2ab11aac822537535afb536a577ae75ca329b807c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XIZZGBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDWm50vIJnk6wo%2BT3uWRq0JdmZyZTrvBkRy606amfSqaAIhAMUQebxyVNb0KnwGQnshSloMYzm15rwlw8wXugJwYftpKv8DCCYQABoMNjM3NDIzMTgzODA1IgwgEs2e3WPM8V7R4G4q3AN10KNujVWH3TWGjMqGz%2FUvA4JJj32O3jKImv7JMjiQjF6Rp9fRohoctcXbgJLE38CnRzOvxS5b3EJ2zg1c9suxfLI4JYQMw8DgTQ5bBZfbiEPeiKutzx96Jv3AN2McPOMBfnL0uAyCvBlINwUuXQ6JhPZUvOlY4wQFKztr7nycwXAWBP9CeMX0yRfupWSptu8VgJzjlTIwUtjrI30piFYc6oEFBB7iFX%2FIS%2B450RutJ2GweBYnhzWowuvxV005%2FCEMAF4trQto60E2aoMuZjH6iuEHXb%2Fw84ti%2Bf9cjKo1dPKpDQOPFnZ6UzfJWcElF2Ue%2BDwQ7SFe65VL%2BhpBqyZjLr4YvETZUuoGoXQr9D%2BsaanKSj5RcoeSWOWqzeKxcJ%2BAmOH4OFlM7w3A6REoabW9R4PVJorcq6EM70OfxoBgvX0vfQ%2FUVamJC3VpbrAVuBwVlBsE9l%2FXuejR1VoED%2F6MrW5xonVkoWQQs1O%2BeCD1dcqrwK1VmTIkbh7cy88xhH5axOGEEfU5NIirCdhhyHPxw8wYZ2fiQ3Vw7MWb%2BAmbIEVRi3j8%2F7%2FGoJ%2BWi%2FNwMf8sUapG9RguzfkfBSfshN%2FKc8LqORlV0BxoykI2Z%2FNKRpkuGvAxEK0W9uVxJzDEv4a9BjqkAYXmMrWwMcFy0aaq%2FDFZiqwN1um5%2B25dCRXHJLlnWXxzAXP0gt%2BuYoTvXAEMQAXC0h%2FwBV0Q4Ymfp4voxGuDxJq%2BGaZCedR92EqSChQhQqeJ19rDI5XDDdIq3F7X1j8ElvBgofk1ewBTI6OQ2M%2FmUIK%2BPG5%2F3SYkcI60gx8q3aAvL%2Bg4sbcEEwrCFzed9%2B3FR5%2BcS5r%2BXzK0QXi0rqHwCeTv3qjc&X-Amz-Signature=38a609983bad1b5f30f3d6349aa904295bece5f1b60f30676c330ee83b2f9f4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XIZZGBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDWm50vIJnk6wo%2BT3uWRq0JdmZyZTrvBkRy606amfSqaAIhAMUQebxyVNb0KnwGQnshSloMYzm15rwlw8wXugJwYftpKv8DCCYQABoMNjM3NDIzMTgzODA1IgwgEs2e3WPM8V7R4G4q3AN10KNujVWH3TWGjMqGz%2FUvA4JJj32O3jKImv7JMjiQjF6Rp9fRohoctcXbgJLE38CnRzOvxS5b3EJ2zg1c9suxfLI4JYQMw8DgTQ5bBZfbiEPeiKutzx96Jv3AN2McPOMBfnL0uAyCvBlINwUuXQ6JhPZUvOlY4wQFKztr7nycwXAWBP9CeMX0yRfupWSptu8VgJzjlTIwUtjrI30piFYc6oEFBB7iFX%2FIS%2B450RutJ2GweBYnhzWowuvxV005%2FCEMAF4trQto60E2aoMuZjH6iuEHXb%2Fw84ti%2Bf9cjKo1dPKpDQOPFnZ6UzfJWcElF2Ue%2BDwQ7SFe65VL%2BhpBqyZjLr4YvETZUuoGoXQr9D%2BsaanKSj5RcoeSWOWqzeKxcJ%2BAmOH4OFlM7w3A6REoabW9R4PVJorcq6EM70OfxoBgvX0vfQ%2FUVamJC3VpbrAVuBwVlBsE9l%2FXuejR1VoED%2F6MrW5xonVkoWQQs1O%2BeCD1dcqrwK1VmTIkbh7cy88xhH5axOGEEfU5NIirCdhhyHPxw8wYZ2fiQ3Vw7MWb%2BAmbIEVRi3j8%2F7%2FGoJ%2BWi%2FNwMf8sUapG9RguzfkfBSfshN%2FKc8LqORlV0BxoykI2Z%2FNKRpkuGvAxEK0W9uVxJzDEv4a9BjqkAYXmMrWwMcFy0aaq%2FDFZiqwN1um5%2B25dCRXHJLlnWXxzAXP0gt%2BuYoTvXAEMQAXC0h%2FwBV0Q4Ymfp4voxGuDxJq%2BGaZCedR92EqSChQhQqeJ19rDI5XDDdIq3F7X1j8ElvBgofk1ewBTI6OQ2M%2FmUIK%2BPG5%2F3SYkcI60gx8q3aAvL%2Bg4sbcEEwrCFzed9%2B3FR5%2BcS5r%2BXzK0QXi0rqHwCeTv3qjc&X-Amz-Signature=cb3a768e7f98717bfeca7801be71fb8b75ecf38fe79748f11de4ad42e1f5196c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XIZZGBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDWm50vIJnk6wo%2BT3uWRq0JdmZyZTrvBkRy606amfSqaAIhAMUQebxyVNb0KnwGQnshSloMYzm15rwlw8wXugJwYftpKv8DCCYQABoMNjM3NDIzMTgzODA1IgwgEs2e3WPM8V7R4G4q3AN10KNujVWH3TWGjMqGz%2FUvA4JJj32O3jKImv7JMjiQjF6Rp9fRohoctcXbgJLE38CnRzOvxS5b3EJ2zg1c9suxfLI4JYQMw8DgTQ5bBZfbiEPeiKutzx96Jv3AN2McPOMBfnL0uAyCvBlINwUuXQ6JhPZUvOlY4wQFKztr7nycwXAWBP9CeMX0yRfupWSptu8VgJzjlTIwUtjrI30piFYc6oEFBB7iFX%2FIS%2B450RutJ2GweBYnhzWowuvxV005%2FCEMAF4trQto60E2aoMuZjH6iuEHXb%2Fw84ti%2Bf9cjKo1dPKpDQOPFnZ6UzfJWcElF2Ue%2BDwQ7SFe65VL%2BhpBqyZjLr4YvETZUuoGoXQr9D%2BsaanKSj5RcoeSWOWqzeKxcJ%2BAmOH4OFlM7w3A6REoabW9R4PVJorcq6EM70OfxoBgvX0vfQ%2FUVamJC3VpbrAVuBwVlBsE9l%2FXuejR1VoED%2F6MrW5xonVkoWQQs1O%2BeCD1dcqrwK1VmTIkbh7cy88xhH5axOGEEfU5NIirCdhhyHPxw8wYZ2fiQ3Vw7MWb%2BAmbIEVRi3j8%2F7%2FGoJ%2BWi%2FNwMf8sUapG9RguzfkfBSfshN%2FKc8LqORlV0BxoykI2Z%2FNKRpkuGvAxEK0W9uVxJzDEv4a9BjqkAYXmMrWwMcFy0aaq%2FDFZiqwN1um5%2B25dCRXHJLlnWXxzAXP0gt%2BuYoTvXAEMQAXC0h%2FwBV0Q4Ymfp4voxGuDxJq%2BGaZCedR92EqSChQhQqeJ19rDI5XDDdIq3F7X1j8ElvBgofk1ewBTI6OQ2M%2FmUIK%2BPG5%2F3SYkcI60gx8q3aAvL%2Bg4sbcEEwrCFzed9%2B3FR5%2BcS5r%2BXzK0QXi0rqHwCeTv3qjc&X-Amz-Signature=b98efa09d2985dd77f40f84324d3b54ae9541154770bdeda6cde67022871dcf9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XIZZGBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDWm50vIJnk6wo%2BT3uWRq0JdmZyZTrvBkRy606amfSqaAIhAMUQebxyVNb0KnwGQnshSloMYzm15rwlw8wXugJwYftpKv8DCCYQABoMNjM3NDIzMTgzODA1IgwgEs2e3WPM8V7R4G4q3AN10KNujVWH3TWGjMqGz%2FUvA4JJj32O3jKImv7JMjiQjF6Rp9fRohoctcXbgJLE38CnRzOvxS5b3EJ2zg1c9suxfLI4JYQMw8DgTQ5bBZfbiEPeiKutzx96Jv3AN2McPOMBfnL0uAyCvBlINwUuXQ6JhPZUvOlY4wQFKztr7nycwXAWBP9CeMX0yRfupWSptu8VgJzjlTIwUtjrI30piFYc6oEFBB7iFX%2FIS%2B450RutJ2GweBYnhzWowuvxV005%2FCEMAF4trQto60E2aoMuZjH6iuEHXb%2Fw84ti%2Bf9cjKo1dPKpDQOPFnZ6UzfJWcElF2Ue%2BDwQ7SFe65VL%2BhpBqyZjLr4YvETZUuoGoXQr9D%2BsaanKSj5RcoeSWOWqzeKxcJ%2BAmOH4OFlM7w3A6REoabW9R4PVJorcq6EM70OfxoBgvX0vfQ%2FUVamJC3VpbrAVuBwVlBsE9l%2FXuejR1VoED%2F6MrW5xonVkoWQQs1O%2BeCD1dcqrwK1VmTIkbh7cy88xhH5axOGEEfU5NIirCdhhyHPxw8wYZ2fiQ3Vw7MWb%2BAmbIEVRi3j8%2F7%2FGoJ%2BWi%2FNwMf8sUapG9RguzfkfBSfshN%2FKc8LqORlV0BxoykI2Z%2FNKRpkuGvAxEK0W9uVxJzDEv4a9BjqkAYXmMrWwMcFy0aaq%2FDFZiqwN1um5%2B25dCRXHJLlnWXxzAXP0gt%2BuYoTvXAEMQAXC0h%2FwBV0Q4Ymfp4voxGuDxJq%2BGaZCedR92EqSChQhQqeJ19rDI5XDDdIq3F7X1j8ElvBgofk1ewBTI6OQ2M%2FmUIK%2BPG5%2F3SYkcI60gx8q3aAvL%2Bg4sbcEEwrCFzed9%2B3FR5%2BcS5r%2BXzK0QXi0rqHwCeTv3qjc&X-Amz-Signature=c566ca0f807b4585d23e18034c23ce934f713ae335e257a6287a1e6f802bc430&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XIZZGBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDWm50vIJnk6wo%2BT3uWRq0JdmZyZTrvBkRy606amfSqaAIhAMUQebxyVNb0KnwGQnshSloMYzm15rwlw8wXugJwYftpKv8DCCYQABoMNjM3NDIzMTgzODA1IgwgEs2e3WPM8V7R4G4q3AN10KNujVWH3TWGjMqGz%2FUvA4JJj32O3jKImv7JMjiQjF6Rp9fRohoctcXbgJLE38CnRzOvxS5b3EJ2zg1c9suxfLI4JYQMw8DgTQ5bBZfbiEPeiKutzx96Jv3AN2McPOMBfnL0uAyCvBlINwUuXQ6JhPZUvOlY4wQFKztr7nycwXAWBP9CeMX0yRfupWSptu8VgJzjlTIwUtjrI30piFYc6oEFBB7iFX%2FIS%2B450RutJ2GweBYnhzWowuvxV005%2FCEMAF4trQto60E2aoMuZjH6iuEHXb%2Fw84ti%2Bf9cjKo1dPKpDQOPFnZ6UzfJWcElF2Ue%2BDwQ7SFe65VL%2BhpBqyZjLr4YvETZUuoGoXQr9D%2BsaanKSj5RcoeSWOWqzeKxcJ%2BAmOH4OFlM7w3A6REoabW9R4PVJorcq6EM70OfxoBgvX0vfQ%2FUVamJC3VpbrAVuBwVlBsE9l%2FXuejR1VoED%2F6MrW5xonVkoWQQs1O%2BeCD1dcqrwK1VmTIkbh7cy88xhH5axOGEEfU5NIirCdhhyHPxw8wYZ2fiQ3Vw7MWb%2BAmbIEVRi3j8%2F7%2FGoJ%2BWi%2FNwMf8sUapG9RguzfkfBSfshN%2FKc8LqORlV0BxoykI2Z%2FNKRpkuGvAxEK0W9uVxJzDEv4a9BjqkAYXmMrWwMcFy0aaq%2FDFZiqwN1um5%2B25dCRXHJLlnWXxzAXP0gt%2BuYoTvXAEMQAXC0h%2FwBV0Q4Ymfp4voxGuDxJq%2BGaZCedR92EqSChQhQqeJ19rDI5XDDdIq3F7X1j8ElvBgofk1ewBTI6OQ2M%2FmUIK%2BPG5%2F3SYkcI60gx8q3aAvL%2Bg4sbcEEwrCFzed9%2B3FR5%2BcS5r%2BXzK0QXi0rqHwCeTv3qjc&X-Amz-Signature=73a31d8635a8cf412329aa5b2d4d1abaf8704c4c22677f95c59610b41ce96e3a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XIZZGBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDWm50vIJnk6wo%2BT3uWRq0JdmZyZTrvBkRy606amfSqaAIhAMUQebxyVNb0KnwGQnshSloMYzm15rwlw8wXugJwYftpKv8DCCYQABoMNjM3NDIzMTgzODA1IgwgEs2e3WPM8V7R4G4q3AN10KNujVWH3TWGjMqGz%2FUvA4JJj32O3jKImv7JMjiQjF6Rp9fRohoctcXbgJLE38CnRzOvxS5b3EJ2zg1c9suxfLI4JYQMw8DgTQ5bBZfbiEPeiKutzx96Jv3AN2McPOMBfnL0uAyCvBlINwUuXQ6JhPZUvOlY4wQFKztr7nycwXAWBP9CeMX0yRfupWSptu8VgJzjlTIwUtjrI30piFYc6oEFBB7iFX%2FIS%2B450RutJ2GweBYnhzWowuvxV005%2FCEMAF4trQto60E2aoMuZjH6iuEHXb%2Fw84ti%2Bf9cjKo1dPKpDQOPFnZ6UzfJWcElF2Ue%2BDwQ7SFe65VL%2BhpBqyZjLr4YvETZUuoGoXQr9D%2BsaanKSj5RcoeSWOWqzeKxcJ%2BAmOH4OFlM7w3A6REoabW9R4PVJorcq6EM70OfxoBgvX0vfQ%2FUVamJC3VpbrAVuBwVlBsE9l%2FXuejR1VoED%2F6MrW5xonVkoWQQs1O%2BeCD1dcqrwK1VmTIkbh7cy88xhH5axOGEEfU5NIirCdhhyHPxw8wYZ2fiQ3Vw7MWb%2BAmbIEVRi3j8%2F7%2FGoJ%2BWi%2FNwMf8sUapG9RguzfkfBSfshN%2FKc8LqORlV0BxoykI2Z%2FNKRpkuGvAxEK0W9uVxJzDEv4a9BjqkAYXmMrWwMcFy0aaq%2FDFZiqwN1um5%2B25dCRXHJLlnWXxzAXP0gt%2BuYoTvXAEMQAXC0h%2FwBV0Q4Ymfp4voxGuDxJq%2BGaZCedR92EqSChQhQqeJ19rDI5XDDdIq3F7X1j8ElvBgofk1ewBTI6OQ2M%2FmUIK%2BPG5%2F3SYkcI60gx8q3aAvL%2Bg4sbcEEwrCFzed9%2B3FR5%2BcS5r%2BXzK0QXi0rqHwCeTv3qjc&X-Amz-Signature=787601a44b8e41869d28cc4ba447a96e00c7bdd38ce1a7d3a8e9c4a6488f5f78&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XIZZGBD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQDWm50vIJnk6wo%2BT3uWRq0JdmZyZTrvBkRy606amfSqaAIhAMUQebxyVNb0KnwGQnshSloMYzm15rwlw8wXugJwYftpKv8DCCYQABoMNjM3NDIzMTgzODA1IgwgEs2e3WPM8V7R4G4q3AN10KNujVWH3TWGjMqGz%2FUvA4JJj32O3jKImv7JMjiQjF6Rp9fRohoctcXbgJLE38CnRzOvxS5b3EJ2zg1c9suxfLI4JYQMw8DgTQ5bBZfbiEPeiKutzx96Jv3AN2McPOMBfnL0uAyCvBlINwUuXQ6JhPZUvOlY4wQFKztr7nycwXAWBP9CeMX0yRfupWSptu8VgJzjlTIwUtjrI30piFYc6oEFBB7iFX%2FIS%2B450RutJ2GweBYnhzWowuvxV005%2FCEMAF4trQto60E2aoMuZjH6iuEHXb%2Fw84ti%2Bf9cjKo1dPKpDQOPFnZ6UzfJWcElF2Ue%2BDwQ7SFe65VL%2BhpBqyZjLr4YvETZUuoGoXQr9D%2BsaanKSj5RcoeSWOWqzeKxcJ%2BAmOH4OFlM7w3A6REoabW9R4PVJorcq6EM70OfxoBgvX0vfQ%2FUVamJC3VpbrAVuBwVlBsE9l%2FXuejR1VoED%2F6MrW5xonVkoWQQs1O%2BeCD1dcqrwK1VmTIkbh7cy88xhH5axOGEEfU5NIirCdhhyHPxw8wYZ2fiQ3Vw7MWb%2BAmbIEVRi3j8%2F7%2FGoJ%2BWi%2FNwMf8sUapG9RguzfkfBSfshN%2FKc8LqORlV0BxoykI2Z%2FNKRpkuGvAxEK0W9uVxJzDEv4a9BjqkAYXmMrWwMcFy0aaq%2FDFZiqwN1um5%2B25dCRXHJLlnWXxzAXP0gt%2BuYoTvXAEMQAXC0h%2FwBV0Q4Ymfp4voxGuDxJq%2BGaZCedR92EqSChQhQqeJ19rDI5XDDdIq3F7X1j8ElvBgofk1ewBTI6OQ2M%2FmUIK%2BPG5%2F3SYkcI60gx8q3aAvL%2Bg4sbcEEwrCFzed9%2B3FR5%2BcS5r%2BXzK0QXi0rqHwCeTv3qjc&X-Amz-Signature=c582651e905e5e697c6b72e923465c9b202a003e13b650b5f63f3dd73e71176a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TP2X7A3C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIHbnJy0BBIiAKp%2Fk%2FmbTS%2BJF6JulBx5IMmT5gTccHQU4AiAElThzIOt5ZclH%2BlQFpl%2FZxWH09YGIiQk0U1RzR31FdSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMSRIvbOuoCLyDQwq0KtwD9FvFniums0%2BNf%2FR7He9kZJlI7IJ6VK807pFKj1emM23B0g0Ts1Rlfzz8pHiZyspA7CwAvrYVO23dFckPaH%2FFAPzTEr%2Fsqj4RuffED4Alho7o9xLq%2FVc07VvznLdCDTw0iy1o0OC9Ucrl243NnSo11deYqXmbT1aKTGEAK4Zz8vb1iZc%2FdtThRxB9ax8Q7bH04%2FLJ9CufCiNADUpu%2BhepGUru1x5hL%2FBCBZvZsf1hH9y7lfMKrNtCI9Ktk7WusgZjAW%2BbDWkSOFx1m%2Bl0WpS1uh7NTlNweRKEhTwFZVuXqZ3Rt4uPGEp9e3QQh5EPjh38IOJvHyMs1JqMtVJgJtooqEi8%2B%2FK2FKsabx89eQkWCsVCtEE2b5Vo0WGMLdr92LUakbul9EE5JhUX%2FM7xA31M3lLHjFUDj8KT0Is15daA8SkRA4%2FsAAXs6WXczorCvK%2FB5BeKGV6Z2S%2F4PmoLD8e%2FMTgXWyFAQeP3cioGT9qOgiFDdJIcmpY%2FRlrFZX4t%2Fw1V29zSVasRpNxEd4Vn6wzNrWbuw88zNvuvSv5HCyynDql8qP24VOn24DqRU9z2YiHR%2BSp7Ao75vJeT0eKg1mlvy3AKzOuss221LD4IEdYiUvk3eVWAq1lxn7G3F3cw276GvQY6pgFVWFLkDPgJxBn%2FxurwzLQEJGPg5lBRN6w9gKMcpeio8A5EqRYNDdouSyx0Sg6ESqBabdae9m7N7T8IhYR4Puk9dmYX4BcEfsugeExWwMlBBvG3LO3fY6h00%2FkwdlrOhWoYNtwT877p5pREQcCsXnVPjZ%2Ft04Lme8lRyke%2BYjFQqkWWEhFBL55AefDpQcbKFizArdmDt637oaEt6HpyPZ4KaIh72cgl&X-Amz-Signature=09e6de10b1e049a2e5f39b5364e5e8b0e060a69ee416e73c2f72c146e8a536aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RJ5HCAJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIG3QrbQyJL0%2BsWNN%2B3zOnnYScDdOyuvhZFuZzdUO5zhKAiBFXoTR9BPo00LMv79xXrDN5hrI5dovRyM1ITAi958EOSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMCHNyA9iwUTxRRj9BKtwDRBQ3xpUX%2Fw9yl33ZH8WnGtZxKFCCW00IlvAH0BDpqfS%2B0UqTwoQ60NONvQlZssWnPY3HMg62%2FGD5RYd6kQBX6YFpOBm7ker8Kk4ZJBvt6iSY8PwtHqvZPoYuFnqLDf9U54wPFUDo4aBmQ6Ct505XU7fXIOIr%2FG3RD4eqNnqMkb0sTyLweaopzzwfJZdNe4vJlTqlqfPxHz0t%2BWDTY6vDv7P4zlF8nt7yNxWNCVZRMNKnIHU8rBXtHVfFUNlpQXQyZt1WbShYXKaNB5aSlzpzNA7e%2FF8juxfr0cIDUK%2Fgf4bmqTwGKNahGxETNJaw%2B5l5Fj7f0yUBfdWYFZ0DLxsjaphyNNzpUIWcB0opZqrsh%2FFD5ge1SAvOpTDV1nN1CRpCQR4joHrdehvPJ6tsTrXZfXE%2B9dhar8wAaWxYdTCqV8Prvn7ByWHsueK8WgZJTIznQ%2BZvq6glgltCfS5bl%2B%2BknC8dMPbqrGR%2FlUYQMF1lK7MWWgO30si5qxAh5ond8MWQXHISGXBPT8dGalRhYDakZMBExt7mFRp0lYz8L6YBlN8wI%2FoNER5%2FbYe7ECZQc%2BFWxBOZA1KEbw%2BNaTTc4aI8vdD4vURoBX1RuHA8hBiSnNs%2FHBhZ6vv%2FZa93cXYwjL%2BGvQY6pgHnBuKbLmGLo9Os23DZ%2ByJCM6nCV2%2FJtq62IqsaKbYXMcVREciloBmiQ503jHIqchVKdmFbJM0ezDGqVvNJrYJg%2F4b3dnyK33icB16n9Q6jssmPCzNN1ahiAJ%2FPMQtDC367iUe35vfW4osctt7T9GybhYsSy36oPJfM5H0cJPyl03pPkPn9MjI%2BfKY%2BHhOo3egblc%2FHxEUd2Q7jPsqqLJX6VeP%2FjxMB&X-Amz-Signature=d222598cb3bf376d18aaa75ab10b17b6c1e901712ce507b0932eb2be94742c91&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTFSCHWJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC0eewpuSHOkcbbmN7Ma70wsVisz8%2BlkIaCZQAACFNt0QIgMo6tOTjsOxLHr49WkQeZG1UaiA%2FjHMtUUypLBAHZIcgq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCluxTHE2exSG2%2B%2BOCrcA0ggQk11zI0TMy5e%2FQu16%2FZsuybALWmQxZ%2FQH5NKjv17ypWhVQhZtxfM4YzjRIfKwKQ9fYHsKEFSRyYVnvWwBjg1d1u5AryxYDkw7ik4je%2FYMZJjNhdtigaS7wJf2T4NOZ73MgC%2BwRA8oNBWcoljuxF16pHJy%2FV7G9LF4a50CWBdg1tRrt9aKsNUfjYjh%2FvL06A8aCpsMsJzZNvO25iF%2FprI7sdVJWx2CHNa5llp8qZJ8SJH2ff1IcwESfW5tY%2FqkH6KB6%2FJdv4OUcglMPwykIC1LUQZaV0XRMjyCMwqT4cpjT5Bkb1GF51FRTWaa3vi5oBJp8kRAyvX0mdqKjcGBt5b%2Fg5h%2FqZ3ylpamCDQDYFvwImoGhxYafAYyUSPykzATCimJYyw6lLJCVS5PgQVuqthJW9GMsT1A9wdKa8yhennGfimDv8lxjqlBJC%2FG5%2Fmnv%2B%2FfJudwsYXR7wrtqTJMJO4A2zR5RUzfAC02z1DeKs%2BAh2FoJR%2B7TMPRk39aqMXYBt7JW%2BVm9bEWpGqRieFcc%2B43j3g4mehKNupb4VbNtjMFytAtpKI5iHPVLYS5dGtGn82VKhiaFl0YApExPJgQmF%2BvtCM1NZIWSJ%2BHuYUh5WRUv9%2F2lIrju0kRjyWMLK%2Bhr0GOqUBgIzvcqnVqB0WihSAJJ1SzUeC3%2F0yamGqw8NN%2F3%2F8C8d4M6WBfB1P6qCz5nuKkxnvPt28px5sm4K24S6Fgxe7Kx7Z97lNrTHzHGmHh0pk7Am4ILGpj%2Fcf6OeyW5vFfbZHmUYigdw3G067CONL9ulMntgBcOJe34rSxid8%2FdP6YD%2FyJ3m0UWrB6gXKCDcuf6Q1CtQygYFW%2BDkaB0Za%2FeKFDCe%2BjaeF&X-Amz-Signature=ba71a240c8629252d645e0b835255cefe70ce5a244149c7b30083ccd77495cff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTFSCHWJ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQC0eewpuSHOkcbbmN7Ma70wsVisz8%2BlkIaCZQAACFNt0QIgMo6tOTjsOxLHr49WkQeZG1UaiA%2FjHMtUUypLBAHZIcgq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCluxTHE2exSG2%2B%2BOCrcA0ggQk11zI0TMy5e%2FQu16%2FZsuybALWmQxZ%2FQH5NKjv17ypWhVQhZtxfM4YzjRIfKwKQ9fYHsKEFSRyYVnvWwBjg1d1u5AryxYDkw7ik4je%2FYMZJjNhdtigaS7wJf2T4NOZ73MgC%2BwRA8oNBWcoljuxF16pHJy%2FV7G9LF4a50CWBdg1tRrt9aKsNUfjYjh%2FvL06A8aCpsMsJzZNvO25iF%2FprI7sdVJWx2CHNa5llp8qZJ8SJH2ff1IcwESfW5tY%2FqkH6KB6%2FJdv4OUcglMPwykIC1LUQZaV0XRMjyCMwqT4cpjT5Bkb1GF51FRTWaa3vi5oBJp8kRAyvX0mdqKjcGBt5b%2Fg5h%2FqZ3ylpamCDQDYFvwImoGhxYafAYyUSPykzATCimJYyw6lLJCVS5PgQVuqthJW9GMsT1A9wdKa8yhennGfimDv8lxjqlBJC%2FG5%2Fmnv%2B%2FfJudwsYXR7wrtqTJMJO4A2zR5RUzfAC02z1DeKs%2BAh2FoJR%2B7TMPRk39aqMXYBt7JW%2BVm9bEWpGqRieFcc%2B43j3g4mehKNupb4VbNtjMFytAtpKI5iHPVLYS5dGtGn82VKhiaFl0YApExPJgQmF%2BvtCM1NZIWSJ%2BHuYUh5WRUv9%2F2lIrju0kRjyWMLK%2Bhr0GOqUBgIzvcqnVqB0WihSAJJ1SzUeC3%2F0yamGqw8NN%2F3%2F8C8d4M6WBfB1P6qCz5nuKkxnvPt28px5sm4K24S6Fgxe7Kx7Z97lNrTHzHGmHh0pk7Am4ILGpj%2Fcf6OeyW5vFfbZHmUYigdw3G067CONL9ulMntgBcOJe34rSxid8%2FdP6YD%2FyJ3m0UWrB6gXKCDcuf6Q1CtQygYFW%2BDkaB0Za%2FeKFDCe%2BjaeF&X-Amz-Signature=4b91e808e7fe7681ec6ef219c0ef5c6f2d5fabe3f6385d4468a297150f7cd978&X-Amz-SignedHeaders=host&x-id=GetObject)
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
