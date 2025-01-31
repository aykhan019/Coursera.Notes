

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE2YWGGR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvhCUBmbJCXZrkBNpRY5V0LQNxU0xwGBAvM%2BkwBlx%2BxgIgVgPc5amSdqjZhxTa5WUQOAcBA4wI0hVQU86EqqWToEUqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrV6qLwFMVEPNu74CrcA02fBvV48T4QkNS3ScwnaPEoISX829nzR2sSN5BvHPoba%2FdG2gM%2B0BLN24c%2BgrZJsLj37Z1AAiOMTyowvEYLr3o6Q3r6uPmf8OoP64v4r0zYCjXVW%2F5Q4vWD6jLhVGMbTnn%2Fgv0%2BGF0uyXfBvtnQ9Vtx8RDii3hoK6dwel%2FZ2lp2JPvjCK6wX66gwyvUBDUln9922w%2FfaRdWUAOZKP1u0h3tF6rMD0XEy6mJbNYbTel5JZEiUjWLRFTgkMK90g8%2BgthNj0%2B8sq5NL4obsc54Cn7bFU%2F46rwkYOJru0W4C5xuOEG290pAqoShiCB0aOSXHDj%2BG%2FIaqlTxoOqAEu1MRxjWwS6rPV%2BQdGWkcwwEkM01XWzFha%2FOmzhCGFYhbLfIr95cPoKPjybTTEC1ocKR0KaW9t2JOqrxW%2FjbForetZrAnzJWh%2B84%2BHVV6JBMYkZXAh5S0r6Jj3GyvXnEi9vY5e9xuPupkX3JwzWV3K2Ndfc25OQrSE%2FfuPc8KVI8lVZ3PiLm90%2BdeWx%2Ftb10kaU7JZPAB1fQTO5rW%2FP0%2FO8V3YJgJVdFmLELGNuDJVIwvUNNxtkLnEO5pMZbFtAohB9lgrM1Fk6ycHYR33wDxfMyS1FErznIij3vNiZgMyAWMIqk9LwGOqUBtu43BZcBgIsxBP4vFLdD3zmcS5%2Bcg%2FT3JctgHqSacc3S8e7dsHbLQd9B2xd55i%2BcaxfvAajEa2qNxS%2B2pzXwQjj%2FA0T1oGRQnGBtVEDWDQ51UtkH2urF8L4TsT1uLI8T1%2FYoqfSo456wrHryUp6CtmRfHRQ8tH4UM6wnxWGNBKy6CN7JCLs1K1ihgfiW9fN0sC%2BhpJmtu8unhycT0JIM7JmukCxX&X-Amz-Signature=13f2fa501865575bd6f18953babc03e54b98044d87a7f21c331af28ac986a529&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE2YWGGR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvhCUBmbJCXZrkBNpRY5V0LQNxU0xwGBAvM%2BkwBlx%2BxgIgVgPc5amSdqjZhxTa5WUQOAcBA4wI0hVQU86EqqWToEUqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrV6qLwFMVEPNu74CrcA02fBvV48T4QkNS3ScwnaPEoISX829nzR2sSN5BvHPoba%2FdG2gM%2B0BLN24c%2BgrZJsLj37Z1AAiOMTyowvEYLr3o6Q3r6uPmf8OoP64v4r0zYCjXVW%2F5Q4vWD6jLhVGMbTnn%2Fgv0%2BGF0uyXfBvtnQ9Vtx8RDii3hoK6dwel%2FZ2lp2JPvjCK6wX66gwyvUBDUln9922w%2FfaRdWUAOZKP1u0h3tF6rMD0XEy6mJbNYbTel5JZEiUjWLRFTgkMK90g8%2BgthNj0%2B8sq5NL4obsc54Cn7bFU%2F46rwkYOJru0W4C5xuOEG290pAqoShiCB0aOSXHDj%2BG%2FIaqlTxoOqAEu1MRxjWwS6rPV%2BQdGWkcwwEkM01XWzFha%2FOmzhCGFYhbLfIr95cPoKPjybTTEC1ocKR0KaW9t2JOqrxW%2FjbForetZrAnzJWh%2B84%2BHVV6JBMYkZXAh5S0r6Jj3GyvXnEi9vY5e9xuPupkX3JwzWV3K2Ndfc25OQrSE%2FfuPc8KVI8lVZ3PiLm90%2BdeWx%2Ftb10kaU7JZPAB1fQTO5rW%2FP0%2FO8V3YJgJVdFmLELGNuDJVIwvUNNxtkLnEO5pMZbFtAohB9lgrM1Fk6ycHYR33wDxfMyS1FErznIij3vNiZgMyAWMIqk9LwGOqUBtu43BZcBgIsxBP4vFLdD3zmcS5%2Bcg%2FT3JctgHqSacc3S8e7dsHbLQd9B2xd55i%2BcaxfvAajEa2qNxS%2B2pzXwQjj%2FA0T1oGRQnGBtVEDWDQ51UtkH2urF8L4TsT1uLI8T1%2FYoqfSo456wrHryUp6CtmRfHRQ8tH4UM6wnxWGNBKy6CN7JCLs1K1ihgfiW9fN0sC%2BhpJmtu8unhycT0JIM7JmukCxX&X-Amz-Signature=b19f6bbcfe35f0daa6c9e754778d779f5a68a7c702bdf1502376267bb8f9c666&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE2YWGGR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvhCUBmbJCXZrkBNpRY5V0LQNxU0xwGBAvM%2BkwBlx%2BxgIgVgPc5amSdqjZhxTa5WUQOAcBA4wI0hVQU86EqqWToEUqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrV6qLwFMVEPNu74CrcA02fBvV48T4QkNS3ScwnaPEoISX829nzR2sSN5BvHPoba%2FdG2gM%2B0BLN24c%2BgrZJsLj37Z1AAiOMTyowvEYLr3o6Q3r6uPmf8OoP64v4r0zYCjXVW%2F5Q4vWD6jLhVGMbTnn%2Fgv0%2BGF0uyXfBvtnQ9Vtx8RDii3hoK6dwel%2FZ2lp2JPvjCK6wX66gwyvUBDUln9922w%2FfaRdWUAOZKP1u0h3tF6rMD0XEy6mJbNYbTel5JZEiUjWLRFTgkMK90g8%2BgthNj0%2B8sq5NL4obsc54Cn7bFU%2F46rwkYOJru0W4C5xuOEG290pAqoShiCB0aOSXHDj%2BG%2FIaqlTxoOqAEu1MRxjWwS6rPV%2BQdGWkcwwEkM01XWzFha%2FOmzhCGFYhbLfIr95cPoKPjybTTEC1ocKR0KaW9t2JOqrxW%2FjbForetZrAnzJWh%2B84%2BHVV6JBMYkZXAh5S0r6Jj3GyvXnEi9vY5e9xuPupkX3JwzWV3K2Ndfc25OQrSE%2FfuPc8KVI8lVZ3PiLm90%2BdeWx%2Ftb10kaU7JZPAB1fQTO5rW%2FP0%2FO8V3YJgJVdFmLELGNuDJVIwvUNNxtkLnEO5pMZbFtAohB9lgrM1Fk6ycHYR33wDxfMyS1FErznIij3vNiZgMyAWMIqk9LwGOqUBtu43BZcBgIsxBP4vFLdD3zmcS5%2Bcg%2FT3JctgHqSacc3S8e7dsHbLQd9B2xd55i%2BcaxfvAajEa2qNxS%2B2pzXwQjj%2FA0T1oGRQnGBtVEDWDQ51UtkH2urF8L4TsT1uLI8T1%2FYoqfSo456wrHryUp6CtmRfHRQ8tH4UM6wnxWGNBKy6CN7JCLs1K1ihgfiW9fN0sC%2BhpJmtu8unhycT0JIM7JmukCxX&X-Amz-Signature=70dc40c2fafd3f5410557e6ebef65d9a21fb80610771810d92c328243a88bd2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE2YWGGR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvhCUBmbJCXZrkBNpRY5V0LQNxU0xwGBAvM%2BkwBlx%2BxgIgVgPc5amSdqjZhxTa5WUQOAcBA4wI0hVQU86EqqWToEUqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrV6qLwFMVEPNu74CrcA02fBvV48T4QkNS3ScwnaPEoISX829nzR2sSN5BvHPoba%2FdG2gM%2B0BLN24c%2BgrZJsLj37Z1AAiOMTyowvEYLr3o6Q3r6uPmf8OoP64v4r0zYCjXVW%2F5Q4vWD6jLhVGMbTnn%2Fgv0%2BGF0uyXfBvtnQ9Vtx8RDii3hoK6dwel%2FZ2lp2JPvjCK6wX66gwyvUBDUln9922w%2FfaRdWUAOZKP1u0h3tF6rMD0XEy6mJbNYbTel5JZEiUjWLRFTgkMK90g8%2BgthNj0%2B8sq5NL4obsc54Cn7bFU%2F46rwkYOJru0W4C5xuOEG290pAqoShiCB0aOSXHDj%2BG%2FIaqlTxoOqAEu1MRxjWwS6rPV%2BQdGWkcwwEkM01XWzFha%2FOmzhCGFYhbLfIr95cPoKPjybTTEC1ocKR0KaW9t2JOqrxW%2FjbForetZrAnzJWh%2B84%2BHVV6JBMYkZXAh5S0r6Jj3GyvXnEi9vY5e9xuPupkX3JwzWV3K2Ndfc25OQrSE%2FfuPc8KVI8lVZ3PiLm90%2BdeWx%2Ftb10kaU7JZPAB1fQTO5rW%2FP0%2FO8V3YJgJVdFmLELGNuDJVIwvUNNxtkLnEO5pMZbFtAohB9lgrM1Fk6ycHYR33wDxfMyS1FErznIij3vNiZgMyAWMIqk9LwGOqUBtu43BZcBgIsxBP4vFLdD3zmcS5%2Bcg%2FT3JctgHqSacc3S8e7dsHbLQd9B2xd55i%2BcaxfvAajEa2qNxS%2B2pzXwQjj%2FA0T1oGRQnGBtVEDWDQ51UtkH2urF8L4TsT1uLI8T1%2FYoqfSo456wrHryUp6CtmRfHRQ8tH4UM6wnxWGNBKy6CN7JCLs1K1ihgfiW9fN0sC%2BhpJmtu8unhycT0JIM7JmukCxX&X-Amz-Signature=d25f24ba3fc46176fab8a58d08bfd7624b182a3edf133c09868770f0fec36859&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE2YWGGR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvhCUBmbJCXZrkBNpRY5V0LQNxU0xwGBAvM%2BkwBlx%2BxgIgVgPc5amSdqjZhxTa5WUQOAcBA4wI0hVQU86EqqWToEUqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrV6qLwFMVEPNu74CrcA02fBvV48T4QkNS3ScwnaPEoISX829nzR2sSN5BvHPoba%2FdG2gM%2B0BLN24c%2BgrZJsLj37Z1AAiOMTyowvEYLr3o6Q3r6uPmf8OoP64v4r0zYCjXVW%2F5Q4vWD6jLhVGMbTnn%2Fgv0%2BGF0uyXfBvtnQ9Vtx8RDii3hoK6dwel%2FZ2lp2JPvjCK6wX66gwyvUBDUln9922w%2FfaRdWUAOZKP1u0h3tF6rMD0XEy6mJbNYbTel5JZEiUjWLRFTgkMK90g8%2BgthNj0%2B8sq5NL4obsc54Cn7bFU%2F46rwkYOJru0W4C5xuOEG290pAqoShiCB0aOSXHDj%2BG%2FIaqlTxoOqAEu1MRxjWwS6rPV%2BQdGWkcwwEkM01XWzFha%2FOmzhCGFYhbLfIr95cPoKPjybTTEC1ocKR0KaW9t2JOqrxW%2FjbForetZrAnzJWh%2B84%2BHVV6JBMYkZXAh5S0r6Jj3GyvXnEi9vY5e9xuPupkX3JwzWV3K2Ndfc25OQrSE%2FfuPc8KVI8lVZ3PiLm90%2BdeWx%2Ftb10kaU7JZPAB1fQTO5rW%2FP0%2FO8V3YJgJVdFmLELGNuDJVIwvUNNxtkLnEO5pMZbFtAohB9lgrM1Fk6ycHYR33wDxfMyS1FErznIij3vNiZgMyAWMIqk9LwGOqUBtu43BZcBgIsxBP4vFLdD3zmcS5%2Bcg%2FT3JctgHqSacc3S8e7dsHbLQd9B2xd55i%2BcaxfvAajEa2qNxS%2B2pzXwQjj%2FA0T1oGRQnGBtVEDWDQ51UtkH2urF8L4TsT1uLI8T1%2FYoqfSo456wrHryUp6CtmRfHRQ8tH4UM6wnxWGNBKy6CN7JCLs1K1ihgfiW9fN0sC%2BhpJmtu8unhycT0JIM7JmukCxX&X-Amz-Signature=a9e4a04d0fd93762bd4e99f19314138de80d9679d758a7d9ff40eb8bfcb69f68&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE2YWGGR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvhCUBmbJCXZrkBNpRY5V0LQNxU0xwGBAvM%2BkwBlx%2BxgIgVgPc5amSdqjZhxTa5WUQOAcBA4wI0hVQU86EqqWToEUqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrV6qLwFMVEPNu74CrcA02fBvV48T4QkNS3ScwnaPEoISX829nzR2sSN5BvHPoba%2FdG2gM%2B0BLN24c%2BgrZJsLj37Z1AAiOMTyowvEYLr3o6Q3r6uPmf8OoP64v4r0zYCjXVW%2F5Q4vWD6jLhVGMbTnn%2Fgv0%2BGF0uyXfBvtnQ9Vtx8RDii3hoK6dwel%2FZ2lp2JPvjCK6wX66gwyvUBDUln9922w%2FfaRdWUAOZKP1u0h3tF6rMD0XEy6mJbNYbTel5JZEiUjWLRFTgkMK90g8%2BgthNj0%2B8sq5NL4obsc54Cn7bFU%2F46rwkYOJru0W4C5xuOEG290pAqoShiCB0aOSXHDj%2BG%2FIaqlTxoOqAEu1MRxjWwS6rPV%2BQdGWkcwwEkM01XWzFha%2FOmzhCGFYhbLfIr95cPoKPjybTTEC1ocKR0KaW9t2JOqrxW%2FjbForetZrAnzJWh%2B84%2BHVV6JBMYkZXAh5S0r6Jj3GyvXnEi9vY5e9xuPupkX3JwzWV3K2Ndfc25OQrSE%2FfuPc8KVI8lVZ3PiLm90%2BdeWx%2Ftb10kaU7JZPAB1fQTO5rW%2FP0%2FO8V3YJgJVdFmLELGNuDJVIwvUNNxtkLnEO5pMZbFtAohB9lgrM1Fk6ycHYR33wDxfMyS1FErznIij3vNiZgMyAWMIqk9LwGOqUBtu43BZcBgIsxBP4vFLdD3zmcS5%2Bcg%2FT3JctgHqSacc3S8e7dsHbLQd9B2xd55i%2BcaxfvAajEa2qNxS%2B2pzXwQjj%2FA0T1oGRQnGBtVEDWDQ51UtkH2urF8L4TsT1uLI8T1%2FYoqfSo456wrHryUp6CtmRfHRQ8tH4UM6wnxWGNBKy6CN7JCLs1K1ihgfiW9fN0sC%2BhpJmtu8unhycT0JIM7JmukCxX&X-Amz-Signature=9abc91b3fe5e47de94e7fe2840dac8014f5764576bf00ff8bb18c228e594a937&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE2YWGGR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvhCUBmbJCXZrkBNpRY5V0LQNxU0xwGBAvM%2BkwBlx%2BxgIgVgPc5amSdqjZhxTa5WUQOAcBA4wI0hVQU86EqqWToEUqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrV6qLwFMVEPNu74CrcA02fBvV48T4QkNS3ScwnaPEoISX829nzR2sSN5BvHPoba%2FdG2gM%2B0BLN24c%2BgrZJsLj37Z1AAiOMTyowvEYLr3o6Q3r6uPmf8OoP64v4r0zYCjXVW%2F5Q4vWD6jLhVGMbTnn%2Fgv0%2BGF0uyXfBvtnQ9Vtx8RDii3hoK6dwel%2FZ2lp2JPvjCK6wX66gwyvUBDUln9922w%2FfaRdWUAOZKP1u0h3tF6rMD0XEy6mJbNYbTel5JZEiUjWLRFTgkMK90g8%2BgthNj0%2B8sq5NL4obsc54Cn7bFU%2F46rwkYOJru0W4C5xuOEG290pAqoShiCB0aOSXHDj%2BG%2FIaqlTxoOqAEu1MRxjWwS6rPV%2BQdGWkcwwEkM01XWzFha%2FOmzhCGFYhbLfIr95cPoKPjybTTEC1ocKR0KaW9t2JOqrxW%2FjbForetZrAnzJWh%2B84%2BHVV6JBMYkZXAh5S0r6Jj3GyvXnEi9vY5e9xuPupkX3JwzWV3K2Ndfc25OQrSE%2FfuPc8KVI8lVZ3PiLm90%2BdeWx%2Ftb10kaU7JZPAB1fQTO5rW%2FP0%2FO8V3YJgJVdFmLELGNuDJVIwvUNNxtkLnEO5pMZbFtAohB9lgrM1Fk6ycHYR33wDxfMyS1FErznIij3vNiZgMyAWMIqk9LwGOqUBtu43BZcBgIsxBP4vFLdD3zmcS5%2Bcg%2FT3JctgHqSacc3S8e7dsHbLQd9B2xd55i%2BcaxfvAajEa2qNxS%2B2pzXwQjj%2FA0T1oGRQnGBtVEDWDQ51UtkH2urF8L4TsT1uLI8T1%2FYoqfSo456wrHryUp6CtmRfHRQ8tH4UM6wnxWGNBKy6CN7JCLs1K1ihgfiW9fN0sC%2BhpJmtu8unhycT0JIM7JmukCxX&X-Amz-Signature=cd2fc23c8fd2abf48d99cf489f04a18ab3b186dfc298b004cd8af13071b9a8f1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE2YWGGR%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvhCUBmbJCXZrkBNpRY5V0LQNxU0xwGBAvM%2BkwBlx%2BxgIgVgPc5amSdqjZhxTa5WUQOAcBA4wI0hVQU86EqqWToEUqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrV6qLwFMVEPNu74CrcA02fBvV48T4QkNS3ScwnaPEoISX829nzR2sSN5BvHPoba%2FdG2gM%2B0BLN24c%2BgrZJsLj37Z1AAiOMTyowvEYLr3o6Q3r6uPmf8OoP64v4r0zYCjXVW%2F5Q4vWD6jLhVGMbTnn%2Fgv0%2BGF0uyXfBvtnQ9Vtx8RDii3hoK6dwel%2FZ2lp2JPvjCK6wX66gwyvUBDUln9922w%2FfaRdWUAOZKP1u0h3tF6rMD0XEy6mJbNYbTel5JZEiUjWLRFTgkMK90g8%2BgthNj0%2B8sq5NL4obsc54Cn7bFU%2F46rwkYOJru0W4C5xuOEG290pAqoShiCB0aOSXHDj%2BG%2FIaqlTxoOqAEu1MRxjWwS6rPV%2BQdGWkcwwEkM01XWzFha%2FOmzhCGFYhbLfIr95cPoKPjybTTEC1ocKR0KaW9t2JOqrxW%2FjbForetZrAnzJWh%2B84%2BHVV6JBMYkZXAh5S0r6Jj3GyvXnEi9vY5e9xuPupkX3JwzWV3K2Ndfc25OQrSE%2FfuPc8KVI8lVZ3PiLm90%2BdeWx%2Ftb10kaU7JZPAB1fQTO5rW%2FP0%2FO8V3YJgJVdFmLELGNuDJVIwvUNNxtkLnEO5pMZbFtAohB9lgrM1Fk6ycHYR33wDxfMyS1FErznIij3vNiZgMyAWMIqk9LwGOqUBtu43BZcBgIsxBP4vFLdD3zmcS5%2Bcg%2FT3JctgHqSacc3S8e7dsHbLQd9B2xd55i%2BcaxfvAajEa2qNxS%2B2pzXwQjj%2FA0T1oGRQnGBtVEDWDQ51UtkH2urF8L4TsT1uLI8T1%2FYoqfSo456wrHryUp6CtmRfHRQ8tH4UM6wnxWGNBKy6CN7JCLs1K1ihgfiW9fN0sC%2BhpJmtu8unhycT0JIM7JmukCxX&X-Amz-Signature=149763c99df964dec14dce0e137fd217f09ec5f75f016b78be72f20e10f82da0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZO5TDHAB%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAUPtzNCqLHApF1JQUK58N6B8hyb18vACqYCxHZvDXsgIhAIfuAHPhO%2F9dkqrKs2K0LMZsCmKVqNtcP7WcrJYfqupjKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyY3p6Vh5BksFHI0gIq3ANaqzAw6bltOEYCHsdwp9BiFlCyJ2QjZuJwmvgLrF7mtMsichPAIcNvB%2FRtvR6TUAzTsjScQKqd6%2FMj32d0uUmA5e24x0P4ChPrNO1zMMHMlkOClYRr7jvcen29jebZbqw5HFdY2kx8%2FcYrQ6zPgoiL8GWsPE%2Fl%2FdZ9EVEXBzovm%2FSRnscuDGwwrypODL9XN6dziPRaG1%2Fhr0rcbKC82bRIL0z3aIat6%2FyJxYrieG6NrafNcGTuG8RGGZuvVcdBFZIIaMFTh%2BGZgmc49isy3UzDNj0vPlwzwOoRC1EUrqvWinL2aMII30M7JeR%2F9zjkl1s2X%2BoeDFkokyyuVIE%2B8daU0YzqyVxRyYokcZGE%2BVjuAaSZBeoBVVjqppvoUf%2FT1w%2BNpvTNCzLIKfHSKaCFJCAjkzXzO4o4YP5PF1d%2FRY%2F2qFNVeysUm61pAtvmFCbswTi0qMbGRPNjESd%2FBAh4UjBuG3fjRkrS3QSwGck%2FgD4eFYnzT4cF56N%2BYOlpNjiNZaLDa4SRkYCXa6LfgJi%2FKTmwx3sOEjQmA9VM%2FHF99BJ0HzXmeoqD7RCfW5kY6KCrkACMMtolMU4u%2FM2rRwR19mJqPB8ma2gZSUUNCxClOcQ8RsUW0OfiTEKIV9bpTTCHpPS8BjqkARSaIe4xn%2FqX4PqRReuu2mXWln%2F%2Bs%2BRNlq7bV4eD67eDPGxwZmgdxZ3EzXaANyPyLZBe9Op9K%2FXbzVAgCUeTfq%2F%2FVHhmxP4zoTmJox%2Fuy5ciluJvMPuzPicxzAB1zgqtnyg513T6NzLw1DYNo4zUcD7QzC9PBE9E%2BuiUF5Nc3qsxrLa3xbKQPWecYr9wR8qFP0KLfYzNS24GsbiM2xmV7kcka%2Fxz&X-Amz-Signature=e96b4c86e3194e4b09e2ffaab72d40ae7c0edfb0b5eaa5ffa3f1be736d230be7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU65MDGM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIErJg3kO5VFb617pPr6NOUuvObwl0cX3qKNuPpICzTJNAiEAyitZTUUPCHLnzAFTlK99HCGy4CR7SK3HxGVMBgdGOCMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHSgqfldT3YQeio%2BjircA22JkvRxzLSnFOIOut1gAbGbYFL8G8IwGER3VfemBnpkQYg3z%2BEGYx6HixQ9POSJ1TClpoFq0AVzld2NgRlKpHgnBGfUD4usgLMqTiCuLHqwKjhneGetyv%2BIJtgY55TvxP1Fxls5dyRpGHTz117aFeBNakTp1snF0NkljqvWp6DHaHKj4fyuy2JTy%2B7pxBtDVA%2FdvfMl%2BqjtfN6uaqszb5n%2BzWy9hAInergkiL9v1e4mf1%2BvEQI2qfHju%2Fxz6OYSNbAbDFmXkBeSD4TQUb4x3aMJvmf0yssVOIoxe51GI6pS4oWX4ttZu5Sp%2FQwByurgPzkhEoVxCDoTmD2aQgYR3TDFqEVsNtYJcRk5kaWY79TDhsURVExK3BTFLjlPdJ5ILs7UsOMfncY%2BIxJQG3%2BQujpAPw6pBbdvkzDd8L9%2F1Pqk2p7P%2Bh9tx74%2FEwglCBi8GUq5gvW5TPkjWLsbhRXq4Y6DIYyN1DKAVeh4Xjy4Ph%2BMqnOE1QhwbGNpa7gSl%2FzkJvUs9oYuSHalSdttC%2Fdjh7MWTNVs8kJUnXGufHNtVDS3dcbzK5nI%2BMtqy4XtSWHaRSdGWXkO%2BbaO2jqKdOKuYlEXB1PkLvnOeGBobV1nOTG%2FtCmsCbS%2BcqkmumrKMInA9LwGOqUB67sRU3fVDlW4N51XRaqJkZl2WKIXf1j1D4QPqsOiUKYWs1eX4uV6Co8u2eSot0U7yFMFV6PhVLH12cy0dAPJgLLzLkafeAKauevexNnBSXxMGhn%2B9CyOdFphHpXEkjCCkuSDvm8KzBFxVr%2FKgG9dE6JJOoXBuUJ1tJIcUDYtxhuyCYud2%2BuzEgRcNrXG4CexhjOGeYRk2I1RluD4CTlcI8pAfolL&X-Amz-Signature=724c289660dce4e9e7faec3eab1f3808eedbf6d6c9f40877efeee9269ff0c167&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU65MDGM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIErJg3kO5VFb617pPr6NOUuvObwl0cX3qKNuPpICzTJNAiEAyitZTUUPCHLnzAFTlK99HCGy4CR7SK3HxGVMBgdGOCMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHSgqfldT3YQeio%2BjircA22JkvRxzLSnFOIOut1gAbGbYFL8G8IwGER3VfemBnpkQYg3z%2BEGYx6HixQ9POSJ1TClpoFq0AVzld2NgRlKpHgnBGfUD4usgLMqTiCuLHqwKjhneGetyv%2BIJtgY55TvxP1Fxls5dyRpGHTz117aFeBNakTp1snF0NkljqvWp6DHaHKj4fyuy2JTy%2B7pxBtDVA%2FdvfMl%2BqjtfN6uaqszb5n%2BzWy9hAInergkiL9v1e4mf1%2BvEQI2qfHju%2Fxz6OYSNbAbDFmXkBeSD4TQUb4x3aMJvmf0yssVOIoxe51GI6pS4oWX4ttZu5Sp%2FQwByurgPzkhEoVxCDoTmD2aQgYR3TDFqEVsNtYJcRk5kaWY79TDhsURVExK3BTFLjlPdJ5ILs7UsOMfncY%2BIxJQG3%2BQujpAPw6pBbdvkzDd8L9%2F1Pqk2p7P%2Bh9tx74%2FEwglCBi8GUq5gvW5TPkjWLsbhRXq4Y6DIYyN1DKAVeh4Xjy4Ph%2BMqnOE1QhwbGNpa7gSl%2FzkJvUs9oYuSHalSdttC%2Fdjh7MWTNVs8kJUnXGufHNtVDS3dcbzK5nI%2BMtqy4XtSWHaRSdGWXkO%2BbaO2jqKdOKuYlEXB1PkLvnOeGBobV1nOTG%2FtCmsCbS%2BcqkmumrKMInA9LwGOqUB67sRU3fVDlW4N51XRaqJkZl2WKIXf1j1D4QPqsOiUKYWs1eX4uV6Co8u2eSot0U7yFMFV6PhVLH12cy0dAPJgLLzLkafeAKauevexNnBSXxMGhn%2B9CyOdFphHpXEkjCCkuSDvm8KzBFxVr%2FKgG9dE6JJOoXBuUJ1tJIcUDYtxhuyCYud2%2BuzEgRcNrXG4CexhjOGeYRk2I1RluD4CTlcI8pAfolL&X-Amz-Signature=52993a4bc1e5a7fe2b358649f7dbe97e8cc85784a85c9e8a392e8ffe1bab4463&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU65MDGM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIErJg3kO5VFb617pPr6NOUuvObwl0cX3qKNuPpICzTJNAiEAyitZTUUPCHLnzAFTlK99HCGy4CR7SK3HxGVMBgdGOCMqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHSgqfldT3YQeio%2BjircA22JkvRxzLSnFOIOut1gAbGbYFL8G8IwGER3VfemBnpkQYg3z%2BEGYx6HixQ9POSJ1TClpoFq0AVzld2NgRlKpHgnBGfUD4usgLMqTiCuLHqwKjhneGetyv%2BIJtgY55TvxP1Fxls5dyRpGHTz117aFeBNakTp1snF0NkljqvWp6DHaHKj4fyuy2JTy%2B7pxBtDVA%2FdvfMl%2BqjtfN6uaqszb5n%2BzWy9hAInergkiL9v1e4mf1%2BvEQI2qfHju%2Fxz6OYSNbAbDFmXkBeSD4TQUb4x3aMJvmf0yssVOIoxe51GI6pS4oWX4ttZu5Sp%2FQwByurgPzkhEoVxCDoTmD2aQgYR3TDFqEVsNtYJcRk5kaWY79TDhsURVExK3BTFLjlPdJ5ILs7UsOMfncY%2BIxJQG3%2BQujpAPw6pBbdvkzDd8L9%2F1Pqk2p7P%2Bh9tx74%2FEwglCBi8GUq5gvW5TPkjWLsbhRXq4Y6DIYyN1DKAVeh4Xjy4Ph%2BMqnOE1QhwbGNpa7gSl%2FzkJvUs9oYuSHalSdttC%2Fdjh7MWTNVs8kJUnXGufHNtVDS3dcbzK5nI%2BMtqy4XtSWHaRSdGWXkO%2BbaO2jqKdOKuYlEXB1PkLvnOeGBobV1nOTG%2FtCmsCbS%2BcqkmumrKMInA9LwGOqUB67sRU3fVDlW4N51XRaqJkZl2WKIXf1j1D4QPqsOiUKYWs1eX4uV6Co8u2eSot0U7yFMFV6PhVLH12cy0dAPJgLLzLkafeAKauevexNnBSXxMGhn%2B9CyOdFphHpXEkjCCkuSDvm8KzBFxVr%2FKgG9dE6JJOoXBuUJ1tJIcUDYtxhuyCYud2%2BuzEgRcNrXG4CexhjOGeYRk2I1RluD4CTlcI8pAfolL&X-Amz-Signature=75aa5a629372c01063f5977002c0fa6b859cd5509cf08138643829b3cd96304f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
