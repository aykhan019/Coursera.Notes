

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WN2GURX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH3pPPzgZVYDJS6ZzRmvY6kXqvwMNn2LqDxFZH5G2sl7AiEAi3%2F3c8eRVGmiXWAtpqAptYvgOEZBtjrQh68pgh3c71gqiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFPPE%2F65DhfvD%2FEpayrcA8lG%2BBrSCHKph6fhqCf2pneoTxnN%2B2Eq4cdtruXWOP495M0BUJiOXw4ASvTXL6RsMMDMpkCtMCmbgsGAJ5r%2Bei2xrYS%2FnNHkvPBfvFv3EghKtEkaOB2BxP5XI0nbyBGvxdxkE6mjPIkh5qmg8K%2F5RIDe4JHKT313iFCEAGgg0Hs04%2FHwYyIOxrIXRjedKK%2FohhiiPnFIeXUHtQ2j98d%2BNEg5Zd6DSdC4t1eIgYpPwk46yb7Nzp6gqR4tKwaDnmlJk9y4yXUCNS2wNtH1oA%2BjBEifUqx6%2Bp0rsTYZmtgYgVhtH6z875fdTCgnjq5j8TnYT9r18tomX39fgbgsw3SpuCuVqnzWZ3PIQ5cgaa0D7LGTLNsVCcrefu%2BQ1FHBxKx2RVlMRolsuxV7OdjaVBWE3DNhO%2FhFTmZKLtK4dwHUiRUIbbPXvGhnhUWnbQ5w6rmszTgwEeVWCpN1kKwXb2Ynl%2F%2FOjFZLzUMbSDqijzaMI6Qcf2rOTIT1HnRUjpd2z2m1wycOrxctxFyVeM5iRYnpVdKFizo4gKAz1G1bu4%2FNbXmUYxix5A01l5FSzskUNIGziWIip5iLiPrDLW2cSfOACCenEH2j5dx3MEhXUZ1CmKoNgRWfAAhzLUw%2BzlmDMM%2Fk%2F7wGOqUB0eobe6hXrlXYFAkm32DZfqhPoFwdTrvtyuP1E7B50EQudcoCooN0cs3hONb3cJjmZK%2F6bLFy0DisReuSmvLl46zcdUqpctSASYt2qymXz87CgCUOTdfve9Ze6AoSSQOFFgdXo6GPWirSKzIUHaYDnYJPGLisLpyznXhIW5aiBBk5ZxRafjlq5kELgOYMHyU%2F7UplL5d8RX5l2FgrXvxaDe9ceH%2FP&X-Amz-Signature=94f9306e51d90cca0e83bc96c8f08e7522fe8188b8761d3266b57d6ca0e06288&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WN2GURX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH3pPPzgZVYDJS6ZzRmvY6kXqvwMNn2LqDxFZH5G2sl7AiEAi3%2F3c8eRVGmiXWAtpqAptYvgOEZBtjrQh68pgh3c71gqiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFPPE%2F65DhfvD%2FEpayrcA8lG%2BBrSCHKph6fhqCf2pneoTxnN%2B2Eq4cdtruXWOP495M0BUJiOXw4ASvTXL6RsMMDMpkCtMCmbgsGAJ5r%2Bei2xrYS%2FnNHkvPBfvFv3EghKtEkaOB2BxP5XI0nbyBGvxdxkE6mjPIkh5qmg8K%2F5RIDe4JHKT313iFCEAGgg0Hs04%2FHwYyIOxrIXRjedKK%2FohhiiPnFIeXUHtQ2j98d%2BNEg5Zd6DSdC4t1eIgYpPwk46yb7Nzp6gqR4tKwaDnmlJk9y4yXUCNS2wNtH1oA%2BjBEifUqx6%2Bp0rsTYZmtgYgVhtH6z875fdTCgnjq5j8TnYT9r18tomX39fgbgsw3SpuCuVqnzWZ3PIQ5cgaa0D7LGTLNsVCcrefu%2BQ1FHBxKx2RVlMRolsuxV7OdjaVBWE3DNhO%2FhFTmZKLtK4dwHUiRUIbbPXvGhnhUWnbQ5w6rmszTgwEeVWCpN1kKwXb2Ynl%2F%2FOjFZLzUMbSDqijzaMI6Qcf2rOTIT1HnRUjpd2z2m1wycOrxctxFyVeM5iRYnpVdKFizo4gKAz1G1bu4%2FNbXmUYxix5A01l5FSzskUNIGziWIip5iLiPrDLW2cSfOACCenEH2j5dx3MEhXUZ1CmKoNgRWfAAhzLUw%2BzlmDMM%2Fk%2F7wGOqUB0eobe6hXrlXYFAkm32DZfqhPoFwdTrvtyuP1E7B50EQudcoCooN0cs3hONb3cJjmZK%2F6bLFy0DisReuSmvLl46zcdUqpctSASYt2qymXz87CgCUOTdfve9Ze6AoSSQOFFgdXo6GPWirSKzIUHaYDnYJPGLisLpyznXhIW5aiBBk5ZxRafjlq5kELgOYMHyU%2F7UplL5d8RX5l2FgrXvxaDe9ceH%2FP&X-Amz-Signature=5edf5c96462a4bcbb01aa7de3fc2533d4abe7374492a9e2467f8f81de6bc08ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WN2GURX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH3pPPzgZVYDJS6ZzRmvY6kXqvwMNn2LqDxFZH5G2sl7AiEAi3%2F3c8eRVGmiXWAtpqAptYvgOEZBtjrQh68pgh3c71gqiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFPPE%2F65DhfvD%2FEpayrcA8lG%2BBrSCHKph6fhqCf2pneoTxnN%2B2Eq4cdtruXWOP495M0BUJiOXw4ASvTXL6RsMMDMpkCtMCmbgsGAJ5r%2Bei2xrYS%2FnNHkvPBfvFv3EghKtEkaOB2BxP5XI0nbyBGvxdxkE6mjPIkh5qmg8K%2F5RIDe4JHKT313iFCEAGgg0Hs04%2FHwYyIOxrIXRjedKK%2FohhiiPnFIeXUHtQ2j98d%2BNEg5Zd6DSdC4t1eIgYpPwk46yb7Nzp6gqR4tKwaDnmlJk9y4yXUCNS2wNtH1oA%2BjBEifUqx6%2Bp0rsTYZmtgYgVhtH6z875fdTCgnjq5j8TnYT9r18tomX39fgbgsw3SpuCuVqnzWZ3PIQ5cgaa0D7LGTLNsVCcrefu%2BQ1FHBxKx2RVlMRolsuxV7OdjaVBWE3DNhO%2FhFTmZKLtK4dwHUiRUIbbPXvGhnhUWnbQ5w6rmszTgwEeVWCpN1kKwXb2Ynl%2F%2FOjFZLzUMbSDqijzaMI6Qcf2rOTIT1HnRUjpd2z2m1wycOrxctxFyVeM5iRYnpVdKFizo4gKAz1G1bu4%2FNbXmUYxix5A01l5FSzskUNIGziWIip5iLiPrDLW2cSfOACCenEH2j5dx3MEhXUZ1CmKoNgRWfAAhzLUw%2BzlmDMM%2Fk%2F7wGOqUB0eobe6hXrlXYFAkm32DZfqhPoFwdTrvtyuP1E7B50EQudcoCooN0cs3hONb3cJjmZK%2F6bLFy0DisReuSmvLl46zcdUqpctSASYt2qymXz87CgCUOTdfve9Ze6AoSSQOFFgdXo6GPWirSKzIUHaYDnYJPGLisLpyznXhIW5aiBBk5ZxRafjlq5kELgOYMHyU%2F7UplL5d8RX5l2FgrXvxaDe9ceH%2FP&X-Amz-Signature=bd978c0360771f3cb44d9c6a693ad53aa8b08b547a61543613fd2d4c22b9a083&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WN2GURX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH3pPPzgZVYDJS6ZzRmvY6kXqvwMNn2LqDxFZH5G2sl7AiEAi3%2F3c8eRVGmiXWAtpqAptYvgOEZBtjrQh68pgh3c71gqiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFPPE%2F65DhfvD%2FEpayrcA8lG%2BBrSCHKph6fhqCf2pneoTxnN%2B2Eq4cdtruXWOP495M0BUJiOXw4ASvTXL6RsMMDMpkCtMCmbgsGAJ5r%2Bei2xrYS%2FnNHkvPBfvFv3EghKtEkaOB2BxP5XI0nbyBGvxdxkE6mjPIkh5qmg8K%2F5RIDe4JHKT313iFCEAGgg0Hs04%2FHwYyIOxrIXRjedKK%2FohhiiPnFIeXUHtQ2j98d%2BNEg5Zd6DSdC4t1eIgYpPwk46yb7Nzp6gqR4tKwaDnmlJk9y4yXUCNS2wNtH1oA%2BjBEifUqx6%2Bp0rsTYZmtgYgVhtH6z875fdTCgnjq5j8TnYT9r18tomX39fgbgsw3SpuCuVqnzWZ3PIQ5cgaa0D7LGTLNsVCcrefu%2BQ1FHBxKx2RVlMRolsuxV7OdjaVBWE3DNhO%2FhFTmZKLtK4dwHUiRUIbbPXvGhnhUWnbQ5w6rmszTgwEeVWCpN1kKwXb2Ynl%2F%2FOjFZLzUMbSDqijzaMI6Qcf2rOTIT1HnRUjpd2z2m1wycOrxctxFyVeM5iRYnpVdKFizo4gKAz1G1bu4%2FNbXmUYxix5A01l5FSzskUNIGziWIip5iLiPrDLW2cSfOACCenEH2j5dx3MEhXUZ1CmKoNgRWfAAhzLUw%2BzlmDMM%2Fk%2F7wGOqUB0eobe6hXrlXYFAkm32DZfqhPoFwdTrvtyuP1E7B50EQudcoCooN0cs3hONb3cJjmZK%2F6bLFy0DisReuSmvLl46zcdUqpctSASYt2qymXz87CgCUOTdfve9Ze6AoSSQOFFgdXo6GPWirSKzIUHaYDnYJPGLisLpyznXhIW5aiBBk5ZxRafjlq5kELgOYMHyU%2F7UplL5d8RX5l2FgrXvxaDe9ceH%2FP&X-Amz-Signature=f2b770241e045f9aa561d57e2ebf50197a59999684902ce8fffb8180153611d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WN2GURX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH3pPPzgZVYDJS6ZzRmvY6kXqvwMNn2LqDxFZH5G2sl7AiEAi3%2F3c8eRVGmiXWAtpqAptYvgOEZBtjrQh68pgh3c71gqiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFPPE%2F65DhfvD%2FEpayrcA8lG%2BBrSCHKph6fhqCf2pneoTxnN%2B2Eq4cdtruXWOP495M0BUJiOXw4ASvTXL6RsMMDMpkCtMCmbgsGAJ5r%2Bei2xrYS%2FnNHkvPBfvFv3EghKtEkaOB2BxP5XI0nbyBGvxdxkE6mjPIkh5qmg8K%2F5RIDe4JHKT313iFCEAGgg0Hs04%2FHwYyIOxrIXRjedKK%2FohhiiPnFIeXUHtQ2j98d%2BNEg5Zd6DSdC4t1eIgYpPwk46yb7Nzp6gqR4tKwaDnmlJk9y4yXUCNS2wNtH1oA%2BjBEifUqx6%2Bp0rsTYZmtgYgVhtH6z875fdTCgnjq5j8TnYT9r18tomX39fgbgsw3SpuCuVqnzWZ3PIQ5cgaa0D7LGTLNsVCcrefu%2BQ1FHBxKx2RVlMRolsuxV7OdjaVBWE3DNhO%2FhFTmZKLtK4dwHUiRUIbbPXvGhnhUWnbQ5w6rmszTgwEeVWCpN1kKwXb2Ynl%2F%2FOjFZLzUMbSDqijzaMI6Qcf2rOTIT1HnRUjpd2z2m1wycOrxctxFyVeM5iRYnpVdKFizo4gKAz1G1bu4%2FNbXmUYxix5A01l5FSzskUNIGziWIip5iLiPrDLW2cSfOACCenEH2j5dx3MEhXUZ1CmKoNgRWfAAhzLUw%2BzlmDMM%2Fk%2F7wGOqUB0eobe6hXrlXYFAkm32DZfqhPoFwdTrvtyuP1E7B50EQudcoCooN0cs3hONb3cJjmZK%2F6bLFy0DisReuSmvLl46zcdUqpctSASYt2qymXz87CgCUOTdfve9Ze6AoSSQOFFgdXo6GPWirSKzIUHaYDnYJPGLisLpyznXhIW5aiBBk5ZxRafjlq5kELgOYMHyU%2F7UplL5d8RX5l2FgrXvxaDe9ceH%2FP&X-Amz-Signature=be556be86020a3d6c480e3a6b19b156657ae7e58a2e1330ba1e85ebc050b6798&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WN2GURX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH3pPPzgZVYDJS6ZzRmvY6kXqvwMNn2LqDxFZH5G2sl7AiEAi3%2F3c8eRVGmiXWAtpqAptYvgOEZBtjrQh68pgh3c71gqiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFPPE%2F65DhfvD%2FEpayrcA8lG%2BBrSCHKph6fhqCf2pneoTxnN%2B2Eq4cdtruXWOP495M0BUJiOXw4ASvTXL6RsMMDMpkCtMCmbgsGAJ5r%2Bei2xrYS%2FnNHkvPBfvFv3EghKtEkaOB2BxP5XI0nbyBGvxdxkE6mjPIkh5qmg8K%2F5RIDe4JHKT313iFCEAGgg0Hs04%2FHwYyIOxrIXRjedKK%2FohhiiPnFIeXUHtQ2j98d%2BNEg5Zd6DSdC4t1eIgYpPwk46yb7Nzp6gqR4tKwaDnmlJk9y4yXUCNS2wNtH1oA%2BjBEifUqx6%2Bp0rsTYZmtgYgVhtH6z875fdTCgnjq5j8TnYT9r18tomX39fgbgsw3SpuCuVqnzWZ3PIQ5cgaa0D7LGTLNsVCcrefu%2BQ1FHBxKx2RVlMRolsuxV7OdjaVBWE3DNhO%2FhFTmZKLtK4dwHUiRUIbbPXvGhnhUWnbQ5w6rmszTgwEeVWCpN1kKwXb2Ynl%2F%2FOjFZLzUMbSDqijzaMI6Qcf2rOTIT1HnRUjpd2z2m1wycOrxctxFyVeM5iRYnpVdKFizo4gKAz1G1bu4%2FNbXmUYxix5A01l5FSzskUNIGziWIip5iLiPrDLW2cSfOACCenEH2j5dx3MEhXUZ1CmKoNgRWfAAhzLUw%2BzlmDMM%2Fk%2F7wGOqUB0eobe6hXrlXYFAkm32DZfqhPoFwdTrvtyuP1E7B50EQudcoCooN0cs3hONb3cJjmZK%2F6bLFy0DisReuSmvLl46zcdUqpctSASYt2qymXz87CgCUOTdfve9Ze6AoSSQOFFgdXo6GPWirSKzIUHaYDnYJPGLisLpyznXhIW5aiBBk5ZxRafjlq5kELgOYMHyU%2F7UplL5d8RX5l2FgrXvxaDe9ceH%2FP&X-Amz-Signature=46319ba90a4a1c94c65bf0a6dc83f3b08ae06ebf078bfee6f5a10f0e57044b0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WN2GURX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH3pPPzgZVYDJS6ZzRmvY6kXqvwMNn2LqDxFZH5G2sl7AiEAi3%2F3c8eRVGmiXWAtpqAptYvgOEZBtjrQh68pgh3c71gqiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFPPE%2F65DhfvD%2FEpayrcA8lG%2BBrSCHKph6fhqCf2pneoTxnN%2B2Eq4cdtruXWOP495M0BUJiOXw4ASvTXL6RsMMDMpkCtMCmbgsGAJ5r%2Bei2xrYS%2FnNHkvPBfvFv3EghKtEkaOB2BxP5XI0nbyBGvxdxkE6mjPIkh5qmg8K%2F5RIDe4JHKT313iFCEAGgg0Hs04%2FHwYyIOxrIXRjedKK%2FohhiiPnFIeXUHtQ2j98d%2BNEg5Zd6DSdC4t1eIgYpPwk46yb7Nzp6gqR4tKwaDnmlJk9y4yXUCNS2wNtH1oA%2BjBEifUqx6%2Bp0rsTYZmtgYgVhtH6z875fdTCgnjq5j8TnYT9r18tomX39fgbgsw3SpuCuVqnzWZ3PIQ5cgaa0D7LGTLNsVCcrefu%2BQ1FHBxKx2RVlMRolsuxV7OdjaVBWE3DNhO%2FhFTmZKLtK4dwHUiRUIbbPXvGhnhUWnbQ5w6rmszTgwEeVWCpN1kKwXb2Ynl%2F%2FOjFZLzUMbSDqijzaMI6Qcf2rOTIT1HnRUjpd2z2m1wycOrxctxFyVeM5iRYnpVdKFizo4gKAz1G1bu4%2FNbXmUYxix5A01l5FSzskUNIGziWIip5iLiPrDLW2cSfOACCenEH2j5dx3MEhXUZ1CmKoNgRWfAAhzLUw%2BzlmDMM%2Fk%2F7wGOqUB0eobe6hXrlXYFAkm32DZfqhPoFwdTrvtyuP1E7B50EQudcoCooN0cs3hONb3cJjmZK%2F6bLFy0DisReuSmvLl46zcdUqpctSASYt2qymXz87CgCUOTdfve9Ze6AoSSQOFFgdXo6GPWirSKzIUHaYDnYJPGLisLpyznXhIW5aiBBk5ZxRafjlq5kELgOYMHyU%2F7UplL5d8RX5l2FgrXvxaDe9ceH%2FP&X-Amz-Signature=129f1dcf298dd7e2ad4ebe84decb8dd3cc2cf4c2178b228def8e1bbbf6778b72&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WN2GURX%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH3pPPzgZVYDJS6ZzRmvY6kXqvwMNn2LqDxFZH5G2sl7AiEAi3%2F3c8eRVGmiXWAtpqAptYvgOEZBtjrQh68pgh3c71gqiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFPPE%2F65DhfvD%2FEpayrcA8lG%2BBrSCHKph6fhqCf2pneoTxnN%2B2Eq4cdtruXWOP495M0BUJiOXw4ASvTXL6RsMMDMpkCtMCmbgsGAJ5r%2Bei2xrYS%2FnNHkvPBfvFv3EghKtEkaOB2BxP5XI0nbyBGvxdxkE6mjPIkh5qmg8K%2F5RIDe4JHKT313iFCEAGgg0Hs04%2FHwYyIOxrIXRjedKK%2FohhiiPnFIeXUHtQ2j98d%2BNEg5Zd6DSdC4t1eIgYpPwk46yb7Nzp6gqR4tKwaDnmlJk9y4yXUCNS2wNtH1oA%2BjBEifUqx6%2Bp0rsTYZmtgYgVhtH6z875fdTCgnjq5j8TnYT9r18tomX39fgbgsw3SpuCuVqnzWZ3PIQ5cgaa0D7LGTLNsVCcrefu%2BQ1FHBxKx2RVlMRolsuxV7OdjaVBWE3DNhO%2FhFTmZKLtK4dwHUiRUIbbPXvGhnhUWnbQ5w6rmszTgwEeVWCpN1kKwXb2Ynl%2F%2FOjFZLzUMbSDqijzaMI6Qcf2rOTIT1HnRUjpd2z2m1wycOrxctxFyVeM5iRYnpVdKFizo4gKAz1G1bu4%2FNbXmUYxix5A01l5FSzskUNIGziWIip5iLiPrDLW2cSfOACCenEH2j5dx3MEhXUZ1CmKoNgRWfAAhzLUw%2BzlmDMM%2Fk%2F7wGOqUB0eobe6hXrlXYFAkm32DZfqhPoFwdTrvtyuP1E7B50EQudcoCooN0cs3hONb3cJjmZK%2F6bLFy0DisReuSmvLl46zcdUqpctSASYt2qymXz87CgCUOTdfve9Ze6AoSSQOFFgdXo6GPWirSKzIUHaYDnYJPGLisLpyznXhIW5aiBBk5ZxRafjlq5kELgOYMHyU%2F7UplL5d8RX5l2FgrXvxaDe9ceH%2FP&X-Amz-Signature=bdf8a376a77db9ed3be3cb51e5a4e203cc179de91555fe8d514ce7b81675c281&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXAJPH3J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqDjXltfp6ctLKQAirW6izWkr96jCxh7tEkZ4BPpQDOQIhAJ6be5nxisWXPwYCUlDhiFAydPA4%2F3FndiYryWh8ohWrKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6yHRh57qFVpJdwKwq3AOvOZrq3Ksc1X4vxgNVBH08541EZgfJxiriHuJC2rwcyKD%2FcH4sMbveVEwmOcVIFK8ZynemKJI6tzema9dJ%2BfEpbpfiU1nCuLygDxTOFXEvVW7EO2q43L7vjibGlg6n3UOjyicSmkdX%2BywHtGfkyDq2qoT3uUevoWQAAaaoxEi1F39iJhwjahoIzcJBWaCVZM3MTXC0HuMFA5TnEmo1%2B16BLN1cQdiiJl4fraerJ7Y7Tvj0aiHxIt4T%2B%2F2w7ssu6in%2FyCiGC2aqQf7QWmCzk1p%2FECJ6Sb6HsRwZnDamPKJl08WKwXXmqNGU6yvAsAh1O02W5Pl%2F7x1WSG%2FFWWjbCeKduLFOVhP5PKWqHfa5BnpkIKCp1tYdsW6BrhmXXhY5rzQgC09s3aTFhnpLUaJxiOJIPir4qqlaBgqE5alRHzZMAxnp%2BMDFHEClstovM1CIwP4CTPEJ8ABX27cpTl1aPt%2BxDfgfNzD7FMWBL%2B4EkhszbWZV2j7EIPrlPMf7yZRxJQqwTT02KAxSknav3HLvXKFlJT3vc4NcUz2yJxjCFS5bY0gdREP%2Ft%2FG%2F3KuXLv14gR45shGXP3vKxJCNGzCE4c5eMlW7R259VYfCBAngELpTaKda4k0X40Vk5vLkLTDA5f%2B8BjqkASoniNyfSgw11qhZg4mPQBnNVKu2aPQsTAeqQ70IxzTM7KTccwmdsYMmitGNbafDvhRlTpEk1%2Ba8wQz2%2FFlaF6BIGetAlrbttM1qQ7ecw8HrD%2FA9tjaeOKRiE%2BgQCUbkl5h1G9ql3rCEerZVlnuV5UPAa4X6rkRfM0SPFmQKfX17PTS97QNQywzf11VTFVxujAfHhQ34l%2B0kRF7OjTJDCaXSWgOc&X-Amz-Signature=324c2938a6475a21912973cb2081c7a254d687f4183af2f9807aae5d56f76c26&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEFFHW6P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICwkNlo34V%2BFNAXoLC665c2MgGz%2Bfy%2BXmroXxwxvzLUbAiAFxdwKdTEtpYj22VW3ubKazBhaObdaV5BToUVqilcS5CqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM10W%2FDybAVdfBkSgHKtwDbos%2BeFrLeMwXal2RK%2BOWqPqZvElXQIAisjI7WpuiOi1X%2FpOHF6alNNZAh%2FvIuNFy%2BKrg0fdnXtcjN0bMVBC0wxP%2BScwjvUaWHSzgXubw85DfogRuwvP95jYkles%2BeiHUMc7opLcAPQSyB05E3n6uWKDC%2BJgySWsGCmvYDrf2ZOyHGXMKy2sZsyWeQFS7Q8ce8LIbUWNCX6ADhZfbTatu1pbgUbaU2mHwzGy4xD7GwbSZ5dnd4Ov8R119fa4KEEZjsj6BhUFqcwgQWfl5XrRu82Kf03cjNLY0gtFpAztwCYil6cDOIFLopEvgKpc1hyFL3IczQjxl5tBM7sUuhI1X8IuUBwP68TFZkIoe0vymgTz77wiSMVh8KFjiEyVl6f2Beo3zt2T%2BNfry9Bqrald2kOuR7Djtcj7nMsFa%2BrLzRrYgyrq%2BcaprgjTA8CVg202Hq8hD08pAfWNDLFGokapCEepwvoVXEfu677aWTQdqIpjCZyE9xnzIS6vbqY4Hc8qtoJju16LgnQ4gNOKsJClP6vsnAB3HYJrtAMD%2FUzhvt5vxHopiScCpIaRIU63qVQ%2BvCs8N%2FlvYh3u%2FtZuRvEYJFyVZF%2BkShOR0iuv303z5HAAXTevF%2BzY%2BnRWTXKswsOT%2FvAY6pgGXytmj8Ko%2FGPcSLEYJIlWtuuLoumAiZpoRp8y3G7BSopFSU2Lj%2B%2BbMyF%2FjrVkIgAJINOnxS%2B8NAEFNH9cAvI0hRgBte0b5bvXsrRLsyzo5zizvO7AvtFOrSDQgx2f%2FXBLMEzuTnQ8kLo%2B2tmgHXutK7kVLBoGCLIpbwyPXcIP%2B%2B5yl7FT5YxjNNvr2lHLfTVeV4dT01fsF7zuiaToSP35jDJ21UHnQ&X-Amz-Signature=6aa117692a2db8e4c5ce5a0b9f6f4ece25b096ca78887618ca3887c6344ceebc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNZ65MSW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGdGnnMKl6sgCvBCadgBcamRsm0jL402u8Tur4U97IMjAiB4dPcCkvYBmWGJK1hmlhbBSEC%2BvLsL86yai9YlpEUlsyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgcJLKygOFDUHg1MWKtwD%2Ft7FLxdUwOmOrU5Qsy0bxFCfW%2B7wPmODLT6U4R60HLZzuEy4LJGXKywm33AX2Zq22mj3W4DUlPXikbQEYsidlWKgtOze2PWOHOM4jUlS%2Feifd4X62stDq9vmKFWMAaKWJgrgHW%2F93bHBFCl8GUPgr7kLE4rhY1D%2FclKtBEFxpBcPvZwNTcF8NJ%2FW4b8e8uoVH8uLTBAvAIpizSMQ%2BSk3Di9%2FKHf5p06zvEjIcOTD7nxBQUnfAuOwj4DNlOYnGro1g4DdTO78hZxnw0YLhzWz2zddHoccGgaPoCF9%2FclmhbMmVfpq9H%2F5CdGuAbbb2qa%2FkpsLGGfI8P62JhXchvnR7WeKsxMBTZByKpujVdJOjnwSf3JZarMKB1iqEMTE%2BWaArK%2BSVhnCMjsB9eVFgTNs4sNfaeLe9ORpVLZ310AZsr459DBIsmxLbOGukzsXSvHjjswfGm7Czm%2BYJUdEJDeBhCCs8qLYn%2BoBWZHrDEfw1JAqdUIrZeZU6el%2FUFLZEJ7BdYOP4etOfZ3i57D6Nqx%2FHmwCOZA2F3GzB1KPJo4Nva69lKxjtLuNAGYop4sGa4jS%2FZ3QqRKU8qJWPmA8ft3nWztXSZSDUA5LWU7bE49c4pzW5IYqqre0edinXWwwruT%2FvAY6pgHXUnd5aCgKOA9PiOWtkfbBYBtThl9Ya0x543dpweAs8KjwF8%2FeTG9hcM%2BVH15O44RqG%2BTV7TiSHLmlfAgCX67y%2BM7R%2FhYTRDic7W7oQ%2FbZ3u29kSHGJEMtnCNGg1UvYzJ%2FpeFbm1UyRm0KxeX9QVxNdvg4koL7JOtZQGeqcOIZVXSvBjfPNvzcn3mNnUhVaJrSsiih55%2BSJ%2Fo3q6Ksr5FOlfg0GqUv&X-Amz-Signature=10da8c0805d876be1855aa4aec4d7dfe69f13154a8a05404ea7919116d63307f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNZ65MSW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGdGnnMKl6sgCvBCadgBcamRsm0jL402u8Tur4U97IMjAiB4dPcCkvYBmWGJK1hmlhbBSEC%2BvLsL86yai9YlpEUlsyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgcJLKygOFDUHg1MWKtwD%2Ft7FLxdUwOmOrU5Qsy0bxFCfW%2B7wPmODLT6U4R60HLZzuEy4LJGXKywm33AX2Zq22mj3W4DUlPXikbQEYsidlWKgtOze2PWOHOM4jUlS%2Feifd4X62stDq9vmKFWMAaKWJgrgHW%2F93bHBFCl8GUPgr7kLE4rhY1D%2FclKtBEFxpBcPvZwNTcF8NJ%2FW4b8e8uoVH8uLTBAvAIpizSMQ%2BSk3Di9%2FKHf5p06zvEjIcOTD7nxBQUnfAuOwj4DNlOYnGro1g4DdTO78hZxnw0YLhzWz2zddHoccGgaPoCF9%2FclmhbMmVfpq9H%2F5CdGuAbbb2qa%2FkpsLGGfI8P62JhXchvnR7WeKsxMBTZByKpujVdJOjnwSf3JZarMKB1iqEMTE%2BWaArK%2BSVhnCMjsB9eVFgTNs4sNfaeLe9ORpVLZ310AZsr459DBIsmxLbOGukzsXSvHjjswfGm7Czm%2BYJUdEJDeBhCCs8qLYn%2BoBWZHrDEfw1JAqdUIrZeZU6el%2FUFLZEJ7BdYOP4etOfZ3i57D6Nqx%2FHmwCOZA2F3GzB1KPJo4Nva69lKxjtLuNAGYop4sGa4jS%2FZ3QqRKU8qJWPmA8ft3nWztXSZSDUA5LWU7bE49c4pzW5IYqqre0edinXWwwruT%2FvAY6pgHXUnd5aCgKOA9PiOWtkfbBYBtThl9Ya0x543dpweAs8KjwF8%2FeTG9hcM%2BVH15O44RqG%2BTV7TiSHLmlfAgCX67y%2BM7R%2FhYTRDic7W7oQ%2FbZ3u29kSHGJEMtnCNGg1UvYzJ%2FpeFbm1UyRm0KxeX9QVxNdvg4koL7JOtZQGeqcOIZVXSvBjfPNvzcn3mNnUhVaJrSsiih55%2BSJ%2Fo3q6Ksr5FOlfg0GqUv&X-Amz-Signature=ae2f7976031439e878ded8c1609c9aa33c9bc79abe7947a25ff9518232b43d57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
