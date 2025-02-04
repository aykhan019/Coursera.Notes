

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EOIT2UK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDs0npmj49dOS9Y7nj105Zi6s1ykuQk0s%2FnNNmAE56AjAIhAIFAkslg9QsTH4HlNFvuKynPyTNwOy4b%2FWt5%2Fs3fWc4RKv8DCDcQABoMNjM3NDIzMTgzODA1IgxL6W3zcbypK1Rp1qoq3AONM8hyvqAJPiiBsOCROCkmDBJmk%2FHfm%2BgW5zNpTA572DrxplgPB%2FHd28n0NFe5eg6uVYEopFErl3%2BmWaSknaD%2BnHeGuemKE5feeYQ62youhUP1YwqxjP2Q2W9Lco01uEhvwNLtobhgrFeQWaC806CQnaN6uSozv%2B92s3yrV1lFQxE5znizeUJWC1sNVtFM5QNi9ao%2FKI2kQ%2BNAXtc67Nd0NDG6m%2FnFw1yZI5sFqog9n5DPvd2fAqxkyH9mTnO5VRazsW7ojyvKbtHnFf1ePLjZDpAtLBGcF2zbSLN6Brd0%2FqYA7LCqaQxa8vTDKRil2Kwz4JdK9u7MBriSEYL8tpbwRnhXw%2BSRjjAUW5quYVTWbk2nl0yxgAtQYWyWoCNfWO64Gy3xHdapui%2BY7J8kYpMh49Zn%2Bh30LFbQ2FohbynCJl%2FhnBwZ61a5GrUapgZBkwo2EVEOb99wJiZirrm1QNy21%2BUbvO4Bcee2xslI%2BJQfvCqUQLfMGE5hx4ciYKa4d7c%2F8VjeBxIt5bZI7iidfh5wRHHoMN%2FUOx%2BkgcnzrBnLxhqbGc5vkK0smF1t%2BgmZOVCwcysCp7Pwl4YYoOyRwwfEKM44nTAAS1nJEVuill3c8qikZg6j2vrvd6h%2FCjCmlIq9BjqkAVxx%2BiaC2aO5Qy33g2%2B4bUDdsoL0CBzumiZizwsVy7Ylmo%2FxNJKsDVaQAxxtyERmUwyKca%2BDIcmekBOe8l2kKnzwFyARVvvLKwkN7Lx8Rulk0fnVpqVh2jDOQzgN68ajFahbj5rDn08OcmNEL2SVa00MTFF494L11rrR4h2DnIVC%2FzWA68%2BYU%2FyTSrOHJ0KOyVqM9Rh3XLvIag4Cz0OQPpAy5ZXU&X-Amz-Signature=b18523db0e113ac10ef1f3e67094ca517cc8913465f5531505123fe9fe9ec83e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EOIT2UK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDs0npmj49dOS9Y7nj105Zi6s1ykuQk0s%2FnNNmAE56AjAIhAIFAkslg9QsTH4HlNFvuKynPyTNwOy4b%2FWt5%2Fs3fWc4RKv8DCDcQABoMNjM3NDIzMTgzODA1IgxL6W3zcbypK1Rp1qoq3AONM8hyvqAJPiiBsOCROCkmDBJmk%2FHfm%2BgW5zNpTA572DrxplgPB%2FHd28n0NFe5eg6uVYEopFErl3%2BmWaSknaD%2BnHeGuemKE5feeYQ62youhUP1YwqxjP2Q2W9Lco01uEhvwNLtobhgrFeQWaC806CQnaN6uSozv%2B92s3yrV1lFQxE5znizeUJWC1sNVtFM5QNi9ao%2FKI2kQ%2BNAXtc67Nd0NDG6m%2FnFw1yZI5sFqog9n5DPvd2fAqxkyH9mTnO5VRazsW7ojyvKbtHnFf1ePLjZDpAtLBGcF2zbSLN6Brd0%2FqYA7LCqaQxa8vTDKRil2Kwz4JdK9u7MBriSEYL8tpbwRnhXw%2BSRjjAUW5quYVTWbk2nl0yxgAtQYWyWoCNfWO64Gy3xHdapui%2BY7J8kYpMh49Zn%2Bh30LFbQ2FohbynCJl%2FhnBwZ61a5GrUapgZBkwo2EVEOb99wJiZirrm1QNy21%2BUbvO4Bcee2xslI%2BJQfvCqUQLfMGE5hx4ciYKa4d7c%2F8VjeBxIt5bZI7iidfh5wRHHoMN%2FUOx%2BkgcnzrBnLxhqbGc5vkK0smF1t%2BgmZOVCwcysCp7Pwl4YYoOyRwwfEKM44nTAAS1nJEVuill3c8qikZg6j2vrvd6h%2FCjCmlIq9BjqkAVxx%2BiaC2aO5Qy33g2%2B4bUDdsoL0CBzumiZizwsVy7Ylmo%2FxNJKsDVaQAxxtyERmUwyKca%2BDIcmekBOe8l2kKnzwFyARVvvLKwkN7Lx8Rulk0fnVpqVh2jDOQzgN68ajFahbj5rDn08OcmNEL2SVa00MTFF494L11rrR4h2DnIVC%2FzWA68%2BYU%2FyTSrOHJ0KOyVqM9Rh3XLvIag4Cz0OQPpAy5ZXU&X-Amz-Signature=50455bc593a378dd0e12a4b6072a44e17a0ac7b279918c7a1d13b8e42e5d19e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EOIT2UK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDs0npmj49dOS9Y7nj105Zi6s1ykuQk0s%2FnNNmAE56AjAIhAIFAkslg9QsTH4HlNFvuKynPyTNwOy4b%2FWt5%2Fs3fWc4RKv8DCDcQABoMNjM3NDIzMTgzODA1IgxL6W3zcbypK1Rp1qoq3AONM8hyvqAJPiiBsOCROCkmDBJmk%2FHfm%2BgW5zNpTA572DrxplgPB%2FHd28n0NFe5eg6uVYEopFErl3%2BmWaSknaD%2BnHeGuemKE5feeYQ62youhUP1YwqxjP2Q2W9Lco01uEhvwNLtobhgrFeQWaC806CQnaN6uSozv%2B92s3yrV1lFQxE5znizeUJWC1sNVtFM5QNi9ao%2FKI2kQ%2BNAXtc67Nd0NDG6m%2FnFw1yZI5sFqog9n5DPvd2fAqxkyH9mTnO5VRazsW7ojyvKbtHnFf1ePLjZDpAtLBGcF2zbSLN6Brd0%2FqYA7LCqaQxa8vTDKRil2Kwz4JdK9u7MBriSEYL8tpbwRnhXw%2BSRjjAUW5quYVTWbk2nl0yxgAtQYWyWoCNfWO64Gy3xHdapui%2BY7J8kYpMh49Zn%2Bh30LFbQ2FohbynCJl%2FhnBwZ61a5GrUapgZBkwo2EVEOb99wJiZirrm1QNy21%2BUbvO4Bcee2xslI%2BJQfvCqUQLfMGE5hx4ciYKa4d7c%2F8VjeBxIt5bZI7iidfh5wRHHoMN%2FUOx%2BkgcnzrBnLxhqbGc5vkK0smF1t%2BgmZOVCwcysCp7Pwl4YYoOyRwwfEKM44nTAAS1nJEVuill3c8qikZg6j2vrvd6h%2FCjCmlIq9BjqkAVxx%2BiaC2aO5Qy33g2%2B4bUDdsoL0CBzumiZizwsVy7Ylmo%2FxNJKsDVaQAxxtyERmUwyKca%2BDIcmekBOe8l2kKnzwFyARVvvLKwkN7Lx8Rulk0fnVpqVh2jDOQzgN68ajFahbj5rDn08OcmNEL2SVa00MTFF494L11rrR4h2DnIVC%2FzWA68%2BYU%2FyTSrOHJ0KOyVqM9Rh3XLvIag4Cz0OQPpAy5ZXU&X-Amz-Signature=626150f1b3d09e69b7bf218b98a6cd8ef281944d927091a626e5d58a74a7ff9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EOIT2UK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDs0npmj49dOS9Y7nj105Zi6s1ykuQk0s%2FnNNmAE56AjAIhAIFAkslg9QsTH4HlNFvuKynPyTNwOy4b%2FWt5%2Fs3fWc4RKv8DCDcQABoMNjM3NDIzMTgzODA1IgxL6W3zcbypK1Rp1qoq3AONM8hyvqAJPiiBsOCROCkmDBJmk%2FHfm%2BgW5zNpTA572DrxplgPB%2FHd28n0NFe5eg6uVYEopFErl3%2BmWaSknaD%2BnHeGuemKE5feeYQ62youhUP1YwqxjP2Q2W9Lco01uEhvwNLtobhgrFeQWaC806CQnaN6uSozv%2B92s3yrV1lFQxE5znizeUJWC1sNVtFM5QNi9ao%2FKI2kQ%2BNAXtc67Nd0NDG6m%2FnFw1yZI5sFqog9n5DPvd2fAqxkyH9mTnO5VRazsW7ojyvKbtHnFf1ePLjZDpAtLBGcF2zbSLN6Brd0%2FqYA7LCqaQxa8vTDKRil2Kwz4JdK9u7MBriSEYL8tpbwRnhXw%2BSRjjAUW5quYVTWbk2nl0yxgAtQYWyWoCNfWO64Gy3xHdapui%2BY7J8kYpMh49Zn%2Bh30LFbQ2FohbynCJl%2FhnBwZ61a5GrUapgZBkwo2EVEOb99wJiZirrm1QNy21%2BUbvO4Bcee2xslI%2BJQfvCqUQLfMGE5hx4ciYKa4d7c%2F8VjeBxIt5bZI7iidfh5wRHHoMN%2FUOx%2BkgcnzrBnLxhqbGc5vkK0smF1t%2BgmZOVCwcysCp7Pwl4YYoOyRwwfEKM44nTAAS1nJEVuill3c8qikZg6j2vrvd6h%2FCjCmlIq9BjqkAVxx%2BiaC2aO5Qy33g2%2B4bUDdsoL0CBzumiZizwsVy7Ylmo%2FxNJKsDVaQAxxtyERmUwyKca%2BDIcmekBOe8l2kKnzwFyARVvvLKwkN7Lx8Rulk0fnVpqVh2jDOQzgN68ajFahbj5rDn08OcmNEL2SVa00MTFF494L11rrR4h2DnIVC%2FzWA68%2BYU%2FyTSrOHJ0KOyVqM9Rh3XLvIag4Cz0OQPpAy5ZXU&X-Amz-Signature=046bc873079fff42b629de945b1f58b8811e46934eba0e7493b5ea841dee7a7d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EOIT2UK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDs0npmj49dOS9Y7nj105Zi6s1ykuQk0s%2FnNNmAE56AjAIhAIFAkslg9QsTH4HlNFvuKynPyTNwOy4b%2FWt5%2Fs3fWc4RKv8DCDcQABoMNjM3NDIzMTgzODA1IgxL6W3zcbypK1Rp1qoq3AONM8hyvqAJPiiBsOCROCkmDBJmk%2FHfm%2BgW5zNpTA572DrxplgPB%2FHd28n0NFe5eg6uVYEopFErl3%2BmWaSknaD%2BnHeGuemKE5feeYQ62youhUP1YwqxjP2Q2W9Lco01uEhvwNLtobhgrFeQWaC806CQnaN6uSozv%2B92s3yrV1lFQxE5znizeUJWC1sNVtFM5QNi9ao%2FKI2kQ%2BNAXtc67Nd0NDG6m%2FnFw1yZI5sFqog9n5DPvd2fAqxkyH9mTnO5VRazsW7ojyvKbtHnFf1ePLjZDpAtLBGcF2zbSLN6Brd0%2FqYA7LCqaQxa8vTDKRil2Kwz4JdK9u7MBriSEYL8tpbwRnhXw%2BSRjjAUW5quYVTWbk2nl0yxgAtQYWyWoCNfWO64Gy3xHdapui%2BY7J8kYpMh49Zn%2Bh30LFbQ2FohbynCJl%2FhnBwZ61a5GrUapgZBkwo2EVEOb99wJiZirrm1QNy21%2BUbvO4Bcee2xslI%2BJQfvCqUQLfMGE5hx4ciYKa4d7c%2F8VjeBxIt5bZI7iidfh5wRHHoMN%2FUOx%2BkgcnzrBnLxhqbGc5vkK0smF1t%2BgmZOVCwcysCp7Pwl4YYoOyRwwfEKM44nTAAS1nJEVuill3c8qikZg6j2vrvd6h%2FCjCmlIq9BjqkAVxx%2BiaC2aO5Qy33g2%2B4bUDdsoL0CBzumiZizwsVy7Ylmo%2FxNJKsDVaQAxxtyERmUwyKca%2BDIcmekBOe8l2kKnzwFyARVvvLKwkN7Lx8Rulk0fnVpqVh2jDOQzgN68ajFahbj5rDn08OcmNEL2SVa00MTFF494L11rrR4h2DnIVC%2FzWA68%2BYU%2FyTSrOHJ0KOyVqM9Rh3XLvIag4Cz0OQPpAy5ZXU&X-Amz-Signature=64824423d78bda56c4a68467ed401e0e3484249e956c63544168df9209db8b26&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EOIT2UK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDs0npmj49dOS9Y7nj105Zi6s1ykuQk0s%2FnNNmAE56AjAIhAIFAkslg9QsTH4HlNFvuKynPyTNwOy4b%2FWt5%2Fs3fWc4RKv8DCDcQABoMNjM3NDIzMTgzODA1IgxL6W3zcbypK1Rp1qoq3AONM8hyvqAJPiiBsOCROCkmDBJmk%2FHfm%2BgW5zNpTA572DrxplgPB%2FHd28n0NFe5eg6uVYEopFErl3%2BmWaSknaD%2BnHeGuemKE5feeYQ62youhUP1YwqxjP2Q2W9Lco01uEhvwNLtobhgrFeQWaC806CQnaN6uSozv%2B92s3yrV1lFQxE5znizeUJWC1sNVtFM5QNi9ao%2FKI2kQ%2BNAXtc67Nd0NDG6m%2FnFw1yZI5sFqog9n5DPvd2fAqxkyH9mTnO5VRazsW7ojyvKbtHnFf1ePLjZDpAtLBGcF2zbSLN6Brd0%2FqYA7LCqaQxa8vTDKRil2Kwz4JdK9u7MBriSEYL8tpbwRnhXw%2BSRjjAUW5quYVTWbk2nl0yxgAtQYWyWoCNfWO64Gy3xHdapui%2BY7J8kYpMh49Zn%2Bh30LFbQ2FohbynCJl%2FhnBwZ61a5GrUapgZBkwo2EVEOb99wJiZirrm1QNy21%2BUbvO4Bcee2xslI%2BJQfvCqUQLfMGE5hx4ciYKa4d7c%2F8VjeBxIt5bZI7iidfh5wRHHoMN%2FUOx%2BkgcnzrBnLxhqbGc5vkK0smF1t%2BgmZOVCwcysCp7Pwl4YYoOyRwwfEKM44nTAAS1nJEVuill3c8qikZg6j2vrvd6h%2FCjCmlIq9BjqkAVxx%2BiaC2aO5Qy33g2%2B4bUDdsoL0CBzumiZizwsVy7Ylmo%2FxNJKsDVaQAxxtyERmUwyKca%2BDIcmekBOe8l2kKnzwFyARVvvLKwkN7Lx8Rulk0fnVpqVh2jDOQzgN68ajFahbj5rDn08OcmNEL2SVa00MTFF494L11rrR4h2DnIVC%2FzWA68%2BYU%2FyTSrOHJ0KOyVqM9Rh3XLvIag4Cz0OQPpAy5ZXU&X-Amz-Signature=fa1d902b472f4c91a89291520aa2cb210e4a0aa7963583e5c30ee1d5c1410cf6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EOIT2UK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDs0npmj49dOS9Y7nj105Zi6s1ykuQk0s%2FnNNmAE56AjAIhAIFAkslg9QsTH4HlNFvuKynPyTNwOy4b%2FWt5%2Fs3fWc4RKv8DCDcQABoMNjM3NDIzMTgzODA1IgxL6W3zcbypK1Rp1qoq3AONM8hyvqAJPiiBsOCROCkmDBJmk%2FHfm%2BgW5zNpTA572DrxplgPB%2FHd28n0NFe5eg6uVYEopFErl3%2BmWaSknaD%2BnHeGuemKE5feeYQ62youhUP1YwqxjP2Q2W9Lco01uEhvwNLtobhgrFeQWaC806CQnaN6uSozv%2B92s3yrV1lFQxE5znizeUJWC1sNVtFM5QNi9ao%2FKI2kQ%2BNAXtc67Nd0NDG6m%2FnFw1yZI5sFqog9n5DPvd2fAqxkyH9mTnO5VRazsW7ojyvKbtHnFf1ePLjZDpAtLBGcF2zbSLN6Brd0%2FqYA7LCqaQxa8vTDKRil2Kwz4JdK9u7MBriSEYL8tpbwRnhXw%2BSRjjAUW5quYVTWbk2nl0yxgAtQYWyWoCNfWO64Gy3xHdapui%2BY7J8kYpMh49Zn%2Bh30LFbQ2FohbynCJl%2FhnBwZ61a5GrUapgZBkwo2EVEOb99wJiZirrm1QNy21%2BUbvO4Bcee2xslI%2BJQfvCqUQLfMGE5hx4ciYKa4d7c%2F8VjeBxIt5bZI7iidfh5wRHHoMN%2FUOx%2BkgcnzrBnLxhqbGc5vkK0smF1t%2BgmZOVCwcysCp7Pwl4YYoOyRwwfEKM44nTAAS1nJEVuill3c8qikZg6j2vrvd6h%2FCjCmlIq9BjqkAVxx%2BiaC2aO5Qy33g2%2B4bUDdsoL0CBzumiZizwsVy7Ylmo%2FxNJKsDVaQAxxtyERmUwyKca%2BDIcmekBOe8l2kKnzwFyARVvvLKwkN7Lx8Rulk0fnVpqVh2jDOQzgN68ajFahbj5rDn08OcmNEL2SVa00MTFF494L11rrR4h2DnIVC%2FzWA68%2BYU%2FyTSrOHJ0KOyVqM9Rh3XLvIag4Cz0OQPpAy5ZXU&X-Amz-Signature=bbbaf9d7586d477f7367549c61b573e7a5826c4a611101922a3e9b564e62039c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EOIT2UK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDs0npmj49dOS9Y7nj105Zi6s1ykuQk0s%2FnNNmAE56AjAIhAIFAkslg9QsTH4HlNFvuKynPyTNwOy4b%2FWt5%2Fs3fWc4RKv8DCDcQABoMNjM3NDIzMTgzODA1IgxL6W3zcbypK1Rp1qoq3AONM8hyvqAJPiiBsOCROCkmDBJmk%2FHfm%2BgW5zNpTA572DrxplgPB%2FHd28n0NFe5eg6uVYEopFErl3%2BmWaSknaD%2BnHeGuemKE5feeYQ62youhUP1YwqxjP2Q2W9Lco01uEhvwNLtobhgrFeQWaC806CQnaN6uSozv%2B92s3yrV1lFQxE5znizeUJWC1sNVtFM5QNi9ao%2FKI2kQ%2BNAXtc67Nd0NDG6m%2FnFw1yZI5sFqog9n5DPvd2fAqxkyH9mTnO5VRazsW7ojyvKbtHnFf1ePLjZDpAtLBGcF2zbSLN6Brd0%2FqYA7LCqaQxa8vTDKRil2Kwz4JdK9u7MBriSEYL8tpbwRnhXw%2BSRjjAUW5quYVTWbk2nl0yxgAtQYWyWoCNfWO64Gy3xHdapui%2BY7J8kYpMh49Zn%2Bh30LFbQ2FohbynCJl%2FhnBwZ61a5GrUapgZBkwo2EVEOb99wJiZirrm1QNy21%2BUbvO4Bcee2xslI%2BJQfvCqUQLfMGE5hx4ciYKa4d7c%2F8VjeBxIt5bZI7iidfh5wRHHoMN%2FUOx%2BkgcnzrBnLxhqbGc5vkK0smF1t%2BgmZOVCwcysCp7Pwl4YYoOyRwwfEKM44nTAAS1nJEVuill3c8qikZg6j2vrvd6h%2FCjCmlIq9BjqkAVxx%2BiaC2aO5Qy33g2%2B4bUDdsoL0CBzumiZizwsVy7Ylmo%2FxNJKsDVaQAxxtyERmUwyKca%2BDIcmekBOe8l2kKnzwFyARVvvLKwkN7Lx8Rulk0fnVpqVh2jDOQzgN68ajFahbj5rDn08OcmNEL2SVa00MTFF494L11rrR4h2DnIVC%2FzWA68%2BYU%2FyTSrOHJ0KOyVqM9Rh3XLvIag4Cz0OQPpAy5ZXU&X-Amz-Signature=854944db43757ab3076daec65a806fa21e53d172d0c7a7f46d50d425f77998d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBPLS2FG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIHqDtsQD7NV4Z4Vwb%2FskJVdRzDW7252LaFpDV14leFhMAiEAhga3TnAvrpzQhmO3UVN58L9zXk2KxKZGDxJq2m%2FFzcMq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDCoKjjp7z4MtffQudircA6IODDy62%2FgiP9BfV%2Fv%2BQPFCgX1nLn5R6XPum%2FAEz%2FwVTWteKKN3oX5fVCdC3AfrsMOWUeCRDZ4NirURdyCf%2Fzzd21crcyOaQLQWro0RD7ZYgUhS9j8RoDRZjGVzcly2bVoOaw3lwDvQ3wlKSFXP%2FO7WO34XzxzYgoN9TFEfCfWZ8r4cNQiRBahqs9VPGG9VpTSXkqTyaUmqQaOpylbceBJfzeccF4Z8RzilvvloMlSSXO9hjRZh%2FhmKBWQgNcNCxD1zjs3Bpk3o%2FlIivGATfhAuky3cNACfZNFMNPeadxIWa%2F3ocCGU92KXK77GyUCQknpNEiJygHrO67n3huPAql%2BpfdnSMMkTlwxmP54gh5%2FYcSKs7eUqg8Vu0M1dbBLjXnQjzB8mWlqKHCdBunX%2BFCgmMhSXZd2zmdoK5IJVxmC36yc%2FhlTPrAw7h2%2FJnfniStOTh3%2FeK5fjQoOMONoApOHJV2wOJbliEThI7Y%2Fiqxl1hqwIh7FO90QoqJ1xNvY8NBkxpv5k7bevbGxoAo6oU49ZyF4s8R6haVUDa4P0wIVNsTTG%2FS7%2BOLrYnUHU1Tuk0XOBr0i8n7ae%2Bg6GcDseD%2BTBrKWK10FrPELQCXedT5hPbARBLBGZwUEhfLygMJ2Uir0GOqUBwHmDfgBSABipYXLHxS5eE%2BTKuvowlCIFUMuSw%2FIp3dHXptkqG4n2Quvu45vKl48e4DxGAZ2WruWt9v%2FbVkn3yHz6pwuuYR8NlJm9wE19R%2Bijuk2ehDMqCJAXYpcl2YtNKQDhq55DMXSJtQARxYfOAU2HOVxVo0muKL8K0ALFgD21fOpRJuFNMPm41eG%2FKncxtG%2BQQ2duwWAukTbIZ4IQ62srKq22&X-Amz-Signature=b67707f360ee4b853c2d4f0fc3f197684b21ffced5325ecd2cc19cfd6cf4fc0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD5WPRHP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQCUoMttFJb3DQbhjsq3zwnbPHOf4q%2BJV3X5n%2FYIz6VUBwIgMAwzR6Qzx9cmeNjCbr%2FVvkx79pFilVZEWGAVmHMHWRcq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDIifCqFV8kQKYjMmkCrcA3%2BpBZEdn8b4ok%2BilBAaOvqzAMvJGjrnLqT4NplNbMcoXOo8yA1D6yMoNjwmuE1KblufKaREGvekc1T3uAPz66tgcBkHexVhXCDThyZvLEP7OzFRqVyf1wBy7NFKXSzm0IcmNfXziLHR%2Bjf1ELCJXW6WS7oHMAhF2K%2Bw9kUGz4SR%2B6sHeLUdur4OeaiN0ARnmO8GSdUmZnGOu0ATi4bFFoj1I8K6TyypNUayPyj9PTg%2B7D2uQHAZO5oOGzVjaCemrRgBzvNlZCCyswDsUHfkJHx8at60OAB3LyRBWx%2Fv6iZV0gIxmuNw8uxc0NSTFX7mD6JxYMTaNJVXyTLfXtQj%2BPUfxRQQznxUQKmwmx%2F6XNxF%2BA4YKQFuQg3zxMgOj73ROfTLfmHfvM3rgXJviOhs6h0rR6HV%2Bmu3YivvDG3KbI5GoR8g78yJ8NNZwaQRQoT5Ooc%2B4aLSPXM0%2B2zApuSUuoZL%2B7XbqH23i6ZbYW9GTygkBjwc3llNQVOv11FTnpwc%2BjISlPz2CW6xSCuu35Gi6M%2BlAtOUXmyrlH2fLX5dwM1I1utpEPoqwTcgqFegL%2BuRANEvemWjO1tjbjh%2FfMGEH2DrMzlcBasR9bhTMJ9jHYnBn3C0UzOtE%2BtNBjPkMO%2BUir0GOqUBA3fpFB8AbkrOgCbAAAISFedPNnWQk9B%2FhkMutIy%2BvVk29ib10cEb%2Fe9VBLam0OII5IPGVBkH9VznN7edCOHvEtDwoVRhgh%2FltdB8HzpzxofmICO9m8FpvzzR9h%2B4BLn2reB5ndSEMaPPuKmuHeqovcVjz%2FpGl08fhEORe6CcLnh8Ms36heBZ5zBYY0VAqAw9wxpedflGc2yG2OPkEonFNFRu95GP&X-Amz-Signature=b86ee70cf7858483e780e2917457766367240da666c8846773809eabc3f4d6fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWJMTPXV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIE%2BNCNB0YuR%2BVuXYTcDo7%2FeFbmSMFDBW%2BKUXMK%2F0WqcOAiBFjJYPVECmLXtBVZCkrETcu50pU3sDSXwL868icl%2B21Cr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMWNwbvk6rX%2BK%2BUMO7KtwD6G%2BJZxOygwXyqIhjTYOkp2cQs%2BXXUGnRuHqlsWIOZbPtQX0CG5E6QNH8fQpvQbmn1W%2F5wrdllJPPRfWCHX5tpQz06Y4w23oPR6rGGvaDEfa1iXzXx7J9EkuQpfZ9khAawgFs%2FbZXBJ9RwEHe2B0kpcl96UU7w1mnZe2TWh1vAii1u2spQfdyDcOkJ321iNkmzpEWo7aMSA5lV52YykZFFzLikdK7KAf7kurTydwP7Ij%2BJpOUDHV6RDxFiRJ8ULXcZo6cbXqiZGUgR2Xi%2FSeEZzevqwdtWkBVwDBevvpEYjdHkJca%2BbLV6RdXTW8%2F5WBz9ieFNEpEbD3oEG7fJDfwG773bn9MSvT4ycQaTraWU2lCa8xEimTje7O0EXtO9jRtJGZy%2B5uOUaFbIEQb8vtorx4LsHtUhhlA3YQl6WYlIOha%2F1wnXezefUNrC2C9Ban2lG%2BWWoKF6UEkstBCSzA8K4joutFrV4hgs0VmOwqRd4yQ8jC%2BCJXLwpiUWRC8shuZKFoC7ebTajyit2NZChx2JF%2FTEZP74FMzyKcBJcvQzGdc84W7olD1y1t5aCGXSee7d7ywxupAim1JjhOvFdLT8%2Bd93dTdK%2FKiTWWbBh%2BF%2Brsh0zWFkGI6lCWLOF4wxJSKvQY6pgG8pzplUZtPnV%2B%2FkvHO%2B%2BP3hdIXAc4ijEJc7nIy%2ByPMnZ3T0Tel3BtVQ92ztDadGCPXj2AaCs70nso8mOEiHIscB77%2Fqsthmb5o%2F%2F2OZq4GuZUtbU9%2BlNr4niKPcTJd2HtlkInOJ9GKqsKMHaQNpdkKk7uAL%2BSovfYnfE6y47s3DUYEcpWFFEBRghp4w80rgW4zLGTuQRcBtUuMuYq3OzVdeStHxP4Z&X-Amz-Signature=65c5f03d4246571c74ee2a3145575e21dbf0e3d9b8df1d97f782ea01844b7afb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWJMTPXV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIE%2BNCNB0YuR%2BVuXYTcDo7%2FeFbmSMFDBW%2BKUXMK%2F0WqcOAiBFjJYPVECmLXtBVZCkrETcu50pU3sDSXwL868icl%2B21Cr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMWNwbvk6rX%2BK%2BUMO7KtwD6G%2BJZxOygwXyqIhjTYOkp2cQs%2BXXUGnRuHqlsWIOZbPtQX0CG5E6QNH8fQpvQbmn1W%2F5wrdllJPPRfWCHX5tpQz06Y4w23oPR6rGGvaDEfa1iXzXx7J9EkuQpfZ9khAawgFs%2FbZXBJ9RwEHe2B0kpcl96UU7w1mnZe2TWh1vAii1u2spQfdyDcOkJ321iNkmzpEWo7aMSA5lV52YykZFFzLikdK7KAf7kurTydwP7Ij%2BJpOUDHV6RDxFiRJ8ULXcZo6cbXqiZGUgR2Xi%2FSeEZzevqwdtWkBVwDBevvpEYjdHkJca%2BbLV6RdXTW8%2F5WBz9ieFNEpEbD3oEG7fJDfwG773bn9MSvT4ycQaTraWU2lCa8xEimTje7O0EXtO9jRtJGZy%2B5uOUaFbIEQb8vtorx4LsHtUhhlA3YQl6WYlIOha%2F1wnXezefUNrC2C9Ban2lG%2BWWoKF6UEkstBCSzA8K4joutFrV4hgs0VmOwqRd4yQ8jC%2BCJXLwpiUWRC8shuZKFoC7ebTajyit2NZChx2JF%2FTEZP74FMzyKcBJcvQzGdc84W7olD1y1t5aCGXSee7d7ywxupAim1JjhOvFdLT8%2Bd93dTdK%2FKiTWWbBh%2BF%2Brsh0zWFkGI6lCWLOF4wxJSKvQY6pgG8pzplUZtPnV%2B%2FkvHO%2B%2BP3hdIXAc4ijEJc7nIy%2ByPMnZ3T0Tel3BtVQ92ztDadGCPXj2AaCs70nso8mOEiHIscB77%2Fqsthmb5o%2F%2F2OZq4GuZUtbU9%2BlNr4niKPcTJd2HtlkInOJ9GKqsKMHaQNpdkKk7uAL%2BSovfYnfE6y47s3DUYEcpWFFEBRghp4w80rgW4zLGTuQRcBtUuMuYq3OzVdeStHxP4Z&X-Amz-Signature=16b64c417f95530d3b930fad806be12be4aa20d1e883b4bedc05bf77a357b269&X-Amz-SignedHeaders=host&x-id=GetObject)
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
