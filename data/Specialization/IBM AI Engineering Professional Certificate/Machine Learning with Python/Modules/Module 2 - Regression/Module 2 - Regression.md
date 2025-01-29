

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5YMJVHN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWs07iK8zXJvpatS3G0xem4mTG%2FfYKzNH%2Fpt%2B%2FenO2HAiAQsLrGOc7RIZUzXtyd%2BYAadsrusCBwiLhzlJHIyAt9lCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0nhRlslvul2ZAMsUKtwDTh5U8wn%2BTWvhp4Er4vXnAPbESj3lfCP4jfFWWC23D2%2FfCCsPmAZQQ%2FAVYS0hN1sdnscnUMaub7pyBtGL4sCozkQRUjNxPQ6PfvhO%2FH8dANAgW6ag2RyWLdt0SVibyeAZ21JfYv9ceQR118r9FekAkdR6wkR5BKZDiauQ5Lh4ytlVEEkq1dA%2FgtRNekCM0MND3Mi5p6XqDAh%2F0oxY%2BWOJMC05v8WUKlATwz83wgs1AYAqbb7a51NQChELJggq2aGsoXX2xNTz%2B7sdiIugs6Qjy5ZkufLIFRjmsvXy%2BlcLgvOdUEb3teer4piO53id%2Ft7Of1VlHy50NbuDB%2FMMMdHSLS7UnTq%2Fs9O6d2Tw17VO%2B648T0fL1peL%2F0l6fH3GC94IqsJuJPa7d9oIqELjbnYt3M8v%2FKVu2Mwd0FzwK6ZIYPyA3Jbq6SnOF8pOaJuEPtl%2BMMi7879y%2BzN%2FM8%2FxfBwu8T%2F3%2FlC6OII6sCySesmfWDpTQcxjm%2BsviSYGCYNmEzZC8NwLY4vgpxYmHxKN%2Bq3oAfr7toqT9ucoiCG1N1IsWczIZqCVUk76p2v6xeyuFemzxnT5CiY%2BYNY1diTcrrofQvVJ8V1fsCNJAfaouKtVmIMQzMA9qVsEv5ifqfowu4PpvAY6pgFmtPhfxMxpR%2Bp4PFNJS8ApqsDALd9yWjkto%2BnS7RzMv%2FlnME0WRxqTCo40T0NuutMPIykATXoylIYdP4audOjW0L%2FEY6B9rtZvKjioi7Vcg1C8XetpypG%2FYyaC9%2FOGEK77QyZW7G15haaFeCwFX8DOYJ4bfW2EZrfKNBPjhqHa0GjRK7%2FXkqawqsF8dmPu6430U9QsMzo9RnYfTvdfdocaQK4eECvG&X-Amz-Signature=d5ef2c3b5ab3de75f36b288e62a9bf2dc0a9182a53405d748cd35901a78d66a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5YMJVHN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWs07iK8zXJvpatS3G0xem4mTG%2FfYKzNH%2Fpt%2B%2FenO2HAiAQsLrGOc7RIZUzXtyd%2BYAadsrusCBwiLhzlJHIyAt9lCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0nhRlslvul2ZAMsUKtwDTh5U8wn%2BTWvhp4Er4vXnAPbESj3lfCP4jfFWWC23D2%2FfCCsPmAZQQ%2FAVYS0hN1sdnscnUMaub7pyBtGL4sCozkQRUjNxPQ6PfvhO%2FH8dANAgW6ag2RyWLdt0SVibyeAZ21JfYv9ceQR118r9FekAkdR6wkR5BKZDiauQ5Lh4ytlVEEkq1dA%2FgtRNekCM0MND3Mi5p6XqDAh%2F0oxY%2BWOJMC05v8WUKlATwz83wgs1AYAqbb7a51NQChELJggq2aGsoXX2xNTz%2B7sdiIugs6Qjy5ZkufLIFRjmsvXy%2BlcLgvOdUEb3teer4piO53id%2Ft7Of1VlHy50NbuDB%2FMMMdHSLS7UnTq%2Fs9O6d2Tw17VO%2B648T0fL1peL%2F0l6fH3GC94IqsJuJPa7d9oIqELjbnYt3M8v%2FKVu2Mwd0FzwK6ZIYPyA3Jbq6SnOF8pOaJuEPtl%2BMMi7879y%2BzN%2FM8%2FxfBwu8T%2F3%2FlC6OII6sCySesmfWDpTQcxjm%2BsviSYGCYNmEzZC8NwLY4vgpxYmHxKN%2Bq3oAfr7toqT9ucoiCG1N1IsWczIZqCVUk76p2v6xeyuFemzxnT5CiY%2BYNY1diTcrrofQvVJ8V1fsCNJAfaouKtVmIMQzMA9qVsEv5ifqfowu4PpvAY6pgFmtPhfxMxpR%2Bp4PFNJS8ApqsDALd9yWjkto%2BnS7RzMv%2FlnME0WRxqTCo40T0NuutMPIykATXoylIYdP4audOjW0L%2FEY6B9rtZvKjioi7Vcg1C8XetpypG%2FYyaC9%2FOGEK77QyZW7G15haaFeCwFX8DOYJ4bfW2EZrfKNBPjhqHa0GjRK7%2FXkqawqsF8dmPu6430U9QsMzo9RnYfTvdfdocaQK4eECvG&X-Amz-Signature=ed288a8240b80159c7287830ffd8787a0369ca9ad50b20a9531b31825792ce1e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5YMJVHN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWs07iK8zXJvpatS3G0xem4mTG%2FfYKzNH%2Fpt%2B%2FenO2HAiAQsLrGOc7RIZUzXtyd%2BYAadsrusCBwiLhzlJHIyAt9lCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0nhRlslvul2ZAMsUKtwDTh5U8wn%2BTWvhp4Er4vXnAPbESj3lfCP4jfFWWC23D2%2FfCCsPmAZQQ%2FAVYS0hN1sdnscnUMaub7pyBtGL4sCozkQRUjNxPQ6PfvhO%2FH8dANAgW6ag2RyWLdt0SVibyeAZ21JfYv9ceQR118r9FekAkdR6wkR5BKZDiauQ5Lh4ytlVEEkq1dA%2FgtRNekCM0MND3Mi5p6XqDAh%2F0oxY%2BWOJMC05v8WUKlATwz83wgs1AYAqbb7a51NQChELJggq2aGsoXX2xNTz%2B7sdiIugs6Qjy5ZkufLIFRjmsvXy%2BlcLgvOdUEb3teer4piO53id%2Ft7Of1VlHy50NbuDB%2FMMMdHSLS7UnTq%2Fs9O6d2Tw17VO%2B648T0fL1peL%2F0l6fH3GC94IqsJuJPa7d9oIqELjbnYt3M8v%2FKVu2Mwd0FzwK6ZIYPyA3Jbq6SnOF8pOaJuEPtl%2BMMi7879y%2BzN%2FM8%2FxfBwu8T%2F3%2FlC6OII6sCySesmfWDpTQcxjm%2BsviSYGCYNmEzZC8NwLY4vgpxYmHxKN%2Bq3oAfr7toqT9ucoiCG1N1IsWczIZqCVUk76p2v6xeyuFemzxnT5CiY%2BYNY1diTcrrofQvVJ8V1fsCNJAfaouKtVmIMQzMA9qVsEv5ifqfowu4PpvAY6pgFmtPhfxMxpR%2Bp4PFNJS8ApqsDALd9yWjkto%2BnS7RzMv%2FlnME0WRxqTCo40T0NuutMPIykATXoylIYdP4audOjW0L%2FEY6B9rtZvKjioi7Vcg1C8XetpypG%2FYyaC9%2FOGEK77QyZW7G15haaFeCwFX8DOYJ4bfW2EZrfKNBPjhqHa0GjRK7%2FXkqawqsF8dmPu6430U9QsMzo9RnYfTvdfdocaQK4eECvG&X-Amz-Signature=08e13fc122f55938ff861773cf5f971d8111409f4167d59b0378e6f9124cce34&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5YMJVHN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWs07iK8zXJvpatS3G0xem4mTG%2FfYKzNH%2Fpt%2B%2FenO2HAiAQsLrGOc7RIZUzXtyd%2BYAadsrusCBwiLhzlJHIyAt9lCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0nhRlslvul2ZAMsUKtwDTh5U8wn%2BTWvhp4Er4vXnAPbESj3lfCP4jfFWWC23D2%2FfCCsPmAZQQ%2FAVYS0hN1sdnscnUMaub7pyBtGL4sCozkQRUjNxPQ6PfvhO%2FH8dANAgW6ag2RyWLdt0SVibyeAZ21JfYv9ceQR118r9FekAkdR6wkR5BKZDiauQ5Lh4ytlVEEkq1dA%2FgtRNekCM0MND3Mi5p6XqDAh%2F0oxY%2BWOJMC05v8WUKlATwz83wgs1AYAqbb7a51NQChELJggq2aGsoXX2xNTz%2B7sdiIugs6Qjy5ZkufLIFRjmsvXy%2BlcLgvOdUEb3teer4piO53id%2Ft7Of1VlHy50NbuDB%2FMMMdHSLS7UnTq%2Fs9O6d2Tw17VO%2B648T0fL1peL%2F0l6fH3GC94IqsJuJPa7d9oIqELjbnYt3M8v%2FKVu2Mwd0FzwK6ZIYPyA3Jbq6SnOF8pOaJuEPtl%2BMMi7879y%2BzN%2FM8%2FxfBwu8T%2F3%2FlC6OII6sCySesmfWDpTQcxjm%2BsviSYGCYNmEzZC8NwLY4vgpxYmHxKN%2Bq3oAfr7toqT9ucoiCG1N1IsWczIZqCVUk76p2v6xeyuFemzxnT5CiY%2BYNY1diTcrrofQvVJ8V1fsCNJAfaouKtVmIMQzMA9qVsEv5ifqfowu4PpvAY6pgFmtPhfxMxpR%2Bp4PFNJS8ApqsDALd9yWjkto%2BnS7RzMv%2FlnME0WRxqTCo40T0NuutMPIykATXoylIYdP4audOjW0L%2FEY6B9rtZvKjioi7Vcg1C8XetpypG%2FYyaC9%2FOGEK77QyZW7G15haaFeCwFX8DOYJ4bfW2EZrfKNBPjhqHa0GjRK7%2FXkqawqsF8dmPu6430U9QsMzo9RnYfTvdfdocaQK4eECvG&X-Amz-Signature=9ea8d1e18b568cc907e8fcd080c97684492fb8e109f6602623fb9562c4c9bde7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5YMJVHN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWs07iK8zXJvpatS3G0xem4mTG%2FfYKzNH%2Fpt%2B%2FenO2HAiAQsLrGOc7RIZUzXtyd%2BYAadsrusCBwiLhzlJHIyAt9lCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0nhRlslvul2ZAMsUKtwDTh5U8wn%2BTWvhp4Er4vXnAPbESj3lfCP4jfFWWC23D2%2FfCCsPmAZQQ%2FAVYS0hN1sdnscnUMaub7pyBtGL4sCozkQRUjNxPQ6PfvhO%2FH8dANAgW6ag2RyWLdt0SVibyeAZ21JfYv9ceQR118r9FekAkdR6wkR5BKZDiauQ5Lh4ytlVEEkq1dA%2FgtRNekCM0MND3Mi5p6XqDAh%2F0oxY%2BWOJMC05v8WUKlATwz83wgs1AYAqbb7a51NQChELJggq2aGsoXX2xNTz%2B7sdiIugs6Qjy5ZkufLIFRjmsvXy%2BlcLgvOdUEb3teer4piO53id%2Ft7Of1VlHy50NbuDB%2FMMMdHSLS7UnTq%2Fs9O6d2Tw17VO%2B648T0fL1peL%2F0l6fH3GC94IqsJuJPa7d9oIqELjbnYt3M8v%2FKVu2Mwd0FzwK6ZIYPyA3Jbq6SnOF8pOaJuEPtl%2BMMi7879y%2BzN%2FM8%2FxfBwu8T%2F3%2FlC6OII6sCySesmfWDpTQcxjm%2BsviSYGCYNmEzZC8NwLY4vgpxYmHxKN%2Bq3oAfr7toqT9ucoiCG1N1IsWczIZqCVUk76p2v6xeyuFemzxnT5CiY%2BYNY1diTcrrofQvVJ8V1fsCNJAfaouKtVmIMQzMA9qVsEv5ifqfowu4PpvAY6pgFmtPhfxMxpR%2Bp4PFNJS8ApqsDALd9yWjkto%2BnS7RzMv%2FlnME0WRxqTCo40T0NuutMPIykATXoylIYdP4audOjW0L%2FEY6B9rtZvKjioi7Vcg1C8XetpypG%2FYyaC9%2FOGEK77QyZW7G15haaFeCwFX8DOYJ4bfW2EZrfKNBPjhqHa0GjRK7%2FXkqawqsF8dmPu6430U9QsMzo9RnYfTvdfdocaQK4eECvG&X-Amz-Signature=777183a9643c3212f346de2d35acc8a4259c43f1327801207f651fdf75220c2a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5YMJVHN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWs07iK8zXJvpatS3G0xem4mTG%2FfYKzNH%2Fpt%2B%2FenO2HAiAQsLrGOc7RIZUzXtyd%2BYAadsrusCBwiLhzlJHIyAt9lCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0nhRlslvul2ZAMsUKtwDTh5U8wn%2BTWvhp4Er4vXnAPbESj3lfCP4jfFWWC23D2%2FfCCsPmAZQQ%2FAVYS0hN1sdnscnUMaub7pyBtGL4sCozkQRUjNxPQ6PfvhO%2FH8dANAgW6ag2RyWLdt0SVibyeAZ21JfYv9ceQR118r9FekAkdR6wkR5BKZDiauQ5Lh4ytlVEEkq1dA%2FgtRNekCM0MND3Mi5p6XqDAh%2F0oxY%2BWOJMC05v8WUKlATwz83wgs1AYAqbb7a51NQChELJggq2aGsoXX2xNTz%2B7sdiIugs6Qjy5ZkufLIFRjmsvXy%2BlcLgvOdUEb3teer4piO53id%2Ft7Of1VlHy50NbuDB%2FMMMdHSLS7UnTq%2Fs9O6d2Tw17VO%2B648T0fL1peL%2F0l6fH3GC94IqsJuJPa7d9oIqELjbnYt3M8v%2FKVu2Mwd0FzwK6ZIYPyA3Jbq6SnOF8pOaJuEPtl%2BMMi7879y%2BzN%2FM8%2FxfBwu8T%2F3%2FlC6OII6sCySesmfWDpTQcxjm%2BsviSYGCYNmEzZC8NwLY4vgpxYmHxKN%2Bq3oAfr7toqT9ucoiCG1N1IsWczIZqCVUk76p2v6xeyuFemzxnT5CiY%2BYNY1diTcrrofQvVJ8V1fsCNJAfaouKtVmIMQzMA9qVsEv5ifqfowu4PpvAY6pgFmtPhfxMxpR%2Bp4PFNJS8ApqsDALd9yWjkto%2BnS7RzMv%2FlnME0WRxqTCo40T0NuutMPIykATXoylIYdP4audOjW0L%2FEY6B9rtZvKjioi7Vcg1C8XetpypG%2FYyaC9%2FOGEK77QyZW7G15haaFeCwFX8DOYJ4bfW2EZrfKNBPjhqHa0GjRK7%2FXkqawqsF8dmPu6430U9QsMzo9RnYfTvdfdocaQK4eECvG&X-Amz-Signature=261095ed96c7b7be35a984ff2baed39bd8125c9ef7c14923af72266796dbc023&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5YMJVHN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWs07iK8zXJvpatS3G0xem4mTG%2FfYKzNH%2Fpt%2B%2FenO2HAiAQsLrGOc7RIZUzXtyd%2BYAadsrusCBwiLhzlJHIyAt9lCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0nhRlslvul2ZAMsUKtwDTh5U8wn%2BTWvhp4Er4vXnAPbESj3lfCP4jfFWWC23D2%2FfCCsPmAZQQ%2FAVYS0hN1sdnscnUMaub7pyBtGL4sCozkQRUjNxPQ6PfvhO%2FH8dANAgW6ag2RyWLdt0SVibyeAZ21JfYv9ceQR118r9FekAkdR6wkR5BKZDiauQ5Lh4ytlVEEkq1dA%2FgtRNekCM0MND3Mi5p6XqDAh%2F0oxY%2BWOJMC05v8WUKlATwz83wgs1AYAqbb7a51NQChELJggq2aGsoXX2xNTz%2B7sdiIugs6Qjy5ZkufLIFRjmsvXy%2BlcLgvOdUEb3teer4piO53id%2Ft7Of1VlHy50NbuDB%2FMMMdHSLS7UnTq%2Fs9O6d2Tw17VO%2B648T0fL1peL%2F0l6fH3GC94IqsJuJPa7d9oIqELjbnYt3M8v%2FKVu2Mwd0FzwK6ZIYPyA3Jbq6SnOF8pOaJuEPtl%2BMMi7879y%2BzN%2FM8%2FxfBwu8T%2F3%2FlC6OII6sCySesmfWDpTQcxjm%2BsviSYGCYNmEzZC8NwLY4vgpxYmHxKN%2Bq3oAfr7toqT9ucoiCG1N1IsWczIZqCVUk76p2v6xeyuFemzxnT5CiY%2BYNY1diTcrrofQvVJ8V1fsCNJAfaouKtVmIMQzMA9qVsEv5ifqfowu4PpvAY6pgFmtPhfxMxpR%2Bp4PFNJS8ApqsDALd9yWjkto%2BnS7RzMv%2FlnME0WRxqTCo40T0NuutMPIykATXoylIYdP4audOjW0L%2FEY6B9rtZvKjioi7Vcg1C8XetpypG%2FYyaC9%2FOGEK77QyZW7G15haaFeCwFX8DOYJ4bfW2EZrfKNBPjhqHa0GjRK7%2FXkqawqsF8dmPu6430U9QsMzo9RnYfTvdfdocaQK4eECvG&X-Amz-Signature=4b9ee94c89e6f78bb067515c296b568acb7c49d22c0b7638a0f998aff2b6286a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5YMJVHN%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBWs07iK8zXJvpatS3G0xem4mTG%2FfYKzNH%2Fpt%2B%2FenO2HAiAQsLrGOc7RIZUzXtyd%2BYAadsrusCBwiLhzlJHIyAt9lCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0nhRlslvul2ZAMsUKtwDTh5U8wn%2BTWvhp4Er4vXnAPbESj3lfCP4jfFWWC23D2%2FfCCsPmAZQQ%2FAVYS0hN1sdnscnUMaub7pyBtGL4sCozkQRUjNxPQ6PfvhO%2FH8dANAgW6ag2RyWLdt0SVibyeAZ21JfYv9ceQR118r9FekAkdR6wkR5BKZDiauQ5Lh4ytlVEEkq1dA%2FgtRNekCM0MND3Mi5p6XqDAh%2F0oxY%2BWOJMC05v8WUKlATwz83wgs1AYAqbb7a51NQChELJggq2aGsoXX2xNTz%2B7sdiIugs6Qjy5ZkufLIFRjmsvXy%2BlcLgvOdUEb3teer4piO53id%2Ft7Of1VlHy50NbuDB%2FMMMdHSLS7UnTq%2Fs9O6d2Tw17VO%2B648T0fL1peL%2F0l6fH3GC94IqsJuJPa7d9oIqELjbnYt3M8v%2FKVu2Mwd0FzwK6ZIYPyA3Jbq6SnOF8pOaJuEPtl%2BMMi7879y%2BzN%2FM8%2FxfBwu8T%2F3%2FlC6OII6sCySesmfWDpTQcxjm%2BsviSYGCYNmEzZC8NwLY4vgpxYmHxKN%2Bq3oAfr7toqT9ucoiCG1N1IsWczIZqCVUk76p2v6xeyuFemzxnT5CiY%2BYNY1diTcrrofQvVJ8V1fsCNJAfaouKtVmIMQzMA9qVsEv5ifqfowu4PpvAY6pgFmtPhfxMxpR%2Bp4PFNJS8ApqsDALd9yWjkto%2BnS7RzMv%2FlnME0WRxqTCo40T0NuutMPIykATXoylIYdP4audOjW0L%2FEY6B9rtZvKjioi7Vcg1C8XetpypG%2FYyaC9%2FOGEK77QyZW7G15haaFeCwFX8DOYJ4bfW2EZrfKNBPjhqHa0GjRK7%2FXkqawqsF8dmPu6430U9QsMzo9RnYfTvdfdocaQK4eECvG&X-Amz-Signature=da0ae89f1e2d6de15664feb5b7b5f6c88e52ea0dda0fe324e90e049b477721d2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QIF2ZV6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBafF6irHV%2F%2F%2FR80C%2BvDMz2hbck2xkAF%2BkGGD%2B23u%2BT0AiAcedduH8fYXBL%2B1dK3mDhrmkXs4BW0w%2FY6W340vPekGCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTgLhiJEjKDnVIsa0KtwDVMMvTD9lTm%2Fw5c7C4hZywQqFMFlaXM2lUEto3sWpxeF0w3pKZQXHkyZ%2FwdLH8FEBEccMcwr%2F7IZXwHUo1uBLEbx%2FCB3EQcJC8sCFu%2Fevm%2FWRCf3PJNu3edCTOGwl%2Bd5RwcRlUDCIOMobA%2FANvzGpxxd8GCfXcQXIT%2F08tiEl2j%2FrOxuT00Mbp4CorIvJgLfR3eK5jbwF8AAWi9MlMaKPMuzJSAlIpdmoN8kdF6TCKqj5Hmw9VMkEfIcdtHJ0qImHjM08URMAoXJwEn0qsKGfKe0V3rO3MLy2jfy45rm%2Fjfq4h2X67iSHUIjrOgMoe9G3xC4X8s8nfxj2s7b4CU4Y%2FIsiE8dkR9XeLivVnQ0OtbEAIP9AQEZD%2FhYwCVnLtPZL4LZWupA7OMbuyr5RunD%2F4yzlsDT4tQPfuMyQUQBEoyFo5ULU6NBciwf8iOhDlsSRi%2F%2B0eC3HItVLuMLWVS9z7bjkS7b4E56X97PBA8aoSqDHAkpmczSGkB6Tdg%2B0ictfZgJFJ%2B7k2MPaosY3K6YdgyO%2BjN%2FdHMash8lIqT%2F4AmvJ7pqTlc4Wonh6XyDmLWkcsl8gDgDvxN7C1nlEpwR2nhyk0h%2BAMlBIoFBZI12Zis7YXMnleq8pbIBvL1QwqoPpvAY6pgHfbsEVYkzJoZAS8cYM5iVpm%2FW0LyZXjXE9U545Klk2VIg0stUYofAWrtyClyY1O9rfuzPVhbiJKRt0nq%2Fbozvgf3Yx2%2FAWllFEBaF6FeTQD6GjXqQxBF4pxFSJipw%2B%2BIo%2FF0OB9rA1hRbOmakQOXVZpd3q%2BeFAwJBkqo0kRtaF46wkZwbrs1BKPaCc8cXDQ%2BWqXRxSleKAU2JFYI84JjhO96wcGTzP&X-Amz-Signature=16a8343600c676ba9e440bb5dc34d67f692f255f48cde3d98cac5fb5f2e43c21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLAEREZZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHQzhSILVqKBAVgNpmonm6N%2BYMqs6C9OOfMPNVIWM5YEAiEA%2B9uTfeHrLdAatlw9dkJkAPvRF%2Fm03iR4krJGPxh8To8qiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDE6XlkQAKY0mGGn3ircAxOCU5YvoXETvIf9b7djB5Z7TWab%2F43Sa%2B1TGgXVzt2FI2wvOPb7zcS2TM%2BVxrkThEN%2BelIL4Gb%2BgXwn6bgyaoM8COWlA%2BYHqCojePy6utWqH0mhP5TzaAkDToCWA3IFH%2BZxyYlp3Qrmg3%2B%2FXSlcfZpPmsKmiVJeb0Bv62Kju7wZvCMx50stRvMm8LZBEjsOhRGph%2FDQIOi8N6odKWby3HptoujHbIj908IyTVvaoHZ9csleLTiTQ85mK92qSr1kXnVeFExzPg1jyp6LKGrMYPaVr8xMVy3SlIPp%2B0fkaXTvS1xn%2Fgo4oP2cZHiUVczhzcyj6yjKkFzm541VWpYzomzEO%2BE1HBm8t%2BFy5o8oJdT7xZNRIJ05pqLy3aG1XQwt6WuYYWUNV9apAs%2B8g8B8a51SSbSJZf8pi9xbRnbMXjKbOxA2H3UXPSTCmxuibvv%2F81JN802f1lKUvSMQYrNN9QlRlqX6MWggJv6L6OjKouj%2Bun8Kp1FDZNDkY5dJLpsATmMPhxbt%2B%2FPu7iTOHPuhCKNTK7P8pq5t3rUkCEInoFvBqr%2Bu88zeyQ87a6v9o5%2F4XYswvM%2FaRlB%2BN7asGWzdB8bqI0V3%2B0zgbL24atxXDrcHWDAH3yqb4o6ZSvSmMNWD6bwGOqUB7Ep%2FkOEidDLY8FdvBTxYX5%2FE%2BlJ3lgPTGJ9OD84pKnQThSOi%2B4xcm8IpSsJm1EK7%2B3Z0Jba8sinw%2BdSnP9CrhWHAchLxIJYObwjWZlrAizcHAXnhJm4c3O6RoXTNCF3KEEvpoTJvTokvOYuYxmzS1lShawlyTXtwhRMaV2g5RiZZaVYdsBYBjR7ellke3iWtqAyDFPzMntM0a3spg%2BJvuhd9Xn%2Ft&X-Amz-Signature=0077247d61994f100006661e6be6883579c673532d9461485f889503ea8d8aca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666G4GJFYK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEgrsg9s%2FMKVedVMo2A4%2BNlHmj2%2BcutPVemGK3u5Tjj5AiAkt%2B7mqEK7aTLl6rXdQRMqzvp3WjCJLUNNEh2V7E6raCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtrfddD1HUfhRJHMRKtwDc1oHHI%2BRLvGzgbcfhw0P%2FW7h52eu7TTTR8NnpuXZb7dVhi4iIy6th%2BWRWM1c5QPdfTS7jZjGIso%2Fr1Y89jLYefoESQpjh5zJJo0aiB0jfyTmIabmbIBNJj7%2Fw6uwAka6ZT6hQG9W2L8hcr6EKk6Gknldh4hdmpd1QVFY3GdBVC%2BQxMG0n6xOvbt4%2BYBty4EvRJMjRuXihKDWnNxKMCYpYwxC0RG4ss0AoOdgyXXgtdPQl7%2BVIQxlPfDp6iJzp96f70eIBoM7Leq%2Ft3kAjw6y%2BlS4YUWXeJt11oPzvs1oQOQiTSexsp%2Fnh8EQsUT0kO9mbyGYPvOYAfa4fhhXIV%2BT%2Fo1BuQGca9QWSot%2FaP6fd%2BJ4xZSpdblXlLac8bmSRl0URp%2BNSzTz1WZbz3nZ%2FhxDumBCH70yFs14pdnYRUIbN%2B5HX36VjbMOYT9ygoWI6vo8lKrIGirIs3fQXt1yNPQ86bzw092E5x4R%2F1cOUl0VCIMYtWXh3NQDn6i%2FMV9KZ2W2gaRwtW0%2F8n%2B6naMMIwXjqOYsSiIjf8HIvOohqv01WkjB%2FsPSO4C4BgS%2FnYcasS%2Bi6X3GgAh6ZbhqeaYodb2prnPYhiRHPARg30LPDA0Po1%2FvYM0NYFx%2FdTh7zwgwqoPpvAY6pgEqiGa%2BkyzPWyqR843eNHtuBlSomicXK7RlxDfDB%2BQp%2BqI593n2SIclc0uC2lPuQlmSd8zNldReW2MZ%2FXqaexGyq8Sv%2FNTStqAcwP%2BP1QfOjMH4X3NGuuM4N7s9BdjLX8PtuiBfhCHVEevVdDOOF5iIZbe7n%2FoZ6FfxFNLZTB8lVTOFLukrpdjXjUC647mNXpViVgKeJOYPH%2F3db6ER%2BfjkzIAd9GIr&X-Amz-Signature=31c07d295acde84839bd403d3a4526b16432eb8c87b346cd7d0ff35dde1a4a75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666G4GJFYK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEgrsg9s%2FMKVedVMo2A4%2BNlHmj2%2BcutPVemGK3u5Tjj5AiAkt%2B7mqEK7aTLl6rXdQRMqzvp3WjCJLUNNEh2V7E6raCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtrfddD1HUfhRJHMRKtwDc1oHHI%2BRLvGzgbcfhw0P%2FW7h52eu7TTTR8NnpuXZb7dVhi4iIy6th%2BWRWM1c5QPdfTS7jZjGIso%2Fr1Y89jLYefoESQpjh5zJJo0aiB0jfyTmIabmbIBNJj7%2Fw6uwAka6ZT6hQG9W2L8hcr6EKk6Gknldh4hdmpd1QVFY3GdBVC%2BQxMG0n6xOvbt4%2BYBty4EvRJMjRuXihKDWnNxKMCYpYwxC0RG4ss0AoOdgyXXgtdPQl7%2BVIQxlPfDp6iJzp96f70eIBoM7Leq%2Ft3kAjw6y%2BlS4YUWXeJt11oPzvs1oQOQiTSexsp%2Fnh8EQsUT0kO9mbyGYPvOYAfa4fhhXIV%2BT%2Fo1BuQGca9QWSot%2FaP6fd%2BJ4xZSpdblXlLac8bmSRl0URp%2BNSzTz1WZbz3nZ%2FhxDumBCH70yFs14pdnYRUIbN%2B5HX36VjbMOYT9ygoWI6vo8lKrIGirIs3fQXt1yNPQ86bzw092E5x4R%2F1cOUl0VCIMYtWXh3NQDn6i%2FMV9KZ2W2gaRwtW0%2F8n%2B6naMMIwXjqOYsSiIjf8HIvOohqv01WkjB%2FsPSO4C4BgS%2FnYcasS%2Bi6X3GgAh6ZbhqeaYodb2prnPYhiRHPARg30LPDA0Po1%2FvYM0NYFx%2FdTh7zwgwqoPpvAY6pgEqiGa%2BkyzPWyqR843eNHtuBlSomicXK7RlxDfDB%2BQp%2BqI593n2SIclc0uC2lPuQlmSd8zNldReW2MZ%2FXqaexGyq8Sv%2FNTStqAcwP%2BP1QfOjMH4X3NGuuM4N7s9BdjLX8PtuiBfhCHVEevVdDOOF5iIZbe7n%2FoZ6FfxFNLZTB8lVTOFLukrpdjXjUC647mNXpViVgKeJOYPH%2F3db6ER%2BfjkzIAd9GIr&X-Amz-Signature=c77821b6c20059a50be3acb9567f420c52b6672be0d51e7831bbf5bf0addaeef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
