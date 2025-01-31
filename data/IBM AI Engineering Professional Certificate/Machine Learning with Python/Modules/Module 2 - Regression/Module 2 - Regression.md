

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOURPDO2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFuWdrxklad%2Fzf%2BhfBI29QkzoPvZymmdj7W6oqkKv%2FdjAiEA355kmmtT5Pt3e7H3xG9Pn6S5bruX3b%2BGX6bE2KYrFyIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAgiijitP90oc0KjWircA6kGzd5Qt75B%2BkEmvBBaUP9Ed%2FWp9UmbKnqt5v45mH1dWJaqRk4MbPYoBsEMEH8LZ293NqNjqDeV0tL3N5CUV3ggD3uwT5r7F1L9nrOd9mqOksPRwhkeUixAkjpzMc9uWZYKclnx8BoS2gYimIpceL7s8B2JKoRisvr7vTEsV7Eedhwl07rh5dhDK0fLQXEdfiwHoBEkCBiWeOOkRLOnQnMEVEouorYEY1OTuquteB7K%2FXZD%2BAjRlM138fi4ZYMcYKDkuowZtx1y2RIghXtSXIeYv1m99STSd4HN%2FUFqAF8CZjdwmcAt%2FGf1VawNXg035okLO%2BhftTR0qXa0UcavduX9srYJu8XeMY53zAjsqtcKVo%2BNBpIr4pNOtUleWJluig0yBv4IxQ1Cd%2F8jl8oJz8j4eMuxSSjq3pnQDLwq7NPB8%2Fz4uGcEWdLADitNzusKgC7KivFsQdJomoVjVKV2M5ipffnIdHKh%2FN146UNmbHTRs7y9mZCTr9eKtmis6gkdSZO1xdPq7MCZCFrSa641L6naEb9Ymc6e4rmnPHRtKEiQyV3wX0s8bMEELvg0WFOWwDl8E%2Fd2lLF4J66059cCS11dZj25Bxz0Vsu4wLFEQVAAo2oulojH3Nwopg%2FJMKP49LwGOqUB2sCcE5J3rXD0diWVvoyLKgI40Yk0iwb4ZEnW0oGd5SlVyflaZyVMP6mu%2BlFPX5qzm9OCVw3wBhAwD4BINrFq6h5VB6vQew4GwXUVlCQCPsFQbS7w7AVozi4oWOa7%2FNYjaEeNkz%2Bg1EgMr6U209K7A%2FziehhS3gOozJIbqNS30d36Qg7Nu8C60i%2BuXzeOB4GxTpBk%2BJP8gXAflqF7IcOzGQH414XN&X-Amz-Signature=3804d8b2a18bf3c0c5743326558d223d92c52eb689c17ff391627530cfffb9b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOURPDO2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFuWdrxklad%2Fzf%2BhfBI29QkzoPvZymmdj7W6oqkKv%2FdjAiEA355kmmtT5Pt3e7H3xG9Pn6S5bruX3b%2BGX6bE2KYrFyIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAgiijitP90oc0KjWircA6kGzd5Qt75B%2BkEmvBBaUP9Ed%2FWp9UmbKnqt5v45mH1dWJaqRk4MbPYoBsEMEH8LZ293NqNjqDeV0tL3N5CUV3ggD3uwT5r7F1L9nrOd9mqOksPRwhkeUixAkjpzMc9uWZYKclnx8BoS2gYimIpceL7s8B2JKoRisvr7vTEsV7Eedhwl07rh5dhDK0fLQXEdfiwHoBEkCBiWeOOkRLOnQnMEVEouorYEY1OTuquteB7K%2FXZD%2BAjRlM138fi4ZYMcYKDkuowZtx1y2RIghXtSXIeYv1m99STSd4HN%2FUFqAF8CZjdwmcAt%2FGf1VawNXg035okLO%2BhftTR0qXa0UcavduX9srYJu8XeMY53zAjsqtcKVo%2BNBpIr4pNOtUleWJluig0yBv4IxQ1Cd%2F8jl8oJz8j4eMuxSSjq3pnQDLwq7NPB8%2Fz4uGcEWdLADitNzusKgC7KivFsQdJomoVjVKV2M5ipffnIdHKh%2FN146UNmbHTRs7y9mZCTr9eKtmis6gkdSZO1xdPq7MCZCFrSa641L6naEb9Ymc6e4rmnPHRtKEiQyV3wX0s8bMEELvg0WFOWwDl8E%2Fd2lLF4J66059cCS11dZj25Bxz0Vsu4wLFEQVAAo2oulojH3Nwopg%2FJMKP49LwGOqUB2sCcE5J3rXD0diWVvoyLKgI40Yk0iwb4ZEnW0oGd5SlVyflaZyVMP6mu%2BlFPX5qzm9OCVw3wBhAwD4BINrFq6h5VB6vQew4GwXUVlCQCPsFQbS7w7AVozi4oWOa7%2FNYjaEeNkz%2Bg1EgMr6U209K7A%2FziehhS3gOozJIbqNS30d36Qg7Nu8C60i%2BuXzeOB4GxTpBk%2BJP8gXAflqF7IcOzGQH414XN&X-Amz-Signature=6c6752e911266e348b7385dff128ab82a4d14a9aea41a5348a6dfc9ed46c30fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOURPDO2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFuWdrxklad%2Fzf%2BhfBI29QkzoPvZymmdj7W6oqkKv%2FdjAiEA355kmmtT5Pt3e7H3xG9Pn6S5bruX3b%2BGX6bE2KYrFyIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAgiijitP90oc0KjWircA6kGzd5Qt75B%2BkEmvBBaUP9Ed%2FWp9UmbKnqt5v45mH1dWJaqRk4MbPYoBsEMEH8LZ293NqNjqDeV0tL3N5CUV3ggD3uwT5r7F1L9nrOd9mqOksPRwhkeUixAkjpzMc9uWZYKclnx8BoS2gYimIpceL7s8B2JKoRisvr7vTEsV7Eedhwl07rh5dhDK0fLQXEdfiwHoBEkCBiWeOOkRLOnQnMEVEouorYEY1OTuquteB7K%2FXZD%2BAjRlM138fi4ZYMcYKDkuowZtx1y2RIghXtSXIeYv1m99STSd4HN%2FUFqAF8CZjdwmcAt%2FGf1VawNXg035okLO%2BhftTR0qXa0UcavduX9srYJu8XeMY53zAjsqtcKVo%2BNBpIr4pNOtUleWJluig0yBv4IxQ1Cd%2F8jl8oJz8j4eMuxSSjq3pnQDLwq7NPB8%2Fz4uGcEWdLADitNzusKgC7KivFsQdJomoVjVKV2M5ipffnIdHKh%2FN146UNmbHTRs7y9mZCTr9eKtmis6gkdSZO1xdPq7MCZCFrSa641L6naEb9Ymc6e4rmnPHRtKEiQyV3wX0s8bMEELvg0WFOWwDl8E%2Fd2lLF4J66059cCS11dZj25Bxz0Vsu4wLFEQVAAo2oulojH3Nwopg%2FJMKP49LwGOqUB2sCcE5J3rXD0diWVvoyLKgI40Yk0iwb4ZEnW0oGd5SlVyflaZyVMP6mu%2BlFPX5qzm9OCVw3wBhAwD4BINrFq6h5VB6vQew4GwXUVlCQCPsFQbS7w7AVozi4oWOa7%2FNYjaEeNkz%2Bg1EgMr6U209K7A%2FziehhS3gOozJIbqNS30d36Qg7Nu8C60i%2BuXzeOB4GxTpBk%2BJP8gXAflqF7IcOzGQH414XN&X-Amz-Signature=ac23dafc7a360ba9e3af0625fc1d2b89effc14943cb34af845eba311523e8c53&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOURPDO2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFuWdrxklad%2Fzf%2BhfBI29QkzoPvZymmdj7W6oqkKv%2FdjAiEA355kmmtT5Pt3e7H3xG9Pn6S5bruX3b%2BGX6bE2KYrFyIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAgiijitP90oc0KjWircA6kGzd5Qt75B%2BkEmvBBaUP9Ed%2FWp9UmbKnqt5v45mH1dWJaqRk4MbPYoBsEMEH8LZ293NqNjqDeV0tL3N5CUV3ggD3uwT5r7F1L9nrOd9mqOksPRwhkeUixAkjpzMc9uWZYKclnx8BoS2gYimIpceL7s8B2JKoRisvr7vTEsV7Eedhwl07rh5dhDK0fLQXEdfiwHoBEkCBiWeOOkRLOnQnMEVEouorYEY1OTuquteB7K%2FXZD%2BAjRlM138fi4ZYMcYKDkuowZtx1y2RIghXtSXIeYv1m99STSd4HN%2FUFqAF8CZjdwmcAt%2FGf1VawNXg035okLO%2BhftTR0qXa0UcavduX9srYJu8XeMY53zAjsqtcKVo%2BNBpIr4pNOtUleWJluig0yBv4IxQ1Cd%2F8jl8oJz8j4eMuxSSjq3pnQDLwq7NPB8%2Fz4uGcEWdLADitNzusKgC7KivFsQdJomoVjVKV2M5ipffnIdHKh%2FN146UNmbHTRs7y9mZCTr9eKtmis6gkdSZO1xdPq7MCZCFrSa641L6naEb9Ymc6e4rmnPHRtKEiQyV3wX0s8bMEELvg0WFOWwDl8E%2Fd2lLF4J66059cCS11dZj25Bxz0Vsu4wLFEQVAAo2oulojH3Nwopg%2FJMKP49LwGOqUB2sCcE5J3rXD0diWVvoyLKgI40Yk0iwb4ZEnW0oGd5SlVyflaZyVMP6mu%2BlFPX5qzm9OCVw3wBhAwD4BINrFq6h5VB6vQew4GwXUVlCQCPsFQbS7w7AVozi4oWOa7%2FNYjaEeNkz%2Bg1EgMr6U209K7A%2FziehhS3gOozJIbqNS30d36Qg7Nu8C60i%2BuXzeOB4GxTpBk%2BJP8gXAflqF7IcOzGQH414XN&X-Amz-Signature=da1600cd0dfa695c7826d7f686643baa65a501f2326a3eb964b9500179dfdb8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOURPDO2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFuWdrxklad%2Fzf%2BhfBI29QkzoPvZymmdj7W6oqkKv%2FdjAiEA355kmmtT5Pt3e7H3xG9Pn6S5bruX3b%2BGX6bE2KYrFyIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAgiijitP90oc0KjWircA6kGzd5Qt75B%2BkEmvBBaUP9Ed%2FWp9UmbKnqt5v45mH1dWJaqRk4MbPYoBsEMEH8LZ293NqNjqDeV0tL3N5CUV3ggD3uwT5r7F1L9nrOd9mqOksPRwhkeUixAkjpzMc9uWZYKclnx8BoS2gYimIpceL7s8B2JKoRisvr7vTEsV7Eedhwl07rh5dhDK0fLQXEdfiwHoBEkCBiWeOOkRLOnQnMEVEouorYEY1OTuquteB7K%2FXZD%2BAjRlM138fi4ZYMcYKDkuowZtx1y2RIghXtSXIeYv1m99STSd4HN%2FUFqAF8CZjdwmcAt%2FGf1VawNXg035okLO%2BhftTR0qXa0UcavduX9srYJu8XeMY53zAjsqtcKVo%2BNBpIr4pNOtUleWJluig0yBv4IxQ1Cd%2F8jl8oJz8j4eMuxSSjq3pnQDLwq7NPB8%2Fz4uGcEWdLADitNzusKgC7KivFsQdJomoVjVKV2M5ipffnIdHKh%2FN146UNmbHTRs7y9mZCTr9eKtmis6gkdSZO1xdPq7MCZCFrSa641L6naEb9Ymc6e4rmnPHRtKEiQyV3wX0s8bMEELvg0WFOWwDl8E%2Fd2lLF4J66059cCS11dZj25Bxz0Vsu4wLFEQVAAo2oulojH3Nwopg%2FJMKP49LwGOqUB2sCcE5J3rXD0diWVvoyLKgI40Yk0iwb4ZEnW0oGd5SlVyflaZyVMP6mu%2BlFPX5qzm9OCVw3wBhAwD4BINrFq6h5VB6vQew4GwXUVlCQCPsFQbS7w7AVozi4oWOa7%2FNYjaEeNkz%2Bg1EgMr6U209K7A%2FziehhS3gOozJIbqNS30d36Qg7Nu8C60i%2BuXzeOB4GxTpBk%2BJP8gXAflqF7IcOzGQH414XN&X-Amz-Signature=3785db3629ff853ce6319ecf5baf2a4e5dfc2f4e4388c250afcbc603650145df&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOURPDO2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFuWdrxklad%2Fzf%2BhfBI29QkzoPvZymmdj7W6oqkKv%2FdjAiEA355kmmtT5Pt3e7H3xG9Pn6S5bruX3b%2BGX6bE2KYrFyIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAgiijitP90oc0KjWircA6kGzd5Qt75B%2BkEmvBBaUP9Ed%2FWp9UmbKnqt5v45mH1dWJaqRk4MbPYoBsEMEH8LZ293NqNjqDeV0tL3N5CUV3ggD3uwT5r7F1L9nrOd9mqOksPRwhkeUixAkjpzMc9uWZYKclnx8BoS2gYimIpceL7s8B2JKoRisvr7vTEsV7Eedhwl07rh5dhDK0fLQXEdfiwHoBEkCBiWeOOkRLOnQnMEVEouorYEY1OTuquteB7K%2FXZD%2BAjRlM138fi4ZYMcYKDkuowZtx1y2RIghXtSXIeYv1m99STSd4HN%2FUFqAF8CZjdwmcAt%2FGf1VawNXg035okLO%2BhftTR0qXa0UcavduX9srYJu8XeMY53zAjsqtcKVo%2BNBpIr4pNOtUleWJluig0yBv4IxQ1Cd%2F8jl8oJz8j4eMuxSSjq3pnQDLwq7NPB8%2Fz4uGcEWdLADitNzusKgC7KivFsQdJomoVjVKV2M5ipffnIdHKh%2FN146UNmbHTRs7y9mZCTr9eKtmis6gkdSZO1xdPq7MCZCFrSa641L6naEb9Ymc6e4rmnPHRtKEiQyV3wX0s8bMEELvg0WFOWwDl8E%2Fd2lLF4J66059cCS11dZj25Bxz0Vsu4wLFEQVAAo2oulojH3Nwopg%2FJMKP49LwGOqUB2sCcE5J3rXD0diWVvoyLKgI40Yk0iwb4ZEnW0oGd5SlVyflaZyVMP6mu%2BlFPX5qzm9OCVw3wBhAwD4BINrFq6h5VB6vQew4GwXUVlCQCPsFQbS7w7AVozi4oWOa7%2FNYjaEeNkz%2Bg1EgMr6U209K7A%2FziehhS3gOozJIbqNS30d36Qg7Nu8C60i%2BuXzeOB4GxTpBk%2BJP8gXAflqF7IcOzGQH414XN&X-Amz-Signature=2880e6941356ae370ad0ac49ed4b4f176fe89bdf62b072004008caaa84556be5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOURPDO2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFuWdrxklad%2Fzf%2BhfBI29QkzoPvZymmdj7W6oqkKv%2FdjAiEA355kmmtT5Pt3e7H3xG9Pn6S5bruX3b%2BGX6bE2KYrFyIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAgiijitP90oc0KjWircA6kGzd5Qt75B%2BkEmvBBaUP9Ed%2FWp9UmbKnqt5v45mH1dWJaqRk4MbPYoBsEMEH8LZ293NqNjqDeV0tL3N5CUV3ggD3uwT5r7F1L9nrOd9mqOksPRwhkeUixAkjpzMc9uWZYKclnx8BoS2gYimIpceL7s8B2JKoRisvr7vTEsV7Eedhwl07rh5dhDK0fLQXEdfiwHoBEkCBiWeOOkRLOnQnMEVEouorYEY1OTuquteB7K%2FXZD%2BAjRlM138fi4ZYMcYKDkuowZtx1y2RIghXtSXIeYv1m99STSd4HN%2FUFqAF8CZjdwmcAt%2FGf1VawNXg035okLO%2BhftTR0qXa0UcavduX9srYJu8XeMY53zAjsqtcKVo%2BNBpIr4pNOtUleWJluig0yBv4IxQ1Cd%2F8jl8oJz8j4eMuxSSjq3pnQDLwq7NPB8%2Fz4uGcEWdLADitNzusKgC7KivFsQdJomoVjVKV2M5ipffnIdHKh%2FN146UNmbHTRs7y9mZCTr9eKtmis6gkdSZO1xdPq7MCZCFrSa641L6naEb9Ymc6e4rmnPHRtKEiQyV3wX0s8bMEELvg0WFOWwDl8E%2Fd2lLF4J66059cCS11dZj25Bxz0Vsu4wLFEQVAAo2oulojH3Nwopg%2FJMKP49LwGOqUB2sCcE5J3rXD0diWVvoyLKgI40Yk0iwb4ZEnW0oGd5SlVyflaZyVMP6mu%2BlFPX5qzm9OCVw3wBhAwD4BINrFq6h5VB6vQew4GwXUVlCQCPsFQbS7w7AVozi4oWOa7%2FNYjaEeNkz%2Bg1EgMr6U209K7A%2FziehhS3gOozJIbqNS30d36Qg7Nu8C60i%2BuXzeOB4GxTpBk%2BJP8gXAflqF7IcOzGQH414XN&X-Amz-Signature=fc064c0de1d0d5eb2c2a7c4794f22f21f83b97cbea322f5e767ab2c7c918fea8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOURPDO2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFuWdrxklad%2Fzf%2BhfBI29QkzoPvZymmdj7W6oqkKv%2FdjAiEA355kmmtT5Pt3e7H3xG9Pn6S5bruX3b%2BGX6bE2KYrFyIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAgiijitP90oc0KjWircA6kGzd5Qt75B%2BkEmvBBaUP9Ed%2FWp9UmbKnqt5v45mH1dWJaqRk4MbPYoBsEMEH8LZ293NqNjqDeV0tL3N5CUV3ggD3uwT5r7F1L9nrOd9mqOksPRwhkeUixAkjpzMc9uWZYKclnx8BoS2gYimIpceL7s8B2JKoRisvr7vTEsV7Eedhwl07rh5dhDK0fLQXEdfiwHoBEkCBiWeOOkRLOnQnMEVEouorYEY1OTuquteB7K%2FXZD%2BAjRlM138fi4ZYMcYKDkuowZtx1y2RIghXtSXIeYv1m99STSd4HN%2FUFqAF8CZjdwmcAt%2FGf1VawNXg035okLO%2BhftTR0qXa0UcavduX9srYJu8XeMY53zAjsqtcKVo%2BNBpIr4pNOtUleWJluig0yBv4IxQ1Cd%2F8jl8oJz8j4eMuxSSjq3pnQDLwq7NPB8%2Fz4uGcEWdLADitNzusKgC7KivFsQdJomoVjVKV2M5ipffnIdHKh%2FN146UNmbHTRs7y9mZCTr9eKtmis6gkdSZO1xdPq7MCZCFrSa641L6naEb9Ymc6e4rmnPHRtKEiQyV3wX0s8bMEELvg0WFOWwDl8E%2Fd2lLF4J66059cCS11dZj25Bxz0Vsu4wLFEQVAAo2oulojH3Nwopg%2FJMKP49LwGOqUB2sCcE5J3rXD0diWVvoyLKgI40Yk0iwb4ZEnW0oGd5SlVyflaZyVMP6mu%2BlFPX5qzm9OCVw3wBhAwD4BINrFq6h5VB6vQew4GwXUVlCQCPsFQbS7w7AVozi4oWOa7%2FNYjaEeNkz%2Bg1EgMr6U209K7A%2FziehhS3gOozJIbqNS30d36Qg7Nu8C60i%2BuXzeOB4GxTpBk%2BJP8gXAflqF7IcOzGQH414XN&X-Amz-Signature=0b830f6902cff01e40d428bba1c16cde335c4c21a6ecfc2af0cd96416cdedb9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PMP44SP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQac5JN2BxhJApWTAvvC9kE8HZGp2V8f%2BT3pgZTYRsCAiAiu9tyscUklR3t8zHFTKoIFukODbz2L2kYYSbXmoFotiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrxKV907WQEA9%2B528KtwDe9MYMt%2Fpq8%2FrDZ89C%2FP7rRic4y6riD6LmHVATD8rgHg3mTMOSQpxN7z9v%2FwlkFwHKudeKwD%2F92nz8aueYofaeEWXT91SFHb7nOaGUMJ7uwI2C7kl1N%2BainZl4wfogiNMq3ECMH%2FfSQIDpmZnkU40AVFkI4ojnt8Uq3T%2BCUnjZHuiOOrzu8VWja%2Ff7vwXnGrteWvBeSkyiEXIDXkJ2SkGDhh3zAnqpeYYk4dmPsWRvioVwNt5LU%2BrAS8T%2F%2F5EPNS4JpQpIf7Stbh2g6vVR13tr6eRmEN%2FlpHG4NHTE%2BTeUCNPoW0c96dEl0foziMFhMF5UPOzFgTFncTEbl36mQeTj6EssV4sPF2MUI88Pgs3PtpMFfQZ6gn16Yzf3euVZPKUzxaXG5ckOarTvfmq8nliJtRWmH%2FuQES8h9JyGoQeoBTGceTtleN5gwQFbeH5w%2BrvF6vhDPQUHJT1rGwT6rytthrXTBncoU0ws8%2FFTu8uKVJZXAjIuyv94%2F%2Byt6ovBGB9MpLO6eP8oJDxto64kLb7Ump%2BhKwpwD7W8QDkoEYjjDLCBg9NpTay%2FRqhaQNL29arKI0AzPcNZQvF1Y8%2BOBCHyClsjqrZQE0l1lqRfGSR80f1vxN%2BYPzui5SzB1Mwu%2Fj0vAY6pgG0o1p8hPL1faTqERb73Kid%2BANKtUv3HUCbsrwd%2F4i0Ahd5oEWkTX30IaIQanNfKLq8NSmjAAMjsmb7UD1kjpC64FpiV07jJuScNDS7tjHm6DB1CQ9PtjyZFs8lSwNzbb6DMDDGa3WgPovzIoZCytfaxKpjxNhGc07NOBdTlYKudvteeNs0lx9iBI4xmsPkh4Kz8N1689TX22Ktw60DwPjoqVDzy0sW&X-Amz-Signature=b8f6543d9c6b665de64c6cab0729d5843cdbb570cf489c4f421b847f510a5f3d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663D35ELO3%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICdCc4Hfb2X4WV0t%2FdlkUnzPQyCBIXueJHITlXo2jjQcAiEAibIOiL6F6Fjwqi0MkXnFNi56QAFj4MlmmTyCUHS5V7IqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDs3ST6tLALBGilCByrcA7Dm0QF5iPqQtdzY7Fn022TXveWT1k6wifCfGxU2V%2FM5mURRXqDUroJmIx9bsN%2B2gCIJLu6ttI9BwATQGfTRsu%2BYQlDLcEdy4akJrtX2pmdhzXUK8Lk9jS6g0TvpVolXP7hqahDK6UYFOxieZQcL791gjREXwwS4SroY534%2F3VkFTGwm9p%2BkXisAcihZ3xyp4hteiY3ZC1xsA9BZXLx%2BsA4tlg3J4VOnC89Yn%2Bngnmdhqnv5r2QfNln9%2FhiCOxA2FT3RjyqdNbAavTWUpNhk7ns84sDTqWuBE8cghDoU08kmaadOdZwc6uI3sjnOFiRIiPnWJ33WyyBLyvnc6I9oVPG4oF%2BTToZg%2FxjItPLGBMaKyc3vymcyo6Tikjd3x7PZgEP%2B4%2FyP0cNhTVsXfmOKYGqCC0838tCIOFZp%2Bz3WIHHkMJb2Qa75X3MeukOxVi2p4%2FsMvhVrFUfhuwvtUC7T5nfxgK2fACyuUMVdEse6CKrFcmain2Ja2XdKHpGidso2JVIgu7ahLqy8sQwurGx75UwFg9Mj3UWHpd4T37y2oYeyMcev1SlN4N1Jl%2B9MnbalFR9cIFiZeviWBjtAUXSFZ%2FKq6MWOxs%2BPhSyqD%2FhzAGFLySo53L9HqLFum%2FQWMPT49LwGOqUBLwKFOH%2Fr6EPtDVQ%2B7QJ4b4um63G1vvg7sjn3dzRy1wVBIDlATCdR5JnzIA9HxOrHl73YW4ivASS4ykPWtsyD9LKMYitKeB3fy2koEXT9b9SrAFpp5%2Fz%2FSoi3sct0nPTBHEsQ1x%2BvGq2BNptOPzqD8feUBS6LjEWCV4n3bnFykIZkK%2FTpRIxPcdT8p%2BsD9YXq1ID875rjUtXb8EOZstrVTqhIWDS%2B&X-Amz-Signature=064d6ccddb8d8bff5756835e8159c63f07df6abb63ba8adea525f3776a7774f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVOS4JJY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmJQTTe2C8aX6Fxom4iwN8lvXXNWqqnywehM0L7zw6KAIgFejiyGAqujcLa9FEBMda25NeUYB3gkfZddZrSYn7WG8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO1H%2B%2Fo3GeG1olOSnSrcAxlU2MXYqzJobKfNSUBCV31RJNt4luiFKRDcqaLZHav4xH6rYfJtX%2B0YDopOTAO5B7nat7kagPVUfYVkibO85lfhLCC6idWbm%2B%2FOzK5y0rDV3HqrvBOn8yy2GbMyGXWD1PtBdSuRs%2BDwR9uLNDSgXitid3LAGJnW57O9VjQ9h%2BkOKNHw55WTDAH1AEUKKwV4LFHFTiZ5U3LPh9Cr%2BlouwGnuEd9M1iN3M2Y%2B5pZynYsVHn1pDZDJ532Mm2Nt3s8URkcMYqIkMoiBCXcSy2CbyqW0ng5g61n0yhZRmOG48eqphAHIz0zZFmq9kuj4qCFoexfllGSa0wU4rOYQMSGpvAZfSrx8Zjb%2FbIAbqtdAGXRdrLbAVW6NerjD9liFNrlOkZQDk41wRX%2Bfa0ImHaPrCkrI09xRTATbAydRdlNbAdNMSM3Fesne9vNoIkRZldMMTiwswh05ayAodBtCTym5c8lKXTCebda4YPBgRrbG2bzS0%2Fa8LjGML1xrSC4rFk4jpxtEXtjmhfZMyAM3J80IDyYup6gz%2F3f6sEdZRSN%2F9tW07PiCIIojOzsDlmnj9eWy0P7YlQ5Sn60LbNVTDEOvod86WNPkdJbjX%2F27ZkY%2FxSx19GkV%2F4vspXFpJPqzMJn49LwGOqUBm8rfpJFob%2FGcLB%2BF7HWUy4RPEsD4OW8ZlgXDUl1Tj0E7cstr2ipYd%2FIaF6NGkoiE42HdyRSDsg748HJLiqgatBDADR3aI0ZG23FlmKM%2Bw9DAUvQqL917nDLbaJVRX8jj%2FCwMVzbv1RbxveTsO7MH%2Bec2J9cENDOmT9yZnpvf3ehd3rBVpWDCrKTaFjYThTe2wbEhEbyL8UfSlaBm7E6CLduuXas5&X-Amz-Signature=584ed6de6c3468ae94f0e4b327390483ecafc78a741a9cdf0b84d8bc6d584aa8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVOS4JJY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T211317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmJQTTe2C8aX6Fxom4iwN8lvXXNWqqnywehM0L7zw6KAIgFejiyGAqujcLa9FEBMda25NeUYB3gkfZddZrSYn7WG8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO1H%2B%2Fo3GeG1olOSnSrcAxlU2MXYqzJobKfNSUBCV31RJNt4luiFKRDcqaLZHav4xH6rYfJtX%2B0YDopOTAO5B7nat7kagPVUfYVkibO85lfhLCC6idWbm%2B%2FOzK5y0rDV3HqrvBOn8yy2GbMyGXWD1PtBdSuRs%2BDwR9uLNDSgXitid3LAGJnW57O9VjQ9h%2BkOKNHw55WTDAH1AEUKKwV4LFHFTiZ5U3LPh9Cr%2BlouwGnuEd9M1iN3M2Y%2B5pZynYsVHn1pDZDJ532Mm2Nt3s8URkcMYqIkMoiBCXcSy2CbyqW0ng5g61n0yhZRmOG48eqphAHIz0zZFmq9kuj4qCFoexfllGSa0wU4rOYQMSGpvAZfSrx8Zjb%2FbIAbqtdAGXRdrLbAVW6NerjD9liFNrlOkZQDk41wRX%2Bfa0ImHaPrCkrI09xRTATbAydRdlNbAdNMSM3Fesne9vNoIkRZldMMTiwswh05ayAodBtCTym5c8lKXTCebda4YPBgRrbG2bzS0%2Fa8LjGML1xrSC4rFk4jpxtEXtjmhfZMyAM3J80IDyYup6gz%2F3f6sEdZRSN%2F9tW07PiCIIojOzsDlmnj9eWy0P7YlQ5Sn60LbNVTDEOvod86WNPkdJbjX%2F27ZkY%2FxSx19GkV%2F4vspXFpJPqzMJn49LwGOqUBm8rfpJFob%2FGcLB%2BF7HWUy4RPEsD4OW8ZlgXDUl1Tj0E7cstr2ipYd%2FIaF6NGkoiE42HdyRSDsg748HJLiqgatBDADR3aI0ZG23FlmKM%2Bw9DAUvQqL917nDLbaJVRX8jj%2FCwMVzbv1RbxveTsO7MH%2Bec2J9cENDOmT9yZnpvf3ehd3rBVpWDCrKTaFjYThTe2wbEhEbyL8UfSlaBm7E6CLduuXas5&X-Amz-Signature=47b6597c4d96831f149d19ae62c43aa8ef1173ab3a2320859858b04cccd503fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
