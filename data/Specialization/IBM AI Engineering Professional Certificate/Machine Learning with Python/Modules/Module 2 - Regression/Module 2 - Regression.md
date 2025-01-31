

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AOTDAU2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJaZV%2Fl9MQIMX%2F%2BtyJuqpuKhBEgG7BrqTJO%2BlOO8xrWQIgHRTMzo4ejND1IXc2Tp%2BSvKVRyXm7dTToJRJkTYidbYQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5u%2B9yY646gMuEydircA3FUhcmXO7OSLbXitm1%2BeWXEitTG52KZ%2FsYcqZhm9sE0ZjOVhmrqCm5dC4nB9OsWC%2BHpkwZbLKtGdmlEiQ0NUwDUCvibdu%2FzH17ybw9o%2BMYY92q0j9sYtp6GehwVtotLFPTyn8S0Ciy2qUV6zja0dX70WHcqXmv0QG1uez1Qehv50hX3Eg0Wzvc1usAcZZZqExFEHmFiYtBhFNdJurSxc4GH4gVf6%2FE70RiegNmSQ9JEQWiYAPvrYE5yIkCzpA05qaDagyu%2BA8V3%2F63JiS9q2%2BAhNdE%2BKNgzbmWQsC4Eu86k%2BcRVf%2FSjNEYboJKn0nAfq%2BeTjhpUuXGbKk0iosCsugRrwIIUKhYvDDnKr36Njuq6HPNb0WU27JFy1M%2BY%2BPNpxrxhwtn%2Fz%2BFE9SZlrguyE9EwwrMO8rwqcZ8Djs8On9NZB5CHmfxrH6sxHIDKIga1OHR5qKcW4Yxx2QhIpbUwaKLD0oGbaulMh5Onyaftmmv1rUSFD3l9BYnZh88MKbnbmAHTbPbGejZvvPRwPQWotc1%2B6De%2B6EKnWrPXLDHJMhSJNTXsrqgdfP1hX8qdOBvIcADpwkv8oabZT70nM51imYZ6TGNiof5NoujhVoY6j6QPZBMYWVs2%2FZJxCX0GMMjQ8LwGOqUBpiWGT4TdWeTVn%2FwP8Xju00IqrckkQEnn11JSMdZ3sHMLtTSc%2BhtipjlKNuuMIlkjH62mk5mCu4K4mGmMPEA%2F0t3PHcWPjXN5KwqETRH0q1FC0BTAiSI%2BR9Zp9njc7voPfI5FY6CfFAYN0fl1RCvBmxaIp5Oa8L%2BZUNb1Tzg4YpPad1lVztTE0EEx70kQThA4g6ZLtc7jJHTjI8R0lzv03ocEIsNu&X-Amz-Signature=fa40d629360f16adbd66809248e2f649212f14404ac96115421c5985d9bfef04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AOTDAU2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJaZV%2Fl9MQIMX%2F%2BtyJuqpuKhBEgG7BrqTJO%2BlOO8xrWQIgHRTMzo4ejND1IXc2Tp%2BSvKVRyXm7dTToJRJkTYidbYQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5u%2B9yY646gMuEydircA3FUhcmXO7OSLbXitm1%2BeWXEitTG52KZ%2FsYcqZhm9sE0ZjOVhmrqCm5dC4nB9OsWC%2BHpkwZbLKtGdmlEiQ0NUwDUCvibdu%2FzH17ybw9o%2BMYY92q0j9sYtp6GehwVtotLFPTyn8S0Ciy2qUV6zja0dX70WHcqXmv0QG1uez1Qehv50hX3Eg0Wzvc1usAcZZZqExFEHmFiYtBhFNdJurSxc4GH4gVf6%2FE70RiegNmSQ9JEQWiYAPvrYE5yIkCzpA05qaDagyu%2BA8V3%2F63JiS9q2%2BAhNdE%2BKNgzbmWQsC4Eu86k%2BcRVf%2FSjNEYboJKn0nAfq%2BeTjhpUuXGbKk0iosCsugRrwIIUKhYvDDnKr36Njuq6HPNb0WU27JFy1M%2BY%2BPNpxrxhwtn%2Fz%2BFE9SZlrguyE9EwwrMO8rwqcZ8Djs8On9NZB5CHmfxrH6sxHIDKIga1OHR5qKcW4Yxx2QhIpbUwaKLD0oGbaulMh5Onyaftmmv1rUSFD3l9BYnZh88MKbnbmAHTbPbGejZvvPRwPQWotc1%2B6De%2B6EKnWrPXLDHJMhSJNTXsrqgdfP1hX8qdOBvIcADpwkv8oabZT70nM51imYZ6TGNiof5NoujhVoY6j6QPZBMYWVs2%2FZJxCX0GMMjQ8LwGOqUBpiWGT4TdWeTVn%2FwP8Xju00IqrckkQEnn11JSMdZ3sHMLtTSc%2BhtipjlKNuuMIlkjH62mk5mCu4K4mGmMPEA%2F0t3PHcWPjXN5KwqETRH0q1FC0BTAiSI%2BR9Zp9njc7voPfI5FY6CfFAYN0fl1RCvBmxaIp5Oa8L%2BZUNb1Tzg4YpPad1lVztTE0EEx70kQThA4g6ZLtc7jJHTjI8R0lzv03ocEIsNu&X-Amz-Signature=612b00fde1d8697bd18152c9d0fd06c344568446d5c2d78f9717e65ebf12d3e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AOTDAU2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJaZV%2Fl9MQIMX%2F%2BtyJuqpuKhBEgG7BrqTJO%2BlOO8xrWQIgHRTMzo4ejND1IXc2Tp%2BSvKVRyXm7dTToJRJkTYidbYQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5u%2B9yY646gMuEydircA3FUhcmXO7OSLbXitm1%2BeWXEitTG52KZ%2FsYcqZhm9sE0ZjOVhmrqCm5dC4nB9OsWC%2BHpkwZbLKtGdmlEiQ0NUwDUCvibdu%2FzH17ybw9o%2BMYY92q0j9sYtp6GehwVtotLFPTyn8S0Ciy2qUV6zja0dX70WHcqXmv0QG1uez1Qehv50hX3Eg0Wzvc1usAcZZZqExFEHmFiYtBhFNdJurSxc4GH4gVf6%2FE70RiegNmSQ9JEQWiYAPvrYE5yIkCzpA05qaDagyu%2BA8V3%2F63JiS9q2%2BAhNdE%2BKNgzbmWQsC4Eu86k%2BcRVf%2FSjNEYboJKn0nAfq%2BeTjhpUuXGbKk0iosCsugRrwIIUKhYvDDnKr36Njuq6HPNb0WU27JFy1M%2BY%2BPNpxrxhwtn%2Fz%2BFE9SZlrguyE9EwwrMO8rwqcZ8Djs8On9NZB5CHmfxrH6sxHIDKIga1OHR5qKcW4Yxx2QhIpbUwaKLD0oGbaulMh5Onyaftmmv1rUSFD3l9BYnZh88MKbnbmAHTbPbGejZvvPRwPQWotc1%2B6De%2B6EKnWrPXLDHJMhSJNTXsrqgdfP1hX8qdOBvIcADpwkv8oabZT70nM51imYZ6TGNiof5NoujhVoY6j6QPZBMYWVs2%2FZJxCX0GMMjQ8LwGOqUBpiWGT4TdWeTVn%2FwP8Xju00IqrckkQEnn11JSMdZ3sHMLtTSc%2BhtipjlKNuuMIlkjH62mk5mCu4K4mGmMPEA%2F0t3PHcWPjXN5KwqETRH0q1FC0BTAiSI%2BR9Zp9njc7voPfI5FY6CfFAYN0fl1RCvBmxaIp5Oa8L%2BZUNb1Tzg4YpPad1lVztTE0EEx70kQThA4g6ZLtc7jJHTjI8R0lzv03ocEIsNu&X-Amz-Signature=54772fbb6ddd53e121ec9e3d68595a32e398039f3917dca26083dd5cd421923b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AOTDAU2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJaZV%2Fl9MQIMX%2F%2BtyJuqpuKhBEgG7BrqTJO%2BlOO8xrWQIgHRTMzo4ejND1IXc2Tp%2BSvKVRyXm7dTToJRJkTYidbYQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5u%2B9yY646gMuEydircA3FUhcmXO7OSLbXitm1%2BeWXEitTG52KZ%2FsYcqZhm9sE0ZjOVhmrqCm5dC4nB9OsWC%2BHpkwZbLKtGdmlEiQ0NUwDUCvibdu%2FzH17ybw9o%2BMYY92q0j9sYtp6GehwVtotLFPTyn8S0Ciy2qUV6zja0dX70WHcqXmv0QG1uez1Qehv50hX3Eg0Wzvc1usAcZZZqExFEHmFiYtBhFNdJurSxc4GH4gVf6%2FE70RiegNmSQ9JEQWiYAPvrYE5yIkCzpA05qaDagyu%2BA8V3%2F63JiS9q2%2BAhNdE%2BKNgzbmWQsC4Eu86k%2BcRVf%2FSjNEYboJKn0nAfq%2BeTjhpUuXGbKk0iosCsugRrwIIUKhYvDDnKr36Njuq6HPNb0WU27JFy1M%2BY%2BPNpxrxhwtn%2Fz%2BFE9SZlrguyE9EwwrMO8rwqcZ8Djs8On9NZB5CHmfxrH6sxHIDKIga1OHR5qKcW4Yxx2QhIpbUwaKLD0oGbaulMh5Onyaftmmv1rUSFD3l9BYnZh88MKbnbmAHTbPbGejZvvPRwPQWotc1%2B6De%2B6EKnWrPXLDHJMhSJNTXsrqgdfP1hX8qdOBvIcADpwkv8oabZT70nM51imYZ6TGNiof5NoujhVoY6j6QPZBMYWVs2%2FZJxCX0GMMjQ8LwGOqUBpiWGT4TdWeTVn%2FwP8Xju00IqrckkQEnn11JSMdZ3sHMLtTSc%2BhtipjlKNuuMIlkjH62mk5mCu4K4mGmMPEA%2F0t3PHcWPjXN5KwqETRH0q1FC0BTAiSI%2BR9Zp9njc7voPfI5FY6CfFAYN0fl1RCvBmxaIp5Oa8L%2BZUNb1Tzg4YpPad1lVztTE0EEx70kQThA4g6ZLtc7jJHTjI8R0lzv03ocEIsNu&X-Amz-Signature=c9d892914687c6b4b623cf18c700da6907f53ff02a20e61735e596b7bfeb2a71&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AOTDAU2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJaZV%2Fl9MQIMX%2F%2BtyJuqpuKhBEgG7BrqTJO%2BlOO8xrWQIgHRTMzo4ejND1IXc2Tp%2BSvKVRyXm7dTToJRJkTYidbYQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5u%2B9yY646gMuEydircA3FUhcmXO7OSLbXitm1%2BeWXEitTG52KZ%2FsYcqZhm9sE0ZjOVhmrqCm5dC4nB9OsWC%2BHpkwZbLKtGdmlEiQ0NUwDUCvibdu%2FzH17ybw9o%2BMYY92q0j9sYtp6GehwVtotLFPTyn8S0Ciy2qUV6zja0dX70WHcqXmv0QG1uez1Qehv50hX3Eg0Wzvc1usAcZZZqExFEHmFiYtBhFNdJurSxc4GH4gVf6%2FE70RiegNmSQ9JEQWiYAPvrYE5yIkCzpA05qaDagyu%2BA8V3%2F63JiS9q2%2BAhNdE%2BKNgzbmWQsC4Eu86k%2BcRVf%2FSjNEYboJKn0nAfq%2BeTjhpUuXGbKk0iosCsugRrwIIUKhYvDDnKr36Njuq6HPNb0WU27JFy1M%2BY%2BPNpxrxhwtn%2Fz%2BFE9SZlrguyE9EwwrMO8rwqcZ8Djs8On9NZB5CHmfxrH6sxHIDKIga1OHR5qKcW4Yxx2QhIpbUwaKLD0oGbaulMh5Onyaftmmv1rUSFD3l9BYnZh88MKbnbmAHTbPbGejZvvPRwPQWotc1%2B6De%2B6EKnWrPXLDHJMhSJNTXsrqgdfP1hX8qdOBvIcADpwkv8oabZT70nM51imYZ6TGNiof5NoujhVoY6j6QPZBMYWVs2%2FZJxCX0GMMjQ8LwGOqUBpiWGT4TdWeTVn%2FwP8Xju00IqrckkQEnn11JSMdZ3sHMLtTSc%2BhtipjlKNuuMIlkjH62mk5mCu4K4mGmMPEA%2F0t3PHcWPjXN5KwqETRH0q1FC0BTAiSI%2BR9Zp9njc7voPfI5FY6CfFAYN0fl1RCvBmxaIp5Oa8L%2BZUNb1Tzg4YpPad1lVztTE0EEx70kQThA4g6ZLtc7jJHTjI8R0lzv03ocEIsNu&X-Amz-Signature=d354483fb2a5c130ba7ba98dd2efbf5247766b4573e17e0370ad355275a98e22&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AOTDAU2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJaZV%2Fl9MQIMX%2F%2BtyJuqpuKhBEgG7BrqTJO%2BlOO8xrWQIgHRTMzo4ejND1IXc2Tp%2BSvKVRyXm7dTToJRJkTYidbYQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5u%2B9yY646gMuEydircA3FUhcmXO7OSLbXitm1%2BeWXEitTG52KZ%2FsYcqZhm9sE0ZjOVhmrqCm5dC4nB9OsWC%2BHpkwZbLKtGdmlEiQ0NUwDUCvibdu%2FzH17ybw9o%2BMYY92q0j9sYtp6GehwVtotLFPTyn8S0Ciy2qUV6zja0dX70WHcqXmv0QG1uez1Qehv50hX3Eg0Wzvc1usAcZZZqExFEHmFiYtBhFNdJurSxc4GH4gVf6%2FE70RiegNmSQ9JEQWiYAPvrYE5yIkCzpA05qaDagyu%2BA8V3%2F63JiS9q2%2BAhNdE%2BKNgzbmWQsC4Eu86k%2BcRVf%2FSjNEYboJKn0nAfq%2BeTjhpUuXGbKk0iosCsugRrwIIUKhYvDDnKr36Njuq6HPNb0WU27JFy1M%2BY%2BPNpxrxhwtn%2Fz%2BFE9SZlrguyE9EwwrMO8rwqcZ8Djs8On9NZB5CHmfxrH6sxHIDKIga1OHR5qKcW4Yxx2QhIpbUwaKLD0oGbaulMh5Onyaftmmv1rUSFD3l9BYnZh88MKbnbmAHTbPbGejZvvPRwPQWotc1%2B6De%2B6EKnWrPXLDHJMhSJNTXsrqgdfP1hX8qdOBvIcADpwkv8oabZT70nM51imYZ6TGNiof5NoujhVoY6j6QPZBMYWVs2%2FZJxCX0GMMjQ8LwGOqUBpiWGT4TdWeTVn%2FwP8Xju00IqrckkQEnn11JSMdZ3sHMLtTSc%2BhtipjlKNuuMIlkjH62mk5mCu4K4mGmMPEA%2F0t3PHcWPjXN5KwqETRH0q1FC0BTAiSI%2BR9Zp9njc7voPfI5FY6CfFAYN0fl1RCvBmxaIp5Oa8L%2BZUNb1Tzg4YpPad1lVztTE0EEx70kQThA4g6ZLtc7jJHTjI8R0lzv03ocEIsNu&X-Amz-Signature=aa71c9bd6d61efbc02138740c3818cd71db015a051b8e81aa3453d59978ebb17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AOTDAU2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJaZV%2Fl9MQIMX%2F%2BtyJuqpuKhBEgG7BrqTJO%2BlOO8xrWQIgHRTMzo4ejND1IXc2Tp%2BSvKVRyXm7dTToJRJkTYidbYQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5u%2B9yY646gMuEydircA3FUhcmXO7OSLbXitm1%2BeWXEitTG52KZ%2FsYcqZhm9sE0ZjOVhmrqCm5dC4nB9OsWC%2BHpkwZbLKtGdmlEiQ0NUwDUCvibdu%2FzH17ybw9o%2BMYY92q0j9sYtp6GehwVtotLFPTyn8S0Ciy2qUV6zja0dX70WHcqXmv0QG1uez1Qehv50hX3Eg0Wzvc1usAcZZZqExFEHmFiYtBhFNdJurSxc4GH4gVf6%2FE70RiegNmSQ9JEQWiYAPvrYE5yIkCzpA05qaDagyu%2BA8V3%2F63JiS9q2%2BAhNdE%2BKNgzbmWQsC4Eu86k%2BcRVf%2FSjNEYboJKn0nAfq%2BeTjhpUuXGbKk0iosCsugRrwIIUKhYvDDnKr36Njuq6HPNb0WU27JFy1M%2BY%2BPNpxrxhwtn%2Fz%2BFE9SZlrguyE9EwwrMO8rwqcZ8Djs8On9NZB5CHmfxrH6sxHIDKIga1OHR5qKcW4Yxx2QhIpbUwaKLD0oGbaulMh5Onyaftmmv1rUSFD3l9BYnZh88MKbnbmAHTbPbGejZvvPRwPQWotc1%2B6De%2B6EKnWrPXLDHJMhSJNTXsrqgdfP1hX8qdOBvIcADpwkv8oabZT70nM51imYZ6TGNiof5NoujhVoY6j6QPZBMYWVs2%2FZJxCX0GMMjQ8LwGOqUBpiWGT4TdWeTVn%2FwP8Xju00IqrckkQEnn11JSMdZ3sHMLtTSc%2BhtipjlKNuuMIlkjH62mk5mCu4K4mGmMPEA%2F0t3PHcWPjXN5KwqETRH0q1FC0BTAiSI%2BR9Zp9njc7voPfI5FY6CfFAYN0fl1RCvBmxaIp5Oa8L%2BZUNb1Tzg4YpPad1lVztTE0EEx70kQThA4g6ZLtc7jJHTjI8R0lzv03ocEIsNu&X-Amz-Signature=8206df874abd9bf5012a62ca2da9a306d5244c6d8af3683d400d425651677ebf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AOTDAU2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJaZV%2Fl9MQIMX%2F%2BtyJuqpuKhBEgG7BrqTJO%2BlOO8xrWQIgHRTMzo4ejND1IXc2Tp%2BSvKVRyXm7dTToJRJkTYidbYQqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5u%2B9yY646gMuEydircA3FUhcmXO7OSLbXitm1%2BeWXEitTG52KZ%2FsYcqZhm9sE0ZjOVhmrqCm5dC4nB9OsWC%2BHpkwZbLKtGdmlEiQ0NUwDUCvibdu%2FzH17ybw9o%2BMYY92q0j9sYtp6GehwVtotLFPTyn8S0Ciy2qUV6zja0dX70WHcqXmv0QG1uez1Qehv50hX3Eg0Wzvc1usAcZZZqExFEHmFiYtBhFNdJurSxc4GH4gVf6%2FE70RiegNmSQ9JEQWiYAPvrYE5yIkCzpA05qaDagyu%2BA8V3%2F63JiS9q2%2BAhNdE%2BKNgzbmWQsC4Eu86k%2BcRVf%2FSjNEYboJKn0nAfq%2BeTjhpUuXGbKk0iosCsugRrwIIUKhYvDDnKr36Njuq6HPNb0WU27JFy1M%2BY%2BPNpxrxhwtn%2Fz%2BFE9SZlrguyE9EwwrMO8rwqcZ8Djs8On9NZB5CHmfxrH6sxHIDKIga1OHR5qKcW4Yxx2QhIpbUwaKLD0oGbaulMh5Onyaftmmv1rUSFD3l9BYnZh88MKbnbmAHTbPbGejZvvPRwPQWotc1%2B6De%2B6EKnWrPXLDHJMhSJNTXsrqgdfP1hX8qdOBvIcADpwkv8oabZT70nM51imYZ6TGNiof5NoujhVoY6j6QPZBMYWVs2%2FZJxCX0GMMjQ8LwGOqUBpiWGT4TdWeTVn%2FwP8Xju00IqrckkQEnn11JSMdZ3sHMLtTSc%2BhtipjlKNuuMIlkjH62mk5mCu4K4mGmMPEA%2F0t3PHcWPjXN5KwqETRH0q1FC0BTAiSI%2BR9Zp9njc7voPfI5FY6CfFAYN0fl1RCvBmxaIp5Oa8L%2BZUNb1Tzg4YpPad1lVztTE0EEx70kQThA4g6ZLtc7jJHTjI8R0lzv03ocEIsNu&X-Amz-Signature=e992bba65ce0c9206c3cc867c87c481cea74d8fe52927bfd0e583d562f824470&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RESP32Y%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFHr69XZ4giC7YZTLGgu9WPri6O7JbQKVyxuPuiV7BkfAiAqcyfLqsJwQ2%2BjQpm38UwxQMzn9nIAtG376jVBQHt4ZiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2n8oTgTY9ADOYeq%2FKtwD%2BPa5guF8vf%2BuPCCqKemG67mOaseWMV1yppwz0TccOjZGSwPEx5p7BxoO9o3rUrsNIbSjn43u3SvglCB%2F6CED1ARTxZUAnpuuMH8TW6OWWdxuztH4QYxhOfXKXUppklaetdJEcCy7Ti7%2FHxTQDO2MyWBt8q8YCH2eAn7B5aGWcmZW6jvxM1d7NIZG%2BUKrWernY9dFQpm9v%2BG%2BimC4NmujRfOJsakNk5pR%2BcOtobScB%2FpYW7jYR7Qr4AWkOREChKH0Vffp5zdFxC8VZNAGt%2FNp4sKrGSqlZmnRehZQHkBCH4Y13L9Q0W4iTy5Yr%2BAArQbFkMoYvycqzW9L%2B9XZA4vsAnDTq2NQbFVfGeg4inzKUJVriDTteSBG17Prn%2FR2Z67tlIXT6DPW0BxcAnJPd%2FrnXT4oO4SBqdBScU4yfTmxQrBgr7CG8p6%2BYF14i48GvkOy61546RFdkG%2FsJRiviO4tMH9vCCkfW%2B4dDhvBiLzsn3bAfwa4e%2Fkkh0%2BU9al%2F2%2BwY0jJj6LuKxlMouLZYQYe1a5gt8ldUDSbkIllMWt9HD7DnpIXmdda8ODwdkTdg%2FgdcwMxKUbEZc05lWi1M%2F%2BcQhyWD0ThXmUyajaSIUCinCEL6WLf9PdmVEsj3yVMww9DwvAY6pgEhLPxGoV9I9%2Bf%2BpoF%2Fytmr9PoRAGcakEBwZNI%2F6xl9lfUsqcTIzy2Men92GQ%2Fakt9TJjVGcvRy10pzPag89N2%2FleImdTnb1vA0K6zGeJqd0d6d7yPXR2jcjWi43BQKXihDD1kbPpsWZZ3YYNoiKqLBzOim4fYLC8q8UdHO0%2FS8DZIyMXHZy8aijBVt4FkE4wn3SNXHKcKvkXEDGEnatOg7F8plDc60&X-Amz-Signature=9d94aa1a0c81b416f9c6cbf967076fe9aef88a49f4705576aa20fd4def439a96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664R4TW7BD%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJ3Fhi5eNbA3j16gJbZJ2dt%2FjHWRy6jkgMjmm2ygv8aAIhAP633cGjrIDEo%2B8%2BY%2BVKWfWEGHLvrOoJ7mWn5vwweFe%2BKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgygkLslKB06j8mkX5Eq3ANVjn7zV3uE0Cd94hlOM3%2Bzi%2FtE8HWVlUYvro3eQUDfpI9f7bB9agQqGHTqaN4Dn2pyFeBXAAhWdXuMX5wredlxs2KvHo1tBftgVdBU1v45ZHGOJTWPOgnc%2Ba9v0k0ySta1CB%2Fzm6BtxDldedegQBO89mHWq7%2BgJNQGTkxyldtqeLO1D20cIH3lr1Uk6aI1jp4mughDPACwvJt5azkgzbqxUwcnHU76rJpDwP%2F8xLLkpmVYAI1wob17m6%2BMWB7HleQXElfbegcBVS8%2BRBGRvihC%2BGj5wpDCQDvdQFXhrwnDNuYtSLH%2FHR8X1cAo4rVqP6JpV3rPOy4TCB230RYSb3VSfhMPi7JwenlIZ8JprnDqy0co1ymQS%2BUWsL0VKDTD9UmXJc8yIph667SbK1pXcoYlgWOnDzVvISf1YNH%2F3tiGmx9P34ePZ%2BPZlNJOlFkHOMJN4lq8I8W66TxQN5rpbiBqCZhh4C3RuOkEX6Ya8ZoeeZfBMYXIgWLVMDMN33radrhCrt6NfutJuGQfcC7OUM2s7K8NBkIZZk2iH1K24WZ6SYvl8tvJ35aPIU3w98SnJJh%2B1%2FsF1nz5pLdPEz0K0U3WHXPa5pFfghfMDXulDCxlZGM%2B6iIhVY20sp1RtzD90PC8BjqkASc%2FISOuID6UQPrTdX%2B%2B%2Bqhy3YWY4fXVzJIKvHu5B6YO03lZ%2B1OGnrMqq%2BUMSJhB%2Bb7k8YG%2BzNnFu2LveNf1eaeMtp2KGEOmIyaoKgBUKSXyGVU5rFfvyW8WOwjRcaL6RpIrIUokuKLLBTp0Zepj782xx7%2B7lOVabZrfZWAfCxRc7iLMicvKKQ5u7EVqoRazSRxRhKYtp3JXjwZaqlvfUYVpGbA4&X-Amz-Signature=c64d5bb2b3a44423c64596e18cdd5fc21270bc164ff382de42410445d49629cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL3UFXGA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBXk%2B8Z6tmF0ljXweky8bICc1ezWz2GOUrJhks5d3tisAiAzi1IsZJOu7Aj1D7knEL6bntFYvaryhXgHeNqWlNKiNiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0i6LD6g5HSQMhLMkKtwDNmhntKkoPef9Quo%2Fr7PoL6rGOphFU9nTkYTe2Mi3D%2FirTi94yF9t1hr96eo6xMBYe3ldvd%2B%2Bwg3ClHUeVPk%2FftR9jperkdK6IqEfCnI9EDsAKDSVtypAM1oCki8rlB6HN1Wis%2B0TI7Ti%2BTrr6tq5el62DA0V6HRp7%2Fhnvla1hxHA76PSRmRa1lxARmzD%2BBDflwUSxb7Vs%2B0SNMaCBVmHCk%2Bh7afd%2BmUUi0kHvoAmLGID94QdjIUMWTyKy6NmzNjKoZG%2BGLPk8eRFXX6%2Fem0IHJvMxuA8MnDVOPG4SweRQPVBuHrU9luQ3G4EDMX79gBxMhvd4Igy3QAiq52XClBjS9RRp2oGdUsY1fubU2YAgFRgS9M9oMMRDB9884AD7WQ1%2FX4hAfWGYY%2Fk7o%2FMNsPsBW77vnsEpKee7SYDQXB%2Bk7CeuEasI3wFeIdjxjWehA4j90sPcEXM4JIASiG1Re%2BBcUFg8HXWpmBOLbvd6xpebT93PGytpFDnCxutKvwcbmMc75Vmq9chYT90Ry2BELpPWnlrg4tG4PRqNAc8f00Xxpn%2FqCqYnUVMBYySHcIBXLIuBmjW9kXJJtyf9nFUiC4LYMJKJ3wdrcxFMzKYb5XbA12ulcS23QUxIqunfSMw1dDwvAY6pgE0WA4bI951rBzsWUae3BacxxVdtXzDyDqgA08%2FcLF4IU9%2FaGfcKP9P4HTVPrrdbTN98OOPeRjoGrVJzWGPSC73vokHcg4U%2FAcjrYb2MhfvjK3ZIFfsX0t5hqb74na8lsedjoza94%2BEZZwKFKzfKVloYJRNToteXMf1lC088ZJlYbR8QU16yLpwxB3KLt8Gs9vctWJlyXnP3qEntEuou%2BwT5RPLCIuI&X-Amz-Signature=fc50d844d7e437eb5a52d7644fcfca8d23be2c6a46302dd2c79b199870e98a24&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL3UFXGA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T051439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBXk%2B8Z6tmF0ljXweky8bICc1ezWz2GOUrJhks5d3tisAiAzi1IsZJOu7Aj1D7knEL6bntFYvaryhXgHeNqWlNKiNiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0i6LD6g5HSQMhLMkKtwDNmhntKkoPef9Quo%2Fr7PoL6rGOphFU9nTkYTe2Mi3D%2FirTi94yF9t1hr96eo6xMBYe3ldvd%2B%2Bwg3ClHUeVPk%2FftR9jperkdK6IqEfCnI9EDsAKDSVtypAM1oCki8rlB6HN1Wis%2B0TI7Ti%2BTrr6tq5el62DA0V6HRp7%2Fhnvla1hxHA76PSRmRa1lxARmzD%2BBDflwUSxb7Vs%2B0SNMaCBVmHCk%2Bh7afd%2BmUUi0kHvoAmLGID94QdjIUMWTyKy6NmzNjKoZG%2BGLPk8eRFXX6%2Fem0IHJvMxuA8MnDVOPG4SweRQPVBuHrU9luQ3G4EDMX79gBxMhvd4Igy3QAiq52XClBjS9RRp2oGdUsY1fubU2YAgFRgS9M9oMMRDB9884AD7WQ1%2FX4hAfWGYY%2Fk7o%2FMNsPsBW77vnsEpKee7SYDQXB%2Bk7CeuEasI3wFeIdjxjWehA4j90sPcEXM4JIASiG1Re%2BBcUFg8HXWpmBOLbvd6xpebT93PGytpFDnCxutKvwcbmMc75Vmq9chYT90Ry2BELpPWnlrg4tG4PRqNAc8f00Xxpn%2FqCqYnUVMBYySHcIBXLIuBmjW9kXJJtyf9nFUiC4LYMJKJ3wdrcxFMzKYb5XbA12ulcS23QUxIqunfSMw1dDwvAY6pgE0WA4bI951rBzsWUae3BacxxVdtXzDyDqgA08%2FcLF4IU9%2FaGfcKP9P4HTVPrrdbTN98OOPeRjoGrVJzWGPSC73vokHcg4U%2FAcjrYb2MhfvjK3ZIFfsX0t5hqb74na8lsedjoza94%2BEZZwKFKzfKVloYJRNToteXMf1lC088ZJlYbR8QU16yLpwxB3KLt8Gs9vctWJlyXnP3qEntEuou%2BwT5RPLCIuI&X-Amz-Signature=79e39dea8a916f47e8ad3b111ec75f97403175a1c71e6441c1c5176b8087f41c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
