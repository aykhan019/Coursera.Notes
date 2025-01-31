

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676FOFSL2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRxCJGbtWeaHfPRKbGXO2Cx1FbYtKzB1hqEIXgMHZ39AiByCyflYDrh769YZZG7Ob30Csp5j9yhs%2FWcbR6y%2Bn%2FbJiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsqS8wyWkoVmnDqs2KtwDen4abrQXwNldqylozAqwFm2bS97LH%2F2Yc5FImx5TOUZoy8ADnMKjLUnZUIvsywBuqrITG9BtkGe%2BHf0CfvnL8Sh5rafqB4L0NaqNRoSnjzJTJz%2BTv68ogL8NksZPtjt4ibbCgB%2BHQw7bd92aVKgPa8SzkAm0AaCDZD0brlSCDgq7JZ30Ez3MFJiBunjpNY8PiR5MnMvqvx%2FZ6kChSQPBsD15jYH1xK7SfvsnIa%2BcjiEcdsUc96kURJfunSIoii84m7ovHDQwCUKvia62NU8%2BGEhyR9MESAJ5xajtxCm4XbvTnpwJxPy5GMKp5y53na2tS4V9IylOuDXcP%2Bp4qc2lSFipTr9ejYgmCpPSNUEv8GhByQtIZakO6SxBh1OHowbGy2b%2FjuGawaZEvNFWA3qfcyYaW0fY%2BRw4JmExcdu%2FlhggeXmLsbHjBXsiDvePu12eoUjnCWhi9dubbNKwTOYSbQPUw6%2Fl4Dhef3FIqt%2FOO133FFdJlrxiu0CuQa6hmzohkAfH6qKAHTtOYr0rAkQREGNUB5LVDmtg7WQFNINVujeHbwqJiC0vzQ7fuXAAVEqgHHV0FOI6oP4s68oiRtZ%2FmedjBi6tECFCaBGvXUgU6Y8Z%2BQdBEJUmvIaJbR4wkdDwvAY6pgHKHviej4PNc93jjmbkxGrQ%2Bjs9FpV7L%2Bx2EBLPzvYtZOmdhc49fvRP%2BKmbULIhYi9PLjq%2BB%2Bb3PcZxwWcY1CUJ8bjgB0Cefoa1uRqeNmp7nOcfZkQlCwXyoW3G8k0fM%2FQR52ZAkUBIK7TEwEFgFSSeJnw1WtMPHE13INzPXtwkRfKjZgaYeF3vdWOuP3iehplrRBIA4kBXZ6Y8IluxVsvqJweWkmo6&X-Amz-Signature=f897198d7ca1bc23396101ab7e6748ca75e660e7cc148b88fc5e98c9250efc72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676FOFSL2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRxCJGbtWeaHfPRKbGXO2Cx1FbYtKzB1hqEIXgMHZ39AiByCyflYDrh769YZZG7Ob30Csp5j9yhs%2FWcbR6y%2Bn%2FbJiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsqS8wyWkoVmnDqs2KtwDen4abrQXwNldqylozAqwFm2bS97LH%2F2Yc5FImx5TOUZoy8ADnMKjLUnZUIvsywBuqrITG9BtkGe%2BHf0CfvnL8Sh5rafqB4L0NaqNRoSnjzJTJz%2BTv68ogL8NksZPtjt4ibbCgB%2BHQw7bd92aVKgPa8SzkAm0AaCDZD0brlSCDgq7JZ30Ez3MFJiBunjpNY8PiR5MnMvqvx%2FZ6kChSQPBsD15jYH1xK7SfvsnIa%2BcjiEcdsUc96kURJfunSIoii84m7ovHDQwCUKvia62NU8%2BGEhyR9MESAJ5xajtxCm4XbvTnpwJxPy5GMKp5y53na2tS4V9IylOuDXcP%2Bp4qc2lSFipTr9ejYgmCpPSNUEv8GhByQtIZakO6SxBh1OHowbGy2b%2FjuGawaZEvNFWA3qfcyYaW0fY%2BRw4JmExcdu%2FlhggeXmLsbHjBXsiDvePu12eoUjnCWhi9dubbNKwTOYSbQPUw6%2Fl4Dhef3FIqt%2FOO133FFdJlrxiu0CuQa6hmzohkAfH6qKAHTtOYr0rAkQREGNUB5LVDmtg7WQFNINVujeHbwqJiC0vzQ7fuXAAVEqgHHV0FOI6oP4s68oiRtZ%2FmedjBi6tECFCaBGvXUgU6Y8Z%2BQdBEJUmvIaJbR4wkdDwvAY6pgHKHviej4PNc93jjmbkxGrQ%2Bjs9FpV7L%2Bx2EBLPzvYtZOmdhc49fvRP%2BKmbULIhYi9PLjq%2BB%2Bb3PcZxwWcY1CUJ8bjgB0Cefoa1uRqeNmp7nOcfZkQlCwXyoW3G8k0fM%2FQR52ZAkUBIK7TEwEFgFSSeJnw1WtMPHE13INzPXtwkRfKjZgaYeF3vdWOuP3iehplrRBIA4kBXZ6Y8IluxVsvqJweWkmo6&X-Amz-Signature=57cf4f453b3da10d5f88338d91212b8fbd70cf31819e7c6c286ddfed97ab62e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676FOFSL2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRxCJGbtWeaHfPRKbGXO2Cx1FbYtKzB1hqEIXgMHZ39AiByCyflYDrh769YZZG7Ob30Csp5j9yhs%2FWcbR6y%2Bn%2FbJiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsqS8wyWkoVmnDqs2KtwDen4abrQXwNldqylozAqwFm2bS97LH%2F2Yc5FImx5TOUZoy8ADnMKjLUnZUIvsywBuqrITG9BtkGe%2BHf0CfvnL8Sh5rafqB4L0NaqNRoSnjzJTJz%2BTv68ogL8NksZPtjt4ibbCgB%2BHQw7bd92aVKgPa8SzkAm0AaCDZD0brlSCDgq7JZ30Ez3MFJiBunjpNY8PiR5MnMvqvx%2FZ6kChSQPBsD15jYH1xK7SfvsnIa%2BcjiEcdsUc96kURJfunSIoii84m7ovHDQwCUKvia62NU8%2BGEhyR9MESAJ5xajtxCm4XbvTnpwJxPy5GMKp5y53na2tS4V9IylOuDXcP%2Bp4qc2lSFipTr9ejYgmCpPSNUEv8GhByQtIZakO6SxBh1OHowbGy2b%2FjuGawaZEvNFWA3qfcyYaW0fY%2BRw4JmExcdu%2FlhggeXmLsbHjBXsiDvePu12eoUjnCWhi9dubbNKwTOYSbQPUw6%2Fl4Dhef3FIqt%2FOO133FFdJlrxiu0CuQa6hmzohkAfH6qKAHTtOYr0rAkQREGNUB5LVDmtg7WQFNINVujeHbwqJiC0vzQ7fuXAAVEqgHHV0FOI6oP4s68oiRtZ%2FmedjBi6tECFCaBGvXUgU6Y8Z%2BQdBEJUmvIaJbR4wkdDwvAY6pgHKHviej4PNc93jjmbkxGrQ%2Bjs9FpV7L%2Bx2EBLPzvYtZOmdhc49fvRP%2BKmbULIhYi9PLjq%2BB%2Bb3PcZxwWcY1CUJ8bjgB0Cefoa1uRqeNmp7nOcfZkQlCwXyoW3G8k0fM%2FQR52ZAkUBIK7TEwEFgFSSeJnw1WtMPHE13INzPXtwkRfKjZgaYeF3vdWOuP3iehplrRBIA4kBXZ6Y8IluxVsvqJweWkmo6&X-Amz-Signature=7bcdf12c9a819bc795fa10eb8e1790431a9fb025eaf479242e617c3d93f22007&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676FOFSL2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRxCJGbtWeaHfPRKbGXO2Cx1FbYtKzB1hqEIXgMHZ39AiByCyflYDrh769YZZG7Ob30Csp5j9yhs%2FWcbR6y%2Bn%2FbJiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsqS8wyWkoVmnDqs2KtwDen4abrQXwNldqylozAqwFm2bS97LH%2F2Yc5FImx5TOUZoy8ADnMKjLUnZUIvsywBuqrITG9BtkGe%2BHf0CfvnL8Sh5rafqB4L0NaqNRoSnjzJTJz%2BTv68ogL8NksZPtjt4ibbCgB%2BHQw7bd92aVKgPa8SzkAm0AaCDZD0brlSCDgq7JZ30Ez3MFJiBunjpNY8PiR5MnMvqvx%2FZ6kChSQPBsD15jYH1xK7SfvsnIa%2BcjiEcdsUc96kURJfunSIoii84m7ovHDQwCUKvia62NU8%2BGEhyR9MESAJ5xajtxCm4XbvTnpwJxPy5GMKp5y53na2tS4V9IylOuDXcP%2Bp4qc2lSFipTr9ejYgmCpPSNUEv8GhByQtIZakO6SxBh1OHowbGy2b%2FjuGawaZEvNFWA3qfcyYaW0fY%2BRw4JmExcdu%2FlhggeXmLsbHjBXsiDvePu12eoUjnCWhi9dubbNKwTOYSbQPUw6%2Fl4Dhef3FIqt%2FOO133FFdJlrxiu0CuQa6hmzohkAfH6qKAHTtOYr0rAkQREGNUB5LVDmtg7WQFNINVujeHbwqJiC0vzQ7fuXAAVEqgHHV0FOI6oP4s68oiRtZ%2FmedjBi6tECFCaBGvXUgU6Y8Z%2BQdBEJUmvIaJbR4wkdDwvAY6pgHKHviej4PNc93jjmbkxGrQ%2Bjs9FpV7L%2Bx2EBLPzvYtZOmdhc49fvRP%2BKmbULIhYi9PLjq%2BB%2Bb3PcZxwWcY1CUJ8bjgB0Cefoa1uRqeNmp7nOcfZkQlCwXyoW3G8k0fM%2FQR52ZAkUBIK7TEwEFgFSSeJnw1WtMPHE13INzPXtwkRfKjZgaYeF3vdWOuP3iehplrRBIA4kBXZ6Y8IluxVsvqJweWkmo6&X-Amz-Signature=d0a7d1434ca86b265c8c10a804adcb7322e6688bf7771595ecaa77a2578ad52e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676FOFSL2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRxCJGbtWeaHfPRKbGXO2Cx1FbYtKzB1hqEIXgMHZ39AiByCyflYDrh769YZZG7Ob30Csp5j9yhs%2FWcbR6y%2Bn%2FbJiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsqS8wyWkoVmnDqs2KtwDen4abrQXwNldqylozAqwFm2bS97LH%2F2Yc5FImx5TOUZoy8ADnMKjLUnZUIvsywBuqrITG9BtkGe%2BHf0CfvnL8Sh5rafqB4L0NaqNRoSnjzJTJz%2BTv68ogL8NksZPtjt4ibbCgB%2BHQw7bd92aVKgPa8SzkAm0AaCDZD0brlSCDgq7JZ30Ez3MFJiBunjpNY8PiR5MnMvqvx%2FZ6kChSQPBsD15jYH1xK7SfvsnIa%2BcjiEcdsUc96kURJfunSIoii84m7ovHDQwCUKvia62NU8%2BGEhyR9MESAJ5xajtxCm4XbvTnpwJxPy5GMKp5y53na2tS4V9IylOuDXcP%2Bp4qc2lSFipTr9ejYgmCpPSNUEv8GhByQtIZakO6SxBh1OHowbGy2b%2FjuGawaZEvNFWA3qfcyYaW0fY%2BRw4JmExcdu%2FlhggeXmLsbHjBXsiDvePu12eoUjnCWhi9dubbNKwTOYSbQPUw6%2Fl4Dhef3FIqt%2FOO133FFdJlrxiu0CuQa6hmzohkAfH6qKAHTtOYr0rAkQREGNUB5LVDmtg7WQFNINVujeHbwqJiC0vzQ7fuXAAVEqgHHV0FOI6oP4s68oiRtZ%2FmedjBi6tECFCaBGvXUgU6Y8Z%2BQdBEJUmvIaJbR4wkdDwvAY6pgHKHviej4PNc93jjmbkxGrQ%2Bjs9FpV7L%2Bx2EBLPzvYtZOmdhc49fvRP%2BKmbULIhYi9PLjq%2BB%2Bb3PcZxwWcY1CUJ8bjgB0Cefoa1uRqeNmp7nOcfZkQlCwXyoW3G8k0fM%2FQR52ZAkUBIK7TEwEFgFSSeJnw1WtMPHE13INzPXtwkRfKjZgaYeF3vdWOuP3iehplrRBIA4kBXZ6Y8IluxVsvqJweWkmo6&X-Amz-Signature=f42c9938b96ad33243680bf77548ee2a15cfa93a73a0440ae0a8b30c65be4eb7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676FOFSL2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRxCJGbtWeaHfPRKbGXO2Cx1FbYtKzB1hqEIXgMHZ39AiByCyflYDrh769YZZG7Ob30Csp5j9yhs%2FWcbR6y%2Bn%2FbJiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsqS8wyWkoVmnDqs2KtwDen4abrQXwNldqylozAqwFm2bS97LH%2F2Yc5FImx5TOUZoy8ADnMKjLUnZUIvsywBuqrITG9BtkGe%2BHf0CfvnL8Sh5rafqB4L0NaqNRoSnjzJTJz%2BTv68ogL8NksZPtjt4ibbCgB%2BHQw7bd92aVKgPa8SzkAm0AaCDZD0brlSCDgq7JZ30Ez3MFJiBunjpNY8PiR5MnMvqvx%2FZ6kChSQPBsD15jYH1xK7SfvsnIa%2BcjiEcdsUc96kURJfunSIoii84m7ovHDQwCUKvia62NU8%2BGEhyR9MESAJ5xajtxCm4XbvTnpwJxPy5GMKp5y53na2tS4V9IylOuDXcP%2Bp4qc2lSFipTr9ejYgmCpPSNUEv8GhByQtIZakO6SxBh1OHowbGy2b%2FjuGawaZEvNFWA3qfcyYaW0fY%2BRw4JmExcdu%2FlhggeXmLsbHjBXsiDvePu12eoUjnCWhi9dubbNKwTOYSbQPUw6%2Fl4Dhef3FIqt%2FOO133FFdJlrxiu0CuQa6hmzohkAfH6qKAHTtOYr0rAkQREGNUB5LVDmtg7WQFNINVujeHbwqJiC0vzQ7fuXAAVEqgHHV0FOI6oP4s68oiRtZ%2FmedjBi6tECFCaBGvXUgU6Y8Z%2BQdBEJUmvIaJbR4wkdDwvAY6pgHKHviej4PNc93jjmbkxGrQ%2Bjs9FpV7L%2Bx2EBLPzvYtZOmdhc49fvRP%2BKmbULIhYi9PLjq%2BB%2Bb3PcZxwWcY1CUJ8bjgB0Cefoa1uRqeNmp7nOcfZkQlCwXyoW3G8k0fM%2FQR52ZAkUBIK7TEwEFgFSSeJnw1WtMPHE13INzPXtwkRfKjZgaYeF3vdWOuP3iehplrRBIA4kBXZ6Y8IluxVsvqJweWkmo6&X-Amz-Signature=7e6dfbb62b51a9fcec8beb895d1e538dc2da77290298dcbec5c6116352b7947a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676FOFSL2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRxCJGbtWeaHfPRKbGXO2Cx1FbYtKzB1hqEIXgMHZ39AiByCyflYDrh769YZZG7Ob30Csp5j9yhs%2FWcbR6y%2Bn%2FbJiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsqS8wyWkoVmnDqs2KtwDen4abrQXwNldqylozAqwFm2bS97LH%2F2Yc5FImx5TOUZoy8ADnMKjLUnZUIvsywBuqrITG9BtkGe%2BHf0CfvnL8Sh5rafqB4L0NaqNRoSnjzJTJz%2BTv68ogL8NksZPtjt4ibbCgB%2BHQw7bd92aVKgPa8SzkAm0AaCDZD0brlSCDgq7JZ30Ez3MFJiBunjpNY8PiR5MnMvqvx%2FZ6kChSQPBsD15jYH1xK7SfvsnIa%2BcjiEcdsUc96kURJfunSIoii84m7ovHDQwCUKvia62NU8%2BGEhyR9MESAJ5xajtxCm4XbvTnpwJxPy5GMKp5y53na2tS4V9IylOuDXcP%2Bp4qc2lSFipTr9ejYgmCpPSNUEv8GhByQtIZakO6SxBh1OHowbGy2b%2FjuGawaZEvNFWA3qfcyYaW0fY%2BRw4JmExcdu%2FlhggeXmLsbHjBXsiDvePu12eoUjnCWhi9dubbNKwTOYSbQPUw6%2Fl4Dhef3FIqt%2FOO133FFdJlrxiu0CuQa6hmzohkAfH6qKAHTtOYr0rAkQREGNUB5LVDmtg7WQFNINVujeHbwqJiC0vzQ7fuXAAVEqgHHV0FOI6oP4s68oiRtZ%2FmedjBi6tECFCaBGvXUgU6Y8Z%2BQdBEJUmvIaJbR4wkdDwvAY6pgHKHviej4PNc93jjmbkxGrQ%2Bjs9FpV7L%2Bx2EBLPzvYtZOmdhc49fvRP%2BKmbULIhYi9PLjq%2BB%2Bb3PcZxwWcY1CUJ8bjgB0Cefoa1uRqeNmp7nOcfZkQlCwXyoW3G8k0fM%2FQR52ZAkUBIK7TEwEFgFSSeJnw1WtMPHE13INzPXtwkRfKjZgaYeF3vdWOuP3iehplrRBIA4kBXZ6Y8IluxVsvqJweWkmo6&X-Amz-Signature=07e2d1a0ee1956723e113d2996354482326f628910945b023c4a6f4e5fac4bcf&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676FOFSL2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHRxCJGbtWeaHfPRKbGXO2Cx1FbYtKzB1hqEIXgMHZ39AiByCyflYDrh769YZZG7Ob30Csp5j9yhs%2FWcbR6y%2Bn%2FbJiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsqS8wyWkoVmnDqs2KtwDen4abrQXwNldqylozAqwFm2bS97LH%2F2Yc5FImx5TOUZoy8ADnMKjLUnZUIvsywBuqrITG9BtkGe%2BHf0CfvnL8Sh5rafqB4L0NaqNRoSnjzJTJz%2BTv68ogL8NksZPtjt4ibbCgB%2BHQw7bd92aVKgPa8SzkAm0AaCDZD0brlSCDgq7JZ30Ez3MFJiBunjpNY8PiR5MnMvqvx%2FZ6kChSQPBsD15jYH1xK7SfvsnIa%2BcjiEcdsUc96kURJfunSIoii84m7ovHDQwCUKvia62NU8%2BGEhyR9MESAJ5xajtxCm4XbvTnpwJxPy5GMKp5y53na2tS4V9IylOuDXcP%2Bp4qc2lSFipTr9ejYgmCpPSNUEv8GhByQtIZakO6SxBh1OHowbGy2b%2FjuGawaZEvNFWA3qfcyYaW0fY%2BRw4JmExcdu%2FlhggeXmLsbHjBXsiDvePu12eoUjnCWhi9dubbNKwTOYSbQPUw6%2Fl4Dhef3FIqt%2FOO133FFdJlrxiu0CuQa6hmzohkAfH6qKAHTtOYr0rAkQREGNUB5LVDmtg7WQFNINVujeHbwqJiC0vzQ7fuXAAVEqgHHV0FOI6oP4s68oiRtZ%2FmedjBi6tECFCaBGvXUgU6Y8Z%2BQdBEJUmvIaJbR4wkdDwvAY6pgHKHviej4PNc93jjmbkxGrQ%2Bjs9FpV7L%2Bx2EBLPzvYtZOmdhc49fvRP%2BKmbULIhYi9PLjq%2BB%2Bb3PcZxwWcY1CUJ8bjgB0Cefoa1uRqeNmp7nOcfZkQlCwXyoW3G8k0fM%2FQR52ZAkUBIK7TEwEFgFSSeJnw1WtMPHE13INzPXtwkRfKjZgaYeF3vdWOuP3iehplrRBIA4kBXZ6Y8IluxVsvqJweWkmo6&X-Amz-Signature=1b284e1d3e2741b413542097786e074c1a51244d930c05d12ea69583fbd7a157&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RERA4XEU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2BlsKhqImM92jNUclsuFj6tqDL0W00uQS9g8IJiQYh%2BAiAMFL0obuovFqOEXFm1l4MesEgDsCUuHVHvUieWHQgn8iqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK7sv%2BY31RpZCYdbUKtwDAwkPc7tzZ1h3li0yh1cMGF%2Bm2GIlB0BgPkou8MGRS5dAn40iTxzIdPoZK7Td6FA4VW%2BTDCUaqbwCUZ4XoGnw%2FD925c%2FqYwVL%2BEmyHBn%2BKsPf2kjir48VybB%2FIecWpMtgYldsWSPRRJaGDg8RTptk0ft9%2BXgYdNAw0PvdWZLp0Jo4RTnZr9krzqX6U%2F%2FDPwqtjrd%2FSaBa%2B%2FHdJmaTMFZZtmXXe69yC1X5lT6mKOJkllkkWBTnDmEwI6m2j29RocHOnCTb0XLBiLRCC%2B2Hy%2BzTXd4hERRCIVCm6WuWw9%2Bp3IZikGlFjYk3vKzRYKf0FwqJbUxoW5gZBZyKMb%2FVf4WPm3brw4L9VC89DDjJYszkrKe2kl0AhIRz%2B7UgzTEG%2BngaiAX6UBcT9U3eqd2suyH3BC01bsTM3DqPiYLT9rXSHWqvYnuGTI7Bfba9DGW4USChsRoe%2BbJHELuUhCUH%2Ft87hMGaE9JVKKu54o29LEKkZhRaVGl7YIZ1QmVmzZLAZPb8tU5ixw3MY%2FGRiCsHaT%2FCwJlkznMc2pq0YGnCIOKH6fYn9823uF39QWKy7R3mDLORecKITtw4od%2BJKI3S6zXtMq7smeNMLyVJLs3W%2F7DYzHA6QbM4m7PFJZLbqvgwktDwvAY6pgGsB%2BArXw40j2PrT5M%2FVDmDol4H4SIIsgkpOc%2BCf9Ub7vwL%2BBEB6opQvhIMVeINitLTvJWJYqNEbXzJebBDNKTtPxA%2FKeXYhndJDoTb7F%2BLDrvQ%2BRF5Sb%2Fv5q%2BkRh0K%2BREl8PoNLm9MOkRettNY74%2F1Pxlls7JojmNlwKJ%2B1jPWf3NSfy1s8ZWAsJuB8EWM%2BmaE23Y1zIRPc0Bf2r41yiccScVhzsVf&X-Amz-Signature=4ad0f968b2f59cd628a64e64d4bfcd0c169090933c5cf582e7de1383bfef841a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLTJK7NA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEvwoCLgptE42hP1Of0iSobVjo6ShaCmrrpoXySi3v73AiABRGcQvQzmEQpenNcki0K%2Bqrh%2Bhf8ucJA7cz6HlPl%2BsiqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMflfhjF15jLNT0lrRKtwDI703NMuW8jiTAybBxpZtKAAS4QwC0c9wQWx15R0jooUihh1HOn0G1naTVJ%2BRaKDU23CR8vxIJsRnXiOkqQNcl0w5oeZ%2FnCqZC8pu6nxE8lE%2F%2B%2BtfvzVkYk5Cmox92ZL3RzmgsUmBlo2BbXxrcWFJ6pWwp%2FvxY8m8TyJOwR85%2F73tOgwq4NlIvA91UdTwWdCWRRl2jNRVwzIOiWVwhLa4m7snfHrbfJxJggpxA0CewMMIovkNaPcGa0bNepSvICRlMBpqK1y%2FHOva5FWrdgBu%2B%2FZ4nG3vRyGhR6Q9MngRRSKZ1VzrDqLjzllbsLkr3dh63WZlDajMkg2qzOGC1%2FjpYqaiiriAaylo9Hf5cXk0LrkNRMDZg37NpPbASjRhnY5x8bkvfb9kMQg7uOQd1MJI7QhMSl70XgIs%2FvlHDbAFZDh8FV9cbSh8poxHJE%2BKKHr7bLn0GBXOpDC5TI9tpdl%2BytStoYup0R8nMU6krc5SlKlWE6UbfUeooO1yMb0xeAsZrBBfC4q1R4qWKthznS66BQBLjShdmaZ7INEbApQeAH%2BG5KEkX64MojB7cJnTYHNTMJnN14RcSFL4yv0R3nJo1Kac6ffeYA78VZEeuG4yk7ml%2ByR0JFbRAyDJBkIwuNHwvAY6pgHDWXhoQ4PsUKhNhwUxvGnXJUkjnUGlWVSZOas%2FZR89e3xODx5JG%2FrIXXmLP%2B8dZvCC2pgsL33zZxxu%2F7t77JydEc%2FTtuZeICFkJRMXgevOzqZ4YxdT4DGRK7IDTUFxl9461UFeTleb3QN12dvoQ5zSFhNKABu94BUShUFxcJcHVmmi%2FSeyjVRQRhxcByNjW0RSfDMf91STgz8ge%2BJJ8LgEFZXSFY8f&X-Amz-Signature=e6250c26185573ea2965ea330f204331b084800cd1529dcf0da89c766afa5ee8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPR5NUXA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgcdqg3Wo0QV25wTLQy0p30r5ql2vBqUOi7S883VsT0QIhAJSxp4eZgagGt7SEjHrrSKEZHvU8CfYoL5MIYNlTIlHuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbR%2BrUs4ME9F18dhMq3AOwjAajgySwTL1QhJIzYHeIJspfRrH0ajZjNA7lKSuvg%2B7KWBDD3tgv4zRTYjOPU1QWMna437gDsHGF40THDxNV25tUw0ovC2FULUef2zAkqvH7cbWgTsoWut4wRam%2BPgJZawncswbjvL0hxK8b2N3QH4DnHDaWFHaK06QcUL0yHosC4ue0pUYDG4SCqnaMRx8kGvq7xcI7jwPHRJYwj6gmhlz4W0b8QQvm3JNXP%2F8ejLcd5JMWjC0kKyiMZdrDHS2OGeKfVsKMPLnwHLTd4Pi63M7QhlnD7gK5QL%2FZoRd%2By2Es0KVQ2GS58peUWSKRbKXQ7CEn2J%2B8JU%2BG0JPoHT%2FOUq%2Bvyym7S9abvGINYpzDKJvIdXQWFSGj%2F1RZxvrkl0ITgeuBiPR5D07yHmmjnvRrWELWz%2BbDHMjFlIA646oMg8xOcjCuNhimtKJz1PaGLOqWoGQ27sGWDGMqJnbQfu3DXlvQlf8UCamg2%2FjJj5TzeRfDM5WYZw7u%2BkiL2y6DGHuYE5BpLRpyqa7CGvKMjJpAPmVCxtO4Zg7FC6iw6u4amwo4sqOPJRH7hPGTgQ8NmkYWjWuBQMH5zVvfdSQuSPKguIq0EGJ8B%2FAPUeF27NsaSyrO5U2dKH3YYNaD6jDf0PC8BjqkAUACPGpJBrU2drFShAPBy%2F09REPi7hWJVFckSVC03MY6H8X%2FKnQjlI1JMPzJ7Xdi5991yNF9Gf54ocBSou20wJeg6rWctArls0VtmNj5XGLa%2F6WlrCouIHpxNfjjTkI%2FOdR2TPvfqukUrhS3d2XVsCPMU%2Fn7k4HsRofMlLp%2Bu0q5HPCl6GkxbjBPSZkBI5wSJkld%2FBA8kmt62wpvTKtyr1n9FTdO&X-Amz-Signature=8f8454e95524cafdf0e66d6bc25e0a63aba09b7e9a519d7c44dd7edb2e02285e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPR5NUXA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T024127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgcdqg3Wo0QV25wTLQy0p30r5ql2vBqUOi7S883VsT0QIhAJSxp4eZgagGt7SEjHrrSKEZHvU8CfYoL5MIYNlTIlHuKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxbR%2BrUs4ME9F18dhMq3AOwjAajgySwTL1QhJIzYHeIJspfRrH0ajZjNA7lKSuvg%2B7KWBDD3tgv4zRTYjOPU1QWMna437gDsHGF40THDxNV25tUw0ovC2FULUef2zAkqvH7cbWgTsoWut4wRam%2BPgJZawncswbjvL0hxK8b2N3QH4DnHDaWFHaK06QcUL0yHosC4ue0pUYDG4SCqnaMRx8kGvq7xcI7jwPHRJYwj6gmhlz4W0b8QQvm3JNXP%2F8ejLcd5JMWjC0kKyiMZdrDHS2OGeKfVsKMPLnwHLTd4Pi63M7QhlnD7gK5QL%2FZoRd%2By2Es0KVQ2GS58peUWSKRbKXQ7CEn2J%2B8JU%2BG0JPoHT%2FOUq%2Bvyym7S9abvGINYpzDKJvIdXQWFSGj%2F1RZxvrkl0ITgeuBiPR5D07yHmmjnvRrWELWz%2BbDHMjFlIA646oMg8xOcjCuNhimtKJz1PaGLOqWoGQ27sGWDGMqJnbQfu3DXlvQlf8UCamg2%2FjJj5TzeRfDM5WYZw7u%2BkiL2y6DGHuYE5BpLRpyqa7CGvKMjJpAPmVCxtO4Zg7FC6iw6u4amwo4sqOPJRH7hPGTgQ8NmkYWjWuBQMH5zVvfdSQuSPKguIq0EGJ8B%2FAPUeF27NsaSyrO5U2dKH3YYNaD6jDf0PC8BjqkAUACPGpJBrU2drFShAPBy%2F09REPi7hWJVFckSVC03MY6H8X%2FKnQjlI1JMPzJ7Xdi5991yNF9Gf54ocBSou20wJeg6rWctArls0VtmNj5XGLa%2F6WlrCouIHpxNfjjTkI%2FOdR2TPvfqukUrhS3d2XVsCPMU%2Fn7k4HsRofMlLp%2Bu0q5HPCl6GkxbjBPSZkBI5wSJkld%2FBA8kmt62wpvTKtyr1n9FTdO&X-Amz-Signature=249a068934824c26af36a6ebb8f74af267633554e670d474053d72773797e78e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
