

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GH44OBC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDsyexhb6GEn8VfoGcEVX0b%2ByH8yny0gLGm%2FNIS%2Bj9eWAiAPOzg25XubwBWFsBjTJr7oTcegRfGsuzciKn1v3M0Y0Cr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMg9PGz%2Bbxkcm%2F85zKKtwDiGAPq5scas8XYLgSX29rGRLtcwSP0HZf%2BsicuEskSOL7q16AdGyUPPCYZPWrmYDqKrXFqOxWUOUnHv767MEiQiJXGANQGn%2F3b1RymUDBna7phSXc5I4lpR%2FmHIIClVnuz64m2XnyiR5iqbvRzcNkuxkEO204Tfl%2Fkbzf2gTfEnOuctA4yjO4hgh%2FizRMMjsLYlY4UdfthZDRHehgbh1Dmek10p4U%2FpY7zVr%2FwDcySw7EJu1q6PMNHOCd1VQ7wNMta9OH998aKNRWCLcGuj07flfrH0pSPfUu334wKUjzZ3ne5SqhCyuOPTdPmgAYzkxRskO44JMIgOfJmNc2iCd8q3t4U3u0lbNnr2P9mYh49lGzYqLTqBQ8fmR30TinCvzNpm0NWvQX2%2BP8zfs%2FoMDQjoNaXNhDU%2BJbQav0YWqFcdsFcDCI8HpfdLukFiEX6AT6bDOI6h25W1feEPfLCqg%2BceF3%2B99SI5lhuih%2B8KAg1Klz%2FeX1KgnCvgynSegWSVyZ5Ss2VyXTb3ped2RFXVv2hNQ%2FgKBAouytOAgO0Bz%2BJl%2Bpx%2BYjE4WeAHoMbosKLmGNPA1KFRhsqjhERHQxucJnkPibgaPGfLHqp0uV0TEG5BjxJ04PW0l9oAqhUosw%2FbDlvAY6pgE6oenICo8bOiDfloShihR2e1iArm5DwXpQXymoNSdVktVkBTmKByFWgBKF1Rwnqrx%2BMytTadi4Hxasqr4gFzG%2B2CnP0u3g2c6e8a1h20VSeAROXClxk0RAUJrfw1toqvSZLx2VGf9eUpqNGp88erqzDwq8Mqh7PAEAs6GI9xdaNVqZ6B6h14bXTk9cEZkvGqpGPg669OafF0N24Z2Sk8gl0BZ3j0t3&X-Amz-Signature=09d5bbe555e344c3d47e1ae3ac3fa1aff544d220ff6f2d4effb4fc3d267e5056&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GH44OBC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDsyexhb6GEn8VfoGcEVX0b%2ByH8yny0gLGm%2FNIS%2Bj9eWAiAPOzg25XubwBWFsBjTJr7oTcegRfGsuzciKn1v3M0Y0Cr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMg9PGz%2Bbxkcm%2F85zKKtwDiGAPq5scas8XYLgSX29rGRLtcwSP0HZf%2BsicuEskSOL7q16AdGyUPPCYZPWrmYDqKrXFqOxWUOUnHv767MEiQiJXGANQGn%2F3b1RymUDBna7phSXc5I4lpR%2FmHIIClVnuz64m2XnyiR5iqbvRzcNkuxkEO204Tfl%2Fkbzf2gTfEnOuctA4yjO4hgh%2FizRMMjsLYlY4UdfthZDRHehgbh1Dmek10p4U%2FpY7zVr%2FwDcySw7EJu1q6PMNHOCd1VQ7wNMta9OH998aKNRWCLcGuj07flfrH0pSPfUu334wKUjzZ3ne5SqhCyuOPTdPmgAYzkxRskO44JMIgOfJmNc2iCd8q3t4U3u0lbNnr2P9mYh49lGzYqLTqBQ8fmR30TinCvzNpm0NWvQX2%2BP8zfs%2FoMDQjoNaXNhDU%2BJbQav0YWqFcdsFcDCI8HpfdLukFiEX6AT6bDOI6h25W1feEPfLCqg%2BceF3%2B99SI5lhuih%2B8KAg1Klz%2FeX1KgnCvgynSegWSVyZ5Ss2VyXTb3ped2RFXVv2hNQ%2FgKBAouytOAgO0Bz%2BJl%2Bpx%2BYjE4WeAHoMbosKLmGNPA1KFRhsqjhERHQxucJnkPibgaPGfLHqp0uV0TEG5BjxJ04PW0l9oAqhUosw%2FbDlvAY6pgE6oenICo8bOiDfloShihR2e1iArm5DwXpQXymoNSdVktVkBTmKByFWgBKF1Rwnqrx%2BMytTadi4Hxasqr4gFzG%2B2CnP0u3g2c6e8a1h20VSeAROXClxk0RAUJrfw1toqvSZLx2VGf9eUpqNGp88erqzDwq8Mqh7PAEAs6GI9xdaNVqZ6B6h14bXTk9cEZkvGqpGPg669OafF0N24Z2Sk8gl0BZ3j0t3&X-Amz-Signature=bf37ec9fe23ee81a3410b2310c091c2a357f3169ed2570104960e46602b08fb1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GH44OBC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDsyexhb6GEn8VfoGcEVX0b%2ByH8yny0gLGm%2FNIS%2Bj9eWAiAPOzg25XubwBWFsBjTJr7oTcegRfGsuzciKn1v3M0Y0Cr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMg9PGz%2Bbxkcm%2F85zKKtwDiGAPq5scas8XYLgSX29rGRLtcwSP0HZf%2BsicuEskSOL7q16AdGyUPPCYZPWrmYDqKrXFqOxWUOUnHv767MEiQiJXGANQGn%2F3b1RymUDBna7phSXc5I4lpR%2FmHIIClVnuz64m2XnyiR5iqbvRzcNkuxkEO204Tfl%2Fkbzf2gTfEnOuctA4yjO4hgh%2FizRMMjsLYlY4UdfthZDRHehgbh1Dmek10p4U%2FpY7zVr%2FwDcySw7EJu1q6PMNHOCd1VQ7wNMta9OH998aKNRWCLcGuj07flfrH0pSPfUu334wKUjzZ3ne5SqhCyuOPTdPmgAYzkxRskO44JMIgOfJmNc2iCd8q3t4U3u0lbNnr2P9mYh49lGzYqLTqBQ8fmR30TinCvzNpm0NWvQX2%2BP8zfs%2FoMDQjoNaXNhDU%2BJbQav0YWqFcdsFcDCI8HpfdLukFiEX6AT6bDOI6h25W1feEPfLCqg%2BceF3%2B99SI5lhuih%2B8KAg1Klz%2FeX1KgnCvgynSegWSVyZ5Ss2VyXTb3ped2RFXVv2hNQ%2FgKBAouytOAgO0Bz%2BJl%2Bpx%2BYjE4WeAHoMbosKLmGNPA1KFRhsqjhERHQxucJnkPibgaPGfLHqp0uV0TEG5BjxJ04PW0l9oAqhUosw%2FbDlvAY6pgE6oenICo8bOiDfloShihR2e1iArm5DwXpQXymoNSdVktVkBTmKByFWgBKF1Rwnqrx%2BMytTadi4Hxasqr4gFzG%2B2CnP0u3g2c6e8a1h20VSeAROXClxk0RAUJrfw1toqvSZLx2VGf9eUpqNGp88erqzDwq8Mqh7PAEAs6GI9xdaNVqZ6B6h14bXTk9cEZkvGqpGPg669OafF0N24Z2Sk8gl0BZ3j0t3&X-Amz-Signature=17cbf3f0f049a38077d99144068f1b66f64f9f3408c3b112468cb562c1a6ed5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GH44OBC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDsyexhb6GEn8VfoGcEVX0b%2ByH8yny0gLGm%2FNIS%2Bj9eWAiAPOzg25XubwBWFsBjTJr7oTcegRfGsuzciKn1v3M0Y0Cr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMg9PGz%2Bbxkcm%2F85zKKtwDiGAPq5scas8XYLgSX29rGRLtcwSP0HZf%2BsicuEskSOL7q16AdGyUPPCYZPWrmYDqKrXFqOxWUOUnHv767MEiQiJXGANQGn%2F3b1RymUDBna7phSXc5I4lpR%2FmHIIClVnuz64m2XnyiR5iqbvRzcNkuxkEO204Tfl%2Fkbzf2gTfEnOuctA4yjO4hgh%2FizRMMjsLYlY4UdfthZDRHehgbh1Dmek10p4U%2FpY7zVr%2FwDcySw7EJu1q6PMNHOCd1VQ7wNMta9OH998aKNRWCLcGuj07flfrH0pSPfUu334wKUjzZ3ne5SqhCyuOPTdPmgAYzkxRskO44JMIgOfJmNc2iCd8q3t4U3u0lbNnr2P9mYh49lGzYqLTqBQ8fmR30TinCvzNpm0NWvQX2%2BP8zfs%2FoMDQjoNaXNhDU%2BJbQav0YWqFcdsFcDCI8HpfdLukFiEX6AT6bDOI6h25W1feEPfLCqg%2BceF3%2B99SI5lhuih%2B8KAg1Klz%2FeX1KgnCvgynSegWSVyZ5Ss2VyXTb3ped2RFXVv2hNQ%2FgKBAouytOAgO0Bz%2BJl%2Bpx%2BYjE4WeAHoMbosKLmGNPA1KFRhsqjhERHQxucJnkPibgaPGfLHqp0uV0TEG5BjxJ04PW0l9oAqhUosw%2FbDlvAY6pgE6oenICo8bOiDfloShihR2e1iArm5DwXpQXymoNSdVktVkBTmKByFWgBKF1Rwnqrx%2BMytTadi4Hxasqr4gFzG%2B2CnP0u3g2c6e8a1h20VSeAROXClxk0RAUJrfw1toqvSZLx2VGf9eUpqNGp88erqzDwq8Mqh7PAEAs6GI9xdaNVqZ6B6h14bXTk9cEZkvGqpGPg669OafF0N24Z2Sk8gl0BZ3j0t3&X-Amz-Signature=1a1ed8d235b2a1c60638397acf494e03eda3003526e97665d1f1c0cbd5a34096&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GH44OBC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDsyexhb6GEn8VfoGcEVX0b%2ByH8yny0gLGm%2FNIS%2Bj9eWAiAPOzg25XubwBWFsBjTJr7oTcegRfGsuzciKn1v3M0Y0Cr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMg9PGz%2Bbxkcm%2F85zKKtwDiGAPq5scas8XYLgSX29rGRLtcwSP0HZf%2BsicuEskSOL7q16AdGyUPPCYZPWrmYDqKrXFqOxWUOUnHv767MEiQiJXGANQGn%2F3b1RymUDBna7phSXc5I4lpR%2FmHIIClVnuz64m2XnyiR5iqbvRzcNkuxkEO204Tfl%2Fkbzf2gTfEnOuctA4yjO4hgh%2FizRMMjsLYlY4UdfthZDRHehgbh1Dmek10p4U%2FpY7zVr%2FwDcySw7EJu1q6PMNHOCd1VQ7wNMta9OH998aKNRWCLcGuj07flfrH0pSPfUu334wKUjzZ3ne5SqhCyuOPTdPmgAYzkxRskO44JMIgOfJmNc2iCd8q3t4U3u0lbNnr2P9mYh49lGzYqLTqBQ8fmR30TinCvzNpm0NWvQX2%2BP8zfs%2FoMDQjoNaXNhDU%2BJbQav0YWqFcdsFcDCI8HpfdLukFiEX6AT6bDOI6h25W1feEPfLCqg%2BceF3%2B99SI5lhuih%2B8KAg1Klz%2FeX1KgnCvgynSegWSVyZ5Ss2VyXTb3ped2RFXVv2hNQ%2FgKBAouytOAgO0Bz%2BJl%2Bpx%2BYjE4WeAHoMbosKLmGNPA1KFRhsqjhERHQxucJnkPibgaPGfLHqp0uV0TEG5BjxJ04PW0l9oAqhUosw%2FbDlvAY6pgE6oenICo8bOiDfloShihR2e1iArm5DwXpQXymoNSdVktVkBTmKByFWgBKF1Rwnqrx%2BMytTadi4Hxasqr4gFzG%2B2CnP0u3g2c6e8a1h20VSeAROXClxk0RAUJrfw1toqvSZLx2VGf9eUpqNGp88erqzDwq8Mqh7PAEAs6GI9xdaNVqZ6B6h14bXTk9cEZkvGqpGPg669OafF0N24Z2Sk8gl0BZ3j0t3&X-Amz-Signature=84b12fff2f9428e6016a5cdb21fc773cb9c9c49806ae4e609a735c9df91e1c16&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GH44OBC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDsyexhb6GEn8VfoGcEVX0b%2ByH8yny0gLGm%2FNIS%2Bj9eWAiAPOzg25XubwBWFsBjTJr7oTcegRfGsuzciKn1v3M0Y0Cr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMg9PGz%2Bbxkcm%2F85zKKtwDiGAPq5scas8XYLgSX29rGRLtcwSP0HZf%2BsicuEskSOL7q16AdGyUPPCYZPWrmYDqKrXFqOxWUOUnHv767MEiQiJXGANQGn%2F3b1RymUDBna7phSXc5I4lpR%2FmHIIClVnuz64m2XnyiR5iqbvRzcNkuxkEO204Tfl%2Fkbzf2gTfEnOuctA4yjO4hgh%2FizRMMjsLYlY4UdfthZDRHehgbh1Dmek10p4U%2FpY7zVr%2FwDcySw7EJu1q6PMNHOCd1VQ7wNMta9OH998aKNRWCLcGuj07flfrH0pSPfUu334wKUjzZ3ne5SqhCyuOPTdPmgAYzkxRskO44JMIgOfJmNc2iCd8q3t4U3u0lbNnr2P9mYh49lGzYqLTqBQ8fmR30TinCvzNpm0NWvQX2%2BP8zfs%2FoMDQjoNaXNhDU%2BJbQav0YWqFcdsFcDCI8HpfdLukFiEX6AT6bDOI6h25W1feEPfLCqg%2BceF3%2B99SI5lhuih%2B8KAg1Klz%2FeX1KgnCvgynSegWSVyZ5Ss2VyXTb3ped2RFXVv2hNQ%2FgKBAouytOAgO0Bz%2BJl%2Bpx%2BYjE4WeAHoMbosKLmGNPA1KFRhsqjhERHQxucJnkPibgaPGfLHqp0uV0TEG5BjxJ04PW0l9oAqhUosw%2FbDlvAY6pgE6oenICo8bOiDfloShihR2e1iArm5DwXpQXymoNSdVktVkBTmKByFWgBKF1Rwnqrx%2BMytTadi4Hxasqr4gFzG%2B2CnP0u3g2c6e8a1h20VSeAROXClxk0RAUJrfw1toqvSZLx2VGf9eUpqNGp88erqzDwq8Mqh7PAEAs6GI9xdaNVqZ6B6h14bXTk9cEZkvGqpGPg669OafF0N24Z2Sk8gl0BZ3j0t3&X-Amz-Signature=09d1b5528297f4c955c3d0cc6582b8d7c4c63c46758af0a4d16f6606b8507c3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GH44OBC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDsyexhb6GEn8VfoGcEVX0b%2ByH8yny0gLGm%2FNIS%2Bj9eWAiAPOzg25XubwBWFsBjTJr7oTcegRfGsuzciKn1v3M0Y0Cr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMg9PGz%2Bbxkcm%2F85zKKtwDiGAPq5scas8XYLgSX29rGRLtcwSP0HZf%2BsicuEskSOL7q16AdGyUPPCYZPWrmYDqKrXFqOxWUOUnHv767MEiQiJXGANQGn%2F3b1RymUDBna7phSXc5I4lpR%2FmHIIClVnuz64m2XnyiR5iqbvRzcNkuxkEO204Tfl%2Fkbzf2gTfEnOuctA4yjO4hgh%2FizRMMjsLYlY4UdfthZDRHehgbh1Dmek10p4U%2FpY7zVr%2FwDcySw7EJu1q6PMNHOCd1VQ7wNMta9OH998aKNRWCLcGuj07flfrH0pSPfUu334wKUjzZ3ne5SqhCyuOPTdPmgAYzkxRskO44JMIgOfJmNc2iCd8q3t4U3u0lbNnr2P9mYh49lGzYqLTqBQ8fmR30TinCvzNpm0NWvQX2%2BP8zfs%2FoMDQjoNaXNhDU%2BJbQav0YWqFcdsFcDCI8HpfdLukFiEX6AT6bDOI6h25W1feEPfLCqg%2BceF3%2B99SI5lhuih%2B8KAg1Klz%2FeX1KgnCvgynSegWSVyZ5Ss2VyXTb3ped2RFXVv2hNQ%2FgKBAouytOAgO0Bz%2BJl%2Bpx%2BYjE4WeAHoMbosKLmGNPA1KFRhsqjhERHQxucJnkPibgaPGfLHqp0uV0TEG5BjxJ04PW0l9oAqhUosw%2FbDlvAY6pgE6oenICo8bOiDfloShihR2e1iArm5DwXpQXymoNSdVktVkBTmKByFWgBKF1Rwnqrx%2BMytTadi4Hxasqr4gFzG%2B2CnP0u3g2c6e8a1h20VSeAROXClxk0RAUJrfw1toqvSZLx2VGf9eUpqNGp88erqzDwq8Mqh7PAEAs6GI9xdaNVqZ6B6h14bXTk9cEZkvGqpGPg669OafF0N24Z2Sk8gl0BZ3j0t3&X-Amz-Signature=cd29186a391f7dcc0d7c4e46f2a69baa6ce61c236dc2871faceaf8725b0db148&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GH44OBC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDsyexhb6GEn8VfoGcEVX0b%2ByH8yny0gLGm%2FNIS%2Bj9eWAiAPOzg25XubwBWFsBjTJr7oTcegRfGsuzciKn1v3M0Y0Cr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMg9PGz%2Bbxkcm%2F85zKKtwDiGAPq5scas8XYLgSX29rGRLtcwSP0HZf%2BsicuEskSOL7q16AdGyUPPCYZPWrmYDqKrXFqOxWUOUnHv767MEiQiJXGANQGn%2F3b1RymUDBna7phSXc5I4lpR%2FmHIIClVnuz64m2XnyiR5iqbvRzcNkuxkEO204Tfl%2Fkbzf2gTfEnOuctA4yjO4hgh%2FizRMMjsLYlY4UdfthZDRHehgbh1Dmek10p4U%2FpY7zVr%2FwDcySw7EJu1q6PMNHOCd1VQ7wNMta9OH998aKNRWCLcGuj07flfrH0pSPfUu334wKUjzZ3ne5SqhCyuOPTdPmgAYzkxRskO44JMIgOfJmNc2iCd8q3t4U3u0lbNnr2P9mYh49lGzYqLTqBQ8fmR30TinCvzNpm0NWvQX2%2BP8zfs%2FoMDQjoNaXNhDU%2BJbQav0YWqFcdsFcDCI8HpfdLukFiEX6AT6bDOI6h25W1feEPfLCqg%2BceF3%2B99SI5lhuih%2B8KAg1Klz%2FeX1KgnCvgynSegWSVyZ5Ss2VyXTb3ped2RFXVv2hNQ%2FgKBAouytOAgO0Bz%2BJl%2Bpx%2BYjE4WeAHoMbosKLmGNPA1KFRhsqjhERHQxucJnkPibgaPGfLHqp0uV0TEG5BjxJ04PW0l9oAqhUosw%2FbDlvAY6pgE6oenICo8bOiDfloShihR2e1iArm5DwXpQXymoNSdVktVkBTmKByFWgBKF1Rwnqrx%2BMytTadi4Hxasqr4gFzG%2B2CnP0u3g2c6e8a1h20VSeAROXClxk0RAUJrfw1toqvSZLx2VGf9eUpqNGp88erqzDwq8Mqh7PAEAs6GI9xdaNVqZ6B6h14bXTk9cEZkvGqpGPg669OafF0N24Z2Sk8gl0BZ3j0t3&X-Amz-Signature=ea199bc5300e8cbe7fa6056af2d96051c5f53ae2561168751fc472f10fd9589f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z6FGCYX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDUB2sZhRuaCkbQDftbELsBRzG6MJOKxt%2BxfhYYVGbnzwIhAJUQuTwBWCQRZtscfJufhzpTXKb5MkQDqQ0R4ElDGW7fKv8DCH8QABoMNjM3NDIzMTgzODA1Igzjc%2BYrPXi7eN4aKSoq3AM36UeqJzAXuaK8B6vmQ1qHK4RPWuVf9%2B41CLv431K2KMIBytxVkNZIc5CGU6q4%2F1NSG6uFzU%2FunpNGxszTjKDDnPiX5R9aNscYNRfCOvQEhQ77cQnEFkhd94eTMt5D86AW6jPKUNaaC0PksRZFaFGDisJL2x59l1ttVz%2FYLKce80zT1%2Fm5jz6x%2FKvNAG4FUNoO3TZgGd6OGJBwgfBixtDhKHbB4QqqzWJ4FPiDSVSia7UXhukc3sgnmRjXyuuOngCLj0Q8DbkWHrdSxkBFxrZD1OiEAITk3Fp%2FrHYvyaAaXqCTd%2FZtyDN5XGZVnDiigg6oUmmiZw61LsSwa1Whc4NHqfagr9QKQq0K0XtPdbcPTrJuGnyvmSxINTimMKEk13YgkkuVFBxWhX%2BNHVII8icmnyz%2F2plFZV7djC72%2FDwzwWYKPWzykCRpbcOnzSTAFPXNF3R4fZo7DJkDQh1ehD20RY4xlFB2%2ByGfj4Fhsks3a%2Bi%2FdZvVfFm30fmqpdr73y%2Brt7PPf%2FDUEZhI9d%2ByNKZqlSdYihz5OPL7ozuj%2F4REXvBptSfZmgLqeUKMi3NNkMDMZWM4gQ1vZuU3LRAXPvecaU6twKttnDmcyhQuJFAJj5Eytj1Bk6PX59LfbjDesOW8BjqkAWpmSGSjEoU%2B2eBv33EdwpPCTkg6H5HUnjEOLiqkI1IbSg4mMjp7ABt%2B0cR%2F3ZdePjmYUFwUUkZG52fcZAlIEo4ZfDyDnxv6RgKlwJ48ZhtB%2F9UEUtC5OfWCmSQvxfdDh1VFv2uJ%2F2R%2FqIPfU2gYy0giAHgc65dTunSWsecvpm3Ga2FqWfIT2FWqu8Bt0UlfDH6jo8Yn7wA0qLnh2tf5iipAa8RW&X-Amz-Signature=1609b4f9f391d5b87fcb3d150b0ff4c23b35eb53656b434795e88f0243c32cd8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LQSMXPF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIDHSX7mRsa6LxKa6ehduOUml%2F6L7XcB1nJzSvEfjwu%2BdAiBBBYBLUEOEvrvNuFnou5y0KfG%2F5K1ahIVNCF5kS09m2yr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJBbVd3FMNQnIyznSKtwDi2scdbota0lRCm9LoPvRMM5FVIrD0dsDcbSCneoPprbvZRABBFIaHDSjiuLg2c8cdI9f9KaM4tLmOawnHT%2FOmryBKpzLxIAVuRZPwi4L%2FxkimVVLSWRWrIXO%2FwW7ZddSk38li9iRwf%2BGzlDKMhuer6nif47wyYAfu9c1f%2Bp1qAvnIpSCo5SqT6WnWVrZLo1bRmwZfo1h7ScGKCPKP9nmDHx77Bfm8B4NNOgNbMJI6qfaXVE4ACOQeJg6UEmEAUFpw8TEgT%2FEuRn5F1SCbKD5BeWYKwpH7ioUdmZKRI30yJVmDHJJ6kC5fJIjNU%2BNwruSgtvVPJ9vdv5l2lalCt%2B78Bqgm%2B38UciK3zxk9iaTmSmB0eztbOnktl7W%2F1EENMUa0ytQHMl0kaaCd0FEoKhAOYNlF%2BvYxIx75O1HPiVTk6qAoMOkJRl0ZwGw9Z7ybNIq880O6t4sTTXkgdBqtvTUKDrTIJzElhHddulHM3xi8Br9k91VDjuBf8I54wfyCEtSLQFyrNBaahXP10gtRVwKmLK9BwGJ55AZDRNzZcTrjLBOy5ldgvBe4WMgVkz0unrrK5yFaQpVgXwxtWghlWOe0T6cAsNp%2BPZNeK8GEtVumrksTFeWMCrgtKGKi90w77DlvAY6pgFr%2B5pwGoKbT2mt%2BdmoaBDXo5w5kO2acOAn3OU4SuLt5VpuhpQLR%2FZeqPBh4D23mgTkXEmawfhEp8c04uq2JIXeawCZvtIhVl1dRLPpxMsO1suO0QUpkrICx8ZfJX0lHLtFBiVDS%2B3EGrs4SlqXpxQlkbfwJ2Znvre8VusOhFvR9zAhdaMHXprsLyHW5fFEjDpaog5V6t0sMExH%2BCTRraMD9yg1MEGY&X-Amz-Signature=aa93b920e1cb312a2b0fa167f3e4460e72c346c389328e170677408e0f614805&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AZJRN55%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDc8UI%2BGmGx5a0oy08cfXfy0CCk2%2BnxictARkyNNNXo1wIhAMgUGd1j8JxYyObsvYyPa4rRBn93mFXzJ6NVOcClDeH9Kv8DCH8QABoMNjM3NDIzMTgzODA1Igxh27KiuCReo8Z6LCkq3AO5wi%2F5q1xE97VeRx01VK3NBmBlzb6rP1CtY0fXl1pfs%2FkV0IX7CtlJ82Sz72XXMPXBx8TrfaCR5G09VSCT%2BwinukQWMMnqOGuGyJ5aNha%2Fgx8vUvXUre%2FQapTZU4YnA7ayBzTJsuR7XWkgHXU846VomvU0cKQO5mJ3VjWje7QtLxvlPnFoQlTLwRs8P6%2FNIELyDpfvjt%2FSRBBz2rzzM19EbctXxRBsyJGeLpdwe0AYzi1GTDCFTnELoAhs4ai0Akq5989KeNQOaw6Uaw2Th0r987%2FWxf9xVdUj39xCDLEJTHpke%2FT%2BsSGlL7Fgvwg3Ij%2F7Y8wIQ%2FGpXwIvyE4OIyVLOQX78T%2F6x%2B%2BnesVcSWgcb%2FP5o%2B4IUG%2BVN9fr3a%2Bm4dBaEIZ0hU8XFXQuh1jUWCoMLl8FavW2zvO6MbydpPVwMfzPNOY2BjqXJ2N09lnzSVGk%2FzgRHjt2WjsuRUXMYMBFM7mgMF%2F9z717wxC7Bl0c0w8DB%2Fm6bhGmyRxWY%2F1SNKeX5P0ODOx6bpSTsAHle8xpioQZB06MXZYbNgRMESNqoGm6pywftUkpGZbN%2B%2FE4g1dvMYoaO8qXFkJHwkH1A6gSa4hS11yUm2BFeEDcJYV%2FBdiKU8KzhIDKknRWhTC0sOW8BjqkAeyoA3whihPxbxMDvUG%2FMRZW54nH4Xv9vzPHsH7cEjIcgbLCDE35X2xG5PLdb7xjzl5ZEccRK1RZ%2BgiEueb06HwSH3xJwRldKEV5LdRm4j2vgEPCMT3aROv9%2F5uThx1qsjUgGqAtKcoq7pReBxdu0xUtRypmWJug1%2BEAV8u%2BtyJCZ61RzCRF2RPlIEif7NgWbdMtTmQnZJHvtqWHvDefyLnuWJFA&X-Amz-Signature=546fdca7c3337a065eea1785e9728395bb8172c7772c5827552c6d100e9c0d60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AZJRN55%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDc8UI%2BGmGx5a0oy08cfXfy0CCk2%2BnxictARkyNNNXo1wIhAMgUGd1j8JxYyObsvYyPa4rRBn93mFXzJ6NVOcClDeH9Kv8DCH8QABoMNjM3NDIzMTgzODA1Igxh27KiuCReo8Z6LCkq3AO5wi%2F5q1xE97VeRx01VK3NBmBlzb6rP1CtY0fXl1pfs%2FkV0IX7CtlJ82Sz72XXMPXBx8TrfaCR5G09VSCT%2BwinukQWMMnqOGuGyJ5aNha%2Fgx8vUvXUre%2FQapTZU4YnA7ayBzTJsuR7XWkgHXU846VomvU0cKQO5mJ3VjWje7QtLxvlPnFoQlTLwRs8P6%2FNIELyDpfvjt%2FSRBBz2rzzM19EbctXxRBsyJGeLpdwe0AYzi1GTDCFTnELoAhs4ai0Akq5989KeNQOaw6Uaw2Th0r987%2FWxf9xVdUj39xCDLEJTHpke%2FT%2BsSGlL7Fgvwg3Ij%2F7Y8wIQ%2FGpXwIvyE4OIyVLOQX78T%2F6x%2B%2BnesVcSWgcb%2FP5o%2B4IUG%2BVN9fr3a%2Bm4dBaEIZ0hU8XFXQuh1jUWCoMLl8FavW2zvO6MbydpPVwMfzPNOY2BjqXJ2N09lnzSVGk%2FzgRHjt2WjsuRUXMYMBFM7mgMF%2F9z717wxC7Bl0c0w8DB%2Fm6bhGmyRxWY%2F1SNKeX5P0ODOx6bpSTsAHle8xpioQZB06MXZYbNgRMESNqoGm6pywftUkpGZbN%2B%2FE4g1dvMYoaO8qXFkJHwkH1A6gSa4hS11yUm2BFeEDcJYV%2FBdiKU8KzhIDKknRWhTC0sOW8BjqkAeyoA3whihPxbxMDvUG%2FMRZW54nH4Xv9vzPHsH7cEjIcgbLCDE35X2xG5PLdb7xjzl5ZEccRK1RZ%2BgiEueb06HwSH3xJwRldKEV5LdRm4j2vgEPCMT3aROv9%2F5uThx1qsjUgGqAtKcoq7pReBxdu0xUtRypmWJug1%2BEAV8u%2BtyJCZ61RzCRF2RPlIEif7NgWbdMtTmQnZJHvtqWHvDefyLnuWJFA&X-Amz-Signature=b062a87ec522f62fda7d6b0254f8a8313c176f865d313273496ebdf87f4482e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
