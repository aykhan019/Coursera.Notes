

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPH4THXA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD0DJpI8BUHVGF5Xb8Akpm6wM7xzzvlzxK4YVfXn0e7hwIhANdpiSpLV0qjjx7lOzWwcOrfMGHFOBf96kNA3hj1N3m%2FKv8DCEQQABoMNjM3NDIzMTgzODA1IgyrrIGnYvZu9Bhz7w0q3APqVdErxDRGZ6KoIDGb%2FjkHrkzBzidDb46xZ0hn2RmfHMGG8d9g0axH05o5%2BMta734y3vvKqthV8BiA%2BkPNtEQmddpqlxsQwfrOSO76OV2gOKDDAwDbLiGe2uSyUDRhEb%2FFY8A%2FQDxGn21VCT7cUSFk1jvw7RaV9dUSPiqH37bJ%2FBydTDPXboDvn6%2F3ZYW6foMjYq%2BUzGDf1HH7N5040wfOXKJjGdPdlu9SSeFyAISb3TXc%2BtrdcnQ2DfvpRDCE7%2BoTPgFT2nYS%2BROFZtLsq31beaelk5tI3evHvq35D54Q5zzqZHcASgTyNEOY68YuDR1ZeuAxyDWvlAFgXyi0e38EXt3fRO4IyXmsHRNfAKeZYjDcNZzuo%2F2%2FEvXmVSDMePwXBcA8h8VjAQWGsxQkocCvkXZOKuC2r992cZylrX7HIUlrFaKCcZRHy%2FdqGDJ%2FCZ7hPGohZjO7GY9%2BGTcorma9Un9m%2FdNxktJIUxRHzIl5rFPBjlOPoeYQF2rSgVEMYTBhGfsrzUpzV89S8ytyDapK6x5bvRnf1WWTcOZjMI4weRotDDnjmo6LKQVUHjCGuRV1X7FTgCP%2B2bWKPId%2BRTUiiIA4cgAkEdUJWdJbaz3yPMKxYq%2FHYIv%2F47%2FyxDCfi429BjqkAeVMCAMVOjf4De60%2FoIO1QRdJHo21MR4o5iIS6FErHKLRjvSzq%2BagNjwaRMz2FIv2aHKaV26N1ML2fof7qNorDL88EursL0x0SDPMWLSfOV4dtFrRonjORCP8ri8iZLZOaefsN1NbRGw6Xbz1vJXr4eTPcNl%2BcZaIcNoYS%2F830KrQHkbBFNo4GtzCkWmZzo8ZPmSsp9keALoSvuSXOqZWw4CRCN4&X-Amz-Signature=ea39011d4d93493c861d285c867908585473408078257a70be9eac62c991516b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPH4THXA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD0DJpI8BUHVGF5Xb8Akpm6wM7xzzvlzxK4YVfXn0e7hwIhANdpiSpLV0qjjx7lOzWwcOrfMGHFOBf96kNA3hj1N3m%2FKv8DCEQQABoMNjM3NDIzMTgzODA1IgyrrIGnYvZu9Bhz7w0q3APqVdErxDRGZ6KoIDGb%2FjkHrkzBzidDb46xZ0hn2RmfHMGG8d9g0axH05o5%2BMta734y3vvKqthV8BiA%2BkPNtEQmddpqlxsQwfrOSO76OV2gOKDDAwDbLiGe2uSyUDRhEb%2FFY8A%2FQDxGn21VCT7cUSFk1jvw7RaV9dUSPiqH37bJ%2FBydTDPXboDvn6%2F3ZYW6foMjYq%2BUzGDf1HH7N5040wfOXKJjGdPdlu9SSeFyAISb3TXc%2BtrdcnQ2DfvpRDCE7%2BoTPgFT2nYS%2BROFZtLsq31beaelk5tI3evHvq35D54Q5zzqZHcASgTyNEOY68YuDR1ZeuAxyDWvlAFgXyi0e38EXt3fRO4IyXmsHRNfAKeZYjDcNZzuo%2F2%2FEvXmVSDMePwXBcA8h8VjAQWGsxQkocCvkXZOKuC2r992cZylrX7HIUlrFaKCcZRHy%2FdqGDJ%2FCZ7hPGohZjO7GY9%2BGTcorma9Un9m%2FdNxktJIUxRHzIl5rFPBjlOPoeYQF2rSgVEMYTBhGfsrzUpzV89S8ytyDapK6x5bvRnf1WWTcOZjMI4weRotDDnjmo6LKQVUHjCGuRV1X7FTgCP%2B2bWKPId%2BRTUiiIA4cgAkEdUJWdJbaz3yPMKxYq%2FHYIv%2F47%2FyxDCfi429BjqkAeVMCAMVOjf4De60%2FoIO1QRdJHo21MR4o5iIS6FErHKLRjvSzq%2BagNjwaRMz2FIv2aHKaV26N1ML2fof7qNorDL88EursL0x0SDPMWLSfOV4dtFrRonjORCP8ri8iZLZOaefsN1NbRGw6Xbz1vJXr4eTPcNl%2BcZaIcNoYS%2F830KrQHkbBFNo4GtzCkWmZzo8ZPmSsp9keALoSvuSXOqZWw4CRCN4&X-Amz-Signature=9d15bc09ef27852fccd3df1125aaf5eb1c616623e99bc7b7a4cfcc30ee65efa2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPH4THXA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD0DJpI8BUHVGF5Xb8Akpm6wM7xzzvlzxK4YVfXn0e7hwIhANdpiSpLV0qjjx7lOzWwcOrfMGHFOBf96kNA3hj1N3m%2FKv8DCEQQABoMNjM3NDIzMTgzODA1IgyrrIGnYvZu9Bhz7w0q3APqVdErxDRGZ6KoIDGb%2FjkHrkzBzidDb46xZ0hn2RmfHMGG8d9g0axH05o5%2BMta734y3vvKqthV8BiA%2BkPNtEQmddpqlxsQwfrOSO76OV2gOKDDAwDbLiGe2uSyUDRhEb%2FFY8A%2FQDxGn21VCT7cUSFk1jvw7RaV9dUSPiqH37bJ%2FBydTDPXboDvn6%2F3ZYW6foMjYq%2BUzGDf1HH7N5040wfOXKJjGdPdlu9SSeFyAISb3TXc%2BtrdcnQ2DfvpRDCE7%2BoTPgFT2nYS%2BROFZtLsq31beaelk5tI3evHvq35D54Q5zzqZHcASgTyNEOY68YuDR1ZeuAxyDWvlAFgXyi0e38EXt3fRO4IyXmsHRNfAKeZYjDcNZzuo%2F2%2FEvXmVSDMePwXBcA8h8VjAQWGsxQkocCvkXZOKuC2r992cZylrX7HIUlrFaKCcZRHy%2FdqGDJ%2FCZ7hPGohZjO7GY9%2BGTcorma9Un9m%2FdNxktJIUxRHzIl5rFPBjlOPoeYQF2rSgVEMYTBhGfsrzUpzV89S8ytyDapK6x5bvRnf1WWTcOZjMI4weRotDDnjmo6LKQVUHjCGuRV1X7FTgCP%2B2bWKPId%2BRTUiiIA4cgAkEdUJWdJbaz3yPMKxYq%2FHYIv%2F47%2FyxDCfi429BjqkAeVMCAMVOjf4De60%2FoIO1QRdJHo21MR4o5iIS6FErHKLRjvSzq%2BagNjwaRMz2FIv2aHKaV26N1ML2fof7qNorDL88EursL0x0SDPMWLSfOV4dtFrRonjORCP8ri8iZLZOaefsN1NbRGw6Xbz1vJXr4eTPcNl%2BcZaIcNoYS%2F830KrQHkbBFNo4GtzCkWmZzo8ZPmSsp9keALoSvuSXOqZWw4CRCN4&X-Amz-Signature=dd49bf599f0071dd0614120b6458349ec62558f92581c93c809ddbb88db17019&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPH4THXA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD0DJpI8BUHVGF5Xb8Akpm6wM7xzzvlzxK4YVfXn0e7hwIhANdpiSpLV0qjjx7lOzWwcOrfMGHFOBf96kNA3hj1N3m%2FKv8DCEQQABoMNjM3NDIzMTgzODA1IgyrrIGnYvZu9Bhz7w0q3APqVdErxDRGZ6KoIDGb%2FjkHrkzBzidDb46xZ0hn2RmfHMGG8d9g0axH05o5%2BMta734y3vvKqthV8BiA%2BkPNtEQmddpqlxsQwfrOSO76OV2gOKDDAwDbLiGe2uSyUDRhEb%2FFY8A%2FQDxGn21VCT7cUSFk1jvw7RaV9dUSPiqH37bJ%2FBydTDPXboDvn6%2F3ZYW6foMjYq%2BUzGDf1HH7N5040wfOXKJjGdPdlu9SSeFyAISb3TXc%2BtrdcnQ2DfvpRDCE7%2BoTPgFT2nYS%2BROFZtLsq31beaelk5tI3evHvq35D54Q5zzqZHcASgTyNEOY68YuDR1ZeuAxyDWvlAFgXyi0e38EXt3fRO4IyXmsHRNfAKeZYjDcNZzuo%2F2%2FEvXmVSDMePwXBcA8h8VjAQWGsxQkocCvkXZOKuC2r992cZylrX7HIUlrFaKCcZRHy%2FdqGDJ%2FCZ7hPGohZjO7GY9%2BGTcorma9Un9m%2FdNxktJIUxRHzIl5rFPBjlOPoeYQF2rSgVEMYTBhGfsrzUpzV89S8ytyDapK6x5bvRnf1WWTcOZjMI4weRotDDnjmo6LKQVUHjCGuRV1X7FTgCP%2B2bWKPId%2BRTUiiIA4cgAkEdUJWdJbaz3yPMKxYq%2FHYIv%2F47%2FyxDCfi429BjqkAeVMCAMVOjf4De60%2FoIO1QRdJHo21MR4o5iIS6FErHKLRjvSzq%2BagNjwaRMz2FIv2aHKaV26N1ML2fof7qNorDL88EursL0x0SDPMWLSfOV4dtFrRonjORCP8ri8iZLZOaefsN1NbRGw6Xbz1vJXr4eTPcNl%2BcZaIcNoYS%2F830KrQHkbBFNo4GtzCkWmZzo8ZPmSsp9keALoSvuSXOqZWw4CRCN4&X-Amz-Signature=4e0fff65038ee29319d6ce29e6e68ec7434a8134448c389b435297889b8f168d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPH4THXA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD0DJpI8BUHVGF5Xb8Akpm6wM7xzzvlzxK4YVfXn0e7hwIhANdpiSpLV0qjjx7lOzWwcOrfMGHFOBf96kNA3hj1N3m%2FKv8DCEQQABoMNjM3NDIzMTgzODA1IgyrrIGnYvZu9Bhz7w0q3APqVdErxDRGZ6KoIDGb%2FjkHrkzBzidDb46xZ0hn2RmfHMGG8d9g0axH05o5%2BMta734y3vvKqthV8BiA%2BkPNtEQmddpqlxsQwfrOSO76OV2gOKDDAwDbLiGe2uSyUDRhEb%2FFY8A%2FQDxGn21VCT7cUSFk1jvw7RaV9dUSPiqH37bJ%2FBydTDPXboDvn6%2F3ZYW6foMjYq%2BUzGDf1HH7N5040wfOXKJjGdPdlu9SSeFyAISb3TXc%2BtrdcnQ2DfvpRDCE7%2BoTPgFT2nYS%2BROFZtLsq31beaelk5tI3evHvq35D54Q5zzqZHcASgTyNEOY68YuDR1ZeuAxyDWvlAFgXyi0e38EXt3fRO4IyXmsHRNfAKeZYjDcNZzuo%2F2%2FEvXmVSDMePwXBcA8h8VjAQWGsxQkocCvkXZOKuC2r992cZylrX7HIUlrFaKCcZRHy%2FdqGDJ%2FCZ7hPGohZjO7GY9%2BGTcorma9Un9m%2FdNxktJIUxRHzIl5rFPBjlOPoeYQF2rSgVEMYTBhGfsrzUpzV89S8ytyDapK6x5bvRnf1WWTcOZjMI4weRotDDnjmo6LKQVUHjCGuRV1X7FTgCP%2B2bWKPId%2BRTUiiIA4cgAkEdUJWdJbaz3yPMKxYq%2FHYIv%2F47%2FyxDCfi429BjqkAeVMCAMVOjf4De60%2FoIO1QRdJHo21MR4o5iIS6FErHKLRjvSzq%2BagNjwaRMz2FIv2aHKaV26N1ML2fof7qNorDL88EursL0x0SDPMWLSfOV4dtFrRonjORCP8ri8iZLZOaefsN1NbRGw6Xbz1vJXr4eTPcNl%2BcZaIcNoYS%2F830KrQHkbBFNo4GtzCkWmZzo8ZPmSsp9keALoSvuSXOqZWw4CRCN4&X-Amz-Signature=5cc702d7a572c09e514d5cf835ac42df1d11ce5f52fcdef02bd38cf10f8a7eb6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPH4THXA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD0DJpI8BUHVGF5Xb8Akpm6wM7xzzvlzxK4YVfXn0e7hwIhANdpiSpLV0qjjx7lOzWwcOrfMGHFOBf96kNA3hj1N3m%2FKv8DCEQQABoMNjM3NDIzMTgzODA1IgyrrIGnYvZu9Bhz7w0q3APqVdErxDRGZ6KoIDGb%2FjkHrkzBzidDb46xZ0hn2RmfHMGG8d9g0axH05o5%2BMta734y3vvKqthV8BiA%2BkPNtEQmddpqlxsQwfrOSO76OV2gOKDDAwDbLiGe2uSyUDRhEb%2FFY8A%2FQDxGn21VCT7cUSFk1jvw7RaV9dUSPiqH37bJ%2FBydTDPXboDvn6%2F3ZYW6foMjYq%2BUzGDf1HH7N5040wfOXKJjGdPdlu9SSeFyAISb3TXc%2BtrdcnQ2DfvpRDCE7%2BoTPgFT2nYS%2BROFZtLsq31beaelk5tI3evHvq35D54Q5zzqZHcASgTyNEOY68YuDR1ZeuAxyDWvlAFgXyi0e38EXt3fRO4IyXmsHRNfAKeZYjDcNZzuo%2F2%2FEvXmVSDMePwXBcA8h8VjAQWGsxQkocCvkXZOKuC2r992cZylrX7HIUlrFaKCcZRHy%2FdqGDJ%2FCZ7hPGohZjO7GY9%2BGTcorma9Un9m%2FdNxktJIUxRHzIl5rFPBjlOPoeYQF2rSgVEMYTBhGfsrzUpzV89S8ytyDapK6x5bvRnf1WWTcOZjMI4weRotDDnjmo6LKQVUHjCGuRV1X7FTgCP%2B2bWKPId%2BRTUiiIA4cgAkEdUJWdJbaz3yPMKxYq%2FHYIv%2F47%2FyxDCfi429BjqkAeVMCAMVOjf4De60%2FoIO1QRdJHo21MR4o5iIS6FErHKLRjvSzq%2BagNjwaRMz2FIv2aHKaV26N1ML2fof7qNorDL88EursL0x0SDPMWLSfOV4dtFrRonjORCP8ri8iZLZOaefsN1NbRGw6Xbz1vJXr4eTPcNl%2BcZaIcNoYS%2F830KrQHkbBFNo4GtzCkWmZzo8ZPmSsp9keALoSvuSXOqZWw4CRCN4&X-Amz-Signature=031f082b6252460041d3bd857adde346fa621e0c10c9ec1945026396c344c064&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPH4THXA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD0DJpI8BUHVGF5Xb8Akpm6wM7xzzvlzxK4YVfXn0e7hwIhANdpiSpLV0qjjx7lOzWwcOrfMGHFOBf96kNA3hj1N3m%2FKv8DCEQQABoMNjM3NDIzMTgzODA1IgyrrIGnYvZu9Bhz7w0q3APqVdErxDRGZ6KoIDGb%2FjkHrkzBzidDb46xZ0hn2RmfHMGG8d9g0axH05o5%2BMta734y3vvKqthV8BiA%2BkPNtEQmddpqlxsQwfrOSO76OV2gOKDDAwDbLiGe2uSyUDRhEb%2FFY8A%2FQDxGn21VCT7cUSFk1jvw7RaV9dUSPiqH37bJ%2FBydTDPXboDvn6%2F3ZYW6foMjYq%2BUzGDf1HH7N5040wfOXKJjGdPdlu9SSeFyAISb3TXc%2BtrdcnQ2DfvpRDCE7%2BoTPgFT2nYS%2BROFZtLsq31beaelk5tI3evHvq35D54Q5zzqZHcASgTyNEOY68YuDR1ZeuAxyDWvlAFgXyi0e38EXt3fRO4IyXmsHRNfAKeZYjDcNZzuo%2F2%2FEvXmVSDMePwXBcA8h8VjAQWGsxQkocCvkXZOKuC2r992cZylrX7HIUlrFaKCcZRHy%2FdqGDJ%2FCZ7hPGohZjO7GY9%2BGTcorma9Un9m%2FdNxktJIUxRHzIl5rFPBjlOPoeYQF2rSgVEMYTBhGfsrzUpzV89S8ytyDapK6x5bvRnf1WWTcOZjMI4weRotDDnjmo6LKQVUHjCGuRV1X7FTgCP%2B2bWKPId%2BRTUiiIA4cgAkEdUJWdJbaz3yPMKxYq%2FHYIv%2F47%2FyxDCfi429BjqkAeVMCAMVOjf4De60%2FoIO1QRdJHo21MR4o5iIS6FErHKLRjvSzq%2BagNjwaRMz2FIv2aHKaV26N1ML2fof7qNorDL88EursL0x0SDPMWLSfOV4dtFrRonjORCP8ri8iZLZOaefsN1NbRGw6Xbz1vJXr4eTPcNl%2BcZaIcNoYS%2F830KrQHkbBFNo4GtzCkWmZzo8ZPmSsp9keALoSvuSXOqZWw4CRCN4&X-Amz-Signature=7e7c9c4031fc91496788fe834f0275bf87583817cd2b509c0ee04145c4f8afeb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPH4THXA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQD0DJpI8BUHVGF5Xb8Akpm6wM7xzzvlzxK4YVfXn0e7hwIhANdpiSpLV0qjjx7lOzWwcOrfMGHFOBf96kNA3hj1N3m%2FKv8DCEQQABoMNjM3NDIzMTgzODA1IgyrrIGnYvZu9Bhz7w0q3APqVdErxDRGZ6KoIDGb%2FjkHrkzBzidDb46xZ0hn2RmfHMGG8d9g0axH05o5%2BMta734y3vvKqthV8BiA%2BkPNtEQmddpqlxsQwfrOSO76OV2gOKDDAwDbLiGe2uSyUDRhEb%2FFY8A%2FQDxGn21VCT7cUSFk1jvw7RaV9dUSPiqH37bJ%2FBydTDPXboDvn6%2F3ZYW6foMjYq%2BUzGDf1HH7N5040wfOXKJjGdPdlu9SSeFyAISb3TXc%2BtrdcnQ2DfvpRDCE7%2BoTPgFT2nYS%2BROFZtLsq31beaelk5tI3evHvq35D54Q5zzqZHcASgTyNEOY68YuDR1ZeuAxyDWvlAFgXyi0e38EXt3fRO4IyXmsHRNfAKeZYjDcNZzuo%2F2%2FEvXmVSDMePwXBcA8h8VjAQWGsxQkocCvkXZOKuC2r992cZylrX7HIUlrFaKCcZRHy%2FdqGDJ%2FCZ7hPGohZjO7GY9%2BGTcorma9Un9m%2FdNxktJIUxRHzIl5rFPBjlOPoeYQF2rSgVEMYTBhGfsrzUpzV89S8ytyDapK6x5bvRnf1WWTcOZjMI4weRotDDnjmo6LKQVUHjCGuRV1X7FTgCP%2B2bWKPId%2BRTUiiIA4cgAkEdUJWdJbaz3yPMKxYq%2FHYIv%2F47%2FyxDCfi429BjqkAeVMCAMVOjf4De60%2FoIO1QRdJHo21MR4o5iIS6FErHKLRjvSzq%2BagNjwaRMz2FIv2aHKaV26N1ML2fof7qNorDL88EursL0x0SDPMWLSfOV4dtFrRonjORCP8ri8iZLZOaefsN1NbRGw6Xbz1vJXr4eTPcNl%2BcZaIcNoYS%2F830KrQHkbBFNo4GtzCkWmZzo8ZPmSsp9keALoSvuSXOqZWw4CRCN4&X-Amz-Signature=995d8475ad05168ada4a7b6ed9f5aca09c7eed89d1f9da7255be77e9ad0fc7bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LY7MPWI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIGWwy4HmzWHtY2FooScV3o8xMHbBFA20xkIz4zdsfCD4AiBKin7S2zSK0oDAJv5ni300CxfDgEBkupzAAdrmNaQjkCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMzwYprTqTEbyObYEzKtwDLoCQdsDUoD1Xbwl7YKXl%2B%2BQLdcktLqeVwhYb%2FZFFo02089HfVHpgxrX9eF27m29QhXHogMsxUm6evT0vHfUGO1CoPJLEUoRACgfDLzXOc6B1omxpDKSH5WlumMBe9koZbznKT3gNEzd8Bi9F6d%2Fz7lXtQRiLHc5egqbiRECxx7KK%2FYticpGkwo3R17z75KDXBPjJa4DRF9NpTkIcVPXQM3%2BcNWrnq2ECfTKrrqwtVho8Fyenq4tFWD4JtM9fo%2FBljB8IHu2CL9sj2RrpEJv8czqfmZfrtvZghyZUK2P2b%2FjA55elqaMQsspjXTIetRFxaTU%2FKjpv%2BPkXuPY9ZhjF1n5OfGPQkRLcHuRcqQRlgmk2x%2BOG6%2FDctYDmXw6Slc5%2FQKY5%2Fxs360fapTfWbVuCueIfqJdXvYVuCLfFUV8r%2Bf7Hvfqu%2Fc5mPCn6gD83vyHTKMvKYtvRyUB3aGyMwYT7OTMmWgYvzNF1xB5%2FfPyFSRylEfnfeVzIi7dwzTr6ql%2BmHB65kkgLQgPVwG1hbjF%2Fhj5RkXeLV880dC%2FoIbqBBU%2FqVtoiXbNFgQ7%2BX%2Fd0jujX26p1NbtWz6mgGhWnuQ7Atad5SYmOffJEU9PsuNP2VpV%2BLfPP8PvfT1xZn8gw84qNvQY6pgGcyEXvqklsEDHwX6Ahw5OVHNOzRQlKLHHM3PXR%2FCSbLnM3kFeqn0Xu29eY43hsaCJmDZf2bkVDgPacvkAnRK1RUamPgUsWDAPiTkCtmEgPZPRmOc6TFkrrevmxucUeIm%2BqXdWXuOg6eBjjtf5YvAi2LSQdgEdL4EM17enSjkwn3Y8GVLhzN9yI13EAP47OD0CUQ0tKT8%2Bdcv1vBKPpf52LQ8hqx4L7&X-Amz-Signature=ed48324faf2031ba9db32e255fc43e326dade31152e533d678ba6b6b8b51610c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5PYWUWL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIA36x8D9DRc4hwtRcay5XAYQKgrYrY5Ed5jE20H4A3HiAiBMOHHNi0lpLWsbaSXupGD34XlluGZp3FQojEaZuYvqpCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMITUwz1tu%2B8w3z6E4KtwDHik9tSBXy0wBjOF7G31rQCL1KTMsdAhbTwiUFZoueAHIe43u5PLGpubhJru9n0QDRcWTM8nKNQsnzaLVeBXDbb7Dc7WkEiUFraenEq53hXEiiqzSYJpOg9aT7GT%2BaRUmjLlVRyX63cig3JxciJMO9jF2LHvDJvTy5iD44e64RUD4xRAPWZqz5AVZ7p0Iz4VNNhR8UXHjpxGXh%2BxFBX%2FfAqtyQX%2BH1%2ByGKdg8PtR5mEKWfuUnL9KUIbSHvlOvBFh1qv2%2BBopTVxBedYsCbbbRfbjX%2B%2BBpP3XLLNCrvfUk9uh3SNhJVuuynAwAJXOpMxSJhMhUyA9c6PJYL4tiTzLsvof%2FFNekEdURA8zm%2BC%2BPt39Zl8VrGlnf4X3QqDjoydywvLwBhXZVuUNtu6cqdagp3IR4%2BGQdegX1gzyZG2njRrzf1wWhCwTj4SfWMtMLU5r1a%2BXuHihGJJNvHbyfGkCnnU7ga%2Bow4Qte7l4eQvApgr5Uv9kkA4hyDqvXBCPbOTZltrq1ETreHOSmLVwRljs3DlcW1cVQ%2Bm51%2FV2xOdsNxMGfhX06OtaoJxUi6u0TaAxfaH38L9Iyxlov%2BpzcZEcjrsVGL6ZZsX0E18q4iOL4ahpwMoxkDra6%2B4E2XXcwjouNvQY6pgGcXxnWw6UTSn2GTaKDRFamGzUo6TM7hZLTl2tkiFYPM5%2BNibCYrVRtrqcXTTcH%2FUuXjm6fRV%2Bz5UvfF4noTGqQuzKgml8%2FtBVboZY4Nx8uqZzgUdbEaxD%2FDlWQT5q0hWMrG%2BY2j7GBx%2FLOfRF%2FFlKn7gBnOk4rTKhLeypYqPv%2FGRA6fz3%2BF5kTx72DastJxj1V5Fz7sAJxLhUtnkOeUCnzXaJLRtHS&X-Amz-Signature=1a2d6a93e28005d5169af2d0e50a5a958040166f09f45d037e86541d68b0c5f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DJX2VCE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCID2FP4E9%2FgMPCmldnjGY1IhbSBVdnYv%2BIzmuRBOPI3IrAiEA8zqyjCfIlm%2BX%2BRw3ueE%2BJpjalpAGc0pwq%2B7KLXU9cnAq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDg0tVY7sj79F4sDMSrcA0klF7gbBiklYaJQQTWBCyFMwjMQl6AKwJzzuHPRp9EBuxz34NMheeylndl9bkUNhcTQLilxuSvLP0uaj38XKZhDLi3b2mAsGODhgO4oEoW0MDKQN5XHxhQvspqvROplHSufqkq9xzlEXb%2BjxW%2FisMW5%2B5pACwmae9Rxm2QNsmdXlMPyEWgohd3PPuIBJHMN%2BdNpWXuBt1XB8ls79S71pOGUxpmbRSv4nxjlf%2B0U6hVx1KQQOmqC8NwvhASpjoCuCb0XMif5T0hfhW1lS%2BPWIie%2BTBXXXepx8Ua3zNPSj9x75eWJH6ebZU4M5e7RvHOpxzwJeJ5Opafb0o4sz3e%2FRkxGfCwz4OQncuBsljvOOUid6kAEJ5a4X%2BGIrQqpB0eYgihqV05kuuXlZk3ijQSylwnLFJW8MjtU%2BxN1epknuje545UyWQdfl8volKBSMLB7HUJAAOAXpYvlbmZ0l96iKvJuX%2Fv4E3epjNul9n7WP%2FcCkNnHndjl8ZJ3sFmLglNcOwvQK1UG0US%2FLQalDCmGlQnx7XFmaVWNmHAHMMOudnqpxIcDFcDuzGP2IFdFP8R%2Bs6gLkbOxPeo3dngxzZn4v7zvP4AtSKllxBJ58gGarvf3E8DKPKwIXMaCghuGMOaKjb0GOqUBBZjrr1kT0qv17vt617sjSCj5OE0CYvx2416d8i75DxYYPM70GIzmb7cBJjbCVXe1JPOHOIroSh0Z3cItPLu%2BoiyKLwxV7J8zWZccoPzVwi9FArJQAKlykBsNP2VWBi1v7hMWyXkyscB%2F0JzQjuxTHIhYZI18qhnKjYoadzVzd4geqA7IesKSK3jul9t3wYKCfIshgiYuJ5OO6PqaAKa8eEZ1eD8W&X-Amz-Signature=189174920af7c62327e071aa535e6fd97127ccebd473b541c722d1ebd339c661&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DJX2VCE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCID2FP4E9%2FgMPCmldnjGY1IhbSBVdnYv%2BIzmuRBOPI3IrAiEA8zqyjCfIlm%2BX%2BRw3ueE%2BJpjalpAGc0pwq%2B7KLXU9cnAq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDg0tVY7sj79F4sDMSrcA0klF7gbBiklYaJQQTWBCyFMwjMQl6AKwJzzuHPRp9EBuxz34NMheeylndl9bkUNhcTQLilxuSvLP0uaj38XKZhDLi3b2mAsGODhgO4oEoW0MDKQN5XHxhQvspqvROplHSufqkq9xzlEXb%2BjxW%2FisMW5%2B5pACwmae9Rxm2QNsmdXlMPyEWgohd3PPuIBJHMN%2BdNpWXuBt1XB8ls79S71pOGUxpmbRSv4nxjlf%2B0U6hVx1KQQOmqC8NwvhASpjoCuCb0XMif5T0hfhW1lS%2BPWIie%2BTBXXXepx8Ua3zNPSj9x75eWJH6ebZU4M5e7RvHOpxzwJeJ5Opafb0o4sz3e%2FRkxGfCwz4OQncuBsljvOOUid6kAEJ5a4X%2BGIrQqpB0eYgihqV05kuuXlZk3ijQSylwnLFJW8MjtU%2BxN1epknuje545UyWQdfl8volKBSMLB7HUJAAOAXpYvlbmZ0l96iKvJuX%2Fv4E3epjNul9n7WP%2FcCkNnHndjl8ZJ3sFmLglNcOwvQK1UG0US%2FLQalDCmGlQnx7XFmaVWNmHAHMMOudnqpxIcDFcDuzGP2IFdFP8R%2Bs6gLkbOxPeo3dngxzZn4v7zvP4AtSKllxBJ58gGarvf3E8DKPKwIXMaCghuGMOaKjb0GOqUBBZjrr1kT0qv17vt617sjSCj5OE0CYvx2416d8i75DxYYPM70GIzmb7cBJjbCVXe1JPOHOIroSh0Z3cItPLu%2BoiyKLwxV7J8zWZccoPzVwi9FArJQAKlykBsNP2VWBi1v7hMWyXkyscB%2F0JzQjuxTHIhYZI18qhnKjYoadzVzd4geqA7IesKSK3jul9t3wYKCfIshgiYuJ5OO6PqaAKa8eEZ1eD8W&X-Amz-Signature=304522ad25c56d8bf8322bc1a7ac51a369d8c0376a4d39efb2676c58e8f79e5f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
