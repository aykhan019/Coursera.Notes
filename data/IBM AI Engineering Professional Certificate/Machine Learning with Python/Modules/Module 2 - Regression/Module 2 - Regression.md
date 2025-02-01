

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNZCFHYX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4%2FlCzaE3uoTX63ioGDL3rxor3i5HyuuCWRKRTXpyxKAIgNFhh2nJrVzf7WqFIflZVdMk6c3rzhIo%2BUGTi2i%2BivrMqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BFqam8wDkNUdkK6yrcA7OPbi7xO4p2pxTgLztmXKVzkFXe8qWBP9rT4LPJJsEyDbY1x8GxHjHhEpj4GYrLhBVIJI2iAw5p%2BFO5ViY4x%2BuAWSp58HU7Jv5deU3lM2slAKqylyl2VyPYx1aQ29idMdkOKq%2FMEvzc8XfJxUgEEErkKfDE5PxrkP%2F%2Fn6ebiwPvxJE7x75LAaQa75KNIv2Z2m0NpDdYMMtmV7eAEOUhPkBQ6E5ItH%2BVDzG9KCxHNXfCywnORpLgD5Ag0%2B%2BJn9FRRHBxVzZmSMLAHZF4K8%2B1JPHoRCCs9uSwhq2WbQwMMqzT6iM1M8hrIcwpYdDBnlqxFwmGKAGxrKSjdJd9%2Ff0Xe%2FQ%2BIyswodcScqxHkGbSiaLijayexEo5sUMw77wl3e19VIyakfgQVykHZXgXCPQBDZ1Sm3u9FZy%2Bo4GtusZ5j7fy1ryOkQZDa6wRPxCFNSDZT%2B%2BRzK2IZYdzK7vfuVTZ9twiM4AFBJ480E0wva1SiCRRYilikRYqV1FY%2BdgOsmKE8qtG1TxwwTg4zUdvWRwIHUukweFzAinrRM9jP91F%2BFS8ZnJtRcwI%2FotHawZL7%2Ft4enU5Ip0KxkdVBbLKywRt9LktoZX7pyKp5eufE1bT1qymuUiSU3VCePcmd%2FItMLH2%2BbwGOqUBxNBnrYBAlaqswpZyVwn8vKUNZQU2eFUrmcimRcIyZn%2Bu35rYwVioixv%2Bdq3LK5IgppEdV5Xyfuzj7ATBbGM99%2FtssMR4J%2FvzX8y3KmHFRDaoDndq40HeBUtOvt5DoF7Oloyjgh1fEWqfdaoYlqAkobi99gbDDaZmkc52EF%2BFbFFqPcXy26La41P2dcj%2BWPt3nNLhGXMOZAuQzT6UVk%2F0ZmBxoyGK&X-Amz-Signature=aeb77ca2e28c858a132a9b44629d56a5f61622862492f934c6e362317578e0ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNZCFHYX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4%2FlCzaE3uoTX63ioGDL3rxor3i5HyuuCWRKRTXpyxKAIgNFhh2nJrVzf7WqFIflZVdMk6c3rzhIo%2BUGTi2i%2BivrMqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BFqam8wDkNUdkK6yrcA7OPbi7xO4p2pxTgLztmXKVzkFXe8qWBP9rT4LPJJsEyDbY1x8GxHjHhEpj4GYrLhBVIJI2iAw5p%2BFO5ViY4x%2BuAWSp58HU7Jv5deU3lM2slAKqylyl2VyPYx1aQ29idMdkOKq%2FMEvzc8XfJxUgEEErkKfDE5PxrkP%2F%2Fn6ebiwPvxJE7x75LAaQa75KNIv2Z2m0NpDdYMMtmV7eAEOUhPkBQ6E5ItH%2BVDzG9KCxHNXfCywnORpLgD5Ag0%2B%2BJn9FRRHBxVzZmSMLAHZF4K8%2B1JPHoRCCs9uSwhq2WbQwMMqzT6iM1M8hrIcwpYdDBnlqxFwmGKAGxrKSjdJd9%2Ff0Xe%2FQ%2BIyswodcScqxHkGbSiaLijayexEo5sUMw77wl3e19VIyakfgQVykHZXgXCPQBDZ1Sm3u9FZy%2Bo4GtusZ5j7fy1ryOkQZDa6wRPxCFNSDZT%2B%2BRzK2IZYdzK7vfuVTZ9twiM4AFBJ480E0wva1SiCRRYilikRYqV1FY%2BdgOsmKE8qtG1TxwwTg4zUdvWRwIHUukweFzAinrRM9jP91F%2BFS8ZnJtRcwI%2FotHawZL7%2Ft4enU5Ip0KxkdVBbLKywRt9LktoZX7pyKp5eufE1bT1qymuUiSU3VCePcmd%2FItMLH2%2BbwGOqUBxNBnrYBAlaqswpZyVwn8vKUNZQU2eFUrmcimRcIyZn%2Bu35rYwVioixv%2Bdq3LK5IgppEdV5Xyfuzj7ATBbGM99%2FtssMR4J%2FvzX8y3KmHFRDaoDndq40HeBUtOvt5DoF7Oloyjgh1fEWqfdaoYlqAkobi99gbDDaZmkc52EF%2BFbFFqPcXy26La41P2dcj%2BWPt3nNLhGXMOZAuQzT6UVk%2F0ZmBxoyGK&X-Amz-Signature=4a289b2724c021f9769a198fe06a50366ec2efd97eb6f39c5c5197a33a21bc41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNZCFHYX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4%2FlCzaE3uoTX63ioGDL3rxor3i5HyuuCWRKRTXpyxKAIgNFhh2nJrVzf7WqFIflZVdMk6c3rzhIo%2BUGTi2i%2BivrMqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BFqam8wDkNUdkK6yrcA7OPbi7xO4p2pxTgLztmXKVzkFXe8qWBP9rT4LPJJsEyDbY1x8GxHjHhEpj4GYrLhBVIJI2iAw5p%2BFO5ViY4x%2BuAWSp58HU7Jv5deU3lM2slAKqylyl2VyPYx1aQ29idMdkOKq%2FMEvzc8XfJxUgEEErkKfDE5PxrkP%2F%2Fn6ebiwPvxJE7x75LAaQa75KNIv2Z2m0NpDdYMMtmV7eAEOUhPkBQ6E5ItH%2BVDzG9KCxHNXfCywnORpLgD5Ag0%2B%2BJn9FRRHBxVzZmSMLAHZF4K8%2B1JPHoRCCs9uSwhq2WbQwMMqzT6iM1M8hrIcwpYdDBnlqxFwmGKAGxrKSjdJd9%2Ff0Xe%2FQ%2BIyswodcScqxHkGbSiaLijayexEo5sUMw77wl3e19VIyakfgQVykHZXgXCPQBDZ1Sm3u9FZy%2Bo4GtusZ5j7fy1ryOkQZDa6wRPxCFNSDZT%2B%2BRzK2IZYdzK7vfuVTZ9twiM4AFBJ480E0wva1SiCRRYilikRYqV1FY%2BdgOsmKE8qtG1TxwwTg4zUdvWRwIHUukweFzAinrRM9jP91F%2BFS8ZnJtRcwI%2FotHawZL7%2Ft4enU5Ip0KxkdVBbLKywRt9LktoZX7pyKp5eufE1bT1qymuUiSU3VCePcmd%2FItMLH2%2BbwGOqUBxNBnrYBAlaqswpZyVwn8vKUNZQU2eFUrmcimRcIyZn%2Bu35rYwVioixv%2Bdq3LK5IgppEdV5Xyfuzj7ATBbGM99%2FtssMR4J%2FvzX8y3KmHFRDaoDndq40HeBUtOvt5DoF7Oloyjgh1fEWqfdaoYlqAkobi99gbDDaZmkc52EF%2BFbFFqPcXy26La41P2dcj%2BWPt3nNLhGXMOZAuQzT6UVk%2F0ZmBxoyGK&X-Amz-Signature=54a3fcc3d4df9485b356368430bd06db6704c381561f1ec734971a71f554b360&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNZCFHYX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4%2FlCzaE3uoTX63ioGDL3rxor3i5HyuuCWRKRTXpyxKAIgNFhh2nJrVzf7WqFIflZVdMk6c3rzhIo%2BUGTi2i%2BivrMqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BFqam8wDkNUdkK6yrcA7OPbi7xO4p2pxTgLztmXKVzkFXe8qWBP9rT4LPJJsEyDbY1x8GxHjHhEpj4GYrLhBVIJI2iAw5p%2BFO5ViY4x%2BuAWSp58HU7Jv5deU3lM2slAKqylyl2VyPYx1aQ29idMdkOKq%2FMEvzc8XfJxUgEEErkKfDE5PxrkP%2F%2Fn6ebiwPvxJE7x75LAaQa75KNIv2Z2m0NpDdYMMtmV7eAEOUhPkBQ6E5ItH%2BVDzG9KCxHNXfCywnORpLgD5Ag0%2B%2BJn9FRRHBxVzZmSMLAHZF4K8%2B1JPHoRCCs9uSwhq2WbQwMMqzT6iM1M8hrIcwpYdDBnlqxFwmGKAGxrKSjdJd9%2Ff0Xe%2FQ%2BIyswodcScqxHkGbSiaLijayexEo5sUMw77wl3e19VIyakfgQVykHZXgXCPQBDZ1Sm3u9FZy%2Bo4GtusZ5j7fy1ryOkQZDa6wRPxCFNSDZT%2B%2BRzK2IZYdzK7vfuVTZ9twiM4AFBJ480E0wva1SiCRRYilikRYqV1FY%2BdgOsmKE8qtG1TxwwTg4zUdvWRwIHUukweFzAinrRM9jP91F%2BFS8ZnJtRcwI%2FotHawZL7%2Ft4enU5Ip0KxkdVBbLKywRt9LktoZX7pyKp5eufE1bT1qymuUiSU3VCePcmd%2FItMLH2%2BbwGOqUBxNBnrYBAlaqswpZyVwn8vKUNZQU2eFUrmcimRcIyZn%2Bu35rYwVioixv%2Bdq3LK5IgppEdV5Xyfuzj7ATBbGM99%2FtssMR4J%2FvzX8y3KmHFRDaoDndq40HeBUtOvt5DoF7Oloyjgh1fEWqfdaoYlqAkobi99gbDDaZmkc52EF%2BFbFFqPcXy26La41P2dcj%2BWPt3nNLhGXMOZAuQzT6UVk%2F0ZmBxoyGK&X-Amz-Signature=73452c36bbcd0b85a6508ae3d6e25deb748b89edde9fa7a3648e47970151a361&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNZCFHYX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4%2FlCzaE3uoTX63ioGDL3rxor3i5HyuuCWRKRTXpyxKAIgNFhh2nJrVzf7WqFIflZVdMk6c3rzhIo%2BUGTi2i%2BivrMqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BFqam8wDkNUdkK6yrcA7OPbi7xO4p2pxTgLztmXKVzkFXe8qWBP9rT4LPJJsEyDbY1x8GxHjHhEpj4GYrLhBVIJI2iAw5p%2BFO5ViY4x%2BuAWSp58HU7Jv5deU3lM2slAKqylyl2VyPYx1aQ29idMdkOKq%2FMEvzc8XfJxUgEEErkKfDE5PxrkP%2F%2Fn6ebiwPvxJE7x75LAaQa75KNIv2Z2m0NpDdYMMtmV7eAEOUhPkBQ6E5ItH%2BVDzG9KCxHNXfCywnORpLgD5Ag0%2B%2BJn9FRRHBxVzZmSMLAHZF4K8%2B1JPHoRCCs9uSwhq2WbQwMMqzT6iM1M8hrIcwpYdDBnlqxFwmGKAGxrKSjdJd9%2Ff0Xe%2FQ%2BIyswodcScqxHkGbSiaLijayexEo5sUMw77wl3e19VIyakfgQVykHZXgXCPQBDZ1Sm3u9FZy%2Bo4GtusZ5j7fy1ryOkQZDa6wRPxCFNSDZT%2B%2BRzK2IZYdzK7vfuVTZ9twiM4AFBJ480E0wva1SiCRRYilikRYqV1FY%2BdgOsmKE8qtG1TxwwTg4zUdvWRwIHUukweFzAinrRM9jP91F%2BFS8ZnJtRcwI%2FotHawZL7%2Ft4enU5Ip0KxkdVBbLKywRt9LktoZX7pyKp5eufE1bT1qymuUiSU3VCePcmd%2FItMLH2%2BbwGOqUBxNBnrYBAlaqswpZyVwn8vKUNZQU2eFUrmcimRcIyZn%2Bu35rYwVioixv%2Bdq3LK5IgppEdV5Xyfuzj7ATBbGM99%2FtssMR4J%2FvzX8y3KmHFRDaoDndq40HeBUtOvt5DoF7Oloyjgh1fEWqfdaoYlqAkobi99gbDDaZmkc52EF%2BFbFFqPcXy26La41P2dcj%2BWPt3nNLhGXMOZAuQzT6UVk%2F0ZmBxoyGK&X-Amz-Signature=5dab91b0060ba48fe41ddd9113b1c662f85bac0141895ea87975a6903c1aa704&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNZCFHYX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4%2FlCzaE3uoTX63ioGDL3rxor3i5HyuuCWRKRTXpyxKAIgNFhh2nJrVzf7WqFIflZVdMk6c3rzhIo%2BUGTi2i%2BivrMqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BFqam8wDkNUdkK6yrcA7OPbi7xO4p2pxTgLztmXKVzkFXe8qWBP9rT4LPJJsEyDbY1x8GxHjHhEpj4GYrLhBVIJI2iAw5p%2BFO5ViY4x%2BuAWSp58HU7Jv5deU3lM2slAKqylyl2VyPYx1aQ29idMdkOKq%2FMEvzc8XfJxUgEEErkKfDE5PxrkP%2F%2Fn6ebiwPvxJE7x75LAaQa75KNIv2Z2m0NpDdYMMtmV7eAEOUhPkBQ6E5ItH%2BVDzG9KCxHNXfCywnORpLgD5Ag0%2B%2BJn9FRRHBxVzZmSMLAHZF4K8%2B1JPHoRCCs9uSwhq2WbQwMMqzT6iM1M8hrIcwpYdDBnlqxFwmGKAGxrKSjdJd9%2Ff0Xe%2FQ%2BIyswodcScqxHkGbSiaLijayexEo5sUMw77wl3e19VIyakfgQVykHZXgXCPQBDZ1Sm3u9FZy%2Bo4GtusZ5j7fy1ryOkQZDa6wRPxCFNSDZT%2B%2BRzK2IZYdzK7vfuVTZ9twiM4AFBJ480E0wva1SiCRRYilikRYqV1FY%2BdgOsmKE8qtG1TxwwTg4zUdvWRwIHUukweFzAinrRM9jP91F%2BFS8ZnJtRcwI%2FotHawZL7%2Ft4enU5Ip0KxkdVBbLKywRt9LktoZX7pyKp5eufE1bT1qymuUiSU3VCePcmd%2FItMLH2%2BbwGOqUBxNBnrYBAlaqswpZyVwn8vKUNZQU2eFUrmcimRcIyZn%2Bu35rYwVioixv%2Bdq3LK5IgppEdV5Xyfuzj7ATBbGM99%2FtssMR4J%2FvzX8y3KmHFRDaoDndq40HeBUtOvt5DoF7Oloyjgh1fEWqfdaoYlqAkobi99gbDDaZmkc52EF%2BFbFFqPcXy26La41P2dcj%2BWPt3nNLhGXMOZAuQzT6UVk%2F0ZmBxoyGK&X-Amz-Signature=9b9b163910c68203d8f6098a0899950affab59f2fb8c3d62c06c3cb23f516bcb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNZCFHYX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4%2FlCzaE3uoTX63ioGDL3rxor3i5HyuuCWRKRTXpyxKAIgNFhh2nJrVzf7WqFIflZVdMk6c3rzhIo%2BUGTi2i%2BivrMqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BFqam8wDkNUdkK6yrcA7OPbi7xO4p2pxTgLztmXKVzkFXe8qWBP9rT4LPJJsEyDbY1x8GxHjHhEpj4GYrLhBVIJI2iAw5p%2BFO5ViY4x%2BuAWSp58HU7Jv5deU3lM2slAKqylyl2VyPYx1aQ29idMdkOKq%2FMEvzc8XfJxUgEEErkKfDE5PxrkP%2F%2Fn6ebiwPvxJE7x75LAaQa75KNIv2Z2m0NpDdYMMtmV7eAEOUhPkBQ6E5ItH%2BVDzG9KCxHNXfCywnORpLgD5Ag0%2B%2BJn9FRRHBxVzZmSMLAHZF4K8%2B1JPHoRCCs9uSwhq2WbQwMMqzT6iM1M8hrIcwpYdDBnlqxFwmGKAGxrKSjdJd9%2Ff0Xe%2FQ%2BIyswodcScqxHkGbSiaLijayexEo5sUMw77wl3e19VIyakfgQVykHZXgXCPQBDZ1Sm3u9FZy%2Bo4GtusZ5j7fy1ryOkQZDa6wRPxCFNSDZT%2B%2BRzK2IZYdzK7vfuVTZ9twiM4AFBJ480E0wva1SiCRRYilikRYqV1FY%2BdgOsmKE8qtG1TxwwTg4zUdvWRwIHUukweFzAinrRM9jP91F%2BFS8ZnJtRcwI%2FotHawZL7%2Ft4enU5Ip0KxkdVBbLKywRt9LktoZX7pyKp5eufE1bT1qymuUiSU3VCePcmd%2FItMLH2%2BbwGOqUBxNBnrYBAlaqswpZyVwn8vKUNZQU2eFUrmcimRcIyZn%2Bu35rYwVioixv%2Bdq3LK5IgppEdV5Xyfuzj7ATBbGM99%2FtssMR4J%2FvzX8y3KmHFRDaoDndq40HeBUtOvt5DoF7Oloyjgh1fEWqfdaoYlqAkobi99gbDDaZmkc52EF%2BFbFFqPcXy26La41P2dcj%2BWPt3nNLhGXMOZAuQzT6UVk%2F0ZmBxoyGK&X-Amz-Signature=c977e8eaaa87a38e0aeaffb1a37bf60822f6bcc13abf473aa6e4e3fb7cdef0e5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNZCFHYX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4%2FlCzaE3uoTX63ioGDL3rxor3i5HyuuCWRKRTXpyxKAIgNFhh2nJrVzf7WqFIflZVdMk6c3rzhIo%2BUGTi2i%2BivrMqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BFqam8wDkNUdkK6yrcA7OPbi7xO4p2pxTgLztmXKVzkFXe8qWBP9rT4LPJJsEyDbY1x8GxHjHhEpj4GYrLhBVIJI2iAw5p%2BFO5ViY4x%2BuAWSp58HU7Jv5deU3lM2slAKqylyl2VyPYx1aQ29idMdkOKq%2FMEvzc8XfJxUgEEErkKfDE5PxrkP%2F%2Fn6ebiwPvxJE7x75LAaQa75KNIv2Z2m0NpDdYMMtmV7eAEOUhPkBQ6E5ItH%2BVDzG9KCxHNXfCywnORpLgD5Ag0%2B%2BJn9FRRHBxVzZmSMLAHZF4K8%2B1JPHoRCCs9uSwhq2WbQwMMqzT6iM1M8hrIcwpYdDBnlqxFwmGKAGxrKSjdJd9%2Ff0Xe%2FQ%2BIyswodcScqxHkGbSiaLijayexEo5sUMw77wl3e19VIyakfgQVykHZXgXCPQBDZ1Sm3u9FZy%2Bo4GtusZ5j7fy1ryOkQZDa6wRPxCFNSDZT%2B%2BRzK2IZYdzK7vfuVTZ9twiM4AFBJ480E0wva1SiCRRYilikRYqV1FY%2BdgOsmKE8qtG1TxwwTg4zUdvWRwIHUukweFzAinrRM9jP91F%2BFS8ZnJtRcwI%2FotHawZL7%2Ft4enU5Ip0KxkdVBbLKywRt9LktoZX7pyKp5eufE1bT1qymuUiSU3VCePcmd%2FItMLH2%2BbwGOqUBxNBnrYBAlaqswpZyVwn8vKUNZQU2eFUrmcimRcIyZn%2Bu35rYwVioixv%2Bdq3LK5IgppEdV5Xyfuzj7ATBbGM99%2FtssMR4J%2FvzX8y3KmHFRDaoDndq40HeBUtOvt5DoF7Oloyjgh1fEWqfdaoYlqAkobi99gbDDaZmkc52EF%2BFbFFqPcXy26La41P2dcj%2BWPt3nNLhGXMOZAuQzT6UVk%2F0ZmBxoyGK&X-Amz-Signature=5516745c31aaa561ea028630425e7e9dcb36cc4fae363361bbb70962cd9ced36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LYPHOQC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBv6yYdle%2BmcPyR40LoxKAMfCaxmMyps0q4J6olQN0RYAiBtPkL1PwscFp59UzcN%2B2oVaBL4Yluln8M%2FYovvYyp4giqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMmH2IHCrZuvxkpRmKtwDqX7uDAHPLaow5l81Ro8mJdvBJbgLjI3KHApKB0DJqXhviquUg9k5Dv8s%2FsiPUzhN5UQq0zn0pVNKo%2FpQCne2WBSR44cQKOdt4wfjaQgkT7ps7Ri154Q%2FjyrLcn42otVupVgpQFURDyWSDE0jhcXI3m4rIZIoeI9Mm41e1DHjLpAMQUoLSgXS2oGn9aibTPgE4Dy1cZ%2FjCIEVQoAt3wKY66lo2KyWhu1o1vQl7aqG7zXQ5rOTCuQ0xWWDZOvPda%2B9N29yocE%2FlTWgdKaM%2BZhwN7qhbB7tg1bVubWGjfis%2F0rmNPEtIzL7TqsnJAZu1jN1gi9hmGlkWYvsFPcJXhskCStat5Zp3uKoKtnhQRoNkyE0ygceTfLmYbEfsJAyCiI6KvKh8ztVyj2K5E52M%2B36%2BEZRTUcHuIOUGq4Ul%2FkNmRN8KM5qXCnUcE0nJTSMpHN2ofuViatU6X0FvrKpfJvDu9BAIcYw7YMCqxHMHNsmrd7MoELwGy90aLMg0ucs7%2FIYm6olfqQlgLxPsl%2FaxVvmYo%2B2JoB6lj%2BvCjmTOwaXtdQwMd2xZGTJpGU7xP%2BVlhHsmLXalr8pWDIf2PWJKWofc8k5CoK5dBaAUmV9u8100xC%2BtOoMv3H8zLWxH2sw4fb5vAY6pgFqpbTlqLi6JkhAoGKaHrxsnvmT19vNzhW8MuTZnmOcmoEgNooQ9BqmSLTHQnpz3qGoETaoKgZhxDkUEhq38MEYSKyakdgxGQfJiU1H4s3CnR%2FZe8CdsZJizUkSHTs9aaWDNuPh26tbjebeisMlOCAyVbWsK%2FYF3KQmouZQKrvBI1qq45iKc2tsdx6YMD2FPaUGsTd3HoxMl%2FcQM2eTpG771alu18Zg&X-Amz-Signature=0249152f7bd8ab3d860c1958fdc9727cfa8576737b822f7d7d9a798d416510de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCNXTRQ6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBtvxFfJwGxFGRFrhxoG9CfRvpRi0kM0ybDU9ngSNCJAiEA355BsijAG013UHUdnw%2BCS4MeAsouRj2jVMHA0yHUgtoqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOGHmdl%2FYfNuKYAjfyrcA35eL95VGSKM%2FPePrZC5jexDdWLfgCJCaAeyujUNbKU%2FEfQ8WUUce68NUszo7zCL6hnthZCiGANuZQXyCkAt8KnHdgv7uAaJz2sRvX7zUMDDwEDiTmr%2FfuPCe2gGkwgmKSVpQ7fzodLWuNPGuo10bmRGXfG9UAW%2FWesZduiC8MbrhQLontDhbrpUZ%2FF09gYcZMMYBDsfydwTgdWxYOhP30%2BL3Ri2xi5ogglJubPQnpFTOTKuFl87b94kUJwj0qWmuxBMh%2B2i%2FOs2xwJ6Wtisw51VpE0VJqW9pexOWvHadpEIGgB%2BVIJHyMVLrarrdqpNbNmKzhLOrVX7DA7S1654GjAl4B90Lqa1urgxmQzYY%2F2YqIxZKbp5tgjpP8srrX3Nr5K6Ajw5%2BV%2F7SyxCojIonRJtj3dS4dxegRGj0FWhr8ywo0NXJyI%2BQeUM76e5IQinffJXVL%2FQgARfFpAKAqQavRluj6POXfNnLmcGGwHkTxdeNY3fIHb5cNjVw%2FRLeJaejdMmgCm65hXxE5CKVjLRZChvffa0C81apfVBS2BKFL56%2Bzvk8eN3LWYChK%2BsHoNZcyBUTHylw5niQANn%2F920uQwC921JzRIJVJsAPepc3QfU0XBOfjS8iRxkLF%2FtMND2%2BbwGOqUBeAU8ueAqmW2r8JSnbuem6bRLF%2BxcMFBU3Z7n3wr3XolSbXcji1jNdxS064KmRjrK8PQvtL%2FW3l8deRd9igGlNz0G%2Fj97r7y3eiQZXzOOWd5QPuvIORvenJaS2GCfdBhpoLfFTBPklbNKJElP6lK%2FYOLAHUWf0Wb1L9Cm8rLpqXbf8a9JdW52dpbgDgnTJGwdTLhMcdBHcdOlIyh%2FPgp2C6r%2FYh5D&X-Amz-Signature=3230f7bd4dcf271cbaf76e69359fff7ae0eb8a52832b39ec76c6a0757dd4d02b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZLR3AAA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFU1K%2BIdMjoVew%2F6piCLObsQqGTCem%2BTQPRO%2B3ChqrZuAiEA0irm8PVeea5qgg1z2PsCc%2FRWc%2BZb%2BMzWwo%2BU%2BWAEVtYqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP1V7Y2q3bSnlt9MfyrcA%2BjpG4VWI0T4wOzCCzYHi61NHkLZ82XeXUBF8ciIqhzuleJkvxbGNLKAqOwMWyUggQNpHZjrPhjCDhS%2Fz9aU2G0rFlEpGCxelH62tZcjcQrX%2B12qTJXYSZJaY9eT%2BHf79H0NQSH3nxBiiLA03nSZH5oDHoOSHFSdQz6T0TDrE52H%2FJeO0Rr8BieBrcxMHyXTcZ97iIbvV%2BxKGKjUVlI%2BLj09kEMqCa4HRiz%2BFS%2BfvIihmArcO5TIixifjtULvBYaGZBbzRRKA3xZNfICVRlP%2FWYKMAQLNupHr4o8SqQcPH6Z1XOc56ElXns7XpeWNBmFQA%2F5EgRgbUgw9DrQ4a7ZOglt1UXxwNLzIyCyi%2F4uG0sLOU23bxA48KJ8jcJpJiQEb6oP9yht6CLrxchQv13VE%2FhNJ6QCF1fy54hSxfazzNWT90JPj0JzQ4QMaO9uMguGCYkexQ60keo%2BYwinUUH1PI5C3fAFbT0SqAgLVFZNYfpLKTMcJKw6JxyaCFG%2F9n1dUkCvh2eV%2B%2BraITovHl6R0F39LamTy5%2F133aGTS1dH2dWHBG2G8pyircWw13m2ERBkdVYinhCFCM8uhOxaW5ejUcvlbi8iPJSqp2sp671cX4jTA7uJYBnwXBho9GOMOL3%2BbwGOqUBeAo2TYUp%2FKuWIhh0JwJRH89rUIW3l5JXpMDGfpndOFiSkogsjDZ7oslRs8GypXxHJGMDuXXudYXIdSFFgzpvg8R2VIikF2BJAF1JWsxH3Ep5m8JCKzPVz4pA6f6Po6cqvilG4WRSezvHfDpQ27RlbBP%2FHelLWnqYXfN1Kp1FlnyUzoRwtCX2EzljQMB4rfo7EnEu26fN2XT28exvjd%2ByWvUn8vsa&X-Amz-Signature=6eb5d091b3cf2a09f1a310817b631314c48d046d920e35f520d12a453693e52c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZLR3AAA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T201442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFU1K%2BIdMjoVew%2F6piCLObsQqGTCem%2BTQPRO%2B3ChqrZuAiEA0irm8PVeea5qgg1z2PsCc%2FRWc%2BZb%2BMzWwo%2BU%2BWAEVtYqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP1V7Y2q3bSnlt9MfyrcA%2BjpG4VWI0T4wOzCCzYHi61NHkLZ82XeXUBF8ciIqhzuleJkvxbGNLKAqOwMWyUggQNpHZjrPhjCDhS%2Fz9aU2G0rFlEpGCxelH62tZcjcQrX%2B12qTJXYSZJaY9eT%2BHf79H0NQSH3nxBiiLA03nSZH5oDHoOSHFSdQz6T0TDrE52H%2FJeO0Rr8BieBrcxMHyXTcZ97iIbvV%2BxKGKjUVlI%2BLj09kEMqCa4HRiz%2BFS%2BfvIihmArcO5TIixifjtULvBYaGZBbzRRKA3xZNfICVRlP%2FWYKMAQLNupHr4o8SqQcPH6Z1XOc56ElXns7XpeWNBmFQA%2F5EgRgbUgw9DrQ4a7ZOglt1UXxwNLzIyCyi%2F4uG0sLOU23bxA48KJ8jcJpJiQEb6oP9yht6CLrxchQv13VE%2FhNJ6QCF1fy54hSxfazzNWT90JPj0JzQ4QMaO9uMguGCYkexQ60keo%2BYwinUUH1PI5C3fAFbT0SqAgLVFZNYfpLKTMcJKw6JxyaCFG%2F9n1dUkCvh2eV%2B%2BraITovHl6R0F39LamTy5%2F133aGTS1dH2dWHBG2G8pyircWw13m2ERBkdVYinhCFCM8uhOxaW5ejUcvlbi8iPJSqp2sp671cX4jTA7uJYBnwXBho9GOMOL3%2BbwGOqUBeAo2TYUp%2FKuWIhh0JwJRH89rUIW3l5JXpMDGfpndOFiSkogsjDZ7oslRs8GypXxHJGMDuXXudYXIdSFFgzpvg8R2VIikF2BJAF1JWsxH3Ep5m8JCKzPVz4pA6f6Po6cqvilG4WRSezvHfDpQ27RlbBP%2FHelLWnqYXfN1Kp1FlnyUzoRwtCX2EzljQMB4rfo7EnEu26fN2XT28exvjd%2ByWvUn8vsa&X-Amz-Signature=5f7131a3989e125d357344cc4a1a772d5b18215f9647a1ea67773c27ea3ccb93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
