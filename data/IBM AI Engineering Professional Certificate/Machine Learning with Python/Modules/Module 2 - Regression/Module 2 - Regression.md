

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGVCN7CU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCFISjHaRADZ5I84qSvzQKbF1tjU6J6KSC7bbIWXemShAIgBBPeeOMOEpcdHWBrSuQIRZbBiLgKMOkWilOh1qtTNq0q%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ2TwsGlAlpN%2B9Lz4ircA3U3D%2FZ4eNPjfBxnCeqZhpvHgSqmEMfSLd0wl93nkdW%2BM4OGo3WlCwmirDkJ8crtS2qzecEOreVsmGnkV8KdUw3TgKJH4v8j%2FIoBi0cp%2BuvUdaFOP%2Fgk26AUt%2B00%2BfMi%2F6nLQkOubtSO2rZTrgsQHt1cuVXfh0RwtjtE7iv5aji%2BTEqyeP0%2BOCDLqBCQ7aqxsQkhd1zcXqXn5tVkTR2s02rvbQXt5mU1OX0dhmgw9kT8yQtVmEQNF1TZ0Pf9K1M%2FHg2w2T3lf63qyxyIw8%2BiN5AODmBKrIFXSRpuUZ7M6AuLwR3TZlPS286paeBWK%2FDhOiGP4Hh3%2FQ4kQM4M2DwHW5x0jdtKtru0OlhX%2BMiGlTREkz5erDQ4zTqVQk7fyFUxZ7p%2FaBWayFgVumqFRLhxNS77yXoypV8Osu1FSou7KWIvQG4Iyw6yQtTi749uQLp8%2FJLRHTxsYBFwMnwP%2FWETveYaqaWV6FcPabgcr4hBYhIZsz05Li8SLVwnb%2BPl2EggZv%2FlBkXSZgDlZ4dsnFQxdyq%2BrT21GuXbqoFr%2BM6rWug2OuiHTNF5WGwnKP%2FtM6iYezxPgUJfIP6%2BQiw0p%2BBktatvPFnECIr1%2Bqn1eSxubwbFUsbIkmEU7Bx98egzMKHelr0GOqUB7ZhLto5v8Qrf34Tn9PprbfBjOGu%2BC%2FmXDbTw9Cz1zNW9HGAqsiJ5eVhVOw8Tm3YBiUJVeri%2B2TSsURnYDPavjqqI4jADo%2FUN5SR6wHFH%2BXFai%2B2NxUBod1hL1eXTBHJy%2F%2FZFMpsTS48DFx3J%2B4OHySvh3PoDZlE%2FZhg6ZmujR0d8aGZx%2BxQ%2FFPrbaOdp%2B0rkJXs6Zau5QfcwS6jKDc7DG3341J7%2F&X-Amz-Signature=c8d97c2d6d142abc8ea828ef7900596d23510074438255c76d86420701caaa4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGVCN7CU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCFISjHaRADZ5I84qSvzQKbF1tjU6J6KSC7bbIWXemShAIgBBPeeOMOEpcdHWBrSuQIRZbBiLgKMOkWilOh1qtTNq0q%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ2TwsGlAlpN%2B9Lz4ircA3U3D%2FZ4eNPjfBxnCeqZhpvHgSqmEMfSLd0wl93nkdW%2BM4OGo3WlCwmirDkJ8crtS2qzecEOreVsmGnkV8KdUw3TgKJH4v8j%2FIoBi0cp%2BuvUdaFOP%2Fgk26AUt%2B00%2BfMi%2F6nLQkOubtSO2rZTrgsQHt1cuVXfh0RwtjtE7iv5aji%2BTEqyeP0%2BOCDLqBCQ7aqxsQkhd1zcXqXn5tVkTR2s02rvbQXt5mU1OX0dhmgw9kT8yQtVmEQNF1TZ0Pf9K1M%2FHg2w2T3lf63qyxyIw8%2BiN5AODmBKrIFXSRpuUZ7M6AuLwR3TZlPS286paeBWK%2FDhOiGP4Hh3%2FQ4kQM4M2DwHW5x0jdtKtru0OlhX%2BMiGlTREkz5erDQ4zTqVQk7fyFUxZ7p%2FaBWayFgVumqFRLhxNS77yXoypV8Osu1FSou7KWIvQG4Iyw6yQtTi749uQLp8%2FJLRHTxsYBFwMnwP%2FWETveYaqaWV6FcPabgcr4hBYhIZsz05Li8SLVwnb%2BPl2EggZv%2FlBkXSZgDlZ4dsnFQxdyq%2BrT21GuXbqoFr%2BM6rWug2OuiHTNF5WGwnKP%2FtM6iYezxPgUJfIP6%2BQiw0p%2BBktatvPFnECIr1%2Bqn1eSxubwbFUsbIkmEU7Bx98egzMKHelr0GOqUB7ZhLto5v8Qrf34Tn9PprbfBjOGu%2BC%2FmXDbTw9Cz1zNW9HGAqsiJ5eVhVOw8Tm3YBiUJVeri%2B2TSsURnYDPavjqqI4jADo%2FUN5SR6wHFH%2BXFai%2B2NxUBod1hL1eXTBHJy%2F%2FZFMpsTS48DFx3J%2B4OHySvh3PoDZlE%2FZhg6ZmujR0d8aGZx%2BxQ%2FFPrbaOdp%2B0rkJXs6Zau5QfcwS6jKDc7DG3341J7%2F&X-Amz-Signature=0ae59326d3a27e809e675ab610583a02eb908e43ac6a4de00fc065106ecba5ee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGVCN7CU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCFISjHaRADZ5I84qSvzQKbF1tjU6J6KSC7bbIWXemShAIgBBPeeOMOEpcdHWBrSuQIRZbBiLgKMOkWilOh1qtTNq0q%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ2TwsGlAlpN%2B9Lz4ircA3U3D%2FZ4eNPjfBxnCeqZhpvHgSqmEMfSLd0wl93nkdW%2BM4OGo3WlCwmirDkJ8crtS2qzecEOreVsmGnkV8KdUw3TgKJH4v8j%2FIoBi0cp%2BuvUdaFOP%2Fgk26AUt%2B00%2BfMi%2F6nLQkOubtSO2rZTrgsQHt1cuVXfh0RwtjtE7iv5aji%2BTEqyeP0%2BOCDLqBCQ7aqxsQkhd1zcXqXn5tVkTR2s02rvbQXt5mU1OX0dhmgw9kT8yQtVmEQNF1TZ0Pf9K1M%2FHg2w2T3lf63qyxyIw8%2BiN5AODmBKrIFXSRpuUZ7M6AuLwR3TZlPS286paeBWK%2FDhOiGP4Hh3%2FQ4kQM4M2DwHW5x0jdtKtru0OlhX%2BMiGlTREkz5erDQ4zTqVQk7fyFUxZ7p%2FaBWayFgVumqFRLhxNS77yXoypV8Osu1FSou7KWIvQG4Iyw6yQtTi749uQLp8%2FJLRHTxsYBFwMnwP%2FWETveYaqaWV6FcPabgcr4hBYhIZsz05Li8SLVwnb%2BPl2EggZv%2FlBkXSZgDlZ4dsnFQxdyq%2BrT21GuXbqoFr%2BM6rWug2OuiHTNF5WGwnKP%2FtM6iYezxPgUJfIP6%2BQiw0p%2BBktatvPFnECIr1%2Bqn1eSxubwbFUsbIkmEU7Bx98egzMKHelr0GOqUB7ZhLto5v8Qrf34Tn9PprbfBjOGu%2BC%2FmXDbTw9Cz1zNW9HGAqsiJ5eVhVOw8Tm3YBiUJVeri%2B2TSsURnYDPavjqqI4jADo%2FUN5SR6wHFH%2BXFai%2B2NxUBod1hL1eXTBHJy%2F%2FZFMpsTS48DFx3J%2B4OHySvh3PoDZlE%2FZhg6ZmujR0d8aGZx%2BxQ%2FFPrbaOdp%2B0rkJXs6Zau5QfcwS6jKDc7DG3341J7%2F&X-Amz-Signature=078d8fce1a1302e13b3f56043e773b5f92458c53a4d83ff50e3b86dee90838df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGVCN7CU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCFISjHaRADZ5I84qSvzQKbF1tjU6J6KSC7bbIWXemShAIgBBPeeOMOEpcdHWBrSuQIRZbBiLgKMOkWilOh1qtTNq0q%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ2TwsGlAlpN%2B9Lz4ircA3U3D%2FZ4eNPjfBxnCeqZhpvHgSqmEMfSLd0wl93nkdW%2BM4OGo3WlCwmirDkJ8crtS2qzecEOreVsmGnkV8KdUw3TgKJH4v8j%2FIoBi0cp%2BuvUdaFOP%2Fgk26AUt%2B00%2BfMi%2F6nLQkOubtSO2rZTrgsQHt1cuVXfh0RwtjtE7iv5aji%2BTEqyeP0%2BOCDLqBCQ7aqxsQkhd1zcXqXn5tVkTR2s02rvbQXt5mU1OX0dhmgw9kT8yQtVmEQNF1TZ0Pf9K1M%2FHg2w2T3lf63qyxyIw8%2BiN5AODmBKrIFXSRpuUZ7M6AuLwR3TZlPS286paeBWK%2FDhOiGP4Hh3%2FQ4kQM4M2DwHW5x0jdtKtru0OlhX%2BMiGlTREkz5erDQ4zTqVQk7fyFUxZ7p%2FaBWayFgVumqFRLhxNS77yXoypV8Osu1FSou7KWIvQG4Iyw6yQtTi749uQLp8%2FJLRHTxsYBFwMnwP%2FWETveYaqaWV6FcPabgcr4hBYhIZsz05Li8SLVwnb%2BPl2EggZv%2FlBkXSZgDlZ4dsnFQxdyq%2BrT21GuXbqoFr%2BM6rWug2OuiHTNF5WGwnKP%2FtM6iYezxPgUJfIP6%2BQiw0p%2BBktatvPFnECIr1%2Bqn1eSxubwbFUsbIkmEU7Bx98egzMKHelr0GOqUB7ZhLto5v8Qrf34Tn9PprbfBjOGu%2BC%2FmXDbTw9Cz1zNW9HGAqsiJ5eVhVOw8Tm3YBiUJVeri%2B2TSsURnYDPavjqqI4jADo%2FUN5SR6wHFH%2BXFai%2B2NxUBod1hL1eXTBHJy%2F%2FZFMpsTS48DFx3J%2B4OHySvh3PoDZlE%2FZhg6ZmujR0d8aGZx%2BxQ%2FFPrbaOdp%2B0rkJXs6Zau5QfcwS6jKDc7DG3341J7%2F&X-Amz-Signature=00d3fbeed30d0e0abe7877bd60e1f28bcdba48fc56d6b5ebd77725670c6364d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGVCN7CU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCFISjHaRADZ5I84qSvzQKbF1tjU6J6KSC7bbIWXemShAIgBBPeeOMOEpcdHWBrSuQIRZbBiLgKMOkWilOh1qtTNq0q%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ2TwsGlAlpN%2B9Lz4ircA3U3D%2FZ4eNPjfBxnCeqZhpvHgSqmEMfSLd0wl93nkdW%2BM4OGo3WlCwmirDkJ8crtS2qzecEOreVsmGnkV8KdUw3TgKJH4v8j%2FIoBi0cp%2BuvUdaFOP%2Fgk26AUt%2B00%2BfMi%2F6nLQkOubtSO2rZTrgsQHt1cuVXfh0RwtjtE7iv5aji%2BTEqyeP0%2BOCDLqBCQ7aqxsQkhd1zcXqXn5tVkTR2s02rvbQXt5mU1OX0dhmgw9kT8yQtVmEQNF1TZ0Pf9K1M%2FHg2w2T3lf63qyxyIw8%2BiN5AODmBKrIFXSRpuUZ7M6AuLwR3TZlPS286paeBWK%2FDhOiGP4Hh3%2FQ4kQM4M2DwHW5x0jdtKtru0OlhX%2BMiGlTREkz5erDQ4zTqVQk7fyFUxZ7p%2FaBWayFgVumqFRLhxNS77yXoypV8Osu1FSou7KWIvQG4Iyw6yQtTi749uQLp8%2FJLRHTxsYBFwMnwP%2FWETveYaqaWV6FcPabgcr4hBYhIZsz05Li8SLVwnb%2BPl2EggZv%2FlBkXSZgDlZ4dsnFQxdyq%2BrT21GuXbqoFr%2BM6rWug2OuiHTNF5WGwnKP%2FtM6iYezxPgUJfIP6%2BQiw0p%2BBktatvPFnECIr1%2Bqn1eSxubwbFUsbIkmEU7Bx98egzMKHelr0GOqUB7ZhLto5v8Qrf34Tn9PprbfBjOGu%2BC%2FmXDbTw9Cz1zNW9HGAqsiJ5eVhVOw8Tm3YBiUJVeri%2B2TSsURnYDPavjqqI4jADo%2FUN5SR6wHFH%2BXFai%2B2NxUBod1hL1eXTBHJy%2F%2FZFMpsTS48DFx3J%2B4OHySvh3PoDZlE%2FZhg6ZmujR0d8aGZx%2BxQ%2FFPrbaOdp%2B0rkJXs6Zau5QfcwS6jKDc7DG3341J7%2F&X-Amz-Signature=80d746f56e83c90e226cf9014482ae133c35dae2b2a89b5857162fc6d8a4f3e5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGVCN7CU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCFISjHaRADZ5I84qSvzQKbF1tjU6J6KSC7bbIWXemShAIgBBPeeOMOEpcdHWBrSuQIRZbBiLgKMOkWilOh1qtTNq0q%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ2TwsGlAlpN%2B9Lz4ircA3U3D%2FZ4eNPjfBxnCeqZhpvHgSqmEMfSLd0wl93nkdW%2BM4OGo3WlCwmirDkJ8crtS2qzecEOreVsmGnkV8KdUw3TgKJH4v8j%2FIoBi0cp%2BuvUdaFOP%2Fgk26AUt%2B00%2BfMi%2F6nLQkOubtSO2rZTrgsQHt1cuVXfh0RwtjtE7iv5aji%2BTEqyeP0%2BOCDLqBCQ7aqxsQkhd1zcXqXn5tVkTR2s02rvbQXt5mU1OX0dhmgw9kT8yQtVmEQNF1TZ0Pf9K1M%2FHg2w2T3lf63qyxyIw8%2BiN5AODmBKrIFXSRpuUZ7M6AuLwR3TZlPS286paeBWK%2FDhOiGP4Hh3%2FQ4kQM4M2DwHW5x0jdtKtru0OlhX%2BMiGlTREkz5erDQ4zTqVQk7fyFUxZ7p%2FaBWayFgVumqFRLhxNS77yXoypV8Osu1FSou7KWIvQG4Iyw6yQtTi749uQLp8%2FJLRHTxsYBFwMnwP%2FWETveYaqaWV6FcPabgcr4hBYhIZsz05Li8SLVwnb%2BPl2EggZv%2FlBkXSZgDlZ4dsnFQxdyq%2BrT21GuXbqoFr%2BM6rWug2OuiHTNF5WGwnKP%2FtM6iYezxPgUJfIP6%2BQiw0p%2BBktatvPFnECIr1%2Bqn1eSxubwbFUsbIkmEU7Bx98egzMKHelr0GOqUB7ZhLto5v8Qrf34Tn9PprbfBjOGu%2BC%2FmXDbTw9Cz1zNW9HGAqsiJ5eVhVOw8Tm3YBiUJVeri%2B2TSsURnYDPavjqqI4jADo%2FUN5SR6wHFH%2BXFai%2B2NxUBod1hL1eXTBHJy%2F%2FZFMpsTS48DFx3J%2B4OHySvh3PoDZlE%2FZhg6ZmujR0d8aGZx%2BxQ%2FFPrbaOdp%2B0rkJXs6Zau5QfcwS6jKDc7DG3341J7%2F&X-Amz-Signature=bbfa44fc6abfc9ffd0f926bbc7b3a6546420cfcf1bdf746b0d88b17e66f59d70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGVCN7CU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCFISjHaRADZ5I84qSvzQKbF1tjU6J6KSC7bbIWXemShAIgBBPeeOMOEpcdHWBrSuQIRZbBiLgKMOkWilOh1qtTNq0q%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ2TwsGlAlpN%2B9Lz4ircA3U3D%2FZ4eNPjfBxnCeqZhpvHgSqmEMfSLd0wl93nkdW%2BM4OGo3WlCwmirDkJ8crtS2qzecEOreVsmGnkV8KdUw3TgKJH4v8j%2FIoBi0cp%2BuvUdaFOP%2Fgk26AUt%2B00%2BfMi%2F6nLQkOubtSO2rZTrgsQHt1cuVXfh0RwtjtE7iv5aji%2BTEqyeP0%2BOCDLqBCQ7aqxsQkhd1zcXqXn5tVkTR2s02rvbQXt5mU1OX0dhmgw9kT8yQtVmEQNF1TZ0Pf9K1M%2FHg2w2T3lf63qyxyIw8%2BiN5AODmBKrIFXSRpuUZ7M6AuLwR3TZlPS286paeBWK%2FDhOiGP4Hh3%2FQ4kQM4M2DwHW5x0jdtKtru0OlhX%2BMiGlTREkz5erDQ4zTqVQk7fyFUxZ7p%2FaBWayFgVumqFRLhxNS77yXoypV8Osu1FSou7KWIvQG4Iyw6yQtTi749uQLp8%2FJLRHTxsYBFwMnwP%2FWETveYaqaWV6FcPabgcr4hBYhIZsz05Li8SLVwnb%2BPl2EggZv%2FlBkXSZgDlZ4dsnFQxdyq%2BrT21GuXbqoFr%2BM6rWug2OuiHTNF5WGwnKP%2FtM6iYezxPgUJfIP6%2BQiw0p%2BBktatvPFnECIr1%2Bqn1eSxubwbFUsbIkmEU7Bx98egzMKHelr0GOqUB7ZhLto5v8Qrf34Tn9PprbfBjOGu%2BC%2FmXDbTw9Cz1zNW9HGAqsiJ5eVhVOw8Tm3YBiUJVeri%2B2TSsURnYDPavjqqI4jADo%2FUN5SR6wHFH%2BXFai%2B2NxUBod1hL1eXTBHJy%2F%2FZFMpsTS48DFx3J%2B4OHySvh3PoDZlE%2FZhg6ZmujR0d8aGZx%2BxQ%2FFPrbaOdp%2B0rkJXs6Zau5QfcwS6jKDc7DG3341J7%2F&X-Amz-Signature=c32bd209dcf323f9125a41a66c0a6135b13085d47797f31b83535400ce06f936&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGVCN7CU%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQCFISjHaRADZ5I84qSvzQKbF1tjU6J6KSC7bbIWXemShAIgBBPeeOMOEpcdHWBrSuQIRZbBiLgKMOkWilOh1qtTNq0q%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDJ2TwsGlAlpN%2B9Lz4ircA3U3D%2FZ4eNPjfBxnCeqZhpvHgSqmEMfSLd0wl93nkdW%2BM4OGo3WlCwmirDkJ8crtS2qzecEOreVsmGnkV8KdUw3TgKJH4v8j%2FIoBi0cp%2BuvUdaFOP%2Fgk26AUt%2B00%2BfMi%2F6nLQkOubtSO2rZTrgsQHt1cuVXfh0RwtjtE7iv5aji%2BTEqyeP0%2BOCDLqBCQ7aqxsQkhd1zcXqXn5tVkTR2s02rvbQXt5mU1OX0dhmgw9kT8yQtVmEQNF1TZ0Pf9K1M%2FHg2w2T3lf63qyxyIw8%2BiN5AODmBKrIFXSRpuUZ7M6AuLwR3TZlPS286paeBWK%2FDhOiGP4Hh3%2FQ4kQM4M2DwHW5x0jdtKtru0OlhX%2BMiGlTREkz5erDQ4zTqVQk7fyFUxZ7p%2FaBWayFgVumqFRLhxNS77yXoypV8Osu1FSou7KWIvQG4Iyw6yQtTi749uQLp8%2FJLRHTxsYBFwMnwP%2FWETveYaqaWV6FcPabgcr4hBYhIZsz05Li8SLVwnb%2BPl2EggZv%2FlBkXSZgDlZ4dsnFQxdyq%2BrT21GuXbqoFr%2BM6rWug2OuiHTNF5WGwnKP%2FtM6iYezxPgUJfIP6%2BQiw0p%2BBktatvPFnECIr1%2Bqn1eSxubwbFUsbIkmEU7Bx98egzMKHelr0GOqUB7ZhLto5v8Qrf34Tn9PprbfBjOGu%2BC%2FmXDbTw9Cz1zNW9HGAqsiJ5eVhVOw8Tm3YBiUJVeri%2B2TSsURnYDPavjqqI4jADo%2FUN5SR6wHFH%2BXFai%2B2NxUBod1hL1eXTBHJy%2F%2FZFMpsTS48DFx3J%2B4OHySvh3PoDZlE%2FZhg6ZmujR0d8aGZx%2BxQ%2FFPrbaOdp%2B0rkJXs6Zau5QfcwS6jKDc7DG3341J7%2F&X-Amz-Signature=79fcc9a219f9d349033904c71e86e6c8860ef6f554756729729f025955a8c493&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQI272CD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJGMEQCIHHs9Ypp98N%2Bcj862bMvXEiz3POadIOjloFZwokasx9jAiBh3YmHyqO9G6jw%2FmkK8ofQh2IwPPHC8OGkMJ7fne2GKCr%2FAwhwEAAaDDYzNzQyMzE4MzgwNSIMFeSRpxhzZ%2Bov5AeGKtwDk1USW3E155hT5U4yK5hArfuCk6FHo9Znl0QtIp7Ap3srBXUXocjtU219DIYoXHVWylVR2BWdxP2x2IGk8oMLQojNntsgF7a5fePV3LPbpG3o4M%2BkkWxtX7VFbAl1fH9mP%2F6mFy%2B75b9TIUnalNlDamU9oVNd4EsiFmnv4gDmD4HXfGEkb6nq7CJJCCiiLmHCDwOGdZw5rUXCyU4Kw6NIZQPwKkccEiJe%2FbaC%2FGdPkgEGJCGHzMVRDK%2FvdRgbgDFonRKbOHPDrIpbCoHeLkRdz6t%2Bdf37fR48LTJ%2FDGQGnzji1ys3dzJ994udFy1Z3N9iYF6orcynrdfUgUq0nWadM7b6pkJo01HfN6QgzlmG264YoTpG7cHc%2FeeytZHAZNsgZeCANcWVMCobwnQVWU783Z4vDm40IvIgFG6gSBbtvnyTi0tlYgrqwIXZ%2BvhHm3xkpds1PZJh0kVMsRLCTWHCum4Xa7W87ZAJ7tLS5ns2L%2FIOjq1Ll43poEqZaDyfQpui75H%2FmrKCqsKvPRLxGCb6oTiPEpEBC8ahmjbl15HSPHurVv%2FKFHhoTeVLMejF0nLeWSr1wBrZi83eABP0DlM%2FnM2%2FVhaPfHGlNU8hsbZk1AnKKARzwZOYFvixBDAw3tyWvQY6pgFwUyVpzbDJJ8181yncXKdLRX0xZzWQB5P%2F7N%2Bk6y2IOMmhyotL%2BFaSmTBbF3LkUcm2fZzyy1zgGBSP5nxHFfrinWfIsOQfiyFHJS4bQfx%2FYoYuPPgM4Xy29Em%2BHI%2BFAeQgVown2QnX9QFSf8uXX1PSoOCbuciaDZcPFHWVtvPFg6tJQ0ghpEwKbGKmA9PpwTN16rN4tsdMtZAy0iDXEifZKxPHnOBF&X-Amz-Signature=c0251f33439158f1ed3ccdae605e658c1ac6515aac56075136f874c078d9023a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PS4SM2C%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJHMEUCIQDtal04pj3YKA%2Bb0QFYPBZhDAWGzAxa2rnGkV8ycOmBoQIgdqDynLa4sOgw%2FE4jeW30AWk%2FP9dmN27nmaeOX0Nwi3sq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDP4vfQXcBNcSXPeOeSrcA0aWje3Xw46j03aVpW2SJ0PIB5c4BSI8cphu4tm%2FDQHZ5zBJVeTsJKLA0eYGaqoyIgLJR9Jck441zQ9S0EH1MdA2shw9%2FrjMWTpHIoT9ZMYDEbiM84gKBskbfpYkkhf%2FezKCe40Zj1hy7wL9cfQlsLvuJ2Ga3Pky056QdhEwp%2FXjizN3pb0DWHWcJES5dzKdOFHF9K%2FOP%2Fvw3wMOXrGfXtZ%2FVdUVWRHyznTQiuXCAV14zzmsa3sA1PaFzRkp1Ie%2Byo%2FZmT4VG0F%2B%2BQZ0sQcw%2BQRu81lVvR4UvvBitpE1EVlDd0qk32DtjAuJVp96N%2F34oIiJKWBIXawh1Ylm5JRTLQP%2FG7RmIT4cfdo7uiPI7aG4lQj%2BelfpdiRoa6hUnUxev4j4BQoG1KgC5vt6yltkW5WASt7M%2BNYlEqgtQCLDJ9h3g%2F0tLfTq3KacRFCFilAgK8NGuZLiT9Wz2tF1PtVPUyxUvBvvYy%2B4fouwtrhpI83OR4K3Vkzshb9WskF%2FQU1Q1ziqihe1Fd9z7%2FA%2BUJmpa8BDliRshYEg3bm0QTPBgBcmmw4joFjCZi9ZS6a6aDqURQN%2FaZS8aAa0rQ%2BCws0Mu%2FaTSTOCeMuvJdrG%2BSlj6cK6dloKHMaHHxjRbYSOMPbdlr0GOqUBIgEwEHq8%2B1sLuwvtaB1T4cZEh6LBOeNEY0co%2FfGvxUuakhDNeWgGC22IqnPa3b14et3WyRt7jwHrNHfcgxkO%2BGV2yZtIVmE3tx5Uy8YwwSOc%2FOZebP%2B9WoQlQrCb%2F2x88kaI0DRf0rk3xcZMVCV7pYQDS6WUuBtywKRtGDOMRioTCfqdF0U50iiUTOFmYWLT5wHWl%2BhNxSypnJbT2cB0%2BCBwpY4U&X-Amz-Signature=2c3bf5f684de385ebc0d1a4460d3d710bf679de9a89983c0a400da06c1cfcb7d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3VLVMSM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQCE8z%2Fj%2BuC%2FOJf0PZab6XPmy5sdsWsye6mvzfiURCgNtwIhAO7YwCLRjOaNJsFSbtppn5XCQ4UbHmCjwamIicBKnkeDKv8DCHAQABoMNjM3NDIzMTgzODA1Igxu82TzIbriW1BP704q3AMmqJpi8PUObn3gPkt8wLUjglI%2FotxTWVqOn8w5VfP%2Bh07eicNzIo60D9yablvhOGrGoJmB%2F84ixE2TrgaQ26x%2BoHh9WOx0zVR8CjC%2BRezqQSzevG81yrGiej2YtKdEospSmN0GStDUBf4dgXe0xGTPflPLh9q1aWHXUqgQQgq%2Fw%2Bn4mTEkQZdNp47RrgtLhLNRPdvuX7l9pPu8UFNS0DlCW97Fwcdvlya7Qf7CCwUv5dVV%2FmiZN3zC35d8epNvaOFfBnYoEcYUZDjWffcrPVJLBYuc3OJRlPnuTba5O6YrAsybR80iMcNAsbhHb%2BZGRR9dG9W6c%2BSegu1pF9LC5j4eb8ql3iSn7o%2FJoCS%2BzpnTsUuFyl1GwKUwyoQju73FdNxf2aSeJzwfOZ9LY4YWgb9KrGwRcLbiTFM6yn0PnfC3Remj2g4Qmquu9EoGOgv1%2Fq7zRkOybznQYvY8bL%2BdKjs1SdInpmhnfHxgfR1VLJqRXO%2FaVbVZ6DgTVYFM1dD3wcwOAcxQlV7gBN5bA102AIlucG0GgTphuNuBkHY0KOhfXBYhOuRC7jNC25VYsnpv%2FpAO6E1UH%2FprxFd25hSjkQqAhVmoh1%2B4K7A28XXRJZKz99hpLt5f%2BamiE2HJ%2FDDW3Ja9BjqkAdSG5M2Ui%2F624iSmXJNoCO%2BQZkCGm8d4V5%2BPfPlJVa0RAwTcSKDlbxbDsf5ZEQjfDCHQgF0%2FfZxbXR5f%2FJY8iYAlQOuDcRWIlfYu9EsrIfkyD0JGY%2BWfurYQYWFtF0r%2FVbVbcu45bU5Zn5rtYoQoOMMiTYCkhMUQTsRgB7HuXKHrczfeE9x0KB0rrAZ0iX6KF%2Btq%2BMUnDNReGgzCaIpcuzBYdAMo&X-Amz-Signature=4007c569219e80963e2feeb4a61e7afc4a542311f8098cf14ac63b674b784bfa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3VLVMSM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T071346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFcaCXVzLXdlc3QtMiJIMEYCIQCE8z%2Fj%2BuC%2FOJf0PZab6XPmy5sdsWsye6mvzfiURCgNtwIhAO7YwCLRjOaNJsFSbtppn5XCQ4UbHmCjwamIicBKnkeDKv8DCHAQABoMNjM3NDIzMTgzODA1Igxu82TzIbriW1BP704q3AMmqJpi8PUObn3gPkt8wLUjglI%2FotxTWVqOn8w5VfP%2Bh07eicNzIo60D9yablvhOGrGoJmB%2F84ixE2TrgaQ26x%2BoHh9WOx0zVR8CjC%2BRezqQSzevG81yrGiej2YtKdEospSmN0GStDUBf4dgXe0xGTPflPLh9q1aWHXUqgQQgq%2Fw%2Bn4mTEkQZdNp47RrgtLhLNRPdvuX7l9pPu8UFNS0DlCW97Fwcdvlya7Qf7CCwUv5dVV%2FmiZN3zC35d8epNvaOFfBnYoEcYUZDjWffcrPVJLBYuc3OJRlPnuTba5O6YrAsybR80iMcNAsbhHb%2BZGRR9dG9W6c%2BSegu1pF9LC5j4eb8ql3iSn7o%2FJoCS%2BzpnTsUuFyl1GwKUwyoQju73FdNxf2aSeJzwfOZ9LY4YWgb9KrGwRcLbiTFM6yn0PnfC3Remj2g4Qmquu9EoGOgv1%2Fq7zRkOybznQYvY8bL%2BdKjs1SdInpmhnfHxgfR1VLJqRXO%2FaVbVZ6DgTVYFM1dD3wcwOAcxQlV7gBN5bA102AIlucG0GgTphuNuBkHY0KOhfXBYhOuRC7jNC25VYsnpv%2FpAO6E1UH%2FprxFd25hSjkQqAhVmoh1%2B4K7A28XXRJZKz99hpLt5f%2BamiE2HJ%2FDDW3Ja9BjqkAdSG5M2Ui%2F624iSmXJNoCO%2BQZkCGm8d4V5%2BPfPlJVa0RAwTcSKDlbxbDsf5ZEQjfDCHQgF0%2FfZxbXR5f%2FJY8iYAlQOuDcRWIlfYu9EsrIfkyD0JGY%2BWfurYQYWFtF0r%2FVbVbcu45bU5Zn5rtYoQoOMMiTYCkhMUQTsRgB7HuXKHrczfeE9x0KB0rrAZ0iX6KF%2Btq%2BMUnDNReGgzCaIpcuzBYdAMo&X-Amz-Signature=b619a0508c944d36ef0c4e8ffc88fd7e339f4b4866310279ca30735156d3fee3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
