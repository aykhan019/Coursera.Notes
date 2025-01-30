

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RANFNGLV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRP%2FKTqLps3gnp4B6ptBnw2oCAslErsDciPX21tQlqDAIhAL6Vy2JRq8GTF7gz4zCrTaJJ7CVwYbZxaVmDjdf5B8PqKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyA6pawA%2F5KvoE8fRsq3AMuNryNaCr98H0PFxulHMt%2BAo37ORLGHAxLNm9LqH%2FFGmbcLxZ4ZsITQ2CBFHQ67WjfNFdIg79x724NpkIG9gDoMroiWPo5e3XGhZsHKeG05t1ll66iNkpAM7Khdr1XTHGR17CX1ju7bVRputU%2FWFYUxpy62FAoYcLJXLnJzSS1%2F%2By9q2KfHNgibyQNylrzl3qYcB9euDJyFm6%2FqtgTD23KJvI3AKEilFb%2FhXFB6MK4M%2F1h7o9PbyveuhuYu6WmT9cKayqeJDVDSSbHcEiWYO7l7TrsZ048K4uZvXnNLg0el0Z%2FBiC8cB75AW7Dmg14cIDrwd1ocbyrrKS%2BLTrGTsVTqgq21qh8aosJGeGnQXw64PgNjA%2FDfaDNOKLEEtLVXdOM9vWv8y60ycwlP%2FAkVx4lKDdjPICOxqxRdB43EzUkFdnstAv3uK1PQGpddASki7VTT7NEXbov15qCCTl3OSNdB62Vj2b2RwaqEYkFAW%2Fh8103plDYUxrFO4vaYHVVLEN3GtODMpY4D6bmInRaHW%2B8EuT2rJBmMAc1vXbjPV5Jh261N8VBU2QP48CVLCEq4LdBj5a1VDW7ganRhPRiRLMbFb1P85kJ8hgVrOU1MZ9ERjk7vDGCcWHvwgaJdjCAl%2Bu8BjqkAcUfalwdiymkPQqNJ1YxwcfAm172EAJ6OKHJgQe4TAkF%2B8Rh%2B2yrSUaDW4tKRZK2nlMELTNFJMr0gAgQtoS%2BH1vwegOebNAgn9JrguCYjr%2B0k1OyWJDDpPalpHgnUlfvsvhsGqc51jcBUvAHF25UdZm1Y2loymG0PRMG2tGBULTT%2FQW1BwbZwO7uVxrgCuzK3k8dHidy%2B2B8VyrtLlHewCVzI0dh&X-Amz-Signature=4930146b5b9d7fe888534ba2088316e0fc99920227de36182a348b15b946c2ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RANFNGLV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRP%2FKTqLps3gnp4B6ptBnw2oCAslErsDciPX21tQlqDAIhAL6Vy2JRq8GTF7gz4zCrTaJJ7CVwYbZxaVmDjdf5B8PqKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyA6pawA%2F5KvoE8fRsq3AMuNryNaCr98H0PFxulHMt%2BAo37ORLGHAxLNm9LqH%2FFGmbcLxZ4ZsITQ2CBFHQ67WjfNFdIg79x724NpkIG9gDoMroiWPo5e3XGhZsHKeG05t1ll66iNkpAM7Khdr1XTHGR17CX1ju7bVRputU%2FWFYUxpy62FAoYcLJXLnJzSS1%2F%2By9q2KfHNgibyQNylrzl3qYcB9euDJyFm6%2FqtgTD23KJvI3AKEilFb%2FhXFB6MK4M%2F1h7o9PbyveuhuYu6WmT9cKayqeJDVDSSbHcEiWYO7l7TrsZ048K4uZvXnNLg0el0Z%2FBiC8cB75AW7Dmg14cIDrwd1ocbyrrKS%2BLTrGTsVTqgq21qh8aosJGeGnQXw64PgNjA%2FDfaDNOKLEEtLVXdOM9vWv8y60ycwlP%2FAkVx4lKDdjPICOxqxRdB43EzUkFdnstAv3uK1PQGpddASki7VTT7NEXbov15qCCTl3OSNdB62Vj2b2RwaqEYkFAW%2Fh8103plDYUxrFO4vaYHVVLEN3GtODMpY4D6bmInRaHW%2B8EuT2rJBmMAc1vXbjPV5Jh261N8VBU2QP48CVLCEq4LdBj5a1VDW7ganRhPRiRLMbFb1P85kJ8hgVrOU1MZ9ERjk7vDGCcWHvwgaJdjCAl%2Bu8BjqkAcUfalwdiymkPQqNJ1YxwcfAm172EAJ6OKHJgQe4TAkF%2B8Rh%2B2yrSUaDW4tKRZK2nlMELTNFJMr0gAgQtoS%2BH1vwegOebNAgn9JrguCYjr%2B0k1OyWJDDpPalpHgnUlfvsvhsGqc51jcBUvAHF25UdZm1Y2loymG0PRMG2tGBULTT%2FQW1BwbZwO7uVxrgCuzK3k8dHidy%2B2B8VyrtLlHewCVzI0dh&X-Amz-Signature=e723b9e611ac398a95cdeed7416dacb0301f633a10ebee6be3fa17bb9b899ae9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RANFNGLV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRP%2FKTqLps3gnp4B6ptBnw2oCAslErsDciPX21tQlqDAIhAL6Vy2JRq8GTF7gz4zCrTaJJ7CVwYbZxaVmDjdf5B8PqKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyA6pawA%2F5KvoE8fRsq3AMuNryNaCr98H0PFxulHMt%2BAo37ORLGHAxLNm9LqH%2FFGmbcLxZ4ZsITQ2CBFHQ67WjfNFdIg79x724NpkIG9gDoMroiWPo5e3XGhZsHKeG05t1ll66iNkpAM7Khdr1XTHGR17CX1ju7bVRputU%2FWFYUxpy62FAoYcLJXLnJzSS1%2F%2By9q2KfHNgibyQNylrzl3qYcB9euDJyFm6%2FqtgTD23KJvI3AKEilFb%2FhXFB6MK4M%2F1h7o9PbyveuhuYu6WmT9cKayqeJDVDSSbHcEiWYO7l7TrsZ048K4uZvXnNLg0el0Z%2FBiC8cB75AW7Dmg14cIDrwd1ocbyrrKS%2BLTrGTsVTqgq21qh8aosJGeGnQXw64PgNjA%2FDfaDNOKLEEtLVXdOM9vWv8y60ycwlP%2FAkVx4lKDdjPICOxqxRdB43EzUkFdnstAv3uK1PQGpddASki7VTT7NEXbov15qCCTl3OSNdB62Vj2b2RwaqEYkFAW%2Fh8103plDYUxrFO4vaYHVVLEN3GtODMpY4D6bmInRaHW%2B8EuT2rJBmMAc1vXbjPV5Jh261N8VBU2QP48CVLCEq4LdBj5a1VDW7ganRhPRiRLMbFb1P85kJ8hgVrOU1MZ9ERjk7vDGCcWHvwgaJdjCAl%2Bu8BjqkAcUfalwdiymkPQqNJ1YxwcfAm172EAJ6OKHJgQe4TAkF%2B8Rh%2B2yrSUaDW4tKRZK2nlMELTNFJMr0gAgQtoS%2BH1vwegOebNAgn9JrguCYjr%2B0k1OyWJDDpPalpHgnUlfvsvhsGqc51jcBUvAHF25UdZm1Y2loymG0PRMG2tGBULTT%2FQW1BwbZwO7uVxrgCuzK3k8dHidy%2B2B8VyrtLlHewCVzI0dh&X-Amz-Signature=2d1c6d90b6b29d407de57301be923b483799edcaac529a6bbcd488bd2ab2f9f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RANFNGLV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRP%2FKTqLps3gnp4B6ptBnw2oCAslErsDciPX21tQlqDAIhAL6Vy2JRq8GTF7gz4zCrTaJJ7CVwYbZxaVmDjdf5B8PqKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyA6pawA%2F5KvoE8fRsq3AMuNryNaCr98H0PFxulHMt%2BAo37ORLGHAxLNm9LqH%2FFGmbcLxZ4ZsITQ2CBFHQ67WjfNFdIg79x724NpkIG9gDoMroiWPo5e3XGhZsHKeG05t1ll66iNkpAM7Khdr1XTHGR17CX1ju7bVRputU%2FWFYUxpy62FAoYcLJXLnJzSS1%2F%2By9q2KfHNgibyQNylrzl3qYcB9euDJyFm6%2FqtgTD23KJvI3AKEilFb%2FhXFB6MK4M%2F1h7o9PbyveuhuYu6WmT9cKayqeJDVDSSbHcEiWYO7l7TrsZ048K4uZvXnNLg0el0Z%2FBiC8cB75AW7Dmg14cIDrwd1ocbyrrKS%2BLTrGTsVTqgq21qh8aosJGeGnQXw64PgNjA%2FDfaDNOKLEEtLVXdOM9vWv8y60ycwlP%2FAkVx4lKDdjPICOxqxRdB43EzUkFdnstAv3uK1PQGpddASki7VTT7NEXbov15qCCTl3OSNdB62Vj2b2RwaqEYkFAW%2Fh8103plDYUxrFO4vaYHVVLEN3GtODMpY4D6bmInRaHW%2B8EuT2rJBmMAc1vXbjPV5Jh261N8VBU2QP48CVLCEq4LdBj5a1VDW7ganRhPRiRLMbFb1P85kJ8hgVrOU1MZ9ERjk7vDGCcWHvwgaJdjCAl%2Bu8BjqkAcUfalwdiymkPQqNJ1YxwcfAm172EAJ6OKHJgQe4TAkF%2B8Rh%2B2yrSUaDW4tKRZK2nlMELTNFJMr0gAgQtoS%2BH1vwegOebNAgn9JrguCYjr%2B0k1OyWJDDpPalpHgnUlfvsvhsGqc51jcBUvAHF25UdZm1Y2loymG0PRMG2tGBULTT%2FQW1BwbZwO7uVxrgCuzK3k8dHidy%2B2B8VyrtLlHewCVzI0dh&X-Amz-Signature=f8f7d4b007befb78e743da4260974cc099d49449edbe3fbea912e7081a4d637e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RANFNGLV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRP%2FKTqLps3gnp4B6ptBnw2oCAslErsDciPX21tQlqDAIhAL6Vy2JRq8GTF7gz4zCrTaJJ7CVwYbZxaVmDjdf5B8PqKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyA6pawA%2F5KvoE8fRsq3AMuNryNaCr98H0PFxulHMt%2BAo37ORLGHAxLNm9LqH%2FFGmbcLxZ4ZsITQ2CBFHQ67WjfNFdIg79x724NpkIG9gDoMroiWPo5e3XGhZsHKeG05t1ll66iNkpAM7Khdr1XTHGR17CX1ju7bVRputU%2FWFYUxpy62FAoYcLJXLnJzSS1%2F%2By9q2KfHNgibyQNylrzl3qYcB9euDJyFm6%2FqtgTD23KJvI3AKEilFb%2FhXFB6MK4M%2F1h7o9PbyveuhuYu6WmT9cKayqeJDVDSSbHcEiWYO7l7TrsZ048K4uZvXnNLg0el0Z%2FBiC8cB75AW7Dmg14cIDrwd1ocbyrrKS%2BLTrGTsVTqgq21qh8aosJGeGnQXw64PgNjA%2FDfaDNOKLEEtLVXdOM9vWv8y60ycwlP%2FAkVx4lKDdjPICOxqxRdB43EzUkFdnstAv3uK1PQGpddASki7VTT7NEXbov15qCCTl3OSNdB62Vj2b2RwaqEYkFAW%2Fh8103plDYUxrFO4vaYHVVLEN3GtODMpY4D6bmInRaHW%2B8EuT2rJBmMAc1vXbjPV5Jh261N8VBU2QP48CVLCEq4LdBj5a1VDW7ganRhPRiRLMbFb1P85kJ8hgVrOU1MZ9ERjk7vDGCcWHvwgaJdjCAl%2Bu8BjqkAcUfalwdiymkPQqNJ1YxwcfAm172EAJ6OKHJgQe4TAkF%2B8Rh%2B2yrSUaDW4tKRZK2nlMELTNFJMr0gAgQtoS%2BH1vwegOebNAgn9JrguCYjr%2B0k1OyWJDDpPalpHgnUlfvsvhsGqc51jcBUvAHF25UdZm1Y2loymG0PRMG2tGBULTT%2FQW1BwbZwO7uVxrgCuzK3k8dHidy%2B2B8VyrtLlHewCVzI0dh&X-Amz-Signature=fa06c5d08a15006e1da5f393b3535bccd1e5a736ea5407a3cf930ecff6cb085f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RANFNGLV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRP%2FKTqLps3gnp4B6ptBnw2oCAslErsDciPX21tQlqDAIhAL6Vy2JRq8GTF7gz4zCrTaJJ7CVwYbZxaVmDjdf5B8PqKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyA6pawA%2F5KvoE8fRsq3AMuNryNaCr98H0PFxulHMt%2BAo37ORLGHAxLNm9LqH%2FFGmbcLxZ4ZsITQ2CBFHQ67WjfNFdIg79x724NpkIG9gDoMroiWPo5e3XGhZsHKeG05t1ll66iNkpAM7Khdr1XTHGR17CX1ju7bVRputU%2FWFYUxpy62FAoYcLJXLnJzSS1%2F%2By9q2KfHNgibyQNylrzl3qYcB9euDJyFm6%2FqtgTD23KJvI3AKEilFb%2FhXFB6MK4M%2F1h7o9PbyveuhuYu6WmT9cKayqeJDVDSSbHcEiWYO7l7TrsZ048K4uZvXnNLg0el0Z%2FBiC8cB75AW7Dmg14cIDrwd1ocbyrrKS%2BLTrGTsVTqgq21qh8aosJGeGnQXw64PgNjA%2FDfaDNOKLEEtLVXdOM9vWv8y60ycwlP%2FAkVx4lKDdjPICOxqxRdB43EzUkFdnstAv3uK1PQGpddASki7VTT7NEXbov15qCCTl3OSNdB62Vj2b2RwaqEYkFAW%2Fh8103plDYUxrFO4vaYHVVLEN3GtODMpY4D6bmInRaHW%2B8EuT2rJBmMAc1vXbjPV5Jh261N8VBU2QP48CVLCEq4LdBj5a1VDW7ganRhPRiRLMbFb1P85kJ8hgVrOU1MZ9ERjk7vDGCcWHvwgaJdjCAl%2Bu8BjqkAcUfalwdiymkPQqNJ1YxwcfAm172EAJ6OKHJgQe4TAkF%2B8Rh%2B2yrSUaDW4tKRZK2nlMELTNFJMr0gAgQtoS%2BH1vwegOebNAgn9JrguCYjr%2B0k1OyWJDDpPalpHgnUlfvsvhsGqc51jcBUvAHF25UdZm1Y2loymG0PRMG2tGBULTT%2FQW1BwbZwO7uVxrgCuzK3k8dHidy%2B2B8VyrtLlHewCVzI0dh&X-Amz-Signature=35f2e8dd61e59ef6be0d71496c7dd39295a10fb8cdc724e6d30dbf9792d08d2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RANFNGLV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRP%2FKTqLps3gnp4B6ptBnw2oCAslErsDciPX21tQlqDAIhAL6Vy2JRq8GTF7gz4zCrTaJJ7CVwYbZxaVmDjdf5B8PqKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyA6pawA%2F5KvoE8fRsq3AMuNryNaCr98H0PFxulHMt%2BAo37ORLGHAxLNm9LqH%2FFGmbcLxZ4ZsITQ2CBFHQ67WjfNFdIg79x724NpkIG9gDoMroiWPo5e3XGhZsHKeG05t1ll66iNkpAM7Khdr1XTHGR17CX1ju7bVRputU%2FWFYUxpy62FAoYcLJXLnJzSS1%2F%2By9q2KfHNgibyQNylrzl3qYcB9euDJyFm6%2FqtgTD23KJvI3AKEilFb%2FhXFB6MK4M%2F1h7o9PbyveuhuYu6WmT9cKayqeJDVDSSbHcEiWYO7l7TrsZ048K4uZvXnNLg0el0Z%2FBiC8cB75AW7Dmg14cIDrwd1ocbyrrKS%2BLTrGTsVTqgq21qh8aosJGeGnQXw64PgNjA%2FDfaDNOKLEEtLVXdOM9vWv8y60ycwlP%2FAkVx4lKDdjPICOxqxRdB43EzUkFdnstAv3uK1PQGpddASki7VTT7NEXbov15qCCTl3OSNdB62Vj2b2RwaqEYkFAW%2Fh8103plDYUxrFO4vaYHVVLEN3GtODMpY4D6bmInRaHW%2B8EuT2rJBmMAc1vXbjPV5Jh261N8VBU2QP48CVLCEq4LdBj5a1VDW7ganRhPRiRLMbFb1P85kJ8hgVrOU1MZ9ERjk7vDGCcWHvwgaJdjCAl%2Bu8BjqkAcUfalwdiymkPQqNJ1YxwcfAm172EAJ6OKHJgQe4TAkF%2B8Rh%2B2yrSUaDW4tKRZK2nlMELTNFJMr0gAgQtoS%2BH1vwegOebNAgn9JrguCYjr%2B0k1OyWJDDpPalpHgnUlfvsvhsGqc51jcBUvAHF25UdZm1Y2loymG0PRMG2tGBULTT%2FQW1BwbZwO7uVxrgCuzK3k8dHidy%2B2B8VyrtLlHewCVzI0dh&X-Amz-Signature=22e7ac68c42645551bd9119017b239a282f3d0fd8768d2c261664e5c7cf919d2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RANFNGLV%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRP%2FKTqLps3gnp4B6ptBnw2oCAslErsDciPX21tQlqDAIhAL6Vy2JRq8GTF7gz4zCrTaJJ7CVwYbZxaVmDjdf5B8PqKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyA6pawA%2F5KvoE8fRsq3AMuNryNaCr98H0PFxulHMt%2BAo37ORLGHAxLNm9LqH%2FFGmbcLxZ4ZsITQ2CBFHQ67WjfNFdIg79x724NpkIG9gDoMroiWPo5e3XGhZsHKeG05t1ll66iNkpAM7Khdr1XTHGR17CX1ju7bVRputU%2FWFYUxpy62FAoYcLJXLnJzSS1%2F%2By9q2KfHNgibyQNylrzl3qYcB9euDJyFm6%2FqtgTD23KJvI3AKEilFb%2FhXFB6MK4M%2F1h7o9PbyveuhuYu6WmT9cKayqeJDVDSSbHcEiWYO7l7TrsZ048K4uZvXnNLg0el0Z%2FBiC8cB75AW7Dmg14cIDrwd1ocbyrrKS%2BLTrGTsVTqgq21qh8aosJGeGnQXw64PgNjA%2FDfaDNOKLEEtLVXdOM9vWv8y60ycwlP%2FAkVx4lKDdjPICOxqxRdB43EzUkFdnstAv3uK1PQGpddASki7VTT7NEXbov15qCCTl3OSNdB62Vj2b2RwaqEYkFAW%2Fh8103plDYUxrFO4vaYHVVLEN3GtODMpY4D6bmInRaHW%2B8EuT2rJBmMAc1vXbjPV5Jh261N8VBU2QP48CVLCEq4LdBj5a1VDW7ganRhPRiRLMbFb1P85kJ8hgVrOU1MZ9ERjk7vDGCcWHvwgaJdjCAl%2Bu8BjqkAcUfalwdiymkPQqNJ1YxwcfAm172EAJ6OKHJgQe4TAkF%2B8Rh%2B2yrSUaDW4tKRZK2nlMELTNFJMr0gAgQtoS%2BH1vwegOebNAgn9JrguCYjr%2B0k1OyWJDDpPalpHgnUlfvsvhsGqc51jcBUvAHF25UdZm1Y2loymG0PRMG2tGBULTT%2FQW1BwbZwO7uVxrgCuzK3k8dHidy%2B2B8VyrtLlHewCVzI0dh&X-Amz-Signature=54c5ce707abb41850fe18b1e7d82056ad0419d7e2374601f968f3e80e1558902&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ7Q7WDZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOz1ZhtTJII7tmvKeyNHSMrHUwxznQXXHUZV7Hl9BWfAIgVzmJuBnKfYCyfruCj%2BYoHPyfqJIhDRkGaHNnHoFRRd8qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMpCVG1s7N8YHtN6pyrcA0lu%2FPMuPDmauHePexX8rigCXnf3MheOX4QpMCaW%2Bhh6UsvpYKacNvU%2FKt3z205VqpEgQ6cDuFww%2FxMLbAThJHvPVPzcF%2FuhacvmlFBoDXW4yEsfwKn6StUDoRlpZZYjWaG9hh7rTEGoetgLuTOwjpV%2BQtrXAE0oAl3HJQ3HEi7nfh8XbY%2BUrnTuBFASPRWeGTCF239K2JRj5ZASEHzgm0S8VKD%2BwBRLPT%2BqcqKEsuy%2FSMqE%2BK5WFr3o13rkGg2h8Gf6INwofr4cs%2F74Ik8jRVIRBeLuSIbej9vJm8niTNajv3XAGbvvHzvGdu2diRbgJhF9ynNoXTaFl72LVWClGn1xJHTVHCC0Sb7Eb9pFzTifcssnuye3TmrH%2B9hyVUEr8lqlf01Lgyy1xyy3MstPRVdSoxn0k%2BXHleMaOCwbOhyNr6%2FSsvwg%2Btgde0GMT6dj3qH2LhBk8rxbn9NncHr0L2w%2BvVi5g5%2FJmTlk5disDBaHVwJ5kS%2BMdXOjEt7oWicJc%2BVqKkUtF1IFe6UzBASywpqB4PsFtXG7wyJZ6N7Id544CGuEx1RLW2aE6l1%2BJPjLtb5ylzEf%2F4F5aA%2BhSucKnEz9gSZ%2FcYrM1849w%2BL%2FtSzXgQlKg3s07HwZ%2FL23MKmX67wGOqUBZSlTV6oHG76hyyNF2FzEAe6WOSL7%2BD8alRL3O6QGp%2BxOwlgyEpvDen4xOSxyImI%2FxGoBOMz%2F6VWszZnDrMAJz5Uf6gOpyFL%2BEMKVNkTGmiaWkQ%2FlZdv%2FxSDGsexKRPeQTqmfk%2B2CJUUfSPtCRxjF8%2Fisz4YE%2FedC0NvwxCirmK3h49kRbkfQ5K0yCkLwiqYNy5GuDqZ1LxftIHOE4NvyoA%2BtS9IB&X-Amz-Signature=d8079ec488679e2c8dabd3ac63377d271ee1cb560c7e065da0ffe4a4578e4623&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP3FSHSG%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJqMWpDsMzRp3KIPhT9odiiSHYpz%2FPlXsCDXUE6t2zJQIgfksxKi2vqpEmWSvZGIwM4G6shtDZdTkHszFVUnK0gyYqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiP%2F9%2BRX71QAosyXircA11t0dZlI%2FJCJfTFEUuUpOvI%2BkCwrWmrcaPiebZY7eW7B32FKcRsjyEBxMYEYSUXOcOhaBjh31QLAZguvDOFTD7G68OWQbB0GO5iGgxeHUrDTFCaPhBtXdZJAdkUxRVEycgyYgQQ1snBNq0weEbQk1IHbtueLfJOIseIjCu%2BKHH7e3Zu0WaZGC%2B2fWnCRh9f8LCIFNu9lVD08xDh8R9%2FFHTHSCYhMCoGmmWGco112LuPxYjGCnXz1CO%2FBhryPHqdLhXmCsy%2FuRJkLb7uFiNFjdZBpvhI7TT1H8h4tnpve4EMl7oUEzAmyFBze5EHy4L22QqYqTMnR4HV0nC4SIxd8KJObVYcc1rsB5xYxQVD3x08oSxb0fYlaRHu32%2B5fWnplz2G6mL0l1dPf6bJciyZAYgP4v5twfH9D6t79qqUnkW%2B%2FxSNjjCSVgU1mxS7E1D0msrTNe3I%2FghbCDklmnLcSch2a9BnsQ6SSyJf8CZ0L953QWvMywy4WmFyxY3ivFopU0wSNFv9A8rj2Co%2BqbhsioQMpF%2F%2FR7GK5rv1VBlrwQDYvtHYnVziA2H1k9MGvHVWDPzfcFoLRtYC6RG941xR8ZPFMoHOh31VaQ5698gAj1X93xeTF2YH9dpo2vbrMOSW67wGOqUBUXBW%2FfLisjQlYh3Zfh3ZK3nDLItkU5j%2BrYtVYdn%2BGP%2F0MYVurI3olx2IRysg1C790dJPvR2JW4jMt4whf7N0U6UcDHxlwXhsJn96UVVGoOAUTeuuPyuiR7m7qhrQ51FHYxg5mP7M84ofdmuVho9ymB%2F7ZlG%2BO%2B99WL7Du3nY3fpB6AAkUTihkzzLUzzlc33BtRNPn86hk0jyR0qYYFsit%2B7fks3P&X-Amz-Signature=ddc732a049c93f667c77d97bbbd7eeffd32a6e24e9d00f12e99b71fb4052912b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBT7TFZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBaepRRyYhwcbhQ5pDOEXH7kSbxVTcwaqpcbU86tEvjLAiEAhtvtxZbhmGM34Z2XGDvSp73KooZffEql8HfmqT36xW4qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLETEKL0Nb%2F2s4vlZSrcAytdycAZMQe7R93kU6yJqdY9CHmJ6VYL7Jf5dI2eKSF%2BDhJfynoLL7wFY1lZ2lvOC86q6qwJD29jOEQ1GF7z7fVMFCj8S0RyvaI7lhQRgWnDzH9peODT1UclG5BkK8d4Xq9ZpCQ4w5fOcqhl4mR68BeIuS59d39vFGmbjk%2FIFXEWFkoFC2ue%2BaH849g6av8OfAyocBKaIKaMkjYetr4cfQCP9EM6r9c4fqxzk9%2FLKTi1PHxj0l4tqG%2FHJ8kikS7a3Dy3L1eleje0yyLNSP2%2FhBFcWRaxnBmc7XsFA27bTMrpx5gGClNKBDYN3AsB4h6IWWk07Aav8W5OdnK4ySE1tmA%2Fv50srDdj%2BS0Rkk3FxCAmCfcxnbiGlyx3ARt7Axsw0xULq6qDhGiXp0usPXrouUo2%2BBkwcKv%2BLRgU3F454e7aOg%2BApEaqdcfIF%2BR5jZ%2BnFFbW%2BkJAz%2FzCamEVpO003hRDkRzF9vesDl6MJ%2FipfpSEAsxZ4rhZLiSD4D0WGvM8Z%2Bfkvsps9fGhmKvlsTjhQAFSe2m2uPXIrLYpytowcL93cqHkfsWiAID1GgEdIlvGz6lyFwEZvEdbG2sHYNonnm%2FIRR%2FDJywWsw0GvxIxTaVE2AOh3NKhBebHXfLZMLGW67wGOqUBx5ppdF8I8IzUgnCyVyx76e0CUFjsEMDik5%2BJYS2%2FNPC2d5J9ogFhCZ0hInWwsX361iCZe%2BjgACGlR9Cgwj2bJh03FEUVBtsoa4nFsiCtEkPmzS3tujGz103JxP5kvpCcMnUrSOPY12M50vDaLWTBM8Tf9M0TPoLN%2FIC8MXr126FaRJMWIDFnsUuXVJuZRqeHTOFZ1neWdfeq%2FfS8PFT4SwQBsadw&X-Amz-Signature=46d7f943817040680cec7896c5866f957e77c5dcc965639ca6534f3365950ed3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBBT7TFZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBaepRRyYhwcbhQ5pDOEXH7kSbxVTcwaqpcbU86tEvjLAiEAhtvtxZbhmGM34Z2XGDvSp73KooZffEql8HfmqT36xW4qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLETEKL0Nb%2F2s4vlZSrcAytdycAZMQe7R93kU6yJqdY9CHmJ6VYL7Jf5dI2eKSF%2BDhJfynoLL7wFY1lZ2lvOC86q6qwJD29jOEQ1GF7z7fVMFCj8S0RyvaI7lhQRgWnDzH9peODT1UclG5BkK8d4Xq9ZpCQ4w5fOcqhl4mR68BeIuS59d39vFGmbjk%2FIFXEWFkoFC2ue%2BaH849g6av8OfAyocBKaIKaMkjYetr4cfQCP9EM6r9c4fqxzk9%2FLKTi1PHxj0l4tqG%2FHJ8kikS7a3Dy3L1eleje0yyLNSP2%2FhBFcWRaxnBmc7XsFA27bTMrpx5gGClNKBDYN3AsB4h6IWWk07Aav8W5OdnK4ySE1tmA%2Fv50srDdj%2BS0Rkk3FxCAmCfcxnbiGlyx3ARt7Axsw0xULq6qDhGiXp0usPXrouUo2%2BBkwcKv%2BLRgU3F454e7aOg%2BApEaqdcfIF%2BR5jZ%2BnFFbW%2BkJAz%2FzCamEVpO003hRDkRzF9vesDl6MJ%2FipfpSEAsxZ4rhZLiSD4D0WGvM8Z%2Bfkvsps9fGhmKvlsTjhQAFSe2m2uPXIrLYpytowcL93cqHkfsWiAID1GgEdIlvGz6lyFwEZvEdbG2sHYNonnm%2FIRR%2FDJywWsw0GvxIxTaVE2AOh3NKhBebHXfLZMLGW67wGOqUBx5ppdF8I8IzUgnCyVyx76e0CUFjsEMDik5%2BJYS2%2FNPC2d5J9ogFhCZ0hInWwsX361iCZe%2BjgACGlR9Cgwj2bJh03FEUVBtsoa4nFsiCtEkPmzS3tujGz103JxP5kvpCcMnUrSOPY12M50vDaLWTBM8Tf9M0TPoLN%2FIC8MXr126FaRJMWIDFnsUuXVJuZRqeHTOFZ1neWdfeq%2FfS8PFT4SwQBsadw&X-Amz-Signature=62b160948f990b8e197786734eb7a7b1ea26cde56c07007fb05b4524131a4f25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
