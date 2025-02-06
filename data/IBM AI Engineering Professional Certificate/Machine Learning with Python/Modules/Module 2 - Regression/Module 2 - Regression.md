

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDKPSC3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDU6i8mhfzhFPUfXqOViY%2FHw1cg8kSeLZ6q16eM2RuPfAIgRkVrh7BDKJvM9Y8av%2FuuiAPXbajV0u%2FKoEcED5avr54q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOTXG8SdmHYP0cQhvircA75pKTcfys%2FYUF0vguXPz1o9Ht8Vfyxdt20K%2F%2Ftv30QDX9ahDW%2FrpF4azBDuXe4yI%2FhIjzGmymW8fT7fmumDrTbOCika2FXvKmLgPQRvdfdr5iEEOIivpuW64IWONRtaNX%2F8EfSytYCvf0dt%2F76pnifqxsSeWiD%2FzXiyfcR5UCH8tkh1HLWqi38g1PwAvIW4Z2VMozC20EyZKfX3Vjy4rjTl3r7jHWKSXU8up7PTDIWEXqH0OHwSgJBugbaNlHgyndlKUfv3%2BPjoNBEcMs%2FqBkoVeFijXpe25O6Lz5QsBMRwvj3RIpmEiKyfVPX9vj%2BTSeLrAog1m21CTT1e0Z9WY89dHE3J3rUyTZ2g5WhnGBIRQMeSJmQV41y5k9h6RuqxBrWtquQeFwo4gRohwxuFBHsItWGKJE9xnr8XXBCNMd1OBj6qnSjGDZTgIUy6EpZQEdiJd9ib4CKny%2FbwSE58%2FhsBDeRjQAxn6UwR2%2FpBgEne%2BYY74n7L%2B9G2CpCiDxvgwlIeWPc0zBfPCaeHaHT1eiNKJL9XKIspL4Ldg4rxN%2BexzbcXZFGywlC4%2FqLiqU93fvTDny%2FgYy7MhanpAC9dgIdYJ0zuM05piBpPZw6ngr2ckFPE6fCR22guhgUJMNbrkb0GOqUB7XKoKnazm0gD%2FEzWRt0%2FP4890RJiBMatJRPhlNJFlTJeUbM0rDtgjFREBFebdWhVMW%2BdHNwGOc143Oq9NsBXw154ZCzZpmvH7JAPB1qzzx5jU3bUtx7jM97WPkRuKCvWqaS2Up3GwxEXG9RVP1bbKpT0WCxaoz8Op8qlwyOM0l9gySMVuOTDVXM1s1AiOH3bHXMBYhq1PBKo3dy0kAQ1UXeMt5sr&X-Amz-Signature=edb9faa48d83b8e32ed4b0caac6a16c04b5450acb6786a7d90cf3262fcc976d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDKPSC3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDU6i8mhfzhFPUfXqOViY%2FHw1cg8kSeLZ6q16eM2RuPfAIgRkVrh7BDKJvM9Y8av%2FuuiAPXbajV0u%2FKoEcED5avr54q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOTXG8SdmHYP0cQhvircA75pKTcfys%2FYUF0vguXPz1o9Ht8Vfyxdt20K%2F%2Ftv30QDX9ahDW%2FrpF4azBDuXe4yI%2FhIjzGmymW8fT7fmumDrTbOCika2FXvKmLgPQRvdfdr5iEEOIivpuW64IWONRtaNX%2F8EfSytYCvf0dt%2F76pnifqxsSeWiD%2FzXiyfcR5UCH8tkh1HLWqi38g1PwAvIW4Z2VMozC20EyZKfX3Vjy4rjTl3r7jHWKSXU8up7PTDIWEXqH0OHwSgJBugbaNlHgyndlKUfv3%2BPjoNBEcMs%2FqBkoVeFijXpe25O6Lz5QsBMRwvj3RIpmEiKyfVPX9vj%2BTSeLrAog1m21CTT1e0Z9WY89dHE3J3rUyTZ2g5WhnGBIRQMeSJmQV41y5k9h6RuqxBrWtquQeFwo4gRohwxuFBHsItWGKJE9xnr8XXBCNMd1OBj6qnSjGDZTgIUy6EpZQEdiJd9ib4CKny%2FbwSE58%2FhsBDeRjQAxn6UwR2%2FpBgEne%2BYY74n7L%2B9G2CpCiDxvgwlIeWPc0zBfPCaeHaHT1eiNKJL9XKIspL4Ldg4rxN%2BexzbcXZFGywlC4%2FqLiqU93fvTDny%2FgYy7MhanpAC9dgIdYJ0zuM05piBpPZw6ngr2ckFPE6fCR22guhgUJMNbrkb0GOqUB7XKoKnazm0gD%2FEzWRt0%2FP4890RJiBMatJRPhlNJFlTJeUbM0rDtgjFREBFebdWhVMW%2BdHNwGOc143Oq9NsBXw154ZCzZpmvH7JAPB1qzzx5jU3bUtx7jM97WPkRuKCvWqaS2Up3GwxEXG9RVP1bbKpT0WCxaoz8Op8qlwyOM0l9gySMVuOTDVXM1s1AiOH3bHXMBYhq1PBKo3dy0kAQ1UXeMt5sr&X-Amz-Signature=a24f551a25170146d795bb32aba7fef86fb2d6091615bb3e2ab8f0b91a187bb7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDKPSC3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDU6i8mhfzhFPUfXqOViY%2FHw1cg8kSeLZ6q16eM2RuPfAIgRkVrh7BDKJvM9Y8av%2FuuiAPXbajV0u%2FKoEcED5avr54q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOTXG8SdmHYP0cQhvircA75pKTcfys%2FYUF0vguXPz1o9Ht8Vfyxdt20K%2F%2Ftv30QDX9ahDW%2FrpF4azBDuXe4yI%2FhIjzGmymW8fT7fmumDrTbOCika2FXvKmLgPQRvdfdr5iEEOIivpuW64IWONRtaNX%2F8EfSytYCvf0dt%2F76pnifqxsSeWiD%2FzXiyfcR5UCH8tkh1HLWqi38g1PwAvIW4Z2VMozC20EyZKfX3Vjy4rjTl3r7jHWKSXU8up7PTDIWEXqH0OHwSgJBugbaNlHgyndlKUfv3%2BPjoNBEcMs%2FqBkoVeFijXpe25O6Lz5QsBMRwvj3RIpmEiKyfVPX9vj%2BTSeLrAog1m21CTT1e0Z9WY89dHE3J3rUyTZ2g5WhnGBIRQMeSJmQV41y5k9h6RuqxBrWtquQeFwo4gRohwxuFBHsItWGKJE9xnr8XXBCNMd1OBj6qnSjGDZTgIUy6EpZQEdiJd9ib4CKny%2FbwSE58%2FhsBDeRjQAxn6UwR2%2FpBgEne%2BYY74n7L%2B9G2CpCiDxvgwlIeWPc0zBfPCaeHaHT1eiNKJL9XKIspL4Ldg4rxN%2BexzbcXZFGywlC4%2FqLiqU93fvTDny%2FgYy7MhanpAC9dgIdYJ0zuM05piBpPZw6ngr2ckFPE6fCR22guhgUJMNbrkb0GOqUB7XKoKnazm0gD%2FEzWRt0%2FP4890RJiBMatJRPhlNJFlTJeUbM0rDtgjFREBFebdWhVMW%2BdHNwGOc143Oq9NsBXw154ZCzZpmvH7JAPB1qzzx5jU3bUtx7jM97WPkRuKCvWqaS2Up3GwxEXG9RVP1bbKpT0WCxaoz8Op8qlwyOM0l9gySMVuOTDVXM1s1AiOH3bHXMBYhq1PBKo3dy0kAQ1UXeMt5sr&X-Amz-Signature=de3a6e15dceb72b975848e3ca4309679ac4b1d3b325336e1f70898eb4b9367c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDKPSC3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDU6i8mhfzhFPUfXqOViY%2FHw1cg8kSeLZ6q16eM2RuPfAIgRkVrh7BDKJvM9Y8av%2FuuiAPXbajV0u%2FKoEcED5avr54q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOTXG8SdmHYP0cQhvircA75pKTcfys%2FYUF0vguXPz1o9Ht8Vfyxdt20K%2F%2Ftv30QDX9ahDW%2FrpF4azBDuXe4yI%2FhIjzGmymW8fT7fmumDrTbOCika2FXvKmLgPQRvdfdr5iEEOIivpuW64IWONRtaNX%2F8EfSytYCvf0dt%2F76pnifqxsSeWiD%2FzXiyfcR5UCH8tkh1HLWqi38g1PwAvIW4Z2VMozC20EyZKfX3Vjy4rjTl3r7jHWKSXU8up7PTDIWEXqH0OHwSgJBugbaNlHgyndlKUfv3%2BPjoNBEcMs%2FqBkoVeFijXpe25O6Lz5QsBMRwvj3RIpmEiKyfVPX9vj%2BTSeLrAog1m21CTT1e0Z9WY89dHE3J3rUyTZ2g5WhnGBIRQMeSJmQV41y5k9h6RuqxBrWtquQeFwo4gRohwxuFBHsItWGKJE9xnr8XXBCNMd1OBj6qnSjGDZTgIUy6EpZQEdiJd9ib4CKny%2FbwSE58%2FhsBDeRjQAxn6UwR2%2FpBgEne%2BYY74n7L%2B9G2CpCiDxvgwlIeWPc0zBfPCaeHaHT1eiNKJL9XKIspL4Ldg4rxN%2BexzbcXZFGywlC4%2FqLiqU93fvTDny%2FgYy7MhanpAC9dgIdYJ0zuM05piBpPZw6ngr2ckFPE6fCR22guhgUJMNbrkb0GOqUB7XKoKnazm0gD%2FEzWRt0%2FP4890RJiBMatJRPhlNJFlTJeUbM0rDtgjFREBFebdWhVMW%2BdHNwGOc143Oq9NsBXw154ZCzZpmvH7JAPB1qzzx5jU3bUtx7jM97WPkRuKCvWqaS2Up3GwxEXG9RVP1bbKpT0WCxaoz8Op8qlwyOM0l9gySMVuOTDVXM1s1AiOH3bHXMBYhq1PBKo3dy0kAQ1UXeMt5sr&X-Amz-Signature=fa90f3d5618a184870358c8d8ada9abd2057d1af6616928ee6c511ec888ea323&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDKPSC3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDU6i8mhfzhFPUfXqOViY%2FHw1cg8kSeLZ6q16eM2RuPfAIgRkVrh7BDKJvM9Y8av%2FuuiAPXbajV0u%2FKoEcED5avr54q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOTXG8SdmHYP0cQhvircA75pKTcfys%2FYUF0vguXPz1o9Ht8Vfyxdt20K%2F%2Ftv30QDX9ahDW%2FrpF4azBDuXe4yI%2FhIjzGmymW8fT7fmumDrTbOCika2FXvKmLgPQRvdfdr5iEEOIivpuW64IWONRtaNX%2F8EfSytYCvf0dt%2F76pnifqxsSeWiD%2FzXiyfcR5UCH8tkh1HLWqi38g1PwAvIW4Z2VMozC20EyZKfX3Vjy4rjTl3r7jHWKSXU8up7PTDIWEXqH0OHwSgJBugbaNlHgyndlKUfv3%2BPjoNBEcMs%2FqBkoVeFijXpe25O6Lz5QsBMRwvj3RIpmEiKyfVPX9vj%2BTSeLrAog1m21CTT1e0Z9WY89dHE3J3rUyTZ2g5WhnGBIRQMeSJmQV41y5k9h6RuqxBrWtquQeFwo4gRohwxuFBHsItWGKJE9xnr8XXBCNMd1OBj6qnSjGDZTgIUy6EpZQEdiJd9ib4CKny%2FbwSE58%2FhsBDeRjQAxn6UwR2%2FpBgEne%2BYY74n7L%2B9G2CpCiDxvgwlIeWPc0zBfPCaeHaHT1eiNKJL9XKIspL4Ldg4rxN%2BexzbcXZFGywlC4%2FqLiqU93fvTDny%2FgYy7MhanpAC9dgIdYJ0zuM05piBpPZw6ngr2ckFPE6fCR22guhgUJMNbrkb0GOqUB7XKoKnazm0gD%2FEzWRt0%2FP4890RJiBMatJRPhlNJFlTJeUbM0rDtgjFREBFebdWhVMW%2BdHNwGOc143Oq9NsBXw154ZCzZpmvH7JAPB1qzzx5jU3bUtx7jM97WPkRuKCvWqaS2Up3GwxEXG9RVP1bbKpT0WCxaoz8Op8qlwyOM0l9gySMVuOTDVXM1s1AiOH3bHXMBYhq1PBKo3dy0kAQ1UXeMt5sr&X-Amz-Signature=1abb4d2f6dcb5a3129a6716d6e4a0dd5f8f104ac7c832c81a5784ee769bcce51&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDKPSC3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDU6i8mhfzhFPUfXqOViY%2FHw1cg8kSeLZ6q16eM2RuPfAIgRkVrh7BDKJvM9Y8av%2FuuiAPXbajV0u%2FKoEcED5avr54q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOTXG8SdmHYP0cQhvircA75pKTcfys%2FYUF0vguXPz1o9Ht8Vfyxdt20K%2F%2Ftv30QDX9ahDW%2FrpF4azBDuXe4yI%2FhIjzGmymW8fT7fmumDrTbOCika2FXvKmLgPQRvdfdr5iEEOIivpuW64IWONRtaNX%2F8EfSytYCvf0dt%2F76pnifqxsSeWiD%2FzXiyfcR5UCH8tkh1HLWqi38g1PwAvIW4Z2VMozC20EyZKfX3Vjy4rjTl3r7jHWKSXU8up7PTDIWEXqH0OHwSgJBugbaNlHgyndlKUfv3%2BPjoNBEcMs%2FqBkoVeFijXpe25O6Lz5QsBMRwvj3RIpmEiKyfVPX9vj%2BTSeLrAog1m21CTT1e0Z9WY89dHE3J3rUyTZ2g5WhnGBIRQMeSJmQV41y5k9h6RuqxBrWtquQeFwo4gRohwxuFBHsItWGKJE9xnr8XXBCNMd1OBj6qnSjGDZTgIUy6EpZQEdiJd9ib4CKny%2FbwSE58%2FhsBDeRjQAxn6UwR2%2FpBgEne%2BYY74n7L%2B9G2CpCiDxvgwlIeWPc0zBfPCaeHaHT1eiNKJL9XKIspL4Ldg4rxN%2BexzbcXZFGywlC4%2FqLiqU93fvTDny%2FgYy7MhanpAC9dgIdYJ0zuM05piBpPZw6ngr2ckFPE6fCR22guhgUJMNbrkb0GOqUB7XKoKnazm0gD%2FEzWRt0%2FP4890RJiBMatJRPhlNJFlTJeUbM0rDtgjFREBFebdWhVMW%2BdHNwGOc143Oq9NsBXw154ZCzZpmvH7JAPB1qzzx5jU3bUtx7jM97WPkRuKCvWqaS2Up3GwxEXG9RVP1bbKpT0WCxaoz8Op8qlwyOM0l9gySMVuOTDVXM1s1AiOH3bHXMBYhq1PBKo3dy0kAQ1UXeMt5sr&X-Amz-Signature=99f8bdd4b074b49a3d64b427daece57e21e8aa4b26a0dc1eabd536079b89a0a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDKPSC3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDU6i8mhfzhFPUfXqOViY%2FHw1cg8kSeLZ6q16eM2RuPfAIgRkVrh7BDKJvM9Y8av%2FuuiAPXbajV0u%2FKoEcED5avr54q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOTXG8SdmHYP0cQhvircA75pKTcfys%2FYUF0vguXPz1o9Ht8Vfyxdt20K%2F%2Ftv30QDX9ahDW%2FrpF4azBDuXe4yI%2FhIjzGmymW8fT7fmumDrTbOCika2FXvKmLgPQRvdfdr5iEEOIivpuW64IWONRtaNX%2F8EfSytYCvf0dt%2F76pnifqxsSeWiD%2FzXiyfcR5UCH8tkh1HLWqi38g1PwAvIW4Z2VMozC20EyZKfX3Vjy4rjTl3r7jHWKSXU8up7PTDIWEXqH0OHwSgJBugbaNlHgyndlKUfv3%2BPjoNBEcMs%2FqBkoVeFijXpe25O6Lz5QsBMRwvj3RIpmEiKyfVPX9vj%2BTSeLrAog1m21CTT1e0Z9WY89dHE3J3rUyTZ2g5WhnGBIRQMeSJmQV41y5k9h6RuqxBrWtquQeFwo4gRohwxuFBHsItWGKJE9xnr8XXBCNMd1OBj6qnSjGDZTgIUy6EpZQEdiJd9ib4CKny%2FbwSE58%2FhsBDeRjQAxn6UwR2%2FpBgEne%2BYY74n7L%2B9G2CpCiDxvgwlIeWPc0zBfPCaeHaHT1eiNKJL9XKIspL4Ldg4rxN%2BexzbcXZFGywlC4%2FqLiqU93fvTDny%2FgYy7MhanpAC9dgIdYJ0zuM05piBpPZw6ngr2ckFPE6fCR22guhgUJMNbrkb0GOqUB7XKoKnazm0gD%2FEzWRt0%2FP4890RJiBMatJRPhlNJFlTJeUbM0rDtgjFREBFebdWhVMW%2BdHNwGOc143Oq9NsBXw154ZCzZpmvH7JAPB1qzzx5jU3bUtx7jM97WPkRuKCvWqaS2Up3GwxEXG9RVP1bbKpT0WCxaoz8Op8qlwyOM0l9gySMVuOTDVXM1s1AiOH3bHXMBYhq1PBKo3dy0kAQ1UXeMt5sr&X-Amz-Signature=12316c0de6faf1fe60ed360fc7fc505d6fd209a1bd55f35352aba66f49e7c102&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUDKPSC3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQDU6i8mhfzhFPUfXqOViY%2FHw1cg8kSeLZ6q16eM2RuPfAIgRkVrh7BDKJvM9Y8av%2FuuiAPXbajV0u%2FKoEcED5avr54q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDOTXG8SdmHYP0cQhvircA75pKTcfys%2FYUF0vguXPz1o9Ht8Vfyxdt20K%2F%2Ftv30QDX9ahDW%2FrpF4azBDuXe4yI%2FhIjzGmymW8fT7fmumDrTbOCika2FXvKmLgPQRvdfdr5iEEOIivpuW64IWONRtaNX%2F8EfSytYCvf0dt%2F76pnifqxsSeWiD%2FzXiyfcR5UCH8tkh1HLWqi38g1PwAvIW4Z2VMozC20EyZKfX3Vjy4rjTl3r7jHWKSXU8up7PTDIWEXqH0OHwSgJBugbaNlHgyndlKUfv3%2BPjoNBEcMs%2FqBkoVeFijXpe25O6Lz5QsBMRwvj3RIpmEiKyfVPX9vj%2BTSeLrAog1m21CTT1e0Z9WY89dHE3J3rUyTZ2g5WhnGBIRQMeSJmQV41y5k9h6RuqxBrWtquQeFwo4gRohwxuFBHsItWGKJE9xnr8XXBCNMd1OBj6qnSjGDZTgIUy6EpZQEdiJd9ib4CKny%2FbwSE58%2FhsBDeRjQAxn6UwR2%2FpBgEne%2BYY74n7L%2B9G2CpCiDxvgwlIeWPc0zBfPCaeHaHT1eiNKJL9XKIspL4Ldg4rxN%2BexzbcXZFGywlC4%2FqLiqU93fvTDny%2FgYy7MhanpAC9dgIdYJ0zuM05piBpPZw6ngr2ckFPE6fCR22guhgUJMNbrkb0GOqUB7XKoKnazm0gD%2FEzWRt0%2FP4890RJiBMatJRPhlNJFlTJeUbM0rDtgjFREBFebdWhVMW%2BdHNwGOc143Oq9NsBXw154ZCzZpmvH7JAPB1qzzx5jU3bUtx7jM97WPkRuKCvWqaS2Up3GwxEXG9RVP1bbKpT0WCxaoz8Op8qlwyOM0l9gySMVuOTDVXM1s1AiOH3bHXMBYhq1PBKo3dy0kAQ1UXeMt5sr&X-Amz-Signature=e2a0ff5b5143ad607a1ad91eeedd6c06072203cead77f0cc912982e123e6374d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OKMOF6M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDHH3kTjd9jhj8RGF7C339yu1KJIwKjrI6FzRVcjN809QIhAKceO2fjWwKvv2l25utmaYg4yxYlvSr6kx7Lx1Yk1totKv8DCFoQABoMNjM3NDIzMTgzODA1IgzfqpQQXAxIKfnGO2oq3AONFhYG0n9v4J32lL4TRms%2FohL4sPx7TORJDgABoxhkJ1hPzZNiQHo6xyZK%2F%2Bj%2FEBAni7bqfyQIvyVV%2F7L217H0CCd%2F8G2euVtrryu2Qf8iMimX756BkdXPSiP52nyp0v8KSaqHjoNae%2Fq7FG4MIfF2eg7HkJriPPbTwWCjQc84zwdQhu7BdaaTcdr628ATV095HC6eylGMxChtg8J14%2Fpn5lKpdmKuF%2F%2BiI97PetN08ATfkql1wWRkEJ1df%2BoJWMn%2FgxfPlfS8L6meBWmr9DSi%2FtGmDVSIUFSA95BLnTO%2BXXZVbWhsV2VY2zsF5LukpAs0XX7ZzDu7UjpGwinpbzQh2jacE3dM%2Bv6QQYaa4QvwQVpiaUyPND2U1%2FrYr0STxlErKiGy6Jm87T3WtWy6WdYFyyZo%2BOZpgejRDptj1CvlCwrmr7ve4HV14lU0Y1CAXAw6yWRNsmiZVihtJSLhJEeAHK4bjRoea1l8GQf0lDCbX9%2Fd0RQiRZETVE2tZ5917OF%2Fi6ZT5ulUEYK6ET%2FitZYivbZaHZ5rMO628569WgWLJ%2FlBq6G8mpHBgQKUf7ZX67HpHu9qG8tIZbbn6E8oCvguNQ8tFC2QbIwr2Vbbf4%2F1musnX4AeQChDZhSMjDD%2F65G9BjqkAYz2MkypneRzn4I0%2FFiZxZAWKgtjgqDFM%2FtniP%2FcQph4MMvFdHnjBaLvZIH%2FY635lyOEu7nS24xtt40frGo1wf4%2B2%2FoASmX%2FSvNhdfeXKXTnLkIWqEoA38zsVXpPcKzpiu06UsX4aHi%2BEMy0LtvogB0%2BuZCZim06hllGI5YBrVRsg3jwEGM837cl4KwXSHMlaXT2lrZsbWj1uYMIHHl75mSKbnHv&X-Amz-Signature=f611e05b5a1bb782c16b9e0e7f1bac98fbc5e55671df5ad0e3ae4a91996f6f3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXIYWUXM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIAqwZMqW3yRG1cq1KoIq%2Fe1uPsPJF%2BwJbjTBkHjxZpntAiEArIrXU9GPLdsfvGAAUCf0r4t73o3d7ZnCOMgtO7c%2B%2FoYq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDGOYtLTGb%2FWFLDIXSyrcA9QyY5SCxKGXKJzuNe0rBxqBUdIe2JRrUyO6uA4jlszu4j%2B1whgQ%2Bphu8aN48WiqYGa4ZZxOAAd9Yd1%2BTrPREJytSUc%2BaU%2Bl5BYhjKMRieHKTghF%2F3FlZ45I80KLM9iK1o%2Fd3jBUz9tRUEDtDKuBTbHD1pq9%2FVsrr7As5czhdfgTYI8Gz9Ppel6inRQXhhhfc05kLlO%2FPVA1g5XZfJyRFBDSYbmFlwJwkbloiDR6jHthS3Bu91FGcyfCeOhgJOquq99%2BhewU5qO44wAc51gI3LzkrtKx1RvKVFUIzYfP2G3w0DT7aXQctroBJdFUxpmBm5ZKc%2FDR8c70kmwcDyISreiwcaorw4DV4qGKhTUpZSe6OH2CCvGUKCSVig%2FjOQi2zRr8fWgzi9YE2XhPchdjm4vxXMSlVjAYh3OMtSTbQlQPakLQu%2FV2namj5AyGGs%2BPW1eWTzbeeFp%2FttIMGeYdOc5dOMct66kKHAApZ28SgA7Qs1jbtirxn7KSkNu4kpEJ5P2E7IHdufCHBro7Swspm5W2bGhCtRpWtG%2Fy1olEpLz5vdMrrXKy3P09JqqzIu0fJ7A36DunMJx5aZ4nKwis6xyRyhL49gjzgwYYehgdUli8YUy9RCzjJU%2BCGxCCMInskb0GOqUBP1bzmA6FCkQp7vzvsS%2BFSQUuSniYZEweAdM9L1MJagSQSVffvLfpTkhGqVS4cYKMsDjyqTSO95%2FXNonPc7R4noYug9D05RXSQZf5i2LW821CWYK5es1B59OHvEQDccUQNfOUz0GZi3WDSnApba2cpFJpjkXCFGA%2Fy8E7Ja3yvmeUVakatE2KQMcysnquyAdfmBbTwlDjzlxonJirU7wKBCNno%2FMn&X-Amz-Signature=d3fa25b984d59aa6e477d8de2a6d33e23c0ddce9260e85979e9eaebdb96384ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX3D2EEU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIEYzl3ElMxf8DLgm3Q4vG07SotToJNQMHkl8r4RxuzUHAiAYaMDTH2cKkM0C8l78V1xdd%2FRKQyHbQdGFDMeAivlXRSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMNquuGaHxDSj4wys4KtwDqIXi2MCWXjTn3zMYqtgZbycjisdxnKMnwyUYQ%2Fw8YkbzL4myr1p1aEAtNw%2BC55Ryio3%2ByWFdU6VrlLjgrW3vK%2BBUNehud7r4Nie9Zndc4Dm8Siokk93UeIwd20EriJbS826TFyRqLs%2FGMZDPEvv1pi3qOmWStvAcCxbzpMEWHjd15GG47FN7035ujyLBtdlO1JIdJ2Xn01VnjWV5xNqKjXcVntkqi1xUsBEkODBBOZ0ounokrGhOS3HMUZMj0NxtyQXPAjKFL9wma%2BE302ebXOwtewWbNP7ABME9Z3dkrdC%2FXfcqX4iLb8wP6kIN%2BwFUjWk5bALSJKQBGUNdpj0Nia6qv%2B5CAEe%2BaIGj6FIXpoEYG3IqBmz9I7J%2B6hxl6vxBaB73jI%2BkQfGyXugccHA0dN2x5nbV3uY2PdSqvGJqzrXI3BrWR47SwNk8pfky6R671di1j7dv8Uuanj%2B%2BVaPNLcnrrVr8elYVpG1TE%2FpT%2BdHJ4bcrlLIQ88EUGnQohAOLQ2bD4kATr7jzzudI4dpmHBcbkkyW0Tq3W9OHXG6mXG1ygko5%2BuhL4BuldVqEtK9OAcJf6jfqSGdTDjTDogwlK1H%2BT7JwcKOrNOtuFQWO08%2Fx5EAtaSstKE1tWW0w3uuRvQY6pgEL9wiTPBpwf9bo3NHHfnGMOFJ%2Fj9b9QnUQ0VFukf7jjfyR%2BSSjDNJRbXvpsyFzjYW%2BW3JhISQZW8nX4D093JoZq54PFdaRaT7%2BJQvbqys%2FAKCi3NicR7WGAswlmS8pT5Vcv2c1eos8gNiYecvg6LjnWzgcsNQzjEuhQDylqAk3kIAEoXFnRCQHDFc8Byu0sCbLBz5dSIO23tOb7rW1Nh6uvf10XBqh&X-Amz-Signature=22de00f31c94397cc04513e6ce7a709c501bcc26d95915acb0ce8d20927b5248&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WX3D2EEU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIEYzl3ElMxf8DLgm3Q4vG07SotToJNQMHkl8r4RxuzUHAiAYaMDTH2cKkM0C8l78V1xdd%2FRKQyHbQdGFDMeAivlXRSr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMNquuGaHxDSj4wys4KtwDqIXi2MCWXjTn3zMYqtgZbycjisdxnKMnwyUYQ%2Fw8YkbzL4myr1p1aEAtNw%2BC55Ryio3%2ByWFdU6VrlLjgrW3vK%2BBUNehud7r4Nie9Zndc4Dm8Siokk93UeIwd20EriJbS826TFyRqLs%2FGMZDPEvv1pi3qOmWStvAcCxbzpMEWHjd15GG47FN7035ujyLBtdlO1JIdJ2Xn01VnjWV5xNqKjXcVntkqi1xUsBEkODBBOZ0ounokrGhOS3HMUZMj0NxtyQXPAjKFL9wma%2BE302ebXOwtewWbNP7ABME9Z3dkrdC%2FXfcqX4iLb8wP6kIN%2BwFUjWk5bALSJKQBGUNdpj0Nia6qv%2B5CAEe%2BaIGj6FIXpoEYG3IqBmz9I7J%2B6hxl6vxBaB73jI%2BkQfGyXugccHA0dN2x5nbV3uY2PdSqvGJqzrXI3BrWR47SwNk8pfky6R671di1j7dv8Uuanj%2B%2BVaPNLcnrrVr8elYVpG1TE%2FpT%2BdHJ4bcrlLIQ88EUGnQohAOLQ2bD4kATr7jzzudI4dpmHBcbkkyW0Tq3W9OHXG6mXG1ygko5%2BuhL4BuldVqEtK9OAcJf6jfqSGdTDjTDogwlK1H%2BT7JwcKOrNOtuFQWO08%2Fx5EAtaSstKE1tWW0w3uuRvQY6pgEL9wiTPBpwf9bo3NHHfnGMOFJ%2Fj9b9QnUQ0VFukf7jjfyR%2BSSjDNJRbXvpsyFzjYW%2BW3JhISQZW8nX4D093JoZq54PFdaRaT7%2BJQvbqys%2FAKCi3NicR7WGAswlmS8pT5Vcv2c1eos8gNiYecvg6LjnWzgcsNQzjEuhQDylqAk3kIAEoXFnRCQHDFc8Byu0sCbLBz5dSIO23tOb7rW1Nh6uvf10XBqh&X-Amz-Signature=bbd0af682252402a7b3f8b94bae7d6f02129d50669f2dcee191aec80be0b8d4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
