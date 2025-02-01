

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REDHKE55%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACU7Bg5b7u2dHZLSrxqPdU7y1MAcgEAmsBGOT0CVqzQAiA1ARAC%2Bn%2BrxFK2Ov8uH1GAaJveg%2BJ%2BPKfJPp2xJfhrFiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMra%2FPMwtsiK%2FBjNOzKtwDsl2D1GUnAAsa1wVCzYJJ5U0s2jCO0eXvXxbMNNdwgpeiPreC%2FjTVWQwAX%2BDTt6g5BTNmhm71xcN0jPhZ%2B2XI9Bu0WZn6vx9jhnOyJvBvHptv5gS4mHBL8%2FqWSiUYgvlno6n%2BgCqBHPe5pwrwVx8no9HRJCblbdi6c7EmK5x%2FcOmlSfOYQK6BIBbh8Pj93cxbTlTqIj%2FRU7qxlu3cPBwRxspaJVUFqHwEwB8TII0QZiSHEfZ4DKP%2BRmJNx23N%2BYtFXYyzRyOVcB7mv0BGxhtODhPtIyPqCbh4JgBNZegNHdkwtI8FT4nE2DB7E%2B%2BU8jTscUvD8pRYE9L3OkPvQ2mtVyEHcIgYWMp6vE9nzLDLPdeZFVd9%2FJUFNAdQPGszxj3uqHK02pFI6p7wzTNphPtIqQC6kk9jj%2BZ1RnoUBiEsY7%2F431KtLe%2Bx%2FQncMNL%2BOY5psT%2BJwSOObSx5WG2vtd7HF0wokphOb63Ks801HM35gBTqJsZt9Ape5Z2m7hc0zv%2BVaCPuzQIiZBr01WRBbu1H2zh3AHYMzGlqwpkKWWAQTGC6tUS3qooHkhbFtfJ7IGHqt6nsPnbNnxMDZwSZAxLo4cgX8zTX%2BaCRmApsmNCOT27%2FhceHam%2FLyUJteQcwr%2Bz1vAY6pgHvy85qZpdr7lmOY0TLrIMmAjSkxhuiGTHjClr560Z7YsSmQyq7yB1uoG9GoIfXKuk3dTnqH0%2FTJ5i2MoCdXs486%2FJg%2FB1zp9LIR7xhub70AVhyyzZqWq%2BKEPuHe8SHATqy39MzDx9%2FGTsIhZLSI99hD7ER4EgXq6tjLiByj5ya%2BkuUfLOHtc4f1oVhSui4P%2F%2FlQ5AupVB6Sw7AcDqwadx%2BswOCU7U6&X-Amz-Signature=386cef4e4cf92b601260c40dc914ac747dd3368cb7da3849585d373d48401593&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REDHKE55%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACU7Bg5b7u2dHZLSrxqPdU7y1MAcgEAmsBGOT0CVqzQAiA1ARAC%2Bn%2BrxFK2Ov8uH1GAaJveg%2BJ%2BPKfJPp2xJfhrFiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMra%2FPMwtsiK%2FBjNOzKtwDsl2D1GUnAAsa1wVCzYJJ5U0s2jCO0eXvXxbMNNdwgpeiPreC%2FjTVWQwAX%2BDTt6g5BTNmhm71xcN0jPhZ%2B2XI9Bu0WZn6vx9jhnOyJvBvHptv5gS4mHBL8%2FqWSiUYgvlno6n%2BgCqBHPe5pwrwVx8no9HRJCblbdi6c7EmK5x%2FcOmlSfOYQK6BIBbh8Pj93cxbTlTqIj%2FRU7qxlu3cPBwRxspaJVUFqHwEwB8TII0QZiSHEfZ4DKP%2BRmJNx23N%2BYtFXYyzRyOVcB7mv0BGxhtODhPtIyPqCbh4JgBNZegNHdkwtI8FT4nE2DB7E%2B%2BU8jTscUvD8pRYE9L3OkPvQ2mtVyEHcIgYWMp6vE9nzLDLPdeZFVd9%2FJUFNAdQPGszxj3uqHK02pFI6p7wzTNphPtIqQC6kk9jj%2BZ1RnoUBiEsY7%2F431KtLe%2Bx%2FQncMNL%2BOY5psT%2BJwSOObSx5WG2vtd7HF0wokphOb63Ks801HM35gBTqJsZt9Ape5Z2m7hc0zv%2BVaCPuzQIiZBr01WRBbu1H2zh3AHYMzGlqwpkKWWAQTGC6tUS3qooHkhbFtfJ7IGHqt6nsPnbNnxMDZwSZAxLo4cgX8zTX%2BaCRmApsmNCOT27%2FhceHam%2FLyUJteQcwr%2Bz1vAY6pgHvy85qZpdr7lmOY0TLrIMmAjSkxhuiGTHjClr560Z7YsSmQyq7yB1uoG9GoIfXKuk3dTnqH0%2FTJ5i2MoCdXs486%2FJg%2FB1zp9LIR7xhub70AVhyyzZqWq%2BKEPuHe8SHATqy39MzDx9%2FGTsIhZLSI99hD7ER4EgXq6tjLiByj5ya%2BkuUfLOHtc4f1oVhSui4P%2F%2FlQ5AupVB6Sw7AcDqwadx%2BswOCU7U6&X-Amz-Signature=410e6882a923f4b9d94762f68b18e4adb8a421b283c9479bf0d3670414e5fe77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REDHKE55%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACU7Bg5b7u2dHZLSrxqPdU7y1MAcgEAmsBGOT0CVqzQAiA1ARAC%2Bn%2BrxFK2Ov8uH1GAaJveg%2BJ%2BPKfJPp2xJfhrFiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMra%2FPMwtsiK%2FBjNOzKtwDsl2D1GUnAAsa1wVCzYJJ5U0s2jCO0eXvXxbMNNdwgpeiPreC%2FjTVWQwAX%2BDTt6g5BTNmhm71xcN0jPhZ%2B2XI9Bu0WZn6vx9jhnOyJvBvHptv5gS4mHBL8%2FqWSiUYgvlno6n%2BgCqBHPe5pwrwVx8no9HRJCblbdi6c7EmK5x%2FcOmlSfOYQK6BIBbh8Pj93cxbTlTqIj%2FRU7qxlu3cPBwRxspaJVUFqHwEwB8TII0QZiSHEfZ4DKP%2BRmJNx23N%2BYtFXYyzRyOVcB7mv0BGxhtODhPtIyPqCbh4JgBNZegNHdkwtI8FT4nE2DB7E%2B%2BU8jTscUvD8pRYE9L3OkPvQ2mtVyEHcIgYWMp6vE9nzLDLPdeZFVd9%2FJUFNAdQPGszxj3uqHK02pFI6p7wzTNphPtIqQC6kk9jj%2BZ1RnoUBiEsY7%2F431KtLe%2Bx%2FQncMNL%2BOY5psT%2BJwSOObSx5WG2vtd7HF0wokphOb63Ks801HM35gBTqJsZt9Ape5Z2m7hc0zv%2BVaCPuzQIiZBr01WRBbu1H2zh3AHYMzGlqwpkKWWAQTGC6tUS3qooHkhbFtfJ7IGHqt6nsPnbNnxMDZwSZAxLo4cgX8zTX%2BaCRmApsmNCOT27%2FhceHam%2FLyUJteQcwr%2Bz1vAY6pgHvy85qZpdr7lmOY0TLrIMmAjSkxhuiGTHjClr560Z7YsSmQyq7yB1uoG9GoIfXKuk3dTnqH0%2FTJ5i2MoCdXs486%2FJg%2FB1zp9LIR7xhub70AVhyyzZqWq%2BKEPuHe8SHATqy39MzDx9%2FGTsIhZLSI99hD7ER4EgXq6tjLiByj5ya%2BkuUfLOHtc4f1oVhSui4P%2F%2FlQ5AupVB6Sw7AcDqwadx%2BswOCU7U6&X-Amz-Signature=48cfb4799ba6ffa3801102b42290732d0788f3bd896d6bac1b4b97c4d08325a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REDHKE55%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACU7Bg5b7u2dHZLSrxqPdU7y1MAcgEAmsBGOT0CVqzQAiA1ARAC%2Bn%2BrxFK2Ov8uH1GAaJveg%2BJ%2BPKfJPp2xJfhrFiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMra%2FPMwtsiK%2FBjNOzKtwDsl2D1GUnAAsa1wVCzYJJ5U0s2jCO0eXvXxbMNNdwgpeiPreC%2FjTVWQwAX%2BDTt6g5BTNmhm71xcN0jPhZ%2B2XI9Bu0WZn6vx9jhnOyJvBvHptv5gS4mHBL8%2FqWSiUYgvlno6n%2BgCqBHPe5pwrwVx8no9HRJCblbdi6c7EmK5x%2FcOmlSfOYQK6BIBbh8Pj93cxbTlTqIj%2FRU7qxlu3cPBwRxspaJVUFqHwEwB8TII0QZiSHEfZ4DKP%2BRmJNx23N%2BYtFXYyzRyOVcB7mv0BGxhtODhPtIyPqCbh4JgBNZegNHdkwtI8FT4nE2DB7E%2B%2BU8jTscUvD8pRYE9L3OkPvQ2mtVyEHcIgYWMp6vE9nzLDLPdeZFVd9%2FJUFNAdQPGszxj3uqHK02pFI6p7wzTNphPtIqQC6kk9jj%2BZ1RnoUBiEsY7%2F431KtLe%2Bx%2FQncMNL%2BOY5psT%2BJwSOObSx5WG2vtd7HF0wokphOb63Ks801HM35gBTqJsZt9Ape5Z2m7hc0zv%2BVaCPuzQIiZBr01WRBbu1H2zh3AHYMzGlqwpkKWWAQTGC6tUS3qooHkhbFtfJ7IGHqt6nsPnbNnxMDZwSZAxLo4cgX8zTX%2BaCRmApsmNCOT27%2FhceHam%2FLyUJteQcwr%2Bz1vAY6pgHvy85qZpdr7lmOY0TLrIMmAjSkxhuiGTHjClr560Z7YsSmQyq7yB1uoG9GoIfXKuk3dTnqH0%2FTJ5i2MoCdXs486%2FJg%2FB1zp9LIR7xhub70AVhyyzZqWq%2BKEPuHe8SHATqy39MzDx9%2FGTsIhZLSI99hD7ER4EgXq6tjLiByj5ya%2BkuUfLOHtc4f1oVhSui4P%2F%2FlQ5AupVB6Sw7AcDqwadx%2BswOCU7U6&X-Amz-Signature=d52bd4361ec0c189e604eca1ef2f8d873399f5f1c226b23620d053be6a263651&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REDHKE55%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACU7Bg5b7u2dHZLSrxqPdU7y1MAcgEAmsBGOT0CVqzQAiA1ARAC%2Bn%2BrxFK2Ov8uH1GAaJveg%2BJ%2BPKfJPp2xJfhrFiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMra%2FPMwtsiK%2FBjNOzKtwDsl2D1GUnAAsa1wVCzYJJ5U0s2jCO0eXvXxbMNNdwgpeiPreC%2FjTVWQwAX%2BDTt6g5BTNmhm71xcN0jPhZ%2B2XI9Bu0WZn6vx9jhnOyJvBvHptv5gS4mHBL8%2FqWSiUYgvlno6n%2BgCqBHPe5pwrwVx8no9HRJCblbdi6c7EmK5x%2FcOmlSfOYQK6BIBbh8Pj93cxbTlTqIj%2FRU7qxlu3cPBwRxspaJVUFqHwEwB8TII0QZiSHEfZ4DKP%2BRmJNx23N%2BYtFXYyzRyOVcB7mv0BGxhtODhPtIyPqCbh4JgBNZegNHdkwtI8FT4nE2DB7E%2B%2BU8jTscUvD8pRYE9L3OkPvQ2mtVyEHcIgYWMp6vE9nzLDLPdeZFVd9%2FJUFNAdQPGszxj3uqHK02pFI6p7wzTNphPtIqQC6kk9jj%2BZ1RnoUBiEsY7%2F431KtLe%2Bx%2FQncMNL%2BOY5psT%2BJwSOObSx5WG2vtd7HF0wokphOb63Ks801HM35gBTqJsZt9Ape5Z2m7hc0zv%2BVaCPuzQIiZBr01WRBbu1H2zh3AHYMzGlqwpkKWWAQTGC6tUS3qooHkhbFtfJ7IGHqt6nsPnbNnxMDZwSZAxLo4cgX8zTX%2BaCRmApsmNCOT27%2FhceHam%2FLyUJteQcwr%2Bz1vAY6pgHvy85qZpdr7lmOY0TLrIMmAjSkxhuiGTHjClr560Z7YsSmQyq7yB1uoG9GoIfXKuk3dTnqH0%2FTJ5i2MoCdXs486%2FJg%2FB1zp9LIR7xhub70AVhyyzZqWq%2BKEPuHe8SHATqy39MzDx9%2FGTsIhZLSI99hD7ER4EgXq6tjLiByj5ya%2BkuUfLOHtc4f1oVhSui4P%2F%2FlQ5AupVB6Sw7AcDqwadx%2BswOCU7U6&X-Amz-Signature=5e8c36fac3ed32e6b5371da6fe4c19b816c4307701cd7f21d6ba99df39b8c67a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REDHKE55%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACU7Bg5b7u2dHZLSrxqPdU7y1MAcgEAmsBGOT0CVqzQAiA1ARAC%2Bn%2BrxFK2Ov8uH1GAaJveg%2BJ%2BPKfJPp2xJfhrFiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMra%2FPMwtsiK%2FBjNOzKtwDsl2D1GUnAAsa1wVCzYJJ5U0s2jCO0eXvXxbMNNdwgpeiPreC%2FjTVWQwAX%2BDTt6g5BTNmhm71xcN0jPhZ%2B2XI9Bu0WZn6vx9jhnOyJvBvHptv5gS4mHBL8%2FqWSiUYgvlno6n%2BgCqBHPe5pwrwVx8no9HRJCblbdi6c7EmK5x%2FcOmlSfOYQK6BIBbh8Pj93cxbTlTqIj%2FRU7qxlu3cPBwRxspaJVUFqHwEwB8TII0QZiSHEfZ4DKP%2BRmJNx23N%2BYtFXYyzRyOVcB7mv0BGxhtODhPtIyPqCbh4JgBNZegNHdkwtI8FT4nE2DB7E%2B%2BU8jTscUvD8pRYE9L3OkPvQ2mtVyEHcIgYWMp6vE9nzLDLPdeZFVd9%2FJUFNAdQPGszxj3uqHK02pFI6p7wzTNphPtIqQC6kk9jj%2BZ1RnoUBiEsY7%2F431KtLe%2Bx%2FQncMNL%2BOY5psT%2BJwSOObSx5WG2vtd7HF0wokphOb63Ks801HM35gBTqJsZt9Ape5Z2m7hc0zv%2BVaCPuzQIiZBr01WRBbu1H2zh3AHYMzGlqwpkKWWAQTGC6tUS3qooHkhbFtfJ7IGHqt6nsPnbNnxMDZwSZAxLo4cgX8zTX%2BaCRmApsmNCOT27%2FhceHam%2FLyUJteQcwr%2Bz1vAY6pgHvy85qZpdr7lmOY0TLrIMmAjSkxhuiGTHjClr560Z7YsSmQyq7yB1uoG9GoIfXKuk3dTnqH0%2FTJ5i2MoCdXs486%2FJg%2FB1zp9LIR7xhub70AVhyyzZqWq%2BKEPuHe8SHATqy39MzDx9%2FGTsIhZLSI99hD7ER4EgXq6tjLiByj5ya%2BkuUfLOHtc4f1oVhSui4P%2F%2FlQ5AupVB6Sw7AcDqwadx%2BswOCU7U6&X-Amz-Signature=73f63aabe39ab5a0d8dca56bab2a844c762508d87e6f77758189a7511845e0db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REDHKE55%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACU7Bg5b7u2dHZLSrxqPdU7y1MAcgEAmsBGOT0CVqzQAiA1ARAC%2Bn%2BrxFK2Ov8uH1GAaJveg%2BJ%2BPKfJPp2xJfhrFiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMra%2FPMwtsiK%2FBjNOzKtwDsl2D1GUnAAsa1wVCzYJJ5U0s2jCO0eXvXxbMNNdwgpeiPreC%2FjTVWQwAX%2BDTt6g5BTNmhm71xcN0jPhZ%2B2XI9Bu0WZn6vx9jhnOyJvBvHptv5gS4mHBL8%2FqWSiUYgvlno6n%2BgCqBHPe5pwrwVx8no9HRJCblbdi6c7EmK5x%2FcOmlSfOYQK6BIBbh8Pj93cxbTlTqIj%2FRU7qxlu3cPBwRxspaJVUFqHwEwB8TII0QZiSHEfZ4DKP%2BRmJNx23N%2BYtFXYyzRyOVcB7mv0BGxhtODhPtIyPqCbh4JgBNZegNHdkwtI8FT4nE2DB7E%2B%2BU8jTscUvD8pRYE9L3OkPvQ2mtVyEHcIgYWMp6vE9nzLDLPdeZFVd9%2FJUFNAdQPGszxj3uqHK02pFI6p7wzTNphPtIqQC6kk9jj%2BZ1RnoUBiEsY7%2F431KtLe%2Bx%2FQncMNL%2BOY5psT%2BJwSOObSx5WG2vtd7HF0wokphOb63Ks801HM35gBTqJsZt9Ape5Z2m7hc0zv%2BVaCPuzQIiZBr01WRBbu1H2zh3AHYMzGlqwpkKWWAQTGC6tUS3qooHkhbFtfJ7IGHqt6nsPnbNnxMDZwSZAxLo4cgX8zTX%2BaCRmApsmNCOT27%2FhceHam%2FLyUJteQcwr%2Bz1vAY6pgHvy85qZpdr7lmOY0TLrIMmAjSkxhuiGTHjClr560Z7YsSmQyq7yB1uoG9GoIfXKuk3dTnqH0%2FTJ5i2MoCdXs486%2FJg%2FB1zp9LIR7xhub70AVhyyzZqWq%2BKEPuHe8SHATqy39MzDx9%2FGTsIhZLSI99hD7ER4EgXq6tjLiByj5ya%2BkuUfLOHtc4f1oVhSui4P%2F%2FlQ5AupVB6Sw7AcDqwadx%2BswOCU7U6&X-Amz-Signature=c16052db7c94e1fedfa7107e9ccc762b8edc70032c5b1d23335fa6754de9e44c&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REDHKE55%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIACU7Bg5b7u2dHZLSrxqPdU7y1MAcgEAmsBGOT0CVqzQAiA1ARAC%2Bn%2BrxFK2Ov8uH1GAaJveg%2BJ%2BPKfJPp2xJfhrFiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMra%2FPMwtsiK%2FBjNOzKtwDsl2D1GUnAAsa1wVCzYJJ5U0s2jCO0eXvXxbMNNdwgpeiPreC%2FjTVWQwAX%2BDTt6g5BTNmhm71xcN0jPhZ%2B2XI9Bu0WZn6vx9jhnOyJvBvHptv5gS4mHBL8%2FqWSiUYgvlno6n%2BgCqBHPe5pwrwVx8no9HRJCblbdi6c7EmK5x%2FcOmlSfOYQK6BIBbh8Pj93cxbTlTqIj%2FRU7qxlu3cPBwRxspaJVUFqHwEwB8TII0QZiSHEfZ4DKP%2BRmJNx23N%2BYtFXYyzRyOVcB7mv0BGxhtODhPtIyPqCbh4JgBNZegNHdkwtI8FT4nE2DB7E%2B%2BU8jTscUvD8pRYE9L3OkPvQ2mtVyEHcIgYWMp6vE9nzLDLPdeZFVd9%2FJUFNAdQPGszxj3uqHK02pFI6p7wzTNphPtIqQC6kk9jj%2BZ1RnoUBiEsY7%2F431KtLe%2Bx%2FQncMNL%2BOY5psT%2BJwSOObSx5WG2vtd7HF0wokphOb63Ks801HM35gBTqJsZt9Ape5Z2m7hc0zv%2BVaCPuzQIiZBr01WRBbu1H2zh3AHYMzGlqwpkKWWAQTGC6tUS3qooHkhbFtfJ7IGHqt6nsPnbNnxMDZwSZAxLo4cgX8zTX%2BaCRmApsmNCOT27%2FhceHam%2FLyUJteQcwr%2Bz1vAY6pgHvy85qZpdr7lmOY0TLrIMmAjSkxhuiGTHjClr560Z7YsSmQyq7yB1uoG9GoIfXKuk3dTnqH0%2FTJ5i2MoCdXs486%2FJg%2FB1zp9LIR7xhub70AVhyyzZqWq%2BKEPuHe8SHATqy39MzDx9%2FGTsIhZLSI99hD7ER4EgXq6tjLiByj5ya%2BkuUfLOHtc4f1oVhSui4P%2F%2FlQ5AupVB6Sw7AcDqwadx%2BswOCU7U6&X-Amz-Signature=9530d5ac1edade0bef40e8659f3cd8f346b663fbe639a900db9bc0df8049f0cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CZQFOFZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9rbMWwpRrXK8LcbXocEIwbGhrNKsScwisbHrkbYOUzgIgIgq69wzM%2BzL6J%2Bkq3YcZFiPrvLoknbsG%2BOoHlfBKpI8qiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH3hHHneyX9sssQjCircA7LbYBwqvBFBfIzm%2B0nufeS04Qwg90mQW4FC7lDY03R%2FSxhSUigTxQjEvgMMGQpMHJSetDPmejcp%2BDgHOMCo7kKN8YGLVVEgz27K7%2FEWw6ggu1XvjW52%2B7fKOYk%2BJlXY9Ef%2BcNUNS418pjY%2Fifx6xA0xfeHMhZaTm7n53IvgpJalXR6RCPUCYWAhIbi8j8zm8Z9DWGxJ5meRamy2xJw0D7i66cngn4oVsu%2BIzJRiCkPeDvnC0Vuu4zhW2yQj2zhufh%2Bg58EkECRFvoyrogvmeuGCQ2AuKfWhEviOYfzzRqZuTQwJw5N2rdl1eo0BCg%2B0HiTHAYYHs9g8b29d68GDKK97Mz9g2Mi145XxCrVWHBXfJ%2FhvRXM7sC087hsqK%2F7O0M92ACGcEHp3fC5vsHjAMhD11sHadZ%2Fi%2FjhRpAQKmF4DzVD5sldMEmVbcN5b25DERUqTQFxg7OqoYQZGE%2B5%2BPceJE2k%2BGsXhugy6ZkcNyJ3QYKVYqsZRJzZ%2FZ2ZkB%2BIFEAoj9EzTMl6Y4%2F%2BgfzES7tBkqN6o%2BOEusqkHBf3kkwjuGRdcQhVz%2FeViKRUFeqFLotTgbg2%2FYrwfp6hkrXDgd6kwLY%2BJsSutjJ57J4d1bdT6lqn%2Bk4gcAuWwAyk7MM3s9bwGOqUBgf2qVsNMhYTfzj%2FLPLV8GRvEtM7jYdMbGyayC6M1MBNtzGdQn3an%2Fu6QHAlrVLyBkJwOCVLCw4A1Yek6WJ%2F141aFo9Z84ANZsI2%2FtMHGr3BHqlgvQgt6YTrz0LY2kkkXiv0WuxqEO69OxAqzpIlR0MJB38sx5Il7nsR2sgZGBQYmHEDFQUp9Rxs2gg%2FzyEIgDGgE%2FRseMM5ZtV0KHznHiUdDfduJ&X-Amz-Signature=b727d8bae0d59d95357baa345f25ad0782c9527e738242ee152dd57b522fca1f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RGSGFWP%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMIeTW4SJOirGc%2FRn9JNeLH4aFGaX3K81YwNW0h51kRwIhANUSfpGizOWu1J3xkOFy2UbPg4j%2Fq59veBdKFrWspz3dKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcaROqm1WFxflOhlUq3AP6r4KKUa8vwywxRi%2F1ymsHmIGGVsv75HHFDw8Omvl%2F%2F%2FtqiahW9Hx4xdV7sMnbqr7o5SVN1BQAhx4mNKsZHveXft4Lc8N4HQo%2BSdsPJYDrMY%2FmX0s2VIIBWTQFiNs7mh%2BLW7rtBvwsdXpkc8VwKqTyfEmFTQC2Ah4uJcn5Cs4Bd8v6l8R%2BnBOfLZRUK9IkQPHlXYd5TxdafpvQgbl9XcD9HQMm2bgS1iVQfxRVVooPxHvzJBcGbl%2BvSO6Yb2AUw8GLf9lJ4HLWV%2BkcCJbgH4oT35RQfwBrWhvCtUvjvxsrpJf1XTcyNTGgbtfbjlzfgvXjNDuGwMDkEQTtcGaifhlgkp2jXYIZFEsxuoq%2B77b97GVMQ7jciAe2%2FJ1qgs%2FPpOpdRMzdjq%2BKTjc4l7lIvOfZPw3gT%2BntqRHE%2B8fIesgXENurHGMSZTowB2irmq7%2BVD2GdqJrACZ0wiBYVnrsks1hzZnPVDBXDBDTIIcflo3tDgkfciq8m%2FNFl0M6dnKKcHBTIZgpdElQRNurzdnrogH9MdLh6bkD02mtCsxmRlFb8J1ODqyUeeSRROmA52uaZRJOu2T5%2FHRwHgqCU%2Fxpr4SwmsK4MCQFjFfUsGwdiDiSo0Hv686574qFTIzJsjC57PW8BjqkAfDuOF5Q4cvNWt%2B4Em0K5P5E6CYlM5f1B4rBtZgZsmvz%2BgZxw8R8IHNBURVF63UNkiBEfhREPZc86IlTRZODmoGoUmEuUjbYendxojjvWTRp3nXGoJ49MTt1q14uh35U5VkH6432fwAhnEnOL2BVbBjD6QfE%2BlL0Y31Ph1sXbXozejijPz6%2FPf9nduYuvdui7ubDRG1F%2Fyd4d1l2SjjO0APjAsJC&X-Amz-Signature=7f4000e039b3493db07624b19b34c84a11dd5b21c5bf6e7a444700d843400731&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPEDT27R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEiMaQJsG%2FNakitfZukI8hmpHrRbgGWAl9vQOyeiZpJMAiEAytf912pqTepPTHGRQnZ2MCyIc9OtdwGO7n1OECIBLNwqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKys5mcbZXkT3IQIECrcA81lrB1XgOxzpII1CFTe4dBM1DO2Pakvi7BY4fzX3y3VgPVGyg41dlP23y1MMMXLn14fna1eAYkiZQxvagWpfwlzWRJ0%2FSpShi6FU%2B7nmMggI%2Fh5uwgVjtiSmqVRJw5p%2BI9vcEjtcQfIoCJJPtigBM50%2FpKvzQ%2Fxi20CnnE77E7qzsFGjhxiDQOIZp%2Fqdut6%2Bn8iKySy%2F9Doa7NbYKPyWipOEbBmgW1A3kkIav0xRcV9XRfS9nipNBLwRm%2BwaMH8RPruNaJYeTjcPQEUk4BYxAoTWQFR19855sLLbR3MX4ShmhlAiFP%2BGQ13Xss7fA2j4gNdECLAionbGHrnjh3s6uJ7%2BK6TRVRfO%2Blan316CUQfiZHhzrVd4i0m40gj4dhRps1RaUIVjGZJhsXbo9r%2BuFNxlaOyXJJSIR%2BriNc6S6tckXVAe6dgzbgJuH%2FdbLQGTgc%2B7M0GzSELdu15Fsf7elLd%2BmEHnQzbTub8JTY683mZfY7Nfod4IRanjycSRt0%2BVOaetUx7Skv4uVJcJN7ccaO9bm7%2B%2FduKy7he1X7kBuS%2F1XGpGvXNatY30UqJR0wm%2BCeZzuiJoe%2BxICOfQG5AbZ9PuVtpCW4KHO9SEmm35kevQejOL6YQg9kdtD36MK%2Fs9bwGOqUBJjcqJXk2LFkO%2FuktMFQN7jUYj0CFNC2Q3WuT%2FM%2BkgasB9MowpfwOp3wXskCnvs%2FnOP8Lv5lJ7x2UOXTrfp3ev%2BY5hitwO9PltEjBPgVF6zg%2BJkuGFqfMR4vJAzTPH8t1ApmvmyiOfoU87VZ2LpzPjm%2FpHrLT7LdpjPjBCn2ksW1LgsRcoDgqa6WQSGcJAmNejIZemuI08wh93v58VF4qBPi9cMoN&X-Amz-Signature=4b8d548cefc627b5f78c4ee8ece0373c6982c5925b83aa3c5f9b0ee04d46a3aa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPEDT27R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEiMaQJsG%2FNakitfZukI8hmpHrRbgGWAl9vQOyeiZpJMAiEAytf912pqTepPTHGRQnZ2MCyIc9OtdwGO7n1OECIBLNwqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKys5mcbZXkT3IQIECrcA81lrB1XgOxzpII1CFTe4dBM1DO2Pakvi7BY4fzX3y3VgPVGyg41dlP23y1MMMXLn14fna1eAYkiZQxvagWpfwlzWRJ0%2FSpShi6FU%2B7nmMggI%2Fh5uwgVjtiSmqVRJw5p%2BI9vcEjtcQfIoCJJPtigBM50%2FpKvzQ%2Fxi20CnnE77E7qzsFGjhxiDQOIZp%2Fqdut6%2Bn8iKySy%2F9Doa7NbYKPyWipOEbBmgW1A3kkIav0xRcV9XRfS9nipNBLwRm%2BwaMH8RPruNaJYeTjcPQEUk4BYxAoTWQFR19855sLLbR3MX4ShmhlAiFP%2BGQ13Xss7fA2j4gNdECLAionbGHrnjh3s6uJ7%2BK6TRVRfO%2Blan316CUQfiZHhzrVd4i0m40gj4dhRps1RaUIVjGZJhsXbo9r%2BuFNxlaOyXJJSIR%2BriNc6S6tckXVAe6dgzbgJuH%2FdbLQGTgc%2B7M0GzSELdu15Fsf7elLd%2BmEHnQzbTub8JTY683mZfY7Nfod4IRanjycSRt0%2BVOaetUx7Skv4uVJcJN7ccaO9bm7%2B%2FduKy7he1X7kBuS%2F1XGpGvXNatY30UqJR0wm%2BCeZzuiJoe%2BxICOfQG5AbZ9PuVtpCW4KHO9SEmm35kevQejOL6YQg9kdtD36MK%2Fs9bwGOqUBJjcqJXk2LFkO%2FuktMFQN7jUYj0CFNC2Q3WuT%2FM%2BkgasB9MowpfwOp3wXskCnvs%2FnOP8Lv5lJ7x2UOXTrfp3ev%2BY5hitwO9PltEjBPgVF6zg%2BJkuGFqfMR4vJAzTPH8t1ApmvmyiOfoU87VZ2LpzPjm%2FpHrLT7LdpjPjBCn2ksW1LgsRcoDgqa6WQSGcJAmNejIZemuI08wh93v58VF4qBPi9cMoN&X-Amz-Signature=366b6758e5eeba1ca7957bc64199ca7a6907d9df0969bc1d2af37153a821f773&X-Amz-SignedHeaders=host&x-id=GetObject)
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
