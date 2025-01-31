

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK4MQ4J2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBRCVNI3OZwb8k%2FLNFqlaGkMwsIeuxrbhPclJtbLyCzvAiBauMqBOiMrHsknWAqY1ethO8KiC4KlKftMDKSbW30y0CqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSWOqkCMNsevOZ2CdKtwDwPZsCaN36AtduTABIyNInWI6P1WDI%2Fx602tv61ZoavGGIFyv520x7CG9DkZPHc%2FF%2BQ%2Fl1aaoMPj9%2FcBQOVndxmcdIKAQAnFDnk9qZ42xctkoard86xN8fA2eWMuNkcCPQ%2FcAaCU11gZNq%2FRNrooSpWHEnmfsmH1YLZm1zBFybnD%2Bb%2FY70k%2BjtW1zAgQs%2BiQkcdL39sraziEkLWFpB3t62U%2Fs%2BsVedxehlLO1ZsHxxWbGIiDpkOo33Pn843%2BcU1Lw1kdt3rlnnVJcRkgLYEbsWr8OB6lpRQkfMATclWj6kYZHJVRoS8cQociM09EYExdifdPNjdV40oCxXzX8JyVq5qeFCJv2X1bU%2FJG1iw1F43znqgn3vQPK2udMfTylq%2BeDIMaMDqMwTb3RZGTz7ZArVvuAkoOU4Q7yJjIVDnv1tddR59Awu4Yr041N8%2BDLZ%2F5VzssLDyfgwmhmYJFali%2BWqn7YbI8B%2FdxX9vaCgC%2BwFYW4ZsWQath2B80dnZTfyB768G7020dajuUIdHVw7royJVYy%2FUv1QsgKyD3aSJRFOS3vh%2BCklgVNhUHv3z%2BBHi4N9SVmeO66OWv%2BMmHXd552gS2b13ow5N1o3%2BHTXzFuZGEydNh9POi7y%2BjF4PswjJT1vAY6pgFSIiMWCmYgdFHOaDYgAlkEn43kdN6vhymO7BRzEQnoDGvFGT%2B%2F9HIk0yQWOmoLu1GyLs5gTNx25iC3Kri3YwIGo3csP4lk1rce7cQBofhZzWRToMp0%2F581vlKhflcSC5rtbmP7vAbDdtcOUBF6MgAt8TjuE3yA0%2B9jqItjSU%2FpVDpQfadefBsYX54QTxMJRmLuMrYG49PdUSx%2BQT9LkYizbuMkQpbH&X-Amz-Signature=4890e12a601b49af7a690ea057c8c45650ccfe9b7fbf766458e323b9b1c91962&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK4MQ4J2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBRCVNI3OZwb8k%2FLNFqlaGkMwsIeuxrbhPclJtbLyCzvAiBauMqBOiMrHsknWAqY1ethO8KiC4KlKftMDKSbW30y0CqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSWOqkCMNsevOZ2CdKtwDwPZsCaN36AtduTABIyNInWI6P1WDI%2Fx602tv61ZoavGGIFyv520x7CG9DkZPHc%2FF%2BQ%2Fl1aaoMPj9%2FcBQOVndxmcdIKAQAnFDnk9qZ42xctkoard86xN8fA2eWMuNkcCPQ%2FcAaCU11gZNq%2FRNrooSpWHEnmfsmH1YLZm1zBFybnD%2Bb%2FY70k%2BjtW1zAgQs%2BiQkcdL39sraziEkLWFpB3t62U%2Fs%2BsVedxehlLO1ZsHxxWbGIiDpkOo33Pn843%2BcU1Lw1kdt3rlnnVJcRkgLYEbsWr8OB6lpRQkfMATclWj6kYZHJVRoS8cQociM09EYExdifdPNjdV40oCxXzX8JyVq5qeFCJv2X1bU%2FJG1iw1F43znqgn3vQPK2udMfTylq%2BeDIMaMDqMwTb3RZGTz7ZArVvuAkoOU4Q7yJjIVDnv1tddR59Awu4Yr041N8%2BDLZ%2F5VzssLDyfgwmhmYJFali%2BWqn7YbI8B%2FdxX9vaCgC%2BwFYW4ZsWQath2B80dnZTfyB768G7020dajuUIdHVw7royJVYy%2FUv1QsgKyD3aSJRFOS3vh%2BCklgVNhUHv3z%2BBHi4N9SVmeO66OWv%2BMmHXd552gS2b13ow5N1o3%2BHTXzFuZGEydNh9POi7y%2BjF4PswjJT1vAY6pgFSIiMWCmYgdFHOaDYgAlkEn43kdN6vhymO7BRzEQnoDGvFGT%2B%2F9HIk0yQWOmoLu1GyLs5gTNx25iC3Kri3YwIGo3csP4lk1rce7cQBofhZzWRToMp0%2F581vlKhflcSC5rtbmP7vAbDdtcOUBF6MgAt8TjuE3yA0%2B9jqItjSU%2FpVDpQfadefBsYX54QTxMJRmLuMrYG49PdUSx%2BQT9LkYizbuMkQpbH&X-Amz-Signature=90d0f564d25901a93327bbc1330164fd1032dc760b1b93a3574bbc09c0080c93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK4MQ4J2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBRCVNI3OZwb8k%2FLNFqlaGkMwsIeuxrbhPclJtbLyCzvAiBauMqBOiMrHsknWAqY1ethO8KiC4KlKftMDKSbW30y0CqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSWOqkCMNsevOZ2CdKtwDwPZsCaN36AtduTABIyNInWI6P1WDI%2Fx602tv61ZoavGGIFyv520x7CG9DkZPHc%2FF%2BQ%2Fl1aaoMPj9%2FcBQOVndxmcdIKAQAnFDnk9qZ42xctkoard86xN8fA2eWMuNkcCPQ%2FcAaCU11gZNq%2FRNrooSpWHEnmfsmH1YLZm1zBFybnD%2Bb%2FY70k%2BjtW1zAgQs%2BiQkcdL39sraziEkLWFpB3t62U%2Fs%2BsVedxehlLO1ZsHxxWbGIiDpkOo33Pn843%2BcU1Lw1kdt3rlnnVJcRkgLYEbsWr8OB6lpRQkfMATclWj6kYZHJVRoS8cQociM09EYExdifdPNjdV40oCxXzX8JyVq5qeFCJv2X1bU%2FJG1iw1F43znqgn3vQPK2udMfTylq%2BeDIMaMDqMwTb3RZGTz7ZArVvuAkoOU4Q7yJjIVDnv1tddR59Awu4Yr041N8%2BDLZ%2F5VzssLDyfgwmhmYJFali%2BWqn7YbI8B%2FdxX9vaCgC%2BwFYW4ZsWQath2B80dnZTfyB768G7020dajuUIdHVw7royJVYy%2FUv1QsgKyD3aSJRFOS3vh%2BCklgVNhUHv3z%2BBHi4N9SVmeO66OWv%2BMmHXd552gS2b13ow5N1o3%2BHTXzFuZGEydNh9POi7y%2BjF4PswjJT1vAY6pgFSIiMWCmYgdFHOaDYgAlkEn43kdN6vhymO7BRzEQnoDGvFGT%2B%2F9HIk0yQWOmoLu1GyLs5gTNx25iC3Kri3YwIGo3csP4lk1rce7cQBofhZzWRToMp0%2F581vlKhflcSC5rtbmP7vAbDdtcOUBF6MgAt8TjuE3yA0%2B9jqItjSU%2FpVDpQfadefBsYX54QTxMJRmLuMrYG49PdUSx%2BQT9LkYizbuMkQpbH&X-Amz-Signature=f24d85bdcd91760968c929c7fae9000ee5f41b5a8d8311a3eb43c445eb7b4c14&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK4MQ4J2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBRCVNI3OZwb8k%2FLNFqlaGkMwsIeuxrbhPclJtbLyCzvAiBauMqBOiMrHsknWAqY1ethO8KiC4KlKftMDKSbW30y0CqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSWOqkCMNsevOZ2CdKtwDwPZsCaN36AtduTABIyNInWI6P1WDI%2Fx602tv61ZoavGGIFyv520x7CG9DkZPHc%2FF%2BQ%2Fl1aaoMPj9%2FcBQOVndxmcdIKAQAnFDnk9qZ42xctkoard86xN8fA2eWMuNkcCPQ%2FcAaCU11gZNq%2FRNrooSpWHEnmfsmH1YLZm1zBFybnD%2Bb%2FY70k%2BjtW1zAgQs%2BiQkcdL39sraziEkLWFpB3t62U%2Fs%2BsVedxehlLO1ZsHxxWbGIiDpkOo33Pn843%2BcU1Lw1kdt3rlnnVJcRkgLYEbsWr8OB6lpRQkfMATclWj6kYZHJVRoS8cQociM09EYExdifdPNjdV40oCxXzX8JyVq5qeFCJv2X1bU%2FJG1iw1F43znqgn3vQPK2udMfTylq%2BeDIMaMDqMwTb3RZGTz7ZArVvuAkoOU4Q7yJjIVDnv1tddR59Awu4Yr041N8%2BDLZ%2F5VzssLDyfgwmhmYJFali%2BWqn7YbI8B%2FdxX9vaCgC%2BwFYW4ZsWQath2B80dnZTfyB768G7020dajuUIdHVw7royJVYy%2FUv1QsgKyD3aSJRFOS3vh%2BCklgVNhUHv3z%2BBHi4N9SVmeO66OWv%2BMmHXd552gS2b13ow5N1o3%2BHTXzFuZGEydNh9POi7y%2BjF4PswjJT1vAY6pgFSIiMWCmYgdFHOaDYgAlkEn43kdN6vhymO7BRzEQnoDGvFGT%2B%2F9HIk0yQWOmoLu1GyLs5gTNx25iC3Kri3YwIGo3csP4lk1rce7cQBofhZzWRToMp0%2F581vlKhflcSC5rtbmP7vAbDdtcOUBF6MgAt8TjuE3yA0%2B9jqItjSU%2FpVDpQfadefBsYX54QTxMJRmLuMrYG49PdUSx%2BQT9LkYizbuMkQpbH&X-Amz-Signature=dc6bf18ab3012428d2f77b022a562944c615bc57d09ebee4a157113bc6dbe6d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK4MQ4J2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBRCVNI3OZwb8k%2FLNFqlaGkMwsIeuxrbhPclJtbLyCzvAiBauMqBOiMrHsknWAqY1ethO8KiC4KlKftMDKSbW30y0CqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSWOqkCMNsevOZ2CdKtwDwPZsCaN36AtduTABIyNInWI6P1WDI%2Fx602tv61ZoavGGIFyv520x7CG9DkZPHc%2FF%2BQ%2Fl1aaoMPj9%2FcBQOVndxmcdIKAQAnFDnk9qZ42xctkoard86xN8fA2eWMuNkcCPQ%2FcAaCU11gZNq%2FRNrooSpWHEnmfsmH1YLZm1zBFybnD%2Bb%2FY70k%2BjtW1zAgQs%2BiQkcdL39sraziEkLWFpB3t62U%2Fs%2BsVedxehlLO1ZsHxxWbGIiDpkOo33Pn843%2BcU1Lw1kdt3rlnnVJcRkgLYEbsWr8OB6lpRQkfMATclWj6kYZHJVRoS8cQociM09EYExdifdPNjdV40oCxXzX8JyVq5qeFCJv2X1bU%2FJG1iw1F43znqgn3vQPK2udMfTylq%2BeDIMaMDqMwTb3RZGTz7ZArVvuAkoOU4Q7yJjIVDnv1tddR59Awu4Yr041N8%2BDLZ%2F5VzssLDyfgwmhmYJFali%2BWqn7YbI8B%2FdxX9vaCgC%2BwFYW4ZsWQath2B80dnZTfyB768G7020dajuUIdHVw7royJVYy%2FUv1QsgKyD3aSJRFOS3vh%2BCklgVNhUHv3z%2BBHi4N9SVmeO66OWv%2BMmHXd552gS2b13ow5N1o3%2BHTXzFuZGEydNh9POi7y%2BjF4PswjJT1vAY6pgFSIiMWCmYgdFHOaDYgAlkEn43kdN6vhymO7BRzEQnoDGvFGT%2B%2F9HIk0yQWOmoLu1GyLs5gTNx25iC3Kri3YwIGo3csP4lk1rce7cQBofhZzWRToMp0%2F581vlKhflcSC5rtbmP7vAbDdtcOUBF6MgAt8TjuE3yA0%2B9jqItjSU%2FpVDpQfadefBsYX54QTxMJRmLuMrYG49PdUSx%2BQT9LkYizbuMkQpbH&X-Amz-Signature=5687d6b8fe65edb6d2f27d10ed467bf142cc6ed89356a3598701e6602aa0d6b2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK4MQ4J2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBRCVNI3OZwb8k%2FLNFqlaGkMwsIeuxrbhPclJtbLyCzvAiBauMqBOiMrHsknWAqY1ethO8KiC4KlKftMDKSbW30y0CqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSWOqkCMNsevOZ2CdKtwDwPZsCaN36AtduTABIyNInWI6P1WDI%2Fx602tv61ZoavGGIFyv520x7CG9DkZPHc%2FF%2BQ%2Fl1aaoMPj9%2FcBQOVndxmcdIKAQAnFDnk9qZ42xctkoard86xN8fA2eWMuNkcCPQ%2FcAaCU11gZNq%2FRNrooSpWHEnmfsmH1YLZm1zBFybnD%2Bb%2FY70k%2BjtW1zAgQs%2BiQkcdL39sraziEkLWFpB3t62U%2Fs%2BsVedxehlLO1ZsHxxWbGIiDpkOo33Pn843%2BcU1Lw1kdt3rlnnVJcRkgLYEbsWr8OB6lpRQkfMATclWj6kYZHJVRoS8cQociM09EYExdifdPNjdV40oCxXzX8JyVq5qeFCJv2X1bU%2FJG1iw1F43znqgn3vQPK2udMfTylq%2BeDIMaMDqMwTb3RZGTz7ZArVvuAkoOU4Q7yJjIVDnv1tddR59Awu4Yr041N8%2BDLZ%2F5VzssLDyfgwmhmYJFali%2BWqn7YbI8B%2FdxX9vaCgC%2BwFYW4ZsWQath2B80dnZTfyB768G7020dajuUIdHVw7royJVYy%2FUv1QsgKyD3aSJRFOS3vh%2BCklgVNhUHv3z%2BBHi4N9SVmeO66OWv%2BMmHXd552gS2b13ow5N1o3%2BHTXzFuZGEydNh9POi7y%2BjF4PswjJT1vAY6pgFSIiMWCmYgdFHOaDYgAlkEn43kdN6vhymO7BRzEQnoDGvFGT%2B%2F9HIk0yQWOmoLu1GyLs5gTNx25iC3Kri3YwIGo3csP4lk1rce7cQBofhZzWRToMp0%2F581vlKhflcSC5rtbmP7vAbDdtcOUBF6MgAt8TjuE3yA0%2B9jqItjSU%2FpVDpQfadefBsYX54QTxMJRmLuMrYG49PdUSx%2BQT9LkYizbuMkQpbH&X-Amz-Signature=9d44cddaa06329dc0f80f4b8c74a91074f51cbdd0bbba9aa1c663b692c4ac8c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK4MQ4J2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBRCVNI3OZwb8k%2FLNFqlaGkMwsIeuxrbhPclJtbLyCzvAiBauMqBOiMrHsknWAqY1ethO8KiC4KlKftMDKSbW30y0CqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSWOqkCMNsevOZ2CdKtwDwPZsCaN36AtduTABIyNInWI6P1WDI%2Fx602tv61ZoavGGIFyv520x7CG9DkZPHc%2FF%2BQ%2Fl1aaoMPj9%2FcBQOVndxmcdIKAQAnFDnk9qZ42xctkoard86xN8fA2eWMuNkcCPQ%2FcAaCU11gZNq%2FRNrooSpWHEnmfsmH1YLZm1zBFybnD%2Bb%2FY70k%2BjtW1zAgQs%2BiQkcdL39sraziEkLWFpB3t62U%2Fs%2BsVedxehlLO1ZsHxxWbGIiDpkOo33Pn843%2BcU1Lw1kdt3rlnnVJcRkgLYEbsWr8OB6lpRQkfMATclWj6kYZHJVRoS8cQociM09EYExdifdPNjdV40oCxXzX8JyVq5qeFCJv2X1bU%2FJG1iw1F43znqgn3vQPK2udMfTylq%2BeDIMaMDqMwTb3RZGTz7ZArVvuAkoOU4Q7yJjIVDnv1tddR59Awu4Yr041N8%2BDLZ%2F5VzssLDyfgwmhmYJFali%2BWqn7YbI8B%2FdxX9vaCgC%2BwFYW4ZsWQath2B80dnZTfyB768G7020dajuUIdHVw7royJVYy%2FUv1QsgKyD3aSJRFOS3vh%2BCklgVNhUHv3z%2BBHi4N9SVmeO66OWv%2BMmHXd552gS2b13ow5N1o3%2BHTXzFuZGEydNh9POi7y%2BjF4PswjJT1vAY6pgFSIiMWCmYgdFHOaDYgAlkEn43kdN6vhymO7BRzEQnoDGvFGT%2B%2F9HIk0yQWOmoLu1GyLs5gTNx25iC3Kri3YwIGo3csP4lk1rce7cQBofhZzWRToMp0%2F581vlKhflcSC5rtbmP7vAbDdtcOUBF6MgAt8TjuE3yA0%2B9jqItjSU%2FpVDpQfadefBsYX54QTxMJRmLuMrYG49PdUSx%2BQT9LkYizbuMkQpbH&X-Amz-Signature=421943abae25e82cf263cf80aeb969e7bfbd67714c1a874001a36a1ac6da0263&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK4MQ4J2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBRCVNI3OZwb8k%2FLNFqlaGkMwsIeuxrbhPclJtbLyCzvAiBauMqBOiMrHsknWAqY1ethO8KiC4KlKftMDKSbW30y0CqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSWOqkCMNsevOZ2CdKtwDwPZsCaN36AtduTABIyNInWI6P1WDI%2Fx602tv61ZoavGGIFyv520x7CG9DkZPHc%2FF%2BQ%2Fl1aaoMPj9%2FcBQOVndxmcdIKAQAnFDnk9qZ42xctkoard86xN8fA2eWMuNkcCPQ%2FcAaCU11gZNq%2FRNrooSpWHEnmfsmH1YLZm1zBFybnD%2Bb%2FY70k%2BjtW1zAgQs%2BiQkcdL39sraziEkLWFpB3t62U%2Fs%2BsVedxehlLO1ZsHxxWbGIiDpkOo33Pn843%2BcU1Lw1kdt3rlnnVJcRkgLYEbsWr8OB6lpRQkfMATclWj6kYZHJVRoS8cQociM09EYExdifdPNjdV40oCxXzX8JyVq5qeFCJv2X1bU%2FJG1iw1F43znqgn3vQPK2udMfTylq%2BeDIMaMDqMwTb3RZGTz7ZArVvuAkoOU4Q7yJjIVDnv1tddR59Awu4Yr041N8%2BDLZ%2F5VzssLDyfgwmhmYJFali%2BWqn7YbI8B%2FdxX9vaCgC%2BwFYW4ZsWQath2B80dnZTfyB768G7020dajuUIdHVw7royJVYy%2FUv1QsgKyD3aSJRFOS3vh%2BCklgVNhUHv3z%2BBHi4N9SVmeO66OWv%2BMmHXd552gS2b13ow5N1o3%2BHTXzFuZGEydNh9POi7y%2BjF4PswjJT1vAY6pgFSIiMWCmYgdFHOaDYgAlkEn43kdN6vhymO7BRzEQnoDGvFGT%2B%2F9HIk0yQWOmoLu1GyLs5gTNx25iC3Kri3YwIGo3csP4lk1rce7cQBofhZzWRToMp0%2F581vlKhflcSC5rtbmP7vAbDdtcOUBF6MgAt8TjuE3yA0%2B9jqItjSU%2FpVDpQfadefBsYX54QTxMJRmLuMrYG49PdUSx%2BQT9LkYizbuMkQpbH&X-Amz-Signature=88db71ff0537de74a506c8c81117112a7e24557c84486e73143a5617c2617af9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XASMGYR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzxKjQsqA2pCRk9mzZTaDIpkuICSiXuJBHzuDZtqWPDgIgb1mo3TaGh7nX98XFeqjSaIG4PbusEcX%2FvAL5Jh9%2FfkIqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOTX8Vf54HAg3AtBvSrcA2rizYU8ifGu0XYrx1pW0zn1xwnCfqP0DIWxAkq7VQ7Wr6K86J%2B6eKdZCR9O1%2FyAjgTobHfiQdk%2FyDjFbeVDEKKuwLjatkvFAnkJ8k7v7%2FW2ECd%2BUOIhZBDIs1IIfjdfvoSfc2r3HiAuSqg%2B%2Fhmuc4SUWQaxQA3sQ%2BW9Lf0m21ZvVJrRaaxUSs0Cc5F5Y3N5YBpvsrdMOX7O4QrERxPSrNrhqPbFLkHBg3ZiLLIwQgl%2BZpSS4mLArOa7tKZ8RPP%2BkI%2BV%2BFLwgbKcNYPOxtmtpLJU1yDZ3ANiglVSaRmsXghz%2B%2F2HAjMjZNvOKQa%2F4TCP0luDFYrmrA5xs8UFgkekH3w7LeFcFjHGPbRdV84sg%2F%2BhoAuEdzW4wq6uRYM3VA%2Bm%2FTuATCjZYKrYzZRMRu%2F7TYqu%2FgwPzKBuqtjRycYetfjtlAEpNZdQPG2xvcH4t2YEboHmOL5n2uMhZCNVR541Tf4nNJQyhpYGSzvX%2F9vxNa%2BaXAkdiKwv%2Ftq6K%2FJvuNKd08wQTEScRt5P0MtnBdtErpQUz3aEbc0LRmyi7cgpnX%2FIRrHPKX5531mt2WR%2BtxmTem4ZN%2FqA7QQKh19LIQ6vrH1IraBdSh93iZKqC460dCTHrrPMZAl4pABRBwehMO%2BT9bwGOqUBVYQED6CMSkxCkAeWDbug9BJ1vMP2mgvWyOkS5PRzXQ9LaxdX4KbThzZNc8NZRFd8kJ2%2B7X7GMmKWKV1LsITETTQ1ArNtK8JJFOF%2FuibYva3ZqL%2Fpsgw6j1NdAZx8Swj%2BoIADFM9CAn2MgCQvOc44mpPyssAOs18kBQ07sss8NgZCITQu9fwyLPxc%2BU1vYDgkvlqTObwtBDKAmxQWyLgisdigMsXj&X-Amz-Signature=8ee69ed3fd8fc037cdff1aa4b4ab7d8334c6b4c3fbab102df3fc6ce67965b5d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6QIDHOF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD7TFq%2FBVTHDGYKQpBGHTHTQWgcdlLtHYJCHPA0uIxgtgIhAOy%2FiYzInGDZmO0f9SVAZhKNLCc8EZ3ZgSA%2B8xxXeE6%2BKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLzu0LmsTfwqweJhMq3AP6yUFSUy%2Faf8JwBcVEwWg4P9KZyj8d0dGCYj4lYcfm%2FvNwm8aHzFdkUEl6gj5Dv6eLxnvqM6s9E8gJBl3xz42algSVu0bn81tKYiFmZOHo0dAQCHoUnV6ASCIqpsj2eeSwt96J26zq1rblzhQy%2FhT3aYsSyBBpbayj1e90jazPdXlBxQxsMQDkXuXr4t0rKhcO0dRd92gTFqIjZP1Cw%2FwxoPQ3y5uj9%2FtKzQ1DHVP1WZ%2BRF5%2BDAotqxHZQN8E%2Fqm%2BI%2BsPEkYi0OxIF7scYOoOtwBVBFYmlnMQwAhAtu4flV81gXYHa4N7yvAhCulBwXYj5jCSFtHR48481HBXaeK9cUm%2FVMM0%2B5rjax%2FG%2BNgRN5Nx77owBCaJywtCefX0kJ1wLMbPiYEd2im0DPt5IimJUC7MxHl43dRDnJUBF1XlYedVRt7lq69A6z05WlTo9ehbzRbWfD8IjCGjW%2BfhPPNLxSe99dGqvN2mmQQmgMzYf8LoX5m7apUNLZ6cXnMj2sRwTBnde0eSd6oXf3fsAl47VN1%2BRakFi1sC67%2B2gOR%2F%2Fw5htvMTdSK8w1MO7N1BR6aLV%2BVweGrWjevxr68R%2Fl8yglr8JOlx6dGi4VgALeGHUXp3%2FA9LpxbpTiSklEjCLlPW8BjqkAbJcyRtoW%2FbRfXnYS4gg4tj%2FlzVz29L%2BdE81%2FUDkuZ82h9s1JJo7mUL8Dy%2Ff5l29Xk%2B77jjt9FRjxnaxM%2B2WSXjkcXot6TpJMxdVAHYrYKC1FWYJJsn0%2BHlJVBPrJSNw9QF1pXt7wfg7yE4m8%2FDAprPHAaFNmgLS0ewdtDOiAkMOBTs4Bsg7O45co%2F9UQXWNVxr%2Bw%2B9n0S0gkgJ%2B%2Fqi3lY7bszkf&X-Amz-Signature=e43a754667b954020b57dcfa41d0adec56abb17757e658eef68f30a79d937923&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7A5YEHW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJ1O%2FsmL5FagCUj9f%2FiF1nnAA%2B6eibxN1FSHlnGz9NkgIhAMmaXo6PzkBHGhmbK4N0TCwtIaym89AGPH5yaxa37wI3KogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyDxT%2FMNdtvnL1BDwwq3APXV%2Bp%2FZ3NwRkyvvDlG5VW4i5lh9697OAgUR%2BqzMYGHezkHz8LqR9kxCxn3xH%2BqTG9Pm49M4kU3CP5l%2B3ttnSq9uDEC3L%2B4iK7nwoRBuEgS3N3z0X8Qt86aME9viZvMs6X7b1Fvwb3zlttKOYDS4e4ZuH4gGn07EKd7rdI%2F9tAt9Bpq6v6%2Bl6lz4wK0ZzuGcs68k3pjm%2FrW8m0mtpD11QbaUcLW4PUHSWgbuascUKatrdz0mpGnJwV0dkmxbP4vDv8J5sA1ijvAoY50%2Bi1nAMZJp9vMn2yqK4WgvlP1MTeuUVfnq2XAWE4lw8VWUSD1Ke2YhnnDj8oPgTZy%2Fb7Q3S3eKJjC9wfOuWQWY6etiHVQsUQL2dOJ6s2Dcn5DwGqpHaqIoorEHCzZpn1r7%2F2GXcSW7PORcml%2FTiCu4Wqs%2BW0d%2Fp9yNeM7LKeN1nsV%2F21OQ1F9Bl%2BjUDpxk2HYr6ORSdpefvsnY682mQoDUaUgSbPJTYBf9Kv%2BPvTUoJUod7W6iINmKJGxDtePje%2BAv9mweN%2BREtCNVqbFOHKeJhoTmiWq35skZA8lUirFResbgd%2FVMBsEIFByi7ejiVzkyK3qYvrgYXnk65XN%2B4Kkd0Rcnbh6fzcaAelZNh9DHrdX5jCDlPW8BjqkAfN3zj%2BSp2Z%2FL3lnjfBwKslVOlw73drviQewPY7qkcaKK%2BbBQgXtNLdsv%2BsXuLz79oWbJapBHtfH4Ffz50Z%2BpbfMEC8DZMeiSL1CIwgH%2BCmkFKt8eeedX1FPYxmq2nubki391k9U5VeKfoVoMJ5EWiq9sPs1V24v%2FfiTanjKMlaxPbnPFL6TIdL0g%2FhuXaFX1wYw4If6jXIrqhBn3YUQ9ZHjDbTQ&X-Amz-Signature=eeb6875d24c9179c1c5da0a93e3faaa2ae9dabfa3d1183ae028a21d646fec2b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7A5YEHW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJ1O%2FsmL5FagCUj9f%2FiF1nnAA%2B6eibxN1FSHlnGz9NkgIhAMmaXo6PzkBHGhmbK4N0TCwtIaym89AGPH5yaxa37wI3KogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyDxT%2FMNdtvnL1BDwwq3APXV%2Bp%2FZ3NwRkyvvDlG5VW4i5lh9697OAgUR%2BqzMYGHezkHz8LqR9kxCxn3xH%2BqTG9Pm49M4kU3CP5l%2B3ttnSq9uDEC3L%2B4iK7nwoRBuEgS3N3z0X8Qt86aME9viZvMs6X7b1Fvwb3zlttKOYDS4e4ZuH4gGn07EKd7rdI%2F9tAt9Bpq6v6%2Bl6lz4wK0ZzuGcs68k3pjm%2FrW8m0mtpD11QbaUcLW4PUHSWgbuascUKatrdz0mpGnJwV0dkmxbP4vDv8J5sA1ijvAoY50%2Bi1nAMZJp9vMn2yqK4WgvlP1MTeuUVfnq2XAWE4lw8VWUSD1Ke2YhnnDj8oPgTZy%2Fb7Q3S3eKJjC9wfOuWQWY6etiHVQsUQL2dOJ6s2Dcn5DwGqpHaqIoorEHCzZpn1r7%2F2GXcSW7PORcml%2FTiCu4Wqs%2BW0d%2Fp9yNeM7LKeN1nsV%2F21OQ1F9Bl%2BjUDpxk2HYr6ORSdpefvsnY682mQoDUaUgSbPJTYBf9Kv%2BPvTUoJUod7W6iINmKJGxDtePje%2BAv9mweN%2BREtCNVqbFOHKeJhoTmiWq35skZA8lUirFResbgd%2FVMBsEIFByi7ejiVzkyK3qYvrgYXnk65XN%2B4Kkd0Rcnbh6fzcaAelZNh9DHrdX5jCDlPW8BjqkAfN3zj%2BSp2Z%2FL3lnjfBwKslVOlw73drviQewPY7qkcaKK%2BbBQgXtNLdsv%2BsXuLz79oWbJapBHtfH4Ffz50Z%2BpbfMEC8DZMeiSL1CIwgH%2BCmkFKt8eeedX1FPYxmq2nubki391k9U5VeKfoVoMJ5EWiq9sPs1V24v%2FfiTanjKMlaxPbnPFL6TIdL0g%2FhuXaFX1wYw4If6jXIrqhBn3YUQ9ZHjDbTQ&X-Amz-Signature=c0f16aba56cd6e80695259a340253bae7d529485e0ef7b4505c6a3f47e2fa44e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
