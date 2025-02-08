

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDODEPGV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDYZkaXPYLreYNzrL4k%2FeZDTtHRfrkoD%2BzDiBjQO8efdwIgcGxjD2d%2Ftg16tOZz6gOtvYLJuofeCGYZAApp5PZpaYcqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYC3ox6W90V3P02HyrcA9qXEkfR03l9j0d3pCg6Rs3R4eViNIUor15NWsqcJi6q45gawqT97PxCsbs72dDCz1xOU9DQ6F2t2lKrMAvfLXXffklAhR%2BI%2BeEC%2FdD1EL1HfmCTXG7rR0PsZDeIimbhkCXbihTOyMK3RsXo7oL0Zah0d5WhnUkEKTy1Xu49WSFouHg8Tn9wYCqX0Zam65vDb6YoZTVMKB9OD18K6lpVh4qx1KbDWUjxHr2p3iwPWt%2FdfwLbkljujU4isNT2oHWOnqPDa8PEl2smDb9gR1WbAhzVvlFo0IKaMdEd3Q2zjfYvv7v09ERvVmejebFBMCdyk8hW8wdGx%2F9UuN5GQQfz6cwq9P7Zlj14VV9TqjUz5W%2Fl8goWUQqj38ijC4JSO8zrFF4mZkFeq1m%2FrKE7m9265jJwScwqwLAdjrCiJK8JErCJ25HaUmyYbzggCp1hdik7xzsdALC7zu%2B0vkPZZJodI5vLtAvOAjKgIAsT57i1tZgr0t%2B9NwRl6U1krODx43Il7HctlI45Ydgw3MiH7kQuVX%2BkCIhxeuHRAGpysh7BdQnzy2yq0VMMz5n4vJ6GnW4aIFYGXbcH%2B4YSUyo0N9xEu00ewsSaLUhaD0y%2BUAce0eku30caTFP%2Bd9uHXvZSMNKOnL0GOqUB6ezi7Km2QseHGA9ujbjSsIdd5LJmtJI2mL%2FPALqZawMtlec9nDtmFO9MU%2BnM%2FMzIn3mYz7xXXIVyFA687qOO05XSzZQGFa%2FKznpuf7jlgE%2Bc973XSdrlT3kbNJtzZBqRhyynUTshxGvoVCcDHFEIFCDuklo%2FV1crjaKMdEbDUf0Cp89kzrAMiZG7tb37zh0oe8FCUOECWEB9AQ0eD4NTYA%2FSWNIU&X-Amz-Signature=3cc923986f74d3bde6d3309fe0fb28169c6eb9c25943a9d885ecbb4003be4638&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDODEPGV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDYZkaXPYLreYNzrL4k%2FeZDTtHRfrkoD%2BzDiBjQO8efdwIgcGxjD2d%2Ftg16tOZz6gOtvYLJuofeCGYZAApp5PZpaYcqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYC3ox6W90V3P02HyrcA9qXEkfR03l9j0d3pCg6Rs3R4eViNIUor15NWsqcJi6q45gawqT97PxCsbs72dDCz1xOU9DQ6F2t2lKrMAvfLXXffklAhR%2BI%2BeEC%2FdD1EL1HfmCTXG7rR0PsZDeIimbhkCXbihTOyMK3RsXo7oL0Zah0d5WhnUkEKTy1Xu49WSFouHg8Tn9wYCqX0Zam65vDb6YoZTVMKB9OD18K6lpVh4qx1KbDWUjxHr2p3iwPWt%2FdfwLbkljujU4isNT2oHWOnqPDa8PEl2smDb9gR1WbAhzVvlFo0IKaMdEd3Q2zjfYvv7v09ERvVmejebFBMCdyk8hW8wdGx%2F9UuN5GQQfz6cwq9P7Zlj14VV9TqjUz5W%2Fl8goWUQqj38ijC4JSO8zrFF4mZkFeq1m%2FrKE7m9265jJwScwqwLAdjrCiJK8JErCJ25HaUmyYbzggCp1hdik7xzsdALC7zu%2B0vkPZZJodI5vLtAvOAjKgIAsT57i1tZgr0t%2B9NwRl6U1krODx43Il7HctlI45Ydgw3MiH7kQuVX%2BkCIhxeuHRAGpysh7BdQnzy2yq0VMMz5n4vJ6GnW4aIFYGXbcH%2B4YSUyo0N9xEu00ewsSaLUhaD0y%2BUAce0eku30caTFP%2Bd9uHXvZSMNKOnL0GOqUB6ezi7Km2QseHGA9ujbjSsIdd5LJmtJI2mL%2FPALqZawMtlec9nDtmFO9MU%2BnM%2FMzIn3mYz7xXXIVyFA687qOO05XSzZQGFa%2FKznpuf7jlgE%2Bc973XSdrlT3kbNJtzZBqRhyynUTshxGvoVCcDHFEIFCDuklo%2FV1crjaKMdEbDUf0Cp89kzrAMiZG7tb37zh0oe8FCUOECWEB9AQ0eD4NTYA%2FSWNIU&X-Amz-Signature=d06b8a9e44cac28d686f38afeceee0f6a3dfd8171f645195f417217e6042df9d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDODEPGV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDYZkaXPYLreYNzrL4k%2FeZDTtHRfrkoD%2BzDiBjQO8efdwIgcGxjD2d%2Ftg16tOZz6gOtvYLJuofeCGYZAApp5PZpaYcqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYC3ox6W90V3P02HyrcA9qXEkfR03l9j0d3pCg6Rs3R4eViNIUor15NWsqcJi6q45gawqT97PxCsbs72dDCz1xOU9DQ6F2t2lKrMAvfLXXffklAhR%2BI%2BeEC%2FdD1EL1HfmCTXG7rR0PsZDeIimbhkCXbihTOyMK3RsXo7oL0Zah0d5WhnUkEKTy1Xu49WSFouHg8Tn9wYCqX0Zam65vDb6YoZTVMKB9OD18K6lpVh4qx1KbDWUjxHr2p3iwPWt%2FdfwLbkljujU4isNT2oHWOnqPDa8PEl2smDb9gR1WbAhzVvlFo0IKaMdEd3Q2zjfYvv7v09ERvVmejebFBMCdyk8hW8wdGx%2F9UuN5GQQfz6cwq9P7Zlj14VV9TqjUz5W%2Fl8goWUQqj38ijC4JSO8zrFF4mZkFeq1m%2FrKE7m9265jJwScwqwLAdjrCiJK8JErCJ25HaUmyYbzggCp1hdik7xzsdALC7zu%2B0vkPZZJodI5vLtAvOAjKgIAsT57i1tZgr0t%2B9NwRl6U1krODx43Il7HctlI45Ydgw3MiH7kQuVX%2BkCIhxeuHRAGpysh7BdQnzy2yq0VMMz5n4vJ6GnW4aIFYGXbcH%2B4YSUyo0N9xEu00ewsSaLUhaD0y%2BUAce0eku30caTFP%2Bd9uHXvZSMNKOnL0GOqUB6ezi7Km2QseHGA9ujbjSsIdd5LJmtJI2mL%2FPALqZawMtlec9nDtmFO9MU%2BnM%2FMzIn3mYz7xXXIVyFA687qOO05XSzZQGFa%2FKznpuf7jlgE%2Bc973XSdrlT3kbNJtzZBqRhyynUTshxGvoVCcDHFEIFCDuklo%2FV1crjaKMdEbDUf0Cp89kzrAMiZG7tb37zh0oe8FCUOECWEB9AQ0eD4NTYA%2FSWNIU&X-Amz-Signature=ba1ab2c02651d4ebb327b523d863f726f84a18cd773d9b9f1cd7190b41c08008&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDODEPGV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDYZkaXPYLreYNzrL4k%2FeZDTtHRfrkoD%2BzDiBjQO8efdwIgcGxjD2d%2Ftg16tOZz6gOtvYLJuofeCGYZAApp5PZpaYcqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYC3ox6W90V3P02HyrcA9qXEkfR03l9j0d3pCg6Rs3R4eViNIUor15NWsqcJi6q45gawqT97PxCsbs72dDCz1xOU9DQ6F2t2lKrMAvfLXXffklAhR%2BI%2BeEC%2FdD1EL1HfmCTXG7rR0PsZDeIimbhkCXbihTOyMK3RsXo7oL0Zah0d5WhnUkEKTy1Xu49WSFouHg8Tn9wYCqX0Zam65vDb6YoZTVMKB9OD18K6lpVh4qx1KbDWUjxHr2p3iwPWt%2FdfwLbkljujU4isNT2oHWOnqPDa8PEl2smDb9gR1WbAhzVvlFo0IKaMdEd3Q2zjfYvv7v09ERvVmejebFBMCdyk8hW8wdGx%2F9UuN5GQQfz6cwq9P7Zlj14VV9TqjUz5W%2Fl8goWUQqj38ijC4JSO8zrFF4mZkFeq1m%2FrKE7m9265jJwScwqwLAdjrCiJK8JErCJ25HaUmyYbzggCp1hdik7xzsdALC7zu%2B0vkPZZJodI5vLtAvOAjKgIAsT57i1tZgr0t%2B9NwRl6U1krODx43Il7HctlI45Ydgw3MiH7kQuVX%2BkCIhxeuHRAGpysh7BdQnzy2yq0VMMz5n4vJ6GnW4aIFYGXbcH%2B4YSUyo0N9xEu00ewsSaLUhaD0y%2BUAce0eku30caTFP%2Bd9uHXvZSMNKOnL0GOqUB6ezi7Km2QseHGA9ujbjSsIdd5LJmtJI2mL%2FPALqZawMtlec9nDtmFO9MU%2BnM%2FMzIn3mYz7xXXIVyFA687qOO05XSzZQGFa%2FKznpuf7jlgE%2Bc973XSdrlT3kbNJtzZBqRhyynUTshxGvoVCcDHFEIFCDuklo%2FV1crjaKMdEbDUf0Cp89kzrAMiZG7tb37zh0oe8FCUOECWEB9AQ0eD4NTYA%2FSWNIU&X-Amz-Signature=ccaeabd72d7a17a8c29691532d5e0db9b218aedbaf8509ff4b49f02c8ebef6ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDODEPGV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDYZkaXPYLreYNzrL4k%2FeZDTtHRfrkoD%2BzDiBjQO8efdwIgcGxjD2d%2Ftg16tOZz6gOtvYLJuofeCGYZAApp5PZpaYcqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYC3ox6W90V3P02HyrcA9qXEkfR03l9j0d3pCg6Rs3R4eViNIUor15NWsqcJi6q45gawqT97PxCsbs72dDCz1xOU9DQ6F2t2lKrMAvfLXXffklAhR%2BI%2BeEC%2FdD1EL1HfmCTXG7rR0PsZDeIimbhkCXbihTOyMK3RsXo7oL0Zah0d5WhnUkEKTy1Xu49WSFouHg8Tn9wYCqX0Zam65vDb6YoZTVMKB9OD18K6lpVh4qx1KbDWUjxHr2p3iwPWt%2FdfwLbkljujU4isNT2oHWOnqPDa8PEl2smDb9gR1WbAhzVvlFo0IKaMdEd3Q2zjfYvv7v09ERvVmejebFBMCdyk8hW8wdGx%2F9UuN5GQQfz6cwq9P7Zlj14VV9TqjUz5W%2Fl8goWUQqj38ijC4JSO8zrFF4mZkFeq1m%2FrKE7m9265jJwScwqwLAdjrCiJK8JErCJ25HaUmyYbzggCp1hdik7xzsdALC7zu%2B0vkPZZJodI5vLtAvOAjKgIAsT57i1tZgr0t%2B9NwRl6U1krODx43Il7HctlI45Ydgw3MiH7kQuVX%2BkCIhxeuHRAGpysh7BdQnzy2yq0VMMz5n4vJ6GnW4aIFYGXbcH%2B4YSUyo0N9xEu00ewsSaLUhaD0y%2BUAce0eku30caTFP%2Bd9uHXvZSMNKOnL0GOqUB6ezi7Km2QseHGA9ujbjSsIdd5LJmtJI2mL%2FPALqZawMtlec9nDtmFO9MU%2BnM%2FMzIn3mYz7xXXIVyFA687qOO05XSzZQGFa%2FKznpuf7jlgE%2Bc973XSdrlT3kbNJtzZBqRhyynUTshxGvoVCcDHFEIFCDuklo%2FV1crjaKMdEbDUf0Cp89kzrAMiZG7tb37zh0oe8FCUOECWEB9AQ0eD4NTYA%2FSWNIU&X-Amz-Signature=5e3314018c9bb76591de83fbad46fc44f40279c17434febd3c2263fae3c0378e&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDODEPGV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDYZkaXPYLreYNzrL4k%2FeZDTtHRfrkoD%2BzDiBjQO8efdwIgcGxjD2d%2Ftg16tOZz6gOtvYLJuofeCGYZAApp5PZpaYcqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYC3ox6W90V3P02HyrcA9qXEkfR03l9j0d3pCg6Rs3R4eViNIUor15NWsqcJi6q45gawqT97PxCsbs72dDCz1xOU9DQ6F2t2lKrMAvfLXXffklAhR%2BI%2BeEC%2FdD1EL1HfmCTXG7rR0PsZDeIimbhkCXbihTOyMK3RsXo7oL0Zah0d5WhnUkEKTy1Xu49WSFouHg8Tn9wYCqX0Zam65vDb6YoZTVMKB9OD18K6lpVh4qx1KbDWUjxHr2p3iwPWt%2FdfwLbkljujU4isNT2oHWOnqPDa8PEl2smDb9gR1WbAhzVvlFo0IKaMdEd3Q2zjfYvv7v09ERvVmejebFBMCdyk8hW8wdGx%2F9UuN5GQQfz6cwq9P7Zlj14VV9TqjUz5W%2Fl8goWUQqj38ijC4JSO8zrFF4mZkFeq1m%2FrKE7m9265jJwScwqwLAdjrCiJK8JErCJ25HaUmyYbzggCp1hdik7xzsdALC7zu%2B0vkPZZJodI5vLtAvOAjKgIAsT57i1tZgr0t%2B9NwRl6U1krODx43Il7HctlI45Ydgw3MiH7kQuVX%2BkCIhxeuHRAGpysh7BdQnzy2yq0VMMz5n4vJ6GnW4aIFYGXbcH%2B4YSUyo0N9xEu00ewsSaLUhaD0y%2BUAce0eku30caTFP%2Bd9uHXvZSMNKOnL0GOqUB6ezi7Km2QseHGA9ujbjSsIdd5LJmtJI2mL%2FPALqZawMtlec9nDtmFO9MU%2BnM%2FMzIn3mYz7xXXIVyFA687qOO05XSzZQGFa%2FKznpuf7jlgE%2Bc973XSdrlT3kbNJtzZBqRhyynUTshxGvoVCcDHFEIFCDuklo%2FV1crjaKMdEbDUf0Cp89kzrAMiZG7tb37zh0oe8FCUOECWEB9AQ0eD4NTYA%2FSWNIU&X-Amz-Signature=bb916b2c667072179b9021b25b281e502c82cd94cdb3da1999e30f6d9219c2ba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDODEPGV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDYZkaXPYLreYNzrL4k%2FeZDTtHRfrkoD%2BzDiBjQO8efdwIgcGxjD2d%2Ftg16tOZz6gOtvYLJuofeCGYZAApp5PZpaYcqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYC3ox6W90V3P02HyrcA9qXEkfR03l9j0d3pCg6Rs3R4eViNIUor15NWsqcJi6q45gawqT97PxCsbs72dDCz1xOU9DQ6F2t2lKrMAvfLXXffklAhR%2BI%2BeEC%2FdD1EL1HfmCTXG7rR0PsZDeIimbhkCXbihTOyMK3RsXo7oL0Zah0d5WhnUkEKTy1Xu49WSFouHg8Tn9wYCqX0Zam65vDb6YoZTVMKB9OD18K6lpVh4qx1KbDWUjxHr2p3iwPWt%2FdfwLbkljujU4isNT2oHWOnqPDa8PEl2smDb9gR1WbAhzVvlFo0IKaMdEd3Q2zjfYvv7v09ERvVmejebFBMCdyk8hW8wdGx%2F9UuN5GQQfz6cwq9P7Zlj14VV9TqjUz5W%2Fl8goWUQqj38ijC4JSO8zrFF4mZkFeq1m%2FrKE7m9265jJwScwqwLAdjrCiJK8JErCJ25HaUmyYbzggCp1hdik7xzsdALC7zu%2B0vkPZZJodI5vLtAvOAjKgIAsT57i1tZgr0t%2B9NwRl6U1krODx43Il7HctlI45Ydgw3MiH7kQuVX%2BkCIhxeuHRAGpysh7BdQnzy2yq0VMMz5n4vJ6GnW4aIFYGXbcH%2B4YSUyo0N9xEu00ewsSaLUhaD0y%2BUAce0eku30caTFP%2Bd9uHXvZSMNKOnL0GOqUB6ezi7Km2QseHGA9ujbjSsIdd5LJmtJI2mL%2FPALqZawMtlec9nDtmFO9MU%2BnM%2FMzIn3mYz7xXXIVyFA687qOO05XSzZQGFa%2FKznpuf7jlgE%2Bc973XSdrlT3kbNJtzZBqRhyynUTshxGvoVCcDHFEIFCDuklo%2FV1crjaKMdEbDUf0Cp89kzrAMiZG7tb37zh0oe8FCUOECWEB9AQ0eD4NTYA%2FSWNIU&X-Amz-Signature=78ff2587ab8d01786428e5b9ddb008968e9249c16d08b62fd021bff46a4be4bd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDODEPGV%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDYZkaXPYLreYNzrL4k%2FeZDTtHRfrkoD%2BzDiBjQO8efdwIgcGxjD2d%2Ftg16tOZz6gOtvYLJuofeCGYZAApp5PZpaYcqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOYC3ox6W90V3P02HyrcA9qXEkfR03l9j0d3pCg6Rs3R4eViNIUor15NWsqcJi6q45gawqT97PxCsbs72dDCz1xOU9DQ6F2t2lKrMAvfLXXffklAhR%2BI%2BeEC%2FdD1EL1HfmCTXG7rR0PsZDeIimbhkCXbihTOyMK3RsXo7oL0Zah0d5WhnUkEKTy1Xu49WSFouHg8Tn9wYCqX0Zam65vDb6YoZTVMKB9OD18K6lpVh4qx1KbDWUjxHr2p3iwPWt%2FdfwLbkljujU4isNT2oHWOnqPDa8PEl2smDb9gR1WbAhzVvlFo0IKaMdEd3Q2zjfYvv7v09ERvVmejebFBMCdyk8hW8wdGx%2F9UuN5GQQfz6cwq9P7Zlj14VV9TqjUz5W%2Fl8goWUQqj38ijC4JSO8zrFF4mZkFeq1m%2FrKE7m9265jJwScwqwLAdjrCiJK8JErCJ25HaUmyYbzggCp1hdik7xzsdALC7zu%2B0vkPZZJodI5vLtAvOAjKgIAsT57i1tZgr0t%2B9NwRl6U1krODx43Il7HctlI45Ydgw3MiH7kQuVX%2BkCIhxeuHRAGpysh7BdQnzy2yq0VMMz5n4vJ6GnW4aIFYGXbcH%2B4YSUyo0N9xEu00ewsSaLUhaD0y%2BUAce0eku30caTFP%2Bd9uHXvZSMNKOnL0GOqUB6ezi7Km2QseHGA9ujbjSsIdd5LJmtJI2mL%2FPALqZawMtlec9nDtmFO9MU%2BnM%2FMzIn3mYz7xXXIVyFA687qOO05XSzZQGFa%2FKznpuf7jlgE%2Bc973XSdrlT3kbNJtzZBqRhyynUTshxGvoVCcDHFEIFCDuklo%2FV1crjaKMdEbDUf0Cp89kzrAMiZG7tb37zh0oe8FCUOECWEB9AQ0eD4NTYA%2FSWNIU&X-Amz-Signature=d03365dacafdf1cf5537a4fb5685276f76b343f41c8bb443717092df348cec64&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPKHHVI5%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIAOrpZRFhSAJdXkQHgjB51CyJIUVD6dqLJnWNdfqbsI7AiEApTWVXgADPh1O7r046kLOS%2FAQjrZcM9KiIP7kD%2BxlHGMqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKWPfBx1JbemdulPdCrcA6VdHt0V%2FPbjzr8VOpc2YLwM6IosLeGKANtWvzruqgvUY74%2BCo5omooGH51DV6IOXr8cDcJkPV92NCSW0K7YQWZRgAxQG2QDn0OWb2hW%2FDnFexS1NoHaR9KRaXfFQMiewTE%2F9yHDSF12jFfTy%2FQ6PjRyIm2dVH4jJixYYVwWOJn2JJOCv%2BqtHjWW7zSYz%2FcDBflybw7el4roz5ygi%2B42ot%2Bm4rBmU67njxlOxtfb7CLFsLOBydslz9I8T3od3uvblYrA0tiRopmuA%2BlSHdnWpv%2BNZhMqEbzAMGrjn7UX9Po7Wu0MnaaAynYeVY742ezEscX%2BvTDrbCLHk6Cm06RX%2Bt8SFz5jV6uqK56JHn0qOpiIy5ZFKjTohNK9zFCH4ojUdAIZzuyfIDEYx45F8IvP1jL%2FuN%2FQ2wXvj7%2FaHdMH8xqL5JiDFpe4K7s4SYkKQXCIze1zyBlO6PwCDMD%2BpTtRXkMJurEW1PEzc5OAW7g%2BZy7pbY3WIoM0jAMYcXZn0W0FWn1rKNsSmXTulSpVG7PSBy%2FSiE4NThp4WxDelnnBNsZSFC%2BPY3rzYQ2cNZ6H8ALSYMGFxD6me0ZGe3ujs6I1%2BCJOrgMBBha%2Fje8dhJSj4USlUFO23E%2BH4l69PxoAMOmOnL0GOqUBYow64No3WPGovtC2QLgM8EE7eRSMth%2FwCzYRi965pPTjE0HL9mrCrLH2SCakghpLOVlDGwobK6R95DzpJwzLbXQiOFbEKR4Ap5E%2F%2FJZjqPZsOwXvFDfHnJBf%2Bmxjq28z%2B%2F9V9PvW71Wp0OMDacnLqijWNj63oiSVrQafs1EuapvhVv0prh0FjQLkYs5P0BBB7qQGPwGqIgBPJQoxQgKlOjQsfXEX&X-Amz-Signature=ceab77fb793a3717128d212a609ffaceabb032d2771453a5ff4692d37c97f952&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466646B77RM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIHJCjwI4K16gIM0ZTds%2FF%2FSJdAdfMk7cLBDXkqgYlEF%2BAiEAjAPx%2FwDuqfHSkIGXa8fQYr67vzqJm4FA5GSfM%2BM2wtwqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDCU16Z%2F6Z%2FG%2F6WigCrcA%2FLG8%2B5E%2FT%2Fg7%2Fj5mjRajJWwnd%2BHuw3J%2BmYaSBVzXYI0HplIULA8FlpxcgFw2meytE4JDgwYuAKMH7lFs3wV5Z1uhi%2BsWpbU6vgOdvALhg8Fzi%2BbIu4f96d0XM7ljbEdqGY%2FWqtKYGVCstXHOoTEo5zN0ve9gFBTkCY4LgLIZy2I3bUJYXW0Je8Pmb63j8xgy7wOoTMz6YOTBUXzsk9VE95EhELaVkQ7k6vFX%2Fa9ZifTcJmy%2FqRKP%2FO6US4XbmddE5SS8ECNnZik%2BtqbGgH1Q5ihbxPW1SvQa%2F%2BJIpqiO618eivwuVCLTr3WQvbW%2FzBgOdOHAn1%2FsQ0s5T482uo4epmZiIaBDEgciClHFIYK2FGbWrvk6rIclIfHshpMjjrxmXCf4Y5Y7fJjkk3%2BfGLAIYW3PipBtxnKa%2F8Biosx4G7eun6KjeUnVF%2BYwpNSXfaFRVDeoNeZkLQGEUClnae0whYjpiYWxeS8RDofp7lJn1CZu5kaYOxOxfeyO0IDIfghMEd4rTlvEBc77hqDoSUb%2FvuHGZzFhuml8Cn0iQhHzykcZdFivaMjqRGhwJw7DWndyrvvXj2XSrayrE7%2FSodsWC3KtO6d0p2IgnvJgJwcf5W7MLA3UX%2FpmTcCBnIAMNuOnL0GOqUBbNAfy3C9kElWWRYl3q5B9Y48ZdYtQoVtmIW7YWiylnLXnfZoknJPBpkRSbQa6VaMnOn3rlF0Fc9Dk%2Bt9nsg90eOdJoxYmjajUqetYIVjbXn4F%2BraPQnktKmlWiE7UiSGe5628VmGpudS%2BdbgEQjzWV5DGiQefnmeG%2BRSIP4TKhKdZ3LvNVbMbl8KLhEPi5iuUF1h9KeMyWqnKfNE8JVkX8lKu3XS&X-Amz-Signature=22d45d310a96aa03c908a1ef8accad37b42057a5b6c3a98d07075c84f934722d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R23LQXES%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIES3HnbeNBN3frZBJpU9yJEDS46DmE94EgX75E77c4vxAiEA88SkUuV2VWa1uJKx2bPJuxiNwHU5SaAs5DjP2HFK88IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2B5jdtOpwJgeJCoBCrcA1M6gO%2B4bmEKh8vp6ReACY9tjgj1tKwJROnwg0P2JayQ%2FKnUpFg518sXC%2F1eeFWOiFLCOmqGDJCVVLmNz64ExrZDGrZ%2BVy%2BRfB31fwlmvF1%2FZ4AdeyMxgkCbSSng%2FTDSmoAjKg2ewquP%2BqEh%2FCwZsZXTJitrsfwrJh9eAL3z34XxcS5ivSQIH6%2F%2BS%2BHoUBOYUt84sO1oNZKIHgg%2BIdiozNVEUabSPznvjvgtRq%2BG9sG%2Bs%2Bxnbiy%2F9PBxH58Jcqzcqa%2FAfSbfOQAN1vH6SLfUqyWjzgXs2X1LiuMSaMCbcCcHNzwIU%2BkuExQDX0xk%2BE6V3QFHmeFFc8aOETXFBvvNfpAN5yc7Kc%2BmmZBNUb7m0PluaBYkX6MqgybrGMs%2BpM81DCwFswjIB1qMhijGP%2BjVld0FAyO%2F2qylesFvZSxl8F6zD7yYRdto53QFNt8EZXUT630tHa%2FwXSdGckU9yup3xbMrGkoCvLsgOU0hsbvDAMEbdFRUYeG87nQWZlmrzvM%2BcevWDZTPkRXP3%2F2zJmZu3aS7zOBF5i00Mjp2sG8LUVZs8Om2sqits2jplkAflOA7qI6cwZTDcNnAs6Cwe25bTnkLHmde3CoFseg4L1t%2FLIegrsmkBl9t598pj%2B%2BOMKOOnL0GOqUBFQMFnoi1KQuY8vtLn1v46WPUfxydh99NR%2FXjomaDiZby%2Bk7asTnU%2F9pe0%2FyvtusaBC0G%2FIFVzLTAJm2rH16yqzMZF4c7VT3UoFapokX4FGIIeh2euuMhrPbfxAWYoXnogQ7m%2FkS3B07IX8omtW4Aqi8vFQbj4HUh%2BucwqcCn86hRN1n1r%2Fj2XIdgiySf0XZgTWDNrW9lUkbvhO7bEZHdt8P3wq%2BO&X-Amz-Signature=35c79a6fd1970ec38534386b9165f6d374a76526746fc5cc02a0ec3ec1a73ec3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R23LQXES%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIES3HnbeNBN3frZBJpU9yJEDS46DmE94EgX75E77c4vxAiEA88SkUuV2VWa1uJKx2bPJuxiNwHU5SaAs5DjP2HFK88IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2B5jdtOpwJgeJCoBCrcA1M6gO%2B4bmEKh8vp6ReACY9tjgj1tKwJROnwg0P2JayQ%2FKnUpFg518sXC%2F1eeFWOiFLCOmqGDJCVVLmNz64ExrZDGrZ%2BVy%2BRfB31fwlmvF1%2FZ4AdeyMxgkCbSSng%2FTDSmoAjKg2ewquP%2BqEh%2FCwZsZXTJitrsfwrJh9eAL3z34XxcS5ivSQIH6%2F%2BS%2BHoUBOYUt84sO1oNZKIHgg%2BIdiozNVEUabSPznvjvgtRq%2BG9sG%2Bs%2Bxnbiy%2F9PBxH58Jcqzcqa%2FAfSbfOQAN1vH6SLfUqyWjzgXs2X1LiuMSaMCbcCcHNzwIU%2BkuExQDX0xk%2BE6V3QFHmeFFc8aOETXFBvvNfpAN5yc7Kc%2BmmZBNUb7m0PluaBYkX6MqgybrGMs%2BpM81DCwFswjIB1qMhijGP%2BjVld0FAyO%2F2qylesFvZSxl8F6zD7yYRdto53QFNt8EZXUT630tHa%2FwXSdGckU9yup3xbMrGkoCvLsgOU0hsbvDAMEbdFRUYeG87nQWZlmrzvM%2BcevWDZTPkRXP3%2F2zJmZu3aS7zOBF5i00Mjp2sG8LUVZs8Om2sqits2jplkAflOA7qI6cwZTDcNnAs6Cwe25bTnkLHmde3CoFseg4L1t%2FLIegrsmkBl9t598pj%2B%2BOMKOOnL0GOqUBFQMFnoi1KQuY8vtLn1v46WPUfxydh99NR%2FXjomaDiZby%2Bk7asTnU%2F9pe0%2FyvtusaBC0G%2FIFVzLTAJm2rH16yqzMZF4c7VT3UoFapokX4FGIIeh2euuMhrPbfxAWYoXnogQ7m%2FkS3B07IX8omtW4Aqi8vFQbj4HUh%2BucwqcCn86hRN1n1r%2Fj2XIdgiySf0XZgTWDNrW9lUkbvhO7bEZHdt8P3wq%2BO&X-Amz-Signature=f6ad9b684b90a1af9e4cfe7693a5e617aa7916536f38837eb511a3a7bc548467&X-Amz-SignedHeaders=host&x-id=GetObject)
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
