

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJT7URFN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIC2AhMqABwFOTjRnlNZtsqE%2FPA%2F%2FJV%2FF9TAE3ut3BLjBAiBK1wl95nKHSzcdPJEDf5oUcCGcp43gjlEKyOXrfWpcoir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMwQaGZXsHdkXOSOxSKtwDk5y6SgmiJvl6kOARYIBjHoLa%2BraM4KZ5x9M6ILhfchaSVvSI%2FNDv3U2hMPxMGQc5nAM2PUrlVs49T4gU2IDno1XkSpi79EktxSljJJGo7l01nDUKuSc%2B88PU%2FA9JvS2OhPj%2BpOxYuYedRlLEQEFUSVCYcbjcOLoI0885VAziPU6mfM6gGM8C5lQB7O6FYjfnX4nT2aUhkyaHZkXA39snQCe8xEDtWzELNCmG9iJhFCP0qKf0nE%2FvNRJoF56DBq2yNtT99y6aAL4LgpMNfuyGjJYefVDAyZqnpgUqFtioH3CB%2F7wo1r%2FMxqvD%2FRAAQAMAxz6sAVdTbBPtgu0jKBVMZyjGK7ngj27%2B7Z5bmzO4ohFxv0jYR5IFRVmhLyEKMgS6tc8nFvrtj9dwErUsAXJcWTOEJ1gXPvR3NqpUktEHBPzJfKnsHa%2BAYhcsE8iibrRZ2bdyQIUJZ7U360ZQhmLKEgNNNRYVaoY%2BdZcncDu8XFQY2ti74es5GcPF4C%2Bj6AkhoB5uBrYsFiqYbyKaKm3WO%2F9ux66EJ42tIQHLS3QVjapX1ZOjmwmGjOYB3oLuoug0SZHpzYz59ZHFeutAJNjTa%2BBZJOorrPOMdpOZI23L%2B3j5tCPKk6uw%2FP1vrXAwzvmWvQY6pgG9OZ65DfnVctsYEtD2IOyUGpshxaJIRdgLZLrFKZljvgtj8VKZuy%2BIV0khYiYPTHj%2Fv9IyAhtddklIXgjM6bD6dJM15zF0O39XIdx6z49ekvC7WXdaoIC%2B0cFtYH5EEcEOF2EW0wISblV2cbAbVfMLQQ27ZQ7DvZv6uSdQWykvj3tBIlwaq%2BGqIpGELYZeA4cdmaSTyEYPNHoBbBuXkJtWmbagznkK&X-Amz-Signature=527259b1bc218309fbbeb35d6c6686263e2305ffbb53e63b98ee40ef188a2e3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJT7URFN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIC2AhMqABwFOTjRnlNZtsqE%2FPA%2F%2FJV%2FF9TAE3ut3BLjBAiBK1wl95nKHSzcdPJEDf5oUcCGcp43gjlEKyOXrfWpcoir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMwQaGZXsHdkXOSOxSKtwDk5y6SgmiJvl6kOARYIBjHoLa%2BraM4KZ5x9M6ILhfchaSVvSI%2FNDv3U2hMPxMGQc5nAM2PUrlVs49T4gU2IDno1XkSpi79EktxSljJJGo7l01nDUKuSc%2B88PU%2FA9JvS2OhPj%2BpOxYuYedRlLEQEFUSVCYcbjcOLoI0885VAziPU6mfM6gGM8C5lQB7O6FYjfnX4nT2aUhkyaHZkXA39snQCe8xEDtWzELNCmG9iJhFCP0qKf0nE%2FvNRJoF56DBq2yNtT99y6aAL4LgpMNfuyGjJYefVDAyZqnpgUqFtioH3CB%2F7wo1r%2FMxqvD%2FRAAQAMAxz6sAVdTbBPtgu0jKBVMZyjGK7ngj27%2B7Z5bmzO4ohFxv0jYR5IFRVmhLyEKMgS6tc8nFvrtj9dwErUsAXJcWTOEJ1gXPvR3NqpUktEHBPzJfKnsHa%2BAYhcsE8iibrRZ2bdyQIUJZ7U360ZQhmLKEgNNNRYVaoY%2BdZcncDu8XFQY2ti74es5GcPF4C%2Bj6AkhoB5uBrYsFiqYbyKaKm3WO%2F9ux66EJ42tIQHLS3QVjapX1ZOjmwmGjOYB3oLuoug0SZHpzYz59ZHFeutAJNjTa%2BBZJOorrPOMdpOZI23L%2B3j5tCPKk6uw%2FP1vrXAwzvmWvQY6pgG9OZ65DfnVctsYEtD2IOyUGpshxaJIRdgLZLrFKZljvgtj8VKZuy%2BIV0khYiYPTHj%2Fv9IyAhtddklIXgjM6bD6dJM15zF0O39XIdx6z49ekvC7WXdaoIC%2B0cFtYH5EEcEOF2EW0wISblV2cbAbVfMLQQ27ZQ7DvZv6uSdQWykvj3tBIlwaq%2BGqIpGELYZeA4cdmaSTyEYPNHoBbBuXkJtWmbagznkK&X-Amz-Signature=0c01d691b233ac66ab8ee154b1b2fff7080464931d1f620576945bb4b0bdcf0e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJT7URFN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIC2AhMqABwFOTjRnlNZtsqE%2FPA%2F%2FJV%2FF9TAE3ut3BLjBAiBK1wl95nKHSzcdPJEDf5oUcCGcp43gjlEKyOXrfWpcoir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMwQaGZXsHdkXOSOxSKtwDk5y6SgmiJvl6kOARYIBjHoLa%2BraM4KZ5x9M6ILhfchaSVvSI%2FNDv3U2hMPxMGQc5nAM2PUrlVs49T4gU2IDno1XkSpi79EktxSljJJGo7l01nDUKuSc%2B88PU%2FA9JvS2OhPj%2BpOxYuYedRlLEQEFUSVCYcbjcOLoI0885VAziPU6mfM6gGM8C5lQB7O6FYjfnX4nT2aUhkyaHZkXA39snQCe8xEDtWzELNCmG9iJhFCP0qKf0nE%2FvNRJoF56DBq2yNtT99y6aAL4LgpMNfuyGjJYefVDAyZqnpgUqFtioH3CB%2F7wo1r%2FMxqvD%2FRAAQAMAxz6sAVdTbBPtgu0jKBVMZyjGK7ngj27%2B7Z5bmzO4ohFxv0jYR5IFRVmhLyEKMgS6tc8nFvrtj9dwErUsAXJcWTOEJ1gXPvR3NqpUktEHBPzJfKnsHa%2BAYhcsE8iibrRZ2bdyQIUJZ7U360ZQhmLKEgNNNRYVaoY%2BdZcncDu8XFQY2ti74es5GcPF4C%2Bj6AkhoB5uBrYsFiqYbyKaKm3WO%2F9ux66EJ42tIQHLS3QVjapX1ZOjmwmGjOYB3oLuoug0SZHpzYz59ZHFeutAJNjTa%2BBZJOorrPOMdpOZI23L%2B3j5tCPKk6uw%2FP1vrXAwzvmWvQY6pgG9OZ65DfnVctsYEtD2IOyUGpshxaJIRdgLZLrFKZljvgtj8VKZuy%2BIV0khYiYPTHj%2Fv9IyAhtddklIXgjM6bD6dJM15zF0O39XIdx6z49ekvC7WXdaoIC%2B0cFtYH5EEcEOF2EW0wISblV2cbAbVfMLQQ27ZQ7DvZv6uSdQWykvj3tBIlwaq%2BGqIpGELYZeA4cdmaSTyEYPNHoBbBuXkJtWmbagznkK&X-Amz-Signature=769c057c101deda2d0a1b3d01bf95ca161f2822e76c9a6144274c707fcf48e1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJT7URFN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIC2AhMqABwFOTjRnlNZtsqE%2FPA%2F%2FJV%2FF9TAE3ut3BLjBAiBK1wl95nKHSzcdPJEDf5oUcCGcp43gjlEKyOXrfWpcoir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMwQaGZXsHdkXOSOxSKtwDk5y6SgmiJvl6kOARYIBjHoLa%2BraM4KZ5x9M6ILhfchaSVvSI%2FNDv3U2hMPxMGQc5nAM2PUrlVs49T4gU2IDno1XkSpi79EktxSljJJGo7l01nDUKuSc%2B88PU%2FA9JvS2OhPj%2BpOxYuYedRlLEQEFUSVCYcbjcOLoI0885VAziPU6mfM6gGM8C5lQB7O6FYjfnX4nT2aUhkyaHZkXA39snQCe8xEDtWzELNCmG9iJhFCP0qKf0nE%2FvNRJoF56DBq2yNtT99y6aAL4LgpMNfuyGjJYefVDAyZqnpgUqFtioH3CB%2F7wo1r%2FMxqvD%2FRAAQAMAxz6sAVdTbBPtgu0jKBVMZyjGK7ngj27%2B7Z5bmzO4ohFxv0jYR5IFRVmhLyEKMgS6tc8nFvrtj9dwErUsAXJcWTOEJ1gXPvR3NqpUktEHBPzJfKnsHa%2BAYhcsE8iibrRZ2bdyQIUJZ7U360ZQhmLKEgNNNRYVaoY%2BdZcncDu8XFQY2ti74es5GcPF4C%2Bj6AkhoB5uBrYsFiqYbyKaKm3WO%2F9ux66EJ42tIQHLS3QVjapX1ZOjmwmGjOYB3oLuoug0SZHpzYz59ZHFeutAJNjTa%2BBZJOorrPOMdpOZI23L%2B3j5tCPKk6uw%2FP1vrXAwzvmWvQY6pgG9OZ65DfnVctsYEtD2IOyUGpshxaJIRdgLZLrFKZljvgtj8VKZuy%2BIV0khYiYPTHj%2Fv9IyAhtddklIXgjM6bD6dJM15zF0O39XIdx6z49ekvC7WXdaoIC%2B0cFtYH5EEcEOF2EW0wISblV2cbAbVfMLQQ27ZQ7DvZv6uSdQWykvj3tBIlwaq%2BGqIpGELYZeA4cdmaSTyEYPNHoBbBuXkJtWmbagznkK&X-Amz-Signature=585119889d82f3a53ea86c7facf1007d372e65b8d28a764e9adac9959eb14713&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJT7URFN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIC2AhMqABwFOTjRnlNZtsqE%2FPA%2F%2FJV%2FF9TAE3ut3BLjBAiBK1wl95nKHSzcdPJEDf5oUcCGcp43gjlEKyOXrfWpcoir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMwQaGZXsHdkXOSOxSKtwDk5y6SgmiJvl6kOARYIBjHoLa%2BraM4KZ5x9M6ILhfchaSVvSI%2FNDv3U2hMPxMGQc5nAM2PUrlVs49T4gU2IDno1XkSpi79EktxSljJJGo7l01nDUKuSc%2B88PU%2FA9JvS2OhPj%2BpOxYuYedRlLEQEFUSVCYcbjcOLoI0885VAziPU6mfM6gGM8C5lQB7O6FYjfnX4nT2aUhkyaHZkXA39snQCe8xEDtWzELNCmG9iJhFCP0qKf0nE%2FvNRJoF56DBq2yNtT99y6aAL4LgpMNfuyGjJYefVDAyZqnpgUqFtioH3CB%2F7wo1r%2FMxqvD%2FRAAQAMAxz6sAVdTbBPtgu0jKBVMZyjGK7ngj27%2B7Z5bmzO4ohFxv0jYR5IFRVmhLyEKMgS6tc8nFvrtj9dwErUsAXJcWTOEJ1gXPvR3NqpUktEHBPzJfKnsHa%2BAYhcsE8iibrRZ2bdyQIUJZ7U360ZQhmLKEgNNNRYVaoY%2BdZcncDu8XFQY2ti74es5GcPF4C%2Bj6AkhoB5uBrYsFiqYbyKaKm3WO%2F9ux66EJ42tIQHLS3QVjapX1ZOjmwmGjOYB3oLuoug0SZHpzYz59ZHFeutAJNjTa%2BBZJOorrPOMdpOZI23L%2B3j5tCPKk6uw%2FP1vrXAwzvmWvQY6pgG9OZ65DfnVctsYEtD2IOyUGpshxaJIRdgLZLrFKZljvgtj8VKZuy%2BIV0khYiYPTHj%2Fv9IyAhtddklIXgjM6bD6dJM15zF0O39XIdx6z49ekvC7WXdaoIC%2B0cFtYH5EEcEOF2EW0wISblV2cbAbVfMLQQ27ZQ7DvZv6uSdQWykvj3tBIlwaq%2BGqIpGELYZeA4cdmaSTyEYPNHoBbBuXkJtWmbagznkK&X-Amz-Signature=37081778b8e50c143a01982fadac4585aa687177435e624f8288e7647e4ac864&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJT7URFN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIC2AhMqABwFOTjRnlNZtsqE%2FPA%2F%2FJV%2FF9TAE3ut3BLjBAiBK1wl95nKHSzcdPJEDf5oUcCGcp43gjlEKyOXrfWpcoir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMwQaGZXsHdkXOSOxSKtwDk5y6SgmiJvl6kOARYIBjHoLa%2BraM4KZ5x9M6ILhfchaSVvSI%2FNDv3U2hMPxMGQc5nAM2PUrlVs49T4gU2IDno1XkSpi79EktxSljJJGo7l01nDUKuSc%2B88PU%2FA9JvS2OhPj%2BpOxYuYedRlLEQEFUSVCYcbjcOLoI0885VAziPU6mfM6gGM8C5lQB7O6FYjfnX4nT2aUhkyaHZkXA39snQCe8xEDtWzELNCmG9iJhFCP0qKf0nE%2FvNRJoF56DBq2yNtT99y6aAL4LgpMNfuyGjJYefVDAyZqnpgUqFtioH3CB%2F7wo1r%2FMxqvD%2FRAAQAMAxz6sAVdTbBPtgu0jKBVMZyjGK7ngj27%2B7Z5bmzO4ohFxv0jYR5IFRVmhLyEKMgS6tc8nFvrtj9dwErUsAXJcWTOEJ1gXPvR3NqpUktEHBPzJfKnsHa%2BAYhcsE8iibrRZ2bdyQIUJZ7U360ZQhmLKEgNNNRYVaoY%2BdZcncDu8XFQY2ti74es5GcPF4C%2Bj6AkhoB5uBrYsFiqYbyKaKm3WO%2F9ux66EJ42tIQHLS3QVjapX1ZOjmwmGjOYB3oLuoug0SZHpzYz59ZHFeutAJNjTa%2BBZJOorrPOMdpOZI23L%2B3j5tCPKk6uw%2FP1vrXAwzvmWvQY6pgG9OZ65DfnVctsYEtD2IOyUGpshxaJIRdgLZLrFKZljvgtj8VKZuy%2BIV0khYiYPTHj%2Fv9IyAhtddklIXgjM6bD6dJM15zF0O39XIdx6z49ekvC7WXdaoIC%2B0cFtYH5EEcEOF2EW0wISblV2cbAbVfMLQQ27ZQ7DvZv6uSdQWykvj3tBIlwaq%2BGqIpGELYZeA4cdmaSTyEYPNHoBbBuXkJtWmbagznkK&X-Amz-Signature=ba54c689ef3461ce4da8d1244bf641df0c318819b526d335b83ef3aa9f0f9c23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJT7URFN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIC2AhMqABwFOTjRnlNZtsqE%2FPA%2F%2FJV%2FF9TAE3ut3BLjBAiBK1wl95nKHSzcdPJEDf5oUcCGcp43gjlEKyOXrfWpcoir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMwQaGZXsHdkXOSOxSKtwDk5y6SgmiJvl6kOARYIBjHoLa%2BraM4KZ5x9M6ILhfchaSVvSI%2FNDv3U2hMPxMGQc5nAM2PUrlVs49T4gU2IDno1XkSpi79EktxSljJJGo7l01nDUKuSc%2B88PU%2FA9JvS2OhPj%2BpOxYuYedRlLEQEFUSVCYcbjcOLoI0885VAziPU6mfM6gGM8C5lQB7O6FYjfnX4nT2aUhkyaHZkXA39snQCe8xEDtWzELNCmG9iJhFCP0qKf0nE%2FvNRJoF56DBq2yNtT99y6aAL4LgpMNfuyGjJYefVDAyZqnpgUqFtioH3CB%2F7wo1r%2FMxqvD%2FRAAQAMAxz6sAVdTbBPtgu0jKBVMZyjGK7ngj27%2B7Z5bmzO4ohFxv0jYR5IFRVmhLyEKMgS6tc8nFvrtj9dwErUsAXJcWTOEJ1gXPvR3NqpUktEHBPzJfKnsHa%2BAYhcsE8iibrRZ2bdyQIUJZ7U360ZQhmLKEgNNNRYVaoY%2BdZcncDu8XFQY2ti74es5GcPF4C%2Bj6AkhoB5uBrYsFiqYbyKaKm3WO%2F9ux66EJ42tIQHLS3QVjapX1ZOjmwmGjOYB3oLuoug0SZHpzYz59ZHFeutAJNjTa%2BBZJOorrPOMdpOZI23L%2B3j5tCPKk6uw%2FP1vrXAwzvmWvQY6pgG9OZ65DfnVctsYEtD2IOyUGpshxaJIRdgLZLrFKZljvgtj8VKZuy%2BIV0khYiYPTHj%2Fv9IyAhtddklIXgjM6bD6dJM15zF0O39XIdx6z49ekvC7WXdaoIC%2B0cFtYH5EEcEOF2EW0wISblV2cbAbVfMLQQ27ZQ7DvZv6uSdQWykvj3tBIlwaq%2BGqIpGELYZeA4cdmaSTyEYPNHoBbBuXkJtWmbagznkK&X-Amz-Signature=6eae244d58430effd994ac07193a7293fcb10b2e78b035115166365a2e870e26&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJT7URFN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIC2AhMqABwFOTjRnlNZtsqE%2FPA%2F%2FJV%2FF9TAE3ut3BLjBAiBK1wl95nKHSzcdPJEDf5oUcCGcp43gjlEKyOXrfWpcoir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMwQaGZXsHdkXOSOxSKtwDk5y6SgmiJvl6kOARYIBjHoLa%2BraM4KZ5x9M6ILhfchaSVvSI%2FNDv3U2hMPxMGQc5nAM2PUrlVs49T4gU2IDno1XkSpi79EktxSljJJGo7l01nDUKuSc%2B88PU%2FA9JvS2OhPj%2BpOxYuYedRlLEQEFUSVCYcbjcOLoI0885VAziPU6mfM6gGM8C5lQB7O6FYjfnX4nT2aUhkyaHZkXA39snQCe8xEDtWzELNCmG9iJhFCP0qKf0nE%2FvNRJoF56DBq2yNtT99y6aAL4LgpMNfuyGjJYefVDAyZqnpgUqFtioH3CB%2F7wo1r%2FMxqvD%2FRAAQAMAxz6sAVdTbBPtgu0jKBVMZyjGK7ngj27%2B7Z5bmzO4ohFxv0jYR5IFRVmhLyEKMgS6tc8nFvrtj9dwErUsAXJcWTOEJ1gXPvR3NqpUktEHBPzJfKnsHa%2BAYhcsE8iibrRZ2bdyQIUJZ7U360ZQhmLKEgNNNRYVaoY%2BdZcncDu8XFQY2ti74es5GcPF4C%2Bj6AkhoB5uBrYsFiqYbyKaKm3WO%2F9ux66EJ42tIQHLS3QVjapX1ZOjmwmGjOYB3oLuoug0SZHpzYz59ZHFeutAJNjTa%2BBZJOorrPOMdpOZI23L%2B3j5tCPKk6uw%2FP1vrXAwzvmWvQY6pgG9OZ65DfnVctsYEtD2IOyUGpshxaJIRdgLZLrFKZljvgtj8VKZuy%2BIV0khYiYPTHj%2Fv9IyAhtddklIXgjM6bD6dJM15zF0O39XIdx6z49ekvC7WXdaoIC%2B0cFtYH5EEcEOF2EW0wISblV2cbAbVfMLQQ27ZQ7DvZv6uSdQWykvj3tBIlwaq%2BGqIpGELYZeA4cdmaSTyEYPNHoBbBuXkJtWmbagznkK&X-Amz-Signature=2df76f4d473098cdd57090cb6c2875b4475f8c5d00165c1fc6550307bfac60dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEMZWCOZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJGMEQCIFDwHjIrs2iGz5Agb6ml3xe4rT%2Fbi%2FMvpxrwM%2BnqpQjAAiBDRLGVg8QO%2BUmj0NE%2B8iccGq7RENi2hIodl%2BPunPQDoir%2FAwhxEAAaDDYzNzQyMzE4MzgwNSIMvwwGXoXmaSXcnjSTKtwDlxvexCwkpZgH22sMV0%2F2E4u6Ud%2BJXxIWZ9gec2GPmtx7hKxFtN%2Fc%2F087oiPWQv6j1gxpAaFUER8jTqaeEUQzh7aScu8X0Qq9fPE0izuKP8AQ2mX7mkPIPRJ%2Bwp3bkPW%2Faydh0bR7XdLTmRL%2BXTBxRtGdfRrXh0LgWFTXZPlOG6QvWqd%2FP6YREvXxR5L4%2BP4%2F%2BuQ9j1I8mhC%2FFJoqFdWGi%2BHETvsMOXiK5onJkLEn4MyCT9kWJkX726MeV6Ocnz%2BtzxJXvaYyIH2iPm1CQfMySa5kstOPZk5YRkdgOpNm85h3RmmfElYXvaGMu4FcloLT3lv2IoD4ZvXNLlhfzcs%2BCN2mhyitEPCKhLuIZTdYTCDW4tgmMvrD8n1mqNBEUWHqGD3uCpRyOtMG7JCX2Rgqfnih0PxxzBKPis0CImJW1kYR2NYSDfdoUjZWjFh3QBIyMUy5DbuPYsa8sRYaNdaUreW797ZKfL2m7VxEfo0pADtRfOE6YKQXJBNOrLjgGRzZsYanKxU00dFj4o7FCzOrlHZkUSAfGsHO9By23Eki5wnSe7izv37sQufO1VdwL6v5jZ9j9KkFpTRoqm9R4s01EJY6Bae4JnqXGMshTB9%2BU91agzn3ZVBAytqnnCIwqvuWvQY6pgGzAYo9%2F8Wioe2sFw%2FxpeLLSupvqhmuNYw%2BlU9sU%2FQ0Knoy%2FPszrtrF0QvTMW0ApjUtToaUQ%2FuositkP2krY%2FTb3r6UmqzExUZIZvUktEtMxKxDMIK6x5GJloYdach90wuukaE6%2B76nZ6KUCjB1WwEjBeE8ETMQSl%2FlbsapPqS%2BZnlTY5TKmrQeGe5F3c7ECNY1PEfoIiebL1Jz5VjBz3cixog1VSZA&X-Amz-Signature=ffd0f227cc0f57b58c5af5bcea4db391d9023526bfa17a0103729feff330b1a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVAGHZMM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQD5%2B6FJMDvrSgijhaNrYZoTEs%2BNp0i%2BI%2BEh62Xpk5KN2gIhAKiOPTFaFq%2Bnqx7njdw0exjx2gc3RZ4y62XpNXNUkefXKv8DCHEQABoMNjM3NDIzMTgzODA1IgwjekER75qBTz9ygKYq3ANKYAA1zf1VGNURhM9nlhyzCyFRcNX4jsryBJHd24wijKMMxTJCHREy7%2F%2FNo8w4tGe1iCgUlyztI1enFvtcKmYfsDVi6oQ52gR5%2BsqalU5bke4p7WLRsZ432JD0bD4%2Bs%2BMRr47DggurM24gYbhWTOhwZkpUwDhJOIXOUJq4lOr4t3f4XaF%2Bj29i%2FaK%2BqKT2TwjPbO9yQrjq%2Fm%2Btaw8jURlmOrNL772D0gvu6N1DFpJllK74QYhwC3MWdmXO85XVpWTEBAbODmllqWcew4DrUPtgue3LMT008YnDCU%2BztfFbVw72GoKJg0EtRctX5EvcvgHFj9l9ysoltOSpvHU7QivcTF7UJ81K6bH2CVzNB6BekxAtNStqKszNf%2B9IptPNP3GnDm5dfO7b0zk4Dp%2BszRoJrnE9pXvNoykuwOE8JNZItGVrlPJSOUP5IJPHaUog6U%2FfFrS2D2zqQD4VrW6ZTNIL3cIo3fkC%2BQpb%2BQgEvlSV3XhZAgmrfesoiVFNB90hYBksBhgPiw%2B0kx%2BaquA%2B87FlMbqEojw957p1sGWBYMsmgUG4Ns1DpMDyQUdG%2Bpj%2FslKUZgnT1j6lu1%2BRD9Nd0ClYe8S8i%2B3CgC5qzwM7elHa8x7oDow7hTc6UU%2BibjDK%2BZa9BjqkAR%2FtRA%2FimD81UtInZELBrLei840zXTqpv%2B%2Fl2yiS4CJNfENXwzVoCmwHjMmNgu0wmev9kadHdi2AhOiy9tJWpa6TrxczqqRRDbMIzuem%2FPUJW46fXvHJJ2hK5McS93eKIWpLa05gf37mfivA1MvaB%2Bzo1mBch%2FCs7nXl1CZ7bTQrwwsmlPFrTS4NA1d%2BoeUOsm8c0ve94eH1pFC%2BfI9E6FFCgGeE&X-Amz-Signature=475dbb1a48e4250ea2c00cdb366ebcfcec95d3f4895ec199c1c1c79ff4bb570a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LVBHZIP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDWL4czZELPDraatpNHgPAyYImX9wwl%2BBYV2yd45%2BRWtwIgcSjy%2FOx%2F4ZQsA9fF5QlQwYr8M8QrVUoLDDwYvMFeK94q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFYubOaoGOLzh%2BDeyCrcAwUkVAFyWGDF78e7kBBfYgSaY0jxp0zTVsmJj%2F2l4kv%2Fr5DS0e2iz3tZAummwoqwk0kyWgKyZxud%2BrNOienziajXmNajd7qqVQSgdEAIGD3bFJWQhm0SnDwsYqjmzq5k5vc%2FqE2%2FBRoSn9aRwrBiXc5OqfpbjH1vlquFJErQUBq7okhNQ2EFs9qciJ%2BYU6DGUDahVAQ8%2FZsE3KUyPGA73UrUsQuJFQsR1rC6bvPK1Oti36%2Fdd1UyReryeMwBYyeHLqM1lfevXE9cNgbn5PQqQGpSiJywkx5UVQ4AC%2ByAjw6xa0KrSRajIl2wK9o9Qy7uW2WGTamaXnMxPkyjv6yJ1wEOrefHYDjyW6CyOClbYiAgYPLMdSMS6s5d%2FqNVbmeomnqAPbIUsV%2FIDZt7SPjnk66q%2Ftoc3vM6gVrco0syWAdmqnxHwXkaUJ9LBDLGTNfMxy96tphLqvbF%2BvJBXAjjT2y0VUPFfRqwXSlSxoC5TjbIUt8fuINtjucbETZqXDG09XRHA%2FOAUji2HrvJAqxlB%2BfBr%2FxQ6NOgFgsBBYCzviwcNg%2BXsx%2Bi4p3%2Fx2%2BsKog6RcOVsiWIRrhWdjHzrcRvLtVzp3UdSKeniDosvZpq0pgoZ7zBNIVC3MhopHobMPv5lr0GOqUBzN8eCtgTv%2FQYuCrcpqoXs3TbWwSwx3ucji9DoNIXysCES18U5kBEXjfFNUWUk3Y64m1hnr3952hU%2BAP6dcnTBR5w8QdMr3JDllmqABnbd5oxDF3htqB1UwIoMFcwJXo9htjRuxEG69FrFiI4fjuKtjkk4XWxsnGee6nf%2BGGIRPD7ojkjA3R1ESFl3x%2FpDLW2tJSAFHMEKB65jnJdE5o9qqeCPu%2BA&X-Amz-Signature=fa54a815b6c317cf38e7dbfc6e3dc84cd18e32828e4fb25873a9310a6eab09cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LVBHZIP%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIQDWL4czZELPDraatpNHgPAyYImX9wwl%2BBYV2yd45%2BRWtwIgcSjy%2FOx%2F4ZQsA9fF5QlQwYr8M8QrVUoLDDwYvMFeK94q%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDFYubOaoGOLzh%2BDeyCrcAwUkVAFyWGDF78e7kBBfYgSaY0jxp0zTVsmJj%2F2l4kv%2Fr5DS0e2iz3tZAummwoqwk0kyWgKyZxud%2BrNOienziajXmNajd7qqVQSgdEAIGD3bFJWQhm0SnDwsYqjmzq5k5vc%2FqE2%2FBRoSn9aRwrBiXc5OqfpbjH1vlquFJErQUBq7okhNQ2EFs9qciJ%2BYU6DGUDahVAQ8%2FZsE3KUyPGA73UrUsQuJFQsR1rC6bvPK1Oti36%2Fdd1UyReryeMwBYyeHLqM1lfevXE9cNgbn5PQqQGpSiJywkx5UVQ4AC%2ByAjw6xa0KrSRajIl2wK9o9Qy7uW2WGTamaXnMxPkyjv6yJ1wEOrefHYDjyW6CyOClbYiAgYPLMdSMS6s5d%2FqNVbmeomnqAPbIUsV%2FIDZt7SPjnk66q%2Ftoc3vM6gVrco0syWAdmqnxHwXkaUJ9LBDLGTNfMxy96tphLqvbF%2BvJBXAjjT2y0VUPFfRqwXSlSxoC5TjbIUt8fuINtjucbETZqXDG09XRHA%2FOAUji2HrvJAqxlB%2BfBr%2FxQ6NOgFgsBBYCzviwcNg%2BXsx%2Bi4p3%2Fx2%2BsKog6RcOVsiWIRrhWdjHzrcRvLtVzp3UdSKeniDosvZpq0pgoZ7zBNIVC3MhopHobMPv5lr0GOqUBzN8eCtgTv%2FQYuCrcpqoXs3TbWwSwx3ucji9DoNIXysCES18U5kBEXjfFNUWUk3Y64m1hnr3952hU%2BAP6dcnTBR5w8QdMr3JDllmqABnbd5oxDF3htqB1UwIoMFcwJXo9htjRuxEG69FrFiI4fjuKtjkk4XWxsnGee6nf%2BGGIRPD7ojkjA3R1ESFl3x%2FpDLW2tJSAFHMEKB65jnJdE5o9qqeCPu%2BA&X-Amz-Signature=c351518892e338c0d119119b7fd072621a4aa2cef84613586c3ec3f76c7a0871&X-Amz-SignedHeaders=host&x-id=GetObject)
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
