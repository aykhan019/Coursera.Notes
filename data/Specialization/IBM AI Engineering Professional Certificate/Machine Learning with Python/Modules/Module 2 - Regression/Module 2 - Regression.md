

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RK5M3TX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2FtWD16ufNw8M%2F5YHIv6FUxiLu7HBZRnX%2F7DRmfpr7OAiBJ1zlSsD6aC8ahbo4E4fOy6oZJ7ujj0kBI2qiDtrHXkyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZefslWg5TGNYnMxKtwDlLSwx%2BeHwXhH%2BrITGiz9LU2icuELn4YEw7wIvBNdGPhKYhS8PZxhjP3VX2g0%2BAM%2BHtermabFFluZ4gWMrp4NLIjfB0PWA5dXXIWkJtGCjCaUOriDxEcLRhwL7ZX6okAyUxW4C2c8age6VhAQsOq4vgW3i2vti3dFAGvI8irTxz8lbEAdSo40GkePlZARr1DhR%2Fw%2FKHqGp%2BoSAHFYJv6WWQ8AvjDe%2BaKuxgOQJdW86d9FmD9rGC6c2StO1gapmhVtTyEUTbk8lZrjv%2FdSV%2BmvDfV%2FsCWy1OG3ez4EVcI2mqmjHeR6tJinGlykZ5mID0j67TS3VAXCYcCCtmZ7s3NxugXqzipDbpLi4EQNbW7Id9gVTiWWaG6gZc5wsegqbfjS5tOiDGVEz26Fyq2QgpGB6yoXxdp9BpI%2FbucWOycVTKYr%2BxNWFL%2B7aY2rfILEsDFcg5%2B1%2BXj3wMeZEV747SKphiok9nFSCW%2BaZseSN0CQYrXQLf6YVv6URONEdnQyLTwTigAm%2F85voOmZDfGw3kfQTusu9db9KQQ%2BTgU44IHcdLQGRuBXA7ylJkebO765AzTUsGGi6Bd5qiUNxUMmZG%2FTT7cBQaWOchbjIhjO4AbnQ9Al6VKjSo8an6VWVFgwg%2F7xvAY6pgHPq2ZaeCZYAr8rGobS6mi%2BDlafVwonkQ9sf4rfTeUWu48VJJFv5AlYRmdt9EpcrBY2JrSdwE7mTxwgtKBH7boKZ4t79qPlMtKcndTimbFoem7BuE0DfgMHilCkLtXO%2Fl9miOstC5qrhY3WJNSwB41p20gql16Jewg6CD0kKg7hKmA3U59s7Ka69uL%2BSeMOwNRBaChhjp460JygiR32WaK%2F4wgvJ0xx&X-Amz-Signature=2f3312dcd48b4895dc7b516b72793ae36885bf7e6ea469063a4473f9b8058d57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RK5M3TX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2FtWD16ufNw8M%2F5YHIv6FUxiLu7HBZRnX%2F7DRmfpr7OAiBJ1zlSsD6aC8ahbo4E4fOy6oZJ7ujj0kBI2qiDtrHXkyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZefslWg5TGNYnMxKtwDlLSwx%2BeHwXhH%2BrITGiz9LU2icuELn4YEw7wIvBNdGPhKYhS8PZxhjP3VX2g0%2BAM%2BHtermabFFluZ4gWMrp4NLIjfB0PWA5dXXIWkJtGCjCaUOriDxEcLRhwL7ZX6okAyUxW4C2c8age6VhAQsOq4vgW3i2vti3dFAGvI8irTxz8lbEAdSo40GkePlZARr1DhR%2Fw%2FKHqGp%2BoSAHFYJv6WWQ8AvjDe%2BaKuxgOQJdW86d9FmD9rGC6c2StO1gapmhVtTyEUTbk8lZrjv%2FdSV%2BmvDfV%2FsCWy1OG3ez4EVcI2mqmjHeR6tJinGlykZ5mID0j67TS3VAXCYcCCtmZ7s3NxugXqzipDbpLi4EQNbW7Id9gVTiWWaG6gZc5wsegqbfjS5tOiDGVEz26Fyq2QgpGB6yoXxdp9BpI%2FbucWOycVTKYr%2BxNWFL%2B7aY2rfILEsDFcg5%2B1%2BXj3wMeZEV747SKphiok9nFSCW%2BaZseSN0CQYrXQLf6YVv6URONEdnQyLTwTigAm%2F85voOmZDfGw3kfQTusu9db9KQQ%2BTgU44IHcdLQGRuBXA7ylJkebO765AzTUsGGi6Bd5qiUNxUMmZG%2FTT7cBQaWOchbjIhjO4AbnQ9Al6VKjSo8an6VWVFgwg%2F7xvAY6pgHPq2ZaeCZYAr8rGobS6mi%2BDlafVwonkQ9sf4rfTeUWu48VJJFv5AlYRmdt9EpcrBY2JrSdwE7mTxwgtKBH7boKZ4t79qPlMtKcndTimbFoem7BuE0DfgMHilCkLtXO%2Fl9miOstC5qrhY3WJNSwB41p20gql16Jewg6CD0kKg7hKmA3U59s7Ka69uL%2BSeMOwNRBaChhjp460JygiR32WaK%2F4wgvJ0xx&X-Amz-Signature=d760e1287099591114f3f45f8076844cd22f409b8322ce0f6f942522ba132315&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RK5M3TX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2FtWD16ufNw8M%2F5YHIv6FUxiLu7HBZRnX%2F7DRmfpr7OAiBJ1zlSsD6aC8ahbo4E4fOy6oZJ7ujj0kBI2qiDtrHXkyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZefslWg5TGNYnMxKtwDlLSwx%2BeHwXhH%2BrITGiz9LU2icuELn4YEw7wIvBNdGPhKYhS8PZxhjP3VX2g0%2BAM%2BHtermabFFluZ4gWMrp4NLIjfB0PWA5dXXIWkJtGCjCaUOriDxEcLRhwL7ZX6okAyUxW4C2c8age6VhAQsOq4vgW3i2vti3dFAGvI8irTxz8lbEAdSo40GkePlZARr1DhR%2Fw%2FKHqGp%2BoSAHFYJv6WWQ8AvjDe%2BaKuxgOQJdW86d9FmD9rGC6c2StO1gapmhVtTyEUTbk8lZrjv%2FdSV%2BmvDfV%2FsCWy1OG3ez4EVcI2mqmjHeR6tJinGlykZ5mID0j67TS3VAXCYcCCtmZ7s3NxugXqzipDbpLi4EQNbW7Id9gVTiWWaG6gZc5wsegqbfjS5tOiDGVEz26Fyq2QgpGB6yoXxdp9BpI%2FbucWOycVTKYr%2BxNWFL%2B7aY2rfILEsDFcg5%2B1%2BXj3wMeZEV747SKphiok9nFSCW%2BaZseSN0CQYrXQLf6YVv6URONEdnQyLTwTigAm%2F85voOmZDfGw3kfQTusu9db9KQQ%2BTgU44IHcdLQGRuBXA7ylJkebO765AzTUsGGi6Bd5qiUNxUMmZG%2FTT7cBQaWOchbjIhjO4AbnQ9Al6VKjSo8an6VWVFgwg%2F7xvAY6pgHPq2ZaeCZYAr8rGobS6mi%2BDlafVwonkQ9sf4rfTeUWu48VJJFv5AlYRmdt9EpcrBY2JrSdwE7mTxwgtKBH7boKZ4t79qPlMtKcndTimbFoem7BuE0DfgMHilCkLtXO%2Fl9miOstC5qrhY3WJNSwB41p20gql16Jewg6CD0kKg7hKmA3U59s7Ka69uL%2BSeMOwNRBaChhjp460JygiR32WaK%2F4wgvJ0xx&X-Amz-Signature=b0d19d3a221630a735fde1afc7a1078d9f0cdbae740dddfc90c01d1a199b1147&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RK5M3TX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2FtWD16ufNw8M%2F5YHIv6FUxiLu7HBZRnX%2F7DRmfpr7OAiBJ1zlSsD6aC8ahbo4E4fOy6oZJ7ujj0kBI2qiDtrHXkyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZefslWg5TGNYnMxKtwDlLSwx%2BeHwXhH%2BrITGiz9LU2icuELn4YEw7wIvBNdGPhKYhS8PZxhjP3VX2g0%2BAM%2BHtermabFFluZ4gWMrp4NLIjfB0PWA5dXXIWkJtGCjCaUOriDxEcLRhwL7ZX6okAyUxW4C2c8age6VhAQsOq4vgW3i2vti3dFAGvI8irTxz8lbEAdSo40GkePlZARr1DhR%2Fw%2FKHqGp%2BoSAHFYJv6WWQ8AvjDe%2BaKuxgOQJdW86d9FmD9rGC6c2StO1gapmhVtTyEUTbk8lZrjv%2FdSV%2BmvDfV%2FsCWy1OG3ez4EVcI2mqmjHeR6tJinGlykZ5mID0j67TS3VAXCYcCCtmZ7s3NxugXqzipDbpLi4EQNbW7Id9gVTiWWaG6gZc5wsegqbfjS5tOiDGVEz26Fyq2QgpGB6yoXxdp9BpI%2FbucWOycVTKYr%2BxNWFL%2B7aY2rfILEsDFcg5%2B1%2BXj3wMeZEV747SKphiok9nFSCW%2BaZseSN0CQYrXQLf6YVv6URONEdnQyLTwTigAm%2F85voOmZDfGw3kfQTusu9db9KQQ%2BTgU44IHcdLQGRuBXA7ylJkebO765AzTUsGGi6Bd5qiUNxUMmZG%2FTT7cBQaWOchbjIhjO4AbnQ9Al6VKjSo8an6VWVFgwg%2F7xvAY6pgHPq2ZaeCZYAr8rGobS6mi%2BDlafVwonkQ9sf4rfTeUWu48VJJFv5AlYRmdt9EpcrBY2JrSdwE7mTxwgtKBH7boKZ4t79qPlMtKcndTimbFoem7BuE0DfgMHilCkLtXO%2Fl9miOstC5qrhY3WJNSwB41p20gql16Jewg6CD0kKg7hKmA3U59s7Ka69uL%2BSeMOwNRBaChhjp460JygiR32WaK%2F4wgvJ0xx&X-Amz-Signature=f48e541ea1fa97a3af3c7d7b7e55c3e5b40a89d5a3ef04522a13c86af0fd3f6a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RK5M3TX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2FtWD16ufNw8M%2F5YHIv6FUxiLu7HBZRnX%2F7DRmfpr7OAiBJ1zlSsD6aC8ahbo4E4fOy6oZJ7ujj0kBI2qiDtrHXkyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZefslWg5TGNYnMxKtwDlLSwx%2BeHwXhH%2BrITGiz9LU2icuELn4YEw7wIvBNdGPhKYhS8PZxhjP3VX2g0%2BAM%2BHtermabFFluZ4gWMrp4NLIjfB0PWA5dXXIWkJtGCjCaUOriDxEcLRhwL7ZX6okAyUxW4C2c8age6VhAQsOq4vgW3i2vti3dFAGvI8irTxz8lbEAdSo40GkePlZARr1DhR%2Fw%2FKHqGp%2BoSAHFYJv6WWQ8AvjDe%2BaKuxgOQJdW86d9FmD9rGC6c2StO1gapmhVtTyEUTbk8lZrjv%2FdSV%2BmvDfV%2FsCWy1OG3ez4EVcI2mqmjHeR6tJinGlykZ5mID0j67TS3VAXCYcCCtmZ7s3NxugXqzipDbpLi4EQNbW7Id9gVTiWWaG6gZc5wsegqbfjS5tOiDGVEz26Fyq2QgpGB6yoXxdp9BpI%2FbucWOycVTKYr%2BxNWFL%2B7aY2rfILEsDFcg5%2B1%2BXj3wMeZEV747SKphiok9nFSCW%2BaZseSN0CQYrXQLf6YVv6URONEdnQyLTwTigAm%2F85voOmZDfGw3kfQTusu9db9KQQ%2BTgU44IHcdLQGRuBXA7ylJkebO765AzTUsGGi6Bd5qiUNxUMmZG%2FTT7cBQaWOchbjIhjO4AbnQ9Al6VKjSo8an6VWVFgwg%2F7xvAY6pgHPq2ZaeCZYAr8rGobS6mi%2BDlafVwonkQ9sf4rfTeUWu48VJJFv5AlYRmdt9EpcrBY2JrSdwE7mTxwgtKBH7boKZ4t79qPlMtKcndTimbFoem7BuE0DfgMHilCkLtXO%2Fl9miOstC5qrhY3WJNSwB41p20gql16Jewg6CD0kKg7hKmA3U59s7Ka69uL%2BSeMOwNRBaChhjp460JygiR32WaK%2F4wgvJ0xx&X-Amz-Signature=3e93321a20c780ef8b76fe5dc8369340e77f382d751c8b62b97bcdb1cd373de8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RK5M3TX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2FtWD16ufNw8M%2F5YHIv6FUxiLu7HBZRnX%2F7DRmfpr7OAiBJ1zlSsD6aC8ahbo4E4fOy6oZJ7ujj0kBI2qiDtrHXkyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZefslWg5TGNYnMxKtwDlLSwx%2BeHwXhH%2BrITGiz9LU2icuELn4YEw7wIvBNdGPhKYhS8PZxhjP3VX2g0%2BAM%2BHtermabFFluZ4gWMrp4NLIjfB0PWA5dXXIWkJtGCjCaUOriDxEcLRhwL7ZX6okAyUxW4C2c8age6VhAQsOq4vgW3i2vti3dFAGvI8irTxz8lbEAdSo40GkePlZARr1DhR%2Fw%2FKHqGp%2BoSAHFYJv6WWQ8AvjDe%2BaKuxgOQJdW86d9FmD9rGC6c2StO1gapmhVtTyEUTbk8lZrjv%2FdSV%2BmvDfV%2FsCWy1OG3ez4EVcI2mqmjHeR6tJinGlykZ5mID0j67TS3VAXCYcCCtmZ7s3NxugXqzipDbpLi4EQNbW7Id9gVTiWWaG6gZc5wsegqbfjS5tOiDGVEz26Fyq2QgpGB6yoXxdp9BpI%2FbucWOycVTKYr%2BxNWFL%2B7aY2rfILEsDFcg5%2B1%2BXj3wMeZEV747SKphiok9nFSCW%2BaZseSN0CQYrXQLf6YVv6URONEdnQyLTwTigAm%2F85voOmZDfGw3kfQTusu9db9KQQ%2BTgU44IHcdLQGRuBXA7ylJkebO765AzTUsGGi6Bd5qiUNxUMmZG%2FTT7cBQaWOchbjIhjO4AbnQ9Al6VKjSo8an6VWVFgwg%2F7xvAY6pgHPq2ZaeCZYAr8rGobS6mi%2BDlafVwonkQ9sf4rfTeUWu48VJJFv5AlYRmdt9EpcrBY2JrSdwE7mTxwgtKBH7boKZ4t79qPlMtKcndTimbFoem7BuE0DfgMHilCkLtXO%2Fl9miOstC5qrhY3WJNSwB41p20gql16Jewg6CD0kKg7hKmA3U59s7Ka69uL%2BSeMOwNRBaChhjp460JygiR32WaK%2F4wgvJ0xx&X-Amz-Signature=bf2ce756cb8cb2cbd2bc2a21d3eec40748149db055413fede1763e2a821be7a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RK5M3TX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2FtWD16ufNw8M%2F5YHIv6FUxiLu7HBZRnX%2F7DRmfpr7OAiBJ1zlSsD6aC8ahbo4E4fOy6oZJ7ujj0kBI2qiDtrHXkyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZefslWg5TGNYnMxKtwDlLSwx%2BeHwXhH%2BrITGiz9LU2icuELn4YEw7wIvBNdGPhKYhS8PZxhjP3VX2g0%2BAM%2BHtermabFFluZ4gWMrp4NLIjfB0PWA5dXXIWkJtGCjCaUOriDxEcLRhwL7ZX6okAyUxW4C2c8age6VhAQsOq4vgW3i2vti3dFAGvI8irTxz8lbEAdSo40GkePlZARr1DhR%2Fw%2FKHqGp%2BoSAHFYJv6WWQ8AvjDe%2BaKuxgOQJdW86d9FmD9rGC6c2StO1gapmhVtTyEUTbk8lZrjv%2FdSV%2BmvDfV%2FsCWy1OG3ez4EVcI2mqmjHeR6tJinGlykZ5mID0j67TS3VAXCYcCCtmZ7s3NxugXqzipDbpLi4EQNbW7Id9gVTiWWaG6gZc5wsegqbfjS5tOiDGVEz26Fyq2QgpGB6yoXxdp9BpI%2FbucWOycVTKYr%2BxNWFL%2B7aY2rfILEsDFcg5%2B1%2BXj3wMeZEV747SKphiok9nFSCW%2BaZseSN0CQYrXQLf6YVv6URONEdnQyLTwTigAm%2F85voOmZDfGw3kfQTusu9db9KQQ%2BTgU44IHcdLQGRuBXA7ylJkebO765AzTUsGGi6Bd5qiUNxUMmZG%2FTT7cBQaWOchbjIhjO4AbnQ9Al6VKjSo8an6VWVFgwg%2F7xvAY6pgHPq2ZaeCZYAr8rGobS6mi%2BDlafVwonkQ9sf4rfTeUWu48VJJFv5AlYRmdt9EpcrBY2JrSdwE7mTxwgtKBH7boKZ4t79qPlMtKcndTimbFoem7BuE0DfgMHilCkLtXO%2Fl9miOstC5qrhY3WJNSwB41p20gql16Jewg6CD0kKg7hKmA3U59s7Ka69uL%2BSeMOwNRBaChhjp460JygiR32WaK%2F4wgvJ0xx&X-Amz-Signature=eb3e0c21b96622f9ff812fec1004da1c04044ce05218c3428937dae97070c6e2&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RK5M3TX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC%2FtWD16ufNw8M%2F5YHIv6FUxiLu7HBZRnX%2F7DRmfpr7OAiBJ1zlSsD6aC8ahbo4E4fOy6oZJ7ujj0kBI2qiDtrHXkyqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAZefslWg5TGNYnMxKtwDlLSwx%2BeHwXhH%2BrITGiz9LU2icuELn4YEw7wIvBNdGPhKYhS8PZxhjP3VX2g0%2BAM%2BHtermabFFluZ4gWMrp4NLIjfB0PWA5dXXIWkJtGCjCaUOriDxEcLRhwL7ZX6okAyUxW4C2c8age6VhAQsOq4vgW3i2vti3dFAGvI8irTxz8lbEAdSo40GkePlZARr1DhR%2Fw%2FKHqGp%2BoSAHFYJv6WWQ8AvjDe%2BaKuxgOQJdW86d9FmD9rGC6c2StO1gapmhVtTyEUTbk8lZrjv%2FdSV%2BmvDfV%2FsCWy1OG3ez4EVcI2mqmjHeR6tJinGlykZ5mID0j67TS3VAXCYcCCtmZ7s3NxugXqzipDbpLi4EQNbW7Id9gVTiWWaG6gZc5wsegqbfjS5tOiDGVEz26Fyq2QgpGB6yoXxdp9BpI%2FbucWOycVTKYr%2BxNWFL%2B7aY2rfILEsDFcg5%2B1%2BXj3wMeZEV747SKphiok9nFSCW%2BaZseSN0CQYrXQLf6YVv6URONEdnQyLTwTigAm%2F85voOmZDfGw3kfQTusu9db9KQQ%2BTgU44IHcdLQGRuBXA7ylJkebO765AzTUsGGi6Bd5qiUNxUMmZG%2FTT7cBQaWOchbjIhjO4AbnQ9Al6VKjSo8an6VWVFgwg%2F7xvAY6pgHPq2ZaeCZYAr8rGobS6mi%2BDlafVwonkQ9sf4rfTeUWu48VJJFv5AlYRmdt9EpcrBY2JrSdwE7mTxwgtKBH7boKZ4t79qPlMtKcndTimbFoem7BuE0DfgMHilCkLtXO%2Fl9miOstC5qrhY3WJNSwB41p20gql16Jewg6CD0kKg7hKmA3U59s7Ka69uL%2BSeMOwNRBaChhjp460JygiR32WaK%2F4wgvJ0xx&X-Amz-Signature=17b2b58ed623381c2e207ca3cad79f52cb5835a42696ff719f80bd90c0cad341&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625MW4QPT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwoXkH5KWAv8TP9SN%2BiCE5iahMs%2FK0mJlajKWydPp8xwIhAMZUjTz%2BlyU2ty5IjQ4DmhGDYcwZgl6fL9cl0ygyZDRVKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTBnWvdcVoMlRURWYq3AMLDtCcsWu5zpEj%2BML68q9UvYl8OWWyvkRPNB4owAeEA6SJCeE7euw7KruVvbhgGX783O5wlYGmWFFvVMoeiPyHf94C9r2zzPtGCSg3mzJfFlD6NcJWyrKTvltdnwtjh%2Frl1AD5VrwnE8ONkR7zdA1SJCVA8eLFUIrsGGLdo6GLjFcXsTSL%2FDk9qurdiBEV0QZPG1tOVdUk4srvoCwbYKbV3QAwnp0aS1H0PhFVUuT443K6AWlpXZXoD12qUd2aQsKfa89wNGVOMWIJsC%2BM7fyuCvzt0fhyGD5GD1xmf3X3OMWbdE506FCg9mYgFk%2BOM9p32p0DM%2FNawQIMUZKzUObTjGzvyXmeYTp22ylr7Y7%2BU1jXDCg1U5pQXFAXwqyG3dw4Mg1zAuNzKcE1lw7T0dG3hXCXxnX5%2BDcBnJYPskIRNoqtb0FMbcOdQ6Mk%2BPHwMjsoSwQY4z8gl4tvYSCuOVxoE3B0jOTcXXJCjiMzhdXxJPytWiZxq6Ny2PoFnWF5kuX6DbJOu8BNFl2alz6oYaDHhkMr8VpW9WyH2zy2h4rHMpLsnHjE%2BzxS%2F5fIKR9u6AsMCyiZgvnxVI2h%2BK6WklQ55PvbXbaf%2F87rJ0mDlZQtnatT%2BOmN8T8iqbAicDDj%2FfG8BjqkAas8M6235E5To%2BW1fOa%2Bma6Cl09V3H3goJY6pzS5bzUW0TZj7WwgGbBp7BxqlG4kCGsjjyD8ItzdftMKCp1ksNv9rA12omzkKkW2nen%2Bm5rxzLpPwJTWnCOi31RZALoZpdV0HXogC6%2BTbFaRe6wrM7qy8UN8tqJXlLcUU9eIN0bEXexY2dpspJWPUvLLU603ruveHt%2B33zagxlCOxaoXi1voFxtW&X-Amz-Signature=8ae8ee739371a9c5f5a9d7ce19d58407d82a86c0cd0e1c55038075b6a9dcd0f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYYVML3Z%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoV3bU5RKwVoqkRK0kJ17WCt9s1ELiCl4GcvnLYzPjvQIhAPVRUw841A9Co6aJOPJX6vtWdGLAU%2BAp54VokFYxMf4oKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzqbx6O6OWxbiIXAjwq3ANQnkVdVB9Pg0oqOTWbdm%2F6HfKyxoZr42bNUDNP52AetQQm7x84dd774jVFJYdoBhAmMdOjgmYAz6XaV0AZN30PkWaAQRiUcdxFTZnhR02s2IgsDfiOKMgpTvlpuz8ANV4elXvLDYU%2BnhWv5%2FVid%2FmCsHIVTqygvT92PERTEh%2FMjgSP%2BoWWZ0y5%2FCHoJHfdsD4aY47QKSZsGzA1JteSIrascTm7cgem1i86SHPXme6GKPZMNqu9TwaHtFK3I6Bd2nZvhILcLNUqgitzQMsbsDcuVRB8hDj8onQNanxmcytPvYHPde0FCjJ7HVIG%2BXB%2B6cOQK3u70fMzSm2Oo0HVxwRMGCsUAAeu0gRxZma8f40jj0Zt5mDglCm61cVLk98VH25Vj31%2FWa2h3cHaf%2B7tLDtNJw2ntre%2BPQuI10NZTnc07cDl%2FY9jicokp91ZNm6EX6d8nsfW5Un9QyK%2FOdoK4WpF99sK5WSUkcXO76vOupdh0Nu%2BSs6AJFeMfaEUUpPMoy1%2BLhPybcJmQYtZ9Vwm0sKhYurJjtG6eSTmboKrmPX3Cq8XuA%2F3mbyXANGqyi6Mdts5JY43%2FHssZFkLv91Q%2FdxbGrUJyw54YXRqVJG3vNVQXBAHQqHDOxl2DwC3xjD7%2FvG8BjqkAQaWyG5x8ab5oXIu94hCQHnIMLxNeV3NEwevW3hEv86SnQ9W8D0Z7HvhfjqwIi9YqUA4eY7cH7aYI1L3Yj%2BZMwOZsLispQdLHjWJNBUWjAAXMyK35rOZwM9vihfJg0MG1KNrrfP1Iu0ACi8gLiDkNd5Ok6TTn%2F3FJZPZoZZoGwIOpCRJBpaQMcAuh2Ud%2Bckd8tdSDZqcvFOYGVhIR2yD5wLIUC45&X-Amz-Signature=ef0a90411b74b23c93712e8ac25ec8ce25fc140936e605099e85d96bb42c9f9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2XAO4S%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDi%2FSpje2i5d0gWakwllW4AjBW4U1SCre%2BNa%2BTXXA3niQIgTi9BJ4lY8FUvvOnY0wRpOTIQDxp4Oa7yQPwhl%2FaLQ0EqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPls%2BT5BzYmzeQa6byrcA8wZKlAZKEtHbpV6W42QcoEdolwwMNrKI93kvCKF%2F4cmSuvsBLDFHDTxqdS2xvjG%2FugJu76OuML3UNjOXcEzbgh0rxwkyosP8gqvnh%2FrrMt0GaTL1tQEeD8tG%2B92fCV5b6Aphu20ur3mdTt25DHVh3HZReIckypui%2BBDDfbtZEONKtp1vEJbvpxz3HKhNIpMmln4Q9VSgFiHT4fDceYJ58GidFbe3tKSYXKqreFkcwwlXcSS71BNDxdWJxj0okZ0ERCVSilDVKGDsU4DCI2ysaFdgV%2F1mvVKon5ON2guPDFg3Gh7EQ%2F9nPNHqYSe5iWW4KxvFLdAqTsDjsoJ27gO7YFvNphPZ%2F6BHT89hVcHjXDOC66lXmgubtxNZ2w9212QONhT%2BNBPZ%2B%2FwYifctMCSMwhCy1%2BGngfLbSUoiYzyXYP7W0OjgjlIjSdykew82lf92XYNL106BWA%2FY3BZF8ukHfyl0adumBGVLLMsR4i96i9B3UCBgeHvRo3xC3uhQJqkdUv7uV1SyhoDYZiegnmvTcxeeOsC3nhGlfjzoYkvcD%2FGJ4J3MQAIBGr4QzoZuXKHmjhg0QPG8rO8KKBDpAFBJNcx9LohRUQta8neH1mcRNxATYwcfZRJGfqtiepfMNX%2B8bwGOqUBRXKPB8qfVCSFq14qTzr192HMc0JbgMFIMg9uH%2FwnGXrlp94Sk618oeceVfXp1tM2jJUraneFfPPSCte3D5ulWsQ458bMFRRyn0TU6Kqlg53%2BbUjt6p%2F5InVQGtGggbskhkb2I1uF%2Bf5rF4dmvz8F45StvOhIcN0fgEe%2F5fBsp9dppkg%2Bo5hw32obw5MprqGvau%2FRBGK9fxTplsmeXa6UAs8k2QQF&X-Amz-Signature=09e9e9944592855c3f0bf9e28c4caa8bee8b2e40c8ca786a27acaf2c0d6703a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG2XAO4S%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDi%2FSpje2i5d0gWakwllW4AjBW4U1SCre%2BNa%2BTXXA3niQIgTi9BJ4lY8FUvvOnY0wRpOTIQDxp4Oa7yQPwhl%2FaLQ0EqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPls%2BT5BzYmzeQa6byrcA8wZKlAZKEtHbpV6W42QcoEdolwwMNrKI93kvCKF%2F4cmSuvsBLDFHDTxqdS2xvjG%2FugJu76OuML3UNjOXcEzbgh0rxwkyosP8gqvnh%2FrrMt0GaTL1tQEeD8tG%2B92fCV5b6Aphu20ur3mdTt25DHVh3HZReIckypui%2BBDDfbtZEONKtp1vEJbvpxz3HKhNIpMmln4Q9VSgFiHT4fDceYJ58GidFbe3tKSYXKqreFkcwwlXcSS71BNDxdWJxj0okZ0ERCVSilDVKGDsU4DCI2ysaFdgV%2F1mvVKon5ON2guPDFg3Gh7EQ%2F9nPNHqYSe5iWW4KxvFLdAqTsDjsoJ27gO7YFvNphPZ%2F6BHT89hVcHjXDOC66lXmgubtxNZ2w9212QONhT%2BNBPZ%2B%2FwYifctMCSMwhCy1%2BGngfLbSUoiYzyXYP7W0OjgjlIjSdykew82lf92XYNL106BWA%2FY3BZF8ukHfyl0adumBGVLLMsR4i96i9B3UCBgeHvRo3xC3uhQJqkdUv7uV1SyhoDYZiegnmvTcxeeOsC3nhGlfjzoYkvcD%2FGJ4J3MQAIBGr4QzoZuXKHmjhg0QPG8rO8KKBDpAFBJNcx9LohRUQta8neH1mcRNxATYwcfZRJGfqtiepfMNX%2B8bwGOqUBRXKPB8qfVCSFq14qTzr192HMc0JbgMFIMg9uH%2FwnGXrlp94Sk618oeceVfXp1tM2jJUraneFfPPSCte3D5ulWsQ458bMFRRyn0TU6Kqlg53%2BbUjt6p%2F5InVQGtGggbskhkb2I1uF%2Bf5rF4dmvz8F45StvOhIcN0fgEe%2F5fBsp9dppkg%2Bo5hw32obw5MprqGvau%2FRBGK9fxTplsmeXa6UAs8k2QQF&X-Amz-Signature=627587f1e0d3c74a9823999e96101c1dfdcd753b4f8f497fc8d467607d0cf893&X-Amz-SignedHeaders=host&x-id=GetObject)
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
