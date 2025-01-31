

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QLYLQLE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZbj8eK4XnCbGlsURM5zpDKmBSIgujuzukbWzV7IWH%2BwIgNfTTCn7KYNVy0fHVEogwiKwc6w1OO2igxxxbVHH8gUEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAw%2BcxnNkWZa0yTcaCrcA5Z1L615RCVTp5NGmmFUEoGNchLjGyBPgRrh%2Fj16uyfLNDFOx8R1ouYdZMWuWqvbJyux7dvzSWOMMmn%2F5ltmr9Ko%2Bq7yJne8Jp4WLVTfIxj2wE7D%2FwzsZHzvpBe9rHEfjE7ZU%2FVf246u3WiiISVhXJ85mmTvC1uIDAo2RW%2F1Tv0qkM3qu%2BS%2BFhXRbUMKTZZtQceb6xMZAL%2BaWKGNqwwNhucMHMCcBoBLU754h5SURPt9zuvIU2aj7jMeprW50OYthkc7b9Y4SAZ%2Bde3ZEuofjuJpZ2NXctCByFrTpGOEdwDOR7UydUz%2FM2DHwKBWVpSp6oAXn0Al%2Bki4f3aCgHc96d82IOcAjlaZeszau8rtBj%2F6G33FE6ZiLEWv0iiJazwRSS%2FgPrFiclhrGSHFnCnPQ13bmlFJYceh3dy7WAsTc8xT3Jg%2F4CbqAGNNtp88jXbnoPjKuimphdA24uBdofdfZfQXSOz33uG%2BU7JC4HYzIdfiF01KcHdpqeE5aEcFbHjnL0ueEFqrntvJ1jG6qZF3G2upOitI2VmDgRoIZEis83MXBMM0%2FZYgHKOfiI98UVOH8t9OuaDFn2ECn735HV5tqOR%2FeVA%2BdBZZ812%2BhX86rgpRS5a2UyuR6M8SnsYIMI%2Fr87wGOqUBxnkiB4f2S0tMWgVnA7A1rpg8FaJJiGWBXeNZwE5lxkYeQheVTU83D0BfUWc9is8PJOv%2Ftfg5kgjms%2FWL3GFFop8iyvsKyyxYa669utjNQdkxaiNqKn7Gt%2BPOr6F%2Bjf3QVU93VOXxCImbjJEGBaOCRVDK9nNylSTnfP6PmZOrs4dsJptTtVRlFjM%2F8OhsNcfEkROv2HpQIi4ySBgj%2FpgNfWDCv5az&X-Amz-Signature=95f1b7eaeb9bb8462ceacd3dbfeb047c6396d7b2d7f7f42cc58dae1457a7edfb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QLYLQLE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZbj8eK4XnCbGlsURM5zpDKmBSIgujuzukbWzV7IWH%2BwIgNfTTCn7KYNVy0fHVEogwiKwc6w1OO2igxxxbVHH8gUEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAw%2BcxnNkWZa0yTcaCrcA5Z1L615RCVTp5NGmmFUEoGNchLjGyBPgRrh%2Fj16uyfLNDFOx8R1ouYdZMWuWqvbJyux7dvzSWOMMmn%2F5ltmr9Ko%2Bq7yJne8Jp4WLVTfIxj2wE7D%2FwzsZHzvpBe9rHEfjE7ZU%2FVf246u3WiiISVhXJ85mmTvC1uIDAo2RW%2F1Tv0qkM3qu%2BS%2BFhXRbUMKTZZtQceb6xMZAL%2BaWKGNqwwNhucMHMCcBoBLU754h5SURPt9zuvIU2aj7jMeprW50OYthkc7b9Y4SAZ%2Bde3ZEuofjuJpZ2NXctCByFrTpGOEdwDOR7UydUz%2FM2DHwKBWVpSp6oAXn0Al%2Bki4f3aCgHc96d82IOcAjlaZeszau8rtBj%2F6G33FE6ZiLEWv0iiJazwRSS%2FgPrFiclhrGSHFnCnPQ13bmlFJYceh3dy7WAsTc8xT3Jg%2F4CbqAGNNtp88jXbnoPjKuimphdA24uBdofdfZfQXSOz33uG%2BU7JC4HYzIdfiF01KcHdpqeE5aEcFbHjnL0ueEFqrntvJ1jG6qZF3G2upOitI2VmDgRoIZEis83MXBMM0%2FZYgHKOfiI98UVOH8t9OuaDFn2ECn735HV5tqOR%2FeVA%2BdBZZ812%2BhX86rgpRS5a2UyuR6M8SnsYIMI%2Fr87wGOqUBxnkiB4f2S0tMWgVnA7A1rpg8FaJJiGWBXeNZwE5lxkYeQheVTU83D0BfUWc9is8PJOv%2Ftfg5kgjms%2FWL3GFFop8iyvsKyyxYa669utjNQdkxaiNqKn7Gt%2BPOr6F%2Bjf3QVU93VOXxCImbjJEGBaOCRVDK9nNylSTnfP6PmZOrs4dsJptTtVRlFjM%2F8OhsNcfEkROv2HpQIi4ySBgj%2FpgNfWDCv5az&X-Amz-Signature=2b61a6065a7a8e11bb6fcaf79d744fb13aa114085706b09568fb6913a0034906&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QLYLQLE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZbj8eK4XnCbGlsURM5zpDKmBSIgujuzukbWzV7IWH%2BwIgNfTTCn7KYNVy0fHVEogwiKwc6w1OO2igxxxbVHH8gUEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAw%2BcxnNkWZa0yTcaCrcA5Z1L615RCVTp5NGmmFUEoGNchLjGyBPgRrh%2Fj16uyfLNDFOx8R1ouYdZMWuWqvbJyux7dvzSWOMMmn%2F5ltmr9Ko%2Bq7yJne8Jp4WLVTfIxj2wE7D%2FwzsZHzvpBe9rHEfjE7ZU%2FVf246u3WiiISVhXJ85mmTvC1uIDAo2RW%2F1Tv0qkM3qu%2BS%2BFhXRbUMKTZZtQceb6xMZAL%2BaWKGNqwwNhucMHMCcBoBLU754h5SURPt9zuvIU2aj7jMeprW50OYthkc7b9Y4SAZ%2Bde3ZEuofjuJpZ2NXctCByFrTpGOEdwDOR7UydUz%2FM2DHwKBWVpSp6oAXn0Al%2Bki4f3aCgHc96d82IOcAjlaZeszau8rtBj%2F6G33FE6ZiLEWv0iiJazwRSS%2FgPrFiclhrGSHFnCnPQ13bmlFJYceh3dy7WAsTc8xT3Jg%2F4CbqAGNNtp88jXbnoPjKuimphdA24uBdofdfZfQXSOz33uG%2BU7JC4HYzIdfiF01KcHdpqeE5aEcFbHjnL0ueEFqrntvJ1jG6qZF3G2upOitI2VmDgRoIZEis83MXBMM0%2FZYgHKOfiI98UVOH8t9OuaDFn2ECn735HV5tqOR%2FeVA%2BdBZZ812%2BhX86rgpRS5a2UyuR6M8SnsYIMI%2Fr87wGOqUBxnkiB4f2S0tMWgVnA7A1rpg8FaJJiGWBXeNZwE5lxkYeQheVTU83D0BfUWc9is8PJOv%2Ftfg5kgjms%2FWL3GFFop8iyvsKyyxYa669utjNQdkxaiNqKn7Gt%2BPOr6F%2Bjf3QVU93VOXxCImbjJEGBaOCRVDK9nNylSTnfP6PmZOrs4dsJptTtVRlFjM%2F8OhsNcfEkROv2HpQIi4ySBgj%2FpgNfWDCv5az&X-Amz-Signature=ac85d3055f86ff5f21782812aca3a4a3bf5df92610dbd2fca4125ce479aa7bdc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QLYLQLE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZbj8eK4XnCbGlsURM5zpDKmBSIgujuzukbWzV7IWH%2BwIgNfTTCn7KYNVy0fHVEogwiKwc6w1OO2igxxxbVHH8gUEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAw%2BcxnNkWZa0yTcaCrcA5Z1L615RCVTp5NGmmFUEoGNchLjGyBPgRrh%2Fj16uyfLNDFOx8R1ouYdZMWuWqvbJyux7dvzSWOMMmn%2F5ltmr9Ko%2Bq7yJne8Jp4WLVTfIxj2wE7D%2FwzsZHzvpBe9rHEfjE7ZU%2FVf246u3WiiISVhXJ85mmTvC1uIDAo2RW%2F1Tv0qkM3qu%2BS%2BFhXRbUMKTZZtQceb6xMZAL%2BaWKGNqwwNhucMHMCcBoBLU754h5SURPt9zuvIU2aj7jMeprW50OYthkc7b9Y4SAZ%2Bde3ZEuofjuJpZ2NXctCByFrTpGOEdwDOR7UydUz%2FM2DHwKBWVpSp6oAXn0Al%2Bki4f3aCgHc96d82IOcAjlaZeszau8rtBj%2F6G33FE6ZiLEWv0iiJazwRSS%2FgPrFiclhrGSHFnCnPQ13bmlFJYceh3dy7WAsTc8xT3Jg%2F4CbqAGNNtp88jXbnoPjKuimphdA24uBdofdfZfQXSOz33uG%2BU7JC4HYzIdfiF01KcHdpqeE5aEcFbHjnL0ueEFqrntvJ1jG6qZF3G2upOitI2VmDgRoIZEis83MXBMM0%2FZYgHKOfiI98UVOH8t9OuaDFn2ECn735HV5tqOR%2FeVA%2BdBZZ812%2BhX86rgpRS5a2UyuR6M8SnsYIMI%2Fr87wGOqUBxnkiB4f2S0tMWgVnA7A1rpg8FaJJiGWBXeNZwE5lxkYeQheVTU83D0BfUWc9is8PJOv%2Ftfg5kgjms%2FWL3GFFop8iyvsKyyxYa669utjNQdkxaiNqKn7Gt%2BPOr6F%2Bjf3QVU93VOXxCImbjJEGBaOCRVDK9nNylSTnfP6PmZOrs4dsJptTtVRlFjM%2F8OhsNcfEkROv2HpQIi4ySBgj%2FpgNfWDCv5az&X-Amz-Signature=1c9e1eba30928565881e7324b7025f745738fd204dce94efd00d7cad3dbf0340&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QLYLQLE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZbj8eK4XnCbGlsURM5zpDKmBSIgujuzukbWzV7IWH%2BwIgNfTTCn7KYNVy0fHVEogwiKwc6w1OO2igxxxbVHH8gUEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAw%2BcxnNkWZa0yTcaCrcA5Z1L615RCVTp5NGmmFUEoGNchLjGyBPgRrh%2Fj16uyfLNDFOx8R1ouYdZMWuWqvbJyux7dvzSWOMMmn%2F5ltmr9Ko%2Bq7yJne8Jp4WLVTfIxj2wE7D%2FwzsZHzvpBe9rHEfjE7ZU%2FVf246u3WiiISVhXJ85mmTvC1uIDAo2RW%2F1Tv0qkM3qu%2BS%2BFhXRbUMKTZZtQceb6xMZAL%2BaWKGNqwwNhucMHMCcBoBLU754h5SURPt9zuvIU2aj7jMeprW50OYthkc7b9Y4SAZ%2Bde3ZEuofjuJpZ2NXctCByFrTpGOEdwDOR7UydUz%2FM2DHwKBWVpSp6oAXn0Al%2Bki4f3aCgHc96d82IOcAjlaZeszau8rtBj%2F6G33FE6ZiLEWv0iiJazwRSS%2FgPrFiclhrGSHFnCnPQ13bmlFJYceh3dy7WAsTc8xT3Jg%2F4CbqAGNNtp88jXbnoPjKuimphdA24uBdofdfZfQXSOz33uG%2BU7JC4HYzIdfiF01KcHdpqeE5aEcFbHjnL0ueEFqrntvJ1jG6qZF3G2upOitI2VmDgRoIZEis83MXBMM0%2FZYgHKOfiI98UVOH8t9OuaDFn2ECn735HV5tqOR%2FeVA%2BdBZZ812%2BhX86rgpRS5a2UyuR6M8SnsYIMI%2Fr87wGOqUBxnkiB4f2S0tMWgVnA7A1rpg8FaJJiGWBXeNZwE5lxkYeQheVTU83D0BfUWc9is8PJOv%2Ftfg5kgjms%2FWL3GFFop8iyvsKyyxYa669utjNQdkxaiNqKn7Gt%2BPOr6F%2Bjf3QVU93VOXxCImbjJEGBaOCRVDK9nNylSTnfP6PmZOrs4dsJptTtVRlFjM%2F8OhsNcfEkROv2HpQIi4ySBgj%2FpgNfWDCv5az&X-Amz-Signature=1ea03280faaa1c4e7fbae642c1cbf84261573d6055dd6319857720caaf0f1444&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QLYLQLE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZbj8eK4XnCbGlsURM5zpDKmBSIgujuzukbWzV7IWH%2BwIgNfTTCn7KYNVy0fHVEogwiKwc6w1OO2igxxxbVHH8gUEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAw%2BcxnNkWZa0yTcaCrcA5Z1L615RCVTp5NGmmFUEoGNchLjGyBPgRrh%2Fj16uyfLNDFOx8R1ouYdZMWuWqvbJyux7dvzSWOMMmn%2F5ltmr9Ko%2Bq7yJne8Jp4WLVTfIxj2wE7D%2FwzsZHzvpBe9rHEfjE7ZU%2FVf246u3WiiISVhXJ85mmTvC1uIDAo2RW%2F1Tv0qkM3qu%2BS%2BFhXRbUMKTZZtQceb6xMZAL%2BaWKGNqwwNhucMHMCcBoBLU754h5SURPt9zuvIU2aj7jMeprW50OYthkc7b9Y4SAZ%2Bde3ZEuofjuJpZ2NXctCByFrTpGOEdwDOR7UydUz%2FM2DHwKBWVpSp6oAXn0Al%2Bki4f3aCgHc96d82IOcAjlaZeszau8rtBj%2F6G33FE6ZiLEWv0iiJazwRSS%2FgPrFiclhrGSHFnCnPQ13bmlFJYceh3dy7WAsTc8xT3Jg%2F4CbqAGNNtp88jXbnoPjKuimphdA24uBdofdfZfQXSOz33uG%2BU7JC4HYzIdfiF01KcHdpqeE5aEcFbHjnL0ueEFqrntvJ1jG6qZF3G2upOitI2VmDgRoIZEis83MXBMM0%2FZYgHKOfiI98UVOH8t9OuaDFn2ECn735HV5tqOR%2FeVA%2BdBZZ812%2BhX86rgpRS5a2UyuR6M8SnsYIMI%2Fr87wGOqUBxnkiB4f2S0tMWgVnA7A1rpg8FaJJiGWBXeNZwE5lxkYeQheVTU83D0BfUWc9is8PJOv%2Ftfg5kgjms%2FWL3GFFop8iyvsKyyxYa669utjNQdkxaiNqKn7Gt%2BPOr6F%2Bjf3QVU93VOXxCImbjJEGBaOCRVDK9nNylSTnfP6PmZOrs4dsJptTtVRlFjM%2F8OhsNcfEkROv2HpQIi4ySBgj%2FpgNfWDCv5az&X-Amz-Signature=2c557e4ef21beb7ea32d2ee632503704d205b5921d30095a12914466eed4c966&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QLYLQLE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZbj8eK4XnCbGlsURM5zpDKmBSIgujuzukbWzV7IWH%2BwIgNfTTCn7KYNVy0fHVEogwiKwc6w1OO2igxxxbVHH8gUEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAw%2BcxnNkWZa0yTcaCrcA5Z1L615RCVTp5NGmmFUEoGNchLjGyBPgRrh%2Fj16uyfLNDFOx8R1ouYdZMWuWqvbJyux7dvzSWOMMmn%2F5ltmr9Ko%2Bq7yJne8Jp4WLVTfIxj2wE7D%2FwzsZHzvpBe9rHEfjE7ZU%2FVf246u3WiiISVhXJ85mmTvC1uIDAo2RW%2F1Tv0qkM3qu%2BS%2BFhXRbUMKTZZtQceb6xMZAL%2BaWKGNqwwNhucMHMCcBoBLU754h5SURPt9zuvIU2aj7jMeprW50OYthkc7b9Y4SAZ%2Bde3ZEuofjuJpZ2NXctCByFrTpGOEdwDOR7UydUz%2FM2DHwKBWVpSp6oAXn0Al%2Bki4f3aCgHc96d82IOcAjlaZeszau8rtBj%2F6G33FE6ZiLEWv0iiJazwRSS%2FgPrFiclhrGSHFnCnPQ13bmlFJYceh3dy7WAsTc8xT3Jg%2F4CbqAGNNtp88jXbnoPjKuimphdA24uBdofdfZfQXSOz33uG%2BU7JC4HYzIdfiF01KcHdpqeE5aEcFbHjnL0ueEFqrntvJ1jG6qZF3G2upOitI2VmDgRoIZEis83MXBMM0%2FZYgHKOfiI98UVOH8t9OuaDFn2ECn735HV5tqOR%2FeVA%2BdBZZ812%2BhX86rgpRS5a2UyuR6M8SnsYIMI%2Fr87wGOqUBxnkiB4f2S0tMWgVnA7A1rpg8FaJJiGWBXeNZwE5lxkYeQheVTU83D0BfUWc9is8PJOv%2Ftfg5kgjms%2FWL3GFFop8iyvsKyyxYa669utjNQdkxaiNqKn7Gt%2BPOr6F%2Bjf3QVU93VOXxCImbjJEGBaOCRVDK9nNylSTnfP6PmZOrs4dsJptTtVRlFjM%2F8OhsNcfEkROv2HpQIi4ySBgj%2FpgNfWDCv5az&X-Amz-Signature=8aa506f57b1a6ecfd70203cf7d7e7f9368306e5f85a52b4c8927f0ced6e060a9&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QLYLQLE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZbj8eK4XnCbGlsURM5zpDKmBSIgujuzukbWzV7IWH%2BwIgNfTTCn7KYNVy0fHVEogwiKwc6w1OO2igxxxbVHH8gUEqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAw%2BcxnNkWZa0yTcaCrcA5Z1L615RCVTp5NGmmFUEoGNchLjGyBPgRrh%2Fj16uyfLNDFOx8R1ouYdZMWuWqvbJyux7dvzSWOMMmn%2F5ltmr9Ko%2Bq7yJne8Jp4WLVTfIxj2wE7D%2FwzsZHzvpBe9rHEfjE7ZU%2FVf246u3WiiISVhXJ85mmTvC1uIDAo2RW%2F1Tv0qkM3qu%2BS%2BFhXRbUMKTZZtQceb6xMZAL%2BaWKGNqwwNhucMHMCcBoBLU754h5SURPt9zuvIU2aj7jMeprW50OYthkc7b9Y4SAZ%2Bde3ZEuofjuJpZ2NXctCByFrTpGOEdwDOR7UydUz%2FM2DHwKBWVpSp6oAXn0Al%2Bki4f3aCgHc96d82IOcAjlaZeszau8rtBj%2F6G33FE6ZiLEWv0iiJazwRSS%2FgPrFiclhrGSHFnCnPQ13bmlFJYceh3dy7WAsTc8xT3Jg%2F4CbqAGNNtp88jXbnoPjKuimphdA24uBdofdfZfQXSOz33uG%2BU7JC4HYzIdfiF01KcHdpqeE5aEcFbHjnL0ueEFqrntvJ1jG6qZF3G2upOitI2VmDgRoIZEis83MXBMM0%2FZYgHKOfiI98UVOH8t9OuaDFn2ECn735HV5tqOR%2FeVA%2BdBZZ812%2BhX86rgpRS5a2UyuR6M8SnsYIMI%2Fr87wGOqUBxnkiB4f2S0tMWgVnA7A1rpg8FaJJiGWBXeNZwE5lxkYeQheVTU83D0BfUWc9is8PJOv%2Ftfg5kgjms%2FWL3GFFop8iyvsKyyxYa669utjNQdkxaiNqKn7Gt%2BPOr6F%2Bjf3QVU93VOXxCImbjJEGBaOCRVDK9nNylSTnfP6PmZOrs4dsJptTtVRlFjM%2F8OhsNcfEkROv2HpQIi4ySBgj%2FpgNfWDCv5az&X-Amz-Signature=622db023db8c93c10e87112f2c511f1be8de1bba2d8a3773407e620d67202589&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFDU5C4X%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICWXYCCj1kBhwXuH7CXuVEKddmTXFdfzzp2P8P6HS174AiEAmV3oHOuvCR8l7%2ByDcnSQFFXHnOn9sBGsPR5cRwru0YgqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEpSp5rBP7RDrQVB8SrcA%2FB%2BWaB8vEovf56zV5%2F%2BEeZ6kMgfh9bNDOSQhgjG3647pJTue7kRRDm%2BvKd7h6T%2FVTyK27IjQEXDAFmz8IsX11e%2FGIeqrW2A%2BBDolh7rehWSUSAHsBNBdZ%2Fs2WJgd7s4C0dtjbA6uI%2ByjNaKNdS2PvIXPVWHw4DUFxP8sGx4IdLd3dsCs7SQvadjHapPg5Xt8DMjw5WjeETuZxiSzQXGi2e6Dm4v2%2F1md%2BrnRNC0pNIPkJEBIyWCpOZM%2FTnEQjNcIwNwKjmKR4Y8jhN%2FRBndZN0mkQxswxZJPmo22lCdh4UFwK2KX9lbHZuCdP2l6Jde5O1BvECzOTRzzzmRviBtKqwz8FNb%2BDT1IOfutA7pTKdqpecicq3Uy198WIqn%2Bh7QdFqlod0TwIXZMRFnBebX5SpuFnCN%2FsiyKCu4BDMxC4c6r2uXoqCcJIfp2PusPjtUWIcvy0%2BBbjPXQmof71e7GNk%2Fy6clz4hsvf4R8dsZDP11XMxU%2FqG3dhQfWZ9tnrC7tkin3M8JSItpVHA49N3CJxdnHxGjm6N3v4Ck76n1XfyXO0lJEHrKPuo%2FZYyB6QB2krbJ91MXCqaPGq2HezyBXXQ3SP%2FEe287wk3nha75M6kxdCn%2BnExqF50oUOj6MKjr87wGOqUBc77jtLWnW%2FJ8rDXBwmo8gcd%2BgqSybAay7Tw7oMchPJSybxuWG4TV0kzgQ%2FmPVRYCHzl7xExnusvHgwqc1Gjuy%2FZrIB5jBZJUP8WIZGA%2FU8yVLjonVvlSQTFYFovz0m17A7ATn5p6z2W6b9StVM6eIrOEb1sipqmA89I4qBoJtFDvFDNHftHRjAZDCvUj1KdAkCjjcZk24ZV5DSiOrWrKYcdBzwkU&X-Amz-Signature=e296e44d51ccbe2990075993c093b3cc42fa9ce13f45a53b2dca676c319a5749&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYWACPTI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDcN3BGB%2FXZi6i7cjt9xGmJICcdA%2BqU9d9i0YqwLv51zAIhALssYf8gUe1Wbw6HSt9iuV9ZIMSI4b7t%2BY5ysyUK1WokKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwt%2BS%2FvVsVmNN49F9cq3APdv661LHzo8dSrR2albm41Yzu3wfYWUElC2kLOVtifp%2B2XN2CDYmIsr3MGsNsFAeyG5YurVKNoDqdys1g1tfs0IJXWd4iHNNQn2YcaKhTMfkMPN1oWksg7UXVDWf2hbXyIv3u2wwyfwaCv1VihEGUm9iD39u7voUOKZ1W3UKS5jmGVh%2FRUAYZqO%2F4gZ05%2BjRyYRRUxi6cSiGAe1TsCzdgQPrjwrHPcKQv1bAmXQv%2FiNnieJWAUewfaAtewhsA3LZijbl%2FbcqUfP6ZQ3tF%2Faw%2FrmzNw8rHrVd3iR9J%2F9%2Br4fBAlh7cvav8rtcu0ApeNp0rtN1W0NzZ39LBeKuMv7B31saXgn8EGXvyEsOt3EFEIL%2FaCT0NZj%2FOPM8G5q0zQKd7FaIPq6KMGWGSQB3bLemtMSvw2aqyfxg9xDLnsIgLpm3jr4hML%2B8%2BhnayMcrYK5RTM5DOigzZwgmqGro2zQxmg%2FdWfPGX8qT9clcRjt%2FsiYfUPZ0g%2BSvT8Ftje4A2BsnBpsMsj0RhU%2FyXT13cwmC7UVRDhpTT9HZOQ5%2B9LwJa%2F9Fz6yXKWx50lk7UwERe3OfCYJonu%2B1tNSeDwd3YBSxFpr5ATwkH8zqf4gm9ksPMFYBwvCiIuAe4qDWsyejDc6vO8BjqkAQrJPgO0D5WykuHi%2BjC6EHBxTjdAcAksmEyccNoo4AnCIbaCcU3GRSBe%2FY3vHR4hjKBd%2BKNO8ZMG7uAFCxdO9TH7PycdpAA%2F3mwmugT%2BTv4mpqVY0fy9SR5TxJ%2BJhKigpRq7S0rlFCVGyPcc%2FSI5%2F223m98TB3I0kH2QA%2Fo%2FEcZfnj2Nm6HyhGqz%2FTbC4ofvekaQGD3IDMKr4GnxLrL4fBu%2BKw4k&X-Amz-Signature=cbbde551e4a801e1d090b0c9ad382fa519e7799b1308defbb3ccffe68084dcf2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJF2H33P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGFm3jHK1AyrUkVHEBd5WzhfFEaD7%2Bx6e2X80%2FcRljxQAiBT2H2YSDb3mDZGq2cxfkbRAccqGbRfM%2FOYToy7Gxh6RCqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoWvN7WXkMxUDPzRyKtwD2kgHIX2HXPiqjmM7YxJqbNuzFJsFMVby68Knf7pRrwx78Xr5GFBfc5a6bSiL710O2tBGT3feE%2BQWlIyuDJXRoQw42ZBR1bCynejGhNNsf0bvpLLlMdAy2UNUPYWkQfXFt8QaiY4gYpzD4ZZOinWFCj1%2Fq%2BdNQYg2xA%2BhwuaApC5AvUK4kZT8RiNCMmI0Vqxq8Y12V9d0SaYMdG0Spz928oQC0n2ioDKIIatBtc6%2Fw0doiQWOma3eN7ys7iqAEy2EtEMs9BWbvt4JdnbAit1RrA4bqCYDi3qBmrKI3UheHMVCxJSjYbi7F6rGeHqBq%2F6LLiCO%2Bp6N%2FIWy991MfYea6PUt8UgYYaSRfwG3Yh7Px8Q86SD8g9D4U0KauH8vFQBm6AObt%2BlmigsYphP6DWu5cclFBALnqL%2FYzblirP06pztMN2UJPcCgMvwK6U4wRZ52XHes%2B9VQD%2FQBXtMcupUm7Xaz62WhHkobb6nJuQ6wdGAlpQVagDDfBlvDxMPqTnP1pRZap%2FuoRItaK%2B%2BQ3XCk3Gi4LECtRaO9Y1mwKY5KpqScow%2FkR2d3S8VmlOrLeeL%2FixOOPUIkfwTslP%2FGFBVxbcDtx6J5lUNptTcL8bO0d1paYQnQLHZ15yM3TVowp%2BvzvAY6pgFxSiRZzYOtRllhcokJiwOZIHrKJXdgJ0FuSNWj083pwNIlRfUkw%2BknPXddbqzdc1m8a%2FTAWcjFTqcI8rUuEVTA0U0%2Bd%2B6SqZlTCgLFHLB%2Bc3oXehmKJRWqLqLkPYQxY2hHmxsMmD0NDMH7qZeRjLRR1Bi0elSGAmwnMbVWHJggYsRqAyMpdlXQzJUPHXcjaTkCqdhq%2BBqy3v%2FIq8ioOZ%2BYJutfuVVm&X-Amz-Signature=b937a26a033a2c17b483e4e82de7f04406101fb3c6038e209fabec2ffd03a525&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJF2H33P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGFm3jHK1AyrUkVHEBd5WzhfFEaD7%2Bx6e2X80%2FcRljxQAiBT2H2YSDb3mDZGq2cxfkbRAccqGbRfM%2FOYToy7Gxh6RCqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoWvN7WXkMxUDPzRyKtwD2kgHIX2HXPiqjmM7YxJqbNuzFJsFMVby68Knf7pRrwx78Xr5GFBfc5a6bSiL710O2tBGT3feE%2BQWlIyuDJXRoQw42ZBR1bCynejGhNNsf0bvpLLlMdAy2UNUPYWkQfXFt8QaiY4gYpzD4ZZOinWFCj1%2Fq%2BdNQYg2xA%2BhwuaApC5AvUK4kZT8RiNCMmI0Vqxq8Y12V9d0SaYMdG0Spz928oQC0n2ioDKIIatBtc6%2Fw0doiQWOma3eN7ys7iqAEy2EtEMs9BWbvt4JdnbAit1RrA4bqCYDi3qBmrKI3UheHMVCxJSjYbi7F6rGeHqBq%2F6LLiCO%2Bp6N%2FIWy991MfYea6PUt8UgYYaSRfwG3Yh7Px8Q86SD8g9D4U0KauH8vFQBm6AObt%2BlmigsYphP6DWu5cclFBALnqL%2FYzblirP06pztMN2UJPcCgMvwK6U4wRZ52XHes%2B9VQD%2FQBXtMcupUm7Xaz62WhHkobb6nJuQ6wdGAlpQVagDDfBlvDxMPqTnP1pRZap%2FuoRItaK%2B%2BQ3XCk3Gi4LECtRaO9Y1mwKY5KpqScow%2FkR2d3S8VmlOrLeeL%2FixOOPUIkfwTslP%2FGFBVxbcDtx6J5lUNptTcL8bO0d1paYQnQLHZ15yM3TVowp%2BvzvAY6pgFxSiRZzYOtRllhcokJiwOZIHrKJXdgJ0FuSNWj083pwNIlRfUkw%2BknPXddbqzdc1m8a%2FTAWcjFTqcI8rUuEVTA0U0%2Bd%2B6SqZlTCgLFHLB%2Bc3oXehmKJRWqLqLkPYQxY2hHmxsMmD0NDMH7qZeRjLRR1Bi0elSGAmwnMbVWHJggYsRqAyMpdlXQzJUPHXcjaTkCqdhq%2BBqy3v%2FIq8ioOZ%2BYJutfuVVm&X-Amz-Signature=41e1a332579fde172a0529daaef60a826829e3813321f2125b9ca49cacc303dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
