

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6JTPLXY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAKxdXj95rVdr0r705Kdzt1B9%2Bk3RjUwKfmsJHq9klTcAiAgT%2F%2FoxjC0IgsuF6yrcjwl3JbojtQJM04lAx0EhrisJir%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIM%2FZ15Jox5sKqURa%2BNKtwD0vAEFB8jbukiGFYzhlRX%2Fz0S%2BzIXon50UdyIGE3sr7BHd%2Fhx0peVit59SsZQW8wH0Zj90cincg35JJnG%2Fxgc9zvzv%2BPQL7l9%2F49dcHkr9ZYmTIBXygdMbg%2FAfHKfMmCgzXfcUI5fbuTuywwHC3yXfJ0vodIUAtsrt55uDEHtezNgq%2Bq%2Bo%2FLQnM1OCt60ZhWtZm0sny4KVpnqTf8Ect9R3jQ56EWcUDcsQclNSMkooi12nPy9P92iPBW3WTAP%2FH0grPX6F5Vh%2BR6RGtR3bx65pWnYrjvC1dLOjJ%2FqyTqQwZr3z57O4ny61%2BNuRjjYJCJ4GGlMkJgLG6JyG0lOqiHv8xSMrkFvrMBx3JpiyQh9zEyVcHsWw5VFsECSwmZzP97PUDt3tIGcMQQVl1hBrqUfoCEUPT14kGoCQfBz1gMhtowvDQfTlwlHoS4WXBo5Fi2VOqFthEpuZDJSb1w6Mu6I%2Fj3UJM0gH%2BSsXDqer%2BdqHcRlWGREYqwmOh326ROCWfBCjG5StA5nCH%2Bsf3Y%2Bk7mXut8HME8bSC3ugyVQ2%2BQ2H4DqbPu3p3cqtmdYK0VkVdR%2F3sKxLL4r9mkiWBFgJdklXKNgHS2hyaVahaLGglPh4REV7SDV1fyt59Ii7nMw7oKIvQY6pgHTXTXHjkJ6pssTeBiW7%2FCA9tIYAw0SR%2BlGp4oCDb1feBAPmMTgE500yquM%2FBJatWJxSJl0X%2BmsgkXVDE6ts%2B5g4bixLSTL0mTqUw9zrkKqhLKL2aqlSklIYZUD4EbCJOi8OJH0IcOm%2B8IW2oYTgRYjDo%2BQeJ58p5hzZw0mAkW8nQ2ntcIdqoX6uTA6OEkYIZ1CeSQ2ZecrCWlXqw2LT%2F4YxVPJmQO4&X-Amz-Signature=f8a1697b5329fcd8bc90ec075a5f5d6545254d69ec4fff4148b5e3fc8548b4cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6JTPLXY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAKxdXj95rVdr0r705Kdzt1B9%2Bk3RjUwKfmsJHq9klTcAiAgT%2F%2FoxjC0IgsuF6yrcjwl3JbojtQJM04lAx0EhrisJir%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIM%2FZ15Jox5sKqURa%2BNKtwD0vAEFB8jbukiGFYzhlRX%2Fz0S%2BzIXon50UdyIGE3sr7BHd%2Fhx0peVit59SsZQW8wH0Zj90cincg35JJnG%2Fxgc9zvzv%2BPQL7l9%2F49dcHkr9ZYmTIBXygdMbg%2FAfHKfMmCgzXfcUI5fbuTuywwHC3yXfJ0vodIUAtsrt55uDEHtezNgq%2Bq%2Bo%2FLQnM1OCt60ZhWtZm0sny4KVpnqTf8Ect9R3jQ56EWcUDcsQclNSMkooi12nPy9P92iPBW3WTAP%2FH0grPX6F5Vh%2BR6RGtR3bx65pWnYrjvC1dLOjJ%2FqyTqQwZr3z57O4ny61%2BNuRjjYJCJ4GGlMkJgLG6JyG0lOqiHv8xSMrkFvrMBx3JpiyQh9zEyVcHsWw5VFsECSwmZzP97PUDt3tIGcMQQVl1hBrqUfoCEUPT14kGoCQfBz1gMhtowvDQfTlwlHoS4WXBo5Fi2VOqFthEpuZDJSb1w6Mu6I%2Fj3UJM0gH%2BSsXDqer%2BdqHcRlWGREYqwmOh326ROCWfBCjG5StA5nCH%2Bsf3Y%2Bk7mXut8HME8bSC3ugyVQ2%2BQ2H4DqbPu3p3cqtmdYK0VkVdR%2F3sKxLL4r9mkiWBFgJdklXKNgHS2hyaVahaLGglPh4REV7SDV1fyt59Ii7nMw7oKIvQY6pgHTXTXHjkJ6pssTeBiW7%2FCA9tIYAw0SR%2BlGp4oCDb1feBAPmMTgE500yquM%2FBJatWJxSJl0X%2BmsgkXVDE6ts%2B5g4bixLSTL0mTqUw9zrkKqhLKL2aqlSklIYZUD4EbCJOi8OJH0IcOm%2B8IW2oYTgRYjDo%2BQeJ58p5hzZw0mAkW8nQ2ntcIdqoX6uTA6OEkYIZ1CeSQ2ZecrCWlXqw2LT%2F4YxVPJmQO4&X-Amz-Signature=f4772156489826093d85a3566f50648aed8a5a284b0022c7fd09a158a9f773c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6JTPLXY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAKxdXj95rVdr0r705Kdzt1B9%2Bk3RjUwKfmsJHq9klTcAiAgT%2F%2FoxjC0IgsuF6yrcjwl3JbojtQJM04lAx0EhrisJir%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIM%2FZ15Jox5sKqURa%2BNKtwD0vAEFB8jbukiGFYzhlRX%2Fz0S%2BzIXon50UdyIGE3sr7BHd%2Fhx0peVit59SsZQW8wH0Zj90cincg35JJnG%2Fxgc9zvzv%2BPQL7l9%2F49dcHkr9ZYmTIBXygdMbg%2FAfHKfMmCgzXfcUI5fbuTuywwHC3yXfJ0vodIUAtsrt55uDEHtezNgq%2Bq%2Bo%2FLQnM1OCt60ZhWtZm0sny4KVpnqTf8Ect9R3jQ56EWcUDcsQclNSMkooi12nPy9P92iPBW3WTAP%2FH0grPX6F5Vh%2BR6RGtR3bx65pWnYrjvC1dLOjJ%2FqyTqQwZr3z57O4ny61%2BNuRjjYJCJ4GGlMkJgLG6JyG0lOqiHv8xSMrkFvrMBx3JpiyQh9zEyVcHsWw5VFsECSwmZzP97PUDt3tIGcMQQVl1hBrqUfoCEUPT14kGoCQfBz1gMhtowvDQfTlwlHoS4WXBo5Fi2VOqFthEpuZDJSb1w6Mu6I%2Fj3UJM0gH%2BSsXDqer%2BdqHcRlWGREYqwmOh326ROCWfBCjG5StA5nCH%2Bsf3Y%2Bk7mXut8HME8bSC3ugyVQ2%2BQ2H4DqbPu3p3cqtmdYK0VkVdR%2F3sKxLL4r9mkiWBFgJdklXKNgHS2hyaVahaLGglPh4REV7SDV1fyt59Ii7nMw7oKIvQY6pgHTXTXHjkJ6pssTeBiW7%2FCA9tIYAw0SR%2BlGp4oCDb1feBAPmMTgE500yquM%2FBJatWJxSJl0X%2BmsgkXVDE6ts%2B5g4bixLSTL0mTqUw9zrkKqhLKL2aqlSklIYZUD4EbCJOi8OJH0IcOm%2B8IW2oYTgRYjDo%2BQeJ58p5hzZw0mAkW8nQ2ntcIdqoX6uTA6OEkYIZ1CeSQ2ZecrCWlXqw2LT%2F4YxVPJmQO4&X-Amz-Signature=e73baccccf89b81ada4a73f9f2d3efd4c893dbf35e63803ffdfbc23b3c04bfaf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6JTPLXY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAKxdXj95rVdr0r705Kdzt1B9%2Bk3RjUwKfmsJHq9klTcAiAgT%2F%2FoxjC0IgsuF6yrcjwl3JbojtQJM04lAx0EhrisJir%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIM%2FZ15Jox5sKqURa%2BNKtwD0vAEFB8jbukiGFYzhlRX%2Fz0S%2BzIXon50UdyIGE3sr7BHd%2Fhx0peVit59SsZQW8wH0Zj90cincg35JJnG%2Fxgc9zvzv%2BPQL7l9%2F49dcHkr9ZYmTIBXygdMbg%2FAfHKfMmCgzXfcUI5fbuTuywwHC3yXfJ0vodIUAtsrt55uDEHtezNgq%2Bq%2Bo%2FLQnM1OCt60ZhWtZm0sny4KVpnqTf8Ect9R3jQ56EWcUDcsQclNSMkooi12nPy9P92iPBW3WTAP%2FH0grPX6F5Vh%2BR6RGtR3bx65pWnYrjvC1dLOjJ%2FqyTqQwZr3z57O4ny61%2BNuRjjYJCJ4GGlMkJgLG6JyG0lOqiHv8xSMrkFvrMBx3JpiyQh9zEyVcHsWw5VFsECSwmZzP97PUDt3tIGcMQQVl1hBrqUfoCEUPT14kGoCQfBz1gMhtowvDQfTlwlHoS4WXBo5Fi2VOqFthEpuZDJSb1w6Mu6I%2Fj3UJM0gH%2BSsXDqer%2BdqHcRlWGREYqwmOh326ROCWfBCjG5StA5nCH%2Bsf3Y%2Bk7mXut8HME8bSC3ugyVQ2%2BQ2H4DqbPu3p3cqtmdYK0VkVdR%2F3sKxLL4r9mkiWBFgJdklXKNgHS2hyaVahaLGglPh4REV7SDV1fyt59Ii7nMw7oKIvQY6pgHTXTXHjkJ6pssTeBiW7%2FCA9tIYAw0SR%2BlGp4oCDb1feBAPmMTgE500yquM%2FBJatWJxSJl0X%2BmsgkXVDE6ts%2B5g4bixLSTL0mTqUw9zrkKqhLKL2aqlSklIYZUD4EbCJOi8OJH0IcOm%2B8IW2oYTgRYjDo%2BQeJ58p5hzZw0mAkW8nQ2ntcIdqoX6uTA6OEkYIZ1CeSQ2ZecrCWlXqw2LT%2F4YxVPJmQO4&X-Amz-Signature=5e7facd3f8aac7f512fe783e7af6e693fc63f4c8e830d0179217927916c424ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6JTPLXY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAKxdXj95rVdr0r705Kdzt1B9%2Bk3RjUwKfmsJHq9klTcAiAgT%2F%2FoxjC0IgsuF6yrcjwl3JbojtQJM04lAx0EhrisJir%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIM%2FZ15Jox5sKqURa%2BNKtwD0vAEFB8jbukiGFYzhlRX%2Fz0S%2BzIXon50UdyIGE3sr7BHd%2Fhx0peVit59SsZQW8wH0Zj90cincg35JJnG%2Fxgc9zvzv%2BPQL7l9%2F49dcHkr9ZYmTIBXygdMbg%2FAfHKfMmCgzXfcUI5fbuTuywwHC3yXfJ0vodIUAtsrt55uDEHtezNgq%2Bq%2Bo%2FLQnM1OCt60ZhWtZm0sny4KVpnqTf8Ect9R3jQ56EWcUDcsQclNSMkooi12nPy9P92iPBW3WTAP%2FH0grPX6F5Vh%2BR6RGtR3bx65pWnYrjvC1dLOjJ%2FqyTqQwZr3z57O4ny61%2BNuRjjYJCJ4GGlMkJgLG6JyG0lOqiHv8xSMrkFvrMBx3JpiyQh9zEyVcHsWw5VFsECSwmZzP97PUDt3tIGcMQQVl1hBrqUfoCEUPT14kGoCQfBz1gMhtowvDQfTlwlHoS4WXBo5Fi2VOqFthEpuZDJSb1w6Mu6I%2Fj3UJM0gH%2BSsXDqer%2BdqHcRlWGREYqwmOh326ROCWfBCjG5StA5nCH%2Bsf3Y%2Bk7mXut8HME8bSC3ugyVQ2%2BQ2H4DqbPu3p3cqtmdYK0VkVdR%2F3sKxLL4r9mkiWBFgJdklXKNgHS2hyaVahaLGglPh4REV7SDV1fyt59Ii7nMw7oKIvQY6pgHTXTXHjkJ6pssTeBiW7%2FCA9tIYAw0SR%2BlGp4oCDb1feBAPmMTgE500yquM%2FBJatWJxSJl0X%2BmsgkXVDE6ts%2B5g4bixLSTL0mTqUw9zrkKqhLKL2aqlSklIYZUD4EbCJOi8OJH0IcOm%2B8IW2oYTgRYjDo%2BQeJ58p5hzZw0mAkW8nQ2ntcIdqoX6uTA6OEkYIZ1CeSQ2ZecrCWlXqw2LT%2F4YxVPJmQO4&X-Amz-Signature=0f6c86e4406ee9d5694e0fa20e53d3687fb71453d9a3ff6600410a4adec59c65&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6JTPLXY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAKxdXj95rVdr0r705Kdzt1B9%2Bk3RjUwKfmsJHq9klTcAiAgT%2F%2FoxjC0IgsuF6yrcjwl3JbojtQJM04lAx0EhrisJir%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIM%2FZ15Jox5sKqURa%2BNKtwD0vAEFB8jbukiGFYzhlRX%2Fz0S%2BzIXon50UdyIGE3sr7BHd%2Fhx0peVit59SsZQW8wH0Zj90cincg35JJnG%2Fxgc9zvzv%2BPQL7l9%2F49dcHkr9ZYmTIBXygdMbg%2FAfHKfMmCgzXfcUI5fbuTuywwHC3yXfJ0vodIUAtsrt55uDEHtezNgq%2Bq%2Bo%2FLQnM1OCt60ZhWtZm0sny4KVpnqTf8Ect9R3jQ56EWcUDcsQclNSMkooi12nPy9P92iPBW3WTAP%2FH0grPX6F5Vh%2BR6RGtR3bx65pWnYrjvC1dLOjJ%2FqyTqQwZr3z57O4ny61%2BNuRjjYJCJ4GGlMkJgLG6JyG0lOqiHv8xSMrkFvrMBx3JpiyQh9zEyVcHsWw5VFsECSwmZzP97PUDt3tIGcMQQVl1hBrqUfoCEUPT14kGoCQfBz1gMhtowvDQfTlwlHoS4WXBo5Fi2VOqFthEpuZDJSb1w6Mu6I%2Fj3UJM0gH%2BSsXDqer%2BdqHcRlWGREYqwmOh326ROCWfBCjG5StA5nCH%2Bsf3Y%2Bk7mXut8HME8bSC3ugyVQ2%2BQ2H4DqbPu3p3cqtmdYK0VkVdR%2F3sKxLL4r9mkiWBFgJdklXKNgHS2hyaVahaLGglPh4REV7SDV1fyt59Ii7nMw7oKIvQY6pgHTXTXHjkJ6pssTeBiW7%2FCA9tIYAw0SR%2BlGp4oCDb1feBAPmMTgE500yquM%2FBJatWJxSJl0X%2BmsgkXVDE6ts%2B5g4bixLSTL0mTqUw9zrkKqhLKL2aqlSklIYZUD4EbCJOi8OJH0IcOm%2B8IW2oYTgRYjDo%2BQeJ58p5hzZw0mAkW8nQ2ntcIdqoX6uTA6OEkYIZ1CeSQ2ZecrCWlXqw2LT%2F4YxVPJmQO4&X-Amz-Signature=90574002402bd7f77901deac7d6ed2e7940abbf19157393d863f87bdc1dc8477&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6JTPLXY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAKxdXj95rVdr0r705Kdzt1B9%2Bk3RjUwKfmsJHq9klTcAiAgT%2F%2FoxjC0IgsuF6yrcjwl3JbojtQJM04lAx0EhrisJir%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIM%2FZ15Jox5sKqURa%2BNKtwD0vAEFB8jbukiGFYzhlRX%2Fz0S%2BzIXon50UdyIGE3sr7BHd%2Fhx0peVit59SsZQW8wH0Zj90cincg35JJnG%2Fxgc9zvzv%2BPQL7l9%2F49dcHkr9ZYmTIBXygdMbg%2FAfHKfMmCgzXfcUI5fbuTuywwHC3yXfJ0vodIUAtsrt55uDEHtezNgq%2Bq%2Bo%2FLQnM1OCt60ZhWtZm0sny4KVpnqTf8Ect9R3jQ56EWcUDcsQclNSMkooi12nPy9P92iPBW3WTAP%2FH0grPX6F5Vh%2BR6RGtR3bx65pWnYrjvC1dLOjJ%2FqyTqQwZr3z57O4ny61%2BNuRjjYJCJ4GGlMkJgLG6JyG0lOqiHv8xSMrkFvrMBx3JpiyQh9zEyVcHsWw5VFsECSwmZzP97PUDt3tIGcMQQVl1hBrqUfoCEUPT14kGoCQfBz1gMhtowvDQfTlwlHoS4WXBo5Fi2VOqFthEpuZDJSb1w6Mu6I%2Fj3UJM0gH%2BSsXDqer%2BdqHcRlWGREYqwmOh326ROCWfBCjG5StA5nCH%2Bsf3Y%2Bk7mXut8HME8bSC3ugyVQ2%2BQ2H4DqbPu3p3cqtmdYK0VkVdR%2F3sKxLL4r9mkiWBFgJdklXKNgHS2hyaVahaLGglPh4REV7SDV1fyt59Ii7nMw7oKIvQY6pgHTXTXHjkJ6pssTeBiW7%2FCA9tIYAw0SR%2BlGp4oCDb1feBAPmMTgE500yquM%2FBJatWJxSJl0X%2BmsgkXVDE6ts%2B5g4bixLSTL0mTqUw9zrkKqhLKL2aqlSklIYZUD4EbCJOi8OJH0IcOm%2B8IW2oYTgRYjDo%2BQeJ58p5hzZw0mAkW8nQ2ntcIdqoX6uTA6OEkYIZ1CeSQ2ZecrCWlXqw2LT%2F4YxVPJmQO4&X-Amz-Signature=1ddbd22c20a2ddcd1faaf7171b9b1ccc3b60028f3b7ace3662f38793def79706&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6JTPLXY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAKxdXj95rVdr0r705Kdzt1B9%2Bk3RjUwKfmsJHq9klTcAiAgT%2F%2FoxjC0IgsuF6yrcjwl3JbojtQJM04lAx0EhrisJir%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIM%2FZ15Jox5sKqURa%2BNKtwD0vAEFB8jbukiGFYzhlRX%2Fz0S%2BzIXon50UdyIGE3sr7BHd%2Fhx0peVit59SsZQW8wH0Zj90cincg35JJnG%2Fxgc9zvzv%2BPQL7l9%2F49dcHkr9ZYmTIBXygdMbg%2FAfHKfMmCgzXfcUI5fbuTuywwHC3yXfJ0vodIUAtsrt55uDEHtezNgq%2Bq%2Bo%2FLQnM1OCt60ZhWtZm0sny4KVpnqTf8Ect9R3jQ56EWcUDcsQclNSMkooi12nPy9P92iPBW3WTAP%2FH0grPX6F5Vh%2BR6RGtR3bx65pWnYrjvC1dLOjJ%2FqyTqQwZr3z57O4ny61%2BNuRjjYJCJ4GGlMkJgLG6JyG0lOqiHv8xSMrkFvrMBx3JpiyQh9zEyVcHsWw5VFsECSwmZzP97PUDt3tIGcMQQVl1hBrqUfoCEUPT14kGoCQfBz1gMhtowvDQfTlwlHoS4WXBo5Fi2VOqFthEpuZDJSb1w6Mu6I%2Fj3UJM0gH%2BSsXDqer%2BdqHcRlWGREYqwmOh326ROCWfBCjG5StA5nCH%2Bsf3Y%2Bk7mXut8HME8bSC3ugyVQ2%2BQ2H4DqbPu3p3cqtmdYK0VkVdR%2F3sKxLL4r9mkiWBFgJdklXKNgHS2hyaVahaLGglPh4REV7SDV1fyt59Ii7nMw7oKIvQY6pgHTXTXHjkJ6pssTeBiW7%2FCA9tIYAw0SR%2BlGp4oCDb1feBAPmMTgE500yquM%2FBJatWJxSJl0X%2BmsgkXVDE6ts%2B5g4bixLSTL0mTqUw9zrkKqhLKL2aqlSklIYZUD4EbCJOi8OJH0IcOm%2B8IW2oYTgRYjDo%2BQeJ58p5hzZw0mAkW8nQ2ntcIdqoX6uTA6OEkYIZ1CeSQ2ZecrCWlXqw2LT%2F4YxVPJmQO4&X-Amz-Signature=e29842bdca0384d6d2893772e64af926275061d51c969916cfd506330b1b8d07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W22ZK2C2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQD4QboB3J5K%2B8WAfz8U2FKRSWuDdIAaB5%2FroS4wdCot4QIgNpwI6NxTMmsS5N%2B2foE58BJshG7RXMRKdNY%2FFAMIc4Eq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDEJiwsUcI5oxjBhSYyrcAwto2QuUo0Q0Me1rgSyHzmcM1paukZ%2FlceGQClkvRbHTJ3bGMLdgKryBEwJ5uRAW%2B14uH7iG%2B2QwicOt4ivz5JNR0DYkUmqLQ7zROu6p3RDSrE7TH9KVoX%2Fd55n%2FmB7903JHGHVDu4WrsTNeFJS%2FIdN22Vmp%2BbRX0%2FYvt96AhYZqLQHhZ3egAkcUR4PBPY8Op4oJBQXI%2FRvbI8hVtcuy1cX2kyNucE1xJG2tvEd46SVXzQzXClfq9BCPRrzD2j%2Fz9MlDBjMjyh6yCfiZ7FElhP3Kd1PHafn4N3El1%2BBRBMFeorTlJq1Vio2HmPrWxSGMTMJxUvotIwPE5FRfj3TFUUBozeg9JwrvIFtMSRp2NaDpjpp%2BC%2BK%2B%2F2BURsQGKHwZK3H%2B72S0UmqXlAIZg4CkXbRGgHqK%2B3lu%2Fez010eN0NXOIY8sttFD4JClWZNcV2OFLU5agfWGsuAft8LXsOUWExdyN0QI829xtKCCa%2FpG%2FqgPZpD3kr7y8wYs88h7FP5I0Xmnz%2BeNeqNKpin%2BGfRrkrOLlobB3UlEUz97A09JXXQLrNURYLbNoLtC2k7f19yE70dp%2BkK36ZiAQUBGvLu49euR1AZF5qmnkbIluUwoJAooKdqzvYSRcl%2BdMd0eMNWCiL0GOqUBWbAqGfkqjr8bD5flcQExqtLLRSr45dNm6K4WRgFZlJVVu0IMiTkX1tRyAmIf1sPowdG5iCJ0%2FAVae6Nq3VeJHMotUJRRua4egK4axPT1yC2zRMRG6JlFSLX69oxpzcufgSWkpYq%2FDPiMhZ2D2LrF2mJsvpDs%2B9fs%2BiHZchalXxn6dEr5LG%2Fn7CKAydGvfRcUKINTF4maE220txtRezjPtrx7jZTN&X-Amz-Signature=c5b4a5d77de1be3e03c2ccbed6d78a5f4bf0c57d6452cfdef05b33b3feecab7a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZA237J2%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIBVv4ns1yxVGw1tNAOGJVzkBWu7jpGVS%2FqmmGgTSax4cAiEAgD2gg23So%2F7Fnx2edwDaruG1Emwwd0lGiCRV8oKNS5Iq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDC3fGwzaKluiYSWALircA%2Bq8Yvj6vFMH44XAB3r%2BeVWV2sgVbjO0aeEiIKweepAd50bE8gWOxTzFdClZ1Sbw2t8xmwVtwZFFLflK1jyI3rfa0pBRLtZ9sJDti%2FESJp68AgdotIWj246NdPMXAP4stHaBPKfZwI5Na8Xq71hZDsADfmKkWVisS3SgepJB1hSUrcnNxTW4aDcZtFVSV6%2FMUd598fC1APsi5Hh5DgReJNTjsw7zNY7JxMekxa8SODc1IUshh7b0W0O4h2Z5LMQ%2FhBH4Dt0aySB56GdlGwZRGnuUwAkMVV1f4eMaEhUpPtNSyXJDJxVIX8KSCEU4kRMQCErmw3L%2FfR6c%2BrpXbGUr7ppU8LJXKk3dwaquD1IGs76wIJoa8ot92Of1nPUAJNPmvJYJlg8n58Kl5VNTjKRU73GC1nyihFeJ6hG0zKQUiw2V7jPtPFfT7ZFVLjBvwmWNVDLWGNOnIsitjyIx7hgsDAKideFqpXNou04pgPfKtNpBbidIZq%2BevB5ZDBtufgxxI5A1olGSOyupQWs6wH9aQj5tmTAuj0Q3KVCKA9e6Ol6CYQ4ESpWr5XhvUm1efk676qWexo9LJK65LsdwP6qwamFCbsWwDepMZsqy%2B1XcFu1PIJhJo4brX5Vo%2BxQvMMaCiL0GOqUBdpe1UhL3oiWcG9hh8H%2FKebpoC8ezSE4pcupFwKZrcoBVeFg9anXl4yBuIH7VFJFvQZdPl1u%2FFqW0yyWqVJ5w7rZwVFbbzpN5NK%2FXt%2FEGusXgUDb66RwZqtEFxHO1jb2VxOxJR1NT3q%2FmWJhaZW9M3d%2F4gBJgh3CdSCT85JNJciX6g2uTl0uU7c%2BG4sGn7JLuE2%2B9b0vZ%2F0t0E4tx%2Fm8vRwoorgt4&X-Amz-Signature=ddd75603203bd811477f4d7cba1a791834f6b4f99ac1c7bb542254a2f413598b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7Q5VOTH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCICFQKESadtYcFspf9dhJ9pMIVaGPIBOQ8lz%2BSID4lsscAiEAuxETzTlyZCv3ttdEWFChwZ0dH9YOgwtR7fxCJ27hSLMq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDIVxVhH%2FlxSnHx1EyyrcA8S%2B1upX7wXHq3832ljhjr1BSg3eudK8bdBRu8EbUzHtSd%2BzmIjiOevlhU8J1CbDeJppXAgeWm8CS8%2BV7WrrDg3H5l9R%2B8MsvaDkbMfi8acyw73KUT8PRw31B0U87olnoJZ4J03bNpJi3c9u9mmyozs2xPIV3NEaD1aNbZHO1aV1Lqqryc6Fnp8D0Ph9Z5GaIeMhUFqW1jdklW6c44Ar%2FZKgyIYO%2B4a9E1Di5jtuAXwXi9O5Uv%2Bqc%2B58ZvlPhK%2BA1vOz5Ck8%2BX6itXZY9FUIjPzE1r4qxz3h630R034p7DCgKXsTqfTLBQCkoDhWnVJ9vQCjvBPIvPiNauJw6JDMvteyjiDgbrmhDskHF0hUvVCYxOo4fNnnfDuANs0ef3v0Elyz6lDg6qculA4WmxdNjMwFVlCqPvUr7Q5QOWhuFakxRrObhxMO%2BpzlldiLbimBwM0JZ8HQWhL8bQxr25I%2BOL7q2GdyUuGT25pBD6AgmI2xo1cSNbpQukAJtfsWYEybudukp%2FDOQ3S%2F0j9RXilS4UTBvi43yO1qgnRDpi7600TlM9pmBFhkSmXXSzJMiF0riXJpL28o8UM6l9xodE5V8M8orsSBziJQEnkJ4mknet%2F4UY22mfMuXF2Dy1DgMOiCiL0GOqUB7fH8Del3MIpQ603gVP%2FsDYsWGQvV%2BzvLur1WAvOtwY0JZdA%2F5SHf1g4u47mMEn9kFaHwT%2FMCvyaoWXZl8OKrTRHHd%2Bl5Gy7gMOVcV4%2BeObuQORZZYMJYXVP35IU3mqjaiNc%2F1CtbwfMWjOr56aHeQECmKygl4TD6dINZMZLt4y6YCz9R0k1lZ1ie%2FEzBEAMZiM7PfDVJwv7JTkUROzskPEHhCC3n&X-Amz-Signature=d079e0e7a8490c7721f391f6db19e1aa7beac00270765b5e27a07e8d5bfaf189&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7Q5VOTH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCICFQKESadtYcFspf9dhJ9pMIVaGPIBOQ8lz%2BSID4lsscAiEAuxETzTlyZCv3ttdEWFChwZ0dH9YOgwtR7fxCJ27hSLMq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDIVxVhH%2FlxSnHx1EyyrcA8S%2B1upX7wXHq3832ljhjr1BSg3eudK8bdBRu8EbUzHtSd%2BzmIjiOevlhU8J1CbDeJppXAgeWm8CS8%2BV7WrrDg3H5l9R%2B8MsvaDkbMfi8acyw73KUT8PRw31B0U87olnoJZ4J03bNpJi3c9u9mmyozs2xPIV3NEaD1aNbZHO1aV1Lqqryc6Fnp8D0Ph9Z5GaIeMhUFqW1jdklW6c44Ar%2FZKgyIYO%2B4a9E1Di5jtuAXwXi9O5Uv%2Bqc%2B58ZvlPhK%2BA1vOz5Ck8%2BX6itXZY9FUIjPzE1r4qxz3h630R034p7DCgKXsTqfTLBQCkoDhWnVJ9vQCjvBPIvPiNauJw6JDMvteyjiDgbrmhDskHF0hUvVCYxOo4fNnnfDuANs0ef3v0Elyz6lDg6qculA4WmxdNjMwFVlCqPvUr7Q5QOWhuFakxRrObhxMO%2BpzlldiLbimBwM0JZ8HQWhL8bQxr25I%2BOL7q2GdyUuGT25pBD6AgmI2xo1cSNbpQukAJtfsWYEybudukp%2FDOQ3S%2F0j9RXilS4UTBvi43yO1qgnRDpi7600TlM9pmBFhkSmXXSzJMiF0riXJpL28o8UM6l9xodE5V8M8orsSBziJQEnkJ4mknet%2F4UY22mfMuXF2Dy1DgMOiCiL0GOqUB7fH8Del3MIpQ603gVP%2FsDYsWGQvV%2BzvLur1WAvOtwY0JZdA%2F5SHf1g4u47mMEn9kFaHwT%2FMCvyaoWXZl8OKrTRHHd%2Bl5Gy7gMOVcV4%2BeObuQORZZYMJYXVP35IU3mqjaiNc%2F1CtbwfMWjOr56aHeQECmKygl4TD6dINZMZLt4y6YCz9R0k1lZ1ie%2FEzBEAMZiM7PfDVJwv7JTkUROzskPEHhCC3n&X-Amz-Signature=b3a10db7c65efd211591ce4245026dafe4b919e55d7bde8ff6b918abb400a4e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
