

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LORLNPO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQ8RglXLEipSLW8MDLSdze1wP78xcWiffjj7YIVgTHWAiB8UgoP0nVZwF82RVog%2BgRKrqrQz6IQHa6btLgYee40XCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6dt0ThEoOIV%2BFaTKtwD4P6va%2Bgo3%2FYjdxPr6eJD%2BjtqpC90cpoQuK11%2BzkaQdUwY2sRYQkAiFBaa9pzyDvJL%2FXDfH1P3JPilPUoGSbDKQoqjRraBA2PPfOtGHjGLtdbxSTGmXzkP8hDMFgc1gQXl4iVx4cSZ9WhXkPj3r%2BK2TX5WqTVZl4w4ilIPC43t%2FMk%2B2YqDcEgkK%2Fs3uWXQnMaY1IV%2FsY3r29z2CKbfKyGk0eijGShA5OHw0%2FHmzZ0jW7jdMVPd8wPlKRNqRPwr8blg7KL%2FyJF6MnMtJ%2Bo6ZtvcidpFGyQCpK54ywwHBwQuI7SdOImaAvfJG6H2x0fhBw9S7dR8HrEy4uS%2BDU6yRLei3VwsXt9ZUD7THuYh3P%2FP3bbOKmipn0yY8N%2Fa4TyjYC4v9xB8pibxV7kSfQ1DH0XZL3Nb3vWGs%2FPvci2qq26USzwlJILyI%2ByUtRMSFikS4%2BKqNFL6qEOaZejgURYjUMUs97NIHgavfdPcKhuow1jKPt00Ta2%2BMyLgLkdY433PX9DTNY%2FAEzKTny%2B7cD7E8tEzvACy8jKzcosS7CieneDDSJiIhVzRvkRwcPHdj4H1g7hamI9XexRjorw9e4vubTAlz3V%2FoOZxwGr0RU9bNqqepKTromdb%2FxMaQzFpRAwmdX%2BvAY6pgErYzyrfx68BAKE86BbCcACYlwlZW89pT4zePgH503ukhNPerpNbrAJXJWimMCYBD%2BLbmrviT%2F2OH8R%2FXsE8BCdQuN64BhEBLGQQ%2B9V9BeWrItF8RkmQzwVrFlNSJXeGwfzZ2oqHnMkVpRKK9rfluK8EzYwTdI9YFzJx8EVgdRg1CO%2BIKpeoW7X7nFQLujTnHY3GPIgMimXYcVmuWsUQLjqPB7LSGlT&X-Amz-Signature=b922b207e479d5e8b35dea8e921b09f86aa39e77beca0dd26a1b5f44d376f794&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LORLNPO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQ8RglXLEipSLW8MDLSdze1wP78xcWiffjj7YIVgTHWAiB8UgoP0nVZwF82RVog%2BgRKrqrQz6IQHa6btLgYee40XCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6dt0ThEoOIV%2BFaTKtwD4P6va%2Bgo3%2FYjdxPr6eJD%2BjtqpC90cpoQuK11%2BzkaQdUwY2sRYQkAiFBaa9pzyDvJL%2FXDfH1P3JPilPUoGSbDKQoqjRraBA2PPfOtGHjGLtdbxSTGmXzkP8hDMFgc1gQXl4iVx4cSZ9WhXkPj3r%2BK2TX5WqTVZl4w4ilIPC43t%2FMk%2B2YqDcEgkK%2Fs3uWXQnMaY1IV%2FsY3r29z2CKbfKyGk0eijGShA5OHw0%2FHmzZ0jW7jdMVPd8wPlKRNqRPwr8blg7KL%2FyJF6MnMtJ%2Bo6ZtvcidpFGyQCpK54ywwHBwQuI7SdOImaAvfJG6H2x0fhBw9S7dR8HrEy4uS%2BDU6yRLei3VwsXt9ZUD7THuYh3P%2FP3bbOKmipn0yY8N%2Fa4TyjYC4v9xB8pibxV7kSfQ1DH0XZL3Nb3vWGs%2FPvci2qq26USzwlJILyI%2ByUtRMSFikS4%2BKqNFL6qEOaZejgURYjUMUs97NIHgavfdPcKhuow1jKPt00Ta2%2BMyLgLkdY433PX9DTNY%2FAEzKTny%2B7cD7E8tEzvACy8jKzcosS7CieneDDSJiIhVzRvkRwcPHdj4H1g7hamI9XexRjorw9e4vubTAlz3V%2FoOZxwGr0RU9bNqqepKTromdb%2FxMaQzFpRAwmdX%2BvAY6pgErYzyrfx68BAKE86BbCcACYlwlZW89pT4zePgH503ukhNPerpNbrAJXJWimMCYBD%2BLbmrviT%2F2OH8R%2FXsE8BCdQuN64BhEBLGQQ%2B9V9BeWrItF8RkmQzwVrFlNSJXeGwfzZ2oqHnMkVpRKK9rfluK8EzYwTdI9YFzJx8EVgdRg1CO%2BIKpeoW7X7nFQLujTnHY3GPIgMimXYcVmuWsUQLjqPB7LSGlT&X-Amz-Signature=c707ba4ef508d132fac56e63d73a63e4ae20cdfbf15f8f5d664b1116e985ff83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LORLNPO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQ8RglXLEipSLW8MDLSdze1wP78xcWiffjj7YIVgTHWAiB8UgoP0nVZwF82RVog%2BgRKrqrQz6IQHa6btLgYee40XCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6dt0ThEoOIV%2BFaTKtwD4P6va%2Bgo3%2FYjdxPr6eJD%2BjtqpC90cpoQuK11%2BzkaQdUwY2sRYQkAiFBaa9pzyDvJL%2FXDfH1P3JPilPUoGSbDKQoqjRraBA2PPfOtGHjGLtdbxSTGmXzkP8hDMFgc1gQXl4iVx4cSZ9WhXkPj3r%2BK2TX5WqTVZl4w4ilIPC43t%2FMk%2B2YqDcEgkK%2Fs3uWXQnMaY1IV%2FsY3r29z2CKbfKyGk0eijGShA5OHw0%2FHmzZ0jW7jdMVPd8wPlKRNqRPwr8blg7KL%2FyJF6MnMtJ%2Bo6ZtvcidpFGyQCpK54ywwHBwQuI7SdOImaAvfJG6H2x0fhBw9S7dR8HrEy4uS%2BDU6yRLei3VwsXt9ZUD7THuYh3P%2FP3bbOKmipn0yY8N%2Fa4TyjYC4v9xB8pibxV7kSfQ1DH0XZL3Nb3vWGs%2FPvci2qq26USzwlJILyI%2ByUtRMSFikS4%2BKqNFL6qEOaZejgURYjUMUs97NIHgavfdPcKhuow1jKPt00Ta2%2BMyLgLkdY433PX9DTNY%2FAEzKTny%2B7cD7E8tEzvACy8jKzcosS7CieneDDSJiIhVzRvkRwcPHdj4H1g7hamI9XexRjorw9e4vubTAlz3V%2FoOZxwGr0RU9bNqqepKTromdb%2FxMaQzFpRAwmdX%2BvAY6pgErYzyrfx68BAKE86BbCcACYlwlZW89pT4zePgH503ukhNPerpNbrAJXJWimMCYBD%2BLbmrviT%2F2OH8R%2FXsE8BCdQuN64BhEBLGQQ%2B9V9BeWrItF8RkmQzwVrFlNSJXeGwfzZ2oqHnMkVpRKK9rfluK8EzYwTdI9YFzJx8EVgdRg1CO%2BIKpeoW7X7nFQLujTnHY3GPIgMimXYcVmuWsUQLjqPB7LSGlT&X-Amz-Signature=2ba9e0b6f92d62cc61773b8d1733ae86b37a60969f3bc8ccfd8f72684402d49d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LORLNPO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQ8RglXLEipSLW8MDLSdze1wP78xcWiffjj7YIVgTHWAiB8UgoP0nVZwF82RVog%2BgRKrqrQz6IQHa6btLgYee40XCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6dt0ThEoOIV%2BFaTKtwD4P6va%2Bgo3%2FYjdxPr6eJD%2BjtqpC90cpoQuK11%2BzkaQdUwY2sRYQkAiFBaa9pzyDvJL%2FXDfH1P3JPilPUoGSbDKQoqjRraBA2PPfOtGHjGLtdbxSTGmXzkP8hDMFgc1gQXl4iVx4cSZ9WhXkPj3r%2BK2TX5WqTVZl4w4ilIPC43t%2FMk%2B2YqDcEgkK%2Fs3uWXQnMaY1IV%2FsY3r29z2CKbfKyGk0eijGShA5OHw0%2FHmzZ0jW7jdMVPd8wPlKRNqRPwr8blg7KL%2FyJF6MnMtJ%2Bo6ZtvcidpFGyQCpK54ywwHBwQuI7SdOImaAvfJG6H2x0fhBw9S7dR8HrEy4uS%2BDU6yRLei3VwsXt9ZUD7THuYh3P%2FP3bbOKmipn0yY8N%2Fa4TyjYC4v9xB8pibxV7kSfQ1DH0XZL3Nb3vWGs%2FPvci2qq26USzwlJILyI%2ByUtRMSFikS4%2BKqNFL6qEOaZejgURYjUMUs97NIHgavfdPcKhuow1jKPt00Ta2%2BMyLgLkdY433PX9DTNY%2FAEzKTny%2B7cD7E8tEzvACy8jKzcosS7CieneDDSJiIhVzRvkRwcPHdj4H1g7hamI9XexRjorw9e4vubTAlz3V%2FoOZxwGr0RU9bNqqepKTromdb%2FxMaQzFpRAwmdX%2BvAY6pgErYzyrfx68BAKE86BbCcACYlwlZW89pT4zePgH503ukhNPerpNbrAJXJWimMCYBD%2BLbmrviT%2F2OH8R%2FXsE8BCdQuN64BhEBLGQQ%2B9V9BeWrItF8RkmQzwVrFlNSJXeGwfzZ2oqHnMkVpRKK9rfluK8EzYwTdI9YFzJx8EVgdRg1CO%2BIKpeoW7X7nFQLujTnHY3GPIgMimXYcVmuWsUQLjqPB7LSGlT&X-Amz-Signature=56ad2d649e35ea7f2090a3bf631dccab72b14a7d0d98e82a5da98d190d035bb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LORLNPO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQ8RglXLEipSLW8MDLSdze1wP78xcWiffjj7YIVgTHWAiB8UgoP0nVZwF82RVog%2BgRKrqrQz6IQHa6btLgYee40XCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6dt0ThEoOIV%2BFaTKtwD4P6va%2Bgo3%2FYjdxPr6eJD%2BjtqpC90cpoQuK11%2BzkaQdUwY2sRYQkAiFBaa9pzyDvJL%2FXDfH1P3JPilPUoGSbDKQoqjRraBA2PPfOtGHjGLtdbxSTGmXzkP8hDMFgc1gQXl4iVx4cSZ9WhXkPj3r%2BK2TX5WqTVZl4w4ilIPC43t%2FMk%2B2YqDcEgkK%2Fs3uWXQnMaY1IV%2FsY3r29z2CKbfKyGk0eijGShA5OHw0%2FHmzZ0jW7jdMVPd8wPlKRNqRPwr8blg7KL%2FyJF6MnMtJ%2Bo6ZtvcidpFGyQCpK54ywwHBwQuI7SdOImaAvfJG6H2x0fhBw9S7dR8HrEy4uS%2BDU6yRLei3VwsXt9ZUD7THuYh3P%2FP3bbOKmipn0yY8N%2Fa4TyjYC4v9xB8pibxV7kSfQ1DH0XZL3Nb3vWGs%2FPvci2qq26USzwlJILyI%2ByUtRMSFikS4%2BKqNFL6qEOaZejgURYjUMUs97NIHgavfdPcKhuow1jKPt00Ta2%2BMyLgLkdY433PX9DTNY%2FAEzKTny%2B7cD7E8tEzvACy8jKzcosS7CieneDDSJiIhVzRvkRwcPHdj4H1g7hamI9XexRjorw9e4vubTAlz3V%2FoOZxwGr0RU9bNqqepKTromdb%2FxMaQzFpRAwmdX%2BvAY6pgErYzyrfx68BAKE86BbCcACYlwlZW89pT4zePgH503ukhNPerpNbrAJXJWimMCYBD%2BLbmrviT%2F2OH8R%2FXsE8BCdQuN64BhEBLGQQ%2B9V9BeWrItF8RkmQzwVrFlNSJXeGwfzZ2oqHnMkVpRKK9rfluK8EzYwTdI9YFzJx8EVgdRg1CO%2BIKpeoW7X7nFQLujTnHY3GPIgMimXYcVmuWsUQLjqPB7LSGlT&X-Amz-Signature=5a27ff3a7494f97df35487bfc0af9e8251bb8306dac8a49bd61c05c7683d164b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LORLNPO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQ8RglXLEipSLW8MDLSdze1wP78xcWiffjj7YIVgTHWAiB8UgoP0nVZwF82RVog%2BgRKrqrQz6IQHa6btLgYee40XCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6dt0ThEoOIV%2BFaTKtwD4P6va%2Bgo3%2FYjdxPr6eJD%2BjtqpC90cpoQuK11%2BzkaQdUwY2sRYQkAiFBaa9pzyDvJL%2FXDfH1P3JPilPUoGSbDKQoqjRraBA2PPfOtGHjGLtdbxSTGmXzkP8hDMFgc1gQXl4iVx4cSZ9WhXkPj3r%2BK2TX5WqTVZl4w4ilIPC43t%2FMk%2B2YqDcEgkK%2Fs3uWXQnMaY1IV%2FsY3r29z2CKbfKyGk0eijGShA5OHw0%2FHmzZ0jW7jdMVPd8wPlKRNqRPwr8blg7KL%2FyJF6MnMtJ%2Bo6ZtvcidpFGyQCpK54ywwHBwQuI7SdOImaAvfJG6H2x0fhBw9S7dR8HrEy4uS%2BDU6yRLei3VwsXt9ZUD7THuYh3P%2FP3bbOKmipn0yY8N%2Fa4TyjYC4v9xB8pibxV7kSfQ1DH0XZL3Nb3vWGs%2FPvci2qq26USzwlJILyI%2ByUtRMSFikS4%2BKqNFL6qEOaZejgURYjUMUs97NIHgavfdPcKhuow1jKPt00Ta2%2BMyLgLkdY433PX9DTNY%2FAEzKTny%2B7cD7E8tEzvACy8jKzcosS7CieneDDSJiIhVzRvkRwcPHdj4H1g7hamI9XexRjorw9e4vubTAlz3V%2FoOZxwGr0RU9bNqqepKTromdb%2FxMaQzFpRAwmdX%2BvAY6pgErYzyrfx68BAKE86BbCcACYlwlZW89pT4zePgH503ukhNPerpNbrAJXJWimMCYBD%2BLbmrviT%2F2OH8R%2FXsE8BCdQuN64BhEBLGQQ%2B9V9BeWrItF8RkmQzwVrFlNSJXeGwfzZ2oqHnMkVpRKK9rfluK8EzYwTdI9YFzJx8EVgdRg1CO%2BIKpeoW7X7nFQLujTnHY3GPIgMimXYcVmuWsUQLjqPB7LSGlT&X-Amz-Signature=b1c8c6a97bf2d939982e228d58fd7548e58110768e7558aac14e685197673840&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LORLNPO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQ8RglXLEipSLW8MDLSdze1wP78xcWiffjj7YIVgTHWAiB8UgoP0nVZwF82RVog%2BgRKrqrQz6IQHa6btLgYee40XCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6dt0ThEoOIV%2BFaTKtwD4P6va%2Bgo3%2FYjdxPr6eJD%2BjtqpC90cpoQuK11%2BzkaQdUwY2sRYQkAiFBaa9pzyDvJL%2FXDfH1P3JPilPUoGSbDKQoqjRraBA2PPfOtGHjGLtdbxSTGmXzkP8hDMFgc1gQXl4iVx4cSZ9WhXkPj3r%2BK2TX5WqTVZl4w4ilIPC43t%2FMk%2B2YqDcEgkK%2Fs3uWXQnMaY1IV%2FsY3r29z2CKbfKyGk0eijGShA5OHw0%2FHmzZ0jW7jdMVPd8wPlKRNqRPwr8blg7KL%2FyJF6MnMtJ%2Bo6ZtvcidpFGyQCpK54ywwHBwQuI7SdOImaAvfJG6H2x0fhBw9S7dR8HrEy4uS%2BDU6yRLei3VwsXt9ZUD7THuYh3P%2FP3bbOKmipn0yY8N%2Fa4TyjYC4v9xB8pibxV7kSfQ1DH0XZL3Nb3vWGs%2FPvci2qq26USzwlJILyI%2ByUtRMSFikS4%2BKqNFL6qEOaZejgURYjUMUs97NIHgavfdPcKhuow1jKPt00Ta2%2BMyLgLkdY433PX9DTNY%2FAEzKTny%2B7cD7E8tEzvACy8jKzcosS7CieneDDSJiIhVzRvkRwcPHdj4H1g7hamI9XexRjorw9e4vubTAlz3V%2FoOZxwGr0RU9bNqqepKTromdb%2FxMaQzFpRAwmdX%2BvAY6pgErYzyrfx68BAKE86BbCcACYlwlZW89pT4zePgH503ukhNPerpNbrAJXJWimMCYBD%2BLbmrviT%2F2OH8R%2FXsE8BCdQuN64BhEBLGQQ%2B9V9BeWrItF8RkmQzwVrFlNSJXeGwfzZ2oqHnMkVpRKK9rfluK8EzYwTdI9YFzJx8EVgdRg1CO%2BIKpeoW7X7nFQLujTnHY3GPIgMimXYcVmuWsUQLjqPB7LSGlT&X-Amz-Signature=e68ad300c38e99c5fae4da4e2fa6790db3164766f6038f2cf3f2363b798ef3dd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LORLNPO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQ8RglXLEipSLW8MDLSdze1wP78xcWiffjj7YIVgTHWAiB8UgoP0nVZwF82RVog%2BgRKrqrQz6IQHa6btLgYee40XCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMK6dt0ThEoOIV%2BFaTKtwD4P6va%2Bgo3%2FYjdxPr6eJD%2BjtqpC90cpoQuK11%2BzkaQdUwY2sRYQkAiFBaa9pzyDvJL%2FXDfH1P3JPilPUoGSbDKQoqjRraBA2PPfOtGHjGLtdbxSTGmXzkP8hDMFgc1gQXl4iVx4cSZ9WhXkPj3r%2BK2TX5WqTVZl4w4ilIPC43t%2FMk%2B2YqDcEgkK%2Fs3uWXQnMaY1IV%2FsY3r29z2CKbfKyGk0eijGShA5OHw0%2FHmzZ0jW7jdMVPd8wPlKRNqRPwr8blg7KL%2FyJF6MnMtJ%2Bo6ZtvcidpFGyQCpK54ywwHBwQuI7SdOImaAvfJG6H2x0fhBw9S7dR8HrEy4uS%2BDU6yRLei3VwsXt9ZUD7THuYh3P%2FP3bbOKmipn0yY8N%2Fa4TyjYC4v9xB8pibxV7kSfQ1DH0XZL3Nb3vWGs%2FPvci2qq26USzwlJILyI%2ByUtRMSFikS4%2BKqNFL6qEOaZejgURYjUMUs97NIHgavfdPcKhuow1jKPt00Ta2%2BMyLgLkdY433PX9DTNY%2FAEzKTny%2B7cD7E8tEzvACy8jKzcosS7CieneDDSJiIhVzRvkRwcPHdj4H1g7hamI9XexRjorw9e4vubTAlz3V%2FoOZxwGr0RU9bNqqepKTromdb%2FxMaQzFpRAwmdX%2BvAY6pgErYzyrfx68BAKE86BbCcACYlwlZW89pT4zePgH503ukhNPerpNbrAJXJWimMCYBD%2BLbmrviT%2F2OH8R%2FXsE8BCdQuN64BhEBLGQQ%2B9V9BeWrItF8RkmQzwVrFlNSJXeGwfzZ2oqHnMkVpRKK9rfluK8EzYwTdI9YFzJx8EVgdRg1CO%2BIKpeoW7X7nFQLujTnHY3GPIgMimXYcVmuWsUQLjqPB7LSGlT&X-Amz-Signature=1ccb777a026c62f376e4be04505f69c066adca4319639702688b914e368b11db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667L6J2MUZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCWomG4TChknxmswxzy3D%2BFoPQ2N7xQAo2KvnJydHbvAIhAJcEqpoTJhXH0Qm3jwguyvHfzMRxjAO4P1L0jtQlCuBUKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwvJ3wggcLPMM9dKuMq3APrDHaD9v29YUlFKd4nIvhv5Ugu0BB0814HP%2BcqJKXrHLKzN6cx3%2FbfH%2FpjOuxcfJALGp6rtOmAE4HtY9popRkl9p1uoxr3BvYjQx2LqYqmKk6UGfLs%2BEBZpizSBQ06oS%2F7Fcud548Qi%2F9icnO0BbVMjtO7mhXSS76a7z6WmwKowJDnksNaRIv63Fh7Ie7g11v19qILBXvOC%2BO1zjFIi62B%2FUl7PeefmWV3xL9DQ6pD2DCq5d%2F9GY6bP45mE2oRHEfLSd0A1xTib0eDuiMZgdBgIdCdY63B8M%2Bc%2FqlwbL0xtexQpT%2BPVy%2BSMaYyS9Ocp8wcxg7Djzl13pUbB1hB%2Fl%2BLG09C3IVOol%2BeO060CtM2xWvAoX%2FQeSqyB5Um93Q6AXkTP4lgseCBuCJDdFTVQVMC4s%2Bz0JqtK2i7kqWTiaWb17rXIcwgx%2FcqsGb90uC2S7cEqxglplOuuANGg5AVFNkfztSvh1gWmE%2FGKAnX663BReaZLARt%2BpdBK0aSTkh7oX8zlHbi7usdr0F7gnur0zWIe8g%2B0tRlmOShOMoTBx%2F6HddY7q4aY9yNK30vyc%2BUcWqT7V6wRCknxetGP6wPRG6uni60rvRXZKlbQtWuxtqhbY8TlxXmjRVmQRQd2TCz2v68BjqkAQJOBd%2BDMYixJQ6MfTiqo1%2FrGCoGk8utAiu5tTmNrV%2BxPqqLsTS9GyJWrth6hxqReBtMTxBME9xSNOUggvO4pqhaIhJo5o4vigG5c4JqW%2FcQwlXy517861Rf7ppOXJVoywNRVp2%2FBhfQUKTA4AU5xD%2FnVLHgR4II%2BJejletZAt0vK17LFTTr4pEI2Ef227uJQuqaMITeX8aWM2p9NWVCYuEX0BN%2B&X-Amz-Signature=015d160a5b344ffc653333b9fc1ab7b65810c24a06b03af66613b3f8d28e4ab3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIFLIMIF%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDje5MYUSkMvalwArLuxqGgB5dfvV8BQJ9NNRkPoMnGNAiEA7bXTyYSs22S4tE6ZU2Xi0V66UqIpAnpNgYA%2BthnM2jgqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNUno%2BYGidrcBkNJiSrcA8ft%2FOqo3W5UXKlMtB1ePHAwUyWPO0FlT0BML0VvGaC%2F751ktgSkDg9ahykz62UQ7BWloKhIs51B2Aiz4yXaUFDMdT3grqzVcICX5%2BGytGJIvmhpgrov%2FxIv4XtWpeCkSJSHKHwkufwR3ij1taAf34048%2BSegwE6kFJZqoobdhFL%2FJLzthun6oMEuqV7UcgMoLCVDocY5yIF7XHOb%2FfSK%2FpIaPwJGwRfwqFMCkih2liYNx07u%2BznO4tm1oa28S6F3qrqNITOXTgKEcsZmESW89tl3Xsil3cO26KlUuXY5kta9mPRkJg8Z7eTmya9RjoB%2BvuixAbcWIWqUJpn%2FYwreh9DVUpPoChOFHvhVfZeMm3wFpintxpmjcSSXnFsR5AvW3BUfJ2U9%2BiwrEmZk9uXG9hRpr%2FRkrmgfrlqLzECBWnACaeNgHxwtehWErkLPaKiK0U5%2BJdfTNKMT%2FDrPuZpzNHVczpA137VYMmYmAi%2BDypEKA%2BkWB78M8ipePY%2BUOcqTWi8PTS3K84m60zNriQUsAmEKGz%2FLGFHOmgGu8Yp%2F2UxyMFhYlzabkzLypv2WlAXPZrg%2F9fGDeWI8qMCLtI4UYYRYknOC9KQ%2FPAYsIw8wVP4AGj%2B2jg3r94wH1pdMP%2Fe%2FrwGOqUBovvQtfnaeGW%2B%2Fp%2FM1SwHY5ybMORAc%2BeQG4xl7Ch0AKgjW6F6hokC3JEOtuMRCjEShk7%2F3mjOAH2%2Fv%2BBjd9A5RUwVWmWEU4nLaNLjCxPFm%2BoMqeKv1YnApf1nTs9oTNimSeKRBGx%2B02QoXsnliDSY2%2BJ0DUjRZQ5XYU2OBUKZtqhwImIhuXVHxGKnqIGvwxzRUydpO%2FQ6s7jWLo6oEDJfNhxd%2BeZZ&X-Amz-Signature=2cc98703c83ca117ec5e299fa6947b90985d025c2fe893b01f5181d8392f28ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXSWCGDP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC54em4hdIVz6Kc9bzb7f2yHPJllEAl%2FTAQoVCC6grNDwIgd7nMgeuv0TkYrPLwwAR42wMUW4zjc2tfU7ckHoXmxAIqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcfSx4ax8dNSCRE4ircAxARGnVHcsH970oNkEsehGvo8SPqlb2%2BF8y4vDImzKMAgmcEx0Buec8mflNPFL8klxYoS5mpIDe2AjsYLMlrdxg%2BJrOOIRMlBm4cJ7%2F5qiuYxJe20Xu209uyenmD2TgJRHMGjX%2B%2B%2F29BYPZYexcwGiGo74j9QaAFc0i1a%2FUlivLWuBGlO%2BR7y1qdpZepjPdK2C%2Ft1paOgheEY26bTM5vIPae3JBIj%2F13jtmD6xjxLm93EXusVGp9bjeYPoD2O05ur3kpm53mT9PKM9vFJhnkCW3c%2BZ28TV%2BuoUGflAuDNXgLgZjIr3mHxjnE3USd80dTloEQq9pXgvx8GzufFQARJPkQUBUJ4G6K6T3mO84sJTNxtmlBTqdSqllXeMMzYB9zmea%2BVeOdDKRT55UmslDh76tYph2No561TO3JVOi%2B2sZZ16q7Sv4uZM4MHPaj0WnTHx83UIPOFSGzEvUUK0jgMQOQt3WtShhcreV5MXymJdoyH00VqBWKGK62owvTWczHr0bu1jq2qoUOGOqkBpPFODXkEYH%2BITvvL4bbZqz3dt3%2Fc755aT%2FAMYXEHXGdW%2BvBA4gYyfv2kD8NnrCfmgC4QzcSYGgTnXfUOENCDG6WXJ7s7r1FJcdk6o4HkJcfMN%2Fe%2FrwGOqUBSbLXnUQlUp8Kwkz%2B1jGclhsXS6iUdtRw9oM1UubBaMoXwvFoo5%2BHFDqlsw6Wd3V3f3QkBQpMzv40cT%2FXPaZr297k2oOyZDAhqcTbI0ZH%2FinmHGfCiHwcxRWQlWIzRylqmtJUUczlfpRa6%2BK4QZk37%2Blg7FMz7x5q9rocCHgwv2M0b8V%2BTDMVj9WseNCM68Rkk%2Bxsaw7fOs8JvkFDy%2BaoHR%2FGN9O%2F&X-Amz-Signature=c3f8c54bf11fee7a2d2aae0f180d928d25a59872226957dce62a8767fb9b973b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXSWCGDP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC54em4hdIVz6Kc9bzb7f2yHPJllEAl%2FTAQoVCC6grNDwIgd7nMgeuv0TkYrPLwwAR42wMUW4zjc2tfU7ckHoXmxAIqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcfSx4ax8dNSCRE4ircAxARGnVHcsH970oNkEsehGvo8SPqlb2%2BF8y4vDImzKMAgmcEx0Buec8mflNPFL8klxYoS5mpIDe2AjsYLMlrdxg%2BJrOOIRMlBm4cJ7%2F5qiuYxJe20Xu209uyenmD2TgJRHMGjX%2B%2B%2F29BYPZYexcwGiGo74j9QaAFc0i1a%2FUlivLWuBGlO%2BR7y1qdpZepjPdK2C%2Ft1paOgheEY26bTM5vIPae3JBIj%2F13jtmD6xjxLm93EXusVGp9bjeYPoD2O05ur3kpm53mT9PKM9vFJhnkCW3c%2BZ28TV%2BuoUGflAuDNXgLgZjIr3mHxjnE3USd80dTloEQq9pXgvx8GzufFQARJPkQUBUJ4G6K6T3mO84sJTNxtmlBTqdSqllXeMMzYB9zmea%2BVeOdDKRT55UmslDh76tYph2No561TO3JVOi%2B2sZZ16q7Sv4uZM4MHPaj0WnTHx83UIPOFSGzEvUUK0jgMQOQt3WtShhcreV5MXymJdoyH00VqBWKGK62owvTWczHr0bu1jq2qoUOGOqkBpPFODXkEYH%2BITvvL4bbZqz3dt3%2Fc755aT%2FAMYXEHXGdW%2BvBA4gYyfv2kD8NnrCfmgC4QzcSYGgTnXfUOENCDG6WXJ7s7r1FJcdk6o4HkJcfMN%2Fe%2FrwGOqUBSbLXnUQlUp8Kwkz%2B1jGclhsXS6iUdtRw9oM1UubBaMoXwvFoo5%2BHFDqlsw6Wd3V3f3QkBQpMzv40cT%2FXPaZr297k2oOyZDAhqcTbI0ZH%2FinmHGfCiHwcxRWQlWIzRylqmtJUUczlfpRa6%2BK4QZk37%2Blg7FMz7x5q9rocCHgwv2M0b8V%2BTDMVj9WseNCM68Rkk%2Bxsaw7fOs8JvkFDy%2BaoHR%2FGN9O%2F&X-Amz-Signature=1b4d1f702da230474e5de83634d36dc0327eda6c463c8cdd69eba481d803cc7d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
