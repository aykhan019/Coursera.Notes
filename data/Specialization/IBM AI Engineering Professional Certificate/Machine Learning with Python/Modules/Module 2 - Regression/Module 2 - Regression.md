

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFM6V56M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEw%2FgKBLWVP8ck%2FTxJi5frTCTxSzFFaACpbnR2fz3oe3AiBTnbQBsSoMtAu%2B7RA3icxvUcPQne5unvv97FU7AvNrISqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIe0yZ7T1SsZ4orZBKtwDoQGtnKCju15u1ri7LLEBzeN%2BrR1QYyMxwXv7T1EFhZsBBrHOQzqsIPXKcfJo3Jm7U3jx68IRDAzwlNzyRrKtdLulqyG3XjwxUaK98QwK0Di%2BMip0RsQ4Qe0AZ5c%2FzCvJFvBzmjoGx32UfrzLEX3Zk0GoiHiq0bc%2BOTd%2FaUWdVAEUZCkSK3pQCybjNwRPdzwKOqTKGlkjPTlHfoI%2BXfMTXvrHxlJ3VCZ2ow%2BPiZs79F31vbdRPgH1IqxScuwQsN97FHaoTdLaPrCKB3%2FU2tB8%2BkGLFAi9Fig0lN%2Bk4UUIIPE%2FLBepPIfm11r64tJGOWp6FQ8O6Jf%2BsZhskIqWnuMz2y%2FG1OLidmAYzSWWs5UKiOXauyzlUFCXazEvJmIEtcuy1yApEyAdOtK1KUjOvqoqmwluw%2F8f7zVhSYXsGYNiQVBI7vOjvM7DZiUmta36pGLnbW2wRFnHzFx96TA5lBLyeqxteH%2BwdcRWyI1okekcMTwRNH%2BsAaS98xLMXG6vpmHCwufpfqaMWsfcyTBZriuMWVo52DGMH1KUR%2BT4SNTqnAtwLLvIaM26DobjhHKti0RPf3zl0N9%2FJazQU1ITOeP6LYkDH3fnS3gmH8whrW9Myzon7DqLPJANjLUsxM8wyMXqvAY6pgGLGcu5AGOnQGQVFvHCz0WYOlGlTAKEqIvLVyezsnM6I9LByXALwRsutaQgchr14ac6yHaSb8EEtWScUxddpw2kXKUEtMXZQKm0BRMKErtz7QpmfWvwhI0dEUjqEa71nTUa%2B3AdERCEVqHgKrF0dZl5v0JNOZWRN335qBvyFQw1miB7lqMSVYhb2%2FvySnUlDlUlAHyml8vnhqyMCVA5pGAfVbqKKpgQ&X-Amz-Signature=c080c28858fafa04fdb149992491c1adc846f3290f9cee6fdb0f614d59f04e1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFM6V56M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEw%2FgKBLWVP8ck%2FTxJi5frTCTxSzFFaACpbnR2fz3oe3AiBTnbQBsSoMtAu%2B7RA3icxvUcPQne5unvv97FU7AvNrISqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIe0yZ7T1SsZ4orZBKtwDoQGtnKCju15u1ri7LLEBzeN%2BrR1QYyMxwXv7T1EFhZsBBrHOQzqsIPXKcfJo3Jm7U3jx68IRDAzwlNzyRrKtdLulqyG3XjwxUaK98QwK0Di%2BMip0RsQ4Qe0AZ5c%2FzCvJFvBzmjoGx32UfrzLEX3Zk0GoiHiq0bc%2BOTd%2FaUWdVAEUZCkSK3pQCybjNwRPdzwKOqTKGlkjPTlHfoI%2BXfMTXvrHxlJ3VCZ2ow%2BPiZs79F31vbdRPgH1IqxScuwQsN97FHaoTdLaPrCKB3%2FU2tB8%2BkGLFAi9Fig0lN%2Bk4UUIIPE%2FLBepPIfm11r64tJGOWp6FQ8O6Jf%2BsZhskIqWnuMz2y%2FG1OLidmAYzSWWs5UKiOXauyzlUFCXazEvJmIEtcuy1yApEyAdOtK1KUjOvqoqmwluw%2F8f7zVhSYXsGYNiQVBI7vOjvM7DZiUmta36pGLnbW2wRFnHzFx96TA5lBLyeqxteH%2BwdcRWyI1okekcMTwRNH%2BsAaS98xLMXG6vpmHCwufpfqaMWsfcyTBZriuMWVo52DGMH1KUR%2BT4SNTqnAtwLLvIaM26DobjhHKti0RPf3zl0N9%2FJazQU1ITOeP6LYkDH3fnS3gmH8whrW9Myzon7DqLPJANjLUsxM8wyMXqvAY6pgGLGcu5AGOnQGQVFvHCz0WYOlGlTAKEqIvLVyezsnM6I9LByXALwRsutaQgchr14ac6yHaSb8EEtWScUxddpw2kXKUEtMXZQKm0BRMKErtz7QpmfWvwhI0dEUjqEa71nTUa%2B3AdERCEVqHgKrF0dZl5v0JNOZWRN335qBvyFQw1miB7lqMSVYhb2%2FvySnUlDlUlAHyml8vnhqyMCVA5pGAfVbqKKpgQ&X-Amz-Signature=8d6f842c677831c317acb8e9f786fe87db2a0e1ba28c73804c66c784ea7fbf9b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFM6V56M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEw%2FgKBLWVP8ck%2FTxJi5frTCTxSzFFaACpbnR2fz3oe3AiBTnbQBsSoMtAu%2B7RA3icxvUcPQne5unvv97FU7AvNrISqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIe0yZ7T1SsZ4orZBKtwDoQGtnKCju15u1ri7LLEBzeN%2BrR1QYyMxwXv7T1EFhZsBBrHOQzqsIPXKcfJo3Jm7U3jx68IRDAzwlNzyRrKtdLulqyG3XjwxUaK98QwK0Di%2BMip0RsQ4Qe0AZ5c%2FzCvJFvBzmjoGx32UfrzLEX3Zk0GoiHiq0bc%2BOTd%2FaUWdVAEUZCkSK3pQCybjNwRPdzwKOqTKGlkjPTlHfoI%2BXfMTXvrHxlJ3VCZ2ow%2BPiZs79F31vbdRPgH1IqxScuwQsN97FHaoTdLaPrCKB3%2FU2tB8%2BkGLFAi9Fig0lN%2Bk4UUIIPE%2FLBepPIfm11r64tJGOWp6FQ8O6Jf%2BsZhskIqWnuMz2y%2FG1OLidmAYzSWWs5UKiOXauyzlUFCXazEvJmIEtcuy1yApEyAdOtK1KUjOvqoqmwluw%2F8f7zVhSYXsGYNiQVBI7vOjvM7DZiUmta36pGLnbW2wRFnHzFx96TA5lBLyeqxteH%2BwdcRWyI1okekcMTwRNH%2BsAaS98xLMXG6vpmHCwufpfqaMWsfcyTBZriuMWVo52DGMH1KUR%2BT4SNTqnAtwLLvIaM26DobjhHKti0RPf3zl0N9%2FJazQU1ITOeP6LYkDH3fnS3gmH8whrW9Myzon7DqLPJANjLUsxM8wyMXqvAY6pgGLGcu5AGOnQGQVFvHCz0WYOlGlTAKEqIvLVyezsnM6I9LByXALwRsutaQgchr14ac6yHaSb8EEtWScUxddpw2kXKUEtMXZQKm0BRMKErtz7QpmfWvwhI0dEUjqEa71nTUa%2B3AdERCEVqHgKrF0dZl5v0JNOZWRN335qBvyFQw1miB7lqMSVYhb2%2FvySnUlDlUlAHyml8vnhqyMCVA5pGAfVbqKKpgQ&X-Amz-Signature=0f4d9c8b1c3860bede1748af3683a523d823db99e978303a63faafa1c37dcdaf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFM6V56M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEw%2FgKBLWVP8ck%2FTxJi5frTCTxSzFFaACpbnR2fz3oe3AiBTnbQBsSoMtAu%2B7RA3icxvUcPQne5unvv97FU7AvNrISqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIe0yZ7T1SsZ4orZBKtwDoQGtnKCju15u1ri7LLEBzeN%2BrR1QYyMxwXv7T1EFhZsBBrHOQzqsIPXKcfJo3Jm7U3jx68IRDAzwlNzyRrKtdLulqyG3XjwxUaK98QwK0Di%2BMip0RsQ4Qe0AZ5c%2FzCvJFvBzmjoGx32UfrzLEX3Zk0GoiHiq0bc%2BOTd%2FaUWdVAEUZCkSK3pQCybjNwRPdzwKOqTKGlkjPTlHfoI%2BXfMTXvrHxlJ3VCZ2ow%2BPiZs79F31vbdRPgH1IqxScuwQsN97FHaoTdLaPrCKB3%2FU2tB8%2BkGLFAi9Fig0lN%2Bk4UUIIPE%2FLBepPIfm11r64tJGOWp6FQ8O6Jf%2BsZhskIqWnuMz2y%2FG1OLidmAYzSWWs5UKiOXauyzlUFCXazEvJmIEtcuy1yApEyAdOtK1KUjOvqoqmwluw%2F8f7zVhSYXsGYNiQVBI7vOjvM7DZiUmta36pGLnbW2wRFnHzFx96TA5lBLyeqxteH%2BwdcRWyI1okekcMTwRNH%2BsAaS98xLMXG6vpmHCwufpfqaMWsfcyTBZriuMWVo52DGMH1KUR%2BT4SNTqnAtwLLvIaM26DobjhHKti0RPf3zl0N9%2FJazQU1ITOeP6LYkDH3fnS3gmH8whrW9Myzon7DqLPJANjLUsxM8wyMXqvAY6pgGLGcu5AGOnQGQVFvHCz0WYOlGlTAKEqIvLVyezsnM6I9LByXALwRsutaQgchr14ac6yHaSb8EEtWScUxddpw2kXKUEtMXZQKm0BRMKErtz7QpmfWvwhI0dEUjqEa71nTUa%2B3AdERCEVqHgKrF0dZl5v0JNOZWRN335qBvyFQw1miB7lqMSVYhb2%2FvySnUlDlUlAHyml8vnhqyMCVA5pGAfVbqKKpgQ&X-Amz-Signature=b2ac1ebff187f5acb210d5ceee01ddf685fd20e2dcd8d711620a915cabb2fb1b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFM6V56M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEw%2FgKBLWVP8ck%2FTxJi5frTCTxSzFFaACpbnR2fz3oe3AiBTnbQBsSoMtAu%2B7RA3icxvUcPQne5unvv97FU7AvNrISqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIe0yZ7T1SsZ4orZBKtwDoQGtnKCju15u1ri7LLEBzeN%2BrR1QYyMxwXv7T1EFhZsBBrHOQzqsIPXKcfJo3Jm7U3jx68IRDAzwlNzyRrKtdLulqyG3XjwxUaK98QwK0Di%2BMip0RsQ4Qe0AZ5c%2FzCvJFvBzmjoGx32UfrzLEX3Zk0GoiHiq0bc%2BOTd%2FaUWdVAEUZCkSK3pQCybjNwRPdzwKOqTKGlkjPTlHfoI%2BXfMTXvrHxlJ3VCZ2ow%2BPiZs79F31vbdRPgH1IqxScuwQsN97FHaoTdLaPrCKB3%2FU2tB8%2BkGLFAi9Fig0lN%2Bk4UUIIPE%2FLBepPIfm11r64tJGOWp6FQ8O6Jf%2BsZhskIqWnuMz2y%2FG1OLidmAYzSWWs5UKiOXauyzlUFCXazEvJmIEtcuy1yApEyAdOtK1KUjOvqoqmwluw%2F8f7zVhSYXsGYNiQVBI7vOjvM7DZiUmta36pGLnbW2wRFnHzFx96TA5lBLyeqxteH%2BwdcRWyI1okekcMTwRNH%2BsAaS98xLMXG6vpmHCwufpfqaMWsfcyTBZriuMWVo52DGMH1KUR%2BT4SNTqnAtwLLvIaM26DobjhHKti0RPf3zl0N9%2FJazQU1ITOeP6LYkDH3fnS3gmH8whrW9Myzon7DqLPJANjLUsxM8wyMXqvAY6pgGLGcu5AGOnQGQVFvHCz0WYOlGlTAKEqIvLVyezsnM6I9LByXALwRsutaQgchr14ac6yHaSb8EEtWScUxddpw2kXKUEtMXZQKm0BRMKErtz7QpmfWvwhI0dEUjqEa71nTUa%2B3AdERCEVqHgKrF0dZl5v0JNOZWRN335qBvyFQw1miB7lqMSVYhb2%2FvySnUlDlUlAHyml8vnhqyMCVA5pGAfVbqKKpgQ&X-Amz-Signature=fe530e19d6212cfb88c27894eb00a32864d6ff5a05a9d03755177a6280111a32&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFM6V56M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEw%2FgKBLWVP8ck%2FTxJi5frTCTxSzFFaACpbnR2fz3oe3AiBTnbQBsSoMtAu%2B7RA3icxvUcPQne5unvv97FU7AvNrISqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIe0yZ7T1SsZ4orZBKtwDoQGtnKCju15u1ri7LLEBzeN%2BrR1QYyMxwXv7T1EFhZsBBrHOQzqsIPXKcfJo3Jm7U3jx68IRDAzwlNzyRrKtdLulqyG3XjwxUaK98QwK0Di%2BMip0RsQ4Qe0AZ5c%2FzCvJFvBzmjoGx32UfrzLEX3Zk0GoiHiq0bc%2BOTd%2FaUWdVAEUZCkSK3pQCybjNwRPdzwKOqTKGlkjPTlHfoI%2BXfMTXvrHxlJ3VCZ2ow%2BPiZs79F31vbdRPgH1IqxScuwQsN97FHaoTdLaPrCKB3%2FU2tB8%2BkGLFAi9Fig0lN%2Bk4UUIIPE%2FLBepPIfm11r64tJGOWp6FQ8O6Jf%2BsZhskIqWnuMz2y%2FG1OLidmAYzSWWs5UKiOXauyzlUFCXazEvJmIEtcuy1yApEyAdOtK1KUjOvqoqmwluw%2F8f7zVhSYXsGYNiQVBI7vOjvM7DZiUmta36pGLnbW2wRFnHzFx96TA5lBLyeqxteH%2BwdcRWyI1okekcMTwRNH%2BsAaS98xLMXG6vpmHCwufpfqaMWsfcyTBZriuMWVo52DGMH1KUR%2BT4SNTqnAtwLLvIaM26DobjhHKti0RPf3zl0N9%2FJazQU1ITOeP6LYkDH3fnS3gmH8whrW9Myzon7DqLPJANjLUsxM8wyMXqvAY6pgGLGcu5AGOnQGQVFvHCz0WYOlGlTAKEqIvLVyezsnM6I9LByXALwRsutaQgchr14ac6yHaSb8EEtWScUxddpw2kXKUEtMXZQKm0BRMKErtz7QpmfWvwhI0dEUjqEa71nTUa%2B3AdERCEVqHgKrF0dZl5v0JNOZWRN335qBvyFQw1miB7lqMSVYhb2%2FvySnUlDlUlAHyml8vnhqyMCVA5pGAfVbqKKpgQ&X-Amz-Signature=74cfabe853be02699c20b32786c7885c3b933dece246197bacfaf62d3a1687c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFM6V56M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEw%2FgKBLWVP8ck%2FTxJi5frTCTxSzFFaACpbnR2fz3oe3AiBTnbQBsSoMtAu%2B7RA3icxvUcPQne5unvv97FU7AvNrISqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIe0yZ7T1SsZ4orZBKtwDoQGtnKCju15u1ri7LLEBzeN%2BrR1QYyMxwXv7T1EFhZsBBrHOQzqsIPXKcfJo3Jm7U3jx68IRDAzwlNzyRrKtdLulqyG3XjwxUaK98QwK0Di%2BMip0RsQ4Qe0AZ5c%2FzCvJFvBzmjoGx32UfrzLEX3Zk0GoiHiq0bc%2BOTd%2FaUWdVAEUZCkSK3pQCybjNwRPdzwKOqTKGlkjPTlHfoI%2BXfMTXvrHxlJ3VCZ2ow%2BPiZs79F31vbdRPgH1IqxScuwQsN97FHaoTdLaPrCKB3%2FU2tB8%2BkGLFAi9Fig0lN%2Bk4UUIIPE%2FLBepPIfm11r64tJGOWp6FQ8O6Jf%2BsZhskIqWnuMz2y%2FG1OLidmAYzSWWs5UKiOXauyzlUFCXazEvJmIEtcuy1yApEyAdOtK1KUjOvqoqmwluw%2F8f7zVhSYXsGYNiQVBI7vOjvM7DZiUmta36pGLnbW2wRFnHzFx96TA5lBLyeqxteH%2BwdcRWyI1okekcMTwRNH%2BsAaS98xLMXG6vpmHCwufpfqaMWsfcyTBZriuMWVo52DGMH1KUR%2BT4SNTqnAtwLLvIaM26DobjhHKti0RPf3zl0N9%2FJazQU1ITOeP6LYkDH3fnS3gmH8whrW9Myzon7DqLPJANjLUsxM8wyMXqvAY6pgGLGcu5AGOnQGQVFvHCz0WYOlGlTAKEqIvLVyezsnM6I9LByXALwRsutaQgchr14ac6yHaSb8EEtWScUxddpw2kXKUEtMXZQKm0BRMKErtz7QpmfWvwhI0dEUjqEa71nTUa%2B3AdERCEVqHgKrF0dZl5v0JNOZWRN335qBvyFQw1miB7lqMSVYhb2%2FvySnUlDlUlAHyml8vnhqyMCVA5pGAfVbqKKpgQ&X-Amz-Signature=944e7ab89bac2bdb01881d4ca63ae36b3157032b7eede48e76111d58cf2b7292&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFM6V56M%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEw%2FgKBLWVP8ck%2FTxJi5frTCTxSzFFaACpbnR2fz3oe3AiBTnbQBsSoMtAu%2B7RA3icxvUcPQne5unvv97FU7AvNrISqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIe0yZ7T1SsZ4orZBKtwDoQGtnKCju15u1ri7LLEBzeN%2BrR1QYyMxwXv7T1EFhZsBBrHOQzqsIPXKcfJo3Jm7U3jx68IRDAzwlNzyRrKtdLulqyG3XjwxUaK98QwK0Di%2BMip0RsQ4Qe0AZ5c%2FzCvJFvBzmjoGx32UfrzLEX3Zk0GoiHiq0bc%2BOTd%2FaUWdVAEUZCkSK3pQCybjNwRPdzwKOqTKGlkjPTlHfoI%2BXfMTXvrHxlJ3VCZ2ow%2BPiZs79F31vbdRPgH1IqxScuwQsN97FHaoTdLaPrCKB3%2FU2tB8%2BkGLFAi9Fig0lN%2Bk4UUIIPE%2FLBepPIfm11r64tJGOWp6FQ8O6Jf%2BsZhskIqWnuMz2y%2FG1OLidmAYzSWWs5UKiOXauyzlUFCXazEvJmIEtcuy1yApEyAdOtK1KUjOvqoqmwluw%2F8f7zVhSYXsGYNiQVBI7vOjvM7DZiUmta36pGLnbW2wRFnHzFx96TA5lBLyeqxteH%2BwdcRWyI1okekcMTwRNH%2BsAaS98xLMXG6vpmHCwufpfqaMWsfcyTBZriuMWVo52DGMH1KUR%2BT4SNTqnAtwLLvIaM26DobjhHKti0RPf3zl0N9%2FJazQU1ITOeP6LYkDH3fnS3gmH8whrW9Myzon7DqLPJANjLUsxM8wyMXqvAY6pgGLGcu5AGOnQGQVFvHCz0WYOlGlTAKEqIvLVyezsnM6I9LByXALwRsutaQgchr14ac6yHaSb8EEtWScUxddpw2kXKUEtMXZQKm0BRMKErtz7QpmfWvwhI0dEUjqEa71nTUa%2B3AdERCEVqHgKrF0dZl5v0JNOZWRN335qBvyFQw1miB7lqMSVYhb2%2FvySnUlDlUlAHyml8vnhqyMCVA5pGAfVbqKKpgQ&X-Amz-Signature=45ea9c508cc20ad88c80bdfc6f242ed4c3522deedf95f1a07d7badfcd4a21a2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZISYLFD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAYUU0JfwTnEkf0npRrqAPsVrT2Y6dXV70aM9CRAk8BAiA%2F5JmcuLeKwBMDAxNqjSbLA2AKJaaVkU9hZKCCq8gSwyqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHReyVikEpuNRk5gbKtwD46tSuYEtd2F2CMzPcUNxv0XHxMzdE%2B8LyIvBI6rV9ZQlPyB0kphZrqJ4Re7xqezrRC%2F0o9UIgKFNsdyr2JCjvAsGGqJJ5hb6m4euKlpXxXbxZbobVv4vZwZWhfCpArCZUmremoEIR1GRpbj7Ip3k1C0loVctEmRnT72XKyK2xGU5ex%2FbRvS0pJMirqSvXqTIN8PZlWg8coc0Z1ld7UFLHLkrqYmg0biEa2iikp8db%2FBfoTvIZHQNJsqGv2CWNSFYkMSX6vXYhUdMHCAwzp7nnR6%2Fh1Rs13J2HRFm5XHuqV2d7Wr%2BOHRMLra2c5dhqKB1nSEIFdP14MtnFRBqi9WC9rWniTZUQU6q8LbUGQdGdSvp4zDkuiO%2F4UFrEDG%2BcpqH3M%2Fu4sjVSExTWwQ3shyiNthUS2OvPow5yeAmQ5uVo0mzKLKQ%2FIfHZd1FgNA2V1htEogZRXRuJop7bMvpo7sRizg8kdCmsajoNxCevV%2Bn9SbDEKbcY%2BqAftxmfLgQcxsMfsvB7jocTx%2B2rLno%2F3SZWvFoc2IfLefwoneDjWkw9uHuydV%2BMzkzARPm8LTD8o7v%2FlAccv5bPgaQ1Q4%2B0YSgjGrY%2F6VrwRRZG762qY8ee5yQnfltI8U2uC4WtbowtMXqvAY6pgGps0D5A%2Bl2uuntplxx9vTj5lT%2FtdxGkzvyJD0zcAnVrOl5gbEEZzJdD4vkEk22fFRdGYzzo1OTImGWcDMfoI%2FTYqSX2WREBzlAXY7OkG9wpe67zckED745zgvgRNlSVs2%2FBiNImMnZ17TA4us5l2juoqrJPcnK3wHGLg4v8doTRGAVxg8lU5tfS76nU6n4%2FZcQPO3Ua9sBzM%2BTQRK2c5lJJw8XmIk6&X-Amz-Signature=e2febb3d7e03601886c01d754a2dd9f4bfc4ca1707eac2d4a9b35e69b9ed9da7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI2XZNN7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsJ6EhX9C8s8HXDI1XmWzt9a%2BhWvq%2Bnosajv4ijcyT8AiEA3unZVkqJQ6BzRNJxkHRflccj1%2BC%2Bs6xJX6XCUP4QJq0qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFYKj70SxRJfUj9WLCrcAwTO0oI04lKr8a35d2eMOe9OhRnSdo1uPMZhDgkFnraQ8GqUrBZbiTknt%2FQBxmA5%2BY8w%2FJpb1x5f9tGhkt2ZurnbtdurBwC1gbmxTmTGXB0WJUDwMiS0CMi0K0%2ByA0VRN9iNVriSWeMu%2FRsJHmr4YkkgdJ0D8bLmKAPojIbgL3%2BEmT48feC6Bncpxcw53mCPR3JwT4lh0%2BlHw1Hc8Y5MGNTTEiwX8H2EfgFDMYak2%2FVSIx1tOG8XCimpvJPsGj%2FdF5QjcfP40yLTOjpoVA%2Fce%2FMYoXYQcwxGU7V3c9%2B3WZWI9PrEPN%2B%2FT36NsFMQdN1ubO2XGbMJrtoi7EbHJY6%2FWucf67q%2BThWxNzANANIlDoRBG52Geqq08u18C4nSytHKaPwW9%2BzuFiPEVyHgiHZUrbFfIduS53bnYtEiNplrAvPXUTpagZFxR624Ip9Kl4oI2VJlGB5%2FiLRsFo%2BRYqEnanMimO6L9iMhQ3Z0Vk0oe2oSrnysBE7c9BDZBhzCA12uF554Q1dtZaj1cFTDWP35TfXmcekxGDI2D6dM%2B8q6wrxZTYoxvkVEdy%2Fy4JPv87W1WT841yNGUT1%2BTQDdNGdapA2cNUuzUHnIVTiOfQB92SC75LYlmh3BlGO5%2BVZOMPTG6rwGOqUBDUWTIOZo0DnLGJDqYFX6wKZS3eotF2p3ApOR5grFoRVk4qPcTiAvcElWLq4cN5%2FqreK6GoQOg7fEw09BTboEf%2BvItHvsPdghr%2BCebvw1VYynYoXJoUDAyPVTPB4Oncvc27Wg18aD5%2BeW8wY0hIEYZlmNdmkJgAr14kNhc3gOJHqDREuNbtbxAIlTe4fhcIOAySnFAEDtwmOBoyFAg9rP0PJG8Zqr&X-Amz-Signature=dfcb8a1ffe8ca202ceefa1d8d69dbb868b34417a1b3ca6ca74ce9ab1781ebad7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KIUE4VC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBCv8SPwzeexf%2FtVZNDHhCh5bHauL2o8h7iXwI1x1gb7AiAS9BbJP9PS%2FVyiOK3ceRBOdObTVEAEhZp2JqgzgsC0miqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNy%2FBRNvHmmN%2BIDMYKtwDrj1KNkaadJg9%2FO75ptZ%2FCvJzEAX2QmJ0MQnSTWxF%2BxqcHja5Ab%2FDh5%2FqxFm5gNmoVzrhxEWyKvIxcZxuNkSX5SqOcU7OGL1dBO6HlOUnMGEtBUnwNC6aPt33LUKPi1LvmqHd6q2mIagaRmjx66C1SosF27RwenA6owjPYVf7mZzlTsGiSk7pgyNMfskDIyb2XebiapP5leZRkhiM4nFVMo4ABi3ZDmS9Moy%2FE5fUguRWKh%2BaJIgHwfYWT8po0BjBFIRphaQNrBppKhsMxnlCqT7kpM8LlKv%2FUAHo4f%2BrnzNioq6fM89I6n6HzI9SoCIZBP0Q6%2Fhs%2Fiqn9Tv59n35DELTCN9U%2BVfyLBhi%2Fh4eFfuE7ufxqFQ2X8DPUAtrNuUfvAQPEouJEjtuBFSBkaGQms1VS2h1p8ecwWDJwvbqBZ4y483KQI5n6u5ObHXYhEp1mRs9oIuvZyBgdUyqqG1UU9KbsDhy2F%2FxfakwS43MwIXXGq0oC771XuVpYHJEmHEq7rneWjEHwe5E0mY4lNVqFA42IdzTXe5qlbdjYzIngd7peKt%2Bmpb8BHCKL2Nt4b5qHdkNuqZMedko4vdGtrh1UMXzGqZFlsHYZKgxvEIruPNkO3eq0kGtLQgKnqcwysXqvAY6pgHQuCo4I8jljk2gV%2BGwVhVt0YJqeDUr3qt7oSjgg19yNB1QlWdO6YGjjVvkcQI11evGprCMJC5GW%2FS3yle1x3VzfarKnaMrZxgnFfCyGc%2BvkxJnGyHY9lqnXLYxpnxrgSeRMv1Q3diss5HG262nHxRhrY75vOBymq2cgSzfuuoeS5W77x7%2FDCsY5XEwLch6Gx9cHJZD%2Bzx%2B2oPvikUAt3TgMBnyF4Xi&X-Amz-Signature=0bd3f27dc4c5cbca69bcb8f3bf8dc279471c69bb83bdc2661746319f5121f479&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KIUE4VC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBCv8SPwzeexf%2FtVZNDHhCh5bHauL2o8h7iXwI1x1gb7AiAS9BbJP9PS%2FVyiOK3ceRBOdObTVEAEhZp2JqgzgsC0miqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNy%2FBRNvHmmN%2BIDMYKtwDrj1KNkaadJg9%2FO75ptZ%2FCvJzEAX2QmJ0MQnSTWxF%2BxqcHja5Ab%2FDh5%2FqxFm5gNmoVzrhxEWyKvIxcZxuNkSX5SqOcU7OGL1dBO6HlOUnMGEtBUnwNC6aPt33LUKPi1LvmqHd6q2mIagaRmjx66C1SosF27RwenA6owjPYVf7mZzlTsGiSk7pgyNMfskDIyb2XebiapP5leZRkhiM4nFVMo4ABi3ZDmS9Moy%2FE5fUguRWKh%2BaJIgHwfYWT8po0BjBFIRphaQNrBppKhsMxnlCqT7kpM8LlKv%2FUAHo4f%2BrnzNioq6fM89I6n6HzI9SoCIZBP0Q6%2Fhs%2Fiqn9Tv59n35DELTCN9U%2BVfyLBhi%2Fh4eFfuE7ufxqFQ2X8DPUAtrNuUfvAQPEouJEjtuBFSBkaGQms1VS2h1p8ecwWDJwvbqBZ4y483KQI5n6u5ObHXYhEp1mRs9oIuvZyBgdUyqqG1UU9KbsDhy2F%2FxfakwS43MwIXXGq0oC771XuVpYHJEmHEq7rneWjEHwe5E0mY4lNVqFA42IdzTXe5qlbdjYzIngd7peKt%2Bmpb8BHCKL2Nt4b5qHdkNuqZMedko4vdGtrh1UMXzGqZFlsHYZKgxvEIruPNkO3eq0kGtLQgKnqcwysXqvAY6pgHQuCo4I8jljk2gV%2BGwVhVt0YJqeDUr3qt7oSjgg19yNB1QlWdO6YGjjVvkcQI11evGprCMJC5GW%2FS3yle1x3VzfarKnaMrZxgnFfCyGc%2BvkxJnGyHY9lqnXLYxpnxrgSeRMv1Q3diss5HG262nHxRhrY75vOBymq2cgSzfuuoeS5W77x7%2FDCsY5XEwLch6Gx9cHJZD%2Bzx%2B2oPvikUAt3TgMBnyF4Xi&X-Amz-Signature=64b7574c10bd68367e8b7306592a50a2665aab6e149917e4292cf178a39eea4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
