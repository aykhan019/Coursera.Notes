

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPZPNOGC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZ8jKqpyn2bTepTpnGua%2BJrGHPwq6y37CRv7RlgNlwJAiAafOiyADr5UBXDkqNg5eJAo1RIVyNWpm4DcPzAZrjlcyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHY22qerRFfWP0H0KtwDNnWq5F7TfSAHdNiXScPB%2BYGsYzl8NcrM34um%2FHdo6gpa5kLTtlfFFymqGac7U4DyXsZbJSj9luICTZyC1AqrJpT%2F0f6YtHbnnYUcnA3LCmFhHHQJreDqJdjXJ%2FOBmJlqvEinfpocXwA1NCrakLLUphCCuKnCJGTAu3RkinH%2BJT92ty10Ms619PQyosCih%2Byvkkksuou5ck36aXVif8kTl%2BCaZga7EdfmoVWmYWV76gLQff3k7DOLPcUU7nxkdFnsmPWAyDSDso0XThAWYxF%2BB9N5gO7kAJkcQHoISrvPT1iSgICThbiLv98KJC1diHBRx4bJ0FaJh%2BM8Y7bPNe6yHdVFdxHraAzV1SQ2TTTV%2BiiqcVRxoihM98dRNYUaOQtpP1elBZNVKyPppq2QOQEn60aY6el8ClnGl9Z71jDkWPaDmnxKo%2FwJIM5%2FMSRPeetiXgqvrTO4zY24Pfa1Kg31Iih1i0pWTKV0FVW%2FHGCo%2BQZvUxmb%2Bx7n7TWRrCmML70aoJVQhZI2BlG56g%2FIcHk8C2aZCx5Xp9W3jujcznga7V6S125xr8qiE85bs8tX4uh9lR52Z38Oeyxw0andDzjaVpSBJshH1yX5pPxMGZrDgmyBsyd8Oz%2F92OaGgvIw%2FaX2vAY6pgGcYLnnKQqSbECvJHOiqcMKRKiFOvtlTk8wYPAFg7QG0Bl9VMSf%2F5Te0dFF%2FTXFRhX3o61U7BG17lMYlePmYP9Dxa4SkQVUrSqkijtnOdvcN73F5Z7FUWxWNCKV8ZKy1Hq%2F8GtiigefDTMpslbGD%2FEEbu88XPdkMoThXVxqWHET0U9bitKil5jxI9K72dMOJl%2BYl3ITMA3lp6qgmeFd4nJyW74Lju50&X-Amz-Signature=fd1ac830cffa70ea4713be2570d910ad9461e0d64e334cb13c761d492ee87509&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPZPNOGC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZ8jKqpyn2bTepTpnGua%2BJrGHPwq6y37CRv7RlgNlwJAiAafOiyADr5UBXDkqNg5eJAo1RIVyNWpm4DcPzAZrjlcyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHY22qerRFfWP0H0KtwDNnWq5F7TfSAHdNiXScPB%2BYGsYzl8NcrM34um%2FHdo6gpa5kLTtlfFFymqGac7U4DyXsZbJSj9luICTZyC1AqrJpT%2F0f6YtHbnnYUcnA3LCmFhHHQJreDqJdjXJ%2FOBmJlqvEinfpocXwA1NCrakLLUphCCuKnCJGTAu3RkinH%2BJT92ty10Ms619PQyosCih%2Byvkkksuou5ck36aXVif8kTl%2BCaZga7EdfmoVWmYWV76gLQff3k7DOLPcUU7nxkdFnsmPWAyDSDso0XThAWYxF%2BB9N5gO7kAJkcQHoISrvPT1iSgICThbiLv98KJC1diHBRx4bJ0FaJh%2BM8Y7bPNe6yHdVFdxHraAzV1SQ2TTTV%2BiiqcVRxoihM98dRNYUaOQtpP1elBZNVKyPppq2QOQEn60aY6el8ClnGl9Z71jDkWPaDmnxKo%2FwJIM5%2FMSRPeetiXgqvrTO4zY24Pfa1Kg31Iih1i0pWTKV0FVW%2FHGCo%2BQZvUxmb%2Bx7n7TWRrCmML70aoJVQhZI2BlG56g%2FIcHk8C2aZCx5Xp9W3jujcznga7V6S125xr8qiE85bs8tX4uh9lR52Z38Oeyxw0andDzjaVpSBJshH1yX5pPxMGZrDgmyBsyd8Oz%2F92OaGgvIw%2FaX2vAY6pgGcYLnnKQqSbECvJHOiqcMKRKiFOvtlTk8wYPAFg7QG0Bl9VMSf%2F5Te0dFF%2FTXFRhX3o61U7BG17lMYlePmYP9Dxa4SkQVUrSqkijtnOdvcN73F5Z7FUWxWNCKV8ZKy1Hq%2F8GtiigefDTMpslbGD%2FEEbu88XPdkMoThXVxqWHET0U9bitKil5jxI9K72dMOJl%2BYl3ITMA3lp6qgmeFd4nJyW74Lju50&X-Amz-Signature=489394579219474276d0d5e497222a36888d7eacf0fe66dbc400b34ca402c526&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPZPNOGC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZ8jKqpyn2bTepTpnGua%2BJrGHPwq6y37CRv7RlgNlwJAiAafOiyADr5UBXDkqNg5eJAo1RIVyNWpm4DcPzAZrjlcyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHY22qerRFfWP0H0KtwDNnWq5F7TfSAHdNiXScPB%2BYGsYzl8NcrM34um%2FHdo6gpa5kLTtlfFFymqGac7U4DyXsZbJSj9luICTZyC1AqrJpT%2F0f6YtHbnnYUcnA3LCmFhHHQJreDqJdjXJ%2FOBmJlqvEinfpocXwA1NCrakLLUphCCuKnCJGTAu3RkinH%2BJT92ty10Ms619PQyosCih%2Byvkkksuou5ck36aXVif8kTl%2BCaZga7EdfmoVWmYWV76gLQff3k7DOLPcUU7nxkdFnsmPWAyDSDso0XThAWYxF%2BB9N5gO7kAJkcQHoISrvPT1iSgICThbiLv98KJC1diHBRx4bJ0FaJh%2BM8Y7bPNe6yHdVFdxHraAzV1SQ2TTTV%2BiiqcVRxoihM98dRNYUaOQtpP1elBZNVKyPppq2QOQEn60aY6el8ClnGl9Z71jDkWPaDmnxKo%2FwJIM5%2FMSRPeetiXgqvrTO4zY24Pfa1Kg31Iih1i0pWTKV0FVW%2FHGCo%2BQZvUxmb%2Bx7n7TWRrCmML70aoJVQhZI2BlG56g%2FIcHk8C2aZCx5Xp9W3jujcznga7V6S125xr8qiE85bs8tX4uh9lR52Z38Oeyxw0andDzjaVpSBJshH1yX5pPxMGZrDgmyBsyd8Oz%2F92OaGgvIw%2FaX2vAY6pgGcYLnnKQqSbECvJHOiqcMKRKiFOvtlTk8wYPAFg7QG0Bl9VMSf%2F5Te0dFF%2FTXFRhX3o61U7BG17lMYlePmYP9Dxa4SkQVUrSqkijtnOdvcN73F5Z7FUWxWNCKV8ZKy1Hq%2F8GtiigefDTMpslbGD%2FEEbu88XPdkMoThXVxqWHET0U9bitKil5jxI9K72dMOJl%2BYl3ITMA3lp6qgmeFd4nJyW74Lju50&X-Amz-Signature=34ff7cdfc02c73ffb144165e483dfc128d9fdf2bfcddf7527295b7d1303f8f11&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPZPNOGC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZ8jKqpyn2bTepTpnGua%2BJrGHPwq6y37CRv7RlgNlwJAiAafOiyADr5UBXDkqNg5eJAo1RIVyNWpm4DcPzAZrjlcyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHY22qerRFfWP0H0KtwDNnWq5F7TfSAHdNiXScPB%2BYGsYzl8NcrM34um%2FHdo6gpa5kLTtlfFFymqGac7U4DyXsZbJSj9luICTZyC1AqrJpT%2F0f6YtHbnnYUcnA3LCmFhHHQJreDqJdjXJ%2FOBmJlqvEinfpocXwA1NCrakLLUphCCuKnCJGTAu3RkinH%2BJT92ty10Ms619PQyosCih%2Byvkkksuou5ck36aXVif8kTl%2BCaZga7EdfmoVWmYWV76gLQff3k7DOLPcUU7nxkdFnsmPWAyDSDso0XThAWYxF%2BB9N5gO7kAJkcQHoISrvPT1iSgICThbiLv98KJC1diHBRx4bJ0FaJh%2BM8Y7bPNe6yHdVFdxHraAzV1SQ2TTTV%2BiiqcVRxoihM98dRNYUaOQtpP1elBZNVKyPppq2QOQEn60aY6el8ClnGl9Z71jDkWPaDmnxKo%2FwJIM5%2FMSRPeetiXgqvrTO4zY24Pfa1Kg31Iih1i0pWTKV0FVW%2FHGCo%2BQZvUxmb%2Bx7n7TWRrCmML70aoJVQhZI2BlG56g%2FIcHk8C2aZCx5Xp9W3jujcznga7V6S125xr8qiE85bs8tX4uh9lR52Z38Oeyxw0andDzjaVpSBJshH1yX5pPxMGZrDgmyBsyd8Oz%2F92OaGgvIw%2FaX2vAY6pgGcYLnnKQqSbECvJHOiqcMKRKiFOvtlTk8wYPAFg7QG0Bl9VMSf%2F5Te0dFF%2FTXFRhX3o61U7BG17lMYlePmYP9Dxa4SkQVUrSqkijtnOdvcN73F5Z7FUWxWNCKV8ZKy1Hq%2F8GtiigefDTMpslbGD%2FEEbu88XPdkMoThXVxqWHET0U9bitKil5jxI9K72dMOJl%2BYl3ITMA3lp6qgmeFd4nJyW74Lju50&X-Amz-Signature=4f9eba5a2dcb6b9a878506d2f1c20c39bed7d479cf931b9a5cd2c59d9788064c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPZPNOGC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZ8jKqpyn2bTepTpnGua%2BJrGHPwq6y37CRv7RlgNlwJAiAafOiyADr5UBXDkqNg5eJAo1RIVyNWpm4DcPzAZrjlcyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHY22qerRFfWP0H0KtwDNnWq5F7TfSAHdNiXScPB%2BYGsYzl8NcrM34um%2FHdo6gpa5kLTtlfFFymqGac7U4DyXsZbJSj9luICTZyC1AqrJpT%2F0f6YtHbnnYUcnA3LCmFhHHQJreDqJdjXJ%2FOBmJlqvEinfpocXwA1NCrakLLUphCCuKnCJGTAu3RkinH%2BJT92ty10Ms619PQyosCih%2Byvkkksuou5ck36aXVif8kTl%2BCaZga7EdfmoVWmYWV76gLQff3k7DOLPcUU7nxkdFnsmPWAyDSDso0XThAWYxF%2BB9N5gO7kAJkcQHoISrvPT1iSgICThbiLv98KJC1diHBRx4bJ0FaJh%2BM8Y7bPNe6yHdVFdxHraAzV1SQ2TTTV%2BiiqcVRxoihM98dRNYUaOQtpP1elBZNVKyPppq2QOQEn60aY6el8ClnGl9Z71jDkWPaDmnxKo%2FwJIM5%2FMSRPeetiXgqvrTO4zY24Pfa1Kg31Iih1i0pWTKV0FVW%2FHGCo%2BQZvUxmb%2Bx7n7TWRrCmML70aoJVQhZI2BlG56g%2FIcHk8C2aZCx5Xp9W3jujcznga7V6S125xr8qiE85bs8tX4uh9lR52Z38Oeyxw0andDzjaVpSBJshH1yX5pPxMGZrDgmyBsyd8Oz%2F92OaGgvIw%2FaX2vAY6pgGcYLnnKQqSbECvJHOiqcMKRKiFOvtlTk8wYPAFg7QG0Bl9VMSf%2F5Te0dFF%2FTXFRhX3o61U7BG17lMYlePmYP9Dxa4SkQVUrSqkijtnOdvcN73F5Z7FUWxWNCKV8ZKy1Hq%2F8GtiigefDTMpslbGD%2FEEbu88XPdkMoThXVxqWHET0U9bitKil5jxI9K72dMOJl%2BYl3ITMA3lp6qgmeFd4nJyW74Lju50&X-Amz-Signature=18edeb6d72d185248c1278205dea35ec69ef8e695da6be8b368098f53947cbff&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPZPNOGC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZ8jKqpyn2bTepTpnGua%2BJrGHPwq6y37CRv7RlgNlwJAiAafOiyADr5UBXDkqNg5eJAo1RIVyNWpm4DcPzAZrjlcyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHY22qerRFfWP0H0KtwDNnWq5F7TfSAHdNiXScPB%2BYGsYzl8NcrM34um%2FHdo6gpa5kLTtlfFFymqGac7U4DyXsZbJSj9luICTZyC1AqrJpT%2F0f6YtHbnnYUcnA3LCmFhHHQJreDqJdjXJ%2FOBmJlqvEinfpocXwA1NCrakLLUphCCuKnCJGTAu3RkinH%2BJT92ty10Ms619PQyosCih%2Byvkkksuou5ck36aXVif8kTl%2BCaZga7EdfmoVWmYWV76gLQff3k7DOLPcUU7nxkdFnsmPWAyDSDso0XThAWYxF%2BB9N5gO7kAJkcQHoISrvPT1iSgICThbiLv98KJC1diHBRx4bJ0FaJh%2BM8Y7bPNe6yHdVFdxHraAzV1SQ2TTTV%2BiiqcVRxoihM98dRNYUaOQtpP1elBZNVKyPppq2QOQEn60aY6el8ClnGl9Z71jDkWPaDmnxKo%2FwJIM5%2FMSRPeetiXgqvrTO4zY24Pfa1Kg31Iih1i0pWTKV0FVW%2FHGCo%2BQZvUxmb%2Bx7n7TWRrCmML70aoJVQhZI2BlG56g%2FIcHk8C2aZCx5Xp9W3jujcznga7V6S125xr8qiE85bs8tX4uh9lR52Z38Oeyxw0andDzjaVpSBJshH1yX5pPxMGZrDgmyBsyd8Oz%2F92OaGgvIw%2FaX2vAY6pgGcYLnnKQqSbECvJHOiqcMKRKiFOvtlTk8wYPAFg7QG0Bl9VMSf%2F5Te0dFF%2FTXFRhX3o61U7BG17lMYlePmYP9Dxa4SkQVUrSqkijtnOdvcN73F5Z7FUWxWNCKV8ZKy1Hq%2F8GtiigefDTMpslbGD%2FEEbu88XPdkMoThXVxqWHET0U9bitKil5jxI9K72dMOJl%2BYl3ITMA3lp6qgmeFd4nJyW74Lju50&X-Amz-Signature=2d52397dc87633bfd31eed86b0010c84c3e3c267d90770bd6485541b935affc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPZPNOGC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZ8jKqpyn2bTepTpnGua%2BJrGHPwq6y37CRv7RlgNlwJAiAafOiyADr5UBXDkqNg5eJAo1RIVyNWpm4DcPzAZrjlcyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHY22qerRFfWP0H0KtwDNnWq5F7TfSAHdNiXScPB%2BYGsYzl8NcrM34um%2FHdo6gpa5kLTtlfFFymqGac7U4DyXsZbJSj9luICTZyC1AqrJpT%2F0f6YtHbnnYUcnA3LCmFhHHQJreDqJdjXJ%2FOBmJlqvEinfpocXwA1NCrakLLUphCCuKnCJGTAu3RkinH%2BJT92ty10Ms619PQyosCih%2Byvkkksuou5ck36aXVif8kTl%2BCaZga7EdfmoVWmYWV76gLQff3k7DOLPcUU7nxkdFnsmPWAyDSDso0XThAWYxF%2BB9N5gO7kAJkcQHoISrvPT1iSgICThbiLv98KJC1diHBRx4bJ0FaJh%2BM8Y7bPNe6yHdVFdxHraAzV1SQ2TTTV%2BiiqcVRxoihM98dRNYUaOQtpP1elBZNVKyPppq2QOQEn60aY6el8ClnGl9Z71jDkWPaDmnxKo%2FwJIM5%2FMSRPeetiXgqvrTO4zY24Pfa1Kg31Iih1i0pWTKV0FVW%2FHGCo%2BQZvUxmb%2Bx7n7TWRrCmML70aoJVQhZI2BlG56g%2FIcHk8C2aZCx5Xp9W3jujcznga7V6S125xr8qiE85bs8tX4uh9lR52Z38Oeyxw0andDzjaVpSBJshH1yX5pPxMGZrDgmyBsyd8Oz%2F92OaGgvIw%2FaX2vAY6pgGcYLnnKQqSbECvJHOiqcMKRKiFOvtlTk8wYPAFg7QG0Bl9VMSf%2F5Te0dFF%2FTXFRhX3o61U7BG17lMYlePmYP9Dxa4SkQVUrSqkijtnOdvcN73F5Z7FUWxWNCKV8ZKy1Hq%2F8GtiigefDTMpslbGD%2FEEbu88XPdkMoThXVxqWHET0U9bitKil5jxI9K72dMOJl%2BYl3ITMA3lp6qgmeFd4nJyW74Lju50&X-Amz-Signature=26b3c7f05d6c311288315bd2e88fa1d1419db5ba32d8f7926b2ae99c8b38cefc&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPZPNOGC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZ8jKqpyn2bTepTpnGua%2BJrGHPwq6y37CRv7RlgNlwJAiAafOiyADr5UBXDkqNg5eJAo1RIVyNWpm4DcPzAZrjlcyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHY22qerRFfWP0H0KtwDNnWq5F7TfSAHdNiXScPB%2BYGsYzl8NcrM34um%2FHdo6gpa5kLTtlfFFymqGac7U4DyXsZbJSj9luICTZyC1AqrJpT%2F0f6YtHbnnYUcnA3LCmFhHHQJreDqJdjXJ%2FOBmJlqvEinfpocXwA1NCrakLLUphCCuKnCJGTAu3RkinH%2BJT92ty10Ms619PQyosCih%2Byvkkksuou5ck36aXVif8kTl%2BCaZga7EdfmoVWmYWV76gLQff3k7DOLPcUU7nxkdFnsmPWAyDSDso0XThAWYxF%2BB9N5gO7kAJkcQHoISrvPT1iSgICThbiLv98KJC1diHBRx4bJ0FaJh%2BM8Y7bPNe6yHdVFdxHraAzV1SQ2TTTV%2BiiqcVRxoihM98dRNYUaOQtpP1elBZNVKyPppq2QOQEn60aY6el8ClnGl9Z71jDkWPaDmnxKo%2FwJIM5%2FMSRPeetiXgqvrTO4zY24Pfa1Kg31Iih1i0pWTKV0FVW%2FHGCo%2BQZvUxmb%2Bx7n7TWRrCmML70aoJVQhZI2BlG56g%2FIcHk8C2aZCx5Xp9W3jujcznga7V6S125xr8qiE85bs8tX4uh9lR52Z38Oeyxw0andDzjaVpSBJshH1yX5pPxMGZrDgmyBsyd8Oz%2F92OaGgvIw%2FaX2vAY6pgGcYLnnKQqSbECvJHOiqcMKRKiFOvtlTk8wYPAFg7QG0Bl9VMSf%2F5Te0dFF%2FTXFRhX3o61U7BG17lMYlePmYP9Dxa4SkQVUrSqkijtnOdvcN73F5Z7FUWxWNCKV8ZKy1Hq%2F8GtiigefDTMpslbGD%2FEEbu88XPdkMoThXVxqWHET0U9bitKil5jxI9K72dMOJl%2BYl3ITMA3lp6qgmeFd4nJyW74Lju50&X-Amz-Signature=ae4b6fce14d56da76eda34769f5aeda6c2888521f2009cbedb9187609ce1789d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OEMWSIC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7S0%2FPQ5govYYJ3dbde4t0Xz%2FVvH%2BZ6yEMmDFFJmNnyQIgQk%2Fit03Sar1fYXNBx6j2fcmOphp7zjvLF%2BY3Wy5x580qiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5RceCaofe4AF1ZeCrcA7ei7gGLhKS5HnZQwrbPpPkVk9pg3BVhJjFX5RUlYV9%2BdhMFTSvs2wfjl8CYdAmYI8hrp%2FiP6mw5ZMaq13d9WN%2B4j0SiIBXfCQ157OpIkx5f%2FOT116NlJ4wDZSULJssrT6rKMyJP1H%2BpgnC312xYkTELsOOXgcaa58usrjVRhPsy1FK5yashujbDJZ131Ug9gvsVobBtK807rkz8ie0PWhsFRKh64T1k9BQ3VfE3QkC5xQ5jrjqRwJnC09utuBlg83b2TTjKz4oTIyG0HUOAkOYU3ktmqdYqMorbICwSCav5zdM%2FVopQBvIzXoi00AyT4xnwHqjykGSMkgLfFTUwh%2FnT%2FHivC%2FiVXlBzRjAMTvDRlzO8fSI%2BCZ0k1LTAaG8Dc%2FEZ8Tta%2Bfomef%2BWHZLxB68RfM3uEnDMw32R5Gyg%2BrVobsau2X7Vg0dWGZRkVYQKuHwB%2B1Emj5TkrOITSlKZMWna58OvqKlmogXoQb%2BAJJa%2B5pRv8pasamYM4eZx9uKpmRPN4Y6eipGT2%2FakvKIpBx%2Be5xQ4mNyTZQwwXetlIgNMv4gIbYi8OHsN94MYOcRtd3emq8FnKXpOSkEnbwC6vab9kQDma9ZIferU8pZTYTKPiNZSFJdNsBiRfoNlMIam9rwGOqUB640KVWVlkERTCkxfX5DfRbm1o%2BcfMo2mCvOxq9ZwIHgDMb16MabTm7DUhtMpyk4vnCJQaCYR9mNZFhqIQ3RhSyafYpmoO5POIXJebt7kJiMaZX%2F7wLBrxBbsSARnup%2Bh%2FkkIeK9xDwsYD4hw%2BOF3VqvQtRUEEoXILu1RywJyEcE98ot7mvaLg34PDcoYfd415bUppoO5R1vSGwG9BG345lcvcfvc&X-Amz-Signature=7cd43f7fc18efd84b2670029587310575d0c76b6f8efe519bff88b4a52f8955f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YP3D7AKJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDa1yreZ4aFY7PJjJfKq3%2FEBbByORmox%2BVp7hlNtMyCzgIgG6%2F4JGiTObgZXeo7VFnY94ouk8lxXAZFGXedVQzVhcIqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP3G6CPEsUwIpzSXPircA180mDN27k8kA%2Ff2mQcPdon8ILPxksSMtMwbupXxcr5r6aDCl61OtOQZgKtphLu%2FS2tPDw%2BMfhcOBCNgGY4tQWBq%2FF1dQ1MdUZlYN2wP4wOHbXEGI1k9pmvN57vqgeni9%2FjRrQJ00sByyNSGwxSr7XJsE9g3EVe5xUwFo5RqSzh0WXuUgRgi0u23zmSoaRdiwR8okGcaGjrMX%2BzJfdJxmk6Z%2F%2BxuJS2BTxUXUm7SVngSjNSkQN9mFH6wNDjduSv7zIFRXTEvxiYsehssgkvfsgw9Kf8beI4I92zOo1uK0jPmBB0aYJcqah7JeIsVK9UHivKcnaGSdeJ4KgOYQibxKz0Jw6BG%2Bp3Em1KJeBRIjKJRMiKAxAxFQfSKjxYmvik%2BHp4S0%2FnRJR68HZZSrFEI%2FZDHugdtkK%2F%2FMe7vJO80IcW2WpjdKXbJCtNvjcvbziFO2sFN9BbI4GyHnJYC9QOSiwk%2F7zKXtQToE1JCkY3WDGOfaGtOgxqyKp2P0Qb%2BVbtgpxxwUJQ%2BeNdtxcgQUwdcMs67yC7hglgDjhXPAIiYpLtihwYSF5%2BGrPv4Z%2BcV%2BJWtq0o%2BU3myj8vsqdJ1G8r95DyGp7Ej0NJhk%2Fs1WPnq4Z22LNm3wrTisAZHDhnMMMml9rwGOqUBJCsvtFgWb8tc5EJ7qMJXDWDMFUB73naigH%2BqziTAqUr%2BjHJnhNR0I55GmjvN5duHpgngndL008kbTE46qJ4V5cy1GJjoFcKIAxrryRfnieFM%2B8jNCyuMVa9hvYcyeImu%2FN4FzWrNwl8vmi91lbV0Aj26cunwcUgClmnW0rOeu6uRikkGtY6SPXvOjVEQQ9s7cOe9aeVGqvWpqMifmc9Ubr9BOa1I&X-Amz-Signature=7e4093773bdf01af791f1841709be5c3d950109ae2dd679a379c564e6bc0e523&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6VYCKWS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYmVp2ruG%2Fnv0ecRpnvcG8bRzlwBSaDgVrGOKM36terQIgezr%2FoEqinwWAR3j3UH35XynIrUtDVxaCFrdbyEMD%2BNEqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAbOpzcOHvZ2F5i4uSrcA%2BJNO%2FFLgIKCwbIUZheDrrLn9kKYCT1afu6b6lznRUpXOTPiQQwUL0En%2BRDkOUpr9Cavvct3sjnDI4K31%2FraxaKfeGkvRA2kNg2EuXjvH0ccT%2FnrshXcTr%2F%2FaNzPhECISsO6Sx0O57hC%2FBiwNMpTx3l8p9TUxnzE17pnsnXIurogwybvNoAVB4Cz6SuOfGocu0l5NMBal4lp%2FSh6ZgiavGwAXqglBmuIeLdgPAIEK2gndrDxvFzqnIesWUO7M6VaLHSXsoWJlCL%2FxRMeLE3gOjLqE9ZJFBTrAMdnTMYCHgzoLCnbCbsf6%2Fxd3jZSd7yYDGEUqYJ5klb4j4Xv6GPgLkTlENFqUhzg2vByGjRtBgLloYNOJb1OwZf10UsgeyCU%2BILCUPvNbAfGD%2FQzHvnVtNKwK5SKmed8IUCsSjR8%2BA6Tw9ailXYkHC0Uc4YjqrvroqoYmqoJgVeuVa%2F4oCo6cepAJIuHg5tAMZBFkAyi9kK9kHNIrfI43VTHLVTBvJxKwYRTNGeM1CGoVrneSrJIM02IP8u6saxETRN%2BUirOl6yboScj%2Fes3QNOx9k8H1uOHm8byjj4Jt%2Bvmp9G5jeNnqHk%2B2CLaog5XQYJQiJMyrKizkv3YSgGTBIYmKu3kMJSm9rwGOqUB37Y8%2B3IriJAzusPK7UsY7IGNVLnKJe%2Briw3tARYv%2BCH0h8lE7u2FjRJsI7BlNxuL5lI0WMbIHfKXEcdV91zp%2FRkWktqSZBxDueFzbkhvJYJsV%2BuOyjPzWk5oplmTj6I3OpE4XqFiWyCUsJvkscdoBtLLCe7iifMo8MkG30FhSntOGQatFiuFZEZ%2BfQ52Nt81N8i62FnK2jGp0AtgrZfa7PbPXiow&X-Amz-Signature=3467eb2d7dc38cbb8ee53506dce4dc498f2829e388d8a9277264dd98741c1fde&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6VYCKWS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041715Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYmVp2ruG%2Fnv0ecRpnvcG8bRzlwBSaDgVrGOKM36terQIgezr%2FoEqinwWAR3j3UH35XynIrUtDVxaCFrdbyEMD%2BNEqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAbOpzcOHvZ2F5i4uSrcA%2BJNO%2FFLgIKCwbIUZheDrrLn9kKYCT1afu6b6lznRUpXOTPiQQwUL0En%2BRDkOUpr9Cavvct3sjnDI4K31%2FraxaKfeGkvRA2kNg2EuXjvH0ccT%2FnrshXcTr%2F%2FaNzPhECISsO6Sx0O57hC%2FBiwNMpTx3l8p9TUxnzE17pnsnXIurogwybvNoAVB4Cz6SuOfGocu0l5NMBal4lp%2FSh6ZgiavGwAXqglBmuIeLdgPAIEK2gndrDxvFzqnIesWUO7M6VaLHSXsoWJlCL%2FxRMeLE3gOjLqE9ZJFBTrAMdnTMYCHgzoLCnbCbsf6%2Fxd3jZSd7yYDGEUqYJ5klb4j4Xv6GPgLkTlENFqUhzg2vByGjRtBgLloYNOJb1OwZf10UsgeyCU%2BILCUPvNbAfGD%2FQzHvnVtNKwK5SKmed8IUCsSjR8%2BA6Tw9ailXYkHC0Uc4YjqrvroqoYmqoJgVeuVa%2F4oCo6cepAJIuHg5tAMZBFkAyi9kK9kHNIrfI43VTHLVTBvJxKwYRTNGeM1CGoVrneSrJIM02IP8u6saxETRN%2BUirOl6yboScj%2Fes3QNOx9k8H1uOHm8byjj4Jt%2Bvmp9G5jeNnqHk%2B2CLaog5XQYJQiJMyrKizkv3YSgGTBIYmKu3kMJSm9rwGOqUB37Y8%2B3IriJAzusPK7UsY7IGNVLnKJe%2Briw3tARYv%2BCH0h8lE7u2FjRJsI7BlNxuL5lI0WMbIHfKXEcdV91zp%2FRkWktqSZBxDueFzbkhvJYJsV%2BuOyjPzWk5oplmTj6I3OpE4XqFiWyCUsJvkscdoBtLLCe7iifMo8MkG30FhSntOGQatFiuFZEZ%2BfQ52Nt81N8i62FnK2jGp0AtgrZfa7PbPXiow&X-Amz-Signature=91ecd7685ad5a3ce7a869afd2dbc173921632162b1e50c7ebf2cd0426011ff4d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
