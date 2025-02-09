

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLJMLQWA%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2exJtmKM%2BA6TS8JW4LAiICFnkDk95CJFn9STrOm90mgIgQo1iL3owWjXXTG7fn5X6sSsfNMTwzcYqg5Bot5fQsL8qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtCvGDzBg1LQBZDRircAwIZJoN%2FrLUUVD5nuI15Yortf8tchzU6FL1gm6Zh%2F8YepFPOFoev8GM5uRMpCSz6GrQReLwa74yOD%2Fekqz7M30JhkzMJG482uIDDkxZfCsfhHB4K2zozhSEbSKGpUzC0Zo52tk7lb7yKgjUelnM087Sh8kEZ7mOChNAOpAknvYp5zo6jaTr8F7n1jhmQqNqVy6LrDlfK9%2B%2Fc1Z6Ac5Q4jn4eQvopJxZOKgKIGt4AYj3V7iXIdQKY3brqoo3SmuyV%2F4l96S9zVvDoG66T5X4AOwdWLLib3Z1gQY3C7a2zBroLkNOOx%2BiJy6%2BoEZp7ePqku3ZF%2FjYwUX3AUeo%2FLFw2GDeGg9caUz5diSdl9335LBA3ws97ujHMtkzWcEJ5PenAdKeUAWKcMRUV44wJHB0nRkuD0GVsX9AHi49RltVZs2J1msBaVX1xlz1ihYxBeUxWc2TNpnmlRF8VPNdka3LM7XwDoIQP1x%2Fp4pr6VuUWfcSByNISrTrhQ%2BkuEt5%2B2Jkl18mMu1ePyM8c2LyCLeKI9wAm7zeRWjVM5ScDiFHaxBVKGEFwjksK7H%2Fgz7PxVn0%2FnWHIH4uD0DgiF587CxADU8aJYTbB9obW5UG9bGVGX3SnTyiRPILFxZrCOQAkMPbWn70GOqUBLYp60WhThmJFUUjefbMSKgtnhb3v%2Fo7o26vHJG9QafWhGXCMZtLHGKKkIebmCO9DtWlFl716uRvJjWqZwikMZY8dT2bhgagb%2FFDUgOcDmBvO96GYxC%2Fl4iXFbuPXSMDAh8xMxz2OzBE5DVtw7VAoyIZ3WMs87J%2BAo%2BmJY0btms2oduqeqDHOUyPnBNaMnaDoyUzTcRNjH5D2ev2FDbZM6EFOontO&X-Amz-Signature=9d9c46432c011801f70a37a8238227331eead0cfde7c2fc6e0556553a8344af4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLJMLQWA%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2exJtmKM%2BA6TS8JW4LAiICFnkDk95CJFn9STrOm90mgIgQo1iL3owWjXXTG7fn5X6sSsfNMTwzcYqg5Bot5fQsL8qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtCvGDzBg1LQBZDRircAwIZJoN%2FrLUUVD5nuI15Yortf8tchzU6FL1gm6Zh%2F8YepFPOFoev8GM5uRMpCSz6GrQReLwa74yOD%2Fekqz7M30JhkzMJG482uIDDkxZfCsfhHB4K2zozhSEbSKGpUzC0Zo52tk7lb7yKgjUelnM087Sh8kEZ7mOChNAOpAknvYp5zo6jaTr8F7n1jhmQqNqVy6LrDlfK9%2B%2Fc1Z6Ac5Q4jn4eQvopJxZOKgKIGt4AYj3V7iXIdQKY3brqoo3SmuyV%2F4l96S9zVvDoG66T5X4AOwdWLLib3Z1gQY3C7a2zBroLkNOOx%2BiJy6%2BoEZp7ePqku3ZF%2FjYwUX3AUeo%2FLFw2GDeGg9caUz5diSdl9335LBA3ws97ujHMtkzWcEJ5PenAdKeUAWKcMRUV44wJHB0nRkuD0GVsX9AHi49RltVZs2J1msBaVX1xlz1ihYxBeUxWc2TNpnmlRF8VPNdka3LM7XwDoIQP1x%2Fp4pr6VuUWfcSByNISrTrhQ%2BkuEt5%2B2Jkl18mMu1ePyM8c2LyCLeKI9wAm7zeRWjVM5ScDiFHaxBVKGEFwjksK7H%2Fgz7PxVn0%2FnWHIH4uD0DgiF587CxADU8aJYTbB9obW5UG9bGVGX3SnTyiRPILFxZrCOQAkMPbWn70GOqUBLYp60WhThmJFUUjefbMSKgtnhb3v%2Fo7o26vHJG9QafWhGXCMZtLHGKKkIebmCO9DtWlFl716uRvJjWqZwikMZY8dT2bhgagb%2FFDUgOcDmBvO96GYxC%2Fl4iXFbuPXSMDAh8xMxz2OzBE5DVtw7VAoyIZ3WMs87J%2BAo%2BmJY0btms2oduqeqDHOUyPnBNaMnaDoyUzTcRNjH5D2ev2FDbZM6EFOontO&X-Amz-Signature=6a2946df4d22c3b023aecaa6352a3fd174ece3a5949a7ede25814646cdfe5039&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLJMLQWA%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2exJtmKM%2BA6TS8JW4LAiICFnkDk95CJFn9STrOm90mgIgQo1iL3owWjXXTG7fn5X6sSsfNMTwzcYqg5Bot5fQsL8qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtCvGDzBg1LQBZDRircAwIZJoN%2FrLUUVD5nuI15Yortf8tchzU6FL1gm6Zh%2F8YepFPOFoev8GM5uRMpCSz6GrQReLwa74yOD%2Fekqz7M30JhkzMJG482uIDDkxZfCsfhHB4K2zozhSEbSKGpUzC0Zo52tk7lb7yKgjUelnM087Sh8kEZ7mOChNAOpAknvYp5zo6jaTr8F7n1jhmQqNqVy6LrDlfK9%2B%2Fc1Z6Ac5Q4jn4eQvopJxZOKgKIGt4AYj3V7iXIdQKY3brqoo3SmuyV%2F4l96S9zVvDoG66T5X4AOwdWLLib3Z1gQY3C7a2zBroLkNOOx%2BiJy6%2BoEZp7ePqku3ZF%2FjYwUX3AUeo%2FLFw2GDeGg9caUz5diSdl9335LBA3ws97ujHMtkzWcEJ5PenAdKeUAWKcMRUV44wJHB0nRkuD0GVsX9AHi49RltVZs2J1msBaVX1xlz1ihYxBeUxWc2TNpnmlRF8VPNdka3LM7XwDoIQP1x%2Fp4pr6VuUWfcSByNISrTrhQ%2BkuEt5%2B2Jkl18mMu1ePyM8c2LyCLeKI9wAm7zeRWjVM5ScDiFHaxBVKGEFwjksK7H%2Fgz7PxVn0%2FnWHIH4uD0DgiF587CxADU8aJYTbB9obW5UG9bGVGX3SnTyiRPILFxZrCOQAkMPbWn70GOqUBLYp60WhThmJFUUjefbMSKgtnhb3v%2Fo7o26vHJG9QafWhGXCMZtLHGKKkIebmCO9DtWlFl716uRvJjWqZwikMZY8dT2bhgagb%2FFDUgOcDmBvO96GYxC%2Fl4iXFbuPXSMDAh8xMxz2OzBE5DVtw7VAoyIZ3WMs87J%2BAo%2BmJY0btms2oduqeqDHOUyPnBNaMnaDoyUzTcRNjH5D2ev2FDbZM6EFOontO&X-Amz-Signature=e036f45f3c67f38fc40ce7bd75fe8008778e66f019a478ee47b97430936c5dc7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLJMLQWA%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2exJtmKM%2BA6TS8JW4LAiICFnkDk95CJFn9STrOm90mgIgQo1iL3owWjXXTG7fn5X6sSsfNMTwzcYqg5Bot5fQsL8qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtCvGDzBg1LQBZDRircAwIZJoN%2FrLUUVD5nuI15Yortf8tchzU6FL1gm6Zh%2F8YepFPOFoev8GM5uRMpCSz6GrQReLwa74yOD%2Fekqz7M30JhkzMJG482uIDDkxZfCsfhHB4K2zozhSEbSKGpUzC0Zo52tk7lb7yKgjUelnM087Sh8kEZ7mOChNAOpAknvYp5zo6jaTr8F7n1jhmQqNqVy6LrDlfK9%2B%2Fc1Z6Ac5Q4jn4eQvopJxZOKgKIGt4AYj3V7iXIdQKY3brqoo3SmuyV%2F4l96S9zVvDoG66T5X4AOwdWLLib3Z1gQY3C7a2zBroLkNOOx%2BiJy6%2BoEZp7ePqku3ZF%2FjYwUX3AUeo%2FLFw2GDeGg9caUz5diSdl9335LBA3ws97ujHMtkzWcEJ5PenAdKeUAWKcMRUV44wJHB0nRkuD0GVsX9AHi49RltVZs2J1msBaVX1xlz1ihYxBeUxWc2TNpnmlRF8VPNdka3LM7XwDoIQP1x%2Fp4pr6VuUWfcSByNISrTrhQ%2BkuEt5%2B2Jkl18mMu1ePyM8c2LyCLeKI9wAm7zeRWjVM5ScDiFHaxBVKGEFwjksK7H%2Fgz7PxVn0%2FnWHIH4uD0DgiF587CxADU8aJYTbB9obW5UG9bGVGX3SnTyiRPILFxZrCOQAkMPbWn70GOqUBLYp60WhThmJFUUjefbMSKgtnhb3v%2Fo7o26vHJG9QafWhGXCMZtLHGKKkIebmCO9DtWlFl716uRvJjWqZwikMZY8dT2bhgagb%2FFDUgOcDmBvO96GYxC%2Fl4iXFbuPXSMDAh8xMxz2OzBE5DVtw7VAoyIZ3WMs87J%2BAo%2BmJY0btms2oduqeqDHOUyPnBNaMnaDoyUzTcRNjH5D2ev2FDbZM6EFOontO&X-Amz-Signature=615d862518eb3f1f8de09bcc821ef8c474d1b47ddc6658f0b35689a205960e4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLJMLQWA%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2exJtmKM%2BA6TS8JW4LAiICFnkDk95CJFn9STrOm90mgIgQo1iL3owWjXXTG7fn5X6sSsfNMTwzcYqg5Bot5fQsL8qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtCvGDzBg1LQBZDRircAwIZJoN%2FrLUUVD5nuI15Yortf8tchzU6FL1gm6Zh%2F8YepFPOFoev8GM5uRMpCSz6GrQReLwa74yOD%2Fekqz7M30JhkzMJG482uIDDkxZfCsfhHB4K2zozhSEbSKGpUzC0Zo52tk7lb7yKgjUelnM087Sh8kEZ7mOChNAOpAknvYp5zo6jaTr8F7n1jhmQqNqVy6LrDlfK9%2B%2Fc1Z6Ac5Q4jn4eQvopJxZOKgKIGt4AYj3V7iXIdQKY3brqoo3SmuyV%2F4l96S9zVvDoG66T5X4AOwdWLLib3Z1gQY3C7a2zBroLkNOOx%2BiJy6%2BoEZp7ePqku3ZF%2FjYwUX3AUeo%2FLFw2GDeGg9caUz5diSdl9335LBA3ws97ujHMtkzWcEJ5PenAdKeUAWKcMRUV44wJHB0nRkuD0GVsX9AHi49RltVZs2J1msBaVX1xlz1ihYxBeUxWc2TNpnmlRF8VPNdka3LM7XwDoIQP1x%2Fp4pr6VuUWfcSByNISrTrhQ%2BkuEt5%2B2Jkl18mMu1ePyM8c2LyCLeKI9wAm7zeRWjVM5ScDiFHaxBVKGEFwjksK7H%2Fgz7PxVn0%2FnWHIH4uD0DgiF587CxADU8aJYTbB9obW5UG9bGVGX3SnTyiRPILFxZrCOQAkMPbWn70GOqUBLYp60WhThmJFUUjefbMSKgtnhb3v%2Fo7o26vHJG9QafWhGXCMZtLHGKKkIebmCO9DtWlFl716uRvJjWqZwikMZY8dT2bhgagb%2FFDUgOcDmBvO96GYxC%2Fl4iXFbuPXSMDAh8xMxz2OzBE5DVtw7VAoyIZ3WMs87J%2BAo%2BmJY0btms2oduqeqDHOUyPnBNaMnaDoyUzTcRNjH5D2ev2FDbZM6EFOontO&X-Amz-Signature=33a8c26871811c44372973c6b4dd7922e19fae914776737e8795dcd8f67712cc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLJMLQWA%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2exJtmKM%2BA6TS8JW4LAiICFnkDk95CJFn9STrOm90mgIgQo1iL3owWjXXTG7fn5X6sSsfNMTwzcYqg5Bot5fQsL8qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtCvGDzBg1LQBZDRircAwIZJoN%2FrLUUVD5nuI15Yortf8tchzU6FL1gm6Zh%2F8YepFPOFoev8GM5uRMpCSz6GrQReLwa74yOD%2Fekqz7M30JhkzMJG482uIDDkxZfCsfhHB4K2zozhSEbSKGpUzC0Zo52tk7lb7yKgjUelnM087Sh8kEZ7mOChNAOpAknvYp5zo6jaTr8F7n1jhmQqNqVy6LrDlfK9%2B%2Fc1Z6Ac5Q4jn4eQvopJxZOKgKIGt4AYj3V7iXIdQKY3brqoo3SmuyV%2F4l96S9zVvDoG66T5X4AOwdWLLib3Z1gQY3C7a2zBroLkNOOx%2BiJy6%2BoEZp7ePqku3ZF%2FjYwUX3AUeo%2FLFw2GDeGg9caUz5diSdl9335LBA3ws97ujHMtkzWcEJ5PenAdKeUAWKcMRUV44wJHB0nRkuD0GVsX9AHi49RltVZs2J1msBaVX1xlz1ihYxBeUxWc2TNpnmlRF8VPNdka3LM7XwDoIQP1x%2Fp4pr6VuUWfcSByNISrTrhQ%2BkuEt5%2B2Jkl18mMu1ePyM8c2LyCLeKI9wAm7zeRWjVM5ScDiFHaxBVKGEFwjksK7H%2Fgz7PxVn0%2FnWHIH4uD0DgiF587CxADU8aJYTbB9obW5UG9bGVGX3SnTyiRPILFxZrCOQAkMPbWn70GOqUBLYp60WhThmJFUUjefbMSKgtnhb3v%2Fo7o26vHJG9QafWhGXCMZtLHGKKkIebmCO9DtWlFl716uRvJjWqZwikMZY8dT2bhgagb%2FFDUgOcDmBvO96GYxC%2Fl4iXFbuPXSMDAh8xMxz2OzBE5DVtw7VAoyIZ3WMs87J%2BAo%2BmJY0btms2oduqeqDHOUyPnBNaMnaDoyUzTcRNjH5D2ev2FDbZM6EFOontO&X-Amz-Signature=54f773919e0f0e0b858ce0b13e7293a5ef1b3e2989c581f8215402d9c39cc25a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLJMLQWA%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2exJtmKM%2BA6TS8JW4LAiICFnkDk95CJFn9STrOm90mgIgQo1iL3owWjXXTG7fn5X6sSsfNMTwzcYqg5Bot5fQsL8qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtCvGDzBg1LQBZDRircAwIZJoN%2FrLUUVD5nuI15Yortf8tchzU6FL1gm6Zh%2F8YepFPOFoev8GM5uRMpCSz6GrQReLwa74yOD%2Fekqz7M30JhkzMJG482uIDDkxZfCsfhHB4K2zozhSEbSKGpUzC0Zo52tk7lb7yKgjUelnM087Sh8kEZ7mOChNAOpAknvYp5zo6jaTr8F7n1jhmQqNqVy6LrDlfK9%2B%2Fc1Z6Ac5Q4jn4eQvopJxZOKgKIGt4AYj3V7iXIdQKY3brqoo3SmuyV%2F4l96S9zVvDoG66T5X4AOwdWLLib3Z1gQY3C7a2zBroLkNOOx%2BiJy6%2BoEZp7ePqku3ZF%2FjYwUX3AUeo%2FLFw2GDeGg9caUz5diSdl9335LBA3ws97ujHMtkzWcEJ5PenAdKeUAWKcMRUV44wJHB0nRkuD0GVsX9AHi49RltVZs2J1msBaVX1xlz1ihYxBeUxWc2TNpnmlRF8VPNdka3LM7XwDoIQP1x%2Fp4pr6VuUWfcSByNISrTrhQ%2BkuEt5%2B2Jkl18mMu1ePyM8c2LyCLeKI9wAm7zeRWjVM5ScDiFHaxBVKGEFwjksK7H%2Fgz7PxVn0%2FnWHIH4uD0DgiF587CxADU8aJYTbB9obW5UG9bGVGX3SnTyiRPILFxZrCOQAkMPbWn70GOqUBLYp60WhThmJFUUjefbMSKgtnhb3v%2Fo7o26vHJG9QafWhGXCMZtLHGKKkIebmCO9DtWlFl716uRvJjWqZwikMZY8dT2bhgagb%2FFDUgOcDmBvO96GYxC%2Fl4iXFbuPXSMDAh8xMxz2OzBE5DVtw7VAoyIZ3WMs87J%2BAo%2BmJY0btms2oduqeqDHOUyPnBNaMnaDoyUzTcRNjH5D2ev2FDbZM6EFOontO&X-Amz-Signature=5560b12a1c6aa5bb63324354db183429da141415bceb4189b4636e71a66a2a6c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLJMLQWA%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2exJtmKM%2BA6TS8JW4LAiICFnkDk95CJFn9STrOm90mgIgQo1iL3owWjXXTG7fn5X6sSsfNMTwzcYqg5Bot5fQsL8qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtCvGDzBg1LQBZDRircAwIZJoN%2FrLUUVD5nuI15Yortf8tchzU6FL1gm6Zh%2F8YepFPOFoev8GM5uRMpCSz6GrQReLwa74yOD%2Fekqz7M30JhkzMJG482uIDDkxZfCsfhHB4K2zozhSEbSKGpUzC0Zo52tk7lb7yKgjUelnM087Sh8kEZ7mOChNAOpAknvYp5zo6jaTr8F7n1jhmQqNqVy6LrDlfK9%2B%2Fc1Z6Ac5Q4jn4eQvopJxZOKgKIGt4AYj3V7iXIdQKY3brqoo3SmuyV%2F4l96S9zVvDoG66T5X4AOwdWLLib3Z1gQY3C7a2zBroLkNOOx%2BiJy6%2BoEZp7ePqku3ZF%2FjYwUX3AUeo%2FLFw2GDeGg9caUz5diSdl9335LBA3ws97ujHMtkzWcEJ5PenAdKeUAWKcMRUV44wJHB0nRkuD0GVsX9AHi49RltVZs2J1msBaVX1xlz1ihYxBeUxWc2TNpnmlRF8VPNdka3LM7XwDoIQP1x%2Fp4pr6VuUWfcSByNISrTrhQ%2BkuEt5%2B2Jkl18mMu1ePyM8c2LyCLeKI9wAm7zeRWjVM5ScDiFHaxBVKGEFwjksK7H%2Fgz7PxVn0%2FnWHIH4uD0DgiF587CxADU8aJYTbB9obW5UG9bGVGX3SnTyiRPILFxZrCOQAkMPbWn70GOqUBLYp60WhThmJFUUjefbMSKgtnhb3v%2Fo7o26vHJG9QafWhGXCMZtLHGKKkIebmCO9DtWlFl716uRvJjWqZwikMZY8dT2bhgagb%2FFDUgOcDmBvO96GYxC%2Fl4iXFbuPXSMDAh8xMxz2OzBE5DVtw7VAoyIZ3WMs87J%2BAo%2BmJY0btms2oduqeqDHOUyPnBNaMnaDoyUzTcRNjH5D2ev2FDbZM6EFOontO&X-Amz-Signature=a48f96ea671217af1aa402432fe44e3742890693ff3ecdffa85c293329e1e7fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HOZCEKP%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVIRpv0R4%2FeHOS2uHoDw%2FnfcalLq93VBCF8iVvt8fqbwIgKMalTKDaeENrIDbI885vufn704r8OkyIXw3uOB5Oya8qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCx9Jb9sG1Kalcg4pSrcAzqRkYAxaXTIb5kN7q%2FFgY%2FYAqq%2FtF19zFhf5w1hH%2FSNwk4yejs0k6%2BDUe9sCh0bR2203Wme21hrxELgX5wVQTx5QVQvTaE2JkaYRvTqcgJx9MRHrJ1drvyk6%2BjdtT8EL4rrNfiBm7iYPqzE2HTvIqZj8E5rSI8MVxC2WO2aSLB3D5MCPpyODGa5kBbSjygdLWzqNEGiRk%2BLYl32EDJw9pogw7McBEH9cOk4NDns6vAmoIbyczlx6Yx5yRiWYj7aUveIUMIh5gDS60Y4ScShjptNQBGq6IIBkgfMkEyn12Ep%2BhZ5ryfMrM6j0j1jFrsqz6tqfOA3%2FO4QNUZc0eVX21%2FvEdIb4dVlavW2igmX7oSBEnSOJhlZcimtRcCzTbCo27AKXIkDiC5pW%2FN174RD7lHlk1AFgl98SjUcvHwI52UCE1E1dhwld95rNEstq097hWhnEQ78BsgqwnlAHIRWQuAnjFObj1zRMWv5Z9r%2F%2FEb3jIXVMpebf%2FJR4HzJP%2FckcpD49okYNQZpn0xoov5smIBnxaK5fRgYtrmbm1cRvuOPJ8T30jm15eDeTplAqDR5I5xu%2BuM9zKrCjHNAvpj0%2F3Z76J9CbGJCro0C71LGu7tILUVbfQrPLy88TwyCMIvXn70GOqUBCAmd%2BtJO%2BdsiOr6JxIWPjqDFnv3ARO0CFlD%2BXDN%2Bk%2BRkil7pzADAkwv7ScasSyCpv2KPMVxzhjGuSW%2FO%2B1CCt4VWIinDDZyPziZr%2F8cLaYyJoPg5yeDYEIaaLPqN9GLjw9xtb5JP6kVGnOT0tb%2FJ5GkwZOKE3l21ZY5B%2BXolEs%2BXcbH1fOIU3BaJuLt3FvIKr0h5Z6T%2F0SbaNhr7BsaV%2FoQaNfqa&X-Amz-Signature=ca21bd99cabd74795fcbea7cc25ab404bd410da841bbe4f82878cfc944ac8786&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AVZ7QXQ%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0u4QI4Yyl%2Fq8l37y5L1LMg7MZRiSPXGJOUIsENLYLxQIgSLKZn50%2FfcG4I3YMk5a1tcRfrdd11QIwrYoYmD9NxVgqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOXZrUZtxwXxFKVyMircA5rfJbI07i7rEuurkX%2Bjl715T4OwSoD%2FYLIAnPmwUHWYAiz6R2ZjCN16AYd7yuK8npdlD4xO3Lj5cDUBN%2BJfaaIYVmGXtDeYr7J9%2FM%2FzEfU%2B7oqZKXn06rqK6I4%2BftM9vxp9v%2BqP9%2BOMf0gtiv4s16JCe1ocLkd3X963MoRSSmjedGO59lIwUQHC95K%2FAGP6eIoJ%2FFq8sGgX78%2F9ueWbUhFZQIkgGDbdHaqZzlNH5jXNt1UR1rNPGK2qRiMqoaon3s%2BMlZ9r7HOKtjDOBsZcEaf4sIhCKyzb2%2FRXDsdvxixXuFarNAcUFL967uH9rIzuuhBngt7MeJw%2BlHnTVpDmY1iBrqswZXkyr7z1R%2Bx%2BL4lYGbtAseYQYrR3PYL7sII76JMsqkiL9wYVh7N2CN5zeTzNlXZHkvD0HKniuwWf2X5gq57Mm8VPhTS8uWi97P2AoGEsSG7gmBhyDHj3oU73eAhztHOTNAbTnCAiKewDZuRpDibJmnC7KO2ftmFI0pbbRyUo9WZ5%2BmjHQFWiIxVIv4U9um5UkCABM4xPZHx4woBOglaxY16ca%2FEUVlfFoEtxxMBmJYekq76RGPRhToPu5TpOBH%2BJ9j2uGB0VXx%2FEvV1070alp2uyteRXOII7MN%2FWn70GOqUBm0nWr%2FhViY9BVcQZY8p8AUaILMizoAp%2FMndqCeQkVJ0P1m8irBBOhea%2BxgHT89EycoSdjb88cJvEo%2FnOpw2sLf9EB35%2FYIIEn5K4fyX1mMIPpIonJlcLGgQzCELv485tNA8%2BaK3pvLHM5tYvlrjns7ZVL9NZzsqtHvoKCz3e5xk9ooxR%2B%2FtiI%2F%2BmQGRxFPkc8lF97FSrDhP8yqcwNyfk0YxHj4U1&X-Amz-Signature=71dd515eaef1edea5b2989a2bd97a7bb873f463340c77eaad82fc61bcf59ac07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSJXDSDM%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICKfcNjkYsu0uDmKAQWQxxWtedNs3dxpwQO%2Bc8%2BV6aVNAiEA3838sdNEqvu%2FvpvZAT%2FwE8tdp4t%2BD27khTTFvo%2B5RH8qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPC8NIWTaSn%2B3B4eZSrcA4hvwLA0YFt9jJp4a3wNP28JbHc7WClIoBrHSD2kNrjMDs7kOvl%2F0kMnw%2FjDWoh9%2FT91wKVfkOuDJkl4AkNjZoVM7XcJ%2BLdKLwHO9mD0Nxu1ud%2Fhg6BKejpZPpB6XE9ZpnAlPutCXoai%2F6SQ9NAb%2BsDBbS150AmsKPb6nEfTZTtRcOjBWvbPbh1wuTnSO9P%2FzrnZpwfu8PNazDy%2ByjVWOmh6xqla0GTqO3Tw4rN6Eegj6D6ARuRTOdwY71EPTDXHI4Ej54jJ8aa1WFJ63IzDpzb2wHnooEBg0HIqjWPvPOfiYUfN0b%2F7qIFrqX3i3rtvC3784QKtYBXzxcoy7VssczfZLhvvgnQZY4cl%2B6IqYDmnRltBdOAqk4Hi1P94tDR9AjH%2BkFtzoT%2B4dNIuoTox%2FGSAzZqbTtXfT5vetuItKDQXeOafScZ5CkrEtgOhuwIxaCA1Q6wQ10TJ0hOzr%2F%2BujsX%2FyWPFYfXD0YvMc8Oj4iGuYQEEO5Lz4INQMaV147V8wNy4hK0ngoS3GTrDSo1%2FDJfGawXeBF0z2mMtD9FmpEvy%2B25pc6lStP06Dls9JypN%2FuRhDn1PJ7OOo6WOZ6%2B8r%2F%2F%2BZ5oBnkD5R7%2Bb6WvraYbcKKQ5OOZ3VfZ5XwSAMLLWn70GOqUBAn2ye8krwkSvMB7MM%2FAs6Qm6AtwKn1eYuTagWQTSJOv430O%2FXol9v6hht67R1%2BEMb3PDUbXt9Bk4VsRvt53nq3eqZsI4rAWyFfETeSeBYbb8Nxt2whp4ajYl4UGCPB%2BleYyfGf3UK%2Fzoc%2BCKnxYoEjf4nWfcyK3VbB47Nt%2FXqv2Gtrul0UQx0akQa205DQcXf9PUx1YaAeR1mK46M1APZp0bPn%2FK&X-Amz-Signature=123705318a71d0fa84052f13a07343c3ba8ee599b534dc128d568318ba01a493&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSJXDSDM%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICKfcNjkYsu0uDmKAQWQxxWtedNs3dxpwQO%2Bc8%2BV6aVNAiEA3838sdNEqvu%2FvpvZAT%2FwE8tdp4t%2BD27khTTFvo%2B5RH8qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPC8NIWTaSn%2B3B4eZSrcA4hvwLA0YFt9jJp4a3wNP28JbHc7WClIoBrHSD2kNrjMDs7kOvl%2F0kMnw%2FjDWoh9%2FT91wKVfkOuDJkl4AkNjZoVM7XcJ%2BLdKLwHO9mD0Nxu1ud%2Fhg6BKejpZPpB6XE9ZpnAlPutCXoai%2F6SQ9NAb%2BsDBbS150AmsKPb6nEfTZTtRcOjBWvbPbh1wuTnSO9P%2FzrnZpwfu8PNazDy%2ByjVWOmh6xqla0GTqO3Tw4rN6Eegj6D6ARuRTOdwY71EPTDXHI4Ej54jJ8aa1WFJ63IzDpzb2wHnooEBg0HIqjWPvPOfiYUfN0b%2F7qIFrqX3i3rtvC3784QKtYBXzxcoy7VssczfZLhvvgnQZY4cl%2B6IqYDmnRltBdOAqk4Hi1P94tDR9AjH%2BkFtzoT%2B4dNIuoTox%2FGSAzZqbTtXfT5vetuItKDQXeOafScZ5CkrEtgOhuwIxaCA1Q6wQ10TJ0hOzr%2F%2BujsX%2FyWPFYfXD0YvMc8Oj4iGuYQEEO5Lz4INQMaV147V8wNy4hK0ngoS3GTrDSo1%2FDJfGawXeBF0z2mMtD9FmpEvy%2B25pc6lStP06Dls9JypN%2FuRhDn1PJ7OOo6WOZ6%2B8r%2F%2F%2BZ5oBnkD5R7%2Bb6WvraYbcKKQ5OOZ3VfZ5XwSAMLLWn70GOqUBAn2ye8krwkSvMB7MM%2FAs6Qm6AtwKn1eYuTagWQTSJOv430O%2FXol9v6hht67R1%2BEMb3PDUbXt9Bk4VsRvt53nq3eqZsI4rAWyFfETeSeBYbb8Nxt2whp4ajYl4UGCPB%2BleYyfGf3UK%2Fzoc%2BCKnxYoEjf4nWfcyK3VbB47Nt%2FXqv2Gtrul0UQx0akQa205DQcXf9PUx1YaAeR1mK46M1APZp0bPn%2FK&X-Amz-Signature=daf51a751baa1fc77f1ef82a0b097c95b66330e04f3c048b0599fc47b670b995&X-Amz-SignedHeaders=host&x-id=GetObject)
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
