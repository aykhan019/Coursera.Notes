

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJU2DNYH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHgorKiw4FB%2B1vw5ySrU%2FA%2BKLhM1imtNE%2FjgcEthn2GvAiA8HG93En7UyR7yee%2FdPBqzPIkAKGYb8xdbZkBblaq27Cr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMtoVLjnTCiT3xCOjXKtwDSvrnVSfnsiowgfGhIPblffNpEH25lDXsjzC0J9%2Fe6dIA967osWxlCOYYJTSSfTMeqPIrp5ilVbpAmEhWTYkDQ5TTvaMtwrn6iJjT0c51X6nnE2G%2BFV%2Bk2xd1sUgE3jRUr3fu5BLTjrkPEgOV%2F5kaVYPaRiLBEa%2FKSiw6Ru9CDTLFu9hW%2FOeakj2xLmZ4EpQ20GJxV%2BmZ21w9M699PrXIR5L4TVi9pDDN10lF8cqhYHVaWUEVl4OxaWwgQvOIH5CL5dGM9frTjFQaQWMfv028iUuNkp5wmqzabmlFKR3sIF63jKFIqX%2BaXVGiH16snkB4CzDl%2B8zAwWdL9LZ9%2FWCZ%2F7Q9VTFEDZETbhWWLwIiLwNUSuhCQ4jmb3Q6Fwcwr9jpEH98Bx7IgK8kpQRr20iRya4RFFDuh6mewVyWbpIqUstDad2TG14patQGXS%2FPbdHzpdeIXACI7kInSNtUWHV8TNw7g1lpmDRUpO653ijaY4AHukYd%2B08gje6tbzOCAfHIibBPnXOq2IXflNfbW38Yb1bhy8O7Wc26yUr2ywvgcHsiy6EGeKiNm0lIFCkirbklshGoMmfkWiWLrQ%2BrI0p9nIzWZH%2Fgwmqi%2FWKJdp8xsxhh%2FzlHi8cd%2BOKUE1kw6N6PvQY6pgGFNvzItzbuZbOLmYsdt6ayjuqufqcMHtYFsUeQUx0NKKmkbPAYZSgOWDdrD0UWCTt8M3UBEbXdv40u1s2WP8fpcyDnHOKGq4irKF%2B858LvEWXNoFc1yLadVaXx5yjoFIQX4xUMYNG9m7vC8SogHfAMSbwteIxN0TlXjlpegDDZb19Piq%2BfMTOEAJ1ByR9%2Fm7x7swO1I9qZDCdsGaT%2FQAqfZJ1MhkZ8&X-Amz-Signature=e84ccae15d289616e58b4954d0aeb34e5f335dc2152962ab1f224c8fcede198f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJU2DNYH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHgorKiw4FB%2B1vw5ySrU%2FA%2BKLhM1imtNE%2FjgcEthn2GvAiA8HG93En7UyR7yee%2FdPBqzPIkAKGYb8xdbZkBblaq27Cr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMtoVLjnTCiT3xCOjXKtwDSvrnVSfnsiowgfGhIPblffNpEH25lDXsjzC0J9%2Fe6dIA967osWxlCOYYJTSSfTMeqPIrp5ilVbpAmEhWTYkDQ5TTvaMtwrn6iJjT0c51X6nnE2G%2BFV%2Bk2xd1sUgE3jRUr3fu5BLTjrkPEgOV%2F5kaVYPaRiLBEa%2FKSiw6Ru9CDTLFu9hW%2FOeakj2xLmZ4EpQ20GJxV%2BmZ21w9M699PrXIR5L4TVi9pDDN10lF8cqhYHVaWUEVl4OxaWwgQvOIH5CL5dGM9frTjFQaQWMfv028iUuNkp5wmqzabmlFKR3sIF63jKFIqX%2BaXVGiH16snkB4CzDl%2B8zAwWdL9LZ9%2FWCZ%2F7Q9VTFEDZETbhWWLwIiLwNUSuhCQ4jmb3Q6Fwcwr9jpEH98Bx7IgK8kpQRr20iRya4RFFDuh6mewVyWbpIqUstDad2TG14patQGXS%2FPbdHzpdeIXACI7kInSNtUWHV8TNw7g1lpmDRUpO653ijaY4AHukYd%2B08gje6tbzOCAfHIibBPnXOq2IXflNfbW38Yb1bhy8O7Wc26yUr2ywvgcHsiy6EGeKiNm0lIFCkirbklshGoMmfkWiWLrQ%2BrI0p9nIzWZH%2Fgwmqi%2FWKJdp8xsxhh%2FzlHi8cd%2BOKUE1kw6N6PvQY6pgGFNvzItzbuZbOLmYsdt6ayjuqufqcMHtYFsUeQUx0NKKmkbPAYZSgOWDdrD0UWCTt8M3UBEbXdv40u1s2WP8fpcyDnHOKGq4irKF%2B858LvEWXNoFc1yLadVaXx5yjoFIQX4xUMYNG9m7vC8SogHfAMSbwteIxN0TlXjlpegDDZb19Piq%2BfMTOEAJ1ByR9%2Fm7x7swO1I9qZDCdsGaT%2FQAqfZJ1MhkZ8&X-Amz-Signature=a4e835102d6a499997faf53e793a70abb605487ecc34e88cf72c1d212667dbe3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJU2DNYH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHgorKiw4FB%2B1vw5ySrU%2FA%2BKLhM1imtNE%2FjgcEthn2GvAiA8HG93En7UyR7yee%2FdPBqzPIkAKGYb8xdbZkBblaq27Cr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMtoVLjnTCiT3xCOjXKtwDSvrnVSfnsiowgfGhIPblffNpEH25lDXsjzC0J9%2Fe6dIA967osWxlCOYYJTSSfTMeqPIrp5ilVbpAmEhWTYkDQ5TTvaMtwrn6iJjT0c51X6nnE2G%2BFV%2Bk2xd1sUgE3jRUr3fu5BLTjrkPEgOV%2F5kaVYPaRiLBEa%2FKSiw6Ru9CDTLFu9hW%2FOeakj2xLmZ4EpQ20GJxV%2BmZ21w9M699PrXIR5L4TVi9pDDN10lF8cqhYHVaWUEVl4OxaWwgQvOIH5CL5dGM9frTjFQaQWMfv028iUuNkp5wmqzabmlFKR3sIF63jKFIqX%2BaXVGiH16snkB4CzDl%2B8zAwWdL9LZ9%2FWCZ%2F7Q9VTFEDZETbhWWLwIiLwNUSuhCQ4jmb3Q6Fwcwr9jpEH98Bx7IgK8kpQRr20iRya4RFFDuh6mewVyWbpIqUstDad2TG14patQGXS%2FPbdHzpdeIXACI7kInSNtUWHV8TNw7g1lpmDRUpO653ijaY4AHukYd%2B08gje6tbzOCAfHIibBPnXOq2IXflNfbW38Yb1bhy8O7Wc26yUr2ywvgcHsiy6EGeKiNm0lIFCkirbklshGoMmfkWiWLrQ%2BrI0p9nIzWZH%2Fgwmqi%2FWKJdp8xsxhh%2FzlHi8cd%2BOKUE1kw6N6PvQY6pgGFNvzItzbuZbOLmYsdt6ayjuqufqcMHtYFsUeQUx0NKKmkbPAYZSgOWDdrD0UWCTt8M3UBEbXdv40u1s2WP8fpcyDnHOKGq4irKF%2B858LvEWXNoFc1yLadVaXx5yjoFIQX4xUMYNG9m7vC8SogHfAMSbwteIxN0TlXjlpegDDZb19Piq%2BfMTOEAJ1ByR9%2Fm7x7swO1I9qZDCdsGaT%2FQAqfZJ1MhkZ8&X-Amz-Signature=4209a36ebea5231f6c06a78daca042909bc771d3e01cb86129741e02f68ecd21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJU2DNYH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHgorKiw4FB%2B1vw5ySrU%2FA%2BKLhM1imtNE%2FjgcEthn2GvAiA8HG93En7UyR7yee%2FdPBqzPIkAKGYb8xdbZkBblaq27Cr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMtoVLjnTCiT3xCOjXKtwDSvrnVSfnsiowgfGhIPblffNpEH25lDXsjzC0J9%2Fe6dIA967osWxlCOYYJTSSfTMeqPIrp5ilVbpAmEhWTYkDQ5TTvaMtwrn6iJjT0c51X6nnE2G%2BFV%2Bk2xd1sUgE3jRUr3fu5BLTjrkPEgOV%2F5kaVYPaRiLBEa%2FKSiw6Ru9CDTLFu9hW%2FOeakj2xLmZ4EpQ20GJxV%2BmZ21w9M699PrXIR5L4TVi9pDDN10lF8cqhYHVaWUEVl4OxaWwgQvOIH5CL5dGM9frTjFQaQWMfv028iUuNkp5wmqzabmlFKR3sIF63jKFIqX%2BaXVGiH16snkB4CzDl%2B8zAwWdL9LZ9%2FWCZ%2F7Q9VTFEDZETbhWWLwIiLwNUSuhCQ4jmb3Q6Fwcwr9jpEH98Bx7IgK8kpQRr20iRya4RFFDuh6mewVyWbpIqUstDad2TG14patQGXS%2FPbdHzpdeIXACI7kInSNtUWHV8TNw7g1lpmDRUpO653ijaY4AHukYd%2B08gje6tbzOCAfHIibBPnXOq2IXflNfbW38Yb1bhy8O7Wc26yUr2ywvgcHsiy6EGeKiNm0lIFCkirbklshGoMmfkWiWLrQ%2BrI0p9nIzWZH%2Fgwmqi%2FWKJdp8xsxhh%2FzlHi8cd%2BOKUE1kw6N6PvQY6pgGFNvzItzbuZbOLmYsdt6ayjuqufqcMHtYFsUeQUx0NKKmkbPAYZSgOWDdrD0UWCTt8M3UBEbXdv40u1s2WP8fpcyDnHOKGq4irKF%2B858LvEWXNoFc1yLadVaXx5yjoFIQX4xUMYNG9m7vC8SogHfAMSbwteIxN0TlXjlpegDDZb19Piq%2BfMTOEAJ1ByR9%2Fm7x7swO1I9qZDCdsGaT%2FQAqfZJ1MhkZ8&X-Amz-Signature=6a2df90102e043dbcf77b4328da4351bda49b05b0f952eb8ef3f796c121e4a67&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJU2DNYH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHgorKiw4FB%2B1vw5ySrU%2FA%2BKLhM1imtNE%2FjgcEthn2GvAiA8HG93En7UyR7yee%2FdPBqzPIkAKGYb8xdbZkBblaq27Cr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMtoVLjnTCiT3xCOjXKtwDSvrnVSfnsiowgfGhIPblffNpEH25lDXsjzC0J9%2Fe6dIA967osWxlCOYYJTSSfTMeqPIrp5ilVbpAmEhWTYkDQ5TTvaMtwrn6iJjT0c51X6nnE2G%2BFV%2Bk2xd1sUgE3jRUr3fu5BLTjrkPEgOV%2F5kaVYPaRiLBEa%2FKSiw6Ru9CDTLFu9hW%2FOeakj2xLmZ4EpQ20GJxV%2BmZ21w9M699PrXIR5L4TVi9pDDN10lF8cqhYHVaWUEVl4OxaWwgQvOIH5CL5dGM9frTjFQaQWMfv028iUuNkp5wmqzabmlFKR3sIF63jKFIqX%2BaXVGiH16snkB4CzDl%2B8zAwWdL9LZ9%2FWCZ%2F7Q9VTFEDZETbhWWLwIiLwNUSuhCQ4jmb3Q6Fwcwr9jpEH98Bx7IgK8kpQRr20iRya4RFFDuh6mewVyWbpIqUstDad2TG14patQGXS%2FPbdHzpdeIXACI7kInSNtUWHV8TNw7g1lpmDRUpO653ijaY4AHukYd%2B08gje6tbzOCAfHIibBPnXOq2IXflNfbW38Yb1bhy8O7Wc26yUr2ywvgcHsiy6EGeKiNm0lIFCkirbklshGoMmfkWiWLrQ%2BrI0p9nIzWZH%2Fgwmqi%2FWKJdp8xsxhh%2FzlHi8cd%2BOKUE1kw6N6PvQY6pgGFNvzItzbuZbOLmYsdt6ayjuqufqcMHtYFsUeQUx0NKKmkbPAYZSgOWDdrD0UWCTt8M3UBEbXdv40u1s2WP8fpcyDnHOKGq4irKF%2B858LvEWXNoFc1yLadVaXx5yjoFIQX4xUMYNG9m7vC8SogHfAMSbwteIxN0TlXjlpegDDZb19Piq%2BfMTOEAJ1ByR9%2Fm7x7swO1I9qZDCdsGaT%2FQAqfZJ1MhkZ8&X-Amz-Signature=ed8c8478bfcc6634e2ead7ae303833593c98f6c4a1b5454c09f43bb8a7259918&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJU2DNYH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHgorKiw4FB%2B1vw5ySrU%2FA%2BKLhM1imtNE%2FjgcEthn2GvAiA8HG93En7UyR7yee%2FdPBqzPIkAKGYb8xdbZkBblaq27Cr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMtoVLjnTCiT3xCOjXKtwDSvrnVSfnsiowgfGhIPblffNpEH25lDXsjzC0J9%2Fe6dIA967osWxlCOYYJTSSfTMeqPIrp5ilVbpAmEhWTYkDQ5TTvaMtwrn6iJjT0c51X6nnE2G%2BFV%2Bk2xd1sUgE3jRUr3fu5BLTjrkPEgOV%2F5kaVYPaRiLBEa%2FKSiw6Ru9CDTLFu9hW%2FOeakj2xLmZ4EpQ20GJxV%2BmZ21w9M699PrXIR5L4TVi9pDDN10lF8cqhYHVaWUEVl4OxaWwgQvOIH5CL5dGM9frTjFQaQWMfv028iUuNkp5wmqzabmlFKR3sIF63jKFIqX%2BaXVGiH16snkB4CzDl%2B8zAwWdL9LZ9%2FWCZ%2F7Q9VTFEDZETbhWWLwIiLwNUSuhCQ4jmb3Q6Fwcwr9jpEH98Bx7IgK8kpQRr20iRya4RFFDuh6mewVyWbpIqUstDad2TG14patQGXS%2FPbdHzpdeIXACI7kInSNtUWHV8TNw7g1lpmDRUpO653ijaY4AHukYd%2B08gje6tbzOCAfHIibBPnXOq2IXflNfbW38Yb1bhy8O7Wc26yUr2ywvgcHsiy6EGeKiNm0lIFCkirbklshGoMmfkWiWLrQ%2BrI0p9nIzWZH%2Fgwmqi%2FWKJdp8xsxhh%2FzlHi8cd%2BOKUE1kw6N6PvQY6pgGFNvzItzbuZbOLmYsdt6ayjuqufqcMHtYFsUeQUx0NKKmkbPAYZSgOWDdrD0UWCTt8M3UBEbXdv40u1s2WP8fpcyDnHOKGq4irKF%2B858LvEWXNoFc1yLadVaXx5yjoFIQX4xUMYNG9m7vC8SogHfAMSbwteIxN0TlXjlpegDDZb19Piq%2BfMTOEAJ1ByR9%2Fm7x7swO1I9qZDCdsGaT%2FQAqfZJ1MhkZ8&X-Amz-Signature=39af36a2ab842356b3da25452d755ede1b129473c460138bfcfed234ef6cedfa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJU2DNYH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHgorKiw4FB%2B1vw5ySrU%2FA%2BKLhM1imtNE%2FjgcEthn2GvAiA8HG93En7UyR7yee%2FdPBqzPIkAKGYb8xdbZkBblaq27Cr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMtoVLjnTCiT3xCOjXKtwDSvrnVSfnsiowgfGhIPblffNpEH25lDXsjzC0J9%2Fe6dIA967osWxlCOYYJTSSfTMeqPIrp5ilVbpAmEhWTYkDQ5TTvaMtwrn6iJjT0c51X6nnE2G%2BFV%2Bk2xd1sUgE3jRUr3fu5BLTjrkPEgOV%2F5kaVYPaRiLBEa%2FKSiw6Ru9CDTLFu9hW%2FOeakj2xLmZ4EpQ20GJxV%2BmZ21w9M699PrXIR5L4TVi9pDDN10lF8cqhYHVaWUEVl4OxaWwgQvOIH5CL5dGM9frTjFQaQWMfv028iUuNkp5wmqzabmlFKR3sIF63jKFIqX%2BaXVGiH16snkB4CzDl%2B8zAwWdL9LZ9%2FWCZ%2F7Q9VTFEDZETbhWWLwIiLwNUSuhCQ4jmb3Q6Fwcwr9jpEH98Bx7IgK8kpQRr20iRya4RFFDuh6mewVyWbpIqUstDad2TG14patQGXS%2FPbdHzpdeIXACI7kInSNtUWHV8TNw7g1lpmDRUpO653ijaY4AHukYd%2B08gje6tbzOCAfHIibBPnXOq2IXflNfbW38Yb1bhy8O7Wc26yUr2ywvgcHsiy6EGeKiNm0lIFCkirbklshGoMmfkWiWLrQ%2BrI0p9nIzWZH%2Fgwmqi%2FWKJdp8xsxhh%2FzlHi8cd%2BOKUE1kw6N6PvQY6pgGFNvzItzbuZbOLmYsdt6ayjuqufqcMHtYFsUeQUx0NKKmkbPAYZSgOWDdrD0UWCTt8M3UBEbXdv40u1s2WP8fpcyDnHOKGq4irKF%2B858LvEWXNoFc1yLadVaXx5yjoFIQX4xUMYNG9m7vC8SogHfAMSbwteIxN0TlXjlpegDDZb19Piq%2BfMTOEAJ1ByR9%2Fm7x7swO1I9qZDCdsGaT%2FQAqfZJ1MhkZ8&X-Amz-Signature=ec88ffde5797e8b73976ae7e41295c18cf5ed8efbf39451934d088880d7762ee&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJU2DNYH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHgorKiw4FB%2B1vw5ySrU%2FA%2BKLhM1imtNE%2FjgcEthn2GvAiA8HG93En7UyR7yee%2FdPBqzPIkAKGYb8xdbZkBblaq27Cr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMtoVLjnTCiT3xCOjXKtwDSvrnVSfnsiowgfGhIPblffNpEH25lDXsjzC0J9%2Fe6dIA967osWxlCOYYJTSSfTMeqPIrp5ilVbpAmEhWTYkDQ5TTvaMtwrn6iJjT0c51X6nnE2G%2BFV%2Bk2xd1sUgE3jRUr3fu5BLTjrkPEgOV%2F5kaVYPaRiLBEa%2FKSiw6Ru9CDTLFu9hW%2FOeakj2xLmZ4EpQ20GJxV%2BmZ21w9M699PrXIR5L4TVi9pDDN10lF8cqhYHVaWUEVl4OxaWwgQvOIH5CL5dGM9frTjFQaQWMfv028iUuNkp5wmqzabmlFKR3sIF63jKFIqX%2BaXVGiH16snkB4CzDl%2B8zAwWdL9LZ9%2FWCZ%2F7Q9VTFEDZETbhWWLwIiLwNUSuhCQ4jmb3Q6Fwcwr9jpEH98Bx7IgK8kpQRr20iRya4RFFDuh6mewVyWbpIqUstDad2TG14patQGXS%2FPbdHzpdeIXACI7kInSNtUWHV8TNw7g1lpmDRUpO653ijaY4AHukYd%2B08gje6tbzOCAfHIibBPnXOq2IXflNfbW38Yb1bhy8O7Wc26yUr2ywvgcHsiy6EGeKiNm0lIFCkirbklshGoMmfkWiWLrQ%2BrI0p9nIzWZH%2Fgwmqi%2FWKJdp8xsxhh%2FzlHi8cd%2BOKUE1kw6N6PvQY6pgGFNvzItzbuZbOLmYsdt6ayjuqufqcMHtYFsUeQUx0NKKmkbPAYZSgOWDdrD0UWCTt8M3UBEbXdv40u1s2WP8fpcyDnHOKGq4irKF%2B858LvEWXNoFc1yLadVaXx5yjoFIQX4xUMYNG9m7vC8SogHfAMSbwteIxN0TlXjlpegDDZb19Piq%2BfMTOEAJ1ByR9%2Fm7x7swO1I9qZDCdsGaT%2FQAqfZJ1MhkZ8&X-Amz-Signature=c56d23bee4c227a73e909cc509e33e4a88b43a5562a84b609e14c769df711e06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4TM635T%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQCGrYGH0yA9dWejqmqoGb71i7%2FDMDIlSHSQUy%2BsH13P%2FQIhAP%2FboSGVi43LpmcR2Ai6ME%2BYhaKOU8xY7lZMQqydt9d%2FKv8DCFAQABoMNjM3NDIzMTgzODA1IgxUmeXU0jQmRGQ0dvUq3AOmF%2Fp3uaNbuE01QZW2USjUOsdPi%2BJYD2U6efDJBITXYQx1uTgDIlFSEMKuGOvftKBmgGiDOiK2uSell03L3xMJmd74tRMF6fpvOWCmZTOrROu4PDk4T5taMCO%2FqR6yG76FyX5VpU7E1FnbSKUN64yUIif7U%2BTY7j9IFD4ewOtxrBiuOO%2FynU2GhRoDgcA5RPMq5xyprB6hq8CERsnzeho5pNocLxYYjt%2Fimaz6D%2FLypEDOhZ8%2F6HvxwYZhkATEb%2FQL%2FGc3j0CuNQELJQzr3yfuurEtvNzpEvqNxzQZJK8GJJY8MVEcLPjgsbPAsNpYqzFY5B7Vabg8r0en9SnBEomo6JO7yU2g3quGsM384hLBhv0FchS%2BY2uce3%2BiSepiMvD1sNPNb1wBVT%2BNRvHs9urbwTNkbURnCVYoidtUYG0%2BaR%2BtrOcklpnZ1m3p4V1krqRqfWSj4Bcwe%2FnVEd6%2FtqlBlRso2Gt0Np2qsUIKpbVFpY%2B4gwCHs%2BVs6Ez%2FjMlemhHSj4dEQ2swjrpqS%2FW4FuOUtKxqDOD72yfofpvc6pW3tkw4h%2BGXoN63Az1VI9dJ5adTA15SWriuT9IxjzwyDx3gCYxHJi51T1s23UJc0E6NqBJAOEn6T0mxIdP9KjCH3I%2B9BjqkAaAvsMOhxFPb1Eiy4PrqNXyE%2Fg6ATTZDqbFtqyl7DHZlKmiomUaTobQsPHCZfLRc7m%2BeMYdXF8VrPqglFfOhbacko00ctLwHeq1K%2FEnLwZcrAwvz3KyRu9BWjHdRkiaS7wS9QIpAOQ8yEwpUScrQPwanaiISp2kyQXA%2Fbbp%2FC9Dzc%2Ft1g0OoTotnfbrSu2UsE4xrwxFkm44fCbgmZcvR53jsXE6z&X-Amz-Signature=5271f48414d76b60af5ef9fa294dafd50fb0a0c94428a6945fff739cdaaa728f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7JENUI6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIBTDKqYtb2wwdDkStwRNpXFCdT8zRxW4EWunN%2Fi19ddPAiAlbRWvlqq7nLS2%2B6dmc%2BKpRgnP9Ez4K%2F01%2Bm7%2BLbxSfyr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIM6OyLvR4XQP6r%2BQiWKtwDlTctjSj3zWyj7pbookUnY%2BjO4778u%2F%2B1GZ0%2FpOHYwcnjeJRP8R1DH7WbgPhwogwANxLidksOmwYlsCdHqTkOM2hga4vg5yVsMkfjpHxB65LmHj8rcj6WwMNM5o8bMLWTw1A%2FuZCRBRxHVGPhxknk%2F5xu%2FiU2Jfe%2BdOBqnh6TiwkL4BbnJR2%2BitfXdpWghmZiER%2FvM73IQW5DaOnWCkW09b%2BnEwPc7WwRigxSe2uVNeEh1Sm8jfYbTl3ZJHFuBp3WlZg1KnHD%2FzuJiMY4aqE94aK5oYFBQCT2IL5tRkM8MZr%2FgqsPwyKxPTsDJ3Bi9gg9wDabbzsK8aqBoRJry2Af0J48TfxiBYsMC%2BGfS2HwOyBsZ%2FAl8ZuGLRQI%2F0i3WYALjnHcbVqmuX040acWW7wrGHACmEIf7Ah01%2F6wYlj7%2BhLdwPo1F21aqS3aiBJhDCb3WOb0tFtkHDiGPxiigKKKvNUFQQWOASr3sdCrtivpLV0CfQ6ODCzOZhXRy8RTLWgmhKyf%2FaI3w6KaCJbiDs6R%2BBBCFcwz1vMteZEM3N7iR10rZD2lp80UI7S9oJqlVHnZjb7HYmqhrT9Y0qZiEKgJdhUhF7VMmvWpjijGeTakDXUP1Sxi%2FPRUdHqfe2kwlNyPvQY6pgFZ0Ecd%2FqIfoRczl2GjWr4MjKtixV%2F38%2F1rZMfHvcv2aVIPFIeaz1xMR75QYPvJCp0c3KQ3Rs5P3E3ylWNi3MGFcqKPdHBfV4GJUfqYxo31jDOqqbmbkFQ8O2ZCkaKbQr%2FVDlcIZyMJvOQ5jy8U%2BCFX%2F1vAill3VO9NANR2NyVghxkAYtranSUK5M1Vc315nr9zywdHON3Q6%2BslyCaK3QQS3tn0EFwD&X-Amz-Signature=7140d02b5a23de213d69c6bfbb719e98b0ff6dc766dd83627b7334014856bc49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI4VWK7V%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHiIgo2TkO4CQb4BHX9N9NgPqGaE0sCk%2FHwW4C7ThP0wAiBE0V13aK4wvvFy7LV7Lp%2Bi6g36IG3sCFncBv7MmjzPqir%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIM6OMmZWvTSHl2I%2BCYKtwDBsxTbnaeJ%2BHX1lMinhyBNQ3FPIFrYwxL5sDoeSGh2SLfumHL6oEnNhpPw7kcM88kD1ndtPDFqdOvRJ%2F3vW0cJ48r3VlmZB7IoKxFom%2Flymid9AHz%2FnJuiJFChqpmHNjwy2nswcVwmQqp%2BsFgM6yHXPXchIdpJzWLFetfNCIfSIaReVpEnwyywIpax65X%2F98g5OlngkODGT0gD07kp1PQM6kX1PMc%2FJYVgzLy5UjRrF71g9Ihq81x0aHtBcEdGbj9Cxq%2B4JG9GjtG9B%2BAvzDAlUSl18uEkFrJlYGkvIjhTBz9qWleOP2Svpsj%2FPOOG6v1m9hcWB7iIljcWSoFc4SV6WlYeV8iRb%2BqdwQ43oil9LVPfJfScTJyKunEFaKcbvHuiT3NP5978wqyWacdKH0QDCBlNQXh01nv%2F6uL7R2e%2FIHWn%2FiK7tuywqqscahykkmniJLvXCoRbBmZUZ6bfExGf0O1nxoSQTc6nUj3Ltv7mPeAK7Wpoi8lUy50HgNGRALysEqZByBWwvFJMSQ3SMj0Op4v8GxSplXJU2xiP%2FbnaFZDwjd0vGogu%2BPG4NrnGZeLzKBeX%2FOrBdgXWzBs42syvUiY%2FFPYB6KJrR7zUF%2FqLkGwow19%2FA%2Bi%2F4uZfKkw29ePvQY6pgFXr3Use7FuqYqWxQxpCuKZYNn0oiXYegiP1s6ljZganfXpGaaL6PyZ%2BDB%2B1IfzpeY0sdbRarWkATUMWM%2FHOENa2tiAdUQ9R%2F4IpkzMrYflr3NTgVXW5S2a1EcySIb%2Fh9lJkkur%2FmJ8c16b7WjkZDwOxmZvDaNFqONDUNE8ttMsw3OcpY8WQU9ST4t12GtujYsxsUldmelXgDTEv9bOrvaim09J9BDL&X-Amz-Signature=bccccddcc42c674632930cd591ff3b225275fe3ee20110d17f07137c7917dd1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI4VWK7V%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIHiIgo2TkO4CQb4BHX9N9NgPqGaE0sCk%2FHwW4C7ThP0wAiBE0V13aK4wvvFy7LV7Lp%2Bi6g36IG3sCFncBv7MmjzPqir%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIM6OMmZWvTSHl2I%2BCYKtwDBsxTbnaeJ%2BHX1lMinhyBNQ3FPIFrYwxL5sDoeSGh2SLfumHL6oEnNhpPw7kcM88kD1ndtPDFqdOvRJ%2F3vW0cJ48r3VlmZB7IoKxFom%2Flymid9AHz%2FnJuiJFChqpmHNjwy2nswcVwmQqp%2BsFgM6yHXPXchIdpJzWLFetfNCIfSIaReVpEnwyywIpax65X%2F98g5OlngkODGT0gD07kp1PQM6kX1PMc%2FJYVgzLy5UjRrF71g9Ihq81x0aHtBcEdGbj9Cxq%2B4JG9GjtG9B%2BAvzDAlUSl18uEkFrJlYGkvIjhTBz9qWleOP2Svpsj%2FPOOG6v1m9hcWB7iIljcWSoFc4SV6WlYeV8iRb%2BqdwQ43oil9LVPfJfScTJyKunEFaKcbvHuiT3NP5978wqyWacdKH0QDCBlNQXh01nv%2F6uL7R2e%2FIHWn%2FiK7tuywqqscahykkmniJLvXCoRbBmZUZ6bfExGf0O1nxoSQTc6nUj3Ltv7mPeAK7Wpoi8lUy50HgNGRALysEqZByBWwvFJMSQ3SMj0Op4v8GxSplXJU2xiP%2FbnaFZDwjd0vGogu%2BPG4NrnGZeLzKBeX%2FOrBdgXWzBs42syvUiY%2FFPYB6KJrR7zUF%2FqLkGwow19%2FA%2Bi%2F4uZfKkw29ePvQY6pgFXr3Use7FuqYqWxQxpCuKZYNn0oiXYegiP1s6ljZganfXpGaaL6PyZ%2BDB%2B1IfzpeY0sdbRarWkATUMWM%2FHOENa2tiAdUQ9R%2F4IpkzMrYflr3NTgVXW5S2a1EcySIb%2Fh9lJkkur%2FmJ8c16b7WjkZDwOxmZvDaNFqONDUNE8ttMsw3OcpY8WQU9ST4t12GtujYsxsUldmelXgDTEv9bOrvaim09J9BDL&X-Amz-Signature=f66777302dace495b09c2a1d005cad9b7118849d8b83b0a967c65ccd9e8459ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
