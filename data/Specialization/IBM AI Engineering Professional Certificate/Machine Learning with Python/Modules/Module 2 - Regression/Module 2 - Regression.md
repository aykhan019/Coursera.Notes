

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLIULPTW%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDcfJZLdgaeIESEXU3Y9L2ApecXPAdj0opgxGGS9CVcgAIgFJ5hfPXnijuSuiLy1uVXCK%2ByDyRxSscYaEDmi0kAOYkq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDNtirL4iGfeZqlE7AircA4eW8nJF2RFjz7FTe82412%2BIhP1uyMb7Vm%2BNwgRAIzN2zApSSB%2Fcg9veUBrhOcGpuMMrj2RuW%2BR3kpohxMYW9zgx2WwWP2I0eeWpir%2B4WxcWv%2B%2BdWTCenxD4pyoIDUX9teEiRgEqwampCv9rVuUq23qxfyNwU2zlBJ%2F0vUWDIhAiiUUc16AFUMgNBccumLNtRKphAQz3c5CBb5WNwmG7%2BGisHl711vd4T%2Bgm9vfVEOnoU41O61TFrJF7SrMnXUqwcjXIIIT37w9hNiznZHu4g0wVrxHLv9rV2s2lKyIvqlRdElfB1DaRkta%2FOJWyQrBVUluBIHij%2F2HMQj711Qqo50Obp6NoOw8x6uollLTTh1rebg6UuLRiCPUC6N8Iy6VdsS2GXGkw%2BshIIddAAsFJxOYy7AcJkWHkCViDj0yksHytuRyJgWvkLwdiSB%2Fig6zeWIHq3tt1nKnKnFRJQRKsGS%2FCInHSm7eJxc3rZcex1SaxtVKcrZHUM0z1MGbLMJ37z094PtksywKWiin7w7qZUq8dtg6CNvwzY6M1VEuquykUwJ7uwyWZR%2Bti%2FOln0ZfmeJ2xjVK0VbjNjl75LkZgg0DS1pTmC6HoBQ%2BcqNn2TPXKCmmAcjEZmX%2BS2XIVML%2BU5bwGOqUBP8zyRgKODes2fH8SR8VnBGJ2Tml3BxPhST89j%2FbsVQX5m4qlP7VUOhJNRgX2BaJUuVjEhylTtL0tC1yLjn2U%2Fs52hwkfTPFoyVJtoQBcEyHGf3OwqPXteqpl6WSZbmuA8Injrhr52xKoG2G8Yy2Py3PrgGn2QlWZ7x0uq7k%2BS4uzkjS6QRq1oOKF4pdjd1xWA%2Foh%2BtCAgQr713w5CVjSeiLTJ1%2F6&X-Amz-Signature=5c231ea61a02543645bcf45ca76a33286274547b2729d6f258e0d83721a4c895&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLIULPTW%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDcfJZLdgaeIESEXU3Y9L2ApecXPAdj0opgxGGS9CVcgAIgFJ5hfPXnijuSuiLy1uVXCK%2ByDyRxSscYaEDmi0kAOYkq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDNtirL4iGfeZqlE7AircA4eW8nJF2RFjz7FTe82412%2BIhP1uyMb7Vm%2BNwgRAIzN2zApSSB%2Fcg9veUBrhOcGpuMMrj2RuW%2BR3kpohxMYW9zgx2WwWP2I0eeWpir%2B4WxcWv%2B%2BdWTCenxD4pyoIDUX9teEiRgEqwampCv9rVuUq23qxfyNwU2zlBJ%2F0vUWDIhAiiUUc16AFUMgNBccumLNtRKphAQz3c5CBb5WNwmG7%2BGisHl711vd4T%2Bgm9vfVEOnoU41O61TFrJF7SrMnXUqwcjXIIIT37w9hNiznZHu4g0wVrxHLv9rV2s2lKyIvqlRdElfB1DaRkta%2FOJWyQrBVUluBIHij%2F2HMQj711Qqo50Obp6NoOw8x6uollLTTh1rebg6UuLRiCPUC6N8Iy6VdsS2GXGkw%2BshIIddAAsFJxOYy7AcJkWHkCViDj0yksHytuRyJgWvkLwdiSB%2Fig6zeWIHq3tt1nKnKnFRJQRKsGS%2FCInHSm7eJxc3rZcex1SaxtVKcrZHUM0z1MGbLMJ37z094PtksywKWiin7w7qZUq8dtg6CNvwzY6M1VEuquykUwJ7uwyWZR%2Bti%2FOln0ZfmeJ2xjVK0VbjNjl75LkZgg0DS1pTmC6HoBQ%2BcqNn2TPXKCmmAcjEZmX%2BS2XIVML%2BU5bwGOqUBP8zyRgKODes2fH8SR8VnBGJ2Tml3BxPhST89j%2FbsVQX5m4qlP7VUOhJNRgX2BaJUuVjEhylTtL0tC1yLjn2U%2Fs52hwkfTPFoyVJtoQBcEyHGf3OwqPXteqpl6WSZbmuA8Injrhr52xKoG2G8Yy2Py3PrgGn2QlWZ7x0uq7k%2BS4uzkjS6QRq1oOKF4pdjd1xWA%2Foh%2BtCAgQr713w5CVjSeiLTJ1%2F6&X-Amz-Signature=61928d9c751e92ac6bb7eb1ef854e93072fa20b4e2f4e0dd98a20f47a76b6831&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLIULPTW%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDcfJZLdgaeIESEXU3Y9L2ApecXPAdj0opgxGGS9CVcgAIgFJ5hfPXnijuSuiLy1uVXCK%2ByDyRxSscYaEDmi0kAOYkq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDNtirL4iGfeZqlE7AircA4eW8nJF2RFjz7FTe82412%2BIhP1uyMb7Vm%2BNwgRAIzN2zApSSB%2Fcg9veUBrhOcGpuMMrj2RuW%2BR3kpohxMYW9zgx2WwWP2I0eeWpir%2B4WxcWv%2B%2BdWTCenxD4pyoIDUX9teEiRgEqwampCv9rVuUq23qxfyNwU2zlBJ%2F0vUWDIhAiiUUc16AFUMgNBccumLNtRKphAQz3c5CBb5WNwmG7%2BGisHl711vd4T%2Bgm9vfVEOnoU41O61TFrJF7SrMnXUqwcjXIIIT37w9hNiznZHu4g0wVrxHLv9rV2s2lKyIvqlRdElfB1DaRkta%2FOJWyQrBVUluBIHij%2F2HMQj711Qqo50Obp6NoOw8x6uollLTTh1rebg6UuLRiCPUC6N8Iy6VdsS2GXGkw%2BshIIddAAsFJxOYy7AcJkWHkCViDj0yksHytuRyJgWvkLwdiSB%2Fig6zeWIHq3tt1nKnKnFRJQRKsGS%2FCInHSm7eJxc3rZcex1SaxtVKcrZHUM0z1MGbLMJ37z094PtksywKWiin7w7qZUq8dtg6CNvwzY6M1VEuquykUwJ7uwyWZR%2Bti%2FOln0ZfmeJ2xjVK0VbjNjl75LkZgg0DS1pTmC6HoBQ%2BcqNn2TPXKCmmAcjEZmX%2BS2XIVML%2BU5bwGOqUBP8zyRgKODes2fH8SR8VnBGJ2Tml3BxPhST89j%2FbsVQX5m4qlP7VUOhJNRgX2BaJUuVjEhylTtL0tC1yLjn2U%2Fs52hwkfTPFoyVJtoQBcEyHGf3OwqPXteqpl6WSZbmuA8Injrhr52xKoG2G8Yy2Py3PrgGn2QlWZ7x0uq7k%2BS4uzkjS6QRq1oOKF4pdjd1xWA%2Foh%2BtCAgQr713w5CVjSeiLTJ1%2F6&X-Amz-Signature=54c6944adac1ddc9b6c1b32ac6f0e3ff2a6132631483fec8a4428dc9d5745a01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLIULPTW%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDcfJZLdgaeIESEXU3Y9L2ApecXPAdj0opgxGGS9CVcgAIgFJ5hfPXnijuSuiLy1uVXCK%2ByDyRxSscYaEDmi0kAOYkq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDNtirL4iGfeZqlE7AircA4eW8nJF2RFjz7FTe82412%2BIhP1uyMb7Vm%2BNwgRAIzN2zApSSB%2Fcg9veUBrhOcGpuMMrj2RuW%2BR3kpohxMYW9zgx2WwWP2I0eeWpir%2B4WxcWv%2B%2BdWTCenxD4pyoIDUX9teEiRgEqwampCv9rVuUq23qxfyNwU2zlBJ%2F0vUWDIhAiiUUc16AFUMgNBccumLNtRKphAQz3c5CBb5WNwmG7%2BGisHl711vd4T%2Bgm9vfVEOnoU41O61TFrJF7SrMnXUqwcjXIIIT37w9hNiznZHu4g0wVrxHLv9rV2s2lKyIvqlRdElfB1DaRkta%2FOJWyQrBVUluBIHij%2F2HMQj711Qqo50Obp6NoOw8x6uollLTTh1rebg6UuLRiCPUC6N8Iy6VdsS2GXGkw%2BshIIddAAsFJxOYy7AcJkWHkCViDj0yksHytuRyJgWvkLwdiSB%2Fig6zeWIHq3tt1nKnKnFRJQRKsGS%2FCInHSm7eJxc3rZcex1SaxtVKcrZHUM0z1MGbLMJ37z094PtksywKWiin7w7qZUq8dtg6CNvwzY6M1VEuquykUwJ7uwyWZR%2Bti%2FOln0ZfmeJ2xjVK0VbjNjl75LkZgg0DS1pTmC6HoBQ%2BcqNn2TPXKCmmAcjEZmX%2BS2XIVML%2BU5bwGOqUBP8zyRgKODes2fH8SR8VnBGJ2Tml3BxPhST89j%2FbsVQX5m4qlP7VUOhJNRgX2BaJUuVjEhylTtL0tC1yLjn2U%2Fs52hwkfTPFoyVJtoQBcEyHGf3OwqPXteqpl6WSZbmuA8Injrhr52xKoG2G8Yy2Py3PrgGn2QlWZ7x0uq7k%2BS4uzkjS6QRq1oOKF4pdjd1xWA%2Foh%2BtCAgQr713w5CVjSeiLTJ1%2F6&X-Amz-Signature=d32a9baf4dd3354c985b0fdccddd68746ea58bb5afc98cbd097fc9cc28d32bc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLIULPTW%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDcfJZLdgaeIESEXU3Y9L2ApecXPAdj0opgxGGS9CVcgAIgFJ5hfPXnijuSuiLy1uVXCK%2ByDyRxSscYaEDmi0kAOYkq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDNtirL4iGfeZqlE7AircA4eW8nJF2RFjz7FTe82412%2BIhP1uyMb7Vm%2BNwgRAIzN2zApSSB%2Fcg9veUBrhOcGpuMMrj2RuW%2BR3kpohxMYW9zgx2WwWP2I0eeWpir%2B4WxcWv%2B%2BdWTCenxD4pyoIDUX9teEiRgEqwampCv9rVuUq23qxfyNwU2zlBJ%2F0vUWDIhAiiUUc16AFUMgNBccumLNtRKphAQz3c5CBb5WNwmG7%2BGisHl711vd4T%2Bgm9vfVEOnoU41O61TFrJF7SrMnXUqwcjXIIIT37w9hNiznZHu4g0wVrxHLv9rV2s2lKyIvqlRdElfB1DaRkta%2FOJWyQrBVUluBIHij%2F2HMQj711Qqo50Obp6NoOw8x6uollLTTh1rebg6UuLRiCPUC6N8Iy6VdsS2GXGkw%2BshIIddAAsFJxOYy7AcJkWHkCViDj0yksHytuRyJgWvkLwdiSB%2Fig6zeWIHq3tt1nKnKnFRJQRKsGS%2FCInHSm7eJxc3rZcex1SaxtVKcrZHUM0z1MGbLMJ37z094PtksywKWiin7w7qZUq8dtg6CNvwzY6M1VEuquykUwJ7uwyWZR%2Bti%2FOln0ZfmeJ2xjVK0VbjNjl75LkZgg0DS1pTmC6HoBQ%2BcqNn2TPXKCmmAcjEZmX%2BS2XIVML%2BU5bwGOqUBP8zyRgKODes2fH8SR8VnBGJ2Tml3BxPhST89j%2FbsVQX5m4qlP7VUOhJNRgX2BaJUuVjEhylTtL0tC1yLjn2U%2Fs52hwkfTPFoyVJtoQBcEyHGf3OwqPXteqpl6WSZbmuA8Injrhr52xKoG2G8Yy2Py3PrgGn2QlWZ7x0uq7k%2BS4uzkjS6QRq1oOKF4pdjd1xWA%2Foh%2BtCAgQr713w5CVjSeiLTJ1%2F6&X-Amz-Signature=8a64356ad978c1769b56184a45a87c885f21b82ada465c350920d622738d06d2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLIULPTW%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDcfJZLdgaeIESEXU3Y9L2ApecXPAdj0opgxGGS9CVcgAIgFJ5hfPXnijuSuiLy1uVXCK%2ByDyRxSscYaEDmi0kAOYkq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDNtirL4iGfeZqlE7AircA4eW8nJF2RFjz7FTe82412%2BIhP1uyMb7Vm%2BNwgRAIzN2zApSSB%2Fcg9veUBrhOcGpuMMrj2RuW%2BR3kpohxMYW9zgx2WwWP2I0eeWpir%2B4WxcWv%2B%2BdWTCenxD4pyoIDUX9teEiRgEqwampCv9rVuUq23qxfyNwU2zlBJ%2F0vUWDIhAiiUUc16AFUMgNBccumLNtRKphAQz3c5CBb5WNwmG7%2BGisHl711vd4T%2Bgm9vfVEOnoU41O61TFrJF7SrMnXUqwcjXIIIT37w9hNiznZHu4g0wVrxHLv9rV2s2lKyIvqlRdElfB1DaRkta%2FOJWyQrBVUluBIHij%2F2HMQj711Qqo50Obp6NoOw8x6uollLTTh1rebg6UuLRiCPUC6N8Iy6VdsS2GXGkw%2BshIIddAAsFJxOYy7AcJkWHkCViDj0yksHytuRyJgWvkLwdiSB%2Fig6zeWIHq3tt1nKnKnFRJQRKsGS%2FCInHSm7eJxc3rZcex1SaxtVKcrZHUM0z1MGbLMJ37z094PtksywKWiin7w7qZUq8dtg6CNvwzY6M1VEuquykUwJ7uwyWZR%2Bti%2FOln0ZfmeJ2xjVK0VbjNjl75LkZgg0DS1pTmC6HoBQ%2BcqNn2TPXKCmmAcjEZmX%2BS2XIVML%2BU5bwGOqUBP8zyRgKODes2fH8SR8VnBGJ2Tml3BxPhST89j%2FbsVQX5m4qlP7VUOhJNRgX2BaJUuVjEhylTtL0tC1yLjn2U%2Fs52hwkfTPFoyVJtoQBcEyHGf3OwqPXteqpl6WSZbmuA8Injrhr52xKoG2G8Yy2Py3PrgGn2QlWZ7x0uq7k%2BS4uzkjS6QRq1oOKF4pdjd1xWA%2Foh%2BtCAgQr713w5CVjSeiLTJ1%2F6&X-Amz-Signature=48c7b52f1b76b3aa7aa9469bbb19d2ba908f76e93a3e98b0407b1c5ebe74feba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLIULPTW%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDcfJZLdgaeIESEXU3Y9L2ApecXPAdj0opgxGGS9CVcgAIgFJ5hfPXnijuSuiLy1uVXCK%2ByDyRxSscYaEDmi0kAOYkq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDNtirL4iGfeZqlE7AircA4eW8nJF2RFjz7FTe82412%2BIhP1uyMb7Vm%2BNwgRAIzN2zApSSB%2Fcg9veUBrhOcGpuMMrj2RuW%2BR3kpohxMYW9zgx2WwWP2I0eeWpir%2B4WxcWv%2B%2BdWTCenxD4pyoIDUX9teEiRgEqwampCv9rVuUq23qxfyNwU2zlBJ%2F0vUWDIhAiiUUc16AFUMgNBccumLNtRKphAQz3c5CBb5WNwmG7%2BGisHl711vd4T%2Bgm9vfVEOnoU41O61TFrJF7SrMnXUqwcjXIIIT37w9hNiznZHu4g0wVrxHLv9rV2s2lKyIvqlRdElfB1DaRkta%2FOJWyQrBVUluBIHij%2F2HMQj711Qqo50Obp6NoOw8x6uollLTTh1rebg6UuLRiCPUC6N8Iy6VdsS2GXGkw%2BshIIddAAsFJxOYy7AcJkWHkCViDj0yksHytuRyJgWvkLwdiSB%2Fig6zeWIHq3tt1nKnKnFRJQRKsGS%2FCInHSm7eJxc3rZcex1SaxtVKcrZHUM0z1MGbLMJ37z094PtksywKWiin7w7qZUq8dtg6CNvwzY6M1VEuquykUwJ7uwyWZR%2Bti%2FOln0ZfmeJ2xjVK0VbjNjl75LkZgg0DS1pTmC6HoBQ%2BcqNn2TPXKCmmAcjEZmX%2BS2XIVML%2BU5bwGOqUBP8zyRgKODes2fH8SR8VnBGJ2Tml3BxPhST89j%2FbsVQX5m4qlP7VUOhJNRgX2BaJUuVjEhylTtL0tC1yLjn2U%2Fs52hwkfTPFoyVJtoQBcEyHGf3OwqPXteqpl6WSZbmuA8Injrhr52xKoG2G8Yy2Py3PrgGn2QlWZ7x0uq7k%2BS4uzkjS6QRq1oOKF4pdjd1xWA%2Foh%2BtCAgQr713w5CVjSeiLTJ1%2F6&X-Amz-Signature=ed17d0b3c3092781b1ea96a4548d2bb5287e23f6d793be7894c79c7f4d5d6ae0&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLIULPTW%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDcfJZLdgaeIESEXU3Y9L2ApecXPAdj0opgxGGS9CVcgAIgFJ5hfPXnijuSuiLy1uVXCK%2ByDyRxSscYaEDmi0kAOYkq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDNtirL4iGfeZqlE7AircA4eW8nJF2RFjz7FTe82412%2BIhP1uyMb7Vm%2BNwgRAIzN2zApSSB%2Fcg9veUBrhOcGpuMMrj2RuW%2BR3kpohxMYW9zgx2WwWP2I0eeWpir%2B4WxcWv%2B%2BdWTCenxD4pyoIDUX9teEiRgEqwampCv9rVuUq23qxfyNwU2zlBJ%2F0vUWDIhAiiUUc16AFUMgNBccumLNtRKphAQz3c5CBb5WNwmG7%2BGisHl711vd4T%2Bgm9vfVEOnoU41O61TFrJF7SrMnXUqwcjXIIIT37w9hNiznZHu4g0wVrxHLv9rV2s2lKyIvqlRdElfB1DaRkta%2FOJWyQrBVUluBIHij%2F2HMQj711Qqo50Obp6NoOw8x6uollLTTh1rebg6UuLRiCPUC6N8Iy6VdsS2GXGkw%2BshIIddAAsFJxOYy7AcJkWHkCViDj0yksHytuRyJgWvkLwdiSB%2Fig6zeWIHq3tt1nKnKnFRJQRKsGS%2FCInHSm7eJxc3rZcex1SaxtVKcrZHUM0z1MGbLMJ37z094PtksywKWiin7w7qZUq8dtg6CNvwzY6M1VEuquykUwJ7uwyWZR%2Bti%2FOln0ZfmeJ2xjVK0VbjNjl75LkZgg0DS1pTmC6HoBQ%2BcqNn2TPXKCmmAcjEZmX%2BS2XIVML%2BU5bwGOqUBP8zyRgKODes2fH8SR8VnBGJ2Tml3BxPhST89j%2FbsVQX5m4qlP7VUOhJNRgX2BaJUuVjEhylTtL0tC1yLjn2U%2Fs52hwkfTPFoyVJtoQBcEyHGf3OwqPXteqpl6WSZbmuA8Injrhr52xKoG2G8Yy2Py3PrgGn2QlWZ7x0uq7k%2BS4uzkjS6QRq1oOKF4pdjd1xWA%2Foh%2BtCAgQr713w5CVjSeiLTJ1%2F6&X-Amz-Signature=11e5b96b3bd2098d26883c8f486febf777bbf86fccc277c39a4ed9592a899165&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TGXJUKD%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIH1MhkYEFRI3Y4NYATcgfFd9MFaV3sjJpJxtdsB3hSpPAiBrYs%2FncRzknutoZqXH5wnCsyBqdys7FcUbVpBX8ndc1Sr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMKVFHP4w3BkqFnXQ0KtwD7Eyfizfh%2BZHmLKl3yrinPvGO1b9mB9KZds6YZWyLjwqyBtQPVf8aQGhWvgAMbP%2BQnUpzGkMxaUVhMmbi8kMO9A%2Fq16xHckQrseOllgk7JddjdnlpQwwXMg7i850QXt87ZC2reJ3vUlg%2Fl5JrwO6UQgEODzhkUvA3enwdFe9U8yOj54OWX5Ut%2FZYjG1tsxSgf5%2FXlraoOHjJLpJFocGsV81TDXob9ZWWc0ss8KvqDA8a4kzXdzKxZksQF2XyDrMwUb6lKoayR5%2BOWZ4%2FdjbcIkHbWcpaCq8R2TJnIoBk21%2BEpDI%2B3Q9WLzWX9O87KwHcbrBqWNSYN2GNNMYVUJzadJ0Dk0Z9fUsrrOPUz2eitpMeeQ37tUtRliFoQ4KGZndlq41P%2BNNyQHxQ71w2yubgv9WE3WndTE8R0gRSu8GCk2UWjvJHkZCFPsEOsDxyRa80OeJERVk4eMk9yySvmx1MiC%2F6k%2FwkaiPcXOt8VfZo0usZrOyw5m2%2FG1TI7bGBhDFades72xpRHH5l4R0NfEI%2FdOqZzbcjvbSHQR3fOlSlUDXRC1ck6RmebSSuV3oiqgSeN8rh2ZER6PSo39d92ZHkkdl2rl13tuRTrdLzOp4aIA%2FW%2BzCBKpwVST50zTBUwopTlvAY6pgGbbDNEudX3XoYDSK8W6l%2FBKbh5VvGXDyTtwJLHoLNQkl8p6WEXJhyt23Zq63%2FcX1pvCNWfiDCiYLQGYic4kSOJDm%2BgL3ejpx9h9YtmUBMJO8Mt3MJB%2BL4Ju5GqU9xy0pb3C8LN3RE6YzWOYEL3k1VJhfG957SYQBxz6smhZWdijNIec3ykjyAF2nR1Ub%2BGTLagoJkQ4tcbIzZetMfu%2BL%2FwcvH6zLTp&X-Amz-Signature=3bb1534b4d15368f15ccb9eedab845febe2be7636a73ae2444cbe9c2f1cda924&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U2JCHKT%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIEWGTI3W%2ByFS%2B2gYH4YkKnxDCaWNJc34%2Fx9lX97BRg8zAiBQZURXclppfKC9hMc02B0e%2BS%2B0fFBR9X%2FGMk26je2U1ir%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMLF%2FVVqoO668ZGm3yKtwD%2F4HVZGrxxje%2BeILud5FsEshtfWNGx6WFhJjA8qO9IiWHB%2BygbhmwSsFLuZXes97on%2BJ2R8GQU5wSntlgXLifgLW8DHe9wPZMaW4edqWBgklBhdf%2Bp2pQPgiH7pTDq0NVxsFGoLxL%2B4DDK840hszdR6EpeD38wzlgbxyW1wp4Xe6Hx%2BSI7AVSvSEAhLld7Dy2SyvTRMxJkKN9znW1o1HfDCNuX6qbC3kAoQGWSEEn%2B70EJdPlpC2iC1xj6D%2B9tO01tIMST%2BaZvYA6oJRKT3nLLJa8xVhLbV3ndQJl32GJ4TekFXg%2FCsQi4yqzIr5fvl606kfFBPwcNTx5s7tv%2F3VoitACInjHv%2FAHPOBvBFCWYML%2F8A3isZogGb5KqbjDbXklfiDZ2HnKltzKMgtQ1Riy3Tnqk0WYFJzew4GUSKovXU%2B7vwBCK9aL3UfVOyUm140oUXtB4pkq6%2Bqd0cYs0mlan1O1hHg1US%2FEg0KMBC3vQT1UGoY9lZdPdctncMAJdDUdVyXPkeXxzqrrKQXs7rl0aEvU9dbC8wApi6LemXcMM48RzH4G3QkZqOQnm2STi3JKtXe7lbL6zCO8%2FhGB9Lveq1PDHy6yf0WWeHNFG6ApfyLPjqrquBgPBGSopDIwqpTlvAY6pgEB%2B3jlUJELMNic4lcXcQK1kvv%2Bt4N%2BdxYkBX1kUFwGak0gPV4rHRQo0bGbszj6xps2uRS3Pjixoq11kqFoVQWgCFmvQPjc8ohhQYOMB51y7scumAa44sNZZVJPfkzvL5%2FRkHAJ3vGMuIfgKrSwmi2Cz6sp69zRmgOP7SUqcJVfqFfSGujoGuv3nEw3jaExvpfojwRNdAH5dif8OGcafd5%2BO6vpTsim&X-Amz-Signature=77f24fad119439329045891e125df4c0460055d2b91c2fedb7addcd295891c2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Y5IAI6N%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIHKfeV7%2FjbNDxB5s3G5C4pSUdoKJk2elVUosfxewu7dcAiAKfX4ChdN%2BJY82NEGzcHi%2B6ta1EpXD3G1447dNZe8AXCr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMFS%2BA2Ndq%2BWUFErwiKtwD7ddHd%2Bh5SeQZjtFn4vbMOOYnMxnSSZuJnkRXaJWbWaFZRtLi9g9PmfxuiylZ9Ls4ffezOjeZbHS8hf9y9a4qvRLv5z61kfbCt8ctSWsfJOQcgecqjksze1R922i2vQmmCxTefvoD1weCrm7H%2BlWfiCA6MpqrCnZryXl1cgzEnieKZuOcL%2FW59c6R1%2FdZz310FYVli1ENpNHFMUxuBF6y1fiP1XS%2BixDHFhFe6QIXIWPIX4%2BBG0uUYF9ZVdLdnMR2ZsEIEu4xnS0V%2BCE%2BaFCgloeiCZU%2B10gKfK%2BmLmS0iZ58BPyJ7sJ4QQ3cmEVTctRxgoq7jBAlCjylO6CQ%2F6i9zfN2nZjExe1DFyAjoVHA75gavpPjxbO1ThmW1NPTcphTmdw64VO40uP7U10TC%2Bj4HO2GPx76W3NQLYbAn%2BTgFkd3LIyZDnLPCGA2rCARSdF21b9DPOkGkn31yw%2FHGSe7ew1obU5IiOtV%2BkkJWVjrL5L65nt2EytEV8tFw1y6se%2BEgqV1xEUNlwXB1BFdCB1Rp%2FEuKSz5WK2aP2mbYSB0O8anOY%2B44jRf76FiOj16V7RsyEtUslYIjfoNdA3Rp5LRAcJ%2B%2BcgxjOlMVqfHKpvWRSDL7kvNEr2ubNa0ynQw6ZTlvAY6pgFd%2BDz8CWBd33FuOqJLahqflJbIhJNQxtYmkRHVQpMKfyc9KlWjL%2FFjf1U99BgnW%2FTPIXJQPA3%2B%2BCQFjyiFJslwiOmKn2q5TDdd8WS%2Fh8ZWD3Y9xV7tXyzbfOsTHjlgGqSkReQibrHx%2BRjhMQMMT4rB%2FfMwIxHoZ0MA42J1M3zHF2U1E6pJu3ki%2BCDUGkI2x5SbhQjjEZl8Aonp1lg%2FRGi0J6mgj5%2FK&X-Amz-Signature=72191cdffa5d0f92c739ce33bc259f208ce9bd16f295e94fc3523d7700547bd8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Y5IAI6N%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIHKfeV7%2FjbNDxB5s3G5C4pSUdoKJk2elVUosfxewu7dcAiAKfX4ChdN%2BJY82NEGzcHi%2B6ta1EpXD3G1447dNZe8AXCr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMFS%2BA2Ndq%2BWUFErwiKtwD7ddHd%2Bh5SeQZjtFn4vbMOOYnMxnSSZuJnkRXaJWbWaFZRtLi9g9PmfxuiylZ9Ls4ffezOjeZbHS8hf9y9a4qvRLv5z61kfbCt8ctSWsfJOQcgecqjksze1R922i2vQmmCxTefvoD1weCrm7H%2BlWfiCA6MpqrCnZryXl1cgzEnieKZuOcL%2FW59c6R1%2FdZz310FYVli1ENpNHFMUxuBF6y1fiP1XS%2BixDHFhFe6QIXIWPIX4%2BBG0uUYF9ZVdLdnMR2ZsEIEu4xnS0V%2BCE%2BaFCgloeiCZU%2B10gKfK%2BmLmS0iZ58BPyJ7sJ4QQ3cmEVTctRxgoq7jBAlCjylO6CQ%2F6i9zfN2nZjExe1DFyAjoVHA75gavpPjxbO1ThmW1NPTcphTmdw64VO40uP7U10TC%2Bj4HO2GPx76W3NQLYbAn%2BTgFkd3LIyZDnLPCGA2rCARSdF21b9DPOkGkn31yw%2FHGSe7ew1obU5IiOtV%2BkkJWVjrL5L65nt2EytEV8tFw1y6se%2BEgqV1xEUNlwXB1BFdCB1Rp%2FEuKSz5WK2aP2mbYSB0O8anOY%2B44jRf76FiOj16V7RsyEtUslYIjfoNdA3Rp5LRAcJ%2B%2BcgxjOlMVqfHKpvWRSDL7kvNEr2ubNa0ynQw6ZTlvAY6pgFd%2BDz8CWBd33FuOqJLahqflJbIhJNQxtYmkRHVQpMKfyc9KlWjL%2FFjf1U99BgnW%2FTPIXJQPA3%2B%2BCQFjyiFJslwiOmKn2q5TDdd8WS%2Fh8ZWD3Y9xV7tXyzbfOsTHjlgGqSkReQibrHx%2BRjhMQMMT4rB%2FfMwIxHoZ0MA42J1M3zHF2U1E6pJu3ki%2BCDUGkI2x5SbhQjjEZl8Aonp1lg%2FRGi0J6mgj5%2FK&X-Amz-Signature=63f87584a48f64dc6d563a07eb6237147986ee6709d0dbe094c0da776ef425d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
