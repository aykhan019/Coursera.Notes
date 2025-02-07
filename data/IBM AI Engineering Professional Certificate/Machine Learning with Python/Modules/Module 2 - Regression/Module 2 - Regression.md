

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFX4SP2O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIH7zoBQHjqeKZEb%2B2y0j5TwhU%2FP9vKhIEzyZlq3oAwNxAiA5tG%2F1tSxRooZq%2BRHbK9QrZWrfaWJpswdzOPAT3fVStSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM9saohHE0u8xXAGnBKtwD39TiMWdDOjXcu7IXcpzINdaUIwz9OxC%2B3CRTfI4pJG204TLuW2AY48ZvgnRIRnNooMHBiCac5ND%2Bf02LGyE2%2FxpAeiCPBEyOc9FLR%2FLEpyR7kmOONh5cudNneQ78OLJMxvro%2BVxvxs5jmUk5NcIY9XkKNvnXmNOssP78551oulI%2FN3whufg1r1CqTqIRYQONH9wZD4qXs8J8mGys2an%2FsMfQVlI20%2BesjePz%2BI8ubKU%2BL4kneW3C6jHqatZnkhtp8jDrNiWx%2FLu1AVpGzPMFNjfek7mfhMMo7FkNfBWx7WARRHsIP1XoeNjWF8NqLejg6%2BPXmBCyIZfU80LoFt4DjBf63CKaavW9n8drJh6WWg31eyo3yMXZT9cp8qj%2B4KHAI9ecxoUrQP9hbpQZdcL%2B8IXD4Y8HqSIqVAbIhQIvXO3X6661IZYlUZ%2BixyUdt7o5QY76cBsRWIZnt6mutWjOgpbepq56Ua76XxcYY3KXE2Uq3YSCZo1CivTokV01%2BByweorAQPFTtn7C6z2r6l6up9eek0kpblyixL8OiprxtOD%2BJdEqwpmi7sZnXIrgF3Yq3pq9CN0mwFzd1vpprqv%2BQQH4zqUZOLSU9J9ozaREkLL6Tk9SCdb0rd2W1egw%2FPmWvQY6pgFpoGXmhA%2BAj6xGTwnDbdLG9%2FyrN%2FOBtWIxedygUfJfCuHAcibyTRwWB8I6fb%2FRhXiP0C6mt3kVJJZw%2BTA6MZRi6RoaLePvn6BDAdwcVRtKGjL2hH4SEi%2BM%2BsaBvF%2BT4AGpDIQuVJDtPBB6YHgmeU52BcCMDgR4r9igbk6%2B2ZVMYdHsaF%2FEPugLyJOAlrk1cBjV11HkOmYzlIcmtlNwrmgNNTv5SYVa&X-Amz-Signature=7d95e90eb8f0ce00249707eb46c0bd18a9282de5526868737563f5e5ec1b8921&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFX4SP2O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIH7zoBQHjqeKZEb%2B2y0j5TwhU%2FP9vKhIEzyZlq3oAwNxAiA5tG%2F1tSxRooZq%2BRHbK9QrZWrfaWJpswdzOPAT3fVStSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM9saohHE0u8xXAGnBKtwD39TiMWdDOjXcu7IXcpzINdaUIwz9OxC%2B3CRTfI4pJG204TLuW2AY48ZvgnRIRnNooMHBiCac5ND%2Bf02LGyE2%2FxpAeiCPBEyOc9FLR%2FLEpyR7kmOONh5cudNneQ78OLJMxvro%2BVxvxs5jmUk5NcIY9XkKNvnXmNOssP78551oulI%2FN3whufg1r1CqTqIRYQONH9wZD4qXs8J8mGys2an%2FsMfQVlI20%2BesjePz%2BI8ubKU%2BL4kneW3C6jHqatZnkhtp8jDrNiWx%2FLu1AVpGzPMFNjfek7mfhMMo7FkNfBWx7WARRHsIP1XoeNjWF8NqLejg6%2BPXmBCyIZfU80LoFt4DjBf63CKaavW9n8drJh6WWg31eyo3yMXZT9cp8qj%2B4KHAI9ecxoUrQP9hbpQZdcL%2B8IXD4Y8HqSIqVAbIhQIvXO3X6661IZYlUZ%2BixyUdt7o5QY76cBsRWIZnt6mutWjOgpbepq56Ua76XxcYY3KXE2Uq3YSCZo1CivTokV01%2BByweorAQPFTtn7C6z2r6l6up9eek0kpblyixL8OiprxtOD%2BJdEqwpmi7sZnXIrgF3Yq3pq9CN0mwFzd1vpprqv%2BQQH4zqUZOLSU9J9ozaREkLL6Tk9SCdb0rd2W1egw%2FPmWvQY6pgFpoGXmhA%2BAj6xGTwnDbdLG9%2FyrN%2FOBtWIxedygUfJfCuHAcibyTRwWB8I6fb%2FRhXiP0C6mt3kVJJZw%2BTA6MZRi6RoaLePvn6BDAdwcVRtKGjL2hH4SEi%2BM%2BsaBvF%2BT4AGpDIQuVJDtPBB6YHgmeU52BcCMDgR4r9igbk6%2B2ZVMYdHsaF%2FEPugLyJOAlrk1cBjV11HkOmYzlIcmtlNwrmgNNTv5SYVa&X-Amz-Signature=f41c537d6d9b3332d11366f9fbf0584adf4af354185b0d1fa1b10d336f316211&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFX4SP2O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIH7zoBQHjqeKZEb%2B2y0j5TwhU%2FP9vKhIEzyZlq3oAwNxAiA5tG%2F1tSxRooZq%2BRHbK9QrZWrfaWJpswdzOPAT3fVStSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM9saohHE0u8xXAGnBKtwD39TiMWdDOjXcu7IXcpzINdaUIwz9OxC%2B3CRTfI4pJG204TLuW2AY48ZvgnRIRnNooMHBiCac5ND%2Bf02LGyE2%2FxpAeiCPBEyOc9FLR%2FLEpyR7kmOONh5cudNneQ78OLJMxvro%2BVxvxs5jmUk5NcIY9XkKNvnXmNOssP78551oulI%2FN3whufg1r1CqTqIRYQONH9wZD4qXs8J8mGys2an%2FsMfQVlI20%2BesjePz%2BI8ubKU%2BL4kneW3C6jHqatZnkhtp8jDrNiWx%2FLu1AVpGzPMFNjfek7mfhMMo7FkNfBWx7WARRHsIP1XoeNjWF8NqLejg6%2BPXmBCyIZfU80LoFt4DjBf63CKaavW9n8drJh6WWg31eyo3yMXZT9cp8qj%2B4KHAI9ecxoUrQP9hbpQZdcL%2B8IXD4Y8HqSIqVAbIhQIvXO3X6661IZYlUZ%2BixyUdt7o5QY76cBsRWIZnt6mutWjOgpbepq56Ua76XxcYY3KXE2Uq3YSCZo1CivTokV01%2BByweorAQPFTtn7C6z2r6l6up9eek0kpblyixL8OiprxtOD%2BJdEqwpmi7sZnXIrgF3Yq3pq9CN0mwFzd1vpprqv%2BQQH4zqUZOLSU9J9ozaREkLL6Tk9SCdb0rd2W1egw%2FPmWvQY6pgFpoGXmhA%2BAj6xGTwnDbdLG9%2FyrN%2FOBtWIxedygUfJfCuHAcibyTRwWB8I6fb%2FRhXiP0C6mt3kVJJZw%2BTA6MZRi6RoaLePvn6BDAdwcVRtKGjL2hH4SEi%2BM%2BsaBvF%2BT4AGpDIQuVJDtPBB6YHgmeU52BcCMDgR4r9igbk6%2B2ZVMYdHsaF%2FEPugLyJOAlrk1cBjV11HkOmYzlIcmtlNwrmgNNTv5SYVa&X-Amz-Signature=cc874ed46572e7fdba06d484fe8763e04a3fb886919db0ec66cd5d95d78acbab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFX4SP2O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIH7zoBQHjqeKZEb%2B2y0j5TwhU%2FP9vKhIEzyZlq3oAwNxAiA5tG%2F1tSxRooZq%2BRHbK9QrZWrfaWJpswdzOPAT3fVStSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM9saohHE0u8xXAGnBKtwD39TiMWdDOjXcu7IXcpzINdaUIwz9OxC%2B3CRTfI4pJG204TLuW2AY48ZvgnRIRnNooMHBiCac5ND%2Bf02LGyE2%2FxpAeiCPBEyOc9FLR%2FLEpyR7kmOONh5cudNneQ78OLJMxvro%2BVxvxs5jmUk5NcIY9XkKNvnXmNOssP78551oulI%2FN3whufg1r1CqTqIRYQONH9wZD4qXs8J8mGys2an%2FsMfQVlI20%2BesjePz%2BI8ubKU%2BL4kneW3C6jHqatZnkhtp8jDrNiWx%2FLu1AVpGzPMFNjfek7mfhMMo7FkNfBWx7WARRHsIP1XoeNjWF8NqLejg6%2BPXmBCyIZfU80LoFt4DjBf63CKaavW9n8drJh6WWg31eyo3yMXZT9cp8qj%2B4KHAI9ecxoUrQP9hbpQZdcL%2B8IXD4Y8HqSIqVAbIhQIvXO3X6661IZYlUZ%2BixyUdt7o5QY76cBsRWIZnt6mutWjOgpbepq56Ua76XxcYY3KXE2Uq3YSCZo1CivTokV01%2BByweorAQPFTtn7C6z2r6l6up9eek0kpblyixL8OiprxtOD%2BJdEqwpmi7sZnXIrgF3Yq3pq9CN0mwFzd1vpprqv%2BQQH4zqUZOLSU9J9ozaREkLL6Tk9SCdb0rd2W1egw%2FPmWvQY6pgFpoGXmhA%2BAj6xGTwnDbdLG9%2FyrN%2FOBtWIxedygUfJfCuHAcibyTRwWB8I6fb%2FRhXiP0C6mt3kVJJZw%2BTA6MZRi6RoaLePvn6BDAdwcVRtKGjL2hH4SEi%2BM%2BsaBvF%2BT4AGpDIQuVJDtPBB6YHgmeU52BcCMDgR4r9igbk6%2B2ZVMYdHsaF%2FEPugLyJOAlrk1cBjV11HkOmYzlIcmtlNwrmgNNTv5SYVa&X-Amz-Signature=0454d2c16fe2b5c721ea6b1873634c911ee77b93cd7ddb41a399cd5f03ee58b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFX4SP2O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIH7zoBQHjqeKZEb%2B2y0j5TwhU%2FP9vKhIEzyZlq3oAwNxAiA5tG%2F1tSxRooZq%2BRHbK9QrZWrfaWJpswdzOPAT3fVStSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM9saohHE0u8xXAGnBKtwD39TiMWdDOjXcu7IXcpzINdaUIwz9OxC%2B3CRTfI4pJG204TLuW2AY48ZvgnRIRnNooMHBiCac5ND%2Bf02LGyE2%2FxpAeiCPBEyOc9FLR%2FLEpyR7kmOONh5cudNneQ78OLJMxvro%2BVxvxs5jmUk5NcIY9XkKNvnXmNOssP78551oulI%2FN3whufg1r1CqTqIRYQONH9wZD4qXs8J8mGys2an%2FsMfQVlI20%2BesjePz%2BI8ubKU%2BL4kneW3C6jHqatZnkhtp8jDrNiWx%2FLu1AVpGzPMFNjfek7mfhMMo7FkNfBWx7WARRHsIP1XoeNjWF8NqLejg6%2BPXmBCyIZfU80LoFt4DjBf63CKaavW9n8drJh6WWg31eyo3yMXZT9cp8qj%2B4KHAI9ecxoUrQP9hbpQZdcL%2B8IXD4Y8HqSIqVAbIhQIvXO3X6661IZYlUZ%2BixyUdt7o5QY76cBsRWIZnt6mutWjOgpbepq56Ua76XxcYY3KXE2Uq3YSCZo1CivTokV01%2BByweorAQPFTtn7C6z2r6l6up9eek0kpblyixL8OiprxtOD%2BJdEqwpmi7sZnXIrgF3Yq3pq9CN0mwFzd1vpprqv%2BQQH4zqUZOLSU9J9ozaREkLL6Tk9SCdb0rd2W1egw%2FPmWvQY6pgFpoGXmhA%2BAj6xGTwnDbdLG9%2FyrN%2FOBtWIxedygUfJfCuHAcibyTRwWB8I6fb%2FRhXiP0C6mt3kVJJZw%2BTA6MZRi6RoaLePvn6BDAdwcVRtKGjL2hH4SEi%2BM%2BsaBvF%2BT4AGpDIQuVJDtPBB6YHgmeU52BcCMDgR4r9igbk6%2B2ZVMYdHsaF%2FEPugLyJOAlrk1cBjV11HkOmYzlIcmtlNwrmgNNTv5SYVa&X-Amz-Signature=5f75369c4de1043b6d8dc1a144d8b5d0f565aa3bf90b5cd192cecc491422b89a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFX4SP2O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIH7zoBQHjqeKZEb%2B2y0j5TwhU%2FP9vKhIEzyZlq3oAwNxAiA5tG%2F1tSxRooZq%2BRHbK9QrZWrfaWJpswdzOPAT3fVStSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM9saohHE0u8xXAGnBKtwD39TiMWdDOjXcu7IXcpzINdaUIwz9OxC%2B3CRTfI4pJG204TLuW2AY48ZvgnRIRnNooMHBiCac5ND%2Bf02LGyE2%2FxpAeiCPBEyOc9FLR%2FLEpyR7kmOONh5cudNneQ78OLJMxvro%2BVxvxs5jmUk5NcIY9XkKNvnXmNOssP78551oulI%2FN3whufg1r1CqTqIRYQONH9wZD4qXs8J8mGys2an%2FsMfQVlI20%2BesjePz%2BI8ubKU%2BL4kneW3C6jHqatZnkhtp8jDrNiWx%2FLu1AVpGzPMFNjfek7mfhMMo7FkNfBWx7WARRHsIP1XoeNjWF8NqLejg6%2BPXmBCyIZfU80LoFt4DjBf63CKaavW9n8drJh6WWg31eyo3yMXZT9cp8qj%2B4KHAI9ecxoUrQP9hbpQZdcL%2B8IXD4Y8HqSIqVAbIhQIvXO3X6661IZYlUZ%2BixyUdt7o5QY76cBsRWIZnt6mutWjOgpbepq56Ua76XxcYY3KXE2Uq3YSCZo1CivTokV01%2BByweorAQPFTtn7C6z2r6l6up9eek0kpblyixL8OiprxtOD%2BJdEqwpmi7sZnXIrgF3Yq3pq9CN0mwFzd1vpprqv%2BQQH4zqUZOLSU9J9ozaREkLL6Tk9SCdb0rd2W1egw%2FPmWvQY6pgFpoGXmhA%2BAj6xGTwnDbdLG9%2FyrN%2FOBtWIxedygUfJfCuHAcibyTRwWB8I6fb%2FRhXiP0C6mt3kVJJZw%2BTA6MZRi6RoaLePvn6BDAdwcVRtKGjL2hH4SEi%2BM%2BsaBvF%2BT4AGpDIQuVJDtPBB6YHgmeU52BcCMDgR4r9igbk6%2B2ZVMYdHsaF%2FEPugLyJOAlrk1cBjV11HkOmYzlIcmtlNwrmgNNTv5SYVa&X-Amz-Signature=5ea7092243c1a56a07f7eb6a86ec4ae12ca2a2afb21299c8ece29b4dd5f5e28a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFX4SP2O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIH7zoBQHjqeKZEb%2B2y0j5TwhU%2FP9vKhIEzyZlq3oAwNxAiA5tG%2F1tSxRooZq%2BRHbK9QrZWrfaWJpswdzOPAT3fVStSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM9saohHE0u8xXAGnBKtwD39TiMWdDOjXcu7IXcpzINdaUIwz9OxC%2B3CRTfI4pJG204TLuW2AY48ZvgnRIRnNooMHBiCac5ND%2Bf02LGyE2%2FxpAeiCPBEyOc9FLR%2FLEpyR7kmOONh5cudNneQ78OLJMxvro%2BVxvxs5jmUk5NcIY9XkKNvnXmNOssP78551oulI%2FN3whufg1r1CqTqIRYQONH9wZD4qXs8J8mGys2an%2FsMfQVlI20%2BesjePz%2BI8ubKU%2BL4kneW3C6jHqatZnkhtp8jDrNiWx%2FLu1AVpGzPMFNjfek7mfhMMo7FkNfBWx7WARRHsIP1XoeNjWF8NqLejg6%2BPXmBCyIZfU80LoFt4DjBf63CKaavW9n8drJh6WWg31eyo3yMXZT9cp8qj%2B4KHAI9ecxoUrQP9hbpQZdcL%2B8IXD4Y8HqSIqVAbIhQIvXO3X6661IZYlUZ%2BixyUdt7o5QY76cBsRWIZnt6mutWjOgpbepq56Ua76XxcYY3KXE2Uq3YSCZo1CivTokV01%2BByweorAQPFTtn7C6z2r6l6up9eek0kpblyixL8OiprxtOD%2BJdEqwpmi7sZnXIrgF3Yq3pq9CN0mwFzd1vpprqv%2BQQH4zqUZOLSU9J9ozaREkLL6Tk9SCdb0rd2W1egw%2FPmWvQY6pgFpoGXmhA%2BAj6xGTwnDbdLG9%2FyrN%2FOBtWIxedygUfJfCuHAcibyTRwWB8I6fb%2FRhXiP0C6mt3kVJJZw%2BTA6MZRi6RoaLePvn6BDAdwcVRtKGjL2hH4SEi%2BM%2BsaBvF%2BT4AGpDIQuVJDtPBB6YHgmeU52BcCMDgR4r9igbk6%2B2ZVMYdHsaF%2FEPugLyJOAlrk1cBjV11HkOmYzlIcmtlNwrmgNNTv5SYVa&X-Amz-Signature=70bcec7df713c93e8152ee55b76eebef8e89773df62ecb7cf2bdc545982ff7fc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFX4SP2O%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIH7zoBQHjqeKZEb%2B2y0j5TwhU%2FP9vKhIEzyZlq3oAwNxAiA5tG%2F1tSxRooZq%2BRHbK9QrZWrfaWJpswdzOPAT3fVStSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIM9saohHE0u8xXAGnBKtwD39TiMWdDOjXcu7IXcpzINdaUIwz9OxC%2B3CRTfI4pJG204TLuW2AY48ZvgnRIRnNooMHBiCac5ND%2Bf02LGyE2%2FxpAeiCPBEyOc9FLR%2FLEpyR7kmOONh5cudNneQ78OLJMxvro%2BVxvxs5jmUk5NcIY9XkKNvnXmNOssP78551oulI%2FN3whufg1r1CqTqIRYQONH9wZD4qXs8J8mGys2an%2FsMfQVlI20%2BesjePz%2BI8ubKU%2BL4kneW3C6jHqatZnkhtp8jDrNiWx%2FLu1AVpGzPMFNjfek7mfhMMo7FkNfBWx7WARRHsIP1XoeNjWF8NqLejg6%2BPXmBCyIZfU80LoFt4DjBf63CKaavW9n8drJh6WWg31eyo3yMXZT9cp8qj%2B4KHAI9ecxoUrQP9hbpQZdcL%2B8IXD4Y8HqSIqVAbIhQIvXO3X6661IZYlUZ%2BixyUdt7o5QY76cBsRWIZnt6mutWjOgpbepq56Ua76XxcYY3KXE2Uq3YSCZo1CivTokV01%2BByweorAQPFTtn7C6z2r6l6up9eek0kpblyixL8OiprxtOD%2BJdEqwpmi7sZnXIrgF3Yq3pq9CN0mwFzd1vpprqv%2BQQH4zqUZOLSU9J9ozaREkLL6Tk9SCdb0rd2W1egw%2FPmWvQY6pgFpoGXmhA%2BAj6xGTwnDbdLG9%2FyrN%2FOBtWIxedygUfJfCuHAcibyTRwWB8I6fb%2FRhXiP0C6mt3kVJJZw%2BTA6MZRi6RoaLePvn6BDAdwcVRtKGjL2hH4SEi%2BM%2BsaBvF%2BT4AGpDIQuVJDtPBB6YHgmeU52BcCMDgR4r9igbk6%2B2ZVMYdHsaF%2FEPugLyJOAlrk1cBjV11HkOmYzlIcmtlNwrmgNNTv5SYVa&X-Amz-Signature=c94b7f42c5895ae3a0daf6a0ccc1fa05e27eff40de5730145c060bc209b363b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627ELILNL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDsTBAEgsWjp8zwpS%2FgSECugZGny2VgbXvMxFExm8HndAIhAPVWKIwRKEC7IRrCq9cbmFwbYi0X1Lkmxvytexfh2x6iKv8DCHEQABoMNjM3NDIzMTgzODA1IgyxSQk60kzDv6HKnSIq3AMKFHWdVlrjFmFV3GoQJG9YZm5XGyQlkcS1e3uYkPq8gXFxbx0KGcOCI2GJnicXHobqAQ6qPxDADVnaIYjQCCKfOxbFKhBoRPq%2BUmJ1o99OMSmpu1JpWqEFiB73oWLD6k%2FVqQzD37yidfgO5Kdl0BYT3FAlaOgX3bJUJvdhmGYvl0KbFfe0EM7zc1Z9ilq0afO8L7Id1kZ1rlftOWru1tfw3EBMAuyEoBXtydbCNCX89isnuShoSJwoDlPDAc9E2zZg2pTy%2BRRuM9kdWBwbwOagYieVSO5XfLYX3V6iPdH4L08kpcjVoBOBXkHhdTqMza7gLPmiNqMJveazNXWpcwp%2Ba28j37zr3u3CAcq2obfqS1z2icWZxNlJ96zTmrE3rAYHi4KHFiyVZ%2FgXo4LPcQ%2F3D3qZBtanSwyVDqInvL9KqaPokUdz4Th%2BuCMZzfVXvwygjGFhN%2F%2BgE%2Fplhp0TwnGPnWg5bUPFQHZib3HmIPluymoOWtbMZ19YTDfxN0aGEZ3k73zXxtd3IFvmq96wfJvx9NHoeI3lwdWYNX9sJ%2BmszBIKRHE6oe%2B%2F0olxm3%2FF3IMZtC8NAH88LEEYekTWxZRI2uQ4fmRKzxWjXvqbUUVEkrDbmwTo8oXYdb0wqjC7%2BZa9BjqkAcUpSiv%2Fc4ztKGnCAVZl85GngSGn9GWGtpo0ArWxY%2FVWwF5jz4KBgWzqCyYozWzjBtpoMSl9F3sUFzsCEzSWjM8lF1rFV51EY4TJZ9brWFvwYh7DkgLmWg3z%2BSFiC97p1HMTk4CzaKx1VRGx%2FvJHxdinEdO5qd4NwFtkHPuE9EckTSGwHa2M0BoyGJUUcq7aTDcHSti3axsn%2BIQp9aM%2BIvI%2BViRN&X-Amz-Signature=7106772e237199337a055c13fb48fc285f4ed305e9b17709fdcdb3d307eecd8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2RBB4EA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCICxE1Rn4Dpjnr0lMZv6jGxK3NBZBu8l1Xoze%2FmD%2B%2Fm6hAiAt7WxAsZ482Zay7WkFT2aJWmSanCmy38M7qoIH7ROHmSr%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMMd5hfzoQd12vIrNnKtwDoBb2CKWW7lA7tQVImUFEOyYNAjL8Zfdsz2ERDCIjh40dGEKE8uyPlMP%2Bdgyot7rICh%2BgrCN4dRAtTP%2BdaPpm157UrRTE2Q6qSGMsZ7OJog2ER7mqR0XzVZyZIQYQGpYosZ7VlY5tdCy%2BVAfmDAi9J4QPmE4IMEpnbRLrACtUjz9S%2B9rnVFeiTwElHz2nDbu3Trpr%2FBMykVzyXSaycJ6MujdpHcg0AtFUIgaTYJgUvna2FSqO34v73AQ9PZI5NLxZEqFjS5IKtOAKV24MuxhwKFq6pXv1FI%2B99Uk1cX%2FtgiOuO5kJH5726XF95Z05bpL9jiNJg2bnEwqqSU%2F2LVQRiei2kD%2B1ovUURDNSCF28bBUsrUb986jPnjZ51kFyoXaAwtthhBxIdvFj0mjft1DxqJN9cQFkmoKjPiQ8nw4Cgub7niQKGkEIHACsRpmPrgDfFpeC0lde37nG3up2SVWwccubnFbdLRiZ6Pj8ruEc4ZxlEgTTVurXlx%2Fxb5JYKBSeuJNsM%2F4515DJxQYxKAk1s0oI2%2F5Vg8k5A%2FGq6R8IVAKWhpmYiSY95Yy9%2FYkznq%2Bv00dM2kSrO1n%2BLFGwtpmnh3%2BRv8vgMEWRSin%2F6yNVyKLps9O1Gdi8ZeSQo4wwj%2FqWvQY6pgFUd6dRTOO95Zyx28fM9Fa6x%2BiWgH4wlA6j5%2BSUBljbEaq2RoWpne3LTxeAr90kRfs%2BNVN%2BhPVeXg98dnnA24wiVdpEY9J9Vz2TmevvZbTAihzyJiyDYvAiAf7ER2wAet%2BF4uP6K4Yzytei7RWgr9kpuDiQSfrmMmGLTo4l%2BQA%2B28J%2FnMUV6TRv8p4Pb3PuJMBi4uAt9tl2MkjtSJvxS7uyYCtWp7ft&X-Amz-Signature=a6027b64682829196a72101d41a3a51e51a9215402ddc0360d837b1fd096f104&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSXU4QTP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCkFJIHmi920L%2B66tr8DxZYwZpBGh%2BIqIUSph8k18kngwIhAPgolSoNSK7MHRn3ClwG1GuAt54v53cEUJYzb78xDy0IKv8DCHEQABoMNjM3NDIzMTgzODA1Igynv%2FKR6ZxPTRWWc7oq3AMfwCnZ6EjPATRDEgo4pa5UyisPeKXc2BF3VDgvbBrmm3scL2bX0C7RchxowBxh4gvrwTOl%2BTLIb5E8Kqs7kL1pkwe%2BV%2FJ6JGNuZle7SE%2FjAwY6dpftuCO%2BkVMmN%2BqbG8GhGAWc721nk4OJshy6SW1wWp2%2FhIdI4SmAstxtfNb%2BtYsfeRGv0pyatMbwpM9WPAtM4qy3ynQfgV56bTOedwiuTZkdvQiCS7SaCfxP1FIFciBLXzkr9s8q4FdnEvRGy8oVyyL23DljC8a0Uu%2FGebexRb7AyELyFSKz%2FvPZzbb1l2ck2twOwPFp6d63n4xtkZz3GPKNqrpOasYKeParxpBUbFwY%2BXBcvoKyS%2FdQpN0nvmSawuUJEEUrO0lP0PHFBKlRWIS3nYX6B8QSWtcyN72qkzdOKX%2BeL5piw7g56CDInQ32jhYvbDD35iFFTuhjRlN39%2Fu%2BWyYh%2FdqcRpKNUBQPUqVkGztCjiaF9ouqhZgTtPDu4d2GYnvWkP5%2BPxbdv3YkLjQTOf7mcX1ApBWbAYcKToamfd1w9yrntjjJdEYUnWqflVcd8BLjHY25KxPa5MR5Y8wOfnaMcIF4XSWVmEYW92LWlXQjYyCs9alIx4%2BR2HUmu8Ak8hhgYa0XXDDM%2Bpa9BjqkAakpJ5P0whWvmRIPmeX7QT1jlm3kWcCQXSTUE3fXyfgy7nsfKbKRMWrJB3aV%2BfXkBUeB8eLMUxHnQWT9nOTrqmvtjzxuQR%2F3zEHQoAzI%2BT14ix%2FzwgqQbpYLqT1P0oQZNoSILzBgap33bX93ECXQj1KIDMhbPdXACUWe4KH%2FlP8f%2FwrUWelBiR0MqefLc4bMzhrI%2B6pP7cwdmL2HZCSpNcx1VF5D&X-Amz-Signature=c13eeb39fc12c5b6de0c6a7806083c99c20fd908560acc8df5d931807abe0424&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSXU4QTP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T081859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCkFJIHmi920L%2B66tr8DxZYwZpBGh%2BIqIUSph8k18kngwIhAPgolSoNSK7MHRn3ClwG1GuAt54v53cEUJYzb78xDy0IKv8DCHEQABoMNjM3NDIzMTgzODA1Igynv%2FKR6ZxPTRWWc7oq3AMfwCnZ6EjPATRDEgo4pa5UyisPeKXc2BF3VDgvbBrmm3scL2bX0C7RchxowBxh4gvrwTOl%2BTLIb5E8Kqs7kL1pkwe%2BV%2FJ6JGNuZle7SE%2FjAwY6dpftuCO%2BkVMmN%2BqbG8GhGAWc721nk4OJshy6SW1wWp2%2FhIdI4SmAstxtfNb%2BtYsfeRGv0pyatMbwpM9WPAtM4qy3ynQfgV56bTOedwiuTZkdvQiCS7SaCfxP1FIFciBLXzkr9s8q4FdnEvRGy8oVyyL23DljC8a0Uu%2FGebexRb7AyELyFSKz%2FvPZzbb1l2ck2twOwPFp6d63n4xtkZz3GPKNqrpOasYKeParxpBUbFwY%2BXBcvoKyS%2FdQpN0nvmSawuUJEEUrO0lP0PHFBKlRWIS3nYX6B8QSWtcyN72qkzdOKX%2BeL5piw7g56CDInQ32jhYvbDD35iFFTuhjRlN39%2Fu%2BWyYh%2FdqcRpKNUBQPUqVkGztCjiaF9ouqhZgTtPDu4d2GYnvWkP5%2BPxbdv3YkLjQTOf7mcX1ApBWbAYcKToamfd1w9yrntjjJdEYUnWqflVcd8BLjHY25KxPa5MR5Y8wOfnaMcIF4XSWVmEYW92LWlXQjYyCs9alIx4%2BR2HUmu8Ak8hhgYa0XXDDM%2Bpa9BjqkAakpJ5P0whWvmRIPmeX7QT1jlm3kWcCQXSTUE3fXyfgy7nsfKbKRMWrJB3aV%2BfXkBUeB8eLMUxHnQWT9nOTrqmvtjzxuQR%2F3zEHQoAzI%2BT14ix%2FzwgqQbpYLqT1P0oQZNoSILzBgap33bX93ECXQj1KIDMhbPdXACUWe4KH%2FlP8f%2FwrUWelBiR0MqefLc4bMzhrI%2B6pP7cwdmL2HZCSpNcx1VF5D&X-Amz-Signature=7e1f9e9aafe1513ae31239c08d88b808777f4b195fd12de53299e60098a945ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
