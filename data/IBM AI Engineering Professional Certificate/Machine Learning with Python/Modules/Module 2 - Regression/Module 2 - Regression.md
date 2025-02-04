

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KNXYBY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIDDI%2FrU57z5JFCiKn3o80tB9CQQdHJx2qfLVrmMHEBF3AiEAjOWItu0Sxcz0uIlcxBKj4yfzo0BI27AiB8wPiFddg%2BQq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDNzesyMxCWwi4fyGOCrcA0VUs6hxc4Wu7huV%2B%2BalHRLWkOXQ8dDhyDiKN65WyU4T9x51UQ1%2FJZfVy0kP8udBqafrM7FcCE5N9XP1cGmof2jPcYglX5zsnSvHdK4I%2FrB7F2SLazwqP34QY6M2nYfO%2Fttf3hIthmSm0z0gwcxgt%2BFXEHM0PKR3ishx6NMdHiQgALPut1NUhP%2FZFK2uc2tii9LJc0owX74A6C5qxe%2BF32VjbkXBgmFUvyrFmVM%2BQYegfhXYFACTZqDgZEygoki5VPhIPPzr%2Bf%2BJoVLYcAMPBdl3JyMyr8%2BtmP2t0O2ztxcNRcJQzzSCuewdLRc%2BgGyPOUywUVo5IJNgZIAPnW6jppu9xcAXZyvGdeIUpbeLGI0SvUvP9%2Fqhk6FE6vWjRZm20%2Fc94vYcwpVJcs0Q%2FsGPTYeDeLe8JA1noy5LYFTbfh40mMgM7KKZwJfJVk1HP3ncLp1oJcbEek0nuMv9vAoNWmCH7LNwr1k%2F9PXLvpiK%2FqvQqsHKNN3dRL7rp24GX1u%2BnZl8TvhrUJt3ZtMAf4g%2FMeMX%2BMAwBNpmLWhefXgo%2BwP2HPieNk2%2BKMlKHQ%2FQscUlrnAKPApXJOV0dzNW%2BUxXV%2BvXImmZy2iCpCceuvunq9RfzzaLPl0CxID8neJGMLy%2Bib0GOqUBvUxt6pPVlFL7xiKcAeu6QeeUbMnvw92tf9Y79GLPwA8h9tMdi58QMpyXX6V0JzYmU4XEWd96GWvU2fzOUedcjLPBrFweq2pPQzNhsKjkryHiszeXL3Lx5Lf3GX42zS788sW%2FxqcOXTZ8QghXbGSRCDPQzQavwXcwC5xcVg9bcIObnYzdJqd%2F4Kb%2BTDkKxsoXIOLDlcVW9U0g%2F1cptEBpXzwv9BcD&X-Amz-Signature=0e8dc58f181d405c23ddcc79327870ff58c4c31841e68ca0ee4fbba33bd26fd4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KNXYBY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIDDI%2FrU57z5JFCiKn3o80tB9CQQdHJx2qfLVrmMHEBF3AiEAjOWItu0Sxcz0uIlcxBKj4yfzo0BI27AiB8wPiFddg%2BQq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDNzesyMxCWwi4fyGOCrcA0VUs6hxc4Wu7huV%2B%2BalHRLWkOXQ8dDhyDiKN65WyU4T9x51UQ1%2FJZfVy0kP8udBqafrM7FcCE5N9XP1cGmof2jPcYglX5zsnSvHdK4I%2FrB7F2SLazwqP34QY6M2nYfO%2Fttf3hIthmSm0z0gwcxgt%2BFXEHM0PKR3ishx6NMdHiQgALPut1NUhP%2FZFK2uc2tii9LJc0owX74A6C5qxe%2BF32VjbkXBgmFUvyrFmVM%2BQYegfhXYFACTZqDgZEygoki5VPhIPPzr%2Bf%2BJoVLYcAMPBdl3JyMyr8%2BtmP2t0O2ztxcNRcJQzzSCuewdLRc%2BgGyPOUywUVo5IJNgZIAPnW6jppu9xcAXZyvGdeIUpbeLGI0SvUvP9%2Fqhk6FE6vWjRZm20%2Fc94vYcwpVJcs0Q%2FsGPTYeDeLe8JA1noy5LYFTbfh40mMgM7KKZwJfJVk1HP3ncLp1oJcbEek0nuMv9vAoNWmCH7LNwr1k%2F9PXLvpiK%2FqvQqsHKNN3dRL7rp24GX1u%2BnZl8TvhrUJt3ZtMAf4g%2FMeMX%2BMAwBNpmLWhefXgo%2BwP2HPieNk2%2BKMlKHQ%2FQscUlrnAKPApXJOV0dzNW%2BUxXV%2BvXImmZy2iCpCceuvunq9RfzzaLPl0CxID8neJGMLy%2Bib0GOqUBvUxt6pPVlFL7xiKcAeu6QeeUbMnvw92tf9Y79GLPwA8h9tMdi58QMpyXX6V0JzYmU4XEWd96GWvU2fzOUedcjLPBrFweq2pPQzNhsKjkryHiszeXL3Lx5Lf3GX42zS788sW%2FxqcOXTZ8QghXbGSRCDPQzQavwXcwC5xcVg9bcIObnYzdJqd%2F4Kb%2BTDkKxsoXIOLDlcVW9U0g%2F1cptEBpXzwv9BcD&X-Amz-Signature=8146aba93ba6c3d4aa4bab0152127a45b750187127ed0680cfc9be59fe57290d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KNXYBY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIDDI%2FrU57z5JFCiKn3o80tB9CQQdHJx2qfLVrmMHEBF3AiEAjOWItu0Sxcz0uIlcxBKj4yfzo0BI27AiB8wPiFddg%2BQq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDNzesyMxCWwi4fyGOCrcA0VUs6hxc4Wu7huV%2B%2BalHRLWkOXQ8dDhyDiKN65WyU4T9x51UQ1%2FJZfVy0kP8udBqafrM7FcCE5N9XP1cGmof2jPcYglX5zsnSvHdK4I%2FrB7F2SLazwqP34QY6M2nYfO%2Fttf3hIthmSm0z0gwcxgt%2BFXEHM0PKR3ishx6NMdHiQgALPut1NUhP%2FZFK2uc2tii9LJc0owX74A6C5qxe%2BF32VjbkXBgmFUvyrFmVM%2BQYegfhXYFACTZqDgZEygoki5VPhIPPzr%2Bf%2BJoVLYcAMPBdl3JyMyr8%2BtmP2t0O2ztxcNRcJQzzSCuewdLRc%2BgGyPOUywUVo5IJNgZIAPnW6jppu9xcAXZyvGdeIUpbeLGI0SvUvP9%2Fqhk6FE6vWjRZm20%2Fc94vYcwpVJcs0Q%2FsGPTYeDeLe8JA1noy5LYFTbfh40mMgM7KKZwJfJVk1HP3ncLp1oJcbEek0nuMv9vAoNWmCH7LNwr1k%2F9PXLvpiK%2FqvQqsHKNN3dRL7rp24GX1u%2BnZl8TvhrUJt3ZtMAf4g%2FMeMX%2BMAwBNpmLWhefXgo%2BwP2HPieNk2%2BKMlKHQ%2FQscUlrnAKPApXJOV0dzNW%2BUxXV%2BvXImmZy2iCpCceuvunq9RfzzaLPl0CxID8neJGMLy%2Bib0GOqUBvUxt6pPVlFL7xiKcAeu6QeeUbMnvw92tf9Y79GLPwA8h9tMdi58QMpyXX6V0JzYmU4XEWd96GWvU2fzOUedcjLPBrFweq2pPQzNhsKjkryHiszeXL3Lx5Lf3GX42zS788sW%2FxqcOXTZ8QghXbGSRCDPQzQavwXcwC5xcVg9bcIObnYzdJqd%2F4Kb%2BTDkKxsoXIOLDlcVW9U0g%2F1cptEBpXzwv9BcD&X-Amz-Signature=64672f5bac16b9437b89fe2c207b72480128cf6c592d94a819380ba057cf7287&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KNXYBY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIDDI%2FrU57z5JFCiKn3o80tB9CQQdHJx2qfLVrmMHEBF3AiEAjOWItu0Sxcz0uIlcxBKj4yfzo0BI27AiB8wPiFddg%2BQq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDNzesyMxCWwi4fyGOCrcA0VUs6hxc4Wu7huV%2B%2BalHRLWkOXQ8dDhyDiKN65WyU4T9x51UQ1%2FJZfVy0kP8udBqafrM7FcCE5N9XP1cGmof2jPcYglX5zsnSvHdK4I%2FrB7F2SLazwqP34QY6M2nYfO%2Fttf3hIthmSm0z0gwcxgt%2BFXEHM0PKR3ishx6NMdHiQgALPut1NUhP%2FZFK2uc2tii9LJc0owX74A6C5qxe%2BF32VjbkXBgmFUvyrFmVM%2BQYegfhXYFACTZqDgZEygoki5VPhIPPzr%2Bf%2BJoVLYcAMPBdl3JyMyr8%2BtmP2t0O2ztxcNRcJQzzSCuewdLRc%2BgGyPOUywUVo5IJNgZIAPnW6jppu9xcAXZyvGdeIUpbeLGI0SvUvP9%2Fqhk6FE6vWjRZm20%2Fc94vYcwpVJcs0Q%2FsGPTYeDeLe8JA1noy5LYFTbfh40mMgM7KKZwJfJVk1HP3ncLp1oJcbEek0nuMv9vAoNWmCH7LNwr1k%2F9PXLvpiK%2FqvQqsHKNN3dRL7rp24GX1u%2BnZl8TvhrUJt3ZtMAf4g%2FMeMX%2BMAwBNpmLWhefXgo%2BwP2HPieNk2%2BKMlKHQ%2FQscUlrnAKPApXJOV0dzNW%2BUxXV%2BvXImmZy2iCpCceuvunq9RfzzaLPl0CxID8neJGMLy%2Bib0GOqUBvUxt6pPVlFL7xiKcAeu6QeeUbMnvw92tf9Y79GLPwA8h9tMdi58QMpyXX6V0JzYmU4XEWd96GWvU2fzOUedcjLPBrFweq2pPQzNhsKjkryHiszeXL3Lx5Lf3GX42zS788sW%2FxqcOXTZ8QghXbGSRCDPQzQavwXcwC5xcVg9bcIObnYzdJqd%2F4Kb%2BTDkKxsoXIOLDlcVW9U0g%2F1cptEBpXzwv9BcD&X-Amz-Signature=3ba67fdeed2ab068e290ddaec4978a25ff2e7a09fa8e470675749633d3069dec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KNXYBY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIDDI%2FrU57z5JFCiKn3o80tB9CQQdHJx2qfLVrmMHEBF3AiEAjOWItu0Sxcz0uIlcxBKj4yfzo0BI27AiB8wPiFddg%2BQq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDNzesyMxCWwi4fyGOCrcA0VUs6hxc4Wu7huV%2B%2BalHRLWkOXQ8dDhyDiKN65WyU4T9x51UQ1%2FJZfVy0kP8udBqafrM7FcCE5N9XP1cGmof2jPcYglX5zsnSvHdK4I%2FrB7F2SLazwqP34QY6M2nYfO%2Fttf3hIthmSm0z0gwcxgt%2BFXEHM0PKR3ishx6NMdHiQgALPut1NUhP%2FZFK2uc2tii9LJc0owX74A6C5qxe%2BF32VjbkXBgmFUvyrFmVM%2BQYegfhXYFACTZqDgZEygoki5VPhIPPzr%2Bf%2BJoVLYcAMPBdl3JyMyr8%2BtmP2t0O2ztxcNRcJQzzSCuewdLRc%2BgGyPOUywUVo5IJNgZIAPnW6jppu9xcAXZyvGdeIUpbeLGI0SvUvP9%2Fqhk6FE6vWjRZm20%2Fc94vYcwpVJcs0Q%2FsGPTYeDeLe8JA1noy5LYFTbfh40mMgM7KKZwJfJVk1HP3ncLp1oJcbEek0nuMv9vAoNWmCH7LNwr1k%2F9PXLvpiK%2FqvQqsHKNN3dRL7rp24GX1u%2BnZl8TvhrUJt3ZtMAf4g%2FMeMX%2BMAwBNpmLWhefXgo%2BwP2HPieNk2%2BKMlKHQ%2FQscUlrnAKPApXJOV0dzNW%2BUxXV%2BvXImmZy2iCpCceuvunq9RfzzaLPl0CxID8neJGMLy%2Bib0GOqUBvUxt6pPVlFL7xiKcAeu6QeeUbMnvw92tf9Y79GLPwA8h9tMdi58QMpyXX6V0JzYmU4XEWd96GWvU2fzOUedcjLPBrFweq2pPQzNhsKjkryHiszeXL3Lx5Lf3GX42zS788sW%2FxqcOXTZ8QghXbGSRCDPQzQavwXcwC5xcVg9bcIObnYzdJqd%2F4Kb%2BTDkKxsoXIOLDlcVW9U0g%2F1cptEBpXzwv9BcD&X-Amz-Signature=3b798c6567f8caee4c853aa84f9d068c9ddeefdc46d05637f28a427a58f4c19f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KNXYBY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIDDI%2FrU57z5JFCiKn3o80tB9CQQdHJx2qfLVrmMHEBF3AiEAjOWItu0Sxcz0uIlcxBKj4yfzo0BI27AiB8wPiFddg%2BQq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDNzesyMxCWwi4fyGOCrcA0VUs6hxc4Wu7huV%2B%2BalHRLWkOXQ8dDhyDiKN65WyU4T9x51UQ1%2FJZfVy0kP8udBqafrM7FcCE5N9XP1cGmof2jPcYglX5zsnSvHdK4I%2FrB7F2SLazwqP34QY6M2nYfO%2Fttf3hIthmSm0z0gwcxgt%2BFXEHM0PKR3ishx6NMdHiQgALPut1NUhP%2FZFK2uc2tii9LJc0owX74A6C5qxe%2BF32VjbkXBgmFUvyrFmVM%2BQYegfhXYFACTZqDgZEygoki5VPhIPPzr%2Bf%2BJoVLYcAMPBdl3JyMyr8%2BtmP2t0O2ztxcNRcJQzzSCuewdLRc%2BgGyPOUywUVo5IJNgZIAPnW6jppu9xcAXZyvGdeIUpbeLGI0SvUvP9%2Fqhk6FE6vWjRZm20%2Fc94vYcwpVJcs0Q%2FsGPTYeDeLe8JA1noy5LYFTbfh40mMgM7KKZwJfJVk1HP3ncLp1oJcbEek0nuMv9vAoNWmCH7LNwr1k%2F9PXLvpiK%2FqvQqsHKNN3dRL7rp24GX1u%2BnZl8TvhrUJt3ZtMAf4g%2FMeMX%2BMAwBNpmLWhefXgo%2BwP2HPieNk2%2BKMlKHQ%2FQscUlrnAKPApXJOV0dzNW%2BUxXV%2BvXImmZy2iCpCceuvunq9RfzzaLPl0CxID8neJGMLy%2Bib0GOqUBvUxt6pPVlFL7xiKcAeu6QeeUbMnvw92tf9Y79GLPwA8h9tMdi58QMpyXX6V0JzYmU4XEWd96GWvU2fzOUedcjLPBrFweq2pPQzNhsKjkryHiszeXL3Lx5Lf3GX42zS788sW%2FxqcOXTZ8QghXbGSRCDPQzQavwXcwC5xcVg9bcIObnYzdJqd%2F4Kb%2BTDkKxsoXIOLDlcVW9U0g%2F1cptEBpXzwv9BcD&X-Amz-Signature=d354ebce218fb71e2c7ad603d0f896057d9589e6a79e980c603f51aae9133efb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KNXYBY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIDDI%2FrU57z5JFCiKn3o80tB9CQQdHJx2qfLVrmMHEBF3AiEAjOWItu0Sxcz0uIlcxBKj4yfzo0BI27AiB8wPiFddg%2BQq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDNzesyMxCWwi4fyGOCrcA0VUs6hxc4Wu7huV%2B%2BalHRLWkOXQ8dDhyDiKN65WyU4T9x51UQ1%2FJZfVy0kP8udBqafrM7FcCE5N9XP1cGmof2jPcYglX5zsnSvHdK4I%2FrB7F2SLazwqP34QY6M2nYfO%2Fttf3hIthmSm0z0gwcxgt%2BFXEHM0PKR3ishx6NMdHiQgALPut1NUhP%2FZFK2uc2tii9LJc0owX74A6C5qxe%2BF32VjbkXBgmFUvyrFmVM%2BQYegfhXYFACTZqDgZEygoki5VPhIPPzr%2Bf%2BJoVLYcAMPBdl3JyMyr8%2BtmP2t0O2ztxcNRcJQzzSCuewdLRc%2BgGyPOUywUVo5IJNgZIAPnW6jppu9xcAXZyvGdeIUpbeLGI0SvUvP9%2Fqhk6FE6vWjRZm20%2Fc94vYcwpVJcs0Q%2FsGPTYeDeLe8JA1noy5LYFTbfh40mMgM7KKZwJfJVk1HP3ncLp1oJcbEek0nuMv9vAoNWmCH7LNwr1k%2F9PXLvpiK%2FqvQqsHKNN3dRL7rp24GX1u%2BnZl8TvhrUJt3ZtMAf4g%2FMeMX%2BMAwBNpmLWhefXgo%2BwP2HPieNk2%2BKMlKHQ%2FQscUlrnAKPApXJOV0dzNW%2BUxXV%2BvXImmZy2iCpCceuvunq9RfzzaLPl0CxID8neJGMLy%2Bib0GOqUBvUxt6pPVlFL7xiKcAeu6QeeUbMnvw92tf9Y79GLPwA8h9tMdi58QMpyXX6V0JzYmU4XEWd96GWvU2fzOUedcjLPBrFweq2pPQzNhsKjkryHiszeXL3Lx5Lf3GX42zS788sW%2FxqcOXTZ8QghXbGSRCDPQzQavwXcwC5xcVg9bcIObnYzdJqd%2F4Kb%2BTDkKxsoXIOLDlcVW9U0g%2F1cptEBpXzwv9BcD&X-Amz-Signature=7689bd29b95955317fa726aafd39cf583835ccee7517feff811e23ffa3581173&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KNXYBY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIDDI%2FrU57z5JFCiKn3o80tB9CQQdHJx2qfLVrmMHEBF3AiEAjOWItu0Sxcz0uIlcxBKj4yfzo0BI27AiB8wPiFddg%2BQq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDNzesyMxCWwi4fyGOCrcA0VUs6hxc4Wu7huV%2B%2BalHRLWkOXQ8dDhyDiKN65WyU4T9x51UQ1%2FJZfVy0kP8udBqafrM7FcCE5N9XP1cGmof2jPcYglX5zsnSvHdK4I%2FrB7F2SLazwqP34QY6M2nYfO%2Fttf3hIthmSm0z0gwcxgt%2BFXEHM0PKR3ishx6NMdHiQgALPut1NUhP%2FZFK2uc2tii9LJc0owX74A6C5qxe%2BF32VjbkXBgmFUvyrFmVM%2BQYegfhXYFACTZqDgZEygoki5VPhIPPzr%2Bf%2BJoVLYcAMPBdl3JyMyr8%2BtmP2t0O2ztxcNRcJQzzSCuewdLRc%2BgGyPOUywUVo5IJNgZIAPnW6jppu9xcAXZyvGdeIUpbeLGI0SvUvP9%2Fqhk6FE6vWjRZm20%2Fc94vYcwpVJcs0Q%2FsGPTYeDeLe8JA1noy5LYFTbfh40mMgM7KKZwJfJVk1HP3ncLp1oJcbEek0nuMv9vAoNWmCH7LNwr1k%2F9PXLvpiK%2FqvQqsHKNN3dRL7rp24GX1u%2BnZl8TvhrUJt3ZtMAf4g%2FMeMX%2BMAwBNpmLWhefXgo%2BwP2HPieNk2%2BKMlKHQ%2FQscUlrnAKPApXJOV0dzNW%2BUxXV%2BvXImmZy2iCpCceuvunq9RfzzaLPl0CxID8neJGMLy%2Bib0GOqUBvUxt6pPVlFL7xiKcAeu6QeeUbMnvw92tf9Y79GLPwA8h9tMdi58QMpyXX6V0JzYmU4XEWd96GWvU2fzOUedcjLPBrFweq2pPQzNhsKjkryHiszeXL3Lx5Lf3GX42zS788sW%2FxqcOXTZ8QghXbGSRCDPQzQavwXcwC5xcVg9bcIObnYzdJqd%2F4Kb%2BTDkKxsoXIOLDlcVW9U0g%2F1cptEBpXzwv9BcD&X-Amz-Signature=2f7404cbacfb6c70a57f1270d423130d5ffce594752a5a5a2fe6664290a4f6a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DUQFR4O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIFn4WNUQCu3zFyXR3DUSsYa%2BXy3tooaMkfd4xRl9t1UOAiBFo3oZ%2FFbTNtXTqBxj0rLIw5BtoWdimBumyPL%2B2VXmxir%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIM5zmWERqYTFNVjcsDKtwDojGDDa5pnMFtdZYs4f%2B550AAKKgK9E6wcTVwLbP5NUS3oRCHQlEfq4xXtisHj6JAT04r2qjwKk7o9HOGoHlgu9Tasi7Q20NMBbwa945%2BcxaAqiTYhuD1nSr58Z%2FgDQV97C5W%2BKSROELoli6V%2Bsw6olLxLmw%2B%2FNnK2aN%2FnAl5YbKKDJPrDBHoLCtW%2B1XBXjYoZ3Bz4e21zqE9UraVShxh%2B%2FXVJRJ0P8fchy0P0CyceTnbOzzREgoKvmTLGgI6vPm66jxu3oclBUvJ9ZmpimN%2F9ERlpj33Y%2BvuXVyMmlmcs%2B8aQMzkXPQW1%2Ft8fPgHjNZT%2Bx8VYBnD%2Fg9E3SRx%2BJz%2FaH7eybOKqQAismvhOJYYYJsEKoi4MOd7s28IP7jxc7TKmQi3zhmx3axUTL%2BRDL8GW9Pq%2FegUC%2FFdLdvLcXhbKQiBD5PB7ahUScf4waEGnLVvZflvRSpc0K491mlfhKJopHyKFmBleF0xHrl%2BXxKbfu5rK08nSbGgsXSNIz%2F%2FcAgBQI%2FwN7p3mZzq8lKfSqjKv7msGevlz36SPpvP%2FjYKpUXfULZEbkVJFW4BYyARG6CApRbDix6KM65ouJDS1%2BkosJDODbizbmgS4buwZjyQIG%2FQqM2xkTGCyDV0t38wkr2JvQY6pgGjQTwbaB4m9wxhPSeNdwMQWu7NGZeuZjfva2BzJAxst%2BY5xr1IyB9NLnh2kNqF10BCNEihuHjAhZocRB5qAlnJDQrsBms50b6hCSMfLXjKO0WHNtwhMZtj6zdUMtq9zuQzsMfAwbUKO5F8tr41WdWHFmRBQQwvzAao33l7kO2BfCufDdtmtAOWr4MXQIiwzDqKOWobtonjkvwlHpEfSDeOv0%2BxhnMp&X-Amz-Signature=eca9571ab76cf5bc641de561c4c9e1153a69476522584832243ddc8144f78336&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OLIQB25%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQCCLce237dfZZlAVxyEhGKIchIZ5yd1SFzD%2F2d90FaScgIgZVKAcRvnO1LdaNF2y8B3T4Ga3F7vw06Tdo%2B5B%2FBfey4q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDJukrQ%2BAHT3aqA0jQyrcAyoknCMqsfhvt9Mn2zh%2BxesvqgdB%2BxZiL2ybK5YprjQ94aJC3jITMk8PTS7SugGCUwXZgPBlp1aTJaA1s7I3f2mc9PD5nsUcHptjxVpw0BRkLrfCndOiz27K2xsvGQKb28BtSdXiLlWnswLXtRPSaQVYEBOzODNk6GCJnY6L720c8qAfGyK6OJAQtFb%2F7vgxsgAs3VTHmrrl2pyCHJ0SBwiv6sE9GpctE9qH6mtOdZ4Mr8%2BBLCEpuNww0bMe9BHqUHcl%2B%2B4sV6aAXi7a%2BRkpE0Pgut2U%2B0JzscU9u979D6AIgs%2FJfYkr9HZAXneHZDWvw%2FMpJ48%2FP9Kc7pMbSgV%2BpICK07EkMffMNGUkFXSWOquDrwBck0COZocHL%2FS6TqrVgfDtnni77boy700IO8LoYp3MMuSWQwbXAbrjJXJ3GDTYR1apSvffRMdQkTmUibWpCuGCc%2BxwmC8sXprMbJbLl9bdipPhYFyo6u5YBvhyMfnhCNYAn1enalQV%2FiyYW8Ci1R0zt%2FUIw53uIn%2Fmu%2BuDAsM7aNlwhl8Muv%2Fv65LxRb53XQgHVzDk2UGSAYovqBq8g2l6u6hqEwXr4RsUAqNkrObelHEveRiKLHIoMDTee71iyzgQosktyU%2Bl3uhQMKu9ib0GOqUBlffguLwIKmR2GT7s1Doyk7fT0%2FdaxVL8c5aSmCMsd6Qo2g7pfR37TlHAZIHznlpN4CFO5v5qQZ%2Bpoo1b24fBHqnF9ru1g8bRtHez2Aggu1SO6%2BGSBPKpwu%2FM5zAlxHSt4z%2BPgXx0nhelgq7I1H7vfLDTR6uVrvhaWwT6TLzMRrenhpExI2bMuE3bnPxPHrIk%2BeEbpNaKn%2BiyUSXYRn5kERHARYWp&X-Amz-Signature=9f0a482714597910fefbc3023a1ffcbded8c527dfcad145c67ae6e5535d6b63c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QH3YOVYX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQCfrECDGZOYE125hLAeuHiah7Q%2BybNhVT8NEQ5M1MJg0QIgdSeOKHyeUnkN65m6RzrRKkIbyp5qiXB98dQBrpf9Fw0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDIgzenjohwKVo73vqircA%2BW78cM4hFkHugzFTWQo6jV7G31XJYx1esfEnYqZpAMXze1tWtUHyx4Z1A9a8hTEgjNQB2oIDstEbjuOrQ2Kmdaq6q2ne%2FsMRi4a%2FcXewIec6KAUawbK4s52gnHMVXeKwr1iEfgx0CJvg5jWP%2Fer0MvZ8zA6FBRu74rQoiEUY%2BfTywmZBYEY6T80ncOeNADah2zZ9iAjM4Qr4prrUOAxB0t4%2BuFOWLr8gLGVOAbQXgWEbWzC%2BoXF29jb6LcU1QjNHm5EYO%2FzHG2zREAozbB0pw8B1wBIuAicboDUEpFaIQ3QjZG3RoO3z3bNrY3nXYqacs4SK0jXc3jPFJa7acoS3OlFyD09pe%2BYpKeXQve5lL0pf6TDJ%2BX2HMahhd0N2TYMer5erPdFApYFRflY0rpgxrNL32bCVGwDzN1GlV2h%2FKsvNLW9w28wZjhDy8d60ioO87c5oimIH4V3vN6mEpBnQD%2F6GBHlq9SpV9rczGfTTUCb%2BkdkNZFYTj5LSASiDgsoP4bjCOUp75i%2F37xrehWT9AzZJub6fra9lHlPNt08k8wbL20u%2Fp26B3pzpENd7LF99Z1AcqcBbiiV5ze7FsbDyFgnug3z7AlezmhEatTUu%2F1t2Xu7v%2BqewGjhNp55MJS9ib0GOqUB30oKunS8R%2BNk2Ip5rljDf%2By3bxBRjHokLvcYUt8kC6PyYhscQ4kkD5fZsTM%2BhjNabd8KcS2IWRAWpOIQ0FCCQSOrKcvL0d%2B9E1J6eZVmxSKMEicZyiHdJar8sTIn732n24QcJRXSwL1LEMhTTyA5fAzBGV9XszTUzdLmp34Yf%2B2L5DplKkgLaTPgAT332qUz8pxycunhVC7kZ1YOP8xodRfgLi2i&X-Amz-Signature=c86842b0113499e570b12c9f1f30201ff5a8788642149de26f9efa6b9a16b596&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QH3YOVYX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQCfrECDGZOYE125hLAeuHiah7Q%2BybNhVT8NEQ5M1MJg0QIgdSeOKHyeUnkN65m6RzrRKkIbyp5qiXB98dQBrpf9Fw0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDIgzenjohwKVo73vqircA%2BW78cM4hFkHugzFTWQo6jV7G31XJYx1esfEnYqZpAMXze1tWtUHyx4Z1A9a8hTEgjNQB2oIDstEbjuOrQ2Kmdaq6q2ne%2FsMRi4a%2FcXewIec6KAUawbK4s52gnHMVXeKwr1iEfgx0CJvg5jWP%2Fer0MvZ8zA6FBRu74rQoiEUY%2BfTywmZBYEY6T80ncOeNADah2zZ9iAjM4Qr4prrUOAxB0t4%2BuFOWLr8gLGVOAbQXgWEbWzC%2BoXF29jb6LcU1QjNHm5EYO%2FzHG2zREAozbB0pw8B1wBIuAicboDUEpFaIQ3QjZG3RoO3z3bNrY3nXYqacs4SK0jXc3jPFJa7acoS3OlFyD09pe%2BYpKeXQve5lL0pf6TDJ%2BX2HMahhd0N2TYMer5erPdFApYFRflY0rpgxrNL32bCVGwDzN1GlV2h%2FKsvNLW9w28wZjhDy8d60ioO87c5oimIH4V3vN6mEpBnQD%2F6GBHlq9SpV9rczGfTTUCb%2BkdkNZFYTj5LSASiDgsoP4bjCOUp75i%2F37xrehWT9AzZJub6fra9lHlPNt08k8wbL20u%2Fp26B3pzpENd7LF99Z1AcqcBbiiV5ze7FsbDyFgnug3z7AlezmhEatTUu%2F1t2Xu7v%2BqewGjhNp55MJS9ib0GOqUB30oKunS8R%2BNk2Ip5rljDf%2By3bxBRjHokLvcYUt8kC6PyYhscQ4kkD5fZsTM%2BhjNabd8KcS2IWRAWpOIQ0FCCQSOrKcvL0d%2B9E1J6eZVmxSKMEicZyiHdJar8sTIn732n24QcJRXSwL1LEMhTTyA5fAzBGV9XszTUzdLmp34Yf%2B2L5DplKkgLaTPgAT332qUz8pxycunhVC7kZ1YOP8xodRfgLi2i&X-Amz-Signature=9ca8310466f6aa9fb24551334594a4beeaadbf9af0b362fbafb149659132bb84&X-Amz-SignedHeaders=host&x-id=GetObject)
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
