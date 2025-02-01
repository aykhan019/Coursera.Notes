

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OGH6VOZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdgBLmdNZHW25rk9sP9b0BMC7QO9FGkgWPbwNymnBzgIhAJ77wDF8u3EVjP2Pv3zf8E7bbN5vtp%2F3lUHKGz4GKWbZKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfK1%2FceMLa5OquDJcq3AMVMODetpuurR1rKbxbcxNakHdgxIRSShK6iztISpeNZ%2FBCiKPzVCxI%2FrtKKG1EOq5KrQMHRl%2BKafEq3SlYVMelaA2ghdI6Qhgq7IlkQDHb5hVgWzaR%2BlN2eDcobZNStnJagTLBJe5qqjneyiWNpE5N4ix9kJEMEku2Y6EF5r3r5hWgGoR5SpjTIZxGVEwzCt2%2FPNCee55jOoStnApHisWtYvOvfhdxJjrDwvQeg1qJlRaDHeWoX2Ve9slaXTxYN%2FmnkfWeaVGOqXQNvvvDb5MsXNZM9r56ZPb6R%2Fdy1ZXGl0HO4tzMFg3h9YwtwYQxn4ivS62nm%2BB5lAVZLUdUZ7U48%2Boi2BKCGo96XwF%2FCpC1zLP1K7p%2FqlNAG0tVmI%2FXUH1BUHqbhtWaycyawQwG078Rhoa51HEGYCCxRvuNlsCQmKDLYoB%2Fd7w55CIt9ii2PInpMBeue81QkURxz4BsMnfxDE0r7UFazQKf7cfg%2B45Vky%2BdcFVcN8g6ey97aGiROcC4hgOYLd8HaKsJJqPKc0PTfd8uCicFTl36WgHZmjWRrTnGuhHkiUuzWbO9hRPBTVDzDGMNmldR4cQVH%2FdbOzGHOPdxWfp1QQMFAr9lLWrS5%2BfnEaOeYjwTfoDnQTD%2Bsfq8BjqkAV0BUuhYAA4zQmoTQRJldz%2FKDXhqsTezv%2BCUPU9%2Bjv0DP6Ljhj08TkFfkjuEfcmOl95t9NEd%2FqKGkvzA1EFvEF1MN0snaQ9Ncr80qN5n4ihrL2erJt13jvVUwiyKjWWwjgSp6NbmjZ3wGi1QTUxKnXGWK%2FMa4%2BX1gy%2F8jECyoQQrt6sf6B0fzOFfQV7LSW7SQ9J1CpXeQAVK1ighBDN0rK%2BQp3iE&X-Amz-Signature=27328a4a546a51b96e92a56c44e5b37566276a4b720fc9d8fe7c8bcae57f7101&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OGH6VOZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdgBLmdNZHW25rk9sP9b0BMC7QO9FGkgWPbwNymnBzgIhAJ77wDF8u3EVjP2Pv3zf8E7bbN5vtp%2F3lUHKGz4GKWbZKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfK1%2FceMLa5OquDJcq3AMVMODetpuurR1rKbxbcxNakHdgxIRSShK6iztISpeNZ%2FBCiKPzVCxI%2FrtKKG1EOq5KrQMHRl%2BKafEq3SlYVMelaA2ghdI6Qhgq7IlkQDHb5hVgWzaR%2BlN2eDcobZNStnJagTLBJe5qqjneyiWNpE5N4ix9kJEMEku2Y6EF5r3r5hWgGoR5SpjTIZxGVEwzCt2%2FPNCee55jOoStnApHisWtYvOvfhdxJjrDwvQeg1qJlRaDHeWoX2Ve9slaXTxYN%2FmnkfWeaVGOqXQNvvvDb5MsXNZM9r56ZPb6R%2Fdy1ZXGl0HO4tzMFg3h9YwtwYQxn4ivS62nm%2BB5lAVZLUdUZ7U48%2Boi2BKCGo96XwF%2FCpC1zLP1K7p%2FqlNAG0tVmI%2FXUH1BUHqbhtWaycyawQwG078Rhoa51HEGYCCxRvuNlsCQmKDLYoB%2Fd7w55CIt9ii2PInpMBeue81QkURxz4BsMnfxDE0r7UFazQKf7cfg%2B45Vky%2BdcFVcN8g6ey97aGiROcC4hgOYLd8HaKsJJqPKc0PTfd8uCicFTl36WgHZmjWRrTnGuhHkiUuzWbO9hRPBTVDzDGMNmldR4cQVH%2FdbOzGHOPdxWfp1QQMFAr9lLWrS5%2BfnEaOeYjwTfoDnQTD%2Bsfq8BjqkAV0BUuhYAA4zQmoTQRJldz%2FKDXhqsTezv%2BCUPU9%2Bjv0DP6Ljhj08TkFfkjuEfcmOl95t9NEd%2FqKGkvzA1EFvEF1MN0snaQ9Ncr80qN5n4ihrL2erJt13jvVUwiyKjWWwjgSp6NbmjZ3wGi1QTUxKnXGWK%2FMa4%2BX1gy%2F8jECyoQQrt6sf6B0fzOFfQV7LSW7SQ9J1CpXeQAVK1ighBDN0rK%2BQp3iE&X-Amz-Signature=018f89d16bdef63105f0e9cd67e1c2b4624fc29a336ed17dc1d992989630f9c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OGH6VOZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdgBLmdNZHW25rk9sP9b0BMC7QO9FGkgWPbwNymnBzgIhAJ77wDF8u3EVjP2Pv3zf8E7bbN5vtp%2F3lUHKGz4GKWbZKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfK1%2FceMLa5OquDJcq3AMVMODetpuurR1rKbxbcxNakHdgxIRSShK6iztISpeNZ%2FBCiKPzVCxI%2FrtKKG1EOq5KrQMHRl%2BKafEq3SlYVMelaA2ghdI6Qhgq7IlkQDHb5hVgWzaR%2BlN2eDcobZNStnJagTLBJe5qqjneyiWNpE5N4ix9kJEMEku2Y6EF5r3r5hWgGoR5SpjTIZxGVEwzCt2%2FPNCee55jOoStnApHisWtYvOvfhdxJjrDwvQeg1qJlRaDHeWoX2Ve9slaXTxYN%2FmnkfWeaVGOqXQNvvvDb5MsXNZM9r56ZPb6R%2Fdy1ZXGl0HO4tzMFg3h9YwtwYQxn4ivS62nm%2BB5lAVZLUdUZ7U48%2Boi2BKCGo96XwF%2FCpC1zLP1K7p%2FqlNAG0tVmI%2FXUH1BUHqbhtWaycyawQwG078Rhoa51HEGYCCxRvuNlsCQmKDLYoB%2Fd7w55CIt9ii2PInpMBeue81QkURxz4BsMnfxDE0r7UFazQKf7cfg%2B45Vky%2BdcFVcN8g6ey97aGiROcC4hgOYLd8HaKsJJqPKc0PTfd8uCicFTl36WgHZmjWRrTnGuhHkiUuzWbO9hRPBTVDzDGMNmldR4cQVH%2FdbOzGHOPdxWfp1QQMFAr9lLWrS5%2BfnEaOeYjwTfoDnQTD%2Bsfq8BjqkAV0BUuhYAA4zQmoTQRJldz%2FKDXhqsTezv%2BCUPU9%2Bjv0DP6Ljhj08TkFfkjuEfcmOl95t9NEd%2FqKGkvzA1EFvEF1MN0snaQ9Ncr80qN5n4ihrL2erJt13jvVUwiyKjWWwjgSp6NbmjZ3wGi1QTUxKnXGWK%2FMa4%2BX1gy%2F8jECyoQQrt6sf6B0fzOFfQV7LSW7SQ9J1CpXeQAVK1ighBDN0rK%2BQp3iE&X-Amz-Signature=95cff38296b83d12b193d086e67ed9962d23d6b9fe353b2a4dc7f6e8625020e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OGH6VOZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdgBLmdNZHW25rk9sP9b0BMC7QO9FGkgWPbwNymnBzgIhAJ77wDF8u3EVjP2Pv3zf8E7bbN5vtp%2F3lUHKGz4GKWbZKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfK1%2FceMLa5OquDJcq3AMVMODetpuurR1rKbxbcxNakHdgxIRSShK6iztISpeNZ%2FBCiKPzVCxI%2FrtKKG1EOq5KrQMHRl%2BKafEq3SlYVMelaA2ghdI6Qhgq7IlkQDHb5hVgWzaR%2BlN2eDcobZNStnJagTLBJe5qqjneyiWNpE5N4ix9kJEMEku2Y6EF5r3r5hWgGoR5SpjTIZxGVEwzCt2%2FPNCee55jOoStnApHisWtYvOvfhdxJjrDwvQeg1qJlRaDHeWoX2Ve9slaXTxYN%2FmnkfWeaVGOqXQNvvvDb5MsXNZM9r56ZPb6R%2Fdy1ZXGl0HO4tzMFg3h9YwtwYQxn4ivS62nm%2BB5lAVZLUdUZ7U48%2Boi2BKCGo96XwF%2FCpC1zLP1K7p%2FqlNAG0tVmI%2FXUH1BUHqbhtWaycyawQwG078Rhoa51HEGYCCxRvuNlsCQmKDLYoB%2Fd7w55CIt9ii2PInpMBeue81QkURxz4BsMnfxDE0r7UFazQKf7cfg%2B45Vky%2BdcFVcN8g6ey97aGiROcC4hgOYLd8HaKsJJqPKc0PTfd8uCicFTl36WgHZmjWRrTnGuhHkiUuzWbO9hRPBTVDzDGMNmldR4cQVH%2FdbOzGHOPdxWfp1QQMFAr9lLWrS5%2BfnEaOeYjwTfoDnQTD%2Bsfq8BjqkAV0BUuhYAA4zQmoTQRJldz%2FKDXhqsTezv%2BCUPU9%2Bjv0DP6Ljhj08TkFfkjuEfcmOl95t9NEd%2FqKGkvzA1EFvEF1MN0snaQ9Ncr80qN5n4ihrL2erJt13jvVUwiyKjWWwjgSp6NbmjZ3wGi1QTUxKnXGWK%2FMa4%2BX1gy%2F8jECyoQQrt6sf6B0fzOFfQV7LSW7SQ9J1CpXeQAVK1ighBDN0rK%2BQp3iE&X-Amz-Signature=0e35adb2ffa668eaac90625c394eb37d4bd8139333052606f4a35821e6c0b7e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OGH6VOZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdgBLmdNZHW25rk9sP9b0BMC7QO9FGkgWPbwNymnBzgIhAJ77wDF8u3EVjP2Pv3zf8E7bbN5vtp%2F3lUHKGz4GKWbZKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfK1%2FceMLa5OquDJcq3AMVMODetpuurR1rKbxbcxNakHdgxIRSShK6iztISpeNZ%2FBCiKPzVCxI%2FrtKKG1EOq5KrQMHRl%2BKafEq3SlYVMelaA2ghdI6Qhgq7IlkQDHb5hVgWzaR%2BlN2eDcobZNStnJagTLBJe5qqjneyiWNpE5N4ix9kJEMEku2Y6EF5r3r5hWgGoR5SpjTIZxGVEwzCt2%2FPNCee55jOoStnApHisWtYvOvfhdxJjrDwvQeg1qJlRaDHeWoX2Ve9slaXTxYN%2FmnkfWeaVGOqXQNvvvDb5MsXNZM9r56ZPb6R%2Fdy1ZXGl0HO4tzMFg3h9YwtwYQxn4ivS62nm%2BB5lAVZLUdUZ7U48%2Boi2BKCGo96XwF%2FCpC1zLP1K7p%2FqlNAG0tVmI%2FXUH1BUHqbhtWaycyawQwG078Rhoa51HEGYCCxRvuNlsCQmKDLYoB%2Fd7w55CIt9ii2PInpMBeue81QkURxz4BsMnfxDE0r7UFazQKf7cfg%2B45Vky%2BdcFVcN8g6ey97aGiROcC4hgOYLd8HaKsJJqPKc0PTfd8uCicFTl36WgHZmjWRrTnGuhHkiUuzWbO9hRPBTVDzDGMNmldR4cQVH%2FdbOzGHOPdxWfp1QQMFAr9lLWrS5%2BfnEaOeYjwTfoDnQTD%2Bsfq8BjqkAV0BUuhYAA4zQmoTQRJldz%2FKDXhqsTezv%2BCUPU9%2Bjv0DP6Ljhj08TkFfkjuEfcmOl95t9NEd%2FqKGkvzA1EFvEF1MN0snaQ9Ncr80qN5n4ihrL2erJt13jvVUwiyKjWWwjgSp6NbmjZ3wGi1QTUxKnXGWK%2FMa4%2BX1gy%2F8jECyoQQrt6sf6B0fzOFfQV7LSW7SQ9J1CpXeQAVK1ighBDN0rK%2BQp3iE&X-Amz-Signature=417a632e3dbe4eac3c8e526a93278a3ba83c7a6a0605df796ea92d33fc5bfe07&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OGH6VOZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdgBLmdNZHW25rk9sP9b0BMC7QO9FGkgWPbwNymnBzgIhAJ77wDF8u3EVjP2Pv3zf8E7bbN5vtp%2F3lUHKGz4GKWbZKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfK1%2FceMLa5OquDJcq3AMVMODetpuurR1rKbxbcxNakHdgxIRSShK6iztISpeNZ%2FBCiKPzVCxI%2FrtKKG1EOq5KrQMHRl%2BKafEq3SlYVMelaA2ghdI6Qhgq7IlkQDHb5hVgWzaR%2BlN2eDcobZNStnJagTLBJe5qqjneyiWNpE5N4ix9kJEMEku2Y6EF5r3r5hWgGoR5SpjTIZxGVEwzCt2%2FPNCee55jOoStnApHisWtYvOvfhdxJjrDwvQeg1qJlRaDHeWoX2Ve9slaXTxYN%2FmnkfWeaVGOqXQNvvvDb5MsXNZM9r56ZPb6R%2Fdy1ZXGl0HO4tzMFg3h9YwtwYQxn4ivS62nm%2BB5lAVZLUdUZ7U48%2Boi2BKCGo96XwF%2FCpC1zLP1K7p%2FqlNAG0tVmI%2FXUH1BUHqbhtWaycyawQwG078Rhoa51HEGYCCxRvuNlsCQmKDLYoB%2Fd7w55CIt9ii2PInpMBeue81QkURxz4BsMnfxDE0r7UFazQKf7cfg%2B45Vky%2BdcFVcN8g6ey97aGiROcC4hgOYLd8HaKsJJqPKc0PTfd8uCicFTl36WgHZmjWRrTnGuhHkiUuzWbO9hRPBTVDzDGMNmldR4cQVH%2FdbOzGHOPdxWfp1QQMFAr9lLWrS5%2BfnEaOeYjwTfoDnQTD%2Bsfq8BjqkAV0BUuhYAA4zQmoTQRJldz%2FKDXhqsTezv%2BCUPU9%2Bjv0DP6Ljhj08TkFfkjuEfcmOl95t9NEd%2FqKGkvzA1EFvEF1MN0snaQ9Ncr80qN5n4ihrL2erJt13jvVUwiyKjWWwjgSp6NbmjZ3wGi1QTUxKnXGWK%2FMa4%2BX1gy%2F8jECyoQQrt6sf6B0fzOFfQV7LSW7SQ9J1CpXeQAVK1ighBDN0rK%2BQp3iE&X-Amz-Signature=7157ee3598665f95fd4fedaa8d59df6daaf0a529c468c1a004f700f409a3cc16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OGH6VOZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdgBLmdNZHW25rk9sP9b0BMC7QO9FGkgWPbwNymnBzgIhAJ77wDF8u3EVjP2Pv3zf8E7bbN5vtp%2F3lUHKGz4GKWbZKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfK1%2FceMLa5OquDJcq3AMVMODetpuurR1rKbxbcxNakHdgxIRSShK6iztISpeNZ%2FBCiKPzVCxI%2FrtKKG1EOq5KrQMHRl%2BKafEq3SlYVMelaA2ghdI6Qhgq7IlkQDHb5hVgWzaR%2BlN2eDcobZNStnJagTLBJe5qqjneyiWNpE5N4ix9kJEMEku2Y6EF5r3r5hWgGoR5SpjTIZxGVEwzCt2%2FPNCee55jOoStnApHisWtYvOvfhdxJjrDwvQeg1qJlRaDHeWoX2Ve9slaXTxYN%2FmnkfWeaVGOqXQNvvvDb5MsXNZM9r56ZPb6R%2Fdy1ZXGl0HO4tzMFg3h9YwtwYQxn4ivS62nm%2BB5lAVZLUdUZ7U48%2Boi2BKCGo96XwF%2FCpC1zLP1K7p%2FqlNAG0tVmI%2FXUH1BUHqbhtWaycyawQwG078Rhoa51HEGYCCxRvuNlsCQmKDLYoB%2Fd7w55CIt9ii2PInpMBeue81QkURxz4BsMnfxDE0r7UFazQKf7cfg%2B45Vky%2BdcFVcN8g6ey97aGiROcC4hgOYLd8HaKsJJqPKc0PTfd8uCicFTl36WgHZmjWRrTnGuhHkiUuzWbO9hRPBTVDzDGMNmldR4cQVH%2FdbOzGHOPdxWfp1QQMFAr9lLWrS5%2BfnEaOeYjwTfoDnQTD%2Bsfq8BjqkAV0BUuhYAA4zQmoTQRJldz%2FKDXhqsTezv%2BCUPU9%2Bjv0DP6Ljhj08TkFfkjuEfcmOl95t9NEd%2FqKGkvzA1EFvEF1MN0snaQ9Ncr80qN5n4ihrL2erJt13jvVUwiyKjWWwjgSp6NbmjZ3wGi1QTUxKnXGWK%2FMa4%2BX1gy%2F8jECyoQQrt6sf6B0fzOFfQV7LSW7SQ9J1CpXeQAVK1ighBDN0rK%2BQp3iE&X-Amz-Signature=c7e34b732d3bdb9689bc1b8d2bc060b169dd3d2bef470647fba0223be9012e64&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OGH6VOZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCdgBLmdNZHW25rk9sP9b0BMC7QO9FGkgWPbwNymnBzgIhAJ77wDF8u3EVjP2Pv3zf8E7bbN5vtp%2F3lUHKGz4GKWbZKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwfK1%2FceMLa5OquDJcq3AMVMODetpuurR1rKbxbcxNakHdgxIRSShK6iztISpeNZ%2FBCiKPzVCxI%2FrtKKG1EOq5KrQMHRl%2BKafEq3SlYVMelaA2ghdI6Qhgq7IlkQDHb5hVgWzaR%2BlN2eDcobZNStnJagTLBJe5qqjneyiWNpE5N4ix9kJEMEku2Y6EF5r3r5hWgGoR5SpjTIZxGVEwzCt2%2FPNCee55jOoStnApHisWtYvOvfhdxJjrDwvQeg1qJlRaDHeWoX2Ve9slaXTxYN%2FmnkfWeaVGOqXQNvvvDb5MsXNZM9r56ZPb6R%2Fdy1ZXGl0HO4tzMFg3h9YwtwYQxn4ivS62nm%2BB5lAVZLUdUZ7U48%2Boi2BKCGo96XwF%2FCpC1zLP1K7p%2FqlNAG0tVmI%2FXUH1BUHqbhtWaycyawQwG078Rhoa51HEGYCCxRvuNlsCQmKDLYoB%2Fd7w55CIt9ii2PInpMBeue81QkURxz4BsMnfxDE0r7UFazQKf7cfg%2B45Vky%2BdcFVcN8g6ey97aGiROcC4hgOYLd8HaKsJJqPKc0PTfd8uCicFTl36WgHZmjWRrTnGuhHkiUuzWbO9hRPBTVDzDGMNmldR4cQVH%2FdbOzGHOPdxWfp1QQMFAr9lLWrS5%2BfnEaOeYjwTfoDnQTD%2Bsfq8BjqkAV0BUuhYAA4zQmoTQRJldz%2FKDXhqsTezv%2BCUPU9%2Bjv0DP6Ljhj08TkFfkjuEfcmOl95t9NEd%2FqKGkvzA1EFvEF1MN0snaQ9Ncr80qN5n4ihrL2erJt13jvVUwiyKjWWwjgSp6NbmjZ3wGi1QTUxKnXGWK%2FMa4%2BX1gy%2F8jECyoQQrt6sf6B0fzOFfQV7LSW7SQ9J1CpXeQAVK1ighBDN0rK%2BQp3iE&X-Amz-Signature=7d8234f87255088a19acabcba2d0ec10a57a53263629a4e71ce3b990d1887cf0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZTV625G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeV7nt7TjpBkrFQTlDgcuf8XD6kKI7W1NmF7ZyVpV%2FCwIgENGdUSa0N3jHlMrY9MyDkIMTjKLqBtbqCaJE0VSpWYcqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBVjj3D2ltcWQGxMcircA2R1gbPjx%2FPbFRBBUI9H6XrKkjZhuoNsY0iLhsY0ASg4%2F2STb3TxTimY1dQfC0RC4k%2FliVxNvULA4gbgg3esN51gX9ADWARcXt5JDqA60o8qSh0CGZnFCRjliUKYHlakEylTefPw5lhycLM2n3ElacrJr8y2cSj%2FODeOBJee0dlnvJbhoSdb1AOeu4bBTdoOKihUgkPtEXQPq9FUzlU1BQBllaSszW9LjN%2Bau4F0ZJkrkzSpE6Pbt%2B7qO3WyiyQMaFpZzl%2FOvDi8epFwUF5FZPsbACbIWR8tgsy313LHhw6qgVrKTwNdB3EGufooUwbnvlzkMFKjER60%2BTZTj0Z89w7VlUaIm9Mxhzl%2F2dYVfYRsSYeX6fLXDzf7f0yhOIi%2BzpMdRXvuJN9t%2FIPHOIFAEDSb1xg27YkQx5EKLzTP%2BJaDGNarfS4w75CuUWdIbdGgVMhYZzECgmd2VBsVguccMIUz%2B%2F%2Bm8s2DJD3d95TRvo2OutcUf2hATz%2Fq13y6uIAqVcRc1I89x4PBqZzqYNFVxzMnV1n1rIEZubBqB%2FlGh0z5csHAUc3FkONccffI3By3JOcVgbIvPW9%2BCJG6lPlse6FK3wJDW5L%2BBEAMwgVuKqpVhdeEa9Z%2BdA7jYsaBMPew%2BrwGOqUBgzC8FvS80TjA1qgS8j9b2Aa9rAVozeZquurXiqUB2%2BBzhE1iQ3EQAvl0mt4g5A4aE243GH9339Z1S3qLnFsapWPNMP8LOPElQgHVRAq%2F4cKJ9r1GXBP7P6orNE2EZJauPq9reb5DWApQ3Iv2L8SNGsdQUCgZmrV7KkKWNu2XrTC3EcamH6X6IO8PjTG8WS3grRyoRh7mX1dZDn0VsqDoSznuwM2%2B&X-Amz-Signature=1cab5897ea716cf6aede737f0cc1f5c0f4d752d4b3254c4cfc1ed3d3863ddd57&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFGHFT7C%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDw5WPwgmk0Cp4%2FhChCglsRlsV0qoVsnyUigij9scxVpAiEAsN80i90zIFWqPxcKMoQqfdEospFi9ZJLDK%2FmzA0IXcUqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtskXK5VLhngiJffSrcA8bkf6NRSWcZy1mPelaU%2B5TZJbUlOt4M%2FPvuwIkhjXptPlO5D3CsIKJFADrY1gzUNEYOim0hwYpLqBojTcPukRVJi90p4VXnPltSD3dVLkp4S5%2Fr8x32PvKePGJ9kQ6hi3mBE0EsFlc%2BgzhQTdaJJqgxXCmf3ptXfZHwFXp3WtE0LjF3Pdw57%2Fqic%2FQNFFXaobYqKaS6abroOn2DDWP7sWOT43WkV5vcfWCeLg9%2FZHiv57Ihe0jwz4AHkgmS7poabPrKzq2oVyBPjXPny3bMNUK93pxMfv9cyXqAYOQzJ0Z20qePlnhgf12a5eteh75Sz0NczkA0vqiBnjY3BZC94upmAwO3mTBvjoa02q1Ol7NdF7vDypAAFUTUDcCuI9Uu4QtSGJhwoGXFx%2B3sRPpwh7HQd50Y4M2tbtpXvW%2B259RHTG%2Bwua7KU9dfecJWwxhIN2kUUpSRqvNlP5oVvdYy3%2F1QjeDU%2BA19DxylMOV%2F1X98WlAtansQ8K9kfR6mE6Ja4FpMl1asVVQ7FHewewLQeTbkwobQhuLz3%2BBn5ReKJjkx6LVfiNpIGJWZ1Ua2Blo1fwJKRoI8%2BE0Lgzkw8rMtPBOM%2B%2F9IH4bi3Ki1oRQ9Cascg4KIeq%2BZt7Q48ppiMKex%2BrwGOqUBhp8jZzlIqv3vP%2BU%2FGpSoKwH%2BnKn4GbDKOMP245AMo3AebOfMhjdv9a5jROQpbDMgiL%2F%2FvLmZYL%2FlCsZLdKD02XhsyPutVD4qjTp50mXcGYxy4YSLCdGEJWjT2xQA3ZC4SMbM0rzugnsufl%2Bb%2BZIcWVcMrhhUecZDl8h%2F3Ns%2FfiIc22M4kIml0kg7WGEHUa0ArqDWrVU6kHhcRLoeeiU8xtsTtWg6&X-Amz-Signature=4c5901a147f4e6bb5a16b145884febe257fcf70ad5b51b91c554082870e4a169&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DM7JQAW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfUfjnuml7tJHRJEJF3XKOs47W9ZUVmQaWfCdzC3WcQwIhANx6R0qrpT7wcuZY%2FBqOSQqmld2gF5Ux%2B2cE6hoTf6X8KogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyDhwKNlW3ibCczQHoq3ANfjz4ASx4PQg7Ch7H4y9GKwMEtRNHXiZia16Zc81SFLb9OvTUIOZ0bqrqfHC3pGZYSy9PB7Iu%2FaJ83EP9G4%2F1C0fPVUV9cUA4AfDAb%2FQxbg%2BJOH5KmVRonqk%2Fozk5xssYZjkCZ2esDb4nxVO1TbUbPusw2XmN%2BBoO0aDypKNQ5XUm5L3aK7YkPwmVe1VsmKq7X5sH8ySS5WAWBEpNzglSCVd%2Fn6nZ5YRUwj6hDUbK9mR9trFwnHfCCmGnnOBpUJv8N0RvH27vw5YFAEeyJhPdA593wrWn96RfZ%2B%2B%2FGeEbk9R67F6f8XtUiCmAOFSDNiybQGsZUooHa%2Fz9bg9dVQjx%2BA3MksLzkTBgd8cnlMmFklgoyjOUDpu%2F%2Fbcs0O%2BXU3K8xnElbzGqFmvRcRmkI2aKNnqmqfXSWc4TdYQV2Orm7HKaXeMOIpiYbCFiUHwbzyWtaP9UdWpnCGtgJgEGYwVk3joPv5vSaxWojMbsz3x%2FjMU1uoNwGD1bdE42fuWjusouznQw9WfoqwpGIScEO0xm8u1xH7sg2DpXzaSE3brcyaiUheCpucty9OB4ydhck7opi8MZLX0f7tCRA5HlJcVCEFzNpHHRhrfyjtEFfYcqLxAsg1CNy4OMlp%2F54AzD1sPq8BjqkAc4OF0fEnw%2FPai44ufDDgd695jvg133Xbn3%2Fk3lRbSe0DBdKp6%2BQy12gGzxdYtDvU%2BIBf%2BBnQCF4sd38D6K0BGk5lrwbbuvHapL8onoiY3E3gbrqJdX7DlfK7J1Z%2FKVbeUIv89XE77DDio8%2B9R63N%2F0uKQdCfA%2F5s0ISYcNjTfLS2U7C%2Fj0ZU7IZDHZMJwJEkdH1bL%2Fzr8e%2BcJ31veeCnTzK52%2FR&X-Amz-Signature=bd27cd4989a3d82ffbd7a9243e2cc78e2bfea07836336688fc66a8baf51a4c72&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DM7JQAW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfUfjnuml7tJHRJEJF3XKOs47W9ZUVmQaWfCdzC3WcQwIhANx6R0qrpT7wcuZY%2FBqOSQqmld2gF5Ux%2B2cE6hoTf6X8KogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyDhwKNlW3ibCczQHoq3ANfjz4ASx4PQg7Ch7H4y9GKwMEtRNHXiZia16Zc81SFLb9OvTUIOZ0bqrqfHC3pGZYSy9PB7Iu%2FaJ83EP9G4%2F1C0fPVUV9cUA4AfDAb%2FQxbg%2BJOH5KmVRonqk%2Fozk5xssYZjkCZ2esDb4nxVO1TbUbPusw2XmN%2BBoO0aDypKNQ5XUm5L3aK7YkPwmVe1VsmKq7X5sH8ySS5WAWBEpNzglSCVd%2Fn6nZ5YRUwj6hDUbK9mR9trFwnHfCCmGnnOBpUJv8N0RvH27vw5YFAEeyJhPdA593wrWn96RfZ%2B%2B%2FGeEbk9R67F6f8XtUiCmAOFSDNiybQGsZUooHa%2Fz9bg9dVQjx%2BA3MksLzkTBgd8cnlMmFklgoyjOUDpu%2F%2Fbcs0O%2BXU3K8xnElbzGqFmvRcRmkI2aKNnqmqfXSWc4TdYQV2Orm7HKaXeMOIpiYbCFiUHwbzyWtaP9UdWpnCGtgJgEGYwVk3joPv5vSaxWojMbsz3x%2FjMU1uoNwGD1bdE42fuWjusouznQw9WfoqwpGIScEO0xm8u1xH7sg2DpXzaSE3brcyaiUheCpucty9OB4ydhck7opi8MZLX0f7tCRA5HlJcVCEFzNpHHRhrfyjtEFfYcqLxAsg1CNy4OMlp%2F54AzD1sPq8BjqkAc4OF0fEnw%2FPai44ufDDgd695jvg133Xbn3%2Fk3lRbSe0DBdKp6%2BQy12gGzxdYtDvU%2BIBf%2BBnQCF4sd38D6K0BGk5lrwbbuvHapL8onoiY3E3gbrqJdX7DlfK7J1Z%2FKVbeUIv89XE77DDio8%2B9R63N%2F0uKQdCfA%2F5s0ISYcNjTfLS2U7C%2Fj0ZU7IZDHZMJwJEkdH1bL%2Fzr8e%2BcJ31veeCnTzK52%2FR&X-Amz-Signature=5a03f06d143b870674bc030d6f029dfc1edce06c63c65a613acdb0b8b6a0f659&X-Amz-SignedHeaders=host&x-id=GetObject)
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
