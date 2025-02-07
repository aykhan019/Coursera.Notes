

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QICOOECC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIEbLlXfdOrOpa41IGZI8bX%2FWXGaqFjDEw6n5TgJFSxwAAiByZd%2FWesZOHM%2Bl6TrmskOVHe2qwX7l%2BDb8CsddP%2FHehir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMADpSK0RvUnl12lhDKtwDLCKvNjI55uM%2FGPDcz%2BNY4TxDRKZsjFmxUnKQnf4KzwZQ%2BAL4EBTvFKrkT%2BdgiqY8Zq8YTlVZWrrPjoq9%2BGpJwgDdOiJauF%2Fupid7fWwt6CFgI62GF5w%2FP%2FT5bgP5zQMa1GNaIOXYNe7oa16GgXxwNyhSGzYfK3V7LQ3gV%2BSg%2B0gxxiovqyVMRGusrhki22l5673RNSyO9o0QUvjFLRtr2OsrnQEj8Av1C8bc8m%2FzF1SIuHmFrLvcFUemYERoIsmAV8sfouHMKvLd9WPov7UvYwd0AWPGnj6SUTY3YhEAaMp2BcsZcZ%2FPyOVuNOYzx0yG%2B9qHMFOBY85lqZTC9%2BA6cjb%2BPQL7HfiecPPMdETdRecoawNt6BjNKKlxSDAZJTcHtyQObU9GkljStp546R7DY0x5LefKFx9oBm1on%2FU3zUpxue7%2B7K4oC2VcTk3rZcDzMYYezEdiQLv7IdmaW9bo8Iz0wq5fLbeHtiw9IKBFZCea4afR7J5bTNllzOoKgNg2yA10NTlkLb8Lg86Zo45pMhCWAxIn1tGTyyFE425nFCiYXBmPZJgslnSjg8bC8uKA5hiB7Z7OK7PxmfAxM3cH97TmjrWCfabri3dZAkzr3ZGrH0WD%2FqISF2gn6v4wp7%2BWvQY6pgGSCAT76up5YADjA6H0rmu%2FUu0yQTPtMtGNOUMgki%2FG2HOwvhpGlAckddJqhndxq5u5viE0dsdeuHHyYrFxSw71IYxugjwvENiWmi6IU4UIjLU0ELwWv8FMpGs4fzfzaA5QARyq56PG18lT1DR4E6z54jqHDOL64nnggFIfMUaIkcfeFk%2F5UG%2BnUg5fnH9dTmb9EA2JjnDwHNZ%2B4t%2BmKEb1lWZFx%2BLz&X-Amz-Signature=4c0eae4b3e36e83ebdd5bedf4419963f8a37a0e1d9b676f5abebd3d01ca72ab2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QICOOECC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIEbLlXfdOrOpa41IGZI8bX%2FWXGaqFjDEw6n5TgJFSxwAAiByZd%2FWesZOHM%2Bl6TrmskOVHe2qwX7l%2BDb8CsddP%2FHehir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMADpSK0RvUnl12lhDKtwDLCKvNjI55uM%2FGPDcz%2BNY4TxDRKZsjFmxUnKQnf4KzwZQ%2BAL4EBTvFKrkT%2BdgiqY8Zq8YTlVZWrrPjoq9%2BGpJwgDdOiJauF%2Fupid7fWwt6CFgI62GF5w%2FP%2FT5bgP5zQMa1GNaIOXYNe7oa16GgXxwNyhSGzYfK3V7LQ3gV%2BSg%2B0gxxiovqyVMRGusrhki22l5673RNSyO9o0QUvjFLRtr2OsrnQEj8Av1C8bc8m%2FzF1SIuHmFrLvcFUemYERoIsmAV8sfouHMKvLd9WPov7UvYwd0AWPGnj6SUTY3YhEAaMp2BcsZcZ%2FPyOVuNOYzx0yG%2B9qHMFOBY85lqZTC9%2BA6cjb%2BPQL7HfiecPPMdETdRecoawNt6BjNKKlxSDAZJTcHtyQObU9GkljStp546R7DY0x5LefKFx9oBm1on%2FU3zUpxue7%2B7K4oC2VcTk3rZcDzMYYezEdiQLv7IdmaW9bo8Iz0wq5fLbeHtiw9IKBFZCea4afR7J5bTNllzOoKgNg2yA10NTlkLb8Lg86Zo45pMhCWAxIn1tGTyyFE425nFCiYXBmPZJgslnSjg8bC8uKA5hiB7Z7OK7PxmfAxM3cH97TmjrWCfabri3dZAkzr3ZGrH0WD%2FqISF2gn6v4wp7%2BWvQY6pgGSCAT76up5YADjA6H0rmu%2FUu0yQTPtMtGNOUMgki%2FG2HOwvhpGlAckddJqhndxq5u5viE0dsdeuHHyYrFxSw71IYxugjwvENiWmi6IU4UIjLU0ELwWv8FMpGs4fzfzaA5QARyq56PG18lT1DR4E6z54jqHDOL64nnggFIfMUaIkcfeFk%2F5UG%2BnUg5fnH9dTmb9EA2JjnDwHNZ%2B4t%2BmKEb1lWZFx%2BLz&X-Amz-Signature=9366db60ce87f11e6cd635a89dc7b4840368faaabb52e7fbfa455f8fb772785a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QICOOECC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIEbLlXfdOrOpa41IGZI8bX%2FWXGaqFjDEw6n5TgJFSxwAAiByZd%2FWesZOHM%2Bl6TrmskOVHe2qwX7l%2BDb8CsddP%2FHehir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMADpSK0RvUnl12lhDKtwDLCKvNjI55uM%2FGPDcz%2BNY4TxDRKZsjFmxUnKQnf4KzwZQ%2BAL4EBTvFKrkT%2BdgiqY8Zq8YTlVZWrrPjoq9%2BGpJwgDdOiJauF%2Fupid7fWwt6CFgI62GF5w%2FP%2FT5bgP5zQMa1GNaIOXYNe7oa16GgXxwNyhSGzYfK3V7LQ3gV%2BSg%2B0gxxiovqyVMRGusrhki22l5673RNSyO9o0QUvjFLRtr2OsrnQEj8Av1C8bc8m%2FzF1SIuHmFrLvcFUemYERoIsmAV8sfouHMKvLd9WPov7UvYwd0AWPGnj6SUTY3YhEAaMp2BcsZcZ%2FPyOVuNOYzx0yG%2B9qHMFOBY85lqZTC9%2BA6cjb%2BPQL7HfiecPPMdETdRecoawNt6BjNKKlxSDAZJTcHtyQObU9GkljStp546R7DY0x5LefKFx9oBm1on%2FU3zUpxue7%2B7K4oC2VcTk3rZcDzMYYezEdiQLv7IdmaW9bo8Iz0wq5fLbeHtiw9IKBFZCea4afR7J5bTNllzOoKgNg2yA10NTlkLb8Lg86Zo45pMhCWAxIn1tGTyyFE425nFCiYXBmPZJgslnSjg8bC8uKA5hiB7Z7OK7PxmfAxM3cH97TmjrWCfabri3dZAkzr3ZGrH0WD%2FqISF2gn6v4wp7%2BWvQY6pgGSCAT76up5YADjA6H0rmu%2FUu0yQTPtMtGNOUMgki%2FG2HOwvhpGlAckddJqhndxq5u5viE0dsdeuHHyYrFxSw71IYxugjwvENiWmi6IU4UIjLU0ELwWv8FMpGs4fzfzaA5QARyq56PG18lT1DR4E6z54jqHDOL64nnggFIfMUaIkcfeFk%2F5UG%2BnUg5fnH9dTmb9EA2JjnDwHNZ%2B4t%2BmKEb1lWZFx%2BLz&X-Amz-Signature=0e51fa6bdf455be63a4d6d866659e4cfb0d97ed1399431f1fb4bf80173ee1358&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QICOOECC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIEbLlXfdOrOpa41IGZI8bX%2FWXGaqFjDEw6n5TgJFSxwAAiByZd%2FWesZOHM%2Bl6TrmskOVHe2qwX7l%2BDb8CsddP%2FHehir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMADpSK0RvUnl12lhDKtwDLCKvNjI55uM%2FGPDcz%2BNY4TxDRKZsjFmxUnKQnf4KzwZQ%2BAL4EBTvFKrkT%2BdgiqY8Zq8YTlVZWrrPjoq9%2BGpJwgDdOiJauF%2Fupid7fWwt6CFgI62GF5w%2FP%2FT5bgP5zQMa1GNaIOXYNe7oa16GgXxwNyhSGzYfK3V7LQ3gV%2BSg%2B0gxxiovqyVMRGusrhki22l5673RNSyO9o0QUvjFLRtr2OsrnQEj8Av1C8bc8m%2FzF1SIuHmFrLvcFUemYERoIsmAV8sfouHMKvLd9WPov7UvYwd0AWPGnj6SUTY3YhEAaMp2BcsZcZ%2FPyOVuNOYzx0yG%2B9qHMFOBY85lqZTC9%2BA6cjb%2BPQL7HfiecPPMdETdRecoawNt6BjNKKlxSDAZJTcHtyQObU9GkljStp546R7DY0x5LefKFx9oBm1on%2FU3zUpxue7%2B7K4oC2VcTk3rZcDzMYYezEdiQLv7IdmaW9bo8Iz0wq5fLbeHtiw9IKBFZCea4afR7J5bTNllzOoKgNg2yA10NTlkLb8Lg86Zo45pMhCWAxIn1tGTyyFE425nFCiYXBmPZJgslnSjg8bC8uKA5hiB7Z7OK7PxmfAxM3cH97TmjrWCfabri3dZAkzr3ZGrH0WD%2FqISF2gn6v4wp7%2BWvQY6pgGSCAT76up5YADjA6H0rmu%2FUu0yQTPtMtGNOUMgki%2FG2HOwvhpGlAckddJqhndxq5u5viE0dsdeuHHyYrFxSw71IYxugjwvENiWmi6IU4UIjLU0ELwWv8FMpGs4fzfzaA5QARyq56PG18lT1DR4E6z54jqHDOL64nnggFIfMUaIkcfeFk%2F5UG%2BnUg5fnH9dTmb9EA2JjnDwHNZ%2B4t%2BmKEb1lWZFx%2BLz&X-Amz-Signature=0555af7a6a59b0cd7693ac6d3df47666adb93fa66c7e1ec4a68acc00515aecae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QICOOECC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIEbLlXfdOrOpa41IGZI8bX%2FWXGaqFjDEw6n5TgJFSxwAAiByZd%2FWesZOHM%2Bl6TrmskOVHe2qwX7l%2BDb8CsddP%2FHehir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMADpSK0RvUnl12lhDKtwDLCKvNjI55uM%2FGPDcz%2BNY4TxDRKZsjFmxUnKQnf4KzwZQ%2BAL4EBTvFKrkT%2BdgiqY8Zq8YTlVZWrrPjoq9%2BGpJwgDdOiJauF%2Fupid7fWwt6CFgI62GF5w%2FP%2FT5bgP5zQMa1GNaIOXYNe7oa16GgXxwNyhSGzYfK3V7LQ3gV%2BSg%2B0gxxiovqyVMRGusrhki22l5673RNSyO9o0QUvjFLRtr2OsrnQEj8Av1C8bc8m%2FzF1SIuHmFrLvcFUemYERoIsmAV8sfouHMKvLd9WPov7UvYwd0AWPGnj6SUTY3YhEAaMp2BcsZcZ%2FPyOVuNOYzx0yG%2B9qHMFOBY85lqZTC9%2BA6cjb%2BPQL7HfiecPPMdETdRecoawNt6BjNKKlxSDAZJTcHtyQObU9GkljStp546R7DY0x5LefKFx9oBm1on%2FU3zUpxue7%2B7K4oC2VcTk3rZcDzMYYezEdiQLv7IdmaW9bo8Iz0wq5fLbeHtiw9IKBFZCea4afR7J5bTNllzOoKgNg2yA10NTlkLb8Lg86Zo45pMhCWAxIn1tGTyyFE425nFCiYXBmPZJgslnSjg8bC8uKA5hiB7Z7OK7PxmfAxM3cH97TmjrWCfabri3dZAkzr3ZGrH0WD%2FqISF2gn6v4wp7%2BWvQY6pgGSCAT76up5YADjA6H0rmu%2FUu0yQTPtMtGNOUMgki%2FG2HOwvhpGlAckddJqhndxq5u5viE0dsdeuHHyYrFxSw71IYxugjwvENiWmi6IU4UIjLU0ELwWv8FMpGs4fzfzaA5QARyq56PG18lT1DR4E6z54jqHDOL64nnggFIfMUaIkcfeFk%2F5UG%2BnUg5fnH9dTmb9EA2JjnDwHNZ%2B4t%2BmKEb1lWZFx%2BLz&X-Amz-Signature=f62982e1b192bdc7db39dc923ec4ba297c53b2834c1312c06fb8beef8fa550dd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QICOOECC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIEbLlXfdOrOpa41IGZI8bX%2FWXGaqFjDEw6n5TgJFSxwAAiByZd%2FWesZOHM%2Bl6TrmskOVHe2qwX7l%2BDb8CsddP%2FHehir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMADpSK0RvUnl12lhDKtwDLCKvNjI55uM%2FGPDcz%2BNY4TxDRKZsjFmxUnKQnf4KzwZQ%2BAL4EBTvFKrkT%2BdgiqY8Zq8YTlVZWrrPjoq9%2BGpJwgDdOiJauF%2Fupid7fWwt6CFgI62GF5w%2FP%2FT5bgP5zQMa1GNaIOXYNe7oa16GgXxwNyhSGzYfK3V7LQ3gV%2BSg%2B0gxxiovqyVMRGusrhki22l5673RNSyO9o0QUvjFLRtr2OsrnQEj8Av1C8bc8m%2FzF1SIuHmFrLvcFUemYERoIsmAV8sfouHMKvLd9WPov7UvYwd0AWPGnj6SUTY3YhEAaMp2BcsZcZ%2FPyOVuNOYzx0yG%2B9qHMFOBY85lqZTC9%2BA6cjb%2BPQL7HfiecPPMdETdRecoawNt6BjNKKlxSDAZJTcHtyQObU9GkljStp546R7DY0x5LefKFx9oBm1on%2FU3zUpxue7%2B7K4oC2VcTk3rZcDzMYYezEdiQLv7IdmaW9bo8Iz0wq5fLbeHtiw9IKBFZCea4afR7J5bTNllzOoKgNg2yA10NTlkLb8Lg86Zo45pMhCWAxIn1tGTyyFE425nFCiYXBmPZJgslnSjg8bC8uKA5hiB7Z7OK7PxmfAxM3cH97TmjrWCfabri3dZAkzr3ZGrH0WD%2FqISF2gn6v4wp7%2BWvQY6pgGSCAT76up5YADjA6H0rmu%2FUu0yQTPtMtGNOUMgki%2FG2HOwvhpGlAckddJqhndxq5u5viE0dsdeuHHyYrFxSw71IYxugjwvENiWmi6IU4UIjLU0ELwWv8FMpGs4fzfzaA5QARyq56PG18lT1DR4E6z54jqHDOL64nnggFIfMUaIkcfeFk%2F5UG%2BnUg5fnH9dTmb9EA2JjnDwHNZ%2B4t%2BmKEb1lWZFx%2BLz&X-Amz-Signature=32e76d2ea2974ac09d2e1f241f222953fd67083a7d492baa7578bb6e0f3a0bb8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QICOOECC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIEbLlXfdOrOpa41IGZI8bX%2FWXGaqFjDEw6n5TgJFSxwAAiByZd%2FWesZOHM%2Bl6TrmskOVHe2qwX7l%2BDb8CsddP%2FHehir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMADpSK0RvUnl12lhDKtwDLCKvNjI55uM%2FGPDcz%2BNY4TxDRKZsjFmxUnKQnf4KzwZQ%2BAL4EBTvFKrkT%2BdgiqY8Zq8YTlVZWrrPjoq9%2BGpJwgDdOiJauF%2Fupid7fWwt6CFgI62GF5w%2FP%2FT5bgP5zQMa1GNaIOXYNe7oa16GgXxwNyhSGzYfK3V7LQ3gV%2BSg%2B0gxxiovqyVMRGusrhki22l5673RNSyO9o0QUvjFLRtr2OsrnQEj8Av1C8bc8m%2FzF1SIuHmFrLvcFUemYERoIsmAV8sfouHMKvLd9WPov7UvYwd0AWPGnj6SUTY3YhEAaMp2BcsZcZ%2FPyOVuNOYzx0yG%2B9qHMFOBY85lqZTC9%2BA6cjb%2BPQL7HfiecPPMdETdRecoawNt6BjNKKlxSDAZJTcHtyQObU9GkljStp546R7DY0x5LefKFx9oBm1on%2FU3zUpxue7%2B7K4oC2VcTk3rZcDzMYYezEdiQLv7IdmaW9bo8Iz0wq5fLbeHtiw9IKBFZCea4afR7J5bTNllzOoKgNg2yA10NTlkLb8Lg86Zo45pMhCWAxIn1tGTyyFE425nFCiYXBmPZJgslnSjg8bC8uKA5hiB7Z7OK7PxmfAxM3cH97TmjrWCfabri3dZAkzr3ZGrH0WD%2FqISF2gn6v4wp7%2BWvQY6pgGSCAT76up5YADjA6H0rmu%2FUu0yQTPtMtGNOUMgki%2FG2HOwvhpGlAckddJqhndxq5u5viE0dsdeuHHyYrFxSw71IYxugjwvENiWmi6IU4UIjLU0ELwWv8FMpGs4fzfzaA5QARyq56PG18lT1DR4E6z54jqHDOL64nnggFIfMUaIkcfeFk%2F5UG%2BnUg5fnH9dTmb9EA2JjnDwHNZ%2B4t%2BmKEb1lWZFx%2BLz&X-Amz-Signature=624917f98dd26834d3c37e5bfec9362046bd0dab87d925734a5c3deb40f573dd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QICOOECC%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIEbLlXfdOrOpa41IGZI8bX%2FWXGaqFjDEw6n5TgJFSxwAAiByZd%2FWesZOHM%2Bl6TrmskOVHe2qwX7l%2BDb8CsddP%2FHehir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMADpSK0RvUnl12lhDKtwDLCKvNjI55uM%2FGPDcz%2BNY4TxDRKZsjFmxUnKQnf4KzwZQ%2BAL4EBTvFKrkT%2BdgiqY8Zq8YTlVZWrrPjoq9%2BGpJwgDdOiJauF%2Fupid7fWwt6CFgI62GF5w%2FP%2FT5bgP5zQMa1GNaIOXYNe7oa16GgXxwNyhSGzYfK3V7LQ3gV%2BSg%2B0gxxiovqyVMRGusrhki22l5673RNSyO9o0QUvjFLRtr2OsrnQEj8Av1C8bc8m%2FzF1SIuHmFrLvcFUemYERoIsmAV8sfouHMKvLd9WPov7UvYwd0AWPGnj6SUTY3YhEAaMp2BcsZcZ%2FPyOVuNOYzx0yG%2B9qHMFOBY85lqZTC9%2BA6cjb%2BPQL7HfiecPPMdETdRecoawNt6BjNKKlxSDAZJTcHtyQObU9GkljStp546R7DY0x5LefKFx9oBm1on%2FU3zUpxue7%2B7K4oC2VcTk3rZcDzMYYezEdiQLv7IdmaW9bo8Iz0wq5fLbeHtiw9IKBFZCea4afR7J5bTNllzOoKgNg2yA10NTlkLb8Lg86Zo45pMhCWAxIn1tGTyyFE425nFCiYXBmPZJgslnSjg8bC8uKA5hiB7Z7OK7PxmfAxM3cH97TmjrWCfabri3dZAkzr3ZGrH0WD%2FqISF2gn6v4wp7%2BWvQY6pgGSCAT76up5YADjA6H0rmu%2FUu0yQTPtMtGNOUMgki%2FG2HOwvhpGlAckddJqhndxq5u5viE0dsdeuHHyYrFxSw71IYxugjwvENiWmi6IU4UIjLU0ELwWv8FMpGs4fzfzaA5QARyq56PG18lT1DR4E6z54jqHDOL64nnggFIfMUaIkcfeFk%2F5UG%2BnUg5fnH9dTmb9EA2JjnDwHNZ%2B4t%2BmKEb1lWZFx%2BLz&X-Amz-Signature=28b1a7f121dc56171d7d04240b14c420d75c4b56bb24bd57690bf5e3dd611f89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GATDOCB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCICwaiRa8CfnoQn34cNS0qmvc4XES9MmBOfpibdGSSW1hAiEA0H1oJPh0IBkZJY4XNfLNUTKjBD0U87MXIefVEpD7gzsq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDOPVLa5VplWHgjeq0ircA%2F6%2FAmCj3KCUb6iarhuBCbc9T0heBK93lQAJYMrd20nkZtQktt6ls4T7crMe%2FsyIBhn06obk%2Be93JzhbHsOlgEirQRFk7mow8pHDTTLQ%2Fak4k7WcgzVygwVhtjRsNMWPnKeQgJQUyJXQ0Sy6lIoSkg5mXerjRDt%2FQXQBl%2FCH58%2Fu3unVokCGbZlmtolSYQbajwS3b4v4FUQSo9lU6Syyi9cwhICmBmtNQexwOrF2wUi98wDjd6YaZid2rtUx6jV67ttzp0QrN1aw8FnPa7r7YYSdEcRt5iQ2bvLgDNMoHp0AEp%2FmIKNkNd%2Fh3UOceE5wYaFfJ1EHG4oWnlgY8CG4QqclNQ9FPTYQHOzBQhJDzyIO%2FSFWxcj%2BEv7%2BKpWX%2FXa8lrztn2QvH6gkazErQsgagL9JeraTSD%2F4ft1VJXOyi%2B6Ik25WUarycJEiOfWVp5FpWgCUE09qXA0iyRymDKsm%2B91ytiFFagP31goPbu7P28EnmC0TVAmEr2UGq5c1b1NmQvZI9rK5smL372%2BRRSsf5I5eV2NSV8gqP0aST3nxkz5YMioaDDHOO65iHKrKfFIvvpWOKmntrSdIUUavigdepFoNb7V5GAOty6SV0zpf1HHf1LUufFOO8Bl21EtMMJa%2Flr0GOqUBime7b0GoJu3nKC1SEzZGIl%2FGfea755UMgQN0I0HH0oCIUR7qhJmVWZKAig4ddd8XEVkoprGAEn10BF4ZhUv%2FuUnBByl1VkRyHEB6sp2O2PlpyrZZUCU9S3v50ScDiBU3EYQHpLj9yOLp%2FZ1GykFNbnASS03BU5BKgZ%2FwTYFJ1iJZwU4P1frl37o6EEl9fgZ5qX1Sk%2B8BpWifLCmqBfuN8%2FUX3jG%2F&X-Amz-Signature=7d2e94347dbe0e8695ece7ed4a1f2f75c97d43cc6fca2cf70cb00ab351c21978&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W472OENB%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIGniNEAY4WCKWfgAN4kmQqrKsBo9kvnyq6GVe2U54jaJAiEAoIT7Fd39ffjjAZw%2BRwdGIr5LX%2Fo7y6dRET3zQCVTk1oq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDLfxLeR55C2tnw8KsircA7zQIMHBMR%2BmWz24QiYwTMS53h%2BNithIqzRJjZ0QLRh5ZqdbvYIFQm69AOBInDz0QyiN4U6pgDtWYILlGYGHLMy49d8z3k1UyKW5YNJpYU89S07OIP71PE7hhg8JPDyh9wUHxbjBXeR7eWmZRwrqWJ8EGawEdSN4oGL90F8IdvqXxiQ19mEL2A0gnqsO4c8iM2KTrSawD85OLkszh7hf6LX9wnv2k%2Fo2DYNgBI3gbtUOzNCHjC1Uw3ImTOlSCY9aFdBnZezkiHpN%2BuI6h7xqXpODUTceQ%2B8WuOPbimUWg82yJYfRz6xmmha1iHOwT8uof%2FQ2ziGfjFst17BkeBFdcpc4AutOkHXc08yvGvwBEohnyPL3ymi%2BrkG4P%2BjgeBZEHkaVmK4jZQko%2BIdiQYTMCM9C7UJJJEYbKosxF8NgLsTau6SD0ss0m8D3VD9YpBVPcT4rImhWzIXqbOrH9J3%2FcoLvL7anDvAwONJUJPlYQ7dflP69p4p7x2%2FntntnG5SreaamqTB5miQUkAhynxbFk9RHnbTHDhhpp2RhkEFu96a5X5%2Fi3lRVFklWpLDAkNoiQmi7%2FPuQxgtXeCxLXCPaBhEN8yG6iGP9TsCBaCuf1in0k%2FXqNU4wBbNWQutrMP%2B%2Blr0GOqUBL%2FKyMr6GayEjx6qlTx3Z3yzd76HlM8nzhKimwebLrIZUzjmY3W6N692UFnIAYuXsXOfPKKNYH1tLn3hz7xhf6yI5QPesdCw1NZ2V%2FhRn1T0UU4ZWqL9wTVA6fiJs5i9jyAM72mH0RPu%2Bja%2FOwnA%2BxqnVneV6KaFKD9WubntVMq4TqyUIkn73DJjzlkG1Nefo06D%2BWNSxg%2FhB74Z%2BnBAeQHnkLrN7&X-Amz-Signature=6cf3276f7df3216cc89350eb180dd9e9e9a58f3aeb791fa1ad2ba7a59e987a50&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3A4WHLU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDnHiU%2B%2Fe7sSr0tfDXFoM5crN3KeIz%2Bl%2B%2BUorvV%2FZjPEwIhALB9UDJSGb952WZutmgvuk29GxABX9IpiBmP7Yux317jKv8DCG8QABoMNjM3NDIzMTgzODA1IgzuXM%2FpuqYUSwzGsBkq3AOkHGXEb4LlpJU%2BBYEum6W6H%2BcQ7BcqqPe%2F7j1%2Fiz3jwcziM%2FY2ETeoQw9eJfZoxZvR1NaxueAzPIVQB4z%2F1VMzUTuGUR9WmUzK86MRFDeDcrDZwOYYvZHzupZd4zIjB57AaWtVEMf0L1qSz8D2vFGsW0P1%2FLv8QHrXhsXT6Bu2en6xAGIvYh92KjZNElF%2Ff9LyzSb9Qjd%2FhBG7UWe56bisLsV%2FmvjLaeoWowNQIEoRhyJOSLrHJBXSqbVRedQJHBpJG7xBwG9uPlhrdJPNM1EvaGp2j0iLgLmQMH36QnAthzjz7vbnrWIg1GvOtWSq9q3%2FtxAmDt5MdLh0chqcS5Ca1xUTVRVt7Xjj5hATEeuIWmUWyZ%2FDNPrthDY6iQpDasJo6raneZA163wTOg4sM2L3YAVsmXAJEGFkXPNkEKSdmrQGmVrQbGMRHeNKfiL7eFaGmQWV%2B8TejY9tFHV3%2BD%2FKkPruSymap%2FyGoZWnjCsOVmFhCqftUXiX8FZMIm7qCiDa32c5rTBt%2BLyw2kzWDSukUTW1uX%2FE0A2w7pqsugOSPEPuB3YH6aBJ2111wguKwVpKJRYReiHuUSAvPc5JD%2BLHBLDzrX9pWbaCet5JZDkh1yMMoB%2FvmL6LWRPcRzCUv5a9BjqkASO4UcAWyiirOutDp1ABWyaFYCZWHIc%2BKS8aLhT0VryM4NTsCS1lQXAEI9EBwBMlACJN8C82t0A%2B1lU%2FUY8MtN5dv%2BJNA2fqbfIwC1m3pVF%2FMnmUKk0lZ9y0BBXf%2B5IjPKlRGZkRgUs4nMCORKmGFxO4dy%2BMsvZaSRIsDcKAe%2BAnxr8nFJzehF576Z7kKkaXrDtkx9t2y9E5sVYQkCJ%2FN1lBPG90&X-Amz-Signature=073b37f95bc46f67a494c022fe770b9dc1284a5803663db542fa3f6da8ce00ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3A4WHLU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQDnHiU%2B%2Fe7sSr0tfDXFoM5crN3KeIz%2Bl%2B%2BUorvV%2FZjPEwIhALB9UDJSGb952WZutmgvuk29GxABX9IpiBmP7Yux317jKv8DCG8QABoMNjM3NDIzMTgzODA1IgzuXM%2FpuqYUSwzGsBkq3AOkHGXEb4LlpJU%2BBYEum6W6H%2BcQ7BcqqPe%2F7j1%2Fiz3jwcziM%2FY2ETeoQw9eJfZoxZvR1NaxueAzPIVQB4z%2F1VMzUTuGUR9WmUzK86MRFDeDcrDZwOYYvZHzupZd4zIjB57AaWtVEMf0L1qSz8D2vFGsW0P1%2FLv8QHrXhsXT6Bu2en6xAGIvYh92KjZNElF%2Ff9LyzSb9Qjd%2FhBG7UWe56bisLsV%2FmvjLaeoWowNQIEoRhyJOSLrHJBXSqbVRedQJHBpJG7xBwG9uPlhrdJPNM1EvaGp2j0iLgLmQMH36QnAthzjz7vbnrWIg1GvOtWSq9q3%2FtxAmDt5MdLh0chqcS5Ca1xUTVRVt7Xjj5hATEeuIWmUWyZ%2FDNPrthDY6iQpDasJo6raneZA163wTOg4sM2L3YAVsmXAJEGFkXPNkEKSdmrQGmVrQbGMRHeNKfiL7eFaGmQWV%2B8TejY9tFHV3%2BD%2FKkPruSymap%2FyGoZWnjCsOVmFhCqftUXiX8FZMIm7qCiDa32c5rTBt%2BLyw2kzWDSukUTW1uX%2FE0A2w7pqsugOSPEPuB3YH6aBJ2111wguKwVpKJRYReiHuUSAvPc5JD%2BLHBLDzrX9pWbaCet5JZDkh1yMMoB%2FvmL6LWRPcRzCUv5a9BjqkASO4UcAWyiirOutDp1ABWyaFYCZWHIc%2BKS8aLhT0VryM4NTsCS1lQXAEI9EBwBMlACJN8C82t0A%2B1lU%2FUY8MtN5dv%2BJNA2fqbfIwC1m3pVF%2FMnmUKk0lZ9y0BBXf%2B5IjPKlRGZkRgUs4nMCORKmGFxO4dy%2BMsvZaSRIsDcKAe%2BAnxr8nFJzehF576Z7kKkaXrDtkx9t2y9E5sVYQkCJ%2FN1lBPG90&X-Amz-Signature=f5b17521c797f5353ca4f17d9c5093cd6fdf569e0cac00ac7ac0aafd2f9bd0b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
