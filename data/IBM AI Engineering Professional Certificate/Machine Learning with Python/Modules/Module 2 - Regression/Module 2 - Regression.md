

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4Q3UPI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDtIvWePub6YmhmgKft3uFvsCbo916wn0q%2BHdXT9NVvsgIhAOImyBEES2wdd1p90Hf%2F%2F5hmteJIjAKdYM%2F%2F5LcdgHPlKv8DCEAQABoMNjM3NDIzMTgzODA1IgxdxdWRn0tdpvlN%2BlMq3AO0EXrdH8gkUIPsxmdNdrUWEnIUIp1E7BsdDPnmyTkMLCvLYAv%2F6KgnRtaydtfRRefGHygEFZtx%2Bs%2FcTYifgFsOEx8VqsJLTv90VGYhfNPOeng%2F45QBs26wlBp0CDx43hMH5dBgJMJiA9bWWFbOEadmihgkrgHscyLNpWaIxj95OBXzvo29rlz4sVkHr7WqtlZPtsmKmsWxm6Rko57dMYi5HsuiyLmr%2ByWD66EUShZDbm0ypNpUfYRXINDEb2McR09H32NjtnQvfiaIGwQCCd1m2tdhVnCvPtrnhk5iMyCj128vvsScupYcEYDhuQIC8bBd3MSrgNtP%2FVC4rbOBkyNsG1lw5qR9s%2FtdaZVLpsiak0icpEs%2FY%2BUGafDT1MY6D2rfmgDrbIMz2cNCrdpPGIu37EjP0gXxH8sMXh2mbdG1wY6BfEIvwvrANWyZprmwUBmnEjWzntEBOewn3XpBVJjHah%2BD%2Bu%2B6YyuhoE8XGrvLAdBZc6V7wzAfvb%2FA3Sxsm5YAHEs3jBUibo644LXRxay62P5p9PL5yubDhb9vPXnPtJw0uZdVRsbsmzerMXKjFJsPv8uLQ751An%2FkyQCIxUxP6gui9Wsb8tLMyVY9%2FcITraoJ%2FhXrGJteBjr4QjDHlYy9BjqkAVe1upfHbWKZiJZSEiRGqwjqipxbMEnkkzNFwGS6tp7AU5heiesrRTTe%2BKICKgzpadA%2FESbQ7WOFlB%2Ftwn1tWBc1JC8wVo0tYK7o4NK6D3r8ELvjq7cg4hO%2FyWKe%2BtpAU%2FwFWnA7jQ9GteMY2fvqXjE%2FgHxlIxYBdLNcf%2Blap%2BnMYNLsiMe7DyKEr%2BtUu6KA6eiP86%2Fc%2BnAvcERj3YqDVa820%2FRx&X-Amz-Signature=5240dd1ceedb0e24f8b4cfcc87bf84441bfa0381b31c875aca4a71d49244a21c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4Q3UPI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDtIvWePub6YmhmgKft3uFvsCbo916wn0q%2BHdXT9NVvsgIhAOImyBEES2wdd1p90Hf%2F%2F5hmteJIjAKdYM%2F%2F5LcdgHPlKv8DCEAQABoMNjM3NDIzMTgzODA1IgxdxdWRn0tdpvlN%2BlMq3AO0EXrdH8gkUIPsxmdNdrUWEnIUIp1E7BsdDPnmyTkMLCvLYAv%2F6KgnRtaydtfRRefGHygEFZtx%2Bs%2FcTYifgFsOEx8VqsJLTv90VGYhfNPOeng%2F45QBs26wlBp0CDx43hMH5dBgJMJiA9bWWFbOEadmihgkrgHscyLNpWaIxj95OBXzvo29rlz4sVkHr7WqtlZPtsmKmsWxm6Rko57dMYi5HsuiyLmr%2ByWD66EUShZDbm0ypNpUfYRXINDEb2McR09H32NjtnQvfiaIGwQCCd1m2tdhVnCvPtrnhk5iMyCj128vvsScupYcEYDhuQIC8bBd3MSrgNtP%2FVC4rbOBkyNsG1lw5qR9s%2FtdaZVLpsiak0icpEs%2FY%2BUGafDT1MY6D2rfmgDrbIMz2cNCrdpPGIu37EjP0gXxH8sMXh2mbdG1wY6BfEIvwvrANWyZprmwUBmnEjWzntEBOewn3XpBVJjHah%2BD%2Bu%2B6YyuhoE8XGrvLAdBZc6V7wzAfvb%2FA3Sxsm5YAHEs3jBUibo644LXRxay62P5p9PL5yubDhb9vPXnPtJw0uZdVRsbsmzerMXKjFJsPv8uLQ751An%2FkyQCIxUxP6gui9Wsb8tLMyVY9%2FcITraoJ%2FhXrGJteBjr4QjDHlYy9BjqkAVe1upfHbWKZiJZSEiRGqwjqipxbMEnkkzNFwGS6tp7AU5heiesrRTTe%2BKICKgzpadA%2FESbQ7WOFlB%2Ftwn1tWBc1JC8wVo0tYK7o4NK6D3r8ELvjq7cg4hO%2FyWKe%2BtpAU%2FwFWnA7jQ9GteMY2fvqXjE%2FgHxlIxYBdLNcf%2Blap%2BnMYNLsiMe7DyKEr%2BtUu6KA6eiP86%2Fc%2BnAvcERj3YqDVa820%2FRx&X-Amz-Signature=13fc0fb163cff435acbb31b40143cc94a464796717c498c6fc338568b4816459&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4Q3UPI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDtIvWePub6YmhmgKft3uFvsCbo916wn0q%2BHdXT9NVvsgIhAOImyBEES2wdd1p90Hf%2F%2F5hmteJIjAKdYM%2F%2F5LcdgHPlKv8DCEAQABoMNjM3NDIzMTgzODA1IgxdxdWRn0tdpvlN%2BlMq3AO0EXrdH8gkUIPsxmdNdrUWEnIUIp1E7BsdDPnmyTkMLCvLYAv%2F6KgnRtaydtfRRefGHygEFZtx%2Bs%2FcTYifgFsOEx8VqsJLTv90VGYhfNPOeng%2F45QBs26wlBp0CDx43hMH5dBgJMJiA9bWWFbOEadmihgkrgHscyLNpWaIxj95OBXzvo29rlz4sVkHr7WqtlZPtsmKmsWxm6Rko57dMYi5HsuiyLmr%2ByWD66EUShZDbm0ypNpUfYRXINDEb2McR09H32NjtnQvfiaIGwQCCd1m2tdhVnCvPtrnhk5iMyCj128vvsScupYcEYDhuQIC8bBd3MSrgNtP%2FVC4rbOBkyNsG1lw5qR9s%2FtdaZVLpsiak0icpEs%2FY%2BUGafDT1MY6D2rfmgDrbIMz2cNCrdpPGIu37EjP0gXxH8sMXh2mbdG1wY6BfEIvwvrANWyZprmwUBmnEjWzntEBOewn3XpBVJjHah%2BD%2Bu%2B6YyuhoE8XGrvLAdBZc6V7wzAfvb%2FA3Sxsm5YAHEs3jBUibo644LXRxay62P5p9PL5yubDhb9vPXnPtJw0uZdVRsbsmzerMXKjFJsPv8uLQ751An%2FkyQCIxUxP6gui9Wsb8tLMyVY9%2FcITraoJ%2FhXrGJteBjr4QjDHlYy9BjqkAVe1upfHbWKZiJZSEiRGqwjqipxbMEnkkzNFwGS6tp7AU5heiesrRTTe%2BKICKgzpadA%2FESbQ7WOFlB%2Ftwn1tWBc1JC8wVo0tYK7o4NK6D3r8ELvjq7cg4hO%2FyWKe%2BtpAU%2FwFWnA7jQ9GteMY2fvqXjE%2FgHxlIxYBdLNcf%2Blap%2BnMYNLsiMe7DyKEr%2BtUu6KA6eiP86%2Fc%2BnAvcERj3YqDVa820%2FRx&X-Amz-Signature=00b27baba2cc41af59abd0ca1089e2fb693b4c7554f2d16528529d72b26d11ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4Q3UPI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDtIvWePub6YmhmgKft3uFvsCbo916wn0q%2BHdXT9NVvsgIhAOImyBEES2wdd1p90Hf%2F%2F5hmteJIjAKdYM%2F%2F5LcdgHPlKv8DCEAQABoMNjM3NDIzMTgzODA1IgxdxdWRn0tdpvlN%2BlMq3AO0EXrdH8gkUIPsxmdNdrUWEnIUIp1E7BsdDPnmyTkMLCvLYAv%2F6KgnRtaydtfRRefGHygEFZtx%2Bs%2FcTYifgFsOEx8VqsJLTv90VGYhfNPOeng%2F45QBs26wlBp0CDx43hMH5dBgJMJiA9bWWFbOEadmihgkrgHscyLNpWaIxj95OBXzvo29rlz4sVkHr7WqtlZPtsmKmsWxm6Rko57dMYi5HsuiyLmr%2ByWD66EUShZDbm0ypNpUfYRXINDEb2McR09H32NjtnQvfiaIGwQCCd1m2tdhVnCvPtrnhk5iMyCj128vvsScupYcEYDhuQIC8bBd3MSrgNtP%2FVC4rbOBkyNsG1lw5qR9s%2FtdaZVLpsiak0icpEs%2FY%2BUGafDT1MY6D2rfmgDrbIMz2cNCrdpPGIu37EjP0gXxH8sMXh2mbdG1wY6BfEIvwvrANWyZprmwUBmnEjWzntEBOewn3XpBVJjHah%2BD%2Bu%2B6YyuhoE8XGrvLAdBZc6V7wzAfvb%2FA3Sxsm5YAHEs3jBUibo644LXRxay62P5p9PL5yubDhb9vPXnPtJw0uZdVRsbsmzerMXKjFJsPv8uLQ751An%2FkyQCIxUxP6gui9Wsb8tLMyVY9%2FcITraoJ%2FhXrGJteBjr4QjDHlYy9BjqkAVe1upfHbWKZiJZSEiRGqwjqipxbMEnkkzNFwGS6tp7AU5heiesrRTTe%2BKICKgzpadA%2FESbQ7WOFlB%2Ftwn1tWBc1JC8wVo0tYK7o4NK6D3r8ELvjq7cg4hO%2FyWKe%2BtpAU%2FwFWnA7jQ9GteMY2fvqXjE%2FgHxlIxYBdLNcf%2Blap%2BnMYNLsiMe7DyKEr%2BtUu6KA6eiP86%2Fc%2BnAvcERj3YqDVa820%2FRx&X-Amz-Signature=c206c1eb12c77dd70ce9854096dbe8f89b8cd35e1828f8327516ea5ead452602&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4Q3UPI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDtIvWePub6YmhmgKft3uFvsCbo916wn0q%2BHdXT9NVvsgIhAOImyBEES2wdd1p90Hf%2F%2F5hmteJIjAKdYM%2F%2F5LcdgHPlKv8DCEAQABoMNjM3NDIzMTgzODA1IgxdxdWRn0tdpvlN%2BlMq3AO0EXrdH8gkUIPsxmdNdrUWEnIUIp1E7BsdDPnmyTkMLCvLYAv%2F6KgnRtaydtfRRefGHygEFZtx%2Bs%2FcTYifgFsOEx8VqsJLTv90VGYhfNPOeng%2F45QBs26wlBp0CDx43hMH5dBgJMJiA9bWWFbOEadmihgkrgHscyLNpWaIxj95OBXzvo29rlz4sVkHr7WqtlZPtsmKmsWxm6Rko57dMYi5HsuiyLmr%2ByWD66EUShZDbm0ypNpUfYRXINDEb2McR09H32NjtnQvfiaIGwQCCd1m2tdhVnCvPtrnhk5iMyCj128vvsScupYcEYDhuQIC8bBd3MSrgNtP%2FVC4rbOBkyNsG1lw5qR9s%2FtdaZVLpsiak0icpEs%2FY%2BUGafDT1MY6D2rfmgDrbIMz2cNCrdpPGIu37EjP0gXxH8sMXh2mbdG1wY6BfEIvwvrANWyZprmwUBmnEjWzntEBOewn3XpBVJjHah%2BD%2Bu%2B6YyuhoE8XGrvLAdBZc6V7wzAfvb%2FA3Sxsm5YAHEs3jBUibo644LXRxay62P5p9PL5yubDhb9vPXnPtJw0uZdVRsbsmzerMXKjFJsPv8uLQ751An%2FkyQCIxUxP6gui9Wsb8tLMyVY9%2FcITraoJ%2FhXrGJteBjr4QjDHlYy9BjqkAVe1upfHbWKZiJZSEiRGqwjqipxbMEnkkzNFwGS6tp7AU5heiesrRTTe%2BKICKgzpadA%2FESbQ7WOFlB%2Ftwn1tWBc1JC8wVo0tYK7o4NK6D3r8ELvjq7cg4hO%2FyWKe%2BtpAU%2FwFWnA7jQ9GteMY2fvqXjE%2FgHxlIxYBdLNcf%2Blap%2BnMYNLsiMe7DyKEr%2BtUu6KA6eiP86%2Fc%2BnAvcERj3YqDVa820%2FRx&X-Amz-Signature=e4f1b494ceb29de5fcb420902a3c19099867c67ee14f0b98dd23ce088b94f44a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4Q3UPI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDtIvWePub6YmhmgKft3uFvsCbo916wn0q%2BHdXT9NVvsgIhAOImyBEES2wdd1p90Hf%2F%2F5hmteJIjAKdYM%2F%2F5LcdgHPlKv8DCEAQABoMNjM3NDIzMTgzODA1IgxdxdWRn0tdpvlN%2BlMq3AO0EXrdH8gkUIPsxmdNdrUWEnIUIp1E7BsdDPnmyTkMLCvLYAv%2F6KgnRtaydtfRRefGHygEFZtx%2Bs%2FcTYifgFsOEx8VqsJLTv90VGYhfNPOeng%2F45QBs26wlBp0CDx43hMH5dBgJMJiA9bWWFbOEadmihgkrgHscyLNpWaIxj95OBXzvo29rlz4sVkHr7WqtlZPtsmKmsWxm6Rko57dMYi5HsuiyLmr%2ByWD66EUShZDbm0ypNpUfYRXINDEb2McR09H32NjtnQvfiaIGwQCCd1m2tdhVnCvPtrnhk5iMyCj128vvsScupYcEYDhuQIC8bBd3MSrgNtP%2FVC4rbOBkyNsG1lw5qR9s%2FtdaZVLpsiak0icpEs%2FY%2BUGafDT1MY6D2rfmgDrbIMz2cNCrdpPGIu37EjP0gXxH8sMXh2mbdG1wY6BfEIvwvrANWyZprmwUBmnEjWzntEBOewn3XpBVJjHah%2BD%2Bu%2B6YyuhoE8XGrvLAdBZc6V7wzAfvb%2FA3Sxsm5YAHEs3jBUibo644LXRxay62P5p9PL5yubDhb9vPXnPtJw0uZdVRsbsmzerMXKjFJsPv8uLQ751An%2FkyQCIxUxP6gui9Wsb8tLMyVY9%2FcITraoJ%2FhXrGJteBjr4QjDHlYy9BjqkAVe1upfHbWKZiJZSEiRGqwjqipxbMEnkkzNFwGS6tp7AU5heiesrRTTe%2BKICKgzpadA%2FESbQ7WOFlB%2Ftwn1tWBc1JC8wVo0tYK7o4NK6D3r8ELvjq7cg4hO%2FyWKe%2BtpAU%2FwFWnA7jQ9GteMY2fvqXjE%2FgHxlIxYBdLNcf%2Blap%2BnMYNLsiMe7DyKEr%2BtUu6KA6eiP86%2Fc%2BnAvcERj3YqDVa820%2FRx&X-Amz-Signature=eca2dadefbafa2cc0f3ffc16b5f6b24a7a1bd6e3eaa57c65b02cdb3c02141924&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4Q3UPI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDtIvWePub6YmhmgKft3uFvsCbo916wn0q%2BHdXT9NVvsgIhAOImyBEES2wdd1p90Hf%2F%2F5hmteJIjAKdYM%2F%2F5LcdgHPlKv8DCEAQABoMNjM3NDIzMTgzODA1IgxdxdWRn0tdpvlN%2BlMq3AO0EXrdH8gkUIPsxmdNdrUWEnIUIp1E7BsdDPnmyTkMLCvLYAv%2F6KgnRtaydtfRRefGHygEFZtx%2Bs%2FcTYifgFsOEx8VqsJLTv90VGYhfNPOeng%2F45QBs26wlBp0CDx43hMH5dBgJMJiA9bWWFbOEadmihgkrgHscyLNpWaIxj95OBXzvo29rlz4sVkHr7WqtlZPtsmKmsWxm6Rko57dMYi5HsuiyLmr%2ByWD66EUShZDbm0ypNpUfYRXINDEb2McR09H32NjtnQvfiaIGwQCCd1m2tdhVnCvPtrnhk5iMyCj128vvsScupYcEYDhuQIC8bBd3MSrgNtP%2FVC4rbOBkyNsG1lw5qR9s%2FtdaZVLpsiak0icpEs%2FY%2BUGafDT1MY6D2rfmgDrbIMz2cNCrdpPGIu37EjP0gXxH8sMXh2mbdG1wY6BfEIvwvrANWyZprmwUBmnEjWzntEBOewn3XpBVJjHah%2BD%2Bu%2B6YyuhoE8XGrvLAdBZc6V7wzAfvb%2FA3Sxsm5YAHEs3jBUibo644LXRxay62P5p9PL5yubDhb9vPXnPtJw0uZdVRsbsmzerMXKjFJsPv8uLQ751An%2FkyQCIxUxP6gui9Wsb8tLMyVY9%2FcITraoJ%2FhXrGJteBjr4QjDHlYy9BjqkAVe1upfHbWKZiJZSEiRGqwjqipxbMEnkkzNFwGS6tp7AU5heiesrRTTe%2BKICKgzpadA%2FESbQ7WOFlB%2Ftwn1tWBc1JC8wVo0tYK7o4NK6D3r8ELvjq7cg4hO%2FyWKe%2BtpAU%2FwFWnA7jQ9GteMY2fvqXjE%2FgHxlIxYBdLNcf%2Blap%2BnMYNLsiMe7DyKEr%2BtUu6KA6eiP86%2Fc%2BnAvcERj3YqDVa820%2FRx&X-Amz-Signature=c767b1a8097b35755612a97212911d6bcfc196d240f36360385a5c0124852698&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4Q3UPI5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQDtIvWePub6YmhmgKft3uFvsCbo916wn0q%2BHdXT9NVvsgIhAOImyBEES2wdd1p90Hf%2F%2F5hmteJIjAKdYM%2F%2F5LcdgHPlKv8DCEAQABoMNjM3NDIzMTgzODA1IgxdxdWRn0tdpvlN%2BlMq3AO0EXrdH8gkUIPsxmdNdrUWEnIUIp1E7BsdDPnmyTkMLCvLYAv%2F6KgnRtaydtfRRefGHygEFZtx%2Bs%2FcTYifgFsOEx8VqsJLTv90VGYhfNPOeng%2F45QBs26wlBp0CDx43hMH5dBgJMJiA9bWWFbOEadmihgkrgHscyLNpWaIxj95OBXzvo29rlz4sVkHr7WqtlZPtsmKmsWxm6Rko57dMYi5HsuiyLmr%2ByWD66EUShZDbm0ypNpUfYRXINDEb2McR09H32NjtnQvfiaIGwQCCd1m2tdhVnCvPtrnhk5iMyCj128vvsScupYcEYDhuQIC8bBd3MSrgNtP%2FVC4rbOBkyNsG1lw5qR9s%2FtdaZVLpsiak0icpEs%2FY%2BUGafDT1MY6D2rfmgDrbIMz2cNCrdpPGIu37EjP0gXxH8sMXh2mbdG1wY6BfEIvwvrANWyZprmwUBmnEjWzntEBOewn3XpBVJjHah%2BD%2Bu%2B6YyuhoE8XGrvLAdBZc6V7wzAfvb%2FA3Sxsm5YAHEs3jBUibo644LXRxay62P5p9PL5yubDhb9vPXnPtJw0uZdVRsbsmzerMXKjFJsPv8uLQ751An%2FkyQCIxUxP6gui9Wsb8tLMyVY9%2FcITraoJ%2FhXrGJteBjr4QjDHlYy9BjqkAVe1upfHbWKZiJZSEiRGqwjqipxbMEnkkzNFwGS6tp7AU5heiesrRTTe%2BKICKgzpadA%2FESbQ7WOFlB%2Ftwn1tWBc1JC8wVo0tYK7o4NK6D3r8ELvjq7cg4hO%2FyWKe%2BtpAU%2FwFWnA7jQ9GteMY2fvqXjE%2FgHxlIxYBdLNcf%2Blap%2BnMYNLsiMe7DyKEr%2BtUu6KA6eiP86%2Fc%2BnAvcERj3YqDVa820%2FRx&X-Amz-Signature=39510eedece975d6dba1a3e97fd8aa2d79cba56c6b4c336ede6ba686fdd64900&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3PWJSAN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCIHiDNxM1jJE8uLET4aEtrmyHbwJ7iY0EuZaa%2FedCQkbNAiBilpqFASPXgjwMsF7MHX0eNy6Yujs9rWZkIwSJ6OfXISr%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMaMa5NreZ9nx35aRMKtwDgIVJs%2FuPUyLlJfQ24NXEGLvhheSMtRm4V%2BjHIJDRBMfE%2FdTEi5sTlHwfwSN3inGILfsNOAaIK94U5A6YXgVSCHZ0mD2fMSRqtF8q%2BFhfeYykh8DYNj3rEI1lSs%2FuWMB09ui4KfvKVun1ZGocZBF1OU8Y%2BTNDNUbrP9Wv2uDcbkdg5byKjQ1bjmY%2Fo6P9uEZrwL7rr6uLfFs%2BLatazPWK82TqlMSgxhowbUpxBsMIiFYm2k%2BbkQ8BOD8t87N%2F6IbUZW1TR9p%2BJ4rlVa%2FlpLw7CQbe810wJ7cTqepaaPc1DuYCQLraTFSIQXhfVgSTU3RG%2Bjn48wBmrJ3YWyHSIVLwbEKX%2FheKSb2TWL%2BL2fiaglhWonN5qbgI0qW6td0aRsOGr7FnLo9WCkM2nbWHd%2FD1VpZwZHXSa0C0QES78cyxLN1SbUDBcgmMEyXabx%2FjJDHUD0urqOwuJ6mHNBMWROXQzp8hXo5Akx%2BzDmdTqWMMgxNv4OEN0Wf24WCIkuxT3vYWx0NPDF0q6rS74mQJmjJyH6hKhw6wLhJRTrdBsA6ZgwAobiL7BL82x2phvs0qqPBYkVLgRl2pRKgxMUdP6%2BNXljqi2uiCj7GFt7Yiccmj%2BOgjc2RISXUQwgDukyow3JWMvQY6pgHlbgByAAHy11hRwxRK7uUy68fTQo1uq981fR0qhDzMrDzd3%2FvEJE0wDj%2FKUJUqe3mFPV651k2J%2BD2DbLCxM5q353RD%2Ba1nNhCKa8UKC2Ergs5fxLfMx%2B%2B4QVxpHEjnDSzdEyYZHDNSSka2U3zK%2BKKhcuc3JalNiIws%2BnzCIykVZI9hNaz0%2BvSfYA4MVIbuJFCdLM9a7Qv8NG%2BctG76SK9E8biL9BZ3&X-Amz-Signature=7b14cb55f09158b5befe0f7989cad00038a5bfa14ce02043a153d161f5c409ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666PBRHGNY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIEfHg1Y4HzexoB9lLU5ZgsYv8FkmdigYIEn8g2tS9VOIAiEA%2BTg2UCiC8q83R3IuyABdjUeRmjSy7vIJ6AIGDL1lMMwq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDFCsvOMKMHjIaizahCrcAxPi6Ro%2BiXT3keUPoIzgN%2FlzBoSDlKUqui703luZIK%2FmhFUkH%2BmlSdNDuIQHwr9KzdYsfFowzygF1%2FR5Wb5pmqZ2xmODraGsAOzTAylHrEYXbscOxcGGm5ZMMoJCAyeOprLriTv9kOEsbI3MaTgiBwo2eOe3eI%2FVlx7%2Fy5tiHSfnrYt%2FJjBnUEaiZoRYZLOVZUej4yqm9bfuVKAB0u8ATvntl3xUQ20NhM8kpkzsiZMul98RYb5MVCQ04JC8IG%2FC71OYiCw7pzAtzA%2FCDkXEyVvo9wkvlKonUImzQ%2BljEhfmj2AyBaNzz87rpN9dAGqrstvLJOW1jIhUtEPE1Lwnj4BpMoaJjjo7g17pxsf8ScmBx1PmaYlDa726NHskb6FmwLdvV%2FxYvFuRb6hYl%2FBoE4qJbAQ9639cWHUIzG7mK4Xfwi6N6my%2FvXO8yeOO62467L3ngLGGA%2FDxwWmv1dMGRd2kQrCSHQiRlpk%2F4%2B%2B4LdEi2%2Fm20jy4FftnX9Uz7VinN1mye2ob7H%2FOSysrNjxsclzmFV9%2FlvcYziJoVQ%2FbaJnmXKN2fp8UbHMoJEQDsyWI52busx6lh0zcpp6hmvjysjUPUnlybmt7QHRlLIEXjrWuEZUCCmCz3Wz3xELXMMyVjL0GOqUB%2Fq9QR75KzyJE7ITk3h8PyclkScKrOgk%2Fl2JXMobbVaCCGo7mT%2FAPakTYSOD4TPq2rGAf1X579b9W%2FjQ6%2F3fOCk8vrPRkgmYp13nvcCapXsTae42AGQFF0yDie8otXqniCyGJOtw7vQ7tpjFsibxC8Ien1046S0xGnzlR3XRYzN8ltdUuoxAHzqny1iTxjmjyJXAn%2FLIwUUSDGsmN%2Bc7in128a4V8&X-Amz-Signature=dc86ffba78b2537dfa0e2f65b9a9f66744506c6380b1060764dfdc29dba21a52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3NE65IC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCICwVFrHp%2FKLBMINptDrL%2BHbhV37%2BKad1GTS5qBwhBvekAiBbu7P%2BKSSoeMJoV4nSGgkxB63ODbt07QDRtySbng1RVir%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMAd%2F3ykzB%2BiwMpi49KtwDNXLBn7juGTREZB0kcCKTR278Nb5byxdyTBshduaicqDVMnFpHZJpFlLIYtl8z09sCSAjx6RFJAgCz5BmgkY%2B9b%2FRthQanuESttTCSeb3Hzdize%2FHX9NLYghyaJMNIxVFw5jRPMvecZfOvjUoZGKU50msyD9MFVydKqAiJlwv1d%2FoYvfoxMudZTl24aKREQtIYuQLET9%2FlGj%2BgkkwFQrLE0GHWuhNRuamsSRw5hUf4fKL%2BjzRNNwHHPNen2UtMpBZ87lq9GPJFXklUbRJuAZ0JEoGONRzBvzdhjtmx3PNwAa18WI6WA7gB1s6s61RfEqH0Asud74C5aDufasrZCTPGeqDcJ5yPFtPNRBxG8jGFviONH0NYQhK2r03EBkdfh7MK9SpWzrPKd7%2F%2FfjW17sgEnwdTVXxDkojnYs%2FBagBi8iBb6SaHQwt%2BrIRFJvQ44H5xOaxmXk%2F6qLieU%2FM3tCIvd9H1Ik19RErahPE11Yl7gnMSv7qlex3xtrwAeDfEa0D9TqRdKexzYYDn%2FK6Kd4edykR8WbY2dfYkV8mWeaP%2BRKV066I1cEZl7K2Pu63C1lOu73gL2wSpnQ0lliTra56N0%2FQRRcVFCze6b2QJ3vDuQeA2M1Bl6tEIOXoJ60wsJaMvQY6pgGRSRQrXRhP5fW9v8gwqyRWB7xsO2fGa%2B%2FQLip%2BY2x0m3dzIaION3rf%2BqxjvQYJmoRxZ%2Bgmsq9493kni3AKDlbuRC3%2F1NPoMzwjPzgNpHwCS0AOK3CfkrnojfR%2B9ZkprELpTkt5fGxpCJKgsib2T6EBfgl0g%2FLPUJVZfbnx7o3Oh2jV1gHrkHlkQNBwclCguZDBrbXezs0ETXZb8vFywqEwgCFhEAiH&X-Amz-Signature=a378d487295e83a95a44868cb8cc93d06ffbd21be928660fa1333635f9701eeb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3NE65IC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T071402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJGMEQCICwVFrHp%2FKLBMINptDrL%2BHbhV37%2BKad1GTS5qBwhBvekAiBbu7P%2BKSSoeMJoV4nSGgkxB63ODbt07QDRtySbng1RVir%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMAd%2F3ykzB%2BiwMpi49KtwDNXLBn7juGTREZB0kcCKTR278Nb5byxdyTBshduaicqDVMnFpHZJpFlLIYtl8z09sCSAjx6RFJAgCz5BmgkY%2B9b%2FRthQanuESttTCSeb3Hzdize%2FHX9NLYghyaJMNIxVFw5jRPMvecZfOvjUoZGKU50msyD9MFVydKqAiJlwv1d%2FoYvfoxMudZTl24aKREQtIYuQLET9%2FlGj%2BgkkwFQrLE0GHWuhNRuamsSRw5hUf4fKL%2BjzRNNwHHPNen2UtMpBZ87lq9GPJFXklUbRJuAZ0JEoGONRzBvzdhjtmx3PNwAa18WI6WA7gB1s6s61RfEqH0Asud74C5aDufasrZCTPGeqDcJ5yPFtPNRBxG8jGFviONH0NYQhK2r03EBkdfh7MK9SpWzrPKd7%2F%2FfjW17sgEnwdTVXxDkojnYs%2FBagBi8iBb6SaHQwt%2BrIRFJvQ44H5xOaxmXk%2F6qLieU%2FM3tCIvd9H1Ik19RErahPE11Yl7gnMSv7qlex3xtrwAeDfEa0D9TqRdKexzYYDn%2FK6Kd4edykR8WbY2dfYkV8mWeaP%2BRKV066I1cEZl7K2Pu63C1lOu73gL2wSpnQ0lliTra56N0%2FQRRcVFCze6b2QJ3vDuQeA2M1Bl6tEIOXoJ60wsJaMvQY6pgGRSRQrXRhP5fW9v8gwqyRWB7xsO2fGa%2B%2FQLip%2BY2x0m3dzIaION3rf%2BqxjvQYJmoRxZ%2Bgmsq9493kni3AKDlbuRC3%2F1NPoMzwjPzgNpHwCS0AOK3CfkrnojfR%2B9ZkprELpTkt5fGxpCJKgsib2T6EBfgl0g%2FLPUJVZfbnx7o3Oh2jV1gHrkHlkQNBwclCguZDBrbXezs0ETXZb8vFywqEwgCFhEAiH&X-Amz-Signature=434103e13abe114e6e9f5de454b79905f794122893a7d8a5bf0a69e3a5e593c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
