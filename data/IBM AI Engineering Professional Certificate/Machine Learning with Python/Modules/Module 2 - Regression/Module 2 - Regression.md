

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2NPLGF4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIB63T9SNVXI6iXJb6Qa8E0xUzApkpUjG7sGkAeNxKdXYAiEAqR0LdNxwf0I7c0uhjgyFqEVUaNrpaNE6r%2FRWUV9yH%2BMq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDCAYWvEJulgXRPfdMircA0q44uqcK%2BZDD%2FsrVa9L5BD0WpY4ceSrOTPj74wyR03FMMMG5P442e5PL9PSD%2BL4qfRtkUTgwutkc3Ae66VSND6ILzxIRCwOYHuUmJGcnyPBgueK1MIQCxM%2FI7PQ3%2FGmF1HulisVoaEWF5PLaRH30ZG0RDG0awOde1%2FlS8G2GBfOmAzRFthrZVMrn95arW7W3sgQsV%2FTyFuveEOOdjwdjAV8c5JJcV2X%2FASvambGWXw12XcD5bHiIAg%2BfSSKDt7ZOZls1MdOLcQ3fsjYM2HH%2BxnzbExZmnw2h7uxrQEYc6%2FesV%2FYWKvqi8t69nTvcpTFKCIaTHA%2BghR4C3rl8fbQ%2BzxjJ4AJH1D8qKQm0%2FdroLgt1htaXTL8KdNDBHpfE8WLPzY%2F9pLepjdctLbtz6FJW8aeDLfQgt3Dr0Ddp3Th2gd6va2tjiSkWGLze5LVsbOCfkRZYcKYXLQ4Ng%2FPybWj6fopx8abnLbBqUlPmYYyLk2rc68QlLS9PmwAT5zqdrQS%2FgfM1%2FOugknYNeWTf3EWpmbylpRNJ0B%2Fks17aePgpKIKJYPuP6lFrsX6863JE%2F%2BHSUZMDikxoN5LPRvwoLAz4xn4DT6Spr3gBglMfEkGGSQYz5pDqEmgtXB5IbGjMJ7skb0GOqUB3KyalWrVmsC5QuS59hJ0I%2Fw8rOrb6UqYlGx4MIU8lpPN%2BHLGoKm%2FTejA%2FnU4wJdRf4LLNFmbIPOXUWtRTY%2FFR6RQc8jmlBCjyOshg4yLbE9F7KsBw7thgYJspXodv9fFQBjxZolVlxz0A1jK8q8mTsMfQm%2F0EHCxIVH14Yy641ci%2FONbr2Dxy3rnJM%2Be05r1jfzp%2B5Zam%2FIwZMSgk8MKY%2Fjq8Nrd&X-Amz-Signature=80fc49f1f21d120c6bdc2984c10923e5795d19af56a07e895927e16a3a623146&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2NPLGF4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIB63T9SNVXI6iXJb6Qa8E0xUzApkpUjG7sGkAeNxKdXYAiEAqR0LdNxwf0I7c0uhjgyFqEVUaNrpaNE6r%2FRWUV9yH%2BMq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDCAYWvEJulgXRPfdMircA0q44uqcK%2BZDD%2FsrVa9L5BD0WpY4ceSrOTPj74wyR03FMMMG5P442e5PL9PSD%2BL4qfRtkUTgwutkc3Ae66VSND6ILzxIRCwOYHuUmJGcnyPBgueK1MIQCxM%2FI7PQ3%2FGmF1HulisVoaEWF5PLaRH30ZG0RDG0awOde1%2FlS8G2GBfOmAzRFthrZVMrn95arW7W3sgQsV%2FTyFuveEOOdjwdjAV8c5JJcV2X%2FASvambGWXw12XcD5bHiIAg%2BfSSKDt7ZOZls1MdOLcQ3fsjYM2HH%2BxnzbExZmnw2h7uxrQEYc6%2FesV%2FYWKvqi8t69nTvcpTFKCIaTHA%2BghR4C3rl8fbQ%2BzxjJ4AJH1D8qKQm0%2FdroLgt1htaXTL8KdNDBHpfE8WLPzY%2F9pLepjdctLbtz6FJW8aeDLfQgt3Dr0Ddp3Th2gd6va2tjiSkWGLze5LVsbOCfkRZYcKYXLQ4Ng%2FPybWj6fopx8abnLbBqUlPmYYyLk2rc68QlLS9PmwAT5zqdrQS%2FgfM1%2FOugknYNeWTf3EWpmbylpRNJ0B%2Fks17aePgpKIKJYPuP6lFrsX6863JE%2F%2BHSUZMDikxoN5LPRvwoLAz4xn4DT6Spr3gBglMfEkGGSQYz5pDqEmgtXB5IbGjMJ7skb0GOqUB3KyalWrVmsC5QuS59hJ0I%2Fw8rOrb6UqYlGx4MIU8lpPN%2BHLGoKm%2FTejA%2FnU4wJdRf4LLNFmbIPOXUWtRTY%2FFR6RQc8jmlBCjyOshg4yLbE9F7KsBw7thgYJspXodv9fFQBjxZolVlxz0A1jK8q8mTsMfQm%2F0EHCxIVH14Yy641ci%2FONbr2Dxy3rnJM%2Be05r1jfzp%2B5Zam%2FIwZMSgk8MKY%2Fjq8Nrd&X-Amz-Signature=f2ffded3421348882a008899a56f481076ae6d295d1cbea6c7ec8d59cc4597bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2NPLGF4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIB63T9SNVXI6iXJb6Qa8E0xUzApkpUjG7sGkAeNxKdXYAiEAqR0LdNxwf0I7c0uhjgyFqEVUaNrpaNE6r%2FRWUV9yH%2BMq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDCAYWvEJulgXRPfdMircA0q44uqcK%2BZDD%2FsrVa9L5BD0WpY4ceSrOTPj74wyR03FMMMG5P442e5PL9PSD%2BL4qfRtkUTgwutkc3Ae66VSND6ILzxIRCwOYHuUmJGcnyPBgueK1MIQCxM%2FI7PQ3%2FGmF1HulisVoaEWF5PLaRH30ZG0RDG0awOde1%2FlS8G2GBfOmAzRFthrZVMrn95arW7W3sgQsV%2FTyFuveEOOdjwdjAV8c5JJcV2X%2FASvambGWXw12XcD5bHiIAg%2BfSSKDt7ZOZls1MdOLcQ3fsjYM2HH%2BxnzbExZmnw2h7uxrQEYc6%2FesV%2FYWKvqi8t69nTvcpTFKCIaTHA%2BghR4C3rl8fbQ%2BzxjJ4AJH1D8qKQm0%2FdroLgt1htaXTL8KdNDBHpfE8WLPzY%2F9pLepjdctLbtz6FJW8aeDLfQgt3Dr0Ddp3Th2gd6va2tjiSkWGLze5LVsbOCfkRZYcKYXLQ4Ng%2FPybWj6fopx8abnLbBqUlPmYYyLk2rc68QlLS9PmwAT5zqdrQS%2FgfM1%2FOugknYNeWTf3EWpmbylpRNJ0B%2Fks17aePgpKIKJYPuP6lFrsX6863JE%2F%2BHSUZMDikxoN5LPRvwoLAz4xn4DT6Spr3gBglMfEkGGSQYz5pDqEmgtXB5IbGjMJ7skb0GOqUB3KyalWrVmsC5QuS59hJ0I%2Fw8rOrb6UqYlGx4MIU8lpPN%2BHLGoKm%2FTejA%2FnU4wJdRf4LLNFmbIPOXUWtRTY%2FFR6RQc8jmlBCjyOshg4yLbE9F7KsBw7thgYJspXodv9fFQBjxZolVlxz0A1jK8q8mTsMfQm%2F0EHCxIVH14Yy641ci%2FONbr2Dxy3rnJM%2Be05r1jfzp%2B5Zam%2FIwZMSgk8MKY%2Fjq8Nrd&X-Amz-Signature=b00961134761aad319a7578f9b1aedaa5dcf7f408ba6df5e12cf281f2af582f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2NPLGF4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIB63T9SNVXI6iXJb6Qa8E0xUzApkpUjG7sGkAeNxKdXYAiEAqR0LdNxwf0I7c0uhjgyFqEVUaNrpaNE6r%2FRWUV9yH%2BMq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDCAYWvEJulgXRPfdMircA0q44uqcK%2BZDD%2FsrVa9L5BD0WpY4ceSrOTPj74wyR03FMMMG5P442e5PL9PSD%2BL4qfRtkUTgwutkc3Ae66VSND6ILzxIRCwOYHuUmJGcnyPBgueK1MIQCxM%2FI7PQ3%2FGmF1HulisVoaEWF5PLaRH30ZG0RDG0awOde1%2FlS8G2GBfOmAzRFthrZVMrn95arW7W3sgQsV%2FTyFuveEOOdjwdjAV8c5JJcV2X%2FASvambGWXw12XcD5bHiIAg%2BfSSKDt7ZOZls1MdOLcQ3fsjYM2HH%2BxnzbExZmnw2h7uxrQEYc6%2FesV%2FYWKvqi8t69nTvcpTFKCIaTHA%2BghR4C3rl8fbQ%2BzxjJ4AJH1D8qKQm0%2FdroLgt1htaXTL8KdNDBHpfE8WLPzY%2F9pLepjdctLbtz6FJW8aeDLfQgt3Dr0Ddp3Th2gd6va2tjiSkWGLze5LVsbOCfkRZYcKYXLQ4Ng%2FPybWj6fopx8abnLbBqUlPmYYyLk2rc68QlLS9PmwAT5zqdrQS%2FgfM1%2FOugknYNeWTf3EWpmbylpRNJ0B%2Fks17aePgpKIKJYPuP6lFrsX6863JE%2F%2BHSUZMDikxoN5LPRvwoLAz4xn4DT6Spr3gBglMfEkGGSQYz5pDqEmgtXB5IbGjMJ7skb0GOqUB3KyalWrVmsC5QuS59hJ0I%2Fw8rOrb6UqYlGx4MIU8lpPN%2BHLGoKm%2FTejA%2FnU4wJdRf4LLNFmbIPOXUWtRTY%2FFR6RQc8jmlBCjyOshg4yLbE9F7KsBw7thgYJspXodv9fFQBjxZolVlxz0A1jK8q8mTsMfQm%2F0EHCxIVH14Yy641ci%2FONbr2Dxy3rnJM%2Be05r1jfzp%2B5Zam%2FIwZMSgk8MKY%2Fjq8Nrd&X-Amz-Signature=89b50391c4604262fa3398d1df3dedaec6b3958c5d34c7571539984ee20a2f1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2NPLGF4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIB63T9SNVXI6iXJb6Qa8E0xUzApkpUjG7sGkAeNxKdXYAiEAqR0LdNxwf0I7c0uhjgyFqEVUaNrpaNE6r%2FRWUV9yH%2BMq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDCAYWvEJulgXRPfdMircA0q44uqcK%2BZDD%2FsrVa9L5BD0WpY4ceSrOTPj74wyR03FMMMG5P442e5PL9PSD%2BL4qfRtkUTgwutkc3Ae66VSND6ILzxIRCwOYHuUmJGcnyPBgueK1MIQCxM%2FI7PQ3%2FGmF1HulisVoaEWF5PLaRH30ZG0RDG0awOde1%2FlS8G2GBfOmAzRFthrZVMrn95arW7W3sgQsV%2FTyFuveEOOdjwdjAV8c5JJcV2X%2FASvambGWXw12XcD5bHiIAg%2BfSSKDt7ZOZls1MdOLcQ3fsjYM2HH%2BxnzbExZmnw2h7uxrQEYc6%2FesV%2FYWKvqi8t69nTvcpTFKCIaTHA%2BghR4C3rl8fbQ%2BzxjJ4AJH1D8qKQm0%2FdroLgt1htaXTL8KdNDBHpfE8WLPzY%2F9pLepjdctLbtz6FJW8aeDLfQgt3Dr0Ddp3Th2gd6va2tjiSkWGLze5LVsbOCfkRZYcKYXLQ4Ng%2FPybWj6fopx8abnLbBqUlPmYYyLk2rc68QlLS9PmwAT5zqdrQS%2FgfM1%2FOugknYNeWTf3EWpmbylpRNJ0B%2Fks17aePgpKIKJYPuP6lFrsX6863JE%2F%2BHSUZMDikxoN5LPRvwoLAz4xn4DT6Spr3gBglMfEkGGSQYz5pDqEmgtXB5IbGjMJ7skb0GOqUB3KyalWrVmsC5QuS59hJ0I%2Fw8rOrb6UqYlGx4MIU8lpPN%2BHLGoKm%2FTejA%2FnU4wJdRf4LLNFmbIPOXUWtRTY%2FFR6RQc8jmlBCjyOshg4yLbE9F7KsBw7thgYJspXodv9fFQBjxZolVlxz0A1jK8q8mTsMfQm%2F0EHCxIVH14Yy641ci%2FONbr2Dxy3rnJM%2Be05r1jfzp%2B5Zam%2FIwZMSgk8MKY%2Fjq8Nrd&X-Amz-Signature=275f3b0b9e97773453a44d066a165d53fbe09fc81e0cd05e6aa2beace9bb45a0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2NPLGF4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIB63T9SNVXI6iXJb6Qa8E0xUzApkpUjG7sGkAeNxKdXYAiEAqR0LdNxwf0I7c0uhjgyFqEVUaNrpaNE6r%2FRWUV9yH%2BMq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDCAYWvEJulgXRPfdMircA0q44uqcK%2BZDD%2FsrVa9L5BD0WpY4ceSrOTPj74wyR03FMMMG5P442e5PL9PSD%2BL4qfRtkUTgwutkc3Ae66VSND6ILzxIRCwOYHuUmJGcnyPBgueK1MIQCxM%2FI7PQ3%2FGmF1HulisVoaEWF5PLaRH30ZG0RDG0awOde1%2FlS8G2GBfOmAzRFthrZVMrn95arW7W3sgQsV%2FTyFuveEOOdjwdjAV8c5JJcV2X%2FASvambGWXw12XcD5bHiIAg%2BfSSKDt7ZOZls1MdOLcQ3fsjYM2HH%2BxnzbExZmnw2h7uxrQEYc6%2FesV%2FYWKvqi8t69nTvcpTFKCIaTHA%2BghR4C3rl8fbQ%2BzxjJ4AJH1D8qKQm0%2FdroLgt1htaXTL8KdNDBHpfE8WLPzY%2F9pLepjdctLbtz6FJW8aeDLfQgt3Dr0Ddp3Th2gd6va2tjiSkWGLze5LVsbOCfkRZYcKYXLQ4Ng%2FPybWj6fopx8abnLbBqUlPmYYyLk2rc68QlLS9PmwAT5zqdrQS%2FgfM1%2FOugknYNeWTf3EWpmbylpRNJ0B%2Fks17aePgpKIKJYPuP6lFrsX6863JE%2F%2BHSUZMDikxoN5LPRvwoLAz4xn4DT6Spr3gBglMfEkGGSQYz5pDqEmgtXB5IbGjMJ7skb0GOqUB3KyalWrVmsC5QuS59hJ0I%2Fw8rOrb6UqYlGx4MIU8lpPN%2BHLGoKm%2FTejA%2FnU4wJdRf4LLNFmbIPOXUWtRTY%2FFR6RQc8jmlBCjyOshg4yLbE9F7KsBw7thgYJspXodv9fFQBjxZolVlxz0A1jK8q8mTsMfQm%2F0EHCxIVH14Yy641ci%2FONbr2Dxy3rnJM%2Be05r1jfzp%2B5Zam%2FIwZMSgk8MKY%2Fjq8Nrd&X-Amz-Signature=acff85a81526ae72689779efd98f7d450ea58580b9c74794d37228a403840d8b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2NPLGF4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIB63T9SNVXI6iXJb6Qa8E0xUzApkpUjG7sGkAeNxKdXYAiEAqR0LdNxwf0I7c0uhjgyFqEVUaNrpaNE6r%2FRWUV9yH%2BMq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDCAYWvEJulgXRPfdMircA0q44uqcK%2BZDD%2FsrVa9L5BD0WpY4ceSrOTPj74wyR03FMMMG5P442e5PL9PSD%2BL4qfRtkUTgwutkc3Ae66VSND6ILzxIRCwOYHuUmJGcnyPBgueK1MIQCxM%2FI7PQ3%2FGmF1HulisVoaEWF5PLaRH30ZG0RDG0awOde1%2FlS8G2GBfOmAzRFthrZVMrn95arW7W3sgQsV%2FTyFuveEOOdjwdjAV8c5JJcV2X%2FASvambGWXw12XcD5bHiIAg%2BfSSKDt7ZOZls1MdOLcQ3fsjYM2HH%2BxnzbExZmnw2h7uxrQEYc6%2FesV%2FYWKvqi8t69nTvcpTFKCIaTHA%2BghR4C3rl8fbQ%2BzxjJ4AJH1D8qKQm0%2FdroLgt1htaXTL8KdNDBHpfE8WLPzY%2F9pLepjdctLbtz6FJW8aeDLfQgt3Dr0Ddp3Th2gd6va2tjiSkWGLze5LVsbOCfkRZYcKYXLQ4Ng%2FPybWj6fopx8abnLbBqUlPmYYyLk2rc68QlLS9PmwAT5zqdrQS%2FgfM1%2FOugknYNeWTf3EWpmbylpRNJ0B%2Fks17aePgpKIKJYPuP6lFrsX6863JE%2F%2BHSUZMDikxoN5LPRvwoLAz4xn4DT6Spr3gBglMfEkGGSQYz5pDqEmgtXB5IbGjMJ7skb0GOqUB3KyalWrVmsC5QuS59hJ0I%2Fw8rOrb6UqYlGx4MIU8lpPN%2BHLGoKm%2FTejA%2FnU4wJdRf4LLNFmbIPOXUWtRTY%2FFR6RQc8jmlBCjyOshg4yLbE9F7KsBw7thgYJspXodv9fFQBjxZolVlxz0A1jK8q8mTsMfQm%2F0EHCxIVH14Yy641ci%2FONbr2Dxy3rnJM%2Be05r1jfzp%2B5Zam%2FIwZMSgk8MKY%2Fjq8Nrd&X-Amz-Signature=d5d3b6895c7b281d061376e01dd9ee7d466e5b3d1c452dade0bdb33bad4d00be&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2NPLGF4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIB63T9SNVXI6iXJb6Qa8E0xUzApkpUjG7sGkAeNxKdXYAiEAqR0LdNxwf0I7c0uhjgyFqEVUaNrpaNE6r%2FRWUV9yH%2BMq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDCAYWvEJulgXRPfdMircA0q44uqcK%2BZDD%2FsrVa9L5BD0WpY4ceSrOTPj74wyR03FMMMG5P442e5PL9PSD%2BL4qfRtkUTgwutkc3Ae66VSND6ILzxIRCwOYHuUmJGcnyPBgueK1MIQCxM%2FI7PQ3%2FGmF1HulisVoaEWF5PLaRH30ZG0RDG0awOde1%2FlS8G2GBfOmAzRFthrZVMrn95arW7W3sgQsV%2FTyFuveEOOdjwdjAV8c5JJcV2X%2FASvambGWXw12XcD5bHiIAg%2BfSSKDt7ZOZls1MdOLcQ3fsjYM2HH%2BxnzbExZmnw2h7uxrQEYc6%2FesV%2FYWKvqi8t69nTvcpTFKCIaTHA%2BghR4C3rl8fbQ%2BzxjJ4AJH1D8qKQm0%2FdroLgt1htaXTL8KdNDBHpfE8WLPzY%2F9pLepjdctLbtz6FJW8aeDLfQgt3Dr0Ddp3Th2gd6va2tjiSkWGLze5LVsbOCfkRZYcKYXLQ4Ng%2FPybWj6fopx8abnLbBqUlPmYYyLk2rc68QlLS9PmwAT5zqdrQS%2FgfM1%2FOugknYNeWTf3EWpmbylpRNJ0B%2Fks17aePgpKIKJYPuP6lFrsX6863JE%2F%2BHSUZMDikxoN5LPRvwoLAz4xn4DT6Spr3gBglMfEkGGSQYz5pDqEmgtXB5IbGjMJ7skb0GOqUB3KyalWrVmsC5QuS59hJ0I%2Fw8rOrb6UqYlGx4MIU8lpPN%2BHLGoKm%2FTejA%2FnU4wJdRf4LLNFmbIPOXUWtRTY%2FFR6RQc8jmlBCjyOshg4yLbE9F7KsBw7thgYJspXodv9fFQBjxZolVlxz0A1jK8q8mTsMfQm%2F0EHCxIVH14Yy641ci%2FONbr2Dxy3rnJM%2Be05r1jfzp%2B5Zam%2FIwZMSgk8MKY%2Fjq8Nrd&X-Amz-Signature=37d5b8b393a781e893280e8be43cb2066938bed7e2b245010b850cc327f1cbe7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJ7PT2GL%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCceef4sqJvgAaU8uhuUBc6BDXtrygw3kJ7t%2FMfEXN5DAIgeXGOBAtOWbnNJUqpGJMhBB1qK4qfza3gfbpx5kzS6Kcq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDFrPa%2BAekLBf68BdJCrcA9cGvt8pyEi8llBDUO%2BXpnKwnFCzGh6DLXccVrXFrteybVTn7nenbdOaxiBoGSRvOc5PzkHTUZFfNTOIRKUTMXIHJAa9RLAAD%2B9YobXVuM7PEZd2v0rs4gEY%2F1uGk4kFU8m%2BC609k9FsR1DN%2Bka%2BCdqcYM6o7RHLUjk%2Bnw%2FB4Y8YpH1cPFEgfsSPrVuELwZMQsjlrbRsfJ7kIm1D75mZRUNyAgREdkjHB9fim%2FRith9bf53M1aYHpXyO0wobtAEzF8ajFQtGPRoaCV%2BPTPwQy8GdNATWYRgxJPg7SAU6YICNyrE6O3vgzFi7HTZ1MqsgLSRCqLzHJh3DxKXDlV1gb0VkQYWVK%2FzDCw2btOZIgBX6FiuJmSTjpciOUk2W3vldfUn0ofFnwGGyJQLZISTgzZJvykxW9Z7rl0DGHYXraqdvcsgC8tE5V7mPjRYKCjRtEKkRt4QLZ3fepl1OUnEallkj74vWfz9ZyS2ItrlS3Fdd%2Beg%2BOFujoT%2FNpfa5S2Oyy3ohM5pYtqDAyLUIQV0KC6gZJ4FTsMEf9ru%2FgXIpWT62f3etGCgnmBHIKDqXvkTP5T0NKw26f54Vt4acBEXSf6Q0cHGI%2BDmoMLhcrJdm8cQfV0a3QvqVCUpH5Y%2FKMI7skb0GOqUBqiCQOhKysk6VYJ9QN1qcDLSS4fY0aUBE0Byv0avwbwJgIPuubBrDr4h91mMVAO7rnbJSNP%2FEQC6fj5hFUM1qWls49rtLTOJcpf9Uw528PlXQtQaqgF19pwT7%2BUj3o4az08iC1q6v3UZ0O%2FaNJKhpWekaVlqjqeyvkfhDM5%2BpPI3DPYzVbxZ3PLjIVt8%2FlibU6vFaoSe4%2F%2BIynLPej3leaeIayNyq&X-Amz-Signature=8aad0afac1237b42234970d47b97ecc2e0a0b8786a6419076a51bd63c6e51275&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WROBA32P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDEQfRdX7NjEOR3hf40kex7vPN%2F13xXW2QQBDrtBS39dwIhANArBfHqARoFkkcn7KnwuH3FsEC2St3wvysn%2FDQXadIjKv8DCFoQABoMNjM3NDIzMTgzODA1IgwoYxri8rr6%2BtDgzlcq3AN4z5lgsqhSx%2BIq4ic%2F57HymQngRl41%2BymLwYNiaEIbFDSi1lLb%2BykMEKa%2F01FS8If%2FeKwWaKEaUFL1S2cEcXWS2VQt6EQePcr1sHZQxfMdngitQiUdKxULsT2EUb9hnxGmFgP9thef%2BiuCX%2FK7M2MTanVPUHOObvaHfdkrw75hJzRdYz2vP3%2F9xcBuPqrGF7wSSWzND0aQx9EtcYm8f%2BJa5xS83f479j1rL5rFALT%2B3Wi1c6f2IEx9vNOdC5ysVhOme9IyeDSwN%2FCN7FlhNYmlawu3ne9kuoYyQrY8YGXtz4CaLqk3fnrpboXamthtARAftEm20q%2F2O9Fv7qCcB9qFMzOOhcpZ1Lq2VP7VHENziLkg7Xly944CqCId%2BfDVYHxls7ZQorkwRb76mOCakuBAofcoX%2BEJ0aRuIFqzrZpU%2Btitjp%2Fdko1bcb04aKByn1eyln6LnsaH8InS%2Bq7fVU8EFI3frXVQnvRWnWDqJKyMdIBI2%2FprEp3HWg0MG1K4Y7wjk5gMW68Jq5wJRGBOyScoz2H31fWNWC45%2BucWvm1QpE8Ss4%2F9JtPrK62abw%2F2Ko4TH3nr5UkmaGZJlOJTjttLIJ4tEl9oH5DMRgl1T3EhKS9m6SerLy6UFv12aDDT65G9BjqkAaCtlsJ0C5iN5kIbDVucSsq%2Fo6DfhIs7WFXA6dJak%2BWEjZotXr1ePP2WTzI2b4%2B9sKE6Jx98Ql9KHBMwYt%2BAXK82uOCF62vyT31EU8GQYWJ7aMKPjTU5PfkLtDFs%2B2gQRQ86BazXpTnvpC9fRXYeUTrUlil4MqW%2ByLUY%2F9yQcwrgJDmEIvBgkdtoDyBcNV7gXHOTuMHoqxjGflLvxmHl6Xv%2FWRQk&X-Amz-Signature=f83096ced3d1d8848fb79a968095675ffa122f93edcb933ac61080506341a0a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSKIAVDQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIHYbCePOhhDdawY%2BP%2Fd%2Bm0Ou6nUa1psB5scYpbg1HusdAiEAiJZ8eNFA0%2B393CX8gCVLdk%2Fm1DxI92Qh83bFJiWNVu8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDAzIBM5ZT%2FOj6zETyrcA9NtrQ3A3Z5NBTTYGedcMXFjewEyu19zsk6%2BWcD6Kk8HcTi1fF6GP4ixUf%2BXK%2FWbnNqglEnbkttnJvDE8qwOSupsxE72FYySdKDHwwvlg6eUn1X1sh7oKZ2TvuuzJ7XMVNuB%2F3K74iBF5mX7gXG2sj39Wfuc2sQqWg%2BBiDlCMkqn7Gj1g0cC1Ipz0jXteIOnIUy%2BxCbGtkzeI7OGKEl2cXiOTRRRSJ%2FYosjC%2FpP71c9z%2Fww21lIhn8YKYZDR4ZOkRSRivPqzFpfoGP0BVVs%2B6NqKQgMzkZO3vmRwK5VvK%2BVFwEL%2FMBy7sYKE6wTdUXFt5zYiB6WXEfdwFOrgz7Eo4mMubsw9YQbHqFEPmvqrCHpCNRnSSoTc6BxQTGmyvV7QP56w9tEx336kKbFnofvYSSZV8PvfZFRXCbqvMReqqgxp6PY5f3acuVWLdDEYqjuSZ9z20NL7s3ewCWPvQ3ozF%2BE7eP7VJWA4d%2FZMyoVfHIIGg3IJ3YvZ4p0JTP%2BUMFHqC0mTrBfwcDv6%2BrK1Irj8iMMupD4bFxXSAf%2FsbGkPWSFvmxSrUg%2Fam93bPo0yQWNSSdpvDED2HlAnCfEXJ%2FoYimRnsHCOF%2F8%2F73ZX01jcYuyWls%2F9w8TBryKgj0vqMIXskb0GOqUBDbNr5ralBr8ZsGiDlQgqQ2abIodXf4CDdZvA87btnmw4P%2BjXEbt4q11VzIrQT9vXXfQOdyayBF9YLHlJQKAjwMEyd%2FdVz625EUUHtZB%2F9QwTaM4%2Fs9qAEjrNvBSvON8yfr%2F7d%2BilS%2F8SkXWNO276%2BWO0tcDxPp06G67yQ%2BVD1k1Vb2DnkF2UeTDD9TGagm7E9x6yXZ8wBTCt5M63YNElFHF0Z4NN&X-Amz-Signature=8be5e2aa923ec5348eab6435306f71c6423d5dbb855788bed66556365a9dfb8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSKIAVDQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIHYbCePOhhDdawY%2BP%2Fd%2Bm0Ou6nUa1psB5scYpbg1HusdAiEAiJZ8eNFA0%2B393CX8gCVLdk%2Fm1DxI92Qh83bFJiWNVu8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDAzIBM5ZT%2FOj6zETyrcA9NtrQ3A3Z5NBTTYGedcMXFjewEyu19zsk6%2BWcD6Kk8HcTi1fF6GP4ixUf%2BXK%2FWbnNqglEnbkttnJvDE8qwOSupsxE72FYySdKDHwwvlg6eUn1X1sh7oKZ2TvuuzJ7XMVNuB%2F3K74iBF5mX7gXG2sj39Wfuc2sQqWg%2BBiDlCMkqn7Gj1g0cC1Ipz0jXteIOnIUy%2BxCbGtkzeI7OGKEl2cXiOTRRRSJ%2FYosjC%2FpP71c9z%2Fww21lIhn8YKYZDR4ZOkRSRivPqzFpfoGP0BVVs%2B6NqKQgMzkZO3vmRwK5VvK%2BVFwEL%2FMBy7sYKE6wTdUXFt5zYiB6WXEfdwFOrgz7Eo4mMubsw9YQbHqFEPmvqrCHpCNRnSSoTc6BxQTGmyvV7QP56w9tEx336kKbFnofvYSSZV8PvfZFRXCbqvMReqqgxp6PY5f3acuVWLdDEYqjuSZ9z20NL7s3ewCWPvQ3ozF%2BE7eP7VJWA4d%2FZMyoVfHIIGg3IJ3YvZ4p0JTP%2BUMFHqC0mTrBfwcDv6%2BrK1Irj8iMMupD4bFxXSAf%2FsbGkPWSFvmxSrUg%2Fam93bPo0yQWNSSdpvDED2HlAnCfEXJ%2FoYimRnsHCOF%2F8%2F73ZX01jcYuyWls%2F9w8TBryKgj0vqMIXskb0GOqUBDbNr5ralBr8ZsGiDlQgqQ2abIodXf4CDdZvA87btnmw4P%2BjXEbt4q11VzIrQT9vXXfQOdyayBF9YLHlJQKAjwMEyd%2FdVz625EUUHtZB%2F9QwTaM4%2Fs9qAEjrNvBSvON8yfr%2F7d%2BilS%2F8SkXWNO276%2BWO0tcDxPp06G67yQ%2BVD1k1Vb2DnkF2UeTDD9TGagm7E9x6yXZ8wBTCt5M63YNElFHF0Z4NN&X-Amz-Signature=cef6d9e51479dc8e525fa383ceb99ce1afe4c0d6eef3b4795318c5cc07a1e78d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
