

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC3P64RB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDv30jYe1ko79t7zgx0qbFU0GwH79fgnsR5lVeyricyYAIhAPsjT9TQ7XTUsONUZYQnSUjxTjXzsK0piNgN%2FwyDX61dKv8DCCwQABoMNjM3NDIzMTgzODA1IgyuSugIjQAhCS7lO6sq3APYb9nAlFn9bKq6n1ObYEXfwRpCxvVqbk0AWX7rVPyY96vFNR7g7c9TZTWMqLkGA%2FYPnzmDTN5D8JcVNZM3aiRIMDiOIkkc7SgOSykCHzPqkUvJBaeuTrL4FjsyFS1Db6l7tsvdy2BDbVa9AIjq%2BnicRtPFx08DH9FXlP272rxk8mQ1bhfK1q3GD%2FhTiQ59lYTVFH7%2BOIWPjyqU0XpoofWv8YKxqdMkvdNFF0dgBUfBUFEub%2Fj%2B2WBHCFoE398RuTCiFg65wYBQu6DPoAlBAc%2F%2BZ5903%2BpDQqDAi%2BlLUhnNvna1OXWVminyVKtGlF2PojiWLLJqLaka9vtFxDRh5xseFTh%2BZjMlCPXHaIqo2h7EzXsWEGoC7J4Rcix%2FUXMa9M%2BoEcKN9EsCRuhsnR51r9i59U5R85gY401odZ9xgo1SksKIe2wBWeuz4kqhXzwPD5v337hrMMWDk0oq2iNuOefAZuQ7q074uRvHj74eWkz4Wht1OowKGkthQQHwuHlqpMVlvG7PO0u9%2Fb7CFWyD3WIbW85FfCW3xJjTz4hUYBd%2FEklZzjF0PRvOtmw9h%2By9M0Gwm%2FtvJZpWFEhRqlE9OL9f2CnQaKCWlRJ%2Ba9%2BjQIhYQiryDFPfYYgAQN8c9DCI5oe9BjqkAVSc98eB6h8C4Vn8GheXX1jrlEuy%2BkREJCP3JcHFSdmkz%2F5WQ7fWExqRyvIM5d9orIcddqEuM8xuXMZDHFQoFw4i6oGVtFvRvW%2FvWlKNymN61fTt5Yw7UEFGtxE838RxXQgW1EB5yoQZJl1FiIx20hpcq11eripTUhn5ON1Difdak5qcIQjkpIZotLdBltD0jT4ivio8qnNyRrKXtCuA5mKd7YWc&X-Amz-Signature=c6f1dfc0e42bfaac9f071e7e995c953a813a72cdc766f8038ca3b4fc7d6a52de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC3P64RB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDv30jYe1ko79t7zgx0qbFU0GwH79fgnsR5lVeyricyYAIhAPsjT9TQ7XTUsONUZYQnSUjxTjXzsK0piNgN%2FwyDX61dKv8DCCwQABoMNjM3NDIzMTgzODA1IgyuSugIjQAhCS7lO6sq3APYb9nAlFn9bKq6n1ObYEXfwRpCxvVqbk0AWX7rVPyY96vFNR7g7c9TZTWMqLkGA%2FYPnzmDTN5D8JcVNZM3aiRIMDiOIkkc7SgOSykCHzPqkUvJBaeuTrL4FjsyFS1Db6l7tsvdy2BDbVa9AIjq%2BnicRtPFx08DH9FXlP272rxk8mQ1bhfK1q3GD%2FhTiQ59lYTVFH7%2BOIWPjyqU0XpoofWv8YKxqdMkvdNFF0dgBUfBUFEub%2Fj%2B2WBHCFoE398RuTCiFg65wYBQu6DPoAlBAc%2F%2BZ5903%2BpDQqDAi%2BlLUhnNvna1OXWVminyVKtGlF2PojiWLLJqLaka9vtFxDRh5xseFTh%2BZjMlCPXHaIqo2h7EzXsWEGoC7J4Rcix%2FUXMa9M%2BoEcKN9EsCRuhsnR51r9i59U5R85gY401odZ9xgo1SksKIe2wBWeuz4kqhXzwPD5v337hrMMWDk0oq2iNuOefAZuQ7q074uRvHj74eWkz4Wht1OowKGkthQQHwuHlqpMVlvG7PO0u9%2Fb7CFWyD3WIbW85FfCW3xJjTz4hUYBd%2FEklZzjF0PRvOtmw9h%2By9M0Gwm%2FtvJZpWFEhRqlE9OL9f2CnQaKCWlRJ%2Ba9%2BjQIhYQiryDFPfYYgAQN8c9DCI5oe9BjqkAVSc98eB6h8C4Vn8GheXX1jrlEuy%2BkREJCP3JcHFSdmkz%2F5WQ7fWExqRyvIM5d9orIcddqEuM8xuXMZDHFQoFw4i6oGVtFvRvW%2FvWlKNymN61fTt5Yw7UEFGtxE838RxXQgW1EB5yoQZJl1FiIx20hpcq11eripTUhn5ON1Difdak5qcIQjkpIZotLdBltD0jT4ivio8qnNyRrKXtCuA5mKd7YWc&X-Amz-Signature=44b0740869223091812706491eb709b74bf26d4fee1bbdee1eff3ffd72f2dae2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC3P64RB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDv30jYe1ko79t7zgx0qbFU0GwH79fgnsR5lVeyricyYAIhAPsjT9TQ7XTUsONUZYQnSUjxTjXzsK0piNgN%2FwyDX61dKv8DCCwQABoMNjM3NDIzMTgzODA1IgyuSugIjQAhCS7lO6sq3APYb9nAlFn9bKq6n1ObYEXfwRpCxvVqbk0AWX7rVPyY96vFNR7g7c9TZTWMqLkGA%2FYPnzmDTN5D8JcVNZM3aiRIMDiOIkkc7SgOSykCHzPqkUvJBaeuTrL4FjsyFS1Db6l7tsvdy2BDbVa9AIjq%2BnicRtPFx08DH9FXlP272rxk8mQ1bhfK1q3GD%2FhTiQ59lYTVFH7%2BOIWPjyqU0XpoofWv8YKxqdMkvdNFF0dgBUfBUFEub%2Fj%2B2WBHCFoE398RuTCiFg65wYBQu6DPoAlBAc%2F%2BZ5903%2BpDQqDAi%2BlLUhnNvna1OXWVminyVKtGlF2PojiWLLJqLaka9vtFxDRh5xseFTh%2BZjMlCPXHaIqo2h7EzXsWEGoC7J4Rcix%2FUXMa9M%2BoEcKN9EsCRuhsnR51r9i59U5R85gY401odZ9xgo1SksKIe2wBWeuz4kqhXzwPD5v337hrMMWDk0oq2iNuOefAZuQ7q074uRvHj74eWkz4Wht1OowKGkthQQHwuHlqpMVlvG7PO0u9%2Fb7CFWyD3WIbW85FfCW3xJjTz4hUYBd%2FEklZzjF0PRvOtmw9h%2By9M0Gwm%2FtvJZpWFEhRqlE9OL9f2CnQaKCWlRJ%2Ba9%2BjQIhYQiryDFPfYYgAQN8c9DCI5oe9BjqkAVSc98eB6h8C4Vn8GheXX1jrlEuy%2BkREJCP3JcHFSdmkz%2F5WQ7fWExqRyvIM5d9orIcddqEuM8xuXMZDHFQoFw4i6oGVtFvRvW%2FvWlKNymN61fTt5Yw7UEFGtxE838RxXQgW1EB5yoQZJl1FiIx20hpcq11eripTUhn5ON1Difdak5qcIQjkpIZotLdBltD0jT4ivio8qnNyRrKXtCuA5mKd7YWc&X-Amz-Signature=c78f6a27c274d2a599eb47b8a568e830d5d9bfefd00f54f936d35ad4d9c8ea9b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC3P64RB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDv30jYe1ko79t7zgx0qbFU0GwH79fgnsR5lVeyricyYAIhAPsjT9TQ7XTUsONUZYQnSUjxTjXzsK0piNgN%2FwyDX61dKv8DCCwQABoMNjM3NDIzMTgzODA1IgyuSugIjQAhCS7lO6sq3APYb9nAlFn9bKq6n1ObYEXfwRpCxvVqbk0AWX7rVPyY96vFNR7g7c9TZTWMqLkGA%2FYPnzmDTN5D8JcVNZM3aiRIMDiOIkkc7SgOSykCHzPqkUvJBaeuTrL4FjsyFS1Db6l7tsvdy2BDbVa9AIjq%2BnicRtPFx08DH9FXlP272rxk8mQ1bhfK1q3GD%2FhTiQ59lYTVFH7%2BOIWPjyqU0XpoofWv8YKxqdMkvdNFF0dgBUfBUFEub%2Fj%2B2WBHCFoE398RuTCiFg65wYBQu6DPoAlBAc%2F%2BZ5903%2BpDQqDAi%2BlLUhnNvna1OXWVminyVKtGlF2PojiWLLJqLaka9vtFxDRh5xseFTh%2BZjMlCPXHaIqo2h7EzXsWEGoC7J4Rcix%2FUXMa9M%2BoEcKN9EsCRuhsnR51r9i59U5R85gY401odZ9xgo1SksKIe2wBWeuz4kqhXzwPD5v337hrMMWDk0oq2iNuOefAZuQ7q074uRvHj74eWkz4Wht1OowKGkthQQHwuHlqpMVlvG7PO0u9%2Fb7CFWyD3WIbW85FfCW3xJjTz4hUYBd%2FEklZzjF0PRvOtmw9h%2By9M0Gwm%2FtvJZpWFEhRqlE9OL9f2CnQaKCWlRJ%2Ba9%2BjQIhYQiryDFPfYYgAQN8c9DCI5oe9BjqkAVSc98eB6h8C4Vn8GheXX1jrlEuy%2BkREJCP3JcHFSdmkz%2F5WQ7fWExqRyvIM5d9orIcddqEuM8xuXMZDHFQoFw4i6oGVtFvRvW%2FvWlKNymN61fTt5Yw7UEFGtxE838RxXQgW1EB5yoQZJl1FiIx20hpcq11eripTUhn5ON1Difdak5qcIQjkpIZotLdBltD0jT4ivio8qnNyRrKXtCuA5mKd7YWc&X-Amz-Signature=1e939a979601fd34af4e0bd3641be66e1eff81bd954e1aff2674291a9a2388e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC3P64RB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDv30jYe1ko79t7zgx0qbFU0GwH79fgnsR5lVeyricyYAIhAPsjT9TQ7XTUsONUZYQnSUjxTjXzsK0piNgN%2FwyDX61dKv8DCCwQABoMNjM3NDIzMTgzODA1IgyuSugIjQAhCS7lO6sq3APYb9nAlFn9bKq6n1ObYEXfwRpCxvVqbk0AWX7rVPyY96vFNR7g7c9TZTWMqLkGA%2FYPnzmDTN5D8JcVNZM3aiRIMDiOIkkc7SgOSykCHzPqkUvJBaeuTrL4FjsyFS1Db6l7tsvdy2BDbVa9AIjq%2BnicRtPFx08DH9FXlP272rxk8mQ1bhfK1q3GD%2FhTiQ59lYTVFH7%2BOIWPjyqU0XpoofWv8YKxqdMkvdNFF0dgBUfBUFEub%2Fj%2B2WBHCFoE398RuTCiFg65wYBQu6DPoAlBAc%2F%2BZ5903%2BpDQqDAi%2BlLUhnNvna1OXWVminyVKtGlF2PojiWLLJqLaka9vtFxDRh5xseFTh%2BZjMlCPXHaIqo2h7EzXsWEGoC7J4Rcix%2FUXMa9M%2BoEcKN9EsCRuhsnR51r9i59U5R85gY401odZ9xgo1SksKIe2wBWeuz4kqhXzwPD5v337hrMMWDk0oq2iNuOefAZuQ7q074uRvHj74eWkz4Wht1OowKGkthQQHwuHlqpMVlvG7PO0u9%2Fb7CFWyD3WIbW85FfCW3xJjTz4hUYBd%2FEklZzjF0PRvOtmw9h%2By9M0Gwm%2FtvJZpWFEhRqlE9OL9f2CnQaKCWlRJ%2Ba9%2BjQIhYQiryDFPfYYgAQN8c9DCI5oe9BjqkAVSc98eB6h8C4Vn8GheXX1jrlEuy%2BkREJCP3JcHFSdmkz%2F5WQ7fWExqRyvIM5d9orIcddqEuM8xuXMZDHFQoFw4i6oGVtFvRvW%2FvWlKNymN61fTt5Yw7UEFGtxE838RxXQgW1EB5yoQZJl1FiIx20hpcq11eripTUhn5ON1Difdak5qcIQjkpIZotLdBltD0jT4ivio8qnNyRrKXtCuA5mKd7YWc&X-Amz-Signature=2af4f3eae044022d024a27a202ac3084e7af5f97ff5472a1b36d690ba4e77649&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC3P64RB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDv30jYe1ko79t7zgx0qbFU0GwH79fgnsR5lVeyricyYAIhAPsjT9TQ7XTUsONUZYQnSUjxTjXzsK0piNgN%2FwyDX61dKv8DCCwQABoMNjM3NDIzMTgzODA1IgyuSugIjQAhCS7lO6sq3APYb9nAlFn9bKq6n1ObYEXfwRpCxvVqbk0AWX7rVPyY96vFNR7g7c9TZTWMqLkGA%2FYPnzmDTN5D8JcVNZM3aiRIMDiOIkkc7SgOSykCHzPqkUvJBaeuTrL4FjsyFS1Db6l7tsvdy2BDbVa9AIjq%2BnicRtPFx08DH9FXlP272rxk8mQ1bhfK1q3GD%2FhTiQ59lYTVFH7%2BOIWPjyqU0XpoofWv8YKxqdMkvdNFF0dgBUfBUFEub%2Fj%2B2WBHCFoE398RuTCiFg65wYBQu6DPoAlBAc%2F%2BZ5903%2BpDQqDAi%2BlLUhnNvna1OXWVminyVKtGlF2PojiWLLJqLaka9vtFxDRh5xseFTh%2BZjMlCPXHaIqo2h7EzXsWEGoC7J4Rcix%2FUXMa9M%2BoEcKN9EsCRuhsnR51r9i59U5R85gY401odZ9xgo1SksKIe2wBWeuz4kqhXzwPD5v337hrMMWDk0oq2iNuOefAZuQ7q074uRvHj74eWkz4Wht1OowKGkthQQHwuHlqpMVlvG7PO0u9%2Fb7CFWyD3WIbW85FfCW3xJjTz4hUYBd%2FEklZzjF0PRvOtmw9h%2By9M0Gwm%2FtvJZpWFEhRqlE9OL9f2CnQaKCWlRJ%2Ba9%2BjQIhYQiryDFPfYYgAQN8c9DCI5oe9BjqkAVSc98eB6h8C4Vn8GheXX1jrlEuy%2BkREJCP3JcHFSdmkz%2F5WQ7fWExqRyvIM5d9orIcddqEuM8xuXMZDHFQoFw4i6oGVtFvRvW%2FvWlKNymN61fTt5Yw7UEFGtxE838RxXQgW1EB5yoQZJl1FiIx20hpcq11eripTUhn5ON1Difdak5qcIQjkpIZotLdBltD0jT4ivio8qnNyRrKXtCuA5mKd7YWc&X-Amz-Signature=8e51b5c86ba1a77cec71743707d6fe761ccfe76e9e13e78d38066c288e82b862&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC3P64RB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDv30jYe1ko79t7zgx0qbFU0GwH79fgnsR5lVeyricyYAIhAPsjT9TQ7XTUsONUZYQnSUjxTjXzsK0piNgN%2FwyDX61dKv8DCCwQABoMNjM3NDIzMTgzODA1IgyuSugIjQAhCS7lO6sq3APYb9nAlFn9bKq6n1ObYEXfwRpCxvVqbk0AWX7rVPyY96vFNR7g7c9TZTWMqLkGA%2FYPnzmDTN5D8JcVNZM3aiRIMDiOIkkc7SgOSykCHzPqkUvJBaeuTrL4FjsyFS1Db6l7tsvdy2BDbVa9AIjq%2BnicRtPFx08DH9FXlP272rxk8mQ1bhfK1q3GD%2FhTiQ59lYTVFH7%2BOIWPjyqU0XpoofWv8YKxqdMkvdNFF0dgBUfBUFEub%2Fj%2B2WBHCFoE398RuTCiFg65wYBQu6DPoAlBAc%2F%2BZ5903%2BpDQqDAi%2BlLUhnNvna1OXWVminyVKtGlF2PojiWLLJqLaka9vtFxDRh5xseFTh%2BZjMlCPXHaIqo2h7EzXsWEGoC7J4Rcix%2FUXMa9M%2BoEcKN9EsCRuhsnR51r9i59U5R85gY401odZ9xgo1SksKIe2wBWeuz4kqhXzwPD5v337hrMMWDk0oq2iNuOefAZuQ7q074uRvHj74eWkz4Wht1OowKGkthQQHwuHlqpMVlvG7PO0u9%2Fb7CFWyD3WIbW85FfCW3xJjTz4hUYBd%2FEklZzjF0PRvOtmw9h%2By9M0Gwm%2FtvJZpWFEhRqlE9OL9f2CnQaKCWlRJ%2Ba9%2BjQIhYQiryDFPfYYgAQN8c9DCI5oe9BjqkAVSc98eB6h8C4Vn8GheXX1jrlEuy%2BkREJCP3JcHFSdmkz%2F5WQ7fWExqRyvIM5d9orIcddqEuM8xuXMZDHFQoFw4i6oGVtFvRvW%2FvWlKNymN61fTt5Yw7UEFGtxE838RxXQgW1EB5yoQZJl1FiIx20hpcq11eripTUhn5ON1Difdak5qcIQjkpIZotLdBltD0jT4ivio8qnNyRrKXtCuA5mKd7YWc&X-Amz-Signature=da3196e22d502546f9c39498e0af1e5f31a990487cd82f89168c55162d9d0781&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC3P64RB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQDv30jYe1ko79t7zgx0qbFU0GwH79fgnsR5lVeyricyYAIhAPsjT9TQ7XTUsONUZYQnSUjxTjXzsK0piNgN%2FwyDX61dKv8DCCwQABoMNjM3NDIzMTgzODA1IgyuSugIjQAhCS7lO6sq3APYb9nAlFn9bKq6n1ObYEXfwRpCxvVqbk0AWX7rVPyY96vFNR7g7c9TZTWMqLkGA%2FYPnzmDTN5D8JcVNZM3aiRIMDiOIkkc7SgOSykCHzPqkUvJBaeuTrL4FjsyFS1Db6l7tsvdy2BDbVa9AIjq%2BnicRtPFx08DH9FXlP272rxk8mQ1bhfK1q3GD%2FhTiQ59lYTVFH7%2BOIWPjyqU0XpoofWv8YKxqdMkvdNFF0dgBUfBUFEub%2Fj%2B2WBHCFoE398RuTCiFg65wYBQu6DPoAlBAc%2F%2BZ5903%2BpDQqDAi%2BlLUhnNvna1OXWVminyVKtGlF2PojiWLLJqLaka9vtFxDRh5xseFTh%2BZjMlCPXHaIqo2h7EzXsWEGoC7J4Rcix%2FUXMa9M%2BoEcKN9EsCRuhsnR51r9i59U5R85gY401odZ9xgo1SksKIe2wBWeuz4kqhXzwPD5v337hrMMWDk0oq2iNuOefAZuQ7q074uRvHj74eWkz4Wht1OowKGkthQQHwuHlqpMVlvG7PO0u9%2Fb7CFWyD3WIbW85FfCW3xJjTz4hUYBd%2FEklZzjF0PRvOtmw9h%2By9M0Gwm%2FtvJZpWFEhRqlE9OL9f2CnQaKCWlRJ%2Ba9%2BjQIhYQiryDFPfYYgAQN8c9DCI5oe9BjqkAVSc98eB6h8C4Vn8GheXX1jrlEuy%2BkREJCP3JcHFSdmkz%2F5WQ7fWExqRyvIM5d9orIcddqEuM8xuXMZDHFQoFw4i6oGVtFvRvW%2FvWlKNymN61fTt5Yw7UEFGtxE838RxXQgW1EB5yoQZJl1FiIx20hpcq11eripTUhn5ON1Difdak5qcIQjkpIZotLdBltD0jT4ivio8qnNyRrKXtCuA5mKd7YWc&X-Amz-Signature=e7be2c3e0893ffcfb559639eccd6581c8aee827d2c82adddcaaadb2c9cacc757&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RH7BNTY5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIFcSzUX5QREYuBAWcIwjcsEg9Bt6y%2FAz%2FvdO9A%2F%2F8zXrAiEAsxEU2yfHDu6qLb9Zep5t6%2FK5dKyQ4z5TEcBtxde3qWEq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNGd7DiiFpf2rNeauircA4SYw3eIrMfZhvbCsoQg4A8vptamKtrWzIYv%2BEtYwa%2FWsNMdGp%2F1bv0FXi%2FMRkce3mVoGV4BIfM443ecAh7GaX%2FGOep2dvzVBbniER2yH%2Bnm7UpOZv9DfiHhYlApZdk%2BaU7Vtiuhi7HtAzvuWVAPyitjkkLnd3oalafQRWh6mXGHM7aFw0tbh1LkLfh5YIzNEe7wNGgbQlzoaEBlzKzOF9Ep5cibC6VCiZcXgw2kJuZCtXY9F3dqUVdRZgQduD%2FeELyG2QGPUQTzxYr0xT1RwOmPGIDk8GDpmZzH9LqEawVNm6M7cepYaaTfsi9ZEDln3HJCfl1HJhtruyXaviXeeq4hLuuFNFtBuEOfM%2FucQ6yATrQAYCyEr0dEVl48%2Fu5nFONDdBpbsywB38KfzyB%2Bw035CUvYv3RXVc6ow4SeNtzIGsf5JJUxpk0XmeeSTfz6W9f2Qerb25Mbtobq6KdoRdFazLwU%2ButQ6jc%2FKVkI%2FD71z04MEM13f5GJuFMjdPovzHYf%2FSbwRNF3lC3qGmnyeiWlrPszS3izj52cR8OL7LeLt0%2FzNgIJ95DrXVrHVA6hXzhNFhGNyT2cny9MPm9gXiIkrH8fLPWWppPAvKTZXVGYoiSBe8ak2XcYCafFML7lh70GOqUBIEnuFEs39J4dpBcbIJ5A6QwZNMZOKbBNoiSGOfnIXalST39O6v%2FwpmTU7d9jiTDz%2BwxRSrefYKLl3wRnm89tqcN9YgHrAF6Qlskw%2FC5dgr5NIvFRqgpC5yv1G063IRB%2BE5ItenlLNmTbIzM6PUdJdKiHsLVf63yc5BREnF8GcTgVPqgnLoxXUVhkoawrhcZcRPmfVpSC5cDQwcdvgOu1NQd8PeUD&X-Amz-Signature=91246f1e519ecd68eca4776c439a8f5c4a21674cd15437f0bc0685ae7b5df59c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEUGCKL2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCICeHrzK5mu49x%2Bo%2FEMPxyh11zF%2FDCr2jfW%2BcGE8HeSNkAiEAxonD0Y2FB8uI7p9jGA2yKxUlLrCyeZqvZOLG%2BliN%2FMkq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDKq6JuDlbH9HJOqwXCrcAz1N0%2FQ03fKr5Mbb0GwU39nhVb1ZxMiwgik28OUf2xWJluU5C4pt1WWS2LSnmLqALsl5OK4gd980O730b3lnZ1RtpIGTgdD%2Bwsn9lbmF57KOeMlNumbiqeUG7AXFES7tSTgv1aERMILAq%2BLGE6isVb8JBHxLR6E%2BbKVVrxEmK4aGtDbUiYtaVvHpPrufAnbh3GTE4v%2Bjdoa5Lz8ei%2FeOLKKhjKC97bKSH3uIMKxE%2FQdD5TdwRqKmVs4N1nCdacT1EgMzKvGyRe1g6vccG2NLuBKB9mNaAg6Q8jHYphD4dT0rk5DA0I7vsJcfKl57Fnry7nG%2FTk3aCHpT8KudLV2tQTkKmsYNe28%2FBdMaCDT8rjJSTeNVvEUuavyYvpGacQ9UQWQvhpa2Q4glMjLdM%2Fiu7sW2jznsjkOIrbXUyZL7zLZZ4Jsn0bs32P5libacf2xhauk7DsGyEPoCehHQRMjCUN919oN7NqI4pzwXf0MkvTNO1fmDbNgGB4vn8AcZvtvfdwERboZ0elS6CGjp4UHhbUXmzcOFlIEJjo38zRJ7nTW6Wq4mlvYeqKFrmWD1lEjVLw7CTWo6qSLI5SfmZgnGjm8zFX4VIIDUPgjkUtty5IEXJWrvA8pzzg4ehqJ2ML%2Flh70GOqUBFdsuWZ2oOTfWWohieRoT1ijqvB9PZxafDvW6WWyG8B5tH8%2FdPsw8EW%2BtnDxC6Bfs1W4SBDghuR4O%2BGN6muFGjod52YmeGYWT6ydh6IRAkdg9AqE7bDNryeLIctI2VyYF8j8E86nAPGv4EXymRfP0LRtxdeQYUT2I3b8ovT7Cwi8eNC9AeRt6KycOOoiYOAvXhEEQJHe6gP%2FQs2kJROMLiiev63me&X-Amz-Signature=497c2c1328acd8e740cc67973575f615c6f3b3e6847451f67b5aa2dd39606c3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW4YVNVX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCObH21JzanHGPlsbzRd02dhgIhcboEccTl9hZ7ZX%2FurgIgVEXglC%2FUmi2Zk5DSxQqIUpkf1So28d%2BVNtTWPuNFc1cq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDJlzUFGiOsJEdRFgMSrcA2iHe4QN7n4n%2BfpShteOg9YxlCJ3qlpg%2F2oF4eXRHwKKjNNRVQbeIRNWF8UibeRW9LVSDYK5fBsdF2hyMGKj%2FTY17ZB%2BUv8fDXT7PQkEm4OGMxN%2BEBOBQkZASqsdZ%2BrcqgJSTIV7VH6irxLoj%2FEaZ%2FNIguZT5o1BRJAQE5WUaJWJLAqmG3AEcjFvDewIB89yiWfav%2BoZ%2B2IqQAMQasbYVKSfph7uGPlJFS8%2BC244XfQtABVTyEfbf%2FO5z13J1PYaaljmAjb8dCaUhL0l0xRbNVgp0HzdaYidDU8HEK5Tn8i6jCYiFfnmtOtt4sZ0W41kfRBUMbjzc7tPvGxwrA9BjCPcvXskz4fniDn9GqG733jVYLqRxMoKPc1hUykQDMAmby5cJSMhbKBpvULA%2FwcGbh9V2sLQDuG5hePXi6tFm0aV5iDbtZ3Lvy7BvRFv2cleRcAJbHfiHIHD0lkGmIdkVMLHdNh%2F%2BStLbVUW1Uwlknsw6eiLdx95VpfYgNXtsQfAwRnlcL2dQmKNW1e%2BHzwUhwGu7MT3OoCB%2BD0vkE%2BVsN3y2tpg1Z5a4hbaV0xzNvVTjzTmp1Asyam%2BTpHR%2FocQiAtplFksvE%2B%2BmFV2zNUllk%2B3drvdEwB8ViIp5popMInmh70GOqUBIJwJ8FJbl5Cnh15qapQGk8aw8mHdQ5v%2BB0FysjTM6hU13T4oygf68keulhxbbBuFhrt%2BYdPc4ycUjnNZGTzfFwcw5RF9JhR5eJrPd4h4pmP6WbT2y5H%2FKmHl2sKiL8lAx5UynKTPYOK8coMQiwPYi209dlP2oCasmUFwFxiNTmPMWLt9qVXS%2BJmEcMpJCVJGSF%2Bi5j9OX1agTukTKRKBJStQFaHQ&X-Amz-Signature=e10241f82ef53530e4ed825ca01b789ea8179fbe08ad3ae74a53d7ee85320c1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW4YVNVX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCObH21JzanHGPlsbzRd02dhgIhcboEccTl9hZ7ZX%2FurgIgVEXglC%2FUmi2Zk5DSxQqIUpkf1So28d%2BVNtTWPuNFc1cq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDJlzUFGiOsJEdRFgMSrcA2iHe4QN7n4n%2BfpShteOg9YxlCJ3qlpg%2F2oF4eXRHwKKjNNRVQbeIRNWF8UibeRW9LVSDYK5fBsdF2hyMGKj%2FTY17ZB%2BUv8fDXT7PQkEm4OGMxN%2BEBOBQkZASqsdZ%2BrcqgJSTIV7VH6irxLoj%2FEaZ%2FNIguZT5o1BRJAQE5WUaJWJLAqmG3AEcjFvDewIB89yiWfav%2BoZ%2B2IqQAMQasbYVKSfph7uGPlJFS8%2BC244XfQtABVTyEfbf%2FO5z13J1PYaaljmAjb8dCaUhL0l0xRbNVgp0HzdaYidDU8HEK5Tn8i6jCYiFfnmtOtt4sZ0W41kfRBUMbjzc7tPvGxwrA9BjCPcvXskz4fniDn9GqG733jVYLqRxMoKPc1hUykQDMAmby5cJSMhbKBpvULA%2FwcGbh9V2sLQDuG5hePXi6tFm0aV5iDbtZ3Lvy7BvRFv2cleRcAJbHfiHIHD0lkGmIdkVMLHdNh%2F%2BStLbVUW1Uwlknsw6eiLdx95VpfYgNXtsQfAwRnlcL2dQmKNW1e%2BHzwUhwGu7MT3OoCB%2BD0vkE%2BVsN3y2tpg1Z5a4hbaV0xzNvVTjzTmp1Asyam%2BTpHR%2FocQiAtplFksvE%2B%2BmFV2zNUllk%2B3drvdEwB8ViIp5popMInmh70GOqUBIJwJ8FJbl5Cnh15qapQGk8aw8mHdQ5v%2BB0FysjTM6hU13T4oygf68keulhxbbBuFhrt%2BYdPc4ycUjnNZGTzfFwcw5RF9JhR5eJrPd4h4pmP6WbT2y5H%2FKmHl2sKiL8lAx5UynKTPYOK8coMQiwPYi209dlP2oCasmUFwFxiNTmPMWLt9qVXS%2BJmEcMpJCVJGSF%2Bi5j9OX1agTukTKRKBJStQFaHQ&X-Amz-Signature=54d076fc4c8e12802d624a2b7f9989aae3d981b9fc9f90ff21a0696751de99db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
