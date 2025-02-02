

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KQXOVQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGsqTWGcGclWqWs9hr3R%2BdHyrP7P%2BD1iKUQPL4xsUo9lAiEA3Kn5y5JtwTqYra%2BKT1uq3me0VRf1aSfSSaZhkPhid9cqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQM1IbkSNP4zWiGASrcA6oT3N%2BCwOEt27AaLk3d1RGZ%2B18EeaIqHLRB%2F5Xnm4O8tmLGUHNtJuw6GHHZwBwFGGhpW%2BS%2BSXbM51%2BapO2%2FXGeJdE1r6ziIXREJ5sxbbLrdxk%2FDgctor2DP1rZiVQMktNN8FNQOrgmKvJyTzu%2FIRKRh4HPmsw8vO7fGADKGyDQyj9rL%2Fkgs8ZIqX6LRuqwtAz4uhK0ZRe6%2FUF2zM5uanNdQGifiKUWsy1sZADFE4HZjp0tu2Ir6o6%2FwRhb1rOdSsSInosRaUMur6X%2FcDyPZTvUXi7Lu8hReXAWBUN40gNQ3VicF7yNtHETpqg4EKZne0acDJYsBrKMJXAY29mNaZU%2Fsx43QC5BQLq4UzOMsH3zPRkx2b608BjsaehsZr2be%2BFPrH0CV0Erh6eQaUhy7leIX8LahprkRUUBWk9fg86gVkuno8gttlp%2BeBYUaaO617GB2nzx6avzxq8HxYVND5naldpHQ69eQz9KKDwni%2BHuoXWWlEn0OzIljS1j72k1HE%2BfY2A6XCR3oDWR8aaXe1qNVwGPiySPgeIV30UFDqREDMYsHuZIaaYsT4mLsSk%2BEpDUUk9X88LbAjc1k7mHIWADJoa3mUM04ZsFltrukNymFlnH1xtb%2FjzvZcj%2B9MOi6%2B7wGOqUBW3DzK%2FDOCpe73Cg0Dz4WNLvUu0p%2FYEG%2FdyvcFNmG7eoIGjj%2BplgEIczBZmhcrTsflpd%2FtXDsF6zji7rQM5agIjXWYWQ%2B5vfoxxaI%2Fmd59QRB9D9Xagyduz2JVMNaLpVo94H%2FQ7PxeFeDW67DqatJGqlN4uVumya31yurG1Nlpu0XIz3b9A3mqU9%2BRnfvkoEHM33YxNupdTiO4hh%2F9FBo%2FoOVueeX&X-Amz-Signature=7c696678642c6a064db1a5b17ef17f27796944073a38a1af01b9d0df78fff795&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KQXOVQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGsqTWGcGclWqWs9hr3R%2BdHyrP7P%2BD1iKUQPL4xsUo9lAiEA3Kn5y5JtwTqYra%2BKT1uq3me0VRf1aSfSSaZhkPhid9cqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQM1IbkSNP4zWiGASrcA6oT3N%2BCwOEt27AaLk3d1RGZ%2B18EeaIqHLRB%2F5Xnm4O8tmLGUHNtJuw6GHHZwBwFGGhpW%2BS%2BSXbM51%2BapO2%2FXGeJdE1r6ziIXREJ5sxbbLrdxk%2FDgctor2DP1rZiVQMktNN8FNQOrgmKvJyTzu%2FIRKRh4HPmsw8vO7fGADKGyDQyj9rL%2Fkgs8ZIqX6LRuqwtAz4uhK0ZRe6%2FUF2zM5uanNdQGifiKUWsy1sZADFE4HZjp0tu2Ir6o6%2FwRhb1rOdSsSInosRaUMur6X%2FcDyPZTvUXi7Lu8hReXAWBUN40gNQ3VicF7yNtHETpqg4EKZne0acDJYsBrKMJXAY29mNaZU%2Fsx43QC5BQLq4UzOMsH3zPRkx2b608BjsaehsZr2be%2BFPrH0CV0Erh6eQaUhy7leIX8LahprkRUUBWk9fg86gVkuno8gttlp%2BeBYUaaO617GB2nzx6avzxq8HxYVND5naldpHQ69eQz9KKDwni%2BHuoXWWlEn0OzIljS1j72k1HE%2BfY2A6XCR3oDWR8aaXe1qNVwGPiySPgeIV30UFDqREDMYsHuZIaaYsT4mLsSk%2BEpDUUk9X88LbAjc1k7mHIWADJoa3mUM04ZsFltrukNymFlnH1xtb%2FjzvZcj%2B9MOi6%2B7wGOqUBW3DzK%2FDOCpe73Cg0Dz4WNLvUu0p%2FYEG%2FdyvcFNmG7eoIGjj%2BplgEIczBZmhcrTsflpd%2FtXDsF6zji7rQM5agIjXWYWQ%2B5vfoxxaI%2Fmd59QRB9D9Xagyduz2JVMNaLpVo94H%2FQ7PxeFeDW67DqatJGqlN4uVumya31yurG1Nlpu0XIz3b9A3mqU9%2BRnfvkoEHM33YxNupdTiO4hh%2F9FBo%2FoOVueeX&X-Amz-Signature=546a613446f906a7c163eda78ead040cb0a90eb9dde2392e2599dc7d7a53c2ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KQXOVQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGsqTWGcGclWqWs9hr3R%2BdHyrP7P%2BD1iKUQPL4xsUo9lAiEA3Kn5y5JtwTqYra%2BKT1uq3me0VRf1aSfSSaZhkPhid9cqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQM1IbkSNP4zWiGASrcA6oT3N%2BCwOEt27AaLk3d1RGZ%2B18EeaIqHLRB%2F5Xnm4O8tmLGUHNtJuw6GHHZwBwFGGhpW%2BS%2BSXbM51%2BapO2%2FXGeJdE1r6ziIXREJ5sxbbLrdxk%2FDgctor2DP1rZiVQMktNN8FNQOrgmKvJyTzu%2FIRKRh4HPmsw8vO7fGADKGyDQyj9rL%2Fkgs8ZIqX6LRuqwtAz4uhK0ZRe6%2FUF2zM5uanNdQGifiKUWsy1sZADFE4HZjp0tu2Ir6o6%2FwRhb1rOdSsSInosRaUMur6X%2FcDyPZTvUXi7Lu8hReXAWBUN40gNQ3VicF7yNtHETpqg4EKZne0acDJYsBrKMJXAY29mNaZU%2Fsx43QC5BQLq4UzOMsH3zPRkx2b608BjsaehsZr2be%2BFPrH0CV0Erh6eQaUhy7leIX8LahprkRUUBWk9fg86gVkuno8gttlp%2BeBYUaaO617GB2nzx6avzxq8HxYVND5naldpHQ69eQz9KKDwni%2BHuoXWWlEn0OzIljS1j72k1HE%2BfY2A6XCR3oDWR8aaXe1qNVwGPiySPgeIV30UFDqREDMYsHuZIaaYsT4mLsSk%2BEpDUUk9X88LbAjc1k7mHIWADJoa3mUM04ZsFltrukNymFlnH1xtb%2FjzvZcj%2B9MOi6%2B7wGOqUBW3DzK%2FDOCpe73Cg0Dz4WNLvUu0p%2FYEG%2FdyvcFNmG7eoIGjj%2BplgEIczBZmhcrTsflpd%2FtXDsF6zji7rQM5agIjXWYWQ%2B5vfoxxaI%2Fmd59QRB9D9Xagyduz2JVMNaLpVo94H%2FQ7PxeFeDW67DqatJGqlN4uVumya31yurG1Nlpu0XIz3b9A3mqU9%2BRnfvkoEHM33YxNupdTiO4hh%2F9FBo%2FoOVueeX&X-Amz-Signature=fe0a84c661403a4134de4f0e96d778e729fe1a674900cb6a458f84dec77da902&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KQXOVQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGsqTWGcGclWqWs9hr3R%2BdHyrP7P%2BD1iKUQPL4xsUo9lAiEA3Kn5y5JtwTqYra%2BKT1uq3me0VRf1aSfSSaZhkPhid9cqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQM1IbkSNP4zWiGASrcA6oT3N%2BCwOEt27AaLk3d1RGZ%2B18EeaIqHLRB%2F5Xnm4O8tmLGUHNtJuw6GHHZwBwFGGhpW%2BS%2BSXbM51%2BapO2%2FXGeJdE1r6ziIXREJ5sxbbLrdxk%2FDgctor2DP1rZiVQMktNN8FNQOrgmKvJyTzu%2FIRKRh4HPmsw8vO7fGADKGyDQyj9rL%2Fkgs8ZIqX6LRuqwtAz4uhK0ZRe6%2FUF2zM5uanNdQGifiKUWsy1sZADFE4HZjp0tu2Ir6o6%2FwRhb1rOdSsSInosRaUMur6X%2FcDyPZTvUXi7Lu8hReXAWBUN40gNQ3VicF7yNtHETpqg4EKZne0acDJYsBrKMJXAY29mNaZU%2Fsx43QC5BQLq4UzOMsH3zPRkx2b608BjsaehsZr2be%2BFPrH0CV0Erh6eQaUhy7leIX8LahprkRUUBWk9fg86gVkuno8gttlp%2BeBYUaaO617GB2nzx6avzxq8HxYVND5naldpHQ69eQz9KKDwni%2BHuoXWWlEn0OzIljS1j72k1HE%2BfY2A6XCR3oDWR8aaXe1qNVwGPiySPgeIV30UFDqREDMYsHuZIaaYsT4mLsSk%2BEpDUUk9X88LbAjc1k7mHIWADJoa3mUM04ZsFltrukNymFlnH1xtb%2FjzvZcj%2B9MOi6%2B7wGOqUBW3DzK%2FDOCpe73Cg0Dz4WNLvUu0p%2FYEG%2FdyvcFNmG7eoIGjj%2BplgEIczBZmhcrTsflpd%2FtXDsF6zji7rQM5agIjXWYWQ%2B5vfoxxaI%2Fmd59QRB9D9Xagyduz2JVMNaLpVo94H%2FQ7PxeFeDW67DqatJGqlN4uVumya31yurG1Nlpu0XIz3b9A3mqU9%2BRnfvkoEHM33YxNupdTiO4hh%2F9FBo%2FoOVueeX&X-Amz-Signature=48c24c541432916ec7320f5bea673cf607fb45a40b1ba097ea231f406d51d76d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KQXOVQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGsqTWGcGclWqWs9hr3R%2BdHyrP7P%2BD1iKUQPL4xsUo9lAiEA3Kn5y5JtwTqYra%2BKT1uq3me0VRf1aSfSSaZhkPhid9cqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQM1IbkSNP4zWiGASrcA6oT3N%2BCwOEt27AaLk3d1RGZ%2B18EeaIqHLRB%2F5Xnm4O8tmLGUHNtJuw6GHHZwBwFGGhpW%2BS%2BSXbM51%2BapO2%2FXGeJdE1r6ziIXREJ5sxbbLrdxk%2FDgctor2DP1rZiVQMktNN8FNQOrgmKvJyTzu%2FIRKRh4HPmsw8vO7fGADKGyDQyj9rL%2Fkgs8ZIqX6LRuqwtAz4uhK0ZRe6%2FUF2zM5uanNdQGifiKUWsy1sZADFE4HZjp0tu2Ir6o6%2FwRhb1rOdSsSInosRaUMur6X%2FcDyPZTvUXi7Lu8hReXAWBUN40gNQ3VicF7yNtHETpqg4EKZne0acDJYsBrKMJXAY29mNaZU%2Fsx43QC5BQLq4UzOMsH3zPRkx2b608BjsaehsZr2be%2BFPrH0CV0Erh6eQaUhy7leIX8LahprkRUUBWk9fg86gVkuno8gttlp%2BeBYUaaO617GB2nzx6avzxq8HxYVND5naldpHQ69eQz9KKDwni%2BHuoXWWlEn0OzIljS1j72k1HE%2BfY2A6XCR3oDWR8aaXe1qNVwGPiySPgeIV30UFDqREDMYsHuZIaaYsT4mLsSk%2BEpDUUk9X88LbAjc1k7mHIWADJoa3mUM04ZsFltrukNymFlnH1xtb%2FjzvZcj%2B9MOi6%2B7wGOqUBW3DzK%2FDOCpe73Cg0Dz4WNLvUu0p%2FYEG%2FdyvcFNmG7eoIGjj%2BplgEIczBZmhcrTsflpd%2FtXDsF6zji7rQM5agIjXWYWQ%2B5vfoxxaI%2Fmd59QRB9D9Xagyduz2JVMNaLpVo94H%2FQ7PxeFeDW67DqatJGqlN4uVumya31yurG1Nlpu0XIz3b9A3mqU9%2BRnfvkoEHM33YxNupdTiO4hh%2F9FBo%2FoOVueeX&X-Amz-Signature=6a2b84fb785e173fc70bbbf28f9cb18965e2676c957a1ac193ae300a81a13a61&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KQXOVQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGsqTWGcGclWqWs9hr3R%2BdHyrP7P%2BD1iKUQPL4xsUo9lAiEA3Kn5y5JtwTqYra%2BKT1uq3me0VRf1aSfSSaZhkPhid9cqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQM1IbkSNP4zWiGASrcA6oT3N%2BCwOEt27AaLk3d1RGZ%2B18EeaIqHLRB%2F5Xnm4O8tmLGUHNtJuw6GHHZwBwFGGhpW%2BS%2BSXbM51%2BapO2%2FXGeJdE1r6ziIXREJ5sxbbLrdxk%2FDgctor2DP1rZiVQMktNN8FNQOrgmKvJyTzu%2FIRKRh4HPmsw8vO7fGADKGyDQyj9rL%2Fkgs8ZIqX6LRuqwtAz4uhK0ZRe6%2FUF2zM5uanNdQGifiKUWsy1sZADFE4HZjp0tu2Ir6o6%2FwRhb1rOdSsSInosRaUMur6X%2FcDyPZTvUXi7Lu8hReXAWBUN40gNQ3VicF7yNtHETpqg4EKZne0acDJYsBrKMJXAY29mNaZU%2Fsx43QC5BQLq4UzOMsH3zPRkx2b608BjsaehsZr2be%2BFPrH0CV0Erh6eQaUhy7leIX8LahprkRUUBWk9fg86gVkuno8gttlp%2BeBYUaaO617GB2nzx6avzxq8HxYVND5naldpHQ69eQz9KKDwni%2BHuoXWWlEn0OzIljS1j72k1HE%2BfY2A6XCR3oDWR8aaXe1qNVwGPiySPgeIV30UFDqREDMYsHuZIaaYsT4mLsSk%2BEpDUUk9X88LbAjc1k7mHIWADJoa3mUM04ZsFltrukNymFlnH1xtb%2FjzvZcj%2B9MOi6%2B7wGOqUBW3DzK%2FDOCpe73Cg0Dz4WNLvUu0p%2FYEG%2FdyvcFNmG7eoIGjj%2BplgEIczBZmhcrTsflpd%2FtXDsF6zji7rQM5agIjXWYWQ%2B5vfoxxaI%2Fmd59QRB9D9Xagyduz2JVMNaLpVo94H%2FQ7PxeFeDW67DqatJGqlN4uVumya31yurG1Nlpu0XIz3b9A3mqU9%2BRnfvkoEHM33YxNupdTiO4hh%2F9FBo%2FoOVueeX&X-Amz-Signature=fdf158623bc768a7c4bb8b9deeeaa15d1e7dcb7a6af3b1cfd45e21546e204cee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KQXOVQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGsqTWGcGclWqWs9hr3R%2BdHyrP7P%2BD1iKUQPL4xsUo9lAiEA3Kn5y5JtwTqYra%2BKT1uq3me0VRf1aSfSSaZhkPhid9cqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQM1IbkSNP4zWiGASrcA6oT3N%2BCwOEt27AaLk3d1RGZ%2B18EeaIqHLRB%2F5Xnm4O8tmLGUHNtJuw6GHHZwBwFGGhpW%2BS%2BSXbM51%2BapO2%2FXGeJdE1r6ziIXREJ5sxbbLrdxk%2FDgctor2DP1rZiVQMktNN8FNQOrgmKvJyTzu%2FIRKRh4HPmsw8vO7fGADKGyDQyj9rL%2Fkgs8ZIqX6LRuqwtAz4uhK0ZRe6%2FUF2zM5uanNdQGifiKUWsy1sZADFE4HZjp0tu2Ir6o6%2FwRhb1rOdSsSInosRaUMur6X%2FcDyPZTvUXi7Lu8hReXAWBUN40gNQ3VicF7yNtHETpqg4EKZne0acDJYsBrKMJXAY29mNaZU%2Fsx43QC5BQLq4UzOMsH3zPRkx2b608BjsaehsZr2be%2BFPrH0CV0Erh6eQaUhy7leIX8LahprkRUUBWk9fg86gVkuno8gttlp%2BeBYUaaO617GB2nzx6avzxq8HxYVND5naldpHQ69eQz9KKDwni%2BHuoXWWlEn0OzIljS1j72k1HE%2BfY2A6XCR3oDWR8aaXe1qNVwGPiySPgeIV30UFDqREDMYsHuZIaaYsT4mLsSk%2BEpDUUk9X88LbAjc1k7mHIWADJoa3mUM04ZsFltrukNymFlnH1xtb%2FjzvZcj%2B9MOi6%2B7wGOqUBW3DzK%2FDOCpe73Cg0Dz4WNLvUu0p%2FYEG%2FdyvcFNmG7eoIGjj%2BplgEIczBZmhcrTsflpd%2FtXDsF6zji7rQM5agIjXWYWQ%2B5vfoxxaI%2Fmd59QRB9D9Xagyduz2JVMNaLpVo94H%2FQ7PxeFeDW67DqatJGqlN4uVumya31yurG1Nlpu0XIz3b9A3mqU9%2BRnfvkoEHM33YxNupdTiO4hh%2F9FBo%2FoOVueeX&X-Amz-Signature=3308439aff4a088edda7f90294fa188024406f0f5107768e89d2072e78a794cd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KQXOVQC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGsqTWGcGclWqWs9hr3R%2BdHyrP7P%2BD1iKUQPL4xsUo9lAiEA3Kn5y5JtwTqYra%2BKT1uq3me0VRf1aSfSSaZhkPhid9cqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFQM1IbkSNP4zWiGASrcA6oT3N%2BCwOEt27AaLk3d1RGZ%2B18EeaIqHLRB%2F5Xnm4O8tmLGUHNtJuw6GHHZwBwFGGhpW%2BS%2BSXbM51%2BapO2%2FXGeJdE1r6ziIXREJ5sxbbLrdxk%2FDgctor2DP1rZiVQMktNN8FNQOrgmKvJyTzu%2FIRKRh4HPmsw8vO7fGADKGyDQyj9rL%2Fkgs8ZIqX6LRuqwtAz4uhK0ZRe6%2FUF2zM5uanNdQGifiKUWsy1sZADFE4HZjp0tu2Ir6o6%2FwRhb1rOdSsSInosRaUMur6X%2FcDyPZTvUXi7Lu8hReXAWBUN40gNQ3VicF7yNtHETpqg4EKZne0acDJYsBrKMJXAY29mNaZU%2Fsx43QC5BQLq4UzOMsH3zPRkx2b608BjsaehsZr2be%2BFPrH0CV0Erh6eQaUhy7leIX8LahprkRUUBWk9fg86gVkuno8gttlp%2BeBYUaaO617GB2nzx6avzxq8HxYVND5naldpHQ69eQz9KKDwni%2BHuoXWWlEn0OzIljS1j72k1HE%2BfY2A6XCR3oDWR8aaXe1qNVwGPiySPgeIV30UFDqREDMYsHuZIaaYsT4mLsSk%2BEpDUUk9X88LbAjc1k7mHIWADJoa3mUM04ZsFltrukNymFlnH1xtb%2FjzvZcj%2B9MOi6%2B7wGOqUBW3DzK%2FDOCpe73Cg0Dz4WNLvUu0p%2FYEG%2FdyvcFNmG7eoIGjj%2BplgEIczBZmhcrTsflpd%2FtXDsF6zji7rQM5agIjXWYWQ%2B5vfoxxaI%2Fmd59QRB9D9Xagyduz2JVMNaLpVo94H%2FQ7PxeFeDW67DqatJGqlN4uVumya31yurG1Nlpu0XIz3b9A3mqU9%2BRnfvkoEHM33YxNupdTiO4hh%2F9FBo%2FoOVueeX&X-Amz-Signature=d5c6f4b5101ddf3ac0401c52fb5e6e08df145d089166e8d386a83a73194ee9e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR3CUNZ7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRqVVHHFw6j4wrV14zPaqUoSuJz2S7DLy5S%2Bcs6yKwpgIgHcrl3%2FQ6wi0uxcQNppmNxuzEm2VB0eK4S1rAvKAhsPwqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPEA3vkwpTt21r%2BrUircA%2F%2B5sXkybYvro7ZjMziF31u%2FvGUh0bsx98alq3vKAr9R4uLnhdxkm6xM1BAHHuaWae4jasjIaB86oII3jLGKHhJ%2BucWtRKQn9cI7BiHWozcKG6CwVvDillZt5lrLZ3yQa6acYYyr%2FyV00r%2BUaRIlqMXmfJRLWTSGsKObm1jN%2FRBc49sNlmctTW37NHOYXDr0qw%2FVRq1eTW6dgIVFiPkEkGfNPrasqZWbqyLKBFMTTQeP43jgF4oXtZL1lyF7GJW8doAOZ8BiMxuXk6I7Bi68NZgmq7L38rRqo5ghp1CRIzJOcgGyEUgKTvOeOJG%2BW30Zm%2F7ixCUXWeVxgMojiv75KJdAPi5oRyJjbkrqPeTeGyDFSTv55VZDySvuSZxiFd3J43%2FcrBAIRg2fiBSCVlOC2%2FDDiFkmCEKSXCt52QImtX2rObmdKipYXspNwfLn%2F8T8M1f14%2FU7yXPKeFGc3Sj05zaTzdbn5MGAPzwi%2FFTmwL0bx%2FZHxIfx7ZIgosqdgmQ%2BxcferCkB%2FyXkrCuv41pDcz12u%2B%2FXSZb1GJs2WKA4pZu9megLzEngaZx1tb7Dt2FAMB9qExde5L4EyTySlil1RIM7%2BADSDQovqsKjEVF0XPQ0OcCBshQzokOUGWW3MNO6%2B7wGOqUBXZGFR9P41SpaXHiqZpFlJMuN9afhefAf45X2DAmBmYpXNftCVRTjbLQ6qb%2Bw4X6OzI5298uFSTIy8pLMyLMjqHuFqYcdN6RRI%2FeRi%2F4lyBygaoiOC1shH%2F%2FScEILL4LMAftubDId0jUQoTfddsX9V8uEGQsITXxWBTl5enP4%2BlCWzh6eteqFdJENkGh58ED18oSoDdf9jN6a9v4h8eX%2FYaQYnq6d&X-Amz-Signature=2e4550f6fc071ddd67e071de8630ad0be0ca1e51bb77ca023a2bdc4422468e58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666N5RFFS%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGpas2ppcdU4pVYHv8CxzgtI2jm%2FLVVAWp0ggI21Yj1FAiBTwAeoL6%2BL87xsoFXkiNfF1msXD6NdMTxjOI4x%2FEnDBiqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMN91IiIUXu%2B3zhThSKtwDey9P%2Fkv1eeQ8P1efYUqfaVl%2BGDlbjK00DHQt6q7MqH%2FEF4O2eKgzgBBWyK3UgoIvrX4G7B2S9Aq4kXElDwwz2%2FRdnFIsPuYMxEoy32ugCpAVIyo0JIruB4dn9K2gqNDoTmm6FH0nup39sMgki2ixjpCF37lHwy%2BJkr2wXKlrzShsCBEPv2ZnAktVZLTSg%2B6VMa7D4TWANelV8sljBxf9l%2BMVIDXfomYCUmtyuDbul6T7W3GPEAMmpMLsSVWscU5HRjet1pku1R09SMblLLY8J6np2tmFtjyQVqhR4qoCvVdtScmO%2F2v5jN%2BqceUMNuqnmYrn06Xfgc4i6gGDl5RxtpKTNM0ZR4MQmLqy9f7XvvDJR4CtLxdwd7g%2FUpQiJmnxUhK%2BpCnbgAIAtqwNJjy3XFl8qMvrlxH07ePmmPHVCn2hfe9n1rb54XEwX4Fdo%2BKLKFbTxy1j9w%2BPVAryV29P7WG%2BVVXyDjjIhNYyZSiZP4N1h7IEnNI%2BzyOItvvTZS%2BwsF%2F2kBYlOah0pGCcbbjDcEu%2BApn2jYWj78ZRH3ecGtZFtVFaxjzPIi6QyIPoD9LH3ivN7Ha5XZ91yZ6MkXxKN0eGMv%2FeCXgFD5dpCna2PNbao%2FrUNEuxgrCev3Ywi7v7vAY6pgFCSvzToG%2BpyjjqMhn9FH50zDvkiEm%2BfCGxVayhtLZN8Sp1Fy7mTUm1y2xxsCPzqBG0eKgTlIH5GPivNN74bP%2F%2Fp1r%2FQ3J%2FfhZvsmmNH7MBxSsHlfcs33%2BWVM5nwSsM0l7pUo1D9dlv%2B3nbJkVJZMSfPOKoR8cfmogev%2FDZ%2Bg57btT6EoApIFwkE4YSIQLkK9fFurqk%2Ba%2F7Z5PkJuT5h96HjK%2ByEJeA&X-Amz-Signature=4d991c3e6d0be9d7911707be2c4a2f2147fd0ff88af533650cc41025c7de4288&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5GLYKHN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGunc6z8DupW5Izut8aaK7Ozfof6Z8G%2FIgUyth9oNFqtAiBn6RqUNmECeAeBFR3Kk11Q9ZpMq7icyYBxL7gAxSyboiqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq4%2BEPtsufRC7onMFKtwD02o5412zWtwSSOkDheV6l3KfCC%2Fe9bO9k5XehMXgBJaf%2FzmukJPnes%2F3wZU0tRJF56jW0%2FvqzE30nVpQPTdj2lH8IH7EQbU0POjSPJvjbB23iAWzldpqwVQseY7BNMHLGuV2MY3GPiC1TiBaHhqi9yrHiEnhqdv73eldRscvyN0%2BTaHa%2F0cd7ADw0Cu5HhDVxK7T8P1uoNpQ7OTs%2BCbZ8KHZ0MnoMtAQPkSJ1XRT24AvsHHGJl9T0mBzvyF86%2BduEVw4EA9H9AzpvAUr6MlCIzb9e34nrTSWef%2FaSrYiNRKN%2B%2BXjs53jBxQgYUiYSxT6tU4o3E%2F5%2FF58vhBnvY1SDTuEKk7l59uM2yWrisoyr3rAcIv3BZn61SgeaDpf8dBS5l1fN9ak8NKXfOISniSCY%2B6L3ajsuSmQf3uIsYEgnWYn55PHmUva3EN1Ganbo45Da7GUOxNVKkgRFRI6tMXMBP%2F5sAe6iYRvk40oxd7%2BGG7kJRBACm1fsanA5%2B2qbzrMKM4qOrz8r0Yr8e6bLyxEkDPlUsyxU6wuKTRRFNoLr3M3cTvehxPx0Kb%2ByslU2VinRi%2FlzyNGu0ZeA7OCOL7JbBz1JLMPWTbIUuSGbKI9d3KrA%2BgRzO%2BXfLzI7J8w1rr7vAY6pgHZOYZY%2BAtyK2RIYN77WoztXYRxJOAY3q2A95DXMwDivr%2F2QyO7EFIu3czzRRKaVkTDrtiCjH8SHAE5qzLg9WQbPeB8a4gZOv0i9SdF%2FXyuUfttbh1yssHe1S0SwFkvL4jRDnrLpsy6VFBinn85Zwl7o5DC2KX8cUulCim5OpeQIIjxYO%2BnWL7E%2F6uRVl5pKei18wNl5lz3%2FCHnxp1gT5AhfNemasU7&X-Amz-Signature=a89be070f8416f15cd5dc9b2168cfc5e701b7863c747c6ae3132afd34a864b6e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5GLYKHN%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGunc6z8DupW5Izut8aaK7Ozfof6Z8G%2FIgUyth9oNFqtAiBn6RqUNmECeAeBFR3Kk11Q9ZpMq7icyYBxL7gAxSyboiqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq4%2BEPtsufRC7onMFKtwD02o5412zWtwSSOkDheV6l3KfCC%2Fe9bO9k5XehMXgBJaf%2FzmukJPnes%2F3wZU0tRJF56jW0%2FvqzE30nVpQPTdj2lH8IH7EQbU0POjSPJvjbB23iAWzldpqwVQseY7BNMHLGuV2MY3GPiC1TiBaHhqi9yrHiEnhqdv73eldRscvyN0%2BTaHa%2F0cd7ADw0Cu5HhDVxK7T8P1uoNpQ7OTs%2BCbZ8KHZ0MnoMtAQPkSJ1XRT24AvsHHGJl9T0mBzvyF86%2BduEVw4EA9H9AzpvAUr6MlCIzb9e34nrTSWef%2FaSrYiNRKN%2B%2BXjs53jBxQgYUiYSxT6tU4o3E%2F5%2FF58vhBnvY1SDTuEKk7l59uM2yWrisoyr3rAcIv3BZn61SgeaDpf8dBS5l1fN9ak8NKXfOISniSCY%2B6L3ajsuSmQf3uIsYEgnWYn55PHmUva3EN1Ganbo45Da7GUOxNVKkgRFRI6tMXMBP%2F5sAe6iYRvk40oxd7%2BGG7kJRBACm1fsanA5%2B2qbzrMKM4qOrz8r0Yr8e6bLyxEkDPlUsyxU6wuKTRRFNoLr3M3cTvehxPx0Kb%2ByslU2VinRi%2FlzyNGu0ZeA7OCOL7JbBz1JLMPWTbIUuSGbKI9d3KrA%2BgRzO%2BXfLzI7J8w1rr7vAY6pgHZOYZY%2BAtyK2RIYN77WoztXYRxJOAY3q2A95DXMwDivr%2F2QyO7EFIu3czzRRKaVkTDrtiCjH8SHAE5qzLg9WQbPeB8a4gZOv0i9SdF%2FXyuUfttbh1yssHe1S0SwFkvL4jRDnrLpsy6VFBinn85Zwl7o5DC2KX8cUulCim5OpeQIIjxYO%2BnWL7E%2F6uRVl5pKei18wNl5lz3%2FCHnxp1gT5AhfNemasU7&X-Amz-Signature=5b9b1ec5bfb96ddd3d9cd06a36001ff3b2a08fa238db518aee088fd2bb1986f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
