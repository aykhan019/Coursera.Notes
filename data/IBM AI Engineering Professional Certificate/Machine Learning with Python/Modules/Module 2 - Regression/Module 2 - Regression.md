

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGG6O4XS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDc1wYL4nt%2BiIPFLraxrJ74Ng2fW%2BiRgoCuof4FEFrYSAiBex0NlPJchimVJ52MCbbcfCnKeqMn1na1DuwXXnQyZYCr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMALFV2Xx6BjHlsiuWKtwDtWztnEXvxCxaBDaw7le6kbUwlKc0TDyWlkahzym57riEgAwFWH%2FXTMUK2F2uUvpYk9eRbce7EikNZdA6hrHf9weDrqiwZjCe0vLoggM69kxiB6vrXsB8sa9o7mU7RF21WNFwKnkys2bj2M7sOBZ8UGDCifUVrWuRW9m%2BZ0ASoRhD89bHrrCRrKg%2FqVZKikviFy%2BaxOB4mDhfZZWWz%2BdAsW3T5YR4sf3N3CwGixWUWFHHruVvmv4Jb%2BETVDDrENtnnolN2uKo6dTYSAkarWJT4Fmpl2udFlLG4qVhd4hRWMEy9k5wn1gBITNSV13Kym2FD6DtRT1aSxgm%2BADQgpb2%2F3eKG051LlxjdgttmaVnPlKIt7YfE0ZE5VyEK56T38V5tXDGgXwkReKXfStF895Sitzf8cFFBOtu6tR8AzUucVmRyEARpW5aUnodjaabniISmB1EzD06z1cGAypxNktAfU2owp4FGoGiI5Ya8jIshasP%2F%2Bf%2FeP6N4Oeg4FKDrJImWZl6tC1ufy1TKKnPHvpFuhpYkKK0XQuvkw4nJZx1s8ozfu5GqpjDYRMI9to51CKaesJSFdHPDs0JHOqOYqSkUtblwrcsmx%2FZkCCWn%2BN2dv7O9CpSCqBZidIvnxswm46DvQY6pgFxUNmO1UKiuvZZjnaanj4p2r1SHiboBu7im%2BYdinrJ1IW4XhypIewZdXoI6CN2w9A4vWc64P0AloooVckdzoHUoQgGZXckNtWj0uTy2093xbzLouFN1%2B8uRoxYVLMoQFQVHuNl6qNeLEB5R6XOrJ3LZvOmKCrZlHA4k0zo84MBNW2ZA6oyt4kpn9Sd4nKjiz9TBBVenjU%2FwgbxKe8zTI3%2FEfHUiWLH&X-Amz-Signature=b47437b5786c78fde5261e4db401e7c7aab64fe177ebebe04891cef887766342&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGG6O4XS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDc1wYL4nt%2BiIPFLraxrJ74Ng2fW%2BiRgoCuof4FEFrYSAiBex0NlPJchimVJ52MCbbcfCnKeqMn1na1DuwXXnQyZYCr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMALFV2Xx6BjHlsiuWKtwDtWztnEXvxCxaBDaw7le6kbUwlKc0TDyWlkahzym57riEgAwFWH%2FXTMUK2F2uUvpYk9eRbce7EikNZdA6hrHf9weDrqiwZjCe0vLoggM69kxiB6vrXsB8sa9o7mU7RF21WNFwKnkys2bj2M7sOBZ8UGDCifUVrWuRW9m%2BZ0ASoRhD89bHrrCRrKg%2FqVZKikviFy%2BaxOB4mDhfZZWWz%2BdAsW3T5YR4sf3N3CwGixWUWFHHruVvmv4Jb%2BETVDDrENtnnolN2uKo6dTYSAkarWJT4Fmpl2udFlLG4qVhd4hRWMEy9k5wn1gBITNSV13Kym2FD6DtRT1aSxgm%2BADQgpb2%2F3eKG051LlxjdgttmaVnPlKIt7YfE0ZE5VyEK56T38V5tXDGgXwkReKXfStF895Sitzf8cFFBOtu6tR8AzUucVmRyEARpW5aUnodjaabniISmB1EzD06z1cGAypxNktAfU2owp4FGoGiI5Ya8jIshasP%2F%2Bf%2FeP6N4Oeg4FKDrJImWZl6tC1ufy1TKKnPHvpFuhpYkKK0XQuvkw4nJZx1s8ozfu5GqpjDYRMI9to51CKaesJSFdHPDs0JHOqOYqSkUtblwrcsmx%2FZkCCWn%2BN2dv7O9CpSCqBZidIvnxswm46DvQY6pgFxUNmO1UKiuvZZjnaanj4p2r1SHiboBu7im%2BYdinrJ1IW4XhypIewZdXoI6CN2w9A4vWc64P0AloooVckdzoHUoQgGZXckNtWj0uTy2093xbzLouFN1%2B8uRoxYVLMoQFQVHuNl6qNeLEB5R6XOrJ3LZvOmKCrZlHA4k0zo84MBNW2ZA6oyt4kpn9Sd4nKjiz9TBBVenjU%2FwgbxKe8zTI3%2FEfHUiWLH&X-Amz-Signature=1a689c6d933550c92847c20fd70e6bf9677caabc4035e9afcce8004f6b184927&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGG6O4XS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDc1wYL4nt%2BiIPFLraxrJ74Ng2fW%2BiRgoCuof4FEFrYSAiBex0NlPJchimVJ52MCbbcfCnKeqMn1na1DuwXXnQyZYCr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMALFV2Xx6BjHlsiuWKtwDtWztnEXvxCxaBDaw7le6kbUwlKc0TDyWlkahzym57riEgAwFWH%2FXTMUK2F2uUvpYk9eRbce7EikNZdA6hrHf9weDrqiwZjCe0vLoggM69kxiB6vrXsB8sa9o7mU7RF21WNFwKnkys2bj2M7sOBZ8UGDCifUVrWuRW9m%2BZ0ASoRhD89bHrrCRrKg%2FqVZKikviFy%2BaxOB4mDhfZZWWz%2BdAsW3T5YR4sf3N3CwGixWUWFHHruVvmv4Jb%2BETVDDrENtnnolN2uKo6dTYSAkarWJT4Fmpl2udFlLG4qVhd4hRWMEy9k5wn1gBITNSV13Kym2FD6DtRT1aSxgm%2BADQgpb2%2F3eKG051LlxjdgttmaVnPlKIt7YfE0ZE5VyEK56T38V5tXDGgXwkReKXfStF895Sitzf8cFFBOtu6tR8AzUucVmRyEARpW5aUnodjaabniISmB1EzD06z1cGAypxNktAfU2owp4FGoGiI5Ya8jIshasP%2F%2Bf%2FeP6N4Oeg4FKDrJImWZl6tC1ufy1TKKnPHvpFuhpYkKK0XQuvkw4nJZx1s8ozfu5GqpjDYRMI9to51CKaesJSFdHPDs0JHOqOYqSkUtblwrcsmx%2FZkCCWn%2BN2dv7O9CpSCqBZidIvnxswm46DvQY6pgFxUNmO1UKiuvZZjnaanj4p2r1SHiboBu7im%2BYdinrJ1IW4XhypIewZdXoI6CN2w9A4vWc64P0AloooVckdzoHUoQgGZXckNtWj0uTy2093xbzLouFN1%2B8uRoxYVLMoQFQVHuNl6qNeLEB5R6XOrJ3LZvOmKCrZlHA4k0zo84MBNW2ZA6oyt4kpn9Sd4nKjiz9TBBVenjU%2FwgbxKe8zTI3%2FEfHUiWLH&X-Amz-Signature=f21586363ce3f1d3de4919e37be0efe24603cd4e61f8b29fe917f389343b562b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGG6O4XS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDc1wYL4nt%2BiIPFLraxrJ74Ng2fW%2BiRgoCuof4FEFrYSAiBex0NlPJchimVJ52MCbbcfCnKeqMn1na1DuwXXnQyZYCr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMALFV2Xx6BjHlsiuWKtwDtWztnEXvxCxaBDaw7le6kbUwlKc0TDyWlkahzym57riEgAwFWH%2FXTMUK2F2uUvpYk9eRbce7EikNZdA6hrHf9weDrqiwZjCe0vLoggM69kxiB6vrXsB8sa9o7mU7RF21WNFwKnkys2bj2M7sOBZ8UGDCifUVrWuRW9m%2BZ0ASoRhD89bHrrCRrKg%2FqVZKikviFy%2BaxOB4mDhfZZWWz%2BdAsW3T5YR4sf3N3CwGixWUWFHHruVvmv4Jb%2BETVDDrENtnnolN2uKo6dTYSAkarWJT4Fmpl2udFlLG4qVhd4hRWMEy9k5wn1gBITNSV13Kym2FD6DtRT1aSxgm%2BADQgpb2%2F3eKG051LlxjdgttmaVnPlKIt7YfE0ZE5VyEK56T38V5tXDGgXwkReKXfStF895Sitzf8cFFBOtu6tR8AzUucVmRyEARpW5aUnodjaabniISmB1EzD06z1cGAypxNktAfU2owp4FGoGiI5Ya8jIshasP%2F%2Bf%2FeP6N4Oeg4FKDrJImWZl6tC1ufy1TKKnPHvpFuhpYkKK0XQuvkw4nJZx1s8ozfu5GqpjDYRMI9to51CKaesJSFdHPDs0JHOqOYqSkUtblwrcsmx%2FZkCCWn%2BN2dv7O9CpSCqBZidIvnxswm46DvQY6pgFxUNmO1UKiuvZZjnaanj4p2r1SHiboBu7im%2BYdinrJ1IW4XhypIewZdXoI6CN2w9A4vWc64P0AloooVckdzoHUoQgGZXckNtWj0uTy2093xbzLouFN1%2B8uRoxYVLMoQFQVHuNl6qNeLEB5R6XOrJ3LZvOmKCrZlHA4k0zo84MBNW2ZA6oyt4kpn9Sd4nKjiz9TBBVenjU%2FwgbxKe8zTI3%2FEfHUiWLH&X-Amz-Signature=30cb333352badbf7578e804acfe37d38853034e4ef30069db917984a156c4f87&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGG6O4XS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDc1wYL4nt%2BiIPFLraxrJ74Ng2fW%2BiRgoCuof4FEFrYSAiBex0NlPJchimVJ52MCbbcfCnKeqMn1na1DuwXXnQyZYCr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMALFV2Xx6BjHlsiuWKtwDtWztnEXvxCxaBDaw7le6kbUwlKc0TDyWlkahzym57riEgAwFWH%2FXTMUK2F2uUvpYk9eRbce7EikNZdA6hrHf9weDrqiwZjCe0vLoggM69kxiB6vrXsB8sa9o7mU7RF21WNFwKnkys2bj2M7sOBZ8UGDCifUVrWuRW9m%2BZ0ASoRhD89bHrrCRrKg%2FqVZKikviFy%2BaxOB4mDhfZZWWz%2BdAsW3T5YR4sf3N3CwGixWUWFHHruVvmv4Jb%2BETVDDrENtnnolN2uKo6dTYSAkarWJT4Fmpl2udFlLG4qVhd4hRWMEy9k5wn1gBITNSV13Kym2FD6DtRT1aSxgm%2BADQgpb2%2F3eKG051LlxjdgttmaVnPlKIt7YfE0ZE5VyEK56T38V5tXDGgXwkReKXfStF895Sitzf8cFFBOtu6tR8AzUucVmRyEARpW5aUnodjaabniISmB1EzD06z1cGAypxNktAfU2owp4FGoGiI5Ya8jIshasP%2F%2Bf%2FeP6N4Oeg4FKDrJImWZl6tC1ufy1TKKnPHvpFuhpYkKK0XQuvkw4nJZx1s8ozfu5GqpjDYRMI9to51CKaesJSFdHPDs0JHOqOYqSkUtblwrcsmx%2FZkCCWn%2BN2dv7O9CpSCqBZidIvnxswm46DvQY6pgFxUNmO1UKiuvZZjnaanj4p2r1SHiboBu7im%2BYdinrJ1IW4XhypIewZdXoI6CN2w9A4vWc64P0AloooVckdzoHUoQgGZXckNtWj0uTy2093xbzLouFN1%2B8uRoxYVLMoQFQVHuNl6qNeLEB5R6XOrJ3LZvOmKCrZlHA4k0zo84MBNW2ZA6oyt4kpn9Sd4nKjiz9TBBVenjU%2FwgbxKe8zTI3%2FEfHUiWLH&X-Amz-Signature=4ec4ef9808620f051eef44681d6c7987e68616e71910bdc8f5296c704a010dd2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGG6O4XS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDc1wYL4nt%2BiIPFLraxrJ74Ng2fW%2BiRgoCuof4FEFrYSAiBex0NlPJchimVJ52MCbbcfCnKeqMn1na1DuwXXnQyZYCr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMALFV2Xx6BjHlsiuWKtwDtWztnEXvxCxaBDaw7le6kbUwlKc0TDyWlkahzym57riEgAwFWH%2FXTMUK2F2uUvpYk9eRbce7EikNZdA6hrHf9weDrqiwZjCe0vLoggM69kxiB6vrXsB8sa9o7mU7RF21WNFwKnkys2bj2M7sOBZ8UGDCifUVrWuRW9m%2BZ0ASoRhD89bHrrCRrKg%2FqVZKikviFy%2BaxOB4mDhfZZWWz%2BdAsW3T5YR4sf3N3CwGixWUWFHHruVvmv4Jb%2BETVDDrENtnnolN2uKo6dTYSAkarWJT4Fmpl2udFlLG4qVhd4hRWMEy9k5wn1gBITNSV13Kym2FD6DtRT1aSxgm%2BADQgpb2%2F3eKG051LlxjdgttmaVnPlKIt7YfE0ZE5VyEK56T38V5tXDGgXwkReKXfStF895Sitzf8cFFBOtu6tR8AzUucVmRyEARpW5aUnodjaabniISmB1EzD06z1cGAypxNktAfU2owp4FGoGiI5Ya8jIshasP%2F%2Bf%2FeP6N4Oeg4FKDrJImWZl6tC1ufy1TKKnPHvpFuhpYkKK0XQuvkw4nJZx1s8ozfu5GqpjDYRMI9to51CKaesJSFdHPDs0JHOqOYqSkUtblwrcsmx%2FZkCCWn%2BN2dv7O9CpSCqBZidIvnxswm46DvQY6pgFxUNmO1UKiuvZZjnaanj4p2r1SHiboBu7im%2BYdinrJ1IW4XhypIewZdXoI6CN2w9A4vWc64P0AloooVckdzoHUoQgGZXckNtWj0uTy2093xbzLouFN1%2B8uRoxYVLMoQFQVHuNl6qNeLEB5R6XOrJ3LZvOmKCrZlHA4k0zo84MBNW2ZA6oyt4kpn9Sd4nKjiz9TBBVenjU%2FwgbxKe8zTI3%2FEfHUiWLH&X-Amz-Signature=99762a013a1bdd62cc31b7b923d48cc54a5a3343bb96fea3aebf99d780a0f66a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGG6O4XS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDc1wYL4nt%2BiIPFLraxrJ74Ng2fW%2BiRgoCuof4FEFrYSAiBex0NlPJchimVJ52MCbbcfCnKeqMn1na1DuwXXnQyZYCr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMALFV2Xx6BjHlsiuWKtwDtWztnEXvxCxaBDaw7le6kbUwlKc0TDyWlkahzym57riEgAwFWH%2FXTMUK2F2uUvpYk9eRbce7EikNZdA6hrHf9weDrqiwZjCe0vLoggM69kxiB6vrXsB8sa9o7mU7RF21WNFwKnkys2bj2M7sOBZ8UGDCifUVrWuRW9m%2BZ0ASoRhD89bHrrCRrKg%2FqVZKikviFy%2BaxOB4mDhfZZWWz%2BdAsW3T5YR4sf3N3CwGixWUWFHHruVvmv4Jb%2BETVDDrENtnnolN2uKo6dTYSAkarWJT4Fmpl2udFlLG4qVhd4hRWMEy9k5wn1gBITNSV13Kym2FD6DtRT1aSxgm%2BADQgpb2%2F3eKG051LlxjdgttmaVnPlKIt7YfE0ZE5VyEK56T38V5tXDGgXwkReKXfStF895Sitzf8cFFBOtu6tR8AzUucVmRyEARpW5aUnodjaabniISmB1EzD06z1cGAypxNktAfU2owp4FGoGiI5Ya8jIshasP%2F%2Bf%2FeP6N4Oeg4FKDrJImWZl6tC1ufy1TKKnPHvpFuhpYkKK0XQuvkw4nJZx1s8ozfu5GqpjDYRMI9to51CKaesJSFdHPDs0JHOqOYqSkUtblwrcsmx%2FZkCCWn%2BN2dv7O9CpSCqBZidIvnxswm46DvQY6pgFxUNmO1UKiuvZZjnaanj4p2r1SHiboBu7im%2BYdinrJ1IW4XhypIewZdXoI6CN2w9A4vWc64P0AloooVckdzoHUoQgGZXckNtWj0uTy2093xbzLouFN1%2B8uRoxYVLMoQFQVHuNl6qNeLEB5R6XOrJ3LZvOmKCrZlHA4k0zo84MBNW2ZA6oyt4kpn9Sd4nKjiz9TBBVenjU%2FwgbxKe8zTI3%2FEfHUiWLH&X-Amz-Signature=5a2f637be4dec83b24aefc35af3ae6bccbac285f5d0358cfda040c927ca45821&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGG6O4XS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDc1wYL4nt%2BiIPFLraxrJ74Ng2fW%2BiRgoCuof4FEFrYSAiBex0NlPJchimVJ52MCbbcfCnKeqMn1na1DuwXXnQyZYCr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMALFV2Xx6BjHlsiuWKtwDtWztnEXvxCxaBDaw7le6kbUwlKc0TDyWlkahzym57riEgAwFWH%2FXTMUK2F2uUvpYk9eRbce7EikNZdA6hrHf9weDrqiwZjCe0vLoggM69kxiB6vrXsB8sa9o7mU7RF21WNFwKnkys2bj2M7sOBZ8UGDCifUVrWuRW9m%2BZ0ASoRhD89bHrrCRrKg%2FqVZKikviFy%2BaxOB4mDhfZZWWz%2BdAsW3T5YR4sf3N3CwGixWUWFHHruVvmv4Jb%2BETVDDrENtnnolN2uKo6dTYSAkarWJT4Fmpl2udFlLG4qVhd4hRWMEy9k5wn1gBITNSV13Kym2FD6DtRT1aSxgm%2BADQgpb2%2F3eKG051LlxjdgttmaVnPlKIt7YfE0ZE5VyEK56T38V5tXDGgXwkReKXfStF895Sitzf8cFFBOtu6tR8AzUucVmRyEARpW5aUnodjaabniISmB1EzD06z1cGAypxNktAfU2owp4FGoGiI5Ya8jIshasP%2F%2Bf%2FeP6N4Oeg4FKDrJImWZl6tC1ufy1TKKnPHvpFuhpYkKK0XQuvkw4nJZx1s8ozfu5GqpjDYRMI9to51CKaesJSFdHPDs0JHOqOYqSkUtblwrcsmx%2FZkCCWn%2BN2dv7O9CpSCqBZidIvnxswm46DvQY6pgFxUNmO1UKiuvZZjnaanj4p2r1SHiboBu7im%2BYdinrJ1IW4XhypIewZdXoI6CN2w9A4vWc64P0AloooVckdzoHUoQgGZXckNtWj0uTy2093xbzLouFN1%2B8uRoxYVLMoQFQVHuNl6qNeLEB5R6XOrJ3LZvOmKCrZlHA4k0zo84MBNW2ZA6oyt4kpn9Sd4nKjiz9TBBVenjU%2FwgbxKe8zTI3%2FEfHUiWLH&X-Amz-Signature=c5b5c74f14279c841f9ebf744d83358d112b13dd0b296c787a375e65875dfeea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUK4E7GU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE37FSx388%2FGLgHgPhwDhWUpsx2CUn%2BypS%2F73QiDG%2BpWAiAsn6LrTpcdYWK70sXsDUEFUdxDunfLVIeGDT1%2FNIcDvCr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIM5Zogyu0Rr8bWpzfCKtwDJiZ6eoDkE0RSig%2BNVYtQAVodmrhRfi8cMV8oX2GOT5MpdbyaHhxAuWWUegVY59sI9F1Ol2Zx8vv1HsGq%2F2cpfLjRCVtOo2sS6Sv2Gumzzqw09%2Bml7guPt%2BMEY%2F1vYfgMjo9ELApUM%2Fs0j6a%2FywPPjHRz2%2FEEfC%2FG4HT9yLSJ2rxvMB685T5xL5fqkxU5s0Gqe5GAavYo%2FHob4oca2GhXwBaqi%2B6Dx90yMwEhkCK6Qdl%2FovlVfDb7Sb4WU0Vp2%2BuQEDYwv%2FU%2FywbcqeIs8UxM2iL0H6Ite5goaT%2BTdgF38ynXa%2F55EFe7XNXPWFDZ3ZzWGw6j92Az18OXqLMqhEJ%2BSRMNYPBsP6zCtn1FthcWh9KO5w6waOuoX9Tz5nA6tHOtqhIuSn9mg0xEWZjS%2FAf4CPsVW3dzzw61OeChrlbcTQNWXUF4nRNphGDgzHv0pujgGWvtQCiQnbJsUVaYjRyGDlGnxg5nQ45pBF0B5eb4SrmIIlK83OA6EdMl%2BIoMS1%2BYFmrXIOXbqQ1wyPh%2BnoZpzP0n24fKGsJF74gxWOcnzJt%2F3EP%2FdKBg76Y2hyI4%2FuSwLGusc4BhaLgpWAFeUydtLqpA%2FZzrAuRqb84Q2P9KE5Q%2BfpQfRX952bzMqHkw7Y2DvQY6pgHDUPAfFjsFiqv8O4ZbbelrKQQHVUYEXGMNPWJYovmZ4klZCq6futunXr%2BjaQU49ejWSiyUC9e3%2FFwBG8Tsssu3R9ReceJl6RwMAiPXVjS68Hde6y3eiVDypwZBzJGZnjLACDaJFWq7jHt8%2FzPMrVPkzLzQZJ4pO1EgfGNicuZq6ojko0Fb1ZUcFdkb3Y5SuyOB3%2F0XAT55mgVxzJL8Vl5uH%2FHue6iW&X-Amz-Signature=359179462bbf8c503438cc15733fe45c76455e4594fe6c42f215588543f068c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ST4NCI4V%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFzWiRiYfYslTUqGtm5SCblDPn1tBbuiNUKRnB9ZHWjzAiBoSTtm1nINml%2FbCEUfFiKw6xilRDSX6OSLtolO9yvOqCr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMsSaDL55AkaiHnrQoKtwDxLUIC6kpgJnFgl%2Bid7X4twHZC7eb3ShxU%2F0H6WScEn72b0CXtOegIkNyk04%2FsuEp9WfKG3LY19v6poz9MQdAIKKKOxsvUb75%2F557X6mm4fvyHrJ5PA%2Bype7T%2BrucClB4%2FNvhZ%2FcnG5Nf2XqO6uwH18cCLKJaZOpogZvXqmy8g1IiKTMHWOwi1C5RL4q%2BNmgmn6CEauOpgY4EXeTJsNeA8M%2FTRHe3P2OPrpT6b2CyZKkeGLgjkX%2BMm1gBemx8bgGzz9ZNlOEaf%2Fn%2BvfWUVa8YBa5zx6XD5b%2BFwnE1vEiPWFcD5KFA6FzWQNlIFRKyBoSfNcte%2BtsfLHiFllpvc8v0aJUpeFLlByi32HLpvlZC0kZ1u%2B3LKnT4DaznTeiwpJ6wj6p7t8Q8avvbthgF8TMY3ML0fOrYGeOtz0DUpPprvJ52Rbv%2BHPv5bCpLgdLlc2Z6dn1%2FdEwhnEbr7wdKhQOdSFYk9GZSJfeENOe%2F9EC769SkP4kkqgoC%2B2TYuH%2F4F5MCvNt2337ZuNzCX8O5GvDZI6cww8I4pV85hx4ZvDC55cfVjKbERPfV%2BYzHCww%2FXvWG8Gwol%2Bu5gAYGS8%2BfvMqOY4JkDfpV8IoN3EDsmFIDp7lexPduTwLC4Bd%2BBCEwvY2DvQY6pgHLywqkGkZTWM29yqrzEyQ4O2C%2B47t6qiBwWzKAvZv3eB1SoXCiHuYTgozj6DArNzyoxHZ0n1w40%2BI3xUbT9ingB5Rr2P89NMXQJyK5V8Mnh1B2PwvYVQrWKLhbJYq9%2BDnGm0W%2BQUAjgx%2BRqxo9uFlqGMsz%2FrZwP6rlTzoMI2i6MqV8%2FCT4JT41szjEHXvkgLj8XR%2FMIh0y8CvS00wckRDMBy02yDdC&X-Amz-Signature=87784a867eed0e5effda209de2ecb9be8afdce12cc9edcfbd7ca8e88a44f4687&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YX7BLZT6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEmUE2jwCzou4MGfujW4a83Dk1vvmk0wUhnVa7C7CKswAiARmfiULCXQtWzKvQMEGctEHNj1P1sIw2P5OMSidWB6MCr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMp5tW1Tq72tM6P1i0KtwDfJ6lu2ozo83ZXLbJEDfTf6B4X%2FoOAozxQfUUhztw%2FvsgzFrXSjEpanMyKdJJyBWez0UA6g5m%2FCMOLUpd1nw3zUCJIKRv2wa4aCMJZrYsPqWIfhcMPdayWa%2Fq%2FJ%2Bya92t6Op0vgUhsK%2Fwt%2BZjvZXCVn8sx%2FO%2FaK0DPnvUrzGWmkTGHn1IcZDsb%2Fm1Zae%2FSHNkLl5eOYwaTA%2FkGlA8ZA9XKA%2F8dO%2BCSslpxamg1DTu7PJGorD3lQWofwrsgJXiqkQfxHNu7wCBrXOhwIuB6%2FMqIgQd1eNQSZGeh9XHJ7nCJUFGZJCtHTpdHuzo%2FSs3uamfl8ITMu%2BAo4bwtO4I%2Bs7n4LQ5w6p8QehkakfzGBbgk74nQqkAgkQySHXiDOUsPD22YW26GR9NPNCYF22yXX1XV%2BPJs8efCq5TX49Tpd1gXNhXVt9Hm6Th0DHQuJAolUMIfRCIRmHu9X4urYZcR%2FBFmHXYwkwQ4L%2FbRN4STfbBcYsEOIT%2FtNNSLfu0ha6UMOyAPuMecdvgi%2FLp6DHWmRoKLv2Lt6FTS9VuiKrRRloTYjcDcOjORTSYmztA35yq5e5Q4sR1z0VpH7MYqGEg9f80S6MnfN8cgmksRIPNQYFX%2BaVMZyRriUvcfwqtId0w0Y2DvQY6pgHpQPBSCTVrEz%2BPfUODtpWbtWvRh2e%2FkFSifPZrMez2Rcku7miG8%2BdWk7le9q1QvWFxKG2aJFkrhrfwG%2FDQhBn4PMK%2F5FiGYbIMI0qnL5joHHRgnIOzEb81SNlIAxw7WofblyyZumfYqS45pfFo7M12vHr2OqAoQ%2BJWHpj1K84izwK9Wtgf%2FMeMPnuW8NhfyBTDro7zVChII903c9mYsiUMYigm9%2BdH&X-Amz-Signature=4e8e02e3026e5a1eef6139e2f6908544f3a825270ad7fe08d3a293d5a48deef1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YX7BLZT6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEmUE2jwCzou4MGfujW4a83Dk1vvmk0wUhnVa7C7CKswAiARmfiULCXQtWzKvQMEGctEHNj1P1sIw2P5OMSidWB6MCr%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMp5tW1Tq72tM6P1i0KtwDfJ6lu2ozo83ZXLbJEDfTf6B4X%2FoOAozxQfUUhztw%2FvsgzFrXSjEpanMyKdJJyBWez0UA6g5m%2FCMOLUpd1nw3zUCJIKRv2wa4aCMJZrYsPqWIfhcMPdayWa%2Fq%2FJ%2Bya92t6Op0vgUhsK%2Fwt%2BZjvZXCVn8sx%2FO%2FaK0DPnvUrzGWmkTGHn1IcZDsb%2Fm1Zae%2FSHNkLl5eOYwaTA%2FkGlA8ZA9XKA%2F8dO%2BCSslpxamg1DTu7PJGorD3lQWofwrsgJXiqkQfxHNu7wCBrXOhwIuB6%2FMqIgQd1eNQSZGeh9XHJ7nCJUFGZJCtHTpdHuzo%2FSs3uamfl8ITMu%2BAo4bwtO4I%2Bs7n4LQ5w6p8QehkakfzGBbgk74nQqkAgkQySHXiDOUsPD22YW26GR9NPNCYF22yXX1XV%2BPJs8efCq5TX49Tpd1gXNhXVt9Hm6Th0DHQuJAolUMIfRCIRmHu9X4urYZcR%2FBFmHXYwkwQ4L%2FbRN4STfbBcYsEOIT%2FtNNSLfu0ha6UMOyAPuMecdvgi%2FLp6DHWmRoKLv2Lt6FTS9VuiKrRRloTYjcDcOjORTSYmztA35yq5e5Q4sR1z0VpH7MYqGEg9f80S6MnfN8cgmksRIPNQYFX%2BaVMZyRriUvcfwqtId0w0Y2DvQY6pgHpQPBSCTVrEz%2BPfUODtpWbtWvRh2e%2FkFSifPZrMez2Rcku7miG8%2BdWk7le9q1QvWFxKG2aJFkrhrfwG%2FDQhBn4PMK%2F5FiGYbIMI0qnL5joHHRgnIOzEb81SNlIAxw7WofblyyZumfYqS45pfFo7M12vHr2OqAoQ%2BJWHpj1K84izwK9Wtgf%2FMeMPnuW8NhfyBTDro7zVChII903c9mYsiUMYigm9%2BdH&X-Amz-Signature=f913fd98971d349f58699fcf397d4df3a24c5001abf05794f4f029dd3ae402ba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
