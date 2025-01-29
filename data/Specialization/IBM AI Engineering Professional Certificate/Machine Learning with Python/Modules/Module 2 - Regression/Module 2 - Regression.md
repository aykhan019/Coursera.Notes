

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E5ZPIJV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1QxGlKD2vRocABipmvJ2JDC0FelbnZlv8boQM0g%2FUiQIhAL2r0GCdxF0kFeSs6D2MC2SyeD4Ryd3LbA%2Bsr76HLtr7KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2BSm6%2BiFHA%2BgsV82wq3ANcgCqdzmlxpCT%2Byy3SUtT86XyvQdzzbpyt6wGlz2C%2BNQ9nSihZoLCpwNI7NrGTXdHYlMbqk2IFxQplKw9yRfO%2FENqqSRHsg8Fp2QT%2Fufk2jZqBS09f28Rt3lqYNSR7LabDZ4jsxvzkBHP3vtvxobDokpP%2FWK2sd9twMr11tia7KTLq%2F8GhzPU6EZpGah6YTSz4NL8s7X6b2J9A3hpeHjjs3DQ%2BvJiirexB2YWG72AontY%2BP6HIsDXJ1k7bW7D%2Bvib%2FPMCATSObBQ7gWZ3vdKD4bz0NdI3gGqWKwa3LAmxwVriTBFPMWyxhfCoHTQ1tYEydCaMLd8Zni%2FBByN5Rhxx2PtR1mAs%2BnCh2MKAPGnYMvY1mFvV%2FPiGr5QzciAWXww%2B9Tha5jY%2Frfud3Xb%2FNMf1wkypFuCsec58GIxJN0gaPaV4nlwVKmi1On2DxcAYF3BgTGHkciNIWd8JkNp9XmmxZpDYuCCEoUzafQ%2FBnPgLStWovqPG7m8YBjE4j5AXl2L8zV5VOzzbE8Ch4WzbIo%2BuONy1jxbhIStXeuAvEW51FIC9498q2ixqGN5tsrWLtrjBzo4aGT6DcKTK3eDFMH5nuI3qufyAYoUDo1wOyWsbuEW9V1QyBmASyMgA7bjCax%2Be8BjqkAdwua4yRXwgsykziHw%2F83D9bKkF9bwSNHnPxSEdzrakQRTnCvHytU9gNJV3Y0VRRPJbMBouRMHJYeakD%2FuTqNEzExCC9NLQEqLfC%2Bzolv9fR4LNsu3Yy1g8%2FZuqU6AkRmKeOyobNhlNTBbtID01KUB1YjZTdUSHKfX8Ey5Z%2FULXKYM5zvDmH%2FylWkoKDj2QH2KiTO%2F4%2FJEsrBKIvgvqoIXFjLRYF&X-Amz-Signature=b2128812ee0feb41b80e3d749db14400cbf959a5f6fd3fe90467bff2bf02f52f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E5ZPIJV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1QxGlKD2vRocABipmvJ2JDC0FelbnZlv8boQM0g%2FUiQIhAL2r0GCdxF0kFeSs6D2MC2SyeD4Ryd3LbA%2Bsr76HLtr7KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2BSm6%2BiFHA%2BgsV82wq3ANcgCqdzmlxpCT%2Byy3SUtT86XyvQdzzbpyt6wGlz2C%2BNQ9nSihZoLCpwNI7NrGTXdHYlMbqk2IFxQplKw9yRfO%2FENqqSRHsg8Fp2QT%2Fufk2jZqBS09f28Rt3lqYNSR7LabDZ4jsxvzkBHP3vtvxobDokpP%2FWK2sd9twMr11tia7KTLq%2F8GhzPU6EZpGah6YTSz4NL8s7X6b2J9A3hpeHjjs3DQ%2BvJiirexB2YWG72AontY%2BP6HIsDXJ1k7bW7D%2Bvib%2FPMCATSObBQ7gWZ3vdKD4bz0NdI3gGqWKwa3LAmxwVriTBFPMWyxhfCoHTQ1tYEydCaMLd8Zni%2FBByN5Rhxx2PtR1mAs%2BnCh2MKAPGnYMvY1mFvV%2FPiGr5QzciAWXww%2B9Tha5jY%2Frfud3Xb%2FNMf1wkypFuCsec58GIxJN0gaPaV4nlwVKmi1On2DxcAYF3BgTGHkciNIWd8JkNp9XmmxZpDYuCCEoUzafQ%2FBnPgLStWovqPG7m8YBjE4j5AXl2L8zV5VOzzbE8Ch4WzbIo%2BuONy1jxbhIStXeuAvEW51FIC9498q2ixqGN5tsrWLtrjBzo4aGT6DcKTK3eDFMH5nuI3qufyAYoUDo1wOyWsbuEW9V1QyBmASyMgA7bjCax%2Be8BjqkAdwua4yRXwgsykziHw%2F83D9bKkF9bwSNHnPxSEdzrakQRTnCvHytU9gNJV3Y0VRRPJbMBouRMHJYeakD%2FuTqNEzExCC9NLQEqLfC%2Bzolv9fR4LNsu3Yy1g8%2FZuqU6AkRmKeOyobNhlNTBbtID01KUB1YjZTdUSHKfX8Ey5Z%2FULXKYM5zvDmH%2FylWkoKDj2QH2KiTO%2F4%2FJEsrBKIvgvqoIXFjLRYF&X-Amz-Signature=dc5d5397921485742ddabd8861bfc1071b5f3488d5a1a81f385ea65eee40ec33&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E5ZPIJV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1QxGlKD2vRocABipmvJ2JDC0FelbnZlv8boQM0g%2FUiQIhAL2r0GCdxF0kFeSs6D2MC2SyeD4Ryd3LbA%2Bsr76HLtr7KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2BSm6%2BiFHA%2BgsV82wq3ANcgCqdzmlxpCT%2Byy3SUtT86XyvQdzzbpyt6wGlz2C%2BNQ9nSihZoLCpwNI7NrGTXdHYlMbqk2IFxQplKw9yRfO%2FENqqSRHsg8Fp2QT%2Fufk2jZqBS09f28Rt3lqYNSR7LabDZ4jsxvzkBHP3vtvxobDokpP%2FWK2sd9twMr11tia7KTLq%2F8GhzPU6EZpGah6YTSz4NL8s7X6b2J9A3hpeHjjs3DQ%2BvJiirexB2YWG72AontY%2BP6HIsDXJ1k7bW7D%2Bvib%2FPMCATSObBQ7gWZ3vdKD4bz0NdI3gGqWKwa3LAmxwVriTBFPMWyxhfCoHTQ1tYEydCaMLd8Zni%2FBByN5Rhxx2PtR1mAs%2BnCh2MKAPGnYMvY1mFvV%2FPiGr5QzciAWXww%2B9Tha5jY%2Frfud3Xb%2FNMf1wkypFuCsec58GIxJN0gaPaV4nlwVKmi1On2DxcAYF3BgTGHkciNIWd8JkNp9XmmxZpDYuCCEoUzafQ%2FBnPgLStWovqPG7m8YBjE4j5AXl2L8zV5VOzzbE8Ch4WzbIo%2BuONy1jxbhIStXeuAvEW51FIC9498q2ixqGN5tsrWLtrjBzo4aGT6DcKTK3eDFMH5nuI3qufyAYoUDo1wOyWsbuEW9V1QyBmASyMgA7bjCax%2Be8BjqkAdwua4yRXwgsykziHw%2F83D9bKkF9bwSNHnPxSEdzrakQRTnCvHytU9gNJV3Y0VRRPJbMBouRMHJYeakD%2FuTqNEzExCC9NLQEqLfC%2Bzolv9fR4LNsu3Yy1g8%2FZuqU6AkRmKeOyobNhlNTBbtID01KUB1YjZTdUSHKfX8Ey5Z%2FULXKYM5zvDmH%2FylWkoKDj2QH2KiTO%2F4%2FJEsrBKIvgvqoIXFjLRYF&X-Amz-Signature=1dfa8166824d02de4428c6363721e0aad516b6981f6123a965f8b5e49715b392&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E5ZPIJV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1QxGlKD2vRocABipmvJ2JDC0FelbnZlv8boQM0g%2FUiQIhAL2r0GCdxF0kFeSs6D2MC2SyeD4Ryd3LbA%2Bsr76HLtr7KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2BSm6%2BiFHA%2BgsV82wq3ANcgCqdzmlxpCT%2Byy3SUtT86XyvQdzzbpyt6wGlz2C%2BNQ9nSihZoLCpwNI7NrGTXdHYlMbqk2IFxQplKw9yRfO%2FENqqSRHsg8Fp2QT%2Fufk2jZqBS09f28Rt3lqYNSR7LabDZ4jsxvzkBHP3vtvxobDokpP%2FWK2sd9twMr11tia7KTLq%2F8GhzPU6EZpGah6YTSz4NL8s7X6b2J9A3hpeHjjs3DQ%2BvJiirexB2YWG72AontY%2BP6HIsDXJ1k7bW7D%2Bvib%2FPMCATSObBQ7gWZ3vdKD4bz0NdI3gGqWKwa3LAmxwVriTBFPMWyxhfCoHTQ1tYEydCaMLd8Zni%2FBByN5Rhxx2PtR1mAs%2BnCh2MKAPGnYMvY1mFvV%2FPiGr5QzciAWXww%2B9Tha5jY%2Frfud3Xb%2FNMf1wkypFuCsec58GIxJN0gaPaV4nlwVKmi1On2DxcAYF3BgTGHkciNIWd8JkNp9XmmxZpDYuCCEoUzafQ%2FBnPgLStWovqPG7m8YBjE4j5AXl2L8zV5VOzzbE8Ch4WzbIo%2BuONy1jxbhIStXeuAvEW51FIC9498q2ixqGN5tsrWLtrjBzo4aGT6DcKTK3eDFMH5nuI3qufyAYoUDo1wOyWsbuEW9V1QyBmASyMgA7bjCax%2Be8BjqkAdwua4yRXwgsykziHw%2F83D9bKkF9bwSNHnPxSEdzrakQRTnCvHytU9gNJV3Y0VRRPJbMBouRMHJYeakD%2FuTqNEzExCC9NLQEqLfC%2Bzolv9fR4LNsu3Yy1g8%2FZuqU6AkRmKeOyobNhlNTBbtID01KUB1YjZTdUSHKfX8Ey5Z%2FULXKYM5zvDmH%2FylWkoKDj2QH2KiTO%2F4%2FJEsrBKIvgvqoIXFjLRYF&X-Amz-Signature=2ab031af33f797a8bbd44111b9b943c0d5a0ffc651f8aec50c38312e5c703a3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E5ZPIJV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1QxGlKD2vRocABipmvJ2JDC0FelbnZlv8boQM0g%2FUiQIhAL2r0GCdxF0kFeSs6D2MC2SyeD4Ryd3LbA%2Bsr76HLtr7KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2BSm6%2BiFHA%2BgsV82wq3ANcgCqdzmlxpCT%2Byy3SUtT86XyvQdzzbpyt6wGlz2C%2BNQ9nSihZoLCpwNI7NrGTXdHYlMbqk2IFxQplKw9yRfO%2FENqqSRHsg8Fp2QT%2Fufk2jZqBS09f28Rt3lqYNSR7LabDZ4jsxvzkBHP3vtvxobDokpP%2FWK2sd9twMr11tia7KTLq%2F8GhzPU6EZpGah6YTSz4NL8s7X6b2J9A3hpeHjjs3DQ%2BvJiirexB2YWG72AontY%2BP6HIsDXJ1k7bW7D%2Bvib%2FPMCATSObBQ7gWZ3vdKD4bz0NdI3gGqWKwa3LAmxwVriTBFPMWyxhfCoHTQ1tYEydCaMLd8Zni%2FBByN5Rhxx2PtR1mAs%2BnCh2MKAPGnYMvY1mFvV%2FPiGr5QzciAWXww%2B9Tha5jY%2Frfud3Xb%2FNMf1wkypFuCsec58GIxJN0gaPaV4nlwVKmi1On2DxcAYF3BgTGHkciNIWd8JkNp9XmmxZpDYuCCEoUzafQ%2FBnPgLStWovqPG7m8YBjE4j5AXl2L8zV5VOzzbE8Ch4WzbIo%2BuONy1jxbhIStXeuAvEW51FIC9498q2ixqGN5tsrWLtrjBzo4aGT6DcKTK3eDFMH5nuI3qufyAYoUDo1wOyWsbuEW9V1QyBmASyMgA7bjCax%2Be8BjqkAdwua4yRXwgsykziHw%2F83D9bKkF9bwSNHnPxSEdzrakQRTnCvHytU9gNJV3Y0VRRPJbMBouRMHJYeakD%2FuTqNEzExCC9NLQEqLfC%2Bzolv9fR4LNsu3Yy1g8%2FZuqU6AkRmKeOyobNhlNTBbtID01KUB1YjZTdUSHKfX8Ey5Z%2FULXKYM5zvDmH%2FylWkoKDj2QH2KiTO%2F4%2FJEsrBKIvgvqoIXFjLRYF&X-Amz-Signature=53c51da650e30d1f5639667f384d1d76748605a373699040d3997733cb71e375&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E5ZPIJV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1QxGlKD2vRocABipmvJ2JDC0FelbnZlv8boQM0g%2FUiQIhAL2r0GCdxF0kFeSs6D2MC2SyeD4Ryd3LbA%2Bsr76HLtr7KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2BSm6%2BiFHA%2BgsV82wq3ANcgCqdzmlxpCT%2Byy3SUtT86XyvQdzzbpyt6wGlz2C%2BNQ9nSihZoLCpwNI7NrGTXdHYlMbqk2IFxQplKw9yRfO%2FENqqSRHsg8Fp2QT%2Fufk2jZqBS09f28Rt3lqYNSR7LabDZ4jsxvzkBHP3vtvxobDokpP%2FWK2sd9twMr11tia7KTLq%2F8GhzPU6EZpGah6YTSz4NL8s7X6b2J9A3hpeHjjs3DQ%2BvJiirexB2YWG72AontY%2BP6HIsDXJ1k7bW7D%2Bvib%2FPMCATSObBQ7gWZ3vdKD4bz0NdI3gGqWKwa3LAmxwVriTBFPMWyxhfCoHTQ1tYEydCaMLd8Zni%2FBByN5Rhxx2PtR1mAs%2BnCh2MKAPGnYMvY1mFvV%2FPiGr5QzciAWXww%2B9Tha5jY%2Frfud3Xb%2FNMf1wkypFuCsec58GIxJN0gaPaV4nlwVKmi1On2DxcAYF3BgTGHkciNIWd8JkNp9XmmxZpDYuCCEoUzafQ%2FBnPgLStWovqPG7m8YBjE4j5AXl2L8zV5VOzzbE8Ch4WzbIo%2BuONy1jxbhIStXeuAvEW51FIC9498q2ixqGN5tsrWLtrjBzo4aGT6DcKTK3eDFMH5nuI3qufyAYoUDo1wOyWsbuEW9V1QyBmASyMgA7bjCax%2Be8BjqkAdwua4yRXwgsykziHw%2F83D9bKkF9bwSNHnPxSEdzrakQRTnCvHytU9gNJV3Y0VRRPJbMBouRMHJYeakD%2FuTqNEzExCC9NLQEqLfC%2Bzolv9fR4LNsu3Yy1g8%2FZuqU6AkRmKeOyobNhlNTBbtID01KUB1YjZTdUSHKfX8Ey5Z%2FULXKYM5zvDmH%2FylWkoKDj2QH2KiTO%2F4%2FJEsrBKIvgvqoIXFjLRYF&X-Amz-Signature=4ca587fcf6a7caaf8115151f555c8f12eac1a3731e549a6a9e656e83b86af162&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E5ZPIJV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1QxGlKD2vRocABipmvJ2JDC0FelbnZlv8boQM0g%2FUiQIhAL2r0GCdxF0kFeSs6D2MC2SyeD4Ryd3LbA%2Bsr76HLtr7KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2BSm6%2BiFHA%2BgsV82wq3ANcgCqdzmlxpCT%2Byy3SUtT86XyvQdzzbpyt6wGlz2C%2BNQ9nSihZoLCpwNI7NrGTXdHYlMbqk2IFxQplKw9yRfO%2FENqqSRHsg8Fp2QT%2Fufk2jZqBS09f28Rt3lqYNSR7LabDZ4jsxvzkBHP3vtvxobDokpP%2FWK2sd9twMr11tia7KTLq%2F8GhzPU6EZpGah6YTSz4NL8s7X6b2J9A3hpeHjjs3DQ%2BvJiirexB2YWG72AontY%2BP6HIsDXJ1k7bW7D%2Bvib%2FPMCATSObBQ7gWZ3vdKD4bz0NdI3gGqWKwa3LAmxwVriTBFPMWyxhfCoHTQ1tYEydCaMLd8Zni%2FBByN5Rhxx2PtR1mAs%2BnCh2MKAPGnYMvY1mFvV%2FPiGr5QzciAWXww%2B9Tha5jY%2Frfud3Xb%2FNMf1wkypFuCsec58GIxJN0gaPaV4nlwVKmi1On2DxcAYF3BgTGHkciNIWd8JkNp9XmmxZpDYuCCEoUzafQ%2FBnPgLStWovqPG7m8YBjE4j5AXl2L8zV5VOzzbE8Ch4WzbIo%2BuONy1jxbhIStXeuAvEW51FIC9498q2ixqGN5tsrWLtrjBzo4aGT6DcKTK3eDFMH5nuI3qufyAYoUDo1wOyWsbuEW9V1QyBmASyMgA7bjCax%2Be8BjqkAdwua4yRXwgsykziHw%2F83D9bKkF9bwSNHnPxSEdzrakQRTnCvHytU9gNJV3Y0VRRPJbMBouRMHJYeakD%2FuTqNEzExCC9NLQEqLfC%2Bzolv9fR4LNsu3Yy1g8%2FZuqU6AkRmKeOyobNhlNTBbtID01KUB1YjZTdUSHKfX8Ey5Z%2FULXKYM5zvDmH%2FylWkoKDj2QH2KiTO%2F4%2FJEsrBKIvgvqoIXFjLRYF&X-Amz-Signature=e896bd1d33b79811a85af0cff02982a85a969f9d1d044e288ced9dbaced789d4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667E5ZPIJV%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1QxGlKD2vRocABipmvJ2JDC0FelbnZlv8boQM0g%2FUiQIhAL2r0GCdxF0kFeSs6D2MC2SyeD4Ryd3LbA%2Bsr76HLtr7KogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2BSm6%2BiFHA%2BgsV82wq3ANcgCqdzmlxpCT%2Byy3SUtT86XyvQdzzbpyt6wGlz2C%2BNQ9nSihZoLCpwNI7NrGTXdHYlMbqk2IFxQplKw9yRfO%2FENqqSRHsg8Fp2QT%2Fufk2jZqBS09f28Rt3lqYNSR7LabDZ4jsxvzkBHP3vtvxobDokpP%2FWK2sd9twMr11tia7KTLq%2F8GhzPU6EZpGah6YTSz4NL8s7X6b2J9A3hpeHjjs3DQ%2BvJiirexB2YWG72AontY%2BP6HIsDXJ1k7bW7D%2Bvib%2FPMCATSObBQ7gWZ3vdKD4bz0NdI3gGqWKwa3LAmxwVriTBFPMWyxhfCoHTQ1tYEydCaMLd8Zni%2FBByN5Rhxx2PtR1mAs%2BnCh2MKAPGnYMvY1mFvV%2FPiGr5QzciAWXww%2B9Tha5jY%2Frfud3Xb%2FNMf1wkypFuCsec58GIxJN0gaPaV4nlwVKmi1On2DxcAYF3BgTGHkciNIWd8JkNp9XmmxZpDYuCCEoUzafQ%2FBnPgLStWovqPG7m8YBjE4j5AXl2L8zV5VOzzbE8Ch4WzbIo%2BuONy1jxbhIStXeuAvEW51FIC9498q2ixqGN5tsrWLtrjBzo4aGT6DcKTK3eDFMH5nuI3qufyAYoUDo1wOyWsbuEW9V1QyBmASyMgA7bjCax%2Be8BjqkAdwua4yRXwgsykziHw%2F83D9bKkF9bwSNHnPxSEdzrakQRTnCvHytU9gNJV3Y0VRRPJbMBouRMHJYeakD%2FuTqNEzExCC9NLQEqLfC%2Bzolv9fR4LNsu3Yy1g8%2FZuqU6AkRmKeOyobNhlNTBbtID01KUB1YjZTdUSHKfX8Ey5Z%2FULXKYM5zvDmH%2FylWkoKDj2QH2KiTO%2F4%2FJEsrBKIvgvqoIXFjLRYF&X-Amz-Signature=c2dd8cc783fb2bbaaaea3a23889b55aaa8ee33e2e60bafce8a29a26f67bfd4ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5MXBJK2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZLxSskl%2BDo1JUFlIFAW2j6w%2FXkXpqInf3q%2F4Nem4fTwIgXLTzIVSsk6BueeMsCfcC8i5jHG%2FKRnGn%2Bf9KZ1AlligqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP6CAoMowsLz1H7RwCrcA7o3VygvAjgojB8GDExoU%2Bkzb2GY6IfLKgXb6SSHws1jUZ2uLt8ld5qiRxCGMNFbh3eUbBVRpp9q2lA0MiFP%2Fp4zB0tUrHeKtxe4nk5%2BDWLeFbRnzQ9dfL4CS6tUZni5iKB64E3zxuYOB4bm8LFLHmfebML2H9cmc7RNeHFO4NSB0IL07zMBbkn7khPVFuXqg%2FE4Bsk2Y%2Fj72H7yf0bxW9WdUCMJ4%2FGVuWTiD2gqNXdgNGWz7XbFLBUuM5njXJW%2FLWGv174zejG4vrF0mQAFQqT1gDIZIAHlaZ%2BtDoKbeCoy6FU%2FDJprah1tt3d5%2FoAl6x%2FGuESSi%2Bl3IGDuBlj%2BCu69WT95nvuLXSqFFuPs2Gv%2FBPr0XSsQrQk6r1oswYkTlM67gpH8GGfV%2B5G%2BZZJfQ%2FuYhpyG14R5R5teP%2Bwr7i%2BCxdAxbO0RHDkoSQGLeK9ZDd%2FlOHedexMgM%2Bddfw2g11ixewZMnGaDa%2FxyjYh9C7HWZAfvSP%2F2TqtPlBb6qAd%2FBHggkTsnzrKPV1YSt7QUMjWn0gc0lfIeCuO17%2BuW6cr%2BM5MfO2ts8TVxB3cRHRkPhR8dhdTMhXV877KG1RYSMp6Ha%2Bqdo7rnGDmMVSUPZMAwQwPrX0binjTOdYEHML%2FH57wGOqUBiwZ2TkrToIfjNkH%2Fj%2F6jdS9GC24PHr62DnenbTZJ80tYKGuZ%2FsgCL7lu0C4gVbGAHX0g0Cu%2BNKHArRXR4gqZ7wR8VmH5n%2B29gg%2B0JjWn%2BhFk%2F6yqPI17NO3VPxBF2zd1ZV9XlAhC39gthKKzJg10oA4abhzYR9pGMwH6VdalXMOaVfGwS03ODFt%2Bs%2FljVrXBmGPQT53FWqglcNEl4k0CNf8eXvgC&X-Amz-Signature=7bc76fda2342f3e96b9cfe73bf07f8b35e65883c8bd67950499c447ba6b959a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBZ4TDRU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoUNAZw%2Ftcs28vfubfjUk1FN%2BiCbCzF2lnfcBqi4S4sAiAzYu3xGyiRyurJxgxlHSLnLC%2FAkvisXhMlhVnGHLbOtSqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMEjM%2BkFghvcx1EqLbKtwDZYaLdXZ68K7FPtX7D938NnZgYdlbighqgweni%2FxlderITLIYa0S%2BcgsgRElHVojNk9eZBLvoXZq95jlDY6CUc%2Fh99UvM0CHq84qROFxnmrYIQZlQsd0Tbl%2BtmQAqOnfSCdfVWy1AE%2BWA5sMcI1SHzXUez%2FQtnhfBxHVNlcgUvrvJ34Dq%2BAJso7VxylucBc48JUefmMEMUa7v%2FwHbbKfNsZ7Ss0B7BQFMqm0jv%2FZLTP5os8VCMlaGaABeuz4bgB8SFrqlWfR4nHppYrHiSfytwwolDMs%2B9mk0KFI7Ql9EBwLZedf2CIJTdbJeN89S9IFA%2FeUf4LppV8TJCL5WbzBzdfBedmjoJAf30yJVriPgcZzfZ9ayBnXiW2Eha8%2FVgYN2zK71GPQHqzniwfjdu4ZQHy09FoSgBniz6m%2F7DJWFVRZxQfPeaxT3JKDM7Wr142V6x65B4IrMGdJN9rzlq1eNWTuRNzfulq2wJPpIEMqTFnMDTOlhT%2B3RJNm9sB5My5jlHWf8Nu3KH3M5Ynzzexu5zYQCT%2BhO%2FFPULgeH3WHX7bwsmrHwWxvvGfDanJVBzHoeBdnCTiEP7Cy0gQM9pg7z8BlmegnzTW%2FJe2zzxiWlBbLUcFzgsslV4rK50EUw5KznvAY6pgHlvHJ7V%2FZGc2mib1kznMo%2BtmALN8ef67RUFZbGNOZaN0fzALV4iTRSRzXByplbNNMYRD5MxevrBEZtoNN9T%2BXwyppWBfskRhB4t0Md0EmTjAKOIKsTYR9iT7UubGu%2FYnIPjZBbJ1F0YLp5bhEwtJ1fydvAfnpeA6L9%2FPmsw74kF9XwooF8quXpnzaBbTFAVEzCdlm1Y6BPAY9wXG%2BBtY2oNnfqpIsg&X-Amz-Signature=dd935994fe86b37ce857e740e5eac47dae24317e86b28fea7fb37bf0a5925233&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDVDDTQK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFJ4ShElDI%2FlG77z4bCR7vV4kBPJlQ0d4SJqlcQAVbPhAiAzm0kRikEme216e3B3sR5dRrfsLss2pARaM5DMQ1bO0iqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME%2FcGpKe%2Bk7aRmKf2KtwDURIgfc7cvlcMKJlp8Zgd9Lq1j2mfTUW%2BkEhnr7pPuDavnAW3u5gSsgt4d%2FQUmrpFW3piX8arOxj7PoGReDEIbwmTr5oj%2BYuVQTECk4ildYXyFzVHlShP%2FsBR7%2B9vU%2FH%2B1GlHFYSimsU%2Bz8ZPv0cVX9jgmV%2BW0Q9jtaR8dnMTeC15vHD4mzn%2Bzgv0BuHkgWocQA6oTzfiD4jIfDCp9wWB%2BUkryYEL1PSiJuSNjzIQWaHeKFC4b4TO9iXbSZ6riWzm5TMuJA9gMKD9kwcOyDxu79iWyHF%2Bw8KSGBRbjeTtJ1yMZp6jPdmD9Ij8tDUXNWt9huLVAqqPRjjaKy50kn71ninZCzSkeV6XtFWFd9IiouT4T%2BV%2Fr62gDJW3XRHUF%2BkZE3tH7kjkWe2q3MGUFj3xFXn7pdOu%2FaA%2FZ9wgVi4ILsZwTjN2bVVrNwY2Pum8jb9aU9OQI9MFRDx%2FITp2z4waJ%2F%2F6yJsoWUfMnLqAYFv7MojqmtIVz7opOKoUukAsGqVV4XF%2BR9NgCdZLC3ZZ2l9zta5PypDdMc6s5LYGyICEmB7QTQIFTEgwYtixdUPRwG%2BMMEbkHc0OD7HbiYMPMyewVko8o68F%2B5Y0qwzMEKfXpbZbzClQShTJor9C%2Bo8w7MfnvAY6pgHWkZKOmQUizlBEsCzIlhuMKe9GpNCRH5uWVCOKEQfZfhqyxd0fr5t4xPouRCxCf3HSwxHLdFcRZAHIQy4crjWe%2BgADutgKl%2F5cjMNfOv4IX8ofOSAKDxSCkM0Biu%2B81IExtT4vaXXtVXj9Wrl%2FnXzE2D%2FnTiqpCCtMzlszcgoBqyi%2FaYbBkuKFYQ9V4KGhG6aM2Xu3bzaHiEVY3wbnoWKhljVJ0Ac5&X-Amz-Signature=7b1c6defd4d0c63c0b764de150995fa023076df5810a01b6041d8b0a69b6d138&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VDVDDTQK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T081902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFJ4ShElDI%2FlG77z4bCR7vV4kBPJlQ0d4SJqlcQAVbPhAiAzm0kRikEme216e3B3sR5dRrfsLss2pARaM5DMQ1bO0iqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIME%2FcGpKe%2Bk7aRmKf2KtwDURIgfc7cvlcMKJlp8Zgd9Lq1j2mfTUW%2BkEhnr7pPuDavnAW3u5gSsgt4d%2FQUmrpFW3piX8arOxj7PoGReDEIbwmTr5oj%2BYuVQTECk4ildYXyFzVHlShP%2FsBR7%2B9vU%2FH%2B1GlHFYSimsU%2Bz8ZPv0cVX9jgmV%2BW0Q9jtaR8dnMTeC15vHD4mzn%2Bzgv0BuHkgWocQA6oTzfiD4jIfDCp9wWB%2BUkryYEL1PSiJuSNjzIQWaHeKFC4b4TO9iXbSZ6riWzm5TMuJA9gMKD9kwcOyDxu79iWyHF%2Bw8KSGBRbjeTtJ1yMZp6jPdmD9Ij8tDUXNWt9huLVAqqPRjjaKy50kn71ninZCzSkeV6XtFWFd9IiouT4T%2BV%2Fr62gDJW3XRHUF%2BkZE3tH7kjkWe2q3MGUFj3xFXn7pdOu%2FaA%2FZ9wgVi4ILsZwTjN2bVVrNwY2Pum8jb9aU9OQI9MFRDx%2FITp2z4waJ%2F%2F6yJsoWUfMnLqAYFv7MojqmtIVz7opOKoUukAsGqVV4XF%2BR9NgCdZLC3ZZ2l9zta5PypDdMc6s5LYGyICEmB7QTQIFTEgwYtixdUPRwG%2BMMEbkHc0OD7HbiYMPMyewVko8o68F%2B5Y0qwzMEKfXpbZbzClQShTJor9C%2Bo8w7MfnvAY6pgHWkZKOmQUizlBEsCzIlhuMKe9GpNCRH5uWVCOKEQfZfhqyxd0fr5t4xPouRCxCf3HSwxHLdFcRZAHIQy4crjWe%2BgADutgKl%2F5cjMNfOv4IX8ofOSAKDxSCkM0Biu%2B81IExtT4vaXXtVXj9Wrl%2FnXzE2D%2FnTiqpCCtMzlszcgoBqyi%2FaYbBkuKFYQ9V4KGhG6aM2Xu3bzaHiEVY3wbnoWKhljVJ0Ac5&X-Amz-Signature=4828ccf587b0f8ac709391b5b0a66066676360a9a7609a5a06449fa3e62e967c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
