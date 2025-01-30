

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECVSXUO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAiUVWKbcT3fMCIqCgef1DWPOT59%2FO89s3a%2Bj7e1EBN6AiEAjjVsSk%2F9STktdgBp%2FWXgmpGCDe5JtuaoQzL5QHGlbjIqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjZ0EyKM0Ge7MBIXyrcA3GUCAzECWDF6kMXmuntVTG9URj%2FjMGiKx8Vsxir6zafJQgW%2F3stwxhkE3S2MBKV4u%2Fr6U0CHfaovOPJRHvkmfsdlkr2hdG3vQlVHdsVDKabBuHZuM5pMWtEuNIG0k2Dr1FfmVueHjmztExX75NFhE33by2JpqGwA4q1hSu4U%2BbNogiSlEl8RtRq4gS2eq%2Bl8b2qxySDOZxYO33sgJy%2FCwkTDbJr7CUhsitlnmVIW9FOTRk%2FwicOaoaxwneENSir7bA57LV09a3%2BJW%2BtutGwDQSkNr7uJisclz2RgP1thx2QDDLA6hrYJ3znlnKSAFQtHulFu5RHvsaRJnAHlxWK4KkDvmQRKxExiu541CSeoT%2FLItq3CCIaAh92b%2FaZwIpUXFOqDGueql4Rf3bX0vkF4y2u2DZ566hTxAzulcMsuu5N0RctsGcI29zkhpEmYvod%2BXxo5wpfjo9Dv%2BLPC0OoOvtqHt1sb0Fnw%2Bauq8BDCK%2B1%2FtGIqfH3AWNaIAD75ORRGBSrM7ONJFQ%2Fhn%2FtoA%2FVNxGB3hwsIbSNEuAcCWCw%2BEAMSIUY4ZPj2cUxK4bJBFT5NqAwI6dM07EkVg7VuZbXWHE2XxmqLxulUtsW7XvskNhJDOCl9bWYRi4Hg1BhMKiy67wGOqUBHRTnXaBm0rmG2j72ftYdT1rnt263BHizJT8ZqJ%2B%2FZkC7f9w5GhdRFvx4rxew7tZDgTVmccJiOqIv0Rdg%2BpozeFYvRe6EK%2BhKBa6GtxBJ8FgN3gzTq8%2BAFhS9r5zgBDe3Wp6qUW5nD0pQNhLFniNz%2BVgXbbeKgrseVtckn7iYfQdGnrigMZScHIhTlgPXIbhS%2BCmvoDYZnNhXz4RIxrV6J7GV0LvR&X-Amz-Signature=7b0dda3a2e91dcb61fef91b15ebfe260f700463cd65dbbc5797e19e7d62cbfa3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECVSXUO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAiUVWKbcT3fMCIqCgef1DWPOT59%2FO89s3a%2Bj7e1EBN6AiEAjjVsSk%2F9STktdgBp%2FWXgmpGCDe5JtuaoQzL5QHGlbjIqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjZ0EyKM0Ge7MBIXyrcA3GUCAzECWDF6kMXmuntVTG9URj%2FjMGiKx8Vsxir6zafJQgW%2F3stwxhkE3S2MBKV4u%2Fr6U0CHfaovOPJRHvkmfsdlkr2hdG3vQlVHdsVDKabBuHZuM5pMWtEuNIG0k2Dr1FfmVueHjmztExX75NFhE33by2JpqGwA4q1hSu4U%2BbNogiSlEl8RtRq4gS2eq%2Bl8b2qxySDOZxYO33sgJy%2FCwkTDbJr7CUhsitlnmVIW9FOTRk%2FwicOaoaxwneENSir7bA57LV09a3%2BJW%2BtutGwDQSkNr7uJisclz2RgP1thx2QDDLA6hrYJ3znlnKSAFQtHulFu5RHvsaRJnAHlxWK4KkDvmQRKxExiu541CSeoT%2FLItq3CCIaAh92b%2FaZwIpUXFOqDGueql4Rf3bX0vkF4y2u2DZ566hTxAzulcMsuu5N0RctsGcI29zkhpEmYvod%2BXxo5wpfjo9Dv%2BLPC0OoOvtqHt1sb0Fnw%2Bauq8BDCK%2B1%2FtGIqfH3AWNaIAD75ORRGBSrM7ONJFQ%2Fhn%2FtoA%2FVNxGB3hwsIbSNEuAcCWCw%2BEAMSIUY4ZPj2cUxK4bJBFT5NqAwI6dM07EkVg7VuZbXWHE2XxmqLxulUtsW7XvskNhJDOCl9bWYRi4Hg1BhMKiy67wGOqUBHRTnXaBm0rmG2j72ftYdT1rnt263BHizJT8ZqJ%2B%2FZkC7f9w5GhdRFvx4rxew7tZDgTVmccJiOqIv0Rdg%2BpozeFYvRe6EK%2BhKBa6GtxBJ8FgN3gzTq8%2BAFhS9r5zgBDe3Wp6qUW5nD0pQNhLFniNz%2BVgXbbeKgrseVtckn7iYfQdGnrigMZScHIhTlgPXIbhS%2BCmvoDYZnNhXz4RIxrV6J7GV0LvR&X-Amz-Signature=7729fa37ae6326d57b6c2e390a08ea8993dff856db1eefc15090c50b0a0f9245&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECVSXUO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAiUVWKbcT3fMCIqCgef1DWPOT59%2FO89s3a%2Bj7e1EBN6AiEAjjVsSk%2F9STktdgBp%2FWXgmpGCDe5JtuaoQzL5QHGlbjIqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjZ0EyKM0Ge7MBIXyrcA3GUCAzECWDF6kMXmuntVTG9URj%2FjMGiKx8Vsxir6zafJQgW%2F3stwxhkE3S2MBKV4u%2Fr6U0CHfaovOPJRHvkmfsdlkr2hdG3vQlVHdsVDKabBuHZuM5pMWtEuNIG0k2Dr1FfmVueHjmztExX75NFhE33by2JpqGwA4q1hSu4U%2BbNogiSlEl8RtRq4gS2eq%2Bl8b2qxySDOZxYO33sgJy%2FCwkTDbJr7CUhsitlnmVIW9FOTRk%2FwicOaoaxwneENSir7bA57LV09a3%2BJW%2BtutGwDQSkNr7uJisclz2RgP1thx2QDDLA6hrYJ3znlnKSAFQtHulFu5RHvsaRJnAHlxWK4KkDvmQRKxExiu541CSeoT%2FLItq3CCIaAh92b%2FaZwIpUXFOqDGueql4Rf3bX0vkF4y2u2DZ566hTxAzulcMsuu5N0RctsGcI29zkhpEmYvod%2BXxo5wpfjo9Dv%2BLPC0OoOvtqHt1sb0Fnw%2Bauq8BDCK%2B1%2FtGIqfH3AWNaIAD75ORRGBSrM7ONJFQ%2Fhn%2FtoA%2FVNxGB3hwsIbSNEuAcCWCw%2BEAMSIUY4ZPj2cUxK4bJBFT5NqAwI6dM07EkVg7VuZbXWHE2XxmqLxulUtsW7XvskNhJDOCl9bWYRi4Hg1BhMKiy67wGOqUBHRTnXaBm0rmG2j72ftYdT1rnt263BHizJT8ZqJ%2B%2FZkC7f9w5GhdRFvx4rxew7tZDgTVmccJiOqIv0Rdg%2BpozeFYvRe6EK%2BhKBa6GtxBJ8FgN3gzTq8%2BAFhS9r5zgBDe3Wp6qUW5nD0pQNhLFniNz%2BVgXbbeKgrseVtckn7iYfQdGnrigMZScHIhTlgPXIbhS%2BCmvoDYZnNhXz4RIxrV6J7GV0LvR&X-Amz-Signature=abbf32e992e708b7453ec3418f68931221a10615d185cef37362e1bab1c7c3d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECVSXUO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAiUVWKbcT3fMCIqCgef1DWPOT59%2FO89s3a%2Bj7e1EBN6AiEAjjVsSk%2F9STktdgBp%2FWXgmpGCDe5JtuaoQzL5QHGlbjIqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjZ0EyKM0Ge7MBIXyrcA3GUCAzECWDF6kMXmuntVTG9URj%2FjMGiKx8Vsxir6zafJQgW%2F3stwxhkE3S2MBKV4u%2Fr6U0CHfaovOPJRHvkmfsdlkr2hdG3vQlVHdsVDKabBuHZuM5pMWtEuNIG0k2Dr1FfmVueHjmztExX75NFhE33by2JpqGwA4q1hSu4U%2BbNogiSlEl8RtRq4gS2eq%2Bl8b2qxySDOZxYO33sgJy%2FCwkTDbJr7CUhsitlnmVIW9FOTRk%2FwicOaoaxwneENSir7bA57LV09a3%2BJW%2BtutGwDQSkNr7uJisclz2RgP1thx2QDDLA6hrYJ3znlnKSAFQtHulFu5RHvsaRJnAHlxWK4KkDvmQRKxExiu541CSeoT%2FLItq3CCIaAh92b%2FaZwIpUXFOqDGueql4Rf3bX0vkF4y2u2DZ566hTxAzulcMsuu5N0RctsGcI29zkhpEmYvod%2BXxo5wpfjo9Dv%2BLPC0OoOvtqHt1sb0Fnw%2Bauq8BDCK%2B1%2FtGIqfH3AWNaIAD75ORRGBSrM7ONJFQ%2Fhn%2FtoA%2FVNxGB3hwsIbSNEuAcCWCw%2BEAMSIUY4ZPj2cUxK4bJBFT5NqAwI6dM07EkVg7VuZbXWHE2XxmqLxulUtsW7XvskNhJDOCl9bWYRi4Hg1BhMKiy67wGOqUBHRTnXaBm0rmG2j72ftYdT1rnt263BHizJT8ZqJ%2B%2FZkC7f9w5GhdRFvx4rxew7tZDgTVmccJiOqIv0Rdg%2BpozeFYvRe6EK%2BhKBa6GtxBJ8FgN3gzTq8%2BAFhS9r5zgBDe3Wp6qUW5nD0pQNhLFniNz%2BVgXbbeKgrseVtckn7iYfQdGnrigMZScHIhTlgPXIbhS%2BCmvoDYZnNhXz4RIxrV6J7GV0LvR&X-Amz-Signature=b1b9f936323104a94e5e47667d80056598c1e9cf4edc9d7ac6e311a8cdd3c31f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECVSXUO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAiUVWKbcT3fMCIqCgef1DWPOT59%2FO89s3a%2Bj7e1EBN6AiEAjjVsSk%2F9STktdgBp%2FWXgmpGCDe5JtuaoQzL5QHGlbjIqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjZ0EyKM0Ge7MBIXyrcA3GUCAzECWDF6kMXmuntVTG9URj%2FjMGiKx8Vsxir6zafJQgW%2F3stwxhkE3S2MBKV4u%2Fr6U0CHfaovOPJRHvkmfsdlkr2hdG3vQlVHdsVDKabBuHZuM5pMWtEuNIG0k2Dr1FfmVueHjmztExX75NFhE33by2JpqGwA4q1hSu4U%2BbNogiSlEl8RtRq4gS2eq%2Bl8b2qxySDOZxYO33sgJy%2FCwkTDbJr7CUhsitlnmVIW9FOTRk%2FwicOaoaxwneENSir7bA57LV09a3%2BJW%2BtutGwDQSkNr7uJisclz2RgP1thx2QDDLA6hrYJ3znlnKSAFQtHulFu5RHvsaRJnAHlxWK4KkDvmQRKxExiu541CSeoT%2FLItq3CCIaAh92b%2FaZwIpUXFOqDGueql4Rf3bX0vkF4y2u2DZ566hTxAzulcMsuu5N0RctsGcI29zkhpEmYvod%2BXxo5wpfjo9Dv%2BLPC0OoOvtqHt1sb0Fnw%2Bauq8BDCK%2B1%2FtGIqfH3AWNaIAD75ORRGBSrM7ONJFQ%2Fhn%2FtoA%2FVNxGB3hwsIbSNEuAcCWCw%2BEAMSIUY4ZPj2cUxK4bJBFT5NqAwI6dM07EkVg7VuZbXWHE2XxmqLxulUtsW7XvskNhJDOCl9bWYRi4Hg1BhMKiy67wGOqUBHRTnXaBm0rmG2j72ftYdT1rnt263BHizJT8ZqJ%2B%2FZkC7f9w5GhdRFvx4rxew7tZDgTVmccJiOqIv0Rdg%2BpozeFYvRe6EK%2BhKBa6GtxBJ8FgN3gzTq8%2BAFhS9r5zgBDe3Wp6qUW5nD0pQNhLFniNz%2BVgXbbeKgrseVtckn7iYfQdGnrigMZScHIhTlgPXIbhS%2BCmvoDYZnNhXz4RIxrV6J7GV0LvR&X-Amz-Signature=8351e2c216cb1c1a42cd0250578a117a8e8892ce671056e0bc989172b5ac1532&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECVSXUO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAiUVWKbcT3fMCIqCgef1DWPOT59%2FO89s3a%2Bj7e1EBN6AiEAjjVsSk%2F9STktdgBp%2FWXgmpGCDe5JtuaoQzL5QHGlbjIqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjZ0EyKM0Ge7MBIXyrcA3GUCAzECWDF6kMXmuntVTG9URj%2FjMGiKx8Vsxir6zafJQgW%2F3stwxhkE3S2MBKV4u%2Fr6U0CHfaovOPJRHvkmfsdlkr2hdG3vQlVHdsVDKabBuHZuM5pMWtEuNIG0k2Dr1FfmVueHjmztExX75NFhE33by2JpqGwA4q1hSu4U%2BbNogiSlEl8RtRq4gS2eq%2Bl8b2qxySDOZxYO33sgJy%2FCwkTDbJr7CUhsitlnmVIW9FOTRk%2FwicOaoaxwneENSir7bA57LV09a3%2BJW%2BtutGwDQSkNr7uJisclz2RgP1thx2QDDLA6hrYJ3znlnKSAFQtHulFu5RHvsaRJnAHlxWK4KkDvmQRKxExiu541CSeoT%2FLItq3CCIaAh92b%2FaZwIpUXFOqDGueql4Rf3bX0vkF4y2u2DZ566hTxAzulcMsuu5N0RctsGcI29zkhpEmYvod%2BXxo5wpfjo9Dv%2BLPC0OoOvtqHt1sb0Fnw%2Bauq8BDCK%2B1%2FtGIqfH3AWNaIAD75ORRGBSrM7ONJFQ%2Fhn%2FtoA%2FVNxGB3hwsIbSNEuAcCWCw%2BEAMSIUY4ZPj2cUxK4bJBFT5NqAwI6dM07EkVg7VuZbXWHE2XxmqLxulUtsW7XvskNhJDOCl9bWYRi4Hg1BhMKiy67wGOqUBHRTnXaBm0rmG2j72ftYdT1rnt263BHizJT8ZqJ%2B%2FZkC7f9w5GhdRFvx4rxew7tZDgTVmccJiOqIv0Rdg%2BpozeFYvRe6EK%2BhKBa6GtxBJ8FgN3gzTq8%2BAFhS9r5zgBDe3Wp6qUW5nD0pQNhLFniNz%2BVgXbbeKgrseVtckn7iYfQdGnrigMZScHIhTlgPXIbhS%2BCmvoDYZnNhXz4RIxrV6J7GV0LvR&X-Amz-Signature=fb1c8de8d4fe67449e1128c0f79f7b2e862767b90b61e92b3d077e5b586a879b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECVSXUO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAiUVWKbcT3fMCIqCgef1DWPOT59%2FO89s3a%2Bj7e1EBN6AiEAjjVsSk%2F9STktdgBp%2FWXgmpGCDe5JtuaoQzL5QHGlbjIqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjZ0EyKM0Ge7MBIXyrcA3GUCAzECWDF6kMXmuntVTG9URj%2FjMGiKx8Vsxir6zafJQgW%2F3stwxhkE3S2MBKV4u%2Fr6U0CHfaovOPJRHvkmfsdlkr2hdG3vQlVHdsVDKabBuHZuM5pMWtEuNIG0k2Dr1FfmVueHjmztExX75NFhE33by2JpqGwA4q1hSu4U%2BbNogiSlEl8RtRq4gS2eq%2Bl8b2qxySDOZxYO33sgJy%2FCwkTDbJr7CUhsitlnmVIW9FOTRk%2FwicOaoaxwneENSir7bA57LV09a3%2BJW%2BtutGwDQSkNr7uJisclz2RgP1thx2QDDLA6hrYJ3znlnKSAFQtHulFu5RHvsaRJnAHlxWK4KkDvmQRKxExiu541CSeoT%2FLItq3CCIaAh92b%2FaZwIpUXFOqDGueql4Rf3bX0vkF4y2u2DZ566hTxAzulcMsuu5N0RctsGcI29zkhpEmYvod%2BXxo5wpfjo9Dv%2BLPC0OoOvtqHt1sb0Fnw%2Bauq8BDCK%2B1%2FtGIqfH3AWNaIAD75ORRGBSrM7ONJFQ%2Fhn%2FtoA%2FVNxGB3hwsIbSNEuAcCWCw%2BEAMSIUY4ZPj2cUxK4bJBFT5NqAwI6dM07EkVg7VuZbXWHE2XxmqLxulUtsW7XvskNhJDOCl9bWYRi4Hg1BhMKiy67wGOqUBHRTnXaBm0rmG2j72ftYdT1rnt263BHizJT8ZqJ%2B%2FZkC7f9w5GhdRFvx4rxew7tZDgTVmccJiOqIv0Rdg%2BpozeFYvRe6EK%2BhKBa6GtxBJ8FgN3gzTq8%2BAFhS9r5zgBDe3Wp6qUW5nD0pQNhLFniNz%2BVgXbbeKgrseVtckn7iYfQdGnrigMZScHIhTlgPXIbhS%2BCmvoDYZnNhXz4RIxrV6J7GV0LvR&X-Amz-Signature=61a8b24e7936709e07edcc0c77217a5f85b47fd04ff7f0c04d3aa1fa96b3cb5a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECVSXUO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAiUVWKbcT3fMCIqCgef1DWPOT59%2FO89s3a%2Bj7e1EBN6AiEAjjVsSk%2F9STktdgBp%2FWXgmpGCDe5JtuaoQzL5QHGlbjIqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGjZ0EyKM0Ge7MBIXyrcA3GUCAzECWDF6kMXmuntVTG9URj%2FjMGiKx8Vsxir6zafJQgW%2F3stwxhkE3S2MBKV4u%2Fr6U0CHfaovOPJRHvkmfsdlkr2hdG3vQlVHdsVDKabBuHZuM5pMWtEuNIG0k2Dr1FfmVueHjmztExX75NFhE33by2JpqGwA4q1hSu4U%2BbNogiSlEl8RtRq4gS2eq%2Bl8b2qxySDOZxYO33sgJy%2FCwkTDbJr7CUhsitlnmVIW9FOTRk%2FwicOaoaxwneENSir7bA57LV09a3%2BJW%2BtutGwDQSkNr7uJisclz2RgP1thx2QDDLA6hrYJ3znlnKSAFQtHulFu5RHvsaRJnAHlxWK4KkDvmQRKxExiu541CSeoT%2FLItq3CCIaAh92b%2FaZwIpUXFOqDGueql4Rf3bX0vkF4y2u2DZ566hTxAzulcMsuu5N0RctsGcI29zkhpEmYvod%2BXxo5wpfjo9Dv%2BLPC0OoOvtqHt1sb0Fnw%2Bauq8BDCK%2B1%2FtGIqfH3AWNaIAD75ORRGBSrM7ONJFQ%2Fhn%2FtoA%2FVNxGB3hwsIbSNEuAcCWCw%2BEAMSIUY4ZPj2cUxK4bJBFT5NqAwI6dM07EkVg7VuZbXWHE2XxmqLxulUtsW7XvskNhJDOCl9bWYRi4Hg1BhMKiy67wGOqUBHRTnXaBm0rmG2j72ftYdT1rnt263BHizJT8ZqJ%2B%2FZkC7f9w5GhdRFvx4rxew7tZDgTVmccJiOqIv0Rdg%2BpozeFYvRe6EK%2BhKBa6GtxBJ8FgN3gzTq8%2BAFhS9r5zgBDe3Wp6qUW5nD0pQNhLFniNz%2BVgXbbeKgrseVtckn7iYfQdGnrigMZScHIhTlgPXIbhS%2BCmvoDYZnNhXz4RIxrV6J7GV0LvR&X-Amz-Signature=68953ce44cea50f674dccb5c78d7b8d73f633b679656dd5e8b74311e7301deab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622VGSG4B%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBCT71lWECnkBMHlcvouemex%2BdLgqhlEX%2Fz1FKjkR7dJAiEAm9pNwzMWUNo4HG8l0yFZHWXQAqkRf9DlcBgFFTiI35kqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAUbO4fFAQjyJYXqFSrcA86j4e%2F2vrpWhsg5ij7C%2B4%2BokN3gGudzgOe3kJkZGiaigVb2JKjv0nPNtxh8GFRo1esoTkh1WJRUMkUCasUEkGLg4EhESxXbl0ZagXmxlnWbvtS9l2pC33co5iUfbaKUj%2FTn2ADxvz6fADyuAZdqf4l9hc3P3xOba3NYqih79Czd4XavnMENv49NYyj%2BPODpgRAQrRFsyAwVwaeCM398%2BnCwKrUUUPXy4GKiOHvdUHhhKKoeqM56%2BDdo%2FCcJ1V9fiCiwtjRTOQUgA6n6kddDvyQ3KBV8SPs6MUEsnXEpKx0aO91MkO8RusLjpCp4l3JyqQpzawS8GV39nQGH0I489aRsZie5itl6SF2phbd9fjNVhZXyAknUcknon%2FULlkiDUhNKxImzCWhzkm0sQ1IeUrzZepWSsPYJ%2FVxOP4t4MWPiJM2%2B8MY7zEWqiI3e255N%2BIwEXa66vND2k2oNe3jb0i7fWo%2FDQfuVb2quKDwhXk8KDNBb1U8PmB0N2jfYuaypXuzld%2FK7bMtr4it%2BUMVzNcbeQyycd71MnviHSOCYZl6s%2BTPZliTJjkxO7EO7J4PG%2FkxcdWO7rCC%2BxLlzfc7XoAIIJl2g7fUxKdHdZ%2BiWvP88oJlpSRC79%2BRDe8wFMO2x67wGOqUBmv7LR0Zn0%2Fs6zsg5yFP1%2FNHIJ0uc5uKYSMvmtDHaKeasmAEC2AjHrj3ZmLVMvAnLu4LHXpO%2FmqFq4f4T%2B9S15qw9ZEX40uLcjzrBx88Evf9x6gZHO%2FyxnRMTAlrcnFIrtXqzIIJuovhL2oddqIHgFLKUq6a48HexaVrr8CkVvlWAbUQ1j4VxjQvAXzmihiN793Iq9ieGm4sJJMGINe55Yu2ZFZx1&X-Amz-Signature=7e616bbe64d1d3e583063a35f6adac0feeb4643e3ab344f132ee25b67701c22c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NHX33RP%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe%2Bbz%2FQZKpSjbA2R2b0ZTeFpKN1nu1cFiU0OS2AUGYYwIgLxFth7LwuYBaI84VEm2ht3lZUUuADaL5XMCHd6H5hT0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLJMzwIhanwf2wgkCircA%2BK1l33TmmidElTbhh7Sh75rKhuQq%2FD9STfYR7xmJND1uR9GJfdhhNFmfP9pdzc9LXXxT2JcO20iRAOMRpIol4DZgcYpFVVXxU9cPh6kRXet9EffpARzSDtVBfrf5Uo%2FmWerDgo9PtbBHkiJHBuUFTqN300aSSKoQQXY2KRbSi26qe4clBiy%2BR3GR12uvikE1seLJ2CiOIiFkKLlbCkWlxcCmgR2OrHP%2BtziOZ6D4SjiQLlOfrhU3F0WC7nJnCQvBOdGcP6HKGEPKjKMZnr26MYnJ%2BqAmWHPzm6FHOT37Wz3aQvSdtJdcAGg%2BfFE3q1c0LvZPNeu11IyL70JNusa62mFun4gNnIYh%2BQCCM3tmbpnAu8jt2wZ2ogVAHfGixeTMK6Qavp39kVbEnZmMGc391mTQTZBcya98pMEeVaoP4v7tk0L4tPJkPgm29QLpH8NnIe9GnnS2gTqGEFsFQNlOxe%2BcHBKcZN8i8sewtSMwvP%2B86erk%2FqTBasQSMG5GF%2F1aw%2Bv5Uupi0M6lfCqskYaV%2FnNbxqOyNg1ZlPLVEcfQ9zzOcfbRiPXq4h8F3yHqX0pWL0h%2BDq9tJP6a%2BJIS1Q3%2Bzbvr01Ej7VeM9VEktE5UpXyLl3ab%2FF%2FIpWbpI8CMO2x67wGOqUBRETc5KKmhMHSZvy5NfQ6wyPa%2FigzKX9FaM%2BaGgHpoYynRlnppupykqbCO8L6IlHJJQ1aKimAnHqI%2FaSdF0%2FsnGP5REO93rCC9S4cHL9fDarHNf42bvb%2BgzSfhmEqghjcO5sdfZH6ymQ31BAWrdM%2F5j%2Bkms26ad5SuWyvVbDlFJLcQf7TswlF%2BUkH%2BNB0C%2BRKsNt1b0tqwe7VVBx2XF8b2Q7Ng0Q%2B&X-Amz-Signature=585195e4ff2190d97cf126497935c39f823ebf9c39441da3220c5c0835ce52d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MXXLMPM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8mV6CRbKgvG7q2kDtCf4p2yCASJNXmbI2d%2FDClQL7sQIhAMz34mOYjr2NXzAuz9HFP3VDHPTecxmNk0ArcSamS5SMKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwkTGimx%2BRvLTKHPxwq3APQth0K9csVeiKIS7EBe03MxV6oV9gIa%2FKYI3YXnUfjzfwe8w1sCOjdhpbMccFJNOi9wqplaTqsvt8Re5FOwAxSz%2FAI6xyYTuzn6A0t6NdVpTQ5wQnUvS%2BHr%2BovFi9u4rjQRPriA5MlL4P3WIOU%2FqhLYGNur1pQjzvrMoRA7HnIvC09mj2IzmGryctS3YY8qfuWrtrWGXpK7Ska2v9sig17TdDbY%2FapDn7Xuqy8503JiPbroE8VVWTW0qQfmL2MRPPoBuHhVnSHF4iTrfQDnQM2j80hDv7TBBoH0ggo%2FO1u9npPzi%2BKjGKWo3jgfkcU4m1MCTvk3QeyDda3SQX6nWxxq%2BMmWsFP%2F7a6yRthHXTmAXt6R0AifvigH64ehiZ5Eg1veUJCQPMe%2BvKnXEarQwVZThyfOxp%2F0x5WizLmHiJiX5tLCvLS6OrbATzepnkHWD42sLgmSmv7QG28n8r2t0yjiWqBp7%2F8qO4yPbc8H210CzV6i9l7T610fXvxIAt3eB6cExhgxkX3q%2FROnVb5Wou0B%2FpXCC1piBcmDrim6qFgQczjcuL9l0%2BvnQDvV41iyv8kRHS6prs9iBU%2BTRNZxioTlvs5Hve5U18d59%2BhmzJSZPijHjDR9eHPKzVa1DDRseu8BjqkAXLyrmJvs%2BhpzpgZj8CVb1tM85rWvd%2BTA%2F5WLtpb2nVM8R5uLId%2FhqE5Gd4YgytXxXp0NCuFITL%2FWGjLgdV%2BR8Ra1VywWlUo2ecp4ASunycjH1qHpFmMmJDZTRLcW3XdqrqdhgoF31RBuq8sE2CCVMjLbTlRkmDOlHAp2y6OZTZiSQN9jAPP1kmGxy9j%2FudtE6X4tUdWS%2Fw94q8AxRCutp5kLHva&X-Amz-Signature=bdf972cdc1a7c393ae0030a520b35d89d41965cd1b1017699efe87b566a735b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MXXLMPM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8mV6CRbKgvG7q2kDtCf4p2yCASJNXmbI2d%2FDClQL7sQIhAMz34mOYjr2NXzAuz9HFP3VDHPTecxmNk0ArcSamS5SMKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwkTGimx%2BRvLTKHPxwq3APQth0K9csVeiKIS7EBe03MxV6oV9gIa%2FKYI3YXnUfjzfwe8w1sCOjdhpbMccFJNOi9wqplaTqsvt8Re5FOwAxSz%2FAI6xyYTuzn6A0t6NdVpTQ5wQnUvS%2BHr%2BovFi9u4rjQRPriA5MlL4P3WIOU%2FqhLYGNur1pQjzvrMoRA7HnIvC09mj2IzmGryctS3YY8qfuWrtrWGXpK7Ska2v9sig17TdDbY%2FapDn7Xuqy8503JiPbroE8VVWTW0qQfmL2MRPPoBuHhVnSHF4iTrfQDnQM2j80hDv7TBBoH0ggo%2FO1u9npPzi%2BKjGKWo3jgfkcU4m1MCTvk3QeyDda3SQX6nWxxq%2BMmWsFP%2F7a6yRthHXTmAXt6R0AifvigH64ehiZ5Eg1veUJCQPMe%2BvKnXEarQwVZThyfOxp%2F0x5WizLmHiJiX5tLCvLS6OrbATzepnkHWD42sLgmSmv7QG28n8r2t0yjiWqBp7%2F8qO4yPbc8H210CzV6i9l7T610fXvxIAt3eB6cExhgxkX3q%2FROnVb5Wou0B%2FpXCC1piBcmDrim6qFgQczjcuL9l0%2BvnQDvV41iyv8kRHS6prs9iBU%2BTRNZxioTlvs5Hve5U18d59%2BhmzJSZPijHjDR9eHPKzVa1DDRseu8BjqkAXLyrmJvs%2BhpzpgZj8CVb1tM85rWvd%2BTA%2F5WLtpb2nVM8R5uLId%2FhqE5Gd4YgytXxXp0NCuFITL%2FWGjLgdV%2BR8Ra1VywWlUo2ecp4ASunycjH1qHpFmMmJDZTRLcW3XdqrqdhgoF31RBuq8sE2CCVMjLbTlRkmDOlHAp2y6OZTZiSQN9jAPP1kmGxy9j%2FudtE6X4tUdWS%2Fw94q8AxRCutp5kLHva&X-Amz-Signature=5949fcb81dd00ad57dec6f2d47188390a034b874425956aeb3879794912e4a70&X-Amz-SignedHeaders=host&x-id=GetObject)
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
