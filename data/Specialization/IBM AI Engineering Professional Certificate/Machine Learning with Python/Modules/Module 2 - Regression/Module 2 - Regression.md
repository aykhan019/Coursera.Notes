

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVW2QXEH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKdKoQsNK4RM9vtEGNWfLU4ir6tH%2Ba1b12i7x5PgWIAQIgLjW0mhAqTda9G9TKlKOhbFsR9QhiY5WWSvoU%2Bqyfzm8qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISHyJ1ECWMp%2FbdsCircA3AYEZVqyNq3I5HBmZI%2Bskcq57mVpVxixpgX2Hs7cqVWg3HpuvidtTk9Hgr8yB1Mt3dguIicprORVdp8m5gBQ6aj%2BAE3ILXIKhL2TOzOcg6%2BK1zftsZ0kaGUNH03vdLXOAJpg9eVXf7xDy1GYV27QTMsOe%2BlXEaEeRG%2FeSIlFxWRBsKAZr1%2Fd8cHRENPUMOdZ78zIvZNITtEj2yJAOfUuDFIxBmNVWKf7D1czz8I%2F5opbO5vW9wxqK%2FEuoFpHmtFHNbsLf6RhHo2qnsQuydPcrglILQggnAI7oh6sO2x1KmHW%2Bwi%2BcFXA2vDEzBF4NIwGwxC4sEcvs92cnDrWn2qPbjH%2BxqVjKfzpX5AVegy%2F5haKpfeVW0yIdKQCilGCtgJTarG2iJ2%2FYp1WFGw%2BCwZDGiYLxlpEHxnV4n7%2B7qtpIMl4Sbj2uFU5vE2FvDrN7ySvUpnJUI2tbLJfPgtjheAizB59QKgZbxOKo5YxzLqhrGZa03FftvIgEjT7gyBc76f%2Fn5kQuqcazuLLrCqunJiwmBjhRS9dQukHjzK1D%2BWXUZ%2B5TSoAvFVk84VpoDBtTdqkpJ9jDOPFt2JJyLH9XGduVIlNfVD0SW6Kp35gMTkxbPI7Vpzi4dfTkgzSuwBMKuO77wGOqUBH20NAbmafqxNVFR%2FVh5Nzq1KTXWKKuZhUP432DjX%2BThVYd3POQd0Y3E5sYVFNMthN8ZkdVMRWTDiKz5cfbHdtt%2Be%2FStizRaFmQrgQoZzpBzmpj9ehg54HMzUlqtOtuXhQgEIYG1kE14rr1nQGaFssx42i91JACeWQuiGiNNcvZUwfArX9PJ%2FbKjTWtMt04w%2FoZuFiFb7NARysEkULN3opC%2FvDSiv&X-Amz-Signature=44f03ae11821f305b26216f9d678fc630888f2a741b35ffc32657cd9d41954ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVW2QXEH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKdKoQsNK4RM9vtEGNWfLU4ir6tH%2Ba1b12i7x5PgWIAQIgLjW0mhAqTda9G9TKlKOhbFsR9QhiY5WWSvoU%2Bqyfzm8qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISHyJ1ECWMp%2FbdsCircA3AYEZVqyNq3I5HBmZI%2Bskcq57mVpVxixpgX2Hs7cqVWg3HpuvidtTk9Hgr8yB1Mt3dguIicprORVdp8m5gBQ6aj%2BAE3ILXIKhL2TOzOcg6%2BK1zftsZ0kaGUNH03vdLXOAJpg9eVXf7xDy1GYV27QTMsOe%2BlXEaEeRG%2FeSIlFxWRBsKAZr1%2Fd8cHRENPUMOdZ78zIvZNITtEj2yJAOfUuDFIxBmNVWKf7D1czz8I%2F5opbO5vW9wxqK%2FEuoFpHmtFHNbsLf6RhHo2qnsQuydPcrglILQggnAI7oh6sO2x1KmHW%2Bwi%2BcFXA2vDEzBF4NIwGwxC4sEcvs92cnDrWn2qPbjH%2BxqVjKfzpX5AVegy%2F5haKpfeVW0yIdKQCilGCtgJTarG2iJ2%2FYp1WFGw%2BCwZDGiYLxlpEHxnV4n7%2B7qtpIMl4Sbj2uFU5vE2FvDrN7ySvUpnJUI2tbLJfPgtjheAizB59QKgZbxOKo5YxzLqhrGZa03FftvIgEjT7gyBc76f%2Fn5kQuqcazuLLrCqunJiwmBjhRS9dQukHjzK1D%2BWXUZ%2B5TSoAvFVk84VpoDBtTdqkpJ9jDOPFt2JJyLH9XGduVIlNfVD0SW6Kp35gMTkxbPI7Vpzi4dfTkgzSuwBMKuO77wGOqUBH20NAbmafqxNVFR%2FVh5Nzq1KTXWKKuZhUP432DjX%2BThVYd3POQd0Y3E5sYVFNMthN8ZkdVMRWTDiKz5cfbHdtt%2Be%2FStizRaFmQrgQoZzpBzmpj9ehg54HMzUlqtOtuXhQgEIYG1kE14rr1nQGaFssx42i91JACeWQuiGiNNcvZUwfArX9PJ%2FbKjTWtMt04w%2FoZuFiFb7NARysEkULN3opC%2FvDSiv&X-Amz-Signature=479945d7008bfc45c021c6169790d2cf8f6c40854a96389c48ed2c826341983e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVW2QXEH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKdKoQsNK4RM9vtEGNWfLU4ir6tH%2Ba1b12i7x5PgWIAQIgLjW0mhAqTda9G9TKlKOhbFsR9QhiY5WWSvoU%2Bqyfzm8qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISHyJ1ECWMp%2FbdsCircA3AYEZVqyNq3I5HBmZI%2Bskcq57mVpVxixpgX2Hs7cqVWg3HpuvidtTk9Hgr8yB1Mt3dguIicprORVdp8m5gBQ6aj%2BAE3ILXIKhL2TOzOcg6%2BK1zftsZ0kaGUNH03vdLXOAJpg9eVXf7xDy1GYV27QTMsOe%2BlXEaEeRG%2FeSIlFxWRBsKAZr1%2Fd8cHRENPUMOdZ78zIvZNITtEj2yJAOfUuDFIxBmNVWKf7D1czz8I%2F5opbO5vW9wxqK%2FEuoFpHmtFHNbsLf6RhHo2qnsQuydPcrglILQggnAI7oh6sO2x1KmHW%2Bwi%2BcFXA2vDEzBF4NIwGwxC4sEcvs92cnDrWn2qPbjH%2BxqVjKfzpX5AVegy%2F5haKpfeVW0yIdKQCilGCtgJTarG2iJ2%2FYp1WFGw%2BCwZDGiYLxlpEHxnV4n7%2B7qtpIMl4Sbj2uFU5vE2FvDrN7ySvUpnJUI2tbLJfPgtjheAizB59QKgZbxOKo5YxzLqhrGZa03FftvIgEjT7gyBc76f%2Fn5kQuqcazuLLrCqunJiwmBjhRS9dQukHjzK1D%2BWXUZ%2B5TSoAvFVk84VpoDBtTdqkpJ9jDOPFt2JJyLH9XGduVIlNfVD0SW6Kp35gMTkxbPI7Vpzi4dfTkgzSuwBMKuO77wGOqUBH20NAbmafqxNVFR%2FVh5Nzq1KTXWKKuZhUP432DjX%2BThVYd3POQd0Y3E5sYVFNMthN8ZkdVMRWTDiKz5cfbHdtt%2Be%2FStizRaFmQrgQoZzpBzmpj9ehg54HMzUlqtOtuXhQgEIYG1kE14rr1nQGaFssx42i91JACeWQuiGiNNcvZUwfArX9PJ%2FbKjTWtMt04w%2FoZuFiFb7NARysEkULN3opC%2FvDSiv&X-Amz-Signature=ec4606cb4dc2368f465df2a234b6860c72a6444d5545afa006c5891fd02d7714&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVW2QXEH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKdKoQsNK4RM9vtEGNWfLU4ir6tH%2Ba1b12i7x5PgWIAQIgLjW0mhAqTda9G9TKlKOhbFsR9QhiY5WWSvoU%2Bqyfzm8qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISHyJ1ECWMp%2FbdsCircA3AYEZVqyNq3I5HBmZI%2Bskcq57mVpVxixpgX2Hs7cqVWg3HpuvidtTk9Hgr8yB1Mt3dguIicprORVdp8m5gBQ6aj%2BAE3ILXIKhL2TOzOcg6%2BK1zftsZ0kaGUNH03vdLXOAJpg9eVXf7xDy1GYV27QTMsOe%2BlXEaEeRG%2FeSIlFxWRBsKAZr1%2Fd8cHRENPUMOdZ78zIvZNITtEj2yJAOfUuDFIxBmNVWKf7D1czz8I%2F5opbO5vW9wxqK%2FEuoFpHmtFHNbsLf6RhHo2qnsQuydPcrglILQggnAI7oh6sO2x1KmHW%2Bwi%2BcFXA2vDEzBF4NIwGwxC4sEcvs92cnDrWn2qPbjH%2BxqVjKfzpX5AVegy%2F5haKpfeVW0yIdKQCilGCtgJTarG2iJ2%2FYp1WFGw%2BCwZDGiYLxlpEHxnV4n7%2B7qtpIMl4Sbj2uFU5vE2FvDrN7ySvUpnJUI2tbLJfPgtjheAizB59QKgZbxOKo5YxzLqhrGZa03FftvIgEjT7gyBc76f%2Fn5kQuqcazuLLrCqunJiwmBjhRS9dQukHjzK1D%2BWXUZ%2B5TSoAvFVk84VpoDBtTdqkpJ9jDOPFt2JJyLH9XGduVIlNfVD0SW6Kp35gMTkxbPI7Vpzi4dfTkgzSuwBMKuO77wGOqUBH20NAbmafqxNVFR%2FVh5Nzq1KTXWKKuZhUP432DjX%2BThVYd3POQd0Y3E5sYVFNMthN8ZkdVMRWTDiKz5cfbHdtt%2Be%2FStizRaFmQrgQoZzpBzmpj9ehg54HMzUlqtOtuXhQgEIYG1kE14rr1nQGaFssx42i91JACeWQuiGiNNcvZUwfArX9PJ%2FbKjTWtMt04w%2FoZuFiFb7NARysEkULN3opC%2FvDSiv&X-Amz-Signature=627dd62b9c45c188ec826f8c9858cbb577e13a41861cc22dc3ca5f84964aef47&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVW2QXEH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKdKoQsNK4RM9vtEGNWfLU4ir6tH%2Ba1b12i7x5PgWIAQIgLjW0mhAqTda9G9TKlKOhbFsR9QhiY5WWSvoU%2Bqyfzm8qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISHyJ1ECWMp%2FbdsCircA3AYEZVqyNq3I5HBmZI%2Bskcq57mVpVxixpgX2Hs7cqVWg3HpuvidtTk9Hgr8yB1Mt3dguIicprORVdp8m5gBQ6aj%2BAE3ILXIKhL2TOzOcg6%2BK1zftsZ0kaGUNH03vdLXOAJpg9eVXf7xDy1GYV27QTMsOe%2BlXEaEeRG%2FeSIlFxWRBsKAZr1%2Fd8cHRENPUMOdZ78zIvZNITtEj2yJAOfUuDFIxBmNVWKf7D1czz8I%2F5opbO5vW9wxqK%2FEuoFpHmtFHNbsLf6RhHo2qnsQuydPcrglILQggnAI7oh6sO2x1KmHW%2Bwi%2BcFXA2vDEzBF4NIwGwxC4sEcvs92cnDrWn2qPbjH%2BxqVjKfzpX5AVegy%2F5haKpfeVW0yIdKQCilGCtgJTarG2iJ2%2FYp1WFGw%2BCwZDGiYLxlpEHxnV4n7%2B7qtpIMl4Sbj2uFU5vE2FvDrN7ySvUpnJUI2tbLJfPgtjheAizB59QKgZbxOKo5YxzLqhrGZa03FftvIgEjT7gyBc76f%2Fn5kQuqcazuLLrCqunJiwmBjhRS9dQukHjzK1D%2BWXUZ%2B5TSoAvFVk84VpoDBtTdqkpJ9jDOPFt2JJyLH9XGduVIlNfVD0SW6Kp35gMTkxbPI7Vpzi4dfTkgzSuwBMKuO77wGOqUBH20NAbmafqxNVFR%2FVh5Nzq1KTXWKKuZhUP432DjX%2BThVYd3POQd0Y3E5sYVFNMthN8ZkdVMRWTDiKz5cfbHdtt%2Be%2FStizRaFmQrgQoZzpBzmpj9ehg54HMzUlqtOtuXhQgEIYG1kE14rr1nQGaFssx42i91JACeWQuiGiNNcvZUwfArX9PJ%2FbKjTWtMt04w%2FoZuFiFb7NARysEkULN3opC%2FvDSiv&X-Amz-Signature=8de15fd6d00005f3843460bcd5995d0f2650a604c4d454f722f45fc5c4b3224f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVW2QXEH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKdKoQsNK4RM9vtEGNWfLU4ir6tH%2Ba1b12i7x5PgWIAQIgLjW0mhAqTda9G9TKlKOhbFsR9QhiY5WWSvoU%2Bqyfzm8qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISHyJ1ECWMp%2FbdsCircA3AYEZVqyNq3I5HBmZI%2Bskcq57mVpVxixpgX2Hs7cqVWg3HpuvidtTk9Hgr8yB1Mt3dguIicprORVdp8m5gBQ6aj%2BAE3ILXIKhL2TOzOcg6%2BK1zftsZ0kaGUNH03vdLXOAJpg9eVXf7xDy1GYV27QTMsOe%2BlXEaEeRG%2FeSIlFxWRBsKAZr1%2Fd8cHRENPUMOdZ78zIvZNITtEj2yJAOfUuDFIxBmNVWKf7D1czz8I%2F5opbO5vW9wxqK%2FEuoFpHmtFHNbsLf6RhHo2qnsQuydPcrglILQggnAI7oh6sO2x1KmHW%2Bwi%2BcFXA2vDEzBF4NIwGwxC4sEcvs92cnDrWn2qPbjH%2BxqVjKfzpX5AVegy%2F5haKpfeVW0yIdKQCilGCtgJTarG2iJ2%2FYp1WFGw%2BCwZDGiYLxlpEHxnV4n7%2B7qtpIMl4Sbj2uFU5vE2FvDrN7ySvUpnJUI2tbLJfPgtjheAizB59QKgZbxOKo5YxzLqhrGZa03FftvIgEjT7gyBc76f%2Fn5kQuqcazuLLrCqunJiwmBjhRS9dQukHjzK1D%2BWXUZ%2B5TSoAvFVk84VpoDBtTdqkpJ9jDOPFt2JJyLH9XGduVIlNfVD0SW6Kp35gMTkxbPI7Vpzi4dfTkgzSuwBMKuO77wGOqUBH20NAbmafqxNVFR%2FVh5Nzq1KTXWKKuZhUP432DjX%2BThVYd3POQd0Y3E5sYVFNMthN8ZkdVMRWTDiKz5cfbHdtt%2Be%2FStizRaFmQrgQoZzpBzmpj9ehg54HMzUlqtOtuXhQgEIYG1kE14rr1nQGaFssx42i91JACeWQuiGiNNcvZUwfArX9PJ%2FbKjTWtMt04w%2FoZuFiFb7NARysEkULN3opC%2FvDSiv&X-Amz-Signature=108c23182a1323a314c9c6b09cad653a370c3c0c36489bf1d4f4ee1e9d828c1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVW2QXEH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKdKoQsNK4RM9vtEGNWfLU4ir6tH%2Ba1b12i7x5PgWIAQIgLjW0mhAqTda9G9TKlKOhbFsR9QhiY5WWSvoU%2Bqyfzm8qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISHyJ1ECWMp%2FbdsCircA3AYEZVqyNq3I5HBmZI%2Bskcq57mVpVxixpgX2Hs7cqVWg3HpuvidtTk9Hgr8yB1Mt3dguIicprORVdp8m5gBQ6aj%2BAE3ILXIKhL2TOzOcg6%2BK1zftsZ0kaGUNH03vdLXOAJpg9eVXf7xDy1GYV27QTMsOe%2BlXEaEeRG%2FeSIlFxWRBsKAZr1%2Fd8cHRENPUMOdZ78zIvZNITtEj2yJAOfUuDFIxBmNVWKf7D1czz8I%2F5opbO5vW9wxqK%2FEuoFpHmtFHNbsLf6RhHo2qnsQuydPcrglILQggnAI7oh6sO2x1KmHW%2Bwi%2BcFXA2vDEzBF4NIwGwxC4sEcvs92cnDrWn2qPbjH%2BxqVjKfzpX5AVegy%2F5haKpfeVW0yIdKQCilGCtgJTarG2iJ2%2FYp1WFGw%2BCwZDGiYLxlpEHxnV4n7%2B7qtpIMl4Sbj2uFU5vE2FvDrN7ySvUpnJUI2tbLJfPgtjheAizB59QKgZbxOKo5YxzLqhrGZa03FftvIgEjT7gyBc76f%2Fn5kQuqcazuLLrCqunJiwmBjhRS9dQukHjzK1D%2BWXUZ%2B5TSoAvFVk84VpoDBtTdqkpJ9jDOPFt2JJyLH9XGduVIlNfVD0SW6Kp35gMTkxbPI7Vpzi4dfTkgzSuwBMKuO77wGOqUBH20NAbmafqxNVFR%2FVh5Nzq1KTXWKKuZhUP432DjX%2BThVYd3POQd0Y3E5sYVFNMthN8ZkdVMRWTDiKz5cfbHdtt%2Be%2FStizRaFmQrgQoZzpBzmpj9ehg54HMzUlqtOtuXhQgEIYG1kE14rr1nQGaFssx42i91JACeWQuiGiNNcvZUwfArX9PJ%2FbKjTWtMt04w%2FoZuFiFb7NARysEkULN3opC%2FvDSiv&X-Amz-Signature=29f80d92d1b7f9e17905dd7eeeae90e9d537a9be2e1d53cc10e3b595fc24526f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVW2QXEH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKdKoQsNK4RM9vtEGNWfLU4ir6tH%2Ba1b12i7x5PgWIAQIgLjW0mhAqTda9G9TKlKOhbFsR9QhiY5WWSvoU%2Bqyfzm8qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDISHyJ1ECWMp%2FbdsCircA3AYEZVqyNq3I5HBmZI%2Bskcq57mVpVxixpgX2Hs7cqVWg3HpuvidtTk9Hgr8yB1Mt3dguIicprORVdp8m5gBQ6aj%2BAE3ILXIKhL2TOzOcg6%2BK1zftsZ0kaGUNH03vdLXOAJpg9eVXf7xDy1GYV27QTMsOe%2BlXEaEeRG%2FeSIlFxWRBsKAZr1%2Fd8cHRENPUMOdZ78zIvZNITtEj2yJAOfUuDFIxBmNVWKf7D1czz8I%2F5opbO5vW9wxqK%2FEuoFpHmtFHNbsLf6RhHo2qnsQuydPcrglILQggnAI7oh6sO2x1KmHW%2Bwi%2BcFXA2vDEzBF4NIwGwxC4sEcvs92cnDrWn2qPbjH%2BxqVjKfzpX5AVegy%2F5haKpfeVW0yIdKQCilGCtgJTarG2iJ2%2FYp1WFGw%2BCwZDGiYLxlpEHxnV4n7%2B7qtpIMl4Sbj2uFU5vE2FvDrN7ySvUpnJUI2tbLJfPgtjheAizB59QKgZbxOKo5YxzLqhrGZa03FftvIgEjT7gyBc76f%2Fn5kQuqcazuLLrCqunJiwmBjhRS9dQukHjzK1D%2BWXUZ%2B5TSoAvFVk84VpoDBtTdqkpJ9jDOPFt2JJyLH9XGduVIlNfVD0SW6Kp35gMTkxbPI7Vpzi4dfTkgzSuwBMKuO77wGOqUBH20NAbmafqxNVFR%2FVh5Nzq1KTXWKKuZhUP432DjX%2BThVYd3POQd0Y3E5sYVFNMthN8ZkdVMRWTDiKz5cfbHdtt%2Be%2FStizRaFmQrgQoZzpBzmpj9ehg54HMzUlqtOtuXhQgEIYG1kE14rr1nQGaFssx42i91JACeWQuiGiNNcvZUwfArX9PJ%2FbKjTWtMt04w%2FoZuFiFb7NARysEkULN3opC%2FvDSiv&X-Amz-Signature=dcb5abb86889990b333080aa6ad27508fdfdb3ec4f0a5164ef04d444f6ec8873&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UJS4N5X%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwVx2Q3Dgk2JavYyey7dlLxps%2Bd4O3WJY2G7PEA4TKqAiBtsuGYLX7ZXAohHWSQIdnihN%2FTJ28yblSpaEbDEmR7yiqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BftqGN64G5DE%2B4LSKtwDB1ArqGft7JJds%2F7tlHW8liyv794bDuF2wOSDM5O4%2BQziKEhbvbYKna373l2L6SGcBewbskSFpzHBAQLTVW%2BlPd8WcXmtQKhJ97QNNY9J5OQ4C%2FArQYmeIjmtR33cEiq5coAnqrN2qexXFEZESF%2BnQObnLm998pTHalAmfVGIvYq%2B5rPjd83skQG9dDKSR7PjqjH26YIXHuyrnetUjw0LCz0hzA2gO0RrI6BW4HgF6NgLBBGbBWKZoXX1MPUnTFtE6RGD7axCuKEOgcPhuPfjOEHzLAAQ5H7%2FC3Nofd7PgeYM%2FvCD%2BGly2LST7t%2BtuM1IVgNWMrRRGmS%2FdQ4gfP5KbAQ2qe1Zh%2BG13slFVSMkN0iIcUptT31%2FRrUJ%2FYBEV%2BwIqakWkUSiC0thZDQV1D7qLB1XtTBDzgb%2FL98onYsrLL5vY87V0wRrvaqcaBMbyKx%2FLXI0U7F%2FJDC2T7XJ2dH%2FvLxUvK8p2keMEziMXMDqDXvr6yKg6kv1KNDRbH631EbvV8MC9X%2BfKuONWxY5IaBPzW%2FeZgOrCx0YjXt7kLxvufVEuTzOOoSfP8HSfDk95NkocpezFh7gJSVGUjmdyrHZ3rfXYS%2FndKbKEHQZB3YGNioSkoc8FQTf9aH2t8AwpY7vvAY6pgFm3rvoWwqysnl4jkZHAKZUbGlAFtd2mYTeyzQh9Hk9Zq%2BJPHJ9akzk3X3memBlnpX66YC1u7wf1fN0rSUV0cMnreTOJ4QViTTPx786WxgptfTzdCdf5Eq%2BXNeGIXx%2BEcVYaOQv8jQRzn7B%2F2AW6SGgyUrCtaIYlWEXQXDc094fVcYxZ2%2FYuQr4DlUb7IhEsagXDJUq2Pb%2FzNfV%2BZBSqQkmQNNuqDHv&X-Amz-Signature=81d8073093bf089d2595819a7f65bc108235d183dce1ddc41a7a7d4832491db5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO4LUEVA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDj%2FPLjZ7a7b3S0BEYSbg1vaUquh9uQfMlB6ZjQF1HOFgIgcixfI%2B2MpY1mE7uDfzUB0cPK9e2NwVIkxD15Un0HGsoqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIQNuNmqEVUCkAnKpSrcA%2F%2FZiNB5tgwGOqkF0a8WsI02fm%2FpcZigxkkq4Zro0uR4ejqrKARFX4rPemGaIJxcI5J7KvwJfkK47h6O2Z8qDnGQBsBmJmFxNKE%2B5KcFrYG%2BqDtFlBUiE890Xi9wfj5GSyaUWHCibVTDS8CwYr7osEdD433QdVW1aHLpRftfDAvZDNrivBD4437bN2bS9dIR23tbycvDlbkoO50jNr0kUKsK0N2WrLBOG9%2FPW1DPlqFNtXpSdabjiq%2BOJrLVu6zV9B5nPDztvkS1sylPsmAiv4Bdma%2Fbrq66NqJ%2B6Cr8iSICYxaS3knPEqXPkHiFx5xcFjY7wbWpCS5J%2BbQz9ZMsU%2B0cLkGzkfNk%2BvGoQnL3AAXyjVxFVOuTmRVuvxd1Yt1yCCcyiDkmEUvRUH42JRQDxWeESyHa2n9hbfLb%2BSrkFzHy5rXuYVKpwsj4yzMlO4%2BAi4MxYbKS0prJVK3YgGzy%2BclWcenD%2BTdDSeTXzKDBy8xDYpn1SEleisEbi3H7avZsTQXNRFo9IKzsoh9DmgSc75FskC81UxOnBVYTyvpqgsT%2F5YQBPoQRfe9qac1dVSK1lgpr1zeg%2BzTyvRjcoB29cEmaGtAEWTIM6fxpDg0jDIS3mKMHxbdfY2UqnY3IMLeO77wGOqUBDi3mUbdPjjtn2ruHbFdaxYhnaR3LJ79dxj5JPuEX4zdoK%2FQNPgFu35uMXFQdrljgVqUIdORiwLPEoOfCPs3S7XKpeTvL%2FWLC6abUrJqK0Ql7gejLzn8OhklqP2OaC1Di3HXZmPPqYjub4%2Bs83cEJnwL7qe13QP0NuLrmeAGpiuXtVE%2FKZQ%2FPoAmisVmKJvrLjVDyQWVH6Bwiql27OhmKU9K07Ng%2B&X-Amz-Signature=ed193f41fbb8877c8ee234b02e103987a06b96f4ad544690361f8c4a1f58b211&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OONRSDQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCo0jzmvfgh55pv5Ch%2BFNvpwd15GOO4QmKswaM5h6SXcQIgKRnbFQXFwwUBDw88xZ0AQ%2BLMafHO53y2oP3hlF8Cp%2FAqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOKXDuT0bVRUSXL2RyrcA5m5r8gc2zLOnHj6Z9jrnK%2B583BI5Z4stKa6oD320Bd3gdhfpUmcMG%2BPUrIJtRI58TsOXY8kswliX%2FW7Ug3C%2FTDG41fNUh4wT9Z0yUx2a7JDmoczxpcahwziDAYXeGvO37eNyX%2FhfxI3bH7xHurl2DZ3KBXiAliS2AH%2FccDtVevryMqMjG7oCNYyThwvasytWRgPdNSUigvqryhgulIK36t1D7Mu1qKW7E8YO3PJhH2tTTnB%2FWqVL5XjjoiBT7CJLQBq4Z7yoHCCIwK9O%2FdKDsL7cS1WPZx0llilcOqEhdIhHMx0x0x3y7znFrmt7JXoI28qOLQVPn3xKUJ404vouGmQyqkc4Eh%2FJWcNX16BAiu9FXnFlBN9NAiRL5Lvd%2Bt2gSTRwCEEWvdCxJjncNHg9fYsCmlgcD3RToTlwlJhlrS5jNr6CBVDhkB61rMk44j9ZPAyMXF4tRPHx7Xlq2FUbV1dodmvjF7Tw0HLVNkUBBDVIujVeQ3k2z%2FG2QSMUhXJKC7REcZpzysyd9Qbyg8ocTuCDN6Ly5MN5UTOoYc4pFrXbGTkjeTkkWcwnW13BfkL%2Fc%2FQn3kTbZLyLyBeaEA9fSRbVvQ%2F%2BgcMmiapFpUUIA17lhJ8WYKKrHLWXoGnMKOO77wGOqUBvQwf8E63Uc8g1DeCZBq3mV32GamuRnH44QWHT4R44zyo4XFX4z8l4GrW3Mw2d6Xk4aHPM4vnjQYCPkeSd5CSlM%2Bg6XjaBSV00rrV1AcgIBC4AM9DwUmHv6h8G%2BpwHcOHGteARxnxpFYlfXZAoHMukUCtJK3uolSnxb9OND1kk3cVd2wnO23tCUynWJwBLYMGLfx%2F%2F6oq4fdjY34aFfmLXNP3zKjm&X-Amz-Signature=1de2f8b149d52b0d9cf5f646cfcaeab0c461ba4f8c5e9395c05f271142b5274c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OONRSDQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCo0jzmvfgh55pv5Ch%2BFNvpwd15GOO4QmKswaM5h6SXcQIgKRnbFQXFwwUBDw88xZ0AQ%2BLMafHO53y2oP3hlF8Cp%2FAqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOKXDuT0bVRUSXL2RyrcA5m5r8gc2zLOnHj6Z9jrnK%2B583BI5Z4stKa6oD320Bd3gdhfpUmcMG%2BPUrIJtRI58TsOXY8kswliX%2FW7Ug3C%2FTDG41fNUh4wT9Z0yUx2a7JDmoczxpcahwziDAYXeGvO37eNyX%2FhfxI3bH7xHurl2DZ3KBXiAliS2AH%2FccDtVevryMqMjG7oCNYyThwvasytWRgPdNSUigvqryhgulIK36t1D7Mu1qKW7E8YO3PJhH2tTTnB%2FWqVL5XjjoiBT7CJLQBq4Z7yoHCCIwK9O%2FdKDsL7cS1WPZx0llilcOqEhdIhHMx0x0x3y7znFrmt7JXoI28qOLQVPn3xKUJ404vouGmQyqkc4Eh%2FJWcNX16BAiu9FXnFlBN9NAiRL5Lvd%2Bt2gSTRwCEEWvdCxJjncNHg9fYsCmlgcD3RToTlwlJhlrS5jNr6CBVDhkB61rMk44j9ZPAyMXF4tRPHx7Xlq2FUbV1dodmvjF7Tw0HLVNkUBBDVIujVeQ3k2z%2FG2QSMUhXJKC7REcZpzysyd9Qbyg8ocTuCDN6Ly5MN5UTOoYc4pFrXbGTkjeTkkWcwnW13BfkL%2Fc%2FQn3kTbZLyLyBeaEA9fSRbVvQ%2F%2BgcMmiapFpUUIA17lhJ8WYKKrHLWXoGnMKOO77wGOqUBvQwf8E63Uc8g1DeCZBq3mV32GamuRnH44QWHT4R44zyo4XFX4z8l4GrW3Mw2d6Xk4aHPM4vnjQYCPkeSd5CSlM%2Bg6XjaBSV00rrV1AcgIBC4AM9DwUmHv6h8G%2BpwHcOHGteARxnxpFYlfXZAoHMukUCtJK3uolSnxb9OND1kk3cVd2wnO23tCUynWJwBLYMGLfx%2F%2F6oq4fdjY34aFfmLXNP3zKjm&X-Amz-Signature=5860d00255cc2f67e0943ffab0a4e4b1c4de703a8e3401a9c605c3b7e9af21cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
