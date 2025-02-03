

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDP5UL3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8WEJwdOeqjSx8X%2B4skB3vpSUqvnUtyZ%2BJq6OFq48zAiEA3SbjbRTJdrfC03StFwDLW%2BCpHoQTj4Rm9mIloZkYVj8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHtvIoTN13cLL%2BDOTCrcAztxtpEErCG8SyPP527tZ%2FfKxvJJNvoPDdTSKVJ55xJOXpU2S2MzNjvd%2FxqoIrzKys1GPxkw9dVqqIRgxUvPCgXYObo3RxpGD7iPfgPFxT49XjyVf7E7fOp6B1VTO5nr0yCOohaKUUQsnPPLW0pfIEfngDXasdmplo0t22aT%2BQjyDaWCbORYMUayVatBLJYiuPBF6AveLoiEd3y6v%2Bxa%2BuLpIukEv9VN2UEDJVjv%2FMCWHziHfPECVbAiuwGwEgTuYzjHnLsHwKK0Q5HF1BNhMMIhy9TW%2Futadh1Y4QfmDFyaLLkPyEGxkrXKN%2BTcrAqZQCqc25hOAIj%2BoD%2F8Qm0H8v5J2DptQkkZMlo8%2FEp26y1P0lro2VvDGuk9tRk%2BIyYSo8TcOTHh%2BMu3Sk3H6ESCyXMv2GTNJEG1NYoMC%2Fyk9TC5kJbwzDWXF%2Fe2rIMClxqUXNslCpUDBtLDRmvEJUVHXq4sMJkMEfX6phi5%2FqD2WNBw5MBdvMs8f9gSJQByRys6AiieIkjzjR24eUZciR9PkB5Ul5pi58MQoDpdYSsB%2F0aSEkLHKqUgCUbWYLJO1voMxyEBHAnf2xnR6XjEg0Y11uQw0uZZyWz7tl1UGak14IeUj22F%2F8tld4cWXC0wMLHzgb0GOqUBOoivwQdQrjkg69Pu4oX8WowoVKkXDtij0eOiF3IP8Sl2z1NXagkq6UJJGe6%2FsrxeyF2ibbUA5pNj0rKzsetqIkxxywzx6oNXKNmoHFGL7s7nSggDRJaCUhmxXBvMFXgEbuUHYj9YOlyJbdIrkQMK4kmmu2gYKAeaD0XTxa6aPs1qI0kaKL7X27veY3NGmAuYGUQTLv12RFuBslSQHxODd%2FrhdrqX&X-Amz-Signature=9dfa4697d98c8ac76ffbf8b2f963fbe57af1eb5a574050a937f80e42a3f90a09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDP5UL3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8WEJwdOeqjSx8X%2B4skB3vpSUqvnUtyZ%2BJq6OFq48zAiEA3SbjbRTJdrfC03StFwDLW%2BCpHoQTj4Rm9mIloZkYVj8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHtvIoTN13cLL%2BDOTCrcAztxtpEErCG8SyPP527tZ%2FfKxvJJNvoPDdTSKVJ55xJOXpU2S2MzNjvd%2FxqoIrzKys1GPxkw9dVqqIRgxUvPCgXYObo3RxpGD7iPfgPFxT49XjyVf7E7fOp6B1VTO5nr0yCOohaKUUQsnPPLW0pfIEfngDXasdmplo0t22aT%2BQjyDaWCbORYMUayVatBLJYiuPBF6AveLoiEd3y6v%2Bxa%2BuLpIukEv9VN2UEDJVjv%2FMCWHziHfPECVbAiuwGwEgTuYzjHnLsHwKK0Q5HF1BNhMMIhy9TW%2Futadh1Y4QfmDFyaLLkPyEGxkrXKN%2BTcrAqZQCqc25hOAIj%2BoD%2F8Qm0H8v5J2DptQkkZMlo8%2FEp26y1P0lro2VvDGuk9tRk%2BIyYSo8TcOTHh%2BMu3Sk3H6ESCyXMv2GTNJEG1NYoMC%2Fyk9TC5kJbwzDWXF%2Fe2rIMClxqUXNslCpUDBtLDRmvEJUVHXq4sMJkMEfX6phi5%2FqD2WNBw5MBdvMs8f9gSJQByRys6AiieIkjzjR24eUZciR9PkB5Ul5pi58MQoDpdYSsB%2F0aSEkLHKqUgCUbWYLJO1voMxyEBHAnf2xnR6XjEg0Y11uQw0uZZyWz7tl1UGak14IeUj22F%2F8tld4cWXC0wMLHzgb0GOqUBOoivwQdQrjkg69Pu4oX8WowoVKkXDtij0eOiF3IP8Sl2z1NXagkq6UJJGe6%2FsrxeyF2ibbUA5pNj0rKzsetqIkxxywzx6oNXKNmoHFGL7s7nSggDRJaCUhmxXBvMFXgEbuUHYj9YOlyJbdIrkQMK4kmmu2gYKAeaD0XTxa6aPs1qI0kaKL7X27veY3NGmAuYGUQTLv12RFuBslSQHxODd%2FrhdrqX&X-Amz-Signature=f4453bedc0955f757ba71af06f348ac80d1dbf68b8bfd8f1ba9038da763fcd0a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDP5UL3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8WEJwdOeqjSx8X%2B4skB3vpSUqvnUtyZ%2BJq6OFq48zAiEA3SbjbRTJdrfC03StFwDLW%2BCpHoQTj4Rm9mIloZkYVj8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHtvIoTN13cLL%2BDOTCrcAztxtpEErCG8SyPP527tZ%2FfKxvJJNvoPDdTSKVJ55xJOXpU2S2MzNjvd%2FxqoIrzKys1GPxkw9dVqqIRgxUvPCgXYObo3RxpGD7iPfgPFxT49XjyVf7E7fOp6B1VTO5nr0yCOohaKUUQsnPPLW0pfIEfngDXasdmplo0t22aT%2BQjyDaWCbORYMUayVatBLJYiuPBF6AveLoiEd3y6v%2Bxa%2BuLpIukEv9VN2UEDJVjv%2FMCWHziHfPECVbAiuwGwEgTuYzjHnLsHwKK0Q5HF1BNhMMIhy9TW%2Futadh1Y4QfmDFyaLLkPyEGxkrXKN%2BTcrAqZQCqc25hOAIj%2BoD%2F8Qm0H8v5J2DptQkkZMlo8%2FEp26y1P0lro2VvDGuk9tRk%2BIyYSo8TcOTHh%2BMu3Sk3H6ESCyXMv2GTNJEG1NYoMC%2Fyk9TC5kJbwzDWXF%2Fe2rIMClxqUXNslCpUDBtLDRmvEJUVHXq4sMJkMEfX6phi5%2FqD2WNBw5MBdvMs8f9gSJQByRys6AiieIkjzjR24eUZciR9PkB5Ul5pi58MQoDpdYSsB%2F0aSEkLHKqUgCUbWYLJO1voMxyEBHAnf2xnR6XjEg0Y11uQw0uZZyWz7tl1UGak14IeUj22F%2F8tld4cWXC0wMLHzgb0GOqUBOoivwQdQrjkg69Pu4oX8WowoVKkXDtij0eOiF3IP8Sl2z1NXagkq6UJJGe6%2FsrxeyF2ibbUA5pNj0rKzsetqIkxxywzx6oNXKNmoHFGL7s7nSggDRJaCUhmxXBvMFXgEbuUHYj9YOlyJbdIrkQMK4kmmu2gYKAeaD0XTxa6aPs1qI0kaKL7X27veY3NGmAuYGUQTLv12RFuBslSQHxODd%2FrhdrqX&X-Amz-Signature=84243b68e4d0ca722fa46bcf10e99086955c7f316f99525472a9cd0612f52ec6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDP5UL3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8WEJwdOeqjSx8X%2B4skB3vpSUqvnUtyZ%2BJq6OFq48zAiEA3SbjbRTJdrfC03StFwDLW%2BCpHoQTj4Rm9mIloZkYVj8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHtvIoTN13cLL%2BDOTCrcAztxtpEErCG8SyPP527tZ%2FfKxvJJNvoPDdTSKVJ55xJOXpU2S2MzNjvd%2FxqoIrzKys1GPxkw9dVqqIRgxUvPCgXYObo3RxpGD7iPfgPFxT49XjyVf7E7fOp6B1VTO5nr0yCOohaKUUQsnPPLW0pfIEfngDXasdmplo0t22aT%2BQjyDaWCbORYMUayVatBLJYiuPBF6AveLoiEd3y6v%2Bxa%2BuLpIukEv9VN2UEDJVjv%2FMCWHziHfPECVbAiuwGwEgTuYzjHnLsHwKK0Q5HF1BNhMMIhy9TW%2Futadh1Y4QfmDFyaLLkPyEGxkrXKN%2BTcrAqZQCqc25hOAIj%2BoD%2F8Qm0H8v5J2DptQkkZMlo8%2FEp26y1P0lro2VvDGuk9tRk%2BIyYSo8TcOTHh%2BMu3Sk3H6ESCyXMv2GTNJEG1NYoMC%2Fyk9TC5kJbwzDWXF%2Fe2rIMClxqUXNslCpUDBtLDRmvEJUVHXq4sMJkMEfX6phi5%2FqD2WNBw5MBdvMs8f9gSJQByRys6AiieIkjzjR24eUZciR9PkB5Ul5pi58MQoDpdYSsB%2F0aSEkLHKqUgCUbWYLJO1voMxyEBHAnf2xnR6XjEg0Y11uQw0uZZyWz7tl1UGak14IeUj22F%2F8tld4cWXC0wMLHzgb0GOqUBOoivwQdQrjkg69Pu4oX8WowoVKkXDtij0eOiF3IP8Sl2z1NXagkq6UJJGe6%2FsrxeyF2ibbUA5pNj0rKzsetqIkxxywzx6oNXKNmoHFGL7s7nSggDRJaCUhmxXBvMFXgEbuUHYj9YOlyJbdIrkQMK4kmmu2gYKAeaD0XTxa6aPs1qI0kaKL7X27veY3NGmAuYGUQTLv12RFuBslSQHxODd%2FrhdrqX&X-Amz-Signature=c0af9c4418040614f8ec0d1e5e515fc1cf694d0635b276a85fc8e8240fa430fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDP5UL3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8WEJwdOeqjSx8X%2B4skB3vpSUqvnUtyZ%2BJq6OFq48zAiEA3SbjbRTJdrfC03StFwDLW%2BCpHoQTj4Rm9mIloZkYVj8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHtvIoTN13cLL%2BDOTCrcAztxtpEErCG8SyPP527tZ%2FfKxvJJNvoPDdTSKVJ55xJOXpU2S2MzNjvd%2FxqoIrzKys1GPxkw9dVqqIRgxUvPCgXYObo3RxpGD7iPfgPFxT49XjyVf7E7fOp6B1VTO5nr0yCOohaKUUQsnPPLW0pfIEfngDXasdmplo0t22aT%2BQjyDaWCbORYMUayVatBLJYiuPBF6AveLoiEd3y6v%2Bxa%2BuLpIukEv9VN2UEDJVjv%2FMCWHziHfPECVbAiuwGwEgTuYzjHnLsHwKK0Q5HF1BNhMMIhy9TW%2Futadh1Y4QfmDFyaLLkPyEGxkrXKN%2BTcrAqZQCqc25hOAIj%2BoD%2F8Qm0H8v5J2DptQkkZMlo8%2FEp26y1P0lro2VvDGuk9tRk%2BIyYSo8TcOTHh%2BMu3Sk3H6ESCyXMv2GTNJEG1NYoMC%2Fyk9TC5kJbwzDWXF%2Fe2rIMClxqUXNslCpUDBtLDRmvEJUVHXq4sMJkMEfX6phi5%2FqD2WNBw5MBdvMs8f9gSJQByRys6AiieIkjzjR24eUZciR9PkB5Ul5pi58MQoDpdYSsB%2F0aSEkLHKqUgCUbWYLJO1voMxyEBHAnf2xnR6XjEg0Y11uQw0uZZyWz7tl1UGak14IeUj22F%2F8tld4cWXC0wMLHzgb0GOqUBOoivwQdQrjkg69Pu4oX8WowoVKkXDtij0eOiF3IP8Sl2z1NXagkq6UJJGe6%2FsrxeyF2ibbUA5pNj0rKzsetqIkxxywzx6oNXKNmoHFGL7s7nSggDRJaCUhmxXBvMFXgEbuUHYj9YOlyJbdIrkQMK4kmmu2gYKAeaD0XTxa6aPs1qI0kaKL7X27veY3NGmAuYGUQTLv12RFuBslSQHxODd%2FrhdrqX&X-Amz-Signature=7b8f2009c42df2f9801934cb970ec84ef49a748fcf234e71478077b55050d503&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDP5UL3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8WEJwdOeqjSx8X%2B4skB3vpSUqvnUtyZ%2BJq6OFq48zAiEA3SbjbRTJdrfC03StFwDLW%2BCpHoQTj4Rm9mIloZkYVj8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHtvIoTN13cLL%2BDOTCrcAztxtpEErCG8SyPP527tZ%2FfKxvJJNvoPDdTSKVJ55xJOXpU2S2MzNjvd%2FxqoIrzKys1GPxkw9dVqqIRgxUvPCgXYObo3RxpGD7iPfgPFxT49XjyVf7E7fOp6B1VTO5nr0yCOohaKUUQsnPPLW0pfIEfngDXasdmplo0t22aT%2BQjyDaWCbORYMUayVatBLJYiuPBF6AveLoiEd3y6v%2Bxa%2BuLpIukEv9VN2UEDJVjv%2FMCWHziHfPECVbAiuwGwEgTuYzjHnLsHwKK0Q5HF1BNhMMIhy9TW%2Futadh1Y4QfmDFyaLLkPyEGxkrXKN%2BTcrAqZQCqc25hOAIj%2BoD%2F8Qm0H8v5J2DptQkkZMlo8%2FEp26y1P0lro2VvDGuk9tRk%2BIyYSo8TcOTHh%2BMu3Sk3H6ESCyXMv2GTNJEG1NYoMC%2Fyk9TC5kJbwzDWXF%2Fe2rIMClxqUXNslCpUDBtLDRmvEJUVHXq4sMJkMEfX6phi5%2FqD2WNBw5MBdvMs8f9gSJQByRys6AiieIkjzjR24eUZciR9PkB5Ul5pi58MQoDpdYSsB%2F0aSEkLHKqUgCUbWYLJO1voMxyEBHAnf2xnR6XjEg0Y11uQw0uZZyWz7tl1UGak14IeUj22F%2F8tld4cWXC0wMLHzgb0GOqUBOoivwQdQrjkg69Pu4oX8WowoVKkXDtij0eOiF3IP8Sl2z1NXagkq6UJJGe6%2FsrxeyF2ibbUA5pNj0rKzsetqIkxxywzx6oNXKNmoHFGL7s7nSggDRJaCUhmxXBvMFXgEbuUHYj9YOlyJbdIrkQMK4kmmu2gYKAeaD0XTxa6aPs1qI0kaKL7X27veY3NGmAuYGUQTLv12RFuBslSQHxODd%2FrhdrqX&X-Amz-Signature=c55a85469b66dd32fae79b67594cc8f200eb66e846a708409f586773c393fe7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDP5UL3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8WEJwdOeqjSx8X%2B4skB3vpSUqvnUtyZ%2BJq6OFq48zAiEA3SbjbRTJdrfC03StFwDLW%2BCpHoQTj4Rm9mIloZkYVj8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHtvIoTN13cLL%2BDOTCrcAztxtpEErCG8SyPP527tZ%2FfKxvJJNvoPDdTSKVJ55xJOXpU2S2MzNjvd%2FxqoIrzKys1GPxkw9dVqqIRgxUvPCgXYObo3RxpGD7iPfgPFxT49XjyVf7E7fOp6B1VTO5nr0yCOohaKUUQsnPPLW0pfIEfngDXasdmplo0t22aT%2BQjyDaWCbORYMUayVatBLJYiuPBF6AveLoiEd3y6v%2Bxa%2BuLpIukEv9VN2UEDJVjv%2FMCWHziHfPECVbAiuwGwEgTuYzjHnLsHwKK0Q5HF1BNhMMIhy9TW%2Futadh1Y4QfmDFyaLLkPyEGxkrXKN%2BTcrAqZQCqc25hOAIj%2BoD%2F8Qm0H8v5J2DptQkkZMlo8%2FEp26y1P0lro2VvDGuk9tRk%2BIyYSo8TcOTHh%2BMu3Sk3H6ESCyXMv2GTNJEG1NYoMC%2Fyk9TC5kJbwzDWXF%2Fe2rIMClxqUXNslCpUDBtLDRmvEJUVHXq4sMJkMEfX6phi5%2FqD2WNBw5MBdvMs8f9gSJQByRys6AiieIkjzjR24eUZciR9PkB5Ul5pi58MQoDpdYSsB%2F0aSEkLHKqUgCUbWYLJO1voMxyEBHAnf2xnR6XjEg0Y11uQw0uZZyWz7tl1UGak14IeUj22F%2F8tld4cWXC0wMLHzgb0GOqUBOoivwQdQrjkg69Pu4oX8WowoVKkXDtij0eOiF3IP8Sl2z1NXagkq6UJJGe6%2FsrxeyF2ibbUA5pNj0rKzsetqIkxxywzx6oNXKNmoHFGL7s7nSggDRJaCUhmxXBvMFXgEbuUHYj9YOlyJbdIrkQMK4kmmu2gYKAeaD0XTxa6aPs1qI0kaKL7X27veY3NGmAuYGUQTLv12RFuBslSQHxODd%2FrhdrqX&X-Amz-Signature=3ac78094525b78509a9e56182568bde43e194147a874207d9643a83c0d2d78d6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664GDP5UL3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICV8WEJwdOeqjSx8X%2B4skB3vpSUqvnUtyZ%2BJq6OFq48zAiEA3SbjbRTJdrfC03StFwDLW%2BCpHoQTj4Rm9mIloZkYVj8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHtvIoTN13cLL%2BDOTCrcAztxtpEErCG8SyPP527tZ%2FfKxvJJNvoPDdTSKVJ55xJOXpU2S2MzNjvd%2FxqoIrzKys1GPxkw9dVqqIRgxUvPCgXYObo3RxpGD7iPfgPFxT49XjyVf7E7fOp6B1VTO5nr0yCOohaKUUQsnPPLW0pfIEfngDXasdmplo0t22aT%2BQjyDaWCbORYMUayVatBLJYiuPBF6AveLoiEd3y6v%2Bxa%2BuLpIukEv9VN2UEDJVjv%2FMCWHziHfPECVbAiuwGwEgTuYzjHnLsHwKK0Q5HF1BNhMMIhy9TW%2Futadh1Y4QfmDFyaLLkPyEGxkrXKN%2BTcrAqZQCqc25hOAIj%2BoD%2F8Qm0H8v5J2DptQkkZMlo8%2FEp26y1P0lro2VvDGuk9tRk%2BIyYSo8TcOTHh%2BMu3Sk3H6ESCyXMv2GTNJEG1NYoMC%2Fyk9TC5kJbwzDWXF%2Fe2rIMClxqUXNslCpUDBtLDRmvEJUVHXq4sMJkMEfX6phi5%2FqD2WNBw5MBdvMs8f9gSJQByRys6AiieIkjzjR24eUZciR9PkB5Ul5pi58MQoDpdYSsB%2F0aSEkLHKqUgCUbWYLJO1voMxyEBHAnf2xnR6XjEg0Y11uQw0uZZyWz7tl1UGak14IeUj22F%2F8tld4cWXC0wMLHzgb0GOqUBOoivwQdQrjkg69Pu4oX8WowoVKkXDtij0eOiF3IP8Sl2z1NXagkq6UJJGe6%2FsrxeyF2ibbUA5pNj0rKzsetqIkxxywzx6oNXKNmoHFGL7s7nSggDRJaCUhmxXBvMFXgEbuUHYj9YOlyJbdIrkQMK4kmmu2gYKAeaD0XTxa6aPs1qI0kaKL7X27veY3NGmAuYGUQTLv12RFuBslSQHxODd%2FrhdrqX&X-Amz-Signature=bbaa2e9566f649f9a54b2915a121bf08ea6d3716c099e99c121e15d07f6c6494&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUZLIFYO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGDyAJttFmTQ9Kip2o27nmIuZRghkaTa%2FDxd85QXTr6RAiAhzmM5a%2FlSoQSxMupqO35yNKxErEjV5sVkvt2us2Aurir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMPB2%2BTmivQnKglf4JKtwDTlk%2BdTLE35q1Y77LmlzV9MeD4L7OiyJLcRIsE8X28j8%2FEsFacBAj9H54B2V3KT5DB8HO%2BtFTZZBJVaDuMz%2FImSUtH4PY7EItzXi1kQ6XdaHbdQFz8%2FzIL75Dmi6Awcl0ERtE3A9%2BBzEBt5ukPa21dnh7Z2JlKdJ9xHg5EbakB3NR1jNLEM3NZbe2GG%2FL1NwZtA0SF7LOXSCBvVQYc0k5Wkhps56%2BazT5VgcCOFVLmAAZhLJY5ZgdygQPhFxbAkvm0s72PZYNpuRgzx5IINcy1qlSdSKIRXlZtIdCJ1%2BPDv3tRYdZ7JMQD4GPfNecM1GDC2%2BRdfa01MXRjqvy0HRxX%2B7Op0XpOi9Q8ZK%2BGVmhE%2Bef47SDawfnIfx8GbqAaf7bPLUiiU%2FaskHPdu0rLLOjjQm8wGIzOnXg%2BnAkBEnWW1r8lI6xdhBgri3ZsM%2FOaOgpqYMguK7Z%2BVBx0niF%2BA5qQtpxHzCwF%2B5C9M3KL6ekJKeBwSTY2mAHOsAY4zU2FfGMIS60%2BgK60aA7BvFH5PlLhNM94S1USLRnZkcQM9kc0pTzvGZvSfKQ%2BmB8Iy4rwO7LsLIsd9cRduD4BEyEFbNF%2FTMVxvRWdys0kQzyF472saRUjWt5omSRjXSVlC0wuvOBvQY6pgFrAupbKVeckD3GsRftMvuqY9oQVPl20XBa6oidtcM6vzFlw1HPJBW82O3nOv8PObWhBhc7PcOIpGimAyHAULboPGNDg7yTMSBBHDSbkRvXCRAoNWjLpd4L%2F944d9h2e8kxCV4XLaU4OoicjvxP8KXG9NO1Mu1nOGHyQjNHn7MiP6JiCGV7ABlq3JLjqpoqx3zDPmaJVpxLW8d3Gk0MEkch0DfZexcT&X-Amz-Signature=528dcc984a4dc2102602cb701c5ec2612b1d2dbb86e24027785d06e725b364db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D3WY4CO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICZUJxuqPv4APNXWAtNwHZAY8%2FCfhXw1eRfvSsdKVUT9AiBbXI8GspFKMKLs4n%2BgHsfbctjYQsl%2Fs0Gxcq7LFpZcACr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMAxax%2FlY%2BW6pqSKmaKtwDfeMPnK9n7rDwFlFmFu2seDe7mI0AzKDjei3zSbtvP3hrMutieO2XnGgJO6m6xCH0XWUHThjyib2Nkv3BVsruqI6HUj6dYJR5kv2BoYLlcaqVXFei%2BPoc0jSMfS2WGwg1elpihoQAg%2BGBN07XIpLGZK3gmMiiMNhRF8bgri5%2FG3ebM%2F3xzljqhwrxZq%2FOLtBvg8R37ht9U%2BZpe6ZqmM7N4nBX8OjkMKVBhXKXP86or3yhSIpSBpD3FappRfbrJOq3BJwWqVRz29CS44gvAHl7Kjl90C9eScyG4AIt1P4FfFLfHhiFCNpVR5C2JQwgRhk4%2B3%2FfVYCf8Ekl1sPSyHYiIvyZtPfcPjmz5BGvVdpkrNptds1N2OFsrj5kJLVuMuftqUQwtw%2F%2BYH4a0eYGinmLUeiD8SsqkzCTtcfLnZo%2FA5LlAQlCbbIsWPsvSwNGwt2yuUZi0hfEPsYNUoFiK7BMfcKal%2BzXc5qcb8FI8khTYqV9B60SWGJh52tCYbyFJXkYp9rn%2BsPsRuPu7r21F5bEKAeQxrdhgKUI0qcx8rIufyLzEULx%2BAL%2FMlXsOEaN%2BGjJrWDs7X5YfYa8EYCASisWTDaR8MXdnKitnAkBB3bb1nYzjquCqgkJWs%2BbhoQwufOBvQY6pgGU9ApmYn3CKs2iocmluxLuAvoanCCoT4XJ%2F82nELz4i8SOajaG%2BoSBkcgWB%2B8xQCs0HX78YwILnM6wSPpSm8mm87uBv78LR30tMNnG9qyDwQe%2FgGDVCjgLYTnLxs4F4KbcxQ1KwHy%2F2E18e7GHLej3yeJRAV98y29CLopC5W6Fw4utDOHYNzDLO6NuGTZRdMMROb7UyeRri53MnUMp36lOcY%2BS0Fyw&X-Amz-Signature=b8b92b90f38f5bc3c233e4f2e18916ae094aba17d28d59dc92a9cfd8b47993d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ5VNFDG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCh9xD%2BWuAp4i5i3w08CTrGx3xQ0pkrVKPcQ8wyy6HhqQIhANAmFXYYHYWzLcC850tBQ045k54Ig8LeA4LbidUCGHIRKv8DCBEQABoMNjM3NDIzMTgzODA1IgwAplocFjR%2Bdl%2BSW6Qq3AOFsr2PpCv%2FFkjlzL3165NHTcMo7h%2FZ5qblhBLgzpLi5GDPZdvumqjQy7OubHrXyefSuU09JCWIjSwaPm4dyeJQFE7i41lyoX2q7Jl%2FFlOl5%2BID9FjbzbzkfLjWvRsSOLIpDbS6ihuMZicQ8g2XsPVLLYiIwSUITdg1Iw6B6BCf0DrqGIesHKNGxielSk50enJkPcol2qU8H6aUNjW5vOvKEv6EILIKEyL4nw0kSikWlCGX5JEw08w7t9ApZpYCTN0l5yfY1zxxT8uG1Bhqk8gaB%2BrTO3mN1%2B3tBvqUgfg1zucd69N1DgdBekHEBWH6yy3q6Hi5wbpQ8zuVVobIQE%2B9vbuQEmxQ1OJj62lQ8k18gScehD0CaYuy2w%2FgvNhqiS7r%2F5g863hCIgLNhADHcEl4RGkib0eRl3qN9QcwBf2FaOv6ppbAdCSWBXeQSWBstKY8oW2l2K4cu%2Fz64Ac4DFXPFDsA8f8jZlKCLulHLgyJPoV4cbn1Yy8%2FBnzX2pV%2B2VI1DLwiD%2Bq9makJaDtoCCOaIUxRiKl23NHwgOeyHZgcH%2F5clo%2BHUHa9JvuNNIzCoie3cL%2Bj7S1knjcWkHiypCTbrqLMWLBTALXFma%2FvBiqCozKDJ%2BhTdxEVbvnI%2BjC184G9BjqkAc6rAoiFHP0jvaSAws3S7ij%2B1s1pVKv8ThmW5Nn7apr52QQ33dpuyzqMDPgB681f3RyUXDLC%2F%2FJgEoXtsLylDV4GlihdLCN%2BPZGchfrnWcavVUz3PZM2%2FxjK2Ytja5agKJMGB3Kka5uMvI70k4xWXYS7v3J3tnmYiMVtSMm%2FoHbRNNYuWBOHs9ttlk%2FDNPzBMmfjdsN6r3hL8bqOqhXeHmt%2FN71f&X-Amz-Signature=f1782612dd1d0e36e3d623c3f153ce90f25424d68f050eaa346a6be16d43de56&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ5VNFDG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T081950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCh9xD%2BWuAp4i5i3w08CTrGx3xQ0pkrVKPcQ8wyy6HhqQIhANAmFXYYHYWzLcC850tBQ045k54Ig8LeA4LbidUCGHIRKv8DCBEQABoMNjM3NDIzMTgzODA1IgwAplocFjR%2Bdl%2BSW6Qq3AOFsr2PpCv%2FFkjlzL3165NHTcMo7h%2FZ5qblhBLgzpLi5GDPZdvumqjQy7OubHrXyefSuU09JCWIjSwaPm4dyeJQFE7i41lyoX2q7Jl%2FFlOl5%2BID9FjbzbzkfLjWvRsSOLIpDbS6ihuMZicQ8g2XsPVLLYiIwSUITdg1Iw6B6BCf0DrqGIesHKNGxielSk50enJkPcol2qU8H6aUNjW5vOvKEv6EILIKEyL4nw0kSikWlCGX5JEw08w7t9ApZpYCTN0l5yfY1zxxT8uG1Bhqk8gaB%2BrTO3mN1%2B3tBvqUgfg1zucd69N1DgdBekHEBWH6yy3q6Hi5wbpQ8zuVVobIQE%2B9vbuQEmxQ1OJj62lQ8k18gScehD0CaYuy2w%2FgvNhqiS7r%2F5g863hCIgLNhADHcEl4RGkib0eRl3qN9QcwBf2FaOv6ppbAdCSWBXeQSWBstKY8oW2l2K4cu%2Fz64Ac4DFXPFDsA8f8jZlKCLulHLgyJPoV4cbn1Yy8%2FBnzX2pV%2B2VI1DLwiD%2Bq9makJaDtoCCOaIUxRiKl23NHwgOeyHZgcH%2F5clo%2BHUHa9JvuNNIzCoie3cL%2Bj7S1knjcWkHiypCTbrqLMWLBTALXFma%2FvBiqCozKDJ%2BhTdxEVbvnI%2BjC184G9BjqkAc6rAoiFHP0jvaSAws3S7ij%2B1s1pVKv8ThmW5Nn7apr52QQ33dpuyzqMDPgB681f3RyUXDLC%2F%2FJgEoXtsLylDV4GlihdLCN%2BPZGchfrnWcavVUz3PZM2%2FxjK2Ytja5agKJMGB3Kka5uMvI70k4xWXYS7v3J3tnmYiMVtSMm%2FoHbRNNYuWBOHs9ttlk%2FDNPzBMmfjdsN6r3hL8bqOqhXeHmt%2FN71f&X-Amz-Signature=a647c98e31f3a48e0ed24aa6173f309f768d3b28579bca49383bb93feee1d59a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
