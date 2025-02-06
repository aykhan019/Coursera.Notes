

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6DHEX3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDohfYmVTXhB2fsj63%2Fa6y8i7yI9kyqNDoVO56AI9gt1gIgBkkomFXoEnbA8bpFzQ3X6QbnzJubRM04Tx6KHn3FwjMq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDBdv7HQ7aLJvmhG2KyrcA9zyPvcRmXXKv4MSv%2FHbhaeSrASfcCDfn2MgOmzXd%2BAJnrVngP6xxMjBMMY6z8E9O9eTQJCMuWFmePv6w3b9njkV0Ljm4oqhC6gUl3A7JyRnXCt0oMyNjvmW8re4T59%2F2pIAx%2BdCdHhRdyQ5mohNnb2z810mDBlC2BO%2BpveLrJ6oPKOIKVFC4XAfyDn7m3MsoPTUV6PoHasmRIrf5i%2FbI5cdhzW1b5llioBKtNE9yQ5A%2Be89PKYrJMFOzD06NX3BgQh5G3l9m3sBlf61%2B7BCVAeD4ZKYG%2BCglxdHGSoZCgjWPjZuezq70hh8boQW2RiHta1GA4nED7mF%2BNMw77fi22IIozfw%2BPp5CMsqJu6g94cKnVkUARwPA%2BOya%2FrkaTtp6m6Nxtx2Z4IWWo%2FN9vOpK86ulVjPVlFD66WFGIaJPTi9klSOsXbjHNS8r9Xgc%2BFauhRh75XFlAUNGRrZd%2F8GoCs6W%2BWN8GMVrajRV%2Fd6of9NLJNUb5ZMe%2FN1XcFA67dYUW1Spb1OALriV00hFDTvD0jPsTmHGeblO9mm7ef1Vcw16%2FRLpd8%2B64VrbMxcMu4lAzX1GksSxOawiRbxGOQdrDUo34UDZ7%2BxVGN3yDQVzuqDJ8V9BMiZulKCvD2AMIzEkr0GOqUB9fRcMVk%2FLSsje673EjgeWix89ABEvqk7qVcc86kVUH2IwVNQWPT40JE%2FndwXtemRzJcJ%2F%2Bv62Vr7lqZ53%2BlleaW6jlx1ylInLhu0eQSeyaXafNXHpYS5UTSXefc9Mt49ZGhP44I%2FrG9wOFBT33o50POGt%2F9%2BFY%2BZHmnSBKBCthQpVfsdjgVTLOmrM5jPh%2BfPCgLFKCzku%2FD6Da7uAeGLRV%2FuGerJ&X-Amz-Signature=e24bd8f9e3bb10662efc4ab22cbeac006d15dce1e5ddc2dd8b0e56f785493b3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6DHEX3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDohfYmVTXhB2fsj63%2Fa6y8i7yI9kyqNDoVO56AI9gt1gIgBkkomFXoEnbA8bpFzQ3X6QbnzJubRM04Tx6KHn3FwjMq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDBdv7HQ7aLJvmhG2KyrcA9zyPvcRmXXKv4MSv%2FHbhaeSrASfcCDfn2MgOmzXd%2BAJnrVngP6xxMjBMMY6z8E9O9eTQJCMuWFmePv6w3b9njkV0Ljm4oqhC6gUl3A7JyRnXCt0oMyNjvmW8re4T59%2F2pIAx%2BdCdHhRdyQ5mohNnb2z810mDBlC2BO%2BpveLrJ6oPKOIKVFC4XAfyDn7m3MsoPTUV6PoHasmRIrf5i%2FbI5cdhzW1b5llioBKtNE9yQ5A%2Be89PKYrJMFOzD06NX3BgQh5G3l9m3sBlf61%2B7BCVAeD4ZKYG%2BCglxdHGSoZCgjWPjZuezq70hh8boQW2RiHta1GA4nED7mF%2BNMw77fi22IIozfw%2BPp5CMsqJu6g94cKnVkUARwPA%2BOya%2FrkaTtp6m6Nxtx2Z4IWWo%2FN9vOpK86ulVjPVlFD66WFGIaJPTi9klSOsXbjHNS8r9Xgc%2BFauhRh75XFlAUNGRrZd%2F8GoCs6W%2BWN8GMVrajRV%2Fd6of9NLJNUb5ZMe%2FN1XcFA67dYUW1Spb1OALriV00hFDTvD0jPsTmHGeblO9mm7ef1Vcw16%2FRLpd8%2B64VrbMxcMu4lAzX1GksSxOawiRbxGOQdrDUo34UDZ7%2BxVGN3yDQVzuqDJ8V9BMiZulKCvD2AMIzEkr0GOqUB9fRcMVk%2FLSsje673EjgeWix89ABEvqk7qVcc86kVUH2IwVNQWPT40JE%2FndwXtemRzJcJ%2F%2Bv62Vr7lqZ53%2BlleaW6jlx1ylInLhu0eQSeyaXafNXHpYS5UTSXefc9Mt49ZGhP44I%2FrG9wOFBT33o50POGt%2F9%2BFY%2BZHmnSBKBCthQpVfsdjgVTLOmrM5jPh%2BfPCgLFKCzku%2FD6Da7uAeGLRV%2FuGerJ&X-Amz-Signature=039677871cac17560400acf5dcf9404c75ab72f727b9f6655db6aa6a6326a57f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6DHEX3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDohfYmVTXhB2fsj63%2Fa6y8i7yI9kyqNDoVO56AI9gt1gIgBkkomFXoEnbA8bpFzQ3X6QbnzJubRM04Tx6KHn3FwjMq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDBdv7HQ7aLJvmhG2KyrcA9zyPvcRmXXKv4MSv%2FHbhaeSrASfcCDfn2MgOmzXd%2BAJnrVngP6xxMjBMMY6z8E9O9eTQJCMuWFmePv6w3b9njkV0Ljm4oqhC6gUl3A7JyRnXCt0oMyNjvmW8re4T59%2F2pIAx%2BdCdHhRdyQ5mohNnb2z810mDBlC2BO%2BpveLrJ6oPKOIKVFC4XAfyDn7m3MsoPTUV6PoHasmRIrf5i%2FbI5cdhzW1b5llioBKtNE9yQ5A%2Be89PKYrJMFOzD06NX3BgQh5G3l9m3sBlf61%2B7BCVAeD4ZKYG%2BCglxdHGSoZCgjWPjZuezq70hh8boQW2RiHta1GA4nED7mF%2BNMw77fi22IIozfw%2BPp5CMsqJu6g94cKnVkUARwPA%2BOya%2FrkaTtp6m6Nxtx2Z4IWWo%2FN9vOpK86ulVjPVlFD66WFGIaJPTi9klSOsXbjHNS8r9Xgc%2BFauhRh75XFlAUNGRrZd%2F8GoCs6W%2BWN8GMVrajRV%2Fd6of9NLJNUb5ZMe%2FN1XcFA67dYUW1Spb1OALriV00hFDTvD0jPsTmHGeblO9mm7ef1Vcw16%2FRLpd8%2B64VrbMxcMu4lAzX1GksSxOawiRbxGOQdrDUo34UDZ7%2BxVGN3yDQVzuqDJ8V9BMiZulKCvD2AMIzEkr0GOqUB9fRcMVk%2FLSsje673EjgeWix89ABEvqk7qVcc86kVUH2IwVNQWPT40JE%2FndwXtemRzJcJ%2F%2Bv62Vr7lqZ53%2BlleaW6jlx1ylInLhu0eQSeyaXafNXHpYS5UTSXefc9Mt49ZGhP44I%2FrG9wOFBT33o50POGt%2F9%2BFY%2BZHmnSBKBCthQpVfsdjgVTLOmrM5jPh%2BfPCgLFKCzku%2FD6Da7uAeGLRV%2FuGerJ&X-Amz-Signature=89de2619f6ee86991bf15d203d83841bc16def93a6a697546d68ff01d74c00f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6DHEX3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDohfYmVTXhB2fsj63%2Fa6y8i7yI9kyqNDoVO56AI9gt1gIgBkkomFXoEnbA8bpFzQ3X6QbnzJubRM04Tx6KHn3FwjMq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDBdv7HQ7aLJvmhG2KyrcA9zyPvcRmXXKv4MSv%2FHbhaeSrASfcCDfn2MgOmzXd%2BAJnrVngP6xxMjBMMY6z8E9O9eTQJCMuWFmePv6w3b9njkV0Ljm4oqhC6gUl3A7JyRnXCt0oMyNjvmW8re4T59%2F2pIAx%2BdCdHhRdyQ5mohNnb2z810mDBlC2BO%2BpveLrJ6oPKOIKVFC4XAfyDn7m3MsoPTUV6PoHasmRIrf5i%2FbI5cdhzW1b5llioBKtNE9yQ5A%2Be89PKYrJMFOzD06NX3BgQh5G3l9m3sBlf61%2B7BCVAeD4ZKYG%2BCglxdHGSoZCgjWPjZuezq70hh8boQW2RiHta1GA4nED7mF%2BNMw77fi22IIozfw%2BPp5CMsqJu6g94cKnVkUARwPA%2BOya%2FrkaTtp6m6Nxtx2Z4IWWo%2FN9vOpK86ulVjPVlFD66WFGIaJPTi9klSOsXbjHNS8r9Xgc%2BFauhRh75XFlAUNGRrZd%2F8GoCs6W%2BWN8GMVrajRV%2Fd6of9NLJNUb5ZMe%2FN1XcFA67dYUW1Spb1OALriV00hFDTvD0jPsTmHGeblO9mm7ef1Vcw16%2FRLpd8%2B64VrbMxcMu4lAzX1GksSxOawiRbxGOQdrDUo34UDZ7%2BxVGN3yDQVzuqDJ8V9BMiZulKCvD2AMIzEkr0GOqUB9fRcMVk%2FLSsje673EjgeWix89ABEvqk7qVcc86kVUH2IwVNQWPT40JE%2FndwXtemRzJcJ%2F%2Bv62Vr7lqZ53%2BlleaW6jlx1ylInLhu0eQSeyaXafNXHpYS5UTSXefc9Mt49ZGhP44I%2FrG9wOFBT33o50POGt%2F9%2BFY%2BZHmnSBKBCthQpVfsdjgVTLOmrM5jPh%2BfPCgLFKCzku%2FD6Da7uAeGLRV%2FuGerJ&X-Amz-Signature=21f565959bd94ec75d07de330aa60cc98e19a8d180b21cc41b3c0b8a0cd1500f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6DHEX3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDohfYmVTXhB2fsj63%2Fa6y8i7yI9kyqNDoVO56AI9gt1gIgBkkomFXoEnbA8bpFzQ3X6QbnzJubRM04Tx6KHn3FwjMq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDBdv7HQ7aLJvmhG2KyrcA9zyPvcRmXXKv4MSv%2FHbhaeSrASfcCDfn2MgOmzXd%2BAJnrVngP6xxMjBMMY6z8E9O9eTQJCMuWFmePv6w3b9njkV0Ljm4oqhC6gUl3A7JyRnXCt0oMyNjvmW8re4T59%2F2pIAx%2BdCdHhRdyQ5mohNnb2z810mDBlC2BO%2BpveLrJ6oPKOIKVFC4XAfyDn7m3MsoPTUV6PoHasmRIrf5i%2FbI5cdhzW1b5llioBKtNE9yQ5A%2Be89PKYrJMFOzD06NX3BgQh5G3l9m3sBlf61%2B7BCVAeD4ZKYG%2BCglxdHGSoZCgjWPjZuezq70hh8boQW2RiHta1GA4nED7mF%2BNMw77fi22IIozfw%2BPp5CMsqJu6g94cKnVkUARwPA%2BOya%2FrkaTtp6m6Nxtx2Z4IWWo%2FN9vOpK86ulVjPVlFD66WFGIaJPTi9klSOsXbjHNS8r9Xgc%2BFauhRh75XFlAUNGRrZd%2F8GoCs6W%2BWN8GMVrajRV%2Fd6of9NLJNUb5ZMe%2FN1XcFA67dYUW1Spb1OALriV00hFDTvD0jPsTmHGeblO9mm7ef1Vcw16%2FRLpd8%2B64VrbMxcMu4lAzX1GksSxOawiRbxGOQdrDUo34UDZ7%2BxVGN3yDQVzuqDJ8V9BMiZulKCvD2AMIzEkr0GOqUB9fRcMVk%2FLSsje673EjgeWix89ABEvqk7qVcc86kVUH2IwVNQWPT40JE%2FndwXtemRzJcJ%2F%2Bv62Vr7lqZ53%2BlleaW6jlx1ylInLhu0eQSeyaXafNXHpYS5UTSXefc9Mt49ZGhP44I%2FrG9wOFBT33o50POGt%2F9%2BFY%2BZHmnSBKBCthQpVfsdjgVTLOmrM5jPh%2BfPCgLFKCzku%2FD6Da7uAeGLRV%2FuGerJ&X-Amz-Signature=bee9b090b3c3a0d7490131b56b56ef75867d9429a7472ab575b8f60a5bf856e9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6DHEX3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDohfYmVTXhB2fsj63%2Fa6y8i7yI9kyqNDoVO56AI9gt1gIgBkkomFXoEnbA8bpFzQ3X6QbnzJubRM04Tx6KHn3FwjMq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDBdv7HQ7aLJvmhG2KyrcA9zyPvcRmXXKv4MSv%2FHbhaeSrASfcCDfn2MgOmzXd%2BAJnrVngP6xxMjBMMY6z8E9O9eTQJCMuWFmePv6w3b9njkV0Ljm4oqhC6gUl3A7JyRnXCt0oMyNjvmW8re4T59%2F2pIAx%2BdCdHhRdyQ5mohNnb2z810mDBlC2BO%2BpveLrJ6oPKOIKVFC4XAfyDn7m3MsoPTUV6PoHasmRIrf5i%2FbI5cdhzW1b5llioBKtNE9yQ5A%2Be89PKYrJMFOzD06NX3BgQh5G3l9m3sBlf61%2B7BCVAeD4ZKYG%2BCglxdHGSoZCgjWPjZuezq70hh8boQW2RiHta1GA4nED7mF%2BNMw77fi22IIozfw%2BPp5CMsqJu6g94cKnVkUARwPA%2BOya%2FrkaTtp6m6Nxtx2Z4IWWo%2FN9vOpK86ulVjPVlFD66WFGIaJPTi9klSOsXbjHNS8r9Xgc%2BFauhRh75XFlAUNGRrZd%2F8GoCs6W%2BWN8GMVrajRV%2Fd6of9NLJNUb5ZMe%2FN1XcFA67dYUW1Spb1OALriV00hFDTvD0jPsTmHGeblO9mm7ef1Vcw16%2FRLpd8%2B64VrbMxcMu4lAzX1GksSxOawiRbxGOQdrDUo34UDZ7%2BxVGN3yDQVzuqDJ8V9BMiZulKCvD2AMIzEkr0GOqUB9fRcMVk%2FLSsje673EjgeWix89ABEvqk7qVcc86kVUH2IwVNQWPT40JE%2FndwXtemRzJcJ%2F%2Bv62Vr7lqZ53%2BlleaW6jlx1ylInLhu0eQSeyaXafNXHpYS5UTSXefc9Mt49ZGhP44I%2FrG9wOFBT33o50POGt%2F9%2BFY%2BZHmnSBKBCthQpVfsdjgVTLOmrM5jPh%2BfPCgLFKCzku%2FD6Da7uAeGLRV%2FuGerJ&X-Amz-Signature=8fd6ac8e82c49fbd9a58b2121425db1d6fed6ef826519c9761ac7f1a243b21ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6DHEX3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDohfYmVTXhB2fsj63%2Fa6y8i7yI9kyqNDoVO56AI9gt1gIgBkkomFXoEnbA8bpFzQ3X6QbnzJubRM04Tx6KHn3FwjMq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDBdv7HQ7aLJvmhG2KyrcA9zyPvcRmXXKv4MSv%2FHbhaeSrASfcCDfn2MgOmzXd%2BAJnrVngP6xxMjBMMY6z8E9O9eTQJCMuWFmePv6w3b9njkV0Ljm4oqhC6gUl3A7JyRnXCt0oMyNjvmW8re4T59%2F2pIAx%2BdCdHhRdyQ5mohNnb2z810mDBlC2BO%2BpveLrJ6oPKOIKVFC4XAfyDn7m3MsoPTUV6PoHasmRIrf5i%2FbI5cdhzW1b5llioBKtNE9yQ5A%2Be89PKYrJMFOzD06NX3BgQh5G3l9m3sBlf61%2B7BCVAeD4ZKYG%2BCglxdHGSoZCgjWPjZuezq70hh8boQW2RiHta1GA4nED7mF%2BNMw77fi22IIozfw%2BPp5CMsqJu6g94cKnVkUARwPA%2BOya%2FrkaTtp6m6Nxtx2Z4IWWo%2FN9vOpK86ulVjPVlFD66WFGIaJPTi9klSOsXbjHNS8r9Xgc%2BFauhRh75XFlAUNGRrZd%2F8GoCs6W%2BWN8GMVrajRV%2Fd6of9NLJNUb5ZMe%2FN1XcFA67dYUW1Spb1OALriV00hFDTvD0jPsTmHGeblO9mm7ef1Vcw16%2FRLpd8%2B64VrbMxcMu4lAzX1GksSxOawiRbxGOQdrDUo34UDZ7%2BxVGN3yDQVzuqDJ8V9BMiZulKCvD2AMIzEkr0GOqUB9fRcMVk%2FLSsje673EjgeWix89ABEvqk7qVcc86kVUH2IwVNQWPT40JE%2FndwXtemRzJcJ%2F%2Bv62Vr7lqZ53%2BlleaW6jlx1ylInLhu0eQSeyaXafNXHpYS5UTSXefc9Mt49ZGhP44I%2FrG9wOFBT33o50POGt%2F9%2BFY%2BZHmnSBKBCthQpVfsdjgVTLOmrM5jPh%2BfPCgLFKCzku%2FD6Da7uAeGLRV%2FuGerJ&X-Amz-Signature=f8c1734e55ebadc5faa3aa2fd9fab38ea59fd49e5eda28d0108b1b54e8541e71&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6DHEX3R%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDohfYmVTXhB2fsj63%2Fa6y8i7yI9kyqNDoVO56AI9gt1gIgBkkomFXoEnbA8bpFzQ3X6QbnzJubRM04Tx6KHn3FwjMq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDBdv7HQ7aLJvmhG2KyrcA9zyPvcRmXXKv4MSv%2FHbhaeSrASfcCDfn2MgOmzXd%2BAJnrVngP6xxMjBMMY6z8E9O9eTQJCMuWFmePv6w3b9njkV0Ljm4oqhC6gUl3A7JyRnXCt0oMyNjvmW8re4T59%2F2pIAx%2BdCdHhRdyQ5mohNnb2z810mDBlC2BO%2BpveLrJ6oPKOIKVFC4XAfyDn7m3MsoPTUV6PoHasmRIrf5i%2FbI5cdhzW1b5llioBKtNE9yQ5A%2Be89PKYrJMFOzD06NX3BgQh5G3l9m3sBlf61%2B7BCVAeD4ZKYG%2BCglxdHGSoZCgjWPjZuezq70hh8boQW2RiHta1GA4nED7mF%2BNMw77fi22IIozfw%2BPp5CMsqJu6g94cKnVkUARwPA%2BOya%2FrkaTtp6m6Nxtx2Z4IWWo%2FN9vOpK86ulVjPVlFD66WFGIaJPTi9klSOsXbjHNS8r9Xgc%2BFauhRh75XFlAUNGRrZd%2F8GoCs6W%2BWN8GMVrajRV%2Fd6of9NLJNUb5ZMe%2FN1XcFA67dYUW1Spb1OALriV00hFDTvD0jPsTmHGeblO9mm7ef1Vcw16%2FRLpd8%2B64VrbMxcMu4lAzX1GksSxOawiRbxGOQdrDUo34UDZ7%2BxVGN3yDQVzuqDJ8V9BMiZulKCvD2AMIzEkr0GOqUB9fRcMVk%2FLSsje673EjgeWix89ABEvqk7qVcc86kVUH2IwVNQWPT40JE%2FndwXtemRzJcJ%2F%2Bv62Vr7lqZ53%2BlleaW6jlx1ylInLhu0eQSeyaXafNXHpYS5UTSXefc9Mt49ZGhP44I%2FrG9wOFBT33o50POGt%2F9%2BFY%2BZHmnSBKBCthQpVfsdjgVTLOmrM5jPh%2BfPCgLFKCzku%2FD6Da7uAeGLRV%2FuGerJ&X-Amz-Signature=a432ad7595d9a7299135f46489f0b0778c9a6010cb8a3c0f7eb3057ead562f2c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUTIMVPM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIBqVGc26kuMLESL4YZUV3LcSBo1navrHo%2BPUhCipr58fAiAJ0Hgm2P2JvqNAGy%2B7POG5%2FVBfwnLcNAYqsychpvsP3Sr%2FAwhdEAAaDDYzNzQyMzE4MzgwNSIMxYRAxWqUmh6p9f63KtwDz5Bj9knSAuq5CsEIaLdHneY%2FtU1v9w5DURAaguNqGXBqPtle97R4QvU9uSmCDoPNUNj7hUCQA2AvTqCuKpReJgVyNbVp1FH%2BlJISyBpr5PbSuAy4hInfnx4j9XUeFko9LV7KwR7%2B4Wke9qcvtqaHvkSobBORojqEJl%2Fypk05DKa%2BQSBX%2FVau36SLowFtDekz742xKCv17p1pegOHUKgHEyL2DBOT6w5RJzMwyglyOXQvV1dXbf5HbHmUdvI5xMYlZWly3tG1QoBbpKYZviYx7xITwS3MpoHdR82yEojc3nXSggbSPspsbXxAb9C%2BS718xxMxB7JYaSnGmLljADGeQg5yoG3Pk9t5iKJpWwumsdX0no1a5ItO710hQa7Dc4J5E6QhRkTHXdjhImUuBspuN6jYF2ba%2Bz6uHq4ZcPdJ9jvSJzXXxhylWGAA3tfCa%2BoyPwTHKuf0w1mYZzfIsLjFGjfYsIBKKiHXakvFifuJOCWzMywXSXKMU1A%2FyxXkKF18cEpqf45REPUNdcSilRiOlv5whtXGJH1fuxgIbfRdjo94lZ72oXM0FFChyNQcm32e0zVH%2BpfpddaGjCKKRBkjXfjiovz16coDVTaWRjg%2FFNJP0yn2y7%2BC5jhExCYw78iSvQY6pgHOXoKN0O%2FcDoF3dPN%2FQpK7MHleGWB8TGVhhDHzeg6Z9GoHsFiRs5bOcOc08nxrkEBFIahRGRwI8Psks5Z18L7UKE66wgDu5tgJIeMSplTaZeX2o%2BUVxrtlCKdBez5hz2iBMHzSryVe1%2FYSY4zJ4mtSIcDyoOsx4j5mjizD%2FKmSwzo9ss71qyeHANh2gjXhKBLknmIGElI5pSthblxA0939I2wI2JLI&X-Amz-Signature=191adb28a71b32a150c6257a740e5d5c2718e0b7dcfc0591ecbac847eeda7171&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTPTYKJS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQC0LFPBn%2BRAXRhd3ru5GKLMTxG0bkOZ5LyaQ6kx1YN2GgIgATjEt9GEswBCXX3KpC463jNF8DV9%2FUnaheMATY4ueXQq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHEMnCn%2B55mpR7tXXircA209%2BwMxXtoC8gMfZczdm5eLkhXCdHtSF6wnIBj9L2uJFDDhyK4axO1Uqd%2Fu3XEpCliJ80a%2BFYOde9o89yFGyK3igwXSWpyM0XbwNM%2BRaUGt%2BJU7H4EUh6upuDjhhwoeSvwcYTtRM5%2BTzbEvWdmmZw9Z01dJIqEa2TXNrb5CUNU115MqsZ8NzFi%2BlgoxxuMH0WM%2BUgkHHt4iKqjYZT3imKHcLwo2pToCRuTcH6jphqHLO%2FTRJAuk17BoFkpDXrsOCo5Zr2fmDUnCOq0bISHSt1g5xYbE3wUgNPp6WBoCWDE0po6plsuBUUaqubgKt4yWe8x0H6pqO9pgotMu%2Bd45AOy9bcIUkJ66U5oCCN5RjoQw%2F1a%2FCnY84Msup8n71Qh70kdiAm%2B%2FkS5qRLPmKm1GtoHnovicoiTuvgIXXiVIz826acpdyJPCbbPu%2Bf%2Bsrs%2BU2xoaX5yFyNODyWVb69YzFwkyqJWF7q6P73aacVAq0iyg%2FTYAX6uCpJkJ%2Bkj6Nzqy95ekWdd1OIpzeOdltWtM%2BH5Aa7nLkdkoFtRFjIfBltTk55OUABGtcOrJviSbCkEp6tF56rU5gjlDGFHtzQndZ8XpnpmrJ2SP6vKBSzldZS7jSzi2k7ACTuNdauFcMNnDkr0GOqUB%2FRMUDtRQ8XZw0Bft%2B3PfEd83zyWBgxOfYe4IketzQC%2Bvxpxv912a3DNvQ0xQbcQmjNgrfNxdHUt4zibLeAZWCIQ40Kpl3AHsl2nNBzqKzHo4qBSh%2FA3XJE1g2%2FBwQ2sV42OlXsbo6lfZo0wiVZcGtxppa3izDA0zrnxbIFAXwbd1wxx8zMhlxtXnkufhtuc%2BzrBfU02k3OAVxNbhkl%2BFxnVFUiVj&X-Amz-Signature=def8eb8e9189798794b77c52888d4a379f4f742c5e444cdb04c31b457a0a4656&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFQUIUKK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIH2wmgO%2FSBeSxRkK88GByyU2bcUOdbO0IJ8ZAmMh0sG4AiEA3ZOLug7kYVz8fOCjoC4CVIj0yYf0p2an6geLHffxx38q%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDB7akynme08rLzVyOyrcA0X%2Fxkh%2F%2BUrNXUHEqrjNjYs3VV66FVT80yZ1fmBBjlW0uxm2AYVqhiSZa9Xkxja%2F7T5JdCV3K6h6LgxYsEuXB4kC%2FeSpGX9O2zdMuxZVHG%2FHvGDbZQ0upQYio3yrFJ6ALg%2FcRntwAeCPMbHP7VWCDl7XR7DwkAjD%2FH3A8OflfG%2BjaTwqmZQEl9IVQx%2FgJGfgHTxqFwq%2F3Dl4vn9hkcPS%2BJdVXYGMa9r4l%2F103K46bFMhTqzhgdiGEMEq4I8pp%2BqJwi1e9wVTtWI3wkSXhjGoqR%2FJI1XcOms%2BE%2Fm%2FwHQDpSdlMWsndTEN%2FiJPAAl7EKzmF8shrxV8xMbifiwcx%2Fq20624kRdU0%2FmiV%2FIpkd4QGJlpzXgazaovmW5CezRnGRKKDEs0R7g3F48Lltwx5j1xMmq8WEI7iuY%2FsJP90RRGrinLbffozFlKu7yQUI464rvkgW28DS0P2BUjuWLBbFTU%2BFWz2rcDZXdcgUOHkdndRHnzCuyd7hIBMaGsxtOvWkFIJUXM%2FpwxN85es4iHs3sB1GmhUuQPV7miFsYDIcJD%2FKZaDRGALNGcYatgP0boWLuVXeFV0J%2BWt%2BYMt%2FRxMOKCmNrwo9dQtpm1nSKFYzLGZGT2048KSE6h99LEHFPzMOjDkr0GOqUBiSf%2FGAAEZjy%2F1iE9BFBg%2BaJ3KnOEUj4aktBdb1qNggTPSxjVylMkWLEE%2BXJX%2FtgdP5u%2BChXywHOIK8hFAGJPihwsj8aCUCutQR57%2FlY6ECIrAWt1XPiw%2Fcw971I2MsAgQUc0H6KDIUhkw2bbR1MaiBAeSWbkdhnrYB6aOn3Um3LSam4ugkoAnV%2B4Xmc4%2FyNbImoYPkt%2B9D4imIZ%2B%2FFW0oWjylcAn&X-Amz-Signature=648fbf001363280e202fd4746ba5b176648c7dca642547cb1a3da90beaf0eacc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFQUIUKK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIH2wmgO%2FSBeSxRkK88GByyU2bcUOdbO0IJ8ZAmMh0sG4AiEA3ZOLug7kYVz8fOCjoC4CVIj0yYf0p2an6geLHffxx38q%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDB7akynme08rLzVyOyrcA0X%2Fxkh%2F%2BUrNXUHEqrjNjYs3VV66FVT80yZ1fmBBjlW0uxm2AYVqhiSZa9Xkxja%2F7T5JdCV3K6h6LgxYsEuXB4kC%2FeSpGX9O2zdMuxZVHG%2FHvGDbZQ0upQYio3yrFJ6ALg%2FcRntwAeCPMbHP7VWCDl7XR7DwkAjD%2FH3A8OflfG%2BjaTwqmZQEl9IVQx%2FgJGfgHTxqFwq%2F3Dl4vn9hkcPS%2BJdVXYGMa9r4l%2F103K46bFMhTqzhgdiGEMEq4I8pp%2BqJwi1e9wVTtWI3wkSXhjGoqR%2FJI1XcOms%2BE%2Fm%2FwHQDpSdlMWsndTEN%2FiJPAAl7EKzmF8shrxV8xMbifiwcx%2Fq20624kRdU0%2FmiV%2FIpkd4QGJlpzXgazaovmW5CezRnGRKKDEs0R7g3F48Lltwx5j1xMmq8WEI7iuY%2FsJP90RRGrinLbffozFlKu7yQUI464rvkgW28DS0P2BUjuWLBbFTU%2BFWz2rcDZXdcgUOHkdndRHnzCuyd7hIBMaGsxtOvWkFIJUXM%2FpwxN85es4iHs3sB1GmhUuQPV7miFsYDIcJD%2FKZaDRGALNGcYatgP0boWLuVXeFV0J%2BWt%2BYMt%2FRxMOKCmNrwo9dQtpm1nSKFYzLGZGT2048KSE6h99LEHFPzMOjDkr0GOqUBiSf%2FGAAEZjy%2F1iE9BFBg%2BaJ3KnOEUj4aktBdb1qNggTPSxjVylMkWLEE%2BXJX%2FtgdP5u%2BChXywHOIK8hFAGJPihwsj8aCUCutQR57%2FlY6ECIrAWt1XPiw%2Fcw971I2MsAgQUc0H6KDIUhkw2bbR1MaiBAeSWbkdhnrYB6aOn3Um3LSam4ugkoAnV%2B4Xmc4%2FyNbImoYPkt%2B9D4imIZ%2B%2FFW0oWjylcAn&X-Amz-Signature=b47fc2c53b4f0a6533faed4c8d6ebf6d4357f43f50ff1075113d7efa47eda0a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
