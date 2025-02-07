

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK3FGNCB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIAUCWlJcarCvRmwutUeSl1pPktV%2FNj3pFAEsMG5rfxWUAiEAyCXn3MzxvqZkQ2i5iuq9mPXr6TrSSRrzQ13o40n%2FnhEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDC3GkXBYpexmieWdRyrcA4%2BcBY3FKtgMHr6yEQfLP%2BKMqQe0vjqSTwJnymbYPs1kowIKUCrcxM6WrA1ZtKFE6gSLWuhXz%2FAqFRkuAKO4is8Z1J1psVzxGtprX5eOnr82AIxH57WpFosqIjiaOw%2BvSEHjzOzsT3xIdlAKV0lOAIVaKYbGXhl9h62Sr77tg2u%2Fzrfj8z9NSYtkqMVF9I9%2Fi4iL1T5k321gv8v6SxUjHLXGt91RfQQZ%2BqS7i9eErobTyZVlRMAJapqjyYTob8hLMb7eAfgYE4Lo0HjSm1ZFyxL5FapzPTmoaS3VnPDSE1HieEHUKYoaN5timcBoowzjGInfDM%2BSGMaHuteUkX%2FgzzvtIxkMJaWXNsTsue%2ByNEJCaneSnYEF8FPLJNy3923gl8YH1cKFUBTWRYW9TAt0L%2Bl4V5PsXarN0F2ovyB2Zdb2L57PJd6Ksn3KucJ40YmzplwO%2FGzXn%2B4vuO15Skrr%2BKPW0ES0USbeEyQ8VXiG3mTspc%2BiFjGBZxQL0Nfpk2JvHsBmwsY%2BLyyidCeE55xxgGqB4fI4T8rhxCm8ep8%2FdrVq6UodybFT5mUTOzYbgWt7kiabVc%2FsBr8pNyg0%2FOQ9YI1yFCsxGfKaiIS3EjazsP7b8uQt7GRRu7K7F5BfMMLSmb0GOqUBLZ567FwDbOCRcZbUBDlPwx9Y7GI4mMtf5CjU2HxjHap1az00EoyorW9sElORum0Ez4XhhCpwPiZgl00go1g1VtG6ss9IT1PRZoJRbHna1SlVFFrGD2VG6pS2x9COTS6cWGiTQoxZxoicETceFLP8puT3LxJXJ%2FosiC%2FX%2F4TpBTku3gq2EwVd7Y3Pd5pJxYcByUYvxp7uTSEDhXqTnD0G0Y5hEqtP&X-Amz-Signature=c29a252ea95c37fab5fddd1e6c20c6013542c3ae662e817be50daa5d45e6c588&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK3FGNCB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIAUCWlJcarCvRmwutUeSl1pPktV%2FNj3pFAEsMG5rfxWUAiEAyCXn3MzxvqZkQ2i5iuq9mPXr6TrSSRrzQ13o40n%2FnhEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDC3GkXBYpexmieWdRyrcA4%2BcBY3FKtgMHr6yEQfLP%2BKMqQe0vjqSTwJnymbYPs1kowIKUCrcxM6WrA1ZtKFE6gSLWuhXz%2FAqFRkuAKO4is8Z1J1psVzxGtprX5eOnr82AIxH57WpFosqIjiaOw%2BvSEHjzOzsT3xIdlAKV0lOAIVaKYbGXhl9h62Sr77tg2u%2Fzrfj8z9NSYtkqMVF9I9%2Fi4iL1T5k321gv8v6SxUjHLXGt91RfQQZ%2BqS7i9eErobTyZVlRMAJapqjyYTob8hLMb7eAfgYE4Lo0HjSm1ZFyxL5FapzPTmoaS3VnPDSE1HieEHUKYoaN5timcBoowzjGInfDM%2BSGMaHuteUkX%2FgzzvtIxkMJaWXNsTsue%2ByNEJCaneSnYEF8FPLJNy3923gl8YH1cKFUBTWRYW9TAt0L%2Bl4V5PsXarN0F2ovyB2Zdb2L57PJd6Ksn3KucJ40YmzplwO%2FGzXn%2B4vuO15Skrr%2BKPW0ES0USbeEyQ8VXiG3mTspc%2BiFjGBZxQL0Nfpk2JvHsBmwsY%2BLyyidCeE55xxgGqB4fI4T8rhxCm8ep8%2FdrVq6UodybFT5mUTOzYbgWt7kiabVc%2FsBr8pNyg0%2FOQ9YI1yFCsxGfKaiIS3EjazsP7b8uQt7GRRu7K7F5BfMMLSmb0GOqUBLZ567FwDbOCRcZbUBDlPwx9Y7GI4mMtf5CjU2HxjHap1az00EoyorW9sElORum0Ez4XhhCpwPiZgl00go1g1VtG6ss9IT1PRZoJRbHna1SlVFFrGD2VG6pS2x9COTS6cWGiTQoxZxoicETceFLP8puT3LxJXJ%2FosiC%2FX%2F4TpBTku3gq2EwVd7Y3Pd5pJxYcByUYvxp7uTSEDhXqTnD0G0Y5hEqtP&X-Amz-Signature=ab99b18194899c98a3f316479f047a11aafd493163db08610461c00c2006d023&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK3FGNCB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIAUCWlJcarCvRmwutUeSl1pPktV%2FNj3pFAEsMG5rfxWUAiEAyCXn3MzxvqZkQ2i5iuq9mPXr6TrSSRrzQ13o40n%2FnhEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDC3GkXBYpexmieWdRyrcA4%2BcBY3FKtgMHr6yEQfLP%2BKMqQe0vjqSTwJnymbYPs1kowIKUCrcxM6WrA1ZtKFE6gSLWuhXz%2FAqFRkuAKO4is8Z1J1psVzxGtprX5eOnr82AIxH57WpFosqIjiaOw%2BvSEHjzOzsT3xIdlAKV0lOAIVaKYbGXhl9h62Sr77tg2u%2Fzrfj8z9NSYtkqMVF9I9%2Fi4iL1T5k321gv8v6SxUjHLXGt91RfQQZ%2BqS7i9eErobTyZVlRMAJapqjyYTob8hLMb7eAfgYE4Lo0HjSm1ZFyxL5FapzPTmoaS3VnPDSE1HieEHUKYoaN5timcBoowzjGInfDM%2BSGMaHuteUkX%2FgzzvtIxkMJaWXNsTsue%2ByNEJCaneSnYEF8FPLJNy3923gl8YH1cKFUBTWRYW9TAt0L%2Bl4V5PsXarN0F2ovyB2Zdb2L57PJd6Ksn3KucJ40YmzplwO%2FGzXn%2B4vuO15Skrr%2BKPW0ES0USbeEyQ8VXiG3mTspc%2BiFjGBZxQL0Nfpk2JvHsBmwsY%2BLyyidCeE55xxgGqB4fI4T8rhxCm8ep8%2FdrVq6UodybFT5mUTOzYbgWt7kiabVc%2FsBr8pNyg0%2FOQ9YI1yFCsxGfKaiIS3EjazsP7b8uQt7GRRu7K7F5BfMMLSmb0GOqUBLZ567FwDbOCRcZbUBDlPwx9Y7GI4mMtf5CjU2HxjHap1az00EoyorW9sElORum0Ez4XhhCpwPiZgl00go1g1VtG6ss9IT1PRZoJRbHna1SlVFFrGD2VG6pS2x9COTS6cWGiTQoxZxoicETceFLP8puT3LxJXJ%2FosiC%2FX%2F4TpBTku3gq2EwVd7Y3Pd5pJxYcByUYvxp7uTSEDhXqTnD0G0Y5hEqtP&X-Amz-Signature=0fdd1a0bd795bdd4fd2cf6a87f54bc6e9d962b7a0f717fa47a1f6c736df41eaf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK3FGNCB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIAUCWlJcarCvRmwutUeSl1pPktV%2FNj3pFAEsMG5rfxWUAiEAyCXn3MzxvqZkQ2i5iuq9mPXr6TrSSRrzQ13o40n%2FnhEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDC3GkXBYpexmieWdRyrcA4%2BcBY3FKtgMHr6yEQfLP%2BKMqQe0vjqSTwJnymbYPs1kowIKUCrcxM6WrA1ZtKFE6gSLWuhXz%2FAqFRkuAKO4is8Z1J1psVzxGtprX5eOnr82AIxH57WpFosqIjiaOw%2BvSEHjzOzsT3xIdlAKV0lOAIVaKYbGXhl9h62Sr77tg2u%2Fzrfj8z9NSYtkqMVF9I9%2Fi4iL1T5k321gv8v6SxUjHLXGt91RfQQZ%2BqS7i9eErobTyZVlRMAJapqjyYTob8hLMb7eAfgYE4Lo0HjSm1ZFyxL5FapzPTmoaS3VnPDSE1HieEHUKYoaN5timcBoowzjGInfDM%2BSGMaHuteUkX%2FgzzvtIxkMJaWXNsTsue%2ByNEJCaneSnYEF8FPLJNy3923gl8YH1cKFUBTWRYW9TAt0L%2Bl4V5PsXarN0F2ovyB2Zdb2L57PJd6Ksn3KucJ40YmzplwO%2FGzXn%2B4vuO15Skrr%2BKPW0ES0USbeEyQ8VXiG3mTspc%2BiFjGBZxQL0Nfpk2JvHsBmwsY%2BLyyidCeE55xxgGqB4fI4T8rhxCm8ep8%2FdrVq6UodybFT5mUTOzYbgWt7kiabVc%2FsBr8pNyg0%2FOQ9YI1yFCsxGfKaiIS3EjazsP7b8uQt7GRRu7K7F5BfMMLSmb0GOqUBLZ567FwDbOCRcZbUBDlPwx9Y7GI4mMtf5CjU2HxjHap1az00EoyorW9sElORum0Ez4XhhCpwPiZgl00go1g1VtG6ss9IT1PRZoJRbHna1SlVFFrGD2VG6pS2x9COTS6cWGiTQoxZxoicETceFLP8puT3LxJXJ%2FosiC%2FX%2F4TpBTku3gq2EwVd7Y3Pd5pJxYcByUYvxp7uTSEDhXqTnD0G0Y5hEqtP&X-Amz-Signature=b7bf2b03100179eb360158a515d531ef21319bf12f67540db0c82121d1d3023a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK3FGNCB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIAUCWlJcarCvRmwutUeSl1pPktV%2FNj3pFAEsMG5rfxWUAiEAyCXn3MzxvqZkQ2i5iuq9mPXr6TrSSRrzQ13o40n%2FnhEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDC3GkXBYpexmieWdRyrcA4%2BcBY3FKtgMHr6yEQfLP%2BKMqQe0vjqSTwJnymbYPs1kowIKUCrcxM6WrA1ZtKFE6gSLWuhXz%2FAqFRkuAKO4is8Z1J1psVzxGtprX5eOnr82AIxH57WpFosqIjiaOw%2BvSEHjzOzsT3xIdlAKV0lOAIVaKYbGXhl9h62Sr77tg2u%2Fzrfj8z9NSYtkqMVF9I9%2Fi4iL1T5k321gv8v6SxUjHLXGt91RfQQZ%2BqS7i9eErobTyZVlRMAJapqjyYTob8hLMb7eAfgYE4Lo0HjSm1ZFyxL5FapzPTmoaS3VnPDSE1HieEHUKYoaN5timcBoowzjGInfDM%2BSGMaHuteUkX%2FgzzvtIxkMJaWXNsTsue%2ByNEJCaneSnYEF8FPLJNy3923gl8YH1cKFUBTWRYW9TAt0L%2Bl4V5PsXarN0F2ovyB2Zdb2L57PJd6Ksn3KucJ40YmzplwO%2FGzXn%2B4vuO15Skrr%2BKPW0ES0USbeEyQ8VXiG3mTspc%2BiFjGBZxQL0Nfpk2JvHsBmwsY%2BLyyidCeE55xxgGqB4fI4T8rhxCm8ep8%2FdrVq6UodybFT5mUTOzYbgWt7kiabVc%2FsBr8pNyg0%2FOQ9YI1yFCsxGfKaiIS3EjazsP7b8uQt7GRRu7K7F5BfMMLSmb0GOqUBLZ567FwDbOCRcZbUBDlPwx9Y7GI4mMtf5CjU2HxjHap1az00EoyorW9sElORum0Ez4XhhCpwPiZgl00go1g1VtG6ss9IT1PRZoJRbHna1SlVFFrGD2VG6pS2x9COTS6cWGiTQoxZxoicETceFLP8puT3LxJXJ%2FosiC%2FX%2F4TpBTku3gq2EwVd7Y3Pd5pJxYcByUYvxp7uTSEDhXqTnD0G0Y5hEqtP&X-Amz-Signature=8ffa8e582b145b2a894c9fdc0af2c460b23d9d91d99b22b7969ae43cdd203b23&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK3FGNCB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIAUCWlJcarCvRmwutUeSl1pPktV%2FNj3pFAEsMG5rfxWUAiEAyCXn3MzxvqZkQ2i5iuq9mPXr6TrSSRrzQ13o40n%2FnhEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDC3GkXBYpexmieWdRyrcA4%2BcBY3FKtgMHr6yEQfLP%2BKMqQe0vjqSTwJnymbYPs1kowIKUCrcxM6WrA1ZtKFE6gSLWuhXz%2FAqFRkuAKO4is8Z1J1psVzxGtprX5eOnr82AIxH57WpFosqIjiaOw%2BvSEHjzOzsT3xIdlAKV0lOAIVaKYbGXhl9h62Sr77tg2u%2Fzrfj8z9NSYtkqMVF9I9%2Fi4iL1T5k321gv8v6SxUjHLXGt91RfQQZ%2BqS7i9eErobTyZVlRMAJapqjyYTob8hLMb7eAfgYE4Lo0HjSm1ZFyxL5FapzPTmoaS3VnPDSE1HieEHUKYoaN5timcBoowzjGInfDM%2BSGMaHuteUkX%2FgzzvtIxkMJaWXNsTsue%2ByNEJCaneSnYEF8FPLJNy3923gl8YH1cKFUBTWRYW9TAt0L%2Bl4V5PsXarN0F2ovyB2Zdb2L57PJd6Ksn3KucJ40YmzplwO%2FGzXn%2B4vuO15Skrr%2BKPW0ES0USbeEyQ8VXiG3mTspc%2BiFjGBZxQL0Nfpk2JvHsBmwsY%2BLyyidCeE55xxgGqB4fI4T8rhxCm8ep8%2FdrVq6UodybFT5mUTOzYbgWt7kiabVc%2FsBr8pNyg0%2FOQ9YI1yFCsxGfKaiIS3EjazsP7b8uQt7GRRu7K7F5BfMMLSmb0GOqUBLZ567FwDbOCRcZbUBDlPwx9Y7GI4mMtf5CjU2HxjHap1az00EoyorW9sElORum0Ez4XhhCpwPiZgl00go1g1VtG6ss9IT1PRZoJRbHna1SlVFFrGD2VG6pS2x9COTS6cWGiTQoxZxoicETceFLP8puT3LxJXJ%2FosiC%2FX%2F4TpBTku3gq2EwVd7Y3Pd5pJxYcByUYvxp7uTSEDhXqTnD0G0Y5hEqtP&X-Amz-Signature=3ffebccef9b75c46162a61d6ba089766db5d166b64ff9e4443eaa608b1cf3227&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK3FGNCB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIAUCWlJcarCvRmwutUeSl1pPktV%2FNj3pFAEsMG5rfxWUAiEAyCXn3MzxvqZkQ2i5iuq9mPXr6TrSSRrzQ13o40n%2FnhEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDC3GkXBYpexmieWdRyrcA4%2BcBY3FKtgMHr6yEQfLP%2BKMqQe0vjqSTwJnymbYPs1kowIKUCrcxM6WrA1ZtKFE6gSLWuhXz%2FAqFRkuAKO4is8Z1J1psVzxGtprX5eOnr82AIxH57WpFosqIjiaOw%2BvSEHjzOzsT3xIdlAKV0lOAIVaKYbGXhl9h62Sr77tg2u%2Fzrfj8z9NSYtkqMVF9I9%2Fi4iL1T5k321gv8v6SxUjHLXGt91RfQQZ%2BqS7i9eErobTyZVlRMAJapqjyYTob8hLMb7eAfgYE4Lo0HjSm1ZFyxL5FapzPTmoaS3VnPDSE1HieEHUKYoaN5timcBoowzjGInfDM%2BSGMaHuteUkX%2FgzzvtIxkMJaWXNsTsue%2ByNEJCaneSnYEF8FPLJNy3923gl8YH1cKFUBTWRYW9TAt0L%2Bl4V5PsXarN0F2ovyB2Zdb2L57PJd6Ksn3KucJ40YmzplwO%2FGzXn%2B4vuO15Skrr%2BKPW0ES0USbeEyQ8VXiG3mTspc%2BiFjGBZxQL0Nfpk2JvHsBmwsY%2BLyyidCeE55xxgGqB4fI4T8rhxCm8ep8%2FdrVq6UodybFT5mUTOzYbgWt7kiabVc%2FsBr8pNyg0%2FOQ9YI1yFCsxGfKaiIS3EjazsP7b8uQt7GRRu7K7F5BfMMLSmb0GOqUBLZ567FwDbOCRcZbUBDlPwx9Y7GI4mMtf5CjU2HxjHap1az00EoyorW9sElORum0Ez4XhhCpwPiZgl00go1g1VtG6ss9IT1PRZoJRbHna1SlVFFrGD2VG6pS2x9COTS6cWGiTQoxZxoicETceFLP8puT3LxJXJ%2FosiC%2FX%2F4TpBTku3gq2EwVd7Y3Pd5pJxYcByUYvxp7uTSEDhXqTnD0G0Y5hEqtP&X-Amz-Signature=c9bd89989296aef9555cc9134c5a01d84fd60bf29103515fc43a3d13caee57d5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK3FGNCB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIAUCWlJcarCvRmwutUeSl1pPktV%2FNj3pFAEsMG5rfxWUAiEAyCXn3MzxvqZkQ2i5iuq9mPXr6TrSSRrzQ13o40n%2FnhEq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDC3GkXBYpexmieWdRyrcA4%2BcBY3FKtgMHr6yEQfLP%2BKMqQe0vjqSTwJnymbYPs1kowIKUCrcxM6WrA1ZtKFE6gSLWuhXz%2FAqFRkuAKO4is8Z1J1psVzxGtprX5eOnr82AIxH57WpFosqIjiaOw%2BvSEHjzOzsT3xIdlAKV0lOAIVaKYbGXhl9h62Sr77tg2u%2Fzrfj8z9NSYtkqMVF9I9%2Fi4iL1T5k321gv8v6SxUjHLXGt91RfQQZ%2BqS7i9eErobTyZVlRMAJapqjyYTob8hLMb7eAfgYE4Lo0HjSm1ZFyxL5FapzPTmoaS3VnPDSE1HieEHUKYoaN5timcBoowzjGInfDM%2BSGMaHuteUkX%2FgzzvtIxkMJaWXNsTsue%2ByNEJCaneSnYEF8FPLJNy3923gl8YH1cKFUBTWRYW9TAt0L%2Bl4V5PsXarN0F2ovyB2Zdb2L57PJd6Ksn3KucJ40YmzplwO%2FGzXn%2B4vuO15Skrr%2BKPW0ES0USbeEyQ8VXiG3mTspc%2BiFjGBZxQL0Nfpk2JvHsBmwsY%2BLyyidCeE55xxgGqB4fI4T8rhxCm8ep8%2FdrVq6UodybFT5mUTOzYbgWt7kiabVc%2FsBr8pNyg0%2FOQ9YI1yFCsxGfKaiIS3EjazsP7b8uQt7GRRu7K7F5BfMMLSmb0GOqUBLZ567FwDbOCRcZbUBDlPwx9Y7GI4mMtf5CjU2HxjHap1az00EoyorW9sElORum0Ez4XhhCpwPiZgl00go1g1VtG6ss9IT1PRZoJRbHna1SlVFFrGD2VG6pS2x9COTS6cWGiTQoxZxoicETceFLP8puT3LxJXJ%2FosiC%2FX%2F4TpBTku3gq2EwVd7Y3Pd5pJxYcByUYvxp7uTSEDhXqTnD0G0Y5hEqtP&X-Amz-Signature=d456e806570ec2bd92759bea03098a70701a07faa6b420b79698a80770eb6352&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SP5IUPG4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQD%2F0YpiQMevd%2BTxxDONsRgGflAmqQNVAUcyFjYScEwhKwIhAOrfn3t5jAfsDcdU7nv5e618XzD5TIXVKSBkYQMoWY1pKv8DCH0QABoMNjM3NDIzMTgzODA1IgzAdKKbxlA0del0Kcgq3AMcSdacInKeG5H6%2By1uBLLGeTKI2Wk88P9h76eY0O0pdeu52Qbiv9awogDSe1V08NK3xgr4VrNxlQYjAlMTrLW9F1h64bxuo%2BoXb6wbOzvRH3oNMPWm56D%2BUsPei%2BVaqGKG45gkisXtSB0rR965AI%2F6803R1sDOsr%2FDCytMTmV53aEFiGDAkjKmDjc5gefz98U8ddxUssic8P9cIyCqDzWIunCWA8bQ8l15V8%2BN9WOI7FoD9%2F%2BkUz7AwFu6eo4OtsE0O37AB41BuNs3vrdcjqXSD%2FKWx1QbjP8cUKBV2mudcmFoY25bXGc03QjUc8dtYHNfpE8hcCAZ5StbbRxwMtDeLQANBDbJ5R63TWi7O2dbKwyCgeYRTRYy%2FYfVk%2Fhf9psTwJE03zAG3LbymfxXcj54eMyUjILgv648JzlVZ0YIF5SbOc2YZRdxoXzgdfy%2F8K9uQyjRPu4a7JeNU%2FkbFM%2BVL%2FSYArYJlX2k1%2Biovi49y6kDJYF8ExAn80QgZ0geNeecPrxXSrfUmQk%2BJTklEuz1vSaKDoMp1tlaTUv%2Fp2bwyKgHZCeRf7239WaCo2HaULJtp7bn2YDdHaYa3kq1vK%2BMSqtabjWOKlDqrQBJth4WweGz6qHmipmP%2FXkogjCL05m9BjqkARX7xUOj%2B1M8mC6gUcwZGQBHocm5N9dJI%2FCueZ25vxolwwIREZ2OIi3SAVtVPEaJvCnsJXmWmZAeEtUW%2BDbluFoYhy0hHvDO9vCLXbiz1A07L%2Bkf7AwjZfZocL8zBBJprj8i2u2%2BUVFKG8%2B0mfQ5Zof0wXAAEWxIByag3IV%2Bcn%2F8kQwOqpmBJXto8OqXrO6DE1uoIUQ4yLIfrBc%2FhNAtIyhsNI7H&X-Amz-Signature=9cd8a7811df89c04f4d790dbf4931ed3abd237210575b50d196ac916fc027fda&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VUE2IDI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIEJfQlziRHk3tlkIVMBBanaPT0rh8nDfO8DSxweah5S7AiEAzo4GeyvAdtM%2FgcKgz1C4Vb%2BO9s59CbuSRH5xN2HkSNsq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDJ3yfHiDsVK2lcWcmCrcA1VNdQ0ZrOQVr9xrc%2FLkelPVPsx4Ol%2BNXANlSy3TsHnKnsVFaL2%2BtWWsYv%2BeewQsPIHS1abQlnaz%2BSUik5vRYcUhxV%2BWw8bchoa0ZNiIyxQYaY2ZYTC2TWfty39cV%2BFe7LWQyePm0NuRAtUxEWlDtMP%2F1NIBrvI4njGm3GZqNPyczKER%2FXRzHFovLKyTfTYDVN5W4ymJXx%2FYau0QWBDDZKHWmlF7yh7GHDNsXblC4NfjtbFTrvGoMNfxZhz8flpd1DYKW0G6SWYSEijj0wJqAbiPjLUsZsKSuqfZmXud%2BGZovLmB4Z4bt9dMdU%2FRDnROp%2BfbUu8acA5ZXctJmHOaVVAFt8lbTm9K7XYGZ6kWRjUG8PoL4dcTvvsB7lltanG92vkI9ucO8cgFJ18Vov3NQkbJbTtkhTpI%2Fw2zffj2z3m61SvutG5bmZeRwudCni0Icm%2BI8FkQflJiATZsdpi785c6kRXWIIH0e5XImzLoNcOLeZt95DdYE8lyFr1vGdpDFfXimAdrepg%2Bpy%2F51AwnEfFCQG%2FhXlP3mWfXC8GvDiPFoUcA66D%2Bt%2BcZ5IR9nSoQbWMO5vq1%2Bjgv0YlQRHk8Wf25bH35VlAjazmG2qpwt%2B%2FwAZPbgKf43jdfTl6AMNTSmb0GOqUBuUQDLjaP4sdWyD%2FLWN%2FgTgZc6U5GGrq%2B7np%2FlCXoEy7pdvHm7lSqrs5guOHhRVqCup73LiuSr%2FNNq4dANrh5LASJGr8DSdBnMUdk7JnYTxOQCFlPtdHhXgSsLB8WL5y5GoNjen1AaWLbiCbb3tNOjkg%2BZDXY6JHuCvP3RNxEd7mzdMGpo0OmwxMKJ3ckeinlfYviL5ajkbmwtPPiRd6I0PoGf%2FmH&X-Amz-Signature=eb30958714ba06390dbd362434fa62680a556c3621dd8a9e2058dab99e58c21f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD3L7QVP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCqgFXS7YZCqaiU8cZLG1NYQUVAi%2F3cQ66dfsnwSm2uQAIgPIVSOD832KEeUaMdMXgoflnH22NQh7URnqSeTPbXSe4q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHwevngQGu93x4s%2B4CrcAxyKaYfn2LwnSuJM0yP8LtJhuqQs7tl2YL3yNJvGTNlgRAo1z1%2BoHF59acONg%2Bx3ivTc4sdmFahO2BMCtY%2FQ8K7VwyqgGCuJ4Stsc2bbgN7LKNlpCw%2BF%2B9Wyw5tja6ONj6TwdBPl9AD7mBEgcm0DlibUGrusLJNEHjH%2BzGxDDlh7XAPIpGAmYBS3wVsd8m%2FXWOkxdwaYu97tCOGNh4hMqzrzusjSOYj9waDbQDdgbW%2FMOwu06XiErAtKvhylGNfCdWrVVqdqDJWmbfJbfBqCz0lJEP%2BrftrcBF3guhibp9RBonnYEh95%2BYep6cPcT2RQWqKAheD5FUCFOjTHHWry5%2F%2FAWTZVQUzR9rgHBqvfdxXCAlVWOus8ny%2FG%2BYLKbb9lr7SxScrW1RrDl7H7mriV8wHUP37qkc8iqn9zqAESypFFJfe2heQMpXW7kXG0B41MyeD6OAKoeJrupvSBEcb7UbcMAOJwTS60%2B%2Bo1ramQWtQwchB5eMoVcb6i%2FshHCll1QJUbXjLMeqty4HxeSQR6%2Fl0hZXZlUsxhAh8%2FAA7MDhfxCgdtPN22Wj1h%2F2pqVKSQ1Dobtio0SIFAUmCgm8BAsHaeK%2BelBIcLj88rrOP6I%2BC2uOUR6BKXqJpbUYL%2FMNXSmb0GOqUBiOJE1i%2B%2BhvUQoSkeEu3G0NccZmOi30OytVEeU2VD%2FBPxg5f61xNp4SPvtwEFortYFGwgVU9KNUljpCiRvXrilYCpp4kq%2Bp0okDa5KcpMw09j4PB9aui55285Pi4%2FfUbMjEww8t34snzQTmUGPGa9HBvntgft8gESye3rb2rbxqM1Eqe5DS2bOudBdyi2CDpdTWs0Tu%2BU1nIi0DG1NGfA1soxOTug&X-Amz-Signature=4212bf45349ba5968af3ad9566f1938098ae6b6abc8e1355b617467ccec55fb4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD3L7QVP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQCqgFXS7YZCqaiU8cZLG1NYQUVAi%2F3cQ66dfsnwSm2uQAIgPIVSOD832KEeUaMdMXgoflnH22NQh7URnqSeTPbXSe4q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHwevngQGu93x4s%2B4CrcAxyKaYfn2LwnSuJM0yP8LtJhuqQs7tl2YL3yNJvGTNlgRAo1z1%2BoHF59acONg%2Bx3ivTc4sdmFahO2BMCtY%2FQ8K7VwyqgGCuJ4Stsc2bbgN7LKNlpCw%2BF%2B9Wyw5tja6ONj6TwdBPl9AD7mBEgcm0DlibUGrusLJNEHjH%2BzGxDDlh7XAPIpGAmYBS3wVsd8m%2FXWOkxdwaYu97tCOGNh4hMqzrzusjSOYj9waDbQDdgbW%2FMOwu06XiErAtKvhylGNfCdWrVVqdqDJWmbfJbfBqCz0lJEP%2BrftrcBF3guhibp9RBonnYEh95%2BYep6cPcT2RQWqKAheD5FUCFOjTHHWry5%2F%2FAWTZVQUzR9rgHBqvfdxXCAlVWOus8ny%2FG%2BYLKbb9lr7SxScrW1RrDl7H7mriV8wHUP37qkc8iqn9zqAESypFFJfe2heQMpXW7kXG0B41MyeD6OAKoeJrupvSBEcb7UbcMAOJwTS60%2B%2Bo1ramQWtQwchB5eMoVcb6i%2FshHCll1QJUbXjLMeqty4HxeSQR6%2Fl0hZXZlUsxhAh8%2FAA7MDhfxCgdtPN22Wj1h%2F2pqVKSQ1Dobtio0SIFAUmCgm8BAsHaeK%2BelBIcLj88rrOP6I%2BC2uOUR6BKXqJpbUYL%2FMNXSmb0GOqUBiOJE1i%2B%2BhvUQoSkeEu3G0NccZmOi30OytVEeU2VD%2FBPxg5f61xNp4SPvtwEFortYFGwgVU9KNUljpCiRvXrilYCpp4kq%2Bp0okDa5KcpMw09j4PB9aui55285Pi4%2FfUbMjEww8t34snzQTmUGPGa9HBvntgft8gESye3rb2rbxqM1Eqe5DS2bOudBdyi2CDpdTWs0Tu%2BU1nIi0DG1NGfA1soxOTug&X-Amz-Signature=0a3ee6c39e537fac5e1e81a28a9e086e9fab55e71f2ecd0ed696e73565d43012&X-Amz-SignedHeaders=host&x-id=GetObject)
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
