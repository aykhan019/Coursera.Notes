

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAPKKDMF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIFvfgarRTbf4DcbUtaL1iafthyymjqnxv9NPhoOpfqy%2FAiBF3KYjpvr9JxFahx8Yb%2FbvF%2BCCY%2Fv%2BoJv9uRUIzpFUhyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMurJlv9xdRy2MUyE%2FKtwDAnHm9WqjZZD%2Fv1rIvNHqUPpW1FkzX4GtU4VOafz7cFr8YujK2h4aFbBFWAVC5VnduWTNb9k%2BkyoHdIsWSVmcedFSHLOgSFL4%2F1enQWuw9bwStsC7K7Xh3XAAZlRnJ7i9r%2Bv%2FupkBuf%2FWaKAc4sqjKp%2BErLRCz5FEvrpxqlPp1npFY0HVoqSTD5lYDqeWC%2F3qChLT%2BU6100q0cFLmvMDxXMW73%2FHwEil4zSv9CgtPgRG9QP6CeS0gn6cnJlJQhDV7iANGJMjA1qqsG7hIX0lOmwXKXWzijeCByCZJqM6SSnhyX%2Fzas83ho5kD5KytIWzKRzY%2FNi7wCMcCSpW8fRh35Fw8chEIyTqeDMr93DmtpRCPLUUxJJg3MoFCxHAe2jjGcqqxRLYjZ5YDS40tSQSsmtnaj%2FwqgdmOT3X9HwnVF2aP0MZpFqP2zyU5kZEpMng%2FExer1OHO3l7mhX1bsMrd59JWQVRI3jBkUPbSiAHxJaLJnlgfbhSYd7QTeI8mSgevy9CIApRpNw7IqP3XsJVz7tjzRGQ52E%2BhXlaloKuP596k2mYooNHqEqVGQB59fkwa5uxah78lBrUH93pKKu5xLX85n23dISr1KWX0qd7TvdyR6hZrfHLTE6uL6VowprqOvQY6pgH4j%2FmvPBdpD8bvjFjnVwQudft%2F6063pS351LLxdEVCipe34oxyX%2BMA0EszRgsGPd%2BsarWOmCrVTtBw6DkSD96X6fOBgaV2HAcOVhfSLeagzTU%2Fn8s3JEgB1PvrDTigmFQv8F8obtSPOCVS6ToKr%2FsugvjrXMtTC0anxR%2BnNdMeupttIHlrDePvRaayEbXpj7aRT3hEn5PybvLCHrFa7XIrJyVFcBaE&X-Amz-Signature=b72c32342ae7715d63e2b91bc757cb4b2af8696b79fe600e99c81919ca43112f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAPKKDMF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIFvfgarRTbf4DcbUtaL1iafthyymjqnxv9NPhoOpfqy%2FAiBF3KYjpvr9JxFahx8Yb%2FbvF%2BCCY%2Fv%2BoJv9uRUIzpFUhyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMurJlv9xdRy2MUyE%2FKtwDAnHm9WqjZZD%2Fv1rIvNHqUPpW1FkzX4GtU4VOafz7cFr8YujK2h4aFbBFWAVC5VnduWTNb9k%2BkyoHdIsWSVmcedFSHLOgSFL4%2F1enQWuw9bwStsC7K7Xh3XAAZlRnJ7i9r%2Bv%2FupkBuf%2FWaKAc4sqjKp%2BErLRCz5FEvrpxqlPp1npFY0HVoqSTD5lYDqeWC%2F3qChLT%2BU6100q0cFLmvMDxXMW73%2FHwEil4zSv9CgtPgRG9QP6CeS0gn6cnJlJQhDV7iANGJMjA1qqsG7hIX0lOmwXKXWzijeCByCZJqM6SSnhyX%2Fzas83ho5kD5KytIWzKRzY%2FNi7wCMcCSpW8fRh35Fw8chEIyTqeDMr93DmtpRCPLUUxJJg3MoFCxHAe2jjGcqqxRLYjZ5YDS40tSQSsmtnaj%2FwqgdmOT3X9HwnVF2aP0MZpFqP2zyU5kZEpMng%2FExer1OHO3l7mhX1bsMrd59JWQVRI3jBkUPbSiAHxJaLJnlgfbhSYd7QTeI8mSgevy9CIApRpNw7IqP3XsJVz7tjzRGQ52E%2BhXlaloKuP596k2mYooNHqEqVGQB59fkwa5uxah78lBrUH93pKKu5xLX85n23dISr1KWX0qd7TvdyR6hZrfHLTE6uL6VowprqOvQY6pgH4j%2FmvPBdpD8bvjFjnVwQudft%2F6063pS351LLxdEVCipe34oxyX%2BMA0EszRgsGPd%2BsarWOmCrVTtBw6DkSD96X6fOBgaV2HAcOVhfSLeagzTU%2Fn8s3JEgB1PvrDTigmFQv8F8obtSPOCVS6ToKr%2FsugvjrXMtTC0anxR%2BnNdMeupttIHlrDePvRaayEbXpj7aRT3hEn5PybvLCHrFa7XIrJyVFcBaE&X-Amz-Signature=3a27e58b65da41b011c4ef9d78c4ce61f18551259c22c0c878fda2daaac668df&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAPKKDMF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIFvfgarRTbf4DcbUtaL1iafthyymjqnxv9NPhoOpfqy%2FAiBF3KYjpvr9JxFahx8Yb%2FbvF%2BCCY%2Fv%2BoJv9uRUIzpFUhyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMurJlv9xdRy2MUyE%2FKtwDAnHm9WqjZZD%2Fv1rIvNHqUPpW1FkzX4GtU4VOafz7cFr8YujK2h4aFbBFWAVC5VnduWTNb9k%2BkyoHdIsWSVmcedFSHLOgSFL4%2F1enQWuw9bwStsC7K7Xh3XAAZlRnJ7i9r%2Bv%2FupkBuf%2FWaKAc4sqjKp%2BErLRCz5FEvrpxqlPp1npFY0HVoqSTD5lYDqeWC%2F3qChLT%2BU6100q0cFLmvMDxXMW73%2FHwEil4zSv9CgtPgRG9QP6CeS0gn6cnJlJQhDV7iANGJMjA1qqsG7hIX0lOmwXKXWzijeCByCZJqM6SSnhyX%2Fzas83ho5kD5KytIWzKRzY%2FNi7wCMcCSpW8fRh35Fw8chEIyTqeDMr93DmtpRCPLUUxJJg3MoFCxHAe2jjGcqqxRLYjZ5YDS40tSQSsmtnaj%2FwqgdmOT3X9HwnVF2aP0MZpFqP2zyU5kZEpMng%2FExer1OHO3l7mhX1bsMrd59JWQVRI3jBkUPbSiAHxJaLJnlgfbhSYd7QTeI8mSgevy9CIApRpNw7IqP3XsJVz7tjzRGQ52E%2BhXlaloKuP596k2mYooNHqEqVGQB59fkwa5uxah78lBrUH93pKKu5xLX85n23dISr1KWX0qd7TvdyR6hZrfHLTE6uL6VowprqOvQY6pgH4j%2FmvPBdpD8bvjFjnVwQudft%2F6063pS351LLxdEVCipe34oxyX%2BMA0EszRgsGPd%2BsarWOmCrVTtBw6DkSD96X6fOBgaV2HAcOVhfSLeagzTU%2Fn8s3JEgB1PvrDTigmFQv8F8obtSPOCVS6ToKr%2FsugvjrXMtTC0anxR%2BnNdMeupttIHlrDePvRaayEbXpj7aRT3hEn5PybvLCHrFa7XIrJyVFcBaE&X-Amz-Signature=cc9beb5a6e019ca85fe9d969a988f9552c8ca7f500a88eae082661064d81f508&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAPKKDMF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIFvfgarRTbf4DcbUtaL1iafthyymjqnxv9NPhoOpfqy%2FAiBF3KYjpvr9JxFahx8Yb%2FbvF%2BCCY%2Fv%2BoJv9uRUIzpFUhyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMurJlv9xdRy2MUyE%2FKtwDAnHm9WqjZZD%2Fv1rIvNHqUPpW1FkzX4GtU4VOafz7cFr8YujK2h4aFbBFWAVC5VnduWTNb9k%2BkyoHdIsWSVmcedFSHLOgSFL4%2F1enQWuw9bwStsC7K7Xh3XAAZlRnJ7i9r%2Bv%2FupkBuf%2FWaKAc4sqjKp%2BErLRCz5FEvrpxqlPp1npFY0HVoqSTD5lYDqeWC%2F3qChLT%2BU6100q0cFLmvMDxXMW73%2FHwEil4zSv9CgtPgRG9QP6CeS0gn6cnJlJQhDV7iANGJMjA1qqsG7hIX0lOmwXKXWzijeCByCZJqM6SSnhyX%2Fzas83ho5kD5KytIWzKRzY%2FNi7wCMcCSpW8fRh35Fw8chEIyTqeDMr93DmtpRCPLUUxJJg3MoFCxHAe2jjGcqqxRLYjZ5YDS40tSQSsmtnaj%2FwqgdmOT3X9HwnVF2aP0MZpFqP2zyU5kZEpMng%2FExer1OHO3l7mhX1bsMrd59JWQVRI3jBkUPbSiAHxJaLJnlgfbhSYd7QTeI8mSgevy9CIApRpNw7IqP3XsJVz7tjzRGQ52E%2BhXlaloKuP596k2mYooNHqEqVGQB59fkwa5uxah78lBrUH93pKKu5xLX85n23dISr1KWX0qd7TvdyR6hZrfHLTE6uL6VowprqOvQY6pgH4j%2FmvPBdpD8bvjFjnVwQudft%2F6063pS351LLxdEVCipe34oxyX%2BMA0EszRgsGPd%2BsarWOmCrVTtBw6DkSD96X6fOBgaV2HAcOVhfSLeagzTU%2Fn8s3JEgB1PvrDTigmFQv8F8obtSPOCVS6ToKr%2FsugvjrXMtTC0anxR%2BnNdMeupttIHlrDePvRaayEbXpj7aRT3hEn5PybvLCHrFa7XIrJyVFcBaE&X-Amz-Signature=97beb6f4eb8a4f6ae29a9f521706386f589afd3d7357fc9f93a4e067d567f3a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAPKKDMF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIFvfgarRTbf4DcbUtaL1iafthyymjqnxv9NPhoOpfqy%2FAiBF3KYjpvr9JxFahx8Yb%2FbvF%2BCCY%2Fv%2BoJv9uRUIzpFUhyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMurJlv9xdRy2MUyE%2FKtwDAnHm9WqjZZD%2Fv1rIvNHqUPpW1FkzX4GtU4VOafz7cFr8YujK2h4aFbBFWAVC5VnduWTNb9k%2BkyoHdIsWSVmcedFSHLOgSFL4%2F1enQWuw9bwStsC7K7Xh3XAAZlRnJ7i9r%2Bv%2FupkBuf%2FWaKAc4sqjKp%2BErLRCz5FEvrpxqlPp1npFY0HVoqSTD5lYDqeWC%2F3qChLT%2BU6100q0cFLmvMDxXMW73%2FHwEil4zSv9CgtPgRG9QP6CeS0gn6cnJlJQhDV7iANGJMjA1qqsG7hIX0lOmwXKXWzijeCByCZJqM6SSnhyX%2Fzas83ho5kD5KytIWzKRzY%2FNi7wCMcCSpW8fRh35Fw8chEIyTqeDMr93DmtpRCPLUUxJJg3MoFCxHAe2jjGcqqxRLYjZ5YDS40tSQSsmtnaj%2FwqgdmOT3X9HwnVF2aP0MZpFqP2zyU5kZEpMng%2FExer1OHO3l7mhX1bsMrd59JWQVRI3jBkUPbSiAHxJaLJnlgfbhSYd7QTeI8mSgevy9CIApRpNw7IqP3XsJVz7tjzRGQ52E%2BhXlaloKuP596k2mYooNHqEqVGQB59fkwa5uxah78lBrUH93pKKu5xLX85n23dISr1KWX0qd7TvdyR6hZrfHLTE6uL6VowprqOvQY6pgH4j%2FmvPBdpD8bvjFjnVwQudft%2F6063pS351LLxdEVCipe34oxyX%2BMA0EszRgsGPd%2BsarWOmCrVTtBw6DkSD96X6fOBgaV2HAcOVhfSLeagzTU%2Fn8s3JEgB1PvrDTigmFQv8F8obtSPOCVS6ToKr%2FsugvjrXMtTC0anxR%2BnNdMeupttIHlrDePvRaayEbXpj7aRT3hEn5PybvLCHrFa7XIrJyVFcBaE&X-Amz-Signature=e062065a82e93cec5407f978c57f1ef022b6f6219f7356b2eaabf957a6687c38&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAPKKDMF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIFvfgarRTbf4DcbUtaL1iafthyymjqnxv9NPhoOpfqy%2FAiBF3KYjpvr9JxFahx8Yb%2FbvF%2BCCY%2Fv%2BoJv9uRUIzpFUhyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMurJlv9xdRy2MUyE%2FKtwDAnHm9WqjZZD%2Fv1rIvNHqUPpW1FkzX4GtU4VOafz7cFr8YujK2h4aFbBFWAVC5VnduWTNb9k%2BkyoHdIsWSVmcedFSHLOgSFL4%2F1enQWuw9bwStsC7K7Xh3XAAZlRnJ7i9r%2Bv%2FupkBuf%2FWaKAc4sqjKp%2BErLRCz5FEvrpxqlPp1npFY0HVoqSTD5lYDqeWC%2F3qChLT%2BU6100q0cFLmvMDxXMW73%2FHwEil4zSv9CgtPgRG9QP6CeS0gn6cnJlJQhDV7iANGJMjA1qqsG7hIX0lOmwXKXWzijeCByCZJqM6SSnhyX%2Fzas83ho5kD5KytIWzKRzY%2FNi7wCMcCSpW8fRh35Fw8chEIyTqeDMr93DmtpRCPLUUxJJg3MoFCxHAe2jjGcqqxRLYjZ5YDS40tSQSsmtnaj%2FwqgdmOT3X9HwnVF2aP0MZpFqP2zyU5kZEpMng%2FExer1OHO3l7mhX1bsMrd59JWQVRI3jBkUPbSiAHxJaLJnlgfbhSYd7QTeI8mSgevy9CIApRpNw7IqP3XsJVz7tjzRGQ52E%2BhXlaloKuP596k2mYooNHqEqVGQB59fkwa5uxah78lBrUH93pKKu5xLX85n23dISr1KWX0qd7TvdyR6hZrfHLTE6uL6VowprqOvQY6pgH4j%2FmvPBdpD8bvjFjnVwQudft%2F6063pS351LLxdEVCipe34oxyX%2BMA0EszRgsGPd%2BsarWOmCrVTtBw6DkSD96X6fOBgaV2HAcOVhfSLeagzTU%2Fn8s3JEgB1PvrDTigmFQv8F8obtSPOCVS6ToKr%2FsugvjrXMtTC0anxR%2BnNdMeupttIHlrDePvRaayEbXpj7aRT3hEn5PybvLCHrFa7XIrJyVFcBaE&X-Amz-Signature=3a78c7f33fef6bbd68285dc9d2938ba2cc77d5bef4ed90eef00cd8ace6ff6f95&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAPKKDMF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIFvfgarRTbf4DcbUtaL1iafthyymjqnxv9NPhoOpfqy%2FAiBF3KYjpvr9JxFahx8Yb%2FbvF%2BCCY%2Fv%2BoJv9uRUIzpFUhyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMurJlv9xdRy2MUyE%2FKtwDAnHm9WqjZZD%2Fv1rIvNHqUPpW1FkzX4GtU4VOafz7cFr8YujK2h4aFbBFWAVC5VnduWTNb9k%2BkyoHdIsWSVmcedFSHLOgSFL4%2F1enQWuw9bwStsC7K7Xh3XAAZlRnJ7i9r%2Bv%2FupkBuf%2FWaKAc4sqjKp%2BErLRCz5FEvrpxqlPp1npFY0HVoqSTD5lYDqeWC%2F3qChLT%2BU6100q0cFLmvMDxXMW73%2FHwEil4zSv9CgtPgRG9QP6CeS0gn6cnJlJQhDV7iANGJMjA1qqsG7hIX0lOmwXKXWzijeCByCZJqM6SSnhyX%2Fzas83ho5kD5KytIWzKRzY%2FNi7wCMcCSpW8fRh35Fw8chEIyTqeDMr93DmtpRCPLUUxJJg3MoFCxHAe2jjGcqqxRLYjZ5YDS40tSQSsmtnaj%2FwqgdmOT3X9HwnVF2aP0MZpFqP2zyU5kZEpMng%2FExer1OHO3l7mhX1bsMrd59JWQVRI3jBkUPbSiAHxJaLJnlgfbhSYd7QTeI8mSgevy9CIApRpNw7IqP3XsJVz7tjzRGQ52E%2BhXlaloKuP596k2mYooNHqEqVGQB59fkwa5uxah78lBrUH93pKKu5xLX85n23dISr1KWX0qd7TvdyR6hZrfHLTE6uL6VowprqOvQY6pgH4j%2FmvPBdpD8bvjFjnVwQudft%2F6063pS351LLxdEVCipe34oxyX%2BMA0EszRgsGPd%2BsarWOmCrVTtBw6DkSD96X6fOBgaV2HAcOVhfSLeagzTU%2Fn8s3JEgB1PvrDTigmFQv8F8obtSPOCVS6ToKr%2FsugvjrXMtTC0anxR%2BnNdMeupttIHlrDePvRaayEbXpj7aRT3hEn5PybvLCHrFa7XIrJyVFcBaE&X-Amz-Signature=8947c1ba0ad1bf649f132549489541d1a62f44a12cd181c261bc546378b315a2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAPKKDMF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIFvfgarRTbf4DcbUtaL1iafthyymjqnxv9NPhoOpfqy%2FAiBF3KYjpvr9JxFahx8Yb%2FbvF%2BCCY%2Fv%2BoJv9uRUIzpFUhyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMurJlv9xdRy2MUyE%2FKtwDAnHm9WqjZZD%2Fv1rIvNHqUPpW1FkzX4GtU4VOafz7cFr8YujK2h4aFbBFWAVC5VnduWTNb9k%2BkyoHdIsWSVmcedFSHLOgSFL4%2F1enQWuw9bwStsC7K7Xh3XAAZlRnJ7i9r%2Bv%2FupkBuf%2FWaKAc4sqjKp%2BErLRCz5FEvrpxqlPp1npFY0HVoqSTD5lYDqeWC%2F3qChLT%2BU6100q0cFLmvMDxXMW73%2FHwEil4zSv9CgtPgRG9QP6CeS0gn6cnJlJQhDV7iANGJMjA1qqsG7hIX0lOmwXKXWzijeCByCZJqM6SSnhyX%2Fzas83ho5kD5KytIWzKRzY%2FNi7wCMcCSpW8fRh35Fw8chEIyTqeDMr93DmtpRCPLUUxJJg3MoFCxHAe2jjGcqqxRLYjZ5YDS40tSQSsmtnaj%2FwqgdmOT3X9HwnVF2aP0MZpFqP2zyU5kZEpMng%2FExer1OHO3l7mhX1bsMrd59JWQVRI3jBkUPbSiAHxJaLJnlgfbhSYd7QTeI8mSgevy9CIApRpNw7IqP3XsJVz7tjzRGQ52E%2BhXlaloKuP596k2mYooNHqEqVGQB59fkwa5uxah78lBrUH93pKKu5xLX85n23dISr1KWX0qd7TvdyR6hZrfHLTE6uL6VowprqOvQY6pgH4j%2FmvPBdpD8bvjFjnVwQudft%2F6063pS351LLxdEVCipe34oxyX%2BMA0EszRgsGPd%2BsarWOmCrVTtBw6DkSD96X6fOBgaV2HAcOVhfSLeagzTU%2Fn8s3JEgB1PvrDTigmFQv8F8obtSPOCVS6ToKr%2FsugvjrXMtTC0anxR%2BnNdMeupttIHlrDePvRaayEbXpj7aRT3hEn5PybvLCHrFa7XIrJyVFcBaE&X-Amz-Signature=fb95b1eaa963a3ae8e1876442f4758583ca187343a820b957c7b9346281dc8a1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZ7CGLYN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIH%2ByX86K2SyhA19VtaWbjL1FPUo3TS65jBS%2F4yv2M3eEAiEAzFUICsEx9Oe%2F4FvEaNG5WBuLOdLFKV3OFy7xiSVysygq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAQ6mQtXpem7gLOlxSrcAx5yLd%2FHxoKCdWBeLVq75YeUGaJWKfmLnuDR51WQPzejK8%2FPQD22Ph6S9VFQAVtbqmUJSQl5cxHULGAuP%2FmKW5%2FH7zmk8aBQX3sozF89XB8UBuzZxajUO0nJkAQAHyXS2IQZ7co%2BXyPXb%2F1nbZ0yQWSJSSrF9w%2FaaDidupJ1bsc64psdWTmxKe1g6BaZSWAVIp5c6GlX%2By8SxYESIu1WNIibahvapgoeCzVWi6q6H3NPINkm%2BQYxg3ptLspzGQ338WGZRJnPcWj%2BFrwRGiB7S%2Fz4tgtqvgK8eYhQRox37nPFyZfFDRifSTE7uHBDS5aBm8TNP71yFD6fE77vVPvLEjCvhJ6Blr5Q3icv4QwGvT2%2BW7SrfYru3aCce1nIdJwMAnGl%2B34fDlKy%2B7I5pjLBMxDvPqFEwURdAV5E%2Fb7xjFJ2iVdcZdiXQFPZoNBJZy%2Bz1ji5uGe5QAhai%2F4pNTP2VxNyHZKaTJs6Y00dbzdq%2By7qutsJTYrIFGIu53xqHRQBs2un5%2FzpHhhdvRbezL65A%2FGjBVegjLHSB%2Bg9g3OollB2CK88AKZClz7maUHLCObQn91pFR7XiLeuROSAUGqGWU5B6d2Vtm6QBJTtGZqKoaLXFw85odf5NiEz9XTMMIm8jr0GOqUBHceNe92KqhP12SZjwWIONRubamzY4djscBJDNCZbN17QL%2Bl663YN3hgH%2B2HRlFh5JoFXFODacUFO7HMfegO3BZ5IuoR%2BXZDbLI8G%2BoqboRmOmXGiQRqtGdAiLt%2FDFH8PwnXT5oLH5vghsQyi%2BQUNNjtdjzR4RPlrx6XXXQ%2FJhrTjXolamwFzz%2FXCgQ4EenmW9nq4ppkjTdOZJBWzLwx2acsnKofE&X-Amz-Signature=82300696e2beaf3d1307b407ab9a374a6e41f37787fd95da457331ee535f2ee0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT2E3HIL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIDxT5QmuSiv5%2Fw4qvau5PQ8Wc3L0k6yT5f1ad%2Fq7JhNwAiEAp9Cf2x6VdH%2FcEfLFSEEoPluFbdm3sQ8loBunw6STAEgq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDMbxUZ1%2FijYsHtaOUyrcAwGmMosIR27ewBuvCTFG9G%2BXCzXhTQr3IbLD6KJFVvh%2BaTAf3%2B%2BDH1n1HzXV0YULS00mQn5xE14fyeu2ythBftvdHjsQiWnU%2FJnp8OBhp64YjHdWtA%2BVDqGYq%2BteSCcKxA3pn061W%2BK0jbIFuOvFX0rV2JYpLgHOc3ojNi8%2Bf%2B5BVkhkn6LRCzG0tpTW6ip2vWso%2F%2B6RRHkRq4QNcpbiLT8zborycZSMHC%2BanSqvinOpc7CObzwh%2FGSTb8YQja9Ph9ZUxf1HxxztIP5OEo2qT7KmWAiXdymoSIo%2F3LFniKjDuc8V4CFoVcThBmjesePTDpfMh5VeWsuy6lStk2C8arQ27pAoIKLKqBedcsmngILditCbkha0zXe2ubWmrPCugS6FXj1AepFVRxx%2BJrvSAssucBA6OBrpR6z5eTk11SbV14%2BBxRS%2Ffj91Rru93tmin%2BULaVWtdwsuBdTrLny4Iwd8atzHudZTz60TtKafL6k1pa5ERgJRUnTQYl%2FogHjUNdThGZZVjnlss2FPJeyLW03u4SeL6mca4HAxN35yN%2B8lA%2FIf28nTDPgXxnVDTX8zJppGNWbl4tWZPmm6MkhhLGRVLxdUjHKBP0dwNe479xfMgfNpEDTFdylmecszMIq8jr0GOqUBmInd9QXDqZhNu48fd9ILbpywSMeHZNNNzYjfQLXQ3Y1mvM5Pqq63OX2sy8uJ3JmdoNg41YMQgyTicsnjs9mwPcJRt2D5fP0EE6JxlOo2fi%2FdYuCJlelMts3pCpqL%2FAxx1acWbxmHAntw%2FWRV6Ul9A4B60TalQzjcofpacrV5gVVfcduwFl8cpYdmdB17ydtHHtJsInx9J06Q2vw4Tc0S63jpJhyL&X-Amz-Signature=da67e535b5ea58723c4d5a4699b0ca8c7eec0d47963755e46a66b61b36fc7138&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZQOKYDA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIEJ%2FOj%2FmKT2R4Gs%2F30NPGjfESoxJKXa0BWhbbY6PYHG8AiEAhCyxm2XA%2BnTUPSgHVraHgD1mAqrC8fPDq87Bz2zNgCQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHPYzwwWBKoK%2F%2B5MlSrcA6fSJWY13vmzgSgM0AJBDaVzFxcbfufydWD2y0NQUbTrN%2BCKeRs8wQ%2BS0UiSBEpCXDowi7rPtoqvubDuVVkAk7cZPjjW1jaEGBxP1DfDe1BiIIvnhbmFvEd8dPGeMmtKED2FbveUAJRP6rDsgtJqLW0j6uft29aRpPyEgLFOl4UAOJeOLsMhHdJsF%2B13chhRNWhqUvCz2gFgjGV%2BIjReUNO%2FIsU8Ilzc%2F4wo36E9KyH0vvadT7Ho%2Bf%2F0omhjKBb7d3FXvLOU4MHI7MPGOu4U3qXVE5qCU51BO9ebdDgeyYX1YeHtaY8t6ZQKW%2FzbmOFB6857tC8uUHFQt45rxv9z8mirVY5cI0s2NWVOSwvJzP8gbd%2BfKDr0pehG30ZP4uSVhKflSSAHjaSXlOZrZdLqbnwev%2FxH9HdfvF2wg%2BuwCgapIuh7u9F%2F6wUsk0eKnsj%2BbxlaanhCUMq3zEDQVarN0h6nRa61VzeXzpYfTitda4RlS77be5JSkS%2FHULjn2NYGJElzm%2FZxwxcfwArI8zO0jBC5O2a3pgXG3BsVaRDAa5uBy3r79yyu%2B7MCLfA7rooF%2BH1A%2FMU2C6QA8uwjri5llIHSq7qiUrRXxamUiYUoPMdnzI1hhQai0C3q8RGzMPO6jr0GOqUBt7pMD8IMrfh%2BzVOMKpaht%2F4cE5OJbBbsYrkynemDcY5U58YLsqMm29yFnl2cNQ0VlM6ikaTYUNyfRQ2IyPAxYU%2F8MrTVbWSzpydSXdfeWWyJ4VOCJ0N%2FsMMwEa8vKzyKqL9QvjbMN%2F4dpvirJW%2FSgnvgvSKsLhkBwL1sgAiZv1K1wevrxD5Axe7BswqiA9qQODHUKmI%2For6raa1QOELnCuTN7HXi&X-Amz-Signature=111063a52d5476166b729991f90e9225ee5b7c92b93a876c58f2c5ee8f6f8af2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZQOKYDA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIEJ%2FOj%2FmKT2R4Gs%2F30NPGjfESoxJKXa0BWhbbY6PYHG8AiEAhCyxm2XA%2BnTUPSgHVraHgD1mAqrC8fPDq87Bz2zNgCQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHPYzwwWBKoK%2F%2B5MlSrcA6fSJWY13vmzgSgM0AJBDaVzFxcbfufydWD2y0NQUbTrN%2BCKeRs8wQ%2BS0UiSBEpCXDowi7rPtoqvubDuVVkAk7cZPjjW1jaEGBxP1DfDe1BiIIvnhbmFvEd8dPGeMmtKED2FbveUAJRP6rDsgtJqLW0j6uft29aRpPyEgLFOl4UAOJeOLsMhHdJsF%2B13chhRNWhqUvCz2gFgjGV%2BIjReUNO%2FIsU8Ilzc%2F4wo36E9KyH0vvadT7Ho%2Bf%2F0omhjKBb7d3FXvLOU4MHI7MPGOu4U3qXVE5qCU51BO9ebdDgeyYX1YeHtaY8t6ZQKW%2FzbmOFB6857tC8uUHFQt45rxv9z8mirVY5cI0s2NWVOSwvJzP8gbd%2BfKDr0pehG30ZP4uSVhKflSSAHjaSXlOZrZdLqbnwev%2FxH9HdfvF2wg%2BuwCgapIuh7u9F%2F6wUsk0eKnsj%2BbxlaanhCUMq3zEDQVarN0h6nRa61VzeXzpYfTitda4RlS77be5JSkS%2FHULjn2NYGJElzm%2FZxwxcfwArI8zO0jBC5O2a3pgXG3BsVaRDAa5uBy3r79yyu%2B7MCLfA7rooF%2BH1A%2FMU2C6QA8uwjri5llIHSq7qiUrRXxamUiYUoPMdnzI1hhQai0C3q8RGzMPO6jr0GOqUBt7pMD8IMrfh%2BzVOMKpaht%2F4cE5OJbBbsYrkynemDcY5U58YLsqMm29yFnl2cNQ0VlM6ikaTYUNyfRQ2IyPAxYU%2F8MrTVbWSzpydSXdfeWWyJ4VOCJ0N%2FsMMwEa8vKzyKqL9QvjbMN%2F4dpvirJW%2FSgnvgvSKsLhkBwL1sgAiZv1K1wevrxD5Axe7BswqiA9qQODHUKmI%2For6raa1QOELnCuTN7HXi&X-Amz-Signature=9f2279266e5d7817ec2caf4ecc6654fe42b34806ae0348cf072f05ca2ecc37a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
