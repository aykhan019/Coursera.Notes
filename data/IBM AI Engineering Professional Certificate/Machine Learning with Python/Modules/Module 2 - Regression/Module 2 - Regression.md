

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVUD622Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIERj2AXX7f9kL54jy8vO3zdeJ%2F4dj6Ik5s2xSmPNsFjrAiEArCj5h0rW%2BQCSb8H6IteL%2Fedr%2Bc1LBzYaUFpLcVNa1owqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHEkv8%2BlXmrT7ziNyrcAyfOJxrLBI8AtfZaMYqWcFJw745joqOGx0fpjBn00gmomYLwE0Uc7RKe6FjcHNr3HrYRi6F3h7opk46coXxZp64XWTmyhTdjCu3vD9PCxGD67iuUdKjGS0s2yD%2FrJXN1BLpbdehBsi%2BUTvc7qEPFm8R8jGswoKm7ZDDoVtegpO6FmMJl00JGTALqkfChKaonIxZX%2Fr5PLERwTJMtg94G0P0qKC3dVkVG3ZBHJGDiSh9kU29YvHljdVjjXUb1%2B8d47rvzM%2Bz40zYegz2PjCWc7GBNBIc%2BOcE4rLIKcmrrawtHWuGGeBGrU286%2Bep%2B%2FbSIQyiTiJa5HYNcMUuHhJAK6Y%2Fg8qbSzBwXTXyTL8MHKiCRoB15CNyXWx0SF9P51lwilcAMERyMz1UdzSPpDUJEfJS7xk%2FdTIsArQmzdb9K%2BZI0E72%2FBP7HVb2921ucMhjBK2f4jCc1pVkqrm5dlSZwQR4i87yz2rC2Jb6G88YM7ibEFSHSGNMfWV2o2yRlLPnXdVGuExZTId%2BnFtxaSM7LF1B6E%2Bz30PEiKWUUfTZIGhztZ8HlnX7ztOg61mzvgJ4WqSZUYjh5Q9T3oE3eKW1EauQw%2BE4M8fsjcJdXP9WGaOasUcCrcXnCrr%2Bxo3W5MIiWm70GOqUBGyENiw2fU2FqWgFobF3ZblYDcGFPvwOv0ZcGE6FtjyHdfsh7kXLcuqkJSPgYjrq751S0vjMKpKxFCIQDZ6NxffsobsaAT6YrzqZtXyTo60MsI040gbusckuozPVeKHFZ7DuNZiF0rA4IVV0qFg2B0xpXqgTxJQ3N5%2FSkXNMv6uOauuC0QkMeq8v%2F%2BXqHYO0S91%2FPY71TSwqadFK9PuD8eJhd0GYm&X-Amz-Signature=fe746c808de38ffbf3498ab2790df57ea53edeb53f62412b8ef74c88358f8b85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVUD622Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIERj2AXX7f9kL54jy8vO3zdeJ%2F4dj6Ik5s2xSmPNsFjrAiEArCj5h0rW%2BQCSb8H6IteL%2Fedr%2Bc1LBzYaUFpLcVNa1owqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHEkv8%2BlXmrT7ziNyrcAyfOJxrLBI8AtfZaMYqWcFJw745joqOGx0fpjBn00gmomYLwE0Uc7RKe6FjcHNr3HrYRi6F3h7opk46coXxZp64XWTmyhTdjCu3vD9PCxGD67iuUdKjGS0s2yD%2FrJXN1BLpbdehBsi%2BUTvc7qEPFm8R8jGswoKm7ZDDoVtegpO6FmMJl00JGTALqkfChKaonIxZX%2Fr5PLERwTJMtg94G0P0qKC3dVkVG3ZBHJGDiSh9kU29YvHljdVjjXUb1%2B8d47rvzM%2Bz40zYegz2PjCWc7GBNBIc%2BOcE4rLIKcmrrawtHWuGGeBGrU286%2Bep%2B%2FbSIQyiTiJa5HYNcMUuHhJAK6Y%2Fg8qbSzBwXTXyTL8MHKiCRoB15CNyXWx0SF9P51lwilcAMERyMz1UdzSPpDUJEfJS7xk%2FdTIsArQmzdb9K%2BZI0E72%2FBP7HVb2921ucMhjBK2f4jCc1pVkqrm5dlSZwQR4i87yz2rC2Jb6G88YM7ibEFSHSGNMfWV2o2yRlLPnXdVGuExZTId%2BnFtxaSM7LF1B6E%2Bz30PEiKWUUfTZIGhztZ8HlnX7ztOg61mzvgJ4WqSZUYjh5Q9T3oE3eKW1EauQw%2BE4M8fsjcJdXP9WGaOasUcCrcXnCrr%2Bxo3W5MIiWm70GOqUBGyENiw2fU2FqWgFobF3ZblYDcGFPvwOv0ZcGE6FtjyHdfsh7kXLcuqkJSPgYjrq751S0vjMKpKxFCIQDZ6NxffsobsaAT6YrzqZtXyTo60MsI040gbusckuozPVeKHFZ7DuNZiF0rA4IVV0qFg2B0xpXqgTxJQ3N5%2FSkXNMv6uOauuC0QkMeq8v%2F%2BXqHYO0S91%2FPY71TSwqadFK9PuD8eJhd0GYm&X-Amz-Signature=4a3c2f39e2c2594f5aff64eb58fbba1d10a235ec789b8ac3e656a0405c9bcf99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVUD622Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIERj2AXX7f9kL54jy8vO3zdeJ%2F4dj6Ik5s2xSmPNsFjrAiEArCj5h0rW%2BQCSb8H6IteL%2Fedr%2Bc1LBzYaUFpLcVNa1owqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHEkv8%2BlXmrT7ziNyrcAyfOJxrLBI8AtfZaMYqWcFJw745joqOGx0fpjBn00gmomYLwE0Uc7RKe6FjcHNr3HrYRi6F3h7opk46coXxZp64XWTmyhTdjCu3vD9PCxGD67iuUdKjGS0s2yD%2FrJXN1BLpbdehBsi%2BUTvc7qEPFm8R8jGswoKm7ZDDoVtegpO6FmMJl00JGTALqkfChKaonIxZX%2Fr5PLERwTJMtg94G0P0qKC3dVkVG3ZBHJGDiSh9kU29YvHljdVjjXUb1%2B8d47rvzM%2Bz40zYegz2PjCWc7GBNBIc%2BOcE4rLIKcmrrawtHWuGGeBGrU286%2Bep%2B%2FbSIQyiTiJa5HYNcMUuHhJAK6Y%2Fg8qbSzBwXTXyTL8MHKiCRoB15CNyXWx0SF9P51lwilcAMERyMz1UdzSPpDUJEfJS7xk%2FdTIsArQmzdb9K%2BZI0E72%2FBP7HVb2921ucMhjBK2f4jCc1pVkqrm5dlSZwQR4i87yz2rC2Jb6G88YM7ibEFSHSGNMfWV2o2yRlLPnXdVGuExZTId%2BnFtxaSM7LF1B6E%2Bz30PEiKWUUfTZIGhztZ8HlnX7ztOg61mzvgJ4WqSZUYjh5Q9T3oE3eKW1EauQw%2BE4M8fsjcJdXP9WGaOasUcCrcXnCrr%2Bxo3W5MIiWm70GOqUBGyENiw2fU2FqWgFobF3ZblYDcGFPvwOv0ZcGE6FtjyHdfsh7kXLcuqkJSPgYjrq751S0vjMKpKxFCIQDZ6NxffsobsaAT6YrzqZtXyTo60MsI040gbusckuozPVeKHFZ7DuNZiF0rA4IVV0qFg2B0xpXqgTxJQ3N5%2FSkXNMv6uOauuC0QkMeq8v%2F%2BXqHYO0S91%2FPY71TSwqadFK9PuD8eJhd0GYm&X-Amz-Signature=3824cfa7a3af161c1ba0128f171e1edae3d8d7a33944c12de23b20feaf69664b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVUD622Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIERj2AXX7f9kL54jy8vO3zdeJ%2F4dj6Ik5s2xSmPNsFjrAiEArCj5h0rW%2BQCSb8H6IteL%2Fedr%2Bc1LBzYaUFpLcVNa1owqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHEkv8%2BlXmrT7ziNyrcAyfOJxrLBI8AtfZaMYqWcFJw745joqOGx0fpjBn00gmomYLwE0Uc7RKe6FjcHNr3HrYRi6F3h7opk46coXxZp64XWTmyhTdjCu3vD9PCxGD67iuUdKjGS0s2yD%2FrJXN1BLpbdehBsi%2BUTvc7qEPFm8R8jGswoKm7ZDDoVtegpO6FmMJl00JGTALqkfChKaonIxZX%2Fr5PLERwTJMtg94G0P0qKC3dVkVG3ZBHJGDiSh9kU29YvHljdVjjXUb1%2B8d47rvzM%2Bz40zYegz2PjCWc7GBNBIc%2BOcE4rLIKcmrrawtHWuGGeBGrU286%2Bep%2B%2FbSIQyiTiJa5HYNcMUuHhJAK6Y%2Fg8qbSzBwXTXyTL8MHKiCRoB15CNyXWx0SF9P51lwilcAMERyMz1UdzSPpDUJEfJS7xk%2FdTIsArQmzdb9K%2BZI0E72%2FBP7HVb2921ucMhjBK2f4jCc1pVkqrm5dlSZwQR4i87yz2rC2Jb6G88YM7ibEFSHSGNMfWV2o2yRlLPnXdVGuExZTId%2BnFtxaSM7LF1B6E%2Bz30PEiKWUUfTZIGhztZ8HlnX7ztOg61mzvgJ4WqSZUYjh5Q9T3oE3eKW1EauQw%2BE4M8fsjcJdXP9WGaOasUcCrcXnCrr%2Bxo3W5MIiWm70GOqUBGyENiw2fU2FqWgFobF3ZblYDcGFPvwOv0ZcGE6FtjyHdfsh7kXLcuqkJSPgYjrq751S0vjMKpKxFCIQDZ6NxffsobsaAT6YrzqZtXyTo60MsI040gbusckuozPVeKHFZ7DuNZiF0rA4IVV0qFg2B0xpXqgTxJQ3N5%2FSkXNMv6uOauuC0QkMeq8v%2F%2BXqHYO0S91%2FPY71TSwqadFK9PuD8eJhd0GYm&X-Amz-Signature=5d3ffac9dc8cb5328d46fb49b1d852d1c2c9b48da4e3b2c6ba277f4f528e743b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVUD622Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIERj2AXX7f9kL54jy8vO3zdeJ%2F4dj6Ik5s2xSmPNsFjrAiEArCj5h0rW%2BQCSb8H6IteL%2Fedr%2Bc1LBzYaUFpLcVNa1owqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHEkv8%2BlXmrT7ziNyrcAyfOJxrLBI8AtfZaMYqWcFJw745joqOGx0fpjBn00gmomYLwE0Uc7RKe6FjcHNr3HrYRi6F3h7opk46coXxZp64XWTmyhTdjCu3vD9PCxGD67iuUdKjGS0s2yD%2FrJXN1BLpbdehBsi%2BUTvc7qEPFm8R8jGswoKm7ZDDoVtegpO6FmMJl00JGTALqkfChKaonIxZX%2Fr5PLERwTJMtg94G0P0qKC3dVkVG3ZBHJGDiSh9kU29YvHljdVjjXUb1%2B8d47rvzM%2Bz40zYegz2PjCWc7GBNBIc%2BOcE4rLIKcmrrawtHWuGGeBGrU286%2Bep%2B%2FbSIQyiTiJa5HYNcMUuHhJAK6Y%2Fg8qbSzBwXTXyTL8MHKiCRoB15CNyXWx0SF9P51lwilcAMERyMz1UdzSPpDUJEfJS7xk%2FdTIsArQmzdb9K%2BZI0E72%2FBP7HVb2921ucMhjBK2f4jCc1pVkqrm5dlSZwQR4i87yz2rC2Jb6G88YM7ibEFSHSGNMfWV2o2yRlLPnXdVGuExZTId%2BnFtxaSM7LF1B6E%2Bz30PEiKWUUfTZIGhztZ8HlnX7ztOg61mzvgJ4WqSZUYjh5Q9T3oE3eKW1EauQw%2BE4M8fsjcJdXP9WGaOasUcCrcXnCrr%2Bxo3W5MIiWm70GOqUBGyENiw2fU2FqWgFobF3ZblYDcGFPvwOv0ZcGE6FtjyHdfsh7kXLcuqkJSPgYjrq751S0vjMKpKxFCIQDZ6NxffsobsaAT6YrzqZtXyTo60MsI040gbusckuozPVeKHFZ7DuNZiF0rA4IVV0qFg2B0xpXqgTxJQ3N5%2FSkXNMv6uOauuC0QkMeq8v%2F%2BXqHYO0S91%2FPY71TSwqadFK9PuD8eJhd0GYm&X-Amz-Signature=d29a8c13a93f0dbfed71867d0a4329f4d389cc97dd08c19f1afb89c0e712b688&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVUD622Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIERj2AXX7f9kL54jy8vO3zdeJ%2F4dj6Ik5s2xSmPNsFjrAiEArCj5h0rW%2BQCSb8H6IteL%2Fedr%2Bc1LBzYaUFpLcVNa1owqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHEkv8%2BlXmrT7ziNyrcAyfOJxrLBI8AtfZaMYqWcFJw745joqOGx0fpjBn00gmomYLwE0Uc7RKe6FjcHNr3HrYRi6F3h7opk46coXxZp64XWTmyhTdjCu3vD9PCxGD67iuUdKjGS0s2yD%2FrJXN1BLpbdehBsi%2BUTvc7qEPFm8R8jGswoKm7ZDDoVtegpO6FmMJl00JGTALqkfChKaonIxZX%2Fr5PLERwTJMtg94G0P0qKC3dVkVG3ZBHJGDiSh9kU29YvHljdVjjXUb1%2B8d47rvzM%2Bz40zYegz2PjCWc7GBNBIc%2BOcE4rLIKcmrrawtHWuGGeBGrU286%2Bep%2B%2FbSIQyiTiJa5HYNcMUuHhJAK6Y%2Fg8qbSzBwXTXyTL8MHKiCRoB15CNyXWx0SF9P51lwilcAMERyMz1UdzSPpDUJEfJS7xk%2FdTIsArQmzdb9K%2BZI0E72%2FBP7HVb2921ucMhjBK2f4jCc1pVkqrm5dlSZwQR4i87yz2rC2Jb6G88YM7ibEFSHSGNMfWV2o2yRlLPnXdVGuExZTId%2BnFtxaSM7LF1B6E%2Bz30PEiKWUUfTZIGhztZ8HlnX7ztOg61mzvgJ4WqSZUYjh5Q9T3oE3eKW1EauQw%2BE4M8fsjcJdXP9WGaOasUcCrcXnCrr%2Bxo3W5MIiWm70GOqUBGyENiw2fU2FqWgFobF3ZblYDcGFPvwOv0ZcGE6FtjyHdfsh7kXLcuqkJSPgYjrq751S0vjMKpKxFCIQDZ6NxffsobsaAT6YrzqZtXyTo60MsI040gbusckuozPVeKHFZ7DuNZiF0rA4IVV0qFg2B0xpXqgTxJQ3N5%2FSkXNMv6uOauuC0QkMeq8v%2F%2BXqHYO0S91%2FPY71TSwqadFK9PuD8eJhd0GYm&X-Amz-Signature=9a1b8aab032efd610481461943ce315b696158e03d3492737481190a2efe53a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVUD622Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIERj2AXX7f9kL54jy8vO3zdeJ%2F4dj6Ik5s2xSmPNsFjrAiEArCj5h0rW%2BQCSb8H6IteL%2Fedr%2Bc1LBzYaUFpLcVNa1owqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHEkv8%2BlXmrT7ziNyrcAyfOJxrLBI8AtfZaMYqWcFJw745joqOGx0fpjBn00gmomYLwE0Uc7RKe6FjcHNr3HrYRi6F3h7opk46coXxZp64XWTmyhTdjCu3vD9PCxGD67iuUdKjGS0s2yD%2FrJXN1BLpbdehBsi%2BUTvc7qEPFm8R8jGswoKm7ZDDoVtegpO6FmMJl00JGTALqkfChKaonIxZX%2Fr5PLERwTJMtg94G0P0qKC3dVkVG3ZBHJGDiSh9kU29YvHljdVjjXUb1%2B8d47rvzM%2Bz40zYegz2PjCWc7GBNBIc%2BOcE4rLIKcmrrawtHWuGGeBGrU286%2Bep%2B%2FbSIQyiTiJa5HYNcMUuHhJAK6Y%2Fg8qbSzBwXTXyTL8MHKiCRoB15CNyXWx0SF9P51lwilcAMERyMz1UdzSPpDUJEfJS7xk%2FdTIsArQmzdb9K%2BZI0E72%2FBP7HVb2921ucMhjBK2f4jCc1pVkqrm5dlSZwQR4i87yz2rC2Jb6G88YM7ibEFSHSGNMfWV2o2yRlLPnXdVGuExZTId%2BnFtxaSM7LF1B6E%2Bz30PEiKWUUfTZIGhztZ8HlnX7ztOg61mzvgJ4WqSZUYjh5Q9T3oE3eKW1EauQw%2BE4M8fsjcJdXP9WGaOasUcCrcXnCrr%2Bxo3W5MIiWm70GOqUBGyENiw2fU2FqWgFobF3ZblYDcGFPvwOv0ZcGE6FtjyHdfsh7kXLcuqkJSPgYjrq751S0vjMKpKxFCIQDZ6NxffsobsaAT6YrzqZtXyTo60MsI040gbusckuozPVeKHFZ7DuNZiF0rA4IVV0qFg2B0xpXqgTxJQ3N5%2FSkXNMv6uOauuC0QkMeq8v%2F%2BXqHYO0S91%2FPY71TSwqadFK9PuD8eJhd0GYm&X-Amz-Signature=68864fc7d15051ee84edbe2732ac1593ec10c8325033f1bed1afbf3740a97d2f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVUD622Y%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIERj2AXX7f9kL54jy8vO3zdeJ%2F4dj6Ik5s2xSmPNsFjrAiEArCj5h0rW%2BQCSb8H6IteL%2Fedr%2Bc1LBzYaUFpLcVNa1owqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHEkv8%2BlXmrT7ziNyrcAyfOJxrLBI8AtfZaMYqWcFJw745joqOGx0fpjBn00gmomYLwE0Uc7RKe6FjcHNr3HrYRi6F3h7opk46coXxZp64XWTmyhTdjCu3vD9PCxGD67iuUdKjGS0s2yD%2FrJXN1BLpbdehBsi%2BUTvc7qEPFm8R8jGswoKm7ZDDoVtegpO6FmMJl00JGTALqkfChKaonIxZX%2Fr5PLERwTJMtg94G0P0qKC3dVkVG3ZBHJGDiSh9kU29YvHljdVjjXUb1%2B8d47rvzM%2Bz40zYegz2PjCWc7GBNBIc%2BOcE4rLIKcmrrawtHWuGGeBGrU286%2Bep%2B%2FbSIQyiTiJa5HYNcMUuHhJAK6Y%2Fg8qbSzBwXTXyTL8MHKiCRoB15CNyXWx0SF9P51lwilcAMERyMz1UdzSPpDUJEfJS7xk%2FdTIsArQmzdb9K%2BZI0E72%2FBP7HVb2921ucMhjBK2f4jCc1pVkqrm5dlSZwQR4i87yz2rC2Jb6G88YM7ibEFSHSGNMfWV2o2yRlLPnXdVGuExZTId%2BnFtxaSM7LF1B6E%2Bz30PEiKWUUfTZIGhztZ8HlnX7ztOg61mzvgJ4WqSZUYjh5Q9T3oE3eKW1EauQw%2BE4M8fsjcJdXP9WGaOasUcCrcXnCrr%2Bxo3W5MIiWm70GOqUBGyENiw2fU2FqWgFobF3ZblYDcGFPvwOv0ZcGE6FtjyHdfsh7kXLcuqkJSPgYjrq751S0vjMKpKxFCIQDZ6NxffsobsaAT6YrzqZtXyTo60MsI040gbusckuozPVeKHFZ7DuNZiF0rA4IVV0qFg2B0xpXqgTxJQ3N5%2FSkXNMv6uOauuC0QkMeq8v%2F%2BXqHYO0S91%2FPY71TSwqadFK9PuD8eJhd0GYm&X-Amz-Signature=bc9fe64360579c603dfe74cd038ffb78254546f079e8df6d6e6c61a194b69713&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PQU35K5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDQqrON8Sv%2BQ6SeDsPcMzoy49MXW0vXok2RHbJoctWzpgIhAJYa1F1IKXAaQJezl%2BzcTmSyfpPVjnjpgfGmj4TN%2B99YKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxSCuEpZQUKnMLeOZMq3APxnqWnJYT24KdLzqybwKFJG0baALqEyLpuktXQ3U8FTVT%2BoU1sN880qbVg2bjR5D8F1Ix3%2FWgt%2FrjmNms62Gu8wmZ6zr8ZCTRaKQnAUge5lyfxICGq3fnSn8N0eshl9LQ9smprZVdIotLR8NzdoQDalhm8jPPTZ17krTJR9aKZ2PnYhoMCPBoVcXUQ0Q4EZEqQpczrVsEbonAikblFzoLUeKLj8pkm%2BUtxhTIlLIgJJsVE5Re7WoEYFFlMjPWi4sPHeOpzzn6HCjQWVX2fnaTaAvQpckMY5PEIzQiim5vyoOripHrlq7Yy6NlwF7OBnTefgKkPBekXO%2FlArlTr6l2m02sOdbe0U1jknpGy0QPIxB2Yj%2BQnKsqVPoV7DY7vS9AXpjq%2B%2BQLAc7B8rG%2FJgaNk0DSDpbaeBZwLTl1WnLJ4wQeZK%2Be%2BG%2F14jnx2Fgv9zXYN45e6gkjdCy8A76ABzF6%2FmhJ0XVlfi8y907%2Fg3vh%2FZsA4B79md3C2Cgi6Qd4tuY9mkogi2k6CO%2BILyc4rjrxN94kPiM8ZBo9gENNJs7MOnbg0GjCNmx7lU1qVpr5xTrA8TNt75Tel8fgvwaFHtAtvyBA7J3RbUPVHDVnOCWZ6iU7fMd4tlZS%2BETq2GzDxlZu9BjqkAcEhIrVFOGuyCZK%2BjalCDoUifn3TkkBiGzTTRt%2BxtFWvylbWzY3CEZUcvza98f2WQUNn6Hdjlx1st2wz0mJs%2FqxsPWXilgLToaoAjap%2BHl6GIrnP8g67fIqPM5kKPW5V8KWOL6JYCfD3BnSr7rf0BlrGCzYEfbyxuYMjcOio9EWoqawZGGHu%2FW7XFyPs8PUt1mZ3tZMBw1T5B8OUZQcqwV7Q1GUm&X-Amz-Signature=dd1cd884fefd80628fec352bdead71f0f55246b71330e0018be989d9a4c88322&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WK7UOS6A%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQCls7%2FbwQM4acKD%2BOAwG7F4XYHSgBz4rtBmJ6pw0Idz8AIhAMkkKbgkBJIzX%2BlAVBQFUQd46e%2FT1dmUCVI2TLawEgyoKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzMiPk0ERpf76Vg8rIq3AMnbyt0pKtF%2BC30h5kG0z8skvz%2FZAZ4kvNKaGxV4zGbmta5jxI%2BmKs8THulMppEVbLAC6BlKQo%2BQ%2BTvNqENtRrwxtsfLrrdJuZ7RdMsKK%2FR5pIyAFSkpz3qiR5y7Y%2F4zJDLHU2q8sgAoerY96xxa91SP6Poqe2z21CdFqHPBCmLugSGlVtbNEpqNxvIhmYHRxmmCJY9e9GZgQBzY6vnq%2F5UvpC%2BXx4wYnxcNZ8aGooJkOAYUUPwiZWoQuDtTzu%2BWAbTCbsQxFhRh%2BgBmRsUZ9YgdY37K0Z79VGyyn5i%2BMKB4goz9qWu8cWzTiC3zwSlBoiOk%2FQC7S8nlyM9CZJNfmb0URwIvGNfk%2FfP8xxcA2XNXyOio5HYhkAwB2%2F4gNwe0uPKjVqESljO6thUz11ElP5CQCZDobpD5AE4Vcop7sslAMXLF55B%2Fvvomr5B%2BH1zXM2zTCd9BCSoa2DjMMUF%2F1lzHdq7tpTBtvJmHuF6O0MWjMUi5KqKRNzERO9u8upLLzVeeX8DdpHHztGe97Yn%2F%2FnJReD9yFsmH8RC%2Be5egrwR08kE3ypgrKH6Ww8ywINw4CoH0xRV0YKh8ToFgNelI5Gq3%2Fo18J5v7ZCZHqaIxO9BjLoP5HGP6inttx7wGDDxlZu9BjqkAbTiyxfnVnX9cxlkIzGVpqL8xUZkw1nWcVe5RBBYyvu1VUceEuBO3hEVtOkwNfkMXr0o%2Fb0HRVzKHn6y7VyrKmdFIBk6FQX8ThnivHsY6NorYcCqORp7NJ%2BbRRjUxdFRbcmbPERhkzHgeqN4m5kphFuHghtLvFGMfdjuRWS9gTL1UUcIrnbnSr1I8X5DcWLQox0cPMWN1xmonPMjLhiUOlmGB5VH&X-Amz-Signature=ab07983040e29f6d7b7e63ebfc2607c994a9d660ccd1c4e3b5346164038d7b4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PJPJZRZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCP68PRNRQnQmVGZcEVEIxLObVxVj9n2UzSefwftO4eTQIgVzGxBbi7GGg5jUTJHdKVp1nI5uQJcWuoA7e6kMcqVq8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG4SrArdOMjbZ6HgVircA4d3ewISWOVrCNoA65xjeuN7TxpugeVzZ3fxoumOQZsy1yt4eEbM2N3lSepxiJLBnN2O0H8V6Ryc4HMKAcg4BDyjxt6Q54HcOKjzY%2BahTHqRPKeeuiskulKhlEtqSgelXh3rrzofT5cZWOjtKVKg2PFxGKwlieHhyYFFebMegCHXtshWX8ppjSGdXIvlr7XftpfqMDKZXpN9U9CNNMGzlrw8PEJ%2BLEzrFqZ7NluVpedQrbeQKCY8QwJbPSAFpXOjro2AGQk%2B9vMQ%2FVPj1ND%2BwCL1tyH6JMg6ZLFta7E0MoSwifhNa21uiTiMblhx8Eaye%2BM0hnajeDhTYd0%2Fb9ug%2BtPdsyBx4jNtMlGVJNWnwVeqO7Ik%2Bp4Z8QE4Q46kUt60d%2Faq%2B8MTQzEadH4PlE2bDsKFIVITDDYdpa5YXC2iE0WudRtASTY8ZQN%2FKGD5lb47IRMt5noQ2osCtFj75d200%2BZc1OrhxBvHrA%2BUzkIALWWboMkeVgdIwFu0WNSnzEFk8QS2A9PoM2cmspClMKORIjXsggtYDlMC6T6rgWeu4UesenNkIF4CHdHQzYiydhH5qdQIK%2FaXy%2FR%2FnJ7jxbpJaWuGeLnG%2FBlV5hlLAOsjk1tJQ%2FtRULKTVO0Z5O0yMNeWm70GOqUBn9oEIRY4DKzXTPcJnNaQJhMm1bGkqAy2%2BohB69WYee%2FGY0ETLIpCAmN%2F01OUz7rbBZw6kV%2BVw6BTeDsNR5sbwLMmWsajY0htlJnbeBllzLXc%2FzbH5SK9RpDtxq7%2B2rvEu6%2BoUkbOf9sd3rqqseC4Q0mTNQNSYLbaeIl0QGnJfOtiuD5tvk4v0d1aPoAPyRU4q3MYZky%2F0Ueff2T%2BBde9bKA3%2ByYI&X-Amz-Signature=07865468a9fbdeabdfce660d4f229e98489f8c08ea4e514214246f9eb9b72963&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PJPJZRZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCP68PRNRQnQmVGZcEVEIxLObVxVj9n2UzSefwftO4eTQIgVzGxBbi7GGg5jUTJHdKVp1nI5uQJcWuoA7e6kMcqVq8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG4SrArdOMjbZ6HgVircA4d3ewISWOVrCNoA65xjeuN7TxpugeVzZ3fxoumOQZsy1yt4eEbM2N3lSepxiJLBnN2O0H8V6Ryc4HMKAcg4BDyjxt6Q54HcOKjzY%2BahTHqRPKeeuiskulKhlEtqSgelXh3rrzofT5cZWOjtKVKg2PFxGKwlieHhyYFFebMegCHXtshWX8ppjSGdXIvlr7XftpfqMDKZXpN9U9CNNMGzlrw8PEJ%2BLEzrFqZ7NluVpedQrbeQKCY8QwJbPSAFpXOjro2AGQk%2B9vMQ%2FVPj1ND%2BwCL1tyH6JMg6ZLFta7E0MoSwifhNa21uiTiMblhx8Eaye%2BM0hnajeDhTYd0%2Fb9ug%2BtPdsyBx4jNtMlGVJNWnwVeqO7Ik%2Bp4Z8QE4Q46kUt60d%2Faq%2B8MTQzEadH4PlE2bDsKFIVITDDYdpa5YXC2iE0WudRtASTY8ZQN%2FKGD5lb47IRMt5noQ2osCtFj75d200%2BZc1OrhxBvHrA%2BUzkIALWWboMkeVgdIwFu0WNSnzEFk8QS2A9PoM2cmspClMKORIjXsggtYDlMC6T6rgWeu4UesenNkIF4CHdHQzYiydhH5qdQIK%2FaXy%2FR%2FnJ7jxbpJaWuGeLnG%2FBlV5hlLAOsjk1tJQ%2FtRULKTVO0Z5O0yMNeWm70GOqUBn9oEIRY4DKzXTPcJnNaQJhMm1bGkqAy2%2BohB69WYee%2FGY0ETLIpCAmN%2F01OUz7rbBZw6kV%2BVw6BTeDsNR5sbwLMmWsajY0htlJnbeBllzLXc%2FzbH5SK9RpDtxq7%2B2rvEu6%2BoUkbOf9sd3rqqseC4Q0mTNQNSYLbaeIl0QGnJfOtiuD5tvk4v0d1aPoAPyRU4q3MYZky%2F0Ueff2T%2BBde9bKA3%2ByYI&X-Amz-Signature=49d8496577a6a976f95e81fbb75c44894b483bca38c4a881b74da62836181ce6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
