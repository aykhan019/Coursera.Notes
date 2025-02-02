

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=2d2b83e4af9afbc38b3f786fd82b10ca7d631f9ec86ab0057824cc08fea9e15a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=5c3494bdec22be1e3f38184301167cadda5c0800fdd210ae141cba32e02c4a89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=e59aa11ef92007df3ee22834844d5b3ca8aeb8978f62a04bf5539c5a2d022269&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=2ee4ebf34e5893c8fbf28889cfa3faa521d5277e957227c66bb0737c7f9a3040&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=d57040673f47711ff0819054190f613ef13efbcd3c2d4c55f265ddca90888699&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=38bed481069a37a936dcf5392904333d239f60b10ef8bee8ec2e0d0a46b7292c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=ff51e7dece7ba19f2ffae03711ce2f0d02dea41dfc96946d90fffe6547efedb5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=b5cee7b8e11978a7195797fbfcdbeec65002ca792b1395de788d893434c3c876&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663O2VU4OJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBUeUB1PJOXQz2TDL4Ew3Gl1If8AZq%2FlX6CH9sTksUJ6AiBbsxH2jJDNu%2B4HdB0YW4i05%2Bju8CnU8tjO1t3HKuiQRSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIXS%2FvFlFyzwgmxyFKtwDmkl%2B%2BrYPk6QFCvf6TDljTtVuucGtShYPusNQXkRTIxUBcz27NAK%2B8dM8Lx0wRfCgWhPEXaRxM0DKfaCM6kCOW52gg2qhISoz3q87bcgFdB2xWfHly2bzuJDV4AgHD1dLDBwwNV%2FKgU2JlyS9CTIBm%2FN9SmQrHeqvYpVtEYuUzOhRy6dLJlmuY%2Fl5SIig17zqIotuE8h3Wp32KBSaTMCiZ%2BlsKX6rqv5NFzI6QiX6pedn1NJDtnx5JarBpxPawkreu0MsYyadI%2FVqdNk9R%2BeO7o%2FKfmWHREZkigEFKSgftCqwemYFjnajf8CjPWZ1NKNca6Cga0mir6SDLYR9%2F0fDTDb2vctFDbPNnMBsf%2Bk%2F1XrI4KhuHHCxua8GR9i9TvI%2B9ocDylKhyIQZt1S4dcMpeOH1u8KzkVAVFPrjfN9qsuhHPzklXZmJ2wNrULz48eukBdSkwdQdkL3FmhpXNVdHLT10uIx95znmHO%2BM7znKubkNKVJKUmOhzKj2QS34ymJQfB0hAu5IjtAnOWLImv89jPQ6dg3O4r42UgCeEpxhmsLM3OsI9Th%2BkcfRjUJDBdYIiE2gI9UvFo77OKRW%2B8Kg923k8476Zz8jLiQ4vLRj269475dYy0g7bTOZsGow0Jv8vAY6pgG9uSdGaZbZy5zsBU%2BMvER9lPBMGIgsm9L33cDspKutJUdsoIBTZp0ZHRMjArkIPHuxEobVQq4cKmh2cBJ0NU%2FL17T5XXsEkBbnocUgNYbgDgF9nvX%2FGQhErRihTqqFVXNVBR%2FoSYGH0a4oP47h3DRe%2BhcV2pAMi9nqiEiwS1sZNQjqLYuj9cpq6b6vxDu9Aq5knXeSUXVJo5SwLdyWLQ5ga0kvl43l&X-Amz-Signature=428e4a578c9bf24f4cd4b9bf3e627ce0552e9eb9e3687d261e70bda037f89059&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFNPIA6E%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIExisnfZKybB%2FzSFRNXoDSWiHF4LS77lRVyA%2F5WKvV4JAiBltko8ORQV%2Fj2%2BsuPGOH%2FlabUPeqI5RLGpwv7Z5PJYciqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZGOh087kh0u7aGaJKtwDxWxNAZRpsLNdYSrM0NdKvfXyT4C62gDMr4bmP4wqOpm2Ot7168Uf0ns4aMFopAkCg%2BQtuOg8%2FX4RXQ6J%2B%2BjBaWhlZn09qjd2lwBoCdtNL3kWbqq%2Fno0GrbYQpqOt8zhA2yi%2F2e1od%2FOYNlOMjVnRLi%2Fvhc14Fv5wR578QbTSqF3QamncBIZtrWCZh1jPuEXo6L53n59MxzetcE0CXzWfptCb7gWsjZ7bOQrHvO30UhDzB51z7Njxd8wQdXqXmM7UfLK64bnl0sxQzAIs686kIQKKpcHq0ffHnuDRUqsKPIek5DHul%2Bg444WzgraC8JGTWAJivAmDoejIKwGP3JdL28co9pECfAlB7w2ulGUzqQEMr1bfShiF3nXvO2wtTjeMBax%2FaUsYvx2Qckb6JF1fDBPBcsPTygAi4CyjhjvoJQMrHyZ%2FhjKpPFiIly%2FwvJdA%2BES2Q7JxLl76fbtdh1G395M7q1PvukJxRxdflCQwZQJ6BrBsFriTsT1vUpLFIH1U8h8CUymh1K7PMHsc4HIHeuobDG61xg2oahAThWjYsMxny2xFMlUVPx3x1IcqcVzpFl0X90PcLVk3K%2BKPBNXuN%2BH6K0bTSTSwAoSyyvxhSFF%2BMWKTkSVQNT3e74MwqeH7vAY6pgEdVThPoCKTcAMYrphvq29H%2Fx%2F5ptE1glauG0xzgb0VyDaXx1Uy5qonO6HKcuBxOCbibOm6USG14LYeDZgpQNpcVQ3XX20IhJeQvgeyD77zaycwTm4mq%2BvVhwGyHDxnlTI1i1b88tn1HyghKXuUWrbQVtzdZT%2FU%2BRvb5Z1fP0cvSehXq7nvVDFMLyi8AqXBJB8TqOfv4kBovaJvBfr5ITnNEvS%2BXcnJ&X-Amz-Signature=e5b9fe031f214c591e77e55b8a611e78ded83b313256fb06c01d645fe4ea23e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGSMKDWQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBLHIMv%2BdCF46j%2BGSq0fDK2MwJ6uKyEqkgXKN41uDrvAiEAn8GXcafyD6kghyWzk9P1MwlnwTJyGAp4WJqNpQbDWMkqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBiUSWoIfURJSH8icircA7cw0W4X8O%2Byd6yCrmbQocdVG9dhAnjdRuLzo3exCaBWCF8roSEUOFUSK%2FZW%2B%2Bkn3MxTHyNFWP3TAqz%2FseJQFuAmWWwHzzOGXfBHMWIM6HHpRikbmxpj6pJttoVHSAe4jr9whVD28ddTXxI2yOOz4w4UiLeAkJqK8g5pj%2Bk5bT0qoaZOvGssdWPQBBwjt7aNNASPVJQ0pD0ID8pLWFQHp2GxivHV824Qc0txH9mamx2JaN5zeljLgLeFYJRmQE5fUXn7i8EFSeCMlXfFFLdpiCdHukL%2Bo9G4EXD5x1tv%2B3RDXOa1uyPXaCGjHgDWy3gTiEqNgnAHrId4Vn%2BP1mKutu1aqkeOe764Jzen8ewvywuNvOxlnRMRv2dW%2BuiL1PkHfD%2FPdxvWcXYcXsmqWzOdoKSghOUxeDv9DWjwFwmtw7evCa1qZ16cGnv0iZlBeIp4ew6AJkxdeLuH4ExHJ5NAUEY1yZtlvpjbhXZGgWVQiGvf50Fu6YYF5kQY5JNuSIlAj0MWQsaBEeeb7r3SMQaOP0mf3XaKY50%2B6KuD1llM4evuxY94cLBOerKkbWqxf0YMX3ioHEVoG1YaurwSlaGnDZoDBzW2HjYxHCEhXN0e5I2y5NmCNFl0iomqX4Q6MNib%2FLwGOqUBRc0O8a6uKUZx%2FutTffXt%2FeYrG9LClrtNLnCNnWswNKwgAjJq0rp2OS%2Flcc7EVcslTxYejPw6K4JAGHOngesHPWNWyG83CdgU6QMf2ydwcxorn7%2Fj3SALJP4ZGAJkXajSxpW77fSjsVEn3sTOMSxuoYfOm3eGQviRShjdyTieECABtc51C3of7Dxaeml%2Bu2t0QXBgCCzPLDe0%2BZFrolwem8FTYaxZ&X-Amz-Signature=21198f22d58393c47e51115703cfda53d8c6bac0a9bbc56791f25c90a76442af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGSMKDWQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBLHIMv%2BdCF46j%2BGSq0fDK2MwJ6uKyEqkgXKN41uDrvAiEAn8GXcafyD6kghyWzk9P1MwlnwTJyGAp4WJqNpQbDWMkqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBiUSWoIfURJSH8icircA7cw0W4X8O%2Byd6yCrmbQocdVG9dhAnjdRuLzo3exCaBWCF8roSEUOFUSK%2FZW%2B%2Bkn3MxTHyNFWP3TAqz%2FseJQFuAmWWwHzzOGXfBHMWIM6HHpRikbmxpj6pJttoVHSAe4jr9whVD28ddTXxI2yOOz4w4UiLeAkJqK8g5pj%2Bk5bT0qoaZOvGssdWPQBBwjt7aNNASPVJQ0pD0ID8pLWFQHp2GxivHV824Qc0txH9mamx2JaN5zeljLgLeFYJRmQE5fUXn7i8EFSeCMlXfFFLdpiCdHukL%2Bo9G4EXD5x1tv%2B3RDXOa1uyPXaCGjHgDWy3gTiEqNgnAHrId4Vn%2BP1mKutu1aqkeOe764Jzen8ewvywuNvOxlnRMRv2dW%2BuiL1PkHfD%2FPdxvWcXYcXsmqWzOdoKSghOUxeDv9DWjwFwmtw7evCa1qZ16cGnv0iZlBeIp4ew6AJkxdeLuH4ExHJ5NAUEY1yZtlvpjbhXZGgWVQiGvf50Fu6YYF5kQY5JNuSIlAj0MWQsaBEeeb7r3SMQaOP0mf3XaKY50%2B6KuD1llM4evuxY94cLBOerKkbWqxf0YMX3ioHEVoG1YaurwSlaGnDZoDBzW2HjYxHCEhXN0e5I2y5NmCNFl0iomqX4Q6MNib%2FLwGOqUBRc0O8a6uKUZx%2FutTffXt%2FeYrG9LClrtNLnCNnWswNKwgAjJq0rp2OS%2Flcc7EVcslTxYejPw6K4JAGHOngesHPWNWyG83CdgU6QMf2ydwcxorn7%2Fj3SALJP4ZGAJkXajSxpW77fSjsVEn3sTOMSxuoYfOm3eGQviRShjdyTieECABtc51C3of7Dxaeml%2Bu2t0QXBgCCzPLDe0%2BZFrolwem8FTYaxZ&X-Amz-Signature=c6b9767cfb595d374921c705a2e588eb6fa073f3cad4b3cd939edf2d3afd2019&X-Amz-SignedHeaders=host&x-id=GetObject)
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
