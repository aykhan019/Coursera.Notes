

# Module 2: Regression
## Introduction to Regression
### Overview
Regression is the process of predicting a continuous value using other variables. It involves two types of variables: dependent (target) and independent (explanatory) variables. The dependent variable is the value being predicted, while the independent variables are the factors used to make the prediction. In regression, the dependent variable should be continuous, whereas the independent variables can be either categorical or continuous.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/048d582c-bb2d-4876-8db6-48170b4c3cd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC3HNRNU%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIGuoMpeJEUbQPyuOauVQbHubirD8zzt%2BCrQ9xcDkWvhrAiAa9Dn5uZCL1vOkTpmft5PvBImYoGA1KzKjbChrOA7WACqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3CpLR9Lk3MkeuwE0KtwDDjTx9XxG%2FX6Om21hurg4NHERKWjFf60%2Fm1vUUELPNh5QA5N%2FwAnI21mUn0Rlu%2BUBsolvQTr2WaQyKLJykBHIbeaZhBs8kXFMNU%2FI6gd5Lb%2BGCm1OImKWF%2Fsf81ZfjKVJCzEDf7jJtg884ltwGU0s%2BgVwhArWktlHig5rXC2m96toyHZhv6BMJZodQS6cz0xiLIbcQXBTaTbapfefrMXwY5mHzc7Fds9P1Jbw5c7z1Z9%2FyWhj%2Bm1xrsXq65G9r4XmxAicXOnJzmE%2BcB%2BPWs366qMjudBIfrs%2ByN%2BImTb7RjxwqfXTDpTGH4OcByNOOyriPMcZaxB04dFTnvJLFElrVER%2BnU9xxpktQK5lYulSzEplenlPvOp5yF32FIian%2FHWMLQGjTr7WwEibL99M2PShQmD5aaPmhd3PPQexds4k%2B1T5OrOXwFe%2F9Nus0CvSxNRtiB2EUvtf7kK4Kkujvl6EVvyx45JlnZFDGwxrmI%2FdU1RGPcUFjxgr7H5gf95tOXlCUC7WyIH27L6KTuzmLBf4VCKatdpC2IqaIpgec3%2BiMtek17qrxiwcm%2FTczghJR7wnIb23YIiuy8GjnF9tK8kCj2ktFuRJZOLstV08TvBq5p8I%2FdVKXZRtaS%2FgI4ws%2FyhvwY6pgH2592Lw0WJsOV%2FUeQYEy%2FAHpixb79QzD4wG7n2f7Ehkz5303maD0Iucce8%2FaP1O9P8he0nGJ4WjG1xcYyL6BBXFJGK6NKkx38bqt4pdhO9W0ine0U3rb6qmhXWpvCUP3A4ff5Tu0ZU5KGTFiGEJyIYGxiVDuSrcJDdR5teavzYuGUltk76KZNW63SobUlHN7Ez6yTcktzw4ov7TUe7kvDggUsvfxZS&X-Amz-Signature=1cc8fcf56d0b4515dcc1cf65927976bf2ae2db32ffba34e92e4eb9ff89ea3dce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/bf5ae032-3b83-43fa-bf50-0b398a6a3696/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC3HNRNU%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIGuoMpeJEUbQPyuOauVQbHubirD8zzt%2BCrQ9xcDkWvhrAiAa9Dn5uZCL1vOkTpmft5PvBImYoGA1KzKjbChrOA7WACqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3CpLR9Lk3MkeuwE0KtwDDjTx9XxG%2FX6Om21hurg4NHERKWjFf60%2Fm1vUUELPNh5QA5N%2FwAnI21mUn0Rlu%2BUBsolvQTr2WaQyKLJykBHIbeaZhBs8kXFMNU%2FI6gd5Lb%2BGCm1OImKWF%2Fsf81ZfjKVJCzEDf7jJtg884ltwGU0s%2BgVwhArWktlHig5rXC2m96toyHZhv6BMJZodQS6cz0xiLIbcQXBTaTbapfefrMXwY5mHzc7Fds9P1Jbw5c7z1Z9%2FyWhj%2Bm1xrsXq65G9r4XmxAicXOnJzmE%2BcB%2BPWs366qMjudBIfrs%2ByN%2BImTb7RjxwqfXTDpTGH4OcByNOOyriPMcZaxB04dFTnvJLFElrVER%2BnU9xxpktQK5lYulSzEplenlPvOp5yF32FIian%2FHWMLQGjTr7WwEibL99M2PShQmD5aaPmhd3PPQexds4k%2B1T5OrOXwFe%2F9Nus0CvSxNRtiB2EUvtf7kK4Kkujvl6EVvyx45JlnZFDGwxrmI%2FdU1RGPcUFjxgr7H5gf95tOXlCUC7WyIH27L6KTuzmLBf4VCKatdpC2IqaIpgec3%2BiMtek17qrxiwcm%2FTczghJR7wnIb23YIiuy8GjnF9tK8kCj2ktFuRJZOLstV08TvBq5p8I%2FdVKXZRtaS%2FgI4ws%2FyhvwY6pgH2592Lw0WJsOV%2FUeQYEy%2FAHpixb79QzD4wG7n2f7Ehkz5303maD0Iucce8%2FaP1O9P8he0nGJ4WjG1xcYyL6BBXFJGK6NKkx38bqt4pdhO9W0ine0U3rb6qmhXWpvCUP3A4ff5Tu0ZU5KGTFiGEJyIYGxiVDuSrcJDdR5teavzYuGUltk76KZNW63SobUlHN7Ez6yTcktzw4ov7TUe7kvDggUsvfxZS&X-Amz-Signature=b804df71a442b5fb095a3cf9687618ae0049d3c350cf9f7731a0b3a1a099299c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/461b9fe5-0f07-4808-8900-af2da1b81f37/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC3HNRNU%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIGuoMpeJEUbQPyuOauVQbHubirD8zzt%2BCrQ9xcDkWvhrAiAa9Dn5uZCL1vOkTpmft5PvBImYoGA1KzKjbChrOA7WACqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3CpLR9Lk3MkeuwE0KtwDDjTx9XxG%2FX6Om21hurg4NHERKWjFf60%2Fm1vUUELPNh5QA5N%2FwAnI21mUn0Rlu%2BUBsolvQTr2WaQyKLJykBHIbeaZhBs8kXFMNU%2FI6gd5Lb%2BGCm1OImKWF%2Fsf81ZfjKVJCzEDf7jJtg884ltwGU0s%2BgVwhArWktlHig5rXC2m96toyHZhv6BMJZodQS6cz0xiLIbcQXBTaTbapfefrMXwY5mHzc7Fds9P1Jbw5c7z1Z9%2FyWhj%2Bm1xrsXq65G9r4XmxAicXOnJzmE%2BcB%2BPWs366qMjudBIfrs%2ByN%2BImTb7RjxwqfXTDpTGH4OcByNOOyriPMcZaxB04dFTnvJLFElrVER%2BnU9xxpktQK5lYulSzEplenlPvOp5yF32FIian%2FHWMLQGjTr7WwEibL99M2PShQmD5aaPmhd3PPQexds4k%2B1T5OrOXwFe%2F9Nus0CvSxNRtiB2EUvtf7kK4Kkujvl6EVvyx45JlnZFDGwxrmI%2FdU1RGPcUFjxgr7H5gf95tOXlCUC7WyIH27L6KTuzmLBf4VCKatdpC2IqaIpgec3%2BiMtek17qrxiwcm%2FTczghJR7wnIb23YIiuy8GjnF9tK8kCj2ktFuRJZOLstV08TvBq5p8I%2FdVKXZRtaS%2FgI4ws%2FyhvwY6pgH2592Lw0WJsOV%2FUeQYEy%2FAHpixb79QzD4wG7n2f7Ehkz5303maD0Iucce8%2FaP1O9P8he0nGJ4WjG1xcYyL6BBXFJGK6NKkx38bqt4pdhO9W0ine0U3rb6qmhXWpvCUP3A4ff5Tu0ZU5KGTFiGEJyIYGxiVDuSrcJDdR5teavzYuGUltk76KZNW63SobUlHN7Ez6yTcktzw4ov7TUe7kvDggUsvfxZS&X-Amz-Signature=90337b7efa819b74cecc18411bc5ef96e68fa45a505dcf31fff46cbc51cb54ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/578ec272-487c-41e1-a17c-3aa0f08a47b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC3HNRNU%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIGuoMpeJEUbQPyuOauVQbHubirD8zzt%2BCrQ9xcDkWvhrAiAa9Dn5uZCL1vOkTpmft5PvBImYoGA1KzKjbChrOA7WACqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3CpLR9Lk3MkeuwE0KtwDDjTx9XxG%2FX6Om21hurg4NHERKWjFf60%2Fm1vUUELPNh5QA5N%2FwAnI21mUn0Rlu%2BUBsolvQTr2WaQyKLJykBHIbeaZhBs8kXFMNU%2FI6gd5Lb%2BGCm1OImKWF%2Fsf81ZfjKVJCzEDf7jJtg884ltwGU0s%2BgVwhArWktlHig5rXC2m96toyHZhv6BMJZodQS6cz0xiLIbcQXBTaTbapfefrMXwY5mHzc7Fds9P1Jbw5c7z1Z9%2FyWhj%2Bm1xrsXq65G9r4XmxAicXOnJzmE%2BcB%2BPWs366qMjudBIfrs%2ByN%2BImTb7RjxwqfXTDpTGH4OcByNOOyriPMcZaxB04dFTnvJLFElrVER%2BnU9xxpktQK5lYulSzEplenlPvOp5yF32FIian%2FHWMLQGjTr7WwEibL99M2PShQmD5aaPmhd3PPQexds4k%2B1T5OrOXwFe%2F9Nus0CvSxNRtiB2EUvtf7kK4Kkujvl6EVvyx45JlnZFDGwxrmI%2FdU1RGPcUFjxgr7H5gf95tOXlCUC7WyIH27L6KTuzmLBf4VCKatdpC2IqaIpgec3%2BiMtek17qrxiwcm%2FTczghJR7wnIb23YIiuy8GjnF9tK8kCj2ktFuRJZOLstV08TvBq5p8I%2FdVKXZRtaS%2FgI4ws%2FyhvwY6pgH2592Lw0WJsOV%2FUeQYEy%2FAHpixb79QzD4wG7n2f7Ehkz5303maD0Iucce8%2FaP1O9P8he0nGJ4WjG1xcYyL6BBXFJGK6NKkx38bqt4pdhO9W0ine0U3rb6qmhXWpvCUP3A4ff5Tu0ZU5KGTFiGEJyIYGxiVDuSrcJDdR5teavzYuGUltk76KZNW63SobUlHN7Ez6yTcktzw4ov7TUe7kvDggUsvfxZS&X-Amz-Signature=85c036599300aedbaa874c4ecae416287f7583e56a2547e56e1978e2945ab6a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e7d7e03-a08b-4932-8307-1f2a23dccc4d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC3HNRNU%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIGuoMpeJEUbQPyuOauVQbHubirD8zzt%2BCrQ9xcDkWvhrAiAa9Dn5uZCL1vOkTpmft5PvBImYoGA1KzKjbChrOA7WACqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3CpLR9Lk3MkeuwE0KtwDDjTx9XxG%2FX6Om21hurg4NHERKWjFf60%2Fm1vUUELPNh5QA5N%2FwAnI21mUn0Rlu%2BUBsolvQTr2WaQyKLJykBHIbeaZhBs8kXFMNU%2FI6gd5Lb%2BGCm1OImKWF%2Fsf81ZfjKVJCzEDf7jJtg884ltwGU0s%2BgVwhArWktlHig5rXC2m96toyHZhv6BMJZodQS6cz0xiLIbcQXBTaTbapfefrMXwY5mHzc7Fds9P1Jbw5c7z1Z9%2FyWhj%2Bm1xrsXq65G9r4XmxAicXOnJzmE%2BcB%2BPWs366qMjudBIfrs%2ByN%2BImTb7RjxwqfXTDpTGH4OcByNOOyriPMcZaxB04dFTnvJLFElrVER%2BnU9xxpktQK5lYulSzEplenlPvOp5yF32FIian%2FHWMLQGjTr7WwEibL99M2PShQmD5aaPmhd3PPQexds4k%2B1T5OrOXwFe%2F9Nus0CvSxNRtiB2EUvtf7kK4Kkujvl6EVvyx45JlnZFDGwxrmI%2FdU1RGPcUFjxgr7H5gf95tOXlCUC7WyIH27L6KTuzmLBf4VCKatdpC2IqaIpgec3%2BiMtek17qrxiwcm%2FTczghJR7wnIb23YIiuy8GjnF9tK8kCj2ktFuRJZOLstV08TvBq5p8I%2FdVKXZRtaS%2FgI4ws%2FyhvwY6pgH2592Lw0WJsOV%2FUeQYEy%2FAHpixb79QzD4wG7n2f7Ehkz5303maD0Iucce8%2FaP1O9P8he0nGJ4WjG1xcYyL6BBXFJGK6NKkx38bqt4pdhO9W0ine0U3rb6qmhXWpvCUP3A4ff5Tu0ZU5KGTFiGEJyIYGxiVDuSrcJDdR5teavzYuGUltk76KZNW63SobUlHN7Ez6yTcktzw4ov7TUe7kvDggUsvfxZS&X-Amz-Signature=5b674276260afe1fb509a11c495d34f79cbfba5d8bc812caa5bc1af50eb1b288&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Prediction Using the Line
Assuming the line is a good fit, it can be used to predict the CO2 emission of an unknown car. For example, for a car with an engine size of 2.4, the predicted CO2 emission is 214.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/26c9b8fd-e224-438c-8bab-1b5558e8d558/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC3HNRNU%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIGuoMpeJEUbQPyuOauVQbHubirD8zzt%2BCrQ9xcDkWvhrAiAa9Dn5uZCL1vOkTpmft5PvBImYoGA1KzKjbChrOA7WACqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3CpLR9Lk3MkeuwE0KtwDDjTx9XxG%2FX6Om21hurg4NHERKWjFf60%2Fm1vUUELPNh5QA5N%2FwAnI21mUn0Rlu%2BUBsolvQTr2WaQyKLJykBHIbeaZhBs8kXFMNU%2FI6gd5Lb%2BGCm1OImKWF%2Fsf81ZfjKVJCzEDf7jJtg884ltwGU0s%2BgVwhArWktlHig5rXC2m96toyHZhv6BMJZodQS6cz0xiLIbcQXBTaTbapfefrMXwY5mHzc7Fds9P1Jbw5c7z1Z9%2FyWhj%2Bm1xrsXq65G9r4XmxAicXOnJzmE%2BcB%2BPWs366qMjudBIfrs%2ByN%2BImTb7RjxwqfXTDpTGH4OcByNOOyriPMcZaxB04dFTnvJLFElrVER%2BnU9xxpktQK5lYulSzEplenlPvOp5yF32FIian%2FHWMLQGjTr7WwEibL99M2PShQmD5aaPmhd3PPQexds4k%2B1T5OrOXwFe%2F9Nus0CvSxNRtiB2EUvtf7kK4Kkujvl6EVvyx45JlnZFDGwxrmI%2FdU1RGPcUFjxgr7H5gf95tOXlCUC7WyIH27L6KTuzmLBf4VCKatdpC2IqaIpgec3%2BiMtek17qrxiwcm%2FTczghJR7wnIb23YIiuy8GjnF9tK8kCj2ktFuRJZOLstV08TvBq5p8I%2FdVKXZRtaS%2FgI4ws%2FyhvwY6pgH2592Lw0WJsOV%2FUeQYEy%2FAHpixb79QzD4wG7n2f7Ehkz5303maD0Iucce8%2FaP1O9P8he0nGJ4WjG1xcYyL6BBXFJGK6NKkx38bqt4pdhO9W0ine0U3rb6qmhXWpvCUP3A4ff5Tu0ZU5KGTFiGEJyIYGxiVDuSrcJDdR5teavzYuGUltk76KZNW63SobUlHN7Ez6yTcktzw4ov7TUe7kvDggUsvfxZS&X-Amz-Signature=1d6a54ff68d03b1db449ab6757d8910e8f697e310db4e5129400f1ca37082a95&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/58b7831d-084a-4eef-bfdf-3cb97ef6723e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC3HNRNU%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIGuoMpeJEUbQPyuOauVQbHubirD8zzt%2BCrQ9xcDkWvhrAiAa9Dn5uZCL1vOkTpmft5PvBImYoGA1KzKjbChrOA7WACqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3CpLR9Lk3MkeuwE0KtwDDjTx9XxG%2FX6Om21hurg4NHERKWjFf60%2Fm1vUUELPNh5QA5N%2FwAnI21mUn0Rlu%2BUBsolvQTr2WaQyKLJykBHIbeaZhBs8kXFMNU%2FI6gd5Lb%2BGCm1OImKWF%2Fsf81ZfjKVJCzEDf7jJtg884ltwGU0s%2BgVwhArWktlHig5rXC2m96toyHZhv6BMJZodQS6cz0xiLIbcQXBTaTbapfefrMXwY5mHzc7Fds9P1Jbw5c7z1Z9%2FyWhj%2Bm1xrsXq65G9r4XmxAicXOnJzmE%2BcB%2BPWs366qMjudBIfrs%2ByN%2BImTb7RjxwqfXTDpTGH4OcByNOOyriPMcZaxB04dFTnvJLFElrVER%2BnU9xxpktQK5lYulSzEplenlPvOp5yF32FIian%2FHWMLQGjTr7WwEibL99M2PShQmD5aaPmhd3PPQexds4k%2B1T5OrOXwFe%2F9Nus0CvSxNRtiB2EUvtf7kK4Kkujvl6EVvyx45JlnZFDGwxrmI%2FdU1RGPcUFjxgr7H5gf95tOXlCUC7WyIH27L6KTuzmLBf4VCKatdpC2IqaIpgec3%2BiMtek17qrxiwcm%2FTczghJR7wnIb23YIiuy8GjnF9tK8kCj2ktFuRJZOLstV08TvBq5p8I%2FdVKXZRtaS%2FgI4ws%2FyhvwY6pgH2592Lw0WJsOV%2FUeQYEy%2FAHpixb79QzD4wG7n2f7Ehkz5303maD0Iucce8%2FaP1O9P8he0nGJ4WjG1xcYyL6BBXFJGK6NKkx38bqt4pdhO9W0ine0U3rb6qmhXWpvCUP3A4ff5Tu0ZU5KGTFiGEJyIYGxiVDuSrcJDdR5teavzYuGUltk76KZNW63SobUlHN7Ez6yTcktzw4ov7TUe7kvDggUsvfxZS&X-Amz-Signature=bac994005c70ed5d5ccfd976bf0d37dd616c851a76b8d5d48e47d4f996722f6d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Calculating $ θ_0 $ and $ θ_1 $
3. **Calculate the Mean:**
	- Calculate the mean of the independent variable ($ \bar{x} $) and the dependent variable ($ \hat{y} $).
4. **Estimate **$ θ_1 $** (slope): **
$$ \theta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} $$
5. **Estimate **$ \theta_0 $** (intercept):**
$$ \theta_0 = \bar{y} - \theta_1 \bar{x} $$
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/771eaaa6-b44a-4958-b185-0146fb685012/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC3HNRNU%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIGuoMpeJEUbQPyuOauVQbHubirD8zzt%2BCrQ9xcDkWvhrAiAa9Dn5uZCL1vOkTpmft5PvBImYoGA1KzKjbChrOA7WACqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3CpLR9Lk3MkeuwE0KtwDDjTx9XxG%2FX6Om21hurg4NHERKWjFf60%2Fm1vUUELPNh5QA5N%2FwAnI21mUn0Rlu%2BUBsolvQTr2WaQyKLJykBHIbeaZhBs8kXFMNU%2FI6gd5Lb%2BGCm1OImKWF%2Fsf81ZfjKVJCzEDf7jJtg884ltwGU0s%2BgVwhArWktlHig5rXC2m96toyHZhv6BMJZodQS6cz0xiLIbcQXBTaTbapfefrMXwY5mHzc7Fds9P1Jbw5c7z1Z9%2FyWhj%2Bm1xrsXq65G9r4XmxAicXOnJzmE%2BcB%2BPWs366qMjudBIfrs%2ByN%2BImTb7RjxwqfXTDpTGH4OcByNOOyriPMcZaxB04dFTnvJLFElrVER%2BnU9xxpktQK5lYulSzEplenlPvOp5yF32FIian%2FHWMLQGjTr7WwEibL99M2PShQmD5aaPmhd3PPQexds4k%2B1T5OrOXwFe%2F9Nus0CvSxNRtiB2EUvtf7kK4Kkujvl6EVvyx45JlnZFDGwxrmI%2FdU1RGPcUFjxgr7H5gf95tOXlCUC7WyIH27L6KTuzmLBf4VCKatdpC2IqaIpgec3%2BiMtek17qrxiwcm%2FTczghJR7wnIb23YIiuy8GjnF9tK8kCj2ktFuRJZOLstV08TvBq5p8I%2FdVKXZRtaS%2FgI4ws%2FyhvwY6pgH2592Lw0WJsOV%2FUeQYEy%2FAHpixb79QzD4wG7n2f7Ehkz5303maD0Iucce8%2FaP1O9P8he0nGJ4WjG1xcYyL6BBXFJGK6NKkx38bqt4pdhO9W0ine0U3rb6qmhXWpvCUP3A4ff5Tu0ZU5KGTFiGEJyIYGxiVDuSrcJDdR5teavzYuGUltk76KZNW63SobUlHN7Ez6yTcktzw4ov7TUe7kvDggUsvfxZS&X-Amz-Signature=95746c9b0744a6039ebed9dd336e92b3270e6da53d8ddb199e8479c3b929c24c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cc20ddcb-2279-4e79-bcfe-8205d0fa76e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MQNWSOS%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCh2Jr9iOPUvgWcVlKR019sMfB4%2BlAL7zFPLGi017tMEQIgLOu9hLNO%2BccJK%2BcxYdIgXzaSx60I91W1Ng8YHTUGqi0qiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMP4w9TrOdMj%2F%2BTfKSrcAxNRgcywyxHjqtH77B0agcVYp39ZFtTI0jcTTghrdkvDulLoH2bH7FZdDw5q61kccY0EI9QvJAr1elYyvQE2TqlL1dwiocwD1kHl%2FTzrBB93xJ0hi95PL%2BB3%2B3Ji16%2BhF6bvVh4NwB8%2FJMPsUeekb4ff78HlTM4r9AF9W8o3y0EYRFXjDgxfFMTskWRZfNTq2hTRhalG2dc%2B9uIsU9xggt2f2jwVzbEwe%2FsmjFnl9Hy%2FE%2FJlnHr1imHa1Rdnud4ySb8zoIn0jerPWRHPbcM94i7qMobhxB%2FzRX7l6d8eg%2BH31YZ7yMumNUkjzYDgZR461F6sdlrCSQQo4mjdhAT%2FfWAYCfjJggP4IOiew4CladP6XRZY5Zz4OOvqpg2Yp8XDE2J2qZSVfzC0oN3ANnjfbgXO4q%2BPkOKYgwfi49tQOXz8j7UIy444Py068O9rUkznV%2BNRPhAKuDoQy6oBm5xAOdNd%2FrDiAaV9jH%2BJVngCiBHWgiHrvmNbIsDAwN0QDfpcxCSaAlRLgC6JS%2F%2BUspevYKXl3YeNlLAraSUdL2c7BXpCntzhXQG%2FnRHMRyju5jpJQcDqqingVVy6OpF5xvK9oPxzZ8lUW4%2Bfg0JmBESMconcPq8W0TRBerZeIVntMJr8ob8GOqUBb5vx3FCgruBVIVa4f118HyNXt%2BB%2B0%2F0UWWeTCE2qcasiIH%2Fd7rE7nLT45TgwcS0rSGInUPSaKTVDplVU2KwxeFwXR0uRfxpbGMlJJovex6fAiOKiWMOY9UNK%2F0ubElR2PYzjK0UUypaHiUHXQz%2FBY6J%2F7J3f3Z6MQckIA4J2bA85u6Zl5q1BkUFDTvVhvpcS8OZw4Ccz7SlD2GHn9ROWr4BfNFEb&X-Amz-Signature=72f3e6115cc91a6a7a362c230f82e1c8fee9177ace48d2d30bd7a7cb7c458c9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ee9c0838-a391-45b2-a788-d0c8854fbdee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQ6MRKFH%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCICgA6E%2Fv5SHfQQ6Ft7fm3GRWftqFnvZvp2HzBhrgFiBXAiEAplqFPI6mlxbzTzSuI4TDhQZps67rUGeoNYXn3B0jWZMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOyd7zVzIIX2vlk89SrcAxlUHYiyNSqd7RKAppW7r6uvutpVmZDZskxDG%2FiAkn6t%2FNkq53udqecgAPkSDkM%2FuAgbsK0tdjci%2FsKYnqqtu2Ot4QveCXOBMDArG3loNDvnl1zGFOoYFOAwBiJ1v7uOXqmkhvEao0It0mtIjqjAPK9emVIYU5MZXm2TNvBpSdrXNSnv1XDgFOQqQfM%2FkXOlbzWZ8j7HiZYcuYp4i46qpZI1jxeaCE6mbnYaK0gjr%2B78pi5x9hIlBcaoxn5bt9Efy4nkGKSBy%2BwdpmaI%2FfdZFXaPCmen0Xv9%2FEf00SrHPcqqTOYKdoXsjq%2Fg0OgS59V7iz8NHpz5MxxvyCEQ3yWTI%2BMBGo6B2R%2BcJCcafiqV%2FfVNbG6PUwNcyr9Xb6J40etV4BYe6OPzsUq%2FwAvE4ZfSmXcYsR6saGkY24J42lpSNsxIoxkGCxINIO0GhwGU%2F1slUgsdFr62LnCv9fckHpIsydHkEwJUZhvUd01z0FnABMGOKLboNgBDZmJSwOkEikUq14%2FbsgnbCGyd0Ry9m%2F2ZRHHIkPZY0LmMohTkVqMwLLzqeuC8KdXlfRvUu5G8uTS7wYb64GFKGvSULsGmCXHeLmcGrXy48hK2azsc1yCa1KUQ%2F3lbFLMOBB5s9ho2MMv8ob8GOqUB02%2BXTfFBC%2FV%2Fk8cCum10gbfo3OhGJI2owVfe6UpSw302COYd0ULESeJqwEcXPXmeRnp9hE%2BgJfbh%2F6hdRYPUdIV54QYu8huhNvFErIrBPkYIB53TwrdxMKmb93AtZMKtcwoxGgHzYtw5ZU2%2FumQCTWRBrCM9Bvs9mLVJiWs4nxAASZt2gVB6KHIdotr2nUEMNORvg6DVS8JfzT%2FFxuScXztCWD8T&X-Amz-Signature=7b7ae26948c5fedd6a1a53dd406313cca3680cfaf0451aa0ad067c036b01d097&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/daf007d4-8db8-4c38-bf21-80ebc37f3976/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664PKRDP2%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIEUQuBRV8g1PKDsVuODC8erA5Q8HDzXnVvnvjNnna13SAiEAtI5LqXrrcpZIWEz7n3kPDhwjmAD0vm3qN%2FXJoQMZY6sqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAPwgBrdfDcUdqnYPircAw7LzVx4lEf6uHq9FFAVEMB0KVI43TUKHqpDcFi0hsQ3lOQsH0rMBrJjreaunpCS9GGCJt542nHPwn9mU8xmWypZgqK2rKqNC7%2FR%2BEdafbc51zo8DNHaaEsSuRbmyaUWON16j%2BeUhY1Mv4DlgDRwppPYqE09AAdVln7f42220PAp8uicC0bikLeGgjhm%2BzngnLNJ%2BcRdODtMIMuoh0iG2HEekM1X0POnyg2O4CrrCRlvWQjkBoEGPIdQFlHqmMsE%2BIVpmIYaZxQlhVcvarKAxUur1vwX5HWLLBan5epI54zm30kgKmDWDAyqTQ%2Bf5URui3mQCquUKFn8aYKMnk8BUOmrVgS5g2hcMXMjSc2OyHmmM1D2ISNHXH%2BUN1T9IFjEMSHCYSAs3CZSee8ik3PAeGGkQ7XjNWCX5j57JTcfYwXuo6%2B14HeEcKxLhTfl1KATX3%2BOf71ZJzwBNAmxk6ErOJjU1CnF1GcxqfnAE9Cd06xiqw6MgRYV4eDFEJpHF%2BGlnDzlaEdHIp6WdhIU9LGDdFQ1U%2FkgBnjhLzkMvr%2F10lZfYXQeMhu0rgke%2BnVFapj2QLzBh6sf4bl%2FoEUc30b%2FocyZhi6MZzFubPldubtpW%2FGg8wrnswmpTE7oPmR%2FMMn8ob8GOqUBd48wzK%2Fkv6dUumQ%2BVc1rfrqQ3S1ynLr1d%2F%2B3%2Bz5Hr4iHLu8hWSLn8vBViBqZ768OX%2F9JqkyJg83XjCxBm90XaSc2z81G7BqDgomWotnbJxkJx81irqF8DY7g9SmzXt1rIMnCqr7CyJQgC1B5t1tGB%2FAJPSkwOjX8pRz1kgwk%2FuWu37396AtEMvsuwZYdslvtHvwgQH5BS%2BgRP4u%2FIy9dkYmZUC2%2F&X-Amz-Signature=10eb6e15fd6bd92e16cb3fcccb405d395b9dcaa38594b7d8d4bcdaa0bb3cf9bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/97c57813-1dc2-4a92-93ef-7edea66e3447/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664PKRDP2%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIEUQuBRV8g1PKDsVuODC8erA5Q8HDzXnVvnvjNnna13SAiEAtI5LqXrrcpZIWEz7n3kPDhwjmAD0vm3qN%2FXJoQMZY6sqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAPwgBrdfDcUdqnYPircAw7LzVx4lEf6uHq9FFAVEMB0KVI43TUKHqpDcFi0hsQ3lOQsH0rMBrJjreaunpCS9GGCJt542nHPwn9mU8xmWypZgqK2rKqNC7%2FR%2BEdafbc51zo8DNHaaEsSuRbmyaUWON16j%2BeUhY1Mv4DlgDRwppPYqE09AAdVln7f42220PAp8uicC0bikLeGgjhm%2BzngnLNJ%2BcRdODtMIMuoh0iG2HEekM1X0POnyg2O4CrrCRlvWQjkBoEGPIdQFlHqmMsE%2BIVpmIYaZxQlhVcvarKAxUur1vwX5HWLLBan5epI54zm30kgKmDWDAyqTQ%2Bf5URui3mQCquUKFn8aYKMnk8BUOmrVgS5g2hcMXMjSc2OyHmmM1D2ISNHXH%2BUN1T9IFjEMSHCYSAs3CZSee8ik3PAeGGkQ7XjNWCX5j57JTcfYwXuo6%2B14HeEcKxLhTfl1KATX3%2BOf71ZJzwBNAmxk6ErOJjU1CnF1GcxqfnAE9Cd06xiqw6MgRYV4eDFEJpHF%2BGlnDzlaEdHIp6WdhIU9LGDdFQ1U%2FkgBnjhLzkMvr%2F10lZfYXQeMhu0rgke%2BnVFapj2QLzBh6sf4bl%2FoEUc30b%2FocyZhi6MZzFubPldubtpW%2FGg8wrnswmpTE7oPmR%2FMMn8ob8GOqUBd48wzK%2Fkv6dUumQ%2BVc1rfrqQ3S1ynLr1d%2F%2B3%2Bz5Hr4iHLu8hWSLn8vBViBqZ768OX%2F9JqkyJg83XjCxBm90XaSc2z81G7BqDgomWotnbJxkJx81irqF8DY7g9SmzXt1rIMnCqr7CyJQgC1B5t1tGB%2FAJPSkwOjX8pRz1kgwk%2FuWu37396AtEMvsuwZYdslvtHvwgQH5BS%2BgRP4u%2FIy9dkYmZUC2%2F&X-Amz-Signature=f8e088c86eb34a68e28a865c94f79d488b5bcc66ec1e60db30e0986ee4ea226c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
