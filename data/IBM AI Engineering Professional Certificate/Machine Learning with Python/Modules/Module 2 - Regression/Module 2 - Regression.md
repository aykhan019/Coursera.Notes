

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAGM76C4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3IfVnO0%2BPozY%2FO%2FuFcfnplkkG2TjO%2Bb9rYRO1ESVYKgIhAOmSBHY0KH9uNHKKdqmPyW1yTQjah8HzwsGkRkH8l1dzKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs%2F7Ozr3%2BvKYk8GxYq3ANYABcFDZIJ0xKJLBBLiqwnPId1SZdyw0iEqTPAI5i8tlXbCC7%2BFr09QpPdnXI2EtwrEj704vhSDWtTDV%2FI3Q7Idvk78ubt%2FJvTFX1CKMljCa6pxwN4ALq0TqCaTC9ciAlnwhdN4N%2BmaJKdhrcugxfhiuPx2CRb%2BfJC%2FlRk7Z9okPj%2BAdIRyVWk1hcsQOyUnGIVXJGHAWIDIaS6TFnVtDWGPlAq4TQfBxSxA%2Fvt34zzoInikDa%2Fu3IXB49X9U%2B%2By9SESZypjLkTTUaqctj04cOVi%2BSgVoz5qrpTlGO0%2F0b%2BJ5FPVwCiFGpAbSgZuIbxZOXjdyPqe8vBamAT3zMMXh039dru5i5SgBiM%2Bl1WasBHJThxdTWYmXlalX%2FxeOYafYizpAS25Xs9Q5g57QoetoS7vJDqrh1kKN1LWTiK200snpTgqGTFtTZOpVCB9K%2FozA1QP%2F%2BikDBXyGrseTNxPOpUqkAzj1Q77FNhrkLqypYZjRAnzEzumEwnG%2FOhoP5tt51vaRVNB42ouWjF5EUiAPw8FGeCwTmKxSg9YwKdTntlQtzDvvbvLdQkfb1jK1dPiruajRVT0cAiGS40H04%2BHKb%2BDAenFnS%2BzFAI1KWAaX4hJ0lkBJ%2Fx9ovQVIHnsTCRzfW8BjqkAQucKfKwWwZ69qSUomp5b6PPguMOmUpciTDOpy5qFtpO4jlQNMEBFUqQgX6f5R8J%2FEJtDurQzdHPHaeqvfjZf7MvXVTmGvWVgPNcALdgUL5pcjCjYc2kxa2fBTNYJKp0fAOVGsDWgTkvwwOVgPAAXTueBdfwsTRXXyv7TlmfozstM6ytCCyno0%2BUCX3U3saW29lKOwhNOHetldegPDcf8NN1ruDK&X-Amz-Signature=ebab0a0a5db7c9ea132b750297e56ae1cf551d5e9723166eb6ad5582c60a2613&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAGM76C4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3IfVnO0%2BPozY%2FO%2FuFcfnplkkG2TjO%2Bb9rYRO1ESVYKgIhAOmSBHY0KH9uNHKKdqmPyW1yTQjah8HzwsGkRkH8l1dzKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs%2F7Ozr3%2BvKYk8GxYq3ANYABcFDZIJ0xKJLBBLiqwnPId1SZdyw0iEqTPAI5i8tlXbCC7%2BFr09QpPdnXI2EtwrEj704vhSDWtTDV%2FI3Q7Idvk78ubt%2FJvTFX1CKMljCa6pxwN4ALq0TqCaTC9ciAlnwhdN4N%2BmaJKdhrcugxfhiuPx2CRb%2BfJC%2FlRk7Z9okPj%2BAdIRyVWk1hcsQOyUnGIVXJGHAWIDIaS6TFnVtDWGPlAq4TQfBxSxA%2Fvt34zzoInikDa%2Fu3IXB49X9U%2B%2By9SESZypjLkTTUaqctj04cOVi%2BSgVoz5qrpTlGO0%2F0b%2BJ5FPVwCiFGpAbSgZuIbxZOXjdyPqe8vBamAT3zMMXh039dru5i5SgBiM%2Bl1WasBHJThxdTWYmXlalX%2FxeOYafYizpAS25Xs9Q5g57QoetoS7vJDqrh1kKN1LWTiK200snpTgqGTFtTZOpVCB9K%2FozA1QP%2F%2BikDBXyGrseTNxPOpUqkAzj1Q77FNhrkLqypYZjRAnzEzumEwnG%2FOhoP5tt51vaRVNB42ouWjF5EUiAPw8FGeCwTmKxSg9YwKdTntlQtzDvvbvLdQkfb1jK1dPiruajRVT0cAiGS40H04%2BHKb%2BDAenFnS%2BzFAI1KWAaX4hJ0lkBJ%2Fx9ovQVIHnsTCRzfW8BjqkAQucKfKwWwZ69qSUomp5b6PPguMOmUpciTDOpy5qFtpO4jlQNMEBFUqQgX6f5R8J%2FEJtDurQzdHPHaeqvfjZf7MvXVTmGvWVgPNcALdgUL5pcjCjYc2kxa2fBTNYJKp0fAOVGsDWgTkvwwOVgPAAXTueBdfwsTRXXyv7TlmfozstM6ytCCyno0%2BUCX3U3saW29lKOwhNOHetldegPDcf8NN1ruDK&X-Amz-Signature=b165ea487c5e110885177e299a43662c59d2a81c58da4c5f729c73a56d32e981&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAGM76C4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3IfVnO0%2BPozY%2FO%2FuFcfnplkkG2TjO%2Bb9rYRO1ESVYKgIhAOmSBHY0KH9uNHKKdqmPyW1yTQjah8HzwsGkRkH8l1dzKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs%2F7Ozr3%2BvKYk8GxYq3ANYABcFDZIJ0xKJLBBLiqwnPId1SZdyw0iEqTPAI5i8tlXbCC7%2BFr09QpPdnXI2EtwrEj704vhSDWtTDV%2FI3Q7Idvk78ubt%2FJvTFX1CKMljCa6pxwN4ALq0TqCaTC9ciAlnwhdN4N%2BmaJKdhrcugxfhiuPx2CRb%2BfJC%2FlRk7Z9okPj%2BAdIRyVWk1hcsQOyUnGIVXJGHAWIDIaS6TFnVtDWGPlAq4TQfBxSxA%2Fvt34zzoInikDa%2Fu3IXB49X9U%2B%2By9SESZypjLkTTUaqctj04cOVi%2BSgVoz5qrpTlGO0%2F0b%2BJ5FPVwCiFGpAbSgZuIbxZOXjdyPqe8vBamAT3zMMXh039dru5i5SgBiM%2Bl1WasBHJThxdTWYmXlalX%2FxeOYafYizpAS25Xs9Q5g57QoetoS7vJDqrh1kKN1LWTiK200snpTgqGTFtTZOpVCB9K%2FozA1QP%2F%2BikDBXyGrseTNxPOpUqkAzj1Q77FNhrkLqypYZjRAnzEzumEwnG%2FOhoP5tt51vaRVNB42ouWjF5EUiAPw8FGeCwTmKxSg9YwKdTntlQtzDvvbvLdQkfb1jK1dPiruajRVT0cAiGS40H04%2BHKb%2BDAenFnS%2BzFAI1KWAaX4hJ0lkBJ%2Fx9ovQVIHnsTCRzfW8BjqkAQucKfKwWwZ69qSUomp5b6PPguMOmUpciTDOpy5qFtpO4jlQNMEBFUqQgX6f5R8J%2FEJtDurQzdHPHaeqvfjZf7MvXVTmGvWVgPNcALdgUL5pcjCjYc2kxa2fBTNYJKp0fAOVGsDWgTkvwwOVgPAAXTueBdfwsTRXXyv7TlmfozstM6ytCCyno0%2BUCX3U3saW29lKOwhNOHetldegPDcf8NN1ruDK&X-Amz-Signature=ed67925fe7b8497741e6c4d8315ece6b587b238120654c07e615c4f93a9db249&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAGM76C4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3IfVnO0%2BPozY%2FO%2FuFcfnplkkG2TjO%2Bb9rYRO1ESVYKgIhAOmSBHY0KH9uNHKKdqmPyW1yTQjah8HzwsGkRkH8l1dzKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs%2F7Ozr3%2BvKYk8GxYq3ANYABcFDZIJ0xKJLBBLiqwnPId1SZdyw0iEqTPAI5i8tlXbCC7%2BFr09QpPdnXI2EtwrEj704vhSDWtTDV%2FI3Q7Idvk78ubt%2FJvTFX1CKMljCa6pxwN4ALq0TqCaTC9ciAlnwhdN4N%2BmaJKdhrcugxfhiuPx2CRb%2BfJC%2FlRk7Z9okPj%2BAdIRyVWk1hcsQOyUnGIVXJGHAWIDIaS6TFnVtDWGPlAq4TQfBxSxA%2Fvt34zzoInikDa%2Fu3IXB49X9U%2B%2By9SESZypjLkTTUaqctj04cOVi%2BSgVoz5qrpTlGO0%2F0b%2BJ5FPVwCiFGpAbSgZuIbxZOXjdyPqe8vBamAT3zMMXh039dru5i5SgBiM%2Bl1WasBHJThxdTWYmXlalX%2FxeOYafYizpAS25Xs9Q5g57QoetoS7vJDqrh1kKN1LWTiK200snpTgqGTFtTZOpVCB9K%2FozA1QP%2F%2BikDBXyGrseTNxPOpUqkAzj1Q77FNhrkLqypYZjRAnzEzumEwnG%2FOhoP5tt51vaRVNB42ouWjF5EUiAPw8FGeCwTmKxSg9YwKdTntlQtzDvvbvLdQkfb1jK1dPiruajRVT0cAiGS40H04%2BHKb%2BDAenFnS%2BzFAI1KWAaX4hJ0lkBJ%2Fx9ovQVIHnsTCRzfW8BjqkAQucKfKwWwZ69qSUomp5b6PPguMOmUpciTDOpy5qFtpO4jlQNMEBFUqQgX6f5R8J%2FEJtDurQzdHPHaeqvfjZf7MvXVTmGvWVgPNcALdgUL5pcjCjYc2kxa2fBTNYJKp0fAOVGsDWgTkvwwOVgPAAXTueBdfwsTRXXyv7TlmfozstM6ytCCyno0%2BUCX3U3saW29lKOwhNOHetldegPDcf8NN1ruDK&X-Amz-Signature=d12402e1905eee25beea954d09c90ef4b8c1f19ac3a91757cd6f1540341c6150&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAGM76C4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3IfVnO0%2BPozY%2FO%2FuFcfnplkkG2TjO%2Bb9rYRO1ESVYKgIhAOmSBHY0KH9uNHKKdqmPyW1yTQjah8HzwsGkRkH8l1dzKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs%2F7Ozr3%2BvKYk8GxYq3ANYABcFDZIJ0xKJLBBLiqwnPId1SZdyw0iEqTPAI5i8tlXbCC7%2BFr09QpPdnXI2EtwrEj704vhSDWtTDV%2FI3Q7Idvk78ubt%2FJvTFX1CKMljCa6pxwN4ALq0TqCaTC9ciAlnwhdN4N%2BmaJKdhrcugxfhiuPx2CRb%2BfJC%2FlRk7Z9okPj%2BAdIRyVWk1hcsQOyUnGIVXJGHAWIDIaS6TFnVtDWGPlAq4TQfBxSxA%2Fvt34zzoInikDa%2Fu3IXB49X9U%2B%2By9SESZypjLkTTUaqctj04cOVi%2BSgVoz5qrpTlGO0%2F0b%2BJ5FPVwCiFGpAbSgZuIbxZOXjdyPqe8vBamAT3zMMXh039dru5i5SgBiM%2Bl1WasBHJThxdTWYmXlalX%2FxeOYafYizpAS25Xs9Q5g57QoetoS7vJDqrh1kKN1LWTiK200snpTgqGTFtTZOpVCB9K%2FozA1QP%2F%2BikDBXyGrseTNxPOpUqkAzj1Q77FNhrkLqypYZjRAnzEzumEwnG%2FOhoP5tt51vaRVNB42ouWjF5EUiAPw8FGeCwTmKxSg9YwKdTntlQtzDvvbvLdQkfb1jK1dPiruajRVT0cAiGS40H04%2BHKb%2BDAenFnS%2BzFAI1KWAaX4hJ0lkBJ%2Fx9ovQVIHnsTCRzfW8BjqkAQucKfKwWwZ69qSUomp5b6PPguMOmUpciTDOpy5qFtpO4jlQNMEBFUqQgX6f5R8J%2FEJtDurQzdHPHaeqvfjZf7MvXVTmGvWVgPNcALdgUL5pcjCjYc2kxa2fBTNYJKp0fAOVGsDWgTkvwwOVgPAAXTueBdfwsTRXXyv7TlmfozstM6ytCCyno0%2BUCX3U3saW29lKOwhNOHetldegPDcf8NN1ruDK&X-Amz-Signature=d289bc039fc0af4f7a0aa83bfaad48592a39bd0e3a27301b576f64d65fd950ad&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAGM76C4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3IfVnO0%2BPozY%2FO%2FuFcfnplkkG2TjO%2Bb9rYRO1ESVYKgIhAOmSBHY0KH9uNHKKdqmPyW1yTQjah8HzwsGkRkH8l1dzKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs%2F7Ozr3%2BvKYk8GxYq3ANYABcFDZIJ0xKJLBBLiqwnPId1SZdyw0iEqTPAI5i8tlXbCC7%2BFr09QpPdnXI2EtwrEj704vhSDWtTDV%2FI3Q7Idvk78ubt%2FJvTFX1CKMljCa6pxwN4ALq0TqCaTC9ciAlnwhdN4N%2BmaJKdhrcugxfhiuPx2CRb%2BfJC%2FlRk7Z9okPj%2BAdIRyVWk1hcsQOyUnGIVXJGHAWIDIaS6TFnVtDWGPlAq4TQfBxSxA%2Fvt34zzoInikDa%2Fu3IXB49X9U%2B%2By9SESZypjLkTTUaqctj04cOVi%2BSgVoz5qrpTlGO0%2F0b%2BJ5FPVwCiFGpAbSgZuIbxZOXjdyPqe8vBamAT3zMMXh039dru5i5SgBiM%2Bl1WasBHJThxdTWYmXlalX%2FxeOYafYizpAS25Xs9Q5g57QoetoS7vJDqrh1kKN1LWTiK200snpTgqGTFtTZOpVCB9K%2FozA1QP%2F%2BikDBXyGrseTNxPOpUqkAzj1Q77FNhrkLqypYZjRAnzEzumEwnG%2FOhoP5tt51vaRVNB42ouWjF5EUiAPw8FGeCwTmKxSg9YwKdTntlQtzDvvbvLdQkfb1jK1dPiruajRVT0cAiGS40H04%2BHKb%2BDAenFnS%2BzFAI1KWAaX4hJ0lkBJ%2Fx9ovQVIHnsTCRzfW8BjqkAQucKfKwWwZ69qSUomp5b6PPguMOmUpciTDOpy5qFtpO4jlQNMEBFUqQgX6f5R8J%2FEJtDurQzdHPHaeqvfjZf7MvXVTmGvWVgPNcALdgUL5pcjCjYc2kxa2fBTNYJKp0fAOVGsDWgTkvwwOVgPAAXTueBdfwsTRXXyv7TlmfozstM6ytCCyno0%2BUCX3U3saW29lKOwhNOHetldegPDcf8NN1ruDK&X-Amz-Signature=e1ec22663080ae1f36a07fe6d1c2a61660270fe172a7c8a94d48b2f144a8f9db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAGM76C4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3IfVnO0%2BPozY%2FO%2FuFcfnplkkG2TjO%2Bb9rYRO1ESVYKgIhAOmSBHY0KH9uNHKKdqmPyW1yTQjah8HzwsGkRkH8l1dzKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs%2F7Ozr3%2BvKYk8GxYq3ANYABcFDZIJ0xKJLBBLiqwnPId1SZdyw0iEqTPAI5i8tlXbCC7%2BFr09QpPdnXI2EtwrEj704vhSDWtTDV%2FI3Q7Idvk78ubt%2FJvTFX1CKMljCa6pxwN4ALq0TqCaTC9ciAlnwhdN4N%2BmaJKdhrcugxfhiuPx2CRb%2BfJC%2FlRk7Z9okPj%2BAdIRyVWk1hcsQOyUnGIVXJGHAWIDIaS6TFnVtDWGPlAq4TQfBxSxA%2Fvt34zzoInikDa%2Fu3IXB49X9U%2B%2By9SESZypjLkTTUaqctj04cOVi%2BSgVoz5qrpTlGO0%2F0b%2BJ5FPVwCiFGpAbSgZuIbxZOXjdyPqe8vBamAT3zMMXh039dru5i5SgBiM%2Bl1WasBHJThxdTWYmXlalX%2FxeOYafYizpAS25Xs9Q5g57QoetoS7vJDqrh1kKN1LWTiK200snpTgqGTFtTZOpVCB9K%2FozA1QP%2F%2BikDBXyGrseTNxPOpUqkAzj1Q77FNhrkLqypYZjRAnzEzumEwnG%2FOhoP5tt51vaRVNB42ouWjF5EUiAPw8FGeCwTmKxSg9YwKdTntlQtzDvvbvLdQkfb1jK1dPiruajRVT0cAiGS40H04%2BHKb%2BDAenFnS%2BzFAI1KWAaX4hJ0lkBJ%2Fx9ovQVIHnsTCRzfW8BjqkAQucKfKwWwZ69qSUomp5b6PPguMOmUpciTDOpy5qFtpO4jlQNMEBFUqQgX6f5R8J%2FEJtDurQzdHPHaeqvfjZf7MvXVTmGvWVgPNcALdgUL5pcjCjYc2kxa2fBTNYJKp0fAOVGsDWgTkvwwOVgPAAXTueBdfwsTRXXyv7TlmfozstM6ytCCyno0%2BUCX3U3saW29lKOwhNOHetldegPDcf8NN1ruDK&X-Amz-Signature=a20481a96cad26caee2ec4bd9a863f2bf69caf621db601ba6a6bab0b2340a588&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAGM76C4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3IfVnO0%2BPozY%2FO%2FuFcfnplkkG2TjO%2Bb9rYRO1ESVYKgIhAOmSBHY0KH9uNHKKdqmPyW1yTQjah8HzwsGkRkH8l1dzKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxs%2F7Ozr3%2BvKYk8GxYq3ANYABcFDZIJ0xKJLBBLiqwnPId1SZdyw0iEqTPAI5i8tlXbCC7%2BFr09QpPdnXI2EtwrEj704vhSDWtTDV%2FI3Q7Idvk78ubt%2FJvTFX1CKMljCa6pxwN4ALq0TqCaTC9ciAlnwhdN4N%2BmaJKdhrcugxfhiuPx2CRb%2BfJC%2FlRk7Z9okPj%2BAdIRyVWk1hcsQOyUnGIVXJGHAWIDIaS6TFnVtDWGPlAq4TQfBxSxA%2Fvt34zzoInikDa%2Fu3IXB49X9U%2B%2By9SESZypjLkTTUaqctj04cOVi%2BSgVoz5qrpTlGO0%2F0b%2BJ5FPVwCiFGpAbSgZuIbxZOXjdyPqe8vBamAT3zMMXh039dru5i5SgBiM%2Bl1WasBHJThxdTWYmXlalX%2FxeOYafYizpAS25Xs9Q5g57QoetoS7vJDqrh1kKN1LWTiK200snpTgqGTFtTZOpVCB9K%2FozA1QP%2F%2BikDBXyGrseTNxPOpUqkAzj1Q77FNhrkLqypYZjRAnzEzumEwnG%2FOhoP5tt51vaRVNB42ouWjF5EUiAPw8FGeCwTmKxSg9YwKdTntlQtzDvvbvLdQkfb1jK1dPiruajRVT0cAiGS40H04%2BHKb%2BDAenFnS%2BzFAI1KWAaX4hJ0lkBJ%2Fx9ovQVIHnsTCRzfW8BjqkAQucKfKwWwZ69qSUomp5b6PPguMOmUpciTDOpy5qFtpO4jlQNMEBFUqQgX6f5R8J%2FEJtDurQzdHPHaeqvfjZf7MvXVTmGvWVgPNcALdgUL5pcjCjYc2kxa2fBTNYJKp0fAOVGsDWgTkvwwOVgPAAXTueBdfwsTRXXyv7TlmfozstM6ytCCyno0%2BUCX3U3saW29lKOwhNOHetldegPDcf8NN1ruDK&X-Amz-Signature=b4d4435c7e90fb1dd917400cbc86b4c845387c130d6a7acf2ad0bd535e1631ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BHFNEMU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF10Ppb6lfFUigrGz8k1ZZQxJg8u2XyIUfyTir0M6LB6AiEAzCP1vjxKRsdDR5Rn3nEgl1BEBt3%2BU0Dm3f3jrGP93lwqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE3kXclkU5LhVlquHircA5aUfhxU7MmfULEjHs5imGkfAXky8L1pYrXBfyw6ymjxokIDCWcfd0bxtCGIfmUJKFKMj379o7HWneqiSLzw6WZK0vPPdu01Fpd%2Bl7iw%2FtkFjkhRV3%2FzWnBYMpYQZLoeai4G9N8h31i6AB0AYLHTqlA2xBxJ4C5az9HzShw2z7cXLDnikUOePvsoUHt0ojo%2B41kvs2Jk27j65bg698ygb9eRtTt8wrNxa5acXvk1XToKogfwVjoWH4IJ16JgThNy9M1%2Bh1DcOymmOEhRJ%2FAibnzbIwEi3Vq%2FBh39%2BYxHMRm6gb6KgTv1a6%2FMPuldRPwoza5njJAEW6n%2B3OI2rLAwqHsUx4yKJi17lgiw6ADuzzDE3W%2FSRgTXlcC7LQL0E4C%2BOy8J83%2FTk4qbeGYk5PzCJZRf%2FghDQRi5UQZ2u%2FGbVlJaKyzEGG3OYiWC32o%2BWlLDWxaCAbhz6pKseRKTQH0%2FVQKRiSndsiygbcvHSYXUL62Tp4OxESOySrK%2BRXdKkVmU4sgMRDFK%2BrnBUXVzOPuFbNPCjQkg6%2FBXkrzqkYHl8EOQwHJ8%2B8Ov4TJAmGkX9pgesw5pK9WvbPNOH5UKCnvg0RmDzq8iO4OKd3CL6a5aDxl4XOZ6dW0v%2F0UkRklSMNfM9bwGOqUBlSliD4B2wLqqEEAHPPS3h7ok2kScJ9MJw10IIVWRgkkP4YXhSd8gjYNgHS9g0J3XAdrn6P525UixOm6uH4r%2B%2FC57OpzhVOVHpq3YPDJ8V3YNorkQP0VNtBFgRR%2BD5bXu%2F7vpLvjS0fXt59lE8ZMBVjChekZuWT7M4nrbe9cwh7PNhTuz%2BrHwWyEZTx6IhESFv%2B8sej2oPULZGfBiaPjt4P24ef4g&X-Amz-Signature=ba0ef7d74f67213c486ed1160527cd147141023987540e5e973746cb22a656f9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSSMMNQN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9PCDbPtr%2B0X5l%2F18JuU5XPyHV5CQFL9Vp8f1%2Bq7%2FoMwIgeyfhX5ijewL2LmcUGRHglHv9OwssLW4OJFjWGL0SZTEqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLMOfIgpD8tZeMQ7iCrcAyem4kjBEjqej0QE80lbtc5jHtboR8EjpZWBc2udDOobUH6RDCfPvmMlZLd3lzPKDCeg2Iw1109%2F%2ByqUIMRCOq3CCQleedJwqxpAjOTOz%2BPXCYAqRdb4kMkPS8oNPB1dEdtqw%2BlUAeNS7s3G%2B36EBYGUcrzbdpe7jreWLl2g3dAX%2FS1DQlO2uz%2FHpc3qssSmS2q0HlPuqhRaJOTVxnI1PFU5MLPCUoiUXl%2Fl13dnzIQ1KT0qzOT5M%2FQv7q%2FC05A8ZHxSffrQ7yjAdhYioLxEI9ZfrLqaVp7F3JbBUmHn8%2Fs3AityfgHEwnPv%2Bsku9xiEaitNES3KFur0Ugm8Xt0kv0q6YZhLDe8YCrLo5z5nJvEdOZ08x9UOs4r3iqOYEwRuwT%2F%2BCWWuzCNHa3P0UDJ43bhlBXGysAtIOkleCGz79WHC5F2yTVogdlHX5eHAdQ4vAnOW%2FmOiP0t0GrNDJu9ipAOQxMR3mAZH3o%2BZ8YqLpWNjilxVny%2B9EKArC5TrHqkr4y%2FbCYQY0JpSfI7uSSjRHc%2B9kcvTatL4RtX5qHkPJOlNrx7trtlJATPgGC7I83eYnv%2BUr1fKDbYB4sbF0hAM5oOb5mpp9wLmYJx8yU8%2ByDAIU80Z6pgoCmThvPSzMO3M9bwGOqUBdFSM8WuP6ezAHfL0tJzmYclLgx3KRUsV85cESDvU%2BiMTwqO5JKtG9Y6%2BfJStLctqgwy9uPSR5Zb%2Fe%2BoxXlvexGLu1B8n9I7xTBFXrjZmqndm1cWm8RPpGnAlD%2Bsq2PFrdkFgK6imSaCVZNZHOUKyTEa%2Fly1jyZd%2F9XHO5xUM0Um%2FYZqJGX6UgaNuZR3gpXVYNcKqXVCywru%2FZlzXsKV2On22o2I%2B&X-Amz-Signature=8f3a1b3c607ee44e46b5960b7a1fe67ff05f1f5b060f7be3a06ca4179291b391&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EN747EV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH0myfJWJyWvRHTLGrseEXpzi9JKIs7tMBWitE6jV%2BDMAiEAt3c5EehB2h97hx7fBu9Rfm41wk47aDCwhIw6heklCeEqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvT7%2Fy2sYdwKkDxKSrcA79VZei3TDKaNiGSYZeVKxpoX%2Fp883ZWfF23lDYWrQ%2Fiyoxz7iJ7qmwfQxmk8exA9gGenRWXuJzvyMtT3kVN3BNIk2dHcROSX8%2ByEISbadHbyyxdxFdldPTkV28fc4FqLro6i%2BdMKk9A5ZqIC7MdP9GdZjICZLpOErTDa2%2BCvvYHgB7ppP7divnT6eStdtKrGNmWfwDVOBAwwUTdAAEgzV23ow8khmM7gJnO7ka%2B10JpKS4slaBjR3etW3CJgsw88xmZtAjjklldYF4tgpeqfY4HujWXezM1x4kEHA5n0F9JEh4ndET6%2BDOCWqiHfNyH0Amoovp9IgiF04VyhDMbUp3bJDsTb5kTKyi20P%2BlsvQb4MJL3gI4ebyJ1KFNj3L2S922n5Az%2Bxs%2BHNYV8B5JoKj0YVzzQZc9oDwlJoPpQabq2oBzJnJ8SC8Ok6Ke1%2BIEbr%2FUVqlNrmBIrnZ0CaDiM6NC7jQQZBufWGCDzm1VHmvDOCBLFEn4ihMe%2B2EPvpay3neiQm%2BBKTl6BQLkRpB0XDOYLk0PI3vk8VKuA%2BHFgO1vl2pEOeHrwm3nWhg76tUmZyS40kVe2uaHLp0qSicL5icvw3Pn8whbAFTEB7I4NvRHt3VlAGR%2FzTHOBUBoMIrN9bwGOqUBeIl3zFqMLXoK7dbF2ijFpfV%2B0JSGaX5Ym6BdukXym%2BN%2B8c%2FRl062rBRckjZ5MjFPBJpGfM8aQC3va5TnLZEoGCfaJ9ikpKIKK56U3hulZFAhJpTt6uQ3vTe4xT4Gjuy9sC02iLrKiWCxjgSr%2FuDx6OaevlTdVlCb4YjsKwq4Op%2BgrfS%2BYLNvR4izL8MApKXRbeuQXI8Fkhn46ZrPzUQ%2FHo8%2Baizu&X-Amz-Signature=1e2abbd4c10889dd864443b7d85749ae1538cc3d2ac86b0a95d59319ee71a7d1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EN747EV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH0myfJWJyWvRHTLGrseEXpzi9JKIs7tMBWitE6jV%2BDMAiEAt3c5EehB2h97hx7fBu9Rfm41wk47aDCwhIw6heklCeEqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvT7%2Fy2sYdwKkDxKSrcA79VZei3TDKaNiGSYZeVKxpoX%2Fp883ZWfF23lDYWrQ%2Fiyoxz7iJ7qmwfQxmk8exA9gGenRWXuJzvyMtT3kVN3BNIk2dHcROSX8%2ByEISbadHbyyxdxFdldPTkV28fc4FqLro6i%2BdMKk9A5ZqIC7MdP9GdZjICZLpOErTDa2%2BCvvYHgB7ppP7divnT6eStdtKrGNmWfwDVOBAwwUTdAAEgzV23ow8khmM7gJnO7ka%2B10JpKS4slaBjR3etW3CJgsw88xmZtAjjklldYF4tgpeqfY4HujWXezM1x4kEHA5n0F9JEh4ndET6%2BDOCWqiHfNyH0Amoovp9IgiF04VyhDMbUp3bJDsTb5kTKyi20P%2BlsvQb4MJL3gI4ebyJ1KFNj3L2S922n5Az%2Bxs%2BHNYV8B5JoKj0YVzzQZc9oDwlJoPpQabq2oBzJnJ8SC8Ok6Ke1%2BIEbr%2FUVqlNrmBIrnZ0CaDiM6NC7jQQZBufWGCDzm1VHmvDOCBLFEn4ihMe%2B2EPvpay3neiQm%2BBKTl6BQLkRpB0XDOYLk0PI3vk8VKuA%2BHFgO1vl2pEOeHrwm3nWhg76tUmZyS40kVe2uaHLp0qSicL5icvw3Pn8whbAFTEB7I4NvRHt3VlAGR%2FzTHOBUBoMIrN9bwGOqUBeIl3zFqMLXoK7dbF2ijFpfV%2B0JSGaX5Ym6BdukXym%2BN%2B8c%2FRl062rBRckjZ5MjFPBJpGfM8aQC3va5TnLZEoGCfaJ9ikpKIKK56U3hulZFAhJpTt6uQ3vTe4xT4Gjuy9sC02iLrKiWCxjgSr%2FuDx6OaevlTdVlCb4YjsKwq4Op%2BgrfS%2BYLNvR4izL8MApKXRbeuQXI8Fkhn46ZrPzUQ%2FHo8%2Baizu&X-Amz-Signature=41d8c879d8dcaa9a26a1262ebcd12d2e0ad2c90a6d9b1a23135f89235410b48f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
