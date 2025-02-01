

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKNTGTIU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5WQyA5SD9z%2Fh7GoYGpjfazrEbCNFpEGVPooCWE7UoGwIgYrEQKdTvTPsZ91sjaww9vnyAM0AlvabJHNvEahvwLKsqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8tegtse17awA2%2FircA%2FKekoFgl4zWWZKaSi8Sh33mpVzx4NCga9UEwPSf4s8nxc99ipITAxNdJ0g8wRpFD331mfv22wehSKNemE9B61L%2Bm5XCuJPehSPT9yFOKgaoZp9EQFVYTdr10yM5mO3Ct%2FeoiZ8UjdCZj%2FQlI%2FfvAR1FBINzI8XiLRvyFjJg1feTTYJqpOPPEPaO0mpbNfQyWBrQV0N%2FBexjzqP%2FXlYWQjBTKnGC3Rtpfko%2F7zGSkq3FIteNZ27bCp3ew1WMZkHziA%2BwaGEbRUXhzINDUqjBLl3mPojuG331trvx27ar47n0voVZJ02553hrKu17%2Fqi5jTo5FhQMd%2BmbYBG0O%2Bt3cQXBZAWNi4hrvQJPjFLUuXlWyq7Y%2BzwPDyMhUaIlXM9VWk74pFvWCokoXKziSEfeR1PeEbkvCwEVQDOdFM%2BBStAnChCeXit4uKQgcQHs68q4xttwIzBRwid3x257lzs1UqSWzg3QrA43GUV%2BhIMc7b2i7vBk9rvrAeb6udeBKXUnSwW5DpdptazCjEk%2FD4eDQ2oD2DCmV4gaEb50SA%2FJD0%2ByJmZR6fNQ0RRE26Sxe9CuQ%2F29nDZYEjrwQeuQ0t3AYQrQ5FIjKdHOp47wkbwYVUhEKcRpiGP8A7EjNqrWMLHA%2BLwGOqUBingJRjGHPUpdVC8nPzifnYXTNeyIeQZJMVqgBj0Inu1H5x09Q1rRrJyJzVli2co0oKwOXAbKjKMQXF636RoDcY7Vq%2B%2FPYaQofBgL2xgVSsIGn8rX4ORQbBVETHZ%2FFB0HAaEAWO%2FChinnWZZG%2BbeKQbmLJMmTaZF3U7N6aqedlvlFNsdwBtB5YBsci7KQBpx7nOigs1G3WjYxllBYCUHuSWlX0Zym&X-Amz-Signature=12d13939b60d1e8011fee557ebe1c237b9700a3b6e4f586049030a54271b4c0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKNTGTIU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5WQyA5SD9z%2Fh7GoYGpjfazrEbCNFpEGVPooCWE7UoGwIgYrEQKdTvTPsZ91sjaww9vnyAM0AlvabJHNvEahvwLKsqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8tegtse17awA2%2FircA%2FKekoFgl4zWWZKaSi8Sh33mpVzx4NCga9UEwPSf4s8nxc99ipITAxNdJ0g8wRpFD331mfv22wehSKNemE9B61L%2Bm5XCuJPehSPT9yFOKgaoZp9EQFVYTdr10yM5mO3Ct%2FeoiZ8UjdCZj%2FQlI%2FfvAR1FBINzI8XiLRvyFjJg1feTTYJqpOPPEPaO0mpbNfQyWBrQV0N%2FBexjzqP%2FXlYWQjBTKnGC3Rtpfko%2F7zGSkq3FIteNZ27bCp3ew1WMZkHziA%2BwaGEbRUXhzINDUqjBLl3mPojuG331trvx27ar47n0voVZJ02553hrKu17%2Fqi5jTo5FhQMd%2BmbYBG0O%2Bt3cQXBZAWNi4hrvQJPjFLUuXlWyq7Y%2BzwPDyMhUaIlXM9VWk74pFvWCokoXKziSEfeR1PeEbkvCwEVQDOdFM%2BBStAnChCeXit4uKQgcQHs68q4xttwIzBRwid3x257lzs1UqSWzg3QrA43GUV%2BhIMc7b2i7vBk9rvrAeb6udeBKXUnSwW5DpdptazCjEk%2FD4eDQ2oD2DCmV4gaEb50SA%2FJD0%2ByJmZR6fNQ0RRE26Sxe9CuQ%2F29nDZYEjrwQeuQ0t3AYQrQ5FIjKdHOp47wkbwYVUhEKcRpiGP8A7EjNqrWMLHA%2BLwGOqUBingJRjGHPUpdVC8nPzifnYXTNeyIeQZJMVqgBj0Inu1H5x09Q1rRrJyJzVli2co0oKwOXAbKjKMQXF636RoDcY7Vq%2B%2FPYaQofBgL2xgVSsIGn8rX4ORQbBVETHZ%2FFB0HAaEAWO%2FChinnWZZG%2BbeKQbmLJMmTaZF3U7N6aqedlvlFNsdwBtB5YBsci7KQBpx7nOigs1G3WjYxllBYCUHuSWlX0Zym&X-Amz-Signature=305f2b6dd3cee213406a5680bae640d1fbbee00c86b89c52f64214410caecd3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKNTGTIU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5WQyA5SD9z%2Fh7GoYGpjfazrEbCNFpEGVPooCWE7UoGwIgYrEQKdTvTPsZ91sjaww9vnyAM0AlvabJHNvEahvwLKsqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8tegtse17awA2%2FircA%2FKekoFgl4zWWZKaSi8Sh33mpVzx4NCga9UEwPSf4s8nxc99ipITAxNdJ0g8wRpFD331mfv22wehSKNemE9B61L%2Bm5XCuJPehSPT9yFOKgaoZp9EQFVYTdr10yM5mO3Ct%2FeoiZ8UjdCZj%2FQlI%2FfvAR1FBINzI8XiLRvyFjJg1feTTYJqpOPPEPaO0mpbNfQyWBrQV0N%2FBexjzqP%2FXlYWQjBTKnGC3Rtpfko%2F7zGSkq3FIteNZ27bCp3ew1WMZkHziA%2BwaGEbRUXhzINDUqjBLl3mPojuG331trvx27ar47n0voVZJ02553hrKu17%2Fqi5jTo5FhQMd%2BmbYBG0O%2Bt3cQXBZAWNi4hrvQJPjFLUuXlWyq7Y%2BzwPDyMhUaIlXM9VWk74pFvWCokoXKziSEfeR1PeEbkvCwEVQDOdFM%2BBStAnChCeXit4uKQgcQHs68q4xttwIzBRwid3x257lzs1UqSWzg3QrA43GUV%2BhIMc7b2i7vBk9rvrAeb6udeBKXUnSwW5DpdptazCjEk%2FD4eDQ2oD2DCmV4gaEb50SA%2FJD0%2ByJmZR6fNQ0RRE26Sxe9CuQ%2F29nDZYEjrwQeuQ0t3AYQrQ5FIjKdHOp47wkbwYVUhEKcRpiGP8A7EjNqrWMLHA%2BLwGOqUBingJRjGHPUpdVC8nPzifnYXTNeyIeQZJMVqgBj0Inu1H5x09Q1rRrJyJzVli2co0oKwOXAbKjKMQXF636RoDcY7Vq%2B%2FPYaQofBgL2xgVSsIGn8rX4ORQbBVETHZ%2FFB0HAaEAWO%2FChinnWZZG%2BbeKQbmLJMmTaZF3U7N6aqedlvlFNsdwBtB5YBsci7KQBpx7nOigs1G3WjYxllBYCUHuSWlX0Zym&X-Amz-Signature=e692b3bfd012efc9707be90492041e18b3a07cae00bc7ba7e990d1c718e1d7da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKNTGTIU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5WQyA5SD9z%2Fh7GoYGpjfazrEbCNFpEGVPooCWE7UoGwIgYrEQKdTvTPsZ91sjaww9vnyAM0AlvabJHNvEahvwLKsqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8tegtse17awA2%2FircA%2FKekoFgl4zWWZKaSi8Sh33mpVzx4NCga9UEwPSf4s8nxc99ipITAxNdJ0g8wRpFD331mfv22wehSKNemE9B61L%2Bm5XCuJPehSPT9yFOKgaoZp9EQFVYTdr10yM5mO3Ct%2FeoiZ8UjdCZj%2FQlI%2FfvAR1FBINzI8XiLRvyFjJg1feTTYJqpOPPEPaO0mpbNfQyWBrQV0N%2FBexjzqP%2FXlYWQjBTKnGC3Rtpfko%2F7zGSkq3FIteNZ27bCp3ew1WMZkHziA%2BwaGEbRUXhzINDUqjBLl3mPojuG331trvx27ar47n0voVZJ02553hrKu17%2Fqi5jTo5FhQMd%2BmbYBG0O%2Bt3cQXBZAWNi4hrvQJPjFLUuXlWyq7Y%2BzwPDyMhUaIlXM9VWk74pFvWCokoXKziSEfeR1PeEbkvCwEVQDOdFM%2BBStAnChCeXit4uKQgcQHs68q4xttwIzBRwid3x257lzs1UqSWzg3QrA43GUV%2BhIMc7b2i7vBk9rvrAeb6udeBKXUnSwW5DpdptazCjEk%2FD4eDQ2oD2DCmV4gaEb50SA%2FJD0%2ByJmZR6fNQ0RRE26Sxe9CuQ%2F29nDZYEjrwQeuQ0t3AYQrQ5FIjKdHOp47wkbwYVUhEKcRpiGP8A7EjNqrWMLHA%2BLwGOqUBingJRjGHPUpdVC8nPzifnYXTNeyIeQZJMVqgBj0Inu1H5x09Q1rRrJyJzVli2co0oKwOXAbKjKMQXF636RoDcY7Vq%2B%2FPYaQofBgL2xgVSsIGn8rX4ORQbBVETHZ%2FFB0HAaEAWO%2FChinnWZZG%2BbeKQbmLJMmTaZF3U7N6aqedlvlFNsdwBtB5YBsci7KQBpx7nOigs1G3WjYxllBYCUHuSWlX0Zym&X-Amz-Signature=a90654f78bb1d7e3ca0f7f00982112d6ff530116ff429a1892d44302c541c605&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKNTGTIU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5WQyA5SD9z%2Fh7GoYGpjfazrEbCNFpEGVPooCWE7UoGwIgYrEQKdTvTPsZ91sjaww9vnyAM0AlvabJHNvEahvwLKsqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8tegtse17awA2%2FircA%2FKekoFgl4zWWZKaSi8Sh33mpVzx4NCga9UEwPSf4s8nxc99ipITAxNdJ0g8wRpFD331mfv22wehSKNemE9B61L%2Bm5XCuJPehSPT9yFOKgaoZp9EQFVYTdr10yM5mO3Ct%2FeoiZ8UjdCZj%2FQlI%2FfvAR1FBINzI8XiLRvyFjJg1feTTYJqpOPPEPaO0mpbNfQyWBrQV0N%2FBexjzqP%2FXlYWQjBTKnGC3Rtpfko%2F7zGSkq3FIteNZ27bCp3ew1WMZkHziA%2BwaGEbRUXhzINDUqjBLl3mPojuG331trvx27ar47n0voVZJ02553hrKu17%2Fqi5jTo5FhQMd%2BmbYBG0O%2Bt3cQXBZAWNi4hrvQJPjFLUuXlWyq7Y%2BzwPDyMhUaIlXM9VWk74pFvWCokoXKziSEfeR1PeEbkvCwEVQDOdFM%2BBStAnChCeXit4uKQgcQHs68q4xttwIzBRwid3x257lzs1UqSWzg3QrA43GUV%2BhIMc7b2i7vBk9rvrAeb6udeBKXUnSwW5DpdptazCjEk%2FD4eDQ2oD2DCmV4gaEb50SA%2FJD0%2ByJmZR6fNQ0RRE26Sxe9CuQ%2F29nDZYEjrwQeuQ0t3AYQrQ5FIjKdHOp47wkbwYVUhEKcRpiGP8A7EjNqrWMLHA%2BLwGOqUBingJRjGHPUpdVC8nPzifnYXTNeyIeQZJMVqgBj0Inu1H5x09Q1rRrJyJzVli2co0oKwOXAbKjKMQXF636RoDcY7Vq%2B%2FPYaQofBgL2xgVSsIGn8rX4ORQbBVETHZ%2FFB0HAaEAWO%2FChinnWZZG%2BbeKQbmLJMmTaZF3U7N6aqedlvlFNsdwBtB5YBsci7KQBpx7nOigs1G3WjYxllBYCUHuSWlX0Zym&X-Amz-Signature=3763b8d774409fcbde551eaf560dbe0601869955c9e14aab06e1aabb09095386&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKNTGTIU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5WQyA5SD9z%2Fh7GoYGpjfazrEbCNFpEGVPooCWE7UoGwIgYrEQKdTvTPsZ91sjaww9vnyAM0AlvabJHNvEahvwLKsqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8tegtse17awA2%2FircA%2FKekoFgl4zWWZKaSi8Sh33mpVzx4NCga9UEwPSf4s8nxc99ipITAxNdJ0g8wRpFD331mfv22wehSKNemE9B61L%2Bm5XCuJPehSPT9yFOKgaoZp9EQFVYTdr10yM5mO3Ct%2FeoiZ8UjdCZj%2FQlI%2FfvAR1FBINzI8XiLRvyFjJg1feTTYJqpOPPEPaO0mpbNfQyWBrQV0N%2FBexjzqP%2FXlYWQjBTKnGC3Rtpfko%2F7zGSkq3FIteNZ27bCp3ew1WMZkHziA%2BwaGEbRUXhzINDUqjBLl3mPojuG331trvx27ar47n0voVZJ02553hrKu17%2Fqi5jTo5FhQMd%2BmbYBG0O%2Bt3cQXBZAWNi4hrvQJPjFLUuXlWyq7Y%2BzwPDyMhUaIlXM9VWk74pFvWCokoXKziSEfeR1PeEbkvCwEVQDOdFM%2BBStAnChCeXit4uKQgcQHs68q4xttwIzBRwid3x257lzs1UqSWzg3QrA43GUV%2BhIMc7b2i7vBk9rvrAeb6udeBKXUnSwW5DpdptazCjEk%2FD4eDQ2oD2DCmV4gaEb50SA%2FJD0%2ByJmZR6fNQ0RRE26Sxe9CuQ%2F29nDZYEjrwQeuQ0t3AYQrQ5FIjKdHOp47wkbwYVUhEKcRpiGP8A7EjNqrWMLHA%2BLwGOqUBingJRjGHPUpdVC8nPzifnYXTNeyIeQZJMVqgBj0Inu1H5x09Q1rRrJyJzVli2co0oKwOXAbKjKMQXF636RoDcY7Vq%2B%2FPYaQofBgL2xgVSsIGn8rX4ORQbBVETHZ%2FFB0HAaEAWO%2FChinnWZZG%2BbeKQbmLJMmTaZF3U7N6aqedlvlFNsdwBtB5YBsci7KQBpx7nOigs1G3WjYxllBYCUHuSWlX0Zym&X-Amz-Signature=c2d8729961f7e7d29108bfa035fdfa237b3909ce52f2aa3792adab52fc704268&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKNTGTIU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5WQyA5SD9z%2Fh7GoYGpjfazrEbCNFpEGVPooCWE7UoGwIgYrEQKdTvTPsZ91sjaww9vnyAM0AlvabJHNvEahvwLKsqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8tegtse17awA2%2FircA%2FKekoFgl4zWWZKaSi8Sh33mpVzx4NCga9UEwPSf4s8nxc99ipITAxNdJ0g8wRpFD331mfv22wehSKNemE9B61L%2Bm5XCuJPehSPT9yFOKgaoZp9EQFVYTdr10yM5mO3Ct%2FeoiZ8UjdCZj%2FQlI%2FfvAR1FBINzI8XiLRvyFjJg1feTTYJqpOPPEPaO0mpbNfQyWBrQV0N%2FBexjzqP%2FXlYWQjBTKnGC3Rtpfko%2F7zGSkq3FIteNZ27bCp3ew1WMZkHziA%2BwaGEbRUXhzINDUqjBLl3mPojuG331trvx27ar47n0voVZJ02553hrKu17%2Fqi5jTo5FhQMd%2BmbYBG0O%2Bt3cQXBZAWNi4hrvQJPjFLUuXlWyq7Y%2BzwPDyMhUaIlXM9VWk74pFvWCokoXKziSEfeR1PeEbkvCwEVQDOdFM%2BBStAnChCeXit4uKQgcQHs68q4xttwIzBRwid3x257lzs1UqSWzg3QrA43GUV%2BhIMc7b2i7vBk9rvrAeb6udeBKXUnSwW5DpdptazCjEk%2FD4eDQ2oD2DCmV4gaEb50SA%2FJD0%2ByJmZR6fNQ0RRE26Sxe9CuQ%2F29nDZYEjrwQeuQ0t3AYQrQ5FIjKdHOp47wkbwYVUhEKcRpiGP8A7EjNqrWMLHA%2BLwGOqUBingJRjGHPUpdVC8nPzifnYXTNeyIeQZJMVqgBj0Inu1H5x09Q1rRrJyJzVli2co0oKwOXAbKjKMQXF636RoDcY7Vq%2B%2FPYaQofBgL2xgVSsIGn8rX4ORQbBVETHZ%2FFB0HAaEAWO%2FChinnWZZG%2BbeKQbmLJMmTaZF3U7N6aqedlvlFNsdwBtB5YBsci7KQBpx7nOigs1G3WjYxllBYCUHuSWlX0Zym&X-Amz-Signature=6af3eec80eec5309c06928c65b2a59c82f9411904370730ed61498e2c2622c06&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKNTGTIU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5WQyA5SD9z%2Fh7GoYGpjfazrEbCNFpEGVPooCWE7UoGwIgYrEQKdTvTPsZ91sjaww9vnyAM0AlvabJHNvEahvwLKsqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg8tegtse17awA2%2FircA%2FKekoFgl4zWWZKaSi8Sh33mpVzx4NCga9UEwPSf4s8nxc99ipITAxNdJ0g8wRpFD331mfv22wehSKNemE9B61L%2Bm5XCuJPehSPT9yFOKgaoZp9EQFVYTdr10yM5mO3Ct%2FeoiZ8UjdCZj%2FQlI%2FfvAR1FBINzI8XiLRvyFjJg1feTTYJqpOPPEPaO0mpbNfQyWBrQV0N%2FBexjzqP%2FXlYWQjBTKnGC3Rtpfko%2F7zGSkq3FIteNZ27bCp3ew1WMZkHziA%2BwaGEbRUXhzINDUqjBLl3mPojuG331trvx27ar47n0voVZJ02553hrKu17%2Fqi5jTo5FhQMd%2BmbYBG0O%2Bt3cQXBZAWNi4hrvQJPjFLUuXlWyq7Y%2BzwPDyMhUaIlXM9VWk74pFvWCokoXKziSEfeR1PeEbkvCwEVQDOdFM%2BBStAnChCeXit4uKQgcQHs68q4xttwIzBRwid3x257lzs1UqSWzg3QrA43GUV%2BhIMc7b2i7vBk9rvrAeb6udeBKXUnSwW5DpdptazCjEk%2FD4eDQ2oD2DCmV4gaEb50SA%2FJD0%2ByJmZR6fNQ0RRE26Sxe9CuQ%2F29nDZYEjrwQeuQ0t3AYQrQ5FIjKdHOp47wkbwYVUhEKcRpiGP8A7EjNqrWMLHA%2BLwGOqUBingJRjGHPUpdVC8nPzifnYXTNeyIeQZJMVqgBj0Inu1H5x09Q1rRrJyJzVli2co0oKwOXAbKjKMQXF636RoDcY7Vq%2B%2FPYaQofBgL2xgVSsIGn8rX4ORQbBVETHZ%2FFB0HAaEAWO%2FChinnWZZG%2BbeKQbmLJMmTaZF3U7N6aqedlvlFNsdwBtB5YBsci7KQBpx7nOigs1G3WjYxllBYCUHuSWlX0Zym&X-Amz-Signature=eb845bb8bf0e33a60ea7f62dd056164788447b5a0faa65cae30c83a03131af7c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ST5NUKYN%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCs3llUMZDxx8RQOxmkNCiZB7vlccoOlz0cwCr2LXkRBwIgeeZqz0a4CcqXrw75JQEu2yPxdjh6wtIUs0gwM7orNxoqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJBLCthgSb5zLuhkCrcAxZK8bLDOaqoSC7uXVevdZMnIGZUuMBV0iHoPad6sye0dk9J7y3ncC7pMISBjAuYRTbwfPOdlv7CNoSevGmrh78Va8ZiHxDQ83BD5nq%2B3QeJ880h180dPHf1F8RKA0QC%2FLLvoT2FXjgA0xVlnAsSYoP7wDZvHXJAEFjNyawMI%2FEruHbgw4jnhSYTj6wWjgVuWfyI4xdyGpCuF9BpqvNAWfxj3h01Zbb%2Bh7MEgqxqfAbN0LOHvkp6I2M1RU%2BqIKRet1NLohx7zBjcYfyqS5CfZfn701jtSsICQGZtcyZOj8k%2F0rq7NnGtiUTMPrcrMdyYd0N3HiKLnM2rIzNStXdqhNdjdwjFaYEaEKPoJltvHAVwvgIglDLBG%2B3O1qA%2Fpljht9RwM6VGFno6vyT%2FPrXq6sbQz67qy0N7yKzrsdWTTKxfdFxH3kZasp%2FkVHShBORuf2yqHzWgRuc%2FI6sIDXv38LjFeR%2FOFkQyhYhN1I2QKRCvwb3Erbk4taAbkopqYbWjbxOPBmfbwZ%2BdzH0D5X3W8%2FFO77LV9VGz%2FgK2UzT26%2BoCRUJjJnPgt2DON4X7Iyb3zzLRcO7UCRtMpoJfrCuRaRhGc0LqmWyMSLn00BbNmxHuumOCOo14zzViM2t4MMnG%2BLwGOqUBnaPup9Va6IEkdCIXM7MRjIOrO9mN4GlCdqoLeGAP2JMkfu3QQClKBH%2B1AzkaduZjoM14xw40gLZBYRdsVc8bwzVRuhHEH7S0sPqgABHTmCIrc880EjP4vCMwItFbPkieU23QQh1Ry5RMoeQMgyUrb%2FPVr1pTHr9TnDhqLNTR8Lmeh2Ms2N0hCfUz0tmFP7%2FF4wnIllq1Q6btrown4Wnw3FnHpolK&X-Amz-Signature=088b3db62af3e6e5e3afdfc7d540512f05b4b8a9f74dbfa958b268a48c219cc1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZ6M3727%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTfPbb%2FjKtBHunPgTAxnlpOgrGio0bP4t%2B9xtBoPU%2FpAIhAJ5v%2BfomGgjyJZ6SbwA4ciicJq6gvkt2nBIxo5luZheZKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyZRWj9Fu644uSPKQoq3ANXAlcVm%2BoJnrGQw1hsA3oPt%2BIc8wNYQJb8yNBarRp5fcFT%2FHCf%2B%2Flc1TKDyJTZFi705k88wMKPlhtMAan%2BaP6CWiixX%2BmYlLK9uLHT39McsTT3Pjepi%2FC5jZnFR%2BQ2ukC3GzcnfE0%2Fl0Wlgl9F35S2NdozI9yxF12vZMbeaUmgCJjjVbPTgycO3RXIwBZsGk160SykG3dm5t41XE4UenIA63RWZpZy0VGk0Xig0eBYc1rhjseoBlN2Eo3mEh5BBVMEZvqUfkXDN%2FrHEN4R%2B5dWieGqNhuHbwok1MlY%2BhRWnceMMju9cOjqZtAk3Mf6hkubHBXNKj%2Fd9HdlfrhnR62dyBaCZOIn%2FSvzrnJ%2BewX8QJfG8Psl7CKK8Q2zwnqF6z0r3GXBWb6MZ7XJZkGtx0%2BAwY%2FjJ2z8EV38caF%2B2IZ1KJd1OMVdrS0P2jYbVQ3QTwIZhHGc5SQ%2FmyMxR2VsESuRxnGzJhuhxQTnkY1XxOQFBNnBkt6GHgzu1QhejsaP5mLH%2FlRpowsZ73MLCgsq05rZUyZUpyb8iFzUbdgJZb6fdbo%2BPHWW4a38e900op0nDzygRx9gGyPA8ynRPBO%2Fnl%2Bxor9r66njrVq1C%2FHsAxI9JoUXWjyf8S9C0laCRDDoyvi8BjqkAUGHzLOjQkD7Xr%2BfLVdN%2BOF128UERl0wWkLPv9QXmmgGjyFUz%2FHxKdc1XRo0KkxJkbR2vXkMSWxG%2F17bVQb73MrnWFFomqlOLFeiE%2Fm82TiXBCjoIf%2B1EAXGn53Nt%2BCu3vnilyQlPx7Qqn5b6X4LPVHI6oDtL%2F0xvQxyWtNJ3vQ%2BjIrlTHxiDlPMLLiJELmqwTtKASruUj5FO9Dn3tnodhcEHM1e&X-Amz-Signature=b20510054c53110e31d2109225774ba60aa80377e9a2262b5ab66a5da841779b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMXYGVVJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpJ1JJ8o5DngFACNI%2B%2BVQpfhF7eHHPIePsFODfYzBp5AiEAoI4WebrrByPcieFdbZdcPKjWO2zBzCRYaC3Clxs2mj8qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsEj%2BkznCuP6qFc%2BCrcA6RRzTiciKEO2PVsR64%2BC87LoR2hePReda8pmeGfHDImq6moqjow9M4YNo9kDGr9UJX%2BXeYsaI60oynY5%2FYt4daLapRdJJoFh46YaYGX7%2B%2F7B3INTFjorCglAOa4JdRKR6DBIILDkDydkC0l4pVHnrT2aTYkt5Y%2FG5Usv5Mv86OcunUMTMm2cFRhCHtnUenACYi6GfE5QUaO661Por%2Fhs%2B%2F%2FoiQJDmIgO1F84%2BYFIf23vG4PoDx3mT96WT5p%2F0IsOFEX%2BR9IhfIL8a%2FTyc8kDZaOLfZEIg4NJBEIfRrG10TISLxrvYmSyFhH9TzYmOlTCzq42YxyTWvVxugp48xmxVKO4SflQjrwG2srEHdLBY8Nu8cp1jfRWBH8nFl5hedl02CY5iQZDMw0jp6OWbUZO9Zw0FmYbpf8oEvLrGmfqpyke7EuiK8z9smnRWw7jq4gLUpdIW18I%2Fs4RiQlv%2BOtAlDc0K2hs3%2FfYjaNBC0xW8c1M7PQAl7U3%2FFjyBemWrIM960rt1h%2BeKt6B%2BrJbxWkbQrUGpIot%2B10mXiAlcexQK5p7YuOEg7BXobnx%2FaJxtMN8OEnLs1yrV3jq33vM6NaBr8BSuGVDdVX1lYsw6Z5amRGT0PcOWRYXCy5li%2BOMI%2FK%2BLwGOqUBFPtWS%2BFb8YyoJhXbGROu7Wg6%2BY4cZVX9nSSe9ZgTzSCScs75mq0tnB0RzSGkXWNgH7KpFre0bHKW3eOITcladtAZCjM4N1NDu3CXcUclwqCV%2B2G6PIDDyh7DKIAGqq0WNUIZ2ejZMJhp2x%2FGh%2BR3AAEZ%2FYbLQjkXSn9GByPhCleSE%2Bat5hvqlGjtMVsny9q8REmdWd9Q89nF3o2z9SzPN%2B0Msmos&X-Amz-Signature=89ea7a6af889f588911e8e470208e9eea4454aa2c9972ff843dacb42bfcc43b0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMXYGVVJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T151527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpJ1JJ8o5DngFACNI%2B%2BVQpfhF7eHHPIePsFODfYzBp5AiEAoI4WebrrByPcieFdbZdcPKjWO2zBzCRYaC3Clxs2mj8qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsEj%2BkznCuP6qFc%2BCrcA6RRzTiciKEO2PVsR64%2BC87LoR2hePReda8pmeGfHDImq6moqjow9M4YNo9kDGr9UJX%2BXeYsaI60oynY5%2FYt4daLapRdJJoFh46YaYGX7%2B%2F7B3INTFjorCglAOa4JdRKR6DBIILDkDydkC0l4pVHnrT2aTYkt5Y%2FG5Usv5Mv86OcunUMTMm2cFRhCHtnUenACYi6GfE5QUaO661Por%2Fhs%2B%2F%2FoiQJDmIgO1F84%2BYFIf23vG4PoDx3mT96WT5p%2F0IsOFEX%2BR9IhfIL8a%2FTyc8kDZaOLfZEIg4NJBEIfRrG10TISLxrvYmSyFhH9TzYmOlTCzq42YxyTWvVxugp48xmxVKO4SflQjrwG2srEHdLBY8Nu8cp1jfRWBH8nFl5hedl02CY5iQZDMw0jp6OWbUZO9Zw0FmYbpf8oEvLrGmfqpyke7EuiK8z9smnRWw7jq4gLUpdIW18I%2Fs4RiQlv%2BOtAlDc0K2hs3%2FfYjaNBC0xW8c1M7PQAl7U3%2FFjyBemWrIM960rt1h%2BeKt6B%2BrJbxWkbQrUGpIot%2B10mXiAlcexQK5p7YuOEg7BXobnx%2FaJxtMN8OEnLs1yrV3jq33vM6NaBr8BSuGVDdVX1lYsw6Z5amRGT0PcOWRYXCy5li%2BOMI%2FK%2BLwGOqUBFPtWS%2BFb8YyoJhXbGROu7Wg6%2BY4cZVX9nSSe9ZgTzSCScs75mq0tnB0RzSGkXWNgH7KpFre0bHKW3eOITcladtAZCjM4N1NDu3CXcUclwqCV%2B2G6PIDDyh7DKIAGqq0WNUIZ2ejZMJhp2x%2FGh%2BR3AAEZ%2FYbLQjkXSn9GByPhCleSE%2Bat5hvqlGjtMVsny9q8REmdWd9Q89nF3o2z9SzPN%2B0Msmos&X-Amz-Signature=92451cfd27ef815b89f3b793d4fc121b7f27d3d4b7e37194fb92f26a13fcceca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
