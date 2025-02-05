

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=f61811c3beef329842f2fafdce70ed816fbdf4be0da9cb527064747ad8224b4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=176a6c72c8f86865b27fe88b998debd8b67f0248db17960c425428f47d5b75dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=c546848671ebd7c2dc12831e8cad004e3f949978416fb40af8156c0364dd1a68&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=3902040208a50ab9ad1955c8229f6c01f2605ab2e6d2ba7fd8f475fb3057c8da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=8fe3626935228c88a6b744f05ac30657e8cd7ec35b6bfac943cb6399690931b8&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=8b06e8abf7ed6a915db94fc7922768237017a7e1239eb0dd531938f41595ea08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=12345c8291b08f32b5762ce4b96006437188245ba96978f03754b49e09d22fd7&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=0102b8dbb00d8a9bb9e98054181f264e9e698c818ec534e9b71678ae7662b3f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGDURF3W%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGEh8UqqDdLTzAlmGTGiVuK3nmO8ZD7DS8ythsW9S0dOAiEA5JXZOwxE8%2Bsz7BXuPp%2BsyxQaFKnH1Q%2FOPdnOOzI%2FGl0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDKltn7hESfT%2F84e%2BLSrcA01rlnDQ%2BfWAQMLGRR15l9T0oWDi7uhOlmlqWhqBl5trzQSfj%2BjUmKu6Gb%2FMB%2Bk3p6CVtQu3I3CuDA6cX4KbCdMwHCjzJosHlQoePih67pgx6rTo56dHHWO9xbTge8T7PJAzooDUQ40SvaTRPPDjeOgqmtDQb%2FNIFrbBNYw5R7rSJaMmsGE0jdBx8K6%2FUosH2EUU81W5WD3jT1AFx1TmwRsRsb%2FANKp3djdVKr73KQ%2Fyavfl7QGdARStS4LL7rTDceXkyu4lNAasL1RSs5p27B07dr5U2R43wPBpup5mY2W45tA%2BIa61jihPsJRFtflRLNha8oMY0GQiG%2BAy%2BkefU8b9Swue1ysWQnim45kYulJXM4nWF1NGf6DqyFbt4exTMGOUU4aTQynCD8trFdp4X0w%2B3YNmWU9QTGIqFgkUyzu130OXNslcBBObcstscfkhVovcUdhIjUYPQp5tyTRFn4VNy19Z5JroPYIXZAiIOwOH8jX%2FtbJxTqRcS74wsV8e%2FVtMwHvQ27UyBQNuFBlK8ff%2Bhw1MjGUfstA0hCi%2BCg13Q61osv0D%2BdF6%2F%2BDxXwVrxT%2FRI6UDXb7TZ13iQvaC2yrSVlM4ujUDBH%2FLDBdpQKjv1WR6wdd8t1B5nrelMPzMir0GOqUBtokhcfTJRntBS6kDlm6kDzbeGdmo8jQSIg4xRpKrXHabbzs1i8mFr1wFzsa7JwGVdH%2BoN4V30zHDp1jc%2BHLMMcOCzKeDe4m06yOZq6i7ekHdklvMzIo2LZO82sBgSYvhgq8kuZlDsxmFE7MCtVhz2TchQqqoZXgRvyROvOAsCzJmY583acZPhnVWQt36Rd%2BrSlxV0K0cg3TXievtB27YuWOiAHwg&X-Amz-Signature=daa52b92434328fdef05f24399dc034b620912b37c3f7d29b1f63d7de61ef04e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662V5HJZRN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCeyXfpYF8cDpT%2BvZoZu7Zx0nyvieaBdjAxwovUkLl%2F3AIhAO8kTbj58ZKvm04gXGgjG8xgF9r9ZGM35dq3lyOUMNwYKv8DCDkQABoMNjM3NDIzMTgzODA1IgwxMNNN0iVksI2blM0q3AMoxenpGQ%2BSdWfyhJ09M8R5vjVXi%2FQYRzRa6rDLxmJDVhF%2Bc7Rsi2NOOCnO5tcDl5NX8ixlfqtCmo6dPEMO7EgjH62c3QN3WSjl34di7VBv0eU04eEfucAPNIrWHsv2k6GEe5i%2FlpLhvNbZl%2Fp%2FX5zV51PLjYAxZ6FgYBG%2BWAQ8%2BjE%2BaxuWBSY1yMGzEtK9WpqaOSQFdqLWd4LFp%2BBtwvzpsM99zfaUCz8Lc8%2BzksbbXzCmKwqf9jm%2FflGOn0RLlnXlKCMc0GzuRohNGLo730tkd%2FDQb1b%2BRUumN7x9pkpLW4Y6Ka8pP%2BKfh31Aj%2BiXQvlqpV%2F%2FbJ2n9ZaxA43EMQ%2B4Zij%2F%2BdEeFTMyGM%2BrvlFNS2dt0jEmrLv74IDqWgWAGgzYIhEfP1Qp5bAZ3MHUKI0IKjuoS1UDllXy8EjFo5SbhUK7iY5es3WEhH8csYIs1puPQa3fm36CtmIWUUhEuuBunTG%2BR%2BFSpmXf7bKjaTdl8AMhOE4lPmj%2BUHHOEV0wPNTeec5hHamgsMRxFMEjVfnXNXQeI2Bu5mcv5zwNRFL1r2BV9CKBEep%2Fx8jpr9L07NSiJfKwqavXGeU7YVpPdbY6Fle2lwuJtTS4yEVKc4FAgW44QTEUGkioVENq%2FDDnzIq9BjqkAQ4ZZBCy%2F0klgFnEGQZhKV%2BCy4fedZIAAh8RxUsOxOtChR2M3QLtzJHKdIkbkiQyI3W2E844IH9HwlxwXJ2fQu6zaQnGQmhv0Xy%2FC%2BRGRFDX5ywgUI%2BuXuKXWMUJf19vFokm03ptHby693lcc3FnaZDEFQyMdM%2BUw7gQ8ehuuZ6CsjiXwuSCRPsuGyVJyhSFeEXse%2Fh6mwgLWzmuzYyVWncswjtF&X-Amz-Signature=74eb0cf5408b19a098b456b9956244663e46455644662650ebcc3e2f3fd64948&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDJ4QFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSs9Nq6NU0wMcE89LH%2Bh7i5rx%2FTFpHaQdhx8r1LoqRmQIhAIoYHzNypZTlQKgoGgaFwlz90WBJg7eZH62u1JGjRgxeKv8DCDkQABoMNjM3NDIzMTgzODA1Igy3lYbWSrUKqali0lwq3ANrUu%2FI2u5yxMwmt2%2BiBQKtzVFuYt%2BkpP8TnwgemPrVNSmt2F5G30ONz9woq2EYIamyW0i36fXUFu1WFdS%2BFLaAX97ouHSKnhn7w2BVk4CuE7PEtPI%2BJb76bAlZ9nhYTCII%2B9SitE%2FWuRFnLfAgkvIp5icxuE7Kw72j%2Fxlz7FUmjM1MBTbAdwyQET%2BtPcxKCkgPplc4YI1a0wzrD%2BI%2F38HaDB2qpISmIfLYkPpcTaW34bGuOiBFjiltdeqDhc%2BWRpLjypgQjIN5FbT%2F4JjiaHJl%2Faa0txb34CBDfK88eVCyteLyMhJBpwPEJ2jAFFTnW6k%2FmEWTSZWkDy1JNoQ0ZVN%2BSfLwGZdP8ir7E8lW5jTcTK8H6GXJOIC5%2FK8maAV2%2F5b%2FKr2nTuNt8Yk38HK%2F0Sl2fLOMUycFw12vWan3Wqjy6WzEOxVSDrSM0eM6yuoAw%2FhsSQpmGuL8nReMZmIHvwR7ullen8ldOWmuIjecKNig94ifS33m5SUScsRFT3%2F9ne502ZByu86%2FBg26ddxFsJdZQr%2FbsoGV7orJZ%2B8hOv4w%2FQMjhazcfYVpy6vvCfLvpiP5Fy1LcHKPzQihYPMA32NhoMfXFq0b9AUbQK%2FXkYKk79a%2FGIlvZ3wTQz63ijD7zIq9BjqkAX61kSrzTwLhZcFQ2mb29kaMsVHyKrw4QEhrLxlkPiKzzins7GpUdlSa3ayZRtbYi%2FdqJgutgze6HulU%2F1g58tTUvJcXfF%2FRXAdAmz9JAjnK6PMOgGDB6NMFruvVEffkYzkj%2FNZ9udgc2j6TE2ptfWoc9SnyUtmajKD1Ku11UnX8FW6b8eTizLKVnEgO6pKdaUuLrxj93iAC1BXPRv%2FMPe6VMS75&X-Amz-Signature=9ff06ab3407bf231a55d63529522f9190757a264f7d3860e11ea4e6b390e2923&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDJ4QFAT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSs9Nq6NU0wMcE89LH%2Bh7i5rx%2FTFpHaQdhx8r1LoqRmQIhAIoYHzNypZTlQKgoGgaFwlz90WBJg7eZH62u1JGjRgxeKv8DCDkQABoMNjM3NDIzMTgzODA1Igy3lYbWSrUKqali0lwq3ANrUu%2FI2u5yxMwmt2%2BiBQKtzVFuYt%2BkpP8TnwgemPrVNSmt2F5G30ONz9woq2EYIamyW0i36fXUFu1WFdS%2BFLaAX97ouHSKnhn7w2BVk4CuE7PEtPI%2BJb76bAlZ9nhYTCII%2B9SitE%2FWuRFnLfAgkvIp5icxuE7Kw72j%2Fxlz7FUmjM1MBTbAdwyQET%2BtPcxKCkgPplc4YI1a0wzrD%2BI%2F38HaDB2qpISmIfLYkPpcTaW34bGuOiBFjiltdeqDhc%2BWRpLjypgQjIN5FbT%2F4JjiaHJl%2Faa0txb34CBDfK88eVCyteLyMhJBpwPEJ2jAFFTnW6k%2FmEWTSZWkDy1JNoQ0ZVN%2BSfLwGZdP8ir7E8lW5jTcTK8H6GXJOIC5%2FK8maAV2%2F5b%2FKr2nTuNt8Yk38HK%2F0Sl2fLOMUycFw12vWan3Wqjy6WzEOxVSDrSM0eM6yuoAw%2FhsSQpmGuL8nReMZmIHvwR7ullen8ldOWmuIjecKNig94ifS33m5SUScsRFT3%2F9ne502ZByu86%2FBg26ddxFsJdZQr%2FbsoGV7orJZ%2B8hOv4w%2FQMjhazcfYVpy6vvCfLvpiP5Fy1LcHKPzQihYPMA32NhoMfXFq0b9AUbQK%2FXkYKk79a%2FGIlvZ3wTQz63ijD7zIq9BjqkAX61kSrzTwLhZcFQ2mb29kaMsVHyKrw4QEhrLxlkPiKzzins7GpUdlSa3ayZRtbYi%2FdqJgutgze6HulU%2F1g58tTUvJcXfF%2FRXAdAmz9JAjnK6PMOgGDB6NMFruvVEffkYzkj%2FNZ9udgc2j6TE2ptfWoc9SnyUtmajKD1Ku11UnX8FW6b8eTizLKVnEgO6pKdaUuLrxj93iAC1BXPRv%2FMPe6VMS75&X-Amz-Signature=c7c8481e5d1afd7888d4e027c35310334fd619dd87937a3c42a6bb8d74429aea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
