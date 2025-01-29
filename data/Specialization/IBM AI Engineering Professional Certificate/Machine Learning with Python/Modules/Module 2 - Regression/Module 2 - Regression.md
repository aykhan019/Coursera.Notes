

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EDVDGUC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIDCTbJGOIgb8RUUbfEYybu%2B7eLP58HPYSvaFErtw39MyAiBuVushVFSE8g2SCeXVC96iCmjQqr1cf7vd7JRCRK%2Fk7iqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRboTpYXl6kk%2FyXkXKtwDNfQHLxOg9mjw8sTdxkNWG2UNGOUjCSZiOh5Z28Tk%2BuCTpqbnaqO9VNYir3mrYQAY7%2FIQgWkdGZGDtrPMv0f6%2FkwFRQkCB5nJvT8ZIYoLNZr3mXh1h7n7En3ekEW1VQldiUFlTJhP7I26vHUTLW6Izr%2Fo9IAGTkAK66Sd43mHO7jokluyAwgTvg9f4PHxDyalPrOuMgUX22kNRTQ3YnLt2EIF8fwtwpk9eGFOxRBrdb%2BJD2y4A%2FafArhv7MqSiKrV7YIEKC1oi8PGTwJkdm8tWN2Xb34YmCVQ%2Fhah9G7Be9lDT%2B5IJjWJQLhuVIzw6%2BNeeQFgrounoJSYB%2FLTbptWC9lZBbsJfvBiLFdR3qpFcdO2M3BUQtnAPUV2YgkGeYo7sU9506PMBhxXyObX9fpgS9aWO7%2Ba1Y0jXNHzWbYknM69EqYb673iND9rQafDi4dVh8XHAOB%2FbOUKbcfbtT5USyJFY69MZNW9VUdA3eJWSKeWTKSa4HjSVRzeUJCRiCikX3mfPtW3f1P3e93ItZIMKeIh0PND9DI3vqsD82eWkCIcLqWIUDK2McA%2FD2krlAjNzXoZbPWIGq1%2BpQdlEdSkZXfwxS%2F4ZsMxAd0nJp3BnBegHa3l3Ez4bq6M3%2BIwsqDmvAY6pgGawwDZOo1ookUDwIRHulutgEU1Pq1%2BjufI1fXxFZb8UERy%2F2%2FLKKOuL7x6nQeXDiOF8%2Fdj9u811MZTSBBIBc3Zis3Gj%2F151gyGj7v4zsfsqaGk3mAwTwiFi31B0qE6ca5zFROoCUXmZq%2BgGmI6G4uF58ykUhcdMbLwRF8gSYW5OhuBv9HnpwAguMihqHXaVShXYqSJbv9kqNMtrHdViSzPwsoQ5MXG&X-Amz-Signature=094640304a7a9967dc17f591a5fafa67b3bf9506eb9730667318f200e0ba80de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EDVDGUC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIDCTbJGOIgb8RUUbfEYybu%2B7eLP58HPYSvaFErtw39MyAiBuVushVFSE8g2SCeXVC96iCmjQqr1cf7vd7JRCRK%2Fk7iqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRboTpYXl6kk%2FyXkXKtwDNfQHLxOg9mjw8sTdxkNWG2UNGOUjCSZiOh5Z28Tk%2BuCTpqbnaqO9VNYir3mrYQAY7%2FIQgWkdGZGDtrPMv0f6%2FkwFRQkCB5nJvT8ZIYoLNZr3mXh1h7n7En3ekEW1VQldiUFlTJhP7I26vHUTLW6Izr%2Fo9IAGTkAK66Sd43mHO7jokluyAwgTvg9f4PHxDyalPrOuMgUX22kNRTQ3YnLt2EIF8fwtwpk9eGFOxRBrdb%2BJD2y4A%2FafArhv7MqSiKrV7YIEKC1oi8PGTwJkdm8tWN2Xb34YmCVQ%2Fhah9G7Be9lDT%2B5IJjWJQLhuVIzw6%2BNeeQFgrounoJSYB%2FLTbptWC9lZBbsJfvBiLFdR3qpFcdO2M3BUQtnAPUV2YgkGeYo7sU9506PMBhxXyObX9fpgS9aWO7%2Ba1Y0jXNHzWbYknM69EqYb673iND9rQafDi4dVh8XHAOB%2FbOUKbcfbtT5USyJFY69MZNW9VUdA3eJWSKeWTKSa4HjSVRzeUJCRiCikX3mfPtW3f1P3e93ItZIMKeIh0PND9DI3vqsD82eWkCIcLqWIUDK2McA%2FD2krlAjNzXoZbPWIGq1%2BpQdlEdSkZXfwxS%2F4ZsMxAd0nJp3BnBegHa3l3Ez4bq6M3%2BIwsqDmvAY6pgGawwDZOo1ookUDwIRHulutgEU1Pq1%2BjufI1fXxFZb8UERy%2F2%2FLKKOuL7x6nQeXDiOF8%2Fdj9u811MZTSBBIBc3Zis3Gj%2F151gyGj7v4zsfsqaGk3mAwTwiFi31B0qE6ca5zFROoCUXmZq%2BgGmI6G4uF58ykUhcdMbLwRF8gSYW5OhuBv9HnpwAguMihqHXaVShXYqSJbv9kqNMtrHdViSzPwsoQ5MXG&X-Amz-Signature=f7b2301c97ebc106a8a9682616fdc8ccbfffb81d336c4ce1cb6a2a03058e7aa1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EDVDGUC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIDCTbJGOIgb8RUUbfEYybu%2B7eLP58HPYSvaFErtw39MyAiBuVushVFSE8g2SCeXVC96iCmjQqr1cf7vd7JRCRK%2Fk7iqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRboTpYXl6kk%2FyXkXKtwDNfQHLxOg9mjw8sTdxkNWG2UNGOUjCSZiOh5Z28Tk%2BuCTpqbnaqO9VNYir3mrYQAY7%2FIQgWkdGZGDtrPMv0f6%2FkwFRQkCB5nJvT8ZIYoLNZr3mXh1h7n7En3ekEW1VQldiUFlTJhP7I26vHUTLW6Izr%2Fo9IAGTkAK66Sd43mHO7jokluyAwgTvg9f4PHxDyalPrOuMgUX22kNRTQ3YnLt2EIF8fwtwpk9eGFOxRBrdb%2BJD2y4A%2FafArhv7MqSiKrV7YIEKC1oi8PGTwJkdm8tWN2Xb34YmCVQ%2Fhah9G7Be9lDT%2B5IJjWJQLhuVIzw6%2BNeeQFgrounoJSYB%2FLTbptWC9lZBbsJfvBiLFdR3qpFcdO2M3BUQtnAPUV2YgkGeYo7sU9506PMBhxXyObX9fpgS9aWO7%2Ba1Y0jXNHzWbYknM69EqYb673iND9rQafDi4dVh8XHAOB%2FbOUKbcfbtT5USyJFY69MZNW9VUdA3eJWSKeWTKSa4HjSVRzeUJCRiCikX3mfPtW3f1P3e93ItZIMKeIh0PND9DI3vqsD82eWkCIcLqWIUDK2McA%2FD2krlAjNzXoZbPWIGq1%2BpQdlEdSkZXfwxS%2F4ZsMxAd0nJp3BnBegHa3l3Ez4bq6M3%2BIwsqDmvAY6pgGawwDZOo1ookUDwIRHulutgEU1Pq1%2BjufI1fXxFZb8UERy%2F2%2FLKKOuL7x6nQeXDiOF8%2Fdj9u811MZTSBBIBc3Zis3Gj%2F151gyGj7v4zsfsqaGk3mAwTwiFi31B0qE6ca5zFROoCUXmZq%2BgGmI6G4uF58ykUhcdMbLwRF8gSYW5OhuBv9HnpwAguMihqHXaVShXYqSJbv9kqNMtrHdViSzPwsoQ5MXG&X-Amz-Signature=f5ac069e1db884e435b9a566c787bb97853387dbd21c3caade445551e3b7196b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EDVDGUC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIDCTbJGOIgb8RUUbfEYybu%2B7eLP58HPYSvaFErtw39MyAiBuVushVFSE8g2SCeXVC96iCmjQqr1cf7vd7JRCRK%2Fk7iqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRboTpYXl6kk%2FyXkXKtwDNfQHLxOg9mjw8sTdxkNWG2UNGOUjCSZiOh5Z28Tk%2BuCTpqbnaqO9VNYir3mrYQAY7%2FIQgWkdGZGDtrPMv0f6%2FkwFRQkCB5nJvT8ZIYoLNZr3mXh1h7n7En3ekEW1VQldiUFlTJhP7I26vHUTLW6Izr%2Fo9IAGTkAK66Sd43mHO7jokluyAwgTvg9f4PHxDyalPrOuMgUX22kNRTQ3YnLt2EIF8fwtwpk9eGFOxRBrdb%2BJD2y4A%2FafArhv7MqSiKrV7YIEKC1oi8PGTwJkdm8tWN2Xb34YmCVQ%2Fhah9G7Be9lDT%2B5IJjWJQLhuVIzw6%2BNeeQFgrounoJSYB%2FLTbptWC9lZBbsJfvBiLFdR3qpFcdO2M3BUQtnAPUV2YgkGeYo7sU9506PMBhxXyObX9fpgS9aWO7%2Ba1Y0jXNHzWbYknM69EqYb673iND9rQafDi4dVh8XHAOB%2FbOUKbcfbtT5USyJFY69MZNW9VUdA3eJWSKeWTKSa4HjSVRzeUJCRiCikX3mfPtW3f1P3e93ItZIMKeIh0PND9DI3vqsD82eWkCIcLqWIUDK2McA%2FD2krlAjNzXoZbPWIGq1%2BpQdlEdSkZXfwxS%2F4ZsMxAd0nJp3BnBegHa3l3Ez4bq6M3%2BIwsqDmvAY6pgGawwDZOo1ookUDwIRHulutgEU1Pq1%2BjufI1fXxFZb8UERy%2F2%2FLKKOuL7x6nQeXDiOF8%2Fdj9u811MZTSBBIBc3Zis3Gj%2F151gyGj7v4zsfsqaGk3mAwTwiFi31B0qE6ca5zFROoCUXmZq%2BgGmI6G4uF58ykUhcdMbLwRF8gSYW5OhuBv9HnpwAguMihqHXaVShXYqSJbv9kqNMtrHdViSzPwsoQ5MXG&X-Amz-Signature=85e6ebf7b71299e8ca71a99b9600364fd54d82b66bedabf848beb11d61c48841&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EDVDGUC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIDCTbJGOIgb8RUUbfEYybu%2B7eLP58HPYSvaFErtw39MyAiBuVushVFSE8g2SCeXVC96iCmjQqr1cf7vd7JRCRK%2Fk7iqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRboTpYXl6kk%2FyXkXKtwDNfQHLxOg9mjw8sTdxkNWG2UNGOUjCSZiOh5Z28Tk%2BuCTpqbnaqO9VNYir3mrYQAY7%2FIQgWkdGZGDtrPMv0f6%2FkwFRQkCB5nJvT8ZIYoLNZr3mXh1h7n7En3ekEW1VQldiUFlTJhP7I26vHUTLW6Izr%2Fo9IAGTkAK66Sd43mHO7jokluyAwgTvg9f4PHxDyalPrOuMgUX22kNRTQ3YnLt2EIF8fwtwpk9eGFOxRBrdb%2BJD2y4A%2FafArhv7MqSiKrV7YIEKC1oi8PGTwJkdm8tWN2Xb34YmCVQ%2Fhah9G7Be9lDT%2B5IJjWJQLhuVIzw6%2BNeeQFgrounoJSYB%2FLTbptWC9lZBbsJfvBiLFdR3qpFcdO2M3BUQtnAPUV2YgkGeYo7sU9506PMBhxXyObX9fpgS9aWO7%2Ba1Y0jXNHzWbYknM69EqYb673iND9rQafDi4dVh8XHAOB%2FbOUKbcfbtT5USyJFY69MZNW9VUdA3eJWSKeWTKSa4HjSVRzeUJCRiCikX3mfPtW3f1P3e93ItZIMKeIh0PND9DI3vqsD82eWkCIcLqWIUDK2McA%2FD2krlAjNzXoZbPWIGq1%2BpQdlEdSkZXfwxS%2F4ZsMxAd0nJp3BnBegHa3l3Ez4bq6M3%2BIwsqDmvAY6pgGawwDZOo1ookUDwIRHulutgEU1Pq1%2BjufI1fXxFZb8UERy%2F2%2FLKKOuL7x6nQeXDiOF8%2Fdj9u811MZTSBBIBc3Zis3Gj%2F151gyGj7v4zsfsqaGk3mAwTwiFi31B0qE6ca5zFROoCUXmZq%2BgGmI6G4uF58ykUhcdMbLwRF8gSYW5OhuBv9HnpwAguMihqHXaVShXYqSJbv9kqNMtrHdViSzPwsoQ5MXG&X-Amz-Signature=cf4dd5b43d4fdc2006dc484029cac667652b4adaee0003f9f8dbfa45d7108012&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EDVDGUC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIDCTbJGOIgb8RUUbfEYybu%2B7eLP58HPYSvaFErtw39MyAiBuVushVFSE8g2SCeXVC96iCmjQqr1cf7vd7JRCRK%2Fk7iqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRboTpYXl6kk%2FyXkXKtwDNfQHLxOg9mjw8sTdxkNWG2UNGOUjCSZiOh5Z28Tk%2BuCTpqbnaqO9VNYir3mrYQAY7%2FIQgWkdGZGDtrPMv0f6%2FkwFRQkCB5nJvT8ZIYoLNZr3mXh1h7n7En3ekEW1VQldiUFlTJhP7I26vHUTLW6Izr%2Fo9IAGTkAK66Sd43mHO7jokluyAwgTvg9f4PHxDyalPrOuMgUX22kNRTQ3YnLt2EIF8fwtwpk9eGFOxRBrdb%2BJD2y4A%2FafArhv7MqSiKrV7YIEKC1oi8PGTwJkdm8tWN2Xb34YmCVQ%2Fhah9G7Be9lDT%2B5IJjWJQLhuVIzw6%2BNeeQFgrounoJSYB%2FLTbptWC9lZBbsJfvBiLFdR3qpFcdO2M3BUQtnAPUV2YgkGeYo7sU9506PMBhxXyObX9fpgS9aWO7%2Ba1Y0jXNHzWbYknM69EqYb673iND9rQafDi4dVh8XHAOB%2FbOUKbcfbtT5USyJFY69MZNW9VUdA3eJWSKeWTKSa4HjSVRzeUJCRiCikX3mfPtW3f1P3e93ItZIMKeIh0PND9DI3vqsD82eWkCIcLqWIUDK2McA%2FD2krlAjNzXoZbPWIGq1%2BpQdlEdSkZXfwxS%2F4ZsMxAd0nJp3BnBegHa3l3Ez4bq6M3%2BIwsqDmvAY6pgGawwDZOo1ookUDwIRHulutgEU1Pq1%2BjufI1fXxFZb8UERy%2F2%2FLKKOuL7x6nQeXDiOF8%2Fdj9u811MZTSBBIBc3Zis3Gj%2F151gyGj7v4zsfsqaGk3mAwTwiFi31B0qE6ca5zFROoCUXmZq%2BgGmI6G4uF58ykUhcdMbLwRF8gSYW5OhuBv9HnpwAguMihqHXaVShXYqSJbv9kqNMtrHdViSzPwsoQ5MXG&X-Amz-Signature=348f43ee17a80f46440f0c2423313c93f13d86a08d6a31b3f3764668bfcb6a4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EDVDGUC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIDCTbJGOIgb8RUUbfEYybu%2B7eLP58HPYSvaFErtw39MyAiBuVushVFSE8g2SCeXVC96iCmjQqr1cf7vd7JRCRK%2Fk7iqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRboTpYXl6kk%2FyXkXKtwDNfQHLxOg9mjw8sTdxkNWG2UNGOUjCSZiOh5Z28Tk%2BuCTpqbnaqO9VNYir3mrYQAY7%2FIQgWkdGZGDtrPMv0f6%2FkwFRQkCB5nJvT8ZIYoLNZr3mXh1h7n7En3ekEW1VQldiUFlTJhP7I26vHUTLW6Izr%2Fo9IAGTkAK66Sd43mHO7jokluyAwgTvg9f4PHxDyalPrOuMgUX22kNRTQ3YnLt2EIF8fwtwpk9eGFOxRBrdb%2BJD2y4A%2FafArhv7MqSiKrV7YIEKC1oi8PGTwJkdm8tWN2Xb34YmCVQ%2Fhah9G7Be9lDT%2B5IJjWJQLhuVIzw6%2BNeeQFgrounoJSYB%2FLTbptWC9lZBbsJfvBiLFdR3qpFcdO2M3BUQtnAPUV2YgkGeYo7sU9506PMBhxXyObX9fpgS9aWO7%2Ba1Y0jXNHzWbYknM69EqYb673iND9rQafDi4dVh8XHAOB%2FbOUKbcfbtT5USyJFY69MZNW9VUdA3eJWSKeWTKSa4HjSVRzeUJCRiCikX3mfPtW3f1P3e93ItZIMKeIh0PND9DI3vqsD82eWkCIcLqWIUDK2McA%2FD2krlAjNzXoZbPWIGq1%2BpQdlEdSkZXfwxS%2F4ZsMxAd0nJp3BnBegHa3l3Ez4bq6M3%2BIwsqDmvAY6pgGawwDZOo1ookUDwIRHulutgEU1Pq1%2BjufI1fXxFZb8UERy%2F2%2FLKKOuL7x6nQeXDiOF8%2Fdj9u811MZTSBBIBc3Zis3Gj%2F151gyGj7v4zsfsqaGk3mAwTwiFi31B0qE6ca5zFROoCUXmZq%2BgGmI6G4uF58ykUhcdMbLwRF8gSYW5OhuBv9HnpwAguMihqHXaVShXYqSJbv9kqNMtrHdViSzPwsoQ5MXG&X-Amz-Signature=4a9e27df92b77e60c95ac7c0b2b07fe49db851c83978c9495ed9e7a85b936962&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EDVDGUC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIDCTbJGOIgb8RUUbfEYybu%2B7eLP58HPYSvaFErtw39MyAiBuVushVFSE8g2SCeXVC96iCmjQqr1cf7vd7JRCRK%2Fk7iqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRboTpYXl6kk%2FyXkXKtwDNfQHLxOg9mjw8sTdxkNWG2UNGOUjCSZiOh5Z28Tk%2BuCTpqbnaqO9VNYir3mrYQAY7%2FIQgWkdGZGDtrPMv0f6%2FkwFRQkCB5nJvT8ZIYoLNZr3mXh1h7n7En3ekEW1VQldiUFlTJhP7I26vHUTLW6Izr%2Fo9IAGTkAK66Sd43mHO7jokluyAwgTvg9f4PHxDyalPrOuMgUX22kNRTQ3YnLt2EIF8fwtwpk9eGFOxRBrdb%2BJD2y4A%2FafArhv7MqSiKrV7YIEKC1oi8PGTwJkdm8tWN2Xb34YmCVQ%2Fhah9G7Be9lDT%2B5IJjWJQLhuVIzw6%2BNeeQFgrounoJSYB%2FLTbptWC9lZBbsJfvBiLFdR3qpFcdO2M3BUQtnAPUV2YgkGeYo7sU9506PMBhxXyObX9fpgS9aWO7%2Ba1Y0jXNHzWbYknM69EqYb673iND9rQafDi4dVh8XHAOB%2FbOUKbcfbtT5USyJFY69MZNW9VUdA3eJWSKeWTKSa4HjSVRzeUJCRiCikX3mfPtW3f1P3e93ItZIMKeIh0PND9DI3vqsD82eWkCIcLqWIUDK2McA%2FD2krlAjNzXoZbPWIGq1%2BpQdlEdSkZXfwxS%2F4ZsMxAd0nJp3BnBegHa3l3Ez4bq6M3%2BIwsqDmvAY6pgGawwDZOo1ookUDwIRHulutgEU1Pq1%2BjufI1fXxFZb8UERy%2F2%2FLKKOuL7x6nQeXDiOF8%2Fdj9u811MZTSBBIBc3Zis3Gj%2F151gyGj7v4zsfsqaGk3mAwTwiFi31B0qE6ca5zFROoCUXmZq%2BgGmI6G4uF58ykUhcdMbLwRF8gSYW5OhuBv9HnpwAguMihqHXaVShXYqSJbv9kqNMtrHdViSzPwsoQ5MXG&X-Amz-Signature=5ff7cc1e3c2a9cdaa788c8fbcafae24d148e9897348178f25f99ad7cf8de8ac6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZY3LFNQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIE%2FS02BUxdl%2FwM3w1CdggeBuUWS7O1YTnM8PlwR%2BcHw3AiAAstesqjN5PTKx0ZIuynbxvyy7uwfexllcG2tWtiIl1yqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy5nKN4nc2i0Pc6sfKtwDqzaLYwbo96DUi3fPlzDeLV1TsIfhQVf3uNBpx45EWZ7JVr%2Fan%2BJFtDl4nZn%2FdIFg%2BKlQ9qRoNX8OKm5bxIWDXgDdasNemyfL6l5yCWl%2BdE2FDmx1vqy49b%2BYmzUbRyMLFwPfOrwPyLiKo%2FdS%2F9MhTZAgjTt8CLXwxAWv2i45Xnj1zFoFwE%2BQ0nhsDBQg3VPQmS%2BC0rotDiuJJWI8FkP0sIRwavAGvtPbwUWAS1lQ%2BwplunNkj5aLflwgv41eQBqWXHbwOwOfBlNfucfruc3Z9EM4U0qmkRu0pG4ROKuEJXw0e8%2F76T6gxagmlLOglbUedHU8IUVOpm5UatCmGcAkECLdGDV4jUqcL4NVI7h9m7GDrSRDzlUKXe4gj%2FBOef1dERxP6WoweYfNKAtZVz9LArJupPaaYM497KkFRSEJh6Bc7RSF%2FCUlY%2BtH7h%2BMKcUHZLaGannQbM4p1NOqWEbX%2Fphy02hc%2BNF7EeWEIyED3BZRAJuDYTareFmW%2FSWtFRNu4LqwodHbVbgAoEWEgDJPbT7H09JxfbihK%2BqVj2Y%2FPmy4b1bk6lfFQ0GyYMbYBzQIO8DCI%2BFGrDzhC1d9BzoXLCrM9DJVHIfKORm2S4iTjtgYhVoBJQXZCy1GZNswtp%2FmvAY6pgFsiZfYG1FME5ThSwvn9YYkYxOb4MS8RAz%2FXZ7FszJL8J0bWYfPfvmxuesAY%2FX7Sjug9j%2F4XnxIsE8p9E1kMDHOs%2FeABU5uPj1ZoOH8Tla1VioeL0uUyXrchXFXMPq%2FNZEaqVKdkFy8rZwzoSSK19RL6EUc9DnyWkegPcTUaGP6uPVGH9kJByRq6QiYvgp655MU3vV6%2Bf7HhfILYV%2Fpkl%2FHY4ONYq5W&X-Amz-Signature=4ad0b1b3c297c299685f5926d0c46e3794230f1ce962c10e9418d08b094ec057&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJOV4SAE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIG0gzXSn5HbYjYPPRfxWY1deS%2FOzg5%2BqUgJGVMdxwRN6AiAFvzot9kk442w%2Frfkc1KSe5umLre0RyiixwjuBpNBRliqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8Ng2FjfaP%2Bhs2W%2FBKtwDg1sQms5luzRR537DG8E3I8kjbDIv4xBSy%2BrKOG4bQctOVIiHIw9KQ7%2B3QCQnGx9CXHpPgx8nzhnuRUbhC3MLwfGcoskUHpztVv9aGGfXZy%2F9Iw2cId6csAEnsR1mES8m%2F8cznW2WbZV21caSQT4ZNgEqciDuVI1CmK5t4OwONNPb63aGOLgTcgm4GZlgPn6Z952Dpp%2B0BXpAXxfYZ%2FaGCFNSteoTJ63hp1qDxKgLrrC8ZvMxWyMsM9uwzrt3%2BHh9yneyePgX0nkRcosXSgYysBmoheqYWxg90wvrKmSUuvTcSwSBh0qTzAyV8qpleBbW0V0wWBmZMXDJoayOObJD0gaXCwDMl%2FUu9%2Bzk01JaJFBRZkIfCic9Ro0QKvXwAZOckDJwbPfD2CasAcGjrqagSrz8k%2FL8xkJW2gaySNfq%2FxnU%2BpbvXHVIYpsVQBGgfezqPkpoBNJdAWkATfZW8n%2FFyEGnx7SzLfE8Zd97m4EN9vrNqpZXmkF9RCamh9cz0Kw7z%2F490RWRBZ8RzBln6et3qjiK7Wd0XbCqWbxQ3zPAw5%2Ba8jIOofoc7Niv9fX8KqrIyY%2B3LhuGqyvQaIbN2OqsMhcpB9ayMVL6hRcxGOwHZTrLj%2FulN3t6r9K8QVwwqp%2FmvAY6pgEJGhRAX8YbqBbTiv5vp9wW0OgeZZUG926XanDjci762xbKgiiTvFraKi6aD9Iec34ysCxGOZ35aEOjM%2F7%2BSGWsG9IvyKEylL8ERiXD46JVcN3QyttjlbDoNbmNVSCWynxXcACYH614eI%2BQOLks2BFcCyTO5jsJrhb32HI5Lg0YbI3LaIcD33AvSExVBQZoqLH7QvEmOrYTmaW2%2Bz5mfSZCZ5oYrKDb&X-Amz-Signature=09f937a3d5c574ea68279ed15628556faa0f4dde1e5cd3897f1c7992f7bbdc8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZ6KK2L2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIFb3Aard8nh4E2lXO3bjmKt4StER0i4E12pCpifogIg%2FAiBgdLlI%2F4ozhMY%2BvYw5z0kFDxKF0S9oVnCQFLgGGq034yqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME1IPUgJHAgiQwQGLKtwDJ8AOYuM8cX4VEAGYXVb3tXIEpp%2F14t00oztA%2FqHIU3F3ykJUN7i6nCw%2FWH6tmPs9RuPLBOP0WwQKK%2Fq6f%2F2NUZJy%2BBx%2FIK7UaGVl%2BQco%2BBV3THF8wcqPL6kCdZmrW74G%2FsXvKfYNhebzxCVONLh2nGfhUQz1SnyfvOBo9pL%2BvwszS91Aa4xmnsPPzOMex09hIRtJZ2xeejESm03N%2BCvlM20XQwHQDsc%2F2W0b8ENJBVsYJky4ks%2BeZ6PKDld4YqHdK0WpSMLy4JcfVfXhBF%2B1F17gekn5iTiuQxDOWYI3ZWWl1z7a5gqMjp9%2FQHrKpkULGcHgTfGGrb0q2uSNCyUvHHnmTRmEBRCfyhMVnB0cp8pzMUJb6pk8cHTNyLRHeDTeaPDgZk9yLDix5SzvowRqFVuDZarA%2F9Q2zh0YQ%2Fc6Qse4jffP771ApMEoga4dqqqD6jgTJ1JPW%2F3N5AuOcg8iB%2FCG%2BiEEw8nhAixnu5L3xwzLC8kHoKCuXRB6JG%2Fqe4S0C1kIe9i6eJu1AL72wzOF7X%2FW33iy1rK7B34cjSZu%2F8Iaw%2F5IH0tFsnQykPix5DUSMIX67QmRADMvA9wZsPRxP13RG3pXv5h%2BBPU5Y0zafPEZ94%2BSS7%2FHP%2FS35nEwpJ%2FmvAY6pgEgDPMU57Xu%2FI44mrCYXYtK%2BYJ8R03yeuLxqwJZ9hbv4Z%2Fce7w3rqRA9In42%2BKlwKEQR2oyMAqS85%2FdWlsY8s%2B0kHxfKjsnwsSrHEyApZieNDhIocw7rj%2Bh6olfuYkLrIzq9ywnqzKrkDrtzBQ3204vr9SVOCmZcFIkQaB8Qz5C1lW5%2F9TqZvHSTtUdqKj9kdt6OddAWkgOtgwBFp41PcKJE1XXXOey&X-Amz-Signature=3cb51577646c5f013b7742d89588a9f60f014bbb131049bd455844c1dec24232&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZ6KK2L2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIFb3Aard8nh4E2lXO3bjmKt4StER0i4E12pCpifogIg%2FAiBgdLlI%2F4ozhMY%2BvYw5z0kFDxKF0S9oVnCQFLgGGq034yqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME1IPUgJHAgiQwQGLKtwDJ8AOYuM8cX4VEAGYXVb3tXIEpp%2F14t00oztA%2FqHIU3F3ykJUN7i6nCw%2FWH6tmPs9RuPLBOP0WwQKK%2Fq6f%2F2NUZJy%2BBx%2FIK7UaGVl%2BQco%2BBV3THF8wcqPL6kCdZmrW74G%2FsXvKfYNhebzxCVONLh2nGfhUQz1SnyfvOBo9pL%2BvwszS91Aa4xmnsPPzOMex09hIRtJZ2xeejESm03N%2BCvlM20XQwHQDsc%2F2W0b8ENJBVsYJky4ks%2BeZ6PKDld4YqHdK0WpSMLy4JcfVfXhBF%2B1F17gekn5iTiuQxDOWYI3ZWWl1z7a5gqMjp9%2FQHrKpkULGcHgTfGGrb0q2uSNCyUvHHnmTRmEBRCfyhMVnB0cp8pzMUJb6pk8cHTNyLRHeDTeaPDgZk9yLDix5SzvowRqFVuDZarA%2F9Q2zh0YQ%2Fc6Qse4jffP771ApMEoga4dqqqD6jgTJ1JPW%2F3N5AuOcg8iB%2FCG%2BiEEw8nhAixnu5L3xwzLC8kHoKCuXRB6JG%2Fqe4S0C1kIe9i6eJu1AL72wzOF7X%2FW33iy1rK7B34cjSZu%2F8Iaw%2F5IH0tFsnQykPix5DUSMIX67QmRADMvA9wZsPRxP13RG3pXv5h%2BBPU5Y0zafPEZ94%2BSS7%2FHP%2FS35nEwpJ%2FmvAY6pgEgDPMU57Xu%2FI44mrCYXYtK%2BYJ8R03yeuLxqwJZ9hbv4Z%2Fce7w3rqRA9In42%2BKlwKEQR2oyMAqS85%2FdWlsY8s%2B0kHxfKjsnwsSrHEyApZieNDhIocw7rj%2Bh6olfuYkLrIzq9ywnqzKrkDrtzBQ3204vr9SVOCmZcFIkQaB8Qz5C1lW5%2F9TqZvHSTtUdqKj9kdt6OddAWkgOtgwBFp41PcKJE1XXXOey&X-Amz-Signature=843687554b914852d959e4367b4c4ac48d3a101988d0a65b5135e20a513bf087&X-Amz-SignedHeaders=host&x-id=GetObject)
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
