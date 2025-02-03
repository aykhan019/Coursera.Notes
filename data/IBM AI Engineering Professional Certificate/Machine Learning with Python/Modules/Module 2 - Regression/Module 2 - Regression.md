

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667644WZON%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEEIKudeA%2F9ywzcIo9ZcnYIZRtWLOdVwIqsyXP12V%2FpeAiEA9FtK44WWm5UYsueT%2FowwstCEmoJf7Ns0tUmT26zk7GsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuEkhlAv43U%2FfNwHCrcA3GuQTKBnYjFqSnRWJIMTQhj5horswb9O6fi0SkeMn9YGLiaU7jaSpn5oMhqpMoHP0WFzLmf3Oai%2BFEv2wcj50lSGTJEF8yG7dfsYWUf2WNg3CpnJirZ6eztO5AcfjegXnwWCwcUR2BPW69Sz7j3BroFt3VbWMs%2B%2FQrCS2zLWadyCmBxfJxMoLMzDXwDxxQpc6J7TM07wAydV2CEy%2FuhcDLd5gZK4bOFqpU7zrdzHRPc7U9Sv4bY8VFZxezgoQtATqBV1BngTrB84klVBSGIKT4UCzI9yXkcXCYvf91qE0H9eCHxW90yLMw0qta4Bjg0csREA6Qoh%2FRDM0ngTS4D7WovwSd%2BvCYI%2B9dhwpAwxWwcnID%2FpMosL9YR1bdQuvl1bYtRJP2BeKgqf0oRcQyr9Fi0NpB26VKdLCHGlVOFYul2eiYauw6iNcpssGJoFQ%2FdEItH99CXbXr%2B2rupmu6BaN4izSuHk2PwJ9iYBKeFQS%2Bx3nx0cZK%2F7FDCS2%2FsEfnE2VY6FmNP6gr%2BqgwOxfVqlJstTxkyvKa0hpJ71BzSJzGxCNjhvVOuj9S%2BXv1MsRJkaYWXoqYUkVpvY5skY4ujz0j4%2BnybSCrbSU4fjXRY4E0Z2YgGGUBmIgNNc0yLMP26gb0GOqUBo%2Bzn3%2BewyytOqMGbsIzYSPzekIOV6an%2Bgkcc4pPM%2Bo%2BNleKMeXP1MdIKYwlcO3%2BR1zJIfyaWXuCWGAkO%2BhvBRKb%2FqnH7WCZII4rM4o4qqqTMcMbX1ar48uxbZ6oDhWjHTKvSMzxbtcBH1IGa5Y1CKEQrRIj8d%2FVc4%2BDf8ePqiuZW8mwW6m6yvqkBXRwvVOsRtPz8%2F1t%2Bq9Gf7FbUeIRtMnVo10pV&X-Amz-Signature=6eb085f00584a46738744f8d8d24c0d35910d74a535d9645de6e79ef700f4f84&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667644WZON%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEEIKudeA%2F9ywzcIo9ZcnYIZRtWLOdVwIqsyXP12V%2FpeAiEA9FtK44WWm5UYsueT%2FowwstCEmoJf7Ns0tUmT26zk7GsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuEkhlAv43U%2FfNwHCrcA3GuQTKBnYjFqSnRWJIMTQhj5horswb9O6fi0SkeMn9YGLiaU7jaSpn5oMhqpMoHP0WFzLmf3Oai%2BFEv2wcj50lSGTJEF8yG7dfsYWUf2WNg3CpnJirZ6eztO5AcfjegXnwWCwcUR2BPW69Sz7j3BroFt3VbWMs%2B%2FQrCS2zLWadyCmBxfJxMoLMzDXwDxxQpc6J7TM07wAydV2CEy%2FuhcDLd5gZK4bOFqpU7zrdzHRPc7U9Sv4bY8VFZxezgoQtATqBV1BngTrB84klVBSGIKT4UCzI9yXkcXCYvf91qE0H9eCHxW90yLMw0qta4Bjg0csREA6Qoh%2FRDM0ngTS4D7WovwSd%2BvCYI%2B9dhwpAwxWwcnID%2FpMosL9YR1bdQuvl1bYtRJP2BeKgqf0oRcQyr9Fi0NpB26VKdLCHGlVOFYul2eiYauw6iNcpssGJoFQ%2FdEItH99CXbXr%2B2rupmu6BaN4izSuHk2PwJ9iYBKeFQS%2Bx3nx0cZK%2F7FDCS2%2FsEfnE2VY6FmNP6gr%2BqgwOxfVqlJstTxkyvKa0hpJ71BzSJzGxCNjhvVOuj9S%2BXv1MsRJkaYWXoqYUkVpvY5skY4ujz0j4%2BnybSCrbSU4fjXRY4E0Z2YgGGUBmIgNNc0yLMP26gb0GOqUBo%2Bzn3%2BewyytOqMGbsIzYSPzekIOV6an%2Bgkcc4pPM%2Bo%2BNleKMeXP1MdIKYwlcO3%2BR1zJIfyaWXuCWGAkO%2BhvBRKb%2FqnH7WCZII4rM4o4qqqTMcMbX1ar48uxbZ6oDhWjHTKvSMzxbtcBH1IGa5Y1CKEQrRIj8d%2FVc4%2BDf8ePqiuZW8mwW6m6yvqkBXRwvVOsRtPz8%2F1t%2Bq9Gf7FbUeIRtMnVo10pV&X-Amz-Signature=6529abc4e5ffcafce5a41c39b7d2a7fa5214197823b9b342366b8d595fb5491b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667644WZON%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEEIKudeA%2F9ywzcIo9ZcnYIZRtWLOdVwIqsyXP12V%2FpeAiEA9FtK44WWm5UYsueT%2FowwstCEmoJf7Ns0tUmT26zk7GsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuEkhlAv43U%2FfNwHCrcA3GuQTKBnYjFqSnRWJIMTQhj5horswb9O6fi0SkeMn9YGLiaU7jaSpn5oMhqpMoHP0WFzLmf3Oai%2BFEv2wcj50lSGTJEF8yG7dfsYWUf2WNg3CpnJirZ6eztO5AcfjegXnwWCwcUR2BPW69Sz7j3BroFt3VbWMs%2B%2FQrCS2zLWadyCmBxfJxMoLMzDXwDxxQpc6J7TM07wAydV2CEy%2FuhcDLd5gZK4bOFqpU7zrdzHRPc7U9Sv4bY8VFZxezgoQtATqBV1BngTrB84klVBSGIKT4UCzI9yXkcXCYvf91qE0H9eCHxW90yLMw0qta4Bjg0csREA6Qoh%2FRDM0ngTS4D7WovwSd%2BvCYI%2B9dhwpAwxWwcnID%2FpMosL9YR1bdQuvl1bYtRJP2BeKgqf0oRcQyr9Fi0NpB26VKdLCHGlVOFYul2eiYauw6iNcpssGJoFQ%2FdEItH99CXbXr%2B2rupmu6BaN4izSuHk2PwJ9iYBKeFQS%2Bx3nx0cZK%2F7FDCS2%2FsEfnE2VY6FmNP6gr%2BqgwOxfVqlJstTxkyvKa0hpJ71BzSJzGxCNjhvVOuj9S%2BXv1MsRJkaYWXoqYUkVpvY5skY4ujz0j4%2BnybSCrbSU4fjXRY4E0Z2YgGGUBmIgNNc0yLMP26gb0GOqUBo%2Bzn3%2BewyytOqMGbsIzYSPzekIOV6an%2Bgkcc4pPM%2Bo%2BNleKMeXP1MdIKYwlcO3%2BR1zJIfyaWXuCWGAkO%2BhvBRKb%2FqnH7WCZII4rM4o4qqqTMcMbX1ar48uxbZ6oDhWjHTKvSMzxbtcBH1IGa5Y1CKEQrRIj8d%2FVc4%2BDf8ePqiuZW8mwW6m6yvqkBXRwvVOsRtPz8%2F1t%2Bq9Gf7FbUeIRtMnVo10pV&X-Amz-Signature=ef96797025e83b87f3199029b8f3fb3f21d15db067da912821553fb883e58bb4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667644WZON%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEEIKudeA%2F9ywzcIo9ZcnYIZRtWLOdVwIqsyXP12V%2FpeAiEA9FtK44WWm5UYsueT%2FowwstCEmoJf7Ns0tUmT26zk7GsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuEkhlAv43U%2FfNwHCrcA3GuQTKBnYjFqSnRWJIMTQhj5horswb9O6fi0SkeMn9YGLiaU7jaSpn5oMhqpMoHP0WFzLmf3Oai%2BFEv2wcj50lSGTJEF8yG7dfsYWUf2WNg3CpnJirZ6eztO5AcfjegXnwWCwcUR2BPW69Sz7j3BroFt3VbWMs%2B%2FQrCS2zLWadyCmBxfJxMoLMzDXwDxxQpc6J7TM07wAydV2CEy%2FuhcDLd5gZK4bOFqpU7zrdzHRPc7U9Sv4bY8VFZxezgoQtATqBV1BngTrB84klVBSGIKT4UCzI9yXkcXCYvf91qE0H9eCHxW90yLMw0qta4Bjg0csREA6Qoh%2FRDM0ngTS4D7WovwSd%2BvCYI%2B9dhwpAwxWwcnID%2FpMosL9YR1bdQuvl1bYtRJP2BeKgqf0oRcQyr9Fi0NpB26VKdLCHGlVOFYul2eiYauw6iNcpssGJoFQ%2FdEItH99CXbXr%2B2rupmu6BaN4izSuHk2PwJ9iYBKeFQS%2Bx3nx0cZK%2F7FDCS2%2FsEfnE2VY6FmNP6gr%2BqgwOxfVqlJstTxkyvKa0hpJ71BzSJzGxCNjhvVOuj9S%2BXv1MsRJkaYWXoqYUkVpvY5skY4ujz0j4%2BnybSCrbSU4fjXRY4E0Z2YgGGUBmIgNNc0yLMP26gb0GOqUBo%2Bzn3%2BewyytOqMGbsIzYSPzekIOV6an%2Bgkcc4pPM%2Bo%2BNleKMeXP1MdIKYwlcO3%2BR1zJIfyaWXuCWGAkO%2BhvBRKb%2FqnH7WCZII4rM4o4qqqTMcMbX1ar48uxbZ6oDhWjHTKvSMzxbtcBH1IGa5Y1CKEQrRIj8d%2FVc4%2BDf8ePqiuZW8mwW6m6yvqkBXRwvVOsRtPz8%2F1t%2Bq9Gf7FbUeIRtMnVo10pV&X-Amz-Signature=80951b0a22634e0d9d43d8ce8a1bc77f7ba21963a86dea31c86d5ff76665de13&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667644WZON%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEEIKudeA%2F9ywzcIo9ZcnYIZRtWLOdVwIqsyXP12V%2FpeAiEA9FtK44WWm5UYsueT%2FowwstCEmoJf7Ns0tUmT26zk7GsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuEkhlAv43U%2FfNwHCrcA3GuQTKBnYjFqSnRWJIMTQhj5horswb9O6fi0SkeMn9YGLiaU7jaSpn5oMhqpMoHP0WFzLmf3Oai%2BFEv2wcj50lSGTJEF8yG7dfsYWUf2WNg3CpnJirZ6eztO5AcfjegXnwWCwcUR2BPW69Sz7j3BroFt3VbWMs%2B%2FQrCS2zLWadyCmBxfJxMoLMzDXwDxxQpc6J7TM07wAydV2CEy%2FuhcDLd5gZK4bOFqpU7zrdzHRPc7U9Sv4bY8VFZxezgoQtATqBV1BngTrB84klVBSGIKT4UCzI9yXkcXCYvf91qE0H9eCHxW90yLMw0qta4Bjg0csREA6Qoh%2FRDM0ngTS4D7WovwSd%2BvCYI%2B9dhwpAwxWwcnID%2FpMosL9YR1bdQuvl1bYtRJP2BeKgqf0oRcQyr9Fi0NpB26VKdLCHGlVOFYul2eiYauw6iNcpssGJoFQ%2FdEItH99CXbXr%2B2rupmu6BaN4izSuHk2PwJ9iYBKeFQS%2Bx3nx0cZK%2F7FDCS2%2FsEfnE2VY6FmNP6gr%2BqgwOxfVqlJstTxkyvKa0hpJ71BzSJzGxCNjhvVOuj9S%2BXv1MsRJkaYWXoqYUkVpvY5skY4ujz0j4%2BnybSCrbSU4fjXRY4E0Z2YgGGUBmIgNNc0yLMP26gb0GOqUBo%2Bzn3%2BewyytOqMGbsIzYSPzekIOV6an%2Bgkcc4pPM%2Bo%2BNleKMeXP1MdIKYwlcO3%2BR1zJIfyaWXuCWGAkO%2BhvBRKb%2FqnH7WCZII4rM4o4qqqTMcMbX1ar48uxbZ6oDhWjHTKvSMzxbtcBH1IGa5Y1CKEQrRIj8d%2FVc4%2BDf8ePqiuZW8mwW6m6yvqkBXRwvVOsRtPz8%2F1t%2Bq9Gf7FbUeIRtMnVo10pV&X-Amz-Signature=e3908f64c4d2f23e1b7779157d0404a5c1bfe8b64705fa746d93cae796990487&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667644WZON%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEEIKudeA%2F9ywzcIo9ZcnYIZRtWLOdVwIqsyXP12V%2FpeAiEA9FtK44WWm5UYsueT%2FowwstCEmoJf7Ns0tUmT26zk7GsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuEkhlAv43U%2FfNwHCrcA3GuQTKBnYjFqSnRWJIMTQhj5horswb9O6fi0SkeMn9YGLiaU7jaSpn5oMhqpMoHP0WFzLmf3Oai%2BFEv2wcj50lSGTJEF8yG7dfsYWUf2WNg3CpnJirZ6eztO5AcfjegXnwWCwcUR2BPW69Sz7j3BroFt3VbWMs%2B%2FQrCS2zLWadyCmBxfJxMoLMzDXwDxxQpc6J7TM07wAydV2CEy%2FuhcDLd5gZK4bOFqpU7zrdzHRPc7U9Sv4bY8VFZxezgoQtATqBV1BngTrB84klVBSGIKT4UCzI9yXkcXCYvf91qE0H9eCHxW90yLMw0qta4Bjg0csREA6Qoh%2FRDM0ngTS4D7WovwSd%2BvCYI%2B9dhwpAwxWwcnID%2FpMosL9YR1bdQuvl1bYtRJP2BeKgqf0oRcQyr9Fi0NpB26VKdLCHGlVOFYul2eiYauw6iNcpssGJoFQ%2FdEItH99CXbXr%2B2rupmu6BaN4izSuHk2PwJ9iYBKeFQS%2Bx3nx0cZK%2F7FDCS2%2FsEfnE2VY6FmNP6gr%2BqgwOxfVqlJstTxkyvKa0hpJ71BzSJzGxCNjhvVOuj9S%2BXv1MsRJkaYWXoqYUkVpvY5skY4ujz0j4%2BnybSCrbSU4fjXRY4E0Z2YgGGUBmIgNNc0yLMP26gb0GOqUBo%2Bzn3%2BewyytOqMGbsIzYSPzekIOV6an%2Bgkcc4pPM%2Bo%2BNleKMeXP1MdIKYwlcO3%2BR1zJIfyaWXuCWGAkO%2BhvBRKb%2FqnH7WCZII4rM4o4qqqTMcMbX1ar48uxbZ6oDhWjHTKvSMzxbtcBH1IGa5Y1CKEQrRIj8d%2FVc4%2BDf8ePqiuZW8mwW6m6yvqkBXRwvVOsRtPz8%2F1t%2Bq9Gf7FbUeIRtMnVo10pV&X-Amz-Signature=2cf978a1f4a5b4bfbf7aebad7e8a7fc0b68bf391c1c295f65633e394571a9857&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667644WZON%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEEIKudeA%2F9ywzcIo9ZcnYIZRtWLOdVwIqsyXP12V%2FpeAiEA9FtK44WWm5UYsueT%2FowwstCEmoJf7Ns0tUmT26zk7GsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuEkhlAv43U%2FfNwHCrcA3GuQTKBnYjFqSnRWJIMTQhj5horswb9O6fi0SkeMn9YGLiaU7jaSpn5oMhqpMoHP0WFzLmf3Oai%2BFEv2wcj50lSGTJEF8yG7dfsYWUf2WNg3CpnJirZ6eztO5AcfjegXnwWCwcUR2BPW69Sz7j3BroFt3VbWMs%2B%2FQrCS2zLWadyCmBxfJxMoLMzDXwDxxQpc6J7TM07wAydV2CEy%2FuhcDLd5gZK4bOFqpU7zrdzHRPc7U9Sv4bY8VFZxezgoQtATqBV1BngTrB84klVBSGIKT4UCzI9yXkcXCYvf91qE0H9eCHxW90yLMw0qta4Bjg0csREA6Qoh%2FRDM0ngTS4D7WovwSd%2BvCYI%2B9dhwpAwxWwcnID%2FpMosL9YR1bdQuvl1bYtRJP2BeKgqf0oRcQyr9Fi0NpB26VKdLCHGlVOFYul2eiYauw6iNcpssGJoFQ%2FdEItH99CXbXr%2B2rupmu6BaN4izSuHk2PwJ9iYBKeFQS%2Bx3nx0cZK%2F7FDCS2%2FsEfnE2VY6FmNP6gr%2BqgwOxfVqlJstTxkyvKa0hpJ71BzSJzGxCNjhvVOuj9S%2BXv1MsRJkaYWXoqYUkVpvY5skY4ujz0j4%2BnybSCrbSU4fjXRY4E0Z2YgGGUBmIgNNc0yLMP26gb0GOqUBo%2Bzn3%2BewyytOqMGbsIzYSPzekIOV6an%2Bgkcc4pPM%2Bo%2BNleKMeXP1MdIKYwlcO3%2BR1zJIfyaWXuCWGAkO%2BhvBRKb%2FqnH7WCZII4rM4o4qqqTMcMbX1ar48uxbZ6oDhWjHTKvSMzxbtcBH1IGa5Y1CKEQrRIj8d%2FVc4%2BDf8ePqiuZW8mwW6m6yvqkBXRwvVOsRtPz8%2F1t%2Bq9Gf7FbUeIRtMnVo10pV&X-Amz-Signature=fb71bf924312aa0a7ba105c2c838405821fb2c1b407eea260a1a18bdeceb3d95&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667644WZON%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEEIKudeA%2F9ywzcIo9ZcnYIZRtWLOdVwIqsyXP12V%2FpeAiEA9FtK44WWm5UYsueT%2FowwstCEmoJf7Ns0tUmT26zk7GsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOuEkhlAv43U%2FfNwHCrcA3GuQTKBnYjFqSnRWJIMTQhj5horswb9O6fi0SkeMn9YGLiaU7jaSpn5oMhqpMoHP0WFzLmf3Oai%2BFEv2wcj50lSGTJEF8yG7dfsYWUf2WNg3CpnJirZ6eztO5AcfjegXnwWCwcUR2BPW69Sz7j3BroFt3VbWMs%2B%2FQrCS2zLWadyCmBxfJxMoLMzDXwDxxQpc6J7TM07wAydV2CEy%2FuhcDLd5gZK4bOFqpU7zrdzHRPc7U9Sv4bY8VFZxezgoQtATqBV1BngTrB84klVBSGIKT4UCzI9yXkcXCYvf91qE0H9eCHxW90yLMw0qta4Bjg0csREA6Qoh%2FRDM0ngTS4D7WovwSd%2BvCYI%2B9dhwpAwxWwcnID%2FpMosL9YR1bdQuvl1bYtRJP2BeKgqf0oRcQyr9Fi0NpB26VKdLCHGlVOFYul2eiYauw6iNcpssGJoFQ%2FdEItH99CXbXr%2B2rupmu6BaN4izSuHk2PwJ9iYBKeFQS%2Bx3nx0cZK%2F7FDCS2%2FsEfnE2VY6FmNP6gr%2BqgwOxfVqlJstTxkyvKa0hpJ71BzSJzGxCNjhvVOuj9S%2BXv1MsRJkaYWXoqYUkVpvY5skY4ujz0j4%2BnybSCrbSU4fjXRY4E0Z2YgGGUBmIgNNc0yLMP26gb0GOqUBo%2Bzn3%2BewyytOqMGbsIzYSPzekIOV6an%2Bgkcc4pPM%2Bo%2BNleKMeXP1MdIKYwlcO3%2BR1zJIfyaWXuCWGAkO%2BhvBRKb%2FqnH7WCZII4rM4o4qqqTMcMbX1ar48uxbZ6oDhWjHTKvSMzxbtcBH1IGa5Y1CKEQrRIj8d%2FVc4%2BDf8ePqiuZW8mwW6m6yvqkBXRwvVOsRtPz8%2F1t%2Bq9Gf7FbUeIRtMnVo10pV&X-Amz-Signature=685363419e1602abea98bdc7ceb87e3afc05a5e48939ed837a723086d8688a25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUVRSD7R%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBnRtZZmkKkWzN%2B1WBSd6VzhPpTfu5MtlxyoUGWvBrj7AiAm2gGMfTNY8VB6rvkpmu5Dg20RiHHX6R%2FHUU3qnFsiISqIBAj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM78z8FDytmdJrS8D8KtwDAfDxP%2FvC8XzX275C4bM3kDO7OXfiuJYRSxJ3ea5o%2BqDADieiSR6W%2BI758VjuxmoPaAE%2FvfHCbWmmQvA1E3HTOwZFf2Ii%2FrRkIpyX9yVnAj2XvUlbbnzeMLJUqJPoM1R4%2BGyNM7KToBZY%2FM98VFfkGnc8d1ZjAm3TcYAhFfeYmq09L9YzrfQnnBj2wbym%2F6i73FETvGakT9JqvV8ozqLL1Ng8qb8WjSvceHaq%2FJMr5ypNU5D%2F0Isp0LT%2BTPd00DsM9v163JN9J4WbUHteR84MtW57iejfwcqJyjTrEgNYUz%2FuiX7s8U3mAoROk85CqIO8ieTfrcIZn6vpDqjsKcuBUz1rWU1BgRskfqFTazI7fHGjgI5mxIN%2FsqzyjFK6G5GFSfJytB7UMpzTX5qGNOE8ICSYPeMgObIBWGOsMoizE2%2B0YYLa8%2FahdV3IbiZ0Velpo4zDfjFOqwgXrRHoYLToUCDgg9F1ui18%2FGIrKH9DB1Kqq2ehoQRHDRbaXKRob1sXezQ1ZxaS8lZlJ97KVQRZoDpEjrgKdxpEbfPGq82c3zXY03oMdNQDRj02bOl5zc%2FNWAB3sBjZnbrMag1oI%2BQoQmvOLnseD0vtRf5ZtUzb%2F1TYFcBTjH32%2FUU%2BzNowj7qBvQY6pgHWm4UmrnM%2Bx8%2F6llNP9IpHx5tOcUPVoWkPVtd5EPX3C7%2B%2FB%2B9nMk6GzMa7UFr53%2BzyDv6wJU%2B7HwiKJhVIzrjIMeo1LgYn%2BhpaJ8c1KKLKnWn5ARXows%2FoY74MqpB18fhHnXdj7uVuKBhIhZFAsnXGRVy%2FaeZE0XcXKGZ18iIKl69FLiGVs%2BZzhMUiI2GOzef3rbjEPhz%2Bg3BHtO44Yz5UWBsIh9BK&X-Amz-Signature=6084cece2d8c7f0502a85049bbfa218a8423978b08b4c2a3a0ec085518034e20&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRQWGOYM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0bTYCDb8lllRfZgtOotrOaKSgCHdGcX%2BaASM%2F9pHPyQIgfAYjV68Gi5uSLWtexz9pO0w1haTq9ZJpGpdDw7q0W%2B0qiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDECV7eVUm17uVdmY6CrcA2i7JQvuwVd9BrdLUh9ULa2d0iY3B1NZUYXAklcR7ttT1EbPxtihLcRH6aU8FhKcMbekADibc5b7tOEHeBbvy2w6xQIDla8lCNutjq4rKpfNxyVac1zbY%2Bzoz%2BbvK8DHbIqk0U6jCoGFZSV4zXuYaxK9DzAtSYqQTJ0XuplknvmvtWMncJPW%2B4V31xIiajgZPPd3i79mszi4Ta7xp39BymwQ0x5LuWaKV%2FaN28aT4WbO9fEAUgxdUvA0azqJlWGrFi2U15ZAEZLPJhvGWqrqJXfWqXDTvTRQ2m8vrayBj4k9rPeeaZipClcKYSGukDm29S2jtES6zP4i%2BPVTumBsAXUpMND4WtnoJxtwwHP8jtvyirZ9iejKWWiT5XlIjN7RqCEDLcIW%2FNp55Hc%2BHYgrLx%2B3pri5KqBFHcMGnbywowxAw2pGD90TOMINknnMkqmZ8%2FGVScKPyIs%2B7BceM2vxAw1DbloWDxfxmMdriUgxAcWcxpxoC%2BoEN4UKhj%2BuPZXN%2BjImcp9vKLl5Ep40%2BUitaoWM1LpqFqDd675CmOgQUlunYQMTcuJ4Eo56JF8twKXZYQZ4viHgzJl79l1HOoN8J%2BH%2FpGm2rPyLDPAY%2BVJ6j20e9aaRZooTsq65pMNdMNu6gb0GOqUBTG1svr9pQWMGy0ofV%2B9xjfeXJVxIS9jg1uA2fbCsYpdLzKIZnKLY9C1rRAG3JbdPGk5%2BcdtLlNUh1uVAnpszPVH5F79d8dueUcYL0xOcZ1Ohe%2FmwVTEzjNQ4isEfLRuC22RGz7LPsEDzK4OUKwtKvXrZWwEFTelbywgVkYKd08Jqtn4meaKZNwziYX3jqOWWca6r5ZeIT0xQOkDwJLfw1g%2B4AMZF&X-Amz-Signature=af0e35105a49c36567cd04a65834c14acc63464ce2a30fc606cfb9fca7698dbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YS4GMEF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICPROm%2Fu%2Fto5ckdk8durrXRNxXm7Yp3YwSJi15j1uGaFAiEAuLEnelR2K%2F3KgHtXjDZKAWjXexvBpCDp5SCWbH%2B7wWsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFYG00zOcjhEsEtHMCrcA30hDrRC3s%2Be28yCA80cC8G7SUZHNxoN4bMCEOPu7Txzcek5JIGJfsEIIRZX%2B37jyTovfWyMcPZVCozI4igLdEYFJUAbFNUgXA9T%2FBfYxGi94xyf0xDTwmYXCntyw%2BusnjEszX2uMH945HCWbmkxivmyCcIFO2FqTIfOGpp4jFI5n0TIjTpjto1USNWDVM7Q5ykm2hREm8JbumfBgFLARN2zGyxWLRYVt6amE472DeYj9DJ2CFhO3mnEGJpwyqLPQBSwk8jx9q%2F19ZCZSEDn5Q5%2FQ0ZcRMk%2Fv6uG8oGmMh0q%2F4rkpefpQAUpRbPrUhY1MHacqPLRcfBxYrHVJOlPFA%2FoW%2FDptrLf5FcvKn39EBhDBoBTFYN0LE1IkReCVWCsoSh%2BRVxF2EREL4Rg6md4jYOwn7bHW0fjKeri4UYtA5zfB4dJdlm6Qoc0Ky8UtPo4lMvJbqA41a9IwqQte%2BgmTnhEqt9qLKw0CjeGPZ7Bjbw5DDNXAL6%2FkPjKYwD5PEPZbFgEIqoxSNKw9jviRxb6P6MaAByipPcyX17lYTG%2Fe0nae%2FnrWn0riyiaN7KnY50b3WDw9xcZ4Tg9srX3jn5XK%2F6s%2BGGfwIQCxl1NjlxRuzRabFqIhAa6Fqm8GCFoMPu5gb0GOqUBzQSIzkM8UCH5raEBuS0yzfVhhgMJf28sFPS0P4CqG941IEv2iw1%2FPTQkkxtCW99VEZ8YIscDN84QcGYI9tp2pD59blET6IDRuUId6paia%2BRPfequSi0sPOTZaQyWg87yW1qmkuAyJHo8c%2BH5K2QMN3XZHgVrIWirzGwTTEOANgm2Qz3w9hKtk1AbWJUojWXX1LayNyFidK16xegCijd259dQljsU&X-Amz-Signature=adc8dd8b2461fd633a08d85a4a7482b61709fd4345d6a45474a4223324fc8f64&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YS4GMEF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICPROm%2Fu%2Fto5ckdk8durrXRNxXm7Yp3YwSJi15j1uGaFAiEAuLEnelR2K%2F3KgHtXjDZKAWjXexvBpCDp5SCWbH%2B7wWsqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFYG00zOcjhEsEtHMCrcA30hDrRC3s%2Be28yCA80cC8G7SUZHNxoN4bMCEOPu7Txzcek5JIGJfsEIIRZX%2B37jyTovfWyMcPZVCozI4igLdEYFJUAbFNUgXA9T%2FBfYxGi94xyf0xDTwmYXCntyw%2BusnjEszX2uMH945HCWbmkxivmyCcIFO2FqTIfOGpp4jFI5n0TIjTpjto1USNWDVM7Q5ykm2hREm8JbumfBgFLARN2zGyxWLRYVt6amE472DeYj9DJ2CFhO3mnEGJpwyqLPQBSwk8jx9q%2F19ZCZSEDn5Q5%2FQ0ZcRMk%2Fv6uG8oGmMh0q%2F4rkpefpQAUpRbPrUhY1MHacqPLRcfBxYrHVJOlPFA%2FoW%2FDptrLf5FcvKn39EBhDBoBTFYN0LE1IkReCVWCsoSh%2BRVxF2EREL4Rg6md4jYOwn7bHW0fjKeri4UYtA5zfB4dJdlm6Qoc0Ky8UtPo4lMvJbqA41a9IwqQte%2BgmTnhEqt9qLKw0CjeGPZ7Bjbw5DDNXAL6%2FkPjKYwD5PEPZbFgEIqoxSNKw9jviRxb6P6MaAByipPcyX17lYTG%2Fe0nae%2FnrWn0riyiaN7KnY50b3WDw9xcZ4Tg9srX3jn5XK%2F6s%2BGGfwIQCxl1NjlxRuzRabFqIhAa6Fqm8GCFoMPu5gb0GOqUBzQSIzkM8UCH5raEBuS0yzfVhhgMJf28sFPS0P4CqG941IEv2iw1%2FPTQkkxtCW99VEZ8YIscDN84QcGYI9tp2pD59blET6IDRuUId6paia%2BRPfequSi0sPOTZaQyWg87yW1qmkuAyJHo8c%2BH5K2QMN3XZHgVrIWirzGwTTEOANgm2Qz3w9hKtk1AbWJUojWXX1LayNyFidK16xegCijd259dQljsU&X-Amz-Signature=aa212df222fc1b83d6ab09edf39aaea57f73134ca489ad2710fcd46d2e41e7ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
